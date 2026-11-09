---
title: 'The Multi-Lab Enterprise: Governance, FinOps, and Telemetry Challenges of Multi-Model AI Adoption'
url: https://arxiv.org/abs/2609.31622
category: digital-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Fabricio F. Costa
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.31622
pages: 21
chars: 59412
fetched_at: '2026-11-08T13:21:32+00:00'
kb_version: 1
---

# The Multi-Lab Enterprise: Governance, FinOps, and Telemetry Challenges of Multi-Model AI Adoption

The Multi-Lab Enterprise:
Governance, FinOps, and Telemetry Challenges
of Multi-Model AI Adoption
Fabricio F. Costa, PhD, MBA, PMP1,2,3,4,∗
1AIx4All, LLC, Sunnyvale, CA 94087, USA
2HCLTech, 2600 Great America Way, Suite 101, Santa Clara, CA 95054, USA
3Genomic Sciences and Biotechnology Program, UCB, Brasília, DF 70.790-160, Brazil
4Cancer Biology and Epigenomics Program, Stanley Manne Children’s Research Institute,
Ann & Robert H. Lurie Children’s Hospital of Chicago, Northwestern University
Feinberg School of Medicine, Chicago, IL 60614, USA
∗Corresponding author:fcosta@aix4all.com;fabriciof.costa@hotmail.com
This version: 2026. Preprint — comments welcome.
Abstract
Enterprises are not choosing a single frontier AI provider; they are licensing all of them. As of early 2026,
81% of Global 2000 enterprises run three or more model families, and OpenAI, Anthropic, and Google
Gemini together account for roughly 88 to 89% of enterprise LLM usage and spend. Drawing on survey
data, transaction data, provider disclosures, and case studies across finance, legal, consulting, healthcare,
life sciences, retail, and government, this paper shows that multi-lab licensing is a structural feature of
the market, driven by durable task-specific model differentiation rather than a transitional phase awaiting
commoditization. This structure creates three operational problems. Governance fragmentation (P1):
heterogeneous vendor security postures, documentation, and compliance surfaces must be reconciled
across overlapping regulatory frameworks while shadow AI proliferates. FinOps breakdown (P2): token-
based, behavior-driven consumption defeats budgeting. In the past year, 79% of enterprises overran
AI budgets, with FinOps-mature organizations overshooting by a mean of 30.9%, and no standardized
cross-provider unit of spend exists. Telemetry fragmentation (P3): each lab exposes adoption and cost
data through incompatible consoles, APIs, and metric definitions, forcing bespoke unification layers.
We map the emerging responses, including LLM gateways, observability platforms, and the Tokenomics
Foundation’s FOCUS extension. We then develop a five-metric framework for evaluating API and agent
cost burn, with a worked example where the cheapest model per attempt is the most expensive per
successful task. We conclude that P1, P2, and P3 reflect one missing abstraction: a cross-provider
enterprise AI control plane.
The views expressed are the author’s own.
Keywords:enterprise AI adoption, large language models, multi-vendor strategy, AI governance, FinOps,
AI observability, frontier AI labs.
1 Introduction
In less than three years, generative AI has become the fastest-scaling software category in history: enterprise
spending on generative AI grew from $1.7B in 2023 to $11.5B in 2024 to $37B in 2025 [1]. Beneath this
1
arXiv:2609.31622v1  [cs.CY]  31 Jul 2026

growth curve, however, lies a market structure that contradicts the standard enterprise-software playbook.
Enterprises do not standardize on one vendor. They license OpenAIandAnthropicandGoogle—often
simultaneously, often within the same quarter, and sometimes for the same workload class.
The evidence is consistent across independent data sources. A January 2026 survey of 100 Global 2000
executives found 81% of enterprises using three or more model families, up from 68% a year earlier [2].
Transaction data across more than 70,000 U.S. firms shows the most sophisticated AI buyers deliberately
avoiding single-vendor concentration [3]. Even the U.S. federal government, through the General Services
Administration’s OneGov agreements of August 2025, licensed ChatGPT Enterprise, Claude for Govern-
ment, and Gemini for Government within a fifteen-day window—at nominal fees of $1, $1, and $0.47 per
agency respectively—explicitly enabling agencies to adopt any or all [4].
This paper asks two questions:
•RQ1:Why do enterprises across verticals license all top-tier frontier AI labs rather than standardizing
on one?
•RQ2:What operational problems does this multi-lab structure create, and how are enterprises and the
surrounding ecosystem responding?
We argue that the answer to RQ1 isdurable differentiation: frontier models have diverged, not con-
verged, in task-specific capability—coding and agentic work, long-context multimodal processing, general
knowledge work and ecosystem breadth—and enterprise switching behavior confirms that buyers treat labs
as complements rather than substitutes. The answer to RQ2 is organized around three problems, which we
label following the numbering of the practitioner observations that motivated this work:
P1 — Governance fragmentation.Each additional lab multiplies the compliance surface: separate secu-
rity reviews, heterogeneous model documentation, distinct data-processing agreements, and diver-
gent certification postures, all mapped against overlapping regulatory frameworks (NIST AI RMF,
ISO/IEC 42001, the EU AI Act, and sector-specific regimes).
P2 — FinOps breakdown.The atomic unit of AI cost is the token, whose consumption scales with model
behavior—prompt length, reasoning depth, agentic iteration—rather than with seats or headcount.
Balancing token consumption against dollar budgets across providers with incompatible pricing struc-
tures defeats traditional financial planning.
P3 — Telemetry fragmentation.Each lab exposes adoption and spend data through its own administrative
console and APIs, with incompatible metric definitions, export formats, and refresh latencies. No
enterprise can answer “how much are we spending on AI, on what, and to what effect?” from any
single vendor surface.
Figure 1 previews the paper’s organizing argument: three labs multiplied by three incompatible op-
erational planes yields nine surfaces every multi-lab enterprise must reconcile alone, and P1–P3 dissolve
jointly—or not at all—through a shared control-plane abstraction developed in Section 9.
Contributions.This paper makes four contributions. (1) A triangulated empirical account of enterprise
multi-lab licensing that combines survey, transaction, and disclosure data with explicit treatment of source
conflicts of interest. (2) A three-problem framework (P1/P2/P3) grounded in documented enterprise cases
across more than seven verticals. (3) A vendor-neutral structured comparison of provider administrative and
usage-telemetry surfaces (Table 4), which to our knowledge is the first of its kind. (4) A minimal five-metric
framework for evaluating API and agent cost burn (cost per attempt, cost-of-pass, burn multiplier, difficulty
2

Enterprise
OpenAI Anthropic Google
Governance surfaces
(security reviews, DPAs,
model cards, certifications)
Commercial models
(seats vs. token pools,
caching, batch, PTUs)
Telemetry APIs
(consoles, exports, metric
definitions, refresh latency)
Cross-provider enterprise AI control plane
(normalized units: tokens, active users, task classes;
unified policy, spend, telemetry)
P1 Governance  +  P2 FinOps  +  P3 Telemetry
solved through one shared abstraction
(a) today: fragmentation
(b) proposed
3 labs × 3 planes = 9 incompatible surfaces per enterprise
Figure 1:The paper’s organizing framework. (a) Today, each licensed lab exposes its own governance surface (P1),
commercial model (P2), and telemetry API (P3), yielding 3×3=9 incompatible surfaces per three-lab enterprise.
(b) The proposed cross-provider control plane normalizes policy, spend, and usage into shared units, addressing P1–
P3 through one abstraction (§9).
elasticity, marginal cost of capability), with a worked example. (5) A gap analysis positioning the technical
LLM-routing literature against the organizational problems enterprises face, together with a research and
standardization agenda.
2 Background and Related Work
2.1 Enterprise LLM Market Structure, 2023–2026
The enterprise LLM market has undergone a rapid redistribution of share. Anthropic’s share of enterprise
LLM spend grew from 12% in 2023 to 24% in 2024 to 40% in 2025, while OpenAI’s declined from 50% to
27% and Google’s rose from 7% to 21% over the same period [1, 5] (Figure 3). Total enterprise generative
AI spending reached $37B in 2025, with the application layer accounting for $19B [1] (Figure 3b). Average
per-enterprise LLM spend rose from approximately $4.5M to $7M over two years and is projected to reach
$11.6M [2].
Critically for this paper’s thesis, provider-level stickiness coexists with portfolio-level expansion: only
11% of enterprise teams changed model providers in the past year, while 66% upgraded to a newer model
from an existing vendor [1]. Enterprises rarelysubstitutelabs; theyaddthem.
2.2 The LLM Routing and Orchestration Literature
A substantial technical literature addresses cost-quality optimization across multiple LLMs. FrugalGPT
demonstrated cascade strategies reducing inference cost by up to 98% while matching top-model quality [6].
3

RouteLLM learns routing policies from preference data, achieving cost reductions of 85% on MT-Bench and
45% on MMLU [7]. Related systems include Hybrid LLM [8], RouterDC [9], MoDEM [10], MetaLLM [11],
and GraphRouter [12], with RouterBench [13] and RouterArena [14] providing standardized evaluation.
This literature answers a narrower question than the one enterprises face. Routing optimizeswhich
model answers a given query. It does not address who reviews four vendors’ security postures (P1), how
finance reconciles four incompatible billing models (P2), or how adoption is measured consistently across
four administrative consoles (P3). The organizational layer above routing is, to our knowledge, unaddressed
in the peer-reviewed literature; the present paper targets that gap.
2.3 AI Governance Frameworks
Enterprises deploying frontier models operate under a growing stack of overlapping frameworks: the vol-
untary NIST AI Risk Management Framework [15]; the certifiable ISO/IEC 42001 AI management-system
standard [16], which industry surveys suggest a large majority of organizations plan to pursue; and the
mandatory EU AI Act [17], whose obligations phase in between February 2025 and August 2027. Sector
regimes add further constraints: HIPAA and FDA guidance in healthcare and life sciences, and FINRA/SEC/OCC
expectations in financial services. Section 5 analyzes how multi-lab licensing multiplies the burden of com-
plying with this stack.
2.4 FinOps and the Token as a Cost Unit
The FinOps Foundation’s FOCUS specification standardized cloud cost-and-usage data, but tokens—the
atomic unit of LLM consumption—fell outside its original scope. In 2026 the Linux Foundation announced
the Tokenomics Foundation, in collaboration with the FinOps Foundation, to extend FOCUS to token-
based consumption; initial supporters include Accenture, Google Cloud, IBM, JPMorganChase, KPMG,
Microsoft, Oracle, Salesforce, SAP, and ServiceNow [18]. The State of FinOps 2026 survey reports that AI
cost management became a near-universal practice concern, cited by 98% of respondents, up from 63% a
year earlier [19]. Section 6 builds on this backdrop.
3 Data and Methods
This is a synthesis study. We combine four evidence classes with distinct reliability properties, and we treat
their disagreements as informative rather than as noise to be averaged away.
1.Survey data:Menlo Ventures (n≈500 U.S. enterprise decision-makers, November 2025; n=150 tech-
nical leaders, July 2025) [1, 5]; Andreessen Horowitz (n=100 CIOs, 2025; n=100 Global 2000 exec-
utives, January 2026) [2, 20]; McKinsey State of AI (2025) [21]; DoiT/Sapio (n=500 finance leaders,
±4.4pp at 95% CI) [22]; Mavvrik/Benchmarkit (n=372 enterprises) [23].
2.Transaction data:the Ramp AI Index, derived from corporate card and bill-pay flows across more
than 70,000 U.S. businesses [3]. Transaction data is behavioral rather than self-reported and uniquely
captures decentralized “shadow” purchasing.
3.Provider disclosures:earnings releases and executive statements from Microsoft, Alphabet, Amazon,
OpenAI, and Anthropic [24–27]. These are flagged as company-claimed throughout.
4.Case documentation:primary company announcements, GSA award notices, and credible trade
press underpinning the vertical case matrix of Section 4.4.
4

Menlo 2025
(survey, n 500)
[Anthropic investor]
a16z 2026
(survey, n=100 G2000)
[OpenAI investor]
Ramp 2026
(transactions, 70K firms)
[independent]
Yipit 2026
(alt-data, 1K cos.)
[independent]
0
20
40
60
80
100Reported metric (%)
27
40
78
44
39.5 41
85
55
spend share production adoption business adoption adoption (panel)
OpenAI Anthropic
Figure 2:Source triangulation for OpenAI and Anthropic enterprise position across four data series with different
constructs and different conflicts of interest [1–3]. Divergence across series is treated as information, not noise (§3).
Conflict-of-interest handling.The two most-cited enterprise AI market surveys are published by venture
firms with direct financial stakes in the outcome: Menlo Ventures is an Anthropic investor, and Andreessen
Horowitz is an OpenAI investor. Anthropic additionally reports revenue transacted through cloud resellers
on a gross basis, complicating cross-lab revenue comparison [28]. Our mitigation is triangulation: where
survey, transaction, and disclosure series diverge, we report the range and note the direction of plausible
bias rather than selecting a single point estimate. Where independent corroboration exists—for example,
an independent alternative-data panel of roughly 1,000 companies finding OpenAI adoption near 85% and
Anthropic near 55%, consistent with the a16z survey [2]—we say so. Figure 2 makes the triangulation
explicit: the four series measure related but non-identical constructs (spend share, production adoption, paid
business adoption, panel adoption), which explains part of their divergence; the residual divergence tracks
the direction one would predict from each publisher’s financial position, which is exactly why no single
series should be cited as ground truth.
Limitations.The quantitative base is U.S.-centric; survey sampling frames differ across sources and years;
and the market moves quickly, so all figures are dated to their publication month. This paper characterizes a
market circa mid-2026; its framework (P1–P3) is intended to outlive its point estimates.
4 The Multi-Lab Licensing Phenomenon
4.1 Prevalence
Multi-lab licensing is now the dominant enterprise pattern. As of January 2026, 81% of surveyed Global 2000
enterprises used three or more model families in testing or production, up from 68% in mid-2025 [2]; 37%
of enterprises ran five or more models in production as of 2025, up from 29% the year prior [20] (Figure 4).
OpenAI models were in production at 78% of surveyed enterprises; Anthropic reached 44% in production
and over 63% including testing, the largest penetration gain of any lab over the survey interval [2]. The three
leading labs jointly account for approximately 88–89% of enterprise LLM spend and wallet share [1, 2].
5

2023 2024 2025
0
10
20
30
40
50Share of enterprise LLM spend (%)
OpenAI 27%
50%
Anthropic 40%
12%
Google 21%
7%
Other 12%
31%
(a) Provider share trajectories
2023 2024 2025
0
5
10
15
20
25
30
35
40Enterprise GenAI spend (US$B)
$1.7B
$11.5B
$37B
(b) Total market, 22 ×  in two years
Figure 3:The redistribution, not contraction, of the enterprise LLM market. (a) Provider share trajectories, 2023–
2025: Anthropic and OpenAI cross as Anthropic climbs 12%→40% and OpenAI declines 50%→27%. (b) The
market itself grew 22×($1.7B→$37B), so every provider’s absolute revenue grew even as shares shifted. Data: Menlo
Ventures annual surveys [1, 5]; 2024 OpenAI value interpolated from Menlo’s 2024 report. Menlo is an Anthropic
investor (§3).
4.2 Why All of Them: Durable Differentiation by Task
The central explanatory claim of this paper is that enterprises license all top-tier labs because the labs have
divergedin task-specific capability, making them complements rather than substitutes.
Coding and agentic work.AI-assisted software development is a category of roughly $4B in enterprise
spend, within which Anthropic holds a 54% share [1]; at mid-2025, Claude models held 42% of developer
usage against OpenAI’s 21% [5].
Reasoning.54% of surveyed enterprises report that reasoning-class models materially accelerated their
adoption [2], and reasoning workloads consume substantially more output tokens per request—a fact that
resurfaces in Section 6.
Price, long context, and multimodality.Google’s Gemini line competes on price-performance and
context length (with long-context surcharges above 200K tokens), and on native multimodal processing [29].
General knowledge work and ecosystem breadth.OpenAI reports that 92% of Fortune 500 compa-
nies touch ChatGPT and that it surpassed one million business customers in late 2025 (company-claimed);
Microsoft reports more than 20 million paid Microsoft 365 Copilot seats [24].
The clearest micro-level evidence comes from deployers who publish their reasoning. Harvey, a legal
AI platform originally built exclusively on OpenAI, added Anthropic and Google models in 2025 after
internal benchmarking on legal tasks found there was “no longer a single best model”: seven models—three
from labs other than OpenAI—beat Harvey’s original system on its BigLaw Bench, with Gemini strongest
at drafting and OpenAI’s o3 strongest at pre-trial analysis [30]. Harvey now routes tasks across all three
labs. What a single sophisticated deployer discovered by measurement, the broader market discovered by
procurement.
6

20 30 40 50 60 70 80 90
Share of surveyed enterprises (%)
68% 81%
Enterprises using 3+ model families
(Global 2000, May 2025  Jan 2026)
29% 37%
Enterprises with 5+ models in production
(CIO survey, 2024  2025)
Figure 4:Multi-homing is deepening on both available measures: three-plus model families among Global 2000 enter-
prises (68%→81%, May 2025→Jan 2026; n=100) [2] and five-plus models in production (29%→37%, 2024→2025;
n=100 CIOs) [20]. Arrows indicate direction of change between survey waves.
4.3 Structural, Not Transitional
An alternative reading holds that multi-lab licensing is a temporary artifact of an immature market that will
consolidate as models commoditize. Three lines of evidence cut against this.
First,switching is rare while portfolios expand: only 11% of teams changed providers in a year, yet the
share of enterprises using three or more families rose from 68% to 81% in roughly the same window [1, 2].
Substitution-driven consolidation would show the opposite signature.
Second,enterprises are architecting for permanence. JPMorgan built its LLM Suite portal—serving
over 200,000 employees—explicitly to move across external models, with its Chief Data & Analytics Officer
stating the plan is “not to be beholden to any one model provider” [31]. Goldman Sachs’ firmwide assistant
is architecturally model-agnostic across OpenAI, Google, Anthropic, and Meta models, a design the firm
characterizes as risk mitigation against single-vendor dependence. These are capital investments in multi-lab
operation, not stopgaps.
Third,capability divergence is widening at the frontier, as the specialization evidence of §4.2 shows,
and bundling pressure from Microsoft and Google—which does exist—operates at the productivity-suite
layer more than at the model-API layer.
The event record makes the pattern legible at a glance (Figure 5): across finance, consulting, and gov-
ernment, the signature is the same—multiple labs adopted nearly simultaneously, by design.
We therefore treat the multi-lab enterprise as the steady state for the foreseeable horizon, which makes
the operational problems it creates worth solving rather than waiting out.
4.4 The Phenomenon Across Verticals
Table 1 summarizes documented multi-lab deployments across eight verticals. Three patterns are worth
drawing out. Infinancial services, the poles are visible: JPMorgan and Goldman Sachs institutionalized
multi-lab architectures, while Morgan Stanley pursued a deliberate deep single-vendor partnership with
OpenAI—the exception that proves the default. Inconsulting, the multi-lab pattern is doubled: firms license
multiple labs internallyandmaintain delivery partnerships with all of them (Accenture announced OpenAI
and Anthropic expansions within eight days of each other in December 2025 [32]). Ingovernment, the GSA
OneGov agreements made the multi-lab default explicit policy, licensing all three labs for the entire federal
workforce within a single month [4].
7

Mid-2024 2025 Mid-2025 2026 Mid-2026
JPMorgan LLM Suite
(multi-model portal,
200K employees)
DoD: 4 awards
(OpenAI, Anthropic,
Google, xAI)
GSA OneGov:
3 labs in 15 days
($1 / $1 / $0.47)
Accenture: OpenAI +
Anthropic deals
8 days apart
Deloitte: Claude to
470K employees
a16z: 81% of G2000
use 3+ model families
Figure 5:Selected multi-lab adoption events, 2024–2026. The clustering of multi-vendor commitments—three GSA
agreements in fifteen days, two Accenture lab partnerships in eight days, four simultaneous DoD awards—indicates
deliberate portfolio construction rather than sequential vendor evaluation. Sources: [2, 4, 31, 32].
5 P1: Governance Fragmentation
Each additional licensed lab multiplies, rather than adds to, the governance burden. A three-lab enterprise
must (i) perform three vendor security reviews against three distinct certification postures; (ii) reconcile
three formats of model documentation—model cards and system cards are not standardized across labs in
content, granularity, or update cadence; (iii) negotiate and monitor three data-processing agreements with
different retention, training-use, and residency terms; and (iv) map all of this against the regulatory stack of
Table 2, whose obligations phase in on different clocks.
Shadow AI as the multi-homing externality.The same demand-side pull that drives sanctioned multi-
lab licensing also drives unsanctioned use. Gartner projects that by 2030 more than 40% of enterprises will
experience a security or compliance incident linked to unauthorized shadow AI, and reports that 69% of or-
ganizations already suspect or have evidence of prohibited public GenAI use [33]. IBM’s 2025 breach study
found only 17% of organizations have technical controls preventing employees from uploading confidential
data to public AI tools, and 86% lack visibility into AI data flows [34]. Transaction data makes the financial
face of this visible: one documented case surfaced $120,000 in annual AI spend that appeared on no provider
dashboard because it was purchased entirely on employee cards [35]. Governance regimes designed for one
sanctioned vendor systematically undercount an environment where employees, teams, and business units
each add labs independently.
Why tooling alone has not solved P1.A market of AI governance platforms (e.g., Credo AI, Holistic AI,
IBM watsonx.governance, ModelOp) has emerged to manage inventories, policies, and attestations. These
tools help, but they inherit the fragmentation they sit atop: they consume vendor-heterogeneous documenta-
tion and telemetry (P3), and they cannot normalize what providers do not expose. Governance fragmentation
is thus not merely a policy problem; it is downstream of a data problem, a point we develop in Section 9.
8

Table 1:Documented multi-lab enterprise deployments by vertical (selected). Deployment modes: API = direct
provider API; cloud = via Bedrock/Vertex/Azure; seats = SaaS subscriptions (ChatGPT Enterprise, Claude Enterprise,
Gemini for Workspace).
Vertical Organization Providers Mode Stated rationale
Finance JPMorgan
(LLM Suite)
OpenAI first; multi-
model by design
portal/API “Not beholden to any one model
provider” [31]
Finance Goldman Sachs OpenAI, Google, An-
thropic, Meta
cloud Model-agnosticism as risk mitiga-
tion
Finance Morgan Stanley OpenAI API/seats Deliberate single-vendor depth
(contrast case)
Legal Harvey OpenAI, Anthropic,
Google
cloud Benchmarked task-level superiority
per lab [30]
Consulting Accenture OpenAI + Anthropic (+
Google partnership)
seats/API Client-driven multi-partner strat-
egy [32]
Consulting Deloitte Anthropic (470K em-
ployees) + others
seats Enterprise-wide rollout within
multi-partner portfolio
Healthcare Mayo Clinic Microsoft (Copilot, fron-
tier partnership), Google
Cloud, Abridge
seats/cloud Different tools per clinical work-
flow
Life sci-
ences
Moderna OpenAI (4,000+ custom
GPTs)
seats Scaling knowledge work without
headcount growth
Life sci-
ences
Sanofi OpenAI partnership +
AWS
API/cloud Drug-development acceleration
Retail Walmart In-house model (“Wal-
laby”)
self-hosted Build-vs-license contrast case [1]
Government U.S. federal
(GSA OneGov)
OpenAI ($1), Anthropic
($1), Google ($0.47)
seats All-of-government access; agencies
adopt any or all [4]
Defense U.S. DoD Anthropic, Google, Ope-
nAI, xAI
contracts Deliberately multi-vendor awards
up to $200M each
6 P2: FinOps Breakdown — Balancing Tokens and Dollars
6.1 Why Tokens Defeat Budgets
Traditional software budgeting assumes cost scales with a slow-moving driver: seats, servers, or headcount.
Token-based AI consumption scales withbehavior. Agentic workflows consume roughly 7×the tokens
of single-prompt usage; a tokenizer revision can change token counts for identical text by double-digit
percentages; reasoning models multiply output tokens per request; and a single prompt-template change can
reprice a production workload overnight [35]. Across one large transaction panel, average monthly AI token
spend grew 13×over eighteen months [3].
The result is a budgeting failure documented across independent surveys. In a survey of 500 enterprise
finance leaders, 79% of organizations overran their AI budgets in the past year; strikingly, organizations
self-assessing as “very mature” or “leading edge” in FinOps overran at a higher rate (89%) and by a larger
mean margin (30.9%) than FinOps novices (69%; 16.1%) [22]. We call this thematurity paradox(Figure 6):
existing FinOps practice, tuned to infrastructure whose costs scale with provisioning, transfers poorly to
costs that scale with model behavior—and mature organizations deploy more AI, compounding exposure.
A separate survey of 372 enterprises found 80% missing AI infrastructure forecasts by more than 25%, and
half of companies with AI-core products not tracking LLM API costs at all [23].
The canonical public case is Uber, whose CTO stated in May 2026 that the company had exhausted
9

Table 2:The overlapping governance framework stack facing a multi-lab enterprise.
Framework Status Multi-lab implication
NIST AI RMF
1.0 [15]
V oluntary
(2023); de facto
required for U.S.
federal contrac-
tors
Govern/Map/Measure/Manage functions must be executed per model
and per vendor
ISO/IEC
42001:2023 [16]
Certifiable; in-
creasingly a
procurement re-
quirement
AI management system must encompass every vendor in scope; audits
multiply with vendor count
EU AI Act [17] Mandatory;
phased Feb 2025
– Aug 2027
Deployer obligations attach per system; shadow use of an unapproved
lab can make the firm an unwitting deployer
Sector: HIPAA /
FDA
Mandatory (U.S.
healthcare, life
sciences)
BAAs and validation evidence required per vendor
Sector: FINRA / SEC
/ OCC
Mandatory (U.S.
financial ser-
vices)
Model risk management (e.g., SR 11-7-style review) per external
model family
its full-year 2026 AI budget by April—“the budget I thought I would need is blown away already”—after
rolling out agentic coding tools to roughly 5,000 engineers, with power users consuming $500–$2,000
per engineer per month; Uber responded by capping agentic-coding spend at $1,500 per employee per
month [36].
6.2 Cross-Provider Pricing Heterogeneity
The multi-lab enterprise must reconcile not one but several pricing systems that differ on every axis: unit
prices, discount mechanisms, and even the commercial model itself. Figure 7 maps list per-token prices
across the three labs’ current model tiers: input prices span more than an order of magnitude, output prices
nearly two, and—most consequentially for forecasting—the output:input ratio itself varies from 2:1 to 6:1
across tiers, so the same workload shifted between models changes not just its price level but its pricestruc-
ture. Beneath list prices sit heterogeneous modifiers: prompt caching (discounts up to 90% on cached input),
batch processing (typically 50%), long-context surcharges (Gemini 3.1 Pro doubles above 200K tokens), and
provisioned-throughput commitments on each cloud (Azure PTUs, Bedrock provisioned throughput, GCP
committed-use discounts) [29].
The commercial models diverge more fundamentally: ChatGPT Enterprise is seat-based with flat-rate
usage; Claude Enterprise combines seats with a consumption-billed token pool; Google folded Gemini into
Workspace seat pricing in 2025; Microsoft 365 Copilot is per-seat. Seat-dollars and token-dollars do not
share a unit, which is precisely the “balance” problem P2 names: enterprises cannot compare, attribute, or
charge back spend expressed in incommensurable units. The Tokenomics Foundation’s extension of FOCUS
to tokens [18] is the first credible standardization response, but it launched in 2026 and is unproven; notably,
its initial supporters include both the largest buyers and the largest sellers of the problem.
Historical context sharpens the problem rather than dissolving it. Inference prices for equivalent capa-
bility fell at a median of roughly 50×per year through 2024 [37], but per-token costs leveled in 2025 and
frontier-tier prices have since risen [19]—while consumption per task grows with reasoning and agentic pat-
terns (roughly 7×for agentic workloads). Figure 8 depicts the resulting scissors: enterprises that budgeted
10

Early-stage
FinOps
Very mature /
leading edge
0
20
40
60
80
100Overran AI budget (%)
69%
89%
(a) Overrun incidence
Early-stage
FinOps
Very mature /
leading edge
0
10
20
30Mean overspend (%)
16.1%
30.9%
(b) Overrun magnitude
The maturity paradox: FinOps maturity correlates with worse AI overruns
Figure 6:The maturity paradox in AI budgeting. Organizations self-assessing as FinOps-mature overran AI bud-
gets more often (a) and by larger margins (b) than early-stage organizations. Survey of 500 enterprise finance lead-
ers,±4.4pp at 95% CI [22]. A plausible mechanism: mature organizations deploy more AI, and practices tuned to
provisioning-driven infrastructure costs transfer poorly to behavior-driven token costs.
on the deflation curve met the consumption curve, and the region where the curves diverge is precisely the
2025–2026 budget-overrun era documented above.
7 Evaluating API and Agent Cost Burn
Sections 6 and 8 established that agentic workloads are the fastest-growing driver of token burn and the
hardest to see. This section addresses the layer in between: how an enterprise shouldevaluateAPI usage
and AI agents in economic terms—credits, tokens, and dollars—before and after deployment. Standard
capability benchmarks are silent on this: a leaderboard rank says nothing about what a passing solution costs,
and procurement decisions made on accuracy alone systematically select for expensive configurations.
7.1 From Capability Benchmarks to Economic Evaluation
A small but fast-growing literature has begun to correct this. Kapoor et al. argue that agent benchmarks
which ignore cost invite artificially expensive leaderboard climbing (retries, ensembles, longer reasoning)
and call for jointly reporting accuracy and dollar cost on a Pareto frontier [38]. Erol et al. formalize the
economic view with thecost-of-passmetric: the expected dollar cost of obtaining a correct solution, defined
as the cost of one attempt divided by the success rate, and thefrontier cost-of-pass: the minimum cost-of-
pass achievable across available models, benchmarked against the cost of a human expert performing the
same task [39]. Applying this lens to agents on the GAIA benchmark, the OPPO AI Agent Team showed
that component-level choices (backbone, planning depth, memory design, tool configuration) swing the
economics far more than the accuracy: their cost-optimized framework retained 96.7% of a leading open-
source agent’s performance while improving cost-of-pass by 28.4% ($0.398 to $0.285 per task) [40].
Two of their empirical findings matter directly for the multi-lab enterprise. First,accuracy rankings and
economic rankings disagree: in their backbone comparison, Claude 3.7 Sonnet achieved the highest GAIA
accuracy (61.8% vs. GPT-4.1’s 53.3%) but at 3.6×the cost-of-pass ($3.54 vs. $0.98)—the “best” model
was not the best buy for that workload [40]. Second,agent economics deteriorate nonlinearly with task
difficulty: from the easiest to the hardest GAIA tier, cost-of-pass rose 534% for Claude 3.7 Sonnet and 646%
for OpenAI o1 [40]. Figure 9 plots both findings. For a multi-lab enterprise this is the economic case for
11

10 1
 100 101
Input price (US$ per million tokens, log)
100
101
Output price (US$ per million tokens, log)
Claude Opus 4.8
Claude Sonnet 5
Claude Haiku 4.5
GPT-5.6 Sol
GPT-5.6 Terra
GPT-5.6 Luna
Gemini 3.1 Pro
Gemini 3.5 Flash
Gemini 3.1 Flash-Lite
DeepSeek V4 Flash
3:1
6:1
Anthropic
OpenAI
Google
DeepSeek
Figure 7:List API pricing across provider tiers, July 2026 (log–log). Bubble area scales with the output:input price
ratio; dashed guides mark 3:1 and 6:1 ratios. Because reasoning and agentic workloads shift consumption toward
output tokens, the ratio—not the headline input price—drives realized cost, and it varies across providers and tiers.
Prices from third-party trackers synchronized to provider documentation [29]; excludes caching, batch, long-context,
and committed-use modifiers. Snapshot values; prices change frequently.
the portfolio itself—different labs occupy different points on the cost-accuracy frontier for different task
classes—and simultaneously the case for measuring, because the frontier cannot be exploited blind.
7.2 A Minimal Evaluation Framework for the Multi-Lab Enterprise
Synthesizing this literature with the FinOps evidence of Section 6, we propose that enterprises evaluate every
API workload and agent deployment on five metrics (Table 3), computed per task class and per provider:
1.Cost per attemptC=n in ·p in +n out ·p out +c tools, wherenare token counts,pper-token prices, and
ctools tool/retrieval costs.
2.Cost-of-passv=C/s, the expected cost of asuccessfuloutcome given success rates[39]. This is the
number that belongs in a business case;Calone is not.
3.Burn multiplierB=T agent/Tsingle, the ratio of tokens consumed by the agentic configuration to a
single-shot baseline on the same task (empirically around 7×for agentic coding [35]).
4.Difficulty elasticity: the ratio of cost-of-pass on the hardest to the easiest tier of the workload (5–6×
on GAIA for frontier backbones [40]); high elasticity means average-based budgets will be dominated
by the tail.
5.Marginal cost of capability: when comparing two models, the additional cost-of-pass per point of
accuracy gained—making explicit the trade Kapoor et al.’s Pareto framing implies [38].
12

2023.0 2023.5 2024.0 2024.5 2025.0 2025.5 2026.0 2026.5
Year
10 1
100
101
102
Index (log scale, 2023 = 1 / 100)
reasoning models
agentic coding ( 7 × )
50×/yr deflation
 leveling, frontier prices rising
budget-overrun era
(price leveling ×
agentic consumption)
Price per token (indexed, capability-adjusted)
Tokens consumed per task (indexed)
Figure 8:The token-economics scissors (stylized; indexed, log scale). Per-token prices fell∼50×/year through
2024 [37] then leveled, with frontier prices rising [19]; tokens consumed per task rose with reasoning models and
then sharply with agentic workflows (∼7×) [35]. The shaded region marks the documented budget-overrun era (§6).
Curves are illustrative reconstructions of cited trend magnitudes, not fitted series.
7.3 A Worked Example
To make the framework concrete, consider an enterprise evaluating three configurations for an internal ticket-
resolution agent, using July 2026 list prices (Figure 7) andillustrative but realisticconsumption and success
parameters; the arithmetic, not the parameters, is the point.
•Config A (frontier mid-tier):Claude Sonnet 5 ($3 in / $15 out per M tokens); 40K input + 8K output
tokens per attempt⇒C A =$0.24; successs A =0.75⇒v A =$0.32.
•Config B (efficient tier):GPT-5.6 Luna ($1 / $6); weaker model iterates more: 60K + 12K tokens
⇒C B =$0.132;s B =0.45⇒v B =$0.293.
•Config C (budget tier):Gemini 3.1 Flash-Lite ($0.25 / $1.50); 80K + 16K tokens⇒C C =$0.044;
sC =0.12⇒v C =$0.367.
Three lessons fall out. First, therank reversal: Config C is 5.5×cheaper than Config A per attempt yet
the most expensive per resolved ticket—exactly the inversion the GAIA data shows at benchmark scale. Sec-
ond, thecascade dominates: routing every ticket to Config B first and escalating failures to Config A yields
expected cost $0.264 and success 0.45+0.55×0.75=0.86, i.e.v=$0.306—near Config B’s economics at
well above Config A’s success rate, which is the enterprise-scale version of the routing results in Section 2
and a direct economic argument for the multi-lab portfolio. Third, the evaluation is impossible without P3:
computingsandnper task class requires exactly the per-request, per-outcome telemetry that fragmented
provider surfaces do not natively supply—which is why we place this section between the FinOps problem
and the telemetry problem.
13

10 1
 100
Cost-of-pass (US$ per task, log scale)
10
20
30
40
50
60
70GAIA accuracy (%)
GPT-4.1
Claude 3.7 Sonnet
o1
Qwen3-235B-A22B
Qwen3-30B-A3B
QwQ-32B
accuracy leader
economic leader
(a) Accuracy vs. cost-of-pass (backbones)
Level 1
(easy)
Level 2 Level 3
(hard)
0
2
4
6
8
10
12
14Cost-of-pass (US$ per task)
0.32
1.07
3.51
1.69
3.81
9.04
1.96
3.62
12.66
(b) Cost-of-pass by task difficulty
GPT-4.1
Claude 3.7 Sonnet
o1
$0M
$2M
$4M
$6M
$8M
$10M
$12M
$14M
Annual cost at 1M tasks/year (US$ millions)
Figure 9:Agent cost economics on the GAIA benchmark; data from the Efficient Agents study [40] (per-token prices
as of May 2025). (a) Accuracy versus cost-of-pass for agent backbones: the accuracy leader (Claude 3.7 Sonnet) and
the economic leader (GPT-4.1) are different models, and small open-weight models occupy a low-cost/low-accuracy
corner. (b) Cost-of-pass by GAIA difficulty level: economics deteriorate by 5–6×from easiest to hardest tier for
frontier reasoning backbones; the right-hand axis translates per-task cost-of-pass into annual cost at a nominal one
million tasks per year, expressed in US$ millions, to convey enterprise-scale orders of magnitude. Model generations
shown are those evaluated in the cited study; the pattern, not the point estimates, is the finding.
8 P3: Telemetry Fragmentation - Measuring Adoption and Spend Across
Labs
If P2 is about incommensurable dollars, P3 is about incommensurable data. Table 4 compares the adminis-
trative telemetry surfaces of the three leading labs as of July 2026.
Three properties of this fragmentation deserve emphasis. First, the surfaces differ not only in format but
inontology: seat-based products report users and conversations, API products report tokens and requests,
and no two providers define an “active user” identically, so cross-lab adoption comparisons are category
errors by construction. Second, the surfaces differ intemporal semantics: one lab’s near-real-time dashboard
cannot be joined cleanly with another’s figures that refresh on a 4–24 hour cycle and remain revisable for
30 days [41]. Third, routing paths createblind spots: consumption of the same model through a cloud
marketplace can vanish from the lab’s own analytics surface entirely, reappearing only in the cloud provider’s
billing data.
Enterprises respond by building unification layers from a rapidly growing third-party stack: LLM gate-
ways that normalize requests and capture spend at the point of routing (LiteLLM, OpenRouter, Portkey,
Kong AI Gateway, Cloudflare AI Gateway); observability platforms that trace usage and cost per feature
(Langfuse, LangSmith, Helicone, Datadog LLM Observability, Arize, Weights & Biases Weave); and cost
platforms extending cloud FinOps to AI (CloudZero, Vantage, Finout). The gateway pattern is powerful
precisely because it restores a single point of measurement—but it covers only API traffic that the enterprise
routes through it, leaving seat-based products (where much adoption lives) and shadow usage outside the
frame.
The stakes of not measuring are documented in unit-economics failures: GitHub Copilot reportedly lost
around $20 per user per month in its early period against a $10 subscription; a single agentic query can fan
14

Table 3:A minimal cost-burn evaluation framework for enterprise API and agent workloads. All metrics are computed
per task class and per provider, at current contract prices.
Metric Definition Decision it informs
Cost per attempt (C)n in pin +n outpout +c tools Rate-limit and budget-cap settings; anomaly thresh-
olds
Cost-of-pass (v)C/sfor success ratesModel selection per task class; build-vs-buy; ROI
baselines vs. human-expert cost
Burn multiplier (B) Agent tokens÷single-shot
tokens on the same task
Whether agentic autonomy is worth its overhead for
this task class
Difficulty elasticityv hard/veasy across workload tiers Forecast realism; whether to cap or route hard-tier
tasks
Marginal cost of capa-
bility
∆v/∆accuracy between candi-
date models
When to pay for the frontier model vs. a mid-tier one
Table 4:Provider administrative telemetry surfaces (July 2026). Compiled from provider documentation [41, 42] and
third-party analyses; details change frequently.
OpenAI (ChatGPT Ent.) Anthropic (Claude) Google (Gemini)
Usage analytics Admin console dashboard;
on-demand CSV exports
(users, GPTs, projects)
Analytics API (aggregated
usage/cost; separate key type
from Admin API)
Workspace admin reporting
for Gemini; Cloud billing for
API
Audit/compliance Compliance API + admin au-
dit logs
Separate Compliance API
(per-event records)
Cloud audit logging
Cost granularity Seat-based; no per-token
end-user charges
Per-user and per-SCIM-
group cost; org/user spend
limits with threshold alerts
Seat-bundled (Workspace) +
per-token (Cloud API)
Refresh latency Near-real-time dashboard 4–24h refresh; figures revis-
able for up to 30 days
Billing-cycle latency on
Cloud side
Known blind
spots
Consumption invisible in dol-
lar terms (flat seats)
Claude Code via Bedrock
absent from Analytics API
(must use AWS cost data)
Split across Workspace vs.
Cloud surfaces
“Active user” defi-
nition
Provider-defined Provider-defined (differs) Provider-defined (differs)
out into dozens of LLM calls invisible to the feature owner until the invoice arrives [35]. The measurement
gap, in other words, is not an accounting inconvenience; it determines whether AI products and internal
deployments have knowable economics at all.
9 Discussion: P1–P3 as One Missing Abstraction
The three problems are usually assigned to three different organizational owners—governance to risk and
compliance, spend to finance, telemetry to platform engineering—and to three different tool markets. We
argue they are facets of a single missing abstraction: across-provider enterprise AI control plane, a normal-
ized layer through which policy, spend, and usage for all licensed labs are expressed in shared units.
The argument is structural. P1 cannot be solved without P3: governance requires knowing what models
are used, by whom, for what—exactly the data the fragmented telemetry surfaces fail to provide consistently,
and shadow usage evades entirely. P2 cannot be solved without P3 either: cost attribution and chargeback
presuppose usage data in commensurable units. And P3 alone is insufficient without the policy (P1) and
15

financial (P2) semantics layered on top, which is why raw gateways and dashboards have not closed the
gap. Every existing tool category solves a slice—gateways normalize API traffic, FOCUS/Tokenomics
normalizes cost records, governance platforms normalize attestations—but nothing integrates the three, and
each layer inherits the blind spots of the layers below.
9.1 A Token-Spend Governance Framework
We propose a six-layer Token-Spend Governance (TSG) framework as the enterprise-side instantiation of the
control plane (Figure 10a). The framework deliberately composes standards and results already established
in this paper rather than inventing new ones: its lower layers operationalize P3, its middle layers P2, and its
upper layers P1.
L0 — Data.Ingest every spend- and usage-bearing source: provider analytics and compliance APIs,
cloud-marketplace billing (Bedrock, Vertex, Azure), LLM-gateway logs, and corporate-card transaction
feeds. The card feed is not optional; it is the only source that captures shadow AI (§5).
L1 — Normalization.Express all records in shared units via the FOCUS specification and its token
extension [18], supplemented by the three definitions Section 9 argues have no current owner: a tokenizer-
adjusted normalized token, an auditable active-user definition spanning seat- and API-based products, and a
task-class taxonomy.
L2 — Measurement.Compute the five cost-burn metrics of Table 3 per task class and per provider,
with cost-of-pass [39] as the primary decision metric.
L3 — Allocation.Attribute normalized spend to business units, features, and individual agents (charge-
back or showback), and manage commitment vehicles (PTUs, provisioned throughput, committed-use dis-
counts) against realized consumption.
L4 — Control.Enforce budgets and caps in near-real time—organization, team, and per-user limits with
threshold alerts; anomaly detection tuned to behavior-driven cost (a prompt-template change, an agent loop);
and policy-enforced routing, including the cascade strategies of Section 7.3. Uber’s $1,500/employee/month
agentic cap [36] is an L4 control retrofitted after an L2 failure; TSG’s claim is that the layers must exist
beforedeployment scales.
L5 — Assurance.Maintain audit trails and map them to the governance stack of Table 2: NIST AI
RMF functions, ISO/IEC 42001 audit evidence, and EU AI Act deployer obligations, per vendor.
The framework carries a maturity dimension (M0–M4, Figure 10a): frominvisible(no unified view—
the documented state of half of AI-core companies [23]), throughvisible(one normalized view),attributed
(chargeback live), andgoverned(caps and alerts active), tooptimized(cost-of-pass-driven routing across the
lab portfolio). The maturity paradox of Section 6 carries a warning for this ladder: cloud-FinOps maturity
does not transfer automatically; each rung must be rebuilt on token-native units.
9.2 A Unified FinOps–Governance Cockpit (Concept)
Figure 10b sketches, as a concept only, the visualization layer TSG implies: a single cockpit integrating
all licensed frontier labs, oriented primarily toward FinOps governance rather than raw usage telemetry.
Four design commitments distinguish it from existing per-vendor consoles and gateway dashboards. First,
normalized headline economics: total spend, budget burn versus plan, median cost-of-pass, and active users
are computed in L1 units, so the numbers are comparable across seat-based and token-based products—
something no provider console can offer for its competitors. Second,task-class economics per lab: cost-of-
pass by workload class and provider, which is simultaneously an optimization view (where routing would
save money) and the empirical justification for the multi-lab portfolio itself (§4.2). Third,governance
alerts as first-class citizens: shadow-AI detections from the card feed, agentic-cap breaches, cloud-routed
consumption missing from lab consoles (the Bedrock blind spot of Table 4), and compliance-evidence status
16

Figure 10:Conceptual proposal for enterprises (not a product). (a) The six-layer Token-Spend Governance (TSG)
framework with its maturity ladder (M0 invisible→M4 optimized); lower layers operationalize P3 (data and normal-
ization), middle layers operationalize P2 (measurement and allocation), and upper layers operationalize P1 (control
and assurance). (b) Conceptual wireframe of a unified FinOps–Governance cockpit integrating all licensed frontier
AI labs. The dashboard presents normalized headline economics, per-provider spend, seat-versus-token composition,
budget burn-down, cost-of-pass by task class and provider, and governance alerts including shadow AI, agentic spend-
ing caps, cloud-routing blind spots, and compliance evidence. All numerical values are illustrative and shown for
conceptual purposes only.
per framework—placing P1 on the same pane of glass as P2. Fourth,provenance-labeled data: every number
carries its source and refresh latency, because Section 8 showed the surfaces disagree on both. We emphasize
that Figure 10 is a conceptual proposal for enterprises and a design target for the tooling ecosystem, not a
product; its purpose in this paper is to make the control-plane abstraction concrete enough to critique, build,
and standardize against.
From this diagnosis follows a concrete agenda:
1.A minimal cross-provider metric standard.Three definitions would unlock disproportionate value:
(i) a normalized token accounting for tokenizer differences (or a task-normalized consumption unit);
(ii) a standard, auditable definition of an active AI user across seat- and API-based products; (iii) a
shared task-class taxonomy (e.g., coding, drafting, retrieval, agentic execution) so that adoption and
spend can be compared across labs by workload. The Tokenomics/FOCUS effort [18] addresses (i)
for cost records; (ii) and (iii) have no current owner.
2.Provider telemetry parity.Regulatory deployer obligations (e.g., under the EU AI Act) implicitly
require usage visibility that current provider surfaces do not uniformly supply; procurement leverage—
especially from multi-lab buyers like the GSA—could make telemetry completeness (including cloud-
routed consumption) a standard contractual term.
3.Research.The routing literature should be extended upward: from cost-quality routing per query
to governance- and budget-constrained routing per organization, evaluated not only on benchmark
17

quality but on auditability, attribution accuracy, and forecast error. Empirically, longitudinal firm-
level studies of multi-lab portfolios—entry, expansion, and the rare exits—would put the “structural,
not transitional” claim of §4.3 on firmer causal footing.
10 Conclusion
The enterprise AI market has settled, for now, into a configuration few procurement playbooks anticipated:
the typical large enterprise licenses every top-tier frontier lab because the labs are genuinely good at dif-
ferent things, and the buyers know it. This paper documented the phenomenon across survey, transaction,
and disclosure data and across eight verticals, and characterized the three operational problems it creates—
governance fragmentation, FinOps breakdown, and telemetry fragmentation. Each problem is real on its
own terms: multiplied compliance surfaces and proliferating shadow use; near-universal budget overruns
that worsen, paradoxically, with FinOps maturity; and adoption data that cannot be compared across the very
vendors being adopted. But the deeper finding is their unity. An enterprise that cannot measure consistently
cannot govern or budget consistently. Until a cross-provider control plane—standards, telemetry parity, and
integrated tooling—emerges, every multi-lab enterprise will keep rebuilding, privately and partially, the
same missing layer; the Token-Spend Governance framework and cockpit concept of Sections 9.1–9.2 are
offered as a starting design for that layer. The market has voted for many models; the operating model for
many models does not yet exist. Building it is a tractable, consequential agenda for researchers, standards
bodies, and the labs themselves.
Data availability.All quantitative claims cite public sources; no proprietary data was used.
References
[1] Menlo Ventures. 2025: The state of generative AI in the enterprise.https://
menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/, De-
cember 2025. Survey of≈500 U.S. enterprise decision-makers, Nov. 7–25, 2025. Menlo Ventures
is an investor in Anthropic.
[2] Andreessen Horowitz. Leaders, gainers and unexpected winners in the enterprise AI arms race.https:
//a16z.com/, January 2026. Survey of 100 Global 2000 executives (88%>$1B revenue). a16z is an
investor in OpenAI.
[3] Ramp. Ramp AI index.https://ramp.com/data/ai-index, June 2026. Corporate card and bill-
pay transaction data across 70,000+ U.S. businesses.
[4] U.S. General Services Administration. OneGov agreements with OpenAI, Anthropic, and Google.
GSA press releases, August 6–21, 2025, August 2025. ChatGPT Enterprise at $1/agency; Claude for
Government at $1; Gemini for Government at $0.47/agency.
[5] Menlo Ventures. 2025 mid-year LLM market update.https://menlovc.com/perspective/
2025-mid-year-llm-market-update/, July 2025. Survey of 150 enterprise technical leaders.
[6] Lingjiao Chen, Matei Zaharia, and James Zou. FrugalGPT: How to use large language models while
reducing cost and improving performance.arXiv preprint arXiv:2305.05176, 2023.
[7] Isaac Ong, Amjad Almahairi, Vincent Wu, Wei-Lin Chiang, Tianhao Wu, Joseph E. Gonzalez,
M. Waleed Kadous, and Ion Stoica. RouteLLM: Learning to route LLMs with preference data. In
International Conference on Learning Representations (ICLR), 2025. arXiv:2406.18665.
18

[8] Dujian Ding, Ankur Mallick, Chi Wang, Robert Sim, Subhabrata Mukherjee, Victor Rühle, Laks V .S.
Lakshmanan, and Ahmed Hassan Awadallah. Hybrid LLM: Cost-efficient and quality-aware query
routing. InInternational Conference on Learning Representations (ICLR), 2024. arXiv:2404.14618.
[9] Shuhao Chen, Weisen Jiang, Baijiong Lin, James T. Kwok, and Yu Zhang. RouterDC: Query-based
router by dual contrastive learning for assembling large language models. InAdvances in Neural
Information Processing Systems (NeurIPS), 2024.
[10] Toby Simonds, Eldar Kurtic, and Dan Alistarh. MoDEM: Mixture of domain expert models.arXiv
preprint arXiv:2410.07490, 2024.
[11] Quang H. Nguyen, Duy C. Hoang, Juliette Decugis, Saurav Manchanda, Nitesh V . Chawla, and
Khoa D. Doan. MetaLLM: A high-performant and cost-efficient dynamic framework for wrapping
LLMs.arXiv preprint arXiv:2407.10834, 2024.
[12] Tao Feng, Yanzhen Shen, and Jiaxuan You. GraphRouter: A graph-based router for LLM selections.
arXiv preprint arXiv:2410.03834, 2024.
[13] Qitian Jason Hu, Jacob Bieker, Xiuyu Li, Nan Jiang, Benjamin Keigwin, Gaurav Ranganath, Kurt
Keutzer, and Shriyash Kaustubh Upadhyay. RouterBench: A benchmark for multi-LLM routing sys-
tems.arXiv preprint arXiv:2403.12031, 2024.
[14] others Lu. RouterArena: An open platform for comprehensive comparison of LLM routers.arXiv
preprint arXiv:2510.00202, 2025.
[15] National Institute of Standards and Technology. Artificial intelligence risk management framework
(AI RMF 1.0). NIST AI 100-1, January 2023.
[16] International Organization for Standardization. ISO/IEC 42001:2023 — information technology —
artificial intelligence — management system, December 2023.
[17] European Parliament and Council. Regulation (EU) 2024/1689 laying down harmonised rules on
artificial intelligence (AI Act). Official Journal of the European Union, entered into force August 1,
2024, 2024.
[18] The Linux Foundation. Intent to launch the Tokenomics Foundation. Announced at FinOps X 2026,
2026. Extension of the FOCUS specification to token-based AI consumption; initial supporters include
Accenture, Booking.com, Google Cloud, IBM, JPMorganChase, KPMG, Microsoft, Oracle, Sales-
force, SAP, and ServiceNow.
[19] FinOps Foundation. State of FinOps 2026.https://data.finops.org, 2026.
[20] Andreessen Horowitz. How 100 enterprise CIOs are building and buying gen AI in 2025.https:
//a16z.com/ai-enterprise-2025/, June 2025. Survey of 100 CIOs across 15 industries. a16z is
an investor in OpenAI.
[21] McKinsey & Company. The state of AI in 2025.https://www.mckinsey.com/capabilities/
quantumblack/our-insights/the-state-of-ai, November 2025.
[22] DoiT International and Sapio Research. AI spending survey: Why 79% of enterprises overspent on
AI.https://www.doit.com/blog/ai-spending-survey, February 2026. Survey of 500 finance
leaders at organizations with 1,000+ employees (U.S./U.K.),±4.4pp at 95% CI.
19

[23] Mavvrik and Benchmarkit. 2025 state of AI cost management.https://www.mavvrik.ai/blog/
ai-cost-governance-report/, September 2025. Survey of 372 enterprises.
[24] Microsoft Corporation. FY26 Q3 earnings release. April 29, 2026, April 2026. AI business at $37B
annualized run rate, +123% YoY (company-claimed).
[25] Alphabet Inc. Q2 2026 earnings release. July 22, 2026, July 2026.
[26] Amazon.com Inc. Q1 2026 earnings release and CEO commentary, April 2026.
[27] Reuters. Anthropic aims to nearly triple annualized revenue in 2026. April 24, 2026, April 2026.
[28] Sacra. Anthropic revenue, valuation & funding.https://sacra.com/c/anthropic/, 2026. Notes
gross-basis reporting of reseller revenue.
[29] BenchLM. LLM API pricing tracker.https://benchlm.ai, July 2026. Third-party aggregation
synchronized to provider documentation; retrieved July 2026.
[30] Harvey AI. Expanding Harvey’s model offerings.https://www.harvey.ai/blog, May 2025. See
also TechCrunch coverage, May 13, 2025.
[31] CNBC. JPMorgan rolls out AI assistant powered by ChatGPT maker OpenAI. August 9, 2024. Quoting
CDO Teresa Heitsenrether, August 2024.
[32] Accenture. Accenture and Anthropic form strategic alliance. Accenture Newsroom, December 9, 2025,
December 2025.
[33] Gartner. Gartner identifies critical GenAI blind spots that CIOs must urgently address. Press
release, November 19, 2025.https://www.gartner.com/en/newsroom/press-releases/
2025-11-19-gartner-identifies-critical-genai-blind-spots-that-cios-must-urgently-address0,
November 2025.
[34] IBM Security. Cost of a data breach report 2025.https://www.ibm.com/reports/data-breach,
2025.
[35] Ramp. The $1 trillion AI spend blind spot.https://ramp.com/3-steps-to-manage-ai-spend,
2026.
[36] Janakiram MSV. Uber burns its 2026 AI budget in four months on Claude Code.Forbes, May 2026.
May 17, 2026; reporting statements by Uber CTO Praveen Neppalli Naga to The Information.
[37] Stanford Institute for Human-Centered Artificial Intelligence. The AI index 2025 annual report.https:
//aiindex.stanford.edu, 2025.
[38] Sayash Kapoor, Benedikt Stroebl, Zachary S. Siegel, Nitya Nadgir, and Arvind Narayanan. AI agents
that matter.arXiv preprint arXiv:2407.01502, 2024.
[39] Mehmet Hamza Erol, Batu El, Mirac Suzgun, Mert Yuksekgonul, and James Zou. Cost-of-pass: An
economic framework for evaluating language models.arXiv preprint arXiv:2504.13359, 2025.
[40] Ningning Wang, Xavier Hu, Pai Liu, Yue Hou, Heyuan Huang, Shengyu Zhang, Jian Yang, Jiaheng
Liu, Ge Zhang, Changwang Zhang, Jun Wang, Yuchen Eleanor Jiang, He Zhu, and Wangchunshu Zhou.
Efficient agents: Building effective agents while reducing cost.arXiv preprint arXiv:2508.02694, 2025.
OPPO AI Agent Team.
20

[41] Anthropic. Usage and cost API — Claude platform documentation.https://platform.claude.
com/docs/en/manage-claude/usage-cost-api, 2026.
[42] OpenAI. ChatGPT enterprise compliance API and admin analytics.https://platform.openai.
com/docs, 2025.
21
