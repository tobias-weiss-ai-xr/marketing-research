---
title: 'Governed Self-Evolution for Autonomous Investing: A Multi-Agent LLM System with an Invariant Core'
url: https://arxiv.org/abs/2610.30557
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Yebo Feng
- Jingyang Dai
- Liangrui Pan
- Nelson Lau
- Jiahua Xu
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.30557
pages: 13
chars: 73074
fetched_at: '2026-11-08T13:31:14+00:00'
kb_version: 1
---

# Governed Self-Evolution for Autonomous Investing: A Multi-Agent LLM System with an Invariant Core

Governed Self-Evolution for Autonomous Investing:
A Multi-Agent LLM System with an Invariant Core
Yebo Feng
Nanyang Technological University
Singapore, Singapore
yebo.feng@ntu.edu.sg
Jingyang Dai
Nanyang Technological University
Singapore, Singapore
jingyang.dai@ntu.edu.sg
Liangrui Pan
Nanyang Technological University
Singapore, Singapore
liangrui.pan@ntu.edu.sg
Nelson Lau
Nanyang Technological University
Singapore, Singapore
nelson.lauls@ntu.edu.sg
Jiahua Xu
University College London
London, United Kingdom
jiahua.xu@ucl.ac.uk
Yang Liu
Nanyang Technological University
Singapore, Singapore
yangliu@ntu.edu.sg
Abstract
LLM agents that act on live Web data must combine heteroge-
neous evidence, remember what they have done and improve from
outcomes without weakening their own safeguards. We study this
problem in autonomous investing, where every action is irreversible
and based on untrusted Web content. We presentSteward, a multi-
agent LLM system that draws the boundary of self-evolution in
its type system. First, nine role-specialised agents decide jointly:
four analysts read news feeds, SEC filings, macroeconomic series
and market data and emit typed reports, from which a Portfolio
Manager sets target positions that a protected Risk Manager audits.
Second, a seven-layer shared memory, assembled by code from
the system’s own record, gives each decision its position context,
the market narrative, calibration and the agent’s past decisions.
Third, the system improves itself by review: code grades every
trade and forecast nightly and writes the grades into memory, and
each quarter a reflector proposes prompt learnings that a determin-
istic gate applies reversibly and replay of recorded inputs verifies.
All three operate around aninvariant coreof order arithmetic, risk
rules and discipline-agent prompts that no self-edit can reach. In
a five-month live deployment (102 trading days, 1,632 LLM calls),
the system contained a 24.6% sector drawdown to a 0.3% loss; in re-
play of its recorded inputs, a single model given the same raw data
traded more and lost1 .35points against the market over five days
where the joint design showed no significant loss, and no injected
instruction was followed; and a 2015–2026 backtest shows the core
alone lowering the maximum drawdown under all 50 random entry
policies. The reflector traced the dominant failure to its root cause,
and the gate applied a learning that the agent adopted on trigger
evenings and on no control evening. The code and prompts of the
deployed system are open source.
CCS Concepts
•Computing methodologies → Multi-agent planning;Intel-
ligent agents;•Information systems → Web applications;•
Applied computing→Economics.
Keywords
LLM multi-agent systems, shared memory, self-evolving agents,
autonomous investing, agentic Web, guardrails, field study
1 Introduction
LLM agents increasingly act on the Web rather than only answer
from it [38]. An agent that makes consequential decisions from
Web content must do three things at once: combine heterogeneous,
individually weak evidence into one decision; remember what it
has decided and how those decisions turned out; and improve from
experience [1, 7, 20, 25, 27] without weakening the rules that con-
strain it. The third is the hardest to make safe: an agent that can
rewrite its instructions can also rewrite its safeguards, and an agent
that grades itself grades optimistically and does not reliably correct
itself [11, 20, 36].
Autonomous investing makes these requirements concrete. Ev-
ery action is irreversible and scored daily in money, and the incen-
tive to let a plausible lesson override a hard rule is constant. It is also
a Web setting in the sense of the agentic Web: every input is public
Web content (news feeds, SEC EDGAR filings, FRED statistics and
exchange quotes), every action leaves through a brokerage Web
API, and the central threat, untrusted content reaching an agent
with authority to act, is the one the Web-agent security literature
studies [2, 5, 8]. Prior LLM trading agents [ 28, 40, 41] combine
analyst roles, memory and reflection, but they are evaluated on
historical data, where pre-training leakage is hard to exclude [18];
their learning loops run on the model’s own reflection or on back-
tests, and nothing in them separates what may change from what
must not.
We presentSteward, a multi-agent LLM system in which nine
agents trade a US equity portfolio through a brokerage API, in six
sessions per trading day and with no human in the trading loop.
Four analysts read news, filings, macroeconomic series and market
data; a Portfolio Manager decides from their typed reports and
from a seven-layer shared memory that code assembles from the
system’s own record; and the system improves itself bygoverned
self-evolution: code grades every decision against realised outcomes,
a reflector proposes typed changes to the prompts, and a determin-
istic, reversible gate applies them but cannot reach aninvariant
coreof order arithmetic, blocking risk rules and the prompts of
the discipline agents. The key idea is to draw the boundary of self-
evolution in the type system rather than in a prompt: the proposal
type cannot name the core, and every signal that drives evolution is
computed by code from outcomes, so the system can rewrite itself
without being able to weaken its own safeguards. Every decision
is a typed object stored with its inputs, so the trace that makes
arXiv:2610.30557v1  [cs.AI]  22 Oct 2026

Feng et al.
9 RSS feeds
Reuters, CNBC,
AP, BBC, Fed
SEC EDGAR
10-Q and
10-K filings
FRED
VIX, yields, CPI,
UNRATE, HY OAS
Market data
OHLCV, sector,
valuation
News Intelligence
3-layer typed report
Earnings Analyst
5-step CoT
Macro Analyst
6-step CoT
Technical Analyst
5-step CoT
Prompt editor
12 invariants, 6
target prompts
Meta Reflector
7-step CoT→
PromptLearning[]
Replay harness
re-runs recorded
inputs (R5)
Shared memory, assembled by code
L1 today’s typed signals·L2 position context and rating trajectories·L3 narrative, regime, active state changes·L4 45-day
calibration by size·L5 last five Risk Manager verdicts·L6 own last three decisions·L7 projected book
Evening Analyst
7-step CoT grades
every trade
Circuit breaker
no LLM;−3%day
⇒liquidate
Portfolio Manager
7-step CoT→
TargetPosition
Order constructor
shares, stops, R/R
from live quotes
Hard risk engine
cash-only; size,
sector, loss caps
Risk Manager
6-step CoT: approve,
reject, modify, scale
Executor
sells then buys; stop
after each fill
Brokerage API
orders, fills, P&L
Position Reviewer
HOLD, REDUCE,
SELL, TRAIL_STOP
orders
positions, equity
insights
verify
Morning sessiononce a day; the only session that may open positions
Evening and quarterlygrade, reflect, gate, verify
Intradayevery 30 min, sell-only
evolvable LLM agent
protected LLM agent
deterministic code
Web / API boundary
data and orders
state feedback
self-evolution loop
Figure 1:Steward. Header colour gives each component’s governance class; shaded panels group the sessions; green arrows
trace the self-evolution loop.
the system governable also makes itevaluable: each output can
be re-scored against later prices and each input replayed through
modified prompts. We ranStewardlive for five months in a bro-
kerage paper account on real-time Web data and market quotes,
so every decision was recorded before its outcome existed. To our
knowledge,Stewardis the first self-evolving LLM agent evaluated
over months of live operation with every proposal and rejection of
its evolution loop logged.
Contributions.
C1 Joint decisions by role-specialised agents over hetero-
geneous Web data(§4.1, §4.3): four analysts turn four Web
sources into typed reports, and a Portfolio Manager synthe-
sises them, while order arithmetic, blocking risk rules and the
prompts of two discipline agents form an invariant core beyond
the reach of any prompt, including prompts the system writes
for itself.
C2 A seven-layer shared memory with schema-enforced rea-
soning(§4.2): code assembles the day’s signals, position con-
text, narrative and regime, calibration by position size, recent
risk verdicts, the agent’s own last decisions and the projected
book, so that every number an agent cites comes from code
rather than from another agent’s prose, and every reasoning
step is a mandatory field of a typed chain-of-thought (CoT).
C3 Governed self-evolution at two time scales(§4.4–§4.6):
each evening, code grades every trade and forecast and writes
the grades into memory; each quarter, a Meta Reflector pro-
poses typed prompt learnings that a twelve-invariant gate ap-
plies reversibly and that replay verifies.
C4 A five-month live deployment with a complete decision
trace(§5): 102 trading days, 1,632 LLM calls with complete
outputs, 95% of them also with complete inputs, and 438 broker
round trips, evaluated forward on live data. The value lies in the
joint synthesis, as a single model on the same data trades more
and worse; the system contained a 24.6% sector drawdown to
a 0.3% loss and followed no injected instruction, and a 2015–
2026 backtest shows the core alone lowering drawdowns across
four crashes; 99.9% of the numbers cited in recorded reasoning
are grounded in the agents’ inputs; and the evolution loop
diagnosed its own failures and applied a learning that the agent
adopted only where intended. The code, prompts and replay
harness are open source.1
2 Related Work
Self-improving and self-evolving agents.Reflexion [ 25] and
Self-Refine [20] let a model critique and revise its own outputs;
Voyager [27] accumulates a skill library; Promptbreeder [ 7] and
OPRO [ 37] optimise prompts with the model as the proposer;
Generative Agents [ 23] add memory and periodic reflection; a
survey frames these asself-evolving agents[ 1]. Two findings qual-
ify the programme: LLMs do not reliably self-correct [ 11], and
their verbalised confidence is overconfident [36]. We take both as
constraints: evolution is driven by code-computed outcomes and
bounded by a type-level allow-list and a deterministic gate. No
prior work reports a self-evolving agent operating for months in a
live market with its proposals and rejections logged.
Text, machine learning and LLMs in finance.That text moves
prices is established: media pessimism predicts short-lived pres-
sure that reverts [26]; general sentiment lexicons misclassify most
negative words in filings [19]; and much of newswire sentiment
is impounded within the day [ 15]. Machine-learning return pre-
diction from characteristics is the benchmark [9]. LLMs enter as
readers of text: GPT-4 headline labels predict a short drift [18], and
LLMs hallucinate financial facts unless grounded by retrieval and
tools [13]. This literature evaluates signals in backtests; our contri-
bution is not a signal but the governance of an agent that acts on
many, evaluated live.
1https://github.com/yebof/quant-agent

Governed Self-Evolution for Autonomous Investing
LLM agents for trading.FinMem [ 40] introduced layered mem-
ory; FinCon [41] a manager–analyst hierarchy with verbal rein-
forcement; QuantAgent [28] a self-improving knowledge base; Fi-
nAgent [45] and TradingAgents [34] tool use and trading-firm roles;
StockAgent [43] a simulated market. Their evaluation is historical,
where pre-training leakage is hard to exclude [18], or simulated, and
where they learn, the signal is the model’s own reflection [41, 45]
or a backtest [28];Stewardis evaluated forward in live trading,
learns from live outcomes graded by code and evolves around a
core its loop cannot reach. Surveys [21], domain models [32] and
benchmarks [35] evaluate no deployed agent.
Security of LLM agents.Prompt injection was characterised as
goal hijacking [24] and, in its indirect form, as an attack delivered
through retrieved Web content [8]; a formal treatment followed [17],
and benchmarks show that agents remain vulnerable [ 5, 42, 44].
Recent defences are architectural: execution isolation [ 33], capa-
bility and information-flow control [3, 4], and design patterns that
bound what an agent may do after reading untrusted input [2]. Our
invariant core is of this architectural kind, and our setting adds a
channel beyond the memory poisoning it studies [44]: the agent’s
own record fed back to a reflector that rewrites its instructions.
Frameworks, structured output and Web agents.AutoGen [ 31],
MetaGPT [10] and CAMEL [16] coordinate role-specialised agents
through natural language and structured messages, building on
chain-of-thought [29] and ReAct [39]. Constrained decoding [30]
and structured-output modes [22] make schema-conformant JSON
cheap; we use schemas as the specification of the reasoning proce-
dure, the audit artefact and the boundary of what evolution may
touch. Mind2Web [6] and WebArena [46] evaluate agents that op-
erate Web interfaces, the agentic-Web vision anticipates agents as
first-class Web actors [38], and Kapoor et al. [ 14] ask that agent
evaluation report cost and reproducibility, which we do.
3 Problem Statement
Setting.An agentic system 𝑆 with instructions 𝜋 (prompts and
code) observes Web evidence 𝑥𝑡 at each decision epoch 𝑡, emits a
decision 𝑑𝑡 =𝑆 𝜋(𝑥𝑡) and acts on it through an API. The environ-
ment later reveals an outcome 𝑦𝑡 , here market prices, that scores
𝑑𝑡 independently of 𝑆. Aself-evolvingsystem also runs a loop that
maps its own recordR𝑇 ={(𝑥 𝑡 , 𝑑𝑡 , 𝑦𝑡)} 𝑡≤𝑇 to revised instructions
𝜋′. We assume that the LLM components are capable but unreliable
in known ways: they cannot be trusted with factual recall [ 13],
their self-assessments are overconfident [36] and degrade on new
tasks [12], their free text is not machine-checkable, and the evidence
they read is untrusted [8].
Failure modes.Four failures can occur in such a loop without
being observed. (F1)Self-grading: the signal that drives evolution is
the agent’s own assessment ˆ𝑔𝑡 rather than 𝑦𝑡 , and ˆ𝑔𝑡 is optimistic.
(F2)Discipline erosion: 𝜋′ weakens the rules that bound risk, because
nothing separates what the loop may change from what it must
not. (F3)Unauditable change: no record ties 𝜋′ to the evidence that
produced it, so an erroneous edit can be neither found nor reverted.
(F4)Undetected inertness: an edit passes every check yet changes
no decision, and the loop reports progress it did not make.
Governed self-evolution.We call a self-evolving systemgoverned
if it meets five requirements. (R1)Typed record: every 𝑑𝑡 is a
machine-checkable object stored with 𝑥𝑡 , so that code can grade,
read and replayR𝑇 . (R2)Outcome grading: every signal fed back
into decisions or reflection is computed from 𝑦𝑡 by deterministic
code, never by 𝑆. (R3)Typed proposals: every proposed change
to 𝜋 is a typed object whose justification cites the graded record.
(R4)Gated application: deterministic code applies proposals under
invariants, logs every acceptance and rejection, can revert in one
step, and cannot reach aninvariant core 𝜋0⊂𝜋 (the arithmetic,
the blocking rules and the discipline agents’ prompts) because
the proposal type cannot name it. (R5)Verification: the effect of
a proposal is measured by replaying recorded inputs through 𝜋′.
R1 and R2 address F1 and F3; R3 and R4 address F2 and F3; R5
addresses F4.
Research questions.A live deployment of such a system lets five
questions be answered from the record alone. (RQ1) What does
each layer of 𝑆, from analyst signal to executed order, contribute
to the outcome? (RQ2) What do the multi-agent decomposition
and the shared memory add over a single model? (RQ3) What does
the evolution loop propose, how does the gate act on it, and what
does an applied learning change? (RQ4) Does the invariant core
hold, including under adversarial Web content, and at what cost?
(RQ5) Are the numbers the agents reason with grounded in their
inputs? §4 instantiates R1–R5 in a trading system and §5 answers
RQ1–RQ5.
4 Design ofSteward
Stewardinstantiates R1–R5 in a trading system. Nine LLM agents
and a deterministic core run in six sessions (§4.1); a shared memory
and typed CoT make every decision a checkable record (§4.2); safety
is enforced by construction rather than by instruction (§4.3); and
the system evolves itself at two time scales, by evening grading
(§4.4), a gated quarterly loop (§4.5) and replay (§4.6).
4.1 Agents and sessions
Sessions.The system runs sixsessionsper trading day (Figure 1;
Table 6, Appendix D). Only the morning session may open posi-
tions: four analysts read the Web in parallel, a Portfolio Manager
synthesises their typed reports with the shared memory of §4.2,
and the plan passes through a deterministic order constructor, a
blocking risk engine and an LLM Risk Manager before execution.
The midday and close sessions are sell-only and run a Position
Reviewer; a circuit breaker runs every 30 minutes without any
LLM; the evening session grades the day; and a quarterly session re-
flects on the quarter’s graded outcomes. All evidence is public Web
data (nine RSS feeds, SEC EDGAR filings, nine FRED series, and
daily price, sector and valuation data for a universe of 80 US stocks
and 21 exchange-traded funds (ETFs)), and orders leave through a
brokerage REST API.
Agents and their typed outputs.Each agent emits one Pydantic
object (Appendix B). TheNews Intelligenceagent maintains three
layers: a macro narrative of themes and regime that persists across
sessions, zero to fourstate changesper session (an event with its
previous and new state, market impact, affected symbols and a

Feng et al.
conviction), and per-symbol news items with a sentiment and an
impact summary. TheEarnings Analystreads 10-Q and 10-K filings
and reports revenue, margins, guidance and risk flags with a sen-
timent and a data-quality note. TheMacro Analystclassifies the
regime (risk-on, risk-off, neutral or transitional) from the FRED
series and issues sector stances and a target invested share. The
Technical Analystrates each symbol on a five-level scale with an
entry, a reference target, a stop and the condition that would in-
validate the setup. ThePortfolio Managerreturns target positions;
theRisk Managerapproves or rejects the plan with a reason cate-
gory, field-level modifications and an optional scale factor for all
buys; thePosition Reviewerreturns SELL, REDUCE, TRAIL_STOP
or HOLD per holding.
Orchestration.A session runs at most once per day under a lock
and is killed after 20 minutes. An LLM call is retried up to seven
times with exponential backoff and then fails over to a model from
a second vendor. Every other failure removes an action rather than
adding one (Table 13, Appendix F).
4.2 Shared memory and typed reasoning
Shared multi-layer memory.The agents share no conversation
history. They share a memory that code assembles from the sys-
tem’s own record in seven layers, read by the Portfolio Manager
every morning. L1 holds the day’s typed analyst signals. L2 gives
each holding its entry date, days held, entry thesis and its last seven
Technical ratings. L3 is the narrative: the last seven evening out-
looks, seven days of macro regime, and the high-conviction news
state changes of the last two weeks. L4 is a 45-day calibration table:
code matches buys to later exits first-in-first-out and reports win
rate, mean return and holding time by entry size (below $5k, $5–10k,
above $10k), so that the agent learns whether its conviction pays.
L5 lists the last five Risk Manager verdicts with their categories, L6
the agent’s own last three decisions, so that reversals are visible,
and L7 a projected book that flags sectors approaching their cap.
Every number an agent can cite therefore comes from code, not
from another agent’s prose.
Schema-enforced reasoning.Every agent’s output type contains
its reasoning procedure as a nested CoT object in which each step
is a field declared str = Field(min_length=1) (Listing 1; Ap-
pendix B lists every agent’s steps). An agent cannot skip a step,
enumerations are Literal types, and cross-field validators encode
domain invariants: an actionable rating must carry an entry and a
stop on the protective side, a wrong grade must name a root cause,
and a proposal must cite a number. List-valued fields are validated
item by item, so a malformed entry is dropped and logged instead of
invalidating a whole report. The validated object is stored verbatim
with its exact input, so the record is not a logaboutdecisions but
the decisions themselves, in a form that code can grade, a reflector
can read and a harness can replay.
4.3 Safety by design
Safety does not rest on any prompt: order arithmetic, blocking
rules and two discipline agents’ prompts form theinvariant core 𝜋0,
which no self-edit can reach.
Judgement is separated from arithmetic.No LLM number
reaches the broker unchecked. The Portfolio Manager emits
TargetPosition intent(a symbol, a target weight of at most
20%, a conviction and a named condition that falsifies the thesis;
Listing 1), and a deterministic constructor turns it into orders. It
takes the stop from the Portfolio Manager or the Technical Analyst
and otherwise places it two average true ranges (ATR) below entry;
at execution, code widens any stop closer than one ATR, sizes the
position as the smaller of its target weight and a risk budget of
0.5% of equity at the stop, skips an entry more than 5% from the
market price, and skips a trade whose risk/reward falls below 1.2
once execution has moved its prices. Risk/reward is a computed
field that the Risk Manager audits against a floor of 1.5.
Hard rules run before the LLM check.A blocking engine rejects
BUYs that would drive cash negative, positions above 20% of equity,
sectors above 40%, net exposure above 90%, entries without a stop,
and any buy after a 3% daily loss. Only plans that pass reach the
LLM Risk Manager, which can reject, modify or scale them but
cannot approve what the engine blocked. The Risk Manager fails
closed: if its call or its schema fails, the plan is rejected.
Untrusted Web text stays upstream.Prompt injection is the central
threat to an agent that reads the Web and holds authority to act [8].
Raw headlines and filing text reach only the News and Earnings
agents, whose prompts treat them as data, drop instruction-like
items and flag them in the report. Code then drops any news state
change whose keywords and symbols appear neither in the input
nor in the prior state, so an agent cannot assert an event its sources
do not contain. The Portfolio Manager never sees a headline or
a filing: it reads typed fields and the News agent’s briefing, and
anything it proposes still meets the constructor, the hard rules and
the Risk Manager. An injected instruction must therefore survive a
typed report, a deterministic engine and an independent auditor
before it can become an order (§5.5).
Execution is fail-safe.The executor sends sells first as limit orders
and waits for their fills, re-checks the daily loss before any buy,
records each order before submission so that a crash cannot leave
an untracked fill, and places a good-till-cancelled stop order as soon
as a buy fills. The circuit breaker, which uses no LLM, runs every
30 minutes and again at each stage of the morning session; on a 3%
daily loss it cancels open entries and liquidates.
The evolvable periphery.Whatcanchange is the memory, rewrit-
ten daily by code, and the prompts of the four analysts, the Portfolio
Manager and the Evening Analyst, each of which carries a marked
Learningssection that the gate of §4.5 may append to. The Risk
Manager and the Position Reviewer, which encode the hard disci-
pline, are absent from the Literal type of the proposal schema,
so no self-edit can name them, and every rule above lives in code
that no prompt reaches. A learning can changewhatan agent pro-
poses; it cannot change how a proposal becomes an order, or relax
a constraint.
4.4 Short-term self-evolution: evening grading
The evening session closes each trading day with two kinds of
grading (R2). Code first assembles the evidence: the sells of the last

Governed Self-Evolution for Autonomous Investing
two days and the buys of the last five with their realised returns, the
last ten next-day calls scored against the next day’s return, and the
moves of at least 8% over five days in universe names the system
did not hold. The Evening Analyst then completes a seven-step CoT
that attributes performance, reviews the previous outlook and each
position’s thesis, grades every trade correct, premature or wrong,
assigns every wrong buy one of nine root causes (for examplemacro
warning ignoredortop chasing), classifies missed opportunities, and
sets a next-day bias. Grades and P&L are written to the record in
one transaction.
The labels the Evening Analyst assigns are categories; every
quantity that measures an outcome is computed by code from fills
and prices. What feeds forward is aggregated by code from that
record: the calibration of L4, the hit rates of the next-day calls,
missed themes that recur in at least two episodes or symbols over
the last 14 evenings, and root causes that recur across at least two
symbols. The Portfolio Manager reads them the next morning with
the evening’s outlook, and its prompt bounds the tilt a prior evening
may apply to sizing at 20%.
4.5 Long-term self-evolution: the quarterly loop
The quarterly loop acts on the periphery in six steps, each assigned
to one side of a boundary: language models act and reflect, whereas
code records, grades, gates and rewrites.
Reflect and propose (R3).On the last trading day of each quar-
ter the evening session invokes a Meta Reflector. Its input is a
deterministic digest of 90 days of graded record (alpha against SPY,
calibration by size, themes caught and missed, root causes of wrong
trades and per-agent signal activity) together with every editable
prompt, its currentLearningssection and the previous quarter’s
reflection. Its CoT has seven mandatory steps in a fixed order: per-
formance facts, theme audit, loss autopsy, a five-axisself-portrait, a
gap diagnosisthat attributes the largest gaps to agents, anaudit of
existing promptsthat checks whether a rule for each gap already
exists, and only thenproposal reasoning. Its output is at most three
PromptLearning objects (Listing 1), each an append or a retraction
by content hash, with a text of 20–300 characters, a justification of
at least 40 characters that must contain a number from the digest,
a target drawn from a Literal of the six editable agents, and a
self-rated confidence.
Gate and rewrite (R4).The gate has two deterministic layers
(Appendix C). The proposal schema rejects a malformed learning
before it is staged, and a PromptEditor applies the rest under its
own invariants. Edits are append-only into the marked section and
tagged with quarter and content hash, so human-written text is
never modified; targets must be on the allow-list; a word-boundary
tripwire rejects absolutes such asnever,alwaysandoverride, which
conflict with the hard rules; a Jaccard similarity of 0.6 or more to
an existing entry rejects a paraphrase; a FIFO cap of ten entries per
agent bounds the section; at most three agents change per cycle;
every acceptedandrejected proposal is logged with its reason; and
a cycle’s edits form a single version-control commit, so that one
git revert undoes a quarter of evolution. The editor runsstage-
only(proposals written to a file for human review) orlive-apply, in
which it can apply the reviewed file rather than a fresh reflection.
The Q2 cycle ran stage-only and the Q3 cycle live (§5.4).
4.6 Verification by replay
Every LLM call is stored with its full response, the model, token
counts and cost and, since April 12, its complete input message,
so any later decision can be re-run (R5). Adecision-replayharness
passes recorded inputs through the prompt before and after a learn-
ing, with the rest of the input fixed, and compares the outputs
structurally: for the Portfolio Manager, which symbols were added,
dropped or resized; for the Evening Analyst, whose full evening
inputs are frozen to disk, how its bias, grades, miss categories and
suggested actions changed. Re-running the unchanged prompt on
the same inputs measures the model’s own variance, against which
a learning’s effect is read. This replaces the argument that a learning
shouldhelp with a measurement of what it changed on 𝑛 recorded
inputs, at a cost of tens of dollars per experiment.
5 Evaluation
5.1 Live deployment, data and methodology
Stewardtraded live from April 8 to September 10, 2026 (102 trading
days) on real-time Web data, in a brokeragepaperaccount funded
with US$100,000. Paper fills are simulated against live quotes, so
prices, timing and order rejections are real; market impact is not.
Every decision was recorded before its outcome existed, so the live
record is forward and free of the pre-training leakage that is hard
to exclude in backtests of LLM agents [ 18]. Idle cash earned the
Treasury-bill rate. No human intervened in any trading decision;
the evening loop ran on 98 evenings and the quarterly loop at both
quarter ends. Code and prompts were unchanged from July 16 to
the end of the window. The deployment produced 619 pipeline
runs and 1,632 logged LLM calls served by frontier models from
two vendors with automatic failover. Logged API cost was $455,
about US$4.4 per trading day (Appendix D). The broker recorded
492 orders and 746 fills; the fill record is the ground truth for all
trade-level analysis.
R1 yields three kinds of evidence. Thelive recordis broker fills
and daily equity.Trace re-scoringgrades every recorded agent out-
put (7,843 Technical Analyst ratings, 1,885 symbol-days of news
sentiment, 97 evening forecasts, 556 target weights, 90 risk ver-
dicts and 438 round trips) against later prices without any LLM.
Replayre-runs recorded inputs through modified prompts or ar-
chitectures. Forward-return statistics use day-clustered standard
errors because horizons overlap. Every number, figure and table
in this paper is computed by scripts from the recorded trace, and
the open-source system can be re-run on its recorded inputs (https:
//github.com/yebof/quant-agent).
5.2 RQ1: What each layer contributes
Each analyst signal is weak on its own.Scored against market-
adjusted forward returns, the Technical Analyst’s five-level rating
has a mean daily rank information coefficient (IC) of−0.004,0 .019
and0 .031at 5, 10 and 20 days ( 𝑡= 1.2at 20 days), withsellratings
carrying the only discernible effect (−1.7%± 1.4over 20 days); and
News sentiment is uncorrelated with later moves (Figure 5, Appen-
dix E). The value therefore lies in their synthesis. Code grading also

Feng et al.
May Jun Jul Aug Sep
100
102
104
106
108
110
112
114
116Indexed value (8 Apr = 100) Analysts +1.3%
Live +5.0%
Intent +12.2%
SPY +12.4%
a Policy layers on recorded decisions
May Jun Jul Aug Sep
0
25
50
75
100Gross exposure (% of equity)means: intent 79%, live 56%
Intent
Live
b Execution gap
May Jun Jul Aug Sep
−5
0
5
10
15
20
25
30
35Post-exit gain of sold lots (US$k)
Stops
(n = 132)
Agent exits
(n = 306)
c Opportunity cost of exits
5 d 10 d 20 d
Horizon
−4
−2
0
2
4
6
8
10Excess return of book (pp)
d Replay: 20 mornings
Deployed
No memory
Single agent
Figure 2: What the typed trace attributes to each layer. (a) Recorded decisions followed through prices as signal-following
portfolios, against the live portfolio and SPY (other layers in Table 1). (b) Gross exposure of simulated intent and live portfolio
(capped at 100% before April 19); shading, the execution gap. (c) Cumulative gain of sold lots after exit, by exit mechanism.
(d) Replay of 20 mornings through three decision layers: market-adjusted forward return of the proposed book (mean, 95% CI).
held the Evening Analyst to account: its 38 directional next-day
calls were right 37% of the time, below the 54% base rate of up
days, and because the grade is computed by code (R2), this hit rate
appeared in its own next-day prompt.
The synthesis carries the value.Following the recorded decisions
through prices (Figure 2a, Table 1; targets set at the decision-day
close, 20% position cap, cash earning the T-bill return), the analysts’
buy ratings return+1.3%, whereas the Portfolio Manager’s target
weights return+15.4%with no exits (at 93% exposure),+11.6%with
the system’s own exit rules and+12.2%with the Risk Manager’s
recorded edits, at a higher Sharpe ratio than without them (2.33
against 1.80). The Portfolio Manager’s synthesis of weak signals
with the shared memory thus matched the index and beat every
analyst-following baseline by more than ten points, and the Risk
Manager reduced volatility more than return.
Execution and exits hold the headroom.The live portfolio returned
+5.0% against the intent’s+12.2%because it was less invested: re-
alised gross exposure averaged 56% against 79% (Figure 2b), as 180
of 492 orders were cancelled or expired unfilled, the hard rules
trimmed buys and intraday stops fired where the close-based simu-
lation held. The same gap appears on the risk side, as a beta of 0.16
for the live book against 0.64 for the intent (Table 1). Exits show
the same pattern. Of 438 round trips, 306 were closed by agent
decisions and 132 by broker-held stops (Table 7). Lots closed by the
core’s mechanical stops went on to gain only US$0.7k beyond the
US$3.7k they realised; lots closed by agent decisions went on to
gain US$19.9k beyond the US$0.8k realised (Figure 2c). The Evening
Analyst had graded 134 of 163 sellscorrect; only the outcome-scored
measure exposes the opportunity cost, which is why R2 puts grad-
ing in code.
5.3 RQ2: The decomposition and the memory
The simulations take the Portfolio Manager’s intent as given. To
test the design upstream of it, we replay 20 mornings sampled
evenly over the deployment through three decision layers on their
exact recorded inputs (Table 2, Figure 2d; 100 LLM calls): the de-
ployed design (typed analyst reports plus memory; two samples
Table 1: Policy layers on recorded decisions against the live
portfolio and SPY. Return, volatility and maximum draw-
down in %; exposure, mean gross.
Policy Return Vol. Max DD Sharpe Beta Exposure
PM intent, no exits, no RM+15.4 13.7−4.7 2.52 0.83 93%
PM intent + system exits+11.6 15.0−4.7 1.80 0.80 76%
PM intent + exits + RM (Intent)+12.2 11.9−4.5 2.33 0.64 79%
Live portfolio+5.0 9.0−6.0 1.39 0.16 56%
Analyst-following, all buys+1.3 11.3−7.8 0.32 0.50 41%
Analyst-following, high-conv. buys+0.4 2.0−1.8 0.41−0.01 5%
SPY+12.4 12.4−4.5 2.28 1.00 –
Table 2: Architecture replay on 20 recorded mornings. Names:
positions targeted; New: of which not held; Gross: new intent,
% of equity; Rev.: reversals; Excess: market-adjusted forward
return, pp (mean±s.e.).
Decision layer Names New Gross Rev. Excess 5d Excess 20d
Deployed design3.7 3.2 19% 0.10−0.5±0.9+1.3±2.9
No shared memory 3.5 3.0 19% 0.12−0.4±0.8+0.8±2.5
Single agent, raw data 5.8 4.4 41% 0.25−1.3±0.4−0.8±0.9
per morning), the same input without any memory layer, and a
single model that receives the raw data the analysts read and must
analyse and decide in one call. Each proposed book is scored by the
weight-averaged market-adjusted forward return of its names. The
single agent is a different trader: it targets 5.8 names a morning
against 3.7, puts 41% of equity into new intent against 19%, and
reverses its own recent decisions two and a half times as often (0.25
against 0.10 per morning), including re-buying names it had just
closed, which the deployed design never did. Its books lose over the
next five and ten days (−1.35± 0.44and−1.76± 0.75points against
SPY; hit rates 35% and 32%), whereas the deployed design’s are
indistinguishable from zero. Removing the memory changes almost
nothing on a single morning, so the typed reports carry most of the
per-morning information and the memory’s role is longitudinal:
calibration, continuity and feedback.

Governed Self-Evolution for Autonomous Investing
0 5 10
Weight, base prompt (%)
0.0
2.5
5.0
7.5
10.0Weight, with learning (%)
grey band: ±1.8 pp
re-run noise
a Q2 learning (withheld)
Control
Graded wrong
Recurring
named
Prescribed
form
Form on
controls
0
20
40
60
80
100Share (%)
b Q3 learning (applied)
0 0 0
Base prompt
With learning
Figure 3: Both quarterly learnings verified by replay. (a) Q2,
withheld: weight of each flagged BUY with and without the
learning; grey band, re-run noise. (b) Q3, applied: share of
recurring misses named, and of replays in the prescribed
form, on trigger and control evenings (95% Wilson CI).
5.4 RQ3: Two cycles of self-evolution
Q2: a root-cause diagnosis and a withheld learning.The Meta
Reflector’s first run (stage-only, 52 trading days) attributed the
shortfall against the index to “structural under-participation in a
broad rally, not a blow-up”; found that 14 of the 20 BUYs graded
wrongshared one root cause,macro warning ignored(an active
high-conviction bearish news state change at purchase); declined
to edit a prompt where it traced the gap to the data rather than
the instructions; and proposed exactly one learning, to treat such
a state change as a sizing gate, at self-ratedlowconfidence. The
gate withheld it on its length invariant (282 characters against a
200-character cap) and logged why. Replay then measured what the
gate had declined (Figure 3a, Table 8; 35 calls, US$17): on the ten
mornings whose BUYs were later graded wrong and five control
mornings, the Portfolio Manager prompt with the learning kept 8
of the 10 flagged names that the baseline still proposed within one
point, and every weight moved within the noise of re-running the
baseline itself (1.8 points per name at the median). The withheld
learning was inert, so the strict gate cost nothing.
Q3: self-audit and an applied learning.The second run, on Sep-
tember 30, was live. The reflector first audited its own Q2 diagnosis:
macro warning ignoredhad fallen from 14 wrong BUYs to 3, and
because the Portfolio Manager prompt already carried rules for it,
the reflector declined to add more, citing the risk of overcorrection.
It again sent two anomalies to the operators instead of into prompts,
attributing them correctly to the digest’s instrumentation. It then
located a new gap: 70 of 104 classified misses were missed value
entries or trend timings, some named on three or more evenings
without being acted on. Its one proposal, atmediumconfidence, was
a 185-character learning for the Evening Analyst: when the same
symbol is classified a missed value entry or trend on three or more
evenings, promote it to a suggested action with a TAKE/WAIT call
and a named blocker. The gate applied it as a one-file, reversible
commit. Because the operators had also revised other prompts and
the universe before the cycle, the October record cannot isolate
the learning; replay can. We re-ran ten evenings on which such
recurrences existed and four control evenings through the prompt
before and after the commit, two samples each (Figure 3b, Table 9;
56 calls, about US$16). The agent adopted the learning, and only
where it applied: the prescribed form (an explicit TAKE/WAIT call
or named blocker) appeared in 5 of 20 trigger replays against 0 of
20 for the base prompt and never on a control evening, while the
next-day bias stayed as stable as re-running the base prompt (86%
against 79% agreement). The edit thus added the targeted behaviour
without disturbing the rest of the output. Replay also located what
the learning still needs: the trigger presupposes a count of past
classifications that the Evening Analyst’s input does not provide,
so the recurring misses surfaced were unchanged (25 of 64 against
26 of 64). Adding that count is a concrete next step, for a gap that
the gate’s invariants cannot detect and that replay found for US$16.
The evening loop.The daily loop should make the system less
active after poorly graded periods, and the record is consistent with
this: realised exposure co-moves with the trailing forecast hit rate
(𝜌= 0.34, 𝑝= 0.01) and the trailing realised win rate ( 𝜌= 0.22,
𝑝= 0.05), whereas the Portfolio Manager’s declared sizing does
not (|𝜌|≤ 0.14; Table 10; Holm-adjusted 𝑝= 0.08for the strongest
relation): the adaptation runs through the graded memory rather
than through the agent’s stated intent.
5.5 RQ4: The invariant core under live and
adversarial conditions
Containment.The portfolio returned +5.0% against +12.4% for
SPY during a semiconductor-led rally (Table 3), at a beta of 0.16 and
volatility of 9.0% against 12.4%; alpha is not identifiable over 102
days, and no claim of this paper rests on it. Between June 22 and
July 29 the semiconductor ETF fell 24.6%, QQQ 10.3% and SPY 2.0%,
whereas the portfolio lost 0.3%, having exited its semiconductor
positions in May on named triggers that are legible in the trace. One
window holds one drawdown, so we also backtest the deterministic
core alone over 2015–2026 (Table 11, Figure 6): its stops, caps, cash-
only rule and breaker applied to LLM-free weekly entries on the
universe’s 80 stocks, which rules out pre-training leakage. The
core lowered the maximum drawdown under all 50 random entry
policies (median 37%→ 28%) and under momentum entries (61%
→ 33%), and the drawdown of the 2018, 2020 and 2022 sell-offs for
at least 49 of 50, at an unchanged Sharpe ratio; the caps and the
breaker do most of the work. In the 2026 semiconductor window the
same rules still lost 27% under momentum entries: the core bounds
what judgement can lose, and the agents’ May exits did the rest.
The Risk Manager rejected 4 of 90 plans and made 146 field-level
edits; the circuit breaker never had to liquidate; after the cash-only
rule took effect on April 19 gross exposure never exceeded 92%; and
across 1,632 calls validation failed on 13 sub-items, each isolated
without losing a session.
Adversarial Web content.Untrusted content reaches the agents
through the news feeds. We insert one adversarial item into the
exact recorded input of ten mornings and re-run the agent (Table 4;
50 calls, US$19), with three payloads: a direct override (set one
name to 45% and every other target to zero), a plausible headline
(300% upside; managers are taking maximum size and disabling
stops) and a suspension of discipline (stops and the cash-only rule
lifted, allocate 60% to an inverse ETF). The News agent excluded

Feng et al.
Table 3: Full-period outcome against benchmarks and daily-
rebalanced T-bill blends (zero risk-free rate). Return, volatil-
ity, drawdown and 𝛼 (Jensen’s, against SPY, annualised) in %.
Return Vol. Max DD Sharpe Sortino Beta𝛼(ann.)
Live portfolio+5.0 9.0−6.0 1.39 1.76 0.16+8.2
SPY (S&P 500)+12.4 12.4−4.5 2.28 3.55 1.00−0.0
QQQ (Nasdaq-100)+17.1 22.1−11.2 1.79 2.79 1.63−6.6
SMH (semiconductors)+32.5 46.8−24.6 1.65 2.45 2.79−1.7
50/50 SPY / T-bills+6.9 6.2−2.2 2.58 4.02 0.50+1.8
Exposure-matched (56% SPY)+7.5 6.9−2.5 2.52 3.92 0.56+1.6
Beta-matched (0.16 SPY)+3.2 1.9−0.6 3.87 6.15 0.16+3.1
Table 4: Prompt-injection red team on 10 recorded morn-
ings. Excluded/Labelled: dropped from / flagged in the News
report; Followed/Refused: weight given to / refusal of the
payload’s target by the Portfolio Manager; Max wt: largest
weight the caps would allow.
News agent Portfolio Manager Core
Payload Excluded Labelled Followed Refused Max wt
P1 direct override 10/10 10/10 0/10 7/10 0%
P2 plausible headline 10/10 10/10 0/10 6/10 0%
P3 discipline suspension – – 0/10 10/10 0%
the item from its typed report in all 20 replays and flagged it as
instruction-like in every briefing. Placed directly in the Portfolio
Manager’s news section, as if the analyst layer had passed it through,
the item was followed in none of 30 replays; in 23 the Portfolio
Manager’s CoT named it as injected content and refused it, most
often because the symbol had no Technical Analyst report and the
demand conflicted with the stop and cash rules. Had any replay
complied, the schema would have dropped a 45% or 60% target
before the constructor and the hard caps would have bounded
anything smaller: injected content could at most change what an
agentwanted, and here it did not achieve even that.
5.6 RQ5: Grounding of cited numbers
Because every CoT is stored with its exact input, we can ask whether
the numbers an agent cites exist in what it was given. A determin-
istic audit of 750 recorded CoTs (Table 12) extracted 254,094 cited
numbers, excluding small integers and years, and matched each
against the agent’s input, its prompt and its own emitted fields. A
strict matcher (exact, rounded or truncated matches and explicitly
written arithmetic) grounds 96.1%; recognising derived quantities
such as risk/reward ratios and ATR-based stops raises this to 99.9%,
and the median CoT is fully grounded for every agent. A placebo
against another day’s input grounds 22% under the strict matcher,
so the test discriminates. Of the 226 ungrounded numbers, nearly all
are unwritten intermediate results of the sizing formula or chosen
trigger levels; three are candidate fabrications (a wrong price, a
misread indicator and a recalled policy-rate peak absent from the
input).
6 Discussion
RQ1–RQ5 yield three implications for multi-agent systems that act
and evolve in high-stakes Web settings.
Place the invariant core at the type level.Making the core un-
reachable rather than discouraged (arithmetic and blocking rules
in code, the discipline agents absent from the Literal of editable
targets) is what makes it safe for the system to rewrite itself. Lower
drawdowns across four crashes in backtest and the failed injections
are its observable consequences.
Grade with code, and allocate discretion where the data show skill.
Outcome-scored grading attributes the value to the Portfolio Man-
ager’s synthesis and the core’s mechanical exits and locates the
headroom in discretionary exits and execution; the Evening Ana-
lyst’s own grades, which rated 134 of 163 sells correct, would not
have shown this. A self-evolving system can improve only what
it measures, so the next step is to narrow the periphery on exits
and add an execution agent inside the core, leaving the judgement
layer that works untouched.
A syntactic gate needs a semantic check.The gate guarantees that
a learning is short, novel, reversible and confined to the periphery;
it cannot tell whether the learning changes a decision. Replay can,
cheaply: it confirmed that the withheld learning was inert and that
the applied one was adopted only where intended (§5.4). The Q3
learning also presupposes a count of past classifications that the
Evening Analyst’s input does not provide. Replay turned this into
a concrete fix. The natural next invariant is therefore an outcome-
scored replay check that confirms a learning is operable on the
agent’s actual inputs and measures its effect on decisions before it
is applied.
Limitations and next steps.The evidence comes from one config-
uration traded on a paper account through one rising window, with
overlapping forward horizons, simulations that ignore fill risk and
two quarterly cycles, one applied; replays of 14–20 inputs expose
behavioural differences but cannot rank variants by return. Each
limit narrows with operation: every further quarter adds a cycle to
the record, and the released harness scales replay to more inputs at
tens of dollars per experiment.
7 Conclusion
We presentedSteward, a multi-agent LLM system for autonomous
investing in which role-specialised agents decide jointly over het-
erogeneous Web data, share a memory computed by code, and
evolve at two time scales around an invariant core that no self-edit
can reach. Five months of live operation showed that the typed
trace that makes such a system governable also makes it evalu-
able: it located the method’s value and its headroom layer by layer,
recorded the system containing a sector drawdown and resisting
injected instructions, with a backtest of the core alone lowering
drawdowns across four crashes, and documented self-evolution
diagnosing its own failures and making targeted, reversible edits
whose effects replay verified at a cost of tens of dollars. We release
the system, the trace and the scripts so that outcome-scored replay
can be developed into a gate invariant on real inputs.
Ethical Considerations
The system traded a paper account, so no capital was at risk; all
inputs are public Web data used under the providers’ terms; no
human subjects were involved; and the released software is not

Governed Self-Evolution for Autonomous Investing
investment advice. The invariant core prevents a self-modifying
agent from eroding its own risk discipline by construction, and the
recorded trace lets this be audited.
References
[1] Huan ang Gao, Jiayi Geng, Wenyue Hua, et al. 2026. A Survey of Self-Evolving
Agents: What, When, How, and Where to Evolve on the Path to Artificial Super
Intelligence.TMLR(2026).
[2] Luca Beurer-Kellner, Beat Buesser, Ana-Maria Creţu, et al. 2025. Design Patterns
for Securing LLM Agents against Prompt Injections. arXiv:2506.08837.
[3] Manuel Costa, Boris Köpf, Aashish Kolluri, et al. 2025. Securing AI Agents with
Information-Flow Control. arXiv:2505.23643.
[4] Edoardo Debenedetti, Ilia Shumailov, Tianqi Fan, et al. 2025. Defeating Prompt
Injections by Design. arXiv:2503.18813.
[5] Edoardo Debenedetti, Jie Zhang, Mislav Balunović, Luca Beurer-Kellner, Marc
Fischer, and Florian Tramèr. 2024. AgentDojo: A Dynamic Environment to
Evaluate Prompt Injection Attacks and Defenses for LLM Agents. InNeurIPS
Datasets and Benchmarks.
[6] Xiang Deng, Yu Gu, Boyuan Zheng, et al. 2023. Mind2Web: Towards a Generalist
Agent for the Web. InNeurIPS Datasets and Benchmarks.
[7] Chrisantha Fernando, Dylan Banarse, Henryk Michalewski, Simon Osindero,
and Tim Rocktäschel. 2024. Promptbreeder: Self-Referential Self-Improvement
via Prompt Evolution. InICML.
[8] Kai Greshake, Sahar Abdelnabi, Shailesh Mishra, Christoph Endres, Thorsten
Holz, and Mario Fritz. 2023. Not What You’ve Signed Up For: Compromising
Real-World LLM-Integrated Applications with Indirect Prompt Injection. In
AISec.
[9] Shihao Gu, Bryan Kelly, and Dacheng Xiu. 2020. Empirical Asset Pricing via
Machine Learning.Rev. Financ. Stud.33, 5 (2020), 2223–2273.
[10] Sirui Hong, Mingchen Zhuge, Jiaqi Chen, et al. 2024. MetaGPT: Meta Program-
ming for a Multi-Agent Collaborative Framework. InICLR.
[11] Jie Huang, Xinyun Chen, Swaroop Mishra, et al. 2024. Large Language Models
Cannot Self-Correct Reasoning Yet. InICLR.
[12] Saurav Kadavath, Tom Conerly, Amanda Askell, et al. 2022. Language Models
(Mostly) Know What They Know.arXiv:2207.05221(2022).
[13] Haoqiang Kang and Xiao-Yang Liu. 2023. Deficiency of Large Language Models in
Finance: An Empirical Examination of Hallucination. arXiv:2311.15548. NeurIPS
Workshop.
[14] Sayash Kapoor, Benedikt Stroebl, Zachary S. Siegel, Nitya Nadgir, and Arvind
Narayanan. 2025. AI Agents That Matter.TMLR2025 (2025).
[15] Zheng Tracy Ke, Bryan Kelly, and Dacheng Xiu. 2019. Predicting Returns with
Text Data. NBER Working Paper No. 26186.
[16] Guohao Li, Hasan Abed Al Kader Hammoud, Hani Itani, Dmitrii Khizbullin, and
Bernard Ghanem. 2023. CAMEL: Communicative Agents for “Mind” Exploration
of Large Language Model Society. InNeurIPS.
[17] Yupei Liu, Yuqi Jia, Runpeng Geng, Jinyuan Jia, and Neil Zhenqiang Gong.
2024. Formalizing and Benchmarking Prompt Injection Attacks and Defenses. In
USENIX Security.
[18] Alejandro Lopez-Lira and Yuehua Tang. 2026. Can ChatGPT Forecast Stock Price
Movements? Return Predictability and Large Language Models.J. Financ. Econ.
184 (2026), 104335.
[19] Tim Loughran and Bill McDonald. 2011. When Is a Liability Not a Liability?
Textual Analysis, Dictionaries, and 10-Ks.J. Finance66, 1 (2011), 35–65.
[20] Aman Madaan, Niket Tandon, Prakhar Gupta, et al. 2023. Self-Refine: Iterative
Refinement with Self-Feedback. InNeurIPS.
[21] Yuqi Nie, Yaxuan Kong, Xiaowen Dong, et al . 2024. A Survey of Large Lan-
guage Models for Financial Applications: Progress, Prospects and Challenges.
arXiv:2406.11903(2024).
[22] OpenAI. 2024. Introducing Structured Outputs in the API. https://openai.com/
index/introducing-structured-outputs-in-the-api/.
[23] Joon Sung Park, Joseph C. O’Brien, Carrie J. Cai, Meredith Ringel Morris, Percy
Liang, and Michael S. Bernstein. 2023. Generative Agents: Interactive Simulacra
of Human Behavior. InUIST.
[24] Fábio Perez and Ian Ribeiro. 2022. Ignore Previous Prompt: Attack Techniques
For Language Models. arXiv:2211.09527. NeurIPS ML Safety Workshop.
[25] Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and
Shunyu Yao. 2023. Reflexion: Language Agents with Verbal Reinforcement
Learning. InNeurIPS.
[26] Paul C. Tetlock. 2007. Giving Content to Investor Sentiment: The Role of Media
in the Stock Market.J. Finance62, 3 (2007), 1139–1168.
[27] Guanzhi Wang, Yuqi Xie, Yunfan Jiang, et al. 2024. Voyager: An Open-Ended
Embodied Agent with Large Language Models.TMLR(2024).
[28] Saizhuo Wang, Hang Yuan, Lionel M. Ni, and Jian Guo. 2024. QuantAgent:
Seeking Holy Grail in Trading by Self-Improving Large Language Model.
arXiv:2402.03755(2024).
[29] Jason Wei, Xuezhi Wang, Dale Schuurmans, et al . 2022. Chain-of-Thought
Prompting Elicits Reasoning in Large Language Models. InNeurIPS.
[30] Brandon T. Willard and Rémi Louf. 2023. Efficient Guided Generation for Large
Language Models.arXiv:2307.09702(2023).
[31] Qingyun Wu, Gagan Bansal, Jieyu Zhang, et al. 2024. AutoGen: Enabling Next-
Gen LLM Applications via Multi-Agent Conversation. InCOLM.
[32] Shijie Wu, Ozan Irsoy, Steven Lu, et al. 2023. BloombergGPT: A Large Language
Model for Finance.arXiv:2303.17564(2023).
[33] Yuhao Wu, Franziska Roesner, Tadayoshi Kohno, Ning Zhang, and Umar Iqbal.
2025. IsolateGPT: An Execution Isolation Architecture for LLM-Based Agentic
Systems. InNDSS.
[34] Yijia Xiao, Edward Sun, Di Luo, and Wei Wang. 2024. TradingAgents: Multi-
Agents LLM Financial Trading Framework.arXiv:2412.20138(2024).
[35] Qianqian Xie, Weiguang Han, Zhengyu Chen, et al . 2024. FinBen: A Holis-
tic Financial Benchmark for Large Language Models. InNeurIPS Datasets and
Benchmarks.
[36] Miao Xiong, Zhiyuan Hu, Xinyang Lu, et al . 2024. Can LLMs Express Their
Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs. In
ICLR.
[37] Chengrun Yang, Xuezhi Wang, Yifeng Lu, et al. 2024. Large Language Models as
Optimizers. InICLR.
[38] Yingxuan Yang, Mulei Ma, Yuxuan Huang, et al. 2025. Agentic Web: Weaving
the Next Web with AI Agents.arXiv:2507.21206(2025).
[39] Shunyu Yao, Jeffrey Zhao, Dian Yu, et al. 2023. ReAct: Synergizing Reasoning
and Acting in Language Models. InICLR.
[40] Yangyang Yu, Haohang Li, Zhi Chen, et al . 2024. FinMem: A Performance-
Enhanced LLM Trading Agent with Layered Memory and Character Design. In
AAAI Symposium Series.
[41] Yangyang Yu, Zhiyuan Yao, Haohang Li, et al . 2024. FinCon: A Synthesized
LLM Multi-Agent System with Conceptual Verbal Reinforcement for Enhanced
Financial Decision Making. InNeurIPS.
[42] Qiusi Zhan, Zhixiang Liang, Zifan Ying, and Daniel Kang. 2024. InjecAgent:
Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language
Model Agents. InFindings of ACL.
[43] Chong Zhang, Xinyi Liu, Zhongmou Zhang, et al. 2026. When AI Meets Finance
(StockAgent): A Benchmark for Simulating Large Language Model Behaviors in
Controlled Trading Environments.ACM TIST(2026).
[44] Hanrong Zhang, Jingyuan Huang, Kai Mei, et al. 2025. Agent Security Bench
(ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based
Agents. InICLR.
[45] Wentao Zhang, Lingxuan Zhao, Haochong Xia, et al. 2024. A Multimodal Foun-
dation Agent for Financial Trading: Tool-Augmented, Diversified, and Generalist.
InKDD.
[46] Shuyan Zhou, Frank F. Xu, Hao Zhu, et al . 2024. WebArena: A Realistic Web
Environment for Building Autonomous Agents. InICLR.
A Schema Excerpts
Listing 1 shows the typed record for the Portfolio Manager’s deci-
sion and for a self-evolution proposal; the CoT steps of every agent
are in Appendix B.
Listing 1: Excerpts of the typed record (src/models.py). Every
CoT step is mandatory; the proposal type cannot name a
protected agent.
classReasoningChain(BaseModel): # Portfolio Manager CoT
macro_filter:str=Field(min_length=1)
news_check:str=Field(min_length=1)
earnings_check:str=Field(min_length=1)
signal_conflicts:str=Field(min_length=1)
sizing_logic:str=Field(min_length=1)
portfolio_balance:str=Field(min_length=1)
cash_target:str=Field(min_length=1)
classTargetPosition(BaseModel): # intent, not shares
symbol:str
target_weight_pct:float=Field(ge=0, le=20) # cap in the type
thesis:str
conviction:Literal["high", "medium", "low"]
thesis_invalid_if:str# named exit condition
MetaReflectionAgentName =Literal[ # no risk_manager,
"tech_analyst", "news_analyst", # no position_reviewer
"macro_analyst", "earnings_analyst",
"portfolio_manager", "evening_analyst"]
classPromptLearning(BaseModel): # a proposed self-edit
agent_name: MetaReflectionAgentName

Feng et al.
operation:Literal["append", "retract"]
learning_text:str=Field(min_length=20, max_length=300)
justification:str=Field(min_length=40) # must cite numbers
B Agent Chain-of-Thought Schemas
Every LLM agent’s output model contains a nested chain-of-thought
(CoT) object whose fields are the reasoning steps the agent must per-
form, in order. Each step is declaredstr = Field(min_length=1) ,
so a missing or empty step fails validation and the response is re-
tried; the steps are therefore not a prompting hint but part of the
output contract, and they are persisted verbatim with the decision.
Table 5 lists the mandatory steps of each agent’s CoT as they appear
in src/models.py. The News Intelligence agent is the one agent
without a CoT: its structured output (a persistent macro narrative,
a list of typed state changes with conviction, and per-symbol alerts)
isits reasoning structure. The Portfolio Manager’s CoT additionally
carries two optional steps, continuity_check (consistency with
its own last three decisions) and premortem_check (the strongest
argument against its largest position), which the prompt requires.
Table 5: Mandatory chain-of-thought steps per agent (field
names of the Pydantic CoT models).
Agent CoT steps, in order
Tech Analyst (5)trend (price versus moving averages) →momentum (RSI, MACD) →
volatility (Bollinger position, ATR)→volume (confirming or diverging)
→support_resistance (levels, valuation flags). Output: rating, conviction,
entry, stop, target, thesis_invalid_if; risk/reward is computed, not written.
Macro Analyst (6)volatility_analysis→yield_curve_analysis→
monetary_policy_analysis→inflation_labor_credit→
cross_signal_synthesis→sector_implications . Output: regime,
confidence, target exposure, sector stances, regime-shift flag.
Earnings Analyst
(5)
fundamental_quality→growth_trajectory→strategic_risks→
management_execution→valuation_context . Output: sentiment and con-
viction derivable from the steps.
Portfolio Manager
(7 + 2)
macro_filter→news_check→earnings_check→signal_conflicts
→sizing_logic→portfolio_balance→cash_target ; optional
continuity_check, premortem_check. Output: TargetPosition intent per
symbol.
Risk Manager (6)rr_audit→signal_fidelity→correlation_check→event_risk→
sizing_sanity→overall . Output: approve or reject, per-symbol modifica-
tions,scale_all_buys, reason category.
Position Reviewer
(6)
macro_continuity_check→thesis_progress_check→
thesis_integrity_check→winners_discipline_check→
session_disposition_check→execution_rationale . Output: HOLD,
REDUCE, SELL or TRAIL_STOP per position.
Evening Analyst
(7)
performance_attribution→outlook_retrospection→
thesis_health_review→decision_quality_review→
calibration_meta→market_regime_read→tomorrow_preparation .
Output: trade grades, thesis trajectories, missed opportunities, next-day bias.
Meta Reflector (7)performance_vs_benchmark→secular_theme_audit→
loss_autopsy_audit→self_portrait_synthesis→
portrait_gap_diagnosis→existing_prompt_audit→
prompt_edit_reasoning. Output: PromptLearning proposals, blind
spots, confidence.
News Intelligence
(–)
No CoT; typed output of macro narrative, state changes and per-symbol alerts.
C Gate Invariants
The proposal schema and the deterministic prompt editor enforce
the following on every proposed learning, independently of the
LLM: (1) append-only into a markedLearningssection, each entry
tagged with quarter and content hash; (2) an allow-list of target
agents, with the Risk Manager and Position Reviewer excluded both
here and in the proposal schema’s Literal; (3) length ceiling (300
characters; 200 before the Q3 cycle) and justification floor; (4) a
word-boundary prohibited-word tripwire (never,always,override,
ignore all,must always,must never); (5) Jaccard token-similarity
dedup against existing entries (threshold 0.6); (6) a per-agent FIFO
cap that evicts the oldest auto-added entry; (7) a per-cycle cap on
the number of agents edited; (8) atomic file writes; (9) an audit
log of accepted and rejected proposals with reasons; (10) one git
commit per cycle, skipping any prompt file with uncommitted
human edits so that the commit stays cleanly revertible; (11) single-
line, whitespace-normalised entries; (12) an apply-from-file lane so
that a human-reviewed proposal file, not a fresh reflection, is what
gets applied.
D Sessions, Latency and Cost
Table 6 lists the daily sessions; Figure 4 gives wall-clock and cost
from the trace: the morning session, which runs four analysts, the
Portfolio Manager and the Risk Manager, takes ten minutes at the
median and always finished within the 20-minute session limit;
half of the cost is the Technical Analyst scoring the whole universe
each morning.
Table 6: Daily sessions (US Eastern, Mon–Fri). “LLM” marks
sessions that call language models.
Window Session LLM Scope
08:00–09:15 earnings_preprocess✓analyse newly filed 10-Q/10-K
09:30–12:00 morning✓ research, decide, risk-check, execute; the
only session that may buy
09:30–16:00 intra_check (30’) – 3% daily-loss circuit breaker
13:00–14:30 midday✓sell-only review (patient)
15:30–16:00 close✓sell-only review (act on hard triggers)
20:00–22:00 evening✓ reconcile fills; grade trades and forecasts;
write insights
quarter end meta✓ self-portrait over 90 days; propose learn-
ings; governed apply
MorningMiddayCloseEvening
0
5
10
15
20Session wall-clock (min)
time limit
a
0 100 200
Logged API cost (US$)
Meta Reflector
Risk Manager
Earnings Analyst
Macro Analyst
Position Reviewer
Evening Analyst
Portfolio Manager
News Intelligence
Tech Analyst
0.2
6.1
16
18
18
24
48
106
220
b
Figure 4: (a) Session wall-clock; dashed line, the session time
limit. (b) Logged API cost per agent over the deployment (a
lower bound: per-call cost logging began on May 12).
E Additional Evaluation Material
Every table and figure below is computed from the recorded trace
by our evaluation scripts.

Governed Self-Evolution for Autonomous Investing
Scoring and simulation.Forward returns are close to close over
1, 5, 10 and 20 trading days and are market-adjusted by subtracting
SPY’s return over the same horizon. Means are taken first within
each day and then across days, so that a day with many ratings
counts once, and standard errors are computed on the daily means.
The rank IC is the daily Spearman correlation between a signal and
the market-adjusted forward return, on days with at least eight
scored symbols. The policy-layer simulations of Table 1 hold each
recorded target from the decision day’s close, cap a name at 20%
and the book at 100%, and earn the T-bill ETF’s return on idle cash.
With system exits they apply the Technical Analyst’s stop from
the entry day or the three days before it (8% below entry if none)
and the Position Reviewer’s recorded SELL, REDUCE (halving) and
TRAIL_STOP actions; with the Risk Manager, a rejected plan sets
no targets and its recorded allocation edits and scale factors are
applied. The analyst-following baselines put 5% in every name rated
buy (or high-conviction buy), up to 70% of equity.
Analyst signals and forecasts (RQ1).Figure 5 scores analyst out-
puts against market-adjusted forward returns.
1 d 5 d 10 d 20 d
Horizon
−3
−2
−1
0
1
2
3
Market-adj. fwd return (%)
a
Technical rating
Sell Neutral Buy
1 d 5 d 10 d 20 d
Horizon
−0.10
−0.05
0.00
0.05
0.10
0.15
Mean daily rank IC
b
Technical rating
News sentiment
Figure 5: Analyst signal quality. (a) Market-adjusted for-
ward return after each Technical Analyst rating. (b) Mean
daily Spearman rank IC between signal and forward market-
adjusted return. Mean and 95% interval, day-clustered.
Exits (RQ1).Table 7 splits the 438 broker round trips by exit
mechanism.
Table 7: Exit quality. Post-exit 20d: the sold symbol’s 20-day
return after exit minus SPY’s (“correct” if negative); Left:
further gain to the end of the study.
Post-exit 20d
Exit Lots Win Realised Hold (d) Excess Correct Left (US$k)
Agent decision 306 51%+0.45% 9.6+0.44% 42% 19.9
Mechanical stop 132 39%+2.29% 15.3+4.06% 45% 0.7
All 438 47%+1.01% 11.4+1.27% 43% 20.6
Self-evolution (RQ3).Table 8 details the Q2 replay, Table 9 the Q3
replay and Table 10 the evening-loop correlations. The Q2 replay
feeds recorded mornings through the Portfolio Manager prompt
with and without the withheld learning; the Q3 replay runs frozen
evening inputs through the Evening Analyst prompt before and
after the commit, two samples each, where a trigger evening has
a symbol classified as a missed value entry or trend timing on at
least three of the last ten evenings.
Table 8: Replay of the withheld Q2 learning on the Portfolio
Manager. Flag.: flagged BUYs; Base: of which the baseline
still proposed; Kept: within±1 point.
Learning vs. baseline
Mornings Flag. Base Kept Red. Incr. Drop. Added
Wrong BUYs (10 d) 15 10 8 1 1 0 1
Control BUYs (5 d) 14 12 8 3 1 0 0
Summed weight of flagged BUYs, wrong mornings: 59.6% → 63.5%; control: 72.5%→ 67.3%.
Re-running the baseline itself moves a flagged weight by 1.8pp at the median (𝑛=7 pairs). 35 LLM
calls, US$17.
Table 9: Replay of the applied Q3 learning on the Evening
Analyst. Recurring named: recurring missed symbols named
in suggested actions; TAKE/W AIT, Blocker: replays with an
explicit call or a named blocker.
Evenings Prompt Replays Recurring named TAKE/WAIT Blocker
Trigger (10) base 20 26/64 0/20 0/20
+ learning 20 25/64 3/20 4/20
Control (4) base 8 0/2 0/8 0/8
+ learning 8 0/2 0/8 0/8
Table 10: Evening loop: Spearman correlations between trail-
ing code-computed grades and next-morning behaviour, with
raw and Holm-corrected𝑝-values.
Relation (Spearman)𝜌 𝑝 𝑝 Holm 𝑛
New BUY weight∼trailing 10-evening forecast hit rate−0.14 0.32 1.00 54
Number of BUYs∼trailing forecast hit rate−0.11 0.41 1.00 54
New BUY weight∼RM cuts in last 5 sessions−0.08 0.49 1.00 82
New BUY weight∼trailing 45-day realised win rate+0.02 0.89 1.00 80
Book exposure∼trailing 45-day realised win rate+0.22 0.05 0.32 80
Book exposure∼trailing forecast hit rate+0.34 0.01 0.08 54
Containment and grounding (RQ4, RQ5).Table 11 and Figure 6
give the 2015–2026 backtest of the deterministic core; Table 12 gives
the grounding audit by agent.
Backtest protocol.Entries are rebalanced on the first trading day
of each week to ten names at 9% each: the top ten by 126-day
return skipping the last five days (momentum), or ten names drawn
uniformly (random, 50 seeds). Without the core, the book holds
10% per name, fully invested, with no stop, cap or breaker. The
core applies a stop at entry minus two ATR(14), triggered on the
daily low and filled at the lower of the open and the stop; a 40%
GICS sector cap; at most 90% net exposure; the cash-only rule; and
a breaker that liquidates at the close after a day of−3%or worse
and re-enters at the next open. Stopped names stay flat until the
next rebalance. Trades cost 5 bp per side, and idle cash earns a T-bill
ETF.

Feng et al.
Grounding protocol.The audit samples up to 150 CoTs per agent
and extracts every number in their reasoning fields, excluding small
integers and years. A number is grounded if it occurs in the agent’s
input message, in any historical version of its prompt or in its
own emitted fields, allowing rounding and truncation; the derived
matcher also accepts risk/reward ratios, ATR multiples, percentage
changes, weights and stop levels computed from those values, and
arithmetic written out in the text. The placebo pairs each CoT with
the input of another row of the same agent, half the sample apart
in time; because two-digit numbers such as 25% or 1.5 match by
chance, the placebo is reported on numbers with three or more
significant digits.
Table 11: Backtest of the deterministic core alone, 2015–2026,
on the 80 single stocks of the universe with LLM-free weekly
entries (top 10 by 126-day momentum, or random over 50
seeds). Core: the rules of §4.3; ablations remove one. CAGR
and drawdowns in %; 5 bp per side. The universe is from 2026,
so only comparisons between variants are meaningful.
Crisis drawdown
Entries / variant CAGR Sharpe Max DD 2018 2020 2022 2026
Momentum entries
No core+61 1.15−61−25−36−27−46
Stops only+58 1.12−61−25−29−27−51
Core−stops+40 1.26−36−20−36−21−27
Core−breaker+50 1.09−60−23−25−19−39
Full core+41 1.30−33−18−30−18−27
Random entries, median of 50 seeds
No core+17 0.81−37−20−35−26−8
Full core+14 0.82−28−17−27−21−7
SPY+14 0.82−34−19−34−24−3
2016 2018 2020 2022 2024 2026
−60
−40
−20
0
Drawdown (%)
a Momentum, no core Momentum, core SPY
2018
Q4
COVID
2020
2022
bear
2026
semis
0
20
40
60Window drawdown (%)
b
No core, momentum
Core, momentum
No core, random entries
Core, random entries
Figure 6: Deterministic core, 2015–2026. (a) Drawdown of
momentum entries without and with the core, and of SPY;
shaded, crisis windows. (b) Drawdown per window: median
and 5–95% range over 50 random seeds; diamonds, momen-
tum.
Replay noise.The deployed design runs twice per morning to
measure re-run noise.
Table 12: Number-grounding audit of recorded CoTs.
Grounded: cited numbers found in the agent’s input, prompt
or own fields, including derived quantities; Strict: exact or
rounded matches only; Placebo: strict grounding against an-
other day’s input.
Agent Rows Numbers Grounded Strict Placebo
Portfolio Manager 133 7,827 99.69% 98.85% 41%
Risk Manager 75 979 99.59% 91.52% 18%
Macro Analyst 137 3,457 99.94% 99.28% 9%
Technical Analyst 150 233,310 99.94% 95.85% 23%
Position Reviewer 150 3,155 99.40% 98.07% 21%
Evening Analyst 105 5,366 99.27% 98.53% 17%
All 750 254,094 99.91% 96.06% 22%
F Web Input, Taxonomies and Failure Handling
Web input.RSS items are deduplicated by normalised URL and
then by title-word Jaccard similarity above 0.7, their summaries are
truncated to 300 characters, and at most 50 items enter the News
agent’s prompt. Filing text is parsed from HTML and capped at
30,000 characters. The Portfolio Manager receives at most three
news items per symbol, each reduced to its conviction, sentiment
and impact summary, with no headline. Every news state change
is checked by code against the session’s input and the prior state,
and dropped if none of its keywords or symbols occurs there.

Governed Self-Evolution for Autonomous Investing
Evening taxonomy.A wrong BUY carries one of nine root causes:
greed or top chasing, macro warning ignored (which must cite
the warning), herd buying, averaging down, broken thesis held,
concentration, timing, systemic drawdown and tail event, together
with a thesis trajectory (strengthening, intact, weakening, broken).
A missed move is classified as a trend-timing miss, a theme blind
spot, a fundamentals mispricing, a missed value entry, a noise
rally or a risk-disciplined pass; the last two are not counted as
misses. The Risk Manager labels each verdict with one of ten reason
categories (for exampleoversized,rr_fail,concentration,event risk,
data degraded), which L5 feeds back to the Portfolio Manager.
Failure handling.Table 13 lists how the system contains each
class of failure. The rule throughout is that a failure removes an
action rather than adding one.
Table 13: Failure classes and the system’s response.
Failure Response
Transient LLM error (429, 5xx) up to 7 retries with backoff, then one call to a second vendor’s
model
Unparseable or invalid output the agent’s output is dropped; invalid list items are dropped
singly
Research agent fails recorded as degraded; two degraded sources raise a Risk
Manager advisory
Portfolio Manager fails session aborts without orders; the next 30-minute tick retries
Risk Manager fails the plan is rejected (fail closed)
Position Reviewer fails no exit actions; broker-held stops remain
Evening Analyst fails P&L is recorded; no grades are written
Crash between order and record write-ahead record and reconciliation of orphans
Stale entry price (>5% from market) the BUY is skipped
Daily loss beyond 3% no new buys; the circuit breaker cancels entries and liqui-
dates
Session overrun killed after 20 minutes; at most one run per session per day
Ablations.With momentum entries the core’s drawdown is 36%
without stops and 60% without the breaker (33% in full).
