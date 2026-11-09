---
title: 'Households with insufficient liquid assets: Consumption responses to income changes'
url: https://arxiv.org/abs/2607.15363
category: consumer-behavior
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Ignacio Belloc
- José Alberto Molina
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.15363
pages: 40
chars: 87852
fetched_at: '2026-11-08T13:03:00+00:00'
kb_version: 1
---

# Households with insufficient liquid assets: Consumption responses to income changes

Households with insufficient liquid assets:
Consumption responses to income changes ∗
Ignacio Belloc 1 and Jos´ e Alberto Molina1,2
1IEDIS and University of Zaragoza, Zaragoza, Spain
2IZA, LISER, Luxembourg
July 20, 2026
Abstract
The fraction of households living with insufficient liquid assets is important
to understand consumption responses to income changes. Using harmonized data
for 23 European countries over 2010–2023 from the Household Finance and Con-
sumption Survey, we investigate the consumption responses to income changes of
hand-to-mouth (HtM) households, grouped into non-HtM, poor HtM and wealthy
HtM. Our findings indicate significant variability across countries in the shares
of HtM households, with the majority in all countries being wealthy households
with sizeable wealth in housing and other real estates. By examining the marginal
propensity to consume (MPC) to hypothetical shocks across these households, we
find that poor HtM households exhibit the highest MPC, whereas wealthy HtM
households display a negative association with the MPC. The relationship for poor
HtM households seems to be driven by unobserved factors, whereas the relationship
with wealthy HtM is negative and significant even controlling for unobserved pref-
erence heterogeneity and households who switch their status. These consumption
responses align with life-cycle models with liquidity constraints and precautionary
savings.
Keywords: hand-to-mouth, savings, marginal propensity to consume, HFCS data
JEL classification: D12, D14, D15, E21, G51
∗Belloc: Department of Economic Analysis, University of Zaragoza; ibelloc@unizar.es. Molina: De-
partment of Economic Analysis, University of Zaragoza; jamolina@unizar.es.
Funding: This paper has benefitted from funding from the Spanish Ministry of Science, Innovation and
Universities [PID2024-156465NB-I00].
Acknowledgements: This paper was partially written while I. Belloc and J. A. Molina were visiting the
Department of Econometrics & Operations Research at Tilburg University (The Netherlands) and the
Department of Economics at Boston College (US), to which they would like to express their thanks
for the hospitality and facilities provided. We are also grateful for the helpful comments provided by
participants in several conferences.
Declaration of Competing Interest: None.
1
arXiv:2607.15363v1  [econ.GN]  16 Jul 2026

1 Introduction
Households allocate their current income between consumption and savings taking into
account the persistence of current changes and the uncertainty about their future in-
come flows. As a result, forward looking consumers adjust their consumption only in
response to unexpected and permanent income shocks, against expected and transitory
ones. From a theoretical perspective, these implications are formalized under the so-called
Life-Cycle and Permanent Income models (Modigliani and Brumberg, 1954; Friedman,
1957). However, contrary to these economic theories on consumption behavior, antici-
pated and temporary changes to income components are not smoothed and also trigger
meaningful responses in consumption (e.g. see Blundell et al., 2008, 2016; Jappelli and
Pistaferri, 2010; Crawley, 2020; Fagereng et al., 2021; Wu and Krueger, 2021; Commault,
2022; Bryukhanov and Hryshko, 2024).
Households’ wealth is composed of a wide variety of (safe and risky) assets that are
stored in either financial markets or their homes, with possibly very different degrees
of liquidity, returns and adjustment costs. One of the most prominent determinants in
explaining the issue of excessive sensitivity of consumption to current income is liquid-
ity constraints (Attanasio and Weber, 2010; Kaplan et al., 2014; Fuchs-Sch¨ undeln and
Hassan, 2016; Fisher et al., 2020). Specifically, the lack of liquid assets as a mechanism
to self-insure against fluctuations of income through financial assets prevents households
from responding to income risks and completely smooth consumption over the life-cycle.
This household heterogeneity in the consumption–income dynamics due to differences
in assets holdings, which implies that marginal propensities to consume (MPCs) out of
income changes are decreasing in liquid wealth, has stimulated research aiming to identify
which consumers are more likely to be liquidity constrained and thus overrespond to
changes in the household economic environment. However, any definition of liquidity
constraints depends on household characteristics typically not observed in data sources
(i.e., preference heterogeneity across households) that could drive the excess sensitivity of
consumption and thus contaminate results, such as impatience and risk attitudes (Aguiar
et al., 2025; Jappelli and Pistaferri, 2025). As a result, it is difficult to empirically
measure the degree of household-level liquidity constraints and different definitions have
been proposed.
For instance, Kaplan et al. (2014) (henceforth, KVW), use the Survey of Consumer
Finances (SCF) and show that the fraction of households that are unable to save and
have insufficient amounts of liquid wealth is around 31% in the US. These households
have been labeled as hand-to-mouth (HtM) households. Furthermore, they show that
most of these households are rich because they hold positive, and sometimes substantial,
illiquid wealth. They incorporate these households into the HtM pool and call them
“the wealthy HtM”. Although traditionally overlooked in the literature because of their
2

sizeable wealth position due to their large illiquid asset holdings, these consumers are
also important in explaining heterogeneous consumption responses, since they are still
affected by liquidity constraints, and behave like HtM households because they hold low
levels of liquid assets.
Other related approaches that analyze binding financial constraints include the frac-
tion of liquid assets to household income (Zeldes, 1989; Johnson and Li, 2010; Campbell
and Hercowitz, 2019; Sokolova, 2023; Jappelli and Pistaferri, 2025), the position across
household wealth and income deciles (Johnson et al., 2006; Parker et al., 2013; Chris-
telis et al., 2020; Fisher et al., 2020; Fagereng et al., 2021; Kim and Koh, 2025; Belloc
and Molina, 2026), the difficulty in obtaining loans for finance purchases (Jappelli, 1990;
Cox and Jappelli, 1993; Paiella and Pistaferri, 2017; Toussaint-Comeau, 2021; Sala and
Trivin, 2024; Castaldo and Tirelli, 2025), and the ratio between debt payments relative to
household income (Johnson and Li, 2010; Wu and Krueger, 2021; Du Caju et al., 2023). 1
Recent research that updated the KVW estimates supports these figures using the
modern Panel Study of Income Dynamics in the US (Aguiar et al., 2025; Belloc et al.,
2025), which collects detailed information on wealth and consumption at a biennial fre-
quency since 1999. Beyond the US, a limited set of estimates appears, with recent research
indicating that this fraction ranges from 23% in Belgium (Cherchye et al., 2024) to 27%
in Portugal (Duarte and Pereira, 2023), with Spain falling between these two extremes
(Cutanda and Sanchis, 2025). Although Kaplan et al. (2014) primarily focus on the
US economy, they also report the shares of HtM across Australia, Canada, the United
Kingdom and a limited number of large European countries in 2010, namely Germany,
France, Italy, and Spain, with figures indicating that less than 20% of households in Spain
and more than 30% of households in Germany live hand-to-mouth, most of them being
wealthy HtM households. Extending their analysis to 2014, Slacalek et al. (2020) and
Almgren et al. (2022) obtain distinct averages, suggesting some variance over time in this
measure within countries.
In other geographical contexts, Park (2017) and Song (2020) find shares of HtM
households above 30% in South Korea, whereas Hara et al. (2016) obtain that the share
of HtM is about 13% in Japan. 2 Although limited research attention has been devoted
to developing countries due to data availability complications and very data-demanding
requirements imposed by the empirical strategy of KVW, Cui and Feng (2017) obtain
that on average 17% of households are HtM in China, whereas Gupta et al. (2025) use a
different approach based on imputation techniques for household income and obtain that
about 17–32% are HtM among Indian households. Similarly to developed economies, the
vast majority of HtM households consists of wealthy HtM.
1Table A.3 in Sokolova (2023) presents different definitions used for binding liquidity constraints.
2Song (2020) did not use the same measure to define HtM households.
3

Within this framework, the purpose of this paper is to investigate the consumption
responses to income changes of HtM households using harmonized cross-country data in
Europe from 2010–2023. These households with insufficient liquid assets are distinguished
among poor and wealthy HtM through a survey question that asks what percentage of
a transitory, unexpected, income change would hypothetically be transmitted into either
spending or saving choices. This new evidence of heterogeneous MPCs across different
non-HtM, poor and wealthy HtM households, rather than average MPCs for all house-
holds, allows us to verify the predictions of standard consumption models. Related works
have shown that holdings of liquid wealth correlate with MPCs (Jappelli and Pistaferri,
2014, 2020; Christelis et al., 2019, 2021; Fuster et al., 2021), but low holdings of liquid
assets include both those who have low net worth as well as those who are wealthy HtM.
The representative panel of the population constitutes a key advantage over previous re-
search (Bunn et al., 2018; Drescher et al., 2020; Christelis et al., 2019, 2021; Fuster et al.,
2021; Albacete et al., 2025; Jappelli et al., 2026) and allows to identify households who
switch their HtM status by controlling for unobserved preference heterogeneity across
households.
The remainder of the paper is organized as follows. Section 2 describes the data we
use in our analysis and provides descriptive statistics of the shares of HtM households in
Europe. This includes shares by country and recent trends over time, alongside analyses
of the characteristics of HtM households. Section 3 outlines our econometric strategy,
whereas Section 4 empirically analyzes the MPC using regression analysis across these
household groups. Finally, Section 5 concludes the paper. The appendices contain addi-
tional results.
2 Data and variables
2.1 The HFCS dataset
Our empirical analysis is based on micro-data from the Household Finance and Con-
sumption Survey (henceforth, HFCS), a harmonized cross-country survey coordinated by
the European Central Bank, jointly conducted with all the national central banks of the
Eurosystem and EU countries that have not yet adopted the euro, as well as various
national statistical institutes. The HFCS is a repeated cross-sectional survey of a repre-
sentative sample of European households, in general and at country level, that has been
conducted in five waves: 2010, 2014, 2017, 2021, and 2023. 3 For certain countries, it also
includes a panel component for those five years. The main purpose of the HFCS is to
3The fieldwork period of the survey does not match across countries, both in terms of length and time
period, but those years are the most common reference period for the data in each wave, except wave
2023 which refers to 2022 year.
4

provide insights into the distribution of household net wealth and its components in the
euro area, so it is particularly suitable to carry out our analysis. 4
Our study uses data from all the years of the HFCS, the most recent data at the
time of writing this article, and we combine the HFCS into a single pooled cross-section.
The HFCS contains information on a sample of more than 410,000 households (68,627
were surveyed in 2010, 84,611 in 2014, 91,242 in 2017, 83,162 in 2021, and 84,755 in
2023) across all the euro area countries, as well as Czech Republic, Hungary and Poland,
with resulting sample sizes varying in each country. For consistency, given that wealth
components are collected at the household level in the data, as is frequent in household
surveys (Belloc and Molina, 2026), we construct all of the variables at the household
level. Hence, for individual-level demographic variables, we attribute to each household
variables associated with the household head.
2.2 Sample requirements
Turning to the sample selection of our empirical analysis, we start with a sample of house-
hold heads and mimic all of the sample restrictions made by KVW (we refer the reader
to their paper for a detailed discussion of the motivation behind those restrictions). In so
doing, we select household heads aged 22–79, both included, i.e., who make active con-
sumption and saving decisions. This removes 33,962 households. We do not select our
sample based on the working status of the household head or spouse (if any) to minimize
sample selection biases and only exclude households who derive all their income from
self-employment (i.e., about 6,988 households) to eliminate the impact of any unusual
observations, as it is likely that both assets and income from these are not well mea-
sured.5 Finally, we retain households with complete information on key variables such as
demographics, income, work status, and wealth (overall, these restrictions discard around
1.3% of observations/households). The HFCS imputes data for missing values for some
variables and uses multiple imputation techniques to minimize missing observations. This
consists of 5 different imputed values (‘implicates’) for selected variables. The restrictions
should apply consistently to all the implicates per household.
The restrictions leave us with a final sample corresponding to 349,908 household-year
observations across 5 waves (2010, 2014, 2017, 2021, and 2023) from 23 European coun-
tries, namely: Austria (AT), Belgium (BE), Cyprus (CY), Czech Republic (CZ), Germany
(DE), Estonia (EE), Spain (ES), Finland (FI), France (FR), Greece (GR), Hungary (HU),
4The HFCS is the only database that currently provides the most comprehensive information on
income, assets and liabilities for all the population in Europe, compared to alternative datasets such as
the European Union Statistics on Income and Living Conditions (EU-SILC), which focuses on income,
or the Survey of Health, Ageing and Retirement in Europe (SHARE), which targets respondents aged
50 and above.
5In our sample, there are no households with negative or missing income, conditional on the above
restrictions.
5

Croatia (HR), Italy (IT), Ireland (IE), Lithuania (LT), Luxembourg (LU), Latvia (L V),
Malta (MT), Netherlands (NL), Poland (PL), Portugal (PT), Slovenia (SI), and Slovakia
(SK).6 Of these, 12,120 observations correspond to Austria, 9,916 to Belgium, 5,915 to
Cyprus, 5,581 to Czech Republic, 18,655 to Germany, 8,986 to Estonia, 26,236 to Spain,
41,917 to Finland, 56,477 to France, 13,918 to Greece, 23,036 to Hungary, 3,722 to Croa-
tia, 5,072 to Ireland, 34,100 to Italy, 4,587 to Lithuania, 9,552 to Luxembourg, 4,555 to
Latvia, 4,477 to Malta, 9,611 to Netherlands, 8,615 to Poland, 24,754 to Portugal, 8,122
to Slovenia, and 9,984 to Slovakia.
2.3 Variable construction
The HFCS collects detailed information on household portfolios and debts. Specifically,
the household head or the person most knowledgeable about the family’s finances is
asked about ownership of many types of assets and liabilities in various categories (i.e.,
the participation rate), and about the amounts of wealth held and owed in each category
(the intensive margin). Assets include: cash, savings and deposits, stocks, bonds, cash
value in life insurance, home value, and other investments such as vehicles, business
assets, valuables, and other real estate. 7 On the other hand, liabilities are divided into
mortgage debt and non-mortgage debt, where the former consists of mortgages on the
household main residence and mortgages on other real estate properties, and the latter
comprises credit line and overdraft debt, credit card debt and other non-mortgage loans.
From the information provided in the survey, we classify assets into liquid and illiquid
wealth components. Our division of assets by liquidity largely follows the definitions of
previous research using similar data (Kaplan et al., 2014; Slacalek et al., 2020; Cherchye
et al., 2024; Aguiar et al., 2025; Cutanda and Sanchis, 2025). Specifically, we define liquid
wealth as the sum of cash, balances in sight and savings accounts (i.e., current accounts),
mutual fund holdings directly held, shares in publicly traded companies, and corporate
or government bond holdings, whereas we measure illiquid wealth as the sum of the value
of the household’s main residence and other real estate properties, plus the value of any
occupational and voluntary pension plans, the cash value of life insurance policies, and
certificates of deposit. 8 In terms of debt, we consider the balance on credit cards and the
balances on any credit lines or bank overdrafts as liquid debts in order to calculate net
liquid wealth, and debts related to real estate acquisitions (i.e., mortgages) are considered
as illiquid debt to obtain net illiquid wealth. 9
6Note that the survey has a panel component, meaning that some of those households are followed
over time.
7Valuables are defined as valuable jewelry, antiques or art.
8We do not include other nonfinancial wealth, such as antiques, artwork, and jewels, or the value of
self-employment businesses in this definition, as in Kaplan et al. (2014) or Cherchye et al. (2024).
9Financial debts, such as overdrafts or credits tied to household consumption, are more easily liqui-
dated relative to real debt products.
6

We define a household net worth as the sum of its liquid and illiquid assets net of
debts. These components of net worth are the key variables in order to properly define
and stratify households into poor HtM, wealthy HtM and non-HtM, in terms of either net
liquid and illiquid wealth or net worth according to the definitions proposed in Kaplan
et al. (2014) and Zeldes (1989), respectively (see Subsection 2.4 below for a discussion on
this issue).10
Furthermore, in order to categorize a given household as either poor or wealthy HtM,
we also need information on household income. Our measure of income in the survey is
defined as the sum of all income earned by household members over the last 12 months
preceding the survey or the calendar year prior to the survey year. It includes both labor
and non-labor income sources such as gross income from wages, salaries, self-employment,
and pension, unemployment benefits, and regular transfers such as child support alimony
and other public transfers, consistent with Kaplan et al. (2014), Cherchye et al. (2024) and
Aguiar et al. (2025). We exclude interest, dividends, and other capital income because
they are realized more infrequently. All these monetary amounts, i.e. household income
and wealth, are deflated and expressed in 2021 constant euros using the Harmonised
Index of Consumer Prices (HICP) from the Eurostat data (the annual average index, all
items HICP).11
Finally, the HFCS allows us to define a range of other household and individual demo-
graphics that may be important in explaining HtM and have been shown to be important
determinants of consumption behavior. These variables include the age of the head of the
household, a dummy variable indicating whether the household head is employed, vari-
ables denoting the maximum educational level achieved by the household head, primary
housing tenure status, the marital status through a dummy variable denoting whether the
household head is married, the number of individuals in the family unit, and the number
of children under the age of 16. Education is categorized into three groups based on the
maximum level of educational attainment achieved by the household head on the basis
of the 1997 International Standard Classification of Education (ISCED-97) scale: pri-
mary or no education comprises heads who do not have secondary education, secondary
education includes those who completed secondary education but did not graduate, and
tertiary education refers to those with tertiary education. Finally, we control for the
primary housing tenure status and define three dummy variables indicating households
who own their primary residence without mortgage or rental payments (i.e., outright
owners), households who own part of the residence and have a mortgage (homeowners
10In order to decrease non-response rates, the HFCS uses stochastic multiple imputation techniques
for all missing observations in households’ income, consumption and wealth. We estimate all our results
using these imputed values together, adjusting coefficients and standard errors accordingly throughout
the paper (see Trivin, 2022; Du Caju et al., 2023; Sala and Trivin, 2024).
11Available at https://ec.europa.eu/eurostat/databrowser/view/prc hicp aind/default/table?lang=en,
accessed January 2026.
7

with a mortgage), and households who are renters.
2.4 Identifying HtM households in Europe
We identify HtM households following the criteria of Kaplan et al. (2014) and split house-
holds between HtM and non-HtM based on their holdings of net liquid and illiquid wealth.
Specifically, households whose balances of liquid wealth are positive but equal to or less
than half their earnings per pay period are classified as HtM. 12 In addition, we also in-
corporate the household’s credit limit, and count as HtM any household whose balances
of liquid wealth are negative and for whom the sum of their liquid wealth and credit limit
(assumed at 0.185 times of annual earnings (Kaplan et al., 2014; Aguiar et al., 2025))
is less than half their earnings per pay period. Next, to distinguish between poor and
wealthy HtM among households who do not hold liquid assets (i.e., conditional on being
HtM), we rely on their holdings of net illiquid wealth, if any. Specifically, households who
holdanyamount of illiquid wealth are labeled as wealthy HtM, whereas those who hold
negative or zero amounts of illiquid wealth are labeled as poor HtM.
We present summary statistics on HtM households across countries and over time,
given the extended time span covered by the dataset. Figure 1 shows the fraction of
HtM households in our sample of European countries, distinguishing between wealthy,
poor, and total HtM households, using the pooled cross-sectional HFCS dataset over the
2010–2023 period. Across our entire sample, we label 27.3% of households as HtM. The
fraction of wealthy HtM is, on average, larger than the share of poor HtM, with 21.1%
denoted as wealthy HtM and the remaining 6.2% as poor HtM.
Across all countries, HtM households constitute a quantitatively important share of
the population, with HtM shares ranging from roughly 14% in Czechia to nearly 71%
of households in Greece. Apart from these countries, other countries such as Estonia,
Spain and Italy have low levels under 25%, and others have values higher than 40%,
such as Cyprus and Croatia. Moreover, in every country the majority (i.e., well over
65%) of HtM households are wealthy rather than poor, indicating that these households
hold substantial wealth in illiquid assets, a common finding in the existing literature.
In particular, the share of wealthy HtM households among all HtM households varies
between 64% in Ireland and Italy and 90% in Greece, Luxembourg, and Malta.
As expected, the variation across countries is significant. Among Western European
countries, the fraction of HtM households ranges from 25.9% in Germany to 36.5% in
Ireland. In Eastern European countries, HtM shares lie between 13.9% in Czech Republic
and 43.3% in Cyprus. Southern European countries display the greatest cross-sectional
variance, largely driven by Greece and Cyprus, with HtM shares oscillating between
22.9% in Spain and Italy and 70.6% in Greece.
12As in KVW, we set the pay frequency to two weeks.
8

Figure 1: Shares of total, wealthy, and poor HtM households, HFCS 2010–2023
Notes:The figure shows percentages across HtM households for the different countries. Percentages
overtotalhouseholds. Data come from the Household Finance and Consumption Survey, 2010–2023.
Figures refer to sample averages, calculated using population weights and bootstrapped replicated
weights.
Alternatively, Table 1 documents the evolution of the share of HtM households over
time for all countries in the sample. 13 Overall, the share of HtM households experiences
a decline in our sample over 2010–2023, from 28.5% in 2010 to 27.3% in 2023, especially
concentrated during the last two waves of the survey and due to the lower presence of
wealthy HtM households. In contrast, the share of poor HtM households is relatively
stable over time. Most countries exhibit a decline in the prevalence of HtM households
over the sample period, including Austria, Belgium, Cyprus, Czech Republic, Germany,
Estonia, Spain, Finland, Hungary, Croatia, Italy, Lithuania, Luxembourg, Latvia, Malta,
the Netherlands, Slovenia, and Slovakia. By contrast, other countries, such as France,
Greece, and Portugal, display an increase in these shares over time. Finally, the fraction
of HtM households has stayed stable in Poland throughout the observation period.
2.5 Descriptive statistics
Table 2 presents summary statistics for five household groups: the full sample after ap-
plying the selection criteria, non-HtM households, HtM households, wealthy HtM house-
holds, and poor HtM households. We first compare HtM households with their non-HtM
13The patterns in some subsets of countries, such as Belgium, Spain, and Portugal, match with recent
research at the country level using part of the HFCS (Kaplan et al., 2014; Slacalek et al., 2020; Duarte
and Pereira, 2023; Cherchye et al., 2024; Cutanda and Sanchis, 2025).
9

Table 1: Trends in shares of HtM households
2010 2014 2017 2021 2023 2010–2023
Wealthy Poor Total Wealthy Poor Total Wealthy Poor Total Wealthy Poor Total Wealthy Poor Total Wealthy Poor Total
Austria 29.7 4.9 34.5 26.1 5.2 31.3 21.9 3.9 25.8 22.4 4 26.4 21.3 4.7 26 24.2 4.5 28.7
Belgium 22.2 4 26.2 21.5 6.4 27.9 19.7 5.3 25 22.7 5.2 27.9 23 0.4 23.5 21.8 4.2 26
Cyprus 37.7 5.1 42.8 33.3 10.6 43.9 37.8 11.5 49.4 34.3 11.6 45.9 25.8 10.1 35.9 33.5 9.8 43.3
Czech Republic — — — — — — — — — 9.9 4.3 14.2 9.7 3.9 13.6 9.8 4.1 13.9
Germany 22.7 7.3 30 20.9 8 28.9 19.3 8.1 27.5 15.3 6.1 21.4 14.8 7.2 22 18.6 7.4 25.9
Estonia — — — 21.1 7.3 28.4 18 6.3 24.3 16.8 3.5 20.2 17 2.4 19.4 18.2 4.8 23
Spain 18 5.9 23.8 17 7.6 24.6 14.7 7.8 22.5 15 9.5 24.5 13.4 8 21.4 15.6 7.8 23.3
Finland 27.5 8.9 36.3 21 6.8 27.8 21.6 7.2 28.8 21.9 7.3 29.2 23 8.3 31.3 22.5 7.6 30.1
France 23.4 3.1 26.5 25.7 3.1 28.8 25.8 3.9 29.7 24.4 3.3 27.7 23.5 3.2 26.7 24.5 3.3 27.9
Greece 26.9 9.5 36.5 68.1 10.3 78.4 76.8 5.2 82 74.4 1.3 75.8 77.6 0.7 78.3 65.3 5.3 70.6
Hungary — — — 29.7 5.3 35 33 6.5 39.5 20.8 3.2 24 24.1 4.4 28.6 26.9 4.9 31.8
Croatia — — — — — — 44.4 5.9 50.3 35.1 7.7 42.8 26.4 3.8 30.2 35.4 5.8 41.2
Ireland — — — 23.7 12.9 36.5 — — — — — — — — — 23.7 12.9 36.5
Italy 17.8 8.5 26.2 16.3 10.5 26.8 15 9.6 24.6 13.1 6.7 19.8 11.1 6.3 17.4 14.6 8.3 22.9
Lithuania — — — — — — 26.7 3 29.7 26.5 1.1 27.6 21.9 2.7 24.6 24.9 2.3 27.2
Luxembourg 19 5.7 24.7 23.7 5.5 29.3 23.7 4.4 28.1 25.3 2.7 28 18.1 2.4 20.5 22.1 4 26
Latvia — — — 39.8 11.3 51.1 36.1 9.7 45.8 20.3 3.5 23.8 18.7 4.1 22.8 28.7 7.2 35.9
Malta 34.9 3 37.9 33.8 2 35.8 36.8 1.4 38.3 22.3 3.8 26.1 14.8 2 16.7 27.2 2.4 29.6
Netherlands 34.7 4.8 39.5 33.2 5 38.2 17.5 5.5 22.9 22.4 4.8 27.1 18.4 3.8 22.2 25.1 4.8 29.9
Poland — — — 20.7 5.6 26.4 22.2 3.8 26 — — — — — — 21.4 4.7 26.2
Portugal 18.4 5.7 24.1 19.6 8.2 27.8 19 8 27 18.7 7.1 25.7 17.5 7.8 25.3 18.6 7.3 26
Slovenia 35.4 6.5 41.8 35 8.1 43.1 26.6 8.4 35 29.9 7.9 37.8 24.6 5.2 29.8 30.3 7.2 37.5
Slovakia 22.7 2.3 25 25.1 4.9 30 26.7 3.4 30.1 20.7 2.3 23.1 20.7 2.7 23.4 23.2 3.1 26.3
Pooled 22.4 6.1 28.5 23 7 30.1 21.8 6.6 28.5 19.7 5.6 25.3 18.7 5.4 24.1 21.1 6.2 27.3
Notes: Data come from the Household Finance and Consumption Survey, 2010–2023. Figures refer to sample averages, calculated using population
weights and bootstrapped replicated weights.
10

counterparts. On average, HtM households are approximately three years younger and
display lower household income and labor earnings, consistent with Aguiar et al. (2025).
They are also characterized by negative net liquid wealth and substantially lower hold-
ings of illiquid assets, resulting in lower overall net worth. In demographic terms, HtM
households tend to be slightly larger, display a more balanced gender distribution among
household heads and have lower levels of education, whereas they are less likely to be em-
ployed or married. Housing tenure also differs sharply across groups; while around 42%
of HtM households are renters, approximately 44% of non-HtM households are outright
owners.
Further insights emerge when comparing wealthy and poor HtM households. Specifi-
cally, heads of wealthy HtM households are, on average, about three years older and earn
nearly twice as much in terms of both household income and labor earnings. Although
wealthy HtM households hold substantial illiquid assets (aboute156,311 in net illiquid
wealth), their net liquid wealth remains negative and is even lower than that of poor HtM
households. Notably, wealthy HtM households exhibit the lowest average in net liquid
wealth among all groups, highlighting the liquidity constraints that also characterize this
group despite their sizable illiquid asset position. Alongside other demographics, wealthy
HtM households show the highest employment rates and larger family sizes, whereas
poor HtM households have the lowest levels of educational attainment. As expected,
poor HtM households tend to be renters (about 78.8% state they are renters), whereas
about 65% of wealthy HtM households are home-owners (40.4% are outright owners and
24.4% mortgagors).
In Table 3 we look at additional characteristics among those groups of the population
and analyze their level of indebtedness, the debt-to-income ratios, and the debt-payments-
to-income ratio (Johnson and Li, 2010; Albuquerque, 2019; Toussaint-Comeau, 2021;
Du Caju et al., 2023; Cherchye et al., 2024; Sala and Trivin, 2024; Bartscher et al.,
2025; Belloc et al., 2025), along with the presence of binding credit constraints. The
debt-payments-to-income is the ratio between the household’s total debt payments and
disposable income. We also display the average ratio of total homeowners’ mortgage
balances and household income (i.e., the housing debt-to-income ratio). To control for
binding financial constraints due to credit constraints, we consider whether the household
experienced credit refusal within the last years or did not apply for credit within the last
years as it expected to be turned down. (Note that we exclude 7,570 households who have
missing values on debt payments or report zero amounts for family income to properly
define the debt-payments-to-income and the debt-to-income ratios). 14
The main difference across household groups arises from the composition and burden
of debt, particularly in liquid liabilities unrelated to real estate. HtM households hold
14The survey question about the presence of credit constraints is not available in the HFCS for Italy
in 2010 and 2014, for instance.
11

substantially larger amounts of liquid debt than non-HtM households and the population
as a whole. In addition, HtM households also display higher debt payments related to
income, as expected, and show a higher probability, more than double, of being credit
constrained compared to their non-HtM counterparts. Within the HtM group, important
heterogeneity also emerges. Wealthy HtM households hold the largest amounts of both
mortgages and liquid debts. However, despite their higher indebtedness, they face a
considerably lower debt burden relative to income and a substantially lower probability
of being credit constrained than poor HtM households.
Finally, Table 4 reports the transition probabilities across the HtM categories, allowing
us to assess the persistence of household types by comparing households observed over
two and three consecutive waves. Looking at the diagonal elements, we find the highest
persistence among non-HtM households, as indicated by the first element of the main
diagonal. In particular, households classified as non-HtM in a given year (Non-HtM t,
column) have an 86% probability of remaining in that status in the following period
and an 87% probability two periods later. In contrast, households classified as wealthy
or poor HtM in a given year exhibit only a 38.4–39.9% probability of remaining in the
same category in the following observation period. After two periods, persistence in HtM
status declines. Overall, these findings regarding the persistence of household types are
consistent with Aguiar et al. (2025). 15
15The period across HFCS interviews varies between 2-4 years. If we study average transition rates
between HtM status across HFCS 2021-2023 waves, we find that the persistence across non-HtM, wealthy
HtM and poor HtM is 88.6%, 37.2% and 41.2%, respectively. That is, the persistence among poor HtM
households is even larger.
12

Table 2: Summary statistics among household groups
All Non-HtM HtM Wealthy HtM Poor HtM
Income and wealth
Income 45,368.910 48,026.27 38,287.470 42,506.830 23,850.310
Labor income (age 22–65) 37,603.010 40,616.940 30,263.190 34,451.240 16,524.850
Net liquid wealth 17,855.040 28,948.660 -11,707.600 -13,304.960 -6,242.147
Net illiquid wealth 206,038.700 238,325 120,001.300 156,310.600 -4,220.173
Net worth 223,893.700 267,273.600 108,293.700 143,005.700 -10,462.320
Demographics
Male 0.559 0.573 0.523 0.525 0.513
Age 51.949 52.807 49.664 50.301 47.483
Primary education 0.119 0.107 0.153 0.140 0.199
Secondary education 0.582 0.563 0.631 0.619 0.671
Tertiary education 0.299 0.330 0.216 0.241 0.130
Employed 0.601 0.604 0.593 0.623 0.490
Married 0.526 0.540 0.490 0.525 0.369
Household size 2.375 2.346 2.453 2.507 2.267
Number of children 0.412 0.381 0.497 0.494 0.505
Outright owner 0.403 0.436 0.313 0.404 0.002
Mortgagor 0.216 0.221 0.203 0.244 0.063
Renter 0.329 0.295 0.422 0.315 0.788
Notes: Data come from the Household Finance and Consumption Survey, 2010–2023. Figures refer
to sample averages, calculated using population weights and bootstrapped replicated weights. All
monetary figures are expressed in 2021 euros.
Table 3: Indebtedness among household groups
All Non-HtM HtM Wealthy HtM Poor HtM
Mortgage debt 32,100.850 33,237.780 29,080.680 31,972.320 18,472.990
Liquid debt 4,665.021 1,396.857 13,346.990 15,048.270 7,106.283
Total debt-to-income ratio 1.574 0.994 3.115 2.451 5.526
Housing debt-to-income ratio 1.385 0.962 2.509 1.865 4.853
Debt-payments-to-income 0.010 0.007 0.019 0.016 0.030
Credit constraints 0.076 0.057 0.128 0.108 0.202
Notes: Data come from the Household Finance and Consumption Survey, 2010–2023. Figures
refer to sample averages, calculated using population weights and bootstrapped replicated
weights. Debt figures, in levels, are expressed in 2021 euros.
Table 4: Transition rates for HtM households
Non-HtMt Wealthy HtMt Poor HtMt
Panel A: 54,179 households
Non-HtMt+1 0.861 0.582 0.433
Wealthy HtMt+1 0.120 0.384 0.169
Poor HtMt+1 0.018 0.034 0.399
Panel B: 18,832 households
Non-HtMt+2 0.868 0.648 0.477
Wealthy HtMt+2 0.114 0.315 0.179
Poor HtMt+2 0.019 0.037 0.344
Notes: Data come from the Household Finance and Consumption Survey,
2010–2023.
13

2.6 Robustness checks about the definition of HtM
We run many robustness checks on our results for HtM households in Europe. For
comparison, we also stratify HtM households in net worth based on Zeldes (1989), and
consider that a household is HtM in net worth when their net worth is positive but equal
to or less than half their earnings per pay period, or negative with absolute value greater
than half their earnings per paid period plus the credit limit (Kaplan et al., 2014; Aguiar
et al., 2025). This highlights the importance of distinguishing between liquid and illiquid
asset positions. We also focus on a sample of 250,172 household heads aged 25-64 and
use labor earnings as the reference measure for income (Aguiar et al., 2025; Cutanda and
Sanchis, 2025). The percentages, shown in Table A.1 in Appendix A, are significantly
lower than those using the definition of KVW. Furthermore, we also change the payment
frequency of income payments from two weeks to one month, which increases the fraction
of HtM households. Symmetrically, shortening the paid period and setting it to one week
decreases the fraction of HtM households. Finally, our main definition of HtM omits other
real assets such as the value of self-employment business (Slacalek et al., 2020) or other
assets such as vehicles, jewelry, antiques or artwork, meaning that our baseline shares
for wealthy HtM households outlined above may provide a lower bound. As a result,
we explore an alternative specification of illiquid asset categories and incorporate those
into the definition of net illiquid wealth, together with 6,869 households whose income
is entirely from self-employment (Kaplan et al., 2014). This increases the fraction of
wealthy HtM households, while the overall percentage of HtM households remains stable,
as in KVW. All these results are included in Table A.2.
3 Econometric strategy
Since the 2017 survey wave, the HFCS collects information on the MPC per household.
Specifically, the survey asks the following question: “Imagine that you unexpectedly re-
ceive money from a lottery, equal to the amount of income your household receives in a
month. What percentage would you spend over the next 12 months on goods and services,
as opposed to any amount you would save for later or use to repay loans?”, with the
potential answers ranging from 0 (not spend anything) to 100 percent (spend the full
windfall over the next 12 months), both included. This question does not target a spe-
cific category of consumption and refers to both durable and non-durable consumption
spending. An additional question is available to measure the marginal propensity to save
(MPS), analogous to the previous one (i.e., the sum of these two hypothetical choices
must add up to 100 percent). 16
16This question is nearly identical to a hypothetical question for spending responses available in the
Italian Survey of Household Income and Wealth (SHIW) (Jappelli and Pistaferri, 2014, 2020) and does
not refer to a fixed sum of money across households (Crossley et al., 2021; Albuquerque and Green,
14

This survey question directly elicits the MPC and captures the percentage by which
households would raise their consumption upon receiving an unexpected, transitory and
positive, income change within a year. A number of recent studies have used survey data
and responses to scenarios involving changes to the households’ economic environment to
elicit the MPC (see, e.g., Jappelli and Pistaferri, 2014, 2020; Bunn et al., 2018; Christelis
et al., 2019, 2021; Fuster et al., 2021; Jappelli et al., 2026) or labor supply responses
(Georgarakos et al., 2025).
In contrast to other approaches taken in the literature based on quasi-experimental
events that mimic unexpected changes in household budgets (due, for example, to lottery
wins, see Fagereng et al., 2021; Golosov et al., 2024) and semistructural methods based
on a statistical decomposition of income processes and consumption (Blundell et al.,
2008; Ghosh and Theloudis, 2025), this method uses a “reported preference” approach
(Fuster et al., 2021) and measures directly how households would modify their expenses
in response to a scenario involving an unexpected windfall gain equal to their average
monthly income.17
We go beyond the previous descriptive evidence and further analyze this unique sur-
vey question available in the HFCS using formal regression analysis considering a set of
household characteristics.18 Specifically, we estimate the following baseline linear regres-
sion model for the MPC by pooled Ordinary Least Squares (OLS):
M P Cijt =α 0 +β 1P oor HT Mijt +β 2W ealthy HT Mijt +X ′ ijtγ+µ j +τ t +ε ijt, (1)
where subscriptirefers to the householdi, subscriptjdenotes the country of residence
j, and subscripttrepresents the survey yeart. The dependent variable,M P C ijt, is the
MPC reported by householdiresiding in countryjin periodt, whereasP oor HT M ijt
andW ealthy HT Mijt, our two key explanatory variables in Equation (1), are two dummy
variables each taking value 1 for households who are either poor or wealthy HtM at time
t, respectively, and value 0 otherwise. Theβ k coefficients, fork= 1,2, are the main
2023). A difference with the SHIW is that the question in the HFCS refers to an explicit time frame for
the spending response. Similar data also exist for the Netherlands (Christelis et al., 2019).
17Crawley and Theloudis (2024) and Trivin (2024) survey the advantages and underlying assumptions
of this method to infer MPCs, whereas Colarieti et al. (2024) and Ueda (2025) compare self-reported
and actual spending behavior.
18The mean value of the MPC in our sample equals to 43.5 percent, which is close to the average
percentages reported in Drescher et al. (2020) and Albacete et al. (2025) using the third wave of the
HFCS. Across countries, MPCs range from 29.2 in Portugal to 55 in Croatia and Lithuania. The
estimate for Italy is also close to those reported in previous studies (Jappelli and Pistaferri, 2014, 2020).
These average reported MPCs are larger than current estimates based on survey data on observed
consumption and income changes. As is frequently the case with subjective perceptions and expectations
data (Manski, 2018; Bruine de Bruin et al., 2022; Ko¸ sar and O’Dea, 2023; Arellano et al., 2024), our
variable concerning the MPC is clustered around specific rounded values like 0 percent (saving all), 50
percent (saving/spending half), and 100 percent (spending all), similar to Albacete et al. (2025). In
addition, the strong buching responses at 0/50/100 tend to be some persistent one and two periods later.
These features are displayed in Tables B.1-B.2 and Figures B.1-B.2 in Appendix B.
15

parameters of interest from Eq. (1) and measure the percentage point differences in the
MPC across poor and wealthy HtM households, relative to their non-HtM household
counterparts.
On the other hand,X ijt is a vector of household-level control characteristics, which
includes households’ heterogeneous demographic characteristics such as the head of house-
hold’s age, indicators for household heads who are males, their education levels and em-
ployment status, the family structure (e.g., marital status, household size and number of
children), and the specific housing tenure status through two dummy variables denoting
mortgagors and renters, with outright owners and others considered as the baseline cate-
gory for housing tenure status. 19 Finally, the termsτ t andµ j indicate wave and country
fixed effects, andε ijt is an error term. 20
4 Results
Table 5 presents the results of estimating Equation (1). In Column (1) we find that HtM
households do not display higher MPCs, according to the definition in KVW. In contrast,
HtM households in net worth (Zeldes, 1989) show higher MPCs in Column (2), relative
to their non-HtM counterparts. Quantitatively, a HtM household in net worth displays
2.441 more percentage points in the MPC than non-HtM households.
Turning to our main estimates from Eq. (1) shown in Column (3), we find a positive
association between the MPC and poor HtM status, and a negative relationship with
wealthy HtM households. In particular, we find that poor HtM households display the
highest MPC, and being a poor HtM household correlates to an increase by about 6.029
percentage points in the MPC, relative to non-HtM households. That is, these types of
households, who ultimately hold litle wealth, consume the majority of the extra liquidity
they receive and display the highest MPC, in line with theoretical predictions of hetero-
geneous MPCs when people face binding liquidity constraints that prevent them from
smoothing consumption fluctuations in response to income changes. On the other hand,
wealthy HtM households have MPCs that are 1.789 percentage points lower than those
of non-HtM households, a magnitude which is statistically significant at the 1% level.
This result implies that the shock is not large enough to relax the financial constraint,
which may be a reasonable assumption given the survey question we exploit, and that
these households would use part of the income shock to increase their liquid savings due
19We control for age using 5-year intervals to capture potential non-linearities in consumption (Kaplan
et al., 2014). Our results are robust to the inclusion of log family income and a set of country-year fixed
effects.
20An alternative estimator would be a Tobit model (Jappelli and Pistaferri, 2014; Bunn et al., 2018;
Christelis et al., 2021, 2025; Albuquerque and Green, 2023; Albacete et al., 2025), as MPCs are con-
strained to vary from 0 to 100. However, this estimator is not compatible with bootstrapped replicates
used in the HFCS.
16

to a precautionary motive, pay off their debts or adjust their balance sheets, rather than
spending. Unfortunately, the survey question does not allow us to distinguish among
these channels and households who repay debt, similar to Jappelli and Pistaferri (2014,
2020) and Jappelli et al. (2026).
As a result, despite their limited holdings of liquid assets, wealthy HtM households
display lower MPCs than the non-HtM. This underscores the composition of household
resources for spending responses, as spending is more responsive to liquid assets rather
than total wealth (Kaplan et al., 2014), and adds a new result in the related literature that
finds a negative correlation between MPC and liquid wealth or cash-on-hand (Jappelli
and Pistaferri, 2014, 2020; Bunn et al., 2018; Christelis et al., 2019, 2021; Fuster et al.,
2021; Albacete et al., 2025). 21 A potential explanation for the above result arises from
the significant holdings of illiquid assets across the wealthy HtM that cannot be used
immediately to smooth consumption in the event of shocks, meaning that they may
differ in their spending purposes from those who do not hold neither liquid nor illiquid
assets (i.e., poor HtM households).
Overall, both subsets of households fail to smooth consumption in response to tran-
sitory increases in income. This result is contrary to the theory that suggests that the
MPC out of a transitory and small income shock will either be relatively small or very
close to zero (i.e., a transitory change in disposable income should not trigger meaning-
ful responses in current consumption, whereas the response should be smaller for small
shocks in comparison to large ones), and aligns with life-cycle models that incorporate liq-
uidity constraints and precautionary saving purposes to explain the lack of consumption
smoothing of agents and high MPCs.
Turning to the rest of our estimates in Table 5, we find that other observable household
characteristics are associated with MPC heterogeneity. Specifically, we find that older
individuals tend to have higher MPCs relative to younger groups, meaning that the MPC
increases with age, particularly for the oldest age group. That is, the income windfall is
not transmitted to savings among the elderly. Specifically, those in the oldest age group
(75 and over) exhibit the largest MPCs compared to the youngest group (less than 25
years old, the reference category). These older households have relatively fewer periods
than young over to spread changes in lifetime income and smooth their consumption so
this is a result consistent with the predictions of standard life-cycle models with finite
planning horizons and no bequest motives for saving (Modigliani and Brumberg, 1954). 22
We also find that the education level attainment correlates with the MPC, and sec-
ondary as well as university educated households appear to display a significantly larger
MPC than those with primary or no education, in contrast to Blundell et al. (2008).
21Using the 2017 HFCS, Drescher et al. (2020) did not find any relationship between net wealth and
MPCs. However, they did not analyze the MPC across poor, wealthy, and non-HtM households.
22These older households may leave inheritances at the end, but these are involuntary and unplanned.
17

Specifically, secondary educated household heads have MPCs 1.98-2.14 percentage points
higher than primary educated household heads, whereas university educated households
heads display 1.86 more percentage points in the MPC than primary educated house-
hold heads.23 On the other hand, we find lower MPCs for employed household heads and
mortgagors as well as renters. The empirical findings for employed, mortgagor, and renter
households are consistent with precautionary saving models and frameworks incorporat-
ing liquidity constraints. Unemployed individuals, who face greater income volatility,
tend to accumulate larger precationary buffers relative to their employed counterparts.
On the other hand, mortgagor households face tighter liquidity constraints arising from
debt service obligations, whereas renters are on average younger households. As a re-
sult, the transitory income windfall is more likely to be saved or applied to debt service
rather than consumed among these. Quantitatively, households headed by an employed
individual exhibit MPCs approximately 4.4–4.7 percentage points lower than those of
non-working households, whereas mortgagors and renters report MPCs that are lower by
approximately 3.06 and 1.81 percentage points, respectively, relative to outright owners
and households in other primary tenure categories. Most of these relationships have been
reported in previous works (Jappelli and Pistaferri, 2014, 2020; Bunn et al., 2018; Chris-
telis et al., 2019, 2021; Albuquerque and Green, 2023; Sokolova, 2023; Albacete et al.,
2025).
23We alternatively distinguish households with and without college education, similar to Blundell et al.
(2008), and do not find that tertiary educated household heads display lower MPCs, in comparison to
less educated households.
18

Table 5: Pooled OLS regression results
(1) (2) (3)
HtM -0.050 — —
(0.595)
HtM in net worth — 2.441 ∗∗ —
(1.123)
Poor HtM — — 6.029 ∗∗∗
(1.412)
Wealthy HtM — — -1.789 ∗∗∗
(0.574)
Male -0.042 -0.050 -0.105
(0.469) (0.469) (0.466)
25 – 29 years 0.468 0.407 0.295
(3.279) (3.228) (3.212)
30 – 34 years 1.692 1.640 1.472
(3.163) (3.119) (3.095)
35 – 39 years 3.553 3.566 3.471
(3.106) (3.077) (3.057)
40 – 44 years 4.490 4.472 4.253
(3.051) (3.017) (2.998)
45 – 49 years 5.761 ∗ 5.752∗ 5.575∗
(3.069) (3.015) (2.976)
50 – 54 years 5.539 ∗ 5.558∗ 5.315∗
(3.078) (3.044) (3.014)
55 – 59 years 6.162 ∗∗ 6.190∗∗ 5.939∗∗
(2.993) (2.956) (2.932)
60 – 64 years 5.292 ∗ 5.384∗ 5.196∗
(2.990) (2.961) (2.932)
65 – 69 years 5.845 ∗ 5.994∗∗ 5.817∗∗
(3.009) (2.971) (2.934)
70 – 74 years 5.049 ∗ 5.249∗ 5.100∗
(3.054) (3.007) (2.978)
75 – 79 years 7.709 ∗∗ 7.932∗∗∗ 7.765∗∗∗
(3.013) (2.967) (2.940)
Secondary education 1.978 ∗ 2.099∗∗ 2.137∗∗
(1.072) (1.026) (0.978)
Tertiary education 1.645 1.881 ∗ 1.860∗∗
(1.016) (0.979) (0.944)
Employed -4.736 ∗∗∗ -4.611∗∗∗ -4.392∗∗∗
(0.717) (0.684) (0.653)
Married 0.789 0.825 0.837
(0.529) (0.525) (0.524)
Household size 0.104 0.106 0.125
(0.298) (0.294) (0.284)
Number of children 0.120 0.074 0.050
(0.426) (0.425) (0.417)
Mortgagor -3.041 ∗∗∗ -3.067∗∗∗ -3.055∗∗∗
(0.598) (0.587) (0.584)
Renter -1.029 ∗ -1.456∗∗ -1.809∗∗∗
(0.612) (0.659) (0.657)
Constant 31.148 ∗∗∗ 30.869∗∗∗ 31.352∗∗∗
(3.230) (3.188) (3.167)
Country fixed effects Yes Yes Yes
Year fixed effects Yes Yes Yes
Observations 157,430 157,430 157,430
Notes: OLS estimates. Standard errors in paren-
theses. Data come from the Household Finance
and Consumption Survey, 2017–2023. Sample is
restricted to households whose head is between 22
and 79 years old, have no negative family income
and whose income is not entirely derived from self-
employment. Estimates are weighted using sampling
and bootstrapped replicated weights. ∗ p <0.10, ∗∗
p <0.05, ∗∗∗ p <0.01. 19

Given that the HFCS has a panel component over the period 2017–2023, we also em-
ploy a panel data regression model and rerun Equation (1) further incorporating house-
hold fixed effects (e.g. aα i term in Eq. (1)) that initially remain in the error term and
account for household unobserved heterogeneity that is fixed over time, such as personal-
ity traits, risk aversion or discount rates. These features might affect both HtM behavior
and consumption decisions simultaneously (Jappelli and Pistaferri, 2020; Aguiar et al.,
2025), thus introducing a potential bias in the OLS estimates ofβ 1 andβ 2 in Eq. (1),
which exploits variation both between and within households. (Hausman test results
support the validity of the fixed effects specification).
This approach is similar to that taken by Jappelli and Pistaferri (2020), who also have
panel data on a sample of Italian households over two years in 2010 and 2016. 24
To properly include household fixed effects, we need households to be observed at least
twice to identify coefficients. To do so, we use the panel information of the HFCS over
2017–2023 and focus on a sample of household heads observed for at least two periods,
which restricts our analysis to an unbalanced panel sample of 63,602 household-year
observations from 26,814 households. 25
Table 6 shows the results of estimating Equation (1) after incorporating household
fixed effects.26 These estimates are comparable to those in Jappelli and Pistaferri (2020).
We find that controlling for household unobserved heterogeneity significantly changes
the main results, and previous pooled OLS estimates exagerate the negative relation-
ship between wealthy HtM and MPC as well as the positive relationship with poor
HtM. Specifically, the coefficient estimated for poor HtM households is no longer sta-
tistically significant after controlling for unobserved heterogeneity, whereas the negative
estimate for wealthy HtM household remains statistically significant (at the 1% level),
albeit slightly smaller in absolute terms. 27 The comparison between pooled OLS and
household fixed effects results for poor and wealthy HtM households fits the patterns dis-
played by Jappelli and Pistaferri (2020), who also find that OLS estimates exaggerates
the negative relationship between the cash-on-hand distribution and MPC (Jappelli and
Pistaferri, 2020), meaning that unobserved factors also account for the observed relation-
ship in the cross-section. The remaining statistically significant variables are the dummy
24As argued in Jappelli and Pistaferri (2020), in contrast to Bunn et al. (2018), Christelis et al. (2019),
Fuster et al. (2021) and Jappelli et al. (2026), we have data for the same households at (at least) two
different points in time, rather than on a different set of MPC questions asked at the same point. For
further details on this matter, we refer to footnote 9 in their paper.
25In principle, the analysis requires at least two observations per household, either consecutive or non-
consecutive. However, we focus on households observed for at least twoconsecutivewaves due to the
HFCS design of the longitudinal household identifier.
26In principle, household time-invariant variables such as gender or educational level attainment should
be excluded. However, the identity of the household head could change between interviews in the HFCS.
Household fixed effects subsume country fixed effects.
27Poor HtM households are relatively persistent over time, which may reflect the insignificant esti-
mated effect within this group. Nevertheless, sufficient within-household variation exists to identify the
coefficient.
20

variables for employed household heads, mortgagors and renters, which indicates that
households headed by an employed individual exhibit MPCs approximately 2.5 percent-
age points lower than those headed by a non-employed individual, while mortgagor and
renter households report MPCs approximately 1.8 and 3.2 percentage points lower than
those of outright owners and households with other housing tenure statuses, respectively.
21

Table 6: Fixed effects regression results
(1) (2) (3)
HtM -1.326 ∗∗∗ — —
(0.502)
HtM in net worth — 0.655 —
(1.137)
Poor HtM — — 1.049
(1.361)
Wealthy HtM — — -1.671 ∗∗∗
(0.524)
Male 1.544 ∗ 1.521∗ 1.544∗
(0.819) (0.819) (0.819)
25 – 29 years 1.168 1.192 1.206
(2.803) (2.812) (2.801)
30 – 34 years 3.699 3.746 3.736
(2.954) (2.963) (2.951)
35 – 39 years 2.063 2.125 2.130
(3.035) (3.043) (3.032)
40 – 44 years 1.101 1.189 1.173
(3.089) (3.096) (3.086)
45 – 49 years 1.191 1.238 1.242
(3.120) (3.128) (3.117)
50 – 54 years 0.103 0.136 0.130
(3.152) (3.160) (3.148)
55 – 59 years 0.522 0.536 0.556
(3.206) (3.212) (3.201)
60 – 64 years 0.188 0.214 0.231
(3.281) (3.288) (3.276)
65 – 69 years 1.185 1.234 1.235
(3.371) (3.378) (3.366)
70 – 74 years 0.862 0.914 0.915
(3.491) (3.500) (3.486)
75 – 79 years 1.610 1.657 1.654
(3.642) (3.650) (3.637)
Secondary education -0.531 -0.512 -0.530
(1.313) (1.313) (1.311)
Tertiary education -1.111 -1.092 -1.113
(1.607) (1.607) (1.606)
Employed -2.525 ∗∗∗ -2.506∗∗∗ -2.497∗∗∗
(0.668) (0.667) (0.667)
Married -0.434 -0.433 -0.420
(0.937) (0.937) (0.937)
Household size -0.536 -0.519 -0.536
(0.413) (0.413) (0.413)
Number of children 0.985 ∗ 0.969∗ 0.981∗
(0.569) (0.569) (0.569)
Mortgagor -1.846 ∗∗ -1.805∗∗ -1.858∗∗
(0.788) (0.788) (0.788)
Renter -3.098 ∗∗∗ -3.107∗∗∗ -3.214∗∗∗
(1.179) (1.180) (1.180)
Constant 45.955 ∗∗∗ 45.591∗∗∗ 45.893∗∗∗
(3.532) (3.540) (3.528)
Year fixed effects Yes Yes Yes
Observations 63,602 63,602 63,602
Households 26,814 26,814 26,814
Notes: FE estimates. Robust standard errors clus-
tered at the household level in parentheses. Data
come from the Household Finance and Consumption
Survey, 2017–2023. Sample is restricted to house-
holds whose head is between 22 and 79 years old,
have no negative family income and whose income is
not entirely derived from self-employment, observed
for at least two periods. ∗ p <0.10, ∗∗ p <0.05, ∗∗∗
p <0.01. 22

In Table 7 we show that our main results are robust to different robustness checks in-
volving alternative subsamples or model specifications. Mimicking Jappelli and Pistaferri
(2014, 2020), in Column (1), we rerun our Eq. (1) after excluding those who declare MPCs
equal to the 50 value, which may indicate respondent indecisiveness and measurement
error, whereas in Column (2) we only keep those households who declare that their spend-
ing during the year was similar to what they would do in a “normal” year (Castaldo and
Tirelli, 2025). 28 The reported MPC could depend on the macroeconomic context (Jap-
pelli and Pistaferri, 2014). In our unbalanced panel, the sample period includes the year
immediately following the Covid-19 pandemic, which may bias the MPC estimates, in-
fluence HtM transitions and limit the external validity of our findings, even though the
most common reference period was not 2020 and ultimately conducted throughout 2021.
In Column (3) we include an indicator for those who declare a loan rejection or were dis-
couraged from applying for credit in the past 12 months, an important control according
to previous estimates on MPCs (Bunn et al., 2018; Jappelli and Pistaferri, 2020), along
with total non-durable consumption (in logarithmic terms) as our proxy for permanent
income (Jappelli and Pistaferri, 2020; Boehm et al., 2025). Fourth, in Column (4), we
restrict the sample to household heads aged 25–64 (Aguiar et al., 2025) to minimize the
influence of major life-cycle decisions, such as retirement. Besides, many of the variables
considered, such as housing tenure, seem closely related to the HtM status of a house-
hold. However, removing this control variable does not affect the results in Column (5)
of Table 7. Another issue is that the estimates for individual variables, such as the neg-
ative statistically significant coefficient estimated for employed households, could reflect
changes in the household head’s identity. Nevertheless, restricting to same household
heads with no changes in marital status (Blundell et al., 2008; Jappelli and Pistaferri,
2020) does not alter our main findings in Column (6). 29 For the sake of simplicity, we
only report the significant coefficients estimated in Table 7, which are robust and very
similar.30
28The question is: “Aside from any purchases of assets, would you say that your household’s regu-
lar expenses over the last 12 months were higher than normal, lower than normal, or were they about
normal?”. We keep households who report that their consumption in 2021 was “just about normal”.
29We emphasize that this does not impact household variables, such as the dummy variables denoting
HtM household status.
30We explore other alternatives for the structure of the error term, like country level clustered standard
errors, and find identical conclusions.
23

Table 7: Robustness checks, fixed effects regression results
No MPCs equal to 50 “Normal” consumption in 2021 Additional controls Heads aged 25–64 No housing tenure variables Same household head
Poor HtM 2.206 0.222 0.659 0.881 0.961 0.872
(1.819) (1.550) (1.381) (1.541) (1.362) (1.597)
Wealthy HtM -1.733 ∗∗ -2.059∗∗∗ -1.676∗∗∗ -1.393∗∗ -1.631∗∗∗ -1.394∗∗
(0.750) (0.630) (0.529) (0.614) (0.523) (0.594)
Employed -2.858 ∗∗∗ -2.432∗∗∗ -2.539∗∗∗ -2.661∗∗∗ -2.545∗∗∗ -2.030∗∗
(0.967) (0.768) (0.674) (0.806) (0.667) (0.797)
Mortgagor -2.202 ∗ -1.287 -1.792 ∗∗ -1.285 — -1.730 ∗∗
(1.143) (0.921) (0.799) (0.906) (0.870)
Renter -3.027 ∗ -3.043∗∗ -3.022∗∗ -3.051∗∗ — -3.501 ∗∗∗
(1.679) (1.344) (1.188) (1.355) (1.319)
Credit constraints — — 0.087 — — —
(0.885)
Permanent income — — 0.794 ∗∗ — — —
(0.332)
Rest of controls from Eq. (1) Yes Yes Yes Yes Yes Yes
Year fixed effects Yes Yes Yes Yes Yes Yes
Observations 39,261 46,378 62,844 40,648 63,602 52,088
Households 17,435 20,312 26,591 17,461 26,814 22,355
Notes: FE estimates. Robust standard errors clustered at the household level in parentheses. Data come from the Household Finance and Consumption
Survey, 2017–2023. Sample is restricted to households whose head is between 22 and 79 years old, have no negative family income and whose income is not
entirely derived from self-employment, observed for at least two periods. ∗ p <0.10, ∗∗ p <0.05, ∗∗∗ p <0.01.
24

Given the harmonized cross-country design of the survey, in Table 8 we analyze the
relationship between HtM and MPC behavior across country groups. Specifically, we
group countries into Western (Belgium, Germany, France, Ireland, Netherlands), South-
ern (Cyprus, Spain, Italy, Malta), and Eastern (Estonia, Lithuania, Latvia, Slovakia)
European countries.31 We find consistent results across all these country groups.
Finally, we examine coarse responses and focus on the fraction of households reporting
MPCs of 0, 50, and 100 percent in Table 9. To do so, we estimate linear probability
models with household fixed effects for three separate binary outcomes, each taking the
value 1 when the reported MPC equals 0, 50, and 100 percent, respectively. We find
that wealthy HtM households are 2.4 percentage points more likely to save the additional
income. In contrast, poor HtM households are 5.7 percentage points more likely than
non-HtM households to spend the entire income windfall, consistent with life-cycle models
incorporating binding financial constraints. Besides, they are also less likely to report an
MPC of 50 percent. This latter finding may reflect either behavioral differences or a lower
degree of uncertainty in the interpretation of the survey question (Jappelli and Pistaferri,
2020).
31Limited sample sizes within countries prevent a detailed analysis at the country level. Table B.3
reports the country-level sample composition of the unbalanced panel.
25

Table 8: Fixed effects regression results across country groups
Western Southern Eastern
Poor HtM 0.819 0.695 4.265
(2.131) (1.862) (5.180)
Wealthy HtM -1.153 ∗ -1.830∗∗ -4.296∗∗
(0.680) (0.930) (1.768)
Male 0.547 2.275 ∗ 2.457
(1.236) (1.223) (2.500)
25 – 29 years -0.110 0.885 9.528
(3.209) (6.604) (9.525)
30 – 34 years 3.571 6.295 1.769
(3.482) (6.545) (9.813)
35 – 39 years 2.562 3.376 -0.245
(3.682) (6.532) (9.921)
40 – 44 years 1.826 1.550 0.365
(3.799) (6.519) (10.013)
45 – 49 years 1.776 1.120 3.353
(3.911) (6.462) (9.947)
50 – 54 years -0.269 1.137 2.444
(3.991) (6.467) (9.980)
55 – 59 years -0.015 1.344 4.444
(4.122) (6.471) (10.126)
60 – 64 years 0.245 0.216 3.103
(4.275) (6.526) (10.390)
65 – 69 years 1.102 1.264 4.407
(4.446) (6.616) (10.642)
70 – 74 years -0.380 2.439 4.088
(4.685) (6.719) (10.992)
75 – 79 years 0.829 2.977 1.626
(4.989) (6.876) (11.488)
Secondary education 3.546 -1.418 -25.207 ∗∗∗
(2.764) (1.505) (9.149)
Tertiary education 1.514 -0.373 -26.006 ∗∗∗
(3.014) (2.128) (9.129)
Employed -3.603 ∗∗∗ -2.140∗∗ 0.510
(1.001) (0.996) (2.037)
Married -0.010 -0.133 -3.735
(1.308) (1.537) (2.907)
Household size -1.013 0.106 -1.335
(0.641) (0.605) (1.308)
Number of children 1.570 ∗∗ -0.112 2.705
(0.764) (0.954) (1.907)
Mortgagor -1.566 -2.248 ∗ -3.875
(1.068) (1.283) (3.310)
Renter -4.641 ∗∗∗ 0.037 -6.795
(1.580) (1.942) (5.203)
Constant 44.724 ∗∗∗ 42.965∗∗∗ 73.204∗∗∗
(5.009) (6.755) (13.938)
Year fixed effects Yes Yes Yes
Observations 32,374 24,868 6,360
Households 13,301 10,352 3,161
Notes: FE estimates. Robust standard errors clus-
tered at the household level in parentheses. Data
come from the Household Finance and Consumption
Survey, 2017–2023. Sample is restricted to house-
holds whose head is between 22 and 79 years old,
have no negative family income and whose income is
not entirely derived from self-employment, observed
for at least two periods. ∗ p <0.10, ∗∗ p <0.05, ∗∗∗
p <0.01.
26

Table 9: Linear probability model results
MPC equal to 0 MPC equal to 50 MPC equal to 100
Poor HtM 0.022 -0.038 ∗∗ 0.057∗∗∗
(0.016) (0.015) (0.016)
Wealthy HtM 0.024 ∗∗∗ -0.004 -0.007
(0.007) (0.007) (0.006)
Employed 0.030 ∗∗∗ -0.007 -0.014 ∗
(0.008) (0.009) (0.007)
Mortgagor 0.032 ∗∗∗ -0.005 -0.006
(0.010) (0.010) (0.009)
Rest of controls from Eq. (1) Yes Yes Yes
Year fixed effects Yes Yes Yes
Observations 63,602 63,602 63,602
Households 26,814 26,814 26,814
Notes: Linear probability model with FE estimates. Robust standard errors clustered at the
household level in parentheses. Data come from the Household Finance and Consumption
Survey, 2017–2023. Sample is restricted to households whose head is between 22 and 79
years old, have no negative family income and whose income is not entirely derived from self-
employment, observed for at least two periods. ∗ p <0.10, ∗∗ p <0.05, ∗∗∗ p <0.01.
5 Conclusions
A key parameter driving the excess sensitivity of consumption to income changes is
liquidity constraints. This paper studies the consumption responses to income changes of
HtM households in Europe. To do so, it uses harmonized cross-country data from a total
of 23 countries of the HFCS over 2010–2023 and examines the MPC across these groups
through a hypothetical survey question that captures how households believe they would
modify their consumption in response to a transitory, unexpected, income gain. Related
literature has typically used semistructural methods based on statistical decomposition
and covariance restrictions on the joint distribution of income and consumption growth,
which requires very long panels along with information on all the components of the
budget constraint rarely available.
We find wide cross-country heterogeneity and that the shares of HtM households
oscillate from 13.9% in Czech Republic to 70.6% in Greece. In addition, the vast majority
of HtM households are wealthy in Europe, over 60% in all countries analyzed, indicating
that most of those households hold positive, and sometimes substantial, amounts of
illiquid wealth. This result is consistent with previous works in either developed or
developing economies. Specifically, the percentage of HtM that are considered wealthy
HtM ranges from 64% in Ireland and Italy to 90% in Greece, Luxembourg and Malta.
Concerning MPCs, poor HtM households exhibit the highest MPC, as expected due to
their limited access to both liquid and illiquid assets, whereas wealthy HtM households
have lower MPCs compared to their non-HtM counterparts.
27

The dataset further enables us to analyze potential biases arising from cross-sectional
regressions on the MPC, as it follows a subset of households over time which allows
to focus on households who switch their HtM status over time. Interestingly, we show
that pooled OLS estimates exaggerate the estimates for poor and wealthy HtM house-
holds. Specifically, the initial positive association reported for poor HtM households is
no longer statistically significant once household unobserved heterogeneity is accounted
for. Similarly, the estimated relationship for wealthy HtM households remains negative
and statistically significant, although it is lower in absolute terms after controlling for
cofounders and household unobserved heterogeneity. Finally, we show that poor HtM
households are more likely to spend the whole windfall gain. All these results align with
life-cycle models with liquidity constraints and precationary saving motives.
Overall, these MPC results highlight the joint analysis of liquid and illiquid assets
in the household balance sheets to identify constrained households and study the excess
sensitivity in consumption to temporary changes in income. As expected, the fraction
of poor HtM households correlates positively with the MPC. However, the heterogeneity
shown within HtM households suggests that liquid wealth may be an imperfect proxy to
define financial constrained status across households.
This paper offers new results on the fraction of HtM households and their consump-
tion behavior using harmonized cross-country data in Europe. Despite the important
findings, we are aware of several limitations arising from this work that may motivate
future works. On the one hand, the variable concerning the MPC only considers hypo-
thetical windfall gains and consumption/saving choices on the short-run. The sign of
income shocks is an important determinant of the MPC, whereas the windfall gain may
induce debt repayments or portfolio allocation, in addition to spending or saving. On the
other, similar to other methodological alternatives, limitations concerning this reported
approach to estimating MPCs include its external validity and quality of data, despite
recent work pointing to the validity of this approach.
28

References
Aguiar, M., M. Bils, and C. Boar (2025). Who are the hand-to-mouth?Review of
Economic Studies92(3), 1293–1340.
Albacete, N., P. Fessler, and A. Pekanov (2025). The role of MPC heterogeneity for fiscal
policy in the euro area.Journal of Macroeconomics, 103719.
Albuquerque, B. (2019). Household heterogeneity and consumption dynamics in the
presence of borrowing and liquidity constraints.Applied Economics Letters26(6),
454–459.
Albuquerque, B. and G. Green (2023). Financial concerns and the marginal propensity to
consume in COVID times: Evidence from UK survey data.Journal of Macroeconomics
78, 103563.
Almgren, M., J.-E. Gallegos, J. Kramer, and R. Lima (2022). Monetary policy and liq-
uidity constraints: Evidence from the euro area.American Economic Journal: Macroe-
conomics14(4), 309–340.
Arellano, M., O. Attanasio, S. Crossman, and V. Sancibri´ an (2024). Estimating flexible
income processes from subjective expectations data: Evidence from India and Colom-
bia. Working Paper 32922, National Bureau of Economic Research.
Attanasio, O. P. and G. Weber (2010). Consumption and saving: Models of intertemporal
allocation and their implications for public policy.Journal of Economic Literature
48(3), 693–751.
Bartscher, A. K., M. Kuhn, M. Schularick, and U. I. Steins (2025). The distribution
of household debt in the United States, 1950–2022.Review of Economic Dynamics,
101288.
Belloc, I., J. A. Molina, and J. Velilla (2025). Consumption responses to inheritances:
The role of durable goods.Journal of Macroeconomics83, 103661.
Belloc, I. and J. A. Molina (2026). How inheritance expectations impact household
savings.Review of Income and Wealth72(1), e70044.
Blundell, R., L. Pistaferri, and I. Preston (2008). Consumption inequality and partial
insurance.American Economic Review98(5), 1887–1921.
Blundell, R., L. Pistaferri, and I. Saporta-Eksten (2016). Consumption inequality and
family labor supply.American Economic Review106(2), 387–435.
Boehm, J., E. Fize, and X. Jaravel (2025). Five facts about MPCs: Evidence from a
randomized experiment.American Economic Review115(1), 1–42.
Bruine de Bruin, W., A. Chin, J. Dominitz, and W. Van der Klaauw (2022). Household
surveys and probabilistic questions. InHandbook of Subjective Expectations, Chapter 1.
Elsevier.
Bryukhanov, M. and D. Hryshko (2024). Inequality in Russia over time and over the life
cycle.The Scandinavian Journal of Economics126(2), 289–319.
29

Bunn, P., J. Le Roux, K. Reinold, and P. Surico (2018). The consumption response to
positive and negative income shocks.Journal of Monetary Economics96, 1–15.
Campbell, J. R. and Z. Hercowitz (2019). Liquidity constraints of the middle class.
American Economic Journal: Economic Policy11(3), 130–155.
Castaldo, S. and M. Tirelli (2025). Subjective income risk and precautionary saving.
Economic Modelling143, 106965.
Cherchye, L., T. Demuynck, B. De Rock, M. Kovaleva, G. Minne, M. De Sola Perea, and
F. Vermeulen (2024). Poor and wealthy hand-to-mouth households in Belgium.Review
of Economics of the Household22(3), 909–934.
Christelis, D., D. Georgarakos, T. Jappelli, L. Pistaferri, and M. Van Rooij (2019).
Asymmetric consumption effects of transitory income shocks.The Economic Jour-
nal129(622), 2322–2341.
Christelis, D., D. Georgarakos, T. Jappelli, and M. Van Rooij (2020). Consumption
uncertainty and precautionary saving.Review of Economics and Statistics102(1),
148–161.
Christelis, D., D. Georgarakos, T. Jappelli, L. Pistaferri, and M. Van Rooij (2021). Het-
erogeneous wealth effects.European Economic Review137, 103805.
Christelis, D., D. Georgarakos, T. Jappelli, and G. Kenny (2025). Wealth shocks and
portfolio choice.Journal of Monetary Economics149, 103632.
Colarieti, R., P. Mei, and S. Stantcheva (2024). The how and why of household reactions
to income shocks. Working Paper 32191, National Bureau of Economic Research.
Commault, J. (2022). Does consumption respond to transitory shocks? Reconciling nat-
ural experiments and semistructural methods.American Economic Journal: Macroe-
conomics14(2), 96–122.
Cox, D. and T. Jappelli (1993). The effect of borrowing constraints on consumer liabilities.
Journal of Money, Credit and Banking25(2), 197–213.
Crawley, E. (2020). In search of lost time aggregation.Economics Letters189, 108998.
Crawley, E. and A. Theloudis (2024). Income shocks and their transmission into con-
sumption. Working Paper 2404.12214, arXiv.
Crossley, T. F., P. Fisher, P. Levell, and H. Low (2021). MPCs in an economic crisis:
Spending, saving and private transfers.Journal of Public Economics Plus2, 100005.
Cui, Z. and Y. Feng (2017). Wealthy hand-to-mouth households in China.Asian Eco-
nomic Journal31(3), 275–297.
Cutanda, A. and J. A. Sanchis (2025). How interest rates influence hand-to-mouth con-
sumption patterns. Working Paper.
Drescher, K., P. Fessler, and P. Lindner (2020). Helicopter money in Europe: New evi-
dence on the marginal propensity to consume across European households.Economics
Letters195, 109416.
30

Du Caju, P., G. P´ erilleux, F. Rycx, and I. Tojerow (2023). A bigger house at the cost
of an empty stomach? The effect of households’ indebtedness on their consumption:
micro-evidence using Belgian HFCS data.Review of Economics of the Household21(1),
291–333.
Duarte, J. B. and N. Pereira (2023). The effect of monetary policy on household con-
sumption expenditures in Portugal: A decomposition of the transmission channel.Por-
tuguese Economic Journal22(2), 149–172.
Fagereng, A., M. B. Holm, and G. J. Natvik (2021). MPC heterogeneity and household
balance sheets.American Economic Journal: Macroeconomics13(4), 1–54.
Fisher, J. D., D. S. Johnson, T. M. Smeeding, and J. P. Thompson (2020). Estimating
the marginal propensity to consume using the distributions of income, consumption,
and wealth.Journal of Macroeconomics65, 103218.
Friedman, M. (1957). The permanent income hypothesis. InA Theory of the Consumption
Function, pp. 20–37. Princeton University Press.
Fuchs-Sch¨ undeln, N. and T. A. Hassan (2016). Natural experiments in macroeconomics.
InHandbook of Macroeconomics, Volume 2, pp. 923–1012. Elsevier.
Fuster, A., G. Kaplan, and B. Zafar (2021). What would you do with$500? Spending
responses to gains, losses, news, and loans.The Review of Economic Studies88(4),
1760–1795.
Georgarakos, D., T. Jappelli, G. Kenny, and L. Pistaferri (2025). Labor supply response
to windfall gains.Journal of Public Economics250, 105476.
Ghosh, A. and A. Theloudis (2025). Consumption partial insurance in the presence of
tail income risk. Working Paper 2306.13208, arXiv.
Golosov, M., M. Graber, M. Mogstad, and D. Novgorodsky (2024). How Americans
respond to idiosyncratic and exogenous changes in household wealth and unearned
income.The Quarterly Journal of Economics139(2), 1321–1395.
Gupta, V., F. Pizzolon, and A. Singh (2025). Identifying hand-to-mouth households:
Evidence from India. Working Paper 5559305, SSRN.
Hara, R., T. Unayama, and J. Weidner (2016). The wealthy hand to mouth in Japan.
Economics Letters141, 52–54.
Jappelli, T. (1990). Who is credit constrained in the US economy?The Quarterly Journal
of Economics105(1), 219–234.
Jappelli, T. and L. Pistaferri (2010). The consumption response to income changes.
Annual Review of Economics2(1), 479–506.
Jappelli, T. and L. Pistaferri (2014). Fiscal policy and MPC heterogeneity.American
Economic Journal: Macroeconomics6(4), 107–136.
Jappelli, T. and L. Pistaferri (2020). Reported MPC and unobserved heterogeneity.
American Economic Journal: Economic Policy12(4), 275–297.
31

Jappelli, T. and L. Pistaferri (2025). Permanent income shocks, target wealth, and the
wealth gap.American Economic Journal: Macroeconomics17(1), 102–125.
Jappelli, T., E. Savoia, and L. Pistaferri (2026). Intertemporal MPC and shock size.
European Economic Review186.
Johnson, D. S., J. A. Parker, and N. S. Souleles (2006). Household expenditure and the
income tax rebates of 2001.American Economic Review96(5), 1589–1610.
Johnson, K. W. and G. Li (2010). The debt-payment-to-income ratio as an indicator
of borrowing constraints: Evidence from two household surveys.Journal of Money,
Credit and Banking42(7), 1373–1390.
Kaplan, G., G. L. Violante, and J. Weidner (2014). The wealthy hand-to-mouth.Brook-
ings Papers on Economic Activity1, 77–153.
Kim, S. and K. Koh (2025). Consumption responses to income shocks through lottery
winning: Evidence from older adults in Singapore.Oxford Bulletin of Economics and
Statistics87(1), 1–25.
Ko¸ sar, G. and C. O’Dea (2023). Expectations data in structural microeconomic models.
InHandbook of Economic Expectations, pp. 647–675. Elsevier.
Manski, C. F. (2018). Survey measurement of probabilistic macroeconomic expectations:
Progress and promise.NBER Macroeconomics Annual32(1), 411–471.
Modigliani, F. and R. H. Brumberg (1954). Utility analysis and the consumption function:
An interpretation of cross-sectional data. In K. K. Kurihara (Ed.),Post Keynesian
Economics, pp. 388–436. Rutgers University Press.
Paiella, M. and L. Pistaferri (2017). Decomposing the wealth effect on consumption.
Review of Economics and Statistics99(4), 710–721.
Park, K. Y. (2017). The wealthy hand-to-mouth households in South Korea.Global
Economic Review46(3), 299–324.
Parker, J. A., N. S. Souleles, D. S. Johnson, and R. McClelland (2013). Consumer
spending and the economic stimulus payments of 2008.American Economic Review
103(6), 2530–2553.
Sala, H. and P. Trivin (2024). Household finances, debt overhang and consumption
patterns.Economic Modelling139, 106836.
Slacalek, J., O. Tristani, and G. L. Violante (2020). Household balance sheet channels
of monetary policy: A back of the envelope calculation for the euro area.Journal of
Economic Dynamics and Control115, 103879.
Sokolova, A. (2023). Marginal propensity to consume and unemployment: A meta-
analysis.Review of Economic Dynamics51, 813–846.
Song, S.-Y. (2020). Leverage, hand-to-mouth households, and heterogeneity of the
marginal propensity to consume: Evidence from South Korea.Review of Economics
of the Household18(4), 1213–1244.
32

Toussaint-Comeau, M. (2021). Liquidity constraints and debts: Implications for the
saving behavior of the middle class.Contemporary Economic Policy39(3), 479–493.
Trivin, P. (2022). The wealth-consumption channel: Evidence from a panel of Spanish
households.Review of Economics of the Household20(4), 1377–1428.
Trivin, P. (2024). The marginal propensity to consume. Working Paper.
Ueda, K. (2025). The reality of consumption: Comparing self-reported and observed
marginal propensity to consume.Economics Letters247, 112179.
Wu, C. and D. Krueger (2021). Consumption insurance against wage risk: Family la-
bor supply and optimal progressive income taxation.American Economic Journal:
Macroeconomics13(1), 79–113.
Zeldes, S. P. (1989). Consumption and liquidity constraints: An empirical investigation.
Journal of Political Economy97(2), 305–346.
33

Appendix
A Additional results HtM
Table A.1: Comparison between HtM definitions
Country Baseline Zeldes in net worth Zeldes in labor income
Austria 28.721 7.148 7.958
Belgium 26.045 6.589 6.297
Cyprus 43.280 11.218 11.339
Czech Republic 13.894 5.084 5.448
Germany 25.950 11.693 12.879
Estonia 22.990 6.528 6.382
Spain 23.326 10.133 12.062
Finland 30.100 11.636 12.893
France 27.864 8.731 8.791
Greece 70.634 10.275 11.471
Hungary 31.793 5.963 6.205
Croatia 41.187 6.594 7.576
Ireland 36.527 20.601 24.359
Italy 22.944 8.921 10.208
Lithuania 27.193 2.871 2.798
Luxembourg 26.012 6.452 7.491
Latvia 35.925 9.406 8.844
Malta 29.644 3.415 3.595
Netherlands 29.859 11.707 13.659
Poland 26.181 5.841 5.719
Portugal 25.967 8.937 9.400
Slovenia 37.484 8.306 8.764
Slovakia 26.329 3.698 3.604
Pooled 27.286 9.515 10.434
Notes: Data come from the Household Finance and Consumption Survey, 2010–
2023. Figures refer to sample averages, calculated using population weights and
bootstrapped replicated weights. Column (3) focuses on 250,172 households with
heads aged 25–64 years.
1

Table A.2: HtM households, alternative definitions
Main criteria Pay period of 1 week Pay period of 1 month Other illiquid
Country Wealthy Poor Total Wealthy Poor Total Wealthy Poor Total Wealthy Poor Total
Austria 24.200 4.521 28.721 15.263 3.495 18.758 39.289 5.970 45.260 26.063 2.525 28.588
Belgium 21.833 4.212 26.045 15.235 3.468 18.702 33.347 5.123 38.471 23.758 2.177 25.935
Cyprus 33.478 9.801 43.280 30.731 9.167 39.897 38.580 10.565 49.145 40.461 2.742 43.203
Czech Republic 9.800 4.905 13.894 7.658 3.551 11.209 14.764 4.894 19.658 11.669 2.157 13.827
Germany 18.584 7.366 25.950 14.166 6.361 20.527 28.263 8.740 37.003 21.429 4.466 25.895
Estonia 18.173 4.818 22.991 14.669 4.248 18.917 24.306 5.612 29.918 19.358 3.608 22.966
Spain 15.560 7.765 23.326 13.369 7.059 20.427 20.223 9.537 29.761 19.582 3.738 23.321
Finland 22.521 7.579 30.100 20.389 6.748 27.136 26.847 9.146 35.993 26.143 3.784 29.927
France 24.550 3.314 27.864 17.736 2.352 20.088 40.147 4.825 44.972 27.782 0.128 27.911
Greece 65.325 5.309 70.634 64.041 4.952 68.994 67.843 5.901 73.744 66.945 2.672 69.617
Hungary 26.929 4.864 31.793 22.685 4.385 27.070 34.365 5.816 40.181 28.397 3.396 31.793
Croatia 35.377 5.809 41.187 30.261 5.289 35.550 43.724 6.882 50.606 39.175 2.008 41.184
Ireland 23.671 12.856 36.527 18.884 10.952 29.836 30.709 15.387 46.096 30.635 5.819 36.454
Italy 14.630 8.315 22.944 13.402 7.714 21.115 17.545 9.543 27.087 21.453 1.521 22.974
Lithuania 24.874 2.319 27.193 18.850 1.661 20.511 36.621 3.091 39.712 25.882 1.308 27.190
Luxembourg 22.050 3.962 26.012 18.039 3.463 21.502 29.754 5.100 34.853 24.520 1.453 25.973
Latvia 28.740 7.185 35.925 23.098 6.250 29.348 36.926 8.981 45.906 30.614 5.410 36.024
Malta 27.199 2.445 29.644 25.229 2.135 27.364 31.127 2.816 33.943 29.077 0.760 29.837
Netherlands 25.089 4.770 29.859 18.971 3.936 22.907 36.251 6.183 42.431 27.413 2.405 29.818
Poland 21.449 4.732 26.181 17.499 4.236 21.735 30.912 5.482 36.393 22.803 3.378 26.181
Portugal 18.613 7.355 25.967 14.195 6.132 20.328 28.359 9.319 37.678 22.105 3.769 25.874
Slovenia 30.281 7.202 37.484 25.939 6.053 31.992 37.844 8.433 46.277 34.916 2.462 37.377
Slovakia 23.211 3.118 26.329 18.333 2.511 20.844 32.281 3.811 36.091 24.525 1.755 26.280
Pooled 21.115 6.172 27.286 16.888 5.349 22.236 30.087 7.529 37.617 24.629 2.647 27.276
Notes: Data come from the Household Finance and Consumption Survey, 2010–2023. Figures refer to
sample averages, calculated using population weights and bootstrapped replicated weights.
2

B Additional results MPC
Table B.1: Average values for the MPC
Country MPC
Austria 47.220
Belgium 39.183
Cyprus 44.104
Germany 47.940
Estonia 37.797
Spain 39.821
France 38.773
Greece 51.676
Croatia 54.991
Italy 46.941
Lithuania 54.998
Luxembourg 34.422
Latvia 49.502
Malta 51.070
Netherlands 33.512
Portugal 29.205
Slovenia 48.065
Slovakia 54.298
Pooled 43.534
Notes: Data come from the Household Finance and Consumption Survey, 2017–2023.
3

Table B.2: Transition rates for reported MPCs
MPC equal to 0 attMPC equal to 50 attMPC equal to 100 att
Panel A: 21,345 households
MPC equal to 0 att+ 1 0.464 0.208 0.201
MPC equal to 50 att+ 1 0.202 0.376 0.247
MPC equal to 100 att+ 1 0.143 0.159 0.381
Panel B: 7,543 households
MPC equal to 0 att+ 2 0.435 0.212 0.223
MPC equal to 50 att+ 2 0.221 0.366 0.252
MPC equal to 100 att+ 2 0.155 0.168 0.340
Notes: Data come from the Household Finance and Consumption Survey, 2017–2023.
4

Figure B.1: Histogram of the distribution on reported MPC
Notes:The figure shows the distribution of the responses to the survey question eliciting the MPC.
Sample size is 157,430. Data come from the Household Finance and Consumption Survey, 2017–2023.
MPC in percent on horizontal axis. Response frequency in frequent on vertical axis.
5

Figure B.2: Histogram of the distribution on the change in MPC
Notes:The figure shows the distribution of the changes in reported MPCs. Sample size is 36,788.
Data come from the Household Finance and Consumption Survey, 2017–2023. The change in MPC
in percent on horizontal axis. Response frequency in frequent on vertical axis.
6

Table B.3: Sample composition by country, unbalanced panel sample
Country # households # observations
Belgium 1,234 2,897
Cyprus 901 2,310
Germany 2,823 7,244
Estonia 1,243 2,486
Spain 4,621 11,052
France 7,669 18,342
Italy 4,385 10,616
Lithuania 303 644
Latvia 299 598
Malta 445 890
Netherlands 1,575 3,891
Slovakia 1,316 2,632
Pooled 26,814 63,602
Notes: Data come from the Household Finance and Consumption Survey,
2017–2023. Sample is restricted to households whose head is between 22
and 79 years old, have no negative family income and whose income is not
entirely derived from self-employment, observed for at least two periods.
7
