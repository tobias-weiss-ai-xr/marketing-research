---
title: Climate Variability Modulates the Impact of Price Spikes on Food Insecurity
url: https://arxiv.org/abs/2609.24394
category: ai-marketing
subcategory: measurement
date: 2026-09
venue: ''
authors:
- Jordi Cerdà-Bautista
- Vasileios Sitokonstantinou
- Homer Durand
- Gherardo Varando
- Michele Ronco
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.24394
pages: 49
chars: 114235
fetched_at: '2026-11-08T13:25:10+00:00'
kb_version: 1
---

# Climate Variability Modulates the Impact of Price Spikes on Food Insecurity

Climate Variability Modulates the Impact of
Price Spikes on Food Insecurity
Jordi Cerd` a-Bautista1*, Vasileios Sitokonstantinou2, Homer
Durand1, Gherardo Varando1, Michele Ronco 3 and Gustau
Camps-Valls1
1Image Processing Laboratory , Universitat de V al` encia, V al` encia, Spain.
2Artificial Intelligence Group, W ageningen University & Research, W ageningen, The Netherlands.
3Joint Research Centre, European Commission, Ispra, Italy .
*Corresponding author(s). E-mail(s): jordi.cerda@uv.es;
Abstract
Climate variability influences whether a market disruption escalates into
a food crisis, yet broad climate patterns like El Ni˜ no, tracked months
before they alter hydro-climatic conditions, are still not incorporated as
an early-warning component in food-security responses. We address this
gap by introducing sensitivity regimes—a stratification of regions by the
direction and strength of their vegetation response to the El Ni˜ no South-
ern Oscillation—and using them to estimate how food price spikes affect
acute food insecurity across sub-Saharan Africa. Integrating remote sens-
ing, socioeconomic data, and causal machine learning, we find that in
regions where ENSO systematically suppresses vegetation, a price spike
raises the share of the population at acute risk by 5.4 percentage points
in the following month. In regions where vegetation is unaffected by or
positively linked to ENSO, the estimated effect is smaller (around 2 per-
centage points) and statistically insignificant. These results demonstrate
that climate context is critical for understanding food security vulnera-
bilities. Sensitivity regimes can be combined with operational price-spike
triggers to stage anticipatory action: the ENSO state flags vulnerable
regions months ahead, and a pre-positioned response in those regions
to a price spike would avert the largest jump in acute food insecurity.
Keywords:Food insecurity, price spikes, Africa, causal inference, conditional
average treatment effect, evidence-based policy-making
1
arXiv:2609.24394v1  [cs.LG]  21 Sep 2026

2Climate Variability Modulates Price-Spike Impacts
Introduction
Food insecurity remains a pressing global issue, especially in sub-Saharan
Africa, where food systems are increasingly strained by food price spikes,
climate variability, and geopolitical instability. According to United Nations
estimates, more than 250 million people in Africa are exposed to severe food
insecurity, and many additional individuals are at risk as a result of climate
change, economic instability, and persistent conflicts 1. Gaining a nuanced
understanding of the context-specific drivers of food insecurity is essential
to crafting effective policies that bolster resilience and foster sustainable
development.
One of the primary drivers of food insecurity is short-run food price spikes,
which reduce household purchasing power and can rapidly force changes in
consumption and coping strategies 2,3,4,5,6. In operational early-warning sys-
tems, food price spikes refer to episodes in which staple prices rise abnormally
relative to their expected seasonal pattern. However, the effects of food price
spikes are not uniform: they depend on local climatic conditions, agricultural
production systems, market structure, and household vulnerability7,8,9. Recent
research has highlighted the need to account for these contextual factors when
assessing the impact of food price spikes on food security outcomes 10,11. When
ecosystem and agrosystem conditions for crop production are unfavorable,
households often have weaker buffers (e.g., lower agricultural income, reduced
own production, and diminished seasonal labor demand). Hence, an abnormal
increase in staple prices is more likely to push them into crisis-level coping.
When agroclimatic conditions are more favorable, households may be better
able to absorb price abnormalities, leading to a smaller marginal impact on
acute food insecurity 12,13,14,15,16,17. Here, we investigate whether the effects
of food price spikes on acute food insecurity can be quantified and how they
vary across different climatic contexts.
Climate teleconnections—large-scale anomalies that alter local rainfall,
vegetation, and agricultural conditions with a seasonal delay—are a key
part of this context. A well-known example is El Ni˜ no Southern Oscilla-
tion (ENSO): tropical Pacific sea-surface temperature anomalies propagate
through atmospheric circulation and systematically influence African hydro-
climate and vegetation with seasonal lags of about 1–3 months, varying by
region, season, and whether transmission is mediated by rainfall or soil mois-
ture 18,13,19,20,21,22,23. This delayed response matters for food security because
shifts in harvest prospects, incomes, and coping capacity unfold before price
stress materialises. Unlike static agroclimatic zones, ENSO-sensitive regions
identify where a remotely observed climate signal is likely to translate into
local vulnerability with lead time, providing a natural early-warning layer for
anticipatory action before market stress escalates into acute food insecurity.
We present an analytical approach that estimates the effect of food price
spikes on acute food insecurity—explicitly conditioned on vegetation sen-
sitivity, as observed through the Normalized Difference Vegetation Index
(NDVI)—to ENSO. Our approach proceeds in three integrated stages, as

Climate Variability Modulates Price-Spike Impacts3
10
5
0
5
Negative Regime
Weak Regime
Positive Regime
Causal Effect (%)
1.0
0.5
0.0
1.0
0.5
0.0
1.0
0.5
0.0
Jan
2021
Jul
Jan
2022
Jul
Date
rCSI
Price Spike
rCSI
Price Spike
rCSI
Price Spike
Jul
Positive Regime: Lamu (KEN)
Weak Regime: Ségou (MLI)
Negative Regime: Midlands (ZWE)
Jan
2023
71
64
87
N
Regions
238
378
229
N
Price
Spikes
0
50
100
50
Positive Influence
Weak Influence
Negative Influence
1. Extract dominant climate signals
2. Characterize regions by climate
sensitivity
3. Estimate the heterogeneous causal
effects
3
2
1
0
1
Jan
2013
Jul
Jan
2014
NDVI Harare (ZWE)
NDVI Lamu East (KEN)
NDVI Banamba (MLI)
ENSO 3.4
Jul
Jan
2015
Date
Jul
Jan
2016
Jul
Fig. 1:Proposed analytical pipeline.The workflow begins by extracting
the dominant ENSO-linked vegetation signal, then stratifies regions by sen-
sitivity regimes, and concludes with the estimation of causal effects averaged
within each regime. The time-series plots show examples from Kenya, Mali,
and Zimbabwe.
shown in Figure 1. First, we extract the dominant ENSO-linked mode of vege-
tation variability by combining NDVI time series with the Ni˜ no 3.4 index and
isolating the NDVI component that is temporally driven by ENSO24,25,26. Sec-
ond, we use this ENSO-linked vegetation signal to definesensitivity regimes:
areas where ENSO is associated with systematically negative, positive, or weak
vegetation responses. These regimes do not summarize average climate condi-
tions; rather, they capture how strongly and in which direction local vegetation
responds to ENSO. This differs from static agroclimatic zones, which summa-
rize long-run mean conditions but not dynamic sensitivity to the climate driver.
Third, we estimate the causal effect of a price spike within each regime, thereby
identifying policy levers that can be toggled before a crisis occurs, which is
aligned with early-warning decision needs 27,28 (see theMethodssection for
details). By conditioning on these sensitivity regimes, we capture context-
specific causal impacts, moving beyond average treatment effects to provide a
more granular and nuanced assessment of food security risks 29,30,31,32,14.
Leveraging remote sensing data, socioeconomic indicators, and causal
machine learning, our analysis offers a novel approach to understanding how
food price spikes affect food security under climate variability across a wide
area of sub-Saharan Africa. More broadly, it shows how sensitivity regimes can
be combined with price-spike triggers to create an early warning system where
pre-positioned responses in vulnerable regions to those price spikes would avert
the largest jump in acute food insecurity.

4Climate Variability Modulates Price-Spike Impacts
ENSO
Crop Drivers
SPI-3, Soil Moisture, Rainfall,
Temperature, FPAR
Economic Drivers
Market Prices, GDP
Social Drivers
Population, Conflicts,
Displacements
Food Price Spikes
Treatment T (ALPS)
Food Insecurity
Outcome Y (rCSI)
Causal Effect Direct Edges  Additional Edges Heterogeneity
NDVI
Fig. 2:Directed acyclic graph (DAG) representing key determinants
of food security in Sub-Saharan Africa and their interactions.ALPS
serves as the treatment, while rCSI represents the outcome of interest. The
Food Price Spikes→Food Insecurity arrow indicates the causal relationship
under investigation. The directed edges represent hypothesized dependencies
derived from domain knowledge and the literature.
Results
The multivariate food insecurity problem
Food systems in sub-Saharan Africa are complex, nonlinear, and heavily
impacted by climate variability. A causal analysis, therefore, requires both
explicit modeling assumptions and a transparent representation of how these
drivers may jointly influence exposure and vulnerability. Figure 2 shows the
directed acyclic graph (DAG) adopted here, grounded in expert knowledge
and prior evidence on climate–vegetation dynamics 33,34, conflict and displace-
ment 35, market stress, and food security outcomes 36,37. The DAG serves both
as a conceptual model of food-system vulnerability and as a guide for selecting
adjustment variables in treatment-effect estimation.
In our study, the treatment of interest is above-normal food price con-
ditions, captured by the Alert for Price Spikes (ALPS) indicator 38, and the
outcome is acute food insecurity measured as the share of the population with

Climate Variability Modulates Price-Spike Impacts5
a reduced Coping Strategy Index (rCSI) 39 in crisis or worse. This outcome is
designed to reflect short-term stress in households’ ability to access food and
is therefore responsive to changes in market conditions.
The DAG doesn’t capture every mechanism; it makes explicit which factors
drive both treatment and outcome. Its key message is that price stress rarely
occurs in isolation. Large-scale climate variability, including ENSO-related
teleconnections, influences local agroclimatic conditions such as rainfall, tem-
perature, and soil moisture, which shape vegetation and production conditions
and can contribute to market pressure 40,41. At the same time, conflict and
displacement disrupt livelihoods and markets, increasing the likelihood of
abnormal prices and reducing households’ capacity to cope. Broader economic
conditions and demographic structure further shape exposure and vulnera-
bility 42. Our empirical analysis compares observations with similar climate,
conflict, displacement, economic, and demographic conditions to estimate how
food price spikes are followed by changes in rCSI. This makes our central
questions concrete:
How much do spikes in food prices amplify acute food insecurity in the fol-
lowing month? How does this effect vary across sensitivity regimes?
The assumed DAG is an abstraction of the system. In reality, food systems
involve feedback across time: for example, price spikes can affect displacement
and livelihoods, which may later feed back into market conditions. Captur-
ing these dynamics would require an explicitly time-unrolled causal model,
whereas the DAG in Figure 2 is acyclic by construction and is a necessary
assumption for applying causal inference methods. We partially reduce con-
temporaneous simultaneity by using a one-month lead of the outcome and
discuss remaining limitations in theDiscussionsection, and, inAppendix A
of theSupplementary Material, we report the justifying literature for each
causal link. Finally, to quantify any sensitivity to the one-month lead timing
choice, we re-estimate the effects across different leads inAppendix Eof the
Supplementary Material.
Sensitivity regime stratification for causal impact
analysis
Climate variability is a major determinant of food insecurity, and ENSO is
among the most important large-scale modes shaping African rainfall and veg-
etation through teleconnections that operate with seasonal lags 18,13,19. This
makes ENSO especially relevant for early warning, since tropical Pacific con-
ditions can signal where vegetation and production are likely to deteriorate

6Climate Variability Modulates Price-Spike Impacts
0
50
100
50
Positive Influence
Weak Influence
Negative Influence
PC1
Fig. 3:Geographical distribution of sensitivity regimes based on
GPCA stratification.(Left) First PC of the GPCA analysis on ENSO–
NDVI, providing a continuous map of the causal influence. (Right) Regions
classified as Positive, Negative, or Weak based on the strength and direction
of ENSO–NDVI causal linkages.
months later. NDVI is widely used to monitor these responses, but inte-
grating such high-dimensional, noisy signals into causal effect estimation is
challenging 20.
We address this with Granger PCA (GPCA) 26, a particular instance of
Direct Effect Analysis 43, which combines NDVI time series with the ENSO
index to extract the dominant components of vegetation variability causally
driven by ENSO. The output is a set ofsensitivity regimesregions where the
ENSO anomaly is systematically associated with negative, positive, or weak
vegetation responses that move beyond static agroclimatic zones based on
long-run averages.
Figure 3 shows the resulting map.Negativeregions, where ENSO is asso-
ciated with systematically worse vegetation conditions, broadly align with
known drought-prone belts.Positiveregions correspond to areas with more
favorable vegetation conditions, typically zones of more reliable rainfall under
the relevant teleconnection states. TheWeakregime groups regions with a
small or mixed ENSO imprint and acts as a buffer between the other two.
The regimes thus capture where vegetation is more or less sensitive to a
remote driver, not simply where average climates are dry or wet. Implemen-
tation details are in theMethods; robustness to threshold choices and pixel
subsampling is reported inAppendix Bof theSupplementary Material.
Sensitivity regimes modulate the causal effect
Our analysis covers 222 administrative level-1 (ADM1) regions observed
over 42 months, from September 2020 to February 2024: 71 regions in the Neg-
ative regime, 64 in the Weak regime, and 87 in the Positive regime (see the

Climate Variability Modulates Price-Spike Impacts7
T able 1:Conditional Average T reatment Effect (CA TE) estimates
for ALPS impacts on rCSI, stratified by sensitivity regimes.Confi-
dence intervals are reported at the 95% level.
Model Regime CA TE (p.p.) C.I. p-value
Negative 6.00 (2.57, 8.73) 0.020
Linear DML Weak 1.94 (-0.47, 4.99) 0.098
Positive 2.16 (-3.92, 4.21) 0.784
Negative 5.35 (2.16, 8.08) 0.020
Causal Forest DML Weak 1.80 (-0.47, 4.75) 0.137
Positive 1.70 (-3.70, 4.15) 0.922
MethodssubsectionsDataandData Preprocessing). Within this panel, we esti-
mate Conditional Average Treatment Effects (CATEs) of above-normal food
price stress on acute food insecurity using two Double Machine Learning esti-
mators: Linear DML and Causal Forest DML. The treatment is defined from
the ALPS indicator over a three-month window and contrasts normal food
price conditions with above-normal conditions (Stress, Alert, or Crisis). The
outcome is the regional monthly prevalence of acute food insecurity, measured
as the share of the population with rCSI in crisis or above.
The main result is that the impact of a food price spike depends on climate
context (Table D13). In regions where ENSO tends to suppress vegetation con-
ditions (Negative regime), a price spike is followed by an increase of about 5.4
percentage points (p.p.) in the share of the population experiencing crisis-level
coping. In regions where ENSO effects on vegetation are weak or favorable, the
estimated increases are much smaller, around 2 p.p., and are not statistically
distinguishable from zero. This pattern is consistent with a vulnerability-
amplification mechanism. When teleconnected climate conditions repeatedly
erode vegetation and production, households enter market-stress episodes with
fewer buffers, so the same food price spike translates into a larger increase in
acute food insecurity.
To ensure that a single modeling choice does not drive this regime pattern,
we compare the DML results with simpler baselines: a difference-in-means
estimator, a fixed-effects regression, and a propensity score weighting model.
All methods recover the same qualitative ordering, with the largest effects
concentrated in the Negative regime (seeAppendix Dof theSupplementary
Material).
Across outcome leads from 0 to 4 months (Appendix E), the Negative-
regime effect remains of similar magnitude and statistically distinguishable
from zero, whereas Weak-regime estimates remain small and imprecise. In
the Positive regime, estimates are near zero at short horizons and become

8Climate Variability Modulates Price-Spike Impacts
50
40
30
20
10
0
Negative Regime Weak Regime Positive Regime
Baseline risk (T=0)
Added risk (CATE)
Risk of acute food insecurity (%)
Fig. 4:Baseline risk of acute food insecurity under normal food price
conditions and added risk when prices spike.Estimations provided by
the Causal Forest DML CATE estimates stratified for the sensitivity regimes.
negative at longer leads; given the observational design and possible differ-
ences in seasonality and market integration, we interpret this sign change
cautiously as suggestive of different timing or recovery dynamics rather than
evidence for a specific mechanism. Pairwise contrasts between regimes follow
the expected ordering but are generally not statistically distinguishable from
zero (Appendix F). The strongest robust conclusion is therefore that food
price spikes have a measurable short-run effect in drought-prone Negative-
regime areas, with a directional gradient consistent with the vulnerability-
amplification mechanism, but only partially supported by formal pairwise
tests.
The regime pattern is most intuitive when viewed alongside the baseline
vulnerability under normal food-price conditions (Fig. 4). Regions in the Neg-
ative regime already face the highest baseline prevalence of crisis-level coping.
A price spike then adds a larger marginal increase on top of an already elevated
baseline, pushing more households past critical thresholds. To translate this
effect into population terms, we use the median total population across ADM1
regions and the nonlinear estimate for the Negative regime. An ADM1 with a
population of approximately 1.32M corresponds to roughly 70,600 additional
people in crisis or worse in the following month (95% CI: 28,500 to 106,700).
In weaker or more favorable ENSO–sensitivity contexts, baseline risk is lower,
and the marginal effect is smaller and statistically indistinguishable from zero.
Taken together, these results suggest that sensitivity regimes provide a prac-
tical vulnerability lens for early warning: they help identify where an episode
of market stress is most likely to translate into acute food insecurity.

Climate Variability Modulates Price-Spike Impacts9
                             Food Price Index
       Conflict Stock Displacement
           Mean Temperature (Crop)
 Urban Population (Cluster)
 Rural Population
 IDP Inflows (6m)
 GDP Growth
 Urban Population (Centre)
 Mean FPAR (Crop)
 Mean Rainfall (Crop)
                                 ACLED Fatalities
 Mean SPI-3 (Crop)
 Mean Soil Moisture (Crop)
                                   UCDP Deaths
0.02
0.00
0.02
Negative Regime
Weak Regime
Positive Regime
0.04
0.06
0.08
0.10
0.12
0.14
Permutation importance
Drivers of Exposure (ALPS)
GDP Growth
 Mean Rainfall (Crop)
 Mean SPI-3 (Crop)
 Mean FPAR (Crop)
 Food Price Index
 Mean Temperature (Crop)
 Rural Population
 Urban Population (Centre)
Conflict Stock Displacement
Urban Population (Cluster)
 Mean Soil Moisture (Crop)
 ACLED Fatalities
 IDP Inflows (6m)
 UCDP Deaths
0.02
0.00
0.02
Negative Regime
Weak Regime
Positive Regime
0.04
0.06
0.08
0.10
0.12
0.14
Permutation importance
Drivers of Vulnerability (rCSI)
Climate
Economic
Social
Climate
Economic
Social
Fig. 5:F eature importance of the nuisance models.Estimations of the
treatment (top) and outcome (bottom) for the Causal Forest DML estimator
stratified for the sensitivity regimes.
Context-specific drivers guide the effect identification
As part of the DML procedure, we model both the treatment assignment
mechanism (exposure to food price spikes) and the outcome regression (vul-
nerability to acute food insecurity) using machine learning models. Figure 5
summarizes which covariates carry the most predictive signal for these two
tasks across sensitivity regimes. Covariates fall into three broad domains sum-
marized in the causal graph (Fig. 2): Climate, Economic, and Social. For
further information, see theMethodssection and Table A1 (Appendix A).
The main message is that the variables that best explain exposure are not
the same as those that best explain vulnerability, and their relative importance
shifts across ENSO–sensitivity contexts. Exposure is more strongly associated
with market and disruption metrics, such as price indices, displacement, and
population structure, whereas vulnerability places greater weight on macroe-
conomic and agroclimatic conditions, as well as conflict/displacement. These
feature importances are predictive diagnostics rather than causal attributions.

10Climate Variability Modulates Price-Spike Impacts
Discussion
We quantified how food price spikes affect acute food insecurity across
distinct sensitivity regimes in sub-Saharan Africa, treating climate not as a
control variable but as a source of structured heterogeneity. By defining regimes
from ENSO–sensitivity teleconnections rather than static agroclimatic zones,
we capture dynamic vulnerability to a remote driver that is monitored months
in advance, providing a basis for anticipatory action rather than retrospective
adjustment 17.
The geography of the sensitivity regimes recovers well-known ENSO–
rainfall–vegetation patterns: Negative regions concentrate in semi-arid,
drought-prone zones of the Horn and South-Eastern Africa, where El Ni˜ no con-
ditions typically reduce rainfall and vegetation greenness13,19,20, while Positive
regions overlap areas where ENSO anomalies coincide with wetter conditions
and greener vegetation 18,20. The regime-specific effects we estimate are also
consistent with documented food-crisis episodes: the 2015–2016 El Ni˜ no pro-
duced severe drought and elevated food assistance needs across Southern Africa
and parts of the Horn 44,45, the areas falling into our Negative regime, where
we estimate the largest CATEs and the highest baseline risk. East African
regions where El Nio tends to bring above-average rainfall map mainly to the
Positive regime, where smaller but positive CATEs are consistent with favor-
able agroclimate, partially attenuating price-spike impacts even under market
stress 32,14.
Across both linear and nonlinear estimators, the Negative regime consis-
tently shows the largest effect, around 5.4 p.p., with Weak and Positive regimes
near 2 p.p. (Table D13). The Negative-regime effect is statistically distinguish-
able from zero in both estimators and stable across outcome leads, indicating
that the clearest, most robust short-run impact of price stress is concentrated
in drought-prone, ENSO-sensitive regions. Evidence for between-regime dif-
ferences is weaker than evidence for a non-zero effect within the Negative
regime: point estimates follow the expected ordering (Negative>Weak∼Pos-
itive), but pairwise contrasts are statistically distinguishable from zero only
in the linear case for the Negative–versus–Positive comparison (Appendix F).
We therefore conclude that food price spikes have a measurable short-run
impact in the Negative regime, but the broader gradient across regimes can-
not be confirmed through statistical testing. The positive point estimate in
the Weak regime informs that, where local production is not strongly ENSO-
sensitive, households remain exposed through market channels–dependence on
purchased staples, price transmission, and conflict- or displacement-related
disruptions 11,7.
Substantively, regions in the Negative regime exhibit the highest baseline
prevalence of crisis-level coping even under normal price conditions, so a price
spike adds a larger marginal increase on top of an already elevated baseline,
pushing more households across acute-insecurity thresholds. This is consistent
with food-system risk architectures in which hazards, exposure, and vulner-
ability interact rather than operate independently 36,37,40,41: climate does not

Climate Variability Modulates Price-Spike Impacts11
directly determine food insecurity but shapes the conditions under which a
market shock becomes more damaging.
From a policy perspective, these findings argue against treating the impact
of price spikes as a single, uniform number. In the Negative regime, where
both baseline risk and marginal effects are high, price-based triggers can
be combined with ENSO-informed seasonal outlooks to pre-position assis-
tance, reinforce social protection, and stabilize staple markets before conditions
worsen. In the Weak regime, monitoring may need to focus more strongly
on conflict, displacement, and market-transmission channels. In the Positive
regime, longer-term resilience and agricultural investments may be more rel-
evant, while maintaining attention to conflict-affected or highly urbanized
pockets.
Several limitations should temper interpretation. Identification relies on
conditional unconfoundedness: informal transfers, local safety nets, targeted
aid, and subnational policy responses are not directly observable, and fixed
effects can reduce but not eliminate this concern. The Stable Unit Treat-
ment Value Assumption (SUTV A)46,47 is unlikely to hold exactly: prices are
transmitted across markets, and conflict and displacement spill over borders,
so estimates should be read as within-panel direct-plus-spillover effects, with
attenuation toward zero most likely in regimes where market integration is
high (one plausible reason non-Negative effects are smaller and less precise).
Our climate stratification focuses on ENSO; other remote modes (e.g., the
Indian Ocean Dipole) and local extremes (floods, heatwaves) are not explic-
itly represented. Finally, both ALPS and rCSI are operational indicators with
measurement error, so our estimates concern the causal effect of ALPS-defined
price stress on harmonized rCSI outcomes, not an abstract true price spike on
perfect food security.
The framework is modular and extensible to other climate drivers, out-
comes, or interventions. Substantively, the results highlight a double burden
in the Negative sensitivity regime: higher underlying vulnerability and sharper
deterioration when prices become abnormal. By using sensitivity regimes as a
stratification layer, we show that the short-run food-security impact of price
stress is most pronounced in drought-prone regions and smaller elsewhere—
a climate-aware perspective for integrating remote climate information into
food-security analysis and developing more targeted, anticipatory responses in
an era of rising climatic impact, political unrest, and economic volatility.
Methods
Data
This study uses the Harmonized Food Insecurity Dataset (HFID) 48 as the
primary data source to model the impact of food price spikes on food insecurity
under ENSO–sensitivity variability in Sub-Saharan Africa. The HFID provides
sub-national data, integrating multiple sources to capture the complexity of

12Climate Variability Modulates Price-Spike Impacts
food insecurity dynamics. Among the different food insecurity indicators, the
Reduced Coping Strategy Index (rCSI) is a survey-based measure that sum-
marizes the frequency and severity of food-related coping strategies used by
households over the previous seven days 49. In the HFID, rCSI is harmonized
and aggregated at the administrative 1 sub-national level; in this study, we
focus on the share of the population per region with rCSI at or above the cri-
sis level, which corresponds to households using severe coping strategies and
is treated here as an operational threshold for acute food insecurity.
Climate data include monthly measurements of rainfall, temperature,
and the fraction of absorbed photosynthetically active radiation (FPAR) as
proxies for agricultural productivity, as well as additional drought (SPI)
and soil moisture indicators to measure water availability and environmen-
tal stress. Socioeconomic data encompass measures such as Gross Domestic
Product (GDP) to capture economic performance, population density, conflict
data 50,51, and internal displacement 35.
To quantify abnormal food price conditions, we use the Alert for Price
Spikes (ALPS) indicator developed by the World Food Program (WFP) 38,52.
ALPS is an index that compares observed staple prices to expected sea-
sonal trends and standard deviations, accounting for typical market variability,
yielding a continuous measure of price stress. Operationally, WFP uses the
threshold 0.25 to distinguish normal from above-normal price conditions: Nor-
mal if ALPS is lower than 0.25, Stress if ALPS is between 0.25 and 1, Alert
if ALPS is between 1 and 2, and Crisis if ALPS is higher than 2. We focus
on a binary treatment that contrasts normal prices with above-normal price
conditions, a policy-relevant distinction for early warning and response.
The dataset used in this work is, therefore, a subset of the HFID that
accounts for climatic variables, crop drivers, conflict, displacement, and pop-
ulation proxies, a food price spikes treatment via the ALPS indicator, and
a behavioral metric of acute food insecurity that is responsive to short-term
stress, via the rCSI. Table A1 inAppendix Aof theSupplementary Material
summarizes all this information. The area of study comprises countries from
West Africa (Benin, Cameroon, Mali, Niger, and Nigeria), the Horn of Africa
(Ethiopia, Kenya, and Somalia), and South-East Africa (Mozambique, Zambia,
and Zimbabwe), and spans from September 2020 until February 2024.
On the other hand, for the sensitivity regime stratification via GPCA analy-
sis, we employ the MODIS Version 6 product MOD13C1 to analyze the impact
of ENSO on vegetation 53. The original global MOD13C1 product contains
NDVI and EVI observations at 16-day temporal resolution and 0.05-degree
spatial resolution. We consider data from 1st of January, 2001 to 31st of Decem-
ber, 2020, and spatially restrict them to the African continent (37 ◦ S to 38 ◦
N, 20◦ E to 55◦ W). Data have been reprojected into the Equal Area Scalable
Earth (EASE) 2.0 25km grid by averaging the original resolution 54,55.

Climate Variability Modulates Price-Spike Impacts13
Data preprocessing
To construct a consistent, analysis-ready panel, we harmonized all data
sources to a common spatial and temporal support and derived the treatment,
outcome, heterogeneity, and covariate variables for the causal models. We work
at the region–month level (ADM1×month), indexing each observation by
i= (r, t), whererdenotes the region andtthe month–year. After merging
all sources, each row corresponds to a unique region–month with associated
food security, price, climate, and conflict information. For each region-month
i= (r, t), we construct a confounder vectorW i including: agroclimatic condi-
tions (mean rainfall, soil moisture, temperature, FPAR, and a 3-month mean
average of SPI over crop areas), conflict intensity (ACLED fatalities, UCDP
deaths), displacement (IDMC conflict stock displacement, and a 6-month
sum of IDPs), macroeconomic conditions (annual GDP growth), market con-
ditions (World Bank food price index), and demography (rural population,
urban-center population, and urban-cluster population).
HFID food security indicators, ALPS price indices, climate variables, and
conflict data are first aligned to a common monthly time axis over the
study period. Climate fields (e.g., rainfall, temperature, soil moisture, NDVI-
based indicators) are aggregated from their native grid or station resolution
to regional means, while conflict and displacement indicators (e.g., ACLED
events, IDP stocks and flows) are summed or averaged within each region
and month. All variables are then joined using a harmonized set of ADM1
boundaries, ensuring consistent spatial units across datasets.
To mitigate simultaneity between prices and food security measured in the
same month, we define the outcome as next-month acute food insecurity. Let
Yr,t denote the population prevalence of households in regionrwith rCSI in
crisis or above in montht(a continuous variable in [0,1]). The outcome used
in estimation is the one-month lead,Y i ≡Y r,t+1. As a robustness check on
timing, we repeat the CATE analysis with outcome leadsℓ∈ {0,1,2,3,4}.
Across leads, the Negative-regime effect remains stable and statistically distin-
guishable from zero, while Weak-regime effects remain smaller and imprecisely
estimated; Positive-regime estimates are near zero at short leads and turn
negative at longer leads (seeAppendix Eof theSupplementary Material).
The treatment captures abnormal price conditions using ALPS. Let
ALPSr,t denote the (continuous) ALPS index in regionrand montht.
To reduce short-term noise and capture sustained price stress, we use a
three-month moving average
ALPS
(3)
r,t = 1 3
2X
k=0
ALPSr,t−k.(1)

14Climate Variability Modulates Price-Spike Impacts
We then define the binary treatment as
Ti ≡T r,t =
(
1,if ALPS
(3)
r,t ≥0.25,
0,otherwise,
(2)
so thatT i = 0 corresponds to Normal price conditions andT i = 1 corresponds
to above-normal conditions (Stress/Alert/Crisis) under WFP’s operational
thresholds 38. This timing choice is also consistent with the temporal scale
of the climatic stratification: ENSO-related vegetation responses in Africa
are often expressed over seasonal horizons of roughly 1–3 months, with some
regions showing lags of about 3 months, so the 3-month ALPS moving average
is intended to capture sustained price stress on a similar multi-month scale
rather than a point-in-time shock 23,21,56.
Each region is assigned to one of three sensitivity regimes derived from the
GPCA analysis (Negative, Weak, Positive), as described in the following sub-
section. This yields a categorical heterogeneity variableX i, which we later use
to stratify the CATE estimates. For each observation, we construct a vector of
observed covariatesW i that capture climatic, conflict, displacement, economic,
and demographic conditions:
Wi =

rainfall, soil moisture, temperature, FPAR, SPI3, conflict events,
displacement, GDP, rural/urban populations

.
These covariates correspond to the variables used in the adjustment set for
the Double Machine Learning models. To absorb time-invariant regional differ-
ences (e.g., baseline market access, geography, long-run livelihood structure),
we include region fixed effects by adding ADM1 dummy variables to the set of
covariates. Otherwise, to absorb global shocks that may affect all geographies
equally at a given moment, we include time fixed effects by adding year–month
dummy variables, aligned to thet+1 time step of the outcome, to the covariate
set. Concretely, we augment the adjustment vector with a one-hot encoding of
regions and year–month, so that the nuisance models are fit on
W ∗ i =  Wi, δr, δt+1  ,(3)
whereδ r andδ t+1 denote the spatial and temporal fixed effects, respectively.
We remove observations with missing values in the treatment, lead out-
come, regime label, or any confounder. Continuous covariates are standardized
to have zero mean and unit variance using the training sample to facilitate sta-
ble estimation with machine learning models. Categorical variables (including
the sensitivity regime and geographic location) are one-hot (dummy) encoded
when needed. To avoid regions with insufficient treated/control support, we
enforce a minimum within-region support condition, retaining only regions
with both treated and control observations over the study window. These steps

Climate Variability Modulates Price-Spike Impacts15
reduce sensitivity to extreme imbalance and improve the stability of regime-
specific estimates. The resulting panel is a monthly region-level dataset where
each observation contains (Y i, Ti, Xi, W∗ i ) and is ready for use in the DML
pipeline.
Sensitivity regime Stratification via GPCA
Algorithm 1GPCA for sensitivity Regime Classification
Require:NDVI time seriesZ t ∈R N×T forNspatial units over timeT; ENSO
indexE t
Ensure:Sensitivity regime labelX i ∈ {Negative,Weak,Positive}for each unitr
1:Construct the data matrixZ t = [NDVIt 1, . . . ,NDVIt N ]T
2:Compute a low-rank representation via PCA to obtain components Φ k and
loadingsW
3:Apply GPCA to obtain rotated components eΦk and select eΦ1 as the dominant
ENSO-linked signal
4:Pixel-level weights:for each pixelp, estimate the regression coefficient
βp from NDVI p(t) =α p +β p eΦ1(t) +ε p,t,
and sign-correct eΦ1 so that corr( eΦ1, Et)≥0
5:Define astrong-effectthresholdt 0 =Q 0.2(|β p |) across all pixels
6:foreach regionrdo
7:ComputestrengthS r = medianp∈r(|β p |)
8:Computecoverageq r = Prp∈r(|β p |> t0)
9:Computedominanceover strong pixels:
Dr =
P
p∈r:|βp|>t0 βpap P
p∈r:|βp|>t0 |β p |a p
,
wherea p = cos(latp) is an area weight.
10:end for
11:Define a weak thresholdS th =Q 0.33(Sr) across regions
12:foreach regionrdo
13:ifS r < Sth orq r <0.2or|D r |<0.2then
14:X i ←Weak
15:else ifD r >0then
16:X i ←Positive
17:else
18:X i ←Negative
19:end if
20:end for
21:returnX i for all regions
To model ENSO’s influence on vegetation, we use satellite-derived NDVI
time series across Africa and monthly ENSO indices (Ni˜ no 3.4). We capture

16Climate Variability Modulates Price-Spike Impacts
causal temporal dependencies using Granger-rotated PCA, as shown in Algo-
rithm 1. This identifies low-rank NDVI projections that are causally influenced
by ENSO.
Using the leading Granger-causal component, we quantify ENSO sensitiv-
ity spatially through the regression coefficientβ p obtained from NDVI p(t) =
αp +β p eΦ1(t)+ε p,t at each pixelp. We sign-correct eΦ1 so that corr(eΦ1, Et)≥0,
implyingβ p >0 corresponds to higher NDVI under positive ENSO (El
Ni˜ no-like) conditions. To obtain stable administrative-level regimes, pixels are
spatially joined to ADM2 district polygons and aggregated to ADM1 regions.
For each ADM1 regionr, we compute
• a robust strength statisticS r = medianp∈r(|β p |),
• a strong-signal coverageq r = Pr(|β p |> t0) usingt 0 defined as the 20th
percentile of|β p |across the area of interest,
• a magnitude-weighted sign dominanceD r = P βpap/ P |β p |a p over
pixels with|β p |> t0, witha p = cos(lat p) to approximate equal-area
weighting under geographic coordinates.
Regions are labeledWeakifS r falls below the 33rd percentile across
regions, ifq r <0.2, or if|D r |<0.2 (mixed-sign response). Otherwise, regions
are labeledPositiveifD r >0 andNegativeifD r <0. These ADM1 regime
labels are then used as stratification variables in the CATE models. Regime-
map robustness to threshold choices and to pixel subsampling is reported in
Appendix Bof theSupplementary Material.
Conditional Average Treatment Effect Estimation
Estimating the heterogeneous impacts of price spikes on food insecurity is
a complex challenge, particularly in regions exposed to significant climate vari-
ability. Traditional causal inference methods, such as matching and regression,
often struggle to capture the non-linear and high-dimensional relationships
present in real-world data. To address these limitations, machine learning
approaches like Causal Trees 27, Meta-learners 28, and Causal Forests 57 have
been developed. These methods provide flexible, nonparametric tools for esti-
mating heterogeneous treatment effects, making them well-suited for analyzing
complex, context-specific interventions.
In this work, we adopt the potential outcomes framework 58,59 to estimate
the causal effect of food price spikes on food insecurity. For each uniti, letYi(1)
andY i(0) represent the potential outcomes under treatment (i.e., exposure to
a price spike) and control (no spike), respectively. The observed outcome is
defined as:
Yi =T iYi(1) + (1−T i)Yi(0),(4)
whereT i ∈ {0,1}indicates the binary treatment status, derived from the ALPS
indicator. Our target estimand is the Conditional Average Treatment Effect
(CATE), defined as:
τ(x) =E[Y i(1)−Y i(0)|X i =x],(5)

Climate Variability Modulates Price-Spike Impacts17
whereX i is the vector of effect heterogeneity. Treatment effect hetero-
geneity is examined with respect to the categorical sensitivity regime vari-
ableX i ∈ {Negative, Weak, Positive}, derived from Granger-rotated PCA
(GPCA). We compute stratified average treatment effects within each regime
while adjusting for confoundersW i (climatic, demographic, socioeconomic,
and conflict-related features) using flexible machine learning estimators: the
Linear DML and the Causal Forest DML. To estimate these effects, we fol-
low a two-stage process: (1) estimate outcome and propensity models using
gradient boosting regressors/classifiers; (2) plug the models into CATE esti-
mators to obtain treatment effect estimates and confidence intervals within
each sensitivity regime.
Assumptions
Our causal identification strategy relies on the following assumptions, which
enable the estimation of Conditional Average Treatment Effects (CATEs) from
observational data.
Unconfoundedness (Ignorability)
Formally, this refers to
Yi(1), Yi(0)⊥T i |X i, Wi,(6)
where we assume that all variables that jointly affect the treatment assignment
(price spike exposure) and the outcome (acute food insecurity) are observed
in the covariate setW i, which includes demographic, climate, market, and
conflict indicators.
Positivity (Overlap)
Positivity refers to the fact that
0<P(T i = 1|X i, Wi)<1,∀i(7)
which ensures that for all covariate profiles, there is a non-zero probability of
observing both treated and untreated units.
SUTV A (Stable Unit Treatment Value Assumption)
We assume no interference between units (e.g., no spillover effects between
regions) and that treatment is consistently applied.

18Climate Variability Modulates Price-Spike Impacts
Consistency
Finally, the observed outcome equals the potential outcome under the
treatment actually received:
Yi =Y i(Ti) (8)
The previous assumptions are not directly testable. We aim to make
them more plausible by conditioning on a rich set of pre-treatment covariates
motivated by the causal graph and domain knowledge, and assessing over-
lap empirically through propensity score diagnostics and trimming. The DML
estimators address high-dimensional, nonlinear confounding adjustment and
reduce sensitivity to nuisance-model misspecification through orthogonaliza-
tion and cross-fitting, but they do not resolve violations due to unobserved
confounding or interference.
Double Machine Learning for CATE Estimation
The main effect estimates reported in this work are obtained using Dou-
ble Machine Learning (DML) estimators, which combine flexible predictive
models with Neyman-orthogonal moment conditions to mitigate regularization
bias in high-dimensional settings. In our context, DML allows us to estimate
EV-regime-specific effects of food price spikes on acute food insecurity while
controlling for a rich set of climatic, conflict, displacement, and demographic
covariates.
Setup and notation
For each observationi, letT i ∈ {0,1}denote the treatment indicator for
price spikes (ALPS in Normal vs. Stress/Alert/Crisis),Y i ∈[0,1] the preva-
lence of acute food insecurity (share of population with rCSI in crisis or above),
Xi the heterogeneity features (including the sensitivity regime encoded as
dummies), andW i the vector of observed confounders denoted in theData
Preprocessingsubsection. Under the assumptions in the previous subsection,
the target estimand is the Conditional Average Treatment Effect
τ(x) =E

Yi(1)−Y i(0)|X i =x

,(9)
which we summarize by sensitivity regimesX i ∈ {Negative, Weak, Positive}.
We interpret the estimand as the effect of entering an above-normal price-stress
state as defined by WFPs ALPS trigger (ALPS≥0.25), relative to remaining
in normal conditions, on next-month rCSI prevalence.
Orthogonalization and nuisance functions
Following the DML framework, we decompose the estimation problem
into: (i) learning nuisance functions that capture exposure and vulnerability

Climate Variability Modulates Price-Spike Impacts19
pathways, and (ii) estimating the treatment effect from residualized (orthogo-
nalized) outcomes and treatments. We assume a partially linear model of the
form
Yi =m Y (Xi, W∗ i ) +T i ·τ(X i) +ε i,E[ε i |X i, W∗ i , Ti] = 0,(10)
and a treatment model
Ti =m T (Xi, W∗ i ) +ν i,E[ν i |X i, W∗ i ] = 0.(11)
DML estimatesτ(·) by learning the nuisance functionsm Y (·) andm T (·) with
machine learning models, constructing orthogonalized residuals, and fitting the
final-stage effect model on these residuals. We estimate the nuisance functions
mY (X, W∗) =E[Y|X, W ∗], m T (X, W∗) =E[T|X, W ∗],(12)
and, when needed for overlap restriction, the propensity score
e(W ∗) =P(T= 1|W ∗).(13)
Given estimates ˆmY ,ˆmT , we form residuals
˜Yi =Y i −ˆmY (Xi, W∗ i ), ˜Ti =T i −ˆmT (Xi, W∗ i ),(14)
and estimate a treatment effect functionτ(·) by fitting the final-stage model
using ( ˜Y ,˜T , Xi). Because the score function is Neyman-orthogonal, small
errors in ˆmY and ˆmT have only a second-order impact on the final estimates,
which is crucial when using flexible machine learning models.
Cross-fitting
To reduce overfitting and support the theoretical guarantees of DML while
avoiding temporal leakage in panel data, we useK-fold cross-fitting with
blocked time folds. Concretely, we partition the panel intoK= 5 folds defined
by contiguous time blocks (months), and for each foldkwe fit nuisance mod-
els on the remaining blocks and generate out-of-fold residuals on the held-out
block. For each foldk, nuisance models are trained on the complement of fold
k, and residuals ( ˜Yi, ˜Ti) are computed on foldkusing only models that were
not trained on those observations. The treatment effect model is then fit on
the pooled residuals across all folds. This procedure is implemented directly
through theLinearDMLandCausalForestDMLclasses from theeconml 60
package.
Estimators
We employ two DML estimators, a Linear DML and a Causal Forest DML.
In the LinearDML specification, the final stage assumes a linear treatment

20Climate Variability Modulates Price-Spike Impacts
effect in a set of basis functions ofX. Concretely, the estimator fits a penalized
linear model of the form
˜Yi = ˜Ti θ⊤ϕ(Xi) +ε i,(15)
whereϕ(X i) includes sensitivity regime dummies, andθis estimated via Ridge
regression. This yields a parametric, interpretable treatment effect function
τ(x) =θ ⊤ϕ(x).
In the CausalForestDML specification, the final stage is a nonparametric
causal forest that allows flexible nonlinear interactions among treatment, sen-
sitivity regimes, and covariates. The forest partitions the feature space so that
neighboring units with similar (X, W) share similar treatment effect estimates.
Both estimators treat the outcome as continuous and the treatment as
binary.
Nuisance model selection
For each nuisance function (outcome regressionm Y and treatment model
mT ), we perform predictive model selection over a small library of tree-
based learners (Random Forest, Gradient Boosting, and XGBoost). We tune
hyperparameters via randomized search and evaluate candidates using 5-
fold time-block cross-validation, selecting the configuration with the highest
validationR 2 (form Y ) or ROC–AUC (form T ). The selected learner and
hyperparameters are then used within the DML cross-fitting procedure to fit
nuisance models on the training folds and generate out-of-fold residuals. This
predictive tuning is a practical choice; more targeted selection criteria for
doubly robust functionals are an active research topic 61.
InAppendix Dof theSupplementary Material, we report cross-validated
predictive scores (and in-sample diagnostics) for the selected nuisance learn-
ers as a check that the covariates capture exposure and vulnerability signal;
uncertainty quantification for the causal effects is obtained via the bootstrap
described below.
Propensity score trimming
To improve overlap between treated and control observations, we estimate
a propensity score ˆe(W ∗) using logistic regression with standardized covari-
ates 62. To reduce sensitivity to limited overlap and extreme propensity scores,
we apply hard trimming, following common-support recommendations in the
literature 63. In practice, we retain only units satisfying
0.2≤ˆe(W ∗)≤0.8.(16)
After trimming to the common-support region, we retain≈56% of obser-
vations overall (about 43–64% across regimes), while preserving non-trivial
treated/control support in each regime. The estimators are then fit on this

Climate Variability Modulates Price-Spike Impacts21
trimmed sample. The relatively large fraction of discarded observations indi-
cates limited overlap in covariate distributions between treated and control
units in the full panel, consistent with price-stress episodes being more
likely to occur in systematically different contexts (e.g., conflict/displacement
and adverse agroclimatic conditions). Consequently, post-trimming estimates
should be interpreted as effects for the overlap population in which both treat-
ment states are empirically supported, thereby improving internal validity at
the expense of external validity and statistical precision. InAppendix Cof the
Supplementary Material, we provide additional trimming diagnostics (propen-
sity distributions, sample sizes before/after trimming, and standardized mean
differences).
Sensitivity regime specific effects
The DML estimators learn an individual-level treatment effect function
ˆτ(x). We obtain regime-specific CATEs by averaging these predictions within
each sensitivity regime:
bτ(x) = 1 nx X i:Xi=x ˆτ(Xi),(17)
wheren x is the number of observations in regimex. These are the values
reported for Negative, Weak, and Positive regimes in theResults section.
Uncertainty and robustness
Uncertainty around regime-specific CATE estimates is quantified using
a nonparametric bootstrap that accounts for time dependence and com-
mon shocks. Specifically, we use a time-block bootstrap: we resample months
with replacement from the propensity-score-trimmed panel and retain all
regional observations within each selected month, yieldingB= 1000 boot-
strap replicates. For each replicate, we refit the full estimation pipeline
(including nuisance models under cross-fitting) and recompute regime-specific
CATEs. Percentile-based confidence intervals are computed from the empirical
bootstrap distributions, and two-sidedp-values are computed as
p= 2 min{P(bτ∗ ≥0),P(bτ ∗ ≤0)},(18)
wherebτ∗ denotes the bootstrap replicate of the CATE.
Finally, to probe sensitivity to modeling choices and residual confound-
ing, we run robustness checks: (i) placebo tests where treatment is permuted
within regimes, (ii) random common cause (RCC) experiments where a syn-
thetic covariate is added toWand stability of CATEs is assessed, and (iii)
random subset removal (RSR), where a fixed fraction of observations is repeat-
edly dropped and dispersion of CATE estimates is summarized. An additional

22Climate Variability Modulates Price-Spike Impacts
table with all the robustness metrics can be found inAppendix Dof the
Supplementary Material.
Data Availability
The Harmonized Food Insecurity Dataset (HFID) used in this study will
be openly available at Zenodo upon publication.
Code Availability
All code used for the analysis in this paper will be openly available on
GitHub at Causal4FS-Prices. The effect estimation analysis was conducted
using the open-source Python packages EconML and Scikit-learn.

Climate Variability Modulates Price-Spike Impacts23
References
[1] Food and Agriculture Organization of the United Nations (F AO). The
State of Food Security and Nutrition in the World 2023.F AO Publications,
2023.
[2] Maros Ivanic and Will Martin. Implications of higher global food prices
for poverty in low-income countries 1.Agricultural economics, 39:405–416,
2008.
[3] Quentin Wodon and Hassan Zaman. Higher food prices in sub-saharan
africa: Poverty impact and policy responses.World Bank Research
Observer, 25:157–176, 02 2010. doi: 10.1093/wbro/lkp018.
[4] Christopher B Barrett. Food security and food assistance programs.
Handbook of Agricultural Economics, 2:2103–2190, 2002.
[5] Derek Headey and Shenggen Fan. Anatomy of a crisis: the causes and
consequences of surging food prices.Agricultural Economics, 39(s1):375–
391, 2008.
[6] Amartya Sen.Poverty and Famines: An Essay on Entitlement and
Deprivation. Oxford University Press, 01 1981.
[7] Matthias Kalkuhl and Joachim von Braun. Food Price Volatility and Its
Implications for Food Security and Policy. Technical report, University
Library of Munich, Germany, 04 2016.
[8] Marc F Bellemare. Rising food prices, food price volatility, and social
unrest.American Journal of Agricultural Economics, 97(1):1–21, 2015.
[9] Nicholas Minot. Transmission of world food price changes to markets in
sub-saharan africa. 01 2011.
[10] Joseph W Glauber, David Laborde, Will Martin, and Rob Vos. COVID-
19: Trade restrictions are worst possible response to safeguard food
security.International Food Policy Research Institute, 2020.
[11] Steven Haggblade, Nathalie M Me-Nsope, and John M Staatz. Food
security implications of staple food substitution in Sahelian West Africa.
Food Policy, 71:27–38, 2017.
[12] Tim Wheeler and Joachim von Braun. Climate change impacts on global
food security.Science, 341(6145):508–513, 2013. doi: 10.1126/science.
1239402.
[13] Molly E Brown and Christopher C Funk. Food security under climate
change.Science, 319(5863):580–581, 2008.
[14] Samuel S Myers, Matthew R Smith, Sarah Guth, Christopher D Golden,
Bapu Vaitla, Nathaniel D Mueller, Alan D Dangour, and Peter Huybers.
Climate change and global food systems: potential impacts on food secu-
rity and undernutrition.Annual review of public health, 38(1):259–277,
2017.
[15] Isaac G. K. Ansah, Cornelis Gardebroek, and Rico Ihle. Shock interac-
tions, coping strategy choices and household food security.Climate and
Development, 13(5):414–426, 2021. doi: 10.1080/17565529.2020.1785832.

24Climate Variability Modulates Price-Spike Impacts
[16] Tosin Gbadegesin, Bo Pieter Johannes Andr´ ee, and Ademola Braimoh.
Climate Shocks and Their Effects on Food Security, Prices, and Agricul-
tural Wages in Afghanistan. Policy Research Working Paper 10999, World
Bank, 12 2024.
[17] Committee on World Food Security.HLPE Report: Price volatility and
food insecurity. 2011.
[18] Michael J McPhaden, Stephen E Zebiak, and Michael H Glantz. ENSO
as an integrating concept in Earth science.Science, 314(5806):1740–1745,
2006.
[19] Sharon E Nicholson and Denise Klotter. The impact of drought on African
agriculture: A review.Climate Research, 58(3):173–188, 2014.
[20] Assaf Anyamba and Compton J Tucker. Historical Perspectives of
A VHRR NDVI and Vegetation Drought Monitoring. InRemote sensing
of drought: Innovative monitoring approaches, pages 23–51. CRC Press,
2012.
[21] Nazmus Sazib, Iliana E. Mladenova, and John D. Bolten. Assessing the
impact of ENSO on agriculture over africa using earth observation data.
Frontiers in Sustainable Food Systems, 4:509914, 2020. doi: 10.3389/fsufs.
2020.509914.
[22] Nathalie Philippon, Nad` ege Martiny, Pierre Camberlin, M. T. Hoff-
man, and Val´ ery Gond. Timing and patterns of the ENSO signal in
africa over the last 30 years: Insights from normalized difference veg-
etation index data.Journal of Climate, 27(7):2509–2532, 2014. doi:
10.1175/JCLI-D-13-00365.1.
[23] Assaf Anyamba, Compton J. Tucker, and J. Ronald Eastman. NDVI
Anomaly Patterns over Africa during the 1997/98 ENSO Warm Event.
International Journal of Remote Sensing, 22(10):1847–1859, 2001. doi:
10.1080/01431160010029156.
[24] Clive WJ Granger. Investigating causal relations by econometric models
and cross-spectral methods.Econometrica, 37(3):424–438, 1969.
[25] Robert H Shumway and David S Stoffer.Time Series Analysis and Its
Applications. Springer, 2000.
[26] Gherardo Varando, Miguel ´Angel Fern´ andez-Torres, Jordi Mu˜ noz Mar ´ ı,
and Gustau Camps-Valls. Learning Causal Representations with Granger
PCA. InCausal Representation Learning Workshop at the Conference on
Uncertainty in Artificial Intelligence (UAI), 2022.
[27] Susan Athey and Guido W Imbens. Recursive partitioning for heteroge-
neous causal effects.Proceedings of the National Academy of Sciences,
113(27):7353–7360, 2016.
[28] S¨ oren R K¨ unzel, Jasjeet S Sekhon, Peter J Bickel, and Bin Yu. Met-
alearners for estimating heterogeneous treatment effects using machine
learning.Proceedings of the National Academy of Sciences, 116(10):
4156–4165, 2019.

Climate Variability Modulates Price-Spike Impacts25
[29] Vasileios Sitokonstantinou, Emiliano D ´ ıaz Salas Porras, Jordi Cerd` a
Bautista, Maria Piles, Ioannis Athanasiadis, Hannah Kerner, Giulia Mar-
tini, Lily belle Sweet, Ilias Tsoumas, Jakob Zscheischler, and Gustau
Camps-Valls. Causal machine learning for sustainable agroecosystems,
2024.
[30] Jordi Cerd` a-Bautista, Jos´ e Mar ´ ıa T´ arraga, Vasileios Sitokonstantinou,
and Gustau Camps-Valls. Assessing the causal impact of humanitarian
aid on food security, 2024.
[31] Georgios Giannarakis, Vasileios Sitokonstantinou, Roxanne Suzette
Lorilla, and Charalampos Kontoes. Personalizing Sustainable Agriculture
with Causal Machine Learning, 2022.
[32] Charlotte Benson and Edward Clay. The Impact of Drought on Sub-
Saharan African Economies.ids bulletin, 25(4):24–32, 1994.
[33] Assaf Anyamba, Erin Glennie, and Jennifer Small. Teleconnections and
interannual transitions as observed in african vegetation: 2015–2017.
Remote Sensing, 10(7):1038, 2018.
[34] Chester F. Ropelewski and Michael S. Halpert. Global and regional scale
precipitation patterns associated with the El Ni˜ no/Southern Oscillation.
Monthly Weather Review, 115(8):1606–1626, 1987.
[35] Internal Displacement Monitoring Centre. Global report on internal
displacement 2024, 2024.
[36] F AO, IF AD, UNICEF, WFP, and WHO.The State of Food Security
and Nutrition in the World 2023. Food and Agriculture Organization
of the United Nations, Rome, 2023. Urbanization, agrifood systems
transformation and healthy diets across the rural-urban continuum.
[37] Food Security Information Network and Global Network Against Food
Crises. Global report on food crises 2024, 2024.
[38] World Food Programme. Calculation and Use of the Alert for Price
Spikes (ALPS) Indicator. Technical report, United Nations World Food
Programme, 2014. Technical Guidance Note.
[39] World Food Programme and CARE International.The Coping Strate-
gies Index: Field Methods Manual. World Food Programme, Rome, 2008.
Revised edition.
[40] Melissa Dell, Benjamin F. Jones, and Benjamin A. Olken. Tempera-
ture shocks and economic growth: Evidence from the last half century.
American Economic Journal: Macroeconomics, 4(3):66–95, 2012.
[41] Marshall Burke, Solomon M. Hsiang, and Edward Miguel. Global non-
linear effect of temperature on economic production.Nature, 527:235–239,
2015.
[42] World Bank.Poverty and Shared Prosperity 2020: Reversals of Fortune.
World Bank, Washington, DC, 2020.
[43] Homer Durand, Gherardo Varando, and Gustau Camps-Valls. Learning
Causal Response Representations through Direct Effect Analysis, 2025.
[44] Food and Agriculture Organization of the United Nations (F AO). The
2015-2016 El Ni˜ no event: impacts on agriculture, food security and

26Climate Variability Modulates Price-Spike Impacts
nutrition. F AO Knowledge Repository, 2016.
[45] Karina Winkler, Ursula Gessner, and Volker Hochschild. Identifying
droughts affecting agriculture in africa based on remote sensing time
series between 20002016.Remote Sensing, 9(8):831, 2017. doi: 10.3390/
rs9080831.
[46] Donald B Rubin. Randomization analysis of experimental data: The
fisher randomization test comment.Journal of the American statistical
association, 75(371):591–593, 1980.
[47] Donald B Rubin. Comment: Which ifs have causal answers.Journal of
the American statistical association, 81(396):961–962, 1986.
[48] Melissande Machefer, Michele Ronco, Anne-Claire Thomas, Michael
Assouline, Melanie Rabier, Christina Corbane, and Felix Rembold. A
monthly sub-national Harmonized Food Insecurity Dataset for compre-
hensive analysis and predictive modeling.Scientific Data, 12(1):741,
2025.
[49] Daniel Maxwell and Richard Caldwell. The coping strategies index : Field
methods manual - second edition. 01 2008.
[50] Clionadh Raleigh, Andrew Linke, Havard Hegre, and Joakim Karlsen.
Introducing acled: An armed conflict location and event dataset.Journal
of Peace Research, 47(5):651–660, 2010. ISSN 00223433.
[51] Shawn Davies, Garoun Engstr¨ om, Therese Pettersson, and Magnus
¨Oberg. Organized violence 1989–2023, and the prevalence of organized
crime groups.Journal of Peace Research, 61(4):673–693, 2024.
[52] J. Herteux, C. R¨ ath, G. Martini, A. Baha, K. Koupparis, I. Lauzana,
and D. Piovani. Forecasting trends in food security with real time
data.Communications Earth & Environment, 5, 2024. doi: 10.1038/
s43247-024-01698-9.
[53] Chris O Justice, John RG Townshend, Eric F Vermote, Edward Masuoka,
Robert E Wolfe, Nazmi Saleous, David P Roy, and Jeffrey T Morisette.
An overview of MODIS land data processing and product status.Remote
Sensing of Environment, 83(1-2):3–15, 2002.
[54] M. F Goodchild and A. Kimerling. Discrete Global Grids: A Web Book,
2002.
[55] Mary J. Brodzik, Brendan Billingsley, Terry Haran, Bruce Raup, and
Matthew H. Savoie. EASE-Grid 2.0: Incremental but significant improve-
ments for earth-gridded data sets.ISPRS International Journal of
Geo-Information, 1(1):32–45, 2012.
[56] Food and Agriculture Organization of the United Nations. The Transmis-
sion of International Maize Price Signals in Eastern and Southern Africa.
Technical brief no. 2, F AO Trade and Markets Division, Rome, 2009.
[57] Stefan Wager and Susan Athey. Estimation and Inference of Heteroge-
neous Treatment Effects using Random Forests, 2017.
[58] Donald B. Rubin. Estimating causal effects of treatments in randomized
and nonrandomized studies. 66(5):688–701, 1974. doi: 10.1037/h0037350.

Climate Variability Modulates Price-Spike Impacts27
[59] Guido W. Imbens and Donald B. Rubin.Causal Inference in Statistics,
Social, and Biomedical Sciences. Cambridge University Press, 2015.
[60] Keith Battocchi, Eleanor Dillon, Maggie Hei, Greg Lewis, Paul
Oka, Miruna Oprescu, Vasilis Syrgkanis. EconML: A Python
Package for ML-Based Heterogeneous Treatment Effects Estimation.
https://github.com/py-why/EconML, 2019.
[61] Y. Cui and E. J. Tchetgen Tchetgen. Selective machine learning of dou-
bly robust functionals.Biometrika, 111(2):517–535, 2024. doi: 10.1093/
biomet/asad055.
[62] Rosenbaum, Paul R. and Rubin, Donald B. The Central Role of the
Propensity Score in Observational Studies for Causal Effects.Biometrika,
70(1):41–55, 1983. doi: 10.1093/biomet/70.1.41.
[63] Crump, Richard K. and Hotz, V. Joseph and Imbens, Guido W. and
Mitnik, Oscar A. Dealing with Limited Overlap in Estimation of Average
Treatment Effects.Biometrika, 96(1):187–199, 2009. doi: 10.1093/biomet/
asn055.

28Climate Variability Modulates Price-Spike Impacts
Acknowledgments
This work was supported by the European Union’s Horizon Europe Research
and Innovation Program through the ThinkingEarth project (under Grant
Agreement number 101130544). GCV research for this study was funded by the
European Research Council (ERC) Synergy Grant “Understanding and Mod-
eling the Earth System with Machine Learning” (USMILE) under the Horizon
2020 Research and Innovation program (Grant Agreement No. 855187).
Author Contributions
J.C-B., V.S., and G.C-V. designed and structured the study. J.C-B. and G.C-
V. wrote the initial draft, with contributions and revisions from all co-authors.
H.D. and G.V. provided expertise and implemented GPCA. J.C-B. led the
data harmonization for this specific task. M.R. led the curation, collection, and
harmonization of the full HFID. G.C-V. supervised the study from inception
and secured funding.
Competing Interests
The authors declare no competing interests.

Climate Variability Modulates Price-Spike Impacts29
Supplementary material
Appendix A Justification of the causal links
in the DAG
T able A1:Outcome, treatment, and confounders derived from the
HFID and used in the causal analysis.All variables are aggregated at
the ADM1-month level. Confounders are grouped into climate, economic, and
social domains.
Domain V ariable Description Source
OutcomerCSI Reduced Coping Strategy Index crisis prevalence, monthly mean. WFP
T reatmentALPS Alert for Price Spikes averaged for staple food commodities. WFP Prices
Mean Temperature (Crop) Spatial mean of the monthly average temperature over crop-covered areas. ASAP
Mean FPAR (Crop)
Spatial mean of the monthly average
fraction of absorbed photosynthetically
active radiation (FPAR) over
crop-covered areas.
ASAP
ClimateMean Rainfall (Crop) Spatial mean of the monthly average rainfall over crop-covered areas. ASAP
Mean SPI-3 (Crop)
Spatial mean of the 3-month
Standardized Precipitation Index over
crop-covered areas.
ASAP
Mean Soil Moisture (Crop)
Spatial mean of the monthly average
combined soil moisture over
crop-covered areas.
ASAP
Economic
GDP Growth Gross Domestic Product annual growth (in %) of the previous year. F AO GDP
Food Price Index Monthly change in international prices of a basket of food commodities. World Bank
Social
Conflict Stock Displacement Number of internally displaced people in stock due to conflict. IDMC
IDP Inflows (6m) Number of internally displaced people summed over the last 6 months. Rost et al. 2025
Urban Population (Centre) Total population for urban centres (cities). GHSL
Urban Population (Cluster) Total population for urban clusters (suburbs/peri-urban). GHSL
Rural Population Total rural population. GHSL
ACLED Fatalities Number of deaths from conflict events. ACLED
UCDP Deaths Number of fatalities from conflict events. UCDP

30Climate Variability Modulates Price-Spike Impacts
T able A2: Justification of the causal links in the DAG (Part I). For each
directed edge we provide a short rationale and example supporting references.
F rom T o Justification and references
ENSO NDVI,
Crop
Drivers
ENSO alters regional rainfall and temperature patterns, which drive veg-
etation greenness and define crop growing conditions (Anyamba et al.,
2018; Ropelewski and Halpert, 1987; F AO et al., 2023).
ENSO GDP Climate shocks associated with ENSO influence aggregate output and
growth, particularly in agriculture-dependent economies (Dell et al., 2012;
Burke et al., 2015).
NDVI Crop
Drivers
Vegetation condition indices are closely tied to local biophysical crop con-
ditions such as canopy development and water stress (Anyamba et al.,
2018; F AO et al., 2023).
Crop
Drivers
GDP Weather- and climate-sensitive crop conditions affect yields and agricul-
tural value added, which is a key component of GDP in many low- and
middle-income countries (Dell et al., 2012; Burke et al., 2015; F AO et al.,
2023).
Crop
Drivers
Conflicts Agricultural prod. failures can exacerbate income loss, rural hardship, and
competition over resources, recognized as structural and proximate drivers
of conflict and instability (Burke et al., 2015; FSIN and Global Network
Against Food Crises, 2024).
Crop
Drivers
IDPs Agroclimatic shocks contribute to livelihood collapse and displacement,
especially in agriculture-dependent settings (FSIN and Global Network
Against Food Crises, 2024; IDMC, 2024).
Crop
Drivers
ALPS Local weather and crop conditions influence food availability and mar-
keting costs and are core drivers of abnormal local price dynamics, as
measured by ALPS (F AO et al., 2023; WFP, 2014).
Crop
Drivers
rCSI Adverse crop conditions reduce availability and access to food, increasing
the prevalence of crisis-or-worse food consumption and negative coping
strategies (F AO et al., 2023; FSIN and Global Network Against Food
Crises, 2024).
GDP Population Economic growth influences fertility, mortality and migration, shaping
spatial patterns of rural and urban populations as documented in devel-
opment and demographic-transition analyses (World Bank, 2020; F AO et
al., 2023).
GDP, Food
Prices
IDPs Macroeconomic downturns interact with shocks and fragility to increase
the likelihood that households resort to displacement as a coping strategy
(World Bank, 2020; IDMC, 2024).
GDP, Food
Prices
ALPS Macroeconomic conditions affect purchasing power, import costs, and
pass-through from global to local food prices, shaping the probability of
abnormal price spikes (F AO et al., 2023; FSIN and Global Network Against
Food Crises, 2024).
Our directed acyclic graph (DAG) links large-scale climate variability1
(ENSO), local biophysical conditions (NDVI, crop-relevant climate), macroe-2
conomic performance (GDP), structural factors (population), violent conflict,3
internal displacement (IDPs), local food prices (ALPS), and household food4
security (rCSI). Here, we briefly justify each group of arrows with support5
from the literature.6

Climate Variability Modulates Price-Spike Impacts31
T able A3: Justification of the causal links in the DAG (Part II). For each
directed edge we provide a short rationale and example supporting references.
F rom T o Justification and references
GDP, Food
Prices
rCSI Household income and employment prospects modulated by GDP growth
influence the need to adopt negative coping strategies (F AO et al., 2023;
World Bank, 2020).
Conflicts IDPs Violent conflict is the leading global driver of internal displacement
(IDMC, 2024; FSIN and Global Network Against Food Crises, 2024).
Conflicts ALPS Conflict disrupts markets, transport, and production, constraining supply
and raising transaction costs (F AO et al., 2023; FSIN and Global Network
Against Food Crises, 2024).
Conflicts rCSI Conflicts reduce incomes, destroy assets and constrain humanitarian
access, all of which raise the prevalence of acute food insecurity and severe
coping captured by rCSI (FSIN and Global Network Against Food Crises,
2024; F AO et al., 2023).
IDPs ALPS Inflows of displaced populations can increase local demand, strain markets
and infrastructure, and contribute to localised food price spikes (FSIN and
Global Network Against Food Crises, 2024; IDMC, 2024).
IDPs rCSI IDPs face greater exposure to shocks, have constrained access to liveli-
hoods and services, and are consistently among the most food-insecure
groups (FSIN and Global Network Against Food Crises, 2024; IDMC,
2024).
Population IDPs High population concentration in exposed or fragile areas increases the
number of people at risk of displacement when conflict or disasters occur
(IDMC, 2024; FSIN and Global Network Against Food Crises, 2024).
Population ALPS Population size and urbanization patterns shape aggregate demand and
pressure on food markets and infrastructure (F AO et al., 2023; FSIN and
Global Network Against Food Crises, 2024).
Population rCSI Larger and more rapidly growing, poor populations in fragile settings are
associated with higher rates of household food insecurity and negative
coping (F AO et al., 2023; World Bank, 2020).
ALPS rCSI Abnormal food price spikes directly reduce real purchasing power, forcing
households to reduce food quantities and quality or adopt harmful coping
strategies (WFP, 2014; WFP and CARE, 2008; FSIN and Global Network
Against Food Crises, 2024).
A.1 ENSO, vegetation, and crop-relevant climate
El Ni˜ no Southern Oscillation (ENSO) is a dominant mode of interannual7
climate variability and strongly affects rainfall and temperature patterns in8
many food-insecure regions. Classic work documents systematic ENSO telecon-9
nections in precipitation across the tropics and subtropics, which directly shape10
soil moisture and drought indices such as SPI. More recent global analyses11
show that ENSO phases are associated with coherent anomalies in vegetation12
greenness (NDVI), reflecting impacts on plant growth and crop performance.13

32Climate Variability Modulates Price-Spike Impacts
We therefore include direct arrows from ENSO to NDVI and to the crop-14
relevant climate variables (rainfall, soil moisture, temperature, FPAR, SPI)15
grouped as Crop Drivers.16
NDVI is both a response to and an integrator of multiple biophysical17
drivers, especially soil moisture, precipitation and radiation. Empirical studies18
consistently document strong statistical links between NDVI and concur-19
rent rainfall/soil-moisture anomalies across rain-fed agricultural systems, with20
NDVI often used as a proxy for realized crop conditions in early-warning sys-21
tems. We represent this tight coupling with an arrow from NDVI to Crop22
Drivers, acknowledging that in practice, NDVI and the Crop Drivers variables23
are jointly determined by the same underlying climate processes.24
A.2 Crop conditions, macroeconomy, and food prices
In low- and middle-income, agriculture-dependent economies, weather25
shocks to rainfall and temperature have measurable effects on aggregate26
economic output. A large macroeconomic literature shows that negative tem-27
perature and precipitation shocks reduce GDP growth, particularly in poorer28
and agriculturally intensive countries. Since our Crop Drivers summarize those29
agro-climatic shocks, we include a directed edge from Crop Drivers to GDP.30
Adverse agro-climatic conditions reduce local production and pasture avail-31
ability, contributing to tighter food markets, higher prices, and lower dietary32
adequacy. Global and regional assessments from F AO, WFP, and partners con-33
sistently highlight weather and climate extremes as major drivers of food price34
spikes and acute food insecurity. Accordingly, we include arrows from Crop35
Drivers to ALPS (our indicator of abnormal local food price conditions) and36
to rCSI (household stress and coping, via their impact on food availability and37
income opportunities).38
A.3 GDP, population pressure, and food security
Higher GDP per capita is associated with lower risk of conflict- and39
disaster-related displacement, in part through improved state capacity, infras-40
tructure, and social protection, while weak or contracting GDP is linked to41
fragility and higher displacement risk. We capture these long-run relationships42
with arrows from GDP to Population (through fertility, mortality, and migra-43
tion) and GDP to IDPs (more prosperous contexts generally experience less44
forced displacement, all else equal).45
Macroeconomic conditions influence both the pass-through of international46
price shocks and households ability to afford food. The State of Food Secu-47
rity and Nutrition in the World reports repeatedly emphasize macroeconomic48
slowdowns and downturns as core drivers of rising food prices and reduced49
food access for poor households. We therefore allow GDP to affect both ALPS50
(through macro-level price dynamics and exchange-rate pass-through) and51
rCSI (through household incomes and purchasing power).52

Climate Variability Modulates Price-Spike Impacts33
A.4 Conflict, displacement and market disruption
Several studies find that weather-related income shocks can increase the53
risk of conflict in agriculturally dependent settings, for example, via competi-54
tion over scarce land and water or reduced state capacity. On this basis, we55
include an edge from Crop Drivers to Conflicts.56
Armed conflict is a leading cause of internal displacement. The Internal57
Displacement Monitoring Center and related work consistently identify conflict58
and violence as the dominant source of new and protracted internal displace-59
ment in many of the countries covered by our data. This motivates a direct60
link from Conflicts to IDPs.61
Conflict disrupts markets, transport infrastructure, and livelihoods, rais-62
ing transaction costs, constraining supply, and often causing local food price63
spikes. At the same time, it limits income-earning opportunities and humani-64
tarian access, deepening acute food insecurity. Global food crisis assessments65
repeatedly highlight conflict as the primary driver of acute food insecurity66
episodes, acting through both price and non-price channels. We therefore67
include outgoing edges from Conflicts to ALPS and to rCSI.68
A.5 Displacement, population, and food security
outcomes
Population density and urbanization patterns condition both the scale of69
potential displacement and the pressure that displaced and host communities70
exert on local markets. Higher resident populations and inflows of IDPs into71
urban and peri-urban areas can strain local food systems and housing, thereby72
putting upward pressure on prices even when aggregate national production is73
unchanged. We represent these channels with arrows from Population to IDPs74
(exposure) and from IDPs to ALPS.75
Rapid population growth without commensurate improvements in service76
delivery and employment opportunities is associated with greater vulnerability77
to food insecurity in many low-income settings. At the same time, displaced78
households face particularly high rates of livelihood disruption, asset loss, and79
food insecurity. Global assessments by WFP and partners consistently report80
higher rCSI values and worse food security outcomes among IDPs and refugees81
than among non-displaced populations. We therefore include arrows from both82
Population and IDPs to rCSI.83
A.6 From price spikes (ALPS) to coping responses
(rCSI)
The reduced Coping Strategy Index (rCSI) is designed to capture the84
frequency and severity of short-term food-related coping strategies, such as85
reducing meal portions, skipping meals, or relying on less preferred foods, as86
households struggle to maintain caloric intake. WFP technical guidelines and87

34Climate Variability Modulates Price-Spike Impacts
validation studies show that rCSI scores rise when households experience dete-88
riorating food access due to income losses or rising staple food prices. Because89
ALPS (derived from the WFP Price Early Warning Index) explicitly captures90
abnormal food price conditions, our DAG includes a direct link from ALPS to91
rCSI, representing the pathway from local price spikes to stress on household92
food consumption behaviors.93
Appendix B Robustness of the sensitivity
regime construction
Here, we quantify the robustness of the sensitivity regime map derived from94
the GPCA analysis. The goal is to assess whether thePositive/Weak/Negative95
discretization is sensitive to the regime thresholds used to summarize pixel-96
level heterogeneity and finite-sample variability in the set of pixels contributing97
to each administrative unit. All analyses are conducted on the set of countries98
used in the causal panel (Benin, Cameroon, Mali, Niger, Nigeria, Ethiopia,99
Kenya, Somalia, Mozambique, Zambia, Zimbabwe).100
B.1 From pixel-level weights to ADM1 regimes
Letβ p denote the pixel-level GPCA weight (sensitivity influence) for pixel101
p, where the GPCA component has been sign-corrected so that corr( eΦ1, Et)≥102
0. Hence,β p >0 indicates that positive ENSO anomalies are associated with103
increased vegetation greenness, andβ p <0 indicates a negative vegetation104
response.105
To obtain stable administrative-level regimes, pixels are spatially joined106
to ADM2 polygons and aggregated to ADM1 units. We use three region-level107
summaries: (i) strengthS r = median p∈r(|β p |), (ii) coverageq r = Pr p∈r(|108
βp |> t0), and (iii) dominance over strong pixels,109
Dr =
P
p∈r:|βp|>t0 βpap P
p∈r:|βp|>t0 |β p |a p
, a p = cos(latp),(B1)
wherea p approximates equal-area weighting under geographic coordinates.110
The thresholdt 0 is defined as a low quantile of|β p |across pixels (baseline:111
20th percentile), selecting pixels with non-negligible ENSO-related influence.112
Regions are labeledWeakif any of the following holds:113
Sr < Sth orq r < qmin or|D r |< dmin,(B2)
whereS th is a low quantile of the strength distribution across regions (baseline:114
33rd percentile). Otherwise, regions are labeledPositiveifD r >0 andNega-115
tiveifD r <0. This design intentionally concentrates ambiguity in theWeak116
class (boundary regions), while preserving sign consistency in thePositiveand117
Negativeregimes.118

Climate Variability Modulates Price-Spike Impacts35
T able B4:Sensitivity of ADM1 regime labels to threshold choices
(study countries).Agreement metrics compare each configuration to the
baseline labeling. Pos↔Neg counts direct Positive↔Negative sign reversals.
Strong-pixel q Min. Dominance Min. Coverage Unchanged κ Pos↔Neg #Neg #Weak/#Pos
0.20 0.20 0.10 1.000 1.000 0 158 204/203
0.20 0.20 0.20 1.000 1.000 0 158 204/203
0.10 0.15 0.10 0.993 0.989 0 159 200/206
0.10 0.15 0.20 0.993 0.989 0 159 200/206
B.2 Sensitivity to threshold choices
We evaluate sensitivity to the main regime thresholds by varying: (i) the119
strong-pixel quantile used to definet 0 (Strong-pixel q), (ii) the minimum dom-120
inance magnituded min (Min. Dominance), and (iii) the minimum strong-signal121
shareq min (Min. Coverage). For each configuration, we recompute regime122
labels for all ADM1 units and compare them to the baseline labeling using:123
unchanged share (fraction of ADM1 units with identical labels) and Cohen’s124
κ(chance-corrected agreement). We also count Positive↔Negative sign flips,125
which are the most consequential changes.126
Table B4 summarizes representative settings. Across the tested ranges,127
agreement with the baseline labeling is high (unchanged share≥0.993,κ≥128
0.989), and we observe no direct Positive↔Negative sign flips (all changes129
occur via theWeakboundary).130
B.3 Stability under pixel subsampling
Threshold sensitivity addresses parametric choices, but regime assign-131
ment can also vary because each ADM1 label is inferred from a finite132
set of pixels. We therefore run a pixel subsampling stability test: for each133
ADM1 unitr, we repeatedly subsample a fixed fraction of its pixels (keep-134
ing their spatial membership), recompute (Sr, qr, Dr) and the resulting regime135
label, and estimate the empirical label probabilities Pr( bXr =ℓ) overℓ∈136
{Negative, Weak, Positive}.137
We define thestabilityof ADM1 unitras the probability assigned to its138
baseline label:139
Stabilityr = Pr( bXr =X base r ).(B3)
To isolate the most consequential failure mode, we also compute the140
Positive↔Negative switch probability,141
Pr(Pos↔Neg) r,(B4)
i.e., the probability that a baseline Positive region is labeled Negative (or vice142
versa) under subsampling.143

36Climate Variability Modulates Price-Spike Impacts
T able B5:Subsampling stability summary (study countries).Stability
is the probability of retaining the baseline label when pixels are subsampled.
The Pos↔Neg switch probability measures direct sign reversals.
Metric Value Notes
# ADM1 units 222 Study countries only
Baseline counts (Neg/Weak/Pos) 71 / 64 / 87
Mean stability 0.941 Pr( bXr =X base r )
Share stability≥0.9 0.794
Share stability = 1.0 0.622
Mean Pos↔Neg switch prob. 1.39×10 −4 Median = 0, 75th pct = 0
Max Pos↔Neg switch prob. 0.020 Worst-case ADM1
T able B6:Lowest-stability ADM1 units in the subsampling test
(study countries).Columns show baseline label, stability, and empirical label
probabilities under subsampling.
GID 0 Country ADM1 Baseline Stability P(Neg) P(Weak) P(Pos)
MOZ Mozambique Maputo Negative 0.575 0.575 0.425 0.000
NGA Nigeria Sokoto Weak 0.585 0.000 0.585 0.415
KEN Kenya Kericho Negative 0.585 0.585 0.380 0.035
NGA Nigeria Nasarawa Weak 0.590 0.410 0.590 0.000
NGA Nigeria Rivers Positive 0.600 0.005 0.395 0.600
KEN Kenya Turkana Negative 0.615 0.615 0.385 0.000
KEN Kenya Bungoma Negative 0.640 0.640 0.360 0.000
KEN Kenya Kiambu Weak 0.655 0.330 0.655 0.000
In the study countries, baseline regime counts are 71 Negative, 64 Weak,144
and 87 Positive. Stability is high overall: mean stability is 0.941, and 79.4%145
of ADM1 units have stability≥0.9 (62.2% have stability = 1.0). Instability is146
concentrated in theWeakboundary. Crucially, direct sign reversals are essen-147
tially absent: the mean Positive↔Negative switch probability is 1.39×10 −4148
(median and 75th percentile equal to 0), with a maximum of 0.02. This indi-149
cates that uncertainty is overwhelmingly about whether a region is labeled150

Climate Variability Modulates Price-Spike Impacts37
1.75
1.50
1.25
1.00
0.75
0.50
0.25
0.00
0.2 0.0
Treated
Control
0.2 0.4 0.6
Propensity score
0.8 1.0 1.2
Density
Fig. C1:Kernel density estimates of the propensity scores.The density
distributions illustrate the propensity score distributions for the treated and
control groups. The vertical dashed lines indicate the lower and upper cutoffs
for the propensity-score trimming.
Weakversus a strong-sign regime, not about the sign of the ENSO–Vegetation151
response.152
B.4 Most unstable units (illustrative)
To illustrate where instability arises, Table B6 lists ADM1 units with the153
lowest stability in the subsampling test. In all cases, probability mass concen-154
trates betweenWeakand one strong-sign regime, whereas sign flips remain155
negligible.156
Appendix C Propensity Score analysis
C.1 Calculation
In the main analysis, propensity scores are used to (i) assess covariate157
overlap between treated and control observations and (ii) trim observations158
with extreme treatment probabilities prior to causal effect estimation. For each159
region–month observationi, we define the propensity score as160
e(W ∗ i ) =P(T i = 1|W ∗ i ),(C5)
whereT i ∈ {0,1}is the binary treatment indicator for food price spikes (ALPS161
in Stress/Alert/Crisis vs. Normal) andW ∗ i denotes the vector of observed162

38Climate Variability Modulates Price-Spike Impacts
T able C7:Sample sizes before and after propensity-score trimming,
overall and by sensitivity regime.We report the number of control (T=0)
and treated (T=1) observations before trimming and after restricting to the
common-support region 0.2≤ˆe(W i)≤0.8.
Regime Before trimming After trimming
Control T reated Control T reated
Overall 829 845 483 455
Negative 318 238 227 130
Weak 271 378 158 220
Positive 240 229 98 105
confounders, including climatic, conflict, displacement, economic, demographic163
variables, and fixed effects as described in the main text.164
We estimatee(W ∗ i ) using a logistic regression with anℓ 2 penalty (Ridge),165
fitted on the full set of standardized confounders. Formally,166
logit

e(W ∗ i )  =β 0 +β ⊤W ∗ i ,(C6)
whereW ∗ i has been centered and scaled to unit variance. The model is trained167
on the pooled sample of treated and control observations, without using the168
sensitivity regime labels, so that the propensity score reflects only confounding169
structure, not heterogeneity by sensitivity regime.170
To improve overlap and avoid undue influence of units that are almost171
always treated or almost never treated, we perform propensity-score trimming.172
Specifically, we retain only observations such that173
0.2≤ˆe(W ∗ i )≤0.8.(C7)
The treatment effect estimators are then fitted on this trimmed sample.174
Figure C1 shows kernel density estimates of ˆe(W∗ i ) for treated and control175
observations, with vertical dashed lines marking the trimming cutoffs. The176
presence of substantial mass near the boundaries indicates that, for many177
region–months, above-normal price conditions are either highly likely or highly178
unlikely given observed covariates. Trimming, therefore, focuses inference on179
the subset of observations where both treated and control units are empirically180
comparable (i.e., contexts in which a price-stress month is plausible but not181
near-certain).182
Table C7 reports sample sizes before and after trimming. Overall, the full183
sample contains 829 control and 845 treated observations, and the trimmed184
sample contains 483 control and 455 treated observations (938 total;≈56% of185
the original sample). By regime, the Negative regime changes from 318 control186
and 238 treated to 227 control and 130 treated; the Weak regime from 271187
control and 378 treated to 158 control and 220 treated; and the Positive regime188
from 240 control and 229 treated to 98 control and 105 treated. These counts189
show that trimming removes a fraction of observations with extreme predicted190

Climate Variability Modulates Price-Spike Impacts39
T able C8: Standardized mean differences (SMD) for confounders before and
after propensity-score trimming (Overall sample).
Confounder |SMD|(Before) |SMD|(After)
Conflict Stock Displacement 0.080 0.240
Mean Temperature (Crop) 0.115 0.118
Mean Soil Moisture (Crop) 0.202 0.064
Mean FPAR (Crop) 0.232 0.156
ACLED Fatalities 0.199 0.182
Rural Population 0.035 0.085
IDP Inflows (6m) 0.069 0.036
Urban Population (Centre) 0.110 0.038
UCDP Deaths 0.125 0.166
Mean Rainfall (Crop) 0.138 0.106
GDP Growth 0.128 0.019
Urban Population (Cluster) 0.075 0.066
Mean SPI-3 (Crop) 0.038 0.048
Food Price Index 0.189 0.207
T able C9: Standardized mean differences (SMD) for confounders before and
after propensity-score trimming (Negative regime).
Confounder |SMD|(Before) |SMD|(After)
Conflict Stock Displacement 0.441 0.274
Mean Temperature (Crop) 0.137 0.118
Mean Soil Moisture (Crop) 0.408 0.333
Mean FPAR (Crop) 0.406 0.325
ACLED Fatalities 0.302 0.165
Rural Population 0.183 0.102
IDP Inflows (6m) 0.319 0.245
Urban Population (Centre) 0.445 0.187
UCDP Deaths 0.043 0.107
Mean Rainfall (Crop) 0.325 0.028
GDP Growth 0.499 0.318
Urban Population (Cluster) 0.103 0.223
Mean SPI-3 (Crop) 0.098 0.103
Food Price Index 0.539 0.316
treatment probabilities while preserving non-trivial treated/control support in191
every regime for subsequent effect estimation.192
C.2 Covariate balance before and after trimming
Propensity-score trimming improves overlap by excluding samples with193
extreme treatment probabilities, but it does not, by itself, guarantee covari-194
ate balance between treated and control units. To document how comparable195
the treated and control samples are, we report standardized mean differences196
(SMDs) for every confounder before and after trimming.197

40Climate Variability Modulates Price-Spike Impacts
T able C10: Standardized mean differences (SMD) for confounders before and
after propensity-score trimming (Weak regime).
Confounder |SMD|(Before) |SMD|(After)
Conflict Stock Displacement 0.518 0.309
Mean Temperature (Crop) 0.177 0.061
Mean Soil Moisture (Crop) 0.123 0.336
Mean FPAR (Crop) 0.220 0.065
ACLED Fatalities 0.291 0.299
Rural Population 0.034 0.088
IDP Inflows (6m) 0.040 0.078
Urban Population (Centre) 0.344 0.319
UCDP Deaths 0.196 0.259
Mean Rainfall (Crop) 0.225 0.087
GDP Growth 0.218 0.189
Urban Population (Cluster) 0.228 0.250
Mean SPI-3 (Crop) 0.091 0.173
Food Price Index 0.158 0.229
T able C11: Standardized mean differences (SMD) for confounders before and
after propensity-score trimming (Positive regime).
Confounder |SMD|(Before) |SMD|(After)
Conflict Stock Displacement 0.248 0.089
Mean Temperature (Crop) 0.212 0.336
Mean Soil Moisture (Crop) 0.028 0.003
Mean FPAR (Crop) 0.213 0.018
ACLED Fatalities 0.086 0.083
Rural Population 0.071 0.049
IDP Inflows (6m) 0.125 0.087
Urban Population (Centre) 0.317 0.193
UCDP Deaths 0.030 0.047
Mean Rainfall (Crop) 0.045 0.066
GDP Growth 0.516 0.256
Urban Population (Cluster) 0.274 0.169
Mean SPI-3 (Crop) 0.008 0.012
Food Price Index 0.200 0.043
For a given confounderW k, the SMD is computed as198
SMD(Wk) = W k,1 − W k,0r
1
2

s2 k,1 +s 2 k,0
 ,(C8)
where W k,1 and W k,0 are treated/control means ands 2 k,1 ands 2 k,0 are treat-199
ed/control variances. SMD is a scale-free effect size that quantifies covariate200
separation in standard-deviation units. As a rule of thumb,|SMD|<0.1 is201
often considered negligible imbalance and|SMD|<0.2 small-to-moderate202
imbalance; larger values indicate substantively different covariate profiles.203

Climate Variability Modulates Price-Spike Impacts41
Table C8 reports absolute SMDs in the overall sample. Trimming reduces204
imbalance for some covariates (e.g., Mean Soil Moisture (Crop) decreases from205
0.202 to 0.064 and Urban Population (Centre) from 0.110 to 0.038), but it can206
also increase imbalance for others (e.g., Conflict Stock Displacement increases207
from 0.080 to 0.240 and the Food Price Index from 0.189 to 0.207). This208
reinforces that trimming should be interpreted as enforcing common support209
(overlap), not as a balancing procedure.210
Because the main interpretation relies on regime-specific CATEs, we also211
compute within-regime SMDs (Tables C9–C11). Within-regime diagnostics212
show that moderate-to-large imbalances persist after trimming, especially in213
the Negative and Weak regimes. In the Negative regime, several covariates214
remain above 0.3 after trimming (e.g., Mean Soil Moisture (Crop) 0.333, Mean215
FPAR (Crop) 0.325, GDP Growth 0.318, Food Price Index 0.316). In the Weak216
regime, post-trimming imbalance is also substantial for key covariates (e.g.,217
Mean Soil Moisture (Crop) 0.336, Conflict Stock Displacement 0.309, Urban218
Population (Center) 0.319, ACLED Fatalities 0.299). In the Positive regime,219
balance is generally better for several variables, but notable imbalances remain220
for Mean Temperature (Crop) (0.336) and GDP Growth (0.256), among others.221
Accordingly, our causal estimates should be interpreted as effects condi-222
tional on the remaining observed confounders. Trimming is used to remove223
extreme non-overlap, while the DML estimators rely on flexible nuisance mod-224
els (with fixed effects implied by the feature construction in the main text)225
to adjust for residual confounding in the trimmed sample. The SMD diagnos-226
tics are therefore reported to transparently document overlap and remaining227
imbalance, particularly within regimes, rather than to claim that trimming228
alone yields randomized-like balance.229
Appendix D Additional results report
D.1 Nuisance models
For the CATE experiments in the main text, we model the outcome and230
treatment mechanisms231
E[Y|X, W] andE[T|X, W] (D9)
using a small library of tree-based regressors and classifiers, respectively, and232
selecting the best-performing specification via cross-validated model selection.233
Concretely, for each nuisance function, we consider three model fami-234
lies: Random Forest, Gradient Boosting, and XGBoost, with the following235

42Climate Variability Modulates Price-Spike Impacts
T able D12:Nuisance model selection and fit for the CA TE exper-
iments.Best cross-validatedR 2 and ROC–AUC for each candidate model
family when predicting the outcomeY|X, Wand treatmentT|X, W. The
final nuisance models used in the CATE estimators are highlighted in bold;
the corresponding in-sample metrics are reported in the last row.
Model family
CVR 2 for
(Y|X, W)
(Regressor)
CV ROC–AUC for
(T|X, W)
(Classifier)
Random Forest 0.214 0.613
Gradient Boosting0.3940.633
XGBoost 0.3520.637
In-sample (selected models) 0.786 0.982
hyperparameter search spaces:236
RandomForest:n estimators ∈ {200,400},max depth∈ {3,5,7},
min samples split∈ {2,5},min samples leaf∈ {2,5},
max features ="sqrt",
GradientBoosting:n estimators ∈ {200,400},max depth∈ {2,3},
learning rate∈ {0.05,0.1},subsample∈ {0.7,0.9},
min samples leaf∈ {2,5},
XGBoost:n estimators ∈ {200,400},max depth∈ {2,3,4},
learning rate∈ {0.03,0.05,0.1},subsample∈ {0.6,0.8},
colsample bytree∈ {0.6,0.8},min child weight∈ {5,10},
λ∈ {1.0,5.0,10.0}, α∈ {0.0,1.0,5.0}.
For each family, we perform a randomized hyperparameter search with 5-237
fold cross-validation and select the configuration with the highest validationR2238
(regressor for the outcome function) and ROC–AUC (classifier for the treat-239
ment function). The selected models are then used as nuisance functions within240
the LinearDML and CausalForestDML estimators. Table D12 summarizes the241
selected nuisance models and their performance for the CATE experiments.242
The Gradient Boosting regressor model achieves the highest cross-validated243
R2 for the outcome, and the XGBoost classifier model achieves the highest244
ROC–AUC for the treatment, and are therefore used as nuisance models in245
the DML-based CATE estimators.246
D.2 Baseline and DML Estimators
The main paper reports treatment effects using Double Machine Learning247
(DML) estimators. Here, we benchmark these results against simpler baseline248

Climate Variability Modulates Price-Spike Impacts43
approaches commonly used in observational panel settings. The purpose of249
this comparison is twofold: (i) provide a transparent sanity check that the250
estimated sign and regime ordering are not an artifact of a single modeling251
choice; and (ii) motivate the use of DML as the primary estimator given the252
high-dimensional, nonlinear confounding structure of the problem.253
To ensure a fair comparison across estimators, we apply the same data-254
processing steps whenever applicable: (a) the same treatment and outcome255
timing, (b) the same propensity-score trimming to common support 0.2≤256
ˆe(Wi)≤0.8, and (c) the same dependence-aware inference via a time-block257
bootstrap. Thus, differences between methods reflect their identifying assump-258
tions and functional-form restrictions rather than changes in the analysis259
sample or uncertainty quantification.260
D.2.1 Baseline estimators261
LetY i denote the outcome (acute food insecurity prevalence, rCSI),T i ∈262
{0,1}the price-stress treatment (ALPS above-normal vs. normal), andX i ∈263
{Negative, Weak, Positive}the sensitivity regime. Define the regime-specific264
CATE asτ(x) =E[Y(1)−Y(0)|X=x].265
(1) Difference in means (unadjusted).266
Within each regimex, we compute the raw treated–control difference267
bτDM(x) = Y 1,x − Y 0,x,(D10)
where Y 1,x and Y 0,x are treated and control means in regimexafter trimming.268
This estimator is easy to interpret but does not adjust for remaining covariate269
imbalance within the trimmed sample; it is therefore used only as a descriptive270
benchmark.271
(2) Two-way fixed-effects regression (linear FE).272
We estimate a linear regression with region and time fixed effects and allow273
regime-specific treatment effects via interactions:274
Yr,t+ℓ =α r +γ t+ℓ +
X
x
βx 1{X r =x}T r,t +ε r,t,(D11)
whereα r absorbs time-invariant regional differences andγ t+ℓ absorbs month275
shocks aligned to the lead of the outcome. The FE model is a standard base-276
line in applied panel work but imposes strong functional-form restrictions277
(linearity, additive separability, limited interactions). If the true confounding278
adjustment is nonlinear or involves higher-order interactions among climate,279
conflict, displacement, and demographics, FE regression can be biased and/or280
unstable.281

44Climate Variability Modulates Price-Spike Impacts
(3) Propensity-score weighting (IPW).282
Using the estimated propensity score ˆe(W∗ i ) = Pr(T i = 1|W ∗ i ), we compute283
inverse-probability-weighted regime-specific contrasts. A common form is284
bτIPW(x) =
P
i:Xi=x
TiYi
ˆe(Wi) P
i:Xi=x
Ti
ˆe(W∗ i )
−
P
i:Xi=x
(1−Ti)Yi
1−ˆe(W∗ i ) P
i:Xi=x
(1−Ti)
1−ˆe(W∗ i )
.(D12)
IPW adjusts for confounding through the propensity model, but can be285
sensitive to propensity misspecification and residual lack of overlap (hence286
trimming). In our setting, exposure is driven by complex interactions between287
market structure, conflict, displacement, and agroclimatic conditions, making288
a purely parametric propensity model a potentially fragile foundation for the289
main causal conclusions.290
D.2.2 DML estimators291
We use two DML estimators (LinearDML and CausalForestDML) that com-292
bine (i) flexible machine learning models for the nuisance functions (outcome293
regression and treatment model), (ii) orthogonalization to reduce sensitivity to294
nuisance-model errors, and (iii) cross-fitting with blocked time folds to avoid295
temporal leakage. DML targets the same regime-specific estimands as the base-296
lines, but is designed for settings like this one where confounding adjustment is297
high-dimensional and nonlinear. Conceptually, DML improves on the baselines298
in three key ways:299
(i) Flexible confounding adjustment.300
Difference-in-means is unadjusted; FE regression restricts adjustment to lin-301
ear/additive structure; IPW relies heavily on a correct propensity specification.302
In contrast, DML learnsm Y (X, W∗) =E[Y|X, W ∗] andm T (X, W∗) =303
E[T|X, W ∗] using flexible learners and then estimates effects on orthogonal-304
ized residuals. This is well suited to the nonlinear relationships among prices,305
conflict, climate anomalies, and displacement.306
(ii) Reduced sensitivity to nuisance misspecification307
(orthogonalization).308
Because the DML score is Neyman-orthogonal, small errors in the nuisance309
models have only a second-order impact on the final effect estimates. This310
provides practical robustness when nuisance functions are complex and must311
be approximated from finite data.312
(iii) Heterogeneity with stability.313
Our scientific question is explicitly heterogeneous:do effects differ across sen-314
sitivity regimes?LinearDML provides interpretable regime-specific contrasts,315
while CausalForestDML allows richer nonlinear interactions. Baselines either316

Climate Variability Modulates Price-Spike Impacts45
T able D13:F ull CA TE estimates for ALPS impacts on rCSI, strati-
fied by sensitivity regimes.Baseline and DML models. Confidence intervals
at 95%, and estimations are statistically significant ifp-values≤0.05.
Model Regime CA TE (p.p.) C.I. p-value
Negative 6.065 (3.257, 8.124) 0.020
Diff. in Means Weak -0.040 (-3.596, 3.114) 0.922
Positive 0.423 (-4.807, 5.344) 0.765
Negative 4.135 (2.051, 5.633) 0.020
Linear Regression Weak 1.084 (-0.881, 4.204) 0.157
Positive 3.312 (-1.014, 5.671) 0.216
Negative 7.102 (4.366, 9.225) 0.020
Propensity IPW Weak 0.077 (-3.848, 3.968) 0.863
Positive 0.573 (-4.348, 4.551) 0.843
Negative 5.999 (2.567, 8.730) 0.020
Linear DML Weak 1.938 (-0.473, 4.991) 0.098
Positive 2.155 (-3.924, 4.211) 0.784
Negative 5.353 (2.161, 8.082) 0.020
Causal Forest DML Weak 1.804 (-0.469, 4.747) 0.137
Positive 1.703 (-3.702, 4.146) 0.922
do not target heterogeneity (difference-in-means) or impose a narrow form of317
it (linear interactions in FE regression).318
D.2.3 Empirical comparison and interpretation319
Table D13 summarizes regime-specific estimates for all methods under the320
same trimming and bootstrap scheme. Across methods, the qualitative message321
is consistent: effects are largest in the Negative regime, smaller in Weak, and322
smallest (and often near zero or negative at longer leads) in Positive. Baseline323
estimators, therefore, provide an important robustness check on directional-324
ity and regime ordering. However, the magnitude and statistical strength of325
baseline estimates vary more across specifications, reflecting stronger modeling326
assumptions and greater sensitivity to the structure of confounding.327
For these reasons, we use the DML estimators for the remainder of the anal-328
ysis and for the main conclusions. We emphasize that the baseline models are329
informative sanity checks. Still, in settings with high-dimensional confounding,330
nonlinear mechanisms, and explicit heterogeneity, DML is a more appropriate331

46Climate Variability Modulates Price-Spike Impacts
T able D14:Robustness diagnostics for regime-specific CA TEs (DML
estimators).For each estimator and sensitivity regime, we report the Placebo
effect, the RCC mean absolute change, the RSR effect, and their respective
p-values. Tests succeed ifp-values≥0.05.
Method Regime Placebo eff. Placebop RCC eff. RCCp RSR eff. RSRp
Negative 0.008 0.385 0.000 0.885 0.000 0.938
LinearDML Weak -0.004 0.807 0.002 0.808 0.002 0.500
Positive 0.012 0.615 -0.005 0.769 0.002 0.688
Negative 0.010 0.269 0.002 0.769 0.001 0.750
CausalForestDML Weak -0.004 0.731 0.002 0.731 0.002 0.500
Positive 0.012 0.615 -0.004 0.769 0.003 0.688
primary identification strategy. The baselines are reported to increase trans-332
parency and to show that the headline results are not an artifact of a single333
estimator.334
D.3 Robustness checks
We summarize a set of robustness diagnostics for the regime-specific CATEs335
of the DML estimates: placebo tests, random common cause (RCC) stress336
tests, and random subset removal (RSR). For each estimator and sensitivity337
regime (Negative, Weak, Positive), we: (i) perform a placebo test by permuting338
the treatment and refitting the model, (ii) add a random synthetic covariate339
(RCC) and recompute the CATE, and (iii) repeatedly drop random subsets of340
observations (RSR) and recompute the CATE.341
Table D14 reports, for each method-regime combination: (i) the placebo342
effect andp-value for the CATE, (ii) the mean absolute change in the CATE343
under RCC and correspondingp-values, and (iii) the new effect andp-value344
for the CATE under RSR.345
Appendix E Timing and lead–lag robustness
A potential concern in high-frequency panel designs is that the treatment346
and outcome may partially overlap in time. In our setting, the treatment347
indicator is based on a smoothed price signal, ALPS
(3)
r,t , constructed from a348
three-month rolling window that includes montht(conceptuallyt−2 :t). If349
the outcome is measured contemporaneously (Yt), then part of the information350
used to define treatment can coincide with the month in which coping responses351
are observed, complicating causal interpretation (e.g., due to within-month352
timing and simultaneity).353

Climate Variability Modulates Price-Spike Impacts47
T able E15:Lead–lag robustness: regime-specific CA TEs under out-
come leadsℓ∈ {0, . . . ,4}.Rows report regime-specific CATEs for the
Negative/Weak/Positive sensitivity regimes. Each cell shows the point esti-
mate, the 95% confidence interval, and the p-value.Nreports the post-
trimming sample size (treated/control) under the common-support restriction
0.2≤ˆe(Wi)≤0.8.
Method Leadℓ N (T/C) Negative W eak Positive
0 823 (423/400)
0.0514
(0.0255, 0.0795)
p= 0.0196
0.0206
(-0.0030, 0.0558)
p= 0.1176
-0.0070
(-0.0475, 0.0317)
p= 0.6471
1 938 (455/483)
0.0599
(0.0257, 0.0873)
p= 0.0196
0.0194
(-0.0047, 0.0499)
p= 0.0980
0.0216
(-0.0392, 0.0421)
p= 0.7843
LinearDML 2 845 (430/415)
0.0550
(0.0328, 0.0814)
p= 0.0196
0.0024
(-0.0179, 0.0472)
p= 0.4314
-0.0472
(-0.0772, 0.0049)
p= 0.1373
3 840 (419/421)
0.0675
(0.0294, 0.0894)
p= 0.0196
0.0151
(-0.0112, 0.0370)
p= 0.2745
-0.0496
(-0.0908, -0.0056)
p= 0.0392
4 777 (414/363)
0.0638
(0.0412, 0.0923)
p= 0.0196
0.0193
(-0.0145, 0.0679)
p= 0.2941
-0.0738
(-0.1054, -0.0209)
p= 0.0196
0 823 (423/400)
0.0524
(0.0256, 0.0805)
p= 0.0196
0.0199
(-0.0060, 0.0510)
p= 0.1373
-0.0125
(-0.0465, 0.0398)
p= 0.6078
1 938 (455/483)
0.0535
(0.0216, 0.0808)
p= 0.0196
0.0180
(-0.0047, 0.0475)
p= 0.1373
0.0170
(-0.0370, 0.0415)
p= 0.9216
CausalForestDML 2 845 (430/415)
0.0539
(0.0259, 0.0773)
p= 0.0196
0.0010
(-0.0159, 0.0463)
p= 0.5098
-0.0388
(-0.0676, 0.0144)
p= 0.3333
3 840 (419/421)
0.0616
(0.0226, 0.0813)
p= 0.0196
0.0174
(-0.0120, 0.0338)
p= 0.3725
-0.0464
(-0.0807, 0.0013)
p= 0.0980
4 777 (414/363)
0.0510
(0.0193, 0.0755)
p= 0.0392
0.0156
(-0.0180, 0.0529)
p= 0.3725
-0.0739
(-0.1064, -0.0165)
p= 0.0196
To assess sensitivity to this timing issue, we re-estimate the causal effects354
while varying the outcome lead:355
Yt+ℓ, ℓ∈ {0,1,2,3,4}.(E13)
The main specification usesℓ= 1 (one-month lead) to reduce contemporaneous356
overlap, whileℓ= 0 is included as a benchmark andℓ≥2 provides a lead–lag357
profile of the estimated response. In all cases, we keep the treatment definition,358
covariate set, nuisance-model selection procedure, and overlap restriction fixed.359

48Climate Variability Modulates Price-Spike Impacts
We apply the same propensity-score trimming (0.2≤ˆe(W i)≤0.8) and use a360
time-block bootstrap strategy to compute confidence intervals and p-values.361
Table E15 shows that the estimated effects are broadly stable across out-362
come leads once we adopt a dependence-aware estimation scheme (time-block363
cross-fitting and time-block bootstrap) and include lead-aligned month fixed364
effects. In particular, the Negative sensitivity regime consistently exhibits a365
positive effect acrossℓ∈ {0, . . . ,4}, with point estimates remaining of similar366
magnitude over the full lead window and typically statistically distinguishable367
from zero. Weak-regime estimates remain closer to zero and are less consis-368
tently distinguishable from zero across leads. Positive-regime estimates are369
near zero at short leads but become negative at longer leads in several spec-370
ifications; the sign change is suggestive of temporal reallocation or delayed371
adaptation dynamics, but inference remains sensitive at these longer leads372
given reduced effective information and the dependence-aware resampling.373
Two features of the design help explain why lead–lag settings remain stable.374
First, the treatment indicator is defined using a three-month moving average375
of ALPS, ALPS
(3)
r,t , soT r,t = 1 reflects sustained abnormal price conditions376
over monthst−2 :t, rather than an instantaneous shock. This exposure def-377
inition mechanically induces persistence: treatment attpartially summarizes378
recent price stress that can plausibly influence coping responses over multi-379
ple subsequent months. Because ALPS is smoothed over three months and380
price-stress states are temporally persistent, varyingℓshould be interpreted381
as a timing/alignment robustness check rather than a causal impulse-response382
curve. Second, lead-aligned month fixed effects absorb common seasonal and383
macro shocks (e.g., continent-wide price movements, survey seasonality, and384
other month-specific disturbances) that affect both treatment propensity and385
food-security outcomes. With these fixed effects, identification relies primarily386
on within-month cross-sectional contrasts across regions, which can yield the387
flatter lead profile observed.388
Sample sizes after trimming are comparable across lead choices389
(Table E15), suggesting that the observed lead–lag stability is not an artifact390
of changing overlap restrictions. Overall, these results support interpreting the391
estimated impactsespecially the elevated sensitivity in the Negative regimeas392
robust to reasonable shifts in the timing of the outcome measurement over a393
0–4 month window.394
Appendix F Regime-contrast tests
The main text reports regime-specific CATEs and observes a monotone395
ordering in point estimates (Negative>Weak∼Positive). To assess whether396
this pattern reflects statistically distinguishable differences between regimes,397
analogous to an interaction test, we use the bootstrap replicates already gen-398
erated for uncertainty quantification and compute the distribution of pairwise399
regime contrasts. Specifically, for each bootstrap replicateb= 1, . . . , B, we400

Climate Variability Modulates Price-Spike Impacts49
T able F16:Regime-contrast tests.Bootstrap distributions of pairwise dif-
ferences between regime-specific CATEs for the DML estimators. Confidence
intervals at 95%, and estimations are statistically significant ifp-values≤0.05.
Method Contrast ∆(p.p.) C.I. p-value
Linear DML
Neg – Pos 3.844 (0.909, 11.738) 0.039
Neg – Weak 4.061 (−0.083, 6.809) 0.098
Causal Forest DML
Neg – Pos 3.650 (−0.129, 10.678) 0.078
Neg – Weak 3.549 (−0.446, 6.572) 0.137
compute401
∆(b) Neg−Weak =bτ(b) Neg −bτ(b) Weak,∆ (b) Neg−Pos =bτ(b) Neg −bτ(b) Pos.(F14)
We then report percentile 95% confidence intervals for ∆ and a two-sided402
bootstrapp-value based on the empirical sign probability,403
p= 2 min{Pr(∆ (b) ≥0),Pr(∆ (b) ≤0)}.(F15)
This procedure directly tests whether the Negative-regime effect is larger than404
the effects in the other regimes under the same dependence-aware resampling405
scheme used throughout the paper.406
AcrossB=1000 time-block bootstrap replicates, the Neg–Pos contrast is407
statistically significant for the Linear DML estimator (Neg–Pos: ∆ = 3.844408
p.p., 95% CI (0.909,11.738),p= 0.039) and directionally consistent but not409
significant for the Causal Forest DML estimator (Neg–Pos: ∆ = 3.650 p.p.,410
95% CI (−0.129,10.678),p= 0.078). In contrast, the Neg–Weak contrast is411
positive in both estimators but not statistically distinguishable from zero at412
conventional levels (Linear DML:p= 0.098; Causal Forest DML:p= 0.137).413
Overall, these results support a directional ordering of point estimates, with the414
strongest evidence for between-regime separation occurring in the Negative-415
versus-Positive comparison under the Linear DML specification (Table F16).416
It is important to note that rejecting the nullτ Neg = 0 does not auto-417
matically imply rejectingτ Neg −τ Weak = 0. The between-regime contrast is a418
different estimand with its own sampling variability. In particular,419
Var(bτNeg −bτWeak) = Var(bτNeg) + Var(bτWeak)−2 Cov(bτNeg,bτWeak),(F16)
so even ifbτNeg is estimated precisely, uncertainty inbτWeak (and the covariance420
term) can make the contrast substantially noisier. As a result, a regime-specific421
effect can be statistically distinguishable from zero while the corresponding422
difference between regimes remains statistically indistinguishable from zero423
under the same bootstrap-based inference.424
