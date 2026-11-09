---
title: Data-driven budget allocation of retail media by ad product, funnel metric, and brand size
url: https://doi.org/10.1057/s41270-024-00294-2
category: cx-retail
subcategory: case-study
date: 2024-03
venue: Journal of Marketing Analytics
authors:
- Vivian Qin
- Koen Pauwels
- Bo Zhou
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1057/s41270-024-00294-2.pdf
pages: 15
chars: 67467
fetched_at: '2026-11-08T17:09:31+00:00'
kb_version: 1
---

# Data-driven budget allocation of retail media by ad product, funnel metric, and brand size

Vol.:(0123456789)
Journal of Marketing Analytics (2024) 12:235–249
https://doi.org/10.1057/s41270-024-00294-2
ORIGINAL ARTICLE
Data‑driven budget allocation of retail media by ad product, funnel
metric, and brand size
Vivian Qin1 · Koen Pauwels1  · Bobby Zhou1
Revised: 25 October 2023 / Accepted: 18 January 2024 / Published online: 1 March 2024
© The Author(s) 2024
Abstract
Sellers on online marketplaces such as Amazon.com use a variety of retail and retail media advertising services to improve
their brand performance, including awareness, consideration, and revenue. But how can they measure their progress and drive
these metrics? For 122,000 brands, we measure Amazon shoppers’ brand awareness, consideration, and purchases and test
how they change with ad and retail actions. Furthermore, we compare these brands’ past media mix with the recommended
allocation based on the model’s coefficients. We find that new product launches and upper-funnel retail media advertising
are particularly effective for small brands. Medium-sized and large brands benefit most from lower-funnel advertising. For
the funnel stages, all three metrics benefit from the number of new reviews, % discount, negative keywords, and geo-reach
campaigns. These results are robust across different product categories, but we find notable differences in how upper- and
middle-funnel ad products succeed in driving sales.
Keywords Retail media · Budget allocation · Brand awareness · Brand consideration · Brand revenue · Digital advertising ·
Online retail · Brand building
Introduction
Global e-commerce is estimated to increase from $3.3 tril-
lion in 2022 to $5.4 trillion in 2026 (Giuditta 2022). As the
pillars of online retail, online marketplaces continue to play
an essential role in facilitating transactions by connecting
sellers and consumers. For example, Amazon1 offers sellers
many options to grow their brands, covering the 4Ps of mar-
keting: product launch, price (selling prices and discounts),
place (search rank position), and promotion (ad impressions,
audience segments, and campaign goals). Such promotion
is widely known as “retail media,” which currently repre-
sents $125.7 billion of advertising spend and is expected to
overtake TV advertising by 2028 (Davey 2023). At the same
time, online marketplaces offer a rich portfolio of targeting,
including location-based reach and negative keywords that
filter out irrelevant searches. While negative keywords are
widely discussed in practice (a Google search reveals 536
million results on October 24, 2023), published scientific
results are lacking. To sellers, these prolific new ad formats
and retail options are both intriguing and often overwhelm-
ing (Masters 2022). Against this background, our research
question is: which advertising and retail factors matter most
for brand growth to sellers on Amazon?
This question remains unanswered in the existing litera-
ture for several reasons. The first lies in the unique context
of the online marketplace, in which insights from traditional
offline settings may not apply. Sellers on online marketplaces
have access to many more types of advertising in addition
to their ability to directly set retail prices. By contrast, in
offline retail stores, retailers choose the prices, and in-store
ad options are limited. Thus, while marketing literature on
budget allocation among mass media advertising is rich,
it shows a large gap for online retail media. The second
 * Koen Pauwels
 koen.h.pauwels@gmail.com
 Vivian Qin
 qnyue@amazon.com
 Bobby Zhou
 bobzhou@amazon.com
1 Data Science, Ads Insights, Amazon Ads, 450 W 33rd St,
New York, NY 10001, USA
1 In July 2022, Amazon.com, the most popular online marketplace in
the United States, generated 5.3 billion monthly visits; eBay, the sec-
ond most visited shopping site, had 3 billion visits. In addition, both
Amazon and eBay were the world’s top online retailers in terms of
mobile web traffic (https:// www. stati sta. com/ stati stics/ 11552 46/ leadi
ng- online- marke tplac es- usa- avera ge- month ly- visits/).

236 V. Qin et al.
challenge is data availability, as collecting data on both
advertising and brand performance and tracking them over
time are difficult. This gap is especially pronounced for new
ad forms, such as retail media; for new targeting options,
such as negative keywords; and in the context of the full 4Ps
of retail media. Finally, advertisers differ in important ways,
such as existing brand sizes and advertiser goals across pur-
chase funnels. We follow the empirics-first approach (Golder
et al. 2022), in which analysis of an abundance of potential
ad and retail drivers yields empirical results, which form
the basis of potential explanations and offer suggestions for
theory development.
In this research, we examine the impact of advertising
and retail drivers on brand performance in the context of
Amazon’s online marketplace. We leverage a unique data-
set from the Amazon Brand Index (ABI), which measures
brand-level awareness, consideration, and revenue, based
on shopper behaviors. We also collect ad and retail factors
as potential drivers for brand growth metrics. Specifically,
we analyze weekly data in the period between January 1,
2021, and May 16, 2022, which includes more than 122,000
US brand/product category combinations among the largest
categories within verticals of hardlines, softlines, and con-
sumables (consumer packaged goods). We use a fixed-effects
panel model, which controls for the potential endogeneity
problem to explain weekly changes in the three ABIs: brand
awareness, brand consideration, and brand revenue. From
the results, we calculate the optimal budget allocation across
ad products based on funnel metric and brand size.
Our contributions are fourfold. First, we find that growth
in all three brand metrics was driven by advertising impres-
sions from Sponsored Brands (SBs), Sponsored Brands
video (SBv), Sponsored Display (SD), and Sponsored Prod-
ucts (SPs), suggesting robust performances of Amazon spon-
sored ads on all brand metrics. For campaign strategies, the
total number of ads and ads with negative keywords or geo
reach significantly improved all three metrics. Negative key-
words allow marketers to prevent a shopper’s search query
from triggering an ad impression when it is not desired, by
a specific list of suppression terms. For example, a seller of
adult diapers may specify “babies” as a negative keyword
to avoid serving ads to consumers looking for diapers for
babies. In terms of retail factors, both the count of newly
available reviews in that week and the percentage of discount
had significant impacts on ABI. In addition, all three brand-
building metrics displayed significantly positive changes on
Prime Day and during the Thanksgiving week.
Second, we identified key performance indicator– (KPI-)
specific drivers. For example, while Fire TV and Owned &
Operated (O&O) Display impressions increased both aware-
ness and revenue, they did not show a significant impact on
consideration. Remarketing, lifestyle/in-market segments,
and ads optimized for purchase significantly improved
awareness. Furthermore, ads optimized for click-through
rate (CTR) significantly improved consideration. Drawing
on the performance from each ad format, known at Amazon
as “ad products,” we also calculated the optimal media mix
to contrast with the current mix, recommending an increase
in budget for Fire TV, O&O Display, SBs, and SBv to grow
brand revenue.
Third, we find notable differences in advertising driv -
ers for brand awareness based on brand sizes. Upper-fun-
nel advertising products (e.g., Streaming TV [STV]) were
especially effective for small brands, though those brands
have yet to fully take advantage of these opportunities. For
medium-sized and large brands, both SBs and SBv signifi-
cantly improved brand awareness. We find little differentia-
tion across brand sizes in brand consideration and revenue
drivers.
Fourth, we also find differences among top advertising
products as ABI drivers across product categories. Upper-
funnel products (i.e., Fire TV, STV) had a significant impact
in Clothing, Shoes & Jewelry; Grocery & Gourmet Food;
Sports & Outdoors; Electronics; Toys & Games; and Pet
Supplies. Middle-funnel products (i.e., O&O and Demand-
Side Platform [DSP] Displays) had significant impacts in
Grocery & Gourmet Food, Tools & Home Improvement, and
Health & Household. By contrast, sponsored ads showed a
significant impact on brand revenues in all product catego-
ries, with SBs and SBv having the largest effect sizes.
Taken together, these results indicate that both retail and
advertising actions help grow brands, and they have differ -
ential impacts depending on brand sizes and success metrics.
As a result, to improve their brand performance, sellers need
to choose their priority actions according to which brand
metrics they want to improve, as well as their current brand
sizes and the product categories in which they operate.
The remainder of this paper is organized as follows: we
first review the related literature streams and integrate them
into our conceptual framework. Then, we specify data and
measurement. After detailing our method, we estimate it
and report on the results. Finally, we leverage the empiri -
cal results to calculate the optimal budget allocation across
ad products, for different brand sizes and advertising goals.
Literature review
This study investigates how different advertising and retail
drivers improve brand awareness, consideration, and rev -
enue. Therefore, we contribute to the literature streams on
brand attitude metrics, e-commerce, the impact of adver -
tising, and how it differs across ad products, brands, and
categories.
Prior research shows that consumer attitudes toward a
brand influence the association between advertising and

237Data-driven budget allocation of retail media by ad product, funnel metric, and brand size
brand outcomes (Chaudhuri 2002), highlighting the impor-
tance of consumer perceptions in determining ad effective-
ness (Buil et al. 2013). In their theory of buying behavior,
Howard and Sheth (1969, p. 14) note, “Attitude is an input
into executive decisions because many marketing decisions,
including advertising, can be more adequately evaluated or
measured in terms of attitude than of purchase behavior.”
However, this perspective has been challenged by psychol-
ogy literature (e.g., Ajzen and Fishbein 1977). Consistent
with this literature, Pauwels and van Ewijk’s ( 2020 recent
marketing study confirmed the low correlations between
general attitudes and behavior, unless the measurement
context maps onto the behavior in a very specific way. We
propose that retail media offers such specific mapping,
because retail site visitors leave specific behavioral clues
as to their attitudes toward the brands and products they are
browsing, searching, and examining. Indeed, behavior can
be viewed as an action (e.g., a purchase) directed at a target
(e.g., a brand), performed in a given context , at a certain
point in time (Ajzen and Fishbein 1977). The principle of
compatibility requires that measures of attitude and behavior
involve the same action, target, context, and time elements,
as Krauss (1995) shows across eight studies.
In marketing, researchers have assessed important con-
cepts such as brand awareness and consideration with pur -
chase (Vakratsas and Ambler 1999). Market response mod-
els have shown that such metrics predict sales above and
beyond long-term marketing effects (Hanssens et al. 2014;
Kumar et al. 2019; Petersen et al. 2018; Srinivasan et al.
2010). These studies note, however, that continuously track-
ing high-quality funnel metrics with surveys is costly, as
they require representative sampling and survey procedures
for hundreds and often thousands of consumers. Therefore,
they call for further research on the explanatory power of
online behavior metrics, which are inexpensive to collect
and unobtrusive to prospective customers (Lecinski 2011).
As such, these metrics are less, or even not, sensitive to the
well-documented survey issues of memory, mere measure-
ment, and social desirability biases (Morwitz et al. 1993;
Simmons et al. 1993; Tourangeau et al. 2000).
For e-commerce, the internet has generated many new
metrics recommended to managers when evaluating market-
ing effectiveness and assessing how consumers think, feel,
and act regarding their brand (Colicev et al. 2018; Yadav
and Pavlou 2014). Generic and branded search, website page
views, and reviews are key examples of consumers’ brand-
related actions. Several empirical articles have shown that
such online behavior metrics convert to sales and are respon-
sive to marketing actions (Colicev et al. 2018; De Vries et al.
2017; Srinivasan et al. 2016), but this is typically done for a
single or a small number of brands. By contrast, large-scale
studies focus on a particular (retail media) ad product, such
as Sponsored Video, and do not investigate brand building
(Pauwels et al. 2023). In this study, we leverage weekly data,
for more than 122,000 brands and product category combi-
nations, from the ABI, which automatically and regularly
measures Amazon shoppers’ brand awareness, considera-
tion, and purchases. This dataset allows us to uncover more
generalized insights across a large number of brands with
different characteristics.
Regarding advertising’s impact, different ads likely have
different impacts on specific brand metrics (Batra and Keller
2016). Depending on the context, advertising could influ-
ence some but not all brand metrics. Buil et al. (2013) find
that advertising spend improves brand awareness but not per-
ceived quality. In addition, De Haan et al. (2016) show that
content-separated advertising (e.g., remarketing) is effec-
tive in driving traffic to an online retailer but that content-
integrated advertising (e.g., ads for products directly relevant
to a search query) is more likely to convert to purchase.
Research on newer advertising tactics, such as negative key-
words, focuses on how to select them (Peltonen et al. 2017;
Tavşanoğlu 2018) instead of their impact on outcomes such
as brand metrics and sales. Finally, advertising effective -
ness research has examined budget allocation from different
angles, including short- versus long-term ad effectiveness
(Vakratsas and Ma 2005), different types of online advertis-
ing (Breuer et al. 2011), and search platforms (Zia and Rao
2019). A key finding is that the effects of both advertising
and retail factors, such as product assortment, price, review
volume, and valence, likely depend on the product category
and the brand size (Colicev et al. 2018; Pauwels et al. 2016;
You et al. 2015). Consistent with this line of literature, our
research incorporates various ad and retail factors to evaluate
their impact across brands of different sizes and in different
categories.
Conceptual development
While the literature review guides our analysis, we do not
derive hypotheses from a unified theory. Instead, we address
our research question in an empirics-first approach, defined
by Golder et al. (2022) as research that “(1) is grounded in
(originates from) a real-world marketing phenomenon, prob-
lem, or observation; (2) involves obtaining and analyzing
data over multiple categories; and (3) produces valid market-
ing-relevant insights without necessarily developing or test-
ing a theory” (p. 319). To guide these insights, we provide
a conceptual framework on the dimensions by which digital
advertising effectiveness may differ and explore how these
dimensions translate into metrics in our empirical setting.
First, the purchase funnel (Srinivasan et al. 2010) is a key
concept in marketing literature. Before deciding on a brand,
consumers first become aware of the brand and then con-
sider it for purchase. In the awareness stage, consumers may

238 V. Qin et al.
notice the brand and search for it. However, they may not yet
have a clear idea of what the brand stands for or whether its
products are serious contenders for the purchase decision.
In the consideration stage, consumers research and become
informed about the brand and product specifics. This infor -
mation enables the evaluation and subsequent purchase
decision. Therefore, the number of consumers considering a
brand should predict brand sales, and the number of consum-
ers aware of the brand should predict brand consideration.
Second, research has long treated brand familiarity as
a driver of consumer response to marketing (Aaker et al.
2013). Consumers perceive less risk in a familiar brand and
are more likely to pay attention to its call-to-action (lower-
funnel) marketing. For example, price promotions by famil-
iar brands such as Coca-Cola generate a much stronger
response than the same discount for unfamiliar brands
(Lichtenstein et al. 1991; Mela et al. 1997). As a result, less
familiar brands typically try to build awareness and consid-
eration through upper-funnel and middle-funnel advertising,
respectively. Outside marketing communication, product
innovation, and price discounts also help bring an unfamil-
iar brand to the attention of potential customers (Slotegraaf
and Pauwels 2008).
Third, word of mouth is a key post-purchase metric with
substantial power to influence potential customers’ aware-
ness, consideration, and purchases (Trusov et al. 2009). In
e-commerce, reviews are easy to access and search. Prior
research has demonstrated separate effects of review (star)
ratings and the number of reviews (You et al. 2015). The for-
mer indicates the product quality and the latter its popularity
and the confidence a potential customer has in the review
rating (You et al. 2015). On Amazon, a minimum of 3.5 stars
and 15 reviews signal that product quality and popularity are
sufficient to start advertising (Ibarra 2020).
Fourth, we consider both the number of ad impressions
and the number of ad campaigns. For the former, a larger
number of impressions increases the likelihood that consum-
ers are exposed to the brand’s message and thus become
aware of its offering (Keller and Lehmann 2006; Tellis
2003). For the latter, different campaigns provide variety
in ad messaging and execution, which can help maintain
consumers’ interest in the brand, especially if it is familiar to
them (Pauwels et al. 2022). We include ad impressions and
the number of campaigns by ad format, as their impact may
differ across upper-, middle-, and lower-funnel advertising.
Finally, digital advertisers have many new options in
both ad formats and metrics. For the former, ad relevance
to the reached audience can be enhanced through the use
of negative keywords (e.g., “babies” when offering diapers
for adult incontinence) and by lifestyle, being “in-market,”
and geographic (geo-) location. Moreover, audiences that
browsed the category previously can be retargeted (e.g., De
Haan et al. 2016), labeled as “remarketing” on Amazon.
Campaigns can be optimized for CTR or for purchase con-
version. For metrics, Amazon offers a 0/1 coded “ad readi-
ness score” (previously called “retail readiness”), which
simplifies the click probability of a product in the absence
of ads. A score of 1 indicates that the product detail pages
include all the information necessary for consumers to
make informed purchase decisions, including “informative,
[search engine optimization–] rich titles, bullets, and prod-
uct descriptions, clear imagery, engaging videos, customer
ratings and reviews, and ample inventory” (Ibarra 2020).
Because research has shown that advertising works well for
high-quality products (Erdem and Swait 2004; Golder and
Tellis 1997), an ad readiness score of 1 signals to sellers that
their products are worthy of advertising.
Data and measurement
Data and sample selection
To ensure the generalizability of our results, we begin with
more than 30 product categories across three consumer ver-
ticals (hardlines, softlines, and consumables) on Amazon.
Of the product categories included in the ABI, we retain the
top 12 categories based on the number of Amazon Standard
Identification Numbers (ASINs).2 Specifically, we select the
following product categories: Home & Kitchen; Clothing,
Shoes & Jewelry; Grocery & Gourmet Food; Electronics;
Arts, Crafts & Sewing; Sports & Outdoors; Tools & Home
Improvement; Health & Household; Beauty & Personal
Care; Toys & Games; Patio, Lawn & Garden; and Pet Sup-
plies. These categories differ on many dimensions, includ-
ing their utilitarian (e.g., Tools & Home Improvement) and
hedonic (e.g., Toys & Games) nature (Li et al. 2020). As
ABI is updated on a weekly basis for each brand, we merge
brand-level retail and advertising data with ABI from Janu-
ary 1, 2021, to May 16, 2022. Because retail and advertising
data are both at the ASIN/daily level, we aggregate them
to the brand/product category weekly level to be consistent
with the ABI cadence. Specific aggregation depends on the
metrics. For example, for the percentage of discount of retail
price, we take the average of all ASINs within a brand to be
the brand-level proxy, and for advertising spend, we sum up
all ASIN spend at the brand level (see Table 1). Because we
are mostly interested in the drivers that explain the move-
ment in ABI, we only keep brand/product categories with
at least 28 weeks of our variables, dropping less than 10%
of the data. This time frame ensures sufficient variability
in the data to uncover the significant impact of advertising
2 This is equivalent to the stock-keeping unit (SKU) in a traditional
retail setting.

239Data-driven budget allocation of retail media by ad product, funnel metric, and brand size
and retail drivers. To measure ad investment, we use the
number of impressions instead of dollar spend, because the
former has fewer missing values and is less subject to inac-
curacies (e.g., currency conversion, negotiation). The final
sample contains more than 122,000 brand/product category
combinations with over 6.4 million observations in total at
the weekly level.
ABI calculation and brand size categorization
In our sample, key dependent variables such as awareness,
consideration, and revenue are ABIs at the brand/prod-
uct category level updated weekly. ABIs, computed using
Amazon first-party data, are predictive of the downstream
impact not only on Amazon but also on surveys measuring
customer perceptions (Pauwels and van Ewijk 2020). To
meet the leading performance indicator criteria in Hanssens
et al. (2014), we optimally selected and weighed the brand
awareness metrics to predict brand consideration, and the
brand consideration metrics to predict sales. The Awareness
Index metrics include consumer actions revealing that they
both are aware of the brand (e.g., branded search) and have
been exposed to the brand (non-ad retail impressions). The
Consideration Index metrics include the number of detail
page views and dwell time (time spent on the detail page).
Both metrics indicate that the consumer is actively evaluat-
ing products for purchase (Li et al. 2020). Furthermore, we
categorize brands by sizes using the Consideration Index
because it has the highest correlation with both awareness
and revenue (r ≥ 0.72). Specifically, we categorize brands as
small, medium-sized, and large if they belong to the bottom
33%, middle 33%, or top 33% in the Consideration Index,
respectively.
Analysis and results
Table  2 overviews the analysis steps with the addressed
question and result for each step.
Table 1  Key variables and their explanation
Underlying variables (aggregation) Operationalization and explanation
New products launched (sum) The number of new ASINs launched in the last month
% discount Average % discount across all ASINs of a brand
Overall visible review ratings (average) Overall ratings displayed
New ratings in each week (average) New ratings added that could reflect shopper momentum at a given time
Search rank (average) Page number on which ASINs of the brand are shown
Ad readiness score (average) Binary coded showing the click probability of a product in the absence of ads
SP readiness score (average) Binary coded showing the click probability when using SPs
Ad impressions by types (sum) Fire tablet, Kindle, video, Fire TV, O&O Display, DSP Display, audio, STV, IMDb, and sponsored ads
(including SBs, SBv, SD, and SPs)
Number of campaigns by types (sum) Remarketing, lifestyle/in-market, contextual, negative keywords, geo reach, CTR optimization, and
conversion optimization
Amazon Brand Awareness Index Number of consumers likely aware of the brand, calculated as a weighted index of searches and non-ad
retail impressions
Amazon Brand Consideration Index Number of consumers likely considering the brand, calculated as a weighted index of detail page views
and dwell time
Amazon brand revenues Brand sales revenue on Amazon.com
Table 2  Analysis steps
Analysis step Question addressed Result
Ordinary least squares Are the residuals heteroskedastic? Need for panel model
Augmented Dickey–Fuller test Are variables mean stationary (have a fixed mean) or
evolving?
Amazon Brand Metrics evolve, so take difference
Hausman test Random- or fixed-effects model? Fixed effects
Elasticity What is the % impact for a 1% change in the driver
variable?
SBv drives all three ad goals, Fire TV, O&O Display,
and SBs drive brand revenue only
Ratio of elasticities What is the optimal allocation across ad products for
smaller and for larger brands?
Smaller brands should allocate more to STV and SD,
larger brands to SBv

240 V. Qin et al.
Model selection
First, we run ordinary least squares regressions of the change
in brand metrics on ad and retail drivers. The residual plots
clearly show their correlation with the predicted ABI values
(i.e., the significant presence of heteroskedasticity). Thus,
we establish the need for a panel model that accounts for
within-brand variations. Second, we conduct the augmented
Dickey–Fuller test because stationarity is a requirement for
longitudinal data modeling. Using Python’s Statsmodel
package for 30 randomly selected brand/product categories,
we find that 30% were evolving. As a result, we take the
first-order difference of ABI (i.e., changes in ABI as values
of the current period minus those of the previous period)
and use that as the dependent variables for all brands. The
augmented Dickey–Fuller tests further revealed that all
first-order differences are stationary, suggesting no need
for second-order differencing. Third, we use the Hausman
test to select between the random- and fixed-effects models.
Given that all the tests reject the null hypothesis that the
random-effects estimator is consistent (i.e., assuming errors
are not correlated with the regressors, and thus there is no
endogeneity problem), we report only the results with the
fixed-effects estimators. However, we also test the random-
effects model as a robustness check and find quantitatively
similar results.
The resulting fixed-effects model specification is
where Δ(ABI)j i,t is the difference of j th ABI feature for brand
i between week t − 1 and week t , where j =1 , 2,3  for the
three ABI features (awareness, consideration, and revenue);
Adi,t is the advertising spending of brand i in week t , includ-
ing all Amazon Ads such as SBs, SBv, and DSP Display
(see Table  1 for ad types); NPDi,t are the number of new
products launched one month before week t by brand i ;
Ratingi,t are the overall visible and newly added ratings for
brand i in week t , respectively; Searchranki,t is the average
page number of search results across all SKUs by brand i
in week t ; Campaigni,t is the number of campaigns of brand
i in week t (see Table  1 for types); Readinessi,t is the click
probability across all SKUs for a brand with or without any
ad; PDt, Thanksgivingt are indicator functions for the weeks
of Prime Day and Thanksgiving; and 𝛼i is the brand-level
fixed effect for brand i . We estimate this model with the
Linearmodels Python package.
Δ(ABI)j i,t = 𝛽0 + 𝛽1Adi,t + 𝛽2NPDi,t + 𝛽3Ratingsi,t
+ 𝛽4SearchRanki,t + 𝛽4Campaigni,t
+ 𝛽6Readinessi,t + 𝛽7PDt + 𝛽8Thanksgivingt
+ 𝛼i + 𝜖i,t, fort = 1, … , 28, j =1 , 2, 3,
Media mix calculation
Ever since Dorfman and Steiner (1954) derived the optimal
marketing allocation, marketing literature has validated the
profit-maximizing allocation spend on ad products on the
basis of their sales elasticities, that is, the percentage of sales
increase from a 1% increase in the ad investment. This for -
mula is the basis for the generalizable findings in research
(e.g., Hanssens 2015). In a first step, we estimate the pre-
ferred model (fixed effects in our case) to extract statistically
significant coefficients of ad products’ impressions. Second,
together with the descriptive statistics on impression levels,
we calculate the elasticity of each KPI to each ad spend.
Third, we derive the optimal budget allocation from the
magnitude of elasticities to contrast with the current alloca-
tion on average across all applicable brands to make media
mix recommendations (for a similar procedure, see De Haan
et al. 2016). The exact steps are as follows:
1. Calculate KPI’s elasticity by ad product: elastic-
ity = coefficient estimated from the model × average (ad
impressions)/average (KPI). For example, suppose that
the estimated regression coefficient is 1 (i.e., each ad
impression increases awareness by 1). If the average
ad impressions are 10 and average awareness is 100,
the elasticity is 0.1. In other words, a 1% increase in ad
impressions increases awareness by 0.1%.
2. Sum up elasticities from the first step and divide each
by the total, to generate the recommended percentage of
allocation of impression by ad product.
3. Contrast the second step with the current allocation as
the suggestion for that KPI.
As an example of two ad products with elasticities of
0.2 and 0.1, respectively, two-thirds of the budget should be
allocated to the former and one-third to the latter.
Model fit, coefficients, and media mix allocation
for all brands
Overall model fit
Fixed-effects models explain ABIs reasonably well, with
F-statistics (including F-stats with robust standard errors)
with p ≤ 0.01 for all KPIs. The explanatory power is high-
est for Clothing, Shoes & Jewelry and lowest for Grocery
& Gourmet Food (with a two-times difference), suggesting
product category differences. The average explanatory power
of the variance between panel units is 0.12 for brand aware-
ness, 0.11 for brand consideration, and 0.07 for brand rev -
enue. These R-squares are significant and substantial and, at
the same time, show that most metrics are explained by fac-
tors other than Amazon Ads during the studied period. Such

241Data-driven budget allocation of retail media by ad product, funnel metric, and brand size
factors may include product quality, competitive actions,
and the reputational impact of brand marketing before the
period. Across the brand metrics, the explanatory power is
highest for changes in awareness, followed by consideration
and then revenue, consistent with prior research that finds
that advertising is a more powerful driver of upper- than
lower-funnel metrics (Pauwels et al. 2013; Srinivasan et al.
2010).
Model coefficients
We report the fixed-effects model coefficients for the retail
and ad campaign actions in Table 3. First, we note that fun-
nel drivers in the general marketing literature also apply
at Amazon. Launching new products is crucial to increase
brand awareness, and price discounts work for all KPIs, as
do new reviews, indicating the importance of word of mouth
(Rojas-Lamorena et al. 2022; Srinivasan et al. 2010; You
et al. 2015). Moreover, brands appearing high in the search
rank garner greater brand awareness, which translates into
more consideration and revenue (Bertozzi et al. 2022; Rutz
and Bucklin 2011). New results appear for the campaign
variables. While the number of remarketing and lifestyle/
in-market campaigns raise brand awareness, we find no
significant increase in brand revenue. By contrast, the use
of negative keywords and geolocation campaigns is asso-
ciated with higher performance on all three KPIs. While
campaigns optimized for CTR significantly increase brand
consideration, those optimized for purchase mainly increase
awareness. Across the board, we observe that digital market-
ing, which once was relegated to lower-funnel activation, is
effective at increasing brand awareness and consideration,
consistent with the conceptual arguments of Batra and Keller
(2016) and the results of Pauwels and van Ewijk (2020).
Finally, both Amazon’s Prime Day and the Thanksgiving
week (Black Friday/Cyber Monday) boost brand awareness,
consideration, and revenue, with Prime Day enjoying about
double the effect of Thanksgiving.
How should advertisers adjust their main digital market-
ing allocation? Table 4 shows the coefficients for the adver-
tising products that we can compare with current alloca-
tions, because advertisers have sufficiently spent in our data.
As the table shows, SBv is a significant driver of all three
dependent variables: brand awareness, consideration, and
revenue. By contrast, Fire TV, O&O Display, and SBs (non-
video) are significant drivers of brand revenue only.
Table 3  Fixed-effects model results: Campaigns and retail actions coefficients
Standard errors are in parenthesis and disclosed only for review purposes. Amazon Ads do not approve public disclosure
ns non-significant at the 10% confidence level
*p < 0.10, **p < 0.05, ***p < 0.001
Brand awareness Brand consideration Brand revenue
Number of new products launched last month 0.1181 (0.0694)* ns ns
% discount 1362.7 (225.05)*** 987.2 (24.629)*** 3434.9 (121.31)***
Weekly new reviews 126.7 (5.9177)*** 10.858 (0.6476)*** 71.802 (3.1898)***
Search results page number − 304.76 (14.515)*** − 6.8825 (1.5884)*** − 74.713 (7.8239)***
Number of remarketing campaigns 0.0386 (0.0062)*** ns ns
Number of lifestyle/in-market campaigns 0.0829 (0.015)*** 0.0023 (0.0013)* ns
Number of negative keyword campaigns 0.0321 (0.0051)*** 0.0056 (0.0006)*** 0.0248 (0.0028)***
Number of geo-reach campaigns 0.0168 (0.0038)*** 0.0062 (0.0004)*** 0.0303 (0.0021)***
Number of campaigns optimized for CTR ns 0.0018 (0.0004)*** ns
Number of campaigns optimized for purchase 0.0265 (0.0062)*** ns ns
The week of Prime Day 2835.3 (75.765)*** 271.38 (8.2914)*** 1096 (40.84)***
The week of Thanksgiving 1134.5 (73.801)*** 116.68 (8.0764)*** 549.4 (39.781)***
Table 4  Fixed-effects model results: Ad product coefficients for
media allocation calculation
Only coefficients used to calculate the media mix are shown.
Although other ad impressions are significant, their effects on ad mix
are too small to be included
a Average impressions and KPIs are not approved by Amazon Ads to
disclose beyond the scope of review. This column is for reviewers
only
*p < 0.10, **p < 0.05, ***p < 0.001
Dependent variable Ad product Coefficient Average
weekly
 impressionsa
Brand awareness SBv 0.0132*** 1860
Brand consideration SBv 0.0006*** 1860
Brand revenue SBv 0.0030*** 1860
Fire TV 1.7758** 5530
O&O Display 0.0386*** 119
SBs 0.0013*** 10,800

242 V. Qin et al.
With the model coefficients, we can calculate the ratio
of elasticities that summarizes our model’s recommenda-
tion on ad product allocation (De Haan et al. 2016; Dorf-
man and Steiner 1954; Wright 2009). Comparing the cur -
rent advertising spending with this model-based advice
shows managers the gap between reality and recommen -
dation. We begin with our general recommendations and
then differentiate by advertiser size because adoptions of
different ad products vary with this variable.
For the average advertiser in our data, Figs.  1, 2, and
3 compare our recommended media mix with the current
allocation. First, the current allocation of 0.9% of the
media budget to SBv is insufficient: the model suggests
it should increase to 5.9% for awareness goals, 1.8% for
consideration goals, and 2.7% for revenue goals. Second,
SBs allocation should increase from 4.99% to 6.94%.
Likewise, upper-funnel Fire TV and O&O Display should
reflect 0.01% and 0.02% of the budget, respectively, com-
ing from the dominant spending on the lower-funnel ad
product SPs. Note that the elasticities show that brands
should optimally spend more on the analyzed ad products.
Because we do not have data on other brand communica-
tion channels, we do not know their elasticities, which are
needed to advise for reallocation of funds to Amazon Ads
or increasing the overall budget. The likelihood of manag-
ers to follow such advice is partly based on their decision
authority to only reallocate an existing budget or to also
change the budget size (Hanssens and Pauwels 2016).
Coefficients for advertising mix by brand size
Next, we show the model coefficients by brand size and their
recommended versus current media mix. Table  5 provides
the coefficients, and panels A–C of Fig.  4 depict the media
mix, depending on brand sizes, using brand awareness as an
example.
Consistent with marketing theory and research findings
(e.g., Hanssens et al. 2014; Pauwels et al. 2016), small brands
have more potential to increase awareness and thus show a
higher elasticity to upper-funnel advertising actions such as
STV and SD. As a result, our model recommends that these
brands allocate 0.2% of the budget to STV and 8.6% to SD.
Moreover, middle-funnel ad product SBs should receive 9.0%
of media mix allocation, more than for any other advertiser
size. By contrast, SBs are already close to optimal for medium-
sized and large brands, which we recommend increase to 5.1%
and 7.2% of the budget, respectively. The greatest opportunity
for these brands lies in SBv, as the model recommends increas-
ing the current 0.9% allocation to 4.5% and 6.2%, respectively.
Top three advertising and retail drivers by product
category
In this section, we present the top three drivers for brand
growth for each product category focusing on brand revenue.
To enhance exposition, we summarize the results in Table 6.
Fig. 1  Increasing SBv for brand awareness
Fig. 2  Increasing SBv for brand consideration

243Data-driven budget allocation of retail media by ad product, funnel metric, and brand size
First, the most effective retail drivers and advertising
drivers differ across product categories. Upper-funnel
products (i.e., Fire TV, STV) have a significant impact on
Clothing, Shoes & Jewelry; Grocery & Gourmet Food;
Electronics; Sports & Outdoors; Toys & Games; and Pet
Supplies. Middle-funnel products (i.e., O&O and DSP
Display) have a significant impact on Grocery & Gourmet
Food, Tools & Home Improvement, and Health & House -
hold. By contrast, sponsored ads have a significant impact
on brand revenues in all studied product categories, with
SBs and SBv having the largest effect sizes.
Second, the number of new reviews is the most effec-
tive retail driver across most product categories across the
purchase funnel, expanding the finding of Li et al. (2020)
that reviews matter outside the immediate purchase con-
text. This result highlights the power of the most recent
reviews to shape consumer behavior, consistent with
previous findings across categories and countries (Kübler
et al. 2018; You et al. 2015).
Third, the total number of ads is the most effective adver-
tising driver across most product categories. A larger num-
ber of ads typically means more consumer exposure. This
result highlights the importance of the informative role of
advertising in facilitating the focal brands’ entry into con -
sumers’ consideration set. Regarding specific advertising
tactics, remarketing only shows up as a top-three driver for
Clothing, Shoes & Jewelry. Negative keyword ads are a top
driver for Electronics and Health & Household. Lifestyle/
in-market matters for Home & Kitchen; Clothing, Shoes &
Jewelry; Arts, Crafts & Sewing; and Patio, Lawn & Garden.
Ads optimized for CTR are a top-three driver for Sports &
Outdoors and Patio, Lawn & Garden. Finally, ads optimized
for purchase are a top-three driver for Pet Supplies.
Discussion
We show that digital advertising and retail drivers not only
are specific to brand funnel metrics but also differ by adver-
tiser size and product category. These results raise several
questions for marketing theory and practice. First, why are
new product launches and upper-funnel advertising products
particularly effective for brands of low- and medium-level
consideration? New product launches build brand aware-
ness (Srinivasan et al. 2009), especially for relatively small
brands, for which this funnel metric has more room to grow
(Hanssens et al. 2014). Larger brands are more likely to
be well-known and thus potentially benefit less from any
new information. Because smaller brands tend to have
fewer products, we speculate that each new addition to their
Fig. 3  Adopting Fire TV and
O&O Display, and increasing
SBs and SBv for brand revenue
Table 5  Fixed-effects model results: Ad product coefficients for brand
awareness by brand size
*p < 0.10, **p < 0.05, ***p < 0.001
Ad product Coefficient Average weekly
impressions
Brand size
STV 0.008* 21 Small
SBs 0.0027*** 3371
SD 0.0135*** 646
SBs 0.0016*** 10,066 Medium-sized
SBv 0.0076*** 1847
SBs 0.0029*** 20,984 Large
SBv 0.0162*** 3276

244 V. Qin et al.
Fig. 4  Increasing awareness. A
Small brands. B Medium-sized
brands. C Large brands
Panel A. Small brands
Panel B. Medium-sized brands
Panel C. Large brands

245Data-driven budget allocation of retail media by ad product, funnel metric, and brand size
product lines influences consumers’ perception of the focal
brand to a greater extent than larger brands. In other words,
paying more attention to new product launches by smaller
brands is in consumers’ best interest because a richer amount
of information will be revealed about the focal brand. Con-
sistent with this rationale, we also find that upper-funnel
advertising intended to increase brand recognition, such as
STV ads, improves awareness of small brands but not large
brands.
Second, why do % discount and remarketing ads increase
awareness more than consideration? The first finding high-
lights the power of discounts to attract consumer attention,
as Slotegraaf and Pauwels (2008) demonstrate in fast-mov-
ing consumer goods categories. However, discounts alone
do not suffice to keep consumers’ interest, as operational-
ized by the dwell time on the product’s detail page to obtain
information (consideration). The same holds for remarketing
ads: while they get consumers (again) in the funnel, they are
less effective in evoking consideration and purchase. As De
Haan et al. ( 2016) demonstrate for a Dutch online retailer,
the likely reason is that remarketing is content-separated
(i.e., shown on web pages, which consumers do not visit for
the purpose of the remarketed product). Instead, they find
higher revenue for consumers who come in through content-
integrated ads, referred to as “contextual advertising.”
Consistent with this contextual rationale, we observe
strong effects for campaigns using negative keywords and
geolocation. Negative keywords help advertisers avoid
audiences focused on other products and thus increase the
chances that the ad-exposed audience is interested in the
advertised product. This advertising tactic is a top-three
brand revenue driver in the Electronics and Health & House-
hold categories. Likewise, geolocation allows advertisers
to reach audiences at the right place and at the right time.
Because they are seeing ads relevant to their real-time loca-
tion, consumers are more likely to pay attention to, consider,
and ultimately purchase the advertised product.
The effectiveness of new reviews shows the importance
of this word-of-mouth metric as a demand-perspective
indicator of product quality. At the same time, ad readiness
indicates product quality from a supply side perspective.
Thus, advertisers should ensure that product detail pages
include all the necessary information for consumers, such as
search engine optimization – rich titles, bullets, and product
descriptions; clear imagery; engaging videos; customer rat-
ings and reviews; and ample inventory.
Finally, we observe similar retail drivers across catego-
ries, with the number of new reviews, % discount within
the top three drivers, and new product launches criti-
cal for Home & Kitchen; Clothing, Shoes & Jewelry, and
Table 6  Top three drivers for each product category
*p < 0.10, **p < 0.05, ***p < 0.001
Product categories Top three retail drivers Top three advertising drivers
Home & Kitchen Number of new reviews***, percentage of ASINs with
5 + reviews***, percentage of price discount***
Total # ads***, # of lifestyle/in-market ads***, # of geo
ads***
Clothing, Shoes & Jewelry Number of new reviews***, count of total visible
reviews**, new ASINs launches*
Total # ads**, # of lifestyle/in-market ads***, # of
remarketing ads**
Grocery & Gourmet Food Ratings of new reviews*, new ASINs launches***,
percentage of price discount***
Fire TV impressions***, # contextual ads***, # ads with
geo reach**
Electronics Count of new reviews***, # new ASIN launches*,
percentage of price discount***
Total # ads***, # of geo ads***, # of negative keyword
ads***
Arts, Crafts & Sewing Percentage discount*** SBv impressions***, # of lifestyle/in-market ads***, #
of geo ads***
Sports & Outdoors Count of new reviews**, ratings of total visible
reviews**, percentage of price discount***
Fire TV impressions***, total # ads*, # of ad optimized
for CTR*** or purchase***
Tools & Home Improvement Count of new reviews*, count of total visible reviews*,
percentage of price discount***
Total # ads*, # of contextual ads**, # of geo ads*
Health & Household Count of new reviews***, percentage of price dis-
count***
Total # ads**, # of negative keyword ads***, O&O
Display***
Beauty & Personal Care Count of total visible reviews*, percentage of price
discount*
Total # ads***, # of contextual ads***, # of geo ads***
Toys & Games Count of new reviews*, percentage of price dis-
count***
Total # ads**, # of contextual ads*, DSP impressions**
Patio, Lawn & Garden Count of total visible reviews*, percentage of price
discount*
# of lifestyle/in-market ads***, # of geo ads*, # of ads
optimized for CTR***
Pet Supplies NA Total # ads***, # of ads optimized for purchase**, STV
impressions**

246 V. Qin et al.
Electronics. Likewise, the number of ad campaigns matters
across categories, with SBs and SBv showing the largest
effect sizes. Beyond sponsored ads, (O&O and DSP) Display
has a significant impact in Grocery & Gourmet Food, Tools
& Home Improvement, and Health & Household. Future
research is necessary to shed light on the reasons behind this
effectiveness. One possible explanation is that these catego-
ries are rather utilitarian in nature and therefore engender
deeper information processing, often starting several weeks
before purchase (Mathwick et al. 2001; Park et al. 2018).
Consumers prefer online search because of its ease of com-
parison, which reduces brand differentiation (Noble et al.
2005), increasing the potential for Display to influence the
purchase funnel. By contrast, upper-funnel ad products (i.e.,
Fire TV, STV) have a significant impact on Clothing, Shoes
& Jewelry; Grocery & Gourmet Food; Electronics; Sports
& Outdoors; Toys & Games; and Pet Supplies. Many of
these product categories are rather hedonic in nature, which
enhances the appeal of fun, surprise, variety, and adven-
ture in consumers’ shopping journey (Arnold and Reynolds
2003; Novak et al. 2003). Li et al. (2020) find that hedonic
purchases involve more product page views of the target
retailers up to two weeks before conversion, providing a
funneling effect of final purchases.
Conclusion
In this research, we analyze the impact of different retail
and advertising actions on brand growth. Two typical chal-
lenges are the difficulty of measuring brand metrics and the
difficulty of combining advertising information and brand
performance. Focusing on the empirical context of Amazon.
com, we overcome these challenges by leveraging a unique
dataset from ABI, which automatically and regularly meas-
ures Amazon shoppers’ brand awareness and brand consid-
eration, and by combining it with different advertising and
retail drivers. Our data start on January 1, 2021, and end
on May 16, 2022, and include 122,000 US brand/product
category combinations across the largest categories within
the verticals of hardlines, softlines, and consumables. Spe-
cifically, weekly changes of brand awareness, brand con-
sideration, and brand revenue are all documented by ABI.
This comprehensive dataset allows us to confidently address
our focal research question with a fixed-effects panel model.
Our fixed-effects panel model includes both retail and
advertising variables, after controlling for the potential
endogeneity problem (i.e., regressors might be correlated
with the error terms). We find that retail and advertising
actions differentially increase brand awareness, consid -
eration, and revenue. In particular, SBv improves brand
awareness and consideration, whereas STV, SBs, and SD
are especially helpful for brand revenue. For small brands,
we suggest increased investment in STV, SBs, and SD for
awareness; STV, SBv, and SD for consideration; and SBs
and SBv for revenue. For medium-sized and large brands,
we recommend SBs and SBv for all metrics. We also recom-
mend that sellers choose their priority actions according to
which ABIs they want to improve, as well as their current
brand sizes.
We highlight three main findings and their correspond-
ing managerial recommendations. First, different advertising
products drive different brand metrics. We find that increas-
ing SBv investment is crucial for brand awareness and con-
sideration while adopting STV, together with increasing the
budget for SBs and SD, is particularly helpful for brand reve-
nue. Second, specific recommendations for advertising prod-
ucts depend on brands’ sizes. For small brands, STV, SBs,
SBv, and SD can help improve brand metrics. For medium-
sized and large brands, we recommend prioritizing increas-
ing budgets for SBs and SBv. Third, the recommendation
for advertising products depends on the product category.
Upper-funnel products (i.e., Fire TV, STV) have significant
impacts on Clothing, Shoes & Jewelry; Grocery & Gourmet
Food; Electronics; Sports & Outdoors; Toys & Games; and
Pet Supplies. Middle-funnel products (i.e., O&O and DSP
Display) have a significant impact on Grocery & Gourmet
Food, Tools & Home Improvement, and Health & House -
hold. Finally, sponsored ads have a significant impact on all
product categories’ revenues, with SBs and SBv having the
largest effect sizes.
Despite using a large dataset that combines advertising,
retail, and brand performance, our study has some limita-
tions. First, owing to data collection limitations, we analyze
only advertisers on Amazon’s marketplace. Future research
could examine our research question in different empiri-
cal contexts. Second, our research focuses on the impact of
online ads and retail actions on brand performance online.
Future research could assess the impact of advertising and
retail drivers on both online and offline brand performance.
Third, we include the effect of the 4Ps, such as new product
introductions, but do not study whether larger or smaller
brands show different effects of relative changes. One pos-
sible direction is to integrate brand size directly into the
model. Fourth, multinational corporations are interested in
understanding the differences in different markets. Thus,
analyzing the impact of advertising and retail drivers on
brand performance in non-US markets would be worthwhile.
Finally, we do not have information on brands’ contribu-
tion margin or profits. While budget allocation optimization
does not require this information, optimizing brands’ overall
budget does (e.g., Dorfman and Steiner 1954; Wright 2009).
Of the considerable digital advertising spending in the
United States, $189.8 (of $248.8) billion is in digital video
advertising, and retail media is on the rise and likely to hit
$100 billion by 2026 (Adgate 2022). Our study sheds new

247Data-driven budget allocation of retail media by ad product, funnel metric, and brand size
light on how advertising and retail factors drive growth
of different brands, and we hope to inspire exciting new
research in this area.
Funding Open access funding provided by Northeastern University
Library.
Data availability The data are confidential to the data provider, given
its contract with its customers.
Declarations
Conflict of interest All authors worked at Amazon Ads during the re-
search. No other conflicts of interest are present.
Open Access This article is licensed under a Creative Commons Attri-
bution 4.0 International License, which permits use, sharing, adapta-
tion, distribution and reproduction in any medium or format, as long
as you give appropriate credit to the original author(s) and the source,
provide a link to the Creative Commons licence, and indicate if changes
were made. The images or other third party material in this article are
included in the article’s Creative Commons licence, unless indicated
otherwise in a credit line to the material. If material is not included in
the article’s Creative Commons licence and your intended use is not
permitted by statutory regulation or exceeds the permitted use, you will
need to obtain permission directly from the copyright holder. To view a
copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
References
Aaker, D.A., A.L. Biel, and A. Biel. 2013. Brand equity & advertising:
Advertising’s role in building strong brands. New York: Psychol-
ogy Press.
Adgate, B. 2022. Retail media networks are the next big advertising
channel, Forbes, 1 December. https:// www. forbes. com/ sites/ brada
dgate/ 2022/ 12/ 01/ retail- media- netwo rks- are- the- next- big- adver
tising- chann el/? sh= 1a65c ee634 6c.
Ajzen, I., and M. Fishbein. 1977. Attitude-behavior relations: A theo-
retical analysis and review of empirical research. Psychological
Bulletin 84 (5): 888–918.
Arnold, M.J., and K.E. Reynolds. 2003. Hedonic shopping motivations.
Journal of Retailing 79 (2): 77–95.
Batra, R., and K.L. Keller. 2016. Integrating marketing communica-
tions: New findings, new lessons, and new ideas. Journal of Mar-
keting 80 (6): 122–145.
Bertozzi, G., S.R. Bagheri, B. Graham, P. Knowles, O. Netzer, and K.
Pauwels. 2022. How much does digital advertising accelerate new
product success? Applied Marketing Analytics 7 (4): 318–328.
Breuer, R., M. Brettel, and A. Engelen. 2011. Incorporating long-term
effects in determining the effectiveness of different types of online
advertising. Marketing Letters 22: 327–340.
Buil, I., L. De Chernatony, and E. Martínez. 2013. Examining the role
of advertising and sales promotions in brand equity creation. Jour-
nal of Business Research 66 (1): 115–122.
Chaudhuri, A. 2002. How brand reputation affects the advertising-
brand equity link. Journal of Advertising Research 42 (3): 33–43.
Colicev, A., A. Malshe, and K. Pauwels. 2018. Social media and
customer-based brand equity: An empirical investigation in retail
industry. Administrative Sciences 8 (3): 55.
Davey, J. 2023. Retail media ad revenue forecast to surpass TV
by 2028. Reuters, 12 June, https:// www. reute rs. com/ busin
ess/ retail- consu mer/ retail- media- ad- reven ue- forec ast- surpa
ss- tv- by- 2028- 2023- 06- 12/.
De Haan, E., T. Wiesel, and K. Pauwels. 2016. The effectiveness of
different forms of online advertising for purchase conversion in a
multiple-channel attribution framework. International Journal of
Research in Marketing 33 (3): 491–507.
De Vries, L., S. Gensler, and P. Leeflang. 2017. Effects of traditional
advertising and social messages on brand-building metrics and
customer acquisition. Journal of Marketing 81 (5): 1–15.
Dorfman, R., and P.O. Steiner. 1954. Optimal advertising and optimal
quality. American Economic Review 44 (5): 826–836.
Erdem, T., and J. Swait. 2004. Brand credibility, brand consideration,
and choice. Journal of Consumer Research 31 (1): 191–198.
Giuditta, K. 2022. The future of ecommerce demands a better under -
standing of online consumer journeys. retailTouchPoints, 10
November, https:// www. retai ltouc hpoin ts. com/ topics/ digit al-
comme rce/ the- future- of- ecomm erce- deman ds-a- better- under stand
ing- of- online- consu mer- journ eys.
Golder, P.N., M.G. Dekimpe, J.T. An, H.J. van Heerde, D.S. Kim,
and J.W. Alba. 2022. Learning from data: An empirics-first
approach to relevant knowledge generation. Journal of Market-
ing 87 (3): 319–336.
Golder, P.N., and G.J. Tellis. 1997. Will it ever fly? Modeling the
takeoff of really new consumer durables. Marketing Science 16
(3): 256–270.
Hanssens, D.M., ed. 2015. Empirical generalizations about mar -
keting impact , 2nd ed. Cambridge, MA: Marketing Science
Institute.
Hanssens, D.M., and K.H. Pauwels. 2016. Demonstrating the value
of marketing. Journal of Marketing 80 (6): 173–190.
Hanssens, D.M., G. Yildirim, S. Srinivasan, K.H. Pauwels, and M.
Vanhuele. 2014. Consumer attitude metrics for guiding market-
ing mix decisions. Marketing Science 33 (4): 534–550.
Howard, J.A., and J.N. Sheth. 1969. The theory of buyer behavior.
New York: Wiley.
Ibarra, C. 2020. What is Amazon Retail Readiness? Feedvisor,
October 21, https:// feedv isor. com/ resou rces/ amazon- marke
ting- adver tising- strat egies/ what- is- amazon- retail- readi ness/.
Keller, K.L., and D.R. Lehmann. 2006. Brands and branding:
Research findings and future priorities. Marketing Science 25
(6): 740–759.
Kraus, S.J. 1995. Attitudes and the prediction of behavior: A meta-
analysis of the empirical literature. Personality and Social Psy -
chology Bulletin 21 (1): 58–75.
Kübler, R., K. Pauwels, G. Yildirim, and T. Fandrich. 2018. App popu-
larity: Where in the world are consumers most sensitive to price
and user ratings? Journal of Marketing 82 (5): 20–44.
Kumar, V., B. Rajan, R. Venkatesan, and J. Lecinski. 2019. Under -
standing the role of artificial intelligence in personalized engage-
ment marketing. California Management Review 61 (4): 135–155.
Lecinski, J. 2011. Winning the zero moment of truth (eBook). Mountain
View, CA: Google Inc.
Lichtenstein, D.R., S. Burton, and E.J. Karson. 1991. The effect of
semantic cues on consumer perceptions of reference price ads.
Journal of Consumer Research 18 (3): 380–391.
Masters, K. 2022. Amazon just announced 7 new advertising features.
Which ones matter most? Forbes, 26 October 26, https:// www.
forbes. com/ sites/ kirim asters/ 2022/ 10/ 26/ amazon- just- annou nced-
7- new- adver tising- featu res- which- ones- matter- most/? sh= 6af99
8e02c 79.
Mathwick, C., N. Malhotra, and E. Rigdon. 2001. Experiential value:
Conceptualization, measurement and application in the catalog
and Internet shopping environment. Journal of Retailing 77 (1):
39–56.
Mela, C.F., S. Gupta, and D.R. Lehmann. 1997. The long-term impact
of promotion and advertising on consumer brand choice. Journal
of Marketing Research 34 (2): 248–261.

248 V. Qin et al.
Morwitz, V.G., E. Johnson, and D. Schmittlein. 1993. Does measur -
ing intent change behavior? Journal of Consumer Research 20
(1): 46–61.
Noble, S.M., D.A. Griffith, and M.G. Weinberger. 2005. Consumer
derived utilitarian value and channel utilization in a multi-channel
retail context. Journal of Business Research 58 (12): 1643–1651.
Novak, T.P., D.L. Hoffman, and A. Duhachek. 2003. The influence of
goal-directed and experiential activities on online flow experi-
ences. Journal of Consumer Psychology 13 (1/2): 3–16.
Park, E., R. Rishika, R. Janakiraman, M.B. Houston, and B. Yoo. 2018.
Social dollars in online communities: The effect of product, user,
and network characteristics. Journal of Marketing 82 (1): 93–114.
Pauwels, K., C. Demirci, G. Yildirim, and S. Srinivasan. 2016. The
impact of brand familiarity on online and offline media synergy.
International Journal of Research in Marketing 33 (4): 739–753.
Pauwels, K., S. Erguncu, and G. Yildirim. 2013. Winning hearts, minds
and sales: How marketing communication enters the purchase pro-
cess in emerging and mature markets. International Journal of
Research in Marketing 30 (1): 57–68.
Pauwels, K., M. Peran, Z. Shah, G. Schnaidt, and D. Vercamer. 2023.
Sponsored brands video rings up clicks and sales in the short and
long run. Journal of Marketing Analytics 11 (3): 275–286.
Pauwels, K., B. Sud, R. Fisher, and K. Antia. 2022. Should you change
your ad messaging or execution? It depends on brand age. Applied
Marketing Analytics 8 (1): 43–54.
Pauwels, K., and B. van Ewijk. 2020. Enduring attitudes and contextual
interest: When and why attitude surveys still matter in the online
consumer decision journey. Journal of Interactive Marketing 52
(1): 20–34.
Peltonen, J., J. Strahl, and P. Floréen. 2017. Negative relevance feed-
back for exploratory search with visual interactive intent mod-
eling. In: G.A. Papadopoulos and T. Kuflik (eds.) Proceedings of
the 22nd international conference on intelligent user interfaces.
New York: Association for Computing Machinery, pp. 149–159.
Petersen, J.A., V. Kumar, Y. Polo, and F.J. Sese. 2018. Unlocking the
power of marketing: Understanding the links between customer
mindset metrics, behavior, and profitability. Journal of the Acad-
emy of Marketing Science 46 (5): 813–836.
Rojas-Lamorena, Á.J., S. Del Barrio-García, and J.M. Alcántara-Pilar.
2022. A review of three decades of academic research on brand
equity: A bibliometric approach using co-word analysis and bibli-
ographic coupling. Journal of Business Research 139: 1067–1083.
Rutz, O.J., and R.E. Bucklin. 2011. From generic to branded: A model
of spillover in paid search advertising. Journal of Marketing
Research 48 (1): 87–102.
Simmons, C.J., B.A. Bickart, and J.G. Lynch Jr. 1993. Capturing and
creating public opinion in survey research. Journal of Consumer
Research 20 (2): 316–329.
Slotegraaf, R.J., and K. Pauwels. 2008. The impact of brand equity and
innovation on the long-term effectiveness of promotions. Journal
of Marketing Research 45 (3): 293–306.
Srinivasan, S., O.J. Rutz, and K.H. Pauwels. 2016. Paths to and off
purchase: Quantifying the impact of traditional marketing and
online consumer activity. Journal of the Academy of Marketing
Science 44 (4): 440–453.
Srinivasan, S., M. Vanhuele, and K. Pauwels. 2010. Mind-set metrics
in market response models: An integrative approach. Journal of
Marketing Research 47 (4): 672–684.
Tavşanoğlu, B. 2018. Decision support system for search engine adver-
tising campaign management by determining negative keywords.
Doctoral dissertation, Sabancı University.
Tellis, G.J. 2003. Effective advertising: Understanding when, how, and
why advertising works. Thousand Oaks, CA: SAGE.
Tourangeau, R., L.J. Rips, and K. Rasinski. 2000. The psychology of
survey response. Cambridge: Cambridge University Press.
Trusov, M., R.E. Bucklin, and K. Pauwels. 2009. Effects of word-of-
mouth versus traditional marketing: Findings from an internet
social networking site. Journal of Marketing 73 (5): 90–102.
Vakratsas, D., and T. Ambler. 1999. How advertising works: What do
we really know? Journal of Marketing 63 (1): 26–43.
Vakratsas, D., and Z. Ma. 2005. A look at the long-run effectiveness
of multimedia advertising and its implications for budget alloca-
tion decisions. Journal of Advertising Research 45 (2): 241–254.
Wright, M. 2009. A new theorem for optimizing the advertising budget.
Journal of Advertising Research 49 (2): 164–169.
Yadav, M.S., and P.A. Pavlou. 2014. Marketing in computer-mediated
environments: Research synthesis and new directions. Journal of
Marketing 78 (1): 20–40.
You, Y., G.G. Vadakkepatt, and A.M. Joshi. 2015. A meta-analysis
of electronic word-of-mouth elasticity. Journal of Marketing 79
(2): 19–39.
Zia, M., and R.C. Rao. 2019. Search advertising: Budget allocation
across search engines. Marketing Science 38 (6): 1023–1037.
Publisher's Note Springer Nature remains neutral with regard to
jurisdictional claims in published maps and institutional affiliations.
Vivian Qin received her doctoral degree in Marketing from Fuqua
School of Business, Duke University. She joined Amazon in Apr 2021.
Currently, she is the team lead for data science within analytics and
insights of Amazon Ads. She also advises global research program.
She is also adjunct professor of marketing analytics at University of
Maryland – College Park.
Koen Pauwels is the Associate Dean of Research and Distinguished
Professor at Northeastern University and founding General Director of
its Digital, Analytics, Technology and Automation (DATA) Initiative.
Koen’s European positions include Adjunct Professor at BI Norwegian
Business School, and Visiting Professor at Vrije Universiteit Amster -
dam. For 4.5 years, he was Principal Research Scientist at Amazon
Ads, with brand building and budget allocation recommendations
reaching hundreds of thousands of advertisers.  Koen received his
Ph.D. from UCLA, where he was chosen Top 100 Inspirational Alum-
nus. After getting tenure at the Tuck School of Business at Dartmouth,
he helped build the startup Ozyegin University in Istanbul. Named a
worldwide top 2% scientist, and ‘The Best Marketing Academic on the
Planet’, Koen published over 100 articles on marketing effectiveness,
from product innovation and dynamic pricing to distribution channels
and communication. This research was awarded by managers (Google,
WPP and Syntec), academics (O’Dell, Davidson, and Varadarajan) and
both (Gary Lilien ISMS-MSI-EMAC Practice Prize). Ongoing research
focuses on retail media and on better business for a better world, with
papers on privacy, disinformation, racial pay gap and ESG metrics.
Koen is the incoming editor-in-chief of the International Journal of
Research in Marketing, and Associate Editor for the Journal of Market-
ing, the Journal of Consumer Research, and the Journal of Interactive
Marketing. His books include ‘Modeling Markets’, ‘Modeling Dynamic
Relations among Marketing and Performance Metrics’, and ‘Advanced
Methods for Modeling Markets’ for analysts, and ‘Break the Wall:
Why and How to Democratize Digital in Your Business’, and ‘It’s Not
the Size of the Data – It’s How You Use It: Smarter Marketing with
Analytics and Dashboards for managers.
Bo (Bobby) Zhou is an associate professor of marketing and an Emerg-
ing Fellow at Smith at the Smith School of Business, University of
Maryland, College Park. His research focuses on competitive marketing
strategies, in particular, pricing and promotion in online platforms and
media markets. He uses both analytical models as well as experimental

249Data-driven budget allocation of retail media by ad product, funnel metric, and brand size
approaches in his research. His work has been published in the Journal
of Marketing Research, Marketing Science, and Management Science.
He also serves on the editorial board of Decision Science, International
Journal of Research in Marketing, Journal of Marketing Research, Jour-
nal of Retailing, and Marketing Science.
