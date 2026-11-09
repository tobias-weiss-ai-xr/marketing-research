---
title: 'Sponsored is the New Organic: Implications of Sponsored Results on Quality of Search Results in
  the Amazon Marketplace'
url: https://arxiv.org/abs/2407.19099
category: digital-marketing
subcategory: empirical
date: 2024-07
venue: AAAI
authors:
- Abhisek Dash
- Saptarshi Ghosh
- Animesh Mukherjee
- Abhijnan Chakraborty
- Krishna P. Gummadi
source: arxiv
pdf_url: https://arxiv.org/pdf/2407.19099
pages: 12
chars: 58327
fetched_at: '2026-11-08T13:18:16+00:00'
kb_version: 1
---

# Sponsored is the New Organic: Implications of Sponsored Results on Quality of Search Results in the Amazon Marketplace

Sponsored is the New Organic: Implications of Sponsored Results
on Quality of Search Results in the Amazon Marketplace
Abhisek Dash1, Saptarshi Ghosh2, Animesh Mukherjee2,
Abhijnan Chakraborty2, Krishna P. Gummadi1
1Max Planck Institute for Software Systems, Germany
2Indian Institute of Technology Kharagpur, India
adash@mpi-sws.org, saptarshi@cse.iitkgp.ac.in, animeshm@cse.iitkgp.ac.in,
abhijnan@cse.iitkgp.ac.in, gummadi@mpi-sws.org
Abstract
Interleaving sponsored results (advertisements) amongst or-
ganic results on search engine result pages (SERP) has be-
come a common practice across multiple digital platforms.
Advertisements have catered to consumer satisfaction and
fostered competition in digital public spaces; making them an
appealing gateway for businesses to reach their consumers.
However, especially in the context of digital marketplaces,
due to the competitive nature of the sponsored results with
the organic ones, multiple unwanted repercussions have sur-
faced affecting different stakeholders. From the consumers’
perspective the sponsored ads/results may cause degradation
of search quality and nudge consumers to potentially irrele-
vant and costlier products. The sponsored ads may also af-
fect the level playing field of the competition in the market-
places among sellers. To understand and unravel these po-
tential concerns, we analyse the Amazon digital marketplace
in four different countries by simulating 4,800 search oper-
ations. Our analyses over SERPs consisting 2M organic and
638K sponsored results show items with poor organic ranks
(beyond 100th position) appear as sponsored results even be-
fore the top organic results on the first page of Amazon SERP.
Moreover, we also observe that in majority of the cases, these
top sponsored results are costlier and are of poorer quality
than the top organic results. We believe these observations
can motivate researchers for further deliberation to bring in
more transparency and guard rails in the advertising practices
followed in digital marketplaces.
Introduction
Digital marketplaces have emerged as ubiquitous plat-
forms to serve the purchase needs of consumers and liveli-
hood of businesses across the globe 1. These platforms me-
diate the interaction between consumers and businesses
through sophisticated algorithmic systems and choice archi-
tectures (Dash et al. 2021, 2022). In recent years,advertising
has evolved as a lucrative gateway for businesses to reach
potential consumers on online marketplaces. For instance,
advertisements on Amazon are said to reach almost 96% of
all Americans between the age of 25 and 54 (FTC 2023).
Copyright © 2024, Association for the Advancement of Artificial
Intelligence (www.aaai.org). All rights reserved.
1In this paper, we shall discuss the different nuances by keep-
ing Amazon marketplace as a case study. Most of the practices dis-
cussed here are also deployed by other e-commerce marketplaces.
Sponsored product advertisements on Amazon: When
a consumer searches for a query on Amazon, a number of
results are shown in different arrangements on its search en-
gine result pages (SERPs) in the decreasing order of rele-
vance (Sorokina and Cantu-Paz 2016). Increasingly, some of
the results are marked with small gray tags that read ‘Spon-
sored’. These are sponsored product advertisements (Ama-
zon 2024) on Amazon. These sponsored results can be
looked as a way of providing exposure to sellers who are
getting started on the marketplace and would find it harder to
get better organic ranks (Amazon 2024). In fact, many sell-
ers have utilised sponsored product ads for improving their
sales and revenue. Amazon also ensures that only those sell-
ers’ advertisements show up as sponsored results who are
eligible to win the buy box of Amazon i.e., they are amongst
the better sellers who as per Amazon’s estimate can provide
good quality of service to consumers (Support 2024).
However, increasingly sponsored results and their place-
ments are gaining attention among policymakers. Over time,
these sponsored results are replacing organic results at the
top of SERPs. For example, Figure 1 shows the first two
rows of search results for the query ‘baby wipes’ on Ama-
zon. The first four results (highlighted within red rectangle)
on the SERP are all sponsored results i.e., advertisements.
Each sponsored result is demarcated with a tag which has
been encircled in blue. The organic results start at the right
hand corner of the top row. Note that the organic results are
ranked based on prior user engagement (clicks, product page
visits, purchases, etc.) with different products while search-
ing for the same query (Sorokina and Cantu-Paz 2016). Fur-
ther, the same product can appear as sponsored and organic
results on the SERP as well. For example, the first product
in Figure 1 also appears as a result in the SERP in organic
position two. In this paper, we consider that this first spon-
sored result has an organic rank two. Next we discuss some
potential concerns with sponsored ads keeping this example
figure in the perspective.
Potential concerns from the point of view of consumers:
Note that apart from the first product (which costs 22.25$),
none of the other sponsored results are among the top-5
organic results shown on the SERP. Due to cognitive bi-
ases, most consumers tend to give more attention to the top
left of a web-page (Baeza-Yates 2018). Similarly, multiple
works have shown results appearing higher in the ranked
arXiv:2407.19099v1  [cs.CY]  26 Jul 2024

Figure 1: First two rows of the search engine result page (SERP) for query ‘baby wipes’ onAmazon.com. The first four
results are sponsored results (i.e., ads) while the rest of the results shown are organic.
lists are perceived to be more relevant and are more likely
to be clicked (Biega, Gummadi, and Weikum 2018; Singh
and Joachims 2018). Hence, by being positioned before the
organic results, sponsored ads are more likely to be clicked
(or even purchased) by consumers. Although, in Amazon’s
defense, these results are demarcated as ‘sponsored’, prior
surveys have shown that almost half of the consumers on
Amazon are not able to distinguish between sponsored and
organic results (Graham 2019). On most occasions, these
demarcations are in significantly smaller fonts and in gray
color (as seen in Figure 1). Even worse, sometimes it may
not even read ‘Sponsored’ but as ‘Featured from Amazon
brands’, as in the first result in Figure 1. Replacing top or-
ganic results with relatively lower quality sponsored results
(without proper demarcation) can potentially nudge con-
sumers to irrelevant products and lead to consumer dissat-
isfaction. In fact, Amazon’s internal surveys also hint at in-
clusion of sponsored results affecting consumer satisfaction.
However, the ad revenue outweighs the loss that Amazon
has endured due to degradation of search result quality (FTC
2023); giving further incentive to Amazon to increase the
ad-estate on its SERPs.
Now, let us consider the price of the different sponsored
results and organic results in Figure 1. The average price of
the four sponsored results is 25.8$; whereas that of the same
number of top organic results is 18.83$. Hence, the average
price of sponsored results is 37% costlier than the average
price of organic results. Although this is an anecdotal ex-
ample, these concerns are also raised in the lawsuit filed by
FTC against Amazon late last year (FTC 2023). If this phe-
nomenon is a frequent occurrence, then sponsored ads may
systemically nudge consumers towards costlier products.
Potential concerns from the point of view of sellers: Re-
placing and / or interleaving sponsored results among or-
ganic results demotes products from their organic and de-
served position that they merit. For example, the Pamper
sensitive baby wipes (shown as the penultimate result in
Figure 1) would be placed in the first row had there been
no sponsored results at all. Consumers would not require to
scroll down to get to see the product on most standard laptop

or desktop devices. Such deprivation of exposure may have
effects on the sales and revenue of the corresponding sellers.
Furthermore, sponsored results being the first point of
interaction for consumers, sellers and businesses will have
more incentives to use advertisements as their gateway to
reach consumers. If so, this will end up favoring the larger
sellers and putting the new and small scale sellers at disad-
vantageous position. Since all these ads are allocated based
on second price auctions (Amazon 2024), the seller bidding
the highest price will eventually end up getting more expo-
sure. This, in turn, (a) may result in affecting the competition
in the marketplace and (b) the increased cost on advertising
may trickle down to consumers in terms of increased prices.
Concerns resonated by policymakers: The concerns de-
scribed above have been resonated by policymakers across
the globe. In the past few years, Amazon has faced multi-
ple antitrust investigations (Response 2019, 2020; Release
2020; FTC 2023). Most of the antitrust investigations focus
on Amazon’s preferential treatment toward itself or some re-
lated sellers. However, we fear that some of the practices
described above can have much more fundamental ramifica-
tions in the functioning of a fair marketplace. Even without
the existence of any special relationships, interleaving and
replacing organic results with potentially less relevant and
costlier ads can cause harm to consumers and competition
on the digital marketplaces.
Current work: In this work, we carry out a comprehensive
study of the effects and implications (if any) of sponsored re-
sults on the quality of search results in digital marketplaces.
As a case study, we conduct our investigations on four
different marketplaces of Amazon i.e., in Amazon.com
(USA), Amazon.in (India), Amazon.de (Germany) and
Amazon.fr (France). By designing web-scrapers, we col-
lect search result data from each of these marketplaces. Our
extensive analyses on 4,800 search operations and the re-
sultant SERPs consisting of more than 2M organic results
and 638K sponsored results bring out multiple concerning
observations regarding top Amazon search results:
• Nearly 30% of results in our collected dataset on Amazon
are sponsored results i.e., advertisements. In 85% cases at
least one sponsored result appears before the top organic
result on the first SERP.
• Many of the top sponsored results appearing in the ob-
served SERPs seem to be less relevant than the organic
results as per Amazon’s own ranking algorithm. Almost
half of the sponsored results never appear within the first
three pages of the collected organic results.
• In more than half of the instances, the top sponsored re-
sults are 50% costlier than the corresponding top organic
results in our dataset. In other words, through positioning
sponsored results before organic results, consumers may
potentially be nudged to seemingly costlier products.
Curious case of ads on digital marketplaces: We want to
clarify that we do not posit that advertising in all cases is
harmful to consumers and fair competition. In fact, if prop-
erly conducted, advertising can improve consumer satisfac-
tion and foster healthy competition on the marketplaces.
However, the case of digital marketplaces is a tricky one. If
we notice Figure 1 again, the same product is appearing as
the first sponsored result and the second organic result, i.e.,
the candidates of sponsored results and organic results are
not mutually exclusive or complementary. In fact, in most
cases they are competing offers or products. In other words,
advertisements in digital marketplaces arecompetitive in na-
ture with the organic results (Dash et al. 2021).
Further, there can be significant delayed impact of these
sponsored result on organic ranking as well. For example,
as per Amazon’s internal experiments, advertised products
are 46 times more likely to be clicked on as opposed to non-
advertised products (FTC 2023). At the same time, click-
through and several other browsing patterns are important
metrics in deciding organic ranking (Sorokina and Cantu-
Paz 2016). Thus, if organic results on top of the page are
increasingly replaced by sponsored results, it may not only
propel some of the short term harms to consumers and busi-
nesses at scale, but also result in long term harms to the or-
ganic competition in the marketplace. Similar concerns were
also raised by Page et al. (1999) in their seminal work on
PageRank algorithm, where they discussed how commercial
interests can be a threat to organic ranking and the primary
goals of a search system. In fact, our observations in this pa-
per demonstrate that Amazon’s practices in showing spon-
sored ads in their SERPs may not arguably comply with sev-
eral regulations on fair commercial practices in many coun-
tries. We discuss these legal aspects in the penultimate sec-
tion of the paper. Hence, we posit such fairness concerns
should not go unnoticed by auditors, policymakers, practi-
tioners and the platform companies as well.
Related work
In this section, we survey some prior works especially in
the area of (a) auditing digital marketplaces, (b) algorithmic
auditing of content search, and (c) regulations on fair com-
mercial practices to further contextualise the current work.
Auditing digital marketplaces
While Algorithmic auditing has emerged as a vibrant new
direction of research under the broad umbrella of Respon-
sible AI , most of the prior works have come in the con-
text of digital public space (Kulshrestha et al. 2017; Ali
et al. 2019) and sensitive applications e.g., recidivism pre-
diction (Angwin et al. 2022); gender detection (Buolamwini
and Gebru 2018; Jaiswal et al. 2022); algorithmic hir-
ing (Wilson et al. 2021) etc. Thus a long line of research
has focused on fairness concerns regarding different sensi-
tive demographics. However, the context of digital market-
places has been largely understudied. Recently, some stud-
ies have tried to understand the intricacies and fairness con-
cerns in digital marketplaces (Dash et al. 2024) focusing on
their (a) related item recommendations (Dash et al. 2021),
(b) choice architectures (Dash et al. 2024). These works
delve into the anti-competitive concerns in the digital mar-
ketplace. Whereas, several other studies look into issues like
algorithmic pricing (Chen, Mislove, and Wilson 2016), fair-
ness across different modalities (Dash et al. 2022), vaccine
misinformation (Juneja and Mitra 2021) on Amazon.

In contrast, the current study focuses on the most impor-
tant apparatus on Amazon ecosystem i.e., Amazon search
with an aim to understand how sponsored advertising may
potentially distort the observed ranking of products and what
are their repercussions to the quality of search results.
Algorithmic auditing of content search
Algorithmic auditing is not new in the context of content
search. Multiple prior audit studies have been conducted
with different goals in mind. Mehrotra et al. (2017) studied
whether Bing search engine provides equal level of satis-
faction to its end-users. Kulshrestha et al. (2017) proposed
a bias quantification metric to evaluate the political biases.
The same metric was then utilised to evaluate the partisan-
ship of Google search result as well (Robertson et al. 2018).
While bias in search results has been a well-studied prob-
lem, interleaving of sponsored results and their effects has
not yet been well studied. The interleaving of sponsored re-
sults become even more important in the context of digital
marketplaces such as Amazon where the advertisements are
traditionally lower funnel and are competitive in nature with
the organic results (Dash et al. 2021). Hence the effects of
such interleaving should not go unnoticed.
Regulations on fair commercial practices
Maintaining fairness in marketplaces (both physical and dig-
ital) is of paramount importance. Thus a series of such reg-
ulations are in place in different parts of the world. Older
regulations e.g., the Federal Trade Commission Act (FTC
2006) in the USA; Unfair commercial directives (EU 2021)
in the EU; Consumer Protection Act (GOI 2019) in India –
all prohibit adopting unfair and deceptive commercial prac-
tices in the marketplaces. However, with increasing reliance
on digital marketplaces, many countries are coming up with
new directives to set guidelines for fair conduct on the online
world to avoid deceptive user interface design and bring in
transparency in deployed design choices and algorithms e.g.,
Dark Pattern directives in India (GOI 2019) and DSA (Re-
lease 2022), DMA (Commision 2022) in the EU. We shall
discuss some specific regulations in detail later in the paper,
when we outline the legal implications of our observations.
Data collection
Amazon search system is context sensitive (Sorokina and
Cantu-Paz 2016) i.e., it uses different search ranking model
for different contexts, where contexts are defined by the
category of products and the specific Amazon market-
places (e.g., USA or India etc.). To this end, our data col-
lection strategy covers more than ten product categories
across four popular Amazon marketplaces across the globe –
Amazon.in (India), Amazon.com (USA), Amazon.de
(Germany) and Amazon.fr (France). The increasing at-
tention of policymakers toward digital marketplaces in these
countries has motivated us to study these marketplaces.
Search queries in two settings - default and refined: We
start our data collection by searching for several queries on
Amazon’s desktop search across the four marketplaces. We
Category # Query Category # Query
Refined setting (50 queries × 4 snapshots × 4 marketplaces)
Electronics 9 Mobile accessories 3
Computer accessories 8 Office products 3
Home & Kitchen 9 Home improvement 2
Health & personal care 8 Video games 2
Amazon devices 4 Others 2
Default setting (1000 queries × 1 snapshot × 4 marketplaces)
Electronics 238 Mobile accessories 74
Computer accessories 211 Office products 48
Home & Kitchen 118 Home improvement 50
Health & personal care 112 Video games 25
Sports, fitness 21 Luggage and bags 79
Table 1: Distribution of queries from top-10 categories
present in our dataset. For these 50 queries, we collected
data for 4 countries across 4 different timestamps. For
a super set of 1000 queries, we also collect data for one
snapshot across the 4 countries.
observe that for all queries, irrespective of the query cate-
gory, we get a maximum of 306 organic results. Amazon
search box has several refinement settings as per the differ-
ent product categories available on the marketplace. The de-
fault search setting is ‘All categories’ which is used by most
end-users. In this setting, only 306 organic results are shown
for a given query, i.e., it does not show an exhaustive list of
products for the query.
However, for the purpose of our analyses, we need to
know the organic position of as many sponsored products
as possible; even beyond 306. Hence, we choose to collect
data in the refined setting where we specify a category for
the search query. Through this setting, one can have access
to more products relevant to the query under the specified
category. On the website of each of the four Amazon mar-
ketplaces stated earlier, we search for a set of 50 queries
using the refined setting. The selected queries are among
the most searched queries on Amazon (Hardwick 2021) and
also belong to some of the top and most competitive prod-
uct categories on Amazon (Connolly 2024). The number of
queries across the different top categories are shown in the
upper panel of Table 1. In this setting, we collect results for
50 queries across 4 different marketplaces at4 different tem-
poral points (which we refer to as snapshots).
However, due to the overarching nature of the default set-
ting, most end-users may actually query in the default set-
ting and hence are exposed to search result pages returned
in the default setting. Hence, we also collect one snapshot
of search results for 1000 queries in the default setting, to
investigate if observations in those SERPs conform to what
we observe in the refined setting. The set of 1000 queries has
been inherited from a prior work Dash et al. (2022). This set
of queries cover some of the most competitive and popular
categories e.g., electronics, computer accessories, home and
kitchen, etc. The distribution of the queries across categories
are shown in the lower panel of Table 1.
Crawling methodology: To this end, we design a web-
scraper to mimic search operations on Amazon desktop

websites. The scraper is seeded with a query, and the cor-
responding search results are scraped. We perform this task
till we get the last indexed SERP on Amazon for the given
query. This enables us to find the organic search rank (and
thus the Amazon defined relevance ) of each product that
Amazon indexes at a certain point of time with respect to the
mentioned query. We use Gecko driver and Mozilla Firefox
browser for our data collection.
We take some precautions to ensure the meaningfulness
of the comparative analysis. The search algorithms are likely
to tailor results based on several signals, including the geo-
graphical location, consumer browsing history, and so on. To
minimize these variations, we collect search results over four
different weeks through incognito Firefox browsers, during
the same time frame, with the same delivery address and
keeping all the necessary contexts e.g, account, IP address,
delivery address etc. as similar as possible.
Data collected: Upon searching a query on Amazon, a list
of products are shown on the search engine result pages
(SERPs). The search results are organised in different pages
with several number of results per page. We collect the
search results for each of the queries till we find no next
available SERP. As stated earlier, Amazon shows two types
of search results – organic (algorithmically curated results
considering prior consumer behavior) and sponsored ads.
For each result, we collect its type. For each product shown
as a search result, we also collect different metadata, e.g.,
brand, price, average user rating, number of reviews, etc.
Next, we will investigate how sponsored search results may
affect the quality of Amazon search results.
Observations
In this section, we describe the important observations on
how the sponsored ads may affect the quality of search re-
sults on Amazon. We perform our analyses across three im-
portant factors: (a) How prevalent are sponsored results on
Amazon SERPs for different queries? (b) How relevant are
the top sponsored results as per Amazon’s own organic rank-
ing? (c) How comparable are the top sponsored results with
the top organic results (based on price and quality)?.
How prevalent are sponsored results on Amazon
SERPs for different queries?
For all queries across different snapshots, we observe some
sponsored results interleaved among the organic results. Ta-
ble 2 shows the number of organic results and sponsored
results collected across the different settings during our data
collection. Across the board, almost 1/3rd of the observed
Amazon SERPs constitute of sponsored results. Apart from
France, the percentage of sponsored results increases in the
default setting. However, the presentation of these sponsored
results is not uniform. Usually, sponsored results are shown
in the top, middle and at the end of a SERP depending on
the number of results shown on the SERP.
For the sake of the analyses reported in this section, we
will rely on sponsored results which especially appear be-
fore even the first organic result . We focus on these spon-
USA
India
Germany
France
0
1
2
3
4
Average number of sponsored results
 before top organic result
2.42
2.67 2.63
2.92
2.62
2.88
2.66
3.63
Refined Default
Figure 2: Average number of sponsored results appear-
ing before the top organic search result across the four
marketplaces for all the queries in different settings. In
general 2–3 sponsored results precede organic results;
the number is slightly higher in default setting across the
four marketplaces consistently.
sored results since they are almost certain to get the maxi-
mum attention of the consumers. In the refined setting of our
data collection for 50 queries across four snapshots across
the four marketplaces, we find that in 84.5% queries, at least
one sponsored result appear before the top organic result.
The same percentage increases slightly to 87.37% in the de-
fault setting (where a user queries the search box with ‘all
categories’ setting). This increase is due to a significant rise
in the provision of ads in default setting for the US market-
place. The percentage for each of the marketplaces is shown
in Table 3. The average number of sponsored results appear-
ing before top organic results is shown in Figure 2. We ob-
serve that 2–3 sponsored results usually appear before the
top organic result irrespective of the marketplace and search
setting. The average number of sponsored result before top
organic result, in fact, increases in the default setting.
Implications: While it is very intuitive that Amazon SERPs
show both sponsored and organic results to end-users, nearly
30% of all results on Amazon SERP are observed to be spon-
sored. Interestingly, 2-3 sponsored results usually precede
the top organic result on the first Amazon SERP for most
of the searches we conducted. This observation is striking
because in nearly 85% (or above) cases, at least one spon-
sored result appears even before the top organic result on
these SERPs. Note that, many end-users upon searching for
a product tend to click or engage more with the first results
that appear in the SERPs (Dash et al. 2022; Rubin 2019).
Our observation shows that in 85% cases, those first results
are sponsored results.
How relevant are the top sponsored results to the
query, as per Amazon’s own ranking?
The previous observation demonstrates that a significant
fraction of Amazon SERPs show sponsored results before
the top organic results. The key follow up question is – how
relevant are the sponsored results to the query? If the spon-
sored results (that appear before the organic results) are ac-
tually very relevant to the queries, then they may not neces-
sarily degrade the search result quality. In fact in such cases,

Country #Organic results #Sponsored results
Refined setting (50 queries × 4 snapshots × 4 marketplaces)
USA 143,000 40,177 (28.09%)
India 1,069,399 228,068 (21.32%)
Germany 97,930 29,532 (30.16%)
France 117,899 33,260 (28.21%)
Default setting (1000 queries × 1 snapshot × 4 marketplaces)
USA 258,446 84,951 (32.87%)
India 230,432 64,881 (28.15%)
Germany 272,978 92,646 (33.94%)
France 240,510 64,545 (26.84%)
Table 2: Number of organic and sponsored results col-
lected in each of the data collection setting. Almost1/3rd
of Amazon SERP are sponsored results.
Marketplace Refined Default
USA 77.0% 91.5%
India 83.5% 77.7%
Germany 89% 91.9%
France 88.5% 88.4%
Overall 84.5% 87.37%
Table 3: Percentage of queries where we found a spon-
sored result (advertisement) appearing even before the
top organic result across the different Amazon market-
places in the two settings of data collection.
putting such sponsored results may lead to consumer satis-
faction, while fostering competition by giving exposure to
other competing sellers.
Relevance of sponsored results: There are multiple ways
to operationalise the notion of relevance for different results
in the context of a query. One can come up with some sim-
ple model that utilises the different publicly available fea-
tures of the products to rank them in decreasing order of rel-
evance. To this end, we consider the Amazon search ranking
algorithm itself, which leverages multiple nuanced features
(some public and some private) to come up with the final
ranking of products based on relevance. Hence, we choose
to collect Amazon search results till the end (or till allowed),
to see where a sponsored result appears organically. In other
words, the rank at which a sponsored product appears for the
first time as an organic result is considered as a proxy for its
relevance (as evaluated by Amazon’s ranking algorithm).
Where do the top sponsored results appear organically?
Figure 3 show the average organic rank of top sponsored re-
sults for different queries in our collected dataset. For exam-
ple, for a query q, let us assume 3 sponsored results appear
before the top organic result, and the organic ranks of those
products are at positions x, y, z. Then the corresponding Y-
axis value shows the mean of the three organic positions i.e.,
(x + y + z)/3. The higher the value, lesser the relevance –
i.e., 0 is the top ranked most relevant product as per Ama-
zon’s organic ranking. If a sponsored product isnot found at
all in the organic ranked list, we consider its organic position
to be the total length of the organic result list. Figure 3 (a–d)
show the average organic rank of top sponsored results along
Countries 1st page 2nd page 3rd page
Refined setting (50 queries × 4 snapshots)
USA 73.44% 67.90% 64.55%
India 57.55% 49.63% 43.68%
Germany 65.09% 53.15% 48.38%
France 63.43% 57.87% 52.55%
Default setting (1000 queries)
USA 61.45% 51.35% 46.29%
India 54.59% 43.18% 38.21%
Germany 67.08% 58.49% 54.18%
France 64.98% 55.26% 48.97%
Table 4: Percentage of top sponsored results on Amazon
SERPs appearing in organic positions that are beyond
the first, second and third SERPs respectively. Apart
from India, in all the other marketplaces more than 50%
of sponsored results appear beyond the second SERP for
the first time as an organic result.
with a standard deviation error bar (variation across 4 tem-
poral snapshots) on Y-axis for the different queries (X-axis).
The average organic rank of most SERPs are found to be
beyond 100 i.e., the overall relevance of the top sponsored
results is not comparable with the top organic results in the
observed search results. Similarly, Figure 3 (e–h) show the
same observation for the default setting i.e., where a total
of 306 organic results are shown. Much like the observa-
tion in the refined setting, in the default setting as well the
top sponsored results often come from very bad ranks as per
Amazon’s organic search ranking.
Note that nearly 70% of consumers never go beyond the
first Amazon search engine result page (FTC 2023). If we
consider a geometric decay of exposure, then nearly 97.3%
consumers would never go beyond the third page of Ama-
zon’s search results. If we analyse the organic ranks of the
advertised products closely, we see that a large majority of
them do not get positioned in the top-3 Amazon SERPs as
organic results i.e., they are significantly less relevant as per
Amazon’s own search ranking. Table 4 shows the fraction
of times the top sponsored results appear beyond the top-3
Amazon SERPs in our observed SERPs. For example, in the
United States 64.55% of the top sponsored products do not
get organic positions among the first 3 Amazon SERPs. In
general, nearly 50% of sponsored results do not merit a posi-
tion in the top-3 SERPs based on Amazon’s ranking system.
Similar observations are made in the default setting. How-
ever, we notice a drop in percentages in the default setting
as compared to the refined setting (apart from Germany).
Are the top sponsored results under-explored?
Increasingly Amazon has promoted its sponsored product
advertisements as a means to provide exposure to products
(and their sellers) who may not have gotten exposure organ-
ically (Amazon 2024). Note that Amazon SERPs show the
number of ratings that each product has received over their
lifetime; which can be considered as a proxy for how many
consumers may have purchased the same product. Thus, we

0 5 10 15 20 25 30 35 40
0
200
400
600
800
1000
1200
 Average organic rank of
top sponsored results
(a) USA (Refined)
0 10 20 30 40
0
250
500
750
1000
1250
1500
1750
 Average organic rank of
top sponsored results
 (b) India (Refined)
0 10 20 30 40
0
200
400
600
800
1000
 Average organic rank of
top sponsored results
 (c) Germany (Refined)
0 10 20 30 40
0
100
200
300
400
500
 Average organic rank of
top sponsored results
 (d) France (Refined)
0 200 400 600 800
0
50
100
150
200
250
300
 Average organic rank of
top sponsored results
(e) USA (Default)
0 100 200 300 400 500 600 700 800
0
50
100
150
200
250
300
 Average organic rank of
top sponsored results
 (f) India (Default)
0 200 400 600 800
0
50
100
150
200
250
300
 Average organic rank of
top advertised products
 (g) Germany (Default)
0 200 400 600 800
0
50
100
150
200
250
300
 Average organic rank of
top sponsored results
 (h) France (Default)
Figure 3: Mean (and standard deviation error bar) organic rank, as evaluated by Amazon’s own search ranking algo-
rithm, of top sponsored results appearing before the top organic results on Amazon SERPs for different queries (along
X-axis) across the four marketplaces. For a large majority of cases the top sponsored results appear below organic rank
100 across the four marketplaces for different queries consistently.
Country ≥ 1000 #Ratings ≥ 5000 #Ratings
Refined setting (50 queries × 4 snapshots)
USA 57.49 42.51
India 60.09 31.61
Germany 52.99 26.28
France 45.95 26.28
Default setting (1000 queries)
USA 47.58 30.80
India 42.58 22.47
Germany 46.19 23.26
France 44.82 22.74
Table 5: Percentage of times top sponsored results have
#Ratings more than 1000 and 5000 respectively.
take a look at the number of ratings that the different spon-
sored products might have had.
The observations are listed in Table 5. We find that nearly
50% of all top sponsored products have more than 1000
number of ratings i.e., a minimum of 1000 people have
rated and reviewed those products. More than 50% of those
products in fact have the number of ratings beyond 5000.
Prior consumer surveys show that many consumers are more
likely to purchase products that have more than 1000 rat-
ings (Fischer 2024). Furthermore, the conversion rate drasti-
cally increases when the number of ratings go beyond 5000.
Note that the median number of ratings received byall prod-
ucts that we observed in our data collection across India,
USA, Germany and France are 8, 57, 51, 29 respectively.
Hence, we can infer that the products appearing as top spon-
sored results are typically more explored as opposed to the
median products in our dataset. At the same time, they are
more likely to be clicked by consumers because of higher
#Ratings because of their positioning before the top organic
results.
How comparable are the top sponsored and
organic results on Amazon SERPs?
Although many of the sponsored results we observed come
from very low ranks, i.e., they are less relevant as per the
Amazon’s product ranking, we now check if they are com-
parable with the top organic products in terms of different
features which consumers perceive to be important. For ex-
ample, they may still be of comparable or less price; higher
quality. In such cases, the eventual harm to consumers may
not be as significant either.
To fairly compare the sponsored and organic results, we
turn our focus to the sponsored results appearing before the
top organic results. For a query q, let us assume there are
k sponsored results appearing before the first organic result.
In such case, we compare the top- k sponsored results with
the top- k organic results on the basis of some property p
(e.g., price or quality). In such cases, we compare the av-
erage property of the top sponsored and organic results e.g.,
the average price of top-k sponsored results and that of top-k
organic results for a particular query are compared.
Top sponsored results are costlier than top organic re-
sults: Price is one of the key features which helps consumer
in transactional decision making. Hence, first we check how

Countries ≥ 1.2× ≥ 1.5× ≥ 2×
Refined setting (50 queries × 4 snapshots)
USA 80.73% 63.30% 39.45%
India 79.84% 54.26% 37.98%
Germany 86.81% 70.14% 49.31%
France 82.44% 48.09% 29.01%
Default setting (1000 queries)
USA 78.53% 53.23% 27.50%
India 80.45% 59.39% 37.19%
Germany 80.11% 58.65% 36.19%
France 80.18% 55.89% 30.70%
Table 6: Percentage of times when top sponsored results
on Amazon are 1.2, 1.5 or 2 × costlier than the top or-
ganic results. More than 50% cases, the average price of
the top sponsored results is more than 1.5 × of the aver-
age price of the top organic results.
comparable are the prices of top sponsored and organic re-
sults on Amazon SERPs we collected. Figure 4 shows the
mean and standard deviation error bar of ratio of price of
top sponsored results to top organic results for all the queries
where there are at least one sponsored result shown before
the organic result on the Y-axis. We have highlighted the
horizontal line at Y = 1as a baseline for the average prices
to be similar. We observe that the top sponsored products
are costlier in 70.78%, 77.24%, 80.89% and 74.01% cases,
in USA, India, Germany and France respectively than the
organic products in our collected SERPs.
Table 6 shows the difference between the average prices.
For example, in more than 50% cases, the average price of
the top sponsored results is more than 1.5 times that of aver-
age price of as many top organic results. Similar trends are
observed in the default setting, a setting which is used by
millions of consumers. In fact, in almost 1/3rd of the cases
in the collected SERPs, the average price of top sponsored
results is more than double that of the top organic results.
Quality of organic results are superior: Much like price,
the quality of the product is of utmost importance in con-
sumers’ decision making. For our experiment, we take a
product’s average user rating (out of 5 stars) as an indica-
tor of its quality. We observe that the average quality of top
sponsored products are less than that of the organic products
in 43.5%, 47.3%, 57.3% and 59.89% respectively in USA,
India, Germany and France (see Table 7). The observations
are qualitatively similar for the default setting as well across
the different marketplaces.
Implications of our observations
Implications for the consumers: If a product appearing at
organic position 100 is shown to a consumer as the first re-
sult (albeit sponsored), consumers are more likely to click
on such results due to their cognitive position biases (Baeza-
Yates 2018). In fact, Amazon itself reports that nearly 35%
consumers click on the first result appearing on Amazon
SERPs (Rubin 2021); which increasingly is a sponsored re-
sult or an advertisement. Further, one should also note that
Country Better quality Lower quality
Refined setting (50 queries × 4 snapshots)
USA 56.50 43.50
India 52.70 47.30
Germany 42.70 57.30
France 40.11 59.89
Default setting (1000 queries)
USA 50.71 49.29
India 52.50 47.50
Germany 42.76 57.24
France 41.41 58.59
Table 7: Percentage of times top sponsored results are of
better or comparable quality than the top organic results
in its vicinity. Sponsored results are not of any better
quality than the organic results.
Graham (2019) showed almost half of the participants on
Amazon cannot even distinguish between sponsored and or-
ganic results. Thus, positioning such irrelevant product on
top of observed rankings may potentially nudge consumers
to significantly less relevant options for their desired query
leading to consumer dissatisfaction.
While positioning irrelevant products decreases search
quality, it also is observed to nudge consumers toward po-
tentially costlier products. While Amazon is known for its
consumer-centric policies, this comes as a contradiction.
Even worse, these products are not even of significantly bet-
ter quality i.e., even the quality cannot always justify the
extra cost that consumers have to pay.
Implications for the sellers and competition: From the
perspective of sellers, a number of sellers who have strug-
gled hard to achieve the top organic positions based on prior
engagement / purchase etc., are downgraded (below spon-
sored results) on the observed search ranking. This, in turn,
may deprive them of opportunities to sales and revenue.
Furthermore, such practices can have bigger implications
on the competition in the marketplaces. By virtue of promot-
ing sponsored results at the cost of organic results, essen-
tially sellers are encouraged to invest more on advertising
than to improve or maintain product quality and / or com-
petitive prices. In other words, increasingly advertisement
has become the primary gateway for business users to reach
and attract the attention of the large consumer base of Ama-
zon. This not only increases the costs that sellers must bear
to reach potential consumers but also results in those extra
costs being passed down to the consumers resulting in higher
price. Further, this may even hand in an advantage to poten-
tially large sellers on marketplace who can afford to spend
big on advertising.
Legal implications of our observations
Policymakers across the globe have been proactive on pre-
serving fairness in commercial practices especially from the
vantage points of the businesses and consumers. In this sec-
tion, we briefly discuss the observations in context of some
of the consumer protection and fair commercial practice

0 5 10 15 20 25 30 35 40
0
2
4
6
8
10
12
14
Ratio of Price of T op
Sponsored and Organic results
(a) USA (Refined)
0 10 20 30 40
0.0
2.5
5.0
7.5
10.0
12.5
15.0
17.5
Ratio of Price of T op
Sponsored and Organic results
 (b) India (Refined)
0 10 20 30 40
0
1
2
3
4
5
6
7
Ratio of Price of T op
Sponsored and Organic results
 (c) Germany (Refined)
0 10 20 30 40
0
2
4
6
8
Ratio of Price of T op
Sponsored and Organic results
 (d) France (Refined)
0 200 400 600 800
0
5
10
15
20
Ratio of Price of T op
Sponsored and Organic results
(e) USA (Default)
0 100 200 300 400 500 600 700 800
0
5
10
15
20
25
30
Ratio of Price of T op
Sponsored and Organic results
 (f) India (Default)
0 200 400 600 800
0
5
10
15
20
25
30
35
40
Ratio of Price of T op
Sponsored and Organic results
 (g) Germany (Default)
0 200 400 600 800
0
2
4
6
8
10
12
14
Ratio of Price of T op
Sponsored and Organic results
 (h) France (Default)
Figure 4: Mean (and standard deviation error bar) ratio of average price of top sponsored and organic results for
different queries (along X-axis) on Amazon SERP. For a large majority of cases the top sponsored results are costlier
than top organic results.
guidelines in the relevant parts of the world.
The United States of America
Section 5 of the Federal Trade Commission (FTC) Act de-
clared ‘unfair methods of competition in or affecting com-
merce, and unfair or deceptive acts of practices in or af-
fecting commerce’ to be unlawful (FTC 2006). Usually, the
severity of the practice matters a lot in enforcement of this
regulation. Because of the ex-post nature of the above guide-
lines, different practices of large digital marketplace players
have avoided legal actions on the basis of their potential ben-
efits toward consumers i.e., consumer welfare (Sallet 2018).
Note that advertising is not an unfair trade practice in and of
itself. However, the competitive nature and the potential of
distorting organic consumer behavior at scale is the biggest
concern in the context of interleaving advertisements within
search results in digital marketplaces. Marking a shift in the
policymakers’ approach, recently, Amazon has come under
intense scrutiny in the USA for its business practices ranging
from manufacturing private labels to preferentially treating
its preferred sellers (or itself) (Response 2019, 2020). Re-
cently, US FTC has also filed a law-suit against Amazon for
its unfair trade practices (FTC 2023) which mentions adver-
tisement on Amazon search among other things.
Specifically, the FTC lawsuit alleges Amazon’s advertis-
ing policies are in direct violation of Consumer Fraud Act
of New Jersey state (NJ 2022). This law prohibits adopting
any unconscionable commercial practice, deception in con-
nection with sale or advertisement. Amazon’s degradation
of quality of shopper-facing search results and nudging cus-
tomers to more expensive items, as per the FTC lawsuit, do
not comply with the said regulation.
Potential non-compliance on Amazon: The recent US
FTC law suit sheds some light on internal studies of Amazon
where they find the increased advertising revenue outweighs
the sales it loses from worsening the relevance and quality of
search results (FTC 2023). In other words, such practices are
profitable at the cost of consumer injury. Practices of inter-
leaving and even highlighting sponsored results at the cost of
organic results may result in substantial consumer harm by
degrading the overall consumer experience by nudging con-
sumers to irrelevant, costlier and even lower quality prod-
ucts, as we showed in the previous section. Such harms
do not even outweigh the potential exposure it may pro-
vide to less popular products and their sellers. Furthermore,
since the SERP interface and the ranking algorithm mediates
the interaction between consumers and shown products at a
massive scale, such degradation is arguably unavoidable by
consumers unless they are proactive and attentive.
India
Section 2(47) in Indian Consumer Protection Act also ad-
dresses adoption of any unfair method or deceptive practice
to be unlawful for the purpose of promoting the sale (GOI
2019). In 2023, Central Consumer Protection Authority fur-
ther provided a set of guidelines, especially in the context
of digital marketplaces, to prevent and regulate dark pat-
terns (GOI 2019). Dark pattern is defined in the said noti-
fication as, ‘any practices or deceptive design pattern using
user interface or user experience interactions on any plat-
form that is designed to mislead or trick users to do some-
thing they originally did not intend or want to do’. The set of
potential dark pattern also included disguised advertisement
and interface interference. Under the first point, the guide-

line prohibits the practice of posing, masking advertisements
as other types of contents blending with the rest of an inter-
face to trick consumers into clicking them. The second point
prohibits manipulating consumers in user interfaces by high-
lighting specific information to affect their desired action.
Potential non-compliance on Amazon: We believe the in-
terleaving of sponsored results among organic search result,
and especially putting them above even the top organic re-
sults may not be desirable under such guidelines. In par-
ticular, such practices of blending ads with other types of
(organic) results potentially constitutes a dark pattern (dis-
guised advertisements). These practices may materially dis-
tort a consumers’ decision making as many of them tend to
click top results (Rubin 2019).
The European Union
Article 5 of the Unfair Commercial Practices Directive of
the European Union defines an unfair commercial practice
as one which materially distorts or is likely to materially
distort the economic behavior with regard to the product of
average consumer whom it reaches. It further prohibits any
such commercial practices (EU 2021). Article 8 of the same
directive, further prohibits aggressive commercial practices
which can likely manipulate the transaction decisions of av-
erage consumers. Article 9 also prohibits exploitation of any
specific misfortune or circumstances to impair or influence
consumers’ decision with regard to the product.
Going one step further, the EU has recently come up with
a set of ex-ante regulations for digital platforms in the form
of Digital Services Act (DSA) (Release 2022) and Digital
Markets Act (DMA) (Commision 2022). The primary differ-
ence in these ex-ante regulations from the prior regulations
is here the rules and obligations are established before the
unfairness concerns arise. Therefore, all stakeholders have
to obey them once they come into force. Specifically, the
Article 25 of DSA prohibits online platforms from using de-
ceptive design choices in their interfaces which may distort
the end users’ ability to make a free and informed decision.
Potential non-compliance on Amazon: As we have shown
earlier, the advertisements in Amazon SERPs are being put
even before the first organic search result, which may ma-
terially distort/manipulate the consumers’ economic behav-
ior and transaction decisions especially toward the top spon-
sored results (e.g., non-purchase to purchase for top spon-
sored result and purchase to non-purchase for top organic
results). This concern is even more critical since prior sur-
veys show that almost half of the consumers are not able
to distinguish between organic and sponsored results on
Amazon (Graham 2019). Replacing top organic results with
sponsored ones may be argued as deceptive design as they
intend to exploit the cognitive and positional biases that con-
sumers may have while interacting with digital mediums.
Our position: Note that we donot argue that the practice of
advertising in general to be unfair. However, because of the
competitive nature of the ads on digital marketplaces the in-
advertent consequences of interleaving advertisements with
organic results need to be carefully thought through.
Concluding discussion
Summary: To our knowledge, this is the first work that tries
to understand the effects and implications of sponsored re-
sults on the quality of search results in digital marketplaces.
Our analyses of top sponsored results on Amazon digital
marketplace across four large digital marketplaces show that
they are not only low in relevance to the queries (as per Ama-
zon’s own ranking algorithm), but in most cases they are
costlier and lower quality products than the corresponding
organic results and thus degrading the overall result quality.
Amazon’s consumer-centric approach: While the analy-
ses paints a bad picture of Amazon’s sponsored product ad-
vertising policies, we must also acknowledge the different
guardrails that Amazon has put in place to ensure consumer
satisfaction. As per Amazon’s sponsored product advertis-
ing policy, if at any time a seller is not winning a product’s
buy-box, her advertisements will not show up on Amazon
SERP to consumers. At the same time, Amazon also ensures
very high standards for selection of buy-box winners. How-
ever, while buy-box competition is among competing sellers
for a single product, search ranking is a competition among
different sellers through different products. Hence, mere re-
striction to buy-box winners may not lead to advertisements
being beneficial to consumers.
Extending consumer-centric standards for selection and
provision of ads: Here are a few potential design choices
which can serve all important stakeholders fairly:
1. Separation of sponsored and organic results:One way
to resolve the issue and adhere to different commercial
laws is to separate out (i.e., stop complete interleaving
of) sponsored results from organic results.
2. Downgrade sponsored results:Another relaxed version
of the previous solution may be to slightly downgrade the
sponsored results. For example, instead of replacing the
top organic results, the sponsored results can come after
the top few organic results.
3. Guard rails of relevance and other features: Along
with some of these approaches, digital marketplaces
should also consider stricter relevance criteria to select
sponsored results, to prevent the deterioration of quality
of search results. This may be achieved by using some
constraints as to how far a sponsored result can be pro-
moted from its organic position; its price and quality, etc.
Adhering to such policies may resolve some of the unfair-
ness concerns of existing advertising practices on competi-
tive digital marketplaces, as well as bring in more competi-
tion and adherence to different fair market regulations.
Acknowledgements
This research is supported in part by a European Research
Council (ERC) Advanced Grant for the project “Founda-
tions for Fair Social Computing”, funded under the Euro-
pean Union’s Horizon 2020 Framework Programme (grant
agreement no. 789373), and by a grant from the Max Planck
Society through a Max Planck Partner Group at Indian Insti-
tute of Technology Kharagpur.

References
Ali, M.; Sapiezynski, P.; Bogen, M.; Korolova, A.; Mislove,
A.; and Rieke, A. 2019. Discrimination through Optimiza-
tion: How Facebook’s Ad Delivery Can Lead to Biased Out-
comes. PACM HCI (CSCW), 3.
Amazon. 2024. Sponsored Prod-
ucts Turn browsers into buyers.
https://advertising.amazon.com/solutions/products/sponsored-
products?
Angwin, J.; Larson, J.; Mattu, S.; and Kirchner, L. 2022.
Machine bias. In Ethics of data and analytics , 254–264.
Auerbach Publications.
Baeza-Yates, R. 2018. Bias on the web. ACM CACM, 61.
Biega, A. J.; Gummadi, K. P.; and Weikum, G. 2018. Equity
of attention: Amortizing individual fairness in rankings. In
ACM SIGIR.
Buolamwini, J.; and Gebru, T. 2018. Gender shades: Inter-
sectional accuracy disparities in commercial gender classifi-
cation. In Conference on fairness, accountability and trans-
parency, 77–91. PMLR.
Chen, L.; Mislove, A.; and Wilson, C. 2016. An empirical
analysis of algorithmic pricing on amazon marketplace. In
WWW.
Commision, E. 2022. Digital Markets Act (DMA).
https://eur-lex.europa.eu/eli/reg/2022/1925.
Connolly, B. 2024. Which Amazon Product Cate-
gories are the Most Popular & Profitable in 2024?
https://www.junglescout.com/resources/articles/amazon-
product-categories/.
Dash, A.; Chakraborty, A.; Ghosh, S.; Mukherjee, A.;
Frankenreiter, J.; Bechtold, S.; and Gummadi, K. P. 2024.
Antitrust, Amazon, and Algorithmic Auditing. arXiv
preprint arXiv:2403.18623.
Dash, A.; Chakraborty, A.; Ghosh, S.; Mukherjee, A.; and
Gummadi, K. P. 2021. When the Umpire is also a Player:
Bias in Private Label Product Recommendations on E-
commerce Marketplaces. In ACM FAccT.
Dash, A.; Chakraborty, A.; Ghosh, S.; Mukherjee, A.; and
Gummadi, K. P. 2022. Alexa, in you, I trust! Fairness and
Interpretability Issues in E-commerce Search through Smart
Speakers. In ACM Web Conference.
EU. 2021. Unfair Commercial Practices. https://eur-
lex.europa.eu/EN/legal-content/summary/unfair-
commercial-practices.html.
Fischer, A. 2024. How many reviews do I need for my prod-
ucts? https://www.powerreviews.com/how-many-product-
reviews/.
FTC. 2006. Federal Trade Commission Act.
https://www.ftc.gov/legal-library/browse/statutes/federal-
trade-commission-act.
FTC. 2023. FTC Sues Amazon for Illegally Main-
taining Monopoly Power. https://www.ftc.gov/news-
events/news/press-releases/2023/09/ftc-sues-amazon-
illegally-maintaining-monopoly-power.
GOI. 2019. The Consumer Protection.
https://consumeraffairs.nic.in/acts-and-rules/consumer-
protection.
Graham, M. 2019. Amazon is turning adver-
tising into its next huge business– here’s how.
https://www.cnbc.com/2019/07/17/how-amazon-
advertising-works.html.
Hardwick, J. 2021. Top Amazon Searches (2021).
https://ahrefs.com/blog/top-amazon-searches/.
Jaiswal, S.; Duggirala, K.; Dash, A.; and Mukherjee, A.
2022. Two-face: Adversarial audit of commercial face
recognition systems. In Proceedings of the International
AAAI Conference on Web and Social Media , volume 16,
381–392.
Juneja, P.; and Mitra, T. 2021. Auditing e-commerce plat-
forms for algorithmically curated vaccine misinformation.
In ACM SIGCHI.
Kulshrestha, J.; Eslami, M.; Messias, J.; Zafar, M. B.;
Ghosh, S.; Gummadi, K. P.; and Karahalios, K. 2017. Quan-
tifying search bias: Investigating sources of bias for political
searches in social media. In ACM CSCW.
Mehrotra, R.; Anderson, A.; Diaz, F.; Sharma, A.; Wallach,
H.; and Yilmaz, E. 2017. Auditing search engines for differ-
ential satisfaction across demographics. In WWW.
NJ. 2022. Consumer Fraud Act.
https://www.njconsumeraffairs.gov/statutes/consumer-
fraud-act.pdf.
Page, L.; Brin, S.; Motwani, R.; and Winograd, T. 1999. The
PageRank citation ranking: Bringing order to the web. Tech-
nical report, Stanford InfoLab.
Release, E. P. 2020. Antitrust: Commission sends Statement
of Objections to Amazon for the use of non-public indepen-
dent seller data and opens second investigation into its e-
commerce business practices. https://bit.ly/3h8jAIR.
Release, E. P. 2022. Digital Services Act: Council
and European Parliament provisional agreement for
making the internet a safer space for European citi-
zens. https://www.consilium.europa.eu/en/press/press-
releases/2022/04/23/digital-services-act-council-and-
european-parliament-reach-deal-on-a-safer-online-space/.
Response, A. 2019. Online Platforms and Mar-
ket Power, Part 2: Innovation and Entrepreneurship.
https://bit.ly/2VnSS7q.
Response, A. 2020. Hearing of the Subcommittee on An-
titrust, Commercial, and Administrative Law, Committee on
the Judiciary. https://bit.ly/3n9Um0k.
Robertson, R. E.; Jiang, S.; Joseph, K.; Friedland, L.; Lazer,
D.; and Wilson, C. 2018. Auditing partisan audience bias
within google search. PACM HCI (CSCW), 2.
Rubin, C. 2019. Cracking Amazon’s A9 Algo-
rithm: Increase Your Amazon Ranking to Sell More.
https://www.singlegrain.com/amazon/cracking-amazons-
a9-algorithm-increase-your-amazon-ranking-to-sell-more/.
Rubin, C. 2021. Cracking Amazon’s A9 Algo-
rithm: Increase Your Amazon Ranking to Sell More.

https://www.singlegrain.com/amazon/cracking-amazons-
a9-algorithm-increase-your-amazon-ranking-to-sell-more/.
Sallet, J. 2018. Competitive Edge: Protecting the “competi-
tive process”—the evolution of antitrust enforcement in the
United States. hhttps://equitablegrowth.org/competitive-
edge-protecting-the-competitive-process-the-evolution-of-
antitrust-enforcement-in-the-united-states/.
Singh, A.; and Joachims, T. 2018. Fairness of exposure in
rankings. In ACM SIGKDD.
Sorokina, D.; and Cantu-Paz, E. 2016. Amazon search: The
joy of ranking products. In ACM SIGIR.
Support, A. 2024. Sponsored Products.
https://advertising.amazon.com/help/GJUCNANNV3GQVXJZ.
Wilson, C.; Ghosh, A.; Jiang, S.; Mislove, A.; Baker, L.;
Szary, J.; Trindel, K.; and Polli, F. 2021. Building and au-
diting fair algorithms: A case study in candidate screening.
In ACM FAccT.
