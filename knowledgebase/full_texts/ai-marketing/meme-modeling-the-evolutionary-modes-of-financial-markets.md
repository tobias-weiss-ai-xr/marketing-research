---
title: 'MEME: Modeling the Evolutionary Modes of Financial Markets'
url: https://arxiv.org/abs/2602.11918
category: ai-marketing
subcategory: empirical
date: 2026-02
venue: ''
authors:
- Taian Guo
- Haiyang Shen
- Junyu Luo
- Zhongshi Xing
- Hanchun Lian
source: arxiv
pdf_url: https://arxiv.org/pdf/2602.11918
pages: 20
chars: 69470
fetched_at: '2026-11-08T13:18:59+00:00'
kb_version: 1
---

# MEME: Modeling the Evolutionary Modes of Financial Markets

MEME: Modeling the Evolutionary Modes of Financial Markets
Taian Guo1 2 Haiyang Shen 3† Junyu Luo 1 Zhongshi Xing 4 Hanchun Lian 5 Jinsheng Huang 1 2
Binqi Chen 1 2
Luchen Liu 2 Yun Ma3✉ Ming Zhang 1✉
Abstract
LLMs have demonstrated significant potential in
quantitative finance by processing vast unstruc-
tured data to emulate human-like analytical work-
flows. However, current LLM-based methods pri-
marily follow either anAsset-Centricparadigm fo-
cused on individual stock prediction or aMarket-
Centricapproach for portfolio allocation, often
remaining agnostic to the underlying reasoning
that drives market movements. In this paper, we
propose aLogic-Orientedperspective, modeling
the financial market as a dynamic, evolutionary
ecosystem of competing investment narratives,
termedModes of Thought. To operationalize
this view, we introduce MEME (Modeling the
Evolutionary Modes of Financial Markets), de-
signed to reconstruct market dynamics through
the lens of evolving logics. MEME employs a
multi-agent extraction module to transform noisy
data into high-fidelity Investment Arguments and
utilizes Gaussian Mixture Modeling to uncover
latent consensus within a semantic space. To
model semantic drift among different market con-
ditions, we also implement a temporal evalua-
tion and alignment mechanism to track the life-
cycle and historical profitability of these modes.
By prioritizing enduring market wisdom over
transient anomalies, MEME ensures that portfo-
lio construction is guided by robust reasoning.
Extensive experiments on three heterogeneous
Chinese stock pools from 2023 to 2025 demon-
strate that MEME consistently outperforms seven
SOTA baselines. Further ablation studies, sen-
†Project Leader. ✉Corresponding. Contact: Taian Guo <taian-
guo@stu.pku.edu.cn>, Haiyang Shen <hyshen@stu.pku.edu.cn>.
1National Key Laboratory for Multimedia Information Processing,
PKU-Anker LLM Lab, School of Computer Science, Peking Uni-
versity 2Zhengren Quant, Beijing, China 3Institute for Artificial
Intelligence, Peking University 4Sun Yat-sen University5School of
Electronics Engineering and Computer Science, Peking University.
Correspondence to: Yun Ma <mayun@pku.edu.cn>, Ming Zhang
<mzhang cs@pku.edu.cn>.
Preprint. 2026
sitivity analysis, lifecycle case study and cost
analysis validate MEME’s capacity to identify
and adapt to the evolving consensus of financial
markets. Our implementation can be found at
https://github.com/gta0804/MEME.
1. Introduction
LLMs (Team et al., 2025a; Liu et al., 2025; Yang et al.,
2025; Team et al., 2025b) are increasingly being applied in
quantitative finance (Blyth, 2014; McNeil et al., 2015). By
processing vast amounts of unstructured data such as finan-
cial reports and social media discussions, multi-agent sys-
tems powered by LLMs can emulate the complex workflows
of human analysts to distill insights and inform investment
decisions. These systems demonstrate considerable promise
by analyzing individual assets and adapting to changing
market conditions.
Current LLM-based financial trading methods can be gen-
erally classified into two primary categories based on their
analytical focus. The Asset-Centric category is primarily
predictive, where the core objective is to map micro-level
signals to the performance of individual stocks through fore-
casting (Koa et al., 2024; Zhang et al., 2024a) or Alpha
Factor Mining (Tang et al., 2025; Shi et al., 2025b). The
second category, Market-Centric approaches (Tong et al.,
2024; Guo et al., 2025; Li et al., 2025b), is primarily alloca-
tive, shifting the focus to the stock pool level to optimize
weights across a collection of assets. While effective, these
paradigms are fundamentally object-oriented: they focus
on “what” to buy or “how much” to allocate, while remain-
ing agnostic to the underlying “why”. They often view the
market as a static collection of data points, overlooking the
latent, evolving reasoning that catalyzes market movements.
Distinct from these object-oriented paradigms, we model
the financial trading problem from a Logic-Oriented per-
spective. We posit that the market is not merely a collection
of assets, but a dynamic, evolutionary ecosystem of compet-
ing investment logics, which we term Modes of Thought. In
this view, asset price movements are effectively the physi-
cal manifestations of abstract trading narratives gaining or
1
arXiv:2602.11918v1  [cs.AI]  12 Feb 2026

MEME: Modeling the Evolutionary Modes of Financial Markets
losing consensus among market participants. However, the
path to capturing these modes is obstructed by two layers of
noise. First, the structural chaos and extreme noise density
of multimodal data streams frequently obscure the underly-
ing reasoning. Second, even when arguments are extracted,
the reasoning itself is susceptible to logical noise—plausible-
sounding narratives that are empirically invalid, contradic-
tory, or fail to materialize in price movements. Furthermore,
because individual market signals are inherently sparse and
expressed through diverse terminology, the collective con-
sensus remains hidden within idiosyncratic observations.
Most crucially, the non-stationary nature of financial mar-
kets causes investment narratives to undergo constant seman-
tic drift. Without modeling the complete lifecycle of these
evolving logics and filtering out erroneous reasoning, it is
hard to distinguish enduring market wisdom from fleeting,
high-frequency anomalies.
To navigate these complexities, we introduce MEME, a
framework to reconstruct market dynamics through the lens
of evolving Modes of Thought. Our methodology begins
with a multi-agent extraction module, using specialized fil-
tering and generation agents to transform unstructured noise
into high-fidelity Investment Arguments. This collaborative
architecture is essential for maintaining reasoning purity
while handling vast, heterogeneous data. To uncover latent
consensus, we apply Gaussian Mixture Modeling (GMM)
within a semantic space. This probabilistic approach is
well-suited for financial reasoning as it captures the nu-
anced reality where a single argument may resonate with
multiple overlapping themes. To address the challenge of
logical noise, MEME implements a temporal evaluation and
alignment mechanism. By linking related modes across
consecutive days and evaluating their historical profitabil-
ity through exponential moving averages, the framework
can distinguish between robust, value-generating market
wisdom and erroneous or transient logics. This ensures
that portfolio construction is guided by historically proven
market narratives rather than unverified or failing reasoning.
We conduct extensive experiments on three heterogeneous
stock pools in the Chinese market, including the SSE 50,
CSI 300, and CSI 500, covering a volatile period from 2023
to 2025. Our evaluation compares MEME against eight com-
petitive baselines, ranging from traditional gradient boosting
and deep factor models to state-of-the-art LLM-based agen-
tic frameworks. The results demonstrate that our method
achieves superior profitability and stability across various
market regimes. Beyond performance metrics, we provide a
detailed ablation study to verify each component, a param-
eter sensitivity analysis, and a temporal out-of-sample test
to ensure robustness against data leakage. Finally, a com-
prehensive case study visualizes the lifecycle of identified
modes, validating the capacity of our framework to track
the transition of market consensus and identify effective
investment narratives as market conditions evolve.
In summary, our main contributions are as follows:
• We introduce MEME, a framework that models mar-
ket dynamics as an evolutionary process of competing
Modes of Thought, shifting the focus from assets to the
lifecycle of investment logics.
• We design an end-to-end system that extracts structured
arguments, identifies latent consensus via probabilis-
tic modeling, and tracks the lifecycle of these modes
through temporal alignment.
• We conduct extensive experiments on three stock pools
with distinct styles, achieving consistent improvements
over seven SOTA baselines and providing an in-depth
analysis of the identified market modes.
2. Related Work
This section reviews literature on financial trading. We
categorize existing studies into asset-centric and market-
centric approaches.
2.1. Asset-Centric Approaches
Asset-centric research focuses on the micro-level forecast-
ing of individual assets and the mining of predictive sig-
nals. This field includes traditional quantitative studies such
as formulaic alpha factor mining and stock trend predic-
tion (Blyth, 2014; McNeil et al., 2015). Researchers use
genetic programming (Chen et al., 2021), reinforcement
learning (Yu et al., 2023; Zhu & Zhu, 2025), and flow net-
works (Chen et al., 2025) to generate predictive expressions.
Other studies employ factor modeling (Duan et al., 2022;
Xiang et al., 2024; Duan et al., 2025; Shi et al., 2025a) and
temporal dependency analysis (Yoo et al., 2021; Li et al.,
2024b; Zhang et al., 2025a). Advanced models also in-
tegrate entity dependencies (Zhao et al., 2022; Xu et al.,
2021; Qian et al., 2024; Song et al., 2025), causality mod-
eling (Luo et al., 2023; Li et al., 2024a), and sentiment
features (Araci, 2019; Du et al., 2024) or financial founda-
tion models (Shi et al., 2025c). With the development of
LLMs, agent-based methods have emerged. These systems
perform multi-modal analysis (Zhang et al., 2024a), engage
in expert debates (Xiao et al., 2025a), and use in-context
self-reflection (Koa et al., 2024). Some frameworks also
apply task-specific fine-tuning (Tian et al., 2025; Deng &
Wang, 2025). In alpha factor mining, agents utilize iterative
refinement (Li et al., 2024c; Tang et al., 2025; Cao et al.,
2025) and navigated tree searching (Shi et al., 2025b) to
find effective formulas.
Our method diverges from these asset-centric works by shift-
ing the analytical target from micro-level mapping to macro-
level reasoning. While traditional approaches treat assets as
independent units and attempt to map noisy features directly
2

MEME: Modeling the Evolutionary Modes of Financial Markets
to price movements, we posit that individual asset fluctua-
tions are often idiosyncratic. Instead of predicting “what”
an asset will do based on its internal signals, MEME extracts
the underlying Investment Arguments that explain “why” a
group of assets moves in tandem, thereby achieving higher
reasoning purity by filtering out asset-specific noise.
2.2. Market-Centric Approaches
Market-centric approaches examine the financial problem
at the stock pool or portfolio level. Traditional research
focuses on portfolio construction through inter-stock covari-
ance matrix prediction (Zhu et al., 2022; Zheng et al., 2023)
and multi-factor dimension reduction (Lin et al., 2021).
Some studies apply reinforcement learning for weight opti-
mization across a collection of assets (Zhang et al., 2024b).
Recently, LLM-based systems have been used to synthesize
information across the stock pool. For example, some works
use diverse expert discussions to analyze constituent stocks
for portfolio construction (Tong et al., 2024). Other meth-
ods employ multi-agent collaboration (Guo et al., 2025),
investor behavior simulation (YANG et al., 2025), order-
level simulation (Li et al., 2025a) or model-factor collabora-
tion (Li et al., 2025b) to manage market interactions.
Our framework departs from these market-centric ap-
proaches in both perspective and methodology. First, while
existing methods are primarily object-oriented as they treat
the stock pool as a collection of assets to be weighted, we
adopt a logic-oriented perspective that views the market as
a dynamic competition of underlying narratives. Second,
we shift the focus from spatial allocation to temporal evo-
lution. Instead of merely optimizing asset weights for a
static market snapshot, MEME models the complete life-
cycle of Modes of Thought. By tracking how investment
logics emerge, gain consensus, and decay through temporal
alignment, we ensure that portfolio construction is guided by
the historical robustness of a narrative rather than transient
correlations dependent on specific market states.
3. Methodology
MEME is designed to construct daily portfolios from multi-
modal financial data. Unlike traditional asset-centric or
market-centric methods, MEME is logic-oriented. We focus
on the “why” behind price movements by modeling the mar-
ket as an evolving ecosystem of investment narratives. The
process begins with raw daily data for a universe ofN stocks
over a period of T trading days. The input for a given stock
s on day t is a data point Dt,s, comprising information from
a set of modalitiesM={Fundamental,News,Technical}:
Dt,s ={D t,s,m |m∈M}
where Dt,s,m is for stock s on day t from modality m. The
final outputis a daily portfolio weight vectorW t ∈R N .
MEME operationalizes this process through three sequential
stages. First, we extract structured investment arguments
from noisy multimodal data. Second, we identify latent
modes of reasoning by clustering these arguments and track-
ing their evolution over time. Third, we evaluate the histori-
cal profitability of each mode to construct a final portfolio.
The overall architecture of MEME is provided in Figure 1,
and the pseudocode is available in Appendix 1.
3.1. Argument Extraction: From Noise to Structure
The initial stage of MEME transforms unstructured, multi-
modal financial data into structured records, which we term
Investment Arguments. This stage is designed to overcome
the structural chaos and high noise density in raw data.
To manage the low signal-to-noise ratio inherent in raw
data, we employ a multi-agent system that filters relevant
information from each data modality and then generates
structured arguments, each containing a directional stance,
a rationale, and supporting evidence. This collaborative
design ensures the purity of the reasoning by separating
informative signals from irrelevant noise. This process is
implemented through two steps:
Information Filtering.For each modality m∈M , a filter
agent, Ffilter,m, processes the raw data Dt,s,m to extract a
concise set of relevant information,I t,s,m.
It,s,m =F filter,m(Dt,s,m)(1)
Argument Generation.The filtered information from
all modalities is consolidated. A generator agent, Fgen,
then synthesizes this unified information set to a series of
structured investment arguments,{A t,s,i}i.
{At,s,i}i =F gen
 [
m∈M
It,s,m
!
(2)
Each argument At,s,i is a tuple containing a polarity p, an
analytical rationalea, and its supporting evidencee:
At,s,i = (pt,s,i, at,s,i, et,s,i)(3)
where pt,s,i ∈ {+1,−1}indicates the argument’s direc-
tional stance.The design details are in the Appendix A.2.
3.2. Mode Identification and Alignment
After extracting individual arguments, we identify and track
the underlying consensus they represent. Isolated arguments
are often sparse and may use varied terminology for similar
concepts. Besides, the focus of investors may shift over
time. Therefore, this stage first identifies latent modes of
reasoning by clustering arguments in a semantic space on
a given day. Subsequently, it aligns these modes across
consecutive days to model their temporal evolution.
3

MEME: Modeling the Evolutionary Modes of Financial Markets
Argument Extraction
News
Fundamental
Technical
Filter
Generator
Filtering &
Distillation
Polarity:(1/-1）
Rationale: …
Evidence: …

Mode Identification & Alignment
Latent Modes Of Thought
(Day T)
Semantic Embedding
& Clustering Mode A
Mode B
Mode C
𝝅(Mode A)
𝝅(Mode B)
𝝅(Mode C)
Day T Day T-1
Temporal Alignment
Mode Evaluation &
Portfolio Construction
Market Feedback
Perf
Weighted Signal Aggregation
Top-K Selection
Constructed PortfolioArguments
Figure 1: The overall architecture. MEME first mitigates structural noise by distilling raw multimodal data into structured
Investment Arguments via multi-agent extraction. To uncover latent consensus, it identifies representative Modes of Thought
through GMM-based probabilistic clustering and models market evolution via temporal alignment of these modes across
consecutive days. Finally, MEME filters logical noise by evaluating the historical profitability of each mode through an
alignment-based scoring mechanism, ensuring that the portfolio is guided by robust and enduring investment narratives.
3.2.1. MODEIDENTIFICATION: FROMARGUMENTS TO
LATENTCONSENSUS
We model the shared logic among arguments by identifying
latent modes within a semantic space. We use a probabilistic
approach because market themes often overlap. A single
argument might reflect multiple themes simultaneously. To
implement this, we apply a Gaussian Mixture Model (GMM)
(Duda & Hart, 1973; Dempster et al., 1977) to the collection
of daily argument embeddings. This process yields a set of
modes, each defined by a Gaussian distribution, and assigns
each argument a membership probability to every mode.
This captures the nuanced reality of market consensus better
than rigid classification.
Formally, we generate a semantic representation for each
argument on a given day t. We concatenate the argument’s
rationale at,s,i and evidence et,s,i, then encode the result
into aD-dimensional vectorx t,s,i using an encoderE:
xt,s,i =E(concat(a t,s,i, et,s,i))∈R D (4)
We then apply a GMM to the collection of all daily argu-
ment embeddings {xt,s,i}s,i. This defines K modes for
day t, where each mode Mt,k is a Gaussian distribution
N(µ t,k,Σ t,k). The GMM also computes the posterior prob-
ability ωt,s,i,k that argument At,s,i belongs to mode Mt,k.
The relationship is captured by a vectorω t,s,i:
ωt,s,i = [ωt,s,i,1, . . . , ωt,s,i,K ],where
KX
k=1
ωt,s,i,k = 1
(5)
3.2.2. TEMPORALMODEALIGNMENT: FROM
SNAPSHOT TOEVOLUTION
To understand the persistence of themes, we connect the
identified modes across time. A static daily analysis is
insufficient as the semantic focus of a mode can drift. We
address this semantic drift by linking related modes across
consecutive days. This allows us to track the complete
lifecycle of investment logics as they emerge and decay.
Let {µt−1,k}K k=1 and {µt,k}K k=1 be the sets of mode cen-
troids for days t−1 and t. We seek a permutation π that
minimizes the total semantic drift between matched modes
by applying a linear-assignment algorithm (Jonker & V ol-
genant, 1987):
min
π∈SK
KX
k=1
d(µt−1,k,µ t,π(k))(6)
where d(·,·) is the Euclidean distance and SK is the set of
all permutations of {1, . . . , K}. The resulting permutation
πestablishes the temporal correspondence of each mode.
3.3. Mode Evaluation and Portfolio Construction
The final stage of MEME evaluates the historical effective-
ness of each mode by leveraging the mode evolution process
and the performance of each mode at every historical cross
section. It helps us distinguish between enduring market
wisdom and narratives that sound plausible but fail in prac-
tice. We develop a mechanism to quantify the historical
profitability of each mode. This performance score is then
used to weight new signals and generate final stock rankings
for the future portfolio.
4

MEME: Modeling the Evolutionary Modes of Financial Markets
Formally, at the close of trading on day t, we evaluate the
performance of all modes from day t−1 . The one-day
forward excess return of stocksis:
rt,s = ct,s −c t−1,s ct−1,s − 1 N
NX
i=1
ct,i −c t−1,i
ct−1,i
(7)
where ct,s is the closing price at day t. The realized score
of an argumentA t−1,s,i is:
Score(At−1,s,i) =pt−1,s,i ·r t,s (8)
The daily aggregated score for each mode k on day t−1 ,
AggScoret−1,k, is the responsibility-weighted average score
of all arguments:
AggScoret−1,k =
P
s,i ωt−1,s,i,k ·Score(A t−1,s,i)P
s,i ωt−1,s,i,k
(9)
To filter out fleeting, high-frequency anomalies, we update a
long-term performance score, Perft−1,k, using an exponen-
tial moving average. This update uses the temporal mapping
π′ from the prior step, which links day t−2 to t−1 , to
ensure performance continuity:
Perft−1,k =λ·Perf t−2,π′−1(k) + (1−λ)·AggScore t−1,k
(10)
whereλ∈[0,1]is a smoothing factor.
Finally, we construct our daily portfolio Wt. By using his-
torically proven narratives to weight new signals, we ensure
that our decisions are guided by robust reasoning. The pro-
cess begins by quantifying the alignment of each new argu-
ment At,s,i with the established modes from day t−1 . This
alignment is computed as a posterior probability, ˆωt,s,i,k,
using the GMM parameters {πt−1,k,µ t−1,k,Σ t−1,k}K k=1
from the previous day:
ˆωt,s,i,k = πt−1,kN(x t,s,i|µt−1,k,Σ t−1,k) PK
j=1 πt−1,jN(x t,s,i|µt−1,j,Σ t−1,j)
(11)
This probability distribution then weights the long-term
performance of the modes, Perft−1,k, to produce a predicted
score for the new argument:
[Score(At,s,i) =
KX
k=1
ˆωt,s,i,k ·Perf t−1,k (12)
We then aggregate these argument-level scores to compute
a composite signal for each stock s. Let I + t,s ={i|p t,s,i =
+1} and I − t,s ={i|p t,s,i =−1} be the index sets for
positive and negative arguments. The signal is the difference
between the average predicted scores of its positive and
negative arguments:
Signalt,s = 1 |I + t,s|+ϵ X i∈I+ t,s [Score(At,s,i)
− 1 |I − t,s|+ϵ X i∈I− t,s [Score(At,s,i) (13)
where ϵ is a small constant for numerical stability. The
resulting signal vector, Signalt ∈R N , provides a ranking
for all stocks. Based on this ranking, we employ a top-K
strategy with equal weight to construct the portfolioW t at
the open of the next trading day.
4. Experiments
4.1. Setup
Datasets: We evaluate MEME on three A-share stock uni-
verses with varying styles: the SSE 50, CSI 300, and CSI
500. Our experiments run from 2023 Q4 to 2025 Q4, a
period that encompasses multiple market style transitions,
including the bear market of late 2023 to early 2024, a
comprehensive bull market in September 2024, a structured
market phase in mid-2025, and an out-of-LLM-knowledge
period in 2025 Q4. The details of the dataset description
and composition are provided in the Appendix A.3.
Performance metrics: Following previous work (Yoo et al.,
2021; Li et al., 2024b; Guo et al., 2025; Li et al., 2025b),
we utilize two types of metrics to evaluate the performance
of MEME: (1) Correlation-based metrics: Information Coef-
ficient (IC), IC Information Ratio (ICIR), Rank Information
Coefficient (RIC), and RIC Information Ratio (RICIR). For
these correlation metrics, the prediction target is daily for-
ward return. (2) Portfolio-based metrics: Annualized Return
(AR), Maximum Drawdown (MDD), and Sharpe Ratio (SR).
The details of these metrics are in the Appendix A.4.
Baselines: We compare MEME with various competitive
baselines across different types: (1) Traditional machine
learning methods: LightGBM (Ke et al., 2017). (2) Deep
learning techniques: DTML (Yoo et al., 2021), Factor-
V AE (Duan et al., 2022), MASTER (Li et al., 2024b).
(3) Agent-based approaches centered on a single asset:
SEP (Koa et al., 2024), TradingAgents (Xiao et al., 2025b).
(4) Agent-based approaches centered on the market: R&D-
Agent(Q) (Li et al., 2025b). The details of all baselines are
provided in the Appendix A.5.
Implementation Details: DeepSeek V3.1 (DeepSeek-AI,
2024) serves as the backbone LLM in MEME and all
agent-based baselines for fair comparisons. We use Qwen3
Embedding-8B (Zhang et al., 2025b) as the embedding
model in mode identification. The number of modes K
is set to 15 for the SSE 50 and 20 for the CSI 300 and the
CSI 500. The smoothing factor λ is set to 0.5. The small
constant ϵ is set to 1e-5. For backtest experiments, we uti-
lize an index-enhanced strategy. The transaction cost is set
to 1.5e-4, and we update our portfolio daily by holding the
top 20% stocks in Equation 13.
5

MEME: Modeling the Evolutionary Modes of Financial Markets
Table 1: Performance comparison on the SSE 50, CSI 300, and CSI 500 stock pools.Boldand underlined numbers represent
the best and second-best performance, respectively. The symbols ↑ and ↓ indicate that higher and lower values are better,
respectively. TheBenchmark Indexrepresents the buy-and-hold strategy of the corresponding market index.
Dataset Method Correlation Metrics (%) Portfolio Metrics
IC↑ ICIR↑ RIC↑ RICIR↑ AR↑ MDD↓ SR↑
SSE 50
LightGBM 2.63 13.56 2.98 17.14 21.19% 15.26% 0.9779
DTML 2.97 13.89 3.19 14.53 18.47% 16.17% 0.9767
FactorV AE 3.05 13.25 3.56 13.98 19.06% 16.55% 0.9263
Master 4.30 18.42 5.42 24.84 24.64%10.71% 1.3761
SEP 3.65 17.89 3.16 15.30 22.58% 16.62% 0.9812
TradingAgents 4.32 21.50 5.31 25.27 24.78 % 11.05% 1.3543
R&D-Agent(Q) 4.27 20.89 5.03 25.80 22.70% 11.21% 1.2988
MEME 6.31 32.99 5.48 29.93 28.74% 10.89% 1.4021
Benchmark Index– – – – 16.18% 13.95% 0.8601
CSI 300
LightGBM 1.18 9.86 2.15 17.50 12.89% 19.08% 0.5864
DTML 3.51 23.25 4.16 25.58 19.13% 15.61% 0.8788
FactorV AE 3.47 20.81 3.98 26.82 18.79% 16.20% 0.7892
Master 4.37 22.60 5.26 28.30 24.46% 19.71% 1.0891
SEP 2.98 19.76 3.42 24.75 18.22% 16.98% 0.9730
TradingAgents 4.18 23.67 5.09 25.78 23.69% 18.40% 1.1310
R&D-Agent(Q) 4.85 28.72 5.45 27.81 25.02 % 16.50 % 1.3216
MEME 6.80 41.71 6.16 39.75 32.48% 10.76% 1.5161
Benchmark Index– – – – 15.72% 17.74% 0.7265
CSI 500
LightGBM 2.18 14.01 4.81 33.11 17.41% 24.52% 0.6872
DTML 3.64 30.47 4.18 34.72 21.04% 23.27% 0.7971
FactorV AE 2.98 26.25 4.97 34.63 20.72% 24.99% 0.7104
Master 2.74 15.63 4.60 23.21 16.36% 26.64% 0.6570
SEP 2.88 18.76 3.95 21.86 15.78% 25.32% 0.5865
TradingAgents 4.06 31.56 5.01 33.06 23.29% 18.64 % 1.0517
R&D-Agent(Q) 4.15 29.09 4.88 32.19 23.50 % 19.89% 1.0343
MEME 6.72 41.15 6.64 34.75 31.97% 16.18% 1.2326
Benchmark Index– – – – 17.90% 24.55% 0.6824
2023-11 2024-01 2024-03 2024-05 2024-07 2024-09 2024-11 2025-01 2025-03 2025-05 2025-07 2025-09 2025-11
0.0
0.2
0.4
0.6Cumulative Return
Ours
CSI 300
SEP
R&DAgent(Q)
LightGBM
DTML
MASTER
FactorVAE
TradingAgents
Figure 2: Backtest on the CSI 300. We compare
MEME with all baselines and the CSI 300 Index.
4.2. Main Experiments
We conduct the main experiments on three datasets from
2023 Q4 to 2025 Q3. Table 1 exhibits all experiment re-
sults across three different datasets. Our analysis yields
two key findings. First, MEME demonstrates strong pre-
dictive capabilities for stock returns, consistently achieving
higher IC, RIC, and AR compared to all baselines. Second,
MEME shows improved stability across different market
conditions, obtaining higher ICIR, RICIR, and SR while
also reducing the MDD.
Besides, we also draw the complete backtest curve on
the CSI 300. As shown in Figure 2, MEME takes the
performance lead in most backtest periods. Furthermore,
MEME demonstrates enhanced robustness by sustaining low
drawdowns during the early 2024 liquidity crisis and the
April 2025 trade frictions, while also achieving favorable
returns throughout the bull market in the mid-2025.
4.3. Experiments on Data Leakage Concern
To validate MEME against potential data leakage, we con-
duct a temporal out-of-sample test on three datasets using
new data from Q4 2025. The results in Table 2 demonstrate
that MEME maintains its performance advantage over all
baselines. This strongly indicates that MEME effective-
ness stems from our methodological design and not from
contamination within the LLM’s training corpus.
4.4. Ablation Study
We conduct an ablation study to evaluate the contribution of
each core component of MEME. Table 3 presents the results
of incrementally adding each component: Structured Argu-
6

MEME: Modeling the Evolutionary Modes of Financial Markets
Table 2: Experiments on 2025 Q4. Performance comparison on three datasets after the LLM knowledge cutoff.
Dataset Method Correlation Metrics (%) Portfolio Metrics
IC↑ ICIR↑ RIC↑ RICIR↑ AR↑ MDD↓ SR↑
SSE 50
LightGBM 2.26 20.33 2.37 22.24 8.10% 4.89% 0.8523
DTML 2.45 15.81 3.24 22.91 5.80% 5.53% 0.5334
FactorV AE 1.79 10.602.8819.85 2.84% 5.28% 0.4998
Master 2.3727.962.48 22.08 6.49% 4.81% 0.6820
SEP 2.30 18.55 1.91 17.30 3.03% 6.06% 0.4120
TradingAgents 2.18 20.06 2.05 18.87 4.18% 5.64% 0.5226
R&D-Agent(Q) 2.58 23.88 2.65 21.80 7.88% 6.10% 0.6851
MEME 2.67 24.35 2.83 26.42 8.25% 4.79% 0.8894
Benchmark Index– – – – 5.66% 4.85% 0.7653
CSI 300
LightGBM 1.16 9.84 3.02 20.54 -2.56% 7.42% -0.2579
DTML 3.44 21.08 4.27 26.47 3.20% 5.01% 0.4789
FactorV AE 2.28 16.62 3.70 21.22 0.99% 5.89% 0.1335
Master 3.47 17.18 3.77 18.13 0.79% 6.16% 0.0924
SEP 1.93 11.72 2.34 14.29 2.06% 5.43% 0.1910
TradingAgents 2.61 15.34 3.07 19.89 4.87% 5.12% 0.4120
R&D-Agent(Q) 4.09 23.01 3.89 26.20 5.42% 5.31% 0.5838
MEME 4.12 32.11 4.53 29.39 9.77% 4.87% 0.7353
Benchmark Index– – – – -0.92% 7.46% -0.0837
CSI 500
LightGBM 2.39 12.24 4.71 28.40 2.39% 8.73% 0.0618
DTML 3.24 20.49 1.89 16.54 14.06% 9.02% 0.6495
FactorV AE 2.23 18.80 3.66 17.75 12.51% 8.75% 0.6122
Master 2.88 20.42 4.65 33.28 19.84% 6.21% 1.1254
SEP 3.01 16.35 3.24 19.49 4.71% 8.96% 0.2427
TradingAgents 3.87 21.64 3.93 28.32 8.22% 8.40% 0.5680
R&D-Agent(Q) 4.38 27.70 4.73 33.59 13.98% 7.22% 0.9606
MEME 5.15 32.61 5.31 34.97 20.56% 5.95% 1.1433
Benchmark Index– – – – 2.88% 10.08% 0.2281
ment Generation (SAG), Modes of Thought (MOT), Proba-
bilistic Modeling (PM), and Temporal Alignment (TA).
The first row establishes a baseline by using the LLM di-
rectly on raw data, which yields the lowest performance
across all datasets and demonstrates the necessity of struc-
tured analysis. Introducing SAG alone provides a perfor-
mance lift on smaller stock pools like SSE 50. However,
its effectiveness diminishes on the larger CSI 500, where
metrics show minimal improvement, suggesting that simply
extracting arguments is insufficient for complex scenarios.
The integration of MOT, even with a deterministic clus-
tering approach, leads to a substantial performance leap,
particularly on the CSI 300 and CSI 500 datasets. This high-
lights the critical role of organizing arguments into coherent
reasoning patterns. Subsequently, replacing the determinis-
tic clustering with our Probabilistic Modeling component
further enhances performance across all datasets. This con-
firms the benefit of modeling the ambiguous relationship
between arguments and their underlying modes of thought.
Finally, adding the Temporal Alignment to form the com-
plete model also brings significant gains. For instance, on
SSE 50, the IC nearly doubles from 3.18 to 6.31, and the
ICIR doubles from 16.95 to 32.99. This result validates the
hypothesis that modeling the lifecycle of thought patterns is
essential for generating robust predictive signals.
4.5. Parameter Sensitivity Analysis
We investigate the sensitivity of MEME to its key hyperpa-
rameters: the number of modes K and the smoothing factor
λ. The analysis is conducted on the CSI 300, and the results
are presented in Figure 3.
Overall, MEME demonstrates robustness to variations in
both parameters, maintaining stable performance across a
considerable range of values.
For the number of modes K, performance degrades when
the value is too small. An insufficientK forces conceptually
distinct arguments into the same mode, which negatively
impacts the quality of the resulting signals. Regarding the
smoothing factor λ, excessively large values also harm per-
formance. As defined in Equation 10, a large λ places
greater weight on the long-term historical performance of
modes relative to their most recent effectiveness. This re-
duces the model’s responsiveness to recent shifts in the
predictive power of the thought patterns, thereby degrading
7

MEME: Modeling the Evolutionary Modes of Financial Markets
Table 3: Ablation study of different components on three datasets. We incrementally add components SAG (Structured
Argument Generation), MOT (Mode Of Thoughts), PM (Probabilistic Modeling), and TA (Temporal Alignment) to evaluate
their contribution to the performance metrics (IC, ICIR, RIC, and RICIR). All Values are in percent.
Components SSE 50 CSI 300 CSI 500
SAG MOT PM TA IC ICIR RIC RICIR IC ICIR RIC RICIR IC ICIR RIC RICIR
✗ ✗ ✗ ✗ 1.87 10.11 1.06 7.89 0.79 6.92 0.94 5.88 0.18 1.68 0.24 3.63
✓ ✗ ✗ ✗ 2.51 12.73 1.92 9.33 3.16 14.40 1.89 8.65 0.21 1.65 0.38 4.70
✓ ✓ ✗ ✗ 2.47 14.66 1.91 10.85 5.30 30.43 5.24 29.36 4.90 38.09 4.87 36.20
✓ ✓ ✓ ✗ 3.18 16.95 3.08 17.38 6.44 38.59 5.61 32.67 5.22 37.14 5.10 34.12
✓ ✓ ✓ ✓ 6.31 32.99 5.48 29.93 6.80 41.71 6.16 39.75 6.72 41.15 6.64 34.75
5 10 15 20 25
Hyperparameter number of modes K
0.03
0.04
0.05
0.06
0.07
0.08IC
CSI 300 (K) CSI 300 ( )
0.3 0.4 0.5 0.6 0.7
Hyperparameter smoothing factor
Figure 3: MEME exhibits a moderate sensitivity.
the final results. More results are provided in Figure 5.
4.6. Cost Time Analysis
We compare the daily average running time of MEME with
SOTA LLM-based baselines. As shown in Figure 6 in the
Appendix, MEME achieves lower computational cost by
filtering noise via structured argument extraction and by
aligning information across assets and trading days through
mode identification and alignment, thereby reducing the
overhead of explicit LLM reflection.
4.7. Case Study
2024-01 2024-04 2024-07 2024-10 2025-01 2025-04 2025-07
0%
20%
40%
60%
80%
100%Normalized Modes Performance (%)
Long-term effective
Bear-market effective
Bull-market effective
Figure 4: Temporal evolution of normalized performance
for different categories of Modes of Thought on the CSI 300.
The stack plot illustrates the dynamic lifecycle and shifting
prevalence of modes across different market conditions.
To investigate the lifecycle and nature of the identified
Modes of Thought, we conduct a case study on the CSI
300 dataset. We track the long-term performance score,
Perf, for each mode as defined in Equation 10. A mode is
considered “effective” on a given day if its Perf is positive,
signifying that it is capturing excess returns according to
Equation 7, 8 and 9. Based on their sustained effectiveness
across distinct market regimes—a bear market (Oct 2023 -
Sep 2024) and a bull market (Sep 2024 - Present)—we clas-
sify modes into four categories: 1) Long-term effective, 2)
Bull-market effective, 3) Bear-market effective, and 4) Inef-
fective. In Appendix A.6, we give the detailed classification
methodology of the above four categories.
Figure 4 presents a temporal analysis of these categories.
The x-axis represents the trading days spanning the entire
study period. The y-axis displays the daily aggregated and
normalized performance share of each category. This is
constructed by applying a Softmax function to the Perf
scores of all modes for a given day. Consequently, the total
height of the stacked plot at any point in time sums to one,
with the area of each colored band representing the relative
performance contribution of its corresponding category to
the collective performance of all active modes.
The visualization reveals several key dynamics. First, a
large portion of modes remain ineffective, indicating that
most emergent investment logics do not consistently gener-
ate alpha. This aligns with the observation that sustained
profitability in financial markets is rare. Second, the com-
position of effective modes evolves with market conditions.
Modes effective in the bear market proved resilient during
the early 2024 liquidity crisis. Conversely, modes effective
in the bull market, which correspond to trend-following and
sentiment-driven logic, gained dominance during the market
rally in late 2024. The former’s underperformance in the bull
market highlights its inability to capture sentiment-driven
premiums. This case study demonstrates MEME’s capac-
ity to identify and track the evolving efficacy of distinct
investment narratives. In Appendix A.6, we give detailed
examples of three categories of effective modes.
8

MEME: Modeling the Evolutionary Modes of Financial Markets
5. Conclusion
In this paper, we introduce MEME, a LLM-based frame-
work for financial trading. MEME leverages a new Strategy-
Centric viewpoint by mining, tracking, and evaluating the
lifecycle of different evolving investment logics. Our ap-
proach gains enhanced performance and stability against
competitive baselines and shows promising robustness and
generalizability under different market regimes.
References
Araci, D. Finbert: Financial sentiment analysis
with pre-trained language models.arXiv preprint
arXiv:1908.10063, 2019.
Blyth, S.An introduction to quantitative finance. Oxford
University Press, 2014.
Cao, L., Xi, Z., Liao, L., Yang, Z., and Cao, Z. Chain-of-
alpha: Unleashing the power of large language models
for alpha mining in quantitative trading.arXiv preprint
arXiv:2508.06312, 2025.
Chen, B., Ding, H., Shen, N., Huang, J., Guo, T., Liu, L.,
and Zhang, M. Alphasage: Structure-aware alpha min-
ing via gflownets for robust exploration.arXiv preprint
arXiv:2509.25055, 2025.
Chen, T., Chen, W., and Du, L. An empirical study of finan-
cial factor mining based on gene expression programming.
In2021 4th International Conference on Advanced Elec-
tronic Materials, Computers and Software Engineering
(AEMCSE), pp. 1113–1117. IEEE, 2021.
DeepSeek-AI. Deepseek-v3 technical report, 2024. URL
https://arxiv.org/abs/2412.19437.
Dempster, A. P., Laird, N. M., and Rubin, D. B. Maximum
likelihood from incomplete data via the em algorithm.
Journal of the royal statistical society: series B (method-
ological), 39(1):1–22, 1977.
Deng, Z. and Wang, J. Alphaquanter: An end-to-end tool-
orchestrated agentic reinforcement learning framework
for stock trading.arXiv preprint arXiv:2510.14264, 2025.
Du, K., Xing, F., Mao, R., and Cambria, E. Financial
sentiment analysis: Techniques and applications.ACM
Computing Surveys, 56(9):1–42, 2024.
Duan, Y ., Wang, L., Zhang, Q., and Li, J. Factorvae: A
probabilistic dynamic factor model based on variational
autoencoder for predicting cross-sectional stock returns.
InProceedings of the AAAI conference on artificial intel-
ligence, volume 36, pp. 4468–4476, 2022.
Duan, Y ., Wang, W., and Li, J. Factorgcl: A hypergraph-
based factor model with temporal residual contrastive
learning for stock returns prediction. InProceedings
of the AAAI Conference on Artificial Intelligence, vol-
ume 39, pp. 173–181, 2025.
Duda, R. O. and Hart, P. E. Pattern classification and scene
analysis.A Wiley-interscience publication, 1973.
Guo, T., Shen, H., Huang, J., Mao, Z., Luo, J., Chen, Z.,
Liu, X., Xia, B., Liu, L., Ma, Y ., et al. Mass: Multi-
agent simulation scaling for portfolio construction.arXiv
preprint arXiv:2505.10278, 2025.
Jonker, R. and V olgenant, A. A shortest augmenting path al-
gorithm for dense and sparse linear assignment problems.
Computing, 38(4):325–340, 1987.
Ke, G., Meng, Q., Finley, T., Wang, T., Chen, W., Ma, W.,
Ye, Q., and Liu, T.-Y . Lightgbm: A highly efficient gradi-
ent boosting decision tree. In Guyon, I., Luxburg, U. V .,
Bengio, S., Wallach, H., Fergus, R., Vishwanathan, S.,
and Garnett, R. (eds.),Advances in Neural Information
Processing Systems, volume 30. Curran Associates, Inc.,
2017. URL https://proceedings.neurips.
cc/paper_files/paper/2017/file/
6449f44a102fde848669bdd9eb6b76fa-Paper.
pdf.
Koa, K. J., Ma, Y ., Ng, R., and Chua, T.-S. Learning to gen-
erate explainable stock predictions using self-reflective
large language models. InProceedings of the ACM Web
Conference 2024, pp. 4304–4315, 2024.
Langley, P. Crafting papers on machine learning.Proceed-
ings of the 17th International Conference on Machine
Learning, pp. 1207–1216, 2000.
Li, J., Liu, Y ., Liu, W., Fang, S., Wang, L., Xu, C., and
Bian, J. Mars: a financial market simulation engine pow-
ered by generative foundation model. InThe Thirteenth
International Conference on Learning Representations,
2025a. URL https://openreview.net/forum?
id=Yqk7EyT52H.
Li, S., Sun, Y ., Lin, Y ., Gao, X., Shang, S., and Yan,
R. Causalstock: Deep end-to-end causal discovery for
news-driven multi-stock movement prediction.Advances
in Neural Information Processing Systems, 37:47432–
47454, 2024a.
Li, T., Liu, Z., Shen, Y ., Wang, X., Chen, H., and Huang, S.
Master: Market-guided stock transformer for stock price
forecasting. InProceedings of the AAAI Conference on
Artificial Intelligence, volume 38, pp. 162–170, 2024b.
9

MEME: Modeling the Evolutionary Modes of Financial Markets
Li, Y ., Yang, X., Yang, X., Xu, M., Wang, X., Liu, W., and
Bian, J. R&d-agent-quant: A multi-agent framework for
data-centric factors and model joint optimization. InThe
Thirty-Ninth Annual Conference on Neural Information
Processing Systems, 2025b.
Li, Z., Song, R., Sun, C., Xu, W., Yu, Z., and Wen, J.-R. Can
large language models mine interpretable financial factors
more effectively? a neural-symbolic factor mining agent
model. InFindings of the Association for Computational
Linguistics ACL 2024, pp. 3891–3902, 2024c.
Lin, H., Zhou, D., Liu, W., and Bian, J. Deep risk model:
a deep learning solution for mining latent risk factors to
improve covariance matrix estimation. InProceedings
of the Second ACM International Conference on AI in
Finance, pp. 1–8, 2021.
Liu, A., Mei, A., Lin, B., Xue, B., Wang, B., Xu, B., Wu,
B., Zhang, B., Lin, C., Dong, C., et al. Deepseek-v3.
2: Pushing the frontier of open large language models.
arXiv preprint arXiv:2512.02556, 2025.
Luo, D., Liao, W., Li, S., Cheng, X., and Yan, R. Causality-
guided multi-memory interaction network for multivari-
ate stock price movement prediction. InProceedings of
the 61st Annual Meeting of the Association for Computa-
tional Linguistics (Volume 1: Long Papers), pp. 12164–
12176, 2023.
McNeil, A. J., Frey, R., and Embrechts, P.Quantitative
risk management: concepts, techniques and tools-revised
edition. Princeton university press, 2015.
Qian, H., Zhou, H., Zhao, Q., Chen, H., Yao, H., Wang,
J., Liu, Z., Yu, F., Zhang, Z., and Zhou, J. Mdgnn:
Multi-relational dynamic graph neural network for com-
prehensive and dynamic stock investment prediction. In
Proceedings of the AAAI Conference on Artificial Intelli-
gence, volume 38, pp. 14642–14650, 2024.
Shi, H., Song, W., Zhang, X., Shi, J., Luo, C., Ao, X.,
Arian, H., and Seco, L. A. Alphaforge: A framework
to mine and dynamically combine formulaic alpha fac-
tors. InProceedings of the AAAI Conference on Artificial
Intelligence, volume 39, pp. 12524–12532, 2025a.
Shi, Y ., Duan, Y ., and Li, J. Navigating the alpha jungle: An
llm-powered mcts framework for formulaic factor mining.
arXiv preprint arXiv:2505.11122, 2025b.
Shi, Y ., Fu, Z., Chen, S., Zhao, B., Xu, W., Zhang, C., and
Li, J. Kronos: A foundation model for the language
of financial markets.arXiv preprint arXiv:2508.02739,
2025c.
Song, L., Li, H., Chen, S., Gan, X., Shi, B., Ma, J., Pan,
Y ., Wang, X., and Shang, X. Multi-scale temporal neural
network for stock trend prediction enhanced by temporal
hyepredge learning.Proceedings of the IJCAI, Montreal,
QC, Canada, pp. 16–22, 2025.
Tang, Z., Chen, Z., Yang, J., Mai, J., Zheng, Y ., Wang,
K., Chen, J., and Lin, L. Alphaagent: Llm-driven alpha
mining with regularized exploration to counteract alpha
decay. InProceedings of the 31st ACM SIGKDD Confer-
ence on Knowledge Discovery and Data Mining V . 2, pp.
2813–2822, 2025.
Team, G., Kamath, A., Ferret, J., Pathak, S., Vieillard,
N., Merhej, R., Perrin, S., Matejovicova, T., Ram ´e, A.,
Rivi`ere, M., et al. Gemma 3 technical report.arXiv
preprint arXiv:2503.19786, 2025a.
Team, K., Bai, Y ., Bao, Y ., Chen, G., Chen, J., Chen,
N., Chen, R., Chen, Y ., Chen, Y ., Chen, Y ., et al.
Kimi k2: Open agentic intelligence.arXiv preprint
arXiv:2507.20534, 2025b.
Tian, F., Salim, F. D., and Xue, H. Tradinggroup: A
multi-agent trading system with self-reflection and data-
synthesis.arXiv preprint arXiv:2508.17565, 2025.
Tong, H., Li, J., Wu, N., Gong, M., Zhang, D., and Zhang, Q.
Ploutos: Towards interpretable stock movement predic-
tion with financial large language model.arXiv preprint
arXiv:2403.00782, 2024.
Xiang, Q., Chen, Z., Sun, Q., and Jiang, R. Rsap-dfm:
Regime-shifting adaptive posterior dynamic factor model
for stock returns prediction. InProceedings of the Thirty-
Third International Joint Conference on Artificial Intel-
ligence, IJCAI-24. International Joint Conferences on
Artificial Intelligence Organization, 2024.
Xiao, Y ., Sun, E., Chen, T., Wu, F., Luo, D., and Wang,
W. Trading-r1: Financial trading with llm reasoning via
reinforcement learning.arXiv preprint arXiv:2509.11420,
2025a.
Xiao, Y ., Sun, E., Luo, D., and Wang, W. Tradingagents:
Multi-agents llm financial trading framework. InThe
First MARW: Multi-Agent AI in the Real World Workshop
at AAAI 2025, 2025b.
Xu, W., Liu, W., Wang, L., Xia, Y ., Bian, J., Yin, J., and Liu,
T.-Y . Hist: A graph-based framework for stock trend fore-
casting via mining concept-oriented shared information.
arXiv preprint arXiv:2110.13716, 2021.
Yang, A., Li, A., Yang, B., Zhang, B., Hui, B., Zheng, B.,
Yu, B., Gao, C., Huang, C., Lv, C., et al. Qwen3 technical
report.arXiv preprint arXiv:2505.09388, 2025.
10

MEME: Modeling the Evolutionary Modes of Financial Markets
YANG, Y ., Zhang, Y ., Wu, M., Zhang, K., Zhang, Y .,
Yu, H., Hu, Y ., and Wang, B. Twinmarket: A scal-
able behavioral and social simulation for financial mar-
kets. InThe Thirty-ninth Annual Conference on Neural
Information Processing Systems, 2025. URL https:
//openreview.net/forum?id=h60y6zlPyl.
Yoo, J., Soun, Y ., Park, Y .-c., and Kang, U. Accurate mul-
tivariate stock movement prediction via data-axis trans-
former with multi-level contexts. InProceedings of the
27th ACM SIGKDD Conference on Knowledge Discovery
& Data Mining, pp. 2037–2045, 2021.
Yu, S., Xue, H., Ao, X., Pan, F., He, J., Tu, D., and He,
Q. Generating synergistic formulaic alpha collections via
reinforcement learning. InProceedings of the 29th ACM
SIGKDD Conference on Knowledge Discovery and Data
Mining, pp. 5476–5486, 2023.
Zhang, W., Zhao, L., Xia, H., Sun, S., Sun, J., Qin, M.,
Li, X., Zhao, Y ., Zhao, Y ., Cai, X., et al. A multimodal
foundation agent for financial trading: Tool-augmented,
diversified, and generalist. InProceedings of the 30th
acm sigkdd conference on knowledge discovery and data
mining, pp. 4314–4325, 2024a.
Zhang, W., Zhao, Y ., Sun, S., Ying, J., Xie, Y ., Song, Z.,
Wang, X., and An, B. Reinforcement learning with mask-
able stock representation for portfolio management in
customizable stock pools. InProceedings of the ACM
Web Conference 2024, pp. 187–198, 2024b.
Zhang, X., Huang, Z., Wu, Y ., Lu, X., Qi, E., Chen, Y .,
Xue, Z., Wang, Q., Wang, P., and Wang, W. Multi-period
learning for financial time series forecasting. InProceed-
ings of the 31st ACM SIGKDD Conference on Knowledge
Discovery and Data Mining V . 1, pp. 2848–2859, 2025a.
Zhang, Y ., Li, M., Long, D., Zhang, X., Lin, H., Yang, B.,
Xie, P., Yang, A., Liu, D., Lin, J., Huang, F., and Zhou,
J. Qwen3 embedding: Advancing text embedding and
reranking through foundation models.arXiv preprint
arXiv:2506.05176, 2025b.
Zhao, Y ., Du, H., Liu, Y ., Wei, S., Chen, X., Zhuang, F., Li,
Q., and Kou, G. Stock movement prediction based on
bi-typed hybrid-relational market knowledge graph via
dual attention networks.IEEE transactions on knowledge
and data engineering, 35(8):8559–8571, 2022.
Zheng, X., Liu, M., and Zhu, M. Deep hashing-based
dynamic stock correlation estimation via normalizing
flow. InIJCAI, pp. 4993–5001, 2023.
Zhu, H., Liu, S.-Y ., Zhao, P., Chen, Y ., and Lee, D. L. Fore-
casting asset dependencies to reduce portfolio risk. In
Proceedings of the AAAI Conference on Artificial Intelli-
gence, volume 36, pp. 4397–4404, 2022.
Zhu, Z. and Zhu, K. Alphaqcm: Alpha discovery in fi-
nance with distributional reinforcement learning. InForty-
second International Conference on Machine Learning,
2025.
11

MEME: Modeling the Evolutionary Modes of Financial Markets
A. Appendix
A.1. Pseudocode of MEME
Algorithm 1:MEME
Input:Raw multi-modal data{D t}t∈T , historical prices{P t}t∈T , number of modesK, EMA factorλ
Output:Sequence of daily portfolios{W t}t∈T
Initialize long-term performance scores Perf0,k ←0fork= 1, . . . , K;
Initialize mode parameters for day 0, Modes0 ← ∅;
foreach trading dayt∈Tdo
// --- Stage 1: Argument Extraction ---
Extract structured arguments{A t,s,i}s,i from raw dataD t via Eqs. (1-3);
// --- Stage 2: Mode Identification and Alignment ---
Encode arguments to get embeddings{x t,s,i}via Eq. (4);
Fit GMM on{x t,s,i}to identify daily modes Modes t ={M t,k}K k=1 and responsibilities{ω t,s,i};
ift >0then
// Align today’s modes with yesterday’s
Find permutationπ t by aligning centroids of Modest and Modest−1 via Eq. (6);
// --- Stage 3.1: Mode Evaluation (Backward-looking) ---
// Update performance scores using t-1’s predictions and t’s returns
Calculate aggregated score AggScoret−1,k for each mode from dayt−1via Eqs. (7-9);
Update long-term performance Perft−1,k using Perft−2 andπ t−1 via EMA in Eq. (10);
// --- Stage 3.2: Portfolio Construction (Forward-looking) ---
// Generate trading signals for day t using updated scores
Calculate predicted score [Score(At,s,i)for each new argument via Eqs. (11-12) using Perf t−1;
Aggregate argument scores into a final stock signal Signalt,s via Eq. (13);
Construct portfolioW t based on a Top-K ranking of Signalt;
else
Wt ←EqualWeighted Portfolio
returnSequence of daily portfolios{W t}t∈T ;
A.2. Implementation details of Argument Extraction
A.2.1. IMPLEMENTATION DETAILS OFFILTERAGENT
System & User Prompts
System prompts
You are an expert on financial market analysis, portfolio management and quantitative
trading. Strictly follow the user’s requirements to generate sound, logical and
detailed responses. Your ouput should only contain a JSON object. Do not include any
explanations, addditional text, notes, code block markers like ‘‘‘ or ‘‘‘json.
User prompts for Information Filtering.
Context: You are part of an automated investment analysis framework. Your analysis
will serve as a primary input for a downstream synthesis agent. The goal is to reduce
noise and provide a clear, factual summary of the current situation for[Asset Name]
([Asset Ticker])as of[Analysis Date].
Input Data:
You will be provided with raw [Modality Name] data. [Raw Data for the specified
modality, e.g., a table of fundamental ratios, a list of recent news headlines, or a
time-series of technical indicators]
Task: 1.Analyze: Thoroughly review the provided raw data.
2.Identify Salience: Identify the most salient points, patterns, and anomalies that
could materially impact the asset’s future price performance. Disregard trivial or
redundant information.
3.Summarize: Distill your findings into a concise, structured summary. The
12

MEME: Modeling the Evolutionary Modes of Financial Markets
summary must be objective and based strictly on the provided data.
Constraints:
1. Focus exclusively on the provided data. Do not introduce external information or
make speculative predictions.
2. The output must be a factual distillation, not a final investment recommendation.
3. Present the information in a clear, structured format using the specified headings.
Output Format:
{
"Modality name": [Modality Name],
"Analysis summary": "...",
"Asset code": [Asset Ticker]
}
A.2.2. IMPLEMENTATION DETAILS OFGENERATORAGENT
System & User Prompts
User prompts for Argument Generation.
Context: You have received concise, pre-filtered intelligence reports for [Asset
Name] ([Asset Ticker]) as of [Analysis Date]. Your task is to look for confluence or
divergence between these reports to construct distinct lines of reasoning for either a
bullish or bearish stance.
Input Data:
You will be provided with a collection of structured summaries from different
analytical perspectives.
1.Fundamental Analysis Summary:[fundamental output]
2.Technical Analysis Summary:[technical output]
3.Narrative Analysis Summary:[news output]
Task:
1.Synthesize: Review all provided analysis summaries. Identify distinct lines
of reasoning by connecting facts across different reports. A single fact is not an
argument; a synthesis of facts is.
2.Formulate Arguments: For each distinct line of reasoning, construct a structured
investment argument. An argument can be supported by evidence from one or more of the
analytical summaries.
3.Assign Stance: Clearly define each argument as either bullish or bearish.
Constraints:
1. The output must be a list of structured JSON objects.
2. Each argument must be a self-contained, logical thesis.
3. The ‘rationale‘ should be your own synthesized conclusion, not a direct copy of the
input.
4. The ‘evidence‘ must be a direct quote or a close, factual paraphrase of the key
observations from the input summaries that support your rationale.
Output Format:
Produce a valid JSON array of argument objects. Each object must conform to the
following schema:
{
"p": 1 for bullish. -1 for bearish,
"a": "argument analytical rationale",
"e": "argument evidence"
}
A.3. Dataset composition details
A.3.1. STOCK POOL DETAILS
• SSE 50: This index represents the 50 largest and most liquid A-share stocks on the Shanghai Stock Exchange. It
captures the performance of leading blue-chip companies.
• CSI 300: This index is a broad market benchmark for China’s A-share market. It consists of the 300 largest and
most liquid stocks from both the Shanghai and Shenzhen exchanges, offering a comprehensive representation of the
large-cap segment.
13

MEME: Modeling the Evolutionary Modes of Financial Markets
• CSI 500: This index tracks the performance of the next 500 largest and most liquid A-share stocks after the constituents
of the CSI 300. It primarily reflects the behavior of mid and small-cap companies, providing a distinct universe from
the large-cap focused indices.
A.3.2. DATASET CONSTRUCTION DETAILS
Fundamental Modality
• Financial Statements, including Income Statement, Balance Statement, CashFlow Statement
• Valuation Metrics, including Price-to-Earnings Ratio, Price-to-Book Ratio, Price-to-Cash Flow Ratio, Price-to-Sales
Ratio, and dividend Ratio.
News Modality
• News collected from Wind 1.
• Financial Report Collected from EastMoney 2.
Technical Modality
•Price and Volume Series: Daily, weekly, and monthly adjusted close prices, trading volumes, and market cap.
•Technical Indicators:
–Trend-following: Daily, weekly, and monthly moving averages.
– Momentum: Daily, weekly, and monthly Moving Average Convergence Divergence (MACD) and Relative
Strength Index (RSI).
–V olatility: Daily, weekly, and monthly Bollinger Bands (BOLL).
–Oscillators: Daily, weekly, and monthly Stochastic Oscillator (KDJ).
•Contextual Metadata: The primary industry classification for each stock.
•Benchmark Data: Daily price series for the corresponding industry indices.
A.4. Performance Metrics Details
We assess the performance of a predictive model denoted by f. At each time step t, for a universe of Nt assets, the model
generates a vector of predictive scores st ∈R Nt. The efficacy of these scores is measured against the vector of subsequent
asset returns rt ∈R Nt. Unless specified otherwise, all statistical moments such as expectation E[·], variance Var[·], and
covarianceCov[·,·]are computed cross-sectionally over the asset universe at timet.
The fundamental measure of predictive accuracy is the daily cross-sectional Pearson correlation between the scores and
returns.
ρt = Cov(st,r t)p Var(st) Var(rt) (14)
For portfolio-based metrics, we simulate a strategy where the daily portfolio return, Rp t , is constructed from the factor scores
st. The cumulative wealth over a period of T time steps is given by WT = QT t=1(1 +Rp t ). Let A be the number of trading
periods in a year, e.g.,A= 252for daily data, and letr t,f be the risk-free rate.
Information CoefficientThe Information Coefficient (IC) measures the time-series average of the daily cross-sectional
correlations, quantifying the mean predictive power of the factor.
IC=E t[ρt](15)
1https://www.wind.com.cn/
2https://data.eastmoney.com/report/
14

MEME: Modeling the Evolutionary Modes of Financial Markets
Information RatioThe Information Ratio (IR) evaluates the consistency of the factor’s predictive power. It is the
time-series mean of the daily correlations scaled by their standard deviation, thus rewarding stable performance.
IR= Et[ρt] Stdt(ρt) (16)
Rank Information CoefficientThe Rank Information Coefficient (Rank IC) is the time-series average of the daily
Spearman rank correlations. It assesses the model’s ability to correctly order assets by predicted performance and is robust
to outliers and non-linear monotonic relationships.
Rank IC=E t[Corr(rank(st),rank(r t))](17)
Rank Information RatioThe Rank Information Ratio (Rank IR) measures the stability of the factor’s ordinal predictive
power over time.
Rank IR= Et[Corr(rank(st),rank(r t))] Stdt(Corr(rank(st),rank(r t))) (18)
Annualized ReturnThe Annualized Return (AR) represents the total return of the factor-induced portfolio scaled to a
one-year period.
AR=A·E t[Rp t ](19)
Maximum DrawdownThe Maximum Drawdown (MDD) quantifies the largest peak-to-trough decline in the portfolio’s
cumulative wealth, serving as a critical measure of tail risk.
MDD= max
t≤T

1− Wt
maxu≤t Wu

(20)
Sharpe RatioThe annualized Sharpe Ratio (SR) measures the risk-adjusted excess return of the portfolio. It is defined as
the annualized ratio of the average excess return to the standard deviation of excess returns.
SR= Et[Rp t −r t,f ] Stdt(Rp t −r t,f ) · √ A(21)
A.5. Baseline Details
We conduct experiments on various SOTA baselines:
Machine Learning Approaches
• LightGBM (Ke et al., 2017): A high-efficiency, leaf-wise gradient boosting decision tree framework by Microsoft
research. We utilize the offical python package 3 to implement it.
Deep Learning Approaches
• DTML: DTML (Yoo et al., 2021) presents an innovative attention-based architecture designed to capture intricate
inter-stock correlations for investment decision-making. Our implementation is based on the official publicly available
code4.
• FactorV AE: We include FactorV AE (Duan et al., 2022), an influential probabilistic dynamic factor model that leverages
a variational autoencoder framework. The implementation is adapted from the open-source repository5.
• MASTER: MASTER (Li et al., 2024b) is a powerful Transformer-based model for stock price forecasting. It adeptly
models both contemporaneous and temporal stock correlations while integrating market-wide information to guide
feature selection. We utilize the authors’ provided implementation6.
3https://github.com/microsoft/LightGBM
4https://github.com/ceteris11/DTML
5https://github.com/x7jeon8gi/FactorVAE
6https://github.com/SJTU-DMTai/MASTER
15

MEME: Modeling the Evolutionary Modes of Financial Markets
5 10 15 20 25
Hyperparameter number of modes K
0.03
0.04
0.05
0.06
0.07
0.08RIC
CSI 300 (K) CSI 300 ( )
0.3 0.4 0.5 0.6 0.7
Hyperparameter smoothing factor
Figure 5: MEME exhibits a moderate sensitivity to changes in hyperparameters on RIC.
SSE 50 CSI 300 CSI 500
Dataset
0
400
800
1200
1600
2000
2400Runtime (seconds)
SEP Trading Agents Ours
Figure 6: Average Daily running time on MEME and two LLM-based SOTA baselines.
Agent-Based Approaches
• SEP: SEP (Koa et al., 2024) introduces a novel agent-based approach where a verbal self-reflective agent, trained with
Proximal Policy Optimization, learns to generate explainable predictions for individual stocks. We build our tests upon
the official open-source code7.
• TradingAgents: TradingAgents (Xiao et al., 2025b) offers a sophisticated multi-agent framework that constructs
investment portfolios by simulating the collaborative dynamics within trading firms. Our experiments leverage the
publicly accessible implementation8.
• R&D-Agent(Q):R&D-Agent(Q) (Li et al., 2025b) is a pioneering LLM-driven framework designed for collaborative
factor model development in quantitative finance. For this baseline, we employ the official implementation provided by
the authors9.
7https://github.com/koa-fin/sep
8https://github.com/TauricResearch/TradingAgents
9https://github.com/microsoft/RD-Agent
16

MEME: Modeling the Evolutionary Modes of Financial Markets
A.6. Detailed examples of effective modes
A.6.1. CLASSIFICATION OF MODES
• Long-term effective:Across both bull and bear markets, the selected mode exhibits positive values in Equation 10 for
over 65% of the observed periods.
• Bull-market effective: the selected mode is not long-term effective, and exhibits positive values in Equation 10 for over
70% of the bull-market periods.
• Bear-market effective: the selected mode is not long-term effective and bull-market effective, and exhibits positive
values in Equation 10 for over 70% of the bear-market periods.
• Non-effective: None of the above.
A.6.2. LONG-TERM EFFECTIVE MODES
Modes example & summary
Modes examples
{"converted arguments": [
{"code": "000001.SZ",
"name": "Ping An Bank",
"date": "2024-01-30",
"argument":{
"p": 1, "a": "The stock is significantly undervalued with substantial potential for
mean reversion.", "e": "Based on a relative valuation and historical quantile analysis
framework, the current P/E ratio of 3.80 is only above the 2.8th percentile of its
historical data, far below the median of 8.84. Similarly, the P/B ratio of 0.40 is
at the 2.8th percentile, below the median of 0.82, indicating significant room for
valuation recovery."
}},
{"code": "000895.SZ",
"name": "Henan Shuanghui Investment & Development", "date": "2024-06-25",
"argument":{
"p": 1,
"a": "The inventory management strategy is poised to enhance profitability.",
"e": "Based on the company’s statement on optimizing frozen goods inventory to
maximize returns, combined with industry data showing a month-over-month contraction
in hog production, this cost control optimization is expected to directly improve the
gross profit margin."}},
{"code": "603259.SH",
"name": "WuXi AppTec",
"date": "2024-07-08",
"argument":{"p": 1,
"a": "Utilizing a model that links buyback activities with shareholder confidence, the
cancellation of stock options sends a positive signal.",
"e": "WuXi AppTec’s announcement on July 1st to cancel 31,500 stock options, viewed
in the context of over 1,600 A-share companies conducting nearly 100 billion RMB in
buybacks in the first half of the year, reflects the management’s proactive stance on
supporting the company’s valuation."
}},
{"code": "000725.SZ",
"name": "BOE Technology Group A",
"date": "2025-05-27",
"argument":{
"p": -1,
"a": "Intensifying industry competition and capital expenditure pressures are likely
to weigh on short-term performance.",
"e": "A competitive landscape analysis reveals that competitors like HKC and Tianma
have signed new display projects totaling 72 billion RMB for mass production. This
17

MEME: Modeling the Evolutionary Modes of Financial Markets
acceleration in industry capacity expansion means BOE Technology will face heightened
challenges from price competition and market integration."
}},
{"code": "601138.SH",
"name": "Foxconn Industrial Internet",
"date": "2025-04-12",
"argument":
"p": 1,
"a": "Earnings growth is the primary driver for stock price appreciation.",
"e": "According to a performance-driven analytical framework, the company’s net profit
for the first quarter grew by 24%-27% year-over-year, with revenue increasing by
34%-35.6%, setting a new record for the period. This high-growth data substantiates
expectations for an upward trajectory in the stock price."
}}
],}
Modes summaries
The overarching mode of thought is a multi-faceted, evidence-based reasoning process.
It synthesizes diverse data from quantitative metrics and corporate actions to industry
trends|through specific analytical frameworks to construct a structured investment
thesis on a stock’s future performance.
A.6.3. BULL-MARKET EFFECTIVE MODES
Modes example & summary
Modes examples
{"converted arguments": [
{"code": "000063.SZ",
"name": "ZTE Corporation",
"date": "2024-01-30",
"argument":{
"p": -1, "a": "The trend has deteriorated on a weekly basis, confirming the
continuation of a mid-term downtrend.",
"e": "The weekly closing price of 20.78 has fallen below the Bollinger Band middle
rail of 25.73, the RSI has dropped sharply to 30.9, and the negative MACD value has
widened to -0.62."
}},
{"code": "688256.SH",
"name": "Cambricon Technologies", "date": "2025-07-30",
"argument":{
"p": 1,
"a": "A monthly-level breakout above the upper Bollinger Band, coupled with an
overbought RSI, indicates strong upward momentum.",
"e": "Based on trend continuation logic, the recent monthly closing price of 1492.49
is significantly above the upper Bollinger Band of 1127.98, and the monthly RSI has
reached 84.26, confirming a clear breakout pattern."}},
{"code": "600519.SH",
"name": "Kweichow Moutai",
"date": "2024-05-06",
"argument":{"p": 1,
"a": "The stock is exhibiting a strong short-term technical breakout, suggesting the
price is likely to continue rising.",
"e": "Based on a bullish moving average alignment framework, the daily closing
price has stayed above all short-term moving averages (5-day, 10-day, 20-day) for
three consecutive days, and the 5-day MA has crossed above the 10-day and 20-day MAs,
indicating strong short-term upward momentum."
}},
{"code": "688981.SH",
18

MEME: Modeling the Evolutionary Modes of Financial Markets
"name": "SMIC",
"date": "2025-07-30",
"argument":{
"p": 1,
"a": "The short-term stock price is poised to benefit from institutional capital
inflows and positive market sentiment.",
"e": "Margin financing net purchases on July 29th reached a two-month high of 164
million RMB, and the margin financing balance ratio rose to 4.01% on July 30th.
Concurrently, recommendations from Minsheng Securities and Everbright Securities as
a top pick for August signal strong institutional optimism.."
}},
{"code": "603986.SH",
"name": "GigaDevice Semiconductor",
"date": "2025-04-12",
"argument":
"p": 1,
"a": "The stock price is likely to increase, as inferred from financing activities and
capital flow dimensions.",
"e": "A net margin financing purchase of 65.38 million RMB on June 30th marked the
fourth consecutive day of net purchases, indicating active capital inflow from the
market and reflecting strengthening investor confidence."
}}
],}
Modes summaries
This thinking mode prioritizes technical analysis and market sentiment. It interprets
chart patterns, momentum indicators (RSI, MACD), and capital flows (margin financing)
as direct predictors of short-term price movements, inferring investor conviction and
forecasting trend continuation or reversal based on these signals.
A.6.4. BEAR-MARKET EFFECTIVE MODES
Modes example & summary
Modes examples
{"converted arguments": [
{"code": "600941.SH",
"name": "China Mobile",
"date": "2024-01-30",
"argument":{
"p": 1, "a": "An attractive dividend yield provides downside protection and enhances
investment appeal.",
"e": "Utilizing a yield analysis framework, the dividend yield stands at 4.15%,
surpassing the industry average of 2.44%. The company’s abundant cash flow, with cash
and equivalents consistently exceeding 3.3 trillion RMB and no interest-bearing debt,
supports the sustainability of its dividend policy."
}},
{"code": "601816.SH",
"name": "Beijing-Shanghai High-Speed Railway", "date": "2024-06-27",
"argument":{
"p": 1,
"a": "The implementation of a cash dividend may attract stable, yield-seeking capital
inflows.",
"e": "Based on a dividend event-driven analysis, the company’s execution of a cash
dividend of 1.12 RMB per 10 shares, with the record date completed on June 27th,
highlights its prominent high-dividend characteristic."}},
{"code": "688981.SH",
"name": "SMIC",
"date": "2024-05-12",
"argument":{"p": -1,
"a": "Deteriorating cash flow combined with a lack of dividends diminishes investment
19

MEME: Modeling the Evolutionary Modes of Financial Markets
attractiveness and may lead to valuation pressure.",
"e": "Through P/CF and dividend yield analysis, the company’s cash flow return
is insufficient. The P/CF ratio of 14.55 is above its historical 36th percentile
while cash and equivalents have declined. The 0% dividend yield presents a clear
disadvantage compared to the industry’s average yield.."
}},
{"code": "601012.SH",
"name": "LONGi Green Energy",
"date": "2025-04-24",
"argument":{
"p": -1,
"a": "The balance sheet reveals growing financial pressure, which constrains potential
stock price appreciation.",
"e": "Cash and equivalents have decreased while total debt remains high, causing the
debt-to-asset ratio to rise to 0.592. Persistently high levels of accounts receivable
and inventory signal pressure on operational efficiency."
}},
{"code": "600900.SH",
"name": "China Yangtze Power",
"date": "2025-08-27",
"argument":
"p": 1,
"a": "The stock price is likely to increase, as inferred from financing activities and
capital flow dimensions.",
"e": "Applying dividend and cash flow analysis, the current dividend yield of 3.41%
is above the industry’s 2.67%, and a P/CF ratio of 11.38 below its historical median
indicates a reasonable valuation. An improving financial structure, seen in the
reduced debt-to-asset ratio, enhances dividend sustainability."
}}
],}
Modes summaries
This thinking mode prioritizes financial health and shareholder returns. It assesses
a company’s intrinsic value and risk profile by analyzing balance sheet strength, cash
flow generation, and dividend policies, viewing a strong dividend and stable financials
as key indicators of investment quality and downside protection.
20
