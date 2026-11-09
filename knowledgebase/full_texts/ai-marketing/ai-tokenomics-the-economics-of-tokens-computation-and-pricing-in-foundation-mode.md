---
title: 'AI Tokenomics: The Economics of Tokens, Computation, and Pricing in Foundation Models'
url: https://arxiv.org/abs/2606.24616
category: ai-marketing
subcategory: empirical
date: 2026-06
venue: ''
authors:
- Quanyan Zhu
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.24616
pages: 40
chars: 98051
fetched_at: '2026-11-08T13:08:27+00:00'
kb_version: 1
---

# AI Tokenomics: The Economics of Tokens, Computation, and Pricing in Foundation Models

AI Tokenomics: The Economics of Tokens,
Computation, and Pricing in Foundation Models
Quanyan Zhu*
Abstract
Tokens have become the practical accounting unit for modern foundation model services,
linking information processing, computation, memory use, energy expenditure, pricing, and
economic value. This paper develops a framework for AI tokenomics: the study of how to-
kens are generated, consumed, priced, allocated, and optimized across AI systems. We con-
nect token-level technical costs to workflow-level production functions, enterprise resource
allocation, measurement and instrumentation methods, and emerging market-design ques-
tions. The framework shows that token expenditure and economic value are distinct: value
depends on marginal productivity, workflow position, hidden reasoning activity, risk, and
downstream propagation effects. The paper concludes by identifying open research direc-
tions in hidden-token measurement, empirical calibration, token productivity, dynamic allo-
cation, and token-based markets.
Keywords:AI tokenomics; foundation models; token pricing; workflow optimization; resource
allocation; AI economics.
1 Introduction
The rapid commercialization of foundation models has created a new economic unit for artifi-
cial intelligence: the token. In its original technical sense, a token is a discrete representation
used to process language and other data in transformer architectures [45, 37, 12]. In its emerg-
ing economic sense, however, the token has become the unit through which foundation-model
services meter, price, allocate, and govern computational intelligence. Every prompt, retrieval
operation, reasoning step, tool invocation, memory access, and generated response is ultimately
*Department of Electrical and Computer Engineering, New York University Tandon School of Engineering, 370 Jay
Street, Room 1004, Brooklyn, NY 11201, USA. Email: qz494@nyu.edu; phone: +1 646-997-3371.
1
arXiv:2606.24616v1  [cs.AI]  10 Jun 2026

converted into token consumption. Token usage therefore links information processing to com-
putation, latency, memory, energy expenditure, and monetary cost. This dual role is unusual:
the same object that determines how a model parses and generates information also determines
how users are charged and how organizations reason about capacity, utilization, and return on
investment.
This shift matters now because AI is moving from experimental deployment to large-scale
enterprise infrastructure. Recent industry analyses argue that AI is becoming one of the fastest-
growing categories of enterprise technology expenditure and that organizations must manage
this expenditure at the level of token consumption [27]. Unlike traditional software systems
whose costs are often governed by licenses, seats, or virtual machines, foundation-model de-
ployments exhibit volatile and nonlinear usage patterns. Token demand depends on prompt
complexity, context size, reasoning depth, retrieval design, tool use, workflow architecture,
and autonomous agent interactions. Small changes in a prompt, retrieval policy, or agentic
workflow can therefore create large changes in cost when repeated across many users, tasks,
or automated agents. As a result, conventional total-cost-of-ownership and cloud-accounting
frameworks are increasingly insufficient for managing AI systems at scale. An enterprise no
longer needs only to ask how many servers, licenses, or cloud instances it has purchased. It
must also ask how many tokens different business processes consume, which workflows pro-
duce value per token, where hidden reasoning or retrieval costs arise, and when a deployment
should shift across API, SaaS, or self-hosted infrastructure.
Token-based pricing reinforces this transformation. Historically, computational resources
such as processor cycles, memory, storage, and network bandwidth were measured and man-
aged through distinct accounting mechanisms. Contemporary foundation-model services in-
stead expose a unified economic interface in which heterogeneous computational resources are
abstracted into token usage. Whether an organization relies on proprietary APIs, self-hosted
models, retrieval-augmented generation (RAG), or autonomous AI agents, resource utilization
is increasingly expressed in tokens. The widespread adoption of token-based pricing by Ope-
nAI, Anthropic, Google, xAI, and other providers makes tokens a common accounting interface
for computational intelligence [33, 5, 20, 50].
1.1 From Token Accounting to AI Tokenomics
Current industry practice often treats this interface primarily as a problem of accounting, cost
management, infrastructure optimization, and Financial Operations (FinOps) for AI. FinOps
2

is a management practice concerned with making cloud and AI spending visible, accountable,
and controllable. In an AI setting, it helps organizations track token expenditures, forecast bud-
gets, assign costs to teams or applications, and reduce waste. These activities are necessary for
operational control, but they do not exhaust the economic questions created by tokenized AI
systems. Once tokens become the unit through which AI activity is measured, organizations
must also determine how tokens should be valued, allocated, priced, forecast, governed, and
optimized across complex AI ecosystems. This broader set of questions motivates the field that
we refer to asAI T okenomics. AI tokenomics studies the generation, consumption, pricing, val-
uation, allocation, optimization, and governance of tokens within AI ecosystems. Its central
premise is that tokens should not be viewed merely as artifacts of tokenization schemes such
as Byte Pair Encoding (BPE) or SentencePiece [41, 24]. Rather, they are economic resources that
mediate the relationship between computational effort, workflow performance, organizational
value, and market structure. In this sense, AI tokenomics begins where token accounting and
FinOps end. Accounting records token use after it occurs, and FinOps helps manage the re-
sulting expenditure. Tokenomics asks a broader design question: how should token use be
predicted, priced, constrained, and allocated before and during operation so that tokens gener-
ate value rather than merely cost? This requires studying the marginal productivity of tokens,
tradeoffs among models and workflows, demand created by users and agents, risk propagation
through workflow dependencies, and allocation rules for scarce computational capacity.
From this perspective, the increasing adoption of foundation models is transforming AI
from a purely computational technology into an economic system whose fundamental unit
of activity is the token. Tokens determine how computational resources are consumed, how
providers generate revenue, how organizations incur costs, how workflows allocate scarce re-
sources, and how value is created and distributed across AI ecosystems. They play a role anal-
ogous to energy in industrial systems or bandwidth in communication networks: they are a
resource through which productive capacity is generated, delivered, and consumed. Under-
standing the economics of this resource is therefore essential for the efficient design, operation,
and governance of large-scale AI systems.
1.2 Research Scope
Several structural features distinguish token economics from standard allocation problems.
First, token consumption exhibits strong nonlinearities. Empirical scaling-law studies show
that model performance depends systematically on model size, data volume, and computa-
3

tional expenditure [22, 21]. Additional context, retrieval, reasoning, or tool usage may improve
performance, but the associated gains often display diminishing returns. Second, token de-
mand is endogenous and adaptive: it depends not only on task characteristics but also on
prompt design, workflow structure, model behavior, and autonomous decision making. Third,
token consumption may contain hidden components associated with internal reasoning, chain-
of-thought computation, memory operations, and planning processes that are not directly ob-
servable to users. Fourth, token prices differ across providers, modalities, context windows,
caching regimes, and deployment models, creating heterogeneous economic landscapes for
similar tasks.
The complexity of token economics increases further in enterprise settings, where modern
AI systems rarely operate as isolated model calls. They are increasingly assembled as intercon-
nected workflows involving retrieval systems, reasoning modules, planning engines, monitor-
ing components, tool-using agents, and autonomous decision-support systems [53, 40]. Token
allocations made at one stage of a workflow can influence the quality, reliability, risk, and value
generated by downstream stages. Consequently, token allocation becomes a networked opti-
mization problem in which local decisions have system-wide effects. At the same time, token
markets raise questions about pricing, incentives, access, and governance as AI services be-
come more deeply embedded in organizational and economic life. The relevant unit of analysis
therefore changes with scale. At the task level, tokenomics concerns how difficulty, context, un-
certainty, and output requirements generate token demand. At the workflow level, it concerns
how tokens should be allocated across interdependent stages whose qualities complement or
substitute for one another. At the enterprise level, it concerns how token budgets should be
governed under uncertainty, risk, and organizational objectives. At the market level, it con-
cerns how token prices, contracts, and allocation mechanisms shape access to computational
intelligence.
These observations motivate several fundamental research questions. At the technical level,
how do tokens map to computation, memory, latency, and energy consumption? At the task
level, how do difficulty, context size, and uncertainty shape token demand? At the enterprise
level, how should organizations allocate finite token budgets across competing workflows, and
how should token productivity and economic value be measured? At the market level, what
determines token prices across providers and deployment environments, and what forms of
pricing mechanisms, allocation rules, and governance structures may emerge as AI systems
become increasingly token-centric?
4

This paper develops a framework for addressing these questions by integrating technical
foundations, economic analysis, enterprise resource allocation, measurement methodologies,
and market design into a unified theory of AI tokenomics. The analysis proceeds from token-
level technical costs to task-dependent token demand, provider pricing, workflow-level allo-
cation, instrumentation, and market design. Throughout, tokens are treated not merely as ac-
counting units but as allocable economic resources whose efficient use is fundamental to AI
systems.
1.3 Contributions
Existing work provides important but fragmented foundations for this problem. Tokenization
research explains how raw inputs are converted into discrete model inputs [41, 24]; scaling laws
relate model performance to data, parameters, and compute [22, 21]; provider documentation
and pricing pages describe how tokens are billed [33, 5, 20, 50]; and FinOps practice focuses on
tracking and controlling AI expenditure. These perspectives do not yet provide a unified theory
of tokens as economic resources. In particular, existing treatments often view tokens either as
linguistic units inside a model or as billing units on an invoice, but not as scarce computational
resources whose allocation determines workflow quality, enterprise value, risk exposure, and
market structure.
This paper addresses that gap in six ways. First, it formalizes AI tokenomics as the study
of how tokens are generated, consumed, priced, valued, allocated, optimized, and governed
within AI ecosystems. This definition moves beyond token accounting by treating tokens as
resources that can be assigned, substituted, conserved, and priced. Second, the paper devel-
ops a technical foundation that links token categories to computation, memory utilization,
hidden reasoning, energy consumption, and inference cost. Third, it introduces task-level
token-demand and token-production models in which difficulty, context size, and uncertainty
determine token requirements, thereby creating a basis for empirical calibration across het-
erogeneous workloads. Fourth, it analyzes contemporary provider pricing structures, instru-
mentation methods, and measurement challenges, including input-output price asymmetries,
caching, subscriptions, enterprise agreements, hidden reasoning tokens, and energy profiling.
Fifth, it develops a workflow-level allocation model in which interdependent AI workflows
form a network, workflow quality depends on token allocations, and optimal token use is char-
acterized through marginal productivity, shadow prices, downstream propagation, and risk-
aware allocation. Sixth, it extends the analysis to market and mechanism design by studying
5

dynamic pricing, tokenized compute assets, contract design, and multi-agent token economies.
Numerical case studies then illustrate how token expenditures, workflow quality, and eco-
nomic value interact in realistic AI deployments.
1.4 Organization of the Paper
Section 2 develops the technical anatomy of tokens and models task-level token consumption.
Section 3 examines token pricing, provider cost structures, instrumentation, and computational
profiling. Section 4 studies market-design questions for tokenized compute, multi-agent token
economies, and token-allocation mechanisms. Section 5 then develops one concrete mecha-
nism from that taxonomy: an enterprise-internal workflow allocation model with networked
resource allocation and risk-aware optimization. Section 6 presents case studies illustrating
how token expenditure, workflow quality, and economic value interact in practical settings.
Section 7 concludes with open research directions.
2 Technical Anatomy of Tokens and Task-Dependent Token
Consumption
This section provides the technical foundation for the tokenomic framework developed in the
rest of the paper. It first defines tokens as discrete computational objects produced by a tok-
enizer, then distinguishes the major categories of token usage that appear in deployed AI sys-
tems. The section then connects token counts to computation, energy, pricing, and task-level
demand, thereby establishing the notation and modeling assumptions used in the subsequent
economic and workflow analyses.
2.1 Tokens as Computational and Economic Units
Large Language Models (LLMs) operate on discrete units of information known astokens. A
token constitutes the fundamental unit through which textual, audio, image, or other forms of
data are represented and processed by modern foundation models. Beyond their linguistic role,
tokens have emerged as the primary unit of computation, accounting, and pricing in contem-
porary AI services. Consequently, understanding the anatomy of tokens is essential for both
the engineering analysis of large-scale AI systems and the development of a rigorous theory of
AI tokenomics.
6

Throughout the paper,R + = [0,∞),R ++ = (0,∞),Z ≥0 ={0, 1, 2, . . .}, andN={1, 2, . . .}.
Formally, letXdenote the raw input space and letVdenote the token vocabulary. For text
models,Xmay be taken as the set of finite strings over an alphabet; for multimodal models, it
may be enlarged to finite records containing text, image, audio, or tool-state fields. LetV ∗ =
S
n≥0 V n denote the set of finite token sequences. A tokenizer is a mappingτ:X → V ∗. For
x∈ X, writeτ(x) = (t1, . . . ,tn)witht i ∈ Vandn=|τ(x)| ∈Z ≥0. The precise decomposition
depends on the tokenization scheme employed, such as Byte Pair Encoding (BPE), WordPiece,
or SentencePiece [41, 24]. Modern foundation models rely on such tokenization procedures to
transform raw inputs into discrete representations suitable for transformer-based processing
[12].
In English text, one token typically corresponds to approximately three to four characters,
or roughly three-quarters of a word, although substantial variation exists across languages,
writing systems, and application domains. From the perspective of inference, tokens represent
the atomic objects upon which transformer architectures operate. Every attention computation,
memory access, and prediction step is ultimately conditioned on token representations. Conse-
quently, the total computational burden of an AI service is closely tied to the number of tokens
processed during execution.
Beyond their computational role, tokens have acquired economic significance. Commercial
AI platforms meter usage, allocate resources, and determine pricing primarily through token
counts. As a result, tokens simultaneously function as units of information representation,
computation, and economic exchange, forming the fundamental building blocks of modern AI
tokenomics.
2.2 Categories of Tokens
Although token accounting is often reported as a single aggregate quantity, multiple concep-
tually distinct categories of tokens exist within modern AI systems. Unless otherwise stated,
realized token counts belong toZ ≥0; in optimization problems below, these counts are relaxed
toR + to permit continuous marginal analysis. Input tokens, denoted byT I ∈Z ≥0, correspond
to user prompts, system instructions, and task-specific information supplied before inference
begins. Context tokens, denoted byT C ∈Z ≥0, represent conversational history or persistent
memory retained within the model’s context window. Retrieval-based systems introduce an
additional category of tokens, denoted byT R ∈Z ≥0, corresponding to external documents
incorporated through Retrieval-Augmented Generation (RAG) [26].
7

The model subsequently generates output tokens, denoted byT O ∈Z ≥0, which constitute
the visible response returned to the user. More subtly, advanced reasoning models frequently
generate intermediate computational traces associated with chain-of-thought reasoning and la-
tent deliberation processes [47, 46]. These hidden reasoning tokens, denoted byT H ∈Z ≥0,
are sometimes referred to asthinking tokensorinternal chain-of-thought tokens. Although typi-
cally inaccessible to users, they may contribute substantially to computational cost, memory
consumption, and energy expenditure.
The total token footprint associated with a task may therefore be expressed as
Ttot =T I +T C +T R +T O +T H. (2.1)
This decomposition highlights an important distinction between observable and unobservable
token expenditures. Whereas users generally observe only input and output tokens, infras-
tructure providers must provision resources for the entire quantityT tot. Consequently, token
accounting should be viewed as a system-level concept rather than merely a measure of visible
user interaction.
2.3 Tokens, Computation, and Resource Consumption
The economic significance of tokens derives from their close relationship with computational
complexity. Consider a transformer architecture containingLlayers and model widthm, where
L,m∈N[45]. Each token passing through the network undergoes repeated applications of
self-attention and feedforward transformations. Ignoring constant factors, the computational
burden of processing a sequence of lengthTscales approximately asO(Lm 2T). A more refined
analysis reveals that self-attention introduces an additional dependence on sequence length.
Since each token attends to all preceding tokens, attention operations scale approximately as
O(T 2)[45]. Consequently, extending context windows from 10 4 to 10 5 tokens can increase
computational requirements by orders of magnitude, motivating the development of sparse-
attention architectures, FlashAttention, and memory-efficient inference mechanisms [15].
The relationship between token count and computational effort may be summarized by
F(T)≈κLm 2T, (2.2)
whereF:R + →R + denotes the total number of floating-point operations (FLOPs) required
for inference andκ>0 is an architecture-dependent constant. Although simplified, this expres-
8

sion emphasizes that every additional token carries a measurable computational cost. This ob-
servation underlies contemporary scaling-law analyses, which reveal systematic relationships
among model size, data volume, computational expenditure, and downstream performance
[22, 21]. From this perspective, tokens represent a practical proxy for computational effort and
therefore provide a natural unit for economic accounting.
Tokens also determine memory utilization. During autoregressive inference, transformers
maintain a key-value (KV) cache storing intermediate representations associated with previ-
ously processed tokens. If the model containsLlayers and model widthm, the memory func-
tionM:R + →R + satisfiesM(T)∝LmTin the simplified linear approximation. This lin-
ear dependence on context length explains why long-context models require substantial GPU
memory resources and why context management has become a critical design challenge in
large-scale AI systems.
Because each token triggers computation and memory accesses, token processing is directly
associated with both energy consumption and latency. Let ¯e∈R + denote the average en-
ergy expenditure per token and let ¯ℓ∈R + denote the average latency per token. The model-
based energy-token mapping for a workload containingTtokens may then be approximated
byE tok(T) = ¯eT, while total latency is approximatelyℓ tot = ¯ℓT. These relationships motivate
metrics such asJoules per tokenandmilliseconds per token, which provide hardware-independent
measures of inference efficiency.
2.4 Tokens as Economic Objects
The emergence of commercial AI services has transformed tokens from purely technical enti-
ties into economic objects. Most providers charge separately for input and output tokens. If
pI,p O ∈R + denote the respective prices per token, the cost functionC:R 4 + →R + for a single
interaction may be represented asC=p I(TI +T C +T R) +pOTO. This pricing model reflects
the fact that generating output tokens generally requires more computation than processing in-
put tokens. More fundamentally, however, token-based pricing reveals a conceptual shift in the
role of tokens. Tokens are no longer merely units of information representation; they function
simultaneously as units of computation, resource allocation, and economic exchange. In this
sense, tokens play a role analogous to kilowatt-hours in electricity markets or packet counts
in communication networks. They provide a common currency through which computational
effort, infrastructure utilization, and economic value may be quantified. This dual technical-
economic character forms the foundation of AI tokenomics.
9

2.5 Task-Dependent Token Consumption
While the preceding discussion explains why tokens possess computational and economic sig-
nificance, it does not explain why different AI tasks consume dramatically different numbers
of tokens. Token consumption is not determined solely by prompt length. Rather, it emerges
from the interaction among task complexity, contextual requirements, and uncertainty in the
reasoning process. Prompt construction, context-window management, and per-call usage in-
strumentation therefore enter token demand directly [34, 6, 25].
From an economic perspective, token usage may be viewed as a derived demand for compu-
tational reasoning. Just as electricity demand depends on the activities performed by a factory,
token demand depends on the informational and computational requirements of the under-
lying task. A simple fact lookup or classification query may require only a few hundred to a
few thousand tokens, whereas long-document summarization may require 104–105 or more to-
kens. Code generation often has moderate input demand but large output demand, mathemat-
ical proof and planning tasks can consume substantial hidden reasoning tokens, and agentic
systems amplify usage through repeated model calls, tool invocations, verification loops, and
subtask decomposition [47, 46, 53, 40, 8].
LetJ={1, . . . ,J}, withJ∈N, denote a finite set of task classes. For eachj∈ J, let
bTj :Ω→Z ≥0 be the realized total token footprint of an execution of task classj, whereΩis the
underlying probability space capturing model stochasticity, prompt variation, retrieval varia-
tion, and tool-use paths. Define the task descriptorθ j = (dj,c j,u j)∈Θ=D × C × U, where
D,U ⊆R ++ are normalized dimensionless scales for task difficulty and uncertainty or cre-
ativity, respectively, andC ⊆R++ is a context-size domain measured in tokens or normalized
context units. The expected token-demand mappingf:Θ→R + is defined by
Tj =E[ bTj |d j,c j,u j] =f(d j,c j,u j), (2.3)
whereT j is the continuous relaxation of expected token demand for task classj.
The variabled j measures the computational complexity of the reasoning process, includ-
ing the number and difficulty of intermediate steps required to solve the task. The variablec j
captures the quantity of information that must be processed, including prompt text, retrieved
evidence, conversation history, and tool outputs. The variableu j represents uncertainty, am-
biguity, or creativity requirements, and therefore captures the breadth of the solution space
explored during inference. Two tasks with identical prompt lengths may therefore consume
10

vastly different numbers of tokens if they differ substantially in difficulty or uncertainty.
A useful parametric representation for positive descriptors isT j =ad α j cβ j uγ j , wherea∈R ++
andα,β,γ∈R ++. The exponentsα,β, andγare elasticities of token consumption with respect
to task difficulty, context size, and uncertainty. Precise calibration requires empirical logs of
token consumption across diverse tasks. As an illustrative approximation, context size often
enters nearly linearly, soβ≈1, whereas uncertainty or creativity may have a stronger and
potentially super-linear effect, such asγ>1.
Importantly, this task-level production function serves as the microeconomic foundation
for the workflow-level allocation models developed later in the paper. Whereas the present for-
mulation explains how task characteristics generate token demand, the enterprise tokenomics
framework subsequently examines how finite token budgets should be allocated across inter-
connected workflows to maximize organizational value.
2.6 Empirical Profiles of Token Demand
The heterogeneity of token consumption becomes evident when examining common AI work-
loads. The ranges in Table 1 are representative engineering profiles rather than universal con-
stants; they depend on model, tokenizer, context-window policy, retrieval depth, prompt de-
sign, and orchestration strategy. They are nevertheless useful for illustrating the orders-of-
magnitude differences across task classes and for motivating empirical token logging at the
application level [6, 25, 8].
Table 1: Representative token-consumption profiles across common AI workloads.
Task type Example Input/context Output Hidden/reasoning Drivers
Chat Q&A FAQ or classifica-
tion
50–1,000 50–1,000 Few Lowd j, lowc j, lowu j
Document sum-
marization
Multi-page sum-
mary
104–105+100–2,000 Moderate Moderated j and highc j
Code generation Function imple-
mentation
20–2,000 500–10,000 Moderate Moderated j and
variablec j
Math proof or
analysis
Theorem or prob-
lem solution
50–2,000 300–5,000 Very high Very highd j and highu j
Planning or RAG
workflow
Retrieval and plan-
ning
1,000–10,000 200–1,000 High Highd j, highc j, highu j
Multi-agent task Subtask orchestra-
tion
Varies across turns
and tools
Varies Compounded
across calls
Recursive
decomposition across
subtasks
Typical total token scales implied by these profiles range from roughly 200–2,000 tokens for
chatbot-sized simple queries, to 2,000–12,000 tokens for retrieval-augmented question answer-
ing, to 10,000–100,000+tokens for multi-page summarization. Agentic or multi-step workflows
can reach 15,000–1,000,000+tokens because each planning, retrieval, tool-use, and verification
step may induce another model call. Recent evidence on agentic coding tasks similarly finds
11

that agentic executions can be orders of magnitude more token intensive than ordinary code
chat or single-step reasoning [8].
Several observations emerge from Table 1. First, contextual information frequently dom-
inates token demand in enterprise applications. Second, reasoning-intensive tasks often con-
sume substantial numbers of hidden tokens that may not be directly observable to users. Third,
autonomous and multi-agent systems exhibit token consumption that grows through recursive
decomposition of tasks into subtasks, producing token expenditures several orders of magni-
tude larger than those associated with traditional chatbot interactions.
3 Token Pricing, Measurement, and Instrumentation
This section translates the technical accounting of tokens into the economic and operational
language used by AI providers and enterprise users. The main objective is to show how token
counts become prices, invoices, budgets, and measurement signals, while also identifying the
parts of inference cost that remain difficult to observe. The discussion begins with provider
pricing and then turns to subscription models, instrumentation, hidden reasoning, and energy
profiling.
3.1 Token Pricing as an Accounting Interface
The commercialization of foundation models has led to the widespread adoption of token-
based pricing as the dominant mechanism for allocating computational resources. Because
tokens serve as a direct proxy for inference workload, memory utilization, and infrastructure
consumption, they provide a natural basis for metering AI services. Nearly all major providers,
including OpenAI, Anthropic, Google, and xAI, price access to their models according to the
number of tokens processed during inference [33, 5, 20, 50].
From the provider’s perspective, token pricing offers several advantages. First, it aligns
revenue with resource consumption, thereby allowing costs to scale with demand. Second, to-
ken accounting provides a model-agnostic unit of measurement that remains applicable across
diverse architectures and applications. Third, it enables granular pricing structures that dis-
tinguish between different categories of computational workload, such as prompt processing,
response generation, caching, and long-context inference. Despite the apparent simplicity of
token-based billing, substantial variation exists across providers. Differences arise in input and
output token rates, treatment of cached tokens, handling of reasoning tokens, and support for
12

batch-processing discounts. These distinctions reflect both underlying differences in compu-
tational costs and strategic considerations regarding market positioning and customer acqui-
sition. Accordingly, a rigorous theory of AI tokenomics must treat pricing and measurement
together. Commercial AI platforms routinely report input and output token counts, yet many
aspects of token utilization remain opaque. In particular, hidden reasoning processes, internal
memory operations, and hardware-level resource consumption are typically inaccessible to end
users. Consequently, pricing is not merely a billing convention; it is also an observable interface
through which users infer otherwise hidden computational costs.
3.2 Provider Pricing Structures and Price Asymmetries
Table 2 gives a representative snapshot of token pricing and technical characteristics among ma-
jor foundation-model providers as of June 2026. The figures should be interpreted as illustrative
rather than permanent rates, since pricing evolves rapidly as model capabilities improve, con-
text windows expand, and providers introduce new service tiers [33, 5, 20, 50]. Official provider
pages remain the authoritative source for billing, while third-party dashboards provide a use-
ful cross-provider comparison layer for scenario analysis and models whose commercial terms
are distributed across platform-specific pages [10, 14, 16, 4, 54, 28, 29].
Several important patterns emerge from Table 2. First, output tokens are consistently priced
more expensively than input tokens, with ratios ranging from roughly 2 for some xAI and
DeepSeek offerings to roughly 6 or higher for several OpenAI, Google, and Qwen offerings.
Second, providers increasingly differentiate between standard and cached inputs [33, 5, 20, 50].
OpenAI reports discounted cached-input rates and batch-processing discounts; Anthropic re-
ports tiered cache-write and cache-hit prices; Google reports context-caching mechanisms; and
several open-weight or third-party API offerings either omit cached-input pricing or report it
through separate infrastructure layers. Third, pricing increasingly depends on service mode, in-
cluding batch processing, long-context thresholds, priority processing, tool use, data-residency
options, and whether the model is consumed through a hosted API or an open-weight deploy-
ment stack.
The most striking characteristic of contemporary AI pricing models is the systematic dis-
parity between input and output token costs. Letp I,p O ∈R + denote the prices of input and
output tokens, respectively, and assumep I >0 when forming price ratios. Across most com-
mercial offerings, the ratioρ=p O/p I typically exceeds unity and often lies between four and
six. This asymmetry arises because output generation requires repeated autoregressive decod-
13

Table 2: Representative pricing and technical characteristics of major foundation models (prices
in USD per million tokens; values are representative and subject to change).
Provider Model Context
Window
Input Output Cached
Input
Primary Strength
OpenAI GPT-5.5 1.1M $5.00 $30.00 $0.50 Frontier reasoning and
coding
OpenAI GPT-5.4 1.1M $2.50 $15.00 $0.25 General-purpose
reasoning
OpenAI GPT-5.4 Mini 1.1M $0.75 $4.50 $0.075 Agents and subagents
Anthropic Claude Opus
4.8
1.0M $5.00 $25.00 Tiered Highest-end reasoning
Anthropic Claude Sonnet
4.6
1.0M $3.00 $15.00 Tiered Coding and enterprise
agents
Anthropic Claude Haiku
4.5
1.0M $1.00 $5.00 Tiered Low-cost inference
Google Gemini 3.1 Pro
Preview
1.0M $2–$4 $12–$18 Context
caching
Long-context reasoning
Google Gemini 2.5
Flash
1.0M $0.30 $2.50 Context
caching
Cost-efficient hybrid
reasoning
xAI Grok-4.3 1.0M $1.25 $2.50 $0.20 Tool-oriented API
usage
DeepSeek DeepSeek-V4 1.0M $0.44 $0.87 – Low-cost frontier
model
Qwen Qwen 3.6 Max 262K $1.04 $6.24 – Multilingual
performance
GLM GLM-5.1 203K $0.98 $3.08 – Chinese-language
applications
Llama Llama 4 API
Offerings
Varies Varies Varies – Open-weight ecosystem
ing operations. While input tokens are processed largely in parallel during the initial forward
pass, output tokens are generated sequentially through repeated prediction and sampling steps
[45, 12]. Consequently, each additional output token imposes both computational and latency
costs that exceed those associated with an additional input token. From an economic perspec-
tive,ρmay be interpreted as a measure of the relative scarcity of generation capacity. Higher
values ofρencourage concise outputs and discourage unnecessarily verbose responses.
As context windows continue to expand, providers have also introduced specialized pricing
mechanisms for cached tokens. LetT cache ∈Z ≥0 denote the number of tokens stored in a
reusable cache. Rather than repeatedly charging the full input pricep I, providers often apply
a discounted ratep C ∈[0,p I)for cache retrieval operations [33, 5, 20]. This practice reflects
the observation that retrieving previously computed representations consumes significantly
fewer resources than reprocessing the same information from scratch. Economically, caching
transforms tokens from a pure flow resource into a partially reusable asset.
The API prices in Table 2 should also be distinguished from subscription and enterprise of-
ferings. Consumer and team products often bundle model access behind seat-based or monthly
14

plans, while enterprise contracts may combine seats, usage at API rates, spend controls, service-
level agreements, dedicated support, and platform-specific deployment features [7, 19]. Hence,
public per-token prices reveal only part of the economic contract: the effective price paid by
an organization also depends on volume commitments, latency requirements, governance con-
trols, data-residency constraints, and the degree to which agent platforms bundle orchestration
and monitoring into the service.
3.3 Subscription, Enterprise, and Hybrid Pricing
Although token pricing dominates API-based services, many providers also offer subscription-
based access. Under this model, users pay a fixed monthly fee in exchange for access to
a specified collection of models and usage limits. Examples include consumer-facing plans
such as ChatGPT Plus and premium offerings from competing providers. Subscription pricing
effectively pools token demand across users. Heavy users consume more computational re-
sources than their subscription fees directly cover, whereas light users subsidize excess capac-
ity through underutilization. From the provider’s perspective, subscriptions reduce revenue
volatility and simplify budgeting for customers. From the user’s perspective, subscriptions
replace uncertain token expenditures with predictable recurring costs. Enterprise agreements
frequently combine multiple pricing mechanisms. A typical contract may include seat licenses,
committed spending thresholds, discounted token rates, dedicated infrastructure, service-level
agreements, and reserved throughput guarantees. Such arrangements increasingly decouple
pricing from raw token counts and instead align billing with organizational value creation.
Current industry practice remains largely centered on token accounting. Nevertheless, several
trends suggest movement toward more sophisticated pricing structures. First, long-context
reasoning models increasingly differentiate between standard tokens and reasoning-intensive
computation. Second, agentic systems consume tokens across multiple interconnected model
calls, making direct token accounting less transparent [53, 40, 51]. Third, enterprise customers
increasingly evaluate AI services according to business outcomes rather than computational in-
puts. These developments suggest that token pricing may eventually coexist with mechanisms
based on tasks, outcomes, subscriptions, or hybrid arrangements.
3.4 Token-Level Instrumentation and Hidden Reasoning
The central objective of token instrumentation is to establish mappings between observed to-
ken usage and the underlying computational resources consumed during inference. Formally,
15

ifT∈R + denotes total token consumption, one seeks to estimate functionsg,h,k:R + →R +
such thatC(T) =g(T),E(T) =h(T), andF(T) =k(T), whereC(T)denotes monetary cost,
E(T)denotes the model-based energy consumption associated with a workload of sizeT, and
F(T)denotes computational effort measured in floating-point operations (FLOPs). Such map-
pings provide the foundation for connecting token accounting to resource allocation, pricing,
and economic value.
One of the most challenging aspects of AI tokenomics is the quantification of hidden rea-
soning tokens. Advanced reasoning models frequently perform intermediate computational
processes that are only partially exposed through observable outputs. Recent work on chain-
of-thought reasoning, self-consistency, latent reasoning trajectories, and model interpretability
suggests that substantial computational effort may occur through internal representations that
are not directly visible to users [47, 46, 9, 17].
LetT H ∈Z ≥0 denote the number of hidden reasoning tokens. The true token footprint
of a task follows Eq. (2.1), where only the first four quantities are typically observable. Sev-
eral approaches have been proposed for estimatingT H. One strategy compares token usage
under direct-answer prompting and explicit chain-of-thought prompting. Another approach
leverages interpretability tools such as the logit lens and tuned lens, which provide partial visi-
bility into intermediate representational states [32, 9]. More generally, hidden-token estimation
may be formulated as an inverse problem in which observable outputs are used to infer latent
computational activity.
3.5 Computational and Energy Profiling
Token counts alone provide only a partial characterization of resource consumption. Two
models may process the same number of tokens while consuming vastly different amounts
of computation. Consequently, instrumentation must also quantify the computational effort
associated with token processing. For a transformer containingLlayers and model width
m, inference cost scales approximately as in Eq. (2.2), whereκis an architecture-dependent
constant [45, 22, 21]. Modern profiling frameworks therefore combine analytical models with
GPU telemetry, performance counters, and energy monitors [15, 38]. GPU utilization, mem-
ory bandwidth, execution latency, and throughput can be monitored through tools such as
NVIDIA Management Library (NVML), Data Center GPU Manager (DCGM), and vendor-
specific telemetry interfaces.
The growing scale of AI workloads has elevated energy consumption to a central economic
16

and environmental concern [43, 49]. Let ¯e∈R + denote the average energy expenditure asso-
ciated with processing a single token. The token-based energy approximation for a workload
containingT∈R + tokens isE tok(T) = ¯eT. This relationship motivates a useful performance
metric: energy per token. Measured in Joules per token, this quantity provides a hardware-
independent indicator of inference efficiency and facilitates comparisons across model archi-
tectures and deployment environments [43, 49].
Ifτ>0 is the inference duration andP:[0,τ]→R + denotes integrable instantaneous
power consumption, the realized energy consumed during the inference session is
Esess =
Z τ
0
P(s)ds.
The quantityE tok(T)is therefore a token-based energy model, whereasE sess is a realized phys-
ical measurement. DividingE sess by the number of processed tokens yields an empirical esti-
mate of energy efficiency that can be compared across hardware platforms, model families, and
operational settings.
4 Market and Mechanism Design
The preceding pricing discussion treats token prices mainly as provider-set accounting rules.
This section broadens the perspective from bilateral provider-user pricing to market and mech-
anism design. Once tokens are viewed as scarce units of computational reasoning capacity,
questions of allocation, congestion, incentives, governance, and strategic interaction naturally
arise.
4.1 Token Markets and Allocation Mechanisms
The preceding sections established that tokens function simultaneously as units of information,
computation, and pricing. From an economic perspective, this suggests that tokens may be
treated as scarce resources subject to allocation mechanisms. The study of token markets there-
fore naturally intersects with mechanism design, auction theory, cloud-resource allocation, and
algorithmic game theory [30, 31]. In this setting, a mechanism is not limited to an auction. More
broadly, it is a rule that maps information about demand, supply, priorities, or workflow needs
into token allocations, payments, access rights, or service guarantees. This broader interpreta-
tion is important because AI token allocation appears at several layers: provider-user pricing,
17

cloud-capacity allocation, enterprise budget assignment, agent-to-agent delegation, and inter-
nal workflow optimization.
Formally, considerN∈Nusers or organizational units indexed byI={1, . . . ,N}. Let
Ri denote the report or bid space of participanti, letR= ∏i∈I Ri, and letF N( ¯T) ={a∈
RN + : ∑i∈I ai ≤ ¯T}denote the feasible set of aggregate token allocations. A token-allocation
mechanism may be represented by an allocation ruleX:R → F N( ¯T)and, when monetary
transfers are present, a payment ruleY:R →R N +. The design objective may be welfare
maximization, cost recovery, incentive compatibility, fairness, robustness, or a combination of
these criteria. Fixed posted prices, congestion prices, auctions, enterprise contracts, and inter-
nal budget-allocation rules can therefore be interpreted as different mechanisms for governing
scarce token capacity.
Let ¯T∈R + denote the aggregate supply of computational tokens available within a plat-
form. Users compete for access to these resources, generating a market-demand functionDmkt :
R+ →R +, whereπ∈R + denotes the scalar token price andD mkt(π)denotes aggregate de-
mand at that price. The resulting allocation problem resembles classical resource-allocation
problems in communication networks, cloud computing, and electricity markets.
Most current AI services employ fixed token prices. However, fixed pricing may be inef-
ficient when demand fluctuates substantially over time. LetH>0 denote a pricing horizon.
LetD H,S H :[0,H]→R + denote time-dependent demand and supply withS H(t)>0, and
letπ H :[0,H]→R + denote the time-dependent token price. A simple congestion-pricing rule
may be expressed as
πH(t) =π0 +χ
 DH(t)
SH(t)

,
whereπ 0 ∈R + is a base price andχ≥0 is a congestion sensitivity parameter. Such pricing
mechanisms increase token prices during periods of high congestion and decrease prices when
resources are underutilized, encouraging more efficient allocation of computational capacity
[23, 18].
Auction mechanisms provide another allocation approach. In an auction specialization,
participanti∈ Ireceives allocationT i ∈R + and derives utilityU i(Ti), whereU i :R + →R
is nondecreasing and concave. The platform seeks an allocation maximizing aggregate wel-
fare, max{Ti} ∑i∈I Ui(Ti)subject to ∑i∈I Ti ≤ ¯T. Auction-based mechanisms provide a princi-
pled approach for allocating scarce computational resources while revealing users’ willingness
to pay [30, 31]. The auction formulation is most natural for external markets with strategic
18

participants. In contrast, an enterprise may use an internal allocation mechanism in which
workflows do not bid in a market but are assigned tokens according to measured productiv-
ity, dependency structure, risk, and business priority. Section 5 develops precisely this internal
workflow-allocation mechanism. It specializes the general mechanism-design view above to
a planner-mediated setting in which the allocation rule maps a workflow graph, production
functions, a finite budget, and a risk functional into a feasible token-allocation vector.
4.2 Tokenized Compute and Multi-Agent Economies
Recent developments in decentralized infrastructure and distributed computing have proposed
treating computational capacity itself as a tradable asset [36, 2]. Under this paradigm, own-
ership rights to GPUs, compute clusters, storage resources, or future inference capacity may
be represented through digital tokens. Such proposals illustrate a broader trend toward the
financialization of computational resources and the emergence of secondary markets for AI
infrastructure. If successful, these systems may improve utilization, liquidity, and access to
computational resources while introducing new questions regarding regulation, governance,
and market stability.
The emergence of autonomous AI agents introduces a second layer of economic interaction
[53, 40, 35, 13, 52]. The notion of computational agents exchanging scarce resources has long
been studied in distributed artificial intelligence and computational economics [48, 42, 60]. Let
n∈Nand letA={A 1, . . . ,An}denote a finite collection of agents. AgentA i may allocate
tokens to agentA j in exchange for performing a subtask. Such interactions create internal token
economies governed by incentive mechanisms, budget constraints, and strategic behavior. As
agentic AI systems become increasingly autonomous, tokens may evolve from a billing unit
into an internal computational currency that coordinates distributed reasoning and resource
allocation.
4.3 Governance and Open Market-Design Questions
As token markets evolve, governance and regulatory concerns become increasingly impor-
tant. Token-based allocation mechanisms may inadvertently create barriers to access, favor
wealthier participants, or concentrate computational resources among a small number of ac-
tors. Questions of fairness and access closely parallel earlier concerns in communication net-
works, cloud computing, and platform economics [23, 18, 1, 55, 59]. Consequently, future AI
marketplaces must balance efficiency with broader societal objectives, including transparency,
19

accessibility, competition, and equitable access to computational resources. The convergence
of AI services, cloud computing, and digital markets suggests the emergence of a new class
of economic systems in which tokens represent computational resources. Understanding these
systems requires integrating insights from computer science, economics, operations research,
mechanism design, and game theory. Cyber-resilience and socio-technical-control perspectives
further emphasize that market rules must account for adversarial behavior, bounded rational-
ity, and feedback between human organizations and AI infrastructure [55, 59, 56, 3, 58].
The study of token markets therefore intersects naturally with algorithmic game theory,
mechanism design, cloud-resource allocation, and digital platform economics [30, 31, 39]. Fu-
ture research must address questions concerning equilibrium token prices, optimal allocation
mechanisms, dynamic market design, incentive compatibility, and the interaction between
computational scarcity and economic value. Such questions constitute the foundation of a
broader theory of AI token markets and provide a natural extension of the emerging field of AI
tokenomics.
The next section moves from this market-level perspective to the enterprise workflow level.
Rather than introducing a separate topic, it studies one concrete mechanism in the taxonomy
above: an internal resource-allocation rule for assigning a finite token budget across interde-
pendent AI workflows.
5 Workflow Tokenomics and Resource Allocation
This section develops the workflow-level allocation model that connects task-dependent token
demand to enterprise value. Whereas the previous sections focused on token definitions, mea-
surement, and pricing, the analysis below treats tokens as controllable resources that must be
distributed across interdependent AI workflows under an exogenous budget or capacity limit.
In this sense, the total amount of available computation is not the object being priced; it is the
constraint under which the system must operate. The fundamental planning question is how
a finite token budget should be assigned across workflow components when quality, marginal
productivity, downstream propagation, and risk all depend on the allocation.
Following the mechanism-design perspective in Section 4, the model below can be inter-
preted as a concrete enterprise-internal allocation mechanism: a rule that maps workflow de-
pendencies, token-productivity functions, budget constraints, and risk exposure into a feasible
allocation of tokens. This viewpoint is consistent with recent work on agentic AI workflows in
20

cyber deception, where planning, monitoring, deception design, and defensive response form
coupled stages rather than isolated model calls [3, 58]. The problem is fundamental because
every deployed AI system faces some binding resource envelope, whether expressed as API
spending, latency, energy, throughput, memory, or context-window capacity. Once that enve-
lope is fixed, each token allocated to one workflow stage creates an opportunity cost for the
others, and the best allocation cannot be inferred from task-level token counts alone.
5.1 From Token Demand to Fixed-Budget Workflow Allocation
The preceding sections established that tokens constitute the fundamental resource through
which modern AI systems consume computation, memory, energy, and monetary expenditure.
At the task level, token demand was modeled by the token-demand function in Eq. (2.3). This
relationship explains how computational requirements emerge from task characteristics and
why token consumption varies substantially across applications.
Section 4 then situated token allocation within the broader language of mechanisms, includ-
ing pricing rules, auctions, contracts, agent-to-agent exchange, and internal allocation rules.
The present section focuses on the last of these mechanisms. It studies a single organization or
platform that controls a finite token budget and must allocate it across interdependent work-
flows without relying on an external market-clearing process. Put differently, pricing and con-
tracts help determine how token capacity is charged, procured, or shared across agents; after a
budget has been set, the operator still faces the internal workflow-allocation problem studied
here.
While the task-level perspective provides insight into the determinants of token demand,
many practical AI deployments consist of collections of interconnected workflows operating
under common computational and economic constraints. Examples include RAG, staged rea-
soning, coding, research support, cybersecurity, cyber deception, planning, and decision sup-
port [3, 56, 58]. In such environments, the central challenge is no longer determining how many
tokens a single task requires, but rather how a given token budget should be allocated across
multiple workflows to maximize overall system performance and value. This allocation prob-
lem is a primitive of AI tokenomics: it appears before one can evaluate return on token spend-
ing, compare competing workflow designs, or decide whether additional capacity is worth
purchasing. The cyber-deception examples are particularly instructive because the value of an
agentic workflow depends on how sensing, hypothesis generation, deception selection, adver-
sary modeling, and response planning reinforce one another [3, 58]. This observation motivates
21

a workflow-level theory of token allocation. The resulting problem is closely related to classi-
cal resource-allocation, network optimization, workflow scheduling, and utility-maximization
problems studied in economics, operations research, communication networks, and cloud com-
puting [23, 11, 44, 18, 59, 60, 52]. The distinguishing feature is that the scarce resource is com-
putational reasoning capacity measured in tokens. Conceptually, workflow tokenomics occu-
pies the intermediate layer between task-level token demand and system-level value creation:
task characteristics determine token demand, token allocations generate workflow quality, and
workflow quality determines system utility.
5.2 Workflow Graph Representation
LetW∈Ndenote the number of workflows and letW={1, . . . ,W}denote the finite work-
flow index set. Eachw∈ Wmay represent a retrieval process, a reasoning stage, a planning
module, a verification process, a monitoring function, or any other structured computational
activity. Dependencies among workflows are represented by a directed graphG= (W,E)with
E⊆ W × W. An edge(j,w)∈Eindicates that the output produced by workflowjserves as
an input to workfloww. For each workfloww, define Pa(w) ={j:(j,w)∈E}as the set of
upstream workflows and Ch(w) ={k:(w,k)∈E}as the set of downstream workflows. The
graph representation captures a broad range of workflow structures. For example, a retrieval
workflow may provide contextual information to a reasoning workflow, whose output is sub-
sequently passed to a planning workflow and then to an execution or monitoring workflow.
In agentic cyber-deception workflows, a similar graph can encode how monitoring, attack in-
ference, deception generation, and defensive control depend on one another, as in the gestalt
game-theoretic workflow models of [3, 58]. For analytical tractability, we initially assume thatG
is a directed acyclic graph with no self-loops. This assumption permits workflows to be evalu-
ated in topological order and is consistent with many practical AI pipelines. Feedback systems
may be represented through temporal unfolding over a finite horizon, thereby producing an
equivalent acyclic workflow graph.
5.3 Token Allocation and Workflow Quality
Each workflow receives a token allocationT w ∈R +. Consistent with the token taxonomy
in Eq. (2.1), this allocation may be decomposed asT w =T I w +T C w +T R w +T O w +T H w , where
T I w,T C w,T R w ,T O w , andT H w denote input, context, retrieval, output, and hidden reasoning to-
kens, respectively. The aggregate token-allocation vector isT= (T 1, . . . ,TW )∈R W + . Suppose
22

that the system operates under a finite token budgetB∈R ++. The feasible allocation set is
F(B) ={T∈R W + : ∑w∈W Tw ≤B}. This budget may represent an API expenditure limit,
a computational capacity constraint, a latency budget, an energy budget, or a combination of
these considerations. Associated with each workflow is a quality spaceQ w ⊆R +. The qual-
ity variableq w ∈ Qw may represent predictive accuracy, reliability, robustness, information
quality, task-completion probability, or expected operational effectiveness. LetQ= ∏w∈W Qw
denote the system quality space.
Workflow quality is modeled through a production functionϕ w :R + × ∏j∈Pa(w) Qj → Qw:
qw =ϕ w

Tw,{q j}j∈Pa(w)

. (5.1)
This formulation generalizes classical production functions from economics to workflow-based
AI systems. The token allocation serves as a computational input, while upstream workflow
qualities influence downstream performance. Empirical evidence from scaling laws, retrieval-
augmented generation, and reasoning models suggests several regularities. First, workflow
quality typically improves as token allocation increases [22, 21]. Second, marginal gains gen-
erally diminish as token expenditure increases. Third, downstream workflow quality depends
critically on the quality of upstream information sources [26]. Consequently, in the continu-
ous relaxation we assume thatϕ w is continuously differentiable, nondecreasing and concave in
Tw, and nondecreasing in each upstream quality argument. If Pa(w) =∅, the product over
upstream quality spaces is interpreted as a singleton.
A representative specification is
qw =

1−e −β w Tw

gw

{qj}j∈Pa(w)

, (5.2)
whereβ w >0 measures token efficiency andg w : ∏j∈Pa(w) Qj →R + is a nonnegative aggrega-
tion function for upstream workflow influence.
BecauseGis acyclic, Eq. (5.1) defines a unique quality vectorq(T) = (q 1(T), . . . ,qW (T))∈
Qrecursively in topological order for eachT∈ F(B). Thus the workflow network induces a
nonlinear mappingq:F(B)→ Q. Because workflow qualities are coupled through the graph
structure, this mapping is generally nonseparable. Consequently, the value of tokens allocated
to a workflow cannot be assessed solely through local performance improvements.
23

5.4 System Utility and Network Token Productivity
The objective of token allocation is to maximize the value generated by the workflow system.
LetU:Q →Rbe a continuously differentiable system-utility function. The induced value of a
token allocation is
V(T) =U

q(T)

(5.3)
forT∈ F(B).
A useful benchmark specification isV(T) = ∑w∈W bwqw(T), whereb w >0 measures the
relative importance of workfloww.
Unlike conventional token accounting, the utility in Eq. (5.3) depends on workflow inter-
actions. The value of a token allocated to workflowwdepends not only on local quality im-
provements but also on the influence of workflowwon downstream workflows throughout the
network.
Following the network-utility literature [23, 11], define the adjoint value variable recursively
in reverse topological order by
µw = ∂U ∂qw + ∑ k∈Ch(w) µk ∂qk ∂qw . (5.4)
The quantityµ w measures the total marginal value generated by an incremental improvement
in workfloww, including both direct and indirect downstream effects.
Applying the chain rule yields
∂V
∂Tw
=µ w
∂ϕw
∂Tw
. (5.5)
This quantity represents the marginal productivity of tokens allocated to workfloww.
The expression generalizes the earlier task-level productivity measureη=U/Tby incorpo-
rating workflow position and dependency structure. Two workflows receiving identical token
allocations may therefore exhibit substantially different marginal values depending upon their
locations within the workflow graph.
5.5 Risk-Aware Workflow Allocation
The preceding formulation assumes that workflow quality and system value are deterministic
functions of token allocations. In practice, however, AI workflows operate under substantial
24

uncertainty. Retrieval modules may fail to recover relevant information, reasoning quality may
vary across model executions, tool invocations may be unreliable, and autonomous agents may
propagate errors throughout downstream workflows. Furthermore, failures in AI-enabled sys-
tems may generate operational losses, cybersecurity incidents, regulatory penalties, or legal
liabilities [57].
Consequently, token allocation influences not only expected utility but also the uncertainty,
fragility, resilience, and liability exposure of the workflow network. Two token allocations may
generate identical expected value while exhibiting substantially different operational risk pro-
files. For example, excessive concentration of tokens in a small number of workflows may cre-
ate infrastructure bottlenecks, increase congestion in shared computational resources, amplify
error propagation, and reduce overall system resilience.
Let(Ω,G,P)be a probability space. Its outcomes represent stochastic inference, retrieval
variability, adversarial inputs, model misspecification, and tool uncertainty. For eachw∈ W,
let eϕw be a measurable stochastic production mapping with domain equal to the product of the
token spaceR +, the upstream quality space∏j∈Pa(w) Qj, and the uncertainty spaceΩ, and with
codomainQ w. For anyT∈ F(B)andω∈Ω, the realized quality vector eq(T,ω)∈ Qis defined
recursively by applying eϕw toT w, the upstream realized qualities, andω. When the expectation
exists, the deterministic quality used in the preceding subsections can be interpreted asqw(T) =
E[eqw(T,ω)].
LetO ⊆R W be an open set containingF(B). A risk functional is a differentiable map-
pingΦ:O →R + that assigns each feasible token-allocation vectorT= (T 1, . . . ,TW )a non-
negative measure of uncertainty, congestion, fragility, and liability exposure. The formulation
isrisk-awarebecause the planner maximizes the risk-adjusted objectiveV(T)−ζΦ(T)rather
than workflow value alone. Hereζ≥0 is a risk-awareness parameter:ζ=0 gives a purely
value-maximizing allocation, whereas larger values ofζplace greater weight on robustness,
resilience, and liability mitigation.
Four sources of risk are particularly relevant in workflow tokenomics. First, even un-
der fixed token allocations, workflow outcomes may vary because of stochastic model be-
havior, imperfect retrieval, environmental uncertainty, or adversarial manipulation. Letσ 2 w :
R+ →R + denote a differentiable local variance penalty for workfloww, for exampleσ 2 w(Tw) =
Var[eϕw(Tw,{q j(T)} j∈Pa(w) ,ω)]. Additional tokens devoted to retrieval, verification, monitor-
ing, or reasoning may reduce this term and improve robustness. Second, AI workflows com-
pete for common resources such as GPU memory, inference throughput, API quotas, context-
25

window capacity, storage, and latency budgets. LetRbe a finite set of shared resource classes,
leta r w ≥0 be the load placed on resource classrper token allocated to workfloww, and de-
fine the aggregate load asx r(T) = ∑w∈W ar wTw. Congestion is represented by differentiable,
nondecreasing functionsψ r :R + →R +. Third, workflow networks create interdependen-
cies through which upstream errors may propagate downstream. For each edge(j,w)∈E, let
Σj(T) =Var[ eqj(T,ω)]and letκ jw ≥0 weight the propagation risk along that edge. The sensi-
tivity∂q w/∂q j, evaluated at the baseline quality vectorq(T), measures how strongly workflow
wdepends on the quality of workflowj. Fourth, in safety-critical and enterprise environments,
workflow failures may generate economic losses through cybersecurity incidents, erroneous
legal recommendations, operational disruptions, regulatory violations, or unsafe autonomous
decisions. LetΛ:O →R + be a differentiable expected-liability mapping.
Combining these effects yields the representative risk functional
Φ(T) = ∑
w∈W
σ2 w(Tw) +∑
r∈R
ψr

xr(T)

+ ∑
(j,w)∈E
κjwΣj(T)

∂qw
∂qj
!2
+Λ(T)(5.6)
forT∈ F(B). The first term captures local workflow-quality uncertainty, the second shared-
resource congestion, the third dependency-driven error propagation, and the fourth liability
exposure. Other specifications ofΦare possible; Eq. (5.6) is intended as a tractable model that
makes the main risk channels explicit.
The workflow-allocation problem becomes
max
T∈F(B)
{V(T)−ζΦ(T) } . (5.7)
This is a risk-aware, rather than risk-neutral, optimization problem. Allocations depend on
both marginal value and marginal exposure to uncertainty, congestion, propagation, and liabil-
ity risk.
5.6 Optimality Conditions and Economic Interpretation
The Lagrangian associated with problem (5.7) is
L=V(T)−ζΦ(T) +λ

B− ∑
w∈W
Tw
!
.
At an interior optimum, the first-order conditions imply
26

∂V
∂Tw
−ζ ∂Φ ∂Tw =λ,w∈ W. (5.8)
Substituting Eq. (5.5) into Eq. (5.8) yields
µw
∂ϕw
∂Tw
−ζ ∂Φ ∂Tw =λ. (5.9)
Equation (5.9) equates the risk-adjusted marginal productivity of tokens across workflows.
The first term,µ w ∂ϕw ∂Tw , measures the incremental value generated by allocating an additional
token to workfloww, including both direct and downstream effects. The second term,ζ ∂Φ ∂Tw ,
measures the incremental uncertainty, congestion, fragility, and liability introduced by that al-
location.
The multiplierλrepresents the shadow value of an additional token and therefore quantifies
the marginal value of computational reasoning capacity under the prevailing risk preferences
of the organization. Workflows whose risk-adjusted marginal productivity exceedsλshould
receive additional tokens, whereas workflows whose risk-adjusted contribution falls belowλ
should receive fewer resources.
This result extends AI tokenomics beyond cost accounting and pricing. Tokens become
allocable computational assets whose value depends not only on their contribution to work-
flow quality, but also on their influence on uncertainty, resilience, and systemic risk. As AI
workflows become increasingly autonomous, interconnected, and safety-critical, optimal token
allocation requires balancing productivity against robustness throughout the entire workflow
ecosystem.
6 Case Studies: Workflow Tokenomics in Practice
The preceding sections developed a theory of workflow tokenomics in which tokens serve si-
multaneously as units of information representation, computation, memory consumption, en-
ergy expenditure, and economic allocation. At the task level, token demand follows Eq. (2.3);
at the workflow level, token allocations are represented byT= (T 1, . . . ,TW )and linked to
workflow quality through Eq. (5.1). This section provides numerical case studies showing
how token expenditures, workflow quality, marginal productivity, and economic value in-
teract. Throughout the case studies, the token cost of a workflow is approximated byC=
pI(T I +T C +T R) +pOTO +p H TH, wherep I,p O,p H ∈R + denote the effective prices of input,
27

Figure 1: Representative workflow structures for the Section 6 case studies. From left to right,
the panels show legal contract analysis, software engineering, retrieval-augmented research,
and autonomous multi-agent workflows; the labelsw 1, . . . ,wW identify the workflow stages
used in the allocation calculations.
output, and hidden reasoning tokens. When hidden reasoning tokens are not separately priced,
one may setp H =p O or interpretp H as the provider’s internal marginal inference cost. For
illustration, supposep I =$2/10 6,p O =$10/10 6, andp H =$10/10 6. These values are not
intended as fixed market prices; they provide a common numerical basis for comparing token
allocation across workflows. Figure 1 summarizes the four workflow templates used in the case
studies and highlights the stage-level variablesw1, . . . ,wW that later enter the allocation model.
6.1 Case Study I: Legal Contract Analysis
Corresponding to the first panel of Figure 1, consider a legal-analysis workflow with three
stages: document ingestion (w 1), legal reasoning (w 2), and executive summary (w 3). Sup-
pose the portfolio contains ten contracts, each averaging 50 pages, and that one page corre-
sponds to approximately 200 tokens. Document ingestion therefore requires 10×50×200=
100,000 input tokens, soT I w1 =100,000. The reasoning stage performs clause extraction, obli-
gation analysis, risk identification, compliance checking, and cross-document comparison. If
hidden reasoning consumes between 50% and 150% of the ingested document length, then
TH w2 ∈[50,000, 150,000]. The final executive summary and risk report requireT O w3 =1,000, so
Ttot =100,000+ [50,000, 150,000] +1,000∈[151,000, 251,000]. Using the illustrative prices,
the corresponding cost is computed from input, hidden reasoning, and output charges, giving
Cmin =$0.71 andC max =$1.71. Thus, even though visible output is only 1,000 tokens, most
cost arises from hidden reasoning, which accounts for approximately 33.1% to 59.8% of the total
footprint. Let workflow quality be modeled byq w(Tw) =1−exp(−β wTw). With(β 1,β 2,β 3) =
28

(2×10 −5, 1.5×10 −5, 10−3)and baseline allocation(T 1,T 2,T 3) = (100,000, 100,000, 1,000), the
qualities are(q 1,q 2,q 3) = (0.865, 0.777, 0.632). For utilityV=0.1q 1 +0.7q 2 +0.2q 3, this gives
V=0.7568.
The marginal quality gain from an additional token isdq w/dTw =β we−β w Tw. Under the
baseline allocation, the marginal utilities are 2.71×10 −7 for ingestion, 2.34×10 −6 for reason-
ing, and 7.36×10 −5 for the summary. The high marginal value of summary tokens reflects
the small baseline allocation to the summary stage. However, once the executive summary
reaches a sufficient length, additional summarization tokens saturate rapidly. The reasoning
stage remains economically important because its quality receives the largest utility weight
and propagates downstream into the final legal recommendation.
6.2 Case Study II: Software Engineering Workflow
The second panel of Figure 1 represents the software-engineering workflow. It has five stages:
specification (w 1), code generation (w 2), verification (w 3), testing (w 4), and repair (w 5). Sup-
poseT I w1 =500 andT O w2 =5,000, while verification, testing, and repair consume hidden
reasoning tokens satisfyingT H w3 +T H w4 +T H w5 ∈[20,000, 100,000]. ThenT tot =500+5,000+
[20,000, 100,000]∈[25,500, 105,500]. Using the illustrative prices,C min =0.001+0.05+0.20=
$0.251 andC max =0.001+0.05+1.00=$1.051. Assume a baseline allocation(T 2,T 3,T 4,T 5) =
(5,000, 25,000, 25,000, 10,000)andq w(Tw) =1−e −β w Tw withβ 2 =2×10 −4,β 3 =β 4 =8×10 −5,
andβ 5 =10 −4. The resulting stage qualities areq 2 =0.632,q 3 =0.865,q 4 =0.865, and
q5 =0.632. WithV=0.15q 2 +0.35q 3 +0.35q 4 +0.15q 5, the baseline utility isV=0.795.
Now compare two allocations with the same total token budget of 65,000 tokens. Allocation
A assigns 15,000 tokens each to code generation, verification, and testing, and 20,000 tokens
to repair; it produces(q 2,q 3,q 4,q 5) = (0.950, 0.699, 0.699, 0.865)andVA =0.761. Allocation B
assigns 5,000 tokens to code generation, 25,000 each to verification and testing, and 10,000 to
repair; it produces(q 2,q 3,q 4,q 5) = (0.632, 0.865, 0.865, 0.632)andVB =0.795. Although Allo-
cation A devotes more tokens to code generation and repair, Allocation B yields higher utility
because verification and testing receive larger weights:V B − VA =0.034, a relative improve-
ment of 0.034/0.761≈4.47%. This illustrates a key workflow-tokenomics point: allocating
tokens to the largest or most visible stage is not necessarily optimal. Verification and testing
may dominate marginal productivity because failures propagate downstream into debugging,
deployment delay, security risk, and user harm.
29

6.3 Case Study III: Retrieval-Augmented Research Workflow
The third panel of Figure 1 illustrates a retrieval-augmented research workflow with retrieval
(w1), reasoning (w 2), synthesis (w 3), and recommendation (w 4). Suppose the user query con-
tainsT I =500 tokens, the retrieval stage accesses fifty documents of 1,000 tokens each so
thatT R =50,000, the final synthesis and recommendation stages produceT O =2,000 out-
put tokens, and hidden reasoning consumesT H ∈[20,000, 80,000]. ThereforeT tot =500+
50,000+2,000+ [20,000, 80,000]∈[72,500, 132,500]. The corresponding cost range isC min =
0.101+0.020+0.200=$0.321 toC max =0.101+0.020+0.800=$0.921.
Suppose retrieval quality followsq R(TR) =1−e −β R TR withβ R =8×10 −5. AtT R =
50,000,q R =1−e −4 =0.982 and∂q R/∂TR =8×10 −5e−4 =1.47×10 −6. Suppose rea-
soning quality followsq H(TH) =1−e −β H TH withβ H =3×10 −5. AtT H =40,000,q H =
1−e −1.2 =0.699 and∂q H/∂TH =3×10 −5e−1.2 =9.04×10 −6. Thus, at these allocation levels,
(∂q H/∂TH)/(∂q R/∂TR) = (9.04×10−6)/(1.47×10 −6)≈6.15. An additional reasoning token
produces over six times the marginal quality gain of an additional retrieval token. This calcula-
tion formalizes the diminishing-returns claim: once retrieval has already accessed a sufficiently
large and relevant corpus, marginal value shifts toward reasoning, synthesis, and judgment.
6.4 Case Study IV: Autonomous Multi-Agent Workflow
The fourth panel of Figure 1 depicts an autonomous multi-agent workflow consisting of a plan-
ner, retriever, executor, monitor, and replanner. Suppose one planning cycle requiresT P =
10,000,T R =50,000,T E =100,000,T M =20,000, andT RP =30,000. The total token expen-
diture isT tot =210,000, with sharess P =4.76%,s R =23.81%,s E =47.62%,s M =9.52%,
ands RP =14.29%. Although execution consumes the largest token share, it need not have
the largest marginal value. To see this, suppose system utility depends on the final replan-
ning qualityq RP, and each stage propagates quality multiplicatively so thatq RP =q PqRqEqM.
The marginal contribution of planning is∂q RP/∂q P =q RqEqM, while the marginal contri-
bution of execution is∂q RP/∂q E =q PqRqM. If(q P,q R,q E,q M) = (0.70, 0.90, 0.85, 0.80), then
∂qRP/∂q P =0.90(0.85)(0.80) =0.612, whereas∂q RP/∂q E =0.70(0.90)(0.80) =0.504. Thus, an
improvement in planning quality has a larger downstream effect than an equivalent improve-
ment in execution quality: 0.612/0.504=1.214. Planning has approximately 21.4% greater
downstream marginal impact despite using only 4.76% of the tokens. This example demon-
strates why adjoint values matter. The value of a workflow is not determined only by the
number of tokens it consumes; it is determined by its position in the dependency graph and
30

the extent to which quality improvements propagate downstream.
6.5 Comparative Lessons
The four case studies, visualized in Figure 1, demonstrate that token expenditure, marginal
value, and economic utility can diverge substantially. The totals in Table 3 are computed di-
rectly from the scenario assumptions stated above; they are intended as internally consistent
workload calculations rather than provider-specific empirical averages.
Table 3: Expanded workflow tokenomics comparison.
Application Typical Tokens Largest Token
Component
Dominant
Marginal-Value
Component
Main Allocation
Lesson
Legal Analysis 151K–251K Hidden reason-
ing
Legal reasoning /
risk analysis
Visible output is small;
most value comes from
reasoning quality.
Software Engi-
neering
25.5K–105.5K Verification, test-
ing, repair
Verification and
testing
Quality assurance
tokens may
outperform
code-generation
tokens.
Research Assis-
tance
72.5K–132.5K Retrieval and
hidden reason-
ing
Reasoning after
retrieval satura-
tion
Once retrieval quality
saturates, additional
reasoning dominates.
Multi-Agent Sys-
tems
210K per cycle,
potentially
1M+ over re-
peated cycles
Execution Planning and co-
ordination
Upstream planning
can have higher
marginal value than
large execution stages.
A common pattern emerges. The stage consuming the most tokens is not necessarily the
stage with the highest marginal productivity. Formally, for two workflowsiandj, it is possible
thatT i >T j while∂V/∂T i <∂V/∂T j. This inequality is the central economic lesson of work-
flow tokenomics: allocation should follow risk-adjusted marginal value, not raw token volume.
Several quantitative lessons follow. First, visible output tokens can be a small fraction of total
token expenditure: in legal analysis, the output report may require only 1,000 tokens while the
total footprint ranges from 151,000 to 251,000 tokens. Second, hidden reasoning can dominate
cost: in the legal case, hidden reasoning accounts for approximately 33.1% to 59.8% of total
token consumption, and in software engineering, verification, testing, and repair can consume
four to twenty times as many tokens as code generation. Third, marginal productivity de-
pends on saturation: in the research-assistance case, retrieval quality at 50,000 tokens is already
approximately 0.982 under the assumed production function, implying very low marginal re-
trieval value. Fourth, workflow position matters: in the multi-agent case, planning consumes
31

less than 5% of total tokens but can have greater downstream marginal impact than execution
because planning quality affects every subsequent stage.
Consequently, the practical objective is not to minimize token use in isolation. The objec-
tive is to solve the risk-aware allocation problem in Eq. (5.7), with feasible setF(B) ={T∈
RW + : ∑w∈W Tw ≤B}, so that tokens are assigned to workflows with the highest risk-adjusted
marginal value, satisfyingµ w(∂ϕw/∂Tw)−ζ(∂Φ/∂T w) =λat an interior optimum. This con-
dition states that every workflow receives tokens until its risk-adjusted marginal productivity
equals the shadow value of the token budget.
7 Conclusion and Future Research Directions
The emergence of foundation models has transformed tokens from a technical implementation
detail into a fundamental economic unit of artificial intelligence. Tokens now serve simultane-
ously as units of information representation, computation, memory utilization, energy expen-
diture, resource allocation, and monetary exchange. As a result, understanding the generation,
consumption, pricing, and allocation of tokens has become essential for the efficient design and
operation of modern AI systems.
This paper developed a unified framework forAI T okenomics, defined as the study of how
tokens are generated, consumed, valued, allocated, and optimized within AI ecosystems. The
framework integrates technical, economic, and operational perspectives into a common ana-
lytical structure. At the technical level, tokens were characterized as computational objects
whose processing determines inference cost, memory requirements, latency, and energy con-
sumption. At the economic level, tokens were interpreted as scarce resources whose allocation
influences workflow quality, enterprise value, and organizational performance. At the market
level, tokens were viewed as tradable units that may eventually support new forms of pricing,
allocation, and governance mechanisms.
Several key insights emerge from this perspective. First, token consumption and economic
value are fundamentally distinct concepts. Although tokens provide a convenient accounting
unit for measuring computational effort, their economic significance depends on the value gen-
erated by the tasks they enable. Second, token demand is highly heterogeneous across appli-
cations and depends upon task difficulty, context size, uncertainty, retrieval requirements, and
workflow structure. Third, enterprise AI systems should be understood as networks of inter-
dependent workflows in which token allocations influence both local performance and down-
32

stream organizational outcomes. Finally, efficient token allocation requires balancing computa-
tional cost, productivity, uncertainty, and risk across the entire workflow ecosystem.
The framework developed herein suggests that AI tokenomics may become a foundational
discipline at the intersection of artificial intelligence, economics, operations research, and sys-
tems engineering. Much as classical economics studies the allocation of scarce resources and
communication theory studies the allocation of bandwidth, AI tokenomics studies the alloca-
tion of computational reasoning capacity. Despite recent advances, the field remains in its in-
fancy. Numerous fundamental questions remain unresolved and provide fertile opportunities
for future research.
One important direction concerns the measurement of hidden reasoning activity. Contem-
porary models often perform substantial internal reasoning that is not directly observable to
users. Eq. (2.1) defines total token consumption, whereT H represents hidden reasoning to-
kens. Existing measurement systems generally observe only the visible components. Develop-
ing methodologies for estimating and validating hidden reasoning activity remains a central
challenge for both technical and economic analysis. Relatedly, a second direction concerns
empirical calibration. Eq. (2.3) connects task characteristics to token demand, but the precise
forms of these relationships remain largely unknown. Large-scale empirical studies are needed
to estimate production elasticities, characterize scaling behavior, and understand how token
requirements vary across domains, models, and organizational contexts.
A third research direction involves the development of rigorous utility and productivity
metrics. The notion of token productivity,η=U/T, captures the value generated per token
consumed. However, defining and measuring utility remains difficult. Future work should in-
vestigate methods for quantifying utility through human evaluation, organizational outcomes,
economic return, decision quality, and task-specific performance metrics. Standardized produc-
tivity measures would make comparisons across models, workflows, and deployment strate-
gies more reliable. Another important area concerns enterprise token allocation. This paper
introduced optimization models in which token allocations determine workflow quality and
enterprise value. Future work should extend these formulations to dynamic settings with time-
varying demand, learning agents, adaptive budgets, and strategic interactions among stake-
holders. Connections with stochastic control, network optimization, and multi-agent reinforce-
ment learning appear particularly promising.
Market and mechanism design constitute another major frontier. Existing AI markets pri-
marily rely on fixed per-token pricing schemes. Future systems may employ dynamic pricing,
33

auction-based allocation, congestion pricing, subscription hybrids, or outcome-based compen-
sation mechanisms. The study of such systems raises questions concerning efficiency, incentive
compatibility, market equilibrium, and fairness. Understanding the conditions under which al-
ternative pricing mechanisms outperform conventional token billing remains an open research
problem. Closely related is the problem of contract design for token-based and agentic AI ser-
vices. In many enterprise deployments, a provider does not merely sell raw tokens; it offers
a service contract that may combine token quotas, service-level guarantees, latency commit-
ments, auditability requirements, outcome-based payments, and risk-sharing provisions. De-
signing such contracts requires addressing adverse selection, moral hazard, unobservable hid-
den reasoning effort, heterogeneous customer value, and uncertain downstream consequences
of AI decisions. Contract-theoretic models of agentic AI pricing, such as PACT [51], provide
a promising starting point for studying how token prices, quality guarantees, and incentive-
compatible service agreements should be jointly designed. The emergence of autonomous
agents introduces additional challenges. In future AI ecosystems, agents may allocate, ex-
change, and negotiate token budgets among themselves. Such environments naturally give
rise to multi-agent token economies in which computational resources function as an internal
currency. Designing stable, efficient, and incentive compatible token exchange protocols is a
rich interdisciplinary research area spanning artificial intelligence, economics, and game the-
ory.
An equally important direction concerns the financialization of computational resources.
Recent proposals involving tokenized compute assets, tradable GPU capacity, and decentral-
ized AI infrastructure suggest the possibility of secondary markets for computational resources.
While such systems may improve liquidity and resource utilization, they also raise questions
concerning speculation, market concentration, governance, and regulation. Understanding the
economic implications of treating computational capacity as a financial asset remains an open
challenge. Finally, the development of public benchmarks and datasets is essential for the mat-
uration of AI tokenomics as a scientific discipline. Future research should establish standard-
ized datasets linking tasks, token consumption, workflow characteristics, computational cost,
energy expenditure, and economic outcomes. Such resources would facilitate reproducible
research, enable empirical validation of theoretical models, and support the development of
evidence-based token allocation policies.
In conclusion, tokens have become the fundamental resource through which modern AI
systems consume computation and generate value. As AI systems become increasingly au-
34

tonomous, interconnected, and economically important, the efficient management of token re-
sources will emerge as a central technical and organizational challenge. AI tokenomics provides
a framework for addressing this challenge by integrating computation, economics, measure-
ment, optimization, and market design into a unified theory of resource allocation for compu-
tational intelligence.
References
[1] D. Acemoglu. Harms of AI. Working Paper 29247, National Bureau of Economic Research,
2021. (Cited on p. 19)
[2] Akash Network. Akash network: Decentralized cloud infrastructure.https://akash.
network/whitepapers/, 2020. (Cited on p. 19)
[3] M. A. Al Bari and Q. Zhu. A gestalt game-theoretic framework for designing agentic AI
workflows in cyber deception. InInternational Conference on Game Theory and AI for Security,
pages 228–248, Cham, 2025. Springer Nature Switzerland. (Cited on pp. 20, 21, 22)
[4] Alibaba Cloud. Qwen API pricing.https://help.aliyun.com, 2026. Accessed: 2026-06-
09. (Cited on p. 13)
[5] Anthropic. Claude API pricing.https://platform.claude.com/docs/en/
about-claude/pricing, 2026. Accessed: 2026-06-09. (Cited on pp. 2, 5, 12, 13,
14)
[6] Anthropic. Context windows.https://platform.claude.com/docs/en/
build-with-claude/context-windows, 2026. Accessed 2026-06-09. (Cited on pp. 10, 11)
[7] Anthropic. Plans and pricing.https://claude.com/pricing, 2026. Accessed 2026-06-09.
(Cited on p. 15)
[8] L. Bai, Z. Huang, X. Wang, J. Sun, R. Mihalcea, E. Brynjolfsson, A. Pentland, and J. Pei.
How do AI agents spend your money? analyzing and predicting token consumption in
agentic coding tasks.arXiv preprint arXiv:2604.22750, 2026. (Cited on pp. 10, 11, 12)
[9] N. Belrose, Z. Furman, L. Smith, D. Halawi, I. Ostrovsky, L. McKinney, S. Biderman, and
J. Steinhardt. Eliciting latent predictions from transformers with the tuned lens.arXiv
preprint arXiv:2303.08112, 2023. (Cited on p. 16)
35

[10] BenchLM. LLM pricing comparison dashboard.https://benchlm.ai/llm-pricing,
2026. Accessed: 2026-06-09. (Cited on p. 13)
[11] D. P . Bertsekas.Network Optimization: Continuous and Discrete Models. Athena Scientific,
1998. (Cited on pp. 22, 24)
[12] T. B. Brown, B. Mann, N. Ryder, M. Subbiah, J. Kaplan, P . Dhariwal, A. Neelakantan,
P . Shyam, G. Sastry, A. Askell, et al. Language models are few-shot learners. InAdvances in
Neural Information Processing Systems, volume 33, pages 1877–1901, 2020. (Cited on pp. 1,
7, 14)
[13] Z. S. Chen and Q. Zhu. A theory of multilevel interactive equilibrium in NeuroAI.arXiv
preprint arXiv:2605.10505, 2026. (Cited on p. 19)
[14] CostGoat. LLM API cost comparison.https://costgoat.com/compare/llm-api, 2026.
Accessed: 2026-06-09. (Cited on p. 13)
[15] T. Dao, D. Y. Fu, S. Ermon, A. Rudra, and C. Ré. Flashattention: Fast and memory-efficient
exact attention with io-awareness. InAdvances in Neural Information Processing Systems,
volume 35, pages 16344–16359, 2022. (Cited on pp. 8, 16)
[16] DeepSeek AI. Deepseek API pricing.https://platform.deepseek.com, 2026. Accessed:
2026-06-09. (Cited on p. 13)
[17] N. Elhage, N. Nanda, C. Olsson, T. Henighan, N. Joseph, B. Mann, A. Askell, Y. Bai,
A. Chen, T. Conerly, et al. A mathematical framework for transformer circuits.https:
//transformer-circuits.pub/2021/framework/index.html, 2021. Transformer Circuits
Thread. (Cited on p. 16)
[18] A. Ghodsi, M. Zaharia, B. Hindman, A. Konwinski, S. Shenker, and I. Stoica. Dominant re-
source fairness: Fair allocation of multiple resource types. InProceedings of the 8th USENIX
Symposium on Networked Systems Design and Implementation, pages 323–336, 2011. (Cited on
pp. 18, 19, 22)
[19] Google Cloud. Gemini enterprise agent platform.https://cloud.google.com/
products/gemini-enterprise-agent-platform, 2026. Accessed 2026-06-09. (Cited on
p. 15)
[20] Google DeepMind. Gemini API pricing.https://ai.google.dev/gemini-api/docs/
pricing, 2026. Accessed: 2026-06-09. (Cited on pp. 2, 5, 12, 13, 14)
36

[21] J. Hoffmann, S. Borgeaud, A. Mensch, E. Buchatskaya, T. Cai, E. Rutherford,
D. de Las Casas, L. A. Hendricks, J. Welbl, A. Clark, et al. Training compute-optimal
large language models. InAdvances in Neural Information Processing Systems, volume 35,
pages 30016–30030, 2022. (Cited on pp. 4, 5, 9, 16, 23)
[22] J. Kaplan, S. McCandlish, T. Henighan, T. B. Brown, B. Chess, R. Child, S. Gray, A. Rad-
ford, J. Wu, and D. Amodei. Scaling laws for neural language models.arXiv preprint
arXiv:2001.08361, 2020. (Cited on pp. 4, 5, 9, 16, 23)
[23] F. P . Kelly, A. K. Maulloo, and D. K. H. Tan. Rate control for communication networks:
Shadow prices, proportional fairness and stability.Journal of the Operational Research Soci-
ety, 49(3):237–252, 1998. (Cited on pp. 18, 19, 22, 24)
[24] T. Kudo and J. Richardson. Sentencepiece: A simple and language independent subword
tokenizer and detokenizer for neural text processing. InProceedings of the 2018 Conference
on Empirical Methods in Natural Language Processing: System Demonstrations, pages 66–71,
2018. (Cited on pp. 3, 5, 7)
[25] LangChain. ChatOpenAI integration.https://docs.langchain.com/oss/python/
integrations/chat/openai, 2026. Accessed 2026-06-09. (Cited on pp. 10, 11)
[26] P . Lewis, E. Perez, A. Piktus, F. Petroni, V . Karpukhin, N. Goyal, H. Küttler, M. Lewis,
W.-t. Yih, T. Rocktäschel, and S. Riedel. Retrieval-augmented generation for knowledge-
intensive NLP tasks. InAdvances in Neural Information Processing Systems, volume 33, pages
9459–9474, 2020. (Cited on pp. 7, 23)
[27] N. Merizzi, T. Smith, D. Kearns-Manolatos, N. Mittal, and G. Churiwala. The pivot to
tokenomics: Navigating AI’s new spend dynamics. Industry report, Deloitte, Jan. 2026.
Accessed January 2026. (Cited on p. 2)
[28] Meta AI. Llama models.https://ai.meta.com/llama, 2026. Accessed: 2026-06-09. (Cited
on p. 13)
[29] Mistral AI. Mistral API pricing.https://docs.mistral.ai, 2026. Accessed: 2026-06-09.
(Cited on p. 13)
[30] R. B. Myerson. Optimal auction design.Mathematics of Operations Research, 6(1):58–73,
1981. (Cited on pp. 17, 18, 20)
37

[31] N. Nisan, T. Roughgarden, E. Tardos, and V . V . Vazirani, editors.Algorithmic Game Theory.
Cambridge University Press, 2007. (Cited on pp. 17, 18, 20)
[32] Nostalgebraist. Interpreting GPT: The logit lens.https://www.alignmentforum.org/
posts/AcKRB8wDpdaN6v6ru/interpreting-gpt-the-logit-lens, 2020. Alignment Fo-
rum. (Cited on p. 16)
[33] OpenAI. API pricing.https://openai.com/api/pricing/, 2026. Accessed: 2026-06-09.
(Cited on pp. 2, 5, 12, 13, 14)
[34] OpenAI. Prompt engineering.https://developers.openai.com/api/docs/guides/
prompt-engineering, 2026. Accessed 2026-06-09. (Cited on p. 10)
[35] J. S. Park, J. C. O’Brien, C. J. Cai, M. R. Morris, P . Liang, and M. S. Bernstein. Generative
agents: Interactive simulacra of human behavior. InProceedings of the 36th Annual ACM
Symposium on User Interface Software and T echnology, pages 1–22, 2023. (Cited on p. 19)
[36] Protocol Labs. Filecoin: A decentralized storage network.https://filecoin.io/
filecoin.pdf, 2017. (Cited on p. 19)
[37] A. Radford, J. Wu, R. Child, D. Luan, D. Amodei, and I. Sutskever. Language models are
unsupervised multitask learners.OpenAI T echnical Report, 2019. (Cited on p. 1)
[38] V . J. Reddi, C. Cheng, D. Kanter, P . Mattson, G. Schmuelling, C.-J. Wu, B. Anderson,
M. Breughe, M. Charlebois, W. Chou, et al. MLPerf inference benchmark. In2020
ACM/IEEE 47th Annual International Symposium on Computer Architecture, pages 446–459,
2020. (Cited on p. 16)
[39] J.-C. Rochet and J. Tirole. Platform competition in two-sided markets.Journal of the Euro-
pean Economic Association, 1(4):990–1029, 2003. (Cited on p. 20)
[40] T. Schick, J. Dwivedi-Yu, R. Dessì, R. Raileanu, M. Lomeli, E. Hambro, L. Zettlemoyer,
N. Cancedda, and T. Scialom. Toolformer: Language models can teach themselves to use
tools. InAdvances in Neural Information Processing Systems, volume 36, pages 68539–68551,
2023. (Cited on pp. 4, 10, 15, 19)
[41] R. Sennrich, B. Haddow, and A. Birch. Neural machine translation of rare words with
subword units. InProceedings of the 54th Annual Meeting of the Association for Computational
Linguistics, pages 1715–1725, 2016. (Cited on pp. 3, 5, 7)
38

[42] Y. Shoham and K. Leyton-Brown.Multiagent Systems: Algorithmic, Game-Theoretic, and
Logical Foundations. Cambridge University Press, 2008. (Cited on p. 19)
[43] E. Strubell, A. Ganesh, and A. McCallum. Energy and policy considerations for deep
learning in NLP. InProceedings of the 57th Annual Meeting of the Association for Computational
Linguistics, pages 3645–3650, 2019. (Cited on p. 17)
[44] H. Topcuoglu, S. Hariri, and M.-Y. Wu. Performance-effective and low-complexity task
scheduling for heterogeneous computing.IEEE T ransactions on Parallel and Distributed Sys-
tems, 13(3):260–274, 2002. (Cited on p. 22)
[45] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L. Kaiser, and
I. Polosukhin. Attention is all you need. InAdvances in Neural Information Processing Sys-
tems, volume 30, 2017. (Cited on pp. 1, 8, 14, 16)
[46] X. Wang, J. Wei, D. Schuurmans, Q. Le, E. Chi, S. Narang, A. Chowdhery, and D. Zhou.
Self-consistency improves chain of thought reasoning in language models. InInternational
Conference on Learning Representations, 2023. (Cited on pp. 8, 10, 16)
[47] J. Wei, X. Wang, D. Schuurmans, M. Bosma, B. Ichter, F. Xia, E. H. Chi, Q. V . Le, and
D. Zhou. Chain-of-thought prompting elicits reasoning in large language models. InAd-
vances in Neural Information Processing Systems, volume 35, pages 24824–24837, 2022. (Cited
on pp. 8, 10, 16)
[48] M. Wooldridge.An Introduction to MultiAgent Systems. Wiley, 2 edition, 2009. (Cited on
p. 19)
[49] C.-J. Wu, R. Raghavendra, U. Gupta, B. Acun, N. Ardalani, K. Maeng, G. Chang, F. A.
Behram, J. Huang, C. Bai, et al. Sustainable AI: Environmental implications, challenges
and opportunities. InProceedings of Machine Learning and Systems, volume 4, pages 795–
813, 2022. (Cited on p. 17)
[50] xAI. Grok API pricing.https://docs.x.ai, 2026. Accessed: 2026-06-09. (Cited on pp. 2,
5, 12, 13)
[51] Y.-T. Yang and Q. Zhu. PACT: A contract-theoretic framework for pricing agentic AI ser-
vices powered by large language models. InProceedings of the 2025 IEEE Global Communi-
cations Conference (GLOBECOM), Taipei, Taiwan, 2025. IEEE. (Cited on pp. 15, 34)
39

[52] Y.-T. Yang and Q. Zhu. Internet of agentic AI: Incentive-compatible distributed teaming
and workflow.arXiv preprint arXiv:2602.03145, 2026. (Cited on pp. 19, 22)
[53] S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, and Y. Cao. ReAct: Synergizing
reasoning and acting in language models. InInternational Conference on Learning Represen-
tations, 2023. (Cited on pp. 4, 10, 15, 19)
[54] Zhipu AI. Glm API pricing.https://open.bigmodel.cn, 2026. Accessed: 2026-06-09.
(Cited on p. 13)
[55] Q. Zhu. Foundations of cyber resilience: The confluence of game, control, and learning
theories.arXiv preprint arXiv:2404.01205, 2024. (Cited on pp. 19, 20)
[56] Q. Zhu. Game theory meets LLM and agentic AI: Reimagining cybersecurity for the age
of intelligent threats.arXiv preprint arXiv:2507.10621, 2025. (Cited on pp. 20, 21)
[57] Q. Zhu. Insurance of agentic AI.arXiv preprint arXiv:2606.05449, 2026. (Cited on p. 25)
[58] Q. Zhu and M. A. Al Bari. Agentic AI for cyber deception: A gestalt game-theoretic ap-
proach to defending against botnet DDoS attacks. InProceedings of the 59th Hawaii Interna-
tional Conference on System Sciences, 2026. (Cited on pp. 20, 21, 22)
[59] Q. Zhu and T. Ba¸ sar. Revisiting game-theoretic control in socio-technical networks: Emerg-
ing design frameworks and contemporary applications.arXiv preprint arXiv:2411.01794,
2024. (Cited on pp. 19, 20, 22)
[60] Q. Zhu and Z. Han. Learning, misspecification, and cognitive arbitrage in linear-quadratic
network games.arXiv preprint arXiv:2603.17157, 2026. (Cited on pp. 19, 22)
40
