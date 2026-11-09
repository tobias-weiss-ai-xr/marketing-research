---
title: 'F²Agent: Financial Fusion of Agentic Intelligence for Multimodal Trading'
url: https://arxiv.org/abs/2608.05668
category: ai-marketing
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Changshuo Liu
- Yanzheng Jin
- Shangfeng Cai
- Peng Fang
- Xiaokui Xiao
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.05668
pages: 32
chars: 117234
fetched_at: '2026-11-08T13:22:01+00:00'
kb_version: 1
---

# F²Agent: Financial Fusion of Agentic Intelligence for Multimodal Trading

F2AGENT: FINANCIALFUSION OFAGENTICINTELLI-
GENCE FORMULTIMODALTRADING
Changshuo Liu1†, Yanzheng Jin1†, Shangfeng Cai1∗, Peng Fang1,2, Xiaokui Xiao1, Beng Chin Ooi3
1National University of Singapore
2Huazhong University of Science and Technology
3Zhejiang University
{changshuo, yanzheng, caisf}@u.nus.edu,fangpeng@hust.edu.cn,
xkxiao@nus.edu.sg,ooibc@zju.edu.cn
ABSTRACT
With increasingly diverse and heterogeneous information sources, effectively lever-
aging multimodal data is becoming pivotal for high-quality financial trading. Al-
though recent advancements in Large Language Model (LLM)-based agents have
enabled the ingestion of multimodal inputs, existing methods fail to capture nu-
anced cross-modal dependencies and remain vulnerable to market noise, due to
limited multimodal modeling, ineffective fusion mechanisms, and inadequate ro-
bustness. To address these challenges, we propose F2Agent, a novelmultimodal
agentic paradigmdriven by the Financial Fusion of Agentic Intelligence. F2Agent
first deploys a hierarchy of specialized agents to comprehensively extract modality-
specific signals. It further introduces amodality-aware adaptive fusion mechanism
coupled withnoise-robust consistency regularizationto dynamically capture fine-
grained inter-modality dependencies and generate noise-resilient trading signals.
Extensive experiments on six stocks and cryptocurrency assets demonstrate that
F2Agent consistently outperforms 16 competitive baselines across multiple trading
metrics, with over 20% relative improvement in annualized return on average.
Notably, F2Agent delivers returns of 120.48% on GOOG and 148.41% on TSLA,
demonstrating its efficacy and robustness in varying market dynamics.
1 INTRODUCTION
Trading markets are driven by a complex interplay of heterogeneous information sources, ranging
from quantitative historical prices to qualitative textual narratives Fama (1970). While the efficient
market hypothesis posits that prices incorporate available information, effectively digesting such
multimodal signals remains challenging due to structural disparities across modalities and the high
noise levels inherent in financial streams Feng et al. (2021). Recent research has shifted toward
AI-driven methods that fuse these disparate sources to model cross-modal dependencies and support
more reliable trading decisions, beyond simple pattern extraction Feng et al. (2019); Koa et al. (2023);
Li et al. (2021).
Building on this trend, a broad spectrum of computational approaches has been explored for mul-
timodal trading, including rule-based systems with expert-defined indicators El-Baz et al. (2013),
ML/DL models that learn predictive patterns from statistical and neural architectures Yang et al.
(2020), and reinforcement learning frameworks that optimize sequential trading policies Mnih et al.
(2013); Schulman et al. (2017). Despite progress, conventional methods are largely constrained by
shallow semantics and limited capability to align unstructured textual signals with structured market
data, making it difficult to capture nuanced cross-modal dependencies Koa et al. (2023); Zhang et al.
(2024b). Motivated by this gap, recent studies have begun to build LLM-based trading systems, such
as FinGPT Liu et al. (2023), FinAgent Zhang et al. (2024b), TradingAgents Xiao et al. (2024), and
DeepFund Li et al. (2025), evolving from instruction tuning to agentic collaboration for decision
making. However, existing LLM-based systems often emphasize role-playing and task coordination,
†Equal contribution. Alphabetical order.
1
arXiv:2608.05668v1  [cs.MA]  6 Aug 2026

yet lack a principled mechanism for fusing heterogeneous modalities. In practice, they commonly rely
on prompt-level concatenation that reduces numerical time-series to textual tokens, which undermines
reliable cross-modal dependency modeling and leaves decisions vulnerable to market noise in volatile
markets Xiao et al. (2024); Li et al. (2025).
Achieving reliable multimodal trading for LLM-based agents still faces three key challenges:i)
Limited multimodal modeling.Financial markets are inherently multimodal, with signals derived
from numerical market data, technical indicators, news articles, social media, and analyst reports Ding
et al. (2015); Xu & Cohen (2018); Liu et al. (2023). These heterogeneous sources jointly shape market
dynamics Xiao et al. (2024). However, most existing methods Xiao et al. (2024); Yu et al. (2025);
Liu et al. (2023) either focus primarily on price and technical indicators or rely on textual sentiment
alone, underutilizing complementary information across modalities and overlooking their interactions.
For example, in classic “sell-the-news” scenarios Tetlock (2007), positive news sentiment may
coincide with bearish price movements. Processing modalities in isolation fails to detect cross-source
misalignment, causing agents to chase sentiment traps that joint reasoning would avoid Zhang et al.
(2024b).ii) Ineffective fusion mechanisms.Even when multiple modalities are incorporated into
LLM-based agents, aligning heterogeneous signals with different structures, semantics, and temporal
granularities remains non-trivial. Most current solutions rely on prompt-level concatenation, treating
numerical time-series as textual tokens in the context window Gruver et al. (2023); Zhang et al.
(2024b). This ad-hoc fusion rarely resolves the modality gap: the LLM’s textual bias can dominate the
joint representation and drown out subtle quantitative cues, leading to weak cross-modal interaction
modeling Liang et al. (2022); Huang et al. (2023).iii) Inadequate robustness.Financial streams are
inherently stochastic, with low signal-to-noise ratios and frequent regime shifts Fama (1970); Zhao
et al. (2023). However, existing LLM-based agents often lack explicit mechanisms to disentangle
persistent market trends from transient perturbations (e.g., short-term fluctuations or microstructure
noise). As a result, they may overreact to irrelevant news cues or minor price movements, producing
spurious trading signals and unstable decisions under volatile market dynamics Shi et al. (2023); Zhu
et al. (2025).
To address these challenges, we proposeF 2Agent, a novel multimodal agentic paradigm driven
by the Financial Fusion of Agentic Intelligence. In contrast to prevailing approaches limited to
shallow multimodal utilization, F2Agentfirstdeploys aHierarchy of Specialized Agentsto extract
complementary modality-specific signals, including a Market Analysis Agent, a Technical Analysis
Agent, a News Analysis Agent, and a Sentiment Analysis Agent.Second, F 2Agent introduces a
Modality-aware Adaptive Fusion Mechanismto dynamically capture fine-grained inter-modality
dependencies across heterogeneous sources.Third, F 2Agent leveragesNoise-robust Consistency
Regularizationto improve robustness against market noise and produce noise-resilient trading signals.
Finally, F2Agent provides an end-to-endMultimodal Agentic Trading Systemthat integrates a fine-
tuned LLM with a news summarizer, a modality processing module, and a backtesting engine to
produce trading decisions under practical trading constraints.
The main contributions of this paper are summarized as:1)We introduce aHierarchy of Specialized
Agentsto extract complementary modality-specific signals from heterogeneous sources.2)We
propose aModality-aware Adaptive Fusion Mechanismthat dynamically captures fine-grained
inter-modality dependencies, mitigating the modality gap induced by prompt-level concatenation.
3)We introduceNoise-robust Consistency Regularizationto improve robustness against market
noise and regime shifts, yielding stable trading signals.4)We implement an end-to-endMultimodal
Agentic Trading Systemand conduct extensive experiments on six assets, which demonstrate that
F2Agent consistently outperforms 16 competitive baselines (market/rule-based, ML/DL, RL, general
and financial LLM agents) across multiple trading metrics, achieving over 20% improvement in
annualized return on average. Notably, it attains returns of 120.48% on GOOG and 148.41% on
TSLA, and achieves robust performance across diverse market conditions.
2 PRELIMINARIES
Multimodality.Multimodal financial signals arise from heterogeneous data sources with distinct
statistical properties and preprocessing requirements. Instead of enumerating categories, we treat each
data source as an independent modality, allowing the modality set to evolve over time as new data
sources become available. Formally, let M denote the modality set, where each modality m∈ M
2

Figure 1: The overall architecture of F2Agent, which orchestrates a hierarchy of specialized agents to
extract latent features from heterogeneous multimodal inputs and synthesizes these representations
via a Multi-agent Fusion module to generate robust trading signals.
is characterized by a temporal sequence of T days, X m ={x m 1 , xm 2 , . . . , xm T }. The multimodal
input can be compactly represented as X={X m}m∈M. Each modality is processed by a modality-
specific encoder gm(·), followed by a projection layer P m(·), which maps raw input into a shared
latent spaceh∈R d and serves as the basis for subsequent modality fusion. For each time stept,
hm t =P m gm(xm t )  .(1)
Problem Formulation.We study multimodal stock movement prediction over a stock universe S
and a time horizon T . At date t, the multimodal input for stock s∈S is denoted as {x(i) t }I i=1 where
x(i) t is the feature of the i-th modality (market, technical, news, sentiment) available up to time t. Let
{fk}K k=1 be the K agents, each producing a hidden representation hk(X s t )∈R dk. The multi-agent
fusion module concatenates these features asf(X s t ) =h 1(X s t );h 2(X s t );· · ·;hK(X s t ).
The prediction head Fθ maps the fused representation into class probabilities over the label set
L={UP,DOWN} : Pr(ys t ∈L|X s t ) =F θ(f(X s t )). The ground-truth next-day movement label is
defined from the adjusted closing pricep c t as
Y s t =
(
0,ifp c t < pc t−1
1,ifp c t ≥p c t−1 ,(2)
whereY s t = 0indicates a price decrease andY s t = 1indicates a price increase.
3 METHODOLOGY
3.1 OVERVIEW
As illustrated in Fig. 1, F2Agent is a multimodal agentic trading system that integrates a hierarchy
of specialized agents with a modality-aware adaptive fusion mechanism to produce noise-resilient
trading signals, which are then evaluated by an end-to-end backtesting engine. Specifically, the
market and technical analysis agents encode OHLCV and technical indicator sequences using trained
forecasting models to capture temporal patterns and market dynamics. For textual modalities, the
sentiment analysis agent leverages DeepSeek-R1 (Distill-Llama-8B) Huang & Wang (2025) to infer
market sentiment from ticker-conditioned daily news summaries, while the news analysis agent uses a
Qwen-based LLM Team et al. (2024); Yang et al. (2025) fine-tuned in two stages and prompted with
CoT-style instructions Wei et al. (2022) to generate faithful reasoning explanations. The multi-agent
fusion module then aggregates agent embeddings through adaptive, modality-aware attention and
enforces robustness via consistency regularization, yielding unified representations for downstream
backtesting evaluation.
3

3.2 HIERARCHY OFSPECIALIZEDAGENTS
Market Analysis Agent.The market analysis agent encodes raw OHLCV (Open, High, Low, Close,
V olume) sequences into high-level latent representations. We treat OHLCV as a multivariate time
series with non-stationary volatility, where predictive cues can arise from non-linear price-volume
coupling Cont (2001). To capture long-range temporal dependencies and lead-lag effects within the
lookback window, we adopt a causal Transformer encoder Zerveas et al. (2021). For a stock s at
prediction date t, we construct a T -day window XMA s,t = [x MA s,t−T , . . . , xMA s,t−1]∈R T×F MA, where
xMA s,τ contains OHLCV and FMA is the feature dimension. We embed the input with positional
encoding as H(0) MA = PE(X MA s,t )W E MA ∈R T×d MA, and apply LMA causal Transformer blocks
(mask Mcausal) to obtain HMA s,t ∈R T×d MA. We use the [CLS] representation as a fixed-length
summary hMA s,t ∈R dMA when needed, with projection to the shared space performed by the fusion
module (Eq. 5).
Technical Analysis Agent.The technical analysis agent focuses on expression-based alpha fac-
tors Kakushadze (2016), which provide structured quantitative descriptions of trend, momentum, and
volatility and complement textual modalities in multimodal trading. For a stock s at prediction date t,
we assemble a T -day window of technical indicators XTA s,t = [xTA s,t−T , . . . , xTA s,t−1]∈R T×F T A, where
xTA s,τ ∈R FT Aincludes MACD, RSI, and other technical indicators. We adopt a causal Transformer
encoder to model temporal dependencies and non-linear interactions among indicators. Analogous
to the market encoder, we compute H(0) TA = PE(X TA s,t )W E TA ∈R T×d T Aand obtain the technical
representation HTA s,t ∈R T×d T Aafter LTA masked Transformer blocks. We follow the same fusion
interface as the market agent: we expose the hidden-state sequence HTA s,t and, when needed, a
fixed-length summaryh TAs, t. The fusion module then performs alignment via Eq. 5.
Sentiment Analysis Agent.The sentiment analysis agent captures sentiment signals from financial
news and social media. We use DeepSeek-R1 Huang & Wang (2025) and enable tool-augmented
retrieval: given (s, t), the agent queries external news APIs (e.g., Alpaca and Alpha Vantage), and
the retrieved articles are deduplicated and summarized by the News Summarizer (Fig. 9) to form
XSA s,t ={n s,t,1, . . . , ns,t,Ks,t }.
Per-item Sentiment Inference. For each summary ns,t,j, the agent predicts a binary label ˆcs,t,j ∈
{0,1} and a brief rationale ˆqs,t,j: (ˆcs,t,j,ˆqs,t,j) =g SA(ns,t,j), j= 1, . . . , Ks,t, where gSA(·) is
instantiated by DeepSeek-R1.
Hidden Representation for Fusion. We extract last-layer hidden states HSA s,t,j ∈R Ls,t,j ×dSA, apply
last-token poolingu s,t,j =H SA s,t,j(Ls,t,j), and aggregate across items to obtain
hSA s,t = 1 Ks,t
Ks,tX
j=1
us,t,j ∈R dSA .(3)
The fusion module mapsh SA s,t to the shared space via Eq. 5.
News Analysis Agent.As illustrated in Fig. 1, the news analysis agent (i) retrieves and consolidates
news evidence for a queried pair (s, t)and (ii) generates transparent explanations to support down-
stream prediction. Given (s, t), the agent queries external news APIs, including Alpaca News and the
New York Times API. Retrieved articles are deduplicated and summarized by the News Summarizer
(Fig. 9), yielding top-Ks,t summariesX NA s,t ={n s,t,1, . . . , ns,t,Ks,t }.
Explanation Prompting. Conditioned on (s, t)and XNA s,t , the news reasoning model gNA(·) produces
an auxiliary directional signal ˆcNA s,t ∈ {UP,DOWN}, a confidence score ˆpNA s,t ∈[0,1] , and a natural-
language explanation ˆeNA s,t , where the backbone LLM in F 2Agent instantiates gNA(·) to produce
(ˆcNA s,t ,ˆpNA s,t ,ˆeNA s,t ) =g NA(s, t,XNA s,t ).
Model Fine-tuning. Following Chain-of-Thought prompting Wei et al. (2022), we fine-tune gNA
using a two-stage instruction dataset (Fig. 3). We first collect topic-focused QA pairs (e.g., trading
decisions under different cases) generated with GPT-4o-mini Hurst et al. (2024), and then collect
simulated application trajectories designed to mimic real usage of F2Agent. We optimize a combined
objective:
4

LNA(θ) =−E (P,Y,y)∼D NA
h
logP θ(Y | P) +λ
CX
k=1
yk logP θ(k| P)
i
,(4)
where P is the instruction prompt, Y is the target response, and y∈ {0,1}C is the one-hot label for
the auxiliary classification (e.g., UP/DOWN). The first term corresponds to the language modeling
loss, while the second term is an auxiliary classification cross-entropy weighted by λ. To mitigate
majority-class bias, prompts explicitly require selecting from {UP,DOWN} Zhao et al. (2021). Our
prompt format and interaction design draw inspiration from FinMEM Yu et al. (2025), while inference
is executed in a single summarization-reasoning step (see case studies in Fig. 8 in Appendix D).
Hidden Representation for Fusion. Following the sentiment analysis agent, we apply last-token pool-
ing to the LLM’s last-layer hidden states to obtain hNA s,t ∈R dNA, which is projected into the shared
fusion space via Eq. 5. Detailed implementations are provided in Appendix D.
3.3 MODALITY-AWAREADAPTIVEFUSIONMECHANISM
Inspired by multimodal LLMs and MoE Zhang et al. (2024b;a); Mu & Lin (2025), we design
a modality-aware fusion layer to coordinate specialized agents and robustly model cross-modal
dependencies. Although recent LLM-based agents can ingest diverse inputs, existing systems often
rely on shallow, ad hoc fusion, making them brittle to cross-modal mismatch and corrupted signals.
To this end, F2Agent introduces a modality-aware adaptive fusion mechanism as the coordination
layer. As shown in Fig. 1, it enables structured information exchange across agents, captures inter-
modality dependencies, and forms a unified representation for trading decisions under noise-robust
regularization.
Modality Embedding Extraction and Alignment.Given the multimodal input x={X (m)}M m=1
Market Analysis Agent
Market Encoder
Technical Analysis Agent
Technical Encoder
Xt yt
×N
News Analysis Agent
News Encoder
W1
W2
W3
W4
Last token of Final-layer
token representation
from the backbone
Qwen2.5
Sentiment Analysis Agent
Sentiment Encoder
W1
W2
W3
W4
Last token of Final-layer
token representation
from the backbone
DeepSeek-R1

Temporal
Convolution
Networks

Multi-agent
Fusion Networks
MLP Classifier
Multi-
Head
Attention
Add
&
Norm
Feed
Forward
Add
&
Norm
Market
Emb.
Technical
Emb.
News
Emb.
Sentiment
Emb.
Unified Joint
Cross-modal
Attention Fusion
Cross-modal
Attention Block
V
Q
K
Output
Xt yt
×N
Multi-
Head
Attention
Add
&
Norm
Feed
Forward
Add
&
Norm
Figure 2: Modality-aware adaptive fu-
sion mechanism.
over M modalities, each modality sequence X (m) is pro-
cessed by a modality-specific agent fm to produce a se-
quence representation Hm(x) =f m(X (m))∈R Tm× ˜dm,
where Tm denotes the sequence length and ˜dm is the hid-
den dimension of agent m. We then extract a fixed-length
summary hm(x)∈R ˜dm. For LLM-based agents, we use
last-token pooling BehnamGhader et al. (2024) to sum-
marize the output (e.g., hm(x) =H m(x)Tm ∈R ˜dm),
where Hm(x)Tm is the last-layer hidden state of the last
token. For non-LLM agents, we use a standard sequence
summarization to obtain hm(x) (use the [CLS] token for
Transformers encoders). Since different agents may output
representations of different dimension ˜dm, we project each
hm(x) into a shared d-dimensional space via a learnable
projection Pm ∈R d× ˜dm, yielding the aligned modality
embedding em =P mhm(x)∈R d. For notational conve-
nience, we summarize the above extraction and alignment
as:
em =P m ϕm

fm(X (m))  ∈R d, P m ∈R d× ˜dm .(5)
Here ϕm(·) denotes the pooling operator: for LLM-based agents we use last-token pooling, while for
Transformer encoders we take the[CLS]representation.
Adaptive Modality Attention.Given aligned embeddings {em}M m=1, we compute modality-specific
queries, keys, and values as Qm =e mW (m) Q , Km =e mW (m) K , and Vm =e mW (m) V . We form a joint
query by concatenating modality queries, Qall = [Q1;. . .;QM ]. The modality attention weight is
then computed by αm = softmaxm
 QallK⊤ m√
d

(softmax over m), and obtain the fused representation:
Rfinal = PM m=1 αmVm. To add modality-level priors beyond instance attention, we learn a modality vectorr m and inject it into each modality’s key and value, withQ all fixed:
rm =u mA, ˜Km =e mW (m) K +r mU (m) K , ˜Vm =e mW (m) V +r mU (m) V ,(6)
where A denotes a shared modality space and um is the projection direction for modality m. By
injecting rm into ( ˜Km, ˜Vm), the fusion preserves instance-independent evidence encoded inem while
5

introducing an instance-independent, modality-specific bias via rm. We further regularize {rm} to
encourage modality-wise diversity and avoid trivial scaling solutions:
Lmodality =
X
m̸=n
 r⊤ mrn
∥rm∥ ∥rn∥
2
+
MX
m=1
∥rm∥2,(7)
wherem, nindex modalities,m̸=ndenotes distinct pairs, and∥ · ∥is theℓ 2 norm.
Noise-robust Consistency Regularization.Financial signals are noisy and certain modalities may be
missing or corrupted. To improve robustness, we randomly select a modality m⋆ ∈ {1, . . . , M}and
perturb its embedding (e.g by adding gaussian noise) to obtain a perturbed input x′ with embeddings
{e′ m}M m=1. Let s(x)∈R C and s(x′)∈R C denote the predicted logits for x and x′, where C is
the number of classes. We then let αm and α′ m be the modality attention weights computed from
x and x′, respectively, with PM m=1 αm = PM m=1 α′ m = 1. We enforce logit-level consistency and discourage the model from increasing reliance on the perturbed modality via:
Lrobust =∥s(x)−s(x ′)∥+γmax  0, α′ m⋆ −α m⋆  ,(8)
where∥ · ∥denotes theℓ2 norm andγ >0controls the strength of the attention suppression term.
Overall Objective.Given Rfinal, the prediction head outputs logits s(x)∈R C and probabilities
ˆp(x) = softmax(s(x)), and is trained by:
LCE =−
CX
c=1
y(c) log ˆp(c)(x),(9)
where y∈ {0,1} C is the one-hot label and C is the number of classes. We then augment the
supervised objective with two proposed regularizers and optimize the final loss function:
L=L CE +λ mod Lmodality +λ rob Lrobust,(10)
whereλ mod andλ rob control the modality and robustness regularization strengths.
4 MULTIMODALAGENTICTRADINGSYSTEM
F2Agent provides an end-to-endMultimodal Agentic Trading Systemthat integrates a fine-tuned LLM
with a news summarizer, a modality processing module, and a backtesting engine to produce trading
decisions under practical trading constraints. Detailed implementations are provided in Appendix E.
Figure 3: System workflow of F2Agent.
News Summarizer.To reduce noise and
control token budgets, the news summarizer
serves as a preprocessing filter. It retrieves
ticker-relevant articles via semantic vector
search, ranks them by estimated market im-
pact using DeepSeek-R1, and compresses the
most relevant items into concise daily sum-
maries for downstream reasoning.
Modality Processing Module.F 2Agent en-
codes four modalities with specialized agents: causal Transformers for OHLCV and technical indica-
tors, a fine-tuned Qwen2.5-7B-Instruct model for news reasoning and explanations, and DeepSeek-R1
for sentiment inference. Each agent outputs a fixed-length latent vector for fusion.
Backtesting Engine.The backtesting engine converts predicted signals into executable actions
under a trading policy (detailed policy is provided in Appendix E.3) and evaluates performance
on historical data using standard profitability and risk metrics. Overall, F 2Agent forms a pipeline
that encodes each modality with specialized agents, fuses the resulting representations, and outputs
trading signals with explanations and evaluation metrics. Formally, for a queried pair (s, t)with
inputsX s,t ={X MA s,t ,X TA s,t ,X NA s,t ,X SA s,t }:
(y, e,M) = Ψ

Φ

{gk(Xk s,t, s, t)}k∈{MA,T A,NA,SA}  , s, t  ,(11)
where gk denotes the modality-specific agent, Φ(·) is the fusion module, and Ψ(·) maps the fused
representation to the trading outputy, explanatione, and metricsM.
6

5 EXPERIMENTS
5.1 EXPERIMENTALSETUP
Implementation Details.We use six NVIDIA A40 GPUs for all experiments. To ensure fair
comparison, we standardize hyperparameters and optimization settings within each model category
(gradient-based, RL, and LLM) under a unified environment. Additional details on the benchmark
and experimental setup are provided in Appendix F.1.
Metrics.We evaluate F 2Agent using four standard trading metrics following Sun et al. (2023); Zong
et al. (2024): one profitability metric, annualized rate of return (ARR); two performance metrics,
cumulative return (CR) and Sharpe ratio (SR); and one risk metric, maximum drawdown (MDD).
Definitions are given in Appendix F.3.
Baselines.We comprehensively evaluate F 2Agent against 16 diverse baselines categorized into
traditional quantitative methods and LLM-based agents. The traditional category includes widely used
rule-based strategies (B&H,MACD,ZMR,SMA), deep learning methods (LSTM,Transformer),
and reinforcement learning algorithms (DQN,PPO). For LLM-based comparisons, we select four
state-of-the-art general-purpose models (Qwen3-8B,DeepSeek-R1-0528,Llama4-Scout-17B,GPT-
5-mini) and four specialized financial agents (FinGPT,FinAgent,TradingAgents,DeepFund).
Detailed baseline settings are provided in Appendix F.4.
Table 1: Performance comparison across six assets. Best, second, and third results are marked by
bold-underlined,bold, and underlined text, respectively. TheImprovementrow reports the relative
performance gain of F2Agent over the best-performing baseline. Average Rank is based on annualized
return (ARR). Additional tests on a broader stock pool spanning six sectors and an extended test
horizon are reported in Appendix F.6.
Category Model AAPL AMZN GOOG MSFT TSLA BTCUSD Avg Rank
ARR%↑SR↑MDD%↓ARR%↑SR↑MDD%↓ARR%↑SR↑MDD%↓ARR%↑SR↑MDD%↓ARR%↑SR↑MDD%↓ARR%↑SR↑MDD%↓(ARR)
Market B&H 27.95 0.61 22.99 28.51 0.63 14.64 106.38 1.98 7.98 70.52 1.76 8.03131.281.32 21.54 43.76 1.27 11.70 3.50
Rule-based
MACD -22.48 -0.73 17.46 -33.43 -0.94 19.25 30.80 0.94 12.06 13.61 0.67 6.79 51.48 0.94 17.29 29.92 1.40 8.29 13.67
ZMR 15.79 0.96 4.06 -7.08 -0.974.16 7.99 1.261.03 3.76 0.502.10 20.84 0.60 14.26 14.46 1.103.54 14.33
SMA 17.70 0.865.42-8.93 -0.49 7.36 75.422.158.94 3.50 0.672.10 25.95 0.70 18.68 -8.26 -0.51 13.91 13.17
ML/DL LSTM -7.46 -0.02 22.99 2.26 0.16 14.64 60.88 1.52 7.74 58.26 1.55 8.03 19.13 0.42 21.53 26.09 1.00 9.07 11.17 Transformer 32.90 0.72 13.77 12.60 0.38 14.64 107.85 2.12 8.32 45.64 1.35 8.03 77.88 1.09 16.99 26.35 1.18 8.26 7.00
RL DQN 32.071.0612.18 19.14 0.72 9.84 -11.54 -0.47 13.77 13.91 0.81 9.70 40.02 0.82 19.70 10.05 0.576.9711.83 PPO 27.20 0.68 9.4829.030.70 12.93 43.73 1.14 7.98 38.54 1.51 7.55 34.68 0.80 20.10 24.24 0.89 11.59 9.33
General LLMs
Qwen3-8B 7.34 0.27 18.95 5.12 0.23 19.52 49.70 1.43 10.97 21.19 0.80 9.28 87.48 1.20 23.66 32.93 1.10 12.03 10.00
DeepSeek-R1-0528 4.02 0.20 13.42 16.80 0.51 19.41 68.40 1.67 9.90 20.81 0.97 7.52 78.83 1.15 24.13 17.77 0.71 10.58 10.00
Llama4-Scout-17B 24.23 0.58 18.95 -20.46 -0.39 22.50 79.69 1.87 9.96 31.90 1.19 9.73 103.09 1.34 21.24 35.42 1.15 13.98 8.33
GPT5-mini -18.88 -0.42 25.83 -5.27 -0.06 18.01 23.85 0.74 9.59 39.21 1.63 7.55 105.17 1.55 19.44 16.08 0.71 12.39 11.50
Financial LLMs
FinGPT -7.85 -0.06 26.25 27.780.868.53 65.99 1.40 9.26 26.52 0.98 10.03 94.35 1.20 21.54 35.46 1.20 11.28 8.17
FinAgent 33.77 0.90 13.16 24.76 0.57 14.63108.162.00 7.98 69.872.19 8.02 116.87 1.24 24.4350.07 1.4714.82 3.17
TradingAgents -8.58 -0.09 26.25 23.72 0.66 15.31 66.85 1.57 9.76 48.29 1.595.3151.80 0.93 22.64 38.96 1.37 8.74 8.17
DeepFund33.830.74 15.86 14.41 0.43 16.70 54.13 1.40 12.8680.602.07 5.94 51.181.72 6.52 8.05 0.38 16.11 8.67
Ours F 2Agent 50.08 1.22 7.83 40.87 1.18 5.57 120.48 2.55 7.01 84.14 2.088.03148.41 1.94 12.60 53.57 1.52 9.791.00
Improvement(%) 48.03 15.09 – 40.79 37.21 – 11.39 18.60 – 4.39 – – 13.05 12.79 – 6.99 3.40 – –
Figure 4: Cumulative return comparison of F2Agent and competing benchmarks on AAPL, AMZN,
and BTCUSD. Results for the remaining three assets are provided in Fig. 10 of Appendix F.5.
5.2 OVERALLRESULTS
We evaluate F2Agent against 16 baselines across six diverse financial assets, including five stocks
and BTCUSD, using CR, ARR, SR, and MDD. Table 1 shows that F2Agent consistently outperforms
existing methods across most evaluation dimensions. In terms of ARR, F2Agent achieves an average
rank of 1.00 across all tested assets, indicating consistent return advantages over the nearest competitor,
FinAgent (rank 3.17), and the market benchmark Buy & Hold (rank 3.50). Specifically, F 2Agent
obtains the best ARR on all six assets and the highest SR on five assets. The gains are particularly
evident on TSLA (148.41% ARR, 1.94 SR) and GOOG (120.48% ARR, 2.55 SR), where F2Agent
surpasses the strongest baselines by clear margins. As shown in the improvement row, F 2Agent
delivers substantial gains over the best-performing alternative, with improvements of up to 48.03% in
ARR and 18.60% in SR.
7

Table 2: Ablation study: MF , MP , MR denote the
adaptive fusion module, modality prior, robustness
regularizer, respectively.Bolddenotes best results.
Method Modules Metrics
MF MP MR ARR(%)↑SR↑MDD(%)↓
AAPL
Concat. Fusion× × ×19.21 0.33 22.99
F2Agent ✓ ✓ ✓ 50.08 1.22 7.83
w/oM P , MR ✓ × × 27.28 0.57 22.99
w/oM R ✓ ✓ × 34.77 0.86 8.46
w/oM P ✓ × ✓ 38.04 0.80 10.69
BTCUSD
Concat. Fusion× × ×7.18 0.40 10.76
F2Agent ✓ ✓ ✓ 53.57 1.52 9.79
w/oM P , MR ✓ × × 15.32 0.72 16.28
w/oM R ✓ ✓ × 32.45 1.20 9.79
w/oM P ✓ × ✓ 46.22 1.16 11.70
Figure 4 further illustrates the cumulative return
trajectories on representative assets. On AAPL
and AMZN, F2Agent establishes an early advan-
tage and maintains stable return accumulation
over most of the test horizon. On BTCUSD,
where all methods exhibit larger fluctuations,
F2Agent remains among the strongest perform-
ers while avoiding the severe reversals observed
in several baselines. This suggests that the pro-
posed multimodal agentic design improves not
only final profitability but also temporal robust-
ness under different market conditions.
While conservative rule-based methods occa-
sionally achieve lower MDDs at the cost of re-
turns, F 2Agent strikes a stronger balance be-
tween profitability and drawdown control. In
contrast, several baselines exhibit instability or
asset-specific behavior. Traditional ML/DL and
RL methods show higher cross-asset variance, while FinAgent trails F 2Agent in profitability and
generalizability. These findings suggest multimodal fusion improves decision robustness across
diverse market dynamics.
5.3 ABLATIONSTUDY
Table 2 shows that the proposed fusion design plays an important role in robust performance. The
full F2Agent model clearly outperforms the concatenation-based fusion baseline on both AAPL and
BTCUSD, suggesting that simple feature concatenation is less effective for integrating heterogeneous
financial signals. The improvement is especially pronounced on the higher-volatility BTCUSD asset
in terms of ARR and SR, indicating that the proposed design can better handle noisy or conflicting
modality cues. The ablation variants further support the contribution of each component. Removing
MP or MR weakens return and risk-adjusted performance, while removing both leads to the largest
degradation. This suggests that the modality prior guides the fusion process, whereas the robustness
regularizer improves stability under noisy cross-modal interactions. The full model performs best
overall, which indicates component complementarity.
5.4 ROBUSTNESSSTUDY
To assess robustness under heterogeneous information sources, we compare F 2Agent with the
Table 3: Robustness analysis of F 2Agent under different
modality configurations. Additional random seed variance
and significance analyses are provided in Appendix G.
Modalities Llama4-Scout FinAgent F 2Agent
N M T S ARR(%)↑SR↑MDD(%)↓ARR(%)↑SR↑MDD(%)↓ARR(%)↑SR↑MDD(%)↓
AAPL
✓× × ×18.78 0.55 15.73 22.36 0.59 19.43 26.61 0.60 22.99
✓ ✓× ×36.31 1.00 13.10 – – – 47.29 1.01 12.58
✓×✓×38.34 0.82 18.95 – – – 47.181.22 5.09
✓× ×✓– – – 19.12 0.50 22.25 39.42 0.98 8.00
✓ ✓ ✓×24.23 0.58 18.95 26.23 0.58 22.99 33.97 0.70 22.98
✓ ✓×✓– – – – – – 24.03 0.59 18.95
✓×✓ ✓– – – – – – 28.36 0.61 22.99
✓ ✓ ✓ ✓– – – 33.77 0.90 13.1650.08 1.227.83
BTCUSD
✓× × ×40.20 1.20 10.23 27.85 0.82 21.39 41.68 1.27 9.79
✓ ✓× ×20.63 0.76 11.83 – – – 28.63 1.08 11.88
✓×✓×18.00 0.68 17.65 – – – 22.00 1.048.48
✓× ×✓– – – 51.98 1.50 14.25 43.571.718.67
✓ ✓ ✓×35.42 1.15 13.98 19.43 0.72 13.40 47.10 1.58 11.27
✓ ✓×✓– – – – – – 40.92 1.20 11.91
✓×✓ ✓– – – – – – 48.56 1.57 10.52
✓ ✓ ✓ ✓– – – 50.07 1.47 14.8253.571.52 9.79
strongest general LLM baseline
(Llama4-Scout-17B) and financial
LLM baseline (FinAgent) across
different modality combinations. Re-
sults on AAPL and the highly volatile
BTCUSD asset (Table 3) underscore
the value of our modality-aware
adaptive fusion and noise-robust con-
sistency regularization. The baselines
often degrade as more modalities
are added, suggesting difficulty in
resolving conflicting cross-modal
cues: on AAPL, Llama4-Scout-17B
worsens when technical indicators
are appended to news and market
inputs, and on BTCUSD, FinAgent
likewise shows reduced risk-adjusted
performance under multimodal
integration. In contrast, F 2Agent
remains stable as more modalities are
8

incorporated and benefits from richer multimodal inputs. Across both assets, the full multimodal
setting achieves the strongest or near-strongest risk-adjusted performance, showing that hierarchical
agent specialization, adaptive fusion, and consistency regularization improve inter-modality modeling
and robustness.
5.5 TOKENCONSUMPTIONANALYSIS
We evaluate practical deployment costs by quantifying the average daily token consumption required
FinGPT FinAgent
T radingAgents
DeepFund F2 Agent
103
104
Tokens per Day
Figure 5: Token consumption analysis.
for signal generation across varying assets. As shown
in Figure 5, empirical results demonstrate that F 2Agent
achieves superior token efficiency compared to compet-
ing frameworks like TradingAgents and FinAgent, which
shows that complex architectures need not incur exces-
sive overhead. This efficiency stems from the strategic
architectural design of F2Agent, which aims to minimize
unnecessary reliance on general-purpose LLMs. Unlike
baselines that process heterogeneous data streams through
monolithic LLM calls, our framework allocates computa-
tion across specialized agents. Token-intensive reasoning
is confined mainly to the news and sentiment agents, where
textual understanding is essential, while other components rely on structured processing to reduce
overhead without degrading performance.
5.6 STOCKMOVEMENTPREDICTIONENHANCEMENT
AAPL
AMZNGOOG
MSFT
TSLA BTCUSD
48
52
56
60
(i) Accuracy (ACC)
AAPL
AMZNGOOG
MSFT
TSLA BTCUSD
-0.05
0.05
0.15
0.25
(ii) MCC Score
w/o MaF F2Agent
Figure 6: MaF impact on performance.
To intuitively assess the contribution of the Multi-agent Fu-
sion (MaF) module, we present a radar chart comparison in
Figure 6. The visualization provides empirical support for
the importance of the module. Geometrically, the F2Agent
polygon extends beyond the ablated variant on all axes,
which indicates consistent performance gains across assets.
This consistency suggests that MaF improves robustness
beyond isolated asset-specific performance effects. This
gap is even more pronounced for the Matthews Correlation
Coefficient (MCC), where the ablated model lies much
closer to the origin, with MCC values near zero, suggest-
ing limited ability to capture directional trends. In contrast, the full model shows a substantially
larger coverage area. Overall, this visual evidence suggests that the MaF module plays an important
role in fusing heterogeneous inputs and capturing fine-grained inter-modality dependencies.
5.7 QUALITATIVEANALYSIS: CASESTUDY ONAAPL
To examine F2Agent’s robustness to noise and cross-modal reasoning, we study AAPL from April to
October 2025 (Fig. 7). Compared with DeepFund, F 2Agent better handles noisy narratives, structural
risks, and signal confirmation. On Sep. 22, DeepFund issues BUY on an overstated iPhone 17
preorder narrative, while F2Agent finds weak cross-modal support and chooses HOLD. On May 22,
halted expansion and partnership backlash indicate deterioration; DeepFund still issues BUY from
oversold technical cues, whereas F2Agent chooses SELL based on news-driven risk evidence. On
Apr. 10, aligned valuation and accumulation signals prompt F 2Agent to BUY , while DeepFund
issues SELL. Overall, this case study (see Appendix H) suggests that F2Agent relies on cross-modal
evidence rather than isolated modality cues.
9

F2Agent Buy & Hold DeepFund
Cumulative Return (%)
For Bad News:
Silicon Shield Weakened, Reshoring Calls
Renewed, Strategic Risks Ignited.
For Good News:
Valuation Supported,
Whales Accumulated.
F2Agent HOLD
DeepFund BUY
F2Agent BUY
DeepFund SELL
For Bad News:
Litigation Escalated,
Integrity Questioned.
F2Agent HOLD
DeepFund SELL
For Bad News:
Expansion Halted,
Partnership Backlashed,
Dilemma Confronted.
F2Agent SELL
DeepFund BUY
For Unsustainable News:
Rumors Circulated,
Upside Projected by
Goldman Sachs.
F2Agent HOLD
DeepFund BUY
For Bad News:
AI competitiveness Failed,
Monopoly Weakened.
F2Agent SELL
DeepFund HOLD
For Good News:
Support Pledged by Trump,
Siri will be driven by Gemini.
F2Agent BUY
DeepFund HOLD
For Unsustainable
News: Preorders for
iPhone 17 Topped,
Significance of
iPhone 17
Exaggerated.
F2Agent  HOLD
DeepFund BUY
Figure 7: Case study of F2Agent vs. DeepFund when performing single asset trading. DeepFund is
the strongest baseline on AAPL among the compared alternatives.
6 CONCLUSION
F2Agent is a multimodal agentic paradigm for financial trading that improves cross-modal under-
standing and robustness under noisy markets. F2Agent organizes a hierarchy of specialized agents
to extract modality-specific signals from heterogeneous sources, which provides a holistic view of
market dynamics. It further introduces a modality-aware adaptive fusion mechanism to capture
fine-grained inter-modality dependencies and produce coherent trading representations. In addition,
noise-robust consistency regularization improves stability under corrupted or shifting modalities,
enhancing reliability in information-rich environments. Future work will extend F2Agent to portfolio
management for multimodal, risk-aware allocation under realistic trading frictions.
ACKNOWLEDGEMENTS
We would like to express our gratitude to Yumo Yao and Yiqiu Liu for their contributions to the initial
design and implementation of the trading system. We also thank the anonymous reviewers for their
valuable feedback and constructive comments that helped improve this manuscript.
REFERENCES
Parishad BehnamGhader, Vaibhav Adlakha, Marius Mosbach, Dzmitry Bahdanau, Nicolas Chapados,
and Siva Reddy. Llm2vec: Large language models are secretly powerful text encoders.arXiv
preprint arXiv:2404.05961, 2024.
William Brock, Josef Lakonishok, and Blake LeBaron. Simple technical trading rules and the
stochastic properties of stock returns.The Journal of finance, 47(5):1731–1764, 1992.
Rodolfo C Cavalcante, Rodrigo C Brasileiro, Victor LF Souza, Jarley P Nobrega, and Adriano LI
Oliveira. Computational intelligence and financial markets: A survey and future directions.Expert
Systems with Applications, 55:194–211, 2016.
Zihan Chen, Lei Nico Zheng, Cheng Lu, Jialu Yuan, and Di Zhu. Chatgpt informed graph neural
network for stock movement prediction.arXiv preprint arXiv:2306.03763, 2023.
Rama Cont. Empirical properties of asset returns: stylized facts and statistical issues.Quantitative
finance, 1(2):223, 2001.
Xiao Ding, Yue Zhang, Ting Liu, and Junwen Duan. Deep learning for event-driven stock prediction.
InIjcai, volume 15, pp. 2327–2333, 2015.
Hazim El-Baz, Ibrahim Al Awadhi, and Assia Lasfer. Sma and macd combinations for stock
investment decisions in frontier markets: evidence from dubai financial market.International
Journal of Financial Engineering and Risk Management, 1(2):113–128, 2013.
10

Eugene F Fama. Efficient capital markets: A review of theory and empirical work.The journal of
Finance, 25(2):383–417, 1970.
Fuli Feng, Xiangnan He, Xiang Wang, Cheng Luo, Yiqun Liu, and Tat-Seng Chua. Temporal
relational ranking for stock prediction.ACM Transactions on Information Systems (TOIS), 37(2):
1–30, 2019.
Fuli Feng, Moxin Li, Cheng Luo, Ritchie Ng, and Tat-Seng Chua. Hybrid learning to rank for
financial event ranking. InProceedings of the 44th International ACM SIGIR Conference on
Research and Development in Information Retrieval, pp. 233–243, 2021.
Thomas Fischer and Christopher Krauss. Deep learning with long short-term memory networks for
financial market predictions.European journal of operational research, 270(2):654–669, 2018.
Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad
Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Alex Vaughan, et al. The llama 3 herd of
models.arXiv preprint arXiv:2407.21783, 2024.
Nate Gruver, Marc Finzi, Shikai Qiu, and Andrew G Wilson. Large language models are zero-shot
time series forecasters.Advances in Neural Information Processing Systems, 36:19622–19635,
2023.
Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu,
Shirong Ma, Peiyi Wang, Xiao Bi, et al. Deepseek-r1: Incentivizing reasoning capability in llms
via reinforcement learning.arXiv preprint arXiv:2501.12948, 2025.
Anne Lundgaard Hansen and Sophia Kazinnik. Can chatgpt decipher fedspeak?Available at SSRN
4399406, 2024.
Donghao Huang and Zhaoxia Wang. Explainable sentiment analysis with deepseek-r1: Performance,
efficiency, and few-shot learning.IEEE Intelligent Systems, 2025.
Shaohan Huang, Li Dong, Wenhui Wang, Yaru Hao, Saksham Singhal, Shuming Ma, Tengchao Lv,
Lei Cui, Owais Khan Mohammed, Barun Patra, et al. Language is not all you need: Aligning
perception with language models.Advances in Neural Information Processing Systems, 36:
72096–72109, 2023.
Aaron Hurst, Adam Lerer, Adam P Goucher, Adam Perelman, Aditya Ramesh, Aidan Clark, AJ Os-
trow, Akila Welihinda, Alan Hayes, Alec Radford, et al. Gpt-4o system card.arXiv preprint
arXiv:2410.21276, 2024.
Zhengyao Jiang, Dixing Xu, and Jinjun Liang. A deep reinforcement learning framework for the
financial portfolio management problem.arXiv preprint arXiv:1706.10059, 2017.
Zura Kakushadze. 101 formulaic alphas.Wilmott, 2016(84):72–81, 2016.
Kelvin JL Koa, Yunshan Ma, Ritchie Ng, and Tat-Seng Chua. Diffusion variational autoencoder
for tackling stochasticity in multi-step regression stock price prediction. InProceedings of the
32nd ACM International Conference on Information and Knowledge Management, pp. 1087–1096,
2023.
Changlun Li, Yao Shi, Chen Wang, Qiqi Duan, Runke Ruan, Weijie Huang, Haonan Long, Lijun
Huang, Nan Tang, and Yuyu Luo. Time travel is cheating: Going live with deepfund for real-time
fund investment benchmarking.arXiv preprint arXiv:2505.11065, 2025.
Wei Li, Ruihan Bao, Keiko Harimoto, Deli Chen, Jingjing Xu, and Qi Su. Modeling the stock
relation with graph network for overnight stock movement prediction. InProceedings of the
twenty-ninth international conference on international joint conferences on artificial intelligence,
pp. 4541–4547, 2021.
Paul Pu Liang, Yiwei Lyu, Xiang Fan, Jeffrey Tsaw, Yudong Liu, Shentong Mo, Dani Yogatama,
Louis-Philippe Morency, and Ruslan Salakhutdinov. High-modality multimodal transformer:
Quantifying modality & interaction heterogeneity for high-modality representation learning.arXiv
preprint arXiv:2203.01311, 2022.
11

Xiao-Yang Liu, Hongyang Yang, Qian Chen, Runjia Zhang, Liuqing Yang, Bowen Xiao, and
Christina Dan Wang. Finrl: A deep reinforcement learning library for automated stock trading in
quantitative finance.arXiv preprint arXiv:2011.09607, 2020.
Xiao-Yang Liu, Guoxuan Wang, Hongyang Yang, and Daochen Zha. Fingpt: Democratizing internet-
scale data for financial large language models.arXiv preprint arXiv:2307.10485, 2023.
Alejandro Lopez-Lira and Yuehua Tang. Can chatgpt forecast stock price movements? return
predictability and large language models.arXiv preprint arXiv:2304.07619, 2023.
V olodymyr Mnih, Koray Kavukcuoglu, David Silver, Alex Graves, Ioannis Antonoglou, Daan
Wierstra, and Martin Riedmiller. Playing atari with deep reinforcement learning.arXiv preprint
arXiv:1312.5602, 2013.
Siyuan Mu and Sen Lin. A comprehensive survey of mixture-of-experts: Algorithms, theory, and
applications.arXiv preprint arXiv:2503.07137, 2025.
John J Murphy.Technical analysis of the financial markets: A comprehensive guide to trading
methods and applications. Penguin, 1999.
David MQ Nelson, Adriano CM Pereira, and Renato A De Oliveira. Stock market’s price movement
prediction with lstm neural networks. In2017 International joint conference on neural networks
(IJCNN), pp. 1419–1426. Ieee, 2017.
Isaac Kofi Nti, Adebayo Felix Adekoya, and Benjamin Asubam Weyori. A systematic review of
fundamental and technical analysis of stock market predictions.Artificial Intelligence Review, 53
(4):3007–3057, 2020.
Jigar Patel, Sahil Shah, Priyank Thakkar, and Ketan Kotecha. Predicting stock and stock price index
movement using trend deterministic data preparation and machine learning techniques.Expert
systems with applications, 42(1):259–268, 2015.
Tohida Rehman, Debarshi Kumar Sanyal, and Samiran Chattopadhyay. How green are neural
language models? analyzing energy consumption in text summarization fine-tuning.arXiv preprint
arXiv:2501.15398, 2025.
John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy
optimization algorithms.arXiv preprint arXiv:1707.06347, 2017.
Omer Berat Sezer, Mehmet Ugur Gudelek, and Ahmet Murat Ozbayoglu. Financial time series
forecasting with deep learning: A systematic literature review: 2005–2019.Applied soft computing,
90:106181, 2020.
Freda Shi, Xinyun Chen, Kanishka Misra, Nathan Scales, David Dohan, Ed H Chi, Nathanael
Schärli, and Denny Zhou. Large language models can be easily distracted by irrelevant context. In
International Conference on Machine Learning, pp. 31210–31227. PMLR, 2023.
Shuo Sun, Molei Qin, Wentao Zhang, Haochong Xia, Chuqiao Zong, Jie Ying, Yonggang Xie,
Lingxuan Zhao, Xinrun Wang, and Bo An. Trademaster: A holistic quantitative trading platform
empowered by reinforcement learning.Advances in Neural Information Processing Systems, 36:
59047–59061, 2023.
Richard S Sutton, Andrew G Barto, et al.Reinforcement learning: An introduction, volume 1. MIT
press Cambridge, 1998.
Qwen Team et al. Qwen2 technical report.arXiv preprint arXiv:2407.10671, 2(3), 2024.
Paul C Tetlock. Giving content to investor sentiment: The role of media in the stock market.The
Journal of finance, 62(3):1139–1168, 2007.
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny
Zhou, et al. Chain-of-thought prompting elicits reasoning in large language models.Advances in
neural information processing systems, 35:24824–24837, 2022.
12

Shijie Wu, Ozan Irsoy, Steven Lu, Vadim Dabravolski, Mark Dredze, Sebastian Gehrmann, Prabhan-
jan Kambadur, David Rosenberg, and Gideon Mann. Bloomberggpt: A large language model for
finance.arXiv preprint arXiv:2303.17564, 2023.
Yijia Xiao, Edward Sun, Di Luo, and Wei Wang. Tradingagents: Multi-agents llm financial trading
framework.arXiv preprint arXiv:2412.20138, 2024.
Yumo Xu and Shay B Cohen. Stock movement prediction from tweets and historical prices. In
Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume
1: Long Papers), pp. 1970–1979, 2018.
An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang
Gao, Chengen Huang, Chenxu Lv, et al. Qwen3 technical report.arXiv preprint arXiv:2505.09388,
2025.
Xiao Yang, Weiqing Liu, Dong Zhou, Jiang Bian, and Tie-Yan Liu. Qlib: An ai-oriented quantitative
investment platform.arXiv preprint arXiv:2009.11189, 2020.
Yangyang Yu, Zhiyuan Yao, Haohang Li, Zhiyang Deng, Yuechen Jiang, Yupeng Cao, Zhi Chen,
Jordan W Suchow, Zhenyu Cui, Rong Liu, et al. Fincon: A synthesized llm multi-agent system
with conceptual verbal reinforcement for enhanced financial decision making.Advances in Neural
Information Processing Systems, 37:137010–137045, 2024.
Yangyang Yu, Haohang Li, Zhi Chen, Yuechen Jiang, Yang Li, Jordan W Suchow, Denghui Zhang,
and Khaldoun Khashanah. Finmem: A performance-enhanced llm trading agent with layered
memory and character design.IEEE Transactions on Big Data, 2025.
George Zerveas, Srideepika Jayaraman, Dhaval Patel, Anuradha Bhamidipaty, and Carsten Eickhoff.
A transformer-based framework for multivariate time series representation learning. InProceedings
of the 27th ACM SIGKDD conference on knowledge discovery & data mining, pp. 2114–2124,
2021.
Kai Zhang, Yi Luan, Hexiang Hu, Kenton Lee, Siyuan Qiao, Wenhu Chen, Yu Su, and Ming-Wei
Chang. Magiclens: Self-supervised image retrieval with open-ended instructions.arXiv preprint
arXiv:2403.19651, 2024a.
Wentao Zhang, Lingxuan Zhao, Haochong Xia, Shuo Sun, Jiaze Sun, Molei Qin, Xinyi Li, Yuqing
Zhao, Yilei Zhao, Xinyu Cai, et al. A multimodal foundation agent for financial trading: Tool-
augmented, diversified, and generalist. InProceedings of the 30th acm sigkdd conference on
knowledge discovery and data mining, pp. 4314–4325, 2024b.
Yunhao Zhang and Junchi Yan. Crossformer: Transformer utilizing cross-dimension dependency
for multivariate time series forecasting. InThe eleventh international conference on learning
representations, 2023.
Lifan Zhao, Shuming Kong, and Yanyan Shen. Doubleadapt: A meta-learning approach to incremental
learning for stock trend forecasting. InProceedings of the 29th ACM SIGKDD Conference on
Knowledge Discovery and Data Mining, pp. 3492–3503, 2023.
Zihao Zhao, Eric Wallace, Shi Feng, Dan Klein, and Sameer Singh. Calibrate before use: Improving
few-shot performance of language models. InInternational conference on machine learning, pp.
12697–12706. PMLR, 2021.
Fengbin Zhu, Xiang Yao Ng, Ziyang Liu, Chang Liu, Xianwei Zeng, Chao Wang, Tianhui Tan, Xuan
Yao, Pengyang Shao, Min Xu, et al. Findeepresearch: Evaluating deep research agents in rigorous
financial analysis.arXiv preprint arXiv:2510.13936, 2025.
Chuqiao Zong, Chaojie Wang, Molei Qin, Lei Feng, Xinrun Wang, and Bo An. Macrohft: Memory
augmented context-aware reinforcement learning on high frequency trading. InProceedings of the
30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, pp. 4712–4721, 2024.
13

Appendix
•A. Related Work. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .15
•B. Notations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
•C. Details of Problem Formulation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
•D. Details of Multiple Agents in F 2Agent. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
•E. Details of F 2Agent Design. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
·E.1. News Summarizer. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
·E.2. Modality Processing Module. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
·E.3. Backtesting Engine. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
•F. Details of Comparison with Baselines. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
·F .1. Implementation Details. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
·F .2. Modality Definitions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
·F .3. Formulations of Used Metrics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
·F .4. Details of Baselines. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
·F .5. Full Experimental Results of Stocks Mentioned in Paper. . . . . . . . . . . . . . . . . . . 24
·F .6. Experimental Results of Broader Asset Pool and Extended Test Horizons. . . . 24
•G. Details of Random-seed Robustness and Statistical Significance
•H. Details of Case Study. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
•I. Details of Stock Movement Predictions Enhancement. . . . . . . . . . . . . . . . . . . . . . . . . 32
14

A RELATEDWORK
Vanilla Trading Techniques.The evolution of quantitative trading strategies has progressed from
static heuritics Brock et al. (1992) to sophisticated data-driven decision making models Cavalcante
et al. (2016). Early methods were predominantly rule-based, relying on technical indicators such as
Moving Average Convergence Divergence (MACD) and Relative Strength Index (RSI) derived from
market microstructure theories Murphy (1999); Kakushadze (2016). While computationally efficient
and interpretable, these strategies suffer from structural rigidity, limiting their ability to adapt to
non-stationary market dynamics or capture complex non-linear patterns. To address these limitations,
research shifted towards Machine Learning (ML) and Deep Learning (DL) paradigms. Algorithms
ranging from Support Vector Machines (SVMs) Patel et al. (2015) to advanced sequence modeling
architectures like Nelson et al. (2017) and Transformers Fischer & Krauss (2018); Sezer et al. (2020);
Zhang & Yan (2023), became standard for capturing temporal dependencies in financial time series.
Despite their superior pattern recognition capabilities, these prediction-focused discriminative models
typically operate on isolated modalities or employ shallow fusion schemes, limiting their ability
to captures fine-grained cross-modal dependencies and robustly integrate heterogeneous financial
signals. Consequently, Deep Reinforcement Learning (DRL) emerged as more comprehensive
framework, formulating as a Markov Decision Process (MDP) Sutton et al. (1998) to optimize
long-term cumulative rewards Jiang et al. (2017); Liu et al. (2020). Although DRL methods excel
at dynamic portfolio management Liu et al. (2020), they generally suffer from sample inefficiency
and lack the semantic capacity to process unstructured information (e.g., news and policy reports),
limiting their effectiveness in information-rich environments.
LLM-based Trading Techniques.The advent of Large Language Models (LLMs) has significantly
advanced financial analysis by introducing semantic reasoning capabilities Wu et al. (2023), yet
challenges in multimodal integration persist. Early studies Chen et al. (2023) leveraged general-
purpose LLMs (e.g., GPT-4) for zero-shot sentiment analysis and market prediction, employing
prompt engineering techniques such as Chain-of-Thought (CoT) to extract trading signals from textual
data Lopez-Lira & Tang (2023); Wei et al. (2022); Hansen & Kazinnik (2024). However, without
domain-specific fine-tuning, these general LLMs often hallucinate on quantitative tasks and struggle
to align textual sentiment with precise market movements. To bridge this domain gap, researchers
developed Financial LLMs such as FinGPT Liu et al. (2023) and BloombergGPT Wu et al. (2023),
which are fine-tuned on extensive financial corpora to enhance domain alignment. Building upon
these foundations, the field has recently advanced towards agentic trading, where LLMs function
as autonomous agents equipped with memory, reflection, and tool-use capabilities Yu et al. (2025);
Zhang et al. (2024b); Xiao et al. (2024); Li et al. (2025). Despite enabling dynamic interaction
with market environments, most existing agents remain predominantly text-centric. They tend to
process numerical and textual modalities in isolation , a limitation that the proposed F2Agent system
is explicitly to address.
B NOTATIONS
To improve clarity and maintain consistent notation throughout the paper, we provide a notation table
as a quick reference (see Table 4) for the definitions of all symbols used.
C DETAILS OFPROBLEMFORMULATION
In addition to numerical modalities, we incorporate textual news. For stocks at date t, the summarized
news set is N s t ={n s t,1, . . . , ns t,|N s t |}, with |N s t | the number of daily news items. The model outputs
a binary prediction ˆys t ∈ {0,1}together with a human-readable explanation ˆes t . The parameters
θ are trained by empirical risk minimization with a task-appropriate loss such as cross-entropy:
minθ E(X s t ,Y s t )

ℓ(Fθ(f(X s t )), Ys t )  .
D DETAILS OFMULTIPLEAGENTS INF 2AGENT
Market Analysis Agent.The Market Analysis Agent is tasked with encoding raw OHLCV (Open,
High, Low, Close, V olume) sequences into high-level latent representations. We treat this data as a
15

Table 4: Notation table for the multimodal fusion module.
Symbol Description
MNumber of modalities (and modality-specific agents).
m, nModality indices,m, n∈ {1, . . . , M}.
x={X (m)}M m=1 Multimodal input;X (m) is the input sequence of modalitym.
X (m) Modality-m input sequence (e.g., over a window of trading days or
tokens).
fm(·)Modality-specific agent/encoder for modalitym.
Tm Sequence length for agentm(time steps or tokens).
˜dm Hidden dimension of agentmbefore projection.
Hm(x)∈R Tm× ˜dm Sequence representation produced by agentm.
ϕm(·) Pooling operator that maps Hm(x) to a fixed-length summary (last-
token for LLMs;[CLS]for Transformer encoders).
hm(x)∈R ˜dm Fixed-length summary of modalitymafter pooling.
dShared embedding dimension after projection/alignment.
Pm ∈R d× ˜dm Learnable projection mapping hm(x) to the shared d-dimensional
space.
em ∈R d Aligned modality embedding used for fusion.
Qm, Km, Vm Modality-specific query, key, and value representations derived from
em.
˜Km, ˜Vm Key/value after modality bias injection.
αm, α′ m Modality attention weights forx and perturbed input x′, respectively.
Rfinal Fused representation produced by modality attention.
rm Learnable modality-specific bias vector injected into key/value.
AShared modality space used to parameterize{r m}.
um Projection direction (modality-specific) used to generate rm =
umA.
s(x)∈R C Predicted logits from the classification head for inputx.
CNumber of classes (logit dimension).
ˆp(x) = softmax(s(x))Predicted class probability vector.
y∈ {0,1}C One-hot ground-truth label.
LCE Cross-entropy loss for supervised learning.
Lmodality Modality regularizer encouraging diversity of {rm} and preventing
trivial scaling.
m⋆ Index of the perturbed modality in robust training.
x′ Perturbed input obtained by corrupting/modifying modalitym ⋆.
Lrobust Robust training loss (logit consistency + attention suppression).
γWeight for the attention suppression term inL robust.
λmod, λrob Loss weights forL modality andL robust in the overall objective.
∥ · ∥2 ℓ2 norm;∥v∥ 2 2 = P i v2 i .
16

multivariate time series characterized by non-stationary volatility, where predictive cues often emerge
from the non-linear coupling between price movements and trading volume, known as volume-price
divergence Cont (2001). The core advantage lies in its self-attention mechanism, which provides a
global receptive field to capture long-range temporal dependencies and effectively model the intricate
lead-lag relationships within the lookback window Zerveas et al. (2021). This allows the agent
to dynamically prioritize critical market events regardless of their temporal distance, generating
robust embeddings optimized for downstream multimodal fusion. For a stock s at predictions
date t, we construct a T -day window XMA s,t = [x MA s,t−T , . . . , xMA s,t−1]∈R T×F MA, where contains
{open, high, low, ad j_close, volume}fields. Here T is the window length and FMA is the market
feature dimension.
Transformer-based Market Encoder. Let dMA denote the model dimension. We first project the input
features into a hidden sequence with positional encoding, H(0) MA = PE(X MA s,t )W E MA ∈R T×d MA,
where WE MA ∈R FMA×dMA is learnable. We then apply LMA causal Transformer blocks with a
causal maskM causal to prevent information leakage:
H(ℓ) MA = FFN  MHA  H(ℓ−1) MA ;M causal  .(12)
We expose the final hidden state sequence HMA s,t =H (LMA) MA ∈R T×d MA as the market modality
representation, ℓ= 1, . . . , LMA. Following the implementation, we use the [CLS] representation
as a fixed-length summary hMA s,t ∈R dMA when a vector representation is required. The subsequent
projection into the shared fusion space is performed by the fusion module (Eq. 5).
Technical Analysis Agent.The technical analysis agent focuses on expression-based alpha fac-
tors Kakushadze (2016). Compared with purely statistical features, such indicators provide structured
quantitative descriptions of trend, momentum, and volatility, which are complementary to news and
sentiment signals in multimodal trading. For a stock s at prediction date t, we assemble a window
of technical features from the past T trading days, XTA s,t = [xTA s,t−T , . . . , xTA s,t−1]∈R T×F T A. Each
xTA s,τ ∈R FT Acontains indicators such as MACD, RSI, and other engineered alpha factors.
Transformer-based Technical Encoder.To capture non-linear interactions among technical indicators
and their temporal dependencies within the window, we adopt a Transformer encoder with model
dimension dTA. We first embed the input as H(0) = PE(XTA s,t )W E TA ∈R T×d T A, where WE TA ∈
RFT A×dT Ais learnable and PE(·) denotes positional encoding. The encoder stacks L blocks of causal
multi-head self-attention followed by a position-wise feed-forward network:
H(ℓ) T A= FFN  MHA  H(ℓ−1) T A ;M causal  ,(13)
where Mcausal masks future positions to information leakage, ℓ= 1, . . . , LTA. For attention head
h∈ {1, . . . , H}in layer ℓ, we compute Q(ℓ,h) =H (ℓ−1)WQ ℓ,h, K(ℓ,h) =H (ℓ−1)WK ℓ,h, and
V(ℓ,h) =H (ℓ−1)WV ℓ,h, and apply masked attention:
Attn(ℓ,h) = softmax  Q(ℓ,h)(K(ℓ,h))⊤ √dk +M causal  V(ℓ,h),(14)
where dk is the per-head key dimension. The multi-head outputs are concatenated and linearly
projected following the standard Transformer formulation. We follow the same fusion interface as
market analysis agent, exposing HTA s,t and the optional [CLS] summary hTA s,t , then alignment is
performed by Eq. 5.
Sentiment Analysis Agent.The sentiment analysis agent processes financial news and social
media signals to capture sentiment information that may influence market dynamics. We adopt
DeepSeek-R1 Huang & Wang (2025) as the backbone model.
Tool-augmented News Retrieval.Given a stock ticker s and date t, the agent can autonomously re-
trieve raw news articles on demand by calling external news download APIs (e.g., Alpaca News API
and Alpha Vantage News API), conditioned on(s, t). The retrieved articles are deduplicated and sum-
marized by the News Summarizer (integrated in sentiment analysis agent as a tool) (Fig. 9), yielding
Ks,t summarized items. We denote the resulting sentiment input asX SA s,t ={n s,t,1, . . . , ns,t,Ks,t }.
Per-item Sentiment Inference. For each summary ns,t,j, the agent predicts a binary sentiment label
and a brief rationale. We denote the label by ˆcs,t,j ∈ {0,1}(1 for positive and 0 for negative) and the
rationale byˆqs,t,j:
17

(ˆcs,t,j,ˆqs,t,j) =g SA(ns,t,j),(15)
whereg SA(·)is instantiated by DeepSeek-R1,j= 1, . . . , Ks,t.
Hidden Representation for Fusion. Beyond discrete labels, we extract a continuous representation
from the last-layer hidden states of the LLM. Let HSA s,t,j ∈R Ls,t,j ×dSA denote the last-layer hidden
states produced when encoding ns,t,j, where Ls,t,j is the token length and dSA is the hidden dimen-
sion. Using last-token pooling, we obtain us,t,j =H SA s,t,j(Ls,t,j)∈R dSA and aggregate across items
to form a fixed-length summary:
hSA s,t = 1 Ks,t
Ks,tX
j=1
us,t,j ∈R dSA .(16)
The fusion module then applies its projection step (Eq. 5) to maph SA s,t into the shared fusion space.
News Analysis Agent.As illustrated in Fig. 1, the news analysis agent serves two objectives. First,
it retrieves and consolidates news evidence relevant to a queried stock-date pair (s, t). Second, it
produces transparent, human-readable explanations to support downstream prediction. Given a ticker
s and date t, the agent retrieves raw articles from external news APIs, including the Alpaca News API
(financial news with ticker annotations) and the New York Times API (general news). The retrieved
articles are deduplicated and condensed by the News Summarizer (Fig. 9), yielding a set of top-Ks,t
summarized items, XNA s,t ={n s,t,1, . . . , ns,t,Ks,t }, which serves as the textual input to the news
analysis agent.
Sentiment Analysis
Input: Summarized news supplied by News Summarizer.
Prompt: You are a financial sentiment classifier. You will receive a summary of news items for the last 5
trading days about a stock. Classify the overall sentiment as POSITIVE or NEGATIVE for the stock. Only
return one word: POSITIVE or NEGATIVE."
Response
Prediction: Negative.
Analysis: Alright, I need to determine whether the overall sentiment for
Apple Inc. (AAPL) based on the news summaries from the past five trading
days is positive or negative. First, let's look at each day's news:**Day 1:**
Apple's shares hit a new 52-week low due to concerns about iPhone sales.
This is a negative point ...**Day 2:** ...**Day 3:** ... **Day 4:** ... **Day 5:** ...
Therefore, the overall sentiment seems negative.
News Analysis
Input: Summarized news supplied by News Summarizer and historical data.
Prompt: Predict the next day AAPL stock movement given its following information:
News for the past 5 days: News on Day 1: Apple Inc. NASDAQ AAPL shares fell to another 52week
low ... News on Day 5: What 15 Analyst Ratings Have To Say About Apple...
The following is the information about the stock price and technical indicators:
close: Day 1: 128.54, Day 2: 124.59, ..., Day 5: 123.63, RSI: Day 1: 67.37, Day 2: 62.43, ..., Day 5: 41.32,
MACD: Day 1: -2.83, Day 2: -3.28, ..., Day 5: -2.87, Signal: Day 1: -2.36, Day 2: -2.54, ..., Day 5: -2.66,
Output in the following format: Analysis: <concise analysis> Signal: UP/DOWN.
Qwen2.5
Response
Prediction: Down.
Analysis: The recent news indicates a challenging environment for Apple
due to supply chain concerns and broader market weakness, particularly
after a significant decline at the start of December. This sentiment is
reflected in the stock's price movements, which show a downward trend
over the last five days, culminating in a close below 125, indicating bearish
momentum. Additionally, the RSI ...
Figure 8: Case studies of our stock prediction system, we only display partial prompt for brevity.
Explanation Prompting. Conditioned on (s, t)and the summarized news setXNA s,t , the news reasoning
model gNA(·) generates (i) an auxiliary directional signal ˆcNA s,t ∈ {UP,DOWN}, (ii) a confidence
scoreˆpNA s,t ∈[0,1], and (iii) a natural-language explanationˆe NA s,t :
(ˆcNA s,t ,ˆpNA s,t ,ˆeNA s,t ) =g NA  s, t,XNA s,t  ,(17)
whereg NA(·)is instantiated by the backbone LLM used in F 2Agent.
Model Fine-tuning. Following previous works that utilizes Chain of Thought(CoT) Wei et al. (2022),
we use a similar two-step process to fine-tune a LLM (see Fig. 3). During the training, we use the
binary evaluations to choose the better response (see Fig. 3). In the first step, we collect the QA
pairs related to selected topics (e.g. “trading decisions under different cases”, “momentum strategy
and mean-reverse strategy”, etc.), which are generated with GPT-4o-mini Hurst et al. (2024). In
the second step, we collect the real application simulated QA pairs with GPT-4o-mini, which are
designed to simulate real application of the stock prediction system. Specifically, we fine-tune the
model by minimizing following combined loss:
LNA(θ) =−E (P,Y,y)∼D NA
h
logP θ(Y | P) +λ
CX
k=1
yk logP θ(k| P)
i
,(18)
where P denotes the instruction prompt and Y is the target response. The first term corresponds to
the language modeling loss (lm_loss), i.e., the negative log-likelihood of generating Y conditioned
on P. The second term corresponds to the auxiliary classification cross-entropy loss ( cls_loss),
where y∈ {0,1}C is the one-hot label (e.g., UP/DOWN) and λ weights the classification objective.
To mitigate majority-class bias, prompts require choosing a signal from {UP,DOWN} Zhao et al.
18

(2021). Our prompt format (see Table 6, 5, 7) and interactive trajectory (see Fig. 8) draw inspiration
from FinMEM Yu et al. (2025), while the execution is performed in a single summarization-reasoning
step.
Beyond the textual explanation, we extract a fixed-length representation from the last-layer hidden
states of the LLM and expose it to the fusion module. Let HNA s,t ∈R Ls,t×dNA denote the last-layer
hidden states when encoding the prompt constructed from (s, t,XNA s,t ), where Ls,t is the token length
and dNA is the hidden dimension. We apply last-token pooling to obtain hNA s,t ∈R dNA, which
corresponds to the agent summary hm(x) used in Eq. 5 (with m= NA ). The fusion module then
applies its projection step in Eq. 5 to maph NA s,t into the shared fusion space.
Table 5: Prompt template and filled example for the News Analysis Agent (Part II).
Field Content
Illustrative outputAnalysis: The recent news indicates strong positive momentum for Apple
(AAPL) following its Q4 earnings report, which showed record-breaking
results and strong guidance for the upcoming quarter. Analysts have
raised their price targets and forecast continued growth. Additionally,
the stock has been hitting new all-time highs and setting records,
indicating strong investor confidence. Technical indicators such as RSI
and MACD also suggest upward momentum.
Signal: UP
Purpose of example This example illustrates the 5-day input/output interface used by the News Analysis Agent in the paper: the
model jointly uses summarized news and technical indicators, produces a concise rationale, and outputs a
binary directional signal constrained toUP/DOWN.
19

Table 6: Prompt template and filled example for the News Analysis Agent (Part I).
Field Content
Task Predict the next-day stock movement for a given asset using recent summarized news and recent
price/technical indicators.
Asset AAPL
Reference date 2025-11-03
Example type Adapted from the logged AAPL news-analysis case on 2025-11-03, following the 5-day prompt template used
in the paper.
System instructionYou are a financial analyst. Analyze the historical news and market
data and provide a clear signal with concise reasoning.
User instructionPredict the next-day AAPL stock movement given the following
information.
News and Technical window Past 5 trading days
Output formatAnalysis: <concise analysis>
Signal: UP/DOWN
Filled input promptPredict the next-day AAPL stock movement given the following
information:
News for the past 5 days:
News on Day 1: Apple trades steady as BofA’s Mohan boosts iPhone 17
unit forecasts, raises price target, and models stronger long-term
revenue and margins.; Earnings Preview For Apple; Two Nvidia Shockers.
News on Day 2: Apple reports financial results for the fourth quarter
on Thursday after the close. Here’s a rundown of the iPhone maker’s
report.; Apple Inc. AAPL will release earnings results on 10/30.
Analysts expect earnings of 1.77 per share and quarterly revenue of
102.17 billion.; U.S. stock futures mixed, Amazon, Alphabet, and
Microsoft beat earnings expectations, while Apple and Meta post upbeat
results.
News on Day 3: Apple stock hit new all-time highs Friday after
reporting fourth-quarter results Thursday. The company is guiding for
the first quarter to be even better and record-breaking.; Apple’s
blockbuster fourth-quarter results prompted bullish reactions across
Wall Street, with Wedbush’s Dan Ives calling it a pound-the-table
moment, CNBC’s Jim Cramer saying Apple bears owe us an explanation, and
Gene Munster highlighting stronger iPhone demand and a solid holiday
outlook.; Nasdaq Surges Over 1 Apple Earnings Top Views.
News on Day 4: Apple, Amazon, Microsoft, and Alphabet beat Q3 estimates
with revenue and earnings growth. Trump and Xi conclude high-stakes
meeting with trade, soybean, and resource agreements, potentially
impacting U.S.-China economic relations and global markets.; As 2026
approaches, Apple is gearing up for a critical year filled with
significant product launches and potential executive changes, all while
grappling with regulatory and tariff-related challenges.; Apple breaks
records in Q4 and ad revenue, Samsung teases iPhone users, and Jamie
Dimon echoes Steve Jobs on office meetings.
News on Day 5: CNN Money Fear and Greed index remained in Fear zone on
Friday. U.S. stocks closed higher, Nasdaq up 4.7 in October. Amazon
reported earnings.; The weekend saw major tech milestones as Nvidia hit
a 5 trillion valuation, Apple set iPhone upgrade records, Netflix eyed
Warner Bros. Discovery, Meta doubled down on smart glasses, and OpenAI
prepared for a potential 1 trillion IPO.; 10 Information Technology
Stocks With Whale Alerts In Today’s Session.
Stock market data for the past 5 trading days: The following is the
information about the stock price and technical indicators:
close: Day 1: 268.74, Day 2: 269.44, Day 3: 271.14, Day 4: 270.11,
Day 5: 268.79.
RSI: Day 1: 33.90, Day 2: 34.25, Day 3: 100.00, Day 4: 69.65, Day 5:
64.61.
MACD: Day 1: 3.79, Day 2: 3.97, Day 3: 4.12, Day 4: 3.90, Day 5:
3.42.
Signal: Day 1: 2.24, Day 2: 2.58, Day 3: 2.89, Day 4: 3.09, Day 5:
3.16.
Output in the following format:
Analysis: <concise analysis>
Signal: UP/DOWN
Note: You MUST output either UP or DOWN. NEUTRAL is NOT allowed.
20

Table 7: Prompt template and one filled example for the Sentiment Analysis Agent.
Field Content
Task Classify the overall sentiment of the past 5-day news summaries for a stock asPOSITIVEorNEGATIVE.
Asset AAPL
Reference date 2025-11-03
Example type Adapted from the logged AAPL sentiment case on 2025-11-03, following the 5-day prompt template used in
the paper.
System instructionYou are a financial sentiment classifier. You will receive a summary of
news items for the last 5 days about a stock. Classify the overall
sentiment as POSITIVE or NEGATIVE for the stock. Only return one word:
POSITIVE or NEGATIVE.
User instructionSymbol: AAPL
News for the past 5 days:
News window Past 5 days
Output constraint Only one word is allowed:POSITIVEorNEGATIVE.
Filled input prompt<|im_start|>system
You are a financial sentiment classifier. You will receive a summary of
news items for the last 5 days about a stock. Classify the overall
sentiment as POSITIVE or NEGATIVE for the stock. Only return one word:
POSITIVE or NEGATIVE.
<|im_end|>
<|im_start|>user
Symbol: AAPL
News for the past 5 days:
News on Day 1: Apple reports Q4 results on Thursday with a key first
look at iPhone 17 demand. Here’s what experts are saying ahead of the
report.; Analysts expect steady gains for Amazon, Apple, and Microsoft
in Q3, driven by cloud, advertising, and retail performance. Price
targets range from 280 to 625.; Big Nuclear Deal
News on Day 2: Apple trades steady as BofA’s Mohan boosts iPhone 17
unit forecasts, raises price target, and models stronger long-term
revenue and margins.; Earnings Preview For Apple; Two Nvidia Shockers
News on Day 3: Apple reports financial results for the fourth quarter
on Thursday after the close. Here’s a rundown of the iPhone maker’s
report.; Apple Inc. AAPL will release earnings results on 10/30.
Analysts expect earnings of 1.77 per share and quarterly revenue of
102.17 billion.; U.S. stock futures mixed, Amazon, Alphabet, and
Microsoft beat earnings expectations, while Apple and Meta post upbeat
results.
News on Day 4: Apple stock hit new all-time highs Friday after
reporting fourth-quarter results Thursday. The company is guiding for
the first quarter to be even better and record-breaking.; Apple’s
blockbuster fourth-quarter results prompted bullish reactions across
Wall Street, with Wedbush’s Dan Ives calling it a pound-the-table
moment, CNBC’s Jim Cramer saying Apple bears owe us an explanation, and
Gene Munster highlighting stronger iPhone demand and a solid holiday
outlook.; Nasdaq Surges Over 1 Apple Earnings Top Views
News on Day 5: Apple, Amazon, Microsoft, and Alphabet beat Q3 estimates
with revenue and earnings growth. Trump and Xi conclude high-stakes
meeting with trade, soybean, and resource agreements, potentially
impacting U.S.-China economic relations and global markets.; As 2026
approaches, Apple is gearing up for a critical year filled with
significant product launches and potential executive changes, all while
grappling with regulatory and tariff-related challenges.; Apple breaks
records in Q4 and ad revenue, Samsung teases iPhone users, and Jamie
Dimon echoes Steve Jobs on office meetings.
<|im_end|>
<|im_start|>assistant
ReasoningAlright, let’s analyze the news for the past five days regarding Apple
(AAPL).
Starting with Day 1, Apple is expected to report strong Q4 results,
especially regarding iPhone 17 demand. Experts are optimistic about
their performance.
On Day 2, there’s positive news as BofA analyst Mohan boosts his iPhone
17 forecast and increases the price target, suggesting strength in the
stock.
Day 3 mentions that Apple is set to release earnings, with analysts
expecting $1.77 per share and $102.17 billion in revenue. That’s
already a positive indicator.
By Day 4, Apple hits new all-time highs after reporting strong Q4
results. Analysts like Dan Ives and Jim Cramer are bullish, and the
company guides for an even better first quarter.
Looking at Day 5, Apple, along with other big tech companies, beats Q3
estimates. This shows consistent growth and positive momentum.
Overall, most news points toward positive developments for Apple--strong
earnings, increased forecasts, stock highs, and positive market
reactions. There doesn’t seem to be any major negative news affecting
the stock in this period.
Final labelPOSITIVE
Purpose of example This example illustrates the input/output interface of the Sentiment Analysis Agent under the 5-day setting
used in the paper: the model receives a news summary block together with a fixed role instruction, produces a
free-form reasoning trace, and finally outputs a single-word polarity label constrained to
POSITIVE/NEGATIVE.
21

E DETAILS OFF 2AGENTDESIGN
E.1 NEWSSUMMARIZER
News Summarizer
General News (GN)
GN = {GN1, GN2, ...,  GNN}
Extracted Ratings (R)
R = {R1, R2, ...,  RN}
Selected News
SN = {SN1, SN2, SN3} Filter rating
Ri ≥ 5 & sort
Figure 9: Illustration of News Summarizer.
The News Summarizer, depicted in Fig. 9, comprises three main components: a news extractor, a
news evaluator, and a SQLite cache database. For news extraction, we utilize two distinct sources:
the Alpaca News API, which provides financial news explicitly labeled by stock tickers, and the
New York Times API, which offers broader news content without explicit ticker annotations. We
directly query Alpaca News using stock symbols due to its inherent labeling. Conversely, for news
retrieval from the New York Times API, we employ semantic vector search, matching embeddings of
stock-related keywords against embeddings of news articles. To enhance efficiency and minimize
redundant API requests, the retrieved and summarized news data are stored in an SQLite cache
database. As shown in Fig. 1, when the system receives a query for a specific date and stock ticker, it
first checks the cache database. If the corresponding news summary exists, it is retrieved directly
from the cache; otherwise, relevant news articles are fetched through the APIs, summarized by the
summarization model, and then saved into the cache database.
Regarding the summarization process, we perform evaluations on multiple advanced summarization
models, including LLaMA-3 Grattafiori et al. (2024) and DeepSeek-R1 Rehman et al. (2025); Huang
& Wang (2025), to determine the most effective summarization approach. After retrieving all news
items for a given day, we further prompt DeepSeek-R1 to rate each article according to its potential
impact on the target stock. Based on these ratings, only the top three articles above a defined threshold
are retained. The chosen summarization model then condenses these selected articles into concise,
high-correlation summaries, ensuring that the final outputs capture the most influential news signals.
E.2 MODALITYPROCESSINGMODULE
Our proposed framework consists of four specialized agents designed to extract latent features from
distinct data modalities: market data, technical indicators, news text, and sentiment signals. Each
agent employs a specific architecture tailored to the nature of its input data.
Market Analysis Agent.The market analysis agent encodes historical OHLCV observations to
capture temporal dependencies in market dynamics. For stock s at date t, its input is a lookback
window XMA s,t ∈R T×F MA constructed from standard fields (Open, High, Low, Close, V olume)
collected from data providers such as Yahoo Finance and Alpha Vantage APIs. We employ a
Transformer-based encoder to produce latent market representations, exposing the sequence hidden
statesH MA s,t and a fixed-length summaryh MA s,t for downstream fusion (cf. Eq. 5).
Technical Analysis Agent.The technical analysis agent encodes expression-based alpha factors
derived from technical indicators. For stock s at date t, we construct a technical feature window
XTA s,t ∈R T×F T A, which includes indicators such as MACD, SMA, and Z-score mean reversion
(ZMR) Nti et al. (2020). We employ a Transformer-based encoder to model the temporal structure
of these indicators and their non-linear interactions, producing latent technical representations.
Following the same fusion interface, we expose the hidden states HTA s,t and a fixed-length summary
hTA s,t for downstream fusion (cf. Eq. 5).
News Analysis Agent.The news analysis agent extracts semantic evidence and trading-relevant
implications from unstructured financial text retrieved from news providers (e.g., Bloomberg and
22

Alpaca news APIs). We leverage Qwen2.5-7B-Instruct Team et al. (2024); Yang et al. (2025), which
is fine-tuned on financial corpora, to perform news reasoning conditioned on the queried stock-date
context(s, t). Given a set of summarized news itemsXNA s,t , the agent generates an auxiliary trading
signal (e.g., UP/DOWN) together with a natural-language reasoning chain. In addition, we extract a
fixed-length latent representation hNA s,t from the LLM hidden states, which is subsequently projected
by the fusion module (Eq. 5) and used as the news modality input for downstream fusion.
Sentiment Analysis Agent.The Sentiment Analysis Agent assesses market sentiment by analyzing
news and social media streams (e.g., FinHub). Given a stock s and date t, it constructs a set of
summarized textual items XSA s,t ={n s,t,1, . . . , ns,t,Ks,t } and uses DeepSeek-R1 Guo et al. (2025) to
perform binary sentiment classification (positive/negative) for each item. Beyond discrete polarity,
the agent extracts a fixed-length latent representation hSA s,t from the LLM hidden states, which is
subsequently projected by the fusion module (Eq. 5) and serves as a complementary signal to the
news analysis component.
E.3 BACKTESTINGENGINE
The Backtesting Tool takes the predictions produced by F2Agent and transforms them into bullish or
bearish trading decisions. First, the predicted signals and actual market prices from earlier modules
are loaded. Based on these inputs, customized trading strategies are applied to generate buy, hold, or
sell actions. The resulting trading signals are then backtested on historical market data with specified
stock tickers, simulating how the strategy would have performed in practice. Finally, the module
outputs comprehensive evaluation results, including equity curves, risk–return plots, and standard
performance metrics such as cumulative return, annualized return, Sharpe ratio, and maximum
drawdown.
HOLD signals in binary price prediction.The key distinction is between the binary price-
direction label used for supervised learning and the downstream trading action in the backtest-
ing. In our formulation, {UP,DOWN} is the supervised prediction target defined directly from
the adjusted closing price: following Eq. 2, Yt = 1 if pc t ≥p c t−1, and Yt = 0 otherwise.
Table 8: Mapping from consecutive predicted sig-
nals to execution actions.
Signal attSignal att+ 1 Execution action
BUY BUY Hold the position
BUY SELL Sell / liquidate
SELL BUY Buy / enter position
SELL SELL Stay in cash
Therefore, ano price changecase is grouped
into the UP class by definition, and we do not in-
troduce a separate HOLD class at the label level.
The notion of HOLD appears only in the back-
testing/execution stage, where consecutive pre-
dicted signals are translated into buy/sell/hold
actions, as shown in Table 8. Thus, HOLD is an
execution-state outcome induced by consecutive
predicted signals, rather than a third class in the
binary price-direction prediction task.
Assumptions used in the backtesting setup.Details of the backtesting protocol are specified below.
Our experiments use a daily, low-frequency, long-or-flat backtesting setting. A signal generated
on day t is executed on day t+ 1 , which avoids look-ahead bias. Positions are implemented using
integer shares, with shares=⌊cash/price⌋ , and any remaining capital is kept as cash. When the
signal changes from positive to non-positive, the position is fully liquidated. Thus, the setup is not
long-short and does not involve short borrowing constraints. We apply a uniform transaction cost
of 0.003 to all methods. We do not impose an explicit turnover cap, nor explicitly model slippage
or market impact, following common practice in prior work Zhang et al. (2024b); Yu et al. (2024).
These factors are not the primary focus of this study, which targets prediction performance under
a shared and consistent backtesting engine. To mitigate their potential impact, we evaluate at daily
frequency on highly liquid assets, where such effects are typically reduced.
F DETAILS OFCOMPARISON WITHBASELINES
F.1 IMPLEMENTATIONDETAILS
To ensure reproducibility, all experiments are conducted on NVIDIA A40 GPUs using PyTorch and
HuggingFace Transformers. We adopt a unified optimization strategy for gradient-based models
(LSTM, Transformer, and F2Agent’s fusion module) and RL agents, utilizing the Adam optimizer
23

with a learning rate of 2×10 −3, a batch size of 64, and a 30-day look-back window, with training
capped at 100 epochs under early stopping (patience=10). Specific hyperparameters include a
discount factor of γ= 0.99 for RL agents (with a 10,000-step buffer for DQN and ϵ= 0.2 for PPO)
and a generation temperature of 0.5 with a repetition penalty of 1.1 for all LLM components. To
strictly prevent look-ahead bias, data is chronologically split into training (2023-10-01–2024-09-30),
validation (2024-10-01–2025-03-31), and testing (2025-04-01–2025-09-30) periods.
F.2 MODALITYDEFINITIONS
Specifically, these modalities include: i)Asset Priceat the day-level, covering open, high, low, adj
close, and volume. ii)Refined Alphasrefer to a compact collection of high-signal technical indicators
identified through preliminary feature-selection analysis. iii)Asset newscoverage with daily updates
from various esteemed sources such as New York Times API and Alpaca API, ensuring a diverse and
thorough perspective on the financial markets. iv)Summarized Daily Newsupdated daily via the
Alpaca News API by news summarizer, ensuring broad and in-depth coverage of financial market
information Yu et al. (2025).
F.3 FORMULATIONS OFUSEDMETRICS
Cumulative Return (CR)measures the total value change of an investment over time by summing
daily logarithmic returns, shown in Equation 19. Higher values indicate better strategy effectiveness:
CR=
nX
t=1
ri =
nX
t=1

ln
 pt+1
pt

·action t

.(19)
Annual Rate of Return (ARR)normalizes the cumulative return over one year:
ARR=
  Vend
Vstart
 C
T
−1
!
×100%.(20)
Sharpe Ratio (SR)assesses risk-adjusted returns by dividing the average excess return ( Rp) over
the risk-free rate ( Rf ) by its volatility ( σp), detailed in Equation 21. Higher ratios signify better
performance.
SR= Rp −R f
σp
.(21)
Maximum Drawdown (MDD)calculates the largest portfolio value drop from peak to trough, as
given in Equation 22. Lower values indicate lesser risk and higher strategy robustness.
MDD=max( Ppeak −P trough
Ppeak
).(22)
F.4 DETAILS OFBASELINES
We compare the trading performance of F 2Agent against four widely used rule-based strategies
(B&H,MACD,ZMR,SMA), two ML&DL-based price prediction models, two canonical RL-based
agents, four general-purpose LLMs, and four financial-domain LLM agents. The ML&DL models
compriseLSTMYang et al. (2020) andTransformerYang et al. (2020). The RL-based agents
includeDQNMnih et al. (2013) andPPOSchulman et al. (2017). The general LLM baselines
areQwen3-8B,DeepSeek-R1-0528,Llama4-Scout-17B, andGPT-5-mini. The financial LLM
baselines includeFinGPTLiu et al. (2023),FinAgent,TradingAgentsXiao et al. (2024), and
DeepFund. Below we briefly describe each baseline:
Rule-based Methods.We select representative traditional strategies:Buy-and-Hold (B&H)holds
the asset throughout the evaluation horizon, ignoring short-term fluctuations.MACDgenerates
signals from MACD–signal line crossovers to capture trend momentum.Z-score Mean Reversion
(ZMR)assumes prices revert to a statistical mean, with entries/exits determined by Z-score thresholds.
SMAtrades based on moving-average levels and crossovers to reflect smoothed trend direction.
ML & DL-based Models.We employ sequential modeling baselines:LSTMYang et al. (2020)
models sequential dependencies with gated memory to improve next-step price forecasting.Trans-
formerYang et al. (2020) leverages self-attention to capture long-range temporal interactions for
price prediction.
24

RL-based Methods.We utilize standard reinforcement learning algorithms:DQNMnih et al.
(2013) approximates the action-value function with deep networks to select trades from market states.
PPOSchulman et al. (2017) optimizes a clipped surrogate objective to update policies stably and
sample-efficiently.
General LLMs.We include strong general LLMs as generic text-driven trading agents:Qwen3-8B,
DeepSeek-R1-0528,Llama4-Scout-17B, andGPT-5-miniare prompted to infer directional signals
from the same textual inputs (e.g., news summaries) and to produce trading decisions under a unified
prompting and execution protocol.
Financial LLMs.We compare against LLMs and agent systems specialized for financial tasks
(introduced in chronological order):FinGPTLiu et al. (2023) is an open-source framework converting
financial news and price information into trading decisions.FinAgentZhang et al. (2024b) is a
finance-oriented LLM agent designed to perform market reasoning and decision making with domain-
specific instructions and tools.TradingAgentsXiao et al. (2024) is a multi-agent LLM framework
designed for automated trading decision making.DeepFundLi et al. (2025) is a recent finance-
focused LLM agent that integrates market information and textual evidence for fund-style trading
decisions.
F.5 FULLEXPERIMENTALRESULTS OFSTOCKSMENTIONED INPAPER
We summarize the quantitative results in Table 10, evaluating profitability and risk across four key
metrics: CR, ARR, SR, and MDD. F2Agent establishes a new state-of-the-art by achieving the highest
cumulative returns across all six evaluated assets. On high-volatility assets, the system demonstrates
exceptional profitability, securing a 74.21% return on TSLA and 38.90% on BTCUSD, significantly
outperforming the Buy-and-Hold benchmark (65.64% and 31.78%, respectively). Furthermore, on
stable tech giants, F2Agent generates substantial alpha where other methods struggle. For instance,
on AAPL, while the market yielded only 13.97% and the closest competitor (DeepFund) reached
16.91%, our system delivered a remarkable 25.04%, translating to a relative improvement of 48.08%.
This consistent dominance validates that the multi-agent fusion mechanism successfully captures
long-term appreciation trends that single-modality agents often miss.
Figure 10 further illustrates the cumulative return trajectories on representative assets. On AAPL and
AMZN, F2Agent establishes an early advantage and maintains stable return accumulation over most
of the test horizon. On BTCUSD, where all methods exhibit larger fluctuations, F 2Agent remains
among the strongest performers while avoiding the severe reversals observed in several baselines.
This suggests that the proposed multimodal agentic design improves not only final profitability but
also temporal robustness under different market conditions.
Figure 10: Performance comparison on cumulative return over time between F 2Agent and other
benchmarks across all assets.
25

Table 9: Performance comparison across four metrics on six assets. Top block reports results for
AAPL, AMZN, and GOOG; Bottom block reports results for MSFT, TSLA, and BTCUSD. Best,
second, and third results are marked by bold-underlined,bold, and underlined text, respectively.
CR: Cumulative Return; ARR: Annualized Return; SR: Sharpe Ratio; MDD: Maximum Drawdown.
TheImprovementrow reports the relative gain of F 2Agent over the best-performing baseline.
Category Model AAPL AMZN GOOG
CR%↑ARR%↑SR↑MDD%↓CR%↑ARR%↑SR↑MDD%↓CR%↑ARR%↑SR↑MDD%↓
Market B&H 13.97 27.95 0.61 22.99 14.26 28.51 0.63 14.64 53.19 106.38 1.98 7.98
Rule-based
MACD -11.24 -22.48 -0.73 17.46 -16.72 -33.43 -0.94 19.25 15.40 30.80 0.94 12.06
ZMR 7.89 15.79 0.96 4.06 -3.54 -7.08 -0.974.16 3.99 7.99 1.261.03
SMA 8.85 17.70 0.865.42-4.47 -8.93 -0.49 7.36 37.71 75.422.158.94
ML/DL LSTM -3.73 -7.46 -0.02 22.99 1.13 2.26 0.16 14.64 30.44 60.88 1.52 7.74 Transformer 16.45 32.90 0.72 13.77 6.30 12.60 0.38 14.64 53.92 107.85 2.12 8.32
RL DQN 16.04 32.071.0612.18 9.57 19.14 0.72 9.84 -5.77 -11.54 -0.47 13.77 PPO 13.60 27.20 0.68 9.4814.52 29.030.70 12.93 21.87 43.73 1.14 7.98
General LLMs
Qwen3-8B 3.67 7.34 0.27 18.95 2.56 5.12 0.23 19.52 24.85 49.70 1.43 10.97
DeepSeek-R1 2.01 4.02 0.20 13.42 8.40 16.80 0.51 19.41 34.20 68.40 1.67 9.90
Llama4-Scout 12.12 24.23 0.58 18.95 -10.23 -20.46 -0.39 22.50 39.84 79.69 1.87 9.96
GPT5-mini -9.44 -18.88 -0.42 25.83 -2.64 -5.27 -0.06 18.01 11.92 23.85 0.74 9.59
Financial LLMs
FinGPT -3.92 -7.85 -0.06 26.25 13.89 27.780.868.53 32.99 65.99 1.40 9.26
FinAgent 16.88 33.77 0.90 13.16 12.38 24.76 0.57 14.6354.08 108.162.00 7.98
TradingAgents -4.29 -8.58 -0.09 26.25 11.76 23.72 0.66 15.31 33.43 66.85 1.57 9.76
DeepFund16.91 33.830.74 15.86 7.20 14.41 0.43 16.70 27.06 54.13 1.40 12.86
Ours F 2Agent 25.04 50.08 1.22 7.83 20.44 40.87 1.18 5.5760.24 120.48 2.55 7.01
Improvement(%) 48.08 48.03 15.09 – 40.77 40.79 37.21 – 11.39 11.39 18.60 –
Category Model MSFT TSLA BTCUSD Avg Rank
CR%↑ARR%↑SR↑MDD%↓CR%↑ARR%↑SR↑MDD%↓CR%↑ARR%↑SR↑MDD%↓(ARR)
Market B&H 35.26 70.52 1.76 8.0365.64 131.281.32 21.54 31.78 43.76 1.27 11.70 3.50
Rule-based
MACD 6.80 13.61 0.67 6.79 25.74 51.48 0.94 17.29 21.73 29.92 1.40 8.29 13.67
ZMR 1.88 3.76 0.502.10 10.42 20.84 0.60 14.26 10.50 14.46 1.103.54 14.33
SMA 1.75 3.50 0.672.10 12.98 25.95 0.70 18.68 -6.00 -8.26 -0.51 13.91 13.17
ML/DL LSTM 29.13 58.26 1.55 8.03 9.57 19.13 0.42 21.53 18.94 26.09 1.00 9.07 11.17 Transformer 22.82 45.64 1.35 8.03 38.94 77.88 1.09 16.99 19.14 26.35 1.18 8.26 7.00
RL DQN 6.95 13.91 0.81 9.70 20.01 40.02 0.82 19.70 7.30 10.05 0.576.9711.83 PPO 19.27 38.54 1.51 7.55 17.34 34.68 0.80 20.10 17.60 24.24 0.89 11.59 9.33
General LLMs
Qwen3-8B 10.60 21.19 0.80 9.28 43.74 87.48 1.20 23.66 23.91 32.93 1.10 12.03 10.00
DeepSeek-R1 10.40 20.81 0.97 7.52 39.42 78.83 1.15 24.13 12.91 17.77 0.71 10.58 10.00
Llama4-Scout 15.95 31.90 1.19 9.73 51.55 103.09 1.34 21.24 25.72 35.42 1.15 13.98 8.33
GPT5-mini 19.60 39.21 1.63 7.55 52.58 105.17 1.55 19.44 11.68 16.08 0.71 12.39 11.50
Financial LLMs
FinGPT 13.26 26.52 0.98 10.03 47.17 94.35 1.20 21.54 25.75 35.46 1.20 11.28 8.17
FinAgent 34.93 69.872.19 8.02 58.44 116.87 1.24 24.4336.36 50.07 1.4714.82 3.17
TradingAgents 24.15 48.29 1.595.3125.90 51.80 0.93 22.64 28.29 38.96 1.37 8.74 8.17
DeepFund40.30 80.602.07 5.94 25.59 51.181.72 6.52 5.84 8.05 0.38 16.11 8.67
Ours F 2Agent 42.07 84.14 2.088.0374.21 148.41 1.94 12.60 38.90 53.57 1.52 9.791.00
Improvement(%) 4.39 4.39 – – 13.06 13.05 12.79 – 6.99 6.99 3.40 – –
Table 10: Performance comparison across four metrics on six assets. Top block reports results for
AAPL, AMZN, and GOOG; Bottom block reports results for MSFT, TSLA, and BTCUSD. Best,
second, and third results are marked by bold-underlined,bold, and underlined text, respectively.
CR: Cumulative Return; ARR: Annualized Return; SR: Sharpe Ratio; MDD: Maximum Drawdown.
Category Model AAPL AMZN GOOG
CR%↑ARR%↑SR↑MDD%↓CR%↑ARR%↑SR↑MDD%↓CR%↑ARR%↑SR↑MDD%↓
Market B&H 13.97 27.95 0.61 22.99 14.26 28.51 0.63 14.64 53.19 106.38 1.98 7.98
Rule-based
MACD -11.24 -22.48 -0.73 17.46 -16.72 -33.43 -0.94 19.25 15.40 30.80 0.94 12.06
ZMR 7.89 15.79 0.964.06 -3.54 -7.08 -0.974.16 3.99 7.99 1.261.03
SMA 8.85 17.70 0.865.42-4.47 -8.93 -0.49 7.36 37.71 75.42 2.15 8.94
ML/DL LSTM -3.73 -7.46 -0.02 22.99 1.13 2.26 0.16 14.64 30.44 60.88 1.52 7.74 Transformer 16.45 32.90 0.72 13.77 6.30 12.60 0.38 14.64 53.92 107.85 2.12 8.32
RL DQN 16.04 32.07 1.06 12.18 9.57 19.14 0.72 9.84 -5.77 -11.54 -0.47 13.77 PPO 13.60 27.20 0.68 9.48 14.52 29.03 0.70 12.93 21.87 43.73 1.14 7.98
General LLMs
Qwen3-8B 3.67 7.34 0.27 18.95 2.56 5.12 0.23 19.52 24.85 49.70 1.43 10.97
DeepSeek-R1 2.01 4.02 0.20 13.42 8.40 16.80 0.51 19.41 34.20 68.40 1.67 9.90
Llama4-Scout 12.12 24.23 0.58 18.95 -10.23 -20.46 -0.39 22.50 39.84 79.69 1.87 9.96
GPT5-mini -9.44 -18.88 -0.42 25.83 -2.64 -5.27 -0.06 18.01 11.92 23.85 0.74 9.59
Financial LLMs
FinGPT -3.92 -7.85 -0.06 26.25 13.89 27.78 0.86 8.53 32.99 65.99 1.40 9.26
FinAgent 16.88 33.77 0.90 13.16 12.38 24.76 0.57 14.6354.08 108.162.00 7.98
TradingAgents -4.29 -8.58 -0.09 26.25 11.76 23.72 0.66 15.31 33.43 66.85 1.57 9.76
DeepFund 16.91 33.83 0.74 15.86 7.20 14.41 0.43 16.70 27.06 54.13 1.40 12.86
F2Agent 25.04 50.08 1.227.8320.44 40.87 1.18 5.57 60.24 120.48 2.55 7.01
PMRL_Finance51.28 102.56 2.77 5.72 27.77 55.54 1.73 13.1064.07 127.80 2.397.98
Improvement(%) 48.08 48.03 15.09 – 40.77 40.79 37.21 – 11.39 11.39 18.60 –
26

Table 11: Classification performance comparison on AAPL, AMZN, and GOOG.
Method AAPL AMZN GOOG
ACC%↑MCC↑ACC%↑MCC↑ACC%↑MCC↑
F2Agent 50.00 0.0051 55.56 0.1055 54.76 0.0889
PMRL_Finance64.29 0.2843 56.35 0.1266 59.52 0.1682
Table 12: Ablation study on AAPL.
Method AAPL
ACC%↑MCC↑
F2Agent 50.00 0.0051
PMRL_Finance w/o robust 58.73 0.1686
PMRL_Finance64.29 0.2843
F.6 EXPERIMENTALRESULTS OFBROADERASSETPOOL ANDEXTENDEDTESTHORIZONS
To further examine the generalization capability of F2Agent, we extend the evaluation beyond the
main assets—Apple Inc. (AAPL, Technology, mega-cap), Amazon.com Inc. (AMZN, Consumer
Cyclical, mega-cap), Alphabet Inc. (GOOG, Communication Services, mega-cap), Microsoft Corp.
(MSFT, Technology, mega-cap), Tesla Inc. (TSLA, Consumer Cyclical, mega-cap), andBTCUSD
(Cryptocurrency, digital asset)—to seven additional equities: Grab Holdings (GRAB, Technology,
large-cap), Alibaba Group (BABA, Consumer Cyclical, mega-cap), The Coca-Cola Company (KO,
Consumer Defensive, mega-cap), Johnson & Johnson (JNJ, Healthcare, mega-cap), United Parcel
Service (UPS, Industrials, large-cap), Upwork (UPWK, Communication Services, small-cap), and
Sprouts Farmers Market (SFM, Consumer Defensive, mid-cap).
First, we includeGrab Holdings (GRAB, Singapore)andAlibaba Group (BABA, China)to assess
whether F2Agent remains effective beyond the primary U.S.-centric asset set. As shown in Table 13,
F2Agent achieves the highest Annualized Return on both GRAB and BABA, reaching 105.43% and
122.27%, respectively. It also attains the best Sharpe Ratio on BABA and the second-best Sharpe
Ratio on GRAB, suggesting strong risk-adjusted performance under different market narratives. In
contrast, several ML/DL and LLM-based baselines show unstable behavior, including negative returns
on BABA or GRAB. These results suggest that the proposed multi-agent fusion mechanism remains
effective when the asset-specific information environment differs from the primary benchmark.
27

Table 13: Performance comparison on GRAB and BABA.
Category Model GRAB BABA
ARR%↑SR↑MDD%↓ARR%↑SR↑MDD%↓
Market B&H 64.62 0.96 24.51 73.93 1.07 25.12
Rule-based
MACD 35.80 0.86 15.22 46.30 1.05 22.02
ZMR 68.611.79 6.46 16.06 0.5711.26
SMA 28.10 1.2112.2586.81 1.717.03
ML/DL LSTM 58.90 0.96 24.51 -17.84 -0.24 26.85 Transformer 3.38 0.20 24.51 -19.23 -0.35 26.86
RL DQN 26.78 0.69 18.31 16.94 0.44 20.42 PPO -24.87 -0.54 15.87 65.88 1.37 13.39
General LLMs
Qwen3-8B 60.53 1.01 19.09 96.23 1.38 19.90
DeepSeek-R1 -1.63 0.13 24.51125.811.73 17.75
Llama4-Scout -24.72 -0.32 29.65 16.34 0.43 25.90
GPT5-mini -20.99 -0.26 18.31 48.71 0.99 16.29
Financial LLMs
FinGPT 70.43 1.20 13.27 64.45 1.02 25.12
FinAgent82.271.25 14.48 95.62 1.8014.50
TradingAgents -19.42 -0.33 29.65 27.20 74.31 15.39
DeepFund 74.31 1.16 18.15 84.90 1.43 19.22
Ours F 2Agent 105.43 1.5113.79122.27 2.06 11.26
Second, we evaluate whether the performance advantage persists under a longer and more recent
test horizon. Table 14 reports results from 2025-04-01 to 2026-03-20 while keeping the original
training and validation sets unchanged. Across AAPL, GOOG, TSLA, and BTCUSD, F 2Agent
achieves the best CR, ARR, and SR on all four assets. Specifically, F2Agent obtains 30.15% ARR
and 1.02 SR on AAPL, 108.75% ARR and 2.88 SR on GOOG, and 78.49% ARR and 1.47 SR on
TSLA. The advantage is also evident on BTCUSD, where several baselines suffer negative returns,
whereas F2Agent achieves positive performance with 18.06% CR, 12.58% ARR, 0.84 SR, and the
lowest MDD of 12.90%. As shown in the improvement row, F2Agent improves ARR by 42.35%,
8.50%, 16.54%, and 24.43% over the strongest alternatives on AAPL, GOOG, TSLA, and BTCUSD,
respectively. Although F2Agent does not achieve the lowest MDD on AAPL, it still provides the
strongest return and Sharpe Ratio, indicating a favorable risk-return trade-off over the extended
horizon.
Table 14: Performance comparison across four assets from different sectors, including AAPL
(Technology, ultra-mega-cap), GOOG (Communication Services, ultra-mega-cap), TSLA (Consumer
Cyclical, ultra-mega-cap), and BTCUSD (Cryptocurrency). The evaluation period is 2025-04-01 to
2026-03-20, while the original training and validation datasets remain unchanged.Boldindicates the
best result in each column, and underlined values indicate the second-best result.
Category Model AAPL GOOG TSLA BTCUSD
CR(%)↑ARR(%)↑SR↑MDD(%)↓CR(%)↑ARR(%)↑SR↑MDD(%)↓CR(%)↑ARR(%)↑SR↑MDD(%)↓CR(%)↑ARR(%)↑SR↑MDD(%)↓
Market B&H 11.55 12.00 0.36 22.99 92.43 97.15 2.31 13.51 41.65 43.49 0.65 22.37 -16.78 -12.32 -0.38 47.55
Rule-based SMA -2.13 -2.21 -0.15 11.88 68.84 72.15 2.49 8.94 13.68 14.23 0.45 18.68 -15.79 -11.55 -0.76 27.66
ML/DL Transformer 6.97 7.24 0.25 22.99 56.57 59.19 1.70 12.48 64.30 67.35 1.12 17.64 -14.00 -10.21 -0.37 46.89
RL PPO 17.73 18.45 0.67 9.4841.18 43.00 1.50 9.18 -1.72 -1.78 -0.06 23.50 -15.20 -11.11 -0.51 39.42
General LLMs Llama4-Scout-17B 3.62 3.76 0.13 18.95 77.50 81.31 2.32 9.96 10.86 11.28 0.24 29.20 -3.00 -2.15 -0.10 30.99
Financial LLMs
FinAgent 16.84 17.51 0.65 13.88 95.33 100.23 2.33 12.71 30.40 31.84 0.51 24.43 -13.78 -10.04 -0.43 39.50
TradingAgents -12.04 -12.46 -0.53 26.25 56.50 59.12 2.00 9.76 49.15 51.38 1.15 22.64 16.33 10.11 0.76 23.38
DeepFund 20.35 21.18 0.66 15.86 58.20 60.91 1.95 12.86 39.44 41.17 0.72 34.67 -33.06 -25.16 -1.14 47.14
Ours F 2Agent 28.93 30.15 1.0220.05103.33 108.75 2.88 8.85 74.84 78.49 1.47 15.32 18.06 12.58 0.84 12.90
Improvement(%) 42.16 42.35 52.24 – 8.39 8.50 15.66 1.01 16.39 16.54 27.83 13.15 10.59 24.43 10.53 44.82
Third, we further test F 2Agent on a broader stock pool beyond the main experimental assets. As
reported in Table 15, F2Agent achieves the best CR, ARR, and SR on all newly added assets, including
KO, JNJ, UPS, UPWK, and SFM. The advantage is particularly clear on UPWK and SFM, where the
market benchmark and several baselines produce negative returns, while F2Agent remains profitable.
These results suggest that F 2Agent generalizes beyond mega-cap technology-oriented assets and
remains effective across assets with different sector characteristics, volatility profiles, and market-cap
ranges.
28

Table 15: Performance comparison on the five newly added assets KO (Consumer Defensive, Mega-
cap), JNJ (Healthcare, Mega-cap), UPS (Industrials, Large-cap), UPWK (Communication Services,
Small-cap), and SFM (Consumer Defensive, Mid-cap). The evaluation period is 2025-04-01 to
2026-03-20, while the original training and validation datasets remain unchanged.Boldindicates the
best result in each column, and underlined values indicate the second-best result.
Category Model KO JNJ UPS
CR(%)↑ARR(%)↑SR↑MDD(%)↓CR(%)↑ARR(%)↑SR↑MDD(%)↓CR(%)↑ARR(%)↑SR↑MDD(%)↓
Market B&H 7.02 7.26 0.42 9.82 57.86 59.76 2.68 8.42 -6.27 -6.47 -0.22 22.39
Rule-based SMA 3.47 3.60 0.32 7.62 36.50 38.08 2.40 5.17 6.00 6.23 0.27 23.80
ML/DL Transformer 15.50 16.12 1.02 6.73 41.29 43.11 2.37 8.42 -3.45 -3.58 -0.13 17.97
RL PPO -11.93 -12.34 -0.96 17.92 12.62 13.12 1.07 6.24 -3.04 -3.15 -0.1811.84
General LLMs Llama4-Scout-17B -2.62 -2.71 -0.22 13.03 50.94 53.26 2.57 8.67 -15.11 -15.62 -0.65 26.36
Financial LLMs
FinAgent 7.31 7.59 0.45 10.40 55.98 58.57 2.60 8.42 12.61 13.27 0.50 17.30
TradingAgents -2.30 -2.40 -0.355.8325.61 26.673.25 2.64-15.98 -16.53 -0.81 21.17
DeepFund -5.72 -5.95 -0.46 13.36 22.43 23.68 1.42 10.25 -0.19 -0.20 -0.01 22.46
Ours F 2Agent 24.95 25.98 1.546.9263.31 66.312.92 9.7014.50 15.08 0.6320.09
Improvement(%) 60.91 61.16 51.99 – 9.42 10.95 – – 15.04 13.61 23.98 –
Category Model UPWK SFM
CR(%)↑ARR(%)↑SR↑MDD(%)↓CR(%)↑ARR(%)↑SR↑MDD(%)↓
Market B&H -13.29 -13.75 -0.25 48.67 -45.56 -46.77 -1.35 63.48
Rule-based SMA 10.65 11.07 0.49 26.48 -17.12 -17.70 -1.10 31.09
ML/DL Transformer -9.93 -10.28 -0.23 45.50 -18.21 -18.82 -0.73 42.13
RL PPO -13.81 -14.28 -0.39 34.56 -12.42 -12.85 -0.62 35.00
General LLMs Llama4-Scout-17B -18.61 -19.23 -0.58 34.56 -34.55 -35.57 -1.02 54.93
Financial LLMs
FinAgent 4.69 4.87 0.36 45.31 -24.66 -25.45 -0.87 50.45
TradingAgents -14.51 -15.00 -0.37 39.27 -54.33 -55.63 -2.05 61.67
DeepFund -14.88 -15.33 -0.32 46.32 1.74 1.80 0.20 40.05
Ours F 2Agent 22.04 22.94 0.83 14.68 8.02 8.33 0.61 19.73
Improvement(%) 106.95 107.23 69.39 44.56 360.92 362.78 205.00 36.54
Overall, the additional experiments indicate that the performance of F2Agent is not confined to the
primary asset set or the original evaluation window. Instead, the model maintains strong profitability
and competitive risk-adjusted behavior across broader assets and longer test horizons.
G DETAILS OFRANDOM-SEEDROBUSTNESS ANDSTATISTICAL
SIGNIFICANCE
To further assess the robustness of F 2Agent beyond a single random seed, we conduct additional
experiments with three different seeds on AAPL and BTCUSD. We compare F 2Agent with the
Transformer baseline and the concatenation-based fusion baseline, which respectively represent a
strong sequence modeling baseline and a simplified fusion variant. Tables 16 and 17 report the raw
results and the corresponding mean–standard deviation statistics.
The raw seed-level results show that F2Agent consistently achieves higher ARR and SR than both
baselines across all tested seeds on both assets. On AAPL, F 2Agent obtains ARR values of 50.08%,
47.60%, and 55.59%, all clearly above Transformer and Concat. Fusion. Its SR also remains highly
stable around 1.20–1.22, while the two baselines show larger fluctuations. In particular, Concat.
Fusion varies substantially across seeds, ranging from -3.32% to 28.04% ARR on AAPL, indicating
that simple concatenation is more sensitive to initialization and training randomness.
The mean–standard deviation results further support this observation. On AAPL, F2Agent achieves
the highest average ARR of 51.09% with a standard deviation of 4.09, compared with 31.20±7.68
for Transformer and 14.64±16.17 for Concat. Fusion. The difference is more pronounced for SR:
F2Agent obtains 1.2096±0.0102, showing very small seed-induced variation. In contrast, Transformer
and Concat. Fusion have larger SR deviations, especially Concat. Fusion with 0.1465±0.4257. For
MDD, F2Agent also achieves the lowest average drawdown on AAPL, 8.04±0.37, suggesting that its
stronger return does not come from substantially higher downside exposure.
On BTCUSD, which is more volatile than the equity asset, F2Agent also maintains the best average
ARR and SR. It achieves 50.33 ±3.80 ARR and 1.4984 ±0.0858 SR, outperforming Transformer
29

and Concat. Fusion by clear margins. Although Transformer obtains a lower average MDD on
BTCUSD, its ARR and SR are much lower than those of F 2Agent. Meanwhile, F 2Agent has an
almost unchanged MDD across seeds, 9.7886 ±0.0029, indicating that its drawdown behavior is
highly stable under different random initializations. These results suggest that F2Agent provides a
more reliable risk-return profile rather than relying on a favorable random seed.
Table 18 reports a paired statistical significance analysis based on seed-wise ARR improvements. On
AAPL, F2Agent improves ARR over Transformer by 19.89 percentage points, with a 95% confidence
interval of [9.33, 30.44] and a paired t-test p-value of 0.0149. It also improves over Concat. Fusion
by 36.45 percentage points, with a 95% confidence interval of [5.05, 67.84] and a p-value of 0.0378.
Both comparisons are statistically significant at the 0.05 level.
On BTCUSD, F 2Agent improves ARR over Concat. Fusion by 41.93 percentage points, with a
95% confidence interval of [18.54, 65.33] and a p-value of 0.0164, again indicating a statistically
significant improvement. The comparison against Transformer shows a positive mean improvement
of 21.54 percentage points, but the 95% confidence interval slightly crosses zero and the p-value is
0.0535. Therefore, this result should be interpreted as a strong positive trend rather than a statistically
significant difference at the 0.05 level. Given the small number of seeds, we report these tests as
supporting evidence rather than as a standalone proof of significance.
Overall, the random-seed experiments show that F 2Agent maintains strong performance across
different initializations. It consistently achieves the highest average ARR and SR on both AAPL and
BTCUSD, with lower or comparable variance relative to the baselines. The significance analysis
further confirms that the improvements are statistically reliable in most comparisons, especially
against the concatenation-based fusion baseline. These findings provide additional evidence that the
proposed fusion and robustness mechanisms improve both performance and stability.
Table 16: Random-seed variance analysis on AAPL and BTCUSD. ARR and MDD are reported in
percentage (%), and SR is reported as a unitless ratio.
Method Seed AAPL BTCUSD
ARR(%)↑SR↑MDD(%)↓ARR(%)↑SR↑MDD(%)↓
F2Agent
42 50.0757 1.2201 7.8252 53.5700 1.5200 9.7869
43 47.5979 1.2088 7.8247 46.1502 1.4039 9.7869
44 55.5921 1.1998 8.4610 51.2787 1.5714 9.7919
Transformer
42 32.9000 0.7200 13.7700 26.3500 1.1800 8.2600
43 22.8142 0.5398 11.3903 34.9831 1.0527 9.7869
44 37.8899 0.7937 11.9059 25.0519 0.9280 7.9304
Concat. Fusion
42 19.2080 0.3257 22.9865 7.1844 0.3963 10.7631
43 -3.3172 -0.3395 3.3304 15.0368 0.5926 9.1551
44 28.0350 0.4532 22.9865 2.9817 0.2276 10.0582
Table 17: Results over 3 random seeds on AAPL and BTCUSD. We report mean± standard deviation.
ARR and MDD are reported in percentage (%).
Method AAPL BTCUSD
ARR(%)↑SR↑MDD(%)↓ARR(%)↑SR↑MDD(%)↓
Concat. Fusion 14.6419±16.1672 0.1465±0.4257 16.4345±11.3485 8.4010±6.1189 0.4055±0.1827 9.9921±0.8060
Transformer 31.2014±7.6801 0.6845±0.1306 12.3554±1.2519 28.7950±5.3982 1.0536±0.1260 8.6591±0.9905
F2Agent51.0886±4.0922 1.2096±0.0102 8.0370±0.3672 50.3330±3.7992 1.4984±0.08589.7886±0.0029
30

Table 18: Statistical significance analysis over 3 random seeds. We report the mean ARR improvement
of F2Agent over each baseline, together with the 95% confidence interval (CI) and paired t-test p-
value. ARR improvements are reported in percentage points.
Asset Comparison ARR(%) Improvement↑95% CI p-value
AAPL F 2Agent vs Transformer +19.8872 [9.3330, 30.4414] 0.0149
AAPL F 2Agent vs Concat. Fusion +36.4466 [5.0498, 67.8435] 0.0378
BTCUSD F 2Agent vs Transformer +21.5380 [-0.8072, 43.8832] 0.0535
BTCUSD F 2Agent vs Concat. Fusion +41.9320 [18.5369, 65.3271] 0.0164
H DETAILS OFCASESTUDY
To qualitatively examine F2Agent’s robustness to market noise and its cross-modal reasoning ca-
pability, we conduct a qualitative case study on Apple Inc. (AAPL) during a volatile period from
April to October 2025 (Fig. 7). Compared with DeepFund, F 2Agent better navigates noisy narratives,
structural risks, and high-confidence opportunities through agentic fusion.
For unsustainable news, on Sep 22, the market is driven by a high-noise positive narrative around
iPhone 17 preorders while the news itself suggested the significance is exaggerated. DeepFund issued
a BUY , whereas F2Agent leveraged noise-robust consistency regularization to detect weak cross-
modal confirmation and choose to HOLD, avoiding a potential bull trap. For bad news, on May 22,
signals about expansion halting and partnership backlash implied a more persistent deterioration
rather than a transient technical dip. DeepFund executed a contrarian BUY driven by oversold
technical cues, while F2Agent’s modality-aware fusion prioritized strategic risk evidence extracted by
the News Agent and decisively issued a SELL signal to preserve capital under downside uncertainty.
For good news, on Apr 10, valuation support and accumulation provided a coherent positive catalyst
supported by both textual narratives and market dynamics. F2Agent integrated these aligned cues and
executed a confident BUY , whereas DeepFund misread the context and issued a SELL, missing the
ensuing upside.
To further interpret the case study, we visualize the modality-level attention scores before and after
standardization. As shown in Fig. 11, the raw attention scores reveal how F 2Agent dynamically
allocates attention across market, technical, news, and sentiment modalities over time. After stan-
dardization, Fig. 12 makes the relative salience of each modality more comparable, highlighting
when the model relies more on textual evidence or structured market signals. These results suggest
that F2Agent does not follow a fixed modality preference, but adaptively adjusts modality weights
according to the market context.
Overall, this case study suggests that F2Agent goes beyond single-modality reactions by integrating
cross-modal evidence and robustness regularization to make more reliable trading decisions.
Market: 0.18
Technical: 0.30
News:0.21
Sentiment: 0.31
Market: 0.14
Technical: 0.50
News: 0.21
Sentiment: 0.15
Market: 0.03
Technical: 0.74
News: 0.06
Sentiment: 0.17
Market: 0.14
Technical: 0.67
News: 0.08
Sentiment: 0.12
Market: 0.26
Technical: 0.26
News: 0.27
Sentiment: 0.22
Market: 0.15
Technical: 0.22
News: 0.22
Sentiment: 0.42
Market: 0.30
Technical: 0.39
News: 0.12
Sentiment: 0.19
Market: 0.34
Technical: 0.32
News: 0.15
Sentiment: 0.18
Figure 11: Attention scores of our proposed method.
31

Market: 0.38
Technical: 0.28
News: 0.39
Sentiment: 0.54
Market: 0.29
Technical: 0.54
News: 0.39
Sentiment: 0.23
Market: 0.05
Technical: 0.85
News: 0.06
Sentiment: 0.26
Market: 0.29
Technical: 0.75
News: 0.11
Sentiment: 0.16
Market: 0.57
Technical: 0.22
News: 0.52
Sentiment: 0.36
Market: 0.31
Technical: 0.17
News: 0.41
Sentiment: 0.75
Market: 0.68
Technical: 0.39
News: 0.20
Sentiment: 0.31
Market: 0.77
Technical: 0.31
News: 0.27
Sentiment: 0.29
Figure 12: Attention scores of our proposed method (after standardized).
I DETAILS OFSTOCKMOVEMENTPREDICTIONSENHANCEMENT
Table 19: Performance comparison of F2Agent with and without the MaF module across different
stocks.
Method AAPL AMZN GOOG
ACC(%) MCC ACC(%) MCC ACC(%) MCC
F2Agent w/o MaF 53.02 0.0431 50.30 -0.0044 52.71 0.0533
F2Agent 57.94 0.2122 55.56 0.1055 54.76 0.0889
Method MSFT TSLA BTCUSD
ACC(%) MCC ACC(%) MCC ACC(%) MCC
F2Agent w/o MaF 51.70 0.0159 50.60 0.0191 51.67 0.0261
F2Agent 57.14 0.1840 56.35 0.0778 53.55 0.0599
Table 19 presents the ablation study investigating the impact of the Multi-agent Fusion (MaF) module.
The results provide strong evidence for the importance of the fusion mechanism. When the MaF
module is removed (“F2Agent w/o MaF”), the system shows limited directional discrimination, as
indicated by MCC scores hovering near zero (e.g., 0.0431 for AAPL and -0.0044 for AMZN). In
contrast, integrating the MaF module leads to substantial performance gains across all six assets.
Specifically,Accuracy (ACC)improves by approximately 4–6% on major tech stocks (e.g., AAPL:
53.02%→57.94% , MSFT: 51.70%→57.14% ). More importantly, theMatthews Correlation
Coefficient (MCC)increases substantially (e.g., AAPL: 0.0431→0.2122 , MSFT: 0.0159→
0.1840), which suggests that the fusion module effectively synthesizes conflicting signals from
different experts to generate robust, non-trivial predictive signals.
32
