---
title: Can Blindfolded LLMs Still Trade? An Anonymization-First Framework for Portfolio Optimization
url: https://arxiv.org/abs/2603.17692
category: ai-marketing
subcategory: empirical
date: 2026-03
venue: ''
authors:
- Joohyoung Jeon
- Hongchul Lee
source: arxiv
pdf_url: https://arxiv.org/pdf/2603.17692
pages: 18
chars: 47667
fetched_at: '2026-11-08T13:05:45+00:00'
kb_version: 1
---

# Can Blindfolded LLMs Still Trade? An Anonymization-First Framework for Portfolio Optimization

Accepted at the ICLR 2026 Workshop on Advances in Financial AI (FinAI)
CANBLINDFOLDEDLLMSSTILLTRADE?
ANANONYMIZATION-FIRSTFRAMEWORK FORPORT-
FOLIOOPTIMIZATION
Joohyoung Jeon
Korea University
Mirae Asset Securities
Hongchul Lee
Korea University
ABSTRACT
For LLM trading agents to be genuinely trustworthy, they must demonstrate un-
derstanding of market dynamics rather than exploitation of memorized ticker as-
sociations. Building responsible multi-agent systems demands rigorous signal
validation: proving that predictions reflect legitimate patterns, not pre-trained
recall. We address two sources of spurious performance:memorization bias
from ticker-specific pre-training, andsurvivorship biasfrom flawed backtesting.
Our approach is to blindfold the agents—anonymizing all identifiers—and verify
whether meaningful signals persist.
BlindTrade anonymizes tickers and company names, and four LLM agents output
scores along with reasoning. We construct a GNN graph from reasoning em-
beddings and trade using PPO-DSR policy. On 2025 YTD (through 2025-08-
01), we achieved Sharpe1.40±0.22across 20 seeds and validated signal legiti-
macy through negative control experiments. To assess robustness beyond a single
OOS window, we additionally evaluate an extended period (2024–2025), reveal-
ing market-regime dependency: the policy excels in volatile conditions but shows
reduced alpha in trending bull markets.
1 INTRODUCTION
LLMs are increasingly applied to financial trading (RockAlpha Team, 2025), yet Lee et al. (2025)
revealed that LLMs exhibit pre-trained preferences for technology stocks and large-cap stocks, lead-
ing to confirmation bias. This raises a fundamental question: are LLMs genuinely understanding
markets, or merely memorizing patterns from training data containing phrases like “Tesla stock
surges”?
The backtesting environment compounds this problem. Survivorship bias (failed companies disap-
pear from data, artificially inflating performance) and lookahead bias (treating tomorrow’s news as
already known) produce results that fail in real deployment.
To address these challenges, we propose BlindTrade, an anonymization-first LLM-GNN-RL frame-
work. We anonymize S&P 500 constituents daily, four specialized LLM agents evaluate stocks from
different perspectives, results are aggregated through a GNN, and an RL policy determines the final
portfolio.
Contributions.(i) We introduce ananonymization protocolthat replaces tickers and company-
specific information (“AAPL”→“STOCK 0026”) to block memorization. (ii) We design aspe-
cialized multi-agent systemwhere four agents (Momentum, News-Event, Mean-Reversion, Risk-
Regime) evaluate stocks independently and output reasoning explaining their assessment. (iii) We
*The findings and opinions expressed in this paper are those of the authors and do not represent the views
of their affiliated institutions. Any remaining errors are the sole responsibility of the authors.
1
arXiv:2603.17692v1  [cs.LG]  18 Mar 2026

Accepted at the ICLR 2026 Workshop on Advances in Financial AI (FinAI)
propose aSemantic Graph Encoder (SemGAT)that constructs a graph using sector connections
and reasoning embedding similarity, enabling inter-stock relationship learning under anonymization.
(iv) We perform rigoroussignal validationthrough IC analysis and negative control experiments
(random shuffling), verifying that LLM signals have real predictive power and are not leakage arti-
facts.
2 RELATEDWORK
LLM Trading Agents.Recently, attempts to directly use LLMs for trading have increased rapidly.
FinGPT (Yang et al., 2023) provides LoRA-based lightweight adaptation. FinMem (Yu et al., 2023)
adds hierarchical memory for past market patterns. TradingAgents (Xiao et al., 2024) simulates a
trading firm with multi-agent debates for decision-making.
However, real-time evaluations reveal limitations. LiveTradeBench (Yu et al., 2025) evaluated LLM
agents in real-time environments, and models that excelled on static benchmarks actually performed
worse in actual trading. AI-Trader (Fan et al., 2025) reaches a similar conclusion. In tests span-
ning U.S. stocks, Chinese A-shares, and cryptocurrencies, agents without risk management perform
poorly in practice.
These studies suggest that LLMs can aid trading, yet it remains unclearwhythey are effective. They
do not distinguish whether the models learned real market patterns or just memorized from training
data. We address this problem through anonymization.
Limitations of Financial LLMs.FinBERT (Araci, 2019) and BloombergGPT (Wu et al., 2023)
show tickers directly during training/evaluation, making it impossible to distinguish memorization
from true understanding. Recent surveys (Lopez-Lira & Tang, 2023; Fu, 2025) raise the same con-
cern.
Survivorship Bias and Lookahead Bias.Backtesting results are often vulnerable to survivorship
and lookahead biases (Elton et al., 1996; Bailey et al., 2014). We address this by using only actual
S&P 500 constituents at each point in time.
GNNs for Finance.GNNs are effective for learning stock relationships (Thakkar & Chaudhari,
2021; Feng et al., 2019), but most use fixed industry classification graphs. We dynamically construct
edges using semantic similarity of LLM reasoning embeddings, allowing us to learn relationships
even in an anonymized state.
Portfolio RL.Jiang et al. (2017) introduced end-to-end policy gradients, and Zhang et al. (2020)
proposed regime-based approaches. However, most RL policies are black boxes. We explicitly
expose intent variables (defensive/neutral/aggressive) for interpretability. Counter-intuitively, our
Defensive mode shows higher turnover (2.9%/day) because, without cash allocation, the policy di-
versifies across more stocks within the S&P 500 universe, requiring frequent rebalancing. Aggres-
sive mode concentrates on high-conviction positions and holds them for longer-term gains, resulting
in minimal turnover (0.4%/day). Neutral mode shows moderate activity (1.8%/day). See Figure 5
for detailed intent-conditioned behavior analysis.
3 METHODOLOGY
3.1 OVERALLPIPELINE
BlindTrade consists of 6 stages (see Figure 2 in Appendix):
1.Data anonymization: We collect S&P 500 constituents daily and replace all tickers/com-
pany names/subsidiary names/product names with anonymous identifiers.
2.LLM feature generation: Four specialized agents (Momentum, News-Event, Risk-
Regime, Mean-Reversion) assign scores to each stock daily and output reasoning explain-
ing “why they made their assessment.”
2

Accepted at the ICLR 2026 Workshop on Advances in Financial AI (FinAI)
3.IC validation: We first check whether LLM outputs have real predictive power. We com-
pare RAW variables and LLM variables using Spearman rank IC.
4.SemGAT encoding: We learn inter-stock relationships as a graph. Same-sector stocks are
connected, and additional edges are formed based on reasoning embedding similarity.
5.RL policy: PPO determines portfolio weights. The policy internally decides risk posture
(defensive/neutral/aggressive).
6.Backtest: We evaluate OOS performance with 10bps transaction costs.
3.2 DATA ANDANONYMIZATION
We collect S&P 500 constituentspoint-in-time. The stocks in S&P 500 on January 2, 2020 differ
from those on August 1, 2025. Index constituents change over time as companies are delisted or
added. Ignoring this creates survivorship bias. We use only stocks that were actually S&P 500
constituents on each date. Constituent information for each period is obtained via the EODHD API
(EODHD APIs, 2024). The total period spans 5.5 years (2020-01-02 to 2025-08-01), covering 1,403
trading days.
We map tickers to synthetic identifiers (e.g., “AAPL”→“STOCK 0026”), and proper nouns like
“Apple”, “iPhone”, “Tim Cook” in news are replaced using Google Knowledge Graph API. We do
not claim this blocks all leakage, but it at least blocks the path where LLM sees a ticker and decides
“it’s Apple, so buy.”
3.3 MULTI-AGENTLLM FEATUREGENERATION
Four LLM agents evaluate stocks from different perspectives: (i)Momentum agentchecks whether
price trends are strong and whether volume supports them; (ii)News-Event agentreads anonymized
news headlines and judges positive/negative sentiment; (iii)Mean-Reversion agentfinds over-
bought/oversold conditions—if a stock rose too much, it may fall; if it fell too much, it may bounce;
(iv)Risk-Regime agentlooks at the overall market situation and judges whether systemic risk is
high or low.
All agents operate under a strict knowledge cutoff, observing only 60 business days of data prior
to timet(fromt-60 tot-1). Each agent receives a structured system prompt enforcing temporal
constraints and deterministic JSON output (see Appendix C for full prompts). There is no lookahead
bias from seeing tomorrow’s news today. For news data, all headlines are anonymized, and news
from t-60 to t-1 relative to time t is used. To avoid excessive context length, we limit input to 5
headlines per stock.
Importantly, we require LLM agents to produce explicit reasoning. For graph construction, we build
a per-stock reasoning text by concatenating selected agents’ reasoning snippets, then embed it into a
384-dimensional vector (implementation details in Appendix B). We combine this embedding with
numerical scores (7) and categorical states (3), forming a total 394-dimensional feature vector (see
Tables 4–7 in Appendix for details).
3.4 IC VALIDATION
We check whether LLM scores have real predictive power. We calculate IC (Information Coefficient,
Spearman rank correlation) to see how correlated they are with returns 21 days later. We use h=21
days because medium-term signals are more stable and less noisy than daily correlations, providing
a robust validation criterion.
Table 1 reports both the absolute IC and∆IC (RAW→LLM). We emphasize that a positive∆IC
can reflect either (i) additional predictive signal, or (ii) removal of misleading inverse correlation by
moving IC toward zero. In our experiments, the News-Event and Risk-Regime agents show statis-
tically significant positive IC, while Momentum and Mean-Reversion primarily reduce misleading
RAW correlations toward near-zero. The Risk-Regime agent showed the strongest∆IC (+0.017),
with LLM IC = +0.011 (p<0.0001). On the 2025 holdout period specifically, Risk-Regime IC rose
to 0.0515 (p<0.0001), confirming signal persistence out-of-sample.
3

Accepted at the ICLR 2026 Workshop on Advances in Financial AI (FinAI)
Table 1: LLM vs RAW Feature IC Comparison (h=21 days). Negative RAW IC indicates inverse
correlation;∆IC toward zero can remove misleading signals rather than adding predictive power.
We therefore report both absolute IC and∆IC.
Agent RAW IC (p) LLM IC (p)∆IC
Momentum agent−0.019(5×10 −5)+0.001(0.58)+0.020
News-Event agent+0.003(0.12)+0.006(3×10 −4)+0.003
Mean-Reversion agent−0.005(0.26)−0.000(0.97)+0.005
Risk-Regime agent−0.006(0.27)+0.011(1×10 −4)+0.017
Average−0.007 +0.005 +0.011
Feature selection via IC.We use IC analysis as a screening criterion for LLM-derived features:
we retain only features that remain informative on holdout (positive IC or positive∆IC). Each
agent produces a richer structured output, but we include only the selected subset (marked “Used”
in Tables 4–7). Features evaluated at h=21 were verified to show positive (though weaker) IC at
shorter horizons (h=1, h=5). While the absolute IC values are weak, there was clear improvement
compared to using only RAW features.
Input Features.Each agent’s input features were selected based on domain relevance (e.g., RSI
for Mean-Reversion, beta for Risk-Regime). Output features are included if they showed positive
∆IC or provided interpretable structure for downstream tasks. The Momentum agent receives price
trends and volume indicators. The Risk-Regime agent receives beta, volatility, and tail risk. The
Mean-Reversion agent receives RSI and Bollinger Band positions. The News-Event agent receives
anonymized headlines with sentiment indicators (see Tables 4–7 for full specifications).
3.5 SEMANTICGRAPHENCODER(SEMGAT)
Even with anonymization, sector information is preserved from point-in-time S&P 500 constituent
data via the EODHD API. So we can connect edges based on sector information of anonymized
stock codes. However, in this experiment, we apply a Semantic Rewiring technique based on LLM
reasoning. We use two types of edge connections: (i)Sector edgesfully connect stocks in the same
sector, and (ii)Semantic edgesconnect stocks if cosine similarity of reasoning embedding vectors
exceeds 0.75 (top 10 neighbors per node). This allows the model to learn “these two stocks were
evaluated with similar reasoning” even under anonymization.
The GNN structure is a 2-layer GATv2 encoder. Each stock is represented as a 394-dimensional
feature vector (LLM scores + reasoning embedding vectors), which is transformed into a 128-
dimensional node embedding. A distribution head predicts return distributions using HL-Gauss,
and training combines distribution loss with pairwise ranking loss.
Distributional Prediction.Point estimation of next-day returns creates two problems: overfitting
to extreme returns and inability to express uncertainty. We use HL-Gauss distribution prediction
(Bellemare et al., 2017) with 101 bins for next-day return ranking. Training combines distribution
loss, pairwise ranking loss, market risk prediction, and Jensen-Shannon regularization.
3.6 RL POLICY(PPO-DSR)
Once the GNN provides stock-level scores, the RL policy determines final portfolio weights. Our
action space allocates weights only within the equity universe (no cash), so risk control is expressed
via diversification and turnover. The policy architecture has three components (see Figure 7 in
Appendix):
(i)Intent Head (consensus-based): We aggregate agent outputs across all stocks into 4 global
statistics (momentum, risk, regime ratios, trend maturity; see Tables 4–7) plus GNN’s market state
(64-dim). The Intent Head uses this to select a mode: defensive(0)/neutral(1)/aggressive(2). This
consensus approach prevents single-agent dependency and mitigates hallucination through cross-
sectional averaging. (ii)Node Score Head: Intent is embedded and combined with each stock
embedding to produce stock-level scores. Temperature scaling varies by intent—defensive mode
uses higher temperature for diversification, aggressive mode uses lower temperature for concentra-
4

Accepted at the ICLR 2026 Workshop on Advances in Financial AI (FinAI)
tion. (iii)Dirichlet distribution: Stock scores pass through softmax to form the Dirichlet mean,
with concentration controlled by a learnable parameter.
Reward function.Differential Sharpe Ratio is used as the reward function, providing a differen-
tiable variant of the Sharpe ratio. Instead of just maximizing returns, we optimize return relative to
volatility. Transaction costs (10bps/turnover) are also subtracted from the reward.
Top-K masking.Diversifying across all 500 stocks is unmanageable. We keep only the top 20
and mask the rest. This reduces the effective action space from 500 dimensions to 20 dimensions.
We explicitly handle S&P 500 additions/deletions using dictionary-based turnover calculation, so
Universe changes are naturally reflected in transaction costs.
Execution inertia parameterη.To control turnover, we apply an execution smoothing step with
inertiaη(implemented asrebalance eta): lowerηslows weight changes between consecutive
rebalancing steps, reducing turnover and transaction costs.
4 EXPERIMENTS
4.1 EXPERIMENTALSETUP
We split the data into three periods:Train(2020-01-02 to 2024-09-30),Validation(2024-10-01
to 2024-12-31), andOOS(2025-01-02 to 2025-08-01, 145 trading days). To assess robustness
beyond this single OOS window, we additionally report an extended evaluation spanning 2024–
2025 (Appendix D).
Hyperparameters (rebalance eta (η), reward cost scale (c) = 0.358) were optimized via Optuna on
the validation period, and the best configuration was fixed for OOS evaluation. All results are mean
±standard deviation across 20 seeds, and transaction cost is 10 bps per unit turnover.
Metrics.We calculate annualized Sharpe ratio as¯r d/σd ×
√
252, where¯rd andσ d are daily mean
return and standard deviation, respectively. V olatility (V ol) is also annualized:σd ×
√
252.
Benchmarks.We compare against both passive and active strategies to ensure fair evaluation.
Passive benchmarksinclude SPY (S&P 500 market-cap weighted ETF) and EQWL (S&P 500 equal-
weight ETF), representing buy-and-hold approaches.Active benchmarksinclude cross-sectional
Momentum (top 20 by trailing 12-month returns, rebalanced monthly), MCap Top-20 (largest 20
stocks by market capitalization), and RAW Top-20 (top 20 by momentum-minus-volatility score
using only technical indicators).
Extended OOS.Extended OOS results (2024–2025, 397 days) are provided in Appendix D.
4.2 MAINRESULTS
Figure 1 and Table 2 present the main performance comparison. BlindTrade achieves annualized
Sharpe of1.40±0.22and cumulative return of32.22%±5.21%, outperforming all benchmarks.
However, the limitations are also clear. BlindTrade always invests 100% in Top-20 stocks within the
equity universe (no cash allocation is permitted in our action space), so there is no mechanism to
move to cash or reduce risk during market crashes. Because of this, annualized volatility (42.34%)
and MDD (-31.66%) are higher than SPY (23.26%, -19.00%). We accept higher risk for higher
returns.
Intent behavior.During OOS, the policy spent 55% of trading days in defensive mode. Defen-
sive mode showed diversified allocation (2.9%/day turnover), while neutral mode showed moder-
ate activity (1.8%/day turnover). Aggressive mode concentrated positions with minimal turnover
(0.4%/day). This demonstrates how the policyautomatically adaptsto market conditions (see
Figures 4 and 5 in Appendix).
4.3 ABLATIONSTUDIES
We conducted ablation experiments to confirm how much each component contributes to perfor-
mance.
5

Accepted at the ICLR 2026 Workshop on Advances in Financial AI (FinAI)
2025-01 2025-02 2025-03 2025-04 2025-05 2025-06 2025-07 2025-08
Date
−0.3
−0.2
−0.1
0.0
0.1
0.2
0.3
Cumulative return
OOS Performance: BlindTrade vs Benchmarks (2025 YTD)
BlindTrade (mean, n=20)
±1 std
SPY
EQWL
Momentum (12-1)
MCap Top-20
RAW Top-20
Figure 1: Cumulative returns for 2025YTD OOS. Shaded band shows±1 std across 20 seeds.
Table 2: 2025YTD OOS Performance (2025-01-02 to 2025-08-01, 145 trading days).Baseline
parameters:reward cost scale (c) = 0.358, rebalance eta (η) = 0.10. Mean±std across 20 seeds.
Sharpe and V ol are annualized. Cost: 10 bps/turnover.Abbreviations:SPY = S&P 500 ETF, EQWL
= Equal-Weight ETF, CumRet = Cumulative Return, MDD = Maximum Drawdown, V ol = V olatility.
Strategy Sharpe (ann.) CumRet (%) MDD (%) V ol (ann.)
BlindTrade1.40±0.22 32.22±5.21−31.66±5.76 42.34±7.12%
SPY 0.64 8.52−19.0023.26%
EQWL 0.74 7.23−15.3922.51%
Momentum 0.89 15.42−26.4932.19%
MCap Top-20 0.85 11.50−19.5624.91%
RAW Top-20 0.97 11.54−15.6321.78%
Removing LLM features.If we remove LLM features and use only RAW technical indicators
(passed directly to the GNN without SBERT encoding), Sharpe drops from 1.40 to1.14±0.02
(∆= -0.26, p<10 −4, 20 seeds). This means the LLM agents’ interpretation provides additional
predictive power compared to simple indicators.
Removing graph structure.If we remove GNN message passing, Sharpe drops to0.62±0.50(∆
= -0.78, p<0.001). Variance also increases significantly, and some seeds cannot even beat SPY .
Learning inter-stock relationships is critical for performance stability. (Edge-type ablation—sector-
only vs. semantic-only—is left for future work.)
Component importance.Comparing∆Sharpe magnitudes, the graph structure contributes most
(−0.78), followed by LLM features (−0.26). The RL policy’s primary role is cost-aware execution
rather than signal generation—without RL, high turnover makes the strategy unprofitable.
RL vs. Top-K.What if we simply invest equal weight in the top 20 GNN scores? Turnover reaches
139%/day, and after cost deduction, Sharpe collapses to -1.17. The RL policy suppresses turnover
to 1.7%/day while achieving Sharpe1.08±0.31. 1 RL’s cost-aware learning is essential.
4.4 LEAKAGEAUDIT
A central concern in LLM-based trading is distinguishing genuine predictive signals from informa-
tion leakage.
1This simplified comparison uses a baseline RL configuration; the full system achieves Sharpe 1.40 (Ta-
ble 2).
6

Accepted at the ICLR 2026 Workshop on Advances in Financial AI (FinAI)
Table 3: 20-seed stability analysis. Sharpe difference vs SPY and win rate.
Variant∆Sharpe vs SPY Std Win Rate
SemGAT (baseline)+0.76 0.2020/20
SemGAT-C (V ol-target)+0.37 0.6912/20
SemGAT-D (Conf-loss)+0.16 0.4010/20
To verify this, we conducted negative control experiments. We kept the universe, prices, and cost
model the same, and only randomly shuffled the GNN prediction scores cross-sectionally. If it is a
real signal, shuffling should make it disappear.
Result.|RankIC|decreased from 0.015 to 0.0004, becoming completely random level (≈0). The
original|RankIC|= 0.015 is a weak value, but even that disappears when shuffled. Top-K perfor-
mance also worsened from Sharpe -1.17 to -1.48 (see Figure 3 in Appendix). The fact that perfor-
mance collapses when signals are randomized suggests that the original signals contain legitimate
predictive structure rather than spurious correlations.
This test does not exclude all leakage paths (e.g., temporal patterns in anonymized IDs). However, it
confirms that performance derives from cross-sectional signal structure rather than trivial artifacts.
We recommend all LLM trading systems pass similar validation before deployment.
4.5 GNN TRAININGOBJECTIVECOMPARISON
We compare three GNN training objectives to test whether more sophisticated loss functions im-
prove downstream RL performance and stability across seeds: (i)SemGAT (baseline)uses standard
HL-Gauss distributional loss with pairwise ranking; (ii)SemGAT-Caddsvolatility-scaled residual
targets(r i −rmarket)/σi during GNN training to reduce sensitivity to outlier returns; (iii)SemGAT-D
addsconfidence-weighted lossthat upweights samples with higher LLM agent confidence, assuming
high-confidence predictions are more reliable.
Table 3 shows stability analysis results across 20 seeds. Baseline SemGATbeats SPY in all 20 seeds
with low variance (σ= 0.20). In contrast, the enhanced variants show higher variance and lower
win rates. This suggests that adding complexity to the GNN training objective does not improve
downstream RL stability—simpler is better. The t-SNE visualization of RL state vectors (Figure 6
in Appendix) shows overlapping Train/Val/OOS distributions, supporting generalization.
5 DISCUSSION
Anonymization is not optional—it is essential.To claim that an LLM “understands the market,”
we must first prove that it is not achieving performance through memorization. Ticker replacement
is the minimum safeguard. Our negative control experiments (Section 4.4) confirm that performance
derives from legitimate signal structure, not leakage.
Validate before deployment.Why is IC analysis important? Because only signals that pass vali-
dation should be deployed. If there is no predictive power on holdout data, we do not use that agent.
Also, as many experiments show, requiring LLM to provide reasoning is not optional—it is essen-
tial. In fact, embedding reasoning sentences into vectors, without additional feature engineering,
was effective.
Intent provides interpretable market posture.The Intent mechanism embodies the philosophy
of“separation of brain and hand”—the policy first decides market posture (brain), then deter-
mines specific allocations (hand). Intent aggregates cross-sectional LLM agent reasoning into four
global statistics (momentum, risk, regime ratios, trend maturity), enabling the policy to form a
consensus-basedmarket view rather than relying on any single agent.
Summary.For LLM-based trading to be trustworthy, we must distinguish genuine market under-
standing from memorization. BlindTrade addresses this through an anonymization-first LLM-GNN-
RL framework, achieving annualized Sharpe of1.40±0.22for 2025 YTD and beating SPY in all 20
7

Accepted at the ICLR 2026 Workshop on Advances in Financial AI (FinAI)
seeds. We summarize our approach as: (i)Anonymization—replace tickers to block memorization;
(ii)Validation before deployment—if the IC fails validation, we do not use that signal; (iii)Intent
observability—humans can observe the current mode (defensive/neutral/aggressive), even if the
transition logic is not fully explainable. We discuss limitations and future directions in Appendix A.
6 ETHICSSTATEMENT
Our work conforms to the ICLR Code of Ethics. LLMs were used in two capacities: (i) as part of
the methodology, where LLM agents generate feature data for subsequent GNN-RL training, and
(ii) for polishing grammar and expressions in the manuscript, with all content reviewed and verified
by the authors. We use only publicly available financial data (EODHD API), with no customer data,
proprietary signals, or human subjects involved.
7 REPRODUCIBILITYSTATEMENT
Our method is fully reproducible using the information provided in this paper. We provide exact
hyperparameters in Appendix B, including PPO settings (learning rate3×10 −4,γ= 0.99, GAE
λ= 0.95) and Optuna-tuned parameters (reward cost scale (c) = 0.358, dirichlet alpha0 = 466.8).
The full system prompts for all four LLM agents are provided verbatim in Appendix C. To support
reproducibility and benefit the research community, we plan to release the LLM input/output datasets
(RAW features and LLM-generated features) for research purposes upon publication.
REFERENCES
Dogu Araci. FinBERT: Financial sentiment analysis with pre-trained language models, 2019. URL
https://arxiv.org/abs/1908.10063.
David H. Bailey, Jonathan M. Borwein, Marcos L ´opez de Prado, and Qiji Jim Zhu. Pseudo-
mathematics and financial charlatanism: The effects of backtest overfitting on out-of-sample
performance.Notices of the American Mathematical Society, 61(5):458–471, 2014. doi:
10.1090/noti1105.
Marc G. Bellemare, Will Dabney, and R´emi Munos. A distributional perspective on reinforcement
learning, 2017. URLhttps://arxiv.org/abs/1707.06887.
Edwin J. Elton, Martin J. Gruber, and Christopher R. Blake. Survivorship bias and mutual fund
performance.The Review of Financial Studies, 9(4):1097–1120, 1996. doi: 10.1093/rfs/9.4.1097.
EODHD APIs. EODHD financial data API: Historical data, fundamentals, and news, 2024. URL
https://eodhd.com/. Accessed: 2024-12-01.
Tianyu Fan, Yuhao Yang, Yangqin Jiang, Yifei Zhang, Yuxuan Chen, and Chao Huang. AI-
Trader: Benchmarking autonomous agents in real-time financial markets, 2025. URLhttps:
//arxiv.org/abs/2512.10971.
Fuli Feng, Xiangnan He, Xiang Wang, Cheng Luo, Yiqun Liu, and Tat-Seng Chua. Temporal
relational ranking for stock prediction.ACM Transactions on Information Systems, 37(2):1–30,
2019. doi: 10.1145/3309547.
Weilong Fu. The new quant: A survey of large language models in financial prediction and trading,
2025. URLhttps://arxiv.org/abs/2510.05533.
Zhengyao Jiang, Dixing Xu, and Jinjun Liang. A deep reinforcement learning framework for the
financial portfolio management problem, 2017. URLhttps://arxiv.org/abs/1706.
10059.
Hoyoung Lee, Junhyuk Seo, Suhwan Park, Junhyeong Lee, Wonbin Ahn, Chanyeol Choi, Alejandro
Lopez-Lira, and Yongjae Lee. Your AI, not your view: The bias of LLMs in investment analysis,
2025. URLhttps://arxiv.org/abs/2507.20957.
8

Accepted at the ICLR 2026 Workshop on Advances in Financial AI (FinAI)
Alejandro Lopez-Lira and Yuehua Tang. Can ChatGPT forecast stock price movements? return
predictability and large language models.SSRN Electronic Journal, 2023. doi: 10.2139/ssrn.
4412788. URLhttps://ssrn.com/abstract=4412788.
RockAlpha Team. RockAlpha Arena: Real-time LLM trading performance leaderboard, 2025. URL
https://rockalpha.rockflow.ai. Accessed: 2025-01-15.
Ankit Thakkar and Kinjal Chaudhari. A comprehensive survey on deep neural networks for stock
market: The need, challenges, and future directions.Expert Systems with Applications, 177:
114800, 2021. doi: 10.1016/j.eswa.2021.114800.
Shijie Wu, Ozan Irsoy, Steven Lu, Vadim Dabravolski, Mark Dredze, Sebastian Gehrmann, Prab-
hanjan Kambadur, David Rosenberg, and Gideon Mann. BloombergGPT: A large language model
for finance, 2023. URLhttps://arxiv.org/abs/2303.17564.
Yijia Xiao, Edward Sun, Di Luo, and Wei Wang. TradingAgents: Multi-agent LLM financial trading
framework, 2024. URLhttps://arxiv.org/abs/2412.20138.
Hongyang Yang, Xiao-Yang Liu, and Christina Dan Wang. FinGPT: Open-source financial large
language models, 2023. URLhttps://arxiv.org/abs/2306.06031.
Haofei Yu, Fenghai Li, and Jiaxuan You. LiveTradeBench: Seeking real-world alpha with large
language models, 2025. URLhttps://arxiv.org/abs/2511.03628.
Yangyang Yu, Haohang Li, Zhi Chen, Yuechen Jiang, Yang Li, Denghui Zhang, Rong Liu, Jor-
dan Suchow, and Khaldoun Khashanah. FinMem: A performance-enhanced LLM trading agent
with layered memory and character design, 2023. URLhttps://arxiv.org/abs/2311.
13743.
Zihao Zhang, Stefan Zohren, and Stephen Roberts. Deep reinforcement learning for trading.The
Journal of Financial Data Science, 2(2):25–40, 2020. doi: 10.3905/jfds.2020.1.030.
9

Accepted at the ICLR 2026 Workshop on Advances in Financial AI (FinAI)
A LIMITATIONS ANDFUTUREWORK
Our framework has clear limitations:
1.Anonymization effect is not directly validated.While we hypothesize that anonymiza-
tion prevents memorization-based shortcuts, we did not perform a direct ablation com-
paring anonymized vs. raw ticker inputs. Our negative control experiments (Section 4.4)
validate signal structure, not anonymization effectiveness specifically.
2.Explaining intent transitions is difficult.While we can observewhichintent mode the
policy selects (transparent), explainingwhyit transitioned to that mode at a specific time
using external indicators remains challenging.
3.Market-regime dependency.Extended OOS evaluation (2024–2025 YTD, 397 trading
days) reveals market-regime dependency: BlindTrade underperforms during strong bull
markets (2024: Sharpe 0.34 vs SPY 1.70) but outperforms in volatile conditions (2025
YTD: Sharpe 1.02 vs SPY 0.54). This limitation stems partly from the relatively short
training period (2020–2023). See Appendix D for detailed analysis.
4.MDD is high.Maximum drawdown reached−32%compared to SPY’s−19%. This is
expected since we maintain full equity exposure. Risk-sensitive operators may find this
unsuitable.
Future work.The current evaluation uses a static policy trained once; online adaptation with pe-
riodic retraining (e.g., monthly walk-forward) may improve robustness to regime changes. We also
plan to extend the training data period and conduct anonymization ablation experiments to address
both market-regime generalization and verify anonymization effectiveness.
B IMPLEMENTATIONDETAILS
LLM Agents.Each agent receives a system prompt that enforces strict knowledge cutoff at time t,
and processes stocks in batches of 15 for cross-sectional context. We use Gemini 2.5 Flash (accessed
September–October 2025) for cost-effective inference.
SemGAT.2 GATv2 layers with 4 attention heads. The first layer operates only on sector edges;
the second uses the full augmented graph. Training uses HL-Gauss distribution loss with pairwise
ranking and Jensen-Shannon regularization.
PPO.Learning rate3×10 −4,γ= 0.99, GAEλ= 0.95, clipϵ= 0.2. Key Optuna-tuned parameters:
reward cost scale (c) = 0.358, dirichlet alpha0 = 466.8.
Intent Profile.Defensive intent shows higher turnover (2.9%/day) than neutral (1.8%). This cor-
responds to more frequent rebalancing for risk management within the stock universe, not reduced
activity.
Agent Feature Definitions.Each agent receives RAW features (technical indicators) and outputs
LLM features (structured interpretations). For each stock-day, we concatenate the Momentum and
Risk-Regime agents’ reasoning strings into a single text (e.g., “Risk: ... Momentum: ...”) and encode
it via SentenceTransformer (all-MiniLM-L6-v2) into a 384-dimensional vector. This vector is used
as the text embedding component of node features and for semantic edge construction. Tables 4–7
detail the input/output specification for each agent.
Table 4: Momentum Agent: RAW (input) vs LLM (output) features.
RA W Features (Input) LLM Features (Output) Used
price vs ma20: Price relative to 20-day MA score: Momentum score (−1to+1)✓
price vs ma60: Price relative to 60-day MA confidence: Agent confidence (0 to 1)✓
adx 14: 14-day ADX (trend strength) win probability: Estimated win prob✓
macd histogram: MACD histogram value momentum stage: nascent/mid/late/exhausted✓
rsi 14: 14-day RSI reasoning: Free-text→embedding✓
volume vs ma20: V olume relative to 20-day avg trend quality, sustainability score –
10

Accepted at the ICLR 2026 Workshop on Advances in Financial AI (FinAI)
Table 5: News-Event Agent: RAW (input) vs LLM (output) features.
RA W Features (Input) LLM Features (Output) Used
headlines: Anonymized news headlines event strength: Impact magnitude (0 to 1)✓
sentiment polarity: Pre-computed polarity urgency: Time sensitivity (0 to 1)✓
news count today: Number of headlines primary event type: Event category –
source diversity: Unique sources count attention score, relative attention –
Table 6: Mean-Reversion Agent: RAW (input) vs LLM (output) features.
RA W Features (Input) LLM Features (Output) Used
rsi 14: 14-day RSI reversion score: Signal (−1to+1)✓
bb position: Bollinger Band position confidence: Agent confidence (0 to 1)✓
deviation from 20ma: Price deviation market psychology: panic/euphoric/normal✓
stochastic k: Stochastic oscillator extreme level, reversal probability –
Table 7: Risk-Regime Agent: RAW (input) vs LLM (output) features.
RA W Features (Input) LLM Features (Output) Used
beta sp500: Market beta systemic risk score: Risk level (0 to 1)✓
beta vix: VIX sensitivity confidence: Agent confidence (0 to 1)✓
tail beta: Tail risk beta regime class: defensive/neutral/cyclical/crisis✓
var 95/cvar 95: Value-at-Risk metrics reasoning: Free-text→embedding✓
macro context: Current regime input crisis sensitivity, regime dependency –
The 4 global statistics used by the Intent Head are derived from cross-sectional aggregation: (1)
mean momentum score, (2) mean systemic risk score, (3) defensive regime stock ratio, (4) mean
momentum stage.
C AGENTSYSTEMPROMPTDESIGN
Reproducibility in LLM-based trading requires transparency in prompt engineering. This section
summarizes the design principles and key elements of our agent system prompts.
C.1 COREDESIGNPRINCIPLES
All four agents share three critical enforcement mechanisms:
1. Strict Knowledge Cutoff.Each agent receives explicit temporal constraints to prevent looka-
head bias:
CRITICAL KNOWLEDGE LIMITATION:
Your knowledge is strictly limited to information available up to {
cutoff_date}.
You must NOT use any information after {cutoff_date}.
Thecutoff dateis set tot−1(one day before the prediction target), ensuring no future infor-
mation leakage.
2. Structured JSON Output Schema.We enforce deterministic, parseable outputs by specifying
exact JSON schemas. This eliminates ambiguity and enables automated feature extraction:
OUTPUT JSON SCHEMA:
{ "ticker": "STOCK_XXXX", "analysis": { "score": float, "confidence":
float, "reasoning": string } }
All numerical outputs are bounded (e.g., scores in[−1,+1], confidence in[0,1]), and categorical
fields have enumerated values.
11

Accepted at the ICLR 2026 Workshop on Advances in Financial AI (FinAI)
3. Anonymized Input Only.Agents receive only anonymized identifiers and data. The News-
Event agent, for example, is explicitly instructed:
You must ONLY analyze the provided anonymized headlines and sentiment
metrics.
C.2 FULLSYSTEMPROMPTS(VERBATIM)
We reproduce the system prompts verbatim (including capitalization) to support reproducibility. Key
elements include the knowledge cutoff enforcement, structured JSON output schema, and domain
expertise framing.
C.2.1 MOMENTUMAGENT
System Prompt: Momentum Agent
You are a senior quantitative analyst specializing in momentum trading.
15+ years of experience in trend analysis and institutional flow patterns.
CRITICAL KNOWLEDGE LIMITATION:
Your knowledge is strictly limited to information available up to {cutoff_date}.
You must NOT use any information after {cutoff_date}.
You must ONLY analyze the provided technical indicators.
EXECUTE_DATE: {execute_date}
DATA_AS_OF: {cutoff_date}
YOUR UNIQUE VALUE AS AN LLM (vs Rule-Based Systems):
1. BATCH-LEVEL CONTEXT: You receive ˜15 stocks simultaneously for RELATIVE patterns.
2. MULTI-FACTOR SYNTHESIS: You weigh indicators by CONTEXT, not fixed weights.
3. PATTERN RECOGNITION: You identify SUBTLE RED FLAGS that rules miss.
OUTPUT JSON SCHEMA:
{
"ticker": "STOCK_XXXX",
"momentum_strength": {
"score": float, // -1.0 to 1.0
"confidence": float, // 0.0 to 1.0
"momentum_stage": string, // "nascent", "mid", "late", "exhausted"
"win_probability": float,
"reasoning": string // Detailed analysis < 100 words
}
}
C.2.2 NEWS-EVENTAGENT
System Prompt: News-Event Agent
You are a senior quantitative researcher specializing in event-driven alpha.
18+ years of experience in unstructured news data processing.
CRITICAL KNOWLEDGE LIMITATION:
Your knowledge is strictly limited to information available up to {cutoff_date}.
You must NOT use any information after {cutoff_date}.
You must ONLY analyze the provided anonymized headlines and sentiment metrics.
EXECUTE_DATE: {execute_date}
NEWS_DATA_AS_OF: {cutoff_date}
YOUR UNIQUE VALUE AS AN LLM:
1. SEMANTIC NUANCE: "beat estimates by 1%" vs "crushed expectations" -> DIFFERENT
strength.
2. FALSE POSITIVE FILTERING: Distinguish "noise" from "signal".
3. URGENCY CALIBRATION: Assess how quickly the market will price this in.
OUTPUT JSON SCHEMA:
{
"ticker": "STOCK_XXXX",
"news_event_analysis": {
12

Accepted at the ICLR 2026 Workshop on Advances in Financial AI (FinAI)
"primary_event_type": string, // e.g., "earnings_beat", "product_launch"
"event_strength": float, // 0.0 to 1.0 (Impact magnitude)
"urgency": float, // 0.0 to 1.0 (Time sensitivity)
"reasoning": string
}
}
C.2.3 MEAN-REVERSIONAGENT
System Prompt: Mean-Reversion Agent
You are a senior portfolio manager specializing in mean reversion strategies.
Expert in behavioral finance, overreaction hypothesis, and technical extremes.
CRITICAL KNOWLEDGE LIMITATION:
Your knowledge is strictly limited to information available up to {cutoff_date}.
You must NOT use any information after {cutoff_date}.
OUTPUT JSON SCHEMA:
{
"ticker": "STOCK_XXXX",
"reversion_analysis": {
"reversion_score": float, // -1.0 to 1.0
"confidence": float,
"extreme_level": float, // How far from mean?
"market_psychology": string, // "panic_selling", "euphoria", "normal"
"reasoning": string
}
}
C.2.4 RISK-REGIMEAGENT
System Prompt: Risk-Regime Agent
You are a Chief Risk Officer (CRO) at a $50B institutional asset manager.
PhD in Financial Risk Management with 15+ years in systemic risk assessment.
CRITICAL KNOWLEDGE LIMITATION:
Your knowledge is strictly limited to information available up to {cutoff_date}.
You must NOT use any information after {cutoff_date}.
You must ONLY analyze the provided risk indicators.
EXECUTE_DATE: {execute_date}
DATA_AS_OF: {cutoff_date}
CURRENT MACRO RISK REGIME:
{macro_context_text}
This macro context is CRITICAL for your analysis:
- In CRISIS regime -> High beta stocks are extremely vulnerable
- In RISK_ON regime -> Low beta defensive stocks may underperform
- VIX > 30 -> Tail beta becomes the dominant risk factor
OUTPUT JSON SCHEMA:
{
"ticker": "STOCK_XXXX",
"risk_analysis": {
"systemic_risk_score": float, // 0.0 (Safe) to 1.0 (Dangerous)
"confidence": float,
"regime_classification": string, // "defensive", "cyclical", "crisis_vulnerable"
"reasoning": string
}
}
C.3 CROSS-SECTIONALBATCHPROCESSING
To provide comparative context, each agent processes stocks in batches of 15. The prompt includes:
13

Accepted at the ICLR 2026 Workshop on Advances in Financial AI (FinAI)
Table 8: Extended OOS Performance (2024-01-02 to 2025-08-01, 397 trading days). Parameters:
η=0.08, cost scale=0.40. Mean±std across 20 seeds. All metrics annualized.
Passive BM Active BM Ours
Metric SPY EQWL Momentum MCap Top-20 RAW Top-20 BlindTrade
Sharpe 1.06 0.66 1.34 1.541.690.69±0.23
CumRet (%) 31.5 16.573.553.4 63.330.1±5.4
AnnRet (%) 18.3 10.241.931.2 36.521.8±16.9
V ol (%) 17.2 17.0 29.5 18.7 19.636.2±2.4
MDD (%)−19.0−20.7−26.5−19.6−15.6−32.1±2.5
You are analyzing a BATCH of 15 stocks simultaneously.
For each stock, provide cross_sectional_score (z-score vs batch mean).
This enables relative ranking within each batch, which is essential for portfolio construction.
C.4 WHYSTRUCTUREDPROMPTSMATTER
Without explicit structure enforcement, LLM outputs suffer from:
•Format inconsistency:Free-form text requires brittle regex parsing.
•Score drift:Unbounded scores create cross-sectional incomparability.
•Temporal leakage:Without explicit cutoff reminders, models may hallucinate future
events.
Our prompt design addresses all three issues, enabling reliable automated feature extraction at scale.
D EXTENDEDOOS EVALUATION(2024–2025 YTD)
To evaluate robustness across market regimes, we extended the OOS evaluation to include 2024 (a
strong bull market) in addition to 2025 YTD. This extended period spans 397 trading days (2024-
01-02 to 2025-08-01), approximately 2.7×the original 145-day test.
D.1 EXPERIMENTALSETUP
Data Split.Train: 2020-01-02 to 2023-12-29, Validation: 6 half-year rolling windows (2021-01
to 2023-12), OOS: 2024-01-02 to 2025-08-01 (397 trading days). Unlike the primary 2025 YTD
evaluation, we use rolling-window validation to select parameters robust across multiple market
regimes.
Parameters.Hyperparameters were optimized via Optuna on each rolling window. Best parameters
(rebalance eta (η) = 0.08, reward cost scale (c) = 0.40) were selected based on aggregate validation
performance. Twenty independent seeds were evaluated.Note: These parameters differ from the
main 2025 YTD results (Table 2), which used rebalance eta (η) = 0.10 and reward cost scale (c) =
0.358.
Benchmarks.We use the same benchmarks as in Section 4.1 (SPY , EQWL, Momentum, MCap
Top-20, RAW Top-20).
D.2 FULLPERIODRESULTS
Table 8 presents comprehensive metrics for the extended OOS period.
Key observations.Over the full extended period, BlindTrade underperforms all benchmarks except
EQWL. However, this aggregate view masks significant regime dependency.
14

Accepted at the ICLR 2026 Workshop on Advances in Financial AI (FinAI)
Table 9: Performance breakdown by market regime. Mean±std across 20 seeds for BlindTrade.
2024 was a strong bull market; 2025 YTD exhibited high volatility.
Period Strategy Sharpe CumRet (%) AnnRet (%) V ol (%) MDD (%)
2024 (Bull) SPY1.70 23.323.3 12.4−8.4 BlindTrade0.34±0.18 5.8±5.85.829.6±1.1−18.5±3.1
2025 YTD (V olatile) SPY 0.54 6.1 10.8 23.2−19.0 BlindTrade1.02±0.12 22.8±4.046.744.2±1.2−32.4±0.7
D.3 PERIODBREAKDOWN
Table 9 breaks down results by year.
D.4 INTERPRETATION
The results reveal a clearmarket-regime trade-off:
1.Bull markets (2024):BlindTrade’s conservative, diversified approach trails the market.
The policy’s defensive posture (55% of days) limits upside capture during sustained rallies.
2.Volatile markets (2025 YTD):BlindTrade significantly outperforms, achieving 4×the
cumulative return of SPY (22.8% vs 6.1%). The policy’s ability to adapt intent (defen-
sive/aggressive) provides value when market direction is uncertain.
Implications.BlindTrade appears better suited for volatile or uncertain market conditions than for
sustained bull markets.
E ADDITIONALFIGURES
15

Accepted at the ICLR 2026 Workshop on Advances in Financial AI (FinAI)
RA W DA TA INPUTS
OHLCV Prices News Headlines Sector Mapping S&P 500 Universe
M1 | DA TA ANONYMIZA TION
Ticker Masking
AAPL→STOCK_0026
Entity Masking
Knowledge Graph API
M2 | MULTI-AGENT LLM FEA TURE GENERA TION
Momentum
Agent
News Event
Agent
Reversion
Agent
Risk Regime
Agent
Sentence Embeddings→( ˆµ, ˆσ)
M3 | FEA TURE V ALIDA TION(Data Quality Check)
Walk-Forward
Normalization
LLM vs RAW
(∆IC Comparison)
Horizon
Optimization
M4 | SEMGA T ENCODER (GNN)
Sector-Prior Graph
11 GICS Sectors
Semantic Edge
Augmentation
Graph Attention
Networks
M5 | RL PORTFOLIO OPTIMIZA TION (PPO-DSR)
State: GNN Embed.
+ ˆµ, regime
Action: Portfolio
Weightsw t
Reward: DSR
At =r t −η·SR t−1
M6 | BACKTESTING & EV ALUA TION
OOS Performance
Sharpe, Return, MDD Ablation Studies Negative Control Leakage Audit
Static Policy Online Adaptation ⟳Monthly→M5
PreprocessingValidationLearningEvaluation
Figure 2: The BlindTrade Pipeline: Data anonymization, Multi-agent LLM feature generation, IC
validation, SemGAT encoding, Intent-conditioned RL (PPO-DSR), and Backtesting.
16

Accepted at the ICLR 2026 Workshop on Advances in Financial AI (FinAI)
IC RankIC
−0.015
−0.010
−0.005
0.000
Mean IC
Negative control IC → 0 confirms no leakage
(a) Signal quality: baseline vs shuffled
Baseline
Neg. Control (shuffle)
2025-01 2025-022025-03 2025-04 2025-05 2025-06 2025-07 2025-08
Date
−0.20
−0.15
−0.10
−0.05
0.00
0.05
Cumulative return
(b) Performance collapse under negative control
Baseline Top-K
Neg. Control Top-K
Figure 3: Leakage audit via negative control. When predictions are randomized, IC disappears and
performance collapses.
2024-03 2024-05 2024-07 2024-09 2024-11 2025-01 2025-03 2025-05 2025-07
0.0
0.2
0.4
0.6
0.8
1.0Intent probability
 Val start  OOS start
(a) Intent probability timeline
Defensive (p₀) Neutral (p₁) Aggressive (p₂)
Train Val OOS
0
20
40
60
80
100Share of days (%)
(b) Intent share by split (argmax)
Defensive
Neutral
Aggressive
Figure 4: Intent probability timeline across Train/Val/OOS periods. (a) Daily intent probabilities
show how the policy adapts to market conditions. (b) Intent distribution remains stable across splits,
demonstrating generalization.
Def Neu Agg
0
20
40
60
80
100Daily turnover (%)
μ=2.9% μ=1.8% μ=0.4%
(a) Turnover by intent
Def Neu Agg
5.0
7.5
10.0
12.5
15.0
17.5
20.0
22.5
25.0Max single weight (%)
(b) Max weight by intent
Def Neu Agg
10
12
14
16
18
20Effective N (1/HHI)
Kruskal p=0.000 ***
(c) Effective N (concentration) by intent
Figure 5: Intent-conditioned policy behavior. (a) Defensive mode shows higher turnover (2.9%/day)
for active rebalancing. (b-c) Max weight and concentration (Effective N) differ significantly by
intent (Kruskal p=0.000).
17

Accepted at the ICLR 2026 Workshop on Advances in Financial AI (FinAI)
−0.50 −0.25 0.00 0.25 0.50
t-SNE dimension 1
−1.00
−0.75
−0.50
−0.25
0.00
0.25
0.50
t-SNE dimension 2
Ellipse: ~95% confidence region
RL State Embedding: Train / Validation / OOS
Train (n=150) Validation (n=63) OOS (2025) (n=143)
Figure 6: t-SNE visualization of RL state vectors across Train/Val/OOS splits. Overlapping distri-
butions suggest similar feature characteristics across splits.
RL POLICY NETWORK
GNN Output
market_state(64)
node_embh(N×128)
global_stats(4)
Intent Head
state→{D, N, A}
Aux Features
entropy + risk (2)
Stock Selector
node_emb (128)
+ market_state (64)
+ intent_emb (32)
+ prev_weight (1)
⇒scores
wt−1 (N)
Dirichlet
α→w t
Action
wt ∈R K
feedback:w t →w t−1
Figure 7: RL Policy Network Architecture. The Intent Head selects defensive/neutral/aggressive
mode from aggregated LLM statistics and GNN market state, then the Node Score Head produces
stock-level scores, which parameterize a Dirichlet distribution for portfolio weights.
18
