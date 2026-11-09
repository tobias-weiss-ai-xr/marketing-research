---
title: 'From Bias to Behavior: Learning Bull-Bear Market Dynamics with Contrastive Modeling'
url: https://arxiv.org/abs/2507.14182
category: ai-marketing
subcategory: empirical
date: 2025-07
venue: ''
authors:
- Xiaotong Luo
- Shengda Zhuo
- Min Chen
- Lichun Li
- Ruizhao Lu
source: arxiv
pdf_url: https://arxiv.org/pdf/2507.14182
pages: 18
chars: 82598
fetched_at: '2026-11-08T13:39:00+00:00'
kb_version: 1
---

# From Bias to Behavior: Learning Bull-Bear Market Dynamics with Contrastive Modeling

From Bias to Behavior: Learning Bull-Bear Market Dynamics with
Contrastive Modeling
Xiaotong Luoa, Shengda Zhuob, Min Chenc, Lichun Lia, Ruizhao Lua, Wenqi Fand,
Shuqiang Huangb and Yin Tanga,∗
aExperimental Center for Economics and Management, Jinan University, Jinan University, Guangzhou 511443, Guangdong, China
bCollege of Cyber Security, Jinan University, Guangzhou 511443, Guangdong, China
cSchool of Computer Science and Engineering, South China University of Technology, Guangzhou 510006, Guangdong, China
dDepartment of Computing, Hong Kong Polytechnic University, HongKong 999077, HongKong, China
ARTICLE INFO
Keywords:
Market Representation
Quantitative Trading
Contrastive Learning
Bull-Bear Dynamics
ABSTRACT
Financial markets exhibit highly dynamic and complex behaviors shaped by both historical price
trajectoriesandexogenousnarratives,suchasnews,policyinterpretations,andsocialmediasentiment.
The heterogeneity in these data and the diverse insight of investors introduce biases that complicate
the modeling of market dynamics. Unlike prior work, this paper explores the potential of bull and
bear regimes in investor-driven market dynamics. Through empirical analysis on real-world financial
datasets, we uncover a dynamic relationship between bias variation and behavioral adaptation, which
enhances trend prediction under evolving market conditions. To model this mechanism, we propose
the Bias to Behavior from Bull-Bear Dynamics model(B4), a unified framework that jointly embeds
temporal price sequences and external contextual signals into a shared latent space where opposing
bull and bear forces naturally emerge, forming the foundation for bias representation. Within this
space, an inertial pairing module pairs temporally adjacent samples to preserve momentum, while
the dual competition mechanism contrasts bullish and bearish embeddings to capture behavioral
divergence.Together,thesecomponentsallowB4tomodelbias-drivenasymmetry,behavioralinertia,
and market heterogeneity. Experimental results on real-world financial datasets demonstrate that
our model not only achieves superior performance in predicting market trends but also provides
interpretable insights into the interplay of biases, investor behaviors, and market dynamics.
1. Introduction
Financial markets are dynamic and adaptive systems,
shaped by a complex interplay between historical price
trajectories and exogenous factors such as news, policy
interpretations, and social media sentiment. These factors
giverisetocognitivebiasesthatsubsequentlyexertasignifi-
cantinfluenceoninvestorbehavior,exacerbatingthemarket
heterogeneity [1, 6]. Understanding and modeling these
dynamicspresentsacorechallengeinfinance,necessitating
aframeworkthatbridgesquantitativeandbehavioralfinance
touncovertheintricaterelationshipsbetweenmarkettrends,
external influences, and investor decision-making [24].
Exploringthemechanismsbehindfinancialmarketfluc-
tuationshaslongbeenacentralobjectiveinbotheconomics
andquantitativefinance.Earlyresearchprimarilyfocusedon
modelingpricesasstochasticprocesses,employingmethods
such as random walks [17], GARCH models [4], and the
Black-Scholes framework [2] to describe price randomness
and volatility characteristics. While these models have been
effective in capturing general patterns of price fluctuations,
they fall short in capturing “how” external narratives are
cognitively processed and lead to “price momentum or re-
versal”, lacking an explicit mechanism linking information
flow to bias formation. This gap has motivated a wave of
∗Corresponding Authors: Yin Tang
xiaotong01@stu2020.jnu.edu.cn (X. Luo);zhuosd96@gmail.com (S.
Zhuo); minchen2012@hust.edu.cn (M. Chen);lichun@stu2024.jnu.edu.cn(L.
Li); a13302600808@stu2022.jnu.edu.cn (R. Lu);wangjieqiu@buaa.edu.cn(W.
Fan); hsq@jnu.edu.cn (S. Huang);ytang@jnu.edu.cn (Y. Tang)
1.0
0.5
0.0
0.5
1.0
1.0
0.5
0.0
0.5
1.0
1.0
0.5
0.0
0.5
1.0
bearish dominance
bullish dominance
bull market
bear market
(a) Before B4
1.0
0.5
0.0
0.5
1.0
1.0
0.5
0.0
0.5
1.0
1.0
0.5
0.0
0.5
1.0
bearish dominance
bullish dominance
bull market
bear market (b) After B4
Figure 1: Light green triangles represent “bullish dominance”
scenarios, and light red triangles represent “bearish dominance”
scenarios, indicating the competitive interactions between
bears and bulls. Red circles denote “bear markets”, while green
circles denote “bull markets”, reflecting the outcomes of this
competition corresponding to downward and upward trends,
respectively. In postprocessing of B4, data points are more
clearly differentiated based on market competition dynamics
and outcomes.
multimodal and sentiment-aware preditors, such as news
[34] and social media [9], gained increasing attention [27].
While such models boost short-horizon forecasts, they still
treat sentiment as an auxiliary signal and overlook the be-
havioralasymmetrybetweenheterogeneousinvestorgroups.
As a result, they fail to explain why the same information
maytriggeropposingmarketactions.Inessence,fewmodels
: Preprint submitted to Elsevier Page 1 of 17
arXiv:2507.14182v1  [cs.LG]  12 Jul 2025

explicitly model market participants as two sides——bulls
and bears——with competing cognitive interpretations and
decisioninertia.Withoutthatlink,predictionsremainfragile
when dominant sentiment regimes and bias reverses. We
summarise two key challenges (CHs):
CH-1: Modality Entanglement and Behavioral Align-
ment. Market dynamics emerge from the interaction of
sequential numerical data (e.g., price, volume) and high-
dimensional,event-driventextualinformation.Thesemodal-
ities differ not only in format and frequency, but also in
interpretability. Naive fusion approaches [8, 43] obscure
temporalcausalityandfailtomodelhowexternalnarratives
are mapped into investor expectations and behaviors, espe-
ciallyunderconflictingsentimentconditions.Thus,aligning
cross-modal signals with investor behavior is critical.
CH-2: Modeling the Bias–Behavior–Price Pathway.In-
vestor reactions are not homogeneous. Bullish and bearish
groups often form divergent interpretations of the same
event, leading to dynamics shaped by competitive behavior.
Yet, most existing works [31, 10] either average out this
heterogeneity or treat sentiment as a static attribute. To
model price movement as the outcome of evolving bias and
behavioral inertia, we must capture how attention migrates,
how momentum sustains belief, and how conflicting views
interact. This calls for a framework that tracks how bias
initiates, behavior amplifies, and price reacts.
Our work:By quantitatively modeling the impact of cog-
nitive biases and irrational behavior on market price fluc-
tuations, we propose theBias to Behavior from Bull-Bear
Dynamics model(named B4), which integrates time-series
datawithsemanticinsightsfromexternalfactorsandapplies
momentum-aware strategies, capable of capturing the com-
petitive dynamics between market biases, sentiment, and
market forces.
This paper delivers specific contributions, summarized
as follows:
• Weintroduceabehaviorallygroundedmodelingparadigm
that distinguishes bull and bear forces, empirically vali-
dating how market biases evolve and impact price trends
across time and industries.
• Our model integrates time-series price data and external
textualinformationbyintroducingthe Bias-AwareRepre-
sentation from Prices to Conceptand capture the interac-
tions between Bullish and Bearish forces byMomentum-
Aware Competitive Modeling. The model generates more
accurate and actionable trading insights based on real-
world market dynamics.
• Experimental results based on real-world financial data
(comprising 110 trades across 10 industries) demonstrate
that B4 excels in market trend prediction while revealing
thecomplexinteractionsbetweeninvestorbiasesandmar-
ket behaviors.
• Our work proposed a detailed case to demonstrate how
evolving investor bias and attention—quantified through
novel metrics—drive sentiment shifts, emotional polar-
ization, and structural movements in financial markets.
The organization of our paper is as follows: we first
present related work in Section 2. Section 3 details how
to effectively fuse voice interactions and knowledge graph
information to mine user preferences. Experimental results
areprovidedinSection4.Forbetterunderstanding,detailed
case analyses illustrating bias evolution and its market im-
pact are provided in Section 5. Finally, conclusions and
future work are presented in Section 6.
2. Related Work
2.1. Multimodal Fusion Methods
Financial forecasting has shifted from using only his-
torical price data to integrating multimodal information
such as news, social media, and reports. Early methods
employed simple feature concatenation—e.g., combining
prices with bag-of-words or sentiment scores [40]—which
improved accuracy but overlooked temporal and seman-
tic misalignments. Later, models like FinReport [28] and
MSMF [36] addressed alignment more explicitly, either by
structuringtextualeventsordynamicallyadjustingmodality
weights. Recent efforts—such as CMTF [35], MSGCA
[44], and modality-aware transformers [13]—further in-
troduced cross-modal attention and semantic fusion, often
leveraging pretrained models like FinBERT [22] to align
textualsentimentwithnumericalfeatures[33].Despitethese
advances, most attention mechanisms remain scalar and
uninterpretable, failing to reflect opposing market views
such as bullish versus bearish interpretations.
Graph-based and LLM-enhanced approaches extend fu-
sion by modeling broader relational structures and narra-
tive flows. Temporal GNNs and hierarchical graph models
[15, 23, 39] capture inter-stock dependencies but typically
collapse sentiment diversity into aggregated node states.
Similarly, LLM-based frameworks like TIME-LLM [25]
improve alignment and generalization but encode market
discourse as a single narrative stream, overlooking polarity
and investor competition. Overall, while existing methods
excel at collecting and aligning multimodal inputs, they
rarely model the dynamics of opposing investor behav-
ior—missing a critical link between sentiment divergence
and price formation that our work aims to address.
2.2. Market-Modeling Paradigms
Price reflects the aggregated outcome of investor be-
havior, and its modeling traditionally relies on stochastic
frameworks such as the random walk [17], GARCH models
[5], and Black-Scholes option pricing [2]. Though effective
in capturing volatility and short-term fluctuations, these
models assume market efficiency and often neglect exter-
nal information and investor heterogeneity, limiting their
explanatory capacity during structural or sentiment-driven
changes.
Extensions incorporating macro shocks (e.g., SVAR
[29]),sentiment-awareGARCHvariants[14],anddenoising
: Preprint submitted to Elsevier Page 2 of 17

...
Ht ′
Xt
.........
Eprice
Cross Att.
Bullish &
Bearish
News
Content
Etext
...
E
.........
Lang. M .Finetune
......
Dual Competition
bullish forces
bearish forces
time t
LossCE
LossU
LossM
hU BUhE BE
Att.
Rep.
Mom. Span
hM
hM
hM
...
H′
.........
Eprice
P2C
Sentiment
Marker
News
Content
Etext
...
Sentiment-Aware
Language Model
......

hBU ABUhBE ABE
Positive Pi
Negative Ni
yj=yi & |j-i|≤
yj≠yi & |j-i|＞

DCM
BS
IP
hMar hBEhBU
hMar hBEhBU
hMar hBEhBU
hMar hBEhBU
hMar
hBE
hBU
hMar
hBE
hBU
hMar
hBE
hBU
Pi
Ni
hMar hBEhBU
 X  Ni
BS
Repel
Abstract
Comp
Mar
CE Total
Figure 2:The overall architecture of B4 model for dynamic market modeling. The framework is designed to address key questions
regarding the integration of temporal data and the mitigation of bias to extract insights from news events, as well as capturing
price momentum and reflecting bull-bear competition to produce actionable trading insights.
techniques [19] improve robustness, but still treat behavior
implicitly or linearly. Deep learning models—including
LSTMs, Transformer hybrids [42], and Market-GAN [38]
better capture nonlinear dynamics, yet often model price
as a closed system, leaving decision logic unaddressed.
Recent studies attempt to uncover behavioral signals: MF-
CLR [12] uses contrastive learning for directional trends,
AutoTimes [31] encodes candlestick patterns as symbolic
sequences,andCMLF[21]modelsmomentumviamemory-
aligned representations. However, few works explicitly sep-
arate bullish and bearish interpretations or explain how
competing viewpoints drive market movement. This leaves
open the need for a model that extracts interpretable bias
fromexternalsignalsandlinksittobehavioraldynamicsthat
shape price trajectories—a direction our B4 model pursues.
3. Methodology
To address the core modeling challenge of transforming
bias-aware representations into behavior-oriented predic-
tions, this section aims to bridge the gap between investors’
interpretations of market information and the resulting pat-
terns of observable trading behavior. To this end, we focus
on two key questions:Q1: How can temporal price signals
be integrated with noisy external information sources to
construct bias-aware representations?Q2: How can market
momentumandinvestorcompetitionbeeffectivelycaptured
to simulate behavioral dynamics and generate actionable
insights?
To address these questions, our framework (Figure 2)
comprises two coordinated modules: Bias-Aware Represen-
tation, which transforms price data into conceptual embed-
dings,andMomentum-AwareCompetitiveModeling,which
captures behavioral dynamics through competitive interac-
tions.
3.1. Bias-Aware Representation from Prices to
Concept
To effectively capture the interaction between price dy-
namics and external information sources (e.g., news, pol-
icy signals, and social media sentiment), we introduce two
complementary modules:Price-to-Concept (P2C) andBias
Simulation(BS).P2Calignsstructuredpricetimeserieswith
semantic space representations, enabling cross-modal inte-
gration, while BS captures investors’ divergent interpreta-
tions,bullishandbearish,ofthesameinformation.Together,
theyproduceabias-awaremarketrepresentationthatreflects
both temporal volatility and subjective sentiment, forming
the foundation for behavior-oriented financial modeling.
Price-to-Concept (P2C).Financial time series and textual
newsdatabelongtoinherentlydifferentmodalities.Toalign
them, the P2C module first transforms historical price se-
quences into a latent representation compatible with the
languagemodel’ssemanticspace.Theinitialinputisamul-
tivariate price sequence𝐗𝑃 𝑡 within a specified time window
[𝑡−𝛿,𝑡], where𝛿 denotes the length of the historical look-
back window. It includes the open price𝑥Open 𝑡 , close price
𝑥Close 𝑡 , lowest price𝑥Low 𝑡 , and highest price𝑥High 𝑡 , which
reflecthistoricaltrendsandreal-timemarketfluctuations.To
encodepriceseriesintoaconceptualizedrepresentation,we
firstextracttheinitial-layeroutput 𝐇𝐭 fromanEncoder-Only
Language Model (EOLM), such as BERT or RoBERTa.
Since time-series and text belong to different modalities
with varying semantic expression methods, and Language
Models cannot directly process time-series input features,
it is necessary to align price sequence with the natural
language text domain.
Giventhevastspaceofthenaturallanguagetextdomain,
weapplyaLineartransformationtoobtainthetextprototype
matrix 𝐇′, which represents market-related semantic fea-
tures: 𝐇′= Linear(𝐇).Next,thepricewindow 𝐗𝑃 𝑡 interacts
with 𝐇′ through P2C to generate the semantic-related price
: Preprint submitted to Elsevier Page 3 of 17

embedding:
𝐄price= Softmax
(
𝐗𝑃 𝑡 ⋅ 𝐇′⊤
√
𝑑𝑘
)
⋅ 𝐇
′
, (1)
where𝑑𝑘 represents the dimension of linearly transformed
vectors for scaled dot-product attention. This process aligns
pricefluctuationswithtextualprototypes,narrowingthegap
betweennumericalmarketdataandsemanticunderstanding.
BiasSimulation(BS). WhileP2Cenablessemanticground-
ing of price sequences, the BS module captures asymmetric
interpretations arising from distinct bullish and bearish per-
spectives of investors.
(1) Sentiment Marker Injection:To simulate investor
perspectives, we incorporate symbolic sentiment cues into
news texts. Let𝐗𝑁 𝑡 denote the external news on day𝑡. We
prepend two sentiment markers, ‘UP’ and ‘DOWN’, to the
originalnewsinputtosignalbullishandbearishviewpoints.
Text enriched with sentiment markers is processed sepa-
rately from price data. The augmented text data for day𝑡,
𝐗Aug 𝑡 , is generated by concatenating the sentiment markers
with the original text:
𝐗Aug 𝑡 =Concat( [UP],[DOWN], 𝐗𝑁 𝑡 ). (2)
The augmented text undergoes tokenization and embed-
ding, which converts the text into a sequential representa-
tion:
𝐄text=f( 𝐗Aug 𝑡 ), (3)
where f( ⋅) denotes the embedding and encoding function.
The embedding layer of a pretrained EOLM, which in this
case is the BERT embedding layer, maps the tokenized
sequence into a high-dimensional embedding space𝐄text.
Unlike price data, textual sequences do not participate in
direct cross-attention but act as complementary sentiment
representations.
(2) Bias Modeling and Representation:Investor bi-
ases, the directional divergence arising when bullish and
bearish camps interpret the same signal differently, are em-
bedded by fusing numerical prices with sentiment-injected
text.
We first concatenate the price-aligned embedding𝐄price
andnewsembedding 𝐄text toobtainajointfeaturematrix 𝐄.
𝐄= Concat(𝐄text, 𝐄price). (4)
To reflect the investors’ varied understandings of the
information, this unified representation𝐄 is passed through
a Sentiment-Aware Language Model (), a pretrained
EOLM,whichhasbeenshowneffectiveforsentimentanaly-
sisduetoitsself-attentionmechanismandabilitytocapture
both local and global context. The encoder is particularly
suitable in this setting because it dynamically weighs the
importance of each token, enabling the model to inter-
pretsentiment-bearingcues( e.g.,emotionalverbs,company
names)withinthebroadermarketnarrative.Weexpressthis
sentiment encoding process as:
𝐡= (𝐄). (5)
The output of this encoder is a contextualized sequence
ofembeddings 𝐡∈ ℝ|𝐄|×𝑑,fromwhichweextractthreekey
components:
𝐡Mar= 𝐡[idx([CLS])], 𝐡Comp= 𝐡[idx([UP, DOWN])]. (6)
Investor sentiment is modeled by extracting two embed-
dingsfromthefinallayeroutput. 𝐡Mar representsthemarket
representation, indexed at the [CLS] token, while 𝐡Comp
represents the competition representation which includes
both bullish and bearish sentiments features, indexed at the
[UP] and [DOWN] tokens. The sentiment markers [UP]
and [DOWN] correspond to bullish and bearish sentiments,
respectively,whichrepresentopposingpositionsinthecom-
petition between market participants, driving the dynamics
of price movements.
The indexing function idx extracts the specific posi-
tion of market and sentiment representations from𝐡. These
sentiment-specific vectors,𝐡BU and 𝐡BE, are extracted from
[UP] and [DOWN] fields of𝐡Comp. These vectors are then
combinedwiththeoverallrepresentation 𝐡,generatingbias-
aware representations:
𝐀BU= 𝐡BU ⋅ 𝐡⊤ √
𝑑
, 𝐀BE= 𝐡BE ⋅ 𝐡⊤ √
𝑑
. (7)
where, the resulting biases can be formulated as the differ-
ence between these two attention maps:𝐀BU− 𝐀BE.
This bias matrix reflects how investor sentiment skews
attention toward different features of the input, offering
an interpretable and differentiable mechanism to simulate
investor heterogeneity. It enables the model to account for
the asymmetric impact of news and market signals on price
actions,ultimatelyimprovingtheunderstandingandpredic-
tion of dynamic market behavior.
3.2. Momentum-Aware Competitive Modeling
Market momentum shows up as persistent runs in price
direction, while bullish and bearish investors compete to
extend or reverse those runs.
To model both phenomena in a single pipeline, we
propose an integrated strategy combiningInertial Pairing
(IP) and Dual Competition Mechanism(DCM), capturing
the competitive dynamics between bullish and bearish mar-
ket trends while preserving the temporal consistency of
sequentialdata.Thisstrategyleveragestemporalmomentum
to construct meaningful samples and employs contrastive
losses to align trend-specific features with overall market
characteristics.
Inertial Pairing (IP).To capture market momentum, we
introducetheconceptof InertialPairing togeneratepositive
and negative samples. Positive samples maintain the same
market trend over time, while negative samples either devi-
ate from the trend or fall outside a given temporal window.
: Preprint submitted to Elsevier Page 4 of 17

This approach ensures that the model learns to account for
the momentum inertia in financial markets, reflecting the
persistence of price movements in the same direction.
(1) Market Trend Labeling: At each time𝑡, we derive
the true market trend label𝑦𝑡 based on the direction of
pricemovement,distinguishingbetweenbullishandbearish
trends. Specifically, we define:
𝑦𝑡=
{
1, if𝑥Close 𝑡+1 >𝑥 Close 𝑡 ,
0, if𝑥Close 𝑡+1 <𝑥 Close 𝑡 , (8)
where,𝑦𝑡 = 1indicates a bullish trend, while𝑦𝑡 = 0repre-
sentsabearishtrend.Thislabelingisusedtocreatepositive
and negative samples aligned with the market momentum.
(2) Sample Momentum: Momentum refers to the per-
sistence of price movements in the same direction. In our
model,weleveragemarkettrendinertiatoconstructsamples
that capture this momentum, ensuring that the model can
learn the temporal dependencies inherent in financial data.
Positivesamples 𝑖alignwiththecurrentsample’strend
andfallwithinapredefinedtemporalrange Δ,whilenegative
samples 𝑖 either deviate from the trend or lie outside the
temporal boundary:
𝑖={𝑥𝑗|𝑦𝑗 =𝑦𝑖 and|𝑗−𝑖| ≤Δ}, (9)
𝑖={𝑥𝑗|𝑦𝑗 ≠𝑦𝑖 or|𝑗−𝑖|>Δ}, (10)
where the temporal rangeΔ encapsulates the market’s mo-
mentuminertia,ensuringthatpositiveandnegativesamples
reflect sequential consistency.
DualCompetitionMechanism(DCM). Tomodeldynamic
competition and its impact on market trends, we design a
mechanism to establish dual object links, the competing
participants (bullish vs. bearish) and their resulting out-
comes (market direction). The motivation stems from the
inherentinterplaybetweenbullishandbearishforces,which
collectively drive the market toward bull or bear markets.
Consequently, stronger bullish pressure is typically asso-
ciated with upward price movements, whereas intensified
bearish sentiment often precedes market downturns.
Given 𝑁 samples constructed byInertial Pairing, the
DualCompetitionMechanism employscontrastivelossesfor
feature alignment to align bullish and bearish features with
overall market dynamics.𝐡Comp,𝑖 captures the competition
betweenbullishandbearishforces,while 𝐡Comp,𝑝reflectsthe
dominance of bullish forces over bearish ones.𝐡Mar, on the
other hand, represents the market characteristics of bull or
bear markets. The loss functions are defined as follows:
Comp= 1 𝑁 ∑ 𝑖∈ 1 |𝑖| ∑ 𝑝∈𝑖 −log exp(𝐶𝑀(𝑝,𝑖)∕𝜏)∑ 𝑎∈𝑖 exp(𝐶𝑀(𝑎,𝑖)∕𝜏),
(11)
Mar= 1 𝑁 ∑ 𝑖∈ 1 |𝑖| ∑ 𝑝∈𝑖 −log exp(𝐶𝑀(𝑖,𝑝)∕𝜏)∑ 𝑎∈𝑖 exp(𝐶𝑀(𝑖,𝑎)∕𝜏),
(12)
where 𝐶𝑀(𝑝,𝑖) =𝐡⋆ Comp,𝑝 ⋅ 𝐡Mar,𝑖, 𝐶𝑀(𝑎,𝑖) =𝐡⋆ Comp,𝑎 ⋅
𝐡Mar,𝑖, 𝐶𝑀(𝑖,𝑝) =𝐡⋆ Comp,𝑖 ⋅ 𝐡Mar,𝑝, 𝐶𝑀(𝑖,𝑎) =𝐡⋆ Comp,𝑖 ⋅
𝐡Mar,𝑎,𝜏 isthetemperaturefactor, thesetofindexesofthe
training samples, and𝑖 refers to the union of sets𝑖 and
𝑁𝑖. 𝐡⋆ Comp,𝑖 denotesthecolumnsof 𝐡Comp,𝑖 correspondingto
the ground-truth label of𝐡Mar,𝑖.
To quantify the momentum-aware dominance of bullish
or bearish forces, a cross-entropy loss is introduced:
CE=− 1 𝑁 ∑ 𝑖∈ log exp(𝐶𝑀(𝑖,𝑖)) exp(𝑈𝑀(𝑖,𝑖))+exp( 𝐸𝑀(𝑖,𝑖)),
(13)
where 𝐶𝑀(𝑖,𝑖)= 𝐡⋆ Comp,𝑖⋅𝐡Mar,𝑖, 𝑈𝑀(𝑖,𝑖)= 𝐡BU,𝑖⋅𝐡Mar,𝑖,
𝐸𝑀(𝑖,𝑖)= 𝐡BE,𝑖 ⋅ 𝐡Mar,𝑖.
Thefinallossfunctioncombinesthecontrastiveandmo-
mentum losses, balancing the objectives of trend alignment
and feature competition:
Total=𝛼 ⋅(Comp+ Mar)+(1− 𝛼) ⋅ CE, (14)
where𝛼 is the weighting parameter.
Model Optimization.The model parameters are optimized
using backpropagation and gradient descent:
𝜃new=𝜃old−𝜂∇𝜃Total, (15)
where 𝜂 is the learning rate. During training, the model
minimizes Total, ensuring not only accurate market trend
predictionsbutalsoeffectivedifferentiationbetweenbullish
and bearish dynamics.
By combining Inertial Pairing and Dual Competition
Mechanism,theframeworkestablishestemporalconsistency
in sample construction and enhances the competitive re-
lationship modeling between bullish and bearish forces.
This integration allows the model to better capture market
momentum and investor sentiment, reflecting the nuanced
dynamics of financial markets.
4. Experimental Evaluation
In this section, we evaluate the performance of the B4.
Extensive experiments carried out on 10 industries are de-
signed to explore and answer the following research ques-
tions (RQs):
• RQ1: How does B4 perform compare to other models
using text and time series for stock price prediction?
• RQ2: Do the price translator and contrastive modules
improveB4performance,andhowdodifferentcontrastive
losses affect it?
• RQ3:HowdohyperparametercombinationsimpactB4’s
performance, and which is optimal?
4.1. Experiment Settings
Datasets. CMIN dataset1 comprises the top 110 stocks by
market capitalization from the U.S. stock market datasets
1https://github.com/BigRoddy/CMIN-Dataset/
: Preprint submitted to Elsevier Page 5 of 17

Table 1
Performance comparison of different models across different stock datasets, with each stock representing a distinct industry.
The table presents the Cumulative Returns, Annual Returns, Max Drawdown, and Calmar Ratio for each model, including B4,
LSTM, StockNet, Transformer, ESPMP, DUALformer, and SCLformer. We stylize the best result asBold and the second best
as underline.
Industry Stock Metric B4 LSTM Transformer StockNet DUALformer CEformer SCLformer ESPMP
Technology AAPL Cumulative Returns ↑ 0.301 0.005 0.177 0.152 0.043 0.118 0.112 0.248
Annual Return ↑ 0.270 0.004 0.160 0.137 0.039 0.107 0.101 0.223
Max Drawdown ↓ 0.063 0.059 0.075 0.174 0.148 0.081 0.043 0.052
Calmar Ratio ↑ 4.290 0.072 2.133 0.788 0.266 1.319 2.342 4.338
Financial SCHW Cumulative Returns ↑ 0.697 -0.007 1.108 0.270 0.018 0.232 -0.006 0.158
Annual Return ↑ 0.763 -0.007 1.224 0.293 0.020 0.251 -0.006 0.171
Max Drawdown ↓ 0.123 0.041 0.240 0.176 0.104 0.067 0.185 0.158
Calmar Ratio ↑ 6.223 -0.180 5.110 1.659 0.190 3.744 -0.035 1.077
Energy CVX Cumulative Returns ↑ 0.926 0.528 0.758 0.089 0.729 0.613 0.717 0.347
Annual Return ↑ 0.812 0.471 0.670 0.081 0.646 0.545 0.635 0.312
Max Drawdown ↓ 0.143 0.167 0.189 0.197 0.157 0.159 0.218 0.104
Calmar Ratio ↑ 5.685 2.818 3.547 0.411 4.118 3.435 2.914 2.999
Real Estate EQIX Cumulative Returns ↑ 0.427 -0.201 0.046 0.071 0.065 0.130 0.168 0.178
Annual Return ↑ 0.914 -0.337 0.086 0.133 0.122 0.249 0.329 0.349
Max Drawdown ↓ 0.118 0.234 0.214 0.180 0.086 0.063 0.050 0.096
Calmar Ratio ↑ 7.778 -1.437 0.401 0.738 1.429 3.933 6.567 3.634
Communication NFLX Cumulative Returns ↑ 0.323 0.194 0.114 0.319 0.129 0.046 -0.003 0.213
Annual Return ↑ 0.378 0.291 0.132 0.490 0.150 0.052 -0.004 0.248
Max Drawdown ↓ 0.073 0.132 0.192 0.375 0.119 0.100 0.093 0.077
Calmar Ratio ↑ 5.169 2.195 0.689 1.306 1.261 0.525 -0.042 3.204
Consumer BABA Cumulative Returns ↑ 0.119 -0.089 -0.066 -0.162 -0.167 -0.281 -0.304 -0.043
Annual Return ↑ 0.126 -0.098 -0.069 -0.170 -0.175 -0.293 -0.317 -0.046
Max Drawdown ↓ 0.137 0.254 0.285 0.351 0.340 0.457 0.437 0.137
Calmar Ratio ↑ 0.915 -0.386 -0.243 -0.485 -0.514 -0.642 -0.726 -0.333
Healthcare PFE Cumulative Returns ↑ 0.457 -0.106 0.098 -0.029 -0.015 0.039 0.030 0.262
Annual Return ↑ 0.502 -0.114 0.106 -0.031 -0.016 0.042 0.032 0.286
Max Drawdown ↓ 0.095 0.135 0.232 0.029 0.115 0.126 0.066 0.152
Calmar Ratio ↑ 5.273 -0.842 0.459 -1.080 -0.137 0.333 0.488 1.884
Industrials DE Cumulative Returns ↑ 0.513 0.093 0.283 -0.004 0.129 0.169 0.308 0.252
Annual Return ↑ 0.680 0.119 0.369 -0.005 0.165 0.218 0.402 0.327
Max Drawdown ↓ 0.122 0.128 0.253 0.283 0.167 0.101 0.199 0.167
Calmar Ratio ↑ 5.573 0.928 1.462 -0.019 0.987 2.154 2.020 1.957
Materials BHP Cumulative Returns ↑ 0.256 0.039 0.022 -0.094 0.140 -0.048 0.088 0.083
Annual Return ↑ 0.342 0.052 0.029 -0.120 0.186 -0.062 0.115 0.110
Max Drawdown ↓ 0.057 0.073 0.507 0.399 0.077 0.217 0.165 0.129
Calmar Ratio ↑ 6.017 0.702 0.058 -0.300 2.422 -0.284 0.699 0.852
Utilities DUK Cumulative Returns ↑ 0.370 0.279 0.118 0.080 0.048 -0.034 0.028 0.046
Annual Return ↑ 0.388 0.294 0.124 0.084 0.050 -0.036 0.030 0.048
Max Drawdown ↓ 0.023 0.080 0.035 0.077 0.055 0.096 0.066 0.056
Calmar Ratio ↑ 16.932 3.668 3.531 1.081 0.917 -0.373 0.453 0.861
[32], categorized into 10 industries from 2018-01-01 to
2021-12-31. The industries covered include: 1) Communi-
cation,2)Consumer,3)Energy,4)Financial,5)Healthcare,
6) Industrials, 7) Materials, 8) Real Estate, 9) Technology,
and 10) Utilities. The correspondence between industries
and stocks, are detailed in Table 6. The training set consists
of the first 70% of the time span for all stocks, while the
testing set comprises the remaining 30% of the time span.
EvaluationMetrics.Weevaluatetheriskandreturncharac-
teristicsofthetradingstrategyfrommultipleperspectivesby
employing a set of performance metrics, includingAnnual
Return, Cumulative Returns, Max Drawdown, andCalmar
Ratio.
In this study, we employ a set of performance metrics
to assess the performance of our trading strategy. Each
metric offers a unique perspective on the risk and return
characteristics of the strategy. Below, we define each metric
and provide a clear explanation of the variables involved in
their respective formulas.
: Preprint submitted to Elsevier Page 6 of 17

B4 Stocknet LSTM Transformer DUAL-DNN CE-DNN SCL-DNN ESPMP
  




$$3/
7LPH6WHSV
3RUIROLR9DOXHV
  




%$&
7LPH6WHSV
3RUIROLR9DOXHV
  




&9;
7LPH6WHSV
3RUIROLR9DOXHV
   




'+5
7LPH6WHSV
3RUIROLR9DOXHV
   






(/
7LPH6WHSV
3RUIROLR9DOXHV
  




(4,;
7LPH6WHSV
3RUIROLR9DOXHV
  




*(
7LPH6WHSV
3RUIROLR9DOXHV
    



*22*
7LPH6WHSV
3RUIROLR9DOXHV
Figure 3:Performance Comparison of magnitude𝜂 of CL.
1. Annual Return: The annual return is calculated by tak-
ing the geometric average of the return over the period
and subtracting one. It represents the average annual
profit or loss from an investment:
Annual Return=
(𝑅
𝑛
)1
𝑡
−1,
where𝑅isthetotalreturnovertheperiod, 𝑛isthenumber
ofsub-periods( e.g.,years),and 𝑡isthenumberofyears.
2. Cumulative Returns: Cumulative returns measure the
total change in the value of an investment over a specific
period. It is the ratio of the final value to the initial value
minus one:
Cumulative Returns= 𝑉𝑡
𝑉0
−1,
where𝑉𝑡 isthefinalvalueoftheinvestment,and 𝑉0 isthe
initial value.
3. MaxDrawdown:Themaximumdrawdownisthelargest
peak-to-trough decline in the value of a portfolio during
a specific period before a new peak is achieved:
Max Drawdown=max
(𝑃peak
𝑃valley
−1
)
,
where𝑃peak is the highest peak value, and𝑃valley is the
lowest trough value following that peak.
4. Calmar Ratio: The Calmar ratio is a measure of risk-
adjusted return that uses the maximum drawdown to
represent downside risk:
Calmar Ratio= Annual Return Max Drawdown.
Thesemetricsareessentialforprovidingabalancedview
of the trading strategy’s performance, considering both its
profitability and its risk characteristics.
C. Benchmarks. We compare B4 with seven representative
baseline models, which fall into two major categories: 1)
Modal Fusion methods(MF), which combine textual and
pricemodalitiesforprediction,and2)ContrastiveLearning-
based Language models(CL), which leverage contrastive
objectivestomodelthecompetitivenatureofmarketdynam-
ics.
• StockNet (MF) [40]: A bidirectional Gated Recurrent
Unit (GRU) to extract tweet information and aggregates
price and text using an attention mechanism for predic-
tion.
• LSTM(MF)[20,45]:Atimeseriespredictionmodelthat
directly concatenates text and price data.
• Transformer(MF) [37, 16]: A prediction method utiliz-
ingattentionmechanismstocaptureglobaldependencies.
• ESPMP(CL)[11]:Anoveltripletnetworkforcontrastive
learningtoenhancetheexplainabilityofstockmovement
prediction.
• SCLformer(CL)[26]:Aalgorithmtradingmethodbased
on supervised contrastive learning for sentiment recogni-
tion in text.
• DUALformer (CL) [7]: A trading model that uses a
triple loss function for feature representation and trading
decisions.
• CEformer (CL) [30, 41]): A trading model that utilizes
the cross-entropy loss function for binary classification
tasks on news text.
D.ImplementationDetails .Weaccountforthedifferences
across various stock text datasets by using a fine-tuning
approach to optimize the encoding performance for each
dataset.WeemployedaBERT-basedmodelwithanuncased
tokenization scheme to encode textual data associated with
each company’s stock. A distinct model was trained for
: Preprint submitted to Elsevier Page 7 of 17

eachstock,witheachmodelundergoing200trainingepochs
to ensure convergence. For each stock, a dedicated model
was instantiated and trained. We conducted a grid search
to optimize the hyperparameters crucial for performance,
which are𝛼 in Eq. (14) andMomentumSpanΔ in Eqs. (9) and
(10).
• 𝛼 ∈ {0.1,0.3,0.5,0.7,0.9} balances two loss compo-
nents: the contrastive alignment loss (𝐿S−M + 𝐿M−S),
which encourages consistency between sentiment and
market features, and the cross-entropy loss (𝐿CE), which
enhances polarity discrimination. A higher𝛼 emphasizes
featurealignment,whilealower 𝛼focusesondistinguish-
ing bullish and bearish dominance.
• Δ∈{−2 ,−1,0,1,2,±1,±2}controlstemporalsampling
formarketinertia: Δ=±1 toincludeimmediateadjacent
steps (past and future),Δ = −2 to consider only two
precedingsteps,and Δ=±2 tospantwostepsbeforeand
afterthecurrentsample.Thisenablesadaptivesmoothing
of market state continuity across heterogeneous entities.
Thegridsearchstrategyinvolvedsystematicallycombin-
ing different values of𝛼 andΔ to identify the optimal con-
figuration that yielded the best performance on a validation
set.
4.2. Overall Preformance (RQ1)
Weprovideexamplesfromvariousindustriestoserveas
intuitiveillustrationsoftheadvantagesofourproposedalgo-
rithm. Table 1 presents a performance comparison between
theproposedB4andotherbaselinemethods.Fromthetable,
several key observations can be noted as follows:
Compare with TMF:B4 demonstrates competitive perfor-
mance compared to traditional fusion methods like Stock-
Net, LSTM, and Transformer. While these baseline models
often excel in Cumulative Returns and Annual Return, B4
presents a more balanced performance across both returns
and risk metrics. For instance, in the AAPL dataset, Stock-
Net and LSTM achieve Cumulative Returns of 0.152 and
0.005, respectively, compared to B4’s 0.301. This suggests
thatB4outperformsthesefusionmethodsincapturinglong-
termstocktrends.However,intermsofMaxDrawdownand
Calmar Ratio, traditional methods like LSTM and Stock-
Net tend to show more substantial fluctuations, whereas
B4exhibits more stability, indicating its capability in con-
trolling risk and optimizing the return-risk tradeoff.
Compare with SoTA:B4 performs exceptionally well in
comparison to contrastive learning-based methods, partic-
ularly in terms of Cumulative Returns and Annual Re-
turn. However, contrastive learning models like ESPMP,
SCLformer, and DUALformer tend to show stronger per-
formance in Max Drawdown and Calmar Ratio, which re-
flects their emphasis on learning risk-adjusted returns. In
the EQIX dataset, CEformer achieves a Calmar Ratio of
4.597, significantly higher than B4’s 2.470, indicating that
B4focusmoreonreducingriskwhilesacrificingsomelong-
term profitability.
Full w/o BS w/o DCM w/o IP w/o P2C
0
0.1
0.2
0.3Cumulative Returns
Full w/o BS w/o DCM w/o IP w/o P2C
0
0.2
0.4Annual Return
Full w/o BS w/o DCM w/o IP w/o P2C
0
2
4Calmar Ratio
Full w/o BS w/o DCM w/o IP w/o P2C
0
0.03
0.06
0.09Max Drawdown
Figure 4:Ablation study on key components of the proposed
method, evaluating the impact of removing Price2Concept
(P2C), Bias Simulation (BS), Inertial Pairing (IP), and Dual
Competition Mechanism (DCM).
Overall, B4 strikes a balance between high returns and
low risk. Although it shows slight shortcomings in cer-
tain risk-adjusted return metrics, it demonstrates robust and
highlyadaptiveperformanceacrossmulti-industrydatasce-
narios.
4.3. Ablation Analysis (RQ2)
Four tasks are conducted to ascertain the significance
and efficacy of the core components by removingPrice-
to-Concept (w/o P2C),Bias Simulation(w/o BS), Inertial
Pairing (w/o IP), and Dual Competition Mechanism(w/o
DCM), respectively.
Figure4andTable2presentstheoverallperformanceof
various model variants across different evaluation metrics.
The B4 model (Full) consistently outperforms its ablated
counterparts in both Cumulative Returns and Annual Re-
turns matrix, highlighting the synergistic benefits of an
integrated approach. B4 w/o DCM exhibits the weakest
performance, lacking the ability to discern market trends
and thus failing to capitalize on the contrastive learning’s
potential.B4 w/oBSshowsimprovedperformance,suggest-
ing thatBias Simulationsignificantly enhances the model’s
profitability.B4 w/oIPperformsbetterthanmodelswithout
DualCompetitionMechanism orBiasSimulation,indicating
the module’s role in effectively utilizing price information.
B4w/oP2Cperformssecondarytothefullmodel,indicating
thatwhileP2Ccontributespositively,itisthetrendthatmost
significantly impacts profitability.
For individual stock analysis, diving into individual
datasetsrevealsvariancesthatunderscorethetailoredimpact
of each module: For AAPL, the full model achieves a
Cumulative Return of 0.301, with B4w/o BS lagging at -
0.015, showcasing the critical role of BS.w/oP2C manages
a respectable 0.043, underlining the value of price informa-
tion. For NFLX, the full model excels with a Cumulative
Return of 0.323, and B4w/o DCM follows closely with
0.213,indicatingthatB4 w/oDCMisparticularlyinfluential
for this stock.
: Preprint submitted to Elsevier Page 8 of 17

Table 2
Performance comparison on 5 model variants (Full,w/o P2C,
w/o BS, w/o IP, and w/o DCM) across four datasets. We
stylize the best result asBold and the second best as underline.
Dataset metric Full w/o P2C w/o BS w/o IP w/o DCM
AAPL
Cumulative Returns ↑ 0.301 0.043 -0.015 0.109 0.047
Annual Return ↑ 0.270 0.039 -0.013 0.098 0.042
Max Drawdown ↓ 0.063 0.148 0.039 0.041 0.039
Calmar Ratio ↑ 4.290 0.266 -0.346 2.381 1.076
SCHW
Cumulative Returns ↑ 0.697 0.018 0.891 0.261 0.256
Annual Return ↑ 0.763 0.020 0.980 0.283 0.277
Max Drawdown ↓ 0.123 0.104 0.233 0.149 0.156
Calmar Ratio ↑ 6.223 0.190 4.203 1.899 1.778
CVX
Cumulative Returns ↑ 0.926 0.729 0.023 0.262 -0.107
Annual Return ↑ 0.812 0.646 0.020 0.235 -0.098
Max Drawdown ↓ 0.143 0.157 0.176 0.075 0.193
Calmar Ratio ↑ 5.685 4.118 0.116 3.123 -0.507
EQIX
Cumulative Returns ↑ 0.427 0.065 -0.123 0.196 -0.221
Annual Return ↑ 0.914 0.122 -0.213 0.386 -0.366
Max Drawdown ↓ 0.118 0.086 0.158 0.138 0.221
Calmar Ratio ↑ 7.778 1.429 -1.344 2.804 -1.657
NFLX
Cumulative Returns ↑ 0.323 0.129 0.142 0.027 0.213
Annual Return ↑ 0.378 0.150 0.164 0.031 0.248
Max Drawdown ↓ 0.073 0.119 0.042 0.108 0.051
Calmar Ratio ↑ 5.169 1.261 3.874 0.289 4.811
BABA
Cumulative Returns ↑ 0.119 -0.167 -0.204 -0.231 -0.297
Annual Return ↑ 0.126 -0.175 -0.214 -0.242 -0.311
Max Drawdown ↓ 0.137 0.340 0.371 0.415 0.301
Calmar Ratio ↑ 0.915 -0.514 -0.577 -0.584 -1.031
PFE
Cumulative Returns ↑ 0.457 -0.015 0.039 -0.152 0.068
Annual Return ↑ 0.502 -0.016 0.042 -0.163 0.073
Max Drawdown ↓ 0.095 0.115 0.081 0.173 0.130
Calmar Ratio ↑ 5.273 -0.137 0.515 -0.942 0.564
DE
Cumulative Returns ↑ 0.513 0.129 0.040 0.211 0.314
Annual Return ↑ 0.680 0.165 0.051 0.272 0.411
Max Drawdown ↓ 0.122 0.167 0.201 0.162 0.146
Calmar Ratio ↑ 5.573 0.987 0.254 1.672 2.823
BHP
Cumulative Returns ↑ 0.256 0.140 0.198 -0.018 0.004
Annual Return ↑ 0.342 0.186 0.264 -0.024 0.005
Max Drawdown ↓ 0.057 0.077 0.223 0.147 0.223
Calmar Ratio ↑ 6.017 2.422 1.184 -0.161 0.024
DUK
Cumulative Returns ↑ 0.370 0.048 0.150 0.137 0.098
Annual Return ↑ 0.388 0.050 0.157 0.143 0.103
Max Drawdown ↓ 0.023 0.055 0.043 0.019 0.054
Calmar Ratio ↑ 16.932 0.917 3.617 7.514 1.916
±1 -2 -1 0 1 2 ±2
MomentumSpan
0.1
0.3
0.5
0.7
0.9Alpha
0.14
0.16
0.18
0.20
0.22
Annual Return
Figure 5:B4 under different combinations of hyperparameters.
Larger bubbles mean higher performances.
4.4. Hyper-parameters Combinations (RQ3)
We further analyze the effects of the two key hyper-
parameters introduced in Implementation Details: the loss-
balancingweight 𝛼 andthemomentumwindow Δ.Thegoal
is to reveal the interaction between𝛼 andΔ (Fig. 5) as well
as their sensitivity (Fig. 6).
First,when 𝛼issettolowervalues( e.g.,0.1and0.3),the
model’sperformanceremainsrelativelystableacrossdiffer-
ent values ofΔ, indicating that under low signal extraction
weights,themodel’sdependenceonmomentumconsistency
is weak. However, as𝛼 increases to 0.7 or 0.9, the model’s
    




$QQXDO5HWXUQ
(a)𝛼 for AAPL
      




$QQXDO5HWXUQ
(b)Δfor AAPL
    



$QQXDO5HWXUQ
(c)𝛼 for ECL
      



$QQXDO5HWXUQ (d)Δfor ECL
Figure 6: The performance of the 𝛼 and Δ on the Annual
Return metric for AAPL and ECL stocks.
performancebecomessignificantlyinfluencedbychangesin
Δ, showing greater volatility. This suggests that under high
signalextractionweights,themodel’ssensitivitytomomen-
tum span increases. WhenΔ = ±2(i.e., a larger time-step
range), the model outperforms the case whereΔ = ±1,
demonstrating that an increased momentum span positively
contributes to capturing market trends. In contrast, when
Δ=0 ,themodel’sperformanceismoderate,suggestingthat
completely ignoring momentum consistency may weaken
themodel’sabilitytoextracttrendinformation.Theoptimal
performance is achieved under a combination of high𝛼 and
Δ = ±2, indicating that emphasizing the signal extraction
task while incorporating a larger momentum span enhances
model effectiveness. Additionally, competitive results are
observed with a lower𝛼 and Δ = ±1, suggesting that
finding a balance between signal extraction and momentum
consistency is also a viable strategy.
Second,asshowninFigure6,thesensitivitytohyperpa-
rametersvariesacrossdifferentstocks.IntheAAPLdataset,
both𝛼andΔhaveasignificantimpactonannualizedreturns.
As𝛼 increasesfrom0.1to0.9,themedianannualizedreturn
gradually improves, indicating that increasing the weight of
the signal extraction task helps enhance the model’s perfor-
mance.Thehighestmedianannualizedreturnisobservedat
Δ=±1 ,suggestingthatmoderatemomentumconsideration
is most effective for the AAPL data. In contrast, the ECL
dataset exhibits relatively stable performance in annualized
returns across different values of𝛼, with slight improve-
ments only when𝛼 is set to intermediate values (e.g., 0.5
or0.7).ThissuggeststhatECLislesssensitivetothesignal
extraction task compared to AAPL. Additionally, the best
performance for ECL occurs whenΔ = 0, indicating that
forthisstock,incorporatingtoomuchforwardandbackward
time-step information may lead to overfitting or increased
: Preprint submitted to Elsevier Page 9 of 17

noise, resulting in a negative impact from momentum con-
sistency.
5. Discussion - Case Study
Intuitively, initial biases, generated by bullish and bear-
ish investors(bulls and bears), trigger price changes, and
these biases gradually correct themselves over time, poten-
tially leading to shifts in market behavior or trends. This
reflects the irrational characteristics of the market and the
significant role of investor sentiment in the formation of
marketprices.Intheinvestor-drivenmarket,individualcom-
panies may experience short-term biases due to fluctuations
in investor sentiment or information asymmetry. On an in-
dustry level, the prices of entire sectors may exhibit similar
irrational fluctuations, influenced by collective sentiment or
macroeconomic factors.
5.1. Cognitive Bias Initialization
0
2
4
6
8
Density
T opic1 Bull
T opic1 Bear
T opic1 Bull KDE
T opic1 Bear KDE
0
1
2
3
4
5
Density
T opic2 Bull
T opic2 Bear
T opic2 Bull KDE
T opic2 Bear KDE
0
5
10
15
20
25
Density
T opic3 Bull
T opic3 Bear
T opic3 Bull KDE
T opic3 Bear KDE
0.4 0.6 0.8 1.0 1.2 1.4 1.6 1.8 2.0
Attention Scores
0
2
4
6
8
10
Density
T opic4 Bull
T opic4 Bear
T opic4 Bull KDE
T opic4 Bear KDE
Z1
Z10
Z11
Z12
Z13Z14Z15
Z16
Z17
Z18
Z19
Z2
Z20
Z3
Z4 Z5 Z6
Z7
Z8
Z9
1
2
3
4
5
Bull
Bear
Figure 7: The bias of stock and Industry. Left: Variations
in attention patterns by𝐴𝑆 distribution between bullish and
bearish investors. Right: Differential attention, showed by
𝐼𝐴𝑆𝑇𝑒𝑐ℎ, to various topics within a specific industry ( e.g.,
Technology Sector) across bullish and bearish investors.
This subsection explores biases initialization by formal-
izing the concepts of Attention Score (AS) and Bias, fol-
lowed by an analysis of their distribution and industry-level
effects,toquantifyinvestors’attentiontodifferenttopicsand
their divergence in interpretation within the stock market.
Definition 1. (AttentionScore,AS)Foragivenstock 𝑠,time
window𝜏,andtopic 𝑧,wedefinetheAttentionScoreofbulls
and bears respectively as:𝐴𝑆𝑠,𝜏,𝑧 bull/bear = 1000 ⋅ |||𝐴𝑠,𝜏,𝑧 BU/BE |||, where𝐴BU and 𝐴BE are the bullish and bearish attention
weightsderivedfrom B4 model.Thescalingfactorof1000
is applied for numerical readability. A higher𝐴𝑆 indicates
strongermarketfocusontopic 𝑧regardingstock𝑠attime 𝜏.
(Industry-level Attention Score, IAS) Correspondingly,
Theaggregationof 𝐴𝑆 forallstockswithinacertainindus-
try:𝐼𝐴𝑆 ,𝜏,𝑧 = ∑ 𝑠∈(𝐴𝑆𝑠,𝜏,𝑧).
The Attention Scoreaims to measure the “degree of at-
tention”or“relevance”.Essentiallyitquantifiesthemarket’s
focus on a particular stock at a specific time in relation to a
specific topic.
Definition 2. (Bias) The absolute difference in Attention
Scores between bulls and bears on a particular topic, to
reflecttheirdivergenceininterpretingthattopic: 𝐵𝑖𝑎𝑠𝑠,𝜏,𝑧 =
𝐴𝑆𝑠,𝜏,𝑧 bull −𝐴𝑆𝑠,𝜏,𝑧 𝑏𝑒𝑎𝑟, where𝐴𝑆𝑠,𝜏,𝑧 bull ,𝐴𝑆𝑠,𝜏,𝑧 bear ≥0.
(Industry-levelBias,IBias)Correspondingly, 𝐼𝐵𝑖𝑎𝑠𝐼,𝜏,𝑧 =∑
𝑠∈𝐵𝑖𝑎𝑠𝑠,𝜏,𝑧= ∑ 𝑠∈(𝐴𝑆𝑠,𝜏,𝑧 bull−𝐴𝑆𝑠,𝜏,𝑧 bear)= ∑ 𝑠∈(𝐴𝑆𝑠,𝜏,𝑧 bull)−∑
𝑠∈(𝐴𝑆𝑠,𝜏,𝑧 bear)= 𝐼𝐴𝑆𝐼,𝑘 bull − 𝐼𝐴𝑆𝐼,𝑘 bear , where , 𝜏 and 𝑠 denotes a given industry, a time period and a set of stock
in the industry.
The bias metric shows significant market controversy.
A large discrepancy in attention between bulls and bears
indicates a substantial divergence in market understanding
or predictions regarding that topic.
To analyze the performance of bull and bear from both
stockandindustryperspectives,wevisualizethedistribution
ofaspecificstock,ABT,andaspecificindustry,technology,
as shown in Fig. 7. This comparison provides valuable
insights into the distinct yet complementary perspectives
of market participants at the individual stock level (Micro)
andbroaderindustrylevel(Macro)behave,revealingunique
patterns in attention and allocation strategies.
Micro Perspective
• Attention Distribution Pattern: Bulls and bears exhibit
similarattentiondistributionpatternsacrossdifferenttop-
ics. For ABT stock, Topic1, Topic3, and Topic4 dis-
play long-tail distribution, while Topic2 approximates a
Gaussian distribution. This indicates that certain topics
(e.g.,Topic2)receiveconsistentattention,whereasothers
(e.g., Topic3) generate significant divergence in market
interpretation.
• Attention Allocation Differences: Within the same topic,
there are notable differences in how bulls and bears allo-
cate attention. For instance, in Topic2, the distribution of
𝐴𝑆 ofbearsexhibitskurtosisanddisplaysaleftskewness
compared to that of bulls.
Macro Perspective
• Topic-SpecificAttention:Certaintopicsattractmoreatten-
tion from bulls or bears. For instance, shown as 7(right),
𝐼𝐴𝑆Tech,𝜏,Z7 bull > 𝐼𝐴𝑆Tech,𝜏,Z6 bull indicates that bulls focus more on Z7 (Corporate News) than on Z6 (Economic
Growth). Bulls also exhibit heightened attention to Z10
(Consumer Demand) and Z19 (Economic Policy Trends),
whereas bears show more interest on Z14 (Market Fluc-
tuations) and Z16 (Technology Stock Performance).
• Topic Preference Differences: Bulls and bears demon-
strate significant differences in topic preferences. For ex-
ample,𝐼𝐵𝑖𝑎𝑠𝑇𝑒𝑐ℎ,𝑡,𝑍6 >𝐼𝐵𝑖𝑎𝑠 𝑇𝑒𝑐ℎ,𝑡,𝑍7 suggests that the
divergence in biases between bulls and bears is greater
forZ6(EconomicGrowth)thanforZ7(CorporateNews).
This reflects differences in how market signals are inter-
preted by various participants, highlighting the role of
cognitive biases in shaping industry sentiment.
: Preprint submitted to Elsevier Page 10 of 17

5.2. Bias Evolution
Bias is not static - it evolves as investor attention shifts
across time and topics. To characterize this process, we
introduce the notion ofAttention Migration(𝐴𝑀).
Let(𝜏,𝑧)and(𝜏′,𝑧′)denotesourceanddestinationtime-
topic pairs. We define:
𝐴𝑀𝑠,𝜏→𝜏′,𝑧→𝑧′ =𝐴𝑆𝑠,𝜏,𝑧× 𝐴𝑆𝑠,𝜏′,𝑧′ ∑
𝑧′′∈𝜏′𝐴𝑆𝑠,𝜏′,𝑧′′ (16)
Thismeasurestheflowofattentionfromatopic 𝑧attime
𝜏 to a future topic𝑧′ at time𝜏′, normalized by the relative
salience of 𝑧′ among all topics at 𝜏′. This formulation
assumes that attention flows are both source-weighted and
target-selective, i.e., higher migration occurs when both the
origin is important and the destination is relatively more
salient.
To quantify the divergence in attention shifts between
opposing perspectives, we define theBias Migration:
𝐵𝑀𝑠,𝜏→𝜏′,𝑧→𝑧′ =𝐴𝑀𝑠,𝜏→𝜏′,𝑧→𝑧′ bull −𝐴𝑀𝑠,𝜏→𝜏′,𝑧→𝑧′ bear (17)
It is important to note that the topic set may vary over
time—new topics can emerge while others may disappear.
Thismetrictracktheoverallattentionshiftsandtheevolving
emotional divergence between bulls and bears across time.
Micro Perspective: Stock-Level
To illustrate the pattern of attention migration form a
micro perspective, we analyze the attention data of ASML
stock from September 2020 to December 2021, which is
evenly divided into four time periods as an example.
Fig. 8(Left) depicts the landscape of attention flow and
biases shift over time. Each flow line represents the mag-
nitude of𝐴𝑀, uncovering several important patterns: (1)
Attention flows as hot topics emerge or evolve. (2) The
attention to a topic at time 𝜏 is influenced by attention
from the previous period. (3) Significant biases divergences
between bull and bear at certain times intensifies market
sentiment.
For example, Topic3 is dominant in the first periods,
whileTopic4becomemoreprominentlater.BetweenTime1
to Time2, the increase in attention to Topic3 (bulls) and
Topic2 (bears) is represented by the flow lines.
Fig. 8(Right) shows the volume of attention shifts, with
redorgreenrepresentingbullishandbearishbiases,respec-
tively. The former indicates that bulls pay more attention to
aparticulartopicthanbears,leadingtoanoveralloptimistic
market sentiment towards that topic. Conversely, the latter
signifies that bears focus more on a topic, resulting in a
generally pessimistic market sentiment.
For instance, regarding Topic2 of ASML, the market
rapidly shifted from an extremely bullish bias to an ex-
tremely bearish bias, transitioning from a collective opti-
mism to a collective pessimism. In contrast, for Topic3,
the market maintained a bullish bias from Time1 to Time4,
reflecting a sustained optimistic outlook.
Macro Perspective: Industrial-Level
BullsBullsBullsBullsBulls
BearsBearsBearsBearsBears
Time1-Topic2Time1-Topic2Time1-Topic2Time1-Topic2Time1-Topic2
Time1-Topic3Time1-Topic3Time1-Topic3Time1-Topic3Time1-Topic3
Time1-Topic4Time1-Topic4Time1-Topic4Time1-Topic4Time1-Topic4
Time1-Topic5Time1-Topic5Time1-Topic5Time1-Topic5Time1-Topic5
Time2-Topic2Time2-Topic2Time2-Topic2Time2-Topic2Time2-Topic2
Time2-Topic3Time2-Topic3Time2-Topic3Time2-Topic3Time2-Topic3
Time2-Topic4Time2-Topic4Time2-Topic4Time2-Topic4Time2-Topic4
Time2-Topic5Time2-Topic5Time2-Topic5Time2-Topic5Time2-Topic5
Time3-Topic2Time3-Topic2Time3-Topic2Time3-Topic2Time3-Topic2
Time3-Topic3Time3-Topic3Time3-Topic3Time3-Topic3Time3-Topic3
Time3-Topic4Time3-Topic4Time3-Topic4Time3-Topic4Time3-Topic4
Time3-Topic5Time3-Topic5Time3-Topic5Time3-Topic5Time3-Topic5
Loading [MathJax]/extensions/MathMenu.js
Time1 2
 Time2 3
 Time3 4
T opic2
T opic3
T opic4
T opic5
 0.4
0.2
0.0
0.2
0.4
Figure8: Left:Theattentionmigrationacrosstopicsovertime,
highlighting attention flow. Flow thickness shows𝐴𝑀. Right:
The magnitude of bias shift across different time periods and
various topics, showing𝐵𝑀.
While𝐴𝑀 captures local transitions, industry-level mi-
gration patterns reveal structural regularities. To capture
this “magnetism” of topics within industries, we define the
Industry Attention Migration(𝐼𝐴𝑀) toward a topic𝑧′:
𝐼𝐴𝑀𝐼,𝑧′ = ∑
𝑠∈
∑
𝑧∈
𝐴𝑀𝑠,𝜏→𝜏′,𝑧→𝑧′ (18)
This measures how much total attention across time
flows toward𝑧′ within industry.
To normalize and compare across topics, we define the
Attention Migration Propensity (AMP):
𝐴𝑀𝑃𝐼,𝑧′ = 𝐼𝐴𝑀𝐼,𝑧′ ∑
𝑧′′∈𝐼𝐴𝑀𝐼,𝑧′′ (19)
A high𝐴𝑀𝑃𝐼,𝑧′ indicates that topic𝑧′ frequently be-
comes the “destination” of attention reallocation within in-
dustry 𝐼, suggesting a directional tendency in how biases
evolve.
As shown in Fig. 9 (Left), each arc represents an in-
dustry (e.g. I2, I6, I7, I8, I9, I11) or topic (Z1–Z10), while
the chords represent the strength of𝐼𝐴𝑀. Thicker chords
signify stronger migration.For example, topics like Z1 (En-
ergy Sector Dynamics) and Z3 (Vaccine) attract significant
attention from industries I6 (Industrials) and I7 (Materials),
suggesting these topics act as consistent focus centers. The
proportion of flow at each industry node also indicates its
topic selectivity (𝐴𝑀𝑃). Industries like I6 show strong di-
rectional focus, channeling a large share of attention toward
specific topics.
Toexaminethedynamicsofbias,wedefinetheIndustry-
level Bias Migration (IBM) toward topic𝑧′ as the total
differenceinattentionmigrationfrombullsandbearsacross
all topics and times, aggregated over an industry:
𝐼𝐵𝑀𝐼,𝑧′ = ∑
𝑠∈
∑
𝜏→𝜏′
∑
𝑧∈𝜏
(
𝐴𝑀𝑠,𝜏→𝜏′,𝑧→𝑧′ bull −𝐴𝑀𝑠,𝜏→𝜏′,𝑧→𝑧′ bear )
(20)
This quantity captures how much more attention bullish
investorsaremigratingtowardtopic 𝑧′,comparedtobearish
investors.Alargepositivevalueindicatesdirectionalconver-
gence of bullish sentiment, whereas a large negative value
implies increasing bearish focus.
To normalize these tendencies and enable comparison
across topics, we define the Bias Migration Propensity
: Preprint submitted to Elsevier Page 11 of 17

(BMP):
𝐵𝑀𝑃 𝐼,𝑧′ = 𝐼𝐵𝑀𝐼,𝑧′ ∑
𝑧′′∈|𝐼𝐵𝑀𝐼,𝑧′′ | (21)
Fig. 9 (Right) displays a heatmap of theBias Migration
Propensity(𝐵𝑀𝑃 ), reflecting how bullish and bearish per-
spectives diverge across industries and topics. Green indi-
cates topics where bulls dominate attention migration; red
signals bear dominance.
Z1
Z2
Z3
Z4
Z5 Z6 Z7 Z8
Z9
Z10
I8
I9
I2
I7
I6
I11
I1 I10 I11 I2 I3 I4 I5 I6 I7 I8 I9
Industry
Z1
Z10
Z11
Z12
Z13
Z14
Z15
Z16
Z17
Z18
Z19
Z2
Z20
Z3
Z4
Z5
Z6
Z7
Z8
Z9
Title
0.3
0.2
0.1
0.0
Figure 9: Left: Flow thickness by𝐼𝐴𝑀, the proportion of the
flow at the industry node indicates𝐴𝑀𝑃. Right: Bull-Bear
Industry-Specific Perspective Difference.𝐵𝑀𝑃 determines the
intensity of colors in heatmap.
Several patterns emerge: (1) Topic Z14 (Market Fluctu-
ations) and Z16 (Tech Stocks Performance) show deep red
rows across multiple industries (e.g., I4, I6, I9), indicating
strong bearish focus, potentially linked to risk or negative
sentiment. (2) Z3 (IHS Markit score report) and Z6 (Schall
Law Firm class action) are more green in industries like
I3–I6, suggesting bullish narratives are spreading there. (3)
Someindustries(e.g.,I2,I7)remainneutralacrossmosttop-
ics, showing balanced sentiment. (4) These patterns reveal
notonlywhereattentionismigratingbutalsothepolarityof
that migration. Strong industry-topic biases divergence can
foreshadow directional moves in sector performance.
Thecategoricalencodingschemesutilizedforthedelin-
eation of topics and industries are detailed in Appendix 4
and 6.
5.3. Market Behavior Adaptation
Through the above two steps, we have clearly observed
that how attention forms and migrates. Then we will focus
onhowattentionandbiasdrivetradingdecisions.Weselect
data for AEP stock from September 2020 to July 2021 in
Figure 10. The classification codes for topics are presented
in Appendix 5.
Volatility under Symmetric but Intense Attention. In
somecases,bothbullsandbearsfocusintenselyonthesame
high-stakes themes, such as lawsuits (z1, z2), resulting in
a low net bias but a high total emotional intensity. This
configuration leads to strong market participation on both
sides,producingvolatilepriceswingsdespitetheabsenceof
a dominant sentiment.
• Case:InOctober2020,attentionwashighlyconcentrated
on z1 (Investor lawsuits), z2 (Class action lawsuits), and
2020-09 2020-10 2020-11 2020-12 2021-01 2021-02 2021-03 2021-04 2021-05 2021-06 2021-07
Date
z2
z1
z6
z13
z18
z11
z8
z20
z4
z15
z16
z22T opic
Bull
Bear
Bias
75.0
77.5
80.0
82.5
85.0
87.5
90.0
92.5
Price
Price
Figure 10:Bull-Bear Attention and Bias Migration over Time.
Greenbubblesindicatetheintensityofbullishattentiononeach
topic, while red bubbles represent bearish attention. The size of
each bubble reflects attention magnitude, and their horizontal
drift shows attention migration over time. The yellow line
denotes the evolving bias, and the purple line shows the stock
price.
z6(SchallLawFirmclassaction).Biasoscillatedsharply
betweenpositiveandnegativebutcenterednearzero.Cor-
respondingly,thepriceexperiencedasteeprallyfollowed
by a quick reversal.
Directional Trends Driven by Bias Polarization.When
investor attention becomes structurally polarized—bulls fo-
cusing on constructive or fundamental themes (e.g., z4,
z20), while bears remain anchored to pessimistic ones (e.g.,
z1, z2)—the bias increases in magnitude, providing a clear
directional signal. These phases often align with trend con-
tinuation or reversals.
• Case: From February to April 2021, bulls shifted atten-
tion toward z4 (Energy Projects), z11 (Disability Inclu-
sion), and z20 (Quarterly Earnings), while bears main-
tainedfocusonz1(Investorlawsuits)andz2(Classaction
lawsuits). The bias reached a local maximum, and the
price steadily increased.
Sentiment Collapse Following Structural Realignment.
Sudden shifts in topic focus—particularly when bearish at-
tentionexpandstopreviouslybullishdomains—oftensignal
emotional breakdowns and lead to price corrections. These
structural realignments produce sharp transitions in the bias
curve, often moving from peak optimism to extreme pes-
simism.
• Case: At the end of March 2021, bulls were optimistic
aboutz2(Classactionlawsuits)andz4(Energyprojects),
pushingpricestoalocalpeak.However,bearishattention
quickly spread to z4 (Energy projects) and z15 (Utility
Portfolios), causing the bias to collapse and triggering a
rapid price drop.
Market Recovery Triggered by Attention Rebalancing.
Markets often recover when attention re-centers around
forward-looking or solution-oriented themes, accompanied
byrenewedoptimismfromthebullishside.Thisrebalancing
is typically marked by a reversal in the bias trend and a
reallocation of attention to themes like z4 (Energy projects)
or z20 (Quarterly Earnings Webcast).
: Preprint submitted to Elsevier Page 12 of 17

• Case: In late May 2021, the price hit a low as bears
focused on z1 (Investor lawsuits) and z22 (Customer Set-
tlements), with bias reaching an extreme minimum. Soon
after, bulls shifted attention toward z4 (Energy projects),
and the price initiated a sustained upward rebound.
These patterns demonstrate that both the magnitude and
structureofattentionandbias—notjusttheirdirectionalval-
ues—are critical in explaining market behavior. Structural
transitions in theme engagement often preempt major price
inflection points, while emotionally balanced but intense
phases produce unstable volatility. Recognizing and classi-
fying these market states enables a deeper understanding of
how information interpretation shapes price dynamics.
6. Conclusion
This paper introduces a behavioral framework for mod-
eling market regimes, grounded in the dynamics of bull
and bear sentiment. By aligning investor-driven behaviors
with evolving cognitive biases, we reveal how these bi-
ases emerge and manifest in observable market patterns.
Distinct from prior approaches focused solely on pattern
extraction, our model captures the competitive interplay be-
tweenopposinginvestorstances,offeringbothinterpretabil-
ity and predictive power. Extensive experiments on 110
publicdatasetsacross10industriesvalidatetheframework’s
robustness and broad applicability.
Looking forward, several promising directions remain.
TheseincludeenhancingB4’stemporalgranularityviareal-
timesentimentfromhigh-frequencynewsandsocialmedia,
extendingthedual-biasmodelingtomulti-assetportfoliosto
capture cross-asset sentiment interactions, and applying the
framework to derivative pricing or systemic risk scenarios.
These extensions aim to further bridge behavioral finance
theory with actionable machine learning systems in real-
world financial environments.
Acknowledgements
This work was supported by Jinan University, the Na-
tional Natural Science Foundation of China under Grant
62272198, Guangdong Key Laboratory of Data Security
and Privacy Preserving under Grant 2023B1212060036,
Guangdong-Hong Kong Joint Laboratory for Data Security
and Privacy Preserving under Grant 2023B1212120007,
Guangdong Basic and Applied Basic Research Foundation
underGrantNo.2024A1515010121,theNationalKeyR&D
ProgramofChinaunderGrant2022ZD0116800theSpecial
Funds for the Cultivation of Guangdong College Students’
ScientificandTechnologicalInnovation(ClimbingProgram
Special Funds) under Grant pdjh2025ak028.
References
[1] Ainia, N.S.N., Lutfi, L., 2019. The influence of risk perception,
risk tolerance, overconfidence, and loss aversion towards investment
decision making. Journal of Economics, Business, & Accountancy
Ventura 21, 401–413.
[2] Black, F., Scholes, M., 1973. The pricing of options and corporate
liabilities. Journal of political economy 81, 637–654.
[3] Blei, D.M., Ng, A.Y., Jordan, M.I., 2003. Latent dirichlet allocation.
J. Mach. Learn. Res. 3, 993–1022.
[4] Bollerslev, T., 1986. Generalized autoregressive conditional het-
eroskedasticity. Journal of econometrics 31, 307–327.
[5] Bollerslev, T., 1994. Arch models. Handbook of Econometrics 4.
[6] Chang,E.C.,Cheng,J.W.,Khorana,A.,2000.Anexaminationofherd
behavior in equity markets: An international perspective. Journal of
Banking & Finance 24, 1651–1679.
[7] Chen, Q., Zhang, R., Zheng, Y., Mao, Y., 2022. Dual contrastive
learning:Textclassificationvialabel-awaredataaugmentation. arXiv
preprint arXiv:2201.08702 .
[8] Cheng, D., Yang, F., Xiang, S., Liu, J., 2022. Financial time se-
ries forecasting with multi-modality graph neural network. Pattern
Recognition 121, 108218. doi: https://doi.org/10.1016/j.patcog.
2021.108218.
[9] Derakhshan, A., Beigy, H., 2019. Sentiment analysis on stock social
mediaforstockpricemovementprediction. Engineeringapplications
of artificial intelligence 85, 569–578.
[10] Ding, Q., Shi, H., Liu, B., 2024. Tradexpert: Revolutionizing trading
with mixture of expert llms. arXiv preprint arXiv:2411.00782 .
[11] Du,K.,Mao,R.,Xing,F.,Cambria,E.,2024. Explainablestockprice
movement prediction using contrastive learning, in: Proceedings of
the 33rd ACM International Conference on Information and Knowl-
edgeManagement,AssociationforComputingMachinery,NewYork,
NY, USA. p. 529–537. URL: https://doi.org/10.1145/3627673.
3679544, doi:10.1145/3627673.3679544.
[12] Duan, J., Zheng, W., Du, Y., Wu, W., Jiang, H., Qi, H., 2024. Mf-clr:
Multi-frequency contrastive learning representation for time series,
in: International Conference on Machine Learning. URL: https:
//api.semanticscholar.org/CorpusID:272330491.
[13] Emami Gohari, H., Dang, X.H., Shah, S.Y., Zerfos, P., 2024.
Modality-aware transformer for financial time series forecasting, in:
Proceedings of the 5th ACM International Conference on AI in
Finance, pp. 677–685.
[14] Fang, Y., Wang, W., Wu, P., Zhao, Y., 2023. A sentiment-enhanced
hybrid model for crude oil price forecasting. Expert Systems with
Applications 215, 119329.
[15] Feng, F., He, X., Wang, X., Luo, C., Liu, Y., Chua, T.S., 2019.
Temporal relational ranking for stock prediction. ACM Transactions
on Information Systems (TOIS) 37, 1–30.
[16] Gao, S., Wang, Y., Yang, X., 2023. Stockformer: Learning hybrid
trading machines with predictive coding., in: IJCAI, pp. 4766–4774.
[17] Godfrey, M.D., Granger, C.W., Morgenstern, O., 1964. The random-
walk hypothesis of stock market behavior a. Kyklos 17, 1–30.
[18] Grootendorst,M.,2022.Bertopic:Neuraltopicmodelingwithaclass-
based tf-idf procedure. URL: https://arxiv.org/abs/2203.05794,
arXiv:2203.05794.
[19] Gulay, E., Akgun, O.B., Bekiroglu, K., Duru, O., 2025. Predictive
performance of denoising algorithms in s&p 500 and bitcoin returns.
Expert Systems with Applications 260, 125400.
[20] Hochreiter, S., Schmidhuber, J., 1997. Long short-term memory.
NeuralComput.9,1735–1780. URL: https://doi.org/10.1162/neco.
1997.9.8.1735, doi:10.1162/neco.1997.9.8.1735.
[21] Hou, M., Xu, C., Liu, Y., Liu, W., Bian, J., Wu, L., Li, Z., Chen, E.,
Liu,T.Y.,2021. Stocktrendpredictionwithmulti-granularitydata:A
contrastivelearningapproachwithadaptivefusion,in:Proceedingsof
the30thACMInternationalConferenceonInformation&Knowledge
Management, pp. 700–709.
[22] Huang, A.H., Wang, H., Yang, Y., 2023. Finbert: A large language
model for extracting information from financial text. Contemporary
Accounting Research 40, 806–841.
[23] Iyer, R.G., Wang, W., Sun, Y., 2023. Bi-level attention
graph neural networks. URL: https://arxiv.org/abs/2304.11533,
arXiv:2304.11533.
[24] Jin, H., Yu Zhou, X., 2008. Behavioral portfolio selection in con-
tinuous time. Mathematical Finance: An International Journal of
: Preprint submitted to Elsevier Page 13 of 17

Mathematics, Statistics and Financial Economics 18, 385–426.
[25] Jin, M., Wang, S., Ma, L., Chu, Z., Zhang, J.Y., Shi, X., Chen, P.Y.,
Liang, Y., Li, Y.F., Pan, S., et al., 2023. Time-llm: Time series
forecastingbyreprogramminglargelanguagemodels. arXivpreprint
arXiv:2310.01728 .
[26] Khosla, P., Teterwak, P., Wang, C., Sarna, A., Tian, Y., Isola, P.,
Maschinot, A., Liu, C., Krishnan, D., 2021. Supervised contrastive
learning. URL:https://arxiv.org/abs/2004.11362, arXiv:2004.11362.
[27] Li, X., Shen, X., Zeng, Y., Xing, X., Xu, J., 2024a. Finreport:
Explainable stock earnings forecasting via news factor analyzing
model, in: Companion Proceedings of the ACM on Web Conference
2024, pp. 319–327.
[28] Li, X., Shen, X., Zeng, Y., Xing, X., Xu, J., 2024b. Finreport:
Explainable stock earnings forecasting via news factor analyzing
model. Companion Proceedings of the ACM on Web Conference
2024 URL:https://api.semanticscholar.org/CorpusID:268247835.
[29] Lin, P., Ma, S., Fildes, R., 2024. The extra value of online investor
sentiment measures on forecasting stock return volatility: A large-
scale longitudinal evaluation based on chinese stock market. Expert
Systems with Applications 238, 121927.
[30] Lin, T.Y., Goyal, P., Girshick, R., He, K., Dollár, P., 2017. Focal loss
for dense object detection, in: 2017 IEEE International Conference
onComputerVision(ICCV),pp.2999–3007. doi: 10.1109/ICCV.2017.
324.
[31] Liu, Y., Qin, G., Huang, X., Wang, J., Long, M., 2024. Autotimes:
Autoregressive time series forecasters via large language models.
arXiv preprint arXiv:2402.02370 .
[32] Luo, D., Liao, W., Li, S., Cheng, X., Yan, R., 2023. Causality-
guidedmulti-memoryinteractionnetworkformultivariatestockprice
movement prediction, in: Annual Meeting of the Association for
Computational Linguistics. URL:https://api.semanticscholar.org/
CorpusID:259370608.
[33] Mou, S., Xue, Q., Chen, J., Takiguchi, T., Ariki, Y., 2025. Mm-
itransformer: A multimodal approach to economic time series fore-
casting with textual data. Applied Sciences 15, 1241.
[34] Patil,A.,Sharma,H.,Sinha,A.,2024. Sentimentanalysisoffinancial
news and its impact on the stock market, in: 2024 2nd World Confer-
ence on Communication & Computing (WCONF), IEEE. pp. 1–5.
[35] Pei,Y.,Cartlidge,J.,Mandal,A.,Gold,D.,Marcilio,E.,Mazzon,R.,
2025. Cross-modal temporal fusion for financial market forecasting.
URL: https://arxiv.org/abs/2504.13522, arXiv:2504.13522.
[36] Qin, J., 2024. Msmf: Multi-scale multi-modal fusion for enhanced
stock market prediction. arXiv preprint arXiv:2409.07855 .
[37] Vaswani,A.,Shazeer,N.,Parmar,N.,Uszkoreit,J.,Jones,L.,Gomez,
A.N.,Kaiser,L.,Polosukhin,I.,2023. Attentionisallyouneed. URL:
https://arxiv.org/abs/1706.03762, arXiv:1706.03762.
[38] Xia, H., Sun, S., Wang, X., An, B., 2024. Market-gan: Adding
control to financial market data generation with semantic context, in:
Proceedings of the AAAI Conference on Artificial Intelligence, pp.
15996–16004.
[39] Xiang,S.,Cheng,D.,Shang,C.,Zhang,Y.,Liang,Y.,2022.Temporal
and heterogeneous graph neural network for financial time series
prediction,in:Proceedingsofthe31stACMinternationalconference
on information & knowledge management, pp. 3584–3593.
[40] Xu, Y., Cohen, S.B., 2018. Stock movement prediction from tweets
and historical prices, in: Proceedings of the 56th Annual Meeting
of the Association for Computational Linguistics, Association for
Computational Linguistics, Melbourne, Australia. pp. 1970–1979.
[41] Yang, S., Tang, D., 2024. A large-scale microblog dataset and stock
movementpredictionbasedonsupervisedcontrastivelearningmodel.
Neurocomputing 584, 127583. URL:https://api.semanticscholar.
org/CorpusID:268670132.
[42] Zeng, Z., Kaur, R., Siddagangappa, S., Rahimi, S., Balch, T., Veloso,
M.,2023. Financialtimeseriesforecastingusingcnnandtransformer.
arXiv preprint arXiv:2304.04912 1.
[43] Zhu, L., Zhu, Z., Zhang, C., Xu, Y., Kong, X., 2023. Multimodal
sentiment analysis based on fusion methods: A survey. Information
Fusion 95, 306–325.
[44] Zong, C., Zhou, H., 2024. Stock movement prediction with mul-
timodal stable fusion via gated cross-attention mechanism. URL:
https://arxiv.org/abs/2406.06594, arXiv:2406.06594.
[45] Zou, J., Lou, J., Wang, B., Liu, S., 2024. A novel deep reinforcement
learning based automated stock trading system using cascaded lstm
networks. Expert Systems with Applications 242, 122801.
: Preprint submitted to Elsevier Page 14 of 17

Table 3
Summary of Variables in Attention and Bias Modeling
Symbol Definition Description
𝐗𝑃 𝑡 [𝑥𝑡 Open,𝑥𝑡 Close,𝑥𝑡 Low,𝑥𝑡 High] Multivariate price input at time𝑡
𝛿 Sliding window length Historical window length for time-series input
𝑧 Topic index Index of a topic (e.g., Corporate News, Tech Fluctuations)
𝜏 Time window Discrete time period or interval
𝑠 Stock symbol A specific stock in the market
𝐼 Industry type A specific industry, e.g., finance, energy, or healthcare
 Industry set A collection of stock in industry𝐼, i.e., ={𝑠1,𝑠2,…}
𝜏 Topic set at𝜏 Topics available at time𝜏
A𝑠,𝜏,𝑧 BU ,𝐴𝑠,𝜏,𝑧 BE – Bearish attention weight (output of our model)
𝐴𝑆𝑠,𝜏,𝑧 bull/bear 1000 ⋅|𝐴𝑠,𝜏,𝑧 BU/BE| Scaled attention score for bulls/bears
𝐼𝐴𝑆𝐼,𝜏,𝑧 ∑ 𝑠∈𝐴𝑆𝑠,𝜏,𝑧 Industry-level attention score
𝐵𝑖𝑎𝑠𝑠,𝜏,𝑧 𝐴𝑆𝑠,𝜏,𝑧 bull −𝐴𝑆𝑠,𝜏,𝑧 bear Bias score at stock level
𝐼𝐵𝑖𝑎𝑠𝐼,𝜏,𝑧 𝐼𝐴𝑆 bull−𝐼𝐴𝑆 bear Industry-level bias score
𝐴𝑀𝑠,𝜏→𝜏′,𝑧→𝑧′ 𝐴𝑆𝑠,𝜏,𝑧 ⋅ 𝐴𝑆𝑠,𝜏′,𝑧′ ∑
𝑧′′ 𝐴𝑆𝑠,𝜏′,𝑧′′ Attention migration score across time and topics
𝐵𝑀𝑠,𝜏→𝜏′,𝑧→𝑧′ 𝐴𝑀 bull−𝐴𝑀 bear Bias migration at stock level
𝐼𝐴𝑀𝐼,𝑧′ 𝐼𝐴𝑀𝐼,𝑧′ = ∑ 𝑠∈ ∑ 𝑧∈𝐴𝑀𝑠,𝜏→𝜏′,𝑧→𝑧′ Total industry attention inflow to topic𝑧′
𝐴𝑀𝑃 𝐼,𝑧′ 𝐴𝑀𝑃 𝐼,𝑧′ = 𝐼𝐴𝑀𝐼,𝑧′ ∑
𝑧′′∈𝐼𝐴𝑀𝐼,𝑧′′ Normalized attention migration propensity
𝐼𝐵𝑀𝐼,𝑧′ 𝐼𝐵𝑀𝐼,𝑧′ = ∑ 𝑠∈ ∑ 𝜏→𝜏′ ∑ 𝑧∈𝜏 ( 𝐴𝑀𝑠,𝜏→𝜏′,𝑧→𝑧′ bull −𝐴𝑀𝑠,𝜏→𝜏′,𝑧→𝑧′ bear ) Net industry-level bias migration
𝐵𝑀𝑃 𝐼,𝑧′ 𝐼𝐵𝑀𝐼,𝑧′ ∑
𝑧′′∈|𝐼𝐵𝑀𝐼,𝑧′′| Normalized bias migration propensity
Appendix
A. Summary of Variables
Table 3 summarizes all notations used in our bias-
attention modeling, covering both stock-level and industry-
level constructs. These variables underpin the quantitative
formulationofattentionscores,biasstrength,andtheirtem-
poral migration dynamics across topics and market entities.
B. Dataset Details
Thefollowingtablesprovideacomprehensiveoverview
ofindustry-relatedtopics,theircorrespondingcodes,andthe
stockclassificationsfromtheCMINdataset.Thesetablesare
structuredtofacilitatetheanalysisofthematicandindustry-
specificfactorsthatinfluencestockperformanceandmarket
dynamics. To understand how these thematic developments
correlate with stock behaviors, we use topic modeling tech-
niques, specifically BERTopic [18] and LDA [3], to capture
the underlying themes and sentiment shifts.
The choice of BERTopic and LDA as topic modeling
tools reflects the specific challenges posed by the dataset,
where BERTopic is used for capturing detailed, semantic
themesfromstock-specifictopics,andLDAisemployedfor
handling large-scale industry-level data where fast process-
ing is critical.
• Table4presentsadifferentsetofthematiccodes(Z1–Z20),
modeled using LDA, focusing on broader economic and
sector-specific issues, including energy dynamics, merg-
ers and acquisitions, tech industry trends, and market
fluctuations.
• Table 5 introduces a set of industry topics (z1–z22),
derivedusingBERTopic,coveringkeyareassuchaslegal
actions, investment advice, earnings reports, and market
sentiment, which reflect various factors impacting indus-
try sectors.
• Table 6 maps industry codes (I1–I10) to their respective
explanations and lists major companies within each sec-
tor,suchastechnology,healthcare,andfinancialservices,
providingaclearerunderstandingofindustrycomposition
and stock categorization.
These tables serve as a foundation for analyzing how
thematicdevelopmentscorrelatewithstockbehaviorsacross
different industries, aiding in investment decision-making
and risk assessment strategies.
C. Algorithm design and analysis
Algorithm 1 present the main steps of B4 approach.
Space Complexity: The algorithm’s memory footprint is
dominated by the storage of sequential embeddings and in-
termediate feature maps. The Price-to-Concept (P2C) layer
: Preprint submitted to Elsevier Page 15 of 17

Table 4
Industry topic codes and explanations (cf. Fig. ??).
Topic Explanation
Z1 Energy Sector Dynamics
Z2 Investment and Funds
Z3 Vaccine
Z4 Executive Changes
Z5 Investment Strategies
Z6 Economic Growth
Z7 Corporate News
Z8 Pharmaceutical and Regulatory
Z9 Tech Industry
Z10 Consumer Demand
Z11 E-Commerce and Data
Z12 Earnings Reports
Z13 Mergers and Acquisitions
Z14 Market Fluctuations
Z15 Pharmaceutical Companies
Z16 Tech Stocks Performance
Z17 Industry Developments
Z18 Company Dynamics
Z19 Economic Policy Trends
Z20 Economic Cycles
Table 5
AEP topic codes and explanations (cf. Figs. ?? and 10.)
Topic Explanation
z1 Investor lawsuits
z2 Class action lawsuits
z3 IHS Markit score report
z4 Energy projects
z5 Utilities Sector Appraise
z6 Schall Law Firm class action
z7 Moody’s ratings and outlook
z8 Investment advice
z9 Over-selling
z10 Law lawsuits
z11 Disability Inclusion
z12 Earnings and Revenue Estimates
z13 ETF flows
z14 Analysts’ Views
z15 Durable Utility Stocks Portfolios
z16 Bids for Coal Projects
z17 Ratings and Outlook
z18 Analyst blog highlights
z19 Value comparison with DTE
z20 Quarterly Earnings Webcast
z21 Texas Power Demand Hits Record
z22 Customers Receive Settlement
requires𝑂(𝛿×𝑑) space to store price embeddings, where𝛿
is the temporal window size and𝑑 denotes the embedding
dimension. The concatenated feature matrix 𝐄 consumes
𝑂(𝛿 ×(𝑑 +𝑘)) space, with𝑘 representing the augmented
text feature dimension. Momentum-based contrastive learn-
ing introduces 𝑂(|Δ| × 𝛿2) space complexity for storing
positive/negativepairs 𝐏and 𝐍,where |Δ|isthecardinality
Table 6
Industry codes and explanations, and corresponding stocks
from the CMIN dataset.
Industry Explanation Stocks
I1 Communication CHTR, CMCSA, NFLX, T, TMUS, VZ
I2 Consumer AMZN, BABA, DIS, JD, LOW, MCD, NFLX,
NKE, SBUX, TGT, COST, DEO, KO, PG, PM,
UL, WMT
I3 Energy BP, COP, CVX, EQNR, RDS-B, XOM, TTE,
PTR
I4 Financial ACN, ADP, AC, BRK-A, JPM, MA, SCHW, V
I5 Healthcare ABBV,ABT,JNJ,LLY,NVO,NVS,PFE,TMO,
UNH
I6 Industrials BA, CAT, DE, GE, HON, MMM, RTX, UPS
I7 Materials APD, BHP, ECL, FCX, RIO, SHW, VALE
I8 Real Estate AMT, CCI, DLR, EQIX, O, PLD, PSA, SBAC
I9 Technology AAPL, ADBE, ASML, AVGO, CSCO, FB,
GOOG, MS, NVDA, ORCL, PYPL, TSM
I10 Utilities AEP, DUK, EXC, NEE, NGG, SO, SRE, XEL
Algorithm 1:B4
Input : Price sequence𝑋𝑃 𝑡 =
{𝑥(𝑂𝑝𝑒𝑛) 𝑡 ,𝑥(𝐶𝑙𝑜𝑠𝑒) 𝑡 ,𝑥(𝐿𝑜𝑤) 𝑡 ,𝑥(𝐻𝑖𝑔ℎ) 𝑡 }𝑡 𝑡−𝛿,
News corpus𝑋𝑁 𝑡 ={𝑥𝑁 𝑡 }𝑡 𝑡−𝛿, Learning rate𝜂, Epochs𝑁, Trade-off coefficient𝛼,
MomentumSpanΔ, Pretrained
embeddings𝐻, Price2Concept Layer
P2C, Bias Simulation Layers BS
Output: Prediction𝑌′ 𝑡 , Parameters𝜃
Initialize𝜃∼ (0,0.01);
for∀𝑛∈{1,...,𝑁 }do
𝐇′ ← Linear(𝐇);
𝐄price ← P2C(𝐗𝑃 𝑡 ;H′)via Eq.(1);
𝐗Aug 𝑡 ← Augment(𝐗𝑁 𝑡 )via Eq.(2);
𝐄price ← Embed(𝐗Aug 𝑡 );
𝐄 ← Concat(𝐄text, 𝐄price);
𝐡BU, 𝐡BE ← BS(𝐄) via Eq.(6);
𝑦𝑡 ← Label(𝐗𝑃 𝑡 )via Eq.(8);
,  ←∅;
for∀𝛿∈Δ do
 ← ∪{𝑥𝑗|𝑦𝑖=𝑦𝑗,|𝑖−𝑗| ≤𝛿};
 ←  ∪{𝑥𝑗|𝑦𝑖 ≠𝑦𝑗,|𝑖−𝑗| ≤𝛿};
Compute Comp, Mar via Eq.(11);
Compute CE via Eq.(13);
Total=𝛼 ⋅(Comp+ Mar)+(1− 𝛼) ⋅ CE;
𝜃 ← Adam(Total,𝜂);
of momentum spans. Parameter storage𝜃 contributes𝑂(𝑚),
where𝑚 is the total trainable parameters. The overall space
complexityscaleslinearlywith 𝛿andquadraticallywith |Δ|.
TimeComplexity: Dominatedbyiterativeembeddingtrans-
formations and pair-wise comparisons, the P2C projection
and Bias Simulation (BS) layers incur𝑂(𝑁×𝛿×𝑑2) oper-
ations per epoch due to dense matrix multiplications, where
𝑁 is the number of epochs. Momentum pair construction
: Preprint submitted to Elsevier Page 16 of 17

Table 7
Comparative performances across industries. The table presents the Cumulative Returns, Annual Returns, Max Drawdown, and
Calmar Ratio for each model, including B4, LSTM, StockNet, Transformer, ESPMP, DUAL-DNN, and SCL-DNN. We stylize the
best result asbold and the second best as underline. Note: For Max Drawdown, the smaller the better.
Industry Method B4 LSTM Transformer StockNet DUALformer CEformer SCLformer ESPMP Improve(%)
I1 Cumulative Returns ↑ 0.193 0.046 0.074 0.053 0.017 0.009 -0.024 0.083 +132.53
Annual Return ↑ 0.215 0.069 0.079 0.082 0.016 0.019 -0.023 0.107 +100.93
Max Drawdown ↓ 0.038 0.100 0.164 0.062 0.140 0.106 0.113 0.102 +63.16
Calmar Ratio ↑ 2.189 1.823 0.705 1.306 0.245 0.216 -0.237 1.043 +20.08
I2 Cumulative Returns ↑ 0.185 -0.001 0.024 0.040 0.032 -0.049 -0.026 -0.022 +362.50
Annual Return ↑ 0.223 -0.018 0.010 0.030 0.092 -0.045 -0.016 0.014 +142.39
Max Drawdown ↓ 0.011 0.147 0.116 0.176 0.133 0.156 0.178 0.136 +954.54
Calmar Ratio ↑ 2.637 -1.068 -0.005 0.081 4.969 0.594 0.705 2.034 -46.93
I3 Cumulative Returns ↑ 0.237 0.064 0.103 0.078 0.053 0.107 0.103 0.065 +121.50
Annual Return ↑ 0.317 0.066 0.122 0.092 0.082 0.147 0.149 0.089 +112.75
Max Drawdown ↓ 0.033 0.129 0.115 0.072 0.065 0.068 0.057 0.076 +72.72
Calmar Ratio ↑ 5.118 1.828 2.804 1.760 1.723 2.613 3.483 1.415 +46.94
I4 Cumulative Returns ↑ 0.688 0.307 0.269 0.229 0.272 0.248 0.225 0.264 +124.10
Annual Return ↑ 0.847 0.306 0.311 0.231 0.300 0.277 0.233 0.321 +163.86
Max Drawdown ↓ 0.067 0.202 0.241 0.165 0.138 0.134 0.156 0.159 +100.00
Calmar Ratio ↑ 4.8794 1.891 2.218 1.317 1.971 3.452 2.352 2.603 +41.31
I5 Cumulative Returns ↑ 0.432 0.084 0.323 0.083 0.112 0.114 0.112 0.120 +33.75
Annual Return ↑ 0.648 0.107 0.342 0.102 0.245 0.255 0.301 0.164 +89.47
Max Drawdown ↓ 0.074 0.122 0.123 0.121 0.081 0.085 0.092 0.115 +9.46
Calmar Ratio ↑ 27.735 1.135 2.770 1.033 6.379 9.778 40.917 3.317 -32.22
I6 Cumulative Returns ↑ 0.417 0.038 0.061 0.210 0.035 0.101 0.095 0.130 +98.57
Annual Return ↑ 0.615 0.041 0.046 0.337 0.080 0.158 0.152 0.185 +81.60
Max Drawdown ↓ 0.018 0.083 0.101 0.116 0.103 0.094 0.090 0.090 +361.11
Calmar Ratio ↑ 7.126 2.111 1.042 2.148 1.245 1.769 1.949 2.253 +216.29
I7 Cumulative Returns ↑ 0.296 -0.013 0.061 0.035 0.039 0.006 0.082 0.048 +260.98
Annual Return ↑ 0.328 -0.020 0.066 0.026 0.042 0.005 0.092 0.049 +256.52
Max Drawdown ↓ 0.033 0.129 0.196 0.146 0.140 0.143 0.137 0.179 +290.91
Calmar Ratio ↑ 2.477 0.128 0.282 1.133 0.409 0.400 0.724 0.466 +118.62
I8 Cumulative Returns ↑ 0.416 0.167 0.072 0.285 0.116 0.122 0.094 0.069 +45.96
Annual Return ↑ 0.758 0.292 0.228 0.607 0.201 0.212 0.164 0.321 +159.59
Max Drawdown ↓ 0.067 0.202 0.276 0.391 0.138 0.134 0.156 0.159 +100.00
Calmar Ratio ↑ 5.695 4.990 2.263 4.757 3.323 2.615 2.632 2.214 +14.12
I9 Cumulative Returns ↑ 0.301 -0.013 0.161 0.123 0.097 0.086 0.095 0.153 +86.96
Annual Return ↑ 0.729 -0.001 0.490 0.317 0.216 0.207 0.172 0.297 +48.78
Max Drawdown ↓ 0.064 0.125 0.124 0.087 0.090 0.087 0.076 0.064 +0
Calmar Ratio ↑ 12.515 0.438 4.154 6.336 3.915 5.902 3.143 5.990 +185.22
I10 Cumulative Returns ↑ 0.416 0.025 0.090 0.110 0.077 0.131 0.066 0.202 +105.94
Annual Return ↑ 0.430 0.027 0.093 0.173 0.081 0.125 0.069 0.187 +129.95
Max Drawdown ↓ 0.032 0.102 0.145 0.141 0.111 0.112 0.112 0.108 +218.75
Calmar Ratio ↑ 4.173 2.113 1.135 2.059 0.857 1.413 1.357 2.532 +64.81
requires 𝑂(𝑁 × |Δ| × 𝛿2) time for sliding window com-
parisons across 𝛿-length sequences. The Adam optimizer
contributes 𝑂(𝑁 × 𝑚) complexity for parameter updates.
The total time complexity is𝑂(𝑁 ×(𝛿𝑑2 + |Δ|𝛿2 +𝑚)),
demonstrating polynomial scaling with respect to sequence
length and momentum span configurations.
: Preprint submitted to Elsevier Page 17 of 17

B4 Stocknet LSTM Transformer DUAL-DNN CE-DNN SCL-DNN ESPMP
     




$'%(
7LPH6WHSV
3RUIROLR9DOXHV
   



$07
7LPH6WHSV
3RUIROLR9DOXHV
    




$ 9*2
7LPH6WHSV
3RUIROLR9DOXHV
   




)&;
7LPH6WHSV
3RUIROLR9DOXHV
    




%$
7LPH6WHSV
3RUIROLR9DOXHV
   





%%/
7LPH6WHSV
3RUIROLR9DOXHV
     


%3
7LPH6WHSV
3RUIROLR9DOXHV
  






&&,
7LPH6WHSV
3RUIROLR9DOXHV
    




&23
7LPH6WHSV
3RUIROLR9DOXHV
  






&267
7LPH6WHSV
3RUIROLR9DOXHV
  



&6&2
7LPH6WHSV
3RUIROLR9DOXHV
  




&9;
7LPH6WHSV
3RUIROLR9DOXHV
    




'(
7LPH6WHSV
3RUIROLR9DOXHV
  




'(2
7LPH6WHSV
3RUIROLR9DOXHV
   




(415
7LPH6WHSV
3RUIROLR9DOXHV
   




(415
7LPH6WHSV
3RUIROLR9DOXHV
Figure 11: The comparative performance of eight distinct models on different stock over a series of time steps. The models
include B4, LSTM, Stocknet, Transformer, CE-DNN, and ESPMP, along with DUAL-DNN and SCL-DNN highlighted in the
legend. Each line represents the progression of portfolio values.
: Preprint submitted to Elsevier Page 18 of 17
