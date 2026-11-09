---
title: 'Balancing Trial and Reorder: A Hybrid Sequential Transformer-GBDT Ranker for On-Demand Delivery'
url: https://arxiv.org/abs/2609.16407
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Marcel Kurovski
- Attila Nagy
- Steffen Klempau
- Aleksandr Fedintsev
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.16407
pages: 10
chars: 56638
fetched_at: '2026-11-08T13:24:51+00:00'
kb_version: 1
---

# Balancing Trial and Reorder: A Hybrid Sequential Transformer-GBDT Ranker for On-Demand Delivery

Balancing Trial and Reorder: A Hybrid Sequential
Transformer–GBDT Ranker for On-Demand Delivery
Marcel Kurovski
marcel.kurovski@wolt.com
Wolt (DoorDash, Inc.)
Munich, Germany
Attila Nagy
attila.nagy@wolt.com
Wolt (DoorDash, Inc.)
Munich, Germany
Steffen Klempau
steffen.klempau@wolt.com
Wolt (DoorDash, Inc.)
Berlin, Germany
Aleksandr Fedintsev
aleksandr.fedintsev@wolt.com
Wolt (DoorDash, Inc.)
Helsinki, Finland
Abstract
On a delivery platform, personalized store ranking greatly influ-
ences what users find and order. Unlike digital-only domains, candi-
date stores are local and bound by real-time availability and delivery
operations. One central modeling tension is between surfacing new
stores for trial and preserving ranking quality for sessions with
reorder intent.
We presentUniversal Venue Ranker(UVR), a production system
deployed at Wolt that pairs a bidirectional transformer encoder for
sequential user modeling with a GBDT ranker integrating contex-
tual, user, and store features. Trained across all stores and domains
of a country while enforcing local delivery constraints at infer-
ence, UVR replaces four previously separate ranking models—three
for restaurants, one for retail—with a single unified system. Label
smoothing and trial-biased sample weighting steer the model to-
ward new stores, lifting offline trial MRR by+12%to +30%over
production while regressing reorder MRR in five of six countries.
These regressions leave Global CVR—our core online metric, which
blends trial and reorder sessions—statistically unchanged.
We validate UVR in three consecutive A/B tests, the first two
across Wolt’s largest operating markets and the third spanning
all operating countries and both domains. UVR V1 delivers+5.5%
Merchant Trial Rate and +0.16%Global CVR over the previous
production ranker; V2 adds a further+0.45%Merchant Trial Rate
on top; and V3, our cross-domain unification of the restaurant and
retail rankers, adds a further+1.31%Retail Merchant Trial Rate,
together accounting for substantial incremental gross order value
and a materially simplified serving stack.
CCS Concepts
•Information systems→Recommender systems.
Keywords
Recommender Systems, Sequential Recommendation, Session-aware
Recommendation, Learning to Rank, Transformers, Gradient-Boosted
Decision Trees, Cross-domain Recommendation, On-Demand De-
livery
1 Introduction
Wolt, a DoorDash company, is a local commerce platform oper-
ating across 30+ countries and more than 1,000 cities in Europe
and Asia for on-demand delivery across restaurants, grocery, and
retail. Together with DoorDash, the group serves over 56 million
monthly active users across 40+ countries.1 Users access this selec-
tion through multiple surfaces, from multi-list (carousel) surfaces
1As of December 2025
to single ranked lists [23], making personalized store ranking the
central task that determines which stores users see, click, and pur-
chase from. Throughout this paper we usestoreas the umbrella
term covering restaurants, grocery, and retail stores.
Recommender systems (RS) on delivery platforms face challenges
absent in digital-only domains such as streaming platforms or so-
cial networks. Candidate stores are local: eligibility depends on
delivery location, distance constraints, real-time courier availabil-
ity, merchant operating hours and workload, rendering the stores
candidate set dynamic and sparse at every request. As a multi-
sided marketplace, rankings must balance consumer relevance,
merchant exposure, and platform economics (objectives often in
tension [15, 35]) while generalizing across heterogeneous verticals
(restaurants, grocery, and retail), each with distinct consumption
patterns and business constraints. A further tension is between
reorderandtrialpurchases–the delivery-domain manifestation of
the explore–exploit trade-off [ 3]: users return to trusted stores
out of habit or convenience, yet also expect to find stores they
have not tried before, and the ranker must actively balance both.
We operationalize this trade-off as a constrained multi-objective
problem, implemented via empirically-tuned per-session weighting
(Section 4.4.2).
User behavior is sequential in nature, and purchase histories
encode strong predictive signals for future decisions [17, 27, 28].
We presentUniversal Venue Ranker(UVR), a production system
that pairs a bidirectional transformer encoder for sequential user
modeling with a gradient-boosted decision-tree (GBDT) ranker inte-
grating contextual and content features. Trained per country across
all stores and domains, UVR replaces the previous production rank-
ing stack with a single unified model. We evaluate UVR on offline
benchmarks and in large-scale A/B tests, observing improvements
in conversion rate and trial rate, which translate into increased
gross order value. We present this as a real-world industry case
study of session-aware, cross-domain personalization deployed at
production scale across 30+ countries.
2 Related Work
Transformer-based Models for Sequential User Modeling.Causal-
attention (SASRec [11]) and bidirectional-attention (BERT4Rec [27])
transformer architectures superseded earlier Markov-chain and
RNN-based sequential recommenders, with subsequent work ad-
vancing training objectives and sampling strategies [20, 21]. They
have been adopted across multiple industries; Tran et al. provide
a comprehensive survey of transformers in recommendation [28].
Transformers have further proven effective in combination with
Semantic IDsfor retrieval and search [9, 18, 24].
arXiv:2609.16407v1  [cs.IR]  14 Sep 2026

Marcel Kurovski, Attila Nagy, Steffen Klempau, and Aleksandr Fedintsev
Figure 1: Wolt’s Discovery Page
Recommender Systems in the Delivery Domain.Food and delivery
recommendation has been studied through benchmark datasets [2,
30], food-specific methods [ 12], and production architectures [4,
6, 8, 25, 34]. Relative to general e-commerce, delivery platforms
introduce compounding constraints such as local candidate sets,
real-time availability, and multi-stakeholder objectives, which re-
main underexplored in the RS literature. MTGR [ 8] exemplifies
a recent industrial trend toward target-aware, generative multi-
candidate architectures that score all candidates within a single
model pass. UVR’s classifier shares thismulti-candidate, single-
inferenceproperty–one forward pass per request scores the entire
candidate slate (Section 4.4.2)–but via a simpler, non-target-aware
bidirectional encoder rather than a generative target-aware one.
Reorder vs. Trial Behavior.The tension between reorder and trial
behavior has been studied through surrogate metrics for long-term
engagement [31] and frameworks for balancing trial and reorder
behavior [1, 3, 26, 28], primarily in music and video streaming. In
on-demand delivery, users similarly oscillate between reorder from
trusted stores and trial of new ones [12], and ranking must actively
facilitate both.
Cross-domain Recommender Systems.Cross-domain recommender
systems (CDRS) transfer knowledge across domains to mitigate
cold-start and improve recommendation quality [5, 16]. Our multi-
domain setting calls for this directly: a unified model lets behavior
learned in one vertical inform ranking in another, and naturally
handles user cold-start across domains.
UVR integrates these four threads into a single production sys-
tem.
3 Problem Formulation
We frame personalized store ranking as a sequential recommenda-
tion problem with explicit time conditioning. LetU denote the set
Table 1: Notation overview.
Symbol Meaning
U,Iuser / store sets
𝑢,𝑖a user / a store
𝑙,𝑡delivery location, absolute timestamp
𝑆𝑢 lifetime purchase sequence of user𝑢
𝑆 <𝑡 𝑢 subsequence of𝑆 𝑢 with𝑡 𝑢 𝑘 <𝑡
I<𝑡 𝑢 set of distinct stores in𝑆 <𝑡 𝑢
I𝑡 𝑢,𝑙 stores available to𝑢at(𝑙,𝑡)
𝑟 𝑡 𝑢,𝑖 purchase indicator,∈{0,1}
type(𝑢,𝑖,𝑡)purchase type∈{cs,new,rec}
ℎ𝑖(𝑢,𝑙,𝑡)transformer (classifier) score for store𝑖
𝑔(𝑖|𝑢,𝑙,𝑡)GBDT (ranker) score for store𝑖
x𝑡 𝑢,𝑖,𝑙 ranker feature vector
of users andIthe set of stores. For each user𝑢∈U, let
𝑆𝑢 = 𝑖1, 𝑖2, ..., 𝑖𝑛𝑢 , 𝑖 𝑘∈I,
denote their lifetime purchase sequence ordered by ascending times-
tamp, with𝑡 𝑢 𝑘 the absolute timestamp of the𝑘-th purchase.
For any reference time𝑡, we further introduce the time-truncated
purchase subsequence𝑆 <𝑡 𝑢 (ordered) and the corresponding store
setI <𝑡 𝑢 (unordered):
𝑆 <𝑡 𝑢 = 𝑖𝑘∈𝑆 𝑢 :𝑡 𝑢 𝑘 <𝑡 ,
I<𝑡 𝑢 ={𝑖∈I:𝑖∈𝑆 <𝑡 𝑢 }.
At request time, given a user𝑢 at delivery location𝑙 and time𝑡,
the ranker receives a candidate setI𝑡 𝑢,𝑙⊆I determined by vicinity
and operational constraints.2 The task is to impose a ranking on
I𝑡 𝑢,𝑙 via a scoring function
𝑔𝑖

𝑢,𝑙,𝑡 ∈R, 𝑖∈I 𝑡 𝑢,𝑙,
such that descending order by𝑔 minimizes the rank of the store
the user purchases from.
We denote by𝑟𝑡 𝑢,𝑖∈{ 0, 1} the indicator that user𝑢 purchases
from store𝑖at time𝑡 3. We assume single-purchase sessions:
∑︁
𝑖∈I 𝑡 𝑢,𝑙
𝑟𝑡 𝑢,𝑖 =1.(1)
Sessions with multiple purchases are reduced to the store with the
smallest production rank that received a purchase; sessions without
any purchase are discarded.
We further partition purchases into three types according to a
user’s prior history:
type(𝑢,𝑖,𝑡)=
 

csif𝑟 𝑡 𝑢,𝑖 =1andI <𝑡 𝑢 =∅,
newif𝑟 𝑡 𝑢,𝑖 =1and𝑖∉I <𝑡 𝑢 ,
recif𝑟 𝑡 𝑢,𝑖 =1and𝑖∈I <𝑡 𝑢 .
(2)
Cold-start (cs) purchases are from users with no prior purchase
history;newandrecdistinguish a trial order (first order from a
store) from a recurring order (reorder) among returning users.
2The retrieval ofI𝑡 𝑢,𝑙 fromI is out of scope for this work; in our setting it is driven by
factors such as the size of the delivery area, store availability, and courier availability.
3We use the purchase signal as our primary target; clicks enter Section 4.2 as an
auxiliary indicator𝑐𝑡 𝑢,𝑖,𝑙 . The framework extends naturally to further interaction types
(impressions, dwell time, . . . ).

Balancing Trial and Reorder: A Hybrid Sequential Transformer–GBDT Ranker for On-Demand Delivery
4 Methodology
As depicted in Figure 2, UVR is a two-stage system:
(1) a bidirectional transformerclassifier ℎ that maps a user’s
purchase sequence and request context to a vector of per-
store scores (Section 4.1);
(2) a GBDTranker 𝑔 that consumesℎ as a single scalar feature
alongside content, contextual, and user–store interaction
features (Section 4.2).
Concretely, the final score is
𝑔𝑖

𝑢,𝑙,𝑡  =GBDT  ℎ𝑖(𝑢,𝑙,𝑡),x 𝑡 𝑢,𝑖,𝑙  ,(3)
whereℎ𝑖(𝑢,𝑙,𝑡)∈R is the raw transformer logit for store 𝑖 and
user𝑢 at time𝑡, andx𝑡 𝑢,𝑖,𝑙 collects content and contextual features.
We pass the raw logit rather than a softmax probability because the
GBDT ranker is invariant to monotonic feature transformations.
UVR’s contribution is twofold: (i) it couples a sequential trans-
former to a tree-based ranker inside a single deployed stack, a stack-
ing pattern established in production search [33] and instantiated
here under hard local-availability constraints; and (ii) purchase-
type-aware weighting makes the trial/reorder trade-off directly
tunable (Section 4.4.2). The two stages are fit in sequence on dis-
joint data slices. Both are realized over a unified store vocabulary
I=I rest∪I retail, covering restaurants and retail. The following
sections describe this cross-domain UVR architecture; the experi-
mental study (Section 6) reports on the restaurant-only configura-
tions (V1, V2) followed by the cross-domain variant (V3), whose
online A/B result is reported in Section 6.3.
4.1 Classifier: User Sequence Transformer for
Next-Purchase Prediction
The classifier ℎ is an encoder-only transformer [ 29] trained as
a multi-class store classifier over I, adopting the bidirectional-
attention masked-prediction backbone of BERT4Rec [27] but nar-
rowing its random-position cloze objective to mask only the most
recent purchase in𝑆𝑢.
Partial Target Masking.Three pieces of information are avail-
able to the model at inference time and are therefore supplied
unmasked: (i) the request timestamp𝑡, from which we derive hour-
of-day, day-of-week and calendar week; (ii) the H34 cell ID of the
user’s location𝑙 (see Section 4.1.1); and (iii) the requested domain
(restaurant or retail), which is known because most user surfaces
are partitioned by domain. Two pieces of information are unknown
and are masked: (a) the target store ID𝑖★, which is the prediction
target, and (b) the product line of𝑖★, which is masked because the
model is queried per domain rather than per product line; supplying
the exact product line at the target position would constitute label
leakage.
4.1.1 Embedding Layer.Each step of the input sequence is de-
scribed by six categorical features and one continuous feature,
summarized in Table 2. The categoricals are: target store ID ∈
I∪{mask} ; product line∈PL∪{mask rest,mask retail}, where the
4H3 is an open-source hierarchical hexagonal geospatial indexing system maintained
by Uber that partitions the surface of the Earth into nested hexagonal cells. We use
resolution 8, whose cells have an average area of approximately0.74 km2, comparable
to a small neighborhood or a few city blocks. See https://h3geo.org/.
Table 2: Features Representing Purchases in User Sequences
Feature Source Masked at target?
store ID past or target purchase yes
product line past or target purchase yes (per domain)
H3 hexagon ID delivery location𝑙no
hour-of-day timestamp𝑡no
day-of-week timestamp𝑡no
week-of-year timestamp𝑡no
˜Δ𝑢 𝑘 𝑡−𝑡 𝑢 𝑘 no (=log𝛽at target)
two domain-specific mask tokens are appended beyond the real
product-line vocabulary; week-of-year; day-of-week; hour-of-day;
and the H3 cell ID of the user location. We deliberately do not feed
raw latitude and longitude into the model; discretizing location to
an H3 cell ID aligns with the granularity of our delivery operations
and shares parameters across all requests originating from the same
cell, which may also benefit cold-start users.
The continuous feature is the time gap Δ𝑢 𝑘 =𝑡−𝑡 𝑢 𝑘 from each
historical position to the target. We transform Δ𝑢 𝑘 by a log-affine
map for numerical stability:
˜Δ𝑢 𝑘 =log 𝛼Δ𝑢 𝑘+𝛽 , 𝛼,𝛽>0.(4)
At the target step (where𝑘=𝑇 and Δ𝑢 𝑇 = 0), ˜Δ𝑢 𝑇 =log𝛽 acts as a
constant offset.
Each categorical feature has its own learned embedding func-
tion. WritingC={store,pl,hex,hour,dow,week} for the set of
categorical fields, we associate one embedding function per field,
𝐸𝑐 :X𝑐→R𝑑𝑐, 𝑐∈C,
whereX𝑐 is the input vocabulary for field𝑐 (for example,Xstore =
I∪{mask} andXpl =PL∪{mask rest,mask retail}). We denote by
𝑥𝑐 𝑘 the value of field𝑐at step𝑘. The input representation at step𝑘
is obtained by concatenating the six per-field embeddings with the
transformed continuous gap and projecting to the model dimension
𝑑model:
e𝑘 =𝑊 in
h 𝐸𝑐(𝑥𝑐 𝑘) 𝑐∈C∥ ˜Δ𝑢 𝑘 i +b in +1[𝑘=𝑇]d dom(𝑖 ★),(5)
where∥ denotes concatenation, 𝐸𝑐(𝑥𝑐 𝑘) 𝑐∈C is the concatenation
of the per-field embeddings in a fixed canonical order,𝑊in, bin are
the parameters of the linear input projection, and the indicator
1[𝑘=𝑇] restricts the domain embeddingd dom(𝑖 ★)∈R 𝑑model to the
target step.
Two-level domain conditioning.We inject the requested do-
main at the target step at two points of the embedding pipeline.
Pre-projection, the target’s product line carries either maskrest or
maskretail, which is processed by the product-line embedding along-
side the other five categoricals.Post-projection, the additive term
1[𝑘=𝑇] ddom(𝑖 ★) in Eq. 5 is a dedicated domain embedding, re-
stricted by the indicator to the target step. At𝑘=𝑇 we additionally
substitute the store and product-line inputs by their mask tokens,
𝑥store 𝑇 =maskand𝑥 pl 𝑇 =mask dom(𝑖 ★).
We found that supplying the domain signal only through the
pre-projection mask led to severe dilution as the representation
propagated through successive encoder layers; the additive post-
projection embedding instead acts as a clean, isolated signal in
𝑑model-space and sharpens conditioning without disrupting the rest

Marcel Kurovski, Attila Nagy, Steffen Klempau, and Aleksandr Fedintsev
user purchase history
ddom
𝑘=1
target𝑇
Embedding
Projection
+
e1 𝑢,𝑙
e𝑇 𝑢,𝑙
Transformer
Encoder
(𝐿=4,𝐻=4)
z1 𝑢,𝑙
z𝑇 𝑢,𝑙
Prediction Head
ℎ𝑖 for𝑖∈I 𝑡 𝑢,𝑙
X𝑡 𝑢,𝑙
Restaurant
GBDT
Retail
GBDTscoring
Ranking
restaurant
retail
product line
context (time, location)
store / pl mask
Figure 2: UVR architecture: bidirectional Transformer classifierℎfeeding domain-specific GBDT rankers𝑔.
of the encoder input. We also experimented with FiLM-style feature-
wise affine modulation [19] of the encoder activations but did not
observe a benefit over the simpler additive scheme.
4.1.2 Encoder Layer. 5
We stack𝐿= 4identical transformer encoder layers with pre-
LayerNorm [32], multi-head self-attention with𝐻= 4heads, and a
feed-forward sub-layer of hidden size𝑑ff = 160. The model dimen-
sion is𝑑model = 128. Sequences shorter than the context length𝑇
are left-padded with zero embeddings; padding positions are addi-
tionally excluded from attention via a key-padding mask. No causal
mask is applied: the target step attends to all historical positions.
We denote the encoder output at the target step byz𝑇 𝑢,𝑙∈R 𝑑model.
4.1.3 Prediction Layer.A single linear head with weight matrix
𝑊out∈R|I|×𝑑 model and biasb out∈R|I| projectsz𝑇 𝑢,𝑙 to a logit vector
over the full store vocabulary,
ℎ(𝑢,𝑙,𝑡)=𝑊 out z𝑇 𝑢,𝑙+b out ∈R |I|,
and we writeℎ𝑖(𝑢,𝑙,𝑡)=

𝑊out

𝑖,: z𝑇 𝑢,𝑙+𝑏 out,𝑖 for the per-store logit.
At training time we minimize a per-sample-weighted, label-
smoothed softmax cross-entropy loss whose denominator is re-
stricted to the in-domain vocabularyIdom(𝑖 ★) of the ground-truth
store, preventing cross-domain leakage during gradient updates.
With label-smoothing parameter 𝜀∈[ 0, 1), the smoothed target
distribution is
˜𝑦𝑗 =(1−𝜀)1[𝑗=𝑖 ★] + 𝜀 |I dom(𝑖 ★)|, 𝑗∈I dom(𝑖 ★),
and the loss is
L(𝜃)=−
∑︁
(𝑢,𝑙,𝑡,𝑖 ★)∈D
𝑤𝑡 𝑢,𝑖★
∑︁
𝑗∈I dom(𝑖 ★)
˜𝑦𝑗 log expℎ𝑗(𝑢,𝑙,𝑡)˝
𝑘∈I dom(𝑖 ★) expℎ𝑘(𝑢,𝑙,𝑡) .
(6)
The per-sample weights𝑤𝑡 𝑢,𝑖★ are tied to the purchase type de-
fined in Equation 2 and follow the ordering 𝑤 new >𝑤 cs >𝑤 rec,
biasing the gradient towards stores the user has not yet purchased
from while still rewarding correct predictions of returning pur-
chases. At inference time the classifier is queried once per request
with its(𝑢,𝑙,𝑡) context; only the raw logitsℎ𝑖(𝑢,𝑙,𝑡) for the candi-
date stores𝑖∈I 𝑡 𝑢,𝑙 are retained and passed to the ranker.
5Reported values are for V1 and V2. V3 widens the architecture to𝐻= 6,𝑑model = 192,
𝑑ff = 384and trains for 𝐸= 12epochs (instead of the 𝐸= 15used by V1 and V2); the
encoder depth𝐿=4and all other hyperparameters in Section 4.4 are unchanged.
Cold-start handling.For cold-start users the encoder input
collapses to a single (partially masked) target step. The cold-start
signal is therefore implicit in the input length: with no historical
positions to attend to, the model produces a domain-, location- and
time-conditioned prior over stores from the target step alone. Note
that the contextual features at the target (hex, hour, day-of-week,
week) are not themselves sufficient to identify a user as cold-start,
since two co-located requests at the same timestamp from different
users (one cold-start, one returning) share those features exactly;
the discriminating signal is the absence of historical positions, not
the contents of the target step.
4.2 Ranker: GBDT for Listwise Store Ranking
The ranker𝑔 is a GBDT model implemented with CatBoost [ 22],
taking per-(user, candidate-store) feature vectorsx 𝑡 𝑢,𝑖,𝑙 over the
candidate setI𝑡 𝑢,𝑙; training and label construction are detailed in
Section 4.4.2.
The feature vectorx𝑡 𝑢,𝑖,𝑙 comprises four groups:
• Classifier signal(single scalar): the per-candidate trans-
former logitℎ𝑖(𝑢,𝑙,𝑡).
• Store content features: rating, conversion rate, retention
rate, and assortment size (e.g. menu size for restaurants,
in-stock item count for retail), etc.
• Contextual features: delivery distance, delivery price, and
location-derived signals, etc.
• User–store interaction features: recent click counts, mean
basket size, and trial ratio, etc.
Two domain-specific rankers are trained because the content and
contextual feature sets differ structurally between restaurant and
retail candidates (e.g. menu size is restaurant-only; in-stock item
count is retail-only).
4.3 Coupling and Cross-Domain Transfer
Cross-domain transfer enters through (a) the chronologically inter-
leaved sequence𝑆 <𝑡 𝑢 , (b) the per-position product-line embedding,
and (c) the two-level domain conditioning at the target step (Sec-
tion 4.1.1). A user’s restaurant history thus informs their retail
next-store prediction and vice versa, and the per-domain rankers
inherit this transfer through the shared classifier logitℎ𝑖(𝑢,𝑙,𝑡).

Balancing Trial and Reorder: A Hybrid Sequential Transformer–GBDT Ranker for On-Demand Delivery
Table 3: Comparison of UVR versions. V1, V2, and V3 are
evaluated in Section 6.
Version Domains Ranker Loss Notable additions
V1 restaurants PairLogit(country-
specificmax_pairs)
—
V2 restaurants YetiRank-
Pairwise:NDCG
label smoothing; trial
weighting
V3 restaurants
+ retail
YetiRank-
Pairwise:NDCG
cross-domain coupling;
product-line embedding
4.4 Model Training and Validation
We train one country-specific UVR model for each of the 30 coun-
tries Wolt operates in, and re-train it daily. This is a deliberate
trade-off between training complexity, resource utilization, model
degradation, and store cold-start. We do not observe a clear perfor-
mance trend over the first∼28 days post-training; the daily cadence
is instead driven by store cold-start: the store, H3 cell, and product-
line embedding tables (Section 4.1.1) are populated only for values
observed during training, making the classifiertransductivewith re-
spect to these three vocabularies butinductivewith respect to time
(hour-of-day, day-of-week, week-of-year embeddings are allocated
exhaustively at construction). Without daily retraining the number
of unseen stores accumulates rapidly and degrades predictions. A
complementary mitigation through supplementary content-based
store features is left for future work, e.g. by adopting DenseRec [13].
We train and validate UVR in two stages: first the classifier
(Section 4.4.1), then the ranker (Section 4.4.2), since the trained
classifier is needed to score the candidate slates that constitute the
ranker’s training, validation, and test data. The two stages operate
on disjoint data slices: the classifier is trained on prefixes𝑆 <(𝑡−2d) 𝑢 ,
i.e. the last purchase of any sequence is guaranteed to happen
before the ranker’s validation and test sessions. This prevents both
the ranker’s validation day (which drives early stopping) and its
held-out test day from leaking into the classifier’s training set.
4.4.1 Classifier.
Data split.We adopt a user-based split of user purchase se-
quences into a90%training set Dtrain c and a10%validation set
Dval c . Any sequence inDval c that references a store ID, an H3 cell ID,
or a product line absent fromDtrain c is moved back to the training
set; given the transductive nature of the classifier with respect to
these three feature fields (Section 4.4), this guarantees that every
entity observed at validation time also occurs in the training corpus
and therefore has an associated learned embedding. Sequences are
capped to the most recent𝑀 purchases per user, since we observe
diminishing returns from longer histories, consistent with the find-
ings of Pancha et al. [ 17]. See appendix Section B for a detailed
analysis.
Validation decomposition.We further partition Dval c by the type
of the target purchase, defined in Equation 2. Writing 𝑖𝑢 𝑇 for the
most recent (target) purchase of user𝑢at time𝑡 𝑢 𝑇 ,
Dval𝜏 c =  𝑆𝑢∈D val c : type(𝑢,𝑖 𝑢 𝑇,𝑡𝑢 𝑇)=𝜏 	 ,
𝜏∈{cs,new,rec}.(7)
This decomposition lets us monitor cold-start, trial, and reorder
performance independently during training.
Optimization.We train the transformer for 𝐸= 15epochs with
a training batch size of256and a validation batch size of1024. We
use AdamW[14] with learning rate 𝜂= 10−3 and weight decay
𝜔= 0.15, combined with a multi-step learning-rate schedule that
decays𝜂 by a factor of𝛾= 0.1at epochs {4, 6, 7}. Training runs in
mixed-precision bfloat16 autocast on a single A10G GPU, with
the loss in Equation 6 computed at label-smoothing 𝜀= 0.2and
per-sample weights ordered𝑤 new >𝑤 cs >𝑤 rec.
Checkpoint selection.After each epoch we evaluate the model
on the three validation subsets in Equation 7. For each store 𝑖,
letN𝑖 ⊂I be the set of same-country stores within Haversine
distance𝐷 of𝑖,𝑖 itself included. For each𝑆𝑢 we score the classifier
onN𝑖𝑢 𝑇 , compute the rank of𝑖𝑢 𝑇 , and aggregate to mean reciprocal
rank (MRR) acrossDval𝜏 c . On thenewslice we further exclude I<𝑡 𝑢
from the scored set, so the target competes only against stores
the user has not yet purchased from. We retain the checkpoint
with the highest MRR on Dvalnew c , optimizing explicitly for trial
recommendations; therecandcsMRRs serve as guardrails.
4.4.2 Ranker.
Data.The ranker operates over user sessions rather than pur-
chase sequences. Following the assumptions in Section 3, we focus
on single-purchase sessions (Equation 1); sessions without any pur-
chase are dropped as low-intent noise. A session in which several
stores received a purchase is normalized to a single-purchase ses-
sion by keeping𝑟𝑡 𝑢,𝑖 = 1for the purchased store with the smallest
production rank and setting 𝑟𝑡 𝑢,𝑗 ← 0for every other purchased
store 𝑗≠𝑖 in the same session, so the single-purchase constraint
of Equation 1 holds for every session in the resulting dataset. We
define the ranker dataset as a set of session tuples
D𝑟 =
 𝑢,𝑙,𝑡, 𝑖+,I 𝑡 𝑢,𝑙,X 𝑡 𝑢,𝑙, 𝜌prod,o 𝑡 𝑢,𝑙,c 𝑡 𝑢,𝑙  	 ,(8)
where the session is uniquely identified by the(𝑢,𝑙,𝑡) triple,𝑖+∈
I𝑡 𝑢,𝑙 is the purchased store (the unique𝑖 for which𝑟𝑡 𝑢,𝑖 = 1after the
normalization above),X𝑡 𝑢,𝑙 =( x𝑡 𝑢,𝑖,𝑙)𝑖∈I 𝑡 𝑢,𝑙 collects the per-candidate
feature vectors, 𝜌 prod : I𝑡 𝑢,𝑙 → {1,...,|I 𝑡 𝑢,𝑙|} is the production
ranking served at request time, ando 𝑡 𝑢,𝑙, c𝑡 𝑢,𝑙∈{ 0, 1}|I 𝑡 𝑢,𝑙| are per-
candidate impression and click indicators (𝑜𝑡 𝑢,𝑖,𝑙 = 1iff 𝑖 was shown
to the user during the session,𝑐𝑡 𝑢,𝑖,𝑙 = 1iff 𝑖 was clicked ). At this
stagex 𝑡 𝑢,𝑖,𝑙 contains only content, contextual, and user–store in-
teraction features; the classifier signalℎ𝑖(𝑢,𝑙,𝑡) is appended later
(“Coupling with the classifier” below).
Time-based split.We use the most recent30days of sessions
and adopt a time-based train/validation/test split, disjoint from the
classifier’s user-based split: the first28days formDtrain 𝑟 , the second-
to-last day formsDval 𝑟 (used for early stopping), and the last day
is held out asDtest 𝑟 . The two-day cutoff applied to the classifier’s
training horizon (Section 4.4) is what enforces the disjointness:
where a training prefix𝑆 <𝑡′ 𝑢 allowed to terminate on the ranker’s
validation or test day, the corresponding target purchase would be
the same event that the ranker uses as its label on Dval 𝑟 orDtest 𝑟 ,
and the classifier logitℎ𝑖+(𝑢,𝑙,𝑡) subsequently fed to the ranker as

Marcel Kurovski, Attila Nagy, Steffen Klempau, and Aleksandr Fedintsev
a feature would carry direct knowledge of the held-out target. By
training the classifier only on prefixes𝑆 <(𝑡−2d) 𝑢 we ensure no such
overlap can occur and thatℎ𝑖(𝑢,𝑙,𝑡) , evaluated onDval 𝑟 andDtest 𝑟 ,
is a true out-of-sample prediction.
Training-set restriction.On Dtrain 𝑟 we restrict each session to its
impressed stores{𝑖∈I 𝑡 𝑢,𝑙 :𝑜𝑡 𝑢,𝑖,𝑙 = 1}. These are harder negatives
than stores the user never saw: the production system already
considered them attractive enough to display, so the ranker must
learn to discriminate purchases fromcompetitivealternatives rather
than from random stores in the catalogue. OnDval 𝑟 andDtest 𝑟 we
keep the entire candidate setI𝑡 𝑢,𝑙, including unseen stores, because
this matches inference: at request time the ranker must order the full
slate without knowing which subset will be impressed to the user.
The training data is therefore drawn from historical user session
logs joined with impression events, while validation and test data
couple the same sessions with the full backend slate.
Coupling with the classifier.For each session (𝑢,𝑙,𝑡,...)∈D 𝑟 ,
we reconstruct the user’s purchase sequence as it stood at request
time,𝑆 <𝑡 𝑢 , and append the partially masked target step. The target
step carries the request’s H3 cell𝑙, calendar features derived from𝑡,
and the domain-specific product-line mask maskdom (with dom∈
{rest,retail} chosen according to which per-domain ranker is being
trained). A single forward pass of the trained classifier ℎ on this
input yields the unified logit vector, from which we gather the
per-candidate logits{ℎ𝑖(𝑢,𝑙,𝑡)} 𝑖∈I 𝑡 𝑢,𝑙 and appendℎ𝑖(𝑢,𝑙,𝑡) tox𝑡 𝑢,𝑖,𝑙
as one additional ranker feature. Note thatℎ is invoked once per
session, not once per (session, candidate) pair: the candidate logits
are read out from the same forward pass via a singleO(|I 𝑡 𝑢,𝑙|) gather,
so the offline join scales linearly in the number of sessions rather
than in the number of (session, candidate) pairs.
Loss and labels.Both rankers use the session identifier as the
ranking group. In V1 we used a pairwise BPR-style logistic loss
(PairLogit) with the number of negatives max_pairs tuned per
country, and negatives drawn from impressed-but-not-purchased
stores. With V2’s trial-oriented upgrade we switched to the list-
aware pairwise objectiveYetiRankPairwisewith mode=NDCG [7],
which let us additionally incorporate clicks as graded relevance.
Concretely, YetiRank builds a position-dependent weight for each
pair by repeatedly perturbing the current model scores with random
noise and re-ranking; pairs of candidates that land adjacent near the
top of these perturbed rankings accumulate a larger weight than
pairs deep in the list, concentrating learning signal on the compar-
isons most likely to affect the top of the served ranking [7]. Setting
mode=NDCG selects NDCG as the target metric this weighting is
calibrated toward. We assign a per-row label as a function of the
purchase indicator𝑟𝑡 𝑢,𝑖, the click indicator𝑐𝑡 𝑢,𝑖,𝑙 , and the user–store
relationship rel(𝑢,𝑖,𝑡)∈{new,rec} , defined asrecif 𝑖∈I <𝑡 𝑢 and
newotherwise—the binary projection of Equation 2 extended to
click rows, withcsfolded intonew:
𝑦𝑡 𝑢,𝑖,𝑙 =
 

𝜆 p,new if𝑟 𝑡 𝑢,𝑖 =1,rel=new,
𝜆 p,rec if𝑟 𝑡 𝑢,𝑖 =1,rel=rec,
𝜆 c,new if𝑟 𝑡 𝑢,𝑖 =0,𝑐 𝑡 𝑢,𝑖,𝑙 =1,rel=new,
𝜆 c,rec if𝑟 𝑡 𝑢,𝑖 =0,𝑐 𝑡 𝑢,𝑖,𝑙 =1,rel=rec,
0otherwise.
(9)
The case predicates partition{0, 1}2 along the purchase axis first,
so a row that records both a click and a purchase is treated as a
purchase rather than a click. The constants are calibrated so that
purchase signal dominates click signal and click signal in turn
dominates the absence of interaction:𝜆 p,new =𝜆 p,rec >𝜆 c,new >
𝜆 c,rec > 0. The two purchase-row labels are equal because the
trial-vs-reorder distinction is already captured at the session level
via group weights, applied to the listwise NDCG-style loss; the row
label only needs to express the relative strength of the implicit-
feedback signal. We additionally use per-session weights ordered
𝑤 new >𝑤 rec, biasing the ranker toward trial sessions while preserv-
ing reorder performance. Unlike the classifier, the ranker collapses
cs and non-cs new sessions into a single𝑤 new; a separate cs weight
could yield finer control and is left to future work.
We frame this as a constrained multi-objective problem: maxi-
mize trial ranking quality subject to a bounded reorder regression.
The per-session weight ratio (𝑤 new/𝑤rec) is this constraint’s empir-
ically tuned Lagrange multiplier; Appendix A’s grid sweep traces
the resulting Pareto frontier as the multiplier varies. Tuning a single
scalarization weight empirically, rather than deriving it analytically,
mirrors established practice in multi-objective learning-to-rank and
explore/exploit systems [3, 26].
Per-domain rankers.We train one ranker for the restaurant do-
main (introduced in V1) and, since V3, an additional ranker for
the retail domain. Both share the same loss and label scheme and
most optimization settings. Both are trained for𝑇𝑟 = 500boosting
iterations with tree depth8, learning rate0 .05, and L2 leaf regular-
ization3.0, with early stopping onDval 𝑟 after50rounds without
improvement.
4.5 Testing and Benchmarking
After training has concluded, we evaluate the per-domain ranker
on the held-out last day of sessionsDtest 𝑟 . We compute MRR per
purchase type from Equation 2–separately forcs,new, andrec
targets–and across four scoring functions: a benchmark𝑏, the pro-
duction ranking 𝜌 prod, the classifier ℎ, and the trained ranker 𝑔,
yielding twelve MRR values per evaluation run and model domain.
The benchmark𝑏 combines a binary reorder indicator with a store-
relative popularity score; aside from the reorder indicator (which is
itself user-specific) it uses no further personalized signal, providing
a strong yetweakly personalizedreference. On thenewslice we
consistently observe
MRR𝑏 <MRR 𝜌prod <MRR 𝑔 andMRR ℎ <MRR 𝑔,(10)
in every country and for both versions, while the position of ℎ
relative to𝜌 prod is country-dependent (Table 4). Onrecthe ordering
depends on the operating point: at trial-weighted settings 𝑔 can
fall below bothℎ and𝜌 prod (Section 6.2, Appendix A). We therefore

Balancing Trial and Reorder: A Hybrid Sequential Transformer–GBDT Ranker for On-Demand Delivery
apply the safeguard on the trial side: a new ranker is blocked from
roll-out if its MRR on thenewsegment fails to exceed MRR𝑏 at
95%confidence (the lower bound of a two-sigma interval around
MRR𝑔 must exceed MRR𝑏). Performance onrecis monitored as a
guardrail and surfaces a warning, but does not block deployment.
5 Training and Serving Infrastructure
We launch parallel daily training jobs for each country on our
internal Kubernetes cluster, orchestrated via Flyte6. User interaction
sequences for inference are generated during training and written
to an online feature store to keep training and serving features
synchronized. Since purchases are relatively sparse signals, daily
updates were sufficient in our setting.
Additional feature groups–including content, contextual, and
user-store interaction features–are computed through separate
batch pipelines and published to the online feature store at ca-
dences ranging from a few hours to daily, depending on upstream
data availability.
At inference time, the ranking service retrieves all required fea-
tures from the online feature store, computes the transformer-based
classifier logits on CPUs, and applies the downstream GBDT ranker
to produce the final store ranking. The end-to-end serving pipeline
has a p99 latency of approximately 60 ms, including feature retrieval,
model inference, and serialization.
6 Experiment Results
We report offline and online results for V1 and V2, the two produc-
tion rollouts of UVR; their architectural and loss-function differ-
ences are summarized in Table 3. V1 and V2 are restaurant-only;
V3, our cross-domain unification, is evaluated separately below
(Section 6.3). The offline benchmarks in this section therefore focus
on the restaurant domain, which dominates Wolt’s order volume.
Substantial offline uplifts gave us the conviction to carry both ver-
sions forward to A/B tests: V1 was rolled out in 2025 while V2
was deployed to production and replaced V1 in early 2026. V3 then
replaced V2 a few months later. Throughout the section, we focus
on a subset of our largest operating countries by purchase volume,
which together account for more than50%of Wolt’s worldwide
order volume and provide a representative cross-section while keep-
ing experimental complexity manageable.
6.1 Baselines
We compare UVR against the production stack it was designed
to subsume, which consists of four ranking models split across
two domains. In the restaurant domain we operate three models:
Neural Collaborative Filtering [ 10] with BPR-loss as a first-pass
ranker (FPR), a DNN-based context- and content-aware second-
pass ranker (SPR), and a GBDT-based ranker for cold-start users
(CSR). In the retail domain we operate a single GBDT-based ranker
(RR). The offline experiments below report uplifts of UVR over this
stack, and the online A/B tests (Section 6.3) use FPR+SPR/CSR as
the V1 control arm.
6https://flyte.org/
Table 4: Relative MRR uplift of V1/V2 over production, by
country and purchase type (new/rec); classifierℎ and ranker
𝑔reported separately.
UVR V1 UVR V2
Country Modelnew rec new rec
ISR Classifier−0.5%−3.6%+2.2%−4.2% Ranker+19.7%+5.0%+30.3%−12.5%
GRC Classifier+4.7%−8.7%+5.0%−8.7% Ranker+17.6%−5.0%+22.3%−7.8%
DEU Classifier+4.8%−17.0%+6.4%−16.6% Ranker+19.8%−11.4%+29.0%−27.3%
FIN Classifier−4.8%+6.2%−3.5%+7.7% Ranker+7.5%+11.2%+12.5%+6.7%
HUN Classifier−0.6%+0.3%−1.0%+1.3% Ranker+7.7%+9.4%+14.3%−1.4%
DNK Classifier−3.1%+4.0%−1.7%+5.7% Ranker+9.0%+7.6%+14.5%−5.8%
6.2 Offline Testing
We report the relative MRR improvement of the classifier ℎ and
ranker𝑔 over production, broken down by purchase type; absolute
volumes are omitted due to confidentiality. Headline numbers are
anchored at a Sunday peak-volume test day, with results on other
days directionally consistent. Table 4 reports per-country uplifts
for V1 and V2 onnewandrecurring purchases; we omitcsas its
session volume in this slice is negligible. A single-country study
with multiple training seeds shows run-to-run standard deviation of
∼10-30% relative to the mean uplifts; individual cells are therefore
directional.
V1 (PairLogit) over the production ranker.The ranker 𝑔 improves
over the classifierℎ in all12of12(country, purchase-type) cells,
confirming that content and contextual features carry information
complementary to the sequence signal alone. The improvement
holds uniformly across bothnewandrecpurchases: every country
gains onnew(range +7.5%to+19.8%), and the ranker also recovers
ground onrecrelative to the classifier in every country.
V2 (YetiRankPairwise:NDCG) over V1.The picture splits along
the trial/reorder axis. Onnew, V2 amplifies the V1 gains uni-
formly across all six countries (e.g. ISR +19.7%→+ 30.3%, DEU
+19.8%→+ 29.0%), in line with the design intent of the listwise
NDCG-aware loss. Onrecurring purchases, however, the classifier
alone outperforms the V2 ranker in five of six countries (ISR, DEU,
FIN, HUN, DNK; only GRC remains in the ranker’s favor), suggest-
ing that the trial-oriented loss penalizes reorder relevance more
aggressively than V1’s PairLogit. Section 6.3 tests whether this
trade-off surfaces in production; Appendix A dissects the ranker-
level levers driving it via a controlled ablation with the classifier
held fixed.
Operating point selection.From the sweep of Appendix A we
discard every setting with a negativenewMRR uplift, then take
the setting with the largestnewuplift whoserecregression stays
within−15%. This makes the constraint of Section 4.4.2 explicit.
DEU is the one country where no setting satisfied the bound.

Marcel Kurovski, Attila Nagy, Steffen Klempau, and Aleksandr Fedintsev
Table 5: Online A/B outcomes per UVR version (V1 vs.
FPR+SPR/CSR; V2 vs. V1; V3 vs. V2+RR). Merchant Trial
Rate gains are significant at 𝛼= 0.05; Global CVR is reported
with its𝑝-value.
Version Merchant Trial Rate Global CVR
V1+5.5%+0.16%(𝑝=0.017)
V2+0.45%−0.05%(𝑝=0.398)
V3+1.31% † +0.04%(𝑝=0.457)
†Retail domain.
6.3 Online A/B Testing
The offline uplifts in Section 6.2, combined with our internal experi-
ence with the predecessor FPR and SPR rankers (where offline MRR
gains had consistently translated into online wins), motivated three
consecutive A/B tests. All three tests used a 50:50 user-level random
split over all registered users, cold-start and returning alike. V1 and
V2 ran for two weeks across the ten largest operating countries;
V3 ran for three weeks across all operating countries, reflecting
the larger sample needed for retail-domain significance. The target
metrics were the daily global conversion rate (Global CVR) and the
daily Merchant Trial Rate, which captures first-time ordering from
a store. Table 5 summarizes the per-version outcomes.
Three observations stand out. First, the V1 Merchant Trial Rate
gain of+5.5%confirms that UVR effectively pushes trial in produc-
tion; combined with the simultaneous+0.16%Global CVR uplift,
this shows that the trial push does not come at the expense of con-
versions. Second, V2’s+0.45%Merchant Trial Rate gain on top of
an already strong V1 baseline confirms that the listwise loss, along
with label smoothing and an additional trial feature, continues to
deliver incremental trial value. Third, V3’s+1.31%Merchant Trial
Rate gain is measured on the retail domain–V1 and V2’s figures
above are restaurant-domain–confirming that unifying the restau-
rant and retail rankers lifts retail discovery with no significant
change in restaurant-domain trial rate or blended Global CVR. Ads
revenue regressed significantly under both V1 and V3 (−0.43%for
V3), which we read as confirmation of effectiveness: personalized
ranking outgrew the Ads stack, which still relied on a variant of the
previous production restaurant ranker. RR was retired upon V3’s
rollout, completing the consolidation of four legacy rankers into
one.
6.4 Discussion and Limitations
The online results confirm that the trial side of the trade-off can
be steered effectively, and that steering it is compatible with a con-
version gain (V1:+5.5%Merchant Trial Rate with+0.16%Global
CVR). The partial offline reorder regressions of Section 6.2 left the
blended metric statistically unchanged (|Δ|< 0.1%,𝑝> 0.39). Be-
yond ranking quality, consolidating FPR, SPR, CSR, and RR into a
single cross-domain model (V3) substantially reduces operational
complexity, retiring the last of four legacy rankers. The control arm
reflects the original rank, which includes ad placements and dedu-
plication beyond the ranker, so a direct model-to-model comparison
would likely narrow the observed gap.
The V3 result validates the business case for cross-domain unifi-
cation but does not by itself isolate the contribution of cross-domain
transfer, i.e., whether retail benefits from shared restaurant pur-
chase signal, or simply from finally having a transformer+GBDT
stack rather than a single GBDT (RR). Two ablations would sharpen
the attribution: a domain-siloed transformer+GBDT retail model,
separating transfer from the mere presence of a sequence stage,
and an otherwise-identical ranker trained without the classifier
logit, isolating the transformer’s marginal contribution. The closest
evidence we report is the classifier-versus-ranker comparison of
Table 4 alongside the two purely tree-based production baselines
(CSR, RR); feature sets, losses, and training data differ, so neither is
controlled. Under a fixed engineering timeline we prioritized the
online tests; each ablation is a single training run and we will report
both.
Three limitations are worth noting. First, UVR runs on purchase
histories with up to one day of delay and does not exploit real-time
interaction signals; the architecture could readily accommodate
these as first-class sequence events. Second, the transductive pre-
diction head restricts the classifier to stores seen during training,
leaving new stores reliant on the GBDT’s content features alone.
Third, restricting the sequence to purchases leaves other useful
signals (clicks, browsing, dwell time) untapped, which could benefit
users with sparse histories.
7 Conclusion
We presented UVR, a production transformer–GBDT system that
consolidates four specialized rankers—three for restaurants, one
for retail—into a single unified model. Three consecutive A/B tests
validated the approach: V1 delivered+5.5%Merchant Trial Rate
with a simultaneous+0.16%Global CVR uplift; V2 added a further
+0.45%Merchant Trial Rate; and V3, our cross-domain unification,
delivered a further+1.31%Retail Merchant Trial Rate while retiring
the last domain-specific legacy ranker. The hybrid architecture
makes the trial/reorder balance an explicit operating point: the per-
session weight ratio𝑤 new/𝑤rec and the sampled-negative count
max_pairs scalarize a constrained multi-objective problem, and
150 ranker retrains trace the frontier they span (Appendix A). At
the ratio we deploy, this buys+12%to+30%offline trial MRR over
production and costs reorder MRR in five of six countries, a trade
that did not surface in Global CVR. Future work focuses on target-
aware conditioning of the transformer on the candidate stores,
inductive content store representations for cold-start mitigation,
and real-time interaction signals for short-term intent.
Acknowledgments
The authors would like to thank Adam Smaili, Daniel Lazar, Paavo
Camps, Tanja Menković, Ibrahim Omer Celik, Dzung Nguyen, Ser-
gio Gonzalez Sanz as well as the Machine Learning Platform, Ana-
lytics and Product Management teams at Wolt who contributed or
supported us throughout this project.

Balancing Trial and Reorder: A Hybrid Sequential Transformer–GBDT Ranker for On-Demand Delivery
References
[1] Ashton Anderson, Lucas Maystre, Ian Anderson, Rishabh Mehrotra, and Mounia
Lalmas. 2020. Algorithmic Effects on the Diversity of Consumption on Spotify. In
Proceedings of The Web Conference 2020(Taipei, Taiwan)(WWW ’20). Association
for Computing Machinery, New York, NY, USA, 2155–2165. doi:10.1145/3366423.
3380281
[2] Zhenisbek Assylbekov et al . 2023. Delivery Hero Recommendation Dataset
(DHRD): A Novel Dataset for Benchmarking Recommendation Algorithms. In
Proceedings of the 17th ACM Conference on Recommender Systems (RecSys ’23).
ACM.
[3] Minmin Chen, Yuyan Wang, Can Xu, Ya Le, Mohit Sharma, Lee Richardson, Su-
Lin Wu, and Ed Chi. 2021. Values of user exploration in recommender systems.
InProceedings of the 15th acm Conference on recommender systems. 85–95.
[4] Alex Egg. 2021. Online learning for recommendations at grubhub. InProceedings
of the 15th ACM Conference on Recommender Systems. 569–571.
[5] Ali Mamdouh Elkahky, Yang Song, and Xiaodong He. 2015. A Multi-View Deep
Learning Approach for Cross Domain User Modeling in Recommendation Sys-
tems(WWW ’15). International World Wide Web Conferences Steering Commit-
tee, Republic and Canton of Geneva, CHE, 278–288. doi:10.1145/2736277.2741667
[6] Zhichao Feng, JunJie Xie, Kaiyuan Li, Yu Qin, Pengfei Wang, Qianzhong Li,
Bin Yin, Xiang Li, Wei Lin, and Shangguang Wang. 2024. Context-based fast
recommendation strategy for long user behavior sequence in Meituan Waimai.
InCompanion Proceedings of the ACM Web Conference 2024. 355–363.
[7] Andrey Gulin, Igor Kuralenok, and Dmitry Pavlov. 2011. Winning The Trans-
fer Learning Track of Yahoo!’s Learning To Rank Challenge with YetiRank. In
Proceedings of the Yahoo! Learning to Rank Challenge (Proceedings of Machine
Learning Research, Vol. 14). PMLR, 63–76. https://proceedings.mlr.press/v14/
gulin11a.html
[8] Ruidong Han, Bin Yin, Shangyu Chen, He Jiang, Fei Jiang, Xiang Li, Chi Ma,
Mincong Huang, Xiaoguang Li, Chunzhen Jing, et al . 2025. Mtgr: Industrial-
scale generative recommendation framework in meituan. InProceedings of the
34th ACM International Conference on Information and Knowledge Management.
5731–5738.
[9] Ruining He, Lukasz Heldt, Lichan Hong, Raghunandan Keshavan, Shifan Mao,
Nikhil Mehta, Zhengyang Su, Alicia Tsai, Yueqi Wang, Shao-Chuan Wang, et al.
2026. Plum: Adapting pre-trained language models for industrial-scale generative
recommendations. InProceedings of the ACM Web Conference 2026. 8093–8104.
[10] Xiangnan He, Lizi Liao, Hanwang Zhang, Liqiang Nie, Xia Hu, and Tat-Seng
Chua. 2017. Neural Collaborative Filtering. InProceedings of the 26th International
Conference on World Wide Web(Perth, Australia)(WWW ’17). International World
Wide Web Conferences Steering Committee, Republic and Canton of Geneva,
CHE, 173–182.
[11] Wang-Cheng Kang and Julian McAuley. 2018. Self-Attentive Sequential Rec-
ommendation. In2018 IEEE International Conference on Data Mining (ICDM).
197–206. doi:10.1109/ICDM.2018.00035
[12] Jiayu Li, Aixin Sun, Weizhi Ma, Peijie Sun, and Min Zhang. 2024. Right Tool,
Right Job: Recommendation for Repeat and Exploration Consumption in Food
Delivery. InProceedings of the 18th ACM Conference on Recommender Systems
(RecSys ’24). Association for Computing Machinery, New York, NY, USA, 643–653.
doi:10.1145/3640457.3688119
[13] Jan Malte Lichtenberg, Antonio De Candia, and Matteo Ruffini. 2025. DenseRec:
Revisiting Dense Content Embeddings for Sequential Transformer-based Recom-
mendation. InEARL Workshop at the 19th ACM Conference on Recommender Sys-
tems (RecSys ’25). https://earl-workshop.github.io/pdf/recsys2025-workshops_
paper_167.pdf
[14] Ilya Loshchilov and Frank Hutter. 2019. Decoupled Weight Decay Regularization.
In7th International Conference on Learning Representations (ICLR). New Orleans,
LA, USA. https://openreview.net/forum?id=Bkg6RiCqY7
[15] Rishabh Mehrotra and Benjamin Carterette. 2019. Recommendations in a mar-
ketplace. InProceedings of the 13th ACM Conference on Recommender Systems.
580–581.
[16] Zahra Nazari, Christophe Charbuillet, Johan Pages, Martin Laurent, Denis Char-
rier, Briana Vecchione, and Ben Carterette. 2020. Recommending podcasts for
cold-start users based on music listening and taste. InProceedings of the 43rd
International ACM SIGIR Conference on Research and Development in Information
Retrieval. 1041–1050.
[17] Nikil Pancha, Andrew Zhai, Jure Leskovec, and Charles Rosenberg. 2022. Pinner-
Former: Sequence Modeling for User Representation at Pinterest. InProceedings
of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining
(Washington DC, USA)(KDD ’22). Association for Computing Machinery, New
York, NY, USA, 3702–3712. doi:10.1145/3534678.3539156
[18] Gustavo Penha, Edoardo D’Amico, Marco De Nadai, Enrico Palumbo, Alexandre
Tamborrino, Ali Vardasbi, Max Lefarov, Shawn Lin, Timothy Heath, Francesco
Fabbri, et al. 2025. Semantic ids for joint generative search and recommendation.
InProceedings of the Nineteenth ACM Conference on Recommender Systems. 1296–
1301.
[19] Ethan Perez, Florian Strub, Harm de Vries, Vincent Dumoulin, and Aaron C.
Courville. 2018. FiLM: Visual Reasoning with a General Conditioning Layer. In
Proceedings of the Thirty-Second AAAI Conference on Artificial Intelligence (AAAI
’18). AAAI Press, 3942–3951. doi:10.1609/aaai.v32i1.11671
[20] Aleksandr Petrov and Craig Macdonald. 2022. A Systematic Review and Repli-
cability Study of BERT4Rec for Sequential Recommendation. InProceedings
of the 16th ACM Conference on Recommender Systems(Seattle, WA, USA)(Rec-
Sys ’22). Association for Computing Machinery, New York, NY, USA, 436–447.
doi:10.1145/3523227.3548487
[21] Aleksandr Vladimirovich Petrov and Craig Macdonald. 2023. gsasrec: Reducing
overconfidence in sequential recommendation trained with negative sampling.
InProceedings of the 17th ACM Conference on Recommender Systems. 116–128.
[22] Liudmila Prokhorenkova, Gleb Gusev, Aleksandr Vorobev, Anna Veronika Doro-
gush, and Andrey Gulin. 2018. CatBoost: unbiased boosting with categorical
features. InProceedings of the 32nd International Conference on Neural Information
Processing Systems(Montréal, Canada)(NIPS’18). Curran Associates Inc., Red
Hook, NY, USA, 6639–6649.
[23] Behnam Rahdari, Branislav Kveton, and Peter Brusilovsky. 2022. The Magic of
Carousels: Single vs. Multi-List Recommender Systems. InProceedings of the
33rd ACM Conference on Hypertext and Social Media(Barcelona, Spain)(HT ’22).
Association for Computing Machinery, New York, NY, USA. doi:10.1145/3511095.
3531278
[24] Shashank Rajput, Nikhil Mehta, Anima Singh, Raghunandan Hulikal Keshavan,
Trung Vu, Lukasz Heldt, Lichan Hong, Yi Tay, Vinh Tran, Jonah Samost, et al.
2023. Recommender systems with generative retrieval.Advances in Neural
Information Processing Systems36 (2023), 10299–10315.
[25] Meituan Research. 2025. User Long-Term Multi-Interest Retrieval Model for
Recommendation. InProceedings of the 19th ACM Conference on Recommender
Systems (RecSys ’25). ACM.
[26] Yi Su, Xiangyu Wang, Elaine Ya Le, Liang Liu, Yuening Li, Haokai Lu, Benjamin
Lipshitz, Sriraj Badam, Lukasz Heldt, Shuchao Bi, et al. 2024. Long-term value of
exploration: Measurements, findings and algorithms. InProceedings of the 17th
ACM International Conference on Web Search and Data Mining. 636–644.
[27] Fei Sun, Jun Liu, Jian Wu, Changhua Pei, Xiao Lin, Wenwu Ou, and Peng Jiang.
2019. BERT4Rec: Sequential Recommendation with Bidirectional Encoder Rep-
resentations from Transformer. InProceedings of the 28th ACM International
Conference on Information and Knowledge Management(Beijing, China)(CIKM
’19). Association for Computing Machinery, New York, NY, USA, 1441–1450.
doi:10.1145/3357384.3357895
[28] Viet-Anh Tran, Guillaume Salha-Galvan, Bruno Sguerra, and Romain Hennequin.
2024. Transformers Meet ACT-R: Repeat-Aware and Sequential Listening Session
Recommendation. InProceedings of the 18th ACM Conference on Recommender
Systems(Bari, Italy)(RecSys ’24). Association for Computing Machinery, New
York, NY, USA, 486–496. doi:10.1145/3640457.3688139
[29] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones,
Aidan N Gomez, Łukasz Kaiser, and Illia Polosukhin. 2017. Attention is all
you need.Advances in neural information processing systems30 (2017).
[30] Hai Wang, Lei Zhao, Kaile Yan, Xiaoyi Wang, Yile Liang, and Jinghua Hao.
2025. Meituan: Operational-Level On-Demand Food Delivery Data for the 2025
INFORMS TSL Data-Driven Research Challenge.A vailable at SSRN 5696423
(2025).
[31] Yuyan Wang, Mohit Sharma, Can Xu, Sriraj Badam, Qian Sun, Lee Richardson,
Lisa Chung, Ed H. Chi, and Minmin Chen. 2022. Surrogate for Long-Term User
Experience in Recommender Systems. InProceedings of the 28th ACM SIGKDD
Conference on Knowledge Discovery and Data Mining(Washington DC, USA)
(KDD ’22). Association for Computing Machinery, New York, NY, USA, 4100–4109.
doi:10.1145/3534678.3539073
[32] Ruibin Xiong, Yunchang Yang, Di He, Kai Zheng, Shuxin Zheng, Chen Xing,
Huishuai Zhang, Yanyan Lan, Liwei Wang, and Tieyan Liu. 2020. On Layer
Normalization in the Transformer Architecture. InProceedings of the 37th Inter-
national Conference on Machine Learning (ICML) (Proceedings of Machine Learning
Research, Vol. 119). PMLR, 10524–10533.
[33] Dawei Yin, Yuening Hu, Jiliang Tang, Tim Daly, Mianwei Zhou, Hua Ouyang,
Jianhui Chen, Changsung Kang, Hongbo Deng, Chikashi Nobata, Jean-Marc
Langlois, and Yi Chang. 2016. Ranking Relevance in Yahoo Search. InProceedings
of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and
Data Mining (KDD ’16). ACM, 323–332. doi:10.1145/2939672.2939677
[34] Yu Zhang et al. 2021. A Dual Augmented Two-tower Model for Online Large-
scale Recommendation. InProceedings of the 3rd Workshop on Deep Learning
Practice for High-Dimensional Sparse Data (DLP-KDD ’21).
[35] Yong Zheng. 2019. Multi-stakeholder recommendations: case studies, methods
and challenges. InProceedings of the 13th ACM Conference on Recommender
Systems. 578–579.

Marcel Kurovski, Attila Nagy, Steffen Klempau, and Aleksandr Fedintsev
A Trial vs. Reorder Trade-off
To isolate the ranker’s contribution to the trial vs. reorder trade-off,
we hold the classifier fixed and re-train only the ranker across 3
per-session weighting regimes𝑤 new/𝑤rec∈{ 1.5, 2.0, 3.0} (𝑤 rec=1;
the three clusters in Figure 3) and 50max_pairs negative-sampling
settings per regime (dot color). All 150 runs share the same country,
day, and random seed.
Axes report relative MRR uplift over the production baseline on
new(x) andrec(y) purchases. The clusters trace a Pareto-style
frontier:𝑤 new/𝑤rec=1.5yields strong reorder gains with a small
trial regression,2.0balances both at modest positive uplifts, and
3.0delivers a strong trial uplift at the cost of reorder. Within each
cluster, increasing max_pairs (low→ high) consistently shifts the
model results toward stronger reorder and weaker trial. Together
these two ranker-only levers enabled us to tune the trade-off be-
tween trial and reorder.
Figure 3: Ranker ablation: relative MRR uplift over produc-
tion onnew(x) vs.rec(y) with the classifier held fixed.
B MRR vs. Maximum Sequence Length
Figure 4 shows that reorder MRR rises sharply up to∼30 purchases
and then plateaus, while trial and cold-start MRR are largely insen-
sitive to sequence length. This motivates the moderate sequence
cap𝑀used in training (Section 4.4.1).
Figure 4: Classifier MRR on therec,cs, andnewvalidation
slices vs. the maximum input sequence length.
