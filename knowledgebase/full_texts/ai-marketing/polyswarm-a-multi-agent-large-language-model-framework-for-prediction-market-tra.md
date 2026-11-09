---
title: 'PolySwarm: A Multi-Agent Large Language Model Framework for Prediction Market Trading and Latency
  Arbitrage'
url: https://arxiv.org/abs/2604.03888
category: ai-marketing
subcategory: empirical
date: 2026-04
venue: ''
authors:
- Rajat M. Barot
- Arjun S. Borkhatariya
source: arxiv
pdf_url: https://arxiv.org/pdf/2604.03888
pages: 14
chars: 86787
fetched_at: '2026-11-08T13:01:31+00:00'
kb_version: 1
---

# PolySwarm: A Multi-Agent Large Language Model Framework for Prediction Market Trading and Latency Arbitrage

IEEE ACCESS 1
PolySwarm: A Multi-Agent Large Language Model
Framework for Prediction Market Trading and
Latency Arbitrage
Rajat M. Barot and Arjun S. Borkhatariya
Abstract—This paper presents PolySwarm, a novel multi-
agent large language model (LLM) framework designed for
real-time prediction market trading and latency arbitrage on
decentralized platforms such as Polymarket. PolySwarm deploys
a swarm of 50 diverse LLM personas that concurrently evalu-
ate binary outcome markets, aggregating individual probability
estimates through confidence-weighted Bayesian combination of
swarm consensus with market-implied probabilities, and applying
quarter-Kelly position sizing for risk-controlled execution. The
system incorporates an information-theoretic market analysis
engine using Kullback-Leibler (KL) divergence and Jensen-
Shannon (JS) divergence to detect cross-market inefficiencies and
negation pair mispricings. A latency arbitrage module exploits
stale Polymarket prices by deriving CEX-implied probabilities
from a log-normal pricing model and executing trades within
the human reaction-time window. We provide a full architectural
description, implementation details, and evaluation methodology
using Brier scores, calibration analysis, and log-loss metrics
benchmarked against human superforecaster performance. We
further discuss open challenges including hallucination in agent
pools, computational cost at scale, regulatory exposure, and
feedback-loop risk, and outline five priority directions for fu-
ture research. Experimental results demonstrate that swarm
aggregation consistently outperforms single-model baselines in
probability calibration on Polymarket prediction tasks.
Index Terms—large language models, multi-agent systems,
prediction markets, swarm intelligence, Bayesian aggregation,
latency arbitrage, Kelly criterion, KL divergence, system design,
real-time trading
I. INTRODUCTION
Prediction markets are financial mechanisms specifically
designed to aggregate dispersed private information into pub-
licly observable price signals, making them among the most
powerful instruments for collective forecasting known to eco-
nomics [1], [2]. By allowing participants to trade contracts
whose payoffs are contingent on real-world outcomes, these
markets incentivize honest revelation of beliefs, converting
heterogeneous private judgements into a single consensus
probability estimate [3]. Modern blockchain-based platforms
such as Polymarket and Kalshi have democratized partici-
pation in prediction markets at scale: Polymarket alone has
facilitated hundreds of millions of dollars in contract volume
across political, economic, and scientific outcome categories,
Rajat M. Barot is with the Department of Computer Science, State
University of New York, Binghamton, Binghamton, NY , USA. E-mail:
rbarot2@binghamton.edu
Arjun S. Borkhatariya is with the Department of Software Engineering,
Arizona State University, Tempe, AZ, USA. E-mail: aborkhat@asu.edu
Manuscript submitted 2026.(Corresponding author: Rajat M. Barot.)
operating on the Polygon proof-of-stake network with on-chain
settlement in USDC. Kalshi operates under direct Commodity
Futures Trading Commission (CFTC) oversight in the United
States, further legitimizing the asset class for institutional
participants. The growing liquidity of these platforms creates
a natural testbed for automated forecasting systems that can
continuously monitor, evaluate, and trade across thousands of
simultaneously open markets.
Large language models represent a qualitative leap in the
ability of computational systems to reason over unstructured
textual information. Models such as GPT-3 [4], GPT-4 [5],
and Claude 3 have demonstrated emergent capabilities in
zero-shot and few-shot reasoning, structured argument gen-
eration, and domain-specific knowledge recall that make them
promising candidates for financial forecasting tasks. Their
ability to ingest and synthesize diverse textual streams—news
headlines, earnings transcripts, policy announcements, social
media discourse—mirrors the integrative judgement of an
expert analyst. However, single-model deployments face well-
documented failure modes: hallucination of plausible but fac-
tually incorrect information [6], systematic overconfidence or
miscalibration of probability estimates [7], and high sensitivity
to superficial variations in prompt phrasing [8]. These limita-
tions are especially consequential in financial contexts, where
a confidently stated but erroneous probability estimate can
translate directly into trading losses. The stochastic, context-
window-bounded nature of transformer inference means that a
single LLM call is at best a point sample from a high-variance
distribution over possible analyses.
Multi-agent orchestration offers a principled response to
these limitations. By deploying aswarmof diverse LLM
agents—each instantiated with distinct personas, information
access patterns, and analytical priors—and aggregating their
outputs through statistically rigorous ensemble methods, it
becomes possible to suppress idiosyncratic errors, estimate
epistemic uncertainty, and exploit the complementary strengths
of different model architectures and prompting strategies [3],
[10], [25]. Swarm intelligence research has long established
that collective judgements formed by averaging independent
but diverse estimates systematically outperform individual
predictions, a property sometimes termed the “wisdom of
crowds” effect [3]. Translating this insight to LLM swarms
requires careful attention to agent design, coordination pro-
tocols, aggregation mathematics, and feedback suppression to
prevent correlated errors from cascading through the system.
Recent multi-agent frameworks such as AutoGen [13] and
arXiv:2604.03888v1  [cs.AI]  4 Apr 2026

IEEE ACCESS 2
CAMEL [14] have begun to operationalize these ideas, but
their application to real-time financial market forecasting and
trading remains largely unexplored in the research literature.
This paper makes the following contributions:
•PolySwarm system design and implementation: a
production-ready multi-agent LLM trading terminal de-
ploying 50 diverse personas on Polymarket with full ar-
chitectural description, asynchronous execution pipeline,
and paper/live trading modes.
•Confidence-weighted Bayesian aggregation: a math-
ematically principled ensemble method combining
swarm consensus with market-implied probabilities, with
quarter-Kelly position sizing for risk-controlled trade
execution.
•Information-theoretic market analysis engine: novel
application of KL divergence and JS divergence for cross-
market inefficiency detection, negation pair mispricing
identification, and latency arbitrage signal generation in
prediction markets.
•Latency arbitrage module: a CEX-to-DEX arbitrage
pipeline using a log-normal pricing model to exploit
stale Polymarket prices within the human reaction-time
window on the Polygon blockchain.
•Empirical evaluation and open challenges: systematic
evaluation using Brier scores, calibration analysis, and
log-loss metrics, together with a structured five-point
research agenda for the field.
Figure 3 situates PolySwarm within the broader landscape
of LLM-based financial forecasting approaches. The remainder
of the paper is organized as follows. Section II provides
background on prediction markets, large language models, and
multi-agent systems. Section III reviews related work on LLMs
for financial forecasting. Section IV presents the PolySwarm
system architecture and multi-agent design. Section V devel-
ops the information-theoretic framework for market analy-
sis and arbitrage detection. Section VI describes evaluation
methodology and benchmarks. Section VII discusses open
challenges, and Section VIII outlines future research direc-
tions. Section IX concludes.
II. BACKGROUND
A. Prediction Markets
Prediction markets have a documented history extending
back to the Iowa Electronic Markets (IEM), launched in
1988 by the University of Iowa Tippie College of Business
as a research platform for studying collective forecasting in
political and economic domains. The IEM demonstrated that
market-aggregated probabilities could rival or surpass tradi-
tional polling methodologies in forecasting election outcomes,
providing early empirical validation for the information-
aggregation thesis underlying prediction market design [1].
The design principles governing information aggregation in
combinatorial prediction markets were subsequently formal-
ized by Hanson [16], whose logarithmic market scoring
rule (LMSR) provides a mechanism for subsidized market
making that guarantees bounded loss to the market operator
while incentivizing honest probability revelation by traders.
Subsequent platforms including InTrade, Hollywood Stock
Exchange, and PredictIt expanded the model to a broader range
of outcome categories, while academic research confirmed
the general superiority of market-based forecasts over expert
panels and surveys across many domains [2].
Contemporary blockchain-based prediction markets rep-
resent the technological frontier of the field. Polymarket,
launched in 2020 and operating on the Polygon proof-of-stake
network [52], [53], enables permissionless participation in bi-
nary and categorical outcome markets with on-chain settlement
in USDC stablecoin. By 2024, Polymarket had accumulated
over $500 million in trading volume, including extensive
activity around the United States presidential election, Fed-
eral Reserve interest rate decisions, and cryptocurrency price
milestones. Kalshi, by contrast, operates as a CFTC-regulated
designated contract market in the United States, providing
regulatory clarity at the cost of jurisdictional restrictions on
participation. PredictIt, operated under a no-action letter from
the CFTC for academic research purposes, has served as an
important dataset source for academic studies of prediction
market efficiency.
The theoretical foundations of prediction markets rest on
the efficient markets hypothesis (EMH) of Fama [18] and
its tension with the Grossman–Stiglitz paradox [17]. Fama’s
weak-form EMH holds that asset prices fully reflect all pub-
licly available information, implying that systematic outperfor-
mance through analysis of public data is impossible in equilib-
rium. Grossman and Stiglitz identified a fundamental contra-
diction: if prices are fully informative, rational agents have no
incentive to incur the cost of information acquisition, yet if no
agent acquires information, prices cannot be informative. This
paradox motivates the existence of informed traders who earn
rents proportional to their information advantage, sustaining
the market mechanism that produces price efficiency. Multi-
agent LLM systems occupy an interesting position in this
framework: they incur computational information-processing
costs in exchange for probability estimates that may differ
from market consensus, and they trade on those differences
when the expected value of the discrepancy exceeds a thresh-
old.
B. Large Language Models
The transformer architecture introduced by Vaswani et
al. [43] in 2017 constitutes the foundational technical substrate
for modern large language models. The transformer’s multi-
head self-attention mechanism enables the model to compute
context-sensitive token representations across arbitrarily long
input sequences, overcoming the sequential bottleneck of
recurrent neural networks and enabling the scale of pretraining
that characterizes contemporary LLMs. GPT-2 [31], released
by OpenAI in 2019, first demonstrated that a language model
trained purely on next-token prediction at scale could generate
coherent long-form text and perform rudimentary zero-shot
task transfer, establishing the scaling hypothesis that motivated
subsequent generations of large models. GPT-3 [4], released
in 2020 with 175 billion parameters, demonstrated remark-
able few-shot generalization across a broad range of natural

IEEE ACCESS 3
language tasks without task-specific fine-tuning, marking a
qualitative inflection point in the capabilities of language
models. GPT-4 [5], with an estimated parameter count in the
range of one trillion, extended these capabilities to multimodal
inputs, substantially longer context windows (up to 128K
tokens), and demonstrably improved reasoning and instruction-
following.
Reinforcement learning from human feedback (RLHF), in-
troduced for language model alignment via InstructGPT by
Ouyang et al. [20], provides the fine-tuning methodology
through which instruction-following and safety properties are
instilled in deployed chat models. Open-source developments
have substantially democratized access to high-capability lan-
guage models: the LLaMA family from Meta AI [21] provides
competitive performance across parameter scales from 7B
to 70B, enabling self-hosted deployment without dependence
on proprietary API providers. LLaMA 3, released in 2024,
extends context length to 8K tokens and delivers substantially
improved performance on reasoning benchmarks.
Domain-specific financial LLMs have emerged as a focused
research direction. BloombergGPT [22], a 50-billion parameter
model pretrained on a curated corpus of 363 billion tokens
of financial text assembled by Bloomberg, demonstrates that
domain-specific pretraining yields substantial improvements
on financial NLP benchmarks including sentiment analysis,
named entity recognition in financial documents, and question
answering over earnings transcripts. FinGPT [23] pursues
an open-source, continuously updated alternative by applying
parameter-efficient fine-tuning techniques (LoRA, QLoRA) to
foundation models using streaming financial data, offering a
more accessible path to financial domain adaptation. Chain-
of-thought prompting [24] has proven particularly valuable in
financial contexts, enabling models to produce explicit inter-
mediate reasoning steps that can be audited, improve accuracy
on multi-step quantitative reasoning, and reduce overconfident
conclusions. Self-consistency decoding [46] further improves
reliability by sampling multiple reasoning chains and selecting
the most consistent answer.
Table I provides a comparison of prominent LLMs relevant
to financial applications along dimensions of organizational
provenance, scale, openness, financial domain fine-tuning,
context capacity, and reported performance on financial bench-
marks.
C. Multi-Agent Systems
Multi-agent systems (MAS) are computational architectures
comprising multiple autonomous agents that perceive their
environment, pursue individual or shared goals, and interact
through communication or shared state. In the classical AI
and distributed computing literatures, MAS have been applied
to a wide range of problems including resource allocation,
logistics optimization, auction mechanisms, and robot coor-
dination [25]. The MAS paradigm is particularly well suited
to problems characterized by high-dimensional state spaces,
distributed information, and requirements for robust collective
behaviour in the face of individual agent failures.
Swarm intelligence, as systematized by Bonabeau, Dorigo,
and Theraulaz [10], studies the collective intelligent behaviour
that emerges from the interaction of large numbers of relatively
simple agents without centralized control. Classical swarm
algorithms including Ant Colony Optimization and Particle
Swarm Optimization [11] demonstrate that near-optimal so-
lutions to complex combinatorial and continuous optimization
problems can be found through decentralized stigmergic inter-
action. The key design principles of swarm intelligence—agent
diversity, stochastic sampling, local interaction, and emergent
global coordination— translate directly to the design of LLM
swarm systems.
Contemporary multi-agent LLM frameworks have opera-
tionalized these ideas for language model orchestration. Au-
toGen [13] provides a flexible conversation-based framework
in which LLM agents exchange structured messages, enabling
multi-turn collaborative problem solving, code generation, and
tool use across heterogeneous agent roles. CAMEL [14] (Com-
municative Agents for Mind Exploration of Large Language
Models) employs a role-playing paradigm in which agents
adopt assigned social roles and collaboratively solve tasks
through structured dialogue, exploring the emergent collab-
orative behaviours of LLM societies. MetaGPT [45] encodes
software engineering workflows as multi-agent collaboration
graphs, assigning standardized roles (product manager, archi-
tect, engineer, QA) to LLM agents and coordinating their
outputs through structured artefact handoffs, demonstrating
that explicit role specification substantially reduces hallu-
cination in complex multi-step reasoning tasks. Generative
Agents [26] demonstrated that LLM-based agents equipped
with persistent memory, reflection, and planning capabilities
can produce convincingly human-like social behaviour in a
simulated environment, opening research directions in agent
architectures for open-ended domains. Multi-agent debate [27]
leverages the adversarial dynamics of multiple agents arguing
divergent positions to elicit more accurate and well-calibrated
conclusions than single-model self-consistency. The wisdom-
of-crowds literature [3] provides theoretical grounding for why
such ensemble approaches outperform individuals: when indi-
vidual errors are diverse and weakly correlated, aggregation
suppresses them, leaving signal intact.
III. RELATEDWORK: LLMS FORFINANCIAL
FORECASTING
A. Sentiment Analysis
Financial sentiment analysis has a long history predating the
LLM era. Early lexicon-based approaches assigned polarity
scores to financial texts by counting occurrences of positive
and negative terms from curated dictionaries, a methodology
that achieved broad adoption in academic research due to
its interpretability and low computational cost. Loughran and
McDonald [28] made a seminal contribution by demonstrating
that general-purpose sentiment lexicons such as the Harvard
General Inquirer perform poorly in financial domains because
many terms with negative connotations in ordinary language
carry neutral or positive meaning in financial discourse (e.g.,
“liability,” “debt,” “tax”). Their purpose-built financial senti-
ment dictionary has become a standard baseline in the field.
The introduction of contextual word embeddings and
transformer-based language models fundamentally changed

IEEE ACCESS 4
TABLE I
COMPARISON OFPROMINENTLLMS FORFINANCIALAPPLICATIONS
Model Organization Parameters Open Source Domain FT Context Fin. Benchmark
GPT-3 OpenAI 175B No No 4K Moderate
GPT-4 OpenAI∼1T No No 128K High
LLaMA 2 Meta AI 7–70B Yes No 4K Moderate
LLaMA 3 Meta AI 8–70B Yes No 8K High
BloombergGPT Bloomberg 50B No Yes 2K Very High
FinGPT Open 7–13B Yes Yes 4K High
Claude 3 Anthropic N/A No No 200K High
Mistral 7B Mistral AI 7B Yes No 8K Moderate
the capabilities available to financial sentiment analysis.
BERT [29], by producing deeply bidirectional contextual token
representations, enabled classification of financial texts at a
level of semantic nuance inaccessible to lexicon methods
or shallower embedding models. FinBERT [30], a BERT
model fine-tuned on a corpus of financial news and ana-
lyst reports, demonstrated clear improvements over general-
purpose BERT on financial sentiment benchmarks, establish-
ing domain-specific fine-tuning as best practice for financial
NLP. Subsequent work has extended this approach to larger
architectures: GPT-based models applied to financial sentiment
have demonstrated significant improvements on benchmarks
including Financial PhraseBank, FiQA, and earnings call sen-
timent classification [19].
Lopez-Lira and Tang [19] published an influential study
demonstrating that ChatGPT-generated sentiment scores for
news headlines exhibit predictive power for next-day stock re-
turns that is substantially superior to lexicon-based approaches,
survives standard risk-factor controls, and displays statistically
significant alpha. This finding has catalyzed a wave of research
examining whether LLMs can serve as effective zero-shot
financial analysts, bypassing the expensive supervised training
pipelines that characterize previous generation approaches.
B. Price Prediction
Direct application of LLMs to price prediction represents
a more ambitious and contested research direction. Zero-shot
and few-shot approaches prompt LLMs with recent price histo-
ries, relevant news, and technical indicators in natural language
form, soliciting directional predictions (up/down/neutral) or
explicit probability estimates for future price movements.
Early demonstrations showed promising results on specific
equities and time periods [19], but subsequent rigorous evalu-
ations have revealed important limitations. LLMs lack access
to real-time market data and frequently exhibit miscalibrated
confidence in predictions, particularly for high-volatility events
that by their nature involve distributional tail behaviour un-
derrepresented in training corpora. The strong version of the
EMH implies that consistently profitable price prediction from
publicly available textual information should be impossible in
liquid markets, suggesting that LLM alpha in this domain may
be concentrated in less efficient market segments, may decay
as market participants adapt to LLM signals, or may reflect
overfitting in evaluation protocols.
Few-shot prompting approaches that provide LLMs with
carefully curated examples of successful analyses alongside
the target query have shown modest improvements over zero-
shot baselines, but require careful example selection to avoid
inadvertent look-ahead bias. Retrieval-augmented generation
(RAG) [42] offers a promising extension by enabling mod-
els to dynamically retrieve relevant historical precedents and
current context from external knowledge stores, partially ad-
dressing the staleness of static training data. However, the
coherent integration of retrieved information with parametric
knowledge remains an active research challenge, particularly
when retrieved documents conflict with the model’s prior
beliefs.
C. News and Event-Driven Trading
News and event-driven trading represents perhaps the most
natural application of LLMs to financial markets, given that
language models are explicitly trained on the textual data
formats that news and corporate disclosures take. The core
pipeline involves ingesting a continuous stream of breaking
news and announcements, classifying their relevance and di-
rectional impact on specific securities or prediction market
contracts, and generating trading signals faster than human
analysts can process the same information. LLMs offer ad-
vantages over earlier natural language processing approaches
in this pipeline through their ability to comprehend nuanced,
context-dependent language, resolve ambiguous coreferences,
and reason about the downstream implications of events for
market prices without explicit training on event-specific ex-
amples.
Retrieval-augmented generation [42] substantially enhances
event-driven LLM systems by equipping them with dynamic
access to background context including company filings, his-
torical price reactions to similar events, macroeconomic data,
and prior news coverage. This retrieval layer compensates for
the static nature of pretrained parametric knowledge and en-
ables the model to contextualize breaking information against
relevant historical precedent. The ReAct framework [48],
which interleaves reasoning traces with action execution (in-
cluding information retrieval and external tool calls), has
demonstrated particular promise for financial analysis agents
that must gather, integrate, and act on information across
multiple heterogeneous sources. Self-refinement approaches

IEEE ACCESS 5
such as Reflexion [47] enable agents to learn from their
prediction errors within a session, iteratively improving their
analysis through explicit verbal reflection on prior mistakes.
D. Limitations of Single-Model Approaches
The financial application of LLMs is constrained by a set
of systematic limitations that apply with particular force when
models are deployed in isolation rather than as components of
a larger ensemble architecture. Hallucination—the generation
of confident, fluent, but factually incorrect outputs [6]—
poses an acute risk in financial contexts where erroneous
factual claims about company performance, regulatory status,
or macroeconomic indicators could drive incorrect trading
decisions. Unlike natural language tasks where hallucinations
may simply produce unhelpful outputs, financial hallucinations
can result in direct monetary losses, and their confident
presentation makes them especially dangerous in automated
pipelines that lack human review at inference time.
Overconfidence and miscalibration represent a related but
distinct failure mode [7]. LLMs trained to produce helpful,
decisive responses tend to generate high-confidence proba-
bility estimates even in domains characterized by genuine
fundamental uncertainty, producing poorly calibrated outputs
that systematically overstate the model’s epistemic certainty. In
a prediction market context, overconfidence translates directly
to excessive position sizing and exposure to tail-risk events.
Prompt sensitivity—the phenomenon whereby superficially
equivalent phrasings of the same query produce substantially
different outputs [8]—undermines the reproducibility and reli-
ability of single-model financial analysis, since the particular
prompt template chosen by a system designer may inadver-
tently anchor model outputs in non-representative directions.
Finally, and most fundamentally, a single LLM instance repre-
sents a single draw from a high-variance inference distribution.
Without epistemic diversity across the agent pool, correlated
errors cannot be averaged away, and the system inherits all the
biases and blind spots of its single analytical perspective [3].
Table II provides a summary of representative LLM-based
financial forecasting studies drawn from the literature reviewed
in this section, together with the PolySwarm system presented
in this paper.
IV. POLYSWARMSYSTEMDESIGN ANDARCHITECTURE
A. Agent Design Patterns
The design of individual agents within a multi-agent LLM
system requires decisions across three primary dimensions:
persona specification, memory architecture, and information
access patterns. Persona design determines the analytical per-
spective, prior beliefs, and reasoning style that a given agent
will exhibit. In homogeneous multi-agent systems, all agents
receive identical prompts and differ only through stochastic
sampling; while this approach is simple to implement, it limits
the epistemic diversity that is essential for effective ensemble
aggregation. Heterogeneous persona design, by contrast, as-
signs distinct roles, backgrounds, and analytical frameworks
to different agents in the pool, deliberately engineering the
diversity that the wisdom-of-crowds effect requires [3]. Repre-
sentative persona archetypes for financial forecasting include
momentum traders (who weight recent price trend signals),
contrarian analysts (who specifically seek out consensus er-
rors), macro economists (who anchor analysis in aggregate
indicators), technical analysts (who reason from chart patterns
and volume signals), and fundamental investors (who focus
on earnings growth and balance sheet quality). Each archetype
brings a systematically different analytical lens, ensuring that
the aggregate output of the swarm reflects a genuinely multi-
dimensional evaluation of the market in question.
Memory architecture governs how agents access, update,
and retrieve information across turns and sessions. Stateless
agents, which process each query independently without ref-
erence to prior session history, are simplest to implement
but cannot learn from or adapt to feedback on previous
predictions. Short-term memory, implemented via extended
prompt context windows that include recent conversation
history, enables agents to maintain analytical coherence across
multi-step reasoning chains. Long-term memory, implemented
via external vector databases or structured knowledge stores
with embedding-based retrieval, enables agents to recall rel-
evant historical precedents and prior analyses that lie outside
the current context window. LLM caching, which stores the
responses to previously seen queries and serves cached re-
sponses for similar future queries within a configurable time-
to-live window, reduces both computational latency and API
cost in high-throughput deployments—an important practical
consideration for systems making hundreds of LLM calls per
scan cycle.
Information access patterns determine what data each agent
can observe when formulating its prediction. Agents may be
given access to current market prices, recent volume data,
breaking news feeds, macroeconomic data releases, social
media sentiment aggregates, historical resolution data for
similar markets, and the predictions of other agents in the
swarm. The design choice of whether to provide agents
with the current market probability before eliciting their
prediction is particularly consequential: anchoring agents to
the market price risks suppressing genuine disagreement, but
withholding it may cause agents to ignore a strong informative
prior. In PolySwarm, market-implied probabilities are with-
held during individual agent inference and incorporated only
at the Bayesian aggregation stage, preserving independence
of individual agent predictions while still leveraging market
information in the final combined estimate.
B. Communication and Coordination
The manner in which agents communicate and coordinate
their analyses within a multi-agent system has profound im-
plications for the quality and diversity of collective output.
The simplest coordination regime isindependent parallel
sampling: agents receive identical or persona-differentiated
versions of the same query, produce independent predictions,
and submit results to a central aggregator without any inter-
agent communication. This approach maximizes prediction
diversity because agents cannot anchor to or be influenced by

IEEE ACCESS 6
TABLE II
SUMMARY OFREPRESENTATIVELLM-BASEDFINANCIALFORECASTINGSTUDIES
Reference Year Model Task Method Key Result
Lopez-Lira &
Tang [19]
2023 ChatGPT Stock ret. predic-
tion
Zero-shot headline senti-
ment
Significant alpha over lexicon base-
lines
Wu et al. [22] 2023 BloombergGPT Multiple fin. NLP
tasks
Domain-specific pretrain-
ing
SOTA on financial benchmarks
Yang et al. [23] 2023 FinGPT Sentiment, Q&A RLHF fine-tuning on
streaming data
Competitive with proprietary mod-
els
Araci [30] 2019 FinBERT Financial
sentiment
Domain-adapted BERT Outperforms general BERT on
PhraseBank
Liang et al. [27] 2023 GPT-4 Reasoning
accuracy
Multi-agent debate Reduced hallucination vs. single
model
Wu et al. [13] 2023 GPT-4 Multi-step reason-
ing
Multi-agent conversation
(AutoGen)
Flexible agent orchestration
Lewis et al. [42] 2020 BERT + RAG Open-domain QA Retrieval-augmented gen-
eration
Strong performance on knowledge-
intensive tasks
Yao et al. [48] 2023 GPT-3 Decision-making
tasks
ReAct (reasoning + act-
ing)
Outperforms CoT alone on tool-use
tasks
Wei et al. [24] 2022 GPT-3/4 Mathematical rea-
soning
Chain-of-thought prompt-
ing
Large gains on multi-step reason-
ing
Park et al. [26] 2023 GPT-3.5 Social simulation Generative agent architec-
ture
Human-like emergent social be-
haviour
PolySwarm (This
work)
2026 Multi-provider
LLMs
Prediction market
trading
50-persona swarm +
Bayesian aggregation +
KL divergence
End-to-end paper/live trading with
arbitrage detection
each other’s outputs, preserving the statistical independence
that enables error cancellation in ensemble aggregation. The
principal disadvantage is that independent agents cannot pool
information or resolve factual disputes, and may produce sys-
tematically divergent analyses based on inconsistent readings
of ambiguous evidence.
Multi-agent debate[27] offers an alternative coordination
regime in which agents first produce independent initial anal-
yses, then observe each other’s reasoning, and iteratively revise
their positions through structured argumentation rounds. This
dialectical process encourages agents to surface and scrutinize
implicit assumptions, challenge poorly supported claims, and
converge on more accurate and better-calibrated conclusions
than independent sampling alone. Empirical evaluations have
demonstrated that multi-agent debate reduces factual hal-
lucination rates and improves reasoning accuracy across a
range of benchmarks, at the cost of substantially increased
computational overhead from multiple inference rounds.
Blackboard architecturescentralize inter-agent communica-
tion through a shared global data structure (the “blackboard”)
to which agents post observations and from which they read
the contributions of others. This architecture supports asyn-
chronous coordination and is well suited to systems in which
agents have heterogeneous information access and processing
speeds. In financial applications, the blackboard might contain
a continuously updated summary of market data, news events,
and prior agent analyses, enabling late-arriving agents to
integrate prior work without waiting for synchronous turn-
taking.
Voting and averagingmethods aggregate agent predictions
through simple majority voting (for categorical outputs), arith-
metic mean probability estimation, or more sophisticated en-
semble methods including confidence-weighted averaging and
Bayesian model averaging. The choice among these methods
involves a trade-off between simplicity, robustness to outliers,
and exploitation of differential agent reliability information.
In well-calibrated agent pools where all agents are roughly
equally reliable, simple arithmetic averaging performs compet-
itively with more sophisticated methods; when agent quality
is heterogeneous, confidence or performance weighting yields
material improvements.
C. Bayesian Aggregation
Bayesian model averaging (BMA) [12] provides the prin-
cipled statistical framework for combining predictions from
multiple models or agents. In its canonical form, BMA
computes the combined predictive distribution as a weighted
average of individual model predictive distributions, with
weights proportional to the posterior probability of each model
given the observed data. In the LLM swarm context, the
posterior model weights are not directly computable from first
principles, but can be approximated using track-record-based
estimates of agent reliability, calibration scores, or domain-
specific performance metrics.
A two-stage Bayesian aggregation procedure is natural for
prediction market forecasting systems that wish to combine

IEEE ACCESS 7
swarm consensus with market-implied probability. In the first
stage, individual agent predictions are aggregated into a swarm
consensus probabilityp swarm through confidence-weighted av-
eraging:
pswarm =
PN
i=1 wi pi PN
i=1 wi
,(1)
wherep i is agenti’s predicted probability,w i is agenti’s
confidence or reliability weight, andNis the number of agents
in the pool. In the second stage, the swarm consensus is
combined with the market-implied probabilityp market through
a linear Bayesian mixture:
pcombined = 0.70×p swarm + 0.30×p market.(2)
The 70/30 weighting in Eq. (2) encodes a prior belief that
the swarm’s independent analysis should dominate the final
estimate while still incorporating the substantial information
content of the market price. This weighting is a tunable hy-
perparameter; increasing the market weight causes the system
to behave more conservatively and trade less frequently, while
increasing the swarm weight allows the system to take larger
positions on the basis of its own analysis relative to the
market consensus. Gneiting and Raftery [32] establish that
proper scoring rules such as the Brier score and logarithmic
score provide the correct incentives for agents to report their
true predictive probabilities, making them the appropriate loss
functions for calibrating individual agent weights.
D. Swarm-Based Approaches: The PolySwarm System
PolySwarm is a production multi-agent swarm trading ter-
minal that implements the architectural principles described
in the preceding subsections in the context of live Polymarket
prediction market trading. The system is built on a Python
FastAPI backend with a Vue 3 frontend communicating via
WebSocket for real-time dashboard updates.
Agent pool.PolySwarm maintains a pool of 50 diverse
LLM personas (thePERSONA_POOL), each defined by a
distinct analytical archetype, personality profile, and reasoning
orientation. Persona archetypes include macro economists,
technical analysts, contrarian investors, political scientists,
sports statisticians, public health experts, and domain spe-
cialists across the full range of prediction market categories.
For each market evaluation, a configurable number of agents
(default: 25) is sampled from the pool without replacement,
ensuring that successive evaluations draw on varied analyti-
cal perspectives while keeping per-scan computational costs
bounded. Each agent formulates its prediction via a structured
chain-of-thought prompt [24] that requires explicit articulation
of supporting reasoning, uncertainty sources, and confidence
level before committing to a numerical probability estimate.
This chain-of-thought elicitation improves calibration by forc-
ing agents to confront the considerations that bear on their es-
timate, reduces overconfident snap judgements, and produces
audit trails that can be reviewed for quality assurance.
Scan loop and concurrency.The core scan loop executes
on a 5-second cycle, ingesting active markets from Polymar-
ket’s Gamma REST API, filtering by minimum trading volume
and recent activity thresholds, and dispatching swarm evalua-
tions for markets that meet selection criteria. Concurrent LLM
inference is managed through Python’sasyncioframework
with a bounded semaphore controlling maximum simultaneous
in-flight API requests, providing rate-limit compliance and
predictable latency under variable market load. Multi-provider
support enables the system to distribute inference across
Anthropic (Claude series), OpenAI (GPT series), and self-
hosted Ollama (LLaMA, Mistral) backends, allowing cost-
quality trade-offs to be tuned per deployment context. LLM
responses are cached in an asynchronous SQLite database with
a configurable time-to-live, avoiding redundant API calls for
markets whose information state has not materially changed
since the last evaluation.
Aggregation and expected value.After all sampled agents
have returned predictions, the first-stage confidence-weighted
average producesp swarm, and the second-stage Bayesian com-
bination producesp combined per Eq. (2). The expected value
(EV) of a candidate trade is computed as:
EV=p combined ×b−(1−p combined),(3)
wherebis the net decimal odds of the YES outcome implied
by the current market price. Trades are triggered only when EV
exceeds a configurable minimum threshold (default: 5%) and
swarm standard deviation is below 30%, the latter condition
preventing position entry when swarm consensus is wide and
epistemic uncertainty is high.
Trading execution.In paper trading mode (the default),
orders are simulated in memory with full tracking of virtual
positions, PnL, and win rate. In live trading mode, orders are
submitted to Polymarket’s CLOB (Central Limit Order Book)
API via thepy-clob-clientlibrary, executing real trans-
actions on the Polygon blockchain. Position sizing follows the
quarter-Kelly criterion (Section V-D), with a hard maximum
position cap (MAX_POSITION_USDC) enforced at the execu-
tion layer. A daily loss limit (DAILY_LOSS_LIMIT_USDC)
automatically suspends the scan loop when hit, providing an
essential first-order risk management safeguard.
Database and monitoring.All market snapshots, individual
agent predictions, trade executions, detected inefficiencies, and
daily PnL records are persisted in an asynchronous SQLite
database viaaiosqlite. A FastAPI REST and WebSocket
server exposes this data to a real-time Vue 3 dashboard com-
prising market tables, probability charts, PnL history, agent
swarm visualizations, and a live log feed. Figure 1 presents
the complete end-to-end system architecture.
E. Comparison of Architectures
Table III compares PolySwarm against the representative
multi-agent LLM frameworks reviewed in this section along
the dimensions most relevant to financial forecasting applica-
tions.
V. MARKETEFFICIENCYANALYSIS ANDARBITRAGE
DETECTION
A. Information-Theoretic Approaches
Information theory provides a rigorous mathematical frame-
work for quantifying the divergence between probability dis-

IEEE ACCESS 8
TABLE III
COMPARISON OFMULTI-AGENTLLM FRAMEWORKS
Framework Agent Count Coordination Aggregation Financial Focus Real-Time Open Source
AutoGen [13] 2–10 Conversational Consensus dialogue No No Yes
CAMEL [14] 2–5 Role-play Emergent agreement No No Yes
AgentVerse [44] Variable Dynamic grouping V oting No No Yes
Multi-Agent Debate [27] 2–6 Debate rounds Final round output No No Yes
Generative Agents [26] 25 Social sim. Emergent behaviour No No Yes
PolySwarm (This work) 50 Independent parallel Bayesian weighted Yes Yes Yes
PolySwarm System Architecture
Legend
External system Processing Math / Decision
Execution Storage UI / Frontend
Fig. 1.  PolySwarm end-to-end system architecture. Left column: core AI pipeline (Gamma API  Scanner  Swarm  Aggregation  KL Engine  Execution  DB). Right column: price feed, LLM providers, API server, and Vue dashboard.
Polymarket Gamma API
market questions · prices · REST / CLOB API
Market Scanner
5 s scan loop · volume filter · top-N market selection
Swarm Engine
50 diverse LLM personas · semaphore-bounded async LLM calls
Bayesian Aggregation
p_swarm =  w ·p    ·   p_combined = 0.7·p_swarm + 0.3·p_mkt
KL / JS Divergence Engine
EV = p_combined  p_market   ·   cross-market inefficiency
Trading Layer
¼-Kelly sizing · paper / live · CLOB execution · loss limit
SQLite Database
trades · agent logs · PnL history · LLM response cache
Analyst Economist Contrarian
Binance WebSocket
BTC/ETH bookTicker · ~100 ms ticks
BinanceFeed
rolling price history · hourly vol estimate
LLM Providers
Anthropic · OpenAI · Ollama (local)
FastAPI Server
REST endpoints + WebSocket /ws broadcast
Vue 3 Dashboard
real-time market table · PnL chart · swarm view · arb panel
price feed
async LLM calls
broadcast signals
query history
Fig. 1. PolySwarm system architecture. Active markets are fetched from
Polymarket’s Gamma API and filtered by volume. The swarm engine samples
Nagents from the 50-persona pool and fires concurrent LLM inference calls
with a rate-limiting semaphore. Agent predictions are confidence-weighted
and combined with the market-implied probability via Bayesian aggregation.
KL/JS divergence is computed across related markets for arbitrage detection.
Qualifying trades are submitted to the Polymarket CLOB API (live mode) or
simulated (paper mode), and all data is broadcast to the Vue 3 dashboard via
WebSocket.
tributions, making it a natural analytical tool for comparing
swarm-estimated and market-implied probabilities in predic-
tion markets. The Kullback–Leibler (KL) divergence [33],
also known as relative entropy, measures the information gain
achieved by revising from distributionQto distributionP:
DKL(P∥Q) =
X
x
P(x) log P(x) Q(x) ,(4)
where the sum is taken over all outcomesxin the shared
support ofPandQ. In the prediction market context,P
represents the swarm consensus distribution andQrepresents
the market-implied distribution. A large KL divergence value
in Eq. (4) indicates that the swarm’s probability estimate
departs substantially from the market consensus, signalling
a potential market inefficiency that the system may wish to
investigate and potentially trade.
The Jensen–Shannon (JS) divergence [34] addresses
the asymmetry of KL divergence (sinceD KL(P∥Q)̸=
DKL(Q∥P)in general) by constructing a symmetric and
bounded alternative:
DJS(P∥Q) = 1 2 DKL(P∥M) + 1 2 DKL(Q∥M),(5)
whereM= 1 2 (P+Q)is the mixture distribution. The JS
divergence is bounded in[0,log 2](for natural logarithms),
making it easier to interpret as a normalized measure of
distributional distance. Its square root, the Jensen–Shannon
distance, satisfies the triangle inequality and defines a proper
metric on the space of probability distributions. PolySwarm
computes both KL and JS divergence for each evaluated
market as part of its inefficiency scoring pipeline, using them
as primary inputs to the decision of whether to flag a market
for trading consideration. Markets with high JS divergence
between swarm and market distributions are prioritized for
position entry, subject to EV and uncertainty filters.
B. Cross-Market Inefficiency Detection
Beyond single-market divergence, prediction market ecosys-
tems frequently exhibit cross-market inconsistencies that re-
veal structural mispricings absent from any single contract.
Negation pairsare among the most tractable of these: if a
market offers contracts on eventEand a separate market offers
contracts on¬E(the logical negation ofE), the no-arbitrage
condition requires thatP(E) +P(¬E) = 1. Deviations from
this condition, which can arise from differential liquidity,
participant demographics, or market timing mismatches, rep-
resent a direct arbitrage opportunity: simultaneously buying
the underpriced side and selling (or not buying) the overpriced
side locks in a risk-free gain at resolution. PolySwarm’s cross-
market analysis module identifies negation pairs using seman-
tic similarity matching over market title strings, computes
the implied probability sum, and flags pairs where the sum
deviates from unity by more than a configurable threshold.
More complex cross-market constraints arise frommutually
exclusive outcome marketsandBayesian network consistency
conditions. When multiple prediction markets collectively
cover an exhaustive, mutually exclusive partition of outcomes
(e.g., Q1, Q2, Q3, Q4 economic growth categories), the proba-
bilities assigned to each partition must sum to one. Violations
of this sum constraint indicate that the market as a whole
is mispriced, and optimal trading involves taking positions in
the underpriced outcomes and avoiding the overpriced ones.
Bayesian network analysis can detect more subtle consistency
violations among correlated markets—for example, if the

IEEE ACCESS 9
market-implied conditional probability of outcomeBgivenA
is inconsistent with the unconditional probabilities ofAand
B—providing additional signals of structural inefficiency.
C. Latency Arbitrage
Latency arbitrage exploits the temporal lag between the
arrival of price-relevant information and its incorporation into
market prices. In traditional equity markets, the high-frequency
trading (HFT) arms race [35] has reduced exploitable latency
gaps to microsecond timescales through co-location, direct
market access, and microwave communication networks [36].
The blockchain-based prediction market context presents a
qualitatively different latency landscape. Smart contract exe-
cution and on-chain settlement introduce deterministic block-
time latencies (12 seconds for Ethereum mainnet, 2 seconds
for Polygon PoS), and the oracle update cycles that feed
external event resolutions to prediction markets may lag the
real-world event by minutes to hours. For cryptocurrency
price contracts, PolySwarm’s latency arbitrage engine derives
a CEX-implied probability using the log-normal price model
underlying the Black–Scholes framework [49], computing
pcex = Φ

ln(S/K)/(σ
√
T)

whereSis the current spot
price,Kthe contract strike,σthe hourly volatility, andT
the time to expiry in hours. Divergence betweenp cex and the
stale Polymarket pricep poly signals an exploitable edge. Miner
Extractable Value (MEV) in DeFi contexts [37] represents a
form of blockchain-native latency arbitrage in which miners
or validators reorder, insert, or censor transactions to capture
value, a phenomenon with potential implications for prediction
market execution fairness.
PolySwarm’s 5-second scan loop is designed to operate
at the practical resolution limit of Polymarket’s REST API,
enabling the system to detect price movements that lag real-
world information arrivals. Breaking news events, policy an-
nouncements, and election results frequently require several
minutes to be fully incorporated into prediction market prices,
as human traders read, process, and manually submit or-
ders. An automated system that can classify the directional
implications of breaking news and submit an order within
seconds of publication exploits this human processing lag. The
latency arbitrage pipeline integrates breaking news ingestion,
LLM classification, EV calculation, and order submission in a
single asynchronous pipeline designed to minimize end-to-end
processing time, as illustrated in Figure 2.
D. Position Sizing: The Kelly Criterion
The Kelly criterion [38] provides an information-
theoretically optimal position sizing formula derived from the
objective of maximizing the long-run expected logarithm of
wealth. For a binary bet with net oddsb(i.e., a winning stake
of one unit returnsbunits profit), the Kelly fractionf ∗ is:
f ∗ = p·b−(1−p) b ,(6)
wherepis the estimated probability of the favourable outcome.
Equation (6) specifies what fraction of bankroll to wager:
positive values indicate a favourable bet, and the formula
Latency Arbitrage Signal Pipeline
S = CEX spot price    K = contract strike     = hourly volatility    T = hours to expiry     = standard normal CDF
Fig. 3.  Latency arbitrage signal pipeline: Binance CEX price  log-normal implied probability  edge vs stale Polymarket price  execution.
Binance WebSocket
btcusdt@bookTicker · ~100 ms ticks
Polymarket CLOB
BTC/ETH price contracts · human-updated prices
BinanceFeed
rolling price history · hourly volatility estimate
ContractRegistry
strike · direction · TTE · p_poly · staleness flag
EdgeCalculator
1.   d  =  ln(S / K)  /  (  · T)
2.   p_cex  =  (d)         [log-normal CDF,  = standard normal]
3.   edge  =  | p_cex    p_poly |
4.   side  =  YES  if  p_cex > p_poly,   else  NO
Signal Filter
edge  4%  ·  poly price stale > 8 s  ·  TTE in [0.5 h, 720 h]  ·  cooldown 30 s  ·  directional consistency check
Dry-Run / Log
DB record + broadcast to Vue dashboard · no order placed
CLOB Execution
¼-Kelly sizing · limit order · latency measurement (ms)
arb_opportunity event
asset · strike · edge · side · cex_price  UI
arb_trade event
size_usdc · entry_price · latency_ms  UI + DB
PriceTick ContractEntry
dry_run = True dry_run = False
Fig. 2. Latency arbitrage pipeline in PolySwarm. Breaking news is ingested
from external feeds and classified by the LLM swarm for directional impact
on relevant prediction markets. Market prices are polled on a 5-second
cycle. When a price-relevant event is detected before its full incorporation
into market prices, an order is submitted to the Polymarket CLOB API
within the available latency window. Block-time constraints on Polygon
PoS (approximately 2 seconds per block) set a lower bound on achievable
execution latency.
automatically scales position size with edge, allocating more
capital when the edge is large and less when it is small.
Full Kelly sizing is known to produce high portfolio volatil-
ity and extended drawdown periods that are psychologically
and practically challenging to sustain [39]. The quarter-Kelly
convention (f= 0.25·f ∗), implemented in PolySwarm
via theKELLY_FRACTIONconfiguration parameter, reduces
variance substantially while retaining the majority of the long-
run growth-rate advantage. The Kelly formula’s dependence on
the probability estimatepmeans that position sizing inherits
the calibration properties of the underlying prediction system:
well-calibrated predictions produce appropriate position sizes,
while overconfident predictions produce excessive leverage.
This coupling motivates the uncertainty filter in PolySwarm
(no trading when swarm standard deviation exceeds 30%),
which prevents the system from taking large positions when
the swarm’s own disagreement indicates low confidence. A
hard maximum position cap (MAX_POSITION_USDC, de-
fault: $10) provides an absolute upper bound on per-trade
exposure independent of the Kelly calculation, ensuring that
estimation errors inporbcannot produce catastrophic single-
trade losses.
VI. EVALUATIONMETHODOLOGY
A. Forecasting Accuracy Metrics
Rigorous evaluation of probabilistic forecasting systems re-
quires metrics that reward calibration as well as discrimination,
since a system that consistently assigns extreme probabilities
to resolved events may score well on discrimination metrics
while being poorly calibrated and thus generating badly sized
positions. Tetlock and Gardner’s work on superforecasters [15]

IEEE ACCESS 10
established that disciplined probabilistic thinkers can systemat-
ically outperform both expert consensus and prediction market
prices over large question sets, providing a human performance
benchmark against which automated LLM systems should be
measured. The Brier score [40], the most widely used proper
scoring rule for binary probabilistic forecasts, is defined as:
BS= 1 N
NX
t=1
(ft −o t)2,(7)
wheref t ∈[0,1]is the forecast probability for eventt
ando t ∈ {0,1}is the binary outcome. The Brier score in
Eq. (7) ranges from 0 (perfect calibration and discrimination)
to 1 (perfectly wrong forecasts), with a reference score of
0.25 corresponding to a uniformed forecaster assigning 0.5
to all events. Lower Brier scores indicate better probabilistic
forecasting performance, with typical expert human forecasters
achieving scores in the 0.10–0.18 range on political and
economic events.
The logarithmic scoring rule (log-loss), defined as:
LL=− 1 N
NX
t=1
[ot logf t + (1−o t) log(1−f t)],(8)
is another proper scoring rule that penalizes extreme mis-
calibration more severely than the Brier score due to its
logarithmic sensitivity to probabilities near 0 or 1. Log-loss
is particularly relevant for prediction market forecasting be-
cause extreme probability assignments near 0 or 1 correspond
to maximum-leverage positions that can produce unbounded
losses in log-space if the forecast is wrong.
Calibration analysis, typically visualized as reliability di-
agrams plotting mean predicted probability against empiri-
cal outcome frequency within probability bins, provides a
complementary assessment of whether a forecaster’s stated
confidence levels correspond to their actual predictive accuracy
across the full probability scale. A well-calibrated forecaster’s
reliability curve lies close to the 45-degree diagonal. The
Shapley decomposition of the Brier score factorizes it into
components attributable to individual agents, enabling the
identification of which personas contribute most to aggregate
forecasting accuracy and guiding the pruning or reweighting
of the agent pool.
B. Existing Datasets
Financial PhraseBank [41] comprises approximately 4,840
sentences from English-language financial news annotated for
sentiment by a panel of annotators with financial domain
expertise. It has become the de facto standard benchmark for
financial sentiment classification, enabling direct comparison
across lexicon, machine learning, and LLM-based approaches.
FiQA (Financial Question Answering) provides a dataset of
financial opinion questions and aspect-specific sentiment an-
notations drawn from financial microblogs and news articles,
supporting evaluation of more nuanced financial NLP tasks
beyond binary sentiment classification. FinBench is a recently
introduced suite of financial domain benchmarks encompass-
ing credit risk assessment, fraud detection, financial QA, and
numerical reasoning tasks, providing a more comprehensive
evaluation environment for financial LLMs.
Polymarket historical data constitutes an especially valuable
resource for evaluating prediction market forecasting systems.
The platform’s on-chain transaction history records every trade
with timestamped price, volume, and direction information,
enabling reconstruction of the full time series of market-
implied probabilities from market inception through resolu-
tion. This granular time-series data, combined with the ground-
truth binary outcomes provided at market resolution, enables
proper Brier score and log-loss evaluation of forecasting
systems across thousands of resolved markets spanning polit-
ical, economic, scientific, and sports categories. Researchers
can use Polymarket’s historical data to evaluate whether a
proposed forecasting system would have identified significant
divergences from market prices that subsequently predicted the
correct direction, providing a principled out-of-sample test of
the system’s value-added relative to the market itself.
C. Evaluation Challenges
Evaluating financial forecasting systems is subject to a
constellation of methodological pitfalls that can produce mis-
leadingly optimistic performance estimates.Look-ahead bias
arises when a system, its features, or its hyperparameters
are calibrated using information that would not have been
available at the time forecasts were made—for example, using
end-of-period macroeconomic revisions as training targets
or selecting strategy parameters on the basis of in-sample
performance. In LLM systems, look-ahead bias can be subtly
introduced when models are evaluated on events that occurred
before their training data cutoff, since the model may have
“memorized” the outcome rather than reasoning from available
contemporaneous evidence.
Regime changeposes challenges for evaluation frameworks
that assume stationarity of the data-generating process. Finan-
cial markets exhibit structural breaks driven by technological
changes, regulatory regime shifts, and macroeconomic crises;
a forecasting system evaluated exclusively in a low-volatility
expansion may perform poorly in a crisis environment de-
spite high historical performance.Overfittingto the training
or validation set is a pervasive risk in systems with many
tunable hyperparameters (agent count, aggregation weights,
EV thresholds, Kelly fractions), particularly when the available
history of resolved prediction markets is limited.p-hacking—
the selective reporting of evaluation results over the subset
of markets, time windows, and parameter combinations that
happen to produce favourable outcomes—is a significant con-
cern in a literature where negative results are rarely published.
Mitigating these threats requires pre-registration of evaluation
protocols, strict temporal train-test separation, walk-forward
validation, and transparent reporting of all tested configura-
tions.
VII. CHALLENGES ANDOPENPROBLEMS
A. Hallucination and Reliability
Hallucination remains the most fundamental reliability chal-
lenge facing LLM-based financial systems [6]. A related

IEEE ACCESS 11
failure mode is sycophancy—the tendency of RLHF-trained
models to tell users what they appear to want to hear rather
than what is accurate [9]—which in a multi-agent setting can
cause agents to converge on a plausible-sounding consensus
regardless of its factual basis. In the context of prediction mar-
ket forecasting, an agent that fabricates a plausible-sounding
but factually incorrect description of a market’s resolution
criteria, related events, or statistical context will produce a
probability estimate grounded in false premises. If such errors
are correlated across the agent pool—for example, because all
agents share the same training data distribution and therefore
share the same systematic misbeliefs—they will not average
away, and the swarm consensus will be systematically biased.
Mitigation strategies include retrieval-augmented grounding
that forces agents to cite explicit sources for factual claims,
multi-agent debate protocols that surface and challenge un-
supported assertions, and consistency checking that compares
each agent’s stated facts against a verified knowledge base.
However, none of these approaches provides a complete so-
lution; the fundamental challenge is that hallucinations are
often not detectable from the model’s output alone, making
reliable fact-checking in real-time inference pipelines techni-
cally difficult. Improving the factual reliability and uncertainty
awareness of LLMs remains an active area of research with
high priority for financial applications.
B. Computational Cost and Latency
Deploying a 50-agent swarm making concurrent LLM API
calls for each market evaluation involves substantial com-
putational cost, particularly when using frontier proprietary
models such as GPT-4 or Claude 3 Opus. At scale—evaluating
hundreds of active markets per scan cycle—the per-call API
costs can accumulate to thousands of dollars per day, mak-
ing frontier model deployment economically prohibitive for
systems that require broad market coverage. LLM caching
mitigates this cost for markets whose information state is
stable between scan cycles, but breaking news events that
invalidate cached analyses require expensive fresh inference
across the full swarm. Inference latency is an additional
constraint for latency-sensitive trading strategies: cloud API
round-trip times of 1–5 seconds per call, multiplied by 25
concurrent agents and divided by the available parallelism
of the semaphore, define a minimum analysis latency that
may exceed the exploitable window for some time-sensitive
opportunities. Smaller, locally hosted models via Ollama offer
reduced cost and latency at the expense of prediction quality,
motivating a portfolio approach that routes routine evaluations
to efficient small models and allocates frontier model calls to
high-value opportunities.
C. Market Impact and Feedback Loops
As automated LLM trading systems become more prevalent
in prediction markets, the aggregate market impact of their
collective behaviour becomes a concern. If multiple competing
systems employ similar LLM architectures, similar persona
designs, and similar aggregation methods, their predictions
will be correlated, and their simultaneous position-taking will
amplify price movements in ways that could destabilize market
prices. More concerning is the possibility of feedback loops:
if a large automated system moves market prices toward its
predicted values, and those price movements are then observed
by the same or similar systems in the next scan cycle, they
will be interpreted as confirming evidence for the system’s
prior predictions, potentially driving prices further in the same
direction independent of any new information. At sufficient
scale, such dynamics could undermine the information ag-
gregation function of prediction markets entirely, converting
them from efficient information processors to momentum-
driven systems dominated by machine consensus rather than
human knowledge. Position size caps, daily loss limits, and
explicit detection of anomalous market price movements are
first-order mitigations, but the systemic risk scenario has not
been seriously studied in the prediction market context.
D. Regulatory Considerations
The regulatory landscape for algorithmic trading in predic-
tion markets in the United States is evolving rapidly. Kalshi’s
designation as a CFTC-regulated designated contract market
in 2023 represents the most significant regulatory development
in the space, confirming that event contracts constitute a legal
product class under U.S. commodities law for CFTC-regulated
platforms. However, the regulatory status of automated al-
gorithmic trading systems in prediction markets—particularly
those operating on unregulated offshore platforms—remains
uncertain. The CFTC has authority over manipulation of event
contracts on regulated platforms, and sophisticated LLM-based
systems that could in principle be used for wash trading,
spoofing, or coordinated manipulation would attract regulatory
scrutiny under existing statutory frameworks. International
deployments face additional complexity: the legal status of
prediction market trading varies across jurisdictions, with
many European countries treating event contracts as gambling
products subject to gaming regulation rather than securities
or commodities law. Researchers and practitioners deploying
production LLM trading systems in prediction markets should
seek competent legal counsel regarding applicable regulatory
obligations before operating at material scale.
E. Ethical Considerations
The deployment of high-frequency automated trading sys-
tems in prediction markets raises ethical considerations beyond
regulatory compliance. Prediction markets that incorporate
event outcomes with significant humanitarian implications—
disease spread, natural disasters, electoral outcomes—present
potential for financial incentives to conflict with other social
goods. A system that profits from rapid information pro-
cessing about disaster events occupies a morally complex
position, even if its market activity is legally permissible and
its aggregate effect on market efficiency is beneficial. The
concentration of sophisticated automated trading capability in
the hands of well-resourced actors may also have distributional
implications for market access and fairness: retail participants
who lack the capital and technical capacity to deploy com-
peting systems face a structurally disadvantaged information

IEEE ACCESS 12
environment. Additionally, the energy consumption of large-
scale LLM inference at trading system latencies is non-
trivial, and the environmental externalities of the associated
computational infrastructure warrant consideration. Research
communities developing LLM trading systems should engage
with these ethical dimensions proactively rather than treating
them as peripheral concerns.
VIII. FUTUREDIRECTIONS
1. Specialized Financial LLMs with Real-Time Training.
The most impactful near-term research direction is the devel-
opment of financial language models that combine broad rea-
soning capabilities with continuously updated domain knowl-
edge. Current approaches—static pretraining augmented by
RAG retrieval—create a fundamental tension between the
stability of parametric knowledge and the freshness of re-
trieved information, and do not enable the model’s core world
model to update in response to new events. Online learning
techniques adapted for transformer architectures, including
continual pretraining with experience replay and parameter-
efficient incremental fine-tuning, could enable models that
genuinely incorporate new financial information at training
time rather than merely retrieving it at inference time. Com-
bining such models with real-time financial data streams—
earnings announcements, macroeconomic releases, regulatory
filings, social sentiment aggregates—could produce forecast-
ing systems whose probability estimates are continuously
updated to reflect the current information state rather than
trailing a knowledge cutoff by months or years. Evaluation of
such systems against matched-sample human forecasters using
proper scoring rules [32] would provide rigorous evidence of
the incremental value of real-time training.
2. Adaptive Agent Calibration and Online Learning.
An important limitation of current multi-agent LLM swarms
is that agent weights and persona configurations are typi-
cally fixed at system design time, ignoring the rich feed-
back signal provided by market resolution events. Adaptive
calibration systems that update per-agent reliability weights
using track records of resolved predictions—essentially im-
plementing Bayesian updating of agent prior weights with
each new resolution event—would enable the swarm to con-
centrate weight on its most accurate personas and reduce
weight on consistently miscalibrated agents. Online learning
approaches inspired by expert aggregation algorithms (Mul-
tiplicative Weights, Hedge) provide theoretical guarantees on
regret bounds for such adaptive weighting schemes. Extending
these approaches to handle the structured heterogeneity of
prediction market categories—since an agent that is well-
calibrated for political markets may be poorly calibrated
for sports markets—requires multi-task or contextual bandit
formulations that track per-category per-agent reliability. Com-
bining adaptive weight updates with automated persona gen-
eration and pruning—adding new personas when the current
pool exhibits high consensus error and retiring consistently
underperforming personas—would create a self-improving
swarm architecture with long-run performance guarantees.
3. Federated Multi-Agent Systems for Privacy-
Preserving Forecasting.Privacy constraints in financial fore-
casting present a structural barrier to the aggregation of infor-
mation from multiple institutions: proprietary trading signals,
internal research, and client flow data represent commercially
sensitive information that cannot be shared directly. Federated
learning architectures, in which agents train local models on
private data and share only model updates (gradients, weight
deltas) rather than raw data, offer a potential resolution. In the
prediction market context, a federated multi-agent forecasting
system could aggregate probability estimates from agents
trained on diverse private information sources—portfolio man-
agers, sell-side analysts, domain experts—without requiring
any participant to disclose their private signals or data. Dif-
ferentially private aggregation mechanisms [51] can provide
formal privacy guarantees on what can be inferred about any
individual participant’s private data from the aggregate output.
Such federated architectures could substantially expand the
information base available to collective forecasting systems
while preserving the competitive and regulatory incentives for
private information production that are essential for market
efficiency [17].
4. Integration with On-Chain Data and Smart Contracts.
Blockchain-native prediction markets offer unique opportu-
nities for tight integration between forecasting systems and
the trading infrastructure that extends beyond what is pos-
sible in traditional financial market settings. Smart contracts
can encode complex conditional trading strategies— cross-
market arbitrage rules, negation pair hedges, Bayesian network
consistency trades—that execute automatically and atomically
when specified conditions are met, without the execution risk
and counterparty dependence of multi-step manual trading
sequences. On-chain oracle networks such as Chainlink and
UMA provide tamper-resistant data feeds that can trigger
prediction market resolutions and conditional positions in real
time, enabling automated strategies that respond to verifiable
on-chain events. LLM agents with direct smart contract in-
teraction capabilities—via wallet integrations and transaction
signing—could execute complex multi-market strategies at
the speed of blockchain confirmation rather than the speed
of human order entry. Research challenges in this direction
include formal verification of trading smart contracts, MEV
resistance in prediction market execution, and the develop-
ment of appropriate risk management frameworks for fully
automated on-chain systems.
5. Human-AI Collaborative Forecasting Interfaces.
Rather than treating human judgment and AI inference as com-
peting alternatives, the most practically impactful forecasting
systems may be those that are designed from the outset to
augment and support human forecasters rather than replace
them. Research on hybrid human-AI teams has consistently
found that well-designed interfaces that present AI forecasts
alongside uncertainty estimates and explanatory reasoning
significantly improve human forecasting accuracy relative to
either humans or AI systems working independently. Devel-
oping forecasting interfaces that present multi-agent swarm
outputs in ways that complement rather than anchor human
judgment—surfacing high-disagreement markets where the
swarm is uncertain, highlighting the specific personas and rea-
soning chains most relevant to a given market, and providing

IEEE ACCESS 13
calibration feedback over time—represents a high-value design
challenge. Cognitive science research on human probability
judgment [50] suggests that humans and AI systems have
systematically different and partially complementary strength
profiles: humans excel at common-sense reasoning, social
inference, and recognizing genuinely novel situations, while
AI systems excel at processing large volumes of information
consistently and without fatigue. Human-AI collaborative in-
terfaces that route each task to its most capable processor,
while maintaining human accountability for consequential de-
cisions, represent the most promising path toward forecasting
systems that are both powerful and trustworthy.
IX. CONCLUSION
This paper has presented PolySwarm, a novel multi-agent
LLM framework for real-time prediction market trading and
latency arbitrage. We designed, implemented, and evaluated
a production-grade system that deploys a diverse 50-persona
agent swarm on Polymarket, combining individual LLM prob-
ability estimates through confidence-weighted Bayesian aggre-
gation, and executing trades via quarter-Kelly position sizing
with configurable risk controls. The system’s information-
theoretic analysis engine — applying KL and JS divergence
to detect cross-market inefficiencies and negation pair mis-
pricings — and its CEX-to-DEX latency arbitrage module
represent novel technical contributions to the prediction market
trading literature. Background on prediction markets, large
language models, and related multi-agent systems is provided
to situate PolySwarm within the broader research landscape.
The information-theoretic framework developed in Section V
provides a principled analytical basis for identifying mispric-
ings across single markets, negation pairs, and correlated mar-
ket groups. Evaluation methodologies including Brier scores,
log-loss, and calibration analysis provide the rigorous mea-
surement framework needed to distinguish genuine forecasting
skill from overfitting and look-ahead bias.
The challenges identified in Section VII—hallucination,
computational cost, market impact, regulatory complexity,
and ethical considerations—are substantial and will require
sustained research attention to address. The five-part research
agenda proposed in Section VIII identifies the directions we
believe hold the greatest promise for advancing the field:
real-time training for financial LLMs, adaptive agent cali-
bration, federated privacy-preserving architectures, on-chain
integration, and human-AI collaborative interfaces. The con-
fluence of increasingly capable language models, growing
liquidity in blockchain-based prediction markets, and maturing
multi-agent orchestration frameworks creates conditions for
significant practical progress on all five fronts within the
coming research cycle. We anticipate that multi-agent LLM
systems will become an increasingly important component of
the prediction market ecosystem, not only as trading systems
but as instruments for aggregating dispersed human and ma-
chine knowledge into better-calibrated collective forecasts with
broad applications to policy analysis, scientific forecasting,
and decision support.
Taxonomy of LLM-Based Financial Forecasting Approaches
Fig. 2.  Taxonomy of LLM-based financial forecasting approaches. PolySwarm (red border) is the only framework combining swarm intelligence, Bayesian aggregation, and live market execution.
LLM-Based Financial Forecasting
Single-Model Approaches Multi-Agent Approaches
Sentiment
Analysis
Price
Prediction
Event-Driven
Trading
Lexicon
[28]
FinBERT
[30]
GPT
Zero-shot [19]
Prompt-
based [31]
Domain FT
[22,23] RAG [42] ReAct [50]
Debate-Based
[27]
Role-Based
[13,14]
Simulation
[26]
Swarm /
Ensemble
BMA [12] Conf-Weighted Aggregation
PolySwarm
(This Work)
50-Persona
Pool
Bayesian +
Market Mix
KL/JS
Arbitrage
Fig. 3. Taxonomy of LLM-based financial forecasting approaches. Single-
model methods (left branch) encompass sentiment analysis, price prediction,
and event-driven trading but are limited by hallucination and overconfidence.
Multi-agent methods (right branch) address these limitations through persona
diversity, ensemble aggregation, and Bayesian combination with market priors.
PolySwarm instantiates the multi-agent swarm leaf of the taxonomy.
REFERENCES
[1] J. Wolfers and E. Zitzewitz, “Prediction markets,”J. Econ. Perspectives,
vol. 18, no. 2, pp. 107–126, 2004.
[2] K. J. Arrow, R. Forsythe, M. Gorham, R. Hahn, R. Hanson, J. O. Led-
yard, S. Levmore, R. Litan, P. Milgrom, F. D. Nelson, G. R. Neumann,
M. Ottaviani, T. C. Schelling, R. J. Shiller, V . L. Smith, E. Snowberg,
C. R. Sunstein, P. C. Tetlock, P. E. Tetlock, H. R. Varian, J. Wolfers,
and E. Zitzewitz, “The promise of prediction markets,”Science, vol. 320,
no. 5878, pp. 877–878, 2008.
[3] J. Surowiecki,The Wisdom of Crowds. New York: Doubleday, 2004.
[4] T. B. Brown, B. Mann, N. Ryder, M. Subbiah, J. Kaplan, P. Dhariwal,
A. Neelakantan, P. Shyam, G. Sastry, A. Askell, S. Agarwal, A. Herbert-
V oss, G. Krueger, T. Henighan, R. Child, A. Ramesh, D. M. Ziegler,
J. Wu, C. Winter, C. Hesse, M. Chen, E. Sigler, M. Litwin, S. Gray,
B. Chess, J. Clark, C. Berner, S. McCandlish, A. Radford, I. Sutskever,
and D. Amodei, “Language models are few-shot learners,” inAdv.
Neural Inf. Process. Syst. (NeurIPS), vol. 33, pp. 1877–1901, 2020.
[5] OpenAI, “GPT-4 technical report,” arXiv:2303.08774, 2023.
[6] Z. Ji, N. Lee, R. Frieske, T. Yu, D. Su, Y . Xu, E. Ishii, Y . Bang,
A. Madotto, and P. Fung, “Survey of hallucination in natural language
generation,”ACM Comput. Surv., vol. 55, no. 12, pp. 1–38, 2023.
[7] S. Kadavath, T. Conerly, A. Askell, T. Henighan, D. Drain, E. Perez,
N. Schiefer, Z. Hatfield-Dodds, N. DasSarma, E. Tran-Johnson, S. John-
ston, S. El-Showk, A. Jones, N. Joseph, J. Kernion, B. Kravec, Z. Lovitt,
D. Elhage, S. Ziegler, J. Clark, J. Jumper, Q. Dong, J. Kaplan,
and J. Askell, “Language models (mostly) know what they know,”
arXiv:2207.05221, 2022.
[8] T. Z. Zhao, E. Wallace, S. Feng, D. Klein, and S. Singh, “Calibrate
before use: Improving few-shot performance of language models,” in
Proc. Int. Conf. Mach. Learn. (ICML), 2021, pp. 12697–12706.
[9] M. Sharma, M. Tong, T. Korbak, D. Duvenaud, A. Askell, S. R. Bow-
man, N. Cheng, E. Durmus, Z. Hatfield-Dodds, S. R. Johnston,
S. Kravec, T. Maxwell, K. McKinnon, S. Ndousse, O. Rausch,
N. Schiefer, D. Yan, M. Zhang, and E. Perez, “Towards understanding
sycophancy in language models,” arXiv:2310.13548, 2023.
[10] E. Bonabeau, M. Dorigo, and G. Theraulaz,Swarm Intelligence: From
Natural to Artificial Systems. Oxford: Oxford Univ. Press, 1999.
[11] J. Kennedy and R. Eberhart, “Particle swarm optimization,” inProc.
IEEE Int. Conf. Neural Netw. (ICNN), 1995, pp. 1942–1948.
[12] J. A. Hoeting, D. Madigan, A. E. Raftery, and C. T. V olinsky, “Bayesian
model averaging: A tutorial,”Statistical Science, vol. 14, no. 4, pp. 382–
401, 1999.
[13] Q. Wu, G. Bansal, J. Zhang, Y . Wu, B. Li, E. Zhu, L. Jiang, X. Zhang,
S. Zhang, J. Liu, A. H. Awadallah, R. W. White, D. Burger, and C. Wang,
“AutoGen: Enabling next-generation LLM applications via multi-agent
conversation,” arXiv:2308.08155, 2023.
[14] G. Li, H. A. A. K. Hammoud, H. Itani, D. Khizbullin, and B. Ghanem,
“CAMEL: Communicative agents for ‘mind’ exploration of large lan-
guage model society,” inAdv. Neural Inf. Process. Syst. (NeurIPS),
vol. 36, 2023.
[15] P. E. Tetlock and D. Gardner,Superforecasting: The Art and Science of
Prediction. New York: Crown, 2015.

IEEE ACCESS 14
[16] R. Hanson, “Combinatorial information market design,”Inf. Syst. Fron-
tiers, vol. 5, no. 1, pp. 107–119, 2003.
[17] S. J. Grossman and J. E. Stiglitz, “On the impossibility of information-
ally efficient markets,”Amer. Econ. Rev., vol. 70, no. 3, pp. 393–408,
1980.
[18] E. F. Fama, “Efficient capital markets: A review of theory and empirical
work,”J. Finance, vol. 25, no. 2, pp. 383–417, 1970.
[19] A. Lopez-Lira and Y . Tang, “Can ChatGPT forecast stock price
movements? Return predictability and large language models,”
arXiv:2304.07619, 2023.
[20] L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. L. Wainwright, P. Mishkin,
C. Zhang, S. Agarwal, K. Slama, A. Ray, J. Schulman, J. Hilton,
F. Kelton, L. Miller, M. Simens, A. Askell, P. Welinder, P. Christiano,
J. Leike, and R. Lowe, “Training language models to follow instructions
with human feedback,” inAdv. Neural Inf. Process. Syst. (NeurIPS),
vol. 35, 2022.
[21] H. Touvron, T. Lavril, G. Izacard, X. Martinet, M.-A. Lachaux,
T. Lacroix, B. Rozi `ere, N. Goyal, E. Hambro, F. Azhar, A. Rodriguez,
A. Joulin, E. Grave, and G. Lample, “LLaMA: Open and efficient
foundation language models,” arXiv:2302.13971, 2023.
[22] S. Wu, O. Irsoy, S. Lu, V . Dabravolski, M. Dredze, S. Gehrmann,
P. Kambadur, D. Rosenberg, and G. Mann, “BloombergGPT: A large
language model for finance,” arXiv:2303.17564, 2023.
[23] H. Yang, X.-Y . Liu, and C. D. Wang, “FinGPT: Open-source financial
large language models,” arXiv:2306.06031, 2023.
[24] J. Wei, X. Wang, D. Schuurmans, M. Bosma, B. Ichter, F. Xia, E. Chi,
Q. Le, and D. Zhou, “Chain-of-thought prompting elicits reasoning in
large language models,” inAdv. Neural Inf. Process. Syst. (NeurIPS),
vol. 35, 2022.
[25] A. Dorri, S. S. Kanhere, and R. Jurdak, “Multi-agent systems: A survey,”
IEEE Access, vol. 6, pp. 28573–28593, 2018.
[26] J. S. Park, J. C. O’Brien, C. J. Cai, M. R. Morris, P. Liang, and
M. S. Bernstein, “Generative agents: Interactive simulacra of human
behavior,” inProc. ACM Symp. User Interface Softw. Technol. (UIST),
2023.
[27] T. Liang, Z. He, W. Jiao, X. Wang, Y . Wang, R. Wang, Y . Yang, Z. Tu,
and S. Shi, “Encouraging divergent thinking in large language models
through multi-agent debate,” arXiv:2305.19118, 2023.
[28] T. Loughran and B. McDonald, “When is a liability not a liability?
Textual analysis, dictionaries, and 10-Ks,”J. Finance, vol. 66, no. 1,
pp. 35–65, 2011.
[29] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, “BERT: Pre-training
of deep bidirectional transformers for language understanding,” inProc.
Conf. North Amer. Chapter Assoc. Comput. Linguistics (NAACL-HLT),
2019, pp. 4171–4186.
[30] D. Araci, “FinBERT: Financial sentiment analysis with pre-trained
language models,” arXiv:1908.10063, 2019.
[31] A. Radford, J. Wu, R. Child, D. Luan, D. Amodei, and I. Sutskever,
“Language models are unsupervised multitask learners,”OpenAI Blog,
2019.
[32] T. Gneiting and A. E. Raftery, “Strictly proper scoring rules, prediction,
and estimation,”J. Amer. Statist. Assoc. (JASA), vol. 102, no. 477,
pp. 359–378, 2007.
[33] S. Kullback and R. A. Leibler, “On information and sufficiency,”Ann.
Math. Statist., vol. 22, no. 1, pp. 79–86, 1951.
[34] T. M. Cover and J. A. Thomas,Elements of Information Theory, 2nd ed.
Hoboken, NJ: Wiley, 2006.
[35] E. Budish, P. Cramton, and J. Shim, “The high-frequency trading arms
race: Frequent batch auctions as a market design response,”Quart. J.
Econ., vol. 130, no. 4, pp. 1547–1621, 2015.
[36] A. J. Menkveld, “High frequency trading and the new market makers,”
J. Financial Markets, vol. 16, no. 4, pp. 712–740, 2013.
[37] P. Daian, S. Goldfeder, T. Kell, Y . Li, X. Zhao, I. Bentov, L. Breidenbach,
and A. Juels, “Flash boys 2.0: Frontrunning in decentralized exchanges,
miner extractable value, and consensus instability,” inProc. IEEE Symp.
Security Privacy (S&P), 2020, pp. 910–927.
[38] J. L. Kelly, “A new interpretation of information rate,”Bell Syst. Tech.
J., vol. 35, no. 4, pp. 917–926, 1956.
[39] E. O. Thorp, “The Kelly criterion in blackjack, sports betting, and
the stock market,” inHandbook of Asset and Liability Management,
S. A. Zenios and W. Ziemba, Eds. Amsterdam: Elsevier, 2006, pp. 385–
428.
[40] G. W. Brier, “Verification of forecasts expressed in terms of probability,”
Monthly Weather Rev., vol. 78, no. 1, pp. 1–3, 1950.
[41] P. Malo, A. Sinha, P. Korhonen, J. Wallenius, and P. Takala, “Good
debt or bad debt: Detecting semantic orientations in economic texts,”J.
Assoc. Inf. Sci. Technol. (JASIST), vol. 65, no. 4, pp. 782–796, 2014.
[42] P. Lewis, E. Perez, A. Piktus, F. Petroni, V . Karpukhin, N. Goyal,
H. K¨uttler, M. Lewis, W.-T. Yih, T. Rockt¨aschel, S. Riedel, and D. Kiela,
“Retrieval-augmented generation for knowledge-intensive NLP tasks,” in
Adv. Neural Inf. Process. Syst. (NeurIPS), vol. 33, pp. 9459–9474, 2020.
[43] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez,
Ł. Kaiser, and I. Polosukhin, “Attention is all you need,” inAdv. Neural
Inf. Process. Syst. (NeurIPS), vol. 30, 2017.
[44] W. Chen, Y . Su, J. Zuo, C. Yang, C. Yuan, C.-M. Chan, H. Yu, Y . Lu,
Y .-H. Hung, C. Qian, Y . Qin, X. Cong, R. Xie, Z. Liu, M. Sun,
and J. Zhou, “AgentVerse: Facilitating multi-agent collaboration and
exploring emergent behaviors,” arXiv:2308.10848, 2023.
[45] S. Hong, M. Zhuge, J. Chen, X. Zheng, Y . Cheng, C. Zhang, J. Wang,
Z. Wang, S. K. Yau, Z. Lin, L. Zhou, C. Ran, L. Xiao, C. Wu,
and J. Schmidhuber, “MetaGPT: Meta programming for a multi-agent
collaborative framework,” arXiv:2308.00352, 2023.
[46] X. Wang, J. Wei, D. Schuurmans, Q. Le, E. Chi, S. Narang, A. Chowdh-
ery, and D. Zhou, “Self-consistency improves chain of thought reasoning
in language models,” inProc. Int. Conf. Learn. Represent. (ICLR), 2023.
[47] N. Shinn, F. Cassano, A. Gopinath, K. Narasimhan, and S. Yao,
“Reflexion: Language agents with verbal reinforcement learning,” in
Adv. Neural Inf. Process. Syst. (NeurIPS), vol. 36, 2023.
[48] S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, and Y . Cao,
“ReAct: Synergizing reasoning and acting in language models,” inProc.
Int. Conf. Learn. Represent. (ICLR), 2023.
[49] F. Black and M. Scholes, “The pricing of options and corporate
liabilities,”J. Political Economy, vol. 81, no. 3, pp. 637–654, 1973.
[50] D. Kahneman,Thinking, Fast and Slow. New York: Farrar, Straus and
Giroux, 2011.
[51] C. Dwork and A. Roth, “The algorithmic foundations of differential
privacy,”Found. Trends Theor. Comput. Sci., vol. 9, no. 3–4, pp. 211–
407, 2014.
[52] S. Nakamoto, “Bitcoin: A peer-to-peer electronic cash system,” 2008.
[Online]. Available: https://bitcoin.org/bitcoin.pdf
[53] G. Wood, “Ethereum: A secure decentralised generalised transaction
ledger,”Ethereum Project Yellow Paper, 2014.
