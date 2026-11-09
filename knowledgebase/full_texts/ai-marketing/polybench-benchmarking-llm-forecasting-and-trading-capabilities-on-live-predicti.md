---
title: 'PolyBench: Benchmarking LLM Forecasting and Trading Capabilities on Live Prediction Market Data'
url: https://arxiv.org/abs/2604.14199
category: ai-marketing
subcategory: empirical
date: 2026-04
venue: ''
authors:
- Pu Cheng
- Juncheng Liu
- Yunshen Long
source: arxiv
pdf_url: https://arxiv.org/pdf/2604.14199
pages: 16
chars: 35570
fetched_at: '2026-11-08T13:06:03+00:00'
kb_version: 1
---

# PolyBench: Benchmarking LLM Forecasting and Trading Capabilities on Live Prediction Market Data

PolyBench: Benchmarking LLM Forecasting and
Trading Capabilities on Live Prediction Market
Data
Pu Cheng1, Juncheng Liu1, Yunshen Long2 ()
1 College of Electrical Engineering, Sichuan University, Chengdu, Sichuan, China
{cheng.chengpu123,junchengliu2004}@gmail.com
2 School of Economics, Sichuan University, Chengdu, Sichuan, Chinadhhlys@163.com
Abstract.Predicting real-world events from live market signals de-
mands systems that fuse qualitative news with quantitative order-book
dynamics under strict temporal discipline—a challenge existing bench-
marks fail to capture. We presentPolyBench, a multimodal bench-
mark derived from Polymarket that records point-in-time cross-sections
of38,666binarypredictionmarketsspanning4,997events,synchronously
coupling each snapshot with a Central Limit Order Book (CLOB) state
and a real-time news stream. Using PolyBench, we evaluate seven state-
of-the-art Large Language Models—spanning open- and closed-source
families—generating36,165predictionsunderidentical,timestamp-locked
market states collected between February 6 and 12, 2026. Our multidi-
mensionalframeworkassessesdirectionalaccuracy,ourproposedConfidence-
WeightedReturn(CWR),AnnualizedPercentageYield(APY),andSharpe
ratio via realistic order-book execution simulation. The results reveal a
pronounced performance divergence: only two of seven models achieve
positive financial returns—MiMo-V2-Flash at17.6%CWR and Gemini-
3-Flash at 6.2% CWR—while the remaining five incur losses despite uni-
formly high stated confidence. These findings highlight the gap between
surface-level language fluency and genuine probabilistic reasoning under
live market uncertainty, and establish PolyBench as a contamination-
proof, financially-grounded evaluation standard for future LLM research.
Ourdatasetandcodeavailableathttps://github.com/PolyBench/PolyBench .
Keywords:prediction markets·LLM evaluation·financial forecasting
·benchmark.
1 Introduction
Forecasting the future is a longstanding scientific challenge, ranging from early
astronomytomoderneconometricmodeling.Inmachinelearning,itencompasses
time-series analysis [6,15], online learning [9], and conformal prediction [3]. Yet
open-domainforecasting—producing reliable probabilistic predictions across di-
verse, unseen topics without domain-specific fine-tuning—remains largely un-
solved. Achieving such foresight at scale would represent a paradigm shift in
arXiv:2604.14199v1  [q-fin.CP]  3 Apr 2026

2 P. Cheng et al.
artificialintelligence,withsignificantimplicationsformarketefficiency,riskman-
agement, and data-driven policy [2].
Large Language Models (LLMs) are natural candidates for this task. Trained
on vast corpora via next-token prediction, they exhibit emergent reasoning ca-
pabilities that extend well beyond surface-level pattern matching [7], suggesting
that predicting the next token may generalize toward predicting the next real-
worldevent. Recent studies [25,10] have demonstrated encouraging progress, yet
a central question remains open:Can AI systems accurately forecast outcomes
and execute profitable trades on live decentralized prediction markets using mul-
timodal data?
DecentralizedpredictionmarketssuchasPolymarket[19]constituteauniquely
rigorous evaluation environment—financially incentivized, on-chain, and struc-
turally immune to answer memorization. Forecasting in this setting is inher-
ently multimodal: participants must jointly assess qualitative resolution crite-
ria, breaking news, and quantitative Central Limit Order Book (CLOB) states,
bid-ask spreads, and live liquidity. Existing benchmarks reduce forecasting to
static text question answering or numerical time-series extrapolation, thereby
overlooking the order-book mechanics, capital-risk dimension, and point-in-time
grounding that real prediction markets require.
To address this gap, we present a dual-purpose research initiative:
Fig. 1.Confidence-Weighted Return (CWR) timeline reflecting empirical portfolio evo-
lution. Annotated markers denote outsized individual trade returns resulting from cor-
rect, high-confidence predictions on low-probability events. OnlyMiMo-V2-Flashand
Gemini-3-Flashsustain positive trajectories, isolating predictive alpha from market
noise.

PolyBench: LLM Forecasting and Trading on Prediction Markets 3
– PolyBench—a live multimodal benchmark comprising 38,666 binary pre-
diction markets across 4,997 real-world events. Each market snapshot syn-
chronously couples an exact CLOB state with contemporaneous news and
official resolution criteria.
– MultidimensionalEvaluationFramework—aprotocolthatassessesseven
state-of-the-art LLMs on both forecasting accuracy and trading viability,
measuringConfidence-WeightedReturn(CWR),AnnualizedPercentageYield
(APY), Sharpe ratio, and instruction adherence under realistic order-book
execution simulation.
To quantify LLM viability in financial forecasting, our multidimensional
framework assesses classification accuracy, probabilistic reliability, strategic rea-
soning, and simulated financial execution, highlighting both emerging strengths
and current limitations in information aggregation. As shown in Fig. 1, our
results reveal a pronounced performance divergence: only two of the seven eval-
uated models achieve positive financial returns, while the remaining five incur
losses. demonstrating that strong language modeling does not guarantee prof-
itable trading under live market conditions.
2 Related Work
Deploying LLMs on live decentralized prediction markets lies at the intersection
of three active research areas: financial time-series modeling, contamination-free
LLM evaluation, and financial agent benchmarking.
2.1 Event Forecasting and Financial Time-Series
Computationalfinancehasevolvedfromclassicaleconometricmodels[4,5]through
recurrent and attention-based deep learning [12,20] to large-scale financial foun-
dation models such as BloombergGPT [21], FinBERT [1], and Time-LLM [13].
However, these works predominantly targetcontinuousasset variables rather
than discrete event outcomes. NLP-oriented forecasting benchmarks such as
Autocast [25] address binary event prediction but lack real-time quantitative
market grounding. PolyBench bridges this gap by coupling synchronous order-
book snapshots with aligned news streams to enable evaluation of binary event
outcomes under realistic financial conditions.
2.2 Overcoming Pre-training Data Leakage
Static benchmarks are vulnerable to data contamination: models may inadver-
tently memorize evaluation instances during pre-training, even in carefully cu-
rated test sets such as MATH [11] or Humanity’s Last Exam [18]. Dong et al. [8]
show that this leakage can inflate reported accuracies by up to 66.9%, rendering
published benchmark scores unreliable proxies for true generalization. Decen-
tralized prediction markets are structurally immune to this problem, because

4 P. Cheng et al.
they forecast events that havenot yet occurredat evaluation time, making it
impossible to pre-train on the ground-truth outcomes. PolyBench therefore en-
forces genuine zero-shot temporal reasoning and provides a contamination-proof
measure of true LLM forecasting capability.
2.3 LLMs as Autonomous Forecasting Agents
RecentworkhasshiftedtowardevaluatingLLMsasautonomousdecision-making
agents [17]. Halawi et al. [10] showed that LLM-based systems can approach
human-crowd-level accuracy on Polymarket; Prophet Arena [22] further exposes
predictive bottlenecks on live events. However, both works evaluate models on
purelytextualaxes,ignoringorder-bookmechanicsandthefinancialcostoftrade
execution. PolyBench addresses this limitation by treating prediction markets as
an inherently multimodal environment—ingesting CLOB spreads and live liquid-
ity alongside breaking news—and assessing models on the metric that ultimately
matters in practice: simulated financial return.
Table 1 summarizes the feature gap that PolyBench fills.
T able 1.Comparison of prediction-market and forecasting benchmarks. PolyBench is
the only benchmark combining Polymarket data, live order books, aligned news, and
return-based evaluation at scale.
Method Markets w/ Polymarket w/ Order Book w/ News CWR Eval.
Time-LLM [13] –× × × ×
AgentBench [16] –× × × ×
FinBERT [1] –× ×✓×
BloombergGPT [21] –× ×✓×
Autocast [25] 6,707× ×✓×
Prophet Arena [22] 1,367× ×✓×
Halawi et al. [10] 48,754✓×✓×
LiveTradeBench [23] 10✓ ✓ ✓×
PolyBench (Ours) 38,666✓ ✓ ✓ ✓
3 Polymarket Definitions and Notations
To formalize the evaluation framework within PolyBench, we define the core
components of the Polymarket ecosystem. While these definitions share founda-
tional concepts with general prediction markets, they are specifically adapted to
the decentralized mechanisms, order book structures, and snapshot-based eval-
uations utilized in our pipeline.

PolyBench: LLM Forecasting and Trading on Prediction Markets 5
Event.Let{E i}K i=1 denote the set of evaluated forecasting events sourced via
Polymarket’s Gamma API. An event serves as the overarching high-level con-
tainer concerning a future real-world occurrence (e.g., political elections, finan-
cial milestones, or sports outcomes). It establishes the context, scope, and strict
official resolution criteria for the markets beneath it.
–Example:“Who will win the 2026 World Cup?”
Market.Each eventE i contains one or more binary markets{Mij}Ni j=1. A mar-
ket is a specific, actively tradable proposition under an event that will ultimately
resolve to a definitive Yes (True) or No (False). Markets are identified by unique
token identifiers and are accompanied by live volume metrics and Central Limit
Order Book (CLOB) states.
–Example market:“France will win the 2026 World Cup.”
Event Resolution.An eventE i is said to resolve at timeτi when all of its
constituent marketsM ij have their outcomesoij ∈ {0,1}definitively settled ac-
cording to Polymarket’s official resolution rules. An outcome ofoij = 1indicates
that the marketMij resolved to Yes. PolyBench explicitly accounts for strict ad-
herence to these rules, including conditional constraints (e.g., forced 50-50 split
resolutions).
Contract (Share).For a given marketMij, a Yes contract (or share) is a bi-
nary asset that yields a payout of 1 ifoij = 1, and 0 otherwise. Rather than
occupying a static theoretical price, the acquisition cost of these shares is gov-
erned dynamically by available market liquidity at a specific point in time. In
PolyBench, the executed share price is simulated directly against the historical
Central Limit Order Book (CLOB), sequentially absorbing orders from the best
available ask (aij) until the agent’s allocated capital limit is reached.
State Snapshot.Because PolyBench evaluates trading agents in a simulated
historical context, each marketMij is evaluated within a temporally anchored
State Snapshot. This snapshot is a multi-modal bundle containing the exact his-
torical timestamp, event metadata, precise CLOB state (including wide spreads
or volume imbalances), and conditionally prefetched exogenous Google News
context. This ensures a strict Bayesian baseline and prevents future data leak-
age during backtesting.
Trading Signal.The actionable output generated by the LLM agent for a
given snapshot, characterized by a scalar confidence scoreci ∈[0.0,1.0]. The
agent issues a BUY decision only whenci overcome a rigid threshold 0.6.
4 PolyBench
The goal of PolyBench is to provide a return-focused, extendable and automated
evaluation of LLMs’ advanced forecasting and market trading capabilities on
Polymarket, aiming to match or even surpass the expertise of human profession-
als. In this section, we will introduce the details of PolyBench.

6 P. Cheng et al.
Fig. 2.The four-stage PolyBench construction pipeline: (1) market collection via the
Polymarket Gamma API, (2) multi-modal fetch of news and order-book snapshots,
(3) LLM batch analysis, and (4) ground-truth resolution matching.
4.1 Construction
As illustrated in Fig. 2, the benchmark construction pipeline initiates with the
collection of active events via Polymarket’s Gamma API, extracting essential
metadata such as titles, token identifiers, and market volumes. A background
runner then aggregates multi-modal context by retrieving relevant Google News
article streams and capturing precise Central Limit Order Book (CLOB) states.
This temporally aligned bundle of information constitutes a historicalsnapshot
of each market at a specific timestamp. These multi-modal state snapshots are
subsequently dispatched to the respective LLM endpoints for predictive evalua-
tion.
Prompt DesignTo accurately simulate algorithmic trading without future
data leakage during backtesting, the prompt establishes a strict Bayesian base-
line locked to the specific snapshot timestamp. The language model is anchored
with the exact historical timestamp as the “Current Date”, alongside the event
title and detailed description. The prompt injects the historical market op-
tions—including precise order book spreads and midpoint prices active at that
exact interval—coupled with the conditionally prefetched exogenous news con-
text.
To govern the agent’s decision-making process, a robust system instruction
enforces the following core rules:
– Resolution Rule Primacy: Strict adherence to official market rules over
general knowledge, explicitly accounting for conditional constraints (e.g.,
forced 50-50 split resolutions).

PolyBench: LLM Forecasting and Trading on Prediction Markets 7
– ValueIdentification:Directivestosignal“valuebets” onlywhenthemodel’s
evidence-backed posterior significantly deviates from the market’s implied
odds.
– Market Microstructure Analysis: Guidelines to interpret order book
data, recognizing wide spreads as uncertainty and volume imbalances as
informed trading.
– Evidence-Backed Conviction: A hard constraint requiring probability
confidence exceeding 60% (c >0.6) to be directly justified by provided news
quotes.
– Temporal Awareness: Continuous evaluation of the estimated resolution
timeline against the “Current Date” snapshot for annualized yield mapping.
Structured Output and FilteringThe LLM predictive engine must return
a strictly formatted JSON payload with an overall reasoning narrative and an
array of actionabledecisions. Each executable trade within this array must
adhere to the schema detailed in Table 2.
T able 2.Structured JSON schema requirements for model predictions.
Field Description
decisionThe specific target option identifier
outcomeThe exact predicted position mapping
strategyA classification of the trading rationale (e.g.,
value_bet,news_catalyst)
confidenceA scalar conviction score (c∈[0.0,1.0])
est_resolution_dateThe model’s estimated temporal timeline for mar-
ket settlement
reasoningA concise, specific rationale validating the posi-
tion
Crucially, if a model fails to identify any positive expected value trades or
if its declared confidence falls below a rigid threshold (c <0.6), the decisions
are procedurally discarded. A model can suggest skipping a event explicitly by
giving nothing in decision field. This functionally mimics a disciplined trader’s
behaviour, abstaining from ambiguous markets without penalty.
Dataset StatisticsThe executed data collection pipeline results in an expan-
sive evaluation framework. Table 3 provides a comprehensive breakdown of the
curated PolyBench dataset, highlighting the scale of real-world financial events,
gatheredsnapshots,andtheresultingdensityoflargelanguagemodelpredictions
processed. Notably, all events, underlying prediction markets, and correspond-
ing snapshots—including both exogenous news context and internal order book
states—were collected between February 6, 2026, and February 12, 2026. The

8 P. Cheng et al.
T able 3.PolyBench dataset statistics.
Component Count Notes
Events 4,997
Active 2,904 Open at collection time
Resolved 2,093 Closed / expired
Markets 38,666
Active 26,784 Open at collection time
Inactive 11,882 Settled or delisted
Market Snapshots 38,666
With news context 35,436 91.6% coverage
With order book 19,012 49.2% coverage
Prediction-ready 5,097 Resolved + With order book & news
LLM Predictions 36,165∼5,100 per model
latest market resolution date recorded is February 21, 2026. Crucially, the in-
clusion of actively traded, yet-to-be-resolved markets imbues PolyBench with
inherent extensibility for future longitudinal assessments.
4.2 Evaluation
We continue to use model accuracy as an indicator of forecasting capabilities, in
line with recent LLM benchmark studies [24,14]. These studies typically require
models to predict a deterministic outcome for evaluation. However, a fundamen-
tal limitation of this approach is that forecasting inherently differs from standard
classification tasks due to the probabilistic and random nature of future events
[22]. Furthermore, given the lack of reliable, unbiased continuous probability ref-
erences in volatile decentralized prediction markets, we do not adopt traditional
proper scoring rules such as the Brier Score. Instead, we directly incorporate the
model’s stated confidence into our final economic return calculation to better
evaluate the financial viability of each trade suggestion.
Unlike traditional forecasting-oriented benchmarks that force models to pre-
dict every event, PolyBench is fundamentally tailored toward realistic market
trading and maximizing practical economic returns. Consequently, agents are
provided with aSKIPchoice to explicitly pass on ambiguous or unfavorable
markets, and these instances are entirely excluded from the performance metrics
calculation.
Directional AccuracyTo assess a model’s baseline forecasting capabilities
on its actively chosen positions, we rely on the standard metric of directional
accuracy. For a set ofNvalid, non-skipped predictions, accuracy is defined as the
proportion of trades where the model correctly identifies the ultimate resolution
of the prediction market. Letok represent the ground-truth terminal settlement

PolyBench: LLM Forecasting and Trading on Prediction Markets 9
state for thek-th forecasted market, andˆo k represent the agent’s forecasted
position.
Accuracy= 1 N
NX
k=1
I(ok = ˆok)(1)
WhereI(·)is the indicator function that evaluates to 1 if the predicted state
matches the actual settlement, and 0 otherwise. While accuracy serves as a
fundamental performance baseline, it treats all correct guesses equally and fails
to distinguish between predictions made with marginal certainty and those made
with absolute conviction.
Confidence-Weighted Return (CWR)To capture both correctness and
risk calibration under realistic market constraints, we introduce the Confidence-
Weighted Return (CWR) metric. Rather than evaluating a flat percentage return
against mid-market prices, the agent’s simulated capital allocation is scaled lin-
early by its statedconfidence(c k ∈[0.0,1.0]) and a designated baselot_size
(L) for eachBUYdecision.
For thek-th predicted trade, the allocated budget isBk =c k ×L. This budget
is deployed against the corresponding active Central Limit Order Book (CLOB)
snapshot, absorbing available liquidity starting from the best ask. This simulates
a realistic sweep of the order book, returning the actual invested capitalIk ≤B k
and the total number of shares acquiredSk.
If the model accurately predicts the market’s resolution, the shares settle at
exactly $1.00, yielding a gross payout. If incorrect, the shares resolve at $0.00.
The net profitπk for tradekis thus:
πk =
(
Sk −I k,if prediction is correct
−Ik,if prediction is incorrect (2)
Formally, the aggregate CWR acrossNbuy executed trades is defined as the
total net profit divided by the total invested capital:
CWR=
PNbuy
k=1 πk PNbuy
k=1 Ik
(3)
By structurally accounting for variable slippage and execution limits, this
metricsystematicallyrewardsmodelsthatexhibitstrongriskcalibration—placing
high confidence on successful bets with adequate liquidity—while severely pe-
nalizing overconfident allocations on incorrect assumptions.
Additional Economic and Temporal MetricsTo holistically evaluate the
practical viability and risk-adjusted performance of the agents’ trading strate-
gies, we incorporate three supplementary continuous metrics:

10 P. Cheng et al.
– Annualized Percentage Yield (APY):While CWR measures absolute
return, APY normalizes this return over time to account for the opportunity
cost of locked capital. For a trade yielding returnri held forDdays before its
actualresolution,itsannualizedbaselineiscomputedasAPY=r i×(365/D).
– Sharpe Ratio:To assess risk-adjusted portfolio performance, we compute
the Sharpe Ratio over the distribution of a model’s individual trade returns.
Defined as the mean return divided by the standard deviation of returns
(µr/σr), it strictly penalizes models experiencing erratic, high-variance eq-
uity draw-downs.
– Temporal Resolution Error:Beyond predicting outcomes, agents must
forecastwhena market will resolve to gauge capital efficiency. This met-
ric represents the mean absolute error (in days) between the model’sest_
resolution_dateand the true market resolution timestamp.
5 Experiment
In this section, we present the empirical results from the PolyBench evaluation
framework. The benchmark evaluates seven distinct LLMs representing state-of-
the-art architectures from their respective providers, evaluating a gross total of
36,165 predictions based on active financial snapshots.
Table 4 summarizes the evaluated models, including their releasing company,
the specific API service provider utilized, reported quantization applied during
inference, cost of predicting over 5097 prediction-ready markets and open-source
states as shown in Table 3. To the best of our knowledge, all models’ knowledge
cut-off date is before the benchmark.
T able 4.Evaluated models grouped by open-source availability, detailing respective
companies, API providers, quantization formats, and their costs.
Model Name Company Service Provider Quantization Cost Open Source
GPT-OSS-120B OpenAI DeepInfra FP4 $ 1.34
Yes
DeepSeek-V3.2 DeepSeek Atlas Cloud FP8 $ 3.32
MiMo-V2-Flash Xiaomi Xiaomi FP8 $ 1.72
MiniMax-M2.5 MiniMax Inceptron FP8 $ 8.43
Trinity-Large-Preview Arcee AI Prime - Free
Gemini-3-Flash-Preview Google Vertex AI - $ 11.50 NoGrok-4.1-Fast xAI xAI - $ 6.85
5.1 Overall Performance
TorigorouslyassessthefinancialcapabilityandpredictiveaccuracyofeachLLM,
we employ the metrics derived in Section 4. Crucially, we distinguish between

PolyBench: LLM Forecasting and Trading on Prediction Markets 11
standard, unweighted portfolio returns (Non-CWR) and proposedConfidence-
Weighted Return (CWR). Table 5 details these comprehensive results of metrics
at base lot sizeL= $10across all executed non-skipped trades.
T able 5.Overall LLMs performance on PolyBench. (Base Lot Size=$10)
Model Accuracy↓Avg. Conf. Non-CWR CWR APY Sharpe
Gemini-3-Flash 75.0% 0.855 4.1% 6.2% 1486.5% 0.01
MiMo-V2-Flash 62.1% 0.859 11.1%17.6%4067.3% 0.02
Grok-4.1-Fast 59.1% 0.862 -15.9% -12.1% -5820.4% -0.17
GPT-OSS-120B 58.0% 0.836 -19.4% -17.8% -7075.8% -0.22
DeepSeek-V3.2 53.5% 0.838 -15.3% -11.4% -5571.8% -0.03
Trinity-Large 42.7% 0.871 -12.4% -9.2% -4527.8% -0.02
MiniMax-M2.5 42.6% 0.808 -26.1% -25.2% -9537.2% -0.22
TheseparationbetweenNon-CWRandCWRfundamentallyexposesamodel’s
risk calibration capabilities. Across the board, models consistently achieve a
higherCWR than their unweighted Non-CWR baseline, demonstrating inher-
ent meta-cognition: LLMs effectively assign higher confidence to correct pre-
dictions while discounting misjudgments. Thus in the following discussion, we
will be consistent with CWR metric. Among the seven, onlyMiMo-V2-Flash
andGemini-3-Flashachieved positive absolute returns, yielding 17.6% and 6.2%
CWR, respectively. Notably, the open-sourceMiMo-V2-Flashdemonstrated ro-
bust calibration dynamics, outperforming its proprietary counterparts in net
profitability.
The trajectory of these returns is further contextualized in Figure 1, plotting
CWR from the initial snapshot batch on February 6 through the progressive
settlement of markets on February 21, 2026. Each point on the line stands for the
settlement of one market. Annotated spikes denote outsized returns (exceeding
1,000%) from successful low-probability predictions.
Impact of Position Sizing and Order Book SlippageA critical dynamic
introduced by PolyBench’s realistic execution environment is the impact of po-
sition sizing on achievable returns. Unlike theoretically unlimited flat-price as-
sumptions, trading against historical CLOB states accurately models liquidity
constraints and execution slippage. To reliably model this dynamic without ex-
ceeding the top five levels of order-book depth captured in our snapshot pipeline,
we observe simulated returns up to a maximum base lot size of $1,000.
Figure 3 illustrates the degradation of CWR across varying base lot sizes (L)
for the two top-performing models. At smaller capital allocations (L≤$100), the
limited required volume allows agents to absorb the immediate best-ask prices,
preserving their theoretical alpha. However, as position sizing scales logarithmi-
cally toward $1,000, model profitability violently contracts. High-volume trades

12 P. Cheng et al.
exhaust the top levels of the captured order book, forcing execution into wider
spreads at significantly worse average execution prices. This structural slippage
erodes the alpha ofGemini-3-Flash, whileMiMo-V2-Flashdemonstrates relative
resilience up to$500before ultimately succumbing to systemic liquidity limits.
These results emphasize that in decentralized prediction markets, theoretical
predictive advantages are strictly bounded by available market depth.
Fig. 3.Impact of base lot size (L) on Confidence-Weighted Return (CWR) forMiMo-
V2-FlashandGemini-3-Flash. As the investment budget scales from $10 to $1,000,
algorithmic execution slippage against the limited top levels of the historical order
book rapidly decays theoretical alpha.
5.2 Domain Expertise and Miscalibrated Conviction
Different thematic domains impart vastly different analytical challenges. Fig-
ure 4 maps both the CWR performance and the Average Declared Confidence
of three top-performing models (MiMo-V2-Flash,Gemini-3-FlashandTrinity-
Large) against eight major event categories structuring PolyBench.
Figure4contrastsCWRperformanceandAverageDeclaredConfidenceacross
major event categories. The results expose a severe miscalibration: models main-
tainrigid,highconfidence(0.8≤c≤0.9)regardlessofdomaincomplexity.While
this conviction yields robust alpha inPolitics, a domain rich in parsable textual

PolyBench: LLM Forecasting and Trading on Prediction Markets 13
Fig. 4.Dual-metric radar chart comparing empirical Confidence-Weighted Return
(CWR) and Average Declared Confidence across eight event domains. The disparity
highlights LLM miscalibration; models uniformly maintain high confidence (c≥0.8)
across all domains, yielding severe negative returns in volatile sectors such asCrypto.
polling data, it proves highly detrimental in speculative, high-variance sectors
such asCrypto. Here, models incur deep negative returns while maintaining per-
ilous overconfidence, underscoring that historical text is an insufficient proxy for
volatile price-action derivatives.
5.3 Strategy Utilization and Instruction Governance
T able 6.Strategy utilization (%) paired with subsequent financial performance
(CWR%, Sharpe Ratio), alongside execution instruction adherence (Invalid Strat.) in
overall accuracy order.
Model Value Bet News Cat. Arbitrage Stable Yld. Invalid Strat.
Gemini-3-Flash 80.2% (7.2% , 0.01) 40.0% (20.7% , 0.03) 0.8% (8.1%, 0.07) 28.5% (-0.1% , 0.00) 8
MiMo-V2-Flash 94.8% (19.2%, 0.02) 46.7% (50.0%, 0.04) 5.7% (-31.1%, -0.37) 0.7% (0.4%, 1.03) -
Grok-4.1-Fast 99.3% (-11.7%, -0.17) 37.1% (6.7%, 0.04) 3.5% (-10.8%, -0.11) 0.2% (-49.9%, -0.70) -
GPT-OSS-120B 99.9% (-17.8%, -0.22) 39.4% (-19.3%, -0.21) 1.1% (-2.7%, -0.05) 2.5% (-0.2%, -0.02) -
DeepSeek-V3.2 98.4% (-10.9%, -0.03) 34.0% (19.0%, 0.02) 15.3% (-35.4%, -0.37) 20.7% (-22.6%, -0.29) -
Trinity-Large 98.2% (-9.7%, -0.03) 38.1% (16.6%, 0.01) 5.4% (-10.3%, -0.10) 0.6% (-38.5%, -0.71) 103
MiniMax-M2.5 98.0% (-25.0%, -0.22) 19.3% (-19.8%, -0.22) 5.2% (-22.7%, -0.22) 0.2% (-40.0%, -0.38) 2
Beyond evaluating pure predictive accuracy, a central tenet of autonomous
financial deployment is rigorous instruction adherence. Table 6 highlights strat-
egy utilization, conditional performance, and execution discipline. LLMs over-
whelmingly defaulted tovalue_betandnews_catalyst. However,Gemini-3-
FlashandDeepSeek-V3.2demonstrated greater conceptual diversity, deploying

14 P. Cheng et al.
stable_yieldin over 20% of trades. Performance conditioned on strategy ex-
ecution exposes LLMs’ strategic mastery:MiMo-V2-Flashgenerated notable
alpha utilizingnews_catalyst(50.0% CWR) andvalue_bet(19.2% CWR),
whileGemini-3-Flashachieved resilient positive returns across a broader set of
domains.
Crucially, instruction adherence alone does not guarantee profitability. While
extreme hallucinations (e.g.,Trinity-Largegenerating 103 invalid tags) pre-
dictably correlate with severe negative returns, flawless execution is insufficient
for generating alpha. Models likeGPT-OSS-120BandGrok-4.1-Fastachieved
perfect compliance yet suffered sub-zero returns. In contrast, the open-source
MiMo-V2-Flashuniquely synthesized strict zero-hallucination discipline with
precise predictive capability, generating the highest overall CWR. This demon-
strates that empirical financial viability requires both rigorous operational gov-
ernance and robust probabilistic reasoning.
6 Conclusion
We presented PolyBench, the first large-scale, contamination-proof benchmark
that evaluates LLMs as trading agents on live decentralized prediction markets.
By coupling 38,666 binary market snapshots with point-in-time CLOB state
and aligned news streams, PolyBench provides a financially-grounded evaluation
standard that static benchmarks cannot replicate.
Across seven state-of-the-art LLMs, onlyMiMo-V2-Flash(17.6% CWR) and
Gemini-3-Flash(6.2% CWR) achieve positive returns, while the remaining five
incur losses despite uniformly high confidence. Three key findings emerge: (1)
LLMs exhibit implicit meta-cognition, consistently assigning higher confidence
to correct predictions; (2) domain competence is highly uneven—strong textual
signals inPoliticsyield alpha, while speculative sectors such asCryptoexpose
severe miscalibration; and (3) instruction adherence is necessary but not suffi-
cient for profitability. Order-book slippage further erodes returns at larger lot
sizes, bounding theoretical predictive advantages by available market depth.
Acknowledgments.This study is funded by National Social Science Fund of China
[grant number 23XJY003].
Disclosure of Interests.The authors have no competing interests to declare that
are relevant to the content of this article.
References
1. Araci, D.: Finbert: Financial sentiment analysis with pre-trained language models.
arXiv preprint arXiv:1908.10063 (2019)
2. Arrow, K.J., Forsythe, R., Gorham, M., Hahn, R., Hanson, R., Ledyard, J.O.,
Levmore, S., Litan, R., Milgrom, P., Nelson, F.D., et al.: The promise of prediction
markets. Science320(5878), 877–878 (2008)

PolyBench: LLM Forecasting and Trading on Prediction Markets 15
3. Barber, R.F., Candes, E.J., Ramdas, A., Tibshirani, R.J.: Conformal prediction
beyond exchangeability. The Annals of Statistics51(2), 816–845 (2023)
4. Bollerslev, T.: Generalized autoregressive conditional heteroskedasticity. Journal
of econometrics31(3), 307–327 (1986)
5. Box, G.E., Jenkins, G.M.: Time series analysis: Forecasting and control. Holden-
Day (1970)
6. Box, G.E., Jenkins, G.M.: Time series analysis. forecasting and control. Holden-
Day Series in Time Series Analysis (1976)
7. Bubeck,S.,Chandrasekaran,V.,Eldan,R.,Gehrke,J.,Horvitz,E.,Kamar,E.,Lee,
P., Lee, Y.T., Li, Y., Lundberg, S., et al.: Sparks of artificial general intelligence:
Early experiments with gpt-4. arXiv preprint arXiv:2303.12712 (2023)
8. Dong, Y., Jiang, X., Liu, H., Jin, Z., Gu, B., Yang, M., Li, G.: Generalization or
memorization: Data contamination and trustworthy evaluation for large language
models (2024),https://arxiv.org/abs/2402.15938
9. Foster, D.P., Vohra, R.: Regret in the on-line decision problem. Games and Eco-
nomic Behavior29(1-2), 7–35 (1999)
10. Halawi,D.,Zhang,F.,Yueh-Han,C.,Steinhardt,J.:Approachinghuman-levelfore-
casting with language models. Advances in Neural Information Processing Systems
37, 50426–50468 (2024)
11. Hendrycks, D., Burns, C., Kadavath, S., Arora, A., Basart, S., Tang, E., Song, D.,
Steinhardt, J.: Measuring mathematical problem solving with the MATH dataset
(2021),https://arxiv.org/abs/2103.03874
12. Hochreiter, S., Schmidhuber, J.: Long short-term memory. Neural computation
9(8), 1735–1780 (1997)
13. Jin, M., Wen, S., Liang, Y., Zhang, C., Xue, S., Wang, X., Zhang, J., Wang, M.,
Chen, H., Li, X., et al.: Time-llm: Time series forecasting by reprogramming large
language models. arXiv preprint arXiv:2310.10688 (2023)
14. Karger, E., Bastani, H., Yueh-Han, C., Jacobs, Z., Halawi, D., Zhang, F., Tetlock,
P.E.: Forecastbench: A dynamic benchmark of ai forecasting capabilities (2025),
https://arxiv.org/abs/2409.19839
15. Lim, B., Zohren, S.: Time-series forecasting with deep learning: a survey. Philo-
sophical Transactions of the Royal Society A379(2194), 20200209 (2021)
16. Liu, A., Feng, B., Xue, B., Wang, B., Wu, B., Lu, C., Zhao, C., Deng, C., Zhang,
C., Ruan, C., et al.: Deepseek-v3 technical report. arXiv preprint arXiv:2412.19437
(2024)
17. Liu,X.,Yu,H.,Zhang,H.,Xu,Y.,Lei,X.,Lai,H.,Gu,Y.,Ding,H.,Men,K.,Yang,
K., et al.: Agentbench: Evaluating llms as agents. In: The Twelfth International
Conference on Learning Representations (2024)
18. Phan, L., Gatti, A., Han, Z., Li, N., Hu, J., Zhang, H., Zhang, C.B.C., Shaaban,
M., Ling, J., Shi, S., et al.: Humanity’s last exam (2025),https://arxiv.org/
abs/2501.14249
19. Saguillo, O., Ghafouri, V., Kiffer, L., Suarez-Tangil, G.: Unravelling the probabilis-
tic forest: Arbitrage in prediction markets. arXiv e-prints pp. arXiv–2508 (2025)
20. Vaswani,A.,Shazeer,N.,Parmar,N.,Uszkoreit,J.,Jones,L.,Gomez,A.N.,Kaiser,
Ł., Polosukhin, I.: Attention is all you need. In: Advances in neural information
processing systems. vol. 30 (2017)
21. Wu, S., Irzan, O., Schleiden, S., et al.: Bloomberggpt: A large language model for
finance. arXiv preprint arXiv:2303.17564 (2023)
22. Yang, Q., Mahns, S., Li, S., Gu, A., Wu, J., Xu, H.: Llm-as-a-prophet: Under-
standing predictive intelligence with prophet arena (2025),https://arxiv.org/
abs/2510.17638

16 P. Cheng et al.
23. Yu, H., Li, F., You, J.: Livetradebench: Seeking real-world alpha with large lan-
guage models (2025),https://arxiv.org/abs/2511.03628
24. Zeng, Z., Liu, J., Chen, S., He, T., Liao, Y., Tian, Y., Wang, J., Wang, Z., Yang,
Y., Yin, L., Yin, M., Zhu, Z., Cai, T., Chen, Z., Chen, J., Du, Y., Gao, X., Guo,
J., Hu, L., Jiao, J., Li, X., Liu, J., Ni, S., Wen, Z., Zhang, G., Zhang, K., Zhou, X.,
Blanchet, J., Qiu, X., Wang, M., Huang, W.: Futurex: An advanced live benchmark
for llm agents in future prediction (2025),https://arxiv.org/abs/2508.11987
25. Zou, A., Xiao, T., Jia, R., Kwon, J., Mazeika, M., Li, R., Song, D., Steinhardt, J.,
Evans, O., Hendrycks, D.: Forecasting future world events with neural networks.
Advances in Neural Information Processing Systems35, 27293–27305 (2022)
