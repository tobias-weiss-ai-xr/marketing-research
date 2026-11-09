---
title: 'Agentic Trading: When LLM Agents Meet Financial Markets'
url: https://arxiv.org/abs/2605.19337
category: ai-marketing
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Yihan Xia
- Panpan You
- Taotao Wang
- Fang Liu
- Han Qi
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.19337
pages: 59
chars: 293001
fetched_at: '2026-11-08T13:26:10+00:00'
kb_version: 1
---

# Agentic Trading: When LLM Agents Meet Financial Markets

Agentic Trading: When LLM Agents Meet Financial Markets
Yihan Xiaa, Panpan Youa, Taotao Wanga,∗, Fang Liua, Han Qib, Xiaoxiao Wua, Shengli Zhanga
aCollege of Electronic and Information Engineering, Shenzhen University, Shenzhen, China
bShenzhen Audencia Financial Technology Institute, Shenzhen University, Guangdong, People’s Republic of China
Abstract
The integration of Large Language Models (LLMs) with autonomous agent architectures is transforming quantitative finance, shifting
algorithmic trading from isolated predictive modeling toward fully autonomous, closed-loop trading agents. These systems perceive
multimodal market signals, maintain active context, associative vector stores, and structured knowledge bases, execute complex
strategic reasoning, emit executable trading actions, and adapt continuously to non-stationary market regimes. This survey provides a
comprehensive, systematic, and forward-looking synthesis of the rapidly evolving landscape of agentic trading. We structure the
literature through a unifiedArchitecture–Capability–Adaptation (A-C-A)conceptual framework: (i)Architecturedeconstructs the
foundational cognitive loop into perception (textual, numerical, and multimodal), memory systems (working memory, associative
vector storage, and structured knowledge bases), cognitive reasoning (reactive, reflective, and planning-driven), and execution
mechanisms (order routing and friction management); (ii)Capabilityexamines primary financial functions, including automated
alpha discovery, portfolio optimization, and multi-tier risk control; and (iii)Adaptationinvestigates how agents evolve through in-
context learning, supervised fine-tuning, reinforcement learning, multi-agent coordination, and architectural self-evolution. Drawing
on 185 systematically selected studies (including a core empirical subset of n =80 systems evaluated under closed-loop market
conditions), we analyze design spaces, operational trade-offs, and emerging paradigms. Furthermore, as an essential cross-cutting
dimension, we examine empirical evaluation practices across the literature—including backtesting split schemes, transaction-cost
realism, survivorship-bias handling, and execution fidelity—and distill methodological best practices to guide future research. By
bridging artificial intelligence, market microstructure, and quantitative finance, this survey aims to serve as a foundational roadmap
for designing, benchmarking, and deploying reliable agentic trading systems.
Keywords:Large language models, Trading agents, Autonomous financial systems, Algorithmic trading, Multi-agent systems,
System architecture
1. Introduction
The integration of Large Language Models (LLMs) into finan-
cial trading marks a shift from traditional quantitative prediction
models toward more autonomous, agentic systems. Conven-
tional quantitative finance approaches typically employ black-
box machine learning models that generate price or return predic-
tions without explicit reasoning chains or adaptive capabilities.
In contrast, LLM-based trading agents often implement an ex-
plicit loop—perceiving market information, storing experiences,
reasoning about decisions, executing trades, and learning from
outcomes Zhang et al. (2024); Xiao et al. (2024); Yu et al. (2024).
Figure 1 situates representative papers in the chronological de-
velopment of the field, illustrating the evolution from domain-
adapted financial language models to multimodal and multi-
agent trading systems. To provide a structured and compre-
hensive navigation of this design space, this survey synthesizes
∗Corresponding author.
Email addresses:xiayihan40@gmail.com(Yihan Xia),
xiaomu2311@gmail.com(Panpan You),ttwang@szu.edu.cn(Taotao
Wang),liuf@szu.edu.cn(Fang Liu),steffan@szu.edu.cn(Han Qi),
xxwu.eesissi@szu.edu.cn(Xiaoxiao Wu),zsl@szu.edu.cn(Shengli
Zhang)
185included studies screened through2026-09-30, combining
an initial multi-source ledger (cutoff2026-03-09) with a for-
mal extension window covering 2026-03-10 to 2026-09-30. To
help readers distinguish full trading systems from component
modules, the literature is organized into a primary empirical
cohort (n =80) evaluated under closed-loop market conditions
(satisfyingAction Output+Closed-Loop Evaluation) and an
informative background tier (105studies) covering foundation
models, isolated predictors, and specialized tools. Furthermore,
to provide an objective view of current empirical practices,
our synthesis also systematically documents how key experi-
mental protocols are reported across the literature—including
time-consistent split designs (50/80), explicit transaction costs
(47/80), universe survivorship controls (48/80), and execution
semantics (47/80).
Realizing the potential of agentic trading systems involves
distinct engineering and architectural considerations. First,
LLM-based agents generate natural-language rationales and
multi-step reasoning traces; ensuring that these explanations
faithfully reflect execution requires grounded observation spaces
and structured decision logs. Second, agents can adapt their
strategies under changing market regimes by drawing on
episodic memory and dynamic reflection, demanding robust
arXiv:2605.19337v2  [cs.AI]  4 Oct 2026

Research milestones in financial models and trading agents
Selected milestones by first preprint year, 2019–2026
Financial ML
foundations
FinBERT · 2019
Financial sentiment
with pretrained BERT
FinRL · 2020
Deep RL for
stock trading
FinRL-Meta · 2022
Market environments
and DRL benchmarks
2019–2022
Early LLM
trading
AlphaGen · 2023
RL-based discovery
of formulaic factors
FinVis-GPT · 2023
Multimodal financial
chart analysis
FinMem · 2023
Layered memory for
LLM trading decisions
2023
Multimodal
collaboration
FinAgent · 2024
Tool-augmented
multimodal trading
FinCon · 2024
Trading decisions with
verbal reinforcement
TradingAgents · 2024
Role-based teams for
collaborative trading
2024
Reflection and
benchmarks
TradingGroup · 2025
Self-reflection and
trading-data synthesis
StockBench · 2025
Sequential stock-
trading evaluation
2025
Market ecology
and evaluation
FinEvo · 2026
Market games for
strategy evolution
CLQT · 2026
Closed-loop portfolio
evaluation
LiveOption · 2026
Structured option-
trading evaluation
2026
Blue: foundations · Teal: trading systems · Purple: evaluation research
Figure 1:Selected research timeline of financial language models and agentic trading, 2019–2026. Five thematic periods connect financial language
modeling and reinforcement-learning foundations with early LLM trading, multimodal collaboration, reflection and evaluation, and market ecology
with expanded evaluation. Each paper is labeled by its first arXiv submission year. Panel widths are for readability and do not represent period
duration. Foundation papers provide historical context rather than expanding the empirical review corpus Araci (2019); Liu et al. (2020, 2022b); Yu
et al. (2023a); Wang et al. (2023b); Yu et al. (2023b); Zhang et al. (2024); Yu et al. (2024); Xiao et al. (2024); Tian et al. (2025); Chen et al. (2025);
Zou et al. (2026); Qu and Chen (2026); Luo et al. (2026a).
risk boundaries against catastrophic drift. Third, modular
designs allow specialized components for perception, memory,
reasoning, and execution (see Figure 2), enabling systems to be
decoupled, tested, and enhanced incrementally.
Trading agents are essentially autonomous financial decision-
support pipelines: they transform raw, multimodal market
observations into executable actions subject to real-world
friction, liquidity constraints, and supervisory controls. A
comprehensive survey of this domain must therefore examine
the complete decision loop: what information channels are
perceived, how memory is indexed, which reasoning paradigms
generate trading hypotheses, how orders are routed, and how
agents adapt to non-stationary market feedback.
1.1. Related Surveys and Complementary Positioning
As artificial intelligence intersects with financial engineering,
several surveys and benchmark suites have mapped distinct
facets of this evolving domain (summarized in Table 1). We po-
sition our work as complementary to these existing contributions
across four main lines:
General Autonomous Agent Architectures.Foundational sur-
veys such as Wang et al. (2024) provide overarching taxonomies
for LLM-based autonomous agents across general domains,
structuring the field around agent profiling, memory systems,
planning capabilities, and action spaces. While essential for
establishing general cognitive concepts, these frameworks nat-
urally do not address domain-critical financial realities such
as order execution semantics, market frictions, slippage, and
temporal causality. The present survey builds upon these gen-
eral agent concepts and specializes them to the financial market
environment.
Financial Machine Learning and Econometric Factor Mod-
eling.Methodological surveys in quantitative finance, such as
Giglio et al. (2022), synthesize machine learning in asset pric-
ing, focusing on expected return estimation, factor discovery,
stochastic discount factor modeling, and econometric testing.
These works provide statistical and theoretical grounding for
alpha discovery. In contrast, our survey centers on theagentic
dimension—how automated models transition from statistical
predictors into active, autonomous decision-makers that manage
portfolios and execute orders.
Financial Foundation Models and Standardized Task Bench-
marks.Initiatives such as FinBen Xie et al. (2024), PIXIU
Xie et al. (2023), and InvestorBench Li et al. (2025), along-
side open models like FinGPT Wang et al. (2023a), provide
vital infrastructure and standardized benchmarks for evaluating
LLMs on financial NLP and isolated forecasting tasks. Our
survey complements these task-level benchmarks by examining
end-to-end, closed-loop agent systems where perception, reason-
ing, and execution operate together in live or simulated trading
2

Financial
market
State · reward
Perception
Market state
Memory
Past outcomes
Reasoning
Integrate
and infer
Candidate
actions
Forward
planning
Anticipate
outcomes
Reflection
Evaluate
candidates
Action
selection
Choose action
Execution
Place order
Market feedback
Agentic trading: market signals, decisions and feedback
Figure 2:End-to-end decision and execution loop in agentic trading. Market observations and historical experiences are gathered via perception
and memory modules; cognitive reasoning produces candidate actions that are validated through forward planning or reflection; the execution
module maps decisions to market orders under risk constraints; and market outcomes provide feedback for continuous adaptation.
Table 1:Scopes and organizing perspectives of related surveys, benchmarks, and financial AI frameworks.
Work Type Target Domain Primary Review
Focus
System Decomposition Evaluation Perspective
This surveySurvey Trading agents End-to-end trading
pipelines
Perception, memory,
reasoning, execution
A-C-A framework and empirical
protocols
Wang et al. (2024) Survey General AI agents Cognitive agent
architectures
Profile, memory,
planning, action
General capabilities and
benchmarks
Giglio et al. (2022) Survey Asset pricing and
ML
Factor models and
econometrics
Statistical estimation and
pricing kernels
Econometric testing and
predictability
FinBen
(Xie et al., 2024)
Benchmark Financial NLP
and quant tasks
Standardized task
evaluation
Model-level task
mapping
Financial tasks across difficulty
tiers
FinGPT
(Wang et al., 2023a)
Model/tool Financial NLP Open financial AI
models
Models and data
frameworks
Text and sentiment benchmarks
InvestorBench
(Li et al., 2025)
Benchmark Trading decisions Investor persona
evaluation
Simulated decision
agents
Performance across investor styles
Ding et al. (2024) Survey LLM trading
agents
Trading agent
architectures
Agent modules, inputs,
challenges
Backtest patterns and open
questions
Dong et al. (2025) Survey LLM agents in
finance
Broad financial
applications
Multi-role workflows
and deployment
Research, advisory, and
compliance
Note:Categorizations describe each work’s primary organizing scope and core objectives. Benchmarks (FinBen, InvestorBench) and foundation frameworks (FinGPT)
establish essential task-level foundations, while complementary surveys focus on general agent principles Wang et al. (2024), asset-pricing econometrics Giglio et al.
(2022), trading agent fundamentals Ding et al. (2024), and broad financial application domains Dong et al. (2025).
environments.
Existing Surveys on LLM Agents in Finance and Trading.
Recently, Ding et al. (2024) presented a pioneering survey on
LLM agents in financial trading, systematically categorizing
agent architectures, data inputs, and broad backtesting perfor-
mance. Concurrently, Dong et al. (2025) provided an extensive
survey of LLM agents across diverse financial sectors, highlight-
ing real-world deployment scenarios across research, advisory,
and market operations. Our survey is designed to be deeply
complementary to these works: rather than focusing solely on
broad financial workflows or individual algorithmic setups, we
offer an in-depth, architecture-centric decomposition of the end-
3

to-end trading loop, systematically analyze execution and risk
mechanisms, and provide a structured synthesis of empirical
evaluation practices across the literature.
1.2. A Conceptual Framework: Disentangling Architecture,
Capability, and Adaptation
To analyze the wide diversity of trading agents cohesively, this
survey introduces theArchitecture–Capability–Adaptation
(A-C-A)framework as an analytical lens. By separatinghow
systems are constructedfromwhat financial objectives they
pursueandhow they evolve, the A-C-A lens clarifies design
choices across three orthogonal dimensions:
Dimension 1: Architectural Mechanisms (How the System
is Built).The architectural layer deconstructs an agent into
its underlying engineering blocks: multimodal perception (text,
time-series, charts), memory hierarchies (working memory, as-
sociative vector storage, structured knowledge bases), cognitive
reasoning paradigms (reactive, reflective, planning-based), and
action execution modules (order slicing, venue routing, latency
and cost modeling). This decomposition identifies the inputs,
retained state, decision procedures, and execution assumptions
that can be compared across systems (Part I, Sections 3 to 6).
Dimension 2: Functional Capabilities (What the System Ac-
complishes).The capability layer describes the financial tasks
executed by the agent, including automated alpha generation
(symbolic factor discovery and mathematical expression mining),
portfolio allocation (multi-asset weighting and dynamic rebal-
ancing), and proactive risk management (drawdown controls,
stop-loss limits, and supervisory compliance checks). Distin-
guishing capabilities from architectures clarifies that diverse
architectural setups (e.g., reactive vs. strategic) can be deployed
across identical financial goals with differing operational trade-
offs (Part II, Sections 7 to 9).
Dimension 3: Adaptive Pathways (How the System Evolves).
The adaptation layer characterizes changes to agent behavior, pa-
rameters, and organization over time. It covers in-context learn-
ing, supervised fine-tuning, reinforcement learning, and multi-
agent coordination and adaptive interactions. Self-evolution con-
cerns agent-managed updates retained across decisions; struc-
tural self-evolution is the subset that changes strategy code,
update procedures, or system organization. Memory consolida-
tion and reflection can support persistent adaptation within an
otherwise fixed architecture (Part III, Sections 10 to 12).
Table 2 illustrates how representative trading systems in the
literature map across this three-dimensional A-C-A framework,
highlighting how distinct architectural building blocks combine
with functional goals and adaptation mechanisms. Appendix C
provides additional system-level mappings.
1.3. Contributions and Organization
This survey provides a comprehensive and structured synthesis
of the agentic trading literature. The primary contributions are:
1. The A-C-A Analytical Framework.We organize system
comparisons by architecture, financial capability, and
adaptation. Table 2 and the illustrative mappings in
Appendix C show how the lens applies to representative
systems.
2. A Closed-Loop Mechanism Synthesis.Parts I–III
connect perception, memory, reasoning, and execution
with alpha discovery, portfolio management, risk control,
and adaptation. The technical chapters describe module
interfaces, design alternatives, and operational trade-offs
across this decision loop.
3. Transparent Literature Mapping.Based on 185 sys-
tematically mapped studies, with a formal search window
of 2022–2026 and earlier foundational references (includ-
ing a core empirical subset of n =80 closed-loop trad-
ing systems), we link representative mechanisms to their
literature context. Section 2 and Table 3 document the
selection boundary and corpus composition.
4. Empirical Evaluation and Methodological Landscape.
We characterize reported evaluation practices in the empir-
ical subset across temporal splitting (50/80), transaction-
cost modeling (47/80), survivorship-bias controls (48/80),
and execution semantics (47/80). Table 4 reports the ini-
tial and extension cohorts separately to contextualize the
pooled counts.
5. Forward-Looking Challenges and Best-Practice Guide-
lines.We identify key engineering and financial bottle-
necks (including latency, market impact, hallucination
cascades, and strategy degradation) and connect them to
methodological recommendations (MR-1–MR-7). Sec-
tion 13 and Table 20 organize these directions and the
recommendations’ applicability by study type.
The remainder of this survey is organized as follows. Section 2
details the literature selection protocol and synthesis scope.Part
I: Architecture(Sections 3 to 6) deconstructs the core architec-
tural pillars: perception, memory, reasoning, and action execu-
tion.Part II: Capability(Sections 7 to 9) examines the primary
financial capabilities: alpha discovery, portfolio optimization,
and risk control.Part III: Adaptation(Sections 10 to 12) ex-
plores how agents learn, collaborate, and evolve. Section 13
discusses open challenges and methodological guidelines, and
Section 14 concludes the survey.
We begin by defining what constitutes an agentic trader, drawing
on cognitive science and artificial intelligence literature to
identify the essential architectural components.
Part I addresses the fundamental question:What constitutes an
agentic trader?We characterize an agentic trader by four core
architectural components—perception, memory, reasoning, and
action/execution—that together support autonomous decision-
making in financial markets. Whereas traditional trading systems
focus primarily on prediction, agentic systems typically include
an explicit cognitive loop that interacts with and learns from
the market environment through decisions mapped to tradable
actions under market constraints.
4

Table 2:Illustrative mapping of representative trading systems under the A-C-A conceptual framework, showing how architectural components,
functional capabilities, and adaptation pathways intersect.
System Architecture Dimension Capability Dimension Adaptation Pathway
FinAgent Zhang
et al. (2024)
Multimodal Perception
(Text+Visual)+Execution
Layer
Direct Stock Action Selection &
Position Execution
In-Context Learning from market feedback
AlphaAgent Tang
et al. (2025)
Reflective/Strategic Reasoning+
Feedback Validation
Automated Code-Based Alpha Dis-
covery & Factor Pruning
Hypothesis-Factor Iterative Refinement
TradingAgents Xiao
et al. (2024)
Hierarchical Role-based Multi-
Agent Coordination
Joint Alpha Generation, Portfolio
Sizing & Risk Control
Hierarchical Feedback & Memory Updating
2. Review Protocol and Evidence Scope
To synthesize this rapidly expanding literature with conceptual
clarity and methodological rigor, this review adopts a structured
literature selection and corpus mapping methodology. We
define transparent inclusion boundaries to differentiate end-
to-end trading agent implementations from broader financial
tools, and map the design space along well-defined architectural,
functional, and empirical evaluation dimensions.
The formal search for contemporary trading-agent work covered
records published from2022-01-01through2026-09-30; the
2022 start date marks the period in which LLM-based systems
began to appear as end-to-end trading agents rather than as iso-
lated NLP or forecasting components. Citation chaining also
retained nine pre-2022 foundational background works, includ-
ing classical portfolio and learning methods; these references
belong to the included ledger but fall outside the contemporary
search window. The initial-window search covered 2022-01-01
through2026-03-09(last query date: 2026-03-09), using ACM
Digital Library (including ICAIF), IEEE Xplore, arXiv, SSRN,
and Google Scholar, complemented by backward and forward
citation chaining. For this revision we ran a pre-specified exten-
sion window over2026-03-10 to 2026-09-30on arXiv reusing
the three initial query families and adding trading-agent, multi-
agent, and alpha-mining patterns (agentic trading, LLM finance
agents, evaluation/validity, trading-agent phrases, multi-agent
markets, and alpha mining); the extension retrieved 1,539 unique
records, of which 154 entered eligibility assessment under the
same inclusion boundary (Appendix A). After deduplication and
screening, the current ledger contains 185 included studies from
246 candidate records. The windows are not matched search
samples: the initial window spans multiple databases and cita-
tion chaining, whereas the extension uses arXiv only. Window-
level differences therefore describe the assembled ledger and
should not be interpreted as a controlled comparison of search
coverage.
To make the review boundary reproducible, we distinguish three
fixed denominators throughout the manuscript. Thecandidate
registrycontains 246 unique records after deduplication. The
included evidence-mapping ledgercontains 185 records retained
for either primary evidence or background/design context. The
primary empirical subsetcontains 80 records that satisfy all
three conditions: Action Output, Closed-Loop Evaluation, and
an eligible empirical evaluation type (backtest,simulation,
live, or benchmark); all protocol-field and reproducibility
percentages use this 80-record subset unless explicitly stated
otherwise; the design-theme synthesis draws on representative
primary and background work. Table 3 summarizes the resulting
selection flow.
The inclusion boundary for theprimary empirical subsetis
deliberately restrictive: a study must satisfy all three conditions:
(i) Action Output, meaning that the system emits tradable
actions such as orders, position changes, or portfolio allocations;
(ii) Closed-Loop Evaluation, meaning that those actions are
evaluated in backtesting, simulation, or live trading; and(iii)
an eligible evaluation typecoded as backtest, simulation,
live, orbenchmark. The third condition keeps narrative-only
descriptions outside empirical denominators even when action
output and a closed-loop claim are coded present. In the current
S0 v2 registry, 102 included records carry the raw primary
role tag; 22 of these are narrative-only and are assigned to
the background tier for empirical denominators. Thus the 80-
study primary empirical subset plus 105 background/context
records partitions the 185 included studies. Under this rule,
the present snapshot yields 80 primary empirical studies and
105 background studies.
The screening workflow proceeded in four steps. First, database
and preprint searches were run with agent/trading/finance
keyword families and then expanded through backward and
forward citation chaining. Second, duplicate records were
removed by title, arXiv identifier, DOI, and manual inspection.
Third, title/abstract screening removed records outside financial
trading, portfolio construction, execution, or risk-management
settings. Fourth, full-text screening assigned included records
to the empirical primary subset only when all three criteria
above were met; finance-relevant records failing any criterion
were retained as background/context, not final exclusions.
Accordingly, the initial window contributes 19 primary empirical
and 58 background records, while the extension contributes 61
and 47, respectively. These cohorts also differ in coding depth:
the initial-window coding was followed by a targeted extraction
audit, whereas the extension cohort was coded in a single
pass with focused full-text extraction of protocol paragraphs.
Table 4 reports both cohorts alongside pooled coverage. Search
composition and coding depth can both affect these rates; the
5

Table 3:Study selection summary using the canonical candidate registry, combining the initial-window ledger (cutoff2026-03-09) with the
extension window (2026-03-10 to 2026-09-30). The denominator is the 246-record deduplicated registry. Final exclusions are outside the survey
domain; finance-relevant records that lack Action Output, Closed-Loop Evaluation, or eligible evaluation type remain in the included background
tier. Detailed logs and per-record decisions are provided in Supplementary Material S1.
Stage Count
Registry candidate recordsa 246
Included in evidence mapping set 185
Excluded at screening/eligibility 61
Final exclusion reason
Outside finance/trading/portfolio/risk-management scope 61
Included evidence-map partition
Primary empirical subset 80
Background/context tier 105
aThe canonical registry currently contains 246 unique records after deduplication (185 included in the evidence mapping set and 61 excluded at screening/eligibility).
The included evidence mapping set is partitioned into 80 primary empirical studies and 105 background/context records.
ledger does not identify their separate contributions.
The technical chapters synthesize architectural scope through
representative systems and the illustrative A-C-A notes in Ap-
pendix C. The current registry does not contain populated A-C-A
assignments for all 80 empirical studies, so it supports corpus-
level protocol statistics rather than numerical chapter-level taxon-
omy prevalence. Protocol-critical fields include time-consistent
split discipline, execution timing or semantics, transaction-cost
modeling, universe/survivorship handling, and reproducibility
artifacts. Missing or unclear reporting is coded conservatively
asNR/Unknownrather than imputed. This structured coding
enables a transparent, multifaceted synthesis that contextual-
izes reported findings with their respective execution realism,
temporal validity controls, and methodological transparency.
We audited the screening stage on a stratified double-screening
sample of 182 raw screening records in Supplementary Material
S1. Because that sample predates the final initial-window
canonical registry, we retain it only as a screening-boundary
quality check; it does not inform extraction-level protocol fields,
reproducibility tiers, or A-C-A classification robustness. To
address the more consequential coding decisions, we added
a targeted extraction-level audit over 15 fixed-seed initial-
window records sampled from the legacy 41-record primary-role
frame (seed=20260426). Seven of the 15 sampled records
are narrative-only under the current eligible-evaluation-type
rule. This audit therefore checks coding agreement on its
sampled fields; it is not a representative reliability estimate
for the current 80-record primary empirical subset. The
audit covers action output, closed-loop evaluation, evidence
role, evaluation type, split protocol, cost model, execution
semantics, universe/survivorship handling, artifacts, and R0–
R3 reproducibility (Table B.24). The per-study coding sheet
and adjudication notes are provided in Supplementary Material
S3. The extension-window cohort (154 records) was coded in a
single pass from abstract-level screening plus focused full-text
extraction of protocol paragraphs; its per-record decisions are
released in the v2 registry, and its field-level codings should be
read as more preliminary than the audited initial-window subset.
Table 5 summarizes the two audit layers and their scope.
A source check on 2026-10-03 corrected Alpha2 from R2 to R1
because its official repository provides pseudocode rather than a
runnable implementation. The journal version of the explainable
portfolio-policy study also links public code, correcting its old
R0 assignment to R1 (de la Rica Escudero et al., 2025). Its
complete runnable reproduction is not established here. The
current registry and distributions incorporate these amendments;
historical S3 records are retained as coding snapshots. Neither
amended work was in the 15-record reliability sample, so the
recorded 150/150 agreement is unchanged.
The A-C-A framework organizes representative trading systems
by architecture, financial capability, and adaptation. Corpus-
level descriptive statistics for protocol reporting, reproducibility,
and peer-review status are summarized in Appendix B; boundary
decisions and final exclusions are summarized in Appendix D.
Detailed query strings, initial-window screening logs, the
combined registry, current protocol tables, targeted reliability-
audit files, and coding notes are provided in Supplementary
Materials S1–S3. Historical mapping and coding snapshots are
identified separately from the current registry and protocol table.
2.1. Agentic Trading as an Expert-System Decision Pipeline
Within ESWA’s expert-systems framing, we interpret LLM-
based trading agents as expert-system decision pipelines, which
makes the evaluation problem explicit. Perception modules
perform knowledge acquisition from prices, news, filings, social
media, and market microstructure signals. Memory, retrieval-
augmented generation, and tool-mediated context stores form
a knowledge base whose provenance and update rules must
be inspectable. Reasoning modules act as inference engines
that convert state representations into hypotheses, rationales,
and candidate decisions. Action and execution modules form
the external action interface, where target weights, orders,
fills, latency assumptions, and market frictions must be made
explicit. Risk controls, compliance filters, and portfolio limits
6

Table 4:Protocol-field coverage by retrieval and coding cohort. Each cell gives the number reporting the field, cohort denominator, and percentage.
The initial cohort received a targeted extraction audit; the extension received single-pass coding. Differences are descriptive and combine search
composition with coding depth.
Field Initial (n=19) Extension (n=61) Pooled (n=80)
Time split 2/19 (10.5%) 48/61 (78.7%) 50/80 (62.5%)
Transaction costs 1/19 (5.3%) 46/61 (75.4%) 47/80 (58.8%)
Universe/survivorship 1/19 (5.3%) 47/61 (77.0%) 48/80 (60.0%)
Execution semantics 11/19 (57.9%) 36/61 (59.0%) 47/80 (58.8%)
Table 5:Reliability and coding-quality audits reported with the submission package.
Audit layer Sample Observed agreement Agreement note Scope
S1 screening-boundary
audit
182 raw records Reported in S1 Boundary only Inclusion/exclusion and screening-stage labels
S3 extraction-level
audit
15 legacy primary-
role records
All 150 field
comparisons agreed
pre-adjudication
(100.0%)
field-dependent; see
Supplementary Material
S3
Extraction fields used for protocol and reproducibility statistics
serve as rule constraints on the path from inference to action.
Finally, logs, immutable artifacts, and human oversight provide
the explanation and accountability layer expected of decision-
support systems.
This expert-system framing provides a cohesive conceptual
spine for our synthesis. A trading agent’s real-world viability
depends not only on its conceptual design but also on the rigor
of its empirical evaluation—including temporal split integrity,
transaction-cost realism, universe survivorship controls, and
execution fidelity. The A-C-A framework organizes this
multifaceted design space systematically: architecture describes
how market knowledge is acquired, stored, inferred, and acted
upon; capability delineates which core financial functions are
realized; and adaptation examines how the decision pipeline
evolves under non-stationary market feedback.
3. Perceptual Architecture
The preceding section introduced the cognitive architecture of
agentic traders. This section addresses the question: “How do
agents perceive financial markets?”
In this survey, we definePerceptionas the mechanism by which
an agent acquires a state observation Ot from the environment
state S t at decision time t. Under the primary-subset boundary
specified in Section 2, standalone financial NLP or time-series
forecasting models (e.g., isolated BERT or LSTM predictors)
are treated asBackground (BG)unless they form, or are
explicitly integrated into, an evaluated action-producing loop:
component models lack the closed-loop integration required for
agentic classification, although they may still supply perceptual
capabilities that end-to-end agents incorporate.
A perception module must therefore do more than predict; it
must provide actionable state representations—such as sentiment
scores, market regime indicators, or visual summaries—that the
agent’s reasoning component can use to formulate valid actions.
Architectural Role and Design Dimensions.In an autonomous
trading agent, perception functions as the critical observation
interface between external market feeds and internal cognitive
reasoning. Rather than functioning as an isolated prediction en-
gine, the perception layer in an end-to-end agentic architecture
must construct a structured, temporally synchronized observa-
tion Ot that is immediately actionable for memory retrieval,
factor computation, and order formulation. Current literature
explores this design space across three core modalities:
• Textual Perception(Section 3.1): Parsing unstructured
financial news, earnings announcements, filings, and
social sentiments.
• Time-Series Perception(Section 3.2): Encoding numeri-
cal sequences, including order book microstructure, price
trends, and macroeconomic fundamentals.
• Multimodal Perception(Section 3.3): Aligning and
fusing graphical representations (e.g., candlestick charts,
technical patterns) with textual and numerical signals.
Across these modalities, the central design trade-offs revolve
around feature representation density, cross-modal synchroniza-
tion, and latency constraints, balanced against the critical re-
quirement of preventing temporal information leakage.
Figure 3 compares three complementary perceptual modalities
by information source and processing mechanism.
3.1. Textual Perception
Textual perception refers to the acquisition of state observations
Ot from linguistic information sources (news articles, earnings
reports, analyst commentary, social media posts, regulatory
filings) at decision time t. The module encodes textual
inputs into representations—such as sentiment scores, event
embeddings, or contextualized vectors—that the reasoning
component can use to formulate actions.
7

Three Perceptual Modalities in Agentic Trading
Text-based
Input:
Processing:
• News
• Reports
• Social media
• Sentiment
• NLP
• Extraction
Time-series
Input:
Processing:
• Prices
• Volume
• Indicators
• Patterns
• Trends
• Regimes
Multimodal
Input:
Processing:
• Text + charts
• News + prices
• Text + data
• Fusion
• Alignment
• Attention
Figure 3:Three perceptual modalities in agentic trading. Textual perception processes linguistic information from news and reports. Time-series
perception analyzes numerical patterns in price and volume data. Multimodal perception integrates heterogeneous data sources through cross-modal
fusion mechanisms.
Representative Approaches. Several lines of work have devel-
oped specialized architectures for financial text understanding.
Du et al. (2024) provide a comprehensive survey of financial
sentiment analysis techniques, reviewing prior evidence that
sentiment signals are often associated with subsequent market
movements. Iacovides et al. (2024) introduce FinLlama, an
LLM-based approach fine-tuned for financial sentiment analysis
in algorithmic trading scenarios. Zhang et al. (2023a) propose
Instruct-FinGPT, which uses instruction tuning to adapt general-
purpose LLMs to financial sentiment tasks, while Zhang et al.
(2023b) explore retrieval-augmented generation to enhance sen-
timent analysis with external knowledge.
Technical Mechanisms. Textual perception typically follows
a pipeline of tokenization, encoding, and extraction. Domain-
specific language models such as FinBERT (Araci, 2019) pro-
vide contextualized representations of financial text, capturing
terminology and semantic nuances that are often underrepre-
sented in general-purpose models. Rodriguez Inserte et al.
(2024) show that adapting large language models through task-
specific fine-tuning can improve performance on financial sen-
timent tasks. Sentiment classification models then map these
representations to polarity labels (e.g., positive, negative, and
neutral) or to more fine-grained affective states. Xing (2025) fur-
ther studies heterogeneous LLM agents for financial sentiment
analysis and reports improved benchmark performance relative
to selected baselines.
Critical Challenge: Temporal Alignment. A pervasive risk
in text perception is look-ahead bias. News timestamps often
record publication time rather than the moment an item actually
becomes available to a trading pipeline, creating a mismatch
between historical records and executable decision contexts;
agents trained on historical news corpora without explicit
ingestion-lag modeling or embargo enforcement are therefore
likely to exhibit inflated backtest performance. A related
risk arises from post-publication revisions: some financial
disclosures and structured reports are updated after initial release,
so using retrospectively cleaned or final versions in backtesting
can introduce serious data leakage López de Prado (2018).
Table 6 summarizes representative textual perception meth-
ods, highlighting the diversity of data sources and technical
approaches. Because these methods are effective on textual
information but cannot directly process numerical price data
or visual chart patterns, agents also require the complementary
perceptual modalities discussed next.
3.2. Time-Series Perception
Time-series perception refers to the acquisition of state observa-
tions Ot from numerical sequences (price, volume, Limit Order
Books—LOB) and structured fundamental data (e.g., balance
sheet tables) at decision time t. This modality encodes temporal
patterns—such as trend indicators, volatility estimates, or regime
classifications—into representations the reasoning component
can use. Its inputs range from familiar price and volume se-
quences (Open-High-Low-Close-V olume—OHLCV) to deeper
market structures such as LOB and options-implied state vari-
ables. Because these inputs evolve over time, agents must model
temporal dependence, seasonality, structural breaks, and non-
stationarity when constructing actionable state representations.
Representative Approaches. Representative work in this area
studies how sequence models encode information from market
data streams into trading-relevant state representations. Re-
cent systems use transformer-style or attention-based encoders
to summarize price dynamics, while classical econometric ap-
proaches remain useful for regime identification and structural-
change analysis. In the current agentic trading literature, how-
ever, most implemented systems still rely on readily accessible
8

Table 6:Textual perception methods.Audit Status: BG=Background Model (not integrated into agent loop);R0–R3=Reproducibility Level (see
Appendix B).Time Disc.=Time Discipline (Static=offline batch processing;RT=real-time streaming with specified latency).
Reference Input Source Representation Time Disc. Audit
FinBERT Araci (2019) News Headlines Sentiment Score (Scalar) StaticBG
FinGPT Wang et al. (2023a) News/Social Summary/Embedding StaticBG
BloombergGPT Wu et al. (2023) Financial Corpus General LM StaticBG
FinLlama Iacovides et al. (2024) Reports Instruction Tuned StaticBG
Instruct-FinGPT Zhang et al. (2023a) Financial Text Instruction Tuned StaticBG
RAG-FinGPT Zhang et al. (2023b) Mixed Sources Retrieval-Augmented StaticR0
Heterogeneous Agents Xing (2025) Multi-source Specialized Architectures StaticR0
OHLCV-style inputs, while explicit use of high-frequency LOB
data and richly structured fundamentals remains limited.
Technical Mechanisms. Key challenges include non-
stationarity, noise, and sensitivity to temporal misalignment.
Successful approaches often employ attention mechanisms to fo-
cus on informative time points, regime-switching models to cap-
ture structural breaks Hamilton (1989); Bai and Perron (2003),
and representation-learning objectives that improve robustness
under changing market conditions. Standard positional encod-
ings and related sequence-ordering schemes can also help mod-
els capture periodic structure and temporal context in sequential
financial data Vaswani et al. (2017).
Table 7 compares representative time-series perception methods.
Methods that operate on numerical sequences alone cannot
directly incorporate the rich contextual information available in
text; vision-language variants such as VISTA that render series
as charts already illustrate the cross-modal direction developed
next.
3.3. Multimodal Perception
Multimodal perception refers to the acquisition of state obser-
vations Ot from heterogeneous sources (chart images, text, nu-
merical series, audio) at decision time t, integrating these into
unified representations through cross-modal alignment mecha-
nisms. This mirrors trading practice, in which traders synthesize
visual technical patterns with news flow and price action.
Representative Approaches. For visual perception, Wang
et al. (2023b) introduce FinVis-GPT for financial chart analysis,
which treats chart-like market representations as visual inputs
amenable to language-based interpretation. For multimodal
fusion, Zhang et al. (2024) introduce FinAgent, which combines
textual news and numerical market information through a cross-
modal pipeline designed for trading decisions. More broadly,
multimodal systems differ in where fusion occurs along the
pipeline, a distinction examined under Technical Mechanisms
below.
Critical Challenge: Cross-Modal Asynchrony. Fusing modal-
ities with different update frequencies creates synchronization
risks. News arrives sporadically, whereas market and LOB
data may update at much higher frequencies. Naive framing
strategies such as pairing the latest available news item with the
current price can therefore misrepresent the true decision con-
text when the text signal is stale. Moreover, visual interpretation
and multimodal inference introduce nontrivial latency, so the
perceived market state may already be outdated by the time the
agent acts in live settings. Protocol reporting should therefore
state perception-latency assumptions and alignment procedures
explicitly.
Technical Mechanisms. Multimodal fusion poses significant
challenges because modalities differ in dimensionality, temporal
resolution, and noise characteristics. Early fusion concatenates
raw features from all modalities before processing, while late
fusion maintains separate processing pipelines and combines
high-level representations. Cross-attention mechanisms provide
a flexible alternative by enabling one modality to attend
selectively to another during representation learning Vaswani
et al. (2017); Tsai et al. (2019). The temporal-alignment problem
noted above is especially acute in financial settings, since
textual events arrive discretely while prices update continuously;
preventing look-ahead bias therefore requires strict timestamp
discipline, explicit embargo handling, and clearly reported
latency budgets López de Prado (2018).
Figure 4 illustrates the multimodal fusion pipeline, showing
how text encoders process news and reports while time-series
encoders analyze price movements, with a cross-modal fusion
layer integrating these representations.
Table 8 summarizes representative visual and multimodal
perception approaches. Taken together, these studies suggest
that richer market state estimation often benefits from combining
heterogeneous signals rather than relying on a single modality
in isolation.
Extension-window additions.The extension cohort adds
perception-side infrastructure rather than new modalities:
mechanism-based decomposition of market dynamics for down-
stream agents Chen (2026b) and synthesized financial tool-
use data that couples perception to callable tools Huang et al.
(2026a). Both remain background-level designs in our ledger,
but they illustrate how the perception layer is being engineered
as a service for agent pipelines rather than as a standalone pre-
dictor.
Synthesis and Design Considerations.Perceptual architecture
turns heterogeneous market feeds into state observations Ot.
Textual, time-series, and multimodal inputs differ in source and
processing, while all require temporal alignment; multimodal
fusion adds cross-modal synchronization, and each design must
control look-ahead bias and latency. These observations feed the
memory and retrieval systems examined next.
9

Table 7:Time-series and structured perception methods. Audit and Time Disc. tags follow the convention in Table 6.
Reference Input Data Mechanism Time Disc. Audit
VISTA Khezresmaeilzadeh et al. (2025) Chart Images+Text Zero-Shot VLM Inference StaticR0
Regime-Switching Hamilton (1989) Returns Hidden Markov Model StaticBG
Figure 4:Multimodal fusion flow in agentic trading. The diagram illustrates how text encoders and time-series encoders process their respective
inputs before a cross-modal fusion layer integrates the representations into a unified market understanding.
Table 8:Visual and multimodal perception methods.Latency: Estimated inference latency (critical for alignment).Note: Latency estimates are
author-reported; see Supplementary Material S2 for detailed benchmarking protocols. Audit tags follow the convention in Table 6.
Reference Modalities Fusion Strategy Latency Audit
FinVis-GPT Wang et al. (2023b) Chart Images Vision-Language Analysis LowBG
FinAgent Zhang et al. (2024) News+Prices+Kline Charts Cross-Attention HighR0
Multimodal Transformer Tsai et al. (2019) Text+Audio+Vision Cross-Modal Attention MedBG
Table 9:Summary of perceptual architectures in trading agents. TheProtocol Riskcolumn highlights specific alignment challenges for each
modality.
Modality Primary Inputs Mechanism Protocol Risk Examples
Textual News, Reports, Social Media LLM Fine-tuning, Prompting, Senti-
ment Analysis
Publication Lag, Embargo Violations FinBERT, FinGPT
Time-Series OHLCV , LOB, Fundamentals Temporal Attention, Regime Switch-
ing
Look-ahead Bias, Data Revisions VISTA
Multimodal Charts, Text+Price+Audio Vision-Language Analysis, Cross-
Modal Attention
Synchronization Latency, Causal Misalignment FinVis-GPT, FinAgent
4. Memory Architecture
The preceding section introduced perceptual mechanisms for
gathering market information. This section asks how agents
store, retain, and retrieve that information. It focuses on memory
as an organized state store; Learning Paradigms examines how
agents use feedback to update behavior, while Self-Evolution
examines how retained state and update policies change over
time.
Memory serves three operational roles:working memorymain-
tains active trading context,associative vector storageretrieves
historical episodes by similarity, andstructured knowledge
basespreserve explicit financial information. The core design
challenges are balancing retrieval relevance against context-
window saturation, mitigating retrieval drift, and maintaining
temporal causality across long trading horizons. These cate-
gories are examined in Section 4.1, Section 4.2, and Section 4.3,
respectively. Earlier agent literature also uses cognitive termi-
nology: working memory follows Baddeley and Hitch (1974),
episodic and semantic memory follow Tulving (1972), and multi-
store models draw on Atkinson and Shiffrin (1968). These cogni-
tive descriptions provide context for memory-augmented designs
Zong et al. (2024); the categories below identify the storage and
retrieval mechanisms rather than biological memory processes.
4.1. Working Memory
In agentic trading, working memory is often conflated with a
generic “context window.”For robust agent design, we distin-
guish between theDeterministic State Store(Layer A) and the
Generative Context(Layer B).
Layer A: Deterministic State Store (Audit-Truth). This layer
holds the ground-truth state of the trading system, including
current positions, open orders, account balances, and risk limits.
In a reliable trading architecture, we argue that it should beread-
onlyto the LLM and updated solely by the environment (e.g.,
EMS/OMS feedback). Treating this state as a “memory”subject
to forgetting or hallucination is a critical vulnerability; in
practice, it is better implemented as a structured store exposed
through tools or state queries, as seen in tool-using trading agent
designs Xiao et al. (2024).
10

Working memory
Immediate context
Capacity: limited
Seconds–minutes
Associative vector
storage
Trading episodes
Capacity: large
Long-term
Structured
knowledge base
Explicit facts
Persistent store
Updatable
Consolidation Abstraction
Figure 5:Three memory categories in agentic trading. Working memory maintains active trading context, associative vector storage supports
retrieval of historical trading episodes, and structured knowledge bases preserve explicit financial information. Arrows denote consolidation from
working context into stored experience and abstraction from experience into reusable structured knowledge.
Layer B: Generative Context (Inference Scope). This layer
corresponds to the LLM’s active context window, containing
the sliding history of observations, chain-of-thought reasoning
traces, and recent reflections. Unlike Layer A, information here
is transient and subject to eviction.
Technical Mechanisms. To manage Layer B’s limited ca-
pacity, agents employ eviction policies such asSummary-
Compression(condensing old steps into a narrative) orhier-
archical memory management(using layered storage and re-
trieval priorities to retain higher-value fragments) Packer et al.
(2023); Sun and Zeng (2025). FinMem Yu et al. (2023b) adopts
the same layered pattern in a trading setting, buffering recent
context in a working layer atop its deeper memory layers; it is
therefore listed under working memory in Table 11. A key de-
sign trade-offis thecontext-to-noise ratio: maintaining too much
history can dilute attention and bury decision-relevant content
in long contexts, a risk consistent with the broader “Lost in the
Middle”finding Liu et al. (2024), while aggressive pruning may
drop reasoning that is still relevant to a live position or pending
order.
Table 10 summarizes the three memory categories, highlighting
their differing capacity constraints and temporal scales. Working
memory enables rapid decision-making, while associative vector
storage and structured KBs support longer-term retrieval and
knowledge accumulation.
4.2. Associative Vector Storage
Associative vector storage provides a way to index and retrieve
stored experience through learned or engineered similarity.
Trading episodes may be represented this way, but not every
episodic store uses vector embeddings. To keep retrieved
episodes auditable, we define a valid episode as a tuple
(S t,A t,O t+k,τ ), where S t is the state, At the action, Ot+k the
outcome realized at step t + k, andτ the timestamp at which this
outcome becomes observable.
Information Leakage via Memory. We refer to a key
vulnerability in trading agents as the “Oracle Fallacy,”in which
an agent retrieves a similar past episode that contains apost-
hocnarrative (e.g., “this trade failed due to news X released
tomorrow”).
Protocol Implication
To prevent such leakage, we suggest that reproducible
trading-agent protocols enforce anOutcome Embargo:
an episode recorded at t cannot expose its outcome field to
retrieval until current timet now≥τ.
Complementary work addresses deterministic replay in finan-
cial agents, providing assurance frameworks for regulatory au-
dit Khatchadourian (2026).
Representative Approaches. FinAgent (Zhang et al., 2024)
uses layered memory and diversified retrieval, with temporal
control primarily at the prompt level rather than through explicit
database constraints. FinMem (Yu et al., 2023b) organizes
memory in layers, while Reflexion (Shinn et al., 2023) stores
unsuccessful trajectories as lessons. These examples illustrate
storage and retrieval choices; their cross-time update governance
is considered in Section 12.
Technical Mechanisms. Vector databases Johnson et al. (2017);
Malkov and Yashunin (2020) enable similarity search, but naive
cosine similarity is often insufficient for financial time series,
where relevance also depends on recency and regime. “Time-
Aware Retrieval”therefore becomes a useful design principle.
Protocol Implication
We suggest a relevance score f (q,k ) that includes a decay
terme−λ(tnow−tk) to prioritize recent regimes.
Furthermore,Drift Handlingis required: as market regimes
shift (e.g., from low to high volatility), old episodes with
high feature similarity may still yield misleading expectations,
a risk consistent with recent retrieval-augmented time-series
forecasting evidence Xiao et al. (2025a).
4.3. Structured Knowledge Bases
Structured knowledge bases store explicit domain knowledge
(e.g., “high interest rates hurt growth stocks”). Their auditability
depends on provenance and update controls, not only on format
(graph vs. text). Model weights can also encode financial
knowledge, but that parametric knowledge is a related, implicit
mechanism rather than a structured KB: it is not an external
source-addressable store and should not be classified as one.
11

Table 10:Memory system comparison.
Memory Category Capacity Volatility Key Characteristics
Working Memory Limited (Context) V olatile Fast cache, eviction policies, sliding window
Associative Vector Storage Large (Disk) Persistent Vector embeddings, similarity search, temporal indexing
Structured Knowledge Base Source-dependent Persistent Knowledge graphs, sourced records, explicit relations
Related mechanism: parametric knowledge (implicit). This
knowledge is encoded in model weights via pre-training or fine-
tuning (e.g., FinGPT (Wang et al., 2023a)). While efficient, it
isopaque—it is difficult to tracewhythe model knows a fact—
andstatic, since updates usually require additional training or
alignment. For trading, this raises the risk of “outdated priors,”in
which older market regularities persist in model behavior after
the regime that produced them has changed.
Structured KBs (explicit, non-parametric)retrieve informa-
tion from an external source. We distinguish:
• Curated KBs: Verified documents (Rulebooks, SEC
Filings) where source integrity is high Wang et al. (2025b).
• Uncurated KBs: Open-web data (Social Media, Forums)
susceptible to “Noise Injection”or adversarial poisoning.
Technical Mechanisms. To preserve source integrity, “Source
Tracking”is required: every retrieved retrieved fact should
carry a provenance log (Document ID+Version Timestamp).
Knowledge Graphs encode explicit entity-relation structure
(e.g., Entity A
supplier_o f
−−−−−−−−→EntityB) and can therefore support
provenance-oriented reasoning and constraint checking more
directly than unstructured text alone.
4.4. Design Trade-offs
A systematic architectural analysis of these systems reveals key
design trade-offs that performance-only benchmarks tend to
obscure.
Latency vs. Recall Depth. Deeper retrieval in high-fidelity
RAG systems can introduce latency that is incompatible with
high-frequency or rapid mid-frequency strategies. Agents
therefore need to balanceretrieval depthagainstdecision latency
andexecution speed.
Context Length vs. Distraction. Although newer LLMs
support 1M+token windows, loading all retrieved memories
into context degrades reasoning through the “Lost in the Middle”
phenomenon Liu et al. (2024). A disciplined memory design
therefore favorslessbuthigher-relevancecontext over an
unfiltered dump of history.
Noise Injection Risk. Allowing uncurated knowledge sources
(e.g., scraping Reddit) increases the risk of “Noise Injection,”in
which irrelevant or manipulated public sentiment overrides the
agent’s underlying strategy. We therefore adopt a “Hierarchy
of Truth”as a design principle: internal Layer A state should
override external noisy signals when the two conflict.
Extension-window additions.The extension cohort contributes
several memory- and retrieval-facing designs. On the knowledge
side, LLM-enhanced dynamic financial knowledge graphs sup-
port cross-entity retrieval for trading decisions Zhang (2026b),
and a benchmark for event-grounded personalized memory eval-
uates retention of investor-specific context across sessions Wang
et al. (2026a). On the retrieval side, document-routed hybrid
retrieval Cheng et al. (2026b) and time-series augmented gen-
eration Kolonin et al. (2026) target the financial RAG layer
that can feed vector stores and structured KBs. A cautionary
complement: information-fidelity analyses show that aggressive
summarization can distort the very inputs a memory layer is
meant to preserve Lee et al. (2026)—reinforcing the “Hierarchy
of Truth” principle above.
Synthesis and Design Considerations.Memory architecture
provides temporal depth and experiential continuity: working
memory tracks active trading state, associative retrieval selects
historical episodes, and structured knowledge bases preserve
explicit information. Retrieval depth must be balanced against
latency and context distraction, while temporal rules and prove-
nance checks protect against hindsight leakage and preserve
source traceability. The retrieved context feeds the reasoning
engine examined in Section 5.
5. Reasoning Architecture
Having examined how agents perceive markets and store
information, we now address the question: “How do agents make
trading decisions?” Building on the notation from Section 3 and
Section 4, we write Ot for the state observation at time t and
Massoc for retrieved associative memory.
We treat reasoning as the decision function that transforms
perceptions and memories into candidate actions. Because
decision horizon, computational budget, and search depth are
more directly auditable than broad cognitive analogies, we
organize reasoning architectures along aTime-Scale Reasoning
Paradigm. The three paradigms below loosely echo the
System 1/System 2 distinction of dual-process theory, although
that framework offers no consensus definitions for long-horizon
planning; we therefore use the analogy strictly as a shorthand
for latency and compute budget, not as a cognitive claim.
Architectural Role and Reasoning Spectrum.Reasoning is the
cognitive engine of an agentic trading system, converting state
representations Ot and retrieved memories into structured, ac-
tionable trading hypotheses. Financial markets present a unique
cognitive challenge characterized by non-stationary dynamics,
12

Current context
State · positions
Market event
Query
Retrieval key
Associative
vector storage
Similarity search
Relevant episodes
Top-k · time-aware
Current decision
Reasoning input
Update context
Figure 6:Memory retrieval mechanism. The agent formulates a query based on current context, searches an associative vector store using
similarity-based retrieval, and selects relevant episodes to inform the current decision.
Table 11:Comparison of memory retrieval mechanisms in trading agents. Tags follow the convention in Table 6 for the representative works in
each row. NR=not reported; N/A=not applicable.
Memory Category Representative Ref Timestamp Rule Embargo Drift Check Audit Status
Working Memory FinMem Yu et al. (2023b) N/A N/A N/AR0
Episodic memory (paper term) FinAgent Zhang et al. (2024) NR NR NoR0
Parametric knowledge (related) FinGPT Wang et al. (2023a) Implicit No NoBG
Structured Knowledge Base FinSage Wang et al. (2025b) Versioned Yes (Doc Date) YesBG
low signal-to-noise ratios, and severe latency constraints. To
address these demands, reasoning architectures operate across a
spectrum of decision timescales:
• Reactive Control(Section 5.1): Sub-second rule-based
or specialized policy execution, optimized for immediate
order adjustments and safety stops.
• Reflective Reasoning(Section 5.2): Second-scale delib-
erative inference utilizing chain-of-thought, self-critique,
and tool execution to formulate structured trade rationales.
• Strategic Planning(Section 5.3): Multi-minute or daily
planning loops employing tree search (e.g., Monte Carlo
Tree Search) and multi-step scenario simulation over
extended horizons.
The central engineering trade-offlies in balancing cognitive
depth and reasoning faithfulness against computational latency
and the risk of search-based overfitting.
Table 12 contrasts the three paradigms in terms of time-scale,
mechanism, reproducibility level, and evaluation considerations.
Terminological Clarification: Reactive Reasoning
We use “reactive” strictly fornon-LLMlatency-constrained
control. LLM-based methods (including ReAct adaptations)
operate at second-scale or slower, placing them in the
reflectivecategory. This distinction matters because it
prevents the misconception that LLMs can support high-
frequency trading decisions.
Figure 7 illustrates the time-scale comparison.
Reasoning I/O Contract. Formally, we model the agen-
tic reasoning module as a structured decision function
f(O t,M assoc,P port f olio)→(A cand,α,V check), where:
• Inputs: timestamped observation Ot, retrieved associative
memory Massoc, and read-only portfolio state Pport f olio
(positions, risk limits).
• Outputs: a set of candidate actions Acand, a confidence
scoreα∈ [0, 1], and a validity check Vcheck (e.g., “holds
<max_leverage”).
The contract is designed to reduce the risk of “hallucinated
actions” by enforcing risk constraintsduringorimmediately
afterthe reasoning step, rather than leaving them entirely to the
final execution layer.
5.1. Reactive Reasoning
Reactive reasoning, the System 1 end of the analogy above,
denotes aconstrained, simplified decisionoptimized for
latency budgets measured in microseconds to milliseconds.
Importantly, this paradigmdoes notinvolve LLM-mediated
deliberation—the latency of even lightweight LLMs (hundreds
of milliseconds) exceeds the budgets of high-frequency trading.
Instead, reactive trading systems employ rule-based controllers,
lightweight neural networks (often<100K parameters), or pre-
compiled decision tables that execute in constant time.
Representative Approaches. ReAct (Yao et al., 2023b)
exemplifiesreflective(not reactive) reasoning in general agent
architectures—its “think” step involves explicit LLM inference
that operates at second-scale latency. In trading contexts
requiring millisecond response times, ReAct-style deliberation
must bedecoupled from the critical pathand confined to offline
analysis or non-latency-sensitive decision support. Rule-based
systems encode expert knowledge as if-then rules (e.g., “if
13

Three Reasoning Paradigms in Agentic Trading
Reactive control
Characteristics:
Use Cases:
• Fast, intuitive
• Pattern recognition
• Pre-computed actions
• Fast execution
• Order execution
• Risk monitoring
Reflective reasoning
Characteristics:
Use Cases:
• Deliberate reasoning
• Multi-step CoT
• Self-reflection
• Strategy analysis
• Decision evaluation
• Risk assessment
Strategic planning
Characteristics:
Use Cases:
• Long-term planning
• Tree search
• Hierarchical planning
• Portfolio optimization
• Asset allocation
• Strategic planning
Figure 7:Three complementary reasoning roles: reactive control supports fast operational responses, reflective reasoning evaluates decisions
through deliberation and self-reflection, and strategic planning explores longer decision horizons. Their latency depends on the model, hardware,
tools, and search budget.
Table 12:Comparison of reasoning paradigms.R-Level: Reproducibility level (R0–R3, see Appendix B).Evaluation considerationssummarize
protocol dimensions relevant to interpreting reported results.
Paradigm Time-Scale Mechanism R-Level Representative Works Evaluation consider-
ations
Reactive Microsecond–millisecond budgets Rule-based/
Lightweight NN
(often<100K params)/
pre-compiled decision
tables
R0–R1 ReAct Yao et al. (2023b) (reflective,
not reactive), reactive components in
FinAgent Zhang et al. (2024)
Execution Latency of-
ten ignored
Reflective Seconds CoT/Self-Critique R0–R1 FinCoT Nitarach et al. (2025), FinCon
Yu et al. (2024)
Inference Cost not re-
ported
Strategic Minutes/Hours MCTS/Planning R0–R1 Alpha Jungle Shi et al. (2025), RAP-
TOR Almon et al. (2025)
Search Budget &
Overfitting Risk
price crosses moving average, buy”) and execute immediately
once the conditions are met, sacrificing flexibility for speed
because they rely on pre-defined patterns rather than reasoning
from first principles. Consequently, the reactive paradigm
is most effective in relatively stable market regimes where
previously learned patterns remain actionable. In agentic trading
settings, this shallow-loop structure typically appears as a
reactive component inside larger systems—for example, through
tool-augmented signal retrieval coupled with constrained actions
(Zhang et al., 2024), or through role-specialized teams that
decompose perception while preserving a structured final
decision pipeline (Xiao et al., 2024). Gradient-based policy
optimization can further couple reactive decisions to reward-
driven updates in interactive markets (Xiong et al., 2025).
Technical Mechanisms. Reactive systems employ feature
extractors that map raw market data to action logits and then
select and execute the highest-logit action. Shallow neural
architectures with limited reasoning depth are common because
they balance prediction speed against accuracy; typical choices
include temporal convolutional networks for processing time-
series data Bai et al. (2018) and attention mechanisms for
weighting relevant features Vaswani et al. (2017). A further
advantage isrelativeinterpretability: because the mapping runs
from a small feature set to actions, it can be inspected and
constrained Lundberg and Lee (2017), although inspection alone
does not guarantee faithful explanations of the decision logic.
The same simplicity, however, limits adaptability: these systems
struggle with novel situations outside their training distribution,
and when market structure shifts abruptly they may continue
applying outdated patterns, potentially leading to significant
losses.
Beyond latency, the integration of tool use into financial agents
requires explicit evaluation along at least two dimensions: Agent-
Guard studies safety-oriented evaluation for tool orchestration
Chen and Cong (2025), whereas FinToolBench measures the
capability of LLM agents to use financial tools in realistic tasks
14

Lu et al. (2026). Autonomous agent frameworks can likewise
strengthen complex reasoning over structured knowledge Jiang
et al. (2024).
5.2. Reflective Reasoning
Reflective reasoning, the System 2 counterpart in the same
analogy, produces slow, deliberate decisions through multi-step
chains of thought. This paradigm enables agents to reason
through complex scenarios, consider multiple hypotheses, and
reflect on potential mistakes before acting. Unlike reactive
systems that respond immediately to stimuli, reflective reasoning
allocates computational resources to explore the decision space
more thoroughly, which makes it suitable for medium-frequency
trading where execution latency on the order of seconds is
acceptable.
Representative Approaches. Chain-of-Thought (CoT) prompt-
ing (Wei et al., 2022) guides LLMs to explicitly reason through
trading decisions, producing intermediate steps such as “the
stock price dropped because of worse- than-expected earnings,
but the long-term fundamentals remain strong, so this is a buy-
ing opportunity.” FinCoT (Nitarach et al., 2025) adapts CoT to
finance through domain-grounded prompting that encourages
financial reasoning in trading tasks. FinCon (Yu et al., 2024)
operationalizes reflective workflows through multi-agent or role-
structured coordination that updates investment beliefs over time.
CryptoTrade (Li et al., 2024c) and TradingGroup (Tian et al.,
2025) further instantiate this reflective pattern by revising trading
decisions based on prior outcomes and synthesizing multi-source
signals. Reflexion (Shinn et al., 2023) extends this paradigm
with self-reflection, in which agents critique their own reasoning
and refine their conclusions before acting. A Reflexion-based
trader, for example, might generate an initial trading rationale,
identify potential flaws in its logic (such as overlooking sector-
wide risks), and revise its decision accordingly.
Technical Mechanisms: Protocol Implication
We synthesize five stages for reflective trading decisions: (1)
analyze the current situation; (2) retrieve relevant memories;
(3) consider multiple hypotheses; (4) assess each candidate
action’s benefits and risks; and (5) select an action and
justify the choice.
Temperature sampling controls the trade-offbetween creativity
and consistency, with lower temperatures producing more deter-
ministic reasoning. A recurring challenge is maintaining coher-
ence across long reasoning chains, since LLMs may lose context
or contradict themselves over dozens of steps; checkpointing
(saving intermediate reasoning states) and consistency checks
(verifying that conclusions follow from premises) help mitigate
these issues Wei et al. (2022); Wang et al. (2022); Madaan et al.
(2023). The computational cost of reflective reasoning scales
linearly with the number of reasoning steps, so it is more expen-
sive than reactive approaches but also significantly more capable
of handling novel situations that require adaptation.
A further caveat concerns feedback timing: Reflexion-style
systems assume relatively prompt feedback, whereas trading
outcomes often materialize only after meaningful market delay
Shinn et al. (2023). Beyond self-critique loops, modern risk-
sensitive frameworks provide structured decision support for
financial markets, although their exact internal decomposition
varies by implementation Liu and Dang (2025b).
5.3. Strategic Reasoning
Strategic reasoning extends beyond immediate decisions to plan
across extended time horizons, weighing sequences of actions
and their long-term consequences. This paradigm addresses
questions such as “what portfolio allocation will maximize risk-
adjusted returns over the next quarter?” rather than “should I
buy this stock right now?” It operates at time scales of minutes
to hours, which suits portfolio optimization, risk management,
and longer-term investment strategies where thorough planning
matters more than immediate execution.
Representative Approaches. Tree-of-Thought (ToT) (Yao
et al., 2023a) frames reasoning as search through a tree of
possible thoughts, exploring multiple reasoning paths in parallel
and selecting the most promising through explicit evaluation.
Each node in the tree represents a partial reasoning state, and
the algorithm systematically explores alternatives rather than
committing to the first plausible solution. Monte Carlo Tree
Search (MCTS) methods such as Navigating Alpha Jungle (Shi
et al., 2025) apply the same idea to the space of possible trading
strategies, using rollouts to estimate the long-term value of
each candidate strategy. These methods balance exploration
(trying new strategies) against exploitation (refining known good
strategies) through upper confidence bounds applied to financial
domains. Planning ideas from classical AI and reinforcement
learning continue to inform strategic trading design: state
spaces represent market conditions and actions represent trading
decisions. For portfolio-scale planning, RAPTOR (Almon
et al., 2025) integrates deliberative portfolio reasoning with
an orchestrated rebalancing pipeline to produce interpretable,
risk-aware allocations.
Technical Mechanisms. Strategic reasoning requires models
of the environment—predicting how market prices will evolve
in response to trading actions. Model-based methods learn
explicit transition models that capture causal relationships
between actions and market states, which then allow agents
to simulate future scenarios and evaluate action sequences
without executing them. Model-free methods instead learn value
functions directly from experience, estimating the long-term
return of each state-action pair without an explicit environment
model Sutton and Barto (2018). To keep planning tractable,
hierarchical schemes decompose long horizons into shorter
sub-problems: a strategic planner sets high-level targets (e.g.,
“reduce tech exposure by 20%”), and tactical planners execute
specific trades to achieve these targets. Abstraction is critical
here—planning over individual stocks is intractable because the
space of possible portfolios explodes combinatorially, whereas
planning over sectors or factors reduces the state space to
manageable dimensions. A strategic planner might therefore
operate at the level of sector allocations (technology, healthcare,
15

energy), while tactical planners handle individual stock selection
within each sector, so that agents can reason about long-term
objectives while remaining computationally feasible Kocsis and
Szepesvári (2006); Sutton et al. (1999).
Critical Challenge: Search-Based Overfitting. Unlike game
environments (e.g., Go, Chess) where simulated rollouts are
exact, financial planning relies on noisy historical data. Search
algorithms (MCTS, ToT) that evaluate thousands of candi-
date strategies therefore face themultiple testingproblem—a
profitable-looking trajectory may emerge purely by chance. To
mitigate thisdata snoopingrisk, reproducible evaluation requires
reporting theSearch Budget(number of visited nodes) and en-
forcing strictWalk-Forward Validation, in which the plan is
frozen before being applied to out-of-sample data Bailey et al.
(2014).
Hybrid Architecture: Cascaded Controller. To balance
these trade-offs, advanced systems can employ what we call
aCascaded Controllerarchitecture (cf. Figure 7 for the
paradigms it routes among): a master intent router classifies
the market regime (e.g., “Flash Crash” vs. “Stable Trend”)
and routes execution to the appropriate paradigm, triggering
lower-level reactive stops in volatile conditions while scheduling
strategic re-allocations during calm periods. This architectural
recommendation synthesizes principles observed in hierarchical
trading systems Yu et al. (2023b); Xiao et al. (2024).
Extension-window addition.Complementing the paradigm
taxonomy, work in the extension cohort examines how market
state isrepresentedfor reasoning: representation signatures that
align internal features with risk-feedback signals Xue (2026)
probe whether an agent’s reasoning is grounded in decision-
relevant structure rather than surface patterns.
Synthesis and Design Considerations.Reactive control, re-
flective reasoning, and strategic planning trade decision speed
against deliberation and search depth; reflective methods depend
on alignment with market timescales, while strategic search re-
quires explicit exploration budgets and walk-forward verification
to guard against data snooping. Candidate decisions then pass
to the action execution layer examined next.
6. Action and Execution Architecture
The preceding sections examined perception, memory, and
reasoning. This section addresses the complementary question:
“How do agents turn decisions into market actions?”
Architectural Role and Execution Scope.The action and execu-
tion architecture bridges cognitive reasoning with the physical
reality of financial markets, marking the definitive boundary be-
tween an abstract forecasting model and a genuine trading agent.
While forecasting models evaluate directional accuracy on paper,
an autonomous trading agent must transform high-level inten-
tions into executable market orders subject to microstructure
frictions, liquidity limits, and latency budgets. The execution
design space encompasses three key dimensions:
• Decision-to-Order Mapping: Translating target weights
or directional convictions into discrete order specifications
(order side, quantity, limit price, time-in-force).
• Execution Policies and Cost Modeling: Implementing
algorithmic order slicing (e.g., TW AP, VW AP, POV) and
explicitly modeling fees, spreads, and market impact.
• Microstructure and Latency Management: Incorporat-
ing order book dynamics, fill probabilities, and exchange
round-trip latency into trade scheduling.
Action I/O Contract. Formally, we model the action execution
module as a structured function f (Dt)→ (Aorder,A algo) (see
Figure 8), where:
• Input: Decision output Dt (e.g., target portfolio weights
w∗ t or signals t).
• Output: A set of executable orders Aorder (with strictly
typed fields: side, size, limit price, time-in-force (TIF))
and an execution algorithm selection Aalgo (e.g., “submit
immediately” or “TW AP over 5 min”).
• Failure Modes: The interface typically handlesRejection
(risk check failure),Partial Fill(liquidity shortage), and
Timeout(latency violation), feeding these states back to
memory.
The contract is designed to prevent “implicit execution,” in
which an agent is assumed to trade at the close price without
order-generation delays or constraints.
Comparability note.Protocol-comparable action/execution
claims typically report MR-3 (action semantics), MR-4 (exe-
cution & costs), and MR-6 (artifacts & logs); see Section 13.
6.1. Decision-to-Order Mapping
First Principle: Action Definition Risk.A critical failure
mode in agent design is the ambiguity betweentarget weights
(portfolio intent) andexecutable orders(market instructions). If
an agent emits only target weights without explicitly modeling
order timing, fill constraints, and costs, evaluation quietly
collapses intent into execution and thereby underestimates the
execution gapand liquidity constraints Zhang et al. (2024); Chen
et al. (2022); Cheridito and Weiss (2025); Liu and Dang (2025a);
Papadakis et al. (2025); Olby et al. (2025).
In the surveyed systems, action modules translate high-level
decisions (e.g.,increase exposure) into concrete order instruc-
tions. This mapping depends on explicit choices about order type
(limit versus market) and queue position, because microstruc-
ture theory models execution probability as a function of order
aggressiveness and market state Foucault (1999); Parlour (1998).
Constraints such as pre-trade validation and kill switches then
act as safeguards that keep theoretical alpha from becoming
realized losses once market impact is accounted for Kyle (1985);
Glosten and Milgrom (1985).
16

Figure 8:From decision to execution. Agent outputs map into order parameters and are executed with explicit cost and impact modeling under
market microstructure constraints.
Table 13:Representative action/execution approaches and evaluation dimensions.Type: E2E=end-to-end agent literature; Algo=algorithmic-
execution literature. Note thatAgentliterature often adopts simplified assumptions (Sim-based), whereasAlgoliterature focuses on execution
quality but lacks agentic reasoning.Evaluation considerationssummarize execution details relevant to interpreting reported results.Tagsfollow
the R0–R3 reproducibility-level convention (see Appendix B).
Category Type Action Space Core Mechanism Cost Assumption Evaluation consider-
ations
Tags
Schedule-based Algo Order schedule TW AP/VW AP-style scheduling Explicit fees Slippage Calib.R0
RL Execution Algo Market Orders Policy optimization in simulator Impact-aware reward Latency BudgetR0
Sim-based RL E2E Order-level Market simulator+RL Simulator-dependent Decision TimingR0
Microstructure Algo Limit Orders Fill/LOB modeling Implicit via LOB Realized SpreadR0
Hierarchical E2E Meta-Actions Hierarchical RL for order types Explicit/implicit Failure ModesR0
6.2. Execution and Cost Modeling
Execution policies determine how orders are placed over time
and across venues. Typical approaches include schedule-
based execution (e.g., time-weighted average price (TWAP)
and volume-weighted average price (VWAP)), cost-aware op-
timization that trades urgency against market impact Almgren
and Chriss (2001); Bertsimas and Lo (1998); Perold (1988), and
learning-based execution that adapts to market conditions. Re-
cent studies apply deep learning and reinforcement learning to
execution and impact-aware trading Genet (2025); Byun (2023);
Cheridito and Weiss (2025); Hafsi and Vittori (2024); Chen
et al. (2022); Olby et al. (2025). Within this line, FinPos Liu
and Dang (2025a) introduces a position-aware trading agent
designed for real financial markets, emphasizing continuous
portfolio adjustment, while StockSim Papadakis et al. (2025)
provides a dual-mode order-level simulator for evaluating multi-
agent LLMs in financial markets and thereby enables realistic
execution modeling. Table 13 contrasts representative action
and execution approaches across these categories, summarizing
their action spaces, cost assumptions, and common audit gaps.
6.3. Microstructure and Latency Awareness
Microstructure signals (order book imbalance, spread, queue
position) act not merely as inputs for optimization but ashard
feasibility constraintsthat filter the action space. Throughout,
LOBdenotes the real-time queue of outstanding buy and sell
limit orders; its features include imbalance (bid versus ask
volume), spread, and depth.
1. Data Availability: Agents can incur “look-ahead bias”
when they act on LOB features (e.g., Imbalancet) that are
not yet available at decision time t because of processing
latency; feasible actions must therefore be conditioned on
Ot−δ.
2. Latency Budget: In high-frequency regimes, thela-
tency budget—the time from perception to exchange
acknowledgment—determines whether an arbitrage op-
portunity still exists Budish et al. (2015): if Tcompute >
Tdecay, the action at is invalid regardless of its theoretical
alpha.
Models of order book dynamics Gould et al. (2013); Briola
et al. (2024) then allow these constraints to be validated before
execution.
Protocol Implication
Beyond execution optimization, LLMs can supportpost-
trade narrativesby summarizing execution logs. To
reduce “ex post rationalization” (in which the LLM invents
a strategic reason for a random failure), we recommend
grounding these narratives inimmutable logsand replayable
evidence Tan et al. (2025a); Khatchadourian (2026).
• Recommendation: Narrative generation can
cite the specific Order_ID and cryptographic
S napshot_Hashproduced by the execution layer.
• Verification: Auditors can replay the
17

S napshot_Hash to check whether the market con-
dition claimed by the narrative (e.g., “high spread”)
actually held.
Without thisLog-to-Narrative Verificationlink, LLM explana-
tions remain qualitative summaries rather than audit artifacts.
Extension-window additions.The extension cohort sharpens
the execution side along two directions. First, evaluation
infrastructure: systematic benchmarking of learning-based
equity trading Wang and Zhang (2026) and inference-time
optimization that plans before committing orders Go et al.
(2026) both treat the decision-to-order mapping as a measurable
component rather than an implementation detail, while realistic
market-impact modeling for RL traders Abbade and Costa
(2026) supplies the cost layer that MR-4 asks papers to report;
auditability-oriented execution frameworks such as AutoQuant
Deng (2025) reinforce the same principle from the engineering
side by treating execution constraints as an auditable system
boundary. Second, a crypto-native execution niche: multi-agent
MEV generation and cross-chain arbitrage systems Wen et al.
(2026); Ye et al. (2026b) operate directly on order-flow and
settlement mechanics, a setting in which execution semantics
constitute the strategy rather than a downstream assumption.
Synthesis and Practical Considerations.The action execution
layer grounds cognitive decisions in market dynamics by
accounting for transaction costs, slippage, fill timing, and
microstructure constraints. In multi-agent or institutional
deployments, structured order logging supports audits that link
execution traces to strategic reasoning. With these architectural
foundations established, Part II turns to enabled capabilities,
beginning with automated alpha discovery.
7. Alpha Discovery Capability
The preceding sections established the architectural foundations
of agentic traders. This section addresses the question: “How
do agents discover trading signals?”
Here, alpha discovery refers to generating and testing candidate
trading signals; consistent with the evidence-map framing, we
count autonomous alpha search as supported only when the
reported system connects discovery to out-of-sample or closed-
loop evaluation, rather than merely proposing factors.
Functional Scope and Discovery Paradigms.Automated alpha
discovery represents one of the most prominent applications
of LLM agents in quantitative finance, transitioning formulaic
factor generation from manual trial-and-error to autonomous,
hypothesis-driven exploration. By combining financial reason-
ing with programmatic code generation, agents search through
vast functional hypothesis spaces to uncover predictive trading
signals. Across the literature, alpha discovery is realized through
three core paradigms:
• Code-Based Generation(Section 7.1): Expressing eco-
nomic hypotheses in executable code and refining them
through automated syntax and runtime feedback.
• Retrieval-Augmented Discovery(Section 7.2): Ground-
ing factor exploration in academic literature, financial
corpora, and historical factor libraries to seed domain-
consistent hypotheses.
• Evolutionary and Genetic Search(Section 7.3): Guiding
symbolic expression trees through LLM-directed muta-
tion, crossover, and fitness selection.
The central methodological considerations include managing
search budgets to prevent multiple-testing data snooping, en-
forcing factor diversity to mitigate crowding, and verifying that
statistical predictive power survives net of turnover and execu-
tion frictions.
Classical Baseline: Factor Models and Information Coeffi-
cient
Before LLM-based approaches, alpha generation relied on
manually engineered factor models (e.g., the Fama–French
three-factor model, momentum, value), in which factor validity
is measured by the information coefficient (IC), the correlation
between factor scores and subsequent returns, and statistical
rigor required controlling for multiple testing (White’s Reality
Check, Hansen’s SPA) to distinguish genuine signals from data
mining Fama and French (1993); Grinold and Kahn (2000).
LLM-based agents automate this discovery process but inherit
the same fundamental challenge: ensuring that discovered
patterns generalize out-of-sample rather than exploit historical
noise.
Comparability note.Comparable alpha-search evidence should
report MR-2 (time split+sealed test), MR-4 (execution & costs),
factor definitions, and MR-6 (artifacts & logs); see Section 13
for detailed protocol requirements and reporting checklists.
Author Framework
Alpha-to-Trade Contract. We introduce the Alpha-to-Trade
Contract as a conceptual framework for separating statistical
significance from tradable signals; the conversion contract
specifies three checks:
1. Frequency Compatibility: Does the signal update
frequency match the execution latency budget?
2. Turnover Constraints: Does the theoretical gain
survive realistic transaction costs and market impact?
3. Liquidity Reality: Is the factor universe liquid
enough for the assumed capital capacity?
Papers omitting this contract risk conflating theoretical
IC with realized alpha return, a common pitfall in agentic
trading literature López de Prado (2018).
Figure 9 illustrates these discovery paradigms.
7.1. Code-based Alpha Discovery
Code-based alpha generation draws on the code-synthesis capa-
bilities of LLMs to translate natural-language hypotheses about
market behavior into executable factor definitions. Because
it lowers the programming barrier, this paradigm lets domain
experts express and test their trading ideas directly.
18

Three Alpha Discovery Paradigms
Code-based
Approach:
Examples:
• LLM writes code
• Formula expressions
• Factor engineering
• Momentum factors
• Reversal signals
• Volume patterns
Retrieval-based
Approach:
Examples:
• Search literature
• Retrieve strategies
• Adapt to context
• Published factors
• Analyst insights
• Academic models
Evolutionary
Approach:
Examples:
• Generate variations
• Test performance
• Select candidates
• Genetic algorithms
• Ensemble methods
• Auto-ML
Figure 9:Three alpha discovery paradigms. Code-based discovery translates natural language hypotheses into executable code. Retrieval-based
discovery finds and adapts existing factors from a library. Evolutionary discovery searches the factor space through mutation and selection.
Representative Approaches. CogAlpha (Liu et al., 2025) ex-
tends code-based generation with structured prompting tem-
plates that guide the LLM toward syntactically correct and se-
mantically meaningful factor definitions. AlphaAgent (Tang
et al., 2025) further introduces regularization mechanisms (orig-
inality enforcement, hypothesis alignment, and complexity con-
trol) to counteract alpha decay. FactorMAD (Duan et al., 2025)
uses a multi-agent debate framework in which LLM agents
critique and refine factor proposals to enhance interpretability.
Automate Strategy Finding (Kou et al., 2025) implements a
three-stage pipeline with risk-aware multi-agent validation and
ensemble strategy selection, and reports 53.17% cumulative re-
turns on SSE50 under its backtest setup (Split: NR;Execution:
NR;Cost: NR;Universe: SSE50;Tier: BG); because protocol-
critical fields areNR/Unknown, we read such results as illustrative
rather than protocol-comparable evidence.
Beyond factor synthesis, recent work combines LLM reasoning
with reinforcement learning for structured trading decision-
making Xiao et al. (2025b), and ensemble strategies built on
deep reinforcement learning report strong performance on stock
trading tasks Yang et al. (2025).
Technical Mechanisms. The generation pipeline operates as an
adaptive search processsusceptible to overfitting: it (1) parses
the natural-language hypothesis to identify key components,
(2) maps them to code templates and APIs, (3) generates
executable code, (4) validates it through sandboxed execution,
and (5) backtests it on historical data; Figure 10 illustrates this
generation–validation loop. Crucially, the “validation chain”
feeds performance feedback into the next generation step, so
the loop risksadaptive overfitting: as the agent iterates to
maximize the validation Sharpe ratio, it effectively “mines”
the validation set Bailey et al. (2014); López de Prado (2018).
A rigorous protocol therefore requires reporting theSearch
Budget(the number of generated hypotheses) and ensuring
that final performance is measured on a sealedtest setthat is
never exposed to the agent during the refinement loop; without
this separation, reported “validation” metrics are statistically
inflated. Sandboxed execution, standard practice for mitigating
security risks, addresses a different concern and does not by
itself enforce split integrity. Whatever form the output takes—
synthesized factors include momentum and reversal signals—its
validity depends entirely on the integrity of the data split.
7.2. Retrieval-based Alpha Discovery
Retrieval-based alpha generation adapts existing factor knowl-
edge rather than generating factors from scratch: the agent re-
trieves related signals or financial context that can inform the
current situation.
Representative Approaches. RAG-based financial retrieval
systems (Cook et al., 2025) index domain knowledge as
embeddings and retrieve contextually similar items using
semantic search. PRISM (Ng et al., 2025) refines this retrieval
through prompt-optimized in-context modeling for financial
domains, and retrieval-augmented frameworks for financial
time-series forecasting (Xiao et al., 2025a) illustrate how LLM
generation can be combined with historical pattern retrieval.
Technical Mechanisms. Retrieval relies on vector embeddings
that encode factor semantics (formula structure) and market
context. The validity of this paradigm, however, hinges on
Factor Library Governance, a data-integrity requirement that
is easy to overlook.
• Survivorship Bias: If the library collects only “histori-
cally successful” factors, the retrieval process implicitly
conditions on future outcomes, inflating backtest perfor-
mance.
19

Generation
chain
Natural
language idea
Prompt /
Context
Factor
code
Refine
Validation
chain
 Feedback
 Metrics
 Backtest
Figure 10:Chain-of-Alpha workflow. The generation chain (top) translates natural language into factor code. The validation chain (bottom)
backtests the factor, computes performance metrics, and provides feedback for refinement. The two chains interact iteratively until a satisfactory
factor is produced.
• Look-ahead Leakage in Embeddings: If the embedding
model is trained on textual descriptions containing future
knowledge (e.g., “a successful high-volatility factor”), the
retrieval query qt effectively leaks information from t + k.
Protocol Implication
We recommendPoint-in-Time (PIT) Governancefor
verifiable evidence: the retrieval corpus Lt available at time
t must contain only documents and performance metadata
known attCook et al. (2025); Ng et al. (2025).
7.3. Evolutionary Alpha Discovery
Evolutionary alpha generation searches the factor space through
iterative mutation, crossover, and selection, treating factor
discovery as an optimization problem. This paradigm can
discover novel factor combinations that human experts might
not conceive.
Representative Approaches. Navigating Alpha Jungle (Shi
et al., 2025) employs Monte Carlo Tree Search (MCTS)
to efficiently explore the combinatorial space of possible
factors: each node in the search tree represents a partial factor
definition (e.g., a specific transformation applied to a price
series), and MCTS balances exploration (trying new factor
components) against exploitation (refining promising factors).
Alpha2 (Xu et al., 2024a) uses deep reinforcement learning,
in which an agent learns to construct factors by sequencing
primitive operations and receives rewards based on backtest
performance. EFS (Evolutionary Factor Searching) (Luo et al.,
2025) reformulates asset selection as a top-m ranking task
guided by LLM-generated factors, incorporating an evolutionary
feedback loop for iterative refinement.
Technical Mechanisms. Evolutionary methods define a search
space of primitive operations (price transformations, technical
indicators) and combination rules, which MCTS and Genetic
Programming (GP) navigate by balancing exploration (new
operations) against exploitation (refining promising factors). The
paradigm, however, faces a severeMultiple Testing Scalability
risk: as the search space grows exponentially, the probability of
finding a false positive approaches 1.0 unless rigorous statistical
corrections are applied White (2000). A valid protocol must
therefore report (1) aPrimitive Ops Audit(the exact set of
allowed functions), (2) theTotal Search Depth/Budget, and (3)
statistical tests for data snooping (e.g., White’s Reality Check
or Hansen’s SPA) Hansen (2005). At present, few agent papers
report these quantities, which makes their results difficult to
distinguish from noise; regularization techniques (complexity
penalties, ensemble methods) are useful heuristics but do not
substitute for formal multiple-hypothesis testing.
Open Question: Mathematical Bounds for Agent-Driven
Search.While classical multiple-testing corrections (White’s
Reality Check, Hansen’s SPA, and the Deflated Sharpe Ratio
Bailey et al. (2014)) remain the statistical gold standard, a
critical question emerges for LLM-based agents: can the agent’s
internal reflection/evolution loop provide novel mathematical
bounds on overfitting risk? Current evidence suggestsnot yet.
The reflection budget (Section 12.3) limits search iterations
but offers no statistical guarantee on the false discovery rate;
the sealed test set protocol prevents adaptive overfitting but
relies on experimental discipline rather than closed-form bounds;
and factor originality constraints (e.g., AST-based similarity
in AlphaAgent) shrink the effective search space without
quantifying the residual multiple-testing penalty.This represents
a significant research gap: future work could explore whether
LLM reasoning traces, factor genealogy logs, or Bayesian model
averaging over discovered factors can yield principled, agent-
native overfitting controls that complement or extend classical
methods. Until such methods exist, evolutionary alpha systems
should report both (1) search-budget and protocol constraints
and (2) classical multiple-testing statistics (e.g., deflated Sharpe
ratio Bailey et al. (2014)) to enable rigorous evaluation.
Table 14 organizes representative mechanisms and their design
20

Table 14:Representative alpha-discovery mechanisms and design considerations. The considerations identify review dimensions discussed in this
survey. Tags describe artifact availability (R0–R1) or background literature (BG); see Table B.24.
Paradigm Mechanism Search object Dimensions to examine Works Tags
Code-based LLM→Code Semantic fac-
tors
Structured prompting; hypothesis-to-code mapping CogAlpha Liu et al.
(2025)
R0
Code-based Multi-Agent
Debate
Interpretable
factors
Debate-based critique and refinement FactorMAD Duan
et al. (2025)
BG
Retrieval Vector Search Factor library Point-in-time (PIT) library governance RAG-Fintech Cook
et al. (2025)
R0
Retrieval Prompt-
Refined RAG
Financial cor-
pus
Point-in-time (PIT) corpus governance PRISM Ng et al.
(2025)
BG
Evolutionary MCTS/Deep
RL
Combinatorial
operations
Allowed operations; search budget; multiple testing Alpha Jungle (R0),
Alpha2 (R1) Shi et al.
(2025); Xu et al.
(2024a)
R0–R1
Evolutionary LLM-Guided
Evolution
Sparse portfo-
lios
Search budget and sealed-test separation EFS Luo et al. (2025) BG
considerations.
Extension-window additions (2026-03-10 to 2026-09-30).
Additional studies automate factor or strategy discovery through
agentic generation–backtest loops (Weng et al., 2026; Yuan et al.,
2026b; Yu et al., 2026a; Li et al., 2026e; Liu et al., 2026; Yi et al.,
2026; Zhao and Sha, 2026; Wang et al., 2026d; Li et al., 2026d;
Zhao et al., 2026; Kim et al., 2026a; Ye et al., 2026a; Li et al.,
2026g; Kvasiuk et al., 2026; Sharma and Shroff, 2026; Kim
et al., 2026b), with further variants pushing toward trajectory-
level self-iteration (Zhu et al., 2026a), constrained hypothesis-to-
factor pipelines in cryptocurrency markets (Huang et al., 2026c),
self-evolving coding agents for quantitative research (Li et al.,
2026h), and stratified strategy-alignment objectives (Huang and
Yu, 2026).
The reported evaluation settings span held-out or out-of-sample
windows, per-trade or turnover-based costs, and named index
universes such as CSI 300/500 or S&P 500. Interpreting results
across these settings requires attention to the split, cost, and
universe conventions used by each study.
A parallel mini-cluster interrogates the evaluation layer itself:
closed-loop benchmarks and referee protocols for mining agents
(Qu and Chen, 2026; Qu et al., 2026; Wang et al., 2026c; Deng
et al., 2026; Cao et al., 2026; Zhang et al., 2026a), together with
leakage and validity analyses (Ye et al., 2026c; Zhang and Stadie,
2026; Yao et al., 2026), now make evaluation design an explicit
research object rather than an implementation detail. Two further
studies deserve note: a direct assessment of LLMs on technical
market-analysis tasks (Ntale, 2026), and evidence that nominally
valid LLM signals can fail across regime boundaries (Yang,
2026)—a useful reminder that alpha-mining output is regime-
conditional even when protocol fields are reported.
Synthesis and Empirical Considerations.Code-based genera-
tion, retrieval-augmented discovery, and evolutionary search
explore different parts of the factor hypothesis space. Their em-
pirical value depends on out-of-sample survival: recursive search
can overfit noisy backtests, so walk-forward testing, factor-
correlation checks, and turnover-adjusted transaction costs re-
main essential. The next section examines how discovered sig-
nals are aggregated into portfolios in Section 8.
8. Portfolio Management Capability
The preceding section examined how agents generate alpha
signals. This section addresses the question: “How do agents
manage multi-asset portfolios?”
The evidence is strongest where papers specify the action
object—weights, orders, constraints, or rebalancing rules—
and thinnest where portfolio management appears only as a
conceptual layer.
Functional Scope and Allocation Paradigms.Portfolio man-
agement represents the functional layer where individual asset
signals are synthesized into constrained, multi-asset capital al-
locations. While single-asset trading models emit directional
buy/sell signals in isolation, portfolio-level agents must account
for cross-asset covariance, leverage limits, sector exposure bud-
gets, and rebalancing turnover. Across the surveyed literature,
portfolio agents operate through three primary approaches:
• Strategic Asset Allocation(Section 8.1): Synthesizing
macro market regimes and factor signals into baseline
target asset distributions.
• Tactical Position Sizing(Section 8.2): Dynamically
modulating individual asset exposures based on volatility,
conviction, and liquidity.
• Dynamic Rebalancing(Section 8.3): Managing execu-
tion turnover and rebalancing intervals under transaction-
cost and market-friction constraints.
Key empirical considerations include the specification of re-
balancing calendars, explicit universe filtering (accounting for
21

delistings and liquidity), and turnover-induced transaction cost
modeling.
Classical Baseline: Mean-Variance Optimization and Kelly
Criterion
Classical portfolio theory casts allocation as mean-variance
optimization (Markowitz 1952), which maximizes risk-adjusted
returns given covariance estimates, or as growth-optimal
betting (Kelly 1956), which maximizes the log-utility of wealth.
The Black-Litterman model incorporates investor views into
equilibrium returns. These frameworks yield closed-form
solutions under Gaussian assumptions but struggle with non-
stationary higher-order moments and tail risks—precisely
where LLM-based approaches may add value through adaptive
reasoning and regime-aware dynamic allocation.
Comparability note.Protocol-comparable portfolio claims typ-
ically report MR-1 (data/universe), MR-2 (time split), MR-3
(I/O contracts+constraints), and MR-4 (execution & costs); see
Section 13.
8.1. Asset Allocation
Asset allocation sets portfolio weights across asset classes and
broad themes (sectors, regions, styles), shaping the long-horizon
risk/return envelope.
Representative Approaches. Classical baselines include
mean-variance optimization Markowitz (1952) [BG] and Black-
Litterman Black and Litterman (1992) [BG]; both hinge on
estimates (returns, covariances, or implied priors) that can
drift quickly. Risk-based allocations (risk parity/HRP-style
clustering) are often preferred when estimates are noisy. In
agentic systems, LLMs commonly act asview generatorsLee
et al. (2025); Kirtac and Germano (2025) conditioned on news
and macro releases. Lee et al. (2025) show how LLM-generated
views can be fed into the Black-Litterman framework, while
Kirtac and Germano (2025) use LLM-based sentiment analysis
to drive portfolio optimization decisions.
A parallel line of work pursues end-to-end neural allocation
at scale: end-to-end networks have been proposed for vari-
ance minimization in large portfolios Bongiorno et al. (2025),
and deep architectures combining 3D-CNNs with BiLSTMs
target medium-term covariance forecasting Reis et al. (2025).
Graph attention-based heterogeneous multi-agent reinforcement
learning Zhang (2026a) offers adaptive portfolio optimization
through multi-agent coordination, and pair-trading work that
couples graph attention networks for pair selection with deep
reinforcement learning for execution provides a non-LLM back-
ground example of relation-aware portfolio construction Xia
et al. (2025) [BG]. HARLF Coriat and Benhamou (2025) in-
tegrates hierarchical reinforcement learning with lightweight
LLM-driven sentiment analysis for financial portfolio optimiza-
tion. These neural approaches complement mean-variance op-
timization by capturing non-linear dependencies that classical
methods may miss Zouaoui and Naas (2025); Uysal et al. (2024).
These pipelines, however, introduce severe leakage risks wher-
ever they ingest text and macro data. The time-series evalua-
tion literature therefore requiresPoint-in-Time (PIT) Textual
Alignment: macro inputs must use the unrevised values avail-
able at the exact release timestamp, and validation pipelines
must prevent future information from leaking through prepro-
cessing or feature construction Liu et al. (2022a); Albelali and
Ahmed (2025) [BG]. For the same reason,regime taggingis
best generated online from t−k lookback windows, since full-
sample regime clustering can leak future volatility states Hamil-
ton (1989); Bai and Perron (2003) [BG].
Technical Mechanisms. HRP-style allocation reduces sensitiv-
ity to covariance noise by allocating at the cluster level before
distributing within clusters. Regime-aware allocation (statistical
or LLM-driven) can switch risk budgets when volatility/liquid-
ity conditions change, but it is best treated as a hypothesis to
test rather than a guarantee. For agentic trading, the practi-
cal core is constraint-aware optimization (exposure, leverage,
turnover) with explicit transaction-cost assumptions López de
Prado (2016); Ledoit and Wolf (2004); Jagannathan and Ma
(2003) [BG].
8.2. Position Sizing
Position sizing determines how much capital to allocate to each
trading signal, balancing the upside of strong signals against the
risk of outsized losses. This tactical decision directly shapes
portfolio volatility and drawdown.
Representative Approaches. The Kelly criterion Kelly (1956)
[BG] links size to estimated edge and uncertainty, but is
fragile to estimation error; most implementations therefore use
fractional Kelly. Recent work revisits portfolio optimization
from complementary angles Boyd et al. (2024); Salo et al.
(2024) [BG], highlighting the growing importance of constraint-
aware sizing in modern markets. Alternatives include risk-
budget schemes (risk parity-style) and decision-informed neural
methods Hwang et al. (2025) that integrate learned forecasts and
LLM inputs into portfolio decisions.
Beyond these rules, recent formulations widen the sizing
design space. ODE-based dynamic optimization Alkhudaydi
(2025) offers continuous-time solutions to the mean-variance
problem, while cardinality- and bound-constrained formulations
Li et al. (2024b); Caner and Fan (2024) address practical trading
constraints that theoretical models often ignore. On top of these
formulations, agentic systems may inject qualitative risk flags
extracted from text; such inputs, however, require strict time
alignment and auditability.
Technical Mechanisms. In practice, sizing layers use conserva-
tive shrunk estimates and fractional Kelly-style scaling to keep
worst-case losses bounded.
Protocol Implication
For comparability, we recommend reporting aPosition
Sizing Checklist: (1)Risk Metric: What is minimized?
(V ol, CVaR, MaxDD), (2)Constraints: What are the
boundaries? (Long-only, Leverage< 1.5, Sector< 20%),
22

and (3)Scaling Logic: How is conviction mapped to size?
(Fractional Kelly, V olatility Targeting).
When LLMs contribute qualitative risk signals, they can be
treated as features with strict timestamping and ablation tests
(text signal on/off) to verify incremental value Kelly (1956);
MacLean et al. (2011); Rockafellar and Uryasev (2000) [BG].
8.3. Rebalancing
Rebalancing adjusts portfolio weights to maintain target allo-
cations as market prices move and new signals arrive. This
operational decision trades the benefit of preserving the intended
risk profile against the cost of frequent trading.
Across the mapped literature, agentic portfolio construction and
allocation already appear in several applied settings. Agentic AI
systems have been applied to dynamic crypto-asset allocation,
where adaptability matters most under high volatility Castelli
et al. (2025); as background examples, generative-AI pipelines
construct sector portfolios from LLM selections combined with
classical optimization V oronina et al. (2025) [BG], and Poly-
Model theory coupled with iTransformer architectures targets
hedge-fund portfolio construction Zhao et al. (2024) [BG]. On
the transparency side, explainable DRL techniques aim to make
financial policy decisions interpretable de la Rica Escudero
et al. (2025) [BG]. Strategy-guided exploration mechanisms can
broaden agent robustness for portfolio workflows, though they
are best read here as a generic robustness idea rather than direct
evidence for rebalancing Szot et al. (2026) [BG].
Representative Approaches. Canonical policies include
threshold rebalancing (act only when weights drift beyond
bands), time-based schedules, and cost-aware optimization that
trades offtracking error vs. transaction/impact/tax costs.
Learning-based methods then refine how these policies are
decided. Heuristic-guided reward learning has been proposed
for portfolio optimization, showing how learned heuristics can
improve rebalancing decisions Zhang et al. (2025), and multi-
objective gradient descent enables simultaneous optimization of
competing portfolio objectives during rebalancing Oliva et al.
(2025).
Agentic workflows often addevent awarenesson top of these
schedules (e.g., going risk-offbefore FOMC), which creates a
second leakage surface. Comparisons are most credible when
evaluations distinguish betweenCalendar Events(scheduled
ahead of time, e.g., Earnings Calendar) andShock Events
(unexpected news): rebalancing driven by shocks should rely on
real-time proxies (e.g., VIX spike, spread widening) observable
at t, rather than future-annotated event labels Li et al. (2023);
Unnikrishnan (2024). FinVision Fatemi and Hu (2024) [BG] is
better read as a multimodal stock-prediction example than as
direct evidence for this taxonomy.
News-driven rebalancing has emerged as a particularly active
application: one line of work combines financial news analysis
with reinforcement learning for portfolio management, enabling
dynamic rebalancing in response to real-time sentiment shifts
Unnikrishnan (2024). Liquidity-aware selection and rebalancing
strategies Abensur (2024); Nguyen (2025) further incorporate
machine learning-based liquidity classification to guide alloca-
tion and execution timing.
Technical Mechanisms. No-trade regions (bands) reduce churn
by ignoring small drift until it matters for risk, while execu-
tion models (VW AP/TW AP/implementation shortfall (IS); Sec-
tion 6.2) and explicit slippage assumptions determine whether a
policy survives outside a backtest. For agentic trading, the key
protocol caveat is separatingdecision timing(signal/optimizer)
fromfill timing(execution) to avoid overstating performance.
Where tax-aware logic is included, the evaluation should match
the account type and jurisdiction that the tax model assumes
Constantinides (1986); Davis and Norman (1990); Almgren and
Chriss (2001); Perold (1988) [BG].
Extension-window additions.Building on agentic crypto-
asset allocation Castelli et al. (2025), additional studies include
screening pipelines that feed portfolio construction Caner et al.
(2026), LLM-driven small-capitalization trading with integrated
allocation Kargarzadeh et al. (2026), recursively self-optimizing
multi-agent portfolio systems Yang et al. (2026), and a market-
regime council that performs dynamic credit assignment across
specialized agents Pei et al. (2026). These systems make the
portfolio layer an explicit, inspectable component, though their
evaluation conventions (rebalancing frequency, constraints, cost
models) remain heterogeneous.
Synthesis and Practical Considerations.Portfolio management
translates alpha into diversified holdings under allocation, sizing,
and rebalancing constraints. LLM-generated views can be
paired with classical optimization to connect qualitative context
with quantitative risk bounds; credible evaluation depends on
reporting the asset universe, rebalancing schedule, and turnover
costs. Section 9 examines controls across the trading lifecycle.
9. Risk Management Capability
The preceding sections examined alpha generation and portfolio
management. This section addresses the question: “How do
agents control financial risks?”
We treat risk management here as the set of constraints, monitors,
and post-trade controls that shape allowable actions. The
discussion stays tied to the evidence base because many risk
mechanisms are specified at the architecture level but rarely
isolated in empirical evaluation.
Systemic Role and Risk Governance Architecture.Risk manage-
ment forms the essential protective foundation of an autonomous
trading system, ensuring capital preservation, regulatory com-
pliance, and resilience against market shocks. Because LLMs
can exhibit hallucination, overconfidence, or vulnerability to
adversarial input, real-world deployment requires independent,
deterministically governed risk guardrails. Across the trading
lifecycle, risk architecture is structured across three defensive
stages:
23

Table 15:Portfolio management method comparison: traditional methods, candidate LLM enhancements, and key challenges at each decision level.
Level Traditional Methods LLM Enhancement Key Challenges
Asset Allocation Mean-variance optimization,
Black-Litterman, Risk parity,
Hierarchical clustering
Regime detection from narra-
tives, View generation, Market
sentiment analysis
Covariance estima-
tion errors, Regime
misclassification
Position Sizing Kelly criterion, Risk parity
equalization, Convex opti-
mization (VaR/CVaR)
Qualitative risk assessment from
news, Constraint handling with
reasoning
Estimation error
sensitivity, Over-
aggressive sizing
Rebalancing Threshold-based, Time-
based, Cost-aware optimiza-
tion
Strategic timing around events,
Transaction cost estimation, Tax-
aware harvesting
Transaction costs,
Market impact, Tax
optimization com-
plexity
• Pre-Trade Risk Controls(Section 9.1): Hard gatekeep-
ing filters verifying instrument whitelists, maximum order
sizes, leverage ceilings, and liquidity availability prior to
order submission.
• In-Trade Monitoring and Dynamic Exposure(Sec-
tion 9.2): Real-time surveillance tracking aggregate port-
folio value-at-risk (VaR), sector concentration limits, trail-
ing stop-losses, and emergency circuit breakers.
• Post-Trade Attribution and Compliance(Section 9.3):
Systematic trade reconciliation, slippage analysis, perfor-
mance attribution, and regulatory audit logging.
From an engineering standpoint, the key challenge lies in
establishing non-bypassable, deterministic overrides that can
intercept errant LLM actions before market transmission without
introducing unacceptable execution delays. These safety
mechanisms apply across the pre-trade, in-trade, and post-trade
stages. The stages are detailed in Section 9.1, Section 9.2, and
Section 9.3; cross-stage guardrails are discussed in Section 9.4.
Classical Baseline: VaR, CVaR, and Drawdown Control
Traditional risk management quantifies tail risk through Value-
at-Risk (VaR)—the quantile of the loss distribution—and
Conditional VaR (CVaR), the expected loss beyond VaR.
Drawdown control limits peak-to-trough declines via dynamic
programming or convex optimization. These metrics provide
computationally tractable risk bounds but assume stationary
distributions and known correlation structures. LLM agents can
instead produce natural-language explanations of risk exposures
and generate scenarios; to reach an auditability standard
comparable to classical frameworks, however, those explanations
must be grounded in verifiable metrics and immutable logs
Khatchadourian (2026) [BG].
Figure 11 illustrates the lifecycle overview.
Comparability note.Protocol-comparable risk claims typically
report MR-3 (risk action semantics+priorities), MR-4 (execu-
tion/cost assumptions that risk controls depend on), and MR-6
(artifacts & logs); see Section 13.
9.1. Pre-trade Risk Control
Pre-trade risk control prevents excessive risk by checking orders
against risk limits before they are submitted to the market. This
preventive stage is the first line of defense against catastrophic
losses.
Representative Approaches. Value-at-Risk (VaR) limits cap
the maximum potential loss at a specified confidence level (e.g.,
99% one-day VaR of $1M). Conditional VaR (CVaR) extends
this by estimating the expected loss in the tail beyond the
VaR threshold Rockafellar and Uryasev (2000) [BG]. Exposure
constraints limit concentrations to single assets, sectors, or
counterparties (e.g., no more than 10% of portfolio in any
single stock), and compliance checks ensure that trades respect
regulatory requirements and internal policies. On the agentic
side, some prototypes use LLMs to translate human-readable
policies into executable constraints Cosler et al. (2023) [BG],
while others employ structured, model-based risk representations
to estimate market risk transparently. This translation step,
however, injects non-determinism into a layer that is expected
to behave deterministically—a tension the protocol implication
below addresses directly.
Protocol Implication
For protocol comparability, we recommend reporting: (1)
VaR Config(Confidence Level, Holding Period, Window),
(2)Scenario Source(Standard vs Custom), and (3)LLM
Verification: policy-to-code translations are best validated
against deterministic test sets rather than raw LLM chat
outputs for compliance.
Technical Mechanisms. Portfolio risk models estimate the
risk contribution of each potential trade, considering both
the standalone risk of the position and its correlation with
existing holdings. LetΣdenote the covariance matrix of asset
returns with entries σi j, and let w denote portfolio weights.
The portfolio variance is V = w⊤Σw, and themarginal
contribution to varianceis ∂V ∂wi =2(Σ w)i. A commonly used risk contributiondecomposition is RCi = wi(Σw)i, while the
marginal contribution to volatilityis ∂σp ∂wi =(Σ w)i/σp withσp =
24

Risk Control Across the Trading Lifecycle
Pre-trade
Controls:
Timing:
• Set limits
• Check orders
• Validate constraints
• Before submission
Real-time
Controls:
Timing:
• Monitor positions
• Watch markets
• Intervene on breaches
• During trading
Post-trade
Controls:
Timing:
• Analyze outcomes
• Review losses
• Improve controls
• After execution
Figure 11:Risk control timeline across the trading lifecycle. Pre-trade risk control sets limits and checks before orders are submitted. Real-time
risk control monitors positions and markets during trading, intervening when thresholds are breached. Post-trade risk analysis analyzes outcomes to
improve future risk management.
√
w⊤Σw Roncalli (2013) [BG]. Scenario analysis simulates
portfolio performance under stress scenarios (market crash: -
30% equities, interest rate spike:+200bps, volatility surge:
σ× 3) to identify hidden risks that might not manifest under
normal conditions Basel Committee on Banking Supervision
(2009). Rule engines encode regulatory and internal policies as
executable rules (e.g., Reg T margin requirements, Reg NMS
order protection rules); here LLMs can parse natural-language
policies into such rules automatically, which is precisely where
the non-determinism caveat above applies.
Adjacent work supports this layer at two different levels.
Agent-based market models generate realistic transaction costs
and slippage for liquidity risk assessment Vytelingum et al.
(2025) [BG], while the STRIDE framework offers guidance on
when a risk-sensitive application calls for agentic AI, an AI
assistant, or a direct LLM call Asthana et al. (2025) [BG].
9.2. Real-time Risk Control
Real-time risk control monitors positions and market conditions
during trading, intervening when risk thresholds are breached or
anomalous conditions emerge. This reactive stage catches risks
that pre-trade models miss due to changing market conditions or
model error.
Representative Approaches. Position monitoring tracks
portfolio metrics (greeks for options, duration for bonds, beta
for equities) in real time, alerting when they exceed thresholds.
Drawdown stops halt trading when portfolio losses reach
specified levels (e.g., stop trading if down 5% from peak),
and volatility scaling reduces position sizes as market volatility
increases, maintaining constant risk exposure. Text streams can
extend this monitoring with early warnings Tetlock (2007) [BG];
slower-moving macro uncertainty indices complement them
Baker et al. (2016) [BG], though these indices are not real-
time signals. Because real-time control is also a first-order
design concern for cross-market robustness, the division of labor
matters: LLMs are generally unsuitable for the sub-millisecond
Critical Path, so a robust architecture separates aGating
Layer(deterministic algorithms such as circuit breakers for sub-
millisecond stops) from an asynchronousExplanation Layer
(LLMs for cause attribution). Evaluations should then disclose
Latency BudgetsandFalse Positive Ratesfor all triggers.
Technical Mechanisms. Stream processing systems update
risk metrics from tick data, trades, and order-book changes.
Anomaly detection can flag price spikes, volume surges, and
order-book imbalance as stress signals Easley et al. (2012);
Kirilenko et al. (2017) [BG]. Circuit breakers halt trading when
drawdown or single-position loss limits are breached. Manual
review before restart helps prevent stress-driven decisions Lo
and Repin (2002); Kahneman and Tversky (1979) [BG].
Protocol Implication
We suggest reporting any dynamic exposure rule in display
form rather than embedding it in prose. A simple example is
wi(t)=min

wmax i , risk_budget risk_per_uniti
!
which caps concentration as prices and volatility change.
9.3. Post-trade Risk Analysis
Post-trade risk analysis learns from trading outcomes to improve
future risk management. This retrospective stage identifies
what risks were missed, how effective controls were, and where
improvements are needed.
Representative Approaches. Performance attribution decom-
poses returns into component sources (alpha return, beta, timing,
25

stock selection), identifying which risks contributed to gains or
losses; LLM-assisted attribution can narrate how market fac-
tors propagated through the portfolio structure. Stress testing
simulates portfolio performance under historical crisis scenarios
(2008 financial crisis and other major stress episodes) to as-
sess resilience Basel Committee on Banking Supervision (2009).
Regime analysis examines how portfolio performance varied
across market regimes (bull, bear, high volatility), identifying
conditions where risk management failed. LLM-enhanced sys-
tems can summarize these risk outcomes, but guarding against
post-hoc rationalization requires every narrative claim to be
grounded in immutable logs and replayable evidence Tan et al.
(2025a); Khatchadourian (2026) [BG]. For the same reason,
Counterfactual Reasoning(e.g., "what if" scenarios) is best
labeledHypothetical Inference—an assumption-dependent con-
struction, not an empirical fact.
Technical Mechanisms. Causal analysis identifies the root
causes of risk events, distinguishing between market risk
(systemic factors affecting all assets), idiosyncratic risk (asset-
specific events), and model error (incorrect assumptions or
predictions). Techniques include Granger causality tests,
Shapley value decomposition for attribution, and structural break
detection to identify when risk models failed. Counterfactual
reasoning estimates what would have happened under different
risk management decisions (as an illustrative example, “if
we had reduced position size by 50%, drawdown would
have been 3% instead of 8%”), enabling learning from near-
misses. Report generation produces human-readable risk
summaries for compliance and management review, with LLMs
translating quantitative metrics (“VaR exceeded by 20% on
March 15th”) into narrative explanations (“Risk was elevated due
to concentrated tech exposure during the AI sector correction;
position limits were triggered but too late to prevent significant
losses”), making risk analysis interpretable for non-technical
stakeholders Granger (1969); Shapley (1953); Bai and Perron
(2003); Pearl (2009) [BG].
Table 16 summarizes risk management approaches across the
three stages. Effective risk management depends on all three
stages working in concert: pre-trade controls prevent excessive
risk, real-time controls catch emerging risks, and post-trade
analysis enables continuous improvement.
9.4. Safety and Constraint Mechanisms
Deployable trading agents require safety layers that sit outside
the model’s generative reasoning loop. These include pre-
trade exposure checks, hard position limits, concentration caps,
drawdown triggers, and kill-switch logic that can halt order
flow when market conditions or model behavior leave the
approved operating envelope. In the current literature, such
mechanisms are often mentioned in passing but rarely specified
at reproducible detail. We therefore treat safety architecture
as part of the risk-management interface, not as an optional
deployment afterthought.
Extension-window additions.The extension cohort begins
to fill this gap: parameterized stop-loss/take-profit layers for
autonomous strategies Li et al. (2026c) make exit-rule design an
explicit, tunable risk interface, and dynamic objective selection
under safeguard constraints with LLM oversight Sakurai et al.
(2026) treats risk bounds as first-class control inputs. A
complementary background analysis systematizes how trading
agents fail under adversarial and regime-shifted conditions Wang
and Saxena (2026) [BG]; it is not primary evidence for this gap.
Synthesis and Governance Considerations.Risk governance
spans pre-trade limits, in-trade monitoring, and post-trade analy-
sis, with deterministic safety mechanisms constraining actions
across all three stages. FinRS Liu and Dang (2025b) incorpo-
rates risk sensitivity into the trading objective; dedicated limits,
gating, and monitoring provide complementary safeguards at
the execution and governance layers. Part III turns to adaptation
and evolution, beginning with adaptive learning paradigms in
Section 10.
10. Learning Paradigms
The preceding parts of this survey established the architectural
foundations of agentic traders and the capabilities these archi-
tectures enable. This section addresses the question: “How do
agents learn from market feedback?”
Learning enables agents to adapt their behavior based on
experience and changing market conditions. This section covers
learning mechanisms; governance of persistent state and update
cycles is treated in Section 12.
Adaptive Mechanisms and Learning Spectrum.Financial mar-
kets are intrinsically non-stationary: statistical patterns decay,
volatility regimes shift abruptly, and trading signals erode as
market participants adapt. Consequently, static trading agents
face rapid performance degradation unless equipped with mech-
anisms for continuous adaptation. Across the surveyed literature,
agent learning spans three foundational paradigms along the
spectrum of parameter persistence and adaptation speed:
• In-Context Learning (ICL)(Section 10.2): Adaptation
through prompts that conditions future decisions on re-
trieved market exemplars and reflective feedback without
modifying model weights.
• Supervised Fine-Tuning (SFT)(Section 10.3): Domain
adaptation through weight updates that trains base LLMs
on specialized financial instructions, historical trade
rationales, and domain corpora.
• Reinforcement Learning (RL)(Section 10.4): Policy
optimization that trains agents to maximize risk-adjusted
sequential rewards (e.g., cumulative return, Sharpe ratio)
within interactive trading environments.
The primary methodological trade-offs involve balancing sample
efficiency and adaptation agility against catastrophic forgetting
and distribution-shift vulnerability.
26

Table 16:Risk management method comparison: mechanisms and candidate LLM enhancements across the three lifecycle stages.
Stage Mechanisms LLM Enhancement
Pre-trade VaR/CVaR limits; exposure constraints; compliance checks Rule interpretation; policy translation; natural-language
constraints
Real-time Position monitoring; drawdown stops; volatility scaling Anomaly detection; news monitoring; early-warning signals
Post-trade Attribution; stress testing; regime analysis Narrative explanation; report generation; learning insights
10.1. Reward and Feedback Design
Reward specification is a first-order design choice rather than an
implementation detail. Trading environments impose delayed,
noisy, and partially confounded feedback: realized P&L arrives
after execution, inventory risk accumulates across steps, and
reward proxies can be gamed through simulator artifacts. We
therefore distinguish immediate execution feedback (fill quality,
slippage, rejected orders) from delayed portfolio feedback (P&L,
drawdown, turnover, and risk-adjusted return). Papers claiming
adaptive improvement should report which of these signals are
optimized, over what horizon, and with what safeguards against
reward hacking.
Figure 12 provides a conceptual comparison of the three
paradigms.
10.2. In-context Learning
In-context learning (ICL) enables agents to adapt from examples
provided in the prompt without updating model parameters,
following the GPT-3-style few-shot paradigm Brown et al.
(2020) [BG]. This rapid adaptation mechanism is particularly
valuable in dynamic markets where conditions change faster
than models can be retrained.
Representative Approaches. FinAgent Zhang et al. (2024) uses
ICL by retrieving relevant trading episodes from memory and
inserting them as examples in the prompt, enabling the LLM
to adapt its reasoning to similar situations without parameter
updates.
Technical Mechanisms. ICL selects and orders examples for
the prompt, using retrieval and context-management choices
described in Section 4 Brown et al. (2020) [BG], Zhang et al.
(2024). RAG also adds current financial documents from
external stores. Because neither updates model parameters, any
adaptation is temporary and bounded by the context window.
10.3. Supervised Fine-tuning
Supervised fine-tuning (SFT) updates model parameters on
labeled demonstrations of desired behavior, teaching agents
to imitate expert trading decisions. This approach transfers
knowledge from expert traders or historical successful strategies
into the agent.
Representative Approaches. The examples below distinguish
finance-domain tuning methods from end-to-end trading systems.
The extension cohort begins to move this boundary: post-
training of local quantitative research agents Wang et al. (2026d)
and cognitive fine-tuning for stable financial reasoning Pan and
Liew (2026) bring weight updates closer to the trading loop,
though fully end-to-end SFT evidence for trading agents remains
thin. The FinGPT instruction-tuning benchmark Wang et al.
(2023a) [BG] illustrates finance-domain instruction tuning on
financial NLP tasks. Two supervised variants matter most for
trading agents:behavior cloning, which maps market states
to expert actions so that trader demonstrations become usable
policy targets Ross et al. (2011) [BG]; andmulti-task adaptation,
which trains on sentiment, portfolio, and risk tasks jointly
and produces representations that may transfer across finance
subtasks Caruana (1997) [BG].
Technical Mechanisms. SFT relies on instruction and demon-
stration datasets with prompt-response pairs (market context→
expert decision or analysis). Training minimizes a supervised
loss (e.g., cross-entropy for discrete actions, regression for siz-
ing/allocation), with standard regularization and careful held-out
evaluation to check robustness to unseen regimes. Parameter-
efficient methods (e.g., LoRA-style methods) reduce cost while
preserving much of the base model; finance-oriented bench-
marking work has explored these trade-offs Wang et al. (2025a).
General parameter-efficient variants are background mechanisms
Dettmers et al. (2023); Xu et al. (2024b) [BG]. SFT can produce
persistent behavioral changes but is sensitive to label quality and
distribution shift.
10.4. Reinforcement Learning
Reinforcement learning (RL) is used in trading agents when
the objective is inherently sequential (portfolio rebalancing,
execution, or iterative factor construction), the feedback is
delayed, and the policy needs to trade offreturn, risk, and costs
under constraints.
Representative Approaches. FinRL-DeepSeek Benhenda
(2025) combines LLM-based priors with policy optimization,
reporting risk-adjusted return improvements over baselines
in simulated environments 1. MacroHFT Zong et al. (2024)
introduces memory-augmented context-aware RL for high-
frequency trading, while EarnHFT Qin et al. (2024) explores
hierarchical RL for HFT; both are conventional deep-RL trading
systems rather than LLM agents and are retained as non-agentic
baselines. Deep RL for alpha discovery Xu et al. (2024a) frames
factor construction as a program-generation task, optimizing an
1Specific performance metrics vary by configuration (e.g., CPPO-
DeepSharpe vs. CPPO-DeepV ol) and market regime; readers should consult the
original paper for detailed protocol assumptions, cost models, and train/test split
discipline.
27

Three Learning Paradigms Comparison
ICL
Approach:
Trade-offs:
Use Cases:
• Prompt engineering
• Few-shot examples
• No weight updates
• Fast adaptation
• No training
• Limited context
• Quick strategy testing
SFT
Approach:
Trade-offs:
Use Cases:
• Labeled examples
• Task-specific data
• Weight fine-tuning
• Domain-aligned
• Specialized
• Needs data
• Domain adaptation
RL
Approach:
Trade-offs:
Use Cases:
• Reward signals
• Trial and error
• Policy optimization
• Policy-aligned
• Adaptive
• Sample inefficient
• Performance tuning
Figure 12:Conceptual comparison of three learning paradigms. The panels summarize what each loop updates, the main trade-offs emphasized in
the design literature, and illustrative use cases.
evaluation metric over the search space while balancing alpha
performance and diversity.
Adjacent work marks the boundary between learning rules and
persistent cross-time change: modular memory architectures
retain experience across tasks Dorovatas et al. (2026) [BG],
explicit state dynamics improve temporal coherence Subaharan
(2026) [BG], and code-based alpha evolution refines strategies
from execution traces and natural-language feedback Liu et al.
(2025) [BG]. The latter update-governance questions are taken
up in Section 12.
What should be reported (and why it matters). Because
RL results are highly sensitive to experimental setup, trading
papers should explicitly specify (i) chronological data splits
(train/validation/test or walk-forward) and how hyperparameters
are chosen to avoid leakage; (ii) the cost model (commissions,
spread/slippage, and market impact assumptions); and (iii)
simulator fidelity (fill/latency assumptions, action/state/reward
definitions, constraints, and whether the simulator matches the
instrument/microstructure being claimed). Key risks include
simulator overfitting and reward hacking: policies can exploit
artifacts of the backtester/cost model and fail catastrophically
out-of-sample, especially under non-stationarity and regime
shifts.
Synthesis and Algorithmic Considerations.In-context learning
conditions decisions on prompt examples and retrieved experi-
ence; supervised fine-tuning updates parameters from demon-
strations; reinforcement learning optimizes sequential policies
through reward feedback. FinAgent illustrates prompt-context
adaptation Zhang et al. (2024), while FinRL-DeepSeek and
Alpha2 use RL Benhenda (2025); Xu et al. (2024a). These ap-
proaches differ in persistence and feedback, and their evaluation
depends on example and label coverage, temporal splits, sim-
ulator fidelity, and reward design. Section 11 next examines
collective coordination.
11. Multi-Agent Coordination
Note: Multi-agent coordination is a cross-cutting organizational
dimension: role structure is architectural, while coordination
dynamics can shape capabilities and adaptation. This section
focuses on those interactions and appears in Part III because its
emphasis is on emergent coordination.
The preceding sections examined the architecture and capabil-
ities of agentic traders. This section addresses the question:
“How do multiple agents collaborate in markets?”
Multi-agent systems enable specialization and decomposition,
with different agents focusing on different aspects of the trading
problem (analysis, execution, risk management). What remains
unsettled is whether coordination itself delivers superior trading
performance once computational budget, information access,
and protocol design are held constant.
Coordination Patterns and Market Ecology.Financial decision-
making in institutional environments is inherently collaborative,
distributed across macroeconomic analysts, sector specialists,
quantitative modelers, risk officers, and execution traders.
Multi-agent trading frameworks mirror this division of labor
by deploying specialized agents that interact, deliberate, and
coordinate. In the literature, multi-agent organizations are
structured along three principal paradigms:
• Role-Based Collaboration(Section 11.1): Flat or peer-
to-peer agent topologies where specialized personas
(e.g., fundamental bull/bear debaters, sentiment analysts)
exchange structured messages to reach trading consensus.
• Hierarchical Networks(Section 11.2): Multi-tiered com-
mand structures where supervisory portfolio manager
28

Table 17:Conceptual design trade-offs of learning paradigms. These descriptions characterize adaptation mechanisms; training cost and data
requirements depend on the task and implementation.
Paradigm Adaptation mecha-
nism
Data source Typical strengths Design considerations
ICL Context updates Prompts and exam-
ples
Immediate task conditioning Context capacity; no persis-
tent weight update
SFT Supervised weight
updates
Labeled demonstra-
tions
Persistent domain specialization Label coverage; retraining;
overfitting
RL Reward-driven pol-
icy updates
Interactive trajecto-
ries
Optimizing sequential decisions Simulator fidelity; reward de-
sign; sample cost
agents aggregate tactical recommendations from subordi-
nate asset specialists.
• Synthetic Market Ecologies(Section 11.3): Agent-based
market simulations where heterogeneous populations
of autonomous buyers, sellers, and liquidity providers
interact, allowing the study of emergent price dynamics,
market impact, and reflexivity.
The central research challenges involve attributing performance
gains to specific communication topologies (via rigorous role
ablations), managing communication latency overheads, and
preventing groupthink or herd dynamics.
Comparability note.Protocol-comparable coordination claims
should report MR-7 (roles/permissions, message protocol,
consensus, shared state, and evaluation); see Section 13.
Figure 13 illustrates these stylized archetypes.
11.1. Role-based Collaboration
Role-based collaboration assigns specialized roles to different
agents, each focusing on a specific aspect of the trading problem
while coordinating to achieve collective goals. This division of
labor enables deep specialization while maintaining coherent
decision-making Wooldridge (2009) [BG].
Representative Approaches. We distinguish three evidence
layers.Primary trading systemsin the current section-level
subset show role specialization most directly: TradingAgents
Xiao et al. (2024) assigns analyst/trader/risk/portfolio roles;
FINCON Yu et al. (2024) uses a manager–analyst architecture
with Conceptual Verbal Reinforcement (CVRF) to update
investment beliefs; TradingGroup Tian et al. (2025) combines
role specialization with reflection; and the REIT pipeline
Li (2026) makes an analysis–prediction–decision–execution
workflow explicit. These papers make decomposition visible,
yet complex role assignments can still obscure the source of
gains. Supportingattributiontherefore requires logging decision
contributions (which agent proposed or vetoed an action) and
running role/communication ablations that verify gains stem
from coordination rather than from increased computational
budget. General LLM multi-agent optimization work such
as HiveMind supplies relevant background on contribution-
guided credit assignment and online prompt refinement Xia
et al. (2026) [BG].
Benchmarks and simulated arenasform a second layer: Trader-
Bench, MarS, and related multi-agent market arenas Lopez-Lira
(2025); Li et al. (2024a); Yuan et al. (2026a) [BG] stress special-
ization and interaction patterns under their respective simulation
protocols. Trading-performance comparisons across these layers
require matched execution semantics and computational bud-
gets.
Background MAS/ABM literatureforms a third layer, including
social or behavioral market models Bohorquez and Cartlidge
(2024); Wheeler and Varner (2023) [BG], RL-plus-ABM in-
teraction studies Dicks et al. (2023); Oort et al. (2023) [BG],
workspace delegation Nie et al. (2026) [BG], and reciprocity-
oriented foundations Diau (2025); Gao et al. (2022) [BG]. These
works inform mechanism design through models of delegation,
reciprocity, and market interaction.
Communication Protocols. Role-based collaboration rests on
communication protocols that coordinate specialized agents ef-
fectively. Broadcasting allows an agent to share information
with all team members simultaneously, which suits market-wide
alerts or portfolio status updates. Peer-to-peer communication
enables direct exchange between specific agents, such as the risk
manager warning the trader about excessive exposure. Shared
memory provides a common knowledge base where agents can
read and write information, enabling asynchronous coordina-
tion without requiring all agents to be available simultaneously.
These protocols need to be designed to balance information rich-
ness against communication overhead, as excessive messaging
can slow decision-making in fast-moving markets Wooldridge
(2009) [BG].
Consensus Mechanisms. When specialized agents disagree,
consensus mechanisms aggregate diverse opinions into coherent
decisions. V oting treats all agents equally, with the majority or
plurality determining the final action. Expert weights assign
different influence to agents based on their historical accuracy
or domain expertise, allowing the analyst to dominate stock
selection while the risk manager influences position sizing.
Debate-based consensus enables agents to present arguments
and counterarguments, as illustrated by the bull–bear researchers
in TradingAgents Xiao et al. (2024). FinCon instead refines
investment beliefs across episodes through CVRF Yu et al.
(2024). The choice of consensus mechanism involves trade-
offs between speed (voting is fast) and quality (debate can
29

Three Coordination Patterns in Multi-agent Trading
Role-based
Structure:
Examples:
Scope:
• Specialized roles
• Peer communication
• Flat organization
• Analyst agent
• Risk agent
• Executor agent
• Specialized roles
Hierarchical
Structure:
Examples:
Scope:
• Manager agents
• Worker agents
• Command chain
• Portfolio manager
• Sector specialists
• Trading executors
• Task decomposition
Market Ecology
Structure:
Examples:
Scope:
• Competitive
• Emergent order
• No central control
• Diverse strategies
• Market feedback
• Evolutionary
• Market interaction
Figure 13:Three coordination patterns in multi-agent trading. Role-based collaboration assigns specialized roles (analyst, trader, risk manager)
to different agents. Hierarchical organization layers agents from strategic (asset allocation) to tactical (position sizing) to execution (individual
trades). Market ecology models agents interacting through markets with feedback and emergence. The structure/example/scope panels are stylized
archetypes of these organizational designs.
uncover blind spots but takes longer). Dynamic mechanisms
that adapt based on market conditions or agent confidence
are particularly valuable in volatile markets Hu et al. (2024);
Wooldridge (2009) [BG].
Task Allocation. Effective role-based collaboration requires
task allocation that matches work to agent capabilities and
current workload. Capability-based allocation assigns tasks
based on specialized expertise, such as routing earnings analysis
to the fundamental analyst while the technical analyst handles
technical signals. Workload-based allocation considers current
load, preventing bottlenecks when one agent is overwhelmed.
Hybrid approaches combine both factors, ensuring that urgent
but non-specialized tasks (such as emergency risk reduction)
can be handled by any available agent. Task allocation
may be centralized (a supervisor agent assigns work, as in
TradingAgents) or decentralized (agents self-assign based on
capability and availability). Dynamic reallocation enables
the system to adapt when agents fail or become overloaded,
improving robustness Wooldridge (2009) [BG].
Conflict Resolution. Disagreements between specialized
agents are inevitable, particularly when agents have different
perspectives (optimistic analyst vs pessimistic risk manager) or
when their roles create tensions (trader seeking profit vs risk
manager seeking safety). Negotiation allows agents to propose
compromises, such as reducing position size to satisfy both profit
targets and risk limits. Arbitration delegates dispute resolution
to a higher authority (the supervisor in TradingAgents), ensuring
that critical decisions are not deadlocked. Authority hierarchies
establish which agent’s view dominates in which domain
(the risk manager has veto power over position sizing, while
the analyst controls stock selection). Learning from past
conflicts improves resolution over time, with agents developing
heuristics for when to escalate disagreements and when to accept
compromises Wooldridge (2009) [BG].
11.2. Hierarchical Organization
Hierarchical organization structures agents into layers, with
higher-level agents making strategic decisions and lower-level
agents executing tactical actions. This structure enables
coherence across time scales, from long-term asset allocation to
short-term execution.
Representative Approaches. FinMem Yu et al. (2023b) illus-
trates hierarchy within a single agent’s memory rather than a
multi-agent command structure. It employs a working memory
for summarization, observation, and reflection, together with
long-term memory divided into shallow, intermediate, and deep
processing layers. These layers use different retention and de-
cay schedules to support daily trading decisions; they are not
separate working, episodic, and semantic stores. H-MEM Sun
and Zeng (2025) extends this with semantic hierarchy, reporting
efficiency improvements through hierarchical memory organi-
zation. In multi-agent settings, strategic agents set high-level
targets (“reduce tech exposure by 20%”) and tactical agents
determine specific trades to achieve these targets. General-
purpose frameworks provide complementary organizational ex-
amples: MetaGPT uses predefined roles and standard operating
procedures for software engineering Hong et al. (2024) [BG],
while DyLAN and HiveMind explore adaptive team selection
or prompt refinement Liu et al. (2023); Xia et al. (2026) [BG].
These mechanisms inform the design of trading hierarchies with-
out establishing trading performance themselves.
Benchmarks and Protocols. Coordination claims are difficult
to compare without common evaluation protocols and cost
and execution semantics. Recent work introduces live and
30

replay-based benchmarks for trading agents that stress sequential
decision-making under real or event-driven market dynamics,
including AI-Trader Fan et al. (2025) [BG], Agent Market
Arena Qian et al. (2025) [BG], LiveTradeBench Yu et al.
(2025) [BG], ContestTrade Zhao et al. (2025) [BG], and
PredictionMarketBench Arora and Malpani (2026) [BG]. These
benchmarks help separate architecture effects (coordination
design, memory, workflow) from model-backbone effects, but
remain sensitive to market selection, episode construction, and
transaction cost assumptions.
Protocol Implication
For multi-agent systems, we recommend explicit reporting
of: (i)cross-playevaluation (swap individual agents to
test interoperability vs. team overfitting), (ii) explicit
communication constraints(channel bandwidth and tool-
call budgets), (iii)crowding and impactmetrics (e.g.,
impact amplification under correlated policies), and (iv)
role ablationsto attribute gains to coordination rather than
increased information access.
Goal Decomposition. Hierarchical organization requires break-
ing high-level objectives into actionable sub-goals that lower-
level agents can execute. Top-down decomposition starts with
strategic objectives (“target 15% annual return and 10% volatil-
ity”) and recursively breaks them into smaller targets (“allo-
cate 60% to equities, 30% to bonds, 10% to cash” then “select
50 technology stocks with equal weights”). Constraint-based
decomposition helps ensure that sub-goals respect risk limits,
liquidity constraints, and regulatory requirements. Dynamic
decomposition adjusts targets based on market conditions, such
as reducing return targets during bear markets or tightening
risk limits when volatility spikes. The effectiveness of goal
decomposition depends on how well strategic intent can be trans-
lated into tactical guidance without micromanaging lower-level
agents; layers should specify clear I/O contracts (e.g., strategic
targets vs. tactical orders) to prevent semantic drift Wooldridge
(2009) [BG].
Feedback Mechanisms. Hierarchies rely on upward feedback
to close the loop between strategy and execution. Bottom-up
reporting enables tactical agents to inform strategic agents about
outcomes, constraints, and opportunities. For example, execu-
tion agents report that liquidity is insufficient for the desired
position size, prompting strategic agents to revise the allocation.
Exception escalation triggers when lower-level agents encounter
problems they cannot resolve, such as unexpected market events
or violations of risk limits. Performance feedback provides in-
formation about which strategies are working, enabling strategic
agents to reallocate resources to successful approaches. Effec-
tive feedback requires appropriate aggregation: raw data from
execution must be summarized into metrics that inform strategic
decisions without overwhelming strategic agents with details
Wooldridge (2009) [BG].
Exception Handling. Lower-level agents inevitably encounter
situations that exceed their authority or capability, requiring es-
calation to higher-level decision-makers. Predefined escalation
triggers determine when to elevate issues, such as position lim-
its exceeded, unusual market conditions, or conflicting signals.
Time-sensitive exceptions (market crashes, circuit breakers) re-
quire immediate escalation with minimal delays. Resolution
strategies range from fully automated (circuit breakers automati-
cally reduce exposure) to human-in-the-loop (unusual patterns
reported to human supervisors). Learning from exceptions im-
proves future handling, with systems developing better triggers
and resolution strategies over time. The design of exception
handling involves trade-offs between false positives (escalating
too often, creating noise) and false negatives (missing critical
issues that require intervention) Wooldridge (2009) [BG].
Temporal Abstraction. Different layers of the hierarchy
operate at different time scales, enabling separation between
long-term planning and short-term reaction. Strategic agents
operate at daily, weekly, or monthly frequencies, making
decisions about asset allocation, factor tilts, and overall portfolio
construction. Tactical agents operate at intraday or minute-
level frequencies, managing individual positions, entry and exit
timing, and execution quality. This separation prevents short-
term noise from disrupting long-term strategy: a temporary
price spike should not trigger a reallocation of the entire
portfolio. However, temporal abstraction creates challenges
for coordination: strategic agents need to set bounds (risk limits,
position limits) that constrain tactical agents without being
overly restrictive. Multi-scale learning enables agents to learn at
different time horizons, with strategic agents learning from long-
term patterns while tactical agents adapt to short-term dynamics
Sutton et al. (1999) [BG].
11.3. Market Ecology
Market ecology models agents as participants in a market
environment, interacting through trading and prices rather than
direct communication. In the current literature, this pattern
is best read as an exploratory setting for studying collective
behavior, not as mature evidence that ecological coordination
improves live trading outcomes.
Representative Approaches. Market simulators Hashimoto
et al. (2025) populate markets with heterogeneous agents to gen-
erate synthetic market data and to stress test strategies under con-
trolled conditions. Related work studies how agent-environment
feedback can produce boom-bust dynamics and how repeated
interaction may lead to undesirable emergent coordination, mo-
tivating regulatory and monitoring considerations. FinEvo Zou
et al. (2026) proposes an ecological market-game framing to
study the evolution of interacting financial strategies, empha-
sizing that competitive performance can depend on population
composition and adaptive feedback rather than isolated back-
tests. Validating ecological models requires rigorous calibration
against real market microstructure to avoidsimulator overfitting,
and protocols must further audit fortimestamp leakageandcon-
sensus smoothingso that emergent coordination is not an artifact
of look-ahead bias or noise suppression.
Pioneering work on generative agents Park et al. (2023) [BG] es-
tablished the viability of LLM-based simulacra, and subsequent
31

financial-market simulations Hashimoto et al. (2025) use such
agents to probe how collective behavior shapes market dynamics
in controlled settings.
Market Mechanisms. Market ecology relies on established
market structures to mediate agent interactions without requiring
direct coordination. Continuous double auctions enable buyers
and sellers to trade at any time, with prices emerging from the
real-time balance of supply and demand. Call auctions aggregate
orders over specific time intervals (open, close, volatility
interruptions), determining prices through batch execution that
reduces informational asymmetry. Dealer markets designate
specific market makers who provide liquidity by continuously
quoting bid and ask prices, with agents trading against these
quotes rather than directly with each other. Each mechanism
creates different incentives and dynamics: continuous double
auctions favor fast reactions to information, call auctions reduce
timing risk, and dealer markets provide guaranteed liquidity but
at a cost (the bid-ask spread). The choice of market mechanism
shapes the ecology by determining which strategies are viable
and how information propagates through prices Kyle (1985);
Glosten and Milgrom (1985) [BG].
Price Formation. In market ecology, no single agent sets prices;
instead, prices emerge from the aggregate behavior of all agents.
Order aggregation combines individual buy and sell orders into
a collective order book, with the intersection of supply and de-
mand determining the market-clearing price. Supply-demand
balance shifts as agents react to news, portfolio changes, or
risk management needs, causing prices to adjust. Informational
efficiency measures how quickly prices incorporate new informa-
tion, with efficient markets preventing agents from consistently
profiting from public information. However, when agents are
heterogeneous (different beliefs, time horizons, risk tolerances),
prices may deviate from fundamental values for extended pe-
riods, creating opportunities for some agents at the expense
of others. The dynamics of price formation depend on agent
diversity: homogeneous agents tend to produce rapid conver-
gence to consensus prices, while heterogeneous agents create
more complex patterns with mispricings that persist until cor-
rected by informed agents Kyle (1985); Glosten and Milgrom
(1985) [BG].
Reflexivity and Feedback Loops. Market ecology creates
reflexive relationships where agent actions affect prices, which in
turn affect agent perceptions and actions. This two-way feedback
can produce complex dynamics not present in systems with one-
way causality. Positive feedback amplifies initial movements:
price increases attract trend-following agents who buy, pushing
prices higher and attracting more trend followers, potentially
creating bubbles. Negative feedback stabilizes: price increases
trigger profit-taking by mean-reversion agents who sell, pushing
prices back toward fundamentals. The balance between positive
and negative feedback determines market stability. Reflexivity
becomes particularly powerful when agents learn and adapt:
successful strategies attract imitators, changing market dynamics
and potentially rendering the original strategy unprofitable.
This co-evolution of agents and markets creates continuously
changing patterns, making long-term prediction difficult even as
short-term patterns may be exploitable Shiller (1981); Kirilenko
et al. (2017) [BG].
Emergent Phenomena. The interaction of heterogeneous
agents through market mechanisms can generate collective
phenomena that are not apparent from studying individual
agents in isolation. Bubbles may occur when positive feedback
dominates, with rising prices attracting speculative buying
disconnected from fundamentals. Crashes may follow when
bubbles burst or when negative feedback triggers panic selling,
with prices plummeting as agents rush to exit simultaneously.
Flash crashes—extreme short-term collapses in which prices
plummet and recover within minutes—are mechanistically
plausible when high-frequency agents interact with market
structure. Tacit collusion is another plausible risk when
agents learn to coordinate behavior implicitly through repeated
interaction without explicit communication, raising regulatory
concerns about market manipulation. Because these phenomena
depend on the collective behavior of many agents and are
difficult to predict, agent-based simulation is more appropriately
viewed as a hypothesis-generation tool for understanding market
dynamics and stress cases Kirilenko et al. (2017); Shiller
(1981) [BG].
Strategy Crowding and Alpha Decay.As LLM-based agents
proliferate, similar training data and reasoning patterns may lead
tostrategy homogenization. When multiple agents:
•Use similar foundation models (GPT-4, Claude)
•Fine-tune on similar financial corpora
•Employ comparable CoT or RAG patterns
they may generate correlated trading signals, creating mechanis-
tically plausible risks such as:
1. Alpha decay: Common signals are arbitraged away faster
2. Self-reinforcing trends: Similar entry points amplify
momentum
3. Correlated exits: Simultaneous stop-loss triggering
increases volatility
4. Flash crash risk: Rapid unwinding of crowded positions
The evidence base currently lacks studies of multi-agent market
impact at scale—a critical gap that requires simulation-based
research before deployment.
Regulatory Constraints. Regulators shape market ecology
by constraining agent behavior to maintain market integrity
and stability. Position limits prevent any single agent from
dominating the market or taking excessive risks. Circuit
breakers halt trading during extreme volatility, providing time for
information to diffuse and potentially preventing panic selling.
Market maker obligations require designated liquidity providers
to quote prices continuously, ensuring that other agents can
always trade. Reporting rules may oblige agents to disclose
large positions or trades, reducing information asymmetry.
Manipulation rules prohibit agents from engaging in behavior
32

that artificially affects prices (spoofing, layering, pump-and-
dump schemes). The design of these regulations must balance
competing goals: too little regulation enables manipulation and
instability, while too much regulation reduces liquidity and
efficiency. Agent-based simulation enables regulators to test
proposed rules before implementation, identifying unintended
consequences and optimizing regulatory parameters European
Parliament and Council of the European Union (2014, 2016);
Article 29 Working Party (2018).
TradingAgents is coded R2, whereas FinCon and TradingGroup
are R0; all three report order-level execution semantics. The
hierarchical investment pipeline reports target weights, and
FinEvo uses market-game execution. These tags record reporting
categories rather than equivalent execution realism.
Table 18 compares their communication, authority, and design
considerations.
Latency Constraints on Coordination.The coordination mecha-
nisms discussed above must operate within the latency budget
established in Section 6. Coordination cost is dominated by
communication, consensus formation, and decision aggregation,
so voting is typically cheaper than debate while expert-weighted
aggregation sits in between. In latency-sensitive regimes, sys-
tems may need to prefer the simplest mechanism that preserves
acceptable decision quality. This latency-aware coordination de-
sign remains an open research direction for financial multi-agent
systems.
The representative systems above illustrate several coordination
mechanisms. Extension-window examples include selective-
consensus trading (Li et al., 2026b), co-evolving MARL agents
(Jia et al., 2026), live deliberative analysis (Letteri, 2026), and
a belief-to-trade execution layer (Wang et al., 2026e). Alpha-
mining pipelines are discussed in Section 7. Background market
ecosystems examine self-organization (Hashimoto et al., 2026;
Saxena et al., 2026), specialized asset markets (Casas and Mon-
tero, 2026; Passos et al., 2026), mechanism design (Sheng and
Shen, 2026; Qian, 2026; Varghese et al., 2026), and behav-
ioral dynamics (Ouyang and Sui, 2026; Park, 2026). Language-
grounded testbeds (Shi et al., 2026) and prediction-market arenas
(Barot and Borkhatariya, 2026) provide further settings for study-
ing interaction. These background works inform coordination
design and market behavior; the ledger separates them from
evaluated, action-producing trading systems.
Synthesis and Coordination Trade-offs.Role-based collabora-
tion, hierarchy, and market ecology differ in how agents com-
municate and where coordination occurs. Communication cost,
consensus quality, and attribution shape these designs; role abla-
tions and compute-matched single-agent baselines help distin-
guish coordination effects. The final section examines persistent
adaptation and structural self-evolution in Section 12.
12. Adaptation and Self-Evolution
Adaptation is the umbrella term for updates to an agent’s state or
behavior. Here, self-evolution denotes agent-managed changes
retained across decision episodes; structural or architectural self-
evolution is the narrower case in which strategy code, update
procedures, modules, interfaces, workflows, or system topology
change. Memory consolidation changes what experience
is retained, while meta-learning changes how learning is
performed; either can support persistent adaptation without
changing the architecture. Reflection within a single decision
episode does not by itself qualify as self-evolution. Building
on the stores and retrieval operations in Memory Architecture
and the ICL, SFT, and RL update modes in Learning Paradigms,
this section examines memory consolidation, meta-learning, and
self-reflection in that order: “How are agent updates carried
across decision episodes and evaluated?”The conceptual update
loop is shown in Figure 15.
Note: Many mechanisms described in this section (e.g., memory
consolidation, meta-learning, self-reflection) originate in general
AI research; in trading, they remain experimental and should be
interpreted through explicitupdate governancerather than as
industry-standard practice. Studies marked [BG] are background
literature without end-to-end trading evaluation. Adaptation/
self-evolution claims are only comparable when the update loop
is reproducible (MR-6; see Section 13): papers should report
what can change (prompts, memory summaries, retrieval indices,
weights), when updates trigger, and what historical window is
used. They should preserve immutable logs, frozen execution
and cost semantics, and a rollback path, and evaluate the post-
update state on sealed data.
12.1. Memory Consolidation
Building on the stores and retrieval operations described in
Section 4, memory consolidation changes what those stores
retain over time: it compresses experience into reusable patterns
while discarding details that no longer aid retrieval.
Representative Approaches. Within the section-level primary
subset, memory-consolidation-like behavior appears in systems
that retain episodic traces and derived summaries for later re-
trieval, including FinMem and related retrieval-centered trading
agents Yu et al. (2023b); Zhang et al. (2024). Background work
considers replay, summarization, abstraction, and forgetting as
ways to select or compress those traces. Broader systems such
as TradingGPT remain in the wider citation set and do not enter
the section-level primary-study count Li et al. (2023).
Technical Mechanisms. Background methods score memories
by recency, outcome, or retrieval frequency and use replay,
compression, or abstraction to retain useful signals Lin (1992);
Schaul et al. (2016); McClelland et al. (1995); Hinton and
Salakhutdinov (2006) [BG]. When market conditions change,
temporal or contextual rules can resolve conflicting memories
McClelland et al. (1995); Kirkpatrick et al. (2017) [BG]. These
operations may run periodically, respond to events such as
regime shifts, or combine both schedules Kirkpatrick et al.
(2017) [BG]; their value depends on whether the resulting state
remains temporally valid and auditable.
Audit Trail Requirement: Summarization can hallucinate details
not present in the original log or lose the link to the trade decision.
33

Analyst agent
 Trader agent
Risk agent
 Execution agent
Market environment
Orders in
Quotes · prices · spreads · fills out
Reflexive feedback
Competition
Figure 14:Market ecology interaction network. Agents interact both with one another and through the market environment, where prices, spreads,
quotes, and fills feed back into subsequent behavior. The figure highlights reflexive feedback and competition channels that can support exploratory
study of crowding, instability, and adaptation.
Table 18:Multi-agent coordination patterns and design considerations.Tags: R=Reproducibility level (R0–R3), E=Execution semantics reported.
Tags apply to the named trading systems in each row (see Section 2 for full coding rules).
Pattern Example Comm. Decision making Coordination considerations Tags
Role-based TradingAgents
Xiao et al. (2024),
FINCON Yu et al.
(2024), Trading-
Group Tian et al.
(2025)
Direct, rich
communica-
tion
Debate; belief up-
dates
Communication and decision aggrega-
tion
R0–R2,E
Hierarchical Multi-agent invest-
ment pipeline Li
(2026)
Vertical, lay-
ered feedback
Top-down com-
mands, bottom-up
reporting
Layered reporting and decision aggre-
gation
R0,E
Market Ecology Agent simulations;
FinEvo Zou et al.
(2026)
Indirect, via
prices/trades
Decentralized, in-
dependent
Simulator calibration and market cou-
pling
R0,E
To remain auditable, consolidated memories must retain an
immutable pointer (hash or timestamp) to the raw transaction
logs. Adaptation protocols should periodically validate that
summaries do not contain factual errors or future information
compared to the ground-truth logs.
12.2. Meta-Learning
Meta-learning enables agents to learn how to learn, improving
the efficiency and effectiveness of the learning process itself.
Finance-oriented prototype systems considered here primarily
explore multi-agent evolutionary loops to generate and select
strategies or factors under backtest feedback Yun et al. (2025);
Luo et al. (2025); Zou et al. (2026). The extension window
adds a distinct self-evolving cluster—experience-driven policy
refinement Kim et al. (2026b), rubric-policy evolution Chen
et al. (2026b), agent-to-agent alpha co-evolution Li et al.
(2026e), meta-evolution of trading programs Sharma and
Shroff(2026); Kvasiuk et al. (2026), and post-trained local
research agents Wang et al. (2026d)—alongside regime-adaptive
continual learning for portfolio management Pan et al. (2026).
These results remain prototype-level and must be interpreted
under each study’s evaluation and cost/execution assumptions.
Evolutionary simulation also provides an existence proof for
trend-following behavior Chen (2026a), situating adaptation in
a market-ecology context. Across these lines, the central trading
challenge is to define tasks without temporal leakage and seal
feedback against future outcomes.
Task Splitting Requirement. In trading, a “task” cannot simply
be a random sample of assets or days. To prevent leakage, tasks
must be split by time (e.g., 2010–2015 as source, 2016 as target)
34

Trading
experience
Actions · outcomes
Memory
consolidation
Retain patterns
Update policy
Meta-learning
Reflection
Critique reasoning
Shared governance across the update loop
Logging
 Versioning
 Protocol constraints
Iterative update
Figure 15:Conceptual governed update loop. Agents accumulate experience through trading, consolidate important patterns into memory, apply
meta-learning-like update policies, and use reflection to critique reasoning under logging and rollback constraints.
or by distinct, non-overlapping asset classes. Random shuffling
of episodes across time violates the causal structure of markets,
creating false “adaptation” that is merely memorization of future
regimes.
Representative Approaches. Background MAML learns an ini-
tialization that supports rapid adaptation, while learning-to-learn
methods can update the learning-rate schedule, exploration strat-
egy, or architecture Finn et al. (2017) [BG]. Finance-oriented
prototypes apply iterative critique to factor or policy search:
AlphaAgent regularizes factor generation, and TradingGroup
combines reflection with data synthesis Tang et al. (2025); Tian
et al. (2025). General multi-agent optimization provides a re-
lated refinement pattern, but remains background rather than
finance-specific evidence Yuksel and Sawaf (2024) [BG].
Technical Mechanisms. Meta-learning evaluates adaptation
across a task distribution, using support data for within-task
updates and query data to measure post-update performance.
MAML formalizes this as inner-loop adaptation and outer-
loop optimization; few-shot and domain-generalization methods
extend the same idea to low-data or unseen related tasks Finn
et al. (2017); Vinyals et al. (2016); Snell et al. (2017); Muandet
et al. (2013) [BG]. Memory or replay can support these updates,
but concerns how learning uses stored experience rather than
how that experience is represented Finn et al. (2017) [BG].
Transfer learning applies learned representations or behavioral
strategies to new tasks, while domain adaptation fine-tunes them
with target-specific data Pan and Yang (2010) [BG].
12.3. Self-Reflection
Self-reflection enables agents to critique their own reasoning
and to catch mistakes before they propagate into actions, thereby
improving decision quality.
Representative Approaches.
Reflexion Shinn et al. (2023) [BG] adds an explicit critique–
revise loop: after proposing a decision, the agent diagnoses
weaknesses in its own reasoning and regenerates an improved
plan. In trading settings, such reflection can check for com-
mon failure modes (feature/label leakage, stale data, ignored
costs, regime mismatch). Self-consistency and retrospective
error analysis complement Reflexion by exposing unstable ra-
tionales and recurring mistake patterns. In a finance-specific
setting, CryptoTrade uses a reflective mechanism to refine zero-
shot cryptocurrency trading decisions by analyzing outcomes of
prior trades Li et al. (2024c). Within the section-level primary
subset, the main trading-facing anchor is TradingGroup, which
combines role specialization with self-reflection and data syn-
thesis Tian et al. (2025); other examples illustrate critique and
refinement mechanisms.
Technical Mechanisms: Protocol Implication
Effective self-reflection is aprotocol, not a free-form
“thinking harder” step; we suggest five stages. (i)Critique
generation: produce actionable checks tied to the trade
proposal (data timestamps, assumptions, transaction costs,
liquidity/slippage, and risk constraints). (ii)Refinement: run
a small, bounded number of critique–revise iterations with
early stopping; log the critique and the resulting change for
auditability. (iii)Consistency/uncertainty: sample multiple
reasoning paths; treat disagreement as a deferral/abstain
signal to reduce overconfident errors, but validate thresholds
empirically (consensus is not correctness). (iv)Post-
trade review: categorize failures (prediction vs execution
vs risk) and store compact lessons in memory keyed by
instrument/regime so they can be retrieved at decision time.
(v)Pre-trade verification: enforce hard constraints (risk
limits, compliance rules, and operational feasibility) as
deterministic checks.
Risk of Search Bias: Unbounded reflection acts as a search
process. To prevent “testing into success” (retrying until a
profitable trade appears by chance), protocols must enforce
aReflection Budget(max iterations) and refrain from using
Out-of-Sample feedback to terminate the loop. Reflective traces
are not a substitute for testing, monitoring, or out-of-sample
evaluation Wang et al. (2022); Madaan et al. (2023); Geifman
and El-Yaniv (2017) [BG].
Synthesis and Governance Dimensions.The subsections and
Table 19 distinguish updates to retained experience, learning pro-
35

Table 19:Conceptual update mechanisms and uses of experience. All entries are background mechanisms (BG); the descriptions identify update
operations and the role of retained experience.
Mechanism Description Key Mechanism Update work Experience use Tags
Consolidation Summarize, ab-
stract, forget
Importance scoring, com-
pression
Memory summarization, abstrac-
tion, and forgetting
Selects retained traces for later
retrieval
BG
Meta-Learning Learn to learn MAML Finn et al. (2017),
memory-based opt
Inner-loop adaptation and outer-
loop optimization
Support/query data across tasksBG
Self-Reflection Critique and refine Reflexion Shinn et al.
(2023), self-consistency
Critique and revision of a pro-
posed plan
Critique informs a regenerated
plan
BG
cedures, and reasoning outputs; persistent changes to strategy
code, update procedures, or system organization are structural
self-evolution. Whether any update carries across later trad-
ing decisions is an empirical question under the governance
conditions above. These distinctions frame the cross-cutting
challenges and future directions in Section 13.
13. Technical Challenges, Methodological Guidelines, and
Open Problems
The preceding sections have systematically synthesized the
architectural foundations, functional capabilities, and adaptation
pathways of agentic trading systems. This section examines
the principal technical and practical bottlenecks that arise
when deploying LLM agents in financial markets, consolidates
methodological best-practice guidelines (MR-1–MR-7) to foster
reliable empirical evaluation, and outlines key open research
problems.
As observed across the empirical literature (n =80), researchers
adopt varying conventions regarding data splits, transaction
frictions, asset universe definition, and execution timing. To
promote cross-study comparability, mitigate data snooping,
and facilitate real-world translation, we distill these recurring
empirical considerations into a structured set of methodological
recommendations:
Methodological Guidelines and Recommended Evalua-
tion Practices (MR-1–MR-7)
To support rigorous benchmarking and reproducibility, future
research on agentic trading is encouraged to document the
following empirical dimensions:
• MR-1 (Data&Universe): Specify asset universe
construction criteria, survivorship bias treatment, and
synchronized data availability timestamps across all
perceived modalities.
• MR-2 (Temporal Splitting): Enforce strict chrono-
logically ordered train/validation/test partitions, walk-
forward or rolling windows, and explicit embargo periods
to prevent look-ahead bias; for iterative alpha search,
maintain a frozen holdout test set.
• MR-3 (Action Semantics): Explicitly define output
format (discrete orders vs. continuous portfolio target
weights), decision timestamps, order mapping rules, and
portfolio constraints (leverage, gross/net exposure).
Methodological Guidelines (continued)
• MR-4 (Execution&Costs): Explicitly state execution
timing, fill price assumptions (e.g., next-open or volume-
weighted prices), rebalancing intervals, and realistic
friction models (brokerage fees, bid-ask spread, market
impact).
• MR-5 (Leakage Controls): Verify causal temporal
integrity across feature normalization, text sentiment
alignment, and target label construction.
• MR-6 (Artifacts&Verification): Provide open-source
code, reproducible configuration scripts, random seeds,
and structured decision logs; for adaptive systems, record
update frequencies and rollback criteria.
• MR-7 (Multi-Agent Evaluation): In collaborative or
competitive systems, document agent role topologies,
communication protocols, and ablation experiments
isolating the marginal contribution of inter-agent interac-
tions.
Table 20 relates the guidelines to each study’s task. For
end-to-end trading, universe construction and cost models
help interpret profitability; anexecution algorithmreceiving
parent orders may take the universe as given. A standalone
component study, such as sentiment analysis, needs time-
consistent evaluation but may operate without a transaction cost
model. The matrix distinguishes relevant evaluation dimensions
from fields outside the study’s scope.
13.1. Technical Challenges
The subsections below synthesize technical challenges, method-
ological guidance, and representative research directions.
13.1.1. Hallucination in Finance
LLM hallucination, which generates plausible but false infor-
mation, posesmaterialrisk in finance because trading decisions
may be executed, and losses realized, before the underlying
claim can be verified. Only one primary study explicitly fore-
grounds this issue, so the discussion below combines that direct
evidence with cross-section risk synthesis.
Propagation Mechanisms.In agentic workflows, hallucinated
claims propagate through tool calls into downstream actions. A
fabricated earnings report can trigger:
1. Erroneous position entry (immediate loss when corrected)
2. Stop-loss cascade (if other agents detect the “signal”)
36

Table 20:Applicability of the MR-1–MR-7 evaluation guidelines by study type.E: Essential to interpreting the relevant result;R: Recommended for
verification;O: Task-dependent;–: Generally outside the stated task. These designations summarize this survey’s methodological recommendations.
MR Item End-to-End Execution Component
(Full Trading) (Ord/Wt Algo) (Perception/Risk)
MR-1 (Data & Universe)EOE
MR-2 (Time Split & Leakage)E E E
MR-3 (Action Semantics)E E–
MR-4 (Exec & Costs)E E–
MR-5 (Leakage Audit)E R R
MR-6 (Artifacts)R R R
MR-7 (Multi-Agent Eval) O – –
Reading the matrix:Applicability follows the study’s task and reported result. Action semantics and cost assumptions are essential to interpreting trading or
execution outcomes, while a standalone perception study may be evaluated without generating orders. Universe selection can be exogenous to an execution algorithm.
Artifacts and extraction checks support verification, and multi-agent evaluation applies when interaction is part of the design. The matrix guides interpretation;
corpus-level reporting counts follow the separate coding rules in Section 2.
3. Confidence-based position scaling (larger losses due to
false certainty)
Mitigation Limitations.Binding outputs to verifiable sources
(FinMCP, HydraRAG) shifts rather than eliminates risk, because
source selection itself can be erroneous. Cross-validation helps
only where multiple independent sources exist, which is often
not the case for time-sensitive trading signals; moreover, current
fact-checking mechanisms operate at second-scale latency,
which is incompatible with millisecond trading decisions. We
therefore cite these systems as illustrative tooling, not as
empirically validated mitigations.
Regulatory Implications.Firms deploying LLM agents may
face heightened liability if hallucinated outputs cause client
losses; documentation of source binding, validation checks, and
human review may be needed to withstand regulatory scrutiny.
13.1.2. Look-ahead Bias
We treat look-ahead bias here as methodological guidance
tied directly to MR-2 and MR-5. Recent work includes
dedicated analyses of temporal leakage in LLM backtesting
Zhang and Stadie (2026), look-ahead-freedom as a verifiable
correctness property Fonseca (2026), deployment-evidence
limits of reported alpha Ye et al. (2026c), and execution-
assumption audits Yao et al. (2026), alongside leakage-masking
benchmarks Zhu et al. (2026b); Qu and Chen (2026); Cai et al.
(2026). Methodological work goes further by engineering the
problem away: anonymization-first evaluation asks whether
“blindfolded” LLMs can still trade when asset identities and
dates are withheld Jeon and Lee (2026), directly operationalizing
look-ahead-freedom as a test condition.
Look-ahead bias occurs when models inadvertently access
future information during training or evaluation, producing
unrealistic performance estimates that fail to generalize to
real trading conditions. The risk is particularly insidious in
time-series settings, where leakage can enter through improper
cross-validation that shuffles temporal data, technical indicators
computed with future information (e.g., centered moving
averages), or textual sources that contain hindsight about market
movements. Detection requires careful examination of model
inputs and training procedures, including causal inference tests
that check whether model performance degrades when strict
temporal constraints are enforced: a model that appears strong
under naive random splits can degrade sharply under proper
time-consistent evaluation, revealing substantial look-ahead
contamination López de Prado (2018). Prevention requires
strict temporal splitting (train on past, test on future), walk-
forward validation that simulates real-time deployment, and
causal modeling so that information flows only from past to
future. Without these controls, even the most sophisticated
learning and adaptation procedures fail under evaluation leakage.
13.1.3. Latency vs Accuracy Tradeoff
Latency is a design constraint that links reasoning depth, model
inference, communication, and execution timing. System 2
reasoning (reflective, multi-step) yields better decisions but is
too slow for high-frequency trading, where decisions must be
made in microseconds, while System 1 reasoning (reactive,
fast) lacks the depth for complex decisions involving multi-
hop reasoning or extensive analysis. In latency-sensitive
regimes, the throughput advantage of faster decision policies
can therefore outweigh modest accuracy gains from slower
deliberation, especially when opportunities are fleeting and
execution queues are competitive. Hybrid approaches address
this tension with cascaded designs: fast System 1 handles
routine decisions using Section 3 perceptual features and
escalates difficult cases to slower System 2 reasoning that
leverages Section 5 deliberative mechanisms. Model distillation
offers a complementary route, compressing large reasoning
models into smaller, faster models that retain much of their
accuracy. Future work should develop tradeoffmechanisms that
allocate computational budget dynamically according to decision
importance, market volatility, and time pressure, potentially
learned via reinforcement learning.
13.1.4. Explainability vs Performance
The explainability–performance tension is a cross-section gover-
nance concern. Representative approaches include debate-based
explainable trading Huang et al. (2026b), post-hoc explanation
37

of learned portfolio policies de la Rica Escudero et al. (2025),
and audits of asset-specific preferences embedded in financial
LLMs Wu (2026). The discussion below accordingly provides
background and author guidance linked to deployment gover-
nance.
More complex models (deep neural networks, ensemble meth-
ods, large language models) often achieve better performance
but are less interpretable, creating a fundamental tension be-
tween explainability and predictive power. This tension has
practical as well as academic weight: depending on jurisdiction
and system role, regulatory and legal frameworks (e.g., the EU’s
MiFID II) may impose governance, record-keeping, and explain-
ability expectations for algorithmic trading and decision support
European Parliament and Council of the European Union (2014),
and GDPR provisions with subsequent guidance can imply obli-
gations to provide “meaningful information” about automated
processing in certain contexts, though scope and applicability
vary European Parliament and Council of the European Union
(2016); Article 29 Working Party (2018). When an agent’s
alpha generation module (Section 7) triggers a large position,
risk managers and regulators need to know why—whether the
driver was a particular news event, a technical-indicator pattern,
or a reasoning chain. Neuro-symbolic approaches pair neural
components for pattern recognition with symbolic components
for transparent reasoning, aiming to preserve both performance
and interpretability. Attention visualization highlights which
inputs most influenced the model (e.g., specific news articles
or price movements), while counterfactual explanations spec-
ify what would have had to change to alter a decision (e.g.,
“the trade would not have occurred if the FOMC minutes had
been less hawkish”). Regulatory and governance expectations
around explainability are likely to motivate further advances in
this area, particularly for the risk-management and compliance
applications of Section 9.
Many academic systems demonstrate explanations over offline
datasets or controlled prototypes; production deployments
typically require additional engineering for auditability (decision
logs, data lineage, and controlled model/prompt changes) to
make explanations actionable for governance.
13.1.5. Computational Cost and Economic Feasibility
The economic viability of LLM-based trading agents depends on
the relationship between inference costs and generated returns.
A simple annualized estimate is
Annual API Cost=D×N×C req,
where D denotes trading days per year, N the number of
decisions per day, and Creq the effective per-request cost implied
by model pricing, prompt/completion token budgets, and any
tool-specific charges. Because vendor pricing and model
offerings change rapidly, empirical cost estimates should specify
the model version, pricing snapshot date, token assumptions,
tool usage, and the break-even gross P&L required for net
profitability after inference and execution costs. Recent work
directly examines whether agentic trading systems can cover
their inference costs once those costs are charged against returns
Duan et al. (2026).
13.1.6. Evaluation Protocols and Deployment Safeguards
This subsection translates the survey-wide minimum reporting
framework (MR-1–MR-7) into concrete deployment safeguards,
drawing on the recurring reporting gaps identified earlier.
Evidence-backed guidelines and common anti-patterns for
agentic trading research and deployment include:
• Guard against temporal leakage: use strictly time-
ordered splits and walk-forward evaluation, and ensure
feature engineering and scaling are fit only on past data
Albelali and Ahmed (2025).
• Avoid unrealistic cost models: include fees, bid–ask
spread, slippage, and market impact, and report sensitivity
to cost assumptions Perold (1988); Olby et al. (2025).
• Check universe construction: document inclusion and
exclusion rules and timestamp availability, and audit
for survivorship/selection bias when building backtest
datasets Brown et al. (1992).
• Mitigate backtest overfitting: separate model selection
from final evaluation, use robust out-of-sample proce-
dures, and be explicit about multiple-testing risk Arian
et al. (2024).
• Add deployment safeguards: maintain immutable action
logs that link each action to its inputs, evidence, and model
versions, and use verifiable retrieval, citation checks, and
cross-source consistency tests Khatchadourian (2026);
Tan et al. (2025b).
The extension cohort supplies early empirical anchors for this
guidance: backtest-to-live gaps measured directly in crypto
markets Yu et al. (2026b), a live hybrid trading agent evaluated
under a shared task protocol Rashid et al. (2026), prospective
process-aware evaluation of adaptive agents Luo et al. (2026b),
and a unified platform for tracking agentic trading performance
over time Li et al. (2026a).
13.2. Human-in-the-Loop Oversight
Although this survey focuses on agentic systems, many realistic
deployments retain human oversight at escalation points such
as large notional changes, regime breaks, or tool failures. We
therefore view human-in-the-loop design as a practical control
boundary: stronger autonomy should imply stronger logging,
clearer intervention rules, and explicit specification of when
human approval is mandatory.
13.3. Negative Results and Failed Designs
The literature is likely affected by survivorship bias at the survey
level as well as at the backtest level. Few papers report failed
prompts, abandoned reward schemes, degraded live performance,
or architectures that increased turnover without improving net
returns. We therefore interpret the absence of negative results
as a reporting limitation rather than as evidence that the design
space is uniformly promising.
38

13.4. Future Directions
13.4.1. Neuro-Symbolic Integration
Current LLM-based agents rely almost entirely on neural
computation, which is flexible but opaque and unreliable
where exact calculation or logical guarantees are required.
As discussed in Section 5, purely neural approaches struggle
with tasks such as portfolio optimization under constraints or
exact arithmetic. Neuro-symbolic integration addresses this by
combining neural networks (for pattern recognition and learning
from data) with symbolic reasoning (for logic, constraint
satisfaction, and exact computation): hybrid architectures can
use neural networks to extract structured information from
text (prices, dates, entities) and symbolic reasoning to perform
financial calculations, enforce budget constraints, and maintain
logical consistency. Specific approaches include (1)neural
theorem proversthat use neural networks to guide proof
search for financial constraints; (2)differentiable logicthat
integrates logical constraints into neural network loss functions;
(3)program synthesis, in which LLM-generated code is
formally verified; and (4)neuro-symbolic ILP(Inductive
Logic Programming), which learns logical rules from neural
representations. The research objective is to combine neural
flexibility with symbolic precision while keeping the resulting
systems auditable enough for financial use.
13.4.2. Longer-Term Directions: Coordination, Governance,
and Infrastructure
Three longer-term directions extend these expert-system design
considerations. First, larger multi-agent market simulations
could serve as controlled “wind tunnels” for studying crowd-
ing, flash episodes, and systemic-risk propagation. The current
evidence base is concentrated in small role-based teams, motivat-
ing evaluation of larger agent populations. Second, increasing
agent autonomy motivates governance research on auditable
records, intervention rules, and sandboxed evaluation that clar-
ify who approved, monitored, or overrode each action. Third,
low-latency infrastructure and model compression support de-
ployment; evaluating their benefits requires end-to-end decision
latency, execution timing, and cost/benefit analysis.
Table 21 connects the survey’s design themes with representative
studies and the evaluation dimensions needed to interpret them.
Across the empirical literature, rigorous evaluation methods—
such as sealed out-of-sample testing, realistic market impact
modeling, and latency-aware execution—are increasingly recog-
nized as foundational pillars for advancing the field. Combining
architectural innovation with disciplined empirical validation
will be paramount as autonomous agent systems transition from
experimental prototypes toward resilient, production-grade mar-
ket deployment.
14. Conclusion
14.1. Synthesis of the Agentic Trading Landscape
The integration of Large Language Models into quantitative
finance represents a fundamental paradigm shift from static,
black-box forecasting models toward autonomous, cognitive
trading agents. By unifying multimodal perception, structured
memory retrieval, multi-step cognitive reasoning, and friction-
aware order execution, agentic systems introduce an adaptive
decision loop capable of operating in complex, non-stationary
market environments.
This survey has provided a comprehensive, structured synthesis
of this rapidly expanding domain. Through theArchitecture–
Capability–Adaptation (A-C-A)conceptual framework, we
have systematically decoupled:
• Architecture (Part I): The foundational cognitive and
operational building blocks—perception across text, time-
series, and charts; working memory, associative vector
storage, and structured knowledge bases; reactive, reflec-
tive, and strategic reasoning paradigms; and order-routing
action interfaces.
• Capability (Part II): The primary quantitative functions
realized by autonomous agents—symbolic and code-
based alpha discovery, multi-asset portfolio optimization,
and multi-tier pre-trade, in-trade, and post-trade risk
governance.
• Adaptation (Part III): Learning and cross-decision up-
date mechanisms—in-context learning, persistent memory
and reflection that can update decisions without chang-
ing the architecture, supervised fine-tuning, reinforcement
learning, multi-agent coordination and adaptive interac-
tions, and structural self-evolution.
Drawing on185systematically mapped studies from an initial
multi-source ledger and an arXiv extension through 2026-09-30,
our synthesis connects the core cohort of n =80 closed-loop
trading systems with background work on financial models,
tools, and benchmarks.
14.2. Market Microstructure and Practical Implications
The proliferation of autonomous trading agents carries profound
implications for both market dynamics and quantitative practice:
• Market Dynamics and Ecology: As autonomous agents
interact at scale, their collective behaviors will increas-
ingly shape market liquidity, price discovery, and volatil-
ity. Investigating emergent phenomena—such as strategic
crowding, herding around shared LLM foundations, and
algorithmic feedback loops—presents a fertile ground for
synthetic market simulation.
• Quantitative Engineering: In practical asset manage-
ment, agentic architectures provide a principled mecha-
nism to bridge qualitative domain insights (earnings calls,
regulatory filings) with rigorous quantitative optimizers,
transforming quantitative workflow from manual factor
engineering to autonomous research pipelines.
14.3. Empirical Evaluation and Methodological Practices
Empirical evaluation is an important dimension of the architec-
tural landscape. Across the pooled 80-study empirical subset,
39

Table 21:Synthesis of recurring design themes and their evaluation contexts. Representative studies illustrate the mechanisms discussed in the
technical chapters; the final column identifies dimensions for interpreting their implementations and reported results.
Design theme Representative studies Interpretive dimensions
Closed-loop pipelines
and evaluation settings
FinAgent Zhang et al. (2024), TradingAgents Xiao et al.
(2024), FinCon Yu et al. (2024), FinRL-DeepSeek Ben-
henda (2025), Agent Market Arena Qian et al. (2025),
FinMem Yu et al. (2023b); evaluation examples include
OpenPM Cai et al. (2026), CLQT Qu and Chen (2026), and
LiveOption Luo et al. (2026a)
Connect observations, retained state, decisions, and market
feedback; distinguish backtest, simulation, live, and bench-
mark settings.
Action and execution in-
terfaces
FinAgent Zhang et al. (2024), TradingAgents Xiao et al.
(2024), AI-Trader Fan et al. (2025), FinRL-DeepSeek Ben-
henda (2025)
Distinguish target weights from orders, and interpret out-
comes using decision timing, fill rules, and cost assump-
tions.
Memory and adaptation
mechanisms
FinAgent Zhang et al. (2024), FinMem Yu et al. (2023b),
TradingGroup Tian et al. (2025), Alpha2 Xu et al. (2024a)
Separate storage and retrieval from prompt, parameter, and
strategy updates; identify which changes persist across
decisions.
Multi-agent organization TradingAgents Xiao et al. (2024), TradingGroup Tian
et al. (2025), FinCon Yu et al. (2024), REIT multi-agent
pipeline Li (2026)
Specify roles, communication, and decision authority;
role ablations and matched resource budgets help assess
coordination effects.
Evaluation practice and
reproducibility
Primary-subset protocol tables in Section 2 and R0–R3
artifact descriptions
Interpret field coverage within the assembled cohorts,
accounting for retrieval and coding differences; distinguish
artifact availability from trading performance.
reported protocol-field coverage includes time-consistent split
discipline (62.5%), explicit transaction-cost modeling (58.8%),
universe survivorship controls (60.0%), and execution semantics
(58.8%). The cohort breakdown in Table 4 gives the correspond-
ing counts under the different retrieval and coding procedures.
These pooled values summarize the assembled literature; they
do not establish a temporal trend in reporting practices.
The methodological guidelines (MR-1–MR-7) organize prac-
tices that support interpretable comparisons and further valida-
tion. Walk-forward evaluation, realistic execution frictions, and
transparent artifacts help assess generalization, while transfer
to live markets also requires prospective evaluation under the
relevant market and operational conditions.
14.4. Concluding Outlook
Looking forward, the frontier of agentic trading lies at the
intersection of deep neural perception, symbolic reasoning,
and institutional-grade governance. Promising avenues include
architectures that combine neural hypothesis generation with
symbolic reasoning and constraint satisfaction, large-scale agent-
based market sandboxes for systemic risk testing, and verifiable
execution contracts with full cryptographic auditability.
By providing a clear taxonomy, decomposing the end-to-end de-
cision pipeline, and highlighting core methodological principles,
this survey aims to serve as an enduring conceptual roadmap
for researchers, quantitative practitioners, and system architects
shaping the future of autonomous financial intelligence.
14.5. Supplementary Materials and Reproducible Resources
The survey’s conceptual, empirical, and methodological con-
tributions are tied to materials accompanying the manuscript.
Parts I–III present the A-C-A synthesis, with illustrative sys-
tem mappings in Appendix C; the empirical protocol summary
is reported in Supplementary S2; and the methodological rec-
ommendations are stated as MR-1–MR-7 in Section 13. The
supporting review materials are organized as follows:
• Supplementary S1: Search and screening records, includ-
ing the current S0 v2 candidate registry with per-record
decisions.
• Supplementary S2: The current n=80 protocol registry
and coverage summary, alongside a preserved initial-
window v1 evidence-mapping snapshot.
• Supplementary S3: Coding schema and extraction-audit
materials, including a targeted 15-record sample from the
legacy initial-window 41-record primary-role frame and a
record of current amendments to historical codes.
Current per-study codes are recorded in S0 v2, with amendments
documented separately from historical coding snapshots. These
materials make the selection, protocol coding, and version
changes traceable; repository availability is described in the
Data availability statement.
CRediT authorship contribution statement
Yihan Xia: Methodology, Investigation, Data curation, Formal
analysis, Visualization, Writing – original draft, Writing – re-
view & editing. Panpan You: Investigation, Data curation, For-
mal analysis, Visualization, Writing – original draft, Writing –
review & editing. Taotao Wang: Conceptualization, Methodol-
ogy, Supervision, Project administration, Resources, Validation,
Writing – review & editing. Fang Liu: Conceptualization, Vali-
dation, Writing – review & editing. Han Qi: Conceptualization,
Validation, Resources, Writing – review & editing. Xiaoxiao
Wu: Conceptualization, Validation, Writing – review & editing.
40

Shengli Zhang: Conceptualization, Validation, Writing – review
& editing.
Declaration of competing interest
The authors declare that they have no known competing financial
interests or personal relationships that could have appeared to
influence the work reported in this paper.
Acknowledgements
The authors thank colleagues and reviewers whose feedback
helped improve the scope definition, evidence coding, and
presentation of this survey.
Data availability
The registry, protocol tables, and coding materials accompany
the manuscript as Supplementary Materials S1–S3. S1 contains
the combined S0 v2 registry and initial-window search/screening
records. S2 provides the current empirical protocol table and
coverage summary alongside the historical mapping snapshot.
S3 contains the coding schema, historical annotations, current
amendments, and targeted extraction audit. An anonymized
repository containing the same materials and the LaTeX source
will be released upon acceptance, subject to journal policy and
anonymization requirements.
References
Abbade, L.R., Costa, A.H.R., 2026. Realistic market impact
modeling for reinforcement learning trading environments.
arXiv:2603.29086.
Abensur, E., 2024. Machine learning for liquidity classification
and its applications to portfolio selection. Brazilian Review
of Finance/Revista Brasileira de Finanças 22, 1–14. URL:
https://periodicos.fgv.br/rbfin/article/downlo
ad/90713/85865/206675 , doi:10.12660/rbfin.v22n2
.2024.90713.
Albelali, S., Ahmed, M., 2025. Hidden leaks in time series
forecasting: How data leakage affects LSTM evaluation
across configurations and validation strategies. arXiv preprint
arXiv:2512.06932 URL: https://arxiv.org/abs/2512
.06932, doi:10.48550/arXiv.2512.06932.
Aldridge, I., An, J., Burke, R., Cao, M., 2026. Agentic
artificial intelligence in finance: A comprehensive survey.
arXiv:2604.21672.
Alexandrou, G., Pramatari, K., 2026. A multi-agent or-
chestration framework for venture capital due diligence.
arXiv:2605.13110.
Alkhudaydi, M.H., 2025. An ode-based dynamic mean-variance
portfolio optimization. Computational Economics URL:
https://link.springer.com/article/10.1007/s106
14-025-11152-3.
Almgren, R., Chriss, N., 2001. Optimal execution of portfolio
transactions. The Journal of Risk 3, 5–39. URL: https:
//doi.org/10.21314/jor.2001.041 , doi:10.21314/j
or.2001.041.
Almon, B., Caliboso, M., Kim, A., Dutta, R., Raman, R., Srun-
garapu, M., Sharma, V ., Zhu, K., 2025. RAPTOR: Rea-
soned agentic portfolio trading with orchestrated rebalanc-
ing, in: NeurIPS 2025 Workshop (NORA). URL: https:
//openreview.net/forum?id=ziuTkKhgT0.
Araci, D.T., 2019. Finbert: Financial sentiment analysis with pre-
trained language models. arXiv preprint arXiv:1908.10063
URL: https://arxiv.org/abs/1908.10063 , doi:10.4
8550/arXiv.1908.10063.
Arian, H., Norouzi Mobarekeh, D., Seco, L., 2024. Backtest
overfitting in the machine learning era: A comparison
of out-of-sample testing methods in a synthetic controlled
environment. Knowledge-Based Systems 305, 112477. URL:
https://www.sciencedirect.com/science/article/
abs/pii/S0950705124011110 , doi:10.1016/j.knosys
.2024.112477.
Arora, A., Malpani, R., 2026. Predictionmarketbench: A swe-
bench-style framework for backtesting trading agents on
prediction markets. arXiv preprint arXiv:2602.00133 URL:
https://arxiv.org/abs/2602.00133, doi:10.48550/a
rXiv.2602.00133.
Article 29 Working Party, 2018. Guidelines on Automated
individual decision-making and Profiling for the purposes
of Regulation 2016/679. Technical Report. European Data
Protection Board (endorsed). URL: https://ec.europa.
eu/newsroom/article29/items/612053. wP251 rev.01.
Asthana, S., Zhang, B., DeLuca, C., Mahindru, R., Patel, H.,
2025. Stride: A systematic framework for selecting ai
modalities – agentic ai, ai assistants, or llm calls. arXiv
preprint arXiv:2512.02228 URL:https://arxiv.org/ab
s/2512.02228, doi:10.48550/arXiv.2512.02228.
Atkinson, R.C., Shiffrin, R.M., 1968. Human memory: A
proposed system and its control processes, in: Spence,
K.W., Spence, J.T. (Eds.), The Psychology of Learning and
Motivation. Academic Press. volume 2, pp. 89–195. URL:
https://psycnet.apa.org/record/1974-02719-003 ,
doi:10.1016/S0079-7421(08)60422-3.
Baddeley, A.D., Hitch, G., 1974. Working memory. Psychology
of Learning and Motivation 8, 47–89. doi: 10.1016/S007
9-7421(08)60452-1.
Bai, J., Perron, P., 2003. Computation and analysis of multiple
structural change models. Journal of Applied Econometrics
18, 1–22. URL: https://doi.org/10.1002/jae.659 ,
doi:10.1002/jae.659.
Bai, S., Kolter, J.Z., Koltun, V ., 2018. An empirical evaluation
of generic convolutional and recurrent networks for sequence
modeling. arXiv preprint arXiv:1803.01271 URL: https:
//arxiv.org/abs/1803.01271.
41

Bailey, D.H., Borwein, J.M., Lopez de Prado, M., Zhu, Q.J.,
2014. Pseudo-mathematics and financial charlatanism: The
effects of backtest overfitting. SSRN Electronic Journal URL:
https://papers.ssrn.com/sol3/papers.cfm?abstra
ct_id=2326253, doi:10.2139/ssrn.2326253.
Baker, S.R., Bloom, N., Davis, S.J., 2016. Measuring economic
policy uncertainty. The Quarterly Journal of Economics 131,
1593–1636. URL: https://doi.org/10.1093/qje/qjw0
24, doi:10.1093/qje/qjw024.
Barot, R.M., Borkhatariya, A.S., 2026. Polyswarm: A multi-
agent large language model framework for prediction market
trading and latency arbitrage.arXiv:2604.03888.
Basel Committee on Banking Supervision, 2009. Principles for
Sound Stress Testing Practices and Supervision. Technical
Report. Bank for International Settlements. URL: https:
//www.bis.org/publ/bcbs155.htm.
Benhenda, M., 2025. Finrl-deepseek: Llm-infused risk-sensitive
reinforcement learning for trading agents. arXiv preprint
arXiv:2502.07393 URL: https://arxiv.org/abs/2502
.07393, doi:10.48550/arXiv.2502.07393.
Bertsimas, D., Lo, A.W., 1998. Optimal control of execution
costs. Journal of Financial Markets 1, 1–50. URL: ht
tps://doi.org/10.1016/S1386-4181(97)00012-8 ,
doi:10.1016/S1386-4181(97)00012-8.
Black, F., Litterman, R., 1992. Global portfolio optimization.
Financial Analysts Journal 48, 28–43. URL: https://rpc.
cfainstitute.org/en/research/financial-analyst
s-journal/1992/global-portfolio-optimization ,
doi:10.2469/faj.v48.n5.28.
Bohorquez, G., Cartlidge, J., 2024. Simulation of social media-
driven bubble formation in financial markets using an agent-
based model with hierarchical influence network. arXiv
preprint arXiv:2409.00742v1 URL: https://arxiv.or
g/pdf/2409.00742v1.
Bongiorno, C., Manolakis, E., Mantegna, R.N., 2025. End-to-
end large portfolio optimization for variance minimization
with neural networks through covariance cleaning. URL:
https://arxiv.org/abs/2507.01918, doi:10.48550/a
rXiv.2507.01918,arXiv:2507.01918.
Borjigin, A., Stadnyk, I., Bilski, B., Chikita, M., 2026.
Absorbing complexity: An interaction-native knowledge
harness for financial llm agents.arXiv:2606.01886.
Boyd, S., Johansson, R., Kahn, R.N., Schiele, P., Schmelzer,
T., 2024. Markowitz portfolio construction at seventy.
URL: https://arxiv.org/pdf/2401.05080 ,
arXiv:2401.05080.
Briola, A., Bartolucci, S., Aste, T., 2024. Deep limit order
book forecasting: A microstructural guide. arXiv preprint
arXiv:2403.09267 URL: https://arxiv.org/abs/2403
.09267, doi:10.48550/arXiv.2403.09267.
Brown, S.J., Goetzmann, W.N., Ibbotson, R.G., Ross, S.A., 1992.
Survivorship bias in performance studies. The Review of
Financial Studies 5, 553–580. doi:10.1093/rfs/5.4.553.
Brown, T.B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J.D.,
Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G., Askell,
A., Agarwal, S., Herbert-V oss, A., Krueger, G., Henighan,
T., Child, R., Ramesh, A., Ziegler, D.M., Wu, J., Winter,
C., Hesse, C., Chen, M., Sigler, E., Litwin, M., Gray, S.,
Chess, B., Clark, J., Berner, C., McCandlish, S., Radford, A.,
Sutskever, I., Amodei, D., 2020. Language models are few-
shot learners, in: Advances in Neural Information Processing
Systems. URL:https://arxiv.org/abs/2005.14165.
Budish, E., Cramton, P., Shim, J., 2015. The high-frequency
trading arms race: Frequent batch auctions as a market design
response. The Quarterly Journal of Economics 130, 1547–
1621. URL: https://doi.org/10.1093/qje/qjv027 ,
doi:10.1093/qje/qjv027.
Byun, W., 2023. Practical application of deep reinforcement
learning to optimal trade execution. FinTech 2, 414–429.
URL: https://www.mdpi.com/2674-1032/2/3/23 ,
doi:10.3390/fintech2030023.
Cai, X., Guo, M., Liu, J., Han, J., 2026. Openpm: Auditable
point-in-time evaluation for llm portfolio-management agents.
arXiv:2608.09988.
Caner, M., Capponi, A., Sun, N., Tan, J.Y ., 2026. De-
signing agentic ai-based screening for portfolio investment.
arXiv:2603.23300.
Caner, M., Fan, Q., 2024. Portfolio analysis in high dimensions
with tracking error and weight constraints. URL: https:
//arxiv.org/abs/2402.17523,arXiv:2402.17523.
Cao, Y ., Zhang, H., Keung, J.W., Chen, Y ., 2026.
Systradebench: An iterative build-test-patch benchmark for
strategy-to-code trading systems with drift-aware diagnostics.
arXiv:2604.04812.
Caruana, R., 1997. Multitask learning. Machine Learning 28,
41–75. doi:10.1023/A:1007379606734.
Casas, P.F.i., Montero, A.M., 2026. Conceptualization and
experimentation of asset market with price manipulation.
arXiv:2609.13304.
Castelli, A., Giudici, P., Piergallini, A., 2025. Building crypto
portfolios with agentic ai. arXiv preprint arXiv:2507.20468v1
URL:https://arxiv.org/pdf/2507.20468v1.
Chai, J., Zheng, B., Liu, X., Lu, H., 2026. Agentic time
machine as an infrastructure for future-event forecasting.
arXiv:2606.21013.
Chang, S., Zhu, P., Chen, Y ., 2026. Valueblindbench:
Agreement-gated stress testing of llm-judged investment ra-
tionales before returns are observable.arXiv:2604.25224.
42

Chen, D., Zhu, Y ., Liu, M., Li, J., 2022. Cost-efficient rein-
forcement learning for optimal trade execution on dynamic
market environment, in: Proceedings of the ACM Interna-
tional Conference on AI in Finance (ICAIF). URL: https:
//dl.acm.org/doi/10.1145/3533271.3561761 ,
doi:10.1145/3533271.3561761.
Chen, J., Cong, S.L., 2025. Agentguard: Repurposing agentic
orchestrator for safety evaluation of tool orchestration. arXiv
preprint arXiv:2502.09809v1 URL:https://arxiv.org/
pdf/2502.09809v1.
Chen, J., Feng, A., Verma, H., Gu, S., 2026a. Reasoning
through verifiable forecast actions: Consistency-grounded
rl for financial llms.arXiv:2605.21975.
Chen, X., Zhu, W., Zheng, S., Rasul, K., 2026b. Sharp: A self-
evolving human-auditable rubric policy for financial trading
agents.arXiv:2605.06822.
Chen, Y ., 2026a. Be water: An evolutionary proof for trend-
following.arXiv:2603.29593.
Chen, Y ., Yao, Z., Liu, Y ., Xin, A., Ye, J., Yu, J., Hou, L., Li, J.,
2025. Stockbench: Can LLM agents trade stocks profitably in
real-world markets? arXiv preprint arXiv:2510.02209 URL:
https://arxiv.org/abs/2510.02209, doi:10.48550/a
rXiv.2510.02209.
Chen, Z., 2026b. Decomposing financial market dynamics via
mechanism analysis in an evolutionary multi-agent simulation.
arXiv:2606.23158.
Cheng, L., Cheng, X., Liu, S., Oosterlee, C.W., 2026a. Ridge:
An autonomous framework for validation and method discov-
ery in llm-generated option pricing.arXiv:2607.25199.
Cheng, Z., Lai, L., Liu, Y ., 2026b. Sustainable hybrid document-
routed retrieval for financial rag: Resolving the robustness-
precision trade-off.arXiv:2603.26815.
Cheridito, P., Weiss, M., 2025. Reinforcement learning for
trade execution with market and limit orders. arXiv preprint
arXiv:2507.06345 URL: https://arxiv.org/abs/2507
.06345, doi:10.48550/arXiv.2507.06345.
Constantinides, G.M., 1986. Capital market equilibrium with
transaction costs. Journal of Political Economy 94, 842–
862. URL: https://doi.org/10.1086/261412 ,
doi:10.1086/261412.
Cook, T., Osuagwu, R., Tsatiashvili, L., Vrynsia, V ., Ghosal,
K., Masoud, M., Mattivi, R., 2025. Retrieval augmented
generation (rag) for fintech: Agentic design and evaluation.
arXiv preprint arXiv:2510.25518 URL:https://arxiv.or
g/abs/2510.25518, doi:10.48550/arXiv.2510.25518.
Coriat, B., Benhamou, E., 2025. Harlf: Hierarchical rein-
forcement learning and lightweight llm-driven sentiment in-
tegration for financial portfolio optimization. URL: https:
//arxiv.org/abs/2507.18560,arXiv:2507.18560.
Cosler, M., Hahn, C., Mendoza, D., Schmitt, F., Trippel, C.,
2023. nl2spec: Interactively translating unstructured natural
language to temporal logics with large language models,
in: Computer Aided Verification (CA V 2023), pp. 383–
396. URL: https://arxiv.org/abs/2303.04864 ,
doi:10.1007/978-3-031-37703-7_18.
Davis, M.H.A., Norman, A.R., 1990. Portfolio selection with
transaction costs. Mathematics of Operations Research 15,
676–713. URL: https://doi.org/10.1287/moor.15.4.
676, doi:10.1287/moor.15.4.676.
Deng, K., 2025. Autoquant: An auditable expert-system frame-
work for execution-constrained auto-tuning in cryptocurrency
perpetual futures. arXiv preprint arXiv:2512.22476 URL:
https://arxiv.org/abs/2512.22476, doi:10.48550/a
rXiv.2512.22476.
Deng, K., Cai, H., Lu, J., Qian, C.Z., 2026. From search to
research: Exploring search scaling in autonomous quantitative
factor mining.arXiv:2609.35559.
Dettmers, T., Pagnoni, A., Holtzman, A., Zettlemoyer, L., 2023.
Qlora: Efficient finetuning of quantized llms URL: https:
//arxiv.org/abs/2305.14314,arXiv:2305.14314.
Diau, E., 2025. Finance as extended biology: Reciprocity as
the cognitive substrate of financial behavior. arXiv preprint
arXiv:2506.00099v2 URL: https://arxiv.org/pdf/25
06.00099v2.
Dicks, M., Paskaramoorthy, A., Gebbie, T., 2023. Many learning
agents interacting with an agent-based market model. arXiv
preprint arXiv:2303.07393v4 URL:https://arxiv.org/
pdf/2303.07393v4.
Ding, H., Li, Y ., Wang, J., Chen, H., 2024. Large language
model agent in financial trading: A survey. arXiv preprint
arXiv:2408.06361 URL: https://arxiv.org/abs/2408
.06361, doi:10.48550/arXiv.2408.06361.
Dong, Y ., Wu, F., Zhang, K., Dai, Y ., Zhang, S., Ye, W.,
Chen, S., Cheng, Z.Q., 2025. Large language model agents
in finance: A survey bridging research, practice, and real-
world deployment, in: Findings of the Association for
Computational Linguistics: EMNLP 2025, Association for
Computational Linguistics, Suzhou, China. pp. 17889–17907.
URL: https://aclanthology.org/2025.findings-e
mnlp.972/, doi:10.18653/v1/2025.findings-emnlp.9
72.
Dorovatas, V ., Schwerin, M., Bagdanov, A.D., Caccia, L., Carta,
A., Charlin, L., Hammer, B., Hayes, T.L., Hess, T., Kanan,
C., Kudithipudi, D., Liu, X., Lomonaco, V ., Mendez-Mendez,
J., Patil, D., Prabhu, A., Ricci, E., Tuytelaars, T., van de
Ven, G.M., Wang, L., van de Weijer, J., Choi, J., Mundt,
M., Aljundi, R., 2026. Modular memory is the key to
continual learning agents. arXiv preprint arXiv:2603.01761
URL: https://arxiv.org/abs/2603.01761 , doi:10.4
8550/arXiv.2603.01761.
43

Du, K., Xing, F., Mao, R., Cambria, E., 2024. Financial
sentiment analysis: Techniques and applications. ACM
Computing Surveys 56, 1–42. doi:10.1145/3649451.
Duan, Q., Li, C., Wang, C., Zhang, F., 2026. Can agentic trading
systems pay for their own intelligence? arXiv:2607.10286.
Duan, Y ., Zhang, C., Li, J., 2025. Factormad: A multi-
agent debate framework based on large language models for
interpretable stock alpha factor mining, in: Proceedings of the
6th ACM International Conference on AI in Finance. URL:
https://dl.acm.org/doi/10.1145/3768292.37703
77.
Easley, D., López de Prado, M., O’Hara, M., 2012. Flow toxicity
and liquidity in a high-frequency world. The Review of
Financial Studies 25, 1457–1493. URL: https://doi.
org/10.1093/rfs/hhs053, doi:10.1093/rfs/hhs053.
European Parliament, Council of the European Union, 2014.
Directive 2014/65/EU of the European Parliament and of
the Council of 15 May 2014 on markets in financial instru-
ments and amending Directive 2002/92/EC and Directive
2011/61/EU (consolidated text). Technical Report. Official
Journal of the European Union. URL: https://eur-lex
.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A0
2014L0065-20240328 . consolidated version available on
EUR-Lex.
European Parliament, Council of the European Union, 2016.
Regulation (EU) 2016/679 of the European Parliament and
of the Council of 27 April 2016 on the protection of natural
persons with regard to the processing of personal data and on
the free movement of such data (General Data Protection
Regulation). Technical Report. Official Journal of the
European Union. URL: https://eur-lex.europa.eu
/legal-content/EN/TXT/?uri=CELEX%3A32016R0679.
Fama, E.F., French, K.R., 1993. Common risk factors in the
returns on stocks and bonds. Journal of Financial Economics
33, 3–56. URL: https://doi.org/10.1016/0304-405
X(93)90023-5, doi:10.1016/0304-405X(93)90023-5.
Fan, T., Yang, Y ., Jiang, Y ., Zhang, Y ., Chen, Y ., Huang, C.,
2025. Ai-trader: Benchmarking autonomous agents in real-
time financial markets. arXiv preprint arXiv:2512.10971 URL:
https://arxiv.org/abs/2512.10971, doi:10.48550/a
rXiv.2512.10971.
Fatemi, S., Hu, Y ., 2024. Finvision: A multi-agent framework
for stock market prediction, in: Proceedings of the 5th ACM
International Conference on AI in Finance (ICAIF ’24), pp.
582–590. URL: https://dl.acm.org/doi/10.1145/3
677052.3698688, doi:10.1145/3677052.3698688.
Finn, C., Abbeel, P., Levine, S., 2017. Model-agnostic meta-
learning for fast adaptation of deep networks, in: International
Conference on Machine Learning (ICML), pp. 1126–1135.
URL:https://arxiv.org/abs/1703.03400.
Fonseca, X., 2026. Look-ahead-freedom as temporal non-
interference: A verifiable correctness property for backtesting
and agentic trading pipelines.arXiv:2607.04958.
Foucault, T., 1999. Order flow composition and trading costs in
a dynamic limit order market. Journal of Financial Markets 2,
99–134. URL: https://doi.org/10.1016/S1386-418
1(98)00012-3, doi:10.1016/S1386-4181(98)00012-3.
Gao, K., Vytelingum, P., Weston, S., Luk, W., Guo, C., 2022.
Understanding intra-day price formation process by agent-
based financial market simulation: calibrating the extended
chiarella model. arXiv preprint arXiv:2208.14207v1 URL:
https://arxiv.org/pdf/2208.14207v1.
Geifman, Y ., El-Yaniv, R., 2017. Selective classification for
deep neural networks. URL: https://arxiv.org/abs/17
05.08500,arXiv:1705.08500.
Genet, R., 2025. Deep learning for vwap execution in
crypto markets: Beyond the volume curve. arXiv preprint
arXiv:2502.13722 URL: https://arxiv.org/abs/2502
.13722, doi:10.48550/arXiv.2502.13722.
Giglio, S., Kelly, B., Xiu, D., 2022. Factor models, machine
learning, and asset pricing. Annual Review of Financial
Economics 14, 337–368. URL: https://www.annual
reviews.org/doi/full/10.1146/annurev-financial
-101521-104735 , doi:10.1146/annurev-financial-1
01521-104735.
Glosten, L.R., Milgrom, P.R., 1985. Bid, ask and transaction
prices in a specialist market with heterogeneously informed
traders. Journal of Financial Economics 14, 71–100. URL:
https://doi.org/10.1016/0304-405X(85)90044-3 ,
doi:10.1016/0304-405X(85)90044-3.
Go, E., Deb, R., Banerjee, A., 2026. Plan before you
trade: Inference-time optimization for rl trading agents.
arXiv:2605.12653.
Gong, J., Jiang, M., Liu, Z., Qiao, Y ., 2026. Shijianbench: From
dialogue to decision for long-horizon evaluation of investment
advisors.arXiv:2608.01204.
Gould, M.D., Porter, M.A., Williams, S., McDonald, M., Fenn,
D.J., Howison, S.D., 2013. Limit order books. Quantitative
Finance 13, 1709–1742. URL: https://doi.org/10.108
0/14697688.2013.803148, doi:10.1080/14697688.201
3.803148.
Granger, C.W.J., 1969. Investigating causal relations by econo-
metric models and cross-spectral methods. Econometrica 37,
424–438. URL: https://www.jstor.org/stable/191
2791, doi:10.2307/1912791.
Grinold, R.C., Kahn, R.N., 2000. Active Portfolio Management:
A Quantitative Approach for Producing Superior Returns and
Controlling Risk. McGraw-Hill. URL: https://www.mhed
ucation.com/highered/product/active-portfolio
-management-grinold-kahn/M9780070248820.html.
44

Hafsi, Y ., Vittori, E., 2024. Optimal execution with rein-
forcement learning. arXiv preprint arXiv:2411.06389 URL:
https://arxiv.org/pdf/2411.06389, doi:10.48550/a
rXiv.2411.06389.
Hamilton, J.D., 1989. A new approach to the economic
analysis of nonstationary time series and the business cycle.
Econometrica 57, 357–384. URL: https://www.jstor.or
g/stable/1912559, doi:10.2307/1912559.
Hansen, P.R., 2005. A test for superior predictive ability.
Journal of Business & Economic Statistics 23, 365–380.
doi:10.1198/073500105000000063.
Hashimoto, R., Takata, R., Suzuki, M., Tanaka, Y .,
2026. Financial market as a self-organized ecosystem:
Simulation via learning with heterogeneous preferences.
arXiv:2604.23975.
Hashimoto, R., Takayanagi, T., Suzuki, M., Izumi, K., 2025.
Agent-based simulation of a financial market with large
language models. Proceedings of the International Conference
on Principles and Practice of Multi-Agent Systems (PRIMA)
URL: https://arxiv.org/abs/2510.12189 , doi:10.4
8550/arXiv.2510.12189.
Hinton, G.E., Salakhutdinov, R.R., 2006. Reducing the
dimensionality of data with neural networks. Science 313,
504–507. URL: https://doi.org/10.1126/science.
1127647, doi:10.1126/science.1127647.
Hogan, B.R., Chen, X., Wilson, J.T., Rasul, K., 2026. Alpha-
lab: Autonomous multi-agent research across optimization
domains with frontier llms.arXiv:2604.08590.
Hong, S., Zhuge, M., Chen, J., Zheng, X., Cheng, Y ., Zhang,
C., Wang, J., Wang, Z., Yau, S.K.S., Lin, Z., Zhou, L.,
Ran, C., Xiao, L., Wu, C., Schmidhuber, J., 2024. Metagpt:
Meta programming for a multi-agent collaborative framework,
in: International Conference on Learning Representations
(ICLR). URL: https://arxiv.org/abs/2308.00352 ,
doi:10.48550/arXiv.2308.00352.
Hu, X., Xiong, Y ., Zhang, Z., Li, C., 2024. Consensus
of a new multi-agent system via multi-task, multi-control
mechanism and multi-consensus strategy. Neurocomputing
doi:10.1016/j.neucom.2024.127586.
Huang, C., Qiao, Y ., Zhang, R., Ye, J., 2026a. Fintoolsyn: A
forward synthesis framework for financial tool-use dialogue
data with dynamic tool retrieval.arXiv:2603.24051.
Huang, J., Alrassan, A., Harischandra, D., Wu, T., 2026b. Multi-
agent debate for explainable trading: Reasoning, consensus,
and performance in simulated markets. arXiv:2609.29701.
Huang, W., Yu, Z., 2026. Strat-llm: Stratified strategy
alignment for llm-based stock trading with real-time multi-
source signals.arXiv:2605.06024.
Huang, Y ., Fan, Z., Hu, K., Ye, Y ., 2026c. From hypotheses to
factors: Constrained llm agents in cryptocurrency markets.
arXiv:2604.26747.
Hwang, Y ., Kong, Y ., Zohren, S., Lee, Y ., 2025. Decision-
informed neural networks with large language model integra-
tion for portfolio optimization. URL: https://arxiv.org/
pdf/2502.00828,arXiv:2502.00828.
Iacovides, G., Konstantinidis, T., Xu, M., Mandic, D., 2024.
Finllama: Llm-based financial sentiment analysis for algo-
rithmic trading, in: Proceedings of the 5th ACM Interna-
tional Conference on AI in Finance, ACM. pp. 134–141.
doi:10.1145/3677052.3698696.
Jagannathan, R., Ma, T., 2003. Risk reduction in large portfolios:
Why imposing the wrong constraints helps. The Journal of
Finance 58, 1651–1684. URL: https://doi.org/10.111
1/1540-6261.00580, doi:10.1111/1540-6261.00580.
Jeon, J., Lee, H., 2026. Can blindfolded llms still trade?
an anonymization-first framework for portfolio optimization.
arXiv:2603.17692.
Jia, C., Luo, Y ., Han, S., Li, P., 2026. Evonash-marl: A
closed-loop multi-agent reinforcement learning framework
for medium-horizon equity allocation.arXiv:2604.10911.
Jiang, J., Zhou, K., Zhao, W.X., Song, Y ., Zhu, C., Zhu,
H., Wen, J.R., 2024. Kg-agent: An efficient autonomous
agent framework for complex reasoning over knowledge
graph. arXiv preprint arXiv:2402.11163v1 URL: https:
//arxiv.org/pdf/2402.11163v1.
Johnson, J., Douze, M., Jégou, H., 2017. Billion-scale similarity
search with GPUs. arXiv preprint arXiv:1702.08734 URL:
https://arxiv.org/abs/1702.08734.
Kahneman, D., Tversky, A., 1979. Prospect theory: An
analysis of decision under risk. Econometrica 47, 263–291.
URL: https://www.jstor.org/stable/1914185 ,
doi:10.2307/1914185.
Kang, Z., Gong, J., Hu, W., Yin, S., Jiang, K., Fang, Z., He,
Y ., Meng, C., Fu, R., Chen, D., Zheng, L., Jiang, E.H., Feng,
Y ., Leng, Y ., Zhu, J., Chen, X., Yang, X., Xuan, R., 2026.
Quanteval: A benchmark for financial quantitative tasks in
large language models. arXiv preprint arXiv:2601.08689
URL: https://arxiv.org/abs/2601.08689 , doi:10.4
8550/arXiv.2601.08689.
Kargarzadeh, A., Khaledian, N., Parvini, N., Khaledian, A.,
2026. Large language model-driven small-capitalization
trading: Integrating financial news sentiment, macroeconomic
indicators, and technical signals.arXiv:2608.12283.
Kato, M., 2026. Ai economist agent: An agentic frame-
work for evidence-based economic and financial analysis
with rag, knowledge graphs, and large language models.
arXiv:2606.20041.
45

Kelly, J.L., 1956. A new interpretation of information rate.
Bell System Technical Journal 35, 917–926. URL: https:
//onlinelibrary.wiley.com/doi/10.1002/j.1538-7
305.1956.tb03809.x, doi:10.1002/j.1538-7305.1956
.tb03809.x.
Khatchadourian, R., 2026. Replayable financial agents: A
determinism-faithfulness assurance harness for tool-using llm
agents. arXiv preprint arXiv:2601.15322v2 URL: https:
//arxiv.org/pdf/2601.15322v2.
Khezresmaeilzadeh, T., Razmara, P., Azizi, S., Sadeghi, M.E.,
Potraghloo, E.B., 2025. Vista: Vision-language inference
for training-free stock time-series analysis. arXiv preprint
arXiv:2505.18570 doi:10.48550/arXiv.2505.18570.
Kim, H., Kim, M., Jung, S., Pyo, S., 2026a. Favor: Llm-based
agentic framework for factor mining via empirical validation.
arXiv:2608.30192.
Kim, S., Choi, Y ., Kang, M., Hwang, S.J., 2026b. Evolvetrade:
Experience-driven policy refinement for self-evolving llm
trading agents.arXiv:2609.17632.
Kirilenko, A.A., Kyle, A.S., Samadi, M., Tuzun, T., 2017. The
flash crash: High-frequency trading in an electronic market.
The Journal of Finance 72, 967–998. URL: https://doi.
org/10.1111/jofi.12498, doi:10.1111/jofi.12498.
Kirkpatrick, J., Pascanu, R., Rabinowitz, N., Veness, J., Hadsell,
R., 2017. Overcoming catastrophic forgetting using elastic
weight consolidation. Proceedings of the National Academy
of Sciences (PNAS) 114, 3521–3526. URL: https://
www.pnas.org/doi/10.1073/pnas.1611835114 ,
doi:10.1073/pnas.1611835114.
Kirtac, K., Germano, G., 2025. Leveraging llm-based sentiment
analysis for portfolio optimization with proximal policy
optimization, in: Proceedings of the 1st Workshop for
Research on Agent Language Models (REALM 2025). URL:
https://aclanthology.org/2025.realm-1.12/.
Kocsis, L., Szepesvári, C., 2006. Bandit based monte-carlo
planning, in: Machine Learning: ECML 2006, pp. 282–
293. URL: https://doi.org/10.1007/11871842_29 ,
doi:10.1007/11871842_29.
Kolonin, A., Glushchenko, A., Bochkov, E., Saxena, A., 2026.
Time series augmented generation for financial applications.
arXiv:2604.19633.
Kou, Z., Yu, H., Luo, J., Peng, J., Li, X., Liu, C., Dai, J., Chen,
L., Han, S., Guo, Y ., 2025. Automate strategy finding with
llm in quant investment, in: Findings of the Association for
Computational Linguistics: EMNLP 2025, Suzhou, China.
URL: https://aclanthology.org/2025.findings-e
mnlp.1005.pdf.
Kvasiuk, Y ., Li, T., Colegrove, O., Münchmeyer, M., 2026.
Madevolve: Evolutionary optimization of trading systems
with large language models.arXiv:2605.23007.
Kyle, A.S., 1985. Continuous auctions and insider trading.
Econometrica 53, 1315–1335. URL: https://www.jstor.
org/stable/1913210, doi:10.2307/1913210.
Lau, E., Dücker, M., Chaudhary, R., Goh, H.W., 2026. Banker-
toolbench: Evaluating ai agents in end-to-end investment
banking workflows.arXiv:2604.11304.
Ledoit, O., Wolf, M., 2004. Honey, i shrunk the sample
covariance matrix. The Journal of Portfolio Management
30, 110–119. URL: https://doi.org/10.3905/jpm.20
04.110, doi:10.3905/jpm.2004.110.
Lee, H., Park, S., Lee, S., Seo, J., 2026. When summaries distort
decisions: Information fidelity in llm-compressed financial
analysis.arXiv:2606.29251.
Lee, Y ., Kim, Y ., Kim, J., Kim, S., Lee, Y ., 2025. Llm-enhanced
black-litterman portfolio optimization. URL: https://arxi
v.org/abs/2504.14345, doi:10.48550/arXiv.2504.14
345,arXiv:2504.14345.
Letteri, I., 2026. Agenticaita: A proof-of-concept about
deliberative multi-agent reasoning for autonomous trading
systems.arXiv:2605.12532.
Li, C., Ma, P., Duan, Q., Lin, Z., 2026a. Nextfund: A
unified performance tracking platform for agentic portfolio
management.arXiv:2607.11141.
Li, H., Cao, Y ., Yu, Y ., Javaji, S.R., Deng, Z., He, Y ., Jiang,
Y ., Zhu, Z., Subbalakshmi, K.P., Xiong, G., Huang, J., Qian,
L., Peng, X., Xie, Q., Suchow, J.W., 2025. Investorbench:
A benchmark for financial decision-making tasks with llm-
based agent, in: Proceedings of the 63rd Annual Meeting
of the Association for Computational Linguistics (V olume 1:
Long Papers), pp. 2509–2525. URL: https://aclantholo
gy.org/2025.acl-long.126/ , doi:10.18653/v1/2025
.acl-long.126.
Li, J., Liu, Y ., Liu, W., Fang, S., Wang, L., Xu, C., Bian,
J., 2024a. Mars: a financial market simulation engine
powered by generative foundation model. arXiv preprint
arXiv:2409.07486 URL: https://arxiv.org/abs/2409
.07486, doi:10.48550/arXiv.2409.07486.
Li, M., Gonsalves, R., Li, W., Yoon, S., 2026b. Trusttrade:
Human-inspired selective consensus reduces decision uncer-
tainty in llm trading agents.arXiv:2603.22567.
Li, N., Laryea, A., Ihlamur, Y ., 2026c. Optimal stop-loss and
take-profit parameterization for autonomous trading agent
swarm.arXiv:2604.27150.
Li, S., Zhang, J., Yao, R., Qiu, W., 2026d. Evermine: Dissecting
the self-evolution of research capabilities in long-horizon
alpha research.arXiv:2609.33524.
46

Li, Y ., Du, N., Song, X., Yang, X., Cui, T., Xue, N., Farjudian,
A., Ren, J., Cheah, W.P., 2024b. Cardinality and bounding
constrained portfolio optimization using safe reinforcement
learning, in: Proceedings of the International Joint Conference
on Neural Networks (IJCNN). URL: https://doi.org/10
.1109/IJCNN60899.2024.10651491, doi:10.1109/IJCN
N60899.2024.10651491.
Li, Y ., Liu, S., Liu, B., 2026e. Ai trading’s alpha singularity:
Emergent market reasoning through agent-to-agent self-
evolution.arXiv:2606.29194.
Li, Y ., Liu, S., Liu, B., 2026f. Pandaai: A practical agent cq2 for
neuro-symbolic data analysis and integrated decision-making
in quantitative finance.arXiv:2606.06823.
Li, Y ., Liu, S., Liu, B., 2026g. Vst: Verifiable struc-
tured transport for auditable agent-to-agent alpha discovery.
arXiv:2609.07065.
Li, Y ., Luo, B., Wang, Q., Chen, N., Liu, X., He, B., 2024c.
CryptoTrade: A reflective LLM-based agent to guide zero-
shot cryptocurrency trading, in: Al-Onaizan, Y ., Bansal,
M., Chen, Y .N. (Eds.), Proceedings of the 2024 Conference
on Empirical Methods in Natural Language Processing,
Association for Computational Linguistics, Miami, Florida,
USA. pp. 1094–1106. URL: https://aclanthology.org
/2024.emnlp-main.63/, doi:10.18653/v1/2024.emnlp
-main.63.
Li, Y ., Yu, Y ., Li, H., Chen, Z., Khashanah, K., 2023.
Tradinggpt: Multi-agent system with layered memory and
distinct characters for enhanced financial trading performance.
URL: https://arxiv.org/pdf/2309.03736 , doi:10.4
8550/arXiv.2309.03736,arXiv:2309.03736.
Li, Z., 2026. Design and empirical study of a large language
model-based multi-agent investment system for chinese public
reits. arXiv preprint arXiv:2602.00082 URL: https://arxi
v.org/abs/2602.00082, doi:10.48550/arXiv.2602.00
082.
Li, Z., Li, Y ., Guo, Y ., Zhang, M., 2026h. Autoscientist-
quant: Self-evolving coding agents for automatic research
in quantitative investment.arXiv:2608.28632.
Lin, L.J., 1992. Self-improving reactive agents based on
reinforcement learning, planning and teaching. Machine
Learning 8, 293–321. URL: https://doi.org/10.1023/
A:1022628806385, doi:10.1023/A:1022628806385.
Liu, B., Dang, R., 2025a. Finpos: A position-aware trading
agent system for real financial markets. URL: https:
//arxiv.org/abs/2510.27251,arXiv:2510.27251.
Liu, B., Dang, R., 2025b. Finrs: A risk-sensitive trad-
ing framework for real financial markets. arXiv preprint
arXiv:2511.12599v1 URL: https://arxiv.org/pdf/25
11.12599v1.
Liu, F., Chen, L., Zheng, Y ., Feng, Y ., 2022a. A prediction
method with data leakage suppression for time series. Elec-
tronics 11, 3701. URL: https://www.mdpi.com/2079-9
292/11/22/3701, doi:10.3390/electronics11223701.
Liu, F., Fu, Y ., Wang, Y ., Liu, Q., 2026. Xalpha: A memory-
driven ai quant researcher for hypothesis-to-code alpha
discovery.arXiv:2607.08332.
Liu, F., Yi, H., Luo, S., Wang, Y ., Yang, Y ., Li, X., Hu, Z.,
Feng, J., Liu, Q., 2025. Cognitive alpha mining via llm-driven
code-based evolution. arXiv preprint arXiv:2511.18850 URL:
https://arxiv.org/html/2511.18850v1.
Liu, N.F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M.,
Petroni, F., Liang, P., 2024. Lost in the middle: How language
models use long contexts. Transactions of the Association for
Computational Linguistics URL:https://arxiv.org/ab
s/2307.03172, doi:10.1162/tacl_a_00638.
Liu, X.Y ., Xia, Z., Rui, J., Gao, J., Yang, H., Zhu, M., Wang,
C.D., Wang, Z., Guo, J., 2022b. Finrl-meta: Market environ-
ments and benchmarks for data-driven financial reinforcement
learning. URL: https://arxiv.org/abs/2211.03107 ,
arXiv:2211.03107.
Liu, X.Y ., Yang, H., Chen, Q., Zhang, R., Yang, L., Xiao,
B., Wang, C.D., 2020. Finrl: A deep reinforcement
learning library for automated stock trading in quantitative
finance. URL: https://arxiv.org/abs/2011.09607 ,
arXiv:2011.09607.
Liu, Z., Zhang, Y ., Li, P., Liu, Y ., Yang, D., 2023. A dynamic llm-
powered agent network for task-oriented agent collaboration.
arXiv preprint arXiv:2310.02170 URL:https://arxiv.or
g/abs/2310.02170.
Lo, A.W., Repin, D.V ., 2002. The psychophysiology of real-time
financial risk processing. Journal of Cognitive Neuroscience
14, 323–339. URL: https://doi.org/10.1162/089892
902317361921, doi:10.1162/089892902317361921.
Lopez-Lira, A., 2025. Can large language models trade? testing
financial theories with llm agents in market simulations. arXiv
preprint arXiv:2504.10789 URL:https://arxiv.org/ab
s/2504.10789, doi:10.48550/arXiv.2504.10789.
Lu, J., Wang, K., Wang, Y ., Tang, Q., Zeng, H., Chen, X.,
Pi, J., Deng, S., Chen, L., Fu, Y ., Yang, K., Sun, X.,
2026. Fintoolbench: Evaluating llm agents for real-world
financial tool use. arXiv preprint arXiv:2603.08262v1 URL:
https://arxiv.org/pdf/2603.08262v1.
Luan, B., Sun, R., Wang, S., Gu, Y ., 2026. Finresearch-
bench ii: A deep research benchmark with consensus-
derived gold rubrics for distinguishing financial report quality.
arXiv:2607.12252.
Lundberg, S.M., Lee, S.I., 2017. A unified approach to
interpreting model predictions, in: Advances in Neural
Information Processing Systems (NeurIPS). URL: https:
//arxiv.org/abs/1705.07874.
47

Luo, H., Li, Y ., An, B.M., Luo, X., 2026a. Liveoption:
Evaluating llm agents in structured option trading with
nonlinear payoffs.arXiv:2609.33470.
Luo, H., Zhang, Y ., Liu, C., 2025. Efs: Evolutionary
factor searching for sparse portfolio optimization using large
language models. arXiv preprint arXiv:2507.17211 URL:
https://arxiv.org/abs/2507.17211, doi:10.48550/a
rXiv.2507.17211.
Luo, X., Hong, C., Li, H., Xie, Y ., 2026b. Foresight-9:
Prospective and process-aware evaluation of adaptive trading
agents.arXiv:2608.29372.
MacLean, L.C., Thorp, E.O., Ziemba, W.T., 2011. The Kelly
Capital Growth Investment Criterion: Theory and Practice.
World Scientific. URL: https://doi.org/10.1142/7598,
doi:10.1142/7598.
Madaan, A., Tandon, N., Gupta, P., Hallinan, S., Gao,
L., Wiegreffe, S., Alon, U., Dziri, N., Prabhumoye, S.,
Yang, Y ., 2023. Self-refine: Iterative refinement with self-
feedback. URL: https://arxiv.org/abs/2303.17651 ,
arXiv:2303.17651.
Malkov, Y .A., Yashunin, D.A., 2020. Efficient and robust ap-
proximate nearest neighbor search using hierarchical nav-
igable small world graphs. IEEE Transactions on Pattern
Analysis and Machine Intelligence 42, 824–836. URL:
https://doi.org/10.1109/TPAMI.2018.2889473 ,
doi:10.1109/TPAMI.2018.2889473.
Markowitz, H., 1952. Portfolio selection. Journal of Finance 7,
77–91. URL: https://www.jstor.org/stable/29759
74, doi:10.2307/2975974.
McClelland, J.L., McNaughton, B.L., O’Reilly, R.C., 1995. Why
there are complementary learning systems in the hippocampus
and neocortex: Insights from the successes and failures of
connectionist models of learning and memory. Psychological
Review 102, 419–457. URL: https://doi.org/10.103
7/0033-295X.102.3.419 , doi:10.1037/0033-295X.10
2.3.419.
Muandet, K., Balduzzi, D., Schölkopf, B., 2013. Domain gener-
alization via invariant feature representation, in: Proceedings
of the 30th International Conference on Machine Learning
(ICML), pp. 10–18. URL: https://proceedings.mlr.pr
ess/v28/muandet13.html.
Nechepurenko, M., Shuvalov, P., 2026. Foresight arena: An
on-chain benchmark for evaluating ai forecasting agents.
arXiv:2605.00420.
Ng, C.C., Lim, J.Y ., Low, W.Z., 2025. Prism: Prompt-refined
in-context system modelling for financial retrieval. arXiv
preprint arXiv:2511.14130 URL:https://arxiv.org/ab
s/2511.14130, doi:10.48550/arXiv.2511.14130.
Nguyen, P., Pham, T., 2026. Toward reliable evaluation of llm-
based financial multi-agent systems: Taxonomy, coordination
primacy, and cost awareness.arXiv:2603.27539.
Nguyen, T., 2025. Sharpe-driven stock selection and liquidity-
constrained portfolio optimization. URL: https://arxiv.
org/pdf/2511.13251,arXiv:2511.13251.
Nie, X., Guo, Z., Chen, Y ., Zhou, Y ., Zhang, W.,
2026. Awcp: A workspace delegation protocol for deep-
engagement collaboration across remote agents. arXiv
preprint arXiv:2602.20493v1 URL: https://arxiv.or
g/pdf/2602.20493v1.
Nitarach, N., Sirichotedumrong, W., Pitchayarthorn, P., Taveek-
itworachai, P., Manakul, P., Pipatanakul, K., 2025. Fin-
cot: Grounding chain-of-thought in expert financial reason-
ing, in: Proceedings of the 10th Workshop on Financial
Technology and Natural Language Processing (FinNLP) at
EMNLP. URL: https://arxiv.org/abs/2506.16123 ,
doi:10.48550/arXiv.2506.16123 . accepted at FinNLP
2025 (EMNLP).
Ntale, G., 2026. Ai trading: Evaluating large language models
for technical market analysis.arXiv:2607.15414.
Olby, O., Bacalum, A., Baggott, R., Stillman, N., 2025. Right
place, right time: Market simulation-based rl for execution
optimisation, in: Proceedings of ICAIF 2025. URL: https:
//arxiv.org/abs/2510.22206, doi:10.48550/arXiv.2
510.22206.
Oliva, C., Ventura, P.R., Lago-Fernández, L.F., 2025. Multi-
objective portfolio optimization via gradient descent. URL:
https://arxiv.org/html/2507.16717v1 ,
arXiv:2507.16717.
Oort, C.M.V ., Ratliff-Crain, E., Tivnan, B.F., Wshah, S., 2023.
Adaptive agents and data quality in agent-based financial
markets. arXiv preprint arXiv:2311.15974v1 URL: https:
//arxiv.org/pdf/2311.15974v1.
Ouyang, S., Sui, P., 2026. Dissecting ai trading: Behavioral
finance and market bubbles.arXiv:2604.18373.
Packer, C., Wooders, S., Lin, K., Fang, V ., Patil, S.G., Stoica,
I., Gonzalez, J.E., 2023. Memgpt: Towards llms as operating
systems. arXiv preprint arXiv:2310.08560 URL: https:
//arxiv.org/abs/2310.08560, doi:10.48550/arXiv.2
310.08560.
Pan, C., Ren, L., Xiong, L., Li, Y ., 2026. Regime-
adaptive continual learning for portfolio management.
arXiv:2606.00143.
Pan, S.J., Yang, Q., 2010. A survey on transfer learning. IEEE
Transactions on Knowledge and Data Engineering 22, 1345–
1359. URL: https://ieeexplore.ieee.org/document
/5288526, doi:10.1109/TKDE.2009.191.
48

Pan, Y ., Liew, S.C., 2026. Learning to trade like an expert: Cog-
nitive fine-tuning for stable financial reasoning in language
models.arXiv:2604.16862.
Papadakis, C., Filandrianos, G., Dimitriou, A., Lymperaiou, M.,
Thomas, K., Stamou, G., 2025. Stocksim: A dual-mode order-
level simulator for evaluating multi-agent llms in financial
markets. URL: https://arxiv.org/abs/2507.09255 ,
doi:10.48550/arXiv.2507.09255,arXiv:2507.09255.
Park, E., 2026. Reflexivity as prompt: Does awareness of self-
reinforcing market dynamics improve llms as financial market
forecasters?arXiv:2606.00061.
Park, J.S., O’Brien, J.C., Cai, C.J., Ringel Morris, M., Liang,
P., Bernstein, M.S., 2023. Generative agents: Interactive
simulacra of human behavior, in: Proceedings of the ACM
SIGCHI Conference on Human Factors in Computing Sys-
tems (CHI). URL:https://arxiv.org/abs/2304.03442,
doi:10.1145/3544548.3581516.
Parlour, C.A., 1998. Price dynamics in limit order markets.
Review of Financial Studies 11, 789–816. URL: https:
//doi.org/10.1093/rfs/11.4.789 , doi:10.1093/rfs/
11.4.789.
Passos, G.G.F.G., Schmitz, E.A., Ribeiro, S.A., 2026. An
artificial market for brazilian real estate investment funds:
An agent-based proposal.arXiv:2607.25098.
Pearl, J., 2009. Causality: Models, Reasoning, and Inference. 2
ed., Cambridge University Press. URL: https://www.camb
ridge.org/core/books/causality/E62B1C761BC88EF
7A8FE13A25FDFBBCD.
Pei, Y ., Ge, Z., Zheng, J., Cartlidge, J., 2026. Market regime
council for dynamic credit assignment in multi-agent llm
decision systems.arXiv:2605.24490.
Perold, A.F., 1988. The implementation shortfall: Paper versus
reality. The Journal of Portfolio Management 14, 4–9.
URL: https://doi.org/10.3905/jpm.1988.409150 ,
doi:10.3905/jpm.1988.409150.
López de Prado, M., 2016. Building diversified portfolios
that outperform out of sample. The Journal of Portfolio
Management 42, 59–69. URL: https://doi.org/10.390
5/jpm.2016.42.4.059 , doi:10.3905/jpm.2016.42.4.
059.
López de Prado, M., 2018. The 10 reasons most machine
learning funds fail. The Journal of Portfolio Management
44, 120–133. URL: https://doi.org/10.3905/jpm.20
18.44.6.120 , doi:10.3905/jpm.2018.44.6.120 . also
circulated as an SSRN working paper.
Qian, C., 2026. Information limits and attractor dynamics
in economies of frontier llm agents: A pre-registered test.
arXiv:2607.06001.
Qian, L., Peng, X., Wang, Y ., Zhang, V .J., He, H., Smith,
H., Han, Y ., He, Y ., Li, H., Cao, Y ., Yu, Y ., Lopez-Lira,
A., Lu, P., Nie, J.Y ., Xiong, G., Huang, J., Ananiadou,
S., 2025. When agents trade: Live multi-market trading
benchmark for llm agents. arXiv preprint arXiv:2510.11695
URL: https://arxiv.org/abs/2510.11695 , doi:10.4
8550/arXiv.2510.11695.
Qin, M., Sun, S., Zhang, W., Xia, H., Wang, X., An, B., 2024.
Earnhft: Efficient hierarchical reinforcement learning for high
frequency trading, in: Proceedings of the AAAI Conference
on Artificial Intelligence. URL: https://arxiv.org/abs/
2309.12891, doi:10.1609/aaai.v38i13.29384.
Qu, B., Chen, M., 2026. Clqt: A closed-loop, cost-aware,
strategy-consistent benchmark for diagnostic evaluation of
llm portfolio-management agents.arXiv:2606.29771.
Qu, B., Chen, M., Wang, L., 2026. Propose, don’t judge: An
anytime-valid referee for llm agents that mine investment
factors.arXiv:2609.27051.
Rashid, M., Hong, L., Ding, J., Hossain, K.S.M.T., 2026.
Fin-analyst at finmmeval 2026 task 3: A live hybrid
trading agent with llm specialists and rule-based signals.
arXiv:2607.12233.
Reis, P., Serra, A.P., Gama, J., 2025. A deep learning framework
for medium-term covariance forecasting. arXiv preprint
arXiv:2503.01581 URL: https://arxiv.org/abs/25
03.01581, doi:10.48550/arXiv.2503.01581.
de la Rica Escudero, A., Garrido-Merchán, E.C., Coronado-
Vaca, M., 2025. Explainable post hoc portfolio management
financial policy of a deep reinforcement learning agent. PLOS
ONE 20, e0315528. URL: https://journals.plos.org/
plosone/article?id=10.1371/journal.pone.031552
8, doi:10.1371/journal.pone.0315528.
Rockafellar, R.T., Uryasev, S., 2000. Optimization of conditional
value-at-risk. Journal of Risk 2, 21–41. doi:10.21314/JOR
.2000.037.
Rodriguez Inserte, P., Nakhl’e, M., Qader, R., Caillaut, G.,
Liu, J., 2024. Large language model adaptation for financial
sentiment analysis. arXiv preprint arXiv:2401.14777 doi:10
.48550/arXiv.2401.14777.
Roncalli, T., 2013. Introduction to Risk Parity and Budgeting.
CRC Press. URL: https://www.thierry-roncalli.co
m/RiskParityBook.html.
Ross, S., Gordon, G.J., Bagnell, J.A., 2011. A reduction of
imitation learning and structured prediction to no-regret online
learning, in: Proceedings of the International Conference on
Artificial Intelligence and Statistics. URL: http://procee
dings.mlr.press/v15/ross11a.html.
Sakurai, K., Ogawa, T., Haseyama, M., Anan, A., 2026. Dy-
namic objective selection with safeguards and llm oversight
for financial decision-making.arXiv:2606.03704.
49

Salo, A., Doumpos, M., Liesiö, J., Zopounidis, C., 2024.
Fifty years of portfolio optimization: A survey and outlook.
European Journal of Operational Research 318, 1–18. URL:
https://www.sciencedirect.com/science/article/
pii/S0377221723009827 , doi:10.1016/j.ejor.2023.
12.031.
Saxena, M., Pangallo, M., Hommes, C., Caccioli, F., 2026.
Machine spirits: Speculation and adaptation of llm agents in
asset markets.arXiv:2604.18602.
Schaul, T., Quan, J., Antonoglou, I., Silver, D., 2016. Prioritized
experience replay, in: International Conference on Learning
Representations (ICLR). URL: https://arxiv.org/abs/
1511.05952.
Shapley, L.S., 1953. A value for n-person games. Contributions
to the Theory of Games 2, 307–317. URL: https://www.
rand.org/pubs/papers/P295.html.
Sharma, D., Shroff, G., 2026. Algoevolve: Llm-
driven meta-evolution of algorithmic trading programs.
arXiv:2606.26173.
Sheng, E.N.Y ., Shen, B., 2026. Formal mechanisms for market
stability in self-interested agent societies: A marketplace
simulation study.arXiv:2607.08652.
Shi, Y ., Duan, Y ., Li, J., 2025. Navigating the alpha jungle:
An llm-powered mcts framework for formulaic factor mining.
arXiv preprint arXiv:2505.11122 URL:https://arxiv.or
g/abs/2505.11122, doi:10.48550/arXiv.2505.11122.
Shi, Y ., Luo, K., Tang, N., Luo, Y ., 2026. Cstrader: A testbed
for language-grounded trading in a community-driven virtual
asset market.arXiv:2606.31461.
Shiller, R.J., 1981. Do stock prices move too much to be justified
by subsequent changes in dividends? American Economic
Review 71, 421–436. URL: https://www.aeaweb.org/a
er/top20/71.3.421-436.pdf.
Shinn, N., Cassano, F., Berman, E., Gopinath, A., Narasimhan,
K., Yao, S., 2023. Reflexion: Language agents with verbal
reinforcement learning, in: Advances in Neural Information
Processing Systems (NeurIPS). URL: https://papers.n
ips.cc/paper_files/paper/2023/hash/1b44b878bb7
82e6954cd888628510e90-Abstract-Conference.ht
ml.
Snell, J., Swersky, K., Zemel, R., 2017. Prototypical networks
for few-shot learning, in: Advances in Neural Information
Processing Systems (NeurIPS). URL: https://arxiv.or
g/abs/1703.05175.
Subaharan, S., 2026. Controlling long-horizon behavior in
language model agents with explicit state dynamics. arXiv
preprint arXiv:2601.16087v1 URL:https://arxiv.org/
pdf/2601.16087v1.
Sun, H., Zeng, S., 2025. H-mem: Hierarchical memory for high-
efficiency long-term reasoning in llm agents. arXiv preprint
arXiv:2507.22925 URL: https://arxiv.org/abs/2507
.22925, doi:10.48550/arXiv.2507.22925.
Sutton, R.S., Barto, A.G., 2018. Reinforcement Learning: An
Introduction. 2 ed., MIT Press. URL: http://incomplete
ideas.net/book/the-book-2nd.html.
Sutton, R.S., Precup, D., Singh, S., 1999. Between MDPs
and semi-MDPs: A framework for temporal abstraction in
reinforcement learning. Artificial Intelligence 112, 181–211.
URL:https://doi.org/10.1016/S0004-3702(99)000
52-1, doi:10.1016/S0004-3702(99)00052-1.
Szot, A., Kirchhof, M., Attia, O., Toshev, A., 2026. Expanding
llm agent boundaries with strategy-guided exploration. arXiv
preprint arXiv:2603.02045 URL:https://arxiv.org/ab
s/2603.02045, doi:10.48550/arXiv.2603.02045.
Tan, L., Huang, K.W., Wu, K., 2025a. Fred: Financial
retrieval-enhanced detection and editing of hallucinations in
language models. arXiv preprint arXiv:2507.20930 URL:
https://arxiv.org/abs/2507.20930. financial retrieval-
enhanced hallucination detection and editing.
Tan, X., Wang, X., Liu, Q., Xu, X., Yuan, X., Zhu, L., Zhang,
W., 2025b. Hydrarag: Structured cross-source enhanced
large language model reasoning, in: Conference on Empirical
Methods in Natural Language Processing (EMNLP). URL:
https://arxiv.org/abs/2505.17464 , doi:10.48550
/arXiv.2505.17464 . accepted at EMNLP 2025 (Main
Conference).
Tang, Z., Chen, Z., Yang, J., Mai, J., Zheng, Y ., Wang, K.,
Chen, J., Lin, L., 2025. Alphaagent: Llm-driven alpha
mining with regularized exploration to counteract alpha decay,
in: Proceedings of the 31st ACM SIGKDD Conference on
Knowledge Discovery and Data Mining (KDD ’25). URL:
https://dl.acm.org/doi/abs/10.1145/3711896.373
6838.
Tetlock, P.C., 2007. Giving content to investor sentiment: The
role of media in the stock market. The Journal of Finance 62,
1139–1168. URL: https://doi.org/10.1111/j.1540
-6261.2007.01232.x , doi:10.1111/j.1540-6261.2007
.01232.x.
Tian, F., Salim, F.D., Xue, H., 2025. Tradinggroup: A multi-
agent trading system with self-reflection and data-synthesis,
in: Proceedings of the 6th ACM International Conference on
AI in Finance (ICAIF ’25). URL: https://arxiv.org/ab
s/2508.17565.
Tsai, Y .H.H., Bai, S., Yamada, M., Morency, L.P., Salakhutdinov,
R., 2019. Multimodal Transformer for unaligned multimodal
language sequences, in: Proceedings of the 57th Annual
Meeting of the Association for Computational Linguistics
(ACL), pp. 6558–6569. URL: https://aclanthology.o
rg/P19-1656/, doi:10.18653/v1/P19-1656.
50

Tulving, E., 1972. Episodic and semantic memory, in: Tulving,
E., Donaldson, W. (Eds.), Organization of Memory. Academic
Press. URL: https://psycnet.apa.org/record/197
3-08477-007.
Unnikrishnan, A., 2024. Financial news-driven llm reinforce-
ment learning for portfolio management. URL: https:
//arxiv.org/pdf/2411.11059,arXiv:2411.11059.
Uysal, A.S., Li, X., Mulvey, J.M., 2024. End-to-end risk
budgeting portfolio optimization with neural networks. An-
nals of Operations Research 339, 397–426. URL: https:
//doi.org/10.1007/s10479-023-05539-4 , doi:10
.1007/s10479-023-05539-4 . originally circulated as
arXiv:2107.04636.
Varghese, J., Bickmann, L., Sandmann, S., 2026. Information
specialization and constrained synthesis in multi-agent llm
forecasting: A prospective live-study of the 2026 fifa world
cup.arXiv:2609.12495.
Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L.,
Gomez, A.N., Kaiser, Ł., Polosukhin, I., 2017. Attention is
all you need, in: Advances in Neural Information Processing
Systems (NeurIPS). URL: https://arxiv.org/abs/17
06.03762.
Vinyals, O., Blundell, C., Lillicrap, T., Kavukcuoglu, K.,
Wierstra, D., 2016. Matching networks for one shot learning,
in: Advances in Neural Information Processing Systems
(NeurIPS). URL:https://arxiv.org/abs/1606.04080.
V oronina, A., Romanko, O., Cao, R., Kwon, R.H., Mendoza-
Arriaga, R., 2025. Generative ai-enhanced sector-
based investment portfolio construction. arXiv preprint
arXiv:2512.24526v1 URL: https://arxiv.org/pdf/25
12.24526v1.
Vytelingum, P., Baggott, R., Stillman, N., Zhang, J., Zhu, D.,
Chen, T., Lyon, J., 2025. Agent-based liquidity risk modelling
for financial markets. arXiv preprint arXiv:2505.15296 URL:
https://arxiv.org/abs/2505.15296, doi:10.48550/a
rXiv.2505.15296.
Wang, B., Zhang, X., 2026. Deep reinforcement learning
for equity trading: Benchmarking actor-critic methods with
forward retraining.arXiv:2609.31870.
Wang, B., Zhou, K., Guo, L., Chen, F., 2026a. Finperma:
A theory-informed, event-grounded personalized-memory
benchmark for llm agents.arXiv:2608.04095.
Wang, D., Patel, J., Zha, D., Yang, S.Y ., Liu, X.Y ., 2025a.
Finlora: Benchmarking lora methods for fine-tuning llms
on financial datasets. arXiv preprint arXiv:2505.19819 URL:
https://arxiv.org/pdf/2505.19819, doi:10.48550/a
rXiv.2505.19819.
Wang, D., Xu, H., Xian, J., 2026b. Polygnosis 2.0: Enhancing
llm reasoning via agentic harness engineering for polymarket
and osint insight extraction.arXiv:2605.25958.
Wang, L., Ma, C., Feng, X., Zhang, Z., Yang, H., Zhang, J.,
Chen, Z., Tang, J., Chen, X., Lin, Y ., Zhao, W.X., Wei,
Z., Ji, H., 2024. A survey on large language model based
autonomous agents. Frontiers of Computer Science 18,
186345. URL:https://arxiv.org/abs/2308.11432.
Wang, M., Saxena, N., 2026. Sok: Trading agents or market
crashers? dissecting robustness and security failures in aca-
demic financial llm trading schemes.arXiv:2609.19705.
Wang, N., Yang, H., Wang, C.D., 2023a. Fingpt: Instruction
tuning benchmark for open-source large language models in
financial datasets, in: NeurIPS 2023 Workshop on Instruction
Tuning and Instruction Following. URL: https://arxiv.
org/abs/2310.04793, doi:10.48550/arXiv.2310.0479
3.
Wang, Q., Tong, Z., Chen, N., Wu, Z., 2026c. Crossalpha:
An annual-report benchmark for cross-market factor research
(with llm agents).arXiv:2605.29286.
Wang, Q., Wei, Z., Wei, Z., Shen, W., 2026d. Alphadiverse:
Post-training local quantitative research agents for diverse
exploration in alpha factor mining.arXiv:2609.29014.
Wang, X., Chi, J., Tai, Z., Kwok, T.S.T., Li, M., Li, Z., He,
H., Hua, Y ., Lu, P., Wang, S., Wu, Y ., Huang, J., Tian, J.,
Mo, F., Cui, Y ., Zhou, L., 2025b. Finsage: A multi-aspect rag
system for financial filings question answering. arXiv preprint
arXiv:2504.14493 URL: https://arxiv.org/abs/2504
.14493, doi:10.48550/arXiv.2504.14493 . accepted at
CIKM 2025.
Wang, X., Wei, J., Schuurmans, D., Le, Q., Chi, E., 2022. Self-
consistency improves chain of thought reasoning in language
models. URL: https://arxiv.org/abs/2203.11171 ,
arXiv:2203.11171.
Wang, Y ., Wang, Y ., Deng, J., Tang, H., 2026e. Beyond
forecasting: The belief-to-trade layer in prediction-market
agents.arXiv:2607.03015.
Wang, Z., Li, Y ., Wu, J., Soon, J., Zhang, X., 2023b. Finvis-
gpt: A multimodal large language model for financial chart
analysis. arXiv preprint arXiv:2308.01430 doi:10.48550/a
rXiv.2308.01430.
Wang, Z., Yang, W., Wu, Q., Ma, L., 2026f. Backtestbench:
Benchmarking large language models for automated quantita-
tive strategy backtesting.arXiv:2605.17937.
Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B.,
Xia, F., Chi, E., Le, Q., Zhou, D., 2022. Chain-of-
thought prompting elicits reasoning in large language models,
in: Advances in Neural Information Processing Systems
(NeurIPS), pp. 24824–24837. URL: https://arxiv.org/
abs/2201.11903, doi:10.48550/arXiv.2201.11903.
Wen, Y ., Cai, Z., Mirzaei, I., Cai, X., 2026. Evage: Autonomous
mev generation and adaptation via multi-agent harness.
arXiv:2609.27424.
51

Weng, Z., Zhang, S., Wang, T., Xia, Y ., 2026. Alphalogics:
A market logic-driven multi-agent system for scalable and
interpretable alpha factor generation.arXiv:2603.20247.
Wheeler, A., Varner, J.D., 2023. Scalable agent-based modeling
for complex financial market simulations. arXiv preprint
arXiv:2312.14903v2 URL: https://arxiv.org/pdf/23
12.14903v2.
White, H., 2000. A reality check for data snooping. Economet-
rica 68, 1097–1126. URL: https://doi.org/10.1111/
1468-0262.00152, doi:10.1111/1468-0262.00152.
Wooldridge, M., 2009. An Introduction to MultiAgent Systems.
2 ed., John Wiley & Sons. URL: https://www.wiley.co
m/en-us/An+Introduction+to+MultiAgent+Systems%
2C+2nd+Edition-p-9780470519462.
Wu, S., Irsoy, O., Lu, S., Dabravolski, V ., Dredze, M.,
Gehrmann, S., Kambadur, P., Rosenberg, D., Mann, G., 2023.
Bloomberggpt: A large language model for finance. arXiv
preprint arXiv:2303.17564 URL:https://arxiv.org/ab
s/2303.17564, doi:10.48550/arXiv.2303.17564.
Wu, W., 2026. Auditing asset-specific preferences in financial
large language models: Evidence from bitcoin representations
and portfolio allocation.arXiv:2606.02528.
Xia, Y ., Wang, T., Liew, S.C., Zhang, S., 2025. A hierarchical
deep learning framework for pair trading with attention
and graph networks. Expert Systems with Applications
291, 128496. URL: https://www.sciencedirect.
com/science/article/pii/S0957417425011183 ,
doi:10.1016/j.eswa.2025.128496.
Xia, Y ., Wang, T., Zhang, S., Weng, Z., Cao, B., Liew, S.C., 2026.
HiveMind: Contribution-guided online prompt optimization
of LLM multi-agent systems, in: Proceedings of the AAAI
Conference on Artificial Intelligence, pp. 29767–29774. URL:
https://ojs.aaai.org/index.php/AAAI/articl
e/view/40222 , doi:10.1609/AAAI.V40I35.40222 ,
arXiv:2512.06432.
Xiao, M., Jiang, Z., Qian, L., Chen, Z., He, Y ., Xu, Y ., Jiang,
Y ., Li, D., Weng, R.L., Peng, M., Huang, J., Ananiadou,
S., Xie, Q., 2025a. Retrieval-augmented large language
models for financial time-series forecasting. arXiv preprint
arXiv:2502.05878 URL: https://arxiv.org/abs/2502
.05878, doi:10.48550/arXiv.2502.05878.
Xiao, Y ., Sun, E., Chen, T., Wu, F., Luo, D., Wang, W.,
2025b. Trading-r1: Financial trading with llm reasoning
via reinforcement learning. arXiv preprint arXiv:2509.11420
URL: https://arxiv.org/abs/2509.11420 , doi:10.4
8550/arXiv.2509.11420.
Xiao, Y ., Sun, E., Luo, D., Wang, W., 2024. Tradingagents:
Multi-agents llm financial trading framework. arXiv preprint
arXiv:2412.20138 URL: https://arxiv.org/abs/2412
.20138, doi:10.48550/arXiv.2412.20138.
Xie, Q., Han, W., Chen, Z., Xiang, R., Zhang, X., He, Y ., Xiao,
M., Li, D., Dai, Y ., Feng, D., Xu, Y ., Kang, H., Kuang, Z.,
Yuan, C., Yang, K., Luo, Z., Zhang, T., Liu, Z., Xiong, G.,
Deng, Z., Jiang, Y ., Yao, Z., Li, H., Yu, Y ., Hu, G., Huang,
J., Liu, X.Y ., Lopez-Lira, A., Wang, B., Lai, Y ., Wang, H.,
Peng, M., Ananiadou, S., Huang, J., 2024. Finben: A holistic
financial benchmark for large language models, in: Advances
in Neural Information Processing Systems (NeurIPS), pp.
95716–95743. URL: https://arxiv.org/abs/2402.126
59.
Xie, Q., Han, W., Zhang, X., Lai, Y ., Peng, M., Lopez-Lira, A.,
Huang, J., 2023. Pixiu: A large language model, instruction
data and evaluation benchmark for finance. arXiv preprint
arXiv:2306.05443 URL: https://arxiv.org/abs/2306
.05443, doi:10.48550/arXiv.2306.05443.
Xing, F., 2025. Designing heterogeneous llm agents for financial
sentiment analysis. ACM Transactions on Management
Information Systems 16, 1–24. doi:10.1145/3688399.
Xiong, G., Deng, Z., Wang, K., Cao, Y ., Li, H., Yu, Y ., Peng, X.,
Lin, M., Smith, K.E., Liu, X.Y ., Huang, J., Ananiadou, S., Xie,
Q., 2025. FLAG-TRADER: Fusion LLM-agent with gradient-
based reinforcement learning for financial trading, in: Che,
W., Nabende, J., Shutova, E., Pilehvar, M.T. (Eds.), Findings
of the Association for Computational Linguistics: ACL 2025,
Association for Computational Linguistics, Vienna, Austria.
pp. 13921–13934. URL: https://aclanthology.org/2
025.findings-acl.716/ , doi:10.18653/v1/2025.fin
dings-acl.716.
Xu, F., Yin, Y ., Zhang, X., Liu, T., Jiang, S., Zhang, Z., 2024a.
Alpha²: Discovering logical formulaic alphas using deep
reinforcement learning. arXiv preprint arXiv:2406.16505
URL:https://arxiv.org/abs/2406.16505.
Xu, Y ., Xie, L., Gu, X., Chen, X., Chang, H., Zhang, H., Chen,
Z., Zhang, X., Tian, Q., 2024b. Qa-lora: Quantization-
aware low-rank adaptation of large language models, in:
Proceedings of the International Conference on Learning
Representations (ICLR). URL: https://openreview.net
/forum?id=WvFoJccpo8, doi:10.48550/arXiv.2309.14
717.
Xue, W., 2026. Representation signatures and risk-feedback
alignment in llm trading agents.arXiv:2605.28850.
Yang, H., Liu, X.Y ., Zhong, S., Walid, A., 2025. Deep
reinforcement learning for automated stock trading: An
ensemble strategy. arXiv preprint arXiv:2511.12120 URL:
https://arxiv.org/abs/2511.12120, doi:10.48550/a
rXiv.2511.12120.
Yang, J., Wu, Y ., Liu, J., Liang, P., 2026. Recursive multi-agent
trading system: Iterative optimized portfolio strategy under
geopolitical uncertainty.arXiv:2605.25311.
Yang, Z., 2026. When valid signals fail: Regime
boundaries between llm features and rl trading policies.
arXiv:2604.10996.
52

Yao, J., Zheng, Z., Li, B., 2026. Beyond agent architecture:
Execution assumptions and reproducibility in llm-based
trading systems.arXiv:2606.08285.
Yao, S., Yu, D., Zhao, J., Shafran, I., Griffiths, T.L., Cao,
Y ., Narasimhan, K., 2023a. Tree of thoughts: Deliberate
problem solving with large language models, in: Advances
in Neural Information Processing Systems (NeurIPS). URL:
https://arxiv.org/abs/2305.10601, doi:10.48550/a
rXiv.2305.10601.
Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K.,
Cao, Y ., 2023b. React: Synergizing reasoning and acting in
language models, in: International Conference on Learning
Representations (ICLR). URL: https://arxiv.org/abs/
2210.03629, doi:10.48550/arXiv.2210.03629.
Ye, W., Sun, Y ., Ren, X., Yu, S., 2026a. Agonalpha:
Autonomous alpha discovery via prompt economy and
scalable agentic search.arXiv:2608.11250.
Ye, W., Xu, J., Wu, Y ., 2026b. When ai agents meet mev: Cross-
chain arbitrage in the agentic economy. arXiv:2609.17897.
Ye, Y ., Han, J., Hu, A., Bu, J., 2026c. The alpha illusion:
Reported alpha from llm trading agents should not be treated
as deployment evidence.arXiv:2605.16895.
Yi, J., Yang, J., Jin, Y ., Li, Y ., 2026. Alphaschema: Exploring
the space of trading semantics for llm-based alpha mining.
arXiv:2607.26642.
Yu, H., Li, F., You, J., 2025. Livetradebench: Seeking real-
world alpha with large language models. arXiv preprint
arXiv:2511.03628 URL: https://arxiv.org/abs/25
11.03628, doi:10.48550/arXiv.2511.03628.
Yu, H., Zheng, Z., Pan, J.Z., Liu, T., 2026a. Alphamemo:
Structured search-process memory for self-evolving alpha
mining agents.arXiv:2606.20625.
Yu, S., Xue, H., Ao, X., Pan, F., He, J., Tu, D., He, Q.,
2023a. Generating synergistic formulaic alpha collections
via reinforcement learning, in: Proceedings of the 29th ACM
SIGKDD Conference on Knowledge Discovery and Data
Mining. URL: https://arxiv.org/abs/2306.12964 ,
doi:10.1145/3580305.3599831.
Yu, X., Zhou, J., Ding, G., Wei, W., 2026b. Can ai make money
in crypto? measuring the gap from backtests to real markets.
arXiv:2609.34510.
Yu, Y ., Li, H., Chen, Z., Jiang, Y ., Li, Y ., Zhang, D., Liu,
R., Suchow, J.W., Khashanah, K., 2023b. Finmem: A
performance-enhanced llm trading agent with layered memory
and character design. arXiv preprint arXiv:2311.13743 URL:
https://arxiv.org/abs/2311.13743, doi:10.48550/a
rXiv.2311.13743.
Yu, Y ., Yao, Z., Li, H., Deng, Z., Cao, Y ., Chen, Z., Suchow,
J.W., Liu, R., Cui, Z., Xu, Z., Zhang, D., Subbalakshmi, K.,
Xiong, G., He, Y ., Huang, J., Li, D., Xie, Q., 2024. Fin-
con: A synthesized llm multi-agent system with conceptual
verbal reinforcement for enhanced financial decision mak-
ing, in: Advances in Neural Information Processing Systems
(NeurIPS). URL: https://arxiv.org/abs/2407.06567,
doi:10.48550/arXiv.2407.06567.
Yuan, X., Xu, H., Xu, S., Zou, C., Xiong, J., 2026a. Traderbench:
How robust are ai agents in adversarial capital markets? arXiv
preprint arXiv:2603.00285v1 URL:https://arxiv.org/
abs/2603.00285.
Yuan, Y ., Sheng, J., Zeng, S., Wang, J., 2026b. Alphacrafter:
Harnessing multi-agent workflows for cross-sectional quanti-
tative trading.arXiv:2605.05580.
Yuksel, K.A., Sawaf, H., 2024. A multi-ai agent system for
autonomous optimization of agentic ai solutions via iterative
refinement and llm-driven feedback loops. arXiv preprint
arXiv:2412.17149v1 URL: https://arxiv.org/pdf/24
12.17149v1.
Yun, J., Lee, H.J., Jeon, I., 2025. Quantevolve: Automating
quantitative strategy discovery through multi-agent evolu-
tionary framework. arXiv preprint arXiv:2510.18569 URL:
https://arxiv.org/abs/2510.18569, doi:10.48550/a
rXiv.2510.18569.
Zhang, B., 2026a. Graph attention-based heterogeneous multi-
agent deep reinforcement learning for adaptive portfolio
optimization. Scientific Reports 16, 2674. URL: https:
//www.nature.com/articles/s41598-025-32408-w ,
doi:10.1038/s41598-025-32408-w.
Zhang, B., Yang, H., Liu, X.Y ., 2023a. Instruct-fingpt: Financial
sentiment analysis by instruction tuning of general-purpose
large language models. arXiv preprint arXiv:2306.12659
URL: https://arxiv.org/abs/2306.12659 , doi:10.4
8550/arXiv.2306.12659.
Zhang, B., Yang, H., Zhou, T., Babar, M.A., Liu, X.Y .,
2023b. Enhancing financial sentiment analysis via retrieval
augmented large language models, in: Proceedings of the 4th
ACM International Conference on AI in Finance, pp. 349–356.
doi:10.1145/3604237.3626866.
Zhang, K., Ge, W., Jiang, L., Yang, W., 2026a. Openfingym: A
verifiable multi-task gym environment for evaluating quant
agents.arXiv:2606.26350.
Zhang, L., 2026b. Llm-enhanced dynamic financial knowledge
graphs for cross-entity signal propagation and alpha discovery.
arXiv:2607.10932.
Zhang, O., Zhang, Z., 2026. A review of large language models
for stock price forecasting from a hedge-fund perspective.
arXiv:2605.05211.
53

Zhang, W., Jia, R., Wang, Y ., Cheng, D., Zhao, M., Chen,
C., 2025. Enhancing portfolio optimization via heuristic-
guided inverse reinforcement learning with multi-objective
reward and graph-based policy learning, in: Proceedings of
the International Joint Conference on Artificial Intelligence
(IJCAI). URL: https://www.ijcai.org/proceedings/
2025/1054.pdf.
Zhang, W., Zhao, L., Xia, H., Sun, S., Sun, J., Qin, M., Li, X.,
Zhao, Y ., Zhao, Y ., Cai, X., Zheng, L., Wang, X., An, B., 2024.
A multimodal foundation agent for financial trading: Tool-
augmented, diversified, and generalist, in: Proceedings of the
30th ACM SIGKDD Conference on Knowledge Discovery
and Data Mining (KDD ’24). URL: https://arxiv.org/
abs/2402.18485, doi:10.1145/3637528.3671801. aCM
KDD 2024. Full paper PDF available at the NTU author page.
Zhang, Y ., Koyluoglu, O.O., Venkatesh, T., Martinez,
R.D., 2026b. Frontierfinance: A challenging bench-
mark for measuring frontier intelligence of finance agents.
arXiv:2608.11683.
Zhang, Z., Stadie, B.C., 2026. Temporal leakage in llm
backtesting: Measurement, validation, and adjusted scores.
arXiv:2608.02985.
Zhao, L., Sun, R., Jiang, Z., Yang, B., Bai, Y ., Chen, M., Wang,
X., Li, J., Bai, Z., 2025. Contesttrade: A multi-agent trading
system based on internal contest mechanism. arXiv preprint
arXiv:2508.00554 URL: https://arxiv.org/abs/2508
.00554, doi:10.48550/arXiv.2508.00554.
Zhao, R., Raissi, M., 2026. Backtrader-bench: Benchmarking
llm agents on algorithmic trading with self-generated mcqs.
arXiv:2608.11232.
Zhao, S., Dong, Z., Cao, Z., Douady, R., 2024. Hedge
fund portfolio construction using polymodel theory and
itransformer. arXiv preprint arXiv:2408.03320 URL: https:
//arxiv.org/abs/2408.03320, doi:10.48550/arXiv.2
408.03320.
Zhao, S., Sha, T., 2026. Goant: Quality-diversity multi-agent
search for alpha factor discovery in market microstructure
data.arXiv:2609.08719.
Zhao, Y ., Yang, Z., Zhu, Z., 2026. Alphapareto: Formulaic alpha
discovery with llm-guided multi-objective reinforcement
learning.arXiv:2609.34188.
Zhu, L., Cai, M., 2026. Artificial intelligence in equity and
crypto markets: Progress, profitability evidence, and the limits
of automated investing.arXiv:2609.04917.
Zhu, Q., Lu, Z., Zhu, J., Chen, N., 2026a. Alphaseek: Trajectory-
level self-iterative factor mining framework for multi-source
financial data.arXiv:2608.13913.
Zhu, T., Zhao, W., Sun, R., Luan, B., 2026b. From knowing
to doing: A memory-controlled benchmark for llm trading
agents on stock markets.arXiv:2605.28359.
Zong, C., Wang, C., Qin, M., Feng, L., Wang, X., An,
B., 2024. Macrohft: Memory augmented context-aware
reinforcement learning on high frequency trading. arXiv
preprint arXiv:2406.14537 URL: https://arxiv.org/
abs/2406.14537 , doi:10.48550/arXiv.2406.14537 .
accepted to KDD 2024.
Zou, M., Chen, J., Luo, A., Dai, J., Zhang, C., Sun, D., Xu, Z.,
2026. Finevo: From isolated backtests to ecological market
games for multi-agent financial strategy evolution. arXiv
preprint arXiv:2602.00948 URL:https://arxiv.org/ab
s/2602.00948, doi:10.48550/arXiv.2602.00948.
Zouaoui, H., Naas, M.N., 2025. Portfolio optimization based
on mpt-lstm neural networks: A case study of cryptocurrency
markets. Finance, Accounting and Business Analysis (FABA)
7, 82–98. URL:https://faba.bg/index.php/faba/art
icle/view/265/137, doi:10.37075/FABA.2025.1.07.
54

Appendix A. Systematic Search Summary
This appendix documents the information sources and query
patterns that define the survey’s search boundary and support
reproduction of the search.
Table A.22:Information sources and search summary (submitted as
Supplementary Material S1).
Source Notes
ACM Digital
Library
Keyword search over agentic trading, LLM agents, and
financial decision-making.
IEEE Xplore Keyword search focused on trading systems, execution, and
risk control.
arXiv Preprints in cs.AI/cs.LG/q-fin with agent/trading keywords.
SSRN Working papers in quantitative finance and computational
finance.
Google
Scholar
Broad supplementary source for cross-venue discovery and
citation chaining.
Table A.23:Example query patterns used in the search.
Target Query pattern (example)
Agentic
trading
(agentORagenticORLLM agent) AND (tradingOR
portfolioORexecutionORrisk)
LLM finance
agents
(large language model OR LLM) AND (finance OR
financial) AND (agentORtoolORmulti-agent)
Evaluation/
validity
(trading OR backtest) AND (look-ahead OR
leakage OR transaction cost OR slippage OR
survivorship)
Coverage note.This survey discusses literature through the
formal registry cutoffof2026-09-30. The initial ledger was
screened through2026-03-09; at revision, we queried arXiv
in an extension window covering2026-03-10 to 2026-09-30
with the same query families in Table A.23 supplemented by
trading-agent, multi-agent-market, and alpha-mining phrase
patterns, retrieving 1,539 unique records. Of these, 154
records entered eligibility assessment under the same inclusion
boundary; the combined v2 registry records the per-record
decisions. Supplementary S1 retains the initial-window registry,
retrieval counts, and screening logs. Extension query families are
described here and in Section 2; the extension retrieval dumps
are separate working materials. Table A.23 lists representative
example patterns; the full six query families are enumerated in
Sec. 2. Evidence annotations, screening counts, and protocol-
coded denominators all derive from the combined registry
snapshot.
Appendix B. Corpus Snapshot of the Evidence Ledger
This appendix consolidates corpus-level descriptive findings that
follow from the review protocol but are not themselves part of
the protocol definition. Unless stated otherwise, denominator-
based summaries here use the primary empirical subset (n =80),
while the full included ledger contains 185 studies partitioned
into 80 primary empirical studies and 105 background studies.
The primary subset is concentrated in very recent work: within
the current ledger,79/80primary studies were published between
2024 and 2026. As coded by venue type in the registry,19/80
primary studies appear in peer-reviewed venues (journal or
conference),61/80are preprints or otherwise venue-unrecorded,
and0/80remain uncoded. The registry records the first public
version year; a later journal version may therefore have a
different publication year. These counts describe the publication
landscape of the assembled corpus.
The primary subset reports different levels of protocol detail. In
the pooled 80-study subset,50/80studies report an extractable
split protocol,47/80specify a transaction-cost model,48/80
document universe/survivorship handling,47/80report execu-
tion timing or semantics, and35/80meet the R1–R3 artifact-
availability proxy, derived from the reproducibility code rather
than a separate direct artifact-extraction field. Table 4 sepa-
rates these pooled rates by cohort and records the retrieval and
coding differences needed for interpretation. Evaluation types
are distributed across backtest, simulation, live, and benchmark
evaluations; narrative-only and unclear types are outside this
empirical denominator.
Reading note.In the figures below, Unknown denotes informa-
tion that is not reported clearly enough in the source for reliable
extraction under our conservative coding policy; the panels are
corpus-level reporting distributions within the current ledger.
Appendix B.1. Extension-Cohort Landscape
Table B.25 groups the extension-window background/context
studies by the role they serve in the map. Market-level multi-
agent simulation ecosystems, perception/retrieval infrastructure,
and additional validity-oriented studies are discussed in the body
text (Sections 3, 4, 11 and 13); the table collects representative
studies from the remaining background cohort so that the
extension window’s coverage can be inspected in one place.
Appendix C. Representative A-C-A Reclassification Notes
This appendix provides reclassification notes for 19 representa-
tive works to illustrate how the Architecture-Capability-Adap-
tation (A-C-A) lens distinguishes system design choices. For
each work, we document: (i) classification under prior frame-
works (where available), (ii) A-C-A reclassification with coding
rationale, and (iii) the specific analytical insight surfaced by the
lens.
Appendix C.1. Reclassification Procedure
Paper Selection.We selected 19 works representing diverse ar-
chitectural approaches, capabilities, and adaptation mechanisms.
Selection criteria: (a) coverage of all three A-C-A dimensions,
(b) citation count or recency (indicating influence), (c) availabil-
ity of technical details sufficient for classification.
Coding Procedure.For each paper, one author prepared an
initial A-C-A classification and coding rationale, and the authors
then reconciled edge cases through discussion. The resulting
notes document how the lens is applied to the selected works.
Inter-rater agreement and external validation of these A-C-A
classifications were not assessed.
55

Table B.24:Reproducibility levels within the primary empirical subset (n=80).
Level Definition Criteria Count %
R0 No runnable artifacts No publicly accessible code repository, or
repository is broken/404, or it lacks essential
files and cannot run
45 56.2
R1 Code available (not runnable) Public repository exists and is accessible, but
key components are missing (dependencies,
data access, eval scripts)
33 41.2
R2 Runnable with gaps Complete code is available and data is ac-
cessible or clearly documented, and evalua-
tion scripts are provided, but pinned environ-
ment, complete documentation, or an end-to-
end pipeline may still be missing
2 2.5
R3 Full reproduction package Complete code with pinned environment, data
snapshots or clear access instructions, complete
documentation, and an end-to-end evaluation
pipeline
0 0.0
R2 or above (runnable with gaps or better) 2 2.5
0 10 20 30 40
Studies
R0
R1
R2
R3
Unknown
45
33
2
0
0
Reproducibility levels
(a)Reproducibility level.
0 10 20 30 40 50
Studies
backtest
benchmark
live
simulation
narrative-only
Unknown
50
14
9
7
0
0
Evaluation type (b)Evaluation type.
0 10 20 30 40 50
Studies
Split
Execution
Costs
Universe
Artifact proxy
50
47
47
48
35
Protocol-field coverage
(c)Protocol-field coverage.
0 10 20 30
Studies
walk-forward
rolling
other
Unknown
5
8
37
30
Split-protocol reporting (d)Split-protocol reporting.
Figure B.16:Corpus-level reporting distributions within the primary empirical subset (n=80).
Prior Framework Identification.For each work, we identified
its classification in existing surveys where available: Wang et
al. 2024 (LLM-Agent Survey), Ding et al. 2024 (LLM-Finance
Survey), or task-centric benchmarks (FinBen, InvestorBench).
Where a work was not explicitly labeled in one of those sources,
the shorthand in the Prior column should be read as our closest
reconstruction of how that work would map to the earlier
scheme.
Appendix C.2. Reclassification Dataset
Memory descriptors in the table retain terms used in individual
systems. In the survey’s operational taxonomy, experience re-
trieval is discussed under associative vector storage when vector
indexing is specified, while explicit financial knowledge stores
56

Table B.25:Extension-cohort landscape: background/context studies included in the ledger (2026-03-10 to 2026-09-30), grouped by the role they
play for readers. These studies inform design and evaluation practice but are not part of the primary empirical subset (n=80).
Reader-facing role Representative studies
Benchmarks & evaluation har-
nesses
BacktestBench Wang et al. (2026f), Backtrader-Bench Zhao and Raissi (2026), FinResearchBench II Luan
et al. (2026), BankerToolBench Lau et al. (2026), Foresight Arena Nechepurenko and Shuvalov (2026),
ValueBlindBench Chang et al. (2026), ShiJianBench Gong et al. (2026), FrontierFinance Zhang et al. (2026b),
QuantEval Kang et al. (2026), reliable multi-agent evaluation Nguyen and Pham (2026)
Research tooling & agent infras-
tructure
AlphaLab Hogan et al. (2026), PolyGnosis 2.0 Wang et al. (2026b), interaction-native knowledge harnesses
Borjigin et al. (2026), RIDGE Cheng et al. (2026a), PandaAI Li et al. (2026f), agentic forecasting infrastructure
Chai et al. (2026)
Surveys & cross-cutting analyses agentic AI in finance Aldridge et al. (2026), LLM stock forecasting review Zhang and Zhang (2026), AI in
equity/crypto markets Zhu and Cai (2026)
Adjacent financial-agent applica-
tions
AI-economist frameworks Kato (2026), multi-agent venture-capital due diligence Alexandrou and Pramatari
(2026), verifiable forecast actions Chen et al. (2026a)
are discussed under structured knowledge bases; these descrip-
tors do not by themselves establish a particular implementation.
Table C.26 presents the complete reclassification notes, orga-
nized by architectural family.
Appendix C.3. Illustrative Patterns from Reclassification
Pattern 1: Architecture-Capability Non-Alignment.The
same Reactive Architecture (FinAgent, AgentGuard) supports
different capabilities (α vs R) depending on perceptual input and
memory integration. This cross-cutting pattern is obscured by
capability-centric categorizations.
Pattern 2: Adaptation Level Distinction.The adaptation
dimension distinguishes prompt- and memory-mediated updates
(FinAgent, RAG-Fintech, FinRS, and FinCon) from weight-
based RL (Alpha 2, FinRL-DeepSeek) and structural search
(AlphaAgent, FinEvo). MetaGPT provides a background
example of SOP-guided prompting, rather than financial SFT.
Each update mechanism has distinct evaluation requirements
(Sec. 13).
Pattern 3: Multi-Agent Architectural Hierarchy.Prior
frameworks often use broad “multi-agent” labels. The A-C-A
lens distinguishes role-based, hierarchical, and market-ecology
coordination patterns, making the coordination mechanism
visible rather than treating agent count as the primary distinction.
Appendix C.4. Coding Status
The coding notes document qualitative author reconciliation and
the rationale for boundary cases, providing a traceable account
of applying the A-C-A lens to the selected works.
Appendix C.5. Limitations of the Reclassification Notes
1. Selection Bias:19 works selected from a broader review
corpus spanning included studies, background references,
and a small number of boundary cases used to stress-test
the A-C-A lens; they were not randomly sampled.
2. Temporal Coverage:15 of these 19 illustrative works
first appeared in 2024–2026 (79%), using the first public
version year rather than a later publication year. This
denominator is separate from the 80-study empirical
subset and reflects field recency. Earlier works may reveal
different architectural patterns.
3. Prior Framework Availability:Not all works classified
in existing surveys. Where unavailable, we inferred likely
categorization based on paper content and survey scope.
Across these examples, the A-C-A lens distinguishes design
choices and surfaces architectural patterns that may be obscured
by broader system- or task-level labels.
Appendix D. Excluded Studies and Rationale
To keep the evidence-mapping process auditable, this appendix
distinguishes two decisions that are easily conflated. First,
final exclusionsare candidate-registry records outside the
finance, trading, portfolio, or risk-management scope of this
survey. Second,background-tier boundary decisionsare finance-
relevant records that remain in the included evidence ledger
but do not enter the primary empirical subset because they
fail at least one of three criteria: Action Output, Closed-
Loop Evaluation, or an eligible empirical evaluation type.
We document both decision types—using PRISMA-ScR as a
reporting aid for scoping-style transparency rather than as a
claim of a full systematic-review workflow—to facilitate audit
and assessment of potential selection bias.
Appendix D.1. Exclusion Categories and Boundary Decisions
Candidate records were counted as final exclusions only when
they fell outside the domain boundary of this survey. Finance-
relevant records that were prediction models, benchmarks, tools,
or conceptual background papers were retained as background
or context where useful, but were excluded from the primary
empirical denominator. The operational criteria are:
57

Table C.26:Representative A-C-A reclassification notes for 19 works, documenting architectural components, financial capabilities, adaptation
mechanisms, and the rationale for each mapping.
Work Prior A-C-A Reclassification P M R Adapt Key Insight from A-C-A
FinBERT Araci
(2019)
W: “NLP
Model”, D:
“Sentiment”
Arch: Text Perception only; Cap: BG (no Action); Adapt: BG✓– – BG Excluded as BG: demonstrates
Action Output criterion excludes
pure prediction
FinGPT Wang
et al. (2023a)
W: “LLM
Tool”, D:
“Genera-
tion”
Arch: Text Perception+Static Memory; Cap: BG (no closed-loop);
Adapt: BG
✓ ✓– BG Excluded as BG: Generation
without execution integration
FinLlama
Iacovides et al.
(2024)
D: “Senti-
ment”
Arch: Text Perception; Cap: BG; Adapt: BG✓– – BG Same architecture as FinBERT
but instruction-tuned; capability
depends on integration, not just
model
AlphaAgent Tang
et al. (2025)
D: “Multi-
agent”
Arch: Reflective/Strategic hybrid+Episodic Memory; Cap: α; Adapt:
Self-reflection
✓ ✓ ✓SE Multi-agent debate=validation
mechanism for Alpha, not
coordination capability
FinAgent Zhang
et al. (2024)
W: “Multi-
modal”, D:
“Agent”
Arch: Multi-modal P+Episodic M+Reflective R+Microstructure A;
Cap:α(cross-modal); Adapt: ICL
✓ ✓ ✓ICL Core: cross-modal perception-
to-action pipeline, not “multi-
modality”
Alpha2 Xu et al.
(2024a)
B: “Alpha
Mining”
Arch: Working Memory+Strategic Reasoning (MCTS); Cap: α
(evolutionary); Adapt: RL
–✓ ✓RL MCTS is Strategic Reasoning;
evolutionary=search-based
adaptation
RAG-Fintech
Cook et al. (2025)
D: “Re-
trieval”
Arch: Text P+Semantic M (KB)+Reflective R; Cap: α (retrieval-
based); Adapt: ICL
✓ ✓ ✓ICL Retrieval=Memory architecture,
not just augmentation technique
RAPTOR Almon
et al. (2025)
D: “Portfo-
lio”
Arch: Working M+Strategic R+Execution A; Cap: P (hierarchical);
Adapt: ICL
–✓ ✓ICL Portfolio=Strategic+Execution
integration, not separate
capability
AgentGuard Chen
and Cong (2025)
W: “Safety” Arch: Reactive R+Action A with gating; Cap: R (real-time); Adapt:
Rule-based
– –✓– Risk as gating mechanism in
Action architecture, not post-hoc
FinRS Liu and
Dang (2025b)
D: “Risk” Arch: Text P+Episodic M+Reflective R; Cap: R (risk-sensitive);
Adapt: Reward reflection
✓ ✓ ✓ICL Risk capability derives from
Perception-Memory-Reasoning
chain
TradingAgents
Xiao et al. (2024)
W: “Multi-
agent”
Arch: Hierarchical role-based Coordination; Cap: α+P+R distributed;
Adapt: Hierarchical feedback
✓ ✓ ✓ ICL+
SE
Analyst, research, trader, risk,
and manager teams form a
decision hierarchy
TradingGroup
Tian et al. (2025)
D: “Multi-
agent”
Arch: Role-based+Shared Memory; Cap:α; Adapt: Self-reflection✓ ✓ ✓SE Self-reflection coordinates roles,
not external mechanism
FINCON Yu et al.
(2024)
D: “Consen-
sus”
Arch: Role-based+Communication Protocol; Cap: P; Adapt: CVRF
belief updates
✓–✓ICL CVRF updates investment beliefs
across episodes
FinMem Yu et al.
(2023b)
W: “Mem-
ory”
Arch: Working M+Layered long-term M+Strategic R; Cap: P; Adapt:
Memory consolidation
–✓ ✓SE Memory hierarchy enables
temporal abstraction for Portfolio
MetaGPT Hong
et al. (2024)
W: “Multi-
agent”
Arch: Hierarchical (Manager+Engineers); Cap: BG (software
engineering); Adapt: SOP-guided prompting
✓ ✓ ✓– General workflow design; no
evaluated trading capability
FinRL-DeepSeek
Benhenda (2025)
B: “RL Trad-
ing”
Arch: Working M+Reactive/Strategic hybrid R+Execution A; Cap:
α+P; Adapt: RL
–✓ ✓RL RL spans multiple capabilities
with shared architecture
Reflexion Shinn
et al. (2023)
W: “Reflec-
tion”
Arch: Working+Episodic M+Reflective R; Cap: BG (general);
Adapt: Self-reflection
–✓ ✓SE Self-reflection as adaptation
mechanism applicable to trading
Hashimoto
Hashimoto et al.
(2025)
B: “Simula-
tion”
Arch: Market Ecology (no central coordination); Cap: α+P+R
emergent; Adapt: Evolutionary
✓ ✓ ✓ RL+
SE
Ecology=emergent capabilities
from interaction, not design
FinEvo Zou et al.
(2026)
D: “Evolu-
tion”
Arch: Market Ecology+Hierarchical; Cap: α; Adapt: Evolutionary+
SE
✓ ✓ ✓SE Combines ecology (interaction)
with hierarchy (structure)
Prior-column shorthand: W=Wang et al. 2024 (LLM-Agent Survey); D=Ding et al. 2024 (LLM-Finance Survey); B=task-centric benchmark (FinBen,
InvestorBench). Where a work was not explicitly labeled in those sources, the shorthand is our closest reconstruction of how it would map to the earlier scheme.
P/M/R mark the Perception–Memory–Reasoning architectural components.
E1 No Action Output: Pure prediction or analysis systems
that do not generate tradable actions. Finance-relevant
examples remain included as background.
E2 No Eligible Empirical Evaluation: Finance-relevant
studies without a qualifying backtest, simulation, live-
trading, or benchmark evaluation. Narrative-only or
unclear evaluation reports remain background/context
even when action output and a closed-loop claim are coded
present.
E3 Non-Financial Domain: Systems applied to non-financial
markets or generic agent settings without financial trading,
portfolio, execution, or risk-management instantiation.
58

Table D.27:Representative final exclusions and background boundary cases.
Study (Representative) Category Decision rationale
Final excluded records in the current canonical registry
Socio-Agentic LLMs for
Socio-Technical Systems
E3 Generic socio-technical agent paper outside finance/trading/portfolio/risk management.
Learning Game-Playing
Agents with Generative
Code Optimization
E3 General game-playing agent study without financial-market instantiation.
NeSyCoCo E3 Neuro-symbolic compositional generalization study outside the trading domain.
Agentic AI for Commer-
cial Insurance Underwrit-
ing
E3 Insurance underwriting rather than trading, portfolio construction, execution, or market-risk management.
Included background boundary cases
FinBERT (Araci 2019) E1/BG Finance-relevant sentiment model retained as background; no tradable action loop, so it is excluded from the
primary empirical subset.
FinGPT (Wang 2023a) E1/BG Finance language-model/tooling work retained as background; no explicit closed-loop trading execution
integration.
InvestorBench E1/BG Finance benchmark retained as background; the registry codes no tradable action output, so it does not enter
the primary empirical subset.
Candidate
registry
(n =246)
Deduplicated
(n =246)
0 removed
Finance/trading
domain?
Included ledger
(n =185)
Outside scope
(n =61)
Action Output
+Closed-Loop
+Eligible
Evaluation Type?
Primary
empirical
(n =80)
Background
(n =105)
Yes
No
Yes
No
Figure D.17:Inclusion, exclusion, and evidence-tier decision flow. Final exclusions are outside the survey domain; finance-relevant records that
fail Action Output, Closed-Loop Evaluation, or the eligible empirical evaluation-type rule remain in the included background tier.
These form the final excluded set in the current canonical
registry.
E4 No LLM Component: Traditional quantitative trading
systems without a language-model component. These
may be cited only as background context when needed for
finance methodology.
E5 Duplicate: Multiple versions of the same work; the most
complete version is retained.
E6 Inaccessible: Full text unavailable after retrieval attempts.
Appendix D.2. Examples of Final Exclusions and Background
Cases
Table D.27 separates final exclusions from background boundary
cases. The aggregate exclusion count in the current canonical
registry is 61, all of which are outside the finance/trading scope;
the background cases remain in the 185-record included ledger
but do not enter the 80-record primary empirical subset. Under
the current boundary, the 102 included records taggedprimary
in S0 v2 include 22 narrative-only records; these are assigned to
the background denominator, yielding 80 empirical primary and
105 background records.
Appendix D.3. Inclusion/Exclusion Decision Flow
Figure D.17 illustrates the screening logic encoded in the
canonical ledger and summarized in the main text, making the
inclusion/exclusion workflow traceable.
Appendix D.4. Impact of Exclusion Criteria on Evidence Set
After deduplication, all 61 final exclusions fall outside the
survey domain. Finance-relevant records failing the three-part
empirical criterion remain background/context. Reassigning 22
narrative-only studies among 102primary-tagged records
yields 80 empirical primary and 105 background studies. Table 3
reports these macro-backed categories, rather than earlier
screening-log totals.
59
