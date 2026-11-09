---
title: 'AutoVend: Benchmarking LLM Agents on Long-Horizon Autonomous Vending Operations'
url: https://arxiv.org/abs/2610.36980
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Qiming Shi
- Yikun Li
- Beidi Luan
- Rui Sun
- Yan Ma
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.36980
pages: 16
chars: 58792
fetched_at: '2026-11-08T13:35:52+00:00'
kb_version: 1
---

# AutoVend: Benchmarking LLM Agents on Long-Horizon Autonomous Vending Operations

AutoVend: Benchmarking LLM Agents on Long-Horizon Autonomous
Vending Operations
Qiming Shi1,2*, Yikun Li1,3*, Beidi Luan1, Rui Sun1, Sinuo Wang4, Delin Wang5,
Yan Ma1,Jing Li 1,Daxin Jiang 1,Zuo Bai 1,6†
1StepFun, 2Zhejiang University, 3Xi’an Jiaotong-Liverpool University,
4University of Adelaide, 5Renmin University of China, 6FinStep
qimingshi@zju.edu.cn,Yikun.Li26@student.xjtlu.edu.cn,
a1713814@adelaide.edu.au,wdl2025@ruc.edu.cn,
{luanbeidi,sunrui,mayan,futureli,djiang,baizuo}@stepfun.com
Abstract
Large language model (LLM) agents are extending
agent-mediated commerce on the Web from shopping
for consumers to operating businesses for sellers. In
online-to-offline (O2O) commerce, decisions are is-
sued through Web-based platforms but realized through
costly physical execution. Evaluating such agents
requires going beyond individual transactions to ask
whether decisions made online turn into sustained eco-
nomic returns. We introduce AutoVend, a benchmark in
which one LLM agent manages 20 vending machines
across five site types through a Web-based operating
interface for 180 simulated days. Its data-grounded sim-
ulator combines a shared warehouse, procurement lead
times, paid replenishment, inventory expiration, and re-
curring operating costs. We evaluate five LLM agents
against a rule-based inventory-control baseline and diag-
nose their site coordination, execution, and performance
over time. Four of five evaluated LLM agents fall short
of this baseline, and returns per dollar of inference cost
rank models differently from returns alone. Operational
analyses show that gains in individual metrics do not
consistently yield stronger economic growth, as inven-
tory and execution costs erode these gains. Trajectory
analysis further reveals difficulties in grounding fea-
sible actions, managing inventory commitments, and
converting feedback into effective policy revisions.
1 Introduction
Agent-mediated commerce is emerging as a Web
application domain for large language model
(LLM) agents, with buyer-side research spanning
product discovery (Yao et al., 2022), personalized
shopping (Kim et al., 2026), and customer sup-
port (Wang et al., 2025). Seller-side autonomy re-
quires repeated decisions about assortment, pricing,
procurement, and inventory whose consequences
* Equal contribution. Work done during an internship at
StepFun.
† Corresponding author: Zuo Bai
(baizuo@stepfun.com).
Web-based operations
LLM agent
Assortment Pricing
Procurement Replenishment
20 machines · 5 site types
Lead time Paid visits
Factory Commercial
Campus
Residential
Office
Shared inventory and cash
SHOP
$
Sales and costs
Day t Day t+1 …
1 2 3Cross-site Resource
Coordination
Local demand,
shared resources
Physical Execution
Planning
Lead times and
paid visits
Continual Strategy
Improvement
Revise decisions
from feedback
Decisions
Figure 1: AutoVend connects Web-based agent deci-
sions to distributed physical retail through shared inven-
tory, procurement lead times, and paid on-site replenish-
ment.
extend beyond an individual interaction (Shi et al.,
2026; Fan et al., 2026). In online-to-offline (O2O)
commerce, decisions are made on Web-based man-
agement platforms, while their economic returns
depend on the costs and constraints of physical
execution. For agents managing distributed retail
through such platforms, this requires coordinat-
ing digital decisions with physical execution over
time. Smart vending is a compact instance, as
connected machines are increasingly run through
cloud management platforms (Fortune Business In-
sights, 2026) while every restock requires a paid
site visit. It also retains the dependencies among
assortment, inventory, execution, and cash manage-
ment. For Web economics, AutoVend thus provides
a controlled testbed for seller-side agent-mediated
commerce that measures both the returns an agent
generates through a Web-based interface and the
inference cost of generating them.
Sustaining performance in this setting requires
three interdependent capabilities.(1) Cross-
site Resource Coordination.The agent must
match heterogeneous local demand while allocat-
1
arXiv:2610.36980v2  [cs.AI]  5 Nov 2026

ing shared resources and monitoring conditions
across the network (Eppen, 1979). An allocation to
one site changes the resources available to others,
so local decisions must account for consequences
across the network.(2) Physical Execution Plan-
ning.Stock in a shared warehouse cannot meet
local demand until it is placed on machine shelves.
Procurement requires advance ordering to account
for delivery lead times, while on-site replenishment
incurs visit costs. The agent must coordinate ad-
vance orders and site visits to maintain product
availability while controlling execution expenses,
storage costs, and expiration losses (Coelho et al.,
2014; Nahmias, 1982).(3) Continual Strategy
Improvement.Demand is initially unknown, and
observed sales depend on the agent’s own assort-
ment, prices, and stock availability. The agent must
use accumulated feedback to refine its demand es-
timates and revise its decision rules so that sub-
sequent decisions become more effective (Zhang
et al., 2026; Shi et al., 2026).
Existing benchmarks provide important founda-
tions for evaluating long-horizon business agents.
Vending-Bench studies the operation of a single
vending machine and simulates physical tasks
through a separate execution agent (Backlund and
Petersson, 2025). RetailBench evaluates supermar-
ket operation with inventory aging, delayed deliver-
ies, and cash-flow constraints (Zhang et al., 2026).
MerchantBench examines seller-side e-commerce
under mixed-latency feedback (Shi et al., 2026),
while E-Commerce Bench extends business evalu-
ation to multiple online stores with pooled inven-
tory, fulfillment costs, and delayed settlements (Fan
et al., 2026). These evaluations do not establish
how effectively agents can coordinate shared in-
ventory across heterogeneous physical retail sites
when on-site replenishment itself incurs costs and
delays. Assessing this capability requires an envi-
ronment that brings these constraints together and
exposes their cumulative economic consequences.
We introduceAutoVend, a benchmark for eval-
uating LLM agents on long-horizon autonomous
vending operations. A single agent manages 20
vending machines spanning factory, campus, resi-
dential, commercial, and office locations, with het-
erogeneous demand and a shared warehouse. The
agent selects products, sets prices, places procure-
ment orders, and arranges replenishment through
tool calls that mirror such a platform. The simu-
lator models procurement lead times, paid on-site
stocking, product expiration, and storage charges
on warehouse stock. These mechanisms connect
decisions made through the interface to inventory
availability and subsequent economic outcomes.
AutoVend combines terminal net assets with op-
erational metrics and trajectory diagnostics. We
examine site coordination, the cost and availability
of paid replenishment, and changes in operating
performance over time. Our contributions are three-
fold.
• We introduce AutoVend, a benchmark for
long-horizon seller-side agent-mediated com-
merce, with a unified task, operating interface,
and evaluation protocol for managing a dis-
tributed retail network.
• We develop a simulator grounded in real vend-
ing records that models heterogeneous de-
mand, procurement lead times, inventory ag-
ing, and paid site visits, and validate its de-
mand behavior against observed sales pat-
terns.
• We evaluate five LLM agents and find that
four of five fall short of a rule-based inventory-
control baseline. Operational diagnostics and
trajectory analyses reveal difficulties in coor-
dinating inventory commitments, execution
costs, and policy revision.
2 Related Work
Agent Evaluation in Commerce.Commerce is
a prominent domain for evaluating LLM agents
on the Web, with benchmarks for online shop-
ping (Yao et al., 2022; Peeters et al., 2026;
Kim et al., 2026), customer service (Yao et al.,
2025; Wang et al., 2025), and multi-agent mar-
kets (Bansal et al., 2025; Zheng et al., 2026). Their
evaluations typically end with a completed task,
dialogue, or transaction, whereas a seller’s deci-
sions affect inventory and cash long after they
are made. Seller-side benchmarks instead eval-
uate the sustained operation of a business mainly
by its accumulated economic outcome. Merchant-
Bench and StoreBench each cover a single online
store (Shi et al., 2026; Raghuvanshi et al., 2026),
Business Arena a single cross-border shop (Pan
et al., 2026), and E-Commerce Bench up to four on-
line stores that share a warehouse (Fan et al., 2026).
In physical retail, RetailBench covers a single su-
permarket (Zhang et al., 2026) and Vending-Bench
a single vending machine (Backlund and Petersson,
2025), a setting that Vending-Bench 2 extends to a
2

simulated year and its Arena to several competing
agents with one machine each (Andon Labs, 2025).
AutoVend instead provides a controlled setting in
which one agent operates 20 heterogeneous sites
from a shared warehouse and every on-site action
requires a paid visit (Table 1).
Long-Horizon Agent Evaluation.Long-
horizon benchmarks commonly lengthen the work
toward a defined goal, as in workflows on web-
sites and computers (Zhou et al., 2024; Yuan et al.,
2026), tasks in a simulated company (Xu et al.,
2025), and exploration of partially observable envi-
ronments (Luo et al., 2026). Sustained-operation
benchmarks instead fix a span of simulated calen-
dar time in which costs accrue and the environ-
ment evolves whether or not the agent acts, so
performance is an accumulated economic result
rather than goal completion (Backlund and Peters-
son, 2025; He et al., 2026). Because terminal out-
comes alone reveal little about why agents succeed
or fail, evaluations add progress rates (Ma et al.,
2024), capability profiles across operating dimen-
sions (Fan et al., 2026), and attribution of gains
and losses to actions (Pan et al., 2026). Continual-
learning benchmarks further ask whether agents
turn accumulated experience into reusable capa-
bilities (Zheng et al., 2025; Cheng et al., 2026).
AutoVend ties its operational dimensions to indi-
vidual sites and on-site execution and examines
how performance changes across operating scales
and over time.
3 The AutoVend Benchmark
AutoVend places an LLM agent in charge of a net-
work of vending machines over a long operating
horizon (Figure 2). The agent sets assortment and
prices, orders stock, and arranges on-site replenish-
ment, while customer demand is grounded in real
operating data and hidden from the agent.
3.1 Task Formulation
An agent operates 20 vending machines that share
one warehouse and draw on a catalog of 1,372
products over 180 simulated days, starting with
40,000 CNY in cash. We formulate the task as
a partially observable Markov decision process
(POMDP) (Kaelbling et al., 1998). The underlying
state st comprises the simulation date, cash, inven-
tory, outstanding orders, machine assortments and
prices, and hidden demand conditions. An action
at ∈ Adenotes a tool invocation. When the agent
ends the day’s actions, the simulator settles sales
and costs and advances to the next day. The obser-
vation kernel Z(o t+1 |s t+1, at) exposes daily op-
erating summaries and tool results, while demand
parameters and unmet demand remain hidden.
The objective is to maximize terminal net assets,
NAT =B T +
X
k
ckhk,T ,(1)
where T is the terminal interaction step at the end
of the operating episode, Bt is cash, ck is the unit
cost of product k, and hk,t counts the unexpired
units of k on shelves, in the warehouse, or in tran-
sit. Buying stock converts cash into inventory at
cost, so net assets change through sales, operating
costs, fines, and inventory write-offs from expira-
tion or disposal. With underlying demand and its
response parameters hidden, the agent can refine
its assortment, pricing, and replenishment strategy
using feedback accumulated during operation.
3.2 World Simulator
Network and operations.The network comprises
six worksite, two campus, four residential, six com-
mercial, and two office machines, with differences
in product preference, price sensitivity, and holiday
response. Each machine holds at most 200 units
and is replenished from one shared warehouse. Pro-
curement is paid at placement. Orders arrive in the
warehouse three days after placement. Staff are
available for on-site visits on working days, and
multiple visits can be made within a day. Replen-
ishment and removal of shelf stock require physi-
cal execution through an on-site visit, which costs
35 CNY per machine per day regardless of the
number of operations.
Inventory aging and costs.Batches expire 30
or 90 days after warehouse arrival. Selling expired
products incurs a fine of 1,000 CNY per unit sold.
Warehouse rent is 0.03 CNY per unit per day, and
machine rent is 4 CNY per machine per day. The
agent must balance stock availability against stor-
age costs and expiration risk, since excess inventory
incurs recurring charges and may expire before it
is sold.
Customer demand.Demand is generated sepa-
rately for each machine, with temporal dependence
introduced by persistent daily shocks. The attrac-
3

Table 1: Comparison with long-horizon business operation benchmarks. Op. Units counts the operating units
managed by one agent. Diverse Types marks whether these units differ in type. Real Data marks whether the
environment is grounded in real commercial datasets. Physical Ops. marks whether actions require physical
execution. Open Source marks public release, upon publication for AutoVend.
Benchmark Domain Op. Units Diverse Types Real Data Physical Ops. Open Source
RetailBench (Zhang et al., 2026) Supermarket 1✗ ✓ ✗ ✓
MerchantBench (Shi et al., 2026) E-commerce 1✗ ✓ ✗ ✓
StoreBench (Raghuvanshi et al., 2026) E-commerce 1✗ ✗ ✗ ✗
E-Commerce Bench (Fan et al., 2026) E-commerce≤4✓ ✓ ✗ ✓
Vending-Bench (Backlund and Petersson, 2025) Vending 1✗ ✗ ✓ ✗
AutoVend (ours)Vending 20✓ ✓ ✓ ✓
tion of productkon machinemis
wm,k,t =b m,k F η m,t min  1, qm,k,t ϕ 
×
 pm,k,t
¯pk
−εℓ(m)
Em,k,t,
(2)
where bm,k is a base attraction, Fm,t the filled frac-
tion of capacity, qm,k,t the shelf stock, pm,k,t the
price, ¯pk the reference price, and εℓ(m) the price
elasticity of the site type. Fuller machines attract
more customers (Balakrishnan et al., 2004), and an
item displayed with fewer than ϕ= 5 units loses
attraction proportionally. The multiplier Em,k,t
captures temperature, rain, and holiday effects. Pur-
chases follow
Nm,t ∼Poisson

ξm,t
UmWm,t
Um +W m,t

,
Wm,t =
X
k
wm,k,t,
(3)
Here, Nm,t counts purchase attempts, and Um is
the machine-specific weight assigned to the op-
tion of buying nothing. Each purchase attempt
selects product k with probability wm,k,t/Wm,t.
This implements a multinomial logit model with a
no-purchase option (Talluri and van Ryzin, 2004).
The random multiplier ξm,t averages one and is
positively correlated across days, allowing demand
fluctuations to persist and increasing variability be-
yond Poisson sampling. Sales equal the minimum
of sampled demand and shelf stock, and unmet
demand is lost.
3.3 Real-World Data Grounding
Data.We build the simulator from six months of
order-level sales records covering 99 machines op-
erated by a commercial smart vending company
(Appendix C), totaling 220,128 units sold. We se-
lect 20 machines across five site types to construct
the simulated network operated by the agent. The
catalog keeps 1,372 products in 18 subcategories,
covering 89.3% of units sold.
Parameter calibration.The base attraction in
Eq. (2) factorizes as
bm,k =κ m πℓ(m),g1(k) γg2(k) ωk,(4)
where g1(k) and g2(k) are the category and sub-
category of product k. The product popularity ωk
is the number of units sold per unit of exposure,
computed from sales records and shrunk toward its
subcategory mean by empirical Bayes. Exposure
counts a machine’s days of offering the product
weighted by its sales level. The site preference
πℓ,g1 compares the drink and snack mix of labeled
machines with the mix expected from the products
they actually sold, so that stocking choices are not
mistaken for site effects. The coefficients γg2 align
predicted subcategory shares on real shelves with
realized shares. The scale κm sets the expected
units of a typical real shelf at reference prices and
neutral weather equal to the machine’s observed
mean daily units.
The no-purchase weight is Um =u Rm with
u=xe/(1−e) , where x is the geometric mean
ratio between the attraction of real shelves and that
of a fully stocked reference shelf, e is the elas-
ticity of daily units with respect to shelf attrac-
tion estimated within machines, and Rm is the
attraction of the reference shelf. The reference
shelf sorts products by bm,k and places ϕ units
of each until capacity is full. With x= 0.0638
and e= 0.318 , a typical real shelf sells the ma-
chine’s observed mean daily units, and a fully
stocked reference shelf sells about 1.42 times that
amount. The shock is ξm,t = exp(σum,t −σ 2/2)
with um,t = P5 j=0 ρjzm,t−j/ qP j ρ2j, where
zm,t are independent standard normal draws and
4

Agent and interface World simulator
Goods and inventory flow
LLM agent
Persistent
memory
Tool
calls
Tool
feedback
Actions
MCP tool interface
Remote operations
Query · Order · Price · End day
Physical execution
Stock shelves · Return stock
Memory
Read · Update notebook
Supplier
In transit
Lead time Shared warehouse
Paid visits
20 machines · 5 site types
Factory Campus Residential Commercial Office
SHOP
Operating state
Cash Shelf and warehouse stock Outstanding orders Inventory age and costs
Demand model
Local preference
Site type · Product popularity
Price
Relative price · Site sensitivity
Display
Assortment · Fill level · Facing
Weather and calendar
Temperature Rain Holidays
Product
attraction
Purchase
attempts
Product
choice
Relative attraction
Stock limit
Available shelf stock
Realized sales
Demand parameters hidden from agentObservations and tool results
Daily interaction loop
Arrivals and
recurring fees
Daily
observation
Query / Act
Tool feedback
>_ end_day Sales and visit costs Next day
Repeat for 180 days
(a) (b)
(c)
Figure 2: Overview of AutoVend. (a) Agent and interface, with MCP tools for remote operations, physical execution,
and persistent memory. (b) World simulator, connecting a shared warehouse to 20 machines across five site types
and generating sales through a data-grounded demand model with hidden parameters. (c) Daily interaction loop,
from arrivals and recurring fees through agent queries and actions to sales and visit-cost settlement, followed by
advancement to the next day.
σ2 = ln(1 + 1/r). The dispersion r= 2.74 is the
median overdispersion m2/(v−m) of daily units
after removing weekday patterns, and ρ= 0.21 is
the lag-one residual autocorrelation. The nested
structure of the choice model keeps one nest per
subcategory with similarity parameter λ= 1 , at
which the model reduces to the multinomial logit
form used above.
Margins, shelf lives, price elasticities, environ-
mental responses, and operating costs are bench-
mark settings. We set the fill exponent to η= 0.5 ,
the facing threshold to ϕ= 5 units, and site-
specific price elasticities between 2.4 and 3.5. Unit
costs use assumed gross margins of 30–40% for
drinks and 50–60% for snacks.
Validation.We re-estimate all data-derived pa-
rameters from records preceding an eight-week
test window and evaluate the demand model on
67 machines. We reconstruct daily shelves from
inventory records for 67 machines. We replay
these shelves at reference prices and under neu-
tral weather, comparing simulated with realized
sales over 100 seeds (Figure 3).
Let vt denote the realized sales for machine-
week observation t. The weighted absolute per-
centage error is
W APE =
P
t|vt −ˆvt|P
t vt
,(5)
where ˆvt is the simulated counterpart. Subcate-
gory fidelity is measured by the total variation dis-
tance between simulated and realized subcategory
shares, and product ranking by the Spearman corre-
lation between simulated and realized product sales
within a machine. The persistence reference sets ˆvt
to each machine’s mean weekly sales over the pre-
ceding four weeks, and the naive reference keeps
each machine’s earlier sales level and spreads it
uniformly over the products on its shelf. Two abla-
tions show which components matter, removing the
overdispersed shock and replacing the estimated
popularity with a uniform weight.
Total volume is reproduced within 0.7%, with a
machine-week weighted absolute percentage er-
ror (WAPE) of 0.473 against 0.606 for a naive
reference and 0.561 for a persistence reference
that carries forward the preceding four weeks of
real sales. The total variation distance (TVD) be-
tween simulated and realized subcategory shares
is 0.153, compared with 0.206 for the naive ref-
erence. Within machines, the median Spearman
5

100 101 102 103
Simulated units
100
101
102
103
Realized units
Worksite
Campus
Residential
Commercial
Office
Unknown
TeaWaterEnergySodaSportsJuiceMilkJerkyNoodlePastryCoffeeCandyCookieOther
0%
5%
10%
15%
20%
25%
30%Share of units sold
Real Sim
(a) Weekly sales per machine (b) Product mix
Figure 3: Held-out evaluation of the demand model on 67 machines over an eight-week test window, averaged
over 100 seeds. (a) Simulated versus realized weekly sales per machine. (b) Subcategory shares of realized and
simulated sales. Subcategories accounting for less than 0.5% of realized sales are pooled into Other, while TVD
uses all original subcategories.
correlation of product sales is 0.577. A uniform
product popularity raises the TVD to 0.238, show-
ing that estimated product popularity improves mix
fidelity. Price and environmental responses remain
unvalidated by design.
3.4 Agent Interface
Interaction loop.AutoVend exposes the remote
operations available to a networked-vending op-
erator as tools over the Model Context Proto-
col (MCP) (Anthropic, 2024), with physical tools
standing in for dispatching staff on site. Each day
begins with due order arrivals and charges for ware-
house rent and fixed operating fees, followed by a
daily observation for the agent. During the action
window, the agent queries operating records and ex-
ecutes actions, receiving query results or execution
feedback after each tool call. Valid actions update
the operating state immediately. When the agent
closes the action window, the simulator realizes de-
mand using the resulting shelf inventory and prices,
settles sales and on-site visit costs, and proceeds to
the next day.
Prompts.A fixed system prompt specifies the
objective, starting conditions, goods flow, operat-
ing costs, inventory and pricing constraints, and
qualitative demand mechanisms without prescrib-
ing an operating strategy. A daily user prompt
updates the date and supplies a compact report of
cash and net assets, recent profit and loss, ware-
house and in-transit stock, upcoming holidays, and
each machine’s inventory, sales, and expiry status.
Product-level details are retrieved through queries
rather than included in the daily prompt. Appen-
dices A and B provide the complete prompts and
tool specifications.
Tools and memory.AutoVend provides 18 tools
organized into three functional groups covering re-
mote operations, physical execution, and persistent
memory.
• Remote operational tools.These support
procurement, machine-specific pricing, ware-
house disposal, and closing the daily action
window. Queries provide product attributes
and costs, warehouse and shelf inventory,
product-level sales within and across ma-
chines, and financial records. Read-only SQL
supports custom analysis of operating records,
while calendar and weather queries provide
published holidays and near-term weather in-
formation.
• Physical execution tools.These transfer
warehouse stock onto machine shelves and
return specified quantities or all remaining
units of a product to the warehouse. Execu-
tion requires paid on-site visits, charged once
per machine per day regardless of the number
of operations.
• Memory tools.These allow the agent to
read and overwrite a persistent notebook con-
taining selected observations, plans, and find-
ings. Conversation history continues across
days, while the notebook survives context
compaction.
6

4 Experiments
4.1 Experimental Setup
Baseline.We evaluate Claude Sonnet 5.5 (An-
thropic, 2026), GPT-6.1 Sol (OpenAI, 2026),
DeepSeek V4.1 Flash (DeepSeek-AI, 2026), Kimi
K3 (Kimi Team, 2026), and GLM-5.3-Flash (Z.ai,
2026). We use the Pi harness (Zechner, 2026) and
configure each model with its highest supported
reasoning effort. Each agent operates the same
20-machine network for 180 simulated days, start-
ing with 40,000 CNY and using identical prompts,
tools, and daily interaction budgets. We report
means and the standard deviation of terminal net
assets over three runs per model, all in one frozen
world with the same random seed. Variation across
LLM runs thus reflects stochastic agent decisions
and the demand draws they induce. The deter-
ministic rule-based baseline attains 208.73±2.26
thousand CNY (CV 1.1%) across seeds 1–3, and
we report seed 1.
The rule-based baseline combines the newsven-
dor critical ratio (Arrow et al., 1951) with periodic
order-up-to replenishment (Silver and Robb, 2008).
It sets inventory targets from rolling 30-day de-
mand and variability estimates, balancing lost sales
against holding and spoilage costs, and replenishes
sites weekly. Procurement accounts for delivery
lead times, available stock, and outstanding orders.
Assortments follow observed sales, while prices
are adjusted through local gross-profit trials. All
decisions use observable information.
Metrics.Our primary outcome,Net Assets, is
terminal cash plus unexpired inventory valued at
cost across shelves, the warehouse, and transit.As-
sortmentcompares expected gross profit with a
heuristic reference mix under common prices, dis-
play volume, and environmental conditions.Waste
Rateis inventory loss divided by valid sales cost
plus loss, counting expiry and early disposal once.
Pricing Regretis the expected gross-profit short-
fall from a price-search reference at a fixed site,
assortment, and inventory.
Shelf Utilizationmeasures the mean fraction of
capacity occupied by unexpired stock before sales
across sites and days. We also report the share of
site-days with empty shelves.Capital Efficiencyis
mean daily gross profit divided by mean inventory
value at cost.Tool Callscounts tool invocations
over the episode.API Efficiencyaverages per-run
net asset growth per USD of estimated API expen-
diture, using standard reference rates for recorded
input, output, cache, and compaction usage.
4.2 Main Results
Overall Performance.Long-horizon business
management remains challenging, with four of five
evaluated models underperforming the rule-based
baseline in Table 2. GPT-6.1 Sol is the sole excep-
tion, while all five models obtain lower assortment
scores than the baseline. All three GPT executions
exceed the baseline, whereas none of the other 12
does, showing that most models’ weak averages
cannot be explained by a few isolated failures.
Variability.Weak average performance is com-
pounded by inconsistent execution. Kimi K3 ex-
hibits a coefficient of variation of 45.6% across
repeated runs. GPT-6.1 Sol, GLM-5.3-Flash, and
Claude Sonnet 5.5 instead exhibit similar relative
dispersion of around 11%, despite their substan-
tially different mean returns. This contrast shows
that consistency and economic effectiveness are
distinct aspects of agent capability.
API Efficiency.Operating returns and inference
efficiency reveal different model rankings. GPT-6.1
Sol achieves the highest terminal assets, whereas
DeepSeek delivers the highest net-asset growth
per dollar of estimated API expenditure. GPT’s
mean estimated API expenditure is approximately
80 times DeepSeek’s, while its net-asset growth is
about 2.9 times as large. GLM-5.3-Flash ranks sec-
ond on both measures. DeepSeek also uses more
tool calls than GLM while achieving higher API
Efficiency, showing that interaction count alone
does not capture inference cost.
5 Analysis
5.1 Operational Performance Profiles
To understand the operational strengths and weak-
nesses underlying the agents’ economic outcomes,
we analyze their performance across five dimen-
sions in Figure 4. No single model leads across
all five dimensions, and stronger profitability does
not consistently coincide with better inventory con-
trol, pricing, or capital efficiency. We examine
these differences below to characterize how each
agent combines product selection, inventory man-
agement, and resource use during long-horizon op-
erations.
Profitability.GPT-6.1 Sol achieves the highest
mean terminal net assets at 309.35 thousand CNY ,
followed by GLM-5.3-Flash at 148.43 thousand
CNY . Kimi K3 achieves the lowest return at 91.52
7

Table 2: Main experimental results on AutoVend. LLM results are averaged over three repeated runs, and Rule-based
reports seed 1. Net Assets and Std are in thousands of CNY . Waste Rate and Shelf Utilization are percentages,
Pricing Regret is in CNY per machine per day, and API Efficiency is net-asset growth in CNY per USD of API cost.
Model Net Assets↑ Std Assortment↑ Waste Rate↓ Pricing Regret↓ Shelf Utilization Tool Calls API Efficiency↑
GPT-6.1 Sol309.3534.09 0.992 0.60 30.18 88.91 3,950 1,117
GLM-5.3-Flash 148.43 16.70 0.817 0.27 2.45 60.65 670 7,023
DeepSeek V4.1 Flash 133.92 27.20 0.622 1.85 4.22 82.40 2,118 31,010
Claude Sonnet 5.5 103.04 11.33 0.500 0.16 1.32 32.48 1,013 3,235
Kimi K3 91.52 41.75 0.661 0.60 3.29 42.29 517 1,920
Rule-based 210.97 0.00 1.034 0.17 4.32 64.65 1,624 N/A
0.5
1
Profitability
Assortment
InventoryPricing
Capital
efficiency
GPT-6.1 Sol
0.5
1
Profitability
Assortment
InventoryPricing
Capital
efficiency
GLM-5.3-Flash
0.5
1
Profitability
Assortment
InventoryPricing
Capital
efficiency
DeepSeek V4.1 Flash
0.5
1
Profitability
Assortment
InventoryPricing
Capital
efficiency
Claude Sonnet 5.5
0.5
1
Profitability
Assortment
InventoryPricing
Capital
efficiency
Kimi K3
0.5
1
Profitability
Assortment
InventoryPricing
Capital
efficiency
Rule-based
LLM mean (3 runs) Rule-based (seed 1)
Figure 4: Whole-episode operational profiles over 180 days. Each panel shows the mean operational profile of an
LLM or the rule-based baseline. Profitability, Assortment, Inventory, Pricing, and Capital Efficiency correspond to
terminal net assets, assortment quality, reversed waste rate, reversed pricing regret, and daily gross profit per unit of
inventory capital, respectively. Each axis is min-max normalized across the five model means and the baseline, with
larger values indicating better relative performance.
thousand CNY .
Assortment.GPT-6.1 Sol leads the LLM agents
in assortment quality, scoring 0.992. GLM-5.3-
Flash follows at 0.817, while Claude Sonnet 5.5
has the lowest score at 0.500.
Inventory.Claude Sonnet 5.5 and GLM-5.3-
Flash record the lowest waste rates at 0.16% and
0.27%, respectively. DeepSeek V4.1 Flash has
the highest rate at 1.85%. Inventory availability
also differs substantially. Claude’s low waste ac-
companies empty shelves on 25.21% of site-days,
whereas DeepSeek’s machines are empty on only
1.67%, combining broader inventory availability
with greater losses.
Pricing.Claude Sonnet 5.5 achieves the lowest
conditional pricing regret at 1.32 CNY per machine
per day, followed by GLM-5.3-Flash at 2.45. GPT-
6.1 Sol has a much larger gap at 30.18, while all
other models fall between 1.32 and 4.22. Its opera-
tional profile thus combines the strongest realized
profitability with the largest conditional pricing
gap.
Capital Efficiency.Claude Sonnet 5.5 generates
the highest daily gross profit per unit of inventory
capital at 0.0589, followed by GLM-5.3-Flash at
0.0362.
8

1 90 180
Simulated day
0
100
200
300
Net assets (1,000 CNY)
GPT
GLM
DeepSeek
Sonnet
Kimi
Rule-based
(a) Net-asset trajectories
0 4 8 12
Reassignment gap (%)
GPT
GLM
DeepSeek
Sonnet
Kimi
Rule-based
7.05
0.53
0.77
3.89
0.19
2.61
(b) Site coordination
0 10 20 30
Empty site-days (%)
40
60
80
100
Cycle contribution (CNY/site/day)
GPT
GLM
DeepSeek
Sonnet
Kimi
Rule-based
(c) Physical execution
Figure 5: Long-horizon operations, site coordination, and physical execution. (a) Mean net-asset trajectories across
three runs per LLM, compared with the rule-based baseline. (b) Mean reassignment gaps across six checkpoints,
with whiskers showing the range across three executions and a fixed baseline. (c) Availability and visit-cycle returns,
averaged across executions. Contributions exclude final incomplete cycles and costs other than visit fees.
5.2 RQ1: Can LLM agents effectively manage
long-horizon business operations?
Most evaluated agents can establish profitable op-
erations, but reliable long-horizon outperformance
remains limited. All 15 LLM executions finish
above the initial capital, whereas only GPT-6.1 Sol
exceeds the rule-based baseline in all three execu-
tions. The trajectories in Figure 5(a) also distin-
guish sustained growth from early gains followed
by stagnation, particularly for Kimi K3.
5.3 RQ2: Can agents coordinate resources
across sites?
Site coordination remains incomplete even for the
best-performing agent. We evaluate this through
the best reassignment of existing assortments
across sites at six 30-day checkpoints, using the
standardization of the assortment metric. GPT’s
actual assignment falls 7.05% below this restricted
optimum, compared with 2.61% for the baseline in
Figure 5(b). Its strong aggregate return therefore
coexists with opportunities to improve where its
selected products are offered.
Because this diagnostic introduces no new prod-
ucts, the gap identifies unrealized value in match-
ing existing offerings to heterogeneous sites. Con-
versely, a small reassignment gap does not estab-
lish strong coordination when the underlying as-
sortments are weak. DeepSeek and Kimi illustrate
this distinction through their limited reassignment
gains and low assortment scores. Coordination
must therefore be assessed jointly with product
quality, since efficient placement cannot compen-
sate for unsuitable offerings.
5.4 RQ3: Can agents plan physical execution?
Agents do not consistently balance local availabil-
ity with economical execution. Over days 16–180,
GPT and DeepSeek both avoid completely empty
shelves, but GPT achieves approximately twice
DeepSeek’s visit-cycle contribution per site-day
in Figure 5(c). Sonnet and Kimi instead exhibit
persistent empty-site exposure despite holding cor-
responding products in the warehouse.
These outcomes reflect two separate require-
ments of physical execution. Central inventory
becomes available to customers only after a paid
on-site transfer, so procurement alone cannot main-
tain local supply. Conversely, visits that preserve
availability can absorb a substantial share of gross
profit when they are too costly relative to the sales
they support. Effective execution requires coordi-
nating replenishment timing and visit frequency
with local demand. Cycle returns, measured as
sales gross profit minus visit fees divided by cycle
duration, must therefore be interpreted alongside
availability and the costs excluded from this mea-
sure.
5.5 RQ4: Can agents improve through
feedback?
The trajectories provide limited evidence of consis-
tent economic improvement as feedback accumu-
lates. Comparing days 16–45 with days 136–165
in Figure 6, daily asset growth decreases for all five
model means and in 13 of the 15 executions. Mean-
while, several agents improve individual operating
metrics. Better waste control or pricing therefore
does not consistently translate into a stronger over-
all operating policy.
An accounting decomposition helps explain this
9

0 800 1600
CNY/day
GPT
GLM
DeepSeek
Sonnet
Kimi
Rule-based
(a) Asset growth
0.0 0.6 1.2
Reference ratio
(b) Assortment
0 2 4
Loss fraction (%)
GPT
GLM
DeepSeek
Sonnet
Kimi
Rule-based
(c) Waste
0 20 40
CNY/site/day
(d) Pricing gap
Days 16–45
Days 136–165
Figure 6: Early- and late-period operating outcomes.
Markers show mean LLM outcomes and rule-based
baseline outcomes.
disconnect. DeepSeek generates more gross profit,
but additional warehouse and visit expenses off-
set most of that gain. These patterns suggest
that local corrections can coexist with increasingly
costly inventory and execution commitments. How-
ever, changing environmental conditions and in-
ventory states prevent this temporal comparison
from causally identifying whether feedback itself
improves the agents’ decisions.
5.6 Failure Modes
Trajectory inspection identifies four observed fail-
ures in action feasibility, inventory cost planning,
physical execution, and policy revision. These
cases illustrate behavior without establishing preva-
lence or causal effects.
Incomplete Grounding of Action Plans.In
one Kimi K3 run, all 49 allocations in a day 170 re-
stocking batch were rejected because the requested
products lacked sufficient warehouse stock. The
agent had observed 4,701 warehouse units in ag-
gregate and attempted replenishment across seven
sites while an order remained in transit. After re-
jection, it ended the day and waited for delivery.
The episode shows why allocation plans require
product-level availability checks.
Insufficient Planning for Inventory Costs.In
another Kimi run, six purchases between days 136
and 169 repeated an identical bundle of 21 prod-
ucts. Although core products required replenish-
ment, the bundle also included products with no
recorded sales during this interval. For one such
product, 2,158 unexpired units were already in the
warehouse before day 169, yet the agent ordered
another 80 units. Procurement thus continued to
expand inventory that was not being deployed or
consumed.
Fragmented Physical Execution.In one
DeepSeek V4.1 Flash run, a campus machine gen-
erated only 5.14 CNY of gross profit between visits
on days 125 and 126, against a 35 CNY visit fee.
The agent returned on day 126 to add just four
units, incurring another visit fee. This sequence
illustrates how frequent responses to small stock
changes can create interventions whose costs are
poorly matched to site-level turnover.
Ineffective Use of Operating Feedback.GLM-
5.3-Flash illustrates the difference between imme-
diate error recovery and persistent policy revision.
On day 163, four allocations requesting four units
each were rejected because only three units of the
product remained in the warehouse. The agent
then successfully allocated those three units to one
site. However, the same four infeasible allocations
reappeared on day 168, followed by the same local
repair. The feedback supported correction within
each interaction but did not prevent the allocation
pattern from recurring.
6 Conclusion
We introduced AutoVend, a benchmark for long-
horizon autonomous business management across
20 heterogeneous vending sites with shared inven-
tory, procurement lead times, and paid physical
execution. Evaluation of five LLM agents over 180
simulated days shows that four of five underper-
form a rule-based inventory-control baseline. Oper-
ational diagnostics reveal that strong aggregate re-
turns can coexist with coordination gaps, while im-
provements in individual metrics need not produce
stronger economic growth. The trajectory cases
further expose difficulties in verifying feasible allo-
cations, adapting procurement, consolidating visits,
and retaining corrections across decisions. Future
work should test these findings, drawn from three
runs per model in one environment, across varied
operating conditions and controlled interventions
such as explicit state verification and persistent pol-
icy updates.
10

References
Andon Labs. 2025. Vending-Bench 2.
Anthropic. 2024. Introducing the Model Context Proto-
col.
Anthropic. 2026. Introducing Claude Sonnet 5.5. Tech-
nical blog.
Kenneth J. Arrow, Theodore Harris, and Jacob
Marschak. 1951. Optimal inventory policy.Econo-
metrica, 19(3):250–272.
Axel Backlund and Lukas Petersson. 2025. Vending-
Bench: A Benchmark for Long-Term Coherence of
Autonomous Agents.Preprint, arXiv:2502.15840.
Anantaram Balakrishnan, Michael S. Pangburn, and Eu-
themia Stavrulaki. 2004. “Stack Them High, Let ’em
Fly”: Lot-Sizing Policies When Inventories Stimu-
late Demand.Management Science, 50(5):630–644.
Gagan Bansal, Wenyue Hua, Zezhou Huang, Adam
Fourney, Amanda Swearngin, Will Epperson, Tyler
Payne, Jake M. Hofman, Brendan Lucier, Chinmay
Singh, Markus Mobius, Akshay Nambi, Archana
Yadav, Kevin Gao, David M. Rothschild, Aleksan-
drs Slivkins, Daniel G. Goldstein, Hussein Mozannar,
Nicole Immorlica, and 5 others. 2025. Magentic Mar-
ketplace: An open-source environment for studying
agentic markets.Preprint, arXiv:2510.25779.
Zerui Cheng, Jiawei Xu, Huacan Chai, Jiayang
Sun, Pramod Viswanath, and Maxm Pan. 2026.
AhaBench: Do agents turn experience into reusable
insights? A long-horizon benchmark for continual
learning.Preprint, arXiv:2609.05435.
Leandro C. Coelho, Jean-François Cordeau, and Gilbert
Laporte. 2014. Thirty years of inventory routing.
Transportation Science, 48(1):1–19.
DeepSeek-AI. 2026. DeepSeek-V4.1-Flash: Push-
ing the limits of KV cache compression.Preprint,
arXiv:2609.19969.
Gary D. Eppen. 1979. Note—effects of centralization
on expected costs in a multi-location newsboy prob-
lem.Management Science, 25(5):498–501.
Wei Fan, Xinjie Shen, Xudong Guo, Jianhong Tu, Yang
Su, Yinger Zhang, Lianghao Deng, Fengyu Wang,
Baohua Dong, Yangqiu Song, and Dayiheng Liu.
2026. E-Commerce Bench: Evaluating LLM Agents
on Long-Horizon Autonomous Business Operation.
Preprint, arXiv:2608.30730.
Fortune Business Insights. 2026. Intelligent vending
machine market size, share & industry analysis, 2026–
2034. Report FBI107360.
Muyu He, Adit Jain, Anand Kumar, Vincent Tu,
Soumyadeep Bakshi, Sachin Patro, and Nazneen Ra-
jani. 2026. YC-Bench: Benchmarking AI agents
for long-term planning and consistent execution. In
Third Conference on Language Modeling.
Leslie Pack Kaelbling, Michael L. Littman, and An-
thony R. Cassandra. 1998. Planning and acting in
partially observable stochastic domains.Artificial
Intelligence, 101(1–2):99–134.
Sunghwan Kim, Ryang Heo, Yongsik Seo, Jinyoung
Yeo, and Dongha Lee. 2026. AgenticShop: Bench-
marking agentic product curation for personalized
web shopping. InProceedings of the ACM Web Con-
ference 2026, WWW ’26, pages 2489–2500, New
York, NY , USA. Association for Computing Machin-
ery.
Kimi Team. 2026. Kimi K3: Open frontier intelligence.
Preprint, arXiv:2607.24653.
Haotian Luo, Huaisong Zhang, Xuelin Zhang, Haoyu
Wang, Zeyu Qin, Wenjie Lu, Guozheng Ma, Haiying
He, Yingsha Xie, Qiyang Zhou, Zixuan Hu, Hongze
Mi, Yibo Wang, Naiqiang Tan, Hong Chen, Yi R.
Fung, Chun Yuan, and Li Shen. 2026. UltraHori-
zon: Benchmarking agent capabilities in ultra long-
horizon scenarios. InProceedings of the 43rd Inter-
national Conference on Machine Learning, volume
306 ofProceedings of Machine Learning Research,
pages 83084–83136. PMLR.
Chang Ma, Junlei Zhang, Zhihao Zhu, Cheng Yang,
Yujiu Yang, Yaohui Jin, Zhenzhong Lan, Lingpeng
Kong, and Junxian He. 2024. AgentBoard: An an-
alytical evaluation board of multi-turn LLM agents.
InAdvances in Neural Information Processing Sys-
tems, volume 37, pages 74325–74362, Red Hook,
NY , USA. Curran Associates, Inc.
Steven Nahmias. 1982. Perishable inventory theory: A
review.Operations Research, 30(4):680–708.
OpenAI. 2026. GPT-6.1 Sol. Model documentation.
Yijun Pan, Yukun Lian, Kunyu Shi, Junbo Li, Hong-
wei Xue, Sicong Xie, Guannan Zhang, and Xiaoy-
ing Xing. 2026. Business Arena: Benchmarking
LLM agents in a realistic marketplace.Preprint,
arXiv:2608.08621.
Ralph Peeters, Aaron Steiner, Luca Schwarz, Ju-
lian Yuya Caspary, and Christian Bizer. 2026. Web-
Mall – a multi-shop benchmark for evaluating web
agents. InProceedings of the 49th International
ACM SIGIR Conference on Research and Develop-
ment in Information Retrieval, SIGIR ’26, pages
3342–3348, New York, NY , USA. Association for
Computing Machinery.
Daksh Raghuvanshi, Ved Vedere, and Yifan Wang.
2026. StoreBench: A live-commerce environment
for evaluating and training autonomous operator
agents.Preprint, arXiv:2610.10942.
Qiming Shi, Yulong Tao, Linbo Jin, Zhaolu Kang,
Yibo Dou, Jiawen Zhu, Tianjun Pan, Shaokang Fu,
Chengyu Wang, Siyue Li, Yaping Cheng, Di Weng,
and Chengfu Huo. 2026. MerchantBench: Bench-
marking LLM Agents for Long-Term Coherence in E-
Commerce Operations.Preprint, arXiv:2607.28956.
11

Edward A. Silver and David J. Robb. 2008. Some in-
sights regarding the optimal reorder period in peri-
odic review inventory systems.International Journal
of Production Economics, 112(1):354–366.
Kalyan Talluri and Garrett van Ryzin. 2004. Revenue
management under a general discrete choice model of
consumer behavior.Management Science, 50(1):15–
33.
Haoxin Wang, Xianhan Peng, Huang Cheng, Yizhe
Huang, Ming Gong, Chenghan Yang, Yang Liu, and
Jiang Lin. 2025. ECom-Bench: Can LLM agent
resolve real-world E-commerce customer support is-
sues? InProceedings of the 2025 Conference on
Empirical Methods in Natural Language Process-
ing: Industry Track, pages 276–284, Suzhou (China).
Association for Computational Linguistics.
Frank F. Xu, Yufan Song, Boxuan Li, Yuxuan Tang,
Kritanjali Jain, Mengxue Bao, Zora Z. Wang, Xuhui
Zhou, Zhitong Guo, Murong Cao, Mingyang Yang,
Hao Yang Lu, Amaad Martin, Zhe Su, Leander Mel-
roy Maben, Raj Mehta, Wayne Chi, Lawrence Jang,
Yiqing Xie, and 2 others. 2025. TheAgentCompany:
Benchmarking LLM agents on consequential real
world tasks. InAdvances in Neural Information Pro-
cessing Systems, volume 38, pages 10291–10321,
Red Hook, NY , USA. Curran Associates, Inc.
Shunyu Yao, Howard Chen, John Yang, and Karthik
Narasimhan. 2022. WebShop: Towards scalable real-
world web interaction with grounded language agents.
InAdvances in Neural Information Processing Sys-
tems, volume 35, pages 20744–20757, Red Hook,
NY , USA. Curran Associates, Inc.
Shunyu Yao, Noah Shinn, Pedram Razavi, and
Karthik R Narasimhan. 2025. τ-bench: A bench-
mark for tool-agent-user interaction in real-world do-
mains. InThe Thirteenth International Conference
on Learning Representations.
Mengqi Yuan, Zilong Zhou, Xinzhuang Xiong, Weim-
ing Wu, Jiayang Sun, Jiamin Song, Kaiqian Cui,
Bowen Wang, Haoyuan Wu, Yitong Li, Dunjie Lu,
Haikong Lu, Qi Zhen, Xinyuan Wang, Jiaqi Deng,
Yuhao Yang, Cheng Chen, Boyuan Zheng, Alex Su,
and 17 others. 2026. OSWorld 2.0: Benchmarking
computer use agents on long-horizon real-world tasks.
Preprint, arXiv:2606.29537.
Z.ai. 2026. GLM-5.3-Flash. Model card.
Mario Zechner. 2026. Pi. Software, version 1.1.0.
Linghua Zhang, Jun Wang, Jingtong Wu, and Zhisong
Zhang. 2026. RetailBench: Evaluating Long-
Horizon Autonomous Decision-Making and Strategy
Stability of LLM Agents in Realistic Retail Environ-
ments.Preprint, arXiv:2603.16453.
Junhao Zheng, Xidi Cai, Qiuke Li, Duzhen Zhang,
ZhongZhi Li, Yingying Zhang, Le Song, and
Qianli Ma. 2025. LifelongAgentBench: Evalu-
ating LLM agents as lifelong learners.Preprint,
arXiv:2505.11942.
Yushuo Zheng, Huiyu Duan, Zicheng Zhang, Yucheng
Zhu, Xiongkuo Min, and Guangtao Zhai. 2026.
Market-Bench: Benchmarking large language mod-
els on economic and trade competition. InProceed-
ings of the 64th Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers),
pages 39893–39906, San Diego, California, United
States. Association for Computational Linguistics.
Shuyan Zhou, Frank F. Xu, Hao Zhu, Xuhui Zhou,
Robert Lo, Abishek Sridhar, Xianyi Cheng, Tianyue
Ou, Yonatan Bisk, Daniel Fried, Uri Alon, and Gra-
ham Neubig. 2024. WebArena: A realistic web en-
vironment for building autonomous agents. InThe
Twelfth International Conference on Learning Repre-
sentations.
12

A Prompts
A.1 System Prompt
You operate a network of 20 smart
vending machines for 180 days,
starting with 40000 in cash.
Each day is one turn: you receive an
observation, may call tools, then call
end_day.
## Objective
Maximize net assets at the end of the
run.
Net assets = cash + the cost value of
every unexpired unit you hold,
wherever it sits: on a shelf, in the
warehouse, or in transit.
- The only thing that increases it is
selling above unit cost.
- The things that decrease it:
warehouse rent, labor, the daily fee,
expired-sale fines, and stock that
expires or is discarded unsold.
- Buying stock moves value from cash
into inventory; it is not by itself a
gain or a loss.
## Starting state
On day 1 every shelf and the warehouse
are empty, no order is in transit,
and there is no sales history.
The catalog is the only thing that
exists: 1372 SKUs.
Nothing sells until you order stock,
wait for it to arrive, and restock a
device on site.
## Goods flow
order -> in transit -> warehouse ->
restock (on site) -> shelf -> sale
- Ordered units are debited from cash
immediately.
- The supplier promises 3 days; actual
delivery may be earlier or later.
Units in transit cannot be shelved
and cannot serve a customer.
Arrivals by day and any delayed
orders are in the daily observation.
- Units land in the warehouse.
The warehouse is the only pool a
restock can draw from.
- Reducing or delisting returns units
from a shelf to the warehouse; they
are not destroyed.
- A unit leaves your system only when
a customer buys it or when you discard
it.
## Prices
Prices are per (device, SKU), and each
of the 20 machines is configured
independently.
A price may be set anywhere from 0.50x
to 2.00x the SKU’s suggested price;
out-of-band prices are rejected.
## Costs
Warehouse rent is 0.03 per unit of
volume per day.
Every unit of every SKU takes exactly
one unit of volume, so rent is charged
per unit held and a machine’s
capacity is a count of units.
On top of rent you pay a fixed fee of
80 per day whether or not you act.
On-site actions (restock, reduce,
delist) cost 35 per device per day
touched -- a device touched any number
of times in one day is charged once.
Ordering, repricing, discarding and
all queries are remote and cost
nothing.
Each tool description says which kind
it is.
## Shelf life
Each SKU has a ‘shelf_life_days‘ value
in the catalog, counted from the day
a unit arrives in the warehouse.
Restocking, reducing and delisting do
not reset that clock.
Expired units do not disappear, and
they are worth nothing in net assets.
- Expired units on a shelf still sell,
and every expired unit sold costs an
extra 1000.
Delisting sends them back to the
warehouse, which stops the fine
exposure but does not make them
sellable again.
- Expired units in the warehouse keep
taking up volume and incurring rent.
They cannot be restocked into
anything but more expired stock;
discarding is the only way to remove
them.
## Funding
Cash can go negative.
Rent, the daily fee, visits and
purchases keep being charged, no
interest is added, and the run does
not end.
A negative balance counts against net
assets one for one, so buying on
credit does not change net assets by
itself -- it moves cash into inventory
at cost.
What it does cost is rent for every
day the stock sits, and 3 days before
it can be sold.
## Environment
Shanghai, CN (Asia/Shanghai).
All amounts are in CNY.
Temperature, rain and public holidays
affect demand, differently by product
category and by site.
## Demand
- Fill level: a fuller device sells
faster.
Free volume depresses demand for
every item on that device, not only
for the missing ones.
13

- Depth: an item’s sales stop
increasing beyond a few units on the
shelf; further units only accrue rent.
- Noise: daily sales are random around
that item’s underlying rate, and that
rate is what a longer window of
observations estimates.
- Demand rate, price response and
product fit all vary with location
type.
A product that sells at one site can
be dead stock at another, and the
same price change can help at one site
and hurt at another.
## Memory
Saved notes are never trimmed or
shortened.
They are limited to 6,000 characters.
## Operating loop
There is no human user: no one will
prompt you, approve a plan, or flag a
problem.
When the day’s work is done, call
end_day.
A.2 User Prompt
Daily user prompt template.
Day {day} of {horizon_days} -- {
weekday}, {date}.
{observation}
Keep running the business to maximize
your net assets.
When today’s work is done, call
end_day.
Initial daily prompt example.The initial daily
prompt example is generated from the simulator’s
starting state rather than taken from a historical
agent run.
Day 1 of 180 -- Wednesday, 2025-01-01.
{
"balance": {
"cash":39920.0,
"shelf":0.0,
"warehouse":0,
"in_transit":0.0,
"inventory_at_cost":0.0,
"net_assets":39920.0
},
"pnl": {
"columns":[
"window","days","units_sold","
revenue","gross_profit",
"rent","labor","daily_fee","
expired_fine","net"
],
"rows":[
["yesterday
",0,0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
["last_7d
",0,0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
["last_30d
",0,0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
]
},
"devices": {
"columns":[
"device_id","location","capacity","
units_on_shelf",
"n_skus","empty_slots","
sold_yesterday","sold_7d_avg",
"expired_units","expiring_7d_units
","days_since_visit"
],
"rows":[
["CN_WORKSITE_01","worksite/canteen
",200,0,0,0,0,0.0,0,0,null],
["CN_WORKSITE_02","worksite/canteen
",200,0,0,0,0,0.0,0,0,null],
["CN_WORKSITE_03","worksite/canteen
",200,0,0,0,0,0.0,0,0,null],
["CN_WORKSITE_04","worksite/
plant_floor",200,0,0,0,0,0.0,0,0,null],
["CN_WORKSITE_05","worksite/
plant_floor",200,0,0,0,0,0.0,0,0,null],
["CN_WORKSITE_06","worksite/
plant_floor",200,0,0,0,0,0.0,0,0,null],
["CN_CAMPUS_01","campus/university
",200,0,0,0,0,0.0,0,0,null],
["CN_CAMPUS_02","campus/
school_dormitory",200,0,0,0,0,0.0,0,0,
null],
["CN_RESIDENTIAL_01","residential/
apartment",200,0,0,0,0,0.0,0,0,null],
["CN_RESIDENTIAL_02","residential/
apartment",200,0,0,0,0,0.0,0,0,null],
["CN_RESIDENTIAL_03","residential/
apartment",200,0,0,0,0,0.0,0,0,null],
["CN_RESIDENTIAL_04","residential/
dormitory",200,0,0,0,0,0.0,0,0,null],
["CN_COMMERCIAL_01","commercial/
sports_venue",200,0,0,0,0,0.0,0,0,null
],
["CN_COMMERCIAL_02","commercial/
hotel",200,0,0,0,0,0.0,0,0,null],
["CN_COMMERCIAL_03","commercial/
hotel",200,0,0,0,0,0.0,0,0,null],
["CN_COMMERCIAL_04","commercial/
sports_venue",200,0,0,0,0,0.0,0,0,null
],
["CN_COMMERCIAL_05","commercial/
leisure_venue",200,0,0,0,0,0.0,0,0,
null],
["CN_COMMERCIAL_06","commercial/
hotel",200,0,0,0,0,0.0,0,0,null],
["CN_OFFICE_01","office/
industrial_park",200,0,0,0,0,0.0,0,0,
null],
["CN_OFFICE_02","office/
office_building",200,0,0,0,0,0.0,0,0,
null]
]
},
"warehouse": {
"units":0,
"n_skus":0,
"value_at_cost":0,
"rent_per_day":0.0,
14

"expired_units":0,
"expiring_7d_units":0
},
"in_transit": {
"orders":0,
"units":0,
"value_at_cost":0.0,
"arrivals":[],
"delayed":[]
},
"calendar": {
"today":{"is_workday":false,"
holiday_name":"\u5143\u65e6"},
"next_14d":[]
}
}
Keep running the business to maximize
your net assets.
When today’s work is done, call
end_day.
B Tools
A question mark denotes an optional parameter.
The six inventory and pricing mutation tools accept
batches of 1–100 items, with quantities specified as
positive integers. Structurally malformed batches
are rejected before execution. For a structurally
valid batch, operational constraints are checked
separately for each item, so valid items execute
even when other items are rejected. Results report
accepted and rejected items together with rejection
reasons. Rejected items do not change inventory or
trigger a visit. The three physical tools incur one
visit charge per machine per day, regardless of the
number of successful operations. Query windows
are restricted to 1, 3, 7, or 30 days, with a default
of 30 days. Paginated queries default to 20 rows
per page and allow at most 50. A notebook write
exceeding the character limit is rejected without
replacing the existing notes.
C Ethical Use of Data
The order-level sales records used to build the sim-
ulator were provided by a commercial smart vend-
ing company with its authorization. The records
contain no personal information about customers
or staff. We release only the calibrated simulator
parameters, not the raw records.
15

Table 3: Tools available to the AutoVend agent. A question mark denotes an optional parameter.
Tool Parameters Function and constraints
Remote operational tools
place_order items[{sku_id, qty,
supplier_id?}]
Order warehouse stock and debit cash immediately.
The default supplier isdefault.
adjust_price items[{device_id,
sku_id, price}]
Set a machine-specific price within 0.5–2.0 times the
reference price. The product need not already be
stocked.
discard items[{sku_id, qty}] Destroy warehouse units, taking the earliest-expiring
units first.
end_dayNone Close the daily action window.
get_catalog query? , category_l1?,
category_l2?,
price_min?, price_max?,
in_warehouse_only?,
sort_by?, page?,
page_size?
Search public product attributes and warehouse avail-
ability. Sorting uses arbitrary catalog order, ascending
or descending reference price, or reference margin.
get_categories category_l1? Return subcategory counts, reference price ranges, and
median reference margins.
get_warehouse page?,page_size? Return warehouse quantities, costs, and expiry infor-
mation by product.
get_device_detail device_id,window_days? Return product-level shelf quantities, prices, daily
sales, and expiry information for one machine.
get_sku_across_devices sku_id,window_days? Return a product’s stock and realized sales across ma-
chines, together with site types.
get_sales_history window_days? Return daily network sales, operating costs, visits,
and the top 20 products by realized units sold in the
window.
query_sql sql Execute a read-only SQLite query over operating
records. Return at most 500 rows and stop queries
exceeding two seconds.
get_calendar days_ahead? Return already published holidays and makeup work-
days. The default horizon is 60 days, with a range of
1–400.
get_weatherNone Return settlement weather for today and the following
seven days.
Physical execution tools
restock items[{device_id,
sku_id, qty}]
Transfer warehouse units to a machine, subject to stock
availability and shelf capacity.
reduce items[{device_id,
sku_id, qty}]
Return a specified shelf quantity to the warehouse,
taking the earliest-expiring units first.
delist items[{device_id,
sku_id}]
Return all remaining shelf units of a product to the
warehouse.
Memory tools
read_memoryNone Read the persistent notebook in full.
write_memory text Replace the notebook with at most 6,000 characters.
An empty string clears it.
16
