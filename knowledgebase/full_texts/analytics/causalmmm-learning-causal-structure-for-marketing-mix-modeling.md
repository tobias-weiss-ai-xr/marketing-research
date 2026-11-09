---
title: 'CausalMMM: Learning Causal Structure for Marketing Mix Modeling'
url: https://arxiv.org/abs/2406.16728
category: analytics
subcategory: measurement
date: 2024-03
venue: ''
authors:
- C. Gong
- Di Yao
- Lei Zhang
source: arxiv
pdf_url: https://arxiv.org/pdf/2406.16728
pages: 12
chars: 63623
fetched_at: '2026-11-08T12:57:41+00:00'
kb_version: 1
---

# CausalMMM: Learning Causal Structure for Marketing Mix Modeling

CausalMMM: Learning Causal Structure for Marketing Mix
Modeling
Chang Gong
Institute of Computing Technology,
Chinese Academy of Sciences
University of Chinese Academy of
Sciences
China
gongchang21z@ict.ac.cn
Di Yao∗
Institute of Computing Technology,
Chinese Academy of Sciences
China
yaodi@ict.ac.cn
Lei Zhang
Independent Researcher
China
zhanglei342@gmail.com
Sheng Chen
Independent Researcher
China
chensheng.cn@gmail.com
Wenbin Li
Institute of Computing Technology,
Chinese Academy of Sciences
University of Chinese Academy of
Sciences
China
liwenbin20z@ict.ac.cn
Yueyang Su
Institute of Computing Technology,
Chinese Academy of Sciences
University of Chinese Academy of
Sciences
China
suyueyang19b@ict.ac.cn
Jingping Bi∗
Institute of Computing Technology,
Chinese Academy of Sciences
China
bjp@ict.ac.cn
ABSTRACT
In online advertising, marketing mix modeling (MMM) is employed
to predict the gross merchandise volume (GMV) of brand shops
and help decision-makers to adjust the budget allocation of vari-
ous advertising channels. Traditional MMM methods leveraging
regression techniques can only capture linear relationships and fail
in handling the complexity of marketing. Although some efforts
try to encode the causal structures for better prediction, they have
the strict restriction that causal structures are prior-known and
unchangeable. In this paper, we define a new causal MMM prob-
lem that automatically discovers the interpretable causal structures
from data and yields better GMV predictions. To achieve causal
MMM, two essential challenges should be addressed: (1) Causal Het-
erogeneity. The causal structures of different kinds of shops vary a
lot. (2) Marketing Response Patterns. Various marketing response
patterns i.e., carryover effect and shape effect, have been validated
in practice. We argue that causal MMM needs dynamically discover
specific causal structures for different shops and the predictions
should comply with the prior known marketing response patterns.
Thus, we propose CausalMMM that integrates Granger causality in
a variational inference framework to measure the causal relation-
ships between different channels and predict the GMV with the
regularization of both temporal and saturation marketing response
patterns. Extensive experiments show that CausalMMM can not only
achieve superior performance of causal structure learning on syn-
thetic datasets with improvements of5.7%∼ 7.1%, but also enhance
∗Corresponding authors.
the GMV prediction results on a representative E-commerce plat-
form.
KEYWORDS
Causal Structure Learning; Causal Discovery; Marketing Mix Mod-
eling
1 INTRODUCTION
Online advertising platforms enable advertisers to launch their ads
on various marketing channels, e.g., paid search, feed stream, and
etc. How to allocate advertising budget on different channels to
maximize the GMV remains a critical yet unsettled issue. Marketing
mix modeling, short for MMM, try to address this issue as a pre-
diction problem. Taking channel costs and shop attributes as input,
MMM methods aim to predict the GMV in the future and estimate
the effectiveness of costs in sales. The results can shed light on
advertising cost control and performance growth. Therefore, MMM
is of vital importance for both advertisers and online platforms.
In the last decade, MMM has become a popular problem and
attracted many researchers. Because advertisers need reasons for
making decisions, interpretability is essential for MMM and simple
models are preferred to be used as the predictor. The majority
of existing works can be divided into two categories, regression-
based methods [39, 41] and causal-based methods [8]. Methods in
the first category [9, 27] predict the GMV with the regression of
different channel costs and employ the coefficients as evidence of
interpretation. The implicit assumption is that the influences of all
channels are independent and would be direct causes of GMV. This
assumption can be easily violated in practice, e.g., ads in display
arXiv:2406.16728v1  [cs.AI]  24 Jun 2024

WSDM ’24, March 4–8, 2024, Mérida, Yucatán, Mexico Chang Gong et al.
Figure 1: The motivation of CausalMMM. (a) shows heteroge-
neous causal structures in MMM where nodes in different
colors denote channel and target variables, respectively. (b)
illustrates the saturation curve of marketing response deter-
mined by contextual factors, such as economy, events, etc..
channels increasing users’ awareness will promote search channels
to deals. Regression-based methods ignore this effect leading to
their poor performance. For causal-based methods, an ad-hoc causal
structure of channels is pre-defined as the prior knowledge to build
the prediction model. However, for different shops, the influences of
channels are also different. Without considering the heterogeneity,
this kind of method can not be used to guide decision-making
accurately. Moreover, current MMM methods predict the GMV with
linear models, which can not capture the complexity of marketing.
Witnessing the drawbacks of current works, we argue that MMM
should be able to dynamically discover the causal structures of dif-
ferent channels and predict the GMV in small error. Thus, a new
task causal MMM is defined in this paper. Compared with tradi-
tional MMM, causal MMM integrates the causal structure learning
of channels into the GMV prediction and interprets channels’ influ-
ences with the effectiveness of causal relations. Benefitting from
explicitly discovered causal structure, the model can be easily gen-
eralized on long-term predictions and the advertisers gain new
insights.
Nevertheless, it’s often non-trivial to achieve causal MMM. The
reasons are two folds: (1) Causal Heterogeneity. The causal struc-
tures and dynamics of channels vary according to the characters of
shops and in different periods. As shown in Figure 1(a), the under-
lying causal drivers of sales volume and the curves of marketing
response are often heterogeneous across different brands’ profiles
and marketing events. The causal effect between brand ads and
page views in beauty shops are decisive compared with menswear
shops. This heterogeneity of causal structures is further challenging
to discover under the circumstance of data imbalance. (2) Market-
ing Response Patterns. In previous studies [16, 19, 25], several
important patterns in advertising response, such as carryover effect
and saturation effect, have been validated. As illustrated in Figure 1,
the influence of advertising investment has time decay and would
be saturated with the increase of investment. In addition to the
causal structure, GMV curves are also affected by some contextual
variables such as economy and competition. Thus, the predictor
in causal MMM should be designed carefully to satisfy marketing
response patterns.
To address these challenges, we propose a novel marketing mix
model, called CausalMMM, which tackles both causal heterogene-
ity and marketing patterns simultaneously and achieves causal
MMM. Overall, CausalMMM is a graph variational autoencoder-
based method, which consists of two key modules: the causal rela-
tional encoder and the marketing response decoder. Although the
causal structures are heterogeneous, the causal mechanisms are
shared in different shops. Thus, in causal relational encoder, we
encode the historic data of shops to generate the specified causal
structures with Gumbel softmax sampling. Based on the causal
structure, the marketing response decoder is designed to satisfy the
priors of marketing response patterns and achieve good prediction
performance. The sequential models and S-curve transformation
are integrated into the decoder to capture the carryover and satura-
tion effects respectively. For optimization, CausalMMM directly fits
the historical data with the variational inference loss and learns
the parameters in an end-to-end manner. Moreover, CausalMMM
has a theoretical guarantee that the obtained causal structures are
Granger causality. In a nutshell, the contributions of this paper are
summarized as follows:
• We define a new task, called causal MMM, which discovers
the causal relations among channels and marketing targets.
Compared with traditional MMM, the new task provides
more insights for decision-makers in online advertising.
• We propose a novel method CausalMMM, which is the first
neural network-based solution for MMM problem. It is prov-
able for learning heterogeneous Granger causal structures
of different shops and capable of modeling patterns in mar-
keting response.
• Extensive experiments on a synthetic dataset and a real-
world dataset from an E-commerce platform demonstrate
CausalMMM’s superiority. It not only shows its effectiveness
on causal structure learning with improvements of 5.7%∼
7.1% on a synthetic dataset, but also can derive comparative
prediction results on a real-world dataset.
2 PRELIMINARY
2.1 Causality Basics
Granger causality [15] is a widely used method for inferring causal
relationships from observational temporal data, based on the as-
sumption that causes precede their effects. It indicates that if know-
ing past elements of X can enhance the prediction of future Y, then
X “Granger causes” Y. Granger causality was initially defined for
linear relationships. To extend to more general cases, we follow the
formal definition of [20, 22, 24, 36] for non-linear Granger causality.
Definition 1 (Non-Linear Granger Causality):Given𝑑 time-series
X =(x1:𝑇 1 ,..., x1:𝑇 𝑑 ) across𝑇 time points and a non-linear function 𝑔𝑗 ,
x𝑡+1 𝑗 =𝑔𝑗(x1:𝑡 1 ,..., x1:𝑡 𝑑 )+ 𝝐𝑡+1 𝑗
where 𝝐𝑡+1 𝑗 denotes independent noise. Time-series 𝑖 Granger causes
𝑗, if𝑔𝑗 depends on x1:𝑡 𝑖 , i.e.

CausalMMM: Learning Causal Structure for Marketing Mix Modeling WSDM ’24, March 4–8, 2024, Mérida, Yucatán, Mexico
Table 1: The primary notations in this paper.
Marketing Mix Data
𝑁 Number of shops or brands
D Marketing mix dataset
X The advertising spend records of𝑑 channels in𝑇 days
y1:𝑇 Historical values of marketing target, e.g., GMV
C Vector of contextual variable
Graph Structures
G =(V,E) Causal structureG with set of nodesV and set of edgesE
𝑣𝑖 A node𝑣𝑖∈V
𝑒𝑖 𝑗 A directed edge𝑒𝑖 𝑗∈E from𝑣𝑖 to𝑣𝑗
Model Architecture
𝑞𝜙,𝑝 𝜃 The encoder and the decoder, respectively
𝑓enc,𝑓 dec Synonyms for the encoder and the decoder, respectively
𝑓vertex,𝑓 edge Node-specific and edge-specific neural networks
𝑓seq,𝑓 pre The sequence model and the prediction model in decoder
𝑓𝛼,𝑓 𝛾 Neural networks control the shape of saturation curves
h𝑙 𝑖, h𝑙 𝑖 𝑗 The embedding of node𝑣𝑖 and edge𝑒𝑖𝑗 in the𝑙-th layer
of the GNNs in the encoder, respectively
˜h𝑡 𝑗, ˜h𝑡 𝑗 The embedding of node𝑣𝑖 and edge𝑒𝑖𝑗 at𝑡 in the decoder
z The latent causal structure matrix
𝑧𝑖 𝑗 Value representing the likelihood of of edge𝑒𝑖 𝑗
MSG𝑡 𝑗 The aggregate causal information for node𝑣𝑗 at𝑡
𝝁𝑡+1 𝑗 The mean value of prediction for node𝑣𝑗 at𝑡+ 1
𝜆 The penalty factor of the structural prior
𝜏 The temperature parameter
∃x1:𝑡 𝑖 ≠ x′1:𝑡 𝑖 , 𝑔𝑗(x1:𝑡 1 ,..., x1:𝑡 𝑖 ,..., x1:𝑡 𝑑 ) ≠𝑔𝑗(x1:𝑡 1 ,..., x′1:𝑡 𝑖 ,..., x1:𝑡 𝑑 ).
Given the formal definition, Granger causality can be summa-
rized by a directed graph G ={V,E}, referred to as summary
graph [3]. Here,V is the set of vertices corresponding to variables,
andE =

(𝑖,𝑗) : x𝑖→ x𝑗

is the set of edges corresponding to
Granger causal relations. Let A denote the adjacency matrix ofG,
the causal structure learning, or causal discovery, problem is then
to estimate A from observational temporal data.
2.2 Problem Definition
In this paper, we study the problem of causal MMM based on a
marketing mix dataset, which aims to build a model that simul-
taneously (1) infers causal structure among marketing variables
for each shop; (2) predicts the marketing target complying with
the prior known marketing response patterns. The marketing mix
dataset is defined as:
Definition 2 (Marketing Mix Dataset): A marketing mix dataset
D consists of marketing records from 𝑁 shops. For the 𝑛-th shop,
its record can be formulated as a triplet, i.e., (X𝑛, y𝑛, C𝑛). Xn =
(x1:𝑇 𝑛,1,..., x1:𝑇 𝑛,𝑑) ∈R𝑇×𝑑 is a 𝑑-variate time series representing the
advertising spends on 𝑑 channels. y𝑇𝑛 ∈ R𝑇 is the𝑛-th shop’s mar-
keting target value, e.g., GMV. C𝑛 represents the vector of contextual
variables, including economy indices, event identity, and so on.
The causal MMM problem is based on the premise that there
exists a causal graph G𝑛 ={V𝑛,E𝑛} underlying the marketing
process of each shop 𝑛, whereV𝑛 contains advertising spends
X𝑛 and marketing target y𝑛. Therefore, the goal of causal MMM
Causal
Relational
Encoder
Marketing
Response
Decoder
𝐗1:𝑡, 𝐲1:𝑡
𝐗1:𝑡, 𝐲1:𝑡, 𝐂
𝐗𝑡+1:𝑡+𝑀
𝐲𝑡+1:𝑡+𝑀
𝓖
Figure 2: The overview of CausalMMM. The causal relational
encoder predicts causal structures between marketing vari-
ables X, y. The marketing response decoder learns to predict
marketing variables given their past observations and con-
textual variables. This framework enables us to extract het-
erogeneous causal structures and learn marketing responses,
simultaneously.
problem is formulated as: given a marketing datasetD, (1) infer
causal structures{G1,... ,G𝑁}, and (2) predict marketing target
{y𝑇+1:𝑇+𝑀 1 ,..., y𝑇+1:𝑇+𝑀 𝑁 } for each shop.
2.3 Method Overview
As shown in Figure 2, the proposedCausalMMM contains two concise
parts, i.e., an encoder for causal structure learning, and a decoder
for marketing response modeling. In the encoder, we aim to predict
edges in the causal graph given observed marketing mix data so
that heterogeneous causal structures across different shops can be
mined. In the decoder, the marketing response is modeled under the
inferred causal structures with the regularization of both temporal
and saturation patterns. The temporal marketing response module
conducts message passing on the inferred causal structure by taking
the historical hidden states. The saturation marketing response
module fits S-curve in an explicit way by leveraging learnable
inflexion points and curve factors. After that, we can systematically
learn causal structure among heterogeneous marketing data and
model advertising responses explicitly. The reason whyCausalMMM
able to find Granger causal structures and the model complexity
are analyzed respectively.
3 METHODOLOGY
3.1 Causal Relational Encoder
The causal relational encoder aims to infer the likelihood of causal
relation𝑧𝑖𝑗 based on the historical advertising spend(x1:𝑇 1 ,..., x1:𝑇 𝑑 )
and marketing target y1:𝑇 . To be specific, the joint distribution of
causal structure is denoted as ˛𝑑+1 𝑖=1 ˛𝑑+1 𝑗=1𝑧𝑖𝑗 , where 𝑧𝑖𝑗 = 1 ex-
presses that there exists a directed edge from node𝑖 to 𝑗 (i.e.,𝑒𝑖𝑗 )
and𝑖 ≠ 𝑗. Since the underlying causal structures are not known
in advance, we predict causal relations starting from a fully con-
nected graph. The graph neural network (GNN) [5, 21] is utilized to
propagate information across a fully connected graph and predict
causal edges. The causal relational encoder consists of three proce-
dures, i.e., pairwise embedding, relational interaction, and Gumbel
softmax sampling.
3.1.1 Pairwise Embedding. We first initialize the edge represen-
tation in the fully connected graph through pairwise embedding.
With a slight abuse of notation, (X, y)𝑗 refers to record of the 𝑗-
th channel x1:𝑇 𝑗 (1≤ 𝑗≤ 𝑑), and the record of marketing target
y1:𝑇 (𝑗 =𝑑+ 1) in the rest of the paper. And the formulation of

WSDM ’24, March 4–8, 2024, Mérida, Yucatán, Mexico Chang Gong et al.
Saturation Marketing
Response Module
෩𝒉
𝑓𝑝𝑟𝑒𝑒𝑑𝑔𝑒ሚ𝑓 ෍
𝑆 ⋅
𝑪
𝑧𝑖𝑗
Temporal Marketing
Response Module
𝐗1:𝑡, 𝐲1:𝑡
𝐗𝑡+1
𝐲𝑡+1
𝑓α ⋅ 𝑓γ ⋅
MSG 𝑗 t
ℎ 𝑗 1:𝑡
𝑓𝑠𝑒𝑞
Figure 3: The structure of the marketing response decoder.
At each step, the decoder takes the inferred causal structure z,
the past observation of X, y, and the historical hidden states
˜h𝑡+1 as input to model marketing response.
pairwise embedding is as follows:
h1 𝑗 = 𝑓emb (X, y)𝑗 ,
h1 𝑖𝑗 = 𝑓 1 edge [h1 𝑖, h1 𝑗],
where h1 𝑗 denotes node representation and h1 𝑖𝑗 denotes pairwise
representation.𝑓emb and𝑓 1 edge are fully-connected networks (MLPs).
It captures local information in a pairwise manner.
3.1.2 Relational Interaction. To take the relational interaction with
other nodes, a.k.a., global information, into account, we further
calculate the edge embedding h𝑖𝑗 as formulated below:
h2 𝑗 = 𝑓 1 vertex ∑︁
𝑖≠𝑗
h1 𝑖𝑗 ,
h2 𝑖𝑗 = 𝑓 2 edge [h2 𝑖, h2 𝑗],
where𝑓 1 vertex and𝑓 2 edge are implemented based on MLPs as well.
3.1.3 Gumbel Softmax Sampling. The above formulation can be
summarized by𝑓enc(·) to derive structure distribution as follows:
h𝑖𝑗 = 𝑓enc(X, y),
𝑞𝜙
z|( X, y) = Softmax(h𝑖𝑗/𝜏),
where𝜏 is the temperature parameter that controls the smoothness
of sampling. As latent distribution 𝑞𝜙
z|( X, y) are discrete and
cannot be backpropagated through the reparametrization trick, we
add Gumbel distributed noise [18] during training:
z𝑖𝑗 ∼ Softmax(h𝑖𝑗+ g/𝜏),
where g are i.i.d. samples drawn from a Gumbel(0, 1) distribution.
z represents the inferred causal structures.
3.2 Marketing Response Decoder
The aim of the decoder is to model marketing response under the
inferred causal structures. Although the complex causal interaction
can be modeled owing to the above inferred causal structures, other
marketing patterns are still unignorable. There are two typical
hypotheses in marketing mix modeling [19, 41]:
Hypothesis 1 (Temporal Marketing Response): Investments on
advertising channels have lagged and decay effect over time, a.k.a,
carryover effect.
Hypothesis 2 (Saturation Marketing Response): Investments on
advertising channels have diminishing returns.
How to systematically model both temporal and saturation pat-
terns is a nonnegligible issue. In most cases, channel cost at each
time period is relatively small compared to that of cumulative chan-
nel cost across each time point. Therefore, we first model temporal
patterns and then saturation patterns. As shown in Figure 3, the
marketing response decoder consists of two procedures, i.e., tempo-
ral marketing response module, and saturation marketing response
module.
3.2.1 Temporal Marketing Response Module. To incorporate tem-
poral patterns, we add sequence models to the original message-
passing mechanisms in GNNs. More formally:
˜h𝑡 𝑖𝑗 = ˜𝑓edge [( X, y)𝑡 𝑖,(X, y)𝑡 𝑗],
MSG𝑡 𝑗 = ∑︁
𝑖≠𝑗
𝑧𝑖𝑗 ˜h𝑡 𝑖𝑗, (1)
˜h𝑡+1 𝑗 = 𝑓seq MSG𝑡 𝑗, ˜h1:𝑡 𝑗 ,
𝝁𝑡+1 𝑗 = 𝑓pre  ˜h𝑡+1 𝑗 ,(X, y)𝑡 𝑗 , 𝑗 = 1,...,𝑑
where the recurrent hidden states at the previous time step are
leveraged for the message-passing mechanism.𝑓seq is the sequence
model implemented with RNN here, which takes MSG𝑡 𝑗 together
with the current value(X, y)𝑡 𝑗 and the previous hidden states ˜h1:𝑡 𝑗 as
input to capture the temporal pattern for each marketing variable.
𝑓pre is modeled by MLPs.
3.2.2 Saturation Marketing Response Module. The diminishing re-
turn is vital to marketing decision-making as it reflects rational
dynamics between marketing investment and response. In this
module, we focus on S-curve (Hill) transformation, which is the
most widely used for modeling saturation[19], and we adopt it in a
gradient-based way in predicting marketing target y𝑡+1.
The vanilla S-curve𝑆(·) for channels’ saturation effect on y is
defined as follows:
Saturation effect = Temporal effect𝛼
Temporal effect𝛼+𝛾,
where𝛼 manipulates the shape of the curve between exponential
and S-shape, whereas𝛾 indicates the inflexion point of the response
curve. Their values are influenced by the character of the market.
We model𝛼,𝛾 through neural networks by taking the vector of
contextual variable C. This brings stronger representation power
and interpretability to the model, as side information including
shop type, event, and macro trend can be used to determine the
shape of the saturation curve. To be specific, the traditional S-curve
model for the marketing target is extended to the following form:
𝝁𝑡+1 𝑗 = 𝑓pre
 ˜h𝑡+1 𝑗 ,(X, y)𝑡 𝑗 𝑓𝛼(C)
𝑓pre
 ˜h𝑡+1 𝑗 ,(X, y)𝑡 𝑗 𝑓𝛼(C)+𝑓𝛾(C) , 𝑗 =𝑑+ 1
where 𝑓𝛾(·) denotes a neural network to calculate the inflexion
point of the market, and 𝑓𝛼(·) is a neural network whose output
controls the shape of the curve between exponential and S-shape. In
this module, the capability of neural networks and the explicitness
of S-curve is integrated.

CausalMMM: Learning Causal Structure for Marketing Mix Modeling WSDM ’24, March 4–8, 2024, Mérida, Yucatán, Mexico
Based on the above two modules, we can derive 𝝁𝑡+1 1:𝑑+1 charac-
terizing the prediction value of𝑑-variate channels and marketing
target, respectively. The ultimate value is given as follows:
𝑝𝜃
(X𝑡+1, y𝑡+1)|( X1:𝑡, y1:𝑡), z =N𝝁𝑡+1 1:𝑑+1,𝜎 2I,
where𝜎 is the fixed variance term. For multiple-step forecasting,
the prediction results 𝝁𝑡+𝑚 𝑗 is utilized in a recursive manner, i.e.,
𝝁𝑡+1 = 𝑓dec (X, y)𝑡,𝑓 enc(X, y),
𝝁𝑡+𝑚 = 𝑓dec 𝝁𝑡+𝑚−1,𝑓 enc(X, y), 𝑚 = 2,...,𝑀
where𝑀(𝑀≥ 1) is the number of time steps to predict.
3.3 Variational Inference for Optimization
This section gives the optimization procedure with variational infer-
ence. The parameters of𝑓enc and𝑓dec detailed above can be derived
according to the following form :
𝑓enc∗,𝑓 dec∗ = argmin𝑓enc,𝑓decL(D,𝑓 enc,𝑓 dec),
where the loss function is composed of a data-fitting term and a
structural regularization term, i.e.,
L(D,𝑓 enc,𝑓 dec)
=
∑︁
𝑛
∑︁
𝑡
𝑙

(X, y)𝑡+1:𝑡+𝑀,𝑓 dec (X, y)1:𝑡,𝑓 enc(X, y)
+𝜆·𝑟𝑓enc(X, y), (2)
where𝜆 is a penalty factor of the structural prior. We further lever-
age variational inference to model the functions𝑓enc and𝑓dec. As the
causal relational encoder𝑓enc via encoding function𝑞𝜙
z|( X, y)
deriving a distribution over z which represents the predicted edges
in the causal structure, and a decoder𝑝𝜃
(X, y)| z that probabilisti-
cally models marketing response under the inferred causal struc-
ture. Thus, the loss functionL(D,𝑓 enc,𝑓 dec) in Equation 2 can be
reformulated as a variational lower bound:
L = E𝑞𝜙(z|( X,y))

log𝑝𝜃
(X, y)| z −𝜆· KL  𝑞𝜙 z|( X, y)||𝑝(z)  ,
where the first term is a negative log-likelihood for data fitting, and
the second term is a KL divergence to a structural prior distribution
for regularization.
3.4 Theoretical Analysis of CausalMMM
This section first gives the theoretical analysis that we can infer
Granger causality in the framework of CausalMMM. Then the com-
putational complexity of the proposed method is analyzed.
Aligning with the definition of non-linear Granger causality,
our CausalMMM is on the premise that there exists some function𝑔
describing the marketing response of any shop or brand∀𝑛,(1≤
𝑛≤𝑁) given its historical marketing mix dataset(X𝑛, y𝑛)1:𝑡 and its
underlying causal structureG𝑛:(X, y)𝑡+1 =𝑔(X, y)1:𝑡,G𝑛 + 𝝐𝑡+1𝑛 .
The unknown components of the data-generation process above
can be divided into two parts: (1) the causal structureG𝑛 specific
to the 𝑛-th shop; (2) the mapping 𝑔 of marketing response. We
make the following claim, and details of our proof can be found in
Appendix A.1.1.
Claim 1 (Granger Causality of CausalMMM): For the𝑛-th sample
in dataset, the variable x𝑛,𝑖 does not Granger cause variable x𝑛,𝑗 , if
𝑧𝑛,𝑖𝑗 = 0 according to CausalMMM.
We then discuss the computational complexity of the proposed
CausalMMM in both training and causal relations inference stages.
For a shop’s marketing mix records consisting of𝑇 days, their time
complexities areO(𝑊𝑇) andO(𝑊), respectively, where𝑊 is the
number of weights. A detailed analysis of each component can be
found in Appendix A.1.2. The time complexity of the whole model
isO(𝑊𝑇). Appendix A.3.2 provides a comparison between training
time on simulated datasets with varying sizes. According to the
results, CausalMMM scales linearity with the increase in training
data size. Thus, it’s promising to handle massive marketing data
from a large number of shops.
4 EXPERIMENT
In this section, we evaluate the performance of CausalMMM and
answer the following research question:
• RQ1: As a framework based on temporal causal discovery,
can CausalMMM accurately recover causal structures from
heterogeneous marketing data?
• RQ2: What is the performance of CausalMMM in terms of
predicting the target variable?
• RQ3: Can causal structures discovered by CausalMMM align
with expert knowledge on real-world datasets?
• RQ4: What are the capabilities of the causal relational en-
coder, the temporal marketing response module, and the
saturation marketing response module?
4.1 Experimental Settings
This section provides an overview of the data, experimental proto-
col, evaluation metrics, and compared baselines.
Table 2: Dataset statistics
Dataset Shops Channels Context variables Length
Simulation 1 50 (5,10,20) - (30,120,720)
Simulation 2 100 (5,10,20) 2 (30,120,720)
AirMMM 50 12 5 676
4.1.1 Data Descriptions. The performance of CausalMMM is evalu-
ated on two datasets. The first dataset is a synthetic dataset created
to test CausalMMM’s ability to reconstruct causal structures. The data
generation procedure consists of three steps, i.e., graph sampling,
channel generation, and response generation. Compared to Simu-
lation 1, the saturation curve in Simulation 2 is characterized by
contextual variables. We further adjust the channel numbers and
lengths in simulation to test the effectiveness of CausalMMM under
different conditions. The detailed data generation procedure can be
found in Appendix A.2.1. The second, AirMMM, is a real-world
marketing mix dataset collected from an E-commerce platform,
which contains 50 shops’ marketing mix data with a period of 22
months from Jan 30th 2021 to Dec 6th 2022. Appendix A.2.2 de-
scribes the details of advertising channels in AirMMM. The statistics
on two marketing mix datasets are shown in Table 2.
4.1.2 Experimental Protocol. We conduct experiments on two data-
sets to evaluateCausalMMM’s performance. For the synthetic dataset,
we simulate heterogeneous longitudinal data in settings with and
without saturation patterns and we quantify the ability ofCausalMMM

WSDM ’24, March 4–8, 2024, Mérida, Yucatán, Mexico Chang Gong et al.
to reconstruct causal structures (Section 4.2). For the real-world
dataset, we compare CausalMMM’s performance in terms of GMV
prediction to that of two categories of state-of-the-art methods, i.e.,
marketing mix models and temporal causal discovery models (Sec-
tion 4.3). We also report the inferred causal structures on real-world
datasets, which align with domain experts’ knowledge (Section 4.4).
Moreover, we provide the ablation and parameter sensitivity studies
for verifying the effectiveness and robustness of each component
(Section 4.5).
4.1.3 Evaluation Metrics. For evaluating the learned causal struc-
ture against ground truth, two metrics are reported. Accuracy
(ACC), and Areas Under Receiver Operating Characteristic (AUROC).
AUROC is defined as the ratio of true and false positive rates
given the threshold varies between 0 and 1. The prediction of self-
connectivity (i.e., the diagonal part of the adjacency matrix) is not
evaluated in our experiment, which is the easiest relation to infer.
The reported results are averaged over ten random trials. For evalu-
ating the performance of GMV forecasting, the Mean Squared Error
(MSE) metric is used.
4.1.4 Compared Methods. To answer the first question (RQ1), we
compare our CausalMMM method with the following popular base-
lines:
• Linear Granger [2]. As one of the most well-known meth-
ods, it applies the vector autoregressive (VAR) model with
ridge regularization to learn causal structures.
• NGC [36]. It leverages an LSTM or MLP to predict the future
and conduct causal discovery based on input weights.
• GV AR[24]. It’s an interpretable Granger causal structure
learning method which considers both sign effect and time
reversal. Causal links are derived based on self-explaining
neural networks.
• InGRA [12]. It aims to learn Granger causal structures from
heterogeneous MTS based on attention mechanism and pro-
totype learning.
To answer the second question (RQ2), we additionally compare
CausalMMM in terms of GMV forecasting with several competitive
methods as follows:
• LSTM [17]. Its ability to process sequential data with varying
time lags can be utilized for GMV forecasting.
• Wide & Deep [10]. It combines regression and DNN that
benefits from interpretability and representation power.
• BTVC [27]. It’s a time-varying coefficient model based on
hierarchical Bayesian structures for MMM.
To verify the effectiveness of causal relational encoder, temporal
marketing response module, and saturation marketing response
module (RQ4), we introduce some variants ofCausalMMM as follows:
• CM-full. It replaces the causal relational encoder with a
full graph input to the decoder.
• CM-markov. It replaces the temporal marketing response
module with a Markovian module that only captures the
records of the last time step.
• CM-rw. It’s a variant of our method without the saturation
marketing response module.
10 100 1000
Number of shops
0.60
0.65
0.70
0.75
0.80
0.85
0.90
0.95AUROC
CausalMMM
InGRA
Linear Granger
NGC
GVAR
Figure 4: Causal structure learning performance (in AUROC)
w.r.t. the number of shops 𝑁 (𝑑 = 10,𝑇 = 120).
4.2 Performance of Causal Structure Learning
(RQ1)
To answer RQ1, we conduct the synthetic experiment. The main
results of causal structure learning are shown in Table 3. To further
exploit the effectiveness of our CausalMMM under heterogeneous
data, we also report ACC and AUROC results in simulation 2 w.r.t.
the channel number𝑑, the series length𝑇 , and the number of latent
causal structures𝑅 in Table 4 to 6. In Figure 4, we illustrate the
model’s performance with the increasing number of shops.
As shown in Table 3, CausalMMM consistently outperforms the
compared baselines with AUROC improvements of 5.7%∼ 7.1%,
which demonstrates its capability in causal structure learning. In-
GRA is the strongest baseline but also inferior to CausalMMM. It
leverages prototype learning, which is helpful to extract prototyp-
ical structures in heterogeneous data. However, InGRA does not
consider the patterns of marketing response, which would harm the
performance, especially in Simulation 2 where a more complicated
marketing response is entailed. In Table 4, we vary𝑑 and generate
heterogeneous datasets. As shown, CausalMMM consistently outper-
forms compared methods across all cases and achieves good per-
formance even when𝑑 reaches 20. It demonstrates that CausalMMM
effectively handles complex structures with a large number of nodes.
In real scenarios, data collected from different shops may have vary-
ing lengths. Thus, we also vary the lengths in the evaluation. As
shown in Table 5, our CausalMMM still outperforms all compared
baselines across different series lengths. We also observe that the
decreases in𝑇 = 30, but CausalMMM exhibits a relatively smaller de-
gree of degradation compared to baselines such as NGC and GVAR.
In Table 6, by adjusting 𝑅 we directly control the heterogeneity.
We witness a performance decrease for InGRA with increasing𝑅,
which is due to the constraints of a pre-defined prototype num-
ber.CausalMMM outperforms InGRA with the optimal performance
achieved at𝑅 = 10. It demonstratesCausalMMM’s capability in causal
structure learning on datasets with more heterogeneous structures.
To explore the model’s ability to utilize heterogeneous samples,
the performance is illustrated in Figure 4 with the increase in 𝑁 .
Although CausalMMM is inferior to baselines such as GVAR and
InGRA in low-data settings, its performance improves steadily when
𝑁 increases. It significantly outperforms other baselines when𝑁≥
100. This also demonstrates CausalMMM’s capability in modeling

CausalMMM: Learning Causal Structure for Marketing Mix Modeling WSDM ’24, March 4–8, 2024, Mérida, Yucatán, Mexico
Table 3: Causal structure reconstruction results with different simulation settings.
Methods Simulation 1 Simulation 2 ACC AUROC ACC AUROC
Linear Granger 0.630 ±0.101 0.628 ±0.147 0.624 ±0.196 0.661 ±0.020
NGC 0.667 ±0.251 0.694 ±0.170 0.596 ±0.235 0.639 ±0.265
GVAR 0.839 ±0.110 0.847 ±0.092 0.784 ±0.148 0.859 ±0.149
InGRA 0.877 ±0.096 0.863 ±0.082 0.856 ±0.098 0.854 ±0.083
CM-rw 0.921±0.037 0.924 ±0.049 0.858 ±0.053 0.871 ±0.071
CM-markov 0.872±0.039 0.887 ±0.051 0.832 ±0.087 0.865 ±0.062
CausalMMM 0.923±0.020 0.935 ±0.012 0.892 ±0.033 0.903 ±0.015
Table 4: Causal structure reconstruction results w.r.t the channel number (𝑅=5,𝑇 =120).
Methods d=5 d=10 d=20 ACC AUROC ACC AUROC ACC AUROC
Linear Granger 0.612 ±0.125 0.644 ±0.017 0.624 ±0.018 0.661 ±0.020 0.580 ±0.116 0.603 ±0.058
NGC 0.623 ±0.278 0.665 ±0.151 0.596 ±0.235 0.639 ±0.265 0.534 ±0.212 0.595 ±0.120
GVAR 0.842 ±0.158 0.884 ±0.072 0.784 ±0.148 0.859 ±0.149 0.792 ±0.146 0.878 ±0.084
InGRA 0.897 ±0.181 0.882 ±0.140 0.856 ±0.098 0.854 ±0.083 0.839 ±0.024 0.872 ±0.059
CM-rw 0.885±0.178 0.842 ±0.153 0.858 ±0.053 0.871 ±0.071 0.836 ±0.025 0.860 ±0.045
CM-markov 0.854±0.157 0.839 ±0.197 0.832 ±0.087 0.865 ±0.062 0.814 ±0.027 0.825 ±0.032
CausalMMM 0.925±0.140 0.910 ±0.187 0.892 ±0.033 0.903 ±0.015 0.875 ±0.109 0.905 ±0.024
Table 5: Causal structure reconstruction results w.r.t the series length (𝑅=5,𝑑=10).
Methods T=30 T=120 T=720 ACC AUROC ACC AUROC ACC AUROC
Linear Granger 0.514 ±0.000 0.581 ±0.000 0.624 ±0.196 0.661 ±0.020 0.735 ±0.152 0.892 ±0.180
NGC 0.573 ±0.051 0.568 ±0.074 0.596 ±0.235 0.639 ±0.265 0.744 ±0.149 0.752 ±0.185
GVAR 0.693 ±0.116 0.716 ±0.095 0.784 ±0.148 0.859 ±0.149 0.886 ±0.084 0.890 ±0.072
InGRA 0.774 ±0.158 0.763 ±0.142 0.856 ±0.098 0.854 ±0.083 0.899 ±0.075 0.907 ±0.061
CM-rw 0.800±0.110 0.815 ±0.105 0.858 ±0.053 0.871 ±0.071 0.914 ±0.008 0.932 ±0.015
CM-markov 0.763±0.103 0.787 ±0.085 0.832 ±0.087 0.865 ±0.062 0.868 ±0.023 0.879 ±0.019
CausalMMM 0.843±0.119 0.852 ±0.127 0.892 ±0.033 0.903 ±0.015 0.941 ±0.031 0.952 ±0.026
Table 6: Causal structure reconstruction results w.r.t. the latent structure number 𝑅 (𝑑=10,𝑇 =120).
Methods R=5 R=10 R=20 ACC AUROC ACC AUROC ACC AUROC
InGRA 0.876 ±0.098 0.874 ±0.083 0.848 ±0.180 0.865 ±0.119 0.815 ±0.137 0.820 ±0.158
CausalMMM 0.892±0.033 0.903 ±0.015 0.918 ±0.057 0.925 ±0.104 0.877 ±0.066 0.882 ±0.029
20
 15
 10
 5
 0 5 10 15
Day
3.4
3.5
3.6
3.7
3.8
3.9
4.0Normalized GMV
   know  T  predict
BTVC
GVAR
CausalMMM
GroundTruth
Figure 5: Visualization results for GMV prediction.
heterogeneous data. And it’s meaningful in real-world scenarios
where the marketing mix data across various shops are leveraged
for sales promotion.
4.3 Performance of GMV Prediction (RQ2)
To answer RQ2, we employ a real-world dataset AirMMM to evalu-
ate the performance of CausalMMM. A detailed comparison and a
visualization of the predicted results will be presented, respectively.
We show MSE results in Table 7, in which methods are compared
under different prediction steps,i.e., 1, 7, 30. We can observe that: (1)
Among all the compared methods, BTVC performs best at𝑀 = 30,
which could be attributed to the helpful role of explicitly incorporat-
ing trend and seasonality information. (2) Our CausalMMM achieves
the best performance at 𝑀 = 7, while attaining the second-best
performance at𝑀 = 1, 30, which demonstrates the effectiveness of
the proposed method.
We also provide the visualization results in Figure 5, including
the future 15-days forecasts of the BTVC, GVAR, and the proposed
CausalMMM. As we can see, when predicting the future 15-days,
the CausalMMM can catch the sudden alteration and perform good

WSDM ’24, March 4–8, 2024, Mérida, Yucatán, Mexico Chang Gong et al.
Table 7: GMV prediction results. The ‘-’ denotes that multi-
step forecasting is not supported in original implementation.
Methods MSE 𝑀 = 1 𝑀 = 7 𝑀 = 30
Linear Granger 0.60 5.96 21.65
NGC 0.55 - -
GVAR 0.37 1.91 12.41
InGRA 0.48 - -
LSTM 0.58 3.31 15.78
Wide & Deep 0.25 - -
BTVC 0.47 2.07 9.43
CM-full 0.37 2.65 14.63
CM-markov 0.32 2.85 12.92
CM-rw 0.38 3.09 12.74
CausalMMM 0.29 1.80 9.55
forecasting in multi-steps with the help of both the marketing
response pattern characterized by contextual variables and learned
causal structures.
4.4 Graph Visualization (RQ3)
To answer RQ3, this section visualizes the learned causal struc-
ture of a beauty store on real-world data. We illustrate the causal
structures of 11 channels, page view (PV), and the marketing target
(i.e., GMV) by CausalMMM and the best from compared methods
in Figure 6. Among the channels, the first six ( i.e., x-brand-0, ...,
x-feed) are brand channels designed to promote users’ awareness
and interest. In contrast, the remaining five (i.e., x-live, ..., x-effect)
are effect channels where users are more likely to take action and
convert. The details of these channels, including the media type
and the means of placement, are described in Appendix A.2.2.
As we can see, causal relations from brand channels to PV, and
PV to effect channels are observed. These results agree with expert
knowledge and are consistent with the conclusions of the market-
ing funnel effect [7]. Our method also suggests several meaningful
relations, including x-brand-1 to x-search-1/2, which indicate the
increase in search volume on the E-commerce platform due to ads
placements on the other video website. Such causal relations, how-
ever, can never be detected or utilized in traditional MMM methods.
Compared against CausalMMM, GVAR and the other baselines fail
to discover these interactions.
x-brand-0
x-brand-1
x-brand-2
x-brand-3
x-interact
x-feed
x-live
x-search-0
x-search-1
x-search-2
x-effect
PV
GMV
x-brand-0
x-brand-1
x-brand-2
x-brand-3
x-interact
x-feed
x-live
x-search-0
x-search-1
x-search-2
x-effect
PV
GMV
Causal structure by our CausalMMM
x-brand-0
x-brand-1
x-brand-2
x-brand-3
x-interact
x-feed
x-live
x-search-0
x-search-1
x-search-2
x-effect
PV
GMV
x-brand-0
x-brand-1
x-brand-2
x-brand-3
x-interact
x-feed
x-live
x-search-0
x-search-1
x-search-2
x-effect
PV
GMV
Causal structure by GVAR
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.2
0.4
0.6
0.8
1.0
Figure 6: Learned causal structure of AirMMM. Causal rela-
tions from brand channels to PV are highlighted in red, and
those from PV to effect channels are highlighted in orange.
4.5 Ablation and Parameter Study (RQ4)
To answer RQ4, we first compare CausalMMM with three ablation
methods. The parameter-sensitive analysis is also included.
We summarize the metrics of ablation studies in Table 3 and Ta-
ble 7. As shown, the AUROCs of CM-rw, CM-markov are inferior
to CausalMMM, which proves that both the saturation marketing
response module and the temporal marketing response module
help improve causal structure learning. We can observe that the
performance of CM-rw is much better than that of CM-markov,
which indicates the temporal pattern is more informative compared
to the saturation pattern in causal structure learning. For GMV fore-
casting, CM-full, CM-markov, and CM-rw have larger prediction
errors than CausalMMM, which demonstrates the effectiveness the
causal relational encoder, the temporal marketing response module,
and the saturation response module. We also observe the improve-
ment of the causal relational encoder is more significant than the
other two modules of the decoder when𝑀 = 30, which indicates
that structural information is important for long-term prediction.
The hyperparameter𝜆 is critical to balance data fitting and struc-
tural regularization. The temperature factor𝜏 controls the “smooth-
ness" of Gumbel softmax sampling. We conduct extensive experi-
ments across a wider range of𝜆 and𝜏, and the results are shown
in Figure 7. AUROC increases steadily and peaks around𝜆 = 102.
It verifies that adjusting𝜆 can control the effect of structural prior
and reasonable values will benefit causal structure learning. Its
performance is relatively stable when the softmax temperature𝜏 is
not too small, which avoids degenerating to one-hot sampling.
5 RELATED WORK
5.1 Marketing Mix Modeling
Marketing mix modeling leverages statistical techniques and his-
torical data to predict marketing targets with respect to advertis-
ing investment [7, 41]. According to whether assuming the causal
structures, existing methods can be divided into two categories.
Approaches in the first category [39, 41] utilize linear regression or
its non-linear variants, on the premise that regressors are mutually
independent. Recent years have witnessed a vast amount of meth-
ods [9, 19, 27, 34, 37] in this category. Albeit extant work [ 7, 27]
raises the multicollinearity concern, it neglects the complex causal
relations among marketing variables. Another category assumes a
predefined causal model [8] that aligns with the channels’ funnel
effects. Given causal diagrams for the paid search channel, causal ef-
fects of advertising on sales are estimated with bias correction in [8].
However, in real-world scenarios with various advertising channels,
the latent causal structures may be complex and heterogeneous
across shops. And no extant work tackles this issue.
5.2 Causal Discovery from Temporal Data
Causal reasoning [30] is an incredibly valuable tool that finds ex-
tensive application in the field of advertising and online market-
ing [6, 11, 35, 45]. The idea of enhancing MMM by modeling causal-
ity among marketing variables is inspired by works in causal dis-
covery from temporal data [3, 14, 26, 38, 40]. Existing works can be
grouped into four categories, i.e., constraint-based methods [13, 23],
score-based methods [29, 33], functional causal model (FCM)-based
methods [31, 43], and Granger causality methods [24, 36]. Among
them, Granger causality [15, 32] is a popular and practical tool for
causal analysis in many real-world applications [1, 28]. To extract
non-linear relations in high-dimensional conditions, a series of

CausalMMM: Learning Causal Structure for Marketing Mix Modeling WSDM ’24, March 4–8, 2024, Mérida, Yucatán, Mexico
Penalty factor
0
100
101
102
103
104
Softmax temperature
 0.01
0.1
0.5
1
5
50
AUROC
0.75
0.80
0.85
0.90
Sim 1
Penalty factor
0
100
101
102
103
104
Softmax temperature
 0.01
0.1
0.5
1
5
50
AUROC
0.70
0.75
0.80
0.85
0.90
Sim 2
Figure 7: Causal structure learning performance w.r.t.𝜆,𝜏.
works [12, 22, 24, 36, 42] have been proposed recently, including
methods based on information regularization [42], component-wise
modeling [20, 36], low-rank approximation [44], self-explaining net-
works [24], and inductive modeling [12]. Most extant works train
a separate model for each sample which cannot take advantage
of the information shared in the whole dataset, except for InGRA
which utilizes prototype learning in heterogeneous time series. Be-
sides, most extant work only designed for causal structure learning
neglects domain-specific patterns in real-world applications.
Different from existing studies, CausalMMM can discover hetero-
geneous causal structures while complying with the prior market-
ing response patterns.
6 CONCLUSION
In this paper, we define the problem of causal MMM, which infers
causal structure for each shop and learns the mapping from chan-
nel spending to target variable prediction. To tackle the issues of
data heterogeneity and marketing response patterns, we propose
CausalMMM, which is both provable for learning causal structure
from heterogeneous data and capable of modeling patterns in mar-
keting response. CausalMMM employs the causal relational encoder
and the marketing response decoder. Extensive experiments on the
synthetic dataset and real commercial data from an E-commerce
platform shows that CausalMMM outperforms the baselines and
works well in real-world applications.
ACKNOWLEDGMENTS
This work has been supported by the National Natural Science
Foundation of China under Grant No.: 62002343 and Alibaba In-
novative Research (AIR) Program. And we would like to express
sincere gratitude to the anonymous reviewers for their valuable
feedback.
REFERENCES
[1] Negar Arabzadeh, Hossein Fani, Fattane Zarrinkalam, Ahmed Navivala, and
Ebrahim Bagheri. 2018. Causal Dependencies for Future Interest Prediction on
Twitter. In Proceedings of the 27th ACM International Conference on Information
and Knowledge Management, CIKM 2018, Torino, Italy, October 22-26, 2018 . ACM,
1511–1514.
[2] Andrew Arnold, Yan Liu, and Naoki Abe. 2007. Temporal causal modeling with
graphical granger methods. In Proceedings of the 13th ACM SIGKDD International
Conference on Knowledge Discovery and Data Mining, San Jose, California, USA,
August 12-15, 2007. ACM, 66–75.
[3] Charles K. Assaad, Emilie Devijver, and Éric Gaussier. 2022. Survey and Evalua-
tion of Causal Discovery Methods for Time Series. J. Artif. Intell. Res. 73 (2022),
767–819. https://doi.org/10.1613/jair.1.13428
[4] Amir F. Atiya and Alexander G. Parlos. 2000. New results on recurrent network
training: unifying the algorithms and accelerating convergence. IEEE Trans.
Neural Networks Learn. Syst. 11, 3 (2000), 697–709.
[5] Ershad Banijamali. 2022. Neural Relational Inference with Node-Specific Infor-
mation. In The Tenth International Conference on Learning Representations, ICLR
2022, Virtual Event, April 25-29, 2022 .
[6] Wei Cai, Fuli Feng, Qifan Wang, Tian Yang, Zhenguang Liu, and Congfu Xu. 2023.
A Causal View for Item-level Effect of Recommendation on User Preference. In
Proceedings of the Sixteenth ACM International Conference on Web Search and Data
Mining, WSDM 2023, Singapore, 27 February 2023 - 3 March 2023 . ACM, 240–248.
[7] David Chan and Mike Perry. 2017. Challenges and opportunities in media mix
modeling. (2017).
[8] Aiyou Chen, David Chan, Mike Perry, Yuxue Jin, Yunting Sun, Yueqing Wang,
and Jim Koehler. 2018. Bias correction for paid search in media mix modeling.
arXiv preprint arXiv:1807.03292 (2018).
[9] Hao Chen, Minguang Zhang, Lanshan Han, and Alvin Lim. 2021. Hierarchical
marketing mix models with sign constraints. Journal of Applied Statistics 48,
13-15 (2021), 2944–2960.
[10] Heng-Tze Cheng, Levent Koc, Jeremiah Harmsen, Tal Shaked, Tushar Chandra,
Hrishi Aradhye, Glen Anderson, Greg Corrado, Wei Chai, Mustafa Ispir, Rohan
Anil, Zakaria Haque, Lichan Hong, Vihan Jain, Xiaobing Liu, and Hemal Shah.
2016. Wide & Deep Learning for Recommender Systems. In Proceedings of the
1st Workshop on Deep Learning for Recommender Systems, DLRS@RecSys 2016,
Boston, MA, USA, September 15, 2016 . ACM, 7–10.
[11] Lu Cheng, Ruocheng Guo, and Huan Liu. 2022. Estimating Causal Effects of Multi-
Aspect Online Reviews with Multi-Modal Proxies. In WSDM ’22: The Fifteenth
ACM International Conference on Web Search and Data Mining, Virtual Event /
Tempe, AZ, USA, February 21 - 25, 2022 . ACM, 103–112.
[12] Yunfei Chu, Xiaowei Wang, Jianxin Ma, Kunyang Jia, Jingren Zhou, and Hongxia
Yang. 2020. Inductive Granger Causal Modeling for Multivariate Time Series. In
20th IEEE International Conference on Data Mining, ICDM 2020, Sorrento, Italy,
November 17-20, 2020. 972–977.
[13] Andreas Gerhardus and Jakob Runge. 2020. High-recall causal discovery for
autocorrelated time series with latent confounders. In Advances in Neural Infor-
mation Processing Systems 33: Annual Conference on Neural Information Processing
Systems 2020, NeurIPS 2020, December 6-12, 2020, virtual .
[14] Chang Gong, Di Yao, Chuzhe Zhang, Wenbin Li, Jingping Bi, Lun Du, and Jin
Wang. 2023. Causal Discovery from Temporal Data. In Proceedings of the 29th
ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD ’23) .
5803–5804.
[15] Clive WJ Granger. 1969. Investigating causal relations by econometric models
and cross-spectral methods. Econometrica: journal of the Econometric Society
(1969), 424–438.
[16] Dominique M Hanssens, Leonard J Parsons, and Randall L Schultz. 2003. Market
response models: Econometric and time series analysis . Vol. 2. Springer Science &
Business Media.
[17] Sepp Hochreiter and Jürgen Schmidhuber. 1997. Long Short-Term Memory.
Neural Comput. 9, 8 (1997), 1735–1780.
[18] Eric Jang, Shixiang Gu, and Ben Poole. 2017. Categorical Reparameterization with
Gumbel-Softmax. In 5th International Conference on Learning Representations,
ICLR 2017, Toulon, France, April 24-26, 2017, Conference Track Proceedings .
[19] Yuxue Jin, Yueqing Wang, Yunting Sun, David Chan, and Jim Koehler. 2017.
Bayesian methods for media mix modeling with carryover and shape effects.
(2017).
[20] Saurabh Khanna and Vincent Y. F. Tan. 2020. Economy Statistical Recurrent
Units For Inferring Nonlinear Granger Causality. In 8th International Conference
on Learning Representations, ICLR 2020, Addis Ababa, Ethiopia, April 26-30, 2020 .
[21] Thomas N. Kipf, Ethan Fetaya, Kuan-Chieh Wang, Max Welling, and Richard S.
Zemel. 2018. Neural Relational Inference for Interacting Systems. InProceedings of
the 35th International Conference on Machine Learning, ICML 2018, Stockholmsmäs-
san, Stockholm, Sweden, July 10-15, 2018 (Proceedings of Machine Learning Research,
Vol. 80). PMLR, 2693–2702.
[22] Sindy Löwe, David Madras, Richard Z. Shilling, and Max Welling. 2022. Amortized
Causal Discovery: Learning to Infer Causal Graphs from Time-Series Data. In 1st
Conference on Causal Learning and Reasoning, CLeaR 2022, Sequoia Conference
Center, Eureka, CA, USA, 11-13 April, 2022 (Proceedings of Machine Learning
Research, Vol. 177). PMLR, 509–525.
[23] Daniel Malinsky and Peter Spirtes. 2018. Causal Structure Learning from Multi-
variate Time Series in Settings with Unmeasured Confounding. In Proceedings of
2018 ACM SIGKDD Workshop on Causal Discovery, CD@KDD 2018, London, UK,
20 August 2018 (Proceedings of Machine Learning Research, Vol. 92) . PMLR, 23–47.
[24] Ricards Marcinkevics and Julia E. Vogt. 2021. Interpretable Models for Granger
Causality Using Self-explaining Neural Networks. In 9th International Conference
on Learning Representations, ICLR 2021, Virtual Event, Austria, May 3-7, 2021 .
[25] Andrés Martínez, Alfonso Salafranca, Ana E Sipols, Clara Simon de Blas, and
Daniel van Hengel. 2022. Distributed lags using elastic-net regularization for
market response models: focus on predictive and explanatory capacity. Journal
of Marketing Analytics (2022), 1–19.
[26] Raha Moraffah, Paras Sheth, Mansooreh Karami, Anchit Bhattacharya, Qianru
Wang, Anique Tahir, Adrienne Raglin, and Huan Liu. 2021. Causal inference for
time series analysis: problems, methods and evaluation. Knowl. Inf. Syst. 63, 12

WSDM ’24, March 4–8, 2024, Mérida, Yucatán, Mexico Chang Gong et al.
(2021), 3041–3085.
[27] Edwin Ng, Zhishi Wang, and Athena Dai. 2021. Bayesian Time Varying Coefficient
Model with Applications to Marketing Mix Modeling. In Proceedings of AdKDD
2021 Workshop.
[28] Alessandro Nuara, Nicola Sosio, Francesco Trovò, Maria Chiara Zaccardi, Nicola
Gatti, and Marcello Restelli. 2019. Dealing with Interdependencies and Uncer-
tainty in Multi-Channel Advertising Campaigns Optimization. InThe World Wide
Web Conference, WWW 2019, San Francisco, CA, USA, May 13-17, 2019. 1376–1386.
[29] Roxana Pamfil, Nisara Sriwattanaworachai, Shaan Desai, Philip Pilgerstorfer,
Konstantinos Georgatzis, Paul Beaumont, and Bryon Aragam. 2020. DYNOTEARS:
Structure Learning from Time-Series Data. In The 23rd International Conference
on Artificial Intelligence and Statistics, AISTATS 2020, 26-28 August 2020, Online
[Palermo, Sicily, Italy] (Proceedings of Machine Learning Research, Vol. 108) . PMLR,
1595–1605.
[30] Judea Pearl. 2009. Causality. Cambridge university press.
[31] Jonas Peters, Dominik Janzing, and Bernhard Schölkopf. 2013. Causal Inference
on Time Series using Restricted Structural Equation Models. InAdvances in Neural
Information Processing Systems 26: 27th Annual Conference on Neural Information
Processing Systems 2013. Proceedings of a meeting held December 5-8, 2013, Lake
Tahoe, Nevada, United States. 154–162.
[32] Ali Shojaie and Emily B. Fox. 2021. Granger Causality: A Review and Recent
Advances. CoRR abs/2105.02675 (2021). arXiv:2105.02675 https://arxiv.org/abs/
2105.02675
[33] Xiangyu Sun, Guiliang Liu, Pascal Poupart, and Oliver Schulte. 2021. NTS-
NOTEARS: Learning Nonparametric Temporal DAGs With Time-Series Data and
Prior Knowledge. CoRR abs/2109.04286 (2021).
[34] Yunting Sun, Yueqing Wang, Yuxue Jin, David Chan, and Jim Koehler. 2017.
Geo-level bayesian hierarchical media mix modeling. (2017).
[35] Ziqi Tan, Shengyu Zhang, Nuanxin Hong, Kun Kuang, Yifan Yu, Jin Yu, Zhou
Zhao, Hongxia Yang, Shiyuan Pan, Jingren Zhou, and Fei Wu. 2022. Uncovering
Causal Effects of Online Short Videos on Consumer Behaviors. InWSDM ’22: The
Fifteenth ACM International Conference on Web Search and Data Mining, Virtual
Event / Tempe, AZ, USA, February 21 - 25, 2022 . ACM, 997–1006.
[36] Alex Tank, Ian Covert, Nicholas J. Foti, Ali Shojaie, and Emily B. Fox. 2022. Neural
Granger Causality. IEEE Trans. Pattern Anal. Mach. Intell. 44, 8 (2022), 4267–4279.
[37] Jon Vaver and Stephanie Shin-Hui Zhang. 2017. Introduction to the Aggregate
Marketing System Simulator. (2017).
[38] Matthew J. Vowels, Necati Cihan Camgöz, and Richard Bowden. 2023. D’ya Like
DAGs? A Survey on Structure Learning and Causal Discovery. ACM Comput.
Surv. 55, 4 (2023), 82:1–82:36.
[39] Yueqing Wang, Yuxue Jin, Yunting Sun, David Chan, and Jim Koehler. 2017. A
hierarchical Bayesian approach to improve media mix models using category
data. (2017).
[40] Sebastian Weichwald, Martin Emil Jakobsen, Phillip B. Mogensen, Lasse Petersen,
Nikolaj Thams, and Gherardo Varando. 2019. Causal structure learning from time
series: Large regression coefficients may predict causal links better in practice
than small p-values. In NeurIPS 2019 Competition and Demonstration Track, 8-14
December 2019, Vancouver, Canada. Revised selected papers (Proceedings of Machine
Learning Research, Vol. 123). PMLR, 27–36.
[41] Richard Wigren and Filip Cornell. 2019. Marketing Mix Modelling: A comparative
study of statistical models.
[42] Tailin Wu, Thomas M. Breuel, Michael Skuhersky, and Jan Kautz. 2020. Discov-
ering Nonlinear Relations with Minimum Predictive Information Regularization.
CoRR abs/2001.01885 (2020). http://arxiv.org/abs/2001.01885
[43] Tianhao Wu, Xingyu Wu, Xin Wang, Shikang Liu, and Huanhuan Chen. 2022.
Nonlinear Causal Discovery in Time Series. In Proceedings of the 31st ACM
International Conference on Information & Knowledge Management, Atlanta, GA,
USA, October 17-21, 2022 . ACM, 4575–4579.
[44] Chenxiao Xu, Hao Huang, and Shinjae Yoo. 2019. Scalable Causal Graph Learning
through a Deep Neural Network. In Proceedings of the 28th ACM International
Conference on Information and Knowledge Management, CIKM 2019, Beijing, China,
November 3-7, 2019. ACM, 1853–1862.
[45] Di Yao, Chang Gong, Lei Zhang, Sheng Chen, and Jingping Bi. 2022. CausalMTA:
Eliminating the User Confounding Bias for Causal Multi-touch Attribution. In
KDD ’22: The 28th ACM SIGKDD Conference on Knowledge Discovery and Data
Mining, Washington, DC, USA, August 14 - 18, 2022 . 4342–4352.
ETHICAL CONSIDERATIONS
We conduct causal structure learning from real-world marketing
mix data, AirMMM. Important ethical considerations related to pri-
vacy and safety. Privacy considerations necessitate informed con-
sent, anonymization, and robust data security measures. Safety con-
siderations involve responsible dissemination of research findings
to avoid unintended negative impacts. We addressed these consid-
erations and potential misuse concerns with mitigation strategies,
including consent, anonymization, transparency, and stakeholder
collaboration, to promote responsible research practices. To be spe-
cific, the label of channels are anonymized with only descriptions
about media type and means of placement. The shop id and sensitive
indicators are processed to avoid information leakage. By uphold-
ing ethical standards, we can ensure the beneficial and responsible
use of online marketing mix data.

CausalMMM: Learning Causal Structure for Marketing Mix Modeling WSDM ’24, March 4–8, 2024, Mérida, Yucatán, Mexico
A APPENDIX
This material serves as the appendix of “ CausalMMM: Learning
Causal Structures for Marketing Mix Modeling", consisting of theo-
retical analysis, details of datasets, and further experimental analy-
sis.
A.1 Theoretical Analysis of CausalMMM
A.1.1 Granger Causality of CausalMMM. We prove the following
claim to support that we can infer Granger causality in the frame-
work of CausalMMM.
Claim 1 (Granger Causality of CausalMMM): For the𝑛-th sample
in dataset, the variable x𝑛,𝑖 does not Granger cause variable x𝑛,𝑗 , if
𝑧𝑛,𝑖𝑗 = 0 according to CausalMMM.
To prove the above claim is to show that the j’s prediction of
𝑓dec is invariant to x1:𝑡 𝑛,𝑖 when CausalMMM infers that x1:𝑡 𝑛,𝑖 does not
cause x1:𝑡 𝑛,𝑖. If the causal relational encoder predicts𝑧𝑛,𝑖𝑗 = 0 for the
nonexistence of edge𝑖→ 𝑗 on the𝑛-th shop, the information of𝑖 is
blocked in MSG𝑡 𝑗 according to Equation 1, thus it does not further
introduce any new term which depends on x𝑛,𝑖. Therefore, we can
derive that the marketing response decoder’s prediction for 𝑗 is
invariant to x1:𝑡 𝑛,𝑖 if𝑧𝑛,𝑖𝑗 = 0, and the variable x𝑛,𝑖 does not Granger
cause variable x𝑛,𝑗 .
A.1.2 Computational Complexity Analysis. We discuss the com-
plexity of CausalMMM in both training and causal relations inference
stages. For a shop’s marketing mix records consisting of𝑇 days, we
first analyze the time complexity of each module in the training.
For the causal relational encoder, the time complexity of pairwise
embedding and relational interaction isO(𝑊), where𝑊 is the num-
ber of weights in neural networks. The decoder model marketing
response at each time step, so the time complexity isO(𝑊𝑇). For
inferring causal relations, CausalMMM takes marketing mix data as
input and calculates structure distributions based on the causal
relational encoder. The time complexity isO(𝑊). Therefore, the
time complexity of the whole model isO(𝑊𝑇).
A.2 Details of Datasets
A.2.1 Generation of Synthetic Data. We first recap that the number
of channel variables is 𝑑, the length of the time series is 𝑇 , and
the number of shops is 𝑁 . We also assume there exist 𝑅 causal
structures in synthetic datasets with𝑁 samples. We aim to obtain
temporal data for the marketing mix. The marketing mix involves
two issues [37]: the interactions between different marketing forces
and marketing responses. Therefore, the data generation process is
composed of three modules:
• Graph sampling. As illustrated in Figure 8, we first generate
𝑅 directed graphs{G 1,...,G𝑅} with probability distribution
𝑃G, which represents the latent causal structure of marketing
variables. For each shop𝑛, the latent causal structureG𝑛 is
sampled from𝑃G.
• Channel generation. Given the latent causal structureG𝑛
of the𝑛-th shop, we can derive the setS of source nodes,
which aren’t children of any nodes. We use a similar ex-
perimental setup as InGRA [ 12] to mock temporal data,
which follows Non-linear Autoregressive Moving Average
0
1 2
3
45
0
1 2
3
45
0
1 2
3
45
0 1 2 3 4 5
012345
0 1 2 3 4 5
012345
0 1 2 3 4 5
012345
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.2
0.4
0.6
0.8
1.0
(a)
(b)
Figure 8: (a) Heterogeneous causal structures of synthetic
data. (b) The corresponding causal matrix. 𝐴(𝑖,𝑗) = 1 means
node𝑖 causes node 𝑗.
(NARMA) [4] generators:
𝑥𝑡 𝑛,𝑖 =𝛼𝑖𝑥𝑡 𝑛,𝑖+𝛽𝑖𝑥𝑡−1 𝑛,𝑖
𝐾∑︁
𝑘=1
𝑥𝑡−𝑘 𝑛,𝑖 +𝛾𝑖𝜖𝑡−𝐾 𝑛 𝜖𝑡−𝐾 𝑛 +𝜖𝑡 𝑛,(𝑖∈S)
𝑥𝑡 𝑛,𝑗 =
𝑑∑︁
𝑖=1
𝜔𝑛,𝑖(𝜂𝑛,𝑗)⊤tanh(x𝑡−𝐾:𝑡−1 𝑛,𝑖 )+ 𝜖𝑡 𝑛,(𝑖 ∉S)
where𝛼𝑖,𝛽𝑖,𝛾𝑖 generated fromN( 0, 0.1) are parameters bounded
to marketing variable𝑚.𝐾 is the order of non-linear interac-
tions, and𝜖𝑡𝑛 are zero-mean noise terms with 0.01 variance.
• Response generation. We generate the target series via
the formula:
𝑢𝑡 𝑛 =
𝑑∑︁
𝑖=1
𝜔𝑛,𝑖(𝜂𝑛,𝑗)⊤tanh(x𝑡−𝐾:𝑡−1 𝑛,𝑖 )+ 𝜖𝑡 𝑛,
The temporal marketing pattern is mocked in the dataset of
Simulation 1, where𝑦𝑡𝑛 =𝑢𝑡𝑛. Whereas both temporal and
saturation marketing patterns are modeled in the dataset
of Simulation 2, i.e.,𝑦𝑡𝑛 = 𝑓𝑐𝑢𝑟𝑣𝑒(𝑢𝑡𝑛,𝑐𝑛), and𝑓𝑐𝑢𝑟𝑣𝑒 is the
S-curve function whose parameters are characterized by𝑐𝑛.
A.2.2 Details of Real-world AirMMM Dataset. Collected from a
representative E-commerce platform, the AirMMM dataset contains
50 shops’ marketing mix data with a period of 22 months from Jan
30th 2021 to Dec 6th 2022. It consists of costs on 11 advertising
channels, PV (page views, which can also be viewed as channels in
the causal graph), and GMV, as described in Table 8.
These channels can be categorized into two groups, i.e., brand
channels and effect channels. Brand channels are designed to cap-
ture users’ interest and promote awareness of the target brand,
including x-brand-0/1/2/3, x-interact, and x-feed. In contrast, X-live,
x-search-0/1/2, and x-effect are effect channels where users are
more likely to take action and convert. These channels in various
forms (interaction, content feed, live, and etc.) are placed on differ-
ent platforms such as video websites, E-commerce platforms, and
news browsers.

WSDM ’24, March 4–8, 2024, Mérida, Yucatán, Mexico Chang Gong et al.
Table 8: Descriptions of advertising channels in the real-world AirMMM dataset.
Channel Type Channel Label Descriptions
brand channel
x-brand-0 Brand advertising on a video website, including advertising types that appear during video pauses
x-brand-1 Brand advertising on a video website, including splash screen advertisements
x-brand-2 Brand advertising on an E-commerce platform
x-brand-3 Brand advertising which is placed on external websites or platforms
x-interact Interactive advertising which encourages active engagement and participation from the users
x-feed Feed advertising which appears within social media feeds or content feeds on target platforms
effect channel
x-live Advertising takes place during live events on an E-commerce platform
x-search-0 Search advertising placed on external websites or platforms
x-search-1 Search advertising on an E-commerce platform
x-search-2 Search advertising on an E-commerce platform
x-effect Effect advertising
others PV Page views GMV Gross merchandise value
0.2 0.4 0.6 0.8 1.0
dataset size
0
10
20
30
40
50
60
70
80training time
CausalMMM (ours)
InGRA
Linear Granger
NGC
GVAR
Figure 10: Comparison of training scalability.
A.3 Further Experimental Analysis
A.3.1 Training Curve. To show the convergence of ourCausalMMM
method, we plot the training loss, validation loss, and AUROC
metric across training epochs in Figure 9. Firstly, it’s evident that
the training and validation losses converge well, demonstrating that
CausalMMM is reasonably stable. Secondly, it shows that AUROC
rises simultaneously when loss converges, which illustrates that
the quality of the causal structure learning improves as the error of
marketing response modeling converges.
0 20 40 60 80 100
epochs
0
200
400
600
800loss function value
train
val
0 20 40 60 80 100
epochs
0.65
0.70
0.75
0.80
0.85
0.90AUROC
Figure 9: Training, validation loss, and AUROC across epochs.
A.3.2 Comparison of Training Scalability. We investigate the train-
ing scalability of CausalMMM, InGRA, Linear Granger, NGC, and
GVAR. We vary the size of the training dataset from20% to 100%
to simulate the increase of online shops to be served. The results of
Linear Granger, NGC, and GVAR are evaluated by summing training
time on each shop. We train all models on a high-end server with
2× NVIDIA GTX 3090 GPUs. The results are shown in Figure 10.
From the figure, we can observe that all methods scale linearly
with the increase of the training data size. Therefore, they’re promis-
ing to handle massive marketing data from a large number of online
shops. Analogous to CausalMMM, InGRA can utilize information
across different shops. However, its time consumption is much
higher than the proposed CausalMMM because of the computational
complexity of InGRA’s attention mechanism.
