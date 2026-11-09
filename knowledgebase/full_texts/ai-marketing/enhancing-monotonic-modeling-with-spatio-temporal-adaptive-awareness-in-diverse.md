---
title: Enhancing Monotonic Modeling with Spatio-Temporal Adaptive Awareness in Diverse Marketing
url: https://arxiv.org/abs/2406.14132
category: ai-marketing
subcategory: empirical
date: 2024-06
venue: ''
authors:
- Bin Li
- Jiayan Pei
- Feiyang Xiao
- Yifan Zhao
- Zhixing Zhang
source: arxiv
pdf_url: https://arxiv.org/pdf/2406.14132
pages: 12
chars: 61939
fetched_at: '2026-11-08T13:11:18+00:00'
kb_version: 1
---

# Enhancing Monotonic Modeling with Spatio-Temporal Adaptive Awareness in Diverse Marketing

Enhancing Monotonic Modeling with Spatio-Temporal Adaptive
Awareness in Diverse Marketing
Bin Li, HengXu He, Jiayan Pei, Feiyang Xiao, Yifan Zhao, Zhixing Zhang, Diwei Liu, Jia Jia
Alibaba Group
Hangzhou, Zhejiang, China
{ningzhu.lb,hengxu.hhx,jiayanpei.pjy,feiyangxiao.xfy,zhang.zzx,jj229618}@alibaba-
inc.com,{xuefan.zyf,diwei.ldw}@koubei.com
ABSTRACT
In the mobile internet era, the Online Food Ordering Service (OFOS)
emerges as an integral component of inclusive finance owing to the
convenience it brings to people. OFOS platforms offer dynamic allo-
cation incentives to users and merchants through diverse marketing
campaigns to encourage payments while maintaining the platforms’
budget efficiency. Despite significant progress, the marketing do-
main continues to face two primary challenges: (i) how to allocate
a limited budget with greater efficiency, demanding precision in
predicting users’ monotonic response (i.e. sensitivity) to incen-
tives, and (ii) ensuring spatio-temporal adaptability and robustness
in diverse marketing campaigns across different times and loca-
tions. To address these issues, we propose a Constrained Monotonic
Adaptive Network (CoMAN) method for spatio-temporal perception
within marketing pricing. Specifically, we capture spatio-temporal
preferences within attribute features through two foundational
spatio-temporal perception modules. To further enhance catching
the user sensitivity differentials to incentives across varied times
and locations, we design modules for learning spatio-temporal
convexity and concavity as well as for expressing sensitivity func-
tions. CoMAN can achieve a more efficient allocation of incentive
investments during pricing, thus increasing the conversion rate
and orders while maintaining budget efficiency. Extensive offline
and online experimental results within our diverse marketing cam-
paigns demonstrate the effectiveness of the proposed approach
while outperforming the monotonic state-of-the-art method.
CCS CONCEPTS
• Information systems→ Location based services .
KEYWORDS
Monotonic Modeling; Online Food Ordering; Marketing Policy;
Budget Allocation
ACM Reference Format:
Bin Li, HengXu He, Jiayan Pei, Feiyang Xiao, Yifan Zhao, Zhixing Zhang, Di-
wei Liu, Jia Jia. 2018. Enhancing Monotonic Modeling with Spatio-Temporal
Adaptive Awareness in Diverse Marketing. In Proceedings of Make sure to
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than the
author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or
republish, to post on servers or to redistribute to lists, requires prior specific permission
and/or a fee. Request permissions from permissions@acm.org.
Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
© 2018 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM ISBN 978-1-4503-XXXX-X/18/06
https://doi.org/XXXXXXX.XXXXXXX
enter the correct conference title from your rights confirmation emai (Confer-
ence acronym ’XX). ACM, New York, NY, USA, 12 pages. https://doi.org/
XXXXXXX.XXXXXXX
1 INTRODUCTION
With mobile payment services, Online Food Ordering Service (OFOS)
platforms such as Ele.me,1 Meituan 2 and Uber Eats3 have become
critical components of inclusive finance through the convenience
offered by real-time provisioning. To encourage mobile payments
for food and retail delivery, platforms offer incentives (e.g., coupons,
commissions, bonuses) to users through diverse marketing strate-
gies and campaigns. Within these marketing campaigns, the intelli-
gent allocation of incentives to users and merchants represents a
critical aspect for platforms in enhancing marketing efficiency.
Users exhibit different monotone response patterns to platform
incentives across various marketing campaigns[ 38, 40]. It is rea-
sonable that a higher incentive amount increases the probability
of user redemption. Specifically, the user Conversion Rate (CVR)
expresses a monotonic increasing trend to the increment of red
packets or discount amounts, while it monotonically decreases
about the threshold for coupon. Similarly, it exhibits a monotonic
decreasing relationship with delivery fees. Without incorporating
the monotone prior into the predictive model of user response,
the model is susceptible to learning biased and over-fit patterns
influenced by the noise introduced in the dataset.
Previous work in the marketing domain [2, 3] has explored var-
ious methods for optimizing incentives under a limited budget.
[16, 38, 40] have approached marketing pricing by employing a
paradigm consisting of two components: predicting user response
scores and making real-time decisions through linear programming.
Importantly, in the takeaway domain, where user preferences are
significantly influenced by spatio-temporal factors, relevant studies
in the recommendation field [7, 19, 20] have explored the learning
and enhanced utilization of spatio-temporal information.
However, previous research in the takeaway marketing domain
has overlooked the critical importance of perceiving spatio-temporal
information, focusing instead on analyzing users’ sensitivity to
incentives in a general context. In reality, users exhibit varying
sensitivities to platform incentives when ordering from different
merchants at different times and locations. Relying solely on a uni-
form sensitivity function to assess user response across varying
times and locations is flawed. Therefore, it is essential to differenti-
ate descriptions of user sensitivity by spatio-temporal information
1www.ele.me.com
2www.meituan.com
3www.ubereats.com
arXiv:2406.14132v2  [cs.AI]  10 May 2025

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY Bin Li and HengXu He, et al.
awareness. Meanwhile, ensuring the model possesses enhanced
predictive accuracy and adapts robustly to diverse marketing.
In this paper, we tackle these challenges by proposing Con-
strained Monotonic Adaptive Network (CoMAN), a novel market-
ing pricing model utilizing spatiotemporal-enhanced monotonic
response. Specifically, our method employs two spatio-temporal
aware activation modules to guide the model in learning and un-
derstanding spatio-temporal features, thus facilitating a more rea-
sonable capture of spatio-temporal information within the rep-
resentations. Additionally, our meticulously designed monotonic
layer enhances the perception of the spatio-temporal differentia-
tion in users’ monotonic responses to incentives. Concurrently, we
introduce the activation function tailored to adaptively learn the
incentive sensitivity function of users in the marketing domain. Ul-
timately, CoMAN achieves a strict continuous monotonic, precise,
and smooth fitting of the incentive sensitivity function across differ-
ent spatio-temporal dimensions. The effectiveness of our proposed
methodology is demonstrated through extensive online and offline
experiments across diverse marketing campaigns. In summary, our
main contributions are as follows:
• We highlight the primary challenges encountered in the
marketing domain and analyze the significance of spatio-
temporal preference awareness, while further designing a
novel model to address these issues. To the best of our knowl-
edge, our model is the first to systematically model mono-
tonic response by perceiving spatio-temporal information
for diverse takeaway marketing.
• We propose a monotonic layer that utilizes the perception
of spatio-temporal information to enhance modeling mono-
tonic responses. This module adaptively learns the concavity,
convexity, and parametric expression of user incentive sensi-
tivity functions in diverse marketing campaigns conditioned
on different spatio-temporal characteristics.
• We conceptualize a strictly monotonic Convex Linear Unit
(CLU) activation function tailored to diverse marketing. We
utilize the activation function to flexibly learn the differences
in monotonic function expressions. We demonstrate that this
strictly convex function can more effectively approximate
user incentive response functions.
2 RELATED WORK
Activation Functions. Activation functions play a pivotal role
in neural networks by introducing nonlinear transformations, al-
lowing deep models to capture complex patterns beyond the reach
of linear operations[13, 24, 25, 28]. A series of studies like Leaky
ReLU [23], PReLU [11], and ELU [4] have designed ReLU variants
that mitigate this issue by permitting a small, non-zero gradient
to negative inputs, thereby mitigating the issue while enhancing
the model performance. A series of works by [8, 31, 39] have inves-
tigated how to combine the output of the original ReLU with its
point reflection within the same neural network layer.
Monotonicity by architecture. Research methods for model-
ing monotonic response can be categorized into two primary types.
The first involves the monotonic structure by construction, such
as constrained network weights to be exclusively non-negative or
non-positive, guaranteeing the model exhibits either monotoni-
cally increasing or decreasing. The other employs regularization
to impose monotonicity, networks implement monotonic through
the modified loss functions or the heuristic regularization terms
during training. Min-Max networks [6, 32] utilize monotonic linear
embedding and max-min-pooling to endow networks with broad
modeling capacity but are challenging to train and practice. Deep
Lattice Network (DLN)[37] applies constraints to pairs of lattice
parameters but limits the function approximation space and ne-
cessitates a substantial number of parameters learned. CMNN [29]
can approximate any continuous monotonic function by combining
non-saturated and saturated activation functions while lacking the
capability to learn adaptively.
Monotonicity by regularization. As mentioned above, enforc-
ing monotonicity during the training can also be achieved by mod-
ifying loss function or incorporating regularization terms[10, 33].
A. Sivaraman et al.[34] introduced a mechanism based on Satisfia-
bility Modulo Theories (SMT) solvers capable of identifying point
pairs violating monotonicity constraints (i.e. counterexamples). Liu
et al.[21] transforms the mathematically verifying monotonicity
on arbitrary piece-wise linear (i.e. ReLU) networks into a Mixed
Integer Linear Programming (MILP) problem and can be efficiently
solved with existing MILP solvers. Both MILP and SMT methodolo-
gies, depend on the piecewise-linear property of ReLU to validate
the constrained monotonic learning while not being extended to
other activation functions such as ELU[ 4], SELU[17], GELU[12],
etc. Moreover, the computational costs associated with these tech-
niques are significant, frequently necessitating multiple iterations
to achieve a rigorously verified monotonic model.
3 PRELIMINARIES
We formulate the marketing problem as a constrained linear pro-
gramming problem to be solved using the optimization approach.
We define the user set asC and the candidate set of incentive val-
ues asT , where𝑡𝑗 ∈T represents the 𝑗-th treatment. Our goal
is to find an incentive allocation strategy that optimally allocates
incentives to maximize the sum of profits from user response (i.e.
CVR) under the constrained budgetB. Formally,
max𝑥𝑖,𝑗
|C|∑︁
𝑖=1
|T|∑︁
𝑗=1
𝑥𝑖,𝑗𝑟𝑖,𝑗 (1)
𝑠.𝑡.𝑥 𝑖,𝑗 ∈[ 0, 1],𝑓𝑜𝑟 𝑖 = 1,...,|C| ; 𝑗 = 1,...,|T| (2)
|T|∑︁
𝑗=1
𝑥𝑖,𝑗 = 1,𝑓𝑜𝑟 𝑖 = 1,...,|C| (3)
˝|C|
𝑖=1
˝|T|
𝑗=1𝑥𝑖,𝑗𝑡𝑗𝑟𝑖,𝑗
˝|C|
𝑖=1
˝|T|
𝑗=1𝑥𝑖,𝑗𝑟𝑖,𝑗
≤B (4)
where𝑥𝑖,𝑗 denotes the decision vector indicating whether treatment
𝑡𝑗 is allocated to user𝑖, and𝑟𝑖,𝑗 represents the response score by our
response model. And ˝|T| 𝑗=1𝑥𝑖,𝑗𝑡𝑗 is the incentive value for the user
under constraint 3. Furthermore, constraint 4 indicates the limited
average incentive to each user. By introducing dual variables 𝜇𝑖
and𝜆 corresponding to the aforementioned constraints 3 and 4,
we transform the primal problem into its dual counterpart. The
convex optimization problem delineated in objective function 1
is addressed through the application of the Lagrangian multiplier
method, formally depicted as follows:

Enhancing Monotonic Modeling with Spatio-Temporal Adaptive Awareness in Diverse Marketing Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
OD (User x Shop)
 Features
AOI (User)
Features
Shop Features Spatio-temporal
 Features
Spatio-temporal
Activation
S-t
Target Attention
Target AOI (User) Sequences
Experts A
EA,1 EA,2 EA,m…
Experts Shared
ES,1 …
Experts B
EB,1 EB,2 EB,m…
Tower A Tower B
Monotonic
 Layer
TB,1
Dense
 Layer
Output A Output B
TB,n
…
TB,1
TB,n
…
Threshold Amount
Query Features
ES,2 ES,m
…
Concat Concat Concat Concat Concat Concat Concat Concat
S-t Target AttentionSpatio-temporal Activation
Dot-Product
𝒲!,𝑏"
MatMul
Scaled
MatMul
e!"
MatMul
Latent
Embedding
Spatio-temporal
Embedding
Query
Embedding
AOI (User) Seq
Embedding
Gating Network
Vector 1 Vector m…
Selector
FC
Softmax
Output
FC
Fused/Spatio-temporal
Representation "𝜌(.)
’𝜌(.)
(𝜌(.)
Mask Add
)"
𝒲
𝒲#
𝐵𝑖𝑎𝑠 𝐹𝑜𝑢𝑟	𝑃𝑎𝑟𝑎𝑚 	𝑀𝑜𝑑𝑒𝑙
Input
𝑡
𝑠!":̆𝑠,̂𝑠,̃𝑠
Adaptive Activation
Q
K V
Q
K V
S-t Attention
Monotonic Layer
Monotonic
&Non-monotonic
𝒲#,𝑏# 𝒲$,𝑏$
e!"e$% e!e%
ℎ"& ℎ""&
𝑟’,𝑒!"
Scaled
SoftMax
𝑚(
Concat
Figure 1: Overview of our proposed Constrained Monotonic Adaptive Network (CoMAN) architecture.
min𝑥𝑖,𝑗 −
|C|∑︁
𝑖=1
|T|∑︁
𝑗=1
𝑥𝑖,𝑗𝑟𝑖,𝑗+
|C|∑︁
𝑖=1
(𝜇𝑖(
|T|∑︁
𝑗=1
𝑥𝑖,𝑗− 1))
+𝜆(
|C|∑︁
𝑖=1
|T|∑︁
𝑗=1
𝑥𝑖,𝑗𝑟𝑖,𝑗(𝑡𝑗−B))
(5)
Rearrange the equation 5, we have:
min𝑥𝑖,𝑗
|C|∑︁
𝑖=1
|T|∑︁
𝑗=1
𝑥𝑖,𝑗[𝑟𝑖,𝑗(𝜆𝑡𝑗−𝜆B− 1)]
+
|C|∑︁
𝑖=1
(𝜇𝑖(
|T|∑︁
𝑗=1
𝑥𝑖,𝑗− 1))
(6)
Given both the objective function and the constraint functions are
convex, the optimal𝜆∗ is obtained by applying the KKT conditions
and L-BFGS. From 6, it can be observed that different incentive val-
ues are only related to the first term. Consequently, an approximate
solution can be derived as follows:
𝑥𝑖,𝑗 =
(
1, if 𝑗 =𝑎𝑟𝑔𝑚𝑖𝑛𝑗𝑟𝑖,𝑗(𝜆∗𝑡𝑗−𝜆∗B− 1)
0, otherwise (7)
During online pricing decisions, we employ our response model
to predict response scores|T| times based on candidates for each
request. Then utilizing the real-time computed value of𝜆∗ along
with decision equation 7 to price the incentive value.
4 METHODS
In the marketing campaigns, we design a multi-task model as a
pricing model predicting various business objectives such as Con-
version Rate (CVR) or CTCVR (Click Through & Conversion Rate)
and GMV(Gross Merchandise Volume). Given that the tasks’ predic-
tions lack substantive relevance, there is a risk of encountering the
Seesaw Phenomenon during multi-task learning. It may lead one task
to improve while another deteriorates. To mitigate this, we utilize
the Progressive Layered Extraction (PLE) [35] multi-task framework
and propose the Constrained Monotonic Adaptive Network (CoMAN).
Overview. The design and modeling of our proposed framework
focus on three critical aspects: activating spatio-temporal correla-
tions within the attribute features, modeling monotonic response to
incentives in diverse marketing, and enhancing the model’s adapt-
ability to spatio-temporal disparities within the monotonic layer.
The overall architecture is depicted in Figure 1.
In our feature extraction process, we segment the period into
five intervals: breakfast [04:00–10:00), lunch [10:00–14:00), after-
noon tea [14:00–17:00), dinner [17:00–20:00), and midnight snack
[20:00–04:00), and we statistic numerical features to each period. We
construct temporal features by incorporating information such as
the Gregorian and lunar dates, holiday occurrences, and weekdays
for each day. Simultaneously, we formulate spatial features from
geographical data, encompassing the user’s current location, city
ID, district ID, and AOI (Area of Interest) ID. We utilize embedding
matrices to semantically encode user attributes, shop attributes,
queries, user behaviors, and spatio-temporal attributes respectively.
Specifically, the latent embeddings 𝑒𝑙𝑖 for attribute features are
derived from[𝑒𝑙𝑜,𝑒𝑙𝑢,𝑒𝑙𝑠], which correspond to cross features em-
bedding, user embedding, and shop embedding, respectively. The
query embedding is denoted as𝑒𝑞, the behavior embedding as𝑒𝑏,
and the spatio-temporal embedding as𝑒𝑠𝑡 . Notably, in certain mar-
keting campaigns different from user-level modeling, we employ
regional modeling for AOIs. Therefore, depending on marketing
campaigns, we tailor our features to use either users or AOIs (e.g.,
cross features, historical click sequences).
Spatio-temporal Correlation. We design two spatio-temporal
correlation modules, namely Temporal Activation and Temporal

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY Bin Li and HengXu He, et al.
Four Param Model
FC
Fused Representation
FCFCFC
!"=$"+ $# 1+'$%!('$%")
$"
$)
$*
$"+$#
Incentive
CVR
(a) Four-Parameter Model
S-t Attention
!"=$"+ $# 1+'$%!('$%")
Dense
Spatial-temporal
Embedding
Fused
Representation
MatMul
$$,&%
Dense
Dense
×4 (b) Spatio-temporal Attention
Figure 2: Original Four-Parameter Model (FPM) and combined with Spatio-temporal Attention (S-t Attention) fitting.
Target Attention, to respectively explore the spatio-temporal char-
acteristics and preferences inherent in static attributes and user
behaviors. Within the Temporal Activation module, spatio-temporal
features input to compute the weights of each feature embedding
(i.e., User, Shop, Query) 𝑒𝑙𝑖 through a dot-product operation fol-
lowed by a sigmoid function. This process aims to capture the
dynamic variations inherent in spatio-temporal representations.
The outcome is then multiplied by the input representations and
integrated via a residual connection, designed to activate the spatio-
temporal information encapsulated within the feature embeddings.
The output of the Temporal Activation module, denoted asℎ𝑡𝑎 , can
be formulated as follows:
ℎ𝑡𝑎 = sigmoid(
FC(𝑒𝑠𝑡)· 𝑒𝑇 𝑙𝑖
√︃
𝑑𝑒𝑙𝑖
)𝑒𝑙𝑖+𝑒𝑙𝑖. (8)
Employing the Temporal Target Attention mechanism to catch the
interest preferences of different AOIs/Users towards Shops while
simultaneously learning the variation across different times and
spaces effectively. We accomplish this by applying linear projections
to the Query, Key, and Value vectors using weights and biases (e.g.,
[𝑤𝑄,𝑏𝑄]) generated by fully connected neural networks from𝑒𝑠𝑡 .
The module output denoted asℎ𝑡𝑡𝑎 , is articulated as follows:
ℎ𝑡𝑡𝑎 = softmax(
(𝑤𝑄·𝑒𝑞+𝑏𝑄)(𝑤𝐾·𝑒𝑠+𝑏𝐾)𝑇
√︁
𝑑𝑘
)(𝑤𝑉·𝑒𝑠+𝑏𝑉). (9)
Monotonic Response. To circumvent the difficulties in training
when combining traditional linear monotonicity constraints with
saturated (bounded) activation functions and the limitations that
only convex models can be learned by combining convex activation
functions, we construct a monotonic layer based on Constrained
Monotonic Neural Networks (CMNN) [29] framework. This approach
not only facilitates utilizing non-saturated activation functions but
also allows for a priori modeling of varying degrees of convexity
and concavity across diverse application scenarios.
We employ a monotonicity indicator vector𝑡∈{− 1, 0, 1}𝑛 for
the element-wise weights transformation of a feature vector to
constrain the monotonicity. The operation|·| 𝑡 is applied as follows:
𝑤′ 𝑗,𝑖 =
 


𝑤𝑗,𝑖

 if𝑡𝑖 = 1
−

𝑤𝑗,𝑖

 if𝑡𝑖 =−1
𝑤𝑗,𝑖 otherwise
(10)
We rigorously define a convex activation function ˘𝜌∈ ˘A, where
˘A denotes the set of all convex, monotonically increasing, lower-
bounded, zero-centred functions. And we define the concave acti-
vation function ˆ𝜌(𝑥) and the saturated function ˜𝜌(𝑥) as follows:
ˆ𝜌(𝑥) =− ˘𝜌(−𝑥)
˜𝜌(𝑥) =
(
˘𝜌(𝑥+ 1)− ˘𝜌(1) if𝑥 < 0
ˆ𝜌(𝑥− 1)+ ˘𝜌(1) otherwise
(11)
The function ˆ𝜌(𝑥) is concave and upper-bounded, while the func-
tion ˜𝜌(𝑥) is saturated and bounded. Furthermore, the activation
selection vector s =(˘𝑠, ˆ𝑠, ˜𝑠)∈ N3 and ˘𝑠+ˆ𝑠+ ˜𝑠 =𝑚 is introduced to ap-
proximate the concavity and convexity of the monotonic response
through combining concave, convex, and saturated activation func-
tions, where𝑚 denotes the monotonic variables dimension.
Specifically, by setting s =(𝑚, 0, 0), we guarantee that the mono-
tonic response is modeled as a convex function, with analogous
principles applied for concave modeling. Then the output of the
combined activation functions 𝜌s operates element-wise as follows:
4
 2
 0 2 4
4
2
0
2
4
Convex: (x)
Concave: (x)
Saturated: (x)
Figure 3: CLU based activation functions construction

Enhancing Monotonic Modeling with Spatio-Temporal Adaptive Awareness in Diverse Marketing Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
𝜌s(h)𝑗 =
 

˘𝜌 ℎ𝑗  if 𝑗≤ ˘𝑠
ˆ𝜌 ℎ𝑗  if ˘𝑠 < 𝑗≤ ˘𝑠+ ˆ𝑠
˜𝜌 ℎ𝑗  otherwise (12)
Moreover, since the user response to incentives is not smooth
across the entire treatment interval, it is impractical to model these
curves using a linear representation with a fixed smoothing expo-
nential function, as noted by [ 40]. Accordingly, to flexibly adapt
to the spatiotemporally diverse property of marketing campaigns
and learn the monotonic response functions, we introduce a strictly
monotonic convex activation function, named Convex Linear Unit
(CLU). The detailed proof of the convexity properties of CLU is pro-
vided in Appendix B.2. Furthermore, we derive the corresponding
concave activation function ˆ𝜌(𝑥) and the saturated activation func-
tion ˜𝜌(𝑥) through CLU. The activation functions construction is
depicted in Figure 3, with CLU mathematical expressions as follows:
˘𝜌(𝑥) =
(
−𝜔0 2 + 𝜔0 1+𝑒−𝜔1𝑥 if𝑥 < 0
𝑥 otherwise (13)
The Universal Approximation Theorem[5, 14, 27] posits that any
continuous function over a closed interval can be approximated
by neural networks with nonpolynomial activation functions. Con-
currently, any multivariate continuous monotonic function on
compact subsets of R𝑘 can be approximated by monotonic con-
strained neural networks with at most𝑘 hidden layers using sigmoid
activation[6]. Inspired by this, we propose theFour-Parameter Model
(FPM) through an adaptive translation of the sigmoid, combined
with the CMNN framework, to flexibly approximate monotonic
response functions in complex scenarios. Meanwhile, we derive
Theorem 1, with a detailed proof available in the Appendix B.1.
Theorem 1. Let ˘𝜌∈ ˘A. Then any multivariate continuous monotone
function f on a compact subset of R𝑘 can be approximated with a
monotone constrained neural network of at most 𝑘 layers using𝜌 as
the activation function.
Figure 2a elucidates the functional form and parametric behavior
of the FPM method, we learn and interpret the incentive sensitivity
curve through four parameters, each bearing tangible significance
in marketing. The parameter𝜔0 represents the natural conversion
rate in the absence of any incentive. The parameter𝜔1 denotes the
sensitivity of the user at the motivational inflection point𝜔2, while
𝜔3 corresponds to the maximal conversion rate attainable by users.
Adaptive Response Enhancement. To enable the model to
learn the variability of monotonic response across different spatio-
temporal dimensions, we design theAdaptive Activation and Spatio-
temporal Attention (S-t Attention) modules within the monotonic
layer to enhance the model’s capability to perceive spatio-temporal
information. These modules are designed to flexibly adapt the
convexity, concavity, and parametric expressions of monotonic
response functions through spatio-temporal representations.
In previous CMNN methodology, s is a priori parameter requir-
ing manual adjustment through tuning rather than allowing for
adaptive learning. The inflection point of a monotonic response
function divides it into convex and concave segments. Drawing on
these insights, we propose an Adaptive Activation module capable
of adaptively learning and adjusting the proportion of convexity
Breakfast Lunch Afternoon T eaDinner Midnight Snack
City1City2City3City4City5
9.26 9.39 9.46 9.26 9.22
7.95 8.14 8.05 7.47 7.81
8.54 8.42 8.49 8.00 8.22
7.89 7.79 7.89 7.37 7.63
7.78 7.66 7.35 6.98 7.21
7.0
7.5
8.0
8.5
9.0
Figure 4: Visualization of the average redemption amount
of coupons in the top five cities with the most users across
different periods.
and concavity by catching and fusing deep representations with
spatio-temporal information. As depicted on the left of the mono-
tonic layer in Figure 1, we mask different parts of the monotonic
representation𝑚𝑖 with the adaptively learned convexity-concavity
ratio factor𝑠𝑠𝑡 and then combine through convex, concave, and
saturated activation functions separately. The operations of the
Adaptive Activation can be elucidated as follows:
𝑠𝑠𝑡 =|softmax(
𝑚𝑖(Concat(𝑟𝑓,𝑒𝑠𝑡))𝑇
√︁
𝑑𝑘
)𝑚𝑖|. (14)
We design an Spatio-temporal (S-t) Attention module to utilize
spatio-temporal information to further adaptively adjust and learn
FPM. Firstly, we generate weights and bias ([𝑤𝑖,𝑏𝑖]) terms for deep
fused representation vectors (e.g., users, shops, etc.) through a fully
connected layer. Then we conduct matrix multiplication calcula-
tions to derive the FPM parameters. The module structure is illus-
trated in Figure 2b, and can be formulated as follows:
𝜔𝑖 = FC(𝑤𝑖· FC(𝑟𝑓)+ 𝑏𝑖). (15)
5 EXPERIMENTS
5.1 Experimental Setup
Dataset Description. We conducted experiments on real-world
datasets4 from two marketing campaigns on Ele.me, one of the
largest OFOS platforms in China. The training datasets span one
week, while the test dataset covers a single day. Notably, we ran-
domly select 5% of online traffic flow as unbiased sample to ran-
domly allocate incentive values as the ground truth for the incen-
tive sensitivity function approximation. (i) Exploding Red Pack-
ets Dataset: Send an average of 10 million exploding red packets
to users online per day. It’s a classification dataset with approxi-
mately 1.05 million daily training samples and nearly 400 features,
ultimately reaching 8.4 million samples. (ii) Delivery Fee Waiver
Dataset: It is a regression dataset covering approximately 3.2 mil-
lion AOIs, with about 4.3 million shops and 303 features. The daily
samples are around 770 million, with the total exceeding 6 billion
samples. We segment application data by period and city and visu-
alize users’ average redemption amount in exploding red packets,
4We gathered two real-world datasets from Ele.me’s online platform due to the absence
of available public datasets suitable for evaluating our task.

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY Bin Li and HengXu He, et al.
Table 1: Overall performance on Exploding Red Packets and Delivery Fee Waiver.
Method Exploding Red Packets Delivery Fee Waiver AUC↑ MSE↓ KL Div↓ Corr Coeff↑ MAE↓ MSE↓ KL Div↓ Corr Coeff↑
DNN[30] 0.6974 0.0636 0.6243 0.8513 0.1841 0.0831 0.8332 0.8304
DNN-M[1] 0.7022 0.0431 0.4259 0.8713 0.1232 0.0422 0.5347 0.8629
SBBM[40] 0.7081 0.0343 0.2110 0.8927 0.1079 0.0338 0.3219 0.8827
FPM 0.7113 0.0293 0.1901 0.9066 0.0913 0.0323 0.3083 0.8961
CMNN[29](ReLU[24]) 0.7111 0.0282 0.1848 0.9150 0.0894 0.0298 0.2772 0.8916
CMNN(ELU[4]) 0.7139 0.0273 0.1737 0.9171 0.0823 0.0281 0.2761 0.9127
CMNN(CLU) 0.7151 0.0269 0.1718 0.9189 0.0809 0.0274 0.2343 0.9143
CoMAN-B 0.7348 0.0224 0.1305 0.9229 0.0769 0.0263 0.2218 0.9193
CoMAN w/o AA 0.7414 0.0191 0.0984 0.9333 0.0624 0.0227 0.1897 0.9326
CoMAN w/o S-t 0.7407 0.0159 0.0925 0.9357 0.0733 0.0243 0.1809 0.9273
CoMAN 0.7480 0.0115 0.0901 0.9486 0.0454 0.0184 0.1211 0.9469 +0.0506 +0.0521 +0.5342 +0.0973 +0.1387 +0.0647 +0.7121 +0.1165
Table 2: Temporal segment evaluation on Exploding Red Packets. We denote the following periods: Bkfst (Breakfast), Lch
(Lunch), A.Tea (Afternoon Tea), Din (Dinner), and M.S. (Midnight Snack).
Method MAE↓ KL Div↓ Bkfst Lch A.Tea Din M.S. Overall Bkfst Lch A.Tea Din M.S. Overall
FPM 0.1782 0.1385 0.1461 0.1297 0.1118 0.1325 0.1395 0.0824 0.1024 0.0918 0.0439 0.2801
CoMAN 0.0369 0.0449 0.0529 0.0780 0.0629 0.0448 0.0297 0.0288 0.0432 0.0737 0.0360 0.1480 +0.1413 +0.0936 +0.0932 +0.0517 +0.0489 +0.0877 +0.1098 +0.0536 +0.0592 +0.0181 +0.0079 +0.1321
Table 3: Temporal segment evaluation on Delivery Fee Waiver
Method MAE↓ KL Div↓ Bkfst Lch A.Tea Din M.S. Overall Bkfst Lch A.Tea Din M.S. Overall
FPM 0.1073 0.0883 0.1021 0.0932 0.0972 0.0943 0.0721 0.0809 0.0678 0.0733 0.0749 0.3692
CoMAN 0.0771 0.0569 0.0732 0.0631 0.0654 0.0632 0.0307 0.0276 0.0283 0.0259 0.0271 0.1398 +0.0302 +0.0314 +0.0289 +0.0301 +0.0318 +0.0311 +0.0414 +0.0533 +0.0395 +0.0474 +0.0478 +0.2294
as depicted in Figure 4. The visualization reveals that users’ pref-
erences for coupon amounts differ across various spatio-temporal
settings, which is consistent with the analysis.
Evaluation Metric. To comprehensively evaluate the perfor-
mance of our model, we assess it from both accuracy and distribu-
tion perspectives. We first employ metrics such as the Area Under
the Curve (AUC)[9], Mean Absolute Error (MAE)[ 36] and Mean
Squared Error (MSE)[15] to evaluate the precision of the model.
Subsequently, we use the Kullback-Leibler Divergence (KL Div)[18]
and Correlation Coefficients (Corr Coeff)[26] to assess the similar-
ity between the model’s predicted incentive sensitivity functions
and the random traffic (i.e. ground truth).
Baselines. To verify the effectiveness of our proposed method-
ology, we compare it against baselines with several state-of-the-
art methods as follows: (i) DNN: This is a naive model devoid of
spatio-temporal and monotonic modeling capabilities. (ii) DNN-M:
This method constrains the network weights to be exclusively non-
negative or non-positive and combines sigmoid activation functions
for monotonic modeling. (iii)SBBM: The Semi-black-box model[40]
predicts dynamic marketing responses by enhancing the logit de-
mand curve through neural networks. (iv) FPM: This approach
utilizes the mathematical four-parameter function to independently
approximate the monotonic response function. (v) CMNN: This
method employs the CMNN framework in conjunction with differ-
ent base convex activation functions, including CLU proposed in
our study, while combining sigmoid as the final activation function.
Hyperparamters. In our experiments, for Exploding Red Pack-
ets, the model training batch size is set to 128 with Adagrad as an
optimizer and a learning rate of 0.001. In Delivery Fee Waiver, the
batch size is configured to 1024, using an Adagrad optimizer with a
learning rate of 0.012. Furthermore, all experiments are conducted
on AOP5 using 40 parameter servers and 400 worker threads. Fur-
ther implementation details concerning the model parameters can
be found in Appendix C.
5.2 Experimental Results
Performance Comparison We report the overall performance
of various competitive baselines and our proposed model across
5A model training platform self-developed by the Alibaba Group

Enhancing Monotonic Modeling with Spatio-Temporal Adaptive Awareness in Diverse Marketing Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
6 7 8 9 10 11 12 13 14
0.1
0.2
0.3
0.4
0.5
Ground Truth
FPM
CoMAN-B
CoMAN w/o AA
CoMAN w/o S-t
CoMAN
(a) Overall
6 7 8 9 10 11 12 13 14
0.0
0.1
0.2
0.3
0.4
0.5
0.6
Ground Truth
FPM
CoMAN-B
CoMAN w/o AA
CoMAN w/o S-t
CoMAN (b) Breakfast
6 7 8 9 10 11 12 13 14
0.1
0.2
0.3
0.4
0.5
0.6
Ground Truth
FPM
CoMAN-B
CoMAN w/o AA
CoMAN w/o S-t
CoMAN (c) Lunch
6 7 8 9 10 11 12 13 14
0.1
0.2
0.3
0.4
0.5
0.6 Ground Truth
FPM
CoMAN-B
CoMAN w/o AA
CoMAN w/o S-t
CoMAN
(d) Afternoon Tea
6 7 8 9 10 11 12 13 14
0.1
0.2
0.3
0.4
0.5
0.6
Ground Truth
FPM
CoMAN-B
CoMAN w/o AA
CoMAN w/o S-t
CoMAN (e) Dinner
6 7 8 9 10 11 12 13 14
0.1
0.2
0.3
0.4
0.5
0.6
Ground Truth
FPM
CoMAN-B
CoMAN w/o AA
CoMAN w/o S-t
CoMAN (f) Midnight Snack
6 7 8 9 10 11 12 13 14
0.1
0.2
0.3
0.4
0.5
0.6
Ground Truth
FPM
CoMAN-B
CoMAN w/o AA
CoMAN w/o S-t
CoMAN
(g) City 1
6 7 8 9 10 11 12 13 14
0.1
0.2
0.3
0.4
0.5
0.6
Ground Truth
FPM
CoMAN-B
CoMAN w/o AA
CoMAN w/o S-t
CoMAN (h) City 2
6 7 8 9 10 11 12 13 14
0.1
0.2
0.3
0.4
0.5
0.6
Ground Truth
FPM
CoMAN-B
CoMAN w/o AA
CoMAN w/o S-t
CoMAN (i) City 3
Figure 5: Visualization of the prediction scores for incentive responses from various online models and the corresponding
ground truth. Results are observed overall, with concurrent evaluations segmented by periods and cities.
two datasets in Table 1. Moreover, to evaluate the real-world ef-
fectiveness of our approach in practical applications, we present
the performance of the model in online marketing campaigns as
shown in Table 2 and Table 3. The results yield the following obser-
vations: (i) The performance of CoMAN is notably superior to all
competitive baselines. Compared to previous marketing response
approaches, CoMAN achieves an average improvement of 5.33% in
user redemption response accuracy and an average enhancement
of 5.89% in distribution similarity. These remarkable performance
gains strongly indicate that CoMAN has the potential to enhance
0~20% 20%~40% 40%~60% 60%~80% 80%~100%
Sensitivity Level
0.00
0.05
0.10
0.15
0.20
0.25Uplift Gain
SBBM
FPM
CoMAN
(a) Exploding Red Packets
0~20% 20%~40% 40%~60% 60%~80% 80%~100%
Sensitivity Level
0.00
0.05
0.10
0.15
0.20
0.25Uplift Gain
SBBM
FPM
CoMAN (b) Delivery Fee Waiver
Figure 6: Comparisons of uplift gain for users vary with
different incentive sensitivity levels.
marketing efficiency in budget allocation significantly. (ii) Meth-
ods like FPM and SBBM, which employ nonlinear mathematical
functions in conjunction with neural networks to adaptively en-
hance the logit response curve, are more effective than simply
applying positive or negative constraint learning to neural network
weights. These methods are capable of more accurately charac-
terizing users’ sensitivity to incentives. Specifically, FPM is more
effective than SBBM in representing this sensitivity, thereby high-
lighting the effectiveness of our approach in integrating FPM for
learning monotonic response. (iii) Compared to traditional market-
ing approaches like DNN-M and SBBM, CoMAN performs better
in perceiving and incorporating spatio-temporal information. Fur-
thermore, our model surpasses previous monotonic methods such
as CMNN and FPM in effectively capturing spatio-temporal repre-
sentations which enhances monotonic modeling. These findings
underscore the significant advancements of CoMAN, primarily at-
tributed to the activation modeling of spatio-temporal information
and the robust capture of spatio-temporal monotonic patterns. (iv)
Our designed CLU function, when integrated with CMNN, out-
performs the other two activation functions, ReLU and ELU. This
outcome substantiates the validity of approximating user mono-
tonic response curves with a non-fixed exponential function, thus
better capturing and expressing user sensitivity to incentives. (v)

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY Bin Li and HengXu He, et al.
Our approach exhibits superior performance across datasets with
different modeling granularities (i.e., user-level and regional-level).
This indicates that our method is capable of more precisely de-
scribing monotonic response under various incentives, whether the
focus is on user-level perception or regional-level modeling.
To visualize the effectiveness of our model in budget allocation
compared to previous marketing methods, we follow the idea pro-
posed by [22, 38] and use the first derivative of the response curve at
the inflection point as the "gradient" representing a user’s sensitivity
to incentives. Under the same incentive treatment, user groups with
high "gradient" values yield greater commercial returns compared
to those with low "gradient". Therefore, the efficiency of the market-
ing model can be attributed to the accurate estimation of response
scores for users with varying incentive sensitivities. Subsequently,
we rank the users in descending order based on their " gradient"
and divide them into five groups representing different levels of
sensitivity to incentives. As illustrated in Figure 6, CoMAN predicts
a higher uplift gain for the first group of highly sensitive users
compared to SBBM and FPM, while predicting a correspondingly
lower uplift gain for the least sensitive users. This demonstrates
our model’s higher efficiency in budget allocation.
Ablation Study To comprehensively understand the capability
of our proposed CoMAN model in approximating incentive sensi-
tivity functions, and recognizing that the S-t attention and adaptive
activation modules constitute the core modeling components of
CoMAN, we carried out exhaustive ablation studies to evaluate the
effectiveness of these pivotal modules. Accordingly, we introduced
three ablation variants: (i) CoMAN w/o (S-t and AA) (CoMAN-B),
this baseline version employs CMNN based on CLU combined with
FPM as the final activation function. (ii) CoMAN w/o AA, this revi-
sion excludes the Adaptive Activation module from the CoMAN
model. (iii) CoMAN w/o S-t, this variant omits the S-t Attention
module from the CoMAN structure. These versions are evaluated
against the complete CoMAN model, which integrates all the mod-
ules, to systematically assess the impact of each module on the
overall model performance. Additionally, the comparative exper-
iments of CMNN without the spatio-temporal activation and the
spatio-temporal target attention modules.
To validate the monotonic response property of the CoMAN, we
conduct offline tests in which all non-monotonic features are held
constant, while the monotonic features (e.g., amount and thresh-
old) increase. Then construct the CVR monotonic response curves,
as illustrated in Figures 7a and 7b respectively. From the results
shown in the above tables, we have the following observations:
(i) As our analysis suggests, models that leverage spatio-temporal
0.0
0.2
0.4
0.6
0.8
1.0
1 2 3 4 5 6 7 8 9101112131415
Amount
Threshold=20 Threshold=25
Threshold=30 Threshold=35
0.0
0.2
0.4
0.6
0.8
1.0
10121416182022242628303234363840
Threshold
Amo un t= 5 Amo un t= 6 Amo un t= 7 Amo un t= 8
( b )( a )
(a) Amount
0.0
0.2
0.4
0.6
0.8
1.0
1 2 3 4 5 6 7 8 9101112131415
Amount
Threshold=20 Threshold=25
Threshold=30 Threshold=35
0.0
0.2
0.4
0.6
0.8
1.0
10121416182022242628303234363840
Threshold
Amo un t= 5 Amo un t= 6 Amo un t= 7 Amo un t= 8
( b )( a ) (b) Threshold
Figure 7: Monotonic response curves of user sensitivity to
incentives with different amounts and thresholds
information in the monotonic layer to enhance the perception of
the monotonic response outperform models that consider only ba-
sic attributes and behavioral representations (e.g., FPM, CMNN) or
incorporate spatio-temporal capture solely in the embedding (e.g.,
CoMAN-B). (ii) The performance of single-module models in the
monotonic layer is significantly lower than that of models employ-
ing a two-module perception framework. This finding is consistent
with our design rationale, indicating that two-module perception
of spatio-temporal information more effectively captures the ad-
ditional semantics inherent in user monotonic responses. (iii) As
anticipated, employing the Adaptive Activation module facilitates
more adaptive learning of the concavity and convexity proportions
of the response function by harnessing spatio-temporal informa-
tion. Concurrently, utilizing the S-t Attention module enables a
more precise spatio-temporal representation of key parameters in
the sensitive response curves.
Moreover, as observed in Figure 5, we evaluate the model’s online
predicted monotonic response curves both overall and across five
periods, as well as for the top three cities with the most users. The
fitting results for both the ablated and complete versions of CoMAN
more closely approximate the ground truth distribution compared
to the baseline, further verifying CoMAN’s effective capture of
spatio-temporal characteristics in real-world marketing campaigns.
Online A/B Test We deploy our methodology to the Ele.me and
conduct a two-week online A/B test. Compared with the online
baseline model, our proposed model can bring more benefits while
maintaining platform subsidies unchanged or even reduced, helping
the marketing business improve budget efficiency and bring more
growth. Detailed online outcomes as shown in Table 4.
Notably, within the regional pricing strategy for the delivery
fee waiver marketing campaign, the CoMAN model also facilitates
substantial business benefits for the platform. This is achieved even
with a reduction in subsidy intensity by 0.76%, leading to a 0.70%
increase in orders growth, a 0.62% improvement in the CTCVR, and
a 1.06% increment in GMV.
Table 4: Online Business Performance Metrics. In comparison
to the online FPM method, the CoMAN model demonstrated
an improvement rate in the marketing of Ele.me.
Model CVR GMV Orders
CoMAN-B +0.82% +0.10% +0.45%
CoMAN w/o AA +1.20% +0.51% +1.56%
CoMAN w/o S-t +2.18% +3.02% +3.57%
CoMAN +3.09% +3.63% +3.68%
6 CONCLUSION
In this paper, we propose a novel constrained monotonic response
model CoMAN for enhancing monotonic modeling by adaptive
spatio-temporal awareness in diverse takeaway marketing. Specifi-
cally, we employ two spatio-temporal perception modules to acti-
vate and capture the spatio-temporal traits in the attribute represen-
tations. Subsequently, within the monotonic layer, we design two
modules that utilize spatio-temporal information to enhance adap-
tive learning of concavity and convexity, as well as the sensitivity
function expression. Comprehensive offline and online A/B testing
conducted within two marketing campaigns on the Ele.me platform

Enhancing Monotonic Modeling with Spatio-Temporal Adaptive Awareness in Diverse Marketing Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
demonstrates the superiority of our proposed approach. Eventually,
studies prove that our model more accurately reflects users’ incen-
tive sensitivity across different locations and periods and exhibits
superior pricing performance in various spatio-temporal dimen-
sions, thus achieving the goal of improved marketing efficiency.
Furthermore, future research will delve into the finer extraction
of user sensitivity differences to incentives across disparate spatio-
temporal dimensions.
REFERENCES
[1] Norman P Archer and Shouhong Wang. 1993. Application of the back propa-
gation neural network algorithm with monotonicity constraints for two-group
classification problems. Decision Sciences 24, 1 (1993), 60–75.
[2] Samaneh Beheshti-Kashi, Hamid Reza Karimi, Klaus-Dieter Thoben, Michael
Lütjen, and Michael Teucke. 2015. A survey on retail sales forecasting and
prediction in fashion markets. Systems Science & Control Engineering 3, 1 (2015),
154–161.
[3] Craig Boutilier and Tyler Lu. 2016. Budget Allocation using Weakly Coupled,
Constrained Markov Decision Processes.. In UAI.
[4] Djork-Arné Clevert, Thomas Unterthiner, and Sepp Hochreiter. 2015. Fast and
accurate deep network learning by exponential linear units (elus). arXiv preprint
arXiv:1511.07289 (2015).
[5] George Cybenko. 1989. Approximation by superpositions of a sigmoidal function.
Mathematics of control, signals and systems 2, 4 (1989), 303–314.
[6] Hennie Daniels and Marina Velikova. 2010. Monotone and partially monotone
neural networks. IEEE Transactions on Neural Networks 21, 6 (2010), 906–917.
[7] Boya Du, Shaochuan Lin, Jiong Gao, Xiyu Ji, Mengya Wang, Taotao Zhou, Hengxu
He, Jia Jia, and Ning Hu. 2023. BASM: A Bottom-up Adaptive Spatiotemporal
Model for Online Food Ordering Service. In 2023 IEEE 39th International Confer-
ence on Data Engineering (ICDE) . IEEE, 3549–3562.
[8] Lars Eidnes and Arild Nøkland. 2017. Shifting mean activation towards zero with
bipolar activation functions. arXiv preprint arXiv:1709.04054 (2017).
[9] Tom Fawcett. 2006. An introduction to ROC analysis. Pattern recognition letters
27, 8 (2006), 861–874.
[10] Akhil Gupta, Naman Shukla, Lavanya Marla, Arinbjörn Kolbeinsson, and Kartik
Yellepeddi. 2019. How to incorporate monotonicity in deep networks while
preserving flexibility? arXiv preprint arXiv:1909.10662 (2019).
[11] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. 2015. Delving deep
into rectifiers: Surpassing human-level performance on imagenet classification.
In Proceedings of the IEEE international conference on computer vision . 1026–1034.
[12] Dan Hendrycks and Kevin Gimpel. 2016. Gaussian error linear units (gelus).
arXiv preprint arXiv:1606.08415 (2016).
[13] Sepp Hochreiter. 1991. Untersuchungen zu dynamischen neuronalen Netzen.
Diploma, Technische Universität München 91, 1 (1991), 31.
[14] Kurt Hornik. 1991. Approximation capabilities of multilayer feedforward net-
works. Neural networks 4, 2 (1991), 251–257.
[15] Rob J Hyndman and Anne B Koehler. 2006. Another look at measures of forecast
accuracy. International journal of forecasting 22, 4 (2006), 679–688.
[16] Shinji Ito and Ryohei Fujimaki. 2017. Optimization beyond prediction: Prescrip-
tive price optimization. In Proceedings of the 23rd ACM SIGKDD international
conference on knowledge discovery and data mining . 1833–1841.
[17] Günter Klambauer, Thomas Unterthiner, Andreas Mayr, and Sepp Hochreiter.
2017. Self-normalizing neural networks.Advances in neural information processing
systems 30 (2017).
[18] Solomon Kullback and Richard A Leibler. 1951. On information and sufficiency.
The annals of mathematical statistics 22, 1 (1951), 79–86.
[19] Shaochuan Lin, Jiayan Pei, Taotao Zhou, Hengxu He, Jia Jia, and Ning Hu. 2023.
Exploring the Spatiotemporal Features of Online Food Recommendation Service.
In Proceedings of the 46th International ACM SIGIR Conference on Research and
Development in Information Retrieval . 3354–3358.
[20] Shaochuan Lin, Yicong Yu, Xiyu Ji, Taotao Zhou, Hengxu He, Zisen Sang, Jia Jia,
Guodong Cao, and Ning Hu. 2022. Spatiotemporal-enhanced network for click-
through rate prediction in location-based services.arXiv preprint arXiv:2209.09427
(2022).
[21] Xingchao Liu, Xing Han, Na Zhang, and Qiang Liu. 2020. Certified monotonic
neural networks. Advances in Neural Information Processing Systems 33 (2020),
15427–15438.
[22] Ziqi Liu, Dong Wang, Qianyu Yu, Zhiqiang Zhang, Yue Shen, Jian Ma, Wenliang
Zhong, Jinjie Gu, Jun Zhou, Shuang Yang, et al . 2019. Graph representation
learning for merchant incentive optimization in mobile payment marketing.
In Proceedings of the 28th ACM International Conference on Information and
Knowledge Management. 2577–2584.
[23] Andrew L Maas, Awni Y Hannun, Andrew Y Ng, et al. 2013. Rectifier nonlineari-
ties improve neural network acoustic models. In Proc. icml, Vol. 30. Atlanta, GA,
3.
[24] Vinod Nair and Geoffrey E Hinton. 2010. Rectified linear units improve re-
stricted boltzmann machines. In Proceedings of the 27th international conference
on machine learning (ICML-10) . 807–814.
[25] Radford M Neal. 1992. Connectionist learning of belief networks. Artificial
intelligence 56, 1 (1992), 71–113.
[26] Karl Pearson. 1895. VII. Note on regression and inheritance in the case of two
parents. proceedings of the royal society of London 58, 347-352 (1895), 240–242.
[27] Allan Pinkus. 1999. Approximation theory of the MLP model in neural networks.
Acta numerica 8 (1999), 143–195.
[28] David E Rumelhart, Geoffrey E Hinton, and Ronald J Williams. 1986. Learning
representations by back-propagating errors. nature 323, 6088 (1986), 533–536.
[29] Davor Runje and Sharath M Shankaranarayana. 2023. Constrained monotonic
neural networks. In International Conference on Machine Learning . PMLR, 29338–
29353.
[30] Jürgen Schmidhuber. 2015. Deep learning in neural networks: An overview.
Neural networks 61 (2015), 85–117.
[31] Wenling Shang, Kihyuk Sohn, Diogo Almeida, and Honglak Lee. 2016. Under-
standing and improving convolutional neural networks via concatenated rectified
linear units. In international conference on machine learning . PMLR, 2217–2225.
[32] Joseph Sill. 1997. Monotonic networks. Advances in neural information processing
systems 10 (1997).
[33] Joseph Sill and Yaser Abu-Mostafa. 1996. Monotonicity hints. Advances in neural
information processing systems 9 (1996).
[34] Aishwarya Sivaraman, Golnoosh Farnadi, Todd Millstein, and Guy Van den
Broeck. 2020. Counterexample-guided learning of monotonic neural networks.
Advances in Neural Information Processing Systems 33 (2020), 11936–11948.
[35] Hongyan Tang, Junning Liu, Ming Zhao, and Xudong Gong. 2020. Progressive
layered extraction (ple): A novel multi-task learning (mtl) model for personalized
recommendations. In Proceedings of the 14th ACM Conference on Recommender
Systems. 269–278.
[36] Cort J Willmott and Kenji Matsuura. 2005. Advantages of the mean absolute
error (MAE) over the root mean square error (RMSE) in assessing average model
performance. Climate research 30, 1 (2005), 79–82.
[37] Seungil You, David Ding, Kevin Canini, Jan Pfeifer, and Maya Gupta. 2017. Deep
lattice networks and partial monotonic functions. Advances in neural information
processing systems 30 (2017).
[38] Li Yu, Zhengwei Wu, Tianchi Cai, Ziqi Liu, Zhiqiang Zhang, Lihong Gu, Xiaodong
Zeng, and Jinjie Gu. 2021. Joint incentive optimization of customer and merchant
in mobile payment marketing. In Proceedings of the AAAI Conference on Artificial
Intelligence, Vol. 35. 15000–15007.
[39] Sergey Zagoruyko and Nikos Komodakis. 2017. Diracnets: Training very deep neu-
ral networks without skip-connections. arXiv preprint arXiv:1706.00388 (2017).
[40] Kui Zhao, Junhao Hua, Ling Yan, Qi Zhang, Huan Xu, and Cheng Yang. 2019. A
unified framework for marketing budget allocation. In Proceedings of the 25th
ACM SIGKDD International Conference on Knowledge Discovery & Data Mining .
1820–1830.

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY Bin Li and HengXu He, et al.
APPENDIX
A MARKETING MONOTONIC
In the Ele.me’s marketing campaigns, we indicate example attributes
that users will be sensitive to in Figure 8 below. Such monotonic
characteristics are also different in different marketing tools. Specif-
ically, in smart full discounts, the user’s conversion rate will show a
monotonic downward trend with respect to the monotonic increase
in the full discount threshold, while with respect to the full discount
amount It shows the opposite nature; in the delivery fee wavier, the
user’s conversion rate shows a monotonic decreasing trend with
the increase in actual paid delivery fees; in the explosive red enve-
lope, it is similar to the intelligent full reduction, with regard to the
exploding red packets. It shows a monotonically increasing trend,
and the red envelope threshold shows a monotonically decreasing
trend. This paper aims to accurately characterize the sensitivity
Figure 8: Monotonic Properties of Marketing Campaign. En-
closed within the red box in the figure are the monotonic
characteristics of various marketing campaigns. Sequentially
from left to right, the attributes represented are the discount
thresholds and amounts in the tiered discount, followed
by the actual and nominal delivery fees in the delivery fee
waiver, and concluding with the coupon amounts and thresh-
olds in the exploding red packets.
relationship between user response conversion probability and in-
centive attributes and to ensure that such predictions maintain high
accuracy under varying spatio-temporal conditions.
B DETAILED PROOFS
B.1 Monotone Universal Approximation
We provide comprehensive proofs for all the theorems and lemmas
presented in the main text of the paper here. The proof of the
universal approximation theorem for monotone functions [ 6] is
presented as follows:
Theorem 2. for any continuous monotone nondecreasing function𝑓 :
𝐾→ R, where𝐾 is a compact subset of R𝑘 , there exists a feedforward
neural network using the sigmoid as the activation function with
at most 𝑘 hidden layers, positive weights,and output 𝑂 such that
|𝑂𝑥−𝑓(𝑥)| <𝜖,for any𝑥∈𝐾 and𝜖 > 0.
Proof. We derive the proof by utilizing mathematical induction
on the input variable𝑘. Assuming the general case where the con-
tinuous monotone undecreasing function 𝑓 > 0 (otherwise, we
can add a constant𝐶 and approximate 𝑓+𝐶 through the neural
network output𝑂, subsequently correcting𝑂 by subtracting the
constant𝐶 at the final output). If𝑓 is strictly monotone increasing
and𝐶∞, then for𝑘 = 1, we have:
𝑓(𝑥) =
∫ ∞
0
H(𝑓(𝑥)− 𝑢)𝑑𝑢 (16)
where H is the Heavyside Function:
H(𝑥) =
(
1 𝑖𝑓 𝑥≥ 0
0 𝑜𝑡ℎ𝑒𝑟𝑤𝑖𝑠𝑒 (17)
Since𝑓 is continuous and increasing, it is therefore invertible. Con-
sequently, the right side of Equation 16 can be expressed as:
𝑓(𝑥) =
∫ ∞
0
H(𝑥−𝑓−1(𝑣))𝑑𝑣 (18)
Moreover, the integral can be approximated arbitrarily closely by a
Riemann sum, hence we have:
𝑁∑︁
𝑖=1
(𝑣𝑖+1−𝑣𝑖)H(𝑥−𝑓−1(𝑣)) (19)
Here,[𝑣𝑖]𝑁 𝑖=1 denotes the partition of the interval[𝑓(𝑎),𝑓(𝑏)]. Cor-
respondingly, consider a fully connected neural network with𝑁
hidden neurons in a layer, where the weights of input𝑥 are set to 1,
the bias term are𝑓−1(𝑣𝑖), and the output weights between neurons
are𝑣𝑖+1−𝑣𝑖 > 0. It is also noteworthy that the Heavyside function
H can be substituted with the sigmoid activation function utilizing
standard approximation parameters.
Assume that Theorem 2 holds for 𝑘− 1 input variables. We
now combine the integral representation in Equation 16 with the
induction hypothesis. For a given 𝑣, we can solve the level set
equation for𝑥𝑘 corresponding to𝑣:𝑓(𝑥1,...,𝑥 𝑘) =𝑣. According to
the implicit function theorem, there exists a function𝑔𝑣 such that:
𝑓(𝑥1,...,𝑔 𝑣(𝑥1,...,𝑥 𝑘−1)) =𝑣 (20)
where𝑔𝑣 is decreasing with respect to 𝑥𝑖. This can be derived
by taking the partial derivative of equation 20 with respect to𝑥𝑖.
Additionally, we have:
H(𝑓(𝑥)− 𝑣) = H(𝑥𝑘−𝑔𝑣(𝑥1,...,𝑥 𝑘−1)) (21)
Analogous to equation 18 in the 1-D case. It remains to show that
the discussion about𝑓(𝑥) <𝑣𝑖𝑓 𝑎𝑛𝑑𝑜𝑛𝑙𝑦𝑖𝑓 𝑥 𝑘 <𝑔𝑣(𝑥1,...,𝑥 𝑘−1)
and 𝑓(𝑥) > 𝑣 𝑖𝑓 𝑎𝑛𝑑 𝑜𝑛𝑙𝑦𝑖𝑓 𝑥𝑘 > 𝑔𝑣(𝑥1,...,𝑥 𝑘−1). Similarly, by
using the Riemann sum to approximate the integral in equation 16,
we obtain the following equation analogous to equation19:
𝑅 =
𝑁∑︁
𝑖=1
(𝑣𝑖+1−𝑣𝑖)H(𝑥𝑘−𝑔𝑣𝑖(𝑥1,...,𝑥 𝑘−1)) (22)
Due to the fact that𝑔𝑣𝑖 is decreasing with respect to all arguments, it
implies that−𝑔𝑣𝑖 is increasing. By leveraging the inductive hypoth-
esis, we can approximate−𝑔𝑣𝑖 with a feedforward neural network
𝑂𝑖, wherein𝑥1,...,𝑥 𝑘−1 are used as inputs. This neural network
consists of𝑘− 1 hidden layers and employs non-negative weights,
ensuring that
|
𝑁∑︁
𝑖=1
(𝑣𝑖+1−𝑣𝑖)H(𝑥𝑘−𝑂𝑖(𝑥1,...,𝑥 𝑘−1))− 𝑅| <𝜖 (23)

Enhancing Monotonic Modeling with Spatio-Temporal Adaptive Awareness in Diverse Marketing Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
the sum in the above expression is infinite. The expression 22 can
be represented as a feedforward neural network with𝑘 inputs and𝑘
hidden layers. Here,𝑘− 1 hidden layers are utilized to approximate
−𝑔𝑣𝑖 , while the𝑘-𝑡ℎ hidden layer is employed to integrate the 𝑁
neural networks that produce outputs𝑂𝑖 and accept𝑥𝑘 as input.
The weights connecting the final hidden layer to the output layer
are defined as𝑣𝑖+1−𝑣𝑖 > 0. Additionally, the input𝑥𝑘 is directly
skip connected to the𝑘-𝑡ℎ hidden layer. The proof can be readily
generalized to encompass continuous non-decreasing functions. For
a continuous function𝑓 we define its convolution with a mollifier
𝐾𝛿 as𝑓𝛿 = 𝑓 ∯𝐾𝛿 .
Therefore,𝑓𝛿 belongs to𝐶∞ and converges uniformly to 𝑓 on
compact subsets as 𝛿 approaches 0. Additionally, 𝑓𝛿 remains an
increasing function because𝐾𝛿 > 0. Select𝛿 such that the inequality
|𝑓−𝑓𝛿| < 𝜖 2 is satisfied. We then approximate𝑓𝛿 using a feedforward
neural network𝑂 such that|𝑓𝛿−𝑂| < 𝜖 2 . Consequently, it follows
that|𝑓−𝑂| < 𝜖 2 . If𝑓 is nondecreasing, then approximate𝑓 by𝑓𝛿 :
𝑓𝛿 = 𝑓+𝛿(𝑥1+... +𝑥𝑘) (24)
The aforementioned expression is strictly monotonically increasing
as𝛿 tends to 0.
□
Lemma 1. Let ˘𝜌∈ ˘A. Then the Heavyside function H(𝑥) can be
approximated with ˜𝜌𝐻 on R, where
˜𝜌𝐻(𝑥) =𝛼 ˜𝜌(𝑥)+ 𝛽 (25)
for some𝛼,𝛽 ∈ R and𝛼 > 0.
Proof. Given that ˘𝜌 has a lower bound, taking the limit yields:
𝑐 = lim𝑥→−∞ ˘𝜌(𝑥) =− lim𝑥→+∞ ˆ𝜌(𝑥) < 0 (26)
From equation 11, we have
lim𝑥→−∞ ˜𝜌(𝑥) = lim𝑥→−∞ ˘𝜌(𝑥)− ˘𝜌(1) =𝑐− ˘𝜌(1)
lim𝑥→+∞ ˜𝜌(𝑥) = lim𝑥→+∞ ˆ𝜌(𝑥)+ ˆ𝜌(1) =−(𝑐− ˘𝜌(1)) (27)
Let ˜𝜌H(𝑥) be defined as follows:
˜𝜌H(𝑥) = ˜𝜌(𝑥)− 𝑐+ ˘𝜌(1) 2(−𝑐+ ˘𝜌(1)) (28)
Then
lim𝑎→∞ ˜𝜌H(𝑎·𝑥) = H(𝑥) (29)
□
Lemma 2. Let ˜𝜌𝛼,𝛽 be an activation function for some 𝛼,𝛽 ∈ R,𝛼 >
0, such that for every 𝑥∈ R
˜𝜌𝛼,𝛽 =𝛼 ˜𝜌(𝑥)+ 𝛽 (30)
Then for every constrained montone neural network N𝛼,𝛽 using ˜𝜌𝛼,𝛽
as an activation function(𝑠 =(0, 0, ˜𝑠), there is a constrained monotone
neural networkN using ˜𝜌 as an activation function such that for
every x∈ R𝑛:
N( x) =N𝛼,𝛽(x) (31)
Proof. Letℎ𝑘 be the output of the𝑘-𝑡ℎ constrained linear layer
of a constrained monotonic neural networkN𝛼,𝛽 when given input
𝑥. For each𝑘 > 1, we have:
h1 =|W1|t1· x+ b1
h𝑘 =|W𝑘|t𝑘· y𝑘−1+ b𝑘
y𝑘 = ˜𝜌𝛼,𝛽(h𝑘)
y = h𝑙
(32)
Let𝑙 denote the total number of layers inN𝛼,𝛽 . Accordingly, h𝑘
can be reformulated as follows:
h𝑘 =|W𝑘|t𝑘· y𝑘−1+ b𝑘
=|W𝑘|t𝑘· ˜𝜌𝛼,𝛽(h𝑘−1)+ b𝑘
=|W𝑘|t𝑘·(𝛼 ˜𝜌(h𝑘−1)+𝛽1)+ b𝑘 (with|1| =|h𝑘−1|)
=𝛼|W𝑘|t𝑘· ˜𝜌(h𝑘−1)+𝛽|W𝑘|t𝑘 1+ b𝑘
=|𝛼W𝑘|t𝑘· ˜𝜌(h𝑘−1)+𝛽|W𝑘|𝑡𝑘 1+ b𝑘 (from𝛼 > 0)
=

W′ 𝑘

 𝑡𝑘 · ˜𝜌(h𝑘−1)+ b′ 𝑘
(33)
for W′ 𝑘 =𝛼W𝑘 and b𝑘′ =𝛽|W𝑘|𝑡𝑘 1+ b𝑘. Consequently, for each
𝑥∈ R, the output of the networkN with weights W1, W′ 2,..., W′ 𝑙
and biases b1, b′ 2,..., b′ 𝑙 can be expressed asN( x) =N𝛼,𝛽(x). □
Theorem 3. Let ˘𝜌∈ ˘A. Then any multivariate continuous monotone
function f on a compact subset of R𝑘 can be approximated with a
monotone constrained neural network of at most 𝑘 layers using𝜌 as
the activation function.
Proof. The Heaviside function can be approximated by the sig-
moid function over a closed interval, as lim𝑎→∞𝜎(𝑎𝑥) = H(𝑥).
According to Theorem 2 and Lemma 3, any continuous monotonic
function𝑓 defined on a compact subset of R𝑘 can be approximated
with a monotonic constrained neural network of at most𝑘 layers
using the activation function ˜𝜌H .
From Lemma 2, we can get that any continuous monotone func-
tion 𝑓 on a compact subset of R𝑘 can be approximated with a
monotone constrained neural network with at most𝑘 layers using
𝜌 as the activation function. □
B.2 Convex CLU
The rigorous proof of the convexity of the proposed CLU function
is presented to meet the activation function assumption required
for the CMNN framework.
Proof. The proof of concavity and convexity can be established
through the second derivative test theorem as follows.
Theorem 4. Let𝑓(𝑥) be a continuously differentiable function de-
fined on the interval[𝑎,𝑏], possessing a second derivative on the open
interval(𝑎,𝑏). Then for all 𝑥∈( 𝑎,𝑏), we have: If 𝑓′′(𝑥)≥ 0, then
the𝑓(𝑥) is concave on the interval[𝑎,𝑏]. If𝑓′′(𝑥)≤ 0, then the𝑓(𝑥)
is concave on the interval [𝑎,𝑏].
Given CLU formulated as follows:
𝑦 =
 −𝜔0 2 + 𝜔0 1+𝑒−𝜔1𝑥 if𝑥 < 0
𝑥 otherwise ,𝜔 0 > 0,𝜔 1 > 0 (34)

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY Bin Li and HengXu He, et al.
Initially, for x in the domain 𝑥 > 0, the function simplifies to
𝑦 =𝑥, and its second derivative is evidently equal to 0. Hence, our
analysis will focus on the function domain where𝑥 < 0, and then
we proceed to calculate the second derivative of CLU for𝑥 < 0:
𝜕𝑦
𝜕𝑥 = 𝜔0𝜔1𝑒−𝜔1𝑥 (1+𝑒−𝜔1𝑥)2 (35)
𝜕2𝑦
𝜕𝑥2 =
(−𝜔0𝜔2 1𝑒−𝜔1𝑥)( 1+𝑒−𝜔1𝑥)2+ 2𝜔0(𝜔1𝑒−𝜔1𝑥)2(1+𝑒−𝜔1𝑥)
(1+𝑒−𝜔1𝑥)4
=
(1+𝑒−𝜔1𝑥)(−𝜔0𝜔2 1𝑒−𝜔1𝑥−𝜔0(𝜔1𝑒−𝜔1𝑥)2+ 2𝜔0(𝜔1𝑒−𝜔1𝑥)2)
(1+𝑒−𝜔1𝑥)4
=
(1+𝑒−𝜔1𝑥)(−𝜔0𝜔2 1𝑒−𝜔1𝑥+𝜔0(𝜔1𝑒−𝜔1𝑥)2)
(1+𝑒−𝜔1𝑥)4
=
(1+𝑒−𝜔1𝑥)(𝑒−𝜔1𝑥− 1)(𝜔0𝜔2 1𝑒−𝜔1𝑥)
(1+𝑒−𝜔1𝑥)4 ≥ 0
(36)
□
After verifying that the second derivative of CLU is non-negative
for𝑥 < 0, in accordance with Theorem 4, we can conclude that
CLU is a strictly monotone convex function over its entire domain.
B.3 Methodological Property
Lemma 3. For each𝑖∈ 1,...,𝑛 and 𝑗∈ 1,...,𝑚 , We have the weight
matrix for the features
𝜕ℎ𝑗
𝜕𝑥𝑖
(
≥ 0 if𝑡𝑖 = 1
≤ 0 if𝑡𝑖 =−1 (37)
Proof. From equation 37, we have
h =

W𝑇

t · x+ b (38)
ℎ𝑗 =
∑︁
𝑖
𝑤′ 𝑖,𝑗𝑥𝑖+𝑏𝑗 (39)
𝜕ℎ𝑗
𝜕𝑥𝑖
=𝑤′ 𝑖,𝑗 (40)
Finnaly, from equation 10, we have
𝜕ℎ𝑗
𝜕𝑥𝑖
=
(

𝑤𝑖,𝑗

≥ 0 if𝑡𝑖 = 1
−

𝑤𝑖,𝑗

≤ 0 if𝑡𝑖 =−1 (41)
That is, the parameter𝑡 can be used to indicate the monotonicity
of the model. □
Lemma 4. Let𝑦 = 𝜌𝑠(h). Then for each 𝑗 ∈ 1,...,𝑚 , we have
𝜕𝑦 𝑗
𝜕ℎ𝑖 ≥ 0. Moreover, if s =(𝑚, 0, 0), then 𝜌s 𝑗 is convex, and while
s =(𝑚, 0, 0), then𝜌s 𝑗 is concave.
Proof.
ˆ𝜌(𝑥) =− ˘𝜌(−𝑥) (42)
˜𝜌(𝑥) =
(
˘𝜌(𝑥+ 1)− ˘𝜌(1) if𝑥 < 0
ˆ𝜌(𝑥− 1)− ˆ𝜌(1) otherwise (43)
𝜌s ℎ𝑗  =
 

˘𝜌 ℎ𝑗  if 𝑗≤ ˘𝑠
ˆ𝜌 ℎ𝑗  if ˘𝑠 < 𝑗≤ ˆ𝑠
˜𝜌 ℎ𝑗  otherwise (44)
we have:
𝜕𝑦𝑗
𝜕ℎ𝑗
=
 

˘𝜌′ ℎ𝑗 ≥ 0 if 𝑗≤ ˘𝑠
˘𝜌′ −ℎ𝑗 ≥ 0 if ˘𝑠 < 𝑗≤ ˆ𝑠
˘𝜌′ ℎ𝑗+ 1≥ 0 if ˘𝑠+ ˆ𝑠 < 𝑗 andℎ𝑗 < 0
˘𝜌′ 1−ℎ𝑗 ≥ 0 if ˘𝑠+ ˆ𝑠 < 𝑗 andℎ𝑗≥ 0
(45)
if s =(𝑚, 0, 0), we have the convex function as follows:
𝜌𝑠(h) = ˘𝜌(ℎ𝑗) (46)
Similarly,if s =(0,𝑚, 0), we have the concave function as follows:
𝜌𝑠(h) = ˆ𝜌(ℎ𝑗) (47)
□
Corollary 1. From Lemma 3 and Lemma 4, for each 𝑖∈ 1,...,𝑛 and
𝑗∈ 1,...,𝑚 , we can get that if 𝑡𝑖 = 1, then 𝜕𝑦𝑖 𝜕𝑥𝑖 ≥ 0 and while𝑡𝑖 =−1,
then 𝜕𝑦𝑖 𝜕𝑥𝑖 ≤ 0. Moreover, if s =(𝑚, 0, 0), then 𝜌s 𝑗 is convex, else if
s =(𝑚, 0, 0), then𝜌s 𝑗 is concave.
C IMPLEMENTAL DETAILS
In Table 5, we present the optimal architecture of our model as
derived from experimental results. In the embedding layer, we dis-
tinguish between the discretization of categorical ID features and
numerical features, setting the embedding dimensions for these fea-
tures to 8 and 4, respectively. Additionally, in the S-t attention mod-
ule and the FPM, we carefully select the final activation functions
for each parameter. Specifically, for the MLP networks learning𝜔1
and𝜔2, we employ a combination of Leaky ReLU and Softplus to
learn non-negative parameters, whereas for𝜔0 and𝜔3, we utilize
the sigmoid function to learn the probability.
Table 5: Training configurations of the model architecture.
Module Size Activation Dropout
Embedding 400×{ 8, 4} - -
Experts Net 512× 256× 128 ReLU 0.3
Gating Net 128× 64× 3 {ReLU, Softmax} 0.3
Tower Net 128× 64 ReLU 0.3
CMNN 64× 1 {CLU, FPM} 0
S-t 32× 1 {LeakyReLU,
softplus(𝜔1,𝜔2),
sigmoid(𝜔0,𝜔3)}
0.3
AA 64× 3 ReLU 0.3
