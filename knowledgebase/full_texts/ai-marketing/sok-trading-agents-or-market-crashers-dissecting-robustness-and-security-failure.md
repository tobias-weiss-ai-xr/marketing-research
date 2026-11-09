---
title: 'SoK: Trading Agents or Market Crashers? Dissecting Robustness and Security Failures in Academic
  Financial LLM Trading Schemes'
url: https://arxiv.org/abs/2609.19705
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Mengxiao Wang
- Nitesh Saxena
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.19705
pages: 57
chars: 280726
fetched_at: '2026-11-08T13:20:35+00:00'
kb_version: 1
---

# SoK: Trading Agents or Market Crashers? Dissecting Robustness and Security Failures in Academic Financial LLM Trading Schemes

Trading Agents or Market Crashers? Dissecting Robustness and Security Failures
in Academic Financial LLM Trading Schemes
Mengxiao Wang
Texas A&M University
jacksonwang@tamu.edu
Nitesh Saxena
Texas A&M University
nsaxena@tamu.edu
Abstract
Large language model (LLM) agents already trade real cap-
ital, and builders copy a few published designs that share
models and news feeds, so one shock reaches many agents at
once. We present FARSIGHT (Financial Agent Robustness
and Security Investigation and Global Holistic Taxonomy), a
systematization that rates trading agents on robustness to mar-
ket stress and on security against source manipulation, agent
compromise, and agents acting as attackers, and checks the rat-
ings against released code. Across 15 academic schemes, no
paper describes a halt that skips LLM inference or combines
source provenance with cross-source corroboration, and the
7 code releases enforce no stop-loss or position limit outside
the LLM. Three LLMs sell whole positions on a fake headline
and on real hoaxes, including the fake press release behind the
2000 Emulex crash. In a simulated market driven by these de-
cisions, one fake headline crashes the market in all runs with
400 agents, and 400 agents that sell when prices fall nearly
double a 2010-sized crash. The pause that U.S. exchanges
apply to large stocks starts in no headline run, whereas au-
tomatic halts and hard loss limits outside the model remove
both effects. Restated as a domain-independent threat model,
FARSIGHT maps the same gaps onto agents in healthcare,
law, software, and crypto, where compromised agents spread
harm as worms and as cascades. We derive 14 open problems
and urge deployers to corroborate sources, keep interrupts
that bypass the model, and enforce loss limits outside it.
1 Introduction
Autonomous large language model (LLM) agents increas-
ingly invoke tools, move data, and take consequential actions,
and their security is now a serious concern. Recent systemati-
zations [1,2] map agentic-AI attacks and defenses at large, but
their domain-agnostic treatments cannot capture what changes
once an agent operates in ahigh-stakesdomain. Financial
markets [3] are the sharpest such setting: actions are finan-
cially irreversible, adversaries are directly profit-motivated,
and one agent’s output instantly becomes another’s input.Fi-
nancial LLM agents[4] already manage real capital (e.g.,
RockAlpha [5], Composer [6]) and serve retail users (e.g.,
Robinhood [7], Nof1.ai [8]), and because financial systems
can themselves be weaponized [9, 10], a compromised agent
could pass its errors on to other market participants. This is
no longer a research-only concern. In mid-2026 the Bank of
England warned publicly that autonomous AI agents could
trigger a market meltdown [11], and a Wolters Kluwer survey
found that 72% of U.S. banks lack AI-model kill switches or
failure-reporting protocols [12]. U.S. legislators have already
escalated. In June 2026, House Financial Services Democrats
sent SEC Chair Atkins 13 questions on “correlated trading
decisions” and “herding behavior” by AI trading agents on
registered brokerages [13].
As Figure 1 shows, the systems we study follow recent
multi-role designs [14–17]: analyst, researcher, manager, and
trader agents that jointly process market data and execute
trades. Yet their behavior under extreme conditions is un-
derexplored, even though minor algorithmic reactions can
cascade, as in the 2010 Flash Crash that briefly erased nearly
one trillion dollars [18–20], and compromising even a small
subset of the deployed LLM trading agents (e.g., the more
than 150,000 agentic trading accounts that Robinhood re-
ported by September 2026 [7, 21]) could deliberately induce
the same effect through small perturbations in low-liquidity
stocks. This scale of impact, where a fleet of compromised
agents can destabilize an entire market, does not appear in
the single-session threat models that generic agentic-security
studies assume. Recent work further shows that LLM trad-
ing agents systematically inherit and amplify herding, which
can amplify flash crashes [22]. This gap frames our central
goal, which isto measure and ensure that financial LLM
agents remain stable under normal market conditions and
resilient under adversarial ones.We approach it in two steps,
a scheme-level assessment of published trading-agent designs
that maps their attack surface before defenses are designed,
and a simulated market that measures the cost of the missing
controls once many agents trade together. A systematization
1
arXiv:2609.19705v3  [cs.CR]  25 Oct 2026

Figure 1: Overview of threat surfaces in financial LLM agent ecosystems. S1 denotes attacks on market-relevant information
sources (e.g., data or news manipulation) that indirectly influence agent decisions; S2 represents direct attacks on LLM trading
agents (e.g., prompt injection or model poisoning); and S3 captures scenarios where compromised agents act as attackers
themselves: after being influenced via S1 or S2, they inject small perturbations into trading behaviors, which can propagate
through market participants (bots, human traders, and market makers), collectively amplifying reactions and potentially triggering
large-scale sell-offs or flash crashes. In addition to these security threat surfaces, our robustness assessment (R1–R4) evaluates
whether agents can foresee market turbulence, react rapidly to shocks, contain cascading losses, and recover after stress events,
reflecting the inherent risks of operating in volatile financial environments.
fits this stage because deployment has run ahead of research.
Products already let agents trade for retail users, and the most
widely used academic design has over 100k GitHub stars,
yet no common security standard has been applied to these
designs.
Answering it starts with what makes these agents dif-
ferent. Their attacks tend to share five traits: they areIn-
stantandInconspicuous, rely onUnverifiedinputs, remain
Adaptiveacross channels, and can set offCascadingef-
fects across the market. Generic prompt-injection and jail-
break taxonomies do not model this combination, which our
framework is designed to capture. We propose the FAR-
SIGHT (Financial Agent Robustness and Security Investi-
gation and Global Holistic Taxonomy) framework to sys-
tematize agents along robustness and security. Unlike agent-
security SoKs [1, 2], which are domain-agnostic, and surveys
of financial agents [4, 22], which catalog capabilities, FAR-
SIGHT rates every published design against one codebook
that treats market-stress robustness as a security property, and
it checks these ratings against the released code. Robustness
is measured through four metrics:crash foresight,reaction,
loss containment, andrecovery. As shown in Figure 1, secu-
rity includes three metrics:S1(attacks on market-relevant
information sources),S2(attacks on agent logic and prompts,
including prompt-injection, tool/Application Programming
Interface (API) exploitation, and memory manipulation), and
S3(agent-as-attacker behavior).
Across the 15 schemes, robustness and security controls
are largely missing by design. Twelve of the 15 (80%) re-
ceive no credit on at least one of the four robustness metrics.
No paper describes a way to interrupt trading without wait-
ing for LLM inference (R2), and none describes both source
provenance and cross-source corroboration before acting on
a signal (S1). The released code of the 7 schemes that pub-
lish it adds a second view. None of these releases contains
an order-execution path or enforces a stop-loss or position
limit outside the LLM, 2 run model-written code on the host
without a sandbox, and 4 lack a component that their paper
or documentation describes, such as QuantAgent’s risk agent
(§6.3). The recurring failures show that data, tools, and mem-
ory are attack surfaces, so safety must rest on cross-validated
information, pre-committed limits, and containment that sit
outside the model. The adversary here is financially motivated
and the agent holds real execution authority, so once such an
agent is deployed, a single planted feed or hijacked tool could
move real capital. Robustness here is itself a security concern.
In a reflexive, zero-sum market, an attacker can deliberately
trigger the shock that a non-robust agent mishandles, so ro-
bustness and security cannot be assessed apart.
Ratings alone cannot show the cost of these gaps, because
the harm appears once many agents trade the same stock. We
therefore measure how three LLMs, gpt-5.6-luna, deepseek-
v4-flash, and gemini-3.5-flash, trade one position, and we let
hundreds of agents that decide as they do trade in a simulated
market (§7). All three models sell the whole position after
one fake headline and after the fake press release that cost
Emulex $2.2 billion in 16 minutes in 2000 [23].
As Figure 8 shows, the headline then crashes the market in
2

all runs with 400 agents, because each agent sells its whole
position in one order and the orders of all agents arrive within
one decision cycle. Without any attacker, 400 agents whose
model sells when prices fall deepen a 2010-sized crash from
9.2% to 17.3%. Limit Up-Limit Down, the trading pause of
U.S. exchanges [24], starts in 0 of 300 headline runs, whereas
a fast path that freezes orders without an LLM call (R2) and
hard loss limits outside the model (R3) remove both effects
(Table 9).
More broadly, financial trading agents are a sharp instance
ofhigh-stakes agentic security, because every property that
makes a compromised agent costly, from irreversible actions
to coupling with other actors, is at its maximum in mar-
kets. The missing controls recur outside finance. Restated
as domain-independent properties, the FARSIGHT surfaces
map onto clinical, legal, software, and crypto agents (§9),
and S3 ties agent security to market cascades and computer
worms (§10). Options agents raise every stake further (§12.1).
With published injection rates, a channel that ten agents read
lets one compromised agent start an outbreak even against the
frontier model that best resists indirect injection in LivePI [25].
To our knowledge, ours is the first work to jointly systematize
market robustness and security for the academic trading-agent
literature and to measure, with LLM decisions in a simulated
market, what the missing controls cost.
Our Contributions:Our main contributions are outlined
below:
1.F ARSIGHT: A Scheme-Level Framework for High-Stakes
Agentic Security.We present FARSIGHT, a systematization
methodology (not a benchmark suite) that rates financial LLM
agents on both robustness and security via a reproducible
codebook (Appendix A), with dedicated threat models for the
execution-authority, reflexive, and zero-sum conditions that
make these agents high-stakes.
2.Characterizing the Unique Attack Surface of Financial
Trading Agents.We systematically categorize financial LLM
agents and identify five defining traits (Instant,Inconspicuous,
Unverified,Adaptive,Cascading) that widen their exposure
and separate them from agents in law, healthcare, or educa-
tion.
3.Systematic Robustness and Security Assessment of 15
Trading Schemes.Applying FARSIGHT (codebook in Ap-
pendix B) to 15 representative schemes, we find that 12 of the
15 (80%) receive no credit on at least one robustness metric
and that none earns full credit on S1 or R2. A parallel LLM-
based assessment disagreed with ours on 53% of metric-level
judgments (Appendix G), so fine-grained scoring still requires
human expertise. We further audit the released code of the 7
open-source schemes in three independent runs and find that
code-level and paper-level ratings agree on 39 of 63 ratings,
with gaps in both directions (§6.3).
4.Measuring What the Missing Controls Cost.We show that
three LLMs sell whole positions on a fake headline and on
hoaxes that moved real markets, that a few hundred agents
that decide as they do cause and amplify flash crashes in a
simulated market that the exchange pause misses, and that
the fast path and hard limits remove both effects across 15
robustness settings (§7).
5.Lessons Beyond Trading and a Research Agenda.We
restate FARSIGHT as a domain-independent threat model,
rate seven high-stakes domains on what makes their agents
dangerous, classify six channels through which agents propa-
gate harm, including agent worms, derive 14 open problems
(§9–§11), and show why options agents are more dangerous
(§12.1).
Relevance to Security.Each FARSIGHT metric maps to a
systems-security question with an established USENIX, S&P,
or CCS literature on non-financial substrates: source poison-
ing (S1), prompt, tool, and memory compromise (S2), agent-
as-attacker containment (S3), and incident response under
adversarial stress (R1–R4) [26–31]. Like prior security SoKs
that systematize artifacts from adjacent communities [32],
we carry this literature into a high-stakes domain that the
domain-agnostic SoKs [1, 2] leave out.
2 Background
Large language models and LLM agents.Large Lan-
guage Models are transformer-based neural architectures [33]
trained on large text corpora to capture linguistic and fac-
tual patterns. Through large-scale pretraining, they general-
ize across diverse language tasks, achieving state-of-the-art
performance in reasoning, summarization, and generation.
Representative models include GPT-4 [34], LLaMA [35],
Mixtral [36], and Claude [37]. Safety and alignment are typ-
ically enhanced via supervised fine-tuning and Reinforce-
ment Learning from Human Feedback (RLHF) [38], while
Retrieval-Augmented Generation (RAG) [39] improves fac-
tual grounding. Building on these foundations,LLM agentsex-
tend pretrained models with capabilities for autonomous rea-
soning, planning, and environment interaction. Unlike static
LLMs, agents iteratively reason, act, and observe outcomes
through feedback loops [40, 41], integrating modules such as
planning,memory, andtool use[42, 43]. Modern frameworks
(e.g., LangChain, AutoGPT, ReAct) enable multi-step task
execution, including web searches, code execution, and data
analysis.
Financial LLM agents.Ding et al. [4] define afinancial
LLM agent, often instantiated as anLLM trading agent, as
an autonomous system that leverages large language model
reasoning for trading tasks such as market prediction, portfo-
lio optimization, and risk assessment. These agents integrate
LLMs with financial data streams, market simulators, and trad-
ing APIs to enable data-driven investment decisions [44–46].
Unlike conventional algorithmic trading systems, they ex-
hibit adaptability and contextual understanding through nat-
ural language processing, supporting applications such as
3

🕮 1
Collect
127 candidate papers,
40 read in full, 15
schemes selected (§5)
♂list-ul 2
Codebook
9 metrics, 33 binary
indicators, determinis-
tic rules (App. B)
/user-check 3
Rate papers
Two experts, 135 rat-
ings, Cohen’s κ=0.89
(Table 5)
/code 4
Audit code
7 releases, 3 LLM
runs each, pattern
scan (§6.3)
/tools 5
Recommend
Controls outside the
model, mapped to
Rule 15c3-5 and
RTS 6 (§8)
/gl⌢be-americas 6
Generalize
Other domains, cas-
cades and worms, 14
open problems (§9–
§11)
♂robot LLM-based assessment, comparison only:
disagrees with the experts on 24 of 45 cells
(App. G)
Figure 2: Overview of the FARSIGHT pipeline. Two human experts assign the paper-level ratings, an LLM-based assessment
serves only as a comparison, and three independent audit runs check the ratings of the seven open-source schemes against their
code. Sections 9–11 carry the findings beyond trading.
sentiment-based forecasting [47], portfolio construction [48],
high-frequency trading (HFT) [49], and multi-agent risk man-
agement [50]. Recent work further explores contest-based
reinforcement [51] and decision auditing in investment man-
agement [45]. Two main paradigms have emerged:Trader
Agents, which execute buy, hold, or sell decisions [14, 15, 52],
andAlpha Miner Agents, which identify predictive signals (al-
phas) from textual and quantitative data [53]. In practice, Al-
pha Miners often serve as signal generators for Trader Agents,
and we treat them as a functional subset in this study.
3 Related Work and Positioning
Six bodies of work surround this paper: surveys of financial
LLM agents, security systematizations of LLM agents, attacks
on trading agents, studies of correlated LLM decisions and
simulated markets, studies of propagation among agents, and
agent security in other high-stakes domains. Table 1 positions
FARSIGHT against representative studies of each along six
dimensions: whether a study targets trading agents, builds a
security threat model, treats robustness under market stress,
considers spillover from compromised agents to other agents
or the market, assesses each studied system against explicit
criteria, and examines released code.
Surveys of financial LLM agents.Surveys of LLM agents
in trading and finance catalog architectures, data inputs, tasks,
benchmarks, and backtest performance [4,45,46,54,55]. They
describe what trading agents can do, and security appears in
them at most as a deployment challenge. Two recent surveys
go further. Xia et al. note that open-web memory can be poi-
soned and call for deterministic risk guardrails [22], and Gong
discusses the systemic implications of agent adoption in finan-
cial markets [56]. Neither defines a threat model or assesses
individual systems against security criteria. In contrast, FAR-
SIGHT turns these concerns into a threat model with three
attack surfaces and four robustness phases, and it rates each
of 15 schemes against them.
Security systematizations of LLM agents.Agent-security
systematizations map attacks and defenses for LLM agents in
general [1, 2, 76]. They are deliberately domain-agnostic, and
their threat models do not capture an agent that holds execu-
tion authority over capital in a reflexive market, where one
agent’s output becomes another’s input. Newer backbones do
not retire these attacks, because indirect prompt injection still
succeeds against GPT-5-class, Claude 4.x, and Gemini 3.x
models [25, 77]. Closer to finance, Zeng et al. organize seven-
teen attack subtypes across the lifecycle of financial AI, from
data poisoning to prompt injection and deepfake fraud against
identity checks [57], and Mao et al. systematize the security of
agents in agentic commerce, including payment, negotiation,
and market-manipulation risks [58]. Both work at the level of
model lifecycles or commerce protocols, above the level of
concrete trading agents, and neither treats robustness under
market stress. In contrast, FARSIGHT adds a robustness axis
with no direct analogue in these works (crash foresight, shock
reaction, loss containment, and recovery) and instantiates the
security axis with the two surfaces that are specific to trad-
ing: manipulation of market-relevant information (S1) and
compromised agents that act on the market (S3).
Attacks on trading agents.A growing line of empirical work
attacks trading agents directly. Rizvani et al. show that adver-
sarial news headlines cut the profit of an LLM-driven trading
system [59], Liu et al. generate finance-specific misinforma-
tion that misleads trading agents [60], Na et al. poison the
inputs of four multi-agent trading architectures through role-
specific adversaries [61], Sua et al. trace how poisoned social-
media posts spread inside multi-agent trading stacks [62], and
Yan et al. perturb four components of two classes of trading
agents in backtests [63]. Each study tests one or a few attack
surfaces on one or a few systems, most often the information
surface. These results show that the attacks we systematize are
practical. Our systematization complements them by showing
how widely the corresponding controls are missing across 15
published schemes and in their released code (§6.3).
Correlated decisions and simulated markets.Correlation
turns the errors of single agents into a market problem. Reg-
4

Table 1: Positioning of FARSIGHT against representative related work.✓: a central part of the study; ∼: discussed, or limited to
one attack surface or a few systems; –: not covered. Rob. = robustness under market stress; Spillover = harm that spreads from a
compromised agent to other agents or the market; Per-system = each studied system is assessed against explicit criteria; Code =
released implementations are checked against the published designs.
Group Study Type Trading agents Threat model Rob. Spillover Per-system Code
Surveys of
financial
LLM agents
Ding et al. [4] Survey✓– – – – –
Dong et al. [54] Survey∼ ∼–∼– –
Saha et al. [45] Survey∼–∼– – –
Mahdavi et al. [46] Survey∼– – – – –
Hua et al. [55] Survey✓– – – – –
Xia et al. [22] Survey✓∼ ∼ ∼– –
Gong [56] Survey∼– –∼– –
Security
systematizations
Kim et al. [1] SoK –✓– – – –
Raza et al. [2] Survey –✓∼– – –
Zeng et al. [57] Survey∼✓∼ ∼– –
Mao et al. [58] SoK∼✓–∼– –
Attacks on
trading agents
Rizvani et al. [59] Attack✓∼– –∼–
Liu et al. [60] Attack✓∼– –∼–
Na et al. [61] Attack✓∼– –∼–
Sua et al. [62] Attack✓∼ ∼–∼–
Yan et al. [63] Benchmark✓∼ ∼–∼–
Correlation and
market simulation
Apte [64] Stress test✓–∼ ∼– –
Lopez-Lira [44] Simulation✓– –∼– –
Ross et al. [65] Simulation✓∼–✓– –
Propagation
among agents
Schroeder de Witt et al. [66] Agenda –✓–✓– –
Hammond et al. [67] Report –∼–✓– –
Cohen et al. [68] Attack –✓–✓∼–
Gu et al. [69] Attack –✓–✓– –
Lee and Tiwari [70] Attack –✓–✓– –
Triedman et al. [71] Attack –✓–∼✓∼
Other
high-stakes
domains
Alber et al. [72] Attack –✓– – – –
Clusmann et al. [73] Attack –✓– –∼–
Magesh et al. [74] Measurement – – – –✓–
Patlan et al. [75] Attack∼✓– –∼ ∼
This work Rating + simulation✓ ✓ ✓ ✓ ✓ ✓
ulators and economists warn that common models and data
sources produce correlated behavior and that AI can amplify
procyclicality [78–80], and measurements now find this corre-
lation in LLMs. Their errors are correlated across models [81],
shared prompts concentrate the actions of LLM trading agents
in a microstructure stress test [64], stock-price predictions
covary across eight LLMs [82], and ten preference-tuned
forecasters in a prediction market are worth about 1.4 inde-
pendent ones [83]. Ross et al. show that LLM traders that
read the same misleading commentary misprice together in
a simulated market, where more capable models act more
alike [65], and Ng sorts AI-driven flash crashes into herding,
error-cascade, and disinformation crashes [84]. Agent-based
market models study such instability with fundamentalist and
trend-following traders [85], support the leading explanation
of the 2010 Flash Crash [86], and show that fake news lowers
prices [87]. Recent versions use LLM traders [44], which
form bubbles on a simulated social network [88] and switch
trading styles only partly as behavioral finance predicts [89].
These works measure correlated decisions, classify crashes,
or simulate traders. In contrast, we feed measured LLM deci-
sions into such a market, find the number of agents at which
correlation becomes a crash, and test the controls that market
rules require and that no rated design implements (§7).
Propagation among agents.Research agendas for multi-
agent security taxonomize the threats that emerge when agents
interact, including secret collusion, swarm attacks, and the
spread of jailbreaks and poisoned data through network ef-
fects [66, 67]. Attack studies have made propagation concrete.
Self-replicating prompts spread through RAG-based email
assistants [68] and through multi-agent systems [70], one
adversarial image jailbreaks a population of up to one mil-
lion agents exponentially fast [69], adversarial content hijacks
multi-agent frameworks into executing arbitrary code [71],
5

and network topology shapes how far attacks spread [90, 91].
These studies examine agents that infect one another through
messages. In contrast, we connect propagation to markets,
where harm also spreads without compromise through the
prices that every agent reads, and we use published per-hop
success rates to estimate when a single compromised agent
can start an outbreak (§10).
Agent security in other high-stakes domains.Domain stud-
ies document the same surfaces one domain at a time. Med-
ical models can be poisoned through a tiny fraction of their
training data [72] or their weights [92], and medical vision-
language models follow instructions hidden in images [73].
General-purpose models and commercial legal research tools
still invent legal facts and citations [74,93]. Memory injection
steers Web3 agents into unauthorized asset transfers [75], and
autonomous science agents raise safety risks that call for safe-
guards over autonomy [94]. Each study covers one domain
and mostly one surface. In contrast, Section 9 maps all FAR-
SIGHT surfaces and resilience phases onto seven domains
and rates them on the properties that make trading agents
dangerous.
Differences from prior work.FARSIGHT differs from all
six bodies of work along six dimensions at once. First, it tar-
gets trading agents specifically, unlike the domain-agnostic
agent systematizations [1,2] and the finance-wide surveys [54,
57]. Second, it builds a security threat model with three at-
tack surfaces, which the capability surveys [4, 45, 46, 55] lack.
Third, it treats robustness under market stress (crash foresight,
shock reaction, loss containment, and recovery) as a security
property, which none of the other works covers as a central
part. Fourth, it covers spillover from compromised agents to
the market (S3), whereas the trading attack studies measure
harm to the attacked agent’s own decisions or, at most, propa-
gation inside one multi-agent stack [62], and the propagation
studies stop at agents that infect one another. We also measure
this spillover, with three LLMs’ decisions in a simulated mar-
ket, where the simulation studies above measure correlation
but not the controls that would stop it. Fifth, it rates every
one of 15 schemes against the same deterministic codebook,
whereas each attack study tests one or a few systems. Sixth,
it checks these ratings against the released code of the seven
open-source schemes, which no other work in Table 1 does as
a central part. Beyond the six dimensions, this version carries
the framework to other high-stakes domains and to cascades
between agents (§9–§11). To our knowledge, FARSIGHT
is the first systematization of academic trading agents that
combines all six.
4 Our FARSIGHT Framework
This section introduces our FARSIGHT (Financial Agent
Robustness and Security Investigation and Global Holistic
Taxonomy) framework, a structured methodology for system-
atizing the robustness and security of financial LLM agents.
FARSIGHT is ascheme-level assessment framework: each
system is scored as ascheme, the design described in its pub-
lished paper, not as a running instance. It is not a benchmark
suite with fixed datasets and automated test harnesses. It pro-
vides structured criteria, a codebook-based scoring methodol-
ogy, and a reproducible assessment pipeline for expert review
of agent architectures. This design choice reflects the hetero-
geneity of financial LLM agents: their diverse architectures,
data sources, and deployment contexts make a single standard-
ized benchmark insufficient for capturing the full spectrum of
robustness and security concerns. To ensure replicability and
transparency, we include a detailedcodebookoutlining the
coding scheme, metric definitions, and annotation examples
in Appendix B.
4.1 Workflow of FARSIGHT
Inspired by the SoK methodology presented by Akanda et
al. [95], we developed FARSIGHT to assess the state of fi-
nancial LLM agents through literature-grounded assessment
and metric-based analysis. Unlike prior frameworks that fo-
cus on implementation toolkits (e.g., LangChain, AutoGPT,
ReAct) or benchmarking tasks (e.g., AgentDojo [96], Stock-
Bench [97]), FARSIGHT introduces a unified and repro-
ducible assessment pipeline that emphasizes robustness and
security as primary concerns.
Section 3 positions FARSIGHT against surveys of financial
LLM agents, security systematizations of LLM agents, and
attacks on trading agents.
As shown in Figure 2, our study follows the FARSIGHT
framework to assess the robustness and security of financial
LLM agents. We began by collecting a comprehensive corpus
of academic works and real-world products related to financial
LLM agents. From this corpus, we filtered and selected those
directly relevant to trading and market-interacting systems,
specifically agents that autonomously or semi-autonomously
perform financial analysis, strategy generation, or trade exe-
cution. Each selected work was analyzed as aninstantiated
trading agent, forming the foundation of our systematization.
Based on this dataset, FARSIGHT introduces two cate-
gories of metrics: (i)Robustness Metrics, which measure
an agent’s capacity to maintain operational stability under
volatile or flash-crash-like conditions, and (ii)Security Met-
rics, which assess resilience against three major threat di-
mensions:attacks on the information environment,attacks
on agents, andagent-as-attackerbehaviors. The framework
translates these metrics into a systematic assessment process
that runs from literature collection through codebook-based
rating to insight generation. We applied these metrics to 15
representative financial LLM agents, identifying common
design weaknesses, overlooked risks, and insufficient con-
sideration of real-world adversarial conditions. Our findings
show that most existing systems fail to anticipate the impact
of extreme market turbulence or targeted manipulation, leav-
6

ing users and markets vulnerable to cascading financial losses.
Finally, FARSIGHT provides actionable recommendations
for building more robust and secure financial LLM agents,
with robustness and security built in from the design stage.
4.2 Robustness Metrics
Robustness in FARSIGHT refers to a financial LLM agent’s
ability to maintain stable, safe, and rational behavior under
sudden and extreme market disruptions (e.g., flash crashes,
black swan events). We note that market volatility and price
corrections are not inherently undesirable: classical economic
theory recognizes rapid price adjustment as a feature of ef-
ficient markets [98]. Our robustness metrics do not target
market volatilityper se, but ratheragent-amplified instabil-
ity: scenarios where LLM agents, through delayed reaction,
herding behavior, or cascading feedback loops,exacerbate
market disruptions beyond what would occur with human-
only participation. The distinction is between natural price
discovery and artificial destabilization caused by poorly de-
signed autonomous systems [99, 100]. We define four key
robustness metrics that reflect different phases of a market
crisis, from early detection to post-crash recovery. The phases
mirror the incident-handling functions of the NIST Cyberse-
curity Framework 2.0 [101]: R1 maps to Detect, R2 and R3
map to Respond (R3 to its containment of incidents), and R4
maps to Recover.
R1. Crash Foresight and Early Awareness.This metric as-
sesses whether an agent can anticipate extreme market volatil-
ity or potential crashes in advance by identifying anomalous
signals (e.g., spikes in the Chicago Board Options Exchange
(CBOE) V olatility Index (VIX), correlated asset drops, or
sentiment shifts). It measures the agent’s ability to perform
proactive risk sensing before catastrophic losses occur.
R2. Rapid Reaction Capability under Market Shocks.This
metric evaluates the timeliness and appropriateness of an
agent’s response during sudden market disruptions. A robust
agent has a pre-committed path that halts risky orders, freezes
trading, or switches to a safe mode without waiting for LLM
inference, with a reaction time matched to the horizon of its
strategy. The reaction time that suffices ranges from below
0.1 ms in high-frequency trading to about 10 s in daily trad-
ing, whereas TradingAgents takes over 240 s per decision
(Table 7).
R3. Loss Containment and Stop-Loss Execution.This met-
ric measures whether an agent can effectively contain losses
and prevent cascading risk once a market crash begins. It
captures the design of automated stop-loss mechanisms, expo-
sure caps, and cool-off intervals that limit systemic damage.
None of the 7 released implementations enforces such a limit
outside the LLM (§6.3).
R4. Recovery and Post-Crash Adaptation.This metric cap-
tures the agent’s ability to recover from an adverse event and
restore stable operation. It considers whether the agent can
rebalance parameters, retrain on updated data, or adaptively
recalibrate its strategy after a market crash.
To ensure reproducibility, each FARSIGHT metric is as-
signed using anevidence-based checklistwith deterministic
scoring rules that leave no room for subjective judgment. We
detail this assignment methodology (together with the inter-
rater agreement between our two independent evaluators) in
Appendix A.
4.3 Security Metrics and Underlying Threat
Models
This section presents the threat models associated with each
security metric in FARSIGHT, outlining the underlying as-
sumptions, adversary capabilities, attack flows, and the secu-
rity properties each metric is intended to assess.
S1: Attacks on Market-Relevant Information Sources.
Threat Model:We assume the financial LLM agent continu-
ously ingests market-relevant information (news feeds, sen-
timent data, social-media signals) without enforcing strong
source authentication, provenance validation, or cross-source
consistency checks. The attacker cannot access or modify the
agent’s internal prompts or model parameters, but can compro-
mise, forge, delay, or selectively manipulate upstream infor-
mation sources that the agent relies on. By controlling these
external data channels, the adversary can shape the agent’s
perception of market conditions and influence its downstream
trading decisions.
Attack Flow / Objective:The attacker first compromises an
external information provider or feed (e.g., a news API, sen-
timent stream, or social media source). Manipulated content
(falsified news, selectively delayed signals, or biased senti-
ment) is then propagated through the agent’s subscribed chan-
nels. The agent ingests these deceptive inputs, integrates them
into its decision-making context, and executes trades or real-
locations based on corrupted market signals. The objective
is to indirectly influence or steer the agent’s trading logic,
causing misinformed actions, adversary-favorable outcomes,
or broader systemic disruption, all without directly compro-
mising the agent itself.
This metric examines whether the agent relies on trusted,
cross-validated information sources and whether it detects
or filters unreliable inputs. In particular, we assess whether
the agent validates news authenticity, aggregates signals
across multiple feeds, or naively consumes highly manip-
ulable sources such as social media, widely recognized as the
easiest channel for coordinated misinformation.
S2: Attacks on Agent Logic and Prompts.
Threat Model:We assume the financial LLM agent operates
in an interactive or API-accessible environment that accepts
external inputs (chat requests, automated trading commands,
tool-invocation APIs) without strict isolation between sys-
tem prompts, user prompts, tool permissions, and persistent
memory. The attacker can send crafted prompts or payloads
7

to the agent, exploiting its instruction-following behavior, its
ability to call tools or APIs, and its capability to write or
retrieve long-term memory. The attacker aims to directly sub-
vert the agent’s decision logic, induce unauthorized financial
actions, or implant persistent malicious context that continues
influencing behavior across sessions.
Attack Flow / Objective:The attack proceeds by injecting
crafted instructions that blend benign content with adversarial
payloads. Once processed by the agent, these injections may
override internal trading constraints, trigger unintended tool
or API calls, or contaminate long-term memory with biased or
adversarial instructions. FARSIGHT decomposes S2 attacks
into the following categories:
• S2.1 Prompt-Injection and Instruction Override:Mali-
cious text manipulates the agent’s reasoning chain or by-
passes predefined trading rules through context hijacking
or instruction override.
• S2.2 Tool-Use and API Exploitation:Compromised rea-
soning leads to unauthorized execution of tools or APIs,
enabling unintended trades, fund movements, or sensitive
data exfiltration.
• S2.3 Memory or Context Manipulation:The attacker
injects persistent malicious content into memory, causing
long-lived bias or harmful strategy drift that survives resets
or retraining cycles.
This metric evaluates whether the agent enforces prompt
isolation, input sanitization, tool-use sandboxing, API permis-
sion boundaries, and memory-integrity protections, critical
safeguards required to prevent direct logic-layer compromise.
S3: Agent-as-Attacker Behavior.
Threat Model:We assume that one or more financial LLM
agents have already been compromised through S1 or S2 and
continue to operate in a multi-agent or market-simulation en-
vironment where other agents trust their outputs. The attacker
fully controls these compromised agents and can use them
to autonomously generate misinformation, propagate mali-
cious prompts, or execute manipulative trades. The attacker
aims to exploit the compromised agent’s trusted role to in-
fluence broader market dynamics and induce cascading or
destabilizing effects.
Attack Flow / Objective:A compromised agent behaves as
an active adversary rather than a passive victim. It may dis-
seminate false signals, coordinate harmful trades with other
controlled agents, or manipulate liquidity or volatility to trig-
ger cascading reactions. Because financial agents often treat
peer outputs as actionable signals, a single compromised agent
can rapidly propagate harmful behavior across the ecosystem.
The attacker’s objective is to amplify systemic volatility, trig-
ger coordinated sell-offs or flash-crash-like events, or exploit
arbitrage gaps created by the disruption.
This metric evaluates whether the system can detect mali-
cious coordination, isolate compromised agents, and contain
cascading impacts across interconnected agent networks, crit-
ical safeguards for preventing ecosystem-wide failures. It
rates whether these controls are present, not whether the rated
schemes have caused spillover.
Trading-specific changes.Table 2 states, for each surface,
what changes once the agent trades. Two changes recur: the
market pays the adversary, because a pre-positioned trade
turns a manipulated decision into profit, and the harm is irre-
versible, because an executed order settles before any human
review.
5 Financial LLM Agent Selection and Catego-
rization
This section presents our approach to identifying, collecting,
and categorizing financial LLM agents. We describe the paper
selection criteria and dataset construction, then propose a
taxonomy that classifies agents by architecture, functionality,
and evaluation purpose, highlighting the traits that distinguish
financial LLM agents from other domain-specific systems.
5.1 Paper Collection and Selection Criteria
This study focuses specifically on understanding and system-
atizing attacks targetingfinancial LLM agents, includingfi-
nancial LLM trading agentsandfinance-oriented LLM agents
that employ large language models for market analysis, au-
tonomous trading, or financial decision-making. We followed
a structured selection process inspired by the Preferred Re-
porting Items for Systematic Reviews and Meta-Analyses
(PRISMA) guidelines [111].
Identification.We systematically searched for papers pub-
lished between 2023 and 2026 using keyword queries includ-
ing “financial LLM agents,” “LLM trading agents,” “LLM
autonomous trading,” and “LLM financial decision-making.”
Our search covered publications from theUSENIX Security
Symposium, theNetwork and Distributed System Security
Symposium (NDSS), theACM Conference on Computer and
Communications Security (CCS), theIEEE Symposium on
Security and Privacy (IEEE S&P), theConference on Neural
Information Processing Systems (NeurIPS), and theInterna-
tional Conference on Machine Learning (ICML), as well as
relevant preprints on arXiv. We also performed backward and
forward citation snowballing on highly relevant papers to cap-
ture additional works not returned by keyword search. We
targeted these venues because they publish the security and
ML work that our framework builds on, and arXiv because
most trading-agent systems first appear there. Snowballing
added systems published elsewhere, such as FinAgent (KDD)
and FLAG-Trader (ACL). The corpus therefore omits some
trading agents that appear only in NLP, data-mining, or fi-
nance venues, such as HedgeAgents [50], CryptoTrade [112],
and FinVision [113]. They reuse paradigms already in Table 3
(multi-agent collaboration, reflective memory, and multimodal
8

Table 2: Generic agent threats and their instantiation in trading agents. The last column states what the trading setting changes
relative to the generic threat.
Surface Generic agent threat Instantiation in trading agents What changes in trading
S1 Indirect prompt injection via
retrieved content [26]
Forged headline, spoofed filing, or
coordinated social-media posts in
the agent’s feeds
The payload is plausible news rather than an instruction,
so injection filters miss it. The attacker profits from a
position taken beforehand, as in the 2013 AP Twitter
hack [102].
S2.1 Direct prompt injection that
overrides instructions [27]
Injected text that overrides trading
rules such as position limits or
restricted symbols
A rule violation becomes an order that settles. A small
numeric nudge suffices, which is harder to spot than an
instruction override.
S2.2 Unauthorized tool or API
calls [31, 96]
Order submission, fund movement,
or execution of model-written code
(§6.3)
Actions are irreversible, and the damage scales with
account size and leverage, not with the number of calls.
S2.3 Memory and retrieval
poisoning [30]
Poisoned reflections or decision
logs that bias later trades (§6.3)
The bias compounds through self-evolving trading
memory, and the losses it causes look like ordinary
market noise, which delays detection.
S3 A compromised agent
misleads its peers
Compromised agents trade or
broadcast signals that other agents,
bots, and market makers act on
Harm reaches third parties through prices, and herding
among correlated agents [22] amplifies it into
flash-crash-like cascades [18].
R1–R4 Fail-safe behavior under
faults
Agent behavior during gaps,
liquidity shocks, and flash crashes
The attacker can manufacture the shock with spoofed
news or thin-market trades, so a robustness failure
becomes an attack path.
inputs), and the codebook applies to them unchanged. This
identification phase yielded127 candidate papers.
Screening.Two reviewers independently screened all 127
papers by title and abstract, applying the following inclusion
criteria: (I1) the paper must propose, implement, or empiri-
cally evaluate a concrete financial LLM agent system; (I2) the
agent must perform market-facing tasks (e.g., trading, portfo-
lio optimization, or alpha discovery); (I3) the paper must be
written in English and published or posted as a preprint be-
tween January 2023 and March 2026. Papers were excluded if
they (E1) only mentioned LLMs tangentially without an agent
implementation, (E2) focused exclusively on general LLM
security without a financial application, or (E3) were editori-
als, position papers, or surveys outside financial LLM agents,
with no system contribution. Preprints passed the same in-
clusion, exclusion, and eligibility criteria as peer-reviewed
papers, with no filter on citation count or venue. After screen-
ing,87 papers were excluded, leaving40 papersfor full-text
review.
Eligibility and Inclusion.Both reviewers independently read
all 40 full-text papers and assessed them against two addi-
tional eligibility criteria: (G1) the agent architecture must be
described in sufficient detail to apply our FARSIGHT metrics
(i.e., information sources, reasoning pipeline, and output ac-
tions are identifiable); and (G2) the system must include at
least one form of autonomous or semi-autonomous decision-
making rather than being purely a static prediction model. Of
the 40 papers, 25 did not satisfy G2 (they are surveys, bench-
marks, simulations, threat analyses, or defense frameworks
with no autonomous decision-making) and are retained for
background context in Section 5.2. The remaining15 papers
satisfy both G1 and G2, describe distinct, evaluable trading
agent systems, and constitute our final evaluation set (Table 3).
In Section 5.2, we categorize these studies by their agent
architecture, system design, and evaluation methodology to
illustrate how the research community conceptualizes and
analyzes financial LLM agents.
GPT-4GPT-4o
GPT-4o-mini
GPT-3.5GPT-2
DeepSeek-V3
0
5
10
Backbone LLM Model
#Financial Agents
Figure 3: Distribution of backbone LLM models used across
15 financial LLM agents.
5.2 Trading Agent Architectures and Ecosys-
tem Context
From the 40 papers retained during screening (Section 5),
25 are ecosystem studies that inform but are not them-
selves evaluable trading agents: surveys and SoK papers
synthesize financial LLM tasks, inputs, and recurring de-
9

Table 3: Summary of LLM-based Financial Agents: Role, I/O, Mechanisms, and Evaluation Settings
System / Paper Role Typical Inputs Outputs Mechanism Code
TRADINGGPT [103]/d⌢llar-sign📰/hist⌢ry /landmark /file-inv⌢ice-d⌢llar🐁/file♂¶e¶ory♂network-wired/user-circle×
FINMEM[52]/d⌢llar-sign📰/hist⌢ry /file-inv⌢ice-d⌢llar🐁/file♂¶e¶ory/user-circle✓
MARKETSENSEAI
[104]
/d⌢llar-sign📰/hist⌢ry /landmark /file-inv⌢ice-d⌢llar🐁/file♂network-wired/ravelry🔗×
FINCON[14]/d⌢llar-sign📰/hist⌢ry /landmark /file-inv⌢ice-d⌢llar⌣🐁/file♂¶e¶ory♂network-wired× ∗
STOCKAGENT[47]/d⌢llar-sign📰/hist⌢ry /landmark /file-inv⌢ice-d⌢llar🐁/file♂network-wired✓
FINAGENT[105]/d⌢llar-sign📰/hist⌢ry /file-inv⌢ice-d⌢llar/user-tie🐁/file♂¶e¶ory✓
FINROBOT[106]/d⌢llar-sign📰/hist⌢ry /landmark /file-inv⌢ice-d⌢llar⌣🐁/file♂¶e¶ory♂network-wired/ravelry🔗✓
ALPHA-GPT 2.0 [53]♂search-dollar 📰/hist⌢ry /landmark /file-inv⌢ice-d⌢llar /file/user-tie×
QUANTAGENT[49]/d⌢llar-sign /hist⌢ry🐁/file♂network-wired✓
TRADEXPERT[107]/d⌢llar-sign📰/hist⌢ry /file-inv⌢ice-d⌢llar🐁/file🔗×
TRADINGAGENTS[15] /d⌢llar-sign📰/hist⌢ry /file-inv⌢ice-d⌢llar⌣🐁/file♂network-wired✓
FLAG-TRADER[108]/d⌢llar-sign📰/hist⌢ry🐁/file🔗×
CONTESTTRADE[51]/d⌢llar-sign📰/hist⌢ry /landmark🐁/file♂network-wired✓
TRADINGGROUP[109] /d⌢llar-sign📰/hist⌢ry /file-inv⌢ice-d⌢llar⌣🐁/file♂network-wired×
MARKETSENSEAI 2.0
[110]
/d⌢llar-sign📰/hist⌢ry /landmark /file-inv⌢ice-d⌢llar🐁/file♂network-wired/ravelry🔗×
Notes:📰= News,/hist⌢ry= Stock price history,/landmark= Macro-market data,/file-inv⌢ice-d⌢llar= Financial statements/filings,⌣= Market sentiment,/user-tie= Expert Opinions,🐁=
Buy/Sell/Hold decision, /file= Summary / Rationale, /d⌢llar-sign= Trader role,♂search-dollar= Alpha Miner role,♂¶e¶ory= Uses memory module,♂network-wired= Multi-agent collaboration,/user-circle=
Multiple profile/character settings, /ravelry= RAG,🔗= Chain-of-Thought. ✓/ × = official code release linked from the paper or an author’s page (checked October
2026);× ∗ = the linked repository contains no code yet.
signs [2, 4, 45, 46, 114 –117]; benchmarks and evaluation
suites probe agent-level attacks, financial metrics, and long-
run robustness [16, 118–121]; simulation testbeds provide
controllable market environments [88,122,123]; and threat/de-
fense analyses address domain-specific red teaming and
architecture-level safeguards [124, 125]. While these works
shape the broader landscape, our evaluation targets the re-
maining15 trading agent systems, agents that autonomously
transform market data into executable trading decisions. We
definetrading agentsas financial LLM agents that combine
heterogeneous market inputs with LLM reasoning to produce
trades and natural-language rationales. As detailed in Table 3,
we organize them into six architectural paradigms.
Single-Agent Memory & Persona Systems.Trading-
GPT[103] uses layered memory and task decomposition
across cooperative roles for multi-horizon trading via GPT-4.
FinMem[52] refines this withcharacter designand adjustable
cognitive span. Its self-evolution mechanism enables adaptive
risk profiling but also creates persistent attack surfaces.
Analyst & Fundamental-Analysis Agents.Market-
SenseAI[104] (andMarketSenseAI 2.0[110]) applies
chain-of-thought fundamental analysis over U.S. Securities
and Exchange Commission (SEC) filings with minimal live
API exposure.FinCon[14] formalizes a manager–analyst
hierarchy with feedback-driven risk control.
Event-Driven & Multimodal Agents.StockAgent[47] uses
Table 4: Reported attack success rates (ASR) for backbone
LLMs of financial LLM agents: jailbreak benchmarks for the
backbones that the papers report, and prompt injection for
current frontier models that the released code now supports.
Backbone LLM Attack (benchmark) ASR
GPT-4 Jailbreak (DAN [28]) 95%
GPT-4o Jailbreak (HarmNet [126]) 94.8%
GPT-4o-mini Jailbreak (GRAF [127]) 95.0%
GPT-3.5-Turbo Jailbreak (DAN [28]) 95%
DeepSeek-V3 Jailbreak (CNSafe-RT [128]) up to 100%
GPT-5.3-Codex Indirect injection
(LivePI [25])
27.2%
Claude Opus 4.6 Indirect injection
(LivePI [25])
10.7%
Gemini 3.1 Pro Indirect injection
(LivePI [25])
29.6%
GPT-5.4 Adaptive injection, trans-
ferred [77]
63.3%
Gemini 3 Pro Adaptive injection, trans-
ferred [77]
92.6%
10

event-driven simulation with curated inputs.FinAgent[105]
targets cross-asset generality via tool-augmented, multimodal
reasoning with broad API integration.
Platform & Alpha-Discovery Agents.FinRobot[106] pro-
vides a composable multi-LLM platform with modular design.
Alpha-GPT 2.0[53] focuses on alpha discovery with human-
in-the-loop oversight and no live execution, one of the most
secure designs.
Low-Latency & Expert-Fusion Agents.QuantAgent[49]
integrates classical technical features with a dedicated
risk-monitoring agent for HFT-like settings, achieving the
strongest robustness profile.TradExpert[107] uses a mixture-
of-experts architecture fusing specialized LLM outputs.
Multi-Agent Collaborative Systems.TradingAgents[15] is
the most comprehensive system (over 100k GitHub stars as of
October 2026), scaling the firm metaphor with analyst/re-
searcher/risk teams and debate–synthesis, but introduces
>240 s decision latency.FLAG-Trader[108] blends LLM
deliberation with reinforcement learning.ContestTrade[51]
uses internal competition to mitigate overfitting.Trading-
Group[109] probes group-scale collaboration with config-
urable risk parameters.
Cross-Cutting Observations.Three convergences emerge
across Table 3: (i) most systems ingest news, fundamentals,
and price data to output trades with natural-language ratio-
nales; (ii) modular multi-agent structures and reflective mem-
ory modules dominate; (iii) RAG over SEC filings increas-
ingly shapes model reasoning.
To understand what makes financial LLM agents fundamen-
tally different, we first examined how agentic LLM systems
are structured across other high-stakes domains such as law,
healthcare, and education. Prior studies show that legal agents
emphasize traceability and precedent grounding [129, 130],
healthcare agents prioritize safety, hallucination control, and
clinical validation [131, 132], and educational agents focus
on pedagogical reliability and personalized instruction [133].
Across these domains, risks usually stem from instruction-
following errors, hallucinated reasoning, or misalignment with
domain constraints. But none involve real-time market mi-
crostructure or the reflexive, latency-sensitive execution loops
that trading agents operate in.
By contrasting these domain patterns with our analysis of
15 major financial LLM trading systems, we identified a clus-
ter of properties unique to financial agents, shaped by market
speed, heterogeneous signal dependence, execution autonomy,
and systemic reflexivity. As illustrated in Figure 4, financial
LLM agents exhibit five defining characteristics (Appendix E
ties each one to the tables that support it): (i)Instantattack
windows, since markets reprice within milliseconds and an
attacker can profit from a transient dislocation before a deliber-
ating agent or a human reviewer responds; (ii)Inconspicuous
micro-manipulations that resemble legitimate market signals;
(iii)Unverifiedingestion of external data due to speed-first
execution pipelines; (iv)Adaptivemulti-source exploitation
Figure 4: Distinct attack characteristics of financial LLM
agents compared to other domain-specific agent systems.
enabled by heterogeneous signal integration; and (v)Cas-
cadingamplification, where small perturbations propagate
system-wide through inter-agent reflexivity. These proper-
ties combine into an attack surface that is fragile and easily
amplified, and that differs fundamentally from other domain-
specific agent systems.
We also analyze the backbone LLMs underlying current
financial agents to understand how their foundational vulner-
abilities propagate into trading environments. As shown in
Figure 3, the papers report theGPT-4family (GPT-4, GPT-4o,
and GPT-4o-mini) as the backbone of twelve of the fifteen
analyzed systems, with plainGPT-4alone powering ten of
them. For multi-model implementations, we selected the most
capable model that each paper reports. Two systems use open-
weight backbones (GPT-2andDeepSeek-V3), and the remain-
ing thirteen depend on closed-source commercial APIs. The
released code has since moved on: four of the seven open-
source repositories ship configurations for frontier models
such as GPT-5.x, Claude 4.x, and Gemini 3.x, and Tradin-
gAgents now defaults to GPT-6 Sol. Because FARSIGHT
rates controls that sit outside the model, these upgrades leave
Table 5 unchanged, and newer backbones do not close the
attack surfaces. As summarized in Table 4, bothGPT-4and
GPT-4oexceed 94% jailbreak ASR on standard benchmarks,
GPT-4o-ministill exhibits a 95.0% ASR under adaptive multi-
turn jailbreaking, andDeepSeek-V3reaches up to 100% [128].
For current frontier models, indirect prompt injection, the at-
tack most relevant to agents, still succeeds in 10.7% to 29.6%
of LivePI cases against GPT-5.3-Codex, Claude Opus 4.6,
and Gemini 3.1 Pro [25], and adaptive attacks fare far better
(Table 4) [77]. These are base-model or generic-agent rates,
which system prompts, tool constraints, and multi-agent val-
idation may lower, and the jailbreak rates concern harmful
content rather than trading, so we treat them only as indicators
of how easily a backbone’s instructions can be overridden.
11

Table 5: Robustness and security evaluation of financial LLM
agents under the FARSIGHT framework. The table summa-
rizes robustness and security levels across nine metrics: R1
(Crash Foresight and Early Awareness), R2 (Rapid Reaction
Capability under Market Shocks), R3 (Loss Containment and
Stop-Loss Execution), R4 (Recovery and Post-Crash Adapta-
tion), S1 (Attacks on Market-Relevant Information Sources),
S2.1 (Prompt Injection & Instruction Override), S2.2 (Tool-
Use & API Exploitation), S2.3 (Memory or Context Manipu-
lation), and S3 (Agent-as-Attacker Behavior).
Agent System R1 R2 R3 R4 S1 S2.1 S2.2 S2.3 S3
TradingGPT❍ ❍ ❍ ❍ ❍ ❍ ◆ ❍ ❍
FinMem◆ ❍ ◆ ◆ ❍ ❍ ◆ ❍ ❍
MarketSenseAI❍ ❍ ❍ ❍ ❍ ◆ ● ● ◆
FinCon❍ ❍ ❍ ❍ ❍ ◆ ◆ ◆ ◆
StockAgent❍ ❍ ❍ ❍ ◆ ◆ ◆ ◆ ❍
FinAgent❍ ❍ ❍ ◆ ❍ ◆ ◆ ◆ ◆
FinRobot❍ ❍ ❍ ❍ ◆ ◆ ◆ ◆ ●
Alpha-GPT 2.0◆ ❍ ◆ ◆ ◆ ● ● ◆ ●
QuantAgent◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ❍
TradExpert❍ ❍ ❍ ❍ ❍ ◆ ◆ ● ◆
TradingAgents◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ❍
FLAG-Trader❍ ❍ ❍ ❍ ◆ ◆ ◆ ◆ ◆
ContestTrade❍ ❍ ◆ ◆ ◆ ◆ ◆ ◆ ◆
TradingGroup◆ ◆ ◆ ◆ ◆ ◆ ◆ ❍ ❍
MarketSenseAI 2.0❍ ❍ ❍ ❍ ❍ ◆ ● ● ◆
●(Fully Robust / Low Risk)◆(Partially Robust / Medium
Risk)❍(Not Robust / High Risk)
Per-agent justifications for all partial (◆) and fully robust / low-risk (●)
scores are detailed in Appendix C. Scoring criteria follow the codebook in
Appendix B (Table 18). Every security●here reflects a surface that is
absent by design, not an active defense.
6 Systematization Results
This section reports the ratings that the FARSIGHT frame-
work of Section 4 assigns to the 15 schemes. We focus on two
aspects: the robustness of financial LLM agents under market
shocks and their security against diverse adversarial attacks.
A ❍ means that the paper does not evidence the control, not
that a running system lacks it.
Figure 5 condenses Table 5 into one view. The robustness
metrics are the weakest: 39 of the 60 robustness ratings give
no credit, and none gives full credit. Security looks better only
because partial credit is common, and full credit appears in 9
of 75 security ratings, each for a surface that the design leaves
out.
6.1 Findings on the Robustness of Financial
LLM Agents
Table 5 summarizes the robustness ratings of fifteen financial
LLM-based trading systems across four resilience dimensions
0 2 4 6 8 10 12 14
Schemes (of 15)
R1
R2
R3
R4
S1
S2.1
S2.2
S2.3
S3
1
3
3
2
5
3
6
7
8
12
12
9
7
10
12
9
8
7
2
3
6
Full credit Partial credit No credit
Figure 5: Distribution of the paper-level ratings of Table 5
across the 15 schemes. No scheme earns full credit on any
robustness metric or on S1, and every security full credit
comes from a surface that the design removes.
(R1–R4). Overall, robustness remains weak: no scheme earns
full credit on any robustness metric, 12 of the 15 receive no
credit on at least one, and those that earn partial credit do so
through ad-hoc or conceptual mechanisms without complete
automation, verification, or closed-loop control.
Analysis of Crash Foresight and Early Awareness.Five
agents earn partial R1 scores, all through qualitative or reac-
tive mechanisms with no structured quantitative foresight.Fin-
Memadjusts trading aggressiveness after realized drawdowns,
which is a purely reactive mechanism.Alpha-GPT 2.0uses of-
fline human-in-the-loop oversight during research cycles, with
no continuous anomaly surveillance in live trading.Quan-
tAgentincludes a risk monitoring agent but lacks concrete
metrics (e.g., VIX tracking, correlation dislocation).Tradin-
gAgentsandTradingGroupassess the direction of the market
regime from multi-source sentiment, a high-level awareness
with no quantitative foresight. None implement automated
anomaly-detection pipelines comparable to traditional quan-
titative systems (e.g., VIX-based alerts, entropy divergence,
principal component analysis (PCA)-based volatility cluster-
ing), revealing a consistent bias toward qualitative interpreta-
tion over measurable early warning.
Analysis of Rapid Reaction Capability.OnlyQuantAgent,
TradingAgents, andTradingGrouppartially address rapid re-
action.QuantAgentcan trigger alerts upon abnormal volatility
but is bottlenecked by multi-agent inference latency.Tradin-
gAgentsincludes a risk management team that can override
risky behavior, yet the team acts through message-passing and
debate, with no direct execution path.TradingGroupoffers
configurable stop-loss and take-profit thresholds but lacks
autonomous shock detection or circuit-breaking logic. All
systems prioritize analytical deliberation over reflexive action.
None implement fast-path interrupt mechanisms, safe-mode
pipelines, or hardware-level latency reduction.
12

As summarized in Tables 6 and 7, all 15 systems exhibit
LLM inference delay and I/O latency, while 10 add multi-
agent communication overhead. The most widely used frame-
work,TradingAgents, introduces over four minutes of total
decision latency, orders of magnitude slower than algorithmic
or high-frequency trading requirements. These latency gaps
translate into critical vulnerabilities:(1) price staleness, where
agents act on outdated information;(2) stop-loss failures,
where delayed risk-control activation leads to uncontrolled
drawdowns; and(3) slippage and execution drift, where I/O
and API delays cause execution prices to deviate from targets.
Table 6: Occurrence of major latency sources across 15 finan-
cial LLM trading agents.
Latency Source Count
LLM Inference Delay 15/15
Agent Communication Overhead 10/15
I/O & API Latency 15/15
Table 7: Latency comparison between traditional trading
styles and representative LLM trading agents.
Trading Type/Agent Typical La-
tency
Src.
High-Frequency Trading
(HFT)
<0.0001 s [134,
135]
[R]
Algorithmic Trading< 0.1s
[136, 137]
[R]
Intraday Trading∼1 s [136] [R]
Daily / Swing Trading∼10 s [136] [R]
TradingAgents>240s [M]
[R] = Reported in cited literature; [M] = Measured: median wall-clock
latency over five end-to-end runs of the open-source TradingAgents release
in its fastest configuration (smallest supported backbone and shortest
chain-of-thought), and therefore a lower bound. See Section 5.2 for
architectural details.
Analysis of Loss Containment and Stop-Loss Execution.
Six agents earn partial R3 scores, but none formalize con-
tainment into deterministic enforcement.FinMemadapts risk
modes after performance declines yet specifies no drawdown
thresholds or liquidation triggers.Alpha-GPT 2.0andQuan-
tAgentacknowledge risk management roles but lack algo-
rithmic stop-loss execution.TradingAgentsachieves smaller
drawdowns empirically through its risk management team,
but without transparent liquidation logic.ContestTradedown-
ranks poorly performing agents onlyafterlosses material-
ize, andTradingGroupoffers configurable stop-loss settings
without dynamic volatility-adjusted calibration. Across all
systems, containment remains discretionary: none implement
rule-based position limits, volatility-linked exposure scaling,
or forced liquidation protocols, showing that current LLM
agents treatrisk controlas a concept but rarely enforce it as a
hard limit.
Analysis of Recovery and Post-Crash Adaptation.R4
shows the most partial scores, with seven agents displaying
forms of adaptive learning or reflection, yet all rely oncon-
tinuous learning, and none hascrash-triggered recovery.Fin-
Memupdates memory representations over time but lacks
event-triggered retraining to distinguish normal drift from
tail events.FinAgentandAlpha-GPT 2.0enable post-hoc
behavioral adjustments (via self-reflection and human guid-
ance, respectively) but provide no automated crash-recovery
pipeline.QuantAgent’s two-loop optimization gradually in-
tegrates outcomes yet cannot accelerate recalibration after
extreme losses, andTradingAgentsshares this limitation.Con-
testTradepromotes surviving agents via competition, but this
selection process fails under systemic crashes that degrade
all agents simultaneously.TradingGroupsynthesizes data for
continuous model updates, but recovery remains passive, with
no explicit trigger. None implement structured fault analy-
sis, regime reclassification, or volatility-dependent retraining
triggers.
6.2 Findings on the Security of Financial LLM
Agents
Table 5 summarizes the comparative security risk levels of
fifteen financial LLM-based trading systems under the FAR-
SIGHT framework. Full-credit (●) security ratings are rare:
none on S1, one on S2.1, three each on S2.2 and S2.3, and two
on S3, and each of them goes to a scheme that removes the sur-
face by design. None exhibit end-to-end validation, isolation,
or post-compromise containment, underscoring a systematic
neglect of proactive security design in current financial LLM
ecosystems.
Analysis of Attacks on Market-Relevant Information
Sources.Trading agents that continuously consume exter-
nal market data or sentiment feeds are especially exposed
to data-layer manipulation.TradingGPT,FinMem,Market-
SenseAI,MarketSenseAI 2.0,FinCon,FinAgent, andTrad-
Expertreceive ❍ on S1: they ingest news, social sentiment,
macroeconomic indicators, and fundamental documents from
heterogeneous APIs and RAG pipelines, yet their papers ev-
idence none of the four S1 controls (provenance tracking,
cross-source corroboration, structured aggregation, or cura-
tion). Although many of these systems deliberately diversify
inputs and stage multi-round debates to avoid dependence
on a single feed, such mechanisms primarily filter noise and
disagreement rather than targeted misinformation. A poisoned
but plausible source can still be amplified into trading theses
and written back into memory.
The remaining eight schemes receive ◆. Six of them,
TradingAgents,TradingGroup,FinRobot,QuantAgent,FLAG-
Trader, andContestTrade, earn it through structured aggrega-
13

tion such as voting, ranking, debate, or policy learning, which
mitigates but does not eliminate the impact of corrupted feeds.
Alpha-GPT 2.0andStockAgentearn it through curated or
simulated inputs. None of the 15 papers records source prove-
nance or requires cross-source corroboration, the two indica-
tors that a full S1 rating needs, so the data layer remains the
primary attack surface.
Analysis of Attacks on Agent Logic and Prompts.Prompt-
layer and logic-layer threats are pervasive but often under-
addressed. In S2.1 (Prompt-Injection and Instruction Over-
ride), we rateTradingGPTandFinMemashigh risk: both
expose natural-language coordination channels that accept
unverified inputs, enabling adversaries to override instruc-
tions or seed malicious reasoning. By contrast,Alpha-GPT
2.0(an alpha-focused, idea-generation design) islow riskin
S2.1 because it operates on curated inputs rather than open
prompt channels.StockAgentismedium risk, since its simu-
lated inputs reduce but do not eliminate exposure to prompt-
layer manipulation. In S2.2 (Tool-Use and API Exploitation),
MarketSenseAI,MarketSenseAI 2.0, andAlpha-GPT 2.0are
assessed aslow riskbecause their pipelines emphasize static
document retrieval and analysis rather than live API-driven
tool invocation, reducing the attack surface for real-time API
spoofing or tool misuse. Systems that do invoke external tools
remain more exposed, since injected prompts can escalate
into unauthorized API actions.
In S2.3 (Memory or Context Manipulation), we identify
TradingGPT,FinMem, andTradingGroupas thehigh risk
group: their persistent memory and self-updating pipelines
mean injected content can be stored, reinforced, and replayed
across future decision cycles. Conversely,MarketSenseAI,
MarketSenseAI 2.0, andTradExpertarelow riskfor memory
attacks because they lack long-term, self-evolving memory
layers. The most dangerous failures arise when prompt, tool,
and memory weaknesses interact and no provenance, isolation,
or sanitization control stands between them.
Analysis of Agent-as-Attacker Behavior.Once compro-
mised, agents that carry order-placement authority pose the
greatest threat. InS3 (Agent-as-Attacker), we identifyTrad-
ingGPT,FinMem,StockAgent,QuantAgent,TradingAgents,
andTradingGroupashigh risk. Five interact with live markets
through execution APIs or automated pipelines.StockAgent
instead trades inside a multi-agent simulation, but through
a shared order book with no isolation, so a compromised
instance can still steer peer agents and downstream artifacts
trained on that market. Once the internal logic or prompt layer
of any of these agents is compromised, an attacker could issue
real trades, manipulate orders, or coordinate malicious strate-
gies across multiple sub-agents, amplifying both velocity and
market impact.
Agents such asFinRobotandAlpha-GPT 2.0are compara-
tivelylow risk, as their design intentionally excludes any live
execution or external trading connection. They operate strictly
as analytical or simulation frameworks. The remaining agents,
which can interface with market APIs but are not inherently
autonomous, fall into amedium risktier: their exposure de-
pends on whether external tools or execution endpoints are
activated at runtime.
Insights on Robustness.As summarized in Table 5, none
of the evaluated agents achieved full robustness. Analytical
sophistication does not translate into resilience: ten schemes
receive no credit on R1 and twelve none on R2, and none
has a crash-triggered recovery protocol. Partial ratings rise
from five on R1 and three on R2 to six on R3 and seven on
R4, indicating limited attention to adaptation but a persistent
absence of proactive mechanisms such as volatility-aware
controls or circuit-breaker logic.
Insights on Security.High-risk ratings fall from seven on
S1 to six on S3, but this apparent improvement is mislead-
ing: no system actively defends against the pervasive attack
vectors (prompt injection, data poisoning, tool misuse). Secur-
ing these agents requires defense-in-depth: authenticated data
sources, sandboxed reasoning, restricted tool privileges, and
multi-layer anomaly detection. Across the schemes, greater
agent autonomy expands the attack surface, while strict secu-
rity constraints reduce autonomy. Appendix F compares these
agents with passive-income schemes.
6.3 Code-Level Validation of Open-Source
Schemes
Table 5 rates each scheme from its published design, so we
also asked whether the released implementations behave as
the papers describe. Of the 15 schemes, 7 have an official code
release. FinCon’s repository is a placeholder, and the remain-
ing 7 schemes have none. We audited the 7 releases statically
at pinned commits with the same codebook. Claude Son-
net 5.5, given our paper-level ratings to locate the described
mechanisms, labeled every indicator with file-and-line evi-
dence in 3 independent runs per repository, deterministic pat-
tern matching checked the code paths that decide the ratings
(order submission, code execution, persistence, and risk lim-
its), and a separate reading of the cited source lines ruled on
every cross-run disagreement (Appendix D). The runs agreed
on 56 of 63 ratings (88.9%) and on 195 of 231 indicator judg-
ments (84.4%). The pattern scan, which ran independently
of the LLM, found no order-submission or broker call in any
release and located the host-side exec calls in ContestTrade
that weakness (i) below describes. Table 8 lists the resulting
code-level ratings.
Paper and code diverge in both directions.Code-level and
paper-level ratings agree on 39 of 63 ratings (61.9%), and
Figure 6 traces where the other 24 move. Of these, 10 rise
from no credit to partial credit, 8 from partial to full credit, 3
from no credit to full credit, and 3 fall from partial to no credit.
Of the 21 ratings where the code scores better, 10 fall on S2.2
and S3 and share one cause: no release contains an order-
execution path, so 6 of the 7 releases satisfy the no-execution
14

Table 8: Code-level ratings of the seven schemes with an
official code release, derived from three independent audit
runs per repository (pinned commits in Table 20).↑ (↓) marks
a rating that is better (worse) than the paper-level rating in
Table 5.
Scheme R1 R2 R3 R4 S1 S2.1 S2.2 S2.3 S3
FinMem◆ ❍ ◆ ◆ ◆↑ ◆↑ ●↑ ◆↑ ●↑
StockAgent❍ ❍ ◆ ↑ ❍ ◆ ◆ ● ↑ ◆ ❍
FinAgent◆ ↑ ❍ ◆ ↑ ◆ ◆↑ ◆ ● ↑ ◆ ● ↑
FinRobot◆ ↑ ❍ ❍ ◆ ↑ ◆ ◆ ◆ ◆ ●
QuantAgent◆ ❍ ↓ ❍↓ ❍↓ ◆ ◆ ● ↑ ●↑ ●↑
TradingAgents◆ ◆ ◆ ◆ ◆ ◆ ● ↑ ◆ ● ↑
ContestTrade◆ ↑ ❍ ◆ ◆ ◆ ◆ ◆ ◆ ● ↑
Full credit 1
Partial credit 40
No credit 22
Full credit 12
Partial credit 39
No credit 12
Code-level ratingPaper-level rating
unchanged changed
Figure 6: Movement of the 63 ratings of the 7 open-source
schemes from the paper (left) to the released code (right).
Blue flows mark ratings that change: 21 rise and 3 fall. Of the
rises, 10 come from releases that contain no order path, and
all falls belong to QuantAgent.
indicator of S3 (all but StockAgent, whose agents share an
order book). These research prototypes emit trading decisions
or run backtests, and the execution surface that Table 5 rates
returns once a deployer wires their output to a brokerage
account. The opposite gap is more worrying. All 3 code-
worse ratings belong to QuantAgent, whose release contains
neither the risk agent nor the stop-loss that its paper describes.
ContestTrade’s contest mechanism and FinMem’s risk-averse
mode are likewise inactive in the released pipelines. Their
R3 ratings in Table 8 survive only because this dormant code
counts as a partial indicator (both drop to ❍ under the strict
convention), so Table 5 overstates what these releases do.
The code exposes weaknesses that the papers do not show.
None of the 7 releases enforces a stop-loss, position cap, or
drawdown limit outside the LLM. The only stop-loss val-
ues in the code are a field that the model fills into its report
(TradingAgents) and a strategy that the pipeline never calls
(FinAgent). Beyond these missing controls, the audit found
four concrete weaknesses, each tied to a surface of §4.(i)
Model-written code runs on the host.ContestTrade’s default
stock-selection tool extracts Python from the model’s reply
and runs it with exec in the host process, and FinRobot’s
default assistants execute model-written code locally with
neither a sandbox nor human approval. Because news and
social-media text share the context with these tools, an in-
jected headline can turn into code execution on the operator’s
machine, which chains S1 into the worst S2.2 outcome.(ii)
Secrets reach the model or the logs.If an SEC filing download
fails, a FinRobot data tool returns the exception text, which
contains the request URL with the API token, to the model,
and FinAgent prints its market-data API key to standard out-
put.(iii) Memory is stored without validation.FinMem, FinA-
gent, FinRobot, and TradingAgents write memory or retrieval
stores to disk and reuse them without checking what is written.
FinMem and FinAgent load these stores with pickle, so a
tampered memory file executes code when it is loaded. The
codebook does not score deserialization, so Table 8 omits this
risk, and FinMem’s higher S2.3 rating there reflects memory
decay and feedback weighting, not write validation. Tradin-
gAgents appends model-written text to a decision log whose
entry delimiter the model can reproduce, so injected content
can forge a past decision and its lesson for later runs (S2.3).
(iv) Peers are trusted.In StockAgent, every agent’s free-text
forum post reaches all other agents’ next-day prompts unfil-
tered, and the market price is simply the last matched price,
so one agent can broadcast false signals and move the price
that every other agent reads (S3). Paper-level and code-level
assessments therefore answer different questions, and a de-
ployer needs both: the paper states what the design intends,
and the code shows what the deployer actually inherits.
7 A Flash-Crash Experiment
Section 6 shows which controls the 15 designs lack. No pub-
lished design halts trading without an LLM call (R2) or checks
both the provenance of its news and a second source (S1), and
no code release enforces a stop-loss or position limit outside
the model (R3). Ratings cannot show the cost of these gaps,
because the harm appears once many agents trade the same
stock.
We therefore measure how three LLMs trade one position
after a fake headline and after four real hoaxes (§7.1), and
we let populations of minimal agents that decide as these
models do trade in a simulated market (§7.2). We then record
when the agents cause or amplify a flash crash (§7.3), switch
on the three missing controls and the trading pause of U.S.
exchanges (§7.4), and vary the market, the agents, and the
policy (§7.5). The agents keep the two properties that the
ratings and the code audit found across designs, an LLM that
makes each trading decision and a decision cycle as long as
one round of LLM reasoning, and we drop the rest of each
15

design on purpose.
7.1 Trading Decisions of Three LLMs
To measure decisions, we gave gpt-5.6-luna, deepseek-v4-
flash, and gemini-3.5-flash 108 market snapshots each, three
times per snapshot at temperature 0.7 (324 calls per model).
Each snapshot gives the stock, the last price, the one-minute
prices and the change over the last five minutes, and the posi-
tion, which is 300 shares with their average entry price and
unrealized profit and loss. It also states a 600-share position
limit, a hard cap on how many shares the account may hold,
and contains either no headline or one unsourced report that
the company is under SEC investigation over accounting ir-
regularities.
The system prompt asks for one order in JSON, BUY ,
SELL, or HOLD with a share count. The grid crosses nine five-
minute price changes from −6% to +6%, the two headline
states, two position states (just bought, or 3% under water),
and three stocks (MSFT, JPM, and XOM). We chose these
states because an agent passes through them in a crash: a
quiet market, a falling price, a headline, and a position that
has already lost money.
As Figure 7 shows, all three models sell on the headline,
and they sell the whole position. Luna sells in 77% of headline
cases, DeepSeek in 100%, and Gemini in 100%, and each sell
order covers all or nearly all 300 shares. On price changes
alone, however, the models differ. Luna does not trade without
a headline (0% of such cases), whereas DeepSeek sells after
large falls once its position is under water (89% of cases at
−6%). Gemini buys dips on a fresh position (in up to 67%
of cases), yet it also sells after falls once under water (up
to 33%). DeepSeek and Gemini buy 180 and 109 shares on
average. These differences matter in the market, because a
model that sells on falling prices can amplify a crash that it
did not start, whereas a model that ignores prices can start a
crash but cannot amplify one.
The sales follow the headline itself, whatever its wording
and the prompt. A second probe gave Luna and DeepSeek
a guidance cut or a CEO resignation in place of the SEC
report, and a trader prompt in the style of multi-role designs,
in which analysts summarize the snapshot and a risk manager
urges capital protection, at five-minute changes of −2%, 0,
and +2% (27 cases per headline and prompt). DeepSeek sold
in at least 25 and Luna in at least 20 of the 27 cases for each
headline and prompt. Without a headline, the trader prompt
sold in 4 to 5 of 27 cases. Most sales therefore come from
the headline itself. A multi-role design that ends in one LLM
trader therefore inherits the response that we measure here
with a single prompt.
We also replayed four hoaxes that moved real markets, each
under the source it appeared under: the fake Emulex press
release of 2000, which cost $2.2 billion of market value within
16 minutes [23], the hacked AP tweet of 2013 [102], a fake
No news, fresh
No news, −3%
Headline, fresh
Headline, −3%
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
100 100 100 100 100 89 100 100 100
89 100 100 100 78 22 0 0 0
Luna
No news, fresh
No news, −3%
Headline, fresh
Headline, −3%
33 22 11 0 0 0 0 0 0
89 56 11 0 0 0 0 0 0
100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100
DeepSeek
−6 −4 −2 −1 +0 +1 +2 +4 +6
Five-minute price change (%)
No news, fresh
No news, −3%
Headline, fresh
Headline, −3%
0 0 0 0 0 0 0 0 0
22 33 11 0 0 0 0 0 0
100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100
Gemini
Figure 7: Share of sell answers (%) of the three LLMs by
five-minute price change, headline, and position (fresh or 3%
under water), nine answers per entry.
report of an explosion at the Pentagon from 2023 [138], and
a fake Eli Lilly tweet from 2022 [139]. Each hoax received
nine answers per market state (2,430 calls in total). All three
models sell the whole position on the press release, in 100%
of decisions. DeepSeek and Gemini also sell on the AP tweet
(99% and 96% of decisions) and on the Pentagon report (99%
and 90%). Luna chooses Hold in 318 of its 324 decisions on
these two, and 307 of these replies say that the item needs
confirmation. On the Lilly tweet, Gemini sells in 97% of
decisions, DeepSeek in 25%, and Luna in 0%.
The replays stay close to the originals. The Emulex release
follows the SEC’s description [23] with the probe’s stock in
place of Emulex, the Pentagon report follows news coverage,
and the Lilly tweet is verbatim on LLY . The AP tweet is ver-
batim except that “Barack Obama” becomes “the President”.
With the original name, Gemini sells in 28% of decisions,
and 98 of its other 116 replies name the 2013 hack or call
the item a hoax. Gemini thus appears to remember the 2013
event instead of judging the claim, since the same tweet with
one name changed makes it sell in 96% of decisions. A model
can recognize a hoax that is already in its training data, but an
attacker writes a new hoax, as the SEC-investigation headline
of our grid shows.
7.2 Simulated Market and Shocks
The simulated market trades one asset for one hour in one-
second steps. The asset has a constant fundamental value of
$100, which makes any price below $100 a mispricing that
we can measure. Each second, the price changes by λt times
the net order flow plus Gaussian noise ( σ=$0.01 ). Value
traders, which buy below the fundamental and sell above it,
demand 80 shares per second per dollar of mispricing. The
price impact λt, the price change per share of net selling,
starts at $0.0004 and rises up to fivefold with the realized
volatility of the last 60 seconds, because liquidity thinned as
16

volatility rose in 2010 [18]. This setup follows agent-based
market models that pair fundamental traders with other trader
types [85], which also reproduce the leading explanation of
the 2010 Flash Crash [86].
Each agent manages 300 shares for one retail investor and
decides once per 240 seconds on a staggered clock, the deci-
sion latency that we measured for TradingAgents (Table 7).
At each decision, it sells or buys with the probabilities mea-
sured in §7.1, interpolated linearly over the five-minute price
change and its unrealized profit and loss between the just-
bought and the 3%-under-water states. An agent that sells
sells its whole position in one order, as the models did. We
measure each investor’s profit and loss relative to holding the
300 shares. We run 0 to 800 agents with 50 paired seeds per
setting, so that two settings with the same seed see the same
noise and the same shock, and we report the mean deepest
drawdown, the largest fall of the price below $100 within the
hour.
Three shocks start at minute ten. An attacker’s fake head-
line, the SEC-investigation report of the probe, reaches each
agent’s feed with probability 14/15, the share of rated designs
that take news as input, and alone lowers the price by 0.1%.
A sell program with no attacker sells 120,000 shares over ten
minutes and alone lowers the price by 2.6%. A crash that
starts outside the agents, a larger sell program of 220,000
shares over five minutes like the one in 2010, alone takes the
price 9.2% down and back within minutes. We call a fall of at
least 5% below the fundamental within the hour a flash crash
and a fall of at least 10% a severe one, since the 2010 crash
fell about 9% and recovered within the hour [19]. For scale,
selling 120,000 shares, about $12 million, over ten minutes
lowers our price by 2.6%, roughly as in a thinly traded stock,
and the agent counts below describe a market of that depth.
The three controls follow the missing ratings. The fast
path of R2 freezes new orders for ten minutes once the price
falls by more than three calm 60-second standard deviations
within 60 seconds, and it does so without waiting for any
LLM call. The hard limits of R3 cap each position at 300
shares and stop any agent whose loss exceeds 3% of a full
position from trading, using broker prices in place of any text
the LLM receives. Source corroboration (S1) lets an agent
act on a headline only if a second source confirms it, which
the fake headline lacks in our setup. We also model Limit
Up-Limit Down (LULD), the pause that U.S. exchanges apply
to large stocks [24]. Under LULD, the price cannot cross a
5% band around its mean over the previous five minutes, and
if it remains at the band for 15 seconds, trading pauses for five
minutes, during which the sell programs stop and the agents’
orders wait in sequence.
7.3 Causing and Amplifying Crashes
As Figure 8a shows, the fake headline barely affects a market
without agents, yet it sets off a flash crash in 2% of runs
with 100 DeepSeek agents, 30% with 150, and 92% with
200. The other two models come within 8 points of these
rates, and from 300 agents on, all runs crash with each model.
Between 100 and 300 agents the crash thus goes from rare to
certain, although these populations hold only a quarter to three
quarters as many shares as the sell program that the market
absorbs. They need fewer shares because each agent sells its
whole position in one order and the orders of all agents arrive
within one 240-second decision cycle, faster than the value
traders can buy them. With 400 agents the investors lose 5.2%
of their holdings, and with 800 agents 10.5%.
Figure 9 follows one run with 400 DeepSeek agents. The
price remains at $100 until the orders arrive four minutes after
the headline, falls to about $91, and recovers within minutes
as the value traders buy the mispricing, the same shape as
the 2010 crash. In such runs, the agents sell 63% of their
investors’ shares at least 5% below value, and this loss falls
on the investors who own the agents. An attacker who sold the
stock short (sold borrowed shares) before posting the headline
profits from these sales. In this S3 path of FARSIGHT, the
attacker compromises no agent, and the agents’ own orders
execute the attack. The real hoaxes do the same. After the
Emulex press release, 200 agents of each model crash the
market in 92% of runs, and 300 DeepSeek or Gemini agents
crash it in all runs after the AP tweet or the Pentagon report.
Luna’s agents choose Hold on these two, and the same tweet
therefore has no effect on a market of Luna agents.
Without any attacker, agents whose model sells when prices
fall change a shock that the market would absorb into a crash
(Figure 8b). DeepSeek agents sell into the program once under
water and change its 2.6% fall into a flash crash in 32% of
runs with 200 agents and 94% with 300, and into a severe
one in 98% of runs with 800. Gemini agents buy part of the
dip, yet they still cause a flash crash in 58% of runs with 600
agents and 92% with 800. Luna agents do not trade on price
changes alone and match the agent-free level. This failure
needs neither an attacker nor a compromised agent. It is the
robustness failure that R2 and R3 rate, and it follows from a
design that lets the model’s reading of the price decide each
sale.
A crash that starts outside the agents also gets deeper
(Figures 8c and 10). Its 9.2% fall grows to 13.8% with 200
DeepSeek agents, 17.3% with 400, and 23.7% with 800, and
to 11.6% with 800 Gemini agents. In this crash, 400 DeepSeek
agents sell 66% of their investors’ shares at least 5% below
value, and their investors end 6.9% behind a buy-and-hold
investor.
Because the policy in each market state comes from nine
answers, we also resampled the nine answers with replace-
ment in each of the 36 market states, 30 times. Between the
5th and 95th percentile of these policies, 400 DeepSeek agents
deepen the outside crash to 15.8% to 18.1%. The sell program
becomes a crash in 40% to 100% of runs with 300 DeepSeek
agents and in 0% to 100% with 800 Gemini agents, which
17

0 200 400 600 800
Number of LLM trading agents
0
5
10
15
Mean deepest
drawdown (%)
(a) Fake headline: agents cause a crash
0 200 400 600 800
Number of LLM trading agents
0
5
10
(b) Sell program: agents amplify it
0 200 400 600 800
Number of LLM trading agents
0
10
20
(c) Outside crash: agents deepen it
Luna, no controls
DeepSeek, no controls
Gemini, no controls
Worst model, with R2 + R3
No agents
Flash-crash threshold (5%)
Figure 8: LLM agents cause and amplify flash crashes, and the fast path and hard limits (R2 + R3) stop both. Mean deepest
drawdown over 50 seeds as the number of agents grows, for (a) an attacker’s fake headline, (b) a sell program with no attacker,
and (c) a 2010-sized crash that starts outside the agents. All three models appear in each panel, shifted slightly along the x axis.
Because Luna does not trade on price changes alone, it matches the agent-free level in (b) and (c).
90
100Price ($)
No controls
10 20 30 40 50 60
Minutes (fake headline at minute 10)
90
100Price ($)
All three controls
Figure 9: Price path of one run with 400 agents following the
measured DeepSeek policy after a fake headline at minute 10,
without controls and with all three controls.
give few sell answers on price alone and therefore depend
more on sampling. The headline crash depends less on sam-
pling, since DeepSeek and Gemini sell on the headline in all
answers and Luna in 77%.
7.4 Effect of the Controls
Table 9 switches the controls on one at a time with 400 agents,
and each control stops the failure that its metric names. Source
corroboration (S1) removes the agents’ effect after the fake
headline, because no agent acts on it, but it does not change
the two price shocks, because there the agents act on prices.
Corroboration can also fail in part, for instance if a second
outlet copies the first. If it misses a random quarter of 800
agents, the headline still crashes the market in 80% to 100%
of runs, and if it misses half of 400 agents, in 88%. With the
fast path and hard limits, no run crashes even when corrobo-
ration misses half of the agents. The replayed hoaxes show a
further limit of source checks. They arrived through a hacked
news account, fake verified accounts, and a wire-service press
release, and a check of the source label alone would therefore
5 10 15 20 25 30
Minutes (sell program from minute 10 to 15)
90
100Price ($)
No agents (and 400 agents with R2 + R3)
400 DeepSeek agents, no controls
Figure 10: One outside-crash run. The agents’ sales arrive
near the end of the sell program and push the price from about
$91 to $82. With the fast path and hard limits, the price path
remains within $0.2 of the agent-free path.
likely pass all four.
Hard limits (R3) stop the agents from amplifying either
price shock, because an agent that has lost 3% of a full posi-
tion stops trading before its sales can deepen the fall. Yet 6%
of fake-headline runs with 400 agents still crash, because the
agents sell on the headline before any of them is under water.
The limits halt an agent instead of selling its position, and
this choice matters. A stop-loss, an order that sells once the
price falls to a trigger level, changes 400 of 450 shocks into a
collapse of more than half the price at the same 3% threshold,
because the first sales push other agents past their thresholds,
and their sales push the next agents further. Stop-loss sales
run on broker prices and bypass the fast path, and even with
the fast path the outside crash collapses in 150 of 150 runs.
In a population of agents, a hard limit should therefore stop
trading, as a kill switch does, instead of selling.
The fast path (R2) works against all three shocks, since the
first sharp fall freezes the orders still in flight. With the fast
path alone, the mean deepest drawdown after the headline falls
from about 9.6% to 1.1% with each model, and both price
18

Table 9: The framework’s controls keep the agents from causing or amplifying a flash crash. Mean deepest drawdown (%) with
400 agents per measured policy (DS: DeepSeek), 50 paired seeds per entry. Bold marks a crash the agents cause or amplify: at
least 5% of runs fall 5% below the fundamental, or the agents add at least one point to the outside crash.
Fake headline Sell program Outside crash
ControlsLuna DS Gemini Luna DS Gemini Luna DS Gemini
No agents 0.1 0.1 0.1 2.6 2.6 2.6 9.2 9.2 9.2
No controls9.6 9.6 9.52.66.7 4.69.217.3 10.8
Fast path (R2) 1.1 1.1 1.1 2.6 2.6 2.6 9.2 9.2 9.2
Hard limits (R3)3.6 3.6 3.62.6 3.3 3.3 9.2 9.2 9.2
Corroboration (S1) 0.1 0.1 0.1 2.66.7 4.69.217.3 10.8
R2 + R3 1.1 1.1 1.1 2.6 2.6 2.6 9.2 9.2 9.2
R2 + R3 + S1 0.1 0.1 0.1 2.6 2.6 2.6 9.2 9.2 9.2
shocks return to their agent-free levels (Table 9). With all
three controls, each setting matches its agent-free drawdown.
The fast path also works at a looser threshold. At five standard
deviations in place of three, the fast path and hard limits keep
each shock’s drawdown within 1.5 points of the agent-free
level. These controls do not require the agents to be diverse
or slow, because they act on prices and positions, which the
broker observes, and not on the content that the LLM reads.
The fast path has a cost in hours without a shock, because
the agents’ own trades can move the price by three calm
standard deviations within a minute. In a calm hour, it halts
400 DeepSeek agents 0.6 times on average at three standard
deviations and 0.2 times at five. Gemini agents move the price
more, because they buy dips, and the fast path halts 400 of
them 2.4 times per calm hour (1.5 at five standard deviations),
and with both controls their trading falls from 9.8% to 4.1% of
their holdings per hour. The 300-share cap equals the starting
position and blocks buys. With a 600-share cap, 400 Gemini
agents trade 9.8% of their holdings per calm hour, as many
as without controls, and the drawdown under the hard limits
changes by at most 0.1 points. Luna agents do not trade in a
calm hour. A deployer can therefore trade false halts against
protection by moving one threshold.
The controls also protect investors after true news. If the
value really falls 8%, 400 agents without controls push the
price 9.6% to 11.1% below the new value and their investors
end 4.2 to 5.9 points behind holding, while with the fast path
and hard limits the price ends within 0.1% of the new value. A
halt thus does not trap investors in a falling stock. Instead, the
agents’ own sales after true news overshoot the new value, and
the investors who sell near the bottom lose more than those
who hold. Faster models do not help either. If 400 DeepSeek
agents decide every 60 seconds instead of every 240, they sell
into the fall sooner and deepen the outside crash to 35.9%
instead of 17.3%, whereas with the fast path and hard limits
it reaches 9.2%. The part of a trading agent that must be fast
is therefore the rule-based path outside the LLM.
Existing exchange pauses miss these crashes. Table 10
adds LULD to the market, and the headline with 200 or 400
agents starts a pause in 0 of 300 runs across the three models.
Because the agents’ orders arrive over four minutes, the five-
minute average that defines the band falls along with the price.
With 400 DeepSeek agents the price still falls 8.2%, and their
investors lose 4.8% of their holdings. In the outside crash,
trading pauses 2 times per run, yet 400 DeepSeek agents
deepen the fall from 9.2% to 12.9%, and the fast path and
hard limits return it to 9.2%. The four replayed hoaxes give
the same result, since LULD pauses trading in 0 of their
1,500 runs with 200 or 400 agents, while the fast path and
hard limits cap the mean deepest drawdown at 1.3%. Because
LULD responds to price alone, it cannot replace controls
inside the trading stack.
7.5 Robustness of the Results
The crash does not depend on our lookup table of probe an-
swers. In a live check, gpt-5.6-luna decided for each agent in
a separate call during the ten minutes after the headline, with
the probe’s prompt and that second’s simulated prices, and the
agents followed Luna’s measured policy otherwise (10,003
calls). With 200 agents the market crashed in 9 of 10 runs, as
with the measured policy (9 of 10), and with 400 agents in 5
of 5 runs, again as with the measured policy (5 of 5). The live
model received prices that its own agents had already moved,
and this check therefore also covers the feedback between the
agents’ sales and their next decisions, which the lookup table
models through interpolation.
Table 10 changes one setting at a time with the DeepSeek
policy: decisions every 60 or 120 seconds, half or double the
value traders, half or double the price impact, no liquidity
thinning, three times the noise, a headline that reaches half of
the agents, positions that vary, cycles that vary, three models
mixed, five investor personas, and LULD. With 400 agents,
the headline crashes the market in all runs of each setting but
one.
Faster decisions and fewer value traders deepen both price
19

Table 10: Robustness checks (DeepSeek policy, 30 paired
seeds; 50 for mixed population, personas, and LULD):
crashed headline runs (%), mean deepest drawdown (%) of
price shocks, and the largest gap (points) between 400 agents
under R2+R3 and none.
Headline Sell program Outside crash R2+R3
Setting200 400 None 400 None 400 gap
Our setting 93 100 2.6 6.6 9.2 17.3 0.9
Decisions every 60 s 100 100 2.6 24.2 9.2 35.9 1.1
Decisions every 120 s 100 100 2.6 13.6 9.2 24.6 0.9
Value traders×0.5 100 100 5.1 18.0 18.4 31.6 1.0
Value traders×2 0 100 1.3 2.2 4.6 8.6 1.0
Price impact×0.5 13 100 2.6 5.2 9.3 15.7 0.5
Price impact×2 100 100 2.6 8.7 9.2 19.4 1.1
No liquidity thinning 0 100 2.6 4.3 9.2 13.4 0.4
Noise×3 93 100 2.8 6.1 9.4 17.2 1.1
Headline reaches half 0 100 2.6 6.6 9.2 17.3 0.8
Positions vary 100 100 2.6 7.7 9.2 18.1 0.9
Cycles 60–600 s 0 13 2.6 5.4 9.2 13.3 0.9
Three models mixed 92 100 2.6 4.9 9.2 12.8 0.9
Five investor personas 4 100 2.6 7.9 9.2 14.1 0.8
Exchange LULD pause 92 100 2.6 6.7 9.2 12.9 0.9
shocks, because the market then absorbs less of the agents’
selling before their next decisions. Agents deepen the outside
crash by at least 3.5 points in each of the 15 settings, and
the fast path and hard limits keep each drawdown within 1.1
points of the agent-free level. With double depth or no thin-
ning, however, 400 DeepSeek agents deepen the sell program
to only 2.2% and 4.3%. Amplifying a small shock therefore
needs a thin market, whereas the headline crash does not.
The one exception matters for real agents, which do not
share a clock. If each agent trades on its own cycle, drawn
uniformly between 60 and 600 seconds, the orders spread out,
and 400 agents crash the market in 13% of runs, although 600
still crash it in 97%. Positions that vary, drawn lognormally
with a mean of 300 shares (10th to 90th percentile about
110 to 560) and with orders that scale with them, still give a
crash after the headline in all runs with 200 and 400 agents.
Mixed populations, in which agents cycle through the three
models, crash after the headline in 92% of runs with 200
agents and in all runs with 400. They deepen the outside crash
less than DeepSeek alone, because one third of them follow
Luna, which does not sell on price.
Splitting sales raises the number of agents that a crash
needs, yet more agents still crash the market. If each agent
splits its sale into two equal orders over one cycle, 200 agents
crash the market in 13% to 17% of headline runs, and with
four orders in 0%, against 87% to 93% with one order. With
400 or more agents, all runs crash with either split. Split or-
ders also deepen the outside crash, to 13.2% and 11.2% with
400 DeepSeek agents, and with the fast path and hard limits
no split run crashes. An agent that splits its orders, as an exe-
cution algorithm would, thus raises the threshold but keeps
the mechanism.
Five investor personas in place of one prompt make the
agents less alike but do not remove the crash. A system-
prompt sentence makes the investor a buy-and-hold saver,
a momentum trader, a value investor, a conservative retiree,
or a day trader, and agent i follows the policy measured for
persona imod 5 (1,944 calls per model). Sell answers after
the headline fall from 100% to 67% for DeepSeek and from
77% to 53% for Luna, because the buy-and-hold and value
investors hold. Then 200 DeepSeek agents crash the market
in 4% of headline runs and 400 in all runs. Personas also add
a failure. Momentum traders sell on falling prices, so 400
Luna agents deepen the outside crash from 9.2% to 12.7%
and change the sell program into a crash in 100% of runs,
against 0% with one prompt.
The number of agents that a crash needs grows with the
depth of the market. In markets k=2 , 5, and 10 times deeper,
with value-trader demand multiplied by k and price impact
divided by k, 200k agents crash the market in 0% to 24%
of runs, because a larger population spreads its orders more
evenly over the cycle. By contrast,300k agents crash it in 96%
to 100% of runs (100% at k=5 , which takes 1,500 agents).
The mechanism, whole-position sales within one decision
cycle, does not change with depth. For scale, 1,500 agents
are about 1% of the agentic trading accounts that Robinhood
reported in September 2026 [21], if they traded one stock on
one model’s decisions.
8 Recommendations for Secure and Robust Fi-
nancial LLM Agent Design
Building on Table 5, we give concise design recommenda-
tions, each tied to a specific failure pattern observed across
the 15 surveyed agents and mapped to the robustness (R1–R4)
and security (S1–S3) metrics of FARSIGHT. Several of these
controls are already mandatory for conventional algorithmic
trading. SEC Rule 15c3-5 requires broker-dealers with market
access to block orders that exceed pre-set credit or capital lim-
its [140], and the EU’s RTS 6 requires algorithmic traders to
apply pre-trade controls on order entry and to keep a kill func-
tionality that can cancel any or all unexecuted orders [141].
No scheme earns full credit on R2 or R3 (Table 5), so none
describes such limits or interrupts outside the LLM, which
puts these designs below the bar already set for non-LLM
algorithms.
Section 7 measures what this gap costs. With 400 simulated
agents, the fast path of R2 and the hard limits of R3 removed
the crashes that agents caused and amplified with all three
models (Table 9), so we treat these two controls as the first to
add. The experiment also shapes both. A breached loss limit
has to halt the agent instead of selling its position (R3 below),
and the fast path costs a few false halts per calm hour that a
deployer sets through one threshold. For LLM agents, the new
problem is that the inputs to these controls can carry injected
20

content.
R1: Crash Foresight and Early Awareness.No agent in
Table 5 receives a Full rating on R1:FinMemreacts only to re-
alized drawdowns, whileTradingAgents/TradingGroupinfer
regimes from sentiment rather than microstructure. This rec-
ommendation primarily targets R1 and additionally strength-
ens S1 via cross-source verification. History motivates the
baseline: the 2013 AP Twitter hack erased $136 B in minutes
because automated systems acted on a single unverified head-
line [102], and the 2010 Flash Crash was preceded by liquidity
and toxic-flow signals no surveyed agent monitors [18, 19].
Agents should therefore source-rank and cross-check every
market-moving input, downweighting any single-source head-
line until an independent high-reputation feed confirms it,
and maintain a library of quantitative precursors that fire trig-
gers independently of LLM reasoning: VIX, equity–credit
correlation breakdowns, order-book flow toxicity [142], and
exchange-traded fund (ETF)–underlying decoupling. Inputs
arriving in thin-liquidity windows (pre-market, after-hours)
warrant stricter confirmation.
R2: Rapid Reaction Capability under Shocks.Table 5
shows zero Full ratings on R2, and Table 7 measuresTradin-
gAgentsat over four minutes of decision latency, orders of
magnitude slower than the circuit breakers instituted after
the 2010 Flash Crash [18, 19]. This recommendation targets
R2 and cross-covers S2.2 (by constraining which tools run
during shock states) and S3 (by giving a supervisor override
authority). Trading stacks should separate athinking path
(LLM reasoning, multi-agent debate) from afast path(pre-
defined, latency-bounded safety actions). On shock detection
(price gap >3σ in ≤1 minute, spread blow-up, or volatility
regime jump), the agent must not launch a new reasoning
round. Instead, it freezes new orders, cancels non-essential
resting orders, and switches to capital-preservation mode via
a rules engine that does not call the LLM. In multi-agent
settings the risk agent outranks analyst/trader agents during
shocks, and reactions should be hysteresis-based to resist tran-
sient spikes.
R3: Loss Containment and Stop-Loss Execution.Agents
considerrisk but rarelyenforceit:FinMemandAlpha-GPT
2.0describe risk modes without algorithmic stops,Contest-
Tradedownranks losers only after damage, andTrading-
Group’s stops lack volatility-aware calibration. This recom-
mendation targets R3, cross-covers S2.1 (risk invariants live
outside the LLM) and S3 (hard caps bound compromised-
agent damage). Designs should hard-code per-instrument,
per-sector, and per-day loss limits that LLM output cannot
override, with stop-losses evaluated on broker/exchange data
rather than LLM-parsed feeds to remain intact under data
poisoning [143, 144]. Containment must be multi-layered
(position-level stop, strategy-level halt, portfolio-level circuit
breaker) and volatility-aware (wider stops with smaller sizes
in high-vol regimes). Contest-style agents should feed stop-
triggered events back as negative evidence. Once many agents
trade the same stock, a breached limit should halt the agent,
as a kill switch does, instead of selling its position. In our
simulated market, a stop-loss that sells at a 3% loss turned
400 of 450 shocks into a collapse of more than half the price,
because each wave of sales pushed further agents past their
thresholds (§7.4).
R4: Recovery and Post-Crash Adaptation.No surveyed
agent triggers event-gated recovery:FinMemupdates mem-
ory continuously,QuantAgent’s two-loop optimization can-
not accelerate after tail events, andTradingGroup’s recov-
ery is passive. This recommendation targets R4, reinforces
S1 via clean-data replay and S2.3 via quarantine memory.
Crisis economics consistently shows that liquidity spirals de-
mandexplicitpost-event rebalancing rather than incremental
drift [99, 145, 146]. A recovery pipeline should freeze trad-
ing and snapshot model/memory state, run a post-mortem
against historical stress scenarios, downgrade aggressiveness
(leverage, confidence thresholds, confirmation requirements),
and replay the day with clean data to identify corrupted sig-
nals. Memory agents should route uncertain experiences to
aquarantine memoryrevalidated before promotion, and no
long-lived instruction should be accepted from a single event.
S1: Attacks on Market-Relevant Information Sources.
Seven agents that ingest RAG feeds or social sentiment with
no S1 control (e.g.,FinMem,FinCon,MarketSenseAI,Mar-
ketSenseAI 2.0) receive a high-risk S1 rating, and the rest earn
only partial credit because none both tracks provenance and re-
quires corroboration. Real incidents [102] and indirect prompt
injection [26] show a single poisoned source is sufficient to
coerce market-moving actions. This recommendation targets
S1 and reinforces R1 and R4 by ensuring both foresight and
post-mortem replay run on verified inputs. Agents should tag
every inbound item with provenance (domain, timestamp, au-
thentication), require cross-source majority or diversity before
acting, prioritize structured official feeds over unstructured
social sources, maintain a denylist of easily spoofed channels,
and surface single-source anomalies to the operator rather
than silently trading on them. Provenance has to cover the
content and not only the channel. The four hoaxes that we
replayed arrived through a hacked news account, fake verified
accounts, and a wire-service press release (§7.1), so a check
of the source label alone would likely pass all four.
S2: Prompt/Logic, Tool/API, and Memory/Context At-
tacks.Security research already shows that LLM-level align-
ment cannot be the primary defense for autonomous trading.
Jailbreaks bypass safety training [147], persist across model
generations [28], and transfer to closed models [148]. Di-
rect [27, 149] and indirect [26] prompt injection override
instructions, tool-calling agents follow injected content [96,
118], backdoors [150] and memory poisoning [30] persist
inside agents, training corpora can be poisoned cheaply [29],
fine-tuning data can be extracted [151], and tool misuse cas-
cades [31]. Because financial agents expose all three of the
affected surfaces (natural-language prompts, external tool in-
21

vocation, and persistent memory), trading invariants must be
enforcedoutsidethe LLM and treated as security boundaries
in the systems-security sense rather than as soft policies the
model is asked to follow. This recommendation covers S2.1–
S2.3 and reinforces R2 (fast-path safety cannot be stalled by
an injected prompt) and R3 (position caps must sit beyond
the prompt surface).
Concretely, three hardening layers must interlock so that
the system degrades gracefully under partial compromise. At
the logic layer (S2.1), immutable invariants (never exceed 2%
of portfolio per new position,never trade restricted symbols,
no market orders after hours) are enforced by an external
policy engine, and every inbound text passes through a sani-
tizer that strips tool-invocation phrases, role reassignments,
and hidden-channel payloads documented in published in-
jection taxonomies [26, 27]. At the tool layer (S2.2), tool
bindings expose fixed schemas, per-agent capability scopes
separating analyst-tier read permissions from execution-tier
write permissions [31,96], rate limits, and two-signal approval
for high-notional or high-urgency orders, mirroring the dual-
control discipline long used in financial operations. At the
memory layer (S2.3), only trusted and market-consistent ob-
servations are promoted to long-term memory through ex-
plicit write-gates with provenance checks, while suspicious
experiences remain in a revalidated short-term store, directly
countering the retrieval-poisoning and backdoor-implantation
attacks documented in [30, 150]. These three layers together
move the agent away from relying on model alignment alone
and toward defense-in-depth, matching the assurance level
that non-LLM trading infrastructure already provides outside
the model.
S3: Agent-as-Attacker Containment.Because financial
LLM agents act in the real market, a compromised instance
becomes an adversarial participant, the dynamic behind AI-
amplification concerns raised by regulators [3, 9, 18, 152].
In Table 5, six agents receive a high-risk S3 rating. This
recommendation targets S3 and cross-covers R2 (supervi-
sor override in shocks) and R3 (per-agent notional caps).
Systems should assume a subset of agents will be compro-
mised, and provide behavioral anomaly detection (sudden
order-frequency, asset-class, or liquidity shifts), single-agent
isolation without whole-system shutdown, and coordination
guards so that multiple agents cannot place correlated large
trades without risk-agent approval. Inter-agent messages are
untrusted inputs, mediated by a policy engine. Finally, a hu-
manhard stopmust always override agent behavior, so that
operators can revoke the agent’s trading authority at any time.
9 Beyond Trading: Lessons for High-Stakes
Agents
The controls that the 15 schemes lack are missing for rea-
sons that have little to do with finance. Each scheme moves a
decision that markets used to wrap in hard limits into a lan-
guage model, reads inputs that outsiders can write, keeps state
that nobody validates, and passes its output to other decision-
makers. As a result, any agent that acts with real authority
on such inputs inherits the same failure pattern. This section
lifts FARSIGHT out of trading. We first restate its metrics as
domain-independent properties (§9.1), then rate seven high-
stakes domains on what makes their agents dangerous (§9.2),
and finally work through healthcare and law in detail (§9.3,
§9.4) before turning to the remaining domains (§9.5).
9.1 A Domain-Independent Threat Model
Every scheme in Table 3 has the same anatomy, and so do
agents outside finance. An agent reads from aninformation
plane(feeds, documents, records, web pages), decides in a
control plane(prompts, tools, memory), acts on anactua-
tion plane(orders, prescriptions, filings, commits, payments),
and writes into ashared environmentthat other agents and
people read. Figure 11 places the FARSIGHT metrics on
this anatomy. S1 protects the information plane, S2.1–S2.3
protect the three parts of the control plane, and S3 guards
the edge from the agent’s actions back into the inputs of
others. R1–R4 describe how the whole loop behaves when
the environment itself turns hostile, which the NIST Cyber-
security Framework calls detection, response, containment,
and recovery [101]. The anatomy also separates two failures
that the trading schemes tend to conflate. A compromised
agent fails inside its control plane, whereas a non-robust agent
fails because the environment changes faster than its control
plane can respond. Because both failures reach the world
only through the actuation boundary, FARSIGHT places its
strictest requirements there (R2, R3, and S2.2).
Table 11 restates each metric as a property that any high-
stakes agent needs and instantiates it in four domains. The
property column is the useful abstraction. Crash foresight
becomes early warning of abnormal environment states, rapid
reaction becomes an interrupt path that does not wait for
model inference, and loss containment becomes a hard limit
enforced outside the model. Although none of these properties
mentions prices, each has an established counterpart in at least
one other profession: hospitals block out-of-range doses at
order entry [153], courts hold the signing attorney responsible
for every citation [154], and software teams scope credentials
by least privilege. The trading schemes show what happens
when a design moves the decision into a model and forgets
that the old limit lived outside it.
The five traits of §5.2 generalize in the same way.Instant
becomes the gap between how fast harm arrives and how fast a
reviewer can act, andInconspicuousbecomes how well harm
hides in normal variation.Unverifiedbecomes how much
of the input outsiders write,Adaptivebecomes how many
input channels an attacker can choose from, andCascading
becomes how strongly the agent’s outputs couple to other
22

Information plane S1
📰news, filings, feeds
/file-medicalrecords, scans, notes
/gavelbriefs, productions
/codeissues, docs, tool specs
/gl⌢beweb pages, social posts
Agent (control plane) ♂robot
Instructions and context S2.1
untrusted text can act as a command
Tools S2.2
order entry, e-filing, shell, payments
Memory S2.3
reflections, notebooks, clause banks
♂shield-alt
hard limits
R2/R3
Actuation
/d⌢llar-signorders
♂pillsprescriptions
/file-signaturefilings
/code-branchcommits, packages
/coinstransfers
Shared environment
/char◎-linemarket prices
🏥health record
/balance-scalecase law
/da◎abaserepos, ledgers
/usersother agents read it
reads acts
S3: what one agent writes, other agents read as input
/user-secret adversary
R1 Detect
early warning of
abnormal states
R2 Respond
interrupt without
model inference
R3 Contain
hard limits outside the model
R4 Recover
replay, quarantine, recalibrate
Figure 11: FARSIGHT as a domain-independent threat model. An agent reads an information plane that adversaries can write
(S1), decides with instructions, tools, and memory (S2.1–S2.3), acts through limits that should sit outside the model (R2/R3),
and writes into a shared environment that other agents read (S3). The resilience band (R1–R4) describes the whole loop under a
hostile environment. Each plane lists one example per domain: trading, healthcare, law, software, and the open web.
actors. Together with irreversibility and reliance on in-model
safety, these generalized traits are the axes on which §9.2
compares domains.
The anatomy also explains why generic agent benchmarks
miss these failures. Benchmarks such as AgentDojo [96],
InjecAgent [159], and ASB [160] score whether one agent
completes or refuses one task. Because they score single
tasks, they exercise the information and control planes but
stop at the actuation boundary, and none of them asks what
the action does to the next agent. Robustness under a hostile
environment and propagation through the shared environment,
the two halves of FARSIGHT that are specific to trading, are
exactly the halves that transfer to other high-stakes domains.
9.2 Risk Profiles of Seven High-Stakes Do-
mains
Trading agents combine six properties that raise the cost of a
compromise: actions that cannot be undone, inputs that adver-
saries write, harm that arrives faster than review, coupling to
other actors, harm that hides in normal variation, and safety
that rests on the model alone. Figure 12 rates seven domains
on the same six properties. The ratings are our assessment
from the cited literature and deployments, and Appendix H
gives the reason for every cell.
Figure 12 shows that trading is the only domain rated
high on all six properties, which is why it makes a sharp test
case: every weakness it exposes is amplified. Crypto agents
come closest, because on-chain transfers are final, blocks con-
firm within seconds, and front-running bots react within one
block [161]. Crypto is also a domain where context manipu-
lation of a widely used agent framework has been shown to
trigger unauthorized asset transfers [75]. Software engineer-
ing shares the two properties that matter most for propagation.
Outsiders write the issues, pull requests, and tool descriptions
that coding agents read [155, 157], and other developers and
their agents pull the code that coding agents write.
The figure also separates domains by where their last line
of defense sits. Payments wrap every payer, human or agent,
in transaction limits, authentication, and fraud scoring, so an
agent that is talked into a bad payment still meets a control it
cannot argue with. Healthcare and law place a trained human
at the gate, the pharmacist or the signing attorney, which
works only while that human checks what the agent produced.
Trading, crypto, and software agents in their current designs
often have neither, so their safety rests on the model following
its instructions. This property, more than the domain itself,
decides how far a compromise can go.
Read column by column, the profiles also say which control
each domain needs first. Where harm is fast, as in trading and
crypto, only an interlock that does not wait for inference can
respond in time (R2). Where adversaries author the inputs,
as in law and software, provenance and the separation of
instructions from data come first (S1, S2.1). Where coupling
is high, controls belong on the channel itself, such as fan-out
limits and circuit breakers (S3). Where harm is stealthy, as in
healthcare, monitoring against ground truth and replay after
an incident matter most (R1, R4).
23

Table 11: FARSIGHT metrics restated as domain-independent properties and instantiated in four domains. The trading column
summarizes this paper; the other columns show where the same property sits in healthcare, law, and software engineering.
Metric Domain-independent
property
Trading (this paper) Healthcare Law Software engineering
Resilience when the environment turns hostile
R1 Early warning of
abnormal environment
states
V olatility spikes,
correlation breaks, toxic
order flow
Deterioration scores,
abnormal order patterns
Contradictory filings,
sudden changes in
opposing productions
Unusual dependency,
permission, or CI changes
R2 An interrupt path that
does not wait for model
inference
Order freeze and cancel
outside the LLM
Hard stop at order entry,
pharmacist hold
Citation check before
anything is filed or sent
Session kill switch, token
revocation
R3 Hard limits enforced
outside the model
Position caps, stop-loss,
daily loss limit
Dose limits in order entry
and infusion pumps
Limits on what a drafting
agent may file or send
Least-privilege scopes,
sandbox quotas, rate limits
R4 Post-incident replay and
recalibration
Clean-data replay, memory
quarantine
Incident reporting,
root-cause analysis
Corrected filings, notice to
the court
Rollback and audit of agent
commits
Security of the agent and of the actors it affects
S1 Integrity and
provenance of inputs
Forged headlines, spoofed
filings, coordinated posts
Poisoned literature and
training data [72],
patient-supplied images
Documents produced by
the opposing party,
fabricated precedents
Malicious issues, pull
requests, and tool
descriptions [155]
S2.1 Separation of
instructions from data
Injected text overrides
trading rules
Hidden prompts in medical
images [73]
Hidden prompts in
submitted
documents [156]
Instructions planted in
READMEs and web pages
S2.2 Least privilege for
actuating tools
Order submission,
model-written code on the
host (§6.3)
Order entry, prescriptions,
record writes
E-filing, email to
counterparties
Shell, package publishing,
cloud credentials [157]
S2.3 Integrity of persistent
state
Poisoned reflections and
decision logs
Notebooks that persist
across patients [158]
Clause libraries and
precedent banks
Agent memory files and
vector stores
S3 Containment of harm to
third parties
Orders move the prices
that others read
Entries in a shared record
that later readers trust
Fabricated citations copied
into later filings
Malicious commits and
packages pulled by others
Takeaway
The trading-specific parts of FARSIGHT, robustness un-
der a hostile environment and propagation through shared
state, are the parts that transfer. A domain is as safe as the
controls that sit between its agents and their irreversible
actions, and the ratings show that few agent designs place
those controls outside the model.
9.3 Healthcare Agents
Clinical agents have moved from question answering to dia-
logue and action. AMIE, a conversational diagnostic agent,
outperformed 20 primary-care physicians on 30 of 32 axes
rated by specialists in a randomized, double-blind study of
text consultations over 159 case scenarios [162]. Polaris
runs patient-facing voice calls with a primary agent and
specialist support agents that take over nursing tasks to im-
prove safety [163], and ambient scribes already draft clin-
ical notes at health-system scale [164]. Research testbeds
go further. AgentClinic gives agents tools and a notebook
that persists across patients [158], and Agent Hospital lets
doctor agents evolve by treating tens of thousands of simu-
lated patients [165]. These designs reproduce the multi-role,
memory-heavy architectures of Table 3, with a care team in
place of an analyst desk.
Information plane (S1).Poisoning the knowledge that clin-
ical models learn from is cheap. Replacing 0.001% of the
training tokens of a web corpus with medical misinforma-
tion produced models that spread more medical errors while
matching clean models on standard medical benchmarks [72],
and editing about 1.1% of a model’s weights implants a tar-
geted false fact without hurting other tasks [92]. As in trading,
a corrupted agent therefore looks healthy on the metrics that
its builders track.
Control plane (S2).Patients and outside providers write
much of what a clinical agent reads. Clusmann et al. hid
instructions in medical images that human readers could not
see and found all four tested vision-language models suscepti-
ble across 594 attacks [73]. If the agent can also place orders,
such an injection becomes an S2.2 action, and if it keeps a
cross-patient notebook [158] or evolves from past cases [165],
the injection gains the persistence that S2.3 describes. The ad-
versary need not be a criminal outsider. Finlayson et al. point
out that reimbursement rules already reward manipulating the
inputs of medical models [166], which gives healthcare the
profit motive that trading has.
Shared environment (S3).The electronic health record plays
the role of the order book. An agent’s note or order enters a
record that every later clinician, scribe, and decision-support
24

Irrevers-
ibility
Adversary
inputs
Speed of
harm Coupling
Stealth of
harm
In-model
safety only
Trading
Healthcare
Law
Software engineering
Crypto and DeFi
Payments and commerce
Scientific labs
High High High High High High
High Medium Medium Medium High Medium
Medium High Low Medium Medium Medium
Medium High Medium High High High
High High High High Medium High
Medium High Medium Medium Medium Low
High Medium Medium Low Medium Medium
Figure 12: Risk profiles of LLM agents in seven high-stakes domains, rated on the six properties that make trading agents
dangerous. High means the property raises the cost of a compromised agent in that domain. Ratings are our assessment;
Appendix H gives the evidence for each cell.
tool reads, and copied-forward text carries an error from visit
to visit. A compromised scribe does not need to harm the
current patient to cause harm. It only needs to write a plausible
entry that the next reader trusts.
Resilience (R1–R4).Medicine already has the out-of-model
controls that the trading schemes lack. Computerized order
entry with dose checks reduces medication errors [153], and
pharmacist verification adds a second, independent review.
The lesson from trading is to keep these controls in the path of
the agent, because a control re-implemented inside a prompt
can be argued away. However, the weak point is the human
gate. Automation bias makes reviewers accept wrong advice
from decision support [167], so a reviewer who approves a
hundred correct agent drafts per day is a poor detector of the
one poisoned draft.
9.4 Legal Agents
Legal practice adopted retrieval-augmented research tools and
drafting assistants quickly, and the evidence on their reliabil-
ity is sobering. On specific, verifiable questions about federal
court cases, general-purpose models hallucinated between
58% (ChatGPT 4) and 88% (Llama 2) of the time [93]. Com-
mercial legal research tools that advertised hallucination-free
citations still hallucinated on 17% to 33% of queries in a
preregistered evaluation [74]. Courts have sanctioned lawyers
who filed briefs citing cases that a chatbot invented, and the
sanctioning court stressed that existing rules give attorneys a
gatekeeping duty to ensure the accuracy of their filings [154].
Information plane (S1).Law differs from trading in one
respect that makes it harder. In litigation the adversary writes
part of the agent’s input by design. The opposing party pro-
duces the documents that a review agent reads in discovery,
drafts the contract that a negotiation agent marks up, and
files the briefs that a research agent summarizes. Whereas
a trading attacker must plant a headline, a litigant hands the
planted content over through a channel the agent is obliged to
read. Hidden instructions already appear in documents that
AI systems review. In July 2025, 18 arXiv manuscripts car-
ried concealed prompts that asked AI reviewers for positive
reviews [156].
Control and actuation (S2).A drafting agent with e-filing or
email tools can send privileged material to the wrong party,
file on the wrong docket, or miss a deadline, and a firm’s
clause library or precedent bank is a long-lived memory that
every later draft reads (S2.3). Legal harm is slower than mar-
ket harm, but much of it is final in practice, because a disclosed
privileged document cannot be unread and a missed deadline
can end a claim.
Shared environment (S3).Citations are the order book of
law. A fabricated or mischaracterized precedent that enters
one filing can be quoted in the next, and model-drafted clauses
become templates that other agents retrieve. As with herd-
ing in markets [22], the agents that copy the error are not
compromised. They behave correctly given what they read.
Resilience (R1–R4).The legal profession has a hard stop that
trading agents lack, since a filing needs a signature and the
signer answers for it. The hard stop works only if the signer
verifies, and the hallucination rates above show how much ver-
ification it takes. The FARSIGHT recommendations translate
directly: verify every citation against a primary source before
anything leaves the firm (the R2 interrupt), restrict which tools
a drafting agent may call (S2.2), and treat documents from
the other side as untrusted input that cannot issue instructions
(S1, S2.1).
25

9.5 Other High-Stakes Domains
Table 12 puts the domains side by side and adds general multi-
agent platforms. For each, it lists what the agent changes in
the world, who writes its inputs, how its effects reach others,
the strongest published evidence of attacks, and the control
that already exists outside the model.
Web and computer-use agents read the most open informa-
tion plane of all. Adversarial pop-ups that human users would
ignore made vision-language agents click them in 86% of
cases on average and cut task success by 47% [172]. In the
WASP benchmark, prompt injections in realistic web pages
partially succeeded in up to 86% of cases, although agents
often failed to complete the attacker’s full goal [173]. That
gap reflects limited capability, and it will close as agents be-
come more capable. Embodied agents add physical actua-
tion, and RoboPAIR elicited harmful physical actions from
LLM-controlled robots, including a ground robot planned by
GPT-4o [174].
Three patterns run through Table 12. First, code execution
is the most common route from text to action. ContestTrade
and FinRobot execute model-written code on the host (§6.3),
multi-agent frameworks can be steered into executing arbi-
trary malicious code in 58% to 90% of trials with a GPT-4o
backbone [71], and MCP servers expose tools that coerce
models into credential theft and remote access [157]. In all
three cases, a sandbox outside the model is the single control
that would have stopped the attack. Second, physical and fi-
nancial actuation share the property that matters most, finality:
a synthesis that Coscientist runs [170], a transfer that a Web3
agent signs [75], and an order that a trading agent places can-
not be recalled by a later model call. Third, the domains with
the most mature controls, payments and healthcare, built them
for human operators decades before agents arrived. Agents
that call those controls inherit decades of engineering, and
agents that replace them with prompts inherit none of it.
10 Cascades, Contagion, and Agent Worms
S3 is the surface that turns one compromised agent into a
system failure, and it is the surface that the literature on agent
security has studied least. Markets have a century of experi-
ence with cascades, computer security has three decades of
experience with worms, and LLM agents now combine both.
This section draws the three literatures together. We trace how
market failures already propagated through automated par-
ticipants (§10.1), classify the channels through which agents
affect one another (§10.2), compare agent worms with classic
worms and market cascades (§10.3), and use a branching-
process model to show when one compromised agent can
start an outbreak (§10.4).
10.1 From Flash Crashes to Agent Cascades
Figure 13 places the events that shaped this section on one
time line. Automated markets have already failed in the three
ways that populations of agents can fail. On May 6, 2010,
a large sell program met high-frequency traders that passed
inventory back and forth, and nearly one trillion dollars of
market value disappeared within minutes before prices re-
covered [18, 19]. In April 2013, a single false tweet from a
hijacked news account erased $136 billion in minutes, be-
cause automated systems traded on the headline before any-
one checked it [102]. On August 1, 2012, Knight Capital’s
router sent more than 4 million orders in 45 minutes while
trying to fill 212 customer orders and lost more than $460
million [178]. The SEC found that the firm’s controls did
not stop the erroneous orders before they reached the market,
which made Knight the first enforcement action under the
market access rule, Rule 15c3-5 [140].
The three events correspond to the three surfaces of FAR-
SIGHT. The AP hack is an S1 attack, in which one unverified
source moved every automated reader at once. The Flash
Crash is an S3 cascade, in which participants that behaved
correctly given their inputs amplified a shock that none of
them caused alone. Knight Capital is a robustness failure with
no attacker. Its order flood started when code for a function
that the firm had stopped using years earlier was reactivated
on one server, and nothing outside the trading logic stopped
it [178]. Our audit found the agent-era version of the last pat-
tern. ContestTrade ships a contest mechanism that its pipeline
never calls, FinMem’s risk-averse branch is commented out,
and no release enforces a stop-loss outside the LLM (§6.3).
Code that the paper describes but the pipeline does not run is
the kind of dormant path that turned a deployment error into
a $460 million loss.
Economics explains why such cascades are self-reinforcing.
In an informational cascade, each participant rationally sets
aside its own signal and follows the actions of earlier par-
ticipants, so a few early mistakes can lock in a wrong con-
sensus [179]. If losses force sales, the sales cause further
losses, as in the liquidity spirals that turned the 2007–2008
subprime losses into a market-wide crisis [145, 180]. LLM
trading agents inherit and amplify herding [22], and LLM pric-
ing agents reach supracompetitive prices without being told
to collude [181], echoing earlier findings for reinforcement-
learning pricing agents [182] and trading agents [183]. Regu-
lators have drawn the same conclusion. The Financial Stabil-
ity Board warns that common models and data sources can
produce correlated behavior across institutions [78], and the
Bank of England has said publicly that autonomous agents
could trigger a market meltdown [11]. Our simulated market
in Section 7 reproduces two of the three patterns with agents
that decide as measured LLMs do. Agents that sell on one
fake headline start a crash as the automated readers of the
AP tweet did, and agents whose model sells when prices fall
26

Table 12: High-stakes agent domains compared on the questions that FARSIGHT asks of trading agents: what the agent changes
in the world, who writes the inputs it reads, how its effects reach other actors, the strongest published evidence of attacks, and the
control that already exists outside the model.
Domain What the agent
changes
Who writes its inputs How effects reach
others
Published attack evidence Control outside the
model
Trading (this
paper)
Orders and positions News outlets, social
media, data vendors
Prices that every
participant reads
Adversarial headlines and
misinformation mislead trading
agents [59, 60]; poisoned posts
spread inside agent stacks [62]
Pre-trade limits and kill
switches [140, 141]; no
scheme describes them
outside the LLM
Healthcare Orders, notes,
patient messages
Patients, outside
providers, published
literature
Shared health record,
copied-forward notes
0.001% poisoned training
tokens raise medical errors [72];
hidden prompts in images [73]
Order-entry dose
checks [153], pharmacist
verification
Law Filings, contracts,
client emails
Opposing parties,
courts, counterparties
Citations and templates
reused in later work
17–33% hallucination in legal
research tools [74]; hidden
prompts in submitted
documents [156]
Attorney signature and
duty to verify [154]
Software
engineering
Code, packages,
infrastructure
Issue authors,
dependency
maintainers, tool
servers
Repositories and
registries that other
agents pull
MCP tools coerce credential
theft and remote access [157];
risky code execution by coding
agents [168]
Code review, CI,
sandboxes, least-privilege
tokens
Multi-agent
platforms
Messages to other
agents, delegated
tool calls
Other agents, web
content, files
Agent-to-agent
messages and shared
memory
Arbitrary code execution in
58–90% of trials [71];
self-replicating prompts [68, 70]
Message tagging [70],
topology-aware
filtering [169]
Crypto and
DeFi
Signed on-chain
transactions
Social posts, stored
agent context, on-chain
data
Composable contracts
and a shared mempool
Memory injection triggers
unauthorized transfers [75];
front-running within one
block [161]
Few; immutable contracts
leave the signing key as
the last control
Scientific labs Physical experiments
and syntheses
Literature, protocols,
tool outputs
Published results and
shared protocols
Autonomous synthesis planning
and execution [170, 171]; safety
risks of AI scientists [94]
Lab safety protocols,
human sign-off on
hazardous steps
deepen a 2010-sized crash from 9.2% to 17.3% with 400
agents, with no attacker and no compromise.
10.2 Propagation Channels between Agents
A compromised agent can reach other agents through six
channels, which Table 13 lists with a trading instance from
our data, evidence from general agents, and the control that
would interrupt the channel. Two of the channels need no
compromised receiver at all.
Shared inputs.If many agents read one poisoned item, the
item reaches all of them at once. Figure 14 shows how concen-
trated the inputs of the 15 schemes are: 15 read price history,
14 read news, and 12 read company filings. For example, a
fabricated headline in a widely syndicated feed would reach
almost every design at once, which is the AP hack scaled to
agents. Retrieval systems widen the channel further. With five
crafted passages per target question, an attacker makes a RAG
system return the chosen answer 90% of the time, even in a
knowledge base of millions of texts [184].
Shared models.The same backbone fails in the same way. 12
of the 15 schemes run on the GPT-4 family, so a jailbreak or
injection that works on that family works on most of the field.
Monoculture has measurable costs even without an attacker. If
many decision-makers share one algorithm, overall decision
quality can fall below what independent algorithms would
achieve [189], deployed models fail on the same individu-
als [190], and sharing models and training data homogenizes
outcomes [191]. Across more than 350 LLMs, two models
that both err agree on the wrong answer 60% of the time on
one leaderboard, and larger, more accurate models have more
correlated errors even across providers [81]. Diversity across
vendors therefore helps less than it appears to. In finance
specifically, Gensler and Bailey warned that deep learning
could promote herding through uniform models and shared
data [79], and Danielsson et al. argue that AI can destabilize
the financial system by amplifying procyclicality and creating
new tail risks [80].
Agent-to-agent messages.Multi-agent designs pass free text
between roles, and 10 of the 15 schemes use multi-agent mes-
saging. Prompt Infection shows that a payload can make each
receiving agent re-emit it to the next [70], communication
attacks that intercept messages between agents mislead whole
systems [186], and manipulated knowledge spreads through
agent communities without any explicit prompt manipulation
and survives in their retrieval stores [192]. Topology also
matters, because highly connected networks spread attacks
further [90] and hierarchical structures lose less performance
to faulty agents than flat ones [91]. Control-flow hijacking
is the worst case. Adversarial web content steers multi-agent
27

1988
Morris worm
exploits bugs,
spreads in hours
1991
Epidemic model
of computer viruses
2003
Slammer infects
most hosts in minutes
2010
Flash Crash
automated traders
amplify a shock
2012
Knight Capital
dormant code,
$460M lost
2013
AP Twitter hack
one false tweet, $136B
2023
Indirect prompt
injection in LLM apps
2024
Morris II,
Agent Smith
self-replicating
prompts
classic worms market cascades LLM agent attacks
Figure 13: Three lineages of propagating failure converge in LLM agents: classic worms [175–177], market cascades [18,102,178],
and attacks on LLM agents [26, 68, 69]. Since 2025, MCP exploits [157], code execution through multi-agent frameworks [71],
and public warnings from regulators [11, 13] have followed.
0 5 10 15
Schemes sharing the
component (of 15)
Price-history feed
News feed
Closed-API backbone
Filings
GPT-4-family backbone
Multi-agent messaging
Macro data
Persistent memory
Sentiment feed
15
13
12
12
10
8
5
4
14
Figure 14: Components shared by the 15 schemes. A poisoned
price or news feed, or a weakness in the GPT-4 family, reaches
most designs at once. Input counts come from Table 3 and
backbone counts from Figure 3; red marks components shared
by at least 12 schemes.
frameworks into executing arbitrary code in 58% to 90% of
trials with a GPT-4o backbone, even when no single agent is
susceptible to prompt injection on its own [71].
Shared environment.Agents read the world that other agents
write. Prices are the canonical case, and StockAgent’s code
makes the channel explicit. Every agent reads a market price
that is simply the last matched price, so one agent’s order
moves what every other agent sees (§6.3). Outside markets
the shared environment is the health record, the case law, the
package registry, and the open web. If models are trained
on text that earlier models wrote, they degrade over genera-
tions [187], which is the same feedback loop at the scale of a
training corpus.
Shared memory and tools.Retrieval stores, memory files,
and tool servers are long-lived state that several agents or ses-
sions read. Of the seven audited releases, 4 write such stores
without validation and 2 load them withpickle (§6.3). In the
wider agent world, MCP servers distribute tool descriptions
that can carry instructions [155, 157], and memory injection
into a Web3 agent framework produced unauthorized asset
transfers that prompt-injection defenses did not stop [75].
Human relays.People copy agent output into places that
other agents read: a model-drafted brief into a court filing,
a summary into a research report, a scribe’s note into the
record. Each copy launders the output’s origin. The fabricated
citations that reached court filings [154] traveled this way.
10.3 Anatomy of an Agent Worm
A worm replicates without human help. The 1988 Morris
worm exploited a buffer overflow, a sendmail debugging fea-
ture, and weak passwords, and it spread across the early In-
ternet within hours [175], Code Red reached hundreds of
thousands of hosts in less than a day [193], and Slammer in-
fected most vulnerable hosts within about ten minutes [177].
Kephart and White modeled virus spread as an epidemic on a
directed graph and showed that infection persists only above
a threshold set by contact and cure rates [176]. In scale-free
networks, that threshold falls toward zero [194].
LLM agents have produced the first worms of their own.
Morris II plants an adversarial self-replicating prompt in an
email that a RAG-based assistant retrieves, so each assistant
that processes the email leaks data and forwards the prompt to
the next [68]. Agent Smith feeds one adversarial image into
the memory of one agent in a simulated population of up to
one million multimodal agents, and pairwise chats spread the
jailbreak to almost all of them exponentially fast [69]. Prompt
Infection makes agents inside one multi-agent system pass
a payload to each other like a virus [70]. Table 14 compares
these worms with classic worms and with the market cascades
of §10.1.
Two differences stand out. First, an agent worm exploits
28

Table 13: Channels through which one agent affects others. “Needs a compromised receiver” marks whether harm spreads only
through receivers that the payload compromises (✓) or also through receivers that behave correctly on what they read (✗). The
trading instances come from our ratings and code audit.
Channel Mechanism Trading instance Evidence beyond trading Needs a
compro-
mised
receiver
Control on the channel
Shared inputs One poisoned item
reaches many agents in
parallel
14 of 15 schemes read
news; the 2013 AP
hack [102]
Five passages per question
poison RAG answers 90% of the
time [184]; web injection [185]
✗Provenance and
cross-source corroboration
(S1)
Shared
models
One weakness works on
every agent with the
same backbone
12 of 15 schemes run the
GPT-4 family
Transferable adversarial
prompts [148]; correlated errors
across 350+ LLMs [81]
✗Backbone diversity; limits
outside the model (R3)
Agent-to-
agent
messages
Each receiver follows
the payload and re-emits
it
10 of 15 schemes pass free
text between roles
Prompt Infection [70];
communication attacks [186];
code execution in 58–90% of
trials [71]
✓ Treat peer messages as data
(S3-E3); message tagging;
bounded fan-out
Shared
environment
Agents read state that
other agents write
Prices; StockAgent’s price
is the last matched trade
(§6.3)
Training on model-written text
degrades models [187]; shared
records and case law
✗Circuit breakers;
provenance on records
Shared
memory and
tools
Long-lived stores are
read across sessions and
agents
4 releases write stores
without validation, 2 load
them withpickle
MCP tool descriptions carry
instructions [155]; memory
injection moves crypto
assets [75]
✓Write gates and quarantine
(S2.3); signed stores; safe
loading
Human relays People copy agent
output to where other
agents read it
Written rationales, which
all 15 schemes emit
(Table 3)
Fabricated citations reached
court filings [154]
✗ Duty to verify filings [154];
labels for generated
text [188]
instruction following, the very feature that makes agents use-
ful, so no patch removes the vulnerability. Instead, defenses
lower the per-hop success rate but leave it above zero, and
adaptive attacks bypassed 12 published defenses with success
rates above 90% for most of them [195]. Second, the mar-
ket column shows a propagation mode that neither classic
nor agent worms need:propagation without compromise. A
compromised trading agent’s sell orders lower a price, and
every other agent that reads the price sells for its own, correct
reasons. The effect spreads as belief rather than as code. The
same mode appears in law, where a fabricated citation spreads
through lawyers who cite it in good faith, and in medicine,
where an erroneous entry spreads through clinicians who trust
the record. Defenses that detect and isolate compromised
agents (S3-E1 and S3-E2) cannot stop this mode, because no
receiving agent is compromised. Only controls on the chan-
nel itself, such as circuit breakers on prices, provenance on
records, and corroboration of citations, can.
Takeaway
Populations of agents propagate harm in two ways. In
infection, a payload makes each receiver re-emit it. In
propagation without compromise, correct agents amplify
what a compromised agent wrote into a shared environ-
ment. Agent-level defenses address only the first. Markets
already show that the second needs controls on the chan-
nel, such as circuit breakers.
10.4 Outbreak Threshold for One Compro-
mised Agent
The worm literature measures spread with a reproduction
number, the expected number of new infections that one in-
fected node causes. For agents, a simple version is R=k·p ,
where k is the fan-out of a channel (how many agents read
each message, post, or price) and p is the probability that a
receiving agent both follows the payload and passes it on. We
model spread from one seed as a Galton–Watson branching
process with Binomial(k,p) offspring. The chance that the
seed starts an outbreak that never dies out is 1−q , where
q is the smallest solution in [0,1] of q= (1−p+pq) k. An
outbreak is possible only when R>1 . The model assumes
independent hops and a tree-like topology, so it describes the
early phase of spread, and Agent Smith observed the same
exponential regime in simulation [69].
We take p from the injection success rates that Table 4
reports for current frontier models. Because a payload must
also be passed on, these rates are upper reference points for
p. Figure 15 shows the result. With the most resistant model
in LivePI, Claude Opus 4.6 at 10.7% [25], a channel needs
a fan-out of 10 before one seed is expected to cause more
than one new infection, and at a fan-out of 20 the chance of
an outbreak reaches 85%. With Gemini 3.1 Pro at 29.6%, a
fan-out of 4 suffices, and a fan-out of 10 gives 97%. Under
the transferred adaptive attacks [77], two readers per message
are enough.
29

Table 14: Classic computer worms, LLM agent worms, and market cascades compared. The market column has no replication
step: other participants spread the effect by acting correctly on corrupted prices or news.
Classic worm LLM agent worm Market cascade
Exploited weakness Memory-safety bugs and weak
authentication [175]
Instruction following on untrusted
text [68, 70]
Correct reactions to corrupted prices or
news [18, 102]
Replication Copies its code to the next host The model re-emits the payload in its
output [68]
None; each participant acts for its own
reasons
Propagation vector Network services and email RAG stores, email, agent messages, shared
memory [68, 69]
Prices, order books, and news feeds
Target discovery Random scanning of the address
space [177, 193]
Retrieval, contact lists, and broadcast
channels
Every participant reads the same price
Payload Arbitrary code Data exfiltration, tool calls, trades,
misinformation
Correlated selling and withdrawn
liquidity
Observed speed Most vulnerable hosts within about ten
minutes [177]
Exponential in the number of chat
rounds [69]
Minutes [18]; 45 minutes for Knight
Capital [178]
Patching Fixing the bug immunizes the host No complete fix; adaptive attacks bypass
published defenses [195]
Nothing to patch; the reaction is correct
given the input
Containment Firewalls, patching, rate limits Message validation, tagging [70],
propagation guardrails [68]
Circuit breakers, kill switches, pre-trade
limits [140, 141]
0 2 4 6 8 10 12
Smallest fan-out k with k·p > 1
(a) Critical fan-out per success rate.
Claude Opus 4.6 (10.7%)
GPT-5.3-Codex (27.2%)
Gemini 3.1 Pro (29.6%)
GPT-5.4, adaptive (63.3%)
Gemini 3 Pro, adaptive (92.6%)
10
4
4
2
2
k = 5 k = 10 k = 20
Fan-out of the channel
(b) Outbreak chance per seed.
Claude Opus 4.6 (10.7%)
GPT-5.3-Codex (27.2%)
Gemini 3.1 Pro (29.6%)
GPT-5.4, adaptive (63.3%)
Gemini 3 Pro, adaptive (92.6%)
0% 14% 85%
57% 95% >99%
67% 97% >99%
>99% >99% >99%
>99% >99% >99%
Figure 15: When one compromised agent can start an outbreak. (a) Smallest fan-out k at which a channel turns supercritical
(k·p>1 ) for the per-hop success rates that Table 4 reports. (b) Probability that one seed starts an outbreak that never dies
out, from a Galton–Watson branching process with Binomial(k,p) offspring. A broadcast channel such as StockAgent’s forum,
where every agent reads every post, has a fan-out equal to the number of agents minus one.
The model turns three qualitative concerns into design rules.
First, hardening the model and limiting fan-out trade off one
for one, because only their product matters. For example, a ten-
fold drop in per-hop success buys nothing if the channel’s fan-
out grows tenfold, and a broadcast forum like StockAgent’s,
where each post reaches every other agent (§6.3), pushes even
the most resistant model in Table 4 past the threshold once
the population exceeds ten agents. Second, the defenses that
work are those that reducek or p for whole channels: message
validation that treats peer output as data (S3-E3), provenance
that lets a receiver discount unverified content, and rate lim-
its that cap how many agents one message can reach. Third,
monoculture removes the variation in p that would otherwise
slow spread. Because 12 of 15 designs share one model fam-
ily, a payload tuned for that family meets the samep at almost
every hop.
Takeaway
Outbreak risk is the product of per-hop success and fan-
out, so model hardening alone cannot make a broadcast
channel safe. Even 10.7% per-hop success, the best fron-
tier rate in LivePI, makes any channel with ten or more
readers supercritical.
11 Open Problems and Research Agenda
The ratings, the code audit, and the two preceding sections
leave a set of problems that no single paper can close. We
state 14 of them. Each starts from a gap that our data ex-
poses, names what is known, and proposes a first step that
a team could take within a year. Figure 16 places the prob-
lems on the planes of Figure 11 and on a time horizon, and
30

Table 15 summarizes them. Existing agendas for multi-agent
security [66, 67] and surveys of agent threats [76] argue from
first principles and examples. The agenda below starts from
measured gaps, namely the controls that 15 published designs
and 7 code releases leave out.
11.1 Measuring the Problem
1. Empirical evidence for agent-to-market spillover.Six
schemes receive no credit on S3, and we found no study
that measures how far a compromised LLM agent moves a
market in which other LLM agents trade. Although LLM
market simulators exist [88, 122, 123] and attack studies mea-
sure harm inside one agent stack [61, 62], none combines a
shared order book, a population of heterogeneous agents, and
a controlled fraction of compromised ones. A first step is a
simulator with an exchange-grade matching engine in which
the fraction of compromised agents, the backbone mix, and
the channel fan-out of §10.4 are experimental variables, and
price impact, herding, and recovery time are outcomes. The
same testbed would let the community design and test circuit
breakers for agents, whose reaction times differ from those of
human traders.
2. Assessing deployed agents.Our ratings describe published
designs, and the audit shows that released code diverges from
them in 21 ratings upward and 3 downward (§6.3). Products
add a third layer that neither papers nor repositories reveal.
The AI Agent Index found that developers of deployed agents
publish ample information about capabilities but little about
safety and risk management [196]. A first step is a disclosure
template, the agent analogue of a model card, that asks de-
ployers which FARSIGHT controls they implement outside
the model, how fast their interrupt path is, and which inputs
they treat as untrusted.
3. Auditing agent code at scale.Our three LLM audit runs
agreed on 88.9% of ratings and 84.4% of indicator judgments,
which is useful but leaves room for systematic error. Because
the auditor saw our paper-level ratings, its labels may also
be anchored to them (Appendix D). The next questions are
whether blind audits converge to the same ratings, how to
calibrate an LLM auditor against human experts, and how to
combine LLM judgment with static analysis that cannot be
talked out of a finding. A shared benchmark of agent reposito-
ries with expert labels for each codebook indicator would let
the community measure auditors the way it measures models.
4. Harm metrics for third parties.Agent security bench-
marks report attack success rate on the attacked agent [96,
159,160]. The harms that make trading high-stakes fall on oth-
ers: counterparties who trade at manipulated prices, patients
who inherit a corrupted record, courts that receive fabricated
citations. Yet the field lacks metrics for these externalities,
such as the price impact per compromised dollar, the num-
ber of downstream decisions that read a poisoned record, or
the reproduction number of §10.4 measured on real channels.
Benchmarks that report such metrics would make the cost of
a vulnerability comparable across domains.
11.2 Building Defenses
5. Provenance and corroboration when sources are cor-
related.No scheme combines source provenance with cross-
source corroboration (Table 5), and both are harder than
they look. For example, corroboration assumes independent
sources, but syndication, shared wire services, and coordi-
nated posting make sources dependent, so an attacker who
controls one hub controls the majority. Provenance standards
for media, signed data feeds, and watermarks for generated
text [188] each cover part of the problem. A first step is a
corroboration rule that counts sources by their upstream in-
dependence, evaluated against an adversary who can create
sources cheaply.
6. Interlocks outside the model with bounded latency.No
paper describes an interrupt that does not wait for LLM infer-
ence, and no release enforces a loss limit outside the LLM.
For general-purpose agents, system-level designs that separate
control flow from untrusted data [197,198], enforce privileges
on tool calls [199, 200], or track information flow [201, 202]
show how to place a policy engine around an agent. The
missing piece is a trading-grade interlock whose worst-case
latency is bounded and verified, whose rules a regulator can
read, and whose inputs cannot carry injected content. Pre-
trade controls under Rule 15c3-5 and RTS 6 [140, 141] are
the specification to start from.
7. Memory integrity, forensics, and unlearning.Of the au-
dited releases, 4 store memory without validation and 2 load it
with pickle, and TradingAgents’ decision log can be forged
by model output that reproduces its delimiter (§6.3). Memory
injection succeeds more often than prompt injection against
Web3 agents, and prompt-injection defenses do little once the
stored context is corrupted [75]. Agents need tamper-evident
memory that records who wrote each entry, a quarantine for
unverified experience, and a way to undo the decisions that a
poisoned entry influenced. Forensic replay, which the recom-
mendations for R4 ask for, needs this record to exist first.
8. Breaking replication and bounding fan-out.The branch-
ing model shows that outbreak risk is the product of per-hop
success and fan-out (§10.4). Morris II’s guardrail detects self-
replicating prompts with a true-positive rate of 1.0 and a
false-positive rate of 0.015 in its evaluation [68], LLM tag-
ging reduces infection inside multi-agent systems [70], and
topology-guided detection on the utterance graph recovers
over 40% of the performance lost to prompt injection [169].
Agent Smith’s authors derive a condition under which a de-
fense provably restrains infectious jailbreaks but leave its
practical design open [69]. The open problem is a defense
that meets such a condition under adaptive attack [195], to-
gether with protocol-level fan-out limits for agent-to-agent
standards.
31

Inputs (S1) Agent (S2) Actions (R2, R3) Propagation (S3) Oversight and governance
Near
term
Mid
term
Long
term
3 Auditing agent code at scale 6 Interlocks outside the model 4 Harm metrics for third parties
2 Assessing de- ployed agents
10 Codebooks for other domains
5 Provenance with correlated sources 7 Memory integrity and unlearning
1 Spillover testbeds
8 Breaking replica- tion
12 Identity and delega- tion
13 Regulation and incident reports
14 Agents reading agents 9 Diversity against monoculture 11 Oversight at ma- chine speed
Figure 16: Research agenda. The 14 open problems of §11 placed on the planes of the domain-independent model (Figure 11)
and on a time horizon. Near-term problems need engineering and shared benchmarks, mid-term problems need new defenses or
testbeds, and long-term problems need advances in science and governance.
9. Diversity against monoculture.In our corpus, 12 of the
15 schemes share one model family, and errors are correlated
even across providers [81]. N-version programming tolerated
software faults by running independently developed versions
and voting [203]. The same idea protects agents only if differ-
ent backbones fail independently under attack. A first step is
to measure the joint success rate of the same payloads against
pairs of backbones and to ask whether a committee of diverse
models raises the cost of a market-moving attack enough to
justify its latency.
11.3 Generalization and Governance
10. Codebooks for other high-stakes domains.Table 11 sug-
gests which FARSIGHT indicators transfer unchanged (prove-
nance, out-of-model limits, memory gates, peer-message val-
idation) and which need domain content (what counts as an
early warning in a hospital, or as an interrupt in a law firm).
A first step is to apply a healthcare codebook to published
clinical agents such as AgentClinic, Agent Hospital, and Po-
laris [158, 163, 165], and a legal codebook to drafting and
research agents, and to compare their rating distributions with
Figure 5. If the same controls are missing there, the cause
lies in how agents are designed, and finance is only where it
shows first.
11. Human oversight at machine speed.Every domain in
Figure 12 that relies on a human gate rates medium on re-
liance on in-model safety, because the human is the control.
Human review fails in predictable ways. Automation bias
leads reviewers to accept wrong advice [167], and automation
leaves operators least practiced exactly when they must take
over [204]. In trading, a human cannot review a decision that
must happen within a second. The open problem is to decide
which actions deserve a human gate (irreversible, large, or
unfamiliar ones), how much time the gate needs, and how
to keep reviewers alert when nearly every draft they see is
correct.
12. Identity, delegation, and accountability.If a cascade
crosses firms, attribution requires knowing which agent acted
for whom. Proposals for agent identifiers, activity logs, and
real-time monitoring [205, 206], and for authenticated dele-
gation built on OAuth 2.0 and OpenID Connect [207], give
agents verifiable principals. Agent-to-agent protocols and
MCP need the same properties for messages and tools [155].
Open questions include how to scope a delegation so that an
injected instruction cannot widen it, and how to revoke an
agent’s authority across every service it touches within the
time a market cascade takes.
13. Mapping regulation to agent controls and reporting
incidents.The controls that the schemes lack are already
mandatory for algorithmic trading [140, 141], and regulators
now ask about correlated trading by AI agents [11,13]. Health-
care and law have their own anchors in order-entry checks
and attorney verification duties [153, 154]. Yet we know of
no public mapping that translates these duties into agent con-
trols that an auditor can check. Aviation collects near misses
and the AI Incident Database collects AI failures [208], but
agent failures lack a shared taxonomy that names where in
the agent they occurred. The FARSIGHT indicators offer a
starting vocabulary for such a mapping, and an incident tax-
onomy indexed by surface (S1–S3) and phase (R1–R4) would
let reports from different domains be compared.
14. Agents that read what agents write.Prices, records, case
law, and the web increasingly contain text and signals that
agents produced. If models train on such text, they degrade
32

Table 15: Open problems at a glance: the gap in our data that motivates each problem, the surfaces and domains it touches, and a
first step.
# Open problem Gap in our data Surfaces Domains First step
1 Agent-to-market spillover 6 schemes have no S3 control; no
study measures spillover
S3 Trading Shared-order-book simulator with a controlled
fraction of compromised agents
2 Assessing deployed agents Code differs from paper in 21 + 3 of
63 ratings
All All Disclosure template for out-of-model controls
3 Auditing code at scale LLM audit runs agree on 88.9% of
ratings
All All Expert-labeled benchmark of agent repositories
4 Harm metrics for third
parties
Benchmarks score only the attacked
agent
S3 All Report price impact, downstream reads,
reproduction number
5 Provenance with correlated
sources
No scheme combines provenance and
corroboration
S1 All Count sources by upstream independence
6 Interlocks outside the
model
No interrupt without inference; no
enforced loss limit
R2, R3 All Latency-bounded, verified policy engine based on
Rule 15c3-5 and RTS 6
7 Memory integrity and
unlearning
4 releases store memory unvalidated, 2
withpickle
S2.3, R4 All Tamper-evident memory with quarantine and
rollback of affected decisions
8 Breaking replication Fan-out 10 suffices even at 10.7%
per-hop success
S3, S2.1 Multi-agent Defense with a provable spread bound under
adaptive attack
9 Diversity against
monoculture
12 of 15 schemes share one model
family
S2, S3 All Joint attack success across backbone pairs
10 Codebooks for other
domains
Controls missing for design reasons,
not finance
All Healthcare, law Rate published clinical and legal agents with
adapted indicators
11 Oversight at machine speed Human gates fail under automation
bias
R2, R3 Healthcare, law Decide which actions get a human gate and how
long it needs
12 Identity and delegation Cascades cross firms without
attribution
S3 All Scoped, revocable delegation for agent protocols
13 Regulation and incident
reports
Mandatory controls exist but are not
mapped to agents
All All Incident taxonomy indexed by surface and phase
14 Agents reading agents Inputs increasingly written by agents S1, S3 All Provenance and friction in the fastest channels
over generations [187], and when agents read each other’s
outputs, they can lock into the informational cascades that
economists describe for people [179]. The long-term question
is how an information environment stays reliable when most
of its writers and readers are agents. Provenance for generated
content, diversity of sources, and deliberate friction in the
fastest channels are candidate answers, and none has been
tested at the scale at which agents now operate.
Actions for each community.The problems above take
years, but four groups can act on our findings today.Agent
researcherscan report FARSIGHT ratings for new designs,
release code that matches the paper, and evaluate attacks by
their effect on other agents, not only on the target.Builders
and deployerscan move every limit that matters out of the
prompt: corroborate sources before acting, keep an interrupt
path that does not call the model, cap positions and fan-out,
validate memory writes, and never execute model-written
code on the host.Researchers in other high-stakes domains
can apply the codebook of Appendix B with the substitutions
of Table 11 and test whether their agents repeat the pattern we
found.Regulators and standards bodiescan ask agent deploy-
ers the questions that Rule 15c3-5 already asks of algorithmic
traders, and require incident reports that name the surface and
the phase in which a failure occurred.
12 Discussion
The 15 schemes trade stocks, and the first agents that brokers
opened to retail customers did too. This section asks what
changes when the same agents trade options (§12.1), then
discusses the deployment questions that our ratings raise, the
limitations of this work, and its potential harms (§12.2).
12.1 Options Agents: More Decisions, Lower
Floors
Options are the next market that agents enter, and they raise
the stakes of every surface in FARSIGHT. Robinhood an-
nounced in July 2026 that every US customer can now let an
agent trade options [209], and tastytrade publishes an MCP
server through which an agent with write access can trade
options on stocks, indexes, and futures, multi-leg orders in-
cluded [210]. The market that these agents enter is large and
increasingly short-dated. In July 2026, contracts that expire
on the day they trade accounted for a record 66.2% of all
S&P 500 index-options volume [211], and by mid-2026 their
volume was up 46.2% year to date, at more than 20 million
contracts a day [212].
One decision becomes five.A stock order gives an attacker
33

/file-inv⌢ice-d⌢llarStock order
Direction buy or sell
Size shares
Worst case: the wrong direction.
A loss without bound needs an
explicit short, the decision that
risk checks already watch.
checked by direction-based tests
corruptible with the right direction
/file-c⌢ntractOptions order
Direction call or put, long or short
Strike sets the breakeven
Expiry sets the deadline
Implied volatility sets the price paid
Legs set the maximum loss
Size contracts
With the direction still correct
/check-circlea direction check passes
the move never reaches the breakeven
the catalyst arrives after expiry
volatility collapses after the event
a $400 cap becomes $9,900, or none
/user-secreta counterparty fills the visible order
Figure 17: An options order carries five decisions where a stock order carries one. An attacker can corrupt four of them (red)
without touching the direction the agent chose, so a check that compares the order’s direction with the agent’s own analysis passes
while the strike, expiry, volatility, or legs carry the loss. In a thin contract, the order itself can reveal the agent to a counterparty
who trades against it.
one decision to corrupt, the direction, plus a size that risk
limits already bound. An options order carries five decisions:
the direction, the strike that sets the breakeven, the expiry that
sets the deadline, the implied volatility that sets the price paid,
and the legs that set the maximum loss. Figure 17 contrasts
the two orders. The four added fields share one property
that makes them dangerous. An attacker can move each of
them while the agent’s view of the market stays correct, so a
check that compares the order’s direction with the agent’s own
analysis passes. Attack studies on equities agents measure
whether a decision flips or a profit falls [59, 63], and neither
measure registers an attack that leaves the decision intact.
Losing with the right view.Each added field turns a correct
view into a loss in its own way. A call bought at a strike
far above the expected move expires worthless even if the
stock rises, and an expiry chosen before the catalyst ends
the position before the news arrives. V olatility is subtler. Be-
fore a scheduled event, option prices embed a high implied
volatility that usually collapses once the event passes, so an
agent persuaded to buy just before an earnings release pays
for a move that the market had already priced in. Figure 18(b)
shows such a case. A call bought at 80% implied volatility
loses money once implied volatility drops to 25%, unless the
stock gains more than 8.7%. None of these losses requires a
false headline. Urgent framing (“two days left”) or an inflated
volatility statistic is enough, and both are hard to catch, be-
cause the Greeks and implied volatility come out of a pricing
model [213] and cannot be checked against a price chart.
One missing leg removes the floor.The worst case needs no
change of direction at all. Traders cap the risk of a written
option by buying a further option of the same expiry, and the
bound then comes from the pair, not from either leg [214].
Remove the protective leg and the same view becomes an
uncovered position. Figure 18(a) uses a bull put spread, short
the 100 put and long the 95 put, which collects a $1.00 credit
and can lose at most $400 per contract. Without the long put,
the position can lose $9,900, about 25 times as much, and an
uncovered call has no bound at all, because a stock price has
none [215]. On a stock, an unbounded position requires an
explicit short, which is the decision that risk checks already
watch. On an option, it requires only that the agent be talked
out of a leg that, in most months, looks like a cost that never
pays. The pattern has a precedent with human traders. In
2018, after natural gas jumped 18%, a fund that had sold
uncovered options on it informed about 290 clients that their
money was gone and that they might owe their clearing broker
more [216].
The counterparty can be the attacker.Options add a chan-
nel that pays the attacker directly. Liquidity is split across
many strikes and expiries, so a single contract trades thinly,
and retail option flow is concentrated: nearly 90% of pay-
ment for order flow goes to three wholesalers [217], which
specialize in executing against retail option orders [218]. In
a thin contract, an agent that trades by fixed rules can be the
only visible interest, and its displayed orders reveal its entry
conditions, strikes, and timing. An adversary who learns these
rules can publish an input that triggers the agent’s next order
and then fill that order as its counterparty. Each trade is small
and ordinary, the victim’s loss is the attacker’s profit, and the
attack survives a ban on uncovered writing because it needs
only bought premium.
Option flow reaches the stock market.Options also widen
the S3 surface of Section 10. Dealers who sell options hedge
them in the underlying, and when they are short gamma,
the hedging trades in the direction of the price move. That
hedging demand has been linked to intraday momentum
across futures markets [219]. Correlated option orders from
many agents that share one input can therefore move the
stock through the dealers who take the other side, a shared-
environment channel that needs no compromised receiver.
34

Table 16: Stock orders and options orders compared from the attacker’s side. Each row names a property of the order or its
market, and the last column states what the property gives an attacker who can write text that the agent reads.
Property Stock order Options order What it gives the attacker
Decisions in the order Direction, plus size Direction, strike, expiry, implied
volatility, and legs, plus size
Four fields to move while the direction stays
correct
Worst case Capital committed; no bound
only for an explicit short [215]
No bound for an uncovered call; one
dropped leg removes the cap of a
spread [214]
A choice of risk class, not just of direction
Loss with a correct
view
Rare, since a correct view gains Common: a strike the move never
reaches, a late move, or a volatility
collapse
Harm that a direction check reports as correct
Numbers a reviewer
can check
Price and volume, visible on a
chart
Greeks and implied volatility, derived
from a pricing model [213]
Misstated values that few reviewers can catch
Liquidity Deep books and tight spreads Thin books per contract and wide spreads A displaced strike or expiry pays the spread
Visibility of the agent’s
orders
Anonymous in a deep book Possibly the only displayed interest in a
contract; flow concentrated at three
wholesalers [217]
Profiling of a fixed-rule agent, then trading
against it
Lifecycle events None Exercise, assignment, and pin risk,
compressed into hours for contracts that
expire the same day [212]
Unplanned positions from events the agent
mishandles
Effect on other markets Orders move the stock Dealer hedging carries option flow into
the stock [219]
A second route from agent orders to prices (S3)
Controls for options agents.Table 16 summarizes the dif-
ferences, and each row points to a control that works without
detecting manipulated text. The loss limit that R3 asks for
must be the maximum loss of the whole position at expiry,
computed from all legs before entry and enforced outside
the model, because a notional or premium limit does not see
a dropped leg. Agent orders should default to defined-risk
structures, and every leg, strike, and expiry should be checked
against the plan the agent stated before it read new inputs.
Greeks and implied volatility should be recomputed from the
option chain, not taken from text. A ban on uncovered writing
helps, but it is a platform rule that a product change can lift,
and it leaves the strike, expiry, volatility, and counterparty
channels open. Finally, agents that trade thin contracts should
randomize timing and size or route through mechanisms that
hide them, so that their rules are harder to learn.
Takeaway
On options, an attacker does not need to flip a decision.
Four of the five fields of an options order can be corrupted
while the direction stays correct, a single dropped leg turns
a bounded loss into an unbounded one, and the attacker
can profit as the counterparty. Every FARSIGHT surface
carries over, and each becomes more costly.
12.2 Deployment, Practice, and Scope
Flash crashes versus normal pullbacks.V olatility is a nor-
mal feature of markets, so our robustness metrics target ad-
versarial flash crashes, not ordinary price moves. The two
differ in explainability. A normal pullback follows identifi-
able fundamentals or news, such as an earnings miss or a rate
decision, and is interpretable and, in principle, recoverable.
An adversarial flash crash is deliberately manufactured, de-
coupled from fundamentals, and leaves participants unable
to identify a cause. This lack of a clear cause is what makes
adversarial flash crashes dangerous, because an unexplained
drop can invite panic selling, stop-loss cascades, and quant-bot
liquidation, which feed back into trading agents and amplify
the shock.
Applicability to deployed systems.Our evaluation focuses
on academic schemes, which raises the question of whether
production financial agents share the same vulnerabilities.
Proprietary systems, such as those deployed by quantitative
hedge funds, are not publicly accessible for security audit-
ing, but three observations suggest that the risks we iden-
tify apply to them as well. First, production systems such as
RockAlpha [5], Composer [6], and Nof1.ai [8] employ archi-
tecturally similar patterns (LLM-driven signal interpretation,
API-based execution, and multi-source data ingestion) that
expose the same attack surfaces documented in our S1–S3
analysis. Second, the U.S. SEC’s establishment of a dedicated
AI Task Force [152] reflects regulatory recognition that LLM-
based trading agents pose systemic risks that merit oversight.
Third, the architectural weaknesses we identify (unverified
data ingestion, lack of prompt isolation, absence of circuit
breakers) follow from the speed-first ethos of financial sys-
tems, which production systems share. Production systems
operating under the same constraints are unlikely to have
solved these problems without explicit security engineering.
Practicality and latency.A natural concern is whether our
recommended defenses introduce unacceptable latency. The
35

0 50 100
−10k
−5k
0 spread: max loss $400
long put dropped:
max loss $9,900
(25×)
Stock price at expiry ($)
P&L per contract ($)
(a) One leg dropped
90 100 110 120
−10
−5
0
5
10
IV held
IV falls
stock up, losing
breakeven
+8.7%
Stock price after the event ($)
P&L per share ($)
(b) Volatility collapse
Figure 18: Losing money while the direction stays correct.
(a) A bull put spread (short 100 put, long 95 put, $1.00 net
credit) can lose at most $400 per contract. Without its long
put, the same view can lose $9,900, and the shading marks the
loss that the missing leg would have bounded. (b) A 30-day
at-the-money call bought at 80% implied volatility before a
scheduled event loses money once implied volatility drops
to 25%, unless the stock gains more than 8.7%. The shaded
band marks a correct directional view that still loses. Black–
Scholes values with illustrative parameters [213, 214].
fast path that we recommend for R2 runs outside the LLM
and adds rule checks instead of inference calls, so it short-
ens the reaction to a shock instead of lengthening it. The
remaining controls, such as source corroboration and pre-
committed loss limits, follow professional risk-hedging prac-
tice, including portfolio-level risk budgeting, volatility-regime
detection, and multi-leg hedging. Sub-second latency is also
not a binding constraint for strategies with daily or multi-day
holding periods, such asswing trading. For these strategies,
the agent’s edge lies in continuous, around-the-clock infor-
mation ingestion. Human traders cannot maintain constant
vigilance, whereas an autonomous agent monitors and rea-
sons over information streams without attentional lapses. The
trade-off between latency and returns across strategy hori-
zons remains to be measured. Faster LLM decisions alone,
however, do not make a population of agents safer. In our
simulated market, 400 agents that decide every 60 seconds in-
stead of every 240 deepen a 2010-sized crash to 35.9% instead
of 17.3%, because they sell into the fall sooner (§7.4).
Trading agents in the wild.Retail-built LLM trading agents
are already operating with real capital. On X, Reddit, and
Xiaohongshu (a major Chinese lifestyle and social-media plat-
form), users share live returns yet never disclose architectures.
Most of these agents are built through “vibe coding” (lightly
scaffolded, prompt-driven construction using tools such as
Claude Code or Cursor) with minimal programming expertise,
which lowers the deployment barrier while expanding the S1
attack surface. Because free data sources are limited in cover-
age, most no-code agents converge on a narrow set of feeds,
which enablessupply-side poisoning. An adversary offering
a free, high-quality-looking source could steer many agents
simultaneously withzero knowledge of their internals, risking
correlated trades and flash-crash amplification [20, 102]. The
same broad execution authority that makes autonomous trad-
ing attractive also means that, under a poisoned data feed, an
agent can propagate aggressive erroneous trades at the same
speed as legitimate ones. Trading agents therefore need aro-
bustnessandsecuritycodebook that holds under adversarial
and stochastic market conditions, which is what FARSIGHT
provides.
Limitations.Our ratings describe 15 published designs,
whose evidence comes from backtests, simulations, or case
studies with no real capital, and they cannot replace pene-
tration testing of running agents or of proprietary products
such as RockAlpha [5] and Robinhood’s agentic trading [7].
Because the indicators are read from papers, a ❍ means only
that a control is not evidenced. The code audit shows that
this gap runs both ways, covers only the 7 schemes with an
official release, and depends on how partial evidence counts,
since its agreement with the paper-level ratings drops from
39 to 31 of 63 ratings when partial indicators count as absent
(Appendix D). Finally, Sections 9–11 and §12.1 extend the
systematization by analysis. The domain profiles are our as-
sessment of the cited literature, no options agent was attacked,
and the branching model assumes independent hops, so its
thresholds describe the early phase of spread. The market
experiment is a one-asset model driven by decisions mea-
sured on a grid of market states, so its agent counts describe
a thinly traded stock and grow with depth (§7.5); calibrating
the ABIDES simulator [220] to one stock’s order book would
give the counts for that stock.
Potential harms.A systematization of attack surfaces can
guide attackers as well as defenders, and naming weaknesses
in released code points to concrete targets. We limit this risk
in three ways. We describe each surface at the level of de-
sign controls and release no attack code, payloads, or market-
moving content. The weaknesses we report in released code
concern research prototypes without order-execution paths,
and the authors of all 15 schemes received our assessment
before submission. The attacks we discuss, such as planting
false news or coordinating trades to move prices, are forms
of market manipulation that securities law already prohibits,
so they add little for an attacker but show deployers which
controls are missing. Finally, a partial or low-risk rating in
Table 5 certifies nothing about a deployed system, which adds
execution paths that the design and the released code lack.
36

13 Conclusion
We rated 15 academic trading agents with one codebook and
audited 7 code releases. No paper described a halt that by-
passes the LLM, and no release enforced a loss limit outside
it. In a simulated market, a few hundred agents that decided
as three LLMs did caused and amplified flash crashes that
the exchange pause missed, and a fast path and hard limits
stopped both. These controls belong outside the model.
Ethical Considerations
This work aims to help researchers and deployers build trad-
ing agents that are robust and secure. We assessed published
designs and audited released code statically. We ran no at-
tack against the authors’ systems, live markets, or produc-
tion trading infrastructure, and we release no attack code or
market-moving content. We confirmed each code-level weak-
ness that we report (§6.3) by reading the source rather than
by exploiting it.
Responsible disclosure.Before submission, we emailed the
first authors of all 15 schemes with the ratings and justifica-
tions for their scheme. The first author of StockAgent replied,
acknowledged that the design had not considered these issues,
and said that the team would improve the system accordingly.
We will reflect any further responses in the final version.
Open Science
We are committed to open science and to enabling indepen-
dent verification and reuse of our results. This systematiza-
tion is built entirely on publicly available academic papers;
the 15 evaluated financial LLM trading systems and their
original sources are cited throughout the paper. To make
our evaluation reproducible, we release a complete artifact
package containing: (i) the FARSIGHT codebook with all
evidence-based indicator definitions and deterministic scor-
ing rules (Appendix B); (ii) the per-agent evaluation data,
including every metric rating and its supporting justifica-
tion; and (iii) the structured prompts used for the LLM-
assisted literature analysis. All artifacts are available athttps:
//anonymous.4open.science/r/FARSIGHT-266A/ . The
repository link is anonymized for double-blind review, and we
will release the artifacts under an open-source license upon
acceptance.
References
[1] J. Kim, W. Guo, and D. Song, “SoK: Attack and De-
fense Landscape of Agentic AI Systems,” inUSENIX
Security Symposium, 2026.
[2] S. Raza, R. Sapkota, M. Karkee, and C. Emmanouilidis,
“TRiSM for Agentic AI: A Review of Trust, Risk, and
Security Management in LLM-based Agentic Multi-
Agent Systems,” Jul. 2025.
[3] N. Abbas, C. Cohen, D. J. Grolleman, and B. Mosk,
“Artificial intelligence can make markets more
efficient—and more volatile,” IMF Blog (October 15,
2024), 2024. [Online]. Available: https://www.imf.org/
en/blogs/articles/2024/10/15/artificial-intelligence-c
an-make-markets-more-efficient-and-more-volatile
[4] H. Ding, Y . Li, J. Wang, H. Chen, D. Guo, and Y . Zhang,
“Large language model agent in financial trading: A sur-
vey,” inProceedings of the 2026 9th International Con-
ference on Computers in Management and Business,
2026, pp. 76–83.
[5] RockFlow Technology, “RockAlpha: Real-money AI
investing arena,” https://rockalpha.rockflow.ai, 2025.
[6] Composer Technologies Inc., “Composer: Ai-powered
automated trading strategies,” https://www.composer.t
rade, 2025.
[7] Robinhood Markets, Inc., “Robinhood is now open to
agents,” Robinhood Newsroom, https://robinhood.com/
us/en/newsroom/robinhood-is-now-open-to-agents/,
2026.
[8] Nof1 AI Inc., “Alpha Arena: AI trading benchmark,”
https://nof1.ai, 2025.
[9] T. C. W. Lin, “Financial weapons of war,”
Minnesota Law Review, vol. 100, 2016, avail-
able: https://www.minnesotalawreview.org/wp-
content/uploads/2016/04/Lin_ONLINEPDF.pdf.
[10] N. Mulder, “The sanctions weapon,” IMF Finance
& Development Magazine, June 2022, discusses
the scale and spillover effects of modern sanctions
and financial statecraft. [Online]. Available: https:
//www.imf.org/en/Publications/fandd/issues/2022/06
/the-sanctions-weapon-mulder
[11] S. Breeden, “Agents of change,” Speech at the Euro-
pean Central Bank Forum on Central Banking (Sintra),
https://www.bankofengland.co.uk/speech/2026/june
/sarah-breeden-panel-at-the-european-central-bank-f
orum-on-central-banking-2026, Jun. 2026, bank of
England.
[12] American Banker, “72% of banks lack AI model ‘kill
switches,’ failure reporting,” https://www.americanba
nker.com/news/72-of-banks-lack-ai-model-kill-swi
tches-failure-reporting, 2026, reporting on the Wolters
Kluwer U.S. Banking AI Risk and Governance Index,
H1 2026 (survey of 230 U.S. banking professionals).
37

[13] P. Donachie, “Lawmakers press SEC on AI-Driven
stock trading,” https://www.wealthmanagement.com/a
rtificial-intelligence/lawmakers-press-sec-on-ai-tra
ding-agent-oversight, Jun. 2026, wealth Management,
25 June 2026. House Financial Services Democrats
(Reps. Foster and Sherman) letter to SEC Chair Atkins
on “correlated trading decisions and “herding behavior
from AI trading agents on registered brokerages; 13
questions with 31 July 2026 response deadline.
[14] Y . Yu, Z. Yao, H. Li, Z. Deng, Y . Jiang, Y . Cao, Z. Chen,
J. Suchow, Z. Cui, R. Liuet al., “Fincon: A synthe-
sized llm multi-agent system with conceptual verbal
reinforcement for enhanced financial decision making,”
Advances in Neural Information Processing Systems,
vol. 37, pp. 137 010–137 045, 2024.
[15] Y . Xiao, E. Sun, D. Luo, and W. Wang, “TradingAgents:
Multi-Agents LLM financial trading framework,”
arXiv preprint arXiv:2412.20138, 2024. [Online].
Available: https://arxiv.org/abs/2412.20138
[16] W. W. Li, H. Kim, M. Cucuringu, and T. Ma, “Can
LLM-based financial investing strategies outperform
the market in long run?” inProceedings of the 32nd
ACM SIGKDD Conference on Knowledge Discovery
and Data Mining V .1, 2026, pp. 2711–2722.
[17] Y . Chen, Y . Cao, J. Keung, L. Gan, K. Kuang,
Y . Jiang, Z. Ma, J. Zhu, F. Wu, and J. Li,
“MM-ARC: Multimodal adaptive routing of capital
with Robustness-Audited strategy pools,”arXiv
preprint arXiv:2509.05080, 2025. [Online]. Available:
https://arxiv.org/abs/2509.05080
[18] A. Kirilenko, A. S. Kyle, M. Samadi, and T. Tuzun,
“The flash crash: High-frequency trading in an elec-
tronic market,”The Journal of Finance, vol. 72, no. 3,
pp. 967–998, 2017.
[19] U.S. Commodity Futures Trading Commission and
U.S. Securities and Exchange Commission, “Findings
regarding the market events of may 6, 2010: Report of
the staffs of the CFTC and SEC to the joint advisory
committee on emerging regulatory issues,” https://ww
w.sec.gov/news/studies/2010/marketevents-report.pd
f, Sept. 2010.
[20] IT Brew, “The flash crash of 2010 offers warning as ai
automates,”IT Brew, June 2025. [Online]. Available:
https://www.itbrew.com/stories/2025/06/16/the-flash
-crash-of-2010-offers-warning-as-ai-automates
[21] O. Godbole, “Robinhood’s agentic AI trades 24/7, and
you carry the risk,” CoinDesk, https://www.coindesk
.com/markets/2026/09/30/robinhood-is-giving-custo
mers-an-ai-agent-that-trades-for-them-plus-10x-cry
pto-bets, 2026.
[22] Y . Xia, P. You, T. Wang, F. Liu, H. Qi, X. Wu,
and S. Zhang, “Agentic trading: When LLM agents
meet financial markets,” 2026. [Online]. Available:
https://arxiv.org/abs/2605.19337
[23] U.S. Securities and Exchange Commission, “Litigation
release no. 16671: SEC v. mark s. jakob,” https://www.
sec.gov/enforcement-litigation/litigation-releases/lr-1
6671, 2000.
[24] ——, “Order approving, on a pilot basis, the national
market system plan to address extraordinary market
volatility,” https://www.sec.gov/files/rules/sro/nms/2
012/34-67091.pdf, 2012, release No. 34-67091.
[25] L. Zhao, A. Bhaskar, and E. Dobriban, “LivePI:
More realistic benchmarking of agents against indirect
prompt injection,”arXiv preprint arXiv:2605.17986,
2026. [Online]. Available: https://arxiv.org/abs/2605.1
7986
[26] K. Greshake, S. Abdelnabi, S. Mishra, C. Endres,
T. Holz, and M. Fritz, “Not what you’ve signed up
for: Compromising real-world LLM-integrated appli-
cations with indirect prompt injection,” inProceedings
of the 16th ACM Workshop on Artificial Intelligence
and Security (AISec ’23), 2023.
[27] Y . Liu, Y . Jia, R. Geng, J. Jia, and N. Z. Gong, “Formal-
izing and benchmarking prompt injection attacks and
defenses,” inProceedings of the 33rd USENIX Security
Symposium, 2024.
[28] X. Shen, Z. Chen, M. Backes, Y . Shen, and Y . Zhang,
““Do anything now”: Characterizing and evaluating in-
the-wild jailbreak prompts on large language models,”
inProceedings of the 2024 ACM SIGSAC Conference
on Computer and Communications Security (CCS),
2024.
[29] N. Carlini, M. Jagielski, C. A. Choquette-Choo,
D. Paleka, W. Pearce, H. Anderson, A. Terzis,
K. Thomas, and F. Tramèr, “Poisoning web-scale train-
ing datasets is practical,” inProceedings of the 2024
IEEE Symposium on Security and Privacy (S&P),
2024.
[30] Z. Chen, Z. Xiang, C. Xiao, D. Song, and B. Li, “Agent-
Poison: Red-teaming LLM agents via poisoning mem-
ory or knowledge bases,” inAdvances in Neural Infor-
mation Processing Systems (NeurIPS), 2024.
[31] Y . Ruan, H. Dong, A. Wang, S. Pitis, Y . Zhou, J. Ba,
Y . Dubois, C. J. Maddison, and T. Hashimoto, “Iden-
tifying the risks of LM agents with an LM-emulated
sandbox,” inInternational Conference on Learning
Representations (ICLR), 2024.
38

[32] N. Papernot, P. McDaniel, A. Sinha, and M. P. Well-
man, “SoK: Security and privacy in machine learning,”
in2018 IEEE European Symposium on Security and
Privacy (EuroS&P), 2018, pp. 399–414.
[33] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit,
L. Jones, A. N. Gomez, Ł. Kaiser, and I. Polosukhin,
“Attention is all you need,” inAdvances in Neural In-
formation Processing Systems, 2017.
[34] OpenAI, “GPT-4 technical report,” 2023.
[35] H. Touvron, T. Lavril, G. Izacard, X. Martinet, M.-A.
Lachaux, T. Lacroix, B. Rozière, N. Goyal, E. Ham-
bro, F. Azhar, A. Rodriguez, A. Joulin, E. Grave, and
G. Lample, “LLaMA: Open and efficient foundation
language models,”arXiv preprint arXiv:2302.13971,
2023.
[36] A. Q. Jiang, A. Sablayrolles, A. Roux, A. Menschet al.,
“Mixtral of experts,”arXiv preprint arXiv:2401.04088,
2024.
[37] Anthropic, “The Claude 3 model family: Opus, Sonnet,
Haiku,” Model Card, https://assets.anthropic.com/m/6
1e7d27f8c8f5919/original/Claude-3-Model-Card.pdf,
2024.
[38] L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. Wain-
wright, P. Mishkin, C. Zhang, S. Agarwal, K. Slama,
A. Rayet al., “Training language models to follow in-
structions with human feedback,”Advances in neural
information processing systems, vol. 35, pp. 27 730–
27 744, 2022.
[39] Y . Gao, Y . Xiong, X. Gao, K. Jia, J. Pan, Y . Bi, Y . Dai,
J. Sun, M. Wang, and H. Wang, “Retrieval-augmented
generation for large language models: A survey,”arXiv
preprint arXiv:2312.10997, 2023.
[40] S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran,
K. Narasimhan, and Y . Cao, “ReAct: Synergizing
reasoning and acting in language models,” in
International Conference on Learning Representations
(ICLR), 2023. [Online]. Available: https://arxiv.org/ab
s/2210.03629
[41] G. Wang, Y . Xie, Y . Jiang, A. Mandlekar, C. Xiao,
Y . Zhu, L. Fan, and A. Anandkumar, “V oyager: An
open-ended embodied agent with large language mod-
els,”arXiv preprint arXiv:2305.16291, 2023.
[42] LangChain, “LangChain: Building applications with
large language models,” https://github.com/langchain
-ai/langchain, 2023.
[43] Significant Gravitas, “AutoGPT: An autonomous GPT-
4 experiment,” https://github.com/Significant-Gravita
s/AutoGPT, 2023.
[44] A. Lopez-Lira, “Can large language models trade? Test-
ing financial theories with LLM agents in market sim-
ulations,”arXiv preprint arXiv:2504.10789, 2025.
[45] P. Saha, J. Lyu, A. Saxena, T. Zhao, and D. Mehta,
“Large language model agents for investment manage-
ment: Foundations, benchmarks, and research fron-
tiers,” inProceedings of the 6th ACM International
Conference on AI in Finance, 2025, pp. 736–744.
[46] S. Mahdavi, J. Chen, P. K. Joshi, L. H. Guativa, and
U. Singh, “Integrating Large Language Models in Fi-
nancial Investments and Market Analysis: A Survey,”
Jun. 2025.
[47] C. Zhang, X. Liu, Z. Zhang, M. Jin, L. Li, Z. Wang,
W. Hua, D. Shu, S. Zhu, X. Jin, S. Li, M. Du, and
Y . Zhang, “When AI Meets Finance (StockAgent):
Large Language Model-based Stock Trading in Simu-
lated Real-world Environments,” Sep. 2024.
[48] T. Guo, H. Shen, J. Huang, Z. Mao, J. Luo, B. Chen,
Z. Chen, L. Liu, B. Xia, X. Liu, Y . Ma, and M. Zhang,
“MASS: Muli-agent simulation scaling for portfolio
construction,” Sep. 2025.
[49] F. Xiong, X. Zhang, A. Feng, S. Sun, and C. You,
“QuantAgent: Price-Driven Multi-Agent LLMs for
High-Frequency Trading,” Sep. 2025.
[50] X. Li, Y . Zeng, X. Xing, J. Xu, and X. Xu,
“HedgeAgents: A balanced-aware multi-agent finan-
cial trading system,” inCompanion Proceedings of the
ACM on Web Conference 2025, 2025, pp. 296–305.
[51] L. Zhao, R. Sun, Z. Jiang, B. Yang, Y . Bai, M. Chen,
J. Li, and Z. Bai, “ContestTrade: A Multi-Agent Trad-
ing System Based on Internal Contest Mechanism,”
Aug. 2025.
[52] Y . Yu, H. Li, Z. Chen, Y . Jiang, Y . Li, J. W. Su-
chow, D. Zhang, and K. Khashanah, “FinMem: A
Performance-Enhanced LLM trading agent with lay-
ered memory and character design,”IEEE Transactions
on Big Data, vol. 11, no. 6, pp. 3443–3459, 2025.
[53] H. Yuan, S. Wang, and J. Guo, “Alpha-GPT 2.0:
Human-in-the-Loop AI for Quantitative Investment,”
Feb. 2024.
[54] Y . Dong, F. Wu, K. Zhang, Y . Dai, S. Zhang, W. Ye,
S. Chen, and Z.-Q. Cheng, “Large language model
agents in finance: A survey bridging research, practice,
and Real-World deployment,” inFindings of the Asso-
ciation for Computational Linguistics: EMNLP 2025,
2025, pp. 17 889–17 907.
39

[55] F. Hua, H. Yang, X. Hao, H. Zhang, B. Cao, Y . Qi,
J. Li, and J. Guo, “Agentic quantitative trading: A
survey of workflows, systems, and evaluation,”arXiv
preprint arXiv:2608.31041, 2026. [Online]. Available:
https://arxiv.org/abs/2608.31041
[56] H. Gong, “AI agents in financial markets: Architec-
ture, applications, and systemic implications,”FinTech,
vol. 5, no. 2, p. 34, 2026.
[57] Q. Zeng, Z. Zhao, Y . Yang, Y . Zhu, F. Liu, Z. Bi,
M. T. K. Wynn, K.-K. R. Choo, and H. Chen, “When
AI meets wall street: A survey on trustworthy AI
in fintech,”arXiv preprint arXiv:2605.30650, 2026.
[Online]. Available: https://arxiv.org/abs/2605.30650
[58] Q. Mao, J. Wang, Y . Liu, L. Zhu, C. Ma, and J. Yan,
“SoK: Security of Autonomous LLM Agents in Agentic
Commerce,” arXiv preprint arXiv:2604.15367, 2026.
[59] A. Rizvani, G. Apruzzese, and P. Laskov, “Adversar-
ial news and lost profits: Manipulating headlines in
LLM-Driven algorithmic trading,” in2026 IEEE Con-
ference on Secure and Trustworthy Machine Learning
(SaTML), 2026, pp. 849–866.
[60] Z. Liu, Y . Yu, Y . Cao, Y . Jiang, H. Li, Z. Lu, Y . Wang,
Y . Zheng, X. Guo, C. Y . Cheng, and S. Ananiadou,
“AutoRedTrader: Autonomous red teaming of trading
agents through synthetic misinformation injection,”
arXiv preprint arXiv:2605.09185, 2026. [Online].
Available: https://arxiv.org/abs/2605.09185
[61] C. Na, H. Ni, L. Szpruch, Z. Wang, D. Mehta, S. Na-
grecha, A. Lopez-Lira, C. Choi, Y . Lee, and J.-H. Lee,
“Poisoning agentic alpha: Adversarial vulnerabilities
across roles and architectures in Multi-Agent trading
systems,”arXiv preprint arXiv:2608.24069, 2026.
[Online]. Available: https://arxiv.org/abs/2608.24069
[62] Q. R. Sua, J. Dong, N. D. Thai, Y . Wen, C. Tan, and
Y .-S. Ong, “Contagion on the trading floor: How adver-
sarial signals spread in Multi-Agent trading systems,”
inMachine Learning and Knowledge Discovery in
Databases. Research Track. Springer Nature Switzer-
land, 2026, pp. 206–223.
[63] L. Yan, J. Mei, T. Zhou, L. Huang, J. Zhang,
D. Liu, and J. Shao, “TradeTrap: Are LLM-based
trading agents truly reliable and faithful?”arXiv
preprint arXiv:2512.02261, 2025. [Online]. Available:
https://arxiv.org/abs/2512.02261
[64] M. Apte, “Do LLM trading agents herd? a market mi-
crostructure stress test,” in2026 IEEE Symposium on
Computational Intelligence for Financial Engineering
and Economics (CIFEr), 2026, pp. 61–66.
[65] J. Ross, E. So, Z. D. Simone, C. Pozniak, and A. W.
Lo, “Why better models can create riskier systems: Ev-
idence from LLM agents in financial markets,”arXiv
preprint arXiv:2609.04373, 2026.
[66] C. S. de Witt, K. Krawiecka, I. Krawczuk, B. Ha-
gag, W. L. Anderson, P. Belcak, B. Bucknall,
X. Cai, A. Chopra, D. Cohen, R. F. D. Rosario,
A. Draguns, A. Gray, K. Katz, V . Mavroudis,
J. Mink, S. R. Motwani, J. Petit, L.-S. Rembeck,
C. Smith, J. Sotiropoulos, S. Young, S. Scheffler,
and M. Llewellyn, “Open challenges in Multi-Agent
security: Towards secure systems of interacting
AI agents,”arXiv preprint arXiv:2505.02077, 2025.
[Online]. Available: https://arxiv.org/abs/2505.02077
[67] L. Hammond, A. Chan, J. Clifton, J. Hoelscher-
Obermaier, A. Khan, E. McLean, C. Smith, W. Barfuss,
J. Foerster, T. Gaven ˇciak, T. A. Han, E. Hughes,
V . Kovaˇrík, J. Kulveit, J. Z. Leibo, C. Oesterheld, C. S.
de Witt, N. Shah, M. Wellman, P. Bova, T. Cimpeanu,
C. Ezell, Q. Feuillade-Montixi, M. Franklin, E. Kran,
I. Krawczuk, M. Lamparth, N. Lauffer, A. Meinke,
S. Motwaniet al., “Multi-Agent risks from advanced
AI,”arXiv preprint arXiv:2502.14143, 2025. [Online].
Available: https://arxiv.org/abs/2502.14143
[68] S. Cohen, R. Bitton, and B. Nassi, “Here comes
the AI worm: Unleashing zero-click worms that
target GenAI-Powered applications,”arXiv preprint
arXiv:2403.02817, 2024. [Online]. Available: https:
//arxiv.org/abs/2403.02817
[69] X. Gu, X. Zheng, T. Pang, C. Du, Q. Liu, Y . Wang,
J. Jiang, and M. Lin, “Agent smith: A single image
can jailbreak one million multimodal LLM agents
exponentially fast,” inProceedings of the International
Conference on Machine Learning (ICML), 2024.
[Online]. Available: https://arxiv.org/abs/2402.08567
[70] D. Lee and M. Tiwari, “Prompt infection: LLM-to-
LLM prompt injection within Multi-Agent systems,”
arXiv preprint arXiv:2410.07283, 2024. [Online].
Available: https://arxiv.org/abs/2410.07283
[71] H. Triedman, R. Jha, and V . Shmatikov, “Multi-Agent
systems execute arbitrary malicious code,”arXiv
preprint arXiv:2503.12188, 2025. [Online]. Available:
https://arxiv.org/abs/2503.12188
[72] D. A. Alber, Z. Yang, A. Alyakin, E. Yang, S. Rai, A. A.
Valliani, J. Zhang, G. R. Rosenbaum, A. K. Amend-
Thomas, D. B. Kurland, C. M. Kremer, A. Eremiev,
B. Negash, D. D. Wiggan, M. A. Nakatsuka, K. L.
Sangwon, S. N. Neifert, H. A. Khan, A. V . Save,
A. Palla, E. A. Grin, M. Hedman, M. Nasir-Moin,
X. C. Liu, L. Y . Jiang, M. A. Mankowski, D. L. Segev,
40

Y . Aphinyanaphongs, H. A. Riina, J. G. Golfinoset al.,
“Medical large language models are vulnerable to data-
poisoning attacks,”Nature Medicine, vol. 31, no. 2, pp.
618–626, 2025.
[73] J. Clusmann, D. Ferber, I. C. Wiest, C. V . Schneider,
T. J. Brinker, S. Foersch, D. Truhn, and J. N. Kather,
“Prompt injection attacks on vision language models
in oncology,”Nature Communications, vol. 16, no. 1,
2025.
[74] V . Magesh, F. Surani, M. Dahl, M. Suzgun,
C. D. Manning, and D. E. Ho, “Hallucination-
Free? assessing the reliability of leading AI legal
research tools,”arXiv preprint arXiv:2405.20362,
2024. [Online]. Available: https://arxiv.org/abs/2405.2
0362
[75] A. S. Patlan, P. Sheng, S. A. Hebbar, P. Mittal, and
P. Viswanath, “Real AI agents with fake memories:
Fatal context manipulation attacks on Web3 agents,”
arXiv preprint arXiv:2503.16248, 2025. [Online].
Available: https://arxiv.org/abs/2503.16248
[76] Z. Deng, Y . Guo, C. Han, W. Ma, J. Xiong, S. Wen,
and Y . Xiang, “AI agents under threat: A survey of
key security challenges and future pathways,”ACM
Computing Surveys, vol. 57, no. 7, pp. 1–36, 2025.
[77] S. Abdelnabi and E. Bagdasarian, “AI agents
may always fall for prompt injections,”arXiv
preprint arXiv:2605.17634, 2026. [Online]. Available:
https://arxiv.org/abs/2605.17634
[78] Financial Stability Board, “The financial stability im-
plications of artificial intelligence,” https://www.fsb.or
g/2024/11/the-financial-stability-implications-of-art
ificial-intelligence/, 2024.
[79] G. Gensler and L. Bailey, “Deep learning and financial
stability,”SSRN Electronic Journal, 2020.
[80] J. Daníelsson, R. Macrae, and A. Uthemann, “Artificial
intelligence and systemic risk,”Journal of Banking &
Finance, vol. 140, p. 106290, 2022.
[81] E. Kim, A. Garg, K. Peng, and N. Garg, “Correlated
errors in large language models,”arXiv preprint
arXiv:2506.07962, 2025. [Online]. Available: https:
//arxiv.org/abs/2506.07962
[82] M. McClellan, “AI and financial fragility: A frame-
work for measuring systemic risk in deployment of
generative AI for stock price predictions,”Journal of
Risk and Financial Management, vol. 18, no. 9, p. 475,
2025.
[83] J. Begin, B. Gho, S. Muppavarapu, T. Tsay, A. Mohan,
A. Shaik, R. Li, V . Sharma, and A. Vaidheeswaran,
“Preference optimization drives monoculture in LLM
prediction markets,”arXiv preprint arXiv:2606.26583,
2026.
[84] K. Ng, “From herding machines to autonomous agents:
A taxonomy of AI-Driven flash crash mechanisms and
the regulatory gap,”Journal of Risk and Financial Man-
agement, vol. 19, no. 9, p. 664, 2026.
[85] W. A. Brock and C. H. Hommes, “Heterogeneous be-
liefs and routes to chaos in a simple asset pricing
model,”Journal of Economic Dynamics and Control,
vol. 22, no. 8–9, pp. 1235–1274, 1998.
[86] M. Paddrik, R. Hayes, A. Todd, S. Yang, P. Beling, and
W. Scherer, “An agent based model of the E-Mini s&p
500 applied to flash crash analysis,” in2012 IEEE Con-
ference on Computational Intelligence for Financial
Engineering & Economics (CIFEr), 2012, pp. 1–8.
[87] S. Mignot, P. Pellizzari, and F. Westerhoff, “Fake news
and asset price dynamics,”Jahrbücher für Nation-
alökonomie und Statistik, vol. 244, no. 4, pp. 351–379,
2024.
[88] Y . Yang, Y . Zhang, M. Wu, K. Zhang, Y . Zhang,
H. Yu, Y . Hu, and B. Wang, “TwinMarket: A scalable
behavioral and social simulation for financial markets,”
inAdvances in Neural Information Processing
Systems (NeurIPS), 2025. [Online]. Available: https:
//arxiv.org/abs/2502.01506
[89] Z. Li, G. Wan, K. Chen, Y . Chen, Y . Zhao, P. Torr,
G. Ye, Z. Yin, and H. Chai, “Behavioral consistency
validation for LLM agents: An analysis of Trading-
Style switching through Stock-Market simulation,”
arXiv preprint arXiv:2602.07023, 2026. [Online].
Available: https://arxiv.org/abs/2602.07023
[90] M. Yu, S. Wang, G. Zhang, J. Mao, C. Yin, Q. Liu,
Q. Wen, K. Wang, and Y . Wang, “NetSafe: Exploring
the topological safety of multi-agent networks,”arXiv
preprint arXiv:2410.15686, 2024. [Online]. Available:
https://arxiv.org/abs/2410.15686
[91] J. tse Huang, J. Zhou, T. Jin, X. Zhou, Z. Chen,
W. Wang, Y . Yuan, M. R. Lyu, and M. Sap, “On the
resilience of LLM-Based Multi-Agent collaboration
with faulty agents,” inProceedings of the International
Conference on Machine Learning (ICML), 2025.
[Online]. Available: https://arxiv.org/abs/2408.00989
[92] T. Han, S. Nebelung, F. Khader, T. Wang, G. Mueller-
Franzes, C. Kuhl, S. Försch, J. Kleesiek, C. Haarburger,
K. K. Bressem, J. N. Kather, and D. Truhn,
41

“Medical foundation models are susceptible to
targeted misinformation attacks,”arXiv preprint
arXiv:2309.17007, 2023. [Online]. Available: https:
//arxiv.org/abs/2309.17007
[93] M. Dahl, V . Magesh, M. Suzgun, and D. E. Ho, “Large
legal fictions: Profiling legal hallucinations in large
language models,”Journal of Legal Analysis, vol. 16,
no. 1, pp. 64–93, 2024.
[94] X. Tang, Q. Jin, K. Zhu, T. Yuan, Y . Zhang, W. Zhou,
M. Qu, Y . Zhao, J. Tang, Z. Zhang, A. Cohan, D. Green-
baum, Z. Lu, and M. Gerstein, “Risks of AI scientists:
prioritizing safeguarding over autonomy,”Nature Com-
munications, vol. 16, no. 1, 2025.
[95] M. M. R. R. Akanda, A. Lacy, and N. Saxena, “SoK:
Inaccessible and insecure: An exposition of authenti-
cation challenges faced by blind and visually impaired
users in State-of-the-Art academic proposals,” in34th
USENIX Security Symposium (USENIX Security 25),
2025, pp. 1393–1413.
[96] E. Debenedetti, J. Zhang, M. Balunovic, L. Beurer-
Kellner, M. Fischer, and F. Tramèr, “Agentdojo: A dy-
namic environment to evaluate prompt injection attacks
and defenses for LLM agents,”Advances in Neural
Information Processing Systems, vol. 37, pp. 82 895–
82 920, 2024.
[97] Y . Chen, Z. Yao, Y . Liu, A. Xin, J. Ye, J. Yu, L. Hou,
and J. Li, “Stockbench: Can llm agents trade stocks
profitably in real-world markets?” 2025. [Online].
Available: https://arxiv.org/abs/2510.02209
[98] E. F. Fama, “Efficient capital markets: A review of
theory and empirical work,”The Journal of Finance,
vol. 25, no. 2, pp. 383–417, 1970.
[99] H. P. Minsky,Stabilizing an Unstable Economy. Yale
University Press, 1986.
[100] F. A. Hayek,Prices and Production. Routledge, 1931.
[101] National Institute of Standards and Technology, “The
NIST cybersecurity framework (CSF) 2.0,” National In-
stitute of Standards and Technology, Tech. Rep., 2024.
[102] B. GAMBINI, “With one false tweet, hack crash led to
real panic,”University at Buffalo News, 2015. [Online].
Available: https://www.buffalo.edu/ubnow/stories/2
015/05/karppi_hack_crash.html
[103] Y . Li, Y . Yu, H. Li, Z. Chen, and K. Khashanah, “Trad-
inggpt: Multi-agent system with layered memory and
distinct characters for enhanced financial trading per-
formance,”arXiv preprint arXiv:2309.03736, 2023.
[104] G. Fatouros, K. Metaxas, J. Soldatos, and D. Kyriazis,
“Can large language models beat wall street? Evaluat-
ing GPT-4’s impact on financial decision-making with
MarketSenseAI,”Neural Computing and Applications,
pp. 1–26, 2024.
[105] W. Zhang, L. Zhao, H. Xia, S. Sun, J. Sun, M. Qin,
X. Li, Y . Zhao, Y . Zhao, X. Caiet al., “A multimodal
foundation agent for financial trading: Tool-augmented,
diversified, and generalist,” inProceedings of the 30th
Acm Sigkdd Conference on Knowledge Discovery and
Data Mining, 2024, pp. 4314–4325.
[106] H. Yang, B. Zhang, N. Wang, C. Guo, X. Zhang, L. Lin,
J. Wang, T. Zhou, M. Guan, R. Zhang, and C. D. Wang,
“FinRobot: An Open-Source AI Agent Platform for
Financial Applications using Large Language Models,”
May 2024.
[107] Q. Ding, H. Shi, J. Guo, and B. Liu, “TradExpert: Rev-
olutionizing trading with mixture of expert LLMs,”
arXiv preprint arXiv:2411.00782, 2024.
[108] G. Xiong, Z. Deng, K. Wang, Y . Cao, H. Li,
Y . Yu, X. Peng, M. Lin, K. E. Smith, X.-Y . Liu,
J. Huang, S. Ananiadou, and Q. Xie, “FLAG-
Trader: Fusion LLM-Agent with gradient-based
reinforcement learning for financial trading,” in
Proceedings of the Annual Meeting of the Association
for Computational Linguistics (ACL), 2025. [Online].
Available: https://arxiv.org/abs/2502.11433
[109] F. Tian, F. D. Salim, and H. Xue, “TradingGroup: A
Multi-Agent Trading System with Self-Reflection and
Data-Synthesis,” Aug. 2025.
[110] G. Fatouros, K. Metaxas, J. Soldatos, and
M. Karathanassis, “MarketSenseAI 2.0: Enhancing
stock analysis through LLM agents,” in2025 IEEE
International Conference on Data Mining Workshops
(ICDMW), 2025, pp. 883–892.
[111] M. J. Page, J. E. McKenzie, P. M. Bossuyt, I. Boutron,
T. C. Hoffmann, C. D. Mulrow, L. Shamseer, J. M.
Tetzlaff, E. A. Akl, S. E. Brennan, R. Chou, J. Glanville,
J. M. Grimshaw, A. Hróbjartsson, M. M. Lalu, T. Li,
E. W. Loder, E. Mayo-Wilson, S. McDonald, L. A.
McGuinness, L. A. Stewart, J. Thomas, A. C. Tricco,
V . A. Welch, P. Whiting, and D. Moher, “The PRISMA
2020 statement: an updated guideline for reporting
systematic reviews,”BMJ, vol. 372, p. n71, 2021.
[112] Y . Li, B. Luo, Q. Wang, N. Chen, X. Liu, and B. He,
“CryptoTrade: A reflective LLM-based agent to guide
zero-shot cryptocurrency trading,” inProceedings of
the 2024 Conference on Empirical Methods in Natural
Language Processing, 2024, pp. 1094–1106.
42

[113] S. Fatemi and Y . Hu, “FinVision: A Multi-Agent frame-
work for stock market prediction,” inProceedings of
the 5th ACM International Conference on AI in Fi-
nance, 2024, pp. 582–590.
[114] J. Liu, “A Survey of Financial AI: Architectures, Ad-
vances and Open Challenges,” Nov. 2024.
[115] S. Joshi, “A Comprehensive Review of Gen AI Agents:
Applications and Frameworks in Finance, Investments
and Risk Domains,”International Journal of Innova-
tive Science and Research Technology, pp. 1339–1355,
May 2025.
[116] D. Batra, C. B. Hamill, J. Hartley, R. Okhrati, D. Sed-
don, H. Miller, R. Khraishi, and G. A. Cowan, “A Re-
view of LLM Agent Applications in Finance and Bank-
ing,” SSRN, 2025.
[117] S. Wang, Y . Zhao, Z. Liu, Q. Zou, and H. Wang, “De-
mystifying LLM Supply Chain Vulnerabilities in the
Wild: Distribution, Root Cause, and Real-World Im-
pact,” Feb. 2025.
[118] H. Zhang, J. Huang, K. Mei, Y . Yao, Z. Wang, C. Zhan,
H. Wang, and Y . Zhang, “Agent security bench (ASB):
Formalizing and benchmarking attacks and defenses
in LLM-based agents,” inInternational Conference
on Learning Representations (ICLR), 2025. [Online].
Available: https://arxiv.org/abs/2410.02644
[119] H. Li, Y . Cao, Y . Yu, S. R. Javaji, Z. Deng, Y . He,
Y . Jiang, Z. Zhu, K. Subbalakshmi, G. Xiong, J. Huang,
L. Qian, X. Peng, Q. Xie, and J. W. Suchow,
“INVESTORBENCH: A Benchmark for Financial
Decision-Making Tasks with LLM-based Agent,” Dec.
2024.
[120] Z. Chen, J. Chen, J. Chen, and M. Sra, “From Tasks to
Teams: A Risk-First Evaluation Framework for Multi-
Agent LLM Systems in Finance,” inICML 2025 Work-
shop on Reliable and Responsible Foundation Models,
2025.
[121] D. Emmanoulopoulos, O. Olby, J. Lyon, and N. R. Still-
man, “To Trade or Not to Trade: An Agentic Approach
to Estimating Market Risk Improves Trading Deci-
sions,” Jul. 2025.
[122] C. Papadakis, G. Filandrianos, A. Dimitriou, M. Lym-
peraiou, K. Thomas, and G. Stamou, “StockSim: A
Dual-Mode Order-Level Simulator for Evaluating
Multi-Agent LLMs in Financial Markets,” Jul. 2025.
[123] S. Gao, Y . Wen, M. Zhu, J. Wei, Y . Cheng, Q. Zhang,
and S. Shang, “Simulating Financial Market via Large
Language Model based Agents,” Jun. 2024.
[124] G. Cheng, H. Jin, W. Zhang, H. Wang, and J. Zhuang,
“Learning to conceal risk: Controllable multi-turn red
teaming for LLMs in the financial domain,” inProceed-
ings of the 64th Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers),
2026, pp. 41 005–41 020.
[125] S. P. Shah and A. V . Deshpande, “Enforcing Web Se-
curity Constraints for LLM-driven Robot Agents for
Online Transactions,” in2024 International Confer-
ence on Distributed Systems, Computer Networks and
Cybersecurity (ICDSCNC), Sep. 2024, pp. 1–6.
[126] S. Narula, J. Rafiei Asl, M. Ghasemigol, E. Blanco,
and D. Takabi, “Harmnet: A framework for adaptive
multi-turn jailbreak attacks on large language models,”
2025.
[127] H. Tang, L. Yan, Y . Zhao, S. Wang, J. Huang, and
D. Yin, “GRAF: Multi-turn jailbreaking via global
refinement and active fabrication,” 2025.
[128] Z. Ying, G. Zheng, Y . Huang, D. Zhang, W. Zhang,
Q. Zou, A. Liu, X. Liu, and D. Tao, “Towards under-
standing the safety boundaries of DeepSeek models:
Evaluation and findings,” 2025.
[129] Z. Zhou, J.-X. Shi, P.-X. Song, X.-W. Yang, Y .-X. Jin,
L.-Z. Guo, and Y .-F. Li, “Lawgpt: A chinese legal
knowledge-enhanced large language model,”arXiv
preprint arXiv:2406.04614, 2024.
[130] L. Zhu, X. Wang, and X. Wang, “JudgeLM:
Fine-tuned large language models are scalable
judges,” inInternational Conference on Learning
Representations (ICLR), 2025. [Online]. Available:
https://arxiv.org/abs/2310.17631
[131] X. Tang, A. Zou, Z. Zhang, Z. Li, Y . Zhao, X. Zhang,
A. Cohan, and M. Gerstein, “Medagents: Large lan-
guage models as collaborators for zero-shot medical
reasoning,” inFindings of the Association for Compu-
tational Linguistics: ACL 2024, 2024, pp. 599–621.
[132] S. Johri, J. Jeong, B. A. Tran, D. I. Schlessinger,
S. Wongvibulsin, L. A. Barnes, H.-Y . Zhou, Z. R. Cai,
E. M. Van Allen, D. Kimet al., “An evaluation frame-
work for clinical use of large language models in pa-
tient interaction tasks,”Nature medicine, vol. 31, no. 1,
pp. 77–86, 2025.
[133] M. Li, Y . Cheng, L. Bai, F. Cao, K. Lv, J. Liang, and
P. Lio, “Edullm: Leveraging large language models
and framelet-based signed hypergraph neural networks
for student performance prediction,” inForty-second
International Conference on Machine Learning, 2025.
43

[134] C. C. Moallemi and M. Saglam, “The cost of latency
in high-frequency trading,” Working Paper, 2009.
[Online]. Available: https://moallemi.com/ciamac/pa
pers/latency-2009.pdf
[135] J. Hasbrouck and G. Saar, “Low-latency trading,”Jour-
nal of Financial Markets, vol. 16, no. 4, pp. 646–679,
2013.
[136] LuxAlgo. (2025) Latency standards in trading systems.
[Online]. Available: https://www.luxalgo.com/blog/lat
ency-standards-in-trading-systems/
[137] CoinAPI. (2025) Crypto trading latency faq: 10
speed questions answered. [Online]. Available: https:
//www.coinapi.io/blog/crypto-trading-latency-faq/
[138] Bloomberg, “How a fake AI photo of a pentagon blast
went viral and briefly spooked stocks,” https://www.bl
oomberg.com/news/articles/2023-05-22/fake-ai-pho
to-of-pentagon-blast-goes-viral-trips-stocks-briefly,
2023.
[139] Semafor, “A fake eli lilly tweet drove its stock down
and reignited anger over insulin prices,” https://www.
semafor.com/article/11/11/2022/eli-lilly-stock-price
-tumbles-after-fake-tweet, 2022.
[140] U.S. Securities and Exchange Commission, “Risk
management controls for brokers or dealers with
market access,” Final rule adopting Rule 15c3-5,
75 Fed. Reg. 69792, 2010. [Online]. Available:
https://www.federalregister.gov/documents/2010/11/
15/2010-28303/risk-management-controls-for-broke
rs-or-dealers-with-market-access
[141] European Commission, “Commission delegated regu-
lation (EU) 2017/589 of 19 july 2016 supplementing
directive 2014/65/EU with regard to regulatory
technical standards specifying the organisational
requirements of investment firms engaged in algo-
rithmic trading,” Official Journal of the European
Union, L 87, pp. 417–448, 2017. [Online]. Available:
https://eur-lex.europa.eu/eli/reg_del/2017/589/oj
[142] D. Easley, M. M. López de Prado, and M. O’Hara,
“Flow toxicity and liquidity in a high-frequency world,”
The Review of Financial Studies, vol. 25, no. 5, pp.
1457–1493, 2012.
[143] H. Markowitz, “Portfolio selection,”The Journal of
Finance, vol. 7, no. 1, pp. 77–91, 1952.
[144] F. S. Mishkin,The Economics of Money, Banking, and
Financial Markets, 12th ed. Pearson, 2018.
[145] M. K. Brunnermeier, “Deciphering the liquidity and
credit crunch 2007–2008,”Journal of Economic Per-
spectives, vol. 23, no. 1, pp. 77–100, 2009.
[146] C. M. Reinhart and K. S. Rogoff,This Time Is Differ-
ent: Eight Centuries of Financial Folly. Princeton
University Press, 2009.
[147] A. Wei, N. Haghtalab, and J. Steinhardt, “Jailbroken:
How does LLM safety training fail?” inAdvances
in Neural Information Processing Systems (NeurIPS),
2023.
[148] A. Zou, Z. Wang, N. Carlini, M. Nasr, J. Z. Kolter, and
M. Fredrikson, “Universal and transferable adversarial
attacks on aligned language models,” 2023.
[149] F. Perez and I. Ribeiro, “Ignore previous prompt: At-
tack techniques for language models,” 2022.
[150] W. Yang, X. Bi, Y . Lin, S. Chen, J. Zhou, and X. Sun,
“Watch out for your agents! investigating backdoor
threats to LLM-based agents,” inAdvances in Neural
Information Processing Systems (NeurIPS), 2024.
[151] N. Carlini, F. Tramèr, E. Wallace, M. Jagielski,
A. Herbert-V oss, K. Lee, A. Roberts, T. Brown,
D. Song, Ú. Erlingsson, A. Oprea, and C. Raffel, “Ex-
tracting training data from large language models,” in
Proceedings of the 30th USENIX Security Symposium,
2021, pp. 2633–2650.
[152] U. Securities and E. Commission, “Sec creates task
force to tap artificial intelligence for enhanced in-
novation and efficiency across the agency,” https:
//www.sec.gov/newsroom/press-releases/2025-1
03-sec-creates-task-force-tap-artificial-intelligenc
e-enhanced-innovation-efficiency-across-agency,
Aug. 2025, press Release No. 2025-103.
[153] R. Kaushal, K. G. Shojania, and D. W. Bates, “Effects
of computerized physician order entry and clinical de-
cision support systems on medication safety: A system-
atic review,”Archives of Internal Medicine, vol. 163,
no. 12, p. 1409, 2003.
[154] U.S. District Court for the Southern District of New
York, “Mata v. avianca, inc.: Opinion and order on
sanctions,” https://www.nhd.uscourts.gov/sites/def
ault/files/pdf/Mata-v-Avianca-sanctions-order.PDF,
2023.
[155] X. Hou, Y . Zhao, S. Wang, and H. Wang, “Model con-
text protocol (MCP): Landscape, security threats, and
future research directions,”ACM Transactions on Soft-
ware Engineering and Methodology, vol. 35, no. 10,
pp. 1–37, 2026.
[156] Z. Lin, “Hidden prompts in manuscripts exploit AI-
Assisted peer review,”Communications of the ACM,
vol. 69, no. 7, pp. 53–56, 2026.
44

[157] J. T. Halloran, B. Radosevich, and G. Black, “MCP
safety audit: LLMs with the model context protocol al-
low major security exploits,” inAssurance and Security
for AI-enabled Systems 2026, 2026, p. 8.
[158] S. Schmidgall, R. Ziaei, C. Harris, E. Reis, J. Jopling,
and M. Moor, “AgentClinic: a multimodal agent
benchmark to evaluate AI in simulated clinical
environments,”arXiv preprint arXiv:2405.07960, 2024.
[Online]. Available: https://arxiv.org/abs/2405.07960
[159] Q. Zhan, Z. Liang, Z. Ying, and D. Kang, “InjecAgent:
Benchmarking indirect prompt injections in Tool-
Integrated large language model agents,”arXiv
preprint arXiv:2403.02691, 2024. [Online]. Available:
https://arxiv.org/abs/2403.02691
[160] H. Zhang, J. Huang, K. Mei, Y . Yao, Z. Wang, C. Zhan,
H. Wang, and Y . Zhang, “Agent security bench (ASB):
Formalizing and benchmarking attacks and defenses
in LLM-based agents,” inInternational Conference
on Learning Representations (ICLR), 2025. [Online].
Available: https://arxiv.org/abs/2410.02644
[161] P. Daian, S. Goldfeder, T. Kell, Y . Li, X. Zhao, I. Ben-
tov, L. Breidenbach, and A. Juels, “Flash boys 2.0:
Frontrunning in decentralized exchanges, miner ex-
tractable value, and consensus instability,” in2020
IEEE Symposium on Security and Privacy (SP), 2020,
pp. 910–927.
[162] T. Tu, M. Schaekermann, A. Palepu, K. Saab, J. Frey-
berg, R. Tanno, A. Wang, B. Li, M. Amin, Y . Cheng,
E. Vedadi, N. Tomasev, S. Azizi, K. Singhal, L. Hou,
A. Webson, K. Kulkarni, S. S. Mahdavi, C. Semturs,
J. Gottweis, J. Barral, K. Chou, G. S. Corrado, Y . Ma-
tias, A. Karthikesalingam, and V . Natarajan, “Towards
conversational diagnostic artificial intelligence,”Na-
ture, vol. 642, no. 8067, pp. 442–450, 2025.
[163] S. Mukherjee, P. Gamble, M. S. Ausin, N. Kant,
K. Aggarwal, N. Manjunath, D. Datta, Z. Liu,
J. Ding, S. Busacca, C. Bianco, S. Sharma, R. Lasko,
M. V oisard, S. Harneja, D. Filippova, G. Meixiong,
K. Cha, A. Youssefi, M. Buvanesh, H. Weingram,
S. Bierman-Lytle, H. S. Mangat, K. Parikh, S. Godil,
and A. Miller, “Polaris: A safety-focused LLM
constellation architecture for healthcare,”arXiv
preprint arXiv:2403.13313, 2024. [Online]. Available:
https://arxiv.org/abs/2403.13313
[164] A. A. Tierney, G. Gayre, B. Hoberman, B. Mattern,
M. Ballesca, P. Kipnis, V . Liu, and K. Lee, “Ambient
artificial intelligence scribes to alleviate the burden of
clinical documentation,”NEJM Catalyst, vol. 5, no. 3,
2024.
[165] J. Li, Y . Lai, W. Li, J. Ren, M. Zhang, X. Kang, S. Wang,
P. Li, Y .-Q. Zhang, W. Ma, and Y . Liu, “Agent hospital:
A simulacrum of hospital with evolvable medical
agents,”arXiv preprint arXiv:2405.02957, 2024.
[Online]. Available: https://arxiv.org/abs/2405.02957
[166] S. G. Finlayson, J. D. Bowers, J. Ito, J. L. Zittrain,
A. L. Beam, and I. S. Kohane, “Adversarial attacks on
medical machine learning,”Science, vol. 363, no. 6433,
pp. 1287–1289, 2019.
[167] K. Goddard, A. Roudsari, and J. C. Wyatt, “Automation
bias: a systematic review of frequency, effect media-
tors, and mitigators,”Journal of the American Medical
Informatics Association, vol. 19, no. 1, pp. 121–127,
2012.
[168] C. Guo, X. Liu, C. Xie, A. Zhou, Y . Zeng,
Z. Lin, D. Song, and B. Li, “RedCode: Risky
code execution and generation benchmark for code
agents,” inAdvances in Neural Information Processing
Systems (NeurIPS), 2024. [Online]. Available: https:
//arxiv.org/abs/2411.07781
[169] S. Wang, G. Zhang, M. Yu, G. Wan, F. Meng,
C. Guo, K. Wang, and Y . Wang, “G-Safeguard:
A Topology-Guided security lens and treatment on
LLM-based multi-agent systems,” inProceedings
of the Annual Meeting of the Association for
Computational Linguistics (ACL), 2025. [Online].
Available: https://arxiv.org/abs/2502.11127
[170] D. A. Boiko, R. MacKnight, B. Kline, and G. Gomes,
“Autonomous chemical research with large language
models,”Nature, vol. 624, no. 7992, pp. 570–578,
2023.
[171] A. M. Bran, S. Cox, O. Schilter, C. Baldassari, A. D.
White, and P. Schwaller, “Augmenting large language
models with chemistry tools,”Nature Machine Intelli-
gence, vol. 6, no. 5, pp. 525–535, 2024.
[172] Y . Zhang, T. Yu, and D. Yang, “Attacking Vision-
Language computer agents via pop-ups,”arXiv
preprint arXiv:2411.02391, 2024. [Online]. Available:
https://arxiv.org/abs/2411.02391
[173] I. Evtimov, A. Zharmagambetov, A. Grattafiori,
C. Guo, and K. Chaudhuri, “WASP: Benchmarking
web agent security against prompt injection attacks,”
inAdvances in Neural Information Processing
Systems (NeurIPS), 2025. [Online]. Available: https:
//arxiv.org/abs/2504.18575
[174] A. Robey, Z. Ravichandran, V . Kumar, H. Hassani, and
G. J. Pappas, “Jailbreaking LLM-Controlled robots,”
arXiv preprint arXiv:2410.13691, 2024. [Online].
Available: https://arxiv.org/abs/2410.13691
45

[175] E. H. Spafford, “The internet worm program: an analy-
sis,”ACM SIGCOMM Computer Communication Re-
view, vol. 19, no. 1, pp. 17–57, 1989.
[176] J. Kephart and S. White, “Directed-graph epidemio-
logical models of computer viruses,” inProceedings.
1991 IEEE Computer Society Symposium on Research
in Security and Privacy, 1991, pp. 343–359.
[177] D. Moore, V . Paxson, S. Savage, C. Shannon, S. Stani-
ford, and N. Weaver, “Inside the slammer worm,”IEEE
Security & Privacy, vol. 1, no. 4, pp. 33–39, 2003.
[178] U.S. Securities and Exchange Commission, “In the
matter of knight capital americas LLC,” https://www.
sec.gov/litigation/admin/2013/34-70694.pdf, 2013.
[179] S. Bikhchandani, D. Hirshleifer, and I. Welch, “A the-
ory of fads, fashion, custom, and cultural change as
informational cascades,”Journal of Political Economy,
vol. 100, no. 5, pp. 992–1026, 1992.
[180] M. K. Brunnermeier and L. H. Pedersen, “Market liq-
uidity and funding liquidity,”Review of Financial Stud-
ies, vol. 22, no. 6, pp. 2201–2238, 2008.
[181] S. Fish, Y . A. Gonczarowski, and R. I. Shorrer,
“Algorithmic collusion by large language models,”
arXiv preprint arXiv:2404.00806, 2024. [Online].
Available: https://arxiv.org/abs/2404.00806
[182] E. Calvano, G. Calzolari, V . Denicolò, and S. Pastorello,
“Artificial intelligence, algorithmic pricing, and collu-
sion,”American Economic Review, vol. 110, no. 10,
pp. 3267–3297, 2020.
[183] W. Dou, I. Goldstein, and Y . Ji, “AI-Powered trading,
algorithmic collusion, and price efficiency,”SSRN Elec-
tronic Journal, 2023.
[184] W. Zou, R. Geng, B. Wang, and J. Jia, “PoisonedRAG:
Knowledge corruption attacks to Retrieval-Augmented
generation of large language models,” inUSENIX
Security Symposium, 2025. [Online]. Available:
https://arxiv.org/abs/2402.07867
[185] Z. Liao, L. Mo, C. Xu, M. Kang, J. Zhang, C. Xiao,
Y . Tian, B. Li, and H. Sun, “EIA: Environmental
injection attack on generalist web agents for privacy
leakage,” inInternational Conference on Learning
Representations (ICLR), 2025. [Online]. Available:
https://arxiv.org/abs/2409.11295
[186] P. He, Y . Lin, S. Dong, H. Xu, Y . Xing, and
H. Liu, “Red-Teaming LLM Multi-Agent systems
via communication attacks,” inProceedings of the
Annual Meeting of the Association for Computational
Linguistics (ACL), 2025. [Online]. Available: https:
//arxiv.org/abs/2502.14847
[187] I. Shumailov, Z. Shumaylov, Y . Zhao, N. Papernot,
R. Anderson, and Y . Gal, “AI models collapse when
trained on recursively generated data,”Nature, vol. 631,
no. 8022, pp. 755–759, 2024.
[188] J. Kirchenbauer, J. Geiping, Y . Wen, J. Katz,
I. Miers, and T. Goldstein, “A watermark for large
language models,” inProceedings of the International
Conference on Machine Learning (ICML), 2023.
[Online]. Available: https://arxiv.org/abs/2301.10226
[189] J. Kleinberg and M. Raghavan, “Algorithmic monocul-
ture and social welfare,”Proceedings of the National
Academy of Sciences, vol. 118, no. 22, 2021.
[190] C. Toups, R. Bommasani, K. A. Creel, S. H.
Bana, D. Jurafsky, and P. Liang, “Ecosystem-level
analysis of deployed machine learning reveals
homogeneous outcomes,” inAdvances in Neural
Information Processing Systems (NeurIPS), 2023.
[Online]. Available: https://arxiv.org/abs/2307.05862
[191] R. Bommasani, K. A. Creel, A. Kumar, D. Jurafsky,
and P. Liang, “Picking on the same person: Does algo-
rithmic monoculture lead to outcome homogenization?”
inAdvances in Neural Information Processing Systems
35, 2022, pp. 3663–3678.
[192] T. Ju, Y . Wang, Y . Hua, X. Ma, P. Cheng, H. Zhao,
Y . Wang, L. Liu, J. Xie, Z. Zhang, and G. Liu, “Flood-
ing spread of manipulated knowledge in LLM-based
multi-agent communities,”Science China Information
Sciences, vol. 69, no. 7, 2026.
[193] C. C. Zou, W. Gong, and D. Towsley, “Code red worm
propagation modeling and analysis,” inProceedings of
the 9th ACM conference on Computer and communi-
cations security, 2002, pp. 138–147.
[194] R. Pastor-Satorras and A. Vespignani, “Epidemic
spreading in Scale-Free networks,”Physical Review
Letters, vol. 86, no. 14, pp. 3200–3203, 2001.
[195] M. Nasr, N. Carlini, C. Sitawarin, S. V . Schulhoff,
J. Hayes, M. Ilie, J. Pluto, S. Song, H. Chaud-
hari, I. Shumailov, A. Thakurta, K. Y . Xiao,
A. Terzis, and F. Tramèr, “The attacker moves
second: Stronger adaptive attacks bypass defenses
against llm jailbreaks and prompt injections,”arXiv
preprint arXiv:2510.09023, 2025. [Online]. Available:
https://arxiv.org/abs/2510.09023
[196] S. Casper, L. Bailey, R. Hunter, C. Ezell, E. Cabalé,
M. Gerovitch, S. Slocum, K. Wei, N. Jurkovic,
A. Khan, P. J. K. Christoffersen, A. P. Ozisik,
R. Trivedi, D. Hadfield-Menell, and N. Kolt, “The AI
agent index,”arXiv preprint arXiv:2502.01635, 2025.
[Online]. Available: https://arxiv.org/abs/2502.01635
46

[197] E. Debenedetti, I. Shumailov, T. Fan, J. Hayes, N. Car-
lini, D. Fabian, C. Kern, C. Shi, A. Terzis, and
F. Tramèr, “Defeating prompt injections by design,”
in2026 IEEE Conference on Secure and Trustworthy
Machine Learning (SaTML), 2026, pp. 587–618.
[198] L. Beurer-Kellner, B. Buesser, A.-M. Cre¸ tu,
E. Debenedetti, D. Dobos, D. Fabian, M. Fis-
cher, D. Froelicher, K. Grosse, D. Naeff, E. Ozoani,
A. Paverd, F. Tramèr, and V . V olhejn, “Design patterns
for securing LLM agents against prompt injections,”
arXiv preprint arXiv:2506.08837, 2025. [Online].
Available: https://arxiv.org/abs/2506.08837
[199] T. Shi, J. He, Z. Wang, H. Li, L. Wu, W. Guo, and
D. Song, “Progent: Securing AI agents with privilege
control,”arXiv preprint arXiv:2504.11703, 2025.
[Online]. Available: https://arxiv.org/abs/2504.11703
[200] Y . Wu, F. Roesner, T. Kohno, N. Zhang, and U. Iqbal,
“IsolateGPT: An execution isolation architecture
for LLM-Based agentic systems,” inNetwork and
Distributed System Security Symposium (NDSS), 2025.
[Online]. Available: https://arxiv.org/abs/2403.04960
[201] M. Costa, B. Köpf, A. Kolluri, A. Paverd,
M. Russinovich, A. Salem, S. Tople, L. Wutschitz,
and S. Zanella-Béguelin, “Securing AI agents
with Information-Flow control,”arXiv preprint
arXiv:2505.23643, 2025. [Online]. Available:
https://arxiv.org/abs/2505.23643
[202] F. Wu, E. Cecchetti, and C. Xiao, “System-Level
defense against indirect prompt injection attacks:
An information flow control perspective,”arXiv
preprint arXiv:2409.19091, 2024. [Online]. Available:
https://arxiv.org/abs/2409.19091
[203] A. Avizienis, “The N-Version approach to Fault-
Tolerant software,”IEEE Transactions on Software
Engineering, vol. SE-11, no. 12, pp. 1491–1501, 1985.
[204] L. Bainbridge, “Ironies of automation,”Automatica,
vol. 19, no. 6, pp. 775–779, 1983.
[205] A. Chan, C. Ezell, M. Kaufmann, K. Wei, L. Hammond,
H. Bradley, E. Bluemke, N. Rajkumar, D. Krueger,
N. Kolt, L. Heim, and M. Anderljung, “Visibility into
AI agents,” inThe 2024 ACM Conference on Fairness,
Accountability, and Transparency, 2024, pp. 958–973.
[206] A. Chan, K. Wei, S. Huang, N. Rajkumar, E. Per-
rier, S. Lazar, G. K. Hadfield, and M. An-
derljung, “Infrastructure for AI agents,”arXiv
preprint arXiv:2501.10114, 2025. [Online]. Available:
https://arxiv.org/abs/2501.10114
[207] T. South, S. Marro, T. Hardjono, R. Mahari, C. D.
Whitney, D. Greenwood, A. Chan, and A. Pentland,
“Authenticated delegation and authorized AI agents,”
arXiv preprint arXiv:2501.09674, 2025. [Online].
Available: https://arxiv.org/abs/2501.09674
[208] S. McGregor, “Preventing repeated real world AI fail-
ures by cataloging incidents: The AI incident database,”
inProceedings of the AAAI Conference on Artificial
Intelligence, 2021, pp. 15 458–15 463.
[209] Robinhood Markets, “Agentic options trading is now
available to all US customers,” https://x.com/Robinh
oodApp/status/2074206140557037865, 2026.
[210] tastytrade, “tastytrade/tastytrade-mcp: MCP server for
the tastytrade open API,” https://github.com/tastytrad
e/tastytrade-mcp, 2026.
[211] Cboe Global Markets, “Cboe global markets reports
trading volume for july 2026,” https://www.prnewswi
re.com/news-releases/cboe-global-markets-reports-t
rading-volume-for-july-2026-302844194.html, 2026.
[212] ——, “State of the options industry: Options market
continued to break records in Q2 2026,” https://www.
cboe.com/insights/posts/state-of-the-options-industr
y-options-market-continued-to-break-records-in-q-2
-2026, 2026.
[213] F. Black and M. Scholes, “The pricing of options and
corporate liabilities,”Journal of Political Economy,
vol. 81, no. 3, pp. 637–654, 1973.
[214] J. Hull,Options, Futures, and Other Derivatives.
Prentice-Hall International, 1997.
[215] U.S. Securities and Exchange Commission, “Investor
bulletin: An introduction to short sales,” https://www.
investor.gov/introduction-investing/general-resourc
es/news-alerts/alerts-bulletins/investor-bulletins-51,
2026.
[216] CNBC, “A risky natural gas bet gone awry leads to
weepy YouTube confessional video,” https://www.cn
bc.com/2018/11/21/a-risky-natural-gas-bet-gone-a
wry-leads-to-weepy-youtube-confessional.html, 2018.
[217] S. Bryzgalova, A. Pavlova, and T. Sikorskaya, “Re-
tail trading in options and the rise of the big three
wholesalers,”The Journal of Finance, vol. 78, no. 6,
pp. 3465–3514, 2023.
[218] T. Ernst and C. Spatt, “Payment for order flow and op-
tion internalization,”The Review of Financial Studies,
2026.
47

[219] G. Baltussen, Z. Da, S. Lammers, and M. Martens,
“Hedging demand and market intraday momentum,”
Journal of Financial Economics, vol. 142, no. 1, pp.
377–403, 2021.
[220] D. Byrd, M. Hybinette, and T. H. Balch, “ABIDES:
Towards High-Fidelity Multi-Agent market simulation,”
inProceedings of the 2020 ACM SIGSIM Conference
on Principles of Advanced Discrete Simulation, 2020,
pp. 11–22.
[221] M. L. McHugh, “Interrater reliability: the kappa statis-
tic,”Biochemia Medica, vol. 22, no. 3, pp. 276–282,
2012.
A Metric Assignment Criteria
To maximize reproducibility, we adopt anevidence-based
checklistmethodology for metric assignment. For each met-
ric, we define a set ofevidence indicators, concrete, binary
(present/absent) features that evaluators identify in the agent’s
published paper, including described mechanisms, system dia-
grams, and reported experiments. Three-level ratings (● Fully
Robust/Low Risk, ◆ Partial, ❍ Not Robust/High Risk) fol-
lowdeterministic scoring rulesbased on which indicators are
satisfied, eliminating subjective judgment from the scoring
step. The complete indicator definitions and scoring rules
for all nine evaluation metrics (R1–R4, S1, S2.1–S2.3, S3)
are provided in the codebook (Appendix B, Table 18). S2 is
decomposed into three sub-metrics, S2.1 (prompt-injection),
S2.2 (tool/API exploitation), and S2.3 (memory manipula-
tion), each scored independently, yielding nine ratings per
agent.
All 15 agents were independently scored by two evaluators.
Evaluator A is a domain expert with in-depth knowledge of
financial LLM agent architectures (including hands-on expe-
rience reproducing and extending TradingAgents-class sys-
tems). Evaluator B has a solid understanding of LLM security
fundamentals and financial markets but is not a specialist in
agent-level system design. Both evaluators applied the same
codebook (Appendix B) without discussion during the scor-
ing phase. Across all 15 agents × 9 metrics (135 individual
ratings), the two evaluators reached identical scores on 126
ratings, yielding a raw agreement rate of 93.3% and a Cohen’s
κ of 0.89, indicating near-perfect agreement [221]. The nine
disagreements were concentrated in metrics R3, R4, and S2.2,
where Evaluator B occasionally rated an agent asNot Ro-
bust( ❍) while Evaluator A assignedPartial( ◆). Root-cause
analysis showed that these discrepancies stemmed from Eval-
uator B’s incomplete familiarity with certain agent-internal
mechanisms, for example, implicit risk-adjustment loops in
memory-based agents, or tool-permission scoping embedded
in multi-agent communication protocols. Such mechanisms
are not apparent from surface-level paper descriptions but are
identifiable through deeper architectural reading. All disagree-
ments were resolved through joint discussion, and final scores
reflect the consensus ratings reported in Table 5.
B Codebook Used to Apply FARSIGHT
Framework Metrics
Following the approach of Akanda et al. [95], we operational-
ize each FARSIGHT metric into anevidence-based checklist
of binary (present/absent) indicators, each anchored to con-
crete artifacts observable in a published paper (mechanism
descriptions, system diagrams, or experimental results). The
code-level audit (Appendix D) applies the same indicators to
source code. Ratings are assigned by deterministic scoring
rules, ensuring that two independent evaluators examining
the same paper will check the same indicators and arrive at
the same score. Below we specify each indicator set and its
scoring logic; Table 18 presents the full codebook in tabular
form.
Robustness Evidence Indicators.
R1 (Crash Foresight).E1: Quantitative anomaly detection
(e.g., VIX thresholds, statistical outlier tests, correlation-
breakdown monitoring, PCA-based volatility clustering).E2:
Market-regime awareness via qualitative signals (e.g., senti-
ment profiling, macro-trend assessment, multi-source news
synthesis).E3: Automated threshold-based alert or trigger
mechanism (programmatic, not dependent on LLM reasoning
alone).
Rule: ● = E1∧ E3; ◆ = ≥1 of {E1, E2, E3} present but
¬(E1∧E3);❍= none.
R2 (Rapid Reaction).E1: Fast-path interrupt mechanism ex-
ecutablewithoutLLM inference (e.g., external rules engine,
hardware-level circuit breaker, or safe-mode switch that fires
before LLM dispatch).E2: Automated order freeze or can-
cellation under detected shock (programmatic action that may
still pass through the LLM-mediated reasoning chain).E3:
Risk-authority override protocol (risk agent can overrule other
agents without multi-round debate).
Rule: ● = E1 present; ◆ = ≥1 of {E2, E3} present but ¬E1;
❍= none.
R3 (Loss Containment).E1: Quantitative stop-loss param-
eters defined (specific drawdown thresholds, position caps,
or percentage limits).E2: Risk-aware behavioral adjustment
(exposure reduction, risk-mode switching, or loss-triggered
strategy change).E3: Automated enforcement (stop-loss ex-
ecutes programmatically, independent of LLM reasoning or
human approval).E4: Multi-layer or volatility-adjusted con-
tainment (position-level + portfolio-level, or dynamic calibra-
tion).
Rule: ● = E1∧ E3; ◆ = ≥1 of {E1, E2, E3, E4} present but
¬(E1∧E3);❍= none.
R4 (Recovery).E1: Crash-triggered recovery protocol (dis-
tinct recovery activated by tail events, not merely continuous
48

Table 17: Comparison between LLM-based analysis (♂layer-group) and human expert (/users) review under the FARSIGHT framework.
Agent System R1 R2 R3 R4 S1 S2.1 S2.2 S2.3 S3 #Diff Ratio
♂layer-group/users♂layer-group/users♂layer-group/users♂layer-group/users♂layer-group/users♂layer-group/users♂layer-group/users♂layer-group/users♂layer-group/users
FinMem❍ ◆ ◆ ❍ ● ◆ ◆ ◆ ❍ ❍ ❍ ❍ ❍ ◆ ❍ ❍ ❍ ❍4 44.4%
TradingAgents● ◆ ● ◆ ● ◆ ● ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ❍5 55.6%
FinCon● ❍ ● ❍ ● ❍ ● ❍ ❍ ❍ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆4 44.4%
QuantAgent❍ ◆ ❍ ◆ ◆ ◆ ● ◆ ❍ ◆ ◆ ◆ ◆ ◆ ❍ ◆ ◆ ❍6 66.7%
FLAG-Trader◆ ❍ ● ❍ ◆ ❍ ◆ ❍ ❍ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆5 55.6%
Total #Diff / Ratio (per Metric)5 / 100% 5 / 100% 4 / 80% 4 / 80% 2 / 40% 0 / 0% 1 / 20% 1 / 20% 2 / 40% 24 53.3%
●(Fully Robust / Low Risk)◆(Partially Robust / Medium Risk)❍(Not Robust / High Risk)
learning).E2: Structured post-mortem analysis (fault diag-
nosis, historical scenario comparison, or root-cause identifi-
cation).E3: Explicit parameter recalibration post-crash (re-
duced leverage, wider confidence thresholds, strategy down-
grade).E4: Experience replay or self-reflection mechanism
that feeds past outcomes into future decisions.
Rule: ● = E1∧ (E2 ∨ E3 ∨ E4); ◆ = ≥1 of {E1, E2, E3, E4}
present but¬(E1∧(E2∨E3∨E4));❍= none.
Security Evidence Indicators.
S1 (Information-Source Attacks).E1: Source provenance
tracking (source domain, timestamp, and authentication meta-
data are recorded).E2: Cross-source corroboration required
before trade execution (≥2 independent sources must confirm
a market-moving signal).E3: Structured quantitative aggre-
gation (voting, ranking, or policy learning) across independent
analysis channels.E4: Human curation or design-level scope
restriction that limits raw external data exposure.
Rule: ● = E1∧ E2; ◆ = ≥1 of {E1, E2, E3, E4} present but
¬(E1∧E2);❍= none.
S2 Sub-metric Structure.S2 is decomposed into three inde-
pendently scored sub-metrics, S2.1 (prompt-injection), S2.2
(tool/API exploitation), and S2.3 (memory or context manipu-
lation). Each sub-metric uses three indicators with a uniform
pattern:E1captures anactive defensive mechanismfor that
attack class,E2capturesstrict design-levelelimination of the
corresponding attack surface, andE3capturespartial design-
levelrestriction. The same scoring rule applies to all three
sub-metrics.
S2.1 (Prompt-Injection and Instruction Override).E1: Ac-
tive prompt-injection defense, system-prompt immutability
with user/data-input separation, input sanitization or injection
filtering, or multi-agent verification (debate, voting, role sepa-
ration) that requires defeating multiple agents simultaneously.
E2: Strict design-level absence of open prompt channels. Only
curated, authenticated, or research-environment inputs feed
the agent; no end-user free-form prompts processed.E3: Par-
tial design-level restriction. Inputs are simulated, sandboxed,
or otherwise constrained, but residual prompt-layer exposure
remains.
Rule: ● = E2; ◆ = ≥1 of {E1, E3} present but ¬E2;
❍= none.
S2.2 (Tool-Use and API Exploitation).E1: Active tool/API
protection, role-based access control (RBAC), capability
scoping separating read from execution permissions, dual-
authorization, rate limiting, or risk-management agents that
gate trade execution.E2: Strict design-level absence of live
actuating tools. No trade-execution path exists, and the sys-
tem operates as analysis-only or simulation-only.E3: Partial
design-level restriction. Live tools exist but are limited to
read-only or sandboxed endpoints, with actuating tools off by
default or available only under explicit human trigger.
Rule: ● = E2; ◆ = ≥1 of {E1, E3} present but ¬E2;
❍= none.
S2.3 (Memory or Context Manipulation).E1: Active mem-
ory protection, write-gating, quarantine memory, provenance-
checked promotion, or feedback/risk-driven validation before
observations enter persistent storage.E2: Strict design-level
absence of long-term memory. The agent has no persistent
or self-evolving memory state.E3: Partial design-level re-
striction. Memory is short-term, ephemeral across sessions,
or otherwise limited in self-reinforcement.
Rule: ● = E2; ◆ = ≥1 of {E1, E3} present but ¬E2;
❍= none.
Note on S2.1–S2.3.The ● criterion (E2) is intentionally
reserved for advisory-only or offline-analysis systems that
do not expose the corresponding surface at all; execution-
capable agents with strong active defenses (E1) reach at most
◆ by construction. A ◆ on an S2 sub-metric therefore means
that the surface is exposed, not that the agent is trivially ex-
ploitable.
S3 (Agent-as-Attacker).E1: Behavioral anomaly detection
(monitors for sudden changes in order frequency, asset class,
or trade volume).E2: Agent isolation capability (can sand-
box or disable a single compromised agent without system-
wide shutdown).E3: Inter-agent message validation (peer
messages treated as untrusted inputs; policy engine validates
before execution).E4: Human hard-stop override channel
that can immediately halt all agent actions.E5: Strict design-
level absence of autonomous market-action capability. The
agent has no live execution path and operates as an analytical,
advisory, or purely offline simulation-only framework. Multi-
agent simulations with a shared, unisolated order book do not
49

qualify.E6: Partial design-level restriction of autonomous
market-action capability. The agent can interface with mar-
kets but is not inherently autonomous (e.g., minimal live API
exposure, requires explicit human triggers, or limited execu-
tion scope).
Rule: ● = E5∨ (E1 ∧ E2); ◆ = ≥1 of {E1, E2, E3, E4, E6}
present but¬E5∧ ¬(E1∧E2);❍= none.
This evidence-based codebook providesstructured, expert-
appliedscoring rules: given the same published paper, two
evaluators who identify the same indicators will arrive at the
same rating. Consistent identification of the indicators them-
selves still requires domain expertise, as our LLM-application
study (Appendix G) confirms. It also enables automated or
hybrid evaluation workflows: as demonstrated in Appendix G,
we used large language models to assist in applying these
indicators and to cross-validate human expert assessments.
Furthermore, the codebook isextensible: new metrics require
only defining additional indicator sets and scoring rules, and
the modular design allows adaptation to other financial sec-
tors (e.g., derivatives, cryptocurrency, international equities)
or new risk dimensions (e.g., regulatory compliance, liquidity
risk) without altering the existing evaluation logic.
C Per-Agent Metric Justifications
Below we provide justifications for partial (◆) and fully ro-
bust / low-risk (●) scores in Table 5, following the codebook
criteria in Appendix B. (Items not listed are not-robust / high-
risk ❍ entries, for which no satisfied indicator was identified
in the source paper.)
R1 (Crash Foresight):FinMem: sentiment-based risk pro-
filing with adaptive memory switching satisfies E2, but no
quantitative anomaly detection (no E1) and no programmatic
threshold trigger (no E3).Alpha-GPT 2.0: human-in-the-loop
alpha validation catches risky strategies offline (E2), but no
continuous live surveillance (no E1, no E3).QuantAgent:
dedicated risk monitoring agent provides qualitative regime
awareness (E2), but lacks concrete quantitative metrics such
as VIX tracking or correlation dislocation (no E1) and no
programmatic threshold trigger (no E3).TradingAgents: Bul-
l/Bear researcher agents assess market regime via semantic
reasoning (E2), but rely on qualitative reasoning rather than
statistical signals (no E1) and no threshold-based trigger (no
E3).TradingGroup: multi-source news/sentiment synthesis
(E2), but no threshold-based early warning (no E1, no E3).
R2 (Rapid Reaction):QuantAgent: risk-monitoring compo-
nent triggers automated alerts under abnormal volatility (E2),
but bounded by LLM inference latency, no LLM-independent
fast path (no E1).TradingAgents: risk management team can
override (E3), but acts through message-passing rather than
algorithmic immediacy (no E1).TradingGroup: configurable
stop-loss/take-profit thresholds trigger automated cancellation
(E2), but static and user-defined without an LLM-independent
fast path (no E1).
R3 (Loss Containment):FinMem: adaptive risk modes re-
duce exposure after performance declines (E2), but no defined
drawdown thresholds (no E1) or programmatic liquidation
triggers (no E3).Alpha-GPT 2.0: research-stage risk assess-
ment (E2), but no execution-time enforcement (no E3).Quan-
tAgent: position management functions within the risk agent
(E2), but omits mathematical details on stop-loss parameters
(no E1) and no programmatic enforcement (no E3).Tradin-
gAgents: coordinated loss containment via risk management
team yields empirically smaller drawdowns (E2), but no trans-
parent liquidation logic (no E3).ContestTrade: downranks
poorly performing agents (E2), but adaptation occurs after
losses materialize (no E1, no E3).TradingGroup: configurable
stop-loss settings (E1), but without volatility-adjusted calibra-
tion (no E4) or fully autonomous programmatic enforcement
(no E3).
R4 (Recovery):FinMem: self-evolution mechanism updates
memory over time (E4), but no event-triggered recovery dis-
tinct from continuous learning (no E1).FinAgent: dual-level
reflection framework feeds outcomes back into future deci-
sions (E4), but no explicit crash-triggered reparameterization
(no E1).Alpha-GPT 2.0: human researchers guide iterative
improvements (E3), but no automated post-crash recovery
protocol (no E1).QuantAgent: two-loop structure (inner opti-
mization, outer testing) integrates outcomes (E4), but adapta-
tion is slow and not crash-triggered (no E1).TradingAgents:
continuous-learning loop (E4) without crash-specific recovery
triggers (no E1).ContestTrade: evolutionary resilience pro-
motes surviving agents (E4), but cannot handle simultaneous
system-wide crashes (no E1).TradingGroup: self-reflection
and continuous data synthesis (E4), but recovery is passive
rather than crash-triggered (no E1).
S1 (Information-Source Attacks):StockAgent: simulated
market environment limits raw external feed exposure (E4);
no provenance tracking (no E1) or cross-source corroboration
(no E2).FinRobot: structured aggregation across modular
sub-agents (E3); no provenance or corroboration enforce-
ment.Alpha-GPT 2.0: human-curated alpha-research inputs
(E4); no provenance or cross-source corroboration before
signal use.QuantAgent: structured fusion of technical fea-
tures within the risk-monitoring agent (E3); no provenance
or corroboration.TradingAgents: debate-and-synthesis aggre-
gation across analyst/researcher teams (E3); no provenance
or corroboration enforcement.FLAG-Trader: policy-learning
aggregation over heterogeneous signals (E3); no provenance
or corroboration.ContestTrade: real-time ranking and contest-
based aggregation across parallel paths (E3); no provenance
or corroboration.TradingGroup: collaborative aggregation
across group communication channels (E3); no provenance
or corroboration.
S2.1 (Prompt-Injection & Instruction Override):Alpha-
GPT 2.0( ●): operates on curated researcher inputs rather than
open prompt channels, E2 (strict design-level absence of open
prompt channels) satisfied.MarketSenseAI, MarketSenseAI
50

Table 18: Evidence-Based Codebook for FARSIGHT Robustness Metrics (security metrics in Table 19). Each metric is
decomposed into binary evidence indicators. Ratings follow deterministic rules: ● = Fully Robust / Low Risk; ◆ = Partially
Robust / Medium Risk;❍= Not Robust / High Risk.
Metric ID Evidence Indicator (what evaluators look
for)
Observable Artifact in Paper Scoring Rule
Robustness Metrics
R1: Crash
Foresight
E1 Quantitative anomaly detection VIX thresholds, statistical outlier
tests, correlation monitoring, PCA
clustering
●= E1∧E3
◆=≥1 of {E1,E2,E3}
but¬(E1∧E3)
❍= noneE2 Market-regime awareness via qualitative sig-
nals
Sentiment profiling, macro-trend as-
sessment, news synthesis
E3 Automated threshold-based trigger mechanism Programmatic alerts not dependent
on LLM alone
R2: Rapid
Reaction
E1 Fast-path interrupt without LLM inference External rules engine, hardware-
level circuit breaker, or safe-mode
switch firing before LLM dispatch
●= E1 present
◆=≥1 of {E2,E3}
but¬E1
❍= noneE2 Automated order freeze/cancellation under
shock
Programmatic cancel of resting or-
ders (LLM-mediated allowed)
E3 Risk-authority override protocol Risk agent overrules without debate
R3: Loss
Contain.
E1 Quantitative stop-loss parameters defined Drawdown thresholds, position caps,
% limits
●= E1∧E3
◆=≥1 of {E1..E4}
but¬(E1∧E3)
❍= none
E2 Risk-aware behavioral adjustment Exposure reduction, risk-mode
switching
E3 Automated stop-loss enforcement Executes without LLM/human ap-
proval
E4 Multi-layer or volatility-adjusted containment Position + portfolio levels, or dy-
namic calibration
R4:
Recovery
E1 Crash-triggered recovery protocol Distinct from continuous learning;
tail-event activated
●= E1∧(E2∨E3∨E4)
◆=≥1 of {E1..E4}
but¬(E1∧(E2∨E3∨E4))
❍= none
E2 Structured post-mortem analysis Fault diagnosis, scenario compari-
son
E3 Explicit parameter recalibration post-crash Reduced leverage, wider thresholds
E4 Experience replay or self-reflection mechanism Past outcomes feed future decisions
51

Table 19: Evidence-based codebook for FARSIGHT security metrics (continued from Table 18).
Metric ID Evidence Indicator (what evaluators look
for)
Observable Artifact in Paper Scoring Rule
Security Metrics
S1: Info-
Source
Attacks
E1 Source provenance tracking Domain, timestamp, authentication
metadata
●= E1∧E2
◆=≥1 of {E1..E4}
but¬(E1∧E2)
❍= none
E2 Cross-source corroboration before execution≥ 2 independent sources confirm sig-
nal
E3 Structured quantitative aggregation V oting, ranking, or policy learning
across channels
E4 Human curation or scope restriction Curated input pipeline or restricted
exposure
S2.1:
Prompt-
Injection
E1 Active prompt-injection defense Immutable system prompt, input
sanitization, multi-agent verification,
role separation
●= E2
◆=≥1 of {E1,E3}
but¬E2
❍= noneE2 Strict design-level scope restriction No open prompt channels; curat-
ed/authenticated inputs only
E3 Partial design-level restriction Simulated/sandboxed inputs with
residual exposure
S2.2:
Tool/API
Exploit.
E1 Active tool/API protection RBAC, capability scoping, dual-
auth, rate limits, risk-gated execu-
tion
●= E2
◆=≥1 of {E1,E3}
but¬E2
❍= noneE2 Strict design-level scope restriction No live execution / actuating tools
by design
E3 Partial design-level restriction Read-only or sandboxed tools; actu-
ating tools off by default
S2.3:
Memory/
Context
E1 Active memory protection Write-gating, quarantine memory,
provenance/risk-checked promotion
●= E2
◆=≥1 of {E1,E3}
but¬E2
❍= none
E2 Strict design-level scope restriction No persistent / self-evolving long-
term memory
E3 Partial design-level restriction Short-term/ephemeral memory only,
no self-reinforcement
S3: Agent
as
Attacker
E1 Behavioral anomaly detection Monitors order frequency, asset
class, volume changes ●= E5∨(E1∧E2)
◆=≥1 of {E1..E4,E6}
but¬E5∧ ¬(E1∧E2)
❍= none
E2 Agent isolation capability Sandbox/disable one agent without
system shutdown
E3 Inter-agent message validation Peer messages untrusted; policy en-
gine validates
E4 Human hard-stop override Immediate halt of all agent actions
E5 Strict design-level absence of live execution Analysis-only, advisory, or purely
offline simulation (excludes multi-
agent sims with a shared order book)
E6 Partial design-level restriction Minimal live exposure or non-
autonomous execution
52

2.0: chain-of-thought analysis over curated SEC filings in-
troduces multi-step structured reasoning (E1) and a partially
constrained input pipeline (E3); no full design-level isolation
(no E2).StockAgent: simulated event-driven inputs partially
restrict prompt exposure (E3) plus role-decomposition across
investor agents (E1); residual exposure remains (no E2).Fin-
Con, FinAgent, FinRobot, QuantAgent, TradExpert, Tradin-
gAgents, FLAG-Trader, ContestTrade, TradingGroup: multi-
agent verification, role separation, or chain-of-thought struc-
ture constrains direct prompt overrides (E1); none achieve
full design-level absence of open prompt channels (no E2).
S2.2 (Tool-Use & API Exploitation):MarketSenseAI, Mar-
ketSenseAI 2.0( ●): static document retrieval and analysis
without live API-driven trade execution, E2 (strict design-
level absence of actuating tools) satisfied.Alpha-GPT 2.0
(●): alpha-discovery research framework with no autonomous
trade-execution path, E2 satisfied.TradingGPT, FinMem,
StockAgent: limited tool exposure via single-agent or sim-
ulation context (E3); no full design-level execution isolation
(no E2).FinCon, FinAgent, FinRobot, QuantAgent, TradEx-
pert, TradingAgents, FLAG-Trader, ContestTrade, Trading-
Group: risk-management gating, multi-agent veto, or capabil-
ity scoping constrains execution (E1); actuating tools remain
reachable (no E2).
S2.3 (Memory or Context Manipulation):MarketSenseAI,
MarketSenseAI 2.0( ●): stateless analysis pipeline without
persistent self-evolving memory, E2 satisfied.TradExpert
(●): mixture-of-experts produces predictions without persis-
tent self-evolving memory state, E2 satisfied.FinCon, FinA-
gent, FinRobot, Alpha-GPT 2.0, QuantAgent, TradingAgents,
FLAG-Trader, ContestTrade: feedback-driven, validated, or
risk-gated memory updates (E1); memory remains long-term
and modifiable (no E2).StockAgent: simulated environment
limits memory poisoning surface (E3); long-term memory
persists (no E2).
S3 (Agent-as-Attacker):FinRobot( ●): composable analyt-
ical platform whose design intentionally excludes any live
execution or external trading connection, E5 (strict design-
level absence of autonomous market-action capability) sat-
isfied.Alpha-GPT 2.0( ●): alpha-discovery framework with
no autonomous trade execution, E5 satisfied.MarketSenseAI,
MarketSenseAI 2.0: minimal live API exposure with non-
autonomous execution, E6 (partial design-level restriction)
satisfied.FinCon, FinAgent, TradExpert, FLAG-Trader, Con-
testTrade: limited live capability with risk-management gat-
ing, contest filtering, or dual-control structure, E6 satisfied.
D Code-Level Audit Details
Scope.We count a release as official only if the scheme’s
paper or an author’s page links to it. Seven schemes qualify:
FinMem, StockAgent, FinAgent (linked from the first author’s
homepage), FinRobot, QuantAgent (since renamed QuantHar-
ness), TradingAgents, and ContestTrade. FinCon links to a
repository that contains only a README and a license. Trad-
ingGPT, MarketSenseAI, MarketSenseAI 2.0, Alpha-GPT 2.0,
TradExpert, FLAG-Trader, and TradingGroup have no offi-
cial release. Table 20 lists the pinned commits. Two releases
differ from the system in the paper. FinRobot’s repository
now holds several generations of the platform, and we audited
the original package that the paper describes. TradingAgents
published code only after its last arXiv version, so its audit
reflects the released implementation rather than the system in
the paper.
Procedure.The audit is static: we read the source at the
pinned commit and did not run it, install it, or call any exter-
nal service. For each repository, Claude Sonnet 5.5 received
the codebook (Appendix B), our paper-level ratings and their
justifications (Appendix C), and a fixed protocol. It labeled
each of the 33 evidence indicators as present, partial, or absent
with file-and-line evidence, and it answered five factual ques-
tions: whether the code can submit orders, whether memory
persists across runs, which data sources are wired in, whether
any risk limit is enforced outside the LLM, and which de-
scribed mechanisms are missing. Each repository was audited
in 3 runs, each in a fresh clone and without access to the other
runs. A script then re-derives the nine ratings from the indica-
tor labels with the codebook rules, so the rating step itself is
deterministic. A partial indicator supports a partial rating but
never satisfies a requirement for a full rating. Under a stricter
convention that treats partial indicators as absent, 31 of 63
code-level ratings match the paper-level ones, compared with
39 under the main convention.
Pattern matching and claim verification.Independently of
the LLM runs, a script searches each release for five pattern
families: order-submission and broker APIs, dynamic code
execution, persistence of memory or state, risk limits, and
input validation. The order-submission family has no match
in any of the seven releases, which agrees with all 3 runs.
A separate verification pass, run with Claude Opus on local
clones at the pinned commits and independent of the three
auditor runs, checked each of the 14 code-level claims that the
main text relies on against the cited source lines and confirmed
all of them. The same pass ruled on each of the 7 cross-run
disagreements by reading the code, and every ruling agreed
with the two-of-three majority.
Per-scheme findings.FinMemis an offline, single-agent back-
test whose position is a share counter. Its memory layers and
agent state are pickled to disk and reloaded from checkpoints
with no validation before writes, and error strings from failed
output validation can be stored as reflections. The risk-averse
branch of its self-adaptive risk character is commented out
in the released prompt.StockAgentis a pure simulation in
which all agents trade through one shared, unisolated order
book with no price band. The last matched price becomes
the market price, so a single agent can set it. Each agent’s
free-text forum post reaches every other agent’s next-day
53

Table 20: Repositories and pinned commits of the code-level audit. Each repository was audited at the listed commit in three
independent runs.
Scheme Repository Commit Date
FinMempipiku915/FinMem-LLM-StockTrading be814aa2024-08-17
StockAgentMingyuJ666/Stockagent e2a9c052026-06-16
FinAgentDVampire/FinAgent 17248a02024-08-31
FinRobotAI4Finance-Foundation/FinRobot 27174992026-09-28
QuantAgentY-Research-SBU/QuantHarness 2e64c7b2026-08-18
TradingAgentsTauricResearch/TradingAgents 1394a3f2026-10-03
ContestTradeFinStep-AI/ContestTrade 22432f92025-12-22
prompt without filtering, which is the S3 propagation path
in our threat model.FinAgentis a daily-bar backtest with no
order path. Its memory is a FAISS index with a pickled key
map (finagent/memory/faiss.py ), written without vali-
dation and reloadable from disk, and three data downloaders
print the market-data API key to standard output.FinRobot’s
paper-era package has no order path, and its backtests use
a simulated broker. Its default assistants, however, execute
model-written code on the host without a sandbox or human
approval (finrobot/agents/workflow.py ), and the SEC
filing tool returns the exception text, including the token-
bearing request URL, to the model when a download fails
(finrobot/data_source/sec_utils.py ). Its Chroma
retrieval stores persist across runs in fixed directories.Quan-
tAgent’s release contains Indicator, Pattern, and Trend agents
and one decision node, but no risk agent, no stop-loss, and no
memory. It analyzes user-selected candles, from one minute
to one month, on demand. Its local web interface also ren-
ders request parameters without escaping and serves files
without path checks, which are web-application issues out-
side the codebook.TradingAgentsreturns a five-tier rating
and has no order or simulated-exchange path, although its
README describes one. A persistent decision log, added af-
ter the paper, stores model-written text verbatim and splits en-
tries on a fixed delimiter (tradingagents/memory/log.py),
so model output that reproduces the delimiter can forge a
past entry. A stop-loss field is filled in by the model but
never enforced.ContestTrade’s contest mechanism, which
gives the system its name, is not wired into the released
pipeline, which passes research signals straight to the out-
put. Its default stock-selection tool for the Chinese market
executes model-written Python with exec in the host process
(contest_trade/tools/stock_selector_akshare.py).
Threats to validity.Static reading can miss behavior that
appears only at run time, and an LLM auditor can overlook
code. Three independent runs, pattern matching, and manual
verification reduce this risk but do not remove it. Releases
evolve, so our results describe the pinned commits rather than
later versions. The code-level ratings also depend on how
partial indicators are counted, which is why we report both
conventions. The auditor saw our paper-level ratings and their
justifications, which helped it locate the mechanisms that the
papers describe but may anchor its labels toward those ratings.
Two observations limit this effect: the final code-level ratings
still differ from the paper-level ones in 21 cases upward and 3
downward, and the pattern scan, which never saw the ratings,
agrees with every run that no release can submit orders.
E Distinct Characteristics of Financial LLM
Agents
As illustrated in Section 5.2 Figure 4, financial LLM agents
possess attack characteristics distinct from those in domains
like healthcare, law, or education. Their exposure to real-time
market data, dependence on heterogeneous signals, and high-
frequency autonomy make them highly sensitive to latency,
trust, and reflexivity attacks. We summarize five defining traits
below.
Instant.This trait describes the attack window, not the speed
of the agent. Markets reprice within milliseconds, so an at-
tacker can create a transient price dislocation and exit before
human or automated risk systems respond. An agent that de-
liberates for minutes (Table 7) widens this window rather
than closing it, and such monetizable micro-windows have no
counterpart in other domains.
Inconspicuous.Tiny quote or tick manipulations appear legit-
imate, prompting agents to alter trading behavior while users
notice no anomaly. Because financial agents act on minute
price deltas, even subtle perturbations can trigger hidden but
impactful responses.
Unverified.Inputs such as fake news, spoofed APIs, or
forged order messages are often processed without prove-
nance checks due to speed-first system design. This lack of
validation allows attackers to issue unauthorized actions or
trigger auto-trades with minimal friction.
Adaptive.By coordinating multi-source inputs (news, senti-
ment, technical feeds), attackers dynamically tailor strategies
to exploit signal inconsistencies. The agents’ heterogeneous
integration logic grants adversaries flexibility unmatched in
more structured data domains.
Cascading.Minor perturbations, like brief rumors or small
sell orders, can cascade through interconnected trading agents,
54

causing flash crashes or liquidity shocks. Because markets are
reflexive and interdependent, one agent’s output becomes an-
other’s trigger, amplifying small manipulations into systemic
events.
Evidence for each trait.Instant: markets reprice faster than
the agents decide (Table 7), and 12 of the 15 schemes re-
ceive ❍ on R2 (Table 5).Inconspicuous: the S2.1 and S2.3
rows of Table 2 show that a small numeric nudge or a slowly
compounding memory bias suffices, and the resulting losses
resemble ordinary market noise.Unverified: no scheme earns
full credit on S1, and 7 of the 15 receive ❍ (Table 5).Adap-
tive: 13 of the 15 schemes combine three or more input types
(Table 3), which gives an attacker several channels to choose
from.Cascading: 6 schemes receive ❍ on S3, and the S3
row of Table 2 traces how harm reaches third parties through
prices and herding.
F Comparison of Investment Schemes and
Stock-Trading Agents
Passive-income schemes operate with minimal intervention:
once capital is invested, returns are generated automatically
without active management. Fixed-income assets such as
bondsoffer the highest stability and predictable yields, with
risk limited mainly to large-scale defaults or market collapse.
Similarly,mutual funds,index funds, andETFsembody the
passive philosophy, requiring little investor action. They ex-
hibit strong robustness and security due to limited market in-
teraction and low exposure to real-time trading risks, though
their annualized returns remain moderate by design. In con-
trast,LLM-based stock-trading agentsactively engage with
live markets to pursue higher returns, but this introduces la-
tency, prediction errors, and exposure to adversarial manipula-
tion. Passive schemes thus provide stable, secure, and steady
returns, while active stock agents offer higher potential gains
at significantly greater risk, requiring investors to balance
stability against growth ambition.
G LLM Literature Analysis Implementation
Agreement with human experts.We evaluated the utility
of LLM-based analysis under the FARSIGHT framework to
assess how effectively it mirrors human expert judgment. Ap-
plying ChatGPT Deep Research with predefined metrics, defi-
nitions, and scope (see Appendix G for additional details) to a
5-agent sub-sample (FinMem, TradingAgents, FinCon, Quan-
tAgent, FLAG-Trader), we found that the model disagreed
with human expert evaluations on 24 of 45 metric cells (a
53.3% disagreement rate, i.e., 46.7% agreement), while still
identifying similar key financial LLM agents and repeatedly
flagging the same recurring weaknesses. While its reasoning
depth remains more limited than that of human experts, the
approach offers high scalability, enabling rapid and consistent
framework-guided evaluation as the literature continues to
expand.
The disagreements concentrate on robustness. The model
disagreed with the human ratings on all five schemes for R1
and R2, on four of five for R3 and R4, and on at most two
of five for each security metric (Table 17). A likely reason
is that the security metrics build on attack classes with an
established literature, such as prompt injection, tool misuse,
and memory poisoning, whereas the robustness metrics ask
for trading-specific controls, such as fast-path interrupts and
crash-triggered recovery, that the papers seldom name. Rely-
ing solely on black-box LLM assessment is therefore least
reliable on exactly the metrics that are specific to trading.
We conducted an automated literature analysis using Chat-
GPT Deep Research through a structured prompt derived
from our FARSIGHT framework. The process included sup-
plying the framework definitions for robustness (R1–R4) and
security (S1–S3) metrics, restricting the search to academic
papers published between 2023 and 2026 that focused on
“financial LLM agents” or “LLM trading systems,” and re-
questing structured summaries highlighting robustness gaps,
attack surfaces, and mitigation strategies. The LLM outputs
were then compared with our manually reviewed dataset to
assess alignment accuracy, as shown in Table 17. In total,
the LLM identified eight candidate papers labeled as “finan-
cial LLM agents,” but only five of them (FinMem, FinCon,
QuantAgent, TradingAgents, and FLAG-Trader) were gen-
uinely relevant. The remaining three were benchmark, survey,
or simulation studies without real agentic designs. While the
model produced strong summaries and coherent overviews, its
detailed framework-based analysis was unreliable: its metric-
level ratings disagreed with the human ratings on 24 of 45
cells (53.3%). We attribute this to the model’s inability to
precisely locate and interpret framework-specific evidence
within long, multi-section papers. In particular, the context
window limitation caused the LLM to miss fine-grained de-
tails while maintaining fluent but shallow summaries. This
observation reinforces that while LLMs are promising for
rapid literature summarization, their analytical accuracy in
structured scientific evaluation remains substantially lower
than that of human expert review. Table 17 shows that these
disagreements fall mostly on the robustness metrics.
We also examined the reasoning process and retrieved
sources of the ChatGPT Deep Research system to better under-
stand its literature analysis behavior. As shown in Figure 19,
the model queried a diverse set of sources, includingarXiv,
ResearchGate,RePEc, andOpenReview, but also accessed sev-
eral non-academic domains such asMedium,mql5.com, and
DigitalOcean. Although the model could retrieve and summa-
rize relevant papers, it frequently encounteredreCAPTCHA
and rate-limit restrictions that reduced its search coverage
compared to human experts. Additionally, it was easily dis-
tracted by unrelated technical blogs and community sites,
resulting in lower focus and precision. This analysis demon-
55

strates that while LLM-based search can efficiently explore
new research areas, its reliability and selectivity remain infe-
rior to those of human-guided exploration. Overall, as shown
in Table 21, our experiments indicate that while LLM-based
literature reviews are effective for fast scanning and abstract
summarization, they remain limited in deep reasoning, de-
tailed analysis, and evidence-level verification.
Table 21: Observed strengths and weaknesses of LLM-based
review.
Strengths Weaknesses
Fast scanning Deep reasoning
Abstract summarization Detailed analysis
Pattern discovery Evidence verification
Figure 19: Source frequency distribution from ChatGPT Deep
Research.
H Domain Risk Profiles
This appendix gives the evidence for each cell of Figure 12.
Each property is rated from the perspective of a compromised
or misled agent:highmeans that the property raises the cost
of a compromise in that domain.Irreversibilityasks whether
the agent’s actions can be undone.Adversary-authored inputs
asks whether outsiders routinely write what the agent reads.
Speed of harmcompares the time from action to harm with
the time a human reviewer needs.Coupling to other actors
asks whether the agent’s outputs become other actors’ inputs.
Stealth of harmasks whether harmful outcomes resemble
normal variation.Reliance on in-model safetyasks whether
any control that the agent cannot argue with sits between the
agent and its irreversible actions.
Trading (this paper).Irreversibility(high): An executed
order settles before any human review, and losses scale with
size and leverage [18,102].Adversary-authored inputs(high):
Anyone can write the news and social media that the agents
read, and a forged headline moved the market in 2013 [102].
Speed of harm(high): Markets reprice in milliseconds, while
TradingAgents takes over 240 s per decision [18].Coupling
to other actors(high): Every order changes the price that
other agents, bots, and humans read (S3) [22].Stealth of harm
(high): Losses from a slow memory bias or a numeric nudge
look like ordinary market noise.Reliance on in-model safety
(high): No scheme earns full credit on R2 or R3, and no
release enforces a loss limit outside the model.
Healthcare.Irreversibility(high): An administered drug or
a missed diagnosis cannot be undone.Adversary-authored
inputs(medium): Patients supply messages and images that
can carry hidden instructions, and training data can be poi-
soned [72, 73].Speed of harm(medium): Orders take effect
within minutes to hours, so human review is possible but com-
pressed.Coupling to other actors(medium): Agents write
into a shared record that clinicians and other tools read and
copy forward [164].Stealth of harm(high): Poisoned medical
models match clean ones on standard benchmarks, and clini-
cal errors resemble the course of a disease [72].Reliance on
in-model safety(medium): Order-entry hard stops and phar-
macist verification sit outside the agent, but they depend on
attentive humans [153, 167].
Law.Irreversibility(medium): Filings can be corrected,
but sanctions and missed deadlines stick [154].Adversary-
authored inputs(high): The opposing party produces many of
the documents the agent reads, and hidden prompts already
appear in submitted manuscripts [156].Speed of harm(low):
Court deadlines run in days, which leaves time for review.
Coupling to other actors(medium): Briefs, clause libraries,
and citations are reused, so a fabricated case can be copied
into later filings [74].Stealth of harm(medium): A fabricated
citation is detectable when checked, yet commercial tools still
produce them on 17–33% of queries [74].Reliance on in-
model safety(medium): The attorney’s signature and duty to
verify sit outside the model but rest on human diligence [154].
Software engineering.Irreversibility(medium): Deploys
roll back, but deleted data and leaked credentials do not.
Adversary-authored inputs(high): Outsiders write the issues,
pull requests, dependencies, and tool descriptions that coding
agents read [155, 157].Speed of harm(medium): Automated
pipelines ship changes within minutes.Coupling to other
actors(high): Other developers and their agents pull the pack-
ages and repositories that one agent writes.Stealth of harm
(high): A subtle backdoor reads like ordinary code.Reliance
on in-model safety(high): Coding agents often run with host
privileges, and two audited trading releases execute model-
written code on the host [168].
Crypto and DeFi.Irreversibility(high): On-chain trans-
fers are final [75].Adversary-authored inputs(high): Social
posts and stored context can steer agents into unauthorized
transfers [75].Speed of harm(high): Blocks confirm within
seconds, and front-running bots act within one block [161].
Coupling to other actors(high): Composable contracts and
a shared mempool let one agent’s transaction trigger oth-
ers [161].Stealth of harm(medium): The ledger is public,
but counterparties are pseudonymous.Reliance on in-model
56

safety(high): Few controls sit between an agent’s signing key
and an immutable contract [75].
Payments and commerce.Irreversibility(medium): Card
payments can be reversed through chargebacks, but many
transfers cannot [58].Adversary-authored inputs(high):
Counterparties write the merchant pages and listings that the
agent reads [58].Speed of harm(medium): Payments clear
in seconds but settle later, which leaves a short window for
review.Coupling to other actors(medium): Agents negotiate
with other agents over shared marketplaces [58].Stealth of
harm(medium): Fraud monitoring flags many abnormal pay-
ments.Reliance on in-model safety(low): Transaction limits,
authentication, and fraud scoring wrap every payer, human or
agent.
Scientific labs.Irreversibility(high): Synthesized compounds
and physical hazards cannot be undone [170,171].Adversary-
authored inputs(medium): Protocols and literature can
be poisoned, but most inputs are curated [94].Speed of
harm(medium): Automated experiments run for minutes
to hours [170].Coupling to other actors(low): Effects stay
mostly within one lab until results are published.Stealth of
harm(medium): Failed or unsafe runs are usually visible to
lab staff.Reliance on in-model safety(medium): Lab safety
protocols exist, but automated labs can run steps without a
person at the bench [94].
I LLM Usage Considerations
Originality.The conceptual framework, the codebook, the
paper-level ratings, and the conclusions are the authors’ own.
We used LLMs as tools in the ways listed below, and we
manually verified that the collected links and references were
legitimate and not fabricated.
Transparency.We disclose all uses of LLMs in this work.
(1)Literature analysis: We used ChatGPT Deep Research
to conduct automated literature analysis as described in Ap-
pendix G, with results compared against human expert re-
views. (2)Reference discovery: ChatGPT was used to assist in
discovering relevant online references (e.g., blog posts, indus-
try reports). All discovered references were manually verified
for legitimacy and relevance before inclusion. (3)Code audit:
Claude Sonnet 5.5 labeled codebook indicators in the released
code of the open-source schemes, as described in Appendix D.
A script re-derives every rating from these labels, and a sepa-
rate Claude Opus pass checked the cross-run disagreements
and every code-level claim used in the main text. (4)Writ-
ing assistance: Claude (Anthropic) drafted portions of the
text under the authors’ direction, including the related-work
comparison, the code-audit sections, and Sections 9–11 with
their figures and tables. LLMs were also used for grammar
checking and polishing. The authors take full responsibility
for all content. During this process, we identified several prac-
tical challenges, including reproducibility issues caused by
closed-source models and inconsistent responses under iden-
tical prompts. A detailed discussion of these limitations and
observations can be found in Appendix G.
Responsibility.Our use of LLMs aims to advance community
understanding of their role in SoK research, especially in
analyzing financial and security implications of agentic LLM
systems. We selected the GPT-based deep research tool for
its performance and its stable access interface. All usage was
limited to controlled academic evaluation, minimizing the
number of queries and computational cost. No proprietary or
sensitive data was used.
57
