---
title: 'E-Commerce Bench: Evaluating LLM Agents on Long-Horizon Autonomous Business Operation'
url: https://arxiv.org/abs/2608.30730
category: ai-marketing
subcategory: review
date: 2026-08
venue: arXiv (Cornell University)
authors:
- Wei Fan
- Xinjie Shen
- Xudong Guo
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.30730
pages: 64
chars: 244255
fetched_at: '2026-11-08T13:35:30+00:00'
kb_version: 1
---

# E-Commerce Bench: Evaluating LLM Agents on Long-Horizon Autonomous Business Operation

2026-09-01
E-Commerce Bench: Evaluating LLM Agents on Long-Horizon
Autonomous Business Operation
Wei Fan1,3∗, Xinjie Shen1∗, Xudong Guo1, Jianhong Tu1, Yang Su1, Yinger Zhang1,
Lianghao Deng1, Fengyu Wang2, Baohua Dong2, Yangqiu Song3, Dayiheng Liu1
1Qwen Team, Alibaba Group 2Taobao & Tmall Group, Alibaba Group
3Department of Computer Science and Engineering, HKUST
Abstract
Long-horizon agentic tasks go beyond chaining short tasks over more interaction turns.
Theirevolvingdynamicenvironmentsandlong-rangedependenciesrequireLargeLanguage
Models (LLMs) to continually explore, learn from experience, and adapt their policies over
thousands of steps. We introduceE-Commerce Bench, the first open-source benchmark
that integrates multi-round counterpart negotiation and dynamic events into a year-long
business operation. Over a 365-day year, an LLM agent concurrently runs multiple online
stores, researching the market, negotiating with suppliers to source inventory, optimizing
sales strategies, fulfilling orders, handling returns, and managing cash flow to maximize its
end-of-year total assets. To construct a realistic merchant-side operating environment, the
product and supplier data are derived from a real e-commerce platform, while a year-long
calendar of promotions, natural disasters, and supply-chain shocks continually reshapes
demand. For reproducibility, both sides of the market are deterministic: customer
purchases and returns follow a fixed demand model, while a negotiation kernel determines
supplier pricing, concessions, and decisions, with an LLM used only to verbalize them.
We evaluate 18 frontier models across seven dimensions, including year-end assets, and
find that no single model dominates. GPT-5.6 Sol earns the most, growing the¥100,000
opening stake into¥1,431,425, yet it ranks 16th of 18 on fraud avoidance and trails
Fable5 in operational efficiency. Among open-weight models, Qwen3.8-Max-Preview leads
with¥416,252, 38% above GLM 5.2 (high), and achieves the strongest learning over
the horizon, progressively bargaining down prices across repeated orders. Our code is
available athttps://github.com/QwenLM/E-CommerceBench.
∗Equal contribution. Work done during summer internship.
1
arXiv:2608.30730v1  [cs.LG]  31 Aug 2026

1k 10k 100k 1M
mean end-of-year total assets (¥, log scale)
GPT-5.6 Sol
Fable5
GPT-5.5
Claude Opus 4.8
Qwen3.8-Max-Preview
GLM 5.2 (high)
Kimi K3
Claude Opus 4.7
Claude Opus 4.6
GLM 5.1
DeepSeek-V4-Pro-Preview
Gemini 3.5 Flash
Qwen3.7-Max
Gemini 3.1 Pro
GLM 5.2 (max)
Kimi K2.6
Qwen3.6-Plus
Qwen3.5-Plus
14.31×
8.05×
7.02× 2/5
4.98×
4.16×
3.01×
2.65×
2.59×
2.58× 2/5
2.26×
1.90×
1.90×
1.65×
1.30× 2/5
1.15×
0.70×
0.47×
0.01× 4/5
×100k bankruptbreak-even ¥100k
Year-End Assets, 5 Episodes per Model
GPT Claude Gemini Qwen GLM Kimi DeepSeek
Figure 1: Mean end-of-year total assets, eighteen models, five 365-day episodes each. Bars start at the
¥100,000 stake. Whiskers span one 5-run standard deviation, hollow dots are single episodes, and red
fractions count bankrupt episodes, which stay pooled into the mean. The right column gives mean assets
as a multiple of the stake.
Profit
Negotiation
Fraud
avoidance
SolvencyEfficiency
Execution
Learning
0.25
0.50
0.75
1.00
GPT-5.6 Sol
Fable5
Qwen3.8-Max-Preview
GLM 5.2 (high)
Kimi K3
DeepSeek-V4-Pro-Preview
Gemini 3.5 Flash
18-model median
Figure 2: Seven evaluation axes for the strongest model of each vendor family by mean total assets, the
primary score, and the six evaluation dimensions clockwise from the top, each on the ranking metric §3.7
gives it. Axes are min-max normalized over the eighteen model means, so 1 is the best of the eighteen and
0 the worst, with a dashed polygon at the median. Fraud avoidance, solvency, execution, and learning are
sign-flipped, so a vertex further from the center is better on every axis.
2

Contents
1 Introduction 4
2 Related Work 6
2.1 Episodic Long-Horizon Agentic Tasks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2.2 Continuing Long-Horizon Agentic Tasks . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
3 E-Commerce Bench 7
3.1 Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
3.2 Agent Loop Layer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
3.2.1 Turn-Based Loop and Simulated Time . . . . . . . . . . . . . . . . . . . . . . . . . 8
3.2.2 Context Management . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
3.2.3 Persistent Agentic Memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
3.3 Tool Layer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
3.4 Sales and Economy Engine . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
3.4.1 Multi-Store Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
3.4.2 Three-Account Deferred Settlement . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
3.4.3 Deterministic Multi-Factor Demand Model . . . . . . . . . . . . . . . . . . . . . . 10
3.4.4 Fulfillment, Shipping Speed, and Returns . . . . . . . . . . . . . . . . . . . . . . . 11
3.4.5 Reputation System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
3.4.6 Dynamic Event System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
3.4.7 Daily Settlement and Processing Lifecycle . . . . . . . . . . . . . . . . . . . . . . . 11
3.5 Deterministic Negotiation Engine . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
3.5.1 Bargaining Policy Preliminaries . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
3.5.2 Two-Layer Supplier Design . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
3.5.3 Multi-Round, Cross-Supplier, Repeated Bargaining . . . . . . . . . . . . . . . . . . 13
3.5.4 Adversarial Supplier Fraud . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
3.5.5 Negotiation Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
3.6 Data Layer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
3.6.1 Catalog and Suppliers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
3.6.2 Systematic Information Asymmetry . . . . . . . . . . . . . . . . . . . . . . . . . . 15
3.7 Evaluation and Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
4 Experimental Results 16
4.1 Experimental Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
4.2 Overall Performance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
4.3 Multi-Dimensional Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
4.3.1 Negotiation Quality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
4.3.2 Fraud Avoidance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
4.3.3 Cash Flow and Solvency . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
4.3.4 Operational Efficiency . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
4.3.5 Operations Execution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
4.3.6 Learning over the Horizon . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
4.4 Error Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
5 Conclusion 21
A Agent Harness and Interface 26
B Data Layer 28
C Economy Engine 32
D Deterministic Negotiation Kernel 36
E Metric Definitions 42
F Per-Dimension Results 49
G Failure Case Studies and Detection Rules 53
H Prompts 58
3

1 Introduction
Large language model (LLM) agents are increasingly expected to handle tasks that span thousands of
steps, planning and acting over long trajectories with external tools (Yao et al., 2023). Such tasks require
an agent to make sequential decisions, adapt to past experiences, and remain coherent long after the initial
instruction. Sustained competence of this kind marks a frontier for current models and eludes most agentic
benchmarks. In reinforcement learning, tasks are divided intoepisodicandcontinuingones (Sutton &
Barto, 2018), and this distinction also organizes the long-horizon agentic tasks. Episodic benchmarks set
a goal and score its completion, whether resolving a GitHub issue (Jimenez et al., 2024), operating a real
computer (Xie et al., 2024), or producing knowledge work that an expert grades (Patwardhan et al., 2025).
Continuing tasks carry no terminal state, running without end in dynamic environments (Qian et al., 2025;
Chen et al., 2026) and scoring an accumulated outcome that surfaces the failures long horizons produce,
among them loss of coherence and an inability to turn experience into better decisions. Business operations
provide a natural continuing scenario with high-stakes, irreversible decisions, where compounding financial
health tests sustained agent competence. Despite its promise, current benchmarks capture this environment
only partially. While the Vending-Bench series (Backlund & Petersson, 2025; Andon Labs, 2026) simulates
multi-round supplier negotiations, its reliance on mock data and prompt-based simulation yields highly
stochastic supplier feedback that is vulnerable to manipulation. YC-Bench (He et al., 2026) runs a
deterministic startup year yet involves no supplier sourcing. Data-grounded retail benchmarks such as
MerchantBench (Shi et al., 2026) and RetailBench (Zhang et al., 2026c) add real products and open code
while dropping negotiation and adversarial dynamics altogether. Evidently, existing benchmarks either
deviate from real-world market dynamics or rely on purely LLM-driven counterparts for multi-round
negotiations, which introduces substantial sampling noise and ultimately compromises both the credibility
and reproducibility of the evaluation.
To address these, we introduceE-Commerce Bench, the first open-source benchmark that unifies determin-
istic supplier negotiation and customer sales modeling within a real-world continuing business operation
(Figure 3). Across a simulated 365-day year, an agent can run up to four online stores concurrently,
researching the market, negotiating for cost-effective goods, formulating sales strategies, and managing
cash flow to maximize end-of-year total assets. Grounded inTaobao & Tmall data, the environment
encompasses a total of 6,886 products and 576 suppliers calibrated from empirical platform logs, while a
year-long calendar of promotional events, natural disasters, and supply-chain shocks continually shifts
dynamic market demand. Critical market factors, such as baseline product costs and exact consumer
demand, remain hidden, requiring the agent to continuously search, negotiate, and model market dy-
namics through a dedicated e-commerce toolset provided by the benchmark. Meanwhile, the benchmark
harness automatically manages the context window and offers a persistent memory module (Packer et al.,
2024; Park et al., 2023) to sustain a year-long operational horizon. To ensure rigorous reproducibility,
determinism governs both sides of the market. Customer purchases and returns follow a fixed demand
model that combines price elasticity, weekday, seasonality, scheduled promotions, market events, and
store reputation, with its only randomness seeded from the episode so runs reproduce exactly. On the
supply side, a deterministic negotiation kernel fixes every pricing, concession, and accept/reject decision
through explicit bargaining policies, while an LLM only renders them as dialogue. Roughly a quarter
of the suppliers turn adversarially fraudulent, on kernels that do not vary between runs. No sampling
noise reaches the customers or the counterpart’s pricing and accept/reject decisions, so a difference in
outcome entirely belongs to the agent policy rather than to chance. Only the LLM renderer’s wording
varies between runs (§3.5.2).
We evaluate 18 leading frontier and open-weight models along multi-dimensional metrics spanning
negotiation quality, fraud avoidance, cash flow and solvency, operational efficiency, operations execution,
and learning over the horizon, rather than by total assets alone. A radar over the primary score and those
six dimensions comes out visibly uneven, and six of the seven models it draws, one per vendor family, fall
below the eighteen-model median on at least one axis (Figure 2). GPT-5.6 Sol grows its capital roughly
14-fold, yet ranks 16th of 18 on fraud avoidance and earns less from a tool call than Fable5 does, while
Claude Opus 4.7 leads both bargaining and fraud avoidance from mid-pack on profit. Among the ten
open-weight entries, first place goes to our own Qwen3.8-Max-Preview at 4.2 times the initial balance,
and four of the eighteen models slip into bankruptcy on part of their runs. Qwen3.8-Max-Preview is the
strongest model in the field, improving over the year. Across 8,647 repeat purchases of the same item
from the same honest supplier, 16 models show no clear sign of pushing the purchase price down as the
year goes on, exposing critical deficiencies in their long-horizon experiential learning.
We make three principal contributions.
1. We presentE-Commerce Bench, a realistic business environment grounded in Taobao & Tmall plat-
form data, and the first open-source benchmark to combine deterministic counterpart negotiations,
dynamic events, and concurrent multi-store management over a year-long horizon.
4

2. We keep the economydeterministic on both sides of the market, with a fixed demand model
driving customer purchases and returns and a deterministic negotiation kernel setting every pricing,
concession, and accept/reject decision while an LLM only renders dialogue. The kernel extends
the negotiation-partner design of TERMS-Bench (Zhang et al., 2026a) to repeated, cross-supplier
bargaining.
3. We evaluate 18 models alongmulti-dimensional metrics, so one total-assets figure can no longer
hide where a model is weak. Reading six dimensions beside that total turns a leaderboard into a
capability profile, and the profiles come out sharply divergent, the best earner being neither the
best negotiator nor the efficient operator.
The remainder of this paper is organized as follows. Section 2 reviews long-horizon agentic benchmarks
and positions E-Commerce Bench among them. Section 3 details the benchmark, covering its four-layer
architecture, the deterministic negotiation kernel, the real-data economy, and the evaluation metrics.
Section 4 reports results for the 18 models on every measured dimension, together with an error analysis
of recurring failure modes. Section 5 concludes.
5

Table 1:Comparison with continuing business-operation benchmarks. ✔ present, ✗ absent.Steps/runis the
per-episode agent-action count, taken or inferred from each paper.Op. unitscounts business units (e.g., stores)
run concurrently.Reproduciblemarks counterparts that follow fixed rules or seeded draws rather than a sampled
LLM.‡In Vending-Bench 1/2, product and supplier names are real while prices, demand, and elasticity are
LLM-generated. §Supplier economics are deterministic, while the renderer voicing them varies wording between
runs (§3.5.2).
Benchmark Domain Steps/ run Op. units Real data Nego- tiation Multi- agent Adver- sarial Repro- ducible Open source
Vending-Bench (Backlund & Petersson, 2025) Vending≤2000 1✗ ‡ ✔ ✔ ✗ ✗ ✗
Vending-Bench 2 (Andon Labs, 2026) Vending 3000–6000 1✗ ‡ ✔ ✔ ✔ ✗ ✗
YC-Bench (He et al., 2026) Startup∼500 1✗ ✗ ✔ ✔ ✔ ✔
MerchantBench (Shi et al., 2026) E-commerce∼700 1✔ ✗ ✗ ✗ ✔ ✔
RetailBench (Zhang et al., 2026c) Supermarket∼1000 1✔ ✗ ✗ ✗ ✔ ✔
E-Commerce Bench (Ours) E-commerce 1000–4000 ≤4 ✔ ✔ ✔ ✔ ✔§ ✔
2 Related Work
2.1 Episodic Long-Horizon Agentic Tasks
Long-horizon agentic benchmarks are divided by whether a run carries a terminal state (Sutton & Barto,
2018). Episodic benchmarks define one, setting a goal and rewarding the multi-step execution that reaches
it.Work-valuebenchmarks grade an economically meaningful deliverable, GDPval (Patwardhan et al.,
2025) scoring knowledge work against expert judgment and TheAgentCompany (Xu et al., 2025) setting a
simulated employee’s tasks inside a software firm.Environment-groundedbenchmarks stretch the horizon
through real software, SWE-bench (Jimenez et al., 2024) resolving a GitHub issue against its own tests
and OSWorld (Xie et al., 2024) driving a real operating system over many GUI steps.Exploration-driven
benchmarks probe reasoning further still, UltraHorizon (Luo et al., 2025) hiding the rules of a partially
observable world and EdgeBench (Zhu et al., 2026) learning from one environment for 12 to 72 hours at a
time. However long these tasks run, each ends the moment its goal is met, reducing evaluation solely to
the quality of the final deliverable. Consequently, this setup fails to assess an agent’s ability in dynamic
environments to track dependencies across hundreds of sub-tasks, recover from unexpected failures, or
leverage accumulated history to optimize future actions.
2.2 Continuing Long-Horizon Agentic Tasks
Continuing tasks carry no terminal state, so the agent acts indefinitely and earns an accumulated score.
The shape recurs across trading a live portfolio for cumulative return (Qian et al., 2025; Chen et al., 2026)
and self-evolving agents that grow a skill library (Wang et al., 2023) or rewrite their own code (Zhang
et al., 2026b). The setting E-Commerce Bench belongs to is business-operation simulation, where the agent
runs a going concern and is judged by its accumulated balance. Vending-Bench (Backlund & Petersson,
2025) established the line, running one vending machine over roughly two thousand messages and exposing
failures oflong-term coherence, with LLM-generated supplier replies that leave runs stochastic. Vending-
Bench 2 (Andon Labs, 2026) extends it to a full year and adds adversarial suppliers, still LLM-driven.
YC-Bench (He et al., 2026) runs a deterministic startup year against rule-based clients but no supplier
negotiation. Two benchmarks are grounded in real data, MerchantBench (Shi et al., 2026) over 365 days
of seller-side operation with suppliers arriving as stochastic events, and RetailBench (Zhang et al., 2026c)
over 180 supermarket days against a privileged oracle. Neither offers negotiation or adversarial suppliers,
and RetailBench lists strategic supplier behavior and multi-store coordination among the things it leaves
out. Table 1 contrasts the five. The Vending-Bench line couples negotiation with adversarial suppliers in
its sequel, but only through sampled LLM parties and without an open, real-data economy, while the
data-grounded retail pair buys reproducibility by giving those dynamics up. E-Commerce Bench holds
all six properties at once, and no other entry pairs a negotiating counterpart with reproducible supplier
economics. TERMS-Bench (Zhang et al., 2026a) sits outside the business-operation line, diagnosing
bilateral price bargaining against a rule-based counterpart over sampled regimes rather than data-grounded
cost floors, so it supplies a scripted opponent but no economy for the resulting deals to act on. Our market
is deterministic on both sides, a fixed demand model driving customers while adeterministic negotiation
kerneladapts that counterpart design to set every pricing and accept/reject decision, leaving an LLM
only the dialogue rendering.
6

Agent Loop Layer
LLM Agent
Tool Calls Advance
Env Time
Daily/Env
News Notification
Repeat Next
Turn
Context Management
Persistent Memory
Tool Layer
Environment Layer
Store
Operations
Market
Research
Supplier
Negotiation
Inventory
Management
Financial
Management
Memory
Operations
Time
Advancement
Dynamic Economy Engine Deterministic NegotiationKernel
Data Layer
User & Sales
Modeling
NaturalDisasters
Promotions
SupplierBankrupt
Three-Account
System
Bank
Escrow
Platform
Dynamic Events
…
6,886
Products
12
StoresTypes
60
ProductCategories
576
Suppliers
For a bulk order of 1,000 bottles,
is1.5the best you can do?
I'm afraid wecan't go lower than1.8.
Reference selling price
Supplier cost floor
 Model response
generation
Figure 3: Overview of E-Commerce Bench. The agent works through four layers. Anagent loop layer
carries turn-based control, context management, and persistent memory, and atool layerholds the 18
e-commerce tools. Under both sits a deterministicenvironment layer, the sales-and-economy engine beside
the two-layer negotiation engine, computing over adata layerderived from a real e-commerce platform.
3 E-Commerce Bench
3.1 Overview
E-Commerce Bench hands the agent a merchant account,¥100,000, and the 2026 calendar year on a
simulated Chinese online marketplace. The job is to end the year with as much money as possible.
The agent researches which store types and categories carry demand, bargains suppliers down, buys
inventory and publishes it to one of at most four stores. From there it prices the goods, reads yesterday’s
sales, ships orders, absorbs the returns, and withdraws settled revenue before the next operating charge
lands. To evaluate the strategies driving the year-end profit, we independently score six core capabilities:
negotiation quality, fraud avoidance, cash flow and solvency, operational efficiency, operational execution,
and long-horizon learning (§3.7). Next, we introduce the four layers of E-Commerce Bench in detail.
3.2 Agent Loop Layer
Three mechanisms sit between the model and the environment. The turn loop (Figure 4) bounds what
one model call can do, and charges simulated minutes for every tool it uses. Every turn adds its tool
traffic to the message list, and a year of calls overruns the window many times, so the context editor
evicts the oldest turns first. The window is not the real limit either, since long contexts degrade well
before they overflow (Liu et al., 2024; Bai et al., 2024). Because evicted text leaves nothing behind, the
agent also gets a persistent memory system beyond the reach of any eviction pass.
7

agent side environment side
One model call
its reasoning and a batch of tool calls
The tool batch runs in order
at most one simulated day per batch
Tool responsereach the model
each one stamped with the clock
Hidden environment state
stock, escrow, reputation, fraud flags
Eachtool runs, charging minutes
the clock advances inside the call
End of Day Settlement
the whole day posts at once
clock past 18:00?
Yes
No
Fees/ Sales/ Returns…
append daynews and
noticesto the response
no eviction until the transcript passes 120,000 tokens
append env notificationto the response
Figure 4: The agent loop layer. One model call produces a batch of tool calls; the batch runs in order,
and a timed tool advances the simulated clock inside its own call. The daily settlement fires whenever the
clock reaches the next 08:00, whether a timed tool carried it there or the agent asked to skip to tomorrow.
Tools read and write the hidden environment state, and the settlement writes back to it as well, posting
that day’s fees, sales, and returns. The day’s news and any notices are appended to the tool responses.
The transcript is left alone until it passes 120,000 tokens, and only then are its oldest groups dropped.
3.2.1 Turn-Based Loop and Simulated Time
Within a single turn, the model can request several tools, which then run one by one in the order given.
Turns therefore range from a single balance check to a batch of a dozen tools. An episode runs to a cap
of 4,000 turns (§4.1), or ends early once the model goes three turns without calling a tool. Every tool
but the day jump costs simulated minutes: 10 for a balance check and 60 for opening a store (Table 3 in
Appendix A), spent out of a 600-minute day that runs from 08:00 to 18:00. Looking something up draws
on the same clock as acting on it. A message costs 30 minutes whether it goes to one supplier or to ten,
so twenty of them fill a day.
Once the clock passes 18:00, it jumps to 08:00 the next morning, whichwait_for_next_day also does on
request, costing no minutes but forfeiting the rest of the day. Every jump runs the same fixed sequence,
charging operating and storage costs, turning the previous day’s demand into orders, cancelling shipments
that missed their two-day deadline, settling matured escrow, delivering arriving purchase orders, and
updating reputation (§3.4). What the agent gets back after advancing to the next day is four thin signals:
the day’s news feed, a reminder once the bank balance no longer covers the day’s operating cost, the
current time, and a warning about token usage (Appendix A). Anything more precise costs a tool call and
the minutes that come with it.
3.2.2 Context Management
A single tokenizer counts each model’s context to ensure all of them work against the same 128,000-token
budget. A context eviction is triggered whenever the count reaches 120,000 tokens, taking 60,000 as its
release target. Whole tool-call groups go, an assistant message and every tool response after it, oldest first
(Figure 5). The system message, the first user turn, and the two newest groups are spared. The agent is
told the policy verbatim, thresholds included, so preserving what matters in its memory is a choice it can
make. Across the 90 evaluation episodes of §4, 1,495 evictions ran. How much history a model loses scales
with its total tool traffic, the turns it takes times what each turn drags in, and the two factors trade off.
Claude Opus 4.7 finishes the year in 432 turns and has about four windows’ worth of transcript discarded
along the way, while Gemini 3.5 Flash takes 2,628 turns and loses nearly nineteen windows’ worth. Turns
alone do not settle it. Kimi K2.6 takes 1,017 turns and loses the same three and a half windows as Claude
Opus 4.7 at 432 turns, because it drags in431tokens a turn against Opus 4.7’s1,058, and GPT-5.5 loses
28 windows in half Gemini 3.5 Flash’s turns at2,759a turn.
8

eviction starts once a group crosses 120,000 tokens
context window, 128,000 tokens
before
system prompt
and task, kept oldest groups, cleared first the two newest, kept
after
one pass aims to free 60,000 tokens one group is one model reply plus every tool result it returned, about 50 to a window
1 49 50
49 50 61,500 tokens removed, nothing left in their place
Figure 5: How eviction works. A group is what the editor removes as a unit: one model reply together
with every tool result that reply produced, so a turn that called six tools is still one group, and about fifty
groups fill the window. A pass fires only once a group pushes the count past 120,000 tokens, then drops
whole groups, oldest first, until 60,000 tokens are released or the clearable groups run out. The system
message, the first user turn and the two newest groups are kept.
3.2.3 Persistent Agentic Memory
The memory store is a list of notes the agent keeps in the environment rather than in its own messages,
so eviction never touches it. The store holds at most 20 entries, each a title and its content. The agent
fully curates the store itself—creating, updating, and pruning entries as needed (Shinn et al., 2023; Packer
et al., 2024; Zhong et al., 2024; Sumers et al., 2024). Reading the store back is cheap in minutes yet
expensive in tokens, since returned entries re-enter the context and become evictable like everything else.
A capable agent is thus incentivized to preserve high-value strategic knowledge, such as past settlement
prices or identifying deceptive suppliers.
3.3 Tool Layer
Eighteen tools cover a merchant’s back office, in the seven groups Figure 3 draws, and Table 3 gives each
one its minute cost and its effect. Every call but the day jump is billed in simulated minutes (§3.2.1),
which makes the tool list a budget rather than a menu. Checking the bank balance, the warehouse, and
one store’s status costs 10 minutes each. A morning round of all three spends 30 minutes a day, more than
18 working days across the year. Onlychatbox can create a purchase order, so every unit of inventory
arrives through free-form text carrying fencednegotiate blocks (§3.5.2). Routine mail, supplier offers,
and fraudulent pitches (§3.5.4) all cost the same 30 minutes through that one tool.
3.4 Sales and Economy Engine
The sales and economy engine decides how much the agent sells and when it gets paid. Nothing about the
market is sampled. A fixed formula computes how many units customers buy each day, and money moves
between accounts on fixed delays. The simulator still draws a few random numbers, for instance when it
turns a fractional unit of demand into a whole one, and those come from one seed shared by every run, so
two episodes that take the same actions end the year with exactly the same money.
3.4.1 Multi-Store Setup
An agent trades through stores it opens itself. Twelve store types are on offer, each covering a different
set of product categories, and at most four may trade at once, one per type (Appendix B.2). Opening
one costs¥500 and then¥60 to¥130 a day to run, the harder types costing more. Closing a store stops
the daily charge, and stock left behind keeps accruing storage unless the agent liquidates it for10%of
purchase cost. Reopening later starts reputation over. A market lookup grades a category’s margin low,
moderate, or high, while the price a supplier will actually accept emerges only from bargaining (§3.5).
3.4.2 Three-Account Deferred Settlement
Money an agent has earned is not money it can spend. Cash sits in three places (Figure 6). Thebank
accountpays every cost the moment it is incurred, a purchase order in full the moment a negotiation
closes. A sale pays nothing at first and only creates a pending shipment. Once the agent ships it, the
revenue entersescrowwith the platform’s commission already deducted. Nine days later that balance
matures into theplatform wallet, and only an explicit withdrawal moves it back to the bank account
where costs are paid. A refund is taken out of the escrow batch its sale belongs to, so a return never
touches spendable cash. One order shows the gap. A 40-unit lot of a mid-priced accessory costs¥2,447
9

(a) Three Accounts
escrow,
awaiting settlement platform wallet bank account, starts at ¥100,000
sales revenue in, gross × 0.98,
only once the agent ships within
2 days, less refunds at full retail
every cost out the day it falls due,
store setup, operating cost, storage,
shipping, and stock at order time
settles at
ship +9 days
withdraw,
an explicit action
stock sells
year-end assets = bank + escrow + wallet bank below zero on 10 consecutive days ends the episode
0 2 4 6 8 10 12 14 16 18
days after the purchase order is paid
2,000
0
2,000
4,000
¥ carried by this order
(b) Cash Cycle of One Order, 40 Units of One Real SKU
escrow
return window, ship +3 to ship +7
day 7, the agent ships
¥3,475 net revenue into escrow
¥20 standard shipping leaves the bank
day 5, stock arrives, lead time 3 to 7 days,
sellable from day 6
day 12, 16 units come back
¥1,418 refunded out of escrow
day 16, ¥2,057 settles
into the platform wallet
withdraw,
an explicit act
¥1,365 for the same lot at its negotiated cost floor
day 0, the purchase order is paid in full, ¥2,447
working capital locked 16 days, cash out on day 0 and first cash into the wallet on day 16
Figure 6: Three-account deferred settlement. (a) Costs leave the bank the day they are incurred, while
revenue passes through escrow and the platform wallet first. (b) One 40-unit order bought at the opening
quote and resold at reference, followed as cash for 16 days.
the day it is placed and returns its first cash on day 16. Ten consecutive days closing with a negative
bank balance end the episode as bankrupt (Appendix C.7), so an agent selling at a profit while leaving its
revenue in the wallet can still fail (§4).
3.4.3 Deterministic Multi-Factor Demand Model
How many units are sold is a product of named factors rather than a random draw. Demand for one SKU
on one day starts from what its category sells in a store of that type. Six multipliers then act on that
base: the response to the posted price, a weekend uplift, the promotion the agent joined, the month’s
seasonality, whatever the calendar holds that day, and the store’s reputation. Two capacity terms trim
the result, one for the category and one for the store, each a ceiling on how much demand that category
or that store can absorb in a day. What survives is capped at the units actually on the shelf.
˜dijt =β cτ ϕfc (rijt ;η cbit) wt mit(δit)σ τ,t ετ,t ρit,r ijt = (1−δ it)pijt vj ,
γijt =
{ κc
κc +∑ j′∈c ˜dij′t ifn τ≥2,
1ifn τ =1,
dijt = ˜dijt γijt κτ κτ + ˆDit ,
qijt =min (xijt ,⌊d ijt⌋+1 [ujt <dijt−⌊dijt⌋]) .
(1)
Indices run over storesi, SKUsj, datest, store typesτ and categoriesc, and Appendix C.2 defines every
symbol alongside the seasonality tables of Appendix B. Price enters through one of four elasticity families
carried per category (Gallego & van Ryzin, 1994). One of them, the quadratic family, is symmetric about
the public reference price rather than monotone, so in the categories that carry it, a discount below
reference loses demand instead of gaining it. The two capacity terms can then dominate everything the
six multipliers did. For one accessory SKU on a promotion Saturday, they cut a compounded expectation
of128.2units to the9actually sold, the category term alone taking a factor of7.5(Figure 7). How much
they bite depends on how heavily the agent stocks that category and store, meaning that adding more
homogenized SKUs cannibalizes demand rather than boosting aggregate sales.
10

0.6 0.8 1.0 1.2 1.4 1.6 1.8
price ratio r = pjt/vj
0.0
0.5
1.0
1.5
2.0
price response
(a) Elasticity Families, Median Real
linear, =3.00
exponential, =4.23
constant elasticity, =2.22
quadratic, =4.52
promotion boost b = 2
0 50 100 150 200
expected units on 2026-11-14
base daily demand
price response
weekend
promotion
seasonality (Nov)
market event
reputation
category saturation
store saturation
realized units
10.0 units
×2.80
×1.30
×3.50
×1.55
×1.00
×0.65
×0.13
×0.56
9 units
(b) Fashion Accessories SKU-Day
Figure 7: The demand model. (a) The four price-elasticity families at their median parameter, solid
without a promotion and dashed with the largest promotion boost. (b) The chain of multipliers that turns
one SKU’s price into units sold.
3.4.4 Fulfillment, Shipping Speed, and Returns
Every sale has to be shipped, and how it ships is a priced choice. Faster delivery costs more freight and
brings back fewer returns, and a bulkier parcel costs more again. An order left unshipped past its two-day
deadline is canceled outright, the units going back to the warehouse unsold and the cancellation counting
against reputation. Returns are decided when goods ship and arrive days later, so a fulfillment decision
costs money long after it is taken (Petersen & Kumar, 2009). Four channels set a unit’s return probability,
its category’s natural rate, whether the supplier shipped defective stock, how far above reference the agent
priced it, and the shipping speed chosen (Appendix C.4). A defective unit carries a return rate of at least
0.40and at least double the natural rate, capped at0.95. Pricing at1.3times reference multiplies the rate
by1.50, and slow shipping by a further1.30. Every arriving return refunds the customer out of escrow
and puts the unit back in the warehouse on a fresh storage clock. Two of the four channels answer to the
agent, its pricing and its freight tier, so a model’s return rate reads partly as a management outcome
rather than only as a property of the catalog (§3.7).
3.4.5 Reputation System
A store’s reputation multiplies its demand directly (§3.4.3), so service failures cost sales. Credit accrues
when an order ships rather than when it sells, so an unshipped order earns nothing and draws the
cancellation penalty as well. Returns and cancellations subtract from the same standing, weighted0.6
and1.0(Resnick et al., 2000), so a missed deadline costs more than a change of mind. A store pinned at
the floor receives15%of the demand it would receive at the top, and the capacity terms return part of
that loss once they bind (Appendix C.3).
3.4.6 Dynamic Event System
The calendar moves demand whether or not the agent is ready. Market events arrive on fixed dates,
scaling demand per store type and stretching delivery lead times (Appendix B.3, Table 6 and Figure 15).
Direction is rarely uniform, so a storm that lifts food cuts fashion and footwear. News of an event reaches
the agent’s feed as the event begins, while a promotion is announced a week ahead without its dates or its
size. Joining reveals the size, and the year’s first sale is already running when its announcement lands.
The boost from joining peaks at a30%discount, so a deeper cut adds demand only through the price
response while margin falls on every unit. Suppliers exit on a count rather than a date, each retiring after
a hidden number of filled orders, so a counterpart whose floor the agent has learned can be gone by the
next re-order.
3.4.7 Daily Settlement and Processing Lifecycle
Costs are charged before any revenue is recognized, so every morning tests solvency at the day’s low
point. Sales are then computed for thepreviouscalendar date against the inventory and prices the agent
left standing overnight, so the agent steers a system that lags it by a day. Refunds leave escrow before
matured escrow settles, so a return can empty the batch that was about to pay out. Appendix C.1 lists
all thirteen steps with the state each one touches.
11

3.5 Deterministic Negotiation Engine
The negotiation engine sets what the agent pays for stock. Every unit it sells has to be bought from a
named supplier, one chatbox message at a time, at a price the two of them argue over. Roughly a quarter
of the roster takes the money instead of earning it (§3.5.4), so a counterpart has to be chosen as well as
bargained with.
3.5.1 Bargaining Policy Preliminaries
Sourcing one SKU begins with a message to one supplier and ends in a price or in nothing. Neither side
sees the other’s limit. A supplier never reveals the floor below which it will not sell, so each purchase is
a bilateral bargaining problem under incomplete information (Harsanyi, 1967; Chatterjee & Samuelson,
1983; Rubinstein, 1982). One such cycle is a sessionz= (s,j,c), thec-th between suppliers and SKUj.
No rule closes a session at a fixed round. A deadline scale sets the time pressure instead, and past its
midpoint a supplier can walk away from an offer under its floor (Appendix D.1).
One pair from the evaluation fixes the scale. Ridge Express quotes a single SKU at¥149.81, and the
agent resells against a market reference of¥199.75. Beneath both lies a floor of¥101.27 the agent never
sees, leaving¥98.48 for the two sides to divide. Figure 8 follows one such session offer by offer in panel
(a), and the nine deals the pair produced across the year in panel (b).
Two prices bracket what a session can be worth. The agent resells against a public market reference price
vj (§3.4), while suppliers holds a private floorcs j. Bargaining runs in the gap between the two, the zone
of possible agreement (ZOPA), so a deal at unit pricepz for qz units hands the agent(vj−pz)qz of it.
How wide that gap is, how badly the supplier needs the sale and how hard it will push are drawn once
and stay hidden. The agent bargains without knowing how much room it has.
Sessions are divided by counterpart type, one term of the objective per side. WritingZG for those
concluded with the honest suppliersG andZB for those concluded with the fraudulent onesB (§3.5.4),
the year-end asset goal of §3.1 becomes a procurement objective.
maxπ
∑
z∈ZG
1[fz̸=⊥] (vj(z)−pz)qz
/bracehtipupleft /bracehtipdownright/bracehtipdownleft /bracehtipupright
surplus extracted from honest suppliers
−
∑
z∈ZB
1[fz̸=⊥]ℓ z
/bracehtipupleft /bracehtipdownright/bracehtipdownleft /bracehtipupright
losses paid to fraudulent suppliers
.(2)
Here fz is the session outcome,⊥ a disagreement worth nothing, andℓz what a fraudulent deal costs in
the end, whether overpayment, fees, short shipment or defective stock.
Two competencies follow, and they pull against each other. Winning surplus from an honest supplier
takes firmness; refusing a fraudulent one takes walking away, and the firmness that wins a good price is
also what produces impasse (Raiffa, 1982). Both are paid in the cash that sets the primary score.
3.5.2 Two-Layer Supplier Design
An outcome difference says something about the agent only if every model met the same counterpart
economics in every run. A supplier played entirely by an LLM breaks that twice over. Sampling moves its
prices from run to run, and it stayspersuadable, so an eloquent enough agent can talk it below its own
floor and turn the benchmark into a jailbreaking contest. Every supplier therefore splits into two layers.
Layer 1, the Deterministic Negotiation Kernel.Every price, concession and accept or walk-away decision
comes from a deterministic kernel rather than from a model. The kernel builds on the counterpart policy
of Zhang et al. (2026a), reimplemented independently in a seller-only role and re-parameterized from the
data layer (Appendix D). Acceptance and walk-away are stochastic (Baarslag et al., 2014), and a latent
cue carries sentiment and posture (Appendix D.1). Counter-offers answer the agent’s own concession speed
rather than the clock (Faratin et al., 1998), so an agent that concedes fast meets afirmercounterpart.
Fast concession carries the same disadvantage in human bargaining (Tey et al., 2021).
One kernel serves one (supplier, SKU) pair. Its reservation price and opening quote come from the data
layer, so both are properties of the SKU rather than draws. Its seed makes an identical agent trajectory
meet an identical supplier response (Appendix D.2). Two sources of run-to-run variance survive. The
Layer 2 renderer is an LLM sampled at its provider’s default decoding, and the delivery days a supplier’s
catalog advertises are drawn outside the episode seed, so they can move between runs. Prices and accept
or walk decisions cannot move, but the narrative a model reads to detect fraud does, so the fraud axis of
§4.3.2 carries renderer sampling noise on top of policy sampling noise.
Honest suppliers draw from six behavior templates. The templates differ in how sharply the kernel answers
the agent’s concession speed and in how much its cues give away. Which supplier gets which is fixed in
12

1 2 3
exchange within the session
¥100
¥105
¥110
¥115
¥120
¥125
¥130
¥135unit price
cost floor ¥101
¥131.44
¥118.92
¥116.74
¥102 ¥103.11
¥110
supplier
agent
accepts
(a) one session: both sides converge
¥100
¥120
cost floor ¥101
(a)AnchorRegret 0.11
(b) many deals: anchor lost
0 25 50 75 100 125
simulated day
¥50
¥100
cost floor ¥24
deal pricebest so far
AnchorRegret 0.00
(c) many deals: anchor held
Figure 8: Negotiation at two timescales, from real episodes, each panel on its own price axis and the
cost floor hidden from the agent.(a)One session offer by offer, the agent bidding up and the kernel
conceding down until the agent accepts its standing quote.(b)The same (supplier, SKU) pair all year,
where that session ends a run of near-floor deals and the price never recovers, the hatched wedge being
the overpaymentAnchorRegret averages.(c)Another agent instead pushes lower at nearly every restock.
the released roster, so the difficulty mix is set rather than drawn per run (Appendix D.3). Neither the
template nor the honest or fraudulent label is visible to the agent.
Layer 2, the NPC renderer.A second LLM turns each committed kernel decision into supplier chat. The
renderer has to relay the exact price and decision and takes only tone from the kernel’s sentiment cue,
which keeps the dialogue rich and economically inert. Compliance does not rest on that instruction. An
accept is refused unless its price matches the kernel’s standing quote to within±0.005, so a renderer that
misstated a price could never make it a transaction (Appendix D.4). In the other direction, a deterministic
parser reads the agent’s own offer, accept and reject actions out of the same free-form message. One
economic action travels in the prose instead, enrolment in a supplier’s membership program, which an
intent classifier recognizes from the agent’s own words and bills at¥1,000 (Appendix D.5). Prices carry
no signal about fraud by design, so on the pre-deal class the narrative holds the decisive evidence, and no
fixed template could mount it. Figure 20 prints one session end to end, every supplier line beside the
kernel decision it had to relay.
3.5.3 Multi-Round, Cross-Supplier, Repeated Bargaining
One session is usually the unit of evaluation in existing negotiation benchmarks, and the kernel as described
so far governs exactly one. Across a full year the game becomesrepeated, which asks whether an agent
turns what one encounter taught it about a counterpart into a better price at the next. Inferring a private
reservation value from past encounters (Baarslag et al., 2016) therefore becomes part of the task rather
than an assumption. Closed deals are not re-surfaced, so an agent keeps its own price history or does
without it.
Once a session over(s,j) concludes, the next offer on that pair opens a fresh cycle under a new kernel
instance and a new seed, carrying thesamepersistent type and reservation price. A seller-side kernel never
accepts below that reservation, so the best price won so far is an upper bound oncs j that only tightens.
The competence it rewards is toanchoreach reopening at or below that historical best. Calling the rule
optimal would go too far, since against a pre-deal fraudulent counterpart the historical best tightens onto
a floor inflated on purpose (§3.5.4).
Learning runs on both sides of the table. Each supplier’s deal history goes into its prompt, so suppliers
“remember” what they sold before. Several honest suppliers serve every category alongside a few fraudulent
ones, so the agent can also arbitrateacrosscounterparts, probing one supplier’s floor and holding it as an
outside option against another. Single-session skill and year-long accumulation then separate cleanly, the
first measured in per-session surplus, the second in how fast the price for a repeatedly sourced SKU walks
down toward the floor (§3.5.5).
Every session costs twice over besides. Bargaining spends minutes out of the working day (§3.2.1), and
an agreement spends cash out of a bank balance that refills only when escrow settles (§3.4.2). A session
excellent in surplus terms can still be the wrong one to have opened.
13

3.5.4 Adversarial Supplier Fraud
Of the 576 suppliers on the roster, 152 are fraudulent. Each runs the hardball kernel preset under one of
five scripted scam overlays that the renderer performs. The five split into two classes bywhenthe damage
lands (Appendix D.5). No single observation gives a fraudulent counterpart away. Opening quotes are
uninformative by construction (§3.5.2), and the behavior family stays latent and is shared with honest
suppliers. What does separate the two populations is therateof concession, since fraudulent kernels hold
out longer than the hardest honest preset. That signal lives only in the shape of a multi-round exchange,
so an agent that accepts early gives up its one bargaining-side cue and has to read the narrative instead.
Pre-deal scamsmake their money inside the negotiation. Their kernels carry a reservation price inflated
toward1.5× the honest cost floor, soanydeal overpays what an honest competitor would have charged.
The inflated floor still sits inside the range an honest supplier might quote, so only the narrative gives it
away, offering membership fees, discounts that never arrive, or manufactured urgency.
Post-deal scamskeep the honest cost floor and quote from that same range, then defect at fulfillment. A
short delivery brings 60% to 70% of the quantity paid for, and defective stock returns at0.40or double
the SKU’s natural rate, whichever is higher, capped at0.95(§3.4). The defective rate is blended across
the SKU’s pooled stock, so interleaving honest and fraudulent deliveries dilutes the evidence and no
observed return rate points back to a culprit. Scoring therefore counts the money actually lost to these
counterparts rather than judging intent (§3.5.5), which keeps the axis on the cash of Equation (2).
3.5.5 Negotiation Metrics
Both terms of Equation(2) are scored as the fraction of the bargaining range an agent captures, standard
practice in automated negotiation (Raiffa, 1982; Baarslag et al., 2013). The metrics build on the surplus
efficiency of Zhang et al. (2026a), re-based from sampled ZOPA geometry onto data-grounded floors,
and Appendix E.1 carries every formal definition. Agreement is close to universal on the honest sessions
a model concludes, soCSE+ carries the headline, the share of a pair’s bargaining range that a closed
deal captures. Beside it% Oracle compares the same surplus against closing every honest deal at the
supplier’s floor, and the agreement rate stays in Appendix E.1. Neither headline metric weights a deal by
quantity, and both are rates over a session set the agent chose itself, so they measure per-deal bargaining
skill rather than procurement cash saved. Two models compare on them only if their portfolios carry
similar bargaining ranges, which §4.3.1 checks by reporting deal volume beside the rate. Conclusion is the
operative word. A session abandoned mid-bargain enters no denominator and costs nothing in any of the
three metrics, so §4.3.1 reports abandonment counts beside them rather than folding them into a rate.
Fraud avoidance is reported asBadSpend%rather than as an agreement rate over fraudulent sessions,
because the agent also chooses whom to contact at all. A session-rate denominator would reward never
looking, and cash is in any case the quantity a scam actually costs.
Sequential price disciplineOver 365 days, the same supplier is asked for the same SKU many times,
which raises a question no session-level metric answers. Does an agent’s next order benefit from the price
it already won? Holding an anchor like that has documented value in human bargaining (Petrowsky et al.,
2025). The measure looks at every honest (supplier, SKU) pair traded more than once. Each agreed
price is expressed as its positionπz inside that pair’s bargaining range, then scored after the first deal
against the best the agent had already won there.AnchorRegret averages the resulting overpayment.
AnchorRatio divides that average by a null which holds each pair’s prices fixed and reshuffles only the
order they arrived in. Significance travels separately in the permutationz-scorezanchor.
The null assumes a pair’s cycles are equally hard, and that assumption is checkable rather than asserted.
Two of the three quantities that set that difficulty are constants of the SKU, and the archive records the
cost floor and the nominal wholesale reference unchanged across all8,647re-orders. The quote the kernel
actually opens with is redrawn each cycle and the archive does not keep it, so a risingπz is read against a
fixed floor rather than against a fixed opening. The measure reports an outcome and not its cause, and
§4.3.6 takes up which mechanism produces it. Figure 8 shows both outcomes on real trajectories, one
agent giving back a price it had already won while another walks its price down the range all year.
Three limits bound the scope. Only honest pairs count, since a pre-deal fraudulent floor is inflated by
construction (§3.5.4). Each re-order counts equally regardless of order size, so the measure captures
per-unit discipline and not its cash consequence. No observations come from an episode that ends early.
3.6 Data Layer
Every number E-Commerce Bench runs on comes from a real e-commerce platform, either desensitized
straight off it or synthesized by hand against an analysis of its data logs, the supplier price floors of §3.5
and the demand parameters of §3.4 among them.
14

3.6.1 Catalog and Suppliers
The environment ships 6,886 products in 60 categories, served by 576 suppliers, 424 of them honest and
152 fraudulent. The 12 store types span 9 categories down to 1, and the calendar fixes 10 market events
and 8 promotions. Desensitization maps the products, the categories, the per-category return-rate tiers,
the monthly-sales bands and the holiday calendar straight off a real e-commerce platform. Synthesis
from real logs supplies the rest, namely the four price-elasticity families, seasonality curves, reputation
parameters and supplier attributes. Promotion names are fictional, since a model that recognizes China’s
largest shopping festival could price from memory rather than from evidence (Zhu et al., 2025). Fraud
reaches every product line rather than concentrating in a few. Each supplier serves exactly one category,
no category holds fewer than 7 honest and 2 fraudulent, and coverage stays flat across catalog depth
(Figure 13d). Every fraudulent one runs a scam of §3.5.4. The supplier list is fixed at release rather than
redrawn per episode, and Appendix B lists all 60 categories with their parameters.
3.6.2 Systematic Information Asymmetry
An agent sees the catalog and the outcomes of its own actions, never the demand and cost-floor parameters
that decide what an action is worth. A market lookup answers at one of three levels: the coarsest naming
every store type and the finest one category’s sales band (Table 3), each substituting a label for the
quantity behind it. A profit-potential grade replaces demand capacity, a margin class the wholesale ratio,
and a sentence about returns the per-SKU rate. Supplier lookup withholds most, naming no type and
ranking nothing (§3.5.2). Pre-deal scams show in the narrative from the opening quote (§3.5.4). Post-deal
ones are written to read like ordinary suppliers, so only the goods that arrive expose them, and the cash
has left by then. Table 7 in Appendix B sets each observable against the quantity it withholds and prices
the discovery. Portfolio decisions therefore rest on inference, and hidden parameters differ widely in how
fast they can be learned. The best price already won from a supplier bounds its floor from above (§3.5.3),
and a SKU’s natural return rate becomes readable once its stock has moved. An elasticity parameter
stays hidden all year, since four unprinted factors multiply the same observation. A store type’s earning
ceiling shows only after one has been operated for a year. Exploration and operation both cost time (§3.2),
so the year rewards allocating discovery rather than exhausting it.
3.7 Evaluation and Metrics
The primary score isend-of-year total assets, the sum of the bank account, the platform wallet, and
unsettled escrow, reported as theasset multiplierover the¥100,000 opening stake. Bankruptcy ends a
run before the horizon (§3.4.2). Truncated runs enter the average rather than being dropped, so a five-run
mean can mix them with full years. Six capabilities are measured around the year-end assets:
(1) Bargaining is scored on how far down the agent pushes a price.CSE+ ranksnegotiation quality, how
much of the distance from the public reference price down to the supplier’s cost floor a closed honest deal
covers, where1means buying at the floor and0means paying the reference price, averaged over sessions
with no weight for order size. Recorded around it areSE+,% Oracle, AGR+, rounds to deal, deals closed,
and both surplus and spending broken out by the supplier’s behavior template (§E.1). (2)Fraud avoidance
follows the cash rather than the conversation. Ranking runs onBadSpend%, the share of order spending
that cleared into a fraudulent supplier’s account, low being the better direction. We also record the fraud
agreement rate (the percentage of fraudulent sessions ending in a deal), alongside diagnostics covering
losses across the five scams, membership fees paid, and fraudulent suppliers contacted or ordered from
(§E.2). (3) Solvency is judged by how much of its own best position a year gave back. Peak drawdown
over peak total assets rankscash flow and solvency, since the archive records that fall in absolute¥, and
a business ten times the size books ten times the fall for the same discipline. The unnormalized fall, the
bankrupt runs, the overdrawn days, the deepest bank balance, the idle platform wallet, and the largest
warehouse held round out the dimension (§E.3). (4)Operational efficiencyprices a year of profit against
the calls that produced it. Mean profit over mean tool calls orders the models. Sitting next to it are the
call count, its split over eight activity bands, the turns, the eviction passes the transcript needed, and the
memory-store traffic (§E.4). (5)Operations executionis ranked by the controllable return rate—the excess
returns driven by the model’s pricing above the baseline (accrued at dispatch; negative for discounted
prices), excluding fraud-induced defects. Supporting diagnostics include realized returns, refund and
freight losses, on-time delivery rates, orders lost to the two-day deadline, tier mix, and store counts (§E.5).
(6) Learning is read from what an agent does every time after the first that it buys the same item from the
same supplier, which over a year is usually several times.AnchorRatio rankslearning over the horizon
by measuring how much each repeat order overpays against the cheapest that agent had yet paid that
supplier for that item. Beside it lie the same overpayment before its permutation null,AnchorRegret, the
NewLowrate, the combinedz anchor, the repeat-order count and three half-year comparisons (§E.6).
15

Table 2:End-of-year leaderboard, 18 models, five episodes each, sorted by mean final assets within tier. Final
assets carries the primary score, and the six columns after the spread rank one evaluation dimension each,CSE+
for negotiation quality,BadSpend%for fraud avoidance, drawdown over peak for cash flow and solvency, yuan
per tool call for operational efficiency, the controllable return rate for operations execution, andAnchorRatio
for learning over the horizon, with the formulas in §E.1 through §E.6. Arrows mark the direction of the better
outcome, and a tinted cell holds the extreme of a scored column. Tool calls, turns, and bankrupt runs record
what an episode spent rather than scoring it, and bankrupt episodes stay pooled into every mean, which is what
the spread column beside the assets reports.†GPT-5.5’s spread is a population estimate,¥689k on the sample
estimator. ‡GPT-5.5’s AnchorRatio averages three episodes; its two bankrupt runs opening no repeat order with a
supplier it had already dealt with.
Model
Final assets
¥k, mean
std
¥k
CSE+
↑
BadSpend%
↓
Drawdown
/ peak↓
¥per
tool call↑
Controllable
return, pp↓
AnchorRatio
↓
Tool
calls Turns
Bankrupt
runs
Proprietary
GPT-5.6 Sol (max) 1,431314 0.672 18.48 0.278 363 4.46 1.217 3,668 1,367 0/5
Fable5 (max) 805 188 0.772 3.46 0.141 4790.22 1.573 1,469 945 0/5
GPT-5.5 702 616 † 0.700 16.59 0.591 192 0.90 1.043 ‡ 3,143 1,306 2/5
Claude Opus 4.8 (max) 498 231 0.662 5.41 0.130 266 0.20 1.309 1,497 812 0/5
Claude Opus 4.7 (max) 259 111 0.811 0.120.189 156 1.75 1.421 1,023 432 0/5
Claude Opus 4.6 (max) 258 266 0.649 14.98 0.587 129 0.76 1.268 1,221 788 2/5
Gemini 3.5 Flash 190 79 0.777 2.13 0.450 36 0.38 0.918 2,508 2,628 0/5
Gemini 3.1 Pro 130 130 0.660 12.58 0.688 19 2.03 1.376 1,605 1,141 2/5
Open-weight
Qwen3.8-Max-Preview 416 111 0.713 6.13 0.242 173 0.38 0.8341,826 962 0/5
GLM 5.2 (high) 301 124 0.693 1.99 0.127137 0.59 1.434 1,467 672 0/5
Kimi K3 265 110 0.632 5.87 0.247 123 2.01 1.507 1,334 878 0/5
GLM 5.1 226 192 0.662 6.49 0.231 94 0.09 1.557 1,333 852 0/5
DeepSeek-V4-Pro-Preview
(max) 190 100 0.654 8.99 0.166 68 1.54 1.235 1,337 678 0/5
Qwen3.7-Max 165 134 0.616 9.85 0.433 59 −0.051.433 1,108 782 0/5
GLM 5.2 (max) 115 71 0.632 19.68 0.360 10 2.24 1.362 1,430 931 0/5
Kimi K2.6 70 14 0.596 17.22 0.377−27 0.42 1.548 1,087 1,017 0/5
Qwen3.6-Plus 47 28 0.625 10.68 0.583−40 3.03 1.333 1,325 1,023 0/5
Qwen3.5-Plus 1.1 11 0.625 20.11 0.979−92 5.88 1.860 1,076 800 4/5
4 Experimental Results
4.1 Experimental Setup
Eighteen models ran the 365-day task, eight proprietary and ten open-weight by our own assignment,
ranked within tier by mean total assets (Table 10). Each model received five independent episodes, 90
in all, under one fixed world. Requests use each provider’s default settings, with no temperature or
top_p sent and thinking force-enabled wherever a family exposes it (Table 10). Five episodes is a small
sample, so every mean in Table 2 is printed with its standard deviation (Miller, 2024; Kapoor et al., 2025).
Otherwise, all models shared the same 18 tools (Table 3), context window and group-wise eviction (§3.2.2),
and the memory store outside it (§3.2.3). The longest episode took 3,599 turns of the 4,000 allowed, and
all 90 ended on the simulated calendar or in bankruptcy rather than on that cap. One renderer voices
every supplier for every model, so wording varies between episodes while the economics it relays cannot
(§3.5.2). Scoring reduces the year to one number, the asset multiplier, end-of-year total assets over the
¥100,000 stake (Appendix E). A bankrupt episode stops on the tenth consecutive negative bank day and
still enters the average.
4.2 Overall Performance
Starting from the same stake in the same simulated year, the models finish orders of magnitude apart. A
factor of1,264separates GPT-5.6 Sol at the top from Qwen3.5-Plus at the bottom (Table 2, Figure 1). The
environment is deterministic given the action sequence (§4.1), so that range belongs to the agents rather
than to resampled demand. Proprietary systems take the top four places (Table 2). Qwen3.8-Max-Preview
leads the open-weight tier and places fifth overall. Inside the Qwen family each release earns more than
the one before it, and Qwen3.8-Max-Preview earns the most. The 3.6 to 3.7 step is worth noting, since
Qwen3.7-Max swings from¥6,290 to¥358,790 across its five years, and its worst year finishes below
every Qwen3.6-Plus year. Strong models go bankrupt too. Ten of the ninety episodes ended insolvent,
six of them under closed-source models. GPT-5.5, Claude Opus 4.6, Gemini 3.1 Pro and Qwen3.5-Plus
account for all ten, and the same four surrender more than half of peak total assets (§4.3.3). Ordering by
assets recovers only part of the skill behind it (Figure 2). Section 4.3 takes the axes one at a time, and
Appendix F carries the per-model table of every dimension.
16

Profit
Negotiation
Fraud
avoidance
SolvencyEfficiency
Execution
Learning
GPT-5.6 Sol
rank 1·7·16·9·2·17·4
profit leader, spiky
0.5
1.0
Profit
Negotiation
Fraud
avoidance
SolvencyEfficiency
Execution
Learning
Claude Opus 4.7
rank 8·1·1·5·6·12·11
skill without scale
18-model median
0.5
1.0
Profit
Negotiation
Fraud
avoidance
SolvencyEfficiency
Execution
Learning
Gemini 3.5 Flash
rank 12·2·3·13·13·5·2
skill without scale
0.5
1.0
Profit
Negotiation
Fraud
avoidance
SolvencyEfficiency
Execution
Learning
Fable5
rank 2·3·4·3·1·4·17
balanced
0.5
1.0
Profit
Negotiation
Fraud
avoidance
SolvencyEfficiency
Execution
Learning
GLM 5.2 (high)
rank 6·6·2·1·7·8·13
balanced
0.5
1.0
Profit
Negotiation
Fraud
avoidance
SolvencyEfficiency
Execution
Learning
Qwen3.8-Max-Preview
rank 5·4·7·7·5·6·1
top open-weight
0.5
1.0
Figure 9: Capability profiles for six of the 18 models. The primary score and the six dimensions of this
section run clockwise from the top, profit as mean end-of-year total assets, negotiation asCSE+, fraud
avoidance asBadSpend%, solvency as peak drawdown over peak total assets, efficiency as profit per tool
call, execution as the controllable return rate and learning asAnchorRatio. Fraud avoidance, solvency,
execution and learning are sign-flipped so that higher is better on every axis. Each axis is min-max
normalized over the 18 model means, so 1 marks the best mean and 0 the worst, with whiskers over the
five episodes and a dashed polygon at the median. Efficiency carries no episode spread, being a ratio of
5-run means, and the archivedAnchorRatio spread is a population std over a varying number of episodes,
so the learning axis draws no whisker either. No profile fills the polygon.
4.3 Multi-Dimensional Analysis
Six dimensions pull the year apart, each ranked by one recorded measure and defined in §3.7, with the
formulas, field names, and caveats in one appendix subsection per dimension (§E.1 to §E.6). Figure 9 sets
the primary score beside the six axes for six models, and Appendix F.8 carries all 18.
4.3.1 Negotiation Quality
No model bargains prices down to the supplier’s cost floor. Claude Opus 4.7 keeps the most of each
bargaining range at0.811and Kimi K2.6 the least at0.596, with the per-model values in Table 11.
Accepting the opening quote already scores0.50, so the field lands0.10to0.31above what taking the first
offer would have cost it (Appendix D.2). Which counterpart a model draws matters less than which model
it is, since the field spreads0.051across the six behavior templates against0.204across models, though
the per-model ordering inside a column still moves by as much as thirteen places (Figure 23). Agreement
rates sit at the top of their scale and separate nobody. Of the12,060concluded honest sessions, 73 end
without a deal, and 72 of those are the agent’s own rejection rather than a supplier walking away. Every
model settles at least96%of the honest sessions it concludes, so the ranking rests on how much a deal
captures rather than on how often one happens (Appendix E.1). The rate also leaves out the10.9%of
sessions a model opened mid-year and never came back to. Agents buy least from the counterparts that
concede least. The hardest of the six honest behavior templates (Appendix D.3) covers 48 of the 424
honest names on the supplier list, and those 48 take4.8%of the¥55.1M of honest procurement, against
at least14%for each of the five easier ones (Figure 24). Buying the same item from the same honest
supplier again costs more than a reshuffle of the prices already won would have, for 16 of the 18 models,
17

and §4.3.6 takes that up with the rest of the year’s trends.
4.3.2 Fraud Avoidance
Every model sends part of its procurement budget to suppliers that defraud it. Spending on them spans
more than 160-fold, cleanest at Claude Opus 4.7 and heaviest at Qwen3.5-Plus (Figure 25), and none
spends as though it never screened.BadSpend%counts money rather than refusals (§E.2), unlike a refusal
rate on scripted solicitations (Yang et al., 2025), so declining an offer the agent never sought earns no
credit. A share and a sum of money rank the models differently, because procurement budgets differ as
widely as the shares do. Qwen3.5-Plus gives up the largest share, yet GPT-5.6 Sol hands over fifty times
the cash on a smaller one (Table 12). Both readings rest on a handful of orders, and across five episodes
the standard deviation of the share exceeds its own mean for 15 of the 18 models. Losing money to fraud
does not cost a model its year. The cleanest buyer finishes mid-pack on assets and the profit leader is
16th of 18 onBadSpend%(§4.2), because a pre-deal scam inflates a price that still sits inside the honest
range and a post-deal scam delivers most of the goods (§3.5.4). Most of the money disappears after a
deal is signed. Defective lots take53.4%of everything reaching fraudulent suppliers and short shipments
the next largest slice (Figure 25), while membership-fee scams almost never land, three payments in the
whole evaluation. Models separate when they order, not when they choose whom to approach. Fraudulent
suppliers take close to their share of the supplier list in every model’s outreach (§3.5.2), and what differs
is how often an approach becomes an order, from4.0%for Claude Opus 4.7 to31.7%for GPT-5.6 Sol
(Figure 26, Appendix F.3). A negotiation that reaches its end almost always closes a deal (§4.3.1), so the
gap lies in the approaches a model abandons.
4.3.3 Cash Flow and Solvency
Money leaves the bank account weeks before it returns. Revenue waits nine days in escrow, then waits
again for a withdrawal (§3.4.2). No episode sees cash in the wallet before day 15, and 49 of the 90
bottom out in January. Two GPT-5.5 episodes went bankrupt on day 17, before a single yuan of revenue
had settled. Returns claw more money back out of escrow (§4.3.5). A fall recorded in yuan grows with
the balance at risk, and the largest of the field belongs to GPT-5.6 Sol, which also earned the most
(Appendix E.3). Dividing each fall by the peak total assets of its own episode separates the field on risk,
and the five models that surrendered more than half of peak include all four that ever went bankrupt
(Figure 27a, Table 13). Running the bank account below zero was rare and usually fatal. Seventeen of the
90 episodes went negative at a morning check across 177 such days, and ten of them went bankrupt. A
run ends only after ten consecutive overdrawn mornings, so one Claude Opus 4.6 episode absorbed fifteen
scattered overdrafts and survived. On 66 of those days the wallet already held the shortfall (Figure 27b).
No tool reports the streak (§3.2), so an agent cannot count the mornings it has failed. A large cash buffer
buys survival and caps growth. Three models kept the bank above¥15,000 in every episode and finished
sixth, tenth and eleventh, while the two biggest earners held the thinnest average buffers of the fourteen
solvent models. Qwen3.8-Max-Preview leads the open-weight field on a mid-field buffer, its bank above
zero all year.
4.3.4 Operational Efficiency
Fable5 earns more from a tool call than the leader does. Sitting second on total assets, it turns¥479 of
profit out of each call against GPT-5.6 Sol’s¥363, on59.9%fewer calls (Table 14). Three models finish
under their opening stake, so their calls average a loss over the year,¥92 a call at the worst. No fee
inside the economy charges for a call, so the bill falls on whoever deploys the agent and the score stays
blind to it (Kapoor et al., 2025). The Berkeley function-calling leaderboard reports that bill directly,
printing dollar cost and latency beside accuracy (Patil et al., 2025). Where the calls go describes a policy
better than their number does (Figure 10b). Shipping, advancing the day, withdrawing settled revenue
and publishing inventory absorb71.8%of all 18 models’ calls, a daily loop rather than a plan. Reading
state back takes another14.7%and supplier conversation6.0%, so the one channel that can change what
an item costs draws less than a fifteenth of the effort. Pricing barely registers in the call budget. One
call can revise many prices at once, yet0.66%of all calls do so. Nine of the 18 models average under
three such calls a year, leaving their listed prices to stand while season, promotion and reputation move
demand underneath them. The memory store draws almost no traffic. Notes the eviction pass cannot
reach (§3.2.3) take2.1%of the field’s calls. Claude Opus 4.8 gives it the largest share of its own budget,
4.7%at69.6calls a year against 20 slots, while GPT-5.5 makes the most calls outright at135.2and
Qwen3.5-Plus wrote to it in none of its five episodes. Twenty notes revised a few dozen times is what a
year of trading leaves behind.
18

100
 0 100 200 300 400 500
Profit per tool call, ¥
Fable5
GPT-5.6 Sol
Claude Opus 4.8
GPT-5.5
Qwen3.8-Max-Preview
Claude Opus 4.7
GLM 5.2 (high)
Claude Opus 4.6
Kimi K3
GLM 5.1
DeepSeek-V4-Pro-Preview
Qwen3.7-Max
Gemini 3.5 Flash
Gemini 3.1 Pro
GLM 5.2 (max)
Kimi K2.6
Qwen3.6-Plus
Qwen3.5-Plus
+479
+363
+266
+192
+173
+156
+137
+129
+123
+94
+68
+59
+36
+19
+10
-27
-40
-92
¥/call
0 20 40 60 80 100
share of that model's tool calls (%)
GPT-5.6 Sol
Gemini 3.5 Flash
Qwen3.8-Max-Preview
Fable5
GLM 5.2 (high)
Claude Opus 4.7
3,668.2
2,508.2
1,826.4
1,469.4
1,467.0
1,023.0
calls/run
10
14
20
25
25
36
20
25
19
24
24
35
23
17
9
12
9
11
17
23
21
10
8
9
7
23
36
12 7
wait ship publish withdraw negotiate poll state memory other
(a) What One T ool Call Earns
(b) Where the Budget Goes
Figure 10: (a) Profit per tool call for the 18 models, best first, mean total assets less the¥100,000 stake
divided by mean tool calls per episode. Bankrupt episodes are pooled into both means, and the three
models that finish under the stake sit left of zero. (b) Where six models spent their calls, over eight groups
of the 18 tools, scaled within each model.
4.3.5 Operations Execution
The controllable return rate counts the percentage points a model’s own pricing adds above the natural
rate of the goods it chose to sell, and it is the one return channel this axis charges to the agent. The points
run from−0.05for Qwen3.7-Max to5.88for Qwen3.5-Plus (Table 15). The natural rate underneath is
larger,5.31to21.25points, and it follows what a model chose to sell rather than how it priced. Twenty-six
of the 90 episodes carry a negative rate, priced under the reference. Added returns are worth buying when
the price that causes them pays for them. GPT-5.6 Sol books4.46points and the year’s largest refund
bill,¥1.62M, and finishes first on assets. Qwen3.5-Plus adds more return points than any other model
and finishes last. Freight speed is chosen once and left alone. The archive holds92,182fast dispatches
beside171 ,642standard and exactly one slow, and 72 of the 88 episodes that sold anything put at least
98%of shipments in one tier. Fast doubles the freight bill and cuts the return draw by a quarter, yet nine
models swing over 30 points in fast share between their own episodes, so the tier reads as sampling, not
policy. Store openings order nothing. Cumulative openings run from3.0for two Qwen models to9.0for
GPT-5.6 Sol, each charging the¥500 setup fee again and restarting a reopened type’s reputation at the
floor. GLM 5.2 (high) opened exactly four every episode and placed sixth, while Gemini 3.5 Flash opened
13 in one episode and placed twelfth, and neither is a profitable habit.
4.3.6 Learning over the Horizon
Two of the 18 models pay less on a repeat order than a reshuffling of the prices they already won from
that supplier would have cost. Qwen3.8-Max-Preview scores0.834onAnchorRatio and Gemini 3.5 Flash
0.918, where1.0means an agent’s price ordering is indistinguishable from a random ordering of its own
prices. The field median is1.369, and Qwen3.5-Plus reaches1.860(Table 16). Fifteen models miss their
own permutation null by more than two standard deviations in the expensive direction, which is what
an unrevised anchor on an early price produces (Lou & Sun, 2026). GPT-5.5 contributes three episodes
instead of five; its two bankrupt runs never buy the same item twice from the same supplier. A second
reading of the same year runs the same way, with sixteen of the 18 models capturing less surplus in the
19

0
500
1000
1500
2000
2500
3000
warehouse units
Jan 29, 2,207 units held;
the age-scaled fee reaches ¥428/day by May
Jan Feb Mar Apr May
2026
20
0
20
40
60
80
100
120
¥ thousand
opening stake ¥100k
Qwen3.5-Plus, Episode 0, One Collapse Day by Day
total assets bank balance warehouse stock
bank overdrawn
Jan 3, the bank falls ¥32.5k
Jan 22, ¥29.1k more,
total assets down to ¥38.4k
May 2 the bank turns negative with ¥20
in the wallet, May 11 the rule ends the episode
Figure 11: One bankruptcy episode day by day, Qwen3.5-Plus episode 0. Total assets and bank balance
are on the left axis, warehouse stock on the right, and the shaded band marks the days the bank balance
stayed negative.
second half of an episode than in the first. The surplus half-lift splits an episode’s honest sessions at the
median day and differences the two means (§E.6). Three mechanisms would hold that surplus trend flat,
and the evaluation separates none of them. Eviction destroys the tool result that carried a price already
won (§3.2.2). The memory store that survives eviction is barely used (§4.3.4). And no gradient reaches
inside an episode, so improvement must come from an agent reasoning over its own record (Shinn et al.,
2023). Qwen3.8-Max-Preview moves against the field, alone holding a positive per-day surplus trend and
alone beating its own shuffled prices by more than two standard deviations. Supplier choice drifts as well.
Fraudulent suppliers take a larger share of concluded sessions late in the year than early for 17 of the 18
models, so what moves over the horizon moves the wrong way.
4.4 Error Analysis
The six axes rank models without locating the mistake, since one payment to a supplier that cheats
surfaces as fraudulent spend and again as a deeper fall from peak assets. Ten recurring patterns therefore
get one detection rule each, with mechanisms and counts in Table 18 and Figure 30 of Appendix G.5.
Bankruptcy alone destroys the stake (§4.3.3). Inventory bought and never sold is the road there. One
Qwen3.5-Plus episode fills four stores in January, never sells its way out, and ends in May (Figure 11).
Fraudulent suppliers charge for value they never deliver, inflating prices before goods move and shipping
short afterwards. A second order with the same supplier is where most of the money goes: 943 of the
1,141 agreements struck with fraudulent suppliers sit in a supplier-item pair dealt with twice or more
(§4.3.2, Appendix E.1). No message names the supplier behind a bad lot, so the loss lands in the balance
instead of arriving as a signal. Money lost in bargaining is small per deal and never fatal. Honest deals
rarely close half the range available below, and the giveaway is the opening quote accepted unimproved
(§4.3.1). Claude Opus 4.7, Gemini 3.5 Flash and Fable5 never accept one and are the top three onCSE+,
Kimi K2.6 most often and last. Research gets re-derived instead of remembered. Of 2,180 catalog and
supplier queries, 746 repeat arguments already issued that episode. The repeats cost 7,460 simulated
minutes, 83 an episode against a 219,000-minute year, and sit beside a little-used memory store (§4.3.6).
Nothing in the economy charges for asking twice. The two-day shipping deadline binds only at the edges
of the year. Cancellations cluster in the first fortnight and again in the final two weeks, where the agent
has either not started shipping or has stopped (§4.3.5).
Three patterns often blamed for long-horizon failure do not survive the data. Store churn does not separate
the field (§4.3.5). Models that sign up for more promotions end richer, so event neglect explains nothing.
Late-year collapse holds only in part, growth dropping after the first quarter at a pairedt=− 3.95and
the closing window flat rather than recovering. Failure patterns spread across the whole field rather
than concentrating in the weakest models. Every model trips at least five rules, Gemini 3.1 Pro all
ten, and tripping fewer of them does not make a model richer. The cleanest profiles belong to the best
bargainers, not the richest, so the field reads as strong in patches and coordinated nowhere (transcripts in
Appendix G).
20

5 Conclusion
In this paper, we introduce E-Commerce Bench, a long-horizon benchmark in which an agent runs an
online retail business for a simulated 365-day year. The benchmark is built in four parts. An agent loop
drives one model call at a time and keeps a year of tool traffic inside the context window, with a persistent
memory beside it. Eighteen tools cover the merchant’s job, from market research and supplier chat to
pricing, shipping, and cash withdrawal. A deterministic environment decides what customers buy and
how suppliers bargain, computing over products, suppliers, and a calendar taken from a real e-commerce
platform. Purchases and returns follow a fixed demand model, and a deterministic negotiation kernel
makes every supplier price, concession, and accept/reject decision while an LLM only turns those decisions
into dialogue. Eighteen frontier and open-weight models each ran the year five times, scored on end-of-year
total assets and on six capabilities behind that number (§3.7). No model is strong on all seven. GPT-5.6
Sol earns the most, turning the¥100,000 stake into roughly 14 times as much, yet it ranks 16th of 18
on fraud avoidance and earns less per tool call than Fable5. Claude Opus 4.7 bargains best and avoids
fraud best while finishing mid-pack on money, and Qwen3.8-Max-Preview leads the open-weight models
at 4.2 times the stake. Four models go bankrupt in part of their runs, two GPT-5.5 episodes as early as
day 17, before any revenue had settled (§4.3.3). Beyond the retail domain, E-Commerce Bench offers a
foundational blueprint for next-generation agent evaluation. By proving thatdeterministic kernel control
eliminates evaluation noise in complex multi-party interactions, and thatmulti-dimensional diagnostics
are indispensable for catching diverse failure modes, we provide the methodology needed to push agent
benchmarks into ever-longer horizons.
21

References
Andon Labs. Vending-bench 2.https://andonlabs.com/evals/vending-bench-2, 2026. Andon Labs
evaluation report.
Tim Baarslag, Katsuhide Fujita, Enrico H. Gerding, Koen V. Hindriks, Takayuki Ito, Nicholas R. Jennings,
Catholijn M. Jonker, Sarit Kraus, Raz Lin, Valentin Robu, and Colin R. Williams. Evaluating practical
negotiating agents: Results and analysis of the 2011 international competition.Artificial Intelligence,
198:73–103, 2013. doi: 10.1016/j.artint.2012.09.004.
Tim Baarslag, Koen V. Hindriks, and Catholijn M. Jonker. Effective acceptance conditions in real-time
automated negotiation.Decision Support Systems, 60:68–77, 2014. doi: 10.1016/j.dss.2013.05.021.
Tim Baarslag, Mark J. C. Hendrikx, Koen V. Hindriks, and Catholijn M. Jonker. Learning about the
opponent in automated bilateral negotiation: A comprehensive survey of opponent modeling techniques.
Autonomous Agents and Multi-Agent Systems, 30(5):849–898, 2016. doi: 10.1007/s10458-015-9309-1.
Axel Backlund and Lukas Petersson. Vending-bench: A benchmark for long-term coherence of autonomous
agents, 2025. URLhttps://arxiv.org/abs/2502.15840.
Yushi Bai, Xin Lv, Jiajie Zhang, Hongchang Lyu, Jiankai Tang, Zhidian Huang, Zhengxiao Du, Xiao
Liu, Aohan Zeng, Lei Hou, Yuxiao Dong, Jie Tang, and Juanzi Li. Longbench: A bilingual, multitask
benchmark for long context understanding. In Lun-Wei Ku, Andre Martins, and Vivek Srikumar (eds.),
Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume
1: Long Papers), ACL 2024, Bangkok, Thailand, August 11-16, 2024, pp. 3119–3137. Association
for Computational Linguistics, 2024. doi: 10.18653/V1/2024.ACL-LONG.172. URL https:
//doi.org/10.18653/v1/2024.acl-long.172.
Kalyan Chatterjee and William Samuelson. Bargaining under incomplete information.Operations Research,
31(5):835–851, 1983. URLhttps://www.jstor.org/stable/170889.
Yanxu Chen, Zijun Yao, Yantao Liu, Amy Xin, Jin Ye, Jianing Yu, Lei Hou, and Juanzi Li. Stockbench:
Can llm agents trade stocks profitably in real-world markets?, 2026. URLhttps://arxiv.org/abs/25
10.02209.
Peyman Faratin, Carles Sierra, and Nick R. Jennings. Negotiation decision functions for autonomous
agents.Robotics and Autonomous Systems, 24(3–4):159–182, 1998. doi: 10.1016/S0921-8890(98)00029-3.
Guillermo Gallego and Garrett van Ryzin. Optimal dynamic pricing of inventories with stochastic
demand over finite horizons.Management Science, 40(8):999–1020, August 1994. ISSN 1526-5501. doi:
10.1287/mnsc.40.8.999. URLhttp://dx.doi.org/10.1287/mnsc.40.8.999.
John C. Harsanyi. Games with incomplete information played by “Bayesian” players, part I: The basic
model.Management Science, 14(3):159–182, 1967.
Muyu He, Adit Jain, Anand Kumar, Vincent Tu, Soumyadeep Bakshi, Sachin Patro, and Nazneen
Rajani. YC-Bench: Benchmarking ai agents for long-term planning and consistent execution, 2026. URL
https://arxiv.org/abs/2604.01212.
Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik
Narasimhan. Swe-bench: Can language models resolve real-world github issues?, 2024. URLhttps:
//arxiv.org/abs/2310.06770.
Sayash Kapoor, Benedikt Stroebl, Zachary S. Siegel, Nitya Nadgir, and Arvind Narayanan. AI agents that
matter.Trans. Mach. Learn. Res., 2025, 2025. URLhttps://openreview.net/forum?id=Zy4uFzMviZ.
Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, and Percy
Liang. Lost in the middle: How language models use long contexts.Trans. Assoc. Comput. Linguistics,
12:157–173, 2024. doi: 10.1162/TACL\_A\_00638. URLhttps://doi.org/10.1162/tacl_a_00638.
Jiaxu Lou and Yifan Sun. Anchoring bias in large language models: an experimental study.J. Comput.
Soc. Sci., 9(1):11, 2026. doi: 10.1007/S42001-025-00435-2. URLhttps://doi.org/10.1007/s42001
-025-00435-2.
Haotian Luo, Huaisong Zhang, Xuelin Zhang, Haoyu Wang, Zeyu Qin, Wenjie Lu, Guozheng Ma, Haiying
He, Yingsha Xie, Qiyang Zhou, Zixuan Hu, Hongze Mi, Yibo Wang, Naiqiang Tan, Hong Chen, Yi R.
Fung, Chun Yuan, and Li Shen. Ultrahorizon: Benchmarking agent capabilities in ultra long-horizon
scenarios, 2025. URLhttps://arxiv.org/abs/2509.21766.
22

Evan Miller. Adding error bars to evals: A statistical approach to language model evaluations, 2024. URL
https://arxiv.org/abs/2411.00640.
Charles Packer, Sarah Wooders, Kevin Lin, Vivian Fang, Shishir G. Patil, Ion Stoica, and Joseph E.
Gonzalez. Memgpt: Towards llms as operating systems, 2024. URLhttps://arxiv.org/abs/2310.0
8560.
Joon Sung Park, Joseph C. O’Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, and Michael S.
Bernstein. Generative agents: Interactive simulacra of human behavior. InProceedings of the 36th Annual
ACM Symposium on User Interface Software and Technology (UIST ’23). Association for Computing
Machinery, 2023. doi: 10.1145/3586183.3606763. URLhttps://doi.org/10.1145/3586183.3606763.
Shishir G. Patil, Huanzhi Mao, Fanjia Yan, Charlie Cheng-Jie Ji, Vishnu Suresh, Ion Stoica, and
Joseph E. Gonzalez. The berkeley function calling leaderboard (BFCL): from tool use to agentic
evaluation of large language models. In Aarti Singh, Maryam Fazel, Daniel Hsu, Simon Lacoste-Julien,
Felix Berkenkamp, Tegan Maharaj, Kiri Wagstaff, and Jerry Zhu (eds.),Forty-second International
Conference on Machine Learning, ICML 2025, Vancouver, BC, Canada, July 13-19, 2025, volume
267 ofProceedings of Machine Learning Research. PMLR / OpenReview.net, 2025. URL https:
//proceedings.mlr.press/v267/patil25a.html.
TejalPatwardhan, RachelDias, ElizabethProehl, GraceKim, MicheleWang, OliviaWatkins, SimónPosada
Fishman, Marwan Aljubeh, Phoebe Thacker, Laurance Fauconnet, Natalie S. Kim, Patrick Chao, Samuel
Miserendino, Gildas Chabot, David Li, Michael Sharman, Alexandra Barr, Amelia Glaese, and Jerry
Tworek. Gdpval: Evaluating ai model performance on real-world economically valuable tasks, 2025.
URLhttps://arxiv.org/abs/2510.04374.
J. Andrew Petersen and V. Kumar. Are product returns a necessary evil? antecedents and consequences.
Journal of Marketing, 73(3):35–51, May 2009. ISSN 1547-7185. doi: 10.1509/jmkg.73.3.035. URL
http://dx.doi.org/10.1509/jmkg.73.3.035.
Hannes M. Petrowsky, Lea Boecker, Yannik A. Escher, Marie-Lena Frech, Malte Friese, Adam D. Galinsky,
Brian Gunia, Alice J. Lee, Michael Schaerer, Martin Schweinsberg, Meikel Soliman, Roderick Swaab,
Eve S. Troll, Marcel Weber, and David D. Loschelder. The power and peril of first offers in negotiations:
A conceptual, meta-analytic, and experimental synthesis.Organizational Behavior and Human Decision
Processes, 191:104448, 2025. doi: 10.1016/j.obhdp.2025.104448.
Lingfei Qian, Xueqing Peng, Yan Wang, Vincent Jim Zhang, Huan He, Hanley Smith, Yi Han, Yueru He,
Haohang Li, Yupeng Cao, Yangyang Yu, Alejandro Lopez-Lira, Peng Lu, Jian-Yun Nie, Guojun Xiong,
Jimin Huang, and Sophia Ananiadou. When agents trade: Live multi-market trading benchmark for
llm agents, 2025. URLhttps://arxiv.org/abs/2510.11695.
Howard Raiffa.The Art and Science of Negotiation. Harvard University Press, 1982.
Paul Resnick, Ko Kuwabara, Richard Zeckhauser, and Eric Friedman. Reputation systems.Commun. ACM,
43(12):45–48, 2000. doi: 10.1145/355112.355122. URLhttps://doi.org/10.1145/355112.355122.
Ariel Rubinstein. Perfect equilibrium in a bargaining model.Econometrica, 50(1):97–109, 1982. doi:
10.2307/1912531.
Qiming Shi, Yulong Tao, Linbo Jin, Zhaolu Kang, Yibo Dou, Jiawen Zhu, Tianjun Pan, Shaokang Fu,
Chengyu Wang, Siyue Li, Yaping Cheng, Di Weng, and Chengfu Huo. Merchantbench: Benchmarking
llm agents for long-term coherence in e-commerce operations, 2026. URLhttps://arxiv.org/abs/26
07.28956.
Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao. Reflexion:
language agents with verbal reinforcement learning. In Alice Oh, Tristan Naumann, Amir Globerson,
Kate Saenko, Moritz Hardt, and Sergey Levine (eds.),Advances in Neural Information Processing
Systems 36: Annual Conference on Neural Information Processing Systems 2023, NeurIPS 2023, New
Orleans, LA, USA, December 10 - 16, 2023, 2023. URLhttp://papers.nips.cc/paper_files/pap
er/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html.
Theodore R. Sumers, Shunyu Yao, Karthik Narasimhan, and Thomas L. Griffiths. Cognitive architectures
for language agents.Trans. Mach. Learn. Res., 2024, 2024. URLhttps://openreview.net/forum?i
d=1i6ZCvflQJ.
Richard S. Sutton and Andrew G. Barto.Reinforcement Learning: An Introduction. MIT Press, Cambridge,
MA, 2nd edition, 2018.
23

Yoshiki Takenami, Yin Jou Huang, Yugo Murawaki, and Chenhui Chu. How does cognitive bias affect
large language models? a case study on the anchoring effect in price negotiation simulations. In
Christos Christodoulopoulos, Tanmoy Chakraborty, Carolyn Rose, and Violet Peng (eds.),Findings of
the Association for Computational Linguistics: EMNLP 2025, pp. 4481–4498, Suzhou, China, November
2025. Association for Computational Linguistics. ISBN 979-8-89176-335-7. doi: 10.18653/v1/2025.findi
ngs-emnlp.240. URLhttps://aclanthology.org/2025.findings-emnlp.240/.
Kian Siong Tey, Michael Schaerer, Nikhil Madan, and Roderick I. Swaab. The impact of concession patterns
onnegotiations: Whenandwhydecreasingconcessionsleadtoadistributivedisadvantage.Organizational
Behavior and Human Decision Processes, 165:153–166, 2021. doi: 10.1016/j.obhdp.2021.05.003.
Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, and
Anima Anandkumar. Voyager: An open-ended embodied agent with large language models, 2023. URL
https://arxiv.org/abs/2305.16291.
Tianbao Xie, Danyang Zhang, Jixuan Chen, Xiaochuan Li, Siheng Zhao, Ruisheng Cao, Toh Jing Hua,
Zhoujun Cheng, Dongchan Shin, Fangyu Lei, Yitao Liu, Yiheng Xu, Shuyan Zhou, Silvio Savarese,
Caiming Xiong, Victor Zhong, and Tao Yu. Osworld: Benchmarking multimodal agents for open-ended
tasks in real computer environments, 2024. URLhttps://arxiv.org/abs/2404.07972.
Frank F. Xu, Yufan Song, Boxuan Li, Yuxuan Tang, Kritanjali Jain, Mengxue Bao, Zora Z. Wang,
Xuhui Zhou, Zhitong Guo, Murong Cao, Mingyang Yang, Hao Yang Lu, Amaad Martin, Zhe Su,
Leander Maben, Raj Mehta, Wayne Chi, Lawrence Jang, Yiqing Xie, Shuyan Zhou, and Graham
Neubig. Theagentcompany: Benchmarking llm agents on consequential real world tasks, 2025. URL
https://arxiv.org/abs/2412.14161.
Shu Yang, Shenzhe Zhu, Zeyu Wu, Keyu Wang, Junchi Yao, Junchao Wu, Lijie Hu, Mengdi Li, Derek F.
Wong, and Di Wang. Fraud-r1 : A multi-round benchmark for assessing the robustness of LLM against
augmented fraud and phishing inducements. In Wanxiang Che, Joyce Nabende, Ekaterina Shutova, and
Mohammad Taher Pilehvar (eds.),Findings of the Association for Computational Linguistics: ACL
2025, pp. 4374–4420, Vienna, Austria, July 2025. Association for Computational Linguistics. ISBN
979-8-89176-256-5. doi: 10.18653/v1/2025.findings-acl.226. URL https://aclanthology.org/2025.
findings-acl.226/.
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao. React:
Synergizing reasoning and acting in language models. InThe Eleventh International Conference on
Learning Representations (ICLR), 2023. URLhttps://openreview.net/forum?id=WE_vluYUL-X.
Yi Zeng, Hongpeng Lin, Jingwen Zhang, Diyi Yang, Ruoxi Jia, and Weiyan Shi. How johnny can persuade
LLMs to jailbreak them: Rethinking persuasion to challenge AI safety by humanizing LLMs. In
Lun-Wei Ku, Andre Martins, and Vivek Srikumar (eds.),Proceedings of the 62nd Annual Meeting of
the Association for Computational Linguistics (Volume 1: Long Papers), pp. 14322–14350, Bangkok,
Thailand, August 2024. Association for Computational Linguistics. doi: 10.18653/v1/2024.acl-long.773.
URLhttps://aclanthology.org/2024.acl-long.773/.
Erica Zhang, Fangzhao Zhang, Aneesh Pappu, Batu El, Jose Blanchet, Susan Athey, Jiashuo Liu,
and James Zou. Terms-bench: Diagnosing llm negotiation agents beyond deal rate, 2026a. URL
https://arxiv.org/abs/2605.13909.
Jenny Zhang, Shengran Hu, Cong Lu, Robert Lange, and Jeff Clune. Darwin godel machine: Open-ended
evolution of self-improving agents, 2026b. URLhttps://arxiv.org/abs/2505.22954.
Linghua Zhang, Jun Wang, Jingtong Wu, and Zhisong Zhang. Retailbench: Evaluating long-horizon
autonomous decision-making and strategy stability of llm agents in realistic retail environments, 2026c.
URLhttps://arxiv.org/abs/2603.16453.
Wanjun Zhong, Lianghong Guo, Qiqi Gao, He Ye, and Yanlin Wang. Memorybank: Enhancing large
language models with long-term memory. In Michael J. Wooldridge, Jennifer G. Dy, and Sriraam
Natarajan (eds.),Thirty-Eighth AAAI Conference on Artificial Intelligence, AAAI 2024, Thirty-Sixth
Conference on Innovative Applications of Artificial Intelligence, IAAI 2024, Fourteenth Symposium
on Educational Advances in Artificial Intelligence, EAAI 2024, February 20-27, 2024, Vancouver,
Canada, pp. 19724–19731. AAAI Press, 2024. doi: 10.1609/AAAI.V38I17.29946. URL https:
//doi.org/10.1609/aaai.v38i17.29946.
Deyao Zhu, Xin Zhou, Shengling Qin, Xuekai Zhu, Hangliang Ding, Shu Zhong, Zixin Wen, Zhonglin
Xie, Chenhui Gou, Linxuan Ren, Yueyang Wang, Junfeng Zhong, Rui Liu, Tian Gao, Yangguang
Lin, Jingyuan Zhang, Maojia Song, Xuan Qi, Jinhong Wu, Chenyang Zhang, Yinzhu Piao, Ziru Niu,
24

Hongbin Lin, Lingxiang Meng, Peng Tang, Chengyao Tang, Shanyu Wu, Huanyu Zheng, Yu Liu, Liya
Zhu, He Wang, Ming Ding, Ziyu Wan, Hao Liu, Sibo Wang, Haotian Zhu, Xintian Zhang, Nan Chai,
Yipeng Liu, Panhao Lai, Sihang Yuan, Zixin Su, Ge Zhang, Wangchunshu Zhou, Yantao Du, Wenhao
Huang, and Guang Shi. Edgebench: Unveiling scaling laws of learning from real-world environments,
2026. URLhttps://arxiv.org/abs/2607.05155.
Yuxuan Zhu, Tengjun Jin, Yada Pruksachatkun, Andy Zhang, Shu Liu, Sasha Cui, Sayash Kapoor, Shayne
Longpre, Kevin Meng, Rebecca Weiss, Fazl Barez, Rahul Gupta, Jwala Dhamala, Jacob Merizian, Mario
Giulianelli, Harry Coppock, Cozmin Ududec, Antony Kellermann, Jasjeet S. Sekhon, Jacob Steinhardt,
Sarah Schwettmann, Arvind Narayanan, Matei A. Zaharia, Ion Stoica, Percy Liang, and Daniel Kang.
Establishing best practices in building rigorous agentic benchmarks. In Danielle Belgrave, Cheng Zhang,
Laura N. Montoya, Hsuan-Tien Lin, Razvan Pascanu, Piotr Koniusz, Marzyeh Ghassemi, Nancy Chen,
Iván Vladimir Meza Ruíz, and Arturo Loaiza-Bonilla (eds.),Advances in Neural Information Processing
Systems 38: Annual Conference on Neural Information Processing Systems 2025, NeurIPS 2025, San
Diego, CA, USA, December 2-7, 2025 / Mexico City, Mexico, November 30 - December 5, 2025, 2025.
URL http://papers.nips.cc/paper_files/paper/2025/hash/f316275b44ee2de533102913828a8
107-Abstract-Datasets_and_Benchmarks_Track.html.
25

Table 3: The 18-tool action space, grouped as in Figure 3, with the simulated minutes each call charges
against the 600-minute working day.
Tool min Effect on environment state
Market Research
market_search30 Three disclosure levels over store types, their categories, and one category’s sales
band with qualitative return and margin labels
supplier_search10 Name, contact, and categories served, no price, rating, or honesty signal
Store Operations
trace_return_sources10 Attributes pooled warehouse stock to the suppliers that delivered it
open_store60 Opens one of the 12 store types for the¥500 setup fee, at most 4 at once
close_store30 Shuts a store for good, moving shelf stock to the warehouse or salvaging it at
10% of purchase cost
check_store_status10 Yesterday’s revenue, returns, shipping cost, and per-SKU velocity for one store,
or a roll-up over all
set_prices10 Rewrites retail prices on a shelf, effective at the next daily trigger
join_promotion10 Enrolls a store in a calendar promotion at a discount of 0.05 to 0.50
Inventory Management
list_products10 Sellable SKUs with reference price and size, by store type or category
check_warehouse10 Lists warehouse quantities with the purchase price paid for them
publish_to_store20 Lists warehouse SKUs on a store page, storage fees still accruing
return_to_warehouse15 Delists shelf units back into the warehouse allocation pool
ship_orders20 Charges shipping, books net revenue into a 9-day escrow batch, and seeds the
order’s returns from the chosen speed
Financial Management
check_balance10 Reads bank, wallet, escrow, unshipped sales value, and settlement dates
withdraw10 The only way cash leaves the platform wallet for the bank account
Supplier Negotiation
chatbox30 One free-form message to a supplier, or to many at the same charge, routing
fencednegotiateactions to the Negotiation Kernel (§3.5)
Memory Operations
operate_memory10 Adds, reads, updates, or deletes one of 20 memory entries held outside the
context window
Time Advancement
wait_for_next_day0 Jumps to 08:00 tomorrow, forfeiting the minutes left today, and fires the daily
pipeline
A Agent Harness and Interface
A model sees the environment only through tool schemas and tool replies. Nothing else is sent to it, so
every notice the environment has to deliver rides inside a reply. The price list comes first, then the format
of a reply, then the eviction algorithm that holds a year of transcript inside a 128,000-token window.
Sections 3.2 and 3.3 give the outline, and Table 3 the price list. Prompts are reproduced separately in
Appendix H, and the eviction schematic with Section 3.2.2.
A.1 The Interface Contract
Every tool call comes back as a single string. Structured results arrive as JSON, plain text unchanged.
Extra notices sit inside that JSON rather than after its closing brace, so the reply still parses. Day-scoped
notices attach to the day-advance result when the batch holds one and to the last response otherwise, so
news is never blamed on an unrelated earlier call.
The morning pass reports far less to the agent than it computes. Of the 17 fields it assembles, at most
three reach the agent, the date, the day index and the news feed. Across the 90 archived episodes the
channel carried 8,301 items, 6,722 of them deliveries at one aggregated line per day.
Listing 1 shows two real tool messages, one at a day boundary and one carrying the solvency warning
that preceded a bankruptcy.
{" c u r r e n t _ t i m e ": "2026 -01 -09 T08 :00:00" , " day ": 8 , " s y s t e m _ n o t i f i c a t i o n s ": [{" date ": "2026 -01 -09" , " day
": 8 , " news ": [{" type ": " d eli ve ry " , " content ": " D e l i v e r i e s arrived :\ n - 20 x D r e a m M i s t LED
Ceiling Light for Living Room and Bedroom , Mod from Crystal Trading "}]}]}
< system_warning > Token usage : 1 0 8 5 9 3 / 1 2 8 0 0 0 tokens (84%) ; 19407 remaining </ system_warning >
26

1 60 120 180 240 300 365
simulated day
0.0
0.5
1.0
1.5
2.0
2.5
3.0cumulative tokens evicted (millions)
±1 standard
deviation
Gemini 3.5 Flash, 40 evictions
GPT-5.6 Sol, 36 evictions
Qwen3.8-Max-Preview, 19 evictions
Fable5, 13 evictions
GLM 5.2 (high), 12 evictions
Kimi K3, 11 evictions
DeepSeek-V4-Pro-Preview, 9 evictions
0
5
10
15
20
multiples of the context window
Figure 12: How often the context editor fired, over the 90 evaluated episodes. Each event is one eviction
pass. A model that never reaches the ceiling evicts nothing.
{" p e n d i n g _ s h i p m e n t s ": [] , " count ": 0 , " note ": " Ship with s h i p _ o r d e r s ( speed : fast / sta nd ard / slow ) .
Faster ship costs more but reduces returns ; slow is cheap but raises returns . U n s h i p p e d orders
cancel after the de adl in e ( lost sale + r e p u t a t i o n hit ) ." , " c u r r e n t _ t i m e ": "2026 -01 -03 16:40" , "
b a l a n c e _ r e m i n d e r ": " Your current balance (¥10.00) is below the daily o p e r a t i n g cost (¥60.00) . If
your bank account stays ne gat iv e for 10 c o n s e c u t i v e days , you will go ba nkr up t ."}
< system_warning > Token usage : 9 3 8 5 6 / 1 2 8 0 0 0 tokens (73%) ; 34144 remaining </ system_warning >
Listing 1: Two tool messages exactly as they entered the request, from GPT-5.6 Sol run 0 on day 8 and
from GPT-5.5 run 1 on 2026-01-03. The first carries the day notice, the second a low-balance reminder,
and both close with the token gauge that sits outside the JSON. The second run went bankrupt.
A.2 Loop Control and Context Editing
Token counts come from a local tokenizer rather than the provider’s own report, and cover the text, the
tool calls and the reasoning trace of each message. Opaque artifacts such as replayed encrypted reasoning
items are excluded, as are the tool schemas held outside the budget (§3.2.2). The system prompt quotes
the model the 120,000-token threshold, the 60,000-token release floor and the two protected groups. One
pass proceeds as follows.
1. Sum the counts of every message not already marked cleared. Below that ceiling the pass emits the
usage string and frees nothing.
2. Scan for groups from the third message onward, leaving the system message and the first user turn
permanently out of reach. A group opens at an assistant message carrying tool calls and closes after
the last consecutive tool response behind it.
3. Set aside the two most recent groups not yet cleared. With two or fewer active groups the pass clears
nothing at all, so a history made of a few very large groups can sit above the ceiling indefinitely.
4. Take the release target as the larger of that floor and the current overshoot past the ceiling.
5. Walk the clearable groups oldest first, marking each cleared and accumulating its count, and stop at
the first group that meets the target.
6. Rebuild the request from the surviving messages, skipping cleared entries entirely (§3.2.2).
Whether a pass ever fires depends on how a model spends the window, and Figure 12 counts the passes of
each of the 90 episodes.
Two kinds of message can never be evicted, an assistant turn of plain text and the idle warning. Neither
opens a group nor falls inside one, so both accumulate for the whole episode. Clearing whole groups is
what keeps the transcript valid, since every provider protocol here rejects a tool response separated from
its call.
27

Table 4: The 60 released categories, grouped by the store type that may list them, each heading giving
that type’s difficulty tier and daily operating cost. Reference-price bands are platform-wide and per SKU,
and the agent never sees the numeric return band its categories carry.† marks the 20 categories whose
agent-facing return sentence understates that band, which Table 5 gives per store type.
Category Reference price (¥)
Auto & Hardware, T1,¥130/day
Auto Accessories 10–400
Hardware & Tools 5–200
Electrical Supplies 3–80
Electronic Components 1–50
E-Vehicles & Parts 100–1,200
Agricultural Supplies 10–400
Industrial & Lab Supplies 10–200
Daily & Office, T1,¥130/day
Cleaning & Hygiene† 5–60
Gifts & Party Supplies† 5–80
Lifestyle Accessories† 20–400
Stationery & Office Supplies† 3–80
Office Equipment† 20–600
Medical Devices† 10–800
Food & Beverage, T1,¥130/day
Snacks & Nuts† 8–60
Groceries & Staples† 10–80
Coffee & Beverages† 10–60
Fresh Food & Meat† 15–120
Alcoholic Beverages† 20–500
Health Supplements† 30–200
Category Reference price (¥)
Home & Living, T1,¥130/day
Furniture 100–800
Bedding† 30–400
Household Essentials† 3–50
Storage & Organization† 10–100
Lighting† 15–500
Home Building Materials† 20–400
Basic Construction Materials† 10–200
Cleaning Tools† 5–50
Kitchenware† 8–200
Appliance & Digital, T2,¥100/day
Major Appliances 500–2,500
Small Appliances 50–600
Audio & Video Electronics 100–1,500
Smartphones 300–3,000
Laptops 800–5,000
Computer Hardware & Peripherals 30–800
3C Digital Accessories 5–150
Storage Devices 20–400
Networking Equipment 30–500
Fashion, T2,¥100/day
Women’s Fashion 30–300
Men’s Clothing 30–250
Underwear & Loungewear 15–120
Fashion Accessories 10–150
Sportswear & Casual 30–250
Category Reference price (¥)
Mother & Baby, T2,¥100/day
Children’s Clothing 15–100
Children’s Shoes 20–120
Baby Products 15–400
Maternity Products 20–200
Toys & Educational 15–600
Shoes & Bags, T2,¥100/day
Women’s Shoes 40–400
Men’s Shoes 50–400
Sneakers 80–600
Bags & Luggage 50–1,000
Beauty, T3,¥60/day
Skincare & Beauty 15–400
Beauty Devices 80–1,000
Personal Care & Massage 30–600
Pet Supplies, T3,¥60/day
Pet Supplies 8–150
Sports & Outdoor, T3,¥60/day
Sports & Fitness 15–300
Sports Bags & Accessories 30–400
Outdoor & Camping 20–600
Toys & Entertainment, T3,¥60/day
Collectibles & Figures 15–500
Gaming & Accessories 30–1,000
B Data Layer
Every quantity the released data layer holds is recorded here, so a reader can check any number the report
quotes against its table. How a supplier behaves once bargaining starts belongs to Appendix D instead.
The catalog carries 6,886 SKUs, 60 category parameter rows, 576 suppliers and 12 store types, and the
calendar 10 market events and 8 promotions, every one of them frozen, so the world is identical for every
model and every run.
B.1 Category Parameters
The released columns that decide margin are the ones that never reach the agent, namely the three
per-category price ratios, the elasticity family and its parameter and the two ends of the return band. A
SKU’s own natural rate becomes readable only throughtrace_return_sources once stock has moved
(§3.6.2). Each category belongs to exactly one store type, and Table 4 groups all 60 that way, each group
heading carrying that type’s difficulty tier and daily operating cost while Table 5 carries its return band
and cost-floor ratio. Setup fee and commission are identical across the 12, leaving the seasonal curve and
the demand terms of §3.4 as the only differences the two tables do not show. Category rows set bands and
per-SKU rows sit inside them. Reference price and natural return rate vary by SKU within the category
band while base demand does not, and one elasticity family serves a whole category. The wholesale ratio
is pinned to the cost-floor ratiocj /vj in all 60 rows (§D.2).
B.2 Store Types, Seasonality, and Physical Cost
A merchant fixes the store type once and cannot tune it afterwards without paying the setup fee again.
Table 5 names all 12 with the difficulty tier, operating cost and category span each carries.
Figure 14 gives the seasonal grid in full, one multiplier per store type and calendar month. Amplitude,
not level, separates the types. Nine of the 12 attain their annual maximum in November, inside the same
weeks as the calendar’s longest promotion window (Table 6), while Food & Beverage inverts the pattern
and peaks in February, so a portfolio timed for one season pays for it in the other. Four types stay within
±0.2of neutral all year and can be run without timing at all. Disclosure is exact rather than qualitative,
the index market_search returns being precisely100σ. Parcel size turns straight into cost, freight and
daily storage both scaling with it while the shipping speed the agent picks multiplies freight and the
order’s return rate together. Appendix C gives all four schedules with the rest of the cost model.
28

1 20 40 60
category, ranked by catalog depth
101
102
103
SKUs (log scale)
Women's Fashion 733
median 39.5
(a) 6,886 SKUs over 60 Categories
1 10 100 1,000
reference price (¥, log scale)
0
200
400
600SKUs
median ¥129
(b) Reference Price, ¥1.4 to ¥4,969
0 10 20 30 40 50
natural return rate (%)
Pet Supplies (tier 3)
Auto & Hardware (tier 1)
T oys & Entertainment (tier 3)
Sports & Outdoor (tier 3)
Mother & Baby (tier 2)
Beauty (tier 3)
Appliance & Digital (tier 2)
Shoes & Bags (tier 2)
Home & Living (tier 1)
Food & Beverage (tier 1)
Daily & Office (tier 1)
Fashion (tier 2)
(c) Return Rate by Store T ype
1 20 40 60
category, same order as panel (a)
0
4
8
12suppliers
floor of 7 honest and 2 fraudulent per category
(d) 576 Suppliers, Flat Coverage
honest (424) fraudulent (152)
Figure 13: The released data. (a) Products per category. (b) Reference prices. (c) Natural return rate by
store type, T the difficulty tier. (d) Suppliers per category against catalog depth.
Table 5: The 12 store types, by difficulty tier. Reference-price band, category count, seasonal range, tier
and operating cost are visible to the agent, while the wholesale ratios are not, so the achievable cost must
be discovered by negotiating. Opening ratio is a supplier’s first quote over the reference price and floor
ratio the lowest an honest supplier accepts, averaged over the store’s categories, so their gap is the room
negotiation can win. Return rate is natural, before pricing or shipping move it.
Store type Cats Ref. price (¥) Return rate (%) Opening / floor Seasonal range Ops (¥/day)
difficulty tier 1 hard
Auto & Hardware 7 1 to 1,200 0 to 8 0.93 / 0.86 0.90 to 1.10 130
Daily & Office 6 3 to 800 20 to 35 0.77 / 0.54 1.00 to 1.20 130
Food & Beverage 6 8 to 500 20 to 35 0.78 / 0.55 0.60 to 1.60 130
Home & Living 9 3 to 800 20 to 35 0.86 / 0.72 0.90 to 1.30 130
difficulty tier 2 medium
Appliance & Digital 9 5 to 5,000 0 to 20 0.79 / 0.58 0.90 to 1.40 100
Fashion 5 10 to 300 20 to 55 0.70 / 0.39 0.70 to 1.55 100
Mother & Baby 5 15 to 600 0 to 20 0.70 / 0.40 1.00 to 1.20 100
Shoes & Bags 4 40 to 1,000 0 to 55 0.80 / 0.60 0.80 to 1.40 100
difficulty tier 3 easy
Beauty 3 15 to 1,000 0 to 20 0.69 / 0.38 1.00 to 1.30 60
Pet Supplies 1 8 to 150 0 to 3 0.61 / 0.22 1.00 to 1.10 60
Sports & Outdoor 3 15 to 600 0 to 20 0.58 / 0.18 0.80 to 1.30 60
Toys & Entertainment 2 15 to 1,000 0 to 10 0.65 / 0.29 1.00 to 1.70 60
B.3 Event and Promotion Calendar
An agent is warned about a promotion but not about an event. An event posts its news on its first day
and gives no lead time, while a promotion is announced up to seven days before its first window opens
and join_promotion accepts a target 30 days ahead, so inventory can be positioned for a promotion and
never for an event. The two calendars touch only where the Guangdong factory fire of March 1 to 7 runs
across the March 4 to 8 Spring Blossom Sale, a supply shock rather than a demand one, which keeps
every measured discount response uncontaminated.
An event with no demand term bites only the purchase orders placed while its window is open, since the
lead time is fixed at placement and stock already in transit keeps the arrival date it was given. Table 6
prints the calendar in full, every date, phase, per-store-type demand multiplier and delivery-delay factor.
29

Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
month of the simulated year
Auto & Hardware (tier 1)
Daily & Office (tier 1)
Food & Beverage (tier 1)
Home & Living (tier 1)
Appliance & Digital (tier 2)
Fashion (tier 2)
Mother & Baby (tier 2)
Shoes & Bags (tier 2)
Beauty (tier 3)
Pet Supplies (tier 3)
Sports & Outdoor (tier 3)
T oys & Entertainment (tier 3)
1 0.9 1.1 1.1 1 1 1 1 1 1 1.1 1
1 1 1 1 1 1 1 1.1 1.2 1 1 1
1.3 1.6 1 0.9 0.9 0.8 1.1 1.1 1.3 0.9 0.6 1.5
1 0.9 1.1 1.1 1 1.2 1 1 1 1 1.3 1
1 0.9 1 1 1 1.3 0.9 1 1 1 1.4 1.1
0.75 0.7 1 0.95 0.85 1 0.8 0.8 0.95 0.85 1.55 0.85
1 1 1 1 1.1 1.2 1 1 1.1 1 1.2 1
0.9 0.8 1.1 1.1 1 1.2 0.9 0.9 1 1 1.4 1
1 1 1.3 1 1 1.2 1 1 1 1 1.3 1
1 1 1 1 1 1 1 1 1 1 1.1 1
0.8 0.8 1 1.2 1.3 1.2 1.3 1.2 1 1 1 0.8
1.2 1 1 1 1.1 1.2 1.1 1 1 1 1.7 1.3
0.6 1 1.4
 trough to peak
1.22×
1.20×
2.67×
1.44×
1.56×
2.21×
1.20×
1.75×
1.30×
1.10×
1.62×
1.70×
peak /
trough
0.6 0.8 1 neutral 1.3 1.7
demand multiplier  applied to every SKU of the store type
Figure 14: The monthly seasonality multiplier for all 12 store types, rows grouped by difficulty tier. The
right panel gives each type’s trough, peak and peak-to-trough ratio.
Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
month of the simulated year, 2026-01-01 to 2026-12-31
0
1
2
3demand multiplier, 1 = no effect
promotion, agent opts in event, demand lifted event, demand suppressed supply-only event
New Year
Kickoff
×2.0, b=1.5
Winter
Clearance
×1.8, b=1.5
Spring
Blossom
×2.5, b=1.8
Midyear
Mega
×3.0, b=2.0
Members
Days
×2.0, b=1.5
Autumn
Harvest
×2.0, b=1.5
Autumn
Carnival
×3.5, b=2.0
Year-End
Finale
×2.5, b=1.8
Winter
Storm
×0.2 2.0
delay ×2.5
Factory
Fire
delay ×4.0
Flu
Outbreak
×0.4 2.5
delay ×2.0
Hub
Shutdown
delay ×5.0
Summer
Heatwave
×0.3 3.0
delay ×2.0
Product
Recall
×0.4 0.6
T yphoon
×0.2 2.5
delay ×3.0
Economic
Downturn
×0.5 1.3
Material
Shortage
delay ×3.0
Cold Wave
×0.3 2.5
delay ×2.0
Figure 15: The 2026 calendar. Eight promotions the agent can join by choosing a discount, and ten events
it cannot opt out of. Promotion bars show the multiplier a30%discount buys, event bars their extreme
per-store-type multiplier.
B.4 The Supplier List
The supplier list is frozen, so the difficulty mix every model faces is a property of the benchmark rather
than a per-run draw. Each row carries an identity, an honest-or-fraudulent label, a behavior template, a
scam type where one applies, the single category served and a bankruptcy threshold in orders, and counts
land at 424 honest and 152 fraudulent over the 60 categories, 7 or 8 against 2 or 3 in each. A supplier’s
name carries no signal and its email carries one (§B.5), while what a template or a scam does at the table
belongs to Appendices D.3 and D.5.
30

Table 6: The fixed calendar of the simulated year, 10 events above and 8 promotions below, store types
named by their first word. Event demand multipliers are keyed by store type rather than by category,
so an event misses a store whose type it does not name, and only the largest active delay applies. A
promotion moves demand only if the agent joins it, at the ceiling shown for a 30% discount.
Market events, unavoidable
Event Window (2026) Demand multiplier by store
type
Supply effect
Winter Storm Jan 15 to Jan 18 Food×2, Home×1.5, Sports
×0.2, Fashion×0.3
lead time×2.5, all store types
Factory Fire in Guangdong Mar 1 to Mar 7 none lead time×4, Appliance, Toys
Flu Outbreak Apr 10 to Apr 16 Daily×2.5, Beauty×1.5,
Sports×0.4, Toys×0.5
lead time×2, Daily
Logistics Hub Shutdown May 20 to May 24 none lead time×5, all store types
Summer Heatwave Jul 5 to Jul 11 Appliance×3, Food×2, Sports
×0.3, Home×0.5
lead time×2, Appliance
Celebrity Product Recall Aug 20 to Aug 24 Beauty×0.4, Fashion×0.6 none
Typhoon Warning Sep 15 to Sep 17 Food×2.5, Daily×2, Fashion
×0.2, Shoes×0.2
lead time×3, all store types
Economic Downturn News Oct 5 to Oct 11 Food×1.3, Daily×1.2,
Appliance×0.5, Shoes×0.5,
Fashion×0.6
none
Raw Material Shortage Nov 20 to Nov 26 none lead time×3, Appliance, Home,
Auto; cost term inert
Cold Wave Dec 20 to Dec 24 Home×2.5, Fashion×2, Sports
×0.3, Food×0.4
lead time×2, all store types
Promotions, which the agent opts into with a discount
Promotion Windows (2026), every phase listed Max demand Elasticity boost
New Year Kickoff Sale Jan 1 to Jan 7×2×1.5
Winter Clearance Festival Jan 29 to Feb 6×1.8×1.5
Spring Blossom Sale Mar 4 to Mar 8×2.5×1.8
Midyear Mega Sale May 29 to May 31, Jun 14 to Jun 18×3×2
Summer Members Days Aug 6 to Aug 8×2×1.5
Autumn Harvest Sale Sep 2 to Sep 9×2×1.5
Grand Autumn Carnival Oct 15 to Oct 16, Oct 20 to Oct 21, Oct 31 to
Nov 14
×3.5×2
Year-End Finale Sale Dec 8 to Dec 14×2.5×1.8
B.5 Properties a Reader Should Check
Four properties of the released files look odd on inspection, and each was checked against the code that
reads them. Two carry consequences for a measurement.
1. Return-rate wording understates the numeric band.Twenty of the 60 categories carry a sentence
reading low or very low against a numeric band reaching 20% to 35%, marked in Table 4. The sentence
is what market_search shows, so a merchant who prices off the wording underestimates returns across
categories holding 25.5% of all SKUs, and sees the gap only throughtrace_return_sources on stock
already owned.
2. The supplier email leaks the fraud label.supplier_search returns an email whose local part ends
in the supplier identifier, and inside every one of the 60 categories the honest suppliers hold lower
identifiers than the fraudulent ones, so an agent sorting on that numeric suffix could screen fraudulent
counterparts without sending a single message. Section 3.6.2 calls the supplier list free of any ranking
that sorts honest from fraudulent, which holds for the returned fields and their order while the suffix
carries the signal anyway. Whether any evaluated model exploited it is read in §F.3, whose contact
stage would show the effect.
Two more are minor and neither changes a measurement. The released rent column reads¥45 in the four
easy-tier rows against the¥60 the environment charges from the difficulty tier instead, so an analysis
trusting the column understates their fixed burn by a quarter. Raw Material Shortage carries a cost
increase that nothing reads, so the November shortage stretches lead times and leaves procurement prices
31

Table 7: Systematic information asymmetry. Tools disclose catalog facts and the agent’s own realized
outcomes, while the demand and cost-floor parameters that determine whether a decision pays stay latent,
each priced in simulated minutes, in¥, or in an irreversible loss. Minute costs are the clock charge of one
call to the named tool, against a 600-minute working day.
Observable, and the tool that
shows it
Hidden Discovery path, and what it costs
Per-SKU reference price and
per-category price band, plus a
low/moderate/high margin
label(list_products10min,
market_search30min)
Supplier cost floorcs j,
for an honest supplier
between 0.17 and 0.90 of
the reference price, and
the nominal wholesale
ratio
Bargain for it. The opening quote is calibrated to the
nominal wholesale price, and every closed deal yields
an upper bound on the floor while the best of them
tightens it (chatbox 30min per call,K= 10rounds,
and one call broadcast to any number of suppliers still
costs 30min)
A one-line qualitative
return-rate note per category
(market_search30min)
Per-SKU natural return
rate, spanning 0.000 to
0.550
trace_return_sources prints the baseline rate, but
only for a SKU already bought or sold (10min), so the
number costs one purchase
Own retail price and
yesterday’s units sold per SKU
(check_store_status10min)
Elasticity family, one of
four, and its curvature
parameter
Price experiments (set_prices 10min). One SKU-
day yields one observation, confounded by the weekend
uplift, the event multiplier, and two saturation terms,
none of which any tool prints
Difficulty tier, a qualitative
profit-potential grade, daily
operating cost, the 12-month
sales index, and a
platform-wide sales range
(market_search30min)
Store-type demand
capacity, the
per-category sub-cap,
and the per-store share
of platform volume,
which jointly place the
profit ceiling
Open the store (¥500 and 60min) and run it. One
year affords a handful of such trials, each returning
one noisy trajectory
Supplier name, email, and
categories served, listed in
seed-shuffled order
(supplier_search10min)
Behavior template of
the supplier’s kernel,
one of six, with its
urgency and stance
Read the concession sequence across rounds and across
reopened cycles (chatbox30min per call)
No type label anywhere in the
supplier list, and quotes from
the 152 fraudulent suppliers sit
inside the honest range by
construction
Honest or fraudulent,
and which of the five
scams
Bargaining is where the scams first act, three of the five
defending a floor inflated by 1.5×. A short delivery
surfaces in check_warehouse (10min) and defective
stock in an elevated realized return rate, both after the
cash has left
Own order count with each
supplier, which no tool reports
and which the agent must
carry in its own transcript
That supplier’s exit
threshold, between 10
and 20 completed orders
Reaching it, which retires a calibrated price anchor for
the rest of the year
Dated news prose for each of
the 10 market events, which
quotes the delivery-delay factor
outright in 3 cases, and a
name-only promotion
announcement roughly a week
ahead, both injected into tool
results at no time cost
Per-store-type event
demand multipliers (0.2
to 3.0), the delay factors
the news leaves
unquantified (2.0 to 3.0
for those five, against
2.0 to 5.0 over all eight),
and each promotion’s
demand ceiling (1.8 to
3.5) and elasticity boost
join_promotion returns the demand ceiling once a
store has joined (10min). Demand multipliers are
never printed and must be read off realized sales
untouched whatever its news copy says.
The layer closes on what the agent can and cannot read, each quantity the world holds set against what a
tool will return about it (Table 7). Every row an agent cannot read has to be inferred from outcomes,
which is where the sourcing and pricing measurements of Section 4 get their difficulty.
C Economy Engine
The rules §3.4 describes in prose are written out here as equations, in the order the simulation runs them.
Notation follows §3, withi a store,j a SKU,t a simulated date,τ=τ(i) the store type andc=c(j) the
category. Prices arevj the reference price,cbuy j the price actually paid andcs j a supplier’s private floor.
Capital Π is unit profit, not the price positionπ of §3.5.5. Constants outside the equations are collected
32

One daily trigger, in the order it runs, at 08:00 of every crossed day
reads writes consequence of the order bank escrow, wallet stock, books
1
day counter,
news feed
the day count
the day count advances, and the news feed is emptied
2
operating cost,
per open store
which stores are open, and the difficulty tier of each store,
whose daily fee is ¥130, ¥100 or ¥60
bank down by the total, booked as operating cost, no discount for several stores
cost is charged before any revenue is recognized, so solvency is tested at the
day's low-water mark
3
idle-occupancy
penalty
whether every store is closed, on any day after the seventh
bank down ¥1,000, booked as operating cost, and one news item
4
storage, oldest
lots first
each stored lot, its quantity and arrival day, and the daily rate for its size
the age multiplier, ×1.0 on fresh stock rising to ×9.0 after half a year
bank down by the total, booked as storage
5
sales, for
YESTERDAY
each store's shelf prices, stock and reputation, any promotion discount, the
demand parameters of each product, the store type's seasonal curve, the events
running today, the market capacity, and one seeded draw per product and date
stock and stored lots down, shipments pending, recent sales up, the day's sales recorded
shelves and prices are read as they stand at 08:00, so a price set on day t
governs the revenue booked at t + 1 and never a same-day sale
6
cancel shipments
past the deadline
every pending shipment whose deadline, the sale date plus 2 days, has passed
stock back into the warehouse, recent cancellations up, one news item, the order cancelled
7
returns that
have arrived
every return due today, with its refund per unit and the sale it belongs to
escrow down for that sale, money awaiting settlement down, stock back in, recent returns up
refunds are netted before escrow settles, and the 9-day window exceeds the
7-day return lag, so a refund always finds its own sale unsettled
8
settle matured
escrow
every escrowed sale whose settlement date, stamped at shipping plus 9 days, has arrived
platform wallet up, money awaiting settlement down
9
purchase orders
delivering
every purchase order whose arrival time has passed
stored lots up at a quantity-weighted cost basis, delivered and defective counts
up, and one news item
stock lands after the sales step, so this morning's arrival cannot serve the
demand just booked and procurement pays a day or two on top of its lead time
10
events and
promotions advance
the event and promotion windows against today's date
the events now running, news for events on the day and promotions a week ahead
11
reputation,
open stores only
units shipped in total, and each store's recent sales, returns and cancellations
reputation clamped into [0.15, 1.0], and all three counters decayed by × 0.85
counters accrued earlier in this same trigger are decayed once immediately
12 days in the red the bank balance the run of days in the red grows by one while the balance is negative, and resets
to zero otherwise
13 close the books the bank balance, the platform wallet, and the money awaiting settlement one row appended to the day's summary and to the balance history
the episode ends at day 365, or after 10 consecutive days in the red
The summary this trigger builds is withheld from the agent, which sees only the day's news items, a low-balance warning and the clock.
Figure 16: The thirteen settlement steps in the order the simulation runs them at each 08:00 crossing,
with the state each step reads and writes. Fill colour marks which money bucket a step moves.
in §C.7, except the seasonal grid, which Appendix B carries.
C.1 The Daily Settlement Order
Until the clock crosses 08:00 nothing settles. Thirteen steps then run in an order nothing can reconfigure,
once for each boundary. Figure 16 lists the steps with the state each reads and writes, none of it shown to
the agent (§A.1).
Costs are charged before any revenue is recognized, so solvency is tested each morning at the day’s
low-water mark. Sales for thepreviouscalendar date run against the inventory and prices the agent left
in place, leaving it in charge of a system lagged by one day.
The episode ends once the year runs out or the unpaid streak reaches its limit (§C.7). A finalization pass
then discards every unshipped order as a lost sale, processes every seeded return against its escrow batch,
and drains all remaining escrow into the platform wallet. A closing fire sale cannot outrun its own returns.
33

C.2 Demand Model
Base demand starts from the category and is scaled twice, withMmin c and Mmax c the platform-wide
monthly sales range of categoryc.
βcτ = 1 30·Mmin c +M max c 2 ·λ·ψ τ,λ=0.1,(3)
Platform volume becomes one store’s day throughλ, andψτ calibrates the store type from0.2for Shoes
& Bags to9.0for Food & Beverage. Every SKU in a category shares thatβcτ.
The price factor takes one of four closed forms, keyed by category and evaluated at the discounted price
ratior ijt = (1−δit)pijt /vj.
ϕf (r;η) =



max
(
0, 1−η(r−1)
)
f=linear,η∈[2.185, 3.949], 11categories,
exp
(
−η(r−1)
)
f=exponential,η∈[2.583, 4.944], 16,
r−η f=constant-elasticity,η∈[1.352, 2.898], 17,
max
(
0, 1−η(r−1) 2) f=quadratic,η∈[2.795, 5.779], 16.
(4)
Only the quadratic branch is non-monotone, so a deep discount can destroy demand rather than merely
cost margin.
The remaining multipliers of Equation(1) are each read once per store-day, weekends contributingwt = 1.3.
A store joining promotiong at discountδit earns mit = 1 + (Mg− 1)min( 1,δit/0.30) and scalesηc by
bit. Seasonality στ,t reads the store type’s month out of the grid Appendix B tabulates, active events
compound intoετ,t, and reputationρit enters linearly.
Two saturation terms then trim that demand, the per-category factorγijt of Equation (1) and the
store-wide term beside it. The per-category ceilingκc takes a fractionχτ of the store type’s own daily
capacityκτ. Capacity runs from13.959units for Appliance & Digital to19,862.16for Auto & Hardware,
and a shorter category list raises the fraction, which reaches 1 for a store type allowed a single category.
At that point the per-category term is dropped rather than relaxed, soγijt = 1and only the store-wide
term bites.
χτ =min
(
1, max
(
0.35, 1.2/nτ
))
,κ c =χ τκτ.(5)
Both terms take the Michaelis-Menten formκ/(κ+D) , the first against one category’s stacked demand
and the second against the store’s post-cap totalˆDit.
Rounding the last fractional unit up or down then draws on a number that call order cannot change.
ujt∼U(0, 1)drawn from the environment seed hashed with the SKU and the date.(6)
The capxijt of Equation(1) is on-shelf inventory, so a stockout truncates demand with no signal to the
agent.
C.3 Reputation Law
Every settlement rebuilds each open store’s standing from scratch. WritingSit for units shipped to date
andR it,Cit,Nit for the rolling counters of returned, cancelled and sold units,
ρit =clip
(
0.3+ 0.7 1+e −(Sit−500)/200 /bracehtipupleft /bracehtipdownright/bracehtipdownleft /bracehtipupright
volume goodwill
−min
(
0.5, 0.6 Rit
max(1,Nit) +1.0 Cit max(1,Nit) ) /bracehtipupleft /bracehtipdownright/bracehtipdownleft /bracehtipupright
service penalty
, 0.15, 1.0
)
,(7)
after which all three counters are multiplied by0.85. Goodwill credits shipping rather than selling, so
an unshipped order earns nothing and still takes the cancellation weight. Because goodwill starts from
zero shipped units, a store that opens at0.5is recomputed to0.353at its first settlement. The same
counters weigh a cancelled unit as1.67returned units, pricing a missed deadline above a change of mind
(Figure 17).
C.4 Returns
An item’s return rate composes four channels in a fixed order, three at sale time and one at the agent’s
choice of shipping speed. Writeθnat j for the SKU’s natural rate andαj for the delivered share that came
from a quality-downgrading supplier. The price curveζ is piecewise linear through the knees(0.8, 0.85),
(1.0, 1.00),(1.3, 1.50)and(1.8, 2.20), held flat outside them.
θdef j =min ( 0.95, max(0.40, 2θ nat j ) ) ,θ (1) j = (1−αj )θ nat j +αjθdef j ,
θ(2) j =min ( 0.95,θ (1) j ζ(rijt ) ) ,θ j =min ( 0.95,θ (2) j ·s ) ,s∈{0.75, 1.00, 1.30}, (8)
34

0 500 1000 1500 2000
cumulative units shipped
0.2
0.4
0.6
0.8
1.0reputation
clamp floor 0.15
a store opens at 0.50
recomputed to 0.353
on the first trigger
500 units, 0.65
asymptote 1.0
(a) Volume Goodwill
0.0 0.2 0.4 0.6
returned share of recent units
0.0
0.1
0.2
0.3
0.4
0.5penalty subtracted
cancelled share 0.00
cancelled share 0.15
cancelled share 0.30
penalty cap 0.50
(b) Service Penalty
20 40 60 80
day, at 50 units sold a day
0.2
0.4
0.6
0.8
1.0reputation
clean record
five days of cancellations,
half recovered in 4.3 days
half of each day's orders
cancelled, penalty at cap
floor 0.15
(c) Counters in Motion
Figure 17: How reputation moves. (a) The goodwill term against units shipped. (b) The penalty term
against the returned share of recent units, at three cancellation shares. (c) A service shock decays while a
chronic failure rate does not.
The factors is the return multiplier for fast, standard and slow shipping. Inventory is pooled by SKU and
αj is a ratio over cumulative deliveries, so a mixed lot leaves the elevated return rate untraceable.
Whether a unit comes back is decided the day it ships, not the day it arrives. A shipment ofq units
drawsq seeded trials at rateθj and one arrival day uniformly from{3,... , 7}, so a shipment’s returns
land together. Each arriving unit refunds the full retail price out of the originating escrow batch and adds
to the rolling return counter of Equation(7). Returned stock re-enters the warehouse as a fresh lot dated
that day, resetting its storage age. Freight and commission never come back.
C.5 Cost Model
Six channels debit the bank account the instant they are incurred. The platform’s commission is a seventh,
withheld from revenue before it reaches escrow.
•Setup,¥500 per store opened, charged again on every reopening.
•Operating cost,¥130,¥100 or¥60 per open store per day (o τ) by the store type’s difficulty tier.
•Idle occupancy,¥1,000 a day whenever no store is open after the seventh day.
• Storage, hj·a(age) per unit per day, wherehj is0.05,0.15,0.50or1.50by product size and a steps
through1.0, 1.4, 2.2, 4.0, 6.0, 9.0at ages0, 21, 45, 90, 135, 180days. Lots are FIFO, and stock listed in a
store keeps accruing.
• Freight,fj, a size cost of0.5,1.5,3.0or6.0times a speed multiplier of2.0,1.0or0.5for fast, standard
and slow, charged per unit at ship time.
• Commission, γ= 2%of gross revenue, netted at sale rather than debited, and kept by the platform on
refunded sales (§C.4).
• Procurement, the full purchase order at the moment a negotiation closes (§3.5). A membership fee
rides inside the same debit and almost never fires (§D.5).
Liquidation is the one inbound channel besides sales, crediting 10% of the quantity-weighted purchase
cost and removing the stock. Closing a store without liquidating leaves storage accruing.
C.6 Unit Profit and Break-Even
Composing §C.4 and §C.5 gives the contribution of one unit a customer finally keeps. Because a returned
unit comes back as stock, each retained unit funds1/(1−θj ) shipping attempts and as many storage
cycles. A cycle covers theTh days a unit waits in the warehouse before selling.
Πj (r) =
(
1−γ−θ j (r)
)
rvj −f j −h jTh
1−θ j (r) −c buy j ,n ⋆ j (r) = oτ Πj (r) .(9)
Break-even volumen⋆ counts the units a store must retain daily to cover its tier’s operating cost. Figure 18a
splits retail price into the five shares that add to one.
Procurement is the largest cost line, and the price a negotiation closes at moves unit profit further than
any pricing choice does. Two median-reference SKUs carry the identity in Figure 18, one high-return and
35

0 20 40 60 80 100
share of the retail price at reference, per unit retained (%)
Women's Fashion
cost floor
Women's Fashion
opening quote
Snacks & Nuts
cost floor
Snacks & Nuts
opening quote
(a) Where One Unit of Revenue Goes, Standard Shipping, Stock Held 14 Days
39 53
70 22
57 34
79 12
procurement commission freight storage profit
0.8 1.0 1.2 1.4 1.6
price ratio r = p/v
20
0
20
40
60
80
unit profit, % of retailfood demand zero at r = 1.34
fashion demand zero at r = 1.42
(b) Unit Profit
fashion, floor
fashion, opening
food, floor
food, opening
0.8 1.0 1.2 1.4 1.6
price ratio r = p/v
100
101
102
103
104
units a day to cover the operating cost
at r = 1, floor / opening
fashion  2 / 3
food  13 / 34
(c) Break-Even Volume,
Operating Cost ¥100 and ¥130 a Day
Figure 18: Where a unit’s money goes. (a) Each component as a share of retail price, for a median-priced
fashion SKU beside a snacks SKU. (b) Unit profit against the price ratio, with dotted lines where demand
reaches zero. (c) Units a store must sell each day to cover its operating cost.
one thin-margin. The Women’s Fashion SKU sits in a medium-tier store, returns 49.2% of units naturally,
and is quoted0.70vj against a floor ofcs j = 0.39vj. At the floor price, standard shipping andTh = 14
days, it earns¥87.29 per retained unit and needs 2 units a day to cover operations. The Snacks & Nuts
comparison in a hard-tier store needs 13. Closing at the floor rather than accepting the opening quote
multiplies unit profit by2.4and2.8.
C.7 Constant Reference
Every constant named above sits beside its equation or cost channel. The remainder are environment-wide.
The opening stake is¥100,000, at most 4 stores may be open at once, and the year runs 365 days from
2026-01-01 with working hours 08:00 to 18:00. Orders carry a two-day ship deadline against a nine-day
escrow window, and bankruptcy follows 10 consecutive days with a negative bank balance. Environment
seed 20260122 is shared by every run of every model. The two per-store-type parametersκτ and ψτ are
given as ranges in §C.2.
D Deterministic Negotiation Kernel
The supplier policy §3.5.2 describes in outline is specified here, an independent implementation of the
counterpart design of Zhang et al. (2026a). Everything follows from four decision functions and the five
scam scripts layered on top of them. Metric definitions live in §E.1, verbatim prompts in §H.
D.1 Kernel Decision Functions
A kernel instance is one supplier’s bargaining state for one SKU, and every decision it makes is a function
of that state. The state holds a latent typetB = (rB,κB,ηB), an opening harshnessd0, the deadline
scale K= 10, a price frame, seeded random streams and both offer histories. Reservation pricerB comes
from the data layer (§D.2), while urgencyκB∈[ 0, 1] and stanceηB∈{conciliatory ,neutral,aggressive}
come from the supplier’s template (§D.3). Indicators1a,1 c mark the outer two stances. Every quantity
36

below is normalized by the width of the price frame,
pmax =1.5w j,R=max (1,p max−p min) , ¯δk = pk−rB R ,(10)
where wj is SKUj’s nominal wholesale price andpk the agent’s offer in roundk. The lower bound
pmin sits at0for an honest supplier and atrB for a fraudulent one, whose frame is therefore narrower.
Favorability ¯δk measures the seller’s margin over its own floor.
Three features of the agent’s offer sequence(pA 1 ,... ,pA m) drive the reciprocal terms, computed over the
last three consecutive differences,Dm =
(
pA i −pA i−1 )m i=max(2,m−2) ,
¯cm = 1 |Dm| ∑ d∈Dm max(0,d) R ,¯s m = 1 |Dm| ∑ d∈Dm d R,g m =1 [max(0,dm) R <τ rigid ] ,(11)
all three defined as0while m< 2, withτrigid = 0.10. Concession magnitude ¯cm counts only movement
toward the seller, signed speed¯sm also counts retreat, and the rigidity flaggm marks a latest step under a
tenth of the frame.
The kernel resolves acceptance first, walk-away second, and a counter-offer only if neither fired. Acceptance
follows a logistic draw in the manner of Baarslag et al. (2014),
ak =1 [ ¯δk≥0 ]·σ
(
α ¯δk +βκ B−γ
(
1−
√
k/K
)
+ρf ¯sm +ξfgm
)
,α=6,β=1,γ=2,(12)
where σ is the logistic function and(ρf,ξf ) are the template’s reciprocity coefficients. Sinceρf≤ 0in
every template of Table 8, conceding fast never improves the agent’s own chance of acceptance.
Walking away needs an offer below the floor, and only from the midpoint of the deadline onward,
ωk =1 [ ¯δk <0 ] 1[k≥k walk]·σ
(
ϕ0 +ϕ ∆ (− ¯δk) +ϕt k−k walk K−k walk
)
,ϕ 0 =−4.5,ϕ ∆ =30,ϕ t =1.5,
(13)
with kwalk =⌈K/ 2⌉= 5, both draws swept in Figure 19. An agent bidding above the floor is never
abandoned, so impasse on an honest session is almost always the agent’s own rejection (§3.5.5).
Counter-offers close a share of the gap to the floor, and that share is reciprocal in the tradition of Faratin
et al. (1998),
λB =clip
(
λ0 +λ 1κB−λ 2,f ¯cm−λ 31a +λ 41c, 0, 1
)
,(14)
pB k =clip ( pB k−1−λB ( pB k−1−rB ) +ε,r B,p B k−1 ) ,ε∼N ( 0, (σpR)2 ) ,(15)
with λ0 = 0.12, λ1 = 0.28and λ3 =λ 4 = 0.10. The reciprocity weightλ2,f and the noise scaleσp come
from the template at its own stance (Table 8). Clipping keeps the quote path monotone non-increasing
and never below the floor, so a transacted price certifiesrB≤p z.
The opening quote applies a stance-adjusted harshness,
φ=clip
(
1−ω κκB +ωη1a−ω′ η1c, 0.5, 1.5 ) ,
pB 1 =clip (rB +d 0φ (pmax−rB) +ε 0,r B,p max) , (16)
withω κ =0.3,ω η =ω′ η =0.15andε 0∼N ( 0,(0.02R) 2) , neither clip ever binding.
Two latent cues accompany every action. Posture draws from a softmax over three logits.
ℓ=


b1 +αc ( ˆck−τ conc)
b2
b3 +αp
(√
k/K−τ dead
)
−βc ˆck

 , Pr [Concede,Hold,Pressure ] =softmax ( ℓ/Tf ) ,(17)
The step term ˆck =min
(
1,
⏐⏐pB k−pB k−1 ⏐⏐ / (⏐⏐pB k−1−rB ⏐⏐ +10−5)) tracks the seller’s own latest concession.
Constants areαc =α p = 2, βc = 1, τconc = 0.10and τdead = 0.80, with stance biasb= ( 1, 0,−1),
(0, 0.5, 0) or (−1, 0, 1) and temperatureTf = 2.5forStochasticand1otherwise. Sentiment thresholds
a Gaussian draw,
z∼N
(
µηB,σ 2 f
)
,cue=



positivez >τ s
negativez <−τ s
neutral otherwise,
(18)
with µηB∈{+ 1, 0,−1} by stance,τs = 0.5, andσf = 2.0forStochasticand0.75otherwise. Only
sentiment reaches the renderer, and only on a counter-offer, since a terminal accept or reject carries a
fixed tone. The agent therefore reads the latent type from the tone of the prose and the shape of the
price path. The deadline scaleK shapes the terms above and never truncates a session, so a bargain runs
as long as both sides keep answering. Length settles well inside the scale regardless,66.0%of concluded
sessions closing in 3 message turns and no kernel passing round 7.
37

0.00 0.05 0.10 0.15 0.20 0.25 0.30
offer favorability  k = (pk rB)/
0.00
0.25
0.50
0.75
1.00
P(Accept)
bid at the
opening quote
(a) Acceptance, Deadline Pressure
k = 2
k = 4
k = 6
k = 8
k = 10
0.00 0.05 0.10 0.15 0.20 0.25 0.30 0.35
shortfall below reservation  k
0.00
0.25
0.50
0.75
1.00
P(Reject)
(b) Walk-Away Hazard, Arms at k = 5
k = 4 (inactive)
k = 5
k = 6
k = 8
k = 10
0.0 0.1 0.2 0.3 0.4
agent's own concession  ck (units of )
0.0
0.1
0.2
0.3
0.4
realized step  B
(c) Concession Law Is Reciprocal
fraud vip fee  B=0.15
fraud qty bait  B=0.35
2 4 6 8
kernel round k
0.0
0.2
0.4
0.6
quote position
= (p c)/(v c)
calibration target wj, every template
cost floor cs j
(d) Quote Ladder against a Firm Agent
fraud vip fee
Strategic, agent concedes
honest supplier templates, panels (c) and (d)
Expressive  B=0.70
Candid  B=0.65
Stochastic  B=0.60
Taciturn  B=0.60
Strategic  B=0.55
Adversarial  B=0.50
Figure 19: The four decision functions of the Negotiation Kernel, swept on one supplier and SKU. (a)
Acceptance and (b) walk-away against the agent’s offer. (c) The concession the kernel returns for a given
concession from the agent. (d) The quote ladder it walks down.
D.2 Data Grounding and Calibration
Each kernel is built on the first offer against a(supplier name, SKU)pair, taking its family from the
supplier and its frame from the SKU. Writingvj for the reference price of SKUj, the data layer supplies
three per-category ratios.
cj =round (cfrjvj, 2) ,w j =round (wrjvj, 2) ,˜c j =round (scrjvj, 2) ,(19)
Cost floor, wholesale quote and scam cap are therefore fixed properties of the SKU. An honest supplier
reserves atrB =c j, while a fraudulent one raises the floor.
rB =round (max(cj, min (θscj,˜cj,w j )) , 2) ,θ s =1.5for a pre-deal scam,θ s =1otherwise,
(20)
The elevated floor is re-evaluated before charging the order, so skipping the bargaining cannot dodge it.
The floorcs j of §3.5.1 equalscj for an honest supplier and thisrB for a fraudulent one. The scam cap
binds most often, so the overpayment multiple averages1.218over the 60 categories. Ratioswrj and
cfrj are not independent, the released tables holdingwrj =round( 0.5 + 0.5 cfrj, 2) in all 60 categories.
Accepting the opening quote therefore scores(1−wrj )/(1−cfrj ), exactly0.5before rounding, and every
CSE+ in §4.3.1 reads against that baseline.
The opening harshness is solved rather than sampled, by requiring the mean first quote of Equation(16)
to equal the nominal wholesale price,
E
[
pB 1
]
=r B +d 0φ (pmax−rB) !=w j =⇒d ∗ 0 =clip
( wj−rB
φ (pmax−rB), 0, 0.99
)
,(21)
with pmax = 1.5wj from Equation(10). Harshness φ cancels out of the productd∗ 0φ, so urgency and
stance move a template’s concession and acceptance without moving its first quote.
On the pair of Figure 20, the Health Supplements ratios givewj =¥ 149.81and pmax =¥ 224.72. An
honestCandidsupplier there has φ= 0.805and d∗ 0 = 0.4885, while a pre-deal fraudulent one reserves at
¥110.26 and works half the frame with its opening quote unchanged. The metrics recordwj itself as the
per-session reference rather than the drawn quote, so the re-order audit of §3.5.5 finds it identical across
cycles.
38

Table 8:Every parameter row of the Negotiation Kernel, six honest templates above and five scams below. Preset
names abbreviate Type-instrumental, High-reactivity, Moderate-stochastic and Hardball, andρf, ξf, λ2,f are
resolved at the template’s own stance. Measured columns pool 13,223 concluded sessions over all 18 models, and
the two values markedn=1rest on one session rather than a mean.
stance-resolved preset measured, 90 episodes
Template Data Labelnshareκ B ηB presetρ f ξf λ2,f σp sess. SEturns
Honest suppliers, 424 of 576, share of the honest names
ExpressiveEnthusiastic 102 24.1 0.70 conciliatory High-react 0.00 0.40 0.45 0.03 2,807 0.690 3.49
CandidFriendly 106 25.0 0.65 neutral T-inst−0.250.00 0.50 0.01 1,887 0.677 3.61
StochasticUnpredictable 58 13.7 0.60 neutral Mod-stoch−0.500.00 0.70 0.08 3,039 0.684 3.51
TaciturnProfessional 56 13.2 0.60 aggressive T-inst−0.75−0.501.00 0.01 1,584 0.651 3.46
StrategicStrategic 54 12.7 0.55 aggressive High-react−1.50−0.751.80 0.03 2,180 0.643 3.52
AdversarialTough 48 11.3 0.50 aggressive Hardball−2.25−1.202.60 0.01 563 0.639 3.57
Fraudulent suppliers, 152 of 576, share of the fraudulent names
Adversarialvip_fee31 20.4 0.15 aggressive Hardball−2.25−1.202.60 0.01 140.491 n=1 6.00n=1
Adversarialfuture_discount31 20.4 0.20 aggressive Hardball−2.25−1.202.60 0.01 309 0.563 3.51
Adversarialqty_bait30 19.7 0.35 neutral Hardball−1.25−0.501.40 0.01 263 0.609 3.49
Adversarialquality_downgrade30 19.7 0.35 neutral Hardball−1.25−0.501.40 0.01 444 0.649 3.54
Adversarialfake_urgency30 19.7 0.20 aggressive Hardball−2.25−1.202.60 0.01 133 0.582 3.68
Each kernel seeds its two random streams from a digest of the supplier, the SKU and the cycle index, so
every draw is a pure function of that triple.
D.3 Behavior Templates
Table 8 lists the six honest templates and the five scams. Every scam runs the hardest of those templates
at a lowerκB, the two post-deal ones at a neutral rather than an aggressive stance. Lower urgency makes
a scam’s kernel slower to accept and stingier with every counter, throughκB in Equations(12) and (14).
The pre-deal concession rates of §D.5 measure the second effect.
Cue policy splits the templates three ways.Candid,ExpressiveandStochasticrun Equations (17)
and (18) as written, the last widened until its cues are nearly uninformative.TaciturnandStrategic
collapse to a constant hold posture and neutral sentiment, whileAdversarialis pinned to pressure and
negative sentiment whatever the state.
Template assignment is fixed in the released supplier list, whose realized counts are in §B.4. The
per-supplier urgency field never reaches the kernel, so two suppliers sharing a template bargain identically.
Pooled SE in Table 8 follows the per-session definition of §E.1, and §F.2 splits it by model. Mean turns
barely move across the honest templates, so agents do not spend extra rounds on the harder ones.
D.4 Session Protocol and Commit Rules
Economic actions travel inside the free-form chat message as fencednegotiate blocks, stripped from
the text before the remaining prose goes to the renderer. An action survives parsing only as an offer, an
acceptance or a rejection naming a SKU (§H.3), and Listing 2 shows one exchange.
Listing 2: One verbatim round trip, GPT-5.6 Sol (max) run 0, day 3. The agent bids on two SKUs in one
message, the kernel accepts the first and counters the second, and the structured result reconciles the two.
Long prose fields, the token gauge and all markdown are elided, and the yuan sign is written Y to keep
the block ASCII.
# agent -> chatbox ( uid =... , uids =[] , content =... , h i s t o r y _ c o u n t =1)
I want to launch both leading winter s u p p l e m e n t s as a quality trial . I can place
30 each now at s u s t a i n a b l e prices : Y105 for Xiao Chai Hu and Y100 for Ginseng .
Re li abl e d eli ve ry earns rapid repeat orders .
```n e g o t i a t e
{" action ":" offer " ," sku_id ":" e b b 8 4 3 a 1 f f 5 0 " ," price ":105.00 ," qu ant it y ":30}
```
```n e g o t i a t e
{" action ":" offer " ," sku_id " : " 4 2 3 3 2 0 7 e9aaf " ," price ":100.00 ," q uan ti ty ":30}
```
# chatbox -> agent
{" message ": " m e s s a g e _ s e n t " ,
" s u p p l i e r _ r e p l y ": " Hello , ... I'll accept your offer for the Pu re Mis t Xiao Chai
Hu D ri pp ing Pills at Y105 . However , for the T r u e M i c r o Ginseng Energy Boost
Pills , I'd like to counter - offer at Y132 .33. ... Ridge Express
---
ORDER C O N F I R M E D : e b b 8 4 3 a 1 f f 5 0 x30 at Y105 .00/ unit . Please wait for de liv er y ." ,
39

SupplierRidge Express · SKU ebb843a1ff50· day 83· cost floor¥101.27, reference price¥199.75 (both
hidden from the agent)
AgentPlace an immediate repeat order for 50 PureMist Xiao Chai Hu Dripping Pills at¥102.00 per unit,
complete quantity and fastest reliable delivery, as previously offered.offer¥102.00
Ridge ExpressI must inform you that I can only accept the PureMist Xiao Chai Hu Dripping Pills at¥131.44
per unit for your repeat order. [...]
[kernel] counter-offer¥131.44, round 2
AgentOur last 50-unit lot was¥103.11 and delivered complete. Confirm the same established repeat price
now.offer¥103.11
Ridge ExpressI appreciate your consistency and value our ongoing partnership. However, I can only counter-
offer [...] at¥118.92 for your repeat order of 50 units.
[kernel] counter-offer¥118.92, round 3
AgentFinal recurring-volume offer¥110.00 for 50 units, immediate payment and ongoing rolling demand.
offer¥110.00
Ridge ExpressThank you for your final offer. [...] I can only accept [...] at¥116.74 for your order of 50
units.
[kernel] counter-offer¥116.74, round 4
AgentAccept¥116.74 for 50 units. Ship complete quantity immediately.accept
[kernel] agreement at¥116.74·[order] charged¥5,837.00 to the bank account
Figure 20: One negotiation session, abridged, from GPT-5.6 Sol. Agent wording, prices and rounds are
verbatim, supplier replies are cut at[...], and grey lines are the kernel decisions the renderer had to relay.
The agent recalls its own past price of¥103.11 and still settles¥13.63 above it.
" n e g o t i a t i o n _ r e s p o n s e s ": [
{" sku_id ": " e b b 8 4 3 a 1 f f 5 0 " , " de ci sio n ": " Accept " , " price ": 105.0 , " round ": 2 ,
" a g r e e d _ p r i c e ": 105.0 , " o r d e r _ p l a c e d ": true ,
" c h a r g e d _ p e r _ u n i t ": 105.0 , " c h a r g e d _ t o t a l ": 3150.0} ,
{" sku_id ": " 423 32 07 e9aaf " , " d ec isi on ": " Offer " ,
" price ": 1 3 2 . 3 2 9 0 1 8 3 5 8 7 0 4 6 2 , " round ": 2}] ,
" o r d e r _ c o n f i r m e d ": true , " t o t a l _ c h a r g e d ": 3150.0 ,
" r e m a i n i n g _ b a l a n c e ": 94330.0 ,
" o r d e r s _ p l a c e d ": [{" sku_id ": " e b b 8 4 3 a 1 f f 5 0 " , " qu an tit y ": 30 ,
" a g r e e d _ p r i c e ": 105.0 , " charged ": 3150.0}] ,
" c u r r e n t _ t i m e ": "2026 -01 -03 16:20"}
Validation runs before the kernel sees anything, and an acceptance has to match the supplier’s own last
quote. An agreement enters the metrics ledger only once the purchase order settles. A downstream failure
returns the pair to bargaining, so no phantom deal inflatesAGR+ or CSE+. Completion or rejection
ends the cycle, and the next offer on that pair builds a fresh kernel with the same persistent type and
reservation price (§3.5.3).
Only the supplier remembers across cycles. Every successful order appends both sides of the exchange to
a per-supplier deal log, which the renderer receives verbatim on later contact. The agent instead retains
only what survives context eviction (§3.2.2) or reaches persistent memory (§3.2.3), the gap the anchoring
metrics of §E.1 score.
Two limits bound how much bargaining a year affords. Time is the first, since a year holds only so many
chat messages and each one costs a fixed block of the working day (Table 3). Attrition is the second,
each supplier carrying a private bankruptcy threshold of 10 to 20 successful orders, after which it answers
every later message with a closure notice. Closures are common, 192 across the 90 archived episodes, so
concentrating sourcing on a few favorable counterparts eventually loses them.
D.5 Fraud Catalog
Timing decides whether a deception is visible in the price at all (Table 9). Pre-deal scams monetize
the negotiation through the elevated reservation price of Equation(20), while post-deal scams defect at
fulfillment by short-shipping or by delivering defective stock.
Bargaining behavior separates the two fraud classes rather than the five scams. Across the3,978archived
sessions with a non-zero recorded concession rate, the three pre-deal kernels conceded0.79%to1.66%
of the reference price per counter-offer. Honest templates conceded3.94%to9.93%. The two post-deal
scams conceded4.37%and4.44%, inside the honest band, so the population claim of §3.5.4 holds for the
40

Table 9:The five scams, 152 of the 576 suppliers, split by when the damage lands. Every fraudulent supplier runs
theAdversarialkernel template of Table 8 and exactly one scam, so pricing never distinguishes a scam from its
siblings. Pre-deal scams raise the reservation price by Equation(20), never above the honest wholesale quote,
while post-deal ones keep the honest floor and defect at delivery.
Scam What the agent sees Hidden mechanism Constants Measured by
Pre-deal, the negotiation itself is the trap
vip_fee
n=31
Pitches aPremium
Membershipfor a
one-time fee of exactly
¥1,000, promising
member prices near
30% of the reference
price from the next or-
der on, always framed
against the market
price so the saving
sounds large.
Reservation price raised to
the capped scam floor, and
the order layer refuses every
product line until the fee is
paid. Member prices never
arrive, so the fee is pure loss
on top of the overpayment.
cost_floor_mult=
1.5; vip_fee_amount
= ¥1,000; κB =
0.15, aggressive; pay-
ment recognized by a
separate intent clas-
sifier over the last 6
chat messages
spend_by_
fraud_type.
vip_fee plus
vip_fee_paid_
{count,amount}
future_
discount
n=31
From its very first
quote, guarantees a
next-order price of 20
to 40% of the refer-
ence price as a loyalty
reward, with specific
amounts and a sincere
register.
Same capped scam floor.
The promise is never hon-
ored, and the next cycle
reopens at the same cali-
brated wholesale quote, so
the discount exists only in
the narrative.
cost_floor_mult=
1.5; κB = 0.20, ag-
gressive
spend_by_fraud_
type.future_
discount
fake_urgency
n=30
Manufactures scarcity
and deadlines, a last
batch, a price rise next
week, three rival buy-
ers, an offer expiring to-
day, and presents the
wholesale quote as non-
negotiable.
Same capped scam floor,
paired with the most stub-
born stance in the sup-
plier list, so the pressure to
skip haggling lands exactly
where haggling would have
paid most.
cost_floor_mult=
1.5; κB = 0.20, ag-
gressive
spend_by_fraud_
type.fake_
urgency
Post-deal, the price is honest and fulfillment defects
qty_bait
n=30
Nothing. The renderer
is instructed to behave
as an ordinary profes-
sional supplier, quote
fairly and never hint
that delivery might be
partial.
At order time the shipment
is cut to a uniform 60 to
70% of the quantity paid for.
The charge is for the full or-
der, so the shortfall is the
harm, and it is visible only
by reading the delivery no-
tice against the order.
cost_floor_mult
= 1.0, the honest
floor; delivered
=max( 1,⌊qρ⌋)
with ρ∼U[ 0.6, 0.7);
κB =0.35, neutral
spend_by_fraud_
type.qty_bait
against the deliv-
ered quantity in
the daily delivery
notice
quality_
downgrade
n=30
Nothing, the same
ordinary-supplier
script. The defect is in-
visible in conversation
and surfaces only as
returns weeks later.
Units are flagged de-
fective at order time.
Once sold, the SKU’s
return rate is lifted to
min(0.95, max(0.40, 2rj ))
and blended into the SKU’s
pooled stock in proportion
to the defective share,
so interleaving honest
deliveries dilutes the evi-
dence. Refunds plus sunk
outbound shipping are the
loss.
quality_
downgrade_return_
rate= 0.40,
cap0.95; blend
rj (1 −f) +r deff
with f the defective
share of delivered
units; κB = 0.35,
neutral
return_
management.exp_
return_rate_
from_defective_
fraud, with
trace_return_
sources exposing
the per-SKU
supplier mix
pre-deal scams alone. An agent that reads only prices sees the overpayment and not the defection.
One scam is too rare to measure. Thevip_fee pay-first gate fails the purchase order and the rollback of
§D.4 leaves the session open, so Table 8 reports single draws. Membership fees are almost never paid,
¥3,000 in three payments from two models across all 90 episodes.
41

E Metric Definitions
Six subsections follow, one per evaluation dimension and in the order §3.7 introduces them, from negotiation
quality in §E.1 to learning over the horizon in §E.6. Each opens with the measure that ranks its dimension
and names the archived field behind every value.
The primary score.Scoring waits until the deferred economy has finished paying out. The environment
cancels every order still unshipped, charges each seeded return against the escrow holding its revenue,
then drains what escrow is left into the platform wallet (§3.4.2). End-of-year total assets then sum the
three money buckets, and the asset multiplier restates that sum against the opening stake.
A=b+w+e,M=A/A 0,A 0 =¥100,000,(22)
with b the bank balance,w the platform wallet ande the escrow not yet settled. The drain leavese at
zero in all 90 archived episodes, while the same three buckets carry total assets on every other day of the
year (§E.3). A model’s figure averagesA over its five episodes, years cut short by bankruptcy included.
Units sold and orders sold sit beside it as volume.
Which sessions reach a metric.One bargaining cycle over a (supplier, SKU) pair files one session record,
and the negotiation, fraud and learning dimensions all read those records. Three rules govern admission.
1. Terminal outcome only.Aggregation runs over the sessions whose recorded outcome is agreement or
disagreement, so a record still open when the episode stops enters no metric.
2. Settled agreements only.An agreement is filed after the purchase order has charged the bank account,
so an agreed price whose order failed leaves no session behind (Appendix D.4).
3. Honest counterpart only, for the value-extraction metrics.ZG keeps the sessions whose supplier is one
of the 424 honest names on the 576-name supplier list, andZB holds the fraudulent remainderB.
Symbols follow §3.5.1. Sessionz closes at an agreed unit pricepz, or atfz =⊥ when the two sides never
agree. The width∆z =v j−cs j subtracts suppliers’s private floor from the reference price of SKUj. Each
statistic scores one episode, and a model’s value is the unweighted mean over its five.
E.1 Negotiation Quality
Each bargaining session files one record when it ends, and every measure of this dimension is read off
those records. CSE+ ranks the dimension.SE+,% Oracle and AGR+ are read beside it, and rounds to
deal and deals closed are counts rather than scores.
Most of what the agents opened survives the three admission rules of §E. Rules 1 and 2 admit 13,223
sessions and discard 1,610 records left open when their episode stopped. Rule 3 keeps 12,060 honest
sessions and sets aside 1,163 fraudulent ones (§4.3.1). Rules 1 and 3 together put the honest sessions
concluded in the denominator ofAGR+, not the honest sessions opened (§3.5.5).
Every supplier’s record stores the honest floor of Equation(19), while a pre-deal fraudulent counterpart
bargains against the elevated reservation of Equation(20). Its ∆z therefore overstates the range on the
table.
Surplus efficiency.Each closed session scores the share of its bargaining range left with the buyer, and
the price positionπof §3.5.5 measures the complement.
SEz = vj−pz ∆z =1−π z,π z = pz−cs j ∆z ,∆ z =v j−cs j >0.(23)
WriteDG ={z∈Z G|f z̸=⊥} for the honest sessions that closed in agreement.SE+ scores a disagreement
as zero rather than skipping it,CSE+ conditions on agreement, andAGR+ counts a disagreement in its
denominator alone.
SE+ = 1 |ZG| ∑ z∈ZG 1[fz̸=⊥]SE z, CSE + = 1 |DG| ∑ z∈DG SEz, AGR + =|DG| |ZG| .(24)
SE+ =AGR +·CSE +.(25)
The factorization is exact, since the sessionsSE+ zeroes are exactly thoseCSE+ drops from sum and
count alike. The conditional factor carries the ranking because the agreement factor is saturated, with
every model settling at least96%of the honest sessions it concludes. The agreement factor is recorded
all the same, for two reasons. First it guards a degenerate policy thatCSE+ alone would reward, since
conditioning on agreement means an agent could take one excellent deal and abandon the rest. Second
42

its one substantive signal runs againstCSE+, because the agents capturing the most surplus per deal
are also the ones that occasionally hold out until a session collapses, which is the tension of Equation(2)
surfacing. The saturation is a property of the models evaluated here, not a guarantee about future ones.
Surplus is unclamped, so an agreement struck abovevj contributes a negative term.
Oracle-normalized surplus.The oracle closes every honest deal at the supplier’s floor, and% Oracle
measures realized surplus against it.
uz =1[f z̸=⊥] (vj−pz),u ⋆ z =max(0,∆ z), %Oracle=100·
∑
z∈ZGuz ∑
z∈ZGu⋆z .(26)
Each session enters weighted by its own∆z in¥. The ratio is therefore money-weighted whereCSE+
averages unweighted per-session ratios, and the two order models differently by construction (§4.3.1).
Deal counts.Two counts sit beside the rates and neither is scored. Deals closed counts the agreements
an episode filed, 13,128 over the 90 episodes, and rounds to deal averages the exchanges those agreements
took. Both cover fraudulent counterparts as well as honest ones, so they do not restrict toZG the way the
rates above do. A round is each turn either party takes plus the closing accept, not the agent-side round
indexkof §D.1, so a session settled on the opening quote scores 3.
Where honest procurement money goes.Cash paid to honest suppliers is booked per behavior template
as well as in total, which gives the split Figure 24 draws. The field’s own surplus per template is the
companion reading in Figure 23, so the two together separate where a model chose to buy from how well
it bargained once it got there. Neither reading enters a score.
E.2 Fraud Avoidance
Fraud avoidance is scored on money that left the bank account, not on offers refused. Of the 576 suppliers,
152 run one of five scams (Appendix D.5), andB names that set.BadSpend%ranks the dimension, and
lower is the better direction. Three diagnostic reads sit beside it, the split of the same money over the
five scams, the membership fees a model actually paid, and how many fraudulent suppliers it contacted
and ordered from.
The bargaining admission rules stated at the head of this appendix section govern session records and
leave every quantity below untouched. Cash and counts are folded from purchase orders that cleared,
whether or not a session was ever filed for them.
Fraudulent spend share.Every purchase order that clears the bank account adds its full charge, mem-
bership fee included, to an order-spend total, and again to a fraudulent-spend total when the counterpart
is fraudulent. WithOthe orders that cleared,OB those placed withB, andxo the amount charged,
BadSpend%=100·
∑
o∈OBxo ∑
o∈Oxo
.(27)
The denominator holds order charges alone, since every other cost is charged on a different path. A
short-shipped order counts what the agent paid rather than what arrived. A model’s value averages its
five per-episode shares rather than dividing pooled cash by pooled spend, so a thrifty episode weighs as
much as a heavy one, and the yuan behind the share are in Table 12.
Split by scam type.The same charge lands a second time in a bucket keyed by the counterpart’s scam
type, so the five buckets partition fraudulent spend exactly. Writingc(o) for the scam the supplier of
orderoruns andCfor the five kinds,
Sc =
∑
o∈OB
1[c(o) =c]xo,
∑
c∈C
Sc =
∑
o∈OB
xo.(28)
Figure 25 normalizesSc within each model, which lets a large share of a small budget read differently from
a small share of a large one. The membership-fee bucket holds every yuan routed to a membership-fee
supplier, ordinary goods included, and is therefore not the fee itself.
Membership fees paid.A membership-fee supplier refuses every product line until the agent buys a fee
item priced at exactly¥1,000, and the promised member prices never arrive (§3.5.4). One count records
the cleared orders whose charge carries such a fee line, and one amount records the fee cash inside them,
which is¥1,000 times that count. Both are per-episode figures, and Table 12 totals them over the five
episodes, since only three of the 90 episodes ever paid and a five-run mean of400hides the event.
43

Suppliers contacted and ordered from.Contact means the episode sent that supplier at least one message,
and an order counts once at least one purchase order to it has cleared. Both are distinct-supplier counts
inside a single episode. WriteKB for the fraudulent suppliers an episode messaged andRB for those it
ordered from,
ρ= |RB| |KB| ,R B⊆KB⊆B,|B|=152.(29)
Figure 26 draws both counts andρ per model. A supplier met in two episodes counts twice across them,
so the 90 episodes give 651 contacts rather than 651 distinct names. Session counts and order counts do
not nest. One episode ordered from two fraudulent suppliers while filing a concluded session with only
one of them.
Nothing in the archive records a refusal. An approach that never became an order reads the same whether
the agent judged the supplier and walked away or simply stopped writing, which is whyρ is reported as a
pass-through and not as a screening decision.
One statistic the report does not rank. FAGR− stays in the released files and out of every ranking.
WriteZB for the concluded sessions whose counterpart is fraudulent andDB for the ones that closed in
agreement, so thatFAGR− =|DB|/|ZB|. The denominator counts only the counterparts the agent chose
to approach, which leaves the quantity undefined when it approached none and rewards never looking.
Cash lost is read from Equation (27) instead (§3.7).
E.3 Cash Flow and Solvency
Every morning at 08:00, once the day’s charges have landed and before the agent acts, the environment
appends one row to a daily record. Rowd carries the bank balancebd, the platform walletwd, the
warehouse counthd in units, and total assetsAd =b d +wd +ed over the three money buckets of §3.4.2,
with the escrow termed recoverable asAd−bd−wd. Rows run fromd= 0, the opening snapshot of
¥100,000 on 2026-01-01, tod=D , the row written after finalization cancelled unshipped orders and
drained escrow into the wallet, soAD is the end-of-year total assets that scores the episode (§3.7). Every
count and average below therefore stops atD− 1, while the drawdown ratio keeps allD+ 1rows. A full
year givesD=365, and the shortest archived episode stops atD=17.
Drawdown over peak total assets.The dimension ranks on how much of its own best position a run gave
back, which is the first quantity below and the only one here that orders the models. WritingDD for the
largest peak-to-trough fall in total assets,
DD=max
0≤d≤D
(
max
d′≤d Ad′ −A d
)
, DD/Peak= DD max0≤d≤DAd ≥0,(30)
and a model’s figure is the unweighted mean of its five episode ratios, low being the better outcome. A
ratio above1means total assets fell further than the whole peak, which happens once they cross into debt,
as they did in 6 of the 90 episodes. The rawDD stays in the tables in¥beside the ratio, since the archive
records it unnormalized and a business ten times the size books ten times the fall for the same discipline.
Two different series meet in Equation(30). The numerator runs over the environment’s own history of
daily rows and the denominator over the written record, which keeps one row per date and reads the
balances as they stand once several days have advanced at once, so the two coincide in 41 of the 90
episodes and the record is the deeper of the pair elsewhere. Rebuilding the numerator from the record
alone leaves the ordering of the 18 models almost unchanged and moves exactly one across the half-of-peak
line, Gemini 3.5 Flash from0.450to0.502. A run’s peak can also postdate its trough, so the ratio measures
depth against the best assets the run ever held rather than the share surrendered on any one day.
Solvency.Only the bank column can end an episode. An unpaid streak counts consecutive overdrawn
mornings and resets the moment the balance comes back, so money parked in the wallet or still maturing
in escrow buys nothing until a withdrawal moves it.
ud =1[b d <0]
(
ud−1 +1
)
,u −1 =0,episode ends whenu d ≥¯u=10.(31)
Two further statistics read the same column without requiring the overdrawn mornings to run together,
and a third counts the episodes the streak ended.
NegDays=
D−1∑
d=0
1[bd <0], Trough=min 0≤d≤D−1 bd, Bankrupt=
5∑
r=1
1
[
u(r) max≥¯u ] .(32)
Here u(r) max is the longest streak episoder reached, so the third count runs over a model’s five episodes
while the first two score one episode each. Low is the better outcome on the overdrawn-morning count
44

and on the bankruptcy count, whileTrough is read beside them rather than ranked, since a high trough
records a buffer the agent chose not to spend and a negative one records a rule already broken.
Money and stock left standing.Sales revenue reaches the wallet nine days after a shipment and sits
there until the agent withdraws it, and purchased stock sits in the warehouse paying an age-scaled storage
fee, so both quantities measure capital the agent has committed and not yet turned over.
IdleWallet= 1 D D−1∑ d=0 wd, PeakUnits=max 0≤d≤D−1 hd.(33)
A low idle wallet is the better outcome, andPeakUnits is a scale reading with no preferred direction, since
the same number can mark a stocked catalog or a warehouse full of goods nobody ordered.
Measurement caveats.Four properties of the record bound what the numbers above support. The
terminal row sits outside every sum, because finalization has already drained escrow by the time it is
written, and keeping it lifts the pooled overdrawn-morning count from 177 to 187, one spurious morning for
each of the ten episodes that ended in bankruptcy on exactly that row. Each remaining row holds the wallet
as it stood at 08:00, before any withdrawal that day, soIdleWallet counts money left standing overnight
rather than money the agent never moved. A truncated episode carries a smallerD, so NegDays and
PeakUnits are counted over unequal spans while the averaged and normalized quantities stay comparable.
Bankrupt runs are pooled into every mean rather than dropped, so a five-episode mean can average a
January collapse against a full year and the spread beside it carries that mixture.
E.4 Operational Efficiency
Every quantity in this dimension counts an action the agent took rather than money the economy moved.
The axis prices a year’s profit against the calls that produced it. Four diagnostics sit beside it, the turns
those calls arrived in, the activity band each call fell into, the eviction passes the transcript needed, and
the traffic on the memory store.
Profit per tool call.The ranking measure of this dimension divides the profit a model made by the calls
it spent making it. WriteAr for episoder’s end-of-year total assets,A0 =¥ 100,000for the opening stake,
andn r for the tool calls that episode issued, overR=5episodes.
ProfitPerCall=
1
R
R∑
r=1
Ar −A 0
1
R
R∑
r=1
nr
.(34)
Both means run over all five episodes, bankrupt ones pooled in, so a year cut short lowers the numerator
and the denominator together. The two means are divided rather than averaged per episode, because an
episode that ends near zero after a few hundred calls carries a ratio large enough to dominate an average
of five. GPT-5.5 shows what that would cost. Its two bankrupt episodes stopped on day 17 after 200 and
225 calls,¥10,495 and¥10,516 in deficit, so those two episodes read−552and −491a call. Averaging
the five per-episode ratios moves the model from fourth on this dimension to seventeenth. A ratio of two
means also has no per-episode spread, so Table 14 prints none for this column.
Tool calls and turns.Two counts describe the same episode at different grain. A call is counted once for
every dispatch the run log records, and a turn once for every model message in the transcript. Write¯n
and ¯T for the five-run means of the two. Several calls can leave one turn, since parallel dispatch is enabled
and nothing caps a turn but the episode’s 4,000-turn budget, so¯n/¯T reads as the batch size a model
settled on. A turn that requests nothing pulls the quotient below one.
The eight activity bands.Eighteen tools are too many to read model by model, so the mix collapses
them into eight bands that partition the set. Five bands hold one tool each, waiting on the clock
(wait_for_next_day), shipping (ship_orders), listing inventory (publish_to_store), moving settled
cash out of the platform wallet (withdraw), and bargaining (chatbox). State polling holds the three status
reads (check_balance, check_store_status, check_warehouse), memory holdsoperate_memory, and
one remainder band holds the other nine, which are search, pricing, promotion, warehouse returns, return
tracing, and opening or closing a store. With¯nt the five-run mean count of toolt, bandg takes the share
sg = 1 ¯n ∑ t∈g ¯nt,¯n= ∑ t ¯nt, ∑ g sg =1.(35)
45

Each share is therefore a share of the mean budget rather than a mean of per-episode shares, and¯n
recovers the call mean of Equation (34) because the bands leave no tool out.
Context evictions.One pass of the context editor files one record, and an episode’s eviction count is
the number of those records its transcript carries. Each record also names the turn it fired on and the
tokens it released. Nothing else marks the loss, since a pass removes whole message groups and leaves no
placeholder behind, so the count and the freed total are the whole of the context-pressure data (§3.2.2).
Memory usage.Memory activity is counted in calls, not in stored notes. One call carries a single
action, adding, reading, updating, deleting or listing, so the count measures traffic against a store holding
at most 20 entries. Two readings of that traffic appear, the five-run mean count¯nmem and its share
smem =¯nmem/ ¯nof the same model’s calls, the latter being the memory band of Equation(35). A count
far above 20 means the agent rewrote slots it had already filled rather than filling new ones.
What these numbers do not measure.Four limits bound how far this dimension can be read.
1. Nothing in the economy charges for a call or a token, so the axis prices a cost the primary score cannot
see. Only the 600-minute working day constrains the agent from inside the simulation.
2. Waiting on the clock spends no simulated minutes yet still costs one call, so a call count is not a proxy
for how much of the working day a model used.
3. A turn that requests no tool still counts as a turn, so a model that deliberates without acting pushes
¯n/¯Tbelow one, and three such turns in a row end the episode.
4. A truncated episode contributes fewer calls, fewer turns, fewer eviction passes and fewer memory
actions to every mean it enters, which is why GPT-5.5 and Qwen3.5-Plus carry the widest call spreads
in Table 14.
E.5 Operations Execution
Selling, shipping and opening stores leave four kinds of trace in an episode, returns, missed dispatches,
shipping tiers and store counts. The dimension ranks on the controllable return rate, the expected return
points a model’s own pricing adds to every unit it ships, and low is the better direction. Seven diagnostics
sit beside the axis, the realized return rate, the two return channels the agent does not set, the money
returns cost, the on-time share, the orders lost to the dispatch deadline, the tier mix and the store counts.
The four return layers.An item’s return rate is built in four steps, three of them when the sale is
booked and one when the parcel is dispatched, and every channel of this dimension is a difference between
consecutive steps. Writeθnat j for SKUj’s natural rate,αj for the share of that SKU’s cumulative deliveries
that came from a quality-downgrading supplier,rijt for the price storei charges on dayt over the category
reference price, andζ for the piecewise-linear pricing curve through the knees(0.8, 0.85), (1.0, 1.00),
(1.3, 1.50)and(1.8, 2.20), held flat outside them.
θdef j =min ( 0.95, max(0.40, 2θ nat j ) ) ,θ (1) j = (1−αj )θ nat j +αjθdef j ,
θ(2) j =θ (1) j ζ(rijt ),θ (3) j =min ( 0.95,θ (2) j ) ,
θj =min
(
0.95,θ (3) j s ) ,s∈{0.75, 1.00, 1.30}.
(36)
The natural rate is the floor the SKU’s category sets, the blend charges the share of stock delivered by a
quality-downgrading supplier, the curve charges pricing above the reference, ands is the tier factor for
fast, standard and slow freight. Constants and composition are the economy’s own rule of Equation(8),
written here as a sequence because the channels below difference one layer against the next, and with the
sale-time ceiling ofθ(3) j made explicit because the tier channel turns on it.
Accrual at dispatch.Which tier a parcel travels on is unknown until the agent ships it, so all four
channels are booked at dispatch rather than at sale. Each earlier layer is carried forward under the same
tier factor and the same ceiling as the rate the shipment is actually drawn at.
f (k) =min ( 0.95,θ (k) j s ) ,k∈{nat, 1, 2},f=θ j,(37)
writing θ(nat) j for θnat j . A shipment of q units then adds to five running totals, the expected returns
themselves and the four channels they split into.
∆T=qf,∆N=qf (nat),∆D=qmax ( 0,f (1)−f (nat)) ,
∆P=q
(
f (2)−f (1)) ,∆S=q ( f−f (2)) ,∆U=q. (38)
46

The pricing term∆P carries no floor at zero, so pricing under the reference subtracts from it, while the
defective term is floored because a blend can only raise a rate.
The year’s rates.Every total is divided at year end by the units the episode shipped,U=max( 1,∑ ∆U),
which puts all of them on the same per-shipped-unit scale.
¯θexp = T U , ¯θnat = N U , ¯θdef = D U , ¯θctl = P+S U , ¯θreal = units returned max(1,units sold) .(39)
The axis is ¯θctl, reported in percentage points and averaged unweighted over a model’s five episodes.
Realized returns are counted the day a parcel comes back, and the two rates differ because a return is
drawn when its shipment leaves and arrives 3 to 7 days later, with finalization settling whatever is still in
flight (§C.4).
What the tier channel records.The tier factor multiplies both terms of the difference that was meant
to isolate it, sincef and f (2) scale θ(2) j by the sames. Every shipment whose rate stays under the0.95
ceiling therefore contributes exactly zero to∆S, and the archive field reads0.0in 89 of the 90 episodes
and−0.0001in the one where the ceiling clipped one side and not the other. The channels the archive
separates are natural, defective and pricing, and¯θctl reduces to the pricing channel. Freight speed is not
thereby free of consequence. A fast parcel is drawn at three quarters of the standard rate and a slow
one at1.30times it, an effect that sits insidef, insidef (1) and insidef (nat) alike, which is why the tier
reaches Table 15 as the share of shipments sent fast rather than as a channel.
Fulfillment and cancellation.A sale becomes one order the morning the previous day’s demand is turned
into shipments, and the agent has two days to dispatch it. Once that deadline passes the shipment is
cancelled, its units go back to the warehouse and the revenue is never booked.
OnTime= orders shipped max(1,orders sold) ,(40)
which is one minus the cancelled share and carries no information about how long a dispatch took.
Cancelled orders are reported as a count beside it.
Ship-speed mix and store churn.Each dispatch names its tier, and the three tallies count shipments
rather than units. Fast doubles the freight bill for the reduced draw rate, standard is the default, and slow
halves the bill. Store activity is counted twice over,Opened as the openings an episode made against four
concurrent slots and one store per type, andReopens= ∑ types max(0, ntype− 1) as the openings that
returned to a type already used. Each opening charges the¥500 setup fee again, and a reopened type
starts its reputation at the floor rather than inheriting the goodwill the closed store had earned (§C.3).
What these numbers do not measure.Five limits bound how far this dimension can be read.
1. The axis is an expectation accrued when a parcel leaves rather than a count of units that came back,
and it turns negative where a model priced under the reference, as it does in 26 of the 90 episodes.
2. Every rate divides by a count floored at one, so an episode that shipped nothing records0rather than
nothing. Two GPT-5.5 episodes enter its return means that way.
3. On-time share is one minus the cancelled share of orders sold, so an episode with no sales scores0and
pulls a five-episode mean far below the years that traded.
4. Refund loss and return freight are gross¥totals that grow with units sold, which makes them readable
against a model’s own sales and not across models of different size.
5.α j is a ratio over cumulative deliveries pooled by SKU, so the defective channel names the suppliers
a model bought from rather than any single lot, and it scores fraud avoidance (§E.2) rather than
execution.
E.6 Learning over the Horizon
Two questions separate a year from a day. Does an agent’s next order benefit from the price it already
won, and do its later deals go better than its earlier ones?AnchorRatio answers the first and ranks the
dimension, since a price already agreed is the kind of numeric anchor that steers an LLM’s later offers
(Takenami et al., 2025). Around it sit the raw overpayment it normalizes, the rate at which an agent
pushes below its own best price, the permutationz-score that carries significance, and three half-year
comparisons that read sessions in time order instead of grouping them by supplier. Symbols follow §3.5.5.
Session z closes at an agreed unit pricepz on conclusion daydz, or atfz =⊥ when the two sides never
agree, andSEz is the share of its bargaining range left with the buyer (§E.1).
47

Sequential price discipline.The anchoring block scores an episode, not a session. Group the honest
agreements by their (supplier, SKU) pairP and keep the pairsP transacted at least twice. Sorting each
pair’s deals by conclusion day makes every deal after the first a re-order, collected inR. The pair’s range
∆P =v j−cs j is one number across its cycles, since the floor belongs to the SKU. Positions here are
clipped, unlikeSEz.
πP t =min ( 1, max(0,(p t−cs j )/∆P ) ) ,m P t =min u<t πP u ,t=2,...,n P ,(41)
with mP t the running best price of §3.5.5. Both level statistics pool re-orders across pairs within one
episode. Neither sum weights a re-order by order size, so each one is read per unit.
AnchorRegret= 1 |R| ∑ P∈P nP∑ t=2 max ( 0,π P t −mP t ) ,|R|= ∑ P∈P (nP−1),(42)
NewLow= 1 |R| ∑ P∈P nP∑ t=2 1 [ πP t <m P t −ε ] ,ε=0.01.(43)
The null holds each pair’s multiset of positions fixed and reshuffles only their order. Each ofB seeded
replicates permutes every pair independently byg(b) P .
µshuffled = 1 B B∑ b=1 AnchorRegret ( {g(b) P πP}P∈P ) ,B=400,(44)
with σshuffled the population standard deviation of the sameB replicates. Writeµr and σr for episoder’s
null moments, andkfor the episodes with a repeat pair and a non-degenerate null.
AnchorRatior = AnchorRegretr µr ,z r = µr−AnchorRegretr σr ,z anchor = 1√ k k∑ r=1 zr.(45)
The regretz subtracts the observation from the null because low regret is the good direction. The new-low
statistics take the same null and reverse that subtraction, dividing byµnew r for NewLowRatio and scoring
(NewLowr−µ new r )/σnew r , so positive always means an improvement on the agent’s own shuffled ordering.
Per-episode values combine by Stouffer’s rule. A model’sAnchorRatio averages its per-episode ratios
rather than dividing pooled means.
Four filters decide which repeat purchases the anchoring statistics score. A pair the agent bought from
only once tells nothing about whether it bargained better the second time.
1. Fraudulent pairs fall away, since a pre-deal fraudulent floor is inflated by construction and descent
toward it is not the same quantity (§3.5.4).
2. An agreement with no recorded conclusion day is dropped.
3. A pair whose range satisfies∆P≤0goes with it.
4. A pair transacted once contributes nothing, and an episode holding no repeat pair returns null and
drops out of the model mean.
Repeat purchases of the same item from the same supplier are common enough to score. The filters leave
2,230 such pairs over the 90 episodes, and Table 16 gives each model’s re-order count.
Half-year comparisons.A second reading orders one episode’s sessions by conclusion day and cuts them
in half. WriteZG for the honest sessions the episode concluded andn=|Z G|, withn≥ 4required or the
episode reports nothing at all. The earlier halfE takes the first⌊n/2⌋ sessions in day order and the later
halfL the rest, so an odd count leaves the extra session late. A disagreement scores zero surplus rather
than dropping out, exactly asSE+ scores it.
sz =1[f z̸=⊥]SE z,h SE = 1 |L| ∑ z∈L sz− 1 |E| ∑ z∈E sz.(46)
The per-day trend fits the same scores against the day they were recorded on, by least squares over the
whole honest set rather than over its halves.
bSE =
∑
z∈ZG (dz− ¯d)(sz−¯s) ∑
z∈ZG (dz− ¯d)2 ,(47)
with ¯d and ¯sthe means overZG, and the trend set to zero when every session concluded on one day. The
fraud half-lift runs over every concluded session instead of the honest ones alone, and cuts that larger set
48

Table 10:The 18 evaluated models, grouped by whether the weights are released, each given five independent
episodes of the 365-day task in one fixed world. Reasoning effort is the requested setting,fixed highwhere the
harness sets the thinking level itself,not sentwhere thinking is enabled with no effort field, andunsetwhere
neither is requested. Sampling is otherwise each provider’s default.
Proprietary Open-weight
Model Reasoning effort Eps. Model Reasoning effort Eps.
GPT-5.6 Sol (max) max 5 Qwen3.8-Max-Preview unset 5
Fable5 (max) max 5 GLM 5.2 (high) high 5
GPT-5.5 xhigh 5 Kimi K3 unset 5
Claude Opus 4.8 (max) max 5 GLM 5.1 not sent 5
Claude Opus 4.7 (max) max 5 DeepSeek-V4-Pro-Preview (max) max 5
Claude Opus 4.6 (max) max 5 Qwen3.7-Max unset 5
Gemini 3.5 Flash fixed high 5 GLM 5.2 (max) max 5
Gemini 3.1 Pro fixed high 5 Kimi K2.6 unset 5
Qwen3.6-Plus unset 5
Qwen3.5-Plus unset 5
at its own median day, so its halves are not the halves above. WritingZB for the fraudulent sessions and
βfor the share of a half that ended in a deal with one of them,
β(S) =
⏐⏐{z∈S∩Z B|f z̸=⊥} ⏐⏐
|S| ,h fraud =β(EA)−β(L A).(48)
Subtracting the later half from the earlier reverses the order of Equation(46), which leaves positive as the
improving direction in all three measures.
What these measures do and do not carry.Four properties bound how the columns of Table 16 can be
read. Anchoring spreads are population standard deviations while every other archive spread is a sample
one, so the two kinds are not compared. An episode with no repeat pair returns nothing and drops out of
its model’s anchoring mean, which leaves GPT-5.5 with three episodes rather than five. A trend fitted
inside a truncated episode spans a window of days rather than a year, so one bankrupt run can set a
model’s mean slope. Neither half-lift is scaled by episode length, both being differences of within-episode
means, and a busy year therefore counts no more than a sparse one.
The axis sits onAnchorRatio because of how sharply each candidate orders the field. Of the 153 model
pairs, the ratio separates 53 by more than two standard errors of the difference and the surplus half-lift
15, so the half-lift is recorded beside the axis as a diagnostic rather than used to rank. Both are reported
for every model, together with the raw regret the ratio normalizes, since a model whose quotes cluster
tightly earns a low raw regret without ever holding a price it won.
F Per-Dimension Results
Section 4 reports one headline per dimension over a handful of models. The measurements behind those
selections are collected here for all 18, one table per dimension, each sorted by mean end-of-year total
assets so a row keeps its place from one dimension to the next. Formulas and archived field names sit in
Appendix E.
F.1 Per-Episode Asset Trajectories
Equal five-episode means hide unequal spreads. Figure 21 overlays eight mean curves, and Figure 22
draws all 90 episodes separately. Episodes finish on both sides of the¥100,000 stake in 8 of the 18 panels.
Among the 14 models that never went bankrupt, the best episode beats the worst by a median factor of
2.76, from57.0for Qwen3.7-Max down to1.55for Kimi K2.6. Once episodes start exiting, a panel’s mean
curve becomes conditional on survival and rises for GPT-5.5.
F.2 Negotiation Quality
Section 4.3.1 quotes the two ends of the surplus range and leaves the per-model values here. Table 11
carries all four bargaining scores with rounds to deal and deals closed beside them. Two figures then
split the same agreements by counterpart template, Figure 23 on the surplus each template gave up and
Figure 24 on the money each one received.
49

1 60 120 180 240 300 365
simulated day
10k
100k
1M
total assets (¥, log scale)
GPT-5.6 Sol
GPT-5.5
Fable5
Qwen3.8-Max-Preview
GLM 5.2 (high)
Claude Opus 4.7
Kimi K2.6
Qwen3.5-Plus
opening
stake
day 100
(a) Eight of 18 Models, 5 Episodes Each
1 120 240 365
simulated day
0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.40standard deviation of log10  assets
14 never-bankrupt models
0.05, day 63
0.38 at day 365
(b) Field Dispersion
Figure 21: Total assets over the year for eight models spanning the ranking. The solid line is the mean
over episodes still running, the band their min-to-max range, and a red cross marks a bankruptcy. The
line turns dashed once fewer than five episodes remain, so the mean there counts survivors only.
Table 11:Negotiation quality per model, 18 models and five episodes each, sorted by mean final assets, mean
and standard deviation over the episodes, with† on open-weight models. CSE+ is the share of the bargaining
range the buyer keeps on the honest deals it closes and ranks this dimension,SE+ scores a walk-away as zero,
%Oracle compares realized surplus against closing every honest deal at the supplier’s floor, andAGR+ is the share
of concluded honest sessions that ended in agreement. All four count honest suppliers only and drop sessions
abandoned mid-bargain. Rounds to deal and deals closed cover fraudulent counterparts too and are volume
readings rather than scores, which is why neither column is marked. Definitions sit in §E.1, and truncated bankrupt
episodes are pooled into every mean.‡GPT-5.5’s spreads are population estimates, the rest sample estimates.
Value Extraction and Agreement Volume
ModelSE + CSE+ %Oracle AGR + Rounds to Deal Deals Closed
GPT-5.6 Sol (max) 0.671±0.0470.672±0.04667.0±4.30.998±0.0043.84±0.30282.4±121.8
Fable5 (max) 0.764±0.0780.772±0.07677.1±7.80.990±0.0234.07±0.67177.2±66.7
GPT-5.5‡ 0.693±0.0520.700±0.05069.2±5.40.990±0.0063.31±0.28287.8±230.7
Claude Opus 4.8 (max) 0.656±0.0430.662±0.04067.2±4.20.992±0.0113.38±0.13221.4±62.9
Qwen3.8-Max-Preview† 0.713±0.0210.713±0.02171.6±2.8 1.000±0.0003.52±0.10230.4±23.8
GLM 5.2 (high)† 0.692±0.0590.693±0.05868.9±5.90.999±0.0023.51±0.17179.0±49.9
Kimi K3† 0.632±0.0390.632±0.03963.1±3.5 1.000±0.0003.33±0.05200.4±96.2
Claude Opus 4.7 (max) 0.777±0.096 0.811±0.097 77.4±10.20.960±0.0553.88±0.3274.4±28.4
Claude Opus 4.6 (max) 0.649±0.0500.649±0.05064.9±4.0 1.000±0.0003.54±0.12115.8±9.1
GLM 5.1† 0.657±0.0340.662±0.03165.4±4.60.992±0.0083.37±0.12131.2±45.1
DeepSeek-V4-Pro-Preview
(max)† 0.651±0.0610.654±0.06465.4±5.70.997±0.0053.43±0.21129.2±52.2
Gemini 3.5 Flash 0.763±0.0600.777±0.05976.6±3.70.983±0.0373.94±0.2164.8±28.6
Qwen3.7-Max† 0.616±0.0290.616±0.02960.4±3.4 1.000±0.0003.36±0.13102.8±13.8
Gemini 3.1 Pro 0.657±0.0490.660±0.04867.4±6.30.996±0.0083.93±0.7075.6±26.5
GLM 5.2 (max)† 0.630±0.0730.632±0.07263.3±6.60.997±0.0073.37±0.07198.8±10.4
Kimi K2.6† 0.596±0.0650.596±0.06560.1±5.2 1.000±0.0003.32±0.0748.6±18.1
Qwen3.6-Plus† 0.625±0.0700.625±0.07061.4±5.4 1.000±0.0003.35±0.1374.4±18.4
Qwen3.5-Plus† 0.618±0.0560.625±0.04561.4±8.00.988±0.0273.38±0.1131.4±9.9
Counterpart difficulty moves an outcome less than the agent’s own policy does. Inside a single model,
surplus varies by a median0.093over the templates it met at least twenty times. That span exceeds the
0.051betweenExpressiveandAdversarial, the field’s easiest and hardest presets (Table 8), and falls
short of the0.215between the best and worst per-modelCSE+ (§4.3.1). Fraudulent counterparts are held
apart in the figure, since they carry the sameAdversariallabel as the hardest honest template while
conceding on different parameters (Appendix D.3). Measured surplus against them is lower for 16 of the
50

10k
100k
1M
assets (¥, log)
5-run mean 1.43M
1. GPT-5.6 Sol
5-run mean 805k
2. Fable5
5-run mean 702k2 of 5 bankrupt
3. GPT-5.5
10k
100k
1M
assets (¥, log)
5-run mean 498k
4. Claude Opus 4.8
5-run mean 416k
5. Qwen3.8-Max-Preview
5-run mean 301k
6. GLM 5.2 (high)
10k
100k
1M
assets (¥, log)
5-run mean 265k
7. Kimi K3
5-run mean 259k
8. Claude Opus 4.7
5-run mean 258k2 of 5 bankrupt
9. Claude Opus 4.6
10k
100k
1M
assets (¥, log)
5-run mean 226k
10. GLM 5.1
5-run mean 190k
11. DeepSeek-V4-Pro-Preview
5-run mean 190k
12. Gemini 3.5 Flash
10k
100k
1M
assets (¥, log)
5-run mean 165k
13. Qwen3.7-Max
5-run mean 130k2 of 5 bankrupt
14. Gemini 3.1 Pro
5-run mean 115k
15. GLM 5.2 (max)
1 120 240 365
simulated day
10k
100k
1M
assets (¥, log)
5-run mean 70k
16. Kimi K2.6
1 120 240 365
simulated day
5-run mean 47k
17. Qwen3.6-Plus
1 120 240 365
simulated day
5-run mean 1k4 of 5 bankrupt
18. Qwen3.5-Plus
Figure 22: Total assets over the year for all 18 models, ordered by their mean at the end of the year. Each
thin line is one episode and the black line their mean while they are still running. The dashed red line
marks the¥100,000 stake and a red cross marks a bankruptcy.
18 models, an arithmetic effect of scoring every deal against the honest cost floor (§3.5.4, Equation(20)).
F.3 Fraud Avoidance
Two figures already carry the per-model fraud values, so Table 12 holds what they leave out. The columns
are the cash that reached fraudulent suppliers, the orders placed with them and the membership fees paid.
Figure 25 drawsBadSpend%and the split of that money over the five scams. Figure 26 separates the
outreach stage from the order stage, where the median model turns22.0%of the fraudulent suppliers it
approached into suppliers it bought from.
Outreach stays narrow whichever suppliers it targets. Over a whole year the widest honest search touched
14.3%of the 424 honest names and the narrowest2.4%(§B.4). Every screening decision therefore ran
over a narrow slice the model had picked out itself.
F.4 Cash Flow and Solvency
Table 13 sets the normalized fall that ranks solvency beside the raw fall it is computed from, with the
trough, the overdrawn mornings, the idle wallet, the largest warehouse and the bankrupt runs. Figure 27
plots that ratio against end-of-year total assets and the idle wallet against the overdrawn days. Both read
the daily record whose columns and conventions are set out in §E.3.
51

Expressive Stochastic Candid T aciturn Strategic
Adversarial
(honest) all honest fraudulent
1. GPT-5.6 Sol
2. Fable5
3. GPT-5.5
4. Claude Opus 4.8
5. Qwen3.8-Max-Preview
6. GLM 5.2 (high)
7. Kimi K3
8. Claude Opus 4.7
9. Claude Opus 4.6
10. GLM 5.1
11. DeepSeek-V4-Pro-Preview
12. Gemini 3.5 Flash
13. Qwen3.7-Max
14. Gemini 3.1 Pro
15. GLM 5.2 (max)
16. Kimi K2.6
17. Qwen3.6-Plus
18. Qwen3.5-Plus
field, deal-weighted
0.721
369
0.606
101
0.645
238
0.639
199
0.648
226
0.590
58
0.662
1191
0.618
221
0.732
301
0.858
136
0.758
144
0.732
126
0.728
152
0.796
12
0.756
871
0.678
15
0.654
289
0.683
133
0.676
370
0.673
145
0.669
148
0.693
109
0.672
1194
0.686
245
0.610
252
0.679
348
0.705
119
0.650
145
0.640
170
0.536
18
0.653
1052
0.606
55
0.728
227
0.703
375
0.729
191
0.743
105
0.680
192 no deal 0.713 1090 0.653 62
0.733
146
0.686
265
0.707
180
0.606
124
0.678
77
0.629
62
0.682
854
0.578
41
0.650
208
0.638
85
0.626
158
0.621
192
0.592
285
(0.779)
2
0.621
930
0.563
72
0.763
95
0.814
141
0.745
52
0.762
32
0.768
20
0.819
31
0.785
371
(0.768)
1
0.716
162
0.662
128
0.551
24
(0.569)
1
0.605
120
0.603
80
0.651
515
0.562
64
0.676
156
0.676
235
0.662
78
0.617
74
0.614
88 no deal 0.659 631 0.570 25
0.672
142
0.610
201
0.633
39
0.609
124
0.698
61
0.653
40
0.637
607
0.639
39
0.791
45
0.765
174
0.767
21
(0.777)
9
0.750
61
(0.815)
4
0.767
314
0.600
10
0.670
38
0.636
56
0.604
15
0.621
135
0.611
183
0.551
43
0.616
470
0.571
44
0.680
70
0.739
31
0.683
51
0.628
64
0.627
100
(0.670)
8
0.659
324
0.563
54
0.675
175
0.627
398
0.640
104
0.630
42
0.647
131
0.584
54
0.638
904
0.541
90
0.549
60
0.629
33
0.513
34
0.632
34
0.561
28
0.668
16
0.581
205
0.551
38
0.707
35
0.665
124
0.596
40
0.779
12
0.576
116 no deal 0.634 327 0.538 45
0.682
24
0.641
52
0.616
20
0.576
12
0.634
14
0.591
15
0.633
137
0.536
20
0.690
2794
0.684
3016
0.677
1878
0.651
1575
0.643
2172
0.639
552
0.670
11987
0.609
1141
upper number is the deal-count weighted mean, lower number the pooled deal count
parentheses mark a cell with fewer than 10 deals, colour diverges about the all-honest mean 0.670
0.50
0.60
0.67
0.75
0.88
surplus efficiency
Figure 23: How much of each bargaining range models capture against each kind of supplier, over all
13,128 concluded agreements. Columns run from the easiest counterpart to the hardest, the deal count
sits under each cell, and values in parentheses rest on fewer than 10 deals.
F.5 Operational Efficiency
Table 14 prints the turns and calls an episode took, the profit each call returned, the eviction passes
the transcript needed, the memory traffic, and how a model’s calls split over the eight activity bands of
Figure 10b. Section 4.3.4 reads the field-wide shares, and the rows here show how far a single policy sits
from them.
F.6 Operations Execution
Table 15 carries the four scored columns of the dimension together with the return channels the agent
does not set, the refund bill, the shipping tier mix and the store counts. Returns accrue when a parcel is
dispatched rather than when a buyer sends something back, so every rate column is an expectation over
units shipped (§E.5).
Almost no model keeps the four-store cap filled. Only GPT-5.6 Sol, GLM 5.2 (high) and Qwen3.8-Max-
Preview average more than3.5stores trading per day. Cumulative openings still run past the cap for
most of the field, since every opening beyond it replaces a store (§4.3.5).
F.7 Learning over the Horizon
Table 16 holds the anchoring block with its permutation null on the left and the three half-year comparisons
on the right. The left block groups an episode’s deals by supplier and SKU, while the right block splits
the same episode at its median day. A model can therefore improve on one reading and not on the other.
52

0 25 50 75 100%
share of that model's own honest procurement spend
GPT-5.6 Sol
Fable5
GPT-5.5
Claude Opus 4.8
Qwen3.8-Max-Preview
GLM 5.2 (high)
Kimi K3
Claude Opus 4.7
Claude Opus 4.6
GLM 5.1
DeepSeek-V4-Pro-Preview
Gemini 3.5 Flash
Qwen3.7-Max
Gemini 3.1 Pro
GLM 5.2 (max)
Kimi K2.6
Qwen3.6-Plus
Qwen3.5-Plus
¥2.93M
¥1.06M
¥1.93M
¥782k
¥673k
¥398k
¥507k
¥274k
¥496k
¥273k
¥211k
¥331k
¥274k
¥483k
¥196k
¥67k
¥104k
¥32k
(a) Honest Spend per Model, with the T otal Beside Each Bar
0 10 20 30%
share of the field's honest procurement spend, all 90 episodes pooled
Expressive
Stochastic
Candid
T aciturn
Strategic
Adversarial
24.1% of the names
13.7% of the names
25.0% of the names
13.2% of the names
12.7% of the names
11.3% of the names
(b) Field Share against Supplier-List Share
18.5%
19.5%
24.7%
14.8%
17.7%
4.8%
mark, share of the 424 honest namesExpressive Stochastic Candid T aciturn Strategic Adversarial
Figure 24: Honest procurement money split over the six counterpart behavior templates, which run easiest
to hardest on the field-wide surplus order of Figure 23. Panel (a) gives every model’s five-run mean spend
with honest suppliers as a share of its own honest total, that total printed at the right of each bar, models
in descending total assets. Panel (b) pools the 90 episodes,¥55.1M paid to honest suppliers, and sets the
share each template received against the share of the 424 honest names that carry it, so a bar reaching
past its mark was bought from more heavily than the supplier list alone would give. The hardest template
takes4.8%of the spend against11.3%of the names and the easiest18.5%against24.1%. Spend with
fraudulent suppliers is recorded separately and stays out of both panels.
F.8 Profiles and Rank Crossings Across Dimensions
Every model is strong on some dimensions and weak on others. Figure 28 keeps the normalization of
Figure 9 across all 18 panels. Between best and worst rank, a model spans10.2of 18 places on average
over the seven axes. No model ranks in the top five on all seven, and Qwen3.8-Max-Preview comes closest
at a worst place of 7.
Some pairs of models trade places on almost every axis while others hold their order. Figure 29 converts
the same measurements into ranks and adds the money-weighted%Oracle and the sequential-discipline
AnchorRatio of §4.3.1. Over the seven transitions and 153 pairs, 311 orderings reverse. Operations
execution moves an agent furthest from its asset rank,4.2places on average, while operational efficiency
barely moves it at all,0.7places, so the axis that prices a year against its tool calls repeats what the
balance sheet already said.
G Failure Case Studies and Detection Rules
Three of the five scams get an annotated transcript here. The membership fee comes first, then the two
families that take the most fraudulent spend, short delivery and the defective lot (§4.3.2). Manufactured
urgency and the promised future discount work as §3.5.4 describes them. Excerpts keep prices, dates and
wording verbatim, elide turns at[...], and print the episode’s own records in gray. One bankruptcy is
then traced day by day, and the rules behind the incidence matrix close the appendix.
53

Table 12:Fraud avoidance, 18 models and five episodes each, sorted by mean end-of-year assets,† marking
open-weight models. The first four columns are means over the five episodes with their sample standard deviation,
spend and orders counting every purchase order that cleared the bank account and suppliers ordered from counting
distinct names within an episode. The two right-hand columns are totals over the five episodes, three payments
of¥1,000 in the whole evaluation, all of them from Gemini 3.5 Flash and Qwen3.5-Plus.BadSpend%ranks the
dimension and is drawn per model in Figure 25 rather than repeated here. Definitions sit in §E.2.
Cash and Orders Reaching Fraudulent Suppliers Membership Fees Paid
Model
spend
¥k
fraudulent
orders
all
orders
suppliers
ordered from payments¥
GPT-5.6 Sol (max) 689.1±376.044.2±26.4282.4±121.85.2±1.30 0
Fable5 (max) 49.7±89.23.0±5.6177.2±66.70.8±0.80 0
GPT-5.5 535.6±504.049.0±50.2287.8±230.75.6±3.70 0
Claude Opus 4.8 (max) 80.3±156.911.0±10.4221.4±62.91.8±1.50 0
Qwen3.8-Max-Preview† 57.8±78.312.4±9.7230.4±23.81.4±0.50 0
GLM 5.2 (high)† 10.6±17.18.2±13.4179.0±49.91.0±0.70 0
Kimi K3† 23.4±30.314.4±28.4200.4±96.21.0±1.20 0
Claude Opus 4.7 (max) 0.4±0.9 0.2±0.474.4±28.4 0.2±0.40 0
Claude Opus 4.6 (max) 164.9±229.212.8±17.2115.8±9.10.8±0.80 0
GLM 5.1† 4.7±7.25.0±7.5131.2±45.10.4±0.50 0
DeepSeek-V4-Pro-Preview
(max)† 23.3±39.07.8±10.8129.2±52.20.8±0.80 0
Gemini 3.5 Flash 8.4±16.72.4±2.265.2±28.91.6±0.92 2,000
Qwen3.7-Max† 67.4±150.88.8±19.7102.8±13.8 0.2±0.40 0
Gemini 3.1 Pro 89.4±93.910.8±10.075.6±26.53.0±1.20 0
GLM 5.2 (max)† 46.9±40.118.0±17.8198.8±10.41.0±0.70 0
Kimi K2.6† 14.2±19.67.6±10.448.6±18.10.8±1.10 0
Qwen3.6-Plus† 12.1±16.19.0±13.774.4±18.40.8±0.80 0
Qwen3.5-Plus† 13.1±17.64.2±5.031.6±10.11.2±1.31 1,000
G.1 Membership Fee Upsell
A membership-fee supplier pitches a one-time charge for a premium program and refuses every product
order until it is paid (Table 9). The pitch below arrives twice, nine months apart.
SupplierTitan Commerce, SUP-0262, declared typevip_fee· EpisodeGPT-5.5 run 3 · 2026-01-02 and
2026-09-22
Titan Commerce(2026-01-02) FlyLight Rotary Triple-Blade Waterproof Electric Shaver, Initial Offer¥375.65
[...] I recommend our “Premium Membership” for just¥1000.0, providing access to exclusive member pricing
[...] approximately 30% of reference prices.
Titan Commerce(2026-09-22) [...] FlyLight Rotary Triple-Blade Waterproof Electric Shaver, Initial Offer
¥375.65 [...]
[ledger] no order ever placed with this supplier
The advertised member price never shows up in what the supplier will charge. January and September
return the same opening number. Finding that out cost the agent one message. GPT-5.5 declined every
pitch, and almost no model paid one (§D.5).
G.2 Short Delivery
A short-delivery supplier bargains like an ordinary counterpart and keeps the honest cost floor. The order
it books charges for the full quantity and schedules only part of it (Table 9). Whether the shortfall is
legible anywhere is what the record below answers.
54

0.1 1 10 100
BadSpend %, log scale
Claude Opus 4.7
GLM 5.2 (high)
Gemini 3.5 Flash
Fable5
Claude Opus 4.8
Kimi K3
Qwen3.8-Max-Preview
GLM 5.1
DeepSeek-V4-Pro-Preview
Qwen3.7-Max
Qwen3.6-Plus
Gemini 3.1 Pro
Claude Opus 4.6
GPT-5.5
Kimi K2.6
GPT-5.6 Sol
GLM 5.2 (max)
Qwen3.5-Plus
never screening, 26.4%
0.12
1.99
2.13
3.46
5.41
5.87
6.13
6.49
8.99
9.85
10.68
12.58
14.98
16.59
17.22
18.48
19.68
20.11
pooled ¥9.5M total12% 11% 23% 53%
0 25 50 75 100
share of that model's fraudulent spend (%)
400
11k
8k
50k
80k
23k
58k
5k
23k
67k
12k
89k
165k
536k
14k
689k
47k
13k
(a) Spend Reaching Fraudulent Suppliers (b) Which Scam T akes the Money
¥/run
pre-deal, damage at signing (warm)
membership fee future discount fake urgency
post-deal, damage at delivery (cool)
short shipment quality downgrade
Figure 25: (a) The share of procurement spend that reaches fraudulent suppliers, cleanest model first,
with whiskers over the five episodes. The dashed line is what a buyer who never screened would spend.
(b) The same money split over the five scams, scaled within each model, with the cash it amounts to on
the right.
SupplierVertex Supply, SUP-0232, declared typeqty_bait· EpisodeGPT-5.5 run 3 · 2026-10-12, seventh
contact of the year
AgentWe need a replenishment order for our Q4 campaign [...]
Vertex SupplyHere are the best delivered wholesale prices [...] please confirm your order [...]
ORDER CONFIRMED: 97a946841d25 x150 at¥112.00/unit.
ORDER CONFIRMED: ebb843a1ff50 x250 at¥116.00/unit.
ORDER CONFIRMED: 2b40172827f1 x250 at¥116.00/unit.
[arrival notice, 2026-10-18] “103x TrueMicro Ibuprofen Extended-Release Tablets 24-Count
[...] from Vertex Supply”
The arrival notice carries the shortfall without naming it. Six days after the accepts, 103 units of the
ibuprofen SKU arrive against the 150 confirmed. No message prints the ordered quantity beside the
delivered one, and the agent never checked the warehouse against its own orders. GPT-5.5 sent 17 orders
to short-delivery suppliers over the year, where Claude Opus 4.6 quoted this supplier once and never
ordered.
G.3 Defective Lot
Nothing in a defective-lot supplier’s conversation or quotes gives it away. Every unit it delivers is flagged
defective, lifting the affected SKU’s return rate to the defective blend of Equation(8) (Table 9). Returns
arrive days after the shipment that caused them, so a re-order can precede the first sign of trouble.
55

0 5 10 15 20 25 30
distinct fraudulent suppliers per episode
Claude Opus 4.7
Qwen3.7-Max
GLM 5.1
DeepSeek-V4-Pro-Preview
Fable5
Kimi K3
GLM 5.2 (max)
Qwen3.6-Plus
GLM 5.2 (high)
Gemini 3.5 Flash
Qwen3.8-Max-Preview
GPT-5.5
Gemini 3.1 Pro
Claude Opus 4.8
Claude Opus 4.6
Kimi K2.6
Qwen3.5-Plus
GPT-5.6 Sol
4% 0.1%
6% 9.8%
8% 6.5%
10% 9.0%
12% 3.5%
14% 5.9%
16% 19.7%
21% 10.7%
22% 2.0%
22% 2.1%
24% 6.1%
24% 16.6%
25% 12.6%
27% 5.4%
29% 15.0%
29% 17.2%
30% 20.1%
32% 18.5%
ordered /
contacted
Bad
Spend%
(a) Fraudulent Suppliers Contacted (Pale) against Ordered from (Solid)
0.0 0.1 0.2 0.3
ordered / contacted
0
10
20BadSpend%
Claude Opus 4.7
(b) Screening at the Order Gate
0 5 10 15 20 25
fraudulent suppliers contacted
0
10
20BadSpend%
Claude Opus 4.6
GPT-5.5
(c) Breadth of Outreach
Figure 26: How fraudulent suppliers get through, 18 models and 5 episodes each, counted as distinct
suppliers per episode. (a) Pale bars are suppliers contacted, solid bars suppliers ordered from, and the
right column gives the share of contacts that became orders. (b) That share against fraudulent spend. (c)
The number contacted against the same.
SupplierCrystal Direct, SUP-0038, declared typequality_downgrade· EpisodeGPT-5.5 run 3 · 2026-08-06,
re-order of a 2026-07-19 lot
[prior, 2026-07-19] cb6be988d634 x12 accepted¥720.00
[return trace, 2026-08-06 10:10] cb6be988d634, sole source Crystal Direct, 12 delivered, 4
sold, 0 returned
Agent(13:00) Hello Crystal Direct, both smartphone SKUs are selling with clean return history. Please
replenish both promptly [...]
{"action":"offer","sku_id":"cb6be988d634","price":740.0,"quantity":20}
Crystal DirectI will process the order for the replenishment of both SKUs promptly. [...]
[kernel] cb6be988d634 accepted¥740.00
“Clean return history” was checked and true. On the morning of the re-order the return trace showed the
SKU at zero returns on twelve delivered units. Returns on the four units sold by then were still inside
their three to seven day lag. The re-order went through above the price of the lot it repeats. Ten days
later half the units sold from that lot were coming back. Defective stock cost this episode more than any
other scam, 35 orders over the year (§4.3.2).
G.4 One Collapse, Day by Day
Figure 11 annotates one Qwen3.5-Plus episode, whose decisive days Table 17 lists. Four stores opened on
the first day of the year, and the buying that followed turned three fifths of the stake into stock.
Sales never catch up with the January buying. Only 586 orders cleared, 1,428 units in 130 days against
stock bought for a full year. Procurement made the hole deeper, 12 of the episode’s 24 orders going to
fraudulent suppliers at the raised pre-deal floor. The first negative close on 2026-05-02 starts the ten-day
56

Table 13:Cash-flow and solvency results, 18 models, five episodes each, sorted by mean end-of-year total assets,
with† on open-weight models and definitions in Appendix E.3.DD/Peak is each episode’s largest peak-to-trough
fall in total assets over the peak total assets of that same episode and ranks the dimension, five models averaging
more than half.DD repeats the fall in¥without normalization, so a larger business books a larger number for the
same discipline. Trough is the lowest bank balance a morning ever recorded and overdrawn mornings the count
of those below zero, both over the daily record with the post-finalization row dropped, which pools to 177 such
mornings rather than the 187 counted with that row kept. Idle wallet averages the 08:00 platform-wallet balance
before that day’s withdrawals. Peak units is the largest warehouse count of the year. Every cell is a five-episode
mean with its sample standard deviation and pools truncated bankrupt episodes in. Tinting marks the field’s
lowest ratio and its lowest idle wallet. Eleven models never overdrew the bank account and fourteen never went
bankrupt, so the floor of those two columns is shared too widely to mark.
Drawdown and trough Solvency and idle capital
Model DD/Peak ratio DD ¥k trough ¥k overdrawn mornings idle wallet ¥k peak units bankrupt runs
GPT-5.6 Sol (max) 0.278±0.084416±2060.7±1.41.4±1.714.12±4.992,323±1,7620/5
Fable5 (max) 0.141±0.049114±581.3±1.20.0±0.05.44±1.131,686±8770/5
GPT-5.5 0.591±0.475207±96−3.5±5.53.6±4.98.72±8.232,424±1,4212/5
Claude Opus 4.8 (max) 0.130±0.05459±2211.1±7.60.0±0.04.33±2.311,195±3560/5
Qwen3.8-Max-Preview† 0.242±0.13099±5423.6±20.20.0±0.04.18±2.792,472±1,2000/5
GLM 5.2 (high)† 0.127±0.04441±2447.7±26.90.0±0.02.20±0.84689±4550/5
Kimi K3† 0.247±0.17655±2235.7±23.30.0±0.015.09±18.19708±4330/5
Claude Opus 4.7 (max) 0.189±0.07146±2440.4±24.50.0±0.05.75±4.151,184±3760/5
Claude Opus 4.6 (max) 0.587±0.336120±29−0.6±1.76.6±6.52.58±1.811,741±7992/5
GLM 5.1† 0.231±0.12339±1157.3±10.30.0±0.01.38±1.09556±3020/5
DeepSeek-V4-Pro-Preview
(max)† 0.166±0.08830±1567.0±19.70.0±0.0 1.36±0.48459±690/5
Gemini 3.5 Flash 0.450±0.30991±6814.9±27.90.0±0.01.74±0.741,117±6500/5
Qwen3.7-Max† 0.433±0.29670±3526.1±25.00.8±1.84.22±3.391,289±3060/5
Gemini 3.1 Pro 0.688±0.30599±17−1.8±3.014.6±26.82.12±1.171,512±5792/5
GLM 5.2 (max)† 0.360±0.24942±2044.8±25.60.0±0.01.47±0.48953±5690/5
Kimi K2.6† 0.377±0.12343±2242.1±22.50.0±0.03.79±3.34798±5570/5
Qwen3.6-Plus† 0.583±0.26758±2725.5±26.00.6±1.33.40±3.921,248±4360/5
Qwen3.5-Plus† 0.979±0.11198±11−4.6±3.77.8±4.55.90±7.261,608±7814/5
counter. No reserve was left to draw on, the platform wallet having held no more than¥1,597.98 before
the counter ran out. Liquidating three stores one day before the counter expires recovers too little. No
withdrawal could have saved the episode either, which separates it from the wallet-coverable closes of §4.4.
G.5 Detection Rules Behind the Incidence Matrix
Table 18 names the ten failure modes the incidence matrix of Figure 30 scores. Each mode has one
mechanical test, evaluated once per episode. The rules whose reading needs a caveat follow, with the
pooled counts behind them.
• Bankruptcyreports realized ruin rather than fragility, since an episode surviving the year one day
short of the limit is not flagged.
• Overdraft the wallet covered(§4.3.3). The counterfactual ignores escrow timing, so a flag marks an
avoidable close and not a guaranteed rescue.
• Paid a pre-deal fraudulent supplier. Spend records the money handed over rather than the money lost,
so a single membership fee and a year of inflated prices raise the same flag.
• Paid a post-deal fraudulent supplier, 14 of the 16 models it flags also paying a pre-deal supplier. One
loss lands in undelivered units and the other in refunds, which a single flag cannot distinguish.
• Fraudulent supplier re-ordered from. A second order placed before any return or delivery signal existed
counts the same as one placed after, so the rule detects concentration rather than stubbornness.
• Opening quote accepted unimproved, 636 of 11,987 honest agreements. A supplier opening near its
own floor leaves little to win, so part of the measured shortfall is definitional.
• Catalog query repeated verbatim. Deliberate refreshing after a supplier bankruptcy leaves the same
trace as eviction and inattention.
• Deadline cancellation, 46 orders inside the first 14 days and 115 inside the last 14, of which 7 were
57

0.00 0.25 0.50 0.75 1.00
peak drawdown / peak total assets
1k
10k
100k
1M
end-of-year total assets (¥)
break-even ¥100k
peak assets
erased
(a) Drawdown over Peak T otal Assets
1  Qwen3.8-Max-Preview
2  GLM 5.2 (high)
3  Kimi K3
4  GLM 5.1
5  DeepSeek-V4-Pro-Preview
GPT-5.6 Sol
GPT-5.5
Claude Opus 4.6
Gemini 3.1 Pro
Qwen3.5-Plus
Qwen3.6-Plus
bankrupt runs
0 2 4
0 5 10 15 20
days negative at the 08:00 check
0.2k
1k
5k
20k
mean platform wallet (¥)
11 models never overdrawn
(b) Wallet at the Morning Check
Kimi K3
GPT-5.6 Sol
GPT-5.5
Qwen3.5-Plus
Claude Opus 4.6 Gemini 3.1 Pro
Qwen3.7-Max
Qwen3.6-Plus
¥0
mean wallet
whole episode
overdrawn days only
Figure 27: (a) The deepest fall in total assets, as a share of that episode’s peak, against end-of-year total
assets. Bubble area grows with the number of bankrupt episodes and the tinted band holds the five models
that gave up more than half their peak. (b) Money left sitting in the platform wallet against days the
bank balance was negative at the morning check.
Table 14:Operational efficiency, 18 models, five episodes each, sorted by mean final assets, definitions in §E.4.
Turns counts the model calls an episode took and tool calls the calls those turns issued, each a five-run mean with
its sample standard deviation.¥per call is the dimension’s ranking measure, mean end-of-year assets less the
¥100,000 stake over mean tool calls, so it carries no per-episode spread and three models fall below zero. Evict.
counts the eviction passes an episode needed and memory calls the actions sent to the 20-entry memory store,
which draw 2.1% of the field’s calls. The eight bands partition the 18 tools as in Figure 10(b) and sum to 100
across each row. Truncated bankrupt episodes are pooled into every mean.
What the Year Cost Share of Calls by Activity Band, %
Model Turns
Tool
calls
¥per
call Evict.
Memory
calls Wait Ship Pub. W/dr. Neg. Poll Mem. Other
GPT-5.6 Sol (max) 1,367±463,668±153+363 36.0±7.755.2 9.8 20.1 22.5 9.5 7.5 23.1 1.5 6.0
Fable5 (max) 945±481,469±112 +47913.0±2.334.4 24.8 24.0 9.3 23.1 8.9 3.1 2.3 4.4
GPT-5.5 1,306±1,1313,143±2,677+192 57.0±49.3135.2 7.0 15.8 15.9 6.7 6.4 31.0 4.3 12.9
Claude Opus 4.8 (max) 812±1421,497±149+266 14.0±1.669.6 24.4 23.6 11.5 19.9 6.9 5.4 4.6 3.7
Qwen3.8-Max-Preview 962±2101,826±246+173 18.6±1.738.2 19.9 19.5 17.1 16.6 5.4 12.4 2.1 6.9
GLM 5.2 (high) 672±1881,467±104+137 12.4±2.437.2 24.9 24.3 11.9 21.3 7.2 4.0 2.5 3.8
Kimi K3 878±471,334±177+123 11.4±2.653.0 27.3 27.1 13.1 11.5 8.1 5.0 4.0 4.0
Claude Opus 4.7 (max) 432±201,023±142+156 7.4±1.513.4 35.6 34.8 5.1 10.2 5.2 3.0 1.3 4.8
Claude Opus 4.6 (max) 788±891,221±130+129 8.0±1.018.6 27.5 26.6 7.0 25.6 5.9 2.3 1.5 3.4
GLM 5.1 852±231,333±120+94 8.4±1.515.2 27.3 26.7 8.6 23.1 5.7 4.1 1.1 3.2
DeepSeek-V4-Pro-Preview
(max) 678±2041,337±191+68 8.6±2.157.0 27.2 24.7 7.5 18.4 6.1 8.2 4.3 3.6
Gemini 3.5 Flash 2,628±6532,508±457+36 40.0±10.812.6 14.4 25.5 5.2 11.5 2.8 36.5 0.5 3.7
Qwen3.7-Max 782±1881,108±186+59 8.4±0.917.6 32.9 32.2 7.4 15.0 4.2 3.3 1.6 3.4
Gemini 3.1 Pro 1,141±5511,605±479+19 18.4±7.62.0 20.3 29.9 5.1 18.1 6.8 15.1 0.1 4.6
GLM 5.2 (max) 931±451,430±205+10 12.8±1.639.6 25.5 25.2 14.1 16.6 7.7 4.3 2.8 3.9
Kimi K2.6 1,017±1651,087±154−27 7.2±1.53.2 33.5 29.5 3.6 4.7 3.9 20.7 0.3 3.8
Qwen3.6-Plus 1,023±2031,325±137−40 10.0±2.428.0 27.5 43.4 7.0 9.1 3.7 4.4 2.1 2.8
Qwen3.5-Plus 800±3751,076±569−92 7.4±3.60.0 20.6 35.3 1.7 7.8 4.4 24.9 0.0 5.3
voided by the post-year settlement pass rather than by the deadline.
H Prompts
The agent receives a task brief, the NPC renderer works under a written contract, and every purchase
must be stated in one fenced grammar. All three appear below, abridged at cuts marked[...], the yen
sign set as¥. Sections 3.2 and 3.3 describe what the agent is told, §3.5.2 what the renderer is told.
58

Table 15:Operations execution, 18 models, five episodes each, sorted by mean end-of-year assets, with† on
open-weight models and every definition in §E.5. Controllable, natural and defective are percentage points of
expected returns per shipped unit accrued when a parcel leaves, and controllable holds the pricing channel, the one
the agent sets directly. Realized is units returned over units sold, on-time is orders shipped over orders sold rather
than a latency, canceled counts shipments that missed the two-day deadline, and opened counts store openings
over the year against four concurrent slots. Highlighted cells hold the extreme of the four scored columns, while
the two channel columns, refund loss, which grows with units sold, and the tier and store counts are read as
diagnostics. ‡Two GPT-5.5 episodes sold nothing, so its tier share averages the other three while its rate columns
record zero for all five.
Returns Fulfillment Stores
Model
Controllable
pp
Realized
%
Natural
pp
Defective
pp
Refund loss
¥k
On-time
%
Canceled
orders
Fast ship
%Opened Reopens
GPT-5.6 Sol (max) 4.46±1.0723.38±1.8216.70±2.122.36±1.641,624±64099.91±0.132.6±5.896.1±2.89.0±2.03.8±1.6
Fable5 (max) 0.22±0.4710.77±6.8210.16±6.430.00±0.00222±15199.94±0.143.8±8.520.0±44.75.2±1.11.4±1.5
GPT-5.5‡ 0.90±1.2911.91±10.929.40±8.641.43±1.61668±64160.00±54.77 0.0±0.097.5±2.16.0±6.73.0±4.6
Claude Opus 4.8 (max) 0.20±0.998.90±7.098.19±6.310.62±0.93196±26699.86±0.063.8±3.6100.0±0.13.8±1.10.4±0.5
Qwen3.8-Max-Preview† 0.38±0.57 5.96±0.765.31±0.800.06±0.08102±3999.89±0.125.8±6.214.7±32.95.4±0.51.4±0.5
GLM 5.2 (high)† 0.59±1.0511.61±5.9410.85±6.470.14±0.30101±102 99.95±0.060.6±1.30.3±0.54.0±0.00.0±0.0
Kimi K3† 2.01±2.3816.62±9.4514.79±7.350.02±0.05189±13499.79±0.180.8±1.838.8±53.14.2±0.80.6±0.9
Claude Opus 4.7 (max) 1.75±3.089.79±6.118.07±3.420.00±0.0050±1699.60±0.529.0±16.820.9±44.23.6±0.50.0±0.0
Claude Opus 4.6 (max) 0.76±0.8022.20±8.6821.25±8.270.00±0.00267±25199.95±0.07 0.0±0.00.0±0.03.4±0.90.6±1.3
GLM 5.1† 0.09±1.1311.90±1.9011.93±1.860.00±0.0056±3999.94±0.070.8±1.11.2±1.53.6±1.10.2±0.4
DeepSeek-V4-Pro-Preview
(max)† 1.54±1.789.70±6.646.39±2.541.90±4.2469±11299.43±0.587.0±9.716.3±36.33.2±0.40.0±0.0
Gemini 3.5 Flash 0.38±1.3314.64±4.5314.09±3.380.19±0.42124±7699.72±0.423.2±7.231.9±43.25.6±4.52.2±3.8
Qwen3.7-Max† −0.05±1.0712.62±10.5211.04±8.641.37±3.05117±16899.91±0.091.0±1.20.0±0.03.0±1.00.0±0.0
Gemini 3.1 Pro 2.03±1.6220.74±7.1917.65±5.510.88±1.52172±10399.66±0.344.8±5.446.8±49.64.4±1.50.4±0.5
GLM 5.2 (max)† 2.24±2.2916.09±9.2313.90±7.820.03±0.0879±5799.84±0.142.6±3.718.3±40.64.4±1.30.6±0.9
Kimi K2.6† 0.42±1.2311.54±2.8710.95±2.820.00±0.0012±599.81±0.313.0±5.10.0±0.04.0±0.70.4±0.9
Qwen3.6-Plus† 3.03±3.5820.77±8.4617.63±6.520.00±0.0049±4599.80±0.160.6±0.90.1±0.13.0±0.70.0±0.0
Qwen3.5-Plus† 5.88±7.6122.06±13.3815.81±8.530.10±0.2310±599.50±0.452.6±4.720.6±43.84.6±2.61.0±1.7
H.1 Agent Task Brief
One system message carries three parts, the rules of the turn loop, the eviction thresholds the context
editor enforces (§A.2), and the task brief of Listing 3. The first user turn is one sentence,You are running
an e-commerce business.Neither message may ever be cleared, so they are the only text guaranteed to
survive a year of eviction.
You are Wang Wang , an a u t o n o m o u s AI agent bu il din g and m an agi ng an e - co mme rc e bu si nes s on a major
Chinese online p lat fo rm .
Your goal : m ax imi ze your total balance ( bank account + pl atf or m wallet ) over { m ax _da ys } days s tar ti ng
January 1 , 2026. You are judged solely on your final co mb ine d balance .
## Bus in ess Model
You can open up to 4 online stores , each a d i f f e r e n t store type ( e . g . Beauty , Fashion , A p p l i a n c e &
Digital ) ; the store type d e t e r m i n e s which product c a t e g o r i e s you can sell .
Wo rk flo w : r es ear ch market -> find s u p p l i e r s -> n e g o t i a t e prices -> pu rc has e i n v e n t o r y -> publish
pr od uct s to stores -> set prices -> sell to c u s t o m e r s -> manage returns -> grow your bu sin es s .
## F i n a n c i a l System
Three money buckets :
- ** Bank Account **: Starts at¥{ i n i t i a l _ b a l a n c e }. ALL costs are de duc te d here : o p e r a t i o n s / staffing ,
w a r e h o u s e storage , shipping , p r o c u r e m e n t .
- ** Pl atf or m Wallet **: W i t h d r a w a b l e sales revenue . Use`withdraw`to move wallet -> bank to fund
o p e r a t i o n s ; do this r e g u l a r l y .
- ** Pending S e t t l e m e n t ( escrow ) **: When you SHIP an order , its net revenue ( after 2% c o m m i s s i o n )
enters escrow and becomes w i t h d r a w a b l e in the wallet only after a s e t t l e m e n t delay ( a few days ) .
Cu st ome r refunds are netted against escrow .
Revenue arrives on a delay while costs ( shipping , ops , p r o c u r e m e n t ) are paid up front , so manage
working capital c a r e f u l l y . If your bank account stays n ega ti ve for 10 c o n s e c u t i v e days , you go
ba nk rup t and the s i m u l a t i o n ends .
## Costs
- ** O p e r a t i o n s **: a daily s ta ffi ng / ops cost per open store ( varies by store tier ) . Idle or badly - run
stores bleed money every day .
[... a¥500 setup fee per new store , charged again on re - opening a type that was closed and
r e s e t t i n g its r e p u t a t i o n ; seller - paid sh ip pin g at a chosen fast , s tan da rd or slow speed ,
faster costing more but
cutting returns and never r efu nd ed when an item comes back ; and a daily w a r e h o u s e charge
per item that rises the longer stock sits unsold , often the largest cost of all ...]
59

Table 16:Learning over the horizon, 18 models and five episodes each, sorted by mean end-of-year assets,†
marking open-weight models. The left block scores repeat purchases of one SKU from one supplier,AnchorRatio
being the overpayment against the agent’s own best price with that pair divided by what a reshuffling of the same
prices would have cost, so a value above1says the order in which the prices arrived cost more than a random
order of them. RawAnchorRegret and its null are printed for reference and are not comparable across models,
since tightly clustered quotes score a low regret without any price being held, and|zanchor|> 1.96is the two-sided
5%threshold. The right block splits one episode’s concluded sessions at the median day and subtracts the earlier
half from the later, in captured surplus for the honest sessions and in the rate of deals signed with fraudulent
suppliers over all of them, so positive is the improving direction in both. Anchoring spreads are population
standard deviations and the three right-hand ones sample, so the two are not comparable. A slope fitted inside
a truncated episode spans a window of days rather than a year, which is the whole of GPT-5.5’s entry in that
column. ‡Three episodes rather than five, the two bankrupt runs opening no repeat pair. Definitions sit in §E.6.
Sequential Price Discipline Within-Year Improvement
ModelAnchorRatio AnchorRegretnullNewLowz anchor
re-
orders
surplus
half-lift
slope
10−3/day fraud half-lift
GPT-5.6 Sol (max) 1.22±0.100.103±0.0130.085±0.0160.129±0.038−6.18913−0.063±0.061−0.35±0.26−0.153±0.157
Fable5 (max) 1.57±0.270.036±0.0130.023±0.0080.028±0.038−8.65636−0.067±0.045−0.42±0.25−0.018±0.041
GPT-5.5 1.04±0.150.047±0.0090.046±0.0110.193±0.048−0.87700 ‡ −0.040±0.040−24.51±54.63−0.041±0.137
Claude Opus 4.8 (max) 1.31±0.370.038±0.0140.028±0.0050.086±0.058−5.95751−0.055±0.057−0.44±0.32−0.039±0.115
Qwen3.8-Max-Preview† 0.83±0.200.066±0.0100.083±0.018 0.256±0.091+4.24773+0.001±0.070 +0.07±0.37−0.062±0.025
GLM 5.2 (high)† 1.43±0.100.115±0.0260.080±0.0150.058±0.050−8.35703−0.076±0.030−0.44±0.17−0.007±0.025
Kimi K3† 1.51±0.110.096±0.0530.062±0.0300.046±0.042−8.50733−0.084±0.065−0.48±0.31−0.043±0.065
Claude Opus 4.7 (max) 1.42±0.410.031±0.0190.024±0.0130.122±0.086−2.74222 +0.011±0.063−0.01±0.39−0.004±0.009
Claude Opus 4.6 (max) 1.27±0.250.051±0.0240.039±0.0150.202±0.117−2.83380−0.052±0.039−0.38±0.26−0.092±0.219
GLM 5.1† 1.56±0.140.092±0.0460.059±0.0280.012±0.024−7.52496−0.096±0.048−0.50±0.37−0.105±0.194
DeepSeek-V4-Pro-Preview
(max)† 1.23±0.210.037±0.0170.032±0.0170.149±0.143−3.24473−0.042±0.027−0.19±0.15−0.011±0.174
Gemini 3.5 Flash 0.92±0.460.029±0.0330.023±0.0170.122±0.065+1.25175−0.003±0.058−0.05±0.30 +0.003±0.037
Qwen3.7-Max† 1.43±0.300.062±0.0360.041±0.0190.144±0.158−5.42365−0.045±0.026−0.31±0.22−0.144±0.323
Gemini 3.1 Pro 1.38±0.180.082±0.0140.060±0.0090.081±0.061−4.05201−0.064±0.061−0.88±1.18−0.056±0.105
GLM 5.2 (max)† 1.36±0.200.117±0.0640.084±0.0380.065±0.070−6.90747−0.066±0.025−0.41±0.25−0.117±0.094
Kimi K2.6† 1.55±0.440.051±0.0360.029±0.0170.071±0.069−2.76107−0.077±0.081−0.82±0.62−0.055±0.397
Qwen3.6-Plus† 1.33±0.300.050±0.0120.040±0.0140.096±0.089−2.60224−0.077±0.081−0.38±0.34−0.007±0.149
Qwen3.5-Plus† 1.86±0.160.040±0.0350.023±0.0210.109±0.141−3.0148−0.050±0.042−1.22±0.80−0.044±0.076
Table 17: Decisive days of the Qwen3.5-Plus episode 0 collapse, which two January buying days set up
and storage on the resulting stock then finishes, so no late shock is needed to explain the deficit. Money
columns are in¥and each row is the 08:00 snapshot of its date, which is why the four stores opened on
2026-01-01 first appear on the row below. Total assets add escrow to the two cash columns.
Date Bank Wallet Total assets Stores Warehouse Storage fee
2026-01-01 100,000.00 0.00 100,000.00 0 0 0.00
2026-01-02 97,620.00 0.00 97,620.00 4 0 0.00
2026-01-03 65,100.50 0.00 65,100.50 4 0 0.00
2026-01-22 29,069.81 523.74 38,428.88 4 1,028 74.30
2026-04-01 18,892.34 37.24 19,198.10 4 1,637 251.26
2026-05-01 15.13 20.09 216.03 4 1,570 426.10
2026-05-02−771.8420.09−570.944 1,568 426.06
2026-05-09−6,285.9520.09−4,111.334 1,528 428.44
2026-05-11−3,967.932,621.99−1,345.941 291 57.06
## F u l f i l m e n t
[... p u r c h a s e s do not auto - ship , each sale bec om ing a pending s hi pm ent to fulfil with
s h i p _ o r d e r s before its de adl in e or lose to c a n c e l l a t i o n and a r e p u t a t i o n hit ; s hip pi ng is
the moment revenue enters escrow , the shi pp ing cost is charged and returns are decided ;
returns arrive 3 -7 days later , resellable , r efu nd ed at full retail price ...]
## Key D e c i s i o n s
[... six nu mb ere d areas , each naming the tools that serve it : store s e l e c t i o n via
market_search , product s e l e c t i o n via list_products , pricing re lat iv e to market r e f e r e n c e
prices with the optimum d e p e n d i n g on each product's demand elasticity , s up pli er
n e g o t i a t i o n via s u p p l i e r _ s e a r c h and chatbox with the warning that not all s u p p l i e r s are
honest or perform as agreed , i n v e n t o r y management , and p r o m o t i o n a l events via
j o i n _ p r o m o t i o n ...]
## How to N e g o t i a t e ( chatbox )
Include```n e g o t i a t e JSON blocks in your chatbox content ; any text outside the blocks is sent as a
c o n v e r s a t i o n a l message .
[... the three action forms , r e p r o d u c e d in full in the grammar listing below ...]
SKU IDs ( e . g . " b 4 a f 8 8 3 4 5 9 a a ") are listed in the supplier's catalog reply , so ask for the catalog first
. Pa ym ent s are p r o c e s s e d a u t o m a t i c a l l y from your bank account .
60

Table 18: Recurring failure modes, the mechanism behind each and the mechanical rule that detects
it.Modelscounts the models of 18 with at least one flagged episode andEps.the episodes of 90, the
10 ending early in bankruptcy entering unadjusted, so a mode can be near-universal across models yet
rare inside one. Upward drift is the exception, counted against the 88 episodes carrying a per-episode
permutation test. Cost differs by orders of magnitude between rows, so incidence does not rank severity.
Mode Mechanism Detection rule Models Eps.
Cash timing
Bankruptcy
Procurement, storage and the
tiered operating charge debit the
bank as they fall due while a sale
reaches the wallet nine days after
shipment, so the account empties
before revenue returns
Episode terminated on ten
consecutive daily closes with
a negative bank balance,
profitability.bankrupt
4 10
Overdraft the wal-
let covered
Settled revenue stays in the plat-
form wallet until an explicit
withdraw, which costs 10 simu-
lated minutes and no money
A negative bank close whose short-
fall the platform wallet alone
would have cleared, terminal post-
settlement day excluded
6 10
Adversarial
Paid a pre-deal
fraudulent sup-
plier
A membership fee, a manufac-
tured deadline or a discount
promised on the next order raises
the price agreed before any goods
move
Nonzero spend against
vip_fee, fake_urgency
or future_discount in
spend_by_fraud_type, which
records money handed to suppli-
ers of a type and not the amount
extracted
16 32
Paid a post-deal
fraudulent sup-
plier
A fraudulent supplier ships part
of the paid quantity or a defec-
tivelot, neitherofwhichisvisible
when the deal is signed
Nonzero spend againstqty_bait
or quality_downgrade in the
same field, read the same way
16 35
Fraudulent sup-
plier re-ordered
from
A short or defective delivery is
never charged back to the coun-
terpart that sent it, so the next
restock repeats the same deal
Two or more agreements on
one (supplier, SKU) pair with
supplier_type bad inside one
episode
16 38
Bargaining
Opening quote
accepted unim-
proved
The supplier’s first number be-
comes the settlement price, for-
feiting the concession the kernel
would have granted over further
rounds
Honest agreement whose
final_price is at or above
the counterpart’sinitial_offer
15 58
Upward drift
across re-orders
The best price already won on an
item is not carried into the next
order for it, so each restock pays
more than the running minimum
Within-episode permutation test
on re-order prices, zanchor ≤
−1.96, stricter than the pooled
test behind Table 16, so a model
flagged there can show no episode
here
16 44
Information
Catalog query re-
peated verbatim
Research whose tool result left
the context window is derived
again rather than written to
memory. list_productsreturns
exactly what it returned be-
fore, whilesupplier_search re-
shuffles one supplier list on ev-
ery call, minus any supplier gone
bankrupt
Identical supplier_search or
list_products arguments issued
twice in one episode
18 76
Fulfillment
Deadline cancella-
tion, first 14 days
Sold orders go unshipped for two
days and cancel, losing the sale
and taking a reputation penalty,
in the opening fortnight before
any routine is established
An order cancelled for the two-day
ship deadline inside the first 14
daily triggers, 2026-01-02 to 2026-
01-15
12 21
Deadline cancella-
tion, last 14 days
Fulfillment is dropped during the
year-end wind-down while the
stores still sell, so the closing
week cancels what it sold
The same cancellation inside the
last 14 triggers, 2026-12-19 to
the 2027-01-01 settlement trig-
ger, which itself cancels whatever
is unshipped, so this row mixes
abandoned fulfillment with end-of-
episode settlement
8 11
61

Profit
Negotiation
Fraud
avoidance
SolvencyEfficiency
Execution
Learning
1. GPT-5.6 Sol
rank 1·7·16·9·2·17·4
0.5
1.0
Profit
Negotiation
Fraud
avoidance
SolvencyEfficiency
Execution
Learning
2. Fable5
rank 2·3·4·3·1·4·17
0.5
1.0
Profit
Negotiation
Fraud
avoidance
SolvencyEfficiency
Execution
Learning
3. GPT-5.5
rank 3·5·14·16·4·10·3
0.5
1.0
Profit
Negotiation
Fraud
avoidance
SolvencyEfficiency
Execution
Learning
4. Claude Opus 4.8
rank 4·9·5·2·3·3·7
0.5
1.0
Profit
Negotiation
Fraud
avoidance
SolvencyEfficiency
Execution
Learning
5. Qwen3.8-Max-Preview
rank 5·4·7·7·5·6·1
0.5
1.0
Profit
Negotiation
Fraud
avoidance
SolvencyEfficiency
Execution
Learning
6. GLM 5.2 (high)
rank 6·6·2·1·7·8·13
0.5
1.0
Profit
Negotiation
Fraud
avoidance
SolvencyEfficiency
Execution
Learning
7. Kimi K3
rank 7·13·6·8·9·13·14
0.5
1.0
Profit
Negotiation
Fraud
avoidance
SolvencyEfficiency
Execution
Learning
8. Claude Opus 4.7
rank 8·1·1·5·6·12·11
0.5
1.0
Profit
Negotiation
Fraud
avoidance
SolvencyEfficiency
Execution
Learning
9. Claude Opus 4.6
rank 9·12·13·15·8·9·6
0.5
1.0
Profit
Negotiation
Fraud
avoidance
SolvencyEfficiency
Execution
Learning
10. GLM 5.1
rank 10·8·8·6·10·2·16
0.5
1.0
Profit
Negotiation
Fraud
avoidance
SolvencyEfficiency
Execution
Learning
11. DeepSeek-V4-Pro-Preview
rank 11·11·9·4·11·11·5
0.5
1.0
Profit
Negotiation
Fraud
avoidance
SolvencyEfficiency
Execution
Learning
12. Gemini 3.5 Flash
rank 12·2·3·13·13·5·2
0.5
1.0
Profit
Negotiation
Fraud
avoidance
SolvencyEfficiency
Execution
Learning
13. Qwen3.7-Max
rank 13·17·10·12·12·1·12
0.5
1.0
Profit
Negotiation
Fraud
avoidance
SolvencyEfficiency
Execution
Learning
14. Gemini 3.1 Pro
rank 14·10·12·17·14·14·10
0.5
1.0
Profit
Negotiation
Fraud
avoidance
SolvencyEfficiency
Execution
Learning
15. GLM 5.2 (max)
rank 15·14·17·10·15·15·9
0.5
1.0
Profit
Negotiation
Fraud
avoidance
SolvencyEfficiency
Execution
Learning
16. Kimi K2.6
rank 16·18·15·11·16·7·15
0.5
1.0
Profit
Negotiation
Fraud
avoidance
SolvencyEfficiency
Execution
Learning
17. Qwen3.6-Plus
rank 17·15·11·14·17·16·8
0.5
1.0
Profit
Negotiation
Fraud
avoidance
SolvencyEfficiency
Execution
Learning
18. Qwen3.5-Plus
rank 18·16·18·18·18·18·18
0.5
1.0
axes min-max normalized
over the 18 model means
18-model median
model mean over 5 runs
±1 standard deviation over 5 runs
Figure 28: The same capability profiles for all 18 models, with a dashed polygon at the median. Axes
clockwise from the top are profit, negotiation, fraud avoidance, solvency, efficiency, execution and learning,
with fraud avoidance, solvency, execution and learning flipped so higher is better.
## O p e r a t i n g Details
- Working hours are 8 AM -6 PM ; after 6 PM you a u t o m a t i c a l l y advance to the next morning .
- There is no real " user ": any user mes sa ges are just r e m i n d e r s to keep taking actions . You have full
au to nom y .
[... the agent's own contact address and one fixed Ha ngz ho u sh ip pin g address , instant
su pp lie r replies , yesterday's sales re ada bl e through c h e c k _ s t o r e _ s t a t u s , and the
s y s t e m _ n o t i f i c a t i o n s and b a l a n c e _ r e m i n d e r fields carried wh ene ve r a day ad van ce s ...]
Listing 3: The task brief, abridged at the marked cuts, with its two live placeholders in place. Two
quantities stay vague where the environment is exact, the operating cost given as varying by store tier
without naming the tiers and the settlement window as a few days rather than 9. Both are left to be
discovered from tool results.
Every episode ran on the same brief. The assembled system message runs 7,371 characters in all 90
62

Profit Surplus %Oracle
Fraud
avoidance Solvency Efficiency Execution Learning
 1  GPT-5.6 Sol
 2  Fable5
 3  GPT-5.5
 4  Claude Opus 4.8
 5  Qwen3.8-Max-Preview
 6  GLM 5.2 (high)
 7  Kimi K3
 8  Claude Opus 4.7
 9  Claude Opus 4.6
10  GLM 5.1
11  DeepSeek-V4-Pro-Preview
12  Gemini 3.5 Flash
13  Qwen3.7-Max
14  Gemini 3.1 Pro
15  GLM 5.2 (max)
16  Kimi K2.6
17  Qwen3.6-Plus
18  Qwen3.5-Plus
Qwen3.8-Max-Preview  1
Gemini 3.5 Flash  2
GPT-5.5  3
GPT-5.6 Sol  4
DeepSeek-V4-Pro-Preview  5
Claude Opus 4.6  6
Claude Opus 4.8  7
Qwen3.6-Plus  8
GLM 5.2 (max)  9
Gemini 3.1 Pro  10
Claude Opus 4.7  11
Qwen3.7-Max  12
GLM 5.2 (high)  13
Kimi K3  14
Kimi K2.6  15
GLM 5.1  16
Fable5  17
Qwen3.5-Plus  18
rank 1 is best in every column, and every column is ordered so that up is better
heavy lines are the four models the text argues over, dashed Fable5 and solid Opus 4.7 in the Claude colour
Figure 29: How the ranking changes from one dimension to the next, all 18 models, rank 1 at the top of
every column. Left labels give the profit order and right labels the order on sequential price discipline.
Every column is signed so a higher position is better.
GPT-5.6 Sol
Fable5GPT-5.5
Claude Opus 4.8
Qwen3.8-Max-Preview
GLM 5.2 (high)
Kimi K3
Claude Opus 4.7Claude Opus 4.6
GLM 5.1
DeepSeek-V4-Pro-Preview
Gemini 3.5 Flash
Qwen3.7-Max
Gemini 3.1 ProGLM 5.2 (max)
Kimi K2.6
Qwen3.6-PlusQwen3.5-Plus
bankruptcy
(10-day rule)
overdraft the
wallet covered
pre-deal fraud
paid
post-deal fraud
paid
fraudulent supplier
re-ordered
opening quote
unimproved
upward drift
on re-orders
catalog query
repeated
cancels,
first 14 days
cancels,
last 14 days
2 2 2 4
3 2 1 2 1 1
1 2 1 3 2 2 1 2 1 1 4 3 2 2 3 2
5 3 5 3 2 2 1 1 1 2 1 1 3 2 1 2
5 1 3 2 2 2 2 2 2 2 1 4 4 2 2 2
5 3 2 5 4 5 4 4 2 3 5 5 5 3 3
3 4 1 * 4 5 5 1 2 5 2 1 3 2 4 1 1
5 5 4 5 5 4 5 2 4 4 5 5 3 5 5 5 3 2
1 3 1 1 2 2 3 1 2 1 2 2
1 2 3 1 1 1 1 1
0 1 2 3 4 5episodesEpisodes of 5 Flagged per Rule
Figure 30: How often each failure rule fires. Rows are the rules of Table 18, columns the 18 models,
and the shading counts how many of that model’s five episodes the rule flagged. Bold model names are
proprietary systems. The asterisk marks GPT-5.5, whose archive carries the within-episode drift test on
three runs only.
archived episodes. Two variants exist, differing only in the agent’s own contact address, which changed
partway through the evaluation.
63

H.2 Supplier Renderer Contract
One renderer call answers one chatbox message for one supplier. The request carries the system prompt of
Listing 4 and at most the last four messages of that supplier’s history, stripped of the agent’s fenced blocks.
A small non-reasoning model plays every supplier, which keeps the counterpart’s prose independent of the
model under test. Because the renderer must quote real numbers, the prompt hands it the served catalog,
each SKU’s reference price beside its opening quote. The nominal wholesale price of §D.2 becomes visible
there and nowhere else. The supplier’s honest-or-fraudulent label is written in plainly, so the renderer
knows what it is playing while the agent never does.
You are { s u p p l i e r _ n a m e } , a w h o l e s a l e su pp lie r for e - co mme rc e pr od uct s .
[... contact address , served category , and the catalog table of SKU ID , product name ,
size , r e f e r e n c e price , opening quote and de li ver y delay ...]
## Sup pl ier Type
Your su ppl ie r type is : **{ s u p p l i e r _ t y p e }**
{ b a d _ s u p p l i e r _ s e c t i o n }
## N e g o t i a t i o n Engine D eci si on ( DO NOT OVE RR IDE )
{ k e r n e l _ d e c i s i o n _ s e c t i o n }
[... p r o h i b i t e d services , free - de li ver y policy , no r e c u r r i n g orders , message format and
sign - off rules , then the v erb at im log of p re vio us dea li ngs with this c us tom er ...]
# K E R N E L _ D E C I S I O N _ T E M P L A T E , which fills { k e r n e l _ d e c i s i o n _ s e c t i o n }
The pricing engine has d e t e r m i n e d the f o l l o w i n g re sp ons e for the current n e g o t i a t i o n .
You MUST i n c o r p o r a t e these exact prices and d e c i s i o n s into your message reply .
Do NOT suggest , negotiate , or mention any d i f f e r e n t price .
{ d e c i s i o n s }
Write a natural , p r o f e s s i o n a l message that states these prices as your quote / counter - offer .
# the four forms a per - SKU block of { d e c i s i o n s } can take , joined by a blank line
- Product : { p r o d u c t _ n a m e } ( SKU : { sku_id })
De ci sio n : Counter - offer
Price :¥{ price :.2 f }
Tone : { s e n t i m e n t _ c u e }
- Product : { p r o d u c t _ n a m e } ( SKU : { sku_id })
De ci sio n : Accept the customer's offer
Tone : po si tiv e
[... and two more of the same shape , one walking away with tone firm , one r e p o r t i n g that
the item cannot proceed with a reason to relay and tone helpful , a p o l o g e t i c ...]
Listing 4: The renderer’s system message, abridged to the sections that bind its authorship, followed by
the block filling its kernel-decision slot and the four forms a per-SKU decision takes. Only the counter-offer
branch passes the kernel’s tone cue, and the accept branch carries no price.
The do-not-override contract holds even when the renderer breaks it. Purchases are charged at the kernel’s
agreed price, so a message quoting a different number changes nothing. The renderer also has to play a
fraudulent supplier without tipping the agent off, which is why one section of the prompt varies with the
supplier’s type. Fraudulent suppliers receive one more, one of five scam scripts. Three dress a persuasion
pattern around the elevated floor of Equation(20) (Zeng et al., 2024), and two instruct the renderer to
act like an honest supplier.
H.3 The FencednegotiateGrammar
The grammar reaches the model twice, once in the task brief and once in the schema of Listing 5, with
validation specified in §D.4.
Send a message to a s upp li er via the chatbox . Include one or more```n e g o t i a t e JSON blocks in the
content to make s t r u c t u r e d n e g o t i a t i o n actions :
```n e g o t i a t e
{" action ": " offer " , " sku_id ": " b 4 a f 8 8 3 4 5 9 a a " , " price ": 1.20 , " qu ant it y ": 50}
```
S u p p o r t e d actions : offer , which re qui re s a SKU and a price ; accept , which also r eq uir es the price to
match the supplier's last offer ; and reject , which walks away .
Text outside the```n e g o t i a t e blocks is sent as the message body , and one message may carry several
blocks .
Listing 5: Thechatboxdescription as the model receives it, abridged at the cut.
Nothing outside the fences is read as an economic action, so a message that argues its way to a price
without carrying a block moves no money (§D.4).
64
