---
title: How does online shopping affect offline price sensitivity?
url: https://arxiv.org/abs/2506.15103
category: consumer-behavior
subcategory: empirical
date: 2025-06
venue: ''
authors:
- Shirsho Biswas
- Hema Yoganarasimhan
- Haonan Zhang
source: arxiv
pdf_url: https://arxiv.org/pdf/2506.15103
pages: 61
chars: 150049
fetched_at: '2026-11-08T13:12:51+00:00'
kb_version: 1
---

# How does online shopping affect offline price sensitivity?

How does online shopping affect offline price sensitivity?
Shirsho Biswas, University of Washington*
Hema Yoganarasimhan, University of Washington
Haonan Zhang, University of Washington
October 3, 2025
Abstract
The rapid rise of e-commerce has transformed consumer behavior, prompting questions
about how online adoption influences offline shopping. We examine whether consumers who
adopt a retailer’s online shopping channels become more price-sensitive in their subsequent
offlinepurchases with that retailer. Using transaction-level data from a large Brazilian pet
supplies retailer operating both online and offline, we compare “adopters”—customers who began
shopping online after a period of offline-only purchasing—with “non-adopters” who remained
offline-only. We estimate a discrete choice logit model with individual-level heterogeneity, based
on an algorithm that can handle both high-dimensional fixed effects and price endogeneity. We
then apply a staggered difference-in-differences approach to the estimated price elasticities and
obtain the Average Treatment Effect on the Treated (ATT). We find that offline price sensitivity
increases significantly after online adoption in three out of four product categories, particularly
in items with low switching costs, such as pet hygiene. These results underscore the importance
of recognizing cross-channel effects in consumer behavior and contribute to the literature on
pricing and multichannel retailing by identifying online adoption as a key driver of offline price
sensitivity.
Keywords:Digital Platforms, High-dimensional fixed effects, Multichannel Retailing, Online Shopping,
Price Elasticity, Pricing
*Authors contributed equally and names are listed in alphabetical order. E-mails: shirsho@uw.edu, hemay@uw.edu,
hzhang96@uw.edu. We thank an anonymous pet supplies retailer for providing the data and for thoughtful discussions on many
aspects of the paper. The opinions expressed in this paper are the authors’ and do not reflect those of the data providers.
1
arXiv:2506.15103v2  [econ.GN]  1 Oct 2025

1 Introduction
Over the past two decades, online shopping has grown rapidly, driven by the widespread adoption of computers
and smartphones. U.S. e-commerce sales more than doubled from $571 billion in 2019 to approximately
$1.19 trillion in 2024, and the share of e-commerce in total US retail sales has grown from 15.4% to 22.7%
over the same period (Haleem 2025). Consumers are increasingly adapting to the convenience of online
shopping and allocating a large portion of their spending to online channels (McKinsey & Company 2023).
This shift has prompted traditional brick-and-mortar retailers such as Walmart, Target, and Costco to increase
investments into their e-commerce channels as a major driver of growth.
Given the rise of online shopping and investments in e-commerce, a natural question that arises for retailers
is whether a consumer’s adoption of a given retailer’s online channels influences her shopping behavior at that
retailer’s physical stores, and if so, how? In this paper, we focus on one important aspect of consumer behavior
– their price sensitivity. Specifically, we seek to answer the following research question: When an offline-only
consumer starts using the online shopping channel(s) of a given retailer, does it affect her offline price
sensitivity (i.e., price sensitivity at that retailer’s physical stores)? If so, does offline price sensitivity increase
or decrease post-online adoption? There are two main reasons why answering this question is important
from both researchers’ and managers’ perspectives. First, from a substantive perspective, understanding the
determinants of price elasticity is important – doing so gives us insights into what factors make consumers
more or less price sensitive, and how. Second, from a managerial perspective, quantifying the spillover effects
of online shopping on offline price sensitivity can have significant implications for retailers’ pricing strategies
and profits. Given the migration of consumers from offline stores to multi-channel shopping, quantifying
the existence and impact of cross-channel externalities can help firms optimize and coordinate pricing and
promotion across channels. More broadly, there is a growing interest among managers in understanding how
interactions and spillovers between online and offline shopping channels shape consumer behavior, given the
growth of omnichannel retailing across the globe (Zhang et al. 2019; Biswas et al. 2024).
While there is a rich literature studying the determinants of price sensitivity, this literature largely focuses
on determinants of price elasticitieswithina channel (see §2 for a detailed discussion). In contrast, our
focus is on the externalities or spilloversacrosschannels. From a conceptual perspective, there are reasons
why we may expect offline price sensitivity to increase post-online adoption as well as reasons that suggest
the opposite. On the one hand, online shopping may make consumers less price sensitive and more brand
loyal because online recommendation systems promote easy repeat purchases and lead to habit formation by
highlighting prior purchases, e.g., “Buy again” or “Frequently purchased items” (Danaher et al. 2003). This
increase in brand loyalty in a retailer’s online channels could spill over to offline shopping occasions and
may make consumers more brand loyal and less price-sensitive in that retailer’s physical stores too (after
adopting online shopping). On the other hand, online shopping makes it easy for consumers to engage in
price comparisons (due to features like sorting by price and lower search costs of browsing through many
options on an app or website). This habit of checking and comparing prices on a retailer’s online channels
can potentially carry over to the retailer’s offline channels, and consumers may become more aware of price
2

differences in the retailer’s physical stores as well. Another potential reason that may make consumers more
price-sensitive after adopting online shopping is that, in many contexts, prices are lower online than offline
(Brynjolfsson and Smith 2000; Cooper 2006). Being exposed to lower prices for the same products online
can make in-store prices seem inflated by comparison, prompting greater scrutiny of the prices of different
brands. Finally, recent research suggests that when consumers are exposed to a wider variety of prices (which
is likely to occur when they adopt online shopping), they become more price-sensitive (Aparicio et al. 2024).
Therefore, the question of whether the adoption of a retailer’s online channels affects consumers’ offline price
sensitivities at that retailer’s physical stores, and if so, in which direction, is an empirical one.
We address this question using data from a large pet supplies retailer in Brazil that sells through both
online and offline channels. The dataset includes detailed transaction-level information for all customers
across both channels from January 1, 2019, to June 30, 2021. In our data, we observe some consumers
who were initially offline-only and then made their first online purchase with the retailer within our data
window, while others remained offline-only throughout. This allows us to track the offline purchases of online
shopping adopters, both pre- and post-adoption, and also all purchases of those consumers who remained
offline only. We focus on four major product categories: dog food, cat food, dog hygiene, and cat hygiene,
which together account for more than 50% of the retailer’s total revenue. These categories are also relatively
frequently purchased and are characterized by a good amount of price variation both across brands and across
time, which allows us to measure individual-level price elasticities at the monthly level.
From an empirical perspective, a key question relates to the estimand of interest and how to measure
it. Note that adopting online shopping is a consumer-level decision, i.e., firms cannot randomly assign
consumers to adopt online shopping. Therefore, we cannot quantify the Average Treatment Effect (ATE) of
adopting online shopping on offline price sensitivity. In addition, even if obtaining the ATE was possible,
firms cannot act on it because they cannot force consumers to adopt online shopping. Therefore, obtaining
the ATE is not only impractical but also lacks actionable implications. Hence, we focus on identifying the
Average Treatment Effect on the Treated (ATT), which captures the impact of treatment on those who adopted
online shopping.
Our empirical strategy consists of two steps. In the first stage, we specify and estimate a discrete choice
logit model for each category, controlling for unobserved customer heterogeneity in brand preferences. In
our model, we allow consumers’ offline price sensitivity to be a function of the extent to which a given
consumer adopts online shopping at a point in time, measured by the cumulative fraction of their online
spending with the retailer up to that point in time.1 This modeling approach allows us to measure the effect of
interest and examine how the price elasticity of consumers who have adopted online shopping diverges over
time from that of those who have not. We encounter two challenges in estimating this demand model. First,
maximum likelihood estimation of a non-linear model, such as the logit model, is quite challenging in the
presence of high-dimensional fixed effects (customer-brand fixed effects in our case). To accommodate these
high-dimensional fixed effects, we build on the Minorization-Maximization algorithm proposed by Chen et al.
1We also include an alternate specification with a binary online adoption variable, as a robustness check.
3

(2022) and allow for covariates that vary by individual, by alternative, and also over time. We then apply
this algorithm to our setting for estimation. To the best of our knowledge, this is the first empirical paper in
marketing to efficiently estimate high-dimensional customer-brand fixed effects in a demand model using
the MM algorithm. Second, we must address potential endogeneity in prices using our observational data
(Nevo 2001). To that end, we use costs as an instrument (Berry 1994) in conjunction with a control function
approach (Villas-Boas and Winer 1999; Petrin and Train 2010). We then use the estimates from this model to
compute customer-month-level price elasticities.
In the second stage, we use the estimated customer-month-level offline price elasticities of adopters
and non-adopters from the first stage to estimate our ATT of interest, which is the effect of adopting online
shopping on consumers’ offline price elasticities. Again, our observational data pose some challenges for the
identification of the ATT. First, consumers in our sample are either treated or untreated in each time period, and
we do not observe their counterfactual outcomes in the unobserved condition (i.e., their behaviors if they had
not adopted online shopping). Moreover, the staggered timing of online adoption among different consumers
requires careful computation and aggregation of treatment effects (Goodman-Bacon 2021; Callaway and
Sant’Anna 2021; Baker et al. 2022). To deal with this, we employ a staggered difference-in-differences (DID)
framework, as proposed by Callaway and Sant’Anna (2021), utilizing the variation in staggered adoption
timing of online shopping. We identify different cohorts of consumers who adopt online shopping (i.e.,
adopters) in each month of our data and compare changes in their behavior to those of a control group of
customers who shop exclusively offline throughout the observation period (i.e., non-adopters).
Our main finding is that consumers becomemoreprice sensitive in their offline shopping trips after
adopting online shopping for three out of four categories. The relative increase in offline price elasticity,
defined as the ATT relative to the pre-adoption average price elasticity of the treated group is heterogeneous
across categories. We find a large effect in the dog and cat hygiene categories (where price elasticity increases
by 72.7% and 34.7%, respectively). We also observe a significant but smaller increase in the dog food category
(8.4%) and no effect for cat food. The heterogeneity across categories can likely be explained by differences
in switching costs to different brands. While pet owners face little risk in trying a new lower-priced hygienic
mat for their pet, changing the brand of food can be much trickier due to the pets’ stronger preferences for
shape, smell, and texture in food, particularly for cats (Nichelason 2024).
We also provide a series of tests and alternative specifications that establish the robustness of our results
and provide additional empirical support for the generalizability of our findings. First, we show that using a
binary online adoption variable in our demand model does not change our conclusions. Second, we also use
Inverse Propensity Weighting (IPW) approaches to control for self-selection of the online adoption decision.
Third, we consider an alternative estimator where later adopter groups serve as a control group for earlier
adopters. Fourth, we consider an alternate definition of purchase occasions to also include online shopping
visits. Our conclusions and substantive findings remain unchanged across all of these robustness checks.
More broadly, we also present some evidence in favor of portability to other settings. For instance, our data
period also includes COVID-19, an exogenous macro-environmental shock. Interestingly, we do not find
4

differences in the adoption effect between customers who adopted online shopping during COVID-19 vs.
those who adopted organically before that, indicating that the effect is not sensitive to the reasons/drivers of a
consumer’s decision to adopt online shopping.
Our paper contributes to the broad literature on online-offline retailing and pricing. From a substantive
perspective, we contribute to the literature on price sensitivity and multichannel retailing by identifying a new
determinant of offline price sensitivity: the adoption of online shopping. We demonstrate that consumers
become more price-sensitive in a retailer’s physical stores after adopting that retailer’s online channels for
shopping. This finding is important and distinct from previous research, which has mainly focused on
cross-sectional or within-household comparisons of price sensitivity between online and offline settings.
From a managerial perspective, our findings have implications for firms’ pricing strategies and profitability,
emphasizing the need for multichannel retailers to account for the online adoption effect (i.e., heightened
offline price sensitivity when consumers adopt a retailer’s online channels) in their pricing decisions.
The rest of the paper is organized as follows. In §2, we discuss the related literature, and in §3, we discuss
the setting and data. In §4, we document descriptive evidence, and in §5, we specify the firm’s problem
and provide an overview of the empirical strategy. §6 presents the demand model, and §7 presents the ATT
estimates of online adoption on offline price sensitivity. §8 discusses the generalizability and robustness
checks of our main results. Finally, in §9, we summarize our findings and their implications, and also discuss
avenues for future research.
2 Related Literature
Our study relates to multiple streams of literature on the determinants of price elasticity, digital platforms,
and multi-channel retailing.
First, our work relates to the large literature in marketing and economics that has focused on documenting
the drivers of consumers’ price sensitivity. Prior research has identified various determinants of price
sensitivity, particularly in grocery settings. These include (1) macroeconomic conditions, such as GDP
growth and inflation rates (Gordon et al. 2013; Tellis 1988; Bijmolt et al. 2005); (2) marketing interventions,
such as advertising (Kanetkar et al. 1992; Kaul and Wittink 1995; Kalra and Goodstein 1998; Jedidi et al.
1999), promotions Mela et al. (1997); Jedidi et al. (1999); Kopalle et al. (1999) and category expansion (Yu
et al. 2021); (3) brand strength (Guadagni and Little 1983; Kamakura and Russell 1989; Guadagni and Little
2008); (4) consumer loyalty (Danaher et al. 2003); (5) time between purchase and consumption (Joo et al.
2020). Early research has also examined the relationship between customer demographic characteristics
– age, education, income, and household size – and price sensitivity using household-level scanner panel
data (Rossi and Allenby 1993; Narasimhan 1984; Bawa and Shoemaker 1987, 1989). However, later studies
have concluded these relationships are generally weak, suggesting that demographics do not explain a large
portion of the variation in household-level price sensitivity (Hoch et al. 1995; Rossi et al. 1996).
We consider the adoption of a given retailer’s online channels as a novel factor that may affect consumers’
offline price sensitivity at that retailer’s physical stores. Given the rise of digitization and online shopping,
this factor can be particularly important for multi-channel retailers (who are increasingly investing in online
5

channels). Existing literature provides some insights into how consumer behavior differs between online and
offline channels. Early studies focusing on cross-sectional comparisons find that consumers exhibit lower
price sensitivity and less brand switching when shopping online compared to offline (Degeratu et al. 2000;
Andrews and Currim 2004). Danaher et al. (2003) shows that high market share brands exhibit greater brand
loyalty online, whereas low market share brands exhibit greater brand loyalty in offline stores. However,
these studies are “cross-sectional” in nature, i.e., they compare the set of consumers shopping offline vs.
those shopping online, who may be very different from each other. More recent research has shifted toward
within-household analysis. For example, Chu et al. (2008) compare price sensitivity in online and offline
grocery shopping within the same household and find that consumers are generally less price-sensitive online.
Further, Chu et al. (2010) investigate the role of household characteristics in moderating price sensitivity
across channels. However, none of this research looks intoifandhowtheadoptionof online shopping affects
consumers’ offline price sensitivity, which is the focus of our paper.
More broadly, our study contributes to the broader multichannel retailing literature; see Cui et al. (2021)
for a comprehensive overview. One key stream of research highlights that online and offline channels can
function as complements (Avery et al. 2012; Wang and Goldfarb 2017; Bell et al. 2018) or substitutes (Forman
et al. 2009; Li 2021; Shriver and Bollinger 2022), depending on the context. Other studies have examined how
digitization affects consumer shopping behavior across channels, focusing on spend patterns and purchase
volume (Wang et al. 2015; Narang and Shankar 2019; Biswas et al. 2024), brand exploration (Pozzi 2012),
and purchase variety (Chintala et al. 2023). Building on this body of work, our study provides new insights
into multichannel strategy (Neslin 2022) by investigating changes in offline price sensitivity when consumers
adopt a retailer’s online channels for shopping.
3 Setting and Data
3.1 Setting
We use data from a leading pet supplies retailer in Brazil. This firm operates in a multichannel environment,
with over 200 brick-and-mortar stores nationwide and a digital presence through both a mobile app and an
e-commerce website. The retailer offers a broad selection of pet-related products, including food, medicines,
hygiene and grooming items, toys, and accessories. To track consumer purchases across online and offline
channels, the retailer uses Brazil’s National Identification Number, which provides a unique identifier for
each customer. Online purchases - whether through the app or website - require customers to log into their
accounts, making all such transactions traceable to individual IDs. For brick-and-mortar purchases, customers
provide their ID at checkout, although it is not mandatory. According to the retailer, around a quarter of
offline transactions are not associated with a customer ID, and this rate has remained stable throughout the
study period.2
The dataset spans 30 months, from January 1, 2019, to June 30, 2021, and covers all transactions (online
and offline) linked to identifiable customers. Each transaction includes a unique order ID and detailed
2The fact that this rate has remained stable despite the fact that there was a spike in online shopping adoption during COVID-19
reassures us that the adoption of online shopping does not affect it.
6

product-level information, such as price, quantity, brand, category (e.g., dry food or hygiene), and purchase
channel.
3.2 Dataset Construction
We now discuss how we construct the dataset used for our empirical analysis.
Selection of Product Categories:We focus on the four top-selling non-medical categories: Dry Dog Food,
Dry Cat Food, Dog Hygiene (i.e., Hygienic Mats), and Cat Hygiene (i.e., Sands). These categories account
for more than 50% of the focal retailer’s revenue (see Table 1). Products within these four major categories
are generally measured in comparable units, allowing us to construct brand-level prices per unit.
We exclude certain categories from our analysis. First, we exclude medical products such as prescription
drugs and anti-flea medication (second category shown in Table 1) because many products in this category
require a doctor’s prescription and purchase does not depend solely on consumers’ preferences. Further,
medical products can be quite differentiated and target specific ailments, and as such, do not serve as natural
substitutes for each other. Second, we exclude all small categories that account for less than 3% of the total
sales revenue during the observation period, e.g., snacks and toys. Products in these categories are often
unique, serve diverse functions, and are not necessarily natural substitutes for each other.
Table 1: Top Categories Ranked By Total Sales (Offline and Online) During the Observation Period.
Category Share of sales(%) Cumulative share (%)
Dry Dog Food 32.62 32.62
Medical 12.18 44.80
Dry Cat Food 9.41 54.21
Dog Hygiene 5.48 59.68
Cat Hygiene 3.62 63.30
Selection of Brands and Stock Keeping Units (SKUs):Each category contains a large number of pack sizes
and SKUs per brand. First, within each category, we focus on specific pack size(s) to ensure that the price
variation for each brand is captured accurately – this avoids the need to aggregate price movements across a
number of different pack sizes. Focusing on a narrow set of pack sizes to study brand choice within a category
is common in the brand choice literature (e.g. Allenby and Rossi (1998); Kim et al. (2002); Chintagunta
et al. (2005); Dub´e et al. (2010)). The pack sizes we select for each category are as follows: 15KG for dry
dog food, 10 KG for dry cat food, 80cm × 60cm 30-piece mats for dog hygiene, and silica cat sand (1.6KG,
1.8KG, and 2.0KG) for cat hygiene. We provide a detailed discussion of the reasons for selecting these pack
sizes in Web Appendix§A.1.1.
Next, we aggregate SKUs to the brand level and estimate consumer preferences and price elasticities at
the brand level for each product category, similar to Hitsch et al. (2021); Gordon et al. (2013). Specifically,
we follow a two-step process for each category. First, for each category, we select the top-selling brands and
SKUs that are comparable in usage and are substitutes for each other. Next, we aggregate prices and costs
(our instrumental variable to deal with price endogeneity) to the brand level from the SKU level, following
the approach described in Hitsch et al. (2021). We provide details on both these steps in Web Appendix §A.1.
7

Selection of Customers:Following the standard approach in the brand choice literature (Kim et al. 2002;
Chintagunta et al. 2005; Dub´e et al. 2010), for each category, we restrict our sample to only those consumers
who only purchase the specific pack size of interest for that category (as defined earlier), without switching to
any other pack sizes within the same category. This is so that we are able to fully capture these customers’
substitution patterns within the category. Next, given that our goal is to investigate the effect of consumers’
adoption of online shopping at a given retailer 3 on theirofflineprice sensitivity at that retailer’s physical
stores, we need to ensure that we have sufficiently long pre- and post-adoption periods for each adopter in
our sample to effectively measure price elasticities pre- and post-adoption. Therefore, we focus on customers
who adopt online shopping with the retailer in the middle of our observation period, i.e., July 1st, 2019 –
June 30th, 2020. So our 30-month data period is divided into three phases: a pre-adoption period (January
1st, 2019 – June 30th, 2019) when all adopters are in their pre-adoption phase, an adoption period (July 1st,
2019 – June 30th, 2020) during which time the adopters in our sample make their first online purchase, and
a post-adoption period (July 1st, 2020 - June 30th, 2021), when all the adopters in our sample are in their
post-adoption phase. To clarify, a given adopter’s pre- and post-adoption phases are defined as the months
before and after they make their first online purchase. Non-adopters only shop offline through the entire data
period.4
We now outline the criteria used to select adopters and non-adopters for each product category below.
Adoptersin a given category must satisfy the following criteria:
• Made their first-ever online purchase (in any product category, not just the focal category) between July
1st, 2019, and June 30th, 2020.
•Made at least one offline purchase in the focal category both before and after online adoption.
Overall, this gives us 12 cohorts of adopters, where each cohort represents the month in which the user
adopted online shopping. For example, the first cohort of adopters consists of users who adopted online
shopping during July 2019 while the twelfth cohort consists of users who adopted online shopping during
June 2020. Figure A1 in Web Appendix A.1.3 shows stylistic examples of users in different cohorts. Figure
1 shows the number of adopters across the different periods in each category. Notice that there is a spike
in the number of adopters during March–April 2020, which is likely driven by the onset of the COVID-19
pandemic. Our analysis is agnostic to the reasons for adopting online shopping, and in our empirical analysis,
we will allow for the possibility that these cohorts may be different from earlier/later cohorts.
Non-adoptersin a given category must meet the following criteria:
•Did not make any online purchases at any point during the entire observation period.
• Made at least one offline purchase in the category during both the pre-adoption (i.e., January 1st, 2019 –
June 30th, 2019) and the post-adoption periods (i.e., July 1st, 2020 – June 30th, 2021).
Estimation Sample Construction:For each customer in a given category (both adopters and non-adopters),
3“Adoption of online shopping” refers to a customer making his/her first online purchase with the focal retailer inanycategory, and
not just one of the four focal categories.
4Note that we also verified with the retailer that the identified adopters and non-adopters in our data did not adopt online shopping
before our data period begins.
8

Figure 1: Sample Sizes of Adopters by Cohorts and Product Category. Corresponding sample sizes for each cohort are shown in
Table A1 in Web Appendix A.1.3.
(a) Dry Dog Food
 (b) Dry Cat Food
(c) Dog Hygiene
 (d) Cat Hygiene
we organize the data into a panel that captures purchase occasions and brand choices for individual customers
over time. Specifically, we define purchase occasions at the customer-month level. If a customer visits a
physical store of the retailer during a month and purchases in any category (not limited to the categories
we focus on in this study), that customer-month is included as a purchase occasion for all four categories.
If a customer makes no purchases in any category during the month, that customer-month is not included
as a purchase occasion. In other words, a purchase occasion represents any customer-month during which
we observe any offline interaction with the retailer (similar to week-store visit in Gordon et al. (2013)). 5
This approach of using purchase occasions to construct the estimation sample is standard in the demand
5Based on our definition of purchase occasion, if a customer visits multiple times in a month, it is treated as one purchase occasion.
In our data, customers, by and large, do not purchase from more than one store in a month. More than 96% of customer-month-level
purchase occasions involve purchases from a single store. When we process the choice data for each category, for the minor fraction
of purchase occasions that involve more than one store, we label these customer-month purchase occasions with the store where the
customer spent the most within that category during the month so that each customer-month level purchase occasion is associated
with a single store.
9

estimation literature studying brand choice using household level data, since it allows researchers to focus on
modeling brand choice and purchase incidence in a category conditional on a store visit, instead of modeling
the decision of when to go to the store or which store to visit (Chib et al. 2004; Chintagunta et al. 2005;
Dub´e et al. 2010; Gordon et al. 2013). Following the standard practice in the literature, we do not model the
channel choice decision explicitly for a couple of reasons – (a) channel choice can depend on multiple factors
that we do not observe (e.g. transportation costs, distance to stores, consumer expectations of prices etc.); (b)
we would need to impose a structure on the order of store choice, channel choice and brand choice and it is
ex-ante not clear in which order consumers make these decisions. Given that our focus is on documenting
the empirical effect of the adoption of online shopping on price sensitivity in offline brand choice decisions,
modeling the arrival of purchase occasions is neither central nor necessary to answer our research question.
Further, in§8.2.4, we show that our results are robust to alternative definitions of purchase occasions.
For each purchase occasion, we identify the brand chosen by the consumer as the brand that has positive
spend.6 If the customer does not have positive spend on any brand during a purchase occasion, we label it as
choosing the outside option (i.e., “no-purchase”).
3.3 Summary Statistics
We now present some summary statistics on the estimation sample.
First, we find that there are systematic differences in the demographics (age, income, and gender) of
adopters and non-adopters across all four categories. Across all categories, women tend to adopt online
shopping more than men. Additionally, online adopters tend to be younger and from higher-income house-
holds. This makes intuitive sense because younger and higher-income consumers are often more familiar
with online technology and seek time-saving and convenient shopping options. Details of these demographic
characteristics are shown in Web Appendix§A.2.
Next, Table 2 summarizes the category-level statistics, including the number of brands, sample sizes for
adopters and non-adopters (as defined above), the total number of purchase occasions, and the number of
purchase occasions that contain a brand purchase within each category.
Table 2: Summary Statistics By Category
Dry Dog Food Dry Cat Food Dog Hygiene Cat Hygiene
Number of Brands 8 4 4 4
Number of Adopters 2,410 1,037 2,214 1,192
Number of Non-Adopters 7,938 2,297 3,582 2,725
Number of Purchase Occasions 136,411 45,443 78,253 55,410
Purchase Occasions with a Category Purchase 99,233 27,623 40,183 42,596
6We rarely observe customer-month purchase occasions that involve a purchase of more than one brand. All product categories
have fewer than 0.86% of total purchase occasions (e.g., including those with multiple visits to a single store in a month, visits to
multiple stores and a single visit) with multiple brand purchases. For these few purchase occasions with multiple brand purchases,
we assign the brand with the largest spend for that customer during the month, similar to previous brand choice literature, e.g.
Erdem and Keane (1996). Some researchers have handled this issue differently, for instance, by having each brand chosen count as
an independent single-brand purchase occasion (Krishnamurthi and Raj 1988; Chib et al. 2004). Since the fraction of purchases is
so small, we do not think this decision makes a material impact on our results.
10

Table 3: Summary Statistics of Prices and Costs
Dry Dog Food Dry Cat Food Dog Hygiene Cat Hygiene
Mean Price 10.17 11.89 2.28 12.25
SD Price 2.82 2.40 0.28 2.46
Mean Cost 6.29 8.04 0.96 4.95
SD Cost 2.32 3.39 0.29 1.54
Finally, in Table 3, we show some summary statistics of the prices and costs for each category. Specifically,
we show the mean and standard deviation (SD) of the brand price (or cost) per pack size unit (e.g, KG or
piece) for each category, for the estimation sample. These values are calculated by averaging across all
purchase occasions and brands. Specifically, the mean price for category c is calculated as: Mean Pricec =
1
Nc
1
Jc
PNc
t=1
PJ
j=1 Pricejt where Pricejt is the price of brand j on the purchase occasion t. Nc is the total
number of purchase occasions in category c, and Jc is the number of brands of category c. The standard
deviation is computed as SD Pricec =
q
1
Nc
1
Jc
PNc
t=1
PJ
j=1(Pricejt −Mean Price c)2. The mean cost and
SD cost are defined similarly.7 Overall, we see that the data contain significant price and cost variation for
each category. This variation is important and helps us estimate price elasticities.
4 Descriptive Analysis
We now present some descriptive analysis that examines if/how the adoption of online shopping with the
retailer changes consumer behavior during their offline shopping trips at the retailer’s physical stores in the
post-adoption period. Specifically, we focus on two variables that can capture changes inwithin-customer
offline price sensitivity:
• Price Paid: Conditional on making an offline purchase in the focal category, do adopters shift toward
lower-priced after online adoption (compared to non-adopters)?
• Category Purchase Frequency: Conditional on an offline purchase occasion (as defined earlier), do
adopters purchase the focal category less frequently after they adopt online shopping, compared to
non-adopters?
4.1 Price Paid
We examine how the prices paid by adopters change after online adoption (compared to non-adopters). To that
end, we focus on all offline purchase orders (made by adopters and non-adopters) that contain a focal category
purchase and estimate the following two-way fixed-effects regression for each category at the customer-order
level:
ln(Price Paid)it =δ× I{Adopteri} × I{t≥Tadopt i }+Customer i +YearMonth t +ϵ it,(1)
where I{Adopter i} is an indicator variable which is 1 for adopters and 0 for non-adopters. T adopt i is the
adoption time of customer i, and I{t≥T adopt i } is an indicator which is 1 if the order t is during customer i’s
7All price and cost figures are inflation-adjusted. Brazil exhibited significant inflation during our study period, and adjusting for
inflation is crucial to reflect the real price changes. The adjustment is relative to the first observation period, January 2019.
11

Table 4: Two-Way Fixed Effects Model Estimates – ln(Price Paid)
Dependent Variable: ln(Price Paid)
Dry Dog Food Dry Cat Food Dog Hygiene Cat Hygiene
Model: (1) (2) (3) (4)
Variables
I{Adopter i} × I{t≥Tadopt i }-0.0102 ∗ -0.0106∗∗ -0.0046 -0.0160 ∗
(0.0040) (0.0038) (0.0030) (0.0063)
Fixed-effects
Customer Yes Yes Yes Yes
YearMonth Yes Yes Yes Yes
Fit statistics
Observations 99,233 27,623 40,183 42,596
R2 0.89566 0.70460 0.62699 0.66927
Within R2 0.00030 0.00065 0.00012 0.00074
Clustered (Customer & YearMonth) standard-errors in parentheses
Signif. Codes: ***: 0.001, **: 0.01, *: 0.05
post-adoption period. We also include customer-fixed effects, Customeri, to measure the within-customer
change, and time-fixed effects, YearMontht, to control for time-specific unobserved shocks. A negative δ
indicates that adopters, on average, pay lower prices or shift towards the lower end of the price distribution
after adopting online shopping, relative to non-adopters. A positiveδwould indicate the opposite.
Table 4 presents the within-customer changes in the prices paid by adopters relative to non-adopters,
controlling for customer and date fixed-effects. Across all product categories, we see that adopters pay lower
prices offline after they adopt shopping online in the retailer, compared to non-adopters. Further, three of the
categories show a statistically significant effect at the 5% level of significance. In Web Appendix B Table A3,
we repeat this analysis with the percentile of price paid as the dependent variable (instead of ln(Price Paid))
and find consistent results – customers shift towards lower-priced products during their offline purchases
after adopting online shopping. Together, these results suggest that, conditional on purchasing, consumers
are paying lower prices, possibly because they are more price-sensitive.
4.2 Category Purchase Frequency
Next, we examine how the frequency of adopters’ purchase of a given category in the offline channel
changes compares to non-adopters. Specifically, during each offline purchase occasion, we construct a
binary dependent variable, I{BuyCategoryit}, which equals 1 if customer i buys the focal category in
purchase occasion t, and 0 otherwise. We then estimate the following two-way fixed effects regression at the
customer-month purchase occasion level:
I{BuyCategoryit}=δ× I{Adopter i} × I{t≥Tadopt i }+Customer i +YearMonth t +ϵ it (2)
12

Table 5: Two-Way Fixed Effects Model Estimates - BuyCategory
Dependent Variable: BuyCategory
Dry Dog Food Dry Cat Food Dog Hygiene Cat Hygiene
Model: (1) (2) (3) (4)
Variables
I{Adopter i} × I{t≥Tadopt i }-0.0751 ∗∗∗ -0.0497∗∗∗ -0.0617∗∗∗ -0.0654∗∗∗
(0.0077) (0.0109) (0.0075) (0.0106)
Fixed-effects
Customer Yes Yes Yes Yes
YearMonth Yes Yes Yes Yes
Fit statistics
Observations 136,411 45,443 78,253 55,410
R2 0.30479 0.25032 0.23015 0.26662
Within R2 0.00147 0.00066 0.00113 0.00121
Clustered (Customer) standard-errors in parentheses
Signif. Codes: ***: 0.001, **: 0.01, *: 0.05
As before, we include customer and year-month fixed effects. The coefficient δ captures the change in the
probability of buying the category for adopters relative to non-adopters after adoption.
Table 5 shows the results on this estimation. We find that, conditional on a purchase occasion, adopters
purchase dog food and cat food 7.5% and 5.0% less frequently than non-adopters in the offline channel
after they begin using the retailer’s online channel. Similarly, adopters buy dog and cat hygiene 6.2% and
6.5% less frequently than non-adopters, respectively. These findings suggest that, compared to non-adopters,
adopters are more likely to choose the “no-purchase” option when they start shopping online.
In summary, both the descriptive analyses suggests that consumers are less likely to buy the focal category
offline and when they do buy, they pay lower prices, on average. Together these findings provide some
suggestive evidence for potentially higher offline price sensitivity after online adoption. In the next few
sections, we build on these findings and estimate customer-level price elasticities as a function of their online
adoption status and then quantify the effect of online adoption on offline price elasticities.
5 Firm’s Problem and Overview of Empirical Strategy
The primary objective of the firm is to quantify the causal effect of consumers’ adoption of its online channels
on their offline price sensitivity at its physical stores, compared to consumers who shop exclusively offline.
However, quantifying this impact presents both methodological challenges and limited managerial relevance
for several reasons.
First, adopting the online channel is a consumer-level decision, and firms cannot randomly assign
consumers to adopt the online channel or remain offline-only through field experiments. This makes it
impossible to directly measure the Average Treatment Effect (ATE) of online adoption on consumers’ offline
price sensitivity. Second, although firms could implement an intent-to-treat (ITT) design - such as randomly
offering incentives to some offline-only consumers to encourage their online adoption - this approach still
13

does not give us ATE given that some consumers would never adopt online 8.Third, even if a firm could
somehow identify a significant effect of adopting online shopping on consumers’ offline price sensitivity, it
cannot force consumers to choose a specific channel. Therefore, obtaining the ATE is not only impractical
but also lacks actionable implications. Instead, the main quantity of interest for the firm is the change in
offline price sensitivity among consumers who adopt online shopping compared to those who continue to
shop exclusively offline i.e. the Average Treatment Effect on the Treated (ATT). Measuring this would help
firms adjust their offline pricing strategies in response to their customers adopting online shopping. Thus, our
goal is to identify the ATT of online adoption on offline price sensitivity.
We adopt a two-step empirical strategy to solve this problem:
• First, we measure category-level own-price elasticities at the customer-month level: In §6, we use a
logit brand choice model where each consumer’s price sensitivity coefficient varies with the extent
of their online spending and include customer-brand fixed effects. To address price endogeneity, we
use the control function approach (Petrin and Train 2010), using wholesale cost as an instrument. To
efficiently estimate the model given a large number of customer-brand fixed effects, we implement a
Minorization-Maximization (MM) algorithm for the logit model (Chen et al. 2022).
• Next, we use the estimated elasticities in the first step to measure the change in offline price elasticities
due to online adoption. In §7, we use a staggered difference-in-differences approach (Callaway and
Sant’Anna 2021) to estimate the ATT of online adoption on offline price elasticities after accounting for
differences in the timing of adoption between different adopter cohorts.
6 Demand Model
6.1 Choice Model and Utility Specification
For each category, we use a logit model of brand choice (Guadagni and Little 1983; Chintagunta et al. 1991)
to estimate offline price elasticities at customer-brand-month-level.9 Suppose that for a given category, there
are J brands indexed by j= 1,2, . . . , Jplus an outside option indexed by 0. The utility that consumer i
obtains from choosing brandjduring offline purchase occasiontis given by 10:
Uijt =α 0Pricejt +α 1cumPercOnlineSpendit +α 2Pricejt ×cumPercOnlineSpend it
+α 3I{BuyPrevOccaijt}+δ ij +ϵ ijt ∀j∈ {1, . . . , J}
(3)
In this utility specification, Pricejt is the price of brand j during purchase occasion t. We allow a con-
sumer’s price sensitivity coefficient to depend on their cumulative percentage of online spending, denoted
8We do not obtain ATE under the ITT design, since the causal quantity obtained from 2SLS estimators represents the Average Causal
Response, which is a weighted sum of individual treatment effects where weights are compliance scores; For more details, see
Angrist and Imbens (1995); Syrgkanis et al. (2019); Chen et al. (2024); Mummalaneni et al. (2025).
9As discussed in §3.2, we follow the standard approach in the brand choice literature and focus on the brand choice decision
conditional on purchase occasion, and do not model the channel choice decision or the arrival of purchase occasions. Nevertheless,
we note the results are robust to alternative definitions of purchase occasion; see §8.2.4 and Web Appendix§E.6.
10Here, we use a single index t to denote a purchase occasion, which contains both the time (YearMonth) and store information
associated with the purchase occasion.
14

as cumPercOnlineSpendit. This variable represents the proportion of the customer’s total spending with the
retailer that has occurred online up to the purchase occasion t since their first transaction with the retailer.
We use this continuous variable to allow for variation in the online adoption effect based on theextentof a
consumer’s online spend. We also consider an alternate specification where we use a binary online adoption
indicator in §8.2.1. The coefficient α0 represents the baseline price sensitivity for purely offline customers.
The interaction coefficient α2 reflects how price sensitivity changes as consumers spend more online. A
negative α2 would suggest that higher online spending share leads to greater offline price sensitivity.11 The
variable I{BuyPrevOccaijt} is an indicator that equals 1 if customer i purchased brand j at the previous
purchase occasion t−1 , and 0 otherwise, capturing state dependence via α3. The customer-brand fixed
effects δij capture consumer i’s time-invariant preference for brand j. These fixed effects capture systematic
time-invariant consumer-level heterogeneity in brand preferences. However, including these high-dimensional
fixed effects introduces some estimation challenges which we discuss in §6.3. The termϵijt is an idiosyncratic
error term. Finally, the utility of choosing the outside option is normalized as Ui0t = 0 +ϵi0t where ϵi0t also
follows an i.i.d. Type I extreme value distribution.
6.2 Price Endogeneity
A common challenge in estimating price elasticities with observational choice data is price endogeneity. This
issue arises when the error term, ϵijt, contains some time-varying unobserved demand shocks that may be
correlated with prices; e.g., if promotions or advertising are correlated with prices. To address this, we apply
the control function approach for two endogenous variables, Pricejt and Pricejt ×cumPercOnlineSpend it
(Petrin and Train 2010; Wooldridge 2015). We use the weighted wholesale cost indices for each brand j
(constructed as described in §3.2), Costjt, as the instrument. Intuitively, cost is correlated with a brand’s
price but not correlated with unobserved demand shocks, and it is a standard instrument for correcting price
endogeneity in the demand estimation literature (Berry et al. 1995; Berry and Haile 2021).
To obtain control functions for two endogenous variables, we run the following two regressions and
obtain the residuals; see (Aparicio et al. 2024) for a similar use case of this approach.12
Pricejt =γ 1Costjt +Brand j +Store t +YearMonth t +ξ (1) jt (4)
Pricejt ×cumPercOnlineSpendit =γ 2Costjt +γ3Costjt ×cumPercOnlineSpendit +γ ′ 4Controlijt +ξ (2) ijt (5)
Here, Controlijt is a vector of control variables (e.g.,cumPercOnlineSpendit,I{BuyPrevOcca ijt},Customer i,
Brandj,YearMontht). Next, following Petrin and Train (2010), the original error term in the utility specifica-
11Interaction terms in logit and other nonlinear models are best interpreted via marginal effects or elasticities (Ai and Norton 2003).
12Alternatively, some earlier work has suggested that a more parsimonious way to deal with the interaction term between an
endogenous regressor and an exogenous variable is to estimate first-stage regression for price in Equation(4) and add the fitted
residuals as an additional regressor in the model equation, without the need to add another first stage regression deal with the
interaction term between price and online share (Ebbes et al. 2016). We also consider this alternative approach and find that the
results remain consistent with our main findings. Please see Web Appendix§E.7 for details.
15

tion,ϵ ijt, can be decomposed as follows:
ϵijt =λ 1CF Pricejt +λ 2CF Price cumPercOnlineSpendijt + ˜ϵijt (6)
where ˜ϵijt is assumed to follow i.i.d. Type I extreme value distribution. We then include two control functions
into the utility equation as additional regressors, which is now given by:
Uijt =α 0Pricejt +α 1cumPercOnlineSpendit +α 2Pricejt ×cumPercOnlineSpend it
+α 3I{BuyPrevOccaijt}+δ ij +λ 1CF Pricejt +λ 2CF Price cumPercOnlineSpendijt + ˜ϵijt
=ψ ijt + ˜ϵijt ∀j∈ {1, . . . , J},
(7)
where ψijt is the deterministic part of the utility term and ψi0t = 0for the outside option. Under the Type I
extreme value assumption for ˜ϵijt, the probability that consumer i chooses brand j at shopping occasion t is
given by the following formula:
P rijt = exp(ψijt)PJ
j′=0 ψij′t
(8)
Let ψit = (ψi0t, ψi1t, ψi2t, . . . , ψiJt )∈R J+1 be the vector of nominal utilities andyit = (yi0t, yi1t, . . . , yiJt )∈
RJ+1 be the binary choice outcomes for consumer i at shopping occasion t, with yijt = 1if consumer i
chooses brand j at shopping occasion t and 0 otherwise. The likelihood of consumer i at purchase occasion t
is given by:
l(ψit;y it) =
JY
j=0
(P rijt(ψit))yijt (9)
The log-likelihood function over all consumers and purchase occasions can be written as
L(θ) =
NX
i=1
X
t∈Ti
logl(ψ it;y it)(10)
where Ti is the set of purchase occasions associated with customer i. The parameter vector of interest is
θ={α 0, α1, α2, α3, λ1, λ2,{δ ij}i=1,...,N;j=1,...,J }. Note that this is a high-dimensional parameter vector –
in addition to population parameters such as αs and λs, we also have customer-brand fixed-effects (δijs),
which scale with the sample size.
6.3 Estimation
Our main estimation strategy follows the standard two-step approach used in control function approaches;
see (Petrin and Train 2010) for details. However, the key additional challenge in our setting arises from the
presence of high-dimensional customer-brand fixed effects. While high-dimensional fixed effects generally
allow for more flexible substitution patterns (Jiang et al. 2025), doing so complicates the estimation procedure.
We now discuss both the overview of our estimation strategy and also provide a summary of the solution
concept that we adopt to address the high-dimensional fixed-effects.
16

First, we run OLS regressions forPricejt in Equation (4) and Pricejt ×cumPercOnlineSpendit in Equation
(5), respectively. We then obtain the residuals, CF Pricejt and CF Price cumPercOnlineSpendijt, which
serve as control functions. Second, we include these residuals as additional regressors in the logit model
(i.e., Equation (7)). In a standard setting, estimation can proceed as usual at this stage. However, since we
have a large number of customer-brand fixed effects (δij), standard maximum likelihood estimation becomes
computationally infeasible. To overcome this, we adopt a Minorization-Maximization (MM) algorithm
for the logit model with fixed effects, an efficient estimation method proposed by Chen et al. (2022). The
MM algorithm transforms the non-linear optimization problem (i.e., MLE estimation) into a sequence of
simpler problems by iteratively constructing and maximizing a surrogate transfer minorization function S(·)
that minorizes the log-likelihood (James 2017). The transfer minorization function S(·) is less than the
log-likelihood function everywhere except at the current best guess of the parameters, where it is equal. Chen
et al. (2022) derives a transfer minorization function for the standard multinomial logit model in which there
are no alternative-specific time-varying covariates in the utility function. In the theorem below, we extend
their proof to cover a fully flexible logit model with covariates that may vary by individual, by alternative
(brand), and over time. 13 We then derive the corresponding transfer minorization function S(·) for the
log-likelihoodL.
Theorem. Let L(θ) be the log-likelihood of the logit model, defined as in Equation (10). Let S(θ;θ (k)) be
defined as:
S(θ;θ (k)) =L(θ(k)) +1 2 X i,j,t hj(ψ(k) it ;y it)2 − 1 2 X i,j,t [ψ(k) ijt +h j(ψ(k) it ;y it)−ψ ijt]2,(11)
where
hj(ψ(k) it ;y it) = ∂logl(ψ (k) it ;y it) ∂ψ (k) ijt =y ijt −P rijt(ψ(k) it )(12)
ψ(k) it = (ψ(k) i0t , ψ(k) i1t , ψ(k) i2t , . . . , ψ(k) iJt )(13)
Here, hj(ψ(k) it ;y it) is the jth entry of the gradient vector of log-likelihood with respect to the nominal utility
of alternative j, ψ(k) ijt . ψ(k) it denotes the vector of nominal utilities for consumer i at iteration k. Then, the
functionS(θ;θ (k))is a transfer minorization ofL(θ).
Proof.See Web Appendix C.1.
Based on the Theorem 1 and proof from Chen et al. (2022), the iterative sequenceθ(k+1) = arg maxθ S(θ;θ (k)),
k= 0,1, . . . ,converges to a local, if not global, maximum ofL(θ).14
Equation (11) is a second-order Taylor expansion of the log-likelihood function atθ(k). The model param-
eters we are searching over in the iterative MM algorithm (θ, rather than θ(k)), appear only in the third term.
13While our paper was the first to present this extension and proof for this specific case, in a recently posted update, Chen et al.
(2025) present a similar extension.
14For more details, please refer to the proof of Theorem 1 in Chen et al. (2022), which shows the convergence of this iterative
estimator to the true parameters.
17

Because the only term in S(θ;θ (k)) that depends on θ is the sum of squared residuals, maximizing S(θ;θ (k))
is equivalent to minimizing this least squares objective, and the coefficients can be obtained by regressing
ψ(k) ijt +hj(ψ(k) it ;y it) on the vector of explanatory variablesxijt ={Price jt,cumPercOnlineSpend it,Price jt ×
cumPercOnlineSpendit,I{BuyPrevOcca ijt},CF Pricejt,CF Price cumPercOnlineSpendijt, δij} in the util-
ity function. This linearization enables us to apply standard panel data methods despite the large number
of fixed effects δij. Moreover, another advantage of using the MM algorithm to estimate the logit model
is that for customer-brand pairs with few or no purchases, maximum likelihood estimation formally drives
δij toward −∞, so that the predicted choice probability is exactly zero. In practice, this boundary solution
is numerically unstable. The MM algorithm we employ circumvents this by iteratively solving a series of
linearized regressions: never-chosen customer-brand pairs converge to large negative but finite estimates,
which approximate the boundary solution while preserving numerical stability. Thus, the algorithm can
include all (i, j)pairs without manual dropping, effectively regularizing the fixed effects associated with rate
or absent choices.
In summary, the MM-based estimation algorithm that we employ is as follows:
•Initialization: Set the initial parameter estimatesθ (0) including all customer-brand fixed effects as zero.
•Iterative Steps:
1. Minorization step: Givenθ (k), calculateh j(ψ(k) it ;y it)and obtainψ (k) ijt +h j(ψ(k) it ;y it).
2. Maximization step: Regress ψ(k) ijt +h j(ψ(k) it ;y it) on the vector of variables xijt in the utility
equation (7).
3. Repeat until convergence, that is,∥θ (k+1) −θ (k)∥∞ <10 −3.
Since the estimated residuals from the first stage enter the estimation in the second stage, the standard errors
in the second step estimation tend to be downward biased, although the parameter estimates themselves are
consistent (Wooldridge 2010). Therefore, we use block bootstrapping with 500 replications, which treats
individual customers as blocks. In each replication, we resample the same number of customers as in the
original sample with replacement, re-estimate the demand model, and then obtain the bootstrapped standard
errors for the demand parameters and price elasticities (Cameron 2005).
6.4 Demand Model Parameter Estimates
Table 6 presents the estimation results of the demand model based on Equation(7). The standard errors of
the parameter estimates are derived using block bootstrap with 500 replications. All the price coefficients
are negative and statistically significant. The price interaction terms are negative and significant for three
out of the four categories we study: dry dog food and for dog and cat hygiene categories, indicating that the
adoption (and extent of adoption) of a retailer’s channels makes consumersmoreprice sensitive during their
subsequent offline shopping trips at that retailer’s physical stores. The coefficient is insignificant for dry cat
food. We discuss the potential sources for this heterogeneity in§7.1.
The magnitude of the coefficient of the interaction term in the logit model is difficult to interpret directly.
Instead, we can interpret the magnitude of the effect we find by computing the marginal effects and price
18

Table 6: Coefficient Estimates of Demand Model - Main Results
Dry Dog Food Dry Cat Food Dog Hygiene Cat Hygiene
Variables
Price -0.3159∗∗∗
(0.0235)
-0.1603∗∗∗
(0.0188)
-1.2464∗∗∗
(0.123)
-0.221∗∗∗
(0.0209)
cumPercOnlineSpend -0.3357 (0.4601) -1.4046 (1.0888) 8.7512∗∗∗ (1.8675) 3.4655∗∗ (1.0615)
Price * cumPercOnlineSpend -0.1115∗∗
(0.0421)
0.018
(0.091)
-4.1601∗∗∗
(0.8197)
-0.284∗∗∗
(0.0713)
BuyPrevOcca 0.1512∗∗∗
(0.0273)
-0.5037∗∗∗
(0.0451)
-0.1821∗∗∗
(0.0284)
0.3247∗∗∗
(0.0295)
CF Price 0.0515 (0.0293) 0.0468 (0.0258) 0.1911 (0.1815) 0.2805∗∗∗ (0.0279)
CF Price cumPercOnlineSpend 0.0227 (0.0803) -0.0604 (0.1232) 3.6335∗∗∗ (1.0007) 0.3006∗∗ (0.0936)
Customer Brand FE Yes Yes Yes Yes
Observations 136,411 45,443 78,253 55,410
Log-likelihood -84210.21 -30698.052 -55444.644 -37327.537
Bootstrapped standard-errors in parentheses via 500 replications
Signif. Codes: ***: 0.001, **: 0.01, *: 0.05
elasticities (Ai and Norton 2003; Karaca-Mandic et al. 2012). To that end, we calculate price elasticities
using the statistically significant coefficients, as specified in Equation (14) and discuss their implications in
the next section.
7 ATT of Online Adoption on Offline Price Elasticity
Now that we have the demand parameter estimates and we see a negative and significant effect on the
interaction term of interest, we measure the category-level own-price elasticities and formalize the ATT of the
adoption of a retailer’s online channels on offline price elasticities. In §7.1, we present the elasticity estimates
from the estimation procedure. Next, in §7.2, we perform a within-customer comparison of adopters’ offline
price elasticity before and after the adoption of online shopping. In §7.3, we formalize the changes in offline
price elasticity due to the adoption of online shopping using a staggered difference-in-differences (DID)
model.
7.1 Elasticity Estimates
Given the demand model parameters, we can then derive a customer i’s own-price elasticity for brand j in a
purchase occasiontas shown below:
ηijt = ∂P rijt ∂Pricejt · Pricejt P rijt = (α0 +α 2 ×cumPercOnlineSpend it)×Price jt ×(1−P r ijt) (14)
To estimate category-level own-price elasticity, we proceed in two steps. First, for each customer i, brand
j in the customer-month purchase occasion t, we calculate the own-price elasticity ηijt using Equation (14).
We then average across the J brands to obtain a customer-month level own-price elasticity for each category,
19

denoted by ˜ηit = 1 J P j′ ηij′t. Hereafter, we let t index the calendar time (i.e., year-month) rather than a
purchase occasion.˜ηit serves as the dependent variable in our subsequent regression analysis.
For easier interpretation, we further calculate the monthly average elasticity for each adopter and non-
adopter cohort by taking the cross-sectional mean across all customers’ own-price elasticities within that
cohort. Figure 2 shows these monthly average offline price elasticities for both adopters and non-adopters of
these product categories. The dashed line represents the baseline for non-adopters, while the twelve dotted
lines represent adopter cohorts, each defined by the month in which customers first purchased online between
July 2019 and June 2020.
Figure 2: Average price elasticity between adopters (shown in twelve dotted lines) and non-adopters (shown in one dashed line) for
each category.
(a) Dry Dog Food
 (b) Dry Cat Food
(c) Dog Hygiene
 (d) Cat Hygiene
Before online adoption, consumers’ offline price elasticities closely mirror those of non-adopters, sug-
gesting comparable pre-trends. However, after adopting online shopping, adopters consistently become more
price sensitive in their offline shopping. The magnitude of the increase in offline price elasticity is most
20

pronounced for dog hygiene and cat hygiene, moderate for dry dog food, and barely visible for dry cat food.
The sharp increases in elasticities for the hygiene categories are likely due of the fact that these products have
low switching costs: owners face little risk in trying a new hygienic mat for their dog if it is lower priced,
with other attributes like pad size being standardized. The smaller changes to price elasticities in the two pet
food categories, and a zero effect for cat food, are likely due to the fact that brand switching is not so simple
in the case of pet food. Changing a dog’s or cat’s diet entails palatability trials, digestive risks, and rejection.
Cats, in particular, are very picky eaters and have especially strong food preferences in terms of shape, smell,
and texture (Nichelason 2024). Since the main coefficient of interest in Table 6 for cat food is not statistically
significant at the 5% level, and the elasticity figure also shows no effect for cat food, we drop this category in
our subsequent analyses.
In sum, Figure 2 provides clear visual evidence supporting the idea that adoption of online shopping
heightens consumers’ offline price elasticity. Furthermore, this pattern holds true across all cohorts, as well
as for the dry dog food and dog and cat hygiene categories. For cat food, we find a null effect; hence, we
drop the category from our subsequent analyses. A drawback of the plots above is that we don’t control
for common time-specific shocks and/or unobserved customer heterogeneity. In the next few sections, we
address these confounds using within-customer and staggered difference-in-differences (DID) analysis.
7.2 Within-Customer Analysis
We now quantify how adopters’ offline price elasticity changes after they start shopping online at the focal
retailer. We estimate two model specifications on the sample of adopters for each category:
˜ηit =ϕ 0 +ϕ 1 × I{t≥Tadopt i }+e it (15)
˜ηit =Customer i +YearMonth t +ϕ 2 × I{t≥Tadopt i }+e it, (16)
where the binary indicator I{t≥T adopt i } indicates the post-online-adoption period, which equals 1 if
customer i has adopted online shopping at time t, and 0 otherwise. Customeri and YearMontht are customer-
and year-month fixed effects, which control for individual-specific time-invariant unobserved heterogeneity
and time-specific unobserved shocks, respectively. Finally, because the outcome variable is an estimate (rather
than data), we bootstrap standard errors. Specifically, we employ a block bootstrap with 500 replications,
treating individual customers as blocks (as described in §6) to obtain standard errors.
Table 7 presents the parameter estimates (and bootstrapped standard errors) for these categories. We find
that the coefficient on I{t≥T adopt i } is consistently negative across all specifications and categories. This
suggests that, on average, adopters become more sensitive in offline channels in these product categories after
adopting online shopping (even after controlling for customer and time fixed effects).
Although this pre/post comparison isolates within-customer changes, it remains a before-after contrast
confined to adopters. It does not control for common time-varying or macro shocks that could have affected
the trend of price elasticities of both adopters and non-adopters. To effectively address this issue, we
need to construct a counterfactual or control group of non-adopters, who were also offline customers of
21

Table 7: Within-Customer Analysis of Offline Price Elasticity - Main Results
Dependent Variable: Offline Price Elasticity
Dry Dog Food Dog Hygiene Cat Hygiene
Model: (1) (2) (3) (4) (5) (6)
Variables
Constant -2.935 ∗∗∗ -2.464∗∗∗ -2.125∗∗∗
(0.2142) (0.2429) (0.1998)
I{t≥T adopt i }-0.3870 ∗∗∗ -0.1173∗ -1.916∗∗∗ -0.7239∗∗ -0.8860∗∗∗ -0.3347∗∗
(0.0759) (0.0543) (0.3563) (0.2361) (0.1727) (0.1250)
Fixed-effects
Customer Yes Yes Yes
YearMonth Yes Yes Yes
Fit statistics
Observations 29,416 29,416 28,375 28,375 15,081 15,081
R2 0.31325 0.86657 0.34866 0.72137 0.37526 0.75980
Within R2 0.04011 0.03352 0.03960
Bootstrapped standard-errors in parentheses via 500 replications
Signif. Codes: ***: 0.001, **: 0.01, *: 0.05
the firm in the pre-adoption period and continue to be offline only. To address this issue, we outline a
difference-in-differences strategy in the next section.
7.3 Difference-In-Differences (DID) Analysis
To estimate the causal effect of interest – the average treatment effect on the treated (ATT), we use a
difference-in-differences (DID) approach. This method compares adopters with non-adopters before and after
online adoption. As a baseline specification, we estimate the following two-way fixed effects (TWFE) model:
˜ηit =Customer i +YearMonth t +ϕ T W F E× I{Adopteri} × I{t≥Tadopt i }+e it. (17)
Here, ϕT W F Eis our parameter of interest. I{Adopter i} is a binary indicator that is 1 if customer i is an
adopter and 0 otherwise. I{t≥T adopt i } is a binary indicator equal to 1 if the year-montht is in the post-online
adoption phase of customer i. We present the estimation results of the two-way fixed effects estimator in
Table A4 in Web Appendix §D. The estimates show that there is a significant increase in price elasticity
for adopters post-adoption, as indicated by the negative and significant coefficient on ϕT W F Efor these
categories.
Although TWFE regression is widely used in empirical studies involving staggered adoption, it only
provides consistent estimates of ATT under the assumption of homogeneous treatment effects, a condition
that is rarely met in practice; see De Chaisemartin and d’Haultfoeuille (2020); Callaway and Sant’Anna
(2021); Sun and Abraham (2021); Goodman-Bacon (2021) for detailed discussions of this issue. Specifically,
Goodman-Bacon (2021) shows that the TWFE estimator (ϕT W F E) effectively represents a weighted average
of all possible 2-by-2 combinations of pairwise difference-in-differences comparisons between groups of
22

units treated at different times.
To address this issue, we adopt the staggered difference-in-differences (DID) framework proposed by
Callaway and Sant’Anna (2021), hereafter referred to as the CS estimator as our main specification. The CS
estimator addresses the biases associated with TWFE estimators by eliminating problematic comparisons
between late-treated and already-treated units and has been applied recently in the marketing and economics
literature (Ang 2021; Braghieri et al. 2022; Bekkerman et al. 2023). This method is particularly suited to
our context, because we have customers adopting online shopping over a one year period, in 12 cohorts
(one cohort per month). As discussed earlier, because there were exogenous events during this time period
(e.g., the onset of COVID-19), it is possible that the ATT is different across cohorts. Therefore, we use this
estimator in our main analysis and then supplement the analysis with TWFE estimates as a robustness check
(which provide similar results in terms of direction and magnitude). We refer the reader to the original paper
for a discussion of the technical details of how the CS estimator works. The main idea is to identify the
Average Treatment Effect on the Treated (ATT) for each post-treatment period, for consumers who are treated
at different times, and then calculate the overall treatment effect as a weighted average of these ATTs. In our
context, the ATT in monthtfor customers who adopt online shopping in monthgcan be defined as:
AT T(g, t) =E[˜ηit(g)−˜ηit(0)|Gig = 1],(18)
where ˜ηit(g) is the observed elasticity of customer i at month t who adopts online shopping in month g.
Gig is a binary indicator which is set to one if the customer i adopts online shopping in month g. Since the
adoption window in our study spans from July 2019 to June 2020, g ranges from 7 to 18. ˜ηit(0) represents
the potential outcome (i.e. counterfactual elasticity) of customer i at month t, if they did not adopt online
shopping. Under the “no anticipation of treatment” assumption from CS, ˜ηit(0) = ˜ηit(g) for all t < g. In
other words, the offline price elasticity of any customer i during the pre-treatment period does not depend on
whether and when customer i adopts online shopping, and this represents the counterfactual elasticity if they
had not adopted online shopping.
As discussed by Callaway and Sant’Anna (2021), this effect, AT T(g, t), can be identified provided that
parallel pre-trends hold. We provide a test of parallel pre-trends in Figure A7 in Web Appendix §E.3.
The overall treatment effect (θo) is then calculated as a weighted average of AT T(g, t)for all periods
post-adoption across all groups:
θo = 1 Co X g X t>g wgAT T(g, t)(19)
where wg is the weight assigned to units in group g, which is the proportion of the number of online adopters
in treatment groupgrelative to the total number of adopters.C o normalizes the weights to sum to one.
We present the overall treatment effect estimates(θo) in Table 8. Since the customer-month level price
elasticities are themselves estimates from our demand model with confidence intervals around them (and not
directly observed from data), we compute standard errors for our ATT estimates using customer-level block
bootstraps with 500 replications. Figure A3 in Web Appendix §D shows the bootstrapped distribution of
23

Table 8: ATT of Online Adoption on Offline Price Elasticity Over All Post-Adoption Period (CS Estimator)
Dependent Variable: Offline Price Elasticity
Dry Dog Food Dog Hygiene Cat Hygiene
Model: (1) (2) (3)
ATT -0.2482 ∗∗ -1.7922∗∗∗ -0.7381∗∗∗
(0.0945) (0.3678) (0.1794)
ATT Relative to Adopters’
Pre-Adoption Elasticity 8.4% 72.7% 34.7%
Observations 136,411 78,253 55,410
Bootstrapped standard-errors in parentheses via 500 replications
Signif. Codes: ***: 0.001, **: 0.01, *: 0.05
these ATT estimates. The results in Table 8 suggest that consumers become more price-sensitive in the offline
channel after they adopt online shopping, and this finding is consistent across these categories. The effect is
stronger for the dog and cat hygiene categories, consistent with the elasticity visualization in Figure 2. To
help with interpretation, we calculate the relative magnitude of the elasticity increase in percentage terms by
dividing the ATT by the average pre-adoption price elasticity of adopters and show these percentage changes
in the second row of Table 8. The most substantial effects are observed for dog hygiene and cat hygiene
categories; offline price elasticity increases by 72.7% (i.e., -1.792 / -2.464) for dog hygiene and 34.7% (i.e.,
-0.738 / -2.125) for cat hygiene. The increase in offline price elasticity is lower for dry dog food, at 8.4% (i.e.,
-0.248 / -2.935). As discussed in §7.1, the pronounced increase in offline price elasticity for hygiene products
(vs. dry food products) is likely driven by the lower switching costs associated with trying new brands of
hygiene mats or other hygiene-related items. In sum, consistent with the descriptive evidence earlier, we find
that consumers become more price-sensitive in their offline shopping trips when they start shopping online.
8 Generalizability and Robustness Checks
We now discuss the generalizability of our findings, provide some extensions, and present a series of tests
and alternative specifications to establish the robustness of our findings.
8.1 Generalizability
We now discuss the generalizability of our findings and provide some evidence in favor of portability to other
settings.
First, consumers may adopt online shopping for different reasons, and a natural question is whether our
results are specific to consumers who adopt online shopping for certain reasons but not others. To examine
this question, we leverage the fact that our observation period starts before the onset of the COVID-19
pandemic and continues through it. The cohorts that adopted from July 2019 to Feb 2020 are likely to have
done so organically, while those who adopted from March 2020 are likely to have done so for exogenous
reasons, i.e., the COVID-19 pandemic. Indeed, there is a big surge in online adoptions starting March 2020
(see Figure 1). We use this exogenous shock in the reason for adoption across cohorts to examine this
24

issue. Overall, we find that the reason why a consumer switches to online shopping does not seem to have a
significant impact on post-adoption price sensitivity: the ATT of cohorts that switched during the COVID-19
pandemic is similar to that of cohorts that switched organically before the onset of COVID-19 (see Figure 2).
This suggests that the online adoption effect is not sensitive to the reasons that drive a consumer’s decision to
adopt online shopping.
Second, we examine the extent to which our results are likely to be driven by the fact that online prices
are slightly lower than offline prices in our setting. To that end, we examine the magnitude of the price
differences between online and offline channels in our study (see details in in Web Appendix §E.1). We
find that online prices are only 2–6% lower than offline in our data. Furthermore, the variation in prices
explained by channel is significantly smaller than the variation in prices explained by SKU-level differences –
across all categories, only 4% of the variation in prices is explained by channels, whereas when we include
SKU fixed effects, this increases to 65%. Overall, these data patterns suggest that the differences between
online and offline prices are relatively small and are unlikely to be the primary driver of our results. Other
potential mechanisms, such as consumers becoming more accustomed to comparing prices across brands
or their exposure to a wider variety of prices, are likely to be at play as well (as discussed in §1). Thus, we
expect that our results are likely to generalize to other empirical settings where online prices are the same or
higher than offline prices.15
Nevertheless, we note that we are unable to tease out the exact source of these effects because we lack
granular data on consumers’ search and shopping behavior in the online channel. We do not observe online
click-stream data, so we cannot comment on price search behavior online or the variety of prices seen online.
We also do not observe any search behavior in offline stores. Further, while there are some differences in
offline prices across physical stores at any given point in time, we do not have a sufficiently large proportion
of stores that are consistently higher or lower priced than others throughout our entire time period. Therefore,
we cannot conduct a clean test of whether the effect we observe is driven more by price differences across
the offline and online channels, the variety of prices that the consumer sees, or changes in search behavior
that occur after adopting online shopping. We hope that future research can further dis-entangle which of
these mechanisms are at play and to what extent. Further studies of such spillover effects in other countries,
product categories, and retailers can also provide a more comprehensive understanding of the extent to which
these effects manifest in different settings.
8.2 Robustness checks
We first examine alternative demand specifications in §8.2.1 and then consider matching methods and
alternative control groups in §8.2.2 and 8.2.3, respectively. Finally, in §8.2.4, we consider an alternative
definition of the purchase occasions.
8.2.1 Alternative Demand Specifications
We now consider two different demand model specifications:
15In practice, there is considerable heterogeneity in whether online prices are lower, the same, or higher than offline prices across
retailers, countries, and product categories (Cavallo 2017).
25

•Binary online adoption variable:In our main demand model, we use the continuous variable
cumPercOnlineSpendit to capture how consumers’ offline price sensitivity changes after adopting online
shopping. We now consider an alternative specification where we treat online adoption as a binary treat-
ment. To that end, we use the binary indicator, Post OnlineAdoptionit, which takes value one if customer
i has adopted online shopping by time t, and zero otherwise. We substitute cumPercOnlineSpendit with
Post OnlineAdoptionit in Equation (3), and also modify the corresponding control function term accord-
ingly. We estimate revised demand model and compute the average elasticity at the customer-month level
for each product category following the same steps as before. The details of the model and estimation
results are provided in Web Appendix §E.2. The conclusions from this alternative demand model and the
corresponding ATT estimates are consistent with our main results.
•Accounting for a potential change in state dependence or brand loyalty due to online adoption:In
our main model, we include customer-brand fixed effects to capture time-invariant preferences and use
I{BuyPrevOccaijt} to capture the state dependence. We now consider a specification with an additional
control variable, I{BuyPrevOccaijt} ×cumPercOnlineSpendit, which captures the interaction between
state dependence (e.g., repeated purchase of a brand) and the share of online spending. This can account
for any effects that online adoption may have on brand loyalty.
The utility specifications and the estimation results from these two exercises are shown in Web Appendix
§E.2. We find that the results are consistent with our main specification. We also do not find evidence of
significant changes to offline brand loyalty after consumers adopt online shopping.
8.2.2 Matching and IPW Approaches to Control for Selection on Observables
Consumers self-select into adopting a retailer’s online channel (or not), and as shown in Web Appendix
§A.2, there are some systematic differences between adopters and non-adopters in terms of observable
characteristics like demographics. In general, such differences are not an issue as long as the parallel pre-
trends assumption holds (see Chapter 5 of Angrist and Pischke (2008) and Roth et al. (2023) for additional
discussions). To that end, we consider the pre-adoption trends in price elasticities between adopters and
non-adopters and verify that the parallel pre-trends assumption holds in Web Appendix§E.3.
Nevertheless, differences in characteristics between groups may still potentially lead to differences in
price elasticities over time in some way that is not showing up in the first few months of data or is not being
accounted for in our model. For instance, there may be some factor that affects younger customers who are
more likely to adopt online shopping, and only shows up in the later part of our data period. To provide
additional credibility to our findings and to ensure that they are robust to any time-varying factors correlated
with observable characteristics, we use propensity score-based methods like Inverse Propensity Weighting
(IPW) and Propensity Score Matching (PSM) to account for differences in observable characteristics between
the groups, which improves the comparability between the groups. These methods improve covariate balance,
discard poorly matched customers, and make our results more robust to model misspecification with respect
to any time-varying factors that are correlated with observable characteristics.
We perform the propensity score estimation and matching for each adoption cohort separately. Specifically,
26

we define the pre-adoption period separately for each cohort and measure pre-adoption variables (e.g., monthly
average spend) using all purchase data up to the month of adoption (Gu and Kannan 2021). For example,
when identifying matched non-adopters for customers who adopt in July 2019, we measure the pre-adoption
variables for both adopters and non-adopters using the data up to June 30, 2019, and estimate the propensity
score model for the adoption cohort in July 2019. We repeat this process for each cohort and estimate twelve
different propensity score models corresponding to each monthly adoption cohort. We compute propensity
scores with a logistic regression model and the variables included are demographics (e.g., gender, age, and
household income) and pre-adoption purchase variables (i.e. average monthly spend, number of unique
orders, unique brands, and unique categories). With the estimated propensity scores, we use our CS estimator
to estimate the ATT using both IPW and PSM methods. The propensity score model specification and detailed
results from the IPW and PSM methods are shown in Web Appendix E.4. We find that our conclusions
remain the same.
8.2.3 Alternative Control Groups
While we do our best to account for differences in observable characteristics between adopters and non-
adopters in§8.2.2, it may be that there are certain time-specific unobserved factors that only affect adopters
or would-be adopters, or disproportionately affect them more than non-adopters, thus potentially making
non-adopters an unsuitable control group. We conduct an additional robustness check, leveraging the fact that
we have multiple cohorts of consumers who adopted online shopping at different times. Following Narang
and Shankar (2019) and Manchanda et al. (2015), we consider an alternative specification where later adopter
cohorts serve as control groups for earlier adopter cohorts. Since all of these cohorts adopt online shopping
at some point, the differences in any time-specific unobservables (that correlate with factors that drive the
decision of whether a consumer chooses to adopt online shopping or not) should be minimized across these
different adoption cohorts, at least relative to non-adopters. The results from this alternative CS estimator are
shown in Web Appendix §E.5. Overall, we see that the conclusions remain similar to those from our main
specification, i.e., that consumers become more offline price-sensitive after adopting online shopping.
8.2.4 Alternative Definition of Purchase Occasions
In §3.2, we define a purchase occasion as any customer-month during which we observe any offline interaction
with the retailer (similar to a week-store visit in Gordon et al. (2013)). In this section, we consider an
alternative definition. Specifically, if a customer visits the retailer (i.e., either in-store or online) during a
month and purchases in any category (not limited to the categories we focus on in this study), that customer-
month is included as a purchase occasion for all four categories. If a customer makes no purchases in any
category during the month, that customer-month is not included as a purchase occasion. In other words, a
purchase occasion represents any customer-month during which we observe any interaction with the retailer,
either offline or online.
The detailed demand model estimates and ATT estimation results are presented in Web Appendix §E.6.
Overall, our conclusions remain similar to those from our main specification, i.e., that consumers become
27

more offline price-sensitive after adopting online shopping.
9 Managerial Implications and Conclusions
The rapid growth of e-commerce has fundamentally reshaped consumer behavior, but its spillover effects
on offline shopping dynamics remain understudied. In this paper, we investigate how the adoption of
online shopping using a retailer’s e-commerce channels influences consumers’ offline price sensitivity when
shopping at that retailer’s physical stores, utilizing transaction-level data from a multichannel pet supplies
retailer in Brazil. We find that consumers who adopt online shopping become more price-sensitive in their
offline purchases. The relative increase in offline price elasticity, defined as the ATT relative to the pre-
adoption average price elasticity of the treated group, is quite heterogeneous across categories, with a 72.7%
and a 34.7% increase for dog hygiene and cat hygiene categories, and a smaller increase of 8.4% for dog
food. We find no effect on cat food, presumably because it is hard to switch brands easily in this category.
From a substantive standpoint, our results contribute to the literature on price elasticity by identifying
online adoption as a novel determinant of offline price sensitivity. This factor has so far been ignored in
the demand estimation literature, which usually only accounts for factors like consumer demographics and
macro-economic shocks to affect consumer price sensitivity. From a managerial standpoint, our findings
have implications for retailer offline pricing and profitability, emphasizing the need for multichannel retailers
to account for the online adoption effect (i.e., heightened offline price sensitivity when consumers adopt
their online channels) in their pricing decisions. Further, our approach can be used to personalize prices
depending on customers’ channel adoption status. While existing literature has largely focused on pricing
and personalization based on customer demographics and prior purchase behavior (Rossi and Allenby 1993;
Chen et al. 2001; Jiang et al. 2021; Jain et al. 2024), our work suggests that incorporating cross-channel
effects into measures of price elasticity and pricing strategy can further enhance profits.
Finally, our paper opens many avenues for future research. First, future research could explore whether
these effects generalize to other markets (e.g., non-discretionary goods or regions with lower e-commerce
penetration) and investigate mediating factors, such as the role of mobile price-checking apps or subscription
models. Further, while our paper documents one aspect of consumer behavior (price sensitivity), multi-
channel shopping can induce other spillover effects from one channel to another. For instance, product
categories purchased offline may change after adopting online shopping (Huyghe et al. 2017), and there may
be cross-media effects between channels (Joo et al. 2014; Du et al. 2019). Future research can investigate
other such spillover effects and their effect on cross-channel purchases. Ultimately, as retail continues
to evolve toward omnichannel integration, understanding these interdependencies will be critical for both
academics and firms aiming to thrive in a digitally transformed landscape.
Funding and Competing Interests
The authors were not paid by the data provider. A preliminary version of this manuscript was reviewed by the
data provider to ensure that data was accurately depicted, but they did not review/comment on the content of
the manuscript.
28

References
Ai, C. and Norton, E. C. (2003). Interaction terms in logit and probit models.Economics letters, 80(1):123–129.
Allenby, G. M. and Rossi, P. E. (1998). Marketing models of consumer heterogeneity.Journal of econometrics,
89(1-2):57–78.
Andrews, R. L. and Currim, I. S. (2004). Behavioural differences between consumers attracted to shopping online
versus traditional supermarkets: implications for enterprise design and marketing strategy.International Journal of
Internet Marketing and Advertising, 1(1):38–61.
Ang, D. (2021). The effects of police violence on inner-city students.The Quarterly Journal of Economics, 136(1):115–
168.
Angrist, J. and Pischke, J.-S. (2008). Mostly harmless econometrics (princeton uni.
Angrist, J. D. and Imbens, G. W. (1995). Two-stage least squares estimation of average causal effects in models with
variable treatment intensity.Journal of the American statistical Association, 90(430):431–442.
Aparicio, D., Eckles, D., and Kumar, M. (2024). Algorithmic pricing and consumer sensitivity to price variability.
Avery, J., Steenburgh, T. J., Deighton, J., and Caravella, M. (2012). Adding bricks to clicks: Predicting the patterns of
cross-channel elasticities over time.Journal of Marketing, 76(3):96–111.
Baker, A. C., Larcker, D. F., and Wang, C. C. (2022). How much should we trust staggered difference-in-differences
estimates?Journal of Financial Economics, 144(2):370–395.
Bawa, K. and Shoemaker, R. W. (1987). The coupon-prone consumer: some findings based on purchase behavior across
product classes.Journal of marketing, 51(4):99–110.
Bawa, K. and Shoemaker, R. W. (1989). Analyzing incremental sales from a direct mail coupon promotion.Journal of
marketing, 53(3):66–78.
Bekkerman, R., Cohen, M. C., Kung, E., Maiden, J., and Proserpio, D. (2023). The effect of short-term rentals on
residential investment.Marketing Science, 42(4):819–834.
Bell, D. R., Gallino, S., and Moreno, A. (2018). Offline showrooms in omnichannel retail: Demand and operational
benefits.Management Science, 64(4):1629–1651.
Berry, S. T. (1994). Estimating discrete-choice models of product differentiation.The RAND Journal of Economics,
pages 242–262.
Berry, S. T. and Haile, P. A. (2021). Foundations of demand estimation. InHandbook of industrial organization,
volume 4, pages 1–62. Elsevier.
Berry, S. T., Levinsohn, J. A., and Pakes, A. (1995). Automobile prices in market equilibrium.
Bijmolt, T. H., Van Heerde, H. J., and Pieters, R. G. (2005). New empirical generalizations on the determinants of price
elasticity.Journal of marketing research, 42(2):141–156.
Biswas, S., Yoganarasimhan, H., and Zhang, H. (2024). Channel choice and customer value.Available at SSRN
4747756.
Braghieri, L., Levy, R., and Makarin, A. (2022). Social media and mental health.American Economic Review,
112(11):3660–3693.
Brynjolfsson, E. and Smith, M. D. (2000). Frictionless commerce? a comparison of internet and conventional retailers.
Management science, 46(4):563–585.
Callaway, B. and Sant’Anna, P. H. (2021). Difference-in-differences with multiple time periods.Journal of econometrics,
225(2):200–230.
Cameron, A. (2005). Microeconometrics: methods and applications.Cambridge University.
Cavallo, A. (2017). Are online and offline prices similar? evidence from large multi-channel retailers.American
29

Economic Review, 107(1):283–303.
Chen, G., Lu, C., Chan, T., Qi, Z., Zhang, D., Jin, Y ., and Yang, M. (2024). A new estimator for randomized controlled
trials with non-compliance: Theory and empirical evidence.Available at SSRN 4864490.
Chen, M., Meeker, I., Rysman, M., and Wang, S. (2025). An mm algorithm for fixed effects multinomial logit models.
Unpublished manuscript, Boston University.
Chen, M., Rysman, M., Wang, S., and Wozniak, K. (2022). An mm algorithm for fixed effects in multinomial models
with an application to payment choice in grocery stores. Technical report, Working Papers.
Chen, Y ., Narasimhan, C., and Zhang, Z. J. (2001). Individual marketing with imperfect targetability.Marketing
Science, 20(1):23–41.
Chib, S., Seetharaman, P., and Strijnev, A. (2004). Model of brand choice with a no-purchase option calibrated to
scanner-panel data.Journal of marketing research, 41(2):184–196.
Chintagunta, P., Dub´e, J.-P., and Goh, K. Y . (2005). Beyond the endogeneity bias: The effect of unmeasured brand
characteristics on household-level brand choice models.Management Science, 51(5):832–849.
Chintagunta, P. K., Jain, D. C., and Vilcassim, N. J. (1991). Investigating heterogeneity in brand preferences in logit
models for panel data.Journal of Marketing Research, 28(4):417–428.
Chintala, S. C., Liaukonyt˙e, J., and Yang, N. (2023). Browsing the aisles or browsing the app? how online grocery
shopping is changing what we buy.Marketing Science.
Chu, J., Arce-Urriza, M., Cebollada-Calvo, J.-J., and Chintagunta, P. K. (2010). An empirical analysis of shopping
behavior across online and offline channels for grocery products: The moderating effects of household and product
characteristics.Journal of Interactive Marketing, 24(4):251–268.
Chu, J., Chintagunta, P., and Cebollada, J. (2008). Research note—a comparison of within-household price sensitivity
across online and offline channels.Marketing science, 27(2):283–299.
Cooper, J. C. (2006). Prices and price dispersion in online and offline markets for contact lenses.FTC Bureau of
Economics working paper, (283).
Cui, T. H., Ghose, A., Halaburda, H., Iyengar, R., Pauwels, K., Sriram, S., Tucker, C., and Venkataraman, S. (2021).
Informational challenges in omnichannel marketing: Remedies and future research.Journal of Marketing, 85(1):103–
120.
Danaher, P. J., Wilson, I. W., and Davis, R. A. (2003). A comparison of online and offline consumer brand loyalty.
Marketing Science, 22(4):461–476.
De Chaisemartin, C. and d’Haultfoeuille, X. (2020). Two-way fixed effects estimators with heterogeneous treatment
effects.American economic review, 110(9):2964–2996.
Degeratu, A. M., Rangaswamy, A., and Wu, J. (2000). Consumer choice behavior in online and traditional supermarkets:
The effects of brand name, price, and other search attributes.International Journal of research in Marketing,
17(1):55–78.
Du, R. Y ., Xu, L., and Wilbur, K. C. (2019). Immediate responses of online brand search and price search to tv ads.
Journal of Marketing, 83(4):81–100.
Dub´e, J.-P., Hitsch, G. J., and Rossi, P. E. (2010). State dependence and alternative explanations for consumer inertia.
The RAND Journal of Economics, 41(3):417–445.
Ebbes, P., Papies, D., and van Heerde, H. J. (2016). Dealing with endogeneity: A nontechnical guide for marketing
researchers. InHandbook of market research, pages 1–37. Springer.
Erdem, T. and Keane, M. P. (1996). Decision-making under uncertainty: Capturing dynamic brand choice processes in
turbulent consumer goods markets.Marketing science, 15(1):1–20.
30

Forman, C., Ghose, A., and Goldfarb, A. (2009). Competition between local and electronic markets: How the benefit of
buying online depends on where you live.Management science, 55(1):47–57.
Goodman-Bacon, A. (2021). Difference-in-differences with variation in treatment timing.Journal of econometrics,
225(2):254–277.
Gordon, B. R., Goldfarb, A., and Li, Y . (2013). Does price elasticity vary with economic growth? a cross-category
analysis.Journal of Marketing Research, 50(1):4–23.
Gu, X. and Kannan, P. (2021). The dark side of mobile app adoption: Examining the impact on customers’ multichannel
purchase.Journal of Marketing Research, 58(2):246–264.
Guadagni, P. M. and Little, J. D. (1983). A logit model of brand choice calibrated on scanner data.Marketing science,
2(3):203–238.
Guadagni, P. M. and Little, J. D. (2008). A logit model of brand choice calibrated on scanner data.Marketing Science,
27(1):29–48.
Haleem, A. (2025). Us ecommerce sales in 2024 more than double those of 2019. Accessed: May 19, 2025.
Hitsch, G. J., Hortacsu, A., and Lin, X. (2021). Prices and promotions in us retail markets.Quantitative Marketing and
Economics, 19(3):289–368.
Hoch, S. J., Kim, B.-D., Montgomery, A. L., and Rossi, P. E. (1995). Determinants of store-level price elasticity.
Journal of marketing Research, 32(1):17–29.
Huyghe, E., Verstraeten, J., Geuens, M., and Van Kerckhove, A. (2017). Clicks as a healthy alternative to bricks: how
online grocery shopping reduces vice purchases.Journal of Marketing Research, 54(1):61–74.
Jain, L., Li, Z., Loghmani, E., Mason, B., and Yoganarasimhan, H. (2024). Effective adaptive exploration of prices and
promotions in choice-based demand models.Marketing Science.
James, J. (2017). Mm algorithm for general mixed multinomial logit models.Journal of Applied Econometrics,
32(4):841–857.
Jedidi, K., Mela, C. F., and Gupta, S. (1999). Managing advertising and promotion for long-run profitability.Marketing
science, 18(1):1–22.
Jiang, Z., Chan, T., Che, H., and Wang, Y . (2021). Consumer search and purchase: An empirical investigation of
retargeting based on consumer online behaviors.Marketing Science, 40(2):219–240.
Jiang, Z., Li, J., and Zhang, D. (2025). A high-dimensional choice model for online retailing.Management Science,
71(4):3320–3339.
Joo, M., Gauri, D. K., and Wilbur, K. C. (2020). Temporal distance and price responsiveness: Empirical investigation
of the cruise industry.Management Science, 66(11):5362–5388.
Joo, M., Wilbur, K. C., Cowgill, B., and Zhu, Y . (2014). Television advertising and online search.Management Science,
60(1):56–73.
Kalra, A. and Goodstein, R. C. (1998). The impact of advertising positioning strategies on consumer price sensitivity.
Journal of marketing research, 35(2):210–224.
Kamakura, W. A. and Russell, G. J. (1989). A probabilistic choice model for market segmentation and elasticity
structure.Journal of marketing research, 26(4):379–390.
Kanetkar, V ., Weinberg, C. B., and Weiss, D. L. (1992). Price sensitivity and television advertising exposures: Some
empirical findings.Marketing Science, 11(4):359–371.
Karaca-Mandic, P., Norton, E. C., and Dowd, B. (2012). Interaction terms in nonlinear models.Health services
research, 47(1pt1):255–274.
Kaul, A. and Wittink, D. R. (1995). Empirical generalizations about the impact of advertising on price sensitivity and
31

price.Marketing Science, 14(3 supplement):G151–G160.
Kim, J., Allenby, G. M., and Rossi, P. E. (2002). Modeling consumer demand for variety.Marketing Science,
21(3):229–250.
Kopalle, P. K., Mela, C. F., and Marsh, L. (1999). The dynamic effect of discounting on sales: Empirical analysis and
normative pricing implications.Marketing Science, 18(3):317–332.
Krishnamurthi, L. and Raj, S. (1988). A model of brand choice and purchase quantity price sensitivities.Marketing
Science, 7(1):1–20.
Li, H. (2021). Are e-books a different channel? multichannel management of digital products.Quantitative Marketing
and Economics, 19(2):179–225.
Manchanda, P., Packard, G., and Pattabhiramaiah, A. (2015). Social dollars: The economic impact of customer
participation in a firm-sponsored online customer community.Marketing Science, 34(3):367–387.
McKinsey & Company (2023). The next horizon for grocery e-commerce. Accessed: 2024-09-29.
Mela, C. F., Gupta, S., and Lehmann, D. R. (1997). The long-term impact of promotion and advertising on consumer
brand choice.Journal of Marketing research, 34(2):248–261.
Mummalaneni, S., Yoganarasimhan, H., and Pathak, V . (2025). How do content producers respond to engagement on
social media platforms?
Narang, U. and Shankar, V . (2019). Mobile app introduction and online and offline purchases and product returns.
Marketing Science, 38(5):756–772.
Narasimhan, C. (1984). A price discrimination theory of coupons.Marketing Science, 3(2):128–147.
Neslin, S. A. (2022). The omnichannel continuum: Integrating online and offline channels along the customer journey.
Journal of retailing, 98(1):111–132.
Nevo, A. (2001). Measuring market power in the ready-to-eat cereal industry.Econometrica, 69(2):307–342.
Nichelason, A. (2024). Expert q&a: Understanding pet food. Accessed: May 21, 2025.
Petrin, A. and Train, K. (2010). A control function approach to endogeneity in consumer choice models.Journal of
marketing research, 47(1):3–13.
Pozzi, A. (2012). Shopping cost and brand exploration in online grocery.American Economic Journal: Microeconomics,
4(3):96–120.
Rossi, P. E. and Allenby, G. M. (1993). A bayesian approach to estimating household parameters.Journal of Marketing
Research, 30(2):171–182.
Rossi, P. E., McCulloch, R. E., and Allenby, G. M. (1996). The value of purchase history data in target marketing.
Marketing Science, 15(4):321–340.
Roth, J., Sant’Anna, P. H., Bilinski, A., and Poe, J. (2023). What’s trending in difference-in-differences? a synthesis of
the recent econometrics literature.Journal of Econometrics, 235(2):2218–2244.
Shriver, S. K. and Bollinger, B. (2022). Demand expansion and cannibalization effects from retail store entry: A
structural analysis of multichannel demand.Management Science, 68(12):8829–8856.
Sun, L. and Abraham, S. (2021). Estimating dynamic treatment effects in event studies with heterogeneous treatment
effects.Journal of econometrics, 225(2):175–199.
Syrgkanis, V ., Lei, V ., Oprescu, M., Hei, M., Battocchi, K., and Lewis, G. (2019). Machine learning estimation of
heterogeneous treatment effects with instruments.Advances in Neural Information Processing Systems, 32.
Tellis, G. J. (1988). The price elasticity of selective demand: A meta-analysis of econometric models of sales.Journal
of marketing research, 25(4):331–341.
Villas-Boas, J. M. and Winer, R. S. (1999). Endogeneity in brand choice models.Management science, 45(10):1324–
32

1338.
Wang, K. and Goldfarb, A. (2017). Can offline stores drive online sales?Journal of Marketing Research, 54(5):706–719.
Wang, R. J.-H., Malthouse, E. C., and Krishnamurthi, L. (2015). On the go: How mobile shopping affects customer
purchase behavior.Journal of Retailing, 91(2):217–234.
Wooldridge, J. M. (2010).Econometric analysis of cross section and panel data. MIT press.
Wooldridge, J. M. (2015). Control function methods in applied econometrics.Journal of Human Resources, 50(2):420–
445.
Yu, Q., Berman, R., and Bradlow, E. (2021). The dark side of category expansion: Will (and which) existing ones’ pay
the price’?Available at SSRN 3837014.
Zhang, D. J., Dai, H., Dong, L., Wu, Q., Guo, L., and Liu, X. (2019). The value of pop-up stores on retailing platforms:
Evidence from a field experiment with alibaba.Management Science, 65(11):5142–5151.
33

Web Appendices
A Appendix to Setting and Data
A.1 Details of Dataset Construction
A.1.1 Selection of Brands and Stock Keeping Units (SKUs)
For each product category (i.e., dry dog food, dry cat food, dog hygiene and cat hygiene), we focus on a
single pack size that accounts for the largest sales revenue and offers sufficient brand representation. Our goal
is to study consumer brand choice and price elasticity, so consistent with previous brand choice literature
(Allenby and Rossi 1998; Kim et al. 2002; Chintagunta et al. 2005; Dub´e et al. 2010) we focus on a market
(i.e., single most popular pack size within each category) that initially (as of January 1st, 2019 - June 30th,
2019) features at least three brands. We exclude any market with fewer than three brands or with one brand
contributing more than 60% of total sales. Applying these criteria yields the top one selling pack sizes for
each category during the observation period: 15KG adult daily dry dog food, 10.1KG adult daily dry cat food,
and an 80cm×60cm dog hygiene mat containing 30 pieces.
However, we observe high market concentration for certain cat hygiene pack sizes. The 12KG, 4KG,
and 3KG sizes are among the top-selling segments (e.g., ranked 1st, 3rd, and 4th in offline sales). However,
each has less than three brands, and a single brand contributes over 60% of sales revenue (85%, 63%, and
88%, respectively), making these pack sizes unsuitable for brand choice analysis. Furthermore, the excluded
pack sizes differ significantly in sand types, compositions, and functional characteristics, limiting their
substitutability in the consumer’s mind. For example, 3KG pack sizes SKUs are primarily made from cereal-
and vegetable-based materials that are eco-friendly, bio-degenerate, lightweight, and prone to scattering,
whereas 4KG and 12KG pack sizes consist of granulated smectite clay, which is heavy, non-biodegradable
and derived from mine materials. Hence, these pack sizes cater to distinct functional needs and consumer
preferences. 16 The differences in product attributes and target consumer preferences complicate defining a
cohesive market that includes these pack sizes. In addition, even if 4KG and 12KG pack sizes are grouped
into a single market, the top brand still accounts for 77% of the sales, leaving little room for brand choice
analysis.
Consequently, we focus on silica cat sand in the 1.6KG, 1.8KG, and 2.0KG, which together account for
29% of the store’s cat sand sales. Among these, the 1.8KG size is the second largest in the offline cat sand
sales. Despite slight variations in pack sizes across brands, all three pack sizes offer the same sand category
(i.e., silica), and we observe significant overlap in consumer purchases. Specifically, among customers who
purchased the 1.8KG size at least once during the sample period, 28% also purchased the 1.6KG pack size,
and 20% also purchased the 2.0KG pack size during the observation period, indicating a clear overlap of
consumer preferences in this segment.
After defining the market with the top one selling pack size for each category, we rank brands by offline
16For a similar reason, we exclude the 10KG pack size, which ranks 6th and sells sands with pine and wood.
i

sales in descending order and include those that collectively account for at least 80% of the sales, following
earlier literature (Gordon et al. 2013). The remaining brands are grouped into a single ‘Other Brand’ for each
product category, ensuring broad market coverage.
A.1.2 Price and Cost Index Calculations
We construct brand-level price indices for each category by aggregating SKU-level price data fromoffline
transactions (Gordon et al. 2013; Hitsch et al. 2021). First, we construct a store-SKU-month level price
matrix from the available transactions data. To begin with, this price matrix could contain both outliers and
missing values. Any observed price that is more than four times higher than or less than one-quarter of
the median price for each SKU (across all store-month observations) is treated as an outlier and labeled as
missing, following Hitsch et al. (2021). This process filters out unreasonable prices before imputing any
missing values of store-SKU-month price (when there is no sale or there is an outlier). For these missing
prices, we use the highest observed price from the previous three months for the same SKU at the same store
to impute the missing value (Gordon et al. 2013). Finally, we exclude SKUs for a particular store and week if
we have never observed them being sold in that store previously.
Next, we aggregate SKUs to create brand-level price indices by converting all SKU prices to a per-unit
basis for comparable units. All product categories (e.g., dry food and cat sands) are measured by price per
kilogram (KG) except for hygienic mats, which are measured by price per piece. Following the approach of
Hitsch et al. (2021), the brand price for brand j at store s in month t, denoted as BrandPricejst, is calculated
as the weighted average price per unit across all SKUs in that brand in the defined market. The weights are
based on each SKU’s share of offline sales within the brand at that store over the full 30-month data period.
Brand Pricejst =
X
k∈Cjs
wjsk ×SKU Pricejstk ,(A1)
where the weight of SKU k is wjsk = Store SalesjskP k′∈Cjs Store Salesjsk′ , and Store Salesjsk is the total offline sales of
SKU k for brand j at store s from January 1, 2019 to June 30, 2021. Cjs represents the set of SKUs for brand
j available at store s, and SKU Pricejstk is the price of SKU k for brand j sold in store s during month t, as
recorded in the store-SKU-month price matrix.
We then apply a similar approach to construct a store-SKU-month level cost matrix based on wholesale
cost data, and aggregate SKU-level costs to create brand-level cost indices that correspond to each price
index. These cost indices serve as the instrument for addressing price endogeneity, as discussed in Section
§6. Finally, we use Brazil’s Extended National Consumer Index (IPCA) to obtain inflation-adjusted prices
and costs (Brazil Institute of Geography and Statistics (IBGE) 2024), with January 2019, the first month of
observation, as the base period.
ii

A.1.3 Supplementary material for Selection of Customers
Figure A1 illustrates three examples of adopters defined in §3.2, including adopters whose first online
purchase in any category during August 2019, April 2020, and June 2020, respectively. Table A1 presents the
sample sizes for each adoption cohort and each category.
Figure A1: Staggered Adoption Cohorts of Online Shopping (12 Adoption Cohorts from July 2019 to June 2020)
Table A1: Adopters Sample Size by Adoption Time - By Product Category
Adoption Month Dry Dog Food Dry Cat Food Dog Hygiene Cat Hygiene
2019-07 85 53 52 36
2019-08 111 46 71 41
2019-09 100 34 96 44
2019-10 110 42 82 47
2019-11 174 51 143 67
2019-12 144 78 120 58
2020-01 138 57 107 47
2020-02 143 52 106 55
2020-03 334 160 382 190
2020-04 438 208 442 241
2020-05 357 143 353 209
2020-06 276 113 260 157
Total 2410 1037 2214 1192
iii

A.2 Summary Statistics for Customer Demographics
We summarize the customer demographics for each product category. Table A2 presents the gender distribu-
tion for the different product categories amongst adopters and non-adopters. In all categories, adopters exhibit
a higher proportion of women compared to non-adopters. For example, in the dry dog food category, 48%
of adopters are female, whereas only 32.6% of non-adopters are female. Figure A2 shows the cumulative
age and income distributions for adopters and non adopters. The height of the leftmost point on each curve
represents the fraction of customers with missing age or income information. Across all categories, adopters
tend to be younger compared to non-adopters. In terms of monthly household income, adopters generally
exhibit higher incomes relative to compared to non-adopters.
Table A2: Gender by Product Categories
Dry Dog Food Dry Cat Food Dog Hygiene Cat Hygiene
Gender Adopters Non-Adopters Adopters Non-Adopters Adopters Non-Adopters Adopters Non-Adopters
Female 0.480 0.326 0.570 0.418 0.601 0.470 0.602 0.462
Male 0.398 0.522 0.286 0.417 0.285 0.379 0.279 0.387
NaN 0.122 0.152 0.144 0.165 0.113 0.152 0.118 0.151
Total 1 1 1 1 1 1 1 1
iv

Figure A2: Customer demographics of adopters and non-adopters of product category - age and monthly household income
(a) Dry Dog Food - Age
 (b) Dry Dog Food - Income
(c) Dry Cat Food - Age
 (d) Dry Cat Food - Income
(e) Dog Hygiene - Age
 (f) Dog Hygiene - Income
(g) Cat Hygiene - Age
 (h) Cat Hygiene - Income
v

B Appendix to Descriptive Analysis
B.1 Supplementary Result: Percentile Price Paid
As a robustness check for the results in §4, Table A3 presents the within-customer changes in the percentile
of prices paid by adopters relative to non-adopters, controlling for customer and year-month fixed effects.
The percentile of price paid is calculated by first constructing the empirical price distribution for each month,
based on all transactions in that month involving SKUs from the focal category. Each transaction price is
then ranked relative to this monthly price distribution to obtain its percentile.
Table A3: Two-Way Fixed Effects Model Estimates - Percentile Price Paid
Dependent Variable: Percentile Price Paid
Dry Dog Food Dry Cat Food Dog Hygiene Cat Hygiene
Model: (1) (2) (3) (4)
Variables
I{Adopter i} × I{t≥Tadopt i }-1.437 ∗∗ -3.318∗∗ -0.9569 -4.104 ∗∗∗
(0.4141) (0.9727) (0.6351) (1.100)
Fixed-effects
Customer Yes Yes Yes Yes
YearMonth Yes Yes Yes Yes
Fit statistics
Observations 99,233 27,623 40,183 42,596
R2 0.86731 0.61190 0.50654 0.42914
Within R2 0.00057 0.00135 0.00010 0.00126
Clustered (Customer & YearMonth) standard-errors in parentheses
Signif. Codes: ***: 0.001, **: 0.01, *: 0.05
vi

C Appendix to Model and Estimation
C.1 Proof for Minorization-Maximization Estimation
Proof of Theorem.We show that S(θ;θ (k)) is a minorization of L(θ(k)) at θ(k) for maximization by
checking the following requirements.
•S(θ;θ (k))≤ L(θ(k)). For a given consumer i at purchase occasion t, we denote the choice probability
of consumeritoward brandjduring purchase occasiontasP r ijt:
l(ψit;y it) =
Y
j

exp(ψijt)
1 +PJ j=1 exp(Uijt)
!yijt
(A2)
hj(ψit;y it) = ∂logl(ψ it;y it) ∂ψijt =y ijt −P rijt (A3)
hjk (ψit;y it) = ∂2 logl(ψ it;y it) ∂ψijt∂ψikt =



−P rijt(1−P rikt), j=k,
P rijtP rikt, j̸=k.
(A4)
The Taylor expansion oflogl(ψ it)at ˜ψit is
logl(ψ it;y it) = logl(˜ψit;y it)+(ψit− ˜ψit)′∇logl( ˜ψit;y it)+ 1 2 (ψit− ˜ψit)′∇2 logl(ψ ∗ it;y it)(ψit− ˜ψit).
Where
∇2 logl(ψ ∗ it;y it) =


h11(ψ∗ it;y it)h 12(ψ∗ it;y it)· · ·h 1J (ψ∗ it;y it)
h21(ψ∗ it;y it)h 22(ψ∗ it;y it)· · ·h 2J (ψ∗ it;y it)
... ... ... ...
hJ1 (ψ∗ it;y it)h J2 (ψ∗ it;y it)· · ·h JJ (ψ∗ it;y it)


=


−P ri1t(1−P ri1t)P r i1tP ri2t · · ·P r i1tP riJt
P ri2tP ri1t −P ri2t(1−P ri2t)· · ·P r i2tP riJt
... ... ... ...
P riJt P ri1t P riJt P ri2t · · · −P riJt (1−P riJt )


We have∇ 2 logl(ψ ∗ it;y it)≥ −I, i.e.,∇2 logl(ψ ∗ it;y it) +Iis semi-positive definite.
vii

Therefore,
logl(ψ it;y it)≥logl( ˜ψit;y it) + (ψit − ˜ψit)′∇logl( ˜ψit;y it)− 1 2 (ψit − ˜ψit)′(ψit − ˜ψit)
= logl(˜ψit;y it)−( ˜ψit −ψ it)′∇logl( ˜ψit;y it)− 1 2 ( ˜ψit −ψ it)′( ˜ψit −ψ it)
= logl(˜ψit;y it)− X
j
hj( ˜ψit;y it)( ˜ψijt −ψ ijt)− 1 2 X j ( ˜ψijt −ψ ijt)2
= logl(˜ψit;y it) +1 2 X j hj( ˜ψit;y it)2 − 1 2 X j ( ˜ψijt +h j( ˜ψit;y it)−ψ ijt)2.(A5)
For now, we derive a lower bound forlogl(ψ it;y it), the log-likelihood for each choice instance (i.e.,
customer-month purchase occasion). The log-likelihood function is its sum over user i and time t.
We substitute ψit and ˜ψit with the nominal utility x′ ijtα+δ ij and nominal utility evaluated at the
current estimates in the kth iteration x′ ijtα(k) +δ (k) ij , respectively. Summing over all customers over
all periods, the log-likelihoodL(θ)satisfies
L(θ)≥ L(θ(k)) +1 2 X i,j,t hj( ˜ψ(k) it ;y it)2 − 1 2 X i,j,t ( ˜ψ(k) ijt +h j( ˜ψ(k) it ;y it)−x ′ ijtα−δ ij)2
=L(θ (k)) +1 2 X i,j,t hj(x′ ijtα(k) +δ (k) ij ;y it)2
− 1 2 X i,j,t (x′ ijtα(k) +δ (k) ij +h j(x′ ijtα(k) +δ (k) ij ;y it)−x ′ ijtα−δ ij)2
(A6)
where the RHS of the above inequality isS(θ;θ (k)).
•S(θ (k);θ (k)) =L(θ(k)).
By definition,
S(θ (k);θ (k)) =L(θ(k)) +1 2 X i,j,t hj( ˜ψ(k) it ;y it)2 − 1 2 X i,j,t ( ˜ψ(k) ijt +h j( ˜ψ(k) it ;y it)−x ′ ijtα(k) −δ (k) ij )2
=L(θ (k)) +1 2 X i,j,t hj( ˜ψ(k) it ;y it)2 − 1 2 X i,j,t hj( ˜ψ(k) it ;y it)2
=L(θ (k))
(A7)
viii

D Appendix to Difference-in-Differences (DID) Analysis
D.1 Bootstrapped distribution of ATT estimates
Since the customer-month level price elasticities are estimates and not directly observed from data, to obtain
correct standard errors, we perform a customer-level block bootstrap with 500 replications. This includes (1)
resampling customers with replacement; (2) re-estimating the demand model on each bootstrapped dataset;
(3) using the estimated coefficients from that replication to compute price elasticities at the customer-month
level (e.g., insignificant demand model coefficients evaluated based on the analytical standard error in the
current bootstrap iteration is set to 0); (4) estimating the ATT via staggered DID based on these elasticity
estimates; (5) plotting and calculating the bootstrapped standard errors for the ATT and demand parameters.
Figure A3 presents the bootstrapped distribution of ATT estimates — that is, the effect of online adoption
on price elasticity, based on 500 replications.
Figure A3: Bootstrapped distribution of Overall ATT Estimates based on 500 replications with the point estimate Table 8.
(a) Dry Dog Food
 (b) Dog Hygiene
 (c) Cat Hygiene
D.2 Two-Way Fixed Effects (TWFE) Estimates
Table A4 provides TWFE estimates of online adoption on offline price elasticities estimated from the main
demand model described in Equation (7).
ix

Table A4: Two-Way Fixed Effects Estimate - Offline Price Elasticity
Dependent Variable: Offline Elasticity
Dry Dog Food Dog Hygiene Cat Hygiene
Model: (1) (2) (3)
Variables
PostOnlineAdoption -0.2145 ∗∗ -1.544∗∗∗ -0.6368∗∗∗
(0.0697) (0.3308) (0.1605)
Fixed-effects
CUSTOMER ID Yes Yes Yes
MONTHSTART Yes Yes Yes
Fit statistics
Observations 136,411 78,253 55,410
R2 0.91126 0.76395 0.82317
Within R2 0.24557 0.32091 0.32582
Bootstrapped standard-errors in parentheses via 500 replications
Signif. Codes: ***: 0.001, **: 0.01, *: 0.05
E Appendix to Generalizability and Robustness Checks
E.1 Detailed Results for the Role of Price Difference Across Channels
Figure A4 presents the probability density function (PDF) of offline and online prices (in natural log scale)
for each category at the SKU-Store-Date level. While there is substantial price variation across SKUs, the
central tendency, skewness, and dispersion of distributions for online and offline channels are quite similar.
The substantial overlap in online and offline price distribution suggests no systematic difference between
online and offline prices overall.
Figure A4: Distribution of Online and Offline Prices (Natural Log Scale) over SKU-Date - PDF
(a) Dry Dog Food
 (b) Dog Hygiene
 (c) Cat Hygiene
To formally compare offline and online prices, we construct a sample at the SKU-Channel-Store-Date
level. Each row represents the price of a specific SKU on a particular channel (online or offline) at a specific
x

store and date. We then estimate the following model:
ln(SKU Pricekstc) =β×isOnline c +SKU k +Date t +ϵ kstc (A8)
where the SKU Pricekstc refers to the selling price of SKU k of store s at time t. The index c refers to
the online or offline channel. Here, a negative β would indicate that, on average, online prices are lower
than offline prices for the same SKU on the same date, and vice versa. Table A5 presents the regression
result for comparing online and offline prices in Equation (A8) for three categories. Table A6 presents the
regression results of decomposing SKU price variation for each category. Column (1) of Table A6 only
includes the channel indicator,isOnline, and Column (2) includes both channel indicator and SKU fixed
effects. Comparing the R-squared values in Table A6, we see that the price variation across channels is far
smaller than the price variation across SKUs.
Table A5: Descriptive Analysis - Online vs. Offline Prices at the SKU-Date Level
Dependent Variable: ln(SKU Price)
Dry Dog Food Dog Hygiene Cat Hygiene
Model: (1) (2) (3)
Variables
isOnline -0.0322 ∗∗∗ -0.0361∗ -0.0607∗∗∗
(0.0022) (0.0135) (0.0087)
Fixed-effects
SKU Yes Yes Yes
DATE Yes Yes Yes
Fit statistics
Observations 554,191 328,323 244,723
R2 0.95202 0.98493 0.91763
Within R2 0.01819 0.00912 0.02441
Clustered (SKU & DATE) standard-errors in parentheses
Signif. Codes: ***: 0.001, **: 0.01, *: 0.05
xi

Table A6: Descriptive Analysis - SKU-Level Price Variation Decomposition. Compared to column 1, column 2 controls for SKU
fixed effects, indicating that after holding SKU constant, the price variation attributable to the online-offline channel is very small.
Dependent Variable: ln(SKU Price)
Dry Dog Food Dog Hygiene Cat Hygiene
Model: (1) (2) (1) (2) (1) (2)
Variables
Constant 4.941 ∗∗∗ 4.043∗∗∗ 3.224∗∗∗
(0.0439) (0.1420) (0.0769)
isOnline 0.0659 ∗ -0.0313∗∗∗ -0.0123 -0.0382 ∗ -0.0726∗ -0.0594∗∗∗
(0.0287) (0.0025) (0.0269) (0.0135) (0.0304) (0.0087)
Fixed-effects
SKU Yes Yes Yes
Fit statistics
Observations 554,191 554,191 328,323 328,323 244,723 244,723
R2 0.00398 0.895161.61×10 −5 0.95365 0.00309 0.84228
Within R2 0.00797 0.00333 0.01235
Clustered (SKU & DATE) standard-errors in parentheses
Signif. Codes: ***: 0.001, **: 0.01, *: 0.05
E.2 Detailed Results for Alternative Demand Model Specifications
E.2.1 Results for Alternate Demand Specification with Binary Adoption Variable
The alternative demand model specification is given by:
ψijt =α 0Pricejt +α 1Post OnlineAdoptionit +α 2Pricejt ×Post OnlineAdoptionit
+α 3I{BuyPrevOccaijt}+β 1CF Pricejt +β 2CF Price Post OnlineAdoptionijt +δ ij ∀j∈ {1, . . . , J}
(A9)
To address the endogeneity of Pricejt and its interaction with Post OnlineAdoptionit, we use the control
function approach with instruments Costjt and Costjt ×Post OnlineAdoptionit, and construct two control
function terms, CF Pricejt and CF Price Post OnlineAdoptionijt. We then estimate the above demand model
and compute the average elasticity at the customer-month level for each product category following the same
steps as before. The results are shown below.
Table A7 presents the estimates of the demand model. The standard errors for the demand parameters are
based on the customer-level block bootstrap with 500 replications.
Table A8 presents the ATT estimates of offline price elasticity from CS Estimator based on the demand
model in Equation (A9). The standard errors for the ATT estimates and the demand model parameters are
based on the customer-level block bootstrap with 500 replications; See Figure A5.
xii

Table A7: Coefficient Estimates of Demand Model in Equation (A9) - Binary Online Adoption Variable
Dry Dog Food Dry Cat Food Dog Hygiene Cat Hygiene
Variables
Price -0.3031∗∗∗
(0.0171)
-0.1577∗∗∗
(0.0202)
-1.0463∗∗∗
(0.1123)
-0.2038∗∗∗
(0.0199)
Post OnlineAdoption -0.0834 (0.1341) -0.2483 (0.398) 2.1377∗∗∗ (0.3641) 1.8521∗∗∗ (0.3083)
Price * Post OnlineAdoption -0.034∗∗
(0.0123)
-0.004
(0.0337)
-1.0684∗∗∗
(0.159)
-0.1432∗∗∗
(0.0218)
BuyPrevOcca 0.1561∗∗∗
(0.0273)
-0.4977∗∗∗
(0.0451)
-0.1802∗∗∗
(0.0283)
0.3216∗∗∗
(0.0295)
CF Price 0.042 (0.0237) 0.039 (0.0268) 0.0572 (0.1622) 0.2797∗∗∗ (0.0261)
CF Price Post OnlineAdoption 0.0521∗∗
(0.0175)
0.038
(0.0343)
0.6873∗∗
(0.2196)
0.0609∗
(0.0256)
Customer Brand FE Yes Yes Yes Yes
Observations 136,411 45,443 78,253 55,410
Log-likelihood -84085.187 -30700.989 -55426.656 -37292.32
Bootstrapped standard-errors in parentheses via 500 replications
Signif. Codes: ***: 0.001, **: 0.01, *: 0.05
Table A8: ATT of Online Adoption on Offline Price Elasticity (CS Estimator) - Binary Adoption Variable
Dependent Variable: Offline Price Elasticity
Dry Dog Food Dog Hygiene Cat Hygiene
Model: (1) (2) (3)
CS -0.3711 ∗∗ -2.3513∗∗∗ -1.614∗∗∗
(0.1224) (0.3407) (0.2353)
Observations 136,411 78,253 55,410
Bootstrapped standard-errors in parentheses via 500 replications
Signif. Codes: ***: 0.001, **: 0.01, *: 0.05
Figure A5: Bootstrapped distribution of Overall ATT Estimates based on 500 replications with the point estimate from Table A8.
(a) Dry Dog Food
 (b) Dog Hygiene
 (c) Cat Hygiene
xiii

E.2.2 Results for Alternate Demand Model Controlling for State Dependence due to Online Adoption
The alternative utility specification is given by:
ψijt =α 0Pricejt +α 1cumPercOnlineSpendit +α 2Pricejt ×cumPercOnlineSpend it
+α 3I{BuyPrevOccaijt}+α 4I{BuyPrevOccaijt} ×cumPercOnlineSpendit
+β 1CF Pricejt +β 2CF Price cumPercOnlineSpendijt +δ ij ∀j∈ {1, . . . , J}
(A10)
We estimate this model and again obtain the customer-month level average elasticity for each category as
before. Table A9 presents the estimates of the demand model. The standard errors for the demand model
parameters are based on the customer-level block bootstrap with 500 replications.
Table A9: Coefficient Estimates of Demand Model in Equation (A10) - Controlling for Interaction between Online Spend and Brand
Loyalty
Dry Dog Food Dry Cat Food Dog Hygiene Cat Hygiene
Variables
Price -0.3157∗∗∗
(0.0159)
-0.1618∗∗∗
(0.0172)
-1.2497∗∗∗
(0.1142)
-0.2209∗∗∗
(0.0186)
cumPercOnlineSpend -0.3383 (0.4039) -1.5509 (1.2012) 8.6901∗∗∗ (1.8059) 3.4632∗∗∗ (0.9725)
Price * cumPercOnlineSpend -0.1092∗∗
(0.0366)
0.0227
(0.0994)
-4.1435∗∗∗
(0.7895)
-0.284∗∗∗
(0.0661)
BuyPrevOcca 0.1592∗∗∗
(0.0278)
-0.5249∗∗∗
(0.047)
-0.1894∗∗∗
(0.0294)
0.3242∗∗∗
(0.0306)
CF Price 0.0521∗
(0.0219)
0.048
(0.0245)
0.1936
(0.1673)
0.2803∗∗∗
(0.0247)
CF Price cumPercOnlineSpend 0.0212 (0.0719) -0.0595 (0.1169) 3.6167∗∗∗ (0.9742) 0.3009∗∗ (0.0915)
BuyPrevOcca * cumPercOnlineSpend -0.3059 (0.2918) 1.0106∗∗ (0.3853) 0.2991 (0.3022) 0.0133 (0.2768)
Customer Brand FE Yes Yes Yes Yes
Observations 136,411 45,443 78,253 55,410
Log-likelihood -84209.589 -30693.216 -55438.072 -37327.394
Bootstrapped standard-errors in parentheses via 500 replications
Signif. Codes: ***: 0.001, **: 0.01, *: 0.05
Table A10 presents the ATT estimates of offline price elasticity from the CS estimator based on the
demand model in Equation (A10). The standard errors for the ATT estimates are based on the customer-level
block bootstrap with 500 replications; See Figure A6.
xiv

Table A10: ATT of Online Adoption on Offline Price Elasticity (CS Estimator) - Controlling for State Dependence due to Online
Adoption
Dependent Variable: Offline Price Elasticity
Dry Dog Food Dog Hygiene Cat Hygiene
Model: (1) (2) (3)
CS -0.2429 ∗∗ -1.7868∗∗∗ -0.7382∗∗∗
(0.0797) (0.3544) (0.1668)
Observations 136,411 78,253 55,410
Bootstrapped standard-errors in parentheses via 500 replications
Signif. Codes: ***: 0.001, **: 0.01, *: 0.05
Figure A6: Bootstrapped distribution of Overall ATT Estimates based on 500 replications with the point estimate from Table A10.
(a) Dry Dog Food
 (b) Dog Hygiene
 (c) Cat Hygiene
xv

E.3 Detailed results for testing the Parallel Pre-Trend Assumption
A fundamental condition for the credibility of the estimates presented in§7.3 is the parallel trends assumption.
We assess it with an event-study figure following Callaway and Sant’Anna (2021). Figure A7 plots the point
estimates and 95% bootstrapped confidence interval for each pre- and post-treatment period, and shows that
all pre-treatment coefficients are insignificant from zero. We do not exhibit discernible pre-trends. In addition,
the p-values from the Wald tests of the pre-trend assumption are greater than 5% level of significance in each
category. We therefore conclude that the parallel trend assumption is reasonably satisfied throughout the
analysis.
E.4 Detailed Results for Matching, IPW Approaches to Control for Selection on Observables
For each of the adoption cohorts under a product category, we estimate the following propensity score model:
PropensityScorei =f(X T i θ),(A11)
where f(·) is the logit link function where f(X T i θ) = 1 1+exp(−X T i θ) . θ∈ RM×1 is a column vector of
coefficients. Xi ∈ RM×1 is a column vector with M covariates of customer i, including demographics
(e.g., gender, age and income) and the pre-adoption monthly purchase average measured using data up to the
adoption period of the adoption cohort. For example, for customers who adopted in July 2019, we measure
the pre-adoption variables for both adopters and non-adopters using the data up to June 30, 2019, and estimate
the propensity score model for the adoption cohort in July 2019.
Tables A11 and A12 present the propensity score model estimates for the twelve adoption cohorts in
the dry dog food, dog hygiene and cat hygiene categories, respectively. Similarly, Tables A13 and A14
provide results for dog hygiene and Tables A15 and A16 provide results for cat hygiene. We find that certain
observables, such as being female, having a high household income, and having a high pre-adoption monthly
spend, increase the likelihood of adopting online shopping.
Using the predicted propensity score, we apply the R packageMatchItto conduct one-to-one nearest
neighbor matching with replacement for each adoption cohort Stuart et al. (2011). For each product category,
we first estimate the ATT using the CS based on the matched sample, with results shown in Web Appendix
§E.4 Table A17. Second, we estimate the ATT using the CS estimator with the inverse propensity score
weighting (IPW) method, with results shown in Table A18. These findings are consistent with our main
results, demonstrating that consumers become more price sensitive offline after adopting online shopping.
Detailed results are below.
xvi

Figure A7: Parallel Pre-Trends Evaluation and Dynamic Effect during the Pre- and Post-Adoption Periods
(a) Dry Dog Food
(b) Dog Hygiene
(c) Cat Hygiene
xvii

Table A11: Propensity Score Logit Model for Dry Dog Food - Adopter Cohorts between 2019-07 and 2019-12 vs. Non-Adopters
Dependent variable:
Adopter
2019-07 2019-08 2019-09 2019-10 2019-11 2019-12
Gender Female 0.288 ∗∗∗ 0.382∗∗∗ 0.671∗∗∗ 1.030∗∗∗ 0.655∗∗∗ 0.283∗∗∗
(0.078) (0.072) (0.078) (0.073) (0.062) (0.064)
Gender NoInformation−0.944 ∗∗∗ −0.177 0.354 ∗∗∗ −0.114 0.367 ∗∗∗ −0.180
(0.155) (0.111) (0.104) (0.122) (0.083) (0.095)
Age≥50−0.599 ∗∗∗ −0.874∗∗∗ −0.354∗ −0.777∗∗∗ −1.654∗∗∗ −1.523∗∗∗
(0.166) (0.175) (0.160) (0.153) (0.111) (0.112)
Age30 40 0.140 0.667 ∗∗∗ 0.410∗∗ −0.047−0.269 ∗∗ −0.677∗∗∗
(0.161) (0.163) (0.156) (0.149) (0.100) (0.106)
Age40 50−0.077 0.134−0.143 0.204−1.012 ∗∗∗ −0.891∗∗∗
(0.163) (0.165) (0.161) (0.145) (0.106) (0.107)
Age NoInformation−1.798 ∗∗∗ −1.188∗∗∗ −1.496∗∗∗ −2.105∗∗∗ −2.036∗∗∗ −2.120∗∗∗
(0.272) (0.226) (0.245) (0.267) (0.163) (0.174)
Income<1000−0.417 ∗∗∗ −0.302∗∗ 0.038−0.047−0.256 ∗∗∗ −0.314∗∗∗
(0.105) (0.102) (0.093) (0.088) (0.075) (0.081)
Income≥2000 0.223 ∗ 0.762∗∗∗ 0.149 0.043 0.197 ∗∗ 0.181∗
(0.095) (0.088) (0.093) (0.088) (0.073) (0.077)
Income NoInformation−0.063 0.060−0.272 ∗ −0.651∗∗∗ −0.363∗∗∗ −0.075
(0.120) (0.116) (0.125) (0.129) (0.097) (0.097)
AvgSpendPerMonth 0.001 ∗∗∗ 0.001∗∗∗ 0.001∗∗∗ 0.001∗∗∗ 0.0002∗∗ 0.0001
(0.0001) (0.0001) (0.0001) (0.0001) (0.0001) (0.0001)
AvgQuantitiesPerMonth−0.095 ∗∗∗ −0.108∗∗∗ −0.058∗∗ 0.010∗ −0.008 0.010
(0.025) (0.024) (0.018) (0.005) (0.008) (0.009)
AvgUniqueItemsPerMonth−0.221 ∗ 0.231∗ −0.507∗∗∗ −0.444∗∗∗ −0.235∗∗ −0.166∗
(0.105) (0.090) (0.105) (0.090) (0.074) (0.079)
AvgUniqueOrdersPerMonth 0.200 ∗∗ −0.653∗∗∗ −0.195∗ −0.555∗∗∗ 0.048−0.027
(0.075) (0.102) (0.084) (0.102) (0.062) (0.071)
AvgUniqueBrandsPerMonth 0.298 ∗ 0.148 0.662 ∗∗∗ 0.778∗∗∗ 0.188 0.365 ∗∗
(0.145) (0.133) (0.151) (0.150) (0.121) (0.126)
AvgUniqueSubcategoriesPerMonth 0.132−0.079 1.189 ∗∗∗ −0.129 0.243−0.306
(0.164) (0.175) (0.181) (0.183) (0.164) (0.162)
AvgUniqueCategoriesPerMonth 0.046 0.019−1.069 ∗∗∗ 0.172 0.222 0.522 ∗∗∗
(0.142) (0.159) (0.160) (0.158) (0.144) (0.155)
Intercept−2.549 ∗∗∗ −2.504∗∗∗ −2.851∗∗∗ −2.536∗∗∗ −1.535∗∗∗ −1.311∗∗∗
(0.178) (0.180) (0.177) (0.165) (0.117) (0.118)
Observations 8,023 8,049 8,038 8,048 8,112 8,082
Log Likelihood−2,586.499−2,989.092−2,841.850−2,963.057−4,088.072−3,736.394
Akaike Inf. Crit. 5,206.999 6,012.184 5,717.700 5,960.113 8,210.144 7,506.788
Note: ∗p<0.05; ∗∗p<0.01; ∗∗∗p<0.001
xviii

Table A12: Propensity Score Logit Model for Dry Dog Food - Adopter Cohorts between 2020-01 and 2020-06 vs. Non-Adopters
Dependent variable:
Adopter
2020-01 2020-02 2020-03 2020-04 2020-05 2020-06
Gender Female 0.677 ∗∗∗ 0.473∗∗∗ 0.386∗∗∗ 0.658∗∗∗ 0.736∗∗∗ 0.475∗∗∗
(0.065) (0.064) (0.048) (0.044) (0.047) (0.050)
Gender NoInformation−0.223 ∗ −0.331∗∗ −0.098 0.176 ∗∗ 0.134∗ −0.072
(0.105) (0.103) (0.070) (0.062) (0.067) (0.074)
Age≥50−0.957 ∗∗∗ −0.966∗∗∗ −1.150∗∗∗ −1.143∗∗∗ −0.923∗∗∗ −1.165∗∗∗
(0.118) (0.129) (0.093) (0.084) (0.090) (0.097)
Age30 40−0.378 ∗∗ −0.105−0.313 ∗∗∗ −0.403∗∗∗ −0.060−0.113
(0.115) (0.122) (0.090) (0.083) (0.088) (0.092)
Age40 50−0.682 ∗∗∗ −0.363∗∗ −0.698∗∗∗ −0.602∗∗∗ −0.602∗∗∗ −0.742∗∗∗
(0.118) (0.124) (0.091) (0.083) (0.090) (0.095)
Age NoInformation−2.308 ∗∗∗ −2.600∗∗∗ −1.399∗∗∗ −2.220∗∗∗ −2.318∗∗∗ −1.690∗∗∗
(0.215) (0.256) (0.119) (0.127) (0.151) (0.136)
Income<1000−0.211 ∗ 0.212∗∗ 0.051−0.223 ∗∗∗ −0.061−0.470 ∗∗∗
(0.082) (0.080) (0.061) (0.055) (0.058) (0.060)
Income≥2000 0.115 0.163 ∗ 0.481∗∗∗ 0.335∗∗∗ 0.210∗∗∗ −0.334∗∗∗
(0.079) (0.083) (0.058) (0.053) (0.057) (0.061)
Income NoInformation−0.093−0.149−0.159 ∗ −0.450∗∗∗ −0.215∗∗ −0.570∗∗∗
(0.100) (0.106) (0.078) (0.071) (0.074) (0.078)
AvgSpendPerMonth 0.0004 ∗∗∗ 0.0002 0.0005 ∗∗∗ 0.0004∗∗∗ 0.001∗∗∗ 0.0001
(0.0001) (0.0001) (0.0001) (0.0001) (0.0001) (0.0001)
AvgQuantitiesPerMonth−0.051 ∗∗ −0.008−0.011 0.009−0.013−0.034 ∗∗
(0.016) (0.012) (0.008) (0.007) (0.008) (0.011)
AvgUniqueItemsPerMonth−0.285 ∗∗ −0.557∗∗∗ −0.156∗ −0.076−0.028−0.029
(0.095) (0.099) (0.061) (0.054) (0.069) (0.076)
AvgUniqueOrdersPerMonth−0.223 ∗∗ −0.409∗∗∗ −0.558∗∗∗ −0.455∗∗∗ −0.786∗∗∗ −0.267∗∗∗
(0.085) (0.084) (0.066) (0.062) (0.075) (0.065)
AvgUniqueBrandsPerMonth 0.553 ∗∗∗ 1.275∗∗∗ 0.286∗∗ −0.134 0.413 ∗∗∗ 0.547∗∗∗
(0.143) (0.150) (0.103) (0.086) (0.113) (0.119)
AvgUniqueSubcategoriesPerMonth 0.015−0.410 ∗ 0.467∗∗∗ 0.088−0.627 ∗∗∗ −0.426∗
(0.184) (0.181) (0.126) (0.126) (0.155) (0.166)
AvgUniqueCategoriesPerMonth 0.243 0.279 0.025 0.836 ∗∗∗ 0.907∗∗∗ 0.374∗
(0.165) (0.178) (0.121) (0.122) (0.139) (0.149)
Intercept−1.852 ∗∗∗ −2.011∗∗∗ −1.158∗∗∗ −0.870∗∗∗ −1.039∗∗∗ −0.715∗∗∗
(0.132) (0.136) (0.099) (0.091) (0.099) (0.101)
Observations 8,076 8,081 8,272 8,376 8,295 8,214
Log Likelihood−3,577.410−3,603.534−6,105.810−7,120.955−6,365.540−5,585.395
Akaike Inf. Crit. 7,188.819 7,241.067 12,245.620 14,275.910 12,765.080 11,204.790
Note: ∗p<0.05; ∗∗p<0.01; ∗∗∗p<0.001
xix

Table A13: Propensity Score Logit Model for Dog Hygiene - Adopter Cohorts between 2019-07 and 2019-12 vs. Non-Adopters
Dependent variable:
Adopter
2019-07 2019-08 2019-09 2019-10 2019-11 2019-12
Gender Female 0.809 ∗∗∗ 0.697∗∗∗ 0.552∗∗∗ 0.267∗∗ 0.436∗∗∗ 0.253∗∗
(0.118) (0.105) (0.089) (0.092) (0.075) (0.080)
Gender NoInformation−0.169 0.501 ∗∗∗ −0.695∗∗∗ −0.035 0.076 0.037
(0.197) (0.145) (0.164) (0.135) (0.109) (0.116)
Age≥50−0.636 ∗ −1.062∗∗∗ −1.063∗∗∗ −0.713∗∗∗ −0.771∗∗∗ −1.237∗∗∗
(0.275) (0.198) (0.171) (0.183) (0.165) (0.170)
Age30 40 0.610 ∗ −0.246−0.244−0.264 0.077−0.046
(0.261) (0.192) (0.164) (0.179) (0.160) (0.159)
Age40 50 0.148−0.400 ∗ −0.705∗∗∗ −0.442∗ −0.103−0.354 ∗
(0.264) (0.194) (0.167) (0.179) (0.160) (0.161)
Age NoInformation−0.059−1.842 ∗∗∗ −2.730∗∗∗ −1.562∗∗∗ −0.930∗∗∗ −2.127∗∗∗
(0.303) (0.302) (0.358) (0.266) (0.208) (0.277)
Income<1000−0.354 ∗ −0.558∗∗∗ −0.183 0.186 0.167−0.492 ∗∗∗
(0.176) (0.163) (0.124) (0.119) (0.099) (0.117)
Income≥2000 0.307 ∗ 0.345∗∗ −0.239∗ −0.286∗∗ 0.074−0.043
(0.127) (0.107) (0.101) (0.104) (0.084) (0.087)
Income NoInformation 0.535 ∗∗ −0.225 0.540 ∗∗∗ −0.029−0.043 0.009
(0.165) (0.169) (0.123) (0.143) (0.119) (0.122)
AvgSpendPerMonth 0.001 ∗∗∗ 0.001∗∗∗ 0.0004∗∗ 0.001∗∗∗ 0.0002 0.001 ∗∗∗
(0.0001) (0.0001) (0.0001) (0.0001) (0.0001) (0.0001)
AvgQuantitiesPerMonth−0.147 ∗∗∗ 0.015−0.148 ∗∗∗ −0.029−0.039 ∗∗ −0.087∗∗∗
(0.036) (0.009) (0.029) (0.016) (0.013) (0.020)
AvgUniqueItemsPerMonth−0.043−0.249 ∗∗∗ −0.013−0.145−0.327 ∗∗∗ −0.149
(0.115) (0.072) (0.089) (0.078) (0.071) (0.092)
AvgUniqueOrdersPerMonth−0.065 0.187 ∗∗ −0.684∗∗∗ −0.455∗∗∗ −0.149∗ −0.103
(0.091) (0.069) (0.095) (0.091) (0.061) (0.092)
AvgUniqueBrandsPerMonth 0.475 ∗∗∗ 0.462∗∗∗ 0.448∗∗∗ 0.399∗∗ 0.425∗∗∗ −0.253∗
(0.141) (0.123) (0.136) (0.123) (0.114) (0.129)
AvgUniqueSubcategoriesPerMonth 0.161 0.023 0.199 0.048 0.655 ∗∗∗ 1.241∗∗∗
(0.167) (0.161) (0.169) (0.151) (0.141) (0.178)
AvgUniqueCategoriesPerMonth−0.463 ∗∗ −0.239 0.068 0.095−0.305 ∗ −0.512∗∗∗
(0.161) (0.156) (0.157) (0.146) (0.134) (0.152)
Intercept−3.145 ∗∗∗ −2.318∗∗∗ −1.544∗∗∗ −1.800∗∗∗ −1.721∗∗∗ −1.348∗∗∗
(0.296) (0.223) (0.196) (0.205) (0.186) (0.182)
Observations 3,634 3,653 3,678 3,664 3,725 3,702
Log Likelihood−1,353.099−1,680.290−1,967.035−1,897.595−2,712.319−2,353.311
Akaike Inf. Crit. 2,740.197 3,394.581 3,968.071 3,829.189 5,458.638 4,740.623
Note: ∗p<0.05; ∗∗p<0.01; ∗∗∗p<0.001
xx

Table A14: Propensity Score Logit Model for Dog Hygiene - Adopter Cohorts between 2020-01 and 2020-06 vs. Non-Adopters
Dependent variable:
Adopter
2020-01 2020-02 2020-03 2020-04 2020-05 2020-06
Gender Female 0.627 ∗∗∗ 0.370∗∗∗ 0.413∗∗∗ 0.582∗∗∗ 0.571∗∗∗ 0.435∗∗∗
(0.092) (0.086) (0.056) (0.054) (0.057) (0.063)
Gender NoInformation 0.579 ∗∗∗ 0.172−0.093−0.333 ∗∗∗ 0.053−0.056
(0.123) (0.121) (0.083) (0.085) (0.084) (0.093)
Age≥50−1.372 ∗∗∗ −1.130∗∗∗ −1.080∗∗∗ −0.834∗∗∗ −1.256∗∗∗ −1.169∗∗∗
(0.171) (0.168) (0.114) (0.119) (0.121) (0.128)
Age30 40−0.134−0.341 ∗ −0.483∗∗∗ −0.122−0.318 ∗∗ −0.274∗
(0.157) (0.162) (0.114) (0.118) (0.118) (0.123)
Age40 50−0.802 ∗∗∗ −0.800∗∗∗ −0.964∗∗∗ −0.261∗ −0.675∗∗∗ −0.825∗∗∗
(0.163) (0.165) (0.114) (0.117) (0.119) (0.125)
Age NoInformation−1.945 ∗∗∗ −2.592∗∗∗ −2.108∗∗∗ −1.115∗∗∗ −1.837∗∗∗ −2.046∗∗∗
(0.252) (0.286) (0.162) (0.148) (0.160) (0.184)
Income<1000 0.277 ∗ −0.157−0.118−0.144−0.222 ∗∗ −0.182∗
(0.118) (0.125) (0.081) (0.077) (0.081) (0.090)
Income≥2000 0.304 ∗∗ 0.246∗∗ 0.430∗∗∗ 0.331∗∗∗ 0.233∗∗∗ 0.263∗∗∗
(0.100) (0.095) (0.062) (0.060) (0.062) (0.069)
Income NoInformation−0.080 0.119−0.263 ∗∗ −0.317∗∗∗ −0.059−0.137
(0.144) (0.134) (0.096) (0.092) (0.093) (0.105)
AvgSpendPerMonth 0.001 ∗∗∗ 0.001∗∗∗ 0.001∗∗∗ 0.001∗∗∗ 0.001∗∗∗ 0.0005∗∗∗
(0.0001) (0.0001) (0.0001) (0.0001) (0.0001) (0.0001)
AvgQuantitiesPerMonth−0.150 ∗∗∗ −0.007 0.011−0.046 ∗∗∗ −0.009−0.014
(0.024) (0.007) (0.008) (0.012) (0.009) (0.009)
AvgUniqueItemsPerMonth 0.140−0.345 ∗∗∗ −0.139∗∗ 0.056−0.185 ∗∗ 0.138∗
(0.085) (0.075) (0.054) (0.065) (0.058) (0.070)
AvgUniqueOrdersPerMonth−0.124−0.080−0.172 ∗∗∗ −0.498∗∗∗ −0.372∗∗∗ −0.605∗∗∗
(0.084) (0.088) (0.038) (0.064) (0.067) (0.084)
AvgUniqueBrandsPerMonth−0.050 0.436 ∗∗∗ 0.087−0.224 ∗ 0.242∗∗ −0.292∗
(0.133) (0.113) (0.091) (0.102) (0.093) (0.116)
AvgUniqueSubcategoriesPerMonth 0.951 ∗∗∗ 0.664∗∗∗ 0.487∗∗∗ 0.922∗∗∗ 0.502∗∗∗ 0.919∗∗∗
(0.171) (0.156) (0.116) (0.126) (0.131) (0.147)
AvgUniqueCategoriesPerMonth−0.616 ∗∗∗ −0.769∗∗∗ −0.139−0.257 ∗ −0.264∗ −0.394∗∗
(0.154) (0.160) (0.113) (0.117) (0.135) (0.139)
Intercept−2.091 ∗∗∗ −1.383∗∗∗ −0.282∗ −0.497∗∗∗ −0.247−0.426 ∗∗
(0.196) (0.190) (0.125) (0.134) (0.132) (0.141)
Observations 3,689 3,688 3,964 4,024 3,935 3,842
Log Likelihood−2,067.730−2,175.618−4,499.026−4,832.667−4,400.367−3,656.464
Akaike Inf. Crit. 4,169.460 4,385.235 9,032.052 9,699.334 8,834.733 7,346.928
Note: ∗p<0.05; ∗∗p<0.01; ∗∗∗p<0.001
xxi

Table A15: Propensity Score Logit Model for Cat Hygiene - Adopter Cohorts between 2019-07 and 2019-12 vs. Non-Adopters
Dependent variable:
Adopter
2019-07 2019-08 2019-09 2019-10 2019-11 2019-12
Gender Female 0.835 ∗∗∗ 0.450∗∗∗ 0.986∗∗∗ 0.823∗∗∗ 0.526∗∗∗ 0.364∗∗∗
(0.141) (0.129) (0.130) (0.131) (0.107) (0.107)
Gender NoInformation 0.055 0.315−0.655 ∗ 0.164 0.034−0.424 ∗
(0.229) (0.179) (0.259) (0.195) (0.158) (0.179)
Age≥50−0.024−0.217−0.605 ∗ −0.916∗∗∗ −0.503−0.764 ∗∗
(0.361) (0.353) (0.277) (0.218) (0.264) (0.236)
Age30 40 1.468 ∗∗∗ 1.077∗∗ 0.730∗∗ −0.334 1.052 ∗∗∗ 0.182
(0.352) (0.345) (0.270) (0.219) (0.254) (0.234)
Age40 50 0.302 0.325 0.057−0.929 ∗∗∗ 0.504∗ 0.031
(0.361) (0.349) (0.269) (0.222) (0.255) (0.229)
Age NoInformation−15.840−0.103−16.557−17.598−1.475 ∗∗∗ −1.916∗∗∗
(380.738) (0.404) (382.142) (380.148) (0.408) (0.394)
Income<1000 0.269−0.407 ∗ −0.334∗ −0.417∗ −0.544∗∗∗ −0.396∗
(0.229) (0.182) (0.161) (0.199) (0.153) (0.171)
Income≥2000 1.356 ∗∗∗ −0.137−0.495 ∗∗∗ 0.368∗∗ 0.076 0.440 ∗∗∗
(0.171) (0.134) (0.126) (0.130) (0.110) (0.117)
Income NoInformation 0.072−0.148−1.423 ∗∗∗ −0.066−0.364 ∗ −0.507∗
(0.281) (0.187) (0.255) (0.193) (0.171) (0.200)
AvgSpendPerMonth 0.001 ∗∗ 0.001∗∗∗ 0.001∗∗∗ 0.002∗∗∗ −0.0001 0.0002
(0.0002) (0.0001) (0.0002) (0.0002) (0.0001) (0.0002)
AvgQuantitiesPerMonth 0.018 ∗ −0.003 0.005−0.076 ∗∗∗ 0.044∗∗∗ 0.009
(0.008) (0.008) (0.009) (0.015) (0.006) (0.008)
AvgUniqueItemsPerMonth−0.213 ∗ 0.101−0.104 0.241 ∗∗ −0.649∗∗∗ −0.268∗∗
(0.090) (0.053) (0.079) (0.078) (0.094) (0.082)
AvgUniqueOrdersPerMonth−0.076−0.176 ∗ −0.340∗∗ −0.804∗∗∗ −0.962∗∗∗ −0.716∗∗∗
(0.109) (0.084) (0.104) (0.116) (0.126) (0.115)
AvgUniqueBrandsPerMonth 0.116−0.003 0.143−0.528 ∗∗∗ 0.813∗∗∗ −0.002
(0.186) (0.117) (0.138) (0.157) (0.172) (0.159)
AvgUniqueSubcategoriesPerMonth 0.417−0.514 ∗∗ −0.142−0.009 0.608 ∗∗ −0.093
(0.225) (0.160) (0.206) (0.206) (0.207) (0.193)
AvgUniqueCategoriesPerMonth−0.786 ∗∗∗ 0.757∗∗∗ 0.394∗ 0.798∗∗∗ −0.209 1.401 ∗∗∗
(0.228) (0.167) (0.198) (0.211) (0.196) (0.194)
Intercept−3.263 ∗∗∗ −3.235∗∗∗ −2.481∗∗∗ −2.102∗∗∗ −2.167∗∗∗ −2.533∗∗∗
(0.401) (0.371) (0.299) (0.253) (0.268) (0.256)
Observations 2,761 2,766 2,769 2,772 2,792 2,783
Log Likelihood−908.558−1,079.992−1,078.742−1,114.206−1,440.825−1,336.839
Akaike Inf. Crit. 1,851.117 2,193.985 2,191.483 2,262.411 2,915.651 2,707.678
Note: ∗p<0.05; ∗∗p<0.01; ∗∗∗p<0.001
xxii

Table A16: Propensity Score Logit Model for Cat Hygiene - Adopter Cohorts between 2020-01 and 2020-06 vs. Non-Adopters
Dependent variable:
Adopter
2020-01 2020-02 2020-03 2020-04 2020-05 2020-06
Gender Female 0.798 ∗∗∗ 0.887∗∗∗ 0.490∗∗∗ 0.459∗∗∗ 0.357∗∗∗ 0.702∗∗∗
(0.131) (0.122) (0.071) (0.068) (0.068) (0.078)
Gender NoInformation 0.835 ∗∗∗ 0.334−0.072 0.224 ∗ −0.370∗∗∗ 0.232∗
(0.164) (0.176) (0.108) (0.094) (0.106) (0.111)
Age≥50−0.962 ∗∗∗ −1.164∗∗∗ −0.881∗∗∗ −0.896∗∗∗ −1.128∗∗∗ −1.857∗∗∗
(0.253) (0.202) (0.141) (0.130) (0.132) (0.133)
Age30 40 0.505 ∗ −0.194−0.145−0.237−0.319 ∗ −0.801∗∗∗
(0.240) (0.195) (0.142) (0.131) (0.133) (0.130)
Age40 50−0.014−0.816 ∗∗∗ −0.727∗∗∗ −0.629∗∗∗ −0.890∗∗∗ −1.147∗∗∗
(0.240) (0.199) (0.141) (0.130) (0.133) (0.128)
Age NoInformation−0.407−2.189 ∗∗∗ −2.352∗∗∗ −2.549∗∗∗ −1.864∗∗∗ −3.821∗∗∗
(0.298) (0.370) (0.237) (0.231) (0.190) (0.344)
Income<1000−0.463 ∗∗ 0.008−0.241 ∗ 0.499∗∗∗ −0.160−0.097
(0.174) (0.140) (0.104) (0.091) (0.095) (0.107)
Income≥2000 0.122−0.463 ∗∗∗ 0.428∗∗∗ 0.465∗∗∗ 0.038 0.307 ∗∗∗
(0.124) (0.123) (0.077) (0.075) (0.074) (0.082)
Income NoInformation−0.508 ∗ −0.588∗∗ −0.516∗∗∗ 0.224∗ −0.367∗∗ −0.214
(0.205) (0.194) (0.131) (0.108) (0.113) (0.128)
AvgSpendPerMonth−0.002 ∗∗∗ 0.0004∗ −0.00003 0.0003 ∗∗ −0.00001−0.0002
(0.0003) (0.0002) (0.0001) (0.0001) (0.0001) (0.0001)
AvgQuantitiesPerMonth 0.031 ∗∗ 0.012 0.008−0.001 0.008 0.012
(0.012) (0.010) (0.006) (0.006) (0.006) (0.007)
AvgUniqueItemsPerMonth−0.673 ∗∗∗ −0.410∗∗∗ −0.090∗ −0.029−0.072−0.146 ∗
(0.108) (0.091) (0.040) (0.038) (0.045) (0.058)
AvgUniqueOrdersPerMonth−0.330 ∗∗ −0.696∗∗∗ −0.214∗∗∗ −0.482∗∗∗ −0.512∗∗∗ −0.174∗∗
(0.119) (0.112) (0.060) (0.068) (0.066) (0.058)
AvgUniqueBrandsPerMonth 0.586 ∗∗ 0.323∗ 0.167 0.006−0.135 0.205
(0.192) (0.157) (0.085) (0.085) (0.093) (0.111)
AvgUniqueSubcategoriesPerMonth 0.745 ∗∗ 0.984∗∗∗ 0.073−0.027 0.787 ∗∗∗ 0.762∗∗∗
(0.253) (0.169) (0.115) (0.095) (0.128) (0.157)
AvgUniqueCategoriesPerMonth 0.231−0.441 ∗∗ 0.326∗∗ 0.642∗∗∗ −0.109−0.721 ∗∗∗
(0.240) (0.161) (0.117) (0.111) (0.127) (0.162)
Intercept−2.797 ∗∗∗ −1.602∗∗∗ −0.789∗∗∗ −0.740∗∗∗ −0.040−0.024
(0.274) (0.220) (0.157) (0.147) (0.142) (0.151)
Observations 2,772 2,780 2,915 2,966 2,934 2,882
Log Likelihood−1,163.361−1,274.134−2,813.474−3,215.689−3,002.450−2,487.669
Akaike Inf. Crit. 2,360.722 2,582.269 5,660.947 6,465.378 6,038.899 5,009.338
Note: ∗p<0.05; ∗∗p<0.01; ∗∗∗p<0.001
xxiii

Table A17: ATT of Online Adoption on Offline Price Elasticity (CS Estimator) - Propensity Score Matching based on each adoption
cohort’s time of adoption
Dependent Variable: Offline Price Elasticity
Dry Dog Food Dog Hygiene Cat Hygiene
Model: (1) (2) (3)
CS -0.2473 ∗∗ -1.788∗∗∗ -0.7409∗∗∗
(0.0945) (0.3678) (0.1794)
Observations 58,580 50,913 29,039
Bootstrapped standard-errors in parentheses via 500 replications
Signif. Codes: ***: 0.001, **: 0.01, *: 0.05
Table A18: ATT of Online Adoption on Offline Price Elasticity (CS Estimator) - IPW
Dependent Variable: Offline Price Elasticity
Dry Dog Food Dog Hygiene Cat Hygiene
Model: (1) (2) (3)
CS -0.2479 ∗∗ -1.7903∗∗∗ -0.7399∗∗∗
(0.0945) (0.3678) (0.1793)
Observations 136,411 78,253 55,410
Bootstrapped standard-errors in parentheses via 500 replications
Signif. Codes: ***: 0.001, **: 0.01, *: 0.05
xxiv

E.5 ATT Estimates - Using Not-Yet-Treated Adopters as Control Groups
Table A19 presents ATT estimates using Not-Yet-Treated adopters as the control group, as discussed in
§8.2.3.
Table A19: ATT of Online Adoption on Offline Price Elasticity (CS Estimator) - Only Use Not-Yet-Treated Adopters as Comparison
Units
Dependent Variable: Offline Price Elasticity
Dry Dog Food Dog Hygiene Cat Hygiene
Model: (1) (2) (3)
CS -0.1685 ∗ -1.1729∗∗∗ -0.5222∗∗∗
(0.0814) (0.3006) (0.1533)
Observations 29,416 28,375 15,081
Bootstrapped standard-errors in parentheses via 500 replications
Signif. Codes: ***: 0.001, **: 0.01, *: 0.05
E.6 Detailed Results for Alternative Definition of Purchase Occasions
Table A20 presents the estimates of the main demand model based on an alternative definition of the purchase
occasion (i.e., customer-month level during which we observe any interaction with the retailer, either offline
or online interaction). The standard errors for the demand parameters are based on the customer-level block
bootstrap with 500 replications.
Table A20: Coefficients of Demand Model Estimate - Alternative Definition of Purchase Occasions
Dry Dog Food Dry Cat Food Dog Hygiene Cat Hygiene
Variables
Price -0.3171∗∗∗
(0.0204)
-0.1637∗∗∗
(0.0185)
-1.4982∗∗∗
(0.1166)
-0.2933∗∗∗
(0.0205)
cumPercOnlineSpend -1.1362∗∗
(0.365)
-2.8399∗
(1.118)
4.822∗∗
(1.6143)
0.8407
(0.9654)
Price * cumPercOnlineSpend -0.1354∗∗∗
(0.0333)
0.0413
(0.0926)
-2.8394∗∗∗
(0.7037)
-0.1615∗
(0.0652)
BuyPrevOcca 0.173∗∗∗
(0.0263)
-0.4511∗∗∗
(0.0437)
-0.1633∗∗∗
(0.0275)
0.3556∗∗∗
(0.0295)
CF Price 0.0421 (0.0257) 0.0596∗ (0.0247) 0.4807∗∗ (0.1714) 0.3616∗∗∗ (0.0272)
CF Price cumPercOnlineSpend -0.01 (0.0623) -0.1603 (0.1016) 2.372∗∗ (0.881) 0.1731 (0.0889)
Customer Brand FE Yes Yes Yes Yes
Observations 144,094 48,737 84,689 57,344
Log-likelihood -88735.39 -32496.48 -58287.349 -38561.677
Bootstrapped standard-errors in parentheses via 500 replications
Signif. Codes: ***: 0.001, **: 0.01, *: 0.05
Table A21 presents the ATT estimates of offline price elasticity from CS Estimator under this alternative
definition of purchase occasions and customer-month panel. The standard errors for the ATT estimates and
xxv

the demand model parameters are based on the customer-level block bootstrap with 500 replications; See
Figure A8.
Table A21: ATT of Online Adoption on Offline Price Elasticity (CS Estimator) – Alternative Definition of Purchase Occasions
Dependent Variable: Offline Price Elasticity
Dry Dog Food Dog Hygiene Cat Hygiene
Model: (1) (2) (3)
ATT -0.4104 ∗∗∗ -1.5819∗∗∗ -0.6315∗∗∗
(0.0867) (0.3688) (0.1799)
Observations 144,094 84,689 57,344
Bootstrapped standard-errors in parentheses via 500 replications
Signif. Codes: ***: 0.001, **: 0.01, *: 0.05
Figure A8: Bootstrapped distribution of Overall ATT Estimates based on 500 replications with the point estimate from Table A21.
(a) Dry Dog Food
 (b) Dog Hygiene
 (c) Cat Hygiene
E.7 Detailed Results for Alternative Demand Equation with Control Function for Price Term Only
In this section, we follow Ebbes et al. (2016) to implement the control function method by running Equation
(4) and adding the control function term only for price. We show that our main findings are consistent when
only adding the control function terms for price. Table A22 presents the estimates of the main demand model
with control function for price term only. The standard errors for the demand parameters are based on the
customer-level block bootstrap with 500 replications.
Table A23 presents the ATT estimates of offline price elasticity when we estimate the demand model in
Equation (7) with a control function term for price only. The standard errors for the ATT estimates and the
demand model parameters are based on the customer-level block bootstrap with 500 replications; See Figure
A9.
xxvi

Table A22: Coefficient Estimates - Demand Model with Single Control Function Term for Price
Dry Dog Food Dry Cat Food Dog Hygiene Cat Hygiene
Variables
Price -0.3165∗∗∗
(0.0212)
-0.1588∗∗∗
(0.018)
-1.3137∗∗∗
(0.1163)
-0.2401∗∗∗
(0.0197)
cumPercOnlineSpend -0.3837 (0.4008) -1.1528 (1.1453) 3.7018∗∗ (1.1297) 2.4235∗ (0.9528)
Price * cumPercOnlineSpend -0.1076∗∗
(0.0374)
-0.0017
(0.0974)
-1.9529∗∗∗
(0.4989)
-0.2061∗∗
(0.0638)
BuyPrevOcca 0.151∗∗∗
(0.0272)
-0.5032∗∗∗
(0.045)
-0.1805∗∗∗
(0.0283)
0.326∗∗∗
(0.0294)
CF Price 0.0524 (0.0268) 0.0432 (0.0247) 0.3133 (0.1697) 0.3093∗∗∗ (0.0257)
Customer Brand FE Yes Yes Yes Yes
Observations 136,411 45,443 78,253 55,410
Log-likelihood -84211.483 -30698.359 -55455.669 -37337.88
Bootstrapped standard-errors in parentheses via 500 replications
Signif. Codes: ***: 0.001, **: 0.01, *: 0.05
Table A23: ATT of Online Adoption on Offline Price Elasticity (CS Estimator) – Including Single CF Term for Price Endogeneity
Dependent Variable: Offline Price Elasticity
Dry Dog Food Dog Hygiene Cat Hygiene
Model: (1) (2) (3)
ATT -0.2394 ∗∗ -0.867∗∗∗ -0.5584∗∗∗
(0.0807) (0.2119) (0.1566)
Observations 136,411 78,253 55,410
Bootstrapped standard-errors in parentheses via 500 replications
Signif. Codes: ***: 0.001, **: 0.01, *: 0.05
Figure A9: Bootstrapped distribution of Overall ATT Estimates based on 500 replications with the point estimate from Table A23.
(a) Dry Dog Food
 (b) Dog Hygiene
 (c) Cat Hygiene
References
Allenby, G. M. and Rossi, P. E. (1998). Marketing models of consumer heterogeneity.Journal of econometrics,
89(1-2):57–78.
xxvii

Brazil Institute of Geography and Statistics (IBGE) (2024). Brazil’s extended national consumer index (ipca). Accessed:
October 1, 2024.
Callaway, B. and Sant’Anna, P. H. (2021). Difference-in-differences with multiple time periods.Journal of econometrics,
225(2):200–230.
Chintagunta, P., Dub´e, J.-P., and Goh, K. Y . (2005). Beyond the endogeneity bias: The effect of unmeasured brand
characteristics on household-level brand choice models.Management Science, 51(5):832–849.
Dub´e, J.-P., Hitsch, G. J., and Rossi, P. E. (2010). State dependence and alternative explanations for consumer inertia.
The RAND Journal of Economics, 41(3):417–445.
Ebbes, P., Papies, D., and van Heerde, H. J. (2016). Dealing with endogeneity: A nontechnical guide for marketing
researchers. InHandbook of market research, pages 1–37. Springer.
Gordon, B. R., Goldfarb, A., and Li, Y . (2013). Does price elasticity vary with economic growth? a cross-category
analysis.Journal of Marketing Research, 50(1):4–23.
Hitsch, G. J., Hortacsu, A., and Lin, X. (2021). Prices and promotions in us retail markets.Quantitative Marketing and
Economics, 19(3):289–368.
Kim, J., Allenby, G. M., and Rossi, P. E. (2002). Modeling consumer demand for variety.Marketing Science,
21(3):229–250.
Stuart, E. A., King, G., Imai, K., and Ho, D. (2011). Matchit: nonparametric preprocessing for parametric causal
inference.Journal of statistical software.
xxviii
