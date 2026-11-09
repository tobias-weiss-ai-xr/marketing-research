---
title: 'PortBench: A Correlation-Aware, Full-Pipeline Benchmark for LLM-Driven Portfolio Management'
url: https://arxiv.org/abs/2605.27887
category: ai-marketing
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Yuxuan Zhao
- Sijia Chen
- Ningxin Su
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.27887
pages: 40
chars: 137246
fetched_at: '2026-11-08T13:26:16+00:00'
kb_version: 1
---

# PortBench: A Correlation-Aware, Full-Pipeline Benchmark for LLM-Driven Portfolio Management

PORTBENCH: A Correlation-Aware, Full-Pipeline Benchmark
for LLM-Driven Portfolio Management
Yuxuan Zhao1,2 Sijia Chen2 Ningxin Su2
1Yantai Research Institute of Harbin Engineering University
2The Hong Kong University of Science and Technology (Guangzhou)
sijiachen@hkust-gz.edu.cn
Project page: https://portbench.github.io/
Abstract
Large language models (LLMs) have shown
strong performance across diverse financial
tasks, yet portfolio management (PM) remains
poorly evaluated. Existing benchmarks exhibit
two gaps: they are often equity-only and ig-
nore cross-asset correlations; they provide lim-
ited insight into where errors arise and how
they affect subsequent decisions. We introduce
PORTBENCH, a benchmark with market data
spanning six asset classes from 2015 to 2025.
PORTBENCHcomprises a static QA dataset
of 6,269 questions across seven task templates
and a dynamic five-stage portfolio evaluation.
Dynamic evaluation uses a class-level correla-
tion score for allocation and CEPS to summa-
rize reference-based stage scores. We further
evaluate under three stress windows and three
risk profiles, and support real-time evaluation
on newly arriving market data. Evaluating ten
LLMs reveals a disconnect: high financial QA
scores do not ensure consistent portfolio out-
performance. LLMs concentrate exposure in
correlated assets, and their portfolios achieve
higher Sharpe than equal weighting in 54.2%
of 120 evaluations across four market periods.
Our source code is available at this https URL.
1 Introduction
Large language models (LLMs) have shown in-
creasing capabilities across diverse financial tasks,
spurring benchmarks for financial knowledge,
numerical reasoning, and investment decision-
making (Chen et al., 2022; Xie et al., 2023, 2024;
Guo et al., 2025b; Tang et al., 2025). Portfo-
lio management (PM), however, remains inade-
quately evaluated. PM requires diversified allo-
cations to reduce volatility and risk, which in turn
requires accounting for intra- and inter-class corre-
lations (Markowitz, 1952; Qian, 2005). Investment
decisions put capital at risk. Assessing the relia-
bility of PM systems therefore requires evaluating
each stage and how its errors affect later decisions.
However, existing financial benchmarks fail to
comprehensively evaluate PM due to two gaps.
First, they often restrict coverage to a single as-
set class (Liu et al., 2022; Xie et al., 2024; Li et al.,
2024; Chen et al., 2025a; Oh et al., 2025); even in
multi-asset settings, assets are evaluated in isola-
tion (Li et al., 2025b), which ignores cross-asset
correlation structures. This design fails to distin-
guish between highly concentrated portfolios and
genuinely diversified ones, even when their returns
are identical. Additionally, LLM-based multi-agent
systems for portfolio construction are consistently
evaluated on equities alone with proprietary back-
tests that differ in data period, stock pools, and
metrics, making cross-method comparison infeasi-
ble (Yu et al., 2024; Guo et al., 2025a).
Second, existing benchmarks provide limited di-
agnosis of the investment decision process. Most
financial benchmarks rely on static QA that probes
knowledge without linking answers to realistic al-
location (Xie et al., 2023, 2024; Tang et al., 2025).
The few that test portfolio decisions use single-
step predictions or cover only part of the work-
flow (Chen et al., 2025a; Xu et al., 2025; Saha et al.,
2025); none spans the full cycle of market inter-
pretation, signal generation, weight optimization,
execution, and risk monitoring. These evaluations
leave unclear where errors arise and how they af-
fect subsequent decisions. Most further assume one
implicit risk profile in normal markets, leaving the
resilience of PM strategies under stress and align-
ment with investor-specific risk tolerances largely
untested (Chen et al., 2025b; Li et al., 2026a).
To address these gaps, we introduce PORT-
BENCH, a benchmark for LLM-driven PM with
market data spanning six asset classes from 2015 to
2025. PORTBENCHevaluates LLMs through two
complementary layers: a static QA dataset probing
financial reasoning, and a dynamic five-stage sand-
box that evaluates decisions at each stage of the PM
cycle under sequential market conditions. Beyond
1
arXiv:2605.27887v6  [cs.AI]  9 Oct 2026

A. Static QA 6,269 QA pairs · T1–T7
2. Two Complementary Layers
3. Core Evaluation Dimensions
A. Correlation-Aware Allocation
Intra-
class
Inter-
class
Concentration ↓ Hedging ↑
S3 score: Weight accuracy + correlation structure
B. Process-Level Diagnosis C. Stress & Profile Robustness
183 financial instruments
Jan 2015 – Dec 2025
Equities: 126
Commodities: 16
Bonds: 15
Cryptocurrency: 12
Real Estate: 10
Cash Equivalents: 4
A shared market foundation for
evaluations.
B. Dynamic Evaluation Five-stage pipeline
daily prices & returns
macroeconomic indicators
time-aligned financial news
cross-asset correlation structure
Paired stage interventions
Original
Corrected
Compare downstream changes
CEPS across the pipeline
S1 S2 S3 S4 S5
Normal Stress Real-time
Investor risk tolerance
Conservative Balanced Aggressive
Now
New
Historical
1. Market Base Dataset
L4
Portfolio-Level
Judgment
L3
Multi-Asset
L2
Pairwise
L1
Single Asset
LLM decisions Sandbox
Market
Interpretation
Signal
Generation
Weight
Optimization
Execution
Simulation
Risk
Monitoring
Figure 1: Overview of PORTBENCH. A shared multi-asset market base supports complementary static QA and
dynamic five-stage evaluation. The benchmark assesses correlation-aware allocation, stagewise diagnostics through
CEPS and paired interventions, and robustness across evaluation periods and investor risk profiles.
historical replay, PORTBENCHalso supports real-
time evaluation on up-to-date market data. Figure 1
provides an overview. Our contributions are:
• A Multi-Asset Market Dataset.We construct
a 2015–2025 corpus of 183 market series across
six asset classes, with prices, macro series, and
time-aligned news, enabling correlation-aware
PM evaluation beyond single-asset settings.
• A Dual-Layer Evaluation Framework.We
pair static QA with a five-stage pipeline to eval-
uate financial reasoning and its use in portfolio
decisions. Within the pipeline, CEPS summa-
rizes reference-based stage scores, while paired
interventions trace how local changes affect later
decisions. We then evaluate the resulting portfo-
lios across historical stress windows and investor
profiles, with real-time evaluation extending cov-
erage beyond historical replay.
• A QA–Portfolio Performance Gap.Across the
ten evaluated LLMs, high financial QA scores do
not ensure consistent portfolio outperformance.
Models concentrate exposure in correlated as-
sets, and their portfolios beat equal weighting on
Sharpe in 54.2% of 120 evaluations across four
historical market periods.
2 PortBench
2.1 Benchmark Construction
We construct themarket base dataset, covering
six asset classes: equities (126 tickers), commodi-
ties (16 tickers), bonds (15 series), cryptocurrency
(12 tickers), real estate (10 series), and cash equiv-
alents (4 series). In total, the dataset comprises
183 market series spanning January 2015 through
December 2025. For each instrument, we collect
daily price histories, return series, and associated
news text; macroeconomic indicators include in-
terest rates, inflation measures, credit spreads, and
volatility indices. Stress windows are drawn from
within this range and do not overlap with the nor-
mal period. Correlation analysis of the market base
dataset reveals that inter-class average correlations
are generally low, while intra-class correlations are
strongly positive; see Appendix B for details.
2.2 Evaluation Framework
Building on the market base dataset, PORTBENCH
evaluates LLMs through two complementary lay-
ers, as illustrated in Figure 2.
QA evaluation.In the static layer, 6,269 QA
pairs are generated across seven task templates
spanning four complexity levels (L1–L4), probing
financial reasoning abilities from single-asset pre-
diction and sizing (L1: T1–T3) through pairwise
allocation (L2: T4) and constrained multi-asset op-
timization (L3: T5–T6) to regime-driven judgment
(L4: T7). Automated generation from historical
data enables scalable template additions and dataset
regeneration without manual annotation. Represen-
tative QA samples are in Appendix H.2.
Dynamic evaluation.The market base dataset
is replayed point-in-time across the evaluation win-
dow. At each rebalance, the model receives a mar-
ket snapshot and sequentially produces S1 (Market
Interpretation), which assigns sentiment scores and
identifies the prevailing regime; S2 (Signal Gen-
eration), which maps these views to directional
2

Static QA Evaluation 6,269 Questions | 7 Templates | L1 -> L4 Complexity
L1 Single Asset L2 Pairwise L3 Multi-Asset L4 Full Portfolio
T1
Return Direction
Will ETH-USD rise,
fall, or stay flat?
T2
VaR Estimation
What is XLV's 1-day
95% historical VaR?
T3
Position Sizing
What is VCIT's
maximum
feasible weight?
T4
Pairwise Allocation
What XLY/STIP weights
minimize variance?
T5
Max-Sharpe
What four-asset
weights maximize
Sharpe?
T6
Rebalancing
Rebalance? Which
trade is largest?
T7
Regime & Allocation
Which regime? How
should six classes shift?
Market Information
Investor Profile
Evaluation Period
Prices & Returns
Macro Indicators
Time-Aligned
News
Cross-Asset
Correlations
Current Holdings
Dynamic CEPS & Paired Intervention Portfolio State Propagation
State t Execution State t+1
Holdings + cash Trades + costs NAV + weights
Market returns update state before the next decision
Normal
Historical Stress
Real-Time
Conservative Aggressive
Balanced
Dynamic Evaluation At each rebalance date t
S1–S3: LLM decisions S4–S5: deterministic scores
Snapshot at t
Market data
Current state
S1: Market
Interpretation
Asset views
Regime
S2: Signal
Generation
Directions
Strength
S3: Weight
Optimization
Target weights
Constraints
Deterministic
sandbox
Rebalance
Apply costs
S4: Execution
Simulation
Turnover
vs. oracle
S5: Risk
Monitoring
VaR / drawdown
Weight drift
CEPS: score the cascade Paired intervention
S1 S2 S3 S4 S5
CEPS = mean − drop penalty
Original Corrected
S2 S3 S4 S5
Fix S2; compare S3–S5
Figure 2: Overview of the evaluation framework.Top:static QA spans seven templates (T1–T7), from single-asset
tasks at L1 to full-portfolio judgment at L4.Bottom:at each rebalance, the LLM produces S1–S3, while the
sandbox executes the allocation and evaluates execution and risk at S4–S5. CEPS summarizes reference-based stage
scores, paired interventions test downstream effects, and the portfolio state carries into the next decision.
signals; and S3 (Weight Optimization), which pro-
poses portfolio weights. The sandbox executes
the S3 allocation under fixed transaction costs. S4
(Execution Simulation) scores turnover agreement
with the reference, while S5 (Risk Monitoring)
compares lookback VaR, drawdown, and a rule-
based rebalance flag computed from the proposed
and reference allocations. Both deterministically
evaluate S3 under identical execution and risk rules
across models. A stateful sandbox records stage
scores, proposed weights, and the resulting NA V
trajectory, linking allocations to realized costs, re-
turns, and risk under a common execution policy.
Beyond historical replay, PORTBENCHsupports
real-time evaluation on recent market data. Ap-
pendix C details evaluation and replay; Appendix H
shows snapshots and full pipeline traces.
Pipeline metrics.CEPS summarizes reference-
based stage scores with a penalty for downstream
score drops. Let σt ∈[0,1] denote the nor-
malized score at pipeline stage t∈ {1, . . . ,5},
and let ¯σ= 1 5 P5 t=1 σt be the mean stage score.
With cascade penalty weight λ= 0.1 , CEPS=
clip

¯σ−λP4 t=1 max(σt −σ t+1,0),0,1  . At
the same mean score, CEPS assigns a lower value
to a pipeline with larger downstream drops, penal-
izing higher upstream scores followed by lower
downstream scores. ForS3, we combine reference-
weight similarity with class-level correlation struc-
ture: σ3 =α sacc(w,w ∗) + (1−α)s corr(w), with
α= 0.5 . Here sacc(w,w ∗) = 1− 1 2 P i |wi −w ∗ i |
measures total-variation proximity to a signal- and
profile-constrained reference allocation w∗ esti-
mated from the lookback window, while scorr com-
bines exposure to internally correlated classes with
cross-class hedging. The lookback reference sup-
plies a reproducible decision-time target; returns
and risk are evaluated from the resulting portfo-
lios. Asset-level covariance analysis complements
the class-level score by testing how within-class
weighting affects portfolio risk at fixed asset selec-
tion and class exposure, see Section 4.2 for details.
Appendix C.2 defines the scores, and Appendix F.6
examines ranking sensitivity toλandα.
Paired stage interventions.To measure down-
stream effects, PORTBENCHreplaces one stage out-
put with its reference output, reruns the subsequent
stages, and compares their scores with the original
branch. This auxiliary diagnostic scores generated
S4/S5 plans; the main ranking scores turnover and
lookback risk-state agreement (Appendix F.8).
Stress windows and investor profiles.We re-
port normal-period CEPS with a stress drawdown
gate under three historical windows (2015 China
Shock, 2020 COVID Crash, 2022 Market Decline),
and across three investor profiles (conservative, bal-
anced, aggressive) whose exposure and drawdown
constraints condition the S1/S2 prompts and their
3

resulting signals. We compare matched allocations
and realized returns and risk across profiles. Ap-
pendix C.3 gives profile limits and gate criteria.
3 Experiments
3.1 Experimental Setup
LLMs.We evaluate ten frontier LLMs: Kimi-
K2.6 (Kimi Team, 2026), Qwen3.7-Max (Qwen
Team, 2026c), Qwen3.6-Plus (Qwen Team,
2026b), Qwen3.6-35B-A3B (Qwen Team, 2026a),
GLM-5.1 (GLM-5-Team et al., 2026), Doubao-
Seed-2.0-Lite and Doubao-Seed-2.0-Pro (DB-2.0-
Lite/Pro) (ByteDance Seed, 2026), Hunyuan3-
Preview (HY3-Preview) (Tencent Hy Team, 2026),
and DeepSeek-V4-Flash and DeepSeek-V4-Pro
(DS-V4-Flash/Pro) (DeepSeek-ai, 2026).
Evaluation Protocol.We set the temperature
to 0 and maximum output length to 8192 tokens,
with thinking mode enabled by default. For static
QA, each model answers the same 50 test questions
per template using zero-shot prompting. For dy-
namic evaluation, models produce S1–S3 outputs
and are evaluated through the five-stage pipeline un-
der three investor profiles, using monthly decisions
in the normal period and weekly decisions during
stress windows to capture portfolio responses to
rapidly changing market conditions. We use a 2024
bull-market window as the normal period and three
historical stress windows for the stress gate and
cross-period Sharpe comparisons. All strategies
use the same eligible assets, next-close execution,
and transaction costs; see Appendix C for details.
Baselines.We compare LLM-driven portfolios
against six classical strategies: (1) Equal-Weight
(EqW, 1/n) allocates capital uniformly across as-
sets; (2) 60/40 allocates 60% to equities and 40%
to bonds; (3) Risk Parity (RiskPar) weights assets
inversely to volatility; (4) Covariance Risk Par-
ity (CovRiskPar) extends RiskPar using the full
covariance matrix for equal risk contribution; (5)
Minimum Variance (MinVar) selects the long-only
portfolio on the Markowitz efficient frontier that
minimizes variance (Markowitz, 1952); (6) Black–
Litterman (BL) blends prior returns with simple
views. These strategies retain their standard rules
across profiles and are evaluated on Sharpe ratio,
maximum drawdown, volatility, and total return.
3.2 Static QA Evaluation
Portfolio QA performance is task-dependent:
models excel at formula-based allocation but
Model T1 T2 T3 T4 T5 T6 T7 Mean
DS-V4-Flash.520.843 .9451.00.932 .652.843 .819
Qwen3.7-Max .500.859.9511.00.954 .724 .742.819
DS-V4-Pro.520.837 .9631.00 .992.652 .760 .818
DB-2.0-Lite .460 .798 .957 .956 .897 .810 .747 .804
DB-2.0-Pro .440 .847 .963 .991 .912 .824 .530 .787
Qwen3.6-Plus .440 .858.968 1.00.804 .640 .768 .783
GLM-5.1 .440 .855 .9641.00.421.882.738 .757
Qwen3.6-35B-A3B .460 .808 .9611.00.230 .564 .763 .684
HY3-Preview .460 .386 .336 .975 .958 .468 .783 .624
Kimi-K2.6 .420 .422 .493 .956 .280 .684 .320 .511
Table 1: Mean QA score by task template.
-15 -10 -5 0
Kimi-K2.6
Qwen3.6-35B-A3B
DS-V4-Pro
GLM-5.1
HY3-Preview
DS-V4-Flash
DB-2.0-Pro
Qwen3.6-Plus
Qwen3.7-Max
DB-2.0-Lite
EqW
60/40
BL
RiskPar
CovRiskPar
MinVar
LLMs
Baselines
A  2015 China
-25 -20 -15 -10 -5 0
B  2020 COVID
-30 -20 -10 0
C  2022 Bear
Maximum drawdown (%)
LLM pass Baseline pass Exceeds 10% 10% tolerance
Figure 3: Maximum drawdown under the conservative
profile in each stress regime.
remain weak on prediction and rebalancing.Ta-
ble 1 shows that eight of ten models exceed 0.94 on
T3; six score 1.00 on T4, and all reach at least 0.956.
In contrast, none exceeds 0.520 on return predic-
tion (T1), while rebalancing scores (T6) range from
0.468 to 0.882. T4–T5 (allocation with supplied co-
variance statistics) average 0.863, versus 0.652 for
T1–T2 and T6–T7 (prediction, risk estimation, re-
balancing, and regime detection); this 0.211 gap fa-
vors T4–T5 for eight of ten models (Appendix D.4).
Supplementary structured T3/T4 tasks show that
several LLMs retain near-ceiling performance on
position-sizing and allocation-constraint reasoning,
with details in Appendix D.3.
3.3 Pipeline Evaluation
Similar allocation scores conceal downstream
differences.Table 2 ranks GLM-5.1 first and
Qwen3.6-Plus second by CEPS under all three
profiles. Across the 30 model–profile combina-
tions, S1 ranges from .742 to .807 and S3 from
only .264 to .310, while turnover agreement (S4)
spans .121–.320 and risk-state agreement (S5) .000–
.409. Under the conservative profile, Qwen3.6-Plus
outperforms GLM-5.1 at four of five stages, but
GLM-5.1’s S4 score is nearly twice as high (.304
vs. .153), yielding a slightly higher CEPS (.299
vs. .292).Similar allocation scores can there-
fore mask differences in turnover and risk-state
agreement that affect overall pipeline rankings.
4

Profile Model S1 S2 S3 S4 S5 CEPS↑Sharpe↑Ret%↑MaxDD%↑Vol%↓GateConservative
GLM-5.1 .763 .438 .301 .304 .091 .2990.707 11.82−7.87 11.00 ×
Qwen3.6-Plus .774 .491 .310.153 .136.292 0.875 14.97−9.56 12.22 ×
Qwen3.6-35B-A3B .754 .405 .304 .217 .045 .263 0.99213.55−6.19 9.21 ×
Kimi-K2.6 .768 .394 .303 .269 .000 .261 0.445 8.25−6.59 9.94 ×
DS-V4-Flash .742 .315 .298 .320.022 .253−0.029 3.32−8.87 9.51 ×
HY3-Preview .778.489 .290 .121 .000 .251 0.547 9.00−6.38 9.21 ×
DS-V4-Pro .749 .339 .302 .217 .000 .239 0.616 10.07−7.50 9.87 ×
DB-2.0-Pro .750 .403 .295 .143 .000 .236 0.571 8.77 −5.73 8.34 ×
Qwen3.7-Max .746 .385 .291 .151 .000 .232 0.578 9.16−5.97 8.94 ×
DB-2.0-Lite .751 .339 .299 .143 .000 .223 0.740 10.79−6.46 8.98 ×
Balanced
GLM-5.1 .773 .472 .303 .296 .409 .3840.603 13.10−14.20 15.89 ✓
Qwen3.6-Plus .793 .531.298 .209 .091 .300 0.798 13.99−10.11 12.35 ✓
Qwen3.7-Max .774 .451 .297 .158 .182 .292 0.783 14.97−11.02 13.95 ✓
Kimi-K2.6 .786 .464 .297 .247 .000 .274 0.769 14.29−9.34 13.32 ✓
Qwen3.6-35B-A3B .772 .476 .295 .237 .000 .272 0.740 12.87−7.77 11.91 ✓
DS-V4-Pro .764 .387 .301 .289 .005 .266 0.542 9.46−6.93 10.29 ✓
DB-2.0-Pro .778 .483 .294 .179 .000 .263 0.662 12.09−9.83 12.36 ✓
HY3-Preview .791 .531.264 .133 .000 .258 0.650 11.52−8.05 11.66 ✓
DB-2.0-Lite .773 .387 .298 .137 .045 .244 0.83814.01−8.89 11.70 ✓
DS-V4-Flash .774 .321 .290 .172 .000 .226 0.609 9.89 −6.56 9.68 ×
Aggressive
GLM-5.1 .779 .510 .295 .310 .409 .3930.930 21.00−15.13 17.92 ✓
Qwen3.6-Plus .802 .566 .297 .162 .409.366 1.034 21.84−13.05 16.57 ✓
Qwen3.6-35B-A3B .786 .553 .299 .252 .318 .365 0.845 19.49−16.83 18.33 ✓
DB-2.0-Lite .787 .478 .300 .138 .364 .331 0.916 18.48−12.76 15.45 ✓
DB-2.0-Pro .787 .494 .300 .168 .273 .325 0.867 16.15−10.85 13.75 ✓
Qwen3.7-Max .781 .463 .303.190 .273 .323 0.733 15.41−13.20 15.79 ✓
Kimi-K2.6 .790 .514 .293 .199 .136 .304 0.890 19.34−13.08 16.99 ✓
DS-V4-Pro .783 .463 .303 .250 .014 .278 0.653 10.34 −6.63 9.65 ✓
HY3-Preview .807 .574.292 .132 .000 .274 0.673 11.78−8.74 11.61 ✓
DS-V4-Flash .795 .475 .298 .195 .009 .268 0.640 10.84−7.40 10.72 ✓
Baselines
EqW — — — — — — 0.710 10.75−6.16 9.36 —
60/40 — — — — — — 0.592 9.56−5.98 9.42 —
RiskPar — — — — — —−0.130 3.34−3.50 4.68 —
CovRiskPar — — — — — —−0.914 0.28−4.16 3.98 —
MinVar — — — — — —−3.761−0.82 −1.15 1.28—
BL — — — — — —−0.929−3.51−9.62 7.82 —
Table 2: Main pipeline results. Green = column best. “Gate” = pass all three stress scenarios under that profile.
LLMs ranked by CEPS within each profile.
Normal-period drawdown rankings can re-
verse under stress.In the normal period, 15 of the
30 model–profile cells outperform EqW on Sharpe,
and all 30 remain within their respective drawdown
limits. Figure 3 shows that all ten models fail at
least one conservative-profile scenario; nine pass
all three balanced-profile scenarios and all ten pass
the aggressive-profile scenarios. Under the bal-
anced profile, DS-V4-Flash moves from the small-
est normal-period drawdown (6.56%) to the largest
COVID-window drawdown (22.19%), becoming
the only model to fail that profile’s stress gate. Low
normal-market drawdown therefore does not estab-
lish stress resilience. Details are in Appendix E.1.
3.4 QA–Pipeline Rank Inversion
QA and pipeline rankings differ sharply.GLM-
5.1 moves from seventh in QA to first in balanced-
profile CEPS, Kimi-K2.6 from last to fourth, and
DS-V4-Flash from tied first to tenth ( ρ=−.32 ).
Direct QA–Sharpe correlations across ten models
range from −.67 to +.83 over the twelve period–
profile settings. Positive associations appear in con-
servative and balanced 2015–16 settings, while the
other ten intervals include zero (Appendix D.5).
The observed QA rankings do not consistently
carry over to portfolio outcomes.
Dynamic allocation requires combining mar-
ket interpretation, signals, and profile constraints
over the portfolio. T4/T5 test allocation with sup-
plied statistics. Appendix D examines task scores
through information ablations and supplementary
structured decisions.Dynamic evaluation tests
how local answers are used in portfolio construc-
tion, which standalone QA does not establish.
3.5 Cross-Period Evaluation
To probe performance under diverse market condi-
tions, we reuse the three stress windows and report
period Sharpe under three investor profiles: 2015–
16 (volatile), 2020 (COVID crash and rebound),
and 2022 (bear), alongside 2024 (bull). Across the
5

0 1
DS-V4-Flash
DS-V4-Pro
Qwen3.6-Plus
Qwen3.7-Max
Qwen3.6-35B-A3B
GLM-5.1
DB-2.0-Lite
DB-2.0-Pro
HY3-Preview
Kimi-K2.6
A  2015–16 Volatile
90% beat EqW
0 2
B  2020 COVID
77% beat EqW
-2 -1 0
C  2022 Bear
0% beat EqW
-0.5 0.0
D  2024 Bull
50% beat EqW
Sharpe − EqW
Conservative Balanced Aggressive Mean EqW
Figure 4: Sharpe relative to EqW across four market periods. Light shading marks ∆>0 (beat EqW). Panel
annotations report the fraction of model–profile pairs that beat EqW in each period; (d) uses a narrower axis scale.
120 evaluated model–profile–period cases, LLMs
beat EqW in 65 cases (54.2%). Figure 4 plots
Sharpe minus EqW for every model–profile pair.
Beat rates vary sharply: 77% in the 2020 crash-
and-rebound window, 90% in 2015–16, 50% in the
2024 bull market, and 0% in the prolonged 2022
bear market. EqW Sharpe is -0.602 in 2020, where
the mean model gap is +0.68, but reaches 0.710
in 2024; in 2022, every model–profile pair trails
EqW, with mean∆Sharpe −0.74.LLM portfolios
show no consistent Sharpe advantage over EqW
across these four windows.Across fixed model–
profile pairs, the mean range of ∆Sharpe over the
four periods is 1.84, compared with .71 across
profiles within the same model and period, show-
ing that relative performance varies more across
these market-window and decision-frequency set-
tings than across investor profiles. Appendices E.2
and E.3 report results and NA V trajectories.
3.6 Real-Time Evaluation
Evaluating historical markets risks leakage from
prices, headlines, or outcomes seen during LLM
pretraining (Li et al., 2025a; Chen et al., 2025a).
PORTBENCHtherefore supports real-time evalu-
ation with point-in-time inputs: at each decision
date, the model receives only data available through
the previous close and runs the five-stage pipeline.
Over 12 trading days (2026-07-16–07-31), we col-
lect 72 decisions from six models with daily re-
balancing. Mean S1 scores range from .78 to .82,
while S4 turnover agreement remains low at .047–
.163. This initial run demonstrates stage-level eval-
uation on newly arriving data and more frequent
portfolio decisions. Appendix G reports daily stage
scores and lookback CEPS.
4 Deep Analysis
4.1 Local Gains Can Fade or Reverse
Paired interventions under the balanced profile test
how replacing one stage with its reference affects
later decisions. In this auxiliary diagnostic, S4/S5
score the model’s execution and risk-management
plans. Replacing S1 with its reference output raises
S2 by +.626 in normal episodes; both references
follow the same trailing-return rule. Its mean effect
on S3 is only +.017 and is negative in 40 of 110
episodes. Replacing S2 raises S3 by only +.023,
with 39 negative cases. Under stress, S2 and S3
replacement reduce S5 by −.059 and −.056, al-
though most episode-level S5 changes are zero.
Large gains at the next stage become much
smaller or turn negative at later stages.Case
traces reveal execution and risk changes missed by
stage scores; see Appendix F.8 for details.
4.2 Broad Holdings Conceal Correlated Risk
The 330 saved 2024-normal allocations hold 73
assets on average, yet still concentrate weight in
correlated assets. For each decision, we construct
a matched allocation by equalizing weights among
held assets within each class while preserving asset
selection, class weights, and uninvested cash. This
isolates the risk effect of within-class weights.
6

0 .04 .08
Weighted correlation gap
DS-V4-Flash
DS-V4-Pro
Qwen3.6-Plus
Qwen3.7-Max
Qwen3.6-35B-A3B
GLM-5.1
DB-2.0-Lite
DB-2.0-Pro
HY3-Preview
Kimi-K2.6
+0.009
+0.010
+0.072
+0.058
+0.047
+0.030
+0.029
+0.027
+0.012
+0.039
A  Correlation exposure
0 50 100
Variance-gap share (%)
Within-class covariance
76.4%
Individual-asset variance
23.5%
Cross-class covariance
0.1%
B  Variance decomposition
Cons. Bal. Agg.
Investor profile
DS-V4-Flash
DS-V4-Pro
Qwen3.6-Plus
Qwen3.7-Max
Qwen3.6-35B-A3B
GLM-5.1
DB-2.0-Lite
DB-2.0-Pro
HY3-Preview
Kimi-K2.6
1.1 1.8 3.0
1.7 3.2 1.4
15.6 14.4 24.2
9.5 19.6 24.9
-7.1 7.0 16.3
0.3 15.4 13.4
-1.2 9.1 20.2
-6.2 10.1 16.8
0.0 4.8 5.7
1.7 10.2 18.4
C  Volatility reduction
−10
0
10
25
%
Figure 5: Correlation risk at fixed holdings and asset-class weights.A:Mean difference in volatility-weighted
pairwise correlation.B:Contributions to the mean portfolio-variance difference across all 330 decisions; percentages
are shares of this difference. Differences in A and B are model minus within-class equal weighting over the same
held assets.C:Mean relative volatility reduction (%) from equalization; negative values indicate increased volatility.
Across ten models, three profiles, and eleven
decision dates, this equalization lowers volatility
estimated from lookback data by 8.5% on average,
with reductions in 271/330 decisions. Figure 5A
shows higher volatility-weighted pairwise correla-
tion under model weights for all models. Panel B
attributes 76.4% of the mean variance difference to
within-class covariance, versus 23.5% to individual-
asset variance terms. Panel C shows larger mean
volatility reductions under more aggressive pro-
files: 1.6%, 9.6%, and 14.4% for conservative, bal-
anced, and aggressive allocations.Diversification
depends on how capital is distributed among cor-
related holdings, even when asset selections and
class exposures are unchanged.Appendix F.9
gives the covariance decomposition, model–profile
results, and sensitivity analyses.
Active allocation and realized risk.Across the
30 cells, the mean total-variation distance is 0.306
from EqW and 0.890 from the profile-constrained
reference. Figure 6 relates distance from EqW to
realized outcomes. Larger deviations from EqW
are associated with higher volatility ( ρ=.65 ),
drawdown magnitude ( ρ=.61 ), and ∆Sharpe
(ρ=.51 ) in the normal period. The models there-
fore take meaningful active positions, with higher
relative Sharpe accompanied by greater volatility
and drawdowns (DeMiguel et al., 2009). Moving
from conservative to aggressive increases distance
from EqW by .070 on matched allocations.
Allocation-to-execution gap.Under the bal-
anced profile, every model produces less turnover
than the reference; overall, the mean model-to-
reference turnover ratio is .203. Reference al-
locations hold 8–14 securities, with maximum
weights of .24–.72, whereas model allocations
spread weight more broadly. Total-variation dis-
tance from the reference averages .890, giving
mean S3 reference-weight similarity of .110. Mean
model HHI is .0207, whose reciprocal is about 48
effective positions. The allocations differ from the
reference in both concentration and turnover, ex-
plaining why partial credit for class exposure can
coexist with low S4 scores. Appendix F.4 reports
the diagnostics; Appendix H.3 gives full traces.
4.3 Performance Reverses across Regimes
In 2020, 23 of 30 cases beat EqW, whereas none
do so in 2022.Both windows use weekly decisions,
contrasting a sharp crash and recovery with a pro-
longed decline. EqW’s Sharpe is similar in these
windows ( −.602 versus −.540), whereas mean
model Sharpe falls from .074 to −1.281. The re-
versal therefore reflects changes in model-portfolio
performance, rather than simply a stronger bench-
mark.The mean relative Sharpe advantage is
largest in the crash-and-rebound window.The
mean Sharpe advantage of aggressive over conser-
vative profiles is largest in 2020 at +.935, com-
pared with −.039 in 2022 and +.214 in 2024 (Ap-
pendix E.2); details are in Appendix F.7.
4.4 Risk Profiles Shift Exposure
On matched model–date pairs, shifting from con-
servative to aggressive raises risk-asset exposure by
.175 and lowers bond-plus-cash exposure by .162.
Normal-period volatility rises by .050 for nine of
ten models and drawdown magnitude by .047 for
eight. Mean Sharpe increases by .214, with nine
improving and one declining. Under stress, the
shift raises volatility for all ten in 2020 and 2022.
7

Figure 6: Active-allocation diagnostics across 30 normal-period model–profile cells, with gray paths connecting the
three profiles of each model.A:Total-variation distance from EqW versus ∆Sharpe.B:The same distance versus
drawdown magnitude. Shaded regions mark∆Sharpe>0in A and drawdowns larger than EqW in B.
Yet total return rises for all ten in the 2020 rebound
and falls for nine in the 2022 decline. In 2022, five
models achieve higher Sharpe under the aggres-
sive profile, yet four have lower returns and deeper
drawdowns. With negative excess returns, higher
volatility can make Sharpe less negative, highlight-
ing the need to assess returns and drawdowns along-
side Sharpe.Profiles change exposure, risk, and
normal-period returns, while the return advan-
tage varies across periods.Figure 5C shows more
scope to reduce estimated volatility in aggressive
portfolios through within-class reweighting with-
out changing asset selections or class exposures.
Appendix F.5 reports matched changes.
5 Related Work
Financial LLM benchmarks have progressed from
knowledge retrieval (Chen et al., 2021, 2022; Xie
et al., 2023) to investment decision-making (Xie
et al., 2024; Zhang et al., 2025b; Luo et al., 2025a),
yet portfolio management evaluations remain lim-
ited to static QA, single-asset-class backtests, or
asset-by-asset backtests (Liu et al., 2022; Li et al.,
2024; Chen et al., 2025a; Li et al., 2025b). Stock-
Bench (Chen et al., 2025a) introduces process-level
analysis but lacks cross-asset correlation scoring
and investor-profile adaptation; LLM agents for
PM (Yu et al., 2024; Guo et al., 2025a; Li et al.,
2025d) rely on proprietary backtests that assess
only terminal outcomes (Chen et al., 2025b; Li
et al., 2026a). Despite robust portfolio construc-
tion relying on covariance structures (Markowitz,
1952; Qian, 2005) and non-LLM methods exploit-
ing them (Zhang et al., 2025a), cross-asset correla-
tion risk remains underexamined in LLM portfolio
evaluation (Chen et al., 2025c). PORTBENCHex-
amines how multi-asset allocation decisions trans-
late into portfolio risk across market regimes and
investor profiles. Full discussion is in Appendix A.
6 Conclusion
We presented PORTBENCH, a benchmark for LLM-
driven portfolio management with market data
spanning six asset classes from 2015 to 2025.
PORTBENCHprovides a multi-asset market dataset
of 183 market series with prices, macro series, and
time-aligned news, alongside a dual-layer evalua-
tion framework combining static PM QA with a
five-stage evaluation of historical portfolios. The
framework uses a class-level correlation metric,
asset-level covariance diagnostics, and CEPS, and
supports stress-window, investor-profile, and real-
time evaluation. Despite high financial QA scores,
the evaluated LLMs fail to beat equal weighting
on Sharpe in 55 of 120 evaluations across four his-
torical periods. Their portfolios hold many assets,
yet within-class weights concentrate exposure in
correlated holdings, limiting diversification. These
findings expose a gap between financial QA and
portfolio performance: LLMs concentrate corre-
lated exposures and show no consistent Sharpe ad-
vantage over equal weighting across these periods.
8

Limitations
Although PORTBENCHprovides a comprehensive
evaluation framework, several limitations remain:
(1) The sandbox environment relies on determin-
istic transaction costs applied to historical price
data, so it does not capture real-world microstruc-
ture dynamics, liquidity constraints, and order-flow
impact. Integrating generative market simulators
like MarS (Li et al., 2025c) to model tokenized
order flow and support shock injection would pro-
vide more realistic execution feedback. (2) His-
torical evaluation uses monthly decisions in the
normal period and weekly decisions in three se-
lected stress windows. The daily real-time window
covers twelve trading days (Appendix G); longer
real-time evaluation would help test whether the
results hold across periods. (3) The model pro-
duces S1–S3 through a fixed set of isolated LLM
prompts without persistent memory, external tool
access, or multi-agent coordination; the sandbox
then computes the S4/S5 execution and risk scores
used in the ranking from the S3 allocation (Xiao
et al., 2025; Li et al., 2025d). Future work should
adopt agentic methods that incorporate tool calling,
long-horizon memory, and inter-agent communica-
tion to improve portfolio management.
Ethical Statement
PORTBENCHis designed as a research benchmark
for evaluating LLM capabilities in portfolio man-
agement and is not intended as financial advice or
as a decision-support tool for real investment. All
evaluations use publicly available historical market
data; no proprietary, private, or personally identi-
fiable information is used. The benchmark does
not involve human subjects, and no crowd-sourced
annotations were collected. We caution against
deploying LLM-generated portfolio allocations in
live trading without rigorous human oversight. As
our experiments demonstrate, the evaluated mod-
els fail to consistently outperform simple heuristic
baselines and exhibit fragile behavior under stress
conditions. The benchmark’s stress-test evalua-
tion is specifically designed to surface such failure
modes before deployment, but passing the stress
gate does not certify safety in real-world use.
LLM Statement
We used LLM-based tools to polish the writing and
refine the language of this paper.
References
ByteDance Seed. 2026. Seed2.0 model card: To-
wards intelligence frontier for real-world complex-
ity. https://seed.bytedance.com/en/
blog/seed-2-0-official-launch.
Yanxu Chen, Zijun Yao, Yantao Liu, Amy Xin, Jin Ye,
Jianing Yu, Lei Hou, and Juanzi Li. 2025a. Stock-
bench: Can llm agents trade stocks profitably in real-
world markets?arXiv preprint arXiv:2510.02209.
Zhiyu Chen, Wenhu Chen, Charese Smiley, Sameena
Shah, Iana Borova, Dylan Langdon, Reema Moussa,
Matt Beane, Ting-Hao Huang, Bryan Routledge, and
William Yang Wang. 2021. Finqa: A dataset of nu-
merical reasoning over financial data. InProceedings
of the 2021 Conference on Empirical Methods in Nat-
ural Language Processing, pages 3697–3711.
Zhiyu Chen, Shiyang Li, Charese Smiley, Zhiqiang Ma,
Sameena Shah, and William Yang Wang. 2022. Con-
vfinqa: Exploring the chain of numerical reasoning
in conversational finance question answering. In
Proceedings of the 2022 conference on empirical
methods in natural language processing, pages 6279–
6292.
Zichen Chen, Jiaao Chen, Jianda Chen, and Misha
Sra. 2025b. Standard benchmarks fail–auditing llm
agents in finance must prioritize risk.arXiv preprint
arXiv:2502.15865.
Zichen Chen, Jianda Chen, Jiaao Chen, and Misha Sra.
2025c. From tasks to teams: A risk-first evaluation
framework for multi-agent LLM systems in finance.
InICML 2025 Workshop on Reliable and Responsible
Foundation Models.
DeepSeek-ai. 2026. Deepseek-v4: Towards
highly efficient million-token context intel-
ligence. https://huggingface.co/
deepseek-ai/DeepSeek-V4-Pro.
Victor DeMiguel, Lorenzo Garlappi, and Raman Uppal.
2009. Optimal versus naive diversification: How
inefficient is the 1/n portfolio strategy?The review
of Financial studies, 22(5):1915–1953.
Ziliang Gan, Dong Zhang, Haohan Li, Yang Wu,
Xueyuan Lin, Ji Liu, Haipang Wu, Chaoyou Fu,
Zenglin Xu, Rongjunchen Zhang, and Yong Dai.
2025. Mme-finance: A multimodal finance bench-
mark for expert-level understanding and reasoning.
InProceedings of the 33rd ACM International Con-
ference on Multimedia, pages 12867–12874.
GLM-5-Team, Aohan Zeng, Xin Lv, Zhenyu Hou,
Zhengxiao Du, Qinkai Zheng, Bin Chen, Da Yin,
Chendi Ge, Chenghua Huang, Chengxing Xie,
Chenzheng Zhu, Congfeng Yin, Cunxiang Wang,
Gengzheng Pan, Hao Zeng, Haoke Zhang, Haoran
Wang, Huilong Chen, and 167 others. 2026. Glm-5:
from vibe coding to agentic engineering.Preprint,
arXiv:2602.15763.
9

Taian Guo, Haiyang Shen, Jinsheng Huang, Zhengyang
Mao, Junyu Luo, Binqi Chen, Zhuoru Chen, Luchen
Liu, Bingyu Xia, Xuhui Liu, Yun Ma, and Ming
Zhang. 2025a. Mass: Multi-agent simulation
scaling for portfolio construction.arXiv preprint
arXiv:2505.10278.
Xin Guo, Haotian Xia, Zhaowei Liu, Hanyang Cao, Zhi
Yang, Zhiqiang Liu, Sizhe Wang, Jinyi Niu, Chuqi
Wang, Yanhui Wang, Xiaolong Liang, Xiaoming
Huang, Bing Zhu, Zhongyu Wei, Yun Chen, Weining
Shen, and Liwen Zhang. 2025b. Fineval: A chi-
nese financial domain knowledge evaluation bench-
mark for large language models. InProceedings of
the 2025 Conference of the Nations of the Ameri-
cas Chapter of the Association for Computational
Linguistics: Human Language Technologies, pages
6258–6292.
Pranab Islam, Anand Kannappan, Douwe Kiela, Re-
becca Qian, Nino Scherrer, and Bertie Vidgen. 2023.
Financebench: A new benchmark for financial ques-
tion answering.arXiv preprint arXiv:2311.11944.
Jihyeong Jeon, Jiwon Park, Chanhee Park, and U Kang.
2024. Frequant: A reinforcement-learning based
adaptive portfolio optimization with multi-frequency
decomposition. InProceedings of the 30th ACM
SIGKDD Conference on Knowledge Discovery and
Data Mining, pages 1211–1221.
John L Kelly. 1956. A new interpretation of information
rate.the bell system technical journal, 35(4):917–
926.
Kimi Team. 2026. Kimi k2.6: Advancing open-
source coding. https://www.kimi.com/
blog/kimi-k2-6.
Changlun Li, Yao Shi, Chen Wang, Qiqi Duan, Runke
Ruan, Weijie Huang, Haonan Long, Lijun Huang,
Nan Tang, and Yuyu Luo. 2025a. Time travel is
cheating: Going live with deepfund for real-time
fund investment benchmarking.Advances in Neural
Information Processing Systems, 38.
Haohang Li, Yupeng Cao, Yangyang Yu, Shashid-
har Reddy Javaji, Zhiyang Deng, Yueru He, Yuechen
Jiang, Zining Zhu, K. P. Subbalakshmi, Jimin Huang,
Lingfei Qian, Xueqing Peng, Jordan W. Suchow, and
Qianqian Xie. 2025b. Investorbench: A benchmark
for financial decision-making tasks with llm-based
agent. InProceedings of the 63rd Annual Meeting of
the Association for Computational Linguistics (Vol-
ume 1: Long Papers), pages 2509–2525.
Junjie Li, Yang Liu, Weiqing Liu, Shikai Fang, Lewen
Wang, Chang Xu, and Jiang Bian. 2025c. Mars: a
financial market simulation engine powered by gener-
ative foundation model. InInternational Conference
on Learning Representations, volume 2025, pages
39490–39524.
Weixian Waylon Li, Hyeonjun Kim, Mihai Cucuringu,
and Tiejun Ma. 2026a. Can llm-based financial in-
vesting strategies outperform the market in long run?
InProceedings of the 32nd ACM SIGKDD Confer-
ence on Knowledge Discovery and Data Mining V . 1,
pages 2711–2722.
Xiangyu Li, Yawen Zeng, Xiaofen Xing, Jin Xu, and Xi-
angmin Xu. 2025d. Hedgeagents: A balanced-aware
multi-agent financial trading system. InCompanion
Proceedings of the ACM on Web Conference 2025,
pages 296–305.
Yuan Li, Bingqiao Luo, Qian Wang, Nuo Chen, Xu Liu,
and Bingsheng He. 2024. Cryptotrade: A reflective
llm-based agent to guide zero-shot cryptocurrency
trading. InProceedings of the 2024 Conference on
Empirical Methods in Natural Language Processing,
pages 1094–1106.
Yuante Li, Xu Yang, Xiao Yang, Xisen Wang, Weiqing
Liu, and Jiang Bian. 2026b. R&d-agent-quant: a
multi-agent framework for data-centric factors and
model joint optimization.Advances in Neural Infor-
mation Processing Systems, 38.
Shu Liu, Shangqing Zhao, Chenghao Jia, Xinlin Zhuang,
Zhaoguang Long, Jie Zhou, Aimin Zhou, Man Lan,
and Yang Chong. 2025. Findabench: benchmarking
financial data analysis ability of large language mod-
els. InProceedings of the 31st International Confer-
ence on Computational Linguistics, pages 710–725.
Xiao-Yang Liu, Ziyi Xia, Jingyang Rui, Jiechao Gao,
Hongyang Yang, Ming Zhu, Christina Wang, Zhao-
ran Wang, and Jian Guo. 2022. Finrl-meta: Mar-
ket environments and benchmarks for data-driven
financial reinforcement learning.Advances in Neural
Information Processing Systems, 35:1835–1849.
Junyu Luo, Zhizhuo Kou, Liming Yang, Xiao Luo,
Jinsheng Huang, Zhiping Xiao, Jingshu Peng,
Chengzhong Liu, Jiaming Ji, Xuanzhe Liu, Sirui Han,
Ming Zhang, and Yike Guo. 2025a. Finmme: Bench-
mark dataset for financial multi-modal reasoning eval-
uation. InProceedings of the 63rd Annual Meeting of
the Association for Computational Linguistics (Vol-
ume 1: Long Papers), pages 29465–29489.
Yichen Luo, Yebo Feng, Jiahua Xu, Paolo Tasca, and
Yang Liu. 2025b. Llm-powered multi-agent system
for automated crypto portfolio management.arXiv
preprint arXiv:2501.00826.
Rosario N Mantegna. 1999. Hierarchical structure in
financial markets.The European Physical Journal B-
Condensed Matter and Complex Systems, 11(1):193–
197.
Harry Markowitz. 1952. Portfolio selection.The Jour-
nal of Finance, 7(1):77–91.
Daesan Oh, Taehwan Kim, Junkyu Jang, and Sung-
Hyuk Park. 2025. Democratizing alpha: Llm-driven
portfolio construction for retail investors using public
financial media. InProceedings of the 6th ACM
International Conference on AI in Finance, pages
326–334.
10

Edward Qian. 2005. Risk parity portfolios: Efficient
portfolios through true diversification.Panagora As-
set Management, 1(1):1–10.
Lingfei Qian, Xueqing Peng, Hanley Smith, Yi Han,
Yueru He, Haohang Li, Yupeng Cao, Yangyang Yu,
Guojun Xiong, Peng Lu, Yan Wang, Vincent Jim
Zhang, Huan He, Alejandro Lopez-Lira, Jimin
Huang, Jian-Yun Nie, and Sophia Ananiadou. 2026.
When agents trade: Live multi-market trading arena
for llm agents. InProceedings of the ACM Web Con-
ference 2026, pages 7833–7844.
Qwen Team. 2026a. Qwen3.6-35B-A3B: Agentic cod-
ing power, now open to all.
Qwen Team. 2026b. Qwen3.6-Plus: Towards real world
agents.
Qwen Team. 2026c. Qwen3.7: The agent frontier.
Preetha Saha, Jingrao Lyu, Arnav Saxena, Tianjiao
Zhao, and Dhagash Mehta. 2025. Large language
model agents for investment management: Founda-
tions, benchmarks, and research frontiers. InPro-
ceedings of the 6th ACM International Conference
on AI in Finance, pages 736–744.
Raj Shah, Kunal Chawla, Dheeraj Eidnani, Agam Shah,
Wendi Du, Sudheer Chava, Natraj Raman, Charese
Smiley, Jiaao Chen, and Diyi Yang. 2022. When
flue meets flang: Benchmarks and large pretrained
language model for financial domain. InProceedings
of the 2022 Conference on Empirical Methods in
Natural Language Processing, pages 2322–2335.
Zichen Tang, Haihong E, Ziyan Ma, Haoyang He, Ji-
acheng Liu, Zhongjun Yang, Zihua Rong, Rongjin
Li, Kun Ji, Qing Huang, Xinyang Hu, Yang Liu,
and Qianhe Zheng. 2025. Financereasoning: Bench-
marking financial numerical reasoning more credible,
comprehensive and challenging. InProceedings of
the 63rd Annual Meeting of the Association for Com-
putational Linguistics, pages 15721–15749.
Tencent Hy Team. 2026. Hy3 preview: The first step in
rebuilding the hy model. https://hy.tencent.
com/research/hy3.
Zhicheng Wang, Biwei Huang, Shikui Tu, Kun Zhang,
and Lei Xu. 2021. Deeptrader: a deep reinforcement
learning approach for risk-return balanced portfolio
management with market conditions embedding. In
Proceedings of the AAAI conference on artificial in-
telligence.
Yijia Xiao, Edward Sun, Di Luo, and Wei Wang. 2025.
Tradingagents: Multi-agents llm financial trading
framework. InThe First MARW: Multi-Agent AI in
the Real World Workshop at AAAI 2025.
Qianqian Xie, Weiguang Han, Zhengyu Chen, Ruoyu
Xiang, Xiao Zhang, Yueru He, Mengxi Xiao, Dong
Li, Yongfu Dai, Duanyu Feng, Yijing Xu, Haoqiang
Kang, Ziyan Kuang, Chenhan Yuan, Kailai Yang,
Zheheng Luo, Tianlin Zhang, Zhiwei Liu, Guojun
Xiong, and 15 others. 2024. Finben: A holistic fi-
nancial benchmark for large language models. In
Advances in Neural Information Processing Systems.
Qianqian Xie, Weiguang Han, Xiao Zhang, Yanzhao
Lai, Min Peng, Alejandro Lopez-Lira, and Jimin
Huang. 2023. Pixiu: a large language model, in-
struction data and evaluation benchmark for finance.
InProceedings of the 37th International Conference
on Neural Information Processing Systems, pages
33469–33484.
Yuanjian Xu, Jianing Hao, Kunsheng Tang, Jingnan
Chen, Anxian Liu, Peng Liu, and Guang Zhang. 2025.
FinRipple: Aligning large language models with fi-
nancial market for event ripple effect awareness. In
Findings of the Association for Computational Lin-
guistics: ACL 2025.
Yangyang Yu, Zhiyuan Yao, Haohang Li, Zhiyang Deng,
Yuechen Jiang, Yupeng Cao, Zhi Chen, Jordan W. Su-
chow, Zhenyu Cui, Rong Liu, Zhaozhuo Xu, Denghui
Zhang, Koduvayur Subbalakshmi, Guojun Xiong,
Yueru He, Jimin Huang, Dong Li, and Qianqian Xie.
2024. Fincon: A synthesized llm multi-agent system
with conceptual verbal reinforcement for enhanced
financial decision making.Advances in Neural Infor-
mation Processing Systems, 37:137010–137045.
Wentao Zhang, Lingxuan Zhao, Haochong Xia, Shuo
Sun, Jiaze Sun, Molei Qin, Xinyi Li, Yuqing Zhao,
Yilei Zhao, Xinyu Cai, Longtao Zheng, Xinrun Wang,
and Bo An. 2024. A multimodal foundation agent for
financial trading: Tool-augmented, diversified, and
generalist. InProceedings of the 30th acm sigkdd
conference on knowledge discovery and data mining,
pages 4314–4325.
Wenyi Zhang, Renjun Jia, Yanhao Wang, Dawei Cheng,
Minghao Zhao, and Cen Chen. 2025a. Enhancing
portfolio optimization via heuristic-guided inverse
reinforcement learning with multi-objective reward
and graph-based policy learning. InProceedings of
the 34th International Joint Conference on Artificial
Intelligence, IJCAI 2025, pages 9483–9491. Interna-
tional Joint Conferences on Artificial Intelligence.
Zhihan Zhang, Yixin Cao, and Lizi Liao. 2025b. Xfin-
bench: Benchmarking llms in complex financial prob-
lem solving and reasoning. InFindings of the Asso-
ciation for Computational Linguistics: ACL 2025,
pages 8715–8758.
11

Appendix Contents
A Additional Related Work 13
A.1 Financial LLM Benchmarks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
A.2 LLMs in Financial Decision-Making . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
A.3 Portfolio Risk Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
B Dataset and Market Context 13
B.1 Price Trajectories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
B.2 Data Preprocessing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
B.3 Correlation Structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
C Evaluation Protocol 15
C.1 QA Task Templates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
C.2 Pipeline Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
C.3 Stress Windows and Profiles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
C.4 Baselines and Common Portfolio Replay . . . . . . . . . . . . . . . . . . . . . . . . . . 20
C.5 Statistical Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
D QA Dataset and Results 20
D.1 Dataset Statistics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
D.2 Full QA Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
D.3 T3/T4 Numeric and Structured Decisions . . . . . . . . . . . . . . . . . . . . . . . . . 21
D.4 Task Diagnostics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
D.5 QA and Portfolio Outcomes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
E Financial Outcomes 23
E.1 Stress-Gate Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
E.2 Cross-Period Performance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
E.3 NA V Trajectories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
F Pipeline Diagnostics 24
F.1 Stage-Reference Agreement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
F.2 Lookback and Ex-Post References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
F.3 Allocation Agreement and Exposure Compliance . . . . . . . . . . . . . . . . . . . . . 26
F.4 Allocation and Turnover . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
F.5 Allocation Changes by Profile . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
F.6 CEPS Parameter Sensitivity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
F.7 Stage Scores and Financial Associations . . . . . . . . . . . . . . . . . . . . . . . . . . 27
F.8 Paired Stage Interventions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
F.9 Within-Class Correlation Risk . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
G Real-Time Evaluation 32
H Qualitative Examples 34
H.1 Market Snapshot Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
H.2 QA Dataset Samples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
H.3 Pipeline Evaluation Traces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
12

A Additional Related Work
A.1 Financial LLM Benchmarks
Financial LLM benchmarks span knowledge re-
trieval, numerical reasoning, and quantitative
tasks (Chen et al., 2021, 2022; Shah et al., 2022;
Islam et al., 2023; Xie et al., 2023; Tang et al.,
2025; Liu et al., 2025; Xie et al., 2024; Zhang et al.,
2025b; Luo et al., 2025a; Gan et al., 2025). Most
QA benchmarks stop before allocation under re-
alized markets. Dynamic evaluations commonly
restrict the asset universe to equities or cryptocur-
rencies (Liu et al., 2022; Xie et al., 2024; Li et al.,
2024; Chen et al., 2025a; Oh et al., 2025), or score
products independently instead of a joint portfo-
lio (Li et al., 2025b). StockBench (Chen et al.,
2025a) evaluates multiple trading steps for 20 DJIA
equities, but omits cross-asset allocation and in-
vestor profiles. Table 3 compares PORTBENCHon
financial QA, joint multi-asset allocation, linked
decisions, realized risk, and investor constraints.
A.2 LLMs in Financial Decision-Making
LLM agents now support market analysis, signal
generation, and portfolio construction (Zhang et al.,
2024; Xiao et al., 2025; Qian et al., 2026; Li et al.,
2026b; Saha et al., 2025). FinCon (Yu et al., 2024)
uses a manager–analyst hierarchy, MASS (Guo
et al., 2025a) scales multi-agent portfolio simula-
tion, HedgeAgents (Li et al., 2025d) assigns hedg-
ing specialists across asset classes, and a cryptocur-
rency framework (Luo et al., 2025b) coordinates
agents over the top-30 cryptocurrencies. These sys-
tems are evaluated in separate backtesting settings.
PORTBENCHsupplies one six-class market inter-
face and scores each stage of a shared five-stage
process, enabling stage-level comparison alongside
portfolio outcomes.
A.3 Portfolio Risk Evaluation
Portfolio theory makes covariance central to allo-
cation: modern portfolio theory (Markowitz, 1952)
and risk parity (Qian, 2005) optimize portfolio-
level variance or risk contributions. Data-driven
methods also use cross-asset co-movement and
temporal structure (Mantegna, 1999; Wang et al.,
2021; Jeon et al., 2024); SmartFolio (Zhang et al.,
2025a), for example, penalizes positive intra-class
correlation and rewards inter-class hedging. Risk-
first evaluation further shows why average returns
alone miss failures under market stress (Chen et al.,
2025b,c). PORTBENCHaddresses both require-
ments with correlation-aware allocation scoring,
three stress windows, and three investor profiles.
B Dataset and Market Context
PORTBENCHcovers 183 market series spanning
2015–2025 across six asset classes, collected
from Yahoo Finance (price/return series), FRED
(macroeconomic indicators), and Kaggle (supple-
mentary equity and cryptocurrency series). Fig-
ure 7 shows instrument counts by asset class. Eq-
uities exhibit the broadest coverage (126 series),
including individual stocks, broad-market, sector,
and factor ETFs, and index context. Commodities
(16 tickers) and bonds (15 series) provide repre-
sentative cross-class hedging opportunities, cryp-
tocurrency (12 tickers) captures major and mid-cap
digital assets, and real estate (10 series) and cash
equivalents (4 series) extend the market coverage.
Figure 7: Number of unique instruments or series per
asset class in PORTBENCH.
Code and source data.The benchmark imple-
mentation is licensed under Apache 2.0. Market
data are obtained from the providers listed above,
with reuse subject to the respective source terms.
Historical allocation results use the evaluation sub-
set defined in Appendix C.4.
Market context at decision time.At each deci-
sion date, the model receives a point-in-time market
context containing a 60-trading-day lookback win-
dow of price history and daily returns for all assets
in scope; macro indicators (Fed funds rate, VIX,
yield curve slope); an intra-class correlation matrix
for each asset class and an inter-class correlation
matrix, both recomputed from the lookback win-
dow at each decision date; any available news text
or earnings filings preceding the decision date; the
current portfolio weights; and the current portfolio
NA V . The intra- and inter-class correlation matri-
13

Benchmark Multi-Asset Fin. QA Alloc. Quality Seq. Process Risk/Stress Profile Align.
FinQA (Chen et al., 2021)✓
ConvFinQA (Chen et al., 2022)✓
PIXIU (Xie et al., 2023)✓
FinanceBench (Islam et al., 2023)✓
CryptoTrade (Li et al., 2024)◦ ◦✓
FinBen (Xie et al., 2024)◦✓◦ ◦ ◦
FinEval (Guo et al., 2025b)✓◦ ◦
XFinBench (Zhang et al., 2025b)✓◦
InvestorBench (Li et al., 2025b)◦ ◦ ◦✓◦
FinanceReasoning (Tang et al., 2025)✓
FinDABench (Liu et al., 2025)◦
StockBench (Chen et al., 2025a)◦ ◦✓ ✓
PORTBENCH(Ours)✓ ✓ ✓ ✓ ✓ ✓
Table 3: Comparison of representative financial LLM benchmarks. Multi-Asset covers joint allocation across asset
classes; Fin. QA tests financial knowledge or reasoning; Alloc. Quality scores portfolio weights or their outcomes;
Seq. Process evaluates multiple linked decisions; Risk/Stress evaluates realized risk or stress periods; Profile Align.
conditions decisions on investor constraints. ✓ denotes an explicit evaluation dimension, ◦ denotes a restricted
setting or indirect measure, and a blank denotes no reported evaluation.
ces are formatted as structured tables and injected
directly into the S1 and S3 prompts, giving mod-
els explicit access to the correlation information
required for correlation-aware allocation. The cor-
relation interface is restricted to the asset classes
present in each snapshot.
B.1 Price Trajectories
Figure 8 displays representative market series from
the six asset classes over 2015–2025. Coverage
ranges from 126 equity instruments to four cash-
related series. Within-class paths also differ: nat-
ural gas and crude oil fluctuate more sharply than
gold, while BTC, SOL, BNB, DOT, and A V AX fol-
low distinct cryptocurrency cycles and listing histo-
ries. These series differ in history length, volatility,
and drawdown patterns.The dataset combines
long-history traditional assets with later-listed
cryptocurrencies, so history lengths differ across
assets in the dataset.
B.2 Data Preprocessing
Calendar alignment.All price and return series
are aligned to a common business-day calendar.
For realized portfolio accounting, short price gaps
of up to five consecutive trading days are forward-
filled before computing returns; daily returns are
not carried forward. Gaps exceeding five days are
retained as missing values and excluded from cor-
relation estimation using pairwise complete obser-
vations, so that assets with non-overlapping listing
histories (particularly cryptocurrency) do not re-
duce the effective sample for other asset pairs.
Market regime labeling.Each asset class is as-
signed one of four market regime labels, bull, bear,
sideways, or crisis, on a rolling basis. A crisis win-
dow begins when the maximum drawdown from
the trailing 252-trading-day peak exceeds 15%.
Bull and bear periods are identified using a dual
moving-average crossover rule (50-day and 200-
day); periods where neither condition is satisfied
are labeled sideways. Regime labels group QA
samples and evaluation results by market regime.
Data splits.The dataset is divided into three non-
overlapping splits with year-end boundaries:
• Train: 2015–2022 (eight years; used for cor-
relation matrix estimation and QA generation)
• Validation: 2023 (one year; used for hyperpa-
rameter selection and QA validation)
• Test: 2024–2025 (two years; held out for re-
ported QA evaluation)
Pipeline evaluation uses calendar windows that sit
inside this coverage but serve a different role: the
primary normal-period backtest is the 2024 bull
window, with 2015–16, 2020, and 2022 reserved
for stress-gate and cross-period Sharpe compar-
isons (Section 3). These pipeline windows are
therefore evaluation regimes, not a redefinition of
the QA train/val/test split.
Correlation matrix estimation.Figures 9
and 10 use a dataset-level Pearson matrix com-
puted from 2015–2022 daily returns with pairwise
14

(a) Equities (representative)
 (b) Bonds (representative)
(c) Commodities (representative)
 (d) Cryptocurrency (representative)
(e) Real Estate (representative)
 (f) Cash-related macro series (representative)
Figure 8: Representative market-series trajectories from each asset class. Price series are indexed to 100 at their first
available observation; the cryptocurrency panel uses a logarithmic index axis. Interest-rate series retain percentage
units on secondary axes.
complete observations. Each pipeline episode re-
computes its correlation matrix from the trailing
60 trading days available at the decision date. The
profile-constrained S3 reference, CovRiskPar, Min-
Var, and Black–Litterman use covariance estimated
from the same decision-time snapshot; covariance-
based baselines apply 252-day annualization. Pear-
son correlation maps directly to the intra- and inter-
class scoring formulas in Appendix C.2.
B.3 Correlation Structure
Figures 9 and 10 show low average correlation
for several cross-class pairs and stronger positive
correlation within equities and real estate.Diversi-
fication depends on which asset classes receive
weight: spreading capital inside a highly corre-
lated class provides less hedging than allocating
across weakly correlated classes.
C Evaluation Protocol
C.1 QA Task Templates
QA targets are generated automatically from the
market base dataset and explicit task definitions,
without manual item-level annotation. They in-
clude realized outcomes (T1), numerical calcula-
tions and decision rules (T2–T6), and a predefined
regime-to-allocation policy (T7).
15

Figure 9: Pairwise Pearson correlation matrix across all six asset classes, computed from daily returns over the full
training period (2015–2022). Rows and columns are ordered by asset class.
Figure 10: Mean pairwise return correlations within and across asset classes. Left: the class-level correlation matrix,
with diagonal entries denoting within-class means. Right: mean within-class correlation for each asset class.
16

QA results report mean task scores in [0,1] . T1
uses exact direction-label agreement. T2/T3 use
max(0,1−|ˆy−y|/|y|)for nonzero numeric targets;
a zero target receives one only when |ˆy|<10 −6.
T4/T5 use cosine similarity between predicted and
target weight vectors. T6/T7 use the component
scores defined below. Missing or unparseable an-
swers receive zero, and the overall QA score aver-
ages the seven template means equally.
T1 (Return direction).The ground truth is the
sign of the realized h-day forward return, where
h is the forecast horizon specified in the question
(default h=21 trading days). Direction labels are
positive, negative, or flat (within±1%).
T2 (VaR estimation).Historical simulation VaR
at confidence level p (e.g., p=0.95 or 0.99; distinct
from the S3 mixing weightα):
VaRp =quantile(r 1:L,1−p)
where r1:L is the trailing lookback return series
provided in the question (default L=60 trading
days). The scored answer is VaRp; the question
specifies the requested confidence level.
T3 (Position sizing).The fixed-fractional Kelly-
inspired formula (Kelly, 1956):
f ∗ = min

1.0, δmax
|VaR99%|

whereδ max is the question’s drawdown limit.
T4 (Long-only minimum-variance pairwise al-
location).The prompt includes individual daily
volatilities ς1, ς2 (distinct from pipeline stage
scores σt), annualized mean returns µ1, µ2, and
a minimum annualized portfolio return µmin. The
fullcondition also provides the pairwise daily co-
variance and correlation; therestrictedcondition
in Section D.4 removes these two statistics. The
target minimizes two-asset variance subject to the
stated return floor:
min
w1,w2
w2 1ς 2 1 +w 2 2ς 2 2 + 2w1w2ς12
s.t.w 1 +w 2 = 1, w 1, w2 ≥0,
w1µ1 +w 2µ2 ≥µ min,
where ς12 is the lookback sample covariance. With-
out a binding return floor, the long-only minimum-
variance target is w1 = clip((ς 2 2 −ς 12)/(ς 2 1 +ς 2 2 −
2ς12),0,1) and w2 = 1−w 1; a vanishing denom-
inator uses equal weights. When the floor binds,
the weights satisfy w1µ1 +w 2µ2 =µ min, giving
w1 = (µmin −µ 2)/(µ1 −µ 2)andw 2 = 1−w 1.
T5 (Maximum-Sharpe allocation).The long-only
maximum-Sharpe portfolio for three or more assets,
solved numerically via constrained optimization:
max
w
w⊤µ−r f√
w⊤Σw s.t. P i wi = 1, wi ≥0
with a risk-free rate of rf = 4% per annum and
annualized µ, Σ estimated from the 60-day look-
back window. The pipeline S3 reference in Ap-
pendix C.2 uses the raw sample mean and covari-
ance without rf . Equal weight is used as a fallback
if the optimizer does not converge. Under thefull
condition the prompt includes the full mean vector
µ and covariance matrix Σ; under therestricted
condition the covariance matrix and its header row
are stripped (see Section D.4).
T6 (Rebalancing decision with trade specifica-
tion).The model is presented with a holdings
table of current weights and target weights; pre-
computed deviations are withheld. The ground
truth is determined as follows. Let i∗ =
arg maxi |wcurrent i −w target i | be the most off-target
asset. The rebalancing flag is:
rebalance=1

|wcurrent i∗ −w target i∗ |> δreb  ,
with default threshold δreb = 0.05 (distinct from
the profile drawdown tolerance δdd). Classes are
balanced by construction, with half of all instances
requiring rebalancing and half not, yielding exactly
50% positive / 50% negative labels.
The answer has two parts.Part A: a yes/no re-
balancing decision.Part B(required when Part A
is yes): the corrective trade, expressed as “sell
X.XXXXofASSET” or “buyX.XXXXofAS-
SET”, where ASSET =i ∗ and the trade size is
|wcurrent i∗ −w target i∗ |(reported but not scored).
Scoring decomposes as follows. If the ground
truth isno: score = 1 if the model answers no,
else 0. If the ground truth isyes: score = 0.40×
dyes + 0.60×(0.50×c dir + 0.50×c asset), where
dyes =1[model answers yes] , cdir indicates correct
trade direction (buy versus sell), andcasset indicates
correct asset identification.
T7 (Regime detection and allocation).The target
regime is the label assigned to the decision date
by the regime classifier. The allocation target uses
a predefined mapping from each regime to an in-
crease, decrease, or hold direction for each asset
class. This mapping specifies the benchmark’s ref-
erence policy:
17

RegimeEQ BO CO RE CR CA
Bull↑ ↓ ∼ ↑ ↑ ↓
Bear↓ ↑ ∼ ↓ ↓ ↑
Sideways∼ ∼ ∼ ∼ ↓ ↑
Crisis↓ ↑ ↑ ↓ ↓ ↑
EQ = equities, BO = bonds, CO = commodities,
RE = real estate, CR = cryptocurrency, CA = cash.
↑ = increase, ↓ = decrease, ∼ = hold. Scoring is
score= 0.5d reg + 0.5 1 |C| P c∈C 1[ˆac =a ∗ c], where
dreg =1[ \regime=regime ∗], C is the set of six as-
set classes, and ˆac, a∗ c are the predicted and ground-
truth allocation directions for classc.
C.2 Pipeline Metrics
Stage scores and CEPS.Each stage has an ex-
plicit target. S1/S2 use trailing-return rules, S3
uses a profile-constrained numerical allocation and
class exposure, and S4/S5 measure turnover and
lookback risk-state agreement. For σ∈[0,1] 5, the
Cross-Stage Error Propagation Score is
¯σ= 1 5
5X
t=1
σt,(1)
∆cascade =
4X
t=1
max(σt −σ t+1,0),(2)
CEPS = clip(¯σ−.1∆cascade,0,1).(3)
CEPS combines the mean reference-based stage
score with a penalty for downstream score drops.
The five stage scores receive equal weight in the
mean. Paired interventions measure downstream re-
sponses to a reference replacement (Appendix F.8).
S1: market interpretation.For eligible asset i,
let Rlb i be its cumulative return over the last 60
available observations within the preceding 90 cal-
endar days, through the decision date. The refer-
ence view and agreement score are
v∗ i = clip(Rlb i /.10,−1,1),(4)
σ1 = 1− 1 2n nX i=1 |ˆvi −v ∗ i |.(5)
Here ˆvi ∈[−1,1] is the model view and n is the
eligible security count; an absent view is neutral.
The target specifies a reproducible momentum in-
terpretation of the lookback data.
S2: signal generation.The reference maps v∗ i >
.2 to buy, v∗ i <−.2 to sell, and the remaining
values to hold. For model signalsˆsi, agreement is
σ2 = 1 n nX i=1 1[ˆsi =s ∗ i ].(6)
Missing signals receive no agreement credit.
Profile-constrained lookback reference.Let B
contain reference-buy assets, D the eligible bond
and cash securities, and E equity and cryptocur-
rency assets. For profile p, the reference numeri-
cally maximizes
w⊤µ√
w⊤Σw+ϵ
s.t.
X
i
wi = 1, w i ≥0,
wi = 0 (i /∈ B ∪ D), X
i∈E
wi ≤α p,
X
i∈D
wi ≥β p.
(7)
The sample mean µ and covariance Σ use com-
mon observed dates in the trailing window, with
no risk-free adjustment; ϵ= 10 −10 stabilizes the
denominator. SLSQP starts from a feasible alloca-
tion, with tolerance 10−9 and at most 500 iterations.
A solution is accepted only if the solver succeeds,
satisfies the constraints, and matches or improves
the initial objective; otherwise the feasible start is
retained. Defensive securities remain eligible re-
gardless of signal to implement the profile floor.
Real estate follows its separate asset class and is
not included in the equity cap.
We denote the resulting numerical reference by
w∗ p. It gives all models a common allocation target
for each date and profile, using only past returns.
The objective evaluates return relative to volatility
within the lookback sample; subsequent net returns,
drawdown, and the stress gate assess investment
outcomes. Historical stage scores use this look-
back reference. Appendix F.2 compares it with
an ex-post reference constructed from subsequent
realized returns.
S3: allocation agreement and class exposure.
For normalized long-only portfolios, including any
uninvested cash, reference similarity is
sacc = 1− 1 2 X
i
|wi −w ∗ p,i|.(8)
It equals one for identical allocations and zero for
disjoint allocations. S3 combines this term and
class exposure with equal weight. Let Wc be to-
tal exposure to class c, ¯ρc the mean within-class
off-diagonal correlation, and ρ(c, c′) the mean cor-
18

relation between its eligible security pairs:
sintra = clip

1−
X
c
Wc max(¯ρc,0),0,1
!
,
(9)
¯ρcross =
P
c̸=c′ WcWc′ρ(c, c′)P
c̸=c′ WcWc′
,(10)
sinter = clip((1−¯ρcross)/2,0,1),(11)
scorr = 1 2 (sintra +s inter).(12)
With no positive cross-class weight product,
sinter =.5 . Uninvested cash contributes to cash-
class exposure; class correlations use the eligible
securities. These scores describe the class alloca-
tion. Redistributing weights inside a class leaves
them unchanged, and with exactly two positive
classes the cross-class weight product cancels.
Asset-level correlation risk.Portfolio variance
V(w) =w ⊤Σw and the weighted pairwise cor-
relation in Appendix F.9 use the actual security
weights. The matched within-class allocation pro-
vides a controlled test: selected securities and class
totals are identical, while covariance exposure can
change. The class score describes how capital is
split across asset classes; these asset-level measures
assess the risk associated with the weights within
each class.
S4: turnover agreement.Let τ(u,w) =P
i̸=cash |wi −u i| be traded security weight from
pre-trade weights u. Both the proposed and refer-
ence targets are compared from the same pre-trade
state. Withτ=τ(u,w)andτ ∗ =τ(u,w ∗ p),
σ4 = 1− |τ−τ ∗| max(τ, τ∗,10 −4) .(13)
Agreement peaks at matching turnover. Trading
costs are reported separately as a financial outcome.
S5: lookback risk-state agreement.Apply the
target weights to common lookback returns and
compute the 5th-percentile daily VaR and maxi-
mum drawdown, including initial wealth in the
running peak. The rebalance flag is true when
drawdown breaches the profile tolerance or the
maximum deviation from security equal weight-
ing exceeds .05. For model and reference flags
Window Start End Decisions
China shock 2015-08-01 2016-02-29 30
COVID crash 2020-02-01 2020-05-31 17
2022 decline 2022-05-01 2022-12-31 35
2024 normal 2024-01-01 2024-12-31 11
Table 4: Evaluation windows and saved decisions per
model–profile pair. Stress decisions are weekly; normal
decisions are monthly, February–December.
Profileα p βp δp VaR limit
Conservative .40 .40 .10−.010
Balanced .65 .20 .20−.020
Aggressive .90 .05 .35−.040
Table 5: Profile parameters: equity-plus-crypto cap αp,
bond-plus-cash floor βp, and drawdown tolerance δp.
Uninvested cash counts toward the defensive floor.
b, b∗ and risk statistics,
eV = |V−V ∗| max(|V ∗|,10 −6) ,(14)
eD = |D−D ∗| max(|D∗|,10 −6) ,(15)
σ5 = 1 2 1[b=b ∗] + 1 2 clip  1− eV +eD 2 ,0,1  .
(16)
Here V denotes VaR andD drawdown in this equa-
tion. Smaller and larger risk statistics both reduce
reference agreement; realized volatility, drawdown,
and the stress gate independently assess portfolio
risk. The profile VaR threshold is available for risk
alerts and does not set the rebalance flag.
C.3 Stress Windows and Profiles
The weekly stress schedule resolves changes dur-
ing rapidly evolving market conditions; monthly
normal-period evaluation measures longer hold-
ing intervals. All comparison strategies, including
EqW, share the schedule within each window, so
their relative performance is compared at the same
decision frequency. All three stress windows use
weekly decisions, so the 2020–2022 reversal is
observed at the same decision frequency. Compar-
isons with monthly decisions in 2024 also reflect
a change in decision frequency. The stress gate
passes when realized maximum drawdown magni-
tude is at mostδ p in every stress window.
Profiles appear in the S1/S2 prompts; S3 uses the
resulting signals and market statistics. Exposure
compliance evaluates both target-weight inequali-
ties in Table 5.
19

C.4 Baselines and Common Portfolio Replay
Tradable securities.The benchmark comprises
183 market series spanning six asset classes, sup-
porting portfolio QA, macroeconomic and news
context, and broad market coverage. Portfolio eval-
uation supplies 99 series with matched price his-
tories: 43 equities, 15 bonds, 16 commodities, 10
real-estate assets, 10 cryptocurrencies, 4 cash in-
struments, and VIX. VIX is a market indicator,
and any weight assigned to it is held as uninvested
cash. The other 98 series are the investable assets.
The remaining 84 corpus series (82 equities and 2
cryptocurrencies) are excluded from portfolio allo-
cation. At each decision date, an investable asset
is eligible when its price is positive and at least
20 return observations are available over the pre-
ceding 90 calendar days. Weight assigned to an
ineligible asset is held as uninvested cash and is
not redistributed. All compared portfolios use this
eligibility rule.
Execution and return accounting.Every port-
folio starts with unit NA V in cash and replays its
archived target sequence. A decision is executed
at the first observed market close strictly after its
date. Existing positions accrue that date’s return
before trading, and new positions earn subsequent
returns. The calendar uses observed SPY trading
dates. Outcomes use archived adjusted prices: Ya-
hoo series for ETFs and the adjusted-close column
of the NASDAQ-100 source for individual equi-
ties. Short price gaps are forward-filled for at most
five trading dates before computing returns. Each
dated return is applied once. Commission of 5 bps
and slippage of 10 bps are charged on the abso-
lute changes in security weights; transferring the
cash balance has no additional fee. Holdings drift
between trades. Costs are relative to initial NA V .
Sharpe uses (252¯r−.04)/(
√
252sr) from the
net daily portfolio returns, with a fixed 4% an-
nual risk-free rate across windows. V olatility is√
252sr, total return is terminal NA V minus one,
and maximum drawdown includes initial NA V in
the running maximum. Each window contains all
ten models and three profiles. The 2,790 saved de-
cisions remain in coverage and allocation records;
60 terminal decisions have no following execution
close inside their windows, leaving 2,730 executed
decisions for stage-score summaries. All 120 port-
folio cells remain in financial comparisons. The
330 normal-period decisions all execute. For Min-
Var in 2024, the risk-free adjustment contributes
−3.13 to Sharpe at 1.28% annualized volatility;
cumulative trading costs are 0.76% of initial NA V .
Classical strategies.EqW distributes capital
across the eligible securities. The 60/40 baseline
equally weights eligible equities within its 60%
sleeve and eligible bonds within its 40% sleeve.
RiskPar uses inverse volatility; CovRiskPar uses
full-covariance equal risk contribution; MinVar
uses long-only minimum variance; BL combines
a return prior and directional views. Covariance-
based strategies use the common observed trail-
ing returns with 252-day annualization. These six
strategies retain their standard allocation rules, pro-
viding fixed strategy comparators across investor
profiles.
C.5 Statistical Analysis
Per-template QA means retain all 50 evaluated
items for each model. The seven-template QA ag-
gregate weights each template equally. QA–Sharpe
correlations use ten paired model observations sep-
arately for each period and profile. CEPS–outcome
associations likewise compare models within each
profile. Percentile intervals use 10,000 paired
model-bootstrap draws. For the covariance com-
parisons, the model is the resampling cluster, re-
taining its profiles and dates together. The seed
is 20261006. Intervals describe these evaluated
model sets and are not adjusted for multiple com-
parisons. The 65/120 beat rate describes the fixed
evaluation grid; its cells share models and market
windows. Allocation and profile-change intervals
resample models with their dates and profiles re-
tained. Table 14 applies Benjamini–Hochberg cor-
rection to its three Spearman association tests.
D QA Dataset and Results
D.1 Dataset Statistics
The QA dataset contains 6,269 pairs across seven
templates (Figure 12): T1–T5 each have 1,000 sam-
ples, while T6 and T7 have 778 and 491. T7 has
no training split because its adaptive allocation la-
bels are reserved for validation and testing. T6 has
balanced labels: 50/50 rebalance versus hold.
Figure 11 shows the regime composition. Side-
ways markets dominate every template ( >65%),
matching the empirical prevalence of range-bound
periods. T1–T5 share nearly identical regime pro-
portions because they sample from the same date
pool; T7 raises the bull-market share to 29% so that
20

its adaptive allocation task has adequate coverage
of non-sideways regimes.
The amount of textual context increases with
template complexity (Figure 13). L1 templates
(T1–T3) include news or SEC filings in 71–75%
of samples at roughly 2,800–3,000 characters; L2
(T4) is intermediate; and L3–L4 (T5–T7) reach
100% coverage at 4,500–7,388 characters. T7 pro-
vides the longest contexts (7,388 chars), combining
news and macro signals for regime-aware alloca-
tion. Overall, 85.3% of pairs carry textual context,
with a mean length of 3,997 characters.Context
coverage and length rise with complexity: par-
tial coverage in T1–T3, complete in T5–T7.
Figure 11: QA counts by template and market regime.
Figure 12: QA sample counts by template and data split.
D.2 Full QA Results
Table 6 reports QA results: per-template mean
scores with full information (T1–T7), the restricted
condition without the covariance matrix (T4r, T5r),
formula-focused allocation versus broader-task
averages (F = mean of T4+T5; B = mean of
T1+T2+T6+T7; T3 excluded as eight of ten models
exceed 0.94), and mean scores by market regime.
The overall QA score ranges from .511 to .819.
The widest template spreads occur on T3 (.336–
.968), T5 (.230–.992), and T7 (.320–.843), while
T4 remains near ceiling for every model.Aggre-
gate QA rankings therefore combine tasks that
Figure 13: Text richness by template: news or filing
coverage (bars, left axis), mean context length (dashed
line, right axis), and global averages (inset).
differ substantially in both difficulty and the size
of score differences between models.
We also recompute the QA average without
T3 and T4. The resulting ranking has Spearman
ρ=.988 with the seven-template ranking, and no
model moves by more than one place.
D.3 T3/T4 Numeric and Structured Decisions
Table 6 shows near-ceiling numeric scores: eight
of ten models exceed 0.94 on T3 and every model
scores at least 0.956 on T4. Both templates provide
quantitative inputs for sizing or pairwise allocation.
We further evaluate four models on a separate
set of 50 T3 and 50 T4 structured-decision items
per model. Each output gives a plan, feasible set,
and binding constraints. Field score averages cor-
rectness across these fields; exact match requires
all fields to be correct. Table 7 shows high field
accuracy for DB-2.0-Pro and the two DS-V4 mod-
els, with lower exact-match rates. HY3-Preview
produces valid JSON for all 100 items but no exact
matches; 39 T3 and 44 T4 outputs receive partial
credit. Its errors span constraint propagation, arith-
metic, table reading, and multi-field consistency.
For DB-2.0-Pro and the two DS-V4 models,
mean field/exact scores are .947/.787 on T3 and
.959/.820 on T4. Their 95% CIs are [.924,
.968]/[.707, .860] and [.938, .976]/[.747, .880], re-
spectively, from 10,000 item-bootstrap samples re-
taining all three outputs per sampled item.The
supplementary tasks distinguish component ac-
curacy from complete consistency across the se-
lected plan, feasible set, and binding constraints.
D.4 Task Diagnostics
Information ablation.T4 and T5 prompts ex-
pose the statistics used by their allocation formulas:
21

Per-Template (Full) Restricted Task Type Market Regime
Model T1 T2 T3 T4 T5 T6 T7 Mean T4 r T5r F B Bull Bear Side.
DS-V4-Flash .520.843 .945 1.00.932 .652 .843 .819.975 .860 .966 .715 .827 .823 .812
Qwen3.7-Max .500 .859.951 1.00.954 .724 .742 .819 1.00 .990.977 .706 .814 .863.810
DS-V4-Pro .520.837 .963 1.00 .992.652 .760 .818 1.00.660 .996.692 .844.846 .802
DB-2.0-Lite .460 .798 .957 .956 .897 .810 .747 .804 .961 .940 .927 .704 .780 .846 .806
DB-2.0-Pro .440 .847 .963 .991 .912 .824 .530 .787 .979 .923 .952 .660 .764 .806 .792
Qwen3.6-Plus .440 .858 .968 1.00.804 .640 .768 .783 1.00.810 .902 .677 .799 .801 .771
GLM-5.1 .440 .855 .964 1.00.421 .882.738 .757 1.00.531 .711 .729.778 .765 .746
Qwen3.6-35B-A3B .460 .808 .961 1.00.230 .564 .763 .684 1.00.320 .615 .649 .714 .729 .662
HY3-Preview .460 .386 .336 .975 .958 .468 .783 .624 .982 .974 .967 .524 .664 .663 .597
Kimi-K2.6 .420 .422 .493 .956 .280 .684 .320 .511 .978 .710 .618 .462 .556 .531 .487
Table 6: Complete QA evaluation results. Per-template mean scores under the full information condition (T1–T7),
restricted condition without the covariance matrix (T4r, T5r), formula-focused allocation and broader-task averages
(F, B), and mean scores by market regime. Models are ranked by mean score. Green = column best; pink rows =
bottom two models with lower mean scores (Mean<0.65).
T3 T4
Model Field Exact Field Exact
DB-2.0-Pro .956 .820 .965 .840
DS-V4-Pro .953 .800 .989 .940
DS-V4-Flash .931 .740 .922 .680
HY3-Preview .238 .000 .350 .000
Table 7: Supplementary T3/T4 structured-decision re-
sults on separate items. Field score averages correctness
across the selected plan, feasible set, and binding con-
straints; exact match requires all fields to be correct.
Main QA results use the original tasks in Table 6.
T4 includes pairwise covariance and correlation,
and T5 includes the mean vector and covariance
matrix. The restricted prompts remove covariance
and correlation from T4 and the covariance matrix
and its header from T5, retaining the T5 mean vec-
tor. The difference ∆ =score full −score restricted
measures the change in mean task score when co-
variance information is supplied. Results: Table 6.
On T5, only the two DS-V4 models have ∆>
0: DS-V4-Pro falls by 0.332 and DS-V4-Flash by
0.073 when the matrix is removed. The mean T5
score rises for the other eight models, from 0.006
for Qwen3.6-Plus to 0.430 for Kimi-K2.6; Kimi-
K2.6 rises from 0.280 to 0.710. T4 remains near
ceiling in both conditions, ranging from 0.956 to
1.000 with full information and from 0.961 to 1.000
without the covariance statistics. The T5 pattern
shows that the supplied matrix can hinder answer
generation, although the ablation cannot separate
table parsing from numerical reasoning.
Pairing the archived full and restricted responses
by model and item shows that 460/500 T4 scores
(92%) and 360/500 T5 scores (72%) are unchanged.
The aggregate ablation differences are therefore
concentrated in a subset of responses. These counts
retain every evaluated item, including zero scores.
Supplied-statistic allocation versus broader
tasks.We compare formula-focused allocation
tasks (T4: minimum-variance allocation; T5:
maximum-Sharpe optimization, both with covari-
ance statistics supplied) with the broader set of
return prediction, VaR estimation, rebalancing, and
regime detection tasks (T1, T2, T6, and T7). T3
is reported separately because eight of ten models
score above 0.94. The F and B columns of Table 6
report these descriptive averages for all models.
The mean T4–T5 score is 0.863, compared with
0.652 for T1–T2 and T6–T7. This 0.211 difference
favors T4–T5 for eight of ten models. GLM-5.1
and Qwen3.6-35B-A3B reverse the aggregate pat-
tern, with T6 scores of 0.882 and 0.564 versus T5
scores of 0.421 and 0.230. These averages reflect
different information and scoring conditions.
D.5 QA and Portfolio Outcomes
We relate the seven-template QA macro-average to
portfolio Sharpe across four market windows and
three investor profiles. The comparison uses 3,500
responses from ten models, seven templates, and
50 common items per template.
Each period–profile association contains ten
paired model observations. The same QA scores
recur across settings, so 120 portfolio cells are
not 120 independent QA observations. Table 8
reports Spearman correlations and percentile in-
tervals from 10,000 paired model-bootstrap draws.
Correlations range from −.67 to .83. QA scores
are positively associated with Sharpe in the con-
servative and balanced 2015–16 settings, whose
22

Window Profileρ[95% CI]
2015–16 Conservative0.83[0.40,1.00]
2015–16 Balanced0.71[0.10,0.96]
2015–16 Aggressive−0.67[−0.96,0.01]
2020 Conservative0.20[−0.61,0.79]
2020 Balanced−0.33[−0.90,0.52]
2020 Aggressive0.38[−0.45,0.90]
2022 Conservative0.12[−0.69,0.79]
2022 Balanced−0.59[−0.99,0.18]
2022 Aggressive0.36[−0.51,0.77]
2024 Conservative−0.10[−0.90,0.77]
2024 Balanced−0.08[−0.69,0.60]
2024 Aggressive−0.42[−0.89,0.37]
Table 8: QA–Sharpe associations across ten paired mod-
els per setting. QA uses the macro-average over all
seven templates. Intervals use 10,000 paired model-
bootstrap draws.
two unadjusted intervals exclude zero. The other
ten intervals include zero. In 2024, the estimates
are −.10, −.08, and −.42. The correlations vary
across periods and profiles. These descriptive com-
parisons motivate evaluating candidate systems on
portfolio outcomes under the intended profile and
decision schedule.
E Financial Outcomes
E.1 Stress-Gate Results
Table 9 reports maximum drawdown for every
model–profile pair in all three stress windows. Gate
passage uses the stated profile tolerance across all
windows. No model passes all three at the conser-
vative limit; nine pass at the balanced limit and all
ten at the aggressive limit.
Table 10 reports stage scores and drawdown for
GLM-5.1, Qwen3.6-Plus (Qwen3.7-Max for the ag-
gressive profile), HY3-Preview, and DS-V4-Flash.
E.2 Cross-Period Performance
Table 11 compares balanced-profile Sharpe with
EqW under the same universe, schedule, and cost
model in each window. Figure 4 includes all three
profiles. Appendix E.3 plots daily NA V trajectories.
E.3 NA V Trajectories
Figures 14–16 compare the three profiles in the
2024 normal window. Terminal model NA V ranges
from 1.033 to 1.150 for conservative portfolios,
1.095 to 1.150 for balanced portfolios, and 1.103 to
1.218 for aggressive portfolios. Figures 17 and 18
show the corresponding paths during the 2015 and
2020 stress windows. The trajectories show when
portfolios diverge, recover, or retain losses.
Figure 14: Normalized NA V in the 2024 normal window
under the conservative profile.
Figure 15: Normalized NA V in the 2024 normal window
under the balanced profile.
Figure 16: Normalized NA V in the 2024 normal window
under the aggressive profile.
2022 Market Decline.Figure 19 shows the accu-
mulation of losses during the 2022 window. Con-
servative model portfolios finish with NA V be-
tween .907 and .972, below their initial value of
one. No model–profile pair beats EqW on Sharpe
in this window. The dated event markers provide
context for the market path.
23

Profile Model 2015–16 DD% 2020 DD% 2022 DD% Gate
Conservative DS-V4-Flash -11.30 -10.53 -11.92×
DS-V4-Pro -7.51 -17.69 -13.32×
Qwen3.6-Plus -6.37 -11.16 -10.94×
Qwen3.7-Max -9.17 -6.28 -11.15×
Qwen3.6-35B-A3B -11.89 -15.32 -11.50×
GLM-5.1 -9.01 -10.93 -14.06×
DB-2.0-Lite -6.09 -11.18 -8.28×
DB-2.0-Pro -8.42 -13.38 -11.53×
HY3-Preview -8.48 -11.28 -14.04×
Kimi-K2.6 -11.32 -13.02 -14.63×
Balanced DS-V4-Flash -8.93 -22.19 -17.30×
DS-V4-Pro -8.65 -15.81 -14.13✓
Qwen3.6-Plus -8.38 -11.70 -12.71✓
Qwen3.7-Max -9.24 -10.66 -15.21✓
Qwen3.6-35B-A3B -9.51 -16.32 -13.87✓
GLM-5.1 -8.50 -12.99 -14.73✓
DB-2.0-Lite -8.45 -17.86 -14.14✓
DB-2.0-Pro -8.55 -15.46 -13.02✓
HY3-Preview -8.13 -14.60 -15.45✓
Kimi-K2.6 -10.52 -12.57 -12.90✓
Aggressive DS-V4-Flash -11.02 -14.39 -19.24✓
DS-V4-Pro -13.46 -16.47 -18.56✓
Qwen3.6-Plus -10.01 -14.42 -15.46✓
Qwen3.7-Max -17.80 -11.71 -16.19✓
Qwen3.6-35B-A3B -12.43 -13.77 -17.53✓
GLM-5.1 -11.95 -15.99 -15.33✓
DB-2.0-Lite -8.68 -16.68 -15.87✓
DB-2.0-Pro -11.01 -13.78 -13.54✓
HY3-Preview -8.12 -15.86 -16.13✓
Kimi-K2.6 -13.79 -12.57 -19.84✓
Table 9: Stress-window drawdowns and the joint drawdown gate for every model and profile.
Figure 17: Normalized NA V during the 2015 China
Shock under the conservative profile.
F Pipeline Diagnostics
F.1 Stage-Reference Agreement
Table 12 reports all five stage scores and CEPS for
each normal-period model–profile cell. S1/S2 com-
pare outputs with trailing-return rules; S3 measures
allocation similarity and class exposure; S4/S5
measure turnover and lookback risk-state agree-
ment. The exposure and outcome columns in Ta-
ble 13 assess the corresponding investment require-
ments directly.
Figure 18: Normalized NA V during the 2020 COVID
Crash under the balanced profile.
F.2 Lookback and Ex-Post References
Reference allocations depend on the return informa-
tion used to construct them. We therefore consider
two complementary references: a lookback alloca-
tion based on information available at the decision
date, and an ex-post allocation based on subsequent
realized returns. They provide a decision-time view
and a hindsight view of the same portfolio deci-
sions.
We compare them on the same 330 decisions in
24

Model Scenario S1 S2 S3 S4 S5 CEPS MaxDD% Pass
Conservative (10% MaxDD tolerance)
GLM-5.1 2015 China .790 .537 .318 .170 .501 .393−9.01✓
2020 COVID .713 .528 .337 .175 .420 .369−10.93 ×
2022 Decline .744 .529 .305 .143 .552 .390−14.06 ×
Qwen3.6-Plus 2015 China .783 .489 .334 .200 .381 .369−6.37✓
2020 COVID .709 .505 .338 .220 .385 .367−11.16 ×
2022 Decline .740 .512 .293 .215 .528 .395−10.94 ×
HY3-Preview 2015 China .766 .441 .348 .099 .144 .282−8.48✓
2020 COVID .712 .534 .361 .174 .276 .338−11.28 ×
2022 Decline .717 .430 .267 .115 .198 .273−14.04 ×
DS-V4-Flash 2015 China .783 .473 .338 .460 .337 .399−11.30 ×
2020 COVID .716 .386 .300 .376 .312 .350−10.53 ×
2022 Decline .737 .413 .257 .370 .363 .354−11.92 ×
Balanced (20% MaxDD tolerance)
GLM-5.1 2015 China .790 .544 .325 .197 .500 .403−8.50✓
2020 COVID .716 .527 .326 .192 .419 .370−12.99✓
2022 Decline .744 .529 .279 .143 .483 .369−14.73✓
Qwen3.6-Plus 2015 China .785 .526 .320 .193 .422 .381−8.38✓
2020 COVID .697 .464 .288 .261 .250 .326−11.70✓
2022 Decline .737 .498 .293 .224 .418 .370−12.71✓
HY3-Preview 2015 China .771 .446 .330 .131 .107 .277−8.13✓
2020 COVID .707 .486 .322 .173 .387 .346−14.60✓
2022 Decline .716 .402 .258 .130 .042 .234−15.45✓
DS-V4-Flash 2015 China .786 .400 .313 .285 .276 .333−8.93✓
2020 COVID .711 .425 .298 .368 .065 .291−22.19 ×
2022 Decline .737 .468 .247 .387 .285 .348−17.30✓
Aggressive (35% MaxDD tolerance)
GLM-5.1 2015 China .794 .574 .316 .207 .523 .416−11.95✓
2020 COVID .708 .535 .302 .279 .406 .387−15.99✓
2022 Decline .744 .530 .286 .202 .509 .393−15.33✓
Qwen3.7-Max 2015 China .789 .545 .323 .258 .482 .411−17.80✓
2020 COVID .723 .565 .335 .385 .417 .420−11.71✓
2022 Decline .747 .535 .314 .261 .454 .395−16.19✓
HY3-Preview 2015 China .774 .459 .309 .144 .393 .340−8.12✓
2020 COVID .694 .483 .297 .203 .098 .281−15.86✓
2022 Decline .715 .410 .251 .142 .133 .255−16.13✓
DS-V4-Flash 2015 China .772 .443 .292 .336 .102 .310−11.02✓
2020 COVID .682 .425 .270 .373 .125 .302−14.39✓
2022 Decline .742 .383 .235 .461 .071 .282−19.24✓
Table 10: Stress-window stage scores and drawdown for four models per profile. The gate table covers ten models.
the 2024 normal window, holding model outputs,
eligible assets, reference buy signals, and profile
constraints fixed. For the ex-post reference, the
mean and covariance in Eq. 7 use returns after the
decision date through the next decision date, or
year-end for the final decision. Both references use
the same optimization procedure. S3–S5 use the
corresponding reference weights; all other scoring
definitions, including the lookback risk sample for
S5, remain fixed.
GLM-5.1 ranks first under both references, and
the same three models occupy the top three places.
Across all ten models, the profile-averaged CEPS
rankings have Spearman ρ=.77 , with several
other positions changing. Mean S5 rises from
.108 to .283, mainly because the reference VaR
and drawdown estimates are closer to those of the
model portfolios on the unchanged lookback sam-
ple. Five of the 33 ex-post references retain the
feasible initial allocation under the optimization
rule in Appendix C.2; these cases account for about
half of the mean S5 increase. The two references
thus identify the same leading group while showing
how reference choice affects individual scores and
25

Figure 19: Normalized NA V during the 2022 Market Decline under the conservative profile, when no LLM beats
EqW. Vertical lines mark events during this period.
Model 2015–16 2020 2022 2024
EqW -1.047 -0.602 -0.540 0.710
DS-V4-Flash 0.290 -1.250 -1.451 0.609
DS-V4-Pro -0.452 -0.302 -1.460 0.542
Qwen3.6-Plus -0.034 1.696 -1.095 0.798
Qwen3.7-Max -0.214 0.099 -2.146 0.783
Qwen3.6-35B-A3B -0.564 0.078 -0.948 0.740
GLM-5.1 -0.217 -0.170 -0.924 0.603
DB-2.0-Lite -0.255 -0.705 -1.229 0.838
DB-2.0-Pro -0.681 0.062 -1.073 0.662
HY3-Preview -0.819 -0.725 -1.908 0.650
Kimi-K2.6 -0.790 0.239 -0.702 0.769
Table 11: Balanced-profile Sharpe across the four his-
torical windows. Stress windows use weekly decisions;
2024 uses monthly decisions.
ranks. The model portfolios’ realized returns and
risks are unchanged.
F.3 Allocation Agreement and Exposure
Compliance
Table 13 separates reference-weight similarity,
class-exposure score, target-exposure compliance,
and realized financial outcomes for all normal-
period cells. Exposure compliance checks both
profile inequalities at each decision.
F.4 Allocation and Turnover
The 330 normal allocations have mean total-
variation distance .306 from EqW and .890 from
the profile-constrained reference. The mean
decision-wise ratio of model to reference turnover
is .203, using the same pre-trade weights for both
targets. Reference allocations hold 8–14 securities
with maximum weights .24–.72. Model mean HHI
is .0207; its reciprocal is 48.3, while the mean of
the individual reciprocal HHIs is 55.9. EqW over
the eligible securities has HHI 1/n and n effective
holdings. Table 14 reports these allocation diagnos-
tics and their associations with realized outcomes.
F.5 Allocation Changes by Profile
Matching each model and decision date,
conservative-to-aggressive risk exposure increases
by .175 and bond-plus-cash exposure falls by .162;
distance from EqW increases by .070. Across the
ten model-level financial pairs, volatility rises by
.050 on average (nine positive changes), drawdown
magnitude by .047 (eight positive changes), and
Sharpe by .214 (nine positive changes). The mean
aggressive-minus-conservative Sharpe differences
are −.423 in 2015–16, +.935 in 2020, −.039 in
2022, and +.214 in 2024. Table 15 gives the paired
changes and model-cluster intervals. Risk-asset
exposure is the equity-plus-crypto weight used to
assess cap compliance; bond-plus-cash exposure
includes uninvested cash. The exposure response
coexists with period-dependent financial outcomes.
F.6 CEPS Parameter Sensitivity
We vary λ∈ {0, .05, .1, .2, .5}and α∈
{0, .25, .5, .75,1}, changing one parameter at a
time while holding the other at its default (λ=.1 ,
26

Profile Model S1 S2 S3 S4 S5 CEPS
Conservative
DS-V4-Flash 0.742 0.315 0.298 0.320 0.022 0.253
DS-V4-Pro 0.749 0.339 0.302 0.217 0.000 0.239
Qwen3.6-Plus 0.774 0.491 0.310 0.153 0.136 0.292
Qwen3.7-Max 0.746 0.385 0.291 0.151 0.000 0.232
Qwen3.6-35B-A3B 0.754 0.405 0.304 0.217 0.045 0.263
GLM-5.1 0.763 0.438 0.301 0.304 0.091 0.299
DB-2.0-Lite 0.751 0.339 0.299 0.143 0.000 0.223
DB-2.0-Pro 0.750 0.403 0.295 0.143 0.000 0.236
HY3-Preview 0.778 0.489 0.290 0.121 0.000 0.251
Kimi-K2.6 0.768 0.394 0.303 0.269 0.000 0.261
Balanced
DS-V4-Flash 0.774 0.321 0.290 0.172 0.000 0.226
DS-V4-Pro 0.764 0.387 0.301 0.289 0.005 0.266
Qwen3.6-Plus 0.793 0.531 0.298 0.209 0.091 0.300
Qwen3.7-Max 0.774 0.451 0.297 0.158 0.182 0.292
Qwen3.6-35B-A3B 0.772 0.476 0.295 0.237 0.000 0.272
GLM-5.1 0.773 0.472 0.303 0.296 0.409 0.384
DB-2.0-Lite 0.773 0.387 0.298 0.137 0.045 0.244
DB-2.0-Pro 0.778 0.483 0.294 0.179 0.000 0.263
HY3-Preview 0.791 0.531 0.264 0.133 0.000 0.258
Kimi-K2.6 0.786 0.464 0.297 0.247 0.000 0.274
Aggressive
DS-V4-Flash 0.795 0.475 0.298 0.195 0.009 0.268
DS-V4-Pro 0.783 0.463 0.303 0.250 0.014 0.278
Qwen3.6-Plus 0.802 0.566 0.297 0.162 0.409 0.366
Qwen3.7-Max 0.781 0.463 0.303 0.190 0.273 0.323
Qwen3.6-35B-A3B 0.786 0.553 0.299 0.252 0.318 0.365
GLM-5.1 0.779 0.510 0.295 0.310 0.409 0.393
DB-2.0-Lite 0.787 0.478 0.300 0.138 0.364 0.331
DB-2.0-Pro 0.787 0.494 0.300 0.168 0.273 0.325
HY3-Preview 0.807 0.574 0.292 0.132 0.000 0.274
Kimi-K2.6 0.790 0.514 0.293 0.199 0.136 0.304
Table 12: 2024 agreement with stage-specific references. S4 measures turnover agreement and S5 risk-state
agreement; financial outcomes are reported separately.
α=.5 ). We recompute CEPS for all 330 normal-
period decisions, then average by model within
each profile and across the three profiles. Figure 20
compares each ten-model ranking with its default
ranking using Spearmanρand Kendallτ b.
Rankings change little across the tested settings
with λ≤.2 : within-profile Spearman correlations
range from .988 to 1.000. Across the full α sweep,
they range from .964 to 1.000. The three-profile
mean ranking is unchanged at λ=.05 and at
α=.25 or .75. At λ=.5 , clipping sets 253/330
decision scores to zero. In the balanced profile,
93/110 scores become zero, creating tied model
means and making the ranking depend on the few
remaining positive scores. These results support
ranking stability around the default penalty and
across the tested S3 weights.
F.7 Stage Scores and Financial Associations
Table 16 links CEPS to realized outcomes within
each profile. Under the aggressive profile, higher
CEPS is associated with higher Sharpe ( ρ=.85 ,
95% CI [.41,1.00] ), connecting stage agreement
to risk-adjusted performance in this setting. The
association is weaker for conservative (.21) and bal-
anced (.09) portfolios, whose intervals include zero.
Positive associations with volatility and drawdown
magnitude show that the financial interpretation of
stage agreement also depends on the risk taken by
the portfolio.
Table 17 reports pooled associations and stress
diagnostics. Across profiles, CEPS correlates pos-
itively with Sharpe ( ρ=.587 ). Under the bal-
anced profile, higher normal-period CEPS is also
associated with a lower worst-window drawdown
relative to the profile tolerance (ρ=−.818 , 95%
CI [−.975,−.346] ). These profile-specific associa-
tions support assessing stage agreement alongside
risk-adjusted returns and stress resilience.
Full and core CEPS.Table 18 compares full
S1–S5 CEPS with S1–S3 core CEPS, averaging
across profiles. Spearman ρ is .66. GLM-5.1 moves
from core rank 4 to full rank 1, while HY3-Preview
moves from 2 to 8. S4 turnover agreement and S5
risk-state agreement change the ordering of models
with similar upstream scores.
27

Profile Model Ref. Class CEPS Exposure% Sharpe Ret% DD% V ol% GateConservative
DS-V4-Flash 0.118 0.477 0.253 18.2 -0.029 3.32 -8.87 9.51×
DS-V4-Pro 0.117 0.487 0.239 0.0 0.616 10.07 -7.50 9.87×
Qwen3.6-Plus 0.127 0.493 0.292 0.0 0.875 14.97 -9.56 12.22×
Qwen3.7-Max 0.121 0.461 0.232 0.0 0.578 9.16 -5.97 8.94×
Qwen3.6-35B-A3B 0.119 0.489 0.263 0.0 0.992 13.55 -6.19 9.21×
GLM-5.1 0.115 0.486 0.299 0.0 0.707 11.82 -7.87 11.00×
DB-2.0-Lite 0.123 0.476 0.223 0.0 0.740 10.79 -6.46 8.98×
DB-2.0-Pro 0.112 0.477 0.236 0.0 0.571 8.77 -5.73 8.34×
HY3-Preview 0.115 0.464 0.251 0.0 0.547 9.00 -6.38 9.21×
Kimi-K2.6 0.119 0.487 0.261 0.0 0.445 8.25 -6.59 9.94×
Balanced
DS-V4-Flash 0.109 0.471 0.226 81.8 0.609 9.89 -6.56 9.68×
DS-V4-Pro 0.116 0.487 0.266 54.5 0.542 9.46 -6.93 10.29✓
Qwen3.6-Plus 0.112 0.484 0.300 45.5 0.798 13.99 -10.11 12.35✓
Qwen3.7-Max 0.109 0.484 0.292 0.0 0.783 14.97 -11.02 13.95✓
Qwen3.6-35B-A3B 0.102 0.488 0.272 36.4 0.740 12.87 -7.77 11.91✓
GLM-5.1 0.111 0.495 0.384 0.0 0.603 13.10 -14.20 15.89✓
DB-2.0-Lite 0.113 0.483 0.244 9.1 0.838 14.01 -8.89 11.70✓
DB-2.0-Pro 0.107 0.481 0.263 45.5 0.662 12.09 -9.83 12.36✓
HY3-Preview 0.092 0.437 0.258 9.1 0.650 11.52 -8.05 11.66✓
Kimi-K2.6 0.101 0.494 0.274 0.0 0.769 14.29 -9.34 13.32✓
Aggressive
DS-V4-Flash 0.115 0.481 0.268 90.9 0.640 10.84 -7.40 10.72✓
DS-V4-Pro 0.121 0.485 0.278 100.0 0.653 10.34 -6.63 9.65✓
Qwen3.6-Plus 0.099 0.496 0.366 63.6 1.034 21.84 -13.05 16.57✓
Qwen3.7-Max 0.109 0.497 0.323 100.0 0.733 15.41 -13.20 15.79✓
Qwen3.6-35B-A3B 0.092 0.505 0.365 54.5 0.845 19.49 -16.83 18.33✓
GLM-5.1 0.089 0.502 0.393 63.6 0.930 21.00 -15.13 17.92✓
DB-2.0-Lite 0.104 0.496 0.331 100.0 0.916 18.48 -12.76 15.45✓
DB-2.0-Pro 0.105 0.496 0.325 100.0 0.867 16.15 -10.85 13.75✓
HY3-Preview 0.106 0.477 0.274 63.6 0.673 11.78 -8.74 11.61✓
Kimi-K2.6 0.093 0.492 0.304 18.2 0.890 19.34 -13.08 16.99✓
Table 13: 2024 results under common execution. Ref. is similarity to the profile-constrained lookback reference;
Class is the class-exposure correlation score. Exposure is the percentage of decisions meeting both exposure limits.
CEPS combines five-stage scores and penalizes downstream score drops; return, drawdown (DD), and volatility
measure financial outcomes. Gate requires all three stress-window drawdowns to meet the profile tolerance. Models
follow a fixed order.
Quantity Estimate 95% CIq
Mean distance to EqW .306 — —
Mean distance to S3 reference .890 — —
Mean S3 weight similarity .110 — —
Mean S3 correlation score .484 — —
Mean S3 score .297 — —
Mean HHI .0207 — —
Mean turnover ratio .203 — —
dEqW vs.∆Sharpe.514[.209,.736].004
dEqW vs. volatility.655[.389,.803]< .001
dEqW vs. drawdown magnitude.612[.378,.776]< .001
Table 14: Active-tilt diagnostics over 30 normal-period
model–profile cells: Spearman correlations with model-
cluster bootstrap intervals and BH-FDRq-values.
Stress-gate threshold.Rescaling each profile
tolerance by .8, .9, 1.1, and 1.2 changes 27 of
360 scenario-level tolerance checks (7.5%). Most
checks remain unchanged.
F.8 Paired Stage Interventions
Protocol and scoring.Callable S4 selects order
type, urgency, and slippage limits for a bound S3
Agg.–Cons. change Mean 95% CI +−
Equity+crypto exposure.175[.124,.221] 103 6
Bond+cash exposure−.162[−.205,−.117] 5 104
Distance from EqW.070[.026,.113] 89 20
HHI.0065[.0027,.0106] 91 18
V olatility (model means).0496[.0317,.0659] 9 1
DD magnitude (model means).0465[.0237,.0679] 8 2
Sharpe (model means).2140[.0886,.3491] 9 1
Table 15: Matched conservative-to-aggressive alloca-
tion and outcome changes. Allocation rows contain
110 model–date pairs; outcome rows contain ten paired
model means. The last two columns omit zero counts.
target. Its score weights legality, target tracking,
direction consistency, and cost awareness by .20,
.35, .25, and .20; the runtime binds the target quan-
tities and directions. Callable S5 selects a risk
action from executed weights and risk statistics.
Its reference chooses a 0.8 scale-down for a VaR
or drawdown breach, equal-weight rebalancing for
a drift breach, and hold otherwise. These scores
assess plan choices under the bound task interfaces.
28

0 0.05 0.1 0.2 0.5
Cascade penalty λ
0.4
0.6
0.8
1.0
Spearman ρ
A  Spearman ρ
0 0.25 0.5 0.75 1
S3 mixing weight α
Spearman ρ
B  Spearman ρ
0 0.05 0.1 0.2 0.5
Cascade penalty λ
0.4
0.6
0.8
1.0
Kendall τb
C  Kendall τb
0 0.25 0.5 0.75 1
S3 mixing weight α
Kendall τb
D  Kendall τb
Conservative Balanced Aggressive Profile average
Figure 20: CEPS ranking sensitivity over 330 normal-period decisions. Each curve compares ten model means with
the corresponding default ranking. The profile-average curve gives each profile equal weight. Dotted vertical lines
mark the default values. The other parameter is fixed while each parameter varies.
Profile Sharpe V olatility Drawdown magnitude
Conservative0.21[−0.66,0.65]0.82[0.37,0.96]0.58[−0.08,0.86]
Balanced0.09[−0.61,1.00]0.79[0.31,1.00]0.76[0.14,0.99]
Aggressive0.85[0.41,1.00]0.76[0.21,0.96]0.72[0.19,0.96]
Table 16: CEPS–financial outcome associations by profile (ten models). Paired model-bootstrap intervals.
Scope Statistic Estimate 95% CI
All profiles Sharpe (ρ).587[.337,.809]
All profiles V olatility (ρ).855[.683,.921]
All profiles DD magnitude (ρ).835[.618,.921]
Aggressive Stress ratio (ρ)−.600[−.925,.038]
Balanced Stress ratio (ρ)−.818[−.975,−.346]
Conservative Stress ratio (ρ).333[−.459,.887]
Table 17: Pooled outcome associations and profile-
specific stress diagnostics. Stress ratio is the largest
scenario drawdown divided by the profile tolerance. In-
tervals resample models.
The balanced-profile intervention diagnostic
uses callable S4/S5 plan tasks, so its downstream
changes measure responses in generated execution
and risk plans. The main ranking evaluates turnover
and lookback risk-state agreement. The normal di-
agnostic covers 99 securities. The financial replay
uses the tradable set defined in Appendix C.4. The
replaced stage receives its reference output and
scores one; downstream scores use the model out-
puts for those stages.
The paired analysis contains 300 intervention
Model Full R Core R
GLM-5.1 .359 1 .468 4
Qwen3.6-Plus .319 2 .491 1
Qwen3.6-35B-A3B .300 3 .468 3
Qwen3.7-Max .282 4 .451 7
Kimi-K2.6 .280 5 .463 5
DB-2.0-Pro .275 6 .462 6
DB-2.0-Lite .266 7 .442 8
HY3-Preview .261 8 .484 2
DS-V4-Pro .261 9 .441 9
DS-V4-Flash .249 10 .428 10
Table 18: CEPS-full (S1–S5) vs. CEPS-core (S1–S3):
ranks (R), three-profile means, Spearmanρ=.66.
episodes: 110 normal and 190 stress. Replac-
ing each stage with its reference output yields
1,500 branches and 4,500 stage-score changes. All
3,000 calls to subsequent model-dependent stages
meet the required output formats. Confidence
intervals for the complete matrices use 10,000
circular moving-block bootstrap samples within
model–window units, and p-values use Benjamini–
Hochberg FDR control within each split. For this
29

S1 S2 S3 S4 S5
Scored stage
S1
S2
S3
S4
S5
Replaced stage
+0.266* +0.626* +0.017* +0.021* -0.003
+0.699* +0.023* +0.007 -0.009
+0.670* +0.013* -0.002
+0.039* -0.007
+0.012
Normal
S1 S2 S3 S4 S5
Scored stage
S1
S2
S3
S4
S5
Replaced stage
+0.290* +0.652* +0.088* +0.004 -0.014
+0.731* +0.100* +0.005 -0.059*
+0.720* +0.001 -0.056*
+0.041* -0.014*
+0.062*
Stress
0.6
0.4
0.2
0.0
0.2
0.4
0.6
Mean paired score change
Figure 21: Paired influence matrix for normal and stress episodes. Each cell is the measured-stage score change
after replacing the indicated stage with its reference output. Asterisks mark BH-FDR q <0.05; black outlines
identify the stage pairs discussed in the main text.
paired intervention analysis, S3 scores are recom-
puted from the stage allocations. Ten terminal-
period S3 scores use only the finite correlation
pairs, with the corresponding weights renormal-
ized.
Figure 21 shows the stage-specific changes. Re-
placing S1 raises S2 by +.626 in normal episodes,
yet its mean effect on S3 is only +.017 and is neg-
ative in 40 episodes. Replacing S2 raises S3 by
+.023 in normal episodes, with 39 negative cases.
Under stress, replacing S2 or S3 lowers S5 by
−.059 and −.056, respectively. Most changes at
later measured stages are zero.Reference replace-
ments improve some downstream stage scores,
with effects that vary by stage and market con-
dition.
Tables 19 and 20 report the complete cell-level
means, confidence intervals, sign counts, and FDR-
adjusted tests for the normal and stress episodes.
Callable-stage results.Table 21 reports plan
scores, outcome scores, and their components over
330 normal and 570 stress episodes across all three
profiles. Runtime binding fixes S4 legality, tar-
get tracking, and direction, which carry 80% of
the plan score; model variation is concentrated in
cost awareness. Under stress, S5 action choice
falls from .927 to .884 and adjustment scale from
.917 to .857. These experiments evaluate model-
selected execution settings and risk actions under
fixed order and portfolio inputs.
Downstream gains and representative cases.
Table 22 excludes the directly replaced stage and
retains positive, unchanged, and negative down-
stream means. S1 replacement improves the down-
stream mean in 109/110 normal and 186/190 stress
episodes; later replacements have more mixed ef-
fects. To show what the measured changes mean,
Table 23 selects the normal-period branch nearest
the median within each sign group over S1–S3 re-
placements. Selection uses the same fixed rule for
all models.
For HY3-Preview on September 2, replacing S1
raises S2 by .566 and changes S4 from a market to
a limit order, gaining .100, despite a .116 decline
at S3. Its S5 action changes from rebalance to hold
while remaining correct for the respective input
state. For DS-V4-Flash on April 1, replacing S3
gains .696 locally, but both downstream plan scores
remain at their ceiling; the order type remains limit
and the risk action remains rebalance. For the same
model on October 1, replacing S2 gains .747 locally
and .017 at S3, but S4 changes from limit to market
and loses .100; S5 changes from hold to rebalance
without changing its score. These cases show why
both stage scores and action traces matter: changed
decisions need not change scores, and large local
score gains need not raise the downstream mean.
F.9 Within-Class Correlation Risk
Decisions and covariance estimates.We use all
330 normal-period allocations: ten models, three
profiles, and eleven monthly decisions from Febru-
30

Cell Mean 95% CI +−0p q
S1→S1 +0.266 * [+0.258, +0.274] 110 0 0< .001< .001
S1→S2 +0.626 * [+0.607, +0.644] 110 0 0< .001< .001
S1→S3 +0.017 * [+0.004, +0.032] 70 40 0 .011 .019
S1→S4 +0.021 * [+0.012, +0.031] 25 4 81< .001< .001
S1→S5 -0.003 [-0.022, +0.014] 3 6 101 .732 .785
S2→S2 +0.699 * [+0.684, +0.713] 110 0 0< .001< .001
S2→S3 +0.023 * [+0.009, +0.037] 71 39 0 .001 .002
S2→S4 +0.007 [-0.002, +0.017] 24 13 73 .098 .134
S2→S5 -0.009 [-0.026, +0.007] 2 9 99 .277 .324
S3→S3 +0.670 * [+0.659, +0.681] 110 0 0< .001< .001
S3→S4 +0.013 * [+0.003, +0.023] 24 9 77 .009 .015
S3→S5 -0.002 [-0.015, +0.013] 3 4 103 .812 .812
S4→S4 +0.039 * [+0.031, +0.047] 34 0 76< .001< .001
S4→S5 -0.007 [-0.021, +0.006] 2 4 104 .280 .324
S5→S5 +0.012 [+0.003, +0.022] 3 0 107 .040 .061
Table 19: Full normal paired influence matrix. Asterisks mark Benjamini–Hochberg q <0.05. Sign counts are
episode-level paired changes;n= 110for every cell.
Cell Mean 95% CI +−0p q
S1→S1 +0.290 * [+0.283, +0.298] 190 0 0< .001< .001
S1→S2 +0.652 * [+0.637, +0.668] 190 0 0< .001< .001
S1→S3 +0.088 * [+0.081, +0.096] 172 18 0< .001< .001
S1→S4 +0.004 [-0.004, +0.012] 34 25 131 .361 .387
S1→S5 -0.014 [-0.040, +0.011] 28 21 141 .283 .327
S2→S2 +0.731 * [+0.722, +0.740] 190 0 0< .001< .001
S2→S3 +0.100 * [+0.093, +0.108] 175 15 0< .001< .001
S2→S4 +0.005 [-0.003, +0.012] 30 25 135 .233 .291
S2→S5 -0.059 * [-0.087, -0.031] 22 37 131< .001< .001
S3→S3 +0.720 * [+0.714, +0.727] 190 0 0< .001< .001
S3→S4 +0.001 [-0.008, +0.010] 32 29 129 .873 .873
S3→S5 -0.056 * [-0.079, -0.032] 23 45 122< .001< .001
S4→S4 +0.041 * [+0.037, +0.046] 55 0 135< .001< .001
S4→S5 -0.014 * [-0.025, -0.003] 9 9 172 .017 .023
S5→S5 +0.062 * [+0.044, +0.080] 35 0 155< .001< .001
Table 20: Full stress paired influence matrix. Asterisks mark Benjamini–Hochberg q <0.05 . Sign counts are
episode-level paired changes;n= 190for every cell.
Table 21: Callable S4/S5 plan and outcome scores over 330 normal and 570 stress episodes across all three profiles.
Stage Score or subscore Normal Stress
S4 Plan score .954 .959
S4 Outcome score .985 .963
S4 Order legality / target tracking 1.000 / 1.000 1.000 / 1.000
S4 Direction consistency / cost awareness .999 / .774 .999 / .794
S4 Shortfall / cost / turnover / filled-weight match .979 / .979 / .991 / .992 .948 / .948 / .975 / .980
S5 Plan score .952 .918
S5 Outcome score .959 .916
S5 Alert identification / action choice .976 / .927 .961 / .884
S5 Corrective compliance / adjustment scale .972 / .917 .943 / .857
S5 CVaR / drawdown / violation / period return .983 / .976 / .927 / .950 .945 / .945 / .882 / .891
ary through December 2024. We use the financial
replay’s eligible securities, with excluded weight
held in uninvested cash. For each security, we take
its last 60 available return observations in the 90
calendar days up to the decision date. The primary
sample covariance uses dates observed for all eligi-
ble securities, giving each matched pair the same
positive-semidefinite matrix. Annualized estimated
volatility is ˆσ(w) =
p
252w⊤ ˆΣw. Uninvested
cash has zero variance.
31

Split Replaced stagen+ 0−Mean
Normal S1 110 109 0 10.165
Normal S2 110 68 0 420.007
Normal S3 110 24 73 130.006
Stress S1 190 186 0 40.181
Stress S2 190 139 0 510.016
Stress S3 190 45 80 65−0.042
Table 22: Mean score change strictly after the replaced
stage in the paired diagnostic. Counts classify each
branch’s downstream mean; the direct replacement gain
is excluded. Zero means unchanged measured scores,
not necessarily unchanged decisions.
Matched allocation.Let Hc ={i:c(i) =
c, wi >10 −10} contain the held securities in class
c, and W sec c = P i∈Hc wi their combined weight.
The control assigns ewi =W sec c /|Hc| for i∈H c,
with all other security weights zero and uninvested
cash unchanged. This preserves selected securi-
ties and total class exposure, including the cash-
equivalent sleeve. The relative volatility reduction
for decisioneis
re = 1−ˆσ( ewe)/ˆσ(we).(17)
We report the arithmetic mean across 330 pairs and
a 95% interval from 10,000 model-cluster bootstrap
samples. The uniform weights are determined by
the held securities and their class totals.
Variance decomposition.With c(i) denoting se-
curityi’s class,
V(w) =D(w) +I(w) +C(w),(18)
D(w) =
X
i
w2 i ˆΣii,(19)
I(w) = 2
X
i<j
c(i)=c(j)
wiwj ˆΣij,(20)
C(w) = 2
X
i<j
c(i)̸=c(j)
wiwj ˆΣij.(21)
These terms represent individual-security variance,
within-class covariance, and cross-class covariance.
Taking model minus control and averaging gives
∆V= 1.3599×10 −5, comprising 1.0386×10 −5
from I, 3.2017×10 −6 from D, and 1.0762×10 −8
from C. Within-class covariance accounts for
76.4% of the mean difference, individual-security
variance for 23.5%, and cross-class terms for 0.1%.
For si =
p ˆΣii, volatility-weighted pairwise
correlation is
¯ρ(w) =
P
i<j wiwjsisj ˆρij P
i<j wiwjsisj
.(22)
Unlike a class-average correlation, this quantity
changes with the allocation among correlated se-
curities inside a class. Its mean model-minus-
control difference is .033 (95% model-cluster inter-
val [.021, .046]), positive in 289/330 decisions.
Results and estimator sensitivity.Mean volatil-
ity reduction is 8.5% (95% interval [5.3%, 12.0%]),
with 271/330 positive reductions. Table 24 reports
every model–profile cell. The median reduction is
7.1%; mean reductions are positive in 27/30 model–
profile cells and on all eleven decision dates. The
paired design holds the class score fixed.
Pairwise covariance estimation uses each pair’s
overlapping observations in the same lookback win-
dow. It gives an 8.1% mean reduction (95% interval
[5.0%, 11.5%]), with 270/330 positive reductions.
Table 25 also reports controls that equalize across
all eligible securities within each class, or across all
eligible securities. All controls retain the original
uninvested cash. Expanding within-class holdings
gives a 9.6% mean reduction under the common-
date estimator; equal weighting across all eligible
securities gives 15.5%. The primary held-asset con-
trol isolates weighting at fixed asset selection and
class exposure. The main analysis uses common-
date covariance to remain positive semidefinite.
Representative allocation.DB-2.0-Pro’s bal-
anced allocation on November 1, 2024 holds 82
securities. Equalizing within-class weights at fixed
holdings and class exposures lowers estimated
volatility by 8.0% and reduces ¯ρby .074. Its largest
positive pairwise covariance contribution is A VGO–
NVDA, with correlation .765 and 2.00% of total
portfolio variance. NVDA–XLK contributes a fur-
ther 1.07%, with correlation .887. Both pairs con-
tribute correlated risk within this broad portfolio.
G Real-Time Evaluation
As discussed in Section 3.6, historical evaluation
can overlap with market information in model pre-
training (Li et al., 2025a; Chen et al., 2025a). PORT-
BENCHtherefore includes a real-time evaluation
mode: at each decision date D, the model receives
only information available through the previous
market close.
Setup.We run real-time evaluation with daily
rebalancing from 2026-07-16 to 2026-07-31 (12
trading days) under the balanced profile for six
models: HY3-Preview, Qwen3.7-Max, Qwen3.6-
Plus, Qwen3.6-35B-A3B, GLM-5.1, and Kimi-
32

Group Model Date Replaced stage∆S1∆S2∆S3∆S4∆S5 Downstream
Improvement HY3-Preview 2024-09-02 S10.270 0.566−0.116 0.100 0.000 0.138
Unchanged DS-V4-Flash 2024-04-01 S30.000 0.000 0.696 0.000 0.000 0.000
Deterioration DS-V4-Flash 2024-10-01 S20.000 0.747 0.017−0.100 0.000−0.028
Table 23: Median normal-period cases from positive, zero, and negative downstream-mean groups over S1–S3
replacements. Ties are resolved by model, date, then stage. Columns report score changes; upstream stages are
unchanged. These callable S4/S5 diagnostics are separate from the ranked pipeline.
Model Cons. Bal. Agg. All Lower
DS-V4-Flash 1.1 1.8 3.0 2.0 26/33
DS-V4-Pro 1.7 3.2 1.4 2.1 26/33
Qwen3.6-Plus 15.6 14.4 24.2 18.1 33/33
Qwen3.7-Max 9.5 19.6 24.9 18.0 32/33
Qwen3.6-35B-A3B -7.1 7.0 16.3 5.4 23/33
GLM-5.1 0.3 15.4 13.4 9.7 28/33
DB-2.0-Lite -1.2 9.1 20.2 9.4 25/33
DB-2.0-Pro -6.2 10.1 16.8 6.9 22/33
HY3-Preview 0.0 4.8 5.7 3.5 27/33
Kimi-K2.6 1.7 10.2 18.4 10.1 29/33
All models 1.6 9.6 14.4 8.5 271/330
Table 24: Estimated volatility reduction (%) from equal-
izing held securities within each class at fixed class
totals and uninvested cash. Each cell contains eleven
decisions; Lower counts positive reductions.
Control / covariance Reduction [95% CI] Lower
Held assets / common 8.5 [5.3, 12.0] 271/330
Held assets / pairwise 8.1 [5.0, 11.5] 270/330
All assets / fixed classes 9.6 [5.5, 13.8] 266/330
Full-support equal weight 15.5 [9.8, 21.0] 259/330
Table 25: V olatility reductions (%) under alternative co-
variance estimators and allocation controls. Expanded-
support controls use common-date covariance; all con-
trols preserve uninvested cash. Intervals resample mod-
els with all profiles and dates retained.
K2.6. DS-V4 and DB-2.0 models were unavailable
through their APIs during the run. Temperature and
decoding settings match Section 3.1. Table 26 re-
ports mean CEPS under the lookback S3 reference,
and Figure 22 plots daily scores.
           
'HFLVLRQGDWH








&(36ORRNEDFN

.LPL.
*/0
4ZHQ3OXV
4ZHQ%$%
4ZHQ0D[
+<3UHYLHZ
Figure 22: Per-decision lookback CEPS over the 12-day
real-time window (balanced profile).
Model CEPS lookback
Kimi-K2.6.420
GLM-5.1 .418
Qwen3.6-Plus .382
Qwen3.6-35B-A3B .378
Qwen3.7-Max .343
HY3-Preview .258
Table 26: Mean CEPS over the daily real-time window
(2026-07-16–07-31, balanced profile, 12 decision dates).
Models are ranked by lookback CEPS.
S1 S2 S3 S4 S5
Pipeline stage (lookback oracle)
Kimi-K2.6
GLM-5.1
Qwen3.6-Plus
Qwen3.6-35B-A3B
Qwen3.7-Max
HY3-Preview
0.82 0.42 0.60 0.16 0.54
0.82 0.49 0.60 0.14 0.46
0.80 0.41 0.58 0.12 0.44
0.79 0.44 0.56 0.13 0.39
0.79 0.38 0.56 0.08 0.37
0.78 0.38 0.56 0.05 0.00
0.0
0.2
0.4
0.6
0.8
1.0
Mean stage score
Figure 23: Mean lookback stage scores (S1–S5) over
the 12 real-time decision dates.
Kimi-K2.6 leads with lookback CEPS .420,
closely followed by GLM-5.1 at .418. Figure 23
shows high S1 (.78–.82), lookback S3 between
.561 and .604, and low S4 (.047–.163). HY3-
Preview has mean lookback S5 of 0. Figure 22
shows sharp drops for Qwen3.6-Plus and Qwen3.6-
35B-A3B on 2026-07-17, while GLM-5.1 has the
lowest day-level variation (std. .020).Daily scores
vary across models and dates, while turnover
agreement remains low.
Scoring.The lookback reference uses trailing ob-
servations available at the decision date. The daily
results use a signal-constrained reference and total-
variation weight scoring for S3. Historical portfolio
comparisons use the profile-constrained lookback
policy in Eq. 7. The twelve-day period, daily fre-
quency, and six-model coverage complement the
historical evaluation.
33

H Qualitative Examples
This appendix provides detailed examples of three
core components of PORTBENCH: the market base
dataset (§H.1), the QA dataset (§H.2), and the five-
stage evaluation pipeline (§H.3).
H.1 Market Snapshot Examples
A MarketSnapshot is the structured input con-
structed from the trailing lookback window and
provided to the model at each rebalance date for
the five-stage decision process. At each rebalance
date, the model receives the snapshot through three
isolated prompts and produces S1–S3; the sand-
box then executes the S3 allocation and computes
the S4/S5 execution and risk scores used in the
ranking. The snapshot contains four structured
layers: (1) per-asset price summaries with trailing
returns and volatilities, (2) macroeconomic indica-
tors, (3) a pairwise return correlation matrix with
intra-class and inter-class aggregation, and (4) the
current portfolio state. The two-layer correlation
interface exposes within-class co-movement and
cross-class hedging for joint allocation. Figures 24
and 25 illustrate these fields using representative
assets from the six-class market dataset under con-
trasting conditions: a calm bull market (2024-03)
and the COVID crash (2020-03). The field illus-
trations draw representative series from the full
six-class dataset of 183 market series. Historical
comparisons use the date-specific tradable subset
in Appendix C.4; portfolio states are illustrative.
H.2 QA Dataset Samples
Figure 26 presents one representative sample from
each of the seven QA templates (T1–T7), spanning
complexity levels L1–L4. Each shows the context,
ground-truth answer, and key reasoning step.
H.3 Pipeline Evaluation Traces
Figures 27 to 29 show complete five-stage traces
for three models across normal and stress windows.
Each trace reports a prompt summary, selected
model outputs, reference targets, and stage scores.
Scoring and execution use the eligible securities
in each snapshot. Model outputs are shown as
recorded. Their weights are normalized for ex-
ecution, with excluded allocations held as unin-
vested cash; VIX appears as market context and
any proposed VIX weight is held as cash. S1/S2 use
the trailing-return targets, and S3 uses the profile-
constrained lookback reference in Eq. 7. S4 applies
the common next-close execution and cost policy,
while S5 evaluates the resulting lookback risk state.
The examples cover broad equity exposure, a large
defensive reallocation, and a cash-heavy allocation.
34

MarketSnapshot(input constructed from trailing window at each rebalance date)2024-03-01|Balanced Profile
Per-Asset Summary(representative rows from the 183-series dataset)
Class Ticker Close 20d Ret. 60d Ret. Ann. Vol MaxDD 60d Sharpe60d Regime
Equities SPY 499.11+4.2%+8.4% 11.6%−1.7% 2.31 bull
QQQ 440.19+5.8%+15.3% 14.9%−2.4% 3.28 bull
XLE 89.74+7.1%+10.2% 18.3%−3.1% 1.78 bull
Bonds TLT 94.47−1.8%−3.0% 14.3%−4.9%−0.67 bear
IEF 93.49−0.5%−0.9% 7.2%−2.1%−0.40 sideways
Commod. GLD 202.17+3.1%+5.9% 13.3%−1.5% 1.41 bull
USO 76.83+2.4%+4.1% 26.7%−5.8% 0.49 sideways
Crypto BTC 61,148+22.3%+46.5% 50.1%−8.3% 2.96 bull
ETH 3,412+18.7%+38.2% 58.4%−11.6% 2.09 bull
RE VNQ 83.11+0.3%+1.8% 17.0%−4.2% 0.34 sideways
Cash BIL 91.63+0.04%+0.3% 0.3%−0.0% 3.19 sideways
Each asset also carries: daily return series, cumulative return curve, sector/sub-class tag.
Daily Price Series(excerpt from the 60-day lookback, normalized to 100 at excerpt start)
Representative assets from each class over the displayed interval (2024-01-02 to 2024-03-01). BTC surges +46% while TLT declines −3%, illustrating the
cross-class divergence that drives correlation-aware allocation. Daily closes and returns are drawn from the lookback window for the assets available in each
snapshot.
Macroeconomic Indicators
Fed Funds Rate: 5.33% VIX: 13.11 Unemployment: 3.90% 10Y–2Y Spread:−0.35
30Y Mortgage: 6.94% HY OAS: 3.32 10Y Breakeven: 2.32% TED Spread: 0.09
Two-Layer Correlation Interface trailing 60-day window
Class Intra-¯ρversus Equities¯ρ
Equities+0.48 —
Bonds+0.77−0.18
Commodities+0.23+0.12
Crypto+0.60+0.20
Real Estate+0.77+0.53
Cash+0.21−0.07
Portfolio State
NA V = $100,000|Weights: equal-weight ( 1 nt per eligible security)
Figure 24: Illustration of MarketSnapshot fields using the 2024-03-01 market data and an illustrative equal-
weight portfolio over eligible securities. The four input layers contain per-asset price data, macroeconomic indicators,
a two-layer correlation interface, and portfolio state.
35

MarketSnapshotCOVID Crash2020-03-13|Conservative
Per-Asset Summary(representative rows)
Class Ticker Close 20d 60d Vol MaxDD Regime
Equities SPY 270.06−9.8%−13.4% 44.2%−19.8% crisis
XLE 230.83−22.1%−31.3% 56.8%−38.4% crisis
Bonds TLT 151.57+8.3%+17.1% 18.3%−5.2% bull
Commod. USO 68.26−28.7%−36.8% 62.3%−42.1% crisis
Crypto BTC 5,418−4.2%−7.8% 45.2%−38.9% bear
RE / Cash VNQ / SHV 69.24 / 110.13−12.4% /+0.3%−18.9% /+0.7% 51.7% / 0.4%−26.3% / 0% crisis / side.
Daily Price Series(60-day lookback)
Macros|VIX 43.35, HY OAS 7.31, TED 0.57
Fed Funds 1.10% Unemployment 4.40% 10Y–2Y 0.45 10Y Breakeven 1.07% 30Y Mortgage 3.36%
Two-Layer Correlations(stress; RE–Eq¯ρ= 0.61)
Portfolio State
NA V = $94,900|equal-weight ( 1 nt over eligible securities)|Drawdown from peak:−5.1%
Figure 25: Illustration of MarketSnapshot fields during the 2020 COVID Crash with an illustrative equal-weight
portfolio over eligible securities. Compared with Figure 24, VIX is higher (43 versus 13), equities/commodities sell
off, bonds rally, and credit spreads widen.
36

T1: Return PredictionComplexity 1|Single Asset|Train
Context:ETH-USD over past 60 days: start=$320.88, end=$441.72, cumulative return +37.7%, ann. vol 79.6%. Macro:
fed_funds=1.16%, VIX=9.73. Regime: sideways.
Question:Predict whether the return of ETH-USD over the next 21 trading days will be:positive( >+1% ),negative
(<−1%), orflat(±1%).
Answer:positive(actual forward return:+49.99%)
T2: Risk Assessment (VaR)Complexity 1|Single Asset|Train
Context:XLV daily returns (60 days): mean=0.0000, std=0.0053, min=−0.0123, max=+0.0133. Regime: sideways.
Question:Using the historical simulation method, compute the 1-day VaR at 95% confidence level for XLV .
Answer:−0.0080(sort 60 returns, take 5th percentile)
T3: Position SizingComplexity 1|Single Asset|Train
Context:VCIT daily returns (60 days): std=0.0015, worst_day=−0.0043. Max drawdown threshold: 10%.
Question:Determine the maximum fraction of total portfolio to allocate to VCIT using the fixed-fractional formula
f ∗ = min(1, δmax/|VaR99%|).
Answer:1.0000(f ∗ = 0.10/0.0034 = 29.4→capped at 1.0)
T4: Pairwise Min-Variance AllocationComplexity 2|2 Assets|Val
Context:XLY: daily std =0.0123, annualized mean=0.2016. STIP: daily std=0.0021, annualized mean=0.0504. Minimum
annualized portfolio return: 0.1224.
Question:Compute minimum-variance weights satisfying the return floor, P w= 1, andw≥0.
Answer:w XLY = 0.4762,w STIP = 0.5238(binding return floor:w XLY = (0.1224−0.0504)/(0.2016−0.0504))
T5: Max-Sharpe OptimizationComplexity 3|4 Assets|Val
Context:Assets: VLUE, XRP-USD, DBC, BIL. Risk-free rate: 4.00%. Covariance matrix provided.
Question:Compute portfolio weights that maximize the Sharpe ratio. Constraints: P wi = 1,w i ≥0.
Answer:w VLUE=0.000,w XRP=0.001,w DBC=0.000,w BIL=0.999(Sharpe = 1.544)
T6: Rebalancing DecisionComplexity 3|4 Assets|Val
Context:Portfolio: IVV , BNB-USD, SGOV , PDBC. Current versus target weights given. Rebalance thresholdδreb=5%;
largest|w current −w target|=6.5%.
Question:(A) Should the portfolio be rebalanced? (B) If yes, identify the largest trade needed.
Answer:Yes; buy 0.065 of IVV(6.5%> δ reb=5%⇒rebalance triggered)
T7: Regime Detection and AllocationComplexity 4|6 Classes|Test
Context:SPY (60d): $664.67→$685.14, return+3.1%, vol 12.9%. Macro: fed_funds=3.64%, VIX=13.47.
Part A:Identify market regime from {bull, bear, sideways, crisis}.
Part B:For each of six asset classes, recommend: increase, decrease, or hold.
Answer:Regime: sideways. Equities:hold, Bonds:hold, Commodities:hold, RE:hold, Crypto:decrease, Cash:
increase.
Figure 26: Representative QA samples from all seven templates (T1–T7). Color indicates complexity level:
blue = L1 single-asset prediction/sizing (T1–T3), teal = L2 pairwise allocation (T4), orange = L3 multi-asset
optimization/rebalancing (T5–T6), red = L4 multi-signal judgment (T7).
37

Qwen3.6-Plus 2024-03-01|Balanced|Normal Period
S1: Market Interpretation Score = 0.771
Prompt summary:Assess the market on 2024-03-01 from the supplied asset and macro features. Return JSON with a view for each supplied asset, a
regime, confidence, and a macro summary.
Model Output Reference Target
SPY:+0.60, QQQ:+0.80, TLT:+0.10, GLD:+0.60, BIL:+0.60 SPY:+1.00, QQQ:+1.00, TLT:−0.25, GLD:+0.27, BIL:+0.01
Scoring:σ 1 = 1− 1 2n P i |ˆvi −v ∗ i |over eligible securities.
S2: Signal Generation Score = 0.477
Prompt summary:Use the S1 views to return JSON with a buy, hold, or sell signal and signal strength for each supplied asset.
Model Output Reference Target
SPY: buy, QQQ: buy, TLT: hold, GLD: buy, BIL: buy SPY: buy, QQQ: buy, TLT: sell, GLD: buy, BIL: hold
Scoring:Fraction of eligible-security signals matching the reference target.
S3: Weight Optimization Score = 0.313
Prompt summary:Use the S2 signals and supplied correlation information to return JSON with portfolio weights, expected return, volatility, and Sharpe.
Model Output S3 Reference
wNVDA=0.034,w QQQ=0.028,w AMAT=0.028,w A VGO=0.027w BIL=0.567,w DBA=0.092,w STIP=0.090,w XLV=0.086
Scoring:σ 3 = 0.5s acc + 0.5s corr withs acc = 1−TV(Eq. 8). Heres acc = 0.129ands corr = 0.497.
S4: Execution Simulation (deterministic) Score = 0.030
The deterministic S4 calculation defined above produces the following model and reference turnover.
Model Turnover (from S3) Reference Turnover
5.1% (change to the model target) 174.1% (change to the reference target)
Scoring:σ 4 = 1− |τ−τ ∗|/max(τ, τ∗,10 −4)≈0.030. Both changes start from the same pre-trade state.
S5: Risk Monitoring (deterministic) Score = 0.000
The deterministic S5 calculation defined above produces the following model and reference risk states.
Computed from Model Weights Computed from Reference Weights
VaR:−1.10%, MaxDD:−2.45%, Drift: 2.2%, Rebalance: No VaR:−0.18%, MaxDD:−0.22%, Drift: 55.6%, Rebalance: Yes
Scoring:σ 5 = 0.5d reb + 0.5 clip(1−(e VaR +e DD)/2,0,1). Rebalance flags and lookback risk magnitudes differ.
Summary:The model spreads weight broadly, while the reference places its largest weight in BIL. Turnover is 5.1% versus 174.1%, giving S4 of 0.030.
Adjacent score drops total 0.771, giving CEPS of 0.241.
Figure 27: Pipeline trace for Qwen3.6-Plus under normal conditions. A small model reallocation (5.1% turnover)
contrasts with 174.1% for the reference.
38

GLM-5.1 2020-02-28|Balanced|COVID Flash Crash
S1: Market Interpretation Score = 0.802
Prompt summary:Assess the market on 2020-02-28 from the supplied asset and macro features. Return JSON with a view for each supplied asset, a
regime, confidence, and a macro summary.
Model Output Reference Target
IWM:−0.70, XLE:−0.70, TLT:+0.70, GLD:+0.40, VIX:+0.80 IWM:−0.86, XLE:−1.00, TLT:+1.00, GLD:+0.91, VIX: context
Scoring:σ 1 = 1− 1 2n P i |ˆvi −v ∗ i |over eligible securities.
S2: Signal Generation Score = 0.488
Prompt summary:Use the S1 views to return JSON with a buy, hold, or sell signal and signal strength for each supplied asset.
Model Output Reference Target
XLE: sell, USO: sell, TLT: buy, GLD: buy, VIX: buy, QQQ: sell XLE: sell, USO: sell, TLT: buy, GLD: buy, VIX: context, QQQ: buy
Scoring:Fraction of eligible-security signals matching the reference target.
S3: Weight Optimization Score = 0.339
Prompt summary:Use the S2 signals and supplied correlation information to return JSON with portfolio weights, expected return, volatility, and Sharpe.
Model Output S3 Reference
wTLT=0.079,w GLD=0.071,w IAU=0.071,w VIX=0.063w ICSH=0.775,w TLH=0.100,w SHY=0.042,w IEF=0.041
Scoring:σ 3 = 0.5s acc + 0.5s corr withs acc = 1−TV(Eq. 8). Heres acc = 0.166ands corr = 0.511.
S4: Execution Simulation (deterministic) Score = 0.492
The deterministic S4 calculation defined above produces the following model and reference turnover.
Model Turnover (from S3) Reference Turnover
87.4% (change to the model target) 177.4% (change to the reference target)
Scoring:σ 4 = 1− |τ−τ ∗|/max(τ, τ∗,10 −4)≈0.492. Both changes start from the same pre-trade state.
S5: Risk Monitoring (deterministic) Score = 0.500
The deterministic S5 calculation defined above produces the following model and reference risk states.
Computed from Model Weights Computed from Reference Weights
VaR:−0.71%, MaxDD:−2.78%, Drift: 6.7%, Rebalance: Yes VaR:−0.03%, MaxDD:−0.12%, Drift: 76.4%, Rebalance: Yes
Scoring:σ 5 = 0.5d reb + 0.5 clip(1−(e VaR +e DD)/2,0,1). Rebalance flags agree; lookback risk magnitudes differ.
Summary:The model makes a large defensive reallocation. Its turnover of 87.4% versus 177.4% gives S4 of 0.492, the highest in this example set. The
proposed VIX weight of .063 is held as uninvested cash. Adjacent score drops total 0.463, giving CEPS of 0.478.
Figure 28: Pipeline trace for GLM-5.1 during the COVID flash crash (balanced profile). The large defensive
reallocation yields the highest S4 (0.492) among the three examples; the VIX output is held as uninvested cash.
39

Qwen3.7-Max 2022-10-07|Aggressive|2022 Market Decline
S1: Market Interpretation Score = 0.768
Prompt summary:Assess the market on 2022-10-07 from the supplied asset and macro features. Return JSON with a view for each supplied asset, a
regime, confidence, and a macro summary.
Model Output Reference Target
QQQ:−0.40, XLE:+0.20, TLT:−0.20, BIL:+0.60, VIX:+0.60 QQQ:−0.58, XLE:+1.00, TLT:−1.00, BIL:+0.00, VIX: context
Scoring:σ 1 = 1− 1 2n P i |ˆvi −v ∗ i |over eligible securities.
S2: Signal Generation Score = 0.545
Prompt summary:Use the S1 views to return JSON with a buy, hold, or sell signal and signal strength for each supplied asset.
Model Output Reference Target
QQQ: sell, XLE: buy, TLT: sell, BIL: buy, VIX: buy QQQ: sell, XLE: buy, TLT: sell, BIL: hold, VIX: context
Scoring:Fraction of eligible-security signals matching the reference target.
S3: Weight Optimization Score = 0.398
Prompt summary:Use the S2 signals and supplied correlation information to return JSON with portfolio weights, expected return, volatility, and Sharpe.
Model Output S3 Reference
wSGOV=0.232,w BIL=0.231,w SHV=0.165,w CSHI=0.120w SGOV=0.679,w PPLT=0.264,w WEAT=0.031,w CSHI=0.026
Scoring:σ 3 = 0.5s acc + 0.5s corr withs acc = 1−TV(Eq. 8). Heres acc = 0.258ands corr = 0.538.
S4: Execution Simulation (deterministic) Score = 0.025
The deterministic S4 calculation defined above produces the following model and reference turnover.
Model Turnover (from S3) Reference Turnover
3.4% (change to the model target) 140.0% (change to the reference target)
Scoring:σ 4 = 1− |τ−τ ∗|/max(τ, τ∗,10 −4)≈0.025. Both changes start from the same pre-trade state.
S5: Risk Monitoring (deterministic) Score = 0.500
The deterministic S5 calculation defined above produces the following model and reference risk states.
Computed from Model Weights Computed from Reference Weights
VaR:−2.18%, MaxDD:−2.40%, Drift: 22.1%, Rebalance: Yes VaR:−0.74%, MaxDD:−2.05%, Drift: 66.7%, Rebalance: Yes
Scoring:σ 5 = 0.5d reb + 0.5 clip(1−(e VaR +e DD)/2,0,1). Rebalance flags agree; lookback risk magnitudes differ.
Summary:Both portfolios hold cash equivalents, with different weights and turnover. Model turnover is 3.4% versus 140.0%, giving S4 of 0.025. The proposed
VIX weight of .072 is held as uninvested cash. Adjacent score drops total 0.743, giving CEPS of 0.373.
Figure 29: Pipeline trace for Qwen3.7-Max during the 2022 Market Decline (aggressive profile). The cash-heavy
model allocation changes little relative to the reference, giving S4 of 0.025.
40
