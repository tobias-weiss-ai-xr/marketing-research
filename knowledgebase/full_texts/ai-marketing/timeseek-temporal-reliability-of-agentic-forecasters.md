---
title: 'TimeSeek: Temporal Reliability of Agentic Forecasters'
url: https://arxiv.org/abs/2604.04220
category: ai-marketing
subcategory: empirical
date: 2026-04
venue: ''
authors:
- Hamza Mostafa
- Om Shastri
- Dennis Lee
source: arxiv
pdf_url: https://arxiv.org/pdf/2604.04220
pages: 11
chars: 37298
fetched_at: '2026-11-08T12:57:39+00:00'
kb_version: 1
---

# TimeSeek: Temporal Reliability of Agentic Forecasters

The 2nd ICLR Workshop on Advances in Financial AI: Towards Agentic and Responsible Systems
TIMESEEK: TEMPORALRELIABILITY OFAGENTIC
FORECASTERS
Dennis Lee∗
Automorphic Labs
432dennis@gmail.com
Hamza Mostafa∗
Cheriton School of Computer Science
University of Waterloo
hamza.mostafa@uwaterloo.ca
Om Shastri∗
The Wharton School
University of Pennsylvania
omshastri@gmail.com
ABSTRACT
We introduce TimeSeek, a benchmark for studying how the reliability of agentic
LLM forecasters changes over a prediction market’s lifecycle. We evaluate 10
frontier models on 150 CFTC-regulated Kalshi binary markets at five temporal
checkpoints, with and without web search, for 15,000 forecasts total. Models are
most competitive early in a market’s life and on high-uncertainty markets, but much
less competitive near resolution and on strong-consensus markets. Web search
improves pooled Brier Skill Score (BSS) for every model overall, yet hurts in
12% of model-checkpoint pairs, indicating that retrieval is helpful on average but
not uniformly so. Simple two-model ensembles reduce error without surpassing
the market overall. These descriptive results motivate time-aware evaluation and
selective-deference policies rather than a single market snapshot or a uniform
tool-use setting.
1 INTRODUCTION
When should an autonomous AI agent’s forecast be trusted relative to a prediction market? Existing
LLM forecasting benchmarks usually evaluate a single snapshot per question or market (Nel, 2025;
Karger et al., 2024; Ye et al., 2024). That setup obscures an important temporal issue: prediction
markets aggregate information continuously, so early prices can reflect sparse participation while late
prices often incorporate much richer information. A model that is competitive early but weak late has
a very different reliability profile from one that underperforms uniformly.
We study this question with TimeSeek, a benchmark built from 150 CFTC-regulated Kalshi binary
markets evaluated at five lifecycle checkpoints under two conditions: with and without web search.
This yields 15,000 model forecasts across 10 frontier models. Rather than treating “LLMs vs. markets”
as a single aggregate comparison, our goal is to characterize when models are relatively competitive,
when retrieval helps, and when deferring to the market remains the stronger default. Throughout,
we treat these comparisons as descriptive: the paper reports point estimates, while uncertainty
quantification for subgroup analyses is left to future work. Our main contributions are:
1. Time-aware evaluation of agentic forecasters.We introduce a temporal benchmark and
with/without-search ablation that measures model performance at five points in each market’s
lifecycle rather than at a single snapshot.
2. Descriptive evidence of temporal and difficulty-dependent performance.Models are
most competitive early in a market’s life and on high-uncertainty markets, but substantially
less competitive late in the lifecycle and on strong-consensus markets.
3. Evidence for selective rather than uniform tool use.Web search improves pooled BSS
for all 10 models overall, but degrades performance in 12% of model–checkpoint conditions
and shows strong category-specific heterogeneity.
4. A simple ensemble baseline.Model–market error correlations are modest ( r= 0.19 –0.41),
and simple two-model averaging reduces loss relative to the best single model, though no
pair surpasses the market overall.
∗Equal contribution.
1
arXiv:2604.04220v1  [cs.AI]  5 Apr 2026

The 2nd ICLR Workshop on Advances in Financial AI: Towards Agentic and Responsible Systems
Table 1: TimeSeek dataset characteristics.
Characteristic Value
Markets / Checkpoints / Predictions 150 / 5 / 750 per condition
Categories 5 (30 markets each)
Timeline Oct 2025 – Jan 2026
Trading volume $5.6k – $41.3M (med. $35k)
Duration (days) 2 – 337 (med. 89)
Outcomes 73% NO, 27% YES
2 RELATEDWORK
LLM forecasting and prediction benchmarks.KalshiBench (Nel, 2025) evaluates LLMs on thou-
sands of Kalshi markets at fixed snapshots and highlights systematic miscalibration. ForecastBench
(Karger et al., 2024) and Prophet Arena (Yang et al., 2025b) move toward dynamic evaluation on
live markets, while Mirai (Ye et al., 2024) emphasizes event-driven time sensitivity. TruthTensor
(Shahabi et al., 2026) evaluates LLMs under market drift with emphasis on human imitation, but
does not control for tool access or analyze within-market lifecycle dynamics. Our work complements
this literature with a controlled tool-use ablation across temporal checkpoints and difficulty regimes.
Adjacent work studies forecasting-specific reliability via consistency checks (Paleka et al., 2024) and
uncertainty-aware training (Damani et al., 2025).
Agentic AI for financial decision-making.Beyond forecasting, benchmarks increasingly measure
end-to-end agent performance in market interaction, including multi-market trading (Qian et al., 2025;
Yu et al., 2025) and financial decision-making (Li et al., 2025). These stress execution and feedback
loops; we focus on the upstream question of forecast reliability—whether an agent’s probabilistic
prediction should be trusted before any trading decision is made.
Tool use and temporal drift.Tool access can improve task performance (Schick et al., 2023),
but tool-augmented workflows can distort confidence (Xuan et al., 2026) and deeper reasoning can
degrade calibration (Lacombe et al., 2025). Broader concerns about temporal drift in LLM behavior
motivate evaluation protocols that are explicitly time-aware (Khairnar, 2025; Zhang et al., 2025).
Our temporal checkpoint design directly tests these stability and reliability issues in a high-stakes
forecasting setting.
Prediction markets as baselines.Prediction markets are generally well-calibrated across many
domains (Wolfers & Zitzewitz, 2004; Arrow et al., 2008), and crowd forecasting systems span
markets, polls, and elite forecasters (Atanasov et al., 2022). We use contemporaneous market prices
as the baseline, consistent with the view that market-implied probabilities are strong default forecasts
(Wolfers & Zitzewitz, 2004; Fama, 1970).
3 METHOD
3.1 DATASET: CFTC-REGULATEDBINARYMARKETS
We collect 150 binary markets from Kalshi, a CFTC-regulated exchange where real capital is at risk.
Each market resolves to YES/NO based on objective criteria (election results, economic releases,
sports scores). We enforce $5,000+ trading volume per market and require post-October 2025
resolution to ensure temporal separation from model training cutoffs. Concretely, we set the cutoff
date to the latest publicly stated knowledge cutoff among the models we evaluate (October 2025),
and keep only markets whose resolution occurs after that date to minimize outcome contamination (a
KalshiBench-style filtering rule) (Nel, 2025). The dataset spans five categories (30 markets each):
Politics, Sports, Macro-Economics, Science/Tech, and Financial markets. Table 1 provides statistics.
3.2 TEMPORALSAMPLINGPROTOCOL
For each market, we define lifecycle progress
p(t) = t−t open
tclose −t open
2

The 2nd ICLR Workshop on Advances in Financial AI: Towards Agentic and Responsible Systems
and sample at 5 checkpoints: Open+1 (p= 0.01 ), 25%, 50%, 75%, and Close-1 (p= 0.99 ). For each
sample, we record sample date, market price, and ground truth outcome, yielding 750 samples per
model per condition (with/without search), totaling 15,000 predictions.
3.3 AGENTICFORECASTINGARCHITECTURE
We implement agentic forecasters as a 4-node state machine: research (initialize context) → agent
(decide to search or predict) → tools (execute searches) → forecast (extract structured prediction).
The agent loops between agent and tools until it produces a final forecast.
When web search is enabled (agentic condition), agents access web search with date filtering (results
restricted to before the sample date) to prevent future information leakage. When disabled (baseline
condition), the model receives the identical prompt but cannot invoke any tools, isolating parametric
knowledge. Market prices are withheld during prediction to prevent anchoring.
3.4 MODELSEVALUATED
We evaluate 10 frontier LLMs: Claude Opus 4.5 (Anthropic, 2025), GPT-5.2 (OpenAI, 2025), Gemini
3 Pro (Google, 2025), Grok 4.1-fast (xAI, 2025), Kimi-k2 (Xu et al., 2025), Kimi-k2.5 (Moonshot AI,
2026), DeepSeek v3.2 (DeepSeek-AI, 2025), Intellect-3 (Prime Intellect Team et al., 2025), Trinity
Large (Arcee AI, 2026), and Qwen3-235B (Yang et al., 2025a). Each model predicts on 150 markets
× 5 checkpoints = 750 samples per condition, yielding 750×10 models ×2 conditions = 15,000
total predictions.
3.5 EVALUATIONMETRICS
Brier Score (BS):
BS = 1 N
NX
i=1
(ˆpi −y i)2,
whereˆpi is predicted probability andy i ∈ {0,1}(Brier, 1950).
Brier Skill Score (BSS):
BSS = 1− BSmodel
BSmarket
,
using market price at prediction time as baseline (Murphy, 1973). Positive BSS indicates beating
markets.
4 RESULTS
Unless otherwise noted, the results below are descriptive point estimates without confidence intervals,
so subgroup comparisons should be interpreted with appropriate caution.
4.1 TEMPORALDEGRADATION ANDINFORMATIONREGIMES
Table 2 presents BSS for all models with web search. Four models outperform the market baseline at
Open+1 (Claude +0.167, Kimi-k2.5 +0.118, GPT +0.085, Kimi-k2 +0.011), but all underperform it
by Close-1 (BSS <−0.7 ). Performance declines monotonically across 9 of 10 models, with Kimi-k2
showing a slight recovery at Close-1.
One plausible interpretation is that the benchmark spans two broad information regimes. Early in
the market lifecycle (Open+1, 25%), prices may reflect thinner participation, leaving more room for
a web-enabled model to surface relevant public information that is not yet fully incorporated into
price. Late in the lifecycle (75%, Close-1), the market is a much stronger baseline after aggregating
more trades and more diverse signals (Atanasov et al., 2022). Under this interpretation, the apparent
crossover occurs between 25–50% of the lifecycle for the strongest models (Claude, GPT) and earlier
for weaker models. We treat this as a descriptive pattern rather than a causal identification of market
microstructure.
3

The 2nd ICLR Workshop on Advances in Financial AI: Towards Agentic and Responsible Systems
Table 2: BSS across temporal checkpoints with web search. Bold = beating market (BSS>0).
Model Open+1 25% 50% 75% Close-1 Pooled
Claude Opus 4.5+0.167 +0.059-0.136 -0.165 -0.829 -0.068
GPT-5.2+0.085-0.095 -0.344 -0.595 -0.960 -0.252
Gemini 3 Pro -0.084 -0.250 -0.373 -0.510 -0.734 -0.312
Grok 4.1-fast -0.003 -0.071 -0.314 -0.621 -0.909 -0.267
Kimi-k2.5+0.118-0.022 -0.311 -0.579 -0.942 -0.214
Kimi-k2+0.011-0.113 -0.601 -0.912 -0.823 -0.367
DeepSeek v3.2 -0.064 -0.424 -0.690 -0.870 -1.158 -0.507
Intellect-3 -0.057 -0.433 -0.641 -0.698 -1.736 -0.527
Trinity Large -0.128 -0.275 -0.581 -0.684 -1.716 -0.496
Qwen3-235B -0.132 -0.401 -0.955 -1.018 -1.334 -0.615
Table 3: ∆BSS (agentic minus baseline). Bold = search helped. Shaded = search hurt—model was
better without tools.
Model Open+1 25% 50% 75% Close-1 Pooled
Claude Opus 4.5+0.189 +0.378 +0.540 +0.816 +1.383 +0.520
GPT-5.2 -0.040+0.108 +0.130 +0.087 +0.893 +0.140
Gemini 3 Pro -0.080+0.218 +0.246 +0.525 +1.693 +0.325
Grok 4.1-fast+0.214 +0.457 +0.721 +0.679 +1.710 +0.592
Kimi-k2 -0.025+0.234 -0.135 -0.146+1.388 +0.135
Kimi-k2.5+0.110 +0.180 +0.172 +0.195 +0.777 +0.218
DeepSeek v3.2+0.053 +0.090 +0.097 +0.193 +1.044 +0.190
Intellect-3+0.135 -0.049+0.107 +0.662 +0.729 +0.228
Trinity Large+0.000 +0.148 +0.389 +0.304 +0.816 +0.240
Qwen3-235B+0.037 +0.280 +0.063 +0.101 +1.416 +0.245
4.2 WEBSEARCH: A DOUBLE-EDGEDSWORD
Web search improves pooled BSS by 0.14–0.59 points across all models. However, computing
∆BSS = BSS agentic −BSS baseline for every model-checkpoint pair (Table 3) reveals that 6 of 50
conditions have negative ∆BSS. GPT-5.2 at Open+1, for example, drops from BSS +0.125 (baseline)
to +0.085 (agentic), and Kimi-k2 is worse with search at three checkpoints (Open+1, 50%, 75%).
These cases show that average gains from retrieval mask substantial heterogeneity across models and
time.
This pattern is consistent with prior work suggesting that tool use can distort confidence and calibration
in agentic workflows (Xuan et al., 2026): more information processing is not uniformly beneficial.
Further analysis shows a non-monotonic association between Claude’s search count and BSS (Table 4),
with the best observed bucket at 4–7 queries (+0.109). We interpret this pattern cautiously because
query count is endogenous to the agent’s behavior and may also reflect question difficulty.
Implication for selective tool use.These results suggest that unrestricted tool access should not be
assumed to help uniformly. A more realistic design target is an explicit tool-use policy that governs
when to search, when to rely on parametric knowledge, and how many iterations to permit before
forcing a prediction.
4.3 LLMSAREMOSTCOMPETITIVE ONHIGH-UNCERTAINTYMARKETS
Do LLMs and markets struggle on the same questions? We operationalize market difficulty using
price distance from certainty: a market at 50% represents maximum crowd uncertainty (toss-up),
while one at 5% or 95% represents strong consensus (easy). Table 5 stratifies BSS by four such tiers.
Because this definition is derived from market prices, we interpret the analysis as showing where
models are relatively competitive against the market, not as a pure measure of intrinsic task difficulty.
Seven of ten models achieve positive BSS on toss-up markets. Claude leads at +0.301, followed by
GPT (+0.217), Kimi-k2.5 (+0.179), and Kimi-k2 (+0.098). Three weaker models (Intellect-3, Trinity,
Qwen3) remain negative even on toss-ups. The pattern reverses sharply for easy markets: all models
4

The 2nd ICLR Workshop on Advances in Financial AI: Towards Agentic and Responsible Systems
Table 4: Search count vs. BSS (Claude). Performance is non-monotonic across query-count buckets.
SearchesnBSS
1–3 48 -0.811
4–7 152+0.109
8–12 238 +0.007
13+ 312 -0.115
Table 5: BSS stratified by market difficulty (d=|p m −0.5| ): Easy d >0.4, Medium 0.2< d≤0.4 ,
Hard0.1< d≤0.2, Toss-upd≤0.1. Bold = beating market.
Model Easy Medium Hard Toss-up Overall
Claude Opus 4.5 -0.692 -0.188+0.074 +0.301-0.068
GPT-5.2 -1.069 -0.433 -0.001+0.217-0.252
Gemini 3 Pro -0.829 -0.365 -0.346+0.047-0.312
Grok 4.1-fast -0.905 -0.256 -0.201+0.002-0.267
Kimi-k2.5 -1.125 -0.316+0.077 +0.179-0.214
Kimi-k2 -0.906 -0.555 -0.296+0.098-0.366
DeepSeek v3.2 -1.308 -0.669 -0.413+0.041-0.507
Intellect-3 -1.680 -0.625 -0.108 -0.109 -0.527
Trinity Large -1.235 -0.688 -0.260 -0.041 -0.496
Qwen3-235B -1.502 -0.857 -0.238 -0.123 -0.615
nper tier: Easy: 254, Medium: 267, Hard: 100, Toss-up: 129
show strongly negative BSS (from -0.692 to -1.680). Taken descriptively, this monotonic gradient
suggests that current models are relatively most competitive when the market itself is most uncertain,
and least competitive when market consensus is strong.
Pearson correlation between model absolute error and market absolute error (Table 6) points in a
similar direction: all models show low-to-moderate correlation ( r= 0.19 –0.41), suggesting only
partial overlap between model and market error patterns. Intellect-3 shows the lowest correlation
(r= 0.193 ) yet performs poorly on toss-ups, indicating that error diversity alone is not enough;
accuracy matters too. Grok shows the highest correlation (r= 0.408 ), most closely tracking market
pricing patterns.
Contrarian disagreement by difficulty.When Claude strongly disagrees with markets ( |ˆp−pm|>
0.20, n= 303 ), the outcome depends strongly on the market-uncertainty tier: contrarian cases on
toss-ups achieve 80.9% win rate (BSS +0.476, n= 68 ) and 65.4% on hard markets (BSS +0.166,
n= 52 ), but lose on easy markets (19.8% win rate, BSS -0.720, n= 81 ). Within this benchmark,
disagreement appears more informative when the market is uncertain than when consensus is strong,
though we do not treat this offline analysis as a validated trading rule.
Ensemble potential.The low-to-moderate error correlations ( r= 0.19 –0.41) suggest some room
for diversification via simple averaging (Bates & Granger, 1969). The best two-model pair (Claude
+ Kimi-k2.5) reduces Claude’s pooled BSS loss by 40% (from -0.068 to -0.041), though no pair
achieves positive overall BSS. All top ensembles include Claude, suggesting that base model quality
still dominates any ensemble gains.
4.4 CATEGORY-LEVELHETEROGENEITY INSEARCHIMPACT
Table 7 shows category-specific performance across all 10 models. Claude is strongest in Sports
(+0.294) and Macro (+0.163); Kimi-k2.5 also shows positive Sports BSS (+0.124), and GPT and
Gemini show positive Macro BSS. By contrast, all models are negative in Politics and Financial
markets. A plausible interpretation is that these categories contain more information that is hard to
recover reliably with periodic public-web retrieval alone.
Search impact also varies sharply by category. Table 8 presents ∆BSS (agentic minus baseline) for
all models. Search helps all 10 models in Macro (avg ∆BSS +0.96) and Sports (avg +0.39), but is
negative for most models in Politics (7 of 10; avg∆BSS -0.08) and Sci/Tech (6 of 10; avg -0.03). The
5

The 2nd ICLR Workshop on Advances in Financial AI: Towards Agentic and Responsible Systems
Table 6: Error correlation (|ˆp−y| vs. |pm −y| ). Lower r indicates less overlap between model and
market error patterns. Allp <10 −6.
Model Pearsonr
Intellect-3 0.193
Claude Opus 4.5 0.211
Trinity Large 0.218
Kimi-k2.5 0.222
DeepSeek v3.2 0.256
Qwen3-235B 0.261
Kimi-k2 0.291
GPT-5.2 0.336
Gemini 3 Pro 0.340
Grok 4.1-fast 0.408
Table 7: BSS by category (agentic condition). Bold = beating markets.
Model Politics Sports Macro Sci/Tech Financial
Claude Opus 4.5 -0.379+0.294 +0.163-0.154 -0.609
GPT-5.2 -0.484 -0.088+0.021-0.378 -0.482
Gemini 3 Pro -0.598 -0.227+0.033-0.575 -0.217
Grok 4.1-fast -0.427 -0.197 -0.182 -0.190 -0.426
Kimi-k2.5 -0.596+0.124-0.066 -0.213 -0.625
Kimi-k2 -0.421 -0.342 -0.023 -0.369 -0.788
DeepSeek v3.2 -0.703 -0.110 -0.333 -0.596 -1.182
Intellect-3 -0.706 -0.255 -0.275 -0.569 -1.131
Trinity Large -0.376 -0.231 -0.342 -0.605 -1.232
Qwen3-235B -1.020 -0.046 -0.601 -0.719 -1.158
most striking case is GPT-5.2 in Politics: its baseline nearly matches market accuracy (BSS -0.005
without search), but search degrades it to -0.484. Financial markets are evenly split (5 helped, 5 hurt),
and Grok is the only model with positive ∆BSS across all five categories. Overall, the evidence
favors category-aware tool policies over a uniform “always search” rule.
5 DISCUSSION
5.1 FROM“FORECASTING”TO SELECTIVE DECISION:WHEN TO DEFER TO MARKETS
Our results suggest a useful framing is not “LLMs vs. markets” as a single contest, but a selective
decision problem that chooses when to (i) forecast directly, (ii) search then forecast, or (iii) defer to
the market price. This is closely related to selective prediction / classification-with-rejection, where a
system trades coverage for lower risk and more reliable probabilistic outputs (Geifman & El-Yaniv,
2017; Franc & Pruša, 2023; Cortes et al., 2016; 2024; Mao et al., 2024). In our setting, deference
corresponds to using the contemporaneous market-implied probability as a default baseline, consistent
with the view that prediction markets often provide strong probabilistic forecasts in many domains
(Wolfers & Zitzewitz, 2004; Arrow et al., 2008; Plott & Sunder, 1988), while still acknowledging
that prices only partially identify mean beliefs (Manski, 2006). This perspective turns TimeSeek into
a problem of learning a gating function g(x)∈ {defer,predict,search}, potentially with a search
budget, that optimizes a proper scoring objective (Gneiting & Raftery, 2007). It also suggests that
coverage–risk tradeoffs may be more decision-relevant than unconditional BSS alone (Geifman &
El-Yaniv, 2017; Franc & Pruša, 2023). Post-hoc calibration methods such as temperature scaling and
Platt scaling could map raw model scores into more reliable probabilities before a gating decision
(Guo et al., 2017; Platt, 1999; Kuleshov et al., 2018), and conformal methods offer another route to
coverage guarantees under stronger assumptions (Shafer & V ovk, 2008).
6

The 2nd ICLR Workshop on Advances in Financial AI: Towards Agentic and Responsible Systems
Table 8: ∆BSS by category (agentic minus baseline). Bold = search helped. Shaded = search hurt.
Bottom row: models helped / total and category average.
Model Politics Sports Macro Sci/Tech Financial
Claude Opus 4.5 -0.107+0.657 +1.571 +0.217 +0.072
GPT-5.2 -0.479+0.293 +0.870 -0.170+0.074
Gemini 3 Pro+0.135 +0.218 +1.084 -0.267+0.604
Grok 4.1-fast+0.209 +0.440 +1.392 +0.263 +0.792
Kimi-k2.5 -0.384+0.660 +0.711 -0.113 -0.129
Kimi-k2 -0.030+0.252 +0.868 -0.169 -0.430
DeepSeek v3.2 -0.240+0.301 +0.845 +0.051 -0.160
Intellect-3 -0.018+0.230 +0.588 +0.053 +0.302
Trinity Large+0.336 +0.349 +0.806 -0.179 -0.260
Qwen3-235B -0.202+0.530 +0.856 -0.024 -0.203
# helped / avg 3/10; -0.08 10/10; +0.39 10/10; +0.96 4/10; -0.03 5/10; +0.07
5.2 WHY TEMPORAL CROSSOVER IS EXPECTED:AGGREGATION,FRICTIONS,AND
UNDERREACTION
The late-stage degradation is consistent with classic theories of information aggregation and frictions,
though our benchmark does not directly identify those mechanisms. In prediction markets, prices
can aggregate dispersed information and heterogeneous beliefs (Wolfers & Zitzewitz, 2004; Plott
& Sunder, 1988), even if that aggregation is imperfect and prices only partially identify the full
distribution of beliefs (Manski, 2006). Early in a contract’s life, liquidity and participation can be
thin, and prices may underreact to public signals due to limited attention, participation constraints,
or capital frictions (Ottaviani & Sørensen, 2015; Shleifer & Vishny, 1997; De Long et al., 1990).
These are precisely the settings in which web-enabled agents may add value by surfacing relevant
public evidence that is available but not yet fully priced. As resolution approaches, however, markets
typically incorporate real-time signals more quickly, and the marginal value of periodic retrieval
shrinks relative to a continuously updated market. This framing also suggests one reason categories
may differ: some domains may rely more heavily on information that is difficult to recover from
public web search alone.
5.3 TOOL ACCESS IS NOT MONOTONE:RETRIEVAL CAN INCREASE VARIANCE AND
MISCALIBRATION
The finding that search sometimes hurts is consistent with emerging evidence that tool use can distort
confidence and calibration in agentic workflows. Evidence tools such as web search can inject noisy,
conflicting, or low-veracity signals that increase variance unless the agent has strong verification
or calibration mechanisms (Xuan et al., 2026). At the same time, Lacombe et al. (2025) report
calibration gains from search-augmented generation in general QA settings, which suggests that the
value of retrieval is likely task- and domain-dependent rather than universal.
Our category-level analysis sharpens that point. Search helps uniformly in Macro and Sports, but is
often neutral or harmful in Politics and Sci/Tech. We view this as consistent with a public-vs-private
information story: some categories may be better matched to periodic public-web retrieval than others.
The non-monotonic relationship between Claude’s query count and performance points in the same
general direction, but should be interpreted cautiously because search depth is itself a behavioral
outcome. Taken together, these results motivate treating search as a budgeted, category-aware
resource, potentially with explicit stopping rules, verification checks, and post-retrieval calibration
(Paleka et al., 2024; Gneiting & Raftery, 2007; Guo et al., 2017; Damani et al., 2025).
5.4 ENSEMBLING AND MARKET–MODEL HYBRIDS:WHY SIMPLE AVERAGES HELP
That a two-model average reduces BSS loss is consistent with the forecasting-combination literature:
combining partially independent predictors often reduces mean squared error, and simple averaging
can be robust to weight misspecification (Bates & Granger, 1969; Clemen, 1989; Bunn, 1988;
de Menezes et al., 2000). In our setting, a natural next step is a conditional hybrid over the market and
7

The 2nd ICLR Workshop on Advances in Financial AI: Towards Agentic and Responsible Systems
multiple models, where weights depend on temporal position and uncertainty tier. This suggests a
concrete research direction: learn conditional weights, or a gating policy, that optimize proper scoring
rules while controlling calibration and abstention behavior (Gneiting & Raftery, 2007; Geifman &
El-Yaniv, 2017; Franc & Pruša, 2023).
5.5 LIMITATIONS
Statistical uncertainty and subgroup size.We report point estimates throughout. With 150 mar-
kets, the benchmark supports strong directional patterns, but several subgroup analyses—especially
category × time and difficulty slices—would benefit from bootstrap confidence intervals or other
uncertainty estimates. Larger samples would also support more stable learned gating or weighting
policies (Geifman & El-Yaniv, 2017; de Menezes et al., 2000).
Market-defined difficulty and baseline heterogeneity.Our difficulty tiers are derived from market
prices, and BSS also uses the contemporaneous market as the baseline. The analysis is therefore
best read as identifying where models are relatively competitive against the market, not as a clean
decomposition of intrinsic task difficulty. More broadly, market prices embed heterogeneous belief
aggregation and may underreact depending on liquidity, participation, and contract microstructure
(Manski, 2006; Ottaviani & Sørensen, 2015; Shleifer & Vishny, 1997).
Offline evaluation rather than live trading.We compare model forecasts to contemporaneous
market prices, but we do not model execution, transaction costs, slippage, latency, or market impact.
The results should therefore be interpreted as evidence about forecast quality relative to a market
baseline, not as a validated trading strategy evaluation.
Tooling scope and outcome skew.We study only web search; richer tool suites may shift the
observed crossover (Xuan et al., 2026). The NO-heavy outcome distribution (73%) can also interact
with conservative prediction strategies and calibration (Gneiting & Raftery, 2007; Guo et al., 2017).
5.6 FUTUREWORK
Learn the gate.Learn a policy g(x) that chooses defer/predict/search and sets a retrieval budget,
optimizing proper scoring rules while controlling calibration and abstention (Gneiting & Raftery,
2007; Geifman & El-Yaniv, 2017; Franc & Pruša, 2023; Xuan et al., 2026).
Streaming forecasters.Replace one-shot retrieval with periodic updates and sequential decision-
making, aligning agent updates with the market’s continuous aggregation while explicitly managing
variance and calibration drift (Ottaviani & Sørensen, 2015; Xuan et al., 2026).
Mechanism-aware training sandboxes.Many prediction markets rely on market-making mecha-
nisms such as LMSR; integrating mechanism design and learning could enable controlled experiments
on aggregation efficiency and agent impact (Hanson, 2003; Plott & Sunder, 1988).
Market–model combination rules.Extend from fixed averages to conditional combination schemes
informed by forecast-combination theory and abstention, with guarantees on calibration/coverage
(Bates & Granger, 1969; Clemen, 1989; de Menezes et al., 2000; Shafer & V ovk, 2008).
Post-training via market-resolved rewards.Market outcomes provide verifiable binary labels at
scale, making them natural reward signals for reinforcement learning. Fine-tuning forecasters with
Brier-based RL rewards (Damani et al., 2025) on resolved markets could directly optimize calibration,
with the gating policy learned jointly to control when the agent searches, predicts, or defers.
REPRODUCIBILITY
Code and data for TimeSeek are available in the accompanying repository at https://github.
com/coys17/timeseek-anonymous.git. The repository includes the forecasting harness,
temporal sampling pipeline, evaluation scripts, and the dataset of 150 Kalshi markets across five
checkpoints.
8

The 2nd ICLR Workshop on Advances in Financial AI: Towards Agentic and Responsible Systems
REFERENCES
Anthropic. Claude opus 4.5. Anthropic product page / announcements, 2025. URL https:
//www.anthropic.com/claude/opus.
Arcee AI. Trinity large. Arcee AI blog, 2026. URL https://www.arcee.ai/blog/
trinity-large.
Kenneth J. Arrow, Robert Forsythe, Michael Gorham, Robert Hahn, Robin Hanson, John O. Ledyard,
Saul Levmore, Robert Litan, Paul Milgrom, Forrest D. Nelson, et al. The promise of prediction
markets.Science, 320(5878):877–878, 2008. doi: 10.1126/science.1157679.
Pavel Atanasov, Jens Witkowski, Barbara Mellers, and Philip E. Tetlock. Crowd prediction systems:
Markets, polls, and elite forecasters. InProceedings of the 23rd ACM Conference on Economics
and Computation, pp. 1013–1014, 2022.
J. M. Bates and C. W. J. Granger. The combination of forecasts.Journal of the Operational Research
Society, 20(4):451–468, 1969. doi: 10.1057/jors.1969.103.
Glenn W. Brier. Verification of forecasts expressed in terms of probability.Monthly Weather Review,
78(1):1–3, 1950.
Derek W. Bunn. Combining forecasts.European Journal of Operational Research, 33(3):223–229,
1988.
Robert T. Clemen. Combining forecasts: A review and annotated bibliography.International Journal
of Forecasting, 5(4):559–583, 1989. doi: 10.1016/0169-2070(89)90012-5.
Corinna Cortes, Giulia DeSalvo, and Mehryar Mohri. Learning with rejection. arXiv preprint, 2016.
URLhttps://cs.nyu.edu/~mohri/pub/rej.pdf.
Corinna Cortes, Giulia DeSalvo, and Mehryar Mohri. Theory and algorithms for learning with
rejection in binary classification.Annals of Mathematics and Artificial Intelligence, 92:277–315,
2024. doi: 10.1007/s10472-023-09899-2.
Mehul Damani, Ishaan Puri, Stephen Slocum, Idan Shenfeld, Leshem Choshen, Yejin Kim, and Jacob
Andreas. Beyond binary rewards: Training lms to reason about their uncertainty. arXiv preprint
arXiv:2507.16806, 2025.
J. Bradford De Long, Andrei Shleifer, Lawrence H. Summers, and Robert J. Waldmann. Noise trader
risk in financial markets.Journal of Political Economy, 98(4):703–738, 1990. doi: 10.1086/261703.
Lilian D. de Menezes, Derek W. Bunn, and James W. Taylor. Review of guidelines for the use of
combined forecasts.European Journal of Operational Research, 120(1):190–204, 2000. doi:
10.1016/S0377-2217(98)00380-4.
DeepSeek-AI. Deepseek-v3.2: Pushing the frontier of open large language models. arXiv preprint
arXiv:2512.02556, 2025.
Eugene F. Fama. Efficient capital markets: A review of theory and empirical work.The Journal of
Finance, 25(2):383–417, 1970.
Václav Franc and Daniel Pruša. Optimal strategies for reject option classifiers.Journal of Ma-
chine Learning Research, 24(47):1–54, 2023. URL https://jmlr.org/papers/v24/
21-0048.html.
Yonatan Geifman and Ran El-Yaniv. Selective classification for deep neural networks. arXiv preprint
arXiv:1705.08500, 2017. URLhttps://arxiv.org/abs/1705.08500.
Tilmann Gneiting and Adrian E. Raftery. Strictly proper scoring rules, prediction, and es-
timation.Journal of the American Statistical Association, 102(477):359–378, 2007. doi:
10.1198/016214506000001437.
Google. A new era of intelligence with gemini 3. Google Blog, 2025. URL https://blog.
google/products/gemini/gemini-3/.
9

The 2nd ICLR Workshop on Advances in Financial AI: Towards Agentic and Responsible Systems
Chuan Guo, Geoff Pleiss, Yu Sun, and Kilian Q. Weinberger. On calibration of modern neural
networks. InInternational Conference on Machine Learning (ICML), 2017. URL https:
//arxiv.org/abs/1706.04599.
Robin Hanson. Combinatorial information market design.Information Systems Frontiers, 5(1):
107–119, 2003. doi: 10.1023/A:1022058209073.
Ezra Karger, Houtan Bastani, Yueh-Han Chen, Zachary Jacobs, Danny Halawi, Fred Zhang, and
Philip E. Tetlock. Forecastbench: A dynamic benchmark of AI forecasting capabilities. arXiv
preprint arXiv:2409.19839, 2024.
Sachin Khairnar. A survey of temporal drift in large language models. Authorea
Preprints, 2025. URL https://www.techrxiv.org/users/978357/articles/
1350495-a-survey-of-temporal-drift-in-large-language-models.
V olodymyr Kuleshov, Nathan Fenner, and Stefano Ermon. Accurate uncertainties for deep learning
using calibrated regression. InInternational Conference on Machine Learning (ICML), 2018. URL
https://arxiv.org/abs/1807.00263.
Romain Lacombe, Kerrie Wu, and Eddie Dilworth. Don’t think twice! over-reasoning impairs
confidence calibration. arXiv preprint arXiv:2508.15050, 2025. URL https://arxiv.org/
abs/2508.15050.
Hong Li, Yinan Cao, Yujie Yu, S. R. Javaji, Zhi Deng, Yuhang He, Yutong Jiang, Zhenyu Zhu,
K. Subbalakshmi, Jie Huang, et al. Investorbench: A benchmark for financial decision-making
tasks with llm-based agent. InProceedings of the 63rd Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers), pp. 2509–2525, 2025.
Charles F. Manski. Interpreting the predictions of prediction markets.Economics Letters, 91(3):
425–429, 2006. doi: 10.1016/j.econlet.2006.01.004.
Anqi Mao et al. Predictor-rejector multi-class abstention. InProceedings of The 35th International
Conference on Algorithmic Learning Theory (ALT), 2024. URL https://proceedings.
mlr.press/v237/mao24a.html.
Moonshot AI. Kimi k2.5: Visual agentic intelligence. Technical report / blog, 2026. URL https:
//www.kimi.com/blog/kimi-k2-5.html.
Allan H. Murphy. A new vector partition of the probability score.Journal of Applied Meteorology,
12(4):595–600, 1973.
Lukas Nel. Do large language models know what they don’t know? KalshiBench: A new benchmark
for evaluating epistemic calibration via prediction markets. arXiv preprint arXiv:2512.16030,
2025.
OpenAI. Introducing gpt-5.2. OpenAI blog, 2025. URL https://openai.com/index/
introducing-gpt-5-2/.
Marco Ottaviani and Peter Norman Sørensen. Price reaction to information with heterogeneous
beliefs and wealth effects: Underreaction, momentum, and reversal.American Economic Review,
105(1):1–34, 2015. doi: 10.1257/aer.20120881.
Daniel Paleka, A. P. Sudhir, A. Alvarez, V . Bhat, A. Shen, E. Wang, and Florian Tramèr. Consistency
checks for language model forecasters. arXiv preprint arXiv:2412.18544, 2024.
John C. Platt. Probabilistic outputs for support vector machines and comparisons to regularized
likelihood methods. InAdvances in Large Margin Classifiers, pp. 61–74. 1999.
Charles R. Plott and Shyam Sunder. Rational expectations and the aggregation of diverse information
in laboratory security markets.Econometrica, 56(5):1085–1118, 1988. doi: 10.2307/1911360.
Prime Intellect Team et al. Intellect-3: Technical report. arXiv preprint arXiv:2512.16144, 2025.
10

The 2nd ICLR Workshop on Advances in Financial AI: Towards Agentic and Responsible Systems
Le Qian, Xiaoyuan Peng, Yuyang Wang, V . J. Zhang, Hao He, Hannah Smith, Yuxuan Han, Yuhang
He, Hong Li, Yinan Cao, et al. When agents trade: Live multi-market trading benchmark for llm
agents. arXiv preprint arXiv:2510.11695, 2025.
Timo Schick et al. Toolformer: Language models can teach themselves to use tools.Advances in
Neural Information Processing Systems, 36, 2023.
Glenn Shafer and Vladimir V ovk. A tutorial on conformal prediction.Journal of Machine Learning
Research, 9:371–421, 2008. URLhttps://jmlr.org/papers/v9/shafer08a.html.
Shirin Shahabi, Spencer Graham, and Haruna Isah. Truthtensor: Evaluating llms through human
imitation on prediction market under drift and holistic reasoning. arXiv preprint arXiv:2601.13545,
2026.
Andrei Shleifer and Robert W. Vishny. The limits of arbitrage.The Journal of Finance, 52(1):35–55,
1997. doi: 10.1111/j.1540-6261.1997.tb03807.x.
Justin Wolfers and Eric Zitzewitz. Prediction markets.Journal of Economic Perspectives, 18(2):
107–126, 2004. doi: 10.1257/0895330041371321.
xAI. Grok 4.1. xAI news, 2025. URLhttps://x.ai/news/grok-4-1/.
Lin Xu et al. Kimi k2: Open agentic intelligence. arXiv preprint arXiv:2507.20534, 2025.
Weihao Xuan, Qingcheng Zeng, Heli Qi, Yunze Xiao, Junjue Wang, and Naoto Yokoya. The
confidence dichotomy: Analyzing and mitigating miscalibration in tool-use agents. arXiv preprint
arXiv:2601.07264, 2026. URLhttps://arxiv.org/abs/2601.07264.
An Yang et al. Qwen3 technical report. arXiv preprint arXiv:2505.09388, 2025a.
Qingchuan Yang, Simon Mahns, Sida Li, Anri Gu, Jibang Wu, and Haifeng Xu. Llm-as-a-prophet:
Understanding predictive intelligence with prophet arena. arXiv preprint arXiv:2510.17638, 2025b.
Cheng Ye, Zhiyuan Hu, Yuxuan Deng, Zeyu Huang, Mengdi Ma, Yifeng Zhu, and Weiyu Wang.
Mirai: Evaluating llm agents for event forecasting. arXiv preprint arXiv:2407.01231, 2024.
Haoxuan Yu, Feng Li, and Jia You. Livetradebench: Seeking real-world alpha with large language
models. arXiv preprint arXiv:2511.03628, 2025.
Ming Zhang, Yuchen Shen, Jiaming Deng, Yifan Wang, Yucheng Zhang, Jian Wang, Shilong Liu,
Shuzhi Dou, Hong Sha, Qian Peng, et al. LLMEval-Fair: A large-scale longitudinal study on
robust and fair evaluation of large language models. arXiv preprint arXiv:2508.05452, 2025.
11
