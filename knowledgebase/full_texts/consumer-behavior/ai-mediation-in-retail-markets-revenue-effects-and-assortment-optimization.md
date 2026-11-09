---
title: 'AI-Mediation in Retail Markets: Revenue Effects and Assortment Optimization'
url: https://arxiv.org/abs/2610.12917
category: consumer-behavior
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Omar El Housni
- Marouane Ibn Brahim
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.12917
pages: 43
chars: 110944
fetched_at: '2026-11-08T13:17:28+00:00'
kb_version: 1
---

# AI-Mediation in Retail Markets: Revenue Effects and Assortment Optimization

AI-Mediation in Retail Markets:
Revenue Effects and Assortment Optimization
Omar El Housni Marouane Ibn Brahim
Cornell Tech, Cornell University
{oe46,mi262}@cornell.edu
October 12, 2026
Abstract
AI shopping assistants increasingly influence which products consumers consider. We study
retail assortment planning under AI mediation, where a retailer chooses a catalog, an AI interme-
diary forms a customer-facing shortlist, and the customer chooses from that shortlist according
to a multinomial logit model. We consider both deterministic mediation, in which the AI follows
a fixed segment-specific ranking, and stochastic mediation based on the Plackett–Luce model.
Empirically, we construct a dataset of product rankings from leading AI models, estimate
Plackett–Luce ranking models, and evaluate their predictive performance on held-out assort-
ments. Combining these estimates with synthetic customer preferences, we find that accounting
for AI mediation can materially change optimal assortments and revenue. Across the tested ca-
pacity configurations, ignoring mediation yields mean revenue losses between 2.52% and 11.37%
relative to the PL optimum. A much simpler deterministic plug-in, based only on the ordering
of fitted AI utilities, performs substantially better, with mean losses of at most 0.53%.
Motivated by this performance, we study assortment optimization under deterministic me-
diation. We characterize its computational complexity and show that, for any fixed number of
customer segments, the problem admits a fully polynomial-time approximation scheme.
1 Introduction
Assortment optimization is a central problem in retailing and e-commerce, where the goal is to
determine which products a retailer should make available to customers in order to maximize ex-
pected revenue or other business objectives, subject to operational, capacity, or display constraints.
A large literature has developed models and algorithms that translate customer-choice behavior
into concrete prescriptions for the retailer’s assortment decision. A common feature of this clas-
sical paradigm, however, is that the retailer directly controls the set of products from which the
customer ultimately chooses. This direct-control assumption is challenged when customers turn to
generative-AI systems such as ChatGPT, Claude, and Gemini to streamline their shopping deci-
sions. Recent consumer surveys point to rapidly growing use of these systems for product discovery,
1
arXiv:2610.12917v1  [cs.AI]  9 Oct 2026

comparison, and recommendation. For example, Capgemini Research Institute (2025) reports that
58% of consumers surveyed across 12 countries use generative-AI tools as a source of product and
service recommendations, compared with 25% in 2023.
When an AI intermediary stands between the retailer and the customer, the retailer no longer
directly controls the customer-facing assortment. Instead, the retailer may expose a larger machine-
facing catalog, from which the AI filters or ranks a smaller set of products for the customer. Because
the AI’s ranking criterion need not coincide with the retailer’s revenue objective, this additional
layer may change the retailer’s optimal assortment decision. It raises both a descriptive and a
prescriptive question:
What are the revenue consequences of AI-mediated shopping for retailers? How should
retailers adapt their assortment decisions when an AI intermediary determines which
products customers see?
In this paper, we develop a framework for assortment planning when product exposure is me-
diated by an AI system, with the goal of understanding how this additional layer affects retailer
revenue and optimal assortment decisions. Empirically, we collect controlled ranking data from
several leading AI models across different shopper profiles, use these data to estimate models of
AI ranking behavior, and combine the fitted models with controlled customer-preference scenarios
to study the economic consequences of AI mediation. Theoretically, we analyze assortment opti-
mization under deterministic mediation, characterize its computational complexity across different
parameter regimes, and develop exact and approximation algorithms where possible.
Informal model description.We introduce a stylized model of AI-mediated assortment op-
timization that isolates this additional decision layer and allows us to study both its revenue
consequences and the resulting assortment problem. A retailer has access to a universe of sub-
stitutable products, each generating a product-specific revenue when purchased. The retailer first
selects a feasible machine-facing catalog, without observing the arriving customer’s segment. An
AI intermediary then maps this catalog into a smaller customer-facing set according to a known,
possibly stochastic and segment-dependent recommendation rule. The customer observes only this
AI-generated shortlist and chooses either one of its products or an outside option representing no
purchase. If a product is purchased, the retailer receives the corresponding revenue. Thus, unlike in
classical assortment optimization, the retailer controls the set available to the intermediary but not
necessarily the set from which the customer ultimately chooses. Figure 1 illustrates this decision
sequence. Section 2 formalizes this decision sequence, the recommendation kernels considered in
the paper, and the customer’s choice model. In a nutshell, we study two stylized models of how the
AI selects which products to show. Underdeterministic mediation, each AI system and customer
profile induces a fixed ranking of products, and the AI displays the highest-ranked products among
those offered by the retailer, up to its display capacity. UnderPL-stochastic mediation, the ranking
itself is random and follows the classical Plackett–Luce (PL) model (Luce, 1959; Plackett, 1975),
with the AI again displaying the highest-ranked products in the realized ranking. To connect these
2

Retailer selects assortment S
 Before customer arrival
1
2
3
4
5
6
Available products
Segment t
“Find a good-
value option.”
Preferences / persona
AI
Top K
 1
3
5
C ⊆ S; |C| ≤ K
Purchase i ∈ C
No purchase (0)
Customer arrives
Customer prompts
AI ranks & filters
Consideration set
Customer chooses
Figure 1: AI-mediated shopping sequence.
models to actual AI behavior, we conduct a controlled study in which we query leading AI mod-
els as shopping assistants for customers with different profiles, and use the resulting ranking data
to calibrate and evaluate the models. We use both mediation models to study how AI-mediated
product exposure affects retailer revenue, and develop the algorithmic and theoretical analysis of
the retailer’s assortment-planning problem under deterministic mediation.
1.1 Main Contributions and Technical Ideas
Our contributions combine an empirical study of AI ranking behavior, an analysis of how AI medi-
ation affects retailer revenue and assortment decisions, and complexity results and approximation
algorithms for assortment optimization under deterministic mediation. We first construct a con-
trolled dataset of AI recommendations by prompting several AI models, and use these data to
estimate and validate Plackett–Luce (PL) models of their ranking behavior. Using the fitted mod-
els in semi-synthetic experiments, we find that accounting for mediation leads retailers to choose
smaller assortments on average, sometimes avoiding AI filtering altogether. Ignoring mediation can
produce substantial revenue losses. To assess the value of modeling randomness in AI recommenda-
tions, we also consider a deterministic approximation: we rank products by their fitted AI utilities
and optimize the assortment under this fixed ordering. When evaluated under the stochastic PL
model, the resulting assortments recover nearly all of the optimal PL-mediated revenue on average
in our experiments. We also show how display capacity and customer–AI preference alignment
affect these conclusions. On the theoretical side, we characterize the computational complexity of
assortment optimization under deterministic mediation and develop a fully polynomial-time ap-
proximation scheme for any fixed number of customer segments.
Empirical characterization and estimation of AI rankings.In Section 3, we study whether
a tractable ranking model can describe the recommendations of AI shopping assistants. Unlike a
latent consideration process inferred from purchases, the AI’s recommendations can be observed
directly by querying AI models with chosen product sets and customer profiles. We use this access
3

to construct ranking data, estimate the mediation layer, and evaluate how well the fitted model
predicts AI rankings for assortments not used in estimation.
(a)Ranking data construction and model fitting.We generate 32,400 ranked recommendation
lists by prompting models from OpenAI, Anthropic, and Google with real product listings
from three categories: Lightning chargers, robot vacuums, and pet leashes. Each model is
queried under three customer personas: budget-sensitive, value-seeking, and premium-seeking,
which are explicitly specified in the prompts. Each query asks the AI to rank five products
from a retailer assortment of ten. We estimate a separate PL model for each category and
provider–persona pair, using a ridge-regularized maximum-likelihood approach. We show that
the resulting regularized log-likelihood is strictly concave and therefore admits a unique finite
maximizer, which can be computed efficiently.
(b)Out-of-sample validation.We evaluate the fitted PL models on 5,400 held-out AI rankings
whose underlying offer sets were not used for estimation. For each held-out offer set, we use
the estimated PL utilities to rank the ten offered products and compare this predicted ranking
with the recommendation returned by the AI. The product with the highest estimated utility
coincides with the AI’s first-ranked product in 78.8% of observations. The average negative
log-likelihood is 3.312 per held-out ranking, compared with 3.360 on the training sample,
indicating essentially no deterioration on previously unseen offer sets. These results suggest
that the fitted PL models capture a substantial part of the ranking behavior observed in the AI
recommendations. The fitted utilities also provide a natural deterministic approximation: for
each segment, we simply rank products from highest to lowest estimated utility. In Section 4,
we study whether assortments optimized using this simpler fixed ranking continue to perform
well when evaluated under the stochastic PL model.
Experimental effects of mediation on assortments and revenue.Our main economic finding
is that ignoring mediation can be costly. Surprisingly, accounting only for the ordering of AI
preferences, rather than the exact PL fitted utilities, captures most of the attainable revenue in
our experiments. Section 4 develops this conclusion by combining the estimated AI-ranking models
with synthetic customer-side MNL preferences. We compare three policies: optimization under
stochastic PL mediation, optimization under the induced deterministic rankings, and a direct-MNL
benchmark that ignores the mediation layer. All policies are evaluated under the same fitted PL
mediation model. Throughout, we consider a cardinality-constrained setting in which the retailer
may offer at mostBproducts, and the AI displays at mostKproducts to the customer, whereB
andKare exogenous positive integers.
(a)AI mediation leads to lower-cardinality assortments.When the retailer accounts for AI me-
diation, it generally chooses to offer fewer products than when it ignores the AI. Across the
tested configurations, the direct-MNL assortment contains 1.48 to 4.15 more products on av-
erage than the PL-optimal assortment. There are two ways in which the retailer responds to
4

the AI’s display limitK. In some instances, the retailer offers more thanKproducts and
allows the AI to choose whichKproducts the customer sees. In other instances, the retailer
instead reduces its assortment toKproducts or fewer, so that every product it offers is shown
to the customer.
(b)Ignoring mediation creates substantial losses, especially when display capacity is tight.The
direct-MNL policy incurs mean revenue losses ranging from 2.52% to 11.37% across the con-
sidered parameter configurations, relative to the PL-optimal assortment. The losses are not
confined to averages: the configuration-specific 95th percentiles range from 10.36% to 30.66%,
and the largest individual loss is 57.08%. Moreover, losses tend to be larger when the AI
displays fewer products to the customer.
(c)A deterministic plug-in recovers nearly all optimal revenue on average.We next ask how much
is lost if the retailer accounts for the AI’s ranking of products but ignores the randomness in
those rankings. The deterministic model keeps the same segment-specific product ordering
and customer-choice model, but assumes that the AI always follows a fixed ranking. For each
instance, we optimize the assortment under this deterministic model and then evaluate the
resulting assortment under the fitted stochastic PL model. Across the tested configurations,
the mean revenue loss relative to the PL optimum ranges from only 0.08% to 0.53%. These
losses are far smaller than those obtained when the retailer ignores mediation altogether,
suggesting that most of the value of accounting for mediation comes from capturing the AI’s
average ranking of products rather than the full stochastic variation in its recommendations.
(d)Preference alignment reduces the cost of ignoring mediation.We vary how strongly synthetic
customer preferences align with a persona-level summary of the fitted AI preferences, using
an alignment parameterρ∈[0,1], where a largerρrepresents higher alignment. Deferring
the formal definition of alignment to Section 4, this parameter controls the portion of the
customer’s utility which is aligned with the AI and a complementary random portion capturing
each customer’s idiosyncrasies. Mean direct-MNL revenue losses range from 5.75% to 24.06%
whenρ= 0, compared with 0.59%–5.74% whenρ= 1, although the intervening relationship
is not always monotone.
(e)Greater alignment can make retailers more willing to allow filtering.The lower cost of ignoring
mediation at higher alignment does not mean that filtering disappears. Atρ= 0, active
filtering occurs in at most 8.9% of instances across capacity configurations; atρ= 0.95, its
share ranges from 44.4% to 66.7%. Thus, greater alignment can make it optimal to leave more
products for the AI to filter.
Computational complexity and approximation under deterministic mediation.The eco-
nomic performance of the deterministic plug-in motivates studying the corresponding assortment
optimization problem. In particular, we consider the cardinality-constrained setting in which the
5

retailer may offer at mostB≥1 products. In Section 5, we characterize its computational com-
plexity in terms of the number of segmentsmand display capacityK. We then construct an
approximation scheme for any arbitrary precision. Here,ndenotes the number of products.
(a)Complexity landscape under deterministic mediation.When the number of segmentsmis un-
restricted, deterministic mediated assortment optimization is NP-hard even forK= 1 and
B=n. Moreover, for every fixedϵ∈(0,1), the problem admits no polynomial-timeO(n 1−ϵ)-
approximation unless P = NP. Our reduction is from assortment planning under ranking
preferences (Aouad et al., 2018). At the same time, the problem becomes tractable in several
important parameter regimes. In particular, we show that there exists an optimal assort-
ment containing at mostmKproducts, since we can safely remove any product that is never
displayed to any segment. Consequently, when bothmandKare fixed, enumerating these
bounded-size assortments gives a polynomial-time exact algorithm. With a single segment, the
problem is also polynomial-time solvable for arbitraryK, because it reduces to a cardinality-
constrained MNL assortment problem. In contrast, fixingm≥2 alone does not recover exact
polynomial-time solvability: takingK=B=nrecovers assortment optimization under a mix-
ture of MNL models, which is weakly NP-hard already with two segments (Rusmevichientong
et al., 2014). The resulting complexity landscape is summarized in Table 4.
(b)An FPTAS for a fixed number of segments.Our main algorithmic contribution for the deter-
ministic mediated assortment problem is an approximation scheme that, for anyϵ∈(0,1),
returns a feasible assortment whose revenue is at least 1−ϵtimes optimal. For every fixedm,
the running time is polynomial in the binary encoding length of the instance and 1/ϵ, yielding
a fully polynomial-time approximation scheme (FPTAS). The key idea is to enumerate the
worst-ranked displayed product for each segment, which we refer to as threshold products.
Fixing these thresholds determines which selected products contribute to each segment’s dis-
played set, provided that exactlyKselected products lie at or above its threshold. Conditional
on these thresholds, the objective is a sum ofmratios of affine functions. We approximate this
objective using a framework for sums of ratios, whose exact-solvability condition is verified
through multidimensional knapsack.
1.2 Related Literature
Assortment optimization.Assortment optimization studies how a retailer should select a sub-
set of products from a larger universe when customers substitute among the products made available
to them; see K¨ ok et al. (2009) for a broad review. In their seminal paper, Talluri and Van Ryzin
(2004) formulate choice-based revenue management under a general discrete-choice model and iden-
tify the revenue-ordered structure of optimal assortments under the multinomial logit model. A
large subsequent literature develops structural and algorithmic results under richer models of sub-
stitution, including the nested logit model (Gallego and Topaloglu, 2014; Feldman and Topaloglu,
2015) and the Markov-chain choice model (D´ esir et al., 2020, 2024). Other work studies oper-
6

ational or distributional restrictions on the retailer’s decision, including cardinality and capacity
constraints (D´ esir et al., 2022), minimum-visibility requirements (Barr´ e et al., 2026), fairness or
exposure constraints (Lu et al., 2023; Chen et al., 2022) and covering constraints (El Housni et al.,
2024). Although these papers differ substantially in their choice models, objectives, and feasi-
ble assortment families, the core decision sequence is generally the same: the retailer chooses the
customer-facing assortment, and the customer chooses directly from that set. Our model inserts
an additional decision layer. The retailer chooses a machine-facing catalogS, while the customer-
facing setC⊆Sis generated by an AI intermediary. The retailer therefore controls the input to
the mediation rule rather than the set from which the customer ultimately chooses.
Consider-then-choose models.The closest line of research to our paper is the literature on
consideration sets in customer choice. Marketing models have long recognized that consumers
may first screen a large set of alternatives and then choose only among those that survive the
screening stage. Early work explains consideration-set formation through evaluation costs and the
incremental value of examining additional alternatives (Hauser and Wernerfelt, 1990; Roberts and
Lattin, 1991). In a stochastic-choice formulation, Manzini and Mariotti (2014) assume that each
alternative is independently considered with an alternative-specific attention probability before the
consumer selects the most preferred considered alternative.
Within the operations literature, Aouad et al. (2021) develop a general dynamic-programming
framework for assortment optimization under structured consider-then-choose models, in which
products are first screened and then ranked. The closest mathematical connection to our general
formulation is the click-based MNL model of Aouad et al. (2025). In that model, a customer
considers only the products that she clicks and subsequently chooses among the clicked products
according to an MNL model. The seller selects the set of products made available for purchase,
and the authors establish a polynomial-time approximation scheme for the resulting assortment
problem. Gallego and Li (2024) operationalize this random-consideration-set model for demand
estimation, assortment optimization, and pricing.
In our paper, we consider a different class of first-stage mediation mechanisms. As formalized
in Section 2, we study two ranking-based models of AI mediation. In the first, each customer
segment is associated with a deterministic ranking of the products, and the AI displays the top
Kproducts from the retailer’s machine-facing catalog according to this ranking. In the second,
the AI’s ranking is stochastic and follows the classical Plackett–Luce model (Plackett, 1975; Luce,
1959): each product is assigned a positive weight, a random ranking is generated according to these
weights, and the AI displays the topKproducts in that ranking. To the best of our knowledge,
these ranking-based mediation mechanisms, and the resulting assortment-optimization problems,
are not captured by the consideration-set models studied in the existing assortment-optimization
literature. A key difference in our setting is that the consideration set is generated by an AI system
rather than formed internally by the consumer. In traditional consider-then-choose models, the
consumer’s consideration set is typically latent and must be inferred indirectly from observed choices
or auxiliary data. Here, while the consideration sets encountered in actual shopping interactions
7

are still not directly observed by the retailer, the underlying AI systems can be queried in controlled
settings with chosen product sets and customer profiles. This makes it possible to generate targeted
ranking data, fit tractable and interpretable models of AI behavior, and then use those models for
revenue analysis and assortment optimization.
AI-shopping agents.A growing literature studies how AI systems alter product discovery, rec-
ommendation, and purchasing. Allouah et al. (2026) study the behavior of AI shopping agents when
they are asked to choose products from a given assortment. Through controlled experiments across
several AI models, they document systematic responses to product and marketplace attributes, in-
cluding prices, ratings, reviews, listing positions, and platform endorsements, as well as substantial
heterogeneity across AI models in the choices they induce. Their setting treats the AI agent as the
final decision maker, and the main objective is descriptive: to understand and model how the AI
chooses among available products. Our paper instead studies a different decision process in which
the AI first filters the retailer’s assortment and the customer then makes the final purchase decision
from the resulting recommendation set. This additional layer creates a prescriptive problem for
the retailer: how should the assortment be chosen when the retailer controls the products made
available to the AI, but the AI controls which of those products the customer ultimately sees? Our
focus is therefore on the retailer’s assortment-planning problem and on the revenue implications
of this additional mediation layer. At the retailer-controlled end of the spectrum, Liu and Chen
(2026) develop an inventory-aware agentic policy for basket recommendation that jointly accounts
for personalization, product availability, and operational constraints. In that setting, the recom-
mendation agent is itself a decision instrument of the retailer, whereas we treat the AI intermediary
as a separate behavioral layer whose ranking objective need not coincide with the retailer’s revenue
objective.
Several recent papers instead study how a shopping agent should interact with or act on behalf
of a consumer. Cao and Hu (2026) introduce a solicit-then-suggest model in which an agent asks
a sequence of preference-elicitation questions and then recommendskproducts. They characterize
the trade-off between solicitation depth and recommendation-set breadth, as well as the structure
of the agent’s optimal elicitation and recommendation policy. Dong et al. (2025) study costly
and noisy communication between a customer and a recommendation agent, jointly optimizing the
information communicated by the customer and the diversity of the agent’s recommendation set.
Fu and Hu (2026) study a buying agent that monitors prices over time and determines when to
purchase on the consumer’s behalf. These papers optimize the agent’s information acquisition,
recommendation, or purchasing policy from the consumer’s perspective. We instead study the
higher-level prescriptive problem faced by the retailer: taking the intermediary’s behavior as given
or estimated, how should the retailer choose its assortment when the intermediary, rather than the
retailer, determines which products are ultimately exposed to customers?
Random-utility , Plackett-Luce, and multinomial logit models.Our ranking and customer
choice specifications build on the random-utility literature. In a random-utility model, each alterna-
8

tive receives a deterministic utility component and a random shock, and the selected alternative is
the one with the highest realized utility (McFadden, 1974). When the shocks are independent stan-
dard Gumbel-distributed random variables, the probability that an alternative attains the highest
utility has the multinomial-logit form associated with Luce’s choice axiom and conditional logit
(Luce, 1959; McFadden, 1974). The MNL model is widely used in assortment optimization because
its choice probabilities admit a parsimonious closed form, although its independence-of-irrelevant-
alternatives structure can be restrictive. The Plackett–Luce model extends the same probability
structure from a single choice to an ordered ranking (Luce, 1959; Plackett, 1975). It can be gener-
ated by sorting alternatives according to independent Gumbel-perturbed utilities. The relationship
between the two models is therefore probabilistic rather than terminological: MNL describes the
top-ranked alternative, whereas Plackett–Luce describes an ordered sequence of alternatives.
We use this family of models at two distinct stages. On the AI side, segment-tPlackett–Luce
weightsw it govern a random ranking of the products in the seller’s catalog, and the AI displays
the products occupying the firstKpositions. On the customer side, separate MNL weightsv it,
together with an outside option, govern the customer’s purchase decision from the displayed short-
list. These are different behavioral primitives: the AI-side weights determine exposure, whereas the
customer-side weights determine substitution and purchase conditional on exposure. We impose no
requirement that the two sets of utilities coincide, and study the effect of alignment in Section 4.
The remainder of the paper is organized as follows. Section 2 presents the model; Section 3
describes the AI-ranking data, estimation, and validation; Section 4 studies the economic effects
of mediation through numerical experiments; Section 5 develops the deterministic complexity and
approximation results.
2 Model Formulation
This section formulates the AI-mediation model used throughout our work, by modelling the inter-
action between the retailer and the customer through an AI intermediary. The central distinction
from classical assortment optimization is that the retailer does not directly choose the set from
which customers make purchase decisions. Instead, the retailer first selects a machine-facing cata-
log, then an AI intermediary maps this catalog into a smaller customer-facing set, and finally, the
customer chooses from the mediated set. We define this process through a general recommendation
kernel in Section 2.1, and specialize our model to ranking-based kernels in Section 2.2.
2.1 General Model of AI-Mediation
Products and customer segments.LetN={1, . . . , n}denote a universe of substitutable
products, with each producti∈Ngenerating revenuer i >0 when purchased. Customers belong
to one ofmsegments, indexed byt∈ T={1, . . . , m}. Segmenttoccurs with probabilityλ t >
0, with P t∈T λt = 1. We use segments to capture heterogeneity in both customer preferences
and the behavior of the AI assistant through which the customer shops. Concretely, a segment
9

can be interpreted as a particular subpopulation of customers who use a particular AI system.
Both components (subpopulation and AI model) matter: two customers with the same underlying
preferences may belong to different segments if they use different AI systems and therefore receive
different recommendations, while two customers using the same AI system may belong to different
segments if their preferences differ. In our numerical experiments, we make this interpretation
explicit by defining segments through combinations of customer profiles, such as budget-sensitive
or premium-seeking customers, and AI models, such as ChatGPT or Gemini Flash. Thus, for
example, budget-sensitive customers using ChatGPT constitute a different segment from budget-
sensitive customers using Gemini Flash, and also from premium-seeking customers using ChatGPT.
Throughout the paper, however, we keep the notion of a segment fully general and impose no
additional structure onTunless stated otherwise.
Seller assortment and AI mediation.The retailer chooses an assortmentS∈ F, where
F={S⊆N:|S| ≤B}denotes the family of feasible assortments consisting of at mostB
products, whereBis an exogenous positive integer. The retailer selects a single assortment to
display to an arriving request, without observing the corresponding segment. For each segment
t∈ T, we represent the AI’s mediation rule by a probability kernelQ t(C|S) over subsetsC⊆S.
Specifically,Q t(C|S) denotes the probability that segmentt’s AI displays the customer-facing set
Cwhen given assortmentS. Importantly, our model allows for the mediation rule to depend on the
customer segment. The dependence ontallows the AI’s recommendations to vary across segments,
reflecting differences both in the AI system being used and in the customer’s profile or preferences.
For everyS⊆N, this kernel satisfiesQ t(C|S)≥0 for allC⊆Sand P C⊆S Qt(C|S) = 1.
This kernel formulation is intended to serve as a general umbrella framework for AI-mediated
assortment optimization. In its unrestricted form,Q t(C|S) is too general to admit a meaningful
structural analysis. We introduce it to formalize the general retailer–AI–customer interaction and
to define the assortment optimization problems to follow. In Section 2.2, we introduce two ranking-
based mediation models that constitute the focus of our analysis. Throughout, the retailer takes
the mediation rule as given and can affect the customer-facing set only through its choice of the
assortments.
Customer preferences.We assume that each customer segment follows a segment-specific
multinomial logit (MNL) choice model. For every segmentt∈ T, each producti∈Nis asso-
ciated with a preference weightv it ≥0, which captures its attractiveness to customers in that
segment. We also include an outside option, indexed by 0, with a scaled preference weight of 1,
without loss of generality. Subsequently, when a segment-tcustomer is presented with a set of
productsC⊆N, the probability of choosing producti∈Cis
Pt(i|C) = vit 1 + P j∈C vjt .
The probability of choosing the outside option isP t(0|C) = 1/(1 + P j∈C vjt).
10

AI-mediated assortment problem.Based on the preceding discussion, given a customer-facing
setC⊆N, the expected revenue generated by a segment-tcustomer is
Rt(C) =
X
i∈C
riPt(i|C) =
P
i∈C rivit
1 + P i∈C vit .
Since the AI associated with segmentt∈ Tselects the displayed setCaccording to the kernelQ t,
the expected revenue from a segment-tcustomer, conditional on retailer assortmentS, is
X
C⊆S
Qt(C|S)R t(C).
Thus, the overall segment-weighted expected revenue given a retailer assortmentS∈ Fis
RQ(S) =
X
t∈T
λt ·
X
C⊆S
Qt(C|S)R t(C).
We introduce theAI-Mediated assortment optimization problem, denoted byAIM:
max
S∈F
RQ(S).(AIM)
2.2 Ranking-Based Mediation
As previously mentioned, the unrestricted mediation kernel is intended to serve as a general frame-
work and is too broad to study directly. In this paper, we focus on two specific mediation rules, both
based on cardinality-constrained rankings. LetK∈ {1, . . . , n}denote the AI’s display capacity.
When the AI is given an assortmentS⊆N, it ranks these products according to a known segment-
specific ranking, which may be deterministic or stochastic, and displays the topKproducts when
|S| ≥K; if|S|< K, the entire assortment is displayed.
Formally, letS N denote the set of permutations ofN. For any permutationσ∈S N , let
TopKσ(S) denote the min{K,|S|}highest-ranked products inSaccording toσ. Suppose that
segmenttis associated with a distributionµ t overS N . Then, the induced ranking-based mediation
kernel is
Qt(C|S) =
X
σ∈SN
µt(σ)1{C= TopK σ(S)}.(1)
In other words, the AI displays the subsetC⊆Sif and only if the products inCrepresent the
top-Kaccording to the drawn rankingσ, or ifCis the entire assortment when|S|< K.
In this paper, we consider two ranking rules whose specifics are provided in Sections 2.3 and 2.4.
The first is a segment-specific deterministic ranking. The second is based on the classical Plackett–
Luce model, in which products are assigned segment-specific positive weights that induce a random
ranking, and the AI displays the topKproducts under that ranking.
11

2.3 Deterministic Rankings
Deterministic mediation is obtained whenµ t places unit mass on a single rankingσ t. In that
case, for any fixed assortmentS⊆N, the AI displays a single subsetC D t (S) almost surely to
each segment-tcustomer. Specifically,C D t (S) consists of the top-Kproducts according toσ t when
|S| ≥K, and the entire assortment when|S|< K. Hence,Q D t (C|S) =1{C=C D t (S)}.The
expected revenue reduces to
RD(S) = X
t∈T
λtRt

CD t (S)  .
Finally, we defineAI-Mediated assortment optimization under deterministic mediationas
max
S∈F
RD(S).(AIM D)
Deterministic mediation provides a natural benchmark in which, for each segment, the AI follows
a fixed ranking of products and recommends the highest-ranked products available in the retailer’s
assortment. This formulation is also highly expressive: any stochastic ranking rule of the form (1)
can be represented as a distribution over deterministic rankings, and random-utility models admit
such ranking-based representations. Hence, by associating a separate segment with each ranking
realization, the deterministic-mediation model can represent any such stochastic ranking model
exactly. The only caveat is computational: an exact representation may require exponentially
many rankings, and therefore exponentially many segments.
2.4 Plackett–Luce Rankings
Concurrently, we also consider rankings generated by the classic Plackett–Luce model (Luce, 1959;
Plackett, 1975), which is one of the most widespread models considered in theory and practice for
ranked-choice data. It is widely used because it is simple, flexible enough to capture differences in
product attractiveness, and easy to estimate from observed rankings. It is also closely related to the
multinomial logit model: each stage of a Plackett–Luce ranking follows the same logit choice rule.
This choice is also in line with recent work on AI shopping behavior; for example, Allouah et al.
(2026) use a conditional logit model to study how AI agents respond to product and marketplace
attributes.
The Plackett-Luce model.In the PL model, each product receives a utility composed of a
deterministic nominal component and a stochastic shock capturing the inherent uncertainty in
preferences. Formally, for each productiand segmentt, letu it ∈Rdenote a nominal AI utility.
The score of productifor segmentt’s AI is given byU it =u it +ϵ it,where the shocksϵ it are
independent standard Gumbel random variables. These scores then induce a permutation describing
the decreasing order of scores.
Induced mediation kernel.We now derive the mediation kernel induced by the Plackett–Luce
ranking model. Fix an assortmentS⊆N, and letk(S) = min{K,|S|}denote the number of
12

products displayed by the AI. For each segmentt, writew it = exp(uit) for the positive Plackett–
Luce weight of producti. These quantities represent AI-side weights and are distinct from the
customer-side MNL weightsv it, which govern the customer’s final choice from the displayed set.
Consider a candidate displayed setC⊆Swith|C|=k(S). The event that the AI displays
exactlyCoccurs whenever the firstk(S) positions of the realized ranking coincide with the products
inC, in any order. Hence,
QPL t (C|S) = X
τ∈S C
pPL t (τ|S),(2)
whereS C denotes the set of all permutations ofC, andp PL t (τ|S) is the probability that the
ordered listτ= (τ 1, . . . , τk(S) ) occupies the firstk(S) positions of the Plackett–Luce ranking.
For any assortmentS⊆Nand any market segmentt∈ T, letW t(S) = P i∈S wit, the total PL
weight of assortmentSfor segmentt.
In the next lemma, we express the probability of a given ordered list of products appearing in
the firstk(S) positions of the Plackett–Luce ranking. The result follows directly from the Gumbel-
Top-krepresentation of sampling without replacement; see, e.g., Kool et al. (2019, Theorem 1).
Lemma 2.1(Plackett–Luce ranking probabilities).For every assortmentSand every ordered list
τ= (τ 1, . . . , τk(S) )of distinct products fromS,
pPL t (τ|S) =
k(S)Y
ℓ=1
wτℓt
Wt (S\ {τ1, . . . , τℓ−1}) .
Combining the lemma with Equation (2) gives an explicit expression for the induced mediation
kernelQ PL t (C|S). We can now define the resulting retailer’s revenue function under Plackett–Luce
mediation as
RPL(S) = X
t∈T
λt
X
C⊆S:
|C|=k(S)
QPL t (C|S)R t(C).
Finally, we defineAI-Mediated assortment optimization under Plackett–Luce mediationas
max
S∈F
RPL(S).(AIM PL)
3 AI-Ranking Data, Estimation, and Validation
In this section we present our data-generation process, including the product universes examined,
prompting conditions, and train–test design. Specifically, we consider a segmented market as
described in Section 2.1 and generate AI rankings for each segment by prompting the corresponding
AI model with randomly sampled product offer sets. We then estimate a separate Plackett–Luce
(PL) model for each market segment. To this end, we express the PL likelihood of the observed
AI recommendations and establish concavity of the corresponding log-likelihood. We subsequently
use the test samples to evaluate out-of-sample predictive performance.
13

This estimation step focuses on the stochastic PL model, which allows AI recommendations to
vary across queries. In particular, even within a single market segment, the same two products
need not be consistently ranked in the same relative order. The deterministic model, by contrast,
assigns each segment a single ranking, so fitting it directly to data with such variation would require
introducing an additional criterion for reconciling conflicting observed rankings. Instead, we obtain
a natural deterministic counterpart from the PL estimates, where products are ranked according
to their fitted utilities. In Section 4, we evaluate this deterministic plug-in and demonstrate that
it performs well relative to the stochastic PL benchmark in our experiments.
3.1 Data Generation and Prompting Protocol
Product data and universes.In what follows, we utilize the public Amazon Reviews 2023
product metadata dataset (Hou et al., 2024) to construct three product universes, corresponding
to different product categories. Our three product universes are stored in category-specific CSV
files, with one row per product. Each row records a product identifier, its Amazon product page
title, the listed price and brand/store, and a set of category-specific product attributes. These
files describe 25 Lightning chargers, 22 robot vacuums, and 25 pet leashes, for 72 products in
total, whose characteristics are summarized in Table 1. Representative examples are provided in
Appendix A.1.
Table 1: Product universes and information available to the AI ranking models.
Product category Number of
products
Product attributes Listed price ($):
median [min, max]
Lightning chargers 25 Wattage; connector type; cable length;
port count
16.79 [6.90, 32.65]
Robot vacuums 22 Suction power; run time; Wi-Fi
capability; mopping; self-emptying
200.86 [49.99, 1,149.99]
Pet leashes 25 Product type; species; length; closure
type; material
18.00 [8.85, 29.95]
AI models and prompting personas.We consider three widely popular AI models, which
were prompted to produce rankings among randomly generated product offer sets:
•OpenAI’s ChatGPT 5.4 (gpt-5.4-mini-2026-03-17).
•Anthropic’s Claude Haiku 4.5 (claude-haiku-4-5-20251001).
•Google’s Gemini 3.6 Flash (gemini-3.6-flash).
We also consider a stylized customer population consisting of three sub-populations, which are
represented via three prompting personas:
•Budget-sensitive: Prioritizes the cheapest available option and permits compromises in fea-
tures, quality, or brand reputation.
14

•Value-seeking: Prioritizes the best price-to-quality tradeoff, accepting a higher price for a
meaningful quality improvement but not for a marginal improvement or brand name alone.
•Premium-seeking: Prioritizes quality, premium features, and reputable brands, with price
treated as secondary.
Each model is queried under each of these personas, yielding nine model–persona pairs, which
constitute the market segments used in our empirical analysis.
Prompting and AI-data generation.We next describe the protocol employed to generate
the AI-ranking data. For each persona, we specify a persona-specific instruction describing the
shopping preferences that the AI model is asked to represent. This instruction is inserted into
a common prompt template that is subsequently instantiated with the product category and the
products contained in a given offer set. For example, the persona-specific instruction for value-
seeking customers is:
“You are assisting a value-seeking customer who cares most about the best price-to-
quality tradeoff. They will pay more for a meaningful step up in quality, but do not
want to overpay for marginal improvements or for brand name alone.”
In a nutshell, each AI prompt consists of a persona-specific instruction such as the one above,
and a description of the product category. Then, the prompt proceeds by offering a list of ten
products to the AI model, which is instructed to return a list of five products from this offer set,
representing a ranked list of its top five preferences. Each product is represented by its category-
specific product number, title, listed price, brand or store, and the category-specific attributes
appearing in Table 1. In particular, listed price is included in every ranking prompt. The complete
prompt template and model request settings are reported in Appendix A.1.
For each product category, we sample 600 distinct offer sets of cardinality 10 uniformly without
replacement from the collection of all cardinality-10 subsets of the corresponding product universe.
This choice is motivated by Hajek et al. (2014), who show that random uniform product assign-
ment yields near-minimax-optimal estimation rates for Plackett–Luce preference estimation, up to
logarithmic factors. We assign 500 of these underlying offer sets to the training sample and the
remaining 100 to the test sample. For each offer set, we generate two random permutations, deter-
mining the order in which its ten products are presented to the AI model. Both presentations of
a given offer set are assigned to the same side of the training–test partition, so that product sets
appearing in the test sample are not used for estimation. This randomization is intended to reduce
the systematic association between specific products and specific positions in the presented list.
For each market segment and each randomized presentation, we instantiate the prompt using
the corresponding persona instruction, product category, and ten-product offer set, and query the
associated AI model for its five most preferred products from that set. Thus, each observation
consists of a cardinality-10 offer set together with an ordered partial ranking (i 1, . . . , i5).
15

The resulting design contains three product categories, 600 underlying offer sets per category,
two presentation orders per offer set, and nine model–persona segments. Hence, the total number
of observations is 3×600×2×9 = 32,400.Of these, 27,000 belong to the training sample, while
5,400 form the test sample. Equivalently, each category–model–persona cell contains 1,000 training
rankings and 200 test rankings.
3.2 Estimating the Plackett–Luce Model
In this section, we present our estimation procedure for the stochastic AI-ranking model and then
report the resulting estimates and diagnostic statistics. We estimate the Plackett–Luce parameters
using a ridge-regularized likelihood criterion based on the standard PL likelihood and its partial-
ranking variants; see, e.g., Plackett (1975) and Hajek et al. (2014).
T raining data and likelihood function.For presentation purposes, let us consider a category
with product universeN={1, . . . , n}and a market segmentt. Recall that segmentt∈ Tcorre-
sponds to a particular persona–AI-model pair. We assume that the AI model’s recommendations
for this segment are generated according to a Plackett–Luce model with product-specific weights
wit >0 for each producti∈N. Suppose that, for segmentt, we observe a set of independent
training samplesD t ={(S d,(i d,1, . . . , id,K))}Dt d=1 ,whereS d ⊆Nis the offer set presented in ob-
servationd, and (i d,1, . . . , id,K) is the ordered top-Krecommendation returned by the AI model.
Therefore, the likelihood of this observed set of training samples, given the Plackett–Luce weights
w·t = (w1t, . . . , wnt), is defined as the probability of jointly observing the ordered top-Krankings
(id,1, . . . , id,K) for each offer setS d,d= 1, . . . , Dt, assuming that AI recommendations are generated
according to the Plackett–Luce model with weightsw ·t. We denote this likelihood function by
Lt(w·t | Dt) = Pr w·t

(id,1, . . . , id,K)Dt d=1

 (Sd)Dt d=1  .
Using Lemma 2.1, we can express the likelihood of the observed partial rankings as
Lt(w·t | Dt) =
DtY
d=1
KY
q=1
wid,qtP
j∈Sd\{id,1,...,id,q−1} wjt
.(3)
Substitutingw it = exp(uit) and taking logarithms yields
ℓt(u·t | Dt) = logL t((exp(uit))n i=1 | Dt) =
DtX
d=1
KX
q=1

uid,qt −log

 X
j∈Sd\{id,1,...,id,q−1}
exp(ujt)



 .(4)
Concavity of the log-likelihood function.The utility parameterization above is particularly
convenient from a computational perspective, since the resulting estimation problem is concave.
Namely, the log-likelihood function above is concave in the product utilitiesu ·t = (u1t, . . . , unt).
Indeed, for each observationdand rankq, the termu id,qt is linear inu ·t. Additionally, the
16

functionf:x7→log( P j expx j) is convex. To see this, for anyx, y∈R n andt∈[0,1], we have
f((1−t)x+ty) = log
 nX
i=1
exp ((1−t)x i +ty i)
!
= log
 nX
i=1
exp (xi)1−t exp(yi)t
!
≤log


 nX
i=1
exp (xi)
!1−t  nX
i=1
exp (yi)
!t

= (1−t)f(x) +tf(y),
where the inequality follows from H¨ older’s inequality. Hence the second term in each summand of
(4) is convex. Each summand is therefore concave, and summation preserves concavity.
Regularized log-likelihood.Concavity makes the estimation problem computationally trac-
table, but it does not by itself guarantee that the unregularized log-likelihood admits a finite
maximizer. In particular, the observed rankings may exhibit separation. For example, suppose
that, within a given market segment, a product is ranked first every time it appears in a training
offer set. Holding the remaining utilities fixed, increasing the utility of this product increases the
likelihood of each such observation, and the likelihood may approach its supremum only as the
corresponding utility diverges. Thus, directly maximizing the unregularized likelihood can yield an
ill-posed estimation problem even though the log-likelihood is concave.
To ensure a finite and well-defined estimate, we therefore use ridge-regularized maximum likeli-
hood. For each market segmentt, we estimate the utility vectoru ·t by maximizing the log-likelihood
minus a quadratic penalty. Namely,
bu·t = arg max
u·t∈Rn

ℓt(u·t | Dt)− θ 2 ∥u·t∥2 2

,(5)
whereθis a regularization parameter. Since the log-likelihoodℓ t(· | Dt) is concave and the quadratic
penalty θ 2 ∥ · ∥2 2 is strictly convex, the resulting penalized objective is strictly concave and admits a
unique finite maximizer.
Before evaluating the held-out test sample, we examinedθ∈ {0,0.0025,0.01,0.04,0.16,0.64}
using only the training data, whereθ= 0 is the unregularized estimator. We choseθ= 0.04 since
it substantially reduced the most extreme differences between fitted utilities while increasing the
average training negative log-likelihood (NLL) by less than 0.01 per ranking; larger values produced
noticeably larger increases in training NLL. We solve each segment-specific optimization problem
in Python using SciPy’s L-BFGS-B routine with the analytic gradient, initializing all utilities at
zero.
3.3 Out-of-Sample Validation
For this validation, we use the 5,400 held-out rankings from the three product categories. Table 2
reports several measures of predictive performance for the pooled sample, and separately by product
17

Table 2: Training fit and out-of-sample predictive performance of the estimated PL models.
Sample Test rankings Train NLL Test NLL Top-1 Top-3 Top-5 Jaccard
All categories 5,400 3.360 3.312 78.8% 68.4% 66.6% 0.879
By product category
Lightning chargers 1,800 3.712 3.624 78.6% 64.5% 61.4% 0.859
Robot vacuums 1,800 3.117 3.164 77.3% 70.6% 69.7% 0.891
Pet leashes 1,800 3.249 3.148 80.6% 70.1% 68.8% 0.886
By AI model
ChatGPT 1,800 4.337 4.227 73.6% 59.3% 56.9% 0.838
Claude 1,800 3.933 3.871 74.0% 64.0% 61.3% 0.860
Gemini 1,800 1.809 1.837 88.9% 81.9% 81.7% 0.938
category and AI model. Our validation metrics are defined as follows.
•Held-out NLL.This is the average negative log-likelihood that the fitted PL model assigns to the
observed ordered top-five rankings in the held-out sample, using the likelihood function in (3).
Lower NLL means that the model assigns greater probability to the observed recommendations.
Because its absolute scale is difficult to interpret, we compare held-out NLL with the training
and uniform reference values below.
•Training NLL.This is the same average negative log-likelihood computed on the observations
used for estimation. It provides a direct reference for out-of-sample performance: a held-out NLL
close to the training NLL indicates little deterioration on previously unseen offer sets, whereas
a large increase would indicate degradation, implying that the model does not generalize well.
•Top-Kset agreement.ForK∈ {1,3,5}, this is the fraction of held-out observations for which the
unordered set of the AI’s firstKrecommendations coincides exactly with theKoffered products
having the highest fitted PL utilities. Thus, order within the firstKpositions is ignored.
•Jaccard similarity.The Jaccard similarity of two setsAandBis defined as the ratio
|A∩B|/|A∪B|, and provides a measure of similarity of the two sets between 0 and 1. In Ta-
ble 2, we report the average Jaccard similarity between the set of top five products recommended
by the AI and the set of top five products predicted by the estimated PL model.
For reference, a PL model with equal worth for all ten offered products assigns probability
1/(10·9·8·7·6) to any ordered top-five ranking. Its NLL is therefore log(10·9·8·7·6) = 10.316921.
Analysis.The pooled training and held-out NLLs are 3.359555 and 3.311885, respectively, indi-
cating essentially no deterioration in predictive performance on offer sets that were not used for
estimation. The held-out NLL is also far below the uniform benchmark of 10.32, as are all category-
and model-level held-out NLLs.
The agreement metrics provide a complementary view. In the pooled sample, the fitted rank
center identifies the product ranked first by the AI in 78.8% of held-out observations, reproduces
the unordered first-three set in 68.4%, and exactly reproduces the unordered Top-5 set in 66.6%.
The mean Top-5 Jaccard similarity is 0.879. Although the AI recommendations exhibit stochastic
variation, these results indicate that much of that variation is organized around a stable preference
18

ordering captured by the estimated utilities. Performance varies across product categories and
more substantially across AI models. In this experiment, Gemini exhibits lower NLL and higher
agreement than ChatGPT and Claude.
As noted at the beginning of this section, ordering products by their fitted PL utilities gives a
natural deterministic approximation to the AI’s rankings. In Section 4, we optimize assortments
under this approximation and evaluate their revenue under stochastic PL mediation.
4 Experimental Effects of AI Mediation
We now embed the kernels estimated in Section 3 within a controlled semi-synthetic assortment
experiment. Here, the AI-ranking component is estimated from observed LLM rankings, while the
customer’s MNL preferences are generated synthetically. As described below, customer utility com-
bines a component aligned with the fitted AI-ranking preferences, capturing the part of customer
preferences reflected in the AI recommendations, with an independent idiosyncratic component
capturing preference variation not reflected in those recommendations. We use this experiment to
study the following questions:
(i)How does mediation change the retailer’s optimal assortment?
(ii)How costly it is to ignore the mediation layer in terms of revenue?
(iii)How much revenue is lost under PL mediation when the assortment is optimized using the
deterministic ranking induced by the fitted AI utilities?
4.1 Experimental Setup
Market segments.As previously mentioned, the market segments we consider represent unique
combinations of customer persona and AI models. As such, it is useful to indicate these two
components in each market segment. LetP={budget,value,premium}andQ={ChatGPT,
Claude,Gemini}denote the sets of personas and AI models, respectively. Throughout this section,
rather than using the generic segment indext, we index the nine segments by (p, q)∈ P × Q, where
pdenotes the persona andqthe AI model. The segments receive equal probability,λ p,q = 1/9.
For segment (p, q), the fitted PL utilityui,(p,q), and hence the PL weightw i,(p,q) = exp(ui,(p,q)),
governs the AI’s ranking model, whilev i,(p,q) denotes the customer’s MNL preference weight. We
assume that customer preferences depend on the persona but not on the AI model, i.e.,v i,(p,q) =
vi,(p,q′) for alli∈N,p∈ Pandq, q ′ ∈ Q. We therefore writev ip =v i,(p,q) for these common
customer-side weights. Thus, holding the persona fixed, variation across AI models changes the
empirically estimated AI-ranking kernel but not the customer-choice primitives.
Synthetic construction of customer preferences.Customer preferences are not observed in
the AI-ranking data, and we should therefore construct them synthetically. Our construction is
designed to capture two features. First, since each AI is asked to recommend products for a given
19

persona, it is natural for some component of that persona’s customer preferences to be related to the
preferences revealed by the fitted AI rankings. Second, the AI recommendations need not capture
every component of customer preference. To reflect these features, we therefore construct customer
utility from two components: a persona-level component derived from the fitted AI-ranking utilities
and an independent Gaussian component representing idiosyncratic customer preference variation.
An alignment parameterρ∈[0,1] controls the relative importance of these two components.
Specifically, for each personap, we first standardize each model-specific fitted utility vector
across products,
eui,(p,q) = ui,(p,q) −µ pq σpq ,
whereµ pq andσ pq are the cross-product mean and standard deviation ofu ·,(p,q). This standard-
ization puts all models’ utilities on a common scale, so that differences in their original scales do
not give one model more weight than another when we average their preferences. We then av-
erage the three standardized vectors and standardize once more, withb ip = 1 3 P q∈Q eui,(p,q),
anda ip = bip−¯bp sp ,where ¯bp ands p are the cross-product mean and standard deviation ofb ·p. The
purpose of this second standardization becomes clear in the next step, where we generate customer
utility as a weighted combination of these averaged preferences and independent standard Gaussian
noise. Putting both components on the same variance scale allows the alignment parameterρto
control their relative contributions. The resultinga ip is a persona-level summary of the fitted AI
preferences for producti, obtained by averaging across the three models.
For each product category, we generate multiple realizations of the random customer-preference
component. Letℓindex these realizations, which we refer to as replications. For replicationℓ, we
generate customer utility according to
β(ℓ) ip (ρ) =ρa ip + p 1−ρ 2 z(ℓ) ip ,
where thez (ℓ) ip are independent standard Gaussian random variables, and the alignment parameter
ρvaries in the set{0, .25, .50, .75, .90, .95, .99,1}.The same Gaussian perturbation is reused across
alignment values within a category and replication, so comparisons acrossρare paired. We choose
the coefficient
p
1−ρ 2 so that the squared weights of the two standardized components sum to one.
This normalization keeps the overall variance scale of customer utility comparable as alignment
varies. For every customer personap∈ P, we set the MNL preference weight of personapfor
producti∈Nin theℓ th replication as:
v(ℓ) ip (ρ) =cexp  β(ℓ) ip (ρ)  ,
with the outside-option weight normalized to one. Here, the common scalec= 0.248,is chosen to
target an average customer product weight of approximately 0.40 relative to the outside option.
Thus,ρ= 0 makes customer utility independent of the persona-level AI component, whereasρ= 1
removes the idiosyncratic component and makes customer utility fully aligned with that component.
20

Intermediate values interpolate between these two cases.
For everyρ <1, we generate 30 replications per category. Atρ= 1, the Gaussian component
vanishes, meaning that all replications coincide and only one endpoint instance is required per
category. This design yields 30×7 + 1 = 211 instances per category and 633 instances in total.
Policies.We consider three assortment-selection policies. Whenever a policy admits multiple
optimal assortments, we select one with smallest cardinality, and then the lexicographically smallest
among those assortments.
•Optimal PL policy.The policy returnsS ⋆ PL, an optimal solution toAIM PL under the fitted
PL model.
•Deterministic plug-in policy.The policy defines an instance ofAIM D with the same customer
weightsv ip and the deterministic ranking induced by the fitted utilitiesu i,(p,q). It returnsS ⋆ D,
an optimal solution to this deterministic instance.
•Direct-MNL benchmark.This policy ignores the AI mediation layer and returnsS ⋆ MNL, an
optimal solution to
max
S∈F
RMNL(S) = X
(p,q)∈P×Q
λp,qR(p,q)(S),
where we recall thatλ p,q is the arrival probability of segment (p, q)∈ P × Q, which is set
to 1/9 for all segments. Thus, the retailer optimizes as though its assortment were itself
the customer-facing choice set. Since customers in each segment choose directly from the
offered assortment according to their MNL model, this benchmark is equivalent to assortment
optimization under a mixture of MNL models.
In this experiment, the assortments returned by all three policies above are computed through
exhaustive enumeration of all feasible assortments.
Model parameters.For each producti, we set the retailer’s revenuer i equal to the listed product
price in the underlying product metadata. Recalling thatBrepresents the retailer’s assortment-size
limit andKdenotes the AI’s display capacity, we solve every instance under (B, K)∈ {(8,3),(8,5),
(10,3),(10,5),(10,7),(12,5),(12,7)}. Thus, the same 633 semi-synthetic instances are evaluated
in each of seven capacity environments, for 4,431 configuration–instance observations. For any
candidate assortmentS, we measure performance by its relative revenue loss with respect to the
exact PL-optimal assortmentS ⋆ PL, assuming a PL-mediation ground truth, defined as
Loss(S) = 1− RPL(S) RPL(S⋆ PL) .(6)
SinceS ∗ PL is a maximizer of the expected revenue functionR PL, the above loss is in the interval
[0,1], and represents the fraction of revenue lost from an optimal solution assuming a PL-mediation
ground truth.
21

4.2 Experimental Effects of AI Mediation
In this section, we study how the presence of the AI mediation layer affects the retailer’s optimal
assortment and the revenue consequences of ignoring that layer. Concurrently, we study how a
deterministic plug-in policy performs relative to the optimal PL assortment. We first pool across
product categories, alignment values, and replications within each capacity environment. Each
reported capacity-specific statistic therefore summarizes the same 633 underlying instances. We
then condition on the alignment parameterρto study how the revenue effects of mediation change
as customer preferences become more closely aligned with the AI-ranking preferences.
4.2.1 Pooled Analysis
Mediation regimes.The first question we address is whether the introduction of AI mediation
changes the customer-facing assortment compared to the direct-MNL benchmark. Indeed, our
modeling assumptions do not preclude the possibility that the PL-optimal assortment coincides
with the direct-MNL assortment. In particular, if the PL-optimal assortmentS ∗ PL is small enough
to fit within the display capacity, then every offered product is displayed and the PL-mediated and
direct-MNL revenues coincide at that assortment.
This motivates a first distinction between two cases: If|S ⋆ PL|> K, the AI displays only a
subset of the offered products; if|S ⋆ PL| ≤K, every offered product is displayed. However, the
absence of filtering does not mean that mediation has no effect: the retailer may choose a smaller
assortment precisely to avoid AI filtering. Within the case|S ⋆ PL| ≤K, we therefore compare the
PL-optimal assortment with the direct-MNL benchmark. If|S ⋆ MNL|> K, the retailer contracts its
assortment relative to the direct-MNL benchmark so that every offered product is displayed; we call
this endogenous filtering avoidance. If|S ⋆ MNL| ≤K, the retailer would choose an assortment that
fits within the display capacity even without mediation; we call this structurally inactive mediation.
We thus classify each instance into three empirical regimes:
(A) Active filtering:|S ⋆ PL|> K.
(B) Endogenous filtering avoidance:|S ⋆ PL| ≤Kand|S ⋆ MNL|> K.
(C) Structurally inactive mediation:|S ⋆ PL| ≤Kand|S ⋆ MNL| ≤K.
Figure 2 shows that mediation is active throughout much of the capacity grid, either through
realized filtering or through assortment contraction that avoids filtering. AtK= 3, regimes A
and B account for 45.3% and 50.7% of instances, respectively, leaving only 3.9% in regime C. At
K= 5, the corresponding shares are 34.1%, 51.7%, and 14.2%. Even atK= 7, 22.2% of instances
exhibit active filtering and 43.8% endogenous avoidance. Thus, a substantial part of the mediated
share reflects endogenous avoidance rather than realized filtering. The resulting mediated share,
A+B, declines from 96.1% atK= 3 to 85.8% atK= 5 and 66.0% atK= 7. Thus, within the
tested grid, this coarse regime classification varies significantly with the display capacityKand is
essentially invariant to the retailer assortment cardinality boundB.
22

(8,3) (8,5) (10,3) (10,5) (10,7) (12,5) (12,7)
Capacity pair (B, K)
0%
20%
40%
60%
80%
100%Share of instances45%
34%
45%
34%
22%
34%
22%
51%
52%
51%
52%
44%
52%
44%
14% 14%
34%
14%
34%
A: active filtering B: endogenous avoidance C: structurally inactive
Figure 2: Mediation regimes across the seven capacity environments.
Strategic assortment contraction.The regime decomposition points to a broader strategic
response: a retailer that accounts for AI mediation often chooses a smaller assortment than one
treating all offered products as directly customer-facing. Figure 3 compares assortment size under
the three policies. In particular, Panel A reports the mean assortment size under each policy, while
Panel B presents a box plot of|S ⋆ MNL| − |S⋆ PL|across the 633 instances in each capacity setting. The
outer lines indicate the minimum and maximum values. The lower and upper edges of each box
represent the first and third quartiles, and the horizontal line inside the box represents the median.
Across capacity environments, the direct-MNL assortment exceeds the PL-optimal assortment
by 1.48 to 4.15 products on average. The difference is largest when display capacityKis smaller.
For example, at (B, K) = (10,3), direct-MNL selects 8.35 products on average while the PL oracle
selects only 4.20; at (10,7), the corresponding averages are 8.35 and 6.84. The direct assortment is
strictly larger than the PL assortment in 96.0% of theK= 3 instances, compared with 57.2% at
(10,7).
(8,3) (8,5) (10,3) (10,5) (10,7) (12,5) (12,7)
Capacity pair (B, K)
0
1
2
3
4
5
6
7
8
9
10
Mean assortment size
A. Assortment size by policy
|S ⋆ PL|
|S ⋆ D |
|S ⋆ MNL|
(8,3) (8,5) (10,3) (10,5) (10,7) (12,5) (12,7)
Capacity pair (B, K)
0
1
2
3
4
5
6
7
|S ⋆ MNL| − |S ⋆ PL|
B. Assortment-size contraction
Figure 3: Assortment size and assortment contraction across the seven capacity settings.
23

This contraction has a direct interpretation in regime B. Whenever|S| ≤K, every offered
product is displayed and thereforeR PL(S) =R MNL(S).BecauseS ⋆ PL itself lies in this all-display
region in regime B, the direct-MNL problem with the additional constraint|S| ≤Kattains the
PL-optimal value. Regime B therefore isolates the retailer’s response to the display constraint of
AI mediation: the mediation-aware retailer is willing to forgo additional assortment capacity in
order to remove the AI’s discretion over which products reach the customer.
Revenue cost of ignoring mediation.Evidently, these assortment changes have substantial
revenue consequences. Table 3 reports revenue loss separately in each capacity environment. Mean
direct-MNL revenue loss ranges from 2.52% to 11.37%, its 95th percentile from 10.36% to 30.66%,
and its maximum from 23.83% to 57.08%. The largest losses occur when display capacity is tight:
mean direct-MNL revenue loss is 9.80% at (8,3) and 11.37% at (10,3). In contrast, mean deter-
ministic revenue loss ranges from only 0.08% to 0.53% across the full grid, with 95th percentiles
between 0.59% and 2.70%.
Taken together, these experiments show that accounting for AI mediation often leads retailers
to choose smaller assortments and can substantially improve revenue under PL mediation. The
deterministic plug-in captures most of this benefit on average, with mean revenue loss of at most
0.53% across the tested capacity environments.
4.2.2 Role of Preference Alignment
We next condition onρto examine how alignment between AI and customer preferences affects both
the structure of the offered assortments and the expected revenue. For everyρ <1, each capacity
point aggregates 90 instances, corresponding to 30 replications in each of the three categories, while
theρ= 1 endpoint contains one category-specific instance for each of the three categories.
Revenue loss and alignment.In Figure 4, we report the mean revenue loss of the direct-MNL
benchmark (Panel A) and the deterministic plug-in (Panel B) as a function of the alignment param-
eterρ. For clarity, this figure focuses on the three configurations with assortment-size limitB= 10;
the corresponding curves for the remaining capacity configurations are reported in Appendix B.1.
The same qualitative patterns hold across the full capacity grid.
Table 3: Policy performance across the seven capacity environments.
B KMediated Mean|S ⋆ PL|Direct-MNL revenue loss Deterministic revenue loss
share Mean P95 Max Mean P95 Max
8 3 96.05% 4.20 9.80% 28.04% 57.08% 0.52% 2.70% 9.02%
8 5 85.78% 5.60 4.04% 13.85% 37.96% 0.18% 0.99% 4.83%
10 3 96.05% 4.20 11.37% 30.66% 52.11% 0.53% 2.70% 9.02%
10 5 85.78% 5.88 5.50% 18.45% 37.90% 0.26% 1.45% 4.83%
10 7 66.03% 6.84 2.52% 10.36% 23.83% 0.08% 0.59% 2.16%
12 5 85.78% 5.92 6.53% 21.42% 37.90% 0.28% 1.59% 4.83%
12 7 66.03% 7.01 3.56% 12.64% 23.83% 0.13% 1.00% 2.67%
24

The most immediate observation is the substantial difference in scale between the two panels.
Atρ= 0, for example, mean direct-MNL revenue loss is 24.06%, 11.83%, and 5.75% forK= 3,5,7,
respectively, whereas the corresponding deterministic losses are only 0.21%, 0.03%, and essentially
zero. The difference remains large at intermediate levels of alignment: atρ=.75, the direct-
MNL losses are 8.27%, 3.89%, and 1.80%, compared with only 0.79%, 0.23%, and 0.07% for the
deterministic plug-in. The gap narrows only as alignment becomes very high. Thus, over most of
the alignment range, accounting only for the ordering induced by the fitted AI preferences recovers
most of the revenue value of modeling mediation.
A second pattern concerns how costly it is to ignore mediation. Direct-MNL revenue loss
falls sharply as customer preferences become more closely aligned with the AI-ranking preferences.
Across the full capacity grid, mean direct-MNL revenue loss ranges from 5.75% to 24.06% at
ρ= 0, compared with only 0.59% to 5.74% atρ= 1; the endpoint loss is lower atρ= 1 than at
ρ= 0 in every configuration. This relationship is not perfectly monotone, as several configurations
exhibit small reversals in monotonicity, but the overall decline is pronounced. When customer
and AI preferences are poorly aligned, treating the retailer’s assortment as though it were directly
customer-facing can therefore be especially costly; as their preferences become aligned, the economic
penalty of ignoring the mediation layer falls substantially.
The deterministic plug-in exhibits a different relationship with alignment. Its revenue loss re-
mains small throughout, but is not monotone inρacross all seven capacity configurations. In
particular, greater customer–AI alignment can reduce direct-MNL loss while leaving deterministic
loss unchanged or even increasing it. Hence, alignment explains when ignoring mediation is espe-
cially costly, but not when the deterministic approximation is most accurate. The latter remains
a strong approximation across the alignment range, suggesting that the ordering induced by the
fitted AI preferences captures substantial information about the mediation layer even when the
customer’s preferences are only weakly aligned with those of the AI.
Assortment response to alignment.In Figure 5, we report the mean difference between the
PL-optimal assortment size and the display capacityK, and the share of instances in which the
PL-optimal assortment exceeds the display capacityK. Similar to Figure 4, the current figure
focuses on the threeB= 10 configurations, with the remaining capacity configurations reported in
Appendix B.2 for the sake of readability.
Figure 5 shows that the reduction in direct-MNL revenue loss observed in Figure 4 does not arise
since mediation simply disappears at high alignment. In fact, it shows the opposite change in the
mediation mechanism. Atρ= 0, active filtering occurs in at most 8.9% of instances across capacity
environments, whereas endogenous avoidance accounts for 62.2% to 84.4%. As alignment rises, the
PL-aware retailer becomes increasingly willing to offer more thanKproducts. Atρ=.95, active
filtering accounts for 44.4% to 66.7% of instances, while endogenous avoidance remains sizeable at
between 22.2% and 33.3%.
The assortment-size statistic in Panel A draws a similar picture. Atρ= 0, mean|S ⋆ PL| −K
ranges from−0.74 to 0.13 products across capacities; byρ=.95, it ranges from 0.37 to 1.96. Thus,
25

0 .25 .50 .75 .90 1
Preference alignment ρ
0%
5%
10%
15%
20%
25%
 A. Direct-MNL revenue loss
0 .25 .50 .75 .90 1
Preference alignment ρ
0.0%
0.2%
0.4%
0.6%
0.8%
1.0%
 B. Deterministic revenue loss
Mean revenue loss
K = 3 K = 5 K = 7
Figure 4: Revenue loss by customer–AI preference alignment atB= 10. Panel A reports mean
direct-MNL revenue loss and Panel B reports mean deterministic revenue loss, both forK∈
{3,5,7}.
0 .25 .50 .75 .90 1
Preference alignment ρ
−1.0
−0.5
0.0
0.5
1.0
1.5
2.0
2.5
A. Mean |S ⋆ PL| − K
0 .25 .50 .75 .90 1
Preference alignment ρ
0%
20%
40%
60%
80%Share of instances
B. Active-filtering share
K = 3 K = 5 K = 7
Figure 5: Assortment response and mediation mechanism by preference alignment. Panel A reports
mean|S ⋆ PL|−Kfor each capacity environment. Panel B reports the corresponding share of instances
in the active-filtering regime.
greater alignment makes the retailer more willing to allow the AI greater discretion over which
offered products are displayed.
5 Deterministic Ranking Mediation
Section 4.2 shows that deterministic mediation serves as a practical surrogate for a PL-mediated
ground truth. This empirical performance makes deterministic ranking mediation a natural opera-
26

tional surrogate. We now study the resulting assortment optimization problem, by characterizing
its computational status under various primitive regimes, and developing a fully polynomial-time
approximation scheme (FPTAS) for any fixed number of segments.
5.1 Computational Complexity
In what follows, we characterize the computational complexity ofAIM D across the main regimes
of the model parameters. Recall from Section 2.3 that under deterministic mediation, we assume
that each segmentt∈ Tis associated with a rankingσ t ∈S N , and that the AI displaysC D t (S) =
TopKσt(S).The retailer’s expected revenue is
RD(S) = X
t∈T
λtRt

CD t (S)  .
Table 4 summarizes the resulting complexity landscape; we establish the complexity of each of its
considered regimes, while the fixed-m, arbitrary-Kapproximation result is developed in Section 5.2.
m= 1 Fixedm≥2 Arbitrarym
FixedKPolynomial PolynomialO(n 1−ϵ)-inapproximable
ArbitraryKPolynomial NP-hard; FPTASO(n 1−ϵ)-inapproximable
Table 4: Computational complexity and approximability of deterministic AI-mediated assortment
optimization.
We begin with the general setting, in which the number of segmentsmand the display capacity
Kmay both scale with the input, and then examine the tractability that emerges when one or both
of these parameters are fixed.
Arbitrarym.The next theorem shows that when the number of segmentsmmay scale with
the input, deterministic AI mediation leads to a strongly-inapproximable assortment optimization
problem even when the display capacityK= 1.
Theorem 5.1.For any fixedϵ >0,AIM D cannot be approximated in polynomial time within factor
O(n1−ϵ), even whenK= 1andB=n, unlessP = NP.
The proof proceeds by a gap-preserving reduction from assortment optimization under ranking
preferences, which is NP-hard to approximate within factorO(n 1−ϵ) for every fixedϵ >0 (Aouad
et al., 2018, Theorem 2.1). We associate one customer segment with each preference list and setK=
1, using zero customer-side MNL weights for products outside the corresponding preference list.
The resulting deterministic-mediation instance preserves the expected revenue of every assortment
exactly. The complete reduction is provided in Appendix C.1. We therefore turn to parameter
regimes in which the number of segments or the display capacity is restricted.
27

Fixedmand fixedK.Here, we consider the case in which both the number of segmentsmand
the display capacityKare fixed. The key observation is that given an optimal assortment, products
that are not displayed to any segment can be removed without affecting the expected revenue.
Consequently, any optimal assortment can be transformed into another optimal assortment of size
at mostmK, by removing all such products.
Lemma 5.2.There exists an optimal assortmentS ∗ ∈ Fsatisfying|S ∗| ≤mK.
Proof.Consider an optimal assortmentS ∗ ∈ F, and defineeS=C D 1 (S∗)∪ · · · ∪CD m(S∗).Since each
segmentt∈ Tis displayed at mostKproducts,| eS| ≤P t∈T

CD t (S∗)

 ≤mK.Moreover, eS⊆S ∗,
and hence eS∈ F. To prove that eSis optimal, it remains to observe that removing products in
S∗ \ eSdoes not alter any segment’s displayed set. Indeed, every product removed fromS ∗ lies
below the display cutoff for every segment, whereas all products inC D t (S∗) remain in eS. Therefore,
CD t ( eS) =C D t (S∗) for everyt∈ T. Consequently,R D( eS) =R D(S∗).
Lemma 5.2 immediately yields a polynomial-time algorithm whenmandKare fixed. It suffices
to enumerate all feasible assortments consisting of at mostmKproducts and evaluate their deter-
ministic mediated revenues. The number of candidate assortments isO(n mK), which is polynomial
in the input size for fixedmandK.
ArbitraryKandm= 1.The single-segment problem remains tractable even when the display
capacityKis unbounded. By Lemma 5.2, there exists an optimal assortment containing at most
Kproducts. Such an assortment is displayed in its entirety to the unique segment, meaning that
the current setting reduces to
max
S⊆N:
|S|≤min{B,K}
R1(S).
This is exactly single-segment cardinality-constrained MNL assortment optimization which is known
to be solvable in polynomial time (Rusmevichientong et al., 2010, Theorem 2.2). Thus, allowing
the display capacityKto grow does not by itself create computational hardness.
Arbitrary K and fixed m≥2.As we show next, fixing the number of segmentsmdoes not
suffice to recover exact polynomial-time solvability when the display capacity is allowed to grow.
Indeed, consider the special case ofK=B=n. Here, the AI displays every product in the retailer’s
assortment to every segment, so thatC D t (S) =Sfor everyt∈ T. The expected revenue reduces to
RD(S) = X
t∈T
λtRt(S).
This is precisely the expected revenue function under a mixture of multinomial logit models. There-
fore, any assortment optimization problem under the latter model can be mapped to anAIM D
instance, by retaining the same MNL customer preferences across all segments, settingK=B=n,
28

and fixing an arbitrary ranking. Given that assortment optimization under a mixture of multino-
mial logit models is NP-hard even form= 2 segments (Rusmevichientong et al., 2014, Theorem 1),
AIMD is NP-hard for fixedm≥2 whenKis part of the input.
This final regime completes the exact-complexity landscape in Table 4. Although exact opti-
mization remains NP-hard whenmis fixed andKis arbitrary, fixingmleaves only a constant
number of segment-specific revenue components. We exploit this structure in the next section to
obtain an FPTAS.
5.2 An FPTAS for a Fixed Number of Segments
In this section, we show that fixingmpermits a fully polynomial-time approximation scheme.
Theorem 5.3.For every fixedmand everyϵ∈(0,1), a feasible assortment bS∈ Fsatisfying
RD( bS)≥(1−ϵ) max
S∈F
RD(S)
can be computed in time polynomial in the binary encoding length of the instance and1/ϵ.
Preliminaries.Among all optimal assortments for ProblemAIM D, letS ∗ have minimum car-
dinality. We say that mediation isinactivefor an assortmentSif|S| ≤K, in which case every
segment views the entire assortment, andactiveif|S|> K, in which case each segment views only
itsKhighest-ranked products. Since our algorithm does not know which regime containsS ∗, we
propose a separate procedure for each case and return the candidate assortment with the largest
value of expected revenue. We first handle the easy case of inactive mediation.
For every assortmentSwith|S| ≤min{B, K}, each segment viewsSin its entirety, since
CD t (S) =Sfor all segmentst∈ T. Hence,R D(S) = P t∈T λtRt(S), and optimization over
these assortments is precisely the cardinality-constrained assortment optimization problem under
a mixture of multinomial logit models, with capacity min{B, K}. For fixedm, the FPTAS of D´ esir
et al. (2022) therefore returns a feasible assortment ¯Ssatisfying
RD( ¯S)≥(1−ϵ)·max
S⊆N:
|S|≤min{B,K}
RD(S).
The running time of the algorithm therein is

n

L+ log(1/ϵ)

ϵ
!O(m)
,(7)
whereLdenotes the binary encoding length of the instance. If an optimal assortmentS ∗ for
ProblemAIM D satisfies|S ∗| ≤K, it belongs to this restricted feasible family, soR D( ¯S)≥(1−
ϵ)RD(S∗). In the remainder of this section, we focus on the active regime, when|S ∗|> K.
It remains to construct a candidate with the same guarantee when|S ∗|> K, which we address
29

next. In order to do so we proceed in four steps. In Section 5.2.1, we introduce an alternative
formulation forAIM D by guessing the lowest ranked product in each segment’s displayed set under
the optimal assortmentS ∗. In Section 5.2.2, we introduce an approximation framework due to
Mittal and Schulz (2013) for optimizing a sum of a fixed number of ratios of affine functions. In
Section 5.2.3, we use a multidimensional knapsack reformulation to show that the conditions of the
framework of Section 5.2.2 are satisfied. Finally, in Section 5.2.4, we combine these ingredients to
obtain an FPTAS forAIM D whenmis fixed.
5.2.1 A threshold reformulation
Suppose now that|S ∗|> K. Our first step is to guess, through exhaustive enumeration, the lowest-
ranked product in each segment’s displayed set underS ∗. Fixing an arbitrary vectorτ= (τ t)t∈T ∈
N m, we interpret eachτ t as a candidate for the lowest-ranked product inC D t (S∗). We callτ t the
display thresholdfor segmentt∈ T. There aren m candidate vectors, so let’s assume thatτ ∗, the
vector of display thresholds corresponding to the optimal assortmentS ∗, is known as we proceed.
For any producti∈Nand customer segmentt∈ T, let rank t(i) denote the position of
productiin the strict rankingσ t, with smaller positions indicating higher ranks. Leth it =
1{rankt(i)≤rank t(τ ∗ t )}, which indicates whether productiranks at least as high as the optimal
display thresholdτ ∗ t . To realize these thresholds, we require every threshold product to be selected
and exactlyKselected products to satisfyh it = 1 for each segmentt∈ T. LetM={τ ∗ t :t∈ T }
be the set of distinct threshold products and letA={i∈N: P t∈T hit >0}be set of products
that rank at least as high as some threshold. The setMrecords the products whose inclusion
is required, counting a product only once even if it serves as the threshold for several segments.
Products outsideAlie below every proposed threshold. If these thresholds are realized, such prod-
ucts are not displayed to any segment and can be omitted without affecting revenue. We therefore
restrict attention to assortments satisfyingM⊆S⊆A. Finally, we definea it =r ivithit and
bit =v ithit, and we introduce the following optimization problem:
max
S⊆A
Rτ ∗ (S) = X
t∈T
λt ·
P
i∈S ait
1 + P i∈S bit
s.tM⊆S(i)
|S| ≤B(ii)
X
i∈S
hit =Kfor allt∈ T(iii)
(AIMτ ∗ D )
For ease of notation, letX τ ∗ denote the feasible family of Problem (AIM τ ∗ D ), consisting of the
assortmentsS⊆Asatisfying constraints (i)–(iii). The next lemma links this conditional problem
to ProblemAIM D. It shows that their objective functions coincide overX τ ∗, and that the optimal
assortmentS ∗ is feasible for the conditional problem. Its proof is provided in Appendix C.2.1.
Lemma 5.4.For everyS∈ X τ ∗, we haveR τ ∗ (S) =R D(S).Moreover,S ∗ ∈ Xτ ∗.
30

Lemma 5.4 implies that any (1−ϵ)-approximate solution to ProblemAIM τ ∗ D is also a (1−ϵ)-
approximate solution to ProblemAIM D. Indeed, let bS∈ Xτ ∗ be such a solution. Then,
RD( bS) =R τ ∗ ( bS) (8)
≥(1−ϵ) max
S∈Xτ ∗
Rτ ∗ (S) (9)
≥(1−ϵ)R τ ∗ (S∗) (10)
= (1−ϵ)R D(S∗).(11)
Equation (8) follows from Lemma 5.4. Equation (9) follows from the approximation guarantee for
bS. Equation (10) follows fromS ∗ ∈ Xτ ∗. Finally, Equation (11) follows again from Lemma 5.4.
It therefore remains to construct a (1−ϵ)-approximate solution to ProblemAIM τ ∗ D , which we
address in the remainder of this section.
5.2.2 A framework for sums of ratios
We next introduce the approximation framework of Mittal and Schulz (2013) for optimizing a sum
of a fixed number of ratios of affine functions. We proceed by introducing the general setup.
LetX ⊆ {0,1}d be a nonempty feasible family. For eacht∈ {1, . . . , m}, letαt0, βt0 ∈R ≥0 and
αt, βt ∈R d ≥0. We consider the optimization problem
max
x∈X
G(x) =
mX
t=1
αt0 +α ⊤ t x
βt0 +β ⊤ t x .(12)
We assume that every numerator and denominator is strictly positive onX, and letLdenote
the total binary encoding length of the feasible-family description and the objective coefficients.
Next, we define theexact problemassociated with the familyXas: givenc∈Z d ≥0 andC∈Z ≥0,
determine whether there existsx∈ Xsatisfying Pd i=1 cixi =C.LetT ex(L, U) be an upper bound
on the running time of an algorithm that solves the exact problem, whereUis an upper bound on
the absolute values of the entries ofcandC.
The next theorem, due to Mittal and Schulz (2013), shows that if the exact problem is solvable
in pseudopolynomial time, then the sum-of-ratios problem (12) admits a fully polynomial-time
approximation scheme.
Theorem 5.5.For everyϵ∈(0,1), a feasible solutionbx∈ XsatisfyingG(bx)≥(1−ϵ) max x∈X G(x)
can be computed in time
 (d+ 1)L
ϵ
O(m)
Tex

L,
 d+ 1
ϵ
O(m)!
.
The above theorem follows from Theorem 7.5 of Mittal and Schulz (2013), which establishes
the result for a single ratio. The subsequent discussions in Section 7 therein extend the result to
31

the sum of a fixed number of ratios. The displayed running-time bound is obtained by tracking
their construction.
5.2.3 V erifying the exact-solvability condition
We show that Theorem 5.5 can be applied to obtain an FPTAS forAIM τ ∗ D . First, since the numer-
ators and denominators in the framework of Theorem 5.5 must be strictly positive for all feasible
solutions, we slightly shift the objective function by adding a strictly positive term to ensure this
condition is met. Then, we show that the exact problem associated withAIM τ ∗ D can be solved in
pseudopolynomial time by a reduction to a multidimensional knapsack problem.
Objective shift.Recall the objective function ofAIM τ ∗ D :
Rτ ∗ (S) = X
t∈T
λt
P
i∈S ait
1 + P i∈S bit .
The denominators are strictly positive for all feasible assortments, but the numerator for a segment
t∈ Tis zero ifa it = 0 for everyi∈S. To address this issue, we add a strictly positive term to
each numerator. Letℓ= max i∈N RD({i}) denote the maximum expected revenue of a singleton
assortment. Since every singleton assortment is feasible for the original problem, we haveℓ≤
RD(S∗). Ifℓ= 0, every feasible assortment has zero revenue, so we may assume thatℓ >0. For
everyS∈ Xτ ∗, we introduce the shifted revenue function
bRτ ∗ (S) = X
t∈T
λt
P
i∈S ait +ℓ

1 + P i∈S bit 
1 + P i∈S bit =R τ ∗ (S) +ℓ,
where the second equality follows from P t∈T λt = 1. Each numerator is now at leastℓ >0. We
also introduce the shifted problem
max
S∈Xτ ∗
bRτ ∗ (S).( [AIMτ ∗)
Let bS∗ be an optimal solution to dAIMτ ∗. The following lemma shows that an approximation
guarantee for the shifted objective yields one for the original objective.
Lemma 5.6.For everyϵ∈(0,1)and bS∈ Xτ ∗, if bRτ ∗ ( bS)≥(1−ϵ/2) bRτ ∗ ( bS∗),thenR D( bS)≥
(1−ϵ)R D(S∗).
Proof.By Lemma 5.4,S ∗ ∈ Xτ ∗, andR τ ∗ (S) =R D(S) for everyS∈ X τ ∗. Consequently,
RD( bS) = bRτ ∗ ( bS)−ℓ
≥(1−ϵ/2) bRτ ∗ ( bS∗)−ℓ
≥(1−ϵ/2) bRτ ∗ (S∗)−ℓ
= (1−ϵ/2)R D(S∗)− ϵ 2 ℓ
32

≥(1−ϵ)R D(S∗),
where the last inequality usesℓ≤ R D(S∗).
Consequently, a (1−ϵ/2)-approximate solution for the shifted problem yields a (1−ϵ)-
approximate solution for the original problem.
Algorithm for the exact problem.In light of Lemma 5.6, we focus on approximating the
shifted problem dAIMτ ∗. Identifying each assortmentS⊆Awith its incidence vectorx∈ {0,1} A,
wherex i = 1 if and only ifi∈Sfor everyi∈A, we can rewrite dAIMτ ∗ as the following integer
program:
max
X
t∈T
λt
ℓ+ P i∈A(ait +ℓb it)xi
1 + P i∈A bitxi
s.t.x i = 1, i∈M, X
i∈A
xi ≤B,
X
i∈A
hitxi =K, t∈ T,
xi ∈ {0,1}, i∈A.
(13)
LetX ⊆ {0,1}A denote the feasible set of (13). We now show that this problem falls within the
framework of Theorem 5.5. Each numerator is at leastℓ >0, and each denominator is at least
one. Moreover, both are affine functions ofxwith nonnegative coefficients. It remains to provide
a pseudopolynomial-time algorithm for the associated exact problem.
The exact problem associated with (13) is to determine, for a given vectorc∈Z A ≥0 and target
C∈Z ≥0, whether there existsx∈ Xsatisfyingc ⊤x=C. We show that this problem can be solved
in pseudopolynomial time by a reduction to a multidimensional knapsack problem. First notice
that any feasible solutionx∈ Xmust satisfyx i = 1 for alli∈M, and have at mostBentries equal
to one. LettingI=A\M, the exact problem is equivalent to: determine whether there exists a
vectorx∈ {0,1}I satisfying
X
i∈I
xi ≤B− |M|,
X
i∈I
cixi =C−
X
i∈M
ci,
and, for everyt∈ T, X
i∈I
hitxi =K−
X
i∈M
hit.
If any right-hand side above is negative, the exact problem is infeasible. Otherwise, we construct
33

the following (m+ 2)-dimensional 0–1 knapsack problem:
max
x∈{0,1}I
X
i∈I
(ci +
X
t∈T
hit)·x i
s.t.
X
i∈I
xi ≤B− |M|,
X
i∈I
hitxi ≤K−
X
i∈M
hit for allt∈ T,
X
i∈I
cixi ≤C−
X
i∈M
ci.
(14)
The next lemma links problem (14) to the exact problem.
Lemma 5.7.The exact problem is feasible if and only if(14)admits a feasible solution with profit
at least
C−
X
i∈M
ci +mK−
X
t∈T
X
i∈M
hit.
The proof is given in Appendix C.2.2. The standard exact algorithm for multidimensional knapsack
(Kellerer et al., 2004, Section 9.3.2) solves the constructed instance and recovers a selected subset
in timeO

m(C+ 1)n O(m) .
5.2.4 Completing the proof
Correctness.For each candidate threshold vector, we apply Theorem 5.5 to the shifted prob-
lem dAIMτ ∗ with accuracyϵ/2. For the threshold vectorτ ∗, Lemma 5.6 guarantees that the returned
assortment has expected revenue at least (1−ϵ)R D(S∗). Evaluating all returned assortments, to-
gether with ¯S, under the original revenue function and retaining the best therefore gives the desired
approximation guarantee.
Running time.There are at mostn m candidate threshold vectors. For each vector, we solve
the corresponding shifted problem dAIMτ ∗. LetLdenote the length of the original instance, and let
bL=O(nmL) bound the lengths of the shifted conditional instances. The exact algorithm satisfies
Tex(bL, U) =O

m(U+ 1) bLO(m)

.
Therefore, substituting this bound andd=|A| ≤ninto Theorem 5.5, with accuracyϵ/2, gives
a running time ofm

nbL/ϵ
O(m)
per threshold vector. Multiplying by the number of threshold
vectors gives
mnm

nbL
ϵ
!O(m)
=m
 nmL
ϵ
O(m)
.
34

Including the inactive-mediation procedure and the evaluation and comparison of the returned
assortments, the total running time is
m
 nm(L+ log(1/ϵ))
ϵ
O(m)
.
For fixedm, this bound is polynomial inLand 1/ϵ, establishing the FPTAS.
6 Conclusion
This paper studies assortment optimization when a retailer chooses the catalog available to an
AI intermediary, which then determines the products shown to each customer. We estimate and
validate Plackett–Luce ranking models using controlled queries of AI shopping assistants. Com-
bining these estimates with synthetic customer preferences, we find that accounting for mediation
leads to smaller assortments on average and can induce retailers to limit their catalogs so that
every offered product is displayed. Across the tested capacity configurations, ignoring mediation
produces mean revenue losses ranging from 2.52% to 11.37% relative to the PL optimum. A deter-
ministic approximation based on the ordering of fitted AI utilities recovers nearly all of the optimal
PL-mediated revenue on average in our experiments, with mean losses of at most 0.53% across
capacity configurations. This finding motivates our analysis of assortment optimization under de-
terministic mediation. We characterize its computational complexity and develop an FPTAS for
any fixed number of customer segments and arbitrary display capacity. The FPTAS guarantee
applies to deterministic mediation. The numerical comparisons under stochastic mediation use
exactly optimized deterministic assortments.
We hope this work opens new directions for research on assortment optimization under AI
mediation. As AI shopping assistants become more prevalent, understanding how they reshape
product exposure, consumer choice, and retailers’ decisions will become increasingly important.
Acknowledgments
The authors gratefully acknowledge Danny Segev for valuable discussions and thoughtful feedback
on this paper.
References
Amine Allouah, Omar Besbes, Josu´ e D Figueroa, Yash Kanoria, and Akshit Kumar. What is your AI
agent buying? Evaluation, biases, model dependence, & emerging implications of agentic e-commerce. In
Proceedings of the ACM Web Conference 2026, pages 8697–8700, 2026. 8, 12
Ali Aouad, Vivek Farias, Retsef Levi, and Danny Segev. The approximability of assortment optimization
under ranking preferences.Operations Research, 66(6):1661–1669, 2018. 6, 27, 39, 40, 42
Ali Aouad, Vivek Farias, and Retsef Levi. Assortment optimization under consider-then-choose choice
models.Management Science, 67(6):3368–3386, 2021. 7
35

Ali Aouad, Jacob Feldman, Danny Segev, and Dennis J Zhang. The click-based MNL model: A framework
for modeling click data in assortment optimization.Management Science, 71(8):6943–6960, 2025. 7
Th´ eo Barr´ e, Omar El Housni, Marouane Ibn Brahim, Andrea Lodi, and Danny Segev. Assortment optimiza-
tion with visibility constraints.Mathematical Programming, 216(1):177–220, 2026. 7
Shengyu Cao and Ming Hu. A solicit-then-suggest model of agentic purchasing.arXiv preprint
arXiv:2603.20972, 2026. 8
Capgemini Research Institute. What matters to today’s consumer 2025. Capgemini Re-
search Institute, 2025. URLhttps://www.capgemini.com/insights/research-library/
what-matters-to-todays-consumer-2025/. Accessed August 25, 2026. 2
Qinyi Chen, Negin Golrezaei, and Fransisca Susan. Fair assortment planning.arXiv preprint
arXiv:2208.07341, 2022. 7
Antoine D´ esir, Vineet Goyal, Danny Segev, and Chun Ye. Constrained assortment optimization under the
Markov chain–based choice model.Management Science, 66(2):698–721, 2020. 6
Antoine D´ esir, Vineet Goyal, and Jiawei Zhang. Capacitated assortment optimization: Hardness and ap-
proximation.Operations Research, 70(2):893–904, 2022. 7, 29
Antoine D´ esir, Vineet Goyal, Bo Jiang, Tian Xie, and Jiawei Zhang. Robust assortment optimization under
the Markov chain choice model.Operations Research, 72(4):1595–1614, 2024. 6
Jing Dong, Prakirt Jhunjhunwala, and Yash Kanoria. Human-AI interaction in product recommendation.
InNeurIPS 2025 Workshop MLxOR: Mathematical Foundations and Operational Integration of Machine
Learning for Uncertainty-Aware Decision-Making, 2025. 8
Omar El Housni, Qing Feng, and Huseyin Topaloglu. Assortment optimization under the multinomial logit
model with covering constraints.arXiv preprint arXiv:2411.10310, 2024. 7
Jacob B Feldman and Huseyin Topaloglu. Capacity constraints across nests in assortment optimization
under the nested logit model.Operations Research, 63(4):812–822, 2015. 6
Mingyang Fu and Ming Hu. Strategic buying agents.arXiv preprint arXiv:2607.04708, 2026. 8
Guillermo Gallego and Anran Li. A random consideration set model for demand estimation, assortment
optimization, and pricing.Operations Research, 72(6):2358–2374, 2024. 7
Guillermo Gallego and Huseyin Topaloglu. Constrained assortment optimization for the nested logit model.
Management Science, 60(10):2583–2601, 2014. 6
Bruce Hajek, Sewoong Oh, and Jiaming Xu. Minimax-optimal inference from partial rankings.Advances in
Neural Information Processing Systems, 27, 2014. 15, 16
John R Hauser and Birger Wernerfelt. An evaluation cost model of consideration sets.Journal of Consumer
Research, 16(4):393–408, 1990. 7
Yupeng Hou, Jiacheng Li, Zhankui He, An Yan, Xiusi Chen, and Julian McAuley. Bridging language and
items for retrieval and recommendation.arXiv preprint arXiv:2403.03952, 2024. 14
Hans Kellerer, Ulrich Pferschy, and David Pisinger.Knapsack Problems. Springer, 2004. doi: 10.1007/
978-3-540-24777-7. 34
A. G¨ urhan K¨ ok, Marshall L. Fisher, and Ramnath Vaidyanathan. Assortment planning: Review of litera-
ture and industry practice. In Narendra Agrawal and Stephen A. Smith, editors,Retail Supply Chain
Management: Quantitative Models and Empirical Studies, pages 99–153. Springer US, Boston, MA,
2009. ISBN 978-0-387-78903-3. doi: 10.1007/978-0-387-78902-6 6. URLhttps://doi.org/10.1007/
978-0-387-78902-6_6. 6
36

Wouter Kool, Herke Van Hoof, and Max Welling. Stochastic beams and where to find them: The Gumbel-top-
k trick for sampling sequences without replacement. InProceedings of the 36th International Conference
on Machine Learning, volume 97 ofProceedings of Machine Learning Research, pages 3499–3508. PMLR,
09–15 Jun 2019. 13
Xiexin Liu and Xinwei Chen. Governed agentic AI for retail baskets: A consumer world model with inventory-
aware actions.Production and Operations Management, 0(0), 2026. doi: 10.1177/10591478261458079. 8
Wentao Lu, Ozge Sahin, and Ruxian Wang. A step towards fairer assortments: Algorithms and welfare
implications. Research Paper 24-05, Johns Hopkins Carey Business School, 2023. 7
R Duncan Luce.Individual Choice Behavior.John Wiley, 1959. 2, 7, 9, 12
Paola Manzini and Marco Mariotti. Stochastic choice and consideration sets.Econometrica, 82(3):1153–1176,
2014. 7
Daniel McFadden. Conditional logit analysis of qualitative choice behavior. In Paul Zarembka, editor,
Frontiers in Econometrics, pages 105–142. Academic Press, New York, 1974. 9
Shashi Mittal and Andreas S Schulz. A general framework for designing approximation schemes for com-
binatorial optimization problems with many objectives combined into one.Operations Research, 61(2):
386–397, 2013. 30, 31
Robin L Plackett. The analysis of permutations.Journal of the Royal Statistical Society Series C: Applied
Statistics, 24(2):193–202, 1975. 2, 7, 9, 12, 16
John H Roberts and James M Lattin. Development and testing of a model of consideration set composition.
Journal of Marketing Research, 28(4):429–440, 1991. 7
Paat Rusmevichientong, Zuo-Jun Max Shen, and David B Shmoys. Dynamic assortment optimization with
a multinomial logit choice model and capacity constraint.Operations Research, 58(6):1666–1680, 2010. 28
Paat Rusmevichientong, David Shmoys, Chaoxu Tong, and Huseyin Topaloglu. Assortment optimization un-
der the multinomial logit model with random choice parameters.Production and Operations Management,
23(11):2023–2039, 2014. 6, 29
Kalyan Talluri and Garrett Van Ryzin. Revenue management under a general discrete choice model of
consumer behavior.Management Science, 50(1):15–33, 2004. 6
37

A Additional Material for Section 3
A.1 AI-Ranking Data Generation Details
Product examples.To illustrate the information supplied to the AI models, we showcase one
representative product from each product category. Product numbers are category-specific iden-
tifiers used in the ranking task. The prompt includes the product title, listed price, brand/store,
and the available category-specific attributes; fields with missing values are omitted.
•Lightning charger (product 1).Title:(MFi Apple Certified) Galvanox 1-PC Lightning
Fast iPhone Wall Charger Plug for iPhone 11/12/13/14 Pro Max (20W PD Technology).
Listed price:$21.49.Brand/store:GAL V ANOX.Category-specific attributes:wattage=20
andconnector type=lightning.
•Robot vacuum (product 1).Title:Robot Vacuum Cleaner,Sweeping Robot,Ultra Slim
Quiet,1800pa Super-Strong Suction,Cleans Hard Floors to Medium-Pile Carpets,Integral
Memory Multiple Cleaning Modes Vacuum Best for Pet Hairs.Listed price:$73.59.
Brand/store:Green Hills.Category-specific attributes:suction power pa=1800,run time
min=90,wifi=not detected,mopping=no, andself emptying=no.
•Pet leash (product 1).Title:Pet Attire ® Ribbon Nylon Leash, 5/8” x 6’.Listed
price:$9.87.Brand/store:Coastal.Category-specific attributes:product type=leash,
species=pet, andmaterial=nylon.
Prompt template.For reproducibility, we report below the complete prompt template for the
value-seeking persona. Bracketed fields are populated separately for each ranking task using the
relevant product category, the ten product records in the presented offer set, and their product
numbers. The budget-sensitive and premium-seeking prompts use the same template, with only
the opening persona instruction replaced by the corresponding persona description.
System message.
You are assisting a value-seeking customer who cares most about the best
price-to-quality tradeoff. They will pay more for a meaningful step up in
quality, but do not want to overpay for marginal improvements or for brand name
alone.
You are a personal shopping assistant evaluating [CATEGORY LABEL] products.
TASK: You will receive a list of products available in a specific offer set.
Select the best 5 products from ONLY those offered items.
RULES:
- Return valid JSON only --- a single object with a top 5 array.
38

- Return exactly five entries, ordered by preference, with ranks exactly 1
through 5.
- Each element must contain only rank and product number.
- product number MUST be one of the catalog numbers listed in the offer set.
Do not return any product number that was not offered.
- Do not select the same product number more than once.
- Do not include prose, Markdown fences, or any additional field.
User message.
Available items:
[PRODUCT RECORDS]
Pick the best 5 from this list (catalog numbers: [OFFERED PRODUCT NUMBERS])
Provider request settings.As shown above, all three providers receive the same logical prompt
and are constrained to the same JSON response structure: a single object containing atop 5array
of exactly five entries, each containing onlyrankandproduct number. OpenAI uses temperature
1.0 and a maximum output allowance of 4,096 tokens; Anthropic uses temperature 1.0 and a
maximum output allowance of 4,096 tokens. Gemini uses a 4,096-token maximum output allowance,
JSON response mode, and minimal thinking; temperature, top-p, top-k, and candidate count are
left unset.
B Additional Material for Section 4
B.1 Preference Alignment Across Capacity Configurations
Here we complement the preference-alignment analysis of Section 4.2.2 by reporting the complete
set of tested capacity configurations. Figure 6 displays mean revenue loss as a function ofρ,
separately for direct-MNL and the deterministic plug-in, for all seven (B, K) configurations.
B.2 Preference Alignment and Filtering Mechanisms
Here we complement the preference-alignment analysis of Section 4.2.2 by reporting the filtering
mechanisms across the complete set of tested capacity configurations. Figure 7 reports the mean
difference|S ⋆ PL| −Kand the active-filtering share for all seven (B, K) configurations.
C Additional Proofs for Deterministic Ranking Mediation
C.1 Proof of Theorem 5.1
Assortment planning under ranking preferences.We reduce from the assortment planning
problem under ranking preferences studied by Aouad et al. (2018). Consider a set of products
39

0 .25 .50 .75 .90 1
Preference alignment ρ
0%
5%
10%
15%
20%
25%
Direct MNL
Mean revenue loss
K = 3
0 .25 .50 .75 .90 1
Preference alignment ρ
K = 5
0 .25 .50 .75 .90 1
Preference alignment ρ
K = 7
0 .25 .50 .75 .90 1
Preference alignment ρ
0.0%
0.2%
0.4%
0.6%
0.8%
1.0%
Deterministic plug-in
Mean revenue loss
0 .25 .50 .75 .90 1
Preference alignment ρ
0 .25 .50 .75 .90 1
Preference alignment ρ
B = 8 B = 10 B = 12
Figure 6: Revenue loss by customer–AI preference alignment across the full capacity grid.
N={1, . . . , n}, where each producti∈Ngenerates revenue ¯ri >0 when purchased, and a set of
customer segmentsT. Segmentt∈ Toccurs with probabilityλ t >0, where P t∈T λt = 1, and is
associated with an ordered preference listL t = (ℓ t,1, . . . , ℓt,|Lt|) consisting of a subset ofN. The
products inL t are ordered from the most preferred to the least preferred product that segmenttis
willing to purchase. Given an assortmentS⊆N, ifS∩L t ̸=∅, letq t(S) = min{q∈ {1, . . . ,|Lt|}:
ℓt,q ∈S}. Segmenttthen purchases productℓ t,qt(S), generating revenue ¯rℓt,qt(S) . IfS∩L t =∅, the
segment makes no purchase and generates zero revenue. Thus, for every segmentt∈ T, define the
revenue generated by assortmentS⊆Nas
RRP t (S) =



¯rℓt,qt(S) , S∩L t ̸=∅,
0, S∩L t =∅.
The expected revenue of assortmentSis then
RRP(S) = X
t∈T
λtRRP t (S),
and the objective is to maximizeR RP(S) over allS⊆N. For every fixedϵ >0, this problem is
NP-hard to approximate within factorO(n 1−ϵ) (Aouad et al., 2018, Theorem 2.1).
40

0 .25 .50 .75 .90 1
Preference alignment ρ
−1
0
1
2
Mean |S ⋆ PL| − K
K = 3
0 .25 .50 .75 .90 1
Preference alignment ρ
K = 5
0 .25 .50 .75 .90 1
Preference alignment ρ
K = 7
0 .25 .50 .75 .90 1
Preference alignment ρ
0%
20%
40%
60%
80%
Active-filtering share
0 .25 .50 .75 .90 1
Preference alignment ρ
0 .25 .50 .75 .90 1
Preference alignment ρ
B = 8 B = 10 B = 12
Figure 7: Preference alignment and filtering mechanisms across the full capacity grid.
Instance construction.Consider an arbitrary instance of assortment planning under ranking
preferences as defined above. We construct an instance ofAIM D with the same product setN, the
same set of segmentsT, and the same segment probabilities (λ t)t∈T . We setK= 1 andB=n.
For every producti∈N, we set its revenue in the constructed instance tor i = 2¯ri.
For every segmentt∈ T, we construct the deterministic AI rankingσ t by first listing the
products inL t according to their order in the preference list, and then listing the products in
N\L t in increasing order of their product indices. Thus, every product inL t is ranked above every
product outsideL t, while the relative ordering of the products inL t is preserved. Finally, for every
producti∈Nand segmentt∈ T, we define the customer-side MNL weight by
vit =



1, i∈L t,
0, i /∈Lt.
The construction clearly takes polynomial time.
The following claim establishes that the reduction preserves the objective function exactly.
Claim C.1.For every assortmentS⊆N, we haveR D(S) =R RP(S).
Before proving the claim, we show how it establishes the theorem. SinceB=n, every assortment
S⊆Nis feasible in the constructed instance. Claim C.1 therefore implies that the two optimization
problems have the same objective value for every assortment, and in particular the same optimal
41

value. Moreover, anyρ-approximate assortment for the constructed instance is aρ-approximate
assortment for the original ranking-preferences instance. Hence, for every fixedϵ >0, a polynomial-
timeO(n 1−ϵ)-approximation forAIM D would yield a polynomial-timeO(n 1−ϵ)-approximation for
assortment planning under ranking preferences, contradicting Aouad et al. (2018, Theorem 2.1). It
remains to prove Claim C.1.
Proof of Claim C.1.Fix an assortmentS⊆Nand a segmentt∈ T. Suppose first thatS∩L t ̸=∅,
and letq t(S) be defined as above. Since no product precedingℓ t,qt(S) inL t belongs toS, and every
product outsideL t is ranked below every product inL t underσ t, productℓ t,qt(S) is the highest-
ranked product inSunderσ t. SinceK= 1, it is therefore the unique product displayed to segment
t. Its customer-side weight is one, and hence
Rt

{ℓt,qt(S)}

=
rℓt,qt(S)
2 = ¯rℓt,qt(S) .
This is exactly the revenue generated by segmenttin the ranking-preferences instance.
Suppose next thatS∩L t =∅. IfS=∅, both models generate zero revenue from segmentt.
Otherwise, the AI displays some producti∈S. SinceS∩L t =∅, we havei /∈L t, and therefore
vit = 0. Consequently,R t({i}) = 0, which again coincides with the revenue generated by segment
tin the ranking-preferences instance.
Thus, the segment-level revenues coincide for every segmentt∈ T. Multiplying by the segment
probabilities and summing overt∈ TgivesR D(S) =R RP(S).
C.2 Additional Proofs for Section 5.2
C.2.1 Proof of Lemma 5.4
First, fix an assortmentS∈ X τ ∗ and a segmentt∈ T. SinceM⊆S, we haveτ ∗ t ∈S. Moreover,
constraint (iii) gives P i∈S hit =K.By definition,h it = 1 if and only if productiis ranked at least
as high asτ ∗ t underσ t. Hence, exactlyKproducts inSare ranked at least as high asτ ∗ t . These
products are precisely theKhighest-ranked products inS. Therefore,C D t (S) ={i∈S:h it = 1}.
It follows that
Rt

CD t (S)  = P i∈S rivithit 1 + P i∈S vithit .
Multiplying byλ t and summing overt∈ TyieldsR D(S) =R τ ∗ (S).
We next show thatS ∗ ∈ Xτ ∗. By construction,τ ∗ t ∈C D t (S∗)⊆S ∗ for everyt∈ T, and
thereforeM⊆S ∗. Moreover,S ∗ ∈ F, so|S∗| ≤B. Since we are in the active regime,|S ∗|> K,
and thus|C D t (S∗)|=Kfor everyt∈ T. Becauseτ ∗ t is the lowest-ranked product inC D t (S∗), we
haveC D t (S∗) ={i∈S ∗ :h it = 1},and consequently, P i∈S∗ hit =Kfor everyt∈ T
It remains only to show thatS ∗ ⊆A. Suppose, toward a contradiction, that some product
i∈S ∗ \Aexists. By the definition ofA, we haveh it = 0 for everyt∈ T. Thus, productiis ranked
belowτ ∗ t for every segmentt, and hence is not contained inC D t (S∗) for any segment. Removingi
42

therefore does not alter any displayed set:C D t (S∗ \ {i}) =CD t (S∗) for everyt∈ T.Consequently,
RD(S∗ \ {i}) =RD(S∗).
SinceS ∗ \ {i} ∈ F, this gives an optimal assortment with strictly smaller cardinality thanS ∗,
contradicting the choice ofS ∗ as a minimum-cardinality optimal assortment. Therefore,S ∗ ⊆A.
We have shown thatS ∗ satisfies constraints (i)–(iii), and henceS ∗ ∈ Xτ ∗.
C.2.2 Proof of Lemma 5.7
Let
P=C−
X
i∈M
ci +mK−
X
t∈T
X
i∈M
hit.
If the exact problem is feasible, restricting a feasible solution toIyields a feasible solution to (14)
with profit exactlyP. Conversely, letx∈ {0,1} I be a feasible solution to (14) with profit at least
P. On the one hand,
X
t∈T

K−
X
i∈M
hit −
X
i∈I
hitxi
!
+

C−
X
i∈M
ci −
X
i∈I
cixi
!
≥0,
since each of them+ 1 summands is nonnegative by feasibility. On the other hand,
X
t∈T

K−
X
i∈M
hit −
X
i∈I
hitxi
!
+

C−
X
i∈M
ci −
X
i∈I
cixi
!
=P−
X
i∈I

ci +
X
t∈T
hit
!
xi ≤0,
because the profit ofxis at leastP. Thus, this sum equals zero. Since every summand is nonnega-
tive, each must equal zero. It follows that P i∈I cixi =C− P i∈M ci,and, for everyt∈ T, we haveP
i∈I hitxi =K− P i∈M hit.Moreover, P i∈I xi ≤B− |M|by feasibility. Extendingxby setting
xi = 1 for everyi∈Mtherefore yields a feasible solution to the exact problem.
43
