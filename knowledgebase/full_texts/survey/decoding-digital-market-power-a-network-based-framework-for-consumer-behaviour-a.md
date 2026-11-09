---
title: 'Decoding digital market power: a network-based framework for consumer behaviour and strategic
  advantage'
url: https://doi.org/10.1057/s41270-026-00472-4
category: survey
subcategory: framework
date: 2026-03
venue: Journal of Marketing Analytics
authors:
- Larissa M. Batrancea
- Ömer Akgüller
- Mehmet Ali Balcı
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1057/s41270-026-00472-4.pdf
pages: 27
chars: 127361
fetched_at: '2026-11-08T19:14:03+00:00'
kb_version: 1
---

# Decoding digital market power: a network-based framework for consumer behaviour and strategic advantage

ORIGINAL ARTICLE
Journal of Marketing Analytics
https://doi.org/10.1057/s41270-026-00472-4
Introduction
The advent of electronic commerce (e-commerce) has fun -
damentally reshaped the global retail landscape by pro -
viding unprecedented convenience, selection, speed. This
digital transformation extends beyond mere transactional
efficiency. It reflects a socio-technical reconfiguration of
consumer identities, market hierarchies, and cultural prac -
tices in the twenty-first century (Castells 2010). The para -
digm shift has generated an enormous set of transactional
data that, when effectively analysed, can offer invaluable
business insights (Li and Zhang 2021; Zhang et al. 2021a).
Such insights range from predicting consumer demand and
refining marketing campaigns to optimizing inventory man-
agement and supply chain operations. However, the com -
plexity of e-commerce data often surpasses what traditional
modelling techniques (e.g., association rule mining, logistic
regression, decision trees) can grasp. These rely on aggre -
gated or linear assumptions that overlook the multifaceted,
  Larissa M. Batrancea
larissa.batrancea@ubbcluj.ro
Ömer Akgüller
oakguller@mu.edu.tr
Mehmet Ali Balcı
mehmetalibalci@mu.edu.tr
Anca Nichita
anca.nichita@uab.ro
Mircea-Iosif Rus
mircea.rus@incerc-cluj.ro
1 Department of Business, Babes-Bolyai University, Cluj-
Napoca,, Romania
2 Department of Mathematics, Faculty of Science, Muğla Sıtkı
Koçman University, Muğla, Turkey
3 Faculty of Economics, “1 Decembrie 1918” University of
Alba Iulia, Alba Iulia, Romania
4 National Institute for Research and Development in
Construction, Urbanism and Sustainable Territorial
Development URBAN-INCERC, Cluj-Napoca, Romania
Abstract
Despite exponential growth in digital commerce, conventional customer analytics fail to capture relational dynamics and
temporal patterns critical for optimizing targeting precision, cross-selling, and churn prevention. This paper advances
consumer behaviour research by framing e-commerce activity as a relational system shaped by economic incentives and
temporal decision-making, building on social embeddedness theory and (Recency–Frequency–Monetary) RFM modelling
principles. We model transactions as a weighted bipartite network where customers and products form interconnected
nodes, addressing gaps in traditional collaborative filtering and demographic segmentation that overlook relational struc -
tures. Using 38,995 consumers and 44,802 transactional links across four product categories, we introduce an original
edge-weighting methodology fusing linear economic attributes (profit margins, discounts, shipping costs) with nonlinear
behavioural components (purchase recency, order prioritisation). Applying graph neural networks (GCN, GAT, Graph -
SAGE), the framework achieves 94–95% classification accuracy enabling practical applications in personalized marketing
automation, dynamic pricing, and recommendation systems with 12–15% gains in targeting precision. Significant varia -
tions in network centrality reveal differentiated strategic roles among product segments. By integrating network analytics
with social science perspectives, this research illuminates how relational data exposes underlying power relations and
behavioural logics in contemporary e-commerce ecosystems, bridging computational innovation with sociological under -
standing of digital marketplace dynamics.
Keywords Consumer behaviour · E-commerce · Framework · Competitive dynamics
Received: 8 December 2025 / Accepted: 4 March 2026
© The Author(s) 2026
Decoding digital market power: a network-based framework for
consumer behaviour and strategic advantage
Larissa M. Batrancea1  · Ömer Akgüller2 · Mehmet Ali Balcı2 · Anca Nichita3  · Mircea-Iosif Rus4

L. M. Batrancea et al.
relational nature of human behaviour embedded in digital
interactions.
Graph-based approaches are promising because they
portray relational structures that can be easily interpretable
(Tuteja and Kumar 2022; Liu et al. 2021b; Zhang et al.
2021b). Drawing parallels to sociological network theory
(focused on how social actors are embedded in relationship
webs), e-commerce transactions can be conceptualized as
dynamic networks where nodes (customers, products) are
linked through edges weighted by economic and temporal
significance. A bipartite graph models two distinct sets of
entities: customers, product categories (Wang et al. 2019,
2024; Lu et al. 2024; Yu et al. 2021). Edge weights encode
the socio-economic “strength” of each interaction. This
approach offers a lens to decode how transactional behav -
iours reflect rational choice and cultural practices.
However, not all transactions carry equal strategic sig -
nificance. A high-margin purchase made recently with
minimal discount reflects a high-value interaction, while an
older, heavily discounted transaction might hold less predic-
tive value for future customer behaviour (Chen et al. 2016;
Lin et al. 2021; Xu et al. 2020). Existing approaches fail to
integrate multidimensional variations and combine various
elements into a unified framework that captures relational
embeddedness within temporal and social contexts (Moran
2005). Hence, studies should consider aspects such as prof-
itability (Ballestar et al. 2018; Sharma 2024), discount
effects (Liu et al. 2021a; Mishra et al. 2024), shipping costs
(Alves et al. 2023; Deshpande and Pendem 2023), and order
priority (Gligor et al. 2022; Fernandes et al. 2024; Lin et al.
2022; Luo 2025; Zhang et al. 2021c).
Modern graph neural networks (GNNs) provide a robust
framework for integrating node-level and network-level fea-
tures in a single predictive model (Wu et al. 2020; Corso et
al. 2024). GNN integration mirrors sociological theories of
diffusion, where individual actions are shaped by network
position and peer influence (Rogers 2003). In e-commerce,
this translates to models capable of learning from intrinsic
features (e.g., centrality scores) and weighted edges that
define relationships. Distinct GNN architectures, such as
graph convolutional networks (Bhatti et al. 2023; Ren et al.
2022), graph attention networks (Veličković et al. 2017; Liu
and Zhou 2020), and GraphSAGE (Liu et al. 2020; Huang
and Chen 2024), offer unique strengths for handling differ -
ent graph characteristics and reveal how market structures
emerge from micro-level interactions (Fligstein 2001; Lazer
et al. 2020). Such insights can identify influential product
categories as focal points for targeted promotions (Zhang
and Gong 2020; Choi and Kim 2009) or high-centrality
customers as candidates for loyalty programs (Lam et al.
2013). This follows the manner in which consumer culture
theory examines how market actors build identity through
consumption (Arnould and Thompson 2005; Orlikowski
2007).
Our study advances e-commerce analytics by modelling
customer-product interactions as a weighted bipartite graph
and classifying nodes via GNNs. We introduce a novel edge-
weighting methodology that integrates economic attributes
(profit margins, discounts, shipping costs) with behavioural
components grounded in Recency-Frequency-Monetary
(RFM) modelling traditions (Michael et al. 1997; Teich-
man and Zamir 2022), which quantify the socio-economic
significance of each relationship. The graph is enriched by
out-degree centrality and hubs score, two metrics captur -
ing structural network influence. We deployed three GNN
architectures to classify nodes. This achieved a 94‒95%
accuracy level and revealed different strategic roles among
product segments. The novelty of the study lies in its inter -
disciplinary synthesis: it marries computational innovation
with sociological insights, offering a framework to analyse
how digital markets reproduce or disrupt existing social and
economic hierarchies.
The remainder of this article is organized as follows.
The section on literature review synthesizes prior research
on e-commerce analytics and graph-based methods. The
methodology section details our weighted bipartite graph
construction, centrality measures, and GNN architectures.
The section on results presents network analysis and clas -
sification performance, while the Discussion section inter -
prets findings and implications. The last section summarizes
contributions and future research directions.
Literature review
Evolution of e-commerce analytics: From traditional
methods to graph neural networks
Early e-commerce research from 2004 to 2017 relied on
conventional data mining approaches such as collabora -
tive filtering, association rule mining, clustering to analyse
transactional patterns (Huang et al. 2004; Parikh and Shah
2015). Though foundational, these methods treated trans -
actions uniformly and did not capture temporal dynam -
ics, relational structures, varying transaction significance.
Hence, the field evolved toward network-based approaches
that model customer-product relationships.
The years 2016‒2020 witnessed two parallel develop -
ments that addressed such limitations. First, the Recency-
Frequency-Monetary (RFM) analysis emerged as a bridge
between transaction counts and behavioural modelling
by incorporating temporal and value dimensions (Hsu
and Huang 2020; Martens et al. 2016). Second, graph-
based representations gained prominence, while bipartite

Decoding digital market power: a network-based framework for consumer behaviour and strategic advantage
customer-product networks revealed patterns invisible to
traditional data analyses (Lismont et al. 2018; Zhang et al.
2021d). However, research approaches relied on manual fea-
ture engineering and unsupervised algorithms, which lim -
ited their capacity to exploit higher-order network patterns.
Table 1 summarizes the evolutionary trajectory.
Graph neural networks in contemporary
e-commerce (2018‒2025)
The period 2018‒2025 marks a paradigm shift toward graph
neural networks that learn optimal representations from
network structures. In this context, three GNN architec -
tures have dominated recent e-commerce applications, each
addressing specific computational and analytical challenges.
Graph convolutional networks (GCNs) aggregate neigh -
bourhood information through spectral convolution opera -
tions. The neural graph collaborative filtering from Wang
et al. ( 2020) demonstrated that propagating embeddings
through user-item interaction graphs captures high-order
collaborative signals, which yields substantial improve -
ments regarding matrix factorization on benchmark datas -
ets. De Souza Pereira Moreira ( 2018) applied GCN-based
architectures to session-based recommendations and mod -
elled click sequences as item graphs to accurately predict
next-item selections.
Graph attention networks (GATs) introduced learnable
attention mechanisms to prioritize informative connections,
which addressed the limitation of GCNs in uniform neigh -
bour weighting. Veličković et al. ( 2017) demonstrated the
superiority of GATs over standard GCNs on node classifi -
cation benchmarks, since GATs focus on pertinent connec -
tions. In e-commerce contexts, Piao et al. ( 2021) extended
this approach with motif-based multi-view GAT for social
commerce networks. The study captured higher-order con -
nection patterns that predict customer lifetime value with
superior accuracy (if applied to large-scale datasets).
GraphSAGE achieved scalability breakthroughs via
neighbour sampling strategies, which enables training
on graphs with billions of edges. The deployment of Pin -
Sage by Ying et al. ( 2018) on Pinterest data showed the
viability of GNNs for web-scale recommendations. Recent
applications have extended GraphSAGE to customer churn
prediction, where graph-based features identify likely
churners with higher accuracy than traditional methods.
This method achieved 15‒20% improvements over matrix
factorization approaches on benchmark datasets (Wang et
al. 2020), demonstrated superior predictive performance in
session-based recommendation contexts (De Souza Pereira
Moreira 2018) and validated the effectiveness of sampling-
based approaches for operational analytics.
Studies published in the period 2023‒2024 address GNN
explainability challenges that emerged with performance
improvements. For instance, studies from Schaschek et al.
(2023) and Makanga et al. ( 2024) developed techniques to
identify graph features that drive predictions, thus respond-
ing to concerns about algorithmic accountability in auto -
mated decision-making (Zuboff 2019). Recent studies show
that predictive power must be balanced and interpretable for
practical business deployment.
Table 2 synthesizes architectural characteristics and
e-commerce applications.
Edge weighting and feature integration in
e-commerce networks
Despite GNN advances, a critical gap persists. Most appli -
cations treat edges as binary (purchase/no-purchase) or
weight them solely by frequency, while ignoring the multi -
dimensional economic and temporal factors that determine
the significance of an online transaction. Recent studies
establish the importance of specific factors that remain
underexploited in graph-based models.
Profitability influences customer relationship value.
Ballestar et al. ( 2018) showed that segmentation based on
profitability enabled more effective personalized retention
strategies in e-commerce networks. Sharma (2024) revealed
that profit-based customer segmentation facilitates the iden-
tification of high-value interactions, with profitable custom-
ers exhibiting distinct characteristics of network positioning.
Discount strategies create complex, nonlinear effects on
purchasing behaviour. Liu et al. ( 2021a) found threshold
effects: discounts below 19% negatively impacted spend -
ing, while discounts above 19% had positive impact. Mishra
Table 1 Evolution of e-commerce analytics approaches (2004‒2025)
Period Approach Representative studies Key contributions Limitations addressed by next
generation
2004–
2017
Traditional
data mining
Huang et al. (2004), Parikh and Shah (2015),
Leung et al. (2017)
Association rules, collaborative
filtering, clustering
Uniform transaction treatment,
no temporal/relational dynamics
2016–
2020
RFM network
features
Martens et al. (2016), Hsu et al. (2020), Lis-
mont et al. (2018), Zhang et al. (2021d)
Temporal segmentation, bipartite
graphs, community detection
Manual feature engineer-
ing, limited to first-order
relationships
2018–
2025
Graph neural
networks
Wang et al. (2020), Piao et al. (2021), Ying et
al. (2018), Schaschek et al. (2023), Makanga
et al. (2024)
Automatic representation learning,
multi-hop relationships, web-scale
deployment
Edge weighting sophistica-
tion, explainability, theoretical
integration

L. M. Batrancea et al.
Hsu et al. (2020) demonstrated that combining RFM scores
with clustering algorithms improved the identification of
high-value cohorts in large-scale datasets. Martens et al.
(2016) established the effectiveness of RFM variants for
predictive analytics in customer behaviour contexts.
Table 3 synthesizes important factors of influence and
identifies integration gaps.
Research gaps and study positioning
Extant literature reveals three critical gaps that constrain
current GNN applications in e-commerce analytics. First,
studies do not integrate economic factors (profit margins,
shipping costs, discount levels) with temporal dynamics
(recency decay, priority effects) into edge weights. Current
approaches treat edges as binary or frequency-based, with -
out identifying which customer-product relationships carry
business value. This oversimplification contradicts empiri -
cal evidence showing that factors like profitability (Sharma
2024), discounts (Liu et al. 2021a), shipping costs (Alves
et al. 2023) influence online transactions. Second, while
recent studies report high predictive accuracy of GNN mod-
els, they provide limited comparisons of architectural trade-
offs. The literature lacks head-to-head evaluations under
identical conditions that would reveal when: GAT attention
et al. ( 2024) identified significant relationships between
discount levels and purchasing patterns in apparel retail.
Results from Close and Kukar-Kinney ( 2010) showed that
price-sensitive consumers switched channels based on
discount availability and influenced patterns of network
connectivity.
Shipping costs are important operational indicators and
have substantial profit implications. Alves et al. (2023) used
agent-based modelling to demonstrate that shipping costs
have the largest impact in e-commerce operations, with
optimization strategies yielding up to a 79.1% increase in
net profit. According to Deshpande and Pendem (2023), the
shipping cost-to-sales ratio is an important profitability met-
ric that balances customer satisfaction.
Order priority  reflects the dynamics of supply chains
with measurable performance impacts. Gligor et al. ( 2022)
showed that order strategies based on priority customize rout-
ing logic and ensure that high-priority orders receive faster
processing, thus improving turnaround times. Fernandes et
al. (2024) singled out planning priority as fundamental to
the planning of demand-driven material requirements. Lin
et al. (2022), Luo (2025), Zhang et al. ( 2021c) stressed the
role of priority assignment in optimizing resource utiliza -
tion across supply chains activities.
Temporal recency (rooted in RFM modelling traditions)
elicits exponential decay effects on transaction relevance.
Table 2 GNN architectures in e-commerce applications (2018‒2025)
Architecture Core mechanism Representative studies
(recent)
E-commerce applications Empirical performance Primary limitations
GCN Spectral convolu-
tion, neighbourhood
aggregation
Wang et al. (2020), De
Souza Pereira Moreira
(2018)
Collaborative filter-
ing, session-based
recommendations
15–20% improve-
ment over matrix
factorization
Uniform neighbour
weighting, limited
scalability
GAT Attention mecha-
nisms, selective
weighting
Veličković et al. (2017),
Piao et al. (2021)
Customer lifetime
value, social commerce
prediction
Superior accuracy
on heterogeneous
networks
Computational com-
plexity, requires sub-
stantial training data
GraphSAGE Neighbour sam-
pling, inductive
learning
Ying et al. (2018),
recent churn prediction
studies
Web-scale recommenda-
tions (3B + nodes), churn
prediction
Maintains performance
at scale, real-time
inference
Information loss from
sampling, sensitivity
to sample size
Table 3 Transaction value factors in e-commerce networks: Empirical foundations and integration gaps
Factor Theoretical
foundation
Recent empirical evidence (2018–2025) Measured impact Current integration status
in GNN models
Profitability Customer relationship
value theory
Ballestar et al. (2018), Sharma (2024) Distinct network positioning
for profitable customers
Typically absent from
edge weights
Discounts Promotional effects
theory
Liu et al. (2021a), Mishra et al. (2024),
Close and Kukar-Kinney (2010)
Nonlinear threshold effects
(19% critical point), channel
switching
Rarely incorporated;
when present, treated
linearly
Shipping costs Operational efficiency
theory
Alves et al. (2023), Deshpande and Pen-
dem (2023)
Up to 79.1% profit variation,
cost-to-sales ratio critical
Generally excluded from
network models
Order priority Supply chain
dynamics
Gligor et al. (2022), Fernandes et al.
(2024), Lin et al. (2022), Luo (2025),
Zhang et al. (2021c)
Turnaround time optimization,
resource utilization
Novel consideration;
not in existing GNN
applications
Recency RFM modelling,
temporal decay
Hsu and Huang (2020), Martens et al.
(2016)
Exponential decline in predic-
tive value
Occasionally used but not
systematically integrated
with economic factors

Decoding digital market power: a network-based framework for consumer behaviour and strategic advantage
It provides a comprehensive coverage of customer-product
interactions, suitable for graph-based analytics.
Each transaction record contains temporal, operational,
financial attributes, which are essential for constructing
weighted bipartite networks. The “Order Date” column
timestamps each purchase, while “Aging” quantifies order-
to-delivery duration (μ = 5.26 days, SD = 2.96 days), captur-
ing logistical efficiency. Customers are uniquely identified
through “Customer ID,” enabling relationship tracking
across multiple transactions. Financial dimensions include
“Sales” (total transaction value), “Quantity” (units pur -
chased), “Discount” (promotional intensity ranging 0.1–
0.5), “Profit” (net margin after costs), and “Shipping Cost”
(delivery expenses). The “Order Priority” column encodes
operational urgency across four levels (low, medium, high,
critical). Variables enable multidimensional edge weighting
that integrates economic value, temporal recency, opera -
tional significance.
Dataset reliability was established through a systematic
validation across multiple dimensions (Table 4). The assess-
ment of structural integrity revealed completeness with
only 0.001% missing values (8 of 820,640 data points), all
occurring in non-critical fields. We found zero instances of
negative sales or impossible profit combinations. Temporal
validity spans through 363 days of continuous transaction
activity without gaps or anomalous patterns (Fig. 1, panel a).
Behavioural realism was verified through correspondence
with established e-commerce patterns: transaction-per-
customer distributions exhibited power-law characteristics
(mean = 1.32, median = 1.0) (Zhang et al. 2021d); discount
distributions (Liu et al. 2021a); priority classifications (Gli-
gor et al. 2022).
Comparative benchmarking against established research
confirms a structural alignment with network studies on
peer-reviewed e-commerce (Table 5). The customer-to-
category ratio (9749:1) and transaction sparsity patterns
corresponded to bipartite graph characteristics reported
by Lismont et al. ( 2018). The 363-day observation win -
dow provides a temporal depth comparable to longitudinal
studies (Hsu and Huang 2020), while maintaining compu -
tational tractability for GNN training. Category-specific
analysis revealed a realistic variation in transactional char -
acteristics: fashion dominates volume (50.0% of transac -
tions) with highest profit margins (μ = $80.82) and discount
intensity (μ = 0.36), electronics exhibits minimal discount -
ing (μ = 0.16) with moderate profitability (μ = $64.49),
while home & furniture demonstrates compressed margins
(μ = $57.01) with moderate promotional activity (μ = 0.29).
These patterns aligned with retail economics literature that
document the dynamics of category-specific competition.
Three limitations warrant acknowledgment. First, customer
anonymization precludes demographic analysis. However,
mechanisms justify computational costs; the sampling of
GraphSAGE has sufficient accuracy with superior scal -
ability. Third, connections between technical advances and
theoretical frameworks remain fragmented. Recent work
(Schaschek et al. 2023; Makanga et al. 2024) addresses the
explainability of GNN models but rarely integrates findings
with established theories from marketing, network sociol -
ogy, consumer culture.
Our study addresses these gaps by introducing an
enhanced weighted bipartite graph model that encodes five
transaction dimensions (profit, discount, recency, shipping
cost, order priority) into a unified edge-weighting scheme,
grounded in RFM modelling principles and accounting
theory. We provide a systematic comparison of three GNN
architectures under identical conditions on the weighted
network, thus offering evidence of performance-scalabil -
ity trade-offs that lack from current literature. Finally, we
ground our methodology and interpretation in network
theory (Granovetter's embeddedness), marketing (RFM tra-
ditions), consumer culture theory. We also emphasize how
computational findings explain social and economic hierar-
chies in digital commerce.
This multidimensional approach advances technical
capabilities and understanding, which positions our study as
a relevant contribution to the evolving landscape of graph-
based e-commerce analysis.
Methodology
Data set and quality validation
The dataset employed originates from an e-commerce plat -
form spanning a one-year period (January 1–December 30,
2018) and is publicly available through Kaggle’s curated
repository. It comprises 51,290 transactional records involv-
ing 38,997 unique customers across four product categories:
fashion, home & furniture, auto & accessories, electronics.
Table 4 Data quality validation summary
Quality
dimension
Assessment
criteria
Observed result Status
Completeness Missing
values
0.001% (8 of 820,640
values)
Passed
Economic
coherence
Financial
logic
0 negative sales, 0 impos-
sible combinations
Passed
Temporal
validity
Date
continuity
363 days continuous,
aging μ = 5.26 ± 2.96 days
Passed
Behavioural
realism
Literature
alignment
Matches RFM patterns
(Hsu and Huang 2020),
discount effects (Liu et al.
2021a)
Passed
Sample
adequacy
GNN
training
sufficiency
38,997 customers, 51,290
transactions
Passed

L. M. Batrancea et al.
graph framework when analysing e-commerce customer-
product relationship.
Figure 1 illustrates comprehensive data quality valida -
tion across temporal, operational, and categorical dimen -
sions. Panel (a) indicates 363 days of continuous transaction
activity, confirming temporal integrity. Panels (b–d) pres -
ent distributions of key operational variables, which exhibit
realistic patterns consistent with e-commerce logistics and
pricing structures. Panel (b) shows aging distribution con -
centrated around the mean (5.26 days) with realistic vari -
ance that reflects standard fulfilment operations. Panel (c)
displays right-skewed profit distribution where most trans -
actions generate moderate margins, while a minority yield
higher profitability and align with retail economics. Panel
(d) reveals that shipping cost distribution exhibits similar
right-skew patterns with variance corresponding to product
our network-centric approach derives segmentation from
behavioural patterns rather than demographic attributes,
thus aligning with paradigms of privacy-preserving ana -
lytics. Second, single-platform data constrains cross-plat -
form generalizability, which we address through validation
against multi-platform patterns documented in recent lit -
erature (Alves et al., 2023; Sharma, 2024). Third, category
aggregation sacrifices product-level granularity when run -
ning category-level analysis in business contexts (Ballestar
et al., 2018). Robustness was further confirmed through
5-fold cross-validation, which showed consistent model
performance (±2% variation) across data subsets, thus
indicating no quality issues. The convergence of evidence
across structural validation, behavioural verification, and
comparative benchmarking indicated the suitability of the
dataset for developing and validating a weighted bipartite
Network characteristic Our study Benchmark studies Assessment
Transactions per customer 1.32 (median = 1.0) Lismont et al. (2018): 1.5–2.0 Consistent
Sparsity pattern Power-law distribution Zhang et al. (2021d): Power-law Aligned
Temporal coverage 363 days Hsu and Huang (2020): 12 + months Adequate
Priority distribution Medium (57.4%),
High (30.2%)
Gligor et al. (2022): Similar
stratification
Consistent
Table 5 Comparative validation
against e-commerce research
benchmarks

Fig. 1 Distributions of selected features

Decoding digital market power: a network-based framework for consumer behaviour and strategic advantage
We chose a bipartite graph for three methodological rea-
sons. First, bipartite graphs preserve the customer-product
duality, which is inherent for transactional data. Second, this
structure enables direct modelling of heterogeneous relation-
ships and aligns with the focus of marketing on customer-
firm interactions. Third, bipartite representations facilitate
efficient GNN training on large-scale data by maintaining
clear distinctions of node types that constrain operations of
passing messages to meaningful cross-type relationships.
Capturing purchase interactions via bipartite structures
facilitates the computation of aggregated statistics (e.g.,
total revenue generated by each customer–category pair).
Additionally, it enables the application of graph-theoretical
measures like centralities, which highlight the most impor -
tant customers/categories within the network. Moreover,
this structure facilitates the development of graph-based
machine learning models that can predict customer behav -
iour, product demands, other outcomes relevant to e-com -
merce businesses.
Edge weighting scheme
In e-commerce settings, not all C → P  category edges
should be treated equally. Certain purchases might be more
recent, profitable, heavily discounted than others. To reflect
value and relevance, we introduced a weighted bipartite
graph, where each edge (ci,p i) is assigned a scalar wi,j  that
captures the importance or contribution of the customer–
category relationship.
We assume that customer ci has made several transac -
tions k =1 , 2,...,K (i,j) in product category pj . For each
transaction k, we define the variables: P rof itk ‒ the net
profit from transaction k, ShippingCost k ‒ the shipping
cost associated with transaction k, Discountk is the total
discount applied to transaction k, Agingk the recency
(or age) of the transaction (e.g., days since purchase),
P riorityk is a categorical measure showing how critical or
urgent the order was (e.g., low, medium, high, critical), α
is a user-defined parameter to penalize discount usage, λ a
time-decay rate.
The transaction-level contribution ∆k is defined to cap -
ture profitability and recency effects for transaction k with:
∆k =( P rof itk − ShippingCost − α × Discountk)
× exp (−λ × Agingk) × h (P riorityk)  (1)
where h (P riorityk) is a priority factor. In practice, h(·)
may be a numeric multiplier, such as:
h (P riorityk)=



1.0, if low
1.1, if medium
1.25 if high
1.5 if critical
 (2)
size and delivery distance factors. Panels (e–g) illustrate
categorical distributions that confirm a behavioural real -
ism: the distribution of product category (panel e) shows the
dominance of fashion (50.0%), with balanced representation
across other categories. Order priority distribution (panel f)
indicates a realistic concentration in medium (57.4%) and
high (30.2%) priorities with smaller critical (7.7%) and low
(4.7%) segments. Discount distribution (panel g) exhibits
concentration at moderate levels (20–30%), which is in line
with strategic promotional practices (Liu et al. 2021a).
Computational methodology
It proceeds through three interconnected stages designed to
capture, quantify, and analyse the dynamics of customer-
product relationship in e-commerce networks. First, we
constructed a representation of the weighted bipartite graph,
where customers and product categories form distinct node
sets connected by edges. Edge weights encode a multidi -
mensional transaction significance by integrating economic
factors (profit, discount, shipping cost) and behavioural
components (recency decay, order priority). The choice of
this representation is theoretically motivated by the empha-
sis of social network theory on relational embeddedness
(Granovetter 1985). We can thus examine how customer
value emerges from network position. Second, we computed
measures of graph-theoretic centrality (out-degree central -
ity, hubs score) that quantify structural network importance.
These metrics also provide node-level features that capture
the influence of patterns invisible to traditional customer
analytics. Third, we employed graph neural network archi -
tectures to classify nodes and compare their performance
to identify architectural choices that best exploit relational
information concerning customer segmentation.
Bipartite graph construction
In e-commerce analytics, examining relationships of
customers‒product categories is a common task. Mod -
elling relationships as a bipartite graph provides a flex -
ible and mathematically rigorous way to capture buyers,
products, frequency or value of purchases, etc. Let
C =
{
c1,c 2,...,c |C|
}
 represent the set of customers and
P =
{
p1,p 2,...,p |P |
}
 represent the set of product cat -
egories. The set of edges E ⊆ C × P  indicates that a given
customer has purchased from a product category. We con -
struct a bipartite graph G =( C ∪ P, E), where edges exist
only between a customer node and a product-category node.
Depending on the application, this graph can be represented
as either a directed bipartite graph C → P  to distinguish
the direction of purchase interactions or as an undirected
bipartite graph.

L. M. Batrancea et al.
future behaviour better than older ones. The exponential
decay function, exp (−λ × Agingk), is used in business
analytics for gradually down-weighting older purchases.
Emphasis on profitability and discount aligns the weight
measure with true profitability by penalizing discount usage
(α × Discountk) and subtracting shipping costs. Addition-
ally, order priority acknowledges the operational signifi -
cance of orders marked as “high” or “critical” by weighting
them more heavily. Unified weighting offers a business-
centred perspective: edges are stronger if they involve (1)
high net profit, (2) recent transactions, (3) minimal discount
usage, (4) high priority.
Network centrality measures
Centrality measures identify the most central nodes (i.e.,
whether a node represents a power customer or popular
product category). Centralities illuminate structural posi -
tions within the network and can highlight which actors
(customers, categories) are crucial to sustaining overall
e-commerce flows. When treating the bipartite graph as
directed (from customer to product category), distinct con -
cepts of in-degree versus out-degree emerge. If the graph is
undirected, degree indicates the number/sum of weights of
incident edges. However, many e-commerce studies inter -
pret edges as directed from customers to product catego -
ries. Therefore, in-degree measures how many customers
purchase a category, while out-degree measures how many
categories a customer buy from.
In-degree centrality ( IDC ) for a node v in a directed
graph is defined as:
IDC (v)= ∑
u→v∈E
wu,v  (4)
which captures how many customers (and total weight) flow
into that category, when applied to product category nodes.
Out-degree centrality (ODC ) for a node u is defined by:
ODC (v)= ∑
u→v∈E
wu,v  (5)
reflecting how many product categories a customer con -
nects to (weighted by wu,v ).
A high in-degree category node implies it is popular
among customers or has high-value purchases. A high out-
degree customer node indicates that the customer buys from
a broad range of product categories, often associated with
cross-buying opportunities.
Hyperlink-Induced Topic Search (HITS) yields two
related centralities: hubs and authorities. In a bipartite
C → P  context, the authority score measures how valuable
The transaction-level contribution ∆k employs a hybrid
mathematical formulation that combines linear and non -
linear components to capture accounting principles and
behavioural nuances inherent for e-commerce trans -
actions. Our approach stems from the fact that differ -
ent components of transaction value operate through
distinct mechanisms. The linear terms in Eq. 1 (i.e.,
Pr of itk − ShippingCost − α × Discountk) mirror
established accounting principles, where costs and dis -
counts reduce net value proportionally, consistent with
standard accounting practices (Baumgartner et al. 2012;
Banerjee 2021). This linear relationship reflects the direct
economic impact, where each unit of discount or shipping
cost diminishes the transaction’s financial contribution. It
aligns with frameworks of cost–benefit analysis that are
widely employed in operations research (Boucherie 2022).
The nonlinear exponential decay component
exp (−λ × Agingk) is in line with behavioural research,
which demonstrates that transaction relevance diminishes
non-linearly over time (Ebadi Jalal and Elmaghraby 2024;
Jiang et al. 2024; Nofsinger and V arma 2013). The exponen-
tial formulation captures a psychological principle accord -
ing to which recent experiences influence decision-making
and predictive value (Frederick et al. 2002).
The piecewise priority multiplier h (Pr iorityk) reflects
the discrete nature of operational priority classifications
that are used in supply chain management systems. This
approach acknowledges that priority levels represent cat -
egorical operational decisions and align with practices used
in priority-based planning, where orders are classified into
distinct urgency categories (Baumgartner et al. 2012; Lu
et al. 2017; Schulz et al. 2005). The multiplicative effect
ensures that higher priority orders receive greater weight,
consistent with principles of operational management
emphasizing the strategic importance of urgent transactions.
To combine multiple transactions between the same
customer-category pair, the individual contributions are
summed:
wi,j =
K(i,j)∑
k=1
∆k  (3)
Each edge (ci,p j ) is assigned a weight wi,j , reflecting mon-
etary value (profit, cost, discount) and recency (through
exponential decay), priority. This hybrid approach is nec -
essary because purely linear models would fail to capture
temporal dynamics, where recent transactions predict future
behaviour. Nonlinear models would not elicit direct eco -
nomic influences, which can be quantified through cost–
benefit analysis.
Recency and time decay draw on RFM modelling used in
marketing research, where more recent transactions predict

Decoding digital market power: a network-based framework for consumer behaviour and strategic advantage
~A = A + I is the adjacency matrix augmented with self-
loops, ~D is the diagonal node-degree matrix of ~A, W  is a
learnable weight matrix, σ is a nonlinear activation function
(e.g., ReLU). We appreciate your effort in editing the arti -
cle for the publication in this journal and rephrasing some
words for proper reading. Nevertheless, we kindly ask you
not to cut entire paragraphs from the accepted manuscript.
Hence, please add this here, it was cut:GCNs represent the
foundation for processing bipartite e-commerce graphs due
to their inherent suitability for dense customer-product net-
works. GCNs excel in e-commerce contexts because they
leverage convolutional aggregation mechanisms that align
with the dense connectivity patterns observed in digital
marketplaces, where customers frequently interact with
multiple product categories and categories serve numerous
customers simultaneously.
The theoretical foundation of GCNs for e-commerce
analytics rests on their ability to integrate local structural
features through neighbourhood aggregation, capturing how
individual customer behaviours are influenced by immediate
network context. In the bipartite customer-category graph,
GCNs model how a customer’s purchasing profile is shaped
by the categories they engage with and, reciprocally, how
product categories derive market positioning from custom -
ers who purchase from them. This bidirectional information
flow mirrors the fundamental dynamics of consumer-market
interactions described in network economics literature. For
instance, customers who purchase from premium electron -
ics categories may exhibit similar behavioural patterns to
those engaging with luxury fashion, even without direct
overlap in purchase histories. GCNs can detect higher-order
relationships through their layer-wise aggregation process,
making them particularly suited for identifying latent cus -
tomer segments and cross-category purchasing propensities
that traditional methods would miss.
A second architecture (GAT) refines the aggregation
process by introducing an attention mechanism. Instead
of scaling neighbour features, GAT measures an attention
coefficient αij  for each edge and quantifies how much node
i should rely on the centralities of node j. Formally, the
embedding update for node i in one GA T layer is written as:
h′ i = σ
(
∑
j∈mathcalN (i)
αij Wh j
)
,  (9)
where hj  includes centrality of node j alongside its learned
representation from previous layers, W  is a learnable weight
matrix, σ is a non-linear activation. GA Ts provide a sophis-
ticated enhancement over standard graph convolutions by
introducing learnable attention mechanisms that priori -
tize customer-category interactions based on their relative
it is as an “endpoint” (e.g., product category that many good
hubs link to), while the hub score measures how valuable
it is as a “pointer” (e.g., customer linking to many good
authorities). The iterative definitions are:
Hubs (v)= ∑
u∈Out(v)
Authority (u); Authority (u)= ∑
v∈In(u)
Hubs (v)  (6)
In the weighted case, edge weights are incorporated into
summations:
Hubs (v)=
∑
u∈Out(v)
wu,v × Authority (u);
Authority (u)=
∑
v∈In(u)
wu,v × Hubs (v) .
 (7)
Out-degree centrality and hubs score were selected for their
information content and computational tractability. The for-
mer captures the breadth of customer engagement (diver -
sity of categories purchased), providing a straightforward
measure of cross-buying behaviour, which is critical for
cross-selling strategies. The latter (derived from the HITS
algorithm) captures connection quality by weighting rela -
tionships with high-authority categories. This facilitates the
identification of customers whose purchasing patterns con -
centrate on influential product segments. This two-measure
approach balances information richness with computational
efficiency, while providing interpretable business metrics.
Through these tools, businesses can gain valuable insights
into their operations. Hence, one can identify key custom -
ers with diverse purchasing behaviours or influential reach
within the network. Similarly, one can identify product cat-
egories critical to revenue or brand identity.
Graph neural networks in e-commerce analytics
An essential step involves the use of GNNs to classify nodes
in the bipartite e-commerce graph, where each node is rep -
resented by a feature vector containing the seven centrality
measures. By combining centralities with the network struc-
ture, GNNs enable the learning of high-level embeddings
that are relevant for e-commerce applications.
One foundational GNN architecture that we used is
graph convolutional network (GCN). Given an adja -
cency matrix A ∈ RN ×N  for the bipartite graph (where
N = |C| + |P | =3 8,999 total nodes comprising 38,995
customers, 4 product categories) and a node feature matrix
X ∈ RN ×2, where each row of X corresponds to ODC
and hubs score measures of a particular node, a single GCN
layer computes new node embeddings H(1) according to:
hi = σ
(
˜D− 1 2 ˜A ˜D− 1 2 XW ) .  (8)

L. M. Batrancea et al.
representations through localized neighbourhood sampling,
which mirrors how customers make purchasing decisions
based on limited information from their immediate network
context. Rather than requiring global graph information,
GraphSAGE recognizes that customer behaviour is pri -
marily influenced by their local network environment (i.e.,
product categories they directly engage with; purchasing
patterns of similar customers in their vicinity). The induc -
tive learning capability of GraphSAGE enables generaliza -
tion to previously unseen customers and product categories,
thus addressing a critical limitation of traditional collabora-
tive filtering approaches. This feature is valuable for e-com-
merce platforms experiencing rapid growth or seasonal
variations in customer behaviour, where the ability to make
predictions for new market segments without extensive his-
torical data becomes a competitive advantage.
By implementing these architectures on identical
weighted bipartite graphs with identical centrality-based
node features, we isolate the impact of architectural choices
on classification performance. This controlled compari -
son reveals which graph learning mechanisms contribute
most to exploiting relational information. It provides guid -
ance for practitioners that select architectures for specific
e-commerce analytics contexts, while advancing theoretical
understanding of how different GNN components interact
with network structure.
To assess the performance of GNN-based classifiers, we
rely on metrics that compare predicted labels to ground-
truth labels in a node-classification task. Accuracy serves
as a basic measure of overall correctness and is calculated
by dividing the number of correctly classified nodes by the
total number of classified nodes. Accuracy is given by:
Accuracy = TP +TN TP +TN +FP +FN ,  (11)
where TP  (true positives) are nodes correctly classified in
the positive class, TN  (true negatives) are nodes correctly
classified in the negative class, FP  (false positives) repre -
sent nodes mistakenly classified as positive, and FN  (false
negatives) denote nodes mistakenly classified as negative.
Although accuracy provides a straightforward indication
of how many nodes are correctly labelled in aggregate, it
offers limited granularity when misclassification costs or
class imbalance issues become pronounced in e-commerce
contexts.
For more nuanced insights, precision and recall are
employed. Precision measures the ratio of predicted posi -
tives that are truly positive and is computed as:
P recision = TP TP +FP .  (12)
importance and value. This attention-based approach aligns
with consumer culture theory, which emphasizes that pur -
chasing decisions are not uniformly weighted but reflect
hierarchical preferences, status considerations, identity con-
struction processes. The theoretical justification for GATs in
e-commerce contexts stems from their ability to model the
heterogeneous nature of customer-product relationships. In
digital marketplaces, not all interactions carry equal signifi-
cance. For instance, a high-value electronics purchase by a
premium customer should receive different analytical treat-
ment than routine household item purchases. GATs attention
coefficients assign higher weights to valuable interactions,
thus implementing a data-driven approach to the prioritiza -
tion of customer relationship that mirrors real-world busi -
ness practices.
GATs capture status-driven consumption patterns and
aspiration-based purchasing behaviours. The attention
mechanism can identify when customers engage with pre -
mium categories that signal social status or personal identity,
assigning higher importance to interactions in the learning
process. This capability enables GATs to detect subtle pat -
terns in consumption behaviour that reflect deeper sociolog-
ical phenomena (e.g., how customers use product categories
to construct and communicate identities). Learned attention
weights provide interpretable insights into which prod -
uct categories drive customer behaviour, offering valuable
intelligence for strategic marketing and product positioning
decisions.
Graph sample and aggregate (GraphSAGE) provides an
additional paradigm by enabling scalable batch training on
large-scale commerce graphs, which arise when using thou-
sands or millions of customers and products. The framework
draws a fixed-size sample from each node’s neighbourhood
and applies an aggregator function. If h(k) i  denotes node i
’s embedding at layer k, GraphSAGE updates it by concat -
enating h(k) i  with a permutation-invariant aggregator over
its neighbour embeddings, then applying a trainable trans -
formation. A layer update can be written as:
h(k+1) i = σ ( W (k) [ h(k) i AGG ({ h(k) j : j ∈ mathcalN (i) })]) ,  (10)
where || denotes concatenation and AGG is an aggregator
(mean, max pooling). In this scenario, each node’s initial
embedding includes hub score and authority score. Graph -
SAGE addresses the critical scalability challenges inherent
in large-scale e-commerce analytics, while maintaining the
relational modelling capabilities that is essential for under -
standing customer behaviour. The neighbour sampling
strategy of GraphSAGE becomes essential for computa -
tional feasibility without sacrificing analytical depth. In the
e-commerce context, GraphSAGE can learn meaningful

Decoding digital market power: a network-based framework for consumer behaviour and strategic advantage
captures authentic hierarchical market structures, validating
the graph’s suitability for GNN learning.
Our bipartite graph comprises a network of 38,995
nodes, each representing a unique customer, interconnected
by 44,802 weighted edges that map customers to distinct
product categories. The analysis focuses on four primary
product categories: auto & accessories, fashion, electronic,
home & furniture. Auto & accessories includes 6,258 nodes,
fashion dominates with 19,280 nodes, electronic comprises
1956 nodes, home & furniture encompasses 11,501 nodes.
Figure 2 presents the distributions of edge weights per
category.
In the edge weighting process, the parameter α was set
to 1, serving as a direct penalty factor for discounts applied
to transactions. This decision was grounded in the business
rationale that discounts diminish profitability across trans -
actions, regardless of their initial profit margins. Hence, the
model maintains a balanced and interpretable relationship
between discounts and overall transaction value, facilitating
straightforward comparisons and analyses across product
categories and customer segments. Parameter λ, represent-
ing the time-decay rate, was set to 0.001. This value imple -
ments a gradual exponential decay on the aging factor,
ensuring that the influence of older transactions diminishes
at a controlled pace.
For auto & accessories, edge weights are tightly concen-
trated around lower values, with a rapid decline as weights
increase. Namely, most customer-product interactions have
low significance, with only a small fraction of edges repre -
senting higher weights and indicating occasional high-value
purchases. In the fashion category, the distribution exhib -
its a similar pattern. Hence, while most interactions are
minor, the category includes occasional purchases of higher
weight, possibly driven by premium or bulk buying behav -
iour in specific product lines.
Electronics displays a sharp concentration of edge
weights at the lower end, with a frequency decline as
weights increase. The presence of minimal variation at
higher weights indicates that most interactions are consis -
tent on value and relevance, which suggests standardized
pricing. However, the distribution also hints at occasional
higher-weight interactions, potentially corresponding to
high-cost items or repeat purchases. In the home & furni -
ture category, the distribution demonstrates a sharp peak
at the lowest weights, with a gradual tapering as weights
increase. Compared to others, this category shows a slightly
broader tail: while most customer-product interactions are
low-weight, there is a wider range of variability. This could
be attributed to the diversity of items ranging from low-cost
decorative items to higher-value furniture purchases.
Table 6 presents category-specific networks
characteristics.
Recall measures the proportion of actual positives correctly
identified:
Recall = TP TP +FN .  (13)
These metrics become meaningful in an e-commerce set -
ting when focusing on a specific subset of customers or
products. For instance, precision is critical to ensuring that
a marketing campaign does not waste resources on uninter-
ested individuals (false positives). Recall becomes impor -
tant when aiming to capture as many genuinely interested or
high-value customers as possible (true positives).
A balanced way to combine precision and recall is the
F1-score, defined as:
F 1=2 × P recision×Recall P recision+Recall  (14)
This measure is useful in scenarios where false positives
and false negatives can incur tangible costs (e.g., misallo -
cating marketing funds; missing out lucrative customers).
In multi-class or multi-segment e-commerce applications,
these metrics can be extended through micro- or macro-
averaging to capture aggregate classification performance
or treat each class equally. By combining evaluation met -
rics with GNN architectures that exploit centrality-based
features, we obtain a robust mechanism for quantifying and
improving predictive performance in diverse e-commerce
contexts (e.g., targeted promotions; product assortment
optimization).
Results
Network results
Network analysis of weighted bipartite graph reveals three
fundamental patterns that validate our edge weighting
methodology and establish the foundation for GNN classi -
fication. First, edge weight distributions exhibit significant
category-specific variations, with electronics demonstrat -
ing higher mean weights (ANOV A F = 76.178, p < 0.001).
It indicates that this segment captures valuable customer
relationships through higher profitability and priority trans-
actions. Second, centrality measures differ across product
categories (MANOV A Wilks' λ = 0.6863, p < 0.001), with
fashion exhibiting highest out-degree centrality (indicating
broad customer engagement across categories). Electronics
shows elevated hubs score, which suggests connections to
high-authority categories despite lower transaction volume.
Third, the power-law-like edge weight distributions and
varied centrality patterns confirm that the bipartite network

L. M. Batrancea et al.
elevated median. This suggests a more diverse customer
base, where customers engage with product categories dis -
playing higher network authority.
The electronics category demonstrates a tighter distribu -
tion with lower variability and median hubs score that is
relatively low. This pattern reflects a more uniform engage-
ment pattern, where customer interactions with product
categories are consistent. The home & furniture category
presents a broader range of hubs scores, with a higher
median compared to electronics. This suggests a more
Figure 3 presents distributions of centrality measures of
nodes in each category. For hubs scores, the box plot shows
notable variability among categories. In the auto & acces -
sories category, hubs scores are generally low, with most
nodes clustered toward the lower end. Hence, most custom-
ers do not frequently engage with a diverse range of high-
authority product categories. However, a few outliers with
higher scores suggest the existence of key customers inter -
acting with highly authoritative categories. The fashion cat-
egory displays a broader range of hubs scores with a slightly
Product category Trans-
actions
(n)
Mean
edge
weight
Out-degree pattern Hubs score
pattern
Strategic role
Auto and accessories 6,258 0.84 High (broad
engagement)
Moderate Balanced, moderate
value
Fashion 19,280 0.85 Highest (maximum
breadth)
High Gateway category,
high diversity
Electronic 1,956 0.98*** Low (focused) Highest High value, influential
despite low volume
Home and furniture 11,501 0.83 High Moderate V olume-driven, stable
Table 6 Summary of category-
specific network characteristics
***Significantly different from
all other categories ( p < 0.001,
Tukey HSD post-hoc test)

Fig. 2 Distributions of edge weights

Decoding digital market power: a network-based framework for consumer behaviour and strategic advantage
The out-degree centrality distribution shows a slightly
different pattern. In auto & accessories, this metric has a
relatively high median, indicating that customers engage
with a broader range of product categories. However, the
varied customer base, with some customers actively engag-
ing with high-authority categories, while others maintain
lower connectivity.
Fig. 3 Distributions of centrality measures in each category

L. M. Batrancea et al.
stopping criterion was set with a patience of 20 epochs,
namely training would halt if no improvement in validation
loss was observed over 20 consecutive epochs. This strategy
safeguarded against excessive training and preserved the
most effective model state based on validation performance.
Comparative evaluation of GNN architectures reveals
high classification accuracy (94–95%) across all models,
with nuanced differences in category-specific performance
that show architectural trade-offs. GCN achieves the highest
overall accuracy (95%), with strong performance on fashion
(F1 = 0.94) and superior generalization across all categories.
GAT and GraphSAGE achieve 94% accuracy: GAT reports
perfect precision on fashion (1.00) at the cost of slightly
lower recall (0.87); GraphSAGE maintains more balanced
precision-recall trade-offs. All models exhibit a common
challenge in distinguishing fashion from electronics catego-
ries, with 5‒8% of electronics transactions misclassified as
fashion. It suggests that these categories share overlapping
network signatures, which might reflect lifestyle-based con-
sumption patterns where technology and fashion intersect.
A consistent 7‒8% improvement over traditional machine
learning methods (XGBoost: 87%) and 5‒6% gains over
conventional deep learning (CNN: 89%) validate the neces-
sity of graph-aware approaches for modelling customer-
product relationship.
The GCN model was designed with three convolutional
layers, incorporating residual connections between the first
and second layers to facilitate gradient flow and enhance
model stability. Batch normalization layers were strategi -
cally placed after each convolutional layer to standardize
activations. We used a dropout rate of 0.5 to introduce regu-
larization, which reduced the risk of overfitting by randomly
deactivating neurons during training. The architecture’s hid-
den layers were configured with a specific number of hidden
channels, balancing the model’s capacity to learn complex
patterns without incurring excessive computational costs.
The dropout rate followed the standard practices of graph
convolutional network regularization (Kipf and Welling
2017). This provides optimal balance between preventing
overfitting and maintaining sufficient network capacity for
learning complex graph patterns. For GAT, the dropout rate
was increased to 0.6 to account for the additional model
complexity introduced by multi-head attention mechanisms,
which create more trainable parameters susceptible to over-
fitting (Veličković et al. 2017). GraphSAGE employed a
dropout rate of 0.5 consistent with sampling-based archi -
tectures. These values align with architectures reported in
GNN literature and were validated through preliminary
experiments on sets registering optimal generalization per -
formance. The GraphSAGE model adopted a scalable aggre-
gation strategy, enabling efficient training on large-scale
e-commerce graphs by sampling fixed-size neighbourhoods
significant data spread and the outliers reveal heterogene -
ity, with some customers engaging across the network while
others are less active. For fashion, the out-degree centrality
demonstrates a more compact distribution with a slightly
lower median, reflecting moderate connectivity to product
categories. Electronics exhibits low variability and a lower
median out-degree centrality. Home & furniture displays a
broader distribution with a relatively high median, suggest-
ing that customers interact with multiple product categories.
Network analysis reveals fundamental insights into
the relational structure of e-commerce customer behav -
iour. Edge weight distributions demonstrate that our novel
weighting scheme differentiates transaction significance
across product categories. Namely, electronics shows the
most standardized interaction patterns. Home & furniture
exhibits the broadest value range, which reflects the catego-
ry’s diverse price points from decorative items to major fur-
niture purchases. This validates our theoretical premise that
not all customer-product relationships carry equal business
significance and supports the necessity of sophisticated edge
weighting beyond binary or frequency-based approaches.
Centrality measure distributions provide crucial evidence
for how network position reflects customer influence and
market hierarchies. The higher out-degree centrality in auto
& accessories and home & furniture categories suggests
these segments serve as “gateway” categories, with custom-
ers demonstrating broader engagement patterns across the
e-commerce ecosystem. Conversely, the more concentrated
hub scores in electronics indicate a category with clearly
defined high-authority relationships, aligning with our theo-
retical framework that premium categories create distinct
influence hierarchies. These patterns validate that central -
ity-based features capture meaningful structural positions
that traditional customer analytics would miss. It provides
graph neural networks with rich relational information that
reflects real-world customer behaviour dynamics.
Observed variations across categories demonstrate that
customer behaviour emerges from network position and
relational context. This supports our theoretical foundation
that e-commerce transactions exist within complex rela -
tional systems, where network structure shapes customer
classification patterns. It justifies the necessity of graph-
based approaches over traditional tabular methods for
understanding digital marketplace dynamics.
GNN results
We configured the hyperparameters of GNN models to
optimize performance in the context of e-commerce data
analysis. Each model was trained for a maximum of 300
epochs, with an early stopping mechanism that prevented
overfitting and ensured computational efficiency. The early

Decoding digital market power: a network-based framework for consumer behaviour and strategic advantage
< 0.001), indicate robust parameterization that captures gen-
uine relationship patterns. Figure 4 illustrates training and
validation loss curves for three different GNNs over multi -
ple epochs. For the GAT model, training and validation loss
curves show a steady decrease during early epochs, which
indicates effective learning as the model adjusts weights to
minimize errors. After 25 epochs, validation loss begins to
fluctuate slightly, while training loss decreases. This diver -
gence suggests that the model might be overfitting to the
training data and capture patterns in the training set that do
not generalize well to the validation set. In the GCN model,
loss curves exhibit a more consistent pattern, with training
and validation losses decreasing steadily. The gap between
the two curves remains relatively small, which indicates
that the model is generalizing well and avoiding significant
overfitting. The convergence of both loss curves at lower
values compared to initial epochs suggests that the GCN
effectively captures structural and feature information from
graph data. The GraphSAGE model displays a unique train-
ing and validation loss pattern compared to the other two
models. While the training loss decreases steadily, validation
loss exhibits periodic fluctuations before stabilizing at later
epochs. Fluctuations might be attributed to the sampling
strategy used in GraphSAGE, which can introduce vari -
ability in mini-batches during training. Despite fluctuations,
the eventual stabilization of validation loss suggests that the
model learns meaningful representations without significant
overfitting. Confusion matrices (Fig. 5) compare the clas -
sification performance of three different GNN architectures
across four categories. Each matrix highlights the distribu -
tion of predicted versus actual labels, offering insights into
the models’ classification accuracy and errors. For the GAT
model, diagonal entries in the confusion matrix are domi -
nant, indicating that the model achieves high accuracy in
correctly classifying samples within their respective catego-
ries. However, there are some noticeable misclassifications,
particularly between the fashion and electronics categories.
Therefore, the GAT model may struggle with distinguish -
ing these categories, potentially due to overlapping features
or shared characteristics in the input data. The classifica -
tion performance for home & furniture appears robust, with
a minimal number of misclassifications. The GCN model
demonstrates a similar trend, with strong performance
reflected by prominent diagonal values. Compared to GAT,
GCN exhibits fewer misclassifications, particularly in the
fashion and electronics categories. This improvement indi -
cates that the GCN architecture is better suited for capturing
distinctions between categories. The auto & accessories and
home & furniture categories show excellent classification
accuracy, with very few misclassifications. Thus, the model
leverages graph structure and node features to differentiate
categories. In the GraphSAGE model, the confusion matrix
for each node. This model consisted of three convolutional
layers, each followed by BatchNorm1d and dropout layers
with a dropout rate of 0.5. Hidden layers were configured to
maintain a balance between capturing intricate neighbour -
hood information and ensuring computational feasibility.
The aggregation function facilitated the extraction of salient
features from the sampled neighbourhoods, which enhances
the model’s ability to generalize across diverse customer
and product interactions.
Addressing inherent class imbalance in the dataset was a
critical aspect of the model training process. Label distribu-
tion revealed significant disparities among classes. Hence,
auto & accessories (count: 6258) and home & furniture
(count: 11,501) were more prevalent compared to fashion
(count: 19,280) and electronic (count: 1956). To mitigate
the adverse effects of this imbalance on model performance,
we employed class weighting during loss computation.
Specifically, weights were assigned and amplified the loss
contribution of underrepresented classes (auto & accesso -
ries, electronic), which ensured that models did not become
biased towards most classes. This weighting strategy
enhanced the model's sensitivity to minority classes, thus
improving the ability to classify less frequent categories
without compromising performance.
We used the Adam optimizer, renowned for its adaptive
learning rate capabilities and efficient handling of sparse
gradients, which are beneficial for training deep neural net-
works like GNNs. Learning rate was carefully selected to
balance convergence speed and stability, preventing oscil -
lations or premature convergence that could undermine the
model’s predictive capabilities. The integration of Batch -
Norm1d layers across models played a pivotal role in main-
taining consistent activation distributions.
Edge weighting parameters α and γ are grounded in
established frameworks that constrain reasonable variation
ranges. α ≥ 0 is a non-negative user-defined parameter that
sanctions discount usage, while γ ≥ 0 is a non-negative
time-decay rate. The discount penalty α =1  implements
standard accounting principles, where promotional dis -
counts reduce profitability dollar-for-dollar and represent a
neutral treatment without arbitrary amplification (Baumgart-
ner et al. 2012; Mishra et al. 2024). The temporal decay
of γ = 0.001 produces half-life of approximately 693 time
units. Hence, six-month-old transactions retain ~ 60% of ini-
tial weight, which aligns with RFM modelling conventions
where recency effects diminish substantially over typical
retail cycles (Hsu and Huang 2020; Frederick et al. 2002).
This exponential decay rate matches empirically observed
patterns, where recent transactions predict future behaviour
(Murphy et al. 2006). Theoretically constrained selections,
combined with demonstrated 7‒8% performance improve -
ments and statistically significant edge weight variations (p

L. M. Batrancea et al.
Fig. 4 Loss curves of training and valida-
tion of GNNs

Decoding digital market power: a network-based framework for consumer behaviour and strategic advantage
shows dominant diagonal values, indicating high classifica-
tion accuracy. However, similarly to the GAT model, there
are notable misclassifications between fashion and electron-
ics. While GraphSAGE performs well overall, it may face
challenges in handling fine-grained distinctions between
categories with overlapping features. Nonetheless, the clas-
sification performance for auto & accessories and home &
furniture remains strong, with few misclassifications. Train-
ing dynamics and classification performance results provide
compelling evidence that graph neural networks exploit the
relational structure embedded in our weighted customer-
product network to achieve a superior accuracy of customer
classification. The distinct training patterns exhibited by
each architecture demonstrate how different graph learning
mechanisms interact with our weighted bipartite network
structure. These patterns indicate that our edge weighting
scheme and centrality features provide sufficient signal
complexity to challenge sophisticated learning algorithms
while remaining learnable, thus indicating optimal balance
between information richness and model tractability.
Confusion matrix analysis reveals that all GNN architec-
tures achieve consistent high-accuracy classification across
most product categories, with the primary challenge being
the category distinction fashion-electronics. This specific
misclassification pattern is meaningful: certain customer
segments exhibit similar network positions and purchasing
behaviours across categories, possibly reflecting lifestyle-
based consumption patterns where technology and fashion
intersect (e.g., wearable technology, lifestyle electronics).
The consistent accuracy of models in the auto & accessories
and home & furniture classifications demonstrates that cen-
trality-based features capture the distinct network signatures
of categories, validating our theoretical framework.
Empirical results show that graph-based approaches can
achieve high accuracy while revealing meaningful business
insights about category relationships. The consistent perfor-
mance across architectures suggests that this methodologi -
cal framework provides robust foundations for graph neural
network learning. Misclassification patterns offer valuable
intelligence about customer behaviour overlap not detected
by traditional methods. This validates the technical superi -
ority and business relevance of our network-aware approach
to e-commerce customer analytics.
Benchmark model performance evaluation
We used comprehensive benchmark comparisons against
traditional machine learning models and conventional deep
learning architectures. This comparative analysis addresses
a critical gap in demonstrating why graph-based methods
are essential for capturing customer-product relationship
dynamics in digital marketplaces.
Fig. 5 Confusion matrices of GNNs

L. M. Batrancea et al.
traditional methods and a 5‒6% improvement over deep
learning approaches.
Performance advantages are consistent across prod -
uct categories, with GNNs demonstrating superior preci -
sion, recall, and F1-scores for auto & accessories, fashion,
electronic, home & furniture. Traditional models showed
more variability in handling different categories, with
performance ranging from 0.74 to 0.82 F1-scores across
categories, while GNNs maintained robust performance
across categories with F1-scores consistently exceeding
0.89. Results show that relational information embedded
in customer-product bipartite graphs contains critical sig -
nals that traditional approaches cannot fully capture. While
traditional models achieved respectable performance using
centrality-derived features, the consistent improvements
achieved by GNNs underscore the importance of network
topology in understanding e-commerce customer behaviour.
Traditional models capture important structural information
but miss dynamic interactions and higher-order dependen -
cies that define customer-category relationships.
The superior performance of graph neural networks
validates our theoretical premise: e-commerce transactions
exist within complex relational networks where customer
behaviour is influenced by network position, product cat -
egory connectivity, multi-hop relationships. This empirical
validation supports the use of graph-based approaches for
capturing the multidimensional nature of digital market -
place dynamics. This moves beyond traditional tabular data
analysis toward analytics of network-aware customers that
fully exploit the relational structure of e-commerce eco -
systems. Performance improvements represent meaningful
advances in classification accuracy that translate to substan-
tial business value when applied to large-scale customer
segmentation and targeted marketing strategies.
Discussion
Discussions of graph theoretical results
Our statistical analysis reveals significant variations in cus-
tomer-category interactions. We first conducted a one-way
analysis of variance (ANOV A) to assess whether mean edge
weights differed among product categories (Table 8).
ANOV A results were highly significant ( F-statistic of
76.178, p-value of 3.88 × 10 −49). We found differences in
the average edge weights across categories, justifying fur -
ther post-hoc analysis to elucidate the nature of differences.
We ran the Tukey’s Honestly Significant Difference
(HSD) test to conduct pairwise comparisons (Table 9).
Tukey HSD test results highlight that the electronic cat -
egory exhibited different edge weights compared to three
Hence, we implemented six benchmark models using
identical feature vectors with out-degree centrality and
hubs score measures. Traditional machine learning mod -
els included: Random Forest with 100 trees and balanced
class weights; Logistic Regression with L2 regularization
and balanced class weights; Support Vector Machine using
RBF kernel with balanced class weights; XGBoost with 100
estimators and balanced scale position weight. Additionally,
we implemented deep learning baselines including a convo-
lutional neural network with three 1D convolutional layers
followed by dense layers, and a long short-term memory
network with bidirectional architecture and attention
mechanism. All models utilized identical train-test splits
(80‒20%) and fivefold cross-validation for robust perfor -
mance estimation.
Comparative results (Table 7) reveal meaningful perfor-
mance disparities between graph neural networks and con -
ventional approaches. Traditional machine learning models
demonstrated accuracy ranging from 0.80 (Logistic Regres-
sion) to 0.87 (XGBoost), with macro F1-scores spanning
0.79 to 0.85. Deep learning models showed improved per -
formance, with CNN achieving 0.89 accuracy and LSTM
reaching 0.85 accuracy. Graph neural networks achieved
superior performance, with accuracies ranging from 0.94 to
0.95 and macro F1-scores from 0.93 to 0.94.
Performance gaps demonstrate the value of incorporat -
ing graph structure into e-commerce analytics. XGBoost
(i.e., the strongest traditional machine learning approach)
achieved 0.87 accuracy with 0.85 macro F1-score. CNN, a
superior deep learning baseline, reached 0.89 accuracy with
0.87 macro F1-score. However, GCN, the top-performing
graph neural network, achieved 0.95 accuracy with 0.94
macro F1-score, representing a 7‒8% improvement over
Table 7 Comprehensive performance comparison of benchmark mod-
els and graph neural networks
Model Accuracy Macro
Avg
precision
Macro
Avg
recall
Macro
Avg
F1-score
Weighted
Avg
F1-score
Traditional machine learning models
Random
Forest
0.84 0.83 0.82 0.82 0.84
Logistic
Regression
0.80 0.81 0.79 0.79 0.80
SVM 0.82 0.82 0.81 0.82 0.82
XGBoost 0.87 0.86 0.85 0.85 0.87
Deep learning models
CNN 0.89 0.88 0.87 0.87 0.89
LSTM 0.85 0.84 0.83 0.83 0.85
Graph neural network models
GAT 0.94 0.90 0.96 0.93 0.94
GCN 0.95 0.92 0.97 0.94 0.95
GraphSAGE 0.94 0.90 0.96 0.93 0.94

Decoding digital market power: a network-based framework for consumer behaviour and strategic advantage
more influential hubs within the e-commerce network. For
instance, a higher out-degree centrality in fashion compared
to electronic implies that customers interacting with fash -
ion products tend to engage with a broader array of product
categories, reflecting versatile purchasing behaviours and
effective cross-selling opportunities. Conversely, the elec -
tronic category, despite having a lower out-degree central -
ity, may exhibit a higher hubs score. Hence, it plays a pivotal
role in connecting customers to other product categories and
serving as a strategic anchor within the product ecosystem.
Moreover, the variation in hubs score across categories
highlights different levels of influence that each category
holds in the network. Categories with higher hubs scores
are likely to be central to customer interactions, acting as
key nodes that facilitate information flow and influence
across the network. Centrality can be leveraged for targeted
marketing strategies (e.g., personalized recommendations,
promotional campaigns) to maximize customer engagement
and drive sales.
Results imply that operational strategies should be tai -
lored to the unique centrality profiles of each product cat -
egory. For instance, categories exhibiting high out-degree
centrality may benefit from strategies aimed at enhancing
product diversity and fostering broader customer engage -
ment. Those with high hubs scores might focus on strength-
ening their role as pivotal connectors, which amplifies the
influence within the customer network.
other categories. Specifically, the mean difference between
auto & accessories and electronic was ‒ 0.1391 (p < 0.0001),
meaning that the electronic category had a higher mean edge
weight. Similarly, comparisons between electronic and both
fashion ( p < 0.0001) and home and furniture ( p < 0.0001)
yielded significant differences, which reaffirmed elevated
edge weights associated with the electronic category rela -
tive to these segments. Comparisons between auto & acces-
sories and fashion ( p = 0.9871), auto & accessories and
home and furniture ( p = 0.8435), and between fashion and
home & furniture (p = 0.9009) did not reach significance.
Regarding e-commerce, findings have important impli -
cations. The higher edge weights observed in the electronic
category imply that customer interactions are more robust,
potentially reflecting higher profitability, greater purchase
frequency, more recent transactions. This engagement level
could be attributed to factors like higher-value transac -
tions, frequent promotional activities, strategic importance
of electronic goods for platform revenue. The comparable
edge weights among auto & accessories, fashion, and home
& furniture suggest a more balanced customer interaction
landscape within these categories, indicating stable transac-
tional dynamics.
We conducted a multivariate analysis of variance
(MANOV A) that revealed compelling evidence of signifi-
cant differences in centrality measures across product cat -
egories (Table 10).
Results were highly significant and showed that both out-
degree centrality and hubs score varied significantly among
product categories. Our findings have relevant implications
for understanding customer behaviour and the strategic
positioning of product categories within the marketplace.
Out-degree centrality (i.e., whether customers engage with
multiple product categories) and hubs score (nodes serv -
ing as influential network connectors) are crucial metrics
for assessing the dynamism and interconnectedness of cus -
tomer interactions with different product segments.
Differences suggest that certain product categories com -
mand a higher degree of customer engagement and serve as
Table 8 One-way ANOV A for edge weights
Source DF Sum of Sq Mean Sq F-Statistic p-value
Category 3 50.104 10.701 76.168 3.88 × 10−49
Residual 44,798 9822.704 0.219
Table 9 Tukey's HSD test results for pairwise comparisons of edge weights in categories
Group 1 Group 2 Mean diff p-value Lower bound Upper bound Reject
Auto and accessories Electronic ‒ 0.1391 < 0.0001 ‒ 0.1666 ‒ 0.116 True
Auto and accessories Fashion 0.0021 0.9871 ‒ 0.0143 0.0186 False
Auto and accessories Home and furniture 0.0057 0.8435 ‒ 0.0121 0.0236 False
Electronic Home and furniture 0.1412 < 0.0001 0.1164 0.166 True
Electronic Home and furniture 0.1448 < 0.0001 0.119 0.1705 True
Fashion Home and furniture 0.0036 0.9009 -0.0097 0.0169 False
Table 10 MANOV A results for intercept and category effects
Effect Value Num
DF
Den
DF
F-statistics p-value
Intercept
Wilks’ lambda 0.4074 2 38,994 28,357.65  < 0.0001
Pillai’s trace 0.5926 2 38,994 28,357.65  < 0.0001
Hotelling-
Lawley trace
1.4545 2 38,994 28,357.65  < 0.0001
Roy’s greatest
root
1.4545 2 38,994 28,357.65  < 0.0001
Category
Wilks’ lambda 0.6863 6 77,988 2691.59  < 0.0001
Pillai’s trace 0.3172 6 77,990 2450.16  < 0.0001
Hotelling-
Lawley trace
0.4519 6 51,990 2936.83  < 0.0001
Roy’s greatest
root
0.4402 3 38,995 5722.09  < 0.0001

L. M. Batrancea et al.
customer interactions are correctly attributed without signif-
icant misclassifications. The combination of high precision
and perfect recall underscores the model’s effectiveness in
maintaining both sensitivity and specificity, which are criti-
cal for optimizing product placement and customer target -
ing within this segment.
The macro average F1-score of 0.9286 highlights the
model’s consistent and balanced performance across cat -
egories. This metric emphasizes the model's ability to gen -
eralize well across different classes without being biased
toward any category. Additionally, weighted average met -
rics confirm that the model maintains high performance. It
reinforces the robustness and reliability of the GAT model
in practical e-commerce scenarios.
Classification results (Table 12) demonstrate exceptional
performance in predicting interactions between online cus -
tomers and product categories.
With an overall accuracy of 95%, the GCN model dem -
onstrates its efficacy in leveraging the centrality-based
feature vectors to capture nuanced interactions customers‒
product categories. This high accuracy suggests that model
proficiently integrates structural and functional dynamics of
the bipartite graph, which ensures a reliable classification
performance across diverse categories. Delving deeper into
the individual category performances, the auto & accesso -
ries segment showcases an impressive precision of 0.92 and
a perfect recall of 1.00, culminating in an F1-score of 0.96.
Hence, the GCN model identifies nearly all true instances of
auto & accessories transactions and maintains a low rate of
false positives. Such performance is valuable for strategic
Discussions on GNN results
Classification outcomes derived from the GAT model
(Table 11) exhibit a commendable level of accuracy and
robustness in distinguishing among the distinct product cat-
egories within the e-commerce platform.
With an overall accuracy of 94%, the GAT model dem -
onstrates its effectiveness in leveraging centrality-based
feature vectors to capture interactions between customers
and product categories. This high accuracy underscores the
model’s capability to integrate the structural and functional
dynamics of the bipartite graph. Examining individual
category performances, the auto & accessories segment
showcases a precision of 0.90 and a perfect recall of 1.00,
culminating in an F1-score of 0.95. Hence, the GAT model
is highly effective in identifying true instances of auto &
accessories transactions without misclassifying other cate -
gories as belonging to this segment. The perfect recall high-
lights the model’s ability to capture genuine interactions,
while ensuring a comprehensive coverage and minimizing
the risk of overlooking significant customer engagements.
High precision confirms that most transactions classified
under auto & accessories are accurate.
For fashion, the model achieves an impeccable preci -
sion score of 1.00, this demonstrates its ability to classify
fashion transactions without false positives. However, the
recall for fashion stands at 0.87: while the model excels in
ensuring that identified fashion transactions are accurate, it
misses a small proportion of true fashion instances. Despite
this slight shortfall in recall, the F1-score of 0.93 remains
robust, signifying a strong balance between precision and
recall. This performance is valuable in e-commerce applica-
tions, where accurately identifying customer preferences is
crucial for targeted marketing and inventory optimization.
Electronics presents a precision of 0.82 and an outstand-
ing recall of 0.98, leading to an F1-score of 0.89. The high
recall rate signifies that the GAT model can identify nearly
all true electronic transactions, capturing substantial and
often high-value interactions typical for this segment. The
slightly lower precision suggests that while most predictions
of electronic transactions are correct, there are instances
where non-electronic transactions might be incorrectly
classified as electronic. The strong F1-score reflects a well-
rounded performance, highlighting the model’s proficiency
in handling categories that may possess more complex or
subtle interaction patterns inherent to high-value products.
Home & furniture demonstrates a precision of 0.89 and
a perfect recall of 1.00, resulting in an F1-score of 0.94.
The model excels in identifying all true instances of Home
& Furniture transactions while maintaining high preci -
sion. Hence, the GAT model is highly reliable in accurately
classifying transactions within this category, ensuring that
Table 11 Classification report for GAT
Category Precision Recall F1-score Support
Auto and accessories 0.90 1.00 0.95 1252
Fashion 1.00 0.87 0.93 3856
Electronic 0.82 0.98 0.89 391
Home and furniture 0.89 1.00 0.94 2300
Accuracy 0.94 7799
Macro Avg 0.90 0.96 0.93 7799
Weighted Avg 0.94 0.94 0.94 7799
F1-Score (Macro) 0.9286
Table 12 Classification report for GCN
Category Precision Recall F1-score Support
Auto and accessories 0.92 1.00 0.96 1252
Fashion 1.00 0.89 0.94 3856
Electronic 0.86 0.98 0.92 391
Home and furniture 0.90 1.00 0.95 2300
Accuracy 0.95 7799
Macro Avg 0.92 0.97 0.94 7799
Weighted Avg 0.95 0.95 0.95 7799
F1-score (Macro) 0.9430

Decoding digital market power: a network-based framework for consumer behaviour and strategic advantage
of 1.00, culminating in an F1-score of 0.95. This indicates
that model identifies all true instances of auto & accesso -
ries transactions. The recall indicates the model’s ability to
capture genuine interactions, while minimizing the risk of
overlooking significant customer engagements. Its preci -
sion confirms that most transactions classified under auto &
accessories are accurate.
For fashion, the model registers a precision score of
1.00, demonstrating its ability to correctly classify fashion
transactions without false positives. However, the recall
for fashion stands at 0.87, which indicates that it misses a
small proportion of true fashion instances. F1-score of 0.93
remains robust, suggesting a strong balance between preci -
sion and recall.
The electronic category has a precision of 0.82 and a
recall of 0.98, leading to an F1-score of 0.89. Hence, the
GraphSAGE model can identify nearly all true electronic
transactions. Precision suggests that there are instances
where non-electronic transactions might be incorrectly
classified as electronic. Nonetheless, the strong F1-score
reflects a well-rounded performance. The model can handle
categories that may possess more complex or subtle interac-
tion patterns inherent to high-value products.
Home & furniture registers a precision of 0.89 and a
perfect recall of 1.00, resulting in an F1-score of 0.94. The
model elicits all true instances of home & furniture transac-
tions. Hence, GraphSAGE is highly reliable in classifying
transactions within this category. High precision and perfect
recall underscore the model’s effectiveness in maintaining
sensitivity and specificity, which are critical for optimiz -
ing product placement and customer targeting within this
segment.
The macro average F1-score of 0.9285 highlights the
model’s consistent and balanced performance across cat -
egories, which addresses class imbalances within the data -
set. This metric emphasizes the model’s ability to generalize
across different classes without being biased toward any
category.
All models achieved accuracies around 94‒95%, dem -
onstrating their robust capability to classify customer
interactions into the four product categories. However,
subtle variations in precision, recall, F1-scores highlight the
unique mechanisms through which each GNN leverages the
network’s centrality measures and structural properties to
enhance classification performance. Concerning network
centralities, GCN’s residual connections facilitated deeper
integration of these features, allowing the model to harness
local and global structural information. The GAT’s attention
mechanisms enabled it to selectively focus on the most influ-
ential nodes, thereby enhancing its ability to capture critical
transactional patterns that drive high recall rates in pivotal
categories like electronic. GraphSAGE’s neighbourhood
decision-making, as it highlights the model’s capability to
recognize and prioritize high-engagement categories.
Fashion exhibits a precision score of 1.00, indicating the
model’s ability to correctly classify transactions without
misclassifications. Although the recall for Fashion stands
at 0.89, suggesting that a small proportion of true fashion
instances were not captured, the resulting F1-score of 0.94
remains high. This balance between precision and recall is
crucial in e-commerce, where the identification of customer
preferences can drive targeted marketing and inventory
optimization.
The electronic category (precision of 0.86, recall of 0.98)
achieves an F1-score of 0.92. The high recall rate indicates
that the GCN model is highly effective in identifying nearly
all true electronic transactions, capturing high-value inter -
actions. The lower precision suggests a few instances where
non-electronic transactions may have been incorrectly clas-
sified as electronic. Nonetheless, the strong F1-score reflects
a well-rounded performance, highlighting the model’s pro -
ficiency in handling categories that may possess more com-
plex or subtle interaction patterns.
Home & furniture demonstrates a precision of 0.90 and
a perfect recall of 1.00, resulting in an F1-score of 0.95.
The model excels in identifying all true instances of home
& furniture transactions while maintaining high precision.
These results stress the model’s ability to elicit distinctive
characteristics of home & furniture interactions, which is
essential for maintaining balanced and efficient inventory
and marketing strategies across all product categories.
The macro average F1-score of 0.9430 underscores the
model’s consistent and balanced performance across cate -
gories. This metric highlights the model’s ability to general-
ize well across different classes without being biased toward
any category.
Classification outcomes derived from the GraphSAGE
model (Table 13) exhibit a commendable level of accuracy
and robustness in distinguishing among product categories.
With an accuracy of 94%, the GraphSAGE model lever-
ages centrality-based feature vectors to capture the intricate
interactions customers‒product categories. Focusing on
individual category performances, the auto & accessories
segment showcases a precision of 0.90 and a perfect recall
Table 13 Classification report for GraphSAGE
Category Precision Recall F1-score Support
Auto and accessories 0.90 1.00 0.95 1252
Fashion 1.00 0.87 0.93 3856
Electronic 0.82 0.98 0.89 391
Home and furniture 0.89 1.00 0.94 2300
Accuracy 0.94 7799
Macro Avg 0.90 0.96 0.93 7799
Weighted Avg 0.94 0.94 0.94 7799
F1-score (Macro) 0.9285

L. M. Batrancea et al.
networks address a critical limitation of uniform neighbour
weighting by implementing learnable attention mechanisms
that prioritize customer-category interactions based on their
relative importance. Traditional graph methods and stan -
dard GCNs treat edges equally, failing to recognize that cus-
tomer relationships with premium product categories should
receive different analytical treatment than routine interac -
tions. GAT’s attention coefficients learn to assign higher
weights to valuable interactions. It implements a data-
driven approach to relationship prioritization that mirrors
real-world business practices where high-value customers
and strategic product categories receive different attention.
GraphSAGE overcomes the computational complexity lim-
itations through its innovative neighbour sampling strategy.
While traditional graph methods require processing com -
plete neighbourhood information (creating computational
bottlenecks for networks with 38,000 + nodes), GraphSAGE
maintains representational power through fixed-size sam -
pling that scales linearly with dataset size. This architec -
tural innovation enables applications of real-time customer
analytics where processing speed is crucial for dynamic
pricing, personalized recommendations, adaptive marketing
campaigns.
Theoretical implications
This study advances theoretical insights of digital consumer
behaviour across three interrelated domains: network soci -
ology, marketing, computational social science. First, our
findings empirically validate Granovetter’s ( 1985) embed-
dedness thesis in digital marketplace contexts by dem -
onstrating that customer value emerges from structural
network positions. The significant variation in centrality
measures across product categories confirms that market
hierarchies reflect relational dynamics. This extends social
network theory by operationalizing embeddedness through
quantifiable graph metrics that capture engagement breadth
and connection quality. It provides computational ground -
ing for sociological concepts previously examined mainly
through qualitative or survey-based methods.
sampling and aggregation strategies provided a scalable
approach to leverage centrality measures, maintaining high
classification performance even as the network grows in
complexity and size.
Our findings illustrate that GNN architectures offer dis -
tinct advantages depending on the specific classification
challenges and network characteristics. Residual connec -
tions and batch normalization excel in scenarios requiring
deep integration of centrality features. Models provide a
comprehensive toolkit for e-commerce businesses to clas -
sify and understand customer-category interactions They
facilitate data-driven strategies that enhance marketing pre-
cision, optimize inventory management, and drive business
growth through sophisticated graph-based machine learning
techniques.
Architectural advantages and limitations mitigation
The superior performance of GNN stems from their abil -
ity to process relational data and from how specific archi -
tectural innovations address fundamental limitations of
traditional methods and earlier graph-based approaches. To
validate these advantages empirically, we conducted com -
prehensive statistical testing of performance improvements
achieved by GNN architectures over benchmark models and
results (Table 14).
Statistical analysis confirms that GNN performance
improvements are not due to random variation but repre -
sent systematic advantages in capturing customer-product
relationship dynamics. Paired t-tests across fivefold cross-
validation results demonstrate that GNN architectures
achieve significant improvements over benchmark models
(p < 0.001), with effect sizes ranging from 5 to 9% improve-
ment in key metrics. Results provide robust empirical
evidence that graph-based approaches capture relational
information missed by traditional methods, validating the
theoretical necessity of network-aware customer analytics
in e-commerce contexts.
Each GNN architecture provides distinct mechanisms for
overcoming computational and theoretical constraints that
limit conventional approaches of customer analytics. GAT
Table 14 Statistical significance testing of GNN performance improvements
Comparison Metric Traditional ML (Best) GNN (Best) Improvement (%) t-statistic p-value
XGBoost vs GCN Accuracy 0.87 0.95  + 8.0 12.34  < 0.001**
XGBoost vs GCN Macro F1 0.85 0.94  + 9.0 11.78  < 0.001**
CNN vs GCN Accuracy 0.89 0.95  + 6.0 9.45  < 0.001**
CNN vs GCN Macro F1 0.87 0.94  + 7.0 8.92  < 0.001**
XGBoost vs GAT Accuracy 0.87 0.94  + 7.0 10.56  < 0.001**
XGBoost vs GAT Macro F1 0.85 0.93  + 8.0 10.12  < 0.001**
CNN vs GraphSAGE Accuracy 0.89 0.94  + 5.0 8.67  < 0.001**
CNN vs GraphSAGE Macro F1 0.87 0.93  + 6.0 8.23  < 0.001**
Statistical significance tested using paired t-tests across fivefold cross-validation results. ***p < 0.001 indicates highly significant improvements

Decoding digital market power: a network-based framework for consumer behaviour and strategic advantage
Second, category-specific centrality profiles inform dif -
ferentiated marketing strategies by optimizing the role of
each product segment within the customer network. The
dominance of fashion in out-degree centrality identifies
it as a gateway category. From a managerial standpoint,
investments in campaigns boosting the acquisition of fash -
ion items yields spillover benefits across categories, as
fashion purchasers demonstrate propensity for subsequent
cross-category engagement. Conversely, high hubs score
in electronics indicates that this segment attracts influential
customers whose purchasing behaviours (though less fre -
quent) carry disproportionate strategic importance. Practi -
cal implementation involves differentiating service quality
and loyalty program benefits toward electronics customers,
while recognizing their potential to influence broader con -
sumption patterns.
Third, edge weighting methodology provides operational
decision support for dynamic resource allocation across
customer relationships. By quantifying transaction signifi -
cance through integrated economic and behavioural factors,
managers gain systematic frameworks for prioritizing ser -
vice delivery, personalizing promotional offers, allocating
customer support resources. High edge weight relationships
(combining profitability, recency, priority) warrant premium
service commitments including expedited fulfilment, dedi -
cated account management, proactive engagement. From
an operational standpoint, companies should use automated
customer scoring systems within CRM platforms that trig -
ger service tier assignments and promotional targeting
based on real-time edge weight calculations updated with
each transaction.
Fourth, implementing graph neural network-based cus -
tomer analytics creates sustainable competitive advantages
through superior predictive accuracy and adaptive learning
capabilities. The 7‒8% performance improvement over tra-
ditional machine learning methods might appear modest but
it represents substantial value at scale: in customer bases
exceeding 100,000, this translates to 7000–8000 additional
correctly classified customers, which enables precise target-
ing that competitors with conventional methods would miss.
The scalability of GraphSAGE (validated through 3 billion
node deployments at Pinterest; Ying et al. 2018) ensures the
framework extends to enterprise-scale operations without
performance degradation. Strategically, an early adoption
of network-aware analytics establishes first-mover advan -
tages as competitors recognize limitations of demographic
segmentation.
Implementation roadmaps should prioritize three phases:
(1) pilot deployment on high-value customer segments to
demonstrate return on investment through improved target-
ing precision; (2) integration with existing CRM and mar -
keting automation systems to operationalize edge weight
Second, the integration of economic factors (profit,
discounts, shipping costs) with behavioural components
(recency decay, priority effects) into unified edge weights
represents a theoretical advancement in customer rela -
tionship measurement. Traditional RFM modelling treats
recency, frequency, and monetary value as separate dimen -
sions requiring post-hoc integration through scoring
schemes (Hsu and Huang 2020), while our approach syn -
thesizes these elements within the relational structure.
Third, GNN architecture comparison contributes to com-
putational social science methodology by isolating which
graph learning mechanisms (spectral convolution, attention,
sampling) capture relational information regarding cus -
tomer behaviour. The minimal performance variation across
architectures (94‒95% accuracy) suggests that relationship
structure contains sufficient signal for accurate classifica -
tion when quantified through weighted edges and central -
ity measures. This finding implies that network topology
shapes observable outcomes: the consistent 7‒8% improve-
ment over traditional methods empirically demonstrates
that relational patterns invisible to feature-based approaches
determine customer segmentation.
Theoretical contributions show that digital marketplace
dynamics require analytical frameworks, which integrate
sociological concepts of embeddedness, marketing princi -
ples of customer value, computational methods for learning
from network structure. By operationalizing abstract theo -
retical constructs (embeddedness, relational value) through
measurable network metrics and validating predictive power
through controlled GNN comparison, our research strength-
ens connections between grand social theory and empirical
computational analysis. Namely, it advances the interdisci -
plinary synthesis, which is essential for understanding con -
temporary digital economies.
Managerial implications
The business applications of our study manifest across
four strategic domains: customer segmentation, marketing
resource allocation, operational optimization, competitive
positioning. First, the demonstrated superiority of network-
based segmentation (94‒95% accuracy) over demographic
approaches provides actionable guidance for strategies of
customer relationship management. Managers should pri -
oritize customers exhibiting high out-degree centrality (i.e.,
engaging across multiple product categories) as prime can -
didates for cross-selling initiatives, since their diverse pur -
chasing patterns indicate receptiveness to broader product
portfolios. The 12‒15% improvement in targeting precision
over demographic-only approaches translates to reduced
marketing waste and enhanced conversion rates.

L. M. Batrancea et al.
domains while providing empirical evidence for hybrid
approaches that combine theories on rational choice and
temporal discounting. The framework enables three specific
business applications with measurable benefits including
customer segmentation strategies, which improve precision
by 12‒15% over purely demographic approaches. Product
category management can leverage authority scores to iden-
tify strategic categories that disproportionately influence
customer retention and cross-selling opportunities. At the
same time, the optimization of marketing campaigns can
utilize hub scores to identify influential customers whose
purchasing decisions create network effects that amplify
campaign reach beyond direct targeting.
The study acknowledges several limitations that con -
strain generalizability and suggest directions for future
development. The current framework relies on transac -
tional data without incorporating demographic or cultural
variables that significantly influence purchasing decisions
(income levels, cultural background, geographic location),
which mediate the relationship between network posi -
tion and customer behaviour. Parameters of fixed tempo -
ral decay assume uniform recency effects across customer
segments and product categories, while potentially missing
culturally or demographically variable notions relevant for
transactions. The class weighting approach to address cat -
egory imbalances does not tackle the underlying represen -
tational bias in customer coverage across market segments.
Additionally, despite superior performance, GNN models
remain relatively opaque on specific decision pathways,
which limits understanding among stakeholders and con -
straints practical deployment in regulated environments that
require algorithmic transparency.
Future research should pursue three targeted directions
that address limitations while building upon our study’s
contributions. Methodological extensions should develop
adaptive edge weighting schemes that incorporate demo -
graphic and cultural variables through multi-layer net -
work approaches. Studies should implement functions of
demographic-aware temporal decay that capture how cus -
tomer segments exhibit varying sensitivity to transaction
recency. Exploring GraphSMOTE and similar techniques
to address class imbalance and preserve network structure
represents a critical methodological advancement that could
enhance fairness and performance. Theoretical develop -
ment should integrate ethnographic and survey data with
network analytics to examine how computational find -
ings reflect broader societal phenomena (e.g., sustainable
consumption trends, post-pandemic purchasing behaviour
shifts). Applied research opportunities include longitudinal
studies that track the evolution of customer network posi -
tion to reveal how individuals move between market seg -
ments and how transitions relate to life events, economic
calculations and centrality-based segmentation; (3) orga -
nizational capability development to train marketing and
analytics teams in network thinking so that they interpret
and act on graph-based insights. The transparency of cen -
trality measures facilitates stakeholder communication and
cross-functional alignment, while overcoming adoption
barriers that face black-box machine learning approaches.
By grounding practical applications in validated theoreti -
cal frameworks and demonstrating measurable performance
improvements, our research provides strategic direction and
tactical implementation guidance for firms seeking competi-
tive advantage through network-aware customer analytics
in digital marketplace contexts.
Conclusions
This study makes four contributions to e-commerce cus -
tomer analytics: it develops and validates a theoretically-
grounded framework that integrates graph neural networks
with weighted bipartite network representations of cus -
tomer-product relationships. First, we introduced a novel
edge weighting scheme that integrates economic factors
via linear components and behavioural dynamics through
nonlinear temporal decay mechanisms, achieving a 5‒9%
classification accuracy improvements over traditional
machine learning methods and 7‒14% improvements
over unweighted graph approaches. This hybrid approach
addresses a critical gap in existing literature where cus -
tomer-product relationships are treated uniformly. Second,
through comprehensive evaluation of three GNN architec -
tures, we demonstrated that graph-based approaches con -
sistently outperform traditional methods across all product
categories. Third, we operationalized concepts of social
network theory within computational customer analytics.
We demonstrated how centrality measures capture mar -
ket hierarchies and customer influence patterns, therefore
bridging algorithmic outputs with established frameworks
in economic sociology and consumer culture theory. Fourth,
the framework enables customer segmentation that reflects
individual purchasing patterns and network position within
broader consumption ecosystems. This provides a reliable
foundation for automated customer analytics systems with
94‒95% classification accuracy across architectures.
These contributions generate significant theoretical and
practical implications that advance both academic under -
standing and commercial applications. Our findings validate
that customer behaviour in digital marketplaces emerges
from relational embeddedness. Observed centralities pat -
terns demonstrate how network position shapes the con -
struction of consumer identity and purchasing decisions.
This extends consumer culture theory into computational

Decoding digital market power: a network-based framework for consumer behaviour and strategic advantage
Arnould, E. J., and C. J. Thompson. 2005. Consumer culture theory
(CCT): Twenty years of research. Journal of Consumer Research
31(4): 868–882.
Ballestar, M. T., P. Grau-Carles, and J. Sainz. 2018. Customer seg -
mentation in e-commerce: Applications to the cashback business
model. Journal of Business Research 88: 407–414.
Banerjee, B. 2021. Cost accounting: Theory and practice . PHI
Learning.
Baumgartner, K., A. Fuetterer, and U. W. Thonemann. 2012. Supply
chain design considering economies of scale and transport fre -
quencies. European Journal of Operational Research  218(3):
789–800.
Bhatti, U. A., H. Tang, G. Wu, S. Marjan, and A. Hussain. 2023. Deep
learning with graph convolutional networks: An overview and
latest applications in computational intelligence. International
Journal of Intelligent Systems 2023(1): 8342104.
Boucherie, R. J., A. Braaksma, and H. Tijms. 2022. Operations
research: Introduction to models and methods. World Scientific.
Castells, M. 2010. The rise of the network society. Wiley.
Chen, C., L. Zheng, V . Srinivasan, A. Thomo, K. Wu, and A. Sukow.
2016. Conflict-aware weighted bipartite b-matching and its appli-
cation to e-commerce. IEEE Transactions on Knowledge and
Data Engineering 28(6): 1475–1488.
Choi, I. Y ., and J. K. Kim. 2009. Product network analysis to analyze
the purchase behavior of customers. Journal of the Korean Oper-
ations Research and Management Science Society 34(4): 57–72.
Close, A. G., and M. Kukar-Kinney. 2010. Beyond buying: Motiva -
tions behind consumers’ online shopping cart use. Journal of
Business Research 63(9–10): 986–992.
Corso, G., H. Stark, S. Jegelka, T. Jaakkola, and R. Barzilay. 2024.
Graph neural networks. Nature Reviews Methods Primers  4(1):
17.
de Souza Pereira Moreira, G. 2018. CHAMELEON: A deep learning
meta-architecture for news recommender systems. In Proceedings
of the 12th ACM conference on recommender systems, 578–583.
Deshpande, V ., and P. K. Pendem. 2023. Logistics performance, rat -
ings, and its impact on customer purchasing behavior and sales
in e-commerce platforms. Manufacturing & Service Operations
Management 25(3): 827–845.
Ebadi Jalal, M., and A. Elmaghraby. 2024. Analyzing the dynamics of
customer behavior: A new perspective on personalized market -
ing through counterfactual analysis. Journal of Theoretical and
Applied Electronic Commerce Research 19(3): 1660–1681.
Fernandes, N. O., M. Thürer, and S. C. Silva. 2024. DDMRP relative
priority for production execution: An assessment by simulation.
Operations Management Research 17: 1–13.
Fligstein, N. 2001. The architecture of markets: An economic sociol -
ogy of twenty-first-century capitalist societies. Princeton Univer-
sity Press.
Fourcade, M., and K. Healy. 2020. Seeing like a market. Socio-Eco-
nomic Review 18(1): 9–29.
Frederick, S., G. Loewenstein, and T. O’ Donoghue. 2002. Time dis -
counting and time preference: A critical review. Journal of Eco -
nomic Literature 40(2): 351–401.
Gligor, D. M., B. Davis‐Sramek, A. Tan, A. Vitale, I. Russo, I. Golgeci,
and X. Wan. 2022. Utilizing blockchain technology for supply
chain transparency: A resource orchestration perspective. Journal
of Business Logistics 43(1): 140–159.
Granovetter, M. 1985. Economic action and social structure: The
problem of embeddedness. American Journal of Sociology 91(3):
481–510.
Hsu, P. Y ., and C. W. Huang. 2020. IECT: A methodology for identi-
fying critical products using purchase transactions. Applied Soft
Computing 94: 106420.
conditions, cultural shifts. A cross-platform analysis that
examines how customer behaviour patterns transfer across
different e-commerce environments would enhance frame -
work generalizability.
The study demonstrates that effective e-commerce ana -
lytics requires the integration of computational sophistica -
tion with theoretical grounding from multiple disciplines.
This would treat customer-product networks as embodi -
ments of socio-economic relationships. Our framework val-
idates interdisciplinary approaches to digital marketplace
analysis that capture predictive accuracy and meaningful
business insights. The practical deployment of these meth -
ods in commercial environments can enhance the manage -
ment of customer relationships while providing insights
into broader market dynamics informing strategic decision-
making. It simultaneously enables critical examination of
how algorithmic systems might reproduce or challenge
existing market inequities. This integrated approach sup -
ports the development of more equitable digital commerce
ecosystems while advancing theoretical understanding and
practical capabilities in network-aware customer analytics.
The study paves the way for models that prioritize ethical
engagement and systemic equity alongside commercial
effectiveness in the digital marketplace.
Funding The authors received no funding for developing this research
study.
Data availability The datasets generated during and/or analysed dur -
ing the current study are available from the corresponding author on
reasonable request.
Declarations
Conflict of interest The authors declare no conflict of interest.
Open Access   This article is licensed under a Creative Commons
Attribution 4.0 International License, which permits use, sharing,
adaptation, distribution and reproduction in any medium or format,
as long as you give appropriate credit to the original author(s) and the
source, provide a link to the Creative Commons licence, and indicate
if changes were made. The images or other third party material in this
article are included in the article’s Creative Commons licence, unless
indicated otherwise in a credit line to the material. If material is not
included in the article’s Creative Commons licence and your intended
use is not permitted by statutory regulation or exceeds the permitted
use, you will need to obtain permission directly from the copyright
holder. To view a copy of this licence, visit  h t t p  : / /  c r e a  t i  v e c  o m m o  n s .  o
r g  / l i c e n s e s / b y / 4 . 0 /.
References
Alves, R., C. A. Pereira, and R. da Silva Lima. 2023. Operational cost
analysis for e-commerce deliveries using agent-based model -
ing and simulation. Research in Transportation Economics 101:
101348.

L. M. Batrancea et al.
Martens, D., F. Provost, J. Clark, and E. J. de Fortuny. 2016. Mining
massive fine-grained behavior data to improve predictive analyt -
ics. MIS Quarterly 40(4): 869–888.
Michael, P., A. R. Nobay, and D. A. Peel. 1997. Transactions costs and
nonlinear adjustment in real exchange rates; an empirical investi-
gation. Journal of Political Economy 105(4): 862–879.
Mishra, M., R. Kushwaha, and N. Gupta. 2024. Impact of sales promo-
tion on consumer buying behavior in the apparel industry. Cogent
Business & Management 11(1): 2310552.
Moran, P. 2005. Structural vs. relational embeddedness: Social capi -
tal and managerial performance. Strategic Management Journal
26(12): 1129–1151.
Murphy, J., C. Hofacker, and R. Mizerski. 2006. Primacy and recency
effects on clicking behavior. Journal of Computer-Mediated
Communication 11(2): 522–535.
Nofsinger, J. R., and A. Varma. 2013. Availability, recency, and sophis-
tication in the repurchasing behavior of retail investors. Journal
of Banking & Finance 37(7): 2572–2585.
Orlikowski, W. J. 2007. Sociomaterial practices: Exploring technology
at work. Organization Studies 28(9): 1435–1448.
Parikh, V ., and P. Shah. 2015. E-commerce recommendation system
using association rule mining and clustering. International Jour-
nal of Innovation and Advanced Computer Science 91: 944–952.
Piao, J., G. Zhang, F. Xu, Z. Chen, and Y . Li. 2021. Predicting customer
value with social relationships via motif-based graph attention
networks. Proceedings of the Web Conference 2021: 3146–3157.
Public Affairs.  h t t p s :   /  / w w  w . k  a g g  l  e .  c  o m  / d  a t a  s e  t  s / m e  r v  e m e  n e  k  s e / e  c o  m
m e  r c e - d a t a s e t. Accessed January 5, 2025.
Ren, H., W. Lu, Y . Xiao, X. Chang, X. Wang, Z. Dong, and D. Fang.
2022. Graph convolutional networks in language and vision: A
survey. Knowledge-Based Systems 251 : 109250.
Rogers, E. M. 2003. Diffusion of innovations, 5th ed. Free Press.
Schaschek, M., F. Gwinner, B. Hein, A. Winkelmann. 2023. From
black box to glass box: Evaluating the faithfulness of process pre-
dictions with GCNNs. In Joint European conference on machine
learning and knowledge discovery in databases, 233–249.
Sharma, K. 2024. The impact of e-commerce on operational cost effi -
ciency in modern businesses. Sachetas 3(3): 56–62.
Schulz, E. P., M. S. Diaz, and J. A. Bandoni. 2005. Supply chain
optimization of large-scale continuous processes. Computers &
Chemical Engineering 29(6): 1305–1316.
Teichman, D., and E. Zamir. 2022. Exponential growth bias and the
law: Why do we save too little, borrow too much, and fail to react
on time to deadly pandemics and climate change. Vanderbilt Law
Review 75: 1345.
Tuteja, S., and R. Kumar. 2022. A unification of heterogeneous data
sources into a graph model in e-commerce. Data Science and
Engineering 7(1): 57–70.
Veličković, P., G. Cucurull, A. Casanova, A. Romero, P. Lio,
Y . Bengio. 2017. Graph attention networks. arXiv preprint
arXiv:1710.10903.
Wang, X., X. He, M. Wang, F. Feng, T. S. Chua. 2019. Neural graph
collaborative filtering. In Proceedings of the 42nd international
ACM SIGIR conference on research and development in informa-
tion retrieval,  165‒174.
Wang, F., Y . Wen, T. Guo, J. Liu, and B. Cao. 2020. Collaborative
filtering and association rule mining-based market basket recom-
mendation on Spark. Concurrency and Computation: Practice
and Experience 32(7): e5565.
Wang, H., K. Wang, W. Zhang, Y . Zhang. 2024. Bipartite graph ana-
lytics: Current techniques and future trends. In 2024 IEEE 40th
international conference on data engineering (ICDE) 01–07.
Wu, Z., S. Pan, F. Chen, G. Long, C. Zhang, and S. Y . Philip. 2020. A
comprehensive survey on graph neural networks. IEEE Transac-
tions on Neural Networks and Learning Systems 32(1): 4–24.
Huang, K., and C. Chen. 2024. Subgraph generation applied in Graph-
SAGE deal with imbalanced node classification. Soft Computing
6:1–14.
Huang, Z., W. Chung, and H. Chen. 2004. A graph model for E-com -
merce recommender systems. Journal of the American Society for
Information Science and Technology 55(3): 259–274.
Jiang, X., H. B. Im, and M. A. Lee. 2024. Exploring the customer
perceived value of online grocery shopping: A cross-sectional
study of Korean and Chinese consumers using Means-End Chain
theory. Korean Journal of Community Nutrition 29(4): 318–335.
Kipf, T. N., M. Welling. 2017. Semi-supervised classification with
graph convolutional networks. In The 5th international confer -
ence on learning representations,  1‒14.
Lam, A. Y . C., R. Cheung, and M. M. Lau. 2013. The influence of
internet-based customer relationship management on customer
loyalty. Contemporary Management Research 9(4): 420–439.
Lazer, D. M., A. Pentland, D. J. Watts, S. Aral, S. Athey, N. Contractor,
et al. 2020. Computational social science: Obstacles and opportu-
nities. Science 369(6507): 1060–1062.
Leung, M. T., S. Pan, and M. Sun. 2017. A review of data analytic
methods and their applications in E-commerce research. Journal
of Current Issues in Media & Telecommunications 9: 56.
Li, L., and J. Zhang. 2021. Research and analysis of an enterprise
e-commerce marketing system under the big data environment.
Journal of Organizational and End User Computing 33(6): 1–19.
Lin, J., Y . Zhao, W. Huang, C. Liu, and H. Pu. 2021. Domain knowl-
edge graph-based research progress of knowledge representation.
Neural Computing and Applications 33: 681–690.
Lin, H., J. Lin, and F. Wang. 2022. An innovative machine learning
model for supply chain management. Journal of Innovation &
Knowledge 7(4): 100276.
Lismont, J., S. Ram, J. Vanthienen, W. Lemahieu, and B. Baesens.
2018. Predicting interpurchase time in a retail environment using
customer-product networks: An empirical study and evaluation.
Expert Systems with Applications 104: 22–32.
Liu, H., L. Lobschat, P. C. Verhoef, and H. Zhao. 2021a. The effect
of permanent product discounts and order coupons on purchase
incidence, purchase quantity, and spending. Journal of Retailing
97(3): 377–393.
Liu, J., G. P. Ong, and X. Chen. 2020. GraphSAGE-based traffic speed
forecasting for segment network with sparse data. IEEE Trans-
actions on Intelligent Transportation Systems 23(3): 1755–1766.
Liu, W., Y . Zhang, J. Wang, Y . He, J. Caverlee, P. K. Chan, D. S. Yeung,
and P. A. Heng. 2021b. Item relationship graph neural networks
for e-commerce. IEEE Transactions on Neural Networks and
Learning Systems 33(9): 4785–4799.
Liu, Z., and J. Zhou. 2020. Graph attention networks. Introduction to
Graph Neural Networks 6: 39–41.
Lu, G., X. Koufteros, and L. Lucianetti. 2017. Supply chain security:
A classification of practices and an empirical study of differential
effects and complementarity. IEEE Transactions on Engineering
Management 64(2): 234–248.
Lu, Y . W., Y . C. Tsai, and C. T. Li. 2024. Burstiness-aware bipartite
graph neural networks for fraudulent user detection on rating
platforms. Companion Proceedings of the ACM on Web Confer -
ence 2024: 834–837.
Luo, X. 2025. Reshaping coordination efficiency in the textile sup -
ply chain through intelligent scheduling technologies. Economics
and Management Innovation 2(4): 1–9.
Makanga, C., D. Mukwaba, C. L. Agaba, S. Murindanyi, T. Joseph,
N. Hellen, G. Marvin. 2024. Explainable machine learning and
graph neural network approaches for predicting employee attri -
tion. In Proceedings of the 2024 sixteenth international confer -
ence on contemporary computing, 2 43–255.

Decoding digital market power: a network-based framework for consumer behaviour and strategic advantage
Ömer Akgüller  Ömer Akgüller is an Associate Professor of Mathe -
matics at the Faculty of Science, Muğla Sıtkı Koçman University (Tur-
key). His research focuses on deep learning, manifold learning, and
complex network theory, with applications spanning financial market
analysis and biomedical data science. He has contributed extensively
to the development of graph-theoretic and geometric frameworks for
analysing high-dimensional data, including structural modelling of
neurological disorders, drug repurposing, and the topology of financial
networks.
Mehmet Ali Balcı  Mehmet Ali Balcı is a Professor of Applied Math-
ematics at the Faculty of Science, Muğla Sıtkı Koçman University
(Turkey). His research sits at the intersection of fractional calculus,
complex network theory, and mathematical modelling, with a partic -
ular focus on understanding dynamic processes in financial systems
and biological networks. He has made significant contributions to
the development of computational and analytical methods for study -
ing anomalous diffusion, hierarchical structures in stock markets, and
network-based approaches to real-world complex systems.
Anca Nichita  Anca Nichita is an Assistant Professor at the Faculty of
Economics, “1 Decembrie 1918” University of Alba Iulia, Romania.
Her main research interests include tax behaviour, consumer behav -
iour and cross-cultural studies on taxation. Her research has been pub-
lished in top-tier outlets such as the Journal of Economic Psychology,
Financial Innovation, Eastern European Economics, Social Indicators
Research.
Mircea-Iosif Rus  Mircea-Iosif Rus is the Director of the National
Institute for Research and Development in Construction, Urbanism
and Sustainable Territorial Development URBAN-INCERC from
Cluj-Napoca, Romania. His research interests include topics from
the fields of finance, research and development. He received various
awards in innovation and research.
Xu, D., C. Ruan, E. Korpeoglu, S. Kumar, K. Achan. 2020. Product
knowledge graph embedding for e-commerce. In Proceedings of
the 13th international conference on web search and data mining,
672–680.
Ying, R., R. He, K. Chen, P. Eksombatchai, W. L. Hamilton, J. Lesk -
ovec. 2018. Graph convolutional neural networks for web-scale
recommender systems. In Proceedings of the 24th ACM SIGKDD
international conference on knowledge discovery & data mining,
974‒983.
Yu, S., Z. Jiang, D. D. Chen, S. Feng, D. Li, Q. Liu, J. Yi. 2021. Lever-
aging tripartite interaction information from live stream e-com -
merce for improving product recommendation. In Proceedings of
the 27th ACM SIGKDD conference on knowledge discovery &
data mining, 3886–3894.
Zhang, H., and X. Gong. 2020. Consumer susceptibility to social influ-
ence in new product diffusion networks: How does network loca-
tion matter? European Journal of Marketing 55(5): 1469–1488.
Zhang, X., D. Xu, and L. Xiao. 2021a. Intelligent perception system
of big data decision in cross-border e-commerce based on data
fusion. Journal of Sensors 2021(1): 7021151.
Zhang, W., S. Deng, M. Chen, L. Wang, Q. Chen, F. Xiong, X. Liu,
H. Chen. 2021b. Knowledge graph embedding in e-commerce
applications: Attentive reasoning, explanations, and transferable
rules. In Proceedings of the 10th international joint conference on
knowledge graphs, 71–79.
Zhang, Y ., C. E. Montenegro-Marin, and V . G. Díaz. 2021c. Holistic
cognitive conflict chain management framework in supply chain
management. Environmental Impact Assessment Review  88 :
106564.
Zhang, L., J. Priestley, J. DeMaio, S. Ni, and X. Tian. 2021d. Measur-
ing customer similarity and identifying cross-selling products by
community detection. Big Data 9(2): 132–143.
Zuboff, S. 2019. The age of surveillance capitalism: The fight for a
human future at the new frontier of power.
Publisher's Note Springer Nature remains neutral with regard to juris-
dictional claims in published maps and institutional affiliations.
Larissa M. Batrancea Larissa M. Batrancea is a Professor of Finan-
cial Analysis at the Department of Business, Babes-Bolyai Univer -
sity from Cluj-Napoca, Romania. Her research interests range from
economic and financial analysis, family businesses, tax behaviour,
behavioural public finance, neurobusiness, cognitive neuroscience,
behavioural economics, financial and tax literacy to game theory
applied to business, wellbeing and sustainable economic growth. Her
research has been published in top-tier journals such as Journal of
Economic Psychology, Journal of Economic Behavior & Organiza -
tion, Financial Innovation, American Journal of Economics and Soci -
ology, Eastern European Economics, Social Indicators Research. In
2022, 2023 and 2024, she was included among the top 2% most cited
scientists in the world, according to the prestigious Stanford/Elsevier
ranking.
