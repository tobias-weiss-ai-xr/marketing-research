---
title: 'Job Satisfaction Through the Lens of Social Media: Rural--Urban Patterns in the U.S'
url: https://arxiv.org/abs/2512.05144
category: social-media
subcategory: empirical
date: 2025-12
venue: ''
authors:
- Stefano M Iacus
- Giuseppe Porro
source: arxiv
pdf_url: https://arxiv.org/pdf/2512.05144
pages: 18
chars: 37332
fetched_at: '2026-11-08T13:05:49+00:00'
kb_version: 1
---

# Job Satisfaction Through the Lens of Social Media: Rural--Urban Patterns in the U.S

Job Satisfaction Through the Lens of Social Media:
Rural–Urban Patterns in the U.S.
Stefano M. Iacus ∗ Giuseppe Porro †
8th December 2025
Abstract
We analyze a novel large-scale social-media-based measure of U.S. job satisfaction,
constructed by applying a fine-tuned large language model to 2.6 billion georeferenced
tweets, and link it to county-level labor market conditions (2013-2023). Logistic regres-
sions show that rural counties consistently report lower job satisfaction sentiment than
urban ones, but this gap decreases under tight labor markets. In contrast to widening
rural-urban income disparities, perceived job quality converges when unemployment is
low, suggesting that labor market slack, not income alone, drives spatial inequality in
subjective work-related well-being.
JEL classification:J28; R23; J64; I31; C55.
Keywords:job satisfaction; rural–urban divide; social media; subjective well-being.
1 Introduction
The growing literature on subjective well-being (SWB) has increasingly examined the U.S.
rural–urban divide, creating a research stream that spans psychology, sociology, economics,
and political science. In addition to studies on differences in life satisfaction (Atherton
et al., 2024), scholars have examined the relationship between local context and political
orientation, which has in turn triggered a lively public debate (see, e.g., Gimpel and Reeves
(2024); Brown and Mettler (2024)).
∗Harvard University, Institute for Quantitative Social Science, Cambridge (MA), USA. E-mail:
siacus@iq.harvard.edu.
†Department of Law, Economics and Culture, University of Insubria, Como, Italy. E-mail:
giuseppe.porro@uninsubria.it.
1
arXiv:2512.05144v1  [econ.GN]  2 Dec 2025

Less effort has been devoted to economic aspects of SWB, particularly those related to
the labor market, i.e. job satisfaction, likely due to the lack of availability of fine-grained
nationwide data. In fact, research on disparities in job satisfaction between U.S. rural and
urban labor markets has relied, at best, on state-level small-sample surveys (Martinson and
Wilkening (1984)). Other studies have examined satisfaction within specific worker cat-
egories (Flores-Saviaga et al. (2020); Vick (2016); Fossum (1974)) or investigated particular
aspects of employment, such as remote work (Paul (2022)). More recently, scholarly atten-
tion has shifted toward objective measures of job quality (Carnevale et al. (2024)), rather
than subjective satisfaction.
We use a new social media based indicator to study job-related satisfaction among rural
and urban counties in the United States between 2013 and 2023, and relate it to well-
documented trends in U.S. labor markets. Despite some apparently paradoxical patterns in
subjective indicators, our results are broadly consistent with Autor’s interpretation of recent
urban versus rural labor-market dynamics (Autor, 2019).
2 U.S. Job satisfaction 2013–2023
Asnotedabove, thelimitedpriorstudiesdidnotreachconclusiveresultsregardingdifferences
in job satisfaction across U.S. rural and urban contexts. At most, some evidence suggests
a possible non-linear relationship between the degree of urbanization and job satisfaction,
with individuals born in small towns reporting higher levels of satisfaction than those from
open country, villages, or larger cities (Martinson and Wilkening (1984)).
Our new dataset enables a nationwide county-level assessment of SWB dimensions –
including job satisfaction – since 2013 to 2023, a decade characterized by a progressive
decline in unemployment rates, with the exception of the pandemic period (U.S. Bureau of
Labor Statistics (2025)).
2.1 The dataset
The job satisfaction social media indicator is part of a larger set of indicators from the
projectThe Human Flourishing Geographic Index(HFGI) (Iacus et al., 2025), conceptually
inspired by the Harvard’s Human Flourishing Program (VanderWeele, 2017), which defines
flourishing across six areas of well-being: happiness and life satisfaction, mental and physical
health, meaning and purpose, character and virtue, close social relationships, and material
and financial stability. The HFGI dataset offers high-resolution indicators at county and
state level for the United States at both monthly and yearly frequency. It has been obtained
2

analyzing approximately 2.6 billion geo-referenced tweets from the Harvard CGA Geotweet
Archive (Lewis and Kakkar, 2016), classified using a fine-tuned large language model (LLM)
(Carammia et al., 2024). The dataset spans January 2013 to June 2023. The details on
how these indicators have been computed through generative AI analysis are given in the
Supplementary Material as well as in Carammia et al. (2024); Iacus et al. (2025).
The social media indicatorjobsathas been aggregated at county level. Its values vary
in the interval[−1,1]. The indicator comes with the counts of tweets used to evaluate it, i.e.,
those tweets containing expressions of satisfaction or dissatisfaction with the job situation.
This variable is calledTweetVolin models (1) and (S1) below.
In addition to our social media indicator, we provide a set of control variables.
We make use of the 2023 Rural-Urban Continuum Codes (rural) that distinguish U.S.
metropolitan (metro, values 1-3) counties by the population size of their metro area, and non-
metropolitan (nonmetro, values 4-9) counties by their degree of urbanization and adjacency
to a metro area (U.S. Department of Agriculture, Economic Research Service, 2024).
To control for county-level economic conditions, we include a measure of household in-
come derived from the American Community Survey (ACS) 5-Year Estimates (acs5), which
provides reliable small-area averages based on multi-year data (U.S. Census Bureau, 2023).
Monthly county-level labor-market indicators are obtained from the U.S. Bureau of Labor
Statistics (BLS) (U.S. Bureau of Labor Statistics, 2024b) Local Area Unemployment Stat-
istics (LAUS) program via the public BLS API (U.S. Bureau of Labor Statistics, 2024a).
For each county, we collected non-seasonally-adjusted monthly unemployment rates and
labor force data for period 2013-2023, as indicators of local labor-market conditions (named
UnemploymentRateandLaborForcerespectively in models (1) and (S1) below). To control
for seasonality, we include monthly and yearly fixed effects in the models.
Figure 1 plots the monthly national unemployment rate and labor force, which are con-
structed by aggregating county-level data, together with a version of thejobsatindicator
that has been rescaled to reflect monthly variation in the number of contributing counties.
This adjustment is applied only for visualization. The econometric analyses in Section 2.2
rely on the unmodified county-level indicators.
Figure 2 compares the spatial distribution of (i) the averagejobsatindicator rescaled
from its original[−1,1]range to[0,1]to facilitate the visual interpretation, and (ii) the
average unemployment rate, both computed at the county level over the 2013–2023 period.
For each county, we first aggregate monthly observations into a single time-averaged value,
noting that the set of counties contributing data varies slightly across years depending on
tweet availability and BLS reporting. The maps therefore depict long-run spatial patterns
based on all available observations for each county. The use of perceptually uniform viridis
3

Figure 1: Monthly national unemployment rate (%) and labor force (in million) obtained through
county-levelmonthlyaggregationcomparedtothesocialmediaindicatorjobsatrescaledtonational
level to account for the missing counties in some years/months.
5.0
7.5
10.0
12.5
2014 2016 2018 2020 2022
Unempl. rate (%)
140
145
150
155
160
2014 2016 2018 2020 2022
Labor force (m)
0.00
0.25
0.50
2014 2016 2018 2020 2022
Job−satisfaction
color scales ensures comparability across panels. Together, the two maps provide a spatial
overview of baseline labor-market conditions and expressed job-related sentiment, which
serve as the foundation for the econometric analysis presented below.
2.2 A Rural–Urban Disparity?
To investigate the determinants of job-satisfaction sentiment (ourjobsatindicator), we
estimate a sequence of four nested logistic regression models that progressively incorporate
additional socioeconomic and contextual covariates. We introduce a binary county-month
outcome variableY itm =1 {jobsatitm>0}, which equals one if the average job-satisfaction score
incountyiattime(t, m)ispositiveandzerootherwise. Model(1)includesthecounty–month
unemployment rate (UnemploymentRate) as the main explanatory variable, together with the
size of the county labor force (in thousands,LaborForce), number of tweets used to calculate
the indicator (TweetVol), and year and month fixed effects. We use labor force rather than
population to better capture the economic relevance of counties of different sizes: the labor
force reflects the share of residents directly exposed to labor market conditions, which is more
theoretically aligned with job-related sentiment than total population. Model (2) augments
this baseline specification with the ACS 5-year income estimate (ACS5), capturing longer-
term economic well-being. Model (3) introduces an interaction between the unemployment
4

Job satisfaction
(rescaled 0−1)
0 (low)
0.5 (threshold)
1 (high)
Indicator rescaled from [−1,1] to [0,1]; 0.5 corresponds to neutral sentiment
Average Job Satisfaction (2013−2023)
Mean unemployment rate (%)
5
10
15
20
County−level monthly unemployment averaged over time
Average Unemployment Rate (2013−2023)
Figure 2: County-level averages of job-satisfaction sentiment (rescaled to the interval [0,1]) and
unemployment rates in the United States, 2013–2023. The top panel reports the rescaledjobsat
indicator based on social-media sentiment, mapped using a perceptually uniform viridis color scale;
higher values indicate more positive job-related sentiment. The bottom panel shows the mean
county-level unemployment rate over the same period, using an inverted viridis color scale so that
brighter areas correspond to lower unemployment. Counties with missing data in specific years
contribute only when observed; maps reflect the average over available months for each county.
5

rate and labor force. This interaction allows the marginal association between unemployment
and job-satisfaction sentiment to vary with the economic scale of the county: in small labor
markets, changes in unemployment may carry different informational or economic weight
than in large ones. Finally, Model (4) adds rurality (Rural) to capture spatial variation
in socioeconomic context, and introduces state fixed effects to absorb persistent cross-state
heterogeneity. All models include year (γ) and month (δ) fixed effects to absorb temporal
shocks and seasonal patterns. The fully specified Model (4), which forms the basis of our
interpretation and predictive analyses, is given in equation (1) and incorporates state fixed
effects (θs) to account for national specific characteristics. Estimated coefficients for all four
models are reported in Table 1, with fixed effects omitted for brevity. These fixed effects
follow standard panel-data practice and help control for unobserved temporal heterogeneity
arising from macroeconomic shocks (e.g., the COVID-19 pandemic), national policy changes,
and other broad influences affecting all counties (Wooldridge, 2010; Angrist and Pischke,
2009).
Pr(Yitm = 1) =logit −1

β0 +β 1 UnemploymentRateitm +β 2
LaborForceitm
1000
+β 3 UnemploymentRateitm × LaborForceitm 1000
+β 4
ACS5itm
1000 +β 5 Rurali +β 6 TweetVolitm
+γ t +δ m +θ s(i)

,
(1)
where the indexs(i)denotes the state of countyi,γt are the year fixed effects,δm the month
fixed effects, andθs(i) are the state fixed effects that absorb time-invariant differences across
states. To assess whether our results are sensitive to the dichotomization of the sentiment
measure into a binary outcome, we also estimate a traditional OLS model (see equation (S1))
following the same nested specification strategy described above. The results are presented
in the Supplementary Material in Table S2 and they confirm the results of the logit model in
Table 1. All inference is based on heteroskedasticity-robust standard errors clustered at the
county level, which accounts for arbitrary within-county correlation in the error structure
over time. This correction is standard in panel-data settings with many groups and relatively
long time series, and ensures valid asymptotic inference under general forms of within-cluster
dependence (White, 1980; Liang and Zeger, 1986; Cameron and Miller, 2015).
6

2.3 Analysis of the results
The logistic regression estimates reported in Table 1 indicate a highly stable and theoret-
ically coherent set of relationships between local socioeconomic conditions and expressed
job-satisfaction sentiment. Across all specifications, the unemployment rate emerges as the
strongest and most robust predictor: higher unemployment is consistently associated with a
lower probability that county-month sentiment is positive, even after conditioning on income,
rurality, tweet volume, labor-force size, and a full set of temporal and state fixed effects. The
sequential inclusion of ACS5 income, the interaction between unemployment and labor force,
and rurality attenuates the unemployment coefficient only modestly. All three variables enter
with statistically significant signs: higher income is associated with higher job satisfaction,
aligning with expectations; more rural counties exhibit significantly lower sentiment net of
labor-market conditions and socioeconomic controls; and the negative interaction term in-
dicates that the adverse association between unemployment and job satisfaction is stronger
in counties with larger labor forces. Notice that the impact of rurality on job satisfaction is
negative, while the effect of rurality on life satisfaction is, in most of the literature, positive
(Iacus and Porro, 2025).
The average marginal effects reported in Table 2 provide a direct quantification of the
substantive importance of each predictor in the logit model. Higher unemployment rates
are associated with a lower probability that job-satisfaction sentiment is positive, even after
conditioning on socioeconomic characteristics and fixed effects, although the magnitude of
the effect is moderate when expressed in probability units. County income (ACS5) exhibits
a positive and statistically precise relationship with job-satisfaction sentiment, indicating
that counties with higher economic resources tend to display higher levels of expressed job
satisfaction. Rurality remains one of the strongest predictors: moving one step toward a
more rural classification reduces the probability of positive sentiment by nearly one percent-
age point on average, net of controls. Labor-force size has a small but positive marginal
effect, consistent with slightly higher job satisfaction in larger local labor markets, while the
interaction between unemployment and labor force contributes an additional, though mod-
est, strengthening of the negative impact of unemployment in these larger markets. Tweet
volume enters with a small but negative marginal effect, suggesting that months in which
more users discuss work topics tend to coincide with more negative sentiment overall. On
the whole, the AMEs corroborate the core conclusions from the full logit specification, while
translating them into effect sizes that are directly interpretable on the probability scale.
Figure 3 visualizes the relationship between unemployment and job satisfaction across the
rural–urban continuum. Predicted probabilities are obtained from equation (1) by evaluating
the model over a grid of unemployment rates (0–30%) and rurality levels (1–9). Continuous
7

covariates (labor force, ACS5 income, and tweet volume) are held at their median values. To
account for temporal and spatial heterogeneity, predictions are averaged over the empirical
distribution of month and state fixed effects. The final curves represent the average difference
∆P=P(jobsat>0|rural=r)−P(jobsat>0|rural= 1)between each rurality level
(r= 2, . . . ,9) and the most urban counties (r= 1).
Figure 3 shows that the curves converge at low unemployment rates, indicating a partial
rural catch-up, but diverge as unemployment rises, revealing an increasing rural disadvantage
under weaker labor-market conditions.
Table 1: Sequential logit specifications for the probability that county-month job-satisfaction sen-
timent is positive (P(jobsat>0)). Model (1) includes unemployment, labor force, tweet volume,
and year and month fixed effects; Model (2) adds ACS5 income; Model (3) adds an unemployment
time labor force interaction; Model (4) further includes rurality and state fixed effects. Fixed effects
are included but omitted from the table.
Dependent Variable:P(jobsat>0)
Model: (1) (2) (3) (4)
Variables
Unemployment rate -0.0764 ∗∗∗ -0.0423∗∗∗ -0.0299∗∗∗ -0.0101∗
(0.0047) (0.0050) (0.0051) (0.0052)
Labor force (thousands persons) 0.0027 ∗∗∗ 0.0016∗∗∗ 0.0039∗∗∗ 0.0033∗∗∗
(0.0007) (0.0006) (0.0007) (0.0007)
Valid jobsat tweets -0.0002 ∗∗∗ -0.0001∗∗∗ -0.0001∗∗∗ -0.0001∗∗∗
(3.14×10 −5) (3.08×10 −5) (3.17×10 −5) (3.3×10 −5)
ACS5 income (thousands USD) 0.0221 ∗∗∗ 0.0210∗∗∗ 0.0140∗∗∗
(0.0018) (0.0016) (0.0016)
Unemployment rate×Labor force (thousands persons) -0.0003 ∗∗∗ -0.0003∗∗∗
(4.84×10 −5) (4.38×10 −5)
Rurality -0.0871∗∗∗
(0.0063)
Fixed-effects
year Yes Yes Yes Yes
month Yes Yes Yes Yes
State Yes
Fit statistics
Observations 282,079 282,065 282,065 281,941
Pseudo R 2 0.39363 0.39950 0.40079 0.42067
Squared Correlation 0.44230 0.44420 0.44410 0.46273
AIC 181,018.9 179,263.8 178,881.2 173,009.2
BIC 181,282.6 179,538.1 179,166.1 173,810.9
Clustered standard-errors (by county) in parentheses
Signif. Codes: ***: 0.01, **: 0.05, *: 0.1
8

Table 2: Average marginal effects from the logit model in equation (1). Effects are averaged across
county-month observations; year, month, and state fixed effects are included but not shown. Stand-
ard errors clustered at the county level.
Variable AME SE zp-value
Unemployment rate -0.00208 0.00046 -4.49 6.966e −06
Labor force (thousands persons) 0.00016 0.00004 3.78 0.0001567
ACS5 income (thousands USD) 0.00131 0.00015 8.84 9.217e −19
Rurality -0.00809 0.00058 -13.87 9.434e −44
Valid jobsat tweets -0.00001 0.00000 -3.24 0.001214
Unemp.×labor force (interaction) -0.00002 0.00000 -5.86 4.654e −09
Figure 3: Average difference∆P=P(jobsat>0|rural=r)−P(jobsat>0|rural= 1),
between each rurality level (r= 2, . . . ,9) and the most urban counties (r= 1), plotted across
unemployment rates. Predicted probabilities are obtained from the logit model in equation (1) and
averaged over the empirical distribution of year, month, and state fixed effects.
−0.06
−0.04
−0.02
0.00
0 10 20 30
Unemployment Rate (%)
∆P
Rural Level
2
3
4
5
6
7
8
9
P(jobsat > 0 | rural=r) − P(jobsat > 0 | rural=1)
9

3 Discussion: what rural–urban convergence, if any?
Between 2013 and 2023, U.S. unemployment rates experienced a steady decline, interrupted
only during the pandemic years (U.S. Bureau of Labor Statistics (2025)). Over the same
period, however, rural–urban inequality increased in multiple domains. Income gaps widened
(Hardy et al. (2025)), employment opportunities grew more unevenly across space (Dumont
(2023)), and poverty rates in nonmetropolitan areas remained persistently higher than in
metropolitan ones (Farrigan et al. (2024)). In short, the economic expansion of the last dec-
ade did not generate broad-based rural–urban convergence in objective economic conditions.
This period also coincided with pronounced job polarization, characterized by an expansion
of employment at both the low-skill and high-skill ends of the labor market and a relative
decline in mid-skill occupations. These developments reflect deeper structural transforma-
tions associated with technological change, task reallocation, and the declining demand for
routine work (Acemoglu and Autor (2011); Acemoglu and Restrepo (2019); Autor (2019)).
Importantly, these dynamics have not affected rural and urban areas symmetrically. Earn-
ings dispersion, particularly by education level, increased more in urban labor markets than
in rural ones (Autor (2019)). As Hardy et al. (2025) observe, the rural–urban divergence
in household income is driven largely by widening gaps at the top of the distribution, with
only limited convergence at the bottom. These differences help contextualize the patterns
we observe in our job-satisfaction indicator. Declining unemployment rates are associated
with higher job-satisfaction sentiment across all counties, and the overall urban-rural ranking
remains unchanged: more urban counties exhibit higher average sentiment than more rural
ones. However, the magnitude of this rural disadvantage is not constant. Figure 3 shows
that the predicted gap in job satisfaction narrows substantially at low unemployment rates,
whereas it widens when unemployment is higher. This form of conditional convergence is
consistent with a setting in which labor-market tightness disproportionately benefits res-
idents of rural counties, even as average levels of job satisfaction remain higher in urban
areas.
One possible explanation relates to differences in the evolution of earnings dispersion. If
relative income concerns (Duesenberry, 1949) play a role in shaping job satisfaction, rising
inequality within urban counties may partly offset the positive effect of declining unemploy-
ment on perceived job quality. Rural counties, where earnings dispersion has increased less,
may experience larger subjective gains when labor markets tighten. While our empirical
design does not directly test this mechanism, the conditional convergence pattern we estim-
ate is directionally consistent with these documented structural differences. This stands in
contrast to broader life-satisfaction and happiness indicators, which in our related HFGI ana-
10

lyses exhibit weaker or inconsistent associations with relative income dynamics (Deaton and
Stone, 2013; Iacus and Porro, 2025). Job satisfaction, being more domain-specific and closely
tied to labor-market conditions, may be more sensitive to relative economic position. Finally,
the conditional improvement in predicted job satisfaction among rural counties aligns with
aspects of Autor (2019)’s interpretation of changing opportunities for less-educated workers.
The slowdown in migration of low-skill labor into urban areas may place upward pressure
on urban wages, but demographic change, especially population aging, has also increased
demand for labor-intensive, lower-skill services in nonmetropolitan areas. These shifts may
be expanding employment opportunities in rural counties in ways not fully captured by
standard income measures. The patterns in our data, i.e., higher predicted gains in job sat-
isfaction for rural counties under tight labor markets, are consistent with this interpretation
and suggest that perceived job conditions may be improving more quickly in lower-density
labor markets when unemployment is low.
4 Conclusions
The econometric analysis in this work shows that the rural–urban gap in job satisfaction is
not fixed, but varies systematically with local labor-market conditions. Higher unemploy-
ment lowers job satisfaction across all counties, and this negative effect is stronger in rural
areas. When unemployment is low, however, the estimated rural disadvantagenarrows. This
pattern reflects a form of conditional convergence inperceivedjob quality. In this respect,
these findings complement Autor’s evidence by showing that, even as rural-urban income
disparities widen, perceived job satisfaction converges conditionally under tight labor mar-
kets. Subjective assessments of job quality improve relatively more in rural counties when
unemployment is low, revealing a dimension of well-being in which residents of more rural
counties appear to catch up. This conditional and perception-based convergence represents
a new and economically meaningful feature of the U.S. labor market. Although income gaps
continue to widen, our econometric results suggest that rural labor markets realize larger
gains in subjective job satisfaction when labor demand is strong. Policies that help sus-
tain tight labor-market conditions in non-metropolitan areas, such as targeted job creation,
support for care and service sectors, and investments that stabilize local employment, could
therefore yield meaningful improvements in perceived job quality. Because job satisfaction
is linked to retention, productivity, and migration decisions, such policies may strengthen
rural labor markets even without immediate income convergence.
11

References
D. Acemoglu and D. Autor. Chapter 12: Skills, tasks and technologies: Implications
for employment and earnings. In D. Card and O. Ashenfelter, editors,Handbook
of Labor Economics, volume 4, pages 1043–1171. Elsevier, 2011. doi: https://doi.
org/10.1016/S0169-7218(11)02410-5. URLhttps://www.sciencedirect.com/science/
article/pii/S0169721811024105.
D. Acemoglu and P. Restrepo. Automation and new tasks: How technology displaces and
reinstates labor.Journal of Economic Perspectives, 33(2):3–30, May 2019. doi: 10.1257/
jep.33.2.3. URLhttps://www.aeaweb.org/articles?id=10.1257/jep.33.2.3.
J.D.AngristandJ.-S.Pischke.Mostly Harmless Econometrics: An Empiricist’s Companion.
Princeton University Press, Princeton, NJ, 2009. ISBN 978-0-691-12035-5.
O. E. Atherton, E. C. Willroth, E. K. Graham, J. Luo, D. K. Mroczek, and M. W. Lewis-
Thames. Rural–urbandifferencesinpersonalitytraitsandwell-beinginadulthood.Journal
of Personality, 92(1):73–87, 2024. doi: https://doi.org/10.1111/jopy.12818. URLhttps:
//onlinelibrary.wiley.com/doi/abs/10.1111/jopy.12818.
D. H. Autor. Work of the past, work of the future.AEA Papers and Proceedings, 109:1–32,
May 2019. doi: 10.1257/pandp.20191110. URLhttps://www.aeaweb.org/articles?id=
10.1257/pandp.20191110.
T. E. Brown and S. Mettler. Sequential polarization: The development of the rural-urban
political divide, 1976–2020.Perspectives on Politics, 22(3):630–658, 2024. doi: 10.1017/
S1537592723002918.
A. C. Cameron and D. L. Miller. A practitioner’s guide to cluster-robust inference.Journal
of Human Resources, 50(2):317–372, 2015.
M. Carammia, S. M. Iacus, and G. Porro. Rethinking scale: The efficacy of fine-tuned
open-source llms in large-scale reproducible social science research, 2024. URLhttps:
//arxiv.org/abs/2411.00890.
A. P. Carnevale, L. Kam, and M. V. D. Werf. Small towns, big opportunities: Many work-
ers in rural areas have good jobs, but these areas need greater investment in education,
training, and career counseling. Technical report, Georgetown University Center on Edu-
cation and the Workforce, Washington, DC, 2024. URLhttps://cew.georgetown.edu/
ruralgoodjobs. Accessed: 2025-08-21.
12

A. Deaton and A. A. Stone. Two happiness puzzles.American Economic Review, 103(3):591–
97, May 2013. doi: 10.1257/aer.103.3.591. URLhttps://www.aeaweb.org/articles?
id=10.1257/aer.103.3.591.
J.S.Duesenberry.Income, Saving and the Theory of Consumer Behavior. HarvardUniversity
Press, Cambridge, MA, 1949.
A. Dumont. Changes in the u.s. economy and rural–urban employment disparities.FEDS
Notes, Jan. 2023. doi: 10.17016/2380-7172.3428. URLhttps://doi.org/10.17016/
2380-7172.3428.
T. Farrigan, B. Genetin, A. Sanders, J. Pender, K. L. Thomas, R. Winkler, J. Cromartie,
and p. United States. Department of Agriculture. Economic Research Service, sponsor-
ing body. Rural america at a glance, 2024. URLhttps://www.ers.usda.gov/webdocs/
publications/110351/eib-282.pdf.
C. Flores-Saviaga, Y. Li, B. V. Hanrahan, J. Bigham, and S. Savage. The challenges of crowd
workers in rural and urban america, 2020. URLhttps://arxiv.org/abs/2012.15211.
J. A. Fossum. Urban-rural differences in job satisfaction.ILR Review, 27(3):405–409, 1974.
ISSN 00197939, 2162271X. URLhttp://www.jstor.org/stable/2521619.
J. G. Gimpel and A. Reeves. The urban-rural divide and residential contentment as
antecedents of political ideology.Cities, 146:104720, 2024. ISSN 0264-2751. doi:
https://doi.org/10.1016/j.cities.2023.104720. URLhttps://www.sciencedirect.com/
science/article/pii/S0264275123005322.
B. L. Hardy, S. Holla, E. S. Krause, and J. P. Ziliak. Stalled progress? five decades of
black–white and rural–urban income gaps.RSF: The Russell Sage Foundation Journal of
the Social Sciences, 11(2):115–136, 2025. ISSN 2377-8253. doi: 10.7758/RSF.2025.11.2.06.
URLhttps://www.rsfjournal.org/content/11/2/115.
S. M. Iacus and G. Porro. Two americas of well-being: Divergent rural-urban patterns of
life satisfaction and happiness from 2.6 b social media posts, 2025. URLhttps://arxiv.
org/abs/2511.10542.
S. M. Iacus, D. Jain, A. Nasuto, G. Porro, M. Carammia, and A. Vezzulli. The human
flourishing geographic index: A county-level dataset for the united states, 2013–2023,
2025. URLhttps://arxiv.org/abs/2511.03915.
13

B. Lewis and D. Kakkar. Harvard CGA Geotweet Archive v2.0, 2016. URLhttps://doi.
org/10.7910/DVN/3NCMB6.
K.-Y. Liang and S. L. Zeger. Longitudinal data analysis using generalized linear models.
Biometrika, 73(1):13–22, 1986.
O. B. Martinson and E. A. Wilkening. Rural-urban differences in job satisfaction: Further
evidence.The Academy of Management Journal, 27(1):199–206, 1984. ISSN 00014273.
URLhttp://www.jstor.org/stable/255968.
J. Paul. Work from home behaviors among u.s. urban and rural residents.Journal
of Rural Studies, 96:101–111, 2022. ISSN 0743-0167. doi: https://doi.org/10.1016/j.
jrurstud.2022.10.017. URLhttps://www.sciencedirect.com/science/article/pii/
S0743016722002534.
U.S. Bureau of Labor Statistics. BLS Public Data API, 2024a. URLhttps://www.bls.
gov/developers/. Accessed through theblsAPIR package.
U.S. Bureau of Labor Statistics. Local Area Unemployment Statistics (LAUS), 2024b. URL
https://www.bls.gov/lau/. Dataset accessed via the BLS Public Data API.
U.S. Bureau of Labor Statistics. Civilian unemployment rate, 2013–2023, 2025. URLhttps:
//www.bls.gov/charts/employment-situation/civilian-unemployment-rate.htm.
U.S. Department of Labor, last modified March 5, 2025.
U.S. Census Bureau. American community survey 5-year estimates. Technical re-
port, U.S. Department of Commerce, 2023. Retrieved fromhttps://www.census.gov/
programs-surveys/acs.
U.S. Department of Agriculture, Economic Research Service. Rural-urban continuum
codes.https://www.ers.usda.gov/data-products/rural-urban-continuum-codes/,
Jan. 2024. Accessed: 2025-08-01.
T. J. VanderWeele. On the promotion of human flourishing.Proceedings of the National
Academy of Sciences, 114(31):8148–8156, 2017. doi: 10.1073/pnas.1702996114. URL
https://www.pnas.org/doi/abs/10.1073/pnas.1702996114.
B. Vick. Analyzing rural versus urban differences in career dissatisfaction and plans to leave
among pennsylvanian physicians.The Journal of Rural Health, 32(2):164–175, 2016. doi:
https://doi.org/10.1111/jrh.12139. URLhttps://onlinelibrary.wiley.com/doi/abs/
10.1111/jrh.12139.
14

H. White. A heteroskedasticity-consistent covariance matrix estimator and a direct test for
heteroskedasticity.Econometrica, 48(4):817–838, 1980.
J. M. Wooldridge.Econometric Analysis of Cross Section and Panel Data. MIT Press,
Cambridge, MA, 2nd edition, 2010. ISBN 978-0-262-23258-6.
15

Supplementary Material
Large language model fine-tuning and construction of social media
based indicators
We summarize here how the tweet-level indicator ofjob satisfactionwas derived using fine-
tuned large language models, and further aggregated to the county level. A full meth-
odological account of the broader Human Flourishing Geographic Index (HFGI) dataset,
including additional well-being dimensions, validation benchmarks, and reproducibility re-
sources is provided in Iacus et al. (2025). Here we describe only the indicator used in this
work:jobsat.
Fine-tuning and classification pipeline
We trained and validated a fine-tuned large language model (LLM) to classify short social-
media texts according to multiple flourishing-related constructs. The training corpus com-
prised 4,581 manually annotated tweets, selected from an initial pool of 10,000 messages
sampled across topics, years, and geographies to ensure linguistic diversity. Each tweet was
independently labeled by human coders following standardized dimension-specific guidelines.
Forjobsat, coders indicated whether the tweet referred to the construct and, if so, whether
the expressed tone waslow,medium, orhigh. These labels were used to fine-tune an
instruction-following generative model (LLaMA family), optimizing cross-entropy loss across
the three classes.
The fine-tuned model produced a JSON-formatted classification for each tweet, return-
ing both the target label and confidence score. Evaluation on a held-out test set yielded
accuracies around 0.87 depending on the dimension, with consistent precision-recall bal-
ance. Post-hoc validation involved manual review of ambiguous cases to verify conceptual
alignment with the human flourishing framework (see Iacus et al. (2025) for details).
Scaling and county-level aggregation
We later transformed the three-level scale (“low", “medium", “high”) as:−1(negative),+0.5
(somewhat positive),+1(positive) and set0if a tweet does not contain expressions related
to job satisfaction (not-present). Notice that low maps to the opposite concept. For example
“job satisfaction" = “low" means “unsatisfied on the job".
Each classified tweet was geolocated to a U.S. county using the Harvard CGA pipeline.
Tweets with ambiguous or low-confidence geotags were excluded. For every county-month-
16

dimension triple, we computed the mean and standard deviation per geographical region
(county/state) and temporal frequency (month/year).
Labor-market variable selection
For county-level labor-market indicators we rely on those that can be obtained from the
U.S. Bureau of Labor Statistics (BLS) (U.S. Bureau of Labor Statistics, 2024b) Local Area
Unemployment Statistics (LAUS) program. Table S1 shows that our job satisfactionjobsat
indicator is correlated more to theLabor forceindicator and to theUnemployment rateat
county level than to the other labor market indicators, so we selected these two measures as
control variables. Table S1 shows that our job-satisfaction indicatorjobsatis moderately
negatively correlated with theUnemployment rateand weakly positively correlated with
theLabor forcemeasure at the county level, while its associations with other covariates
are smaller in magnitude. We therefore selected theUnemployment rateand theLabor
forceas our primary labor-market controls in the econometric analysis. As the variable
Labor forceis almost perfectly correlated with thePopulationindicator, we include only
the former in the models. The rest of the variables are defined in Section 2.1.
Table S1: Pairwise correlations betweenjobsatand other socio-economic covariates.
Employed Labor force Unemployed Unemployment rate Rural Population TweetVol ACS5
0.04 0.04 -0.02 -0.31 -0.13 0.03 -0.01 0.13
Alternative OLS specification
To assess whether our results from the model in equation (1) in Section 2.2 are sensitive
to the dichotomization of the sentiment measure into a binary outcome, we also estimate
a traditional OLS model as in equation (S1) below, following the same nested specification
strategy described in Section 2.2.
jobsatitm =β 0 +β 1 UnemploymentRateitm +β 2
LaborForceitm
1000
+β 3 UnemploymentRateitm × LaborForceitm 1000
+β 4
ACS5itm
1000 +β 5 Rurali +β 6 TweetVolitm
+γ t +δ m +θ s(i) +ε itm,
(S1)
whereε itm is an idiosyncratic error term with zero mean, representing unobserved determin-
antsofjobsat itm conditionalonthecovariatesandfixedeffects, i.e.E[ε itm |X itm, γt, δm, θs(i)] =
17

0.
Table S2: OLS regression results for county-month job-satisfaction sentiment (jobsat). The four
modelsfollowthesamenestedstructureasinTable1. Allspecificationsincludeyearandmonthfixed
effects; Model (4) additionally includes state fixed effects. Standard errors are heteroskedasticity-
robust and clustered at the county level.
Dependent variable:
jobsat
(1) (2) (3) (4)
Unemployment rate−0.01300 ∗∗∗ −0.01144∗∗∗ −0.01142∗∗∗ −0.00727∗∗∗
(0.00055) (0.00056) (0.00057) (0.00049)
Labor force (thousands persons) 0.00004 ∗∗∗ 0.00002 0.00002 0.00004 ∗∗
(0.00002) (0.00001) (0.00002) (0.00001)
ACS5 income (thousands USD) 0.00081 ∗∗∗ 0.00081∗∗∗ 0.00019∗
(0.00011) (0.00011) (0.00011)
Rurality −0.00749∗∗∗
(0.00055)
Valid jobsat tweets−0.00001 ∗∗∗ −0.00001∗∗∗ −0.00001∗∗∗ −0.00001∗∗∗
(0.000002) (0.000002) (0.000002) (0.000002)
Unemployment rate×Labor force (thousands)−0.0000004−0.000001
(0.000001) (0.000001)
Constant−0.06715 ∗∗∗ −0.11624∗∗∗ −0.11632∗∗∗ −0.07870∗∗∗
(0.00510) (0.00816) (0.00820) (0.01031)
Akaike Inf. Crit. 3010.23 2466.65 2468.48 -8807.15
Year & month FE Yes Yes Yes Yes
State FE No No No Yes
Clustered SE (county) Yes Yes Yes Yes
Observations 282,079 282,065 282,065 282,065
R2 0.62892 0.62963 0.62963 0.64427
Adjusted R 2 0.62889 0.62960 0.62960 0.64417
Note: ∗p<0.1; ∗∗p<0.05; ∗∗∗p<0.01
Heteroskedasticity-robust standard errors clustered at the county level (StateCounty).
18
