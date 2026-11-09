---
title: 'LiDDA: Data Driven Attribution at LinkedIn'
url: https://arxiv.org/abs/2505.09861
category: ai-marketing
subcategory: empirical
date: 2025-05
venue: ''
authors:
- John Bencina
- Erkut Aykutlug
- Yue Chen
- Zerui Zhang
- Stephanie Sorenson
source: arxiv
pdf_url: https://arxiv.org/pdf/2505.09861
pages: 13
chars: 58503
fetched_at: '2026-11-08T13:10:46+00:00'
kb_version: 1
---

# LiDDA: Data Driven Attribution at LinkedIn

LiDDA: Data Driven Attribution at LinkedIn
John Bencina∗
LinkedIn Corporation
Sunnyvale, USA
jbencina@linkedin.com
Erkut Aykutlug∗
LinkedIn Corporation
Sunnyvale, USA
eaykutlug@linkedin.com
Yue Chen
LinkedIn Corporation
Sunnyvale, USA
florachen0014@gmail.com
Zerui Zhang
LinkedIn Corporation
Sunnyvale, USA
zerzhang@linkedin.com
Stephanie Sorenson
LinkedIn Corporation
Sunnyvale, USA
ssorenson@linkedin.com
Shao Tang
LinkedIn Corporation
Sunnyvale, USA
tangshao28@gmail.com
Changshuai Wei†
LinkedIn Corporation
Seattle, USA
chawei@linkedin.com
Abstract
Data Driven Attribution, which assigns conversion credits to mar-
keting interactions based on causal patterns learned from data, is
the foundation of modern marketing intelligence and vital to any
marketing business and advertising platform. In this paper, we in-
troduce a unified transformer-based attribution approach that can
handle member-level data, aggregate-level data, and integration of
external macro factors. We detail the large scale implementation of
the approach at LinkedIn, showcasing significant impact. We also
share learnings and insights which are broadly applicable to the
marketing and ad tech fields.
CCS Concepts
•Computing methodologies → Artificial intelligence;•Ap-
plied computing→ Marketing;•Information systems → On-
line advertising;•Mathematics of computing → Probability
and statistics.
Keywords
Multi-Touch Attribution, Media-Mix Modeling, Attention Mecha-
nism, Computational Marketing, Transformer
1 Introduction
Marketers rely on attribution measurement to understand the im-
pact of marketing campaigns on customers’ journeys and decisions.
Accurate attribution enables marketers to better optimize market-
ing spend and strategy to maximize their return on investment
(ROI). In this paper, we propose a framework for large scale end-to-
end attribution system and detail the implementation at LinkedIn.
LinkedIn Data Driven Attribution (LiDDA) leverages a combina-
tion of bottom-up and top-down modeling approaches in order to
build a more accurate attribution platform to measure campaign
performance and ROI. The system was originally developed for our
internal Go-To-Market (GTM) Marketing and has since expanded
to support external applications for LinkedIn customers.
∗These authors contributed equally
†Corresponding author
1.1 LinkedIn Use Case
GTM Marketing is responsible for managing digital marketing
campaigns for various LinkedIn products (e.g., Recruiter Lite, Sales
Navigator), targeting both acquisition and retention objectives,
where marketing audiences include both consumers and buyers.
Consumer marketing focuses on the individual as a member such as
member account signups. Buyer marketing focuses on the company-
level conversions such as the use of LinkedIn Ads platform ads or
Talent Solutions job posts.
Both segments are targeted using a combination of owned and
external channels. Owned channels include Email and the LinkedIn
Ads Platform (Feed Ads) where we own the platform used and have
greater visibility to individual engagements. External channels refer
to other online platforms such as Paid Search, Social Media, and
Streaming. These channels do not provide individual level data,
and we are often limited to aggregate information such as the total
number of impressions in a time period.
One major challenge is lack of a unified view of the member
journey across multiple channels. Existing media-mix-modeling
(MMM) approaches provide channel-level visibility; however they
lack detailed campaign breakouts and journey information. Last
touch attribution (LTA) was the default standard; yet it biased
results to bottom of funnel (BOFU) campaigns and omitted channels
without individual identifiers.
Through our work on LiDDA, we are able to build an approach
which combines signals using both top-down and bottom-up in-
formation. This enables our marketing team to utilize attribution
across different levels of granularity while still maintaining con-
sistency. In the next section we further discuss the differences in
top-down and bottom-up attribution approaches.
1.2 Overview of Related Work
Data-driven attribution (DDA) aims to measure the contribution
of online campaigns at the user level using a bottom-up approach.
On the other hand, Media-Mix modeling (MMM) considers both
online and offline channels along with seasonality using a top-down
(aggregate time-series) approach.
arXiv:2505.09861v3  [cs.LG]  27 May 2026

Bencina et al.
1.2.1 Media-Mix Modeling.Media-mix models (MMM) use aggre-
gated time-series data to model conversions as a function of online
and offline channels as well as macro-economic factors and sea-
sonality. MMM have been widely used since the 1960s [3, 16], and
provide a holistic view across all channels and external factors. On
the other hand, they come with different challenges [5]. One of the
shortcomings is that they do not have visibility to analyze data at
the user level.
1.2.2 Rules Based Attribution.Traditional attribution models com-
monly use rule-based attribution (RBA) approaches such as first-
touch, last-touch, or time decay[9]. These approaches assign con-
version credit based on simple, predetermined rules at user level.
RBA methods are easy to understand and implement; however, they
are often based on limited assumptions and introduce biases.
1.2.3 Data-Driven Attribution.Data-driven attribution (DDA) ad-
dresses the limitations of RBA by leveraging machine learning and
statistical techniques to allocate conversion credit learned from
data. Different modeling approaches such as Logistic regression
[18], Bayesian [1, 15] and Survival Theory [ 24] have been used.
Deep learning approaches such as CAMTA [ 13], DNAMTA[14],
and CausalMTA [23] have demonstrated improved performance
with these classes of models.
1.3 Our contributions
As far as we know, LiDDA is the first industry-deployed large-scale
DDA system that leverages transformer-type attention mechanism
and can handle member-level, aggregate-level and integration of
external macro factors. In particular, the system is highlighted by: (i)
Transformer Architecture: our use of transformer type of attention
offers both single-pass inference and an explainability mechanism;
(ii)Temporal-aware attention: we discretize time gaps between cam-
paign touchpoints and learn positional embeddings—plus a special
day-of-week embedding—to capture both sequence order and sea-
sonal effects; (iii)Privacy -driven data imputation: to correct for
missing paid-media signals (e.g. due to GDPR/CCPA restrictions),
we probabilistically inject aggregated impressions back into user
paths; (iv)Unified DDA&MMM outputs: we reconcile discrepancies
between independent DDA and macro-level MMM by training-time
calibration; (v)End -to-end solution: we present our modeling in-
novations, implementation details, comprehensive evaluation and
insights from launching to both GTM marketing and Ads platform
in the paper.
2 LiDDA System
2.1 System Overview
LiDDA is our modeled attribution platform (Figure 1) which uti-
lizes an attention-based modeling approach. Attention models are
well suited for this task since they retain sequential information
about the buyer journey and also enable us to incorporate addi-
tional features about the member, their company, and campaign
information.
Overall, the model is structured as a binary classification task
to predict whether a buyer journey will result in a conversion
𝑃(𝑌|𝐸 𝑀,𝐸𝐶,𝑆), where𝑌 denotes the binary conversion outcome,
𝐸𝑀 denotes the member embedding with length 𝐷𝑀,𝐸𝐶 denotes
Figure 1: High level diagram showing the end-to-end compo-
nents of our attribution modeling framework
the (member’s) company embedding with length𝐷𝐶, and𝑆 denotes
the sequence of marketing touchpoints on the member with length
𝑁 .𝐸𝑀 is a member embedding derived from LinkedIn data such as
skills, titles, etc. that generally capture latent features of that mem-
ber. Likewise,𝐸𝐶 is a company embedding derived from LinkedIn
data such as industry, roles, etc.
From the trained model, we output the aggregated attention
weight matrix from the touchpoint sequence 𝑆. The attention
weights are normalized such that they add up to 1.0, i.e., ˆ𝛼𝑖 =
𝛼𝑖˝𝑛
𝑗=1𝛼𝑗 , and the normalized weights are interpreted as percent con-
tribution of that touchpoint to the final conversion event. We further
discuss attention in Section 2.4.
The attention weights represent the relative credits within the
path; however they still need to be rescaled for overall impact.
We use a separate media-mix model (MMM) to adjust the DDA
credits at the channel level to account for overall incrementality
and channels where individual exposure data does not exist or is
not available. This is discussed further in Section 2.7.
2.2 Path Creation
The touchpoint sequence𝑆 is modeled as a time-ordered series of
interactions, where each touchpoint,𝑡∈T , is one of the possible
(channel, action) pairs, such as (EMAIL, OPEN) or (AD, CLICK).
Sequences are truncated to the most recent 𝑁 interactions, and
each touchpoint is encoded as a learned embedding capturing its
latent characteristics. These embeddings are combined across time
to form an𝑁×𝑑representation of the customer journey.
To enrich the representation, each timestep also includes a mar-
keting campaign embedding 𝐸𝑀𝐶𝐼𝐷 R𝑀𝐶𝐼𝐷×dim , generated from
campaign metadata and content using an upstream LLM fine-tuned
on LinkedIn data. This approach allows flexibility in combining
structured and unstructured data consistently across domains.

LiDDA: Data Driven Attribution at LinkedIn
2.3 Positional Representations
2.3.1 Positional Encodings.Attention models do not inherently
model the order of touches in the paths so additional encodings
are needed to capture the relative positions of each touch. Si-
nusoidal positional encodings are commonly used for temporal
ordering as in the original attention design [ 21]. These are im-
plemented as: 𝑃𝐸(𝑝𝑜𝑠,2𝑖) =𝑠𝑖𝑛(𝑝𝑜𝑠/ 100002𝑖/𝑑𝑚𝑜𝑑𝑒𝑙),𝑃𝐸(𝑝𝑜𝑠,2𝑖+1) =
𝑐𝑜𝑠(𝑝𝑜𝑠/10000 2𝑖/𝑑𝑚𝑜𝑑𝑒𝑙)
Because our touchpoint embedding𝐸𝑇 is at the granularity of
(channel, action), the number of possible combinations is far lower
than typical NLP vocabulary sizes. Therefore we use a substantially
smaller embedding dimension for our data. We employ Time Abso-
lute Position Encodings (tAPE) where the positional encoding above
is modified to adjust for the lower dimensional representation[8].
The tAPE encodings are defined as:𝜔𝑘 = 10000−2𝑘/𝑑𝑚𝑜𝑑𝑒𝑙 ,𝜔𝑛𝑒𝑤 𝑘 =
𝜔𝑘×𝑑𝑚𝑜𝑑𝑒𝑙
𝐿 .
2.3.2 Positional Embeddings.Positional encodings are not suffi-
cient for our domain where marketing engagements are generated
with irregular patterns and not across fixed intervals. For example,
the time between an impression and the following click may be a
few seconds while the time between two impressions could be days.
We capture these irregular differences by representing the time dif-
ference between interactions as a discrete interval. For LinkedIn use
cases, we use days as the interval unit since the look-back-window
is limited to a few months based on business requirements.
Each touchpoint has a time interval relative to the final conver-
sion state in the path, encoded by days as𝐷 with a corresponding
learned embedding𝐸𝐷. Due to the strong seasonality of our market-
ing data, we also learn embeddings𝐸𝐷𝑂𝑊 corresponding to DOW
encoding of each touchpoint.
We combine all the embeddings together for each touchpoint as:
𝑐𝑜𝑛𝑐𝑎𝑡(𝐸 𝑀𝐶𝐼𝐷,𝐸𝑇)+𝐸 𝐷+𝐸𝐷𝑂𝑊+𝑡𝐴𝑃𝐸.
2.4 Attention Mechanism
We explored different methodologies for performing data driven
attribution in our model as discussed in Section 1.2.3. In addition
to their efficiency, models incorporating attention layers such as
DNAMTA and CAMTA [13, 14], outperformed other model designs
in this domain. Attention was originally proposed for NLP tasks
[21], but later adopted in many other domains. Formally, attention
is defined as:
Attention(𝑄,𝐾,𝑉)=softmax( 𝑄𝐾𝑇 √𝑑𝑘 )𝑉(1)
We utilize the multi-head variation of attention where each head
𝐻has the ability to generate its own attention weights:
MultiHead(𝑄,𝐾,𝑉)=Concat(h 1,h 2,...,h 𝑛)(2)
The attention mechanism enables the model to adjust the weight
given to different tokens in a sequence to optimally solve its ob-
jective. In LiDDA, we utilize a self-attention setup where 𝑄,𝐾,
and𝑉 are equivalently the marketing engagements performed by
the member. We apply attention over the sequence𝑆 and use the
attention scores in the training classification task. The attention
operation produces a representation of the sequence 𝐸𝑆 where
Channel Incremental Attention
Channel A 14.4% 12.7%
Channel B 52.3% 53.4%
Channel C 29.5% 32.5%
Channel D 3.8% 1.5%
Table 1: Comparison of incremental propensity and attention
weight from LiDDA model.
𝐸𝑆∈R 𝑁×𝐻×dim . We aggregate the heads by averaging the scores
across the head dimension to obtain𝐸′ 𝑆∈R 𝑁×dim .
Different strategies exist for performing classification from at-
tention scores. In BERT [ 6], the authors created a special [CLS]
token at the start and use only the learned representation of the
first token. Other valid approaches include max-pooling or mean-
pooling over the entire sequence. During inference, we compute the
final attribution output as the summation of the attention weights
across all heads and then normalize each row to 1.0 such that each
row represents a path and each value in that row represents the
𝑗-th touchpoint in that sequence. We set masked values to 0 if a
path is shorter than our maximum length.
In LiDDA, we keep all attention scores by flattening the attention
output. The motivation behind this decision is to retain as much
positional information as possible when computing the attention
weights. Additionally, we limit our attention module to a single
layer in order to reduce behavior where attention interpretability
may be affected by abstract representations across timesteps as
discussed in the next section.
2.4.1 Attention for Attribution.Prior works [ 13, 14] utilize
attention-based crediting by applying a self-attention layer over a
recurrent network. Our initial exploration of this approach found
a heavy bias towards end-of-path touches. Using a bi-directional
LSTM may help alleviate this effect; however we modified the ap-
proach to directly apply self attention over the input sequence. One
issue with the LSTM encoder is that the hidden state contains infor-
mation about previous timesteps, making attention interpretation
less straight forward [17]. The topic of attention interpretability
has been the subject of extensive research [ 12, 22]. The central
concern is that the resulting weights may not faithfully align with
the model final output. While our modification can still introduce
interpretability issues in attention based models [ 4], we observe
within our domain that attention weights do impact model output.
It is also possible to compute attribution based on the incremental
propensity from the prior engagement [18] or as an approximation
of Shapley values [23]. These methods are not necessarily superior.
Counterfactual simulations can be computationally expensive and
require accurately determining the counterfactual which is non-
trivial. We did evaluate the attributions under the attention vs
incremental propensity and found negligible differences (Table
1). We also observed that incremental propensity approach often
produces early jumps causing front-loaded attribution as changes
in propensity saturate with length.

Bencina et al.
2.5 Imputation of Paid Media Touchpoints
LinkedIn’s outbound marketing channels are grouped into owned
and paid channels. For owned channels, we can collect touchpoints
from all actions at the user level, e.g., sends, opens, clicks, impres-
sions, while for external channels, impression data at the user level
are not available, e.g., due to privacy regulations like GDPR or
CCPA.
Algorithm 1Allocate Member Impressions
Inputs:
External total Imp. and Clicks{𝐼 ext 𝑐,𝑑,𝐶 ext 𝑐,𝑑}, clicks set𝐽 𝑖,𝑐,𝑑
Owned Impressions{𝐼 own total,𝐼 own clickers}
No-click pathsP𝑑, path-weights{𝑢𝑘}
Outputs:click-imps{𝑚 𝑗}, path-imps{𝐼 𝑘}
Step 1: Member-only budget
𝐼𝑑 =
∑︁
𝑐
𝐼 ext 𝑐,𝑑
˝
𝑖|𝐽𝑖,𝑐,𝑑|
𝐶ext 𝑐,𝑑
Step 2: Stochastic click allocation
𝛼∗ = 𝐼 own clickers
𝐼 own total , 𝑟 𝑐,𝑑 =𝛼∗ 𝐼 ext 𝑐,𝑑 𝐶ext 𝑐,𝑑
𝑚𝑗 ∼Geom 𝑝= 1 𝑟𝑐(𝑗),𝑑 , 𝐿 𝑑 =𝐼𝑑− ∑︁
𝑗
𝑚𝑗
Step 3: Stochastic leftover allocation
𝑝𝑘 = 𝑢𝑘˝
ℓ∈P𝑑𝑢ℓ
, 𝜆 𝑘 =𝐿𝑑𝑝𝑘, ˜𝐼𝑘∼Poisson(𝜆 𝑘)
𝐼𝑘 =
j
˜𝐼𝑘 𝐿𝑑 ˝
ℓ ˜𝐼ℓ
k
When a user clicks on an ad on an external platform they land
on a LinkedIn microsite. We can use the URLs from microsites as a
proxy for paid clicks at the user level. Meanwhile, we can also obtain
daily aggregate campaign-level data, e.g, number of impressions or
clicks for a campaign on a given day. Together with member-level
clicks and impressions from owned channel, we can impute paid
media impressions probabilistically.
Let𝑖 index members,𝑑 days,𝑐 channels, 𝑗∈𝐽 𝑖,𝑐,𝑑 external-click
events, and𝑘∈P 𝑑 no-click paths (i.e., path without clicks from
external channel). We perform the imputation in three steps (Al-
gorithm 1): (i) Estimate member impression from external total
impressions, yielding total "budget" that needs allocation; (ii) Com-
pute impression per click among the clickers 𝑟𝑐,𝑑 and then draw
impression from corresponding geometric distribution; (iii) Assign
weights𝑢𝑘 for no-click path𝑘 based on campaign and location infor-
mation, then draw Poisson counts of impressions for no-click path
to allocate remaining impressions. Further information, including
the step-by-step procedure, implementation notes, the equivalent
convex-optimization formulation, and its solution, is provided in
Appendix A.1.
2.6 Sessionization
Another challenge in attribution modeling is that some channels
generate far more touchpoints than others, creating a signal imbal-
ance. For example, emails may be sent weekly, whereas in-feed ads
can appear multiple times per day. Since our attribution paths have
a fixed length, owned-channel touchpoints can dominate and crowd
out paid (external) exposures. To address this, we apply two path-
adjustment steps, sessionization and downsampling, to produce
more balanced engagement sequences (Figure 2).
For sessionization, we group impressions from the same cam-
paign on the same day into a single session-level touchpoint for
specific channels. For downsampling, we apply empirically de-
rived, channel–action–specific drop rates to remove excess touch-
points. In both approaches, we recover the attribution credit to
grouped/removed events according to the sampling probability.
More details can be found in Appendix A.2.
Figure 2: We group touchpoints from some owned channels,
e.g., LinkedIn Platform, within a session into a single rep-
resentative touchpoint. The attribution given to this one
touchpoint is distributed evenly among the grouped cam-
paigns.
2.7 Output Calibration
MMM provides channel-level attribution and measures marketing
incrementality in the context of macroeconomic factors but cannot
trace individual member journeys. DDA captures those journeys at
the interaction level but lacks certain signals (e.g. radio, events, TV,
or privacy-restricted data). Two independent attribution systems
may diverge, particularly if they utilize different interactions, and
thus a unified approach is needed[7, 10].
We introduce a training-time calibration that extracts signals from
our MMM model to our DDA model to form a unified macro level
view for marketers, while still permitting fine-grained, path-level
attributions. Let𝑎𝑗(𝜃) be the DDA attribution weight for touchpoint
𝑗,𝐴DDA 𝑐 (𝜃)= ˝ 𝑗:chan(𝑗)=𝑐 𝑎𝑗(𝜃) the total DDA weight for channel
𝑐,𝐴MMM 𝑐 the corresponding channel-level attribution from MMM,
LDDA(𝜃) the usual DDA training loss, and𝛽≥ 0a tuning parameter.
We minimize the combined loss:
Ltotal(𝜃)=L DDA(𝜃) +𝛽
∑︁
𝑐
𝐴DDA 𝑐 (𝜃)−𝐴 MMM 𝑐  2,
and providepath level calibrationin Algorithm 2.
This calibration “teaches” the DDA model, during training, to re-
spect the macro-level attribution from MMM, eliminating the need
for any post-hoc rescaling, while preserving detailed, campaign-
and engagement-level attribution within each channel. Details on
batch level calibrationandpath level calibrationcan be found in
Appendix A.3.1 and Appendix A.3.2.
3 Experimentation Results
The goal of the attribution model is to proportionally quantify the
impact of each marketing action towards a conversion. Since there

LiDDA: Data Driven Attribution at LinkedIn
Algorithm 2Train DDA Model with Path-Level MMM Calibration
Inputs:
• Paths dataset{(𝑥𝑖,𝑦𝑖,𝑠𝑖)}𝑁 𝑖=1, where𝑥𝑖 are features,𝑦𝑖 labels,
and𝑠𝑖 the sequence of length𝐿𝑖
•MMM attribution𝑎 MMM 𝑐 , channel distribution𝜋 MMM 𝑐
• DDA network𝑔(· ;𝜃) with parameters𝜃, that output conver-
sion probability𝑓, and attention weight𝑎.
• Hyperparameters: calibration weight 𝛽, learning rate 𝜂,
epochs𝑇, batch size𝐵
Output:Trained parameters𝜃
forepoch=1to𝑇do
Shuffle dataset
foreach batchBof size𝐵do⊲Forward pass
foreach path𝑖∈Bdo
Compute DDA attributions𝑎𝑖(𝑐;𝜃)for𝑐=1,...,𝐶
Compute path-level channel distribution𝜋 (𝑖) 𝑐
Compute path-level IPW weights𝑤(𝑖) 𝑐 = 𝜋(𝑖) 𝑐 𝜋 MMM𝑐
"Recover" path-level MMM attribution as target
˜𝑡(𝑖) 𝑐 =𝑤(𝑖) 𝑐 𝑎MMM 𝑐 , 𝑡 (𝑖) 𝑐 = ˜𝑡(𝑖) 𝑐 ˝
𝑑 ˜𝑡(𝑖) 𝑑
end for
Compute base DDA loss
LDDA = 1 |B| ∑︁ 𝑖∈B ℓ𝑓𝑖(·;𝜃),𝑦 𝑖 
Compute calibration loss (MSE or KL):
Lcalib = 1 |B| ∑︁ 𝑖∈B 𝐶∑︁ 𝑐=1 𝑎𝑖(𝑐;𝜃)−𝑡 (𝑖) 𝑐  2
Total loss:
L=L DDA +𝛽L calib
⊲Backward and update
𝜃←𝜃−𝜂∇ 𝜃L
end for
end for
is no ground-truth data on the contribution of each action towards a
conversion, we perform the following offline and online validations
to evaluate the attribution model.
3.1 Offline Validation
In offline validation, we seek to ensure the model’s accuracy and sta-
bility as these are intuitively desirable properties of any attribution
system. We also performed ablation analysis on model input and
compare our model with external models. Due to space limitation,
we summarize the finding here. Further details can be found in
Appendix B.
3.1.1 Prediction Stability.We first assess the model’s performance
using binary classification metrics, aiming for high predictive accu-
racy. We hold 10% of the training data for validation and separate
the rest into 10 subsets. We retrain an attribution model on each
subset, evaluate it on the holdout dataset, and record its perfor-
mance. The resulting prediction performances converge (> 0.97for
ROC-AUC and PR-AUC), confirming that the attribution model has
high prediction power and exhibits consistent results.
We also evaluate the stability of predicted conversion rate using
the Anderson-Darling statistic [2, 20]. The result shows that the
predicted conversion rates are consistent over time.
3.1.2 Attribution Stability.We perform a similar check on our
model’s stability in producing attribution results. For each action,
we bootstrap sample that action’s weights with replacement for
100 times, calculate the mean of the samples, and analyze the distri-
bution of the 100 means to evaluate the stability of the attribution
weights (Figure 3). We observe that the mean weights of each action
converge. While this approach does not have an intrinsic absolute
threshold, we use these values as guardrails to monitor for potential
issues.
Figure 3: Distribution of bias in the bootstrap means of the
action weights, calculated as the difference between each
bootstrap mean and the actual sample mean. The bias distri-
butions center around 0.
3.1.3 Ablation on Model Input.We conducted an ablation study
to quantify the impact of each model component by training and
evaluating DDA model with particular features removed, including
member/company embeddings, campaign embeddings, date embed-
dings, or all embeddings (sequence only). We compared ROC-AUC
against the baseline and measured how the channel-level attribu-
tion mix deviated (mean squared deviation on percentage) from
the full model. Removing campaign or date features caused small
AUC drops (–0.1% and –0.3%), while omitting entity embeddings
and using sequence alone reduced AUC more substantially (–1.7%
and –5.1%). In terms of attribution stability, date removal produced
the largest shift (MSD=49.3), with campaign and entity removals
and the sequence-only variant showing smaller but non-negligible
deviations (MSD=8.5, 14.4, and 11.8, respectively).
3.1.4 Approach Comparison.We performed additional offline eval-
uations of LiDDA and CausalMTA [23] using code published by
the authors on GitHub. We implemented CausalMTA as described
by the authors, omitting features such as time information that are
not part of its original design, and adapting inputs such as member
embeddings. We trained both CausalMTA and LiDDA for 5 trials
using a static set of marketing paths. In Table 7 we observe the

Bencina et al.
models fit equally well to the data in terms of ROC-AUC evaluation
with both achieving scores between 0.982 and 0.983.
In Table 2, we compare the calculated attribution across two
marketing channels. Here we find significant differences between
the models. LiDDA outperforms CausalMTA where its results are
more closely aligned with our experimentally validated media-mix
model which reports a mix of 89.6% and 10.4% across channels A
and B respectively.
Table 2: Normalized attribution by marketing channel from
CausalMTA, LiDDA, and MMM ground-truth model. Results
are computed over 5 trials and report 95% CI.
Channel CausalMTA LiDDA MMM
Channel A0.667±0.010 0.826±0.0010.896
Channel B0.333±0.011 0.174±0.0010.104
Beyond attribution quality, computational efficiency is a prac-
tical consideration for production deployment. We compare the
training time taken for each model on a common dataset. The
CausalMTA model requires multiple training passes for the vari-
ational autoencoder, journey reweighting, domain classifier, and
outcome prediction. By contrast, LiDDA is trained in a single pass
and obtains weights at no additional cost from the attention layer.
For this comparison we set all models to 3 epochs and trained on
a common dataset with 40,000 training paths and 8,000 inference
paths.
Additionally, while the CausalMTA paper refers to Shapley val-
ues for allocation credit, the authors note that this is computation-
ally infeasible and rely on an approximation [23]. The available code
for CausalMTA utilizes incremental value heuristic (IVH) methodol-
ogy where allocation is derived by measuring the predicted outcome
change caused by each timestep. Although this method has been
shown to produce inaccurate estimations [19], we utilized it for our
baseline since the provided Shapley calculation could not run given
our path lengths.
We made a further improvement to the provided IVH code by
implementing a batched version to facilitate faster testing. This
modified version was used in our benchmark. In Table 3, we ob-
serve significantly faster training and inference performance from
LiDDA with a 78% reduction in training time and a 99% reduction
in inference time.
Table 3: Mean training and inference time in seconds using
all models set to 3 epochs with 95% CI reported over 5 trials.
Inference for CausalMTA uses IVH while LiDDA uses atten-
tion weights.
Stage CausalMTA LiDDA Reduction
Training (epoch)145.37±0.68 31.97±0.37−78%
Inference (dataset)369.72±4.12 2.16±0.05−99%
3.2 Online Validation of Deployment
Offline validation does not give us insight into whether the atten-
tion weight based attribution is close to actual member behavior.
Thus, we run experiments for online validations to check how close
our model’s attributions align with real-world marketing efforts. We
can either run member level test for owned channels or geo-level
experiments for external paid channels. We conduct incremental
lift tests for the email channel. In particular, we randomly split
members into two groups. We select certain campaigns (Tℎ) to
hold out email sending during the experiment in the control group
and conduct business as usual in the treatment group. It is impor-
tant to note that email sending was sparse across both members
and time, limited to approximately one email per week to a small
set of selected members within the connection graph. Additionally,
AA tests were conducted as a basic validation of the experimental
setup, and no statistically significant differences in conversion rates
were found between groups.
To validate member-level experiment, we simulate a holdout exper-
iment within the treatment group by creating counterfactual con-
version paths, where the holdout campaign touchpoints (𝑡∈T ℎ)
are omitted. This approach helps estimate what the conversion
path would look like had the member been in the control group.
Define two conversion probabilities:𝑃(𝑌= 1|𝑍= 1,𝑆=𝑆 1) with
original path𝑆1, and𝑃1(𝑌= 1|𝑍= 1,𝑆=𝑆 1−T ℎ) with counterfac-
tual path𝑆1−T ℎ, where𝑍= 1indexes the treatment group. The
corresponding attribution of touchpoints𝑡∈T ℎ can be defined as:
𝑎(T ℎ)= 𝑃1(𝑌=1|𝑆=𝑆 1)−𝑃 1(𝑌=1|𝑆=𝑆 1−T ℎ) 𝑃1(𝑌=1|𝑆=𝑆 1) (3)
where,𝑃1(·)=𝑃(·|𝑍= 1). We compare the distribution of DDA
attribution against the measured attribution from the experiment.
A similar formulation can be constructed using𝑃0(·). We did not
use this route for validation, as the simulation of counterfactual
paths (𝑆0+T ℎ) by adding touchpoints requires more assumptions
such as sequencing and campaigns which may introduce bias and
noise.
3.2.1 Inverse Propensity Weighting.From the experimentation data,
we can calculate ˆ𝑃1(𝑌= 1|𝑆=𝑆 1) and ˆ𝑃0(𝑌= 1|𝑆=𝑆 1−Tℎ) easily,
by simply counting percentage of conversions in the treatment
and control group. In order to obtain an estimate of𝑃1(𝑌= 1|𝑆=
𝑆1−T ℎ), we use inverse propensity weighting (IPW)[11]. Denote
𝑒𝑖 as the propensity score for member 𝑖 and𝑍𝑖 as the indicator
for member𝑖 receiving campaigns as in the treatment group (=1)
and for being in the control group (=0). Denote𝐸𝑀𝑖 as the member
embeddings for member𝑖that are computed by LinkedIn.
Step 1: Estimate each member’s treatment propensity, and cor-
responding IPW
𝑒𝑖 =𝑃(𝑍 𝑖 =1|𝐸 𝑀𝑖), 𝑤 𝑖 =
(
1,if𝑍 𝑖 =1
𝑒𝑖
1−𝑒𝑖,if𝑍 𝑖 =0 (4)
Step 2: Compute the attribution
ˆ𝑎exp(Tℎ)= ˆ𝑃1(𝑌=1|𝑆=𝑆 1)− ˆ𝑃1(𝑌=1|𝑆=𝑆 1−T ℎ) ˆ𝑃1(𝑌=1|𝑆=𝑆 1) (5)

LiDDA: Data Driven Attribution at LinkedIn
Test index ˆ𝑎exp ˆ𝑎𝐷𝐷𝐴 ˆ𝑑𝐷𝐷𝐴
1 9.68% (1.47%, 20.02%) 7.65% (4.95%, 10.07%) -2.23% (-5.85%, 0.06%)
2 14.05% (3.35%, 24.75%) 14.96% (11.78%, 18.24%) 0.95% (-0.89%, 2.25%)
3 12.54% (2.10%, 27.69%) 15.21% (11.65%, 19.34%) 2.41% (-0.38%, 5.05%)
Table 4: Experimental validation for 3 incrementality tests.
Each cell contains the point estimate and its corresponding
95% confidence intervals.
by plugging in ˆ𝑃1(𝑌=1|𝑆=𝑆 1)=( ˝ 𝑖:𝑍𝑖 =1𝑌𝑖)/(˝ 𝑖:𝑍𝑖 =1 1), and
ˆ𝑃1(𝑌=1|𝑆=𝑆 1−T ℎ)= ∑︁
𝑖:𝑍𝑖 =0
𝑤𝑖𝑌𝑖˝
𝑖:𝑍𝑖 =0𝑤𝑖
.(6)
For validation, we then compute theattention based attribution, i.e.,
ˆ𝑎𝐷𝐷𝐴(Tℎ)=
˝
𝑖:𝑍𝑖 =1
˝
𝑡∈T ℎ𝑎𝐷𝐷𝐴 𝑖 (𝑡)˝
𝑖:𝑍𝑖 =1 1 (7)
where𝑎𝐷𝐷𝐴 𝑖 (𝑡) is attention based attribution for member𝑖 for touch-
point𝑡. Further details, including validation of IPW and two addi-
tional attribution measures are available in Appendix B.5.
3.2.2 Experiment Results.We chose three incrementality tests in
the email channel to validate the attribution model and the primary
metric is attribution defined in eq. [3]. Our goal is to evaluate the
effectiveness of the acquisition email series. The comparisons are
listed in Table 4.
We compare DDA generated attribution ˆ𝑎𝐷𝐷𝐴 with "ground
truth" ˆ𝑎exp and compute their difference, i.e. ˆ𝑑𝐷𝐷𝐴 = ˆ𝑎𝐷𝐷𝐴− ˆ𝑎exp.
Confidence intervals of ˆ𝑎exp, ˆ𝑎𝐷𝐷𝐴 , and ˆ𝑑𝐷𝐷𝐴 were derived using
bootstrap sampling. We notice that the gaps between ˆ𝑎exp and
ˆ𝑎𝐷𝐷𝐴 are not statistically significant. We concluded that our DDA
attention based attribution aligns with the experimental result.
4 Application to LinkedIn Ads Measurement
The LiDDA model architecture was first applied to LinkedIn’s
GTM marketing. We have since integrated a variant of LiDDA into
LinkedIn’s Ad Platform to provide advertisers with comprehensive
funnel insights through LinkedIn Ads. Previously, measurement of
ad impact on the Ads platform heavily relied on last-touch attribu-
tion, which often undervalues upper-funnel ads, potentially result-
ing in suboptimal budget allocation. In contrast, data-driven attri-
bution distributes credit across multiple ad interactions throughout
the buyer’s journey, accounting for the impact of upper-funnel
advertising efforts on business outcomes.
When applying LiDDA to the LinkedIn Ads use case, we also
supply information about the advertiser, via a company embedding
for the advertiser. This is concatenated with embeddings represent-
ing the member and their company. Similar to our GTM marketing
model, we also include a touchpoint sequence representation (en-
coding the sequence of touch types, e.g., "Onsite lead generation
sponsored status update video ad impression"), touchpoint embed-
dings derived from campaign text, and positional encodings (rep-
resenting the time between each touchpoint and the conversion).
While GTM marketing has access to touchpoints across multiple
channels, the Ads platform currently only has access to LinkedIn
touchpoints. When applying the model to lead conversions ob-
tained through LinkedIn’s Lead Generation form, on average the
attribution weights show a time decay effect: touches closer to
the conversion tend to get more credit (Figure 4). Meanwhile, we
also observe the weight assigned to a specific touchpoint can vary,
influenced by factors like the objective type, ad format, interac-
tion type (impression, click), ad creative, days before conversion.
We surface these insights as both path-level detail and aggregated
campaign/creative reports (Details in Appendix B.6).
Figure 4: Attribution weights for LinkedIn lead conversions
show a time decay effect in aggregate; ad touches closer to
the conversion tend to get more credit.
5 Conclusion
In this paper, we introduce LiDDA, a unified transformer-based data-
driven attribution approach we developed and deployed at LinkedIn.
We demonstrated the innovations to DDA methodology that com-
bine an attention mechanism, positional embeddings, touchpoint
imputation, and MMM calibration. We also shared learnings from
implementation and deployment that are broadly applicable to the
marketing and ad tech fields.
Acknowledgments
We thank Licurgo Benemann De Almeida, Artem Grigoryan, GC
Chapiewski, Sabry Tozin, Shruti Sharma, Zaid Nasir, Anu Bedi,
Paolo Provinciali for support of the work.
References
[1] P.K. Kannan A. Li. 2014. Attributing Conversions in a Multichannel Online
Marketing Environment: An Empirical Model and a Field Experiment. 51:40-56,
02 pages.
[2] T. W. Anderson and D. A. Darling. 1952. Asymptotic Theory of Certain ’Goodness
of Fit’ Criteria Based on Stochastic Processes.The Annals of Mathematical
Statistics23, 2 (1952), 193–212. http://www.jstor.org/stable/2236446
[3] N.H. Borden. 1964. The Concept of the Marketing. 4, 2-7 pages.
[4] Gino Brunner, Yang Liu, Damian Pascual, Oliver Richter, Massimiliano Ciaramita,
and Roger Wattenhofer. 2020. On Identifiability in Transformers. In8th Interna-
tional Conference on Learning Representations (ICLR 2020)(virtual). International
Conference on Learning Representations.
[5] David Chan and Mike Perry. 2017.Challenges and Opportunities in Media Mix
Modeling. Technical Report.
[6] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2019. BERT:
Pre-training of Deep Bidirectional Transformers for Language Understanding.
arXiv:1810.04805 [cs.CL] https://arxiv.org/abs/1810.04805
[7] Facebook Experimental. [n. d.]. Robyn. https://facebookexperimental.github.io/
Robyn/

Bencina et al.
[8] Navid Mohammadi Foumani, Chang Wei Tan, Geoffrey I. Webb, and Mahsa
Salehi. 2023. Improving position encoding of transformers for multivariate time
series classification.Data Mining and Knowledge Discovery38, 1 (Sept. 2023),
22–48. doi:10.1007/s10618-023-00948-2
[9] Jitendra Gaur and Kumkum Bharti. 2020. Attribution modelling in marketing:
Literature review and research agenda.Academy of Marketing Studies Journal
24, 4 (2020), 1–21.
[10] Google. [n. d.]. Unified Marketing Measurement. The Power of Blending
Methodologies. https://www.thinkwithgoogle.com/_qs/documents/15401/
UnifiedMarketingMeasurement.pdf
[11] Miguel A Hernán and James M Robins. 2006. Estimating causal effects from
epidemiological data.Journal of Epidemiology & Community Health60, 7 (2006),
578–586.
[12] Sarthak Jain and Byron C. Wallace. 2019. Attention is not Explanation. In
Proceedings of the 2019 Conference of the North American Chapter of the Association
for Computational Linguistics: Human Language Technologies, Volume 1 (Long and
Short Papers), Jill Burstein, Christy Doran, and Thamar Solorio (Eds.). Association
for Computational Linguistics, Minneapolis, Minnesota, 3543–3556.
[13] Sachin Kumar, Garima Gupta, Ranjitha Prasad, Arnab Chatterjee, Lovekesh
Vig, and Gautam Shroff. 2020. Camta: Causal attention model for multi-touch
attribution. In2020 International Conference on Data Mining Workshops (ICDMW).
IEEE, 79–86.
[14] Ning li, Sai Kumar Arava, Chen Dong, Zhenyu Yan, and Abhishek Pani. 2018.
Deep Neural Net with Attention for Multi-channel Multi-touch Attribution.
arXiv:1809.02230 [cs.LG] https://arxiv.org/abs/1809.02230
[15] Andrew Whinston Lizhen Xu, Jason A. Duan. 2014. Path to Purchase: A mutually
exciting point process model for online advertising and conversion. 60(6):1392-
1412 pages.
[16] J. E. McCarthy. 1978. Basic marketing: a managerial approach.
[17] Sofia Serrano and Noah A Smith. 2019. Is Attention Interpretable?. InProceedings
of the 57th Annual Meeting of the Association for Computational Linguistics. 2931–
2951.
[18] Xuhui Shao and Lexin Li. 2011. Data-driven multi-touch attribution models.
InProceedings of the 17th ACM SIGKDD international conference on Knowledge
discovery and data mining. 258–264.
[19] Raghav Singal, Omar Besbes, Antoine Desir, Vineet Goyal, and Garud Iyengar.
2019. Shapley Meets Uniform: An Axiomatic Framework for Attribution in
Online Advertising. InThe World Wide Web Conference(San Francisco, CA,
USA)(WWW ’19). Association for Computing Machinery, New York, NY, USA,
1713–1723. doi:10.1145/3308558.3313731
[20] M. A. Stephens. 1974. EDF Statistics for Goodness of Fit and Some Comparisons.
J. Amer. Statist. Assoc.69, 347 (1974), 730–737. doi:10.2307/2286009
[21] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones,
Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin. 2017. Attention is all
you need.Advances in Neural Information Processing Systems(2017).
[22] Sarah Wiegreffe and Yuval Pinter. 2019. Attention is not not Explanation. In
Proceedings of the 2019 Conference on Empirical Methods in Natural Language Pro-
cessing and the 9th International Joint Conference on Natural Language Processing
(EMNLP-IJCNLP). 11–20.
[23] Di Yao, Chang Gong, Lei Zhang, Sheng Chen, and Jingping Bi. 2022. Causalmta:
Eliminating the user confounding bias for causal multi-touch attribution. In
Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and
Data Mining. 4342–4352.
[24] Ya Zhang, Yi Wei, and Jianbiao Ren. 2014. Multi-touch attribution in online
advertising with survival theory. In2014 ieee international conference on data
mining. IEEE, 687–696.
A Additional Details on Methods
A.1 Three-Step Member Impression Allocation
Let 𝑑 index days, 𝑐 index paid channels, 𝑗∈𝐽 𝑖,𝑐,𝑑 index click-
events for member 𝑖, and 𝑘∈ P𝑑 index no-click paths on day
𝑑. We observe external aggregates(𝐼 ext 𝑐,𝑑,𝐶 ext 𝑐,𝑑), owned-channel to-
tals(𝐼 own total,𝐶 own total,𝐼 own clickers,𝐶 own clickers), and a nonnegative weight𝑢𝑘 for
each no-click path.
A.1.1 Member-Only Impression Budget.Compute the number of
impressions on channel𝑐 and day𝑑 attributable to known members
by scaling the external impressions by the fraction of clicks from
members:
𝐶mem 𝑐,𝑑 = ∑︁
𝑖
|𝐽𝑖,𝑐,𝑑|, 𝐼 mem 𝑐,𝑑 =𝐼 ext 𝑐,𝑑 𝐶mem 𝑐,𝑑 𝐶ext 𝑐,𝑑 .
Summing over channels gives the total daily member-impression
budget:
𝐼𝑑 =
∑︁
𝑐
𝐼 mem 𝑐,𝑑 .
A.1.2 Impute and Pre-Allocate to Clicks.First, derive a down-
weight factor𝛼<1from owned-channel behavior:
𝑅own all = 𝐼 own total 𝐶own total , 𝑅 own clickers = 𝐼 own clickers 𝐶own clickers , 𝛼= 𝑅own clickers 𝑅own all .
Apply𝛼 to the raw external impressions-per-click to obtain the
clickers’ expected impressions per click on(𝑐,𝑑):
𝑅ext all = 𝐼 ext 𝑐,𝑑 𝐶ext 𝑐,𝑑 , 𝑟 𝑐,𝑑 =𝛼𝑅 ext all ≈E  #imps|click,𝑐,𝑑  .
Then allocate to each click 𝑗∈𝐽 𝑖,𝑐,𝑑 at least one impression by
either
𝑚𝑗 =max 1,⌊𝑟𝑐,𝑑⌋ (deterministic),
𝑚𝑗∼Geom 𝑝=1/𝑟 𝑐,𝑑  (stochastic),
and compute the pre-allocated sum and leftover:
𝐼 pre 𝑑 = ∑︁
𝑗
𝑚𝑗, 𝐿 𝑑 =𝐼𝑑−𝐼 pre 𝑑 .
A.1.3 Probabilistic Allocation of Leftover.Assign the remaining 𝐿𝑑
impressions across no-click paths𝑘∈P 𝑑 proportionally to weights
𝑢𝑘. Define
𝑝𝑘 = 𝑢𝑘˝
ℓ∈P𝑑𝑢ℓ
, 𝜆 𝑘 =𝐿𝑑𝑝𝑘.
Draw ˜𝐼𝑘∼Poisson(𝜆 𝑘) independently, then rescale to exactly ex-
haust𝐿𝑑:
𝐼𝑘 =
j
˜𝐼𝑘× 𝐿𝑑 ˝
ℓ ˜𝐼ℓ
k
,
∑︁
𝑘
𝐼𝑘 =𝐿𝑑.
A.1.4 Result.Each click-event 𝑗 receives𝑚𝑗≥ 1(on average 𝑟𝑐,𝑑),
each no-click path𝑘receives𝐼 𝑘≥0, and
∑︁
𝑗
𝑚𝑗 +
∑︁
𝑘
𝐼𝑘 =𝐼 𝑑,
so the member-impression budget is exactly allocated.
A.1.5 Remarks.We note that:
• Both Geometric distribution and Poisson distribution can
be approximated by Normal distribution if needed;
•𝑢 𝑘∝E

#imps|noClick,𝑘

can be assigned by contextual
information such as corresponding campaign audience and
location;
•𝑟 𝑐,𝑑 can be estimated with more complex methods, e.g.,
𝑟𝑖,𝑐,𝑑 =𝑓(𝑥 𝑖,𝑥𝑐,𝑥𝑑) via a NN that leverages both member
level data from owned channels and aggregate data from
external channels.

LiDDA: Data Driven Attribution at LinkedIn
A.1.6 Joint Convex-Optimization Formulation.Instead of treating
click allocation (Step 2) and leftover allocation (Step 3) separately,
we can solve them in one convex-optimization step.
Introduce: (i) Variables𝑥 𝑗 for the impressions assigned to click-
event 𝑗∈𝐽 ∗,∗,𝑑; (ii) Variables𝑦𝑘 for the impressions assigned to
no-click path𝑘∈P 𝑑; (iii) Total budget𝐼𝑑 from Step 1; (iv) Positive
weights
𝑤𝑗 =𝑟 𝑐(𝑗),𝑑
≈E[𝑚 𝑗], 𝑢 𝑘 ≥0
reflecting the expected imps-per-click and the no-click path priori-
ties.
We then solve the following optimization:
maximize
{𝑥𝑗},{𝑦𝑘}
∑︁
𝑗∈𝐽∗,∗,𝑑
𝑤𝑗 log(𝑥𝑗) +
∑︁
𝑘∈P𝑑
𝑢𝑘 log(𝑦𝑘)
subject to
∑︁
𝑗∈𝐽∗,∗,𝑑
𝑥𝑗 +
∑︁
𝑘∈P𝑑
𝑦𝑘 =𝐼 𝑑,
𝑥𝑗 ≥1, 𝑦 𝑘 ≥0.
KKT-based solution.The Karush–Kuhn–Tucker conditions imply
that at optimum there is a multiplier𝜆>0such that
𝑥𝑗 =max

1, 𝑤𝑗
𝜆

, 𝑦 𝑘 =𝑢𝑘 𝜆 ,
and𝜆must satisfy:
∑︁
𝑗
max

1, 𝑤𝑗
𝜆

+
∑︁
𝑘
𝑢𝑘
𝜆 =𝐼𝑑.(8)
Eq. 8 can be solved by Algorithm 3, with complexity𝑂(𝐽log(𝐽)).
To summarize, the solution:
1. Honors the total budget: ˝ 𝑗𝑥𝑗+ ˝ 𝑘𝑦𝑘 =𝐼𝑑.
2. Guarantees each click-bucket𝑥 𝑗≥1whenever𝑤 𝑗 >0.
3. Allocates impressions in proportion to the expected click demand
𝑤𝑗 and the no-click weights𝑢𝑘.
By choosing𝑤𝑗 =𝑟𝑐,𝑑 and𝑢𝑘 as in Steps 2–3, we recover a deter-
ministic analogue of the previous stochastic Geometric+Poisson
draws.
Figure 5: The top row shows an original path with all im-
pressions and clicks a member has interacted with prior to
making a conversion. We cannot collect any paid media im-
pressions due to privacy regulations like GDPR and CCPA,
and we use a fixed length for paths to use in modeling. The
middle row shows the same path after these interactions are
dropped. We impute probabilistic impressions into the paths
and group impressions from owned channels, LinkedIn Plat-
form as shown in the bottom row for modeling.
Algorithm 3Compute Optimal𝜆and Allocations
Input:Click-weights {𝑤𝑗}𝐽 𝑗=1, path-weights{𝑢𝑘}𝐾 𝑘=1, total bud-
get𝐼𝑑
Output:Impressions{𝑥 𝑗},{𝑦𝑘}
Sort𝑤(1)≥𝑤(2)≥···≥𝑤 (𝐽)
Compute𝑆𝑢← ˝𝐾 𝑘=1𝑢𝑘
𝑆𝑤← ˝𝐽 𝑗=1𝑤(𝑗)
for𝑚=0to𝐽do
𝑆(𝑚) 𝑤 ←𝑆 𝑤− ˝𝑚 𝑗=1𝑤(𝑗)
𝜆𝑚← 𝑆(𝑚) 𝑤 +𝑆𝑢 𝐼𝑑−𝑚
end for
Find the unique𝑚∗ such that
𝑤(𝑚∗) ≥𝜆 𝑚∗ and𝑤 (𝑚∗+1) <𝜆 𝑚∗,
with conventions𝑤(0) =∞,𝑤 (𝐽+1) =0.
𝜆←𝜆 𝑚∗
foreach click𝑗=1,...,𝐽do
𝑥𝑗←max 1, 𝑤𝑗/𝜆
end for
foreach path𝑘=1,...,𝐾do
𝑦𝑘←𝑢𝑘/𝜆
end for
Figure 6: Probabilistic touchpoints are imputed in paths in
two steps. First, we add impressions to existing proxy-click
events based on impression to click ratio of each channel.
Second, we distribute the remaining impressions across mem-
bers online each day.
A.2 Path Pre-processing
A.2.1 Sessionization.We group impressions from certain channels
in a path as a single touchpoint within a session if they are from the
same campaign on the same day, as detailed in Algorithm 4. This
helps reduce noise, particularly from on-platform channels where a
member may observe the same campaign repeatedly due to scrolling
behavior. With this approach, we model a single event; however,
we retain the downsampling links for post-model processing to
reallocate credit equally across the grouped events.
A.2.2 Downsampling.We further address signal bias by adjusting
the retention rate of specific channel–action combinations accord-
ing to tunable downsampling rates. We obtain these rates using an

Bencina et al.
independent analysis to estimate the comparable impact of each
channel using signals such as spend and outcomes. With these ra-
tios, we randomly "drop" some touchpoints to yield the expected ra-
tio as described in Algorithm 5. We observe that this pre-processing
step yields more reliable attribution results and path compositions
better aligned with aggregate data.
Our attribution system is complex and heterogeneous, as a result,
certain heuristics are necessary. Meanwhile, we perform compre-
hensive evaluation on these heuristics. For example, to downsample
owned channel activities, we estimate a scaling factor to bring the
number of actions, clicks/impressions, to the same order of magni-
tude of actions from other channels. And we evaluate the impact
through offline and online experiments.
Algorithm 4Sessionization methodology
Require:Member𝑝𝑎𝑡ℎwith marketing𝑡𝑜𝑢𝑐ℎ𝑝𝑜𝑖𝑛𝑡metadata
for𝑝𝑎𝑡ℎdo
Group all impressions by𝑐𝑎𝑚𝑝𝑎𝑖𝑔𝑛,𝑐ℎ𝑎𝑛𝑛𝑒𝑙, and𝑑𝑎𝑡𝑒
for𝑔𝑟𝑜𝑢𝑝do
Select most recent𝑡𝑜𝑢𝑐ℎ𝑝𝑜𝑖𝑛𝑡by timestamp
Record array of remaining𝑡𝑜𝑢𝑐ℎ𝑝𝑜𝑖𝑛𝑡
Store array in𝑡𝑜𝑢𝑐ℎ𝑝𝑜𝑖𝑛𝑡metadata
end for
Output truncated𝑝𝑎𝑡ℎwith linkage metadata
end for
Algorithm 5Downsampling methodology
Require:Member𝑝𝑎𝑡ℎwith marketing𝑡𝑜𝑢𝑐ℎ𝑝𝑜𝑖𝑛𝑡metadata
Require:Sampling𝑟𝑎𝑡𝑖𝑜per𝑎𝑐𝑡𝑖𝑜𝑛and𝑐ℎ𝑎𝑛𝑛𝑒𝑙pair
for𝑝𝑎𝑡ℎdo
Group all touchpoints by𝑎𝑐𝑡𝑖𝑜𝑛and𝑐ℎ𝑎𝑛𝑛𝑒𝑙
for𝑔𝑟𝑜𝑢𝑝do
Sort𝑡𝑜𝑢𝑐ℎ𝑝𝑜𝑖𝑛𝑡𝑠by timestamp
Compute number of𝑡𝑜𝑢𝑐ℎ𝑝𝑜𝑖𝑛𝑡𝑠 𝑁based on𝑟𝑎𝑡𝑖𝑜
Retain𝑁latest𝑡𝑜𝑢𝑐ℎ𝑝𝑜𝑖𝑛𝑡𝑠
end for
Output truncated𝑝𝑎𝑡ℎ
end for
A.3 Training Time Calibration
A.3.1 Batch-Level Calibration.Let a trainingbatchconsist of 𝑁
paths. Denote by
𝑎DDA 𝑖 (𝑐;𝜃)= ∑︁
𝑡∈𝑐
𝑎DDA 𝑖 (𝑡;𝜃),(𝑖=1,...,𝑁, 𝑐=1,...,𝐶)
the DDA model’s attribution share for channel𝑐on path𝑖. Define
the batch-aggregated channel totals
𝐴DDA 𝑐 (𝜃)= 1 𝑁 𝑁∑︁ 𝑖=1 𝑎DDA 𝑖 (𝑐;𝜃), 𝐴 MMM 𝑐 =𝑎 MMM 𝑐
where𝑎MMM 𝑐 is the global MMM-derived share for channel𝑐. We
then add one of the followingbatch-levelpenalties:
Mean-Squared Error (MSE) Penalty
Lbatch calib =
𝐶∑︁
𝑐=1

𝐴DDA 𝑐 (𝜃)−𝐴 MMM 𝑐
 2
;
Kullback–Leibler (KL) Penalty
Lbatch calib =
𝐶∑︁
𝑐=1
𝐴MMM 𝑐 ln 𝐴MMM 𝑐 𝐴DDA𝑐 (𝜃).
These terms are computed once per batch and combined with
the base DDA loss:
Ltotal =L DDA(𝜃) +𝛽L batch calib .
Backpropagation propagates gradients from the channel-sum resid-
uals into each𝑎 DDA 𝑖 (𝑐;𝜃).
A.3.2 Path-Level Calibration.For each path 𝑖, let𝜋(𝑖) 𝑐 be the em-
pirical fraction of touches in channel𝑐:
𝜋(𝑖) 𝑐 = #{touchpoints of𝑐in path𝑖} length(𝑖) .
Let𝜋 MMM 𝑐 be the probability of any touchpoint’s channel being𝑐
(i.e., estimate from all paths), and𝑎𝑀𝑀𝑀 𝑐 be the "attribution" of𝑐
from MMM. Define a per-path, per-channel weight
𝑤(𝑖) 𝑐 = 𝜋(𝑖) 𝑐
𝜋 MMM𝑐 .
Form the unnormalized target
˜𝑡(𝑖) 𝑐 =𝑤(𝑖) 𝑐 𝑎MMM 𝑐 ,
and then normalize to "recover" a valid path-level MMM attribution
𝑡(𝑖) 𝑐 = ˜𝑡(𝑖) 𝑐 ˝𝐶
𝑑=1 ˜𝑡(𝑖) 𝑑 ,
𝐶∑︁
𝑐=1
𝑡(𝑖) 𝑐 =1.
We then penalize the divergence between DDA’s prediction and
this target for each path:
Per-Path MSE
Lpath calib =
𝐶∑︁
𝑐=1

𝑎DDA 𝑖 (𝑐;𝜃)−𝑡 (𝑖) 𝑐
 2
.
Per-Path KL
Lpath calib =
𝐶∑︁
𝑐=1
𝑡(𝑖) 𝑐 ln 𝑡(𝑖) 𝑐 𝑎DDA 𝑖 (𝑐;𝜃) .
As before, the total loss is
Ltotal =L DDA(𝜃) +𝛽L path calib,
and gradients flow from each path-level residual into the DDA
model parameters𝜃.
Remarks on implementation:
(1) When there are padding in the path,𝜋𝑀𝑀𝑀 𝑐 needs to take
into account the padding, e.g.,𝜋𝑀𝑀𝑀 𝑐 = 1 N ˝ 𝑖𝜋(𝑖) 𝑐 if com-
putation of𝜋(𝑖) 𝑐 throws away the padding. Here,N denotes
the number of paths in the full dataset.

LiDDA: Data Driven Attribution at LinkedIn
(2) Since we applied scaling on the (theoretical IPW) tar-
get ˜𝑡, we can apply the weight back to the loss func-
tion when using the normalized target 𝑡, i.e., Lpath calib = ˝𝐶
𝑐=1𝑣(𝑖)

𝑎DDA 𝑖 (𝑐;𝜃)−𝑡 (𝑖) 𝑐
 2
.where,𝑣 (𝑖) = ˝𝐶 𝑑=1 ˜𝑡(𝑖) 𝑑 .
B Additional Offline Analysis
B.1 Model Stability
We provide visualizations of model stability on prediction and at-
tribution in Figure 7, Figure 8 and Figure 3.
Figure 7: The ROC-AUC and PR-AUC of the attributions
models retrained on 10 different subsets of training data and
evaluated on the same holdout dataset. The models’ perfor-
mances converge.
Figure 8: Anderson-Darling statistic comparing the distribu-
tion of conversion propensities each day to the distribution
from the day a week ago. Days where the propensity distri-
butions are significantly different are marked in red.
B.2 Attention Interpretability
When using attention weights in attribution, we would expect that
the computed weights quantify the contribution a touchpoint has
towards the prediction of a conversion outcome. Therefore, if we
were to modify the weight distribution we should observe a change
in the predicted outcome. In this test, we train two models on the
Figure 9: The plot compares the ROC-AUC against a common
holdout for both the baseline and modified attention models
in our study. The baseline model consists of 30 datapoints
with 1 validation step per trial. The modified model consists
of 300 datapoints with 10 validation steps per trial.
same dataset. The baseline model is trained using the standard at-
tention setup described in this paper. The modified model randomly
permutes the attention weights at a path-level during inference
forward passes.
We train both models for 10 epochs each using identical batch
sizes and hyperparameters. After training, we perform an inference
pass on a shared holdout dataset and measure ROC-AUC. For the
baseline model, we perform a single inference pass. For the modified
model, we perform 10 inference passes to capture the variance
introduced by the weight permutation process. We repeat this entire
process 30 times for each model.
In Figure 9, we observe that the baseline model generally yields
higher performance with a median ROC-AUC of 0.956 while the
modified model has a median ROC-AUC value of 0.928 (-2.93%).
While this is not a substantial change, we observe a larger negative
impact on the consistency of results. The AUCs of both models are
noted to be high. There are two explanations for this. One reason
is due to resampling of the data creating an artificially high rate of
conversions. The model is measured on uncalibrated results. Sec-
ondly, we note that in our domain, converting paths have a notably
different composition which facilitates an easier classification task.
In Figure 10, we plot the results of the 30 modified trials sorted
in median ascending order. 23 of the 30 trials ranked below the
20th percentile compared to the baseline model. We conclude from
this test that the introduction of weight noise has a material impact
on model performance and therefore provides some explainability
power.
B.3 Ablation
B.3.1 Methodology.We performed an ablation study to estimate
the contribution of different components of our model introduced
in this paper. We generated fixed training, validation, and inference
datasets to use across each simulation where a new model was
trained and inferenced with the indicated component removed. In
each simulation, the removal of the component was performed by

Bencina et al.
Figure 10: This plot shows the per-trial results for the modi-
fied model. The trials are sorted in ascending order according
to their median ROC-AUC value. We observe that 23 of the 30
models fall below the bottom 20th percentile of the baseline
trials.
modifying the code to omit the component from the graph. All
hyperparameters were held constant, and each model was trained
for 5 epochs.
After training, we evaluated the ROC-AUC metrics against the
validation dataset which contains a resampled population ratio of
non-converting to converting of 10:1. We also evaluated the attri-
bution weight distribution across channels for each of the models.
We tested the following components of the model:
• Baseline:The unmodified model as described in the paper
• No-Entity:Member and company embedding inputs re-
moved
• No-Campaign:Touchpoint campaign embedding inputs
removed
•No-Date:Touchpoint date embedding inputs removed
• Seq-Only:All embeddings removed leaving only the se-
quence and positional encoding
B.3.2 Classification Results.We first evaluated the ablation effects
on the final classification power of the model by comparing the
predicted model score to the ground-truth label. We note high nom-
inal AUC values as the simulations were performed on a resampled
dataset. We observe that there is a moderate performance loss for
the touchpoint level date and campaign features. Removal of entity
embeddings had a larger effect, and removal of all components had
the most negative effect. We also note that utilizing the sequence
only allows for substantial predictive power given that converting
members in our domain behave differently than non-converting
members.
B.3.3 Weight Results.We next evaluated the impact of the com-
ponent removal on the measured attribution credit across a group-
ing of our four marketing channel families. We compute the mean
squared deviation in total attribution from the baseline model across
the four channels as a measure of volatility in the ablation. We
observe that all ablations result in some changes to attribution how-
ever removing the dates alone causes the most significant shifts.
Version ROC-AUC % Change
1. Baseline 0.990 –
2. No-Campaign 0.989 -0.1%
3. No-Date 0.984 -0.3%
4. No-Entity 0.973 -1.7%
5. Seq-Only 0.939 -5.1%
Table 5: ROC-AUC performance measured on a constant val-
idation dataset after 5 epochs of training. Percentage change
vs. the baseline model is shown.
Version Mean Squared Deviation
1. Baseline –
2. No-Campaign 8.5
3. No-Date 49.3
4. No-Entity 14.4
5. Seq-Only 11.8
Table 6: The percent attribution allocated across four market-
ing channels is computed using the indicated LiDDA model
version. The absolute deviation for each channel vs. the base-
line model is computed. The reported number is the mean
squared deviation for that model, across all channels, com-
pared with the original baseline mix.
B.4 Model ROC-AUC Comparison
Additional comparison of ROC-AUC performance between
CausalMTA and LiDDA on common training dataset.
Table 7: ROC-AUC score (95% CI) comparison over 5 trials
using static training and validation datasets.
Model ROC-AUC Score
CausalMTA0.983±0.001
LiDDA0.982±0.000
B.5 Recovering Distribution
The inverse propensity score weight can help balance the converted
members in the treatment group and members in control group
for fairer comparison between model predicted conversions and
observed conversions from online experiments. In Figure 11, we
create weight-scaled pseudo-populations through𝑤𝑖 for those who
converted in the treatment group and for those in the control group.
We observe that IPW functions as expected to adjust the population
from converted members in the treatment group and control group
to a closer match.
Without IPW, we can calculate a raw estimate of𝑎raw(Tℎ), which
can be biased.
𝑎raw(Tℎ)= ˆ𝑃1(𝑌=1|𝑆=𝑆 1)− ˆ𝑃0(𝑌=1|𝑆=𝑆 1−T ℎ) ˆ𝑃1(𝑌=1|𝑆=𝑆 1) .
We also calculate a plug-in estimate ˜𝑎𝐷𝐷𝐴 of the attribution

LiDDA: Data Driven Attribution at LinkedIn
Figure 11: The top chart shows a mismatch between conver-
sion propensity score distribution for converted members in
the treatment group vs. control members. The bottom chart
shows that conversion propensity score distributions are bet-
ter matched in the pseudo-populations where we replicate
the members through𝑤 𝑖 to balance the two populations.
Test index𝑎 raw ˆ𝑎𝐷𝐷𝐴 ˜𝑎𝐷𝐷𝐴
1 8.72% (0.01%, 16.11%) 7.65% (4.95%, 10.07%) 12.54% (10.52%, 14.73%)
2 9.73% (1.71%, 17.75%) 14.96% (11.78%, 18.24%) 19.61% (16.81%, 23.44%)
3 16.65% (3.93%, 29.37%) 15.21% (11.65%, 19.34%) 9.54% (7.53%, 11.75%)
Table 8: Additional comparison for 3 incrementality tests.
Each cell contains estimated attribution and its correspond-
ing 95% confidence intervals.
with DDA model, similar to eq. [5]. Let 𝜋(𝑆) be the predicted
conversion for touchpoint sequence 𝑆 from DDA model, we can
compute ˜𝑃1(𝑌= 1|𝑆=𝑆 1)=( ˝ 𝑖:𝑍𝑖 =1𝜋(𝑆 1,𝑖))/(˝ 𝑖:𝑍𝑖 =1 1), and ˜𝑃1(𝑌= 1|𝑆=𝑆 1−T ℎ)=( ˝ 𝑖:𝑍𝑖 =1𝜋(𝑆 1,𝑖−T ℎ))/(˝ 𝑖:𝑍𝑖 =1 1). We
compared these two estimates with "ground truth" ˆ𝑎exp in Table 8.
B.6 Application to Ad Platform
Touchpoint-level attribution from LiDDA provides very granular
insights, where we see varying credit assignment to earlier touch-
points. In the provided examples in Figure 12, touches closer to
the conversion tend to have higher weights; however, the weight
assigned to a specific touchpoint can vary, influenced by factors
like the objective type, ad format, interaction type (impression,
click), ad creative, days before conversion, etc. Using these types
of signals, the model can learn to allocate credit across all touch-
points in the converting paths. This data can then be surfaced to
advertisers on LinkedIn’s Ad platform at different levels of aggre-
gation, in a variety of ways, including in the Campaign Manager
Reporting table (i.e., showing the number of conversions attributed
to each campaign, creative, etc.), and in a plot in Measurement In-
sights (showing a time series of conversions attributed to different
categories of campaigns).
Figure 12: The attribution weights extracted from the model
can provide granular insights. Here we show example at-
tribution weights for two LinkedIn lead conversions, as a
function of touches until conversion (x-axis) and touch type
(hue). While in aggregate we see a time-decay effect (i.e.,
touches closer to the conversion tend to get more credit), the
credit allocated to each touch in a given path can vary. For
example, in the bottom path, the initial blue touches receive
relatively more credit than the next few touches, and the
red "click" three touches before the conversion receives the
highest credit.
