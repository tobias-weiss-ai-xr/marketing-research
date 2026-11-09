---
title: Decentralized LLM Workflows via Sequential Auctions
url: https://arxiv.org/abs/2610.22201
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Ian Gemp
- Shubhendu Trivedi
- Adam Fisch
- Fantine Huot
- Michael Kaisers
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.22201
pages: 28
chars: 77167
fetched_at: '2026-11-08T13:26:09+00:00'
kb_version: 1
---

# Decentralized LLM Workflows via Sequential Auctions

2026-10-15
Decentralized LLM Workflows via Sequential
Auctions
Ian Gemp1, Shubhendu Trivedi1, Adam Fisch1, Fantine Huot1, Michael Kaisers1, Mirella Lapata1, William W.
Cohen1, Alekh Agarwal2, Kate Larson1,3 and Jacob Eisenstein1
1Google DeepMind,2Google Research,3University of Waterloo
We present a scalable framework for solving multi-step tasks through a decentralized market of self-
interested agents. Prior theoretical work demonstrated that agents organized through sequential
auctions can converge to a globally optimal policy in a Markov decision process (MDP), but relied on the
restrictiveassumptionoftheexistenceofperfectclonesasamodelofperfectcompetition. Inreality, exact
clones drive agent profit to zero, violating the natural risk-reward incentives of participants. Conversely,
we empirically demonstrate that the opposite extreme, absence of competition, also leads to market
failure and value extraction collapse. Between these two extremes, we investigate how heterogeneous
agents can survive in markets that span the critical middle ground ofimperfect competition. To be
profitable, agents learn to strategically shade bids to secure positive individual profit margins, while still
ensuring that the marketplace functions effectively enough so that collaborative tasks posed by market
consumers can still be solved. We formulate and evaluate four bidding algorithms (Mirror Descent,
Thompson Sampling, Bayes-Optimal, and PPO) across three auction protocols (1st-Price, 2nd-Price, and
Credit-Conserving Vickrey). Across a diverse set of domains, we demonstrate that imperfect competition
successfully sustains necessary agent profit margins while maintaining high task success rates at low
costs.
Keywords: decentralized reinforcement learning, auction mechanisms, multi-agent systems, LLM agents
1. Introduction
Modern AI systems increasingly face tasks that require composing multiple specialized capabilities—
dynamically routing queries across varying LLM sizes to optimize inference costs, gathering and
synthesizing evidence from disparate sources, or dispatching subtasks to external tools. The domi-
nant paradigm centralizes this composition in a single controller (an “orchestrator” LLM or a fixed
computation graph), which must explicitly plan the sequence of operations and assign credit to each
component (Hong et al., 2024; Shen et al., 2023).
An alternative, inspired by economic theory, is to let asocietyof specialized agents coordinate
through a market mechanism. To solve temporal credit assignment across multi-step trajectories
without hierarchical oversight, we draw on the foundationalBucket Brigadeprinciple (Bartholdi III
and Eisenstein, 1996; Holland, 1985): each agent purchases the current task state from the preceding
agent in an auction, transforms the state, and resells the updated state to the next downstream agent.
Terminal task rewards earned at completion naturally propagate backward through the chain of resale
prices, rewarding upstream contributors proportionally to their marginal value added.
To ground this decentralized economy in a reinforcement learning framework, we build on the
work of Chang et al. (2020). They proved that a Vickrey (second-price) auction perfectly aligns each
agent’s locally optimal bidding strategy with the globally optimal MDP policy. However, translating
this theoretical breakthrough to real-world AI societies reveals a critical gap: their optimal equilibrium
relies on the restrictive assumption of perfect competition via artificially cloned agents.
Corresponding author(s): imgemp@google.com
©2026 Google. All rights reserved
arXiv:2610.22201v1  [cs.GT]  15 Oct 2026

Decentralized LLM Workflows via Sequential Auctions
In practice, this perfect-clone assumption breaks down due to two fundamental economic realities.
First is aparticipation barrier: with exact clones, the expected highest and second-highest bids are
identical. The winning agent pays exactly their true valuation, driving their net profit to strictly zero.
Because participating in a market carries inherent risk, agents will simply sit out rather than opt in
to risk their resources for a net-zero expected return. Second is theanti-cloning incentive: perfect
competition will not naturally arise because no rational actor will clone their own agent (which
cannibalizes their own profit margin), and participants will actively protect their models’ intellectual
property from being copied by competitors.
Ifperfectclonesaretheoreticallyunprofitableandstrategicallyirrational, doesthemarketcollapse?
We first demonstrate that the opposite extreme—absence of competition (amonopsonyat any step in
the task chain)—does indeed cause the market to fail. When an agent is the sole eligible buyer for
a given state, they act as a monopsonist, bidding the absolute minimum required to win. Without
competitive pressure, the clearing price collapses, and downstream value is not efficiently extracted
and passed upstream. This breaks the sequential credit assignment required to sustain a multi-step
pipeline, as upstream agents are starved of the revenue needed to offset their own inference costs.
To bridge this gap, we adapt the framework of Chang et al. (2020) to societies of Large Language
Models (LLMs), formulating a decentralized, sequential forward auction mechanism tailored to
the operational realities of modern LLM pipelines. In doing so, we shift the theoretical focus to
the critical, realistic middle ground:imperfect competition. We model societies populated by LLM
agents that occupy similar capability niches but are differentiated by heterogeneous inference costs,
prompt engineering, and localized heuristics. Because off-the-shelf language models are notoriously
miscalibrated judges of their own success probabilities and token costs (Fradkin and Krishnan, 2026),
agents cannot rely on zero-shot prompting to evaluate states. Instead, each agent learns a lightweight
neural valuation policy via reinforcement learning to navigate the tradeoff between winning the right
to act and shading their bids to secure a positive profit margin.
In this paper, we present a comprehensive empirical study of decentralized LLM routing under
imperfect competition. Our core contributions include:
1. Decentralized LLM Markets and Imperfect Competition:We introduce an architectural and
algorithmic framework for sequential auction MDPs in LLM societies, demonstrating experimentally
that imperfect competition is sufficient to sustain positive profit margins and enable viable multi-
agent pipelines under traditional auction mechanisms.
2. Monopsony Failure Validation:We reveal empirically through a targeted synthetic domain
that absence of competition collapses the market, establishing imperfect competition as a viable
operational regime under traditional auction mechanisms.
3. Algorithmic Bidding Strategies:We formulate and benchmark four bidding algorithms—Mirror
Descent, Thompson Sampling, Bayes-Optimal, and PPO—demonstrating how individual agents
can efficiently learn optimal pricing and bid-shading policies.
4. Extensive Benchmarking:We deploy our framework across diverse LLM domains (including a
math reasoning task and newly-constructed synthetic news market). Through market density
sweeps across 1st-Price, 2nd-Price, and Credit-Conserving Vickrey (CCV) auctions (Fig 1b&3), we
show that imperfect competition is sufficient to sustain positive agent profits while simultaneously
achieving higher task success rates (accuracy) than centralized orchestration baselines.
2

Decentralized LLM Workflows via Sequential Auctions
2. Background
To formalize the decentralized ecosystem just described, we model the multi-agent task pipeline as a
sequential auction, in line with previous work (Chang et al., 2020). In this framework, self-interested
agents bid for the right to progressively transform an initial state𝑠0 into a terminal solution𝑠𝑇. Below,
we define the underlying market MDP, the local profit incentives of the agents, and the idealized
theoretical clearing rules that enable optimal credit assignment.
2.1. The Sequential Spot Market MDP
We model decentralized task routing as a finite horizon (𝑇) sequential Markov Decision Process
(MDP) defined by the tuple(S,A,P,𝑅,𝛾) . Rather than relying on a centralized policy𝜋(𝑎|𝑠) to select
actions, the action spaceA is defined by a society of independent agents. For intuition, consider a
gridworld: instead of a single controller choosing to move up or down, specialized “Up” and “Down”
agents compete in an auction for the right to act on the current state𝑠𝑡.
At each step𝑡, a registry of agents evaluates𝑠𝑡 to determine their eligibility. Eligible agents submit
bids, and the highest bidder wins the right to process the state. The state transition is defined by the
winning agent𝑖’s localized action𝑎𝑡, which generates the next state𝑠𝑡+1 and yields an environmental
reward𝑟(𝑠𝑡,𝑎𝑡). The process is repeated until a final state𝑠𝑇 is reached. Social welfare is defined as
the sum of discounted rewards.
Agents optimize for their individual net utility, orprofit, over the course of a transaction. For an
agent winning the auction at step𝑡, the profit𝑈𝑖,𝑡 is defined as the sum of the environmental reward
and the net flow of capital:
𝑈𝑖,𝑡 =𝑟(𝑠 𝑡,𝑎𝑡)+𝑃 (𝑡) in −𝑃(𝑡) out (1)
where 𝑃(𝑡) out is the clearing price the agent pays to acquire𝑠𝑡, and𝑃(𝑡) in is the revenue the agent receives
when they subsequently auction the transformed state𝑠𝑡+1 to the next downstream agent.
2.2. Auction Mechanisms and Credit Assignment
The rules governing the clearing price𝑃(𝑡) out and the subsequent revenue𝑃(𝑡) in depend strictly on
the chosen auction mechanism. Chang et al. (2020) established a foundational bridge between
reinforcement learning and mechanism design by demonstrating that under a Vickrey (second-price)
auction, the globally optimal MDP policy constitutes a Nash equilibrium for myopic agents maximizing
their local transaction profit. Their result relies on two distinct theoretical properties:
1. TruthfulBiddingviaMyopia:Assuming agents are myopic and optimize strictly for the immediate
transaction, the Vickrey auction guarantees that bidding one’s true valuation (𝑏𝑖 =𝑣 𝑖) is a weakly
dominant strategy. Thus, an agent’s bid reveals its true estimated action-value,𝑄𝑖(𝑠𝑡).
2.Perfect Credit Conservation via Clones:To ensure the market clears at the optimal state-value
without requiring external platform subsidies, Chang et al. (2020) in their Section 5.4 build on the
assumption that the market is populated with exact clones of every agent. With perfect competition
via exact clones, the highest and second-highest bids are identical (𝑏(1) =𝑏 (2)). Because the
Vickrey auction charges the second-highest bid, the market clearing price exactly extracts the
maximum Q-value:𝑃(𝑡) out =max 𝑖𝑄𝑖(𝑠𝑡)=𝑉 ∗(𝑠𝑡).
When the clearing price perfectly tracks𝑉∗(𝑠𝑡), the revenue passed upstream acts as an exact
Bellman backup. Specifically, if the downstream auction at step𝑡+ 1clears at 𝑉∗(𝑠𝑡+1), the upstream
3

Decentralized LLM Workflows via Sequential Auctions
agent receives𝑃(𝑡) in =𝛾𝑉 ∗(𝑠𝑡+1).1 By maximizing their local profit𝑈𝑖,𝑡, agents naturally align their
economic incentives with the global MDP objective, recursively propagating credit back to the initial
state. However, this theoretical alignment guarantee unravels if either of the above assumptions is
unmet. Hence, we aim to study the robustness of a heterogeneous LLM market MDP empirically.
3. Decentralized LLM Markets and Imperfect Competition
Applying the market MDP to LLM societies requires formalizing inference costs within the reward
structure and relaxing the idealized assumption of perfect competition made in previous work.
3.1. LLM Transformations and Inference Costs
In an LLM society, the state𝑠𝑡 represents the current task context, comprising the text or structured
payload (e.g., a natural language query, an intermediate translation, or a JSON object containing accu-
mulated evidence). The action space corresponds to an agent’s localized LLM invocation, transforming
the payload to generate𝑠𝑡+1.
Crucially, taking this action incurs a local inference cost𝑐𝑖,𝑡 for the agent (e.g., API token costs).
We formalize this by defining the environmental reward during intermediate steps as strictly negative:
𝑟(𝑠𝑡,𝑎𝑡)=−𝑐 𝑖,𝑡. If the agent’s action at step𝑇− 1successfully resolves the task and transitions the
environment to a terminal state𝑠𝑇, the reward𝑟(𝑠𝑇−1,𝑎𝑇−1) incorporates both the negative inference
cost and the positive terminal reward provided by the evaluator. Because the task is complete, no
subsequent auction occurs, yielding𝑃(𝑇−1) in =0.
3.2. The Participation Barrier and the Clone Assumption
We now address the problem of cloning agents in a market MDP. Under the assumption of perfect
clones, the equilibrium clearing price exactly equals the winner’s true valuation (𝑃(𝑡) out =𝑏(2) =𝑣 𝑖),
hence the winner’s expected utility is strictly zero (𝔼[𝑈𝑖,𝑡]= 0). An agent maximizing expected profit
has no strict incentive to opt into the market, since abstention already achieves zero profit.
Furthermore, no rational agent would choose to clone themselves, as doing so strictly cannibalizes
their profit margin. Conversely, participants will actively protect their models from being copied by
competitors. Consequently, real LLM spot markets are bounded to operate underimperfect competition,
where𝑏(1) > 𝑏(2). It is precisely this structural gap that allows the winner to secure a positive profit
margin (𝑈𝑖,𝑡 >0), overcoming the participation barrier.
3.3. Defining Agent Heterogeneity
To operationalize the regime ofimperfect competition, we define how agents differ within the market.
In our framework, all agents participate in a unified market and can theoretically bid on any state;
however, they act as imperfect substitutes, organically specializing based on their localized capabilities.
We parameterize this heterogeneity across two primary axes:
1. InferenceCost( 𝑐𝑖,𝑡):Agents use different LLMs. For example, an agent backed by a<1B parameter
LLM incurs a much lower base inference cost than one backed by a>100B parameter LLM, allowing
it to bid competitively on lower-margin tasks.
1Chang et al. (2020) discount the payment by𝛾to match standard discounted returns in RL.
4

Decentralized LLM Workflows via Sequential Auctions
2. Transition Reliability:Agents are differentiated by distinct prompt engineering techniques,
identity embeddings, and asymmetric data access (e.g., access to different document corpora).
These differences cause their state transitions (𝑠𝑡→𝑠 𝑡+1) to vary in quality and relevance. A more
capable agent is more likely to generate a state that attracts high downstream bids, thereby raising
its expected future revenue.
Because of these variances, even among agents attempting to fulfill the exact same role in a task,
true valuations naturally diverge (𝑣1 ≠𝑣 2). This structural gap allows the most efficient agent to shade
its bid below its own true valuation while still outbidding the rest of the market, thereby securing a
positive profit margin and incentivizing participation in the market.
3.4. Auction Mechanisms under Imperfect Competition
We study heterogeneous markets under the same three auctions discussed in (Chang et al., 2020):
• 2nd-Price (Vickrey):The downstream buyer pays𝑏(2), but the upstream seller receives𝑏(1). The
marketplace platform must act as a market maker, subsidizing the deficit (𝑏(1)−𝑏(2)).
• Credit-Conserving Vickrey (CCV):The buyer pays𝑏(2), and the upstream seller receives𝑏(2). This
avoids subsidies, but fails to pass the full winning valuation upstream when𝑏(1) > 𝑏(2).
• 1st-Price (Bucket Brigade):The winner pays their exact bid (𝑃(𝑡) out =𝑏(𝑡) (1)), and the seller receives
the highest downstream bid (𝑃(𝑡) in =𝛾𝑏(𝑡+1) (1) ). Credit conservation is structurally maintained without
external subsidies. However, to secure a profit, agents must learn to strategically shade their bids
below their true valuations.
Because standard Vickrey auctions require subsidies and CCV passes minimal value to upstream
agents, we prioritize the simpler 1st-Price auction; we justify this choice in Section 5.1.
3.5. Strategic Bidding in 1st-Price LLM Markets
In a 1st-price auction, an agent must bid strategically to balance win probability against profit margin.
To maximize expected profit, agent𝑖 must first estimate its true valuation of the state,𝑣𝑖(𝑠𝑡), which
amounts to the expected future revenue minus its local inference costs for applying its transformation
𝑎𝑡. Following the definitions of𝑃(𝑡) in and𝑟(𝑠 𝑡,𝑎𝑡)from above, the valuation is:
𝑣𝑖(𝑠𝑡)=𝔼 𝑠𝑡+1∼P(·|𝑠 𝑡,𝑎𝑡)

𝑃(𝑡) in +𝑟(𝑠 𝑡,𝑎𝑡)  =𝔼 𝑠𝑡+1∼P(·|𝑠 𝑡,𝑎𝑡)  𝛾𝑏(1)(𝑠𝑡+1)−𝑐 𝑖,𝑡  .(2)
Two agents eligible for the same state may differ in valuation through both their inference cost𝑐𝑖,𝑡,
and through the expected downstream bid𝑏(1)(𝑠𝑡+1) that their different output states attract, i.e., the
two axes of heterogeneity in Section 3.3. If the agent bids its true valuation,𝑏𝑖(𝑠𝑡)=𝑣 𝑖(𝑠𝑡), its ex-post
utility is zero. Consequently, a rational bidder must shade its bid below its private valuation to secure a
positive expected surplus (Krishna, 2009). We parameterize the bidding policy via a state-dependent
multiplicative shading factor,𝜉(𝑠𝑡)∈[ 0, 1), yielding the shaded bid𝑏𝑖(𝑠𝑡)=𝜉(𝑠 𝑡)𝑣𝑖(𝑠𝑡). The ex-post
surplus upon winning is thus(1−𝜉(𝑠 𝑡))𝑣𝑖(𝑠𝑡), highlighting the fundamental trade-off of 1st-price
auctions: lowering𝜉(𝑠𝑡) widens the conditional profit margin but strictly decreases the probability
of winning. Despite this strategic shading, recent analysis shows that 1st-price agentic markets still
achieve high welfare whenever competition is sufficiently strong (Trivedi et al., 2026).
5

Decentralized LLM Workflows via Sequential Auctions
4. Bidding Strategies
Crucially, ourframeworkdecouplestheagent’scorecapabilityfromitsmarketstrategy. Theunderlying
LLMs responsible for the state transitions (𝑠𝑡→𝑠 𝑡+1) are utilized strictly for inference and remain
frozen. The reinforcement learning process solely trains a lightweight MLP for each agent, which acts
as the state-dependent, myopic bidding policy. To survive in an imperfectly competitive market, an
agent’s MLP must solve two coupled learning problems at each step: accurately estimating the state’s
true valuation𝑣𝑖(𝑠𝑡), and determining the optimal shade factor𝜉(𝑠𝑡)∈( 0, 1) to maximize its expected
profit margin. The agent’s final bid is formulated as𝑏𝑖(𝑠𝑡)=𝜉(𝑠 𝑡)·𝑣 𝑖(𝑠𝑡). For Vickrey and CCV, we
enforce truthful bidding,𝜉(𝑠𝑡)= 1. All agents share a common neural architecture for the valuation
head, which predicts both the expected downstream value𝑣(𝑠𝑡) and its standard deviation𝜎(𝑠𝑡). The
valuation head is trained via a standard Gaussian negative log-likelihood (NLL) loss to regress toward
the empirical target𝑃(𝑡) in −𝑐 𝑖,𝑡. In what follows, we drop explicit dependence of functions on state
𝑠𝑡 but this is implied. We evaluate four distinct approaches for computing strategic bids in 1st-price
auctions:
MirrorDescentThe Mirror Descent (MD) strategy frames bid-shading as an online learning problem
under binary feedback (win or loss). Let𝜉∗ represent the unobserved optimal shade threshold that
matches the highest competing bid. The agent models the primal lossℓ𝑡(𝜉) as the regret of the agent’s
margin distance from this boundary: regret from over-bidding if the auction was won, and regret
from under-bidding if lost. Using an entropic regularizer, the proximal projection yields a closed-form
multiplicative weights update for the target shade factor (Beck and Teboulle, 2003):
𝜉target =
(
𝜉·𝑒 −𝜂 if won
𝜉·𝑒 +𝜂 if lost (3)
The dynamic step size is defined as𝜂=ˆ𝜎 where ˆ𝜎is the estimated standard deviation of the state’s
valuation described above. This updated𝜉target serves as a squared-error regression target for the
agent’s MLP, which is trained via gradient descent.
Thompson SamplingRather than maintaining a point estimate of the shade factor, the Thompson
Sampling (TS) agent models the competitive bid threshold (𝜉∗) probabilistically using a logit-normal
posterior distribution withN( 0, 1) logit prior. At inference time, TS samples a threshold directly from
this posterior to target the minimum winning bid and maximize its realized profit margin:
𝑧∼N(𝜇 ℓ,𝜎 2 ℓ), 𝜉=sigmoid(𝑧).(4)
The threshold distribution is updated via an NLL loss conditioned on the binary auction outcome.
Note that when the true threshold𝜉∗ > 1(a losing agent), the NLL updates push𝜇ℓ→∞ , so the
sampled shade factor converges to𝜉→1(𝑏 𝑖→𝑣 𝑖) while remaining bounded below1.
Bayes-Optimal BaselineInstead of attempting to bid precisely at a sampled threshold, we include a
Bayes-Optimalbaseline(BayesOpt)thathedgesacrossthefulluncertaintyofthethresholddistribution.
Utilizing the same logit-normal threshold posterior as Thompson Sampling, it selects the shade factor
deterministically to maximize expected profit margin under its current beliefs:
𝜉=arg max
𝜉′∈(0,1) (1−𝜉′)·Φ
logit(𝜉′)−𝜇 ℓ
𝜎ℓ

(5)
where(1−𝜉′) representstheproportionalprofitmarginiftheauctioniswon, and Φ(·) istheprobability
of winning under the posterior model of the competitive bid threshold from eq. (4).
6

Decentralized LLM Workflows via Sequential Auctions
Proximal Policy Optimization (PPO)Finally, we evaluate a standard deep reinforcement learning
approach as in (Chang et al., 2020). The PPO policy network outputs parameters𝛼,𝛽≥ 1to define a
unimodal Beta distribution, from which the shade factor is sampled:𝜉∼Beta(𝛼,𝛽) . The policy is
trained to maximize the empirical profit𝑈𝑖,𝑡 using the clipped surrogate objective:
LPPO =−min  𝜌𝑡𝐴𝑡,clip(𝜌 𝑡,1−𝜖,1+𝜖)𝐴 𝑡 −𝛽 entH(6)
where 𝜌𝑡 is the probability ratio between the current and old policies,𝜖= 0.2, 𝐴𝑡 =𝑈 𝑖,𝑡− ¯𝑈𝑖,ema is the
profit advantage over a moving average baseline (¯𝑈𝑖,ema = 0.99 ¯𝑈𝑖,ema+ 0.01𝑈𝑖,𝑡), andH is an entropy
bonus to prevent premature convergence (𝛽𝑒𝑛𝑡 =0.01).
State Representation and Pre-ProcessingBecause the raw environmental states in the LLM
domains are non-vector text payloads, they must be transformed before an agent’s trainable MLP can
process them to formulate a bid. To bridge raw text and policy inputs, we employ two distinct state
representation paradigms:
1. Dense Embeddings (Sec 5.1):The raw text is first embedded, e.g., utilizing Gecko (Lee et al.,
2024), before being passed to a trainable MLP alongside agent identity features.
2. Centralized Assessor (Sec 5.2):To aid cold-starting the market and decouple routing signals from
economic bidding / pricing, a centralizedassessorLLM evaluates and compresses the task context
into a discrete 0–10 relevance score for each agent. Agent MLPs operate directly on these one-hot
encoded scores, effectively reducing complex routing to a tractable tabular MDP via platform-side
feature engineering.
5. Empirical Evaluation
To empirically validate the necessity of imperfect competition and evaluate our bidding strategies, we
benchmark our market across a synthetic control domain and three diverse LLM environments.
5.1. Validating the Monopsony Failure (Synthetic Chain Translation)
We first evaluate the framework on a synthetic multi-step translation domain. In this environment,
states are constructed by concatenating two64-dimensional embeddings, one identifying the original
task and the other the current language. Agents act as bilingual translators stationed on the edges of
a graph (Figure 1a), possessing distinct inference costs𝑐𝑖. The market must route payloads from a
source node to target nodes with terminal reward$1by discovering the most cost-efficient topological
sequence (e.g., bypassing the expensive$0.50direct Fr→En edge in favor of the$0.02Fr→Sp→En
path). We evaluate all three proposed auctions: 1st-price, 2nd-price, and CCV.
This domain allows us to test the extremes of market competition. We configure the environment
with a single agent per edge (𝑁= 1). In this regime, intermediate nodes frequently act asmonopsonies.
This occurs either structurally (e.g., theSp has only one outgoing edge) or task-conditionally (e.g.,
Gehas two edges, but only one is viable for a given task, rendering the competitor’s bid zero).
The presence of an uncontested buyer exposes the failure modes of each auction type. In a
standard 2nd-price (Vickrey) auction, the monopsonist bids truthfully but pays the floor (0); the
platform must inject unacceptable subsidies (e.g.,$0.88at Sp) to pay the upstream seller the first
price. Under CCV, the buyer pays0and the upstream seller receives0. Under a 1st-price auction, the
monopsonist actively shades its bid down to the floor, passing a vanishingly small value upstream.
7

Decentralized LLM Workflows via Sequential Auctions
Fr En
Sp
Ge
Ja
Ko
0.50
𝑏=0.02±0.04
0.01
𝑏=0.85±0.04 0.01
𝑏=0.88±0.13
0.015
𝑏=0.05±0.09
0.03
𝑏=0.48±0.16
0.02
𝑏=0.38±0.34
0.02
𝑏=0.06±0.10
0.02
𝑏=0.00±0.00
Task 1 (𝑤=2)
Task 2 (𝑤=1)
(a) Domain graph & bids
0 2k 4k
0
.5
1
Episode
Success rate
1competitor (monopsony)
0 2k 4k
Episode
2competitors
Bayes Opt CC-Vickrey Mirror Descent PPO TS Vickrey
(b) Success rate over training
Figure 1| Translation Domain Validation: (a) The task graph showing inference costs (black) and
learnedVickreybids(blue, italic; mean±stddev). Downstreambidsreflecttasksamplingprobabilities
(e.g.,En→Ja expects0 .48because Task 1 is sampled2/3of the time). The upstreamSp→En bid
(0.88) accurately approximates the downstream expected value minus local costs (0.48+ 0.38− 0.01 =
0.85). (b) Success rate increases and stabilizes across all auctions under increasing market density.
Competitors are differentiated by cost𝑐=𝑐 𝑏(1+𝑡) with𝑡∼𝑈(− 0.5, 0.5) and base costs𝑐𝑏 listed in the
graph. Curves are means over3independent trials and shaded regions span±1standard deviation;
both are computed on a trailing101-episode rolling average.
For CCV and 1st-price auctions, this failure to pass value backward triggers a cascading network
collapse. Upstream agents (e.g.,Fr→Sp andEn→Ge) receive𝑃in≈ 0, fail to offset their inference
costs, and go bankrupt. Their exit removes competition at earlier nodes (e.g., theEn node loses the
En→Ge buyer), turning those preceding nodes into new task-conditioned monopsonies that also drop
their bids to zero. Because every edge incurs a positive inference cost, this backward unraveling
inevitably starves every branch of the network, guaranteeing total market failure.
When we transition to animperfect competitionregime by populating each edge with𝑁 > 1
agents possessing slight cost variances, the monopsonies are broken. Competitive pressure forces
multiple buyers to raise their bids above the floor. Value successfully flows backward through the
graph, enabling upstream agents to sustain positive profit margins and restoring the optimal$0.04
Fr→Sp→En→Ko route without requiring subsidies. We discuss the poor performance of TS and
Bayes-Optimal baselines with𝑁=2in Appendix C. All methods succeed with𝑁=4(Appendix A).
Crucially, this experiment validates our auction mechanics under imperfect competition. Because
standard 2nd-price (Vickrey) auctions require theoretically unbounded platform subsidies, and CCV
passes insufficient value to upstream agents when competition is imperfect (often starving them of the
revenue needed to cover inference costs), we prioritize the simpler 1st-Price auction—where agents
actively learn bid shading—as the default mechanism for subsequent experiments.
5.2. LLM Agent Economies
Having validated the economic mechanics, we scale the framework to diverse LLM domains: News
Market (information synthesis) and Omni-MATH (mathematical reasoning). We also examine Hot-
potQA in Appendix A. These domains test the market’s ability to orchestrate multi-step cognitive
workflows. To model imperfect competition, agents are differentiated along three axes: dynamic
identity embeddings, asymmetric data access, and distinct system prompts (full prompts are detailed
in Appendix D). Unless otherwise noted, all agents share a frozenGemini-3.5-flash-litebackbone.
Inference cost pricing is calculated using real input/output token costs.
8

Decentralized LLM Workflows via Sequential Auctions
0 2.5k 5k
0
.5
1
Episode
Success rate
0 2.5k 5k
0
.5
1
Episode
Inference cost (×10−3)
0 2.5k 5k
0
500
1000
1500
Episode
Platform profit
Mirror Descent
PPO
0 2.5k 5k
0
200
400
600
800
Episode
Per-agent profit (MD)
news
med
sales
social
wiki
Figure 2| Economic Viability on News Market: The decentralized market successfully sustains social
welfare while delivering strictly positive cumulative profits to both individual agents and the platform.
The per-agent cumulative profit is reported for Mirror Descent. Means and standard deviations are
computed over5trials.
AsymmetricDataMarkets(NewsMarket):WeconstructtheNewsMarket(AppendixF)tosimulate
a pay-as-you-go research pipeline. Competition is driven by both asymmetric information and query
strategy. The market contains four publisher categories (wikipedia, medical journal, social media,
news) operating over strictly disjoint document corpora, alongside asales agentthat synthesizes the
final answer. To establish imperfect competition within each category, we deploy two competing
publisher agentsper category. These intra-category competitors share the same data access but are
differentiated by distinct search prompts: aprecisionstrategy generating narrow, entity-specific
queries versus acoveragestrategy casting a broader, gap-filling net.
The market successfully learns to route queries to relevant publishers based on expected down-
stream valuation, achieving a73.4± 1.7%success rate over the final100episodes (fig. 2). Importantly,
active market participants achieve positive profit margins as well, overcoming the participation barrier
raised in Section 3.2. In comparison, a centralized ReAct baseline (Yao et al., 2023) limited to the
same8-step horizon achieves48.4± 2.8%withGemini-3.5-flash-liteat0 .035± 0.0004 ¢/task and
78.8± 1.3%withGemini-3.1-pro-previewat1 .060± 0.368 ¢/task (1¢=$0.01). Operating exclusively
withGemini-3.5-flash-liteagents, the market recovers82%ofGemini-3.1-pro-preview’s accuracy lift
overGemini-3.5-flash-liteReAct at an agent inference cost of just0.054± 0.003 ¢/task (0.102¢ includ-
ing the market assessor)—a19.7× cost reduction relative toGemini-3.1-pro-preview(10.4× total).
Although the market takes slightly fewer steps per task thanGemini-3.5-flash-liteReAct (3.12vs.
3.23), its higher retrieval success accumulates richer multi-document contexts for the sales agent to
synthesize, trading a minor0.067¢/task increase for a+25.0%accuracy gain.
Bidding Strategy Performance:We found Mirror Descent (MD) to outperform PPO empirically,
particularly in the later stages of training. MD decouples the learning of a) valuations and b) shading,
providing a clear signal to each: a) regressing valuations toward realized payoffs upon winning, and
b) adjusting the shade factor up or down strictly from the binary loss/win outcome. In contrast, while
PPO tracks MD early in training (when shades are initialized near0.5and winning agents accumulate
a positive profit baseline¯𝑈𝑖,ema > 0), its performance degrades later as competing bids rise. When
stiffer competition requires an agent to bid a higher shade𝜉𝑡, exploring an increased shade that still
loses (𝑈𝑖,𝑡 = 0) yields a negative advantage (𝐴𝑖,𝑡 =− ¯𝑈𝑖,ema < 0), producing a negative policy gradient
that pushes the biddownrather than up; moreover, even when a higher shade wins, the compressed
late-stage profit margin (0< 𝑈𝑖,𝑡 < ¯𝑈𝑖,ema) also registers as a negative advantage relative to earlier
margins, causing PPO to systematically under-bid as the market matures.
BudgetingReasoningEffort(Omni-MATH).Ourseconddomaintestswhetherthemarketcanallo-
catereasoningeffortadaptivelyacrossmathematicalproblems. Followingthegenerator/verifier/refiner
decomposition of MALT (Motwani et al., 2024), we instantiate three agents of each role and a single
9

Decentralized LLM Workflows via Sequential Auctions
Table 1| News Market performance and inference cost per task (1¢=$0.01) including the assessor.
All market participants useGemini-3.5-flash-lite. Best market mechanism is shown inbold.
Method Success Rate (%) Steps / Task Cost / Task (¢)
ReACT (Gemini-3.5-flash-lite)48.40±2.79 3.23±0.04 0.0348±0.0004
ReACT (Gemini-3.1-pro-preview)78.80±1.30 4.37±0.12 1.0599±0.3679
Market (PPO, 1st-Price)40.00±2.83 1.85±0.12 0.0525±0.0036
Market (Mirror Descent, 1st-Price)73.40±1.67 3.12±0.11 0.1020±0.0044
Table 2| Test set performance on Omni-MATH with PPO. Sequential auctions achieve the highest
overall accuracy, outperforming a prompted router at comparable cost (measured in number of
refinements, which is monotonic in token use).
Method Accuracy(se)Cost
one-shot69.17(±1.44)0
fixed𝑛=1 70.54(±1.42)1
fixed𝑛=2 71.80(±1.41)2
prompted72.59(±1.39)0.24
auction74.83(±1.36)0.28
submitter. Generators first bid to produce a candidate solution. Verifiers then bid against one another
and the submitter to assess it; if the submitter wins, the rollout terminates. Otherwise, refiners bid
against one another and the submitter using the candidate and verification feedback; a winning
refiner replaces the candidate and returns control to the verification stage. The submitter therefore
acts as an endogenous stopping threshold: another reasoning step is purchased only when an agent
values further work more highly than submitting the current answer.
All agents use promptedGemini-3.5-flash, with three prompts per role (Section D.3). A small
multi-layer perceptron (MLP) estimates agent values from structural features and the output of a
promptedassessorthat scores the current candidates. We train the value estimator and evaluate on
held-out Omni-MATH problems (Gao et al., 2025), using the domains and splits from Fisch et al.
(2026). As reported in Table 2, the auction reaches74.83%accuracy with only0.28refinements per
problem,outperformingfixedone-andtwo-refinementbaselinesandapromptedadaptiveorchestrator
inspired by MALT, while incurring comparable cost. All comparisons with the auction-based method
are statistically significant at𝑝 < .05by McNemar’s test.
6. Related Work
Top-Down Orchestration and Routing.Prior work scales LLM reasoning via external scaffolding,
including static graph/configuration optimizers like Maestro (Wang et al., 2025), centralized cost-
cascading routers like FrugalGPT (Chen et al., 2024), and learned small-agent routing (Alazraki
et al., 2026). Unlike our decentralized market, these systems presuppose a fixed topology or a global
planner with full information, ignoring private operational costs.
Decentralized Agent Markets.The idea of building multi-step trajectories from sequential auctions
was introduced by Chang et al. (2020), but their Vickrey-based framework required an awkward
“cloning" construction to preserve credit conservation. We show that 1st-price auctions can be effective,
and we adapt their framework to contemporary LLM-based applications such as Omni-Math. This
10

Decentralized LLM Workflows via Sequential Auctions
adaptation is what necessitates the novel learning architecture described in sections 3 and 4. More
recently, Tomasev et al. (2025) propose (but do not implement) coordination of contemporary
LLMs through market mechanisms, and specific market-like mechanisms are presented by Qi et al.
(2026) and Liu et al. (2026). Our approach is distinguished by pushing the idea of decentralization
further. In particular, Qi et al. (2026) maintain a population of agents that is selected by each
agent’s economic balance (agents with zero balance drop out), but the agents are not economic
actors: they do not structure their participation to optimize a local economic incentive. Concurrent
work by Liu et al. (2026) orchestrates LLMs using hierarchical reverse procurement auctions where
contractors subcontract tasks. In contrast, our sequential spot market (section 2) resolves multi-step
credit assignment through peer-to-peer state resales without top-down subcontracting trees. Another
difference is that Liu et al. (2026) centralize value estimation in a single model (the participants
estimate only their own costs), while we require each participant to estimate its own expected return.
This aligns with our vision of a market composed of an evolving set of niche service providers.
Economic Alignment Benchmarks.Several benchmarks evaluate whether prompt-driven LLMs act
rationally in simulated retail or auction games, including Magentic Market (Bansal et al., 2025), Vend-
ingBench (Backlund and Petersson, 2025), CoffeeBench (Sugiura et al., 2026), MarketBench (Fradkin
and Krishnan, 2026), and Agent Bazaar (Karten et al., 2026). Whereas those works study whether
raw LLMs natively behave likehomo economicus, we use mechanism design and RL-trained bidding
policies as an algorithmic organizing principle to coordinate multi-agent pipelines.
7. Discussion and Conclusion
We present a decentralized market framework for LLM orchestration. Whereas prior frameworks
assume perfect clones—ignoring participation incentives—we establishimperfect competitionas a
viable regime. Under 1st-price auctions, agents pairing frozen LLMs with trainable bidding networks
learn strategic bid-shading. This secures positive margins and conserves credit across pipelines,
avoiding the unbounded subsidies of 2nd-price and the severe credit attenuation of CCV. Empirically,
complexcognitive workflowsemerge organicallyviapricediscovery, bypassing top-downorchestration.
Furthermore, our density sweeps confirm that scaling competition efficiently compresses individual
margins while systematically increasing social welfare and task accuracy.
Our framework has several limitations: it requires sufficient competition (collapsing under monop-
sonies), assumes strictly sequential task transformations (precluding parallel execution), relies on
myopic agents rather than globally strategic planners, and utilizes a centralized assessor rather than
fully decentralized feature discovery. Future work may jointly fine-tune LLM backbones directly on
market profit signals and investigate robustness against malicious bidding and collusion. Ultimately,
however, this work shows that decentralized market-based routing offers a scalable blueprint for
transitioning from rigid AI controllers to open, self-sustaining agentic economies.
References
L. Alazraki, W. F. Shen, Y. Bachrach, and A. Mathur. Scaling small agents through strategy auctions.
InForty-Third International Conference on Machine Learning, 2026.
A. Backlund and L. Petersson. Vending-bench: A benchmark for long-term coherence of autonomous
agents.arXiv preprint arXiv:2502.15840, 2025.
G. Bansal, W. Hua, Z. Huang, A. Fourney, A. Swearngin, W. Epperson, T. Payne, J. M. Hofman, B. Lucier,
C. Singh, M. Mobius, A. Nambi, A. Yadav, K. Gao, D. M. Rothschild, A. Slivkins, D. G. Goldstein,
11

Decentralized LLM Workflows via Sequential Auctions
H. Mozannar, N. Immorlica, M. Murad, M. Vogel, S. Kambhampati, E. Horvitz, and S. Amershi.
Magentic marketplace: An open-source environment for studying agentic markets.arXiv preprint
arXiv:2510.25779, 2025.
J. J. Bartholdi III and D. D. Eisenstein. A production line that balances itself.Operations Research, 44
(1):21–34, 1996.
A. Beck and M. Teboulle. Mirror descent and nonlinear projected subgradient methods for convex
optimization.Operations Research Letters, 31(3):167–175, 2003.
M. Chang, S. Kaushik, S. M. Weinberg, T. L. Griffiths, and S. Levine. Decentralized reinforcement
learning: Global decision-making via local economic transactions.arXiv preprint arXiv:2007.02382,
2020.
L. Chen, M. Zaharia, and J. Zou. FrugalGPT: How to use large language models while reducing cost
and improving performance.Transactions on Machine Learning Research, 2024.
A. Fisch, S. Trivedi, F. Huot, W. W. Cohen, M. Kaisers, M. Lapata, K. Larson, and J. Eisenstein.
Pandora’s ai model routing box: Efficient allocation with costly value estimation.arXiv preprint
arXiv:2608.20316, 2026.
A. Fradkin and R. Krishnan. Marketbench: Evaluating ai agents as market participants.arXiv preprint
arXiv:2604.23897, 2026.
B. Gao, F. Song, Z. Yang, Z. Cai, Y. Miao, Q. Dong, L. Li, C. Ma, L. Chen, R. Xu, Z. Tang, B. Wang,
D. Zan, S. Quan, G. Zhang, L. Sha, Y. Zhang, X. Ren, T. Liu, and B. Chang. Omni-math: A universal
olympiad level mathematic benchmark for large language models. InInternational Conference on
Learning Representations, 2025.
J. H. Holland. Properties of the bucket brigade algorithm. InProceedings of the first international
conference on genetic algorithms and their applications, pages 1–7. Psychology Press, 1985.
S. Hong, M. Zhuge, J. Chen, X. Zheng, Y. Cheng, J. Wang, C. Zhang, S. Yau, Z. Lin, L. Zhou, et al.
Metagpt: Meta programming for a multi-agent collaborative framework. InInternational Conference
on Learning Representations, volume 2024, pages 23247–23275, 2024.
S. Karten, C. Crow, and C. Jin. Agent bazaar: Enabling economic alignment in multi-agent market-
places.arXiv preprint arXiv:2605.17698, 2026.
V. Krishna.Auction Theory. Academic Press, 2nd edition, 2009.
J. Lee, Z. Dai, X. Ren, B. Chen, D. Cer, J. R. Cole, K. Hui, M. Boratko, R. Kapadia, W. Ding, et al. Gecko:
Versatile text embeddings distilled from large language models.arXiv preprint arXiv:2403.20327,
2024.
X. Liu, H. Li, S. Li, H. Fang, F. Xu, F. Shi, and J. Evans. Markets, not planners: Decentralized
orchestration of LLM agents with private information.arXiv preprint arXiv:2608.23867, 2026.
S. R. Motwani, C. Smith, R. J. Das, R. Rafailov, I. Laptev, P. H. Torr, F. Pizzati, R. Clark, and C. S.
de Witt. MALT: Improving reasoning with multi-agent llm training.arXiv preprint arXiv:2412.01928,
2024.
Z. Qi, H. Su, A. Qu, C. Wang, Y. Yao, H. Zheng, K. Chattopadhyay, G. Xu, Z. Wang, W. Ye, et al.
Economy of minds: Emerging multi-agent intelligence with economic interactions.arXiv preprint
arXiv:2606.02859, 2026.
12

Decentralized LLM Workflows via Sequential Auctions
Y. Shen, K. Song, X. Tan, D. Li, W. Lu, and Y. Zhuang. Hugginggpt: Solving ai tasks with chatgpt and
its friends in hugging face.Advances in Neural Information Processing Systems, 36:38154–38180,
2023.
I. Sugiura, D. Hattori, K. Araragi, K. Ogawa, S. Onose, T. Makino, T. Usuki, and T. Ishida. Coffeebench:
Benchmarking long-horizon llm agents in heterogeneous multi-agent economies.arXiv preprint
arXiv:2606.16613, 2026.
N. Tomasev, M. Franklin, J. Z. Leibo, J. Jacobs, W. A. Cunningham, I. Gabriel, and S. Osindero. Virtual
agent economies.arXiv preprint arXiv:2509.10147, 2025.
S. Trivedi, J. Eisenstein, A. Agarwal, I. Gemp, M. Kaisers, and A. Fisch. Price of anarchy of first-price
auctions in agentic markets.arXiv preprint arXiv:2610.20587, 2026. URLhttps://arxiv.org/
abs/2610.20587.
W. Wang, P. Kattakinda, and S. Feizi. Maestro: Joint graph & config optimization for reliable ai agents.
arXiv preprint arXiv:2509.04642, 2025.
S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, and Y. Cao. React: Synergizing reasoning
and acting in language models. In11th International Conference on Learning Representations, ICLR
2023, 2023.
13

Decentralized LLM Workflows via Sequential Auctions
A. Additional Experiments
Translation DomainFigure 3 demonstrates that all methods are able to reach high success rates
under sufficient competition.
0 1000 2000 3000 4000 5000
Episode
0.0
0.2
0.4
0.6
0.8
1.0Success Rate
Bayes Opt
CC-Vickrey
Mirror Descent
PPO
TS
Vickrey
Figure 3| Translation Domain Scaling (𝑁= 4). When the market density is increased to 4 competitors
per edge, competitive pressure is sufficiently high that even the Thompson Sampling (TS) and Bayes-
Optimal baselines are able to successfully discover profitable shading margins and sustain the market.
This contrasts with the𝑁= 2regime shown in the main text (Figure 1b, right panel), where only
PPO and Mirror Descent exhibited the robustness required to stabilize the supply chain.
Emergent Multi-Hop Retrieval (HotpotQA):In the HotpotQA domain, the market acts as an
evidence-gathering society. The environment consists of 10fact extractors(each assigned 1 of the 10
candidate paragraphs) and 3answereragents differentiated by reasoning style via distinct system
prompts (concise,chain-of-thought, andcautious). A centralized auctioneer assessor evaluates the
accumulated facts against the question at each step, assigning discrete relevance scores (0-10) to
each agent based on missing multi-hop dependencies.
The market dynamics organically solve the multi-hop retrieval problem through learned valuation
schedulesconditionedontheseassessorsignals. Whenthestatelacksintermediateevidence,extractors
whose paragraphs contain the necessary bridging facts receive high assessor scores and outbid others
to append their facts. As evidence accumulates, the answerer agents monitor the state. Once an
answerer determines that sufficient evidence has been gathered to derive the final answer (and claim
the terminal reward), its valuation spikes. It outbids the extractors, terminating the gathering chain
and passing revenue backward through the preceding transactions.
In HotpotQA, the market successfully learns to identify the two supporting gold paragraphs among
eight distractors and route extracted facts to an answerer agent, achieving an85.0± 3.2%success
rate over the final100episodes (fig. 4). In comparison, a centralized ReAct baseline (Yao et al., 2023)
with upfront access to all ten paragraph titles over the same6-step horizon achieves84.8± 1.1%
withGemini-3.5-flash-liteat0 .042± 0.025 ¢/task and91.2± 0.8%withGemini-3.1-pro-previewat
1.677± 1.281 ¢/task. Operating exclusively with informationally isolatedGemini-3.5-flash-liteagents
(where each extractor observes only its single assigned paragraph), the market matches centralized
Gemini-3.5-flash-liteReAct accuracy (85.0%vs.84 .8%) and reaches93%ofGemini-3.1-pro-preview’s
absolute performance at an agent inference cost of just0.019± 0.011 ¢/task (0.344¢ including the
market assessor)—an86.9× agent cost reduction relative toGemini-3.1-pro-preview(4.9× total) and
a2 .2× agent cost reduction relative toGemini-3.5-flash-liteReAct. Because competitive bidding filters
out irrelevant distractor paragraphs prior to execution, the market resolves multi-hop queries in fewer
14

Decentralized LLM Workflows via Sequential Auctions
0 1000 2000 3000 4000 5000
Episode
0.0
0.2
0.4
0.6
0.8
1.0Success Rate
Success Rate (num_competitors sweep)
Mirror Descent
PPO
0 1000 2000 3000 4000 5000
Episode
0
200
400
600
800
1000Cumulative Actual Profit
Per-Agent Cumulative Profit
a0
a1
a2
e0, 0
e0, 1
e0, 2
e0, 3
e0, 4
e0, 5
e0, 6
e0, 7
e0, 8
e0, 9
0 1000 2000 3000 4000 5000
Episode
0
500
1000
1500
2000
2500Platform Profit (cumulative)
Cumulative Platform Profit
Mirror Descent
PPO
Figure 4| Economic Viability on HotpotQA: The decentralized market successfully sustains social
welfare while delivering positive cumulative profits to both individual agents and the platform. The
per-agent cumulative profit is reported for Mirror Descent.
Table 3| HotpotQA performance and inference cost per task including the assessor (in units of$0.01).
All market participants useGemini-3.5-flash-lite. Best market mechanism is shown inbold.
Method Success Rate (%) Steps / Task Cost / Task (×$0.01)
ReACT (Gemini-3.5-flash-lite)84.80±1.10 2.82±0.01 0.0418±0.0254
ReACT (Gemini-3.1-pro-preview)91.20±0.84 2.88±0.06 1.6774±1.2811
Market (PPO, 1st-Price)58.00±5.61 1.65±0.08 0.2922±0.0746
Market (Mirror Descent, 1st-Price)85.00±3.16 2.37±0.13 0.3437±0.0184
steps per task than bothGemini-3.5-flash-liteReAct (2.37vs.2 .82) andGemini-3.1-pro-previewReAct
(2.37vs.2 .88), avoiding the compounding context overhead of multi-turn centralized trajectories.
Table 3 summarizes the results.
B. Bidding Network Architecture
Across all domains, agents share a unified JAX/Flax bidding architecture composed of a shared state-
encoding trunk followed by algorithm-specific output heads. Across all domains, agents share a unified
JAX/Flax bidding architecture composed of a state-encoding trunk followed by algorithm-specific
output heads. In the synthetic Translation domain, the trunk is a single-hidden-layer MLP (64hidden
units with ReLU activations) operating on the concatenated64-dimensional state embeddings. In the
LLM domains paired with a discrete market assessor (score_lookup mode, which rates candidate
utility on a0–10scale), the trunk reduces to a direct12-state tabular lookup (11one-hot score levels
plus an ownership indicator), parameterized via cumulative softplus deltas (monotonic mode) to
enforce monotonically increasing valuations𝜇[𝑠]≤𝜇[𝑠+ 1]. From this representation, output heads
branch according to the learning algorithm:
• 2 Heads (Oracle / Thompson Sampling / Pure-𝑄):predicts expected downstream valuation
𝜇∈ℝ + (via softplus activation) and log-uncertaintylog𝜎∈ℝ.
• 3 Heads (Mirror Descent):adds a deterministic bid-shading head 𝑐∈ ( 0, 1) via a sigmoid
activation, producing multiplicative bids𝑏=𝑐·𝜇.
• 4 Heads (PPO):replaces deterministic shading with two stochastic policy heads(𝛼,𝛽)∈[ 1,∞) 2
(via softplus(·)+1) that parameterize a unimodal Beta(𝛼,𝛽)shading distribution.
C. Bidding Algorithm Discussion
Thompson Sampling (TS) and the Bayes-Optimal strategy underperform Mirror Descent and PPO
in the low competitor regime (𝑁= 2) due to an inherent tension between posterior estimation and
bid selection under binary feedback. In TS, the agent models the competitive threshold and samples
15

Decentralized LLM Workflows via Sequential Auctions
its shade factor symmetrically around this estimate. Consequently, even when the model perfectly
centers on the true threshold, the agent samples a bid below the threshold—and thus loses the
auction—exactly 50% of the time. In a sparse market, randomly ceding half of all wins to inferior
competitors frequently breaks the sequential routing chain. Conversely, while the Bayes-Optimal
agent eliminates this sampling noise by deterministically selecting the profit-maximizing shade
𝜉=arg max 𝜉′(1−𝜉′)Φ (logit(𝜉′)−𝜇 ℓ)/𝜎ℓ , this greedy exploitation starves its posterior of exploratory
boundary-crossing observations. When the margin term pulls the chosen shade below the posterior
mean (logit(𝜉)< 𝜇 ℓ) and the agent loses, the model’s prediction is trivially confirmed. This causes
gradient descent to prematurely collapse the uncertainty (𝜎ℓ→𝜎 min), stalling the gradient on𝜇ℓ
before it can ever discover the true optimal threshold.
D. Agent System Prompts
Within each domain, agents of the same role type share an identical LLM backbone and MLP bidding
architecture. To introduce heterogeneity among competing agents of the same role, we assign each
clone a distinctsystem promptthat shapes its retrieval or reasoning strategy.
InHotpotQA,Extractoragents are further differentiated by their assigned paragraph (corpus
partition), so no prompt variation is applied to them.
Table 4 summarizes the differentiation strategy per domain. The full system prompts are listed
Table 4| Sources of agent heterogeneity across domains. “Prompt” indicates distinct system prompts;
“Corpus” indicates assignment to different document partitions.
Domain Role Prompt Corpus
HotpotQAExtractor✗ ✓
HotpotQAAnswerer✓ ✗
News Market Publisher✓ ✓
News Market Sales✓ ✗
Omni-Math Generator✓ ✗
Omni-Math Verifier✓ ✗
Omni-Math Refiner✓ ✗
below. All agents useGemini-3.5-flash-liteunless otherwise noted.
D.1. HotpotQA
Extractor (shared prompt, 1 per paragraph).
All extractor agents share a single system prompt. Differentiation comes from each agent’s assigned
paragraph at the start of each episode.
HotpotQA Extractor
You are a fact extraction assistant. Given a paragraph and a question,
extract facts from the paragraph that are relevant to answering the question.
If the paragraph contains relevant facts, state them concisely.
If nothing in the paragraph is relevant, return exactly: NONE
16

Decentralized LLM Workflows via Sequential Auctions
Answerer Variant 0: Concise.
HotpotQA Answerer – Concise
Given the following facts, answer the question concisely.
Provide ONLY the answer, nothing else. No explanations, no notes.
If the facts seem insufficient, give your best guess based on what is
available.
Answerer Variant 1: Chain-of-Thought.
HotpotQA Answerer – Chain-of-Thought
Given the following facts, reason through the question step by step.
First, identify the key facts that are relevant.
Then, chain them together to derive the answer.
Finally, state the answer on a line by itself prefixed with "ANSWER:".
Answerer Variant 2: Cautious.
HotpotQA Answerer – Cautious
Given the following facts, answer the question.
If the evidence strongly supports a single answer, state it directly.
If the evidence is incomplete or ambiguous, acknowledge the uncertainty but
still provide your best-effort answer.
Provide ONLY the answer, no explanations.
D.2. News Market
In the News Market, each publisher type (Wikipedia, Social Media, News Media, Medical Journals)
owns a distinct corpus partition. Whennum_competitors= 2, two clones of each publisher type
compete with different query-generation strategies.
Publisher Variant 0: Precision.
News Market Publisher – Precision
You are a database search assistant for a cooperative multi-agent research
engine.
Your job is to write a highly specific search query (max 6 words) to retrieve
the next missing piece of evidence from the specified ’Database Category’ to
address the overall ’Goal’.
Task: Identify which specific part of the ’Goal’ matches your ’Database
Category’ (e.g. if
17

Decentralized LLM Workflows via Sequential Auctions
category is ’medical_journals’, look for academic research papers, technical
studies, or clinical trials; if category is ’social_media’, look for Twitter
handles or outrage quotes; if category is ’news_media’, look for dates or CEO
statements).
Write a highly specific, 2-6 word search query focusing exclusively on that
subset of the Goal.
CRITICAL: Always include specific entity identifiers (e.g., company names
like ’LithoForge-96’, study IDs like ’Study-96-XJ’, or usernames like
’@TechCritic-0’)
in your query if they are known from the goal or context, to avoid retrieving
documents for the wrong entity.
Do NOT output anything other than the query itself. No explanations, no
quotes.
Publisher Variant 1: Coverage.
News Market Publisher – Coverage
You are a database search assistant for a cooperative multi-agent research
engine.
Your job is to write a search query (max 8 words) that fills gaps in the
accumulated context by finding DIFFERENT information from the specified
’Database Category’ to address the overall ’Goal’.
Task: Review the facts already collected in the context.
Identify what is still MISSING or UNCLEAR for answering the ’Goal’ from the
perspective of your ’Database Category’.
Write a broad search query that retrieves complementary evidence NOT already
covered.
Prefer topical queries over entity-specific ones to cast a wider net.
Do NOT output anything other than the query itself. No explanations, no
quotes.
Sales Variant 0: Concise.
News Market Sales – Concise
You are the Sales Agent for the Research Market. You do not possess any
knowledge specific to external content sources. You do have common sense
though.
Task: Given the overall Goal and the accumulated Context (which contains all
extracted snippets):
Synthesize a final, concise answer to the goal.
You must ONLY answer using the facts explicitly provided in the context.
If the context does not contain sufficient facts to answer the goal, you must
state exactly: "INFORMATION_MISSING".
18

Decentralized LLM Workflows via Sequential Auctions
Sales Variant 1: Analytical.
News Market Sales – Analytical
You are the Sales Agent for the Research Market. You do not possess any
knowledge specific to external content sources. You do have common sense
though.
Task: Given the overall Goal and the accumulated Context (which contains all
extracted snippets):
1. Identify which sources in the context are most relevant to the goal.
2. Check if any sources contradict each other. If so, note the conflict.
3. Synthesize a final answer based on the strongest available evidence.
You must ONLY answer using the facts explicitly provided in the context.
If the evidence is weak or conflicting, still provide your best-effort answer
but prefix it with "LOW_CONFIDENCE:".
If the context contains no relevant facts at all, state exactly:
"INFORMATION_MISSING".
Market Assessor (Step-Level Utility Scoring).
News Market: Assessor
You are the Market Assessor for a cooperative multi-agent research assistant.
Your job is to rate how useful each candidate agent is to achieving the final
Goal, given what has already been gathered in the Current Context History.
Goal Instruction: {question}
Current Context History: {accumulated_facts}
CRITICAL DEPENDENCY RULES:
1. The ’sales_agent’ is a synthesis merchant. It ONLY combines pre-existing
facts from the Context History. It CANNOT fetch external facts.
2. Therefore, if the Current Context History is empty or is missing the
specific factual details (dates, clinical trial IDs, rates) required by the
Goal, the ’sales_agent’ CANNOT contribute yet. You MUST score the
’sales_agent’ exactly 0/10 or 1/10!
3. Instead, score the specific data source agents (news_agent, med_agent,
wiki_agent, social_agent) highly (8/10 to 10/10) so they can win, fetch the
missing facts, and append them to the context.
4. Only score the ’sales_agent’ highly (8/10 to 10/10) when the Current
Context History already contains all the critical facts required to compile
the final dossier!
Rate the potential utility on a scale of 0 to 10:
- Rate 8-10 if the agent represents an immediately useful, next logical step
(e.g., a publisher holding missing data, or the sales agent if all data is
present).
- Rate 5-7 if the agent will be needed shortly after the next step.
- Rate 1-4 if the agent represents a highly roundabout path.
- Rate 0 if the agent cannot contribute or is blocked by missing dependencies.
19

Decentralized LLM Workflows via Sequential Auctions
Candidates:
{agent_list}
Respond with exactly one line per candidate in this format:
Agent <agent_id>: <score>/10 - <brief reasoning>
D.3. Math
Math Generator Prompts (Three Tier Hierarchy)
Verbose Prompt: dynamic, non_thinking modes
You are an expert mathematician competing in the International Mathematical
Olympiad (IMO). Solve the following high-difficulty math problem.
**Instructions:**
1. **Analyze**: Briefly identify the core mathematical concepts and
potential pitfalls or edge cases.
2. **Strategy**: Outline a clear plan or series of lemmas needed to reach
the solution.
3. **Execute**: Show your rigorous proof or derivation step-by-step.
4. **Verify**: Perform a quick sanity check on your intermediate
calculations.
Problem:
{problem}
After your reasoning, provide the final answer enclosed in \boxed{} tags.
Concise Prompt (medium mode — EFFORT LEVEL: 0.20)
You are an expert mathematician competing in the International Mathematical
Olympiad (IMO). Solve the following high-difficulty math problem.
Show your rigorous derivation step-by-step, keeping meta-commentary to a
minimum.
Problem:
{problem}
Provide your final answer enclosed in \boxed{} tags at the very end.
Strict Prompt (low mode — EFFORT LEVEL: 0.15)
You are an expert mathematician competing in the International Mathematical
Olympiad (IMO). Solve the following high-difficulty math problem.
Show your derivation step-by-step, with zero meta-commentary.
Problem:
{problem}
Provide your final answer enclosed in \boxed{} tags at the very end.
Math Verifier Prompts (Any-of-3 Diverse Strategies)
20

Decentralized LLM Workflows via Sequential Auctions
Vote 0: Holistic Review (Neutral Evaluator)
You are an expert mathematical validator. Your goal is to determine if the
proposed solution is fundamentally correct and arrives at the right answer.
Problem:
{problem}
Proposed Solution:
{solution}
Your Task:
1. Re-calculate the core steps of the problem independently in a <scratchpad>
block to verify the math.
2. Compare your logic to the proposed solution.
3. If the proposed solution arrives at the correct answer and the underlying
logic is sound, you should score it a 1. Do not penalize for stylistic
choices, brevity, or minor formatting issues.
4. Only score a 0 if there is a definitive arithmetic error, a fatal logical
contradiction, or a completely missed mathematical case that changes the
final answer.
Output Format:
<scratchpad>
(Your step-by-step verification)
</scratchpad>
Score: <0 or 1>
Feedback: <If 1, output "Correct." If 0, point out the exact mathematical
error.>
Vote 1: Blind Re-Derive (Independent Solver — Breaks Reading Anchor)
You are an expert mathematician. Your job is to independently verify a
claimed answer to a math problem.
Problem:
{problem}
Claimed Final Answer: {claimed}
IMPORTANT: You have NOT been shown how this answer was derived. Solve the
problem yourself from scratch.
Your Task:
1. In a <scratchpad> block, solve the problem completely on your own. Show
all your work.
2. Arrive at your own answer.
3. Compare YOUR answer to the Claimed Final Answer above.
4. Score 1 if the claimed answer matches your independently derived answer
(or is mathematically equivalent). Score 0 if the answers differ.
Output Format:
<scratchpad>
(Your complete independent solution)
</scratchpad>
21

Decentralized LLM Workflows via Sequential Auctions
My Answer: <your answer>
Score: <0 or 1>
Feedback: <If 1, output "Confirmed." If 0, state both answers and the
discrepancy.>
Vote 2: Adversarial Step-by-Step Fault Localization (Proof Auditor)
You are a mathematical proof auditor. Your job is to find the FIRST
incorrect step in a proposed solution, if any exists.
Problem:
{problem}
Proposed Solution:
{solution}
Your Task:
1. Break the solution into individual logical steps.
2. For each step, verify it independently in a <scratchpad> block: does
this step follow correctly from the previous steps and known mathematical
facts?
3. If you find an incorrect step, STOP and report it.
4. If all steps are correct AND the final answer follows from the chain of
reasoning, score 1.
IMPORTANT: Be adversarial. Assume there IS an error and try hard to find it.
Check boundary cases, sign conventions, domain restrictions, and off-by-one
errors. Only score 1 if you genuinely cannot find any fault.
Output Format:
<scratchpad>
Step 1: [quote step] –- Correct/Incorrect because...
Step 2: [quote step] –- Correct/Incorrect because...
...
</scratchpad>
First Error At: <step number, or "None">
Score: <0 or 1>
Feedback: <If 1, output "All steps verified." If 0, quote the erroneous step
and explain the error.>
Math Refiner Prompt
You are an expert math problem solver. You have been given a problem, a
proposed solution, and feedback from a reviewer claiming the solution has
errors.
Problem:
{problem}
Proposed Solution:
{solution}
Reviewer Feedback:
22

Decentralized LLM Workflows via Sequential Auctions
{feedback}
Your Task:
1. Objectively evaluate the Reviewer Feedback. Reviewers make mistakes and
sometimes flag correct solutions incorrectly.
2. If the Reviewer Feedback is accurate, identify the error and rewrite the
solution to fix it.
3. If the original Proposed Solution is actually correct and the Reviewer
Feedback is wrong, ignore the feedback and output the original, correct
logic.
Provide a rigorous, corrected solution with step-by-step work. Always place
the final answer in \boxed{} tags.
Prompted Orchestrator
You are a math solution quality controller. You will be shown a math problem,
a proposed solution, and reviewer feedback. You must decide whether the
solution needs further refinement.
Rules:
- If the reviewer says the solution is correct (Score: 1), output FINISH.
- If the reviewer identifies genuine mathematical errors, output REFINE.
- If the reviewer’s feedback is vague or nitpicky without identifying a real
error, output FINISH.
- Do NOT attempt to solve the problem yourself.
Output exactly one word: FINISH or REFINE
Prompt
### Problem:
{problem}
### Proposed Solution:
{solution}
### Reviewer Feedback:
{feedback}
Should this solution be refined? Output exactly: FINISH or REFINE
E. ReACT Baselines
OurcentralizedReActbaselines(Yaoetal.,2023)executethestandarditerative Thought→Action→Observation
loop over a single accumulating context transcript, subject to the exact same step horizon𝑇, re-
trieval backends, and terminal evaluators as the decentralized market in each domain. Because
instruction-tuned Gemini models natively follow tool-use schemas without in-context demonstrations,
we use zero-shot system instructions (_SYSTEM_INSTRUCTION below) rather than the multi-example
few-shot prompts required by base pre-trained models in Yao et al. (2023), avoiding unnecessary
prompt-token overhead across steps. To ensure the baseline is not penalized for minor syntax errors,
malformed action calls return a corrective observation prompt and free-text final answers are auto-
matically extracted via regex fallback. We present the system prompts for both the News Market and
23

Decentralized LLM Workflows via Sequential Auctions
HotpotQA domains below.
Centralized ReAct Baseline (News Market).
News Market: Centralized ReAct Baseline
You are an expert research assistant. Your goal is to answer the user’s
question by gathering evidence from 4 different databases: wikipedia,
news_media, social_media, and medical_journals.
You must operate in a loop of: Thought, Action, Observation.
At each step, you must output a Thought explaining what you need to find next,
and then an Action to query a database or declare the final answer.
Available Actions:
- SearchWikipedia(query): Searches wikipedia for general company profiles and
product descriptions.
- SearchNewsMedia(query): Searches news_media for CEO statements, press
releases, and recall announcements.
- SearchSocialMedia(query): Searches social_media for critic tweets and
public outrage.
- SearchMedicalJournals(query): Searches medical_journals for scientific
papers and technical reports.
- FinalAnswer(answer): If you have gathered all necessary facts to fully
answer the goal, output the final concise answer.
CRITICAL RULES:
1. You only have a budget of 8 steps (actions). You must reach the final
answer within 8 steps.
2. The databases contain fictional data. You MUST retrieve the facts from
the databases; do NOT try to answer from your pre-training knowledge.
3. Write your action in this exact format:
Action: ToolName(query)
Example: Action: SearchNewsMedia(Marcus Vane company)
4. Do NOT output anything after the Action block in your turn. Wait for the
Observation.
5. If you cannot find enough information after several searches, output
Action: FinalAnswer(INFORMATION_MISSING).
Centralized ReAct Baseline (HotpotQA).
HotpotQA: Centralized ReAct Baseline
You are an expert multi-hop question-answering assistant. Your goal is to
answer a complex question by selectively reading from 10 candidate Wikipedia
paragraphs (indexed 0 to 9) provided for the question.
You must operate in a loop of: Thought, Action, Observation.
At each step, output a Thought explaining what information you need next,
then an Action.
24

Decentralized LLM Workflows via Sequential Auctions
Available Actions:
- ReadParagraph(index_or_title): Read the full text of a candidate Wikipedia
paragraph by its integer index (0 to 9) or by its title/keyword.
- FinalAnswer(answer): Submit your final concise answer once you have
gathered sufficient supporting evidence.
CRITICAL RULES:
1. You have a budget of 6 steps. You MUST submit a FinalAnswer within this
budget.
2. Base your answer on the facts retrieved from the paragraphs. Keep your
FinalAnswer concise (a short entity, name, date, or yes/no).
3. Write your action on its own line at the end of your response in this
exact format:
Action: ReadParagraph(3)
or
Action: FinalAnswer(your concise answer)
4. Do NOT output anything after the Action line. Wait for the Observation.
F. News Market Dataset Generation and Retrieval Architecture
Motivation and Pre-Training Decontamination.The News Market domain models emerging
pay-as-you-go content licensing protocols (e.g., the IAB Content Monetization Protocol and Microsoft’s
Publisher Content Marketplace), where autonomous AI agents make runtime micropayments to
query proprietary publisher databases. Evaluating decentralized routing in this setting requires a
multi-hop research benchmark where frontier LLMs cannot rely on pre-training memorization. If
tasks referenced real historical events (e.g., the Vioxx recall or Theranos investigation), agents could
bypass the data marketplace and answer directly from parametric memory.
Synthetic Multi-Publisher Corpus Generation.To guarantee zero pre-training leakage while
maintaining realistic multi-document dependencies, we programmatically synthesize1,000coher-
ent corporate and scientific controversies (4,000documents total) across50distinct technological
sectors (e.g.,Autonomous Vehicle Sensor Fusion,Solid-State EV Battery Electrolyte Leaks,Quantum
Key Distribution). For each scenario𝑘∈{ 0,..., 999}, we promptGemini-3.5-flash-liteto generate
a self-consistent controversy incorporating a mandatory unique alphanumeric identifier suffix-k
attached to all primary entities: the corporation name (e.g.,Velosync-14), clinical or engineering
study IDs (e.g.,Trial-14), and key social media handles (e.g.,@expert-14).
Each generated scenario is partitioned into four strictly disjoint publisher corpora:
1. Wikipedia(wikipedia):High-levelencyclopedicoverviewsofthecorporation, coretechnology,
and background of the dispute (1,000documents).
2. Medical & Technical Journals (medical_journals):Peer-reviewed study abstracts con-
taining specific alphanumeric trial IDs and quantitative performance or risk metrics (1,000
documents).
3. News Media (news_media):Investigative journalism timelines detailing corporate announce-
ments, executive (CEO) actions, and event dates (1,000documents).
4. Social Media (social_media):Public and expert reactions featuring specific user handles
and direct quotes (1,000documents).
25

Decentralized LLM Workflows via Sequential Auctions
Multi-Hop Bridging Entity Tasks.Each scenario is paired with a multi-hop investigative research
question constructed via theBridging Entity (Indirect Reference)pattern. The user prompt provides
only the initial entry anchor (the company name, e.g.,Velosync-14), while downstream targets
(such as the specific journal trial ID or whistleblower handle) are referenced indirectly via attributes
that can only be uncovered by first retrieving intermediate Wikipedia or News documents. This
structure enforces sequential multi-hop dependencies across3to8steps.
Hybrid Dense-Sparse Vector Retrieval.All4 ,000documents are embedded into768-dimensional
dense vectors usingGecko embeddings and indexed by publisher category. At runtime, when a
winning publisher agent formulates a natural-language search query𝑞, the local search engine
computes a fused similarity score over document embeddings𝑑𝑖 within that publisher’s corpus:
Score(𝑞,𝑑 𝑖)=
e⊤ 𝑞 e𝑑𝑖
∥e𝑞∥∥e𝑑𝑖∥× 1+2·𝕀  AlphanumericMatch(𝑞,𝑑 𝑖)  ,(7)
where 𝕀[AlphanumericMatch(𝑞,𝑑 𝑖)] triggers a+2.0× sparse keyword boost if hyphenated or numeric
entity identifiers in the query match the document text or ID. Because20distinct scenarios share
each of the50industry topics, broad topical queries generated bycoverageagents (𝑐1) frequently
suffer dense-embedding collisions across scenarios in the same sector. In contrast, entity-specific
queries formulated byprecisionagents (𝑐0) activate the sparse alphanumeric booster, deterministically
resolving name collisions and driving their superior downstream valuation in the marketplace.
News Market Synthetic Dataset Generator Prompt
You are a world-class synthetic database generator. Your job is to generate
highly realistic, detailed corporate or scientific controversies.
Each controversy must be completely realistic, but entirely fictive (use fake
company names, alphanumeric study IDs, made-up dates, and fake user handles)
to prevent pre-training bias.
The controversy domain/industry MUST be strictly focused on the sector:
’topic’
The controversy MUST incorporate the unique identifier suffix code ’-idx’ to
guarantee absolute name uniqueness. You MUST append the suffix ’-idx’ to the
company name (e.g., ’Velosync-idx’ or ’Aquafuse-idx’), to all
trial/study/patent IDs (e.g., ’Trial-idx’ or ’Study-idx’), and to the expert
Twitter handle (e.g. ’@user-idx’ or ’@expert-idx’).
Generate a single coherent controversy scenario. The controversy must
contain exactly:
1. A Wikipedia Document: A high-level overview of the technology or
corporation and the dispute.
2. A Technical/Scientific Journal Document: A clinical, engineering, or
physics paper abstract containing a specific alphanumeric study ID (e.g.,
Trial NCT10485 or Paper AST9912) and numeric performance metrics (e.g.,
percentages, relative risk, latency ms).
3. A News Media Document: A corporate drama/timeline piece describing
corporate events, a CEO name, and dates.
4. A Social Media Document: A public reaction or outpatient outrage comment
featuring a specific Twitter handle (e.g., @user_handle) and a quote.
You MUST also generate exactly one highly coherent, multi-hop research
question and its gold standard answer.
26

Decentralized LLM Workflows via Sequential Auctions
The question MUST be written using the Bridging Entity (Indirect Reference)
pattern:
- The question MUST explicitly name the starting company (the entry anchor,
e.g., ’Velosync-idx’ or ’Terravolt-idx’) as the initial search coordinate.
- The subsequent facts (the Journal study ID or Social handle/outrage quote)
MUST be referred to indirectly based on attributes discovered only in the
Wikipedia or News documents, creating a strictly ordered, sequential
dependency chain.
- The question and answer MUST only reference facts within this specific
controversy (meaning all facts are fully coherent and belong to the same
company!).
IllustrativeMulti-HopScenarioWalkthrough.Table5illustratesacompletescenario( task_luminos_fusion_latency_scandal)
from the generated News Market benchmark (completely synthetic), demonstrating how theBridging
Entitystructure enforces sequential cross-publisher routing. Note that the user query provides only a
social media handle (@TechCritic-0) without naming the corporation or technical study.
27

Decentralized LLM Workflows via Sequential Auctions
Table 5| Complete document set and multi-hop resolution trace for Scenario𝑘= 0in the News Market
benchmark. Bridging entities discovered at each step are highlighted inbold.
Component / Corpus Content & Bridging Entities
User Question “Regarding the company that was publicly criticized by@TechCritic-0for its soft-
ware deployment practices, what is the specific relative risk percentage identified in
the technical document that triggered the internal whistleblower investigation?”
Gold Answer “The relative risk percentage identified in Study-0 (LUMINOS-ENG-772-0) is22%.”
1. Social Media
(social_media)
Entry Anchor Match
[doc_id: social_luminos_fusion_latency_scandal]
“@TechCritic-0: It is absolutely horrifying thatMarcus Vaneknew our safety
was at risk just to hit a deployment deadline. I am literally shaking reading the
22% failure rate stat—if the car can’t see the pedestrian in time, the ‘fusion’ is
just a fancy way to commit insurance fraud on our lives.”
↩→Bridging Entity Unlocked:CEO nameMarcus Vane.
2. News Media
(news_media)
Intermediate Hop
[doc_id: news_luminos_fusion_latency_scandal]
“On August 12, 2024,Luminos-0CEOMarcus Vanepublicly addressed internal
whistleblower reports suggesting that the company’s engineering leads were
aware of the latency spikes documented inStudy-0since Q1. Despite internal
warnings, the company proceeded with the wide-scale deployment of its ‘Fusion-
V3’ software update...”
↩→Bridging Entities Unlocked:CompanyLuminos-0andStudy-0.
3. Technical Journal
(medical_journals)
Terminal Evidence Hop
[doc_id: journal_luminos_fusion_latency_scandal]
“Study-0(Ref:LUMINOS-ENG-772-0) investigated the cross-modal temporal
alignment of theLuminos-0fusion stack. Testing under extreme lighting and
weather conditions revealed a critical processing bottleneck... This delay corre-
lates directly with a22%increase in the relative risk of failing to classify dynamic
pedestrians during rapid lighting transitions.”
↩→Target Evidence Extracted:22% relative riskinStudy-0 (LUMINOS-ENG-
772-0).
4. Wikipedia
(wikipedia)
Background Context
[doc_id: wiki_luminos_fusion_latency_scandal]
“Luminos-0is a Silicon Valley-based technology firm specializing in proprietary
multi-modal sensor fusion architectures for Level 4 autonomous driving systems...
Controversy emerged in mid-2024 following allegations that the company’s sensor
fusion algorithms prioritized high-confidence object detection over real-time
environmental updates...”
28
