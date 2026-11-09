---
title: Cross-Country Code-Mixing for Generative Recommendation
url: https://arxiv.org/abs/2609.28972
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Yuan Gao
- Hao Deng
- Haibo Xing
- Yi Xu
- Lingyu Mu
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.28972
pages: 6
chars: 33540
fetched_at: '2026-11-08T13:24:38+00:00'
kb_version: 1
---

# Cross-Country Code-Mixing for Generative Recommendation

Cross-Country Code-Mixing for Generative Recommendation
Yuan Gao∗
jianbei.gy@alibaba-inc.com
Alibaba International Digital
Commerce Group
Beijing, China
Hao Deng∗
denghao.deng@alibaba-inc.com
Alibaba International Digital
Commerce Group
Beijing, China
Haibo Xing
xinghaibo.xhb@alibaba-inc.com
Alibaba International Digital
Commerce Group
Beijing, China
Yi Xu
xy397404@alibaba-inc.com
Alibaba International Digital
Commerce Group
Beijing, China
Lingyu Mu
moulingyu.mly@alibaba-inc.com
Alibaba International Digital
Commerce Group
Beijing, China
Jinxin Hu†
jinxin.hjx@alibaba-inc.com
Alibaba International Digital
Commerce Group
Beijing, China
Yu Zhang
daoji@alibaba-inc.com
Alibaba International Digital
Commerce Group
Beijing, China
Xiaoyi Zeng
yuanhan@taobao.com
Alibaba International Digital
Commerce Group
Hangzhou, China
Abstract
Cross-country recommendation on modern e-commerce platforms
is typically deployed with disjoint user and item ID spaces across
markets, removing the shared anchors that conventional cross-
domain methods rely on. Generative recommendation (GR) miti-
gates this by mapping items into a shared token space and training
a unified model, but existing approaches keep behavior sequences
strictly country-specific, so knowledge transfer occurs only at the
parameter level and remains absent at the data level. Inspired by
code-switching corpora in multilingual natural language process-
ing, we proposeCMRec, a cross-country GR framework that injects
cross-country supervision at the data level via dual-constrained,
context-aware code-mixing.CMRecfirst learns a shared semantic
codebook from multi-modal content and behavioral co-occurrence
across countries. It then uses this codebook to synthesize mixed-
country sequences via token-level substitutions that satisfy both
static (content) and dynamic (e.g., price, audience, popularity) con-
straints. Finally, it introduces a context-aware loss that reweights
mixed samples according to their plausibility in the current se-
quence. Experiments on two real-world multi-country datasets and
an online A/B test show thatCMRecsubstantially improves rec-
ommendation quality in data-sparse countries while preserving
performance in data-rich countries, achieving+1.77%advertising
revenue and+2.64%orders on a large-scale e-commerce platform.
∗Both authors contributed equally to this research.
†Corresponding author.
This work is licensed under a Creative Commons Attribution 4.0 International License.
CIKM ’26, Rome, Italy
©2026 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-2539-5/2026/11
https://doi.org/10.1145/3799682.3839862
CCS Concepts
•Information systems→Recommender systems.
Keywords
Generative Recommendation, Cross Country, Code Mixing
ACM Reference Format:
Yuan Gao, Hao Deng, Haibo Xing, Yi Xu, Lingyu Mu, Jinxin Hu, Yu Zhang,
and Xiaoyi Zeng. 2026. Cross-Country Code-Mixing for Generative Rec-
ommendation. InProceedings of the 35th ACM International Conference on
Information and Knowledge Management (CIKM ’26), November 07–11, 2026,
Rome, Italy.ACM, New York, NY, USA, 6 pages. https://doi.org/10.1145/
3799682.3839862
1 Introduction
Modern e-commerce platforms increasingly operate across many
countries [18, 26, 28]. In practice, each country is deployed and
logged as an independent system: user interactions are recorded
only within a single country, and both user and item ID spaces
are maintained separately [24]. Consequently, both IDs and behav-
ior sequences are strictly partitioned by country, with no natural
overlap across countries, as illustrated in Figure 1 (a).
This setup differs from the well-studied cross-domain recommen-
dation (CDR) setting [9, 16, 30, 32, 33], where knowledge transfer
typically relies on some form of overlap across domains, such as
shared users, shared items, or manually anchored entities that carry
collaborative signals. Recent CDR methods based on generative
recommendation (GR), such as GenCDR [10] and GMC [13], relax
this ID-level requirement by mapping items from different domains
into a shared semantic token space and training a unified generative
model. In this way, knowledge transfer occurs at theparameter
level, mediated by the shared backbone and token space. However,
GR learns primarily from item co-occurrence within training se-
quences [8, 12, 19]. In the cross-country setting, these sequences
remain strictly partitioned by country, so items from one country
arXiv:2609.28972v1  [cs.IR]  24 Sep 2026

CIKM ’26, November 07–11, 2026, Rome, Italy Yuan Gao et al.
Item 1B Item 2B
Item 2BItem 1C
Item 4B
Item 4B
Item 3B
a. Cross Country Setting b. Code-Mixing with Two Challenges
 Original
 Sequence
 Code-Mixing
 Sequence
Country CCountry B
Country A
Item 2A
Item Level Similarity?
Context Plausible?
∩=∅
∩=∅ ∩=∅
Figure 1: (a) Cross-country setting. (b) Example and chal-
lenges of cross-country behavior-sequence code-mixing.
never appear in another country’s context, leaving cross-country re-
inforcement absent at thedata level. Consequently, rich interaction
signals in large markets cannot benefit small ones, and the potential
for cross-country knowledge sharing remains largely untapped.
A natural reference comes from multilingual natural language
processing (NLP), where models learn cross-lingual alignment from
code-switched corpora, in which tokens from different languages
appear in the same training sequence [2, 3, 17]. Motivated by this,
we investigate whether an analogous construction is possible for
cross-country GR, by building mixed-country sequences that in-
terleave items from different markets, as illustrated in Figure 1 (b).
However, no such corpus exists naturally; it must besynthesized
by substitution. This raises a recommendation-specific question:
what counts as a valid substitute?Existing substitution-based aug-
mentation methods [5, 20, 25], mostly developed for CDR settings,
match items by content (e.g., titles, descriptions, images) and replace
them in user sequences. Such recipes can in principle be applied
to cross-country GR, but they fall short along two complementary
axes.(a) Substitution criteria are incomplete at the item level.
Content similarity alone ignores two critical signals:behavioral(e.g.,
co-purchase and co-click patterns) andmarket(e.g., price, audience,
popularity). Two items that look similar can play very different
roles across markets [24], so a content-only criterion injects sub-
stantial noise.(b) Substitution granularity is too coarse at the
context level.Even if a candidate is reasonable in isolation, it
may still conflict with the user’s current intent. For example, in a
sequence dominated by Apple devices, swapping an item with an
Android pad that looks similar in content and basic attributes is
syntactically plausible but contextually wrong, and this cannot be
detected by any offline item-pair filter.
To address these limitations, we proposeCMRec, a cross-country
GR framework that injects cross-country supervision at the data
level via dual-constrained, context-aware code-mixing.CMRecfirst
learns a shared semantic codebook from multi-modal content and
behavioral co-occurrence across countries, which serves as both
the GR tokenizer and a common semantic space for cross-country
substitution. On top of this codebook, we perform token-level, dual-
constrained code-mixing: substitutions are applied to semantic to-
ken sequences rather than country-specific item IDs, and candidates
must satisfy both static (content) and dynamic (e.g., price, audience,
popularity) constraints, enabling finer-grained, market-aware cross-
country mixing. Finally, we introduce a context-aware loss that lets
the GR model reweight mixed samples according to their plausi-
bility in the current context, downweighting noisy substitutions
while preserving useful cross-country signals. We conduct experi-
ments on two real-world multi-country datasets and an online A/B
test, achieving improvements of+1.77% advertising revenueand
+2.64% orders, demonstrating the practical effectiveness ofCMRec
in production.
2 Problem Formulation
We consider cross-country recommendation over a country setC,
where each 𝑐∈C is an independent domain with disjoint user and
item setsU(𝑐) andI(𝑐) (i.e.,U(𝑐)∩U(𝑐′) =I(𝑐)∩I(𝑐′) =∅ for
𝑐≠𝑐 ′). For each user𝑢∈U (𝑐) , we denote the interaction sequence
as 𝑥𝑐 =(𝑖 1, . . . , 𝑖𝑇) with 𝑖𝑡∈I (𝑐) , and the target item as 𝑦𝑐∈I (𝑐) .
Following the GR paradigm [23, 26], we map each item to a discrete
token sequence via a codebook and formulate recommendation as
conditional sequence generation in this unified token space. Let
D(𝑐) ={(𝑥 𝑐, 𝑦𝑐)} collect the per-country training pairs from users
𝑢∈U (𝑐) . For joint multi-country training, we pool samples from
all countries into a unified setD= — 𝑐∈CD(𝑐) ={(𝑥, 𝑦)} , on which
the GR model is trained to maximize
LGR(𝜃)=
∑︁
(𝑥,𝑦)∈D
log𝑃 𝜃(𝑦|𝑥),(1)
where𝜃are the model parameters.
3 Method
We train a unified cross-country GR model that shares information
across countries while respecting country-specific dynamics. To
this end,CMReccomprises three components: (i) a shared semantic
codebook that tokenizes items from all countries using behavior
and content signals; (ii) a dual-constrained code-mixing mechanism
that substitutes tokens across countries under static and dynamic
constraints; and (iii) a context-aware loss reweighting scheme that
downweights noisy mixed samples during training.
3.1 Behavior- and Content-Grounded Shared
Codebook
To enable a unified cross-country GR backbone, we first construct
a shared semantic codebook that is informed by both multi-modal
content and behavioral signals. This codebook serves two roles at
once: it tokenizes items for GR and provides a common semantic
space for cross-country token substitution.
We first encode each item’s multimodal side information (e.g., ti-
tle, image) into a content embeddingm𝑖 using a pretrained model [1]
shared across countries. This provides a unified semantic space
where items from all countries are comparable at the content level.
However, content alone does not capture how items actually behave
in each country: items with similar visuals can have very different
popularity or co-occurrence patterns, and these behavior signals
are implicitly embedded in user interaction sequences. [22, 29]
To inject such behavioral information, we further train a single
behavior-driven item-to-item (i2i) alignment model jointly across
countries. On top ofm 𝑖, we adopt a two-tower architecture with
sampled softmax [7, 27]: the user tower maps a behavior sequence
to a user embeddingu 𝑖, and the item tower mapsm 𝑖 to an item

Cross-Country Code-Mixing for Generative Recommendation CIKM ’26, November 07–11, 2026, Rome, Italy
p𝜃(y|x)+p𝜃(y'|x)
p𝜃(y'|x)c(y, y'|x) = [Sg [Enc Dec
Part 3.Context-Aware Adapative Reweighting
x' 𝑦′
 ≥ 𝜏𝑠(0.8, 0.1, 0.3)
 ≤𝜏  ≤ 𝜏𝑠(0.1, 0.5, 0.7)
 ≤𝜏
 ≥ 𝜏𝑠(0.8, 0.3, 0.4)
 ≥𝜏
d(qi, qj) ≤ 𝜏
sim(si, sj) ≥ 𝜏𝑠  (0.9, 0.2, 0.3)
Token Seq
Side-info Emb
N𝜏,𝜏𝑠 (𝑖)
AND
Φ𝜏,𝜏s,𝑘 : (x, 𝑦) ↦ (x′, 𝑦′)
Specific of operator Φ
Marks k ratio random positions in x and the target y
x
Original Sequence
Code-Mixing Sequence
𝑦
Sample
Part 1: Shared Codebook Part 2. Dual-Constrained Cross-Country
Code-Mixing
mi
Multimodel
Encoder
Country C
Country B
Country A
ui
...
ei qi
Item
Tower
User
Tower
Li2i
Quantizer
(e.g. RQ-V AE)
(x, y)
(k, v)
𝑃𝜃 (𝑦 | x)
𝑃𝜃 (𝑦' | x')
 L = -∑ log 𝑃𝜃 (𝑦 | x)
  -𝜆∑𝑐· log 𝑃𝜃 (𝑦' | x')
(x', y')
Figure 2: Overview ofCMRec. Part 1 learns a shared semantic codebook from multimodal content and behavioral i2i co-
occurrence, producing token sequencesq 𝑖 that are used by the GR model. Part 2 uses the codebook plus side-info to select
cross-country neighbors and grafts them into the user sequence, yielding a code-mixed twin (x′, 𝑦′). Part 3 lets the GR model
itself reweight each twin by its plausibility under the original context, downweighting noisy substitutions during training.
embeddinge 𝑖 =𝑇(m 𝑖). The joint i2i training objective is
Li2i =−
∑︁
𝑖
log exp(u⊤ 𝑖 e𝑖+) exp(u⊤ 𝑖 e𝑖+)+ ˝ 𝑗∈N 𝑖 exp(u⊤ 𝑖 e𝑗) ,(2)
where the negative poolN𝑖 is shared across countries [11], soe 𝑖
aligns items that are both content-similar and behaviorally similar
in user interaction patterns.
We then apply a residual quantizer (e.g., RQ-VAE [23]) to trans-
form{e𝑖} into shared token sequencesq 𝑖 =(𝑞 (1) 𝑖 , . . . , 𝑞(𝑀) 𝑖 ). These
tokens form a unified codebook that we use both as the GR tokenizer
and as the substrate for cross-country code-mixing.
3.2 Dual-Constrained Cross-Country
Code-Mixing
With the shared codebook in place, items from different countries
can be matched in a common token space. We now introduce cross-
country code-mixing at the token level to expose GR to mixed
sequences across countries.
A naive approach would substitute items based only on their
codebook representations. However, the codebook is updated only
infrequently and does not capture fast-changing attributes such
as price discount, popularity, and audience tags, which are crucial
for deciding whether two items are interchangeable in practice.
To address this, we adopt a dual-constrained filter. Each item𝑖 is
equipped with a side-information embeddings 𝑖 over these dynamic
attributes, with each element discretized by per-country quantile
bucketization so that values from different countries are placed on
a comparable scale, and we define the cross-country candidate set
as
ˆN𝜏,𝜏𝑠(𝑖)=
n
𝑗∈
Ø
𝑐′≠𝑐
I(𝑐′)

 𝑑(q 𝑖,q 𝑗)≤𝜏∧sim(s 𝑖,s 𝑗)≥𝜏 𝑠 o ,(3)
where 𝑑 is the Hamming distance [4] between token sequences and
simis cosine similarity, enforcing static and dynamic consistency.
Given a training pair (x, 𝑦), the operator Φ𝜏,𝜏𝑠 ,𝑘 : (x, 𝑦) ↦→
(x′, 𝑦′) replaces the items at a rate- 𝑘 fraction of slots inxand
𝑦 with neighbors drawn from ˆN𝜏,𝜏𝑠(·), leaving the rest intact while
injecting cross-country co-occurrence at the token level. We then
apply Φ to a rate-𝑝 subsample ofD to form the twin setD′, with
𝑝controlling the cross-country mixing strength.
3.3 Context-Aware Adaptive Reweighting
The filter ˆN𝜏,𝜏𝑠 ensures item-level plausibility, but it is blind to
the user context and to how the model’s predictions evolve during
training. Some synthetic substitutions can still be incompatible with
the surrounding sequence, especially in long and noisy histories. We
therefore let the GR model itself assess each substituted item during
training. For a substituted example(x′, 𝑦′) derived from an original
pair(x, 𝑦), we define the context-conditional substitutability as
𝑤(𝑦, 𝑦′|x)=sg
 𝑃𝜃(𝑦′|x)
𝑃𝜃(𝑦|x)+𝑃 𝜃(𝑦′|x)

∈[0,1],(4)
where 𝑃𝜃(· |x) is the autoregressive item likelihood under the
original context and sg[·] denotes stop-gradient, so 𝑤 affects the
loss but does not receive gradients. We deliberately evaluate 𝑦′
under the original contextxrather than the mixedx ′, since 𝑃𝜃 is
better calibrated on the observedx; this prevents 𝑤 from being
dominated by the model’s unstable response to out-of-distribution
synthetic substitutions early in training.
We then combine original and substituted supervision in the
training objective:
L(𝜃)=−
∑︁
(x,𝑦)∈D
log𝑃 𝜃(𝑦|x)−𝜆
∑︁
(x′,𝑦′)∈D′
𝑤(𝑦, 𝑦′|x)log𝑃 𝜃(𝑦′|x′),
(5)
where 𝜆 controls the overall contribution of substituted examples.
Because 𝑤 is derived from the model’s own predictions, it acts as a
context-aware weight: early in training most substitutions receive
similar weights, while later the model downweights contextually
invalid substitutes that the item-level filter cannot distinguish.

CIKM ’26, November 07–11, 2026, Rome, Italy Yuan Gao et al.
Table 1: Performance comparison on the industrial and Amazon M2 datasets. Each metric reports the 6-country/locale average
(Avg6) plus three representative ones, with superscripts 𝐿/𝑀/𝑆 marking large/medium/small volume (Amazon M2 has no 𝑀 tier).
Best results are in bold and second-best are underlined . “Improv.” shows the relative improvement (%) over the best baseline.
Method Recall@10 Recall@100 NDCG@10 NDCG@100
(a) Industrial Dataset (6 countries)
Avg6 A 𝐿 B𝑀 C𝑆 Avg6 A 𝐿 B𝑀 C𝑆 Avg6 A 𝐿 B𝑀 C𝑆 Avg6 A 𝐿 B𝑀 C𝑆
SASRec 0.1882 0.1993 0.1867 0.1705 0.2648 0.2807 0.2632 0.2404 0.0941 0.0995 0.0933 0.0853 0.1458 0.1546 0.1448 0.1322
HSTU 0.2117 0.2244 0.2098 0.1929 0.2983 0.3158 0.2957 0.2725 0.1058 0.1122 0.1049 0.0964 0.1642 0.1738 0.1629 0.1498
TIGER 0.2261 0.2396 0.2243 0.2062 0.3187 0.3377 0.3163 0.2909 0.1131 0.1198 0.1122 0.1031 0.1753 0.1858 0.1739 0.1600
REG4Rec 0.2372 0.2517 0.2354 0.2163 0.3342 0.3537 0.3318 0.3057 0.1187 0.1258 0.1177 0.1082 0.1838 0.1949 0.1824 0.1681
GenCDR 0.2423 0.2493 0.2407 0.2247 0.3413 0.3562 0.3393 0.3168 0.1212 0.1246 0.1204 0.1123 0.1877 0.1961 0.1866 0.1743
GenCDR+Cont 0.2404 0.2456 0.2371 0.2311 0.3432 0.3496 0.3359 0.3248 0.1202 0.1227 0.1186 0.1156 0.1891 0.1928 0.1847 0.1793
GenCDR+CF 0.2384 0.2528 0.2378 0.2256 0.3412 0.3575 0.3387 0.3179 0.1182 0.1264 0.1192 0.1109 0.1871 0.1969 0.1853 0.1768
CMRec0.2496 0.2567 0.2494 0.2434 0.3613 0.3672 0.3567 0.3474 0.1236 0.1278 0.1239 0.1198 0.1972 0.2018 0.1957 0.1919
Improv.+3.01% +1.54% +3.61% +5.32% +5.27% +2.71% +5.13% +6.96% +1.98% +1.11% +2.91% +3.63% +4.28% +2.49% +4.88% +7.03%
(b) Amazon M2 Dataset (6 locales)
Avg6 UK 𝐿 FR𝑆 ES𝑆 Avg6 UK 𝐿 FR𝑆 ES𝑆 Avg6 UK 𝐿 FR𝑆 ES𝑆 Avg6 UK 𝐿 FR𝑆 ES𝑆
SASRec 0.2774 0.2293 0.3028 0.3095 0.4823 0.3986 0.5274 0.5389 0.1388 0.1147 0.1516 0.1548 0.2653 0.2192 0.2898 0.2963
HSTU 0.3212 0.2654 0.3506 0.3584 0.5584 0.4618 0.6099 0.6236 0.1606 0.1327 0.1753 0.1792 0.3070 0.2539 0.3354 0.3428
TIGER 0.3406 0.2816 0.3719 0.3803 0.5926 0.4898 0.6471 0.6616 0.1703 0.1408 0.1861 0.1902 0.3258 0.2694 0.3559 0.3638
REG4Rec 0.3523 0.2916 0.3846 0.3931 0.6124 0.5066 0.6688 0.6843 0.1762 0.1458 0.1921 0.1964 0.3369 0.2786 0.3679 0.3764
GenCDR 0.3603 0.2894 0.3928 0.4009 0.6266 0.5186 0.6839 0.6994 0.1798 0.1447 0.1963 0.2004 0.3446 0.2852 0.3761 0.3848
GenCDR+Cont 0.3579 0.2862 0.3907 0.3991 0.6291 0.5149 0.6893 0.7063 0.1784 0.1432 0.1951 0.1997 0.3463 0.2831 0.3793 0.3884
GenCDR+CF 0.3559 0.2922 0.3884 0.3961 0.6271 0.5198 0.6862 0.7035 0.1764 0.1465 0.1942 0.1985 0.3443 0.2860 0.3781 0.3865
CMRec0.3748 0.2997 0.4137 0.4203 0.6671 0.5379 0.7432 0.7588 0.1847 0.1484 0.2033 0.2068 0.3637 0.2953 0.4058 0.4136
Improv.+4.02% +2.57% +5.32% +4.84% +6.04% +3.48% +7.82% +7.43% +2.73% +1.30% +3.57% +3.19% +5.03% +3.25% +6.99% +6.49%
4 Experiments
4.1 Experimental Settings
Datasets & Evaluation Metrics.We evaluateCMRecontwo
multi-country datasetswith highly imbalanced data distribu-
tions. The first is an in-house industrial advertising dataset from
an e-commerce platform. It contains over 1 billion interactions
from 19 million users across 25 million advertisements across 6
countries (A–F). The largest country contributes about 10× more
training interactions than the smallest, and user and item IDs are
completely disjoint across countries. The second is Amazon M2 [14],
the public KDD Cup 2023 multilingual session benchmark cover-
ing 6 locales (high-resource: UK/DE/JP; low-resource: IT/FR/ES).
The high-resource locales account for roughly 91% of all training
sessions, yielding a pronounced long-tail distribution. For offline
evaluation, we report Recall@10/100 and NDCG@10/100 [7, 23] for
each representative country/locale, and also report averages over
all countries/locales.
Baselines & implementation.We compare with five represen-
tative methods plus two augmented variants: SASRec [15], GenCDR [10],
REG4Rec [26], HSTU [31], and TIGER [23]. To study single-signal
data augmentation, we follow SRA-CL [ 5] and build a content-
augmented variant on top of GenCDR, denoted GenCDR+Cont. We
also follow CoSeRec [21] and TiCoSeRec [6] to build a collaboration-
augmented variant based on user-behavior signals, denoted GenCDR+CF.
Both augmented variants use the same substitution ratio and sam-
pling budget asCMRecfor a controlled comparison. All baselines
follow their original designs and are trained on the same dataset
partition. ForCMRec, we first encode each item’s content into a
64-dimensional vector using Qwen-VL-32B [1]. We then tokenize
this vector with an RQ-VAE [23] into a token sequence of length
𝐿= 4. We adopt GenCDR as the backbone. We set 𝑝= 0.1and
𝑘= 0.1to balance performance and computational cost. We further
set 𝜆= 0.5and use relatively strict filtering thresholds, 𝜏= 1and
𝜏𝑠 =0.8.
4.2 Experimental Results
Overall performance.Table 1 summarizes the main results, from
which we draw three observations. (1)CMRecachieves the best
Recall@10/100 and NDCG@10/100 on both datasets on all six
countries, outperforming all baselines. (2) Token-based GR models
(REG4Rec, GenCDR) outperform ID-based models (SASRec, HSTU),
showing that tokenization and cross-country parameter sharing
provide a stronger backbone, especially for small countries. (3)
Single-signal augmentations based only on content or collaboration
improve some countries but degrade others, whileCMReccombines
dual-constrained code-mixing with context-aware reweighting and
delivers more consistent gains across all countries.
Ablation study.We conduct an ablation study on three compo-
nents ofCMRecin Table 2: the token-level distance constraint,
the side-information similarity constraint, and the context-aware
reweighting. The token-level distance constraint contributes the
largest improvement, indicating that codebook proximity is cru-
cial for transferring cross-country behavioral structure. The side-
information similarity constraint further refines substitutions by
Table 2: Ablation on the Industrial dataset (6-country avg.).
Numbers in parentheses are relative gaps vs. Full.
Variant Recall@100 NDCG@100
CMRec(Full) 0.3613 0.1972
w/o Token-level distance constraint 0.3447 (−4.59%) 0.1894 (−3.96%)
w/o Side-info Similarity constraint 0.3573 (−1.11%) 0.1947 (−1.27%)
w/o Context-aware Adaptive Reweighting 0.3531 (−2.27%) 0.1928 (−2.23%)

Cross-Country Code-Mixing for Generative Recommendation CIKM ’26, November 07–11, 2026, Rome, Italy
0% 5% 10% 15% 30%
Substitution ratio p
0.3325
0.3350
0.3375
0.3400
0.3425
0.3450Recall@100
(a) Reg4Rec
0% 5% 10% 15% 30%
Substitution ratio p
0.340
0.345
0.350
0.355
0.360
(b) GenCDR
k = 10%
k = 20%
k = 30%
Figure 3: Sensitivity to 𝑝 and 𝑘 on Industrial (Recall@100,
Avg6). Dashed line = baseline.
enforcing multi-modal coherence. Removing adaptive reweighting
leads to clear degradation, showing that it effectively filters samples
whose mixed tokens are incompatible with the original context.
Hyperparameter sensitivity and robustness.To validate sen-
sitivity and robustness of our method, we sweep (𝑝, 𝑘) for our
dual-constrained code-mixing on two backbones (Figure 3). On
both backbones, all(𝑝, 𝑘) combinations consistently outperform the
un-augmented baseline, and the default(𝑝=10%, 𝑘=10%)achieves
near-optimal Recall@100 in both cases, confirming that the aug-
mentation is robust to both hyperparameter and backbone choice.
Online Experiments.We conducted an online A/B test on the
industrial platform (10% live traffic) from May 10 to 20, 2026, cov-
ering all six countries.CMRecachieved a consistent increase of
1.77%inadvertising revenueand2.64%inorderson the six-
country aggregate, demonstrating significant gains in real-world
deployment.
5 Conclusion
We presentedCMRec, a cross-country generative recommenda-
tion (GR) framework that injects cross-country supervision at the
data level through dual-constrained code-mixing.CMReclearns a
shared semantic codebook from multi-modal content and behav-
ioral co-occurrence across countries. It then performs token-level
code-mixing under content-based and market-aware constraints
to synthesize reliable mixed-country sequences without requiring
item or user overlap. A context-aware loss reweights mixed samples
by their contextual plausibility. This suppresses noisy substitutions
while preserving useful cross-country signals. Extensive experi-
ments on offline datasets and an online multi-country e-commerce
platform show thatCMRecachieves superior performance, effec-
tively transfers knowledge from large to small countries, and offers
practical insights for cross-country generative recommendation.
6 GenAI Usage Disclosure
Generative AI was used in the preparation of this paper to assist
with language polishing, grammar checking, and improving the
clarity of the presentation. All technical ideas, including the de-
sign of the method, the implementation of experiments, and the
interpretation of results, are solely contributed by the authors.
References
[1] Shuai Bai, Keqin Chen, Xuejing Liu, Jialin Wang, Wenbin Ge, Sibo Song, Kai
Dang, Peng Wang, Shijie Wang, Jun Tang, Humen Zhong, Yuanzhi Zhu, Mingkun
Yang, Zhaohai Li, Jianqiang Wan, Pengfei Wang, Wei Ding, Zheren Fu, Yiheng
Xu, Jiabo Ye, Xi Zhang, Tianbao Xie, Zesen Cheng, Hang Zhang, Zhibo Yang,
Haiyang Xu, Junyang Lin, et al . 2025. Qwen2.5-VL Technical Report.arXiv
preprint arXiv:2502.13923(2025).
[2] Terra Blevins and Luke Zettlemoyer. 2022. Language Contamination Helps
Explains the Cross-lingual Capabilities of English Pretrained Models. InProceed-
ings of the 2022 Conference on Empirical Methods in Natural Language Processing
(EMNLP). Association for Computational Linguistics, Abu Dhabi, United Arab
Emirates, 3563–3574. doi:10.18653/v1/2022.emnlp-main.233
[3] Eleftheria Briakou, Colin Cherry, and George Foster. 2023. Searching for Needles
in a Haystack: On the Role of Incidental Bilingualism in PaLM’s Translation
Capability. InProceedings of the 61st Annual Meeting of the Association for Compu-
tational Linguistics (ACL), Volume 1: Long Papers. Association for Computational
Linguistics, Toronto, Canada, 9432–9452. doi:10.18653/v1/2023.acl-long.524
[4] Timothy M Chan, Shay Golan, Tomasz Kociumaka, Tsvi Kopelowitz, and Ely
Porat. 2020. Approximating text-to-pattern Hamming distances. InProceedings
of the 52nd Annual ACM SIGACT Symposium on Theory of Computing. 643–656.
[5] Ziqiang Cui, Yunpeng Wu, Lin Bai, Yueqi Wang, Xin Zhao, Xinyu Lin, Wenjie
Wang, Fuli Feng, and Tat-Seng Chua. 2025. Semantic Retrieval Augmented
Contrastive Learning for Sequential Recommendation. InAdvances in Neural
Information Processing Systems.
[6] Yizhou Dang, Enneng Yang, Guibing Guo, Linying Jiang, Xingwei Wang, Xiaoxiao
Xu, Qinghui Sun, and Hong Liu. 2023. Uniform Sequence Better: Time Interval
Aware Data Augmentation for Sequential Recommendation. InProceedings of the
AAAI Conference on Artificial Intelligence.
[7] Hao Deng, Haibo Xing, Kanefumi Matsuyama, Moyu Zhang, Jinxin Hu, Hong
Wen, Yu Zhang, Xiaoyi Zeng, and Jing Zhang. 2025. CSMF: Cascaded Selective
Mask Fine-Tuning for Multi-Objective Embedding-Based Retrieval. InProceedings
of the 48th International ACM SIGIR Conference on Research and Development in
Information Retrieval. 2122–2131.
[8] Yupeng Hou, An Zhang, Leheng Sheng, Zhengyi Yang, Xiang Wang, Tat-Seng
Chua, and Julian McAuley. 2025. Generative Recommendation Models: Progress
and Directions. InCompanion Proceedings of the ACM on Web Conference 2025.
13–16.
[9] Peiyu Hu, Wayne Lu, and Jia Wang. 2026. From IDs to Semantics: A Generative
Framework for Cross-Domain Recommendation with Adaptive Semantic Tok-
enization. InProceedings of the AAAI Conference on Artificial Intelligence (AAAI).
AAAI Press, Philadelphia, PA, USA.
[10] Peiyu Hu, Wayne Lu, and Jia Wang. 2026. From ids to semantics: A generative
framework for cross-domain recommendation with adaptive semantic tokeniza-
tion. InProceedings of the AAAI Conference on Artificial Intelligence, Vol. 40.
14874–14882.
[11] Jui-Ting Huang, Ashish Sharma, Shuying Sun, Li Xia, David Zhang, Philip Pronin,
Janani Padmanabhan, Giuseppe Ottaviano, and Linjun Yang. 2020. Embedding-
based retrieval in facebook search. InProceedings of the 26th ACM SIGKDD
International Conference on Knowledge Discovery & Data Mining. 2553–2561.
[12] Yulei Huang, Hao Deng, Haibo Xing, Jinxin Hu, Chuanfei Xu, Zulong Chen,
Yu Zhang, and Xiaoyi Zeng. 2026. RCLRec: Reverse Curriculum Learning for
Modeling Sparse Conversions in Generative Recommendation.arXiv preprint
arXiv:2603.28124(2026).
[13] Jinqiu Jin, Yang Zhang, Fuli Feng, and Xiangnan He. 2025. Generative Multi-
Target Cross-Domain Recommendation.arXiv preprint arXiv:2507.12871(2025).
[14] Wei Jin, Haitao Mao, Zheng Li, Haoming Jiang, Chen Luo, Hongzhi Wen, Haoyu
Han, Hanqing Lu, Zhengyang Wang, Ruirui Li, et al . 2023. Multilingual e-
commerce session recommendation: The Amazon M2 dataset and a baseline
approach. InProceedings of the ACM Web Conference 2023.
[15] Wang-Cheng Kang and Julian McAuley. 2018. Self-attentive sequential recom-
mendation. In2018 IEEE international conference on data mining (ICDM). IEEE,
197–206.
[16] Hanyu Li, Jiayu Li, Weizhi Ma, Peijie Sun, Haiyang Wu, Jingwen Wang, Yuekui
Yang, Min Zhang, and Shaoping Ma. 2025. CD-CDR: Conditional diffusion-based
item generation for cross-domain recommendation. InProceedings of the 48th
International ACM SIGIR Conference on Research and Development in Information
Retrieval. 1789–1798.
[17] Jiahuan Li, Shujian Huang, Aarron Ching, Xinyu Dai, and Jiajun Chen. 2024.
PreAlign: Boosting Cross-Lingual Transfer by Early Establishment of Multilingual
Alignment. InProceedings of the 2024 Conference on Empirical Methods in Natural
Language Processing (EMNLP). Association for Computational Linguistics, 10246–
10257.
[18] Mang Li and Wei Lyu. 2025. Adaptive Regularization for Large-Scale Sparse
Feature Embedding Models.arXiv preprint arXiv:2511.06374(2025).
[19] Xiaopeng Li, Bo Chen, Junda She, Shiteng Cao, You Wang, Qinlin Jia, Haiying He,
Zheli Zhou, Zhao Liu, Ji Liu, et al. 2025. A survey of generative recommendation
from a tri-decoupled perspective: Tokenization, architecture, and optimization.
(2025).
[20] Qidong Liu, Xiangyu Zhao, Yejing Wang, Zijian Zhang, Howard Zhong, Chong
Chen, Xiang Li, Wei Huang, and Feng Tian. 2025. Bridge the domains: Large

CIKM ’26, November 07–11, 2026, Rome, Italy Yuan Gao et al.
language models enhanced cross-domain sequential recommendation. InProceed-
ings of the 48th International ACM SIGIR Conference on Research and Development
in Information Retrieval. 1582–1592.
[21] Zhiwei Liu, Yongjun Chen, Jia Li, Philip S Yu, Julian McAuley, and Caiming
Xiong. 2021. Contrastive Self-supervised Sequential Recommendation with
Robust Augmentation.arXiv preprint arXiv:2108.06479(2021).
[22] Julian McAuley, Christopher Targett, Qinfeng Shi, and Anton van den Hengel.
2015. Image-based Recommendations on Styles and Substitutes. InProceedings
of the 38th International ACM SIGIR Conference on Research and Development in
Information Retrieval (SIGIR). 43–52.
[23] Shashank Rajput, Nikhil Mehta, Anima Singh, Raghunandan Hulikal Keshavan,
Trung Vu, Lukasz Heldt, Lichan Hong, Yi Tay, Vinh Tran, Jonah Samost, et al.
2023. Recommender systems with generative retrieval.Advances in Neural
Information Processing Systems36 (2023), 10299–10315.
[24] Christopher Starke, Ljubiša Metikoš, Natali Helberger, and Claes de Vreese. 2025.
Contesting personalized recommender systems: a cross-country analysis of user
preferences.Information, Communication & Society28, 1 (2025), 41–60.
[25] Jinpeng Wang, Ziyun Zeng, Yunxiao Wang, Yuting Wang, Xingyu Lu, Tianxiang
Li, Jun Yuan, Rui Zhang, Hai-Tao Zheng, and Shu-Tao Xia. 2023. MISSRec: Pre-
training and Transferring Multi-modal Interest-aware Sequence Representation
for Recommendation. InProceedings of the 31st ACM International Conference on
Multimedia. 6548–6557.
[26] Haibo Xing, Hao Deng, Yucheng Mao, Jinxin Hu, Yi Xu, Hao Zhang, Jiahao
Wang, Shizhun Wang, Yu Zhang, Xiaoyi Zeng, et al. 2025. Reg4rec: Reasoning-
enhanced generative model for large-scale recommendation systems.arXiv
preprint arXiv:2508.15308(2025).
[27] Zhenhui Xu, Meng Zhao, Liqun Liu, Lei Xiao, Xiaopeng Zhang, and Bifeng Zhang.
2022. Mixture of virtual-kernel experts for multi-objective user profile modeling.
InProceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and
Data Mining. 4257–4267.
[28] Wenhao Yang, Yingchun Jian, Yibo Wang, Shiyin Lu, Lei Shen, Bing Wang, Hai-
hong Tang, and Lijun Zhang. 2024. Not all embeddings are created equal: Towards
robust cross-domain recommendation via contrastive learning. InProceedings of
the ACM Web Conference 2024. 3195–3206.
[29] Zheng Yuan, Fajie Yuan, Yu Song, Youhua Li, Junchen Fu, Fei Yang, Yunzhu
Pan, and Yongxin Ni. 2023. Where to Go Next for Recommender Systems? ID-
vs. Modality-based Recommender Models Revisited. InProceedings of the 46th
International ACM SIGIR Conference on Research and Development in Information
Retrieval (SIGIR).
[30] Tianzi Zang, Yanmin Zhu, Haobing Liu, Ruohan Zhang, and Jiadi Yu. 2022. A
Survey on Cross-domain Recommendation: Taxonomies, Methods, and Future
Directions.ACM Transactions on Information Systems (TOIS)41, 2 (2022), 1–39.
[31] Jiaqi Zhai, Lucy Liao, Xing Liu, Yueming Wang, Rui Li, Xuan Cao, Leon Gao, Zhao-
jie Gong, Fangda Gu, Michael He, et al. 2024. Actions speak louder than words:
Trillion-parameter sequential transducers for generative recommendations.arXiv
preprint arXiv:2402.17152(2024).
[32] Hao Zhang, Mingyue Cheng, Qi Liu, Junzhe Jiang, Xianquan Wang, Rujiao
Zhang, Chenyi Lei, and Enhong Chen. 2025. A comprehensive survey on cross-
domain recommendation: Taxonomy, progress, and prospects.arXiv preprint
arXiv:2503.14110(2025).
[33] Wei Zhang, Pengye Zhang, Bo Zhang, Xingxing Wang, and Dong Wang. 2023. A
collaborative transfer learning framework for cross-domain recommendation.
InProceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and
Data Mining. 5576–5585.
