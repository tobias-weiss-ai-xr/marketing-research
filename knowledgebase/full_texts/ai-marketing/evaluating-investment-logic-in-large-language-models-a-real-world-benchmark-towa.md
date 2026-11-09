---
title: 'Evaluating Investment Logic in Large Language Models: A Real-World Benchmark Towards Personalzied
  Financial Agents'
url: https://arxiv.org/abs/2608.06108
category: ai-marketing
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Yuanhong Jiang
- Jingjie Zou
- Rui Jiang
- Zhenghong Lin
- Xusheng Yu
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.06108
pages: 18
chars: 56326
fetched_at: '2026-11-08T13:29:15+00:00'
kb_version: 1
---

# Evaluating Investment Logic in Large Language Models: A Real-World Benchmark Towards Personalzied Financial Agents

Evaluating Investment Logic in Large Language Models: A Real-World
Benchmark Towards Personalzied Financial Agents
Yuanhong Jiang*†1 2 Jingjie Zou * 3 Rui Jiang 2 Zhenghong Lin 1 Xusheng Yu4 Qiqi Huang 4 Shuai Jia 2
Shijie Dai †5 2
Abstract
The dominant paradigm for evaluating Large
Language Models remains anchored in chat and
question-answering (QA) tasks, creating a funda-
mental mismatch with the competencies required
for reliable agent execution in real-world domains.
This disconnect is acutely evident in financial
decision-making, where proficiency is defined not
by knowledge recall, but by the capacity to align
Person—the investor’s unique profile, constraints,
and risk preferences—with the interpretation of
unstructured marketEvents(E), the synthesis of
coherent investmentReasoning(R), the formula-
tion of correspondingDecisions(D), and the pur-
suit of profitableOutcomes(O). Without evalua-
tion grounded in this integrated P→E→R→D→O
chain, progress toward capable financial agents
remains stalled.
To bridge this gap, we introduce INVESTLOG-
ICBENCH2026, a benchmark derived from
the documented decision-making of real-world
investors. It provides structured, validated traces
that explicitly instantiate such investment logic
chain for each investment thesis. Our evaluation
reveals a pronounced investment logic gap:
state-of-the-art LLMs encounter significant
bottlenecks in both emulating the reasoning of
expert investors and translating such reasoning
into profitable outcomes. Our benchmark estab-
lishes the first reproducible and market-aligned
standard for quantifying this deficiency. This
work shifts the evaluation paradigm from passive
knowledge recall to active reasoning, paving
the way for building robust, end-to-end LLM
investment agents that generate market-aligned
and personalized decisions adaptable to diverse
strategies. The project is publicly accessible in
https://anonymous.4open.science/r/InvestLogicBench-
C2D7.
1. Introduction
The rapid integration of Large Language Models (LLMs)
into finance has transformed tasks ranging from sentiment
analysis and earnings call summarization to macroeconomic
forecasting, yet their deployment in live trading environ-
ments reveals significant performance limitations. This pro-
gression has culminated in the emergence of live-trading
arenas where LLM-based agents compete with real capital,
relying solely on real-time news and market data (Fan et al.,
2025). These platforms provide an unforgiving, forward-
looking test of practical capability, revealing a striking disso-
nance: models that excel on established financial reasoning
benchmarks often generate unprofitable or unstable strate-
gies in live markets.
The observed “Capabilities-Performance Paradox”(Ding
et al., 2024) points to a fundamental distinction between
financial knowledge and investment intelligence. Current
LLMs demonstrate impressive proficiency at retrieving facts,
solving textbook problems, and performing quantitative
calculations—skills meticulously measured by benchmarks
such as FinBen (Xie et al., 2024) and BizBench (Koncel-
Kedziorski et al., 2024). Yet they lack the higher-order logic
required for successful market participation: the ability to
distill salient signals from unstructured news, connect dis-
parate geopolitical, corporate, and macroeconomic events
into a coherent narrative, adjudicate between conflicting data
points under uncertainty, and formulate—then steadfastly
maintain—a strategic thesis that aligns with a consistent
investment style.
We argue that this failure is not incidental but systemic,
stemming from threestructural mismatchesbetween the
prevailing LLM paradigm and the cognitive requirements
of successful investing:
Objective Mismatch:LLMs are trained via next-token
prediction on vast corpora, optimizing for linguistic co-
herence over causal reasoning. Raw financial text, while
abundant, rarely contains explicit annotations of the in-
vestment decision cycle: how an investor’s uniquePerson
(P)—comprising their objectives, risk constraints, and be-
havioral biases—interacts with marketEvents(E), which
1
arXiv:2608.06108v2  [cs.AI]  20 Aug 2026

INVESTLOGICBENCH2026
are then interpreted and synthesized into investmentRea-
soning(R), leading to correspondingDecisions(D), and
ultimately aiming at profitableOutcomes(O). Without ex-
posure to structured P →E→R→D→O investment logic
chains, models struggle to internalize the instrumental logic
of investment decision-making. (Chen et al., 2024).
Evaluation Gap:Existing financial benchmarks over-
whelmingly assess static QA skills—fact retrieval, calcu-
lation, and well-defined problem-solving. They evaluate a
model’s prowess as a financial analyst but fail to assess its
competency as a portfolio manager: its ability to identify
consequential signals in real-time noise, synthesize narra-
tives from unfolding events, and maintain strategic disci-
pline. This creates anevaluation opacity: we can measure
whether an agent succeeds (via P&L) but cannot diagnose
the underlying reasoning quality, thus obscuring whether
success stems from sound logic or stochastic luck (Ding
et al., 2024).
To bridge this chasm, we shift the paradigm from evaluat-
ing what models know to assessing how they think. We
introduce InvestLogicBench2026, the first benchmark con-
structed from the dynamic, articulated reasoning processes
of successful market participants. It provides structured, val-
idated traces that explicitly instantiate the P→E→R→D→O
chain for each investment thesis. Our framework extracts
and structures investment theses from experienced fund
managers and key opinion leaders (KOLs) into explicit
P→E→R→D→O chains, capturing market events, logical
rationale, concrete actions, and market-verified outcomes.
Our contributions are threefold:
1. Through a seven-week experimental study comparing
live agent profitability with benchmark results, we em-
pirically identify a pronounced capability-performance
paradox in leading LLMs when applied to real-world
market investment.
2. We present INVESTLOGICBENCH2026, the first
benchmark for evaluating practical investment logic,
featuring 201,247 structured decisions annotated with
events, reasoning , decisions, actions, and market-
verified outcomes from 151 real-world investors.
3. We quantify a significant investment logic gap: lead-
ing LLMs achieve only 1.8/5 reasoning score against
expert traces, revealing systematic failures in event-
noise discrimination and long-horizon consistency that
explain their live trading underperformance.
By establishing a diagnostic benchmark for market-aligned
reasoning under uncertainty, INVESTLOGICBENCH2026
shifts the evaluation focus from financial knowledge recall
to the critical ability to formulate and execute coherent
investment theses.
2. Can Language Models Make Profitable
Investment in Real-World Markets?
Despite demonstrating outstanding competence in informa-
tion retrieval and accessing specialist domain knowledge,
current state-of-the-art models frequently struggle to cap-
ture critical financial events and conduct rigorous logic
analysis when navigating the stochastic, adversarial, and
non-stationary dynamics of live trading scenarios, which
we termed the “Capabilities-Performance Paradox”. This
disconnect highlights a fundamental reliability gap: the pro-
ficiency to explain financial concepts does not guarantee the
agency required to analyze and execute profitable strategies
under uncertainty.
2.1. The U. S. Equity Trading Arena: A Live-Fire
Market Competition
To rigorously evaluate the investment logic of LLMs in
market-aligned conditions, we instantiated a live U.S. equity
trading arena. From November 19, 2025, multiple LLM-
based agents, each initialized with $10,000 in simulated
capital, competed autonomously to maximize risk-adjusted
returns through discretionary hourly trading of U.S. stocks
and ETFs.
The arena was designed to test the complete
P→E→R→D→O chain under uncertainty. Agents
maintained strategic continuity through access to their
full Portfolio Report and Trading History .
To simulate professional practice, they actively foraged
for information via a dual-toolPerception-Action
Loop—querying structured data with FinQuery and
unstructured intelligence with Search—then synthesized
these signals into executable trades with explicit reasoning.
This forward-testing format eliminated retrospective bias,
providing a pure assessment of an LLM’s ability to form
and act on market logic in real time.
2.2. The Capabilities-Performance Paradox
As visualized in Figure 1 (Right), we contrasted the mod-
els’ Foundation Aptitude Scores—an average score de-
rived from MMLU-Pro, SWE-bench, AIME 2025, and Sim-
pleQA—against their realized financial returns. While scal-
ing laws typically postulate a positive correlation between
general reasoning capabilities and downstream task perfor-
mance, our empirical data exhibits a distinct counterintuitive
misalignment.
Strikingly, models possessing superior foundation scores,
such as Claude-Sonnet-4.5 (Score: 77.2) and GPT-5 (Score:
73.5), failed to translate their general reasoning dominance
into effective market execution. Throughout the7-week
live trading window (Nov. 19, 2025 – Jan. 9, 2026),
GPT-5 ended with a portfolio value of $9,901.1 (-1.0%),
2

INVESTLOGICBENCH2026
Nov 19 Dec 12 Jan 07 Jan 30 Feb 24 Mar 17 Apr 06 Apr 23 May 13 May 24
$8,000
$10,000
$12,000
$14,000
$16,000
$18,000
$20,000
$10,000
Total Account Value
$10,268.81
$11,252.74
$11,419.70
$12,582.84
$13,216.42
$14,765.98
$15,173.11
$16,362.11
DeepSeek-V3
Qwen3-Max
Gemini 2.5 Pro
Claude Sonnet 4.5
GPT-5
S&P 500 benchmark
Cathie Wood
Dave Mazza
60.0 62.5 65.0 67.5 70.0 72.5 75.0 77.5 80.0
Foundation Aptitude Score
0.0%
20.0%
40.0%
60.0%
80.0%
Real-World Cumulative Return (%)
Comparative Analysis of LLMs:
Foundation vs. Real-World Trading Performance
Gemini 2.5 Pro: $11419.7
(Score: 70.7)
Qwen3-Max: $14766.0
(Score: 76.1)
DeepSeek-V3: $16362.1
(Score: 64.6)
Claude Sonnet 4.5: $12582.8
(Score: 77.2)
GPT-5: $10268.8
(Score: 73.5)
Figure 1. The “Capabilities-Performance Paradox” in financial domain.(Left) Cumulative equity curves between autonomous
LLM agents and human expert proxies in a 7-week live U.S. stock trading competition. DeepSeek-V3 achieved the highest cumulative
return, significantly outperforming the S&P 500 benchmark, while models like GPT-5 and Claude-Sonnet-4.5 demonstrated lackluster
performance in seizing opportunities. Key market inflection points highlight periods where expert logic diverged from model behavior.
(Right) Comparative analysis between Foundation Aptitude Scores and Real-World Cumulative Returns. It suggests that superior
performance on general benchmarks fails to reliably transfer into financial analytical acumen or effective real-world trading execution.
while Claude-Sonnet-4.5 yielded negligible gains, closing
at $10,072.8 (+0.7%). Both models failed to surpass the
passive S&P 500 (SPY) benchmark, which returned approx-
imately +4.3% over the same period, indicating that most
models were paradoxically less effective in the live financial
domain. In sharp contrast, as detailed in the cumulative
equity curves in Figure 1 (Left), models with comparatively
lower general evaluation scores demonstrated significantly
stronger market adaptability. DeepSeek-V3 achieved the
highest cumulative return of +14.2% ($11,420.3), signifi-
cantly outperforming both the market baseline and its higher-
scoring counterparts.
This divergence suggests a critical transfer barrier, where
current generalist metrics fail to capture the nuances of finan-
cial intelligence-specifically the ability to synthesize noisy,
non-stationary signals into profitable decisions. This finding
exposes a fundamental gap in current evaluation paradigms:
the proficiency to solve static problems is decoupled from
the agency required to execute rigorous financial logic under
uncertainty.
2.3. Deconstructing the Divergence: Consensus Bias and
Reasoning Fragmentation
To diagnose the underlying mechanisms of the “Capabilities-
Performance Paradox”, we conduct a retrospective analysis
of the trading period and identify four pivotal market events
that exerted the key influence on U.S. market.
• Hawkish Minutes & Nvidia Volatility (Nov. 19–20,
2025):Hawkish FOMC minutes dampened rate cut
hopes, coinciding with a reversal in Nvidia stock. The
superposition of fading liquidity support and reignited
AI valuation fears triggered a sharp sell-off.
• Fed Delivers Hawkish Cut (Dec. 9, 2025):The Fed
delivered a widely expected 25 basis point cut with
only one cut for 2026. The lack of a fresh positive
catalyst triggered a “sell-the-news” dynamic with sub-
sequent market adjustment.
• CPI Surprise Cools Anxiety (Dec. 18, 2025):Novem-
ber CPI cooled to 2.7% (3% forecast), reigniting ex-
pectations for further rate cuts. This data thoroughly
eliminated market tension, acting as the catalyst for a
sustained subsequent rally.
• Post-Correction Rebound (Jan. 2, 2026):Year-end
profit-taking and selling pressure were fully digested,
forming a consensus around a soft landing. This re-
newed optimism launched a fresh rally to start the year.
By decomposing the aforementioned turning points and the
timeline, we observed that while the broader market (SPY)
reacted dynamically to these pivotal events, models like
GPT-5 and Claude-Sonnet-4.5 failed to correctly interpret
the signal, resulting in flatlining performance.
Initially, the homogenous drawdowns observed during the
“Hawkish Minutes & Nvidia V olatility” phase suggest a
shared baseline risk sensitivity across all agents. However,
a significant bifurcation emerged during the subsequent
market rally. Claude-Sonnet-4.5 and GPT-5 executed a pre-
mature risk-off rotation—effectively liquidating positions
during the transient shock—thereby failing to capture the
ensuing liquidity-driven upside.
3

INVESTLOGICBENCH2026
Specific inefficiencies were observed in GPT-5, which in-
curred a maximum drawdown exceeding the SPY bench-
mark following the “Fed Hawkish Cut”. Crucially, it failed
to re-enter the market effectively during the “CPI Surprise”
and “Post-Correction Rebound” phases. In contrast, despite
Qwen3-Max suffering a comparable drawdown, it exhibited
a rapid recovery dynamic, repairing losses immediately as
market sentiment shifted. Notably, DeepSeek-V3 displayed
advanced strategic timing effectively accumulating assets
during the market cooling phase and realizing outsized re-
turns during the recovery.
By comparing the decision traces of LLMs, two fundamen-
tal cognitive failures—Consensus Bias and Reasoning Frag-
mentation—are revealed as the drivers of the capabilities-
performance paradox. Models like GPT-5 and Claude-
Sonnet-4.5 tend to converge toward the statistical mean
of their training data to maximize token likelihood; this
results in merely reproducing priced-in market consensus
rather than generating the variant perception necessary for
alpha. Simultaneously, when confronted with a complex,
non-stationary environment, these agents exhibited Rea-
soning Fragmentation. Overwhelmed by the volume of
exogenous data, they reverted to rigid, myopic thinking
patterns that failed to account for forward-looking dynam-
ics, ultimately missing the pivotal rebound that drove the
benchmark’s outperformance.
2.4. The Human Benchmark: Establishing Expert Logic
Anchors
The divergent performance of LLMs raises a critical ques-
tion: How would human experts perform during this trading
period? To incorporate expert logic, we introduced two
professional investors:
• Bill Miller:The founder of Miller Value Partners,
renowned for his legendary 15-year streak of beating
the S&P 500 (Emulate through the Miller Value Part-
ners Appreciation ETF).
• Cathie Wood:The founder and CEO of ARK In-
vest, who commits to find technologies where declin-
ing costs trigger exponential demand growth (Emulate
through the ARK Innovation ETF).
As illustrated in Figure 1 (Left), human expert portfolios
demonstrated superior resilience and excess return genera-
tion. During critical shocks like the “Hawkish Cut” and the
“Nvidia V olatility”, the experts exhibited counter-cyclical
aggression. Unlike most investors and consensus-following
LLMs, human experts can employ forward-looking reason-
ing to avoid drawdowns and accelerate decisively when
opportunities arise. This allowed them to capture the full
magnitude of the “Post-Correction Rebound” with pleasing
cumulative returns (e.g., Miller at +10% and Wood at +8%).
The deconstruction of experts’ unique decision-making
chains provides critical evidence for understanding the per-
formance deficiencies of LLMs in dynamic gaming scenar-
ios. Deep analysis of this divergence reveals that the expert
advantage stems from variant perception. When the Key
Events occurred, the experts leveraged an independent rea-
soning framework to gather information and identify the
mispricing, whereas LLMs lack this depth of analysis. In-
tegrating human experts’ analysis logic is essential not just
for comparison, but as a diagnostic reference system.
3. The INVESTLOGICBENCH2026 Dataset
3.1. Design and Construction
INVESTLOGICBENCH2026 is constructed from the dy-
namic decision-making processes of influential real-world
investment agents (e.g., major KOLs and fund managers),
whose viewpoints are widely followed and accepted by
substantial investor communities. Its design is built upon
theE →R→D→O investment logic chain, where market
Events(E) informReasoning(R) leading to aDecision(D)
aimed at an profitableOutcome(O). This framework shifts
evaluation from static question-answering to the assessment
of active reasoning required for real-world investing.
The benchmark is built through a four-stage pipeline (Fig. 2):
1) Data Preparationingests multi-source data (e.g., video
commentary, fund reports).2) Agent Logic Processing
employs a dual-channel analysis: (i) extracting explicit in-
vestment logic from the agent’s own verbalized theses and
(ii) using our proprietaryStock Investment Logic (SIL)
Engineto infer implicit logic patterns from an agent’s trad-
ing history, constructing a holistic behavioral profile.3)
RAG-Augmented Verificationensures fidelity by checking
logic based on real-market data including general search
engine, financial database, and event prediction markets
where event contracts are traded (e.g., Polymarket, Kalshi).
4) Benchmark Assemblyintegrates verified decisions with
agent profiles into a structured, queryable knowledge graph.
3.2. Structured Schema
Each data instance is a JSON object containing an
agentProfile and a list of decisions, instantiating
the E→R→D→O chain.
Profile Fieldscharacterize the agent: agentProfile
(personalized investment style and preference), capital
(scale), security (asset classes), and metadata ( name,
link).
Decision Fieldscapture each logic-action triplet:
•date , events: Decision timestamp and catalyst
events.
4

INVESTLOGICBENCH2026
Figure 2. The two-stage construction pipeline of INVESTLOGICBENCH2026. Stage 1 creates a static investor profile by aggregating
multiple data points from a single agent. Stage 2 performs per-decision annotation, which includes a quality control loop where logic is
verified and potentially fed back to refine the profile.
•finLogic : The complete E →R→D chain (e.g.,
’[Event]→[Thesis]→Action: [Action]’).
•investDecision : The executable action (e.g.,
’Long NVDA’).
•investPeriod , endDate: Evaluation horizon and
validation date.
•outcome : The market-validated outcome (e.g.,
’+5.2%’).
•finLogicReview : System-generated post-mortem
analysis.
3.3. Statistics and Tasks
The inaugural version of INVESTLOGICBENCH2026 com-
prises 201,247 annotated investment theses sourced from
151 distinct financial KOLs (data details in Appendix A.1
and B). The statistical summary of the investor profiles,
which underscores the dataset’s focus on real-world, event-
driven strategies, is presented in Table 1.
3.4. Benchmark Tasks
We define three progressive tasks: 1.Logic Com-
prehension: Given agent text, extract and summarize
the finLogic. (Evaluates understanding) 2.Logic
& Thesis Generation: Given current events and an
agentProfile, generate a plausible finLogic and de-
cision. (Evaluates synthetic reasoning) 3.End-to-End
Investment Simulation: According to the investment de-
cisions, the outcome is evaluated with real-world market
data. Both static and dynamic investment actions are evalu-
ated depending on whether the account’s position (holdings)
status is disclosed.
3.5. Automated Evaluation via Judge LLM
A high-capacity LLM (e.g., GPT-5) serves as an automated
judge, scoring outputs based on: -Fidelity: Similarity to
ground-truth agent logic (Task 1). -Coherence & Plausi-
bility: Logical soundness and market relevance (Tasks 2,
3). -Consistency: Adherence to initial style and logical
through-line (Task 3).
4. Empirical Analysis: The Investment Logic
Gap
We evaluate some leading LLMs on INVESTLOG-
ICBENCH2026 using Task 2 (Logic & Thesis Genera-
tion), where models must synthesize an investment thesis
from retrieved market events and an agent profile. Perfor-
mance is measured along two axes: (1)Reasoning Qual-
ity—comprisingEvent Coherence(fidelity to input events)
andLogical Plausibility(internal validity of the E →R→D
chain), and (2)Decision Outcome—comprisingWin Rate
and simulatedTotal Profitover the investment horizon.
4.0.1. CONDITIONALSCORINGFRAMEWORK
The overall score synthesizes reasoning quality and decision
outcome. TheDecision Outcome Scoreis a weighted com-
posite of two critical performance dimensions: the agent’s
absolute profitability and its strategy win rate, each evalu-
ated relative to the human expert benchmark.
First, theProfit Score( Sprofit) is calculated conditionally
based on the agent’s total profit ( Pa) against the human
expert benchmark ( Ph) and a neutral midpoint ( Pm =
5

INVESTLOGICBENCH2026
Figure 3. A working example from the Stock Investment Logic (SIL) Engine. It demonstrates how a specific market event (here, an
antitrust probe announcement by China’s SAMR targeting Nvidia on 2025-09-15) is temporally linked to a security ( NVDA) and
its subsequent price series. The engine structures and stores such Event-Security-Time tuples to form a queryable knowledge base for
inferring recurring investment logic patterns and enriching agent profiles.
Table 1. Statistical Summary of Agent Profiles in INVESTLOG-
ICBENCH2026
Category Statistics
Total Investment Experts 151
Total Annotated Decisions 201,247
Avg. Decisions per KOL 1332.8
Avg. Decisions per fund agent 2.5
Primary Style (agentProfile)
- Event-Driven 102 (67.5%)
- Long-Term Value 16 (10.6%)
- Technical 8 (5.3%)
- Macro 30 (19.9%)
Capital Scale (capital)
- Below $1M 19 (12.6%)
- $1M - $10M 41 (27.2%)
- $10M - $100M 74 (49.0%)
- Above $100M 17 (11.3%)
Primary Security Type (security)
- Equity 42 (27.8%)
- Options 16 (10.6%)
- Futures/Commodities 6 (4.0%)
- ETF 15 (9.9%)
-Others/Combined 72 (47.7%)
Primary Sample Type
- Event-driven decisions 94.0%
- Forward-looking event predictions 3.0%
Web-verifiable 2.9%
Prediction-market verified 0.1%
- Technical/quantitative analysis 3.0%
max(0, Ph)):
Sprofit =



5.0,ifP a ≥P h
5.0× Pa −P m
Ph −P m
,ifP m ≤P a < Ph
5.0× Pa
Pm
,if0≤P a < Pm
0.0,ifP a <0
Second, theWin Rate Score( Swin) measures the consistency
of positive returns. The agent’s win rate (Wa) is compared
to the human’s (Wh):
Swin =



5.0,ifW a ≥W h
5.0× Wa
Wh
,ifW a < Wh
The finalDecision Outcome Scoreis the weighted sum of
these components, emphasizing absolute profit:
Soutcome = 0.7×S profit + 0.3×S win
TheReasoning Quality Scoreremains the average of its
Event Coherence(EC) andLogical Plausibility(LP), each
on a 5-point scale:S reasoning = (SEC +S LP)/2.
The finalOverall Scoreis the sum of the reasoning and
outcome scores, providing a balanced assessment on a 0-10
6

INVESTLOGICBENCH2026
scale:
Soverall =S reasoning
| {z }
(0–5)
+S outcome| {z }
(0–5)
This composite metric ensures a robust and multidimen-
sional evaluation of an LLM’s investment logic, equally
valuing the quality of its reasoning process and the practical
efficacy of its decisions.
4.0.2. EVALUATIONRESULTS
As shown in Table 2, four of the five evaluated models ex-
ceeded the expert profitability benchmark, each earning a
perfect outcome score. This indicates that LLMs can gen-
erate financially effective decisions. However, their reason-
ing quality scores show significant variance, with notable
weaknesses in event grounding. The results confirm that
achieving profitability does not guarantee logically coherent
or well-explained investment theses, highlighting a key area
for future improvement.
4.1. Case Study: Event-Driven Reasoning Failure
We present a simulated case where an agent correctly pre-
dicted a rally in semiconductor stocks. The agent’s logic
wove together nuanced observations from earnings call tran-
scripts, industry capacity reports, and geopolitical news.
When leading LLMs were provided the same raw event
data, they either fixated on the most headline-grabbing news
piece, produced a generic ”strong demand” summary, or
generated internally contradictory statements. This case
exemplifies theevent-noise discriminationandintegrative
reasoningdeficits of current models.
Figure 4 illustrates a simulated event-driven investment sce-
nario where Cathie Wood correctly predicted a rally in semi-
conductor stocks by integrating nuanced observations from
multiple data sources. In contrast, LLMs exhibit systematic
reasoning failures when provided the same raw event data.
Key Observations:
(1) Human experts excel atintegrative reasoning, weav-
ing together earnings call transcripts, industry capacity
reports, and geopolitical news into a coherent invest-
ment thesis.
(2) LLMs display poorevent-noise discrimination, either
fixating on headline-grabbing news (e.g., government
shutdown) or producing generic summaries lacking
specificity.
(3) The quantitative evaluation reveals a 25.7% gap in
overall logic quality and a 2.2-point deficit in noise
discrimination between human experts and the best-
performing LLM (Claude-4.5-Sonnet).
Implications:This case exemplifies the core limitations
KOL/Models Event Reasoning Decision Outcome
Cathie Wood
U.S. government
shutdown, ADP payroll
report shows job losses,
Fed cuts interest rates
Cooling labor market→Safe-haven
demand
Shutdown and weak ADP indicate
uncertainty, supporting safe-haven
assets
Buy:GLD
50%, TLT
50%(Short-term
20251231)
+3.53%
DeepSeek V3
LDP elects Sanae
Takaichi as leader, Japan
stocks rally on policy
hopes, Fed cuts rates
Pro-stimulus fiscal→Equity boost
+ Yen depreciation
Takaichi’s policies boost Japanese
equities and depreciate Yen
Buy:TOPIX
(513800¥) +2.44%
Claude-4.5
Japan’s LDP elected
Takaichi, Apple
increased iPhone 17
production, US new
tariffs
Pro-stimulus shift→Bullish but
tariff risk
Loose monetary stance vs tariff fears
lead to defensive positioning
Buy:TOPIX
(Short-term
20251018)
+0.70%
GPT-5
Japan’s LDP elects
Takaichi, Apple increases
production, U.S. funding
market stress
Stimulus hope→Conflated signals
Ignored funding stress, mixed with
unrelated Apple noise
Buy:TOPIX
(Short-term
20251011)
-15.67%
Qwen3 Max
China-Bangladesh 50th
anniversary, Jiaolong
Arctic dive, Pinglu Canal
progress
Infrastructure milestone→
Logistics benefit
Pinglu Canal 65% completion benefits
Western Land-Sea Passage
Buy:
000582.SZ¥ +11.23%
Figure 4. Decomposing theInvestment Logic Gap: A com-
parative case study of investment reasoning across the
P→E→R→D→O chainbetween a human expert (Cathie Wood)
and LLMs instantiated with her agent profile. The analysis focuses
on the market event cluster of October 4, 2025 with empty starting
position, and the performance divergence is substantial: the expert
returned +3.53%, the best LLM (Qwen) +11.23%, and the worst
LLM (GPT) -15.67%, resulting in a 26.9% LLM performance gap.
According to the table, LLMs exhibit significantly divergent invest-
ment logic and outcome. We use ¥ to present security code from
Chinese financial market. Notably, the distinct geographical bias
in asset recommendations across different LLMs reflects inherent
market preferences shaped by their training data.
identified by INVESTLOGICBENCH2026: LLMs struggle
to distinguish signal from noise and fail to maintain logical
consistency across multiple data sources, explaining their
underwhelming performance in live trading environments
despite strong performance on static financial benchmarks.
5. Related Work
LLM evaluation in finance has followed two main tracks:
static benchmarkstesting analytical knowledge, anddy-
namic agent frameworksmeasuring trading performance.
However, a critical gap remains in evaluating theinvestment
reasoning processitself—the logical synthesis of unstruc-
tured events into actionable theses. Recent studies expose
temporal awareness failures and other reasoning limitations
(Sehgal et al., 2026), underscoring the need for process-
centric evaluation. INVESTLOGICBENCH2026 addresses
this gap by introducing the first benchmark grounded in ex-
plicitP →E→R→D→Odecision chains, enablingprocess-
diagnosticassessment of investment logic.
5.1. Static Benchmarks: Knowledge and Analysis
Early work evaluates LLMs as analysts through static QA
and numerical reasoning. FinQA (Chen et al., 2022) and
TAT-QA (Zhu et al., 2021) require multi-step reasoning over
7

INVESTLOGICBENCH2026
Table 2.Comprehensive Evaluation of LLMs on INVESTLOGICBENCH2026
Model Reasoning Quality Decision Outcome Overall Score /10
Event Coherence (/5) Logical Plausibility (/5) Win Rate Total Profit
DeepSeek-V3 2.8 4.1 72% +16.7% 7.8
Qwen3-Max 0.8 4.2 51% +7.7% 5.7
Claude-4.5 2.2 3.9 46% +5.4% 5.3
GPT-5 1.8 4.1 40% +3.8% 3.1
Note: Logical Plausibility evaluates the coherence of the E→R→D chain. Total Profit is the average return of each outcome.
financial reports and hybrid tabular-textual content. Sub-
sequent benchmarks expand scope: FinanceBench (Islam
et al., 2023) tests open-domain QA on SEC filings, while
BizBench (Koncel-Kedziorski et al., 2024) reframes busi-
ness problems as quantitative tasks. Comprehensive suites
like FinBen (Xie et al., 2024) aggregate these tasks.
The key limitation isretrospective analysisof given in-
formation. As noted by Ding et al. (2024), strong perfor-
mance reflects calculation proficiency but notprospective
decision-makingunder uncertainty—the core investor func-
tion. This limitation persists even in specialized models
like BloombergGPT (Wu et al., 2023) and FinGPT (Yang
et al., 2023), which remain predominantly evaluated on
static benchmarks.
5.2. Dynamic Agents: Real-World Performance
Recent work shifts from evaluating models as tools to as-
sessing them as autonomousagentsin simulated or live
markets. This paradigm prioritizes outcome-based metrics
(P&L). Frameworks like FinDABench (Liu et al., 2024)
and XFinBench (Zhang et al., 2025) place LLM agents in
complex financial problem-solving environments. Fully au-
tonomous arenas such as AI-Trader (Fan et al., 2025) and
DeepFund (Li et al., 2025) use real-time data with actual
capital, providing high ecological validity. Architecturally,
this space features multi-agent systems (Yu et al., 2024) and
diverse agent-based modeling approaches (Gao et al., 2023).
While crucial for end-to-end stress-testing, these approaches
are fundamentallyoutcome-opaque. They indicatewhether
an agent profits but notwhy. Profitable trades may stem
from sound logic or noise; losses may reflect poor strat-
egy or black-swan events. This black-box nature hinders
targeted improvement and obscures the root cause of the
“Capabilities-Performance Paradox” (Ding et al., 2024).
5.3. Bridging the Gap: Process-Diagnostic Evaluation
To address these limitations, recent work diagnoses spe-
cific reasoning failures. Look-ahead bias remains a critical
challenge, causing performance decay under point-in-time
constraints. Complementary studies examine temporal rea-
soning under pressure (Sehgal et al., 2026) and advanced
market analysis using LLM agents (Fatouros et al., 2025).
Most pertinent is theChain-of-Decisionframework by
Chen et al. (2024), which argues that modeling professional
decisions requires distilling explicit intermediate reason-
ing steps between information intake and actions. This
directly informs ourP →E→R→D→Oschema. However,
their work focuses on report generation rather than the full
investment cycle encompassing decision, action, and market-
validated outcome.
Unlike prior work measuring input knowledge or output per-
formance, we evaluate thereasoning chainconnecting them
by (1)grounding evaluation in real expert decision trails,
(2)assessing logical coherence independent of P&L, and
(3)enabling style-conditioned diagnosis. This provides
the substrate to quantify the investment logic gap and align
models toward robust, interpretable, expert-aligned financial
reasoning.
6. Conclusion
This paper identifies the absence of benchmarks forprac-
tical investment logic—the reasoning chain—as a funda-
mental obstacle to the development of investment-oriented
agents. We introduce INVESTLOGICBENCH2026, the first
benchmark constructed from the event-driven reasoning
traces of real-world investors. It provides structured, val-
idated data to evaluate an LLM’s ability to formulate and
maintain coherent investment theses. Our analysis confirms
a significantinvestment logic gap: state-of-the-art LLMs fail
to match the nuanced, contextual reasoning of human ex-
perts, explaining their poor performance in live trading. This
reproducible benchmark shifts the evaluation paradigm from
passive knowledge recall to active reasoning. It lays the es-
sential foundation for future work in training logic-aligned
models and architecting personalized, market-aligned in-
vestment agents.
8

INVESTLOGICBENCH2026
7. Impact Statement
This work introduces INVESTLOGICBENCH2026, a bench-
mark designed to advance machine learning by evaluating
the core capability of dynamic, sequential reasoning under
uncertainty—essential for developing reliable autonomous
agents in finance.
By shifting evaluation from opaque performance metrics
to the diagnosis of reasoning quality, the benchmark facil-
itates the development of trustworthy, interpretable, and
logically sound AI systems. It serves as a foundational step
toward transparent and accountable decision-making AI,
with broader implications for improving financial decision-
support tools.
References
Chung-Chi Chen, Hiroya Takamura, Ichiro Kobayashi,
and Yusuke Miyao. Distilling analysis from genera-
tive models for investment decisions.arXiv preprint
arXiv:2410.07225, 2024. URL https://arxiv.or
g/abs/2410.07225.
Zhiyu Chen, Wenhu Chen, Charese Smiley, Sameena
Shah, Iana Borova, Dylan Langdon, Reema Moussa,
Matt Beane, Ting-Hao Huang, Bryan Routledge, and
William Yang Wang. FinQA: A dataset of numer-
ical reasoning over financial data.arXiv preprint
arXiv:2109.00122, 2022. URL https://arxiv.or
g/abs/2109.00122.
Han Ding, Yinheng Li, Junhao Wang, and Hang Chen.
Large language model agent in financial trading: A sur-
vey.arXiv preprint arXiv:2408.06361, 2024. URL
https://arxiv.org/abs/2408.06361.
Tianyu Fan, Yuhao Yang, Yangqin Jiang, Yifei Zhang,
Yuxuan Chen, and Chao Huang. AI-trader: Bench-
marking autonomous agents in real-time financial mar-
kets.arXiv preprint arXiv:2512.10971, 2025. URL
https://arxiv.org/abs/2512.10971.
George Fatouros, Kostas Metaxas, John Soldatos, and
Manos Karathanassis. MarketSenseAI 2.0: Enhanc-
ing stock analysis through LLM agents.arXiv preprint
arXiv:2502.00415, 2025. URL https://arxiv.or
g/abs/2502.00415.
Chen Gao, Xiaochong Lan, Nian Li, Yuan Yuan, Jingtao
Ding, Zhilun Zhou, Fengli Xu, and Yong Li. Large
language models empowered agent-based modeling and
simulation: A survey and perspectives.arXiv preprint
arXiv:2312.11970, 2023. URL https://arxiv.or
g/abs/2312.11970.
Pranab Islam, Anand Kannappan, Douwe Kiela, Rebecca
Qian, Nino Scherrer, and Bertie Vidgen. FinanceBench:
A new benchmark for financial question answering.arXiv
preprint arXiv:2311.11944, 2023. URL https://ar
xiv.org/abs/2311.11944.
Rik Koncel-Kedziorski, Michael Krumdick, Viet Lai,
Varshini Reddy, Charles Lovering, and Chris Tanner.
BizBench: A quantitative reasoning benchmark for busi-
ness and finance.arXiv preprint arXiv:2311.06602, 2024.
URLhttps://arxiv.org/abs/2311.06602.
Changlun Li, Yao Shi, Yuyu Luo, and Nan Tang. Will
LLMs be professional at fund investment? DeepFund: A
live arena perspective.arXiv preprint arXiv:2503.18313,
2025. URL https://arxiv.org/abs/2503.1
8313.
Shu Liu, Shangqing Zhao, Chenghao Jia, Xinlin Zhuang,
Zhaoguang Long, Jie Zhou, Aimin Zhou, Man Lan, and
Yang Chong. FinDABench: Benchmarking financial data
analysis ability of large language models. InProceedings
of the International Conference on Computational Lin-
guistics, 2024. URL https://api.semanticsc
holar.org/CorpusID:266844370.
Neil K. R. Sehgal, Sharath Chandra Guntuku, and Lyle
Ungar. Real-time deadlines reveal temporal awareness
failures in LLM strategic dialogues.arXiv preprint
arXiv:2601.13206, 2026. URL https://arxiv.or
g/abs/2601.13206.
Shijie Wu, Ozan Irsoy, Steven Lu, Vadim Dabravolski, Mark
Dredze, Sebastian Gehrmann, Prabhanjan Kambadur,
David Rosenberg, and Gideon Mann. BloombergGPT:
A large language model for finance.arXiv preprint
arXiv:2303.17564, 2023. URL https://arxiv.or
g/abs/2303.17564.
Qianqian Xie, Weiran Wang, Zhenyu Chen, Ruoyu Xiang,
Xiao Zhang, Yansong Deng, et al. Finben: A holistic
financial benchmark for large language models. InAd-
vances in Neural Information Processing Systems 38
(NeurIPS 2024), 2024. doi: 10.52202/079017-3033.
URL https://proceedings.neurips.cc/p
aper_files/paper/2024/hash/adb1d9fa8
be4576d28703b396b82ba1b-Abstract-Dat
asets_and_Benchmarks_Track.html.
Hongyang Yang, Xiao-Yang Liu, and Christina Dan Wang.
FinGPT: Open-source financial large language models.
arXiv preprint arXiv:2306.06031, 2023. URL https:
//arxiv.org/abs/2306.06031.
Yangyang Yu, Zhiyuan Yao, Haohang Li, Zhiyang Deng,
Yuechen Jiang, Yupeng Cao, Zhi Chen, Jordan W. Su-
chow, Zhenyu Cui, Rong Liu, Zhaozhuo Xu, Koduvayur
Subbalakshmi, Guojun Xiong, Yueru He, Jimin Huang,
Dong Li, and Qianqian Xie. FinCon: A synthesized LLM
9

INVESTLOGICBENCH2026
multi-agent system with conceptual verbal reinforcement
for enhanced financial decision making. InAdvances
in Neural Information Processing Systems, volume 38,
2024.
Zhihan Zhang, Yixin Cao, and Lizi Liao. XFinBench:
Benchmarking LLMs in complex financial problem solv-
ing and reasoning.arXiv preprint arXiv:2508.15861,
2025. URL https://arxiv.org/abs/2508.1
5861.
Fengbin Zhu, Wenqiang Lei, Youcheng Huang, Chao Wang,
Shuo Zhang, Jiancheng Lv, Fuli Feng, and Tat-Seng Chua.
TAT-QA: A question answering benchmark on a hybrid
of tabular and textual content in finance.arXiv preprint
arXiv:2105.07624, 2021. URL https://arxiv.or
g/abs/2105.07624.
10

INVESTLOGICBENCH2026
A. Appendix
A.1. KOL Sample Construction and Measurement Notes
This appendix documents a curated sample of YouTube-based key opinion leaders (KOLs) for descriptive comparison of
investment-logic-orientedcontent. Channels are selected based on whether their content primarily articulatesgeneralizable
decision frameworks(e.g., macro–industry–firm reasoning pipelines; valuation, risk management, and portfolio construction
principles; cycle and sentiment indicators; and rule-based trading systems), as opposed to predominantly event-driven or
news-reactive commentary. The resulting sample covers multiple market segments (equities/funds/macro, options and
trading education, and crypto/Web3), enabling cross-domain characterization of audience scale and content supply.
As shown in Table 3,Subscribersis used as a coarse proxy for audience size, andVideosreflects cumulative content
output and, to a limited extent, channel maturity. Both measures are time-varying; thus, the table should be interpreted
as a descriptive snapshot rather than a fixed ground-truth record. For subsequent quantitative analyses, we recommend
re-scraping and freezing all statistics within a single, pre-specified time window to ensure comparability.
Table 3:Statistics of Selected KOL Creators
Name Description Subscribers Videos
Cathie Wood Investment strategist, founder of ARK Invest 619K 743
Zip Trader (Charlie) Day trading and swing trading education 857 819
Stock Moe Stock and crypto trading strategies 714K 897
Data Dispatch Market data and analytics insights 28.4K 611
Paul Thomas Investing Penny stocks and growth investment analysis 57.4K 478
Stas Talks Stocks Stock market discussion and analysis 61.6K 4283
Lark Davis Crypto investment strategies 638K 4936
Miles Deutscher Cryptocurrency analysis and portfolio strategies 224K 2284
Financial Education Investing education 911K 2800
Everything Money Investing 376K 3019
Joseph Carlson Show Investing 499K 449
Learn to Invest Investing basics 289K 597
Sven Carlin Value investing 263K 2176
New Money Finance commentary 1090K 415
Tom Nash Market analysis 572K 880
Chicken Genius Singapore Singapore investing 249K 249
Ticker Symbol YOU Investing 572K 382
Jimmy Dividend Investing Dividend investing 289K 597
TraderTV Live Professional live market trading sessions 550K 6315
The Plain Bagel Animated financial education 1140K 263
The Compound Casual market commentary 223K 1885
Seeking Alpha Fundamental stock analysis 32.7K 947
Patrick Boyle Academic finance perspective 1100K 460
Option Alpha Systematic options trading education 296K 862
NaNa Talks US Stocks Chinese-language US stock analysis 301K 1573
Morningstar Fund analysis and long-term strategies 129K 2956
Money or Life Financial freedom philosophy 71.8K 217
11

INVESTLOGICBENCH2026
Name Description Subscribers Videos
Investopedia Financial dictionary and concepts 298K 545
Investor’s Business Daily CAN SLIM investing system 169K 4961
Hedgeye Macroeconomic analysis 78.3K 4131
Coin Bureau Comprehensive cryptocurrency education 2730K 1773
The Defiant DeFi and Web3 news and analysis 131K 1346
Unchained Blockchain and crypto industry insights 6770K 1649
Crypto Casey Beginner-friendly cryptocurrency education 678K 875
The Maverick of Wall Street Alternative investment strategies 146K 1686
Larry Jones Stocks and crypto analysis for entrepreneurs 691K 2154
Meet Kevin Real estate and financial independence education 2050K 6095
Graham Stephan Personal finance and real estate investing 5140K 1402
Mark Moss Economic trends and investment strategies 803K 1365
Real Vision In-depth financial markets analysis 89.7K 1210
Garys Economics Economic analysis and market commentary 1520K 369
Let’s Talk Money! Personal finance education and tips 738K 1199
ClearValue Tax Tax strategies and financial planning 2820K 151
Kitco NEWS Precious metals market news and analysis 750K 4818
12

INVESTLOGICBENCH2026
B. Appendix: KOL Resources
B.1. KOL Channel URLs and Reproducibility
To support reproducibility and facilitate follow-up analyses, Table 4 provides the canonical channel URLs for the curated KOL sample
reported in Table 3. These links enable consistent access to each source and allow downstream data collection (e.g., channel metadata,
upload cadence, topical coverage, and representative playlists) under a fixed protocol. In empirical settings where platform statistics and
content inventories evolve over time, anchoring the sample with persistent URLs is essential for re-scraping within a pre-specified time
window and ensuring that subsequent measurements remain comparable across runs.
Table 4:List of KOL Channels and URLs
KOL Name Channel URL
Cathie Woodhttps://www.youtube.com/@ARKInvest2015
Financial Educationhttps://www.youtube.com/@FinancialEducation
Everything Moneyhttps://www.youtube.com/@EverythingMoney
Joseph Carlson Showhttps://www.youtube.com/@JosephCarlsonShow
Learn to Investhttps://www.youtube.com/@LearnToInvest
Sven Carlinhttps://www.youtube.com/c/InvestwithSvenCarlinPhD
New Moneyhttps://www.youtube.com/@NewMoneyYouTube
Tom Nashhttps://www.youtube.com/@TomNashTV
Chicken Genius Singaporehttps://www.youtube.com/@ChickenGeniusSingapore
Ticker Symbol YOUhttps://www.youtube.com/@TickerSymbolYOU
Jimmy Dividend Investinghttps://www.youtube.com/@JimmyDividend
TraderTV Livehttps://www.youtube.com/c/TraderTVLive
The Plain Bagelhttps://www.youtube.com/c/ThePlainBagel
The Compoundhttps://www.youtube.com/@TheCompoundNews
Seeking Alphahttps://www.youtube.com/c/SeekingAlpha
Patrick Boylehttps://www.youtube.com/c/PatrickBoyleOnFinance
Option Alphahttps://www.youtube.com/c/OptionAlpha
NaNa Talks US Stockshttps://www.youtube.com/@NaNaShuoMeiGu
Morningstarhttps://www.youtube.com/@morningstar
Money or Lifehttps://www.youtube.com/@Money_or_Life
Investopediahttps://www.youtube.com/c/Investopedia
Investor’s Business Dailyhttps://www.youtube.com/c/InvestorsBusinessDaily
Hedgeyehttps://www.youtube.com/user/Hedgeye
Zip Trader (Charlie)https://www.youtube.com/c/ziptrader
Stock Moehttps://www.youtube.com/channel/UCoMzWLaPjDJBbipihD694
pQ
Data Dispatchhttps://www.youtube.com/@DataDispatch
Paul Thomas Investinghttps://www.youtube.com/c/PaulThomasInvesting
Stas Talks Stockshttps://www.youtube.com/@StasTalksStocks
Lark Davishttps://www.youtube.com/@TheCryptoLark
Miles Deutscherhttps://www.youtube.com/@MilesDeutscher
Coin Bureauhttps://www.youtube.com/@CoinBureau
The Defianthttps://www.youtube.com/@TheDefiant
13

INVESTLOGICBENCH2026
KOL Name Channel URL
Unchainedhttps://www.youtube.com/@UnchainedOff
Crypto Caseyhttps://www.youtube.com/@CryptoCasey
The Maverick of Wall Streethttps://www.youtube.com/@TheMaverickofWallStreet
Larry Joneshttps://www.youtube.com/c/STOCKUPwithLarryJones
Meet Kevinhttps://www.youtube.com/@MeetKevin
Graham Stephanhttps://www.youtube.com/@GrahamStephan
Mark Mosshttps://www.youtube.com/@1MarkMoss
Real Visionhttps://www.youtube.com/@RealVisionFinance
Garys Economicshttps://www.youtube.com/@garyseconomics
Let’s Talk Money!https://www.youtube.com/@josephhogue
ClearValue Taxhttps://www.youtube.com/@clearvaluetax9382
Kitco NEWShttps://www.youtube.com/@kitco
14

INVESTLOGICBENCH2026
C. Appendix:KOL Fund Reference Tabless
C.1. Institutions, Fund Managers, and Morningstar Ratings
Table 5 reports a compact snapshot of the fund universe by listing each record’s institution (fund firm), fund manager(s), fund name, and
the Morningstaroverallstar rating. We include the star rating as a standardized, coarse descriptor of historical risk-adjusted performance
within a fund’s peer group, and use it strictly for descriptive comparison rather than causal interpretation. Because manager assignments
and ratings may change over time, the table should be interpreted as a snapshot tied to the data extraction window.
Table 5:Institutions, Fund Managers, Fund Names, and Morningstar Overall Ratings
Institution (Firm) Fund Manager(s) Fund Name MS Rating
Aegis Scott L. Barbee Aegis Value I 5
Alger Patrick Kelly, Ankur Crawford Alger Focus Equity Y 5
Alger Gregory S. Adams Alger Growth & Income Z 4
Allspring Global
Investments
Justin P. Carr, Robert M. Wicentowski Allspring Disciplined US Core R6 5
Allspring Global
Investments
John R. Campbell, Vincent Fioramonti Allspring Large Cap Core R6 5
Gotham Joel Greenblatt, Robert Goldstein Gotham Index Plus Institutional 5
American Century
Investments
Keith Lee, Jeffrey R. Bourke, Tong Li American Century U.S. Equity Focus I 3
BNY Mellon Peter D. Goslin BNY Mellon Appreciation Instl 5
Ave Maria Mutual
Funds
George P. Schwartz, Timothy S.
Schwartz
Ave Maria Rising Dividend I 5
V ALIC Jeffrey D. Parker, Brian Demain,
Philip Cody White
V ALIC Company I International Growth 5
WesMark Douglas C. Robertson WesMark Small Cap I 4
Wasatch Garrett S. Lamb, Sean A. Schaub Wasatch Small Cap Value Inst 4
Hood River Capital
Management
Michael J. Delf, John H. Beck Hood River Small-Cap Growth I 5
GMO Ben Inker, Jeremy Grantham GMO Quality Fund III 5
Leavell Thomas A. Rowe, Ryan T. Leavell Leavell Investment Counsel Mid Cap Growth 5
SEI SEI Investments Management
Corporation
SEI Large Cap Growth Instl (SIMT) 4
T. Rowe Price Larry J. Puglia T. Rowe Price Blue Chip Growth I 4
T. Rowe Price Justin P. White T. Rowe Price Growth Stock I 4
T. Rowe Price Brian W. Berghuis T. Rowe Price Mid-Cap Growth I 4
T. Rowe Price Brian C. Rogers T. Rowe Price Equity Income I 4
BlackRock Robert R. Shillito, Michael C.
Clemente
BlackRock Advantage Small Cap Core Instl 4
BlackRock Tony DeSpirito, John M. H. Lawler,
Kevin B. Winkler
BlackRock Global Equity Instl 4
BlackRock Tony DeSpirito, John M. H. Lawler,
Kevin B. Winkler
BlackRock Mid-Cap Growth Equity Instl 4
BlackRock Tony DeSpirito, John M. H. Lawler,
Kevin B. Winkler
BlackRock Small Cap Growth Equity Instl 4
Franklin Templeton
Investments
David M. Winters, Todd Brighton Franklin Small Cap Growth Adv 4
Copley Jeffrey M. Fischer, Benjamin W. Hall Copley Focus Equity Institutional 4
Hotchkis & Wiley Daniel G. Hotchkis, Shannon P. Kress Hotchkis & Wiley Value Opportunities I 4
Independent Franchise
Partners
Andrew L. Moffett, David W. Potter Independent Franchise Partners US Equity I 4
Fidelity Investments Will Danoff Fidelity Contrafund K6 5
Fidelity Investments Joel P. Tillinghast Fidelity Low-Priced Stock K6 4
Fidelity Investments Geode Capital Management Fidelity Total Market Index 4
15

INVESTLOGICBENCH2026
Institution (Firm) Fund Manager(s) Fund Name MS Rating
Dodge & Cox Dodge & Cox Dodge & Cox Income 4
Dodge & Cox Dodge & Cox Dodge & Cox Stock 4
ClearBridge Investments David C. Kupfer, Peter W. Fondren ClearBridge Large Cap Growth IS 4
ClearBridge Investments Robert E. Taylor, John D. Freeman ClearBridge Large Cap Value IS 4
Cohen & Steers Joseph M. Harvey, Jason T. Yablon Cohen & Steers Realty Shares Instl 3
Columbia Threadneedle
Investments
James P. Tierney Columbia Seligman Global Technology Instl 2 5
Dimensional Fund
Advisors
Dimensional Fund Advisors DFA Emerging Markets Core Equity I 4
Dimensional Fund
Advisors
Dimensional Fund Advisors DFA International Core Equity I 4
Dimensional Fund
Advisors
Dimensional Fund Advisors DFA US Core Equity 1 I 4
Invesco Amit D. Kumar Invesco Developing Markets Instl 3
J.P. Morgan Clare H. Hart, Michael D. Marini JPMorgan Equity Income R6 4
J.P. Morgan Jonathan D. Simon, Jennifer L.
Williams
JPMorgan Large Cap Growth R6 4
MFS Investment
Management
Kevin D. Clark, Joseph Flaherty MFS Growth R6 4
MFS Investment
Management
Robert M. Zito, James H. LeBoeuf MFS Value R6 4
PIMCO Scott A. Mather, Esteban J. Burbano PIMCO Total Return Instl 3
Principal William R. Bowen, Allen E. Jackson Principal MidCap R6 4
Charles Schwab Schwab Equity Ratings Schwab S&P 500 Index 4
Artisan Partners David Samra, Kiki P. Pillai Artisan Developing World Instl 4
Artisan Partners Benjamin Herrick, David Samra, Kiki
P. Pillai
Artisan International Value Instl 4
Baron Capital Ronald Baron, Michael J. Lippert Baron Partners Instl 4
Baron Capital Ronald Baron, Michael T. Sheehy,
Neal E. Clark
Baron Small Cap Instl 4
Vanguard Vanguard Equity Index Group Vanguard 500 Index Admiral 4
Vanguard Donald M. Kilbride, Michael D.
Reckmeyer
Vanguard Dividend Growth Investor 4
Vanguard Vanguard Equity Index Group Vanguard Extended Market Index Admiral 4
Vanguard Vanguard Equity Index Group Vanguard FTSE All-World ex-US Index Admiral 4
Vanguard Vanguard Equity Index Group Vanguard Growth Index Admiral 4
Vanguard Vanguard Equity Index Group Vanguard Small-Cap Index Admiral 4
Vanguard Vanguard Equity Index Group Vanguard Total Stock Market Index Admiral 4
Vanguard Vanguard Equity Index Group Vanguard Value Index Admiral 4
Vanguard John T. Keogh, Thomas J. Martin Vanguard Wellington Investor 4
Vanguard John T. Keogh, Thomas J. Martin Vanguard Windsor II Investor 4
Vanguard John T. Keogh, Thomas J. Martin Vanguard Windsor Investor 4
Vanguard John T. Keogh, Thomas J. Martin Vanguard Wellesley Income Investor 4
Vanguard Vanguard Equity Index Group Vanguard World Stock Index Investor 4
16

INVESTLOGICBENCH2026
C.2. Fund Managers and Trailing Return Metrics
Table 6 reports a compact summary of each fund’s manager(s) and trailing performance metrics. We useTR 1Yto denote the trailing
one-year total return, andTR 3Y/TR 5Yto denote the annualized total returns over the trailing three- and five-year horizons, respectively.
These values are time-varying and should be interpreted as a descriptive snapshot tied to the data extraction window.
Table 6:Fund Managers and Trailing Returns
Fund Name Manager(s) 1Y 3Y 5Y
Aegis Value I S. Barbee 29.37% 16.90% 24.01%
Alger Focus Equity Y P. Kelly, A. Crawford 51.38% 32.67% 19.60%
Alger Growth & Income Z G. Adams 14.82% 16.25% 16.23%
Allspring Disciplined US Core R6 J. Carr, R. Wicentowski 18.56% 18.61% 17.29%
Allspring Large Cap Core R6 J. Campbell, V . Fioramonti 19.50% 19.34% 17.89%
Allspring Special Small Cap Value R6 J. Campbell, V . Fioramonti 16.06% 12.17% 12.77%
American Funds Washington Mutual R6 M. Pacheco, K. Martell, B. Reick 10.84% 10.86% 10.71%
Artisan Developing World Instl D. Samra, K. Pillai 10.61% 5.73% 7.13%
Artisan International Value Instl B. Herrick, D. Samra, K. Pillai 9.68% 6.28% 10.21%
Baron Partners Instl R. Baron, M. Lippert 37.09% 17.08% 19.25%
Baron Small Cap Instl R. Baron, M. Sheehy, N. Clark 17.52% 10.71% 12.45%
BlackRock Advantage Small Cap Core Instl R. Shillito, M. Clemente 17.89% 10.62% 11.57%
BlackRock Global Equity Instl T. DeSpirito, J. Lawler, K. Winkler 24.73% 12.81% 13.42%
BlackRock Mid-Cap Growth Equity Instl T. DeSpirito, J. Lawler, K. Winkler 33.92% 15.86% 15.05%
BlackRock Small Cap Growth Equity Instl T. DeSpirito, J. Lawler, K. Winkler 26.72% 10.76% 10.50%
ClearBridge Large Cap Growth IS D. Kupfer, P. Fondren 35.58% 15.01% 13.90%
ClearBridge Large Cap Value IS R. Taylor, J. Freeman 11.51% 10.48% 10.64%
Cohen & Steers Realty Shares Instl J. Harvey, J. Yablon 6.58% 1.68% 4.91%
Columbia Seligman Global Technology Instl 2 J. Tierney 46.84% 19.32% 22.11%
DFA Emerging Markets Core Equity I Dimensional (DFA) 8.96% 5.62% 6.38%
DFA International Core Equity I Dimensional (DFA) 13.62% 9.40% 11.17%
DFA US Core Equity 1 I Dimensional (DFA) 18.48% 11.49% 12.38%
Dodge & Cox Income Dodge & Cox 1.67% 2.57% 1.83%
Dodge & Cox Stock Dodge & Cox 9.53% 9.88% 10.58%
Fidelity Contrafund K6 W. Danoff 27.86% 13.63% 14.26%
Fidelity Low-Priced Stock K6 J. Tillinghast 17.11% 9.69% 11.32%
Fidelity Total Market Index Geode 18.25% 11.24% 12.28%
Franklin Small Cap Growth Adv D. Winters, T. Brighton 28.73% 9.78% 10.52%
Invesco Developing Markets Instl A. Kumar 10.46% 4.55% 5.59%
JPMorgan Equity Income R6 C. Hart, M. Marini 10.24% 10.62% 11.31%
JPMorgan Large Cap Growth R6 J. Simon, J. Williams 36.55% 14.63% 14.26%
MFS Growth R6 K. Clark, J. Flaherty 30.64% 12.54% 13.26%
MFS Value R6 R. Zito, J. LeBoeuf 10.53% 9.85% 10.79%
PIMCO Total Return Instl S. Mather, E. Burbano 1.46% 2.38% 1.63%
Principal MidCap R6 W. Bowen, A. Jackson 25.36% 11.83% 13.10%
Schwab S&P 500 Index Schwab 18.34% 10.99% 12.17%
T. Rowe Price Blue Chip Growth I L. Puglia 37.78% 14.29% 14.87%
T. Rowe Price Equity Income I B. Rogers 11.05% 10.36% 10.77%
T. Rowe Price Growth Stock I J. White 33.65% 12.77% 13.26%
T. Rowe Price Mid-Cap Growth I B. Berghuis 33.17% 12.39% 13.07%
Vanguard 500 Index Admiral Vanguard Index 18.35% 11.00% 12.20%
Vanguard Dividend Growth Investor D. Kilbride, M. Reckmeyer 8.65% 9.91% 10.87%
Vanguard Extended Market Index Admiral Vanguard Index 19.55% 8.72% 10.15%
Vanguard FTSE All-World ex-US Index Admiral Vanguard Index 13.11% 9.43% 11.08%
Vanguard Growth Index Admiral Vanguard Index 25.75% 13.03% 14.19%
Vanguard Small-Cap Index Admiral Vanguard Index 15.17% 7.25% 8.44%
17

INVESTLOGICBENCH2026
Fund Name Manager(s) 1Y 3Y 5Y
Vanguard Total Stock Market Index Admiral Vanguard Index 18.25% 11.25% 12.29%
Vanguard Value Index Admiral Vanguard Index 10.19% 9.79% 10.90%
Vanguard Wellington Investor J. Keogh, T. Martin 10.27% 7.60% 8.60%
Vanguard Windsor II Investor J. Keogh, T. Martin 9.64% 8.53% 9.84%
Vanguard Windsor Investor J. Keogh, T. Martin 8.67% 8.42% 9.52%
Vanguard Wellesley Income Investor J. Keogh, T. Martin 6.31% 5.32% 6.19%
Vanguard World Stock Index Investor Vanguard Index 20.64% 12.12% 12.83%
18
