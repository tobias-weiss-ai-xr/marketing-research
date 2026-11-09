---
title: 'DaDaDa: A Dataset for Data Pricing in Data Marketplaces'
url: https://arxiv.org/abs/2607.08785
category: ai-marketing
subcategory: measurement
date: 2026-06
venue: ''
authors:
- Qiheng Sun
- Hongwei Zhang
- Junxu Liu
- Xiaokai Mao
- Jinfei Liu
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.08785
pages: 14
chars: 71647
fetched_at: '2026-11-08T13:28:38+00:00'
kb_version: 1
---

# DaDaDa: A Dataset for Data Pricing in Data Marketplaces

[Experiment, Analysis, and Benchmark] DaDaDa: A
Dataset for Data Pricing in Data Marketplaces
Qiheng Sun 1,2, Hongwei Zhang 2, Junxu Liu 1, Xiaokai Mao 2, Jinfei Liu 2, Kui Ren 2, Haibo Hu 1
1The Hong Kong Polytechnic University, Hong Kong, China
2Zhejiang University, Hangzhou, China
{qiheng.sun, junxu.liu, haibo.hu}@polyu.edu.hk
{hongweizhang, xiaokaimao, jinfeiliu, kuiren}@zju.edu.cn
Abstract— High-quality data drives machine learning advances
across industries. Recognizing the value of data, data transactions
are increasingly common, giving rise to many data marketplaces,
e.g., A WS Marketplace, Databricks, and Datarade. However,
determining the appropriate prices for data products remains
a signiﬁcant challenge due to the unique properties of data
products. Traditional pricing methods in economics can be
categorized into the cost approach, the income approach, and
the sales comparison approach. The cost approach fails in data
pricing due to near-zero marginal cost from data replication,
and the income approach fails due to inherently unpredictable
data revenue. The sales comparison approach remains viable,
yet its application is hindered by the absence of standardized
pricing benchmarks for data products across marketplaces. To
address this challenge, we introduce DaDaDa, the ﬁrst dataset
for data product pricing, containing metadata for 16,147 data
products from 9 major data marketplaces worldwide. DaDaDa
enables the training of pricing models, thereby establishing price
benchmarks for new data products. In addition, DaDaDa can be
utilized for other important tasks in data markets, such as data
product classiﬁcation and retrieval. Experiments and a retrieval
prototype demonstrate the effectiveness of DaDaDa for pricing,
classiﬁcation, and retrieval of data products. The dataset and
code are available at https://github.com/ZJU-DIVER/DaDaDa.
Index Terms—Data Pricing; Data Marketplaces
I. I NTRODUCTION
The immense value created by data-driven machine learning
models stems from accessible, diverse, and well-structured
data [ 32]. However, publicly available data are running out,
as noted in recent discussions of AI data scarcity [ 47]. More-
over, such data often lack domain speciﬁcity and structural
consistency. In contrast, private data sources not only retain
vast amounts of unused data but also provide curated, task-
speciﬁc datasets. This gap between the need for high-quality
data and the limitations of public sources drives the growth
of private data transactions [ 43], giving rise to dedicated
marketplaces such as AWS Marketplace [ 2], Databricks [ 8],
and Datarade [ 10]. These marketplaces provide a convenient
avenue for showcasing data products and facilitate connections
between data sellers and buyers.
A critical function of marketplaces is enabling pricing for
products, which determines transaction viability and market
liquidity [56]. There are three commonly used pricing methods:
(1) the cost approach, (2) the income approach, and (3) the
sales comparison approach [ 30], [38], [41]. The cost approach
sets the price of a product by assessing the cost of replacing or
reproducing it. Evaluating the cost of data products is difﬁcult
due to the fact that they can be replicated and distributed at
almost zero cost. The income approach determines the price
of a product based on the income that it is expected to bring.
Predicting the income of data products is challenging because
they can generate different revenues across use cases and be
sold multiple times to distinct customers. Due to inherent
issues with these two methods in the context of data products,
the sales comparison approach is more applicable and widely
adopted in data markets. The sales comparison approach
utilizes existing pricing information of similar products to
estimate the price of the commodity to be sold. This reduces
information asymmetry, fosters mutual acceptance between
buyers and sellers, and ultimately facilitates transaction com-
pletion in data markets.
With the rapid development of data marketplaces, the sales
comparison approach holds signiﬁcant potential for proper
data product pricing by leveraging aggregated pricing signals
across platforms. However, its practical implementation faces a
critical barrier: comparing and evaluating data products across
marketplaces is challenging due to different taxonomies and
inconsistent metadata granularity. This complexity is further
compounded by the limited capacity of pricing agents to
conduct exhaustive cross-marketplace comparisons, as the
cognitive burden and time required to manually align dis-
parate product speciﬁcations often exceed practical constraints.
This structural fragmentation limits the applicability of the
sales comparison approach despite its theoretical advantages,
thereby constraining market efﬁciency through suboptimal
pricing decisions and reduced transaction volumes. Conse-
quently, enabling automated cross-marketplace price bench-
marking represents a pivotal challenge for realizing the full
potential of data markets.
To enhance the applicability of the sales comparison ap-
proach in data markets, we propose DaDaDa (A Dataset for
Data Pricing in Data Marketplaces), containing metadata for
16,147 data products from 9 major data marketplaces and
providing price references for pricing decisions. We investigate
60 data marketplaces and carefully select 9 of them based
on speciﬁc criteria, including the accessibility of their data
product catalogs, the diversity of data products they offer,
and the comprehensiveness of the metadata they provide.
This careful selection process ensures that DaDaDa offers a
arXiv:2607.08785v1  [cs.LG]  13 Jun 2026

diverse and representative sample of a broad data marketplace
ecosystem. To create DaDaDa, we use advanced web crawling
techniques to extract detailed metadata for each data product,
then create ﬁelds such as title, description, provider, price,
volume, size, and category. Following metadata scraping, we
conduct thorough data preprocessing to unify various metadata
ﬁelds into a consistent format, making it easy to analyze and
use for various applications. The resulting DaDaDa dataset
serves as a uniﬁed, analyzable benchmark, making the system-
atic research and application of the sales comparison approach
for data product pricing feasible.
We conduct experiments to demonstrate the effectiveness of
using DaDaDa for essential tasks in data markets.
• Data product pricing. This task involves pricing data prod-
ucts based on their metadata. We train several regression
models on DaDaDa to predict product prices, providing
empirical baselines for future research on automated data
pricing.
• Data product classiﬁcation. This task involves classifying
data products into predeﬁned categories. We ﬁne-tune pre-
trained multilingual models using product titles and descrip-
tions, showing that DaDaDa supports semantic analysis and
category prediction in data marketplaces.
• Data product retrieval. This task involves retrieving relevant
data products from a large collection of data products in
response to user queries. We use Elasticsearch [ 12] to
develop a search engine within DaDaDa, allowing users to
quickly ﬁnd interesting data products along with correspond-
ing pricing information.
The rest of the paper is organized as follows. We ﬁrst
review related work on data product pricing in Section II.
Section III provides an overview of the DaDaDa dataset. The
dataset construction pipeline is detailed in Section IV. Sec-
tion V explores the various applications of DaDaDa. Finally,
we conclude this paper and discuss the limitations and future
work in Section VII.
II. R ELATED WORK
A. Theoretical Data Pricing Mechanisms
Existing theoretical studies on data pricing can be broadly
organized around three types of mechanisms. The ﬁrst line
studies how to price data access and query answers under
formal economic constraints. Query-based pricing work es-
tablishes arbitrage-free and discount-free prices for database
queries, and further develops scalable query-pricing systems
and revenue-maximization models [ 49], [ 39], [ 33]. Closely
related, Li et al. [ 51] develop a theoretical framework for
pricing noisy query responses with compensation mechanisms
based on privacy loss.
A second line designs market mechanisms for acquiring,
selling, or allocating data when participants have private infor-
mation. Price-quantity mechanisms account for buyers’ private
valuations of data subsets [ 55], while auction- and Shapley-
value-based marketplace designs aim to elicit truthful bids and
ensure fair revenue distribution among data owners [ 26]. Peer-
prediction mechanisms further support truthful data acquisition
when no test dataset is available [ 36]. Related procurement
work considers scenarios where individuals incur privacy costs,
using truthful auctions under differential privacy to purchase
private data subject to budget or accuracy constraints [ 45].
A third line extends pricing theory from raw data to
machine-learning artifacts and privacy-aware marketplaces.
Model-pricing frameworks prevent arbitrage while balancing
seller revenue and buyer affordability [ 34], and end-to-end
model marketplaces incorporate differential privacy into com-
pensation and pricing functions to support fairness, privacy
preservation, and revenue maximization [ 52]. Despite their
theoretical rigor, these approaches share a critical limitation:
they lack empirical validation using real-world pricing data
from operational data marketplaces.
B. Empirical and Commercial Studies
Complementing theoretical work, empirical studies examine
commercial data marketplaces from an empirical perspec-
tive. Azcoitia et al. [ 29] conduct a comprehensive survey
of commercial data trading entities, analyzing data types,
business models, and underlying technologies. In subsequent
work, they investigate speciﬁc features that inﬂuence data
product pricing [ 28]. Hanspach et al. [ 46] and Wieting and
Sapi [ 58] conduct empirical analyses of pricing on major e-
commerce platforms, analyzing pricing data from thousands of
products to understand automated pricing behavior in digital
marketplaces. Azcoitia et al. [ 27] analyze price distributions
and price-driving features, highlighting both the feasibility and
the challenges of cross-marketplace comparisons. However,
these studies primarily focus on descriptive analysis rather than
providing structured datasets for algorithmic development and
benchmarking.
In summary, existing research suffers from a critical discon-
nect in that theoretical pricing mechanisms remain unvalidated
due to the absence of real-world pricing benchmarks, while
empirical marketplace studies lack structured datasets needed
for algorithmic development.
III. D ATASET OVERVIEW
In this section, we present an overview of DaDaDa. A
detailed description of the construction pipeline is provided
in Section IV.
Overall, DaDaDa distinguishes itself from existing bench-
mark datasets through three key contributions. (1) Bridging
the Gap. It is the ﬁrst real-world dataset for data product
pricing, enabling both empirical validation of pricing theo-
ries and the development of practical marketplace algorithms.
(2) Extensive Coverage. It provides detailed metadata for
16,147 data products sourced from 9 leading data marketplaces
worldwide, facilitating in-depth analysis of the commercial
data landscape. (see Section IV -Afor the full list). (3) Stan-
dardized Metadata. Each data product is described using a
standardized metadata template, curated through web crawling,
scraping, and thorough preprocessing to capture a comprehen-
sive set of relevant attributes. The complete set of metadata
attributes is detailed below.

RET AIL
FINANCIAL
TELECOMM
MEDIA
HEAL THCARE
PUBLIC SECTOR
MANUF ACTURING
RESOURCES
ENVIRONMENT AL
A UTOMOTIVE
OTHER
GAMING
CA TEGOR Y
0
10
20
30
40
PERCENT AGE
35.3
22.8
7.3
7.07
6.71 6.52
4.99
3.41
2.72
2.39
0.66
0.05
10
20
30
V alue → Color
Fig. 1: Percentage of each category in category.
FREE
NEGOTIA TION
SUBSCRIPTION
ONE-OFF
USAGE-BASED
PRICE MODE
0
10
20
30
40
50
PERCENT AGE
41.5
27.9
17.6
8.97
3.88
10
20
30
40
V alue → Color
Fig. 2: Percentage of each pricing mode in price_mode.
• Title. The title of the data product.
• Platform. The marketplace name hosting the data prod-
uct.
• Provider. The name of the data provider as listed on the
data marketplace. The released table contains 1,991 named
data providers. Among them, “Techsalerator” is the leading
provider, offering a total of 644 data products, making it the
supplier with the highest volume of offerings on the market.
For products whose source platform does not disclose the
provider identity, we preserve an empty provider value rather
than imputing a potentially incorrect name.
• Description. The detailed description of the data prod-
uct.
• Volume. The number of records.
• Size. The data size (in Byte) provided by the data
product.
• Dimension. The number of data features.
• Coverage. The countries covered by the data product.
• Update_frequency. The frequency between data product
updates as announced by the seller, such as “monthly”, “daily”,
and “real-time”. Most data products adopt “no-update” and
“daily”.
• Data_sample. The ﬁlename of the data sample if avail-
able. We download and store the data sample of data products
in an additional folder.
• Category. The original category of data product may vary
across different data marketplaces, each with its own way of
categorization. We align the data categories from other market-
places with the AWS Marketplace categories through manual
labeling. As shown in Figure 1, Retail (Retail, Location, and
Marketing Data) and Financial (Financial Services Data) have
the highest proportions.
• Price_mode. The pricing mode of the data product. There
are ﬁve pricing modes: (1) negotiation mode where data buyers
need to negotiate the price with data providers, (2) free mode
where the data is provided at no cost, (3) subscription mode
where data buyers are charged a recurring fee on a monthly or
annual basis, (4) one-off mode where data buyers pay a one-
time fee to access the data permanently, and (5) usage-based
mode where data buyers are charged based on the amount of
data they consume, such as the volume of data downloaded
or the number of API calls. As shown in Figure 2, most data
products in the data marketplaces are either free or priced
through negotiation. A smaller proportion (subscription, one-
off, or usage-based) has clear prices.
• Price. We use USD ($) as the currency unit. If the
pricing mode is free, the price is set to 0. Since data products
with negotiation mode do not have a clear price, we exclude
them from the data product pricing task in Section V -A. As a
result, negotiation-mode data products are assigned a price of
0. If the pricing mode is subscription, the price represents the
subscription cost for 12 months. If the pricing mode is usage-
based, the price reﬂects the cost for a single usage. These
two standardizations facilitate price comparisons within the
same mode. We do not directly compare data products across
different modes, as the price mode is the most signiﬁcant
factor inﬂuencing the price of a data product when training
the pricing model.
• Url. The web address of the detail page of the data
product.
Dataset Statistics and Release. The released dataset contains
16,147 data products described by 14 standardized metadata
ﬁelds. The products come from nine marketplaces with dif-
ferent geographic focuses and platform designs: Datarade
(4,396 products), AWS Data Exchange (3,702), Snowﬂake
(2,585), Databricks (2,004), Zhejiang Big Data Exchange
(838), Canton Data Exchange (792), Beijing International
Data Exchange (714), Guiyang Global Big Data Exchange
(669), and Shanghai Data Exchange (447). This coverage
is important for pricing research because it includes both
international cloud marketplaces and regional data exchanges,
whose metadata conventions and pricing disclosure practices
differ substantially. In addition to the ﬁnal table, we release the
raw crawled ﬁles, intermediate preprocessed ﬁles, preprocess-
ing scripts, crawler implementations, downstream experiment
code, and 255 data product samples when samples are publicly
available from the source platforms. These artifacts allow users
to inspect how each product moves from raw marketplace
metadata to the uniﬁed DaDaDa schema.
Price Coverage. Some products provide explicit nonzero
prices under subscription, one-off, or usage-based modes;
these products constitute the labeled subset used in the data
product pricing task. The remaining products are free or
negotiation-based. We retain them in the complete dataset
because they are still useful for studying marketplace com-
position, category classiﬁcation, retrieval, and pricing-mode
prediction. This design follows the practical structure of cur-
rent data marketplaces: many sellers intentionally hide exact
prices and require buyers to negotiate, while buyers still need

comparable metadata to identify alternatives and understand
market positioning. By separating price_mode from price,
DaDaDa supports both direct price regression on products with
explicit prices and broader analysis of disclosure patterns
across platforms.
Marketplace Coverage and Benchmark Scope. Table I
summarizes the platform-level coverage of DaDaDa, including
product counts, pricing-mode composition, and public sample
availability. The purpose of this proﬁling table is to make
the released snapshot auditable: users can identify which
marketplaces contribute products to the uniﬁed schema and
choose task-speciﬁc subsets according to their experimental
needs.
This platform-level proﬁle documents the scope of the
released snapshot rather than deﬁning a single downstream
task. Since public data marketplaces organize listings using
different pricing and disclosure conventions, the table helps
users understand the composition of DaDaDa and select task-
speciﬁc subsets for pricing, classiﬁcation, retrieval, or mar-
ketplace analysis. The same principle applies to structured
metadata. Attributes such as volume, size, and dimension
are used when they are reliably disclosed, while textual ﬁelds
such as title and description provide a consistent se-
mantic representation across platforms. This design preserves
broad marketplace coverage and allows downstream models
to combine textual and structured signals according to the
requirements of each task.
Metadata Sparsity. The dataset also preserves the in-
completeness of real marketplace metadata. Fields such as
title, description, platform, category, price_mode,
and url are complete after preprocessing, while numerical
ﬁelds such as volume, size, and dimension are disclosed
unevenly across platforms. Instead of discarding products from
metadata-poor marketplaces, we use explicit default values
when a ﬁeld cannot be reliably inferred from the product
page. This choice makes the benchmark more representative
of real data marketplace search and pricing conditions, where
buyers often rely on textual descriptions and partial structured
metadata. It also explains why the textual representation of
title and description plays a major role in the pricing
experiments in Section V -A.
Benchmark Implications. Structured numerical attributes in
data marketplaces are not disclosed as consistently as textual
ﬁelds. When ﬁelds such as volume, size, and dimension
cannot be reliably extracted from the original product pages,
we preserve explicit default values rather than inventing prod-
uct properties that sellers do not publish. The implication is
that real data-product metadata is largely text-centric: title
and description are the most consistently available high-
content ﬁelds across marketplaces, while numerical attributes
are useful complementary signals only when sellers or plat-
forms expose them reliably.
This observation directly shapes the benchmark design
of DaDaDa. First, the pricing task should combine semantic
representations with structured features instead of relying
on purely tabular metadata, because a structured-only model
would either discard many products or depend heavily on
artiﬁcial imputation. Second, the classiﬁcation task is naturally
formulated as a multilingual text understanding problem, since
category evidence is primarily expressed in product titles and
descriptions. Third, the retrieval task should combine full-
text search with optional structured ﬁlters: buyers can search
semantically over all products, while using price, coverage,
update frequency, size, volume, or dimension ﬁlters only when
those ﬁelds are available. The SHAP analysis in Section V -A
further supports this design choice: description is the most
inﬂuential feature group across subscription, one-off, and
usage-based pricing modes, while structured attributes such
as coverage, update frequency, and dimension provide mode-
speciﬁc signals when available.
Survey
Discarded
9 Target Marketplaces
Elimination
Stage 2: Metadata
Scraping
Stage 3: Data
Preprocessing
DaDaDa
…
AWS Datarade Snowflake
Results of Target Marketplaces
Databricks
Stage 1: Data Marketplace Selection
60 Candidates
…
…
…
Fig. 3: Overview of the data collection pipeline. First, we iden-
tify and select 9 major data marketplaces that meet our criteria.
Next, we use web scraping techniques to extract metadata
from the selected data marketplaces. Finally, we carry out data
preprocessing, removing errors or inconsistencies, combining
data from different sources, and converting the data into a
uniﬁed format for analysis.
IV. C ONSTRUCTION PIPELINE
We develop a comprehensive data collection pipeline to
gather and organize data from various data marketplaces. As
shown in Figure 3, this pipeline consists of three main stages:
(1) data marketplace selection, (2) metadata scraping, and (3)
data preprocessing. The details of each stage are described as
follows.
A. Data Marketplace Selection
Ensuring that raw data sources satisfy rigorous quality and
robustness standards is fundamental to developing reliable
pricing benchmarks. To this end, we ﬁrst identify candidate
data marketplaces through a selection process guided by three
criteria:
1) Data Accessibility. Data marketplaces must provide open
access to their data product catalogs and permit data
extraction through web crawling techniques.

TABLE I: Platform-level proﬁling of DaDaDa. “Explicit” denotes products with explicit nonzero prices. “Free”, “Neg.”, “Sub.”,
“One-off”, and “Usage” report the numbers of products under the free, negotiation, subscription, one-off, and usage-based
pricing modes, respectively. “Public samples” denotes publicly available data sample ﬁles downloaded from product pages.
Marketplace Products Explicit Explicit (%) Free Neg. Sub. One-off Usage Public samples
Datarade 4,396 1,986 45.2 0 2,410 1,082 695 209 255
AWS Data Exchange 3,702 1,606 43.4 2,096 0 1,592 0 14 0
Snowﬂake 2,585 237 9.2 2,348 0 172 12 53 0
Databricks 2,004 0 0.0 1,610 394 0 0 0 0
Zhejiang Big Data Exchange 838 833 99.4 0 5 1 735 97 0
Canton Data Exchange 792 14 1.8 0 778 7 2 5 0
Beijing International Data Exchange 714 202 28.3 510 0 0 6 198 0
Guiyang Global Big Data Exchange 669 51 7.6 142 476 0 0 51 0
Shanghai Data Exchange 447 0 0.0 0 447 0 0 0 0
All 16,147 4,929 30.5 6,706 4,510 2,854 1,450 627 255
2) Product V ariety. Data marketplaces must encompass a
sufﬁcient range of product categories to ensure diversity.
In our framework, we adopt a practical threshold of eight
categories and manually assess coverage using AWS Mar-
ketplace classiﬁcation criteria as the benchmark.
3) Metadata Comprehensiveness. Data marketplaces must in-
clude a substantial portion of the essential metadata ﬁelds
associated with each data product. Speciﬁcally, we require
that each marketplace cover at least 70% of the metadata
attributes listed in Section III.
Selection Rationale. The three criteria balance coverage,
diversity, and reproducibility. Marketplace size alone is insufﬁ-
cient: a large catalog may be concentrated in a narrow domain
or expose minimal metadata, while a smaller marketplace can
still contribute structured product pages, multiple categories,
and stable public listings. We therefore ﬁrst require crawlable
catalogs and then assess whether each candidate adds diverse
and comparable metadata to the uniﬁed schema. This also
prevents the benchmark from being dominated by a few
high-volume but narrow catalogs. This protocol helps DaDaDa
represent a broad marketplace ecosystem while remaining
reproducible from public sources.
Our selection process starts with an extensive survey of
data marketplaces worldwide, identifying 60 initial candidates
(see Table II for more details). Candidates that do not meet
the ﬁrst criterion are eliminated in the ﬁrst stage. For exam-
ple, Azure [ 3] is removed because it requires payments to
access data products. This ﬁltering step yields a shortlist of
20 accessible candidates, as shown in Table III. Next, we
evaluate these candidates against the second and third criteria,
gathering information regarding the number of data products
and categories available in each marketplace. Our analysis
reveals that while some marketplaces offer a large volume of
data products, they are often concentrated in speciﬁc domains.
For example, our manual inspection of representative product
samples shows that Advaneo specializes in IoT data and Carto
focuses on spatial data. Additionally, data marketplaces like
Western China Data Exchange [ 22] and Google Cloud [ 13]
provide only limited product information, typically restricted
to titles and brief descriptions. After removing these cases
TABLE II: Summary of the 60 initial data marketplace candi-
dates.
Marketplace URL Accessibility
Advaneo https://www.advaneo-datamarketplace.de/database/en/ 8
Agdatahub https://agdatahub.eu/en/ 8
Aircloak https://aircloak.com/ 8
AMO https://www.amo.foundation/ 8
AWS Marketplace https://aws.amazon.com/marketplace/ 4
Azure https://azure.microsoft.com/en-us/products/open-datasets/ 8
BattleFin https://www.battleﬁn.com/ 8
Beibu Gulf Data Exchange https://www.bbgdex.com/ 4
Beijing International Data Exchange https://www.bjidex.com 4
BurstIQ https://burstiq.com/ 8
Canton Data Exchange https://www.cantonde.com 4
Carto https://carto.com/ 4
Caruso https://www.caruso-dataplace.com/ 8
CleverData https://1dmc.io/ 8
Cognite https://www.cognite.com/en/ 8
Crunchbase https://www.crunchbase.com/ 8
Data Intelligence Hub https://dih.telekom.com/en/ 8
Databricks https://marketplace.databricks.com/ 4
Databroker https://www.databroker.global/ 4
Dataeum https://www.dataeum.io/ 8
Datarade https://datarade.ai/ 4
Datatang https://www.datatang.com/ 4
Datawallet https://www.datawallet.com/ 8
Datum https://arxiv.org/pdf/2201.04561 8
Dawex https://www.dawex.com/en/data-exchange-technology/ 8
Decentr https://decentr.net/ 8
GeoDB https://geodb.com/en/ 8
Google Cloud https://console.cloud.google.com/marketplace 4
Guiyang Global Big Data Exchange https://www.gzdex.com.cn 4
Handshakes https://www.handshakes.com.sg/data 8
Health V erity https://healthverity.com/ 8
HERE https://www.here.com/ 8
IOTA https://www.iota.org/ 8
JDEX https://www.jdex.jp/ 8
Knoema https://knoema.com/ 4
LESG https://www.lseg.com/en/data-analytics 8
Liveramp https://liveramp.com/ 8
LonGenesis https://longenesis.com/ 8
Lotame https://www.lotame.com/ 8
Madana https://www.madana.io/products.html 8
Mobilithek https://mobilithek.info/ 4
Mydex https://mydex.org/ 8
Nasdaq Data Link https://data.nasdaq.com/ 4
Northern China Data Exchange https://www.datadmz.com/ 4
Salesforce https://www.salesforce.com/products/ 8
Shanghai Data Exchange https://dtxp.chinadep.com 4
Shenzhen Data Exchange https://www.szdex.com 4
Space Data Marketplace https://www.space-data-marketplace.eu/en/onboard/ 8
Streamr https://streamr.network/ 8
Terbine https://terbine.com/ 8
The Adex https://theadex.com/ 8
TheTradeDesk https://www.thetradedesk.com/us/ 8
Urgently https://www.geturgently.com/ 8
V eracity https://www.veracity.com/ 4
V etri https://vetri.global/ 8
Weople https://weople.space/en/ 8
Western China Data Exchange https://www.westdex.com.cn 4
Xignite https://www.xignite.com/ 8
Zenome https://zenome.io/ 8
Zhejiang Big Data Exchange https://ditm.zjdex.com 4
from consideration, we ultimately identify 9 candidates, which
are listed in the upper section of Table III.
B. Metadata Scraping
After identifying the candidate data marketplaces, we apply
web scraping techniques to extract the required metadata.

TABLE III: Summary of 20 accessible data marketplaces. The
columns (from left to right) report the total counts of data
products and product categories, followed by indicators of
whether the marketplace meets the second and third criteria.
Marketplace Products Categories V ariety Comprehensiveness
AWS Marketplace [ 2] 3,702 12 4 4
Beijing International Data Exchange [ 5] 714 22 4 4
Canton Data Exchange [ 6] 792 24 4 4
Datarade [ 10] 4,396 25 4 4
Databricks [ 8] 2,004 20 4 4
Guiyang Global Big Data Exchange [ 14] 669 19 4 4
Snowﬂake [ 20] 2,585 25 4 4
Shanghai Data Exchange [ 18] 447 6 4 4
Zhejiang Big Data Exchange [ 24] 838 10 4 4
Advaneo [ 1] 2,376,178 15 8 4
Beibu Gulf Data Exchange [ 4] 1,016 19 4 8
Carto [ 7] 11,800 10 8 4
Databroker [ 9] 129 10 8 8
Datatang [ 11] 465 7 8 8
Google Cloud [ 13] 235 30 4 8
Mobilithek [ 15] 8,015 25 8 4
Nasdaq Data Link [ 16] 750 9 8 8
Shenzhen Data Exchange [ 19] 235 13 8 8
V eracity [21] 186 29 8 4
Western China Data Exchange [ 22] 3,135 10 4 8
This process is non-trivial due to heterogeneity in platform
design. Speciﬁcally, some websites provide complete metadata
for all products in a single request, whereas others restrict
access to product-level detail pages, necessitating item-by-item
extraction.
For the former case, we save the returned results. For the
latter, we use the Selenium library [ 17] to scrape metadata
for data products that are useful for data pricing. Besides, we
save the URL of the data product detail page for potential
applications. We create XPath and CSS selector rules to pre-
cisely target and extract information by analyzing the HTML
structure of the target website. In Figure 4, we illustrate the
sources from which each metadata ﬁeld is scraped. When
dealing with textual ﬁelds such as title and description,
we simply extract the text from the corresponding HTML
elements. As for the data sample, we extract the title and rows
of the sample, save this data to a ﬁle, and then store the path to
the saved ﬁle in the data_sample ﬁeld of the corresponding
data product. Once metadata is successfully extracted, it is
saved in CSV format, allowing easy inspection and simplifying
subsequent analysis. To avoid potential service disruptions,
requests are scheduled at regular intervals, typically every
three minutes. Furthermore, our crawler strictly adheres to
each platform’s directives and terms of service to ensure
ethical and legally compliant data collection practices.
C. Data Preprocessing
Finally, the scraped metadata is preprocessed through two
primary procedures: data cleaning and data integration.
Data Cleaning. We begin by cleaning raw metadata through
three primary operations: removing duplicate items, rectifying
errors, and imputing missing values. These steps lay the foun-
dation for subsequent preprocessing while preserving dataset
integrity.
1. Removing duplicate items. Data crawling may result in
the retrieval of duplicate data products. To ensure dataset
uniqueness, we detect duplicates by comparing the title
and provider ﬁelds. If two data products have identical

Fig. 4: Scraping example of Datarade.
ﬁelds, they are considered duplicates, and the redundant
entries are removed.
2. Rectifying errors. During the crawling process, non-UTF-
8 characters may be retrieved, leading to errors when
reading ﬁles containing such characters. We use a script
to detect and automatically remove non-UTF-8 characters
from the data.
3. Imputing missing values. Some critical ﬁelds like
coverage and size are often not explicitly provided on
many data marketplaces and are only mentioned in the
description. To address these missing ﬁelds, we use
manual annotation. Speciﬁcally, we read the description
ﬁeld to extract relevant information to ﬁll in the missing
ﬁelds. If no relevant information is available, we use default
values.
Data Integration. The objective of data integration is to merge
the cleaned metadata from diverse data marketplaces into a

standardized schema, thereby facilitating subsequent analysis
and application deployment. Given the varying granularity
of metadata, we ﬁrst deﬁne a comprehensive superset that
encompasses all potentially relevant attributes across data
products. During integration, it is essential to account for
each attribute’s characteristics. Attributes such as title and
provider are independent and can be merged directly with-
out any issues. However, when it comes to attributes like
category, combining them directly is problematic due to
the lack of a consistent pattern across different platforms.
As shown in Table III, every data marketplace has its own
way of classifying data products. For example, AWS Mar-
ketplace [ 2] has 12 general categories, while Datarade [ 10]
has 25 general categories and over 560 detailed classiﬁcations.
Different classiﬁcation standards increase the difﬁculty of
ﬁnding similar data products across marketplaces and may
result in the omission of some data products. To solve this
problem, we manually map the diverse categorizations from
various platforms onto the taxonomy of AWS Marketplace
[2], ensuring consistency and creating a uniﬁed pattern to
avoid the confusion that can result from a direct combination.
The AWS Marketplace classiﬁcation system covers a wide
range of industries and application areas, ensuring that most
data products can be categorized. Additionally, as a well-
established data marketplace, its classiﬁcation system is widely
recognized and used by a broad user base. Therefore, we
choose it as our benchmark.
Besides, most of the data products in the data marketplaces
are denominated in USD ($) and RMB (CN¥), with smaller
amounts in EUR ( C), GBP (£), and JPY (JP¥). To maintain
consistency, we convert the other currencies to USD ($) using
the Y early Average Currency Exchange Rates [ 23]. Such inte-
gration eliminates redundancy and resolves conﬂicts, leading
to a more coherent dataset.
Metadata Validation. After integration, we perform con-
sistency checks to reduce avoidable noise before releasing
the dataset. First, we verify schema consistency by ensuring
that every marketplace-speciﬁc ﬁle can be projected into the
same set of standardized attributes. Second, we normalize
categorical values for price_mode and update_frequency;
for example, platform-speciﬁc phrases such as monthly billing,
yearly billing, real-time updates, and on-demand updates are
converted into a ﬁxed vocabulary. Third, we validate numerical
attributes by converting storage units to bytes, normalizing
subscription prices to a 12-month cost, converting usage-based
prices to per-use costs when the unit is disclosed, and checking
that non-free products with explicit prices have positive values.
Finally, for geographic coverage, we convert country abbrevi-
ations to country names and keep multi-country coverage as
a list, allowing both human inspection and machine-readable
ﬁltering.
We deliberately separate automatic normalization from man-
ual annotation. Fields that can be parsed deterministically,
such as currency conversion and many update-frequency ex-
pressions, are handled by scripts. Fields that require semantic
judgment, such as aligning marketplace-speciﬁc categories to
the AWS taxonomy or extracting missing coverage information
from long descriptions, are manually reviewed. This separation
makes the construction process auditable: users can reproduce
the deterministic steps from the released scripts and inspect
the curated ﬁelds in the preprocessed ﬁles. Such transparency
is particularly important for a pricing benchmark, since small
changes in price modes, currency conversion, or category
alignment can affect both downstream model performance and
the interpretation of price benchmarks.
V. A PPLICATIONS
In this section, we show that DaDaDa can be used for
multiple downstream tasks, including data product pricing
(Section V -A), data product classiﬁcation (Section V -B), and
data product retrieval (Section V -C). We use a server with an
NVIDIA A100 GPU (80GB) and 160 Intel(R) Xeon(R) Plat-
inum 8383C CPU @ 2.70GHz for all empirical experiments
in this manuscript. The operating system is Ubuntu 20.04.6.
A. Data Product Pricing
DaDaDa collects important metadata and pricing information
for data products, which can greatly assist in making pricing
decisions. To validate the effectiveness of DaDaDa, we use it to
train models and evaluate pricing performance. Figure 5 shows
a histogram and the corresponding CDF of data product prices
using different pricing modes. We can observe that usage-
based prices are mostly concentrated between $0.01 and $100,
one-off prices are primarily between $10 and $10,000, and
subscription prices are mainly between $100 and $100,000.
The prices for usage-based data are generally associated with
API-type data, which is typically priced per use, resulting in
lower overall prices. One-off data usually consists of static
datasets, while subscription data often includes live data that is
periodically updated with the latest information. This dynamic
nature of subscription data makes it more valuable compared
to static data, which is reﬂected in its higher overall price.
Benchmark Protocol. We formulate data product pricing
as a supervised listed-price regression task over products
with explicit nonzero prices. The input consists of stan-
dardized product metadata, including semantic ﬁelds ( title
and description), categorical ﬁelds ( category, coverage,
update_frequency, and price_mode), and numerical ﬁelds
(volume, size, and dimension) when available. The pre-
diction target is the normalized USD price after applying
the mode-speciﬁc standardization in Section III. Free and
negotiation-based products are excluded from this supervised
regression task because their price values are set to zero
by construction and do not represent observed listed prices.
Including them would mix price regression with pricing-mode
prediction and substantially change the task deﬁnition.
We predict log(price + 1) rather than the raw price
because listed data prices span several orders of magnitude
across subscription, one-off, and usage-based modes. The log
transformation reduces the dominance of extremely expensive
products and makes errors more comparable across price

10 2
 100 102 104 106
Price $(USD)
25
50
100
200
500Number of data products
0.0
0.2
0.4
0.6
0.8
1.0
CDF
subscription
one-off
usage-based
CDF subscription
CDF one-off
CDF usaged-based
Fig. 5: Histogram and CDF (Cumulative Distribution Function)
of the prices in three pricing modes for data products.
ranges. To avoid information leakage, ﬁelds that directly
identify a product page, marketplace, or seller—including url,
platform, provider, and data_sample—are removed before
model training. Raw title and description strings are also
removed after conversion into embeddings. We evaluate all
pricing models using shufﬂed 5-fold cross-validation with a
ﬁxed random seed and report the average R2, MAE, MSE,
and standard deviation across folds. This protocol makes the
task a metadata-based benchmark for estimating public listed
prices rather than a memorization task over marketplaces or
providers.
We preprocess the data to ensure it meets the format
requirements of machine learning models. The preprocessing
procedure includes the following steps.
• Feature extraction. We extract features utilizing the ﬁne-
tuned XLM-RoBERTa-Large model [ 37]. Speciﬁcally, the
model encodes description and title, obtaining word
embeddings from the intermediate layer (12th layer). These
high-dimensional word embeddings are then reduced in size
using Principal Component Analysis (PCA) [ 54] to enhance
computational efﬁciency and decrease feature count. We ﬁnd
the minimum number of principal components required to
achieve a 95% cumulative explained variance ratio, reducing
the original 1024-dimensional word embeddings to 223
dimensions.
• Categorical and numerical feature processing. For the cate-
gorical features such as category, update_frequency, and
price_mode, we employ One-Hot Encoding to allow the
model to interpret these data points accurately. Numerical
features, including size, dimension, and volume, are stan-
dardized to ensure all data points are on a uniﬁed scale,
thus preventing discrepancies in feature magnitudes from
affecting the performance of the model.
• Price processing. Considering the wide range of the target
variable price, we apply a log transformation to stabilize the
values and improve the robustness of the training process.
This comprehensive preprocessing ensures that the data is
well-prepared for the subsequent predictive modeling steps.
We select several regression models to predict the prices
of data products, including random forest [ 31], k-nearest
neighbors [50], gradient boosting [ 44], and XGBoost [ 35]. For
each of these models, we use grid search combined with cross-
validation to ﬁnd the best parameters and perform 5-fold cross-
validation to evaluate the performance. In addition to these
traditional regression models, we develop a basic deep neural
network (DNN). We use ReLU [ 25] as the activation function,
Adam [48] as the optimizer, and apply Dropout [ 57] to reduce
overﬁtting.
A variety of metrics are used to evaluate the performance of
models, including the coefﬁcient of determination ( R2 score),
mean absolute error (MAE), mean squared error (MSE), and
standard deviation (SD). Table IV presents the performance
of different models on the data product pricing prediction
task. The experimental results show that XGBoost consistently
outperforms the other models in most evaluation metrics.
TABLE IV: Performance comparison of different models on
the data product price prediction task. XGBoost achieves the
best overall performance with the highest R2 score and the
lowest MSE and SD. DNN has the lowest MAE but exhibits
the highest variability.
Model R2 score ( ↑) MAE ( ↓) MSE ( ↓) SD ( ↓)
k-Nearest Neighbors 0.765 0.808 2.499 1.576
DNN 0.810 0.779 1.960 4.368
Random Forest 0.814 0.876 1.977 1.405
Gradient Boosting 0.829 0.851 1.815 1.346
XGBoost 0.833 0.805 1.774 1.330
We also extract word embeddings from the last (24th) layer.
The remaining experimental procedures are consistent with
the 12th layer, where we identify the best parameters through
grid search and evaluate model performance using 5-fold
cross-validation. Table V summarizes the experimental results.
XGBoost outperforms other models across all metrics, but it
performs worse than the method that uses the intermediate
layer as word embeddings in Section V -A. This is because the
last layer of the model is more focused on the classiﬁcation
task, potentially losing some information.
TABLE V: Performance comparison of different models on
the data product price prediction task. Different from the
experiment in Section V -A, we obtain word embeddings from
the last layer (24th layer) instead of the intermediate layer
(12th layer) of our best ﬁne-tuned XLM-RoBERTa-Large
model. XGBoost performs the best across all metrics.
Model R2 score ( ↑) MAE ( ↓) MSE ( ↓) SD ( ↓)
k-Nearest Neighbors 0.726 0.921 2.922 1.708
DNN 0.745 0.971 2.630 4.441
Random Forest 0.814 0.874 1.977 1.406
Gradient Boosting 0.808 0.930 2.049 1.431
XGBoost 0.825 0.832 1.860 1.364
Ablation Study. To quantify the contribution of textual and
structured metadata, we conduct an ablation study using Gra-
dient Boosting under the same 5-fold cross-validation protocol.

The structured-only setting excludes text embeddings, the text-
only setting uses only PCA-reduced XLM-RoBERTa-Large
embeddings of title and description, and the full setting
combines both feature groups. The “Features” column in
Table VI reports the ﬁnal input dimensionality after text PCA,
categorical one-hot encoding, and numerical standardization,
rather than the number of raw metadata ﬁelds.
As shown in Table VI, structured metadata alone provides
useful pricing signals, achieving an R2 score of 0.779. Text
embeddings alone are less accurate, but they provide com-
plementary semantic information: combining 12th-layer text
embeddings with structured metadata improves R2 to 0.834.
The 12th-layer representation also outperforms the 24th-layer
representation in both text-only and full settings.
Pricing Results for Two Major Categories. For this exper-
iment, we speciﬁcally select the two major data categories in
the dataset: “Financial Services Data” and “Retail, Location
and Marketing Data”. We train and test the pricing models
separately on these two categories to assess their domain-
speciﬁc performance. As shown in Table VII, the pricing
model achieves higher accuracy on “Financial Services Data”
than “Retail, Location and Marketing Data”. This discrepancy
is likely attributable to more consistent and well-deﬁned
pricing patterns in “Financial Services Data”, which enable
the model to better capture the underlying pricing logic and
generate more accurate estimates.
Pricing Result Explanation. The above experimental results
indicate that models trained on DaDaDa can accurately predict
data product prices. To identify the key determinants of pricing,
we utilize SHAP (SHapley Additive exPlanations) [ 53], a game
theory-based interpretability method that breaks down model
predictions into contributions from individual features.
Figure 5 highlights signiﬁcant differences in price distribu-
tions across different pricing modes, so we conduct separate
feature importance analyses for each mode using three top-
performing models: Random Forest (RF), Gradient Boosting
(GB), and XGBoost (XGB). As illustrated in Figure 6, the
ﬁndings are as follows:
• “Description” is recognized as the most critical feature
across all pricing modes, reﬂecting market realities where
buyers mainly evaluate products based on descriptive con-
tent.
• “Update frequency” holds signiﬁcance in both one-off and
subscription modes. One-off buyers appreciate frequent up-
dates that enhance the utility of the data, while subscription
users are willing to pay a premium for regularly refreshed
information.
• “Coverage” is crucial in the subscription mode, as sub-
scribers need comprehensive data for long-term decision-
making.
• “Dimension” is particularly important in the usage-based
mode, where higher-dimensional data commands premium
pricing due to the increased information density offered per
call.
Fig. 6: Results of SHAP calculation. We calculate the relative
importance of different features (Size, Dimension, V olume,
Description, Category, Update_frequency, Coverage) in pre-
dicting the price of data products under three different pricing
modes (one-off, subscription, usage-based), using three differ-
ent machine learning models (Random Forest - RF, Gradient
Boosting - GB, XGBoost - XGB).
• Model comparisons reveal consistent feature attention pat-
terns, with XGBoost demonstrating the most balanced
SHAP value distribution, which likely contributes to its
superior pricing performance.
Table VIII further summarizes the top feature groups by
pricing mode. The values are grouped mean absolute SHAP
scores averaged across Random Forest, Gradient Boosting,
and XGBoost over the cross-validation folds. This quantitative
summary conﬁrms that description dominates all three
pricing modes, while structured ﬁelds provide complementary
mode-speciﬁc signals.
Generalization. We experimentally validate the generaliza-
tion ability of our pricing model trained on the DaDaDa
dataset. The DaDaDa dataset contains data products from
9 different data marketplaces. We select the data product
information from 8 of these marketplaces as the training set
to train our pricing model and then test the pricing prediction
capability of the model on the 9th marketplace (Snowﬂake).
This approach allows us to assess the generalization ability of
the model across different data marketplaces and evaluate its
performance in a new market environment. The experimental
results in Table IX demonstrate that our model achieves strong
generalization performance on the Snowﬂake marketplace after
training on data from eight distinct marketplaces. Although
data products from different marketplaces may have distinct
characteristics, our model is still capable of achieving high
predictive accuracy in an unseen marketplace.
B. Data Product Classiﬁcation
DaDaDa supports training classiﬁcation models to assist
in classifying new data products into predeﬁned categories
based on their metadata. To validate its effectiveness, we
ﬁne-tune two multilingual pretrained models: mBERT (bert-
base-multilingual-cased) [40] and XLM-RoBERTa-Large [ 37],
testing their classiﬁcation performance.

TABLE VI: Ablation study for the data product pricing task using Gradient Boosting.
Feature setting Embedding layer Features R2 (↑) MAE ( ↓) MSE ( ↓) SD ( ↓)
Structured only N/A 279 0.779 1.047 2.351 1.533
Text only 12th 223 0.652 1.185 3.716 1.923
Text + structured 12th 502 0.834 0.828 1.763 1.327
Structured only N/A 279 0.779 1.047 2.351 1.533
Text only 24th 55 0.577 1.389 4.531 2.125
Text + structured 24th 334 0.812 0.906 2.002 1.414
TABLE VII: Performance comparison of different models on
data product price prediction task, evaluated separately on two
main data categories.
Financial Services Data
Model R2 (↑) MAE ( ↓) MSE ( ↓) SD ( ↓)
k-Nearest Neighbors 0.818 0.936 3.056 1.722
DNN 0.843 0.923 2.306 5.334
Random Forest 0.870 0.917 2.174 1.468
Gradient Boosting 0.882 0.880 2.174 1.468
XGBoost 0.871 0.903 2.161 1.466
Retail, Location and Marketing Data
k-Nearest Neighbors 0.661 0.868 2.570 1.595
DNN 0.801 0.803 1.604 3.775
Random Forest 0.769 0.848 1.745 1.316
Gradient Boosting 0.794 0.802 1.560 1.245
XGBoost 0.778 0.776 1.681 1.293
TABLE VIII: Top feature groups by grouped mean absolute
SHAP value under different pricing modes.
Pricing mode Rank Feature group Mean abs. SHAP
Subscription 1 description 1.0594
Subscription 2 coverage 0.1535
Subscription 3 update_frequency 0.1075
One-off 1 description 1.0731
One-off 2 update_frequency 0.1254
One-off 3 volume 0.0651
Usage-based 1 description 1.2250
Usage-based 2 dimension 0.6059
Usage-based 3 category 0.1070
We divide DaDaDa into three parts: a training set (60%), a
validation set (20%), and a test set (20%). The category of a
data product can be inferred from its title and description.
These two ﬁelds are mainly in English and Chinese, with a
small portion in Japanese. To work with this multilingual data,
we choose mBERT and XLM-RoBERTa-Large, which have
been pretrained in multiple languages. We concatenate title
and description, and input them into the models for ﬁne-
tuning. We assess the performance using the validation set
and select the best ﬁne-tuned model after multiple rounds of
training. Finally, we evaluate the performance of the best ﬁne-
tuned model using the test set.
Table X presents the performance of the ﬁne-tuned models
on the test set. XLM-RoBERTa-Large shows better classiﬁca-
tion performance in most categories, outperforming mBERT
overall. Both models achieve an average F1-score of over 0.8,
demonstrating that our dataset can effectively aid in classifying
TABLE IX: Generalization performance comparison of dif-
ferent models on the data product price prediction task. The
model is trained on eight source marketplaces and evaluated
on the held-out Snowﬂake marketplace, demonstrating gener-
alization capability in new marketplace environments.
Model R2 score ( ↑) MAE ( ↓) MSE ( ↓) SD ( ↓)
Random Forest 0.675 1.733 4.327 1.821
Gradient Boosting 0.741 1.514 3.445 1.702
XGBoost 0.744 1.887 5.350 1.594
data products and promote the standardization of classiﬁcation.
Table XI reports the corresponding confusion matrix.
C. Data Product Retrieval
Fig. 7: A screenshot of the data product search engine.
When searching for a suitable dataset for machine learning
or other purposes, it can be frustrating to sift through many
data marketplaces and thousands of data products, only to
ﬁnd that very few meet the requirements for training. While
general search engines are the ﬁrst thing that comes to mind
for online searches [ 42], they are not well-equipped to handle
the speciﬁc task of searching for data products. This is due
to the fact that different data marketplaces offer different
types of data products with varying levels of detail in the
metadata, making it a daunting task to gather comparable
results and decide which product to choose. DaDaDa makes
it possible to create a vertical search engine for data products
collected from major open-access data marketplaces around

TABLE X: Performance of mBERT and XLM-RoBERTa-Large on different data product categories. The XLM-RoBERTa-Large
model has better classiﬁcation results in most categories.
Category mBERT XLM-RoBERTa-Large
Precision Recall F1 Mean Precision Recall F1 Mean
Automotive 0.667 0.701 0.684 0.684 0.716 0.688 0.702 0.702
Environmental 0.774 0.739 0.756 0.756 0.782 0.693 0.735 0.737
Financial Services 0.839 0.809 0.824 0.824 0.840 0.851 0.846 0.846
Gaming 1.000 0.500 0.667 0.722 1.000 1.000 1.000 1.000
Healthcare and Life Sciences 0.864 0.851 0.858 0.858 0.878 0.851 0.864 0.864
Manufacturing 0.927 0.927 0.927 0.927 0.906 0.921 0.914 0.914
Media and Entertainment 0.739 0.790 0.764 0.764 0.756 0.749 0.752 0.752
Public Sector 0.743 0.774 0.758 0.758 0.732 0.770 0.751 0.751
Resources 0.634 0.607 0.620 0.620 0.717 0.650 0.682 0.683
Retail, Location and Marketing 0.848 0.854 0.851 0.851 0.849 0.878 0.863 0.863
Telecommunications 0.700 0.714 0.707 0.707 0.748 0.671 0.707 0.709
Other 0.562 0.474 0.514 0.517 0.733 0.579 0.647 0.653
Weighted Average 0.810 0.809 0.809 0.809 0.820 0.821 0.820 0.820
TABLE XI: Confusion Matrix for XLM-RoBERTa-Large Classiﬁcation.
Predicted Class
True Class Auto. Env. Fin. Gam. Health Manuf. Media Other Public Res. Retail Tele.
Automotive 53 2 5 0 0 2 1 0 4 0 8 2
Environmental 1 61 6 0 1 0 2 0 6 8 2 1
Financial 3 5 600 0 3 4 15 0 3 3 60 9
Gaming 0 0 0 2 0 0 0 0 0 0 0 0
Healthcare 1 1 4 0 172 1 3 0 4 3 12 1
Manufacturing 3 1 1 0 3 164 0 0 3 0 1 2
Media 6 0 6 0 2 0 164 0 6 0 29 6
Other 0 0 0 0 0 0 2 11 0 0 3 3
Public Sector 2 1 16 0 8 3 4 0 167 7 6 3
Resources 1 3 8 0 1 0 0 0 12 76 12 4
Retail 4 4 55 0 5 4 19 3 15 6 1013 26
Telecomm 0 0 13 0 1 3 7 1 8 3 47 169
the world. To demonstrate how DaDaDa can streamline the
data search process, we use it to create a search engine based
on Elasticsearch.
Figure 7 displays the search engine based on DaDaDa. The
left part of the ﬁgure shows the metadata ﬁlter, where users can
adjust settings to obtain ﬁltered results. The available options
in DaDaDa can be categorized into two types of ﬁlters: range
ﬁlters and keyword ﬁlters. Price, volume, size, and dimension
are examples of range ﬁlters, allowing users to set minimum
and maximum values for each option. The remaining features
are keyword ﬁlters, offering multiple options for users. The
system generates a query based on the ﬁlter parameters and
the search text in the input box at the top of the page. The most
relevant query results are displayed below the input box, along
with necessary metadata such as title, price, platform, and part
of the description. Users can click the title to navigate to the
detail page of the product for more information or to make a
purchase.
For example, to ﬁnd data products that contain B2B data
covering the United States, the user can simply input “B2B
data US”, and all results matching the search text are displayed
below. If the user has more detailed requirements, such as
products from Datarade with a one-off pricing mode and a
price higher than 2000 USD, the user can set the “Platform”,
“Pricing Mode”, “Price Range”, and “Data Coverage” ﬁlters
accordingly for a reﬁned result.
Retrieval Implementation. The search engine indexes each
data product as a document containing textual ﬁelds, struc-
tured categorical ﬁelds, and numerical ﬁelds. The title,
description, and geographic coverage ﬁelds are indexed
for full-text matching, while platform, provider, category,
price_mode, and update_frequency are represented as key-
word ﬁlters. Numerical attributes such as price, volume,
size, and dimension are represented as range-query ﬁelds.
This mixed indexing design is useful for data-product search
because user intent is usually both semantic and constrained:
a buyer may search for “mobility data”, but also require
a particular region, a maximum price, or a speciﬁc pricing
model.
We additionally include a country synonym analyzer for
geographic coverage. This helps bridge query variations such
as country names, abbreviations, and region-related terms,
which frequently appear in marketplace descriptions. Because
every retrieved item links back to its original marketplace

URL, the search engine acts as a cross-marketplace discovery
layer rather than replacing the original transaction platforms.
The implementation demonstrates that DaDaDa can support
not only ofﬂine model training, but also user-facing data
discovery systems where pricing information, metadata ﬁlters,
and original product pages are presented together.
Retrieval Case Study. The Elasticsearch prototype maps each
request to three query channels: full-text matching over title,
desc, and geo_coverage; keyword ﬁltering over platform,
provider, category, pricing_type, and freq; and range
ﬁltering over price, volume, size, and dimension. These
channels mirror the interface in Figure 7: buyers ﬁrst express
a semantic need, such as “B2B data US” or “mobility data
Germany”, and then narrow results by marketplace, geography,
billing model, update frequency, or numerical constraints.
The mapping also keeps the case reproducible because each
interface constraint corresponds to a ﬁeld in the released index
schema.
For example, if a buyer needs B2B data covering the
United States from Datarade with one-off pricing above 2,000
USD, the prototype matches the query text, uses country
synonyms to align “US”, “U.S.”, and “United States”, and
applies platform, pricing_type, and price ﬁlters. Returned
product cards show comparable metadata, including market-
place, title, provider, category, update frequency, coverage,
price or free/negotiation status, a short description, and the
original URL. This case study does not claim end-user retrieval
effectiveness; rather, it shows that the uniﬁed DaDaDa schema
is sufﬁcient to build a practical vertical search layer over
heterogeneous data marketplaces.
The example also exercises all three ﬁeld families in the
released schema, making it useful for checking whether text
analyzers, keyword ﬁlters, and numerical range predicates
work together. Since each result links back to the original
product page, the prototype remains a discovery layer that
helps buyers compare candidates before inspecting licensing
and purchase details on the source marketplace.
VI. A VAILABILITY , E THICS , AND LIMITATIONS
A vailability and Reproducibility. We release
DaDaDa through the project repository at https:
//github.com/ZJU-DIVER/DaDaDa, together with a Kaggle
mirror for convenient dataset access. The repository
contains the ﬁnal standardized dataset, raw crawled ﬁles,
intermediate preprocessed ﬁles, sample data ﬁles, crawling
code, preprocessing scripts, experiment scripts, and metadata
documentation. The pricing pipeline includes scripts for
extracting XLM-RoBERTa-Large embeddings, applying
PCA, constructing regression features, training pricing
models, and computing SHAP-based feature importance.
The classiﬁcation pipeline includes model ﬁne-tuning and
test scripts for multilingual pretrained models. The retrieval
pipeline includes the Elasticsearch index schema and a
frontend demonstration. Releasing these components together
allows researchers to reproduce our task results and to
extend the benchmark with new pricing models, classiﬁcation
methods, or retrieval interfaces.
Ethical Considerations. The dataset is constructed from
publicly accessible product metadata rather than private trans-
action records or raw customer data. We collect product-
level descriptions, public seller-provided attributes, prices, and
URLs that are visible on data marketplace pages. During crawl-
ing, requests are scheduled at controlled intervals and platform
directives are respected to avoid service disruption. We do
not redistribute private buyer information, transaction histories,
or any non-public information. When product samples are
publicly provided by the source marketplace, we store only
the sample ﬁles as released by the marketplace; otherwise, the
data_sample ﬁeld records that no sample is available.
Because the dataset describes commercial data products, it
should be used as a benchmark for research, marketplace anal-
ysis, and decision support rather than as a tool for copying or
reselling products. Prices and descriptions remain attributable
to their original marketplaces through the public URLs. Users
should check the original product page and licensing terms
before purchasing, using, or redistributing any referenced data
product. This is especially important for sensitive domains
such as healthcare, ﬁnance, mobility, and personal-data-related
products, where marketplace listings may involve additional
legal or contractual constraints.
Limitations. DaDaDa is a versioned snapshot of public
marketplace listings, so it is intended as a benchmark for
listed-price estimation and metadata-driven comparison under
transparent and reproducible assumptions rather than a record
of realized transactions. Public pages may change over time,
and private discounts, enterprise contracts, bundling, or custom
licensing terms are usually not visible. Some structured ﬁelds
are also disclosed unevenly across platforms; we preserve
such products to maintain broad marketplace coverage and
encode unavailable numeric values consistently instead of
inventing unsupported properties. Negotiation-based products
remain useful for marketplace and retrieval analysis even when
they are not included in listed-price regression. These design
choices keep the dataset aligned with how buyers observe data
products in practice, while the released URLs, crawlers, pre-
processing scripts, and uniﬁed schema allow future snapshots
to refresh listings and compare new methods under the same
public-data protocol.
VII. C ONCLUSION
In this paper, we introduce DaDaDa, the ﬁrst comprehensive
dataset for data product pricing. This dataset ﬁlls the gap in
data product pricing by including various features that describe
and inﬂuence the price of a data product. Additionally, we
develop a data product search engine to improve the data re-
trieval process. Experimental results show that both the pricing
and classiﬁcation tasks achieve high accuracy, highlighting the
effectiveness of DaDaDa in enhancing data product pricing
and classiﬁcation. Beyond these tasks, DaDaDa provides a
reusable benchmark for empirical data-marketplace research.

The released metadata, URLs, crawlers, preprocessing scripts,
and task code allow future work to refresh public listings and
compare pricing, classiﬁcation, and retrieval methods under a
shared protocol. This gives researchers a common reference
point for studying data products across marketplaces.
The importance of data markets is increasingly recognized
and the ﬁeld continues to develop rapidly. In contributing
to this evolving landscape, we plan to develop an online
metadata crawling system that can automatically gather the
latest product metadata and process it into a standardized
format to ensure regular updates for the dataset. Such temporal
extensions will make it possible to study how sellers revise
prices and how marketplace-level disclosure practices evolve.
REFERENCES
[1] Advaneo. https://www.advaneo-datamarketplace.de/database/en, 2026.
[2] AWS Marketplace. https://aws.amazon.com/marketplace, 2026.
[3] Azure. https://azure.microsoft.com/en-us/products/open-datasets/ , 2026.
[4] Beibu Gulf Data Exchange. https://www.bbgdex.com/, 2026.
[5] Beijing International Data Exchange. https://www.bjidex.com, 2026.
[6] Canton Data Exchange. https://www.cantonde.com, 2026.
[7] Carto. https://carto.com, 2026.
[8] Databricks. https://www.databricks.com/product/marketplace, 2026.
[9] DataBroker. https://www.databroker.global/data-marketplace, 2026.
[10] Datarade. https://datarade.ai/, 2026.
[11] Datatang. https://www.datatang.com/, 2026.
[12] Elasticsearch. https://www.elastic.co/, 2026.
[13] Google Cloud. https://console.cloud.google.com/marketplace, 2026.
[14] Guiyang Global Big Data Exchange. https://www.gzdex.com.cn, 2026.
[15] Mobilithek. https://mobilithek.info, 2026.
[16] Nasdaq data link. https://data.nasdaq.com, 2026.
[17] Selenium. https://www.selenium.dev/, 2026.
[18] Shanghai Data Exchange. https://dtxp.chinadep.com, 2026.
[19] Shenzhen Data Exchange. https://www.szdex.com, 2026.
[20] Snowﬂake . https://www.snowﬂake.com/en/data-cloud/marketplace/,
2026.
[21] V eracity. https://www.veracity.com, 2026.
[22] Western China Data Exchange. https://www.westdex.com.cn, 2026.
[23] Y early Average Currency Exchange Rates. https:
//www.irs.gov/individuals/international-taxpayers/
yearly-average-currency-exchange-rates , 2026.
[24] Zhejiang Big Data Exchange. https://ditm.zjdex.com, 2026.
[25] A. F. Agarap. Deep learning using rectiﬁed linear units (relu). arXiv
preprint arXiv:1803.08375 , 2018.
[26] A. Agarwal, M. Dahleh, and T. Sarkar. A marketplace for data: An
algorithmic solution. In Proceedings of the 2019 ACM Conference on
Economics and Computation , pages 701–726, 2019.
[27] S. A. Azcoitia, C. Iordanou, and N. Laoutaris. What is the price of data?
a measurement study of commercial data marketplaces. arXiv preprint
arXiv:2111.04427, 2021.
[28] S. A. Azcoitia, C. Iordanou, and N. Laoutaris. Understanding the price
of data in commercial data marketplaces. In Proceedings-International
Conference on Data Engineering , 2023.
[29] S. A. Azcoitia and N. Laoutaris. A survey of data marketplaces and
their business models. ACM SIGMOD Record , 51(3):18–29, 2022.
[30] A. E. Baum, N. Crosby, and S. Devaney. Property investment appraisal .
John Wiley & Sons, 2021.
[31] L. Breiman. Random forests. Machine learning , 45:5–32, 2001.
[32] C. Chai, J. Wang, Y . Luo, Z. Niu, and G. Li. Data management for
machine learning: A survey. IEEE Transactions on Knowledge and
Data Engineering , 35(5):4646–4667, 2022.
[33] S. Chawla, S. Deep, P . Koutris, and Y . Teng. Revenue maximization for
query pricing. Proc. VLDB Endow. , 13(1):1–14, 2019.
[34] L. Chen, P . Koutris, and A. Kumar. Towards model-based pricing for
machine learning in a data marketplace. In P . A. Boncz, S. Manegold,
A. Ailamaki, A. Deshpande, and T. Kraska, editors, Proceedings of
the 2019 International Conference on Management of Data, SIGMOD
Conference 2019, Amsterdam, The Netherlands, June 30 - July 5, 2019 ,
pages 1535–1552. ACM, 2019.
[35] T. Chen and C. Guestrin. Xgboost: A scalable tree boosting system.
In Proceedings of the 22nd acm sigkdd international conference on
knowledge discovery and data mining , pages 785–794, 2016.
[36] Y . Chen, Y . Shen, and S. Zheng. Truthful data acquisition via peer
prediction. In H. Larochelle, M. Ranzato, R. Hadsell, M. Balcan, and
H. Lin, editors, Advances in Neural Information Processing Systems
33: Annual Conference on Neural Information Processing Systems 2020,
NeurIPS 2020, December 6-12, 2020, virtual , 2020.

[37] A. Conneau, K. Khandelwal, N. Goyal, V . Chaudhary, G. Wenzek,
F. Guzmán, E. Grave, M. Ott, L. Zettlemoyer, and V . Stoyanov.
Unsupervised cross-lingual representation learning at scale. CoRR,
abs/1911.02116, 2019.
[38] A. Damodaran. Investment valuation: Tools and techniques for deter-
mining the value of any asset . John Wiley & Sons, 2012.
[39] S. Deep and P . Koutris. QIRANA: A framework for scalable query
pricing. In S. Salihoglu, W. Zhou, R. Chirkova, J. Y ang, and D. Suciu,
editors, Proceedings of the 2017 ACM International Conference on
Management of Data, SIGMOD Conference 2017, Chicago, IL, USA,
May 14-19, 2017 , pages 699–713. ACM, 2017.
[40] J. Devlin, M. Chang, K. Lee, and K. Toutanova. BERT: pre-training
of deep bidirectional transformers for language understanding. CoRR,
abs/1810.04805, 2018.
[41] R. Dolan. How do you know when the price is right? Harvard Business
Review, 73(5):174–180, 1995.
[42] R. C. Fernandez, Z. Abedjan, F. Koko, G. Y uan, S. Madden, and
M. Stonebraker. Aurum: A data discovery system. In 34th IEEE
International Conference on Data Engineering, ICDE 2018, Paris,
France, April 16-19, 2018 , pages 1001–1012. IEEE Computer Society,
2018.
[43] R. C. Fernandez, P . Subramaniam, and M. J. Franklin. Data market
platforms: Trading data assets to solve data problems. Proceedings of
the VLDB Endowment , 13(11):1933–1947, 2020.
[44] J. H. Friedman. Greedy function approximation: a gradient boosting
machine. Annals of statistics , pages 1189–1232, 2001.
[45] A. Ghosh and A. Roth. Selling privacy at auction. In Proceedings of the
12th ACM conference on Electronic commerce , pages 199–208, 2011.
[46] P . Hanspach, G. Sapi, and M. Wieting. Algorithms in the marketplace:
An empirical analysis of automated pricing in e-commerce. Information
Economics and Policy , 69:101111, 2024.
[47] N. Jones. The AI revolution is running out of data. what can researchers
do? Nature, 636(8042):290–292, 2024.
[48] D. P . Kingma and J. Ba. Adam: A method for stochastic optimization.
arXiv preprint arXiv:1412.6980 , 2014.
[49] P . Koutris, P . Upadhyaya, M. Balazinska, B. Howe, and D. Suciu. Query-
based data pricing. Journal of the ACM (JACM) , 62(5):1–44, 2015.
[50] O. Kramer. Unsupervised k-nearest neighbor regression. arXiv preprint
arXiv:1107.3600, 2011.
[51] C. Li, D. Y . Li, G. Miklau, and D. Suciu. A theory of pricing private data.
ACM Transactions on Database Systems (TODS) , 39(4):1–28, 2014.
[52] J. Liu, J. Lou, J. Liu, L. Xiong, J. Pei, and J. Sun. Dealer: an end-to-end
model marketplace with differential privacy. Proceedings of the VLDB
Endowment, 14(6), 2021.
[53] S. M. Lundberg and S.-I. Lee. A uniﬁed approach to interpreting model
predictions. Advances in neural information processing systems , 30,
2017.
[54] A. Ma ´ckiewicz and W. Ratajczak. Principal components analysis (pca).
Computers & Geosciences , 19(3):303–342, 1993.
[55] S. Mehta, M. Dawande, G. Janakiraman, and V . S. Mookerjee. How to
sell a data set? pricing policies for data monetization. Inf. Syst. Res. ,
32(4):1281–1297, 2021.
[56] J. Pei, R. C. Fernandez, and X. Y u. Data and ai model markets:
Opportunities for data and model sharing, discovery, and integration.
Proceedings of the VLDB Endowment , 16(12):3872–3873, 2023.
[57] N. Srivastava, G. Hinton, A. Krizhevsky, I. Sutskever, and R. Salakhutdi-
nov. Dropout: a simple way to prevent neural networks from overﬁtting.
The journal of machine learning research , 15(1):1929–1958, 2014.
[58] M. Wieting and G. Sapi. Algorithms in the marketplace: An empirical
analysis of automated pricing in e-commerce. Available at SSRN ,
3945137, 2021.
