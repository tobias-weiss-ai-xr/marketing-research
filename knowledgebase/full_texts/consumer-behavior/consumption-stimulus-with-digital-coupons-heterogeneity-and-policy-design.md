---
title: 'Consumption Stimulus with Digital Coupons: Heterogeneity and Policy Design'
url: https://arxiv.org/abs/2507.01365
category: consumer-behavior
subcategory: empirical
date: 2025-07
venue: ''
authors:
- Ying Chen
- Mingyi Li
- Jonathan J. Mao
- Jingyi Zhou
source: arxiv
pdf_url: https://arxiv.org/pdf/2507.01365
pages: 68
chars: 180524
fetched_at: '2026-11-08T13:14:06+00:00'
kb_version: 1
---

# Consumption Stimulus with Digital Coupons: Heterogeneity and Policy Design

Consumption Stimulus with Digital Coupons:
Heterogeneity and Policy Design
Ying Chen∗ Mingyi Li† Jonathan J. Mao ‡ Jingyi Zhou§¶
June 2026
Abstract
We study consumption stimulus using digital coupons, which provide time-limited
subsidies contingent on minimum spending. Analyzing a large-scale program in
China, we find that the program generates large and heterogeneous short-term
effects. Consumption responses vary across both consumers and locations, re-
flecting both demand-side and supply-side factors. This heterogeneity shapes
the incidence of the program: high-response consumers tend to patronize larger
businesses, leading to a regressive allocation of stimulus benefits. Through coun-
terfactual analysis, we show that targeting rules can reshape both the size and
distribution of stimulus effects. Targeting the most responsive consumers can
more than double the aggregate stimulus, while a hybrid design that combines
targeted distribution with direct support to small businesses improves both effi-
ciency and equity.
∗MOE Key Laboratory of Econometrics, School of Economics, and the Paula and Gregory Chow Institute for
Studies in Economics, Xiamen University. Email: ychen@xmu.edu.cn.
†School of Management and Economics, The Chinese University of Hong Kong, Shenzhen. Email: mingy-
ili@link.cuhk.edu.cn.
‡Corresponding author. Center for Macroeconomic Research and Wang Yanan Institute for Studies in Economics,
Xiamen University. Email: jmao@xmu.edu.cn.
§Amazon.com, Inc. Email: jingyiuohz@gmail.com.
¶We thank Ricardo Perez-Truglia, the editor, and three anonymous referees for their valuable guidance and
constructive comments. We also thank Nathaniel Baum-Snow, Felipe Carozzi, Shihe Fu, Jessie Handbury, Nathaniel
Hendren, Xavier Jaravel, Sophie Calder-Wang, Maisy Wong, and Jianwei Xing for helpful discussions and feedback.
Further helpful comments were received from conference and seminar participants at the North American Meeting of
the Urban Economics Association, Peking University, Wuhan University, CUHK-Shenzhen, and Xiamen University.
Ying Chen acknowledges financial support from the Natural Science Foundation of China [Grants NSFC72203188
and NSFC71988101]. Jonathan Mao acknowledges financial support from the Natural Science Foundation of China
[Grants NSFC72133004 and NSFC71988101]. We are grateful to Yue Wang from Rajax Network Technology (Ele.me)
for data support, and to the High Performance Computing Platform of the Key Laboratory of Econometrics (Xiamen
University), Ministry of Education, for additional data resources.
arXiv:2507.01365v3  [econ.GN]  9 Jul 2026

1 Introduction
During economic downturns, traditional monetary and fiscal policies often face limitations
in their ability to swiftly and effectively boost consumer spending. In response, government-
issued digital coupons—a form of mobile-distributed consumption voucher—have emerged
as an innovative tool to stimulate demand in targeted sectors. Unlike conventional stimulus
measures such as cash transfers or tax rebates, which are often saved rather than spent,
digital coupons feature minimum spending thresholds (e.g., spend¥50 to get¥15 off) and
short expiration periods designed to encourage immediate spending. Their digital distribu-
tion enables rapid, large-scale deployment and allows policymakers to direct support toward
sectors that are particularly vulnerable during downturns.
In this paper, we study digital coupons as a stimulus tool using comprehensive data
from a major program in Beijing, which targeted food delivery services to support the local
restaurant industry. We examine both the overall effectiveness of the program in stimulating
consumer spending and the heterogeneity in its impact across individuals and businesses.
Using detailed transaction records and user attributes from a leading Chinese food deliv-
ery platform—augmented with high-resolution housing transaction data and geocoded es-
tablishment information—we construct rich profiles of consumer demographic, wealth, and
locational characteristics that enable a detailed analysis of the program’s impact.
We begin by establishing baseline results using a difference-in-differences design that ex-
ploits the program’s first-come, first-served allocation rule. We find that, on average, digital
coupons increased daily consumption by 12 percent during the program period. For every¥1
of government subsidy, consumers spent an additional¥2.38 of their own money, resulting
in a spending multiplier of 3.38. Following Ding et al. (2025), we refer to this multiplier as
the coupon MPC—the marginal propensity to consume out of coupon subsidies. Our esti-
mate implies that for every yuan of increased business revenue, approximately one-quarter is
financed by government subsidies, while the remaining three-quarters come from consumers’
out-of-pocket spending. This result highlights a distinctive feature of digital coupons: unlike
conventional stimulus payments where consumers are net recipients of government funds,
with digital coupons, both consumers and the government jointly finance the increase in
business revenue.1
While average effects are informative, they mask substantial variation in individual
responses—variation that is central to understanding both the drivers of stimulus effec-
tiveness and the distribution of benefits. We therefore estimate heterogeneous treatment
effects to examine how the program’s impact varies across both consumers and businesses.
Two key questions guide our heterogeneity analysis. First, we hypothesize that the con-
sumption response to digital coupons is shaped by both demand- and supply-side factors.
1Ding et al. (2025) refers to this feature as “consumer-financed stimulus.”
1

On the demand side, factors such as personal income and wealth influence how much a per-
son spends after receiving digital coupons. On the supply side, the availability and variety
of local businesses determine the opportunity for coupon redemption. 2 For example, two
otherwise similar individuals may exhibit different responses if one resides in an area with
abundant food delivery options, while the other lives in a neighborhood with limited choices.
Consequently, the impact of a digital coupon program varies not only among individuals but
across locations. This spatial variation in stimulus effects, which has not been studied in the
literature to date, could have important implications for how benefits are distributed among
local businesses. Furthermore, wealthier individuals tend to sort into neighborhoods with
greater consumption amenities (Couture and Handbury, 2020), leading to an intertwining
of demand and supply effects. Although existing research consistently identifies income or
wealth as key determinants of consumption responses to fiscal stimulus, 3 it remains unclear
whether these effects are driven by income or wealth itself or are partly attributable to spatial
sorting across locations. Disentangling these mechanisms will improve our understanding of
how heterogeneous individuals and locations jointly shape program outcomes.
Second, because digital coupons act as a stimulus jointly financed by the government and
consumers, they impact businesses and consumers in different ways. This raises the ques-
tion of which businesses benefit most from the program, who the paying consumers are, and
whether these outcomes align with policymakers’ objectives. For instance, if the benefits
accrue primarily to large businesses or if the financing burden falls mainly on consumers
with low income or wealth, the program may fail to achieve its intended policy goals. Un-
derstanding these dynamics is essential for assessing the program’s distributional impact.
Moreover, policymakers may face trade-offs in designing such programs, depending on how
consumer spending patterns interact with business characteristics. If large establishments at-
tract wealthier consumers—and these consumers contribute more out-of-pocket in response
to digital coupons—then maximizing the total stimulus may require targeting these indi-
viduals, potentially concentrating benefits among large businesses. Conversely, prioritizing
support for small businesses may require directing more coupons to lower-income consumers,
resulting in both a weaker overall stimulus and a program that relies more heavily on their
spending as its source of financing.4 Recognizing these potential trade-offs can be important,
which has so far been overlooked in both academic and policy discussions.
2In this paper, we use the term “supply-side” to refer to local consumption opportunities—the set of spending
options available to consumers—rather than to firm-level behavioral responses such as price adjustments or changes
in operating practices.
3See, e.g., Johnson et al. (2006); Parker et al. (2013); Broda and Parker (2014); Misra and Surico (2014); Parker
et al. (2022).
4 We discuss distributional and policy-design implications in Section 5. Under a standard rational benchmark,
receiving digital coupons should weakly increase consumer welfare, so directing more coupons to lower-income con-
sumers would directly benefit them even if their out-of-pocket spending rises. However, if behavioral mechanisms also
shape spending responses, then relying more heavily on lower-income consumers’ spending to finance the stimulus
effect may have ambiguous welfare implications for those consumers, even if the policy raises business revenue.
2

Our empirical analysis builds on modern econometric and machine learning methods. We
nonparametrically estimate heterogeneous treatment effects using the causal forest algorithm
(Athey et al., 2019), adapted to a difference-in-differences setting to recover individual-level
conditional average treatment effects on the treated based on each consumer’s full set of
demographic, wealth, and locational characteristics. Following Semenova and Chernozhukov
(2020), we debias these estimates using augmented inverse-propensity weighting and conduct
inference using their best linear projection framework. Finally, we apply the accumulated
local effects approach of Apley and Zhu (2020) to characterize the marginal influence of
each characteristic on treatment effect heterogeneity while accounting for correlations among
covariates, including spatial sorting between demand- and supply-side variables.
Our analysis yields four main findings. First, we uncover substantial heterogeneity in the
consumption response to digital coupons. The distribution of estimated individual treat-
ment effects was highly dispersed: the standard deviation exceeded twice the average effect.
This dispersion translated into a wide range of implied coupon MPCs. Over 23 percent of
consumers had coupon MPCs above five, indicating very large spending responses. At the
other end of the distribution, 19 percent of consumers had coupon MPCs below one and
reduced their out-of-pocket expenditure. For these individuals, the coupons generated net
savings. Beyond individual heterogeneity, stimulus effects also varied substantially across
locations. Aggregating treatment effects within 3km-by-3km neighborhoods, we found that
neighborhood-level spending gains ranged from less than 10 percent in some areas to more
than 50 percent in others. These patterns highlight the limitations of relying on a single
average response when evaluating stimulus policies.
Second, both demand- and supply-side factors contribute to the variation in stimulus
effects. On the demand side, we identify a strong positive relationship between individual
wealth and consumption response. Consumption habits also matter, with spending increases
concentrated among individuals who historically placed the most frequent orders and spent
the most per order. On the supply side, we uncover a non-monotonic relationship between
consumption response and establishment density. Out-of-pocket spending initially rose with
the number of local businesses but declined beyond a threshold. Conditional on total estab-
lishment count, neighborhoods with a disproportionate share of large businesses generated
significantly higher spending. These findings suggest that digital coupons have limited stim-
ulus effects in both food deserts and areas saturated with small establishments. Thus, both
the availability and composition of consumption amenities shape the program’s effective-
ness. A variance decomposition analysis shows that demand- and supply-side determinants
contribute in broadly comparable magnitudes, with demand playing a modestly larger role.
Third, our findings point to both rational incentives and complementary behavioral mech-
anisms that may shape consumption responses. Consistent with rational, threshold-based
models of coupon use (Xing et al., 2023; Ding et al., 2025), we observe clear bunching of
3

expenditures at coupon thresholds, suggesting that some consumers adjusted their spend-
ing to qualify for redemption. At the same time, spending responses are not concentrated
in narrow regions around the coupon thresholds: treatment effects continue to rise with
baseline spending levels well beyond those thresholds, a pattern that is difficult to recon-
cile with threshold-crossing incentives alone. These patterns are consistent with behavioral
mechanisms such as mental accounting (Thaler, 1999), under which consumers may treat
digital coupons as a distinct budget for discretionary consumption. The design features of
digital coupons—minimum spending thresholds and short expiration windows—may further
amplify these responses.
Fourth, we examine which types of businesses benefited most from the stimulus. By
mapping individual treatment effects onto businesses, we find that larger, higher-priced es-
tablishments captured the most additional revenue. We show that this unequal distribution
stems from a key form of consumer-business matching: consumers with higher coupon MPCs
tended to direct a greater share of their spending to large businesses. Consequently, the inci-
dence of the program—in terms of which businesses ultimately benefited—may not align with
policies aimed at supporting small and vulnerable businesses during economic downturns.
Armed with these results, we show that targeting rules can substantially reshape both the
size and distribution of stimulus effects. Digital coupons are typically distributed via lotteries
or first-come-first-served mechanisms, which do not systematically reach the most responsive
consumers and may not align with distributional objectives. Yet, unlike traditional stimulus
instruments, digital coupons can leverage mobile platforms to enable real-time targeting
based on observable characteristics. This creates scope for improving both the efficiency and
distributional consequences of stimulus policy.
We begin by considering the objective of maximizing aggregate stimulus. Leveraging our
estimated individual treatment effects, we show that targeting the most responsive consumers
could more than double the overall stimulus effect at no additional fiscal cost. These efficiency
gains remain substantial even when the government’s targeting capacity is limited to a subset
of observable characteristics.
However, efficiency-maximizing strategies favor larger businesses and wealthier consumers,
potentially undermining objectives to support vulnerable small businesses. We therefore
evaluate an alternative targeting strategy that prioritizes consumers more likely to patronize
smaller establishments—those with lower wealth, weaker consumption habits, and residing
in areas with a higher share of small businesses. We show that doing so effectively shifts rev-
enue gains toward small businesses, but at the cost of lower aggregate stimulus and greater
reliance on lower-wealth consumers’ out-of-pocket spending as the source of finance.
Recognizing these trade-offs, we evaluate a hybrid policy combining digital coupons with
direct small-business support. In this approach, a portion of the government budget is used
to fund targeted coupons to the most responsive consumers, while the remainder is allocated
4

as direct subsidies to small businesses. Applying this approach to the Beijing program,
we find that the hybrid design can deliver 21 percent more total stimulus while providing
substantial direct support to small businesses that received no government assistance under
the original program, addressing both efficiency and equity objectives within existing budget
constraints.
1.1 Related Literature
Our paper relates to several strands of literature. First, we contribute to the extensive
work on consumption responses to fiscal stimulus, which typically estimates the average
marginal propensity to consume (MPC) out of tax rebates or cash transfers. Most studies
of the 2001 and 2008 U.S. stimulus programs report short-run MPCs between 0.25 and 0.5
for nondurables, though recent work using staggered difference-in-differences designs finds
lower estimates around 0.25 for the 2008 payments (e.g., Johnson et al., 2006; Parker et al.,
2013; Broda and Parker, 2014; Borusyak et al., 2024; Orchard et al., 2025).
Our paper is most closely related to the emerging literature on government-issued digital
coupons, a novel form of voucher-based fiscal stimulus. Earlier examples of voucher-based
stimulus include Japan’s 1999 shopping coupon program (Hsieh et al., 2010) and Taiwan’s
2009 voucher initiative (Kan et al., 2017). Unlike traditional physical vouchers, digital
coupons feature minimum spending thresholds and short expiration windows and are dis-
tributed via mobile platforms. Studies of digital coupon programs in Hangzhou, Shaoxing,
and other Chinese cities estimate coupon MPCs between 3 and 6 (Liu et al., 2021; Xing et al.,
2023; Ding et al., 2025), suggesting substantially larger short-run stimulus effects than those
associated with either cash transfers or physical vouchers. 5
We contribute to this literature by moving beyond average effects to uncover substantial
heterogeneity in consumption responses. We analyze both demand- and supply-side drivers
of this heterogeneity, and show how it leads to unequal impacts on local businesses and
shapes the potential for targeting. Methodologically, we depart from traditional interaction-
based approaches to heterogeneity and join a growing literature applying machine learning
methods to estimate heterogeneous treatment effects and inform policy design (e.g., Hino
et al., 2018; Davis and Heller, 2020; Britto et al., 2022; Johnson et al., 2023).
Our paper also speaks to a literature documenting violations of fungibility in consump-
tion, as evidenced by responses to tax refunds, in-kind transfers, gift cards, and online
coupons (Milkman and Beshears, 2009; Reinholtz et al., 2015; Hastings and Shapiro, 2018;
Baugh et al., 2021). Of particular relevance, Boehm et al. (2025) show that prepaid cards
with short expiration windows yield substantially higher short-run MPCs than cash. Our
findings document patterns consistent with consumers treating digital coupons as partly non-
5Compared with the existing literature on digital coupons, our setting is narrower and focuses on food delivery,
a largely non-storable consumption category.
5

fungible windfall budgets, with their consumption responses likely amplified by the salience
of minimum spending thresholds and expiration constraints.
The rest of the paper is organized as follows. Section 2 provides background on the
digital coupon program and describes the data. Section 3 outlines our empirical approach to
estimating treatment effects and capturing heterogeneity. Section 4 presents the main results.
Section 5 examines distributional consequences and counterfactual targeting policies. Section
6 concludes. References to sections, figures, and tables prefixed by OA refer to the Online
Appendix.
2 Background and Data
2.1 Background
During the Covid-19 pandemic, China experienced a sharp decline in household con-
sumption and economic activity. Face-to-face service industries such as restaurants and
accommodations were hit especially hard, as widespread lockdown measures and limited re-
mote operation options severely restricted their business activities. According to the Beijing
Municipal Bureau of Statistics, the value added of the city’s accommodation and catering
industry fell 13.7 percent in 2022.
In response to these economic challenges, local governments across China implemented a
range of fiscal stimulus measures, with digital coupon programs emerging as a key strategy
to directly incentivize consumer spending in targeted sectors. By the end of 2022, more than
285 municipal governments had launched digital coupon initiatives, targeting industries such
as tourism, retail, and food services. These initiatives were enabled by China’s advanced
digital infrastructure, which allowed widespread and cost-effective distribution to millions of
consumers through mobile platforms.
We study a digital coupon initiative implemented in Beijing during the summer of 2022.
In July, the Beijing municipal government launched a restaurant consumption voucher pro-
gram as part of the 2022 Beijing Consumption Initiatives (Beijing Municipal Commission,
2022). On the Ele.me food delivery platform, coupons were distributed daily from July 18 to
August 27, 2022 on a first-come, first-served basis to individuals with IP addresses located
in Beijing. Each day, a limited quota of coupons became available on a dedicated event
page within the Ele.me mobile app, where users could attempt to claim that day’s coupon
bundle. Each eligible individual could claim one bundle of coupons per day, consisting of a
¥15 discount on purchases over¥50 (the “50-15” coupon) and a¥30 discount on purchases
over¥100 (the “100-30” coupon). These coupons expired at midnight on the day of issuance,
giving users a brief window to redeem them after claiming.
This quota-constrained, first-come, first-served distribution mechanism generated a daily
“rush” environment in which users competed to claim coupons before the quota was ex-
6

hausted. Whether an individual who clicked on the event page successfully obtained a
coupon bundle depended on whether their claim attempt occurred before or after the daily
quota was reached. We define the treatment group as individuals who successfully obtained
at least one coupon bundle during the program period, and the control group as those who
participated in the event but never obtained a coupon. To identify the causal impact of
coupon receipt on consumer spending, we employ a matched difference-in-differences frame-
work, as detailed in Section 3.1. We track the expenditures for online delivery orders placed
through the partnering platform, where coupons were automatically applied once the pur-
chase met the required threshold. Consumers could only use one coupon per order, providing
a clean measure of how coupon availability affected purchasing decisions.
2.2 Data
2.2.1 Sampling and Key V ariables
Our main data come from Ele.me (ele.me), a leading food delivery platform in China
and distributor of digital coupons during the Beijing initiative in 2022. As a major player in
China’s food delivery market, the platform holds over 30 percent market share and employs
over four million delivery riders as of 2024 (Ele.me, 2024; Xinhua News, 2025).
We implement a stratified random sampling design to select active individuals—defined
as those who had placed at least one order on the platform within the past six months—from
two strata: individuals who participated in the coupon program and successfully obtained
coupons (treatment group), and those who participated but did not obtain coupons (control
group). Using a 1:1 stratification ratio between these groups and after excluding invalid
accounts, we obtain a sample of 11,765 unique individuals, with 5,980 in the treatment
group and 5,785 in the control group. 6
We obtain complete ordering records for each sampled individual covering a 69-day pe-
riod from July 4 to September 10, 2022. This time frame encompasses the 41-day coupon
program (July 18 to August 27), which we refer to as the treatment period, as well as two
weeks before program implementation (pre-treatment period) and two weeks after program
completion. Each order record provides information on the total order amount and the
number of items—referred to as stock keeping units (SKU)—purchased. The order amount
reflects both the consumer’s out-of-pocket expenditure and any coupon discount subsidized
by the government, which together sum to the total payment received by the merchant.
We also collect detailed individual-level characteristics from Ele.me to account for demo-
graphic profiles and consumption habits relevant to coupon usage and food delivery demand.
6The platform’s privacy policy limited the number of user-level records we could extract, resulting in an analysis
sample that is substantially smaller than the full population of coupon participants. To assess sample representative-
ness, we conducted an external validation using large-scale mobile-app usage data from a major telecommunications
carrier, covering approximately 50 percent of Beijing’s population. We identify Ele.me users in this dataset and
confirm that their demographic composition closely aligns with our sample. See Section OA1.1 for details.
7

These characteristics include age, gender, platform membership status, 7 the geographic co-
ordinates of frequently used delivery addresses, and the price range of their smartphones. 8
To depict individuals’ consumption habits, we also retrieve their average expenditure per
order and the total number of orders placed in the six months prior to the coupon event.
Because the platform does not provide direct measures of individual wealth or neighbor-
hood amenities, we supplement the data with additional location-based information. We
derive housing price levels from over 0.5 million property transaction records between 2010
and 2020, obtained from Lianjia (lianjia.com), the leading property listing platform in China.
We assign a local housing price to each individual’s frequent delivery address by averaging the
prices of the five nearest properties. Since housing prices and smartphone prices are highly
correlated, we construct a first principal component from these two variables to create a
wealth index that captures individuals’ socioeconomic status.
To capture the local opportunities for consumption, we construct a measure of consump-
tion amenities, defined as the number and composition of restaurants in an individual’s
immediate vicinity. A key hypothesis of our paper is that the supply of nearby restau-
rants influences how likely individuals are to redeem digital coupons, as it shapes both the
ease of access and the attractiveness of dining options. To operationalize this measure, we
draw a random sample of 3,000 merchants on Ele.me in Beijing. After excluding grocery
stores and new establishments that opened in 2022, we retain a sample of 2,120 restaurants.9
We classify restaurants as either small and medium-sized enterprises (SMEs) or large busi-
nesses (non-SMEs) based on their median monthly revenue over the six months preceding
the coupon event, using the citywide median as the cutoff. For each individual, we create a
3km circular buffer around their frequent delivery address and compute two variables: (1)
the total number of restaurants within the buffer, and (2) the share of these restaurants that
are classified as large businesses. This 3km buffer corresponds to the typical food delivery
service range,10 allowing us to quantify both the density and the composition of consumption
amenities available to each individual.
2.2.2 Sample Definitions and Descriptive Patterns
We construct our baseline dataset at the individual-day level, aggregating order infor-
mation each day to compute out-of-pocket expenditure (total expenditure minus coupon
subsidies), total expenditure, unsubsidized expenditure (spending on orders without coupon
7Ele.me offers a paid membership program that provides users with benefits such as waived or reduced delivery
fees and exclusive discounts. Users can purchase memberships on a monthly or annual basis.
8Age and phone price are reported in bins rather than exact values. We use the median value of each bin in the
analysis.
9We exclude grocery stores because the coupon program specifically targeted restaurant services. Newly opened
establishments from 2022 are omitted because they lack sufficient pre-program sales history to reliably categorize
them by size.
10Over 90 percent of orders in our data fall within 3km of users’ delivery addresses.
8

Table 1. Descriptive Statistics
Mean SD Mean SD
Treatment Control
Panel A: Individual-day Level
Out-of-pocket expenditure 17.584 44.390 13.989 41.245
Total expenditure 18.148 45.306 13.989 41.245
Unsubsidized expenditure 16.235 43.186 13.989 41.245
Number of orders 0.401 0.701 0.301 0.640
SKU per order 0.996 2.409 0.746 2.218
Observations 208,285 208,285
Treatment Control
Panel B: Individual Level
∆ Out-of-pocket expenditure 1.877 15.185 0.076 15.751
Age 32.250 8.160 32.281 9.047
Female 0.635 0.481 0.657 0.475
Platform membership 0.382 0.486 0.395 0.489
Wealth 0.043 1.032 0.053 1.019
Number of establishments 52.445 33.987 51.284 32.638
Share of non-SME establishments 0.524 0.125 0.526 0.122
Number of orders, past 6 months 55.580 55.728 54.164 56.853
Spending per order, past 6 months 45.236 26.475 44.913 27.685
Observations 3,787 3,787
SME Non-SME
Panel C: Establishment Level
Average monthly sales, past 6 months (thousand) 12.965 11.816 219.903 219.060
Average order price, past 6 months 50.845 45.119 56.552 42.698
Number of establishments (0.5km radius) 7.012 3.973 8.228 4.399
Average local housing price (thousand) 4,562 3,791 4,975 3,921
Observations 1,060 1,060
Notes:This table presents descriptive statistics at the individual-day, individual, and establishment (restaurant)
levels. Panel A reports individual-day variables related to consumer ordering behavior over the pre-treatment
and treatment periods (55 days), where ∆ out-of-pocket expenditure represents consumer spending net of coupon
subsidies, total expenditure captures the full payment to sellers (including coupon subsidies), and unsubsidized
expenditure measures spending on orders that did not use coupons. All expenditure variables are in yuan (¥). Panel
B shows individual-level characteristics. The treatment group includes individuals who obtained at least one coupon
bundle; the control group includes those who participated but did not obtain coupons. References to “past 6 months”
indicate the six-month period immediately preceding the coupon event (January–July 2022). The wealth index is
constructed as the first principal component of smartphone prices and local housing prices, where “local housing
prices” are calculated using the nearest five transaction records for a given location. Number of establishments and
share of non-SME establishments are calculated within a 3km radius of each individual’s frequent delivery address.
Control group statistics in this panel are weighted to account for matching with replacement. Panel C compares
characteristics between SME and non-SME establishments, with SMEs defined as businesses with median monthly
revenue below the citywide median over the six months preceding the coupon program.
redemption), number of orders, and total items (SKU) per order. On days when a consumer
does not make any purchases, these variables are set to zero, ensuring a balanced panel that
captures both active and inactive consumption days.
9

To further improve comparability between the treatment and control groups, we im-
plement a propensity score matching (PSM) procedure. After dropping individuals with
missing values on any key characteristics, we estimate each individual’s likelihood of obtain-
ing coupons based on their observed demographic, wealth, and locational attributes. Each
treated individual is then matched to a control individual with replacement, based on the
estimated propensity scores. This procedure yields a matched sample of 3,787 treated indi-
viduals and 3,787 matched control observations, drawn from 1,389 unique control individuals.
Altogether, our baseline analysis focusing on the pre-treatment and treatment periods (55
days total) comprises 416,570 individual-day observations (3,787 individuals×2 groups×55
days). When including the two weeks after program completion for supplementary analyses,
our sample expands to 522,606 observations across the full 69-day study period. Further
details on the PSM specification and diagnostic checks are provided in Section OA1.2.
Table 1 presents descriptive statistics for our matched sample. Panel A summarizes
individual-day variables related to consumer ordering behavior, including the three expen-
diture measures, the daily average number of orders and the average number of items per
order. For the control group, the three expenditure measures are identical, as they did not
receive any subsidies. On average, the treatment group spent substantially more than the
control group across all three expenditure measures. Treated individuals also placed slightly
more frequent orders and included more items per order.
Panel B of Table 1 presents summary statistics for the individual-level variables used in
our heterogeneity analysis. The data reveal the profile of typical food delivery consumers
in Beijing: predominantly young adults (average age around 32), with slightly more females
than males. Their wealth index values range from -3 to 3, with our sample centered around
the mean (by construction, the index has mean 0 and standard deviation 1). About 39
percent held platform membership status, indicating regular engagement with the delivery
service. On average, consumers placed roughly 55 orders in the six months preceding the
coupon event, spending about¥45 per order. Their neighborhoods contained an average
of 52 restaurants within delivery range, 11 with a relatively balanced mix of SME and non-
SME establishments. These detailed demographic, wealth, and locational attributes allow
us to examine how treatment effects vary systematically across socioeconomic groups and
geographic areas.
Panel C of Table 1 presents establishment-level characteristics by SME status. The
data reveal notable differences between the large and small establishments in our sample.
Large restaurants generated substantially higher sales, with average monthly revenue nearly
17 times greater than that of SMEs. Although they represent 50 percent of restaurants,
large establishments accounted for approximately 94 percent of total revenue. On average,
11The restaurant count is based on a random sample drawn from the universe of establishments listed on the Ele.me
platform. While the absolute number should be interpreted with caution, it provides a valid basis for comparing
restaurant availability between treatment and control groups.
10

they also charged higher order prices (¥56.55 vs.¥50.85) and were located in areas with
greater restaurant density and higher local housing prices. These systematic differences in
establishment characteristics and spatial distribution highlight the importance of accounting
for neighborhood characteristics in studying the impact of the stimulus program.
3 Empirical Strategy
In this section, we present the empirical framework for analyzing the consumption re-
sponses to digital coupons. We begin by outlining our approach to estimating the average
effect of coupon acquisition on spending behavior. We then describe our methods for es-
timating heterogeneous treatment effects and examining the factors that drive variation in
consumption responses.
3.1 Estimating the Average Treatment Effect
We employ a difference-in-differences (DiD) design to identify the average treatment effect
of obtaining digital coupons on consumer spending. Our identification strategy exploits the
first-come, first-served distribution mechanism described in Section 2.1. All individuals in
our sample actively attempted to claim coupons by clicking on the event link, demonstrating
comparable intent to obtain and use digital coupons. Their success depended on whether
the daily coupon quota had been exhausted at the time of their attempt—a factor plausibly
unrelated to unobserved determinants of spending behavior. 12
To mitigate potential selection bias arising from individual differences in timing and effort
intensity, we first implement propensity score matching, as described in Section 2.2.2, and
then conduct our DiD analysis using the matched sample. Matching treated individuals to
control units using the full set of demographic, wealth, and locational characteristics yields
well-balanced covariates and enhances comparability between the two groups. 13 The credi-
bility of this matched DiD design relies on the parallel trends assumption: in the absence of
treatment, treated and control individuals would have followed similar spending trajectories.
In Section 4.1, we present graphical and formal evidence supporting this assumption using
pre-treatment data.
12An ideal design would restrict comparison to users attempting within very narrow time windows around quota
exhaustion, where success is driven primarily by random server load and connection speed. Unfortunately, the
platform records timestamps only for successful coupon claims, not for unsuccessful attempts, making such a design
infeasible.
13To show that our conclusions do not depend on this particular matching design, Table OA.4 also reports results
from three alternatives: the baseline DiD estimated on the full sample without matching; optimal full matching
(Hansen and Klopfer, 2006), which implements matched subclasses with varying treated–control ratios rather than
one-to-one pair matching; and the doubly robust difference-in-differences estimator of Sant’Anna and Zhao (2020),
which combines propensity-score weighting with outcome regression and remains consistent if either the propensity-
score model or the outcome-evolution model is correctly specified. The estimates are quantitatively similar across all
three alternatives.
11

Formally, we estimate the following two-way fixed effects (TWFE) regression applied to
the matched sample at the individual-day level:
yit =α·Treat i ×Post t +γ i +λ t +ϵ it,(1)
wherey it represents the outcome variables (out-of-pocket expenditure in our baseline model)
for individualion datet, Treat i indicates whether individualiever obtained a coupon
bundle during the treatment period, and Post t equals one during the treatment period (July
18 to August 27, 2022) and zero during the pre-treatment period. The coefficientαcaptures
the average treatment effect on the treated (ATT), representing the increase in daily out-
of-pocket spending by coupon recipients during the treatment period relative to the pre-
treatment period, compared to the same temporal difference for the control group. This
baseline specification focuses exclusively on the pre-treatment and treatment periods, with
the two weeks after the coupon event considered separately in subsequent analyses.
We make several implementation choices to ensure a credible estimation of the treatment
effect. First, we define treatment at the period level rather than the daily level: an indi-
vidual is considered treated if they obtained at least one coupon bundle during any day of
the treatment period. This approach avoids endogeneity concerns that would arise if indi-
viduals timed their participation in response to anticipated consumption needs. 14 Second,
our estimate reflects an “intention-to-treat” effect, measuring the impact of obtaining digital
coupons regardless of actual redemption patterns. This distinction is important because not
all distributed coupons were redeemed. This approach avoids the selection bias that would
arise from conditioning on the endogenous redemption decisions. Third, we adopt a binary
treatment definition, classifying individuals as either treated or control rather than model-
ing treatment intensity based on the number of coupons obtained. While this simplification
may understate heterogeneity in exposure, it provides a clean identification of the overall
program effect. Finally, since the “50-15” and “100-30” coupons were always distributed
together as a bundle, their individual effects cannot be separately identified. Our estimates
therefore represent the combined impact of having obtained both coupon types throughout
the program period.
To alleviate remaining endogeneity concerns, we conduct two robustness exercises that
sharply limit the scope for selection. First, individuals differ in the timing of their claim
attempts: users who attempt earlier in the day are more likely to succeed and may also differ
systematically in their consumption behavior from those who attempt later. To address this
concern, we restrict the treatment group to near-cutoff recipients—individuals who obtained
at least one coupon bundle within the final decile of a day’s successful claim timestamps dur-
14In Section OA3.1, we present an alternative specification that defines treatment at the individual-day level—that
is, individuals are considered treated only on days they obtained coupons. This specification does not conform to a
standard DiD framework, as treatment status is time-varying and non-absorbing. We report these day-level estimates
in the appendix for comparison with our benchmark period-level results presented in the main text.
12

ing the program period. 15 These individuals experienced at least one “last-minute” success,
securing coupons by only a small margin close to the quota-exhaustion time, making them
more comparable to the control group and thereby reducing concerns that our estimates are
driven by selection on timing. 16 Second, individuals vary in their effort intensity. Users who
log in frequently or make repeated attempts are more likely to obtain a coupon bundle and
may also differ systematically from casual users in their underlying consumption behavior.
To address this concern, we restrict the treatment group to one-time recipients—individuals
who obtained exactly one coupon bundle during the program period. This restriction me-
chanically excludes persistent, high-engagement users, thereby reducing concerns that our
estimates are driven by selection on effort intensity. Results for both exercises are reported
in Section OA3.2. Re-estimating the matched DiD specification on these restricted treat-
ment groups yields effects similar in magnitude to our benchmark estimates, suggesting that
timing- and effort-based selection are not driving our main findings.
We further decompose the consumption response along extensive and intensive margins
by replacing the dependent variable with measures such as order frequency, expenditure
per order, and dishes (SKUs) per order. This decomposition helps identify whether digital
coupons primarily stimulate more frequent purchases (extensive margin) or larger purchases
per transaction (intensive margin), which has implications for how the program’s benefits
are distributed across businesses of different sizes and price levels.
We also investigate potential substitution patterns that could limit the net stimulus effect
of digital coupons. Using the platform’s transaction data, we test whether increased restau-
rant spending is offset by inter-temporal, inter-category, or intra-household substitution. To
test for inter-temporal substitution, we compare spending patterns during the two weeks
after the coupon event against those in the two weeks preceding it. If consumers simply
shift their planned purchases to coincide with coupon availability and then reduce spending
afterward (e.g., Mian and Sufi, 2012), the net stimulus effect over a longer horizon might be
negligible. Specifically, we modify our baseline specification by replacing treatment period
observations with data from the two weeks after the coupon event, and redefine Post t to
indicate this period instead of the treatment period. The coefficient on Treat i ×Post t then
captures the difference in individual daily out-of-pocket expenditure between treatment and
control groups during the two weeks after the coupon event relative to the pre-treatment
period. This exercise also examines a closely related question: do digital coupons generate
sustained increases in consumption that persist after the treatment period ends? Persis-
tent consumption increases would suggest ourαestimate in equation (1) underestimates the
15One could further restrict the treatment group to users whose entire set of acquired coupons were obtained
within the final decile of each day’s successful claims. However, such a definition yields too few treated individuals
for reliable estimation, so we adopt the broader near-cutoff criterion.
16We observe timestamps only for successfully obtained coupons but not for unsuccessful claim attempts. As a re-
sult, we cannot isolate control-group individuals who narrowly missed the quota. This prevents us from implementing
a formal regression-discontinuity design or a difference-in-differences design centered on daily quota exhaustion.
13

total impact, while decreased spending would confirm inter-temporal substitution. For inter-
category and intra-household substitution, we replacey it in equation (1) with expenditure
on grocery orders and with the number of tableware sets requested per order, respectively.
Finally, we examine off-platform substitution, which the platform’s transaction data can-
not directly capture. Consumers may shift orders from rival delivery platforms to Ele.me
(cross-platform substitution) or replace in-person dining with delivery orders (offline-to-
online substitution). Since both forms of off-platform substitution would likely appear on
Ele.me primarily through additional orders rather than higher spending per existing order,
we turn to external data to assess this possibility. Specifically, we use the mobile application
usage data introduced in Section 2.2.1 and compare food-delivery app usage during, and
after the coupon event to test whether treated consumers shifted spending from rival plat-
forms to Ele.me during the coupon period. Taken together, these exercises assess whether
the estimated consumption response reflects genuine additional spending or redistribution
across time, categories, platforms, dining formats, or household members.
3.2 Estimating Heterogeneous Treatment Effects
While the average effect estimates provide a measure of the overall effectiveness of the
stimulus program, they mask substantial heterogeneity in individual consumption responses.
Understanding this heterogeneity is crucial for identifying the micro-drivers of spending be-
havior, assessing the distributional impact of the program, and designing optimal strate-
gies to support different policy objectives. Furthermore, since individuals live in different
locations and shop at different places, heterogeneity in individual consumption responses
translates into heterogeneous impact on local businesses. Consequently, theincidenceof the
stimulus program, in terms of which businesses it ultimately benefits, depends fundamentally
on consumer heterogeneity.
To analyze how consumption responses vary across individuals, we estimate a hetero-
geneous treatment effects model. Specifically, let ∆y i denote the change in individuali’s
average out-of-pocket spending, calculated as the difference between their average spend-
ing during the treatment period and the pre-treatment period. Let Treat i be an indicator
for whether individualibelongs to the treatment group. We estimate the following first-
difference DiD regression:
∆yi =α(X i)·Treat i +f(X i) +ε i,(2)
whereX i includes our full set of observed demographic, wealth, and locational attributes
(see Table 1, Panel B), andα(.) andf(.) are allowed to be any functions. In Section 4.1,
we show that the impact of digital coupons was concentrated within the treatment period
and did not extend beyond the program’s duration. Accordingly, we focus on analyzing
14

heterogeneity in spending responses during this period.
Since Treati is binary, equation (2) constitutes a complete nonparametric specification. 17
α(Xi) captures the heterogeneous treatment effects of interest. More precisely, it represents
the conditional average treatment effect on the treated (CATT) for each individual, given
their observed characteristics. In causal inference terminology, the variablesX i are potential
moderatorsoreffect modifiersthat predict variation in treatment effects. By modeling the
treatment effect as a nonparametric function ofX i, we allow for complex patterns to emerge
on how different factors jointly shape variation in spending responses.
To estimateα(X i), we partial out the influence off(X i) by estimating the following
residual-on-residual regression:
∆yi −E[ ∆y i|X i] =α(X i)·(Treat i −E[ Treat i|X i]) +ξ i,(3)
where the nuisance functionsE[ ∆y i|X i] andE[ Treat i|X i] are estimated using machine
learning estimators. 18 This procedure follows the double machine learning (DML) frame-
work of Chernozhukov et al. (2018). 19 The associated moment condition satisfies Neyman
orthogonality, which guarantees that the estimation ofα(X i) will be robust to first-order
errors in nuisance function estimation.
We estimate equation (3) using the causal forest estimator (Wager and Athey, 2018;
Athey et al., 2019), a tree-based machine learning method designed for heterogeneous treat-
ment effect estimation.20 The causal forest constructs an ensemble of causal trees, where each
tree recursively partitions the covariate space to maximize variation in estimated treatment
effects, thereby identifying subgroups with distinct responses to the treatment. The method
employs the “honest” approach (Athey and Imbens, 2016), which uses sample-splitting to
avoid overfitting and ensure valid inference. By averaging across many such trees, the causal
forest produces a nonparametric estimate of the conditional average treatment effect func-
tion.21 This nonparametric approach offers a systematic way to explore treatment hetero-
17Compared to the average effect model (1), model (2) additionally controls for potential differential trends byX i,
as well as any correlation between treatment status and treatment effect that could arise from residual imbalances in
Xi. In Section 4.3, we compare the average treatment effect derived from this heterogeneous effects model to that
estimated from the average effect model.
18We implement the residual-on-residual orthogonalization procedure and estimate the causal forest model using
thegrfpackage inR(Tibshirani et al., 2024). Thegrfpackage allows users to supply pre-estimated nuisance
functions, which it uses to perform orthogonalization prior to fitting the causal forest. We estimate these nuisance
functions using both the default random forest learners ingrfand the Super Learner ensemble method (Laan et al.,
2007). Following Chernozhukov et al. (2018), we apply cross-fitting to reduce overfitting and ensure that Neyman
orthogonality holds asymptotically. Additional implementation details are provided in Section OA5.1.
19Through orthogonalization, this procedure avoids the need to estimatef(X i), whose errors may contaminate the
estimation ofα(X i). Alternatively, we can estimate the regression model (2) directly, which involves learning both
α(Xi) andf(X i) jointly. In Section OA5.2, we implement this direct strategy using alternative machine learning
estimators and compare their performance with our benchmark results based on orthogonalization.
20Section OA5.1 provides details on the implementation, including hyperparameter settings governing forest size,
splitting rules, and sample-splitting fractions.
21The causal forest can be interpreted as a locally weighted estimator, with weights determined by the proportion
15

geneity across a rich set of causal effect moderators, while capturing potentially complex and
high-order interactions among them. 22
3.3 Characterizing Determinants of Treatment Effects
The estimated heterogeneous treatment effects function allows us to analyze how different
factors contribute to variation in consumer responses. A common approach in applied work
is to estimate linear interaction models, in which each potential causal effect moderator is
interacted with the treatment indicator one at a time. However, this strategy has two im-
portant limitations. First, when moderators are correlated with one another, the estimated
coefficients may be confounded by omitted variables that are correlated with the interaction
term. For instance, both individual wealth and local consumption amenities may influence
the consumption response to digital coupons, and these two factors are often correlated due
to spatial sorting. In single-interaction models, a positive association between wealth and
the treatment effect might therefore reflect either wealth’s direct influence—a demand-side
effect—or the influence of local consumption amenities—a supply-side effect. This makes
the estimated coefficient difficult to interpret and obscures the underlying mechanism. Sec-
ond, the linear interaction approach is limited to detecting linear relationships between each
moderator and the treatment effect. As a result, it may miss important nonlinear or non-
monotonic patterns in treatment effect heterogeneity.
By nonparametrically estimating treatment effects as a function of the full set of observed
demographic, wealth, and locational attributes, we can examine the influence of each factor
conditional on the others. This multivariate approach mitigates the confounding concerns
that arise in single-interaction models and brings our analysis closer to a “treatment effect
on treatment effect” framework—that is, assessing how individual characteristics shape the
direction and magnitude of the treatment’s impact. In this section, we pursue two com-
plementary strategies. First, we use a best linear projection to estimate the conditional
linear relationship between each variable and the treatment effect, holding other character-
istics constant. Second, we employ accumulated local effects curves to uncover potentially
nonlinear or nonmonotonic patterns in how individual factors contribute to treatment effect
heterogeneity.
3.3.1 Best Linear Projection
A simple approach to assess how individual characteristics relate to treatment effect het-
erogeneity is to regress the estimated treatment effect functionbα(Xi) on observed covariates.
of trees in which an observation shares a leaf with the target point. These weights define an adaptive kernel that
places greater mass on regions of the covariate space where treatment effect heterogeneity is most pronounced, unlike
classical nearest-neighbor or kernel methods, which apply fixed bandwidths regardless of underlying heterogeneity.
22For examples of empirical research applying the causal forest method, see Davis and Heller (2017), Britto et al.
(2022), and Johnson et al. (2023).
16

However, although causal forests yield pointwise consistent estimates ofα(X i), directly re-
gressing these estimates can lead to biased summaries due to estimation errors that do not
cancel out (Athey and Wager, 2019). 23 Therefore, following Semenova and Chernozhukov
(2020), we construct a doubly robust score that corrects for this bias and enables consistent
estimation of the best linear approximation to the treatment effect function, also known as
the best linear projection (BLP). Specifically, define
ψi =bα(Xi) + Treati − bE[ Treati|X i] bE[ Treati|X i]  1− bE[ Treati|X i]  ·bεi,
wherebεi = ∆yi − bE[ ∆yi|Treat i,X i] = ∆yi − bE[ ∆yi|X i]−

Treati − bE[ Treati|X i]

·bα(Xi),
and bE[ ∆yi|X i] and bE[ Treati|X i] are the estimated nuisance functions from (3). We then
estimate:
ψi =β· eXi +e i,(4)
where eXi are standardized to have mean zero and unit variance. This approach provides
valid standard errors for inference on each coefficientβ k. The standardization allows direct
comparison across coefficients as measures of variable importance. In the absence of unob-
served moderators correlated with eXik, the coefficientβ k can be interpreted as the causal
effect of eXik on the treatment effect of digital coupons, allowing us to identify the key drivers
of treatment effect heterogeneity.
3.3.2 Accumulated Local Effect Curves
While the best linear projection captures linear relationships between treatment effects
and observed moderators, it may miss important nonlinear or nonmonotonic patterns. To
examine these more complex relationships, we construct accumulated local effects (ALE)
curves (Apley and Zhu, 2020), which visualize how each moderator influences the estimated
treatment effect while accounting for the joint distribution of the covariates.
Specifically, letδ k (x) =E[∂α(X i)/∂X ik|X ik =x] denote the conditional average partial
derivative of the treatment effect function with respect toX ik. The ALE curve forX ik is de-
fined as the cumulative integralh k (x) =
R x
x δk (t)dt, wherex is the minimum observed value
ofX ik.24 Intuitively, the ALE curve traces how the treatment effect changes asX ik varies,
averaging the marginal effect over the conditional distribution of the remaining moderators
at each value ofX ik.
23Due to regularization, machine learning estimators like causal forests can produce finite-sample biases that are
correlated with covariates. In particular, the estimates tend to shrink toward the global mean in regions of the
covariate space with sparse support or high variability.
24The curve is then centered as ehk (x) =h k (x)−E[h k (x)], so that its average over the empirical distribution of
Xik is zero.
17

ALE curves are particularly useful when covariates are correlated. Unlike partial depen-
dence plots, which average marginal effects over the entire covariate space (Friedman, 2001),
ALE curves average partial derivatives∂α(X i)/∂X ik only for observations whereX ik =x
is observed. This local averaging prevents extrapolation into unsupported regions, which
can distort inference in the presence of correlated covariates. For example, ALE curves for
neighborhood consumption amenities account for spatial sorting between individuals and
locations by averaging over wealth levels that are empirically observed within each neigh-
borhood, rather than evaluating all possible—and potentially unrealistic—combinations of
wealth and neighborhood characteristics.
In practice, we estimate the ALE curves using the doubly robust scoresψ i introduced in
Section 3.3.1, mirroring the bias-correction approach used in the BLP. 25 This yields a non-
parametric visualization of how each moderator influences the treatment effect. Under the
assumption that unobserved moderators are uncorrelated withX ik, the derivativeδ k (x)—
and hence the slope of the ALE curve—can be interpreted as the local average treatment
effect (LATE) ofX ik on the treatment effect of digital coupons for individuals withX ik =x.
We now turn to the empirical results.
4 Results
4.1 Average Impact of Digital Coupons on Spending
Table 2 presents the estimated average treatment effects of coupon receipt following
Equation (1). We focus on three key outcomes: out-of-pocket expenditure, total expenditure,
and unsubsidized expenditure. Examining these outcomes provides a comprehensive view of
how coupon receipt influences both consumer spending and whether coupon-induced changes
spill over to non-discounted transactions.
On average, obtaining coupons raised consumer daily out-of-pocket expenditure by¥1.80—
a roughly 12 percent increase relative to the average daily unsubsidized expenditure of¥15.04
during the treatment period. Total spending rose even more, reflecting the additional gov-
ernment subsidy. Meanwhile, expenditure on unsubsidized orders showed no statistically
significant change, suggesting that the treatment effects of digital coupons do not spill over
to non-discounted transactions.
We next examine whether the estimated effects are supported by the parallel trends
assumption. Figure 1 illustrates the group-level time trends for the treatment and control
groups. Prior to the coupon event, the two groups followed parallel trends, supported by
an F-statistic of 0.31. During the treatment period, the treatment group’s out-of-pocket
expenditure outpaced that of the control group, with the gap largest in the first weeks of
25Specifically, we nonparametrically estimate the conditional expectation functionE[ψ i|Xi] and compute ALE
curves based on the estimated surface. See Section OA5.3 for further details.
18

Table 2. Average Treatment Effects of Digital Coupons on Different Types of Expenditure
Out-of-pocket expenditure Total expenditure Unsubsidized expenditure
(1) (2) (3)
Treat×Post 1.801*** 2.558*** -0.008
(0.636) (0.639) (0.635)
Observations 416,570 416,570 416,570
Notes:This table presents the average treatment effects of obtaining coupons on daily expenditure among treated
individuals, estimated using Equation 1 with individual and date fixed effects. Out-of-pocket expenditure represents
total expenditure minus government-financed coupon subsidies, total expenditure captures the full payment to sellers
(including coupon subsidies), and unsubsidized expenditure measures spending on orders that did not use coupons.
We exclude the post-program period when estimating the effects, resulting in 416,570 observations (3,787 individuals
×2 groups×55 days). Standard errors are clustered at the individual level. *, **, and *** indicate statistical
significance at the 10%, 5%, and 1% levels, respectively.
the program and tapering visibly during the latter half. After the program ended, the two
groups converged fully. The figure also shows that the control group consumed slightly more
than the treatment group during the two weeks after the coupon event, though this visual
pattern requires formal statistical testing, which we conduct in the following analysis.
Our estimated effect translates into a spending multiplier of 3.38. 26 While this cannot be
given a conventional MPC interpretation—since coupons do not directly increase recipients’
income—we follow Ding et al. (2025) and refer to this multiplier as the “coupon MPC”, the
marginal propensity to consume out of coupon subsidies. In other words, for every yuan
of government expenditure on coupons, consumers increased their total spending by more
than triple that amount. Such a pronounced response aligns with recent studies (Liu et al.,
2021; Xing et al., 2023; Ding et al., 2025) documenting similar magnitudes of coupon MPCs.
This result exemplifies the distinctive joint-financing feature of digital coupon programs:
unlike conventional stimulus payments where consumers are net recipients of government
funds, digital coupons generate earnings for local businesses by amplifying government ex-
penditure through consumer contributions, effectively creating a public-private partnership
in supporting local businesses.
To understand the primary channels driving this increase in spending, Figure 2 decom-
poses the coupon-induced out-of-pocket expenditure effect. Panel A shows that while the
effect of obtaining coupons on order frequency is statistically significant, its magnitude is
near zero, indicating minimal extensive margin effects. Moreover, we observe a significant
26We define the spending multiplier as the ratio of the increase in total expenditure (out-of-pocket expenditure plus
coupon subsidies) to the government subsidy. The estimated daily increase in out-of-pocket expenditure is¥1.80 per
treated individual. The corresponding government subsidy, defined as the daily average coupon discount redeemed
per treated individual (see Section OA6.1), is¥0.76. Total expenditure therefore increased by¥2.56 per treated
individual per day, implying a spending multiplier of 2.56/0.76≈3.38. See Section OA2 for the accounting identities
linking coupon MPC to out-of-pocket spending changes.
19

Figure 1. Event Study of Coupon Effects on Out-of-Pocket Expenditure
Notes:This figure shows daily average out-of-pocket expenditure for treatment and control groups. The treatment
period spans from July 18 to August 27, 2022. Gray shaded areas indicate the two weeks prior to and after the
coupon program. The pre-treatment period exhibits parallel trends (F-statistic = 0.31). The treatment-control gap
is largest in the first weeks of the program and narrows during the latter half, with full convergence after the coupon
event ends.
increase in out-of-pocket expenditure per order alongside an increase in dishes per order,
suggesting that discount thresholds motivate some consumers to bundle additional items to
qualify for the discounts. This response to minimum spending thresholds is further evidenced
by clear “bunching” behavior in the distribution of order amounts. Figure OA.1 presents
histograms of order frequencies by amount, contrasting distributions across different day
types. Redemption days—defined at the individual-day level as days during the treatment
period when consumers placed at least one order using a coupon—show substantial cluster-
ing of orders just above the¥50 and¥100 discount thresholds. No such clustering appears
on non-redemption days.
Panel B of Figure 2 examines the potential substitution patterns discussed in Section
3.1. We find minimal evidence of inter-temporal substitution, consistent with the perishable
nature of delivered meals that limits consumers’ ability to shift consumption across time pe-
riods. This result also aligns with the visual pattern in Figure 1, where the treatment-control
gap converges once the treatment period ends, indicating that digital coupons generate im-
mediate but temporary consumption responses.
We also detect no evidence of inter-category substitution within the platform. Replacing
the outcome variable with out-of-pocket expenditure on grocery orders yields an estimated
effect that is essentially zero, indicating that the increase in restaurant expenditure does not
come at the expense of other food-related purchases on Ele.me. Panel B further shows that
20

Figure 2. Treatment Effect Decomposition and Substitution Patterns
Notes:This figure presents average treatment effects of digital coupons on alternative dependent variables. Panel
A decomposes the consumption response along extensive and intensive margins, showing effects on order frequency,
out-of-pocket (OOP) expenditure per order, and dishes (SKUs) per order. Panel B examines potential substitution
effects. The benchmark OOP shows the baseline average treatment effect on daily OOP expenditure. Post-treatment
OOP tests for inter-temporal substitution by comparing spending in the two weeks after the coupon event to the pre-
treatment period. Restaurant OOP and grocery OOP show effects on restaurant and grocery spending, respectively,
with the latter testing for inter-category substitution. Tableware sets per order proxies for the number of diners and
tests for intra-household or workplace sharing. Dots represent point estimates with 95 percent confidence intervals,
clustering standard errors at the individual level. See Table OA.5 for the full set of estimates and standard errors.
the number of tableware sets requested per order is statistically significant but economically
negligible in magnitude, pointing to no meaningful intra-household or workplace sharing to
meet the spending thresholds.
Turning to off-platform substitution, the near-zero extensive-margin effect in Panel A
makes substantial reallocation across platforms or dining formats unlikely, since both cross-
platform switching and offline-to-online substitution would primarily manifest through ad-
ditional orders (Section 3.1). The mobile application usage data are consistent with this
interpretation: Ele.me’s share of total food-delivery app usage time in Beijing remained sta-
ble across the coupon month and subsequent comparison months, with no temporary increase
during the event, implying little reallocation of app usage from rival platforms to Ele.me. 27
27Section OA3.5 presents details of this exercise. Because coupon recipients constitute a nontrivial share of Ele.me
users during the coupon month, any substantial coupon-induced shift of activity onto Ele.me should generate a
detectable increase in Ele.me’s share of total food-delivery app usage time relative to the non-coupon comparison
months.
21

(a) Conditional Average Treatment Effects
 (b) Conditional Coupon MPCs
Figure 3. Heterogeneity in Individual Responses to Digital Coupons
Notes:Panel (a) displays the distribution of estimated conditional average treatment effects (CATTs) on daily
out-of-pocket spending among treated individuals. The red vertical line indicates the average treatment effect on
the treated (ATT), obtained from the average effects model (1). Panel (b) shows the distribution of conditional
marginal propensities to consume out of coupon subsidies (coupon MPCs), calculated as the ratio of each individual’s
estimated increase in total spending to the expected coupon subsidy they redeem. The red vertical line marks the
benchmark coupon MPC, constructed using the ATT and the average coupon subsidy redeemed across treated
individuals.
Taken together, these results indicate that the estimated consumption response reflects gen-
uine additional spending rather than redistribution across time, categories, platforms, dining
formats, or household members.
Our analysis reveals several key features of digital coupon effectiveness. The program
successfully increased consumer expenditure primarily through the intensive margin, rais-
ing spending per order rather than order frequency. Consistent with Liu et al. (2021), the
consumption boost in the Beijing initiative is short-lived. This temporary nature, combined
with threshold-induced bunching, suggests that the design features—minimum spending re-
quirements and short expiration periods—are important to its effectiveness. However, the
program’s impact varies substantially across merchants. Figure OA.2 further reveals that
coupon redemptions disproportionately occur at establishments that had higher sales rev-
enue and higher average order prices in the six months prior to the coupon event. This
concentration of redemptions at larger, higher-priced establishments reflects the distribution
of consumer spending patterns when using coupons, potentially amplifying revenue gains for
these businesses. These patterns suggest complex interactions between consumer character-
istics and business attributes that we investigate in the following sections.
4.2 Heterogeneous Consumption Responses
The average effects presented in the previous section mask substantial variation in indi-
vidual responses to the program. Figure 3a plots the distribution of estimated heterogeneous
22

Figure 4. Spatial Distribution of Treatment Effects
Notes:This figure plots neighborhood-level average treatment effects against two neighborhood characteristics.
Each point represents a neighborhood, defined as a 3km×3km grid cell. For each grid, the neighborhood-level
average treatment effect is defined as the mean estimated treatment effect on daily out-of-pocket spending among
treated individuals residing in that grid. In panel (a), the horizontal axis reports neighborhood average wealth,
measured as the mean wealth of treated individuals residing in the grid. In panel (b), it reports the total number
of establishments located in the grid. The red line in each panel shows the fitted linear relationship.
treatment effects on daily out-of-pocket spending. While the average effect is¥1.80 accord-
ing to the average effect model (marked by the vertical line), the standard deviation of
the estimated individual treatment effects is¥4.42, revealing wide dispersion in consumer
responses. Approximately 13 percent of individuals exhibited responses at least twice as
large as the average, while 9 percent of individuals accounted for nearly half of the total
aggregate effect—indicating that a small group of high spenders drove most of the increased
revenue for local businesses. On the other hand, 19 percent of consumers reduced their out-
of-pocket spending after receiving digital coupons. For these individuals, coupon redemption
translated into net savings.
We can compute conditional coupon MPCs for each individual using their estimated treat-
ment effect on out-of-pocket expenditure combined with their expected government subsidy.28
These individual-level coupon MPCs measure how much additional total spending could be
generated per yuan of government subsidy if coupons were allocated to individuals with spe-
cific characteristics. Figure 3b presents the resulting distribution. As with treatment effects,
the estimated MPCs show considerable heterogeneity: more than 23 percent of individuals
had MPCs exceeding 5, while the 19 percent of individuals who reduced their out-of-pocket
28The expected subsidy reflects variation in both the number of coupon bundles obtained and the probability
of redemption across treated individuals. We estimate it using a nonparametric regression of realized subsidies on
individual attributes. For details, see Section OA6.1.
23

Figure 5. Best Linear Projection of Heterogeneous Treatment Effects
Notes:This figure plots the estimated coefficients from the best linear projection (BLP) of individual treatment
effects on standardized covariates. All continuous covariates are standardized to have a mean of zero and unit
variance, allowing for direct comparison across coefficients as measures of variable importance. The dots represent
point estimates; horizontal lines denote 95 percent confidence intervals. See Table OA.6 for the full set of estimates
and standard errors.
spending after receiving digital coupons had MPCs below 1. These patterns suggest that
governments could significantly boost the stimulus effects of digital coupon programs through
targeted distribution. In Section 5, we explore targeting rules designed to maximize different
policy objectives, including total spending and support for small businesses.
The response to the digital coupon program also exhibited significant spatial variation
across neighborhoods. Figure OA.7 maps average per-consumer treatment effects across Bei-
jing’s neighborhoods, defined as 3km-by-3km grids. The results show pronounced geographic
disparities in program impact. Ranking neighborhoods by their total contribution to aggre-
gate consumer spending, we find that just 11 percent of neighborhoods accounted for half
of the total citywide increase in spending. Figure 4 explores how these neighborhood-level
effects relate to local characteristics. On average, wealthier neighborhoods with a higher
density of restaurants experienced larger average treatment effects. These findings highlight
heterogeneity in stimulus effects at both the individual and spatial levels. In the next sec-
tion, we examine the underlying drivers of this heterogeneity, focusing on both demand- and
supply-side mechanisms.
24

(a) Wealth
 (b) Order Frequency
 (c) Spending per Order
Figure 6. Accumulated Local Effects of Demand-Side Factors on Consumption Response
Notes:This figure displays accumulated local effects (ALE) curves for wealth, order frequency (total number of
orders placed in the six months prior to the coupon event), and average spending per order (average out-of-pocket
expenditure per order over the same period). The horizontal axis represents empirical quantiles of each variable,
and the vertical axis shows the variable’s marginal influence on the estimated treatment effect, averaging over the
observed distribution of the remaining covariates. Dots denote the estimated ALE values, and the solid line is a
spline-smoothed fit. All curves are centered to have mean zero.
4.3 Drivers of Treatment Effect Heterogeneity
Figure 5 displays the estimated coefficients from the best linear projection (BLP) regres-
sion (4), along with standard errors. 29 All potential moderators, except age, are statistically
significant predictors of treatment effect heterogeneity. In particular, individuals with higher
wealth (as proxied by our wealth index), greater consumption habits (measured by order
frequency and average spending per order over the prior six months), and those living in
neighborhoods with a larger share of non-SME establishments exhibited larger consumption
responses, while being female, having platform membership, and living in areas with more
total establishments were associated with smaller treatment effects, holding other factors
constant.30
Among the identified drivers of consumption responses, wealth, platform membership,
and consumption habits can be considered demand-side factors, reflecting an individual’s
willingness and capacity to spend after receiving digital coupons, 31 while the availability of
consumption amenities—captured by the number of establishments and the share of non-
29Table OA.6 reports the full set of coefficient estimates and standard errors in tabular form. The intercept in the
regression is 1.96 and represents the average of the bias-corrected individual treatment effects, i.e., the ATT implied
by the heterogeneous effects model.
30Since the covariates in the best linear projection are standardized, the coefficients in Figure 5 directly measure
variable importance. An alternative measure is the frequency and magnitude with which each covariate contributes
to splitting across trees in causal forest estimation (Athey and Wager, 2019). Using this metric, the most important
predictors of treatment effect heterogeneity are consumption habits, wealth, and neighborhood consumption amenities
(see Figure OA.5). This aligns with the findings from Figure 5.
31We classify consumption habits as demand-side factors in this section because they primarily reflect an indi-
vidual’s baseline propensity to consume on the platform. However, since consumption habits may also partly reflect
local consumption opportunities, the Shapley decomposition reported later considers alternative allocations of these
variables between demand- and supply-side factors.
25

(a) Number of Establishments
 (b) Share of Non-SME Establishments
Figure 7. Accumulated Local Effects of Supply-Side Factors on Consumption Response
Notes:This figure displays accumulated local effects (ALE) curves for the number of establishments and the share of
non-SME establishments in an individual’s neighborhood. The horizontal axis represents empirical quantiles of each
variable, and the vertical axis shows the variable’s marginal influence on the estimated treatment effect, averaging
over the observed distribution of the remaining covariates. Dots denote the estimated ALE values, and the solid
line is a spline-smoothed fit. All curves are centered to have mean zero.
SME establishments in the neighborhood—represents supply-side factors that determine the
local consumption opportunity set. A central insight of our analysis is that the consump-
tion response to digital coupons—as well as to traditional forms of fiscal stimulus such as
cash payments and tax rebates—is jointly shaped by both demand- and supply-side factors.
These factors are often correlated, as wealthy individuals tend to reside in neighborhoods
with greater consumption amenities, making it difficult to disentangle their respective con-
tributions. While the literature on tax rebates has consistently identified income or wealth
as key determinants of consumption responses (Shapiro and Slemrod, 2003; Johnson et al.,
2006; Sahm et al., 2010; Parker et al., 2013),32 it remains unclear whether these effects partly
stem from spatial sorting into neighborhoods with unequal access to consumption amenities.
In this paper, through nonparametric estimation of treatment effects based on all ob-
served demand- and supply-side factors, we can disentangle their influences by examining
how each factor is related to treatment effect heterogeneity while controlling for the others.
For example, the wealth coefficient of 0.59 implies that, conditional on all other observed
factors—including local consumption amenities—a one-unit increase in the wealth index is
associated with a¥0.59 increase in the treatment effect of digital coupons. While the BLP
32The empirical literature evaluating the MPC out of cash-based fiscal stimulus programs has consistently identified
wealth and income as key predictors of consumption responses, but presents mixed findings regarding the direction
of the relationship. Sahm et al. (2010) and Shapiro and Slemrod (2003, 2009) find that MPC increases with wealth
or income, while Johnson et al. (2006) and Parker et al. (2013) report a negative association. Theoretical models of
consumption responses to unanticipated income shocks emphasize the role of liquidity constraints: individuals with
limited liquid assets—regardless of total wealth—may exhibit hand-to-mouth behavior and respond more strongly to
fiscal transfers (Kaplan and Violante, 2014). Recent evidence from Boehm et al. (2025), however, based on randomized
experiments designed to mimic realistic cash transfers, suggests that liquid wealth may play only a limited role in
explaining variation in consumption responses.
26

captures the linear influence of each factor, we next examine their potential nonlinear and
nonmonotonic effects using ALE curves.
Figure 6 presents the ALE curves for wealth, order frequency, and average spending
per order. Each curve illustrates how the estimated treatment effect varies with the cor-
responding variable, averaging over the conditional distribution of other covariates. To aid
interpretation, the horizontal axis in each plot is scaled to the empirical quantiles of the
variable, and each curve is centered to have mean zero. As the figure shows, the effects of
consumption habit variables—order frequency and average spending per order—are concen-
trated among individuals in the top deciles of the distribution. This nonlinearity qualifies the
average effects reported in Figure 5, suggesting that the positive association between con-
sumption habits and treatment effects is largely driven by a relatively small group of heavy
users. On the other hand, wealth emerges as a consistently strong predictor of consumption
responses: the ALE curve for wealth rises steadily across the distribution. On average, a
10 percent increase in the wealth index corresponds to an additional¥0.45 in daily out-
of-pocket expenditure. Importantly, the ALE curve accounts for the correlation between
individual wealth and neighborhood consumption amenities by showing how a marginal in-
crease in wealth influences an individual’s consumption response within the context of the
neighborhoods where individuals of similar wealth reside.
Turning to the supply side, Figure 7 presents the ALE curves for local consumption
amenities—the number of establishments and the share of non-SME establishments in the
neighborhood. Two conclusions emerge from these plots. First, while Figure 4 shows that
neighborhoods with more restaurants tend to exhibit larger average treatment effects, Fig-
ure 7 reveals a non-monotonic relationship once other factors are controlled for: treatment
effects initially rise with establishment density up to the 25th percentile of the distribu-
tion, and decline thereafter. This pattern suggests that digital coupons generate the largest
consumption response in neighborhoods with a moderate number of establishments, all else
equal. On average, as shown in Figure 5, establishment density is negatively associated with
treatment effects, indicating diminishing returns to consumption amenities in already dense
areas.33 Second, conditional on the number of establishments in a neighborhood, a higher
share of non-SME establishments leads to larger treatment effects. Much like the patterns
observed for consumption habits, these effects are concentrated in neighborhoods with the
highest proportion of large businesses. As shown in Section 4.1, consumers are more likely to
redeem their coupons at larger, higher-priced restaurants. The high concentration of large
establishments thus facilitates greater consumption through digital coupons, which helps ex-
plain the patterns observed in the ALE plot. Together, these findings demonstrate how both
the quantity and composition of neighborhood consumption amenities influence individual
33This pattern is also consistent with consumers in restaurant-dense areas having stronger offline dining alterna-
tives.
27

responses to digital coupon programs.
We can quantify the relative importance of demand-side and supply-side factors using
a Shapley-based variance decomposition of the estimated treatment effects. Section OA5.6
provides the details. Because consumption habits may partly reflect local consumption
opportunities and thus the interplay of both demand and supply forces, we first consider
the demand side to include only wealth and platform membership. Under this comparison,
the relative contribution of the demand side is 58 percent, while that of the supply side
is 42 percent. 34 Alternatively, we allocate the contribution of consumption habits equally
between the demand and supply sides. Under this comparison, the demand side accounts for
52 percent of the explained variation, while the supply side accounts for 48 percent. Taken
together, these results show that demand- and supply-side factors contribute in broadly
comparable magnitudes to shaping the consumption response to digital coupons, with the
demand side playing a modestly larger role.
4.4 Implications for Models of Consumption Behavior
We now discuss the implications of our findings for models of consumption behavior. Xing
et al. (2023) and Ding et al. (2025) develop rational choice frameworks to explain consump-
tion responses to coupons with minimum spending thresholds. In these models, consumer
responses depend on their optimal spending absent the coupon. Marginal consumers, whose
baseline spending lies just below the threshold, increase their spending to qualify for redemp-
tion, while inframarginal consumers, whose baseline spending already exceeds the threshold,
treat the coupon subsidy as cash equivalent and respond only through the income effect of
the discount. Both models therefore predict bunching at the threshold, with coupon-induced
spending arising from threshold-driven reallocation.
Our empirical results provide partial support for this threshold-induced rational optimiza-
tion mechanism. We observe clear bunching at coupon thresholds (Figure OA.1), consistent
with marginal consumers adjusting spending to qualify for redemption. At the same time, we
also document substantial spending responses among consumers whose baseline spending per
order exceeds one or both coupon thresholds and who are therefore likely to be inframarginal
with respect to at least part of the coupon bundle. As shown in Figure 6c, treatment effects
rise smoothly and sharply in the upper tail of the baseline spending-per-order distribution. 35
Under a simple threshold-crossing account, spending responses would be expected to be con-
centrated in relatively narrow regions around the relevant coupon thresholds, rather than
increasing smoothly throughout the upper tail of the spending distribution. In particular,
34The reported shares are normalized to sum to one to reflect their relative contributions.
35Figure OA.6 overlays the¥50 and¥100 thresholds on the same ALE curve and shows that treatment effects
begin to rise around the¥50 threshold and continue increasing further above¥100. Table OA.7 reports corresponding
subgroup DiD estimates for three baseline spending-per-order groups—below¥50,¥50–100, and above¥100—
providing a simple grouped summary that complements the nonparametric evidence in Figure OA.6.
28

one would expect relatively small responses both among consumers whose baseline spending
lies well below the thresholds and among those whose baseline spending already exceeds
them. The pattern we observe is therefore difficult to reconcile with the rational threshold
models alone. It is also not readily explained by consumers simply placing additional or-
ders to use the second coupon in the bundle. As shown in Section 4.1, the treatment effect
operates primarily through the intensive margin, with economically small effects on order
frequency.36
These patterns motivate consideration of complementary behavioral mechanisms. One
candidate is mental accounting (Thaler, 1999), under which consumers may treat digital
coupons as a distinct budget for extra or hedonic consumption. 37 This interpretation is
consistent with the finding that the largest treatment effects are observed among individ-
uals who are wealthy, have high spending levels, and reside in areas with a high share of
large establishments—those who are more capable of discretionary consumption. The de-
sign features of digital coupons may further amplify such responses. Minimum spending
thresholds create salient spending targets, while short expiration windows heighten the per-
ceived cost of non-redemption. Consistent with salience models (Bordalo et al., 2012, 2013)
and loss aversion (Tversky and Kahneman, 1991), these features may elevate spending be-
yond what standard price incentives alone would predict. Although our empirical design
does not separately identify these channels, these behavioral mechanisms may complement
rational threshold-based incentives in explaining the heterogeneous consumption responses
documented in this section. We now turn to the distributional consequences of those re-
sponses.
5 Distributional Consequences and Policy Design
Digital coupons stimulate consumption through heterogeneous consumer responses. Be-
cause consumers differ systematically in where they spend, this heterogeneity necessarily
translates into heterogeneous impacts across businesses. Understanding this mapping from
consumer-side stimulus to firm-level incidence is central to evaluating digital coupon pro-
36A rigorous test of the rational threshold models in our setting would require identifying which consumers are
marginal or inframarginal with respect to the coupon bundle in the absence of treatment. That distinction cannot
be inferred sharply from baseline spending per order alone. Because the coupons are bundled and only one coupon
can be used per order, bundle-level inframarginality depends on the consumer’s counterfactual same-day ordering
pattern—that is, whether the consumer would have placed no order, one qualifying order, or multiple qualifying orders
on that day even without the coupon bundle. Because we do not observe such same-day order histories over the six
months prior to the coupon event, baseline spending per order can provide only an imperfect guide to bundle-level
marginality or inframarginality. The evidence presented here should therefore be interpreted as suggestive rather
than conclusive.
37Boehm et al. (2025) formalize this mechanism in a model where recipients of windfall transfers perceive the funds
as “special money” and experience disutility from allocating them to routine expenditures. Because households face
search costs in identifying non-routine uses, the salience of a short expiration window induces earlier spending and
raises marginal propensities to consume.
29

(a) By Establishment Size
 (b) By Price Level
Figure 8. Coupon-Induced Revenue Gains Across Establishments
Notes:This figure presents estimated coupon-induced revenue gains across establishments. Revenue gains are com-
puted by allocating each consumer’s estimated increase in total spending—including both out-of-pocket expenditure
and the coupon subsidy—across establishments they patronized during the treatment period in proportion to their
observed spending shares. Panel (a) groups establishments by sales revenue (six months prior to the coupon event)
and reports average gains within each size decile. Panel (b) groups establishments by average order price (six months
prior to the coupon event) and reports average gains within each price decile.
grams as a policy tool. In this section, we document the mapping from consumer responses
to business gains and examine how alternative targeting rules affect both overall stimulus
and the distribution of benefits across firms.
5.1 Distributional Impact on Local Businesses
Because digital coupons operate through consumers rather than as direct transfers to
businesses, the distribution of gains across firms depends jointly on which consumers respond
most strongly and where they allocate their spending.
To quantify business-level gains, we link individual treatment effects to establishments
using transaction data. For each consumer, we allocate their estimated increase in total
spending—including both out-of-pocket expenditure and the coupon subsidy—across the
establishments they patronized during the treatment period in proportion to their observed
spending shares. Section OA6.2 provides details. 38 Our results reveal pronounced inequality
in revenue gains across businesses, with larger and higher-priced establishments capturing
the greatest increases. As shown in Figure 8, average gains rise steadily with establishment
size, while higher-priced establishments experience systematically larger increases in revenue.
38Our procedure assumes that each consumer’s additional spending is distributed proportionally across the busi-
nesses they patronized during the treatment period. This isolates the role of consumer–business matching and
abstracts from within-consumer reallocation across establishments. To the extent that coupons can shift incremental
spending toward larger or higher-priced establishments, our results represent an underestimate of both the dispersion
of business gains and the concentration of benefits among large establishments.
30

These patterns align with consumer redemption behavior documented in Figure OA.2, which
shows more frequent coupon redemptions at businesses with higher historical sales and order
prices.
A key empirical correlation underlies these unequal impacts: consumers with higher
coupon MPCs tended to allocate a larger share of their spending to large establishments
(Figure OA.3). Table OA.9 provides additional evidence. Consumers who mainly patron-
ized SMEs differed markedly from those who frequented larger businesses. The former had
lower wealth, placed smaller orders, and lived in areas with fewer restaurants overall but a
higher share of SMEs. We can quantify the importance of this form of consumer-business
matching with a simple counterfactual: suppose all individuals had identical spending alloca-
tions equal to overall market shares. Under this scenario, the variance in revenue gains across
businesses would decline by 52 percent. Together, these results show that firm-level incidence
was shaped by the interaction of heterogeneous consumer responses and consumer-business
matching: larger establishments experienced larger revenue gains because they dispropor-
tionately served consumers with larger consumption responses to the coupon program. 39
These findings have direct implications for policy design. If the goal of a stimulus program
is to provide broad-based support to all businesses, particularly smaller or more vulnerable
ones, then the existing design of digital coupon programs may not achieve that objective.
5.2 Policy Design
Consumer heterogeneity creates scope for targeting and makes coupon allocation a cen-
tral policy design choice. Directing coupons toward consumers with the largest expected
spending responses has the potential to significantly increase the total stimulus generated
by a given budget. However, as shown in the previous subsection, those consumers also
disproportionately patronize larger businesses. Efficiency-maximizing targeting may thus
concentrate the program’s gains among large firms, potentially conflicting with objectives
such as supporting vulnerable small businesses. More generally, allocation rules affect not
only total stimulus but also business incidence. Coupon policy must therefore be tailored
to the policymaker’s objective. In this subsection, we evaluate alternative allocation rules
under different policy goals.
5.2.1 Maximizing Stimulus Effect
We first examine efficiency gains from targeting coupons based on consumers’ predicted
responsiveness to the stimulus. Following the rank-weighted average treatment effect (RATE)
39This observed matching between high-response consumers and larger establishments should be interpreted as
conditional on the threshold structure of the Beijing program. Under alternative coupon designs, a different set of
consumers may respond most strongly, potentially altering the observed matching between consumer responsiveness
and establishment type.
31

(a) Targeting Efficiency
 (b) Correlation among Characteristics
Figure 9. Efficiency Gains from Targeted Coupon Distribution
Notes:This figure evaluates the potential efficiency gains from targeting coupon allocation based on consumer
characteristics. Panel (a) shows how the average treatment effect varies with the fraction of consumers targeted. For
each targeting dimension, consumers are ranked by their predicted treatment effect and each curve plots the average
effect when coupons are allocated to the most responsive consumers up to that fraction. The solid navy curve targets
using the full set of observable characteristics; the remaining curves target using a single characteristic: spending
per order, wealth, and the share of large establishments, respectively. The horizontal gray dashed line indicates the
benchmark ATT under the actual coupon allocation. Panel (b) illustrates residential sorting between individual
wealth and the share of non-SME establishments within 3km of the individual’s home address. For each percentile
cutoff (from the top 10% to 50%), the vertical axis shows the probability that an individual is simultaneously in
the top of both the wealth distribution and the neighborhood non-SME share distribution. The solid blue line
shows the actual joint probability, while the dashed black line shows the probability expected under independence.
Because targeting on one characteristic also selects consumers who score highly on correlated characteristics, single-
characteristic targeting can approximate multidimensional targeting more closely than independent variation would
suggest.
framework of Tibshirani et al. (2024), we rank consumers by their estimated treatment ef-
fects and compute the average effect when coupons are allocated to the most responsive
consumers up to a given fraction of the population.
Figure 9a presents the results. The vertical axis shows the predicted average treatment
effect among targeted consumers, while the horizontal axis indicates the fraction of the pop-
ulation receiving coupons. The solid curve represents targeting based on the full set of
individual characteristics, while the remaining curves target based on a single characteristic:
spending per order, wealth, and the share of large establishments, respectively. 40 The hor-
izontal dashed line indicates the benchmark OOP effect of¥1.80 under the actual coupon
allocation. The results demonstrate substantial efficiency gains from targeting: for example,
allocating coupons to the top 10 percent of consumers based on their predicted treatment
effects increases daily consumption by¥12.39—more than six times the benchmark.
40Section OA6.4 presents the full set of targeting strategies and shows the predicted average treatment effects in
numeric values by targeting decile.
32

In practice, governments may not have the capacity to target based on a large range of
consumer characteristics. We therefore consider targeting strategies based on single charac-
teristics that are more realistic to implement. The single-characteristic targeting curves in
Figure 9a show that even targeting on one dimension can yield substantial gains: treating
the top 10 percent of consumers can achieve daily consumption increases of¥7.43,¥4.50,
and¥3.90 for spending per order, wealth, and the share of large establishments, respec-
tively. Expanding to the top 20 percent, spending-per-order targeting more than doubles
the stimulus effect compared to the benchmark.
While single-characteristic targeting is less effective than using comprehensive consumer
data, spatial sorting patterns partially mitigate efficiency losses. Targeting based on one
attribute can identify a population similar to one selected through more complex criteria due
to correlations among consumer characteristics. Figure 9b illustrates this sorting effect by
examining the correlation between wealth and local consumption amenities. The horizontal
axis represents different targeting thresholds based on the most responsive consumers (from
the top 10 percent to the top 50 percent), while the vertical axis shows the probability
that an individual falls within these top percentiles for both wealth and neighborhood share
of large establishments. The dashed line shows the expected overlap under independence
between these two dimensions (e.g., if 10 percent of individuals are in the top 10 percent
of both distributions, the probability would be 0.01 under independence). The solid line
shows the actual realized overlap, which is substantially higher. For example, among the
top 10 percent wealthiest consumers, approximately 12 percent also live in areas with the
top 10 percent highest share of large establishments—twelve times the 1 percent expected
under independence. This gap demonstrates that targeting one dimension can capture many
of the same consumers as multidimensional targeting, partially compensating for limited
information in practical policy implementation. 41
5.2.2 Supporting Small Businesses
Supporting SMEs is often a central policy objective for local governments during economic
downturns.42 SMEs face greater vulnerability to demand shocks due to limited access to
credit markets and lower liquidity buffers, and their closure can generate persistent losses
in local employment and neighborhood amenities (Chodorow-Reich, 2014; Buera and Moll,
2015; Bartik et al., 2020). However, targeting based solely on consumer responsiveness
may direct spending toward larger businesses, as discussed in Section 5.1. These larger
41While such correlations among consumer characteristics create challenges for disentangling the individual drivers
of treatment effects—which we address in this paper—they are helpful for targeting purposes by allowing simple rules
to approximate more sophisticated selection criteria.
42For example, the Beijing municipal government’s policy document “Specific Measures to Help Enterprises Over-
come Difficulties and Promote Rapid Recovery of Consumption” explicitly stated that its digital coupon program
aimed to maximize support for restaurant business recovery and development, with specific provisions to support
small and medium enterprises in pandemic-affected sectors (Beijing Municipal Commission, 2022).
33

(a) SME at 20th percentile
 (b) SME at 50th percentile
 (c) SME at 86th percentile
Figure 10. Tradeoff Between Overall Stimulus and SME Support
Notes:This figure illustrates the tradeoff between maximizing total coupon-induced revenue and increasing SME
revenue share under alternative targeting policies. We define a weighted objective function that places weightλon
SME revenue and 1−λon non-SME revenue, and construct targeting rules using the optimal policy tree algorithm
(Athey and Wager, 2021) to identify the coupon allocation that maximizes this objective. Panel (a) defines SMEs as
establishments below the 20th percentile of sales revenue in the six months prior to the coupon event, Panel (b) as
those below the 50th percentile, and Panel (c) as those below the 86th percentile. Each bar represents total coupon-
induced revenue, decomposed into SME revenue (red) and non-SME revenue (blue). As weight on SMEs increases
(moving right along the horizontal axis), the SME share rises while total revenue declines. The corresponding details
are presented in Section OA6.3.
businesses may also employ more workers and generate greater tax revenue. This creates a
fundamental tradeoff between maximizing total stimulus (which may favor large businesses)
and achieving distributional objectives that support vulnerable SMEs. This tradeoff is rooted
in the distinct characteristics of consumers who patronize different types of establishments:
since higher-MPC consumers generate larger stimulus effects but tend to frequent large
establishments, prioritizing SME patronage necessarily involves targeting consumers with
lower average responsiveness.
To systematically evaluate policies that balance overall stimulus effectiveness with SME
support, we apply optimal policy trees (Athey and Wager, 2021) to search for the best
allocation rule by defining a weighted objective. Specifically, we search for policies that
maximizeλ·R SME+(1−λ)·R large, whereR SME andR large represent coupon-induced consumer
spending at SMEs and large establishments, respectively, andλ∈[0,1] represents the weight
placed on SME outcomes in the policy objective. 43 Whenλ= 0.5, this objective places
equal weight on SME and non-SME revenue and is therefore equivalent to maximizing total
stimulus. Asλincreases from 0.5 to 1.0, the objective places progressively greater value on
revenue generated at SMEs relative to large establishments. Whenλ= 1, it places weight
exclusively on SME revenue. By varyingλ, we trace out the efficient frontier of policies that
balance these competing objectives.
We present results across three different classification thresholds of SMEs based on per-
centiles of sales revenue in the six months prior to the coupon event: establishments in the
43We implement the policy tree algorithm using thepolicytreepackage inR, restricting the policy class to
depth-2 decision trees. Section OA6.3 provides details.
34

lowest 20th, 50th, and 86th percentiles. The 50th percentile represents a commonly used
threshold and is the definition used throughout our analysis, while the 86th percentile aligns
with definitions used by the U.S. Small Business Administration (U.S. Census Bureau, 2021)
for small business classification. 44 These thresholds show how the tradeoff varies with the
breadth of the SME definition.
Figures 10a to 10c present results across these three SME definitions. The analysis reveals
a clear tradeoff: increasing the weight on SMEs boosts their share of induced revenue but re-
duces overall stimulus effectiveness. For example, in Figure 10b, prioritizing SMEs increases
their revenue share from 6 percent to 10 percent, but at the cost of a 7 percent reduction
in total revenue generated. This pattern persists across all SME definitions, illustrating the
tension between maximizing overall economic impact and ensuring equitable distribution of
benefits.45
5.2.3 Reconciling Efficiency and Equity
The previous section shows that targeting can be used to navigate the efficiency–equity
tradeoff inherent in digital coupon programs. By reallocating coupons across consumers,
policymakers can shift the balance between maximizing total stimulus and directing bene-
fits toward SMEs. Yet demand-side targeting has an inherent limitation: policymakers can
decide which consumers receive coupons, but not which firms those consumers ultimately
patronize. Because business incidence is mediated by consumer spending choices, even an op-
timally targeted coupon policy cannot precisely direct support to particular establishments.
Supply-side instruments such as direct transfers have the opposite property: they can tar-
get firms precisely, but they do not harness consumer co-financing and therefore cannot
generate the same stimulus multiplier as digital coupons. These complementary strengths
and limitations motivate a hybrid policy that combines targeted coupon distribution with
direct transfers to SMEs. Specifically, we propose allocating coupons to a targeted subset of
high-response consumers and using the resulting budget savings to provide direct transfers
to SMEs. Because these consumers generate more spending per yuan of government subsidy,
a given level of aggregate stimulus can be achieved with lower coupon expenditure, freeing
44The U.S. Small Business Administration defines “small” establishments as those accounting for 50 percent of
total industry revenue. Applied to our Beijing restaurant data, this criterion corresponds to the 86th percentile of
six-month pre-event sales revenue.
45In addition to the efficiency-equity tradeoff quantified here, there is also a consumer-side normative consideration.
Because consumers who patronize SMEs tend to have lower wealth (Table OA.9), policies that shift more revenue
toward SMEs also rely more heavily on lower-wealth consumers’ out-of-pocket spending to generate the stimulus effect.
Under a standard rational benchmark, receiving digital coupons should always yield non-negative utility gains, so
targeting lower-wealth consumers would directly benefit them. However, the empirical findings in Section 4.4 suggest
that the observed responses are not fully explained by simple rational threshold-based models alone. If stimulus
relies on consumer co-financing and behavioral mechanisms also shape spending responses, then shifting more of the
financing burden toward lower-wealth consumers may have ambiguous welfare implications for those consumers, even
if such targeting better supports SMEs. Recognizing this consideration can be important in the policy design of
digital coupons, even though our paper does not attempt a behavioral welfare analysis.
35

Table 3. Comparison of Alternative Coupon Distribution Policies
Policy Design Consumers
T reated
Coupon
Subsidies
Consumer
Out-of-pocket
Spending
Direct
T ransfers to
SMEs
T otal
Stimulus
Random allocation 50% 117,108 315,773 0 432,881
Full targeting 51% 117,108 725,960 0 843,068
Hybrid policy 11% 27,551 405,220 89,557 522,328
Notes:This table compares three coupon allocation strategies under a fixed total policy budget of¥117,108. The
“Random allocation” strategy randomly assigns coupons to half of the sample. The “Full targeting” strategy ranks
all consumers by their predicted treatment effects and allocates coupons to the most responsive individuals until the
full budget is exhausted on coupon subsidies. Under the “Hybrid policy,” the algorithm targets only enough high-
response individuals to approximately match the total stimulus achieved under random allocation. This requires
only¥27,551 in coupon subsidies, allowing the remaining¥89,557 of the fixed budget to be redirected as direct
transfers to SMEs. All monetary values are aggregates over the entire coupon period. Total stimulus is defined as
the sum of consumer out-of-pocket spending, coupon subsidies, and any direct transfers to SMEs.
fiscal resources for firm-side support.
To illustrate, Table 3 compares three allocation strategies under a fixed government
budget of¥117,108, which corresponds to the observed coupon subsidy expenditure in our
sample. We compare the total stimulus achieved by each strategy, defined as the total
monetary support delivered to local businesses. The “Random allocation” strategy randomly
assigns coupons to half of the sample. 46 Under this allocation, consumer out-of-pocket
spending totals¥315,773. Together with the¥117,108 in coupon subsidies, this yields
a total stimulus of¥432,881. The “Full targeting” strategy ranks all consumers in our
sample by their predicted treatment effects and allocates coupons to the most responsive
individuals until the full government budget is exhausted. Despite treating a comparable
share of consumers (51 percent), this approach more than doubles consumer out-of-pocket
spending to¥725,960 and raises total stimulus to¥843,068, but provides no targeted support
to SMEs.
The “Hybrid policy” targets only the most responsive 11 percent of consumers. Under this
allocation, consumer out-of-pocket spending totals¥405,220, while requiring only¥27,551 in
coupon subsidies. The coupon component of the policy therefore generates a total stimulus
of¥432,771, approximately matching the¥432,881 achieved under random allocation, while
using less than one quarter of the original budget. The remaining¥89,557 of the government
budget can then be transferred directly to SMEs. With these direct transfers counted one-
for-one as support delivered to businesses, total stimulus reaches¥522,328, exceeding the
random allocation benchmark by approximately 21 percent while also providing targeted
support for vulnerable businesses.
46In practice, the resulting allocation corresponds to our matched estimation sample, where treated and control
units are balanced on observed characteristics and half of the sample is treated.
36

In summary, targeting coupons toward the most responsive consumers can substantially
improve program efficiency but concentrates benefits among large establishments. The hy-
brid approach addresses this limitation by combining the multiplier advantage of targeted
coupons with the targeting precision of direct transfers: coupons generate aggregate stimu-
lus, while direct transfers allow policymakers to channel support to SMEs without relying
on consumer spending choices. More broadly, our results demonstrate that when policy ob-
jectives include both overall stimulus and the distribution of gains across firms, combining
demand-side and supply-side instruments can outperform either instrument used in isolation.
6 Conclusion and Policy Implications
Digital coupon programs have emerged as a popular stimulus tool, yet we do not fully un-
derstand their distributional consequences. Our analysis of Beijing’s 2022 initiative reveals
that digital coupons amplify government subsidies through additional consumer spending,
so that both their stimulus effect and firm-level incidence depend critically on heterogeneous
consumer responses. While the program generates significant increases in short-term spend-
ing, the resulting revenue gains are distributed unevenly across businesses. These findings
offer actionable insights for the design of digital coupon programs, with broader implications
for demand-side stimulus policies.
Governments typically employ two broad categories of stimulus tools during economic
downturns. Demand-side instruments seek to raise consumer spending through transfers or
consumption incentives directed at households, such as the U.S. Economic Stimulus Pay-
ments in 2001, 2008, and 2020, as well as more recent policies using prepaid cards or time-
limited consumption vouchers (Boehm et al., 2025). Supply-side instruments, by contrast,
provide direct support to businesses. During the COVID-19 pandemic, many governments
implemented business-assistance programs, such as the U.S. Paycheck Protection Program
and related schemes in other countries, to help vulnerable enterprises survive temporary
demand shortfalls.
Digital coupons represent a demand-side instrument in the form of consumption vouchers
with minimum spending thresholds and short expiration windows. Our study finds that they
generate significant and highly heterogeneous consumption responses. This heterogeneity,
in turn, shapes the incidence of the program: high-response consumers tend to patronize
larger businesses, leading to an uneven allocation of stimulus benefits. More broadly, this
mechanism extends beyond digital coupons. Whenever a demand-side stimulus policy elic-
its heterogeneous responses from consumers, those differences will translate into unequal
firm-side gains so long as consumers are systematically matched to firms—that is, so long
as different types of consumers frequent different types of businesses. Consequently, the
incidence of demand-side stimulus policies, in terms of which businesses ultimately benefit,
37

cannot be understood from consumer responses alone.
At the same time, our setting is more specific than many traditional coupon or stimulus
environments. The program we study targets food delivery, a largely non-storable con-
sumption category, which likely reduces the scope for intertemporal substitution through
stockpiling, although cross-category substitution remains possible. Our results are there-
fore most directly informative about digital coupon stimulus in an immediately consumable
service category. The heterogeneity we document generalizes beyond this particular con-
sumption category and has immediate implications for how digital coupon programs should
be designed.
The substantial heterogeneity in consumer responses implies that a uniform allocation
of coupons is unlikely to be optimal and creates scope for more deliberate policy design.
Through targeted distribution, policymakers can significantly increase aggregate stimulus by
directing coupons toward consumers with the strongest predicted responses. Alternatively,
targeting can be used to steer spending toward businesses that policymakers wish to support,
such as SMEs. Doing so entails an efficiency-equity tradeoff: shifting revenue gains toward
small businesses comes at the cost of lower aggregate stimulus. Importantly, we show that
such targeting can be implemented using only a few observable characteristics, making it
feasible even in settings with limited data infrastructure.
Hybrid policy provides a way to pursue the dual objectives of raising aggregate stimulus
and supporting desired businesses by combining the strengths of demand-side and supply-
side instruments. Demand-side targeting can generate stimulus efficiently, but it influences
business outcomes only indirectly through the consumers who receive coupons and the busi-
nesses they happen to patronize. Supply-side instruments, by contrast, can channel support
directly to specific businesses, but they do not leverage additional consumer spending and
therefore do not produce the same multiplier effects as digital coupons. A hybrid approach
thus uses each instrument for what it does best: targeted coupons maximize consumption
stimulus, while direct business subsidies ensure that support reaches vulnerable firms such
as SMEs.
Taken together, our analysis points to several broader lessons for stimulus design. First,
policymakers should recognize explicitly that many stimulus instruments involve efficiency-
equity tradeoffs: policies that appear effective in aggregate may distribute gains unevenly.
Second, heterogeneity in consumer responses can be a valuable input into policy design,
allowing governments to improve the effectiveness of stimulus policies through targeting.
Third, when policy objectives include both aggregate demand support and support for vul-
nerable businesses, combining demand-side and supply-side instruments may be more effec-
tive than relying on either margin alone.
Finally, while digital coupons appear especially well suited to generating immediate, tar-
geted stimulus, cash-transfer programs may be better suited to providing medium-term,
38

broad-based consumption support. The choice between instruments should depend on spe-
cific policy objectives: immediate targeted stimulus versus broader consumption support,
and short-term stimulus versus longer-term economic stabilization.
One important margin of policy optimization lies beyond the scope of our analysis. Digital
coupon programs can be optimized along two distinct margins: targeting, which determines
who receives coupons, and coupon design, which determines features such as minimum spend-
ing thresholds and expiration windows. Because the Beijing program does not provide the
independent variation needed to separately identify the causal effects of alternative coupon
designs, our analysis focuses only on the first margin. We therefore do not draw conclusions
about how changes in thresholds or expiration windows would affect consumption responses
or business-side incidence. Studying this second margin, and characterizing optimal design
parameters and targeting rules under alternative policy objectives, is an important direction
for future research.
39

References
Apley, D. W. and Zhu, J. (2020). Visualizing the Effects of Predictor Variables in Black Box
Supervised Learning Models.Journal of the Royal Statistical Society Series B: Statistical
Methodology, 82(4):1059–1086.
Athey, S. and Imbens, G. (2016). Recursive partitioning for heterogeneous causal effects.
Proceedings of the National Academy of Sciences, 113(27):7353–7360.
Athey, S., Tibshirani, J., and Wager, S. (2019). Generalized random forests.The Annals of
Statistics, 47(2):1148–1178.
Athey, S. and Wager, S. (2019). Estimating treatment effects with causal forests: An appli-
cation.Observational Studies, 5:37–51.
Athey, S. and Wager, S. (2021). Policy learning with observational data.Econometrica,
89(1):133–161.
Bartik, A. W., Bertrand, M., Cullen, Z., Glaeser, E. L., Luca, M., and Stanton, C. (2020).
The impact of covid-19 on small business outcomes and expectations.Proceedings of the
National Academy of Sciences, 117(30):17656–17666.
Baugh, B., Ben-David, I., Park, H., and Parker, J. A. (2021). Asymmetric Consumption
Smoothing.American Economic Review, 111(1):192–230.
Beijing Municipal Commission (2022). Interpretation of the ‘specific measures on assisting
enterprises, relieving difficulties, promoting consumption, and accelerating recovery’.http
s://www.beijing.gov.cn/zhengce/zcjd/202207/t20220708_2767092.html. Accessed:
2026-06-25.
Boehm, J., Fize, E., and Jaravel, X. (2025). Five Facts about MPCs: Evidence from a
Randomized Experiment.American Economic Review, 115(1):1–42.
Bordalo, P., Gennaioli, N., and Shleifer, A. (2012). Salience Theory of Choice Under Risk.
The Quarterly Journal of Economics, 127(3):1243–1285.
Bordalo, P., Gennaioli, N., and Shleifer, A. (2013). Salience and Consumer Choice.Journal
of Political Economy, 121(5):803–843.
Borusyak, K., Jaravel, X., and Spiess, J. (2024). Revisiting event-study designs: Robust and
efficient estimation.The Review of Economic Studies, 91(6):3253–3285.
Britto, D. G. C., Pinotti, P., and Sampaio, B. (2022). The effect of job loss and unemployment
insurance on crime in brazil.Econometrica, 90(4):1393–1423.
Broda, C. and Parker, J. A. (2014). The economic stimulus payments of 2008 and the
aggregate demand for consumption.Journal of Monetary Economics, 68:S20–S36.
Buera, F. J. and Moll, B. (2015). Aggregate implications of a credit crunch: The importance
of heterogeneity.American Economic Journal: Macroeconomics, 7(3):1–42.
40

Chernozhukov, V., Chetverikov, D., Demirer, M., Duflo, E., Hansen, C., Newey, W., and
Robins, J. (2018). Double/debiased machine learning for treatment and structural param-
eters.The Econometrics Journal, 21(1):C1–C68.
Chodorow-Reich, G. (2014). The employment effects of credit market disruptions: Firm-level
evidence from the 2008–9 financial crisis.The Quarterly Journal of Economics, 129(1):1–
59.
Couture, V. and Handbury, J. (2020). Urban revival in America.Journal of Urban Eco-
nomics, 119:103267.
Davis, J. M. and Heller, S. B. (2017). Using causal forests to predict treatment heterogeneity:
An application to summer jobs.American Economic Review, 107(5):546–50.
Davis, J. M. and Heller, S. B. (2020). Rethinking the benefits of youth employment programs:
The heterogeneous effects of summer jobs.Review of Economics and Statistics, 102(4):664–
677.
Ding, J., Jiang, L., Msall, L., and Notowidigdo, M. J. (2025). Consumer-financed fiscal
stimulus: Evidence from digital coupons in china.American Economic Review: Insights,
7(3):411–427.
Ele.me (2024). Corporate social responsibility report.https://www.ele.me/csr2024.
Accessed: 2026-06-25.
Friedman, J. H. (2001). Greedy Function Approximation: A Gradient Boosting Machine.
The Annals of Statistics, 29(5):1189–1232.
Hansen, B. B. and Klopfer, S. O. (2006). Optimal full matching and related designs via
network flows.Journal of Computational and Graphical Statistics, 15(3):609–627.
Hastings, J. and Shapiro, J. M. (2018). How are snap benefits spent? evidence from a retail
panel.American Economic Review, 108(12):3493–3540.
Hino, M., Benami, E., and Brooks, N. (2018). Machine learning for environmental monitor-
ing.Nature Sustainability, 1(10):583–588.
Hsieh, C. T., Shimizutani, S., and Hori, M. (2010). Did japan’s shopping coupon program
increase spending?Journal of Public Economics, 94(7):523–529.
Johnson, D. S., Parker, J. A., and Souleles, N. S. (2006). Household expenditure and the
income tax rebates of 2001.American Economic Review, 96(5):1589–1610.
Johnson, M. S., Levine, D. I., and Toffel, M. W. (2023). Improving regulatory effectiveness
through better targeting: Evidence from osha.American Economic Journal: Applied
Economics, 15(4):30–67.
Kan, K., Peng, S. K., and Wang, P. (2017). Understanding consumption behavior: Evidence
from consumers’ reaction to shopping vouchers.American Economic Journal: Economic
Policy, 9(1):137–153.
41

Kaplan, G. and Violante, G. L. (2014). A model of the consumption response to fiscal
stimulus payments.Econometrica, 82(4):1199–1239.
Laan, M. J. v. d., Polley, E. C., and Hubbard, A. E. (2007). Super Learner.Statistical
Applications in Genetics and Molecular Biology, 6(1):1–21.
Liu, Q., Shen, Q., Li, Z., and Chen, S. (2021). Stimulating consumption at low budget:
Evidence from a large-scale policy experiment amid the covid-19 pandemic.Management
Science, 67(12):7291–7307.
Mian, A. and Sufi, A. (2012). The effects of fiscal stimulus: Evidence from the 2009 cash for
clunkers program.The Quarterly Journal of Economics, 127(3):1107–1142.
Milkman, K. L. and Beshears, J. (2009). Mental accounting and small windfalls: Evidence
from an online grocer.Journal of Economic Behavior & Organization, 71(2):384–394.
Misra, K. and Surico, P. (2014). Consumption, income changes, and heterogeneity: Evi-
dence from two fiscal stimulus programs.American Economic Journal: Macroeconomics,
6(4):84–106.
Orchard, J. D., Ramey, V. A., and Wieland, J. F. (2025). Micro MPCs and Macro Counter-
factuals: The Case of the 2008 Rebates.The Quarterly Journal of Economics, 140(3):2001–
2052.
Parker, J. A., Schild, J., Erhard, L., and Johnson, D. S. (2022). Economic impact payments
and household spending during the pandemic.Brookings Papers on Economic Activity,
2022(2):81–156.
Parker, J. A., Souleles, N. S., Johnson, D. S., and McClelland, R. (2013). Consumer spending
and the economic stimulus payments of 2008.American Economic Review, 103(6):2530–
2553.
Reinholtz, N., Bartels, D. M., and Parker, J. R. (2015). On the Mental Accounting of
Restricted-Use Funds: How Gift Cards Change What People Purchase.Journal of Con-
sumer Research, 42(4):596–614.
Sahm, C. R., Shapiro, M. D., and Slemrod, J. (2010). Household response to the 2008
tax rebate: Survey evidence and aggregate implications.Tax Policy and the Economy,
24(1):69–110.
Sant’Anna, P. H. C. and Zhao, J. (2020). Doubly robust difference-in-differences estimators.
Journal of Econometrics, 219(1):101–122.
Semenova, V. and Chernozhukov, V. (2020). Debiased machine learning of conditional av-
erage treatment effects and other causal functions.The Econometrics Journal, 24(2):264–
289.
Shapiro, M. D. and Slemrod, J. (2003). Consumer response to tax rebates.American
Economic Review, 93(1):381–396.
Shapiro, M. D. and Slemrod, J. (2009). Did the 2008 tax rebates stimulate spending?
American Economic Review, 99(2):374–379.
42

Thaler, R. H. (1999). Mental accounting matters.Journal of Behavioral Decision Making,
12(3):183–206.
Tibshirani, J., Athey, S., Sverdrup, E., and Wager, S. (2024).grf: Generalized Random
Forests. R package version 2.4.0.
Tversky, A. and Kahneman, D. (1991). Loss Aversion in Riskless Choice: A Reference-
Dependent Model.The Quarterly Journal of Economics, 106(4):1039–1061.
U.S. Census Bureau (2021). What is a small business?https://www.census.gov/library
/stories/2021/01/what-is-a-small-business.html. Accessed: 2026-06-25.
Wager, S. and Athey, S. (2018). Estimation and Inference of Heterogeneous Treatment Effects
using Random Forests.Journal of the American Statistical Association, 113(523):1228–
1242.
Xing, J., Zou, E. Y., Yin, Z., Wang, Y., and Li, Z. (2023). “quick response” economic
stimulus: The effect of small-value digital coupons on spending.American Economic
Journal: Macroeconomics, 15(4):249–304.
Xinhua News (2025). Will jd’s entry change the landscape of the food delivery industry?
http://www.xinhuanet.com/finance/20250219/38b06361ce0947f0922ca26422c50aa
c/c.html. Accessed: 2026-06-25.
43

Online Appendix for “Consumption Stimulus with Digital
Coupons: Heterogeneity and Policy Design”
by Ying Chen, Mingyi Li, Jiaming Mao and Jingyi Zhou
OA1 Data and Sample Construction
OA1.1 Mobile Application Usage Data
Our analysis sample comprises users who participated in the coupon event on the Ele.me
platform. To assess whether these participants are representative of the broader Ele.me user
base, we draw on a large-scale mobile application usage dataset from a major telecommuni-
cations provider in China. The dataset tracks monthly usage time for all mobile applications
with at least 500 users among all subscribers to the provider’s service in Beijing during Au-
gust 2022, August 2023, and November 2023. The telecommunications provider collaborates
with the Bureau of Statistics to calculate weights using population census data, enabling
representative estimates of app usage across Beijing’s population. The sample covers 10.87
million subscribers in August 2022 (43.5 percent of Beijing’s residential population) and 11.20
million in August 2023 (45.7 percent), representing approximately 21.8 million weighted res-
idents in both periods. We also use this data to assess potential platform substitution in
Section OA3.5.
We assess the representativeness of our baseline sample by comparing it to the popula-
tion of all Ele.me users identified in the mobile application usage data. Among coupon event
participants in our sample, the average age is 32 years and the female share is 64 percent.
Among all Ele.me users in the mobile application usage data, the average age is 35 years
and the female share is 53 percent. While these samples are not directly comparable (the
analysis sample is drawn through stratified random sampling from coupon program partici-
pants, whereas the mobile application usage data captures all Ele.me users in Beijing), the
demographic profiles suggest that coupon participants skew somewhat younger and more
female than the broader Ele.me user base. The modest differences indicate that our analysis
sample, while focused on the event participants, reflects a reasonably representative subset
of the platform’s active user population.
OA1.2 Matching Procedure
We employ a Logit model to estimate propensity scores using 4,237 treatment and 2,225
control users with complete individual characteristics data. The model includes our full set of
observed characteristics, including age, gender, platform membership, wealth, consumption
44

habits (order frequency and expenditure per order over the six months prior to the coupon
event) and local consumption amenities (the number of establishments and the share of non-
SME establishments in the neighborhood). Table OA.1 compares individual characteristics
between groups before and after matching. Panel A shows significant differences across all
variables before matching. Panel B demonstrates successful balancing post-matching, with
no significant differences and small magnitudes relative to mean values.
Table OA.1. Comparison Between the Treatment Group and Control Group
Panel A: Before Matching
Treatment Control Differencet-statistics
Age 32.301 31.716 0.585 2.45**
Female 0.631 0.549 0.081 6.18***
Platform membership 0.361 0.236 0.125 10.71***
Wealth 0.032 -0.061 0.093 3.31***
Number of orders (past 6 months) 54.582 38.840 15.743 12.15***
Spending per order (past 6 months) 45.059 45.581 -0.522−0.52
Number of establishments 51.831 48.056 3.775 4.41***
Share of non-SME establishments 0.523 0.528 -0.004−1.29
Panel B: After Matching
Treatment Control Differencet-statistics
Age 32.250 32.281 -0.030−0.09
Female 0.635 0.657 -0.022−1.25
Platform membership 0.382 0.395 -0.013−0.68
Wealth 0.043 0.053 -0.010−0.25
Number of orders (past 6 months) 55.580 54.164 1.416 0.59
Spending per order (past 6 months) 45.236 44.913 0.324 0.34
Number of establishments 52.445 51.284 1.161 0.90
Share of non-SME establishments 0.524 0.526 -0.002−0.36
Notes:This table compares user characteristics between the treatment and control groups before and after propensity
score matching. Propensity scores are estimated using a Logit model with the covariates listed above, and each
treated individual is matched to one control individual with replacement. The pre-matching sample includes 4,237
treated and 2,225 control individuals with non-missing values on all covariates. The post-matching sample includes
3,787 matched pairs. The difference column reports the difference in group means, andt-statistics test the null of
equal means. *, **, and *** indicate statistical significance at the 10%, 5%, and 1% levels, respectively.
OA2 Coupon MPC and Out-of-Pocket Spending: Accounting Iden-
tities
LetE i denote total expenditure (merchant revenue) andS i the coupon subsidy (discount)
redeemed by individualiduring the treatment period. Out-of-pocket spending is defined as
OOPi =E i −S i.
45

We define the coupon marginal propensity to consume as
MPCcoupon i ≡ ∆Ei Si ,
where ∆E i denotes the change in total expenditure over the treatment period relative to
the no-coupon counterfactual. Since individuals receive no coupon subsidy in the absence of
treatment, we have ∆Si =S i.
Using this normalization, the change in out-of-pocket spending satisfies the accounting
identity:
∆OOPi = ∆(Ei −S i) = (MPCcoupon i −1)S i.(OA.1)
Therefore, MPC coupon i <1 implies ∆OOP i <0, indicating that the coupon user reduces
out-of-pocket spending (i.e., generates net savings for the consumer), while MPC coupon i >1
implies an increase in out-of-pocket spending.
OA3 Average Treatment Effects: Estimation and Results
OA3.1 Same-Day Effects of Coupon Receipt
We estimate a daily entry-exit DiD specification that captures the immediate impact
of coupon receipt on consumer spending. Unlike our baseline model, which defines treat-
ment at the individual level for the entire coupon event period, this alternative specification
defines treatment at the individual-day level, identifying the effect only on days when con-
sumers actually obtained coupons. We estimate the following two-way fixed effects (TWFE)
regression:
yit =γ i +λ t +α·Coupon it +ϵ it,
whereγ i andλ t represent individual and date fixed effects, respectively; and Coupon it is a
binary indicator equal to 1 if individualiobtained a coupon on datet, and 0 otherwise. The
coefficientαis intended to capture the same-day spending response.
Table OA.2 presents the results of this daily entry-exit DiD specification. On days when
consumers received coupons, their out-of-pocket expenditure increased by¥20.75 on aver-
age (Column 1), while total expenditure (including subsidies) increased by¥30.45 (Col-
umn 2). Interestingly, unsubsidized expenditure—spending on orders that did not use
coupons—decreased by¥2.93 (Column 3), suggesting some substitution from unsubsidized
to subsidized orders on coupon receipt days.
These results reveal a substantially larger same-day effect compared to our baseline esti-
mate of¥1.80 daily average effect over the entire coupon period. This difference is expected
since this daily specification captures the concentrated impact on specific days when coupons
46

Table OA.2. Same-Day Coupon Receipt: Spending Impacts by Expenditure Type
Out-of-pocket Total Unsubsidized
(1) (2) (3)
Coupon 20.747*** 30.45*** -2.928***
(0.563) (0.703) (0.441)
Observations 416,570 416,570 416,570
Notes:This table presents estimates from a daily entry-exit DiD specification with individual and date fixed
effects. The treatment variable is an indicator equal to one on days when individualiobtained a coupon, and zero
otherwise. Out-of-pocket expenditure represents total expenditure minus government-financed coupon subsidies,
total expenditure captures the full payment to sellers (including coupon subsidies), and unsubsidized expenditure
measures spending on orders that did not use coupons. Observations from the post-program period are excluded.
Standard errors are clustered at the individual level. *, **, and *** indicate statistical significance at the 10%, 5%,
and 1% levels, respectively.
were obtained, rather than averaging the effect across all days during the coupon period.
While this specification provides insight into the immediate spending response, we pre-
fer our baseline approach for several reasons discussed in the main text. First, the daily
specification may be subject to endogeneity concerns if individuals strategically time their
participation based on anticipated consumption needs on specific days. Second, this entry-
exit treatment definition raises additional concerns beyond those in our baseline specification.
Recent literature on staggered DiD designs highlights potential biases when treatment tim-
ing varies across units and when previously treated units can revert to untreated status
(De Chaisemartin and d’Haultfoeuille, 2020; Goodman-Bacon, 2021). Such designs may
produce biased estimates when treatment effects are heterogeneous across time or units, as
earlier-treated observations can serve as controls for later-treated ones. Nevertheless, these
daily results corroborate our main finding that coupon receipt increases consumer spending,
while providing additional granularity on the timing of these effects.
OA3.2 Robustness to Timing- and Effort-Based Selection
We conduct two robustness checks to ensure our results are not driven by selection bias.
We apply more conservative criteria to define treated users. First, to address selection
on timing, we use the timestamps of successful coupon claims to approximate the daily
coupon quota-exhaustion point and restrict the treatment group to near-cutoff recipients—
individuals who obtained at least one coupon bundle within the final decile of a day’s suc-
cessful claim timestamps during the program period. These users experienced at least one
“last-minute” success and therefore relied less heavily on systematically early claim attempts.
Second, to address selection on effort intensity, we restrict the treated group to one-time
recipients—individuals who obtained exactly one coupon bundle during the program period.
This definition excludes persistent, high-engagement users who claimed coupons repeatedly
47

across multiple days.
Table OA.3 reports the results. Both alternative treatment definitions yield estimates
similar to our baseline specification, with OOP treatment effects of¥1.97 and¥2.53, respec-
tively, compared to our baseline estimate of¥1.80. The consistency across these subsamples
suggests that our main findings are not driven by selection on timing or effort intensity and
remain robust to substantially more restrictive definitions of treatment status.
Table OA.3. Robustness to Timing- and Effort-Based Selection
Panel A: Near-Cutoff Recipients
Out-of-pocket Total Unsubsidized
(1) (2) (3)
Treat×Post 1.972** 2.897*** -0.342
(0.770) (0.784) (0.760)
Observations 85,360 85,360 85,360
Panel B: One-Time Recipients
Treat×Post 2.531*** 3.032*** 1.030
(0.847) (0.847) (0.846)
Observations 98,670 98,670 98,670
Notes:This table re-estimates the baseline DiD specification (Equation 1) with individual and date fixed effects,
using more conservative definitions of the treatment group. In Panel A, the treated group is restricted to near-
cutoff recipients, defined as individuals who obtained at least one coupon bundle within the final decile of a day’s
successful claim timestamps during the program period. In Panel B, the treated group consists of one-time recipients,
defined as individuals who obtained exactly one coupon bundle during the program period. Both panels implement
propensity score matching prior to estimation, following the procedure described in Section OA1.2. Out-of-pocket
expenditure represents consumer spending excluding coupon subsidies, total expenditure captures the full payment
to sellers (including government-financed coupon subsidies), and unsubsidized expenditure measures spending on
orders that did not use coupons. Standard errors are clustered at the individual level. *, **, and *** indicate
statistical significance at the 10%, 5%, and 1% levels, respectively.
OA3.3 Alternative DiD Estimators
We show that our conclusions do not depend on the matching design used in the baseline
specification by considering three alternative estimators. First, we re-estimate the baseline
DiD model on the full sample without matching. Second, we implement optimal full matching
following Hansen and Klopfer (2006). Unlike one-to-one pair matching, this approach forms
matched subclasses with varying treated–control ratios and thus makes fuller use of the
sample. Third, we implement the doubly robust DiD estimator of Sant’Anna and Zhao
(2020). This estimator combines inverse-probability weighting with outcome regression and
remains consistent if either the treatment-assignment model or the outcome-evolution model
is correctly specified.
Table OA.4 reports the results of these alternative estimators. Across all three panels,
48

the estimates are highly consistent with our baseline in Table 2. The estimated effects on
out-of-pocket and total expenditure remain similar in magnitude to the baseline, whereas
the effect on unsubsidized expenditure remains statistically insignificant. These exercises
suggest that neither the decision to match nor the particular matching procedure drives our
findings.
Table OA.4. Alternative DiD Estimates
Panel A: No Matching DiD
Out-of-pocket Total Unsubsidized
(1) (2) (3)
Treat×Post 1.587*** 2.339*** -0.207
(0.383) (0.387) (0.382)
Observations 355,410 355,410 355,410
Panel B: Full Matching DiD
Treat×Post 2.003*** 2.771*** -0.097
(0.494) (0.497) (0.493)
Observations 313,775 313,775 313,775
Panel C: Doubly Robust DiD
Treat×Post 1.992*** 2.756*** 0.166
(0.621) (0.628) (0.604)
Observations 11,490 11,490 11,490
Notes:This table reports alternative DiD estimates for the same three expenditure outcomes as in Table 2. Panel A
re-estimates Equation (1) on the underlying unmatched user-day sample (N=355,410). Panel B applies optimal full
matching using the full set of observed covariates. Since complete covariate information is required, the sample size
is reduced to 313,775. Panel C implements the doubly robust DiD estimator of Sant’Anna and Zhao (2020), which
uses a 2×2 block design at the period level and therefore reports 11,490 period-level observations rather than daily
user-day observations. The reported observation counts are not directly comparable to those in Table 2, because the
baseline specification in Table 2 is estimated on a matched sample constructed with replacement, so matched control
users appear multiple times according to their matching weights. Standard errors are clustered at the individual
level. *, **, and *** indicate statistical significance at the 10%, 5%, and 1% levels, respectively.
OA3.4 Decomposition of Treatment Effects and Substitution Patterns
Table OA.5 reports estimates underlying Figure 2. Panel A decomposes the aggregate
spending response along extensive and intensive margins, while Panel B tests for substitution
across time, categories, and household members. Panel A separates the total treatment effect
into extensive and intensive margins. While the extensive margin (order frequency) exhibits a
statistically significant increase, the magnitude of 0.029 additional orders per day (Column
2) is economically negligible. Instead, we observe a significant increase in out-of-pocket
expenditure per order alongside an increase in dishes per order.
49

Panel B evaluates the potential substitution patterns discussed in Section 3.1. Column
1 tests for inter-temporal substitution by estimating the spending response in the post-
coupon event period. The estimate is statistically indistinguishable from zero, showing that
the coupon event generated an immediate but temporary stimulus. Column 2 reports the
baseline effect on restaurant spending, while Column 3 tests for inter-category substitution
using grocery spending as the outcome. Restaurant out-of-pocket expenditure increases
significantly, whereas the estimated effect on grocery spending is near zero. This indicates
that the increase in restaurant spending did not come at the expense of other food-related
purchases on Ele.me. Column 4 evaluates intra-household or workplace substitution using
the number of tableware sets requested per order, which proxies for the number of diners.
The estimated effect is statistically significant but economically negligible, pointing to no
meaningful intra-household or workplace sharing to meet the minimum thresholds.
Table OA.5. Decomposition and Substitution Effects
Panel A: Decomposition Effects
OOP per order Order frequency SKU per order OOP per SKU
(1) (2) (3) (4)
Treat×Post 1.200*** 0.029*** 0.201** -1.047**
(0.424) (0.010) (0.094) (0.506)
Observations 416,570 416,570 109,640 109,640
Panel B: Substitution Effects
Post-treatment OOP Restaurant OOP Grocery OOP Tableware sets per order
(1) (2) (3) (4)
Treat×Post -1.210 1.769*** 0.033 0.021***
(0.790) (0.584) (0.191) (0.007)
Observations 212,072 416,570 416,570 416,570
Notes:This table presents estimates from Equation 1 using alternative dependent variables. Panel B Column 1
additionally redefines Post t to indicate the two weeks after the coupon event and restricts the sample accordingly
(see Section 3.1) Panel A decomposes the consumption response along extensive and intensive margins. Column
1 shows the effect on out-of-pocket (OOP) expenditure per order, Column 2 on order frequency, Column 3 on the
number of dishes (SKUs) per order, and Column 4 on OOP per dish (SKU). Columns 3 and 4 condition on days
with at least one order, resulting in fewer observations. Panel B examines potential substitution patterns. Column
1 tests for inter-temporal substitution by comparing OOP spending in the two weeks after the coupon event to the
pre-treatment period. Column 2 shows the baseline effect on restaurant OOP spending. Column 3 tests for inter-
category substitution using grocery OOP as the outcome. Column 4 tests for intra-household substitution using
tableware sets per order, which proxies for the number of diners. Standard errors are clustered at the individual
level. *, **, and *** indicate statistical significance at the 10%, 5%, and 1% levels, respectively.
OA3.5 Supplementary Evidence on Platform Substitution
The main text presents within-platform evidence that the coupon program’s spending
response reflects genuine consumption rather than reallocation across platforms or dining
formats. We provide supplementary evidence using mobile application usage data from a
50

major telecommunications provider, which tracks monthly app usage time for all subscribers
in Beijing (see Section OA1.1 for details).
To assess cross-platform substitution, we compute Ele.me’s share of food delivery app
usage time in Beijing, with the denominator comprising usage time on Ele.me and Meituan,
the two major food delivery platforms. If the coupon program attracted users from the rival
platform, Ele.me’s share should be elevated during the coupon month relative to comparable
periods without coupon programs. We use August 2023 and November 2023 as comparison
periods, neither of which featured coupon programs. Ele.me’s share was 14.5 percent during
the coupon month (August 2022), compared to 14.7 percent in both comparison periods.
To gauge whether this comparison can detect substitution at the relevant scale, we es-
timate coupon recipients’ share of Ele.me’s user base. Our baseline estimates imply a per-
person, per-day average government subsidy of¥0.76 (Section OA6.1). Dividing total gov-
ernment expenditure on coupon subsidies distributed through the platform (approximately
¥20 million, based on information provided by the platform) by this per-person subsidy over
the 41-day program period yields an estimated 642,000 coupon recipients. The weighted
number of active Ele.me users in Beijing during August 2022 is approximately 2.8 million,
so coupon recipients constitute roughly 23 percent of the platform’s active user base. Under
full substitution, in which all coupon recipients were users who switched to Ele.me from
rival platforms specifically to obtain coupons, their usage time would be absent from Ele.me
in months without the program. Removing their contribution from Ele.me’s coupon-month
total, while holding total food delivery usage constant, would imply a non-coupon usage
share of approximately 11.2 percent (14.5×0.77, where 0.77 = 1−0.23 is the non-recipient
share). If one in four coupon recipients were platform switchers, the predicted non-coupon
share would be approximately 13.7 percent. The observed shares of 14.7 percent in both
August and November 2023 suggest limited scope for cross-platform substitution.
We interpret this evidence as a consistency check rather than a definitive test, since
other forces affecting Ele.me’s market share could mask smaller substitution effects. This
test also relies on the assumption that any coupon-induced platform switching is transitory:
if switchers remained on Ele.me after the program ended, the platform’s share would stay
elevated in non-coupon months and the comparison would not detect substitution.
Beyond cross-platform switching, the coupon program could also have induced offline-to-
online substitution by shifting consumers from in-person dining to food delivery. As a proxy
for interest in offline dining, we examine usage of DaZhongDianPing (DZDP), an offline
restaurant review platform. If such substitution occurred, we would expect a decline in
DZDP engagement during the month with the coupon program. We compute DZDP’s share
of active users across the major food-related apps (Ele.me, Meituan, and DZDP). This share
was 31.6 percent during the month with the coupon program (August 2022), 30.7 percent
one year later (August 2023), and 30.9 percent in November 2023. This stability is consistent
51

with continued interest in offline dining throughout the coupon period. As with the cross-
platform test, we interpret this as a consistency check subject to the same caveats about
confounding trends; together, the two exercises complement the within-platform intensive-
margin evidence in the main text.
OA4 Heterogeneous Consumer Behavior
OA4.1 Bunching Pattern
Figure OA.1. Discount Threshold and Bunching
Notes:This figure plots the transaction-level probability density of order amounts to illustrate strategic consumer
bunching around the program’s minimum spending thresholds. The horizontal axis represents the gross order
amount, and the vertical axis represents the empirical density. A redemption day is defined at the individual-day
level as any day during the program period when a consumer placed at least one subsidized order. The left panel
compares the distribution of order amounts on redemption days (red) against non-redemption days (blue) during
the coupon event period. The right panel serves as a placebo test, comparing the distribution of order amounts
on non-redemption days during the program period (red) against the baseline distribution from the pre-coupon
event period (blue). Vertical dashed lines mark the¥50 and¥100 discount thresholds. The spikes just above these
thresholds on redemption days demonstrate strategic consumer behavior to qualify for discounts. In contrast, no
such bunching appears in the pre-coupon event period or on non-redemption days.
52

OA4.2 Coupon Redemption Patterns by Establishment Type
(a) By Establishment Size
 (b) By Price Level
Figure OA.2. Coupon Redemption Rates Across Establishment Types
Notes:This figure presents the heterogeneity in coupon redemption rates across establishments. Panel (a) groups
establishments by sales revenue (six months prior to the coupon event) and reports the mean coupon redemption
rate within each size decile. Panel (b) groups establishments by average order price (six months prior to the coupon
event) and reports the mean coupon redemption rate within each price decile.
OA4.3 Consumer Characteristics by Non-SME Expenditure Share
Figure OA.3. Coupon MPC by Non-SME Expenditure Share
Notes:This figure presents the average marginal propensity to consume out of coupon subsidies (Coupon MPC)
across quintiles of consumers’ non-SME expenditure share. The horizontal axis groups consumers by their pre-
treatment share of spending allocated to non-SME establishments. The vertical axis reports mean estimated Coupon
MPC within each quintile.
53

OA5 Heterogeneous Treatment Effects: Estimation and Results
OA5.1 Causal Forest Estimation
We implement the causal forest framework of Athey et al. (2019) using thegrfpackage
inR. Following the residual-on-residual orthogonalization procedure outlined in Section 3.2,
we first estimate the nuisance functionsE[∆y i|Xi] andE[Treat i|Xi]. Ingrf, these nuisance
components are estimated automatically using regression forests. As an independent check,
we also estimate them using the Super Learner (Laan et al., 2007) (see Section OA5.2). The
resulting treatment effect estimates are very similar and available upon request.
We then estimate the causal forest using the package’s “honest” procedure (honesty =
TRUE). Under honesty, each tree uses separate subsamples for split selection and for treatment
effect estimation within the resulting leaves, which helps reduce overfitting and supports
valid statistical inference under the conditions in Athey et al. (2019). Hyperparameters are
selected using the automatedtune.parametersroutine, focusing on the number of variables
considered at each split (mtry) and the subsampling fraction (sample.fraction). We set
tune.num.trees = 1,000andtune.num.reps = 200for tuning, and grow the final forest
withnum.trees = 5,000to ensure stable treatment effect estimates.
OA5.2 Alternative Machine Learning Estimators
Our benchmark strategy relies on Neyman orthogonalization to partial out the influence
of covariates from both the outcome and the treatment indicator, allowing us to estimate
the treatment effect directly. Alternatively, we can estimate heterogeneous treatment ef-
fects using a direct approach that jointly learns the relationship between the covariates, the
treatment indicator, and the outcome by modeling a single conditional response surface:
∆yi =µ(X i,Treat i) +ϵ i,(OA.2)
whereµ(X i,Treat i) =E[∆y i|Xi,Treat i]. Once the joint response surface is estimated, the
conditional average treatment effect,α(X i), is extracted by taking the difference in the
predicted potential outcomes for the treated and untreated states:
ˆα(Xi) = ˆµ(Xi,1)−ˆµ(X i,0).(OA.3)
To estimate the joint response surface, we implement the Super Learner framework of
Laan et al. (2007) using theSuperLearnerpackage inR, which is an ensemble machine
learning algorithm that optimally combines predictions from a set of candidate models. By
utilizing cross-validated weighting, it ensures that the ensemble prediction minimizes overall
cross-validated risk.
54

Specifically, our candidate models include a standard linear model (SL.lm), a generalized
additive model (SL.gam), a kernel-based support vector machine (SL.ksvm), and a random
forest (SL.randomForest). We retain the default hyperparameter configurations for each
candidate model and leverage this direct estimation strategy to calculate ˆα(X i).
Figure OA.4 presents a scatterplot of the predicted conditional average treatment effects
from the direct approach against those from the causal forest benchmark. The clustering
of estimates around the 45-degree reference line demonstrates that the predicted treatment
effects remain consistent across both approaches.
Figure OA.4. Predicted Treatment Effects from Alternative Approaches
Notes:This scatterplot compares the predicted conditional average treatment effects from the direct approach
(vertical axis) against those from the causal forest benchmark (horizontal axis). The solid red line represents the
45-degree line. The clustering of estimates around this line demonstrates that the predicted treatment effects are
consistent across both strategies.
OA5.3 Accumulated Local Effects (ALEs)
We estimate the marginal influence of individual characteristic on the predicted treatment
effect using the Accumulated Local Effects (ALEs) framework of Apley and Zhu (2020),
applied here in a heterogeneous-treatment-effects setting. Let ˆτ(X) denote the bias-corrected
estimate of the treatment effect function obtained by nonparametrically regressing the doubly
robust scoreψ i on covariatesX i. For a given characteristicX k, we compute the accumulated
55

local effect at a specific valuexas:
ALEk(x) =
b(x)X
b=1
1
|Sb|
X
i:Xik∈Sb
[ˆτ(zb,X i,−k)−ˆτ(z b−1,X i,−k)],(OA.4)
where the support ofX k is partitioned intoBintervals, withb(x) denoting the index of the
interval containingx. LetS b represent theb-th interval and|S b|the number of observations
within it. The inner summation aggregates over all observationsifor which the realized
feature value,X ik, falls withinS b, whilez b andz b−1 define the upper and lower boundaries
of theb-th interval, respectively. The vectorX i,−k captures all covariates other thankfor
observationi. Intuitively, ALE aggregates local changes in the predicted treatment effect as
Xk moves across adjacent intervals, while holding the remaining covariates at their observed
values.
We compute ALEs using theimlpackage inR, settinggrid.size = 25so that the sup-
port of each characteristic is partitioned into 25 equal-frequency intervals based on empirical
quantiles. Relative to Partial Dependence Plots (PDPs), ALE has an important advantage
when covariates are correlated. PDPs average predictions over the unconditional distribu-
tion of the remaining covariates and therefore evaluate the model at feature combinations
that may be rare or unsupported in the data. By contrast, ALE computes changes in the
predicted treatment effect over small intervals ofX k, using only observations whose realized
Xk falls in the relevant intervalS b. As a result, the estimated marginal influence ofX k is
based on observed covariate combinations rather than extrapolated values.
OA5.4 Drivers of Treatment Effect Heterogeneity
Figure OA.5 presents variable importance scores from the causal forest estimation, mea-
suring the weighted frequency with which each covariate is selected for splitting across trees.
Consumption habits (spending per order and order frequency), wealth, and neighborhood
consumption amenities emerge as the most important predictors, consistent with the BLP
results in the main text.
56

Figure OA.5. Variable Importance Plot
Notes:This figure displays variable importance scores derived from causal forest estimation. These scores represent
the weighted sum of the relative frequency with which each covariate is selected for splitting at each depth across
all trees in the forest. The final scores are normalized to sum to one.
Table OA.6 reports the full BLP coefficient estimates. Column (1) presents the base-
line specification corresponding to Figure 5 in the main text. Columns (2) and (3) assess
the robustness of the non-SME establishment share, the key supply-side predictor, by con-
trolling for the price composition of local restaurants. Because the program’s two coupon
thresholds are¥50 and¥100, restaurants in higher price tiers may facilitate redemption,
raising the concern that the non-SME share proxies for local price composition rather than
establishment size. Column (2) replaces the non-SME share with two price-tier variables
capturing the share of nearby establishments whose average order price falls between¥50
and¥100, and the share above¥100. Neither is statistically significant, indicating that
local price composition alone does not predict treatment effect heterogeneity. Column (3)
includes both the non-SME share and the price-tier variables. The non-SME share remains
strongly positive and significant, while the price-tier coefficients are positive but statistically
insignificant. Establishment size, not price level, emerges as the primary supply-side driver
of heterogeneous consumption responses in our setting.
57

Table OA.6. Best Linear Projection of Heterogeneous Treatment Effects
(1) (2) (3)
Spending per order (past 6 months) 1.710*** 1.996*** 1.824***
(0.065) (0.068) (0.066)
Number of orders (past 6 months) 0.418*** 0.697*** 0.480***
(0.063) (0.067) (0.064)
Wealth 0.585*** 0.514*** 0.461***
(0.066) (0.070) (0.067)
Platform membership−0.380***−0.331***−0.371***
(0.064) (0.067) (0.065)
Age−0.119*−0.118*−0.109*
(0.064) (0.067) (0.065)
Female−0.244***−0.227***−0.215***
(0.063) (0.067) (0.064)
Number of establishments−0.740***−0.550***−0.705***
(0.065) (0.071) (0.070)
Share of non-SME establishments 0.520*** 0.503***
(0.065) (0.066)
Share of establishments (¥50–100) 0.007 0.005
(0.068) (0.065)
Share of establishments (>¥100) 0.011 0.013
(0.068) (0.065)
Constant 1.958*** 2.179*** 2.047***
(0.061) (0.065) (0.062)
Notes:This table reports the coefficient estimates from the best linear projection (BLP) of the doubly robust score
on the set of observed characteristics. Column (1) includes the baseline characteristics, Column (2) replaces the
share of non-SME establishments with shares of establishments whose average order price (in the six months prior
to the coupon event) is between¥50 and¥100, or above¥100; Column (3) includes both the share of non-SME
establishments and the aforementioned price-tier shares. All continuous covariates are standardized to have a mean
of zero and unit variance, allowing for direct comparison across coefficients as measures of variable importance.
The constant term represents the average of bias-corrected conditional average treatment effects. Robust standard
errors are reported in parentheses. *, **, and *** indicate statistical significance at the 10%, 5%, and 1% levels,
respectively.
58

Figure OA.6 reproduces the ALE curve for average spending per order from Figure 6c,
overlaying the¥50 and¥100 coupon thresholds. Treatment effects begin to rise around the
¥50 threshold and continue increasing above¥100. Section 4.4 discusses the implications
of this pattern for models of consumption behavior. 47
Figure OA.6. Treatment Effects by Spending Level
Notes:This figure reproduces the ALE curve for average spending per order from Figure 6c. The horizontal axis
shows empirical quantiles of average spending per order during the six months prior to the coupon event, and the
vertical axis shows the corresponding marginal effect on the estimated individual treatment effect, centered to have
mean zero. The vertical lines mark the¥50 and¥100 minimum spending thresholds for the “50–15” and “100–30”
coupons, respectively.
To complement the ALE evidence in Figure OA.6, Table OA.7 reports subgroup difference-
in-differences estimates by baseline spending per order. Specifically, we augment the baseline
difference-in-differences specification in Equation (1) by allowing the treatment effect to vary
across three groups defined by average spending per order in the six months before the coupon
event: below¥50,¥50–100, and at least¥100. The estimates show that spending responses
remain substantial among consumers whose baseline spending already exceeds one or both
coupon thresholds, with the largest grouped effect appearing among those above¥100.
47Threshold-based incentives may generate responses not fully captured by standard utility maximization. In
particular, the act of crossing the threshold itself may carry intrinsic utility.
59

Table OA.7. Treatment Effects by Baseline Spending Per Order
Out-of-pocket spending
(1)
Treat×Post×1( ¯Ei <50) 1.591***
(0.619)
Treat×Post×1(50≤ ¯Ei <100) 1.735**
(0.861)
Treat×Post×1( ¯Ei ≥100) 5.883**
(2.575)
Observations 416,570
Notes:This table reports subgroup difference-in-differences estimates based on Equation (1), allowing the treatment
effect to vary across three groups of consumers defined by baseline spending per order. The dependent variable is
daily out-of-pocket spending. Consumers are grouped by their baseline spending per order ( ¯Ei), defined as average
spending per order in the six months before the coupon event, using the program’s minimum-spending thresholds
as cutoffs: below¥50,¥50–100, and at least¥100. Standard errors are clustered at the individual level. *, **, and
*** indicate statistical significance at the 10%, 5%, and 1% levels, respectively.
OA5.5 Spatial Heterogeneity in Digital Coupon Effects
To further explore the geographic variation in consumer responsiveness to the digital
coupon program, we aggregate the estimated individual-level treatment effects into spatial
neighborhoods. Specifically, we divide the Beijing municipality into 3km×3km grid cells
and assign each treated consumer to a cell based on their location. We then calculate the
average conditional treatment effects on the treated within each grid.
60

Figure OA.7. Spatial Distribution of Treatment Effects
Notes:This figure maps the spatial distribution of neighborhood-level average conditional treatment effects across
the Beijing municipality using 3km×3km grid cells. The value for each grid cell represents the mean of the
estimated treatment effects in daily out-of-pocket spending for all treated individuals residing in the grid. Red cells
indicate positive average effects. Blue cells indicate negative average effects. Grids containing only a single treated
individual or those where the average pre-treatment spending was zero are excluded from the visualization. In total,
the map displays 212 valid grids, 203 of which exhibit a positive average treatment effect. Over 6 percent of grids
experienced spending increases exceeding 50 percent, while 33 percent saw gains of less than 10 percent.
OA5.6 Shapley Variance Decomposition of Treatment Effect Heterogeneity
LetX= (D, S, E), whereDdenotes demand-side variables (e.g., wealth),Sdenotes
supply-side variables (e.g., local consumption amenities), andEdenotes variables that may
be influenced by both demand-side and supply-side factors (e.g., consumption habits). As
noted in the main text, consumption habits may reflect equilibrium outcomes shaped jointly
by consumer preferences and local consumption opportunities.
LetV tot ≡Var( ˆαi) denote the variance of the estimated CATEs ˆα(Xi). For each subset
G⊆ {D, S, E}, define
v(G)≡Var(E[ ˆα(X)|G]).
We estimatev(G) by projecting ˆα i onto a fully expanded fourth-degree polynomial in the
variables contained inG, including all interaction terms up to degree four, and then comput-
ing the variance of the fitted values. We do this for all seven nonempty subsets of{D, S, E}:
v(D),v(S),v(E),v(D, S),v(D, E),v(S, E), andv(D, S, E).
These quantities summarize how much of the variation in the estimated treatment ef-
fects can be explained by different combinations of variable groups. However, they do not
by themselves tell us how to allocateV tot acrossD,S, andE, because the incremental
61

contribution of any one group depends on which other groups are already included. For
example, the contribution ofDisv(D) if it enters first,v(D, S)−v(S) if it enters afterS,
andv(D, S, E)−v(S, E) if it enters last. To avoid relying on any single ordering, we use
the Shapley decomposition, which assigns to each group its average incremental contribution
across all possible orderings of entry. With three groups, there are six possible orderings.
Averaging over these orderings yields the Shapley contributionsϕ D,ϕ S, andϕ E:
ϕD = 1 6  2v(D) +  v(D, S)−v(S)  +  v(D, E)−v(E)  + 2  v(D, S, E)−v(S, E)  ,
ϕS = 1 6  2v(S) +  v(D, S)−v(D)  +  v(S, E)−v(E)  + 2  v(D, S, E)−v(D, E)  ,
ϕE = 1 6  2v(E) +  v(D, E)−v(D)  +  v(S, E)−v(S)  + 2  v(D, S, E)−v(D, S)  .
By construction, these contributions sum toV tot. This decomposition is useful in our
setting because demand-side variables, supply-side variables, and consumption habits are
correlated, so the relative importance of any one group cannot be summarized by a single
ordering alone. The Shapley approach provides a symmetric way to apportion the total
variation in estimated treatment effects across the three groups.
Applying this decomposition yieldsϕ D = 4.09,ϕ S = 2.93, andϕ E = 18.10. To summarize
the relative importance of demand-side and supply-side factors, we report two comparisons.
First, we compare demand and supply after excluding consumption habits from both sides.
Under this comparison, the demand share is
ϕD
ϕD +ϕ S
= 58%
and the supply share is 42 percent.
Second, because consumption habits may reflect both demand-side and supply-side forces,
we allocate their contribution equally between the two sides. Under this comparison, the
demand share is
ϕD +ϕ E/2
ϕD +ϕ S +ϕ E
= 52%
and the supply share is 48 percent.
Under both comparisons, demand-side and supply-side factors contribute in broadly com-
parable magnitudes, with the demand side playing a modestly larger role.
OA6 Distributional Consequences and Policy Design
OA6.1 Cost Estimation
To evaluate the fiscal implications of alternative targeting policies, we estimate the gov-
ernment subsidy (cost) associated with treating any given individual. We accomplish this
62

by training a regression forest to predict individual-level coupon redemption costs based on
observed characteristics. The estimation procedure proceeds in three steps.
First, for each individualiin the treatment group, we define the realized cost,C i, as the
average daily coupon subsidy redeemed by individualiduring the treatment period. This
variable represents the exact fiscal outlay incurred by the government for treating individual
i.
Second, we train a regression forest model on the treated users by regressing the realized
cost,C i, on our full set of observed characteristics,X i. We implement this using the package
grffromR, retaining the package’s default hyperparameter settings.
Finally, we apply the trained model to generate predicted costs, ˆCi(Xi), for all individuals
in our full sample. These predictions represent the expected fiscal cost if a given individual
were to receive a digital coupon bundle. For our policy counterfactuals, the total baseline
government budget is subsequently calibrated by summing these predicted costs across all
individuals who are treated during the program.
OA6.2 Impact on Local Businesses
To map individual treatment effects to business earnings, we make two simplifying as-
sumptions. First, we assume no coupon-induced consumption reallocation. Under this as-
sumption, each consumer’s estimated treatment effect is allocated across establishments in
proportion to their observed spending shares during the treatment period. Second, we as-
sume no supply-side adjustment. In particular, establishments do not (a) raise prices, (b)
introduce additional promotions, or (c) change menus in response to the coupon event.
Suppose there areNindividuals andKestablishments. For each individuali, we define
rik as the spending placed by individualion establishmentkin the coupon event period
andp ik =r ik/ P j rij as the corresponding spending share. Letα i be the treatment effect
on buyeri’s total spending (including OOP expenditure and coupon subsidy) andτ k be
treatment effect on sellerk’s total revenue during the coupon event period, and Ψ be the
establishment-level effects we want to recover:
Ψ =


τ1
...
τK

 ,Φ =


α1
...
αN

 ,P=


p11 . . . p1K
... . . . ...
pN1 · · ·pN K

 .
Given the two assumptions, we calculate the change in business revenue for all establish-
ments, Ψ, during the coupon period as Ψ = Φ ′ ·P.
63

OA6.3 Optimal Policy Trees for Coupon Allocation
This section provides technical details on the optimal policy tree method used in Sec-
tion 5.2.2 to evaluate alternative coupon allocation rules. Consider a policymaker who must
decide which individuals should receive a digital coupon. Letπ(X i) :X → {0,1}be a
policy that maps an individual’s observed characteristicsX i to a treatment assignment, and
let Γ i(d) denote the reward from assigning treatmentdto individuali. The policymaker’s
objective is to find the policy that maximizes total reward:
π∗ = arg max
π∈Π
" NX
i=1
Γi (π(X i))
#
,
where Π is the space of admissible policy functions.
Letp i denote consumeri’s spending shares on SMEs (see Section OA6.2). We normalize
the reward from non-treatment to zero, Γ i(0) = 0, and define
Γi (1) = (λ·p i + (1−λ)·(1−p i))·α(X i),
whereα(X i) is the individual treatment effect andλ∈[0,1] governs the weight placed
on SME revenue in the policy objective. This formulation treats coupon-induced spending
at SMEs and non-SMEs as differentially valued by the policymaker. Whenλ= 0.5, the
objective reduces to maximizing the total stimulus. Asλincreases from 0.5 to 1.0, the
policy increasingly favors treating consumers whose spending patterns direct more revenue
toward SMEs. Whenλ= 1, the policy focuses exclusively on SME revenue.
We search for the optimal policy within the class of depth-2 decision trees (Athey and
Wager, 2021). In implementation, we replaceα(X i) with its estimated doubly robust score,
ψi, and solve the policy problem using thepolicy treefunction from thepolicytree
package inR(Athey and Wager, 2021), with the tree depth set to 2. We varyλfrom 0.5
to 1.0, solve for the optimal depth-2 tree at each value, and repeat the exercise under three
alternative SME definitions based on the 20th, 50th, and 86th percentiles of establishment
revenue.
64

OA6.4 Policy Design
Table OA.8. Ranked Average Treatment Effect by Decile
Variable for Ranking 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0
All characteristics 12.39 8.22 6.35 5.25 4.50 3.93 3.46 3.04 2.58 1.80
Spending per order 7.43 5.29 3.84 3.08 2.69 2.39 2.19 2.01 1.87 1.80
Number of orders 4.68 2.54 1.95 2.04 1.94 1.88 1.83 1.84 1.80 1.80
Wealth 4.50 3.27 3.02 2.79 2.52 2.36 2.19 2.04 1.92 1.80
Large establishments 3.90 3.12 2.57 2.32 2.27 2.11 2.01 1.94 1.88 1.80
Number of establishments 2.47 2.54 2.33 2.16 2.09 2.10 2.16 2.10 1.99 1.80
Female 2.00 1.99 2.27 2.21 2.12 2.06 2.05 1.97 1.92 1.80
Platform membership 1.98 1.92 1.92 1.93 1.97 1.99 1.94 1.93 1.89 1.80
Age 1.93 2.33 2.18 2.05 2.10 2.12 2.01 1.95 1.84 1.80
Notes:This table reports the cumulative Ranked Average Treatment Effect (RATE) to evaluate the efficacy of
alternative targeting strategies. Each row denotes one specific strategy, where individuals are ranked in descending
order based on their predicted treatment effect. For the “All characteristics” benchmark (first row), predictions are
derived from the full causal forest model. For the single-characteristic strategies (subsequent rows), predictions are
obtained by projecting the causal forest estimates onto the specified covariate using a one-dimensional Generalized
Additive Model to account for potential nonlinearities. Columns 0.1 through 1.0 denote the cumulative fraction of
the population targeted. The reported estimates represent the accumulated average treatment effect for the entire
targeted subpopulation up to that specific quantile, rather than the marginal effect within an isolated decile bin.
For instance, a value in the 0.1 column represents the average treatment effect achieved when allocating the digital
coupons only to the top 10% most responsive consumers according to that row’s specific predicted ranking. Because
targeting 100% of the population is equivalent to a universal rollout, the estimates in the final column (1.0) naturally
converge to 1.80 across all rows, which corresponds to the ATT.
Table OA.9. Consumer Characteristics by Non-SME Expenditure Quintiles
Mean Difference Standard Error
Expenditure 0 - 20% 80 - 100% of Difference
Age 31.68 32.45 0.77 1.39
Female 0.61 0.65 0.05 0.07
Platform membership 0.11 0.41 0.30 0.04
Wealth -0.22 0.10 0.32 0.13
Number of establishments 27.65 54.14 26.49 3.33
Share of non-SME establishments 0.38 0.54 0.16 0.03
Number of orders (past 6 months) 18.76 58.04 39.29 3.65
Spending per order (past 6 months) 33.25 46.28 13.03 3.15
Notes:This table compares characteristics of consumers with different expenditure patterns across establishment
types. The first column shows mean values for consumers in the lowest quintile of non-SME expenditure share (0-
20%), representing those who predominantly patronize SMEs. The second column shows consumers in the highest
quintile (80-100%), representing those who primarily patronize non-SME establishments. The third and fourth
columns report the differences in means and the associated standard errors.
65

Table OA.10. Tradeoff Between Overall Stimulus and SME Support
Weight on SME 20th Percentile 50th Percentile 86th Percentile
SME non-SME SME non-SME SME non-SME
0.50 48.34 11792.92 739.19 11102.07 4203.70 7638.05
0.60 48.34 11792.92 739.19 11102.07 4203.20 7638.05
0.70 48.34 11792.92 768.73 11055.87 4251.86 7541.98
0.80 182.34 11454.89 1067.00 10120.84 4251.86 7541.98
0.90 218.71 11219.01 1085.37 9986.10 4388.43 6954.43
1.00 279.04 5706.24 1085.57 9956.80 4389.21 6809.37
Notes:This table presents the numerical values (¥) of Figure 10, illustrating the tradeoff between maximizing
total revenue and increasing the SME revenue share. This tradeoff is evaluated by varying the weight parameter
(λ) placed on SME revenue in the targeting algorithm:λ·R SME + (1−λ)·R large, as detailed in Section 5.2.2.
To demonstrate how this tradeoff depends on the size of the targeted group, the table reports outcomes under
three alternative SME definitions. Specifically, an establishment is classified as an SME if its total sales revenue
during the six months prior to the coupon program falls below a specified percentile threshold (the 20th, 50th, or
86th percentile) of the citywide establishment revenue distribution. Establishments above the given threshold are
classified as non-SMEs. The weight parameterλranges from 0.5 (equal weighting between SMEs and non-SMEs)
to 1.0 (exclusive focus on maximizing SME revenue). Asλincreases, the revenue directed to SMEs mechanically
rises, while the revenue directed to non-SMEs and consequently the overall total stimulus declines, highlighting the
fundamental policy tension between aggregate efficiency and small business support. All reported monetary values
represent daily total amounts.
66

References
Apley, D. W. and Zhu, J. (2020). Visualizing the Effects of Predictor Variables in Black Box
Supervised Learning Models.Journal of the Royal Statistical Society Series B: Statistical
Methodology, 82(4):1059–1086.
Athey, S., Tibshirani, J., and Wager, S. (2019). Generalized random forests.The Annals of
Statistics, 47(2):1148–1178.
Athey, S. and Wager, S. (2021). Policy learning with observational data.Econometrica,
89(1):133–161.
De Chaisemartin, C. and d’Haultfoeuille, X. (2020). Two-way fixed effects estimators with
heterogeneous treatment effects.American Economic Review, 110(9):2964–2996.
Goodman-Bacon, A. (2021). Difference-in-differences with variation in treatment timing.
Journal of Econometrics, 225(2):254–277.
Hansen, B. B. and Klopfer, S. O. (2006). Optimal full matching and related designs via
network flows.Journal of Computational and Graphical Statistics, 15(3):609–627.
Laan, M. J. v. d., Polley, E. C., and Hubbard, A. E. (2007). Super Learner.Statistical
Applications in Genetics and Molecular Biology, 6(1):1–21.
Sant’Anna, P. H. C. and Zhao, J. (2020). Doubly robust difference-in-differences estimators.
Journal of Econometrics, 219(1):101–122.
67
