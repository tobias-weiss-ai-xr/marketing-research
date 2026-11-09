---
title: 'Instapopacc: Popular Account Detection on Instagram Via Heterogeneous GNNs with Temporal RNN Modeling'
url: https://doi.org/10.22266/ijies2026.0531.04
category: analytics
subcategory: empirical
date: 2026-05
venue: International journal of intelligent engineering and systems
authors:
- F. Kareem
- Fatima B. Ibrahim
source: openalex-oa
pdf_url: https://doi.org/10.22266/ijies2026.0531.04
pages: 14
chars: 58225
fetched_at: '2026-11-08T17:28:58+00:00'
kb_version: 1
---

# Instapopacc: Popular Account Detection on Instagram Via Heterogeneous GNNs with Temporal RNN Modeling

Received:  January 21, 2026.     Revised: March 4, 2026.                                                                                                   52
International Journal of Intelligent Engineering and Systems, Vol.19, No.5, 2026           DOI: 10.22266/ijies2026.0531.04

This article is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
License details: https://creativecommons.org/licenses/by-sa/4.0/

Instapopacc: Popular Account Detection on Instagram Via Heterogeneous GNNs
with Temporal RNN Modeling

Faten Mohammed Kareem1*          Fatima Bahjat Ibrahim1

1 Department of Information and Communication Engineering, Al-Khwarizmi Engineering College,
University of Baghdad, Baghdad, Iraq
* Corresponding author’s Email: faten.kareem2203@kecbu.uobaghdad.edu.iq

Abstract: Accurately ranking influential or popular accounts in online social networks is critical for recommendation,
content promotion, and marketing analytics, yet most existing influence models either ignore temporal dynamics or
treat heterogeneous signals in is olation. This paper addresses the problem of popular account detection on Instagram
by jointly modelling heterogeneous interaction structure and month -wise engagement trajectories. We construct a
temporal heterogeneous graph over influencers, hashtags, and  user tags, and propose a two -stage architecture: (i) a
heterogeneous GNN (HGNN) that aggregates multi -type neighbours into monthly embeddings, followed by (ii) a
bidirectional STM that captures temporal dependencies, with a ranking head trained using pairwise and listwise losses.
On an Instagram influencer dataset comprising 13 monthly Timestamps with influencer -disjoint splits, our model
achieves NDCG@200 up to 0.881, RBP@200 up to 0.941, and AUC around 0.75. Ablation studies reveal a strong
interaction between encoder and supervision pattern: the HGNN+ BiGRU encoder performs best under dense process
supervision (PSRP + LambdaRank + Neural NDCG surrogate), whereas the HGNN -only encoder is better served by
PSRP supervision only. An experiments on the learned embeddings show that  the recurrent encoder (HGNN+BiGRU)
preserves equal or stronger linearly decodable history in its final state, while loss ablations show it benefits from PSRP
combined with LambdaRank and Neural NDCG, improving top -heavy ranking quality. These findings provide both
an effective architecture for popular account detection and empirical guidance on how to align supervision strategies
with temporal encoders in graph-based ranking systems.
Keywords: Deep learning, Pretrained graph embeddings, Heterogenous graph, Influencer-disjoint, Influencer ranking,
Social network analysis, Temporal node representation, Sequence modelling .

1. Introduction
Rapid advances in information technology (IT)
have made social networks central to global, real -
time communication, evolving them into broad
ecosystems for discussion, marketing, and sales[1].
Within Online Social Networks (OSNs), social
influence refers to an individual's capacity to alter the
opinions or behaviours of others in the network [2].
The extent of influence dissemination is largely
shaped by the structure of relationships among users,
where the strength of connections plays a critical
role[3]. In fact, research has shown that only a small
set of influential users can shape the opinions of large
groups in online communities[4]. Once a message is
forwarded, each recipient becomes a new  publisher,
rapidly amplifying the original users’ comments and
shaping public opinion[5]. Analysing these influence
dynamics helps explain why certain trends suddenly
surge or later fluctuates, enabling more efficient
advertising strategies. However, desp ite the role of
key influencers, the primary catalyst of rapid OSN
diffusion is still considered to be the presence of a
large pool of susceptible users who are ready to
receive and propagate the information[6].
A study investigated how highly popular users on
platforms such as Twitter (X) and Reddit can
indirectly encourage the disclosure of personally
identifiable information (PII) through visible, public
interactions. To quantify influence within discussion
groups, the authors built cluster -level social graphs,

Received:  January 21, 2026.     Revised: March 4, 2026.                                                                                                   53
International Journal of Intelligent Engineering and Systems, Vol.19, No.5, 2026           DOI: 10.22266/ijies2026.0531.04

This article is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
License details: https://creativecommons.org/licenses/by-sa/4.0/
where each node corresponds to a user and edges
indicate interactions occurring inside the same cluster.
They then used eigenvector centrality (implemented
with NetworkX) to assign an influence score to every
node, and identified the most influential user in each
subgraph by selecting the top-ranked node.
Although the work uses time -varying signals—
including resampled, timestamped engagement
traces and ARIMA forecasting —it doesn’t imply a
temporal graph learning approach. As a result, the
influence estimation remains largely dependent on
static, centrality -driven heuristics, rather than a
learned framework that models evolving graph
structure and user influence over time [7].
Likewise, another authors proposed a graph -
oriented approach to study Instagram influencers,
leveraging Node2Vec and Word2Vec embeddings on
the Top 200 Instagram Influencers dataset. They
modelled the system as a network where influencers
are nodes and edg es encode interactions between
them. Influential accounts were then determined
using standard centrality measures (e.g., degree and
betweenness centrality) to highlight the most
prominent users in the graph. The work limitation is
modelling the network as a static, homogeneous
graph, without explicitly capturing temporal
dynamics or distinguishing between different
edge/relationship types. It also relies on unsupervised
similarity-based signals rather than incorporating
supervised ranking objectives to guid e the ordering
of users or interactions [8].
Another work studied influencer selection for
social-media marketing and proposed GNN -IR, a
graph neural network recommender that captures
relationships between companies and YouTube
creators. However, the approach models the
underlying network as static, without explicitly
learning temporal dynamics [9].
The authors introduced a Tree Hierarchical Deep
Convolutional Neural Network (TH -DCNN) paired
with cosine similarity for influencer ranking on social
media. Using an Indian political Twitter dataset, they
built a heterogeneous graph that includes influencers,
users, mentions, and hashtags. TH -DCNN analyzes
the graph at each time period to capture evolving
influence patterns, and ranking is obtained by
comparing temporal vectors via cosine similarity.
A key limitation is the heavy reliance on cosine
similarity, which restricts the model’s ability to learn
more flexible, rank -optimized scoring functions.
Additionally, although the architecture supports node
heterogeneity, it lacks edge -type awareness,
effectively treating all relations the same and not
differentiating between interaction types [10].
Overall, prior work leaves gaps: many methods
still rely on static or homogeneous graphs, treat time
descriptively instead of learning temporal graph
dynamics, and model influence via unsupervised
scores or binary classification rather than ranking -
optimized learning. These limitations motivate
learning temporal influencer representations on fully
heterogeneous graphs with rank -aware supervision.
However, because social media is large -scale, deep
learning typically requires massive datasets, creating
practical challenges in storage, compute, and the
time-consuming preprocessing and analysis pipeline.
For text classification , unsupervised machine
learning (ML) methods[11], supervised ML, deep
learning (DL), or hybrid approaches can be employed.
DL has demonstrated a strong capability for
multimodal inputs [12 , 13]. Moreover, modular
pipelines, such as K -Gen, achieve improved
performance via staged processing [14]. This line of
research indicates that, once influence signals and
user–content interaction features are extracted,
modern ML/DL models can process them effectively
Still, online influence shapes discovery, engagement,
and downstream behaviours on social platforms; yet
most computational studies either (i) analyse static
representations with centrality/heuristics or (ii) study
correlations (e.g. influence vs. engagement) without
learning to rank who will matter this month. Such
designs fail to capture temporal drift, cross -type
interactions (influencer–hashtag–audience tags), and
the requirement to use ranking objectives and metrics
that match the task. In line with recent studies
showing that graph -based and semi -supervised
approaches as especially promising for handling
large-scale social media misuse [15], our work
extends this direction by modelling the platform as a
temporal heterogeneous graph to capture richer,
relation-aware influencer signals. A monthly
influencer ranking on Instagram is studied: given
heterogeneous, time -stamped interaction graphs, a
score for each influencer at month is predicted so that
the induced order optimizes ranking utility.
Our Contributions are a scalable pipeline for
temporal, heterogeneous influencer ranking, an
empirical analysis of supervision granularity
showing that per -step objectives benefit temporally
enriched encoders, whereas last-step is preferable for
GNN-only encoder, a comprehensive comparison of
ranking losses on real monthly graphs, and a
reproducible evaluation criterion aligned to ranking
metrics.
This paper is organized as follows: section 2,
presents the theoretical foundation of each
component in the system. Section 3 describes the
preparing of the dataset used in the work. Section 4

Received:  January 21, 2026.     Revised: March 4, 2026.                                                                                                   54
International Journal of Intelligent Engineering and Systems, Vol.19, No.5, 2026           DOI: 10.22266/ijies2026.0531.04

This article is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
License details: https://creativecommons.org/licenses/by-sa/4.0/

Figure. 1 The Proposed Framework. ℎ𝑖 (𝑠)is the representation for each influencer set (train, validation, and test) that spans
all available month and 𝑆𝑖 is the score for each influencer

describes the implementation of the proposed system,
including the heterogeneous GNN -based backbone
and the temporal ranking model.  Section 5 presents
the experimental setup and evaluation results. Finally,
Section 6 concludes the paper and outlines directions
for future research.
2. Theory
In the past few years, deep learning has
demonstrated strong effectiveness in modelling
complex, high-dimensional signals that evolve over
time. Within influencer detection and ranking, such
models can automatically learn latent behavioral
patterns and mul ti-relational structures from large
and dynamic social graphs. This study adopts a two-
stage framework tailored to monthly influencer
rankings. First, heterogeneous graph neural networks
(HGNNs) encode the rich schema of social platforms,
spanning multiple node and edge types, and project
them into a shared representation space.
To robustly capture the platform structure before
any temporal modelling, we began with a a
HeteroConv. It is a heterogeneous spatial encoder
that aggregates information across the multi -
relational social graph within each month [16].
HeteroConv backbone was adopted and
populated with relation -specific GraphSAGE
operators. Each edge type (e.g., user→influencer
interactions, influencer↔hashtag usage) is assigned
its own SAGEConv that (i) linearly projects
source/target node types into a shared latent space,
(ii) performs neighbourhood . aggregation with
degree-aware normalization, and (iii) applies type -
specific affine transforms. HeteroConv fusion then
combines the relation outputs (mean), followed by
residual connections and dropout.
 In the second stage, a temporal sequence encoder,
Long Short-Term Memory (LSTM), is applied over
the month-wise embeddings to capture the directional
dynamics. Each LSTM unit maintains a cell state and
employs three gating mechanisms —forget, input,
and ou tput—that modulate the information flow
across successive time steps. This gating control
mitigates vanishing gradients and enables the model
to preserve and exploit long -range dependencies,
including those prevalent in textual sequences[17].
After the BiLSTM layer, a multi -head self-attention
layer is added to refines long -range temporal
dependencies and emphasizes salient time steps.
Attention mechanisms have become central to high -
performance sequence modelling and transduction
systems across diverse tas ks, enabling the model to
capture dependencies regardless of the distance
between elements within the input or output
sequences[18].
Together, these components capture both the
structural semantics and temporal evolution of
influencer behaviour, yielding a more accurate and

Received:  January 21, 2026.     Revised: March 4, 2026.                                                                                                   55
International Journal of Intelligent Engineering and Systems, Vol.19, No.5, 2026           DOI: 10.22266/ijies2026.0531.04

This article is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
License details: https://creativecommons.org/licenses/by-sa/4.0/
robust monthly ranking. The tow -stages are
illustrated in Fig. 1.
While the temporal head (BiLSTM with
attention) models how influence evolves across
months, our learning signal is driven primarily by
ranking-aware objectives defined within each month.
Within-month ordering is optimized using
complementary loss families that emphasize different
facets of ranking quality.
One such family is the RankNet Pairwise logistic
loss, RankNet developed by [19] is a pairwise method.
RankNet optimizes its parameters using a cross -
entropy objective function during training. Initially,
it was presumed that each object pair in the traini ng
dataset was linked to an associated probability.
Second, the framework assumes that a probability is
computed for every pair of objects, given the ranking
function. RankNet utilizes the backpropagation
algorithm, also known as Stochastic Gradient
Descent, to optimize the network parameters during
training[20]. For a given pair (𝑥𝑖 (1)), 𝑥𝑖 (2))), RankNet
first maps each item to a scalar score using the
ranking network as shown in Eq. (1).

𝑠𝑖 (1) = 𝑓(𝑥𝑖 (1)),  𝑠𝑖 (2) = 𝑓(𝑥𝑖 (2))                        (1)

and define the score difference as Eq. (2):

𝑠𝑖 = 𝑠𝑖 (1) − 𝑠𝑖 (2)                                                 (2)

The probability that 𝑥𝑖 (1) is ranked higher than
𝑥𝑖 (2) is defined using the logistic function in Eq. (3):

𝑃𝑖 ≡
exp (𝑠𝑖)
1+exp (𝑠𝑖)                         (3)

This implies that if 𝑓(𝑥𝑖 (1)) > 𝑓(𝑥𝑖 (2)) , then
𝑥𝑖 (1)is more likely to be ranked ahead of 𝑥𝑖 (2)with
probability 𝑃𝑖.
To quantify the error in predicting this pairwise
ranking, the Cross Entropy loss was used, which
evaluates the discrepancy between the predicted
probability 𝑃𝑖and the ground -truth label 𝑃ˉ𝑖 ∈ {0,1}.
The loss is defined as Eq. (4) [21]:

𝐿𝑖 =  −𝑃ˉ𝑖 log 𝑝𝑖 − (1 − 𝑃ˉ𝑖) log(1 −  𝑃𝑖)
𝐿𝑖= − P 𝑖log𝑝𝑖−1−P 𝑖log1− 𝑃𝑖              (4)

Substituting Eq. (3) into Eq. (4), the simplified
form of the loss is in Eq. (5):

𝐿𝑖 = −𝑃ˉ𝑖𝑠𝑖 + log (1 + exp (𝑠𝑖))                      (5)

In the special case where 𝑃ˉ𝑖 = 1 (i.e., the first
item should be ranked higher), the Cross Entropy loss
reduces to the logistic loss as shown in Eq. (6):

𝐿𝑖 = log (1 + exp (−𝑠𝑖))                                 (6)

Take the uses of Neural Network, Cross Entropy
loss, back-propagation, and Cross Validation as the
major characteristics of the RankNet method[22].
The Second family is Lambda Rank, the ranking
evaluation metric—used as the learning objective —
is typically neither continuous nor differentiable, as
it depends on a sorting operation. (Moreover, the
sorting function itself lacks continuity and
differentiability.). LambdaRank, introduced by[23 ,
24], adopts Gradient Descent to optimize the
evaluation metric and seeks to directly specify and
exploit the gradient of that metric. LambdaRank does
not provide an explicit loss function. Instead, it
specifies the g radient of the surrogate loss. In
particular, the gradient is defined by[19] using Eq. (7).

∂𝐿
∂𝑠𝑗
  =   −  𝜆𝑗(𝑠1, 𝑦1, … , 𝑠𝑛, 𝑦𝑛)                        (7)

where 𝑠1, 𝑠2, ···, 𝑠𝑛 denote the scores and 𝑦1, 𝑦2,
···, 𝑦𝑛  denote the labels. In implementing
LambdaRank, it suffices to design a procedure for
computing the Lambda values (i.e., the gradients of
the surrogate loss). A common choice is to base these
on NDCG, yielding Eq. (8)

𝜆𝑗  =
∂𝐿
∂𝑠𝑗
  =
1
𝐺max
∑
1
1+exp (𝑠𝑖−𝑠𝑗)  (𝑔𝑖 − 𝑔𝑗) (𝐷𝑖 − 𝐷𝑗)
𝑖≠𝑗
 (8)

where 𝑔𝑖, 𝐷𝑖, and 𝑠𝑖, respectively, denote the gain,
discount, and score. 𝐺𝑚𝑎𝑥−1  denotes the normalizing
factor of NDCG. Its training procedure mirrors the
(fast) RankNet algorithm, but adopts a different loss
function.
Another loss is the mean absolute error (MAE) or
L1 loss, is a fundamental regression criterion that
computes the average magnitude of prediction errors
without considering their direction [23]. MAE is also
employed as an evaluation metric for model
performance. Its mathematical definition is given in
Eq. (9)[24]:

MAE =
1
𝑛 ∑ ∣ 𝑦𝑖 − 𝑠𝑖 ∣𝑛 𝑖=1       (9)

Where 𝑦𝑖 the true (ground -truth) value for the 𝑖-
th observation and 𝑠𝑖 the model’s predicted value for

Received:  January 21, 2026.     Revised: March 4, 2026.                                                                                                   56
International Journal of Intelligent Engineering and Systems, Vol.19, No.5, 2026           DOI: 10.22266/ijies2026.0531.04

This article is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
License details: https://creativecommons.org/licenses/by-sa/4.0/
the 𝑖 -th observation. Because the penalty grows
linearly with the error magnitude, small and large
errors are weighted equally, making the metric less
sensitive to outliers.
Another loss is scalable optimal -transport-based
differentiable Top-K (SOFT Top-K), The goal of top-
𝑘  learning is to maximize the likelihood that the
model 𝑓Θproduces an accepted prediction on samples
(𝑋, 𝑦) ∼ 𝒟, given a marginal distribution 𝑃𝐾 (or a
conditional 𝑃𝐾∣𝑋,𝑦when it depends on the label and/or
input). Let 𝑃𝑘,𝑦 denote the model’s predicted
probability that 𝑦 is the 𝑘-th best prediction for input
𝑋. The objective is shown in Eqs. (3) and (10) [25].

arg max
Θ
  𝔼(𝑋,𝑦)∼𝒟
[log  (𝔼𝑘∼𝑃𝐾[∑ 𝑃𝑚,𝑦
𝑘
𝑚=1
])]  (10)

𝑃𝑘,𝑦  is the predicted probability of 𝑦  marginal
distribution 𝑃𝑘 . Let 𝑃 ∈ ℝ𝑛×∣𝒞∣ provide rank -wise
class probabilities, where 𝑃𝑘,𝑐denotes the probability
that class 𝑐  is the 𝑘 -th prediction. Each row is
required to be stochastic, ∑ 𝑃𝑘,𝑐𝑐∈𝒞 = 1, and ideally
also column-stochastic, ∑ 𝑃𝑘,𝑐
𝑛
𝑘=1 = 1, so that 𝑃 is
doubly stochastic. With these scores, train done  by
minimizing Eq. (11) [25]

𝐿(𝑋, 𝑦)  =
  − log (∑ 𝑃𝐾(𝑘)𝑛 𝑘=1 (  ∑ 𝑃𝑚,𝑦
𝑘
𝑚=1
 (𝑓Θ(𝑋)))  (11)

The last loss is a learned NDCG surrogate that
obtain a differentiable objective that directly
encourages high NDCG@𝐾on each month -slate. For
a month 𝑚, let s(𝑚) ∈ ℝ𝑛 be the predicted scores and
y(𝑚) ∈ ℝ𝑛the graded relevance labels (shifted to be
non-negative). We pretrain a permutation -invariant
DeepSets model 𝑔𝜃 to regress the true metric as in
Eqs. (12) and (13) [26]:

𝑔𝜃(s(𝑚), y(𝑚)) ≈ NDCG@𝐾(s(𝑚), y(𝑚))      (12)

𝑔𝜃(𝑠, 𝑦 = 𝜎 (𝜌𝜃(∑ 𝜙𝜃 𝑛 𝑖=1 ([𝑠𝑖, 𝑦𝑖])))             (13)

Where:
• 𝜃: all trainable parameters (weights) of the
surrogate model.
• si: model score
• yi: label
• ϕθ(⋅): item encoder MLP. It maps each item
feature vector into a hidden representation:
• ρθ(⋅): global encoder/head MLP that maps
the pooled vector to one scalar.
• σ(⋅): the sigmoid function.
𝑔𝜃 is frozen and used as an auxiliary term by
maximizing the predicted NDCG via Eq. (14)

𝐿sur (𝑚) = − 𝑔𝜃(s(𝑚), y(𝑚))                                (14)

This yields a smooth proxy that rewards month -
wise rankings with higher NDCG@𝐾.
3. Proposed data preparing
This study utilizes the Instagram Influencer
Dataset [25], which was curated to analyse influencer
behaviour and interaction dynamics on the platform.
The dataset comprises user -level metadata and
content-based attributes derived from influencer
profiles a nd their posts. To model temporal
heterogeneity, only posts published between January
1, 2017, and January 31, 2018, were included. This
13-month window enables the construction of
monthly dynamic time slices that capture the
temporal evolution of the cont ent and user
interactions.
The dataset encompasses 21,923 unique
influencer accounts, each annotated with one of nine
predefined categories: beauty, family, fashion, fitness,
food, interior, pets, travel, and other. The total,
dataset contained 2,067,235 posts, each enriched
with me tadata such as captions, timestamps,
sentiment scores, and user engagement metrics (e.g.,
likes, hashtags, and user mentions).
In addition to user nodes, the dataset includes two
auxiliary node types:
• Hashtag nodes: 1,019,749 unique hashtags
extracted from influencer posts.
• User tag nodes: 607,279 distinct usernames
tagged by the influencers.
All node types are temporally replicated across
each month to generate a dynamic heterogeneous
graph, with each node representing the interactions
within a specific month. The dataset contains
approximately 5.6 million unique edges, capturing
the complex r elationships between influencers,
hashtags, and tagged users over time.
For experimental evaluation, the dataset was
partitioned at the user (influencer) level into three
mutually exclusive subsets: 70 % (15346) of the
influencers were allocated to the training set, 20%
(4385) to the testing set, and the remaining 10%
(2192) to the validation set used for hyperparameter
tuning. This stratified partitioning ensured that posts
associated with each influencer appeared in only one
subset, thereby preventing data leakage.

Received:  January 21, 2026.     Revised: March 4, 2026.                                                                                                   57
International Journal of Intelligent Engineering and Systems, Vol.19, No.5, 2026           DOI: 10.22266/ijies2026.0531.04

This article is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
License details: https://creativecommons.org/licenses/by-sa/4.0/
The same partitioning protocol was uniformly
applied to both the HGNN encoder and BiLSTM
downstream classification module, to ensure
consistency in training, validation, and evaluation
across all components of the proposed framework.
To support temporal graph -based learning, a
comprehensive data preprocessing pipeline tailored
for heterogeneous influencer data derived from
Instagram was implemented. The process began by
parsing files, each representing an individual post, to
count the number of posts per influencer and extract
monthly interaction patterns. Influencer metadata —
such as follower counts, followee counts, total post
activity, and categorical labels.
Post-level features were extracted by processing
the corresponding post files, capturing both content -
level (e.g., caption length, hashtags, emojis, and
sentiment scores) and engagement -level attributes
(likes, comments, and feedback activity). These
features were aggregated monthly, allowing the
calculation of time -dependent metrics, such as the
average caption sentiment, advertising ratio,
engagement rate, and posting intervals.
In parallel, monthly statistics for hashtags and
user mentions were independently extracted and
aggregated for analysis. All node types (influencers,
hashtags, and user tags) were then temporally aligned
and serialized, producing a time -resolved node
feature matrix.
Subsequently, monthly heterogeneous graphs
were created. For each month, a separate HeteroData
object was built to encode directed interactions:
(influencer → hashtag), (influencer → user_tag), and
their reverse counterparts.
Finally, node feature matrices for each timestamp
were created, ensuring consistent dimensionality and
the presence of padded zero vectors for inactive
nodes. The resulting temporally heterogeneous graph
and feature tensors were saved for downstream GNN
training.
4. Implementation
Two scenarios were implemented and evaluated
for influencer ranking: (1) InstaPopAcc (our model),
designed for month -resolved heterogeneous graphs
and optimized as a learning-to-rank pipeline, and (2)
an adopted model (HetEmbedRank) from [28],
integrated w ithout modification. Both scenarios
consume the same processed data and feature set, are
trained and evaluated with identical pipelines, fixed
seeds, and the same hyperparameter budget, and are
assessed using ranking metrics (e.g., NDCG@K).
Critically, we enforce influencer-disjoint (user-level)
splits—training, validation, and test partitions share
no influencer identities —to prevent leakage and
ensure fair generalization across months, whereas the
adopted work applied their model using a
chronological split.
For the first scenario (our model), at each month
𝑚, given each influencer’s multi -relational activity
history up to and including 𝑚 , a score 𝑠𝑖,𝑚  is
produced, and
 influencers are ranked within the month.
Supervision comes from an engagement-rate-derived
relevance signal aggregated per influencer and month.
Training and testing are influencer -disjoint:
70/20/10% split of influencers, with each set
spanning all available months. The engagement rate
𝑦𝑖,𝑡 is calculated as in Eq. (15):

𝑦𝑖,𝑡 =
∑ 𝑙(𝑝) 𝑁𝑖,𝑡⁄ 𝑁𝑖,𝑡 𝑝=1
𝑓𝑖
                                          (15)

Where 𝑦𝑖,𝑡is the engagement rate for influencer 𝑖
at time 𝑡, ∑ 𝑙(𝑝) 𝑁𝑖,𝑡 ⁄ 𝑁𝑖,𝑡 𝑝=1 is the average number of
likes 𝑙  per post  𝑝  on the posts published by
influencer 𝑖 at time stamp 𝑡 and 𝑓𝑖 is the number of
followers of i.
Then monthly sequence of heterogeneous graphs
{𝒢𝑡}𝑡=1 𝑇  Are observed. Each 𝒢𝑡 = (𝒱𝑡, ℰ𝑡) contains
three node types as in Eq. (16):

𝒱 = 𝒱inf ∪  𝒱hash ∪  𝒱utag                            (16)

and four directed relation types ℰ𝑡 :
(inf  →  hash): uses
(hash  →  inf): used_by
(inf  →  utag): tags
(utag  →  inf): tagged_by
For node type 𝒱 ∈ {inf,hash,utag} , let X𝑡 (𝒱) ∈
ℝ𝑁𝑡 (𝒱)×𝑑in (𝒱) denote the input features at month 𝑡 and
ℰ𝑡 (𝑟)the edge index matrix for relation 𝑟. Influencer
node IDs are partitioned into mutually exclusive sets
𝐼𝑡𝑟𝑎𝑖𝑛, 𝐼𝑣𝑎𝑙, 𝐼𝑡𝑒𝑠𝑡 . For each month 𝑚 , the full
heterogeneous snapshot 𝐺𝑚 is loaded. For each split
𝑠 and month 𝑚, an induced split-specific graph 𝐺𝑚𝑠  is
constructed by retaining only influencer nodes in 𝐼𝑠,
removing all edges incident to removed influencers
(for both influencer→non -influencer and non -
influencer→influencer directions), and reindexing
remaining influencers to contiguous IDs . After
filtering, hashtag and user tag features are
recomputed using only the retained split edges to
prevent leakage: each non-influencer node receives a
frequency feature aggregated over incoming edges
from retained influencers.  The non-influencer nodes

Received:  January 21, 2026.     Revised: March 4, 2026.                                                                                                   58
International Journal of Intelligent Engineering and Systems, Vol.19, No.5, 2026           DOI: 10.22266/ijies2026.0531.04

This article is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
License details: https://creativecommons.org/licenses/by-sa/4.0/

Figure. 2 The first stage (HGNN) backbone layers

with no edges connected to them are removed from
the set and all relations are reindexed. Under this
construction, training graphs contain no
validation/test influencer nodes or incident edges,
and non-influencer statistics are computed per split -
month, pr eventing cross -split information leakage
through shared hashtag/user_tag nodes. The graph
construction is illustrated in algorithm 1.
Standard message -passing GNNs (MP -GNNs)
are not directly applicable to heterogeneous graphs
because node and edge features from different
categories cannot be handled uniformly owing to
their different types. A practical approach is to define
the message a nd update functions per edge type. In
practice, the MP -GNN iterates over the edge -type
dictionaries for message computation and node -type
dictionaries for state updates. Therefore, we
employed a Heterogeneous Graph Convolution
(HeteroConv) wrapper to run c onvolutions on
heterogeneous structures: it routes messages from
source to target nodes via a bipartite GNN layer
specific to each relation, and then aggregates the
results when multiple relations share a target.
Accordingly, we used relation-
specific SAGEConv layers for every edge type.
The graph includes multiple node categories —
influencers, hashtags,
and user tags —each with its own feature
dimensionality and statistical profile as shown in Eq.
(17).

𝑥𝑖 (1) =
𝜎 ( ∑ 𝑊𝑟𝑟 𝜖 𝑅  ∙  [𝑥𝑖 (0) ∥ 𝑀𝐸𝐴𝑁𝑗 ∈ 𝒩𝑟(𝑖) 𝑥𝑗 (0)]) (17)

Where:
R set of all relation types (edge types) in the
heterogeneous graph.
𝒩r(i) neighbours of node i under relation r.
MEAN j ∈𝒩r(i) Xj(0) Aggregated feature vector from
neighbours connected by edge type r. Xi(1) Updated
node embedding for node i after one message passing
layer.
Wi Learnable weight matrix specific to relation r.
σ activation function (ReLU is used here) applied
after the weighted sum.
To unify all nodes in a single embedding space,
each node type is first passed through linear
projection. These type -specific transforms map
features to a common embedding dimension,
enabling meaningful cross -type comparisons and
aggregation. A ReLU activa tion and dropout
areapplied after the projection as in Eq. (18). The
HGNN stage’s layers are illustrated in Fig. 2.

Z𝑡 (𝑎) = σ(Wτ 𝑥𝑖 𝑡 ) ∈ ℝ𝑁𝑡 (𝑎)×𝑑                         (18)

Z𝑡 (𝑎)are the hidden representations produced after
the linear projection layer, and W τ denotes the weight
matrix for the linear projection applied to nodes of
type τ. To handle missing data, a node -level signal
mask is set to 1 when features exist or the monthly
degree is non-zero; otherwise, it is set to 0. Only the
signalled nodes are L2-normalized, and the no-signal
nodes receive zero embeddings. Edgeless relations
contribute no reconstruction loss, eliminating false
gradients during inactive months. Together, these
choices ensure stability under sparse activity and
suppress artifacts for missing nodes.

Received:  January 21, 2026.     Revised: March 4, 2026.                                                                                                   59
International Journal of Intelligent Engineering and Systems, Vol.19, No.5, 2026           DOI: 10.22266/ijies2026.0531.04

This article is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
License details: https://creativecommons.org/licenses/by-sa/4.0/

Figure. 3 The downstream ranker layers

For the training objective, a hypered loss function
was used. First is the edge reconstruction loss. For
every relation 𝑟: source →  d estination month 𝑡 ,
embeddings were unit -normalized and edges were
scored with temperature -scaled dot products as
shown in Eqs. (19) and (20):
z̃(src) =
Z𝑡 (src)
∥Z𝑡 (src)∥2 , z̃(dst) = Z𝑡 (dst) ∥Z𝑡 (dst)∥2                       (19)

𝑠(𝑟)(𝑢, 𝑣) =
𝜏 z̃𝑢 (src) ⋅ z̃𝑣 (dst)                                                   (20)

Algorithm 1: Graph construction
Input: monthly graphs {Gm}      m=1..T
influencer IDs I → (Train IDs, Validation IDs, Test IDs)

Output: 𝒢 train,  𝒢 validation,  𝒢 test
Load {Gm}
Split influencer IDs → Train IDs, Validation IDs, Test IDs
Set 𝒢 train ← ∅ , 𝒢 validation ← ∅ , 𝒢 test ← ∅
FOR each split s ∈ {train, validation, test} do
│ Allowed ← Is
│ FOR each month m = 1..T do
│ │ G ← Load(Gm)
│ │ KeepInf ← {u ∈ Vinf : u ∈ Allowed} ; oldtonewInf ← Reindex(KeepInf)
│ │ Remove all edges with influencer endpoint ∉ KeepInf ; reindex influencer endpoints by  oldtonewInf
│ │ Update non-influencer frequency: for each removed (inf→x) edge with weight w: frequency[x]
│ │ Remove isolated hashtag/user_tag nodes (degree=0) ; oldtonewNon ← Reindex(kept nodes)
│ │ Reindex all remaining non-influencer endpoints by oldtonewNon
│ │ Append G to 𝒢s
│ END FOR
END FOR
Return 𝒢 train, 𝒢 validation, 𝒢 test

Where:
𝑍𝑡 (dst) : embeddings for source and destination
node types at time t
𝑧̃(src) , 𝑧̃(dst)L2 row-normalized embeddings
 𝑠(𝑟)(𝑢, 𝑣) a scaled cosine similarity between
node 𝑢(source type) and node 𝑣(destination type) for
relation 𝑟.
𝜏 > 0is a temperature/scale

Received:  January 21, 2026.     Revised: March 4, 2026.                                                                                                   60
International Journal of Intelligent Engineering and Systems, Vol.19, No.5, 2026           DOI: 10.22266/ijies2026.0531.04

This article is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
License details: https://creativecommons.org/licenses/by-sa/4.0/
with negatives sampled uniformly over the
endpoints to match the positive count. The relation -
wise loss is binary cross -entropy over positives and
sampled negatives; the across relations that present in
the timestamps were averaged.
In addition to the edge reconstruction loss, a
temporal loss is applied in which it discourages large
changes in embeddings across successive time steps,
and L2 regularization on the output embeddings is
included to prevent value explosion. The total loss
was calculated using Eq. (21).

ℒ =
1
𝑇 ∑ ℒrecon(𝑡)
𝑇
𝑡=1 + 𝜆smℒsmooth + 𝜆ℓ2ℒℓ2  (21)

with 𝜆sm = 0.1and 𝜆ℓ2 = 10−4.
To capture temporal dependencies in the
influence, let {z𝑖,𝑡 ∈ ℝ𝑑}denote the decoupled per -
influencer embeddings exported from the HGNN for
influencer 𝑖  at month 𝑡 . For each split 𝑠 ∈
{train,val,test}, sequences are assembled in Eq. (22).

h𝑖 (𝑠) = [z𝑖,𝑡1, … , z𝑖,𝑡𝐿𝑖 ] ∈ ℝ𝐿𝑖×𝑑                       (22)

The pre -trained node embeddings h𝑖 (𝑠) for each
month were extracted and saved. These embeddings
are then L2 normalized and fed to a separate BiLSTM
tailored for the influencer ranking task.
Train/validation/test follows the same protocol as
the HGNN stage in which it is influencer -disjoint
(70/20/10%), and each split spans all available
months.
The BiLSTM is followed by a multi -head self-
attention module that extracts contextual features and
emphasizes salient temporal intervals. The attention
output, that is, a temporally weighted representation
of each influencer’s activity—is then passed through
a two-layer feed-forward
network with ReLU activations to estimate the
predicted engagement at time 𝑡, 𝑠̂𝑖,𝑡, as illustrated in
Eq. (23). The downstream ranker’s layers are
illustrated in Fig. 3.

𝑠̂𝑖,𝑡 = 𝑊2 ∙ 𝜎(𝑊1 ∙ 𝑂𝑡)                                (23)

Where:
𝑂𝑡 output of the BiLSTM for timestep t
𝑊1  weight matrix for the first fully connected
layer 𝑊2 Weight matrix for final prediction layer
The model predicts per -step scores 𝑠̂𝑖,𝑡 for all
valid 𝑡.
For the training objectives, we evaluated several
loss functions (listed in Section 2). The PSRP loss
achieved the best results. For any calendar month 𝑚,
let ℐ𝑚 = {(𝑖, 𝑡): 𝜏𝑖,𝑡 = 𝑚}be all valid influencer–time
pairs in month 𝑚 . For each (𝑖, 𝑡) ∈ ℐ𝑚  there is a
model score 𝑠𝑖,𝑡and supervision 𝑦𝑖,𝑡(rank-normalized
engagement). The loss within month 𝑚 is defined in
Eq. (24).

ℒPSRP(𝑚) =
𝔼(𝑖,𝑡),(𝑗,𝑢)∈ℐ𝑚:  𝑦𝑗,𝑢>𝑦𝑖,𝑡     log   (
1 +
exp [−
𝑠𝑗,𝑢−𝑠𝑖,𝑡
𝜏 ]) ⋅
𝑤(𝑖,𝑡),(𝑗,𝑢)       (24)

with temperature 𝜏 > 0 and gap weighting
𝑤(𝑖,𝑡),(𝑗,𝑢)   =    ∣  𝑦𝑗,𝑢 − 𝑦𝑖,𝑡  ∣.
where:
𝑚 : the group/context to ranking within.
ℐ𝑚 : the index set of all candidate items that
belong to group 𝑚.
(𝑖, 𝑡), (𝑗, 𝑢): two elements from ℐ𝑚.
𝑦𝑖,𝑡, 𝑦𝑗,𝑢: ground-truth for those elements.
𝑠𝑖,𝑡, 𝑠𝑗,𝑢: model scores (logits) produced for those
elements.

Table 1. Comparison table between losses for both HGNN only encoder and HGNN + BiGRU encoder for embeddings
generating
Loss function/Metric/encoder
NDCG@200 RBP@200 AUC
HGNN +
BiGRU HGNN HGNN HGNN + BiGRU HGNN HGNN + BiGRU
PSRP + LambdaRank 0.8732 0.880 0.942 0.922 0.765 0.7585
PSRP 0.87460 0.881 0.941 0.918 0.763 0.740
PSRP + LambdaRank + Neural NDCG
surrogate 0.8746 0.880 0.941 0.926 0.7776 0.753
LSRP + Lambdarank 0.86378 0.869 0.923 0.914 0.765 0.725
Last-step hybrid (pointwise L1 + LSRP)
+ Lambdarank 0.865 0.866 0.919 0.908 0.7213 0.7112
LSRP 0.8640 0.868 0.928 0.916 0.761 0.728

Received:  January 21, 2026.     Revised: March 4, 2026.                                                                                                   61
International Journal of Intelligent Engineering and Systems, Vol.19, No.5, 2026           DOI: 10.22266/ijies2026.0531.04

This article is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
License details: https://creativecommons.org/licenses/by-sa/4.0/
Table 2. Statistical analysis on both pretrained encoders embeddings
Probe / Metric GNN-only HGNN+BiGRU
Month-ID accuracy (Val / Test) 0.1194 / 0.1201 0.1229/ 0.1207
Linear dynamics R² (zₜ → zₜ₊₁) Val: ~0.2972→ 0.67 across months; Test: ~0.81 → 0.67 Val: ~0.78 → 0.58; Test: ~0.79 → 0.59
Linear dynamics cosine (with learned
W) 0.9079 (Val), 0.9067 (Test) 0.9101 (Val), 0.9096 (Test)
Autocorrelation (lag=1) (cosine) 0.9055 (Val), 0.9042 (Test) Val0.9080, Test: =0.9075
Order-direction accuracy (Val) mean=0.8191 |median=0.8590 mean=0.8532 | median=0.9103
Order-direction accuracy (Test) mean=0.8538 | median=0.9103 mean=0.8642 | median=0.9359
History compression – global R² (last z
→ all months’ labels) 0.0533 0.0597
History compression – per-month
Pearson correlation 0.177–0.297 (avg ≈ 0.24) 0.3118 → 0.2259
Local vs outcome R²
local=-0.7495 , 0.2010, -0.0013,
0.0070.
outcome=-0.0662, 0.4645
, -0.0324, -0.0070 , -0.0217
local = -0.1843,  0.0315, -0.0312,
0.0141, 0.0336.
R²_outcome = -1.5576, -0.1661, -
0.4099, 0.0336
Temporal smoothness – mean L2 step
size 0.0827 0.0837
Temporal smoothness – mean cosine 0.6130 0.6129

Table 3. Spatial encoder comparison
Spatial Encoder NDCG@200 RBP@200 AUC
SAGEconv 0.881 0.9433 0.7776
GAT2vec 0.7353 0.7644 0.6434
Graphconv 0.797 0.828 0.689

𝜏 > 0 : temperature (scale) on the score
differences.
Target gap: 𝑤 =∣ 𝑦𝑗,𝑢 − 𝑦𝑖,𝑡 ∣
𝔼(⋅)[⋅]: expectation over ordered pairs in ℐ𝑚.
The gap weighting (w) is used and for 𝜏  and k,
1.0 and 10,000 are chosen respectively.
Intuitively, pairs that are farther apart in the label
space are emphasized, and the logistic term
encourages score order consistency within the same
month. For efficiency, when the number of
admissible pairs is large, pairs per month are
uniformly subsampled up to 𝑘.
Beyond our default heterogeneous message -
passing GNN that applies SAGE neighborhood
aggregation per relation and the objectives, we
evaluate (i) alternative spatial encoders —
GATv2Conv and GraphConv —within the same
HeteroConv scaffold, and (ii) alternative ranking
losses, including last-step hybrid loss (L1 pointwise
and RANKNET pairwise per sequence), month-wise
listwise surrogate (λ-NDCG), SOFT Top-K loss, and
Neural NDCG surrogate. All comparisons are
reported in the Results section under identical data
splits, budgets, optimizer settings, and early stopping
criteria.
For the second scenario (HetEmbedRank), we
applied the same pre -training and downstream
ranking criteria. The authors pretrained the
embeddings using the HGNN jointly with BiGRU,
then extracted the pretrained embeddings from the
HGNN and saved them separat ely, ignoring the
BiGRU outputs. These embeddings were then used as
inputs for the downstream BiLSTM. They applied the
criteria on a chronological split; we adopted their
work on our user -level split. All losses were
examined for training objectives. The PSRP +
LambdaRank + Neural NDCG surrogate  loss
achieved the best results.
Monthly ground -truth relevance is computed
from the engagement -rate by mapping each
influencer to its node ID and, within each month 𝑚,
converting engagement rate to a within -month
normalized percentile ranks of engagement rate as
graded relevance in [0, 1]. Thus relevance is relative
per month rather than raw engagement. For sequence
construction, an (influencer, month) step is included
only if the influencer exists in that month’s
embedding snapshot for the corresponding split; if a
CSV label is missing fo r that month, it is stored as
NaN and excluded from evaluation. Therefore, the
evaluated candidate set for month 𝑚 consists of
influencers with both available embeddings and non-
NaN labels. Evaluation is performed per month:
influencers are ranked by predicted scores and
NDCG@K is computed using graded relevance.
Final performance is reported as an equal -weight
macro-average across test months. RBP is computed
with the same graded relevance values.

Received:  January 21, 2026.     Revised: March 4, 2026.                                                                                                   62
International Journal of Intelligent Engineering and Systems, Vol.19, No.5, 2026           DOI: 10.22266/ijies2026.0531.04

This article is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
License details: https://creativecommons.org/licenses/by-sa/4.0/
Table 4. Five seeds experiments for backbone-loss combination
Backbone/Loss/NDCG@200 Mean ± std [95% CI]
Last-step hybrid (pointwise L1 + LSRP) + Lambdarank
HGNN 0.873 0.8683 0.867 0.860 0.865 0.86666 ± 0.00475 [0.86077 , 0.87255]
HGNN + BiGRU 0.869 0.863 0.863 0.865 0.866 0.86520±2.776 [0.86211, 0.86829]
PSRP + LambdaRank + Neural NDCG surrogate
HGNN 0.884 0.882 0.878 0.880 0.879 0.8806 ± 0.00241 [0.8776, 0.8836]
HGNN + BiGRU 0.878 0.875 0.875 0.872 0.873 0.8746±0.00286 [0.87174, 0.87746]
LSRP + Lambdarank
HGNN 0.868 0.867 0.871 0.876 0.867 0.8698 ± 0.00383 [0.8650, 0.8746]
HGNN + BiGRU 0.8609 0.865 0.865 0.866 0.862 0.86378±0.00220 [0.86105, 0.86651]
lspr
HGNN 0.871 0.866 0.872 0.871 0.863 0.86860 ± 0.00391[0.86374, 0.87346]
HGNN + BiGRU 0.860 0.867 0.863 0.867 0.863 0.8640 ± 0.0030 [0.8603, 0.8677]
PSRP
HGNN 0.882 0.883 0.881 0.881 0.880 0.88140±0.00142 [0.87998, 0.88282]
HGNN + BiGRU 0.874 0.873 0.876 0.874 0.876 0.87460±0.00167 [0.87293, 0.87627]
PSRP + LambdaRank
HGNN 0.882 0.881 0.880 0.880 0.880 0.8806 ± 0.00089 [0.87949, 0.88171]
HGNN + BiGRU 0.878 0.871 0.869 0.871 0.877 0.8732 ± 0.0041[0.8682, 0.8782]

5. Results and experiments
The month -wise influencer ranking head is
evaluated on influencer -disjoint splits (70/20/10)
spanning all months using the Instagram influencer
dataset. Several loss functions are examined to
understand how supervision patterns interact with the
encoder. T he results in Table 1 show that
InstaPopAcc (HGNN -only) achieves its best
downstream ranking when trained with PSRP alone,
reaching the highest NDCG@200 = 0.881, while
adding LambdaRank or the Neural NDCG surrogate
does not improve NDCG (remaining at 0.880 ) and
provides no consistent gain on the other metrics. This
pattern suggests that for the stateless HGNN encoder,
the embeddings already support effective outcome
supervision, so extra ranking surrogates mainly
introduce competing gradients without clear benefit.
By contrast, HetEmbedRank (HGNN+BiGRU)
benefits most from PSRP + LambdaRank + Neural
NDCG surrogate when considering ranking-oriented
metrics jointly: it matches the best NDCG@200
(0.8746, essentially tied with PSRP) and achieves the
strongest RBP@200 = 0. 926 among the tested
objectives, indicating better top -heavy ranking
quality under richer ranking-aligned supervision.
Overall, the table supports the conclusion that
HGNN-only is best served by a simple final -month
pairwise signal (PSRP), whereas HGNN+BiGRU
requires stronger, combined ranking supervision
(PSRP+LambdaRank+Neural NDCG) to best shape
its recurrent temporal states for ranking performance.
This suggests that the same family of ranking losses
behaves differently depending on how temporal
information is represented by the encoder.
NDCG@K is computed using each item’s month-
wise engagement percentile as a graded relevance
signal in [0,1] and similar trends were observed
across RBP).
Table 2 indicates that both encoders produce
similarly smooth temporal trajectories, but
HetEmbedRank embeds more linearly decodable
temporal structure than InstaPopAcc. Month -ID
accuracy is slightly higher for HGNN+BiGRU on
validation and nearly tied on t est, and the linear
dynamics probe shows marginally higher cosine
alignment for HGNN+BiGRU across splits,

Table 5. Comparing with another baseline
Module NDCG@20
GNN-SN- IRR [15] 0.694
TH-DCNN- SN-IRR [16] 0.786
The proposed InstaPopAcc 0.913

Table 6. Backbone hyperparameter
Hyperparameter Value
Hidden dimension 128
Embedding dimension 32
Dropout 0.3
Learning rate 0.001
Number of epochs 60

Table 7. training objectives
loss parameters Value
Edge reconstruction) temperature 10.0
Temporal smoothness weight 0.1
L2 regularization weight 0.0001

Received:  January 21, 2026.     Revised: March 4, 2026.                                                                                                   63
International Journal of Intelligent Engineering and Systems, Vol.19, No.5, 2026           DOI: 10.22266/ijies2026.0531.04

This article is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
License details: https://creativecommons.org/licenses/by-sa/4.0/
Table 8. Optimization and training-stability settings.
Aspect Method Parameter Value
Gradient
stabilization Anomaly detection — —
Gradient
stabilization Gradient clipping Max norm 1.0
Optimizer Adam Weight decay 5e-4
Learning rate
scheduler ReduceLROnPlateau
mode max
factor 0.5
patience 5
Scheduler driver Validation metric (NDCG@200) — —

suggesting month-to-month evolution is a bit easier
to track with a linear map in the BiGRU space.
This advantage is clearest in probes that directly
test temporal ordering and memory. HetEmbedRank
achieves substantially higher order -direction
accuracy and shows slightly stronger history -
compression, with higher global (R 2) and generally
higher per-month Pearson correlations, meaning the
final state retains a more linearly recoverable
summary of past labels. At the same time, step -wise
L2 distances and cosine similarities are almost
identical between models, so the contrast  reflects
alignment with time/supervision, not raw smoothness.
Two other spatial encoders were also examined, as
shown in Table 3, holding the temporal head and
training budget fixed, GraphSAGE was replaced with
GATv2 and GraphConv within the same HeteroConv.
SAGEConv produced the highest ranking with
NDCG@200 0.881, surpassing GATv2 0.7353) and
GraphConv (0.797) in the same evaluation. On these
heterogeneous monthly graphs relation -wise SAGE
aggregation with mean fusion provides a stable bias
for sparse multi -relational neighborhoods, whereas
attention-based aggregati on (GATv2) provides no
advantage at this scale and label regime.
The experiments is conducted on five seeds for
both backbones choices and for each loss. The mean
NDCG@200 is calculated across the five seeds.in
Table 4.
Finally, a comparison with existing baselines is
made. As shown in Table 5, our model outperforming
the other models.
5.1 Optimization and hyperparameter
After several hyperparameter tuning experiments,
we found that the following settings achieved the
highest performance. for backbone stage are shown
in Table 6.
The backbone is implemented as a relation -
specific GraphSAGE-based HeteroConv layer with
Table 9. Ranker model settings
Component Setting
LSTM direction Bidirectional
hidden dimension 256
LSTM layers 2
Attention module Multihead self-Attention
Attention heads 4
Optimizer AdamW
Learning rate 5e-5
Weight decay 1e-5
LR scheduler ReduceLROnPlateau
Scheduler metric Validation NDCG
Scheduler mode max
Factor 0.5
Patience 5
Cooldown 2
Min LR 1e-6
Epsilon 1e-9
epoch 100
Batch size 128
Gradient clipping Max norm = 1.0
Early stopping min delta 0.001

mean aggregation over relations. Each relation uses
SAGEConv((-1,-1), hidden dim) to infer input
feature sizes at runtime, which allows the encoder to
consume the per -month features tensors without
manually specifying feature dimensionalities. The
produced embedding dimension=32.
For training objectives, the parameters are stated
in Table 7.
The optimizations parameters are stated in Table
8.
The ranker model hypereparameters and
optimization setting are shown in Table 9.
6. Conclusion
This paper presented InstaPopAcc, a two -stage
framework for monthly influencer ranking on
Instagram that operates on temporal, heterogeneous
graphs and clean influencer -disjoint splits. A
HeteroConv backbone with relation -specific
GraphSAGE encoders first learns month -wise
embeddings over influencer –hashtag–user-tag
interactions, and a BiLSTM with multi -head self -
attention then produces per -step scores optimized
with ranking-aware losses. Extensive experiments on
a real 13 -month influencer dataset showed th at this
architecture reliably captures both structural and
temporal signals and yields strong ranking utility
under NDCG@200, RBP@200, and AUC. A central
finding of this work is that supervision granularity
must be matched to the temporal capacity of the

Received:  January 21, 2026.     Revised: March 4, 2026.                                                                                                   64
International Journal of Intelligent Engineering and Systems, Vol.19, No.5, 2026           DOI: 10.22266/ijies2026.0531.04

This article is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
License details: https://creativecommons.org/licenses/by-sa/4.0/
encoder. For the adopted HetEmbedRank model,
PSRP + LambdaRank + Neural NDCG surrogate
achieved NDCG@200 (0.874) with the best top -
heavy ranking quality (RBP@200 ≈ 0.926).
 In contrast, for the proposed InstaPopAcc
encoder (HGNN-only), PSRP alone achieved the best
performance (NDCG@200 ≈ 0.881), and adding
LambdaRank or Neural NDCG offered no
improvement.
Relation-wise GraphSAGE provides a strong,
stable backbone for this large sparse heterogeneous
setting, and the results show that loss design must be
matched to the encoder’s temporal capacity rather
than treated as a plug-in choice.
The study also compared alternative spatial
backbones under a fixed temporal head and
supervision scheme. Relation -wise GraphSAGE
consistently outperformed GATv2 and GraphConv
on NDCG, RBP, and AUC, suggesting that degree -
normalized neighborhood aggregatio n with simple
mean fusion is a robust inductive bias for large,
sparse, heterogeneous OSN graphs. Together, these
results emphasize that ranking performance in
temporal heterogeneous networks is jointly
determined by (i) the spatial encoder, (ii) the
temporal architecture, and (iii) the alignment between
loss design and evaluation metric, rather than by any
single component in isolation.
Conflicts of Interest
The authors declare no conflict of interest.
Author Contributions
Conceptualization, Fatima Bahjat Ibrahim;
methodology, software, validation, formal analysis,
investigation, resources, data curation, Faten
Mohammed Kareem and Fatima Bahjat Ibrahim;
writing—original draft preparation, Faten
Mohammed Kareem; writing —review and editing,
visualization, Faten Mohammed Kareem and Fatima
Bahjat Ibrahim; supervision, Fatima Bahjat Ibrahim.
Acknowledgments
This work was supported by the Department of
Information and Communication Engineering, Al -
Khwarizmi Engineering College, University of
Baghdad.
References
[1] S. Saeidi and Z. Baradari, “Examining the
correlation between metrics in the Instagram
social network to identify fake pages and
improve marketing”, Computers in Human
Behavior Reports, Vol. 12, Art. 100341, 2023,
doi: 10.1016/j.chbr.2023.100341.
[2] R. Zheng, L. O .-Forero and Y. Chen,
“Implications of social network structures on
socially influenced decision-making”, Decision,
Vol. 51, No. 1, pp. 85-103, 2024.
[3] J. K. Lee and A. Kronrod, “The strength of
weak-tie consensus language”, J. Mark. Res. ,
Vol. 57, No. 2, pp. 353-374, 2020.
[4] E. Katz, P. F. Lazarsfeld and E. Roper, Personal
Influence: The Part Played by People in the
Flow of Mass Communications , 2006, doi:
10.4324/9781315126234.
[5] Z. Li, W. Piao, Z. Sun, L. Wang, X. Wang and
W. Li, “User real -time influence ranking
algorithm of social networks considering
interactivity and topicality”, Entropy, Vol. 25,
No. 6, Art. 926, 2023, doi: 10.3390/e25060926.
[6] D. J. Watts and P. S. Dodds, “Influentials,
networks, and public opinion formation”,
Journal of Consumer Research, Vol. 34, No. 4,
pp. 441-458, 2007, doi: 10.1086/518527.
[7] E. J. Rosado, L. Wang, L. P. Dringus and J. Sun,
“Unveiling influencer-driven PII disclosures in
social media discourse”, Open Science
Framework, 2024, doi: 10.31219/osf.io/k6gmf.
[8] K. K. Renganathan, S. B. Krishnan, S. S.
Subramanian and P. Chakrabarti, “Exploring
Instagram influencer networks: A graph -based
machine learning approach”, Mathematical
Modelling of Engineering Problems , Vol. 11,
No. 8, pp. 2048 -2059, 2024, doi:
10.18280/mmep.110806.
[9] J. Park, H. Ahn, D. Kim and E. Park, “GNN-IR:
Examining graph neural networks for influencer
recommendations in social media marketing”, J.
Retail. Consum. Serv. , Vol. 78, Art. 103705,
2024, doi: 10.1016/j.jretconser.2024.103705.
[10] Y. Kim, C. Denton, L. Hoang and A. M. Rush,
“Structured attention networks”, In: Proc. of
International Conference on Learning
Representations, 2017.
[11] M. A. Reda and F. B. Ibrahim, “Color
quantization based artificial bee colony and
training tools”, International Journal of
Computing and Digital Systems, Vol. 11, No. 1,
pp. 314-324, 2022, doi: 10.12785/ijcds/110126.
[12] N. M. Sulaiman, A. A. Tmeme and M. N. Mahdi,
“An overview of audio-visual source separation
using deep learning”, Al-Khwarizmi
Engineering Journal, Vol. 19, No. 4, pp. 42-55,
2023, doi: 10.22153/kej.2023.06.003.
[13] T. A. Wotaifi and B. N. Dhannoon, “An
effective hybrid deep neural network for Arabic
fake news detection”, Baghdad Science Journal,

Received:  January 21, 2026.     Revised: March 4, 2026.                                                                                                   65
International Journal of Intelligent Engineering and Systems, Vol.19, No.5, 2026           DOI: 10.22266/ijies2026.0531.04

This article is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
License details: https://creativecommons.org/licenses/by-sa/4.0/
Vol. 20, No. 4, pp. 1392 -1401, 2023, doi:
10.21123/bsj.2023.7427.
[14] A. Al-Hafiz, A. Jabir and S. Subramaniam, “K-
Gen PhishGuard: An ensemble approach for
phishing detection with K -means and genetic
algorithm”, Al-Khwarizmi Engineering Journal,
Vol. 21, No. 2, pp. 117 -135, 2025, doi:
10.22153/kej.2025.04.011.
[15] F. M. Kareem and F. B. Ibrahim,
“Comprehensive review on machine learning
methods for detecting social media malicious
activities”, International Journal of Computing
and Digital Systems , Vol. 18, No. 1, pp. 1 -18,
2025, doi: 10.12785/ijcds/1571099452.
[16] PyTorch Geometric Documentation ,
“torch_geometric.nn.conv.HeteroConv”,
[Online]. Available: https://pytorch -
geometric.readthedocs.io/en/latest/generated/to
rch_geometric.nn.conv.HeteroConv.html.
[17] S. Hochreiter and J. Schmidhuber, “Long short-
term memory”, Neural Computation, Vol. 9, No.
8, pp. 1735 -1780, 1997, doi:
10.1162/neco.1997.9.8.1735.
[18] Y. Kim, C. Denton, L. Hoang and A. M. Rush,
“Structured attention networks”, In: Proc. of
International Conference on Learning
Representations, 2017.
[19] C. Burges, T. Shaked, E. Renshaw, A. Lazier,
M. Deeds, N. Hamilton and G. Hullender,
“Learning to rank using gradient descent”, In:
Proc. of 22nd International Conference on
Machine Learning , pp. 89 -96, 2005, doi:
10.1145/1102351.1102363.
[20] H. Li, “Learning to rank for information
retrieval and natural language processing” ,
Foundations and Trends in Information
Retrieval, Vol. 4, No. 1 –2, pp. 1 –113, 2011,
doi:10.1561/1500000016.
[21] C. Burges, R. Ragno and Q. V. Le, “Learning to
rank with nonsmooth cost functions”, Advances
in Neural Information Processing Systems 19 ,
pp. 193-200, 2006.
[22] P. Donmez, K. M. Svore and C. J. C. Burges,
“On the local optimality of LambdaRank”, In:
Proc. of 32nd International ACM SIGIR
Conference on Research and Development in
Information Retrieval, pp. 460 -467, 2009, doi:
10.1145/1571941.1572021.
[23] C. J. Willmott and K. Matsuura, “Advantages of
the mean absolute error (MAE) over the root
mean square error (RMSE) in assessing average
model performance”, Climate Research, Vol. 30,
pp. 79-82, 2005, doi: 10.3354/cr030079.
[24] C. Li, K. Liu and S. Liu, “A survey of loss
functions in deep learning”, Mathematics, Vol.
13, No. 15, Art. 2417, 2025, doi:
10.3390/math13152417.
[25] F. Petersen, H. Kuehne, C. Borgelt and O.
Deussen, “Differentiable Top -k classification
learning”, In: Proc. of 39th International
Conference on Machine Learning , pp. 17656 -
17668, 2022.
[26] J. Grabocka, R. Scholz and L. S .-Thieme,
“Learning surrogate losses”, arXiv Preprint,
arXiv:1905.10108, 2019.
[27] S. Kim, J.-Y. Jiang, M. Nakada, J. Han and W.
Wang, “Multimodal post attentive profiling for
influencer marketing”, In: Proc. of The Web
Conference 2020 , pp. 2878 -2884, 2020, doi:
10.1145/3366423.3380052.
[28] F. M. Kareem and F. B. Ibrahim,
“HetEmbedRank: Pretrained heterogeneous
graph embeddings for temporal influencer
ranking”, International Journal of Intelligent
Engineering and Systems, Vol. 18, No. 10, pp.
589-606, 2025, doi:
10.22266/ijies2025.1130.38.
