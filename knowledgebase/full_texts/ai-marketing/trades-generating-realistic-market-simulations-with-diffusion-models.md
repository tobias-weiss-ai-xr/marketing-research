---
title: 'TRADES: Generating Realistic Market Simulations with Diffusion Models'
url: https://arxiv.org/abs/2502.07071
category: ai-marketing
subcategory: empirical
date: 2025-01
venue: ''
authors:
- Leonardo Berti
- Bardh Prenkaj
- Paola Velardi
source: arxiv
pdf_url: https://arxiv.org/pdf/2502.07071
pages: 8
chars: 50355
fetched_at: '2026-11-08T13:14:54+00:00'
kb_version: 1
---

# TRADES: Generating Realistic Market Simulations with Diffusion Models

TRADES: Generating Realistic Market Simulations
with Diffusion Models
Leonardo Bertia,*, Bardh Prenkajb and Paola V elardia
aSapienza University of Rome
bTechnical University of Munich
Abstract.Financial markets are complex systems characterized
by high statistical noise, nonlinearity, volatility, and constant evolu-
tion. Thus, modeling them is extremely hard. Here, we address the
task of generating realistic and responsive Limit Order Book (LOB)
market simulations, which are fundamental for calibrating and test-
ing trading strategies, performing market impact experiments, and
generating synthetic market data. We propose a novelTRAnsformer-
based DenoisingDiffusion ProbabilisticEngine for LOBSimulations
(TRADES). TRADES generates realistic order flows as time series
conditioned on the state of the market, leveraging a transformer-based
architecture that captures the temporal and spatial characteristics of
high-frequency market data. There is a notable absence of quantitative
metrics for evaluating generative market simulation models in the
literature. To tackle this problem, we adapt the predictive score, a
metric measured as an MAE, to market data by training a stock price
predictive model on synthetic data and testing it on real data. We com-
pare TRADES with previous works on two stocks, reporting a ×3.27
and ×3.48 improvement over SoTA according to the predictive score,
demonstrating that we generate useful synthetic market data for fi-
nancial downstream tasks. Furthermore, we assess TRADES’s market
simulation realism and responsiveness, showing that it effectively
learns the conditional data distribution and successfully reacts to an
experimental agent, giving sprout to possible calibrations and evalua-
tions of trading strategies and market impact experiments. To perform
the experiments, we developed DeepMarket, the first open-source
Python framework for LOB market simulation with deep learning.
In our repository, we include a synthetic LOB dataset composed of
TRADES’s generated simulations.
1 Introduction
A realistic and responsive market simulation1 has always been a dream
in the finance world [ 35, 24, 29, 22]. Recent years have witnessed
a surge in interest towards deep learning-based market simulations
[25, 30, 16, 10]. An ideal market simulation should fulfill four key
objectives: (1) enable the calibration and evaluation of algorithmic
trading strategies including reinforcement learning models; (2) facili-
tate counterfactual experiments to analyze (2.1) the impact of orders
[44], and (2.2) the consequences of changing financial regulations
and trading rules, such as price variation limits; (3) analyze market
statistical behavior and stylized facts in a controlled environment; (4)
∗ Corresponding Author. Email: berti.1883894@studenti.uniroma1.it. Work
done during M.Sc. at Sapienza University of Rome.
1 To abbreviate, throughout this paper, by “market simulation”, we refer to a
Limit Order Book (LOB) market simulation for a single stock.
generate useful granular market data to facilitate research on finance
and foster collaboration.
For these objectives, two key elements are paramount: therealism
and theresponsivenessof the simulation. Realism refers to the similar-
ity between the generated probability distribution and the actual data
distribution. Responsiveness captures how the simulated market reacts
to an experimental agent’s actions. Furthermore, the generated data
usefulnessis crucial for achieving the last objective (4). Usefulness
refers to the degree to which the generated market data can contribute
to other related financial tasks, such as predicting the trends of stock
prices [34, 38].
Backtesting and Interactive Agent-Based Simulations (IABS) [6]
are two of the most used traditional market simulation methods. Back-
testing assesses the effectiveness of trading strategies on historical
market data. It is inherently non-responsive since there is no way
to measure the market impact of the considered trading strategies,
making the analysis partial. IABS, on the other hand, enables the
creation of heterogeneous pools of simplified traders with different
strategies, aiming to approximate the diversity of the real market.
However, obtaining realistic multi-agent simulations is challenging,
as individual-level historical data of market agents is private, which
impedes the calibration of the trader agents, resulting in an oversim-
plification of real market dynamics.
Recent advances in generative models, particularly Wasserstein
GANs [11, 10, 25], have shown promise in generating plausible mar-
ket orders for simulations. However, GANs are susceptible to mode
collapse [41] and training instability [9], leading to a lack of realism
and usefulness in the generated data.
To address these shortcomings, we present our novelTRAnsformer-
based DenoisingDiffusion ProbabilisticEngine for LOB market
Simulations (TRADES). TRADES generates realistic order flows
that are time series, conditioned on past observations. We demonstrate
that TRADES surpasses state-of-the-art (SoTA) methods in gener-
ating realistic and responsive market simulations. Importantly, due
to its ability to handle multivariate time series generation, TRADES
is adaptable to other domains requiring conditioned sequence data
generation. Furthermore, TRADES readily adapts to an experimen-
tal agent introduced into the simulation, facilitating counterfactual
market impact experiments. In summary, our contributions are:
1. Realistic and responsive market simulation method:We develop
a Denoising Diffusion Probabilistic Engine for LOB Simulations
(TRADES), exploiting a transformer-based neural network archi-
tecture.
2. DeepMarket: We releaseDeepMarket, the first open-source
arXiv:2502.07071v3  [q-fin.TR]  20 Nov 2025

Python framework for market simulation with deep learning. We
also publish TRADES’s implementation and checkpoints to pro-
mote reproducibility and facilitate comparisons and further re-
search.
3. Synthetic LOB dataset:We release a synthetic LOB dataset com-
posed of the TRADES’s generated simulations. We show in the
results (section 7.1) how the synthetic market data can be useful to
train a deep learning model to predict stock prices.
4. New “world” agent for market simulations:We extend ABIDES
[6], an agent-based simulation environment, in our framework by
introducing a new world agent class accompanied by a simulation
configuration, which, given in input a trained generative model,
creates limit order book market simulations. Our experimental
framework does not limit the simulation to a single-world agent
but enables the introduction of other trading agents, which inter-
act among themselves and with the world agent. This defines a
hybrid approach between deep learning-based and agent-based
simulations.
5. First quantitative metric for market simulations:The literature
shows a notable absence of quantitative metrics to evaluate the
generated market simulations. Typically, the evaluation relies on
plots and figures. We posit that a robust and quantitative assessment
is essential for the comparative analysis of various methodologies.
To this end, we adapt the predictive score introduced in [45] to ob-
jectively and quantitatively evaluate the usefulness of the generated
market data.
6. Extensive experiments assessing usefulness, realism, and re-
sponsiveness:We perform a suite of experiments to demonstrate
that TRADES-generated market simulations abide by these three
principles. We show how TRADES outperforms SoTA methods
[6, 11, 10, 43] according to the adopted predictive score and il-
lustrate how TRADES follows the established stylized facts in
financial markets [43].
2 Background
Here, we provide background information on multivariate time se-
ries generation and limit order book markets. Furthermore, since
TRADES is an extension of the Denoising Diffusion Probabilistic
Model (DDPM), we summarize it in the Appendix [3].
2.1 Multivariate time series generation
Generating realistic market order streams can be formalized as a mul-
tivariate time series generation problem. Let X={x 1:N,1:K } ∈
RN×K , be a multivariate time series, where N is the time dimension
(i.e., length) and K is the number of features. The goal of generating
multivariate time series is to consider a specific time frame of previ-
ous observations, i.e., {x1:N,1:K }, and to produce the next sample
xN+1 . This task can easily be formulated as a self-supervised learn-
ing problem, where we leverage the past generated samples as the
conditioning variable for an autoregressive model. In light of this, we
can define the joint probability of the time series as in Eq. (1).
q(x) =
NY
n=1
q(xn |x 1, ...,xn−1)(1)
We leverage this concept at inference time using a sliding window
approach. Hence, for every generation step, 2 we generate a single
2 For everyTdiffusion steps there is a generation step
sample xN ∈R K. In the next step, we append the generated xN to
the end of the conditional part and shift the entire time series one step
forward (see Section 4 for details with TRADES). Because we aim to
generate a multivariate time series starting from observed values, we
model the conditioned data distribution q(xN |x1:N−1 ) with a learned
distribution pθ(xN |x1:N−1 ), to sample from it. Hereafter, we denote
the conditional part3 with xc, and the upcoming generation part with
xg.
2.2 Limit Order Book
In a Limit Order Book (LOB) market, traders can submit orders to
buy or sell a certain quantity of an asset at a particular price. There
are three main types of orders in a limit order market. (1) Amarket
orderis filled instantly at the best available price. (2) Alimit order
allows traders to decide the maximum (in the case of a buy) or the
minimum (in the case of a sell) price at which they want to complete
the transaction. A quantity is always associated with the price for
both types of orders. (3) Acancel order 4 removes an active limit
order. The Limit Order Book (LOB) is a data structure that stores and
matches the active limit orders according to a set of rules. The LOB
is accessible to all the market agents and is updated with each event,
such as order insertion, modification, cancellation, and execution. The
most used mechanism for matching orders is the Continuous Double
Auction (CDA). In a CDA, orders are executed whenever a price
overlaps between the best bid (the highest price a buyer is willing to
pay) and the best ask (the lowest price a seller is willing to accept).
This mechanism allows traders to trade continuously and competi-
tively. The evolution over time of a LOB represents a multivariate
temporal problem. We can classify the research on LOB data into four
main types of studies, namely empirical studies analyzing the LOB
dynamics [4, 12], price and volatility forecasting [47, 38], modeling
the LOB dynamics [13, 17] and LOB market simulation [6, 10, 25].
3 Related Works
Diffusion models for time series generation.Diffusion models have
been successfully applied to generate images [2], video [28], and text
[48]. Recently, they have also been exploited for time series forecast-
ing [26], imputation [40], and generation [27]. Lim et al. [27] tackle
time series generation using diffusion models. They present TSGM,
which relies on an RNN-based encoder-decoder architecture with a
conditional score-matching network. Yangming Li’s TS-Diffusion
[46] introduces a neural-ODE encoder with self-attention and a diffu-
sion core to manage irregularities and missingness in complex series
Market simulation with deep learning.Generating realistic market
simulations using deep learning is a new paradigm. Traditional
computational statistical approaches [ 12] and IABS [ 6] rely on
strong assumptions, such as constant order size, failing to produce
realistic simulations. These methods are mainly used to study how
the interactions of autonomous agents give rise to aggregate statistics
and emergent phenomena in a system. Limit order book simulations
are increasingly relying on deep learning. Li et al. [25] were the first
to leverage a Wasserstein GAN (WGAN) [ 1] for generating order
flows based on historical market data. Similarly, Coletta et al. [10, 11]
employ WGANs in their stock market simulations, addressing the
issue of responsiveness to experimental agents for the first time.
Different
3 We remark that the conditioning can be composed of real or generated
samples.
4 Sometimes, events referring to these orders are defined as deletion.

+
... x 0 gx t-1 g
  ϵ θ
... x t g q(x t |x t-1 )g g x T g
x 0 c
MLP
MLP
LOB
Orders
Diffusion step
Embedding
+
Positional
Embedding
TRADES
Block
X N
θΣ
Latent Space
X  T
x T-1
g
MLP
MLP
x 0 gMLP MLP MLP MLP + Diffusion
step t
+
Positional
Embedding
Latent Space
X  N
θΣ
θ ϵCDT
Block
p θ (x t |x t-1, x 0 )cg g
Dataset
Figure 1: The training procedure and architecture of TRADES. We apply noise to the time series’s last element until obtaining xg T . We condition
xg T on the previous N−1 orders and the last N LOB snapshots. We feed these new tensors to two separate MLPs, each composed of two
fully connected layers, to augment them into a higher-dimensional space. We concatenate the augmented output vectors on the features axis
and sum the diffusion embedding step t and the positional embedding; We feed the result to the TRADES modules, composed of multi-head
self-attention and feedforward layers, producing the noise εθ and the standard deviation Σθ. εθ and Σθ go through a de-augmentation phase via
MLPs to map them back to the input space and are used to reconstruct xg T−1 . We repeat this procedure T times until we recover the original xg 0.
from [ 10, 11, 25], we condition with both the last orders and
LOB snapshots, pushing the generation process toward a more
realistic market simulation. Hultin et al. [21] extend [14] and model
individual features with separate conditional probabilities using
RNNs. Instead of relying on GANs, which are prone to model
collapse and instability [ 9], and RNNs, often hampered by the
vanishing gradient phenomenon, we exploit diffusion-based models
with an underlying transformer architecture. Nagy et al. [ 30] rely
on simplified state-space models to learn long-range dependencies,
tackling the problem via a masked language modeling approach. Shi
and Cartlidge [37] introduce NS-LOB, a novel hybrid approach that
combines a pre-trained neural Hawkes [36] process with a multi-agent
trader simulation. We refer the reader to [ 23] for a comprehensive
review of limit order book simulations.
4 Transformer-based Denoising Diffusion
Probabilistic Engine for LOB Simulations
We introduce TRADES, a Transformer-based Denoising Diffusion
Probabilistic Engine for LOB Simulations. Conditional diffusion mod-
els are better suited than standard diffusion models in generative se-
quential tasks because they can incorporate information from past
observations that guide the generation process towards more specific
and desired outputs. We formalize the reverse process for TRADES
and the self-supervised training procedure. In Section 5, we specialize
our architecture for market simulations.
4.1 Generation with TRADES
Here, we focus on an abstract time series generation task with
TRADES. The goal of probabilistic generation is to approximate the
true conditional data distribution q(xg 0 |x c 0) with a model distribution
pθ(xg 0 |x c 0). During the forward process, we apply noise only to
the “future” – i.e., the part of the input we want to generate – while
keeping the observed values unchanged. Therefore, the forward
process is defined as in the unconditional case (see Appendix [3] or
[18]). For the reverse process, we extend the unconditional
onep θ(x0:T ), to the conditional case:
pθ(xg 0:T ) :=p(x g T )
TY
t=1
pθ(xg t−1 |x g t ,x c 0)(2)
pθ(xg t−1 |x g t ,x c 0) :=N(x g t−1;µ θ(xg t ,x c 0, t),Σθ(xg t ,x c 0, t))(3)
We define the conditional denoising learnable function as in Eq. (4).
ϵθ :

xg t ∈R S×K ,x c 0 ∈R M×K , t∈R K

→ϵ t ∈R S×K (4)
where M+S=N . We set M=N−1 and S= 1 for our
experiments. Using S >1 increases the efficiency, but also the task
complexity because, in a single generative step, we generate S time
series steps. We exploit the parametrization proposed in [18] described
in Eq. (5) to estimate the mean term.
µθ(xg t ,x c 0, t) = 1√αt

xg t − βt√1− αt ϵθ(xg t ,x c 0, t)  (5)
wherex g t = √ αtxg 0 + √ 1− αtϵ ϵ∼ N(0,I).(6)
We do not rely on a fixed schedule as in [18] regarding the variance
term. Inspired by [31], we learn it as in Eq. (7).
Σθ(xg t ,x c 0, t) = exp(vlogβt + (1−v) log ˜βt),(7)
where v is the neural network output, together with ϵθ. Nichol and
Dhariwal [ 31] found that this choice improves the negative log-
likelihood, which we try to minimize. After computing ϵt and σt, we
denoisex g t−1 as in Eq (8).
xg t−1 = 1√αt

xg t − βt√1− αt ϵθ(xg t ,x c 0, t)  +σ tz(8)
where z∼ N(0,I) . After the T steps, the denoising process is
finished, andx g 0 is reconstructed.
4.2 Self-supervised Training of TRADES
Given generation target xg 0 and conditional observations xc 0, we sam-
ple xg t = √αtxg 0 + √1− αtϵ, where ϵ∼ N(0,I), and train ϵθ by
minimizing Eq. (9).
Lϵ(θ) :=E t,x0,ϵ
h
||ϵ−ϵ θ(xg t ,x c 0, t)||2
i
.(9)

Inspired by [ 31], we also learn 5 Σθ optimizing it according to
Eq. (10).
LΣ(θ) :=E q
"
−pθ(xg 0 |x g 1,x c 0)| {z }
L0
+D KL (q(xg T |x g 0)||p θ(xg T )| {z }
LT
+
TX
t=2
DKL (q(xg t−1 |x g t ,x g 0)||p θ(xg t−1 |x g t ,x c 0)) | {z }
Lt−1
#
.
(10)
We optimize Eq. (10) to reduce the negative log-likelihood, especially
during the first diffusion steps where LΣ is high [31]. The final loss
function is a linear combination of the two as in Eq: (11).
L=L ϵ +λL Σ.(11)
Where λ is used to balance the two terms. We perform training by
relying on a self-supervised approach as follows. Given a time series
x0 ∈R N×K , we apply noise only to its last element – i.e., xN 0 –
through the forward pass. Then, we denoise it via the reverse process
and learn pθ(xg t−1 |x g t ,x c 0) which aims to generate a new sample
from the last observations. Therefore, during training, the conditioning
has only observed values. At sampling time, TRADES generates new
samples autoregressively, conditioned on its previous outputs, until
the simulation ends.
5 TRADES for Market Simulation
To create realistic and responsive market simulations, we imple-
ment TRADES to generate orders conditioned on the market state.
TRADES’s objective is to learn to model the distribution of orders. Fig.
1 presents an overview of the diffusion process and the architecture.
The network that produces εθ and Σθ contains several transformer
encoder layers to model the temporal and spatial relationships of
the financial time series [38]. Since transformers perform better with
large dimension tensors, we project the orders tensor and the LOB
snapshots to a higher dimensional space, using two fully connected
layers. Hence, TRADES operates on the augmented vector space.
After the reverse process, we de-augment εθ and Σθ projecting them
back to the input space to reconstructx g t−1 and compute the loss.
Conditioning.The conditioned diffusion probabilistic model learns
the conditioned probability distribution pθ(o|s), where s is the
market state, and o is the newly generated order, represented as
(p, q, d, b, δ, c), where p is the price, q is the quantity, d is the di-
rection either sell or buy, b is the depth, i.e., the difference between p
and the best available price,δ is the time offset representing the tempo-
ral distance from the previously generated order andc is the order type
– either market, limit or cancel order. The asymmetries between the
buying and selling side of the book indicate shifts in the supply and
demand curves caused by exogenous and unobservable factors that
influence the price [8]. Therefore, as depicted in Fig. 1, the model’s
conditioning extends beyond the last N−1 orders. To effectively cap-
ture market supply and demand dynamics encoded within the LOB,
we incorporate the last N LOB snapshots of the first L LOB levels as
input, where each level has a bid price, bid size, ask price, and ask size.
We set N= 256 as in [10], and L= 10 . We argue that this choice
of L is a reasonable trade-off between conditioning complexity and
feature informativeness. Several works [20, 42, 33, 7, 8] have shown
that the orders behind the best bid and ask prices play a significant
role in price discovery and reveal information about short-term future
5 Notice from Eq (??) of the original DDPM formulation thatΣ θ is fixed.
price movements. In Sec. 7.3, we delve deeper into the conditioning
choice and method, performing an ablation and a sensitivity study.
6 DeepMarket framework with synthetic dataset for
deep learning market simulations
We present DeepMarket, an open-source Python framework devel-
oped for LOB market simulation with deep learning. DeepMarket
offers the following features: (1) pre-processing for high-frequency
market data; (2) a training environment implemented with PyTorch
Lightning; (3) hyperparameter search facilitated with WANDB; (4)
TRADES and CGAN implementations and checkpoints to directly
generate a market simulation without training; (5) a comprehensive
qualitative (via the plots in this paper) and quantitative (via the pre-
dictive score) evaluation. To perform the simulation with our world
agent and historical data, we extend ABIDES [ 6], an open-source
agent-based interactive Python tool.
6.1 TRADES-LOB: a new synthetic LOB dataset
In LOB research, one major problem is the unavailability of a large
LOB dataset. In fact, if you want to access a large LOB dataset, you
need to pay large fees to a data provider. The only two freely available
LOB datasets are [19] and [32], which have a lot of limitations. The
high cost and low availability of LOB data restrict the application
and development of deep learning algorithms in the LOB research
community. In order to foster collaboration and help the research
community, we release a synthetic LOB dataset: TRADES-LOB.
TRADES-LOB comprises simulated TRADES market data for Tesla
and Intel for two days. Specifically, the dataset is structured into
four CSV files, each containing 50 columns. The initial six columns
delineate the order features, followed by 40 columns that represent
a snapshot of the LOB across the top 10 levels. The concluding
four columns provide key financial metrics: mid-price, spread, order
volume imbalance, and V olume-Weighted Average Price (VWAP),
which can be useful for downstream financial tasks, such as stock
price prediction. In total, the dataset is composed of 265,986 rows and
13,299,300 cells, which is similar in size to the benchmark FI-2010
dataset [32]. The dataset will be released with the code in the GitHub
repository. We show in the results (section 7.1) how the synthetic
market data can be useful to train a deep learning model to predict
stock prices.
7 Experiments
Dataset and reproducibility.In almost all SoTA papers in this sub-
field, the authors use one, two, or three stocks [37, 10, 30, 25, 36, 21],
most of which are tech. Following this practice, we create a LOB
dataset from two NASDAQ stocks 6 – i.e., Tesla and Intel – from
January 2nd to the 30th of 2015. We argue that stylized facts and
market microstructure behaviors, which are the main learning ob-
jective of TRADES, are independent of single-stock behaviors (see
[5, 4, 15, 17]), so the particular stock characteristics, such as volatil-
ity, market cap, and p/e ratio, are not fundamental. Each stock has
20 order books and 20 message files, one for each trading day per
stock, totaling ∼24 million samples. The message files contain a
comprehensive log of events from which we select market orders,
limit orders, and cancel orders. Each row of the order book file
is a tuple

P ask(t), Vask(t), Pbid(t), Vbid(t)  where P ask(t) and
6 The data we used are downloadable from https://lobsterdata.com/
tradesquotesandprices upon buying the book indicated on the website.

Figure 2: PCA analysis on TSLA 29/01. TRADES covers 67.04% of the real distribution, better than the other two methods (52.92% for IABS
and 57.49% for CGAN).
P bid(t)∈R L are the prices of levels 1 through L, and V ask(t) and
V bid(t)∈R L are the corresponding volumes. We use the first 17
days for training, the 18th day for validation, and the last 2 for market
simulations. We are aware of the widely used FI-2010 benchmark
LOB dataset [32] for stock price prediction. However, the absence of
message files in this dataset hinders simulating the market since the
orders cannot be reconstructed. In the Appendix [3], we provide an
overview of FI-2010 and its limitations.
Experimental setting.After training the model for 70,000 steps until
convergence, we freeze the layers and start the market simulation. A
simulation is composed of (1) the electronic market exchange that
handles incoming orders and transactions; (2) the TRADES-based
“world” agent, which generates new orders conditioned on the market
state; and (3) one or more optional experimental agents, that follow
a user-customizable trading strategy, enabling counterfactual and
market impact experiments. So, the experimental framework is a
hybrid approach between a deep learning model and an interactive
agent-based simulation.
We conduct the simulations with the first 15 minutes of real orders
to compare the generated ones with the market replay.7 Afterward, the
diffusion model takes full control and generates new orders autoregres-
sively, conditioned on its previous outputs, until the simulation ends.
After the world agent generates a new order, there is a post-processing
phase in which the output is transformed into a valid order. We begin
the simulation at 10:00 and terminate it at 12:00. This choice ensures
that the generated orders are sufficient for a thorough evaluation while
maintaining manageable processing times. On average, 50,000 orders
are produced during this two-hour time frame. The output CSV file of
the simulation contains the full list of orders and LOB snapshots of
the simulation. All experiments are performed with an RTX 3090 and
a portion of an A100. In the Appendix [3], we detail the data pre- and
post-processing and model hyperparameter choice.
Baselines.We compare TRADES with the Market Replay – i.e.,
ground truth (market replay) – a IABS configuration, and the Wasser-
stein GAN – i.e., CGAN – under the setting of [11], similar to the same
of those proposed in [ 10?]. We implemented CGAN from scratch
given that none of the implementations in [? 11, 10] are available. We
report details in the Appendix [3]. Regarding IABS configuration, we
used the Reference Market Simulation Configuration, introduced in
[6], which is widely used as comparison [ 10, 11, 43]. The configu-
ration includes 5000 noise, 100 value, 25 momentum agents, and 1
market maker.8 We do not compare with other SoTA methods due
to the unavailability of open-source implementations and insufficient
details to reproduce the results. In some cases, the code is provided
7 Market replay denotes the simulation performed with the real historical
orders of that day.
8 the full specifics are in the GitHub page of ABIDES in the tutorial section.
but the results are not reproducible due to computational constraints.
7.1 Results
Here, we evaluate theusefulness,realism, and theresponsivenessof
the generated market simulations for Tesla and Intel. We train two
TRADES Models, one for each stock. After training, we freeze the
models and use them to generate orders during the simulation phase.
A major disadvantage of market simulation is the misalignment in
the literature for a single evaluation protocol. All the other works
[11, 21, 30, 10] analyze performances with plots, hindering an
objective comparison between the models. To fill this gap, we adapt
thepredictive score[ 45] for market simulation. Predictive score
is measured as an MAE, by training a stock mid-price predictive
model on synthetic data and testing it on real data, that evaluates the
usefulness of the generated simulations. In the Appendix [ 3], we
detail the computation of the predictive score.
Table 1: Average predictive score (MAE) over two days on Tesla and
Intel stocks. Bold values show the best MAE.
Predictive Score↓
Method Tesla Intel
Market Replay 0.923 0.149
IABS 1.870 1.866
CGAN 3.453 0.699
TRADES 1.213 0.307
Usefulness: TRADES outperforms the second-best by a factor of
×3.27 and ×3.48 on both stocks. 9 We report both stocks’ average
predictive scores in Table 1. Notice that the market replay scores
represent the desired MAE of each model. The table reveals that
TRADES exhibits performances approaching that of the real market
replay, with an absolute difference of 0.29 and 0.158 from market
replay, respectively, for Tesla and Intel, suggesting a diminishing
gap between synthetic and real-data training efficacy. Interestingly,
although IABS cannot capture the complexity of real trader agents, it
outperforms CGAN on Tesla, while it remains the worst-performing
strategy on Intel. In conclusion, we demonstrated how a predictive
model trained with TRADES’s generated market data can effectively
forecast mid-price.
Realism: TRADES covers the real data distribution and emulates
many stylized facts.To evaluate the realism of the generated time
series, we compare the real data distributions with those of the
generated one. We employ a combination of Principal Component
9 The values are computed dividing the second best value with the TRADES
values, both subtracted by the market replay predictive score.

0 5 10 15 20 25 30
Lag (minutes)
0.2
0.1
0.0
0.1
0.2
0.3
0.4
Correlation Coefficient
Log Returns Autocorrelation
Real
TRADES
IABS
CGAN
1.00
 0.75
 0.50
 0.25
 0.00 0.25 0.50 0.75 1.00
Correlation
0
5
10
15
20
25
30Density
Correlation between volume and volatility
TRADES
IABS
Real
CGAN
1.00
 0.75
 0.50
 0.25
 0.00 0.25 0.50 0.75 1.00
Correlation
0
1
2
3
4
5
6
7Density
Correlation between returns and volatility
TRADES
IABS
Real
CGAN

 
 
 
    
/RJ5HWXUQV
 




/RJ)UHTXHQF\
0LQXWHO\/RJ5HWXUQV&RPSDULVRQ
5HDO
75$'(6
&*$1

 
 
     
&RUUHODWLRQ&RHIILFLHQW






)UHTXHQF\
$XWRFRUUHODWLRQ/RJ5HWXUQV'LVWULEXWLRQ
5HDO
,$%6
75$'(6
&*$1
09:30 10:00 10:30 11:00 11:30 12:00
194
196
198
200
202
204
Normalized Mid Price
Market Replay
TRADES simulation init.
TRADES inference
Time
Mid-Price Traces for Generated Orders
Figure 3: Stylized facts on Tesla 29/01. (1) Log returns autocorrelation.
(2) The correlation between volume and volatility, and (3) between
returns and volatility. (4) Comparison of the minute Log Returns dis-
tribution and (5) autocorrelation. (6) Mid-price traces of five different
TRADES simulations.
09:36 10:04 10:33 11:02 11:31 12:00
Time
100
200
300
400
500Volume at 1st level
Volume Market Replay
ask_size mean
ptc5-95 enveloppe ask
bid_size mean
ptc5-95 enveloppe bid
09:36 10:04 10:33 11:02 11:31 12:00
Time
100
200
300
400
500
600Volume at 1st level
Volume TRADES simulation
ask_size mean
ptc5-95 ask
bid_size mean
ptc5-95 bid
09:36 10:04 10:33 11:02 11:31 12:00
Time
0
2000
4000
6000
8000
10000
12000Volume at 1st level
Volume CGAN simulation
ask_size mean
ptc5-95 ask
bid_size mean
ptc5-95 bid
09:36 10:04 10:33 11:02 11:31 12:00
Time
0
5000
10000
15000
20000
25000Volume at 1st level
Volume IABS simulation
ask_size mean
ptc5-95 enveloppe ask
bid_size mean
ptc5-95 enveloppe bid
Figure 4: V olume at the first level of LOB on TSLA 29/01.
Analysis (PCA), alongside specialized financial methodolo-
gies that include the comparison of stylized facts and important
features. In Fig. 2, we show PCA plots to illustrate how well the
synthetic distribution covers the original data. TRADES (blue points)
cover 67.04% of the real data distribution (red points) according
to a Convex Hull intersection compared to 52.92% and 57.49%
of CGAN and IABS, respectively. Following [ 43], we evaluate
the simulation realism by ensuring that the generated market data
mimics stylized facts derived from real market scenarios. Fig. 3
(1) illustrates that TRADES, similarly to the market replay and
differently to IABS and CGAN, obey the expectedabsence of
autocorrelation, indicating that the linear autocorrelation of asset
returns decays rapidly, becoming statistically insignificant after 15
minutes. Fig. 3 (2) highlights TRADES’s resemblance withthe
positive volume-volatility correlation. TRADES’s generated orders
show a positive volume-volatility correlation. Interestingly, TRADES
captures this phenomenon better than that particular market replay
day. Recall that TRADES is trained on 17 days of the market, so
it correctly captures this correlation. We acknowledge that the real
market might not always respect all the stylized facts due to their
inherent non-deterministic and non-stationary nature. Also, CGAN
resembles this phenomenon but, differently from TRADES, with an
unrealistic intensity.
Fig 3 (3) shows that TRADES exhibitsasset returns and volatil-
ity negative correlation, emulating the market replay distribution in
contrast with IABS. Similar to the previous case, also, CGAN also
resembles this phenomenon but with an unrealistic intensity. Fig. 3
(4) illustrates that TRADES almost perfectly resembles the real distri-
bution in terms oflog returns. We leave IABS out since it disrupts the
plot’s scale. In Fig. 3 (5), we show the autocorrelation function of the
squared returns, commonly used as an analytical tool to measure the
degree ofvolatility clustering: i.e., high-volatility episodes exhibit a
propensity to occur in close temporal proximity. Note that TRADES
emulates the real distribution better than the other two methods. In
Fig. 3 (6), we illustrate the mid-price time series of five different
TRADES10 simulations on the same day of Tesla (29/01) and the
market replay of that day. The mid-price traces generated show diver-
sity and realism. Lastly, to consolidate our claims about TRADES’s
realism, in Fig. 4 we also analyze the volume distribution of the first
LOB level. Notice how the scale and the overall behavior of the vol-
ume time series in the market replay strongly correlate with that of
TRADES’s simulation, while it is completely different w.r.t. SoTA
approaches.
Responsiveness: TRADES is responsive to external agent.The re-
sponsiveness of a LOB market simulation generative model is crucial,
especially if the objective of the market simulation is to verify the
profitability of trading strategies or perform market impact experi-
ments. Generally [10, 11, 37], the responsiveness of a generator is
assessed through a market impact experiment (A/B test). Therefore,
we conducted an experiment running some simulations w/ and w/o a
Percentage-Of-V olume (POV) agent, which wakes up every minute
and places a bunch of buy orders, until either ϕ shares have been
transacted or the temporal window ends. We refer the reader to the
Appendix [3] for the details of the settings of this experiment. Fig.
5 depicts the normalized mid-price difference between the simula-
tions w/ and w/o the POV agent for the market replay and TRADES.
Results are averaged over 5 runs. As expected, the historical market
simulation exhibits only instantaneous impact [17], that is the direct
effect of the agent’s orders, which rapidly vanishes. Contrarily, the
diffusion-based simulations demonstrate substantial deviation from
the baseline simulation without the POV agent, altering the price
permanently. Quantifying the permanent price impact in real markets
poses a significant challenge, as it requires comparing price differ-
ences between scenarios where a specific action took place and those
where it did not. Such scenario analysis is not feasible with empirical
data. However, by using TRADES-generated realistic simulations,
this analysis becomes both feasible and measurable. In fact, the sim-
ulations allow us to run identical scenarios both with and without
additional trader agents whose strategy can be fully defined by the
user. In conclusion, the observed market impact in the TRADES sim-
ulations aligns with real market observations [ 17, 5], enabling the
evaluation of trading strategies11 and counterfactual experiments.
10 TRADES is frozen, and the same model is used for all simulations.
11 we want to be clear that it technically enables evaluating trading strategies,
but it does not assure any profitability in a real market scenario.

09:30 09:40 09:50 10:00 10:10 10:20 10:30 10:40 10:50 11:00
Time
0.4
0.2
0.0
0.2
0.4
Average Difference in Mid Price
Market replay responsiveness
09:30 09:40 09:50 10:00 10:10 10:20 10:30 10:40 10:50 11:00
Time
4
2
0
2
4
Average Difference in Mid Price
TRADES responsiveness
Figure 5: Average mid-price difference of market replay simulations and TRADES simulations with (shaded part) and without a POV agent
(unshaded part), on 5 different seeds.
7.2 DDIM sampling
One of the known limitations of diffusion models is the sampling time.
Indeed, the generation of a single sample necessitates hundreds of
iterative passes through the neural network. In this work, the model
was trained using a diffusion process comprising 100 steps. Recently,
the Denoising Diffusion Implicit Model (DDIM) sampling method
was proposed in [39] to speed up the generative process. Given that
each hour of market simulation required six hours of computation
on an RTX 3090, accelerating the simulation process was a relevant
improvement. Consequently, we conducted simulations employing
DDIM sampling (η= 0 ), which is deterministic, utilizing a single
step for each order. We use the same trained model. The results,
presented in Table 2, demonstrate that the performance degradation is
significant but not disastrous despite a remarkable 100-fold increase
in computational efficiency.
Table 2: Average predictive score (MAE) over two days on Tesla and
Intel stocks. DDIM sampling is done with a single step, while DDPM
with 100.
Predictive Score↓
Method Tesla Intel
DDIM 3.146 0.486
DDPM (orig.) 1.213 0.307
7.3 Ablation and sensitivity studies
Table 3 shows two ablations (i.e., LOB conditioning and augmenta-
tion) and two sensitivity analyses (i.e., backbone choice and condi-
tioning method) that highlight the effectiveness of TRADES design
choice.
Ablation analyses.We verify two of the hypotheses made in the
method design: (1) how much the LOB conditioning part is necessary
for the task and (2) how augmenting the feature vectors influences the
performance. When we include LOB in the conditioning w.r.t. last or-
ders only, TRADES has an average gain of 2.473. When we augment
the features through the MLPs in Fig. 1, we gain an average of 1.980
MAE absolute points.Sensitivity analyses.We aim to verify whether
the complexity of the backbone – i.e., the transformer in TRADES –
is needed after all. Therefore, we replace the transformer backbone
with an LSTM, leaving the augmentation and conditioning invariant.
The table shows that the performances degrade by an average of 6.06
absolute points. This is expected since transformers directly access
all other steps in the sequence via self-attention, which theoretically
leaves no room for information loss that occurs in LSTMs. Recall
Table 3: Predictive score for the ablation (A) and sensitivity (S) analy-
ses for two days of Tesla simulations.
Predictive Score↓
Method 29/01 30/01
A TRADES w/o LOB 2.642 4.728 TRADES w/o Aug. 1.442 4.942
S LSTM backbone 8.391 6.153 TRADES w/ CA 11.90 4.891
TRADES (orig.)1.336 1.089
that we concatenate the past orders and the LOB snapshots, after the
augmentation, into a single tensor and use it to condition the diffu-
sion model – i.e., TRADES (Orig.). We also tried a cross-attention
(CA) conditioning strategy, – see TRADES w/ CA – between the past
orders and the LOB snapshots. TRADES w/ CA reports an average
performance loss of 7.814 absolute points w.r.t. the original architec-
ture. Note that cross-attention limits the model’s capability because
the orders cannot attend to each other but only to LOB and vice-versa.
8 Conclusion
We proposed a Transformer-based Denoising Diffusion Probabilistic
Engine for LOB Simulations (TRADES) to generate realistic order
flows conditioned on the current market state. We adapted the pre-
dictive score to verify the usefulness of the generated market data
by training a prediction model on it and testing it on real data. We
showed that TRADES can cover the real data distribution by 67% on
average and outperforms SoTA by ×3.27 and ×3.48 on Tesla and
Intel. Furthermore, we demonstrated that TRADES correctly abides
by many stylized facts used to evaluate the goodness of financial
market simulation approaches. We release DeepMarket, a Python
framework for market simulation with deep learning and TRADES-
LOB, a synthetic LOB dataset composed of TRADES’s generated
market simulations. We argue that TRADES-LOB and DeepMarket
will have a positive impact on the research community, as almost no
LOB data is freely available. We believe that TRADES is a viable
market simulation strategy in controlled environments, and further
tests must be performed to have a mature evaluation trading strat-
egy protocol. A promising experiment could involve training a larger
model across various stocks, eliminating the need for an individual
model for each stock.

Acknowledgements
This work was supported by a grant from Lazio Region, FESR
Lazio 2021-2027, project @HOME (F89J23001050007 CUP
B83C23006240002) and by the project “E-DAI”: Piano Operativo
Salute (POS) 2014-2020, CUP: B83C22004150001.
References
[1] M. Arjovsky, S. Chintala, and L. Bottou. Wasserstein generative adver-
sarial networks. InInternational conference on machine learning, pages
214–223. PMLR, 2017.
[2] J. Austin, D. D. Johnson, J. Ho, D. Tarlow, and R. Van Den Berg. Struc-
tured denoising diffusion models in discrete state-spaces.Advances in
Neural Information Processing Systems, 34:17981–17993, 2021.
[3] L. Berti, B. Prenkaj, and P. Velardi. Appendix for trades: Generating
realistic market simulations with diffusion models, 2025. URL https:
//github.com/LeonardoBerti00/DeepMarket/blob/main/Appendix.pdf.
[4] J.-P. Bouchaud, M. Mézard, and M. Potters. Statistical properties of
stock order books: empirical results and models.Quantitative finance, 2
(4):251, 2002.
[5] J.-P. Bouchaud, J. D. Farmer, and F. Lillo. How markets slowly digest
changes in supply and demand. InHandbook of financial markets:
dynamics and evolution, pages 57–160. Elsevier, 2009.
[6] D. Byrd, M. Hybinette, and T. H. Balch. Abides: Towards high-fidelity
multi-agent market simulation. InProceedings of the 2020 ACM SIGSIM
Conference on Principles of Advanced Discrete Simulation, pages 11–22,
2020.
[7] C. Cao, O. Hansch, and X. Wang. Order placement strategies in a pure
limit order book market.Journal of Financial Research, 31(2):113–140,
2008.
[8] C. Cao, O. Hansch, and X. Wang. The information content of an open
limit-order book.Journal of Futures Markets: Futures, Options, and
Other Derivative Products, 29(1):16–41, 2009.
[9] C. Chu, K. Minami, and K. Fukumizu. Smoothness and stability in gans.
arXiv preprint arXiv:2002.04185, 2020.
[10] A. Coletta, M. Prata, M. Conti, E. Mercanti, N. Bartolini, A. Moulin,
S. Vyetrenko, and T. Balch. Towards realistic market simulations: a
generative adversarial networks approach. InProceedings of the Second
ACM International Conference on AI in Finance, pages 1–9, 2021.
[11] A. Coletta, A. Moulin, S. Vyetrenko, and T. Balch. Learning to simulate
realistic limit order book markets from data as a world agent. InPro-
ceedings of the Third ACM International Conference on AI in Finance,
pages 428–436, 2022.
[12] R. Cont. Empirical properties of asset returns: stylized facts and statisti-
cal issues.Quantitative finance, 1(2):223, 2001.
[13] R. Cont. Statistical modeling of high-frequency financial data.IEEE
Signal Processing Magazine, 28(5):16–25, 2011.
[14] R. Cont, S. Stoikov, and R. Talreja. A stochastic model for order book
dynamics.Operations research, 58(3):549–563, 2010.
[15] R. Cont, A. Kukanov, and S. Stoikov. The price impact of order book
events.Journal of financial econometrics, 12(1):47–88, 2014.
[16] R. Cont, M. Cucuringu, J. Kochems, and F. Prenzel. Limit order book
simulation with generative adversarial networks.Available at SSRN
4512356, 2023.
[17] M. D. Gould, M. A. Porter, S. Williams, M. McDonald, D. J. Fenn,
and S. D. Howison. Limit order books.Quantitative Finance, 13(11):
1709–1742, 2013.
[18] J. Ho, A. Jain, and P. Abbeel. Denoising diffusion probabilistic mod-
els.Advances in neural information processing systems, 33:6840–6851,
2020.
[19] C. Huang, W. Ge, H. Chou, and X. Du. Benchmark dataset for short-term
market prediction of limit order book in china markets.The Journal of
Financial Data Science, 3(4):171–183, 2021.
[20] R. D. Huang and H. R. Stoll. Market microstructure and stock return
predictions.The Review of Financial Studies, 7(1):179–213, 1994.
[21] H. Hultin, H. Hult, A. Proutiere, S. Samama, and A. Tarighati. A gen-
erative model of a limit order book using recurrent neural networks.
Quantitative Finance, pages 1–28, 2023.
[22] B. I. Jacobs, K. N. Levy, and H. M. Markowitz. Financial market
simulation.The Journal of Portfolio Management, 30(5):142–152, 2004.
[23] K. Jain, N. Firoozye, J. Kochems, and P. Treleaven. Limit order book
simulations: A review.arXiv preprint arXiv:2402.17359, 2024.
[24] H. Levy, M. Levy, and S. Solomon.Microscopic simulation of financial
markets: from investor behavior to market phenomena. Elsevier, 2000.
[25] J. Li, X. Wang, Y . Lin, A. Sinha, and M. Wellman. Generating realistic
stock market order streams. InProceedings of the AAAI Conference on
Artificial Intelligence, volume 34, pages 727–734, 2020.
[26] Y . Li, X. Lu, Y . Wang, and D. Dou. Generative time series forecast-
ing with diffusion, denoise, and disentanglement.Advances in Neural
Information Processing Systems, 35:23009–23022, 2022.
[27] H. Lim, M. Kim, S. Park, and N. Park. Regular time-series generation
using sgm.arXiv preprint arXiv:2301.08518, 2023.
[28] K. Mei and V . Patel. Vidm: Video implicit diffusion models. InProceed-
ings of the AAAI Conference on Artificial Intelligence, volume 37, pages
9117–9125, 2023.
[29] T. Mizuta. A brief review of recent artificial market simulation (agent-
based model) studies for financial market regulations and/or rules.Avail-
able at SSRN 2710495, 2016.
[30] P. Nagy, S. Frey, S. Sapora, K. Li, A. Calinescu, S. Zohren, and J. Foerster.
Generative ai for end-to-end limit order book modelling: A token-level
autoregressive generative model of message flow using a deep state space
network.arXiv preprint arXiv:2309.00638, 2023.
[31] A. Q. Nichol and P. Dhariwal. Improved denoising diffusion probabilistic
models. InInternational conference on machine learning, pages 8162–
8171. PMLR, 2021.
[32] A. Ntakaris, M. Magris, J. Kanniainen, M. Gabbouj, and A. Iosi-
fidis. Benchmark dataset for mid-price forecasting of limit order
book data with machine learning methods. http://urn.fi/urn:nbn:fi:
csc-kata20170601153214969115. N/A.
[33] R. Pascual and D. Veredas. What pieces of limit order book information
do are informative? an empirical analysis of a pure order-driven market.
2003.
[34] M. Prata, G. Masi, L. Berti, V . Arrigoni, A. Coletta, I. Cannistraci,
S. Vyetrenko, P. Velardi, and N. Bartolini. Lob-based deep learning
models for stock price trend prediction: A benchmark study, 2023.
[35] M. Raberto and S. Cincotti. Modeling and simulation of a double
auction artificial financial market.Physica A: Statistical Mechanics and
its applications, 355(1):34–45, 2005.
[36] Z. Shi and J. Cartlidge. State dependent parallel neural hawkes process
for limit order book event stream prediction and simulation. InProceed-
ings of the 28th ACM SIGKDD Conference on Knowledge Discovery
and Data Mining, pages 1607–1615, 2022.
[37] Z. Shi and J. Cartlidge. Neural stochastic agent-based limit order book
simulation: A hybrid methodology. In N. Agmon, B. An, A. Ricci, and
W. Yeoh, editors,Proceedings of the 2023 International Conference
on Autonomous Agents and Multiagent Systems, AAMAS 2023, London,
United Kingdom, 29 May 2023 - 2 June 2023, pages 2481–2483. ACM,
2023. doi: 10.5555/3545946.3598974. URL https://dl.acm.org/doi/10.
5555/3545946.3598974.
[38] J. A. Sirignano. Deep learning for limit order books.Quantitative
Finance, 19(4):549–570, 2019.
[39] J. Song, C. Meng, and S. Ermon. Denoising diffusion implicit models.
arXiv preprint arXiv:2010.02502, 2020.
[40] Y . Tashiro, J. Song, Y . Song, and S. Ermon. Csdi: Conditional score-
based diffusion models for probabilistic time series imputation.Advances
in Neural Information Processing Systems, 34:24804–24816, 2021.
[41] H. Thanh-Tung and T. Tran. Catastrophic forgetting and mode collapse
in gans. In2020 international joint conference on neural networks
(ijcnn), pages 1–10. IEEE, 2020.
[42] D. T. Tran, J. Kanniainen, and A. Iosifidis. How informative is the
order book beyond the best levels? machine learning perspective.arXiv
preprint arXiv:2203.07922, 2022.
[43] S. Vyetrenko, D. Byrd, N. Petosa, M. Mahfouz, D. Dervovic, M. Veloso,
and T. Balch. Get real: Realism metrics for robust limit order book
market simulations. InProceedings of the First ACM International
Conference on AI in Finance, pages 1–8, 2020.
[44] K. T. Webster.Handbook of Price Impact Modeling. Chapman and
Hall/CRC, 2023.
[45] J. Yoon, D. Jarrett, and M. Van der Schaar. Time-series generative adver-
sarial networks.Advances in neural information processing systems, 32,
2019.
[46] X. Yuan and Y . Qiao. Diffusion-TS: Interpretable diffusion for general
time series generation. InThe Twelfth International Conference on
Learning Representations, 2024. URL https://openreview.net/forum?id=
4h1apFjO99.
[47] Z. Zhang, S. Zohren, and S. Roberts. Deeplob: Deep convolutional
neural networks for limit order books.IEEE Transactions on Signal
Processing, 67(11):3001–3012, 2019.
[48] Y . Zhu, Z. Li, T. Wang, M. He, and C. Yao. Conditional text image
generation with diffusion models. InProceedings of the IEEE/CVF
Conference on Computer Vision and Pattern Recognition, 2023.
