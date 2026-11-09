---
title: Enhanced Trading Systems with Intelligent Market Analysis
url: https://arxiv.org/abs/2610.13998
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Vedanth Padmaraman
- Shreen Anand
- Vamshi Vishruth J
- Vineet V Pai
- Arvind Srinath K. T
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.13998
pages: 9
chars: 32074
fetched_at: '2026-11-08T13:29:14+00:00'
kb_version: 1
---

# Enhanced Trading Systems with Intelligent Market Analysis

ENHANCED TRADING SYSTEMS WITH
INTELLIGENT MARKET ANALYSIS
1 Vedanth Padmaraman, 1 Shereen Anand, 1 Vamshi Vishruth J, 1 Vineet V Pai,
2 Arvind Srinath K.T, 2 Dr. Subramanyam Natarajan, 1 Dr. Shylaja S S
1 Department of Computer Science and Engineering, PES University, Bengaluru, India
2 Key Resource Person, Bengaluru, India
Email: vedanthpadmaraman0566@gmail.com, shreenanand@gmail.com, vamshivishruthj@gmail.com,
ho75vineet@gmail.com,
shylajass@pesu.edu, arvind.srinath@gmail.com, natarajan@pes.edu
Abstract:This paper proposes a hybrid reinforcement learning trading framework integrating intraday mar-
ket data with transformer-based financial sentiment signals. The system extracts sentiment dynamics and
semantic event clusters from financial news and incorporates them into a PPO-based trading agent. Experi-
ments on intraday NSE data demonstrate improved risk-adjusted returns compared to price-only baselines.
Index T erms:Reinforcement learning, Sentiment analysis, FinBERT, ONNX, Algorithmic trading, PPO,
Intraday trading, Curriculum learning.
1 Introduction
The present-day financial markets are understood
not only by numerical signals such as price and vol-
ume but also by textual narratives such as news,
analyst notes, social networks, etc. Standard algo-
rithmic trading approaches handle these signals sep-
arately. This study bridges them by (1) use of the
FinBERT pipeline with fallback lexicon scoring to
extract textual sentiment, (2) deriving higher-order
sentiment dynamics (velocity, acceleration, correla-
tion), and (3) training RL agents across a controlled
curriculum to exploit these signals together with nu-
merical signals.
This work develops a hybrid trading framework
that uses the dynamics associated with textual
data and news embedding-based structure in the
decision-making process of reinforcement learning
(RL) agents. Our objective was to establish the
methodological foundations required to (i) extract
temporally aligned sentiment features, (ii) quan-
tify sentiment evolution through physically inspired
derivatives, and (iii) evaluate whether such features
contain predictive structure that can be exploited by
RL agents.
Our contributions:
1. A module that synchronized OHLCV data with
asynchronous signals from news data, including
clustering/de-duplication.
2. Formulated MDP designs for multi-RL environ-
ment tiers, including observation/action spaces
and reward engineering that explicitly inte-
grates sentiment.
3. A practical PPO training procedure with train-
ing, checkpoint, and logs.
4. Detailed experimental plan, metrics tests, and
reproducibility checklist.
Here, we introduce two categories of textual sig-
nals along with the numerical indicators.
Sentiment velocity:In addition to raw senti-
ment scores, sentiment velocity (the first-order tem-
poral derivative of sentiment, representing the rate
of sentiment change) and sentiment acceleration (the
derivative of sentiment velocity) were calculated.
These higher-order features aim to capture the mo-
mentum of market narratives, and therefore assess
the rapid shifts that could occur in market sentiment
by judging the textual tone, and hence anticipate
subsequent actions to be taken by the self-trading
agent to achieve higher returns.
Embedding-driven news structure:Dense se-
mantic embeddings for each news article were con-
structed, and exploratory clustering was performed
to identify groups of thematically related events.
Preliminary analysis using future return windows of
different timeframes (1 hour, 4 hours, 1 day, 3 days)
revealed that certain clusters exhibit consistent di-
rectional impacts on returns. However, substantial
event duplication bias was also identified, where clus-
ters were dominated by near-identical articles sur-
rounding a single financial/corporate event, artifi-
cially inflating the predictive signals backed by the
clusters.
To mitigate this, we followed a rigorous de-biasing
pipeline:
1. De-duplicated articles into canonical events.
2. Re-clustered events using HDBSCAN and K-
Means with cluster-size constraints.
3. Transitioned from sign-based return analysis to
quantile-binned returns with bootstrap confi-
dence intervals.
1
arXiv:2610.13998v1  [cs.LG]  27 Sep 2026

4. Computed permutation-based significance tests
and Spearman information coefficients.
5. Generated event-study and horizon-wise
heatmaps to evaluate the robustness of cluster
signals. This process isolated only those clus-
ters whose return patterns generalized beyond
single-event artifacts.
The validated textual features, sentiment deriva-
tives, statistically reliable cluster indicators, and
news-event embeddings were then integrated into
three progressively expressive RL environments,
which were designed to test whether policy perfor-
mance improves when agents have access to higher-
order market narratives. We formalized Markov
Decision Processes (MDPs), developed sentiment-
aware reward shaping functions, and trained agents
using Proximal Policy Optimization (PPO) with
a portfolio-state-aware policy wrapper. Experi-
ments on intraday datasets (e.g., BHEL, Jan–Jul
2020) demonstrated that incorporating these tex-
tual signals yielded measurable gains in return, risk-
adjusted metrics, and stability under curriculum
training.
2 Related Work
This work was synthesized from incremental
work along three related research strands: (i)
reinforcement-learning (RL) methods for algorith-
mic and intraday trading, (ii) financial sentiment
analysis including transformer-based models and lex-
icon methods, and (iii) multimodal/hybrid decision
approaches that aimed at combining numeric mar-
ket data with textual signals. We contextualize the
representative previous work, highlight common lim-
itations, and identify the gaps our paper addresses
along each of the strands.
2.1 Reinforcement Learning for Trad-
ing
The research thus far along this path treated trad-
ing as a sequential decision problem and utilized
RL to learn trading policies directly from market
data. Frameworks such asFinRLprovide modular
environments, state/action abstractions, and stan-
dard algorithms for single-asset and portfolio prob-
lems [5]. Recent algorithmic advances emphasize
instability-aware training, risk-sensitive objectives,
and architectures suited to intraday tasks: for exam-
ple,DeepScalperproposed an architecture tailored
to fleeting intraday opportunities, combining fine-
grained action branching, temporal encoders, and
auxiliary risk targets to balance profit and volatil-
ity [12]. More recently, mixture-of-actor approaches
employed multiple specialized policies (actors) and
optimal transport or other regularizers to differenti-
ate market regimes and allocate learning resources
more effectively [10]. These RL works demonstrate
that carefully designed environments, reward for-
mulation, and architectures affect intraday perfor-
mance, and the agent can adapt to different such
patterns.
Limitations.Despite their strengths, the major-
ity of RL-for-trading research relies predominantly
on numeric inputs (prices, volumes, order-book fea-
tures, technical indicators). This numeric focus
makes it difficult for such agents to anticipate ex-
ternal information shocks originating from textual
sources (news, disclosures, social commentary) that
can materially affect short-term price dynamics.
2.2 Financial Sentiment Analysis and
LLMs
Financial sentiment modeling has advanced from
lexicon-based scoring to transformer-based models,
either pre-trained or fine-tuned on finance-related
data. Models such as FinBERT and similar domain-
tuned transformers produce more accurate polar-
ity and intensity estimates for financial text than
generic models or lexicons [14]. More recent work ex-
plores aligning large language models (LLMs) with
human instructions and market feedback, combining
instruction tuning, retrieval augmentation, and re-
inforcement or feedback loops to improve sentiment
signals that better reflect market reactions [11]. Em-
pirical studies showed that LLM-derived sentiment
can correlate with subsequent returns and be useful
for supervised prediction or rule-based strategies.
Limitations.Prior sentiment-based work typi-
cally stops short of integrating these signals with
other principled RL decision frameworks. Moreover,
many studies treated sentiment as a static score at
an article timestamp, rarely exploiting higher-order
temporal derivatives (e.g., velocity/acceleration) or
addressing clustering and event-duplication biases
that can inflate apparent predictive power. The
asynchronous nature of news relative to high-
frequency OHLCV data and the problem of near-
duplicate reporting were often, but not system-
atically, addressed in downstream decision experi-
ments.
2.3 Multimodal and Hybrid Decision
Systems
There is growing interest in combining multiple
modalities (numeric and textual) for financial pre-
diction. Several supervised and hybrid methods fuse
sentiment features with price/technical indicators
for return forecasting or risk estimation. A smaller
set of works attempts to incorporate textual signals
into trading strategies or RL environments, demon-
strating improved performance in some settings.
However, many such attempts were exploratory:
they do not (i) provide rigorous statistical de-biasing
2

of news clusters, (ii) formalize MDPs that explic-
itly accommodate asynchronous textual events, or
(iii) evaluate the contribution of structured textual
derivatives (velocity, acceleration) and embedding-
cluster signals under robust inference (bootstrap
CIs, permutation tests, information coefficients).
Limitations and open gaps.Existing hy-
brid approaches rarely combine the following
elements in one methodological pipeline: de-
duplication of events, embedding-based event clus-
tering with cluster-level inference, higher-order sen-
timent derivatives, and a reproducible RL experi-
mentation protocol (MDP formalization, curriculum
training, ablation studies). Consequently, there ex-
ists a lack of clarity on when and how text-derived
features truly add sequential decision value beyond
price-only baselines.
2.4 Positioning and Contributions
Against this backdrop, our paper makes a method-
ological proof-of-concept contribution rather than
presenting a deployment system. Concretely, we (i)
compute and validatesentiment derivatives(veloc-
ity and acceleration) as candidate predictive features
across multiple forward horizons, (ii) construct a de-
biased event representation pipeline (near-duplicate
de-duplication, embedding clustering, cluster ro-
bustness testing), and (iii) integrate the validated
textual features into formally defined RL environ-
ments with sentiment-aware observation and reward
structures. By combining rigorous statistical vali-
dation of textual signals with principled MDP and
curriculum design, our approach aims to fill the gap
between sentiment-centered predictive work and RL-
based trading research. We therefore position our
contribution as an incremental but nontrivial exten-
sion of the RL trading literature — one that intro-
duces multimodal, statistically validated textual fea-
tures into the RL decision loop.
3 Dataset and Preprocessing
This section describes the construction of the mul-
timodal dataset used for training and evaluating
our hybrid trading agents. We integrated high-
frequency OHLCV market data with timestamped
financial news by applying a unified preprocess-
ing pipeline to ensure temporal consistency, repro-
ducibility, and statistical reliability. All signals used
by the RL agents—including technical indicators,
sentiment scores, sentiment derivatives, and clus-
ter/event features—were calculated from scratch us-
ing our own processing scripts.
3.1 Market Data
We collect intraday OHLCV data for two actively
traded Indian equities:BHELandJSW Infras-
tructure. Data were scraped at a resolution of
1 minute from March 2025 to August 2025. Each
per-instrument file contains the canonical schema:
timestamp, open, high, low, close, volume.
Data integrity checksinclude:
•Strict chronological ordering and duplicate-
timestamp removal,
•Normalizing timezone to IST (UTC+5:30),
•Removal of non-market-hour records,
•Sanity checks on volume spikes, outliers, and
malformed candles.
3.2 Train–Test Protocol
To ensure fair evaluation and reduce temporal leak-
age, we adopted a rolling-window split:
•T raining window:First 3 months of each in-
strument’s time range (e.g., March–May 2025).
•T esting window:Subsequent 3 months (e.g.,
June–August 2025).
Each RL experiment was run independently per
instrument using this 3+3 month split, allowing for
cross-instrument generality analysis while preserving
chronological causality.
3.3 Resampling and Normalization
Despite the raw data being recorded at a frequency
of 1 minute, we constructed multiple synchronized
resolutions for downstream components:
•1-minute barsfor high-frequency RL training,
•5-minute and 1-hour barsfor smoothed eval-
uation, baselines, and sentiment-aligned sanity
checks.
For each resampled bar, the OHLC values were
aggregated using standard conventions, and a sum-
mation of volume was carried out. Missing bars
are filled forward for price columns and zero for
volume, where appropriate. All numeric features
were standardized usingrolling z-score normal-
izationcomputed strictly within the training win-
dow to avoid look-ahead bias.
3.4 Technical Indicator Computation
We computed a comprehensive set of technical fea-
tures per bar, including:
•T rend and smoothing:SMA/EMA (5, 20,
50),
•Momentum:MACD (12, 26, 9), RSI (14),
•V olatility:rolling standard deviation (10, 20),
3

•Liquidity:log(volume+1), rolling volume Z-
score,
•Price microstructure:logarithmic returns,
realized volatility, high–low spread, close–open
spread.
All indicators were computed using our own
scripts to ensure reproducibility and maintain a con-
trolled feature-generation pipeline.
3.5 News and Textual Data
We scraped timestamped financial news and head-
lines that matched the selected instruments during
the same period (March–August 2025). Each article
contains:
•timestamp,
•headline or full body text,
•source metadata,
•optional unique IDs.
Raw text was minimally cleaned: converting to
lowercase, removal of HTML tags, and retention of
domain-specific tokens (e.g., EBITDA, MoU, ATF,
subsidy).
3.6 Event De-duplication and News-
Clustering Pipeline
To prevent statistical irregularities arising from re-
peated rewrites of the same corporate event, we con-
structed a structured de-duplication and clustering
pipeline:
1.Semantic embedding:Each article was en-
coded using an LLM-based sentence embedding
model, all-MiniLM-L6-v2.
2.Initial deduplication:Within sliding 1–4
hour windows, we clustered the embeddings us-
ing cosine similarity (threshold≈0.80–0.85) to
collapse identical or nearly identical rewrites.
3.Event representation:For each cluster, we
retained the highest-quality representative arti-
cle and treated it as the canonical ‘event’.
4.Global event clustering:Canonical events
were further re-clustered over multi-day win-
dows using HDBSCAN to identify higher-level
thematic clusters (e.g., earnings, regulatory an-
nouncements, management changes).
This two-stage process was used to remove event
duplication bias and produces stable event clusters
for statistical validation.
3.7 Sentiment Processing and
Derivative Signals
For each canonical event, the sentiment was com-
puted using a two-stage fallback system:
•Primary:FinBERT-based sentiment classifier,
•F allback:Domain-tuned lexicon scoring for
low-confidence cases.
Further temporal derivatives were computed for
the sentiment:
•Sentiment velocity:change in sentiment
score per unit time,
•Sentiment acceleration:change in sentiment
velocity.
These features were then aligned with the nearest
market-time bins and synchronized with the OHLCV
data.
3.8 Multimodal Alignment for RL
Lastly, all numeric and textual signals were fused
into MDP-ready state vectors. Alignment steps in-
clude:
•timestamp quantization to 1-minute bars,
•forward propagation of event-based features un-
til the next event,
•masking of unavailable features during training
to avoid leakage,
•standardization of features per instrument.
4 Reinforcement Learning En-
vironment
This section describes the formulation of the rein-
forcement learning (RL) environment with which the
trading agent interacts. The RL environment is a
crucial component in any RL-based system, as it de-
fines the agent’s capabilities, restrictions, and learn-
ing objective.
Our environment is modeled around a time series
of financial data. At each timestep, the agent con-
sumes an observation and outputs an action. A re-
ward is assigned for each timestep, and the training
process aims to optimize the cumulative reward over
many timesteps.
4.1 Observation Space
The observation space is the set of values that the
agent can consume as input. We incorporate, in our
observation space, a variety of technical indicators
characterizing positional information as well as asset
performance. Formally, each observation is a tuple
consisting of the following fields:
4

•Technical Indicators (normalized so that maxi-
mum magnitude is 1):
–Relative Strength Index (RSI)
–Average Directional Index (ADX)
–Ultimate Oscillator (ULTOSC)
–William’s %R (WILL%R)
•Positional Parameters:
–Current position: whether the agent is
holding a short, neutral, or long position,
encoded as−1, 0, or 1
–Current capital
–Fraction of trading day remaining
We also incorporate frame stacking, wherein a
fixed number of past observations are stacked to-
gether and passed as input to the neural network.
This is a simple measure that allows the agent to
learn deeper temporal patterns.
The indicators are constructed from raw financial
data, as discussed in Section 3.
4.2 Action Space
The action space is the set of values that the agent
can output. We use an action space consisting of 2
binary signals:
•Should-Sell:This indicates that a share
should be sold.
•Should-Buy:This indicates that a share
should be bought.
In a long position, Should-Sell = 1 causes a share
to be sold. Conversely, in a short position, Should-
Buy = 1 causes a share to be bought. In a neutral
position, if only one of the signals is 1, that signal is
heeded (i.e., Should-Sell causes a sale, Should-Buy
causes a buy).
4.3 Reward Function
The reward function is derived from the change in
portfolio value. At each timestept, the reward func-
tion is defined as
rt =p t −p t−1
wherep t is the portfolio value, defined by
pt =n tst +c t
wheresis the share price,nis the number of shares
held, andcis the capital.
Figure 1: Architecture of the Proposed System
5 Statistical Analysis of Senti-
ment and Semantic Signals
5.1 Sentiment Dynamics and Predic-
tive Strength
To assess whether textual information contains ex-
ploitable structure beyond raw polarity, we evalu-
ated the temporal derivatives of aggregated senti-
ment. Consistent with our hypothesis, it was ob-
served that sentiment acceleration — the second-
order change in sentiment score — exhibited a
stronger correlation with forward returns than raw
sentiment or sentiment velocity.
Across both instruments, acceleration peaks
aligned with elevated volatility and directional
moves, suggesting that rapid shifts in narrative tone
preceded the corresponding price adjustments. Im-
portantly, acceleration produced a statistically sig-
nificant median-return separation in the 4-hour and
12-hour forward horizons, whereas raw sentiment
scores showed weaker or inconsistent effects.
Thus, sentiment acceleration improved responsive-
ness, capturing the speed at which markets inter-
nalize textual information rather than its absolute
polarity. This supported its inclusion as a Level-3
feature within the RL state space.
6 System Architecture
As shown in Fig. 1, the proposed model integrates
multimodal inputs.
6.1 Semantic Embeddings Reveal
Non-Obvious Structure
Although sentiments captured the directional tone,
they ignored the underlying semantics of the event
itself. Using LLM-derived embeddings of canoni-
cal news events, we performed clustering to iden-
tify semantically coherent groups (e.g., earnings, reg-
ulatory actions, management changes, sector-wide
macro catalysts).
Our analysis showed that embedding clusters re-
vealed patterns that could not be observed through
sentiment alone. Clusters with nearly identical sen-
5

timent distributions nevertheless show markedly dif-
ferent future return characteristics, indicating that
coarse polarity measures are insufficient to capture
nuanced market responses.
This validates the choice of embeddings as a com-
plementary channel—not just noise filtering or de-
duplication, but an information dimension that iden-
tified recurring thematic contexts that sentiment
models under-differentiate.
6.2 Cluster-Level Return Patterns
and Market Regimes
Across instruments, we identified between 5 and 8
stable event clusters after de-duplication and signif-
icance filtering. Using quantile-binned forward re-
turns and bootstrapped 95% confidence intervals, we
observed:
•Clusters 3 and 7 consistently exhibited posi-
tive median returns throughout the 4–12 hour
horizons, with statistically separated confidence
bounds.
•Event clusters dominated by highly specific one-
off events were filtered out via de-duplication
and cluster-size thresholds, reducing the event-
duplication bias.
•Significance tests (Spearman IC, permutation
tests) further confirmed that certain clusters
carry robust predictive information under re-
sampling.
We interpreted these clusters as semantic mar-
ket regimes, reflecting distinct economic narratives
rather than price-driven regimes (as in MOT-style
RL). These findings demonstrated that semantic
similarity between events is a valuable predictor of
how the market will respond in the near future.
6.3 Optimal Signal Density at 4-Hour
Aggregation
We evaluated returns across multiple horizons (1
hour, 4 hours, 1 day, 3 days). The results showed
that the 4-hour bar interval consistently provides the
most stable and dense predictive signal for both sen-
timent acceleration and embedding-cluster features.
Shorter horizons (1 hour) captured noise and tran-
sient microstructure effects, while longer horizons (1
day, 3 days) diluted the impact of individual events
due to overlapping narratives. The 4-hour horizon
balances rapidity with statistical reliability, leading
to the clearest separation between cluster-level re-
turn distributions.
This informs both our feature-engineering deci-
sions and the granularity of the RL environment’s
observation.
6.4 Sentiment-Guided Action Modu-
lation
One of the key innovations of our approach was the
dynamic modulation of raw RL actions based on sen-
timent signals. The modulated action ˜at was calcu-
lated as:
˜at =



min

at(1 +|s t|ct),1.0

if sign(a t) = sign(st)
and|s t|> θ
at(1− |st|ct) if sign(a t)̸= sign(s t)
and|s t|> θ
at otherwise
(1)
whereθis a sentiment threshold (empirically set to
0.2). This modulation implements two important
behaviors:
1.Amplification:When the agent’s intended ac-
tion aligns with strong sentiment signals, the
position size is increased proportionally to sen-
timent magnitude and confidence.
2.Attenuation:When the agent acts against
prevailing sentiment, the position is reduced to
limit exposure to sentiment-driven price move-
ments.
7 Evaluation Protocol and
Metrics
Our proposed multimodal trading framework was
evaluated using standard quantitative finance met-
rics, RL-specific validation procedures, and statis-
tically robust comparisons across model variants.
Because the goal of this work was to demonstrate
methodological viability rather than production-
grade deployment, the evaluation emphasized risk-
adjusted performance, return distribution character-
istics, and statistical reliability of the observed im-
provements.
7.1 Trading Performance Metrics
The following performance measures were calculated
in the 3-month test window for each instrument:
•Cumulative Return (ROI):Measured the
total multiplicative growth of the portfolio over
the test horizon. This was considered the pri-
mary measure of directional profitability.
Sharpe Ratio:
Sharpe = E[r] σ[r]
whererrefers to the daily returns. Because test
windows are short and risk-free rates are negligi-
ble at this horizon, we assumed a risk-free value of
6

zero. This reflects the efficiency of the reward-to-
variability ratio.
Sortino Ratio:
Sortino = E[r] σ[rr<0]
This ratio highlights whether the improvements arise
from controlled downside risk rather than symmetric
variance.
•Maximum Drawdown (MDD):This mea-
sure captures the worst decline from peak-to-
trough in the portfolio. Lower MDD indicates
improved risk management and resilience to loss
streaks.
Win Rate:
WinRate = #winning trades #total trades
Profit F actor:
ProfitFactor = gross profit gross loss
These metrics provide interpretable diagnostics on
the agent’s trade-level behavior.
•Return Stability:We report the standard de-
viation of the daily returns as a measure of the
smoothness of the policy. Low variability indi-
cates that the agent avoids oscillatory or impul-
sive trading behavior.
7.2 Model Comparison and Statisti-
cal Testing
To ensure that the observed differences between
model configurations (Base, Sentiment-only, Senti-
ment+Embeddings) were not due to the stochastic-
ity of PPO or episodic variation, we performed:
•Bootstrap resamplingof the evaluation
episodes (1,000–5,000 samples depending on
configuration),
•Median and 95% confidence intervalsfor
ROI and risk-adjusted metrics,
•Non-parametric significance tests(e.g.,
permutation tests on paired Sharpe differences).
These methods provided robust quantification of
whether the hybrid sentiment–semantic feature set
yielded meaningful improvements over the numeric-
only baselines.
7.3 Reporting Conventions
Only the above ratios and performance statistics are
used in the evaluation. Latency or inference-related
measurements for the sentiment pipeline were not
emphasized, as they do not affect the scientific con-
clusions of this proof-of-concept study. All reported
metrics were calculated in the test window held
from June–August 2025 for each instrument, using
chronological (non-shuffled) data so that temporal
integrity was preserved.
8 Conclusion
This work presented a comprehensive, multimodal
framework that integrated textual market data, nu-
merical market data, LLM-derived sentiment sig-
nals, and semantic embedding-based event structure
into a unified reinforcement learning trading system.
Unlike prior RL-only trading agents or sentiment-
only predictive models, this approach explicitly com-
bined (i) higher-order sentiment indicators, (ii) sta-
tistically validated semantic clusters of news events,
and (iii) a PPO-based agent within a formally de-
fined MDP. These enabled the agent to react not
only to price movements, but also to the narra-
tive velocity and evolving informational context of
the market. Although not intended as a deploy-
able trading system, the proposed framework of-
fers a reproducible foundation for future research
in multimodal financial RL, including extensions to
cross-asset generalization, transformer-based state
encoders, richer sentiment models, and uncertainty-
aware policy learning.
The empirical results demonstrated that sen-
timent acceleration, event de-duplication, and
embedding-driven regime identification provided a
predictive structure that is absent in numeric-only
baselines. The set of hybrid features consistently
improved the risk-adjusted returns, convergence sta-
bility, and drawdown behavior across multiple in-
struments and evaluation horizons. These findings
established that textual signals, when processed rig-
orously and aligned with market microstructure, can
materially enhance sequential decision-making for
trading.
More broadly, this study provides a proof-of-
concept methodology to bridge natural-language
financial information with reinforcement learning
agents in a statistically grounded manner. It high-
lighted the feasibility and value of incorporating nar-
rative dynamics, semantic regimes, and multimodal
alignment into RL environments.
7

Algorithm 1Sentiment Aggregation (per-bin)
1:procedureAggregateSenti-
ment(articles, bins)
2:forallbininbinsdo
3:items←articles[timestamps∈bin]
4:ifitemsemptythen
5:S bin ←decay(lastS)
6:else
7:foralliteminitemsdo
8:s i, ci ←FinBERTScore(item)
9:w i ←c i ×
sourceWeight(item.source)
10:end for
11:S bin ←
P
i wisiP
i wi
12:end if
13:end for
14:return{S bin}
15:end procedure
Algorithm 2Smart Multi-Phase Training
1:procedureTrainPipeline(data, news)
2:preprocData←PreprocessMarket(data)
3:dailySentiment←
AggregateSentiment(news, bins)
4:agent 1 ←TrainPPO(Level1Env(preprocData))
5:val 1 ←Validate(agent 1)
6:agent 2 ←InitFrom(agent 1)
7:TrainPPO(Level2Env(preprocData, dailySentiment))
8:val 2 ←Validate(agent 2)
9:ifval 2.metric > val1.metric×(1 +δ)then
10:agent 3 ←InitFrom(agent 2)
11:TrainPPO(Level3Env(preprocData, dailySentiment))
12:end if
13:returnbest agent
14:end procedure
Appendix A: Algorithms and
Pseudocode
Appendix B: Hyperparameter
Table
References
[1] H. Kapoor, “Indian Financial News Ar-
ticles 2001–2020,” Kaggle, 2020.https:
//www.kaggle.com/datasets/hkapoor/
indian-financial-news-articles-20032020
[2] H. Rathod, “India Financial News Head-
lines Sentiments,” Kaggle, 2021.https:
//www.kaggle.com/datasets/harshrkh/
india-financial-news-headlines-sentiments
[3] K. Dave, “Indian Financial News,” Hug-
gingFace, 2022.https://huggingface.co/
Table 1: *
T ABLE I
Representative hyperparameters and defaults.
Item V alue
Training steps (per phase) 1M steps (example)
Observation window 60 bars (1-hr for 1-min)
Transaction cost 0.02% per trade
Slippageκ0.01–0.1% (tunable)
Sentiment bin size 1 hr (or 4 hrs)
Sentiment weightα0.01–0.1 (tunable)
Risk penaltyβ0.5 (example)
datasets/kdave/Indian_Financial_News
[4] H. Yang, X.-Y. Liu, and C. D. Wang,
“FinGPT: Open-Source Financial Large
Language Models,” arXiv:2306.06031, 2023.
doi:10.48550/arXiv.2306.06031
[5] X.-Y. Liu, H. Yang, J. Gao, and C. D. Wang,
“FinRL: Deep Reinforcement Learning Frame-
work to Automate Trading in Quantitative Fi-
nance,”Proc. 2nd ACM Int. Conf. AI Finance,
2021, pp. 1–9.
[6] C. Y. Dai, I. Wang, and Y. Xu, “Reinforce-
ment Learning for FX Trading,” Stanford Uni-
versity, 2019.https://stanford.edu/class/
msande448/2019/Final_reports/gr2.pdf
[7] Z. Kou, H. Yu, J. Peng, and L. Chen, “Au-
tomate Strategy Finding with LLM in Quant
Investment,” arXiv:2409.06289, 2024.
[8] K. J. L. Koa, Y. Ma, R. Ng, and T.-S. Chua,
“Learning to Generate Explainable Stock Pre-
dictions using Self-Reflective Large Language
Models,”Proc. ACM Web Conf. (WWW), Sin-
gapore, 2024, pp. 4304–4315.
[9] J. Kim et al., “Is Small Really Beautiful for
Central Bank Communication?,”Proc. ACM
ICAIF, 2024. doi:10.1145/3677052.3698675
[10] X. Cheng, J. Zhang, Y. Zeng, and W. Xue,
“MOT: A Mixture of Actors Reinforcement
Learning Method by Optimal Transport for Al-
gorithmic Trading,”PAKDD 2024, LNCS vol.
14648, pp. 30–42, 2024.
[11] Z. Zhao and R. E. Welsch, “Aligning LLMs
with Human Instructions and Stock Market
Feedback in Financial Sentiment Analysis,”
arXiv:2410.14926, 2024.https://arxiv.org/
pdf/2410.14926v1
[12] S. Sun et al., “DeepScalper: A Risk-Aware
Reinforcement Learning Framework to Cap-
ture Fleeting Intraday Trading Opportunities,”
arXiv:2201.09058, 2022.
8

[13] S. Wang, J. Tan, Z. Dou, and J.-R. Wen, “Om-
niEval: An Omnidirectional and Automatic
RAG Evaluation Benchmark in Financial Do-
main,” arXiv:2412.13018, 2024.
[14] S. Shen et al., “Financial Sentiment Analysis on
News and Reports using LLMs and FinBERT,”
arXiv:2410.01987, 2024.
[15] B. Zhang, H. Yang, T. Zhou, M. A. Babar,
and X.-Y. Liu, “Enhancing Financial Sentiment
Analysis via Retrieval Augmented Large Lan-
guage Models,”Proc. ACM ICAIF, 2023, pp.
349–356. doi:10.1145/3604237.3626868
9
