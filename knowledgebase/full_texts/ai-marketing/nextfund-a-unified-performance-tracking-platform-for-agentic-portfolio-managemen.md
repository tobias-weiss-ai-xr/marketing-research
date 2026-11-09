---
title: 'NextFund: A Unified Performance Tracking Platform for Agentic Portfolio Management'
url: https://arxiv.org/abs/2607.11141
category: ai-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Changlun Li
- Peixian Ma
- Qiqi Duan
- Zhenyu Lin
- Peineng Wu
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.11141
pages: 10
chars: 38298
fetched_at: '2026-11-08T13:02:06+00:00'
kb_version: 1
---

# NextFund: A Unified Performance Tracking Platform for Agentic Portfolio Management

NEXTFUND: A Unified Performance Tracking Platform
for Agentic Portfolio Management
Changlun Li* Peixian Ma Qiqi Duan Zhenyu Lin Peineng Wu
Paradoox AI Research
Abstract
Large language models (LLMs) based agents
are beginning to participate in portfolio con-
struction and market analysis, where decisions
must be justified under evolving information
and risk constraints. Current assessment prac-
tice, however, remains poorly aligned with
this setting: many studies rely on static ex-
aminations or report only terminal portfolio
returns, while the intermediate evidence, ana-
lyst judgments, and execution steps that pro-
duced those returns stay largely invisible. We
introduce NEXTFUND, an evaluation platform
that makes financial-agent behavior observable
under live market conditions. The platform
couples time-consistent market access, coor-
dinated multi-agent analysis, and persistent
logging of the full decision path from obser-
vation to trade. Through an interactive Trad-
ing Arena, users can compare models across
markets, inspect equity curves, and drill from
leaderboard outcomes down to individual jus-
tifications. We present NEXTFUNDon Hong
Kong, U.S., and China A-share equities, illus-
trating how inspectable decision histories en-
able fairer benchmarking and more actionable
diagnosis. Our demo is available at https:
//paradoox.cn/nextfund/.
1 Introduction
Recent advancement of large language models
(LLMs) has driven a shift from static financial
text analysis toward agentic portfolio management,
where LLMs-based agents can plan, gather evi-
dence, and act under live market conditions (Xiao
et al., 2024; Li et al., 2025, 2024; Yu et al., 2023;
Xiong et al., 2025; Fan et al., 2025; YANG et al.,
2025). Unlike traditional quantitative systems that
follow fixed features and hard-coded rules, LLM-
based agents can combine prices, news, calendars,
and portfolio constraints through multi-step reason-
ing before placing an order. This change widens
*Correspondence: tiger@paradoox.ai
what financial automation can do, but it also raises
a crucial tracking question: can an agent’s portfo-
lio decisions be shown to be reliable, comparable
across models, and open to systematic improve-
ment when markets move in real time?
Existing benchmarks answer this question only
in part. Many focus on task coverage or final per-
formance metrics such as cumulative return and
Sharpe ratio, while giving little insight into how
an action was formed (Li et al., 2024; Xiao et al.,
2024; Fan et al., 2025). As a result, users who need
to approve, monitor, or improve agent strategies
still face three recurring problems:
Incomplete Evaluation.Standard quizzes and
generic leaderboards rarely test whether an agent
can work with live market information, follow port-
folio constraints, and stay stable across different
market conditions.
Opaque Failure Diagnosis.When an agent uses
unsupported evidence, mishandles tools, or drifts
from its investment mandate, developers often can-
not tell whether the fault lies in retrieval, analysis,
synthesis, or execution, and thus cannot improve
the system with clear, repeatable feedback.
Lost Evaluation Traces.Decision logs, error
cases, reviewer notes, and tool-call histories are
often discarded after a run. Institutions therefore
gain little reusable data for later prompt revision or
model adaptation.
These problems grow more serious in multi-step
workflows. An early error in evidence selection
or time alignment can lead to a costly portfolio
change. Backtests that look only at final profit and
loss therefore miss the failure modes that matter
most for risk control and review. What is needed
is a unified performance tracking platform where
agentic portfolio decisions can be measured at each
step, compared across models, and retained for
later improvement.
We present NEXTFUND, a unified performance
tracking platform for agentic portfolio management
1
arXiv:2607.11141v1  [cs.AI]  13 Jul 2026

Method Markets Live Trace Arena
TradingAgents (Xiao et al., 2024) US✓× ×
FinMem (Yu et al., 2023) US× × ×
InvestorBench (Li et al., 2024) US, Crypto× × ×
DeepFund (Li et al., 2025) US✓×✓
TwinMarket (Y ANG et al., 2025) CN× × ×
QuantAgent (Xiong et al., 2025) US, Crypto, Comm.×Partial×
AI-Trader (Fan et al., 2025) US, CN, Crypto✓×Partial
NEXTFUND(Ours) HK, US, CN✓ ✓ ✓
Table 1: Comparison of NEXTFUNDwith prior systems for agentic portfolio management.Markets: covered
trading venues.Live: forward evaluation on live market streams.Trace: persistent end-to-end decision logs.Arena:
interactive interface for leaderboard comparison and inspection.
under these requirements. As shown in Table 1,
earlier systems provide multi-agent trading, live
testing, or interactive dashboards, yet rarely com-
bine live multi-market tracking with reusable deci-
sion traces and arena-style inspection. NEXTFUND
addresses this gap by recording observations, in-
termediate analyst outputs, and executed actions
under a shared point-in-time view of the market. Its
web-based Trading Arena enables leaderboard com-
parison and step-wise inspection, allowing users to
move from performance differences to underlying
agent behaviors.
Our contributions are as follows:
• A unified performance tracking platform.
NEXTFUNDunifies multi-market data access,
multi-agent coordination, and portfolio execu-
tion under common schemas and synchronized
time, supporting fair comparison across models.
• End-to-end decision tracing.NEXTFUNDsys-
tematically records observations, analyst sig-
nals, portfolio decisions, and execution outcomes,
thereby transforming opaque agent operations
into transparent performance histories.
• An interactive Trading Arena.The interface
provides cross-market leaderboards, trajectory
comparison, and trade-level rationale views, help-
ing users move from summary scores to concrete
diagnosis and improvement.
2 Related Work
2.1 Financial Agentic Frameworks
FinLLMs have moved financial AI from document
understanding toward systems that retrieve evi-
dence, reason over market state, and issue port-
folio actions (Wu et al., 2023; Yang et al., 2023;
Li et al., 2023; Nie et al., 2024). Building on this
shift, recent agentic frameworks organize memory,
personas, and specialist roles for trading and alloca-
tion (Yu et al., 2023, 2024; Xiao et al., 2024; Xiong
et al., 2025; Chen et al., 2025a; Y ANG et al., 2025),
while adjacent toolchains and RL environments
supply brokerage interfaces or executable market
simulators (Luo et al., 2026; Zhang et al., 2026;
Liu et al., 2021, 2022). These systems advance
agentic portfolio management, but they mainly op-
timize strategy construction or simulated returns;
persistent, cross-model performance tracking under
a shared live protocol remains secondary.
2.2 Agent Tracking and Benchmarking
Most financial LLM benchmarks still emphasize
knowledge, reasoning, or trustworthiness rather
than sequential portfolio decisions (Xie et al., 2023;
Islam et al., 2023; Xie et al., 2024; Liu et al., 2024;
Peng et al., 2025; Kang et al., 2026; Hu et al.,
2025). Decision-oriented suites move closer to
deployment by testing agentic trading and alloca-
tion tasks (Li et al., 2024; Chen et al., 2026, 2025b),
and live protocols further reduce contamination by
evaluating agents on post-cutoff market streams (Li
et al., 2025; Fan et al., 2025; Yu et al., 2025). Even
so, many trackers privilege terminal P&L, cover a
narrow venue set, or retain only partial intermedi-
ate state. NEXTFUNDtargets this gap as a unified
performance tracking platform that couples live
multi-market evaluation with end-to-end decision
traces and arena-style inspection.
3 NEXTFUNDSystem
NEXTFUNDserves as an evaluation layer connect-
ing market data, multi-agent reasoning, and portfo-
lio execution. Figure 1 summarizes the system ar-
chitecture, which aligns information access, agent
outputs, and decision traces.
2

Figure 1: Overview of the NEXTFUNDframework. The system integrates point-in-time data processing, multi-agent
decision making, performance evaluation, and traceable inspection. The database module uses PostgreSQL for
persistent backend data storage and SQLite for rapid I/O with the frontend.
3.1 Data Layer
NEXTFUNDbegins with a data pipeline that turns
heterogeneous market feeds into a shared, time-
consistent observation set for agentic portfolio man-
agement. The pipeline covers price bars, macro
snapshots, and hotlist news across U.S., China,
and Hong Kong equities, then compresses narrative
sources into a unified digest before any specialist
agent is invoked.
Market Data.For each candidate universe in the
U.S., China, and Hong Kong markets, we collect
daily equity price and volume bars and write them
into a shared OHLCV store. From these bars, the
pipeline derives market features used by later spe-
cialist analysts, while macro snapshots are retained
alongside the price series for audit and recovery.
All quantitative records are time-stamped so that
downstream serving can enforce a consistent point-
in-time view of the market.
News Data.We collect time-stamped financial
news as market-specific hotlists that feed the shared
observation pipeline. For China A-shares and Hong
Kong, the two markets share the same Chinese-
language news sources, built from finance hot-
rank articles on portals such as Sina Finance, East
Money, and Tencent Finance. For the U.S., we re-
tain English-language articles with publisher meta-
data from sources including Yahoo Finance and
CNBC. Before compression, each article is cleaned
for duplicates, aligned to a unified timestamp, and
retained only if it passes basic quality filters.
3.2 Multi-Agent Decision Pipeline
Time-aligned observations from the data layer are
consumed by a multi-agent decision pipeline that
maps market state to portfolio-level allocation pro-
posals. The pipeline is staged into separate steps:
specialized analysis is kept apart from constrained
synthesis, and only proposals that satisfy execution
constraints are forwarded to a shared evaluation
layer. This separation prevents a single model from
collapsing evidence gathering, risk control, and
trade generation into one opaque step.
Specialist Analysis.A set of dedicated analysts ex-
amines the shared decision state from complemen-
tary perspectives, including price dynamics, news
narratives, macroeconomic conditions, and policy
or risk cues. Each analyst returns a structured inter-
mediate signal, thereby encoding directional judg-
ment together with supporting justification. An up-
stream planner may activate the full analyst roster
or a context-dependent subset; because activation
and outputs are explicit, subsequent review can
attribute each contribution to a specific specialist.
Constrained Decision Synthesis.A decision man-
ager aggregates the analyst signals subject to ex-
plicit execution constraints, including long-only
exposure, position limits, cash availability, and
transaction costs. The manager produces a tex-
tual rationale together with target allocations over
the candidate universe and cash. By enforcing fea-
sibility at this stage, the pipeline converts research
judgments into portfolio proposals that remain con-
sistent with operational and risk requirements.
Handoff to Evaluation.The resulting proposals
are transferred to evaluation layer, where they are
instantiated as trades for backtesting and behavioral
analysis. Maintaining boundary among research
evidence, feasibility checks, and executed actions
enables systematic attribution: performance short-
3

falls can be traced to deficiencies in analysis, po-
sition sizing, or execution, rather than remaining
entangled in an end-to-end black box.
3.3 Performance Tracking and Provenance
The preceding pipelines produce observations and
allocation proposals; performance tracking is what
makes those artifacts comparable, diagnosable, and
reusable. In line with the platform goal stated in
the title, NEXTFUNDtreats tracking not as an after-
the-fact log dump, but as a first-class data plane
of agentic portfolio management: every evalua-
tion episode is retained as a structured provenance
graph under a shared clock, so that terminal returns
can be traced back to intermediate judgments and
executed actions.
Write-Through Integration.Tracking is embed-
ded in the multi-agent workflow rather than at-
tached after execution. When an analyst emits a
signal, or when the decision manager commits a
target allocation, the corresponding record is per-
sisted immediately together with its justification
and prompt context. Each trading day is anchored
by a portfolio snapshot that serves as the join key
for that day’s signals, decisions, and news digests.
Historical decisions and digests can also be read
back into later runs as memory, closing the loop
between recording and reasoning.
From Traces to Improvement.Because traces
are complete and time-aligned, the same substrate
supports cross-model comparison, failure attribu-
tion, and iterative refinement. Reviewers can ask
whether a rebalance followed coherent evidence ag-
gregation or reflected a localized fault in retrieval,
synthesis, or execution; retained trajectories fur-
ther supply material for prompt revision and super-
vised adaptation. The interactive demo application
in Section 5 is the user-facing interface over this
tracking layer.
4 Evaluation
We assess NEXTFUNDas an evaluation substrate
for agentic portfolio management. The central
question is whether the platform enables fair, time-
consistent, and inspectable comparison of frontier
LLM agents under a shared live protocol.
4.1 Task Setup
All runs use the same multi-agent workflow, point-
in-time data access, asset universe, and portfolio
constraints are in Appendix A.
Evaluation Windows.Experiments cover the first
two quarters of 2026 in full: 2026 Q1 (2026-01-01
to 2026-03-31) and 2026 Q2 (2026-04-01 to 2026-
06-30). Within each window, agents rebalance on
business days with synchronized prices, news di-
gests, and account states.
Markets and Universes.We evaluate three equity
markets (U.S., China A-shares, and Hong Kong),
each with a fixed seven-name universe spanning
major large-cap names in that venue. Each run
starts with a cash endowment of $100,000 and
follows long-only weight-based rebalancing under
shared position and cash constraints.
Models.We compare eight frontier LLMs as in-
terchangeable backbones of the same agent stack,
covering both proprietary and open-weight model
families. Details are listed in Appendix B.1.
Metrics.We report cumulative return, Sharpe ra-
tio, volatility, maximum drawdown, and turnover
to capture performance, risk, and trading behavior
in Section 4.2. Beyond aggregate metrics, NEXT-
FUNDretains the analyst outputs, portfolio deci-
sions, rationales, and execution records of each run,
which support the tracable analysis in Section 4.3
and the interactive inspection in Section 5.
4.2 Cross-Model Performance Comparison
Table 2 compares the eight model backbones on
the U.S. market across the two evaluation quar-
ters. Results for China A-shares and Hong Kong
equities are in Appendix B.2. The comparison re-
veals three main patterns. First, ranking depends
on both the metric and the regime. In 2026 Q1,
every backbone loses money in the U.S., but Kimi-
K2.6 is the least negative on return (−2.89%) and
also records the best volatility (5.04%) and draw-
down (4.39%), whereas DeepSeek-V4-Flash has
the least negative Sharpe. In Q2 the book rebounds:
Qwen3.5-Flash leads return (12.23%), while GPT-
5.4-Mini leads Sharpe (3.16), volatility (13.03%),
and drawdown (6.36%); Gemini-3.5-Flash records
the lowest turnover in Q1 (7.81%) and DeepSeek-
V4-Pro in Q2 ( 3.32%). Second, return, risk, and
trading intensity do not move together: a higher-
return model is not automatically the most efficient,
the most stable, or the least active, which is why
NEXTFUNDexposes the full metric vector rather
than a single P&L score. Third, the same proto-
col yields qualitatively different leaderboards in
China and Hong Kong (Appendix B.2), confirm-
ing that cross-market tracking is necessary for fair
comparison.
4

Model 2026 Q1 2026 Q2
Return (%) Sharpe V ol (%) MDD (%) Turn (%) Return (%) Sharpe V ol (%) MDD (%) Turn (%)
DeepSeek-V4-Flash−4.51−1.5011.82 8.57 11.28 8.66 2.16 15.70 9.37 7.44
DeepSeek-V4-Pro−11.86−2.94 16.69 15.36 8.15 10.27 2.16 18.65 11.863.32
Gemini-3.5-Flash−9.61−4.45 9.00 11.627.813.28 0.86 16.36 11.13 6.45
GLM-5.1−5.48−3.65 6.13 7.11 11.57 0.18 0.12 14.83 12.00 12.57
GPT-5.4-Mini−7.87−3.15 10.23 10.23 14.09 10.793.16 13.03 6.3614.02
Kimi-K2.6−2.89−2.305.04 4.398.91 8.95 2.18 16.07 9.84 5.96
MiniMax-M3−9.04−2.68 13.81 12.15 18.37 6.92 1.65 16.83 11.82 9.49
Qwen3.5-Flash−11.15−2.78 16.51 15.22 15.4312.232.77 16.93 9.63 10.58
Table 2: Live outcome metrics on U.S. equities under the shared NEXTFUNDprotocol. Return: cumulative return;
Sharpe: Sharpe ratio; V ol: annualized volatility; MDD: max drawdown (absolute); Turn: avg turnover. Bold
indicates best (higher is better for Return/Sharpe; lower for V ol/MDD/Turn). China/HK results are in Appendix B.2.
4.3 Case Study
To illustrate NEXTFUND’s diagnostic capability,
we compare two LLM backbones under the same
market, period, asset universe, and input stream.1
The aligned traces connect portfolio trajectories
with specialist signals and portfolio-manager ac-
tions, enabling inspection of where cross-model
divergence emerges. We use the U.S. 2026 Q1
case, comparing Kimi-K2.6 and Qwen3.5-Flash,
the highest- and lowest-return models in Table 2
for that period.
Signals can agree while decisions diverge.On
sampled trading days in U.S. 2026 Q1, compara-
ble analyst signal pairs (analyst×ticker) between
Kimi-K2.6 and Qwen3.5-Flash agree on about
92.9% of cases, suggesting that specialist views
are often similar when both models see the same
prices and news digests. Final BUY/SELL/HOLD
actions, however, agree on only 36.4% of ticker-
days over the full 64-day window, and on 47 days
more than half of the seven tickers disagree. The
action mixes explain much of the gap: Kimi-K2.6
remains conservative (396 HOLD / 29 BUY / 23
SELL), whereas Qwen3.5-Flash trades far more
actively (152 HOLD / 160 BUY / 136 SELL). The
comparison therefore surfaces a concrete failure
mode for opaque evaluation: similar intermediate
evidence need not imply similar portfolio behavior.
Metric profiles separate return from risk and
trading intensity.The same pair also illustrates
why a single P&L number is insufficient. In
U.S. 2026 Q1, Kimi-K2.6 records the best re-
turn (−2.89%), volatility (5.04%), and drawdown
(4.39%) among the eight backbones, with moderate
turnover (8.91%). Qwen3.5-Flash finishes near the
bottom on return (−11.15%) while posting higher
1Interactive comparison is available at https://
paradoox.cn/nextfund/comparison.
volatility (16.51%), deeper drawdown ( 15.22%),
and nearly double the turnover ( 15.43%). In Q2
the ranking flips on return, where Qwen3.5-Flash
leads at 12.23%, yet GPT-5.4-Mini remains prefer-
able on Sharpe, volatility, and drawdown. Head-to-
head tracking thus shows that model differences are
multi-dimensional. Aggressiveness in the decision
layer can raise turnover and risk even when analyst
signals look aligned, and the best return model in
one quarter need not dominate risk-adjusted met-
rics in the next.
5 Demo Application
Unlike benchmarks that mainly report end-state
returns (Li et al., 2024; Xiao et al., 2024), NEXT-
FUNDconnects portfolio outcomes with the de-
cision traces behind them. The demo supports
a two-stage workflow for researchers and practi-
tioners: identifying agent behavioral differences
(Section 5.2) and tracing them back to intermediate
decisions (Section 5.3).
5.1 Workflow Overview
Users first select a market among China, U.S.,
and Hong Kong and an evaluation window among
2026 Q1 and 2026 Q2. Given this selection, the
interface loads the corresponding runs under the
same universe, cash endowment, and rebalancing
rules used in Section 4. From there, users can move
to a comparison view for side-by-side model rank-
ing and trajectory inspection, or to a detail view for
step-wise decision tracking.
5.2 Model Arena
The Model Arena provides the entry point for cross-
model analysis. Users select a market, evaluation
period, and set of model runs to compare. The
interface presents cumulative return, Sharpe ratio,
5

Figure 2: The interface of NEXTFUNDdemo. This interface enables users to select different LLM backbones,
evaluation periods and markets. Users can also select a specific model to view detailed information and analyze the
decision trajectory.
volatility, maximum drawdown, and turnover to-
gether with equity curves, allowing users to identify
when and how portfolio trajectories diverge under
identical evaluation conditions. Because each run
is linked to its retained execution trace, users can
directly move from a performance difference to the
corresponding decision records. For example, a
model with higher return but higher turnover can
be selected for further inspection to understand
whether the difference arises from more frequent
actions or different portfolio allocation choices.
5.3 Detail Tracking
The Detail Tracking view enables users to inspect
an individual run at the decision level. For each
trading day and ticker, the interface links special-
ist outputs, portfolio-manager decisions, executed
actions, and textual rationales along a shared time-
line. Users can examine whether two agents di-
verge during upstream analysis, decision synthesis,
or execution. For instance, after observing a tra-
jectory divergence in the Model Arena, users can
select the corresponding period and compare ana-
lyst signals with final actions to determine whether
similar evidence led to different portfolio decisions.
This workflow transforms aggregate performance
comparison into a traceable diagnosis: rather than
only identifying which model performed differ-
ently, NEXTFUNDhelps users inspect how and
where the difference emerged.
6 Conclusion and Future Work
We present NEXTFUND, a unified live platform
for agentic portfolio management. By combining
multi-market data access, multi-agent analysis, and
end-to-end decision tracing, NEXTFUNDaddresses
the three recurring problems identified above: in-
complete evaluation, opaque failure diagnosis, and
lost evaluation traces. The demo application further
turns recorded trajectories into practical tools for
ranking, inspection, and iterative improvement. In
future work, we plan to cover more asset classes,
add stronger checks for unsupported claims and
risk compliance, and reuse retained trajectories for
prompt optimization and agentic learning.
6

Limitations
The current release centers on equity rebalancing
across three markets with a fixed analyst roster.
Support for derivatives, multi-currency hedging,
and richer compliance rules is left to future work.
Even with synchronized clocks and structured logs,
textual rationales may remain incomplete or only
loosely aligned with latent model computation; hu-
man review is still required for consequential deci-
sions. Live evaluation also depends on third-party
market feeds whose licenses may prohibit redis-
tributing raw data; public artifacts therefore em-
phasize schemas, traces, and interfaces rather than
proprietary market dumps.
Ethical Considerations
Financial agent evaluation can influence high-
stakes judgments. NEXTFUNDis intended as an
auditing and comparison aid, not as an investment
advisor. Demonstration outcomes should not be
the sole basis for investment or regulatory deci-
sions without independent checks against primary
sources. Users should examine provenance, de-
cision histories, and risk metrics, and interpret
leaderboard results as comparative evidence under
a stated protocol rather than as forecasts of future
performance.
References
Alibaba Cloud. 2026. Qwen3.5-flash: Production-grade
hosted model. https://qwen.ai/blog?id=qwen3.
5. Accessed: 2026-05-06.
Liyuan Chen, Gaoguo Jia, Dongsheng Gu, Jiangpeng
Yan, Yuhang Jiang, Xiu Li, and Xiaojun Zeng. 2025a.
Mentor: a multi-agent framework for event and narra-
tive trend prediction with optimized reasoning.Fron-
tiers of Information Technology & Electronic Engi-
neering, 26(10):1847–1861.
Liyuan Chen, Shilong Li, Jiangpeng Yan, Shuoling Liu,
Qiang Yang, and Xiu Li. 2026. Cn-buzz2portfolio: A
chinese-market dataset and benchmark for llm-based
macro and sector asset allocation from daily trending
financial news.arXiv.org.
Yanxu Chen, Yantao Liu, Zijun Yao, Jin Ye, Jianing Yu,
Lei Hou, and Juanzi Li. 2025b. Stockbench:can llm
agents trade stocks profitably in real-world markets?
DeepSeek-AI, Anyi Xu, Bang Lin, Bing Xue, Bing-
Li Wang, Bin Xu, Bo Wu, Bowei Zhang, Chao Lin,
Chengyao Dong, and 1 others. 2026. Deepseek-v4:
Towards highly efficient million-token context in-
telligence. https://deepseekv4.wiki/en/intro.
Accessed: 2026-05-06.
Tianyu Fan, Yuhao Yang, Yangqin Jiang, Yifei Zhang,
Yuxuan Chen, and Chao Huang. 2025. AI-Trader:
Benchmarking Autonomous Agents in Real-Time
Financial Markets.arXiv.org, arXiv:2512.10971.
Google DeepMind. 2026. Gemini 3.5 flash
model card. https://storage.googleapis.
com/deepmind-media/Model-Cards/
Gemini-3-5-Flash-Model-Card.pdf . Accessed:
2026-07-10.
Tiansheng Hu, Tongyan Hu, Liuyang Bai, Yilun Zhao,
Arman Cohan, and Chen Zhao. 2025. FinTrust: A
comprehensive benchmark of trustworthiness evalu-
ation in finance domain. InConference on Empiri-
cal Methods in Natural Language Processing, pages
10110–10139. Association for Computational Lin-
guistics.
Pranab Islam, Anand Kannappan, Douwe Kiela, Re-
becca Qian, Nino Scherrer, and Bertie Vidgen. 2023.
Financebench: A new benchmark for financial ques-
tion answering.arXiv.org.
Zhaolu Kang, Junhao Gong, Wenqing Hu, Shuo Yin, Ke-
han Jiang, Zhicheng Fang, Yingjie He, Chunlei Meng,
Rong Fu, Dongyang Chen, and 1 others. 2026. Quan-
teval: A benchmark for financial quantitative tasks in
large language models.arXiv.org, abs/2601.08689.
Changlun Li, Yao Shi, Chen Wang, Qiqi Duan, Runke
Ruan, Weijie Huang, Haonan Long, Lijun Huang,
Nan Tang, and Yuyu Luo. 2025. Time travel is cheat-
ing: Going live with deepfund for real-time fund
investment benchmarking. InarXiv.org, volume 38.
Curran Associates, Inc.
Haohang Li, Yupeng Cao, Yangyang Yu, Shashid-
har Reddy Javaji, Zhiyang Deng, Yueru He, Yuechen
Jiang, Zining Zhu, K. Subbalakshmi, Guojun Xiong,
and 1 others. 2024. Investorbench: A benchmark
for financial decision-making tasks with LLM-based
agent. InarXiv.org, pages 2509–2525. Association
for Computational Linguistics.
Yinheng Li, Shaofei Wang, Han Ding, and Hang Chen.
2023. A survey of large language models in finance
(finllms).4th ACM International Conference on AI
in Finance, pages 374–382.
Shu Liu, Shangqing Zhao, Chenghao Jia, Xinlin Zhuang,
Zhaoguang Long, Jie Zhou, Aimin Zhou, Man Lan,
and Yang Chong. 2024. FinDABench: Benchmark-
ing financial data analysis ability of large language
models. InInternational Conference on Computa-
tional Linguistics.
Xiao-Yang Liu, Ziyi Xia, Jingyang Rui, Jiechao Gao,
Hongyang Yang, Ming Zhu, Christina Dan Wang,
Zhaoran Wang, and Jian Guo. 2022. Finrl-meta: mar-
ket environments and benchmarks for data-driven
financial reinforcement learning. InNeural Informa-
tion Processing Systems, NIPS ’22, pages 1835–1849,
Red Hook, NY , USA. Neural Information Processing
Systems Foundation, Inc. (NeurIPS).
7

Xiao-Yang Liu, Hongyang Yang, Jiechao Gao, and
Christina Dan Wang. 2021. Finrl: deep reinforce-
ment learning framework to automate trading in quan-
titative finance. InInternational Conference on AI in
Finance, ICAIF ’21, New York, NY , USA. Elsevier
BV .
Haochen Luo, Yifan Li, Ho Tin Ko, An Binh Minh,
Junjie Xu, Tang Pok Hin, Wang Chak Wong, Gao
Yuan, Zhengzhao Lai, Yuan Zhang, and 1 others.
2026. QFinZero: A unified financial toolchain for
LLM-based trading agents. InProceedings of the
64th Annual Meeting of the Association for Compu-
tational Linguistics (V olume 3: System Demonstra-
tions), pages 68–77. Association for Computational
Linguistics.
MiniMax Research. 2026. Minimax m3: Frontier cod-
ing, 1m context, native multimodality — all in one
model. Accessed: 2026-07-11.
Moonshot AI. 2026. Kimi k2: A new era of reasoning.
Yuqi Nie, Yaxuan Kong, Xiaowen Dong, John M Mul-
vey, H Vincent Poor, Qingsong Wen, and Stefan
Zohren. 2024. A survey of large language models
for financial applications: Progress, prospects and
challenges.arXiv.org.
OpenAI. 2026. Introducing gpt-5.4. https://openai.
com/index/introducing-gpt-5-4/ . Accessed:
2026-05-06.
Xueqing Peng, Lingfei Qian, Yan Wang, Ruoyu Xiang,
Yueru He, Yang Ren, M. Jiang, Jeff Zhao, Huan He,
Yi Han, and 1 others. 2025. Multifinben: A multi-
lingual, multimodal, and difficulty-aware benchmark
for financial llm evaluation.arXiv.org.
Shijie Wu, Ozan Irsoy, Steven Lu, Vadim Dabravolski,
Mark Dredze, Sebastian Gehrmann, Prabhanjan Kam-
badur, David Rosenberg, and Gideon Mann. 2023.
Bloomberggpt: A large language model for finance.
arXiv.org.
Yijia Xiao, Edward Sun, Di Luo, and Wei Wang. 2024.
TradingAgents: Multi-Agents LLM Financial Trad-
ing Framework.arXiv.org, arXiv:2412.20138.
Qianqian Xie, Weiguang Han, Zhengyu Chen, Ruoyu
Xiang, Xiao Zhang, Yueru He, Mengxi Xiao, Dong
Li, Yongfu Dai, Duanyu Feng, and 1 others. 2024.
Finben: a holistic financial benchmark for large lan-
guage models. InNeural Information Processing
Systems, NIPS ’24, pages 95716–95743, Red Hook,
NY , USA. Neural Information Processing Systems
Foundation, Inc. (NeurIPS).
Qianqian Xie, Weiguang Han, Xiao Zhang, Yanzhao
Lai, Min Peng, Alejandro Lopez-Lira, and Jimin
Huang. 2023. PIXIU: A large language model, in-
struction data and evaluation benchmark for finance.
InarXiv.org, NIPS ’23, pages 33469–33484, Red
Hook, NY , USA. Neural Information Processing Sys-
tems Foundation, Inc. (NeurIPS).
Fei Xiong, Xiang Zhang, Aosong Feng, Siqi Sun, and
Chenyu You. 2025. QuantAgent: Price-driven multi-
agent LLMs for high-frequency trading.arXiv.org.
Hongyang Yang, Xiao-Yang Liu, and Christina Dan
Wang. 2023. Fingpt: Open-source financial large
language models.Social Science Research Network,
arXiv:2306.06031.
Yuzhe Y ANG, Yifei Zhang, Minghao Wu, Kaidi Zhang,
Yunmiao Zhang, Honghai Yu, Yan Hu, and Benyou
Wang. 2025. TwinMarket: A scalable behavioral and
social simulation for financial markets. InarXiv.org,
volume 38, pages 63469–63519. Curran Associates,
Inc.
Haofei Yu, Fenghai Li, and Jiaxuan You. 2025. Live-
tradebench: Seeking real-world alpha with large lan-
guage models.arXiv.org, arXiv:2511.03628.
Yangyang Yu, Haohang Li, Zhi Chen, Yuechen
Jiang, Yang Li, Jordan W Suchow, Denghui Zhang,
and Khaldoun Khashanah. 2023. FinMem: A
performance-enhanced LLM trading agent with lay-
ered memory and character design.IEEE Transac-
tions on Big Data.
Yangyang Yu, Zhiyuan Yao, Haohang Li, Zhiyang Deng,
Yupeng Cao, Zhi Chen, Jordan W. Suchow, Rong
Liu, Zhenyu Cui, Denghui Zhang, and 1 others. 2024.
Fincon: a synthesized llm multi-agent system with
conceptual verbal reinforcement for enhanced finan-
cial decision making. InNeural Information Pro-
cessing Systems, NIPS ’24, pages 137010–137045,
Red Hook, NY , USA. Neural Information Processing
Systems Foundation, Inc. (NeurIPS).
GLM-4.5 Team Aohan Zeng, Xin Lv, Zhenyu Hou,
Zhengxiao Du, Qinkai Zheng, Bin Chen, Da Yin,
Chendi Ge, Chengxing Xie, Cunxiang Wang, and 1
others. 2026. Glm-5: from vibe coding to agentic
engineering.arXiv.org.
Fan Zhang, M. Song, R. Elbadry, Yankai Chen, Shaobo
Wang, Yixi Zhou, Xu Zheng, Yueru He, Yuyang Dai,
Georgi N. Georgiev, and 1 others. 2026. FinReport-
ing: An agentic workflow for localized reporting of
cross-jurisdiction financial disclosures. InProceed-
ings of the 64th Annual Meeting of the Association
for Computational Linguistics (V olume 3: System
Demonstrations), pages 728–735. Association for
Computational Linguistics.
8

A Additional Details
A.1 Detailed Database Schema
Tracking Trajectory Schema.NEXTFUNDper-
sists each evaluation episode as a time-aligned tra-
jectory that can be reconstructed from the live track-
ing API. Table 3 summarizes the core fields of a
per-ticker decision record returned by the trajectory
endpoint, including the attached analyst signals
used for diagnosis.
Field Type Description
trading_datestring Business date of the decision
record.
portfolio_idstring Identifier linking the record to
the same-day portfolio snap-
shot.
tickerstring Asset symbol under consider-
ation.
actionstring Executed action ( Buy, Sell,
orHold).
shares numberNumber of shares traded; zero
for hold actions.
price numberReference or execution price
used by the record.
justificationstring Textual rationale for the exe-
cuted action.
linked_trace_idstring Provenance identifier for the
decision trace.
workflow_decisionobject Portfolio-manager workflow
metadata, including selected
analysts.
analyst_signalsarray Specialist outputs attached to
the decision.
Table 3: Schema of a tracking trajectory decision record
in NEXTFUND.
Price Data Schema.Market prices are stored as
daily OHLCV bars under a shared point-in-time
protocol. Table 4 lists the fields of the equity price
table used by the data layer.
News Data Schema.News items are collected
from market-specific hotlists and aligned to the
evaluation clock before compression into digests.
Table 5 summarizes the core fields of the news
table.
B Additional Evaluations
B.1 Evaluation Models and Universes
Models.We evaluate eight frontier LLMs as
interchangeable backbones of the same multi-
agent stack: DeepSeek-V4-Flash (DeepSeek-AI
et al., 2026), DeepSeek-V4-Pro (DeepSeek-AI
et al., 2026), Gemini-3.5-Flash (Google DeepMind,
2026), GLM-5.1 (Zeng et al., 2026), GPT-5.4-
Mini (OpenAI, 2026), Kimi-K2.6 (Moonshot AI,
Field Type Description
pool_nametext Equity pool name (e.g., cn, us,
hk).
markettext Market identifier of the listed
venue.
symboltext Ticker symbol in the evaluation
universe.
trade_datetext Trading date in YYYY-MM-DD
format.
openreal Opening price.
highreal Highest price.
lowreal Lowest price.
closereal Closing price.
volumeinteger Trading volume.
sourcetext Upstream data provider identi-
fier.
Table 4: Schema of the daily equity price table in NEXT-
FUND.
Field Type Description
idinteger Auto-increment primary key.
sourcetext News source identifier (e.g.,
sina).
titletext Article headline.
urltext Canonical article URL.
publish_timetext Publication timestamp.
crawl_timetext Timestamp when the article
was crawled.
crawl_datetext Calendar date used for day-
level alignment.
mediatext Publisher or media outlet
name.
top_numinteger Hotlist rank or popularity in-
dex.
categorytext Source category or channel tag.
contenttext Article body text when avail-
able.
authortext Author byline when available.
keywordstext Extracted or provided key-
words.
word_countinteger Approximate body length in
words or characters.
related_stockstext Linked tickers associated with
the article.
created_at timestampDatabase insertion time.
Table 5: Schema of the hotlist news table in NEXT-
FUND.
2026), MiniMax-M3 (MiniMax Research, 2026),
and Qwen3.5-Flash (Alibaba Cloud, 2026). The
set covers both proprietary and open-weight model
families. All backbones share the same point-
in-time data access, analyst roster, portfolio con-
straints, and logging schema.
Asset Universes.Each market uses a fixed seven-
name large-cap universe: the U.S. pool comprises
AAPL, MSFT, NVDA, TSLA, AMZN, GOOGL,
and JPM; the China A-share pool comprises
600519.SH, 300750.SZ, 601318.SH, 601899.SH,
9

Model 2026 Q1 2026 Q2
Return (%) Sharpe V ol (%) MDD (%) Turn (%) Return (%) Sharpe V ol (%) MDD (%) Turn (%)
DeepSeek-V4-Flash 3.36 0.86 17.11 3.86 18.55−14.98−4.32 14.52 15.64 16.54
DeepSeek-V4-Pro 7.29 1.51 19.86 4.32 8.00−15.31−4.83 13.36 15.75 10.40
Gemini-3.5-Flash 4.18 0.82 23.27 7.527.49−12.38−5.11 10.06 12.38 12.50
GLM-5.19.762.20 17.67 3.70 10.20−12.58−4.63 11.29 12.759.49
GPT-5.4-Mini 0.85 0.429.13 2.7916.84−11.97−5.65 8.82 12.20 17.80
Kimi-K2.6 9.522.4215.51 3.31 13.01−7.66−3.89 7.98 7.8512.03
MiniMax-M3 7.02 1.66 17.18 4.08 22.09−17.21−5.57 13.17 18.70 18.72
Qwen3.5-Flash−4.81−0.96 18.76 7.39 13.89−14.00−5.07 11.58 14.00 16.31
Table 6: Live outcome metrics on China A-share equities under the shared NEXTFUNDprotocol. Metric definitions
follow Table 2.
Model 2026 Q1 2026 Q2
Return (%) Sharpe V ol (%) MDD (%) Turn (%) Return (%) Sharpe V ol (%) MDD (%) Turn (%)
DeepSeek-V4-Flash 1.77 0.37 36.81 15.33 13.85 11.95 1.65 29.48 9.48 16.42
DeepSeek-V4-Pro 14.63 1.63 37.66 11.01 9.10 1.34 0.35 22.07 8.46 7.92
Gemini-3.5-Flash 18.56 1.86 40.91 13.03 8.4523.41 2.8730.48 7.985.78
GLM-5.1 7.02 1.4619.987.595.500.47 0.19 20.60 8.92 7.09
GPT-5.4-Mini 7.27 1.32 23.33 9.50 16.36 4.43 1.2115.07 5.7713.79
Kimi-K2.630.94 3.2135.516.4511.33 7.01 1.55 18.33 6.94 12.26
MiniMax-M3 10.24 1.29 34.99 11.23 19.63 8.79 1.43 25.35 8.83 15.27
Qwen3.5-Flash 20.10 2.05 39.56 8.67 15.04 8.71 1.30 28.18 9.77 14.16
Table 7: Live outcome metrics on Hong Kong equities under the shared NEXTFUNDprotocol. Metric definitions
follow Table 2.
601398.SH, 601857.SH, and 600938.SH; and the
Hong Kong pool comprises 9992.HK, 0700.HK,
1810.HK, 2513.HK, 03690.HK, 0005.HK, and
1299.HK.
B.2 Additional Market Results
This subsection reports the same outcome metrics
as Table 2 for China A-shares and Hong Kong
equities. In China (Table 6), GLM-5.1 leads re-
turn in 2026 Q1 (9.76%), while Kimi-K2.6 leads
Sharpe (2.42) and GPT-5.4-Mini leads volatility
and drawdown; Gemini-3.5-Flash records the low-
est turnover in Q1 ( 7.49%). In Q2 all models
are negative, and Kimi-K2.6 remains strongest
across return, Sharpe, volatility, and drawdown,
while GLM-5.1 has the lowest turnover ( 9.49%).
In Hong Kong (Table 7), Kimi-K2.6 leads return
(30.94%), Sharpe (3.21), and drawdown (6.45%)
in Q1, with GLM-5.1 recording the lowest volatility
and turnover; in Q2, Gemini-3.5-Flash leads return
(23.41%), Sharpe ( 2.87), and turnover ( 5.78%),
whereas GPT-5.4-Mini leads volatility and draw-
down.
B.3 License
The NEXTFUNDsoftware and associated artifacts
released with this paper are licensed under the
Apache License 2.0.2
2https://www.apache.org/licenses/LICENSE-2.0
10
