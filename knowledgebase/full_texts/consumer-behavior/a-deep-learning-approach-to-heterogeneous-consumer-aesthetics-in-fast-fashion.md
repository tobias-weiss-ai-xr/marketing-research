---
title: A Deep Learning Approach to Heterogeneous Consumer Aesthetics in Fast Fashion
url: https://arxiv.org/abs/2405.10498
category: consumer-behavior
subcategory: empirical
date: 2024-05
venue: ''
authors:
- Pranjal Rawat
source: arxiv
pdf_url: https://arxiv.org/pdf/2405.10498
pages: 71
chars: 153074
fetched_at: '2026-11-08T13:11:05+00:00'
kb_version: 1
---

# A Deep Learning Approach to Heterogeneous Consumer Aesthetics in Fast Fashion

A Deep Learning Approach to Heterogeneous Consumer
Aesthetics in Fast Fashion ∗
Pranjal Rawat†
April 22, 2026
Abstract
Aesthetics drives product differentiation in industries such as fashion, interior decor,
luxury goods, real estate and hospitality. However, visual differentiation is hard to
encode in formal economic analysis. This paper develops a methodology to parse, process
and model the aesthetic dimension and applies it to fast fashion. It works with millions
of purchase records from H&M in the Netherlands, including product images, text
descriptions, prices, and consumer demographics. I fine-tune Fashion CLIP embeddings
with a three-tower approach that builds separate channels for product visuals and
text, consumer history, and price, which makes downstream analysis tractable and
scalable. The embeddings feed a latent-class deep demand system that captures price
and taste sensitivities through deep nets, recovers rich substitution patterns, reveals
meaningful heterogeneity, and performs much better than competing alternatives. Then,
a supply-side inversion recovers sensible markups and costs and supports conduct tests
and counterfactuals on sustainability practices. I also estimate machine learning hedonic
pricing models that perform much better than competing alternatives. This model
allows us to construct quality-adjusted price indices, make it possible to price completely
new designs, and with an Oaxaca-Blinder decomposition reveal the underlying sources
of price changes. Finally, a Poisson event study around the COVID-19 lockdown shows
that the range of demand responses across embedding-based product and user clusters
exceeds anything recoverable from simple text-based attributes or demographic labels
alone. All these findings show that high-dimensional embeddings can be first class
citizens in disciplined economic and statistical analysis. The methodology is portable
to any market where products are differentiated along sensory dimensions that are hard
to encode but meaningfully important for consumer choices.
∗I thank John Rust, Sanjog Misra, Nathan Miller, and Harry Paarsch for guidance and feedback.
†PhD Candidate, Georgetown University
1
arXiv:2405.10498v2  [econ.GN]  20 Apr 2026

Contents
1 Introduction 4
2 Data and Context 8
2.1 Primary Estimation Sample: Dresses . . . . . . . . . . . . . . . . . . . . . . 10
2.2 Cross-Category Estimation Samples . . . . . . . . . . . . . . . . . . . . . . . 11
3 Representation Learning 11
3.1 Three-Tower Architecture . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
3.2 Contrastive Training . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
4 Theoretical Framework 15
4.1 Latent Class Deep Logit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
4.2 Price Elasticities and IIA Departures . . . . . . . . . . . . . . . . . . . . . . 18
4.3 Supply-Side Markup Recovery . . . . . . . . . . . . . . . . . . . . . . . . . . 19
4.4 Consumer Surplus . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
5 Demand and Supply Estimation 20
5.1 Latent Class Estimates: Taste vs Price . . . . . . . . . . . . . . . . . . . . . 20
5.2 Heterogeneity Decomposition . . . . . . . . . . . . . . . . . . . . . . . . . . 23
5.3 Substitution Structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
5.4 Consumer-Cluster Substitution . . . . . . . . . . . . . . . . . . . . . . . . . 25
5.5 Seasonal Demand Dynamics . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
5.6 Markup Recovery . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
6 Counterfactuals 28
6.1 Sustainability Practices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
6.2 Aesthetic Differentiation Collapse . . . . . . . . . . . . . . . . . . . . . . . . 29
6.3 Personalized Pricing Ladder . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
6.4 Recommendation Validation:β-net vs Collaborative Filtering . . . . . . . . 31
6.5 Class-Level Taste Heterogeneity in theβ-net . . . . . . . . . . . . . . . . . . 32
7 Hedonic Price Indices 33
7.1 Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
7.2 Interpretation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
7.3 Price Indices and Conformal Inference . . . . . . . . . . . . . . . . . . . . . 36
7.4 Decomposition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
8 Event Study: COVID-19 Lockdown 41
8.1 Empirical Framework . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
8.2 Heterogeneous Demand Responses . . . . . . . . . . . . . . . . . . . . . . . . 42
9 Discussion and Conclusion 49
9.1 Implications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
9.2 Limitations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
2

9.3 Future Research . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
A Choice Model Robustness 51
A.1 Control Function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
A.2 Consumer Bootstrap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
A.3 Outside-Good Calibration Sensitivity . . . . . . . . . . . . . . . . . . . . . . 52
A.4 Alternative Pre-trained Item Features . . . . . . . . . . . . . . . . . . . . . . 53
B Alternative Estimators 54
B.1 Demand . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
B.2 Hedonic . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
C Cross-Category Comparison 56
C.1 Demand Estimation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
C.2 Hedonic Pricing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
C.3 Lockdown Event Study . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
C.4 Post-Clustering Robustness for the Heterogeneity Range . . . . . . . . . . . 58
D Embedding Validation 59
E Glossary of Machine Learning Terms 63
3

1 Introduction
Aesthetics drive product differentiation in fashion, furniture, automobiles, and consumer
electronics. A dress’s commercial success comes down to its silhouette, color palette, fabric,
drape, proportion, texture, occasion fit, embellishment, print, and trend alignment. A human
eye picks these up instantly. Encoding them into the structured variables that empirical
economic analysis requires is the hard part. Demand systems need measurable dimensions
of differentiation [Berry et al., 1995, Train, 2009]. Hedonic pricing models need observable
product characteristics [Rosen, 1974, Court, 1939]. Event studies need meaningful product
groupings. Whenever differentiation is primarily visual, all three frameworks hit the same
obstacle, which is that the attributes that matter most are precisely the ones the researcher
cannot measure easily. Fast fashion markets show this at scale, and therefore are an ideal
ground to build models that can capture the great depth contained within “taste".
Numerical product embeddings learned from data have entered economic analysis from
multiple domains, including text [Gentzkow et al., 2019, Ash and Hansen, 2023], images
[Dell, 2025, Han et al., 2021, Zhang et al., 2022], product design [Burnap et al., 2023],
and financial portfolios [Gabaix et al., 2025]. In demand estimation, several recent papers
incorporate embeddings from pre-trained models into structural choice frameworks [Quan
and Williams, 2024, Bach et al., 2025, Magnolfi et al., 2023, Adam et al., 2024, Gabel and
Timoshenko, 2022, Sifringer et al., 2020, Wang et al., 2020, Berry and Haile, 2024]. Compiani
et al. [2025] is the closest specification to this paper, incorporating PCA-reduced pre-trained
image and text embeddings as random-coefficient characteristics in mixed logit applied to
Amazon data. Donnelly et al. [2021] learn joint product and consumer embeddings via
variational inference1 for grocery basket prediction, producing representations that predict
complementarity and substitution but are not deployed within a utility-maximizing demand
model. Bajari et al. [2025] use BERT and ResNet embeddings in a multi-task neural network
for hedonic price indices. These approaches either treat pre-trained representations as fixed
inputs to downstream estimation or learn embeddings without imposing economic structure
during training.
So what is new in this paper? First, the embeddings are fine-tuned on purchase behavior rather
than borrowed off the shelf, and this gives us better consumer and product representation.
Secondly, we not only have product embeddings but also user embeddings allowing us to
capture a great range of sensitivities than before. Third, we do not reduce embeddings via
PCA but show that it is possible to work fully with dense embeddings, and this allows a
greater diversity of counterfactuals such as generative fashion design. Lastly, we also estimate
hedonic and event study models to show that embeddings are not just a demand-side tool but
can be used across the board. The analysis proceeds in two clearly separated stages, divided
by a clean time break. Representation learning uses purchase records from September 2018
through June 2019. All three downstream applications run on a held-out window from July
2019 onwards.
1Variational inference is a technique for fitting probabilistic models with unobserved variables. The exact
posterior distribution over those variables is usually intractable. Variational inference instead picks the closest
member of a tractable family of distributions and optimizes that proxy. The technique scales to very large
datasets where classical Bayesian methods do not.
4

The first stage is representation learning. I fine-tune a pre-trained vision-language model
(OpenAI CLIP ViT-B/32, Radford et al. [2021]) on roughly8.8million H&M purchase
records from a first-window sample (September 2018 through June 2019) using a contrastive
purchase-prediction objective [van den Oord et al., 2018]. The architecture is a three-tower
neural network trained jointly across12product categories and39 969items. The item tower
maps562-dimensional features,512from the pre-trained CLIP encoder plus50from ten
categorical product attributes, to a64-dimensional aesthetic embedding. The consumer tower
maps purchase history and demographics to a64-dimensional user embedding. The price
tower maps log reference price through a small network to a separate64-dimensional price
embedding. The contrastive objective pulls a buyer’s embedding toward the purchased item
and pushes it away from every other item in the same product category. This in-category
negative sampling forces the item tower to encode aesthetic similarity from co-purchase
patterns while the dedicated price tower absorbs product-level price variation.
The fine-tune sits between two alternatives. Training a visual model directly on raw product
images needs more data and compute than this study has. Plugging in an off-the-shelf
representation is a reasonable fallback, and a pre-trained vision-language model is the natural
choice because it has already learned to place product images and product descriptions into
a shared vector space from a large external image-caption corpus. The approach taken here
fine-tunes this pre-trained CLIP model once more on the purchase records in this catalogue,
which distils the information in the pre-trained vector that matters for in-category choice. The
dress demand master in Section 5 then concatenates a separately extracted512-dimensional
FashionCLIP vector [Chia et al., 2022] alongside the three-tower item vector, so the master
model gets the richest feasible visual signal. The same fine-tune also produces a64-number
user embedding for every consumer, learned from first-window purchase behaviour, which
carries richer information than any hand-coded set of demographic attributes. The two-
stage split also gives fine-tuning access to all12product categories and roughly8.8million
H&M transactions, while the downstream estimation runs on the dress sample alone, so
representation learning gets the breadth it needs for generalisation and structural estimation
gets the specific choice set it needs for identification.
The second stage deploys the learned representations. The embeddings are frozen and used as
inputs to three distinct economic applications on a held-out second time window (July 2019
onwards), each asking a different question of the same representations. Section 5 estimates a
latent-class deep logit demand model and inverts the estimated system through a supply-side
markup recovery to recover implied marginal costs. Section 6 runs the counterfactual policy
analysis on the estimated primitive. Section 7 uses the embeddings as regressors in a machine
learning hedonic pricing model to construct quality-adjusted price indices and decompose
price changes. Section 8 clusters products and users in embedding space and tracks the
dispersion of demand responses to the COVID-19 lockdown within a single retail category.
The demand model recovers meaningful consumer-specific price sensitivity through a small
neural network, theα-net, whose final layer forces the price coefficient to be negative for every
consumer. A latent-class extension separates two consumer segments and delivers a realistic
mean own-price elasticity. A supply-side inversion on the same estimated system yields
positive implied marginal costs for the large majority of the2034dresses, with a mean Lerner
5

index close to H&M’s reported gross margin (Section 5). The estimated demand-supply
system then feeds a battery of policy-relevant counterfactuals (Section 6), including the
profitability of sustainability practices, why visual differentiation in trend-chasing fast fashion
is critical to profitability, a personalised pricing ladder over demographic segments, and a
validation of the taste-matching network as a stand-alone recommender.
Figure 1 isolates aesthetic taste and price sensitivity in a single example. For two real H&M
customers drawn from the estimated demand system and two synthetic dresses that look
almost identical at a glance, each panel sweeps one dress’s own price across a realistic band
while holding the other dress at a forty-euro reference price. Every dot is one direct evaluation
of the two-type latent-class deep logit demand model for dresses. Two patterns emerge. First,
every curve slopes downward, which is the price-sensitivity network responding to own-price
increases. Second, the two customers disagree about which dress they prefer: in the Dress 1
panel, Customer A sits above Customer B at every price shown; in the Dress 2 panel, the
pattern mirrors, and Customer B sits above Customer A. This is the ranking flip that the
taste-matching network produces once it reads small design differences (sleeve length, fabric
sheen, neckline) that a hand-entered attribute list (colour, length, silhouette, garment group)
would collapse into a single identical label.
Figure 1: Two synthetic dresses produced by a generative image model. Each dot is the
probability that a customer picks the labelled dress given they pick one of these two, under
the two-type latent-class deep logit model of Section 4.1, evaluated at the named own price
with the other dress held at a forty-euro reference. Blue: Customer A. Red: Customer B.
The hedonic price indices reveal a product-mix composition bias of roughly9.9percentage
points over two years relative to matched-item indices, meaning the average product sold in
year two differs aesthetically from the average product sold in year one. An Oaxaca-Blinder
decomposition points to quality shifts that categorical controls cannot capture, rather than
aggregate price changes (Section 7). The lockdown event study surfaces wide dispersion in
6

demand responses across embedding-based clusters within a single retail category. Both item
and user clusters reveal heterogeneity substantially wider than anything the demographic
labels alone can recover, and several embedding clusters cross-cut the retailer’s own product
taxonomy in ways no text-only or category-label partition can reproduce (Section 8).
The methodology is portable to any market where products differ along sensory dimensions
that matter for consumer choice but are hard to put into structured variables. The recipe is
the same in each case. Start with a suitable pre-trained encoder, image models for visual
products, text models for prose-heavy categories, audio models for music. Fine-tune it on
observed purchase behavior using a contrastive loss with within-category negatives. Split
the signal into dedicated channels whenever price and match quality must be identified
independently. Freeze the learned representations and feed them to standard structural
estimation. Luxury goods, interior decor, furniture, hospitality, fine dining, art markets, and
high-end real estate all present the same measurement problem and the same solution path.
The framework offers a scalable way to relax the Independence of Irrelevant Alternatives
restriction in applied demand estimation. Mapping visual similarity into substitution patterns
produces cross-price elasticities that are non-proportional across product pairs at the consumer
level and aggregate into realistic market-level substitution. Ignoring unobserved aesthetic
differentiation can bias inflation measurement through quality-unadjusted price indices,
misstate market power by reattributing differentiation rents to raw price sensitivity, and
distort the welfare gain from product variety.
So where can practitioners apply this machinery? First, we can employ such models to
get consumer-specific price and aesthetic sensitivities. These can be useful in downstream
optimization tasks. Secondly, we can use the model to solve cold-start problems such as
pricing new products or recommending products to new users. Thirdly, we can use the
model to do “generative fashion design", where design teams can leverage this model to
run quick computer simulations to study both the price and demand impact of different
designs. Fourthly, we can use the hedonic model to better understand a firm’s (or the
market’s) pricing decisions and how they have evolved over time. This can be useful for
both the firm itself and for policymakers who are interested in understanding the market
dynamics. Lastly, the user and product embeddings themselves are very useful in causal
machine learning applications, where one can use a two-step (cluster-then-estimate) or even
a single-step (cluster-and-estimate) approach to estimating heterogeneous treatment effects
across products and users.
Several limitations apply. The analysis uses data from a single retailer in one market segment
over two years. The demand model is a deep neural network trained with stochastic gradient
descent, which makes convergence hard to certify, standard errors hard to obtain, computation
heavy, and estimates sensitive to architectural choices in theα-net and the taste projection
layers. The logit specification imposes IIA at the individual level, though heterogeneous
price sensitivity generates market-level departures. The model abstracts from size and fit
availability, browsing behavior, wardrobe complementarity, sequential purchasing dynamics,
and competitor pricing or assortment responses.
The paper proceeds as follows. Section 2 describes the data. Section 3 develops the three-tower
7

representation learning framework. Section 4.1 sets out the theoretical framework for the
latent-class deep logit and the Bertrand-Nash markup recovery. Section 5 presents the demand
and supply estimates and the seasonal extension. Section 6 runs the counterfactual policy
analysis. Section 7 constructs quality-adjusted hedonic price indices. Section 8 estimates
heterogeneous lockdown effects. Section 9 concludes.
2 Data and Context
The empirical analysis uses transaction data from H&M, the world’s second-largest fashion
retailer by revenue, covering a single national market.2 The dataset contains31 788 324
transactions from1 362 281customers purchasing104 547unique articles between September
20, 2018, and September 22, 2020. Table 1 summarizes the four constituent files.
Table 1: Data Structure
File Observations Key Variables
Transactions 31.8M date (734 days: Sept 2018 to Sept 2020), customer, product,
price, channel (online 70.4%, store 29.6%)
Articles 105K hierarchy (5 index groups, 21 garment groups, 131 types, 250
departments), aesthetic attributes (50 colors, 30 patterns),
text descriptions
Customers 1.36M age (16 to 99), gender (inferred), postal code (hashed), club
membership status, fashion news frequency
Images 105K product photographs
2The data come from the Netherlands. Two independent checks confirm this. First, several hundred
products in the catalog carry explicit “COLLAB NL” labels in their product names, corresponding to
Netherlands-only H&M designer collaborations sold during the sample period. Second, prices in the raw
transaction file are in H&M’s internal units; multiplying by the community-derived rescaling factor of 590
produces EUR amounts that match H&M Netherlands list prices for the same items verified against the
retailer’s website. The competition page that originally distributed the data notes that the currency was
deliberately obfuscated to avoid revealing the market; cross-referencing product names and price levels
identifies the market as the Netherlands.
8

Figure 2: Product assortment examples spanning price points and categories.
Figure 2 shows representative products spanning price points and categories in the catalogue.
The distribution of purchases exhibits positive skew across both products and customers. As
detailed in Table 2, product revenues are highly concentrated; the SKU-level Gini coefficient
equals0 .772, with the top 20% of products generating80.6%of total revenue. Pervasive
promotional pricing yields temporal price variation for92.3%of articles, securing identification
for the subsequent demand specifications.
On the consumer side (Table 2), the average purchase frequency rests at23.3transactions,
but the 90th percentile reaches60. This reflects a long tail of frequent buyers whose
dense purchase histories provide strong signals for learning consumer embeddings, while the
remaining infrequent buyers contribute primarily through demographic inputs.
Survey evidence from Dutch consumers provides a useful benchmark for the customer panel in
this dataset. Leinenga [2019] surveys 293 Dutch fashion consumers and finds wide variation
in purchase frequency: 2% buy clothing each week, 26% each month, and 44% once every
six months. The average Dutch wardrobe holds 173 items, of which 28% goes unworn in
a given year, and approximately 46 new fashion items are purchased annually per person.
This distribution is broadly consistent with the long right tail in Table 2, where purchase
frequency spans from 2 to over60transactions and9.7%of customers make only a single
purchase over the two-year window. The same survey also documents that consumers who
treat fashion as central to their identity buy more often and substitute less across product
types, a split between consumer types that reappears in the latent-class demand model in
Section 5.
Beyond static distributions, fast-fashion retail is defined by product turnover. Table 3
summarises weekly new-article introductions, article lifespan, and the basic/fashion/fashion-
basic tier split that governs markdown and clearance cycles.
9

Table 2: Market Distributions: Products and Customers
Products Customers
Statistic Price (EUR) Purchases Spending (EUR)
10th percentile 5.96 2 24.98
25th percentile 9.33 3 51.96
Median 14.99 9 144.90
75th percentile 19.99 27 413.70
90th percentile 29.99 60 957.51
Mean (SD) 16.42 (11.32) 23.3 (39.2) 383.14 (707.00)
Range 0.01–349.00 – –
Gini coefficient 0.772 – –
Top-20% revenue share 80.6% – –
One-time rate – 9.7% –
Pricing dynamics (all 104,547 articles)
Articles with price variation 92.3% – –
Median distinct prices/article 13 – –
Median max markdown depth 60.0% – –
Same-day markdowns 43.5% – –
Table 3: Fast Fashion Product Dynamics
Panel A: Product Lifecycle (all 104,547
articles)
Statistic Value
New articles/week (median) 706
New articles/week (mean) 986
Median lifespan 205 days
Lifespan<180 days 45.3%
Lifespan<90 days 26.2%
Panel B: Three-Tier Supply Chain †
Tier Articles Revenue p50 (EUR) Lifespan
Basic 15.3% 7.1% 9.40 155d
Fashion 23.0% 29.4% 18.93 238d
Fashion-B. 61.7% 63.5% 13.03 202d
†Author-constructed classification from product metadata (garment group, price level, and lifespan). Basic =
staples with low price CV; Fashion = trend-driven items; Fashion-Basic = hybrid.
2.1 Primary Estimation Sample: Dresses
The subsequent empirical analysis primarily uses the dress category as the estimation sample.
The raw dress catalogue contains10 266articles and3.2million transactions (10.2%of total
volume) from608 936customers. Dresses are suited for studying aesthetic differentiation for
three reasons. The category carries high visual variance, with47color groups and28pattern
types producing far more visual combinations than standard categorical controls can capture.
Seasonal demand amplitude is pronounced, peak summer volume exceeds the January trough
by a factor of 3.2, which gives the seasonal demand model real temporal variation to fit. And
10

94.5%of dress articles show within-product price variation, which is what the demand model
needs to identify price elasticities. All5870dress articles in the embedding sample have
product photographs, and99.6%carry text descriptions (median30words), confirming the
three input streams for the joint embedding in Section 3.
Downstream sample filters narrow this raw set in two steps. The embedding-validation cuts
in Section 3 use the5870dress articles that remain after applying CLIP image-extraction
filters (products must have a usable product photograph with non-trivial pixel coverage).
The demand-estimation sample in Section 5 narrows further to2034dress articles and38 918
consumers over a31-week pre-COVID window (July 2019 through January 2020), chosen to
avoid contamination from the lockdown demand regime documented in Section 8. Most of the
article-count drop from5870to2034comes from two cuts inside that window: keeping only
SKUs that fall inside the top 99 percent of category sales coverage, and requiring each SKU
to match an entry in the three-tower embedding index. The consumer panel is trimmed in
parallel by requiring at least two purchases per customer. Each of these filters is a mechanical
data requirement rather than a modelling choice.
2.2 Cross-Category Estimation Samples
The paper focuses on dresses for the main results, but the demand model runs identically
on five additional categories. All six use the same pre-COVID estimation window (T = 31
weeks, July 2019 to January 2020, online channel only). Table 4 reports the per-category
sample sizes, purchase counts, and median prices. The hedonic analysis in Section 7 and the
lockdown event study in Section 8 draw on the same product universe but extend to the full
two-year panel.
Table 4: Per-category estimation samples
Category ProductsJConsumersIWeeksTPurchases Price p50 (EUR)
Dress2034 38 91831162 60619.21
Trousers1818 68 75731272 94918.99
T-shirt1367 26 0533187 0539.55
Sweater1011 22 8083169 09114.72
Shorts1029 11 6933142 51912.61
Shirt496 44203112 29314.72
All categories: pre-COVID window (Jul 2019 to Jan 2020, online channel). Price p50 from article-month panel.
3 Representation Learning
3.1 Three-Tower Architecture
The first stage of the empirical pipeline compresses high-dimensional categorical features and
raw product images into concise embeddings that feed the structural models in Sections 5, 7
and 8. Throughout the paper I use the term embedding to mean a short numerical vector
11

that summarizes a product, consumer, or price in a learned space. Vectors that sit close to
each other in that space represent objects the model judges to be economically similar.
I fine-tune the embeddings once and then reuse them in everything that follows.3 Figure 3
summarizes the data flow from raw inputs to frozen embeddings to structural models.
Product
Images
CLIP
R512
Three-Tower
InfoNCE
Embeddings
vj,d i,p j
frozen
encode fine-tune extract
Event
Study
Hedonic
Indices
Deep Logit
Demand
Supply-Side
Markups
Figure 3: The modular estimation pipeline. Embeddings are fine-tuned once and then frozen
for all downstream identification strategies.
Two concerns motivate this fine-tuning step. First, the downstream demand, hedonic, and
event-study pipelines are easier to run with a compact representation than with raw image
features. A64-number vector per product is small enough to load, index, and pass through
subsequent networks at reasonable speed and memory cost; the512-dimensional CLIP output
multiplied across roughly39 969products and every consumer-item pair in the panel would be
slow and expensive to work with. Second, CLIP was trained on a different dataset and with
a different objective. It is a rich encoder but rich about many things that do not matter for
choice in this catalogue, such as photographic style, garment angle, lighting, and background
texture. Fine-tuning uses actual purchases in this catalogue as the training target, which
forces the64-number output to keep only the visual and categorical information that helps
rank the product actually bought above the products that were not.
A critical challenge in learning aesthetic representations is avoidingprice contamination. If
a single network ingests price alongside the visual inputs, the resulting product embedding
mergesprice-positioninginformationwithvisualcontent. Atypicaltwo-towerrecommendation
model does exactly this by feeding log price alongside image and categorical features into
a single item tower. That shortcut raises training-time purchase-prediction scores, but it
hurts the downstream estimation. The item embedding ends up carrying part of the price
variation. When this embedding is then passed to a logit demand model with price as a
separate regressor, the estimated price coefficient is pulled toward zero, because some of the
3Fine-tuning starts with a neural network already trained on a large external dataset and continues
training its parameters on task-specific data. In this paper, the pre-trained CLIP image-text encoder is used
as a frozen 512-dimensional feature extractor. What is trained on H&M purchase records is the three-tower
projection on top of it, which compresses the CLIP vector together with ten product categoricals into a
64-dimensional task-specific embedding.
12

true price response has already been absorbed into the item vector. Price plays a special role
in the downstream demand model as the scalar for elasticity estimation, so it has to sit in
its own place in the feature pipeline. I therefore route user, item, and price inputs through
three architecturally distinct towers that share no weights. The item tower requires a fixed-
dimensional representation of each product’s visual appearance, so I extract512-dimensional
embeddings from product photographs and product descriptions using a pre-trained vision-
language model, alongside50dimensions of categorical attributes (e.g., color group, garment
type).4 The item tower thus receives a562-dimensional input per product, the user tower
receives an85-dimensional input comprising a learnable ID embedding, demographics (e.g.,
age, postal code), and aggregate purchase history statistics, and the separate price tower
maps the log reference price through a specialized feedforward network. The item tower
maps its562-dimensional input through a feedforward network to produce a64-dimensional,
L2-normalized item embeddingvj5; similarly, the user tower produces a64-dimensional user
embeddingd i, and the price tower producespj. The predicted affinity between useri and
itemjis calculated as
ˆyij = d⊤ i vj−softplus(d⊤ i pj) τInfoNCE (1)
where τInfoNCE = 0.1is a temperature parameter.6 The softplus function,7 ensures the price
term always acts as a penalty against affinity. Because the item tower never sees price
as an input, the learned item embeddingvj contains no direct price signal. Any residual
correlation betweenvj and price must go through genuine visual or categorical features. As
Table 25 shows, the three-tower item embeddings still predict log prices with substantial
fit, because visual style and categorical features are themselves correlated with price tier.
The architectural claim is cleaner separation of price from visual content, not statistical
orthogonality. A related line of work in recommender systems makes a similar argument,
building price-aware models that keep price in its own channel rather than folding it into a
single mixed item representation [Zheng et al., 2020, 2023, Cui et al., 2020].
3.2 Contrastive Training
The three towers are trained jointly by minimising an InfoNCE contrastive loss [van den Oord
et al., 2018]8, which pulls the buyer’s representation toward the purchased item and pushes
4Visual and text features are extracted with the OpenAI CLIP ViT-B/32 model [Radford et al., 2021],
which was trained on a large external set of image and caption pairs using a contrastive objective that places
matching pairs close together and non-matching pairs far apart in a shared512-dimensional vector space.
The image and text embeddings for each product are averaged and renormalised to give one512-dimensional
vector per product, which the three-tower fine-tune then compresses to the task-relevant directions.
5L2 normalisation rescales each vector to unit length. After this step, the inner product between two
embeddings is the cosine of the angle between them, so magnitudes no longer affect scoring.
6The temperature controls how sharply the loss penalizes wrong rankings. A lower value concentrates
probability mass on the top-scoring item and makes training more aggressive; a higher value spreads mass
more evenly and smooths the gradient signal. The role is analogous to the scale parameter in a logit model.
7Softplus is log(1 +ex), a smooth version of the positive-part function. It is always positive, so the price
term in the score always subtracts from affinity.
8InfoNCE rewards the model for ranking the purchased item above a set of unpurchased distractors drawn
from the same product category. When the distractor set covers the entire category, the loss coincides with
13

it away from the other items in the same product category. Formally, for each observed
purchase(i,j +):
LInfoNCE =−
∑
(i,j+)
log exp (ˆyij+) ∑
k∈C(j +) exp (ˆyik) (2)
In standard econometric terms, Equation 2 is the negative log-likelihood of a conditional logit
in which each productj carries a latent characteristic vectorvj, each consumeri carries a
latent taste vectordi, and the systematic utility isd⊤ i vj/τInfoNCE. The setC(j+)is the choice
set, the purchased item together with the competing alternatives in the category, so the
denominator includes exp(ˆyij+)and the choice probabilities integrate to one. The absolute
scale and orientation of the latent vectors are not point-identified by the loss alone, a known
issue in the contrastive-learning literature [Rusak et al., 2024]. The non-identification does
not bind downstream because only inner productsd⊤ i vj enter the demand utility, and inner
products are invariant to joint orthogonal rotations and matched rescalings of the two vectors.
The two-stage design sits between two alternatives the paper does not take. Training a visual
model from raw product images needs more data and deeper networks than this sample
supports. A generic off-the-shelf image model is the next fallback but is weak here, since
it is not trained on fashion style. OpenAI CLIP is the strongest available fallback, so the
approach keeps the CLIP encoder frozen and trains only the three-tower projection head
on its 512-dimensional output. The resulting 64-dimensional projection is faster to work
with downstream and higher in retrieval accuracy than raw CLIP. The dress demand master
in Section 5 additionally concatenates a 512-dimensional FashionCLIP vector [Chia et al.,
2022] alongside the three-tower item vector. The fine-tune uses the September 2018 through
June 2019 window, and every downstream estimate uses the separate window from July 2019
onwards, so embedding-stage noise cannot leak into downstream coefficients through shared
observations. The same fine-tune also produces a 64-dimensional user embeddingdi for every
consumer, richer than any hand-coded demographic attribute set.
This training stage is used strictly to learn dense representations, not to recover structural
behavioural parameters. The items competing against the purchased item in the denominator
are drawn from the same product category, not from the entire catalogue, which forces the
embeddings to capture fine-grained aesthetic differences within a valid choice set. When this
denominator covers every other product in the category, Equation (2) is algebraically identical
to the log-likelihood of a standard multinomial choice model with utilityd⊤ i vj/τInfoNCE and
no price term. A recent line of work in operations research and transportation research
develops this exact equivalence between contrastive representation learning and discrete
choice estimation [Aouad and Désir, 2022, Arkoudi et al., 2023]. In practice the embedding
stage uses a random subsample of competing items per batch9 rather than the full category,
the same subsampling trick used in early methods for learning numerical embeddings from
very large text datasets [Mikolov et al., 2013]. The full structural demand system that uses
these embeddings as fixed inputs to a price-sensitivity network and a taste-matching network
is developed in Section 5.
the negative log-likelihood of a multinomial logit over that choice set.
9A batch is the small random slice of training examples used for one update to the model’s parameters.
Sampling negatives at the batch level keeps memory bounded as the catalogue grows.
14

Joint training that combines the contrastive loss with an explicit choice-model objective would
pull the price response back into the item tower and defeat the separation just described.
Other common contrastive objectives lose the clean mapping to discrete choice used above.
A pairwise ranking loss contrasts one purchased item against a single unpurchased one rather
than against a full choice set. A margin-based loss enforces a fixed gap between scores and is
not a probability distribution. A batch-level objective treats every item in the training batch
as a negative regardless of product category, which throws away the within-category choice
set the downstream demand model relies on.10 The trained three-tower model reaches Hit@10
retrieval accuracy of0.1896on a held-out validation sample of1.12million consumer-item
pairs.11
The training dataset covers12major product categories, roughly39 969items, and8.8million
pre-COVID transactions drawn from the full31.8million transaction panel. Only pre-COVID
records are used so the COVID shock does not contaminate the aesthetic space. Figure 4
illustrates this temporal separation. The resulting shared embedding space allows subsequent
analyses to extract category-specific subsets.
Sep 2018 Feb 2020 Sep 2020
Pre-COVID (T1) COVID Shock (T2)
Lockdown
Embedding Fine-T uning
(10 months)
Structural Estimation
Demand, Supply, & Hedonics
Figure 4: Training timeline. Embeddings are learned strictly on theT1 sequence to prevent
demand shocks from altering visual characteristics.
4 Theoretical Framework
This section lays out the latent-class deep logit of Section 5, the Bertrand-Nash markup
inversion that feeds off its demand Jacobian [Berry et al., 1995, Nevo, 2001], and the welfare
formulas used in the counterfactuals of Section 5. Notation is introduced inline as each object
appears.
10Pairwise ranking, triplet-margin, and SimCLR-style batch objectives are three well-known training
losses for representation learning. None of the three delivers the exact log-likelihood of a choice model at
convergence.
11Hit@10 is the fraction of held-out purchases for which the item actually bought appears among the top
ten items ranked by the model’s affinity score within its own product category.
15

4.1 Latent Class Deep Logit
Consumeriin classc∈{1,2}draws utility from productjin weekt,
Uijt|c =u ijt|c +εijt,(3)
with εijt i.i.d. Type I Extreme Value [McFadden, 1974], giving the standard class-conditional
logit
sij|c = exp(uijt|c) exp(V0) +∑ ℓ∈Jt exp(uiℓt|c),(4)
where V0 is a scalar outside-good utility shared across classes, calibrated by bisection below.
The within-class systematic utility decomposes into a price channel, a taste channel, an
endogeneity correction, and a class-specific intercept,
uijt|c =α c(di)pjt +
[
rc i +δ m
]⊤
tc j +γ c ˆλj +b c,(5)
whered i∈R 64 is the pre-trained user embedding andxj is the pre-trained item feature vector,
both from the three-tower model in Section 3. The raw item featurexj is the 64-dimensional
three-tower item vector for the five non-Dress categories in Section C, and the 576-dimensional
concatenation of that same three-tower vector with the 512-dimensional raw FashionCLIP
vector for the Dress master (Section 5 footnote). The scalar interceptbc is a learnable
class-specific bias estimated jointly with the networks; because the outside-good utilityV0 is
shared across classes,bc is what lets each class have its own effective inside-vs-outside tilt.
Price sensitivity is a class-specific neural function of the user embedding,
αc(di) =−softplus
(
MLPc α(di) ) −0.1.(6)
MLPc α is a small feedforward network [Goodfellow et al., 2016]12 with one hidden layer of width
64. The softplus-and-negate wrapper13 enforces the law of demand (αc < 0) without a hard
cutoff that would break gradient-based training. The trailing−0.1floor keeps|αc(di)|≥ 0.1
for every consumer, which keeps the Bertrand-Nash markup inversion well conditioned even
when the price signal is weak.
The class-c user taste projection compresses the user embedding into aKrank = 16taste
bottleneck,
rc i = MLPc r(di)∈R 16,(7)
and the class-c item taste projection lives in the same bottleneck, unit-normalised on the
sphere,
tc j = MLPc t(xj) ∥MLPc t(xj)∥∈R 16.(8)
12A feedforward network passes the input through a chain of linear transformations with nonlinear squashing
functions in between, from input to output with no loops back. The “small” here is literal: one hidden layer
of width 64.
13softplus(x) = log(1 +e x)>0; negating enforcesα c <0smoothly.
16

The two MLPs compose into theβ-net, whose class-c scalar taste match between consumeri
and productjis
βc(di,xj) :=r c⊤ i tc j = MLP c r(di)⊤ MLPc t(xj) ∥MLPc t(xj)∥,(9)
and this scalar is the taste channel that enters Equation (5). The unit-norm constraint on
tc j is a design choice that forces the price channelαc(di)pjt, not the taste channel, to carry
price-correlated variation; without it, the taste inner product could absorb price information
by scaling its own norm, which would attenuateαc toward zero (see Compiani and Kitamura
[2016] on the broader mixture-identification literature).
A shared monthly taste shiftδm∈R 16 rotates which latent taste directions attract demand
in each calendar month, under a low-rank factorisation,
δm =Wz m, W∈R 16×8,z m∈R 8,
12∑
m=1
zm =0.(10)
The zero-sum constraint onzm identifies the seasonal shift against the static user tasterc i.
The rank-8 basis is shared across months to avoid overfitting on the single year of pre-COVID
data.
The termγcˆλj is the Petrin and Train [2010] control-function correction for price endogeneity.
ˆλj is a per-product pricing residual (the cross-sectional component of price the item embedding
cannot explain, treated as a proxy for unobserved quality), loaded back into utility with a
class-specific coefficientγc so each latent type absorbs its own share of the price-correlated
quality signal. See Section A for the construction and robustness to linear and nonparametric
CF specifications.
Consumers are assigned to one of two classes with constant mixture weightsπ1 andπ2 = 1−π1,
estimated jointly. Demographic routing of class membership is not used; the gating is
unconditional. The unconditional choice probability mixes the two class-conditional logits,
sij =
2∑
c=1
πc·sij|c =
2∑
c=1
πc·
exp
(
uijt|c
)
exp(V0) +∑ ℓ∈Jt exp ( uiℓt|c ).(11)
Parameters are estimated by maximising the log-likelihood of observed purchases over each
consumer’s transaction historyTi,
LL=
I∑
i=1
∑
t∈Ti
log
(
si,yit,t
)
.(12)
Training uses the EM algorithm: the E step computes each consumer’s posterior class
probability given current parameters, and the M step takes one AdamW14 update on the
14AdamW is a gradient-based optimiser with decoupled weight decay, which separates the regularisation
step from the adaptive-learning-rate step and typically generalises better than plain Adam.
17

class-weighted log-likelihood. The outside-good utilityV0 is not part of the likelihood; it is
calibrated post-estimation by bisection on
1
I
I∑
i=1
J∑
j=1
sij(V0) = ˆτ= 0.04,
consistent with H&M’s3%to5%single-category online share (Section 5). A single scalar V0
is shared across both classes.
Standard errors for¯αc, the coefficient gap|¯α1−¯α2|, the mixture weightπ1, and the validation
fit metrics come from a consumer-level bootstrap withB = 10refits (Table 16), holding the
first-stage embeddings fixed. The consumer-only bootstrap undercovers relative to a full
two-stage correction that also propagates first-stage embedding noise; see Karaca-Mandic
and Train [2003], Lennon et al. [2025], Battaglia et al. [2024] for the relevant corrections
when the second-stage regressors are variables generated by a first-stage machine-learning
model. The contrastive InfoNCE loss of Section 3 structurally mirrors this log-likelihood;
see Aouad and Désir [2022], Arkoudi et al. [2023] for the formal link between contrastive
representation learning and discrete choice estimation.
4.2 Price Elasticities and IIA Departures
All derivatives are taken with respect to linear pricespj. Differentiating the mixture choice
probabilitys ij with respect topj andp ℓ gives the individual-level derivatives
∂sij
∂pj
=
2∑
c=1
πc·αc(di)·s ij|c·
(
1−s ij|c
)
,(13)
∂sij
∂pℓ
=−
2∑
c=1
πc·αc(di)·s ij|c·siℓ|c, j̸=ℓ,(14)
where sij|c is the choice probability conditional on classc. The own-price derivative is strictly
negative and the cross-price derivative is strictly positive. Substitution between two products
scales withsij|c·s iℓ|c, so products favoured by the same consumer class exhibit stronger
cross-price effects. The aggregate market share derivative that fills the Jacobian matrixJ
averages these individual effects across allIconsumers,
∂Sj
∂pℓ
= 1 I I∑ i=1 ∂sij ∂pℓ ,(15)
yielding own-price elasticityεjj = (pj/Sj)·∂S j/∂pj and cross-price elasticityεjℓ = (pℓ/Sj)·
∂Sj/∂pℓ. The standard IIA restriction of plain logit [McFadden, 1974] breaks at the aggregate
level through two channels. Heterogeneous tastes make two dresses favoured by the same
consumer group closer substitutes than dresses favoured by disjoint groups. Heterogeneous
price sensitivity across classes adds a second channel, in which highly price-sensitive con-
sumers concentrate their probability mass on specific products and generate non-proportional
substitution toward those products when prices change. Both channels have multiple sources
in this model, including the two latent classes, the consumer-level variation within each class
captured by theα-net andβ-net, and the seasonal taste shiftδm.
18

4.3 Supply-Side Markup Recovery
The markup inversion follows Berry et al. [1995] and Nevo [2001] applied to a multi-product
monopolist, which is the natural conduct for H&M pricing its own dress catalog. The firm
chooses prices to maximise static profit
π=
J∑
j=1
(pj−mcj)MS j(p),
with mcj a constant marginal cost andM total market size. The first-order condition for
product j balances the direct revenue effect against cross-product cannibalisation across the
full catalog,
Sj +
J∑
ℓ=1
(pℓ−mcℓ)· ∂Sℓ
∂pj
= 0.(16)
Defining the ownership matrixΩ (Ωjk = 1if the firm internalises the cross-effect between
products j and k; Ω =11⊤ under the multi-product monopolist baseline) and the matrix
∆ = Ω⊙ J′, provided∆ is nonsingular the markup vectorη =p−mc and marginal costs
are recovered cleanly as
η=−∆ −1S, ˆmc=p+∆ −1S.(17)
For a single-product firm (∆ diagonal), the Lerner index, which measures the markup
a firm charges above its own marginal cost as a fraction of the final price, reduces to
Lj =ηj/pj = 1/|εjj|. Given H&M’s small individual item shares, cross-tier cannibalization is
weak, rendering multi-product monopolist pricing nearly indistinguishable from independent
single-product pricing. Figure 5 sketches the inputs that feed the markup inversion.
Observed
pricesp
Estimated
demandJ
Ownership
Ω
Invert:
η=−∆ −1S
Recoveredˆmc
=p+∆ −1S
Lerner
index
Welfare
analysis
Figure 5: Markup inversion pipeline. Observed prices, estimated demand (the JacobianJ
from Section 5), and the ownership matrixΩare combined to recover unobserved marginal
costs.
19

4.4 Consumer Surplus
Applying the log-sum formula [Train, 2009], individual consumer surplus is the probability-
weighted sum of conditional expected maximum utilities,
CSi =
2∑
c=1
πc
|αc(di)|·log

∑
j∈J
exp
(
uij|c
)
+ exp(V0)

,(18)
where V0 is the outside-good utility from Equation (4), shared across classes and calibrated
once by bisection. The compensating variation from moving between market states0and1
is CVi =CS 1 i−CS 0 i; becauseV0 is held fixed across counterfactuals, theV0-induced additive
term in CSi cancels in CVi. Aggregate policy analysis evaluates the sum of changes in
consumer surplus and producer profit,∆TW=M· CV+ ∆PS.
5 Demand and Supply Estimation
I estimate the two-class latent deep logit from Section 4.1 on the dress category, restricting to
the pre-COVID window (July 2019 through January 2020) to avoid contamination from the
lockdown demand regime documented in Section 8. The estimation sample hasI = 38 918
online consumers choosing amongJ = 2034products over31weeks. The outside good utility
V0 is calibrated by bisection to a target inside shareˆτ= 0.04, the midpoint of the3%to5%
single-category online share that is a reasonable estimate for H&M dresses in this window.
Elasticity estimates are invariant to the precise choice ofˆτwhen individual item shares
remain small (Table 17 in Section A.3).
The two-class latent deep logit gives mean absolute own-price elasticity|¯ε|= 2.13and an
implied Lerner of60.6%under multi-product monopolist conduct. Validation McFadden
R2 is strongly positive on held-out weeks; Table 5 reports the point estimate alongside the
control-function robustness run.15 The remainder of this section traces where that fit comes
from. A benchmark against plain aggregate logit, random-coefficient logit, BLP with GMM
[Berry et al., 1995], and individual mixed logit is reported in Section B.
5.1 Latent Class Estimates: Taste vs Price
The model recovers two classes of roughly comparable size, with the minority slightly smaller
than the majority. Mean price sensitivity differs meaningfully across the two classes, with
the minority running nearly twice as price-elastic as the majority. Mixture weights and
class-mean price coefficients are in Table 5. The class split combines price and taste: the
price-sensitive minority shows a broader taste distribution, while the majority has a tighter
one. Within each class, individual-levelα-net outputs still vary smoothly across consumers.
15The β-net item input for the Dress master concatenates the three-tower item vector with the raw
FashionCLIP vector. The concatenation lifts validationR2 over three-tower only; see Section A.4 for the full
comparison.
20

Figure 6: Individual-level price sensitivity (left) and the dispersion of taste scores across
all products per consumer (right), split by latent class. Meanα separates the classes; taste
dispersion separates them further.
Figure 7: Own-price elasticity heterogeneity. Left, the distribution of|ˆεjj|across theJ = 2,034
dresses computed under each latent class separately. Right, the same distribution computed
within the youngest age decile (age≤23) and the oldest age decile (age≥55).
Figure 6 shows the two classes separating more sharply on taste dispersion than on price
sensitivity, so the split is primarily taste-driven. Figure 7 maps theα gap into product-level
elasticities, where the minority class runs substantially more elastic than the majority. The
same gap appears when consumers are grouped directly on the user embeddingdi into clusters
of near-identical mean age (see Figure 12 below), so the pattern reflects taste, not age.
Figure 8 shows the visual pattern behind the taste split on the dress estimation sample
itself. Each panel shows the dresses theβ-net picks as top matches at the mean consumer
embedding of one age and spending segment. The separation by age and by spending is
visible by eye.
21

Shirts Shorts
Figure 9: Younger and higher-spending shoppers prefer visibly different shirts and shorts, and
the pattern holds across categories. Rows from top to bottom: young, older, high-spending,
low-spending segments. Each row shows the top taste picks under theβ-net at that segment’s
mean user embedding.
Low spend High spend
Figure 8: Younger and higher-spending shoppers prefer visibly different dresses. Columns
group shoppers by total spending (low spend left, high spend right). Rows group shoppers by
age (younger above, older below). Each panel shows the top dress matches under theβ-net
at that segment’s mean consumer embedding.
Figure 9 repeats the same picture on shirts and shorts. Both categories sit outside the
dress estimation sample, so they serve as an external generalization check. The same age
and spending separation shows up in both. The taste dimensions are general rather than
dress-specific.
22

5.1.1 Control Function Robustness
I re-fit the same specification without the hedonic residual entering utility. Table 5 reports
the comparison. The control function makes both classes more price-sensitive, with the
minority class shift larger than the majority class shift. Signs, class ordering, the mixture
split, and the aggregate own-price elasticity ordering are preserved. Validation log-likelihood
improves modestly with the control function, so the qualitative picture does not depend on
the correction.
Table 5: Control function robustness under the576D Dress master. Same specification, seed,
and data; only the hedonic residual is dropped from per-class utility. Both columns train for
the same epoch budget.
With CF Without CF Change
¯α1 (minority, more price-sensitive)−0.211−0.198 +6.6%with CF
¯α2 (majority, less price-sensitive)−0.120−0.118 +1.7%with CF
Val NLL6.0181 6.080−0.062with CF
Val R2 +7.36% +6.40% +0.96pp with CF
π1 (minority mixture weight)0.403 0.431−0.028with CF
5.2 Heterogeneity Decomposition
To see what the two structural utility components do separately, I regress model-predicted
log market shares on the price channel and the taste channel. Each channel alone carries a
substantial share of the variance, and together they capture essentially all of it, so nothing
outside these two channels matters for the model’s aggregate predictions. Inside each price
tier, the aesthetic channel is exactly what sorts products from most- to least-preferred: among
products with identical posted prices, the actual chosen product’s aesthetic utility ranks well
above the 50% random baseline on average and is highly significant.
23

Figure 10: Within-tier aesthetic ranking. Each row shows products that share the same
posted price, ordered by theβ-net’s predicted taste utility. Price determines which tier a
product lives in, and the taste channel decides which product wins inside the tier.
Figure 10 shows that the pre-trained embeddings carry enough resolution to rank products
inside a price tier even though horizontal characteristics like price are held fixed. Price sorts
products vertically across tiers, and theβ-net sorts products horizontally inside each tier.
5.3 Substitution Structure
Aggregating the product-level cross-elasticity matrix over fourK-means clusters on the
three-tower aesthetic features gives Figure 11: an average dress loses meaningfully more to
other dresses in its own visual cluster than to dresses in other clusters. Substitution follows
look, not price tier. Most of the response to a price change still leaks out of the category
entirely; the cluster pattern describes the structure inside the residual that stays in the
category.
24

Figure 11: Substitution structure at the cluster level. Left, the column-normalized four-by-four
cross-elasticity matrix from the two-class latent deep logit. Middle, the similarity-to-elasticity
scatter on the same-price-decile pair sample. Right, the Spearman rank correlation by
similarity bin.
5.4 Consumer-Cluster Substitution
The matrix above pools every consumer in the sample. To see whether different consumers
substitute differently, I group consumers using the user embeddingdi and pick the two groups
whose substitution matrices look the most different.16 Figure 12 shows their cross-elasticity
matrices alongside the cell-by-cell difference. The difference panel makes the divergence
explicit: several product clusters attract substitution from cluster A but not from cluster B,
and one (a Divided line of cheap youth-targeted dresses) flips diagonal dominance by a factor
of four across the two consumer clusters. The model therefore picks up real taste-driven
differences across consumers that an age-only split would miss.
16Method: K-means ond i with K = 8, seed7; among the eight-cluster pairs, the pair reported here
maximises the Frobenius distance between cluster-aggregated cross-elasticity matrices across a sweep over
K∈{ 2, 4, 6, 8} and three random seeds. The pair’s Frobenius distance is3.25with cell-by-cell Pearson
correlation+0.48.
25

Figure 12: Cross-elasticity matrices for two consumer clusters obtained byK-means (K=8,
seed=7) on the user embeddingdi. Left panel: cluster A (n = 5859, mean age35.1). Middle
panel: cluster B (n = 4928, mean age37.9). Right panel: the cell-by-cell differenceB−A .
The pair was chosen to maximise the Frobenius distance between the two matrices across a
sweep overK and random seeds (selected pair:3.25Frobenius, Pearson+0 .48). The left two
panels are aggregated to eight aesthetic product clusters fromK-means on item embeddings
and column-normalized so1.0is the independence baseline; the difference panel shares row
and column clusters and is centered at0with a separate divergent scale.
5.5 Seasonal Demand Dynamics
A seasonal extension of the demand model lets the taste vector depend on calendar month
through the rank-eight shiftδm of Equation (10). Price sensitivity is not given a seasonal
component; the channel that moves with the calendar is aesthetic taste, not the price
coefficient.
5.5.1 Taste Rotation
The two-class latent deep logit identifies a monthly taste shift inside the pre-COVID estimation
window. The peak occurs in June at roughly57%of the grand-mean taste norm, and the
rotation persists through summer and fall. Figure 13 visualises the month-by-month shift in
the item clusters that gain and lose utility. Implied own-price elasticities vary across months
because δm rotates which clusters consumers attend to, and the cross-cluster spread exceeds
the cross-month spread; seasonal markdown decisions should therefore be anchored to the
taste rotation, not to a calendar of price moves.
26

Figure 13: Monthly aesthetic cluster rotation driven by the low-rank taste shiftδm =Wzm.
Each row shows, for one month, the item cluster that gains the most utility next to the
cluster that loses the most.
5.6 Markup Recovery
Applying the multi-product monopolist inversion from Section 4.3 to the latent-class demand
Jacobian gives mean Lerner index¯L = 0.606with mean marginal cost€8.92 among positive-
cost items. Of2034dresses,1897(93 .3%) haveˆmcj > 0; the remainder are cheap jersey basics
where the model estimates inelastic demand (|ε|< 1) and the pre-trained embeddings do not
provide enough differentiation to generate elastic substitution. The result is robust to the
choice of outside share: Table 17 in Section A.3 shows mean|ε| essentially unchanged across
ˆτvalues spanning the plausible single-category online share band. The recovered Lerner sits
modestly above H&M’s reported gross margin. The static Bertrand-Nash model overstates
realized margins because it assumes prices are always set at the instantaneous profit maximum,
while in practice markdown calendars and seasonal clearance pricing push realized margins
below that benchmark [Soysal and Krishnamurthi, 2012, Caro et al., 2020]. Cross-category
27

substitution beyond the dresses in the estimation sample would further moderate margins.
Figure 14: Implied costs and the revenue-versus-profit ranking. Left, mean implied marginal
cost per garment (blue) grouped by the primary fabric keyword in the product description,
plotted next to the median wholesale fabric price (grey) from industry sources, each min-max
rescaled. Right, the top three dresses ranked by total revenue (upper row) and by total profit
(lower row). The two lists barely overlap.
Figure 14 supports the inversion in two ways. The material breakdown on the left shows
that structured fabrics such as woven and satin have higher implied costs than jersey and
viscose, which are stretch materials that are cheaper to cut and sew. The model never saw
any information about materials, so the ordering is a qualitative out-of-sample check that
the implied costs line up with production economics. The revenue-versus-profit panel on the
right shows that the top sellers by revenue are not the top earners by profit, which is what
the Lerner formula implies when low-priced products have the highest elasticity and therefore
the thinnest margins.
6 Counterfactuals
6.1 Sustainability Practices
The first counterfactual tests a sustainability practice. Fast-fashion retailers face pressure
to reduce SKU counts, so I order dresses by their baseline market share and drop the
bottom quantile. I compute the profit consequences two ways. Method A holds prices at
the observed values and lets shares redistribute across the surviving items, which is the
conventional accounting used in the existing SKU-pruning literature. Method B re-solves
the multi-product Bertrand-Nash equilibrium on the retained subset using the latent-class
mixture Jacobian, so the firm is allowed to re-optimize prices on the products it keeps.
Figure 15 compares the two profit curves. A cross-category view covering the other five
categories is in Section C.
28

Under the latent-class demand model, dropping the lowest-share dresses costs the firm profit
on the observed-price path and recovers part of that loss on the re-pricing path. Method
A profit falls monotonically and convexly as the prune deepens. Method B earns a positive
re-pricing premium over Method A at every prune depth, because removing close aesthetic
substitutes lets the firm lift markups on what it keeps. The premium keeps Method B profit
positive up to a moderate prune depth and crosses the profit-neutral line near a one-third
catalogue cut. The mean retained-item price rises with deeper prunes. Figure 15 reports the
profit curves and retained-item price path.
Figure 15: Sustainability prune for dresses, ordered by baseline inside share (smallest first).
Left panel: firm profit change against prune depth under two methods. The dashed gray
line holds prices at observed values (Method A), the solid dark line re-solves the multi-
product Bertrand-Nash equilibrium on the retained subset (Method B). Method A loses profit
monotonically, from−0.01%at a2%prune to −10.94%at a70%prune. Method B earns a
re-pricing premium of roughly+1.9percentage points over Method A at every depth, which
keeps profit positive up to about a30%cut and crosses the profit-neutral line between30%
and35%. Right panel: retained-item mean price under Method B, rising from+1.07%at a
2%prune to+0.64%at a70%prune. Cross-category curves are in Section C.
6.2 Aesthetic Differentiation Collapse
The second counterfactual collapses aesthetic differentiation instead of catalogue size. I hold
the catalogue fixed and push each class’s item projections one standard deviation toward
the class-specific centroid, then re-solve the multi-product Bertrand-Nash equilibrium on
the flattened taste space. Consumer surplus barely moves and mean price drops slightly,
but firm profit collapses (a drop of41.5%). Table 6 reports the full decomposition. The
profit collapse is driven by the Bertrand-Nash markup formula. When products become
more similar in taste space, substitution inside the catalogue intensifies, and in the re-solved
system that stronger cannibalisation lowers equilibrium markups across the board. In this
model, most dress profit comes from product differences in the learned demand space, which
is the economic value of the three-tower representation in euros.
29

Table 6: Effect of collapsing per-class aesthetic differentiation by one standard deviation
toward the class-specific centroid. Dress master, J = 2,034, I = 38,918, K = 2. The
Bertrand-Nash equilibrium is re-solved on the flattened taste space. The mean within-class
item cosine similarity to the class centroid is reported separately for each latent class; both
go up because items move closer to their class centroid.
Baseline∆vs baseline
Firm profit (€per week)14 588−41.5%
Consumer surplus (€per consumer)101.85−0.16%
Total welfare (€per week)3 981 733−0.35%
Mean price18.75−1.99%
Mean within-class item cosine to centroid (class 1)0.322 +0.134
Mean within-class item cosine to centroid (class 2)0.361 +0.153
6.3 Personalized Pricing Ladder
The firm clusters consumers intoNs segments by K-means on the 64-dimensional user
embeddingd i.17 Within each segmentg with consumer setIg of sizeIg, the firm solves the
multi-product Bertrand-Nash problem
max
pg∈R J +
J∑
j=1
(pgj−ˆmcj)Sgj(pg), S gj(pg) = 1 Ig ∑ i∈Ig K∑ c=1 πcsij|c(pg),(19)
under multi-product monopolist conduct (Ω =11⊤). The first-order conditionpg− ˆmc =
−
[
Ω⊙∂ Sg/∂pg
]−1
Sg is solved numerically, and total firm profit isΠ(Ns) =∑ gIg (p⋆ g−ˆmc)·
Sg(p⋆ g). Ns = 1is uniform pricing and the finest segmentation I run isNs = 128(roughly300
consumers per cluster atI= 38 918).
The Ns = 1rung lands essentially at the static FOC baseline, confirming that the FOC-
inverted optimal uniform price is close to the observed mean. Segmentation then builds
monotonically up to the finest rung atNs = 128, which caps at a profit gain of+1.234%over
uniform pricing. Most of the gain accrues in the middle rungs; the final doublings add little.
That saturation is the signature of bounded heterogeneity inα(di)within the two latent
classes: the user embedding carries a real pricing signal, but one that does not get reliably
bigger by cutting the consumer base more finely. Table 7 reports the full ladder.
17Ns is the pricing-segment count, distinct from theK = 2latent classes inside the demand model. The
segment indexgbelow is locally scoped and does not collide with the latent-class indexcof Section 4.
30

Table 7: Personalization ladder: Dress, under the canonicalK = 2latent-class deep logit
with the multi-product monopolist first-order condition solved separately inside each ofNs
K-means segments ondi. Ns is the segmentation count, distinct from theK = 2latent
classes inside the demand model.
Ns Profit gain (%) Mean price shift (%) Converged
1+0.224 +1.04 1/1
2+0.260 +0.87 2/2
4+0.511 +0.70 4/4
8+0.616 +0.90 8/8
16+0.908 +1.23 16/16
32+0.993 +1.37 32/32
64+1.011 +1.56 64/64
128+1.234 +1.75 128/128
6.4 Recommendation Validation:β-net vs Collaborative Filtering
The fourth counterfactual asks whether theβ-net is useful as a recommender in its own
right. Holding the price band fixed and training both models on the same earlier weeks, the
β-net beats a tuned collaborative-filtering baseline on items the user has never bought before.
The Recall@1018 lead is reported in Table 8 and survives every one-at-a-time perturbation
of the active-user threshold, the price-tile granularity, the held-out horizon, and all three
hyperparameters of the collaborative filter. The collaborative filter does win on items the
user already bought during training, by simply recognising past purchases, but that is a
memorisation gap, not a taste-prediction gap. Theβ-net’s user-side projectionsrc i are a
function of the pre-trained user embeddingdi alone, so it is the pre-trained taste signal by
itself that beats collaborative filtering on the new-purchase task.
Table 8: Recall@10 on the held-out weeks; both models train on the same earlier weeks.All:
every held-out purchase.Warm: items the user bought during training (memorisation slice,
N=47).Cold: items new to this user (N=730).Best of grid: the highest-cold-recall cell of
an eighteen-point tuning grid for the collaborative filter. The cold-slice lead is robust to all
sensitivity sweeps reported in the validation script’s output file.
Method all warm cold
Popularity2.2% 6.4% 1.9%
Collaborative filter, default8.0% 42.6% 6.3%
Collaborative filter, best of grid7.9% 34.0% 6.5%
β-net, mixture-weighted7.6% 10.6%7.3%
β-net, dominant-class2.8% 6.4% 2.7%
18Recall@10 is the share of a user’s held-out purchases that the model ranks among its top ten dresses for
that user, averaged across users.
31

6.5 Class-Level Taste Heterogeneity in theβ-net
Fifty synthetic dresses are generated through a vision-language design pipeline, projected
through the frozen item tower, and scored separately under each of the two latent classes.19
Figure 16 shows the six designs on which the two classes disagree most. Table 9 reports
per-design class ranks and the rank-correlation summary.
Two findings. The demand model extends cleanly to designs outside the estimation sample,
which supports generative counterfactuals on the catalogue without re-estimation. Theβ-net
recovers consumer-side aesthetic heterogeneity that the aggregate share model averages away,
so the same new product is more or less attractive depending on which latent class looks at
it.20
Design 1
 Design 2
 Design 3
 Design 4
 Design 5
 Design 6
Figure 16: The six synthetic dresses on which the two latent consumer classes disagree most
in ranking. Per-design ranks and summary rank-agreement statistics appear in Table 9.
Table 9: Class-level ranking disagreement on the six most-polarising synthetic dresses. Rank
under class 1 is each design’s position among the fifty synthetic designs under the minority,
more price-sensitive class; rank under class 2 is the position under the majority, less price-
sensitive class; lower is more preferred. The lower panel reports summary rank-agreement
statistics across all fifty designs.
Design Rank under class 1 Rank under class 2 Rank gap
Design 1 (Light Blue Solid) 6 50 44
Design 2 (Dark Green Lace) 47 6 41
Design 3 (Dark Green Lace) 48 9 39
Design 4 (Light Blue Lace) 4 38 34
Design 5 (Light Blue Lace) 14 46 32
Design 6 (Light Blue Lace) 9 41 32
Summary across allN= 50synthetic designs
Kendall-τ(class 1 vs class 2)+0.058(p<10 −3)
Mean absolute rank gap16.0positions
Maximum absolute rank gap44positions
19A vision-capable language model writes a design brief and ten categorical attribute fields; an image model
renders the design; the item tower from Section 3 maps the result to a sixty-four-dimensional unit-norm
embedding in the same space asvj. The class-c score is the inner product of that embedding with the
grand-meanβ-net output within classc.
20The disagreement is a property of the latent-class split, not of user-embedding geometry. Within any
K-means cluster ondi, ranking agreement across clusters is high on both synthetic and held-out real dresses,
while cross-class agreement is substantially lower. Full Kendall-τ values appear in the validation script output.
32

7 Hedonic Price Indices
7.1 Model
Matched-model indices track price changes for surviving products but fail when assortment
turnover is rapid. Hedonic regressions [Rosen, 1974] instead treat listed price as a function of
observable product characteristics. Listed prices respond to many forces at once, including
assortment turnover, seasonality, discounts, underlying quality and construction, input costs,
and competition, and the hedonic surface summarises how those forces are reflected in the
implicit price of each attribute. I specify the hedonic surface as
logpjt =f t(vj,hj) +εjt,(20)
where ft denotes the evaluation at montht of a single gradient-boosted tree, fitted jointly on
all months in the sample using LightGBM [Ke et al., 2017]. LightGBM is an open-source
gradient-boosted tree library optimized for large datasets. The month and year enter as
features ofh j, so the same fitted surface returns a period-specific prediction. The dress
category averages about three article-month observations per product per period, too few to
fit the 684-feature surface period by period, so pooling is a sample-size compromise rather
than a methodological preference. A gradient-boosted tree is a flexible nonlinear regressor
that builds many small decision trees in sequence, with each new tree fitted to the residual
errors of the trees before it. The feature space includes the64-dimensional pre-trained item
embeddingsv j,512raw CLIP dimensions (the same pre-trained CLIP image-text encoder
that enters the three-tower model), 100 TF-IDF text dimensions from product descriptions21,
and a small set of temporal and categorical controls, for a total of684features.
Table 10 reports the ablation. Text features carry most of the within-timeR2 gain. However,
the three-tower embeddings encode the most time-stable product properties, losing the least
predictive power in out-of-time evaluation compared to text.
Table 10: Hedonic model ablation and temporal stability
Specification FeatR 2 (in-time)R 2 (forward)R 2 loss
Baseline (cat + time)8 0.43 0.25 43%
+ TF-IDF text108 0.71 0.43 39%
+ CLIP620 0.73 0.44 40%
+ Three-tower72 0.65 0.4727%
Full (all combined)6840.720.45 39%
Figure 17 visualizes the fitted surface at the attribute level. For each color and pattern I
average the product feature vectors across every dress in that cell, feed the averaged vector
21TF-IDF (term frequency-inverse document frequency) turns a text description into a numerical vector by
counting how often each word appears in that product’s description, then down-weighting words that appear
in nearly every product. Common words like “dress” get low weight; distinctive words like “lace” or “ruffled”
get high weight.
33

through the fitted model, and read off the predicted fair-value price. Across the eight most
common colors and six most common patterns, predicted prices span EUR14.6to EUR
37.8. Lace dresses carry a consistent premium across every color, while stripe dresses sit at
the low end regardless of color. The gradients are smooth and directionally consistent with
merchandising intuition.
Solid
All over pattern
Stripe Lace
Embroidery Melange
Black
Dark Blue
White
Light Pink
Red
Off White
Blue
Light Beige
EUR 19 EUR 23 EUR 16 EUR 29 EUR 28
EUR 26 EUR 21 EUR 15 EUR 33 EUR 26 EUR 19
EUR 28 EUR 20 EUR 17 EUR 33 EUR 32
EUR 28 EUR 25 EUR 21 EUR 34
EUR 23 EUR 24 EUR 15 EUR 34 EUR 26
EUR 30 EUR 24 EUR 19 EUR 38
EUR 27 EUR 24 EUR 25 EUR 31
EUR 27 EUR 25 EUR 16
15
20
25
30
35
Predicted fair-value price (EUR)
Figure 17: Predicted fair-value dress prices by color and pattern. Cells with fewer than five
dresses are masked.
The color and pattern gradients average over all dresses of a given type. A complementary
test asks whether the same attribute edit produces the same price change for every individual
dress. Figure 18 applies four standardized edits, changing color to red, lengthening to mid-calf,
swapping fabric to glossy silk satin, and adding a small floral print, to two real H&M dresses:
a pink twill dungaree and a grey jersey T-shirt dress. Two of the four edits move in the same
direction for both dresses: length adds roughly eleven to eighteen percent, and changing to
red takes a small amount away. The other two edits reverse across the two dresses. Switching
to glossy silk satin lowers the dungaree’s predicted price by about four percent while raising
the T-shirt dress’s by about thirty-four percent, and adding a small floral print lowers the
dungaree’s predicted price by about twenty-two percent while raising the T-shirt dress’s by
about two percent. A model that treated satin or print as a fixed additive premium would
miss both reversals. The hedonic surface captures that the value of a material or pattern
depends on the rest of the dress. Satin on a dungaree looks out of place, while satin on a
dressier jersey dress looks like an upgrade, and the same logic applies to florals.
34

Original
EUR 19.84
Color
EUR 18.94  (-4.5%)
Length
EUR 23.34  (+17.7%)
Material
EUR 19.06  (-3.9%)
Pattern
EUR 15.57  (-21.5%)
Original
EUR 11.32
Color
EUR 10.81  (-4.5%)
Length
EUR 12.55  (+10.8%)
Material
EUR 15.14  (+33.7%)
Pattern
EUR 11.58  (+2.3%)
Figure 18: Image-edit counterfactuals on two real H&M dresses. Each column applies one
standardized attribute change and reports the predicted fair-value price delta relative to
the original. Two edits (length, color) move in the same direction for both dresses. The
fabric and print edits reverse: switching to silk satin and adding a floral print both lower
the dungaree’s predicted price while raising the T-shirt dress’s, showing the hedonic surface
captures attribute interactions rather than fixed additive premia.
7.2 Interpretation
The literature gives three main ways to read a hedonic regression. The first, due to Rosen
[1974] and sharpened by Ekeland et al. [2004], reads the slope of price on a feature as the
additional amount a buyer would pay for a small increase in that feature, an equilibrium
outcome of many buyers with different tastes meeting many sellers with different costs. The
standard example is the gradient of house price in floor area, which recovers what the marginal
buyer pays for an extra square metre of living space. The second tradition, running from
Court [1939] and Griliches [1961] to the handbook of Triplett [2006], treats the regression as
an accounting device. Its purpose is to hold measured features fixed so the price change of a
like-for-like bundle can be separated from shifts in the mix of products on sale. This is the
reading the United States Bureau of Labor Statistics uses when it imputes the current price
of an exiting laptop model from its features and removes quality change from the consumer
price index. A third tradition extends the second. Bajari et al. [2025] replace the hand-picked
list of characteristics with learned image and text representations for categories with rich
variety, without changing the accounting interpretation. In their application to Amazon
apparel listings, features from a pre-trained image network and a pre-trained text network
feed a hedonic Fisher price index that is then compared directly with the official consumer
price index for the same product category.
35

Our setup sits in the second and third traditions. The fitted surface is used only through its
predictions, which feed a quality-adjusted index and a decomposition in the spirit of Oaxaca
[1973] and Blinder [1973]. No coefficient or feature importance score is read as a measure
of consumer taste. The main price index uses a single fitted surface for all months, with
time entering as a feature ofhj. The Oaxaca-Blinder decomposition in Section 7.4 uses two
period-specific fits, one for each ofT1 and T2, because the decomposition explicitly compares
how implicit prices of features differ between the two windows. The pooled setup for the main
index follows Bajari et al. [2025], who fit a single multi-task network across all months of their
sample and read period-specific predictions off a shared representation. Diewert et al. [2007]
argues that period-specific imputation is preferred when characteristic prices drift across time.
An explicit stability test on our data rejects stable coefficients (p <10−4), so the pooled
model is a practical compromise. Section B.2 re-runs the index under a per-period imputation
surface and a pooled time-dummy surface and reports the range of answers. This paper does
not use the Rosen interpretation. Identifying consumer preferences is done elsewhere in the
paper through a separate choice model, not through this surface.
7.3 Price Indices and Conformal Inference
The Jevons index is the geometric mean of raw price relatives across surviving articlesMt,
Jt,t+1 =
∏
j∈Mt
(
pj,t+1
pj,t
)1/|Mt|
.(21)
TheFisheridealindexusespredictedpricesfromthepooledhedonicsurface, ˆpjt = exp( ˆft(vj, hj)),
evaluated on the set of articles common to adjacent months,Mt,t+1 =Nt∩Nt+1, together
with observed quantitiesqjt,
Ft,t+1 =
√
Lt,t+1·Pt,t+1, L=
∑
j∈Mt,t+1 ˆpj,t+1qjt ∑
j∈Mt,t+1 ˆpjtqjt
, P=
∑
j∈Mt,t+1 ˆpj,t+1qj,t+1 ∑
j∈Mt,t+1 ˆpjtqj,t+1
.(22)
The chained index isFT =∏T t=1Ft−1,t. Because predicted prices are estimated, the index is
estimated with error too. I quantify index uncertainty through split conformal prediction
[Vovk et al., 2005, Lei et al., 2018].22 A Monte Carlo stress test with500draws from out-of-fold
residuals establishes a14percentage point band on the aggregate index.
Figure 19 plots the three indices alongside the conformal band. Quality-adjusted indices show
less deflation than naive ones, and the gap widens over time. The Jevons index declines60.5%
over two years, while the embedding Fisher declines50.6%, yielding a terminal gap of9.9
percentage points. The gap stays positive at the 5th percentile of the conformal stress test,
so compositional shifts dwarf the model’s own prediction uncertainty. Section B.2 re-runs the
same index under three alternative hedonic methods from the literature; the deep multi-task
network recovers a similar Fisher decline and gap (both inside the conformal band), while
two classical five-characteristic surfaces return much larger gaps that sit outside the band.
22The idea is to set aside a fresh slice of the data, record how large the prediction errors are on that slice,
and use the empirical quantile of those errors as an honest error bar on new predictions, without assuming
anything about the shape of the error distribution.
36

2018-10 2019-01 2019-04 2019-07 2019-10 2020-01 2020-04 2020-07 2020-10
Month
20
40
60
80
100Price Index (Base = 100)
  COVID lockdown
90% conformal band (Full Fisher)
Jevons (no quality adjustment)
Categorical Fisher (R2 = 0.43)
Embedding Fisher (R2 = 0.72)
Figure 19: Chained price indices for dresses over the two-year window, with the90%conformal
band on the embedding Fisher. The matched-item Jevons overstates the true deflation by
the gap between the red and blue lines, which widens as catalogue turnover accumulates.
This pattern is not unique to dresses. Table 11 reports the same gap computed per category.
Every entry is positive. In every product category I looked at, the matched-model approach
overstates the true deflation, with the gap ranging from about 4 percentage points for blouses
to almost 30 for trousers.
Table 11: Jevons minus Fisher gap by product category
Category Gap (pp) Category Gap (pp)
Trousers29.3Shorts7.8
T-shirt22.3Blouse4.3
Top17.0Skirt8.1
Shirt16.8Vest top9.5
Sweater16.0Jacket12.8
Dress9.9
Beyond quantifying index uncertainty, the conformal band doubles as a fair-value reference
for cold-start pricing. During theT2 window,39dress articles appear that did not exist inT1.
For each new article I check whether the actual selling price sits inside the90%conformal
prediction band around the model’s fair-value estimate each month. At launch,82.0%are
already inside the band; coverage climbs with age, dips briefly at month six under the summer
markdown cycle, and reaches100%by month twelve. Figure 20 traces the trajectory for five
representative new dresses. The hedonic surface therefore prices products it has never seen
using only features observed at launch, and it predicts those prices well against eventual
market outcomes.
37

0 2 4 6 8 10 12 14
5
10
15
20
25EUR
Light Beige | Short, gently fitted dress in patterned stretch twill with a
0 2 4 6 8 10 12
10
20
30
40EUR
Dark Blue | Knee-length dress in lightly crêped satin with a V-neck, sew
0 2 4 6 8 10 12
10
15
20EUR
Grey | Short, fitted dress in soft jersey with short sleeves.
0 2 4 6 8 10 12
5
10
15
20EUR
Light Beige | Short dress in an airy viscose weave with a V-neck and butto
0 2 4 6 8 10 12
Months since launch
10
20
30
40EUR
Light Blue | Sleeveless, knee-length dress in soft, washed T encel  lyocel
Conformal band (90\%) Hedonic prediction Actual price
Figure 20: Fair-value tracking for five new dresses introduced only in theT2 window. Each
panel shows one dress: the actual selling price each month (solid line), the model’s fair-value
estimate (dashed line), and the90%conformal prediction band (shaded ribbon). The band is
about14percentage points wide. All five dresses settle inside the band within three months
of launch, consistent with the91%aggregate coverage reported in the text.
38

7.4 Decomposition
The nonlinear Oaxaca-Blinder extension23 [Bauer and Sinning, 2008] decomposes the price
decline into pure repricing (valuation) versus assortment composition. With f1 and f2
denoting the fitted surfaces for early (T1) and late (T2) time windows:
logp 2− logp 1/bracehtipupleft /bracehtipdownright/bracehtipdownleft /bracehtipupright
total
= 1 2
[
(f1
T2
−f1
T1
) + (f2
T2
−f2
T1
)
]
/bracehtipupleft /bracehtipdownright/bracehtipdownleft /bracehtipupright
composition
+ 1 2
[
(f2
T2
−f1
T2
) + (f2
T1
−f1
T1
)
]
/bracehtipupleft /bracehtipdownright/bracehtipdownleft /bracehtipupright
valuation
+ξ,(23)
wherefk
Tℓ
= ETℓ[fk(v, h)]is the average prediction of surfacefk on the articles in windowTℓ,
and ξ is a small residual that absorbs the difference between observed mean log-prices and
their hedonic predictions. This averages the two standard reference-window decompositions.
It is the Cotton average of theT1-reference andT2-reference splits, which reduces sensitivity
to the choice of reference window.
Table 12 reports the deseasonalized decomposition. The dress price decline is almost entirely
repricing, slightly offset by an improving mix. The valuation effect accounts for a16.9%drop
in prices, while the assortment composition shifted slightly (+3.0%) toward features the model
values higher. Figure 21 visualizes the same decomposition as a waterfall, and Figure 22
shows the dresses at the top and bottom of the valuation ranking. Trendy, fashion-forward
items such as pink satin, ruffled off-shoulder, and patterned summer dresses gained hedonic
value fromT1 to T2. Basics such as plain cami, simple pleated, and jersey dresses lost the
most value.
23The Oaxaca-Blinder decomposition [Oaxaca, 1973, Blinder, 1973] splits a difference in mean outcomes
between two groups into two parts. The first part is driven by differences in observed characteristics and is
called composition. The second part is driven by differences in how those characteristics are valued and is
called valuation. The nonlinear extension of Bauer and Sinning [2008] replaces the linear regressions on each
side with arbitrary fitted functions. Here those functions are the period-specific gradient-boosted hedonic
surfacesf 1 andf 2.
39

Composition
(mix shift)
Valuation
(repricing)
Total
15.0
12.5
10.0
7.5
5.0
2.5
0.0
2.5
5.0
Price change (%)
+2.8%
-15.2%
-12.9%
Figure 21: Oaxaca-Blinder waterfall decomposition of the dress log-price change between
T1 and T2. The total decline of−13.9%breaks into composition (+3.0%) and valuation
(−16.9%), which means the catalogue’s mix improved slightly, but H&M priced the same
features meaningfully lower in the second window.
EUR 6 → 6
Most resilient
Black
Val: +112.6
EUR 6 → 6
White
Val: +105.4
EUR 15 → 16
Dark Red
Val: +103.3
EUR 9 → 6
Oﬀ White
Val: +97.1
EUR 7 → 7
Black
Val: +83.9
EUR 192 → 79
Biggest losers
Oﬀ White
Val: -59.9
EUR 33 → 9
Blue
Val: -59.4
EUR 68 → 42
White
Val: -56.2
EUR 21 → 10
Greenish Khaki
Val: -55.1
EUR 17 → 7
Black
Val: -54.9
Aesthetic depreciation extremes (Variant S)
Figure 22: Dresses ranked by the per-product valuation effect from the Oaxaca-Blinder
decomposition. Top row, dresses whose hedonic value rose the most betweenT1 and T2.
Bottom row, those whose hedonic value fell the most. The pricing surface rewards novelty,
consistent with trend alignment driving value in a fashion-forward category.
40

Table 12: Oaxaca-Blinder decomposition (dresses, deseasonalized)
Total Composition Valuation
Point estimate−13.9%+3.0%−16.9%
Bootstrap90%CI [−16.0,−11.4] [−0.2,+4.1] [−16.5,−14.8]
Notes:Valuation negative in100%of200bootstrap replicates. Compo-
sition positive in92%.
8 Event Study: COVID-19 Lockdown
8.1 Empirical Framework
Indext runs over calendar dates. Indexi denotes the unit of observation: the single aggregate
series in M0, and one of twelve item clusters or ten user clusters in M1. LetYit denote daily
transaction counts for uniti on datet, and letXt collect daily covariates common to all units,
namely day-of-week dummies and a deep-discount indicator. The coefficientκp is the absolute
period-p effect in a single-series fit. The regression coefficients in §9 (κp, κtrend, νm, ζ) use
locally scoped Greek letters that do not collide with the demand-side networksαc, β-net,
γc, or δm of Section 4. Counts are fit by Poisson quasi-maximum likelihood [Gourieroux
et al., 1984, Wooldridge, 1999]. Two specifications are estimated, M0 (aggregate) and M1
(per cluster); both share the Poisson likelihood and the common covariate blockXt and differ
only in the unit of observation.
The COVID-19 lockdown hit every product and every store on March 20, 2020. Every unit
was treated on the same day, so the sample contains no untreated 2020 observations and
no control group inside the treated year.24 The lockdown effect is therefore measured by
comparing 2020 to 2019 under the assumption that the 2019 seasonal pattern would have
continued in 2020 absent the shock. The 2020 lockdown coefficient is the deviation from that
baseline. The assumption is not testable from within the sample. All estimates that follow,
including differences across item and user clusters, are conditional on it. The item and user
embeddings were trained only on pre-COVID transactions, so the embedding space itself
does not absorb the shock.25
24When every unit is treated on the same day and no never-treated unit is available, the aggregate treatment
effect is not identified without an outside assumption [Miller, 2023]. The 2019 seasonal pattern stands in as
the counterfactual for 2020. All lockdown coefficients reported below are absolute effects under that outside
assumption.
25Clustering first and regressing afterwards treats the partition as fixed, so first-stage uncertainty is not
reflected in standard errors. Two design choices limit this: theK-means partition is fit on pre-COVID data
only, andK is chosen by pre-COVID silhouette rather than by lockdown outcomes. A seed-stability check in
Section C.4 refits M1 under twenty randomK-means initialisations and finds the heterogeneity range within
ten percentage points of the main-text estimate on nineteen of twenty seeds.
41

8.1.1 Aggregate and per-cluster single-series: M0 and M1
M0 uses total daily dress transactions; the indexi is trivial (one aggregate series) and is
carried in the notation only to match M1. M1 uses per-cluster daily transactions, re-fitting
the same equation once for each of twelve item clusters and once for each of ten user clusters,
so i identifies the cluster and every coefficient below is cluster-specific. Both share the same
single-series specification,26
logE[Yit|X t] =µ 0 +κ trend·t+
12∑
m=2
νmMonthmt +
∑
p∈P
κp 1pt +ζ′Xt,(24)
where µ0 is the intercept andt∈ [0, 1]is the date index rescaled to the unit interval, so
κtrend is the log-scale change across the whole sample. The month blockMonthmt is a set of
eleven calendar-month indicators (January omitted) with coefficientsνm. The period block
1pt gives one indicator per period inP ={WHO,Lockdown,Reopening,Post-Recovery} ,
with coefficientsκp. The control block ζ′Xt loads on six day-of-week indicators and the
deep-discount indicator. The coefficients have a semi-elasticity interpretation. In particular,
exp(κp)−1is the proportional change in expected transactions during periodp relative to the
pre-shock seasonal norm. M0 delivers the category-level lockdown estimate, and M1 returns
one lockdown estimate per cluster by re-running the same specification on each cluster’s daily
count.
8.2 Heterogeneous Demand Responses
The aggregate model (M0) estimates a lockdown effect of−28.6%on daily dress transactions
(p < 0.01), and the WHO announcement period shows a−31.5%decline ( p < 0.001),
confirming that consumer responses began before formal lockdown measures.
The shock is not specific to dresses. Table 13 reports the aggregate Poisson estimate for each
of the eleven fashion categories in the H&M catalog. Occasion-wear categories (sweaters,
blouses, shirts, jackets, skirts) fall sharply. Loungewear-adjacent categories (t-shirts, shorts,
vest tops) rise. Dresses fall in between. The same within-category heterogeneity holds across
all six main product groups. Full per-category item and user cluster breakdowns appear in
Section C.
26The structural-break form with a linear time trend, calendar-month dummies, day-of-week controls, and
one indicator per post-shock period is the standard fit for a single time series with a known intervention date,
documented in the applied literature under the names interrupted time series, segmented Poisson regression,
and structural break regression [Linden, 2015].
42

Table 13: Aggregate lockdown effect by product category, from M0 (Equation (24) on total
daily counts). Column ‘Lockdown %’ reports100·[exp(ˆκLockdown)−1].
Category Lockdown % Category Lockdown %
Sweater−56.1T-shirt+14.2
Blouse−46.2Shorts+14.6
Jacket−40.2Vest top+23.9
Shirt−37.5
Skirt−33.6
Dress−28.6
Top−24.1
Trousers−6.8
A second striking aggregate fact is the collapse of in-store transactions during lockdown.
Before lockdown the store-to-online split of H&M transactions was about30/70, close to the
long-run share in the full sample. During the lockdown weeks, physical store transactions fell
to zero because every brick-and-mortar location was closed, so all activity moved online. After
reopening the split moved to34/66, with a slight permanent lift in store share relative to the
pre-lockdown baseline. The event compresses the usual retail channel mix into a pure online
channel for roughly seven weeks and then only partly reverses. The cluster-level Poisson
models below combine purchases across both channels into a single daily count per cluster, so
channel substitution enters the estimated lockdown coefficient rather than a separate control.
The store-closure mechanism is therefore part of the measured lockdown effect.
The per-cluster models (M1) reveal substantial heterogeneity across the twelve item embedding
clusters [Lloyd, 1982]. These clusters cut across the retailer’s product taxonomy rather than
aligning with it, so different kinds of dresses were hit very differently and the embedding
partition shows where the drop was largest.27
27The number of clusters,K = 12for items and K = 10for users, is chosen by maximizing silhouette
score acrossK∈{ 4, 6, 8, 10, 12, 15, 20} for items andK∈{ 4, 6, 8, 10, 12} for users, among values where every
cluster averages at least10daily transactions in a pre-COVID window of matched length (24 January to 11
March 2020). The silhouette score for a pointi is si = (bi−a i)/max (ai,b i), whereai is the mean distance
from i to other points in its cluster andbi is the mean distance fromi to points in the nearest other cluster;
it is bounded in[−1, 1]and higher is better. The pre-COVID viability filter keepsK-selection independent of
the shock and rejectsK = 15and K = 20because their smallest clusters fall below the10-per-day threshold.
43

Table 14: Lockdown impact by product cluster from M1 (per-cluster single-series, Equa-
tion (24) fit once per cluster withi indexing the cluster). Column ‘Lockdown (%)’ reports
100·[exp(ˆκLockdown)−1]for each cluster.
Segment Items Daily Txn Lockdown (%) 95% CI
Item Cluster 0600 50−38.0 ∗∗∗ [−52.8,−18.6]
Item Cluster 1608 10−1.9 [−50.6,+94.9]
Item Cluster 2639 384−53.0 ∗∗∗ [−62.7,−40.7]
Item Cluster 3572 19−40.8 ∗∗ [−56.9,−18.6]
Item Cluster 4532 186−34.7 ∗∗∗ [−45.0,−22.5]
Item Cluster 51079 533−27.3 ∗∗ [−40.7,−10.9]
Item Cluster 6820 235 +54.9 [−6.6,+157.1]
Item Cluster 71190 307−33.2 ∗∗ [−48.7,−13.0]
Item Cluster 8984 195−45.0 ∗∗ [−61.8,−20.9]
Item Cluster 91012 803−28.8 ∗∗∗ [−40.5,−14.7]
Item Cluster 10894 417−43.1 ∗∗∗ [−57.0,−24.6]
Item Cluster 111309 20−40.0 [−68.7,+15.0]
Range:107.9percentage points
Notes: Poisson QMLE with seven-day Newey-West standard errors [Newey
and West, 1987]. Daily Txn is the mean daily transaction count during
lockdown.
∗∗∗,∗∗,∗ denote significance at 0.1%, 1%, 5% after Benjamini-Hochberg
FDR correction [Benjamini and Hochberg, 1995].
Table 14 reports a107.9percentage point range across twelve embedding clusters. Womens
Tailoring falls the most; jersey-knit everyday basics carry the only positive point estimate.
Matched-K TF-IDF text clustering and H&M’s section taxonomy produce comparable raw
ranges (see Table 15 for the partition-agreement comparison). On raw variance the three
segmentations are comparable. On partition structure they are not.
Table 15 reports pairwise Adjusted Rand Index28 and Normalized Mutual Information29
between the three partitions. The embedding partition is almost orthogonal to the TF-IDF
partition and only partially aligned with H&M section labels (Table 15). Several embedding
clusters cross-cut the section taxonomy. Cluster 6 draws roughly a quarter of its items each
28The Adjusted Rand Index compares two partitions of the same items. Letnij denote the number of
items assigned to clusteri in the first partition and clusterj in the second, with row sumsai =∑ jnij and
column sumsbj =∑ inij, and totaln. The index isARI = ∑ ij ( nij 2 )−[ ∑ i ( ai 2 )∑ j ( bj 2 )]/( n 2) 1
2 [
∑
i (
ai
2 )+
∑
j (
bj
2 )]−[
∑
i (
ai
2 )∑ j ( bj 2 )]/( n 2). It equals
one for identical partitions and zero when the overlap matches chance [Hubert and Arabie, 1985].
29Normalized Mutual Information rescales the mutual information between two partitions by their average
entropy: NMI(U,V ) = 2I(U;V )/[H(U)+H(V )], whereI(U;V ) =∑ ij(nij/n) log ( nn ij/(aibj) ) is the mutual
information andH(U) =−∑ i(ai/n) log(ai/n)is the partition entropy (withH(V )defined symmetrically).
It is bounded in[0, 1], equals one for identical partitions and zero when the partitions are statistically
independent.
44

from Womens Everyday Collection, Everyday Basics, and Womens Casual, a grouping no
text-only method reproduces.
Table 15: Pairwise agreement between item-side segmentations on the Dress catalog.
Pair of segmentations ARI NMI
Embedding vs TF-IDF0.086 0.182
Embedding vs H&M section0.479 0.656
TF-IDF vs H&M section0.055 0.168
Figure 23 shows representative products from the two extreme clusters. Cluster 2 is almost
entirely Womens Tailoring, the structured officewear most exposed to office closures. Cluster 6
cross-cuts Womens Everyday Collection, Everyday Basics, and Womens Casual, and contains
jersey-knit solid-colour dresses of the kind worn at home.
Cluster 2
-53.0
(n=639)
Cluster 6
+54.9
(n=820)
Dress item clusters: representative products
Figure 23: Item-cluster view. Representative products from the two most extreme dress item
embedding clusters, ranked by the M1 estimateexp(ˆκLockdown)− 1(Equation (24)). Item
Cluster 6 (jersey-knit everyday basics,+54.9%) is the only cluster with a positive point
estimate. Item Cluster 2 (Womens Tailoring officewear,−53.0%) is the hardest hit.
Turning to consumer heterogeneity, embedding-based user clusters are estimated from the
highest-activity customer tier, whose transaction histories are sufficiently dense for reliable
continuous representation, and these clusters cleanly cross-cut traditional demographic bins.
The per-segment M1 fits give a28.4percentage point range across embedding clusters,1.80×
wider than the range across three age-based demographic segments (Figure 24). The most
and least affected embedding clusters both fall outside the demographic range, despite sharing
nearly identical age distributions.
45

40
 30
 20
 10
 0 10 20
Lockdown Effect on Daily Transactions (%)
Cluster 7
Cluster 4
Cluster 2
Cluster 1
25 40
Cluster 5
Cluster 8
Over 40
Other
Cluster 9
Cluster 0
Cluster 3
Under 25
Cluster 6
Embedding range: 30.5 pp  |  Demographic range: 17.3 pp  |  Ratio: 1.8×
Embedding cluster
Demographic segment
Not significant
Figure 24: User-cluster view. Lockdown effect per user embedding cluster (blue) and per
age-based demographic segment (red), from M1 (Equation (24) fit once per segment). Each
point is100· [exp(ˆκLockdown)− 1]. The user embedding clusters span1.80× the range of the
demographic segments.
Figure 25 plots the M1 recovery path for each user cluster across the four event periods. The
hardest-hit and most resilient user clusters diverge during lockdown and remain partially
separated through the post-recovery window, so the user-side heterogeneity is not just a
one-period anomaly.
46

WHO
Announcement
(Mar 11 19)
National
Lockdown
(Mar 20 May 5)
Reopening
(May 6 19)
Post-
Recovery
(May 20+)
-80
-40
-20
-10
0
10
20
40
80
160Effect on Daily Transactions (%), symlog
Aggregate
Cluster 0
Cluster 1
Cluster 2
Cluster 3
Cluster 4
Cluster 5
Cluster 6
Cluster 7
Cluster 8
Cluster 9
Figure 25: User-cluster view. Recovery trajectories by user embedding cluster across the four
event periods, from M1 (Equation (24) fit once per user cluster). Each line plotsexp(ˆκp)− 1
for one user cluster acrossp∈P. Shaded bands are 95% CIs.
A per-cell fit of M1 (Equation (24)) on each item-cluster by user-cluster cell yields a cell-level
lockdown range of175.9percentage points across the sufficient-volume cells. This range
exceeds both the item-only and user-only margins reported in Table 14 and Figure 24.
Figure 26 plots all cells. The cell ordering does not reduce to a rescaling of either marginal
cut.
47

Figure 26: Item× user-cell view. Lockdown effect on daily dress transactions at the item-
cluster by user-cluster cell level, from per-cell M1 fits (Equation (24) fit once per(i,j )cell
on that cell’s daily count). Each point is100· [exp(ˆκLockdown)− 1]for one of the132cells;
horizontal bars are 95% confidence intervals. Green markers flag cells with positive point
estimates. The dashed vertical line and light grey band mark the aggregate M0 estimate
(−28.6%) and its 95% CI. The cell-level spread is wider than either the item-only (107.9pp)
or user-only (28.4pp) range in Table 14 and Figure 24.
Figure 27 puts product images on the two tails of the cell-level M1 distribution in Figure 26.
For each tail, three distinct item clusters are shown, each represented by its best sufficient-
48

volume cell and three items from that cluster. The display keeps the item clusters distinct so
the span of the distribution is visible as variation in product type.
Figure 27: Item × user-cell view. Tail cross-cells from the per-cell M1 distribution in
Figure 26, shown as product images. Left panel: three distinct item clusters whose best
sufficient-volume cell is most positive. Right panel: three distinct item clusters whose best
sufficient-volume cell is most negative. Each row shows three items from the named cluster;
the label above each row gives the item cluster, the user cluster, and100· [exp(ˆκLockdown)− 1]
from the cell-level M1 fit.
User Cluster 6 has the least-negative row average in the cross-cell panel; the remaining rows
sit deeply negative. UC6 is a young cohort skewed toward ladies’ dresses. Within this row,
the jersey-knit everyday basics cluster shows a positive point estimate while the Womens
Tailoring cluster is deeply negative. The pattern is not visible from the item-only or user-only
cut alone. Several cross-cell estimates rest on fewer than fifteen daily transactions with
confidence intervals that cross zero, and are not interpreted individually.
9 Discussion and Conclusion
9.1 Implications
For retailers, the value of the representation learning framework is aesthetic segmentation,
which identifies which products appeal to which consumer classes and enables targeted
assortment decisions. The two latent classes differ meaningfully in price sensitivity, with
the minority class substantially more responsive to markdowns than the majority. The
classes also separate along taste dimensions, so the retailer can potentially gain from both
49

class-targeted assortment and class-differentiated pricing. Seasonal timing dominates seasonal
pricing. The low-rank monthly taste rotationδm shows the aesthetic direction of demand
shifting noticeably during the spring collection turnover, so assortment timing, not price
timing, is what moves with the calendar.30 The hedonic composition bias implies that retailers
calibrating markdown timing to matched-item price indices will systematically mistime their
interventions.
For industrial organization theory, the logit specification imposes the Independence of
Irrelevant Alternatives conditional on class membership, but the two-class latent formulation
generates substantial market-level departures. Substitution patterns depend on class shares, so
a price increase drops demand onto products favoured by the same class rather than dispersing
symmetrically. Encoding visual similarity in the choice probabilities turns latent taste
heterogeneity into an aggregate-level relaxation of the IIA restriction. On the measurement
side, contrastive pre-training on purchase records recovers economic structure, and the three-
tower embeddings act as sufficient statistics for unobservable preferences across several disjoint
applications. The near-zero Adjusted Rand Index between embedding-based behavioural
clusters and traditional demographic segments confirms that the learned representations
capture dimensions orthogonal to age and income.
9.2 Limitations
The analysis uses data from a single retailer in one market segment over two years, so
the specific estimates are not portable without replication across retailers, categories, and
market structures. Price is the dominant predictor of demand but not a purely causal
estimate, since identification rests on a hedonic control function rather than an exogenous
cost-shock instrument. The outside option is calibrated by bisection rather than jointly
estimated, because session-level logs recording non-purchases are not in the data. Choice-
model parameters come with consumer-bootstrap standard errors (Table 16); a full two-stage
bootstrap that also propagates first-stage embedding noise is left to future work. Rival
retailers are absorbed into the outside option rather than modelled as best-response players.
The data does not record fit or per-size availability, and survey evidence ranks fit as the most
valued attribute in fast-fashion purchases, ahead of price and trend [de Kok, 2022, Van der
Kwaak, 2009, Leinenga, 2019]. A non-purchase cannot be separated into a taste rejection, a
price rejection, or a stock-out in the customer’s size. The taste sensitivity network therefore
encodes a bundle of aesthetic preference and item availability rather than pure aesthetic taste.
Session-level logs linked to real-time size-level inventory would be needed to separate these
channels cleanly.
9.3 Future Research
Several extensions would address these limitations and expand the framework. The most
direct path forward is a richer supply-side specification. The current static Bertrand-Nash
30The seasonal demand extension uses a low-rank monthly taste rotation and does not add a seasonal
component to the price coefficient; the master latent-class model holdsαc fixed across months.
50

assumption recovers a multi-product Lerner index modestly above H&M’s reported gross
margin, qualitatively consistent with the monopolist conduct assumption. The static model
overstates realized margins because it treats every price as an instantaneous profit maximum,
while in practice markdown calendars and seasonal clearance push realized margins below
that benchmark. A dynamic pricing extension that models inventory clearance and markdown
timing could close this gap by accounting for intertemporal substitution.
Extending the framework also requires a deeper understanding of cross-category substitution
and budgeting behaviour. The current choice set is restricted to dresses, which implicitly
assumes out-of-category substitution behaves exactly like the outside good. Accounting for
complementary purchases (such as buying a dress and matching shoes) and broader wallet
constraints would naturally lower aggregate elasticity, expand margins, and better match
observed retail behaviour.
A Choice Model Robustness
A.1 Control Function
As a first-stage check for price endogeneity I follow the control-function approach of Petrin
and Train [2010] and add the per-product hedonic residualˆλj = logpj−ˆg(vj)to the utility
specification, where logpj is the mean log price of productj over all weeks it sells and
ˆgis a five-fold cross-validated LightGBM regression of mean log price on the three-tower
item embeddingvj. The residual captures the cross-sectional component of price the item
embedding cannot explain and is constant within each product. Two variants are tested, a
linear control and a nonparametric MLP. The price coefficientˆαis stable across both, and
the control-function coefficient is economically small.
A.2 Consumer Bootstrap
To check whether the estimates in Section 5 are stable at the sample size used, I refit the
demand model on ten consumer bootstrap draws of the estimation panel. Table 16 reports
the bootstrap mean and standard error for the class-mean price coefficients, the mixture
weight of the more price-sensitive class, and the validation fit metrics. All ten refits reach
early-stopping convergence under EM without class collapse. The standard errors are small
on every row, and the gap between the two class-mean price coefficients sits many standard
errors above zero. The full-sample numbers cited in the main text are therefore stable at this
sample size rather than an artefact of a single optimisation draw.
51

Table 16: Consumer-bootstrap standard errors for the Dress demand model,B = 10draws of
the 38,918 consumers sampled with replacement. Inside each replicate the two classes are
reordered so the more price-sensitive one is labelled class 1.
Bootstrap mean Bootstrap SE
¯α1 (minority, more price-sensitive) -0.216 0.004
¯α2 (majority, less price-sensitive) -0.124 0.003
|¯α1−¯α2|0.093 0.003
π1 (mixture weight of more price-sensitive class) 0.402 0.010
Val NLL 6.10 0.02
ValR 2 +6.10% +0.34%
A.3 Outside-Good Calibration Sensitivity
The demand model calibrates the outside-good utilityV0 by bisection to a target inside share
ˆτ= 0.04(Section 5). The robustness sweep coversˆτ∈[0.02, 0.30], bracketing the plausible
single-category online share range. Across this range mean own-price elasticity moves by less
than5%, mean Lerner shifts by roughly39percentage points, and the fraction of positive
marginal costs falls from94.1%to61 .0%. Only the level of the recovered markup is sensitive
to the outside-good calibration. Table 17 reports the full sweep on the demand-side primitive.
Table 17: Sensitivity of recovered marginal costs to the calibrated outside shareˆτunder the
two-class latent deep logit. All specifications use multi-product monopolist conduct (Ω =1).
The outside good utilityV0 is calibrated via bisection.
ˆτ V 0 Mean|ε|Mean ˆmc(€) MeanL ˆmc>0
0.0214.44 2.122 9.42 0.579 1913/2034
0.0413.62 2.128 8.92 0.606 1897/2034
0.0613.11 2.134 8.46 0.632 1870/2034
0.0812.72 2.140 8.01 0.658 1853/2034
0.1012.41 2.146 7.56 0.683 1834/2034
0.1511.80 2.160 6.43 0.748 1772/2034
0.2011.32 2.174 5.24 0.817 1645/2034
0.3010.55 2.204 2.59 0.972 1240/2034
Table 18 turns the sweep into welfare deltas from the aesthetic-collapse counterfactual. The
profit drop stays between36%and44%across the five calibrations, so this within-model
result does not hinge on the outside-good choice.
52

Table 18: Sensitivity of the aesthetic-collapse counterfactual to the outside-good calibrationˆτ,
under monopolist ownership. Class-specific item projections are pulled one standard deviation
toward the class centroid.∆Profit is percent of baseline firm profit;∆CS per consumer is
percent of baseline mean consumer surplus. Baseline PS grows withˆτbecause a larger inside
share scales the weekly profit pool. Theˆτ= 0.04row is the paper’s main-text baseline.
ˆτBaseline PS (€)∆Profit∆CS/i
0.028282−43.94−0.08
0.0414 588−41.46−0.16
0.0628 249−39.48−0.25
0.0839 548−37.80−0.33
0.1051 645−36.34−0.42
A.4 Alternative Pre-trained Item Features
We assess whether the demand and markup estimates for the Dress category depend on the
choice of pre-trained item feature. The main analysis uses the576-dimensional concatenation
of our three-tower64D item vector and the512-dimensional raw FashionCLIP vector (Section 5
footnote). We re-estimate the same two-class mixture demand model, with the same sample,
hyperparameters, and random seed, under two ablations that drop back to one channel at a
time. The first replaces the three-tower vector with FashionCLIP, a 512-dimensional image-
and-text matching model fine-tuned on around 800,000 products from the Farfetch retail
site, fed directly into the demand model. The second uses the576-dimensional concatenation
of the two vectors. Table 19 reports the main fit, demand, and supply quantities, together
with correlations of mixture-weighted item-taste-network scores across the three variants.
The class structure and the supply-side markup summary are close across specifications.
Item-level taste scores correlate less tightly, so the three models produce distinct item-by-item
rankings while agreeing at the aggregate level. The paper’s main Dress conclusions rest on
aggregate elasticities and markups, not on item-by-item rankings, so they do not depend on
the three-tower pre-training choice in particular.
53

Table 19: Dress demand and supply estimates under three pre-trained item features.
Three-tower FashionCLIP Concatenation
64D (legacy) 512D direct64+512 = 576D(main)
Demand fit
Validation negative log-likelihood6.1279 6.0408 6.0181
Validation McFaddenR2 +5.67% +7.03% +7.36%
Parameters in the item taste network41 474 156 162 172 546
Demand class structure
Mean price coefficient, class 1 (¯α1)−0.164−0.200−0.211
Mean price coefficient, class 2 (¯α2)−0.119−0.119−0.120
Share of class 1 consumers (π1)0.363 0.449 0.403
Supply (Bertrand-Nash,ˆτ= 0.04, monopolist)
Mean absolute own-price elasticity2.09 2.13 2.13
Mean Lerner index0.621 0.606 0.606
Share of products withmc>0 0.915 0.933 0.933
Cross-elasticity departure from IIA0.683 1.043 1.043
Agreement with 64D reference
Per-item taste-score correlation, Pearson1.000 0.743 0.791
Per-user taste-score correlation, Pearson1.000 0.760 0.895
Per-item taste-score correlation, Spearman1.000 0.713 0.767
Column 3 (576D concatenation) is the main specification for Dress; column 1 (three-tower 64D) is retained as a legacy
robustness comparison. All three columns report post-V0-fix supply quantities under their respective LC artifacts.
Agreement rows correlate each variant’s mixture-weighted item-taste-network score against the three-tower 64D reference,
aggregated per item and per user.
B Alternative Estimators
B.1 Demand
Table 20 benchmarks the two-class deep latent class against four classical alternatives on the
same J = 500top-selling-dress,31-week pre-COVID panel. 31 The alternatives are a plain
aggregate logit, a random-coefficient logit by simulated maximum likelihood, the Berry et al.
[1995] GMM estimator with differentiation instruments following Gandhi and Houde [2020]
and the Conlon and Gortmaker [2020] checklist, and an individual mixed logit by simulated
maximum likelihood. Rows one and three collapse the price coefficient toward zero because
per-product shares of order10−4 dominate the share inversion, and the single-firm Bertrand-
Nash inversion returns negative marginal costs on every product. The random-coefficient
SML estimator recovers an economically meaningfulˆαwith positive marginal costs on 90%
31The deep-logit row in this benchmark uses the 64-dimensional three-tower item features to match
the PyBLP comparison panel. The main-paper Dress LC master in Section 5 uses the 576-dimensional
concatenation of three-tower and FashionCLIP as theβ-net item input; the BLP comparison is a separate
J=500 panel kept architecturally aligned with the classical estimators.
54

of products. The individual mixed logit has positive costs on 17% of products. The deep
latent class recovers a mean price coefficient roughly two orders of magnitude larger than the
classical aggregate rows and positive marginal costs on essentially every dress. The classical
specifications cannot support the individual-level counterfactuals in Section 6 because they
do not map an observed consumer to a specific(αi,ri)pair.
Modelˆα|ε|mc>0Lerner NLL/obs
Plain aggregate logit -0.01 0.11 0% +11.85 6.50
RC aggregate logit -0.12 2.16 90% +0.60 7.77
BLP with PCA features -0.02 0.40 1% +3.27 6.50
Individual mixed logit -0.04 0.73 17% +1.79 6.50
Deep latent class -0.18 3.13 98% +0.42 7.11
Table 20: Five demand models on the dress category. All rows use the sameJ = 500
top-selling-dress panel over31pre-COVID weekly markets. Rows 1 to 4 use16principal-
component features; row 5 uses the full64-dimensional item embedding with individual
purchase records. ˆαis the mean price coefficient per euro.|ε| is the mean-α own-price
elasticity at mean prices. mc>0is the fraction of products with positive inferred marginal
cost under the single-firm Bertrand-Nash inversion. Lerner is the mean implied markup as a
share of price. NLL/obs is per-inside-purchase conditional log loss on the held-out validation
set.
B.2 Hedonic
The composition-gap headline in Section 7 uses a LightGBM hedonic surface. To check that
the choice of surface is not driving the result I re-estimate the same monthly-chained Fisher
index on the same Dress sample under three alternatives: the pooled time-dummy hedonic
of Court [1939], Griliches [1961], the per-period imputation of Diewert et al. [2007], and a
deep multi-period network following Bajari et al. [2025]. Table 21 reports the comparison.
LightGBM and the deep network agree that the quality-adjusted Fisher decline sits between
−50%and −60%and that the Jevons-minus-Fisher composition gap is in the single digits.
The disagreement between the two stays inside the14percentage-point conformal band
reported in Section 7. The two classical five-characteristic rows explain under40%of price
variation and show gaps roughly four times larger; they stand as a thin-feature reference
rather than a competing estimate.
55

Table 21: Alternative hedonic methods for dresses, reported for the Dress category only; the
cross-category gap table in Table 11 is not re-estimated. Same sample and quantity weights
as Section 7; the Jevons index declines60.5%in every row by construction.
Method OOSR 2 Index decline Gap vs Jevons (pp)
Pooled time dummy [Court, 1939, Griliches, 1961]0.40−27.7% 32.8
Per-period imputation [Diewert et al., 2007]0.39−32.1% 28.4
Multi-price network [Bajari et al., 2025]0.67−58.3% 2.2
Paper LightGBM (Section 7)0.72−50.6% 9.9
Notes:OOS R2 is from 5-fold article-level cross-validation, quantity-weighted, for all four rows (unseen arti-
cles, not out-of-time; not comparable to the in-time and forwardR2 columns in Table 10). The LightGBM
row’s Fisher decline and gap are transcribed from Section 7; itsR2 is re-scored under the same protocol as the
other three rows and happens to coincide with the in-time figure in Table 10 to two decimal places. The pooled
time-dummy row is a fixed-base index; the other three are monthly-chained Fisher indices. The deep-network
row is the mean across three random seeds (standard deviation2.9pp on the Fisher decline and on the gap).
C Cross-Category Comparison
All six product categories (Dress, Trousers, Sweater, T-shirt, Shirt, and Shorts) are estimated
using the same three-tower embedding architecture and estimation pipeline.32 The compar-
isons test whether the structural findings from the preceding sections, which focus on Dress,
generalize across product types with different price levels, seasonal patterns, and demand
structures.
C.1 Demand Estimation
Across the six categories, theK = 2latent-class master recovers class-mean price sensitivities
between−0.24and −0.12per euro, with class-separation gaps ranging from0.00(T-shirt,
collapsed on price, split by taste only) to0.10(Shirt). Mean own-price elasticity runs from
1.17for T-shirts to2 .21for Trousers. The within-tier aesthetic percentile exceeds50for
four of five non-Dress categories, significant atp< 0.001. Table 22 reports the per-category
estimates.
32For Dress, theβ-net item input in the latent-class demand master concatenates the 64-dimensional
three-tower item vector with the 512-dimensional raw FashionCLIP vector (see Section 5 footnote). The
other five categories use the 64-dimensional three-tower item vector only. All six use the same three-tower
user embedding and price tower, and the same R3.2K= 2unconditional-gating specification.
56

Table 22: Demand model estimates across product categories.
Scale Price (K= 2LC master) Val NLL Decomposition
CategoryI J¯α 0 ¯α1 π0 |¯ε|Static TimeR 2(p)R 2(aes)WT%
Dress‡ 38 918 2034−0.211−0.120 0.403 2.13– –0.518 0.437–
Trousers68 757 1818−0.142−0.124 0.355 2.21 11.18 10.65 0.929 0.012 62.8 ∗∗∗
Sweater22 808 1011−0.191−0.139 0.539 1.85 5.53 6.12 0.850 0.141 47.9
T-shirt26 053 1367−0.210−0.210 0.375 1.17 5.58 5.69 0.730 0.282 65.1 ∗∗∗
Shirt4420 496−0.244−0.143 0.374 1.91 6.76 6.10 0.930 0.010 56.6 ∗∗∗
Shorts11 693 1029−0.228−0.144 0.335 1.50 8.38 8.35 0.801 0.242 55.9 ∗∗∗
Notes: I = consumers,J = products in theK = 2LC estimation sample (prep_phase3, pre-COVID
window 2019-07-01 to 2020-02-02,T = 31weeks). ¯α0, ¯α1 = class-mean price sensitivities (EUR−1)
from theK = 2LC master; π0 = unconditional class-0mixture weight (π1 = 1−π 0). |¯ε|= mean
own-price elasticity from theK = 2LC master. Val NLL Static and Time are retained three-tower
MNL diagnostics on the full sample and are notK = 2LC numbers. R2(p)and R2(aes)= share of
predicted market share variance explained by price and aesthetic components respectively. WT% =
within-tier aesthetic percentile (50 = no discrimination).∗∗∗ p<0.001.
C.2 Hedonic Pricing
The gap between the Jevons and hedonic Fisher indices runs from9.9percentage points for
Dress to29.3percentage points for Trousers. The hedonic fit stays within a narrow band,
R2 between0.57and0 .74. The gap is positive for all six categories. Table 23 reports the
per-category values.
Table 23: Hedonic price indices across product categories.
CategoryR 2 Jevons↓Fisher↓Gap (pp)
Dress0.72 60.5% 50.6% 9.9
Trousers0.68 58.8% 29.5% 29.3
Sweater0.69 51.6% 35.6% 16.0
T-shirt0.62 46.8% 24.6% 22.3
Shirt0.71 60.2% 43.3% 16.8
Shorts0.64 44.0% 36.3% 7.8
Notes: R2 = hedonic regression fit. Jevons and
Fisher columns report cumulative price decline over
the sample period. Gap = composition bias (Jevons
− Fisher). Positive gap means the naïve index over-
states true price decline.
C.3 Lockdown Event Study
Aggregate lockdown effects run from−56.1%for Sweaters to+14.2%for T-shirts. Item-cluster
ranges span14.6to144 .4percentage points, user-cluster ranges10.6to55 .9percentage points.
57

The ratio of user-cluster range to demographic-group range runs from0.5× to1 .8×. The
Adjusted Rand Index between embedding clusters and age groups sits near0.03for every
category. Table 24 reports the full set.
Table 24: COVID-19 lockdown effects across product categories.
Item clusters User clusters
Category AggregateKRange (pp)KRange (pp) User/Demo
Dress−28.6% ∗∗∗ 12 107.9 10 28.4 1.8×
Trousers−6.8% n.s.15 82.5 6 25.5 0.9×
Sweater−56.1% ∗∗∗ 8 55.3 4 10.5 1.0×
T-shirt+14.2% ∗ 15 152.1 10 53.9 1.1×
Shirt−37.5% ∗∗∗ 10 201.8 6 32.1 1.7×
Shorts+14.6% n.s.4 147.0 4 47.3 0.5×
Notes:Aggregate = Poisson QMLE average treatment effect.K = number of
embedding clusters. Range = spread between most positive and most negative
cluster effects (percentage points). User/Demo = ratio of embedding-cluster
heterogeneity range to demographic-group heterogeneity range.∗ p< 0.05;∗∗∗
p<0.001; n.s. = not significant.
C.4 Post-Clustering Robustness for the Heterogeneity Range
The per-cluster range of lockdown coefficients reported in Section 8 depends on one K-means
partition of the Dress item embeddings atK = 12. A standard concern with any two-step
estimate that first clusters and then tests is that the partition is itself estimated, and the
second-stage regression treats it as fixed. To check whether the heterogeneity finding is an
artifact of a single favorable seed, I re-estimate the partition under twenty different K-means
initialisations, refit M1 (per-cluster Poisson QMLE with Newey-West standard errors) on
each resulting assignment, and record the range of lockdown coefficients across the twelve
clusters for each seed. The main-text value of107.9percentage points is the seed-42 estimate.
Figure 28 plots the distribution of the range across the20seeds. Mean range is103 .4
percentage points with standard deviation10 .2. The 5th-to-95th percentile interval is
[90.4, 111.0]. The main-text point estimate sits inside this interval. Nineteen of twenty seeds
give ranges between91and115percentage points; the one outlier seed (range63) corresponds
to a K-means local minimum that merges two of the occasion-wear clusters. The heterogeneity
finding is not an artifact of a single favorable initialisation.
58

Figure28: DistributionoftheM1heterogeneityrangeacross20randomK-meansinitialisations
on the pre-COVID item embeddings atK = 12. The dashed red line is the main-text point
estimate; the green line is the seed-average.
The check varies the K-means initialisation but not the embedding stage or the item sample.
A fuller treatment would bootstrap the item sample, re-train the embeddings, and re-estimate
the partition on each draw before refitting M1. The narrower seed check rules out one of the
two first-stage concerns.
D Embedding Validation
Before running any quantitative diagnostics, Figure 29 shows what a single item embedding
looks like side by side with the raw categorical information the dataset records for each
product. Each dress has only three recorded attribute fields in the raw data, pattern, color,
and product group, which is the kind of input a standard hedonic regression or a demand
model with categorical fixed effects would use. The learned 64-number embedding spreads
the differences between dresses across many dimensions instead of collapsing them into a
small set of named categories.
59

Dress 1
 Dress 2
 Dress 3
 Dress 4
Hand-coded attributes
Pattern Color Group
Dress 1 Solid Black Jersey Basic
Dress 2 All over pattern White Jersey Fancy
Dress 3 Jacquard Off White Studio
Dress 4 All over pattern Turquoise Ladies
Learned embeddingvj∈R 64
Dress 1
Dress 2
Dress 3
Dress 4
Figure 29: What the 64-dimensional item embedding looks like compared with the hand-coded
product attributes available in the raw data. Four representative dresses are shown at the
top. The bottom-left panel lists their three recorded attribute fields, which is the kind of
input a hedonic regression or a demand model with categorical fixed effects would use. The
bottom-right panel shows the same four dresses as rows of a heatmap, with each column
being one of the 64 learned dimensions. The embedding spreads fine aesthetic distinctions
across many dimensions instead of forcing them into a short list of named categories.
For the embeddings to be useful downstream, they must encode economically meaningful
spatial structure. Figure 30 illustrates this by tracing a straight path between the two most
dissimilar dresses in the space.
60

Figure 30: A path through the64-dimensional dress embedding space.Top:A PCA
projection33 of all5870dress embeddings (gray dots). The nine interpolation dresses are
highlighted as a colored path from blue (Dress A) to red (Dress B), with thumbnail images
at each stop.Bottom:Starting from Dress A (a yellow printed dress, cosine= 1.00), each
column shows the actual dress nearest to an evenly-spaced interpolation point along the
straight line toward Dress B (a black strap dress, cosine=−0.74). The cosine similarity to
Dress A falls from1.00to −0.74across the nine columns, tracing how the model’s notion of
visual similarity shifts continuously from one aesthetic extreme to the other.
K-Means clustering34 [Lloyd, 1982] withk = 4on5870dress items confirms this structure.
The learned embeddings group dresses by how they actually look rather than by their product
codes. Figure 31 plots a t-SNE projection35 [van der Maaten and Hinton, 2008] of the
embeddings with cluster assignments, and Figure 32 shows representative items. The clusters
group visual styles (e.g., solids versus all-over patterns) that traverse product categories.
34K-Means partitions items intok groups by iteratively assigning each item to its nearest group center and
recomputing each center as the mean of its assigned items. The algorithm repeats until assignments stop
changing.
35t-SNE (t-Distributed Stochastic Neighbor Embedding) projects high-dimensional data into two dimensions
while preserving local neighborhood relationships. Items that are close together in the original 64-dimensional
space tend to appear close together in the 2D picture.
61

Figure 31: t-SNE projection of item embed-
dings with K-Means (k= 4).
Figure 32: Representative product images
from the four clusters.
The user tower encodes purchase behaviour orthogonal to observed demographics. The
Adjusted Rand Index between embedding-based user clusters and age-based demographic
segments is near zero (0.047).36 Standard demand models attribute whatever variation
demographics fail to capture to unobserved taste shocks. The user embeddings capture this
behaviour systematically, mapping consumers with diverging aesthetic tastes into distinct
spatial segments even when their observed demographics are identical.
Table 25 reports quantitative diagnostics for the embeddings, focusing on cluster concentration
and out-of-sample predictive power. Panel A details the cluster profiles and shows the extreme
skew in demand, with Cluster 0 dominating transactions (53.0%) despite containing only
20%of the products. Panel B validates the value of contrastive training over zero-shot
representations. In regressions predicting article-level log market shares, the64-dimensional
three-tower embeddings outperform the raw512-dimensional CLIP baseline, achieving an
OLSR 2 of0.48versus0.21.
36The Adjusted Rand Index measures agreement between two groupings of the same items. It equals 1
when both groupings are identical and is near 0 when overlap is no better than chance.
62

Table 25: Quantitative Validation of Item Embeddings
Panel A: Cluster Profiles for Dresses (N= 5870)
ClusterNModal Color Modal Pattern Mean Price Sales %
01169Black Solid 0.0358 53.0
11740Dark Blue All over pattern 0.0219 4.7
21736Black Solid 0.0560 13.1
31225Black All over pattern 0.0277 29.1
Panel B: Predictive Performance on Downstream Outcomes
Feature SetR 2 for Log SharesR 2 for Log Prices
OLS LightGBM OLS LightGBM
Raw CLIP (512D) 0.21 0.39 0.60 0.71
Three-Tower Embeddings (64D) 0.48 0.48 0.58 0.65
Note: Panel A uses K-Means (k = 4). Mean Price is normalized transaction
price; Sales % is the cluster’s share of total category volume. Panel B tests
article-level predictions on an 80/20 train-test split, with both linear OLS and
a gradient-boosted decision tree fit via LightGBM [Ke et al., 2017]; a gradient-
boosted tree builds many small decision trees in sequence, each correcting the
residuals of the ones before it. The 64D Three-Tower embeddings achieve
superior share prediction, while structural design appropriately suppresses their
price predictivity. The Dress LC demand model in Section 5 consumes both
representations jointly as a576D concatenation; Panel B here documents their
individual share-prediction power, which motivates retaining three-tower as the
distilled signal.
The log price regressions in Panel B show the three-tower item embeddings still predict price
about as well as the raw image features (R2 = 0.58versus0 .60under OLS). The point of the
three-tower design is not that the item embedding loses all correlation with price. It is that
the item tower never sees price as an input during training, so any predictive power comes
from genuine visual and categorical features, not from a learned copy of the price signal.
That architectural separation is what the downstream demand model needs, because price
enters the utility function as its own term with its own coefficient.
E Glossary of Machine Learning Terms
This thesis uses a small set of terms from the machine learning literature that may be
unfamiliar to economists. The table below gives a plain-English explanation of each term
and the canonical reference. Terms that are already standard in econometrics (softmax, logit,
cross-validation, principal components, K-means, simulated maximum likelihood, Halton
draws) are not included.
63

Table 26: Machine learning terms used in this thesis.
Term Explanation Reference
Embedding A learned low-dimensional vector that represents a product or a
consumer. Proximityinthevectorspacecorrespondstosimilarity
in the task the model was trained on.
Mikolov et al.
[2013]
Pre-training Training a model on a large generic corpus so that it learns
broadly useful representations. The item tower in this thesis
starts from a pre-trained CLIP checkpoint.
Radford et al.
[2021]
Fine-tuning Continuing to train a pre-trained model on the target sample so
that the generic representations specialise to the task at hand.
Goodfellow
et al. [2016]
Three-tower / dual-
encoder architecture
A neural network with two or three parallel sub-networks whose
outputs are scored against each other by an inner product, rather
than being chained in series. CLIP is the prototype dual-encoder;
this thesis uses a three-tower variant.
Radford et al.
[2021]
Contrastive learning A training objective that pulls the representation of a matched
pair (for example, a consumer and a product they bought) close
together and pushes unmatched pairs apart.
van den Oord
et al. [2018]
InfoNCE loss The specific contrastive loss used in this thesis. Algebraically
equivalent to a categorical log-likelihood over the product cate-
gory, and therefore to a multinomial logit likelihood with within-
category negatives.
van den Oord
et al. [2018]
CLIP Contrastive Language-Image Pre-training. A vision-language
model that maps images and short text descriptions into a
shared vector space, trained contrastively on internet-scale image-
caption pairs.
Radford et al.
[2021]
FashionCLIP CLIP fine-tuned on fashion product catalogues. Used as an
additional 512-dimensional feature bundle concatenated with the
three-tower item vector in the dress demand master, alongside
the CLIP-based three-tower embedding.
Chia et al.
[2022]
BERT, ResNet Pre-trained text and image models used by Bajari et al. [2025] as
drop-in feature extractors for hedonic regressions. BERT returns
a vector for any short string; ResNet returns a vector for any
image.
Devlin et al.
[2019], He
et al. [2016]
Multi-layer percep-
tron (MLP)
A feedforward neural network built from a stack of linear layers
separated by elementwise nonlinearities. Theα-net and the taste
projections in this thesis are MLPs.
Goodfellow
et al. [2016]
Softplus activation The function log(1 +ex), a smooth non-negative approximation
to max(0,x ). The paper negates its output to enforceαc < 0in
the price-sensitivity network.
Goodfellow
et al. [2016]
LightGBM, gradient-
boosted trees
An ensemble of shallow decision trees, fit sequentially so that
each new tree targets the residuals of the previous ones. Used
here as the hedonic pricing surface.
Ke et al. [2017]
t-SNE t-Distributed Stochastic Neighbor Embedding. A non-linear
two-dimensional projection that preserves local neighbourhood
structure. Used onlyfor visualisingthe item embedding in figures,
never as an input to estimation.
van der
Maaten and
Hinton [2008]
Adjusted Rand Index A measure of agreement between two clusterings of the same
items, corrected for chance. Equals zero when the two clusterings
agree no better than chance and one when they are identical.
Hubert and
Arabie [1985]
64

Term Explanation Reference
Hit@K, Recall@K Retrieval accuracy metrics widely used in information retrieval
and recommender systems. Hit@K is one if the held-out item
appears in the model’s top-K list and zero otherwise, averaged
across queries. Recall@K is the fraction of relevant items that
appear in the top-Klist.
–
Adam Stochastic-gradient optimizer that adapts the step size per pa-
rameter. Used throughout this paper for neural network training.
–
Epoch One full pass through the training dataset. Training stops when
validation error stops improving.
–
Validation set A held-out slice of the data, not used for fitting, used to decide
when to stop training. Distinct from the test set reserved for
final reporting.
–
Mini-batch A small random subset of the training data used for one gradient
update. Replaces full-dataset gradients when data is large.
–
Checkpoint A saved snapshot of a neural network’s weights at a point during
training. Used for resuming, reuse, or freezing an encoder for
downstream work.
–
L2 normalisation Rescaling a vector to unit length. After this step, the inner
product of two vectors equals the cosine of the angle between
them, so magnitudes no longer influence scoring.
–
Negative sampling In contrastive training, the denominator of the loss is summed
over a random subsample of non-matching items rather than
the full set, which keeps each gradient step cheap on a large
catalogue.
Mikolov et al.
[2013]
Overfitting A model that fits training-sample noise loses accuracy on new
data. Common counters are regularisation, low-rank structure,
and validating on a held-out sample.
Goodfellow
et al. [2016]
Low-rank factorisa-
tion
Writing a matrix as the product of two narrower matrices, which
lowers the parameter count and acts as a regulariser. Used here
for the monthly taste shiftδm =Wz m.
–
EM algorithm Expectation-Maximization. An iterative procedure for fitting
mixture models: the E step computes posterior class probabilities
givencurrentparameters, andtheMstepre-estimatesparameters
weighted by those probabilities.
–
AdamW A variant of Adam (see above) that separates weight decay
from the adaptive learning-rate step. The decoupling typically
improves generalisation compared to plain Adam and is the
optimiser used in this paper.
–
Validation NLL The negative log-likelihood of the fitted model evaluated on the
validation set (see above). Lower is better; the demand model in
this paper reports validation NLL as its main held-out fit metric.
–
TF-IDF Term frequency-inverse document frequency. A text feature
that counts words in one document and down-weights words
that appear across many documents, so distinctive vocabulary
receives more weight.
–
Conformal prediction A distribution-free way to build prediction intervals with a target
coverage level, by recording prediction errors on a fresh slice and
reading off their empirical quantile.
Vovk et al.
[2005]
65

Term Explanation Reference
Silhouette score A goodness-of-clustering metric in[−1, 1]. For each point it com-
paresdistancetoown-clustermeanagainstdistancetothenearest
other cluster; higher values indicate tighter, better-separated
groups.
–
Normalized Mutual
Information
A measure of agreement between two clusterings that rescales
their mutual information by the average entropy of the two
partitions. Bounded in[0, 1]; equals one for identical partitions.
–
Variational inference An approximate method for fitting probabilistic models with
unobserved variables. The exact posterior is replaced with the
closest member of a tractable family, which is optimised instead.
–
Poisson QMLE Poisson quasi-maximum likelihood. Consistent for the condi-
tional mean of a count outcome even when the variance does
not equal the mean, with sandwich standard errors handling
overdispersion.
Gourieroux
et al. [1984]
Oaxaca-Blinder
decomposition
Splits a mean outcome gap between two groups into a composi-
tion part (differences in observed characteristics) and a valuation
part (differences in coefficients on those characteristics). The
nonlinear extension replaces linear regressions with any fitted
function.
Oaxaca [1973],
Blinder [1973],
Bauer and Sin-
ning [2008]
66

References
Hammaad Adam, Pu He, and Fanyin Zheng. Machine learning for demand estimation in
long tail markets.Management Science, 70(8):5040–5065, 2024.
Ali Aouad and Antoine Désir. Representing random utility choice models with neural networks.
arXiv preprint arXiv:2207.12877, 2022.
Ioanna Arkoudi, Rico Krueger, Carlos Lima Azevedo, and Francisco C. Pereira. Combining dis-
crete choice models and neural networks through embeddings: Formulation, interpretability
and performance.Transportation Research Part B: Methodological, 175:102783, 2023.
Elliott Ash and Stephen Hansen. Text algorithms in economics.Annual Review of Economics,
15:659–688, 2023.
Philipp Bach, Victor Chernozhukov, Sven Klaassen, Martin Spindler, Jan Teichert-Kluge,
and Suhas Vijaykumar. Adventures in demand analysis using AI.CeMMAP Working
Paper CWP01/25, 2025. arXiv:2501.00382.
Patrick Bajari, Zhihao Cen, Victor Chernozhukov, Manoj Huber, Nikita Manziuk, Nicola
Pavanini, and Suhas Wan. Hedonic prices and quality adjusted price indices powered by
AI.Journal of Econometrics, 2025.
Laura Battaglia, Timothy Christensen, Stephen Hansen, and Szymon Sacher. Inference
for regression with variables generated by ai or machine learning.arXiv preprint
arXiv:2402.15585, 2024.
Thomas K. Bauer and Mathias Sinning. An extension of the Blinder–Oaxaca decomposition
to nonlinear models.AStA Advances in Statistical Analysis, 92(2):197–206, 2008.
Yoav Benjamini and Yosef Hochberg. Controlling the false discovery rate: a practical and
powerful approach to multiple testing.Journal of the Royal Statistical Society: Series B,
57(1):289–300, 1995.
Steven Berry, James Levinsohn, and Ariel Pakes. Automobile prices in market equilibrium.
Econometrica, 63(4):841–890, 1995.
Steven T. Berry and Philip A. Haile. Nonparametric identification of differentiated products
demand using micro data.Econometrica, 92:1135–1162, 2024.
Alan S. Blinder. Wage discrimination: Reduced form and structural estimates.Journal of
Human Resources, 8(4):436–455, 1973.
Alex Burnap, John R. Hauser, and Artem Timoshenko. Product aesthetic design: A machine
learning augmentation.Marketing Science, 42(6):1029–1056, 2023.
Felipe Caro, A. Gürhan Kök, and Víctor Martínez-de Albéniz. The future of retail operations.
Manufacturing & Service Operations Management, 22(1):47–58, 2020.
PatrickJohnChia, GiuseppeAttanasio, FedericoBianchi, SilviaTerragni, AnaRitaMagalhães,
Diogo Goncalves, Ciro Greco, and Jacopo Tagliabue. Contrastive language and vision
learning of general fashion concepts.Scientific Reports, 12(1):18958, 2022.
67

Giovanni Compiani and Yuichi Kitamura. Using mixtures in econometric models: A brief
review and some new results.The Econometrics Journal, 19(3):C95–C127, 2016.
Giovanni Compiani, Ilya Morozov, and Stephan Seiler. Demand estimation with text and
image data.CESifo Working Paper No. 10695, 2025. arXiv:2503.20711.
Christopher Conlon and Jeff Gortmaker. Best practices for differentiated products demand
estimation with PyBLP.The RAND Journal of Economics, 51(4):1108–1161, 2020.
Andrew T Court. Hedonic price indexes with automotive examples.The Dynamics of
Automobile Demand, pages 99–117, 1939.
Zeyu Cui, Feng Yu, Shu Wu, Qiang Liu, and Liang Wang. Disentangled item representation
for recommender systems.ACM Transactions on Intelligent Systems and Technology, 2020.
arXiv:2008.07178.
Vivian de Kok. Fast fashion: An insight in the most important attributes while buying
fast fashion by students from the Erasmus University. Master’s thesis, Erasmus School of
Economics, Erasmus University Rotterdam, 2022.
Melissa Dell. Deep learning for economists.Journal of Economic Literature, 63(1):5–58, 2025.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. BERT: Pre-training of
deep bidirectional transformers for language understanding. InProceedings of the 2019
Conference of the North American Chapter of the Association for Computational Linguistics,
pages 4171–4186, 2019.
W. Erwin Diewert, Saeed Heravi, and Mick Silver. Hedonic imputation versus time dummy
hedonic indexes. Working Paper 07/234, International Monetary Fund, 2007.
Robert Donnelly, Francisco J.R. Ruiz, David Blei, and Susan Athey. Counterfactual inference
for consumer choice across many product categories.Quantitative Marketing and Economics,
19(3):369–407, 2021.
Ivar Ekeland, James J. Heckman, and Lars Nesheim. Identification and estimation of hedonic
models.Journal of Political Economy, 112(S1):S60–S109, 2004.
Xavier Gabaix, RalphS.J. Koijen, RobertJ. Richmond, and MotohiroYogo. Asset embeddings.
Working Paper 33651, National Bureau of Economic Research, 2025.
Sebastian Gabel and Artem Timoshenko. Product choice with large assortments: A scalable
deep-learning model.Management Science, 68(3):1808–1827, 2022.
Amit Gandhi and Jean-François Houde. Measuring substitution patterns in differentiated-
products industries.NBER Working Paper No. 26375, 2020.
Matthew Gentzkow, Bryan Kelly, and Matt Taddy. Text as data.Journal of Economic
Literature, 57(3):535–574, 2019.
Ian Goodfellow, Yoshua Bengio, and Aaron Courville.Deep Learning. MIT Press, Cambridge,
MA, 2016.
68

Christian Gourieroux, Alain Monfort, and Alain Trognon. Pseudo maximum likelihood
methods: Theory.Econometrica, 52(3):681–700, 1984.
Zvi Griliches. Hedonic price indexes for automobiles: An econometric analysis of quality
change.The Price Statistics of the Federal Government, pages 173–196, 1961.
Xiao Han, Kanishka Misra, and Eric M Schwartz. Using deep learning to predict product
aesthetics.Marketing Science, 40(6):1117–1140, 2021.
Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Deep residual learning for image
recognition. InProceedings of the IEEE Conference on Computer Vision and Pattern
Recognition, pages 770–778, 2016.
Lawrence Hubert and Phipps Arabie. Comparing partitions.Journal of Classification, 2(1):
193–218, 1985.
Pinar Karaca-Mandic and Kenneth Train. Standard error correction in two-stage estimation
with nested samples.Econometrics Journal, 6(2):401–407, 2003.
Guolin Ke, Qi Meng, Thomas Finley, Taifeng Wang, Wei Chen, Weidong Ma, Qiwei Ye, and
Tie-Yan Liu. LightGBM: A highly efficient gradient boosting decision tree. InAdvances in
Neural Information Processing Systems, volume 30, 2017.
Jing Lei, Max G’Sell, Alessandro Rinaldo, Ryan J. Tibshirani, and Larry Wasserman.
Distribution-free predictive inference for regression.Journal of the American Statistical
Association, 113(523):1094–1111, 2018.
Mayte Leinenga. Dutch sustainable clothing consumption and the influence of materialism,
fashion clothing involvement and environmental awareness. Master’s thesis, University of
Twente, 2019. URLhttps://essay.utwente.nl/79038/.
Connor Lennon, Edward Rubin, and Glen Waddell. Machine learning the first stage
in 2sls: Practical guidance from bias decomposition and simulation.arXiv preprint
arXiv:2505.13422, 2025.
Ariel Linden. Conducting interrupted time-series analysis for single- and multiple-group
comparisons.The Stata Journal, 15(2):480–500, 2015.
Stuart Lloyd. Least squares quantization in PCM.IEEE Transactions on Information Theory,
28(2):129–137, 1982.
Lorenzo Magnolfi, Jonathon McClure, and Alan T. Sorensen. Triplet embeddings for demand
estimation.SSRN Working Paper, 2023. SSRN:4113399.
Daniel McFadden. Conditional logit analysis of qualitative choice behavior. In Paul Zarembka,
editor,Frontiers in Econometrics, pages 105–142. Academic Press, New York, 1974.
Tomas Mikolov, Ilya Sutskever, Kai Chen, Greg S. Corrado, and Jeff Dean. Distributed
representations of words and phrases and their compositionality. InAdvances in Neural
Information Processing Systems, volume 26, 2013.
69

Douglas L. Miller. An introductory guide to event study models.Journal of Economic
Perspectives, 37(2):203–230, 2023.
Aviv Nevo. Measuring market power in the ready-to-eat cereal industry.Econometrica, 69
(2):307–342, 2001.
Whitney K. Newey and Kenneth D. West. A simple, positive semi-definite, heteroskedasticity
and autocorrelation consistent covariance matrix.Econometrica, 55(3):703–708, 1987.
Ronald Oaxaca. Male-female wage differentials in urban labor markets.International
Economic Review, 14(3):693–709, 1973.
Amil Petrin and Kenneth Train. A control function approach to endogeneity in consumer
choice models.Journal of Marketing Research, 47(1):3–13, 2010.
Thomas W. Quan and Kevin R. Williams. Extracting characteristics from product images
and its application to demand estimation.R&R, RAND Journal of Economics, 2024.
Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini
Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, et al. Learning
transferable visual models from natural language supervision. InInternational Conference
on Machine Learning, pages 8748–8763. PMLR, 2021.
Sherwin Rosen. Hedonic prices and implicit markets: product differentiation in pure compe-
tition.Journal of Political Economy, 82(1):34–55, 1974.
Evgenia Rusak, Patrik Reizinger, Attila Juhos, Oliver Bringmann, Roland S. Zimmermann,
and Wieland Brendel. InfoNCE: Identifying the gap between theory and practice.arXiv
preprint arXiv:2407.00143, 2024.
Brian Sifringer, Virginie Lurkin, and Alexandre Alahi. Enhancing discrete choice models
with representation learning.Transportation Research Part B: Methodological, 140:236–261,
2020.
Güven P. Soysal and Lakshman Krishnamurthi. Demand dynamics in the seasonal goods
industry: An empirical analysis.Marketing Science, 31(2):293–316, 2012.
Kenneth E Train.Discrete choice methods with simulation. Cambridge University Press, 2nd
edition, 2009.
Jack E. Triplett.Handbook on Hedonic Indexes and Quality Adjustments in Price Indexes:
Special Application to Information Technology Products. OECD Publishing, Paris, 2006.
Aaron van den Oord, Yazhe Li, and Oriol Vinyals. Representation learning with contrastive
predictive coding.arXiv preprint arXiv:1807.03748, 2018.
A. Van der Kwaak. Hoe beleeft de Nederlandse consument mode? Technical report, Ruigrok
NetPanel, 2009. Survey of 500 Dutch consumers.
Laurens van der Maaten and Geoffrey Hinton. Visualizing data using t-SNE.Journal of
Machine Learning Research, 9(11):2579–2605, 2008.
70

Vladimir Vovk, Alex Gammerman, and Glenn Shafer.Algorithmic Learning in a Random
World. Springer, 2005.
Shenhao Wang, Qingyi Wang, and Jinhua Zhao. Deep neural networks for choice analysis:
Extracting complete economic information for interpretation.Transportation Research
Part C: Emerging Technologies, 117:102727, 2020.
Jeffrey M. Wooldridge. Distribution-free estimation of some nonlinear panel data models.
Journal of Econometrics, 90(1):77–97, 1999.
Shunyuan Zhang, Dokyun Lee, Param Vir Singh, and Kannan Srinivasan. What makes a good
image? Airbnb demand analytics leveraging interpretable image features.Management
Science, 68(8):5644–5666, 2022.
Yu Zheng, Chen Gao, Xiangnan He, Yong Li, and Depeng Jin. Price-aware recommendation
with graph convolutional networks. InIEEE 36th International Conference on Data
Engineering (ICDE), pages 133–144, 2020.
Yu Zheng, Chen Gao, Xiangnan He, Depeng Jin, and Yong Li. Incorporating price into
recommendation with graph convolutional networks.IEEE Transactions on Knowledge
and Data Engineering, 35(2):1609–1623, 2023.
71
