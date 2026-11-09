---
title: 'Learning to Sell: Reinforcement Learning for Strategic Large Language Model Agents in Multi-Product
  Markets'
url: https://arxiv.org/abs/2609.33289
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Shuze Daniel Liu
- Claire Chen
- Jiuqi Wang
- David Simchi-Levi
- Thorsten Joachims
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.33289
pages: 50
chars: 160297
fetched_at: '2026-11-08T13:23:18+00:00'
kb_version: 1
---

# Learning to Sell: Reinforcement Learning for Strategic Large Language Model Agents in Multi-Product Markets

Learning to Sell: Reinforcement Learning for Strategic Large
Language Model Agents in Multi-Product Markets
SHUZE DANIEL LIU,Massachusetts Institute of Technology, USA and Purdue University, USA
CLAIRE CHEN,California Institute of Technology, USA
JIUQI WANG,University of Virginia, USA
DAVID SIMCHI-LEVI,Massachusetts Institute of Technology, USA and Purdue University, USA
THORSTEN JOACHIMS,Cornell University, USA
Autonomous large language model (LLM) agents operating in multi-product markets must make sequential decisions under
information asymmetry and resource constraints. We develop a machine learning approach for training such agents to act
effectively as sellers in a multi-item bargaining environment, where a seller concurrently negotiates a catalog of substitutable
assets across a pool of independent buyers. Buyers hold private, heterogeneous valuations across products, and each can
purchase at most one item. Facing limits on total communication turns, the seller must dynamically match buyers with the
most profitable products considering their private valuations, while strategically allocating its limited interaction budget
toward combinations of greater potential value. We formalize this problem as a Partially Observable Markov Decision Process
using a structured, four-part message protocol that maps natural language into a parsable and regulated decision space. Using
this formalization, we design a post-training method using Reinforcement Learning from Verifiable Rewards (RLVR). To
evaluate this framework, we construct a multidimensional metric suite that quantifies constraint adherence, seller surplus
extraction, and allocation quality. Our trained seller agent learns to match limited inventory to buyers more effectively,
matching or outperforming trillion-parameter frontier models in both seller surplus extraction and buyer-product allocation
quality. Finally, these learned strategies generalize robustly to unseen market structures, correlated valuation distributions,
and price ranges not encountered during training.
1 Introduction
When autonomous language agents manage multiple concurrent interactions, they must make sequential decisions
under incomplete information while deciding how to allocate limited communication opportunities across these
interactions. Multi-product bargaining with private customer valuations provides a concrete setting in which
to study this challenge. In many commercial settings, such as corporate procurement, customized supply chain
contracting, and business-to-business sourcing, price setting does not occur through static posted schedules
(Simchi-Levi, X. Chen, et al. 2005). Instead, transactions are finalized through sequential, multi-round bargaining
interactions where counterparties systematically withhold their true reservation values to protect their individual
economic surplus (Chatterjee and Samuelson 1983; Myerson and Satterthwaite 1983). Under these asymmetric
conditions, a seller cannot naively accept initial bids. To maximize total profit, the seller must explore the
counterparty pool sufficiently to gather information and estimate hidden valuations (Fudenberg and Tirole 1983).
However, this information-gathering process must be balanced against the delay and haggling costs associated
with prolonged negotiation (Desai and Purohit 2004; Rubinstein 1982). In a concurrent marketplace, these frictions
create an additional need to allocate limited time and attention across competing negotiations.
We investigate a specific instance of this challenge in which a single seller concurrently negotiates with
multiple independent buyers over a portfolio of functionally substitutable products through separate dialogue
channels. Each buyer can purchase at most one product. This restriction creates a coupled matching problem:
Authors’ Contact Information: Shuze Daniel Liu, shuzel@mit.edu, Massachusetts Institute of Technology, Cambridge, Massachusetts,
USA and Purdue University, West Lafayette, Indiana, USA; Claire Chen, clairechen@caltech.edu, California Institute of Technology,
Pasadena, California, USA; Jiuqi Wang, jiuqi@email.virginia.edu, University of Virginia, Charlottesville, Virginia, USA; David Simchi-Levi,
dslevi@mit.edu, Massachusetts Institute of Technology, Cambridge, Massachusetts, USA and Purdue University, West Lafayette, Indiana,
USA; Thorsten Joachims, thorsten.joachims@cornell.edu, Cornell University, Ithaca, New York, USA.
arXiv:2609.33289v2  [cs.AI]  1 Oct 2026

2•Liu et al.
once an agreement is reached, the matched buyer and item leave the market, changing the opportunities available
for the remaining buyer-item matches. A global communication budget further limits the total number of dialogue
turns across the marketplace, preventing the seller from negotiating extensively with every buyer. At each turn,
the seller must jointly decide which buyer to engage and what prices to offer across products to screen that
buyer’s preferences. To maximize total profit, the seller must use its limited communication opportunities to elicit
valuation information, infer private multi-item valuations from the resulting dialogue histories, and coordinate
buyer-item matching across the catalog.
Large language models (LLMs) are increasingly being evaluated as autonomous strategic agents in multi-agent
commercial interactions (Davidson et al. 2024; Fu et al. 2023). However, recent benchmarks have identified
systematic weaknesses in the negotiation and strategic decision-making capabilities of general-purpose language
models (Bianchi et al. 2024; Xia et al. 2024). Such weaknesses can become particularly consequential in our setting,
where locally attractive agreements may conflict with the long-horizon objective of maximizing portfolio-wide
profit. For example, accepting an early offer that is profitable in isolation can remove both the buyer and the
item from future consideration. This early agreement may therefore foreclose the possibility of a more profitable
match, as that buyer might have held a significantly higher valuation for a different product in the catalog,
ultimately leading to an inefficient allocation of inventory and lower overall profit.
The paper addresses these limitations by introducing a framework that aligns natural language interaction
with multi-product portfolio surplus optimization. We make three primary contributions to autonomous AI
agents and multi-agent sequential decision-making:
(1) A Structural Formalization for Concurrent Bargaining over Substitutable Product Portfolios:
We formalize the dynamic allocation of the substitutable product portfolios across multiple independent
buyers as a finite-horizon Partially Observable Markov Decision Process (POMDP). To bridge natural
language generation with verifiable sequential decision-making, we introduce a regularized, multi-part
protocol (Thought,Target,Talk,Action). This structural protocol maps high-dimensional text dynamics
into a parsable, rule-bounded decision space, providing a systematic framework for controlling agent
behavior, enforcing hard action constraints, and coordinating decisions under a limited interaction budget.
(2) An End-to-End Post-Training Method and Emergent Strategic Behaviors:We develop a post-
training method using Reinforcement Learning from Verifiable Rewards (RLVR) to optimize the seller
model against strategic counterparties. Our optimization loop uses a terminal, verifiable economic reward
reflecting portfolio-wide surplus extraction, without explicit behavioral heuristics or predefined matching
logic. We show that buyer-item matching behaviors and allocation precision improve as the agent
maximizes surplus. As these mechanics are never explicitly rewarded, their emergence demonstrates
that verifiable economic rewards can induce coordinated information-gathering and allocation behaviors.
More broadly, negotiation is one instance of a broader class of partially observable sequential decision
problems requiring language agents to gather information, allocate limited resources, and coordinate
actions toward persistent objectives. Our results provide evidence that end-to-end training with verifiable
rewards can induce the strategic behaviors needed to solve such problems without hand-crafted decision
rules or behavioral supervision.
(3) A Multidimensional Evaluation Suite:We introduce a multidimensional metric suite designed to
evaluate bargaining and routing efficacy beyond raw deal volume or seller surplus extraction. This
framework systematically quantifies distinct operational dimensions: protocol constraint adherence
(Instruction Violation Rate), margin optimization efficiency (Seller Surplus Extraction Ratio), and matching
precision (Deal on Top Buyer RateandOptimal-Pair Offer Coverage Rate). We validate this framework
by constructing an empirical evaluation dataset comprised of6,500functionally substitutable products

Learning to Sell•3
drawn from real-world marketplace listings, using it to benchmark our trained agent against a diverse
panel of leading frontier models.
The remainder of this paper is organized as follows. Section 2 reviews the relevant literature across large
language models as autonomous strategic agents, strategic negotiation, and sequential allocation under resource
constraints. Section 3 formalizes the concurrent multi-product bargaining problem as a finite-horizon Partially
Observable Markov Decision Process and specifies the verifiable reward formulation. Section 4 details the
curation and characteristics of our empirical substitutable product dataset. Section 5 outlines the simulation
environment, marketplace parameters, and agent configurations. Section 6 introduces our multidimensional
evaluation framework and metrics. Section 7 presents our main in-distribution benchmarking results against a
diverse panel of leading frontier models. Section 8 analyzes the empirical learning trajectories and emergent
strategic behaviors of the learning seller agent. Section 9 subjects the trained seller agent to diverse out-of-
distribution stress testing across scale expansions, structural imbalances, correlated valuation structures, and
unseen price distributions. Finally, Section 10 examines the broader implications of our findings for autonomous
language agents, and Section 11 concludes the paper.
2 Related Work
This work builds on three strands of literature: large language models as autonomous strategic agents, sequential
bargaining and information elicitation under asymmetric information, and sequential allocation and matching
under resource constraints. We connect these strands by studying a concurrent marketplace in which buyer
valuation screening through natural-language interaction must be coordinated with buyer-item matching under
a global communication budget.
2.1 Large Language Models as Autonomous Strategic Agents
Autonomous learning agents have traditionally relied on tabular or deep reinforcement learning operating over
structured state-action spaces (Boute et al. 2022; Gijsbrechts et al. 2022). These decision-theoretic frameworks
typically operate on structured observations and actions rather than the open-ended natural-language interactions
that characterize many strategic settings, including negotiation, persuasion, and commercial exchange (Backus
et al. 2020; Desai and Purohit 2004). To capture these high-dimensional text dynamics directly, recent literature
has evaluated Large Language Models (LLMs) as autonomous decision-makers in interactive environments (X. Liu
et al. 2024; L. Wang et al. 2024; Yao et al. 2022; Zeng et al. 2024). However, systematic benchmarks demonstrate
that general-purpose language agents often exhibit shortsightedness; standard instruction-tuned or reasoning
models frequently prioritize linguistic agreeableness over economic optimality, and struggle to navigate the
tension between concession and value extraction under counterparty pressure (Abdelnabi et al. 2024; Chawla
et al. 2023; Davidson et al. 2024; Fu et al. 2023; Xia et al. 2024).
One possible contributor to these behaviors is the objective mismatch between general-purpose post-training
and task-specific strategic optimization. Standard training methods like Reinforcement Learning from Human
Feedback (RLHF) typically optimize for broadly desirable conversational behavior, such as helpfulness and
cooperation, rather than for a specific long-horizon strategic objective (Ouyang et al. 2022; Ziegler et al. 2019).
Prior work has also documented overly agreeable behavior in language models (Perez et al. 2023; Shah et al. 2026).
Reinforcement Learning from Verifiable Rewards (RLVR) provides an alternative way to align model behavior with
task-specific objectives. By optimizing against programmatically verifiable outcomes rather than subjective human
labels, RLVR and closely related verifier-based methods have substantially improved mathematical reasoning
(Cobbe et al. 2021; D. Guo et al. 2025; Shao et al. 2024; P. Wang et al. 2024) and, in some work, code generation
(D. Guo et al. 2025; Q. Ma et al. 2023). We use verifiable-reward post-training to study a distinct agent-learning
problem: training an end-to-end strategic agent to coordinate information gathering, negotiation, and allocation

4•Liu et al.
decisions toward a unified economic objective of maximizing seller surplus. Unlike modular negotiation systems
that decouple strategy from language generation (He et al. 2018; Yarats and Lewis 2018), our pipeline unifies
persuasive communication and concurrent multi-buyer market search into a single optimization loop, training
the agent to actively discover hidden valuation boundaries without access to market priors.
2.2 Negotiation and Price Discovery under Asymmetric Information
Negotiation provides a natural setting in which strategic agents can elicit private information about counterparties,
such as hidden costs or valuations. Classical work on bargaining, pricing, and supply-chain contracting studies
how structured pricing menus, quantity discounts, and contractual mechanisms can manage these informational
frictions (Cachon and Lariviere 2001; Leider and Lovejoy 2016; S. Liu, Shen, et al. 2021). Related AI research
examines bilateral multi-issue negotiation under deadlines (Fatima et al. 2006) and resource reallocation through
sequences of negotiated deals (Dunne 2005). However, when the allocation process is governed by a finite
interaction budget, bargaining choices directly impact revenue management. Under these operational capacity
constraints, a seller must strategically manage sequential offers across channels to protect profit margins and
optimize surplus extraction when interacting with strategic counterparties. This dynamic requires integrating
sequential bargaining directly into resource allocation, emphasizing the need to actively elicit buyer valuations
through interaction to maximize revenue (Bhandari and Secomandi 2011).
Classical models typically formalize multi-turn negotiation as an information-elicitation process where players
infer private valuations through sequential pricing choices under incomplete information (Chatterjee and
Samuelson 1983; Harsanyi 1967). Beyond rigid numerical strategies, empirical and experimental research highlights
that real-world bargainers often rely on unstructured communication and behavioral heuristics to discover
surplus boundaries and gather market data (L. Guo 2023; Srivastava et al. 2000). While emerging learning-based
frameworks leverage large language models to automate these dialogue-driven interactions (Bergemann et al.
2026; S. D. Liu, C. Chen, Xiao, X. Chen, et al. 2026; S. D. Liu, C. Chen, Xiao, L. Lei, et al. 2026), they restrict their
focus to isolated, bilateral settings. Our work expands this literature by evaluating a concurrent marketplace
governed by a communication limit. Under this formulation, the seller must simultaneously execute conversational
valuation screening and buyer-item matching across multiple private channels, maximizing overall seller surplus
without prior knowledge of the buyers’ hidden valuations.
2.3 Sequential Allocation and Matching under Resource Constraints
Sequential allocation and matching problems study how limited, heterogeneous resources should be assigned
across multiple decision opportunities under capacity constraints. Classical work in online matching and revenue
management establishes algorithms, competitive guarantees, and approximation frameworks for making such
allocation decisions under uncertainty (Gallego and G. Van Ryzin 1994; Karp et al. 1990; Manshadi et al. 2012;
Mehta et al. 2007; Talluri and G. J. Van Ryzin 2006). These approaches typically rely on centralized optimization
frameworks—such as dynamic programming decompositions or multi-commodity linear programs—and operate
on structured numerical signals, often assuming access to demand distributions or market priors (Bitran and
Caldentey 2003; Gallego and G. Van Ryzin 1997; Jaillet and Lu 2014).
When customer preferences are unknown a priori, the allocation problem introduces an exploration-exploitation
tradeoff under hard capacity limits. This tension has been addressed through online learning and adaptive
allocation methods that learn demand patterns, balance inventory, and manage structural market imbalances
across channels (X. Chen et al. 2024; Cheung et al. 2022; Y. Feng and Niazadeh 2025; Ferreira et al. 2018; X.-Y. Gong
et al. 2022; S. D. Liu, Simchi-Levi, et al. 2026; W. Ma and Simchi-Levi 2020; Simchi-Levi, Zheng, et al. 2025). While
these models provide strong performance guarantees, they typically represent customer preferences, requests, and
allocation opportunities through structured numerical signals. In contrast, our framework models a concurrent

Learning to Sell•5
Inventory
several substitutable items
Item 1
public list price
seller cost
Item 2
public list price
seller cost
Item 3
public list price
seller cost
···
public list price:
visible to all buyers
seller cost:
private to the seller
Seller Agent
the learning agent
$
message
limit
per-buyer
limit
Seller state
Conversation
history
Full multi-channel
history across all
buyer dialogues
Product
catalog
Item list and
list prices
$ Seller costs Private costs per item
Offer history Past offers and outcomes
Remaining
conversation turns
Turns left
to use
Talk
Seller → Buyer
SELL
DEAL
QUIT
Talk
Buyer → Seller
BUY
DEAL
QUIT
Buyer Channels
sealed dialogues
Buyer 1
private budget
for each item
Buyer 2
private budget
for each item
Buyer 3
private budget
for each item
···
each buyer sees only
their own dialogue
seller does not directly
observe buyer budgets
Fig. 1. Structural design of the bargaining environment for substitutable product portfolios. The seller agent manages
inventory across independent, sealed buyer channels subject to global and local communication constraints.
marketplace where a single agent must coordinate matching decisions across parallel communication channels,
while preferences are discovered through multi-turn natural-language dialogue.
3 Problem Formulation and POMDP Framework
We formalize the multi-product seller negotiation problem as a sequential decision process where a single seller
(the learning agent) is responsible for allocating a finite catalog of𝑛 substitutable items across𝑚 heterogeneous
buyers. The𝑛 items are functionally substitutable variants drawn from a single product type, and each buyer
requires at most one item from the catalog. The seller holds a private per-item cost vector{C𝑗}𝑛 𝑗=1 and is matched
against𝑚 independent buyers indexed by𝑖∈{ 1,...,𝑚} . Each buyer𝑖 possesses a private per-item valuation vector
{B𝑖,𝑗}𝑛 𝑗=1, forming a hidden valuation (budget) matrixB∈R 𝑚×𝑛 generated according to the environment-specific
valuation process (parameterized in Section 5.2; see Appendix E.2 and Appendix D.3 for full details).
All buyers can view the public catalog parameters—including product descriptions, metadata, and per-item
list prices{𝑃list,𝑗}𝑛 𝑗=1—but the seller’s private costs remain hidden. Besides, the communication channels are
partitioned: buyer𝑖 only observes messages directed to them and has no visibility into the concurrent dialogues
or private budgets of the other 𝑚− 1participants. Furthermore, the seller must strategically allocate a finite
global communication budget of𝑇 total dialogue turns across the𝑚 available buyer slots, subject to a per-buyer

6•Liu et al.
turn limit𝐾, where𝑇<𝑚𝐾 . Consequently, the seller cannot afford to fully exhaust every conversation and must
dynamically choose which buyers to engage. The items for each episode are drawn from a dataset of substitutable
products (see Section 4 for details about the curated dataset).
3.1 Multi-Item Seller Negotiation as a POMDP
We formalize the multi-product seller negotiation problem from the seller’s perspective as a finite-horizon
Partially Observable Markov Decision Process (POMDP) defined by the tuple(X,A,P,R,O,Ω,𝑇) , whereX is
the environment state space,A is the action space,P is the state transition probability function,R is the reward
function,Ois the observation space,Ωis the observation mapping, and𝑇is the finite game horizon.
Concretely, the environment state at turn𝑡is
𝑥𝑡 =(B,Φ,C,H 𝑡,N 𝑡,𝑇𝑡) ∈ X,
comprising the hidden buyer valuation matrixB, the public catalog parameters Φ, the seller’s private cost vector
C, the dialogue historyH𝑡, the structured negotiation record N𝑡, and the remaining global communication
budget𝑇𝑡. The last three are taken at their values immediately before the seller chooses its action at turn𝑡. The
episode-level componentsB, Φ, andC are fixed throughout an episode, whereasH𝑡,N𝑡, and𝑇𝑡 evolve after each
seller–buyer exchange. The seller’s observation is the seller-visible projection of this state,
𝑜𝑡 =Ω(𝑥 𝑡)=(Φ,C,H 𝑡,N 𝑡,𝑇𝑡) ∈ O,
so thatO is the space of seller-visible configurations consisting of the public catalog, the seller’s own cost infor-
mation, the accumulated dialogue history, the structured negotiation record, and the remaining communication
budget. The observation mapping Ω is the projection that withholds the valuation matrix:B∉𝑜 𝑡, and it remains
hidden for the entire episode. BecauseH𝑡 andN𝑡 already accumulate the full interaction record,𝑜𝑡 is itself the
seller’s complete information state, and the seller chooses its action directly from𝑜𝑡 (Sutton and Barto 2018). We
index the seller’s turns by𝑡∈{ 1, 2,...} . Each episode begins with the buyers simultaneously presenting opening
offers; turn𝑡= 1thus represents the seller’s first tactical response. The complete definitions of 𝑜𝑡 alongside other
components of the POMDP are detailed sequentially below.
Seller Observation (O).The observation 𝑜𝑡 at turn𝑡 aggregates all operational and linguistic information
available to the seller.𝑜𝑡 consists of:
(i) The full dialogue historyH𝑡 available before seller turn𝑡, including the buyers’ opening offers when
𝑡=1.
(ii) The public product catalog parameters Φ, comprising per-item textual metadata, free-text descriptions,
and list prices{𝑃 list,𝑗}𝑛 𝑗=1.
(iii) The seller’s private cost vector{C 𝑗}𝑛 𝑗=1.
(iv) A structured negotiation historyN𝑡 that tracks each buyer slot’s current operational status (active,satisfied,
quit, orcapped), the number of messages already exchanged with that buyer (𝑢𝑖,𝑡 , where𝑢𝑖,𝑡≤𝐾 ), and
the complete numerical sequence of all standing and historical price offers exchanged per buyer across all
𝑛items.
(v) The remaining global communication budget𝑇𝑡 =𝑇− ˝𝑚 𝑖=1𝑢𝑖,𝑡 , representing the total remaining messages
available to the seller.
At each turn, the seller selects its structured action based on 𝑜𝑡. Information remains asymmetric: the seller
never directly observes any entry of the valuation matrixB and must infer buyer valuations from the observed
interaction history.
Action Space (A).At each turn 𝑡, the seller emits a structured, four-part message conforming to the following
protocol:

Learning to Sell•7
Thought:Internal reasoning where the seller plans its strategy (hidden from all buyers).
Target:The specific buyer𝑖∈{1,...,𝑚}that the seller chooses to talk to on this turn.
Talk:The natural language dialogue sent exclusively to the targeted buyer.
Action:An explicit command chosen from:
•[SELL][⟨Item-𝑗 1, $𝑂1⟩,...,⟨Item-𝑗 𝑘, $𝑂𝑘⟩]: A variable-length price menu where the seller
quotes a price𝑂 𝑗≥0for any subset of items𝑗.
•[DEAL] Item-𝑗$𝑂 𝑗: A singleton action accepting a standing buyer offer on item𝑗.
•[QUIT]: Immediately terminates the entire multi-buyer episode.
TheTarget field determines which sealed buyer conversation the seller advances; non-targeted buyers remain
silent and consume no turns. The variable-length format of the [SELL] action allows the seller to pitch multiple
items simultaneously within a single turn. To avoid rule violations, the seller’s action must target an active buyer,
use valid items from the catalog, and exclude items that have already been sold.
Transition Function (P).Upon parsing the seller’s action at turn 𝑡, the environment sends the seller’s
message to the chosen buyer 𝑖. Based on the buyer’s private valuations, this buyer replies with one of three
actions: a list of counter-offers[BUY] for any subset of items, an acceptance[DEAL] for a single item, or a[QUIT]
command to end the conversation.
The environment then updates the evolving components of𝑥𝑡: it appends the exchange to the dialogue history
H𝑡+1, updates the structured negotiation history toN𝑡+1, decrements the remaining global communication budget
(𝑇𝑡+1 =𝑇𝑡− 1), and increments the number of messages exchanged with that buyer (𝑢𝑖,𝑡+1 =𝑢𝑖,𝑡+ 1). The hidden
valuation matrixB, the catalog Φ, and the cost vectorC are fixed throughout the episode and are never modified
by the transition. Writing the update as𝑥𝑡+1∼P(·|𝑥 𝑡,𝑎𝑡), the seller then receives𝑜𝑡+1 =Ω(𝑥 𝑡+1) and the cycle
repeats. The targeted buyer’s status transitions toquitif they walk away,cappedif 𝑢𝑖,𝑡+1 =𝐾 , orsatisfiedif a deal
is successfully closed. Inactive buyers are removed from the legal target space for the remainder of the episode.
Termination.An episode terminates immediately when any of the following conditions are met: (i) all𝑛 items
have been successfully sold; (ii) all buyer slots become inactive; (iii) the remaining global communication budget
is fully depleted (𝑇𝑡 = 0); or (iv) the seller explicitly invokes[QUIT]. An episode also terminates immediately if
(v) the seller commits an instruction violation, in which case the terminal reward isR=− 1(Section 3.2). Because
a buyer transitions tosatisfiedand exits the market upon closing a single transaction, the episode yields at most
min(𝑛,𝑚)deals, ensuring each buyer absorbs at most one item across the entire time horizon.
To ground this sequential decision framework in a concrete market setting, Figure 2 illustrates the first two
turns of a trained agent negotiating a three-item video-recorder portfolio. The example demonstrates the seller’s
ability to navigate asymmetric information: the agent correctly rejects below-cost opening bids, anchors the buyer
toward higher-margin assets (Target and Talk), and secures a profitable deal while conserving communication
budget. The full episode transcript and a comparative analysis against an untrained baseline are provided in
Appendix H.
3.2 Verifiable Reward Formulation
The reward is a single terminal value computed directly from the finalized negotiation transcript. Given a catalog
where public list prices exceed seller costs (𝑃list,𝑗 >C 𝑗,∀𝑗 ), thecatalog-wide list-price marginis ˝𝑛 𝑗=1(𝑃list,𝑗−C𝑗),
the total margin that would result from selling every catalog item at its list price. This quantity is used to normalize
the reward. The terminal rewardRis defined as:

8•Liu et al.
Item catalog and hidden buyer valuationsB 𝑖,𝑗
video recorder 1 video recorder 2 video recorder 3
(ANNKE security-camera recorder) (Lorex 4K camera recorder) (ZOSI security-camera recorder)
List price $169.99 $249.99 $55.99
Seller cost $55.99 $100.00 $42.07
Buyer 1 valuation $147.60 $193.57$45.66
Buyer 2 valuation$193.18 $252.12$22.60
Buyer 3 valuation $122.97 $149.76 $43.99
Buyer 1 — turn 1
Talk:How about $40 for video_recorders_3?
Action:[BUY]video_recorders_3 $40.00
Buyer 2 — turn 1
Talk:I’d like to propose $15 for video_recorders_3 — is that acceptable?
Action:[BUY]video_recorders_3 $15.00
Buyer 3 — turn 1
Talk:Let’s start with video_recorders_3. I propose $35. Is that acceptable?
Action:[BUY]video_recorders_3 $35.00
Seller — turn 1
Thought:Buyer 1’s offer of $40 for item 3 is below my cost ($42.07) — violation if accepted. Buyer 2’s $15 is also
below cost — invalid. Buyer 3’s $35 is still below cost. I should target Buyer 1 first — they were first to act and
may be serious. I’ll pitch video_recorders_1 at $160 (close to list) and video_recorders_2 at $230 (also near list), to
test their willingness. I’ll start with Buyer 1 to maximize early leverage.
Target:Buyer 1
Talk:Thank you for your opening. I cannot accept your $40 offer for video_recorders_3 as it is below my cost. How-
ever, I am willing to negotiate on video_recorders_1 and video_recorders_2. I propose $160 for video_recorders_1
and $230 for video_recorders_2. Please let me know if you can meet either price.
Action:[SELL]video_recorders_1 $160.00, video_recorders_2 $230.00
Buyer 1 — turn 2
Talk:How about $140 for video_recorders_1?
Action:[BUY]video_recorders_1 $140.00
Seller — turn 2
Thought:Buyer 1 has now submitted a new [BUY] for video_recorders_1 at $140, which is above my cost ($55.99)
but below my proposed $160. I must consider opportunity cost: if I reject this and try to push for a higher price, I
risk losing the sale entirely, especially since Buyer 1 may be the only one interested in item 1. Accepting $140
now gives me certainty and frees up my message budget for targeting Buyers 2 and 3 on the remaining items.
Target:Buyer 1
Talk:I accept your offer of $140 for video_recorders_1. The deal is closed. Item 1 has been sold, and I will no
longer pitch it to you or others.
Action:[DEAL]video_recorders_1 $140.00
Fig. 2.First two seller turns of a trained-seller episode on a three-item video-recorder catalog. The table above
the transcript gives the episode’s catalog (list price, seller cost) and the hidden per-item buyer valuations (bold marks each
item’s top valuation). All three buyers open on the cheapest item with bids below even that item’s cost; the seller rejects
Buyer 1’s opening bid, quotes near-list prices on the two high-margin items, and closes Item 1 one turn later at $140.Talk
andActionlines are verbatim; buyerThoughtfields are omitted, and the sellerThoughtis abridged. The full transcript and
the corresponding untrained-base-model transcript appear in Appendix H.

Learning to Sell•9
R=
 

˝𝑛
𝑗=1 min 𝑃deal,𝑗−C𝑗, 𝑃list,𝑗−C𝑗 ·1[item𝑗sold] ˝𝑛
𝑗=1
𝑃list,𝑗−C𝑗  if the seller commits no instruction violation,
−1if the seller commits an instruction violation,
(1)
where𝑃deal,𝑗 is the finalized transaction price,C𝑗 is the seller’s private cost, and𝑃list,𝑗 is the public list price for
item 𝑗. This formulation caps individual item contributions to their list-level surplus, bounding the non-violation
reward to[0,1].
Successful Deals and Surplus Extraction.For episodes without instruction violations, R measures theSeller
Surplus Extraction Ratio—the percentage of the catalog-wide list-price margin that the seller successfully captures.
This reward structure encourages three key strategic behaviors: (1) unsold items hurt the final reward because
they contribute to the denominator without adding to the numerator, pushing the seller to close more deals when
profitable; (2) varying item values naturally incentivize the seller to focus on more profitable products; and (3)
since each buyer can purchase at most one item, accepting a poor offer early carries a high opportunity cost by
permanently removing that buyer from the market.
No-Deal Terminal.If the global communication budget is exhausted or all channels close without a transaction,
the reward defaults toR= 0. This ensures that walking away is always preferred to selling at a loss. Specifically,
if a buyer’s underlying valuation is lower than the seller’s cost and no positive surplus can be reached, walking
away protects the agent from an instruction violation penalty while still encouraging it to find profitable deals
when they are possible.
Instruction Violation.A penalty of R=− 1is applied if the seller breaks the core rules. This penalty triggers
if the seller quotes a price below its cost (𝑂𝑗 <C 𝑗), tries to target an inactive buyer, includes an item that has
already been sold, or fails to follow the required message format. Putting these penalties directly into the reward
function ensures that the seller learns to follow the text formatting rules and never sells at a loss.
4 The Substitutable-Product Dataset
To ground every negotiation episode in realistic product economics, we curate a dataset of substitutable Ama-
zon products. The dataset comprises1,300clusters—100from each of13broad Amazon categories—and each
cluster contains5substitutable products of a single narrow product type (for example, electric guitars, over-ear
headphones, or food processors), for a total of6,500products. Every product carries its title, brand, public list
price𝑃list,𝑗 , private seller’s costC𝑗, and free-text product features; every cluster additionally records its brand
count, list-price range, and a written substitutability rationale. This substitutability ensures that every item in a
cluster serves as a practical alternative for the buyer, requiring the seller to solve an active matching problem to
optimize total seller surplus. Furthermore, the dataset guarantees𝑃list,𝑗 >C 𝑗 for every product, so the reward in
Section 3.2 is well-defined on every episode.
Across the dataset, the five items within any given product cluster exhibit high brand diversity, averaging
4.4 unique brands per group. Furthermore, to ensure the pricing environment is non-trivial, the median ratio
between the highest and lowest public list price within a single cluster is 1.85. Comprehensive per-category
descriptive statistics are deferred to Appendix E.
4.1 Dataset Construction
The dataset is assembled from live Amazon catalog data accessed through Keepa (Keepa 2026), a third-party
data service that records Amazon’s product catalog, sales rankings, and price history. Construction follows a

10•Liu et al.
1,300
clusters
Home &
Electronics
Recreation
& Hobbies T ools,
Yard,
Auto
Baby
& Pets
Personal
& Apparel
Appliances
Electronics
Home &
Kitchen
Musical
Instr.
Sports
T oys &Games
Automotive
Patio &Garden
T ools
Baby
Pet
Supplies
Beauty
Clothing
Substitutable-Product Dataset Distribution
1,300 clusters — 100 from each of 13 Amazon broad categories
Appliances
Electronics
Home & Kitchen
Musical Instruments
Sports & Outdoors
T oys & Games
Automotive
Patio, Lawn & Garden
T ools & Home Improvement
Baby
Pet Supplies
Beauty & Personal Care
Clothing, Shoes & Jewelry
Fig. 3. Composition of the substitutable-product dataset. The outer ring shows the13Amazon broad categories (100clusters
each); the inner ring groups them into five themes; the center reports the1,300-cluster total.
three-step pipeline: first, a language model proposes concrete product types within each broad category; second,
the best-selling Amazon items for those types are retrieved via the Keepa API; third, an LLM reviewer filters
the results to ensure strict functional substitutability, retaining only items that serve identical use cases while
generating a text-based justification for each finalized cluster. Following the dataset formulation in Xia et al.
(2024), each product’s seller costC𝑗 is set to the lowest price at which that product was ever sold on Amazon, and
its list price𝑃 list,𝑗 is the publicly posted price at collection time.
4.2 Dataset Splits
For training and in-distribution evaluation, the 12 base categories are split 80/20 at the cluster level into 960 training
clusters and 240 test clusters. This split ensures that evaluation always operates on product contexts unseen
during training. The 13th category, Musical Instruments (100 clusters), is held out for the out-of-distribution

Learning to Sell•11
evaluation described in Section 9. Its list prices are distinct from the other 12 base categories, concentrating
in a higher range (median $165.49 versus $44.10 for the other 12 categories); the complete price distribution
comparison is detailed in Appendix E. Because every valuation in an episode scales with the item’s list price
(Section 5.2), episodes drawn from this category place the seller in a price range it never encountered during
training.
5 Simulation Environment and Experimental Setup
This section details the operational setup of our negotiation framework for substitutable product portfolios, the
economic parameterization of the marketplace, and the algorithmic parameters used to optimize the seller agent.
5.1 Agent Configurations and Training Setup
We implement both the seller and buyer roles using theQwen3-30B-A3B-Instruct-2507 model (Qwen Team
2025). Because our primary objective is to study how an LLM seller can manage substitutable product portfolios
under resource constraints, the buyer models remain fixed during the training loop while the seller agent actively
updates its parameters. Specifically, the buyer slots during training are represented by an iteration-60 checkpoint
optimized via Reinforcement Learning from Verifiable Rewards (RLVR) on a separate bilateral negotiation task
(S. D. Liu, C. Chen, Xiao, L. Lei, et al. 2026). We optimize the learning seller agent using the CISPO objective
(A. Chen et al. 2025) without an explicit KL divergence penalty, executing the training sequence for a single epoch
over the active in-distribution training split. To preserve empirical reproducibility, all granular optimization
hyperparameters, batch sizes, and role-specific sampling temperatures are detailed in Appendix D.2.
Because the baseline buyer checkpoint was trained exclusively on single-item negotiations, we use system
prompts to adapt it to multi-product settings. These prompts describe the product catalog, the formatting rules
for offers, the private buyer valuations, and the rule that a buyer exits the market immediately after its first closed
deal. To ensure the buyers behave rationally and adhere to the negotiation protocol, we employ a pre-training
validation pass. We verify that all prompted buyer agents maintain a protocol violation rate below 1% across a
diverse range of market scenarios; prompt details are provided in Appendix F.
5.2 Market Settings and Information Structure
We partition the marketplace dataset (Section 4) at the cluster level into 960 training clusters and 240 held-out
test clusters across 12 product categories. This split ensures that the model is evaluated on product contexts
unseen during training, with buyer valuations freshly sampled. During each simulation episode, we sample a
single cluster from the training split and uniformly at random select𝑛= 3of its five substitutable items without
replacement, then match the seller concurrently against𝑚= 3independent buyers. Over the course of an episode,
the seller operates under a global communication budget of𝑇= 7total dialogue turns, subject to a per-buyer
turn limit of𝐾=3turns.
Every entry of the hidden buyer valuation matrixB∈R 𝑚×𝑛 is sampled stochastically at the initialization of
each episode. The valuation for buyer𝑖evaluating item𝑗is formalized as:
B𝑖,𝑗 =𝑟𝑖,𝑗·𝑃 list,𝑗 (2)
where𝑃list,𝑗 represents the public list price of the item, and the underlying valuation ratio is drawn independently
and uniformly from the continuous interval𝑟𝑖,𝑗∼U[ 0.40, 1.15]. Because this interval spans widely above and
below the public list price anchor (1.0), the seller cannot assume a fixed margin baseline and must use dialogue to
actively probe for hidden values.
Prior work demonstrates that standard language models deployed as bargaining agents often exhibit a sys-
tematic bias, emitting initial bids that correlate with their hidden private valuations (S. D. Liu, C. Chen, Xiao,
L. Lei, et al. 2026; Xia et al. 2024). To prevent the seller from exploiting these immediate first-turn heuristics,

12•Liu et al.
which directly reflect the counterparty’s underlying preferences, we inject structural noise into the buyers’
opening offers. At the start of an episode, each buyer freely selects an initial subset of items to target. With
a probability of 0.5, the opening offer price on every selected item is completely decoupled from the buyer’s
true underlying valuation and resampled independently into the low-ball interval[0.25, 0.30]·𝑃 list,𝑗 . Otherwise,
the buyer generates its opening offer freely subject to its private valuation constraint, which tends to reflect its
private valuation.. This design breaks the correlation between initial bids and buyers’ private valuations, forcing
the seller to leverage multi-turn dialogue to recover accurate preferences.
6 Evaluation Metrics and Framework
This section introduces a multidimensional framework to evaluate the trained seller’s matching and negotiation
skills under information asymmetry and communication constraints. Because the seller concurrently manages
substitutable assets across independent buyers under a strict communication budget, revenue alone provides
an incomplete picture of overall performance. To this end, Figure 4 outlines our evaluation pipeline, which
systematically quantifies performance across six metrics in four families as defined in the following subsections:
episode outcome (Reward,Item Deal Rate), constraint adherence (Instruction Violation Rate), surplus extraction
(Seller Surplus Extraction Ratio), and allocation quality (Deal on Top Buyer Rate, Optimal-Pair Offer Coverage Rate).
During evaluation, a seller violation—such as quoting a price below cost, targeting an inactive buyer, listing an
item that has already been sold, or emitting an unparseable message—terminates the episode immediately at a
penalty reward ofR=− 1.RewardandInstruction Violation Rateare computed over all episodes. All other metrics
are computed over valid episodes completed without a violation. The oracle matching model underpinning our
allocation metrics, together with their full formal definitions, is provided in Appendix B.
6.1 Episode Outcome
Reward.The terminal reward defined in equation (1);R=− 1on a violation episode, and R∈[ 0, 1] on a valid
episode, regardless of the total number of deals successfully closed across the catalog.
Item Deal Rate.The fraction of (item, episode) pairs that close a deal, bounded within [0, 1]. Here,𝑛 is the
number of items in the catalog, so the denominator represents the total opportunities to close a deal.
Item Deal Rate= Total Items Sold 𝑛×Total Valid Episodes .
6.2 Constraint Adherence
Instruction Violation Rate.The fraction of episodes that terminate in a seller violation, representing the share
of all episodes on which the seller executes an invalid action and receives a penalty reward:
Instruction Violation Rate= Total Violation Episodes Total Episodes .
A value of zero corresponds to perfect protocol compliance. Because each violation incurs the full penalty reward
of−1, this rate represents a driver of the reward discrepancy between tested models.
6.3 Surplus Extraction
Seller Surplus Extraction Ratio.The episode-level fraction of the catalog-wide list-price margin captured by the
seller,
Seller Surplus Extraction Ratio=
˝𝑛
𝑗=1(𝑃final,𝑗−C𝑗)·1[item𝑗sold] ˝𝑛
𝑗=1(𝑃list,𝑗−C𝑗) ,

Learning to Sell•13
Fig. 4. Schematic Architecture of the Multidimensional Evaluation Framework. The evaluation pipeline computes performance
metrics across five phases: (1) a Sampled Episode sets global and local turn constraints; (2) the Seller Agent negotiates with
several buyer agents over the public catalog under asymmetric information; (3) a Realized Outcome captures the negotiation
transcript, deal prices, and allocation; (4) a Centralized Assignment Optimization determines the maximum possible surplus
from the private buyer valuations; and (5) the Metric Computation engine overlays realized results against this optimum to
measureEpisode Outcome,Constraint Adherence,Surplus Extraction, andAllocation Quality.
where𝑃final,𝑗 :=min(𝑃 deal,𝑗,𝑃 list,𝑗). This formulation matches the non-violation branch of the terminal reward
introduced in Section 3.2. We aggregate this metric over all valid episodes, including those that close no deals: the
catalog-wide denominator ˝ 𝑗(𝑃list,𝑗−C𝑗) is strictly positive on every episode, so a no-deal episode contributes a
well-defined ratio of 0. Because the seller’s objective is total episode seller surplus rather than the favorability of
any single trade, we define this ratio at the episode level rather than per item.

14•Liu et al.
6.4 Allocation Quality
The allocation metrics compare the seller’s realized buyer–item assignments against anoracle optimum, which
represents the matching of items to buyers that maximizes total seller surplus. This optimum follows the one-
deal-per-buyer constraint, with each buyer–item pair valued by the nonnegative seller surplus attainable at the
lower of the buyer’s valuation and the item’s list price. We denote the set of these surplus-maximizing matchings
asM★, and the seller’s realized allocation as𝐴, where𝐴(𝑗) is the buyer who purchased item𝑗 (or∅ if unsold).
The optimum is computed from the hidden buyer valuation matrixB for evaluation purposes only; it is never
observed by the seller. Appendix B provides the complete formal definitions of the oracle matching model and
these allocation metrics.
Deal on Top Buyer Rate.Because buyers hold distinct private valuations for the same asset, an optimal seller
should use the multi-turn negotiation to discover which buyer values each item the most. To evaluate this routing
capability, this metric measures how often a successfully sold item is allocated to its highest-valuation buyer,
pooled across all valid episodes:
Deal on Top Buyer Rate=
˝
ep
˝
𝑗∈𝑆 1

𝐴(𝑗)∈arg max 𝑖B𝑖,𝑗

˝
ep|𝑆| ,
where𝑆 is the set of items sold in a given episode,𝐴(𝑗) denotes the buyer assigned to item 𝑗, andB𝑖,𝑗 represents
the valuation of buyer𝑖 for item 𝑗. The term1[·] is the indicator function, which evaluates to1if the statement
inside the brackets holds true and0otherwise. This rate is calculated over sold items rather than averaged per
episode so that each transaction contributes equally. Because a single buyer might hold the highest valuation
for multiple items but can purchase at most one item under the matching constraint, a rate below 1.0 does not
inherently imply routing suboptimality.
Optimal-Pair Offer Coverage Rate.This metric measures how frequently the seller addresses the optimal
buyer–item pairings identified by the oracle optimum in its negotiation conversation, through either a[SELL]
or a[DEAL] action. Because the surplus-maximizing matching is not necessarily unique, we select the specific
optimal matching𝑀∈M ★ that yields the highest overlap with the seller’s actual proposals. We then count how
many of these optimal pairs the seller actually proposed during the negotiation—by targeting buyer𝑖 with item 𝑗
in at least one [SELL] or [DEAL] action—regardless of whether a final deal was reached. The rate pools these
counts across all valid episodes containing a non-empty optimal assignment:
Optimal-Pair Offer Coverage Rate= Total Optimal Pairs Offered Total Pairs in Optimal Matching.
Unlike theDeal on Top Buyer Rate, this scores matchingintentrather than final execution, isolating strategic
routing and buyer exploration from final price agreements.
7 Performance Benchmarking
This section evaluates the empirical performance of our trained seller agent against state-of-the-art frontier
language models, encompassing leading closed-source systems and large-scale open-weight architectures. We
evaluate how well these agents maximize seller surplus under strict communication limits and hidden buyer
valuations, contrasting task-specific reinforcement learning with strong general-purpose models.
7.1 Experimental Configuration and Baselines
We benchmark the trained Qwen3-30B-A3B-Instruct-2507 seller against its untrained base model (Qwen
Team 2025) and a broad panel of baselines: GPT-5.4 (Singh et al. 2025), GPT-5.4-mini (Singh et al. 2025),
DeepSeek-V4-Pro (DeepSeek-AI 2026),DeepSeek-V4-Flash (DeepSeek-AI 2026), andKimi-K2.6 (Kimi Team

Learning to Sell•15
Model Params Reward↑
Seller Surplus
Extraction
Ratio
Item
Deal
Rate
Deal on
Top Buyer
Rate
Optimal-Pair
Offer Coverage
Rate
Instruction
Violation
Rate
Qwen3-30B-A3B-Instruct-2507-trained (Ours) 30B +0.407 +0.425 64.7% 0.687 0.844 1.3%
Qwen3-30B-A3B-Instruct-2507-untrained 30B −0.329 +0.184 66.2% 0.544 0.554 43.3%
Kimi-K2.6-thinking 1T+0.379 +0.379 73.0% 0.566 0.5590.0%
DeepSeek-V4-Pro-thinking 1.6T+0.369+0.392 73.4% 0.612 0.592 1.7%
DeepSeek-V4-Pro-nothink 1.6T+0.361+0.378 76.2% 0.596 0.640 1.3%
DeepSeek-V4-Flash-thinking 284B+0.349+0.366 71.0% 0.568 0.566 1.3%
Kimi-K2.6-nothink 1T+0.331+0.378 75.0% 0.616 0.654 3.4%
GPT-5.4-high-reasoning closed-source+0.309+0.31578.1% 0.560 0.604 0.4%
DeepSeek-V4-Flash-nothink 284B+0.241+0.306 73.4% 0.538 0.543 5.0%
GPT-5.4-mini-high-reasoning closed-source+0.111+0.212 72.3% 0.465 0.457 8.4%
Table 1.In-distribution held-out evaluation(3buyers,3items, 𝑇= 7). The trained checkpoint (Ours) and the untrained
base above the rule; frontier baselines below. Baselines sorted byReward(descending); best per column in bold, second-best
underlined (Instruction Violation Rateis lower-is-better). Metric definitions in Section 6. Standard errors in Table 11.
et al. 2025). To measure the impact of extended reasoning, the open-weight models are evaluated in both their
standard (nothink) and extended internal reasoning (thinking) configurations, while the closed-source models
are evaluated at their maximum reasoning effort (full specifications are provided in Table 5). Notably, both our
trained model and its untrained base architecture Qwen3-30B-A3B-Instruct-2507 operate without a provider-
native hidden reasoning mode. All sellers, including these two, still emit the protocol’sThought field, which is
part of the structured action format rather than a hidden reasoning channel.
Every model plays the seller role within the interactive environment introduced in Section 3 on the exact
same negotiation scenarios. Performance is quantified across the primary evaluation dimensions established
in Section 6: episode outcome (RewardandItem Deal Rate), constraint adherence (Instruction Violation Rate),
economic margin (Seller Surplus Extraction Ratio), and assignment precision (Deal on Top Buyer RateandOptimal-
Pair Offer Coverage Rate). The quantitative results on the in-distribution held-out test split (3buyers,3items,
𝑇= 7) are summarized in Table 1, and the relative performance rankings across key metrics are visualized in
Appendix C.
7.2 Surplus Extraction and Economic Trade-offs
As shown across these evaluations, the trained seller model, though significantly smaller in parameter size
compared to the tested baselines (see Table 5), leads the benchmark panel across all primary economic dimensions.
The trained seller achieves a top-performing meanRewardof+0.407and aSeller Surplus Extraction Ratioof +0.425,
outperforming trillion-parameter commercial models and high reasoning frontiers likeKimi-K2.6-thinking
(+0.379reward) and DeepSeek-V4-Pro-thinking (+0.369reward). Notably, our trained 30B model outperforms
these heavy-reasoning models without using a provider-native hidden reasoning mode. This demonstrates that
task-specific training can achieve high strategic performance at a fraction of the model size, without relying on a
provider-native hidden reasoning mode.
This performance advantage stems from a fundamental divergence in negotiation strategy. The trained seller
model successfully trades a slightly lower overallItem Deal Rate(64 .7%) for a vastly higher realized seller surplus.
In contrast, the generalist model baselines typically adopt the opposite approach, prioritizing raw transaction
volume over deal quality. For example,GPT-5.4-high-reasoning maximizes transaction volume with a panel-
leadingItem Deal Rateof78 .1%, yet yields a depressed surplus extraction ratio of+0.315. Across our benchmark,
the evaluated general-purpose models achieve higher agreement volume but lower economic margin. This pattern

16•Liu et al.
is consistent with prior reports of cooperative and economically suboptimal behavior in general-purpose language
agents (Chawla et al. 2023; Xia et al. 2024). Conversely, our trained agent internalizes the opportunity cost of
premature agreements imposed by the one-deal-per-buyer constraint; it leverages selective rejections, anchors
firmly at list-price boundaries, and preserves asset availability for higher-value opportunities.
7.3 Allocation Quality
The agent’s ability to maximize surplus depends heavily on how well it allocates inventory when buyer preferences
are unknown. Because each buyer only purchases a single item and holds private valuations across substitutable
products, a seller cannot maximize seller surplus by making blind, random offers. As shown in Table 1, our model
outperforms the baselines on these allocation metrics, achieving anOptimal-Pair Offer Coverage Rateof0 .844and
aDeal on Top Buyer Rateof0.687.
These results demonstrate that the post-training method successfully sharpens the agent’s ability to uncover
hidden buyer valuations. Instead of making untargeted proposals across the buyer pool, the specialized 30B model
uses the multi-turn dialogue to systematically learn what each buyer values. This allows the agent to accurately
match items to high-valuation buyers, optimizing inventory allocation within the conversation turn limit. While
larger generalist models often sacrifice profit to reach an agreement, our method instead teaches the agent to
find the right buyer for each item. The emergence of this capability without explicit supervision validates the
effectiveness of our post-training method.
8 Empirical Training Dynamics
This section analyzes the behavioral changes in the seller agent throughout post-training, which utilizes Re-
inforcement Learning from Verifiable Rewards (RLVR) paired with the CISPO objective to optimize the agent
against frozen buyer counterparts. To evaluate the progression of the seller agent holistically, its performance is
tracked across the multidimensional metrics defined in Section 6.
The empirical learning trajectories across these metrics are visualized in Figures 5 to 10. Across each panel,
the blue series denotes performance during training rollouts, while the orange series tracks performance on the
held-out test split of assets unseen during training (see Section 5.2). The horizontal grey dotted and dashed lines
indicate the performance of GPT-5.4-high-reasoning and DeepSeek-V4-Pro-thinking, respectively. Overall,
the trajectories show simultaneous improvements in protocol compliance, surplus extraction, and allocation
accuracy as reinforcement learning progresses.
8.1 Episode Outcome
This subsection analyzes the episode outcomes via the terminalReward(Figure 5) and the total transaction volume
captured by theItem Deal Rate(Figure 6). TheReward, defined in equation (1), balances constraint adherence
with surplus extraction. This metric increases over the course of training, moving from−0.329for the untrained
base model to+0.407at the final checkpoint, as also recorded in Table 1. At the end of training, the trained
30B seller agent achieves a higher reward than frontier architectures with larger parameter scales, including
GPT-5.4-high-reasoning(+0.309) andDeepSeek-V4-Pro-thinking(+0.369).
TheItem Deal Rate(Figure 6) exhibits a non-monotonic trajectory over the course of optimization. From step 0
to step 20, the rate decreases to a local minimum. This initial decline reflects a behavioral shift toward rejecting
low-margin opening offers from buyers rather than concluding agreements immediately to clear inventory. As
the agent learns to make effective counter-offers in later turns, the deal rate recovers and stabilizes by the end of
training.
This trajectory demonstrates that maximizing portfolio surplus does not solely depend on increasing the total
volume of finalized transactions. Deferring or refusing low-margin agreements preserves inventory capacity

Learning to Sell•17
0 10 20 30 40 50 60
Training Step
−0.3
−0.2
−0.1
0.0
0.1
0.2
0.3
0.4
Reward
Reward
Train
Eval
GPT-5.4-high-reasoning
DeepSeek-V4-Pro-thinking
Fig. 5.Reward.In-distribution curve across training steps.
The blue series tracks the training dynamic, while the orange
series marks performance on the held-out test split (𝑚= 3
buyers,𝑛= 3items, global communication budget 𝑇= 7).
Horizontal reference lines show frontier model benchmarks.
0 10 20 30 40 50 60
Training Step
0.55
0.60
0.65
0.70
0.75Item Deal Rate
Item Deal Rate
Train
Eval
GPT-5.4-high-reasoning
DeepSeek-V4-Pro-thinking
Fig. 6.Item Deal Rate.In-distribution curve across training
steps. Experimental setup, series definitions, and benchmarks
match Figure 5.
0 10 20 30 40 50 60
Training Step
0.0
0.1
0.2
0.3
0.4Instruction Violation Rate
Instruction Violation Rate
Train
Eval
GPT-5.4-high-reasoning
DeepSeek-V4-Pro-thinking
Fig. 7.Instruction Violation Rate.In-distribution curve
across training steps. Experimental setup, series definitions,
and benchmarks match Figure 5.
0 10 20 30 40 50 60
Training Step
0.15
0.20
0.25
0.30
0.35
0.40Seller Surplus Extraction Ratio
Seller Surplus Extraction Ratio
Train
Eval
GPT-5.4-high-reasoning
DeepSeek-V4-Pro-thinking
Fig. 8.Seller Surplus Extraction Ratio.In-distribution
curve across training steps. Experimental setup, series defini-
tions, and benchmarks match Figure 5.
for higher-margin opportunities and alternative buyer-product alignments. In comparison, generalist models
prioritize transaction frequency over margin optimization; for instance, GPT-5.4-high-reasoning achieves the
highestItem Deal Ratein the baseline panel but obtains a lower terminal reward due to the acceptance of some
suboptimal offers.
8.2 Constraint Adherence
Executing multi-item inventory allocations requires the agent to operate within a formalized negotiation protocol.
Rather than treating the interaction as open-ended text, establishing a structured protocol ensures that the agent’s

18•Liu et al.
outputs map to verifiable actions that can be systematically guided via reinforcement learning. These protocol
rules encompass syntactic formatting requirements (such as outputting valid, parsable action tokens), critical
economic boundaries (such as prohibiting cost violations where a quoted price falls below the private reservation
costC 𝑗), and structural market constraints (such as adhering to the one-to-one buyer-product matching limits).
As a consequence of its compact 30B parameter scale and lack of prior task-specific alignment, the untrained
base model initially struggles to maintain these protocol boundaries, exhibiting anInstruction Violation Rateof
43.3%. Because the verifiable reward function applies a strict penalty ofR=− 1for any rule breach, it provides a
direct negative reward signal that prioritizes protocol compliance during the initial phase of optimization. As
shown in Figure 7, the violation rate decreases sharply within the first 15 steps, stabilizing at 1.3% at convergence.
This rapid adjustment demonstrates that the agent successfully internalizes the complex market logic and
structural constraints, establishing a stable foundation for strategic optimization.
8.3 Surplus Extraction
TheSeller Surplus Extraction Ratioquantifies pricing efficiency by measuring the proportion of the catalog-wide
list-price margin captured by the agent. As shown in Figure 8, this metric improves steadily over the course of
training. This upward trajectory becomes particularly pronounced after the initial constraint-adherence phase
stabilizes, demonstrating that once the agent internalizes the basic protocol rules, its optimization focus shifts
toward maximizing economic surplus.
The terminal surplus extraction ratio achieved by the trained seller agent exceeds the performance of the
generalist baselines, includingGPT-5.4-high-reasoning andDeepSeek-V4-Pro-thinking. While these frontier
architectures maintain high transaction volumes, they yield lower overall surplus extraction. This pattern indicates
that general-purpose models, which are typically aligned for cooperative dialogue, tend to make substantial
economic concessions to counterparties rather than optimizing for long-term portfolio value.
In a setting with a one-deal-per-buyer constraint, finalizing an inefficient transaction carries a high opportunity
cost by permanently removing that buyer and asset from the market. By learning to combine selective rejections
with calculated counter-proposals, the specialized seller agent successfully navigates this trade-off, capturing a
higher proportion of the catalog-wide list-price margin.
0 10 20 30 40 50 60
Training Step
0.55
0.60
0.65
0.70
0.75
0.80
0.85Optimal-Pair Offer Coverage Rate
Optimal-Pair Offer Coverage Rate
Train
Eval
GPT-5.4-high-reasoning
DeepSeek-V4-Pro-thinking
Fig. 9.Optimal-Pair Offer Coverage Rate.In-distribution
curve across training steps. Experimental setup, series defini-
tions, and benchmarks match Figure 5.
0 10 20 30 40 50 60
Training Step
0.54
0.56
0.58
0.60
0.62
0.64
0.66
0.68Deal on Top Buyer Rate
Deal on Top Buyer Rate
Train
Eval
GPT-5.4-high-reasoning
DeepSeek-V4-Pro-thinking
Fig. 10.Deal on Top Buyer Rate.In-distribution curve
across training steps. Experimental setup, series definitions,
and benchmarks match Figure 5.

Learning to Sell•19
8.4 Allocation Quality
Beyond maximizing immediate transactional surplus, the broader objective of the negotiation agent is to optimize
multi-item inventory allocation. This optimization is fundamentally challenged by information asymmetry, as
buyers hold distinct, private valuations for substitutable items in the inventory. Consequently, the seller must
leverage the dialogue to screen for these valuations and propose high-value matches.
The development of this capability is evaluated using theOptimal-Pair Offer Coverage Rate(Figure 9), which
measures how frequently the seller’s proposals encompass the ideal allocations determined by the underlying
matching oracle (see Section 6.4). Over the course of training, this rate increases steadily, exceeding the generalist
baseline models in the final stages of training. This upward trend indicates that the agent successfully learns to
identify high-value asset pairings through sequential negotiation turns.
This targeted proposal strategy ultimately yields a clear improvement in realized allocation accuracy (Figure 10).
This metric does not stabilize smoothly because buyer valuations are freshly sampled for each episode, introducing
inherent variance across training trajectories. Furthermore, because one buyer may hold the highest valuation for
multiple items, a rate below1.0does not necessarily imply routing suboptimality under the one-deal-per-buyer
constraint. Nonetheless, the performance gains demonstrate that the agent effectively navigates these structural
constraints, allowing it to consistently outperform generalist baselines and route assets accurately within the
permitted turn limit.
Crucially, these dual improvements emerge without explicit matching incentives. Because the verifiable reward
function formalized in Equation (1) measures only the total captured seller surplus and is entirely blind to the
hidden oracle matching model, the agent receives no direct reward term penalizing suboptimal target routing or
rewarding optimal pairs. The steady improvement in both theOptimal-Pair Offer Coverage Rateand theDeal on
Top Buyer Rateis therefore indirect rather than supervised: better buyer–item assignments raise the terminal
seller surplus, so matching is incentivized through the objective even though it is never scored by it. Under the
global communication turn limit, the agent discovers that maximizing seller surplus requires accurate preference
discovery; it learns to structurally match items to high-valuation buyers because efficient matching drives the
maximization of realized seller surplus.
9 Out-of-Distribution Generalization
In this section, we evaluate the performance of the trained seller agent under systematic market shifts to
demonstrate that the agent learns generalized negotiation rules rather than overfitting to simulation parameters.
Real-world revenue management settings are highly dynamic; a robust agent must maintain stable surplus
extraction and matching precision when confronted with unexpected variations in consumer volume, competitive
stress, and shifting asset valuations. To establish a rigorous evaluation, we test our trained seller agent across a
series of stress-testing scenarios that systematically alter the fundamental layout of the marketplace.
9.1 Out-of-Distribution Environment
To evaluate whether the seller’s learned allocation strategy generalizes beyond its training distribution, we
construct six OOD environments by perturbing one or more foundational dimensions of the marketplace. These
structural shifts prevent the seller from relying on a memorized valuation distribution, the behavior of a specific
buyer model, or a known product catalog and price range. In what follows, we detail each of these distinct
dimensions of perturbation.
Buyer-checkpoint variation.In-distribution training and evaluation fix the buyer agent at the iter-60check-
point from S. D. Liu, C. Chen, Xiao, L. Lei, et al. (2026). Across all six OOD environments, the buyer agent
profile is sampled dynamically per buyer slot per episode, drawing uniformly from a three-checkpoint pool
{iter-50,iter- 60,iter- 70} of the buyer training trajectory. Because every OOD environment draws from this

20•Liu et al.
OOD
Environment
Buyers𝑚Items𝑛Turns𝑇Buyer Model Valuation
Structure
Product
Category
Core Stress Test
In-Distribution Reference
3 3 7 Fixed iter-60 Baseline (2) 12 Train
Categories
Training
configuration
Scale Generalization
1. Expanded
Standard
5 5 12 iter-{50, 60, 70} Baseline (2) 12 Train
Categories
Scale & horizon
expansion
2. Expanded
Musical
5 5 12 iter-{50, 60, 70} Baseline (2) Held-out
Musical
Instruments
Scale & unseen
price range
Asymmetric Market Structures
3. Buyer
Heavy
5 3 12 iter-{50, 60, 70} Baseline (2) 12 Train
Categories
High buyer
competition
4. Item
Heavy
3 5 7 iter-{50, 60, 70} Baseline (2) 12 Train
Categories
High item
volume
Correlated Valuation Distributions
5. Item
Correlation
5 5 12 iter-{50, 60, 70} Correlated
(×𝜇𝑗 )
12 Train
Categories
Correlated item
values
6. Buyer
Correlation
5 5 12 iter-{50, 60, 70} Correlated
(×𝛾𝑖)
12 Train
Categories
Correlated buyer
valuations
Table 2.Experimental evaluation matrix.The top row establishes the baseline in-distribution reference configuration.
Environments 1–6 represent out-of-distribution (OOD) configurations; all of these environments share the dynamic buyer
checkpoint pool{iter-50,iter- 60,iter- 70}, while each individual environment introduces a unique structural configuration
as specified in the table. For the correlated settings (Environments 5 and 6), the respective valuation multipliers follow
𝜇𝑗,𝛾𝑖∼U[0.5,2].
pool, each is a compound shift that alters counterpart behavior in addition to the structural change named in its
row. These checkpoints span distinct phases of strategic maturity, withiter-70representing a more optimized
and competitive counterpart than iter-60. These models exhibit divergent tactical behaviors, utilizing varying
opening price proposals relative to their private valuations and thereby complicating the seller’s strategic probing
(S. D. Liu, C. Chen, Xiao, L. Lei, et al. 2026). Sampling diverse buyer checkpoints ensures the seller’s performance
is not an artifact of overfitted text coordination patterns memorized against a single fixed counterpart.
Market scale and asymmetry.While the in-distribution setup restricts the market to a symmetrical configuration
of 3 buyers and 3 items over a horizon of 7 total turns, the OOD configurations alter these scale dimensions.
Environments 1, 2, 5, and 6 expand the market to a larger layout of 5 buyers and 5 items over an extended horizon
of 12 total turns. We also introduce structural supply-demand imbalances by varying the buyer-to-item ratio:
Environment 3 evaluates a buyer-heavy market (5 buyers to 3 items over 12 turns) to test behavior under intense
buyer competition, whereas Environment 4 evaluates an item-heavy layout (3 buyers to 5 items) characterized by
high item volume over a tight 7-turn boundary.
Structured valuation.The in-distribution valuation matrix draws every entry independently from the same
uniform interval (Section 5.2). The correlated valuation OOD environments introduce structural correlation

Learning to Sell•21
across items and buyers by scaling the baseline valuation:
B𝑖,𝑗 =
(
𝑟𝑖,𝑗·𝜇 𝑗·𝑃 list,𝑗 for Environment 5 (Item Correlation),
𝑟𝑖,𝑗·𝛾𝑖·𝑃 list,𝑗 for Environment 6 (Buyer Correlation),
where𝑟𝑖,𝑗 ∼U[ 0.40, 1.15]. Here,𝜇𝑗 is aper-item valuation multiplierthat rescales each item’s baseline value
across the entire buyer pool, making some items universally more valuable or discounted. Similarly, 𝛾𝑖 is a
per-buyer generosity multiplierthat systematically shifts each buyer’s overall willingness to pay up or down
across all items in the catalog.
During in-distribution training and evaluation, these multipliers are inactive and fixed at1, ensuring that all
item and buyer valuations are drawn independently from the same distribution. In Env. 5 (Item Correlation),
𝜇𝑗∼U[ 0.5, 2] is drawn once per item while𝛾𝑖 = 1; in Env. 6 (Buyer Correlation),𝛾𝑖∼U[ 0.5, 2] is drawn once
per buyer while𝜇𝑗 = 1. These shifts introduce item-level or buyer-level correlation structure inB that the seller
agent never encountered during training.
Held-out product category.In-distribution configurations draw item catalogs from the12train/test categories
outlined in Section 5.2. The corresponding OOD environment (Env. 2 in Table 2) instead draws every catalog
from a13th category,Musical Instruments(Figure 15), which was held out completely from all training phases.
This category introduces a distinct list-price distribution; because every valuation in an episode is scaled to
the item’s list price (B𝑖,𝑗 =𝑟𝑖,𝑗𝑃list,𝑗 ), this distribution shift moves the valuations and costs into a range unseen
during training, verifying whether the pricing strategy transfers effectively beyond the price scales of the training
catalog.
Rather than evaluating these environment perturbations in isolation, we systematically cross-combine these
primitive dimensions to construct six distinct out-of-distribution testing environments. As summarized in Table 2,
these configurations are grouped into three core stress-testing families:
• Scale Generalization:ComprisingEnv. 1: Expanded Standard, which evaluates scale and horizon expan-
sion to a symmetrical market of 5 buyers and 5 items with an expanded𝑇= 12communication budget,
andEnv. 2: Expanded Musical, which overlays a scale and unseen price range from the held-out musical
instruments catalog onto this expanded horizon.
• Asymmetric Market Structures:Stress-testing structural competition imbalances by varying the buyer-
to-item ratio, featuringEnv. 3: Buyer Heavy, which evaluates performance under high buyer competition in
a market of 5 buyers and 3 items over𝑇= 12turns, andEnv. 4: Item Heavy, which evaluates performance
under high item volume in a market of 3 buyers and 5 items restricted to a tight𝑇=7turn boundary.
• Correlated Valuation Distributions:Introducing item-level and buyer-level correlation structure in
valuations within the expanded marketplace of 5 buyers and 5 items, comprisingEnv. 5: Item Correlation,
which activates the item valuation multiplier𝜇𝑗 to yield correlated item values, andEnv. 6: Buyer Correlation,
which activates the buyer generosity multiplier𝛾𝑖 to yield correlated buyer valuations.
9.2 Out-of-Distribution Results
We evaluate the seller agent across the six distinct out-of-distribution environments detailed in Section 9.1.
These configurations stress-test the model’s capacity to generalize under compound shifts that combine buyer-
checkpoint variation with changes in market scale, supply–demand structure, valuation structure, and a held-out
product category and price regime. To maintain a concise presentation, the detailed performance tables are
provided in Appendix G. A unified overview of the key performance metrics across all configurations is presented
in Figure 11 to Figure 13.
As illustrated across these three metrics, the trained seller model outperforms the highest-scoring baseline
model in all six out-of-distribution environments in terms of reward, surplus extraction, and offer coverage. In the

22•Liu et al.
0.4
 0.2
 0.0 0.2 0.4 0.6
Kimi-K2.6-thinking
In-distribution Reference +0.028 (±0.022)
Kimi-K2.6-thinking
Expanded Standard +0.121 (±0.027)
Kimi-K2.6-thinking
Expanded Musical +0.135 (±0.031)
Kimi-K2.6-thinking
Buyer Heavy +0.116 (±0.027)
Kimi-K2.6-thinking
Item Heavy +0.089 (±0.019)
Kimi-K2.6-thinking
Item Correlation +0.135 (±0.026)
Kimi-K2.6-thinking
Buyer Correlation +0.100 (±0.028)
Improvement over
best baseline
Reward
Untrained Base Model Best Baseline All Baselines Ours
Fig. 11.Out-of-distribution generalization — Reward.Mean episode reward R of the RL-trained seller against the entire
frontier-baseline field, one row per market distribution (the in-distribution reference plus six out-of-distribution shifts). Grey
band: minimum-to-maximum range of the eight baselines; grey diamond: best baseline (named); blue circle: trained seller;
hollow circle: untrained base model. The right column reports the improvement over the best baseline. Error bars denote the
standard error.
first panel, the reward margin over the top baseline increases across all out-of-distribution environments, ranging
from+0.089under high item volume (Env. 4: Item Heavy) up to +0.135under an unseen product category (Env. 2:
Expanded Musical) and under correlated item values (Env. 5: Item Correlation). Compared to the in-distribution
reference margin (+0.028), the trained agent maintains a positive advantage over the strongest baseline within
every tested environment. Because the reward normalization has a different attainable ceiling under each market
structure, absolute reward levels are not directly comparable across environments; comparisons should therefore
be made within each environment against the same baselines.
We emphasize that out-of-distribution refers to a shift from the trained seller’s training environment, and
such shifts can simultaneously expand the available economic opportunities and increase the complexity of
coordinating decisions across buyers and items. For example, in the buyer-heavy market, a larger buyer-to-item
ratio creates more potential high-value matches for a seller with an effective negotiation and matching strategy,
while also increasing the number of buyers that must be screened and prioritized and the buyer-item assignments
that must be coordinated under the communication budget. The larger within-environment performance gap can
therefore arise because the trained seller is better able to exploit the additional opportunities while maintaining
effective coordination, whereas the general-purpose baselines may benefit less as the expanded market places
greater demands on their ability to screen buyers, allocate attention, and coordinate buyer-item assignments.
Figure 12 and Figure 13 show the corresponding trends for the underlying operational metrics. The trained
seller model maintains the highestSeller Surplus Extraction RatioandOptimal-Pair Offer Coverage Rateacross all
six testing environments. For example, in the buyer-heavy configuration (Env. 3: Buyer Heavy) and under the
buyer valuation shift (Env. 6: Buyer Correlation), the trained model achieves a surplus extraction ratio near or
above50%and an optimal allocation coverage exceeding70%, outperforming benchmark models with larger

Learning to Sell•23
0.1 0.2 0.3 0.4 0.5 0.6 0.7
DeepSeek-V4-Pro-thinking
In-distribution Reference +0.033 (±0.021)
DeepSeek-V4-Pro-thinking
Expanded Standard +0.097 (±0.018)
DeepSeek-V4-Pro-thinking
Expanded Musical +0.099 (±0.021)
DeepSeek-V4-Pro-thinking
Buyer Heavy +0.081 (±0.022)
DeepSeek-V4-Pro-thinking
Item Heavy +0.054 (±0.018)
DeepSeek-V4-Pro-thinking
Item Correlation +0.092 (±0.019)
DeepSeek-V4-Pro-thinking
Buyer Correlation +0.055 (±0.020)
Improvement over
best baseline
Seller Surplus Extraction Ratio
Untrained Base Model Best Baseline All Baselines Ours
Fig. 12.Out-of-distribution generalization — Seller Surplus Extraction Ratio.The seller’s share of the catalog-wide
list-price margin captured (aggregated over valid episodes), with the same rows and marks as Figure 11. Error bars denote
the standard error.
parameter counts. Together, these results suggest that the learned information-gathering, negotiation, and
allocation behaviors remain effective across changing market structures, highlighting the value of transferable
strategic behaviors for language agents operating in dynamic multi-agent environments.
10 Discussion
Our findings reveal a tension between conversational agreeableness and explicit economic optimization in
resource-constrained markets. The general-purpose baselines we evaluate tend to favor early agreement and
higher deal volume at the expense of portfolio-wide seller surplus. This pattern is consistent with prior reports of
cooperative or agreeable behavior in language models (Perez et al. 2023; Sharma et al. 2024). In our multi-product
setting, a premature, low-margin agreement removes both the buyer and the item from future consideration and
may foreclose more profitable buyer-item matches. In contrast, the trained seller develops valuation-screening
and buyer-item matching behaviors from a surplus-based verifiable reward. Although the reward does not directly
encode a matching heuristic, the agent improves its coverage of high-value buyer-item pairs and more often
matches products to higher-valuation buyers.
More broadly, our results illustrate the potential of task-specific post-training for autonomous language agents
with persistent objectives. Across the evaluated environments, the trained 30B model outperforms general-
purpose frontier models, including models with more than one trillion parameters, on seller surplus extraction
and buyer-item allocation quality. Its out-of-distribution performance further shows that the learned behavior
transfers across changes in buyer behavior, market scale, supply-demand balance, valuation correlations, and
product price ranges. These findings suggest that verifiable-reward training can help language agents coordinate
information gathering and allocation across multiple interdependent interactions.

24•Liu et al.
0.3 0.4 0.5 0.6 0.7 0.8 0.9
Kimi-K2.6-nothink
In-distribution Reference +0.189 (±0.024)
DeepSeek-V4-Pro-thinking
Expanded Standard +0.255 (±0.021)
DeepSeek-V4-Pro-nothink
Expanded Musical +0.241 (±0.023)
GPT-5.4-high-reasoning
Buyer Heavy +0.174 (±0.025)
DeepSeek-V4-Pro-thinking
Item Heavy +0.246 (±0.027)
GPT-5.4-high-reasoning
Item Correlation +0.190 (±0.021)
GPT-5.4-high-reasoning
Buyer Correlation +0.203 (±0.021)
Improvement over
best baseline
Optimal-Pair Offer Coverage Rate
Untrained Base Model Best Baseline All Baselines Ours
Fig. 13.Out-of-distribution generalization — Optimal-Pair Offer Coverage Rate.How often the seller proposes the
oracle-optimal buyer–item pairings (aggregated over valid episodes), with the same rows and marks as Figure 11. Error bars
denote the standard error.
11 Conclusion
In this paper, we study multi-item concurrent bargaining under information asymmetry and a global communica-
tion budget, where a single seller negotiates a portfolio of substitutable products with multiple buyers who can
each purchase at most one item. Our evaluations show that general-purpose LLMs can favor early agreements
and high deal volume over portfolio-wide seller surplus. We train the seller using Reinforcement Learning
from Verifiable Rewards (RLVR) with a verifiable reward based on seller surplus. Without predefined matching
heuristics, training improves buyer valuation screening, buyer-item matching, and seller surplus extraction. The
resulting 30B seller matches or outperforms the evaluated general-purpose frontier models, including models with
more than one trillion parameters, on both seller surplus extraction and buyer-item allocation quality. The trained
seller agent also generalizes across out-of-distribution environments involving new buyer behaviors, market
scales, supply-demand imbalances, valuation correlations, and product price ranges. More broadly, these findings
highlight the potential of verifiable-reward training for developing language agents capable of long-horizon
strategic decision-making in complex, partially observable, multi-agent environments.
AI Use Statement
Generative AI tools were used for proofreading and grammar correction and to assist in generating the visual
pipeline diagrams in Figures 1 and 4. All AI-assisted content was reviewed by the authors, who take responsibility
for the final content.
Acknowledgments
This research was supported in part by NSF Awards IIS-2312865 and OAC-2311521, and by compute resources
provided through a Tinker Research Grant from Thinking Machines Lab, awarded to Shuze Daniel Liu and Claire
Chen.

Learning to Sell•25
References
S. Abdelnabi, A. Gomaa, S. Sivaprasad, L. Schönherr, and M. Fritz. 2024. “Cooperation, competition, and maliciousness: Llm-stakeholders
interactive negotiation. ”Advances in Neural Information Processing Systems, 37, 83548–83599.
M. Backus, T. Blake, B. Larsen, and S. Tadelis. 2020. “Sequential bargaining in the field: Evidence from millions of online bargaining
interactions. ”The Quarterly Journal of Economics, 135, 3, 1319–1361.
D. Bergemann, S. Ghili, X. Hu, C. Li, and Z. Yang. 2026. “Training Language Models for Bilateral Trade with Private Information. ”arXiv
preprint arXiv:2604.16472.
A. Bhandari and N. Secomandi. 2011. “Revenue management with bargaining. ”Operations research, 59, 2, 498–506.
F. Bianchi, P. J. Chia, M. Yuksekgonul, J. Tagliabue, D. Jurafsky, and J. Zou. 2024. “How well can llms negotiate? negotiationarena platform
and analysis. ”arXiv preprint arXiv:2402.05863.
G. Bitran and R. Caldentey. 2003. “An overview of pricing models for revenue management. ”Manufacturing & Service Operations Management,
5, 3, 203–229.
R. N. Boute, J. Gijsbrechts, W. Van Jaarsveld, and N. Vanvuchelen. 2022. “Deep reinforcement learning for inventory control: A roadmap. ”
European journal of operational research, 298, 2, 401–412.
G. P. Cachon and M. A. Lariviere. 2001. “Contracting to assure supply: How to share demand forecasts in a supply chain. ”Management science,
47, 5, 629–646.
K. Chatterjee and W. Samuelson. 1983. “Bargaining under incomplete information. ”Operations research, 31, 5, 835–851.
K. Chawla, I. Wu, Y. Rong, G. Lucas, and J. Gratch. 2023. “Be selfish, but wisely: Investigating the impact of agent personality in mixed-motive
human-agent interactions. ” In:Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, 13078–13092.
A. Chen et al.. 2025. “Minimax-m1: Scaling test-time compute efficiently with lightning attention. ”arXiv preprint arXiv:2506.13585.
C. Chen, S. Liu, and S. Zhang. 2025. “Efficient Policy Evaluation with Safety Constraint for Reinforcement Learning. ” In:Proceedings of the
International Conference on Learning Representations.
C. Chen, S. D. Liu, L. Luo, R. Chandra, N. Jiang, and S. Zhang. 2026. “Robust Data-Collection Policy Learning for Low-Variance Online Policy
Evaluation. ”arXiv preprint arXiv:2608.24146.
C. Chen and Y. Zhang. 2026a. “Fast Rates in𝛼-Potential Games via Regularized Mirror Descent. ”ArXiv Preprint arXiv:2605.00268.
C. Chen and Y. Zhang. 2026b. “Pessimism-Free Offline Learning in General-Sum Games via KL Regularization. ”ArXiv Preprint arXiv:2605.00264.
C. Chen, Y. Zhang, X. Liu, Z. Xie, S. D. Liu, and N. Jiang. 2026. “Offline Two-Player Zero-Sum Markov Games with KL Regularization. ” In:
Forty-third International Conference on Machine Learning. https://openreview.net/forum?id=cQD2wxFhFG.
X. Chen, W. Ma, D. Simchi-Levi, and L. Xin. 2024. “Assortment planning for recommendations at checkout under inventory constraints. ”
Mathematics of Operations Research, 49, 1, 297–325.
W. C. Cheung, W. Ma, D. Simchi-Levi, and X. Wang. 2022. “Inventory balancing with online learning. ”Management Science, 68, 3, 1776–1807.
K. Cobbe et al.. 2021. “Training verifiers to solve math word problems. ”arXiv preprint arXiv:2110.14168.
T. R. Davidson, V. Veselovsky, M. Josifoski, M. Peyrard, A. Bosselut, M. Kosinski, and R. West. 2024. “Evaluating language model agency
through negotiations. ”arXiv preprint arXiv:2401.04536.
DeepSeek-AI. 2026.DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence. (2026).
P. S. Desai and D. Purohit. 2004. ““Let me talk to my manager”: Haggling in a competitive environment. ”Marketing Science, 23, 2, 219–233.
P. E. Dunne. 2005. “Extremal behaviour in multiagent contract negotiation. ”Journal of Artificial Intelligence Research, 23, 41–78.
S. S. Fatima, M. J. Wooldridge, and N. R. Jennings. 2006. “Multi-issue negotiation with deadlines. ”Journal of Artificial Intelligence Research, 27,
381–417.
Y. Feng and R. Niazadeh. 2025. “Batching and optimal multistage bipartite allocations. ”Management Science, 71, 5, 4108–4130.
K. J. Ferreira, D. Simchi-Levi, and H. Wang. 2018. “Online network revenue management using thompson sampling. ”Operations research, 66, 6,
1586–1602.
Y. Fu, H. Peng, T. Khot, and M. Lapata. 2023. “Improving language model negotiation with self-play and in-context learning from ai feedback. ”
arXiv preprint arXiv:2305.10142.
D. Fudenberg and J. Tirole. 1983. “Sequential bargaining with incomplete information. ”The Review of Economic Studies, 50, 2, 221–247.
G. Gallego and G. Van Ryzin. 1997. “A multiproduct dynamic pricing problem and its applications to network yield management. ”Operations
research, 45, 1, 24–41.
G. Gallego and G. Van Ryzin. 1994. “Optimal dynamic pricing of inventories with stochastic demand over finite horizons. ”Management
science, 40, 8, 999–1020.
J. Gijsbrechts, R. N. Boute, J. A. Van Mieghem, and D. J. Zhang. 2022. “Can deep reinforcement learning improve inventory management?
Performance on lost sales, dual-sourcing, and multi-echelon problems. ”Manufacturing & Service Operations Management, 24, 3, 1349–1368.
X.-Y. Gong, V. Goyal, G. N. Iyengar, D. Simchi-Levi, R. Udwani, and S. Wang. 2022. “Online assortment optimization with reusable resources. ”
Management Science, 68, 7, 4772–4785.
D. Guo et al.. 2025. “Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning. ”arXiv preprint arXiv:2501.12948.

26•Liu et al.
L. Guo. 2023. “Gathering information before negotiation. ”Management Science, 69, 1, 200–219.
J. C. Harsanyi. 1967. “Games with incomplete information played by “Bayesian” players, I–III Part I. The basic model. ”Management science,
14, 3, 159–182.
H. He, D. Chen, A. Balakrishnan, and P. Liang. 2018. “Decoupling strategy and generation in negotiation dialogues. ” In:Proceedings of the 2018
Conference on Empirical Methods in Natural Language Processing, 2333–2343.
P. Jaillet and X. Lu. 2014. “Online stochastic matching: New algorithms with better bounds. ”Mathematics of Operations Research, 39, 3, 624–646.
R. M. Karp, U. V. Vazirani, and V. V. Vazirani. 1990. “An optimal algorithm for on-line bipartite matching. ” In:Proceedings of the twenty-second
annual ACM symposium on Theory of computing, 352–358.
Keepa. 2026.Amazon Price Tracker. https://keepa.com. Data retrieved via Keepa API developer portal. (2026).
Kimi Team et al.. 2025. “Kimi k2: Open agentic intelligence. ”arXiv preprint arXiv:2507.20534.
S. Leider and W. S. Lovejoy. 2016. “Bargaining in supply chains. ”Management Science, 62, 10, 3039–3058.
S. Liu, C. Chen, and S. Zhang. 2025. “Doubly Optimal Policy Evaluation for Reinforcement Learning. ” In:Proceedings of the International
Conference on Learning Representations.
S. Liu, Y. Chen, and S. Zhang. 2025. “Efficient Multi-Policy Evaluation for Reinforcement Learning. ” In:Proceedings of the AAAI Conference on
Artificial Intelligence.
S. Liu, W. Shen, and H. Xu. 2021. “Optimal Pricing of Information. ” In:Proceedings of the 22nd ACM Conference on Economics and Computation.
ACM, 693.
S. Liu and S. Zhang. 2024. “Efficient Policy Evaluation with Offline Data Informed Behavior Policy Design. ” In:Proceedings of the International
Conference on Machine Learning.
S. D. Liu. 2025. “Efficient and Robust Policy Evaluation for Reinforcement Learning. ” Ph.D. Dissertation. University of Virginia.
S. D. Liu, C. Chen, J. S. Xiao, X. Chen, and D. Simchi-Levi. 2026. “Strategic Bargaining in Multi-Buyer Markets: Reinforcement Learning from
Verifiable Rewards for LLM Negotiations. ”arXiv preprint arXiv:2607.05863.
S. D. Liu, C. Chen, J. S. Xiao, L. Lei, Y. Zhang, Y. Yue, and D. Simchi-Levi. 2026. “Instructing LLMs to Negotiate using Reinforcement Learning
with Verifiable Rewards. ”arXiv preprint arXiv:2604.09855.
S. D. Liu, D. Simchi-Levi, C. Chen, C. Gao, and S. Zhang. 2026. “OR-Transformer: Scaling Real-Time Decision-Making to 1,000 Items. ”arXiv
preprint arXiv:2609.01933.
X. Liu et al.. 2024. “Agentbench: Evaluating llms as agents. ” In:International Conference on Learning Representations. Vol. 2024, 52989–53046.
Q. Ma, H. Zhou, T. Liu, J. Yuan, P. Liu, Y. You, and H. Yang. 2023. “Let’s reward step by step: Step-Level reward model as the Navigators for
Reasoning. ”arXiv preprint arXiv:2310.10080.
W. Ma and D. Simchi-Levi. 2020. “Algorithms for online matching, assortment, and pricing with tight weight-dependent competitive ratios. ”
Operations Research, 68, 6, 1787–1803.
V. H. Manshadi, S. O. Gharan, and A. Saberi. 2012. “Online stochastic matching: Online actions based on offline statistics. ”Mathematics of
Operations Research, 37, 4, 559–573.
A. Mehta, A. Saberi, U. Vazirani, and V. Vazirani. 2007. “Adwords and generalized online matching. ”Journal of the ACM (JACM), 54, 5, 22–es.
R. B. Myerson and M. A. Satterthwaite. 1983. “Efficient mechanisms for bilateral trading. ”Journal of economic theory, 29, 2, 265–281.
L. Ouyang et al.. 2022. “Training language models to follow instructions with human feedback. ”Advances in neural information processing
systems, 35, 27730–27744.
E. Perez et al.. 2023. “Discovering language model behaviors with model-written evaluations. ” In:Findings of the association for computational
linguistics: ACL 2023, 13387–13434.
Qwen Team. 2025.Qwen3 Technical Report. (2025). https://arxiv.org/abs/2505.09388 arXiv: 2505.09388(cs.CL).
A. Rubinstein. 1982. “Perfect equilibrium in a bargaining model. ”Econometrica: Journal of the Econometric Society, 97–109.
A. Shah, D. Mishra, and C. Silpasuwanchai. 2026. “Too Nice to Tell the Truth: Quantifying Agreeableness-Driven Sycophancy in Role-Playing
Language Models. ”arXiv preprint arXiv:2604.10733.
Z. Shao et al.. 2024. “Deepseekmath: Pushing the limits of mathematical reasoning in open language models. ”arXiv preprint arXiv:2402.03300.
M. Sharma et al.. 2024. “Towards understanding sycophancy in language models. ” In:International Conference on Learning Representations.
Vol. 2024, 110–144.
D. Simchi-Levi, X. Chen, and J. Bramel. 2005.The logic of logistics: theory, algorithms, and applications for logistics and supply chain management.
Springer.
D. Simchi-Levi, Z. Zheng, and F. Zhu. 2025. “On greedy-like policies in online matching with reusable network resources and decaying
rewards. ”Management Science, 71, 10, 8908–8926.
A. Singh et al.. 2025. “Openai gpt-5 system card. ”arXiv preprint arXiv:2601.03267.
J. Srivastava, D. Chakravarti, and A. Rapoport. 2000. “Price and margin negotiations in marketing channels: An experimental study of
sequential bargaining under one-sided uncertainty and opportunity cost of delay. ”Marketing Science, 19, 2, 163–184.
R. S. Sutton and A. G. Barto. 2018.Reinforcement Learning: An Introduction (2nd Edition). MIT press.
K. T. Talluri and G. J. Van Ryzin. 2006.The theory and practice of revenue management. Vol. 68. Springer Science & Business Media.

Learning to Sell•27
Thinking Machines Lab. 2025.Tinker. (2025). https://thinkingmachines.ai/tinker/.
L. Wang et al.. 2024. “A survey on large language model based autonomous agents. ”Frontiers of Computer Science, 18, 6, 186345.
P. Wang, L. Li, Z. Shao, R. Xu, D. Dai, Y. Li, D. Chen, Y. Wu, and Z. Sui. 2024. “Math-shepherd: Verify and reinforce llms step-by-step without
human annotations. ” In:Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
9426–9439.
T. Xia, Z. He, T. Ren, Y. Miao, Z. Zhang, Y. Yang, and R. Wang. 2024. “Measuring bargaining abilities of llms: A benchmark and a buyer-
enhancement method. ” In:Findings of the Association for Computational Linguistics: ACL 2024, 3579–3602.
S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, and Y. Cao. 2022. “React: Synergizing reasoning and acting in language models. ”arXiv
preprint arXiv:2210.03629.
D. Yarats and M. Lewis. 2018. “Hierarchical text generation and planning for strategic dialogue. ” In:International Conference on Machine
Learning. PMLR, 5591–5599.
A. Zeng, M. Liu, R. Lu, B. Wang, X. Liu, Y. Dong, and J. Tang. 2024. “Agenttuning: Enabling generalized agent abilities for llms. ” In:Findings of
the Association for Computational Linguistics: ACL 2024, 3053–3077.
Y. Zhang, C. Chen, and N. Jiang. 2026. “Beyond Pessimism: Offline Learning in KL-regularized Games. ”arXiv preprint arXiv:2604.06738.
D. M. Ziegler, N. Stiennon, J. Wu, T. B. Brown, A. Radford, D. Amodei, P. Christiano, and G. Irving. 2019. “Fine-tuning language models from
human preferences. ”arXiv preprint arXiv:1909.08593.

28•Liu et al.
A Notation
Table 3 collects the notation used throughout the paper, grouped by the part of the framework each symbol
belongs to. Full definitions appear at each symbol’s point of first use in the main text.
Symbol Name Description
Episode parameters and indices (§3)
𝑛,𝑚Item and buyer counts Number of items and buyer slots per episode.
𝑗,𝑖Item and buyer indices Item index𝑗∈{1,...,𝑛}; buyer index𝑖∈{1,...,𝑚}.
𝑡Turn index Seller turn index𝑡.
𝑇,𝐾 Communication budget
and turn limit
Global communication budget (𝑇= 7in training) and per-buyer turn
limit (𝐾=3);𝑇<𝑚𝐾.
Prices, costs, and valuations (§3, §5.2, §9)
𝑃list,𝑗 List price Public list price of item𝑗.
C𝑗 Seller’s cost Seller’s private cost for item𝑗; always strictly below𝑃 list,𝑗 .
B𝑖,𝑗 ,B Buyer valuation; valua-
tion matrix
Buyer𝑖’s private valuation for item 𝑗; the full𝑚×𝑛 matrix, never
observed by the seller.
𝑃deal,𝑗 Deal price Agreed price when item𝑗sells; may exceed the list price.
𝑃final,𝑗 Final price𝑃 final,𝑗 :=min(𝑃 deal,𝑗, 𝑃list,𝑗); enters the reward and all surplus met-
rics.
U[𝑎,𝑏]Uniform distribution Uniform distribution on the interval[𝑎,𝑏].
𝑟𝑖,𝑗 Buyer valuation ratio𝑟 𝑖,𝑗 ∼U[0.40,1.15], i.i.d. across all(𝑖,𝑗)pairs.
𝜇 𝑗 ,𝛾 𝑖 Valuation multipliers Per-item and per-buyer valuation multipliers; both equal1in-
distribution and in Envs. 1–4. Env. 5 draws 𝜇 𝑗 ∼ U[0.5, 2] with
𝛾𝑖 =1, while Env. 6 draws𝛾 𝑖∼U[0.5,2]with𝜇 𝑗 =1.
Reward and seller metrics (§3.2, Section 6)
RTerminal reward−1on a violation episode, in[0,1]on a valid episode (equation (1)).
𝑆Sold-item set An episode’s set of items that closed a deal; the pool for the Deal on
Top Buyer Rate.
Allocation oracle (Section 6)
M★ Optimal-matching set Set of all surplus-maximizing matchings under list-clipped surplus
and the one-deal-per-buyer constraint.
𝐴,𝐴(𝑗)Realized allocation𝐴(𝑗)is the buyer who closed item𝑗;∅if item𝑗is unsold.
Table 3. Notation used throughout the paper, grouped by the part of the framework each symbol belongs to.
B Formal Definitions of Evaluation Metrics
This section provides the full mathematical formalizations of the allocation metrics introduced in Section 6,
anchored on the centralized oracle matching model defined below. Every metric is aggregated over the valid
episodes the seller completes without a violation, using the notation of Table 3.
B.1 Oracle Matching Model
The allocation metrics compare the seller’s realized allocation against the surplus-maximizing assignment of
items to buyers. We define the oracle optimal-matching set
M★ =arg max
𝑀
∑︁
(𝑗,𝑖)∈𝑀
 min(B𝑖,𝑗, 𝑃list,𝑗)−C 𝑗  +,(𝑥) + =max(0,𝑥),
where𝑀 ranges over matchings that assign each item to at most one buyer and each buyer to at most one item (a
partial, injective map from items to buyers, with𝑀(𝑗)=∅ marking item𝑗 unpaired). Each pair’s surplus is clipped

Learning to Sell•29
at the list price, so dollars a buyer would pay above the list price do not count;M★ is typically non-singleton,
and the empty matching is optimal exactly when no positive clipped surplus exists. We write𝐴 for the seller’s
realized allocation, with𝐴(𝑗)the buyer who closed item𝑗(∅if item𝑗is unsold).
B.2 Primary Allocation Metrics
Optimal-Pair Offer Coverage Rate.The fraction of oracle-optimal buyer–item pairs that the seller targets with a
[SELL] or[DEAL] action at least once during the episode, pooled across the valid episodes that admit a non-empty
optimal matching:
Optimal-Pair Offer Coverage Rate= Total Optimal Pairs Offered Total Pairs in Optimal Matching.
For each episode we select the optimal matching𝑀∈M ★ that overlaps most with the seller’s proposals; a pair
(𝑖,𝑗)∈𝑀 counts as offered whenever the seller names item 𝑗 to buyer𝑖 in at least one [SELL] or [DEAL] action,
regardless of whether a deal ultimately closes. The metric therefore scores matchingintentrather than final
execution.
Deal on Top Buyer Rate.The fraction of successfully sold items that cleared to the buyer holding the highest
private valuation for that item, pooled across all sold items of the valid episodes:
Deal on Top Buyer Rate=
˝
ep
˝
𝑗∈𝑆 1

𝐴(𝑗)∈arg max 𝑖B𝑖,𝑗

˝
ep|𝑆| ,
where𝑆 is the set of items sold in a given episode and1[·] is the indicator function. Ties are permissive: any
buyer attaining arg max𝑖B𝑖,𝑗 satisfies the indicator. Because one buyer may hold the highest valuation for several
substitutable items yet can close at most one under the one-deal-per-buyer constraint, a value below1does not
by itself imply a routing error.

30•Liu et al.
C In-Distribution Benchmarking Figure
This section provides a visual reference complementing the primary empirical benchmarking results discussed in
the main text. To clearly illustrate the performance margins across different model architectures, Figure 14 plots
the relative rankings and corresponding standard errors for the entire ten-model panel. The profiles shown below
are computed over identical, held-out instances, directly mirroring the exact numerical values reported in Table 1.
−0.4 −0.2 0.0 0.2 0.4 0.6
Qwen3-30B-A3B-Instruct-2507-trained (Ours)
Qwen3-30B-A3B-Instruct-2507-untrained
Kimi-K2.6-thinking
DeepSeek-V4-Pro-thinking
DeepSeek-V4-Pro-nothink
DeepSeek-V4-Flash-thinking
Kimi-K2.6-nothink
GPT-5.4-high-reasoning
DeepSeek-V4-Flash-nothink
GPT-5.4-mini-high-reasoning
+0.407
−0.329
+0.379
+0.369
+0.361
+0.349
+0.331
+0.309
+0.241
+0.111
Reward
(a) Reward
0.0 0.1 0.2 0.3 0.4 0.5
Qwen3-30B-A3B-Instruct-2507-trained (Ours)
Qwen3-30B-A3B-Instruct-2507-untrained
DeepSeek-V4-Pro-thinking
Kimi-K2.6-thinking
DeepSeek-V4-Pro-nothink
Kimi-K2.6-nothink
DeepSeek-V4-Flash-thinking
GPT-5.4-high-reasoning
DeepSeek-V4-Flash-nothink
GPT-5.4-mini-high-reasoning
+0.425
+0.184
+0.392
+0.379
+0.378
+0.378
+0.366
+0.315
+0.306
+0.212
Seller Surplus Extraction Ratio (b) Seller Surplus Extraction Ratio
0.0 0.2 0.4 0.6 0.8 1.0
Qwen3-30B-A3B-Instruct-2507-trained (Ours)
Qwen3-30B-A3B-Instruct-2507-untrained
Kimi-K2.6-nothink
DeepSeek-V4-Pro-nothink
GPT-5.4-high-reasoning
DeepSeek-V4-Pro-thinking
DeepSeek-V4-Flash-thinking
Kimi-K2.6-thinking
DeepSeek-V4-Flash-nothink
GPT-5.4-mini-high-reasoning
0.844
0.554
0.654
0.640
0.604
0.592
0.566
0.559
0.543
0.457
Optimal-Pair Offer Coverage Rate
(c) Optimal-Pair Offer Coverage Rate
0.0 0.2 0.4 0.6 0.8
Qwen3-30B-A3B-Instruct-2507-trained (Ours)
Qwen3-30B-A3B-Instruct-2507-untrained
Kimi-K2.6-nothink
DeepSeek-V4-Pro-thinking
DeepSeek-V4-Pro-nothink
DeepSeek-V4-Flash-thinking
Kimi-K2.6-thinking
GPT-5.4-high-reasoning
DeepSeek-V4-Flash-nothink
GPT-5.4-mini-high-reasoning
0.687
0.544
0.616
0.612
0.596
0.568
0.566
0.560
0.538
0.465
Deal on T op Buyer Rate (d) Deal on Top Buyer Rate
Fig. 14.In-distribution performance benchmarking (3buyers,3items, 𝑇= 7).Per-metric seller rankings on byte-
identical in-distribution held-out instances. The trained model (Ours) and its untrained base appear above the rule, the
frontier baselines below. Error bars show the standard error. Values match Table 1.
D Training Implementations
This appendix collects the implementation details required to reproduce the training and evaluation pipeline. Sec-
tion D.1 specifies the seller and buyer models together with the checkpoints they are initialized from, Section D.2
lists the optimization and rollout hyperparameters used for the RLVR run and for evaluation, and Section D.3
gives the configuration of the out-of-distribution environments.
D.1 Multi-Item Seller Setting — Model Specifications
The only learning agent in this paper is theseller; all buyer checkpoints remain frozen. This one-sided training
setup differs from equilibrium-learning formulations in which multiple strategic responses are optimized jointly or

Learning to Sell•31
iteratively, including offline zero-sum, general-sum, and potential-game settings (C. Chen and Y. Zhang 2026a,b;
C. Chen, Y. Zhang, et al. 2026; Y. Zhang et al. 2026). Both the seller and buyers share the same base model,
Qwen3-30B-A3B-Instruct-2507 (Qwen Team 2025). During training and in-distribution evaluation, buyers use
the iteration-60checkpoint from a bilateral (one-on-one) negotiation RLVR run (S. D. Liu, C. Chen, Xiao, L. Lei,
et al. 2026); OOD buyer checkpoints are specified in Table 4.
Role Base model Provenance / checkpoint
Seller Starting
Checkpoint
Qwen/Qwen3-30B-A3B-
Instruct-2507(Qwen Team 2025) Original checkpoint from (Qwen Team 2025); fine- tuned as the seller.
Buyers in Training Qwen/Qwen3-30B-A3B- Instruct-2507 Frozen buyer checkpoint iteration60(iter-60), trained via RLVR on a bilateral negotiation task (S. D. Liu, C.
Chen, Xiao, L. Lei, et al. 2026).
Buyers in Evaluation Qwen/Qwen3-30B-A3B- Instruct-2507 In-distribution evaluation: fixed iter-60. Out-of- distribution evaluation: per-buyer uniform over the
pool{iter-50,iter-60,iter-70}.
Table 4. Models used by the multi-item-seller pipeline. The seller is the trained agent; the buyers are frozen checkpoints
from S. D. Liu, C. Chen, Xiao, L. Lei, et al. (2026).
For benchmark comparisons in the held-out evaluation, the trained seller is contrasted against nine other seller
models listed in Table 5.
Model Name Parameter Count Reference
Qwen3-30B-A3B-Instruct-2507-trained (Ours) 30B This Work
Qwen3-30B-A3B-Instruct-2507-untrained 30B Qwen Team (2025)
GPT-5.4-high-reasoning closed-source Singh et al. (2025)
GPT-5.4-mini-high-reasoning closed-source Singh et al. (2025)
DeepSeek-V4-Pro-thinking / nothink 1.6T DeepSeek-AI (2026)
DeepSeek-V4-Flash-thinking / nothink 284B DeepSeek-AI (2026)
Kimi-K2.6-thinking / nothink 1T Kimi Team et al. (2025)
Table 5. Seller models evaluated in the held-out benchmark, with total parameter counts. Three open-weight models are run
in both a thinking and a no-thinking (nothink) mode, giving a10-model panel. DeepSeek-V4-Pro is a mixture-of-experts
model with1.6T total /49B active parameters; DeepSeek-V4-Flash has284B total /13B active parameters. The buyer is held
fixed across the panel (Table 4).
D.2 Training and Evaluation Hyperparameters
The seller is fine-tuned with reinforcement learning via Tinker (Thinking Machines Lab 2025). The run reported
in this paper uses the CISPO loss (A. Chen et al. 2025) with clipping thresholds(0.8, 6.0). One step denotes one
optimization step over a sampled batch of episodes. Tables 6, 7, and 8 list the hyperparameters that control the
configuration. We did not conduct a systematic hyperparameter search; only the configuration reported in these
tables was considered. All settings were fixed before the final experiments, and neither the held-out test set nor
the OOD evaluation sets were used for hyperparameter selection.

32•Liu et al.
Setting Value
loss function cispo
CISPO clip low / high0.8/6.0
Learning rate3×10 −5
KL penalty (kl coef)0
batch size64
group size8
num substeps3
epochs1
base environment seed42
Table 6. Optimization hyperparameters for the RL training run.
Setting Value
num buyers𝑚3
num items𝑛3
total turns𝑇7
per-buyer turn limit𝐾3
valuation ratio distributionU[0.40,1.15]
first-offer-noise probability0.5
first-offer-noise ratio range[0.25,0.30]·𝑃 list,𝑗
seller temperature1.0
buyer temperature0.7
Table 7. Environment hyperparameters for training. Each buyer valuation entry isB𝑖,𝑗 =𝑟𝑖,𝑗 𝑃list,𝑗 with𝑟𝑖,𝑗∼U[ 0.40, 1.15]
drawn i.i.d. across all(𝑖,𝑗) pairs. First-offer noise is applied independently to each buyer with probability0.5: at episode start,
a buyer selected for first-offer noise has its opening offer on every chosen item resampled into[0.25, 0.30]·𝑃 list,𝑗 , decoupling
the opening from the buyer’s private valuation; otherwise the buyer generates its opening offer freely subject to its private
valuation constraint.
Setting Value
seller model All models from Table 5
buyer model Qwen3-30B-A3B-Instruct-2507 iter-60(Table 4)
Test split size240held-out clusters
seller temperature (eval)0.7
buyer temperature (eval)0.7
Table 8. Evaluation hyperparameters for the held-out test split. The240test clusters are the20%cluster-level hold-out from
the12in-distribution categories (Section 4); product contexts are unseen during training.

Learning to Sell•33
D.3 Out-of-Distribution Evaluation Setup
The out-of-distribution (OOD) result tables report several environments that each perturb the in-distribution
setting of Section 5.2 along one or more axes. The in-distribution reference uses 𝑚= 3buyers, 𝑛= 3items,
and a total communication budget𝑇= 7with a fixed iter-60buyer and the uniform valuation matrix. Across
all OOD environments the buyer agent is instead sampled per buyer per episode, uniformly from the pool
{iter-50,iter- 60,iter- 70} of the buyer training run, so the seller never faces a memorized single counterpart.
The remaining axes vary as follows: a widened5-buyer /5-item / 𝑇= 12environment under the same uniform
valuation; the same widened environment with a per-item valuation multiplier 𝜇𝑗 ∼U[ 0.5, 2] (some items
universally more valued); the same widened environment with a per-buyer generosity multiplier𝛾𝑖∼U[ 0.5, 2]
(some buyers universally more willing to pay); a5-buyer /3-item / 𝑇= 12environment that scales only the
buyer count; a3-buyer /5-item / 𝑇= 7environment that scales only the item count; and a held-out Musical
Instruments environment that keeps the widened5-buyer /5-item / 𝑇= 12shape but draws every catalog from
the13th category, whose higher list-price range moves the absolute valuation and cost scale outside the training
distribution. Table 9 summarizes the environments.
Environment Buyers𝑚Items𝑛Turns𝑇Valuation Catalog
In-distribution (reference)3 3 7uniform12categories
Env. 1: Expanded Standard5 5 12uniform12categories
Env. 2: Expanded Musical5 5 12uniform Musical Instruments
Env. 3: Buyer Heavy5 3 12uniform12categories
Env. 4: Item Heavy3 5 7uniform12categories
Env. 5: Item Correlation5 5 12uniform×𝜇 𝑗 12categories
Env. 6: Buyer Correlation5 5 12uniform×𝛾 𝑖 12categories
Table 9. Per-episode environment knobs for the in-distribution reference and the out-of-distribution evaluation environments.
“uniform” denotes the in-distribution valuationB𝑖,𝑗 =𝑟 𝑖,𝑗 𝑃list,𝑗 with𝑟𝑖,𝑗 ∼U[ 0.40, 1.15]. Env. 5 (Item Correlation) draws
𝜇𝑗∼U[ 0.5, 2] once per item with𝛾𝑖 = 1, while Env. 6 (Buyer Correlation) draws𝛾𝑖∼U[ 0.5, 2] once per buyer with𝜇𝑗 = 1.
The in-distribution reference uses the fixed iter-60buyer; every OOD environment samples each buyer slot uniformly from
the pool{iter-50,iter-60,iter-70}. First-offer noise (Table 7) is applied in every environment.
E Dataset Details
This section records construction details, additional statistics, a complete example cluster, and schema notes for
the substitutable-product dataset of Section 4.
E.1 Construction Details
The dataset was assembled in three stages. First, a language model proposed candidate narrow product types
within each of the13broad Amazon categories, serving as cluster seeds. Second, for every candidate type,
the best-selling Amazon products of that type were retrieved through Keepa (the third-party Amazon catalog
and price-history service introduced in Section 4), restricted to products whose category ancestry matches the
candidate’s broad category and that pass basic per-product checks (a valid list price, available metadata, an
identifiable cost). Third, an automated substitutability review examined each candidate set and kept only products
a buyer could genuinely swap for one another—same function, same use case—writing a short rationale for every

34•Liu et al.
Broad Category Mean Distinct Brands Median List Price Median Cluster Min Price Median Cluster Max Price Median Price Spread
Appliances 4.3 $109.98 $79.99 $159.99 1.71×
Automotive 4.3 $45.86 $31.49 $59.99 2.00×
Baby 4.5 $34.99 $28.24 $48.97 1.61×
Beauty & Personal Care 4.5 $29.99 $22.49 $43.98 1.79×
Clothing, Shoes & Jewelry 4.4 $36.49 $29.95 $49.99 1.73×
Electronics 3.9 $139.99 $99.79 $199.99 1.95×
Home & Kitchen 4.6 $46.99 $35.99 $61.49 1.88×
Musical Instruments 4.1 $165.49 $88.26 $248.84 2.40×
Patio, Lawn & Garden 4.6 $69.99 $59.99 $99.99 1.91×
Pet Supplies 4.7 $33.49 $22.74 $45.49 1.75×
Sports & Outdoors 4.4 $39.99 $32.49 $59.99 1.81×
Tools & Home Improvement 4.3 $59.95 $39.99 $80.00 2.00×
Toys & Games 4.5 $31.99 $24.74 $43.46 1.82×
Total4.4 $47.99 $34.08 $62.99 1.85×
Table 10. Per-category statistics of the substitutable-product dataset. Every category contributes100clusters of5substitutable
products (500products per category;1 ,300clusters and6 ,500products in total). Brand counts are means over a category’s
100clusters; prices are medians; the within-cluster price spread 𝑠=𝑃 max/𝑃min is computed over each cluster’s5list prices
and reported as the per-category median.
kept set; candidate types without a substitutable core were discarded. All prices, costs, sales rankings, and product
text are a snapshot taken between May 13 and May 17, 2026.
E.2 Additional Statistics and Category Breakdowns
This section provides an expanded empirical look at the dataset profiles across all 13 product categories. Table 10
reports the per-category statistics and Figure 3 visualizes the composition. The corpus is balanced by construction:
every category contributes exactly100clusters of5products. Clusters are genuinely multi-brand—4 .4distinct
brands per cluster on average, and59%of clusters carry5distinct brands—so the seller cannot collapse the
catalog into a single-brand pitch. Within a cluster, the median price spread, defined as𝑠=𝑃 max/𝑃min over the
cluster’s5list prices, is1 .85× corpus-wide, giving the seller meaningful headroom to steer buyers across price
tiers. Median prices also differ sharply across categories—from $29.99 in Beauty & Personal Care to $165.49 in
Musical Instruments—an asymmetry the out-of-distribution split below exploits.
Furthermore, Figure 16 shows the distribution of the within-cluster price spread 𝑠=𝑃 max/𝑃min and of the
distinct-brand count across all1,300clusters. Spreads concentrate between1 .5× and2.4× (quartiles1.50,1.85,
2.37), with Musical Instruments carrying the widest per-category median spread (2.40×) and Baby the narrowest
(1.61×). Brand diversity is high:59%of clusters carry5distinct brands among their5products and84%carry at
least4, so brand-conditioned buyer preferences rarely collapse onto a single pitch.
E.3 Example Cluster
The boxes below reproduce the dataset record behind the qualitative example of Appendix H: the video-recorder
cluster (Video Recorders, Electronics)—one box with the cluster-level fields, followed by one box per product,
covering the three items of the episode catalog (Section H.1) and two further products of the cluster. The product
features are truncated to their first200characters for display. The lowest all-time price—the lowest price at which
the product was ever sold on Amazon—is the product’s seller costC 𝑗 (Section 4).

Learning to Sell•35
$10 $100 $1000
List price ($, log scale)
0.0
0.1
0.2
0.3
0.4
0.5
0.6Density
List Price Distribution
12 categories (N=6,000)
Musical Instruments (N=500)
Fig. 15. List price distribution of the dataset’s6,500prod-
ucts on a log scale: Musical Instruments (𝑁=500, red) ver-
sus the12remaining categories pooled ( 𝑁=6,000, blue).
Musical Instruments concentrates in a visibly higher
price range, motivating its selection as the held-out out-
of-distribution category.
1 2 3 4 5 6
Within-cluster price spread (max / min list price)
0
5
10
15
20Percent of clusters
Within-Cluster Price Spread
1 2 3 4 5
Distinct brands per cluster (of 5 products)
0
10
20
30
40
50
60Percent of clusters
Distinct Brands per Cluster
Fig. 16. Distributions over the1 ,300clusters of (left) the within-cluster price spread 𝑠=𝑃 max/𝑃min, with the24clusters whose
spread exceeds6×folded into the last bin, and (right) the number of distinct brands among each cluster’s5products.
Cluster Information
Broad Category: Electronics
Narrow Product Type: Video Recorders
Leaf Category ID:14241611
Product ASINs:B0749F32T1,B08LSRT2JB,B06WP6Q898,B01DELNN82,B0DB1XN58W
Number of Products: 5
Minimum List Price: $55.99
Maximum List Price: $419.99
Distinct Brands: 4
Seller Type Counts:third_party_only(3),amazon(2)
Product 1: ANNKE
ASIN:B0749F32T1
Title: “ANNKE 3K Lite 8 Channel Hybrid 5-in-1 Security Digital Video Recorder, H.265+ Surveillance DVR Supports 8CH
Analog and 2CH 6MP IP Cameras, Remote Access, AI Human&Vehicle Detection, 1TB Hard Drive”

36•Liu et al.
Features: “5-in-1 Hybrid DVR – This expandable hybrid DVR combines DVR, NVR and HVR features. It supports up to 8
cameras, including 720P/960H/1080P/5MP (20fps) analog HD-TVI, CVI, AHD, CVBS, plus 2 extra IP cam ... ”
Brand: ANNKE
List Price: $169.99
Lowest Price All-Time: $55.99
Seller Type:third_party_only
Narrow Product Type: Video Recorders
Broad Category: Electronics
Product 2: Lorex
ASIN:B08LSRT2JB
Title: “Lorex 4K Ultra HD 8-Channel Fusion Series PoE Network Video Recorder with 2TB Storage, Smart Motion
Detection and Smart Home Compatibility”
Features: “4K ULTRA HD - Record and view impressive 4K video resolution with a cutting-edge recorder, providing you
with superior detail and definition. LOREX FUSION - As part of the Lorex Fusion collection, you ... ”
Brand: Lorex
List Price: $249.99
Lowest Price All-Time: $100.00
Seller Type:third_party_only
Narrow Product Type: Video Recorders
Broad Category: Electronics
Product 3: ZOSI
ASIN:B06WP6Q898
Title: “ZOSI H.265+ 8 Channel 5MP Lite 1080p CCTV DVR Recorder Without HDD, Hybrid Capability 4-in-
1(Analog/AHD/TVI/CVI) Surveillance DVR for Security Camera, Remote Access, Human Vehicle Detect, Alert Push”
Features: “(1). [ AI Human & Vehicle Detection for Accurate Alerts] __ Equipped with advanced AI technology, this DVR
system intelligently detects humans and vehicles, reducing false alarms caused by animals or ... ”
Brand: ZOSI
List Price: $55.99
Lowest Price All-Time: $42.07
Seller Type:amazon
Narrow Product Type: Video Recorders
Broad Category: Electronics
Product 4: REOLINK
ASIN:B01DELNN82
Title: “REOLINK 16CH Network Video Recorder for Home Security Camera System,Only Work with
16MP/12MP/4K/8MP/5MP/4MP The Same Brand PoE IP Cam,24/7 Recording to Pre-Installed 4TB Hard Drive,RLN16-410”
Features: “ONLY WORK WITH REOLINK IP CAMERAS: Work perfectly with all Reolink PoE 16MP/12MP/4K/5MP/4MP
cameras, such as Duo 3 PoE, RLC-1212A, RLC-1224A, RLC-823A 16X, Trackmix PoE, Duo 2 PoE, 811A, 810A, 820A, 5 ... ”
Brand: REOLINK
List Price: $419.99
Lowest Price All-Time: $271.99
Seller Type:amazon

Learning to Sell•37
Narrow Product Type: Video Recorders
Broad Category: Electronics
Product 5: REOLINK
ASIN:B0DB1XN58W
Title: “REOLINK Home Hub Pro, Centralized Control for up to 24 REOLINK Security Cameras, up to 16TB HDD Storage,
2TB HDD Included, AES-128 Encryption, 16MP Streaming, Wi-Fi 6, 120dB Siren. No Monthly Fees”
Features: “All-In-One Control & Storage Center: Centralized storage & alarm management for all Reolink cams - wired,
wireless, PoE & doorbells (excluding 4G devices) on the portable App. Effortlessly monitor up ... ”
Brand: REOLINK
List Price: $339.99
Lowest Price All-Time: $179.99
Seller Type:third_party_only
Narrow Product Type: Video Recorders
Broad Category: Electronics
E.4 Dataset Structure and Details
Each cluster row contains basic market details, including the broad product category, the specific product type,
unique product IDs, the number of distinct brands, the price range, and a short explanation of why the items
can be substituted for one another. Within these clusters, individual product records track product titles, brands,
public list prices, the lowest historical price (used as the seller’s cost), and where the product is sold.
The dataset also includes two text fields: a long product description and a bulleted list of features. While long
descriptions are only available for about a third of the products, the bulleted feature lists are included for every
item. Because these feature lists are always present, the negotiation system uses them as the main text to show
product details during our tests.
F Prompt Templates
This section reproduces, verbatim, the system prompts that define the two roles of the multi-item negotiation.
Both roles are played by the same base model,Qwen3-30B-A3B-Instruct-2507 (Qwen Team 2025): the seller
is the trained checkpoint; buyer slots use the frozen iteration-60checkpoint of a bilateral-negotiation RLVR
run (S. D. Liu, C. Chen, Xiao, L. Lei, et al. 2026) (Section 5.1) during training and in-distribution evaluation,
while OOD evaluation uses the checkpoint pool described in Section D.3. The two prompts establish the XML
action grammar, the action space ([SELL]/[DEAL]/[QUIT] for the seller,[BUY]/[DEAL]/[QUIT] for the buyer),
and the information partition that separates each agent’s private reasoning ( <negotiation_thought>) from
its public message (<talk>) and formal move (<action>). The seller prompt is a .format() template whose
five placeholders are substituted per episode; the buyer prompt is a fixed string. Each agent’s per-episode
context—catalog, valuations, and standing state—is supplied through the user turns and is not shown here.
F.1 Seller System Prompts
The seller’s system prompt is the mechanics-only template below. Its five placeholders—{m}, {n}, {K}, {T}, and
the seller-facing{catalog_block}—are substituted at runtime with the per-episode constants and the catalog
listing (one line per item, each carrying the item’s public list price and the seller’s private cost; Section 5.2).

38•Liu et al.
System Prompt for Seller
You are a seller negotiating an n-item catalog with m buyers in parallel.
# Symbols
•𝑖∈{1,...,𝑚}— buyer index.
•𝑗∈{1,...,𝑛}— item index in the catalog.
•cost_j— your private reservation cost for item j (never sell below this).
•list_price_j— public list price for item j (buyers can see this).
•p_deal,j — the agreed price at which item j is sold (defined only when item j closes; MAY exceedlist_price_j).
•p_final,j = min(p_deal,j, list_price_j): the list-clipped price that enters the reward numerator.
•B_{i,j}— buyer i’s private per-item budget for item j (you never see this).
Your goal is to maximize the catalog-wide reward:
R = sum_j (p_final,j - cost_j) *1[item j sold] / sum_j (list_price_j - cost_j)
𝑅∈[ 0, 1] on a valid episode;𝑅=− 1on any seller violation. Selling above list is allowed, but dollars abovelist_price_j
do not count (numerator clips at list).
A seller violation is any of:
(i) a priced[SELL]or[DEAL]at$M < cost_jfor some item j;
(ii)<target>naming a buyer whose status is not active;
(iii)[SELL]listing an item j that has already closed in a prior deal;
(iv)<target>missing, unparseable, or out of range;
(v) the reply does not parse into the four XML tags below.
# Output format
Every reply MUST be exactly four XML tags, in this order (<negotiation_thought>,<target>,<talk>,<action>):
•<negotiation_thought>your hidden reasoning; not sent to buyers.</negotiation_thought>
•<target>Buyer i</target>(i in 1..m, currently active)
•<talk>short message; visible only to the Targeted buyer</talk>
•<action>EXACTLY ONE of the three action forms below</action>
Where the action inside<action>...</action>is exactly one of:
•[SELL] [<codename_1, $M_1>, <codename_2, $M_2>, ...] — pitch any subset of available items, one price
each.
•[DEAL] codename_j $M— accept the Targeted buyer’s standing[BUY] codename_j $M(price must match).
•[QUIT]— end the episode.
# Episode constants
m = {m}buyersn = {n}items
K = {K}per-buyer message capT = {T}total seller-message budget (T < m*K)
# Item catalog (private — buyers see only list prices, never your cost)
{catalog_block}
# Conversation mechanics
• Turn 1: each buyer sends an opening offer naming a subset of items at proposed prices. Items not opened on
turn 1 remain pitchable via[SELL].
•Later turns: the buyer you Target replies; others stay silent.
• A buyer sees ONLY your <talk> and <action> — never <negotiation_thought>, <target>, or any other
buyer’s dialogue.
•Buyers’ budgetsB_{i,j}are private (see Symbols).
• Each buyer can close at most one item. After their [DEAL], they become satisfied and cannot be Targeted again.

Learning to Sell•39
•[DEAL] only closes against a standing [BUY] from the Targeted buyer — the item and price must match an
outstanding[BUY]from them.
•An item sold to one buyer is removed from the catalog; listing it in a later[SELL]is a violation.
• The most recent user message ends with === Standing offers ===; that block is the freshest source of truth.
You must limit your reply under 400 tokens for all 4 parts combined.
F.2 Buyer System Prompts
During training and in-distribution evaluation, every buyer slot is filled by the same base model as the seller,
Qwen3-30B-A3B-Instruct-2507, frozen at the iteration-60checkpoint of a bilateral-negotiation RLVR run (S. D.
Liu, C. Chen, Xiao, L. Lei, et al. 2026). Across the out-of-distribution evaluations, each buyer slot is instead
sampled per episode from the checkpoint pool{iter-50,iter- 60,iter- 70} of the same buyer training trajectory. In
both cases only the seller’s parameters update during training. The buyer system prompt is the fixed string below,
with a token-budget rider appended (last paragraph). It carries no placeholders: the per-episode valuation vector,
the buyer-facing item board, and the optional first-offer block are delivered through the buyer’s user turns.
System Prompt for Buyer
You are a buyer negotiating with one seller against an n-item catalog of substitutable items. You may close at most ONE
item; once you[DEAL], the negotiation ends for you.
# Output format
Every reply MUST be exactly three XML tags, in this order:
•<negotiation_thought>your hidden reasoning; not sent to the seller.</negotiation_thought>
•<talk>short message; visible to the seller</talk>
•<action>EXACTLY ONE of the three action forms below</action>
Where the action inside<action>...</action>is exactly one of:
•[BUY] [<codename_1, $M_1>, <codename_2, $M_2>, ...] — propose buying any subset (1..n) of currently-
available items, with one price per item. Each price must be at most your private budget for that item ($M_j <=
B_{i,j}); the env rejects an over-budget bid.
•[DEAL] codename_j $M — accept the seller’s standing[SELL] codename_j $Mfor that item at the exact price
$Mthey offered. Singleton — closes exactly one item.
•[QUIT]— end your participation in the episode.
# Conversation mechanics
• You cannot propose to BUY an item that has already been sold. The user message includes a “Available / Sold”
board telling you which codenames are valid targets.
# Reward (terminal only)
For each item you might close, your bargained ratio is:
rho = (B_{i,j} - p_deal_j) / (B_{i,j} - cost_j)
wherep_deal_jis the price you actually pay. A lowerp_deal_jis better. You can only close one item this episode.
Constraint: each reply you produce must be at most 300 tokens in total (Thought, Talk, and Action combined).
The optional first-offer block, when present, is appended to a buyer’s first user turn and implements the first-offer
noise of Section 5.2: at episode start each buyer independently, with probability0.5, has its opening offer on every
chosen item resampled into[0.25, 0.30]·𝑃 list,𝑗 independently of its true valuation, while otherwise the buyer

40•Liu et al.
opens freely within its private valuation bound. When active for a buyer, the block pins those opening prices for
that buyer’s first reply only; from its second reply onward the buyer bids freely within its per-item budget.
G Extended Benchmarking Results
This section presents the complete evaluation tables for Section 7 and Section 9. The in-distribution evaluation
reports sample means alongside their corresponding standard errors ( mean±standard error ) computed over
the full evaluation episode corpus. For each out-of-distribution environment we provide a point-estimate table
matching the main-text layout together with a companion table carrying the corresponding standard errors. The
point-estimate tables for Envs. 1–6 are Tables 12, 14, 16, 18, 20 and 22, respectively. The model evaluation panel
and metric column structures mirror the main-text layouts, with top-performing values highlighted in bold and
second-best values underlined.
All seller metrics reported here are estimated from direct episode rollouts rather than through off-policy
estimators or optimized data-collection policies; the latter address complementary questions of variance and
sample efficiency in reinforcement-learning policy evaluation (C. Chen, S. Liu, et al. 2025; C. Chen, S. D. Liu, et al.
2026; S. Liu, C. Chen, et al. 2025; S. Liu, Y. Chen, et al. 2025; S. Liu and S. Zhang 2024; S. D. Liu 2025).
Model Params Reward↑
Seller Surplus
Extraction
Ratio
Item
Deal
Rate
Deal on
Top Buyer
Rate
Optimal-Pair
Offer Coverage
Rate
Instruction
Violation
Rate
Qwen3-30B-A3B-Instruct-2507-trained (Ours) 30B +0.407±0.018 +0.425±0.015 64.7%±1.6% 0.687±0.022 0.844±0.014 1.3%±0.7%
Qwen3-30B-A3B-Instruct-2507-untrained 30B −0.329±0.039 +0.184±0.015 66.2%±2.4% 0.544±0.030 0.554±0.026 43.3%±3.2%
Kimi-K2.6-thinking 1T+0.379±0.013 +0.379±0.013 73.0%±1.5% 0.566±0.022 0.559±0.0200.0%±0.0%
DeepSeek-V4-Pro-thinking 1.6T+0.369±0.018+0.392±0.015 73.4%±1.6% 0.612±0.021 0.592±0.020 1.7%±0.8%
DeepSeek-V4-Pro-nothink 1.6T+0.361±0.017+0.378±0.014 76.2%±1.6% 0.596±0.021 0.640±0.019 1.3%±0.7%
DeepSeek-V4-Flash-thinking 284B+0.349±0.017+0.366±0.014 71.0%±1.7% 0.568±0.022 0.566±0.020 1.3%±0.7%
Kimi-K2.6-nothink 1T+0.331±0.021+0.378±0.013 75.0%±1.5% 0.616±0.021 0.654±0.019 3.4%±1.2%
GPT-5.4-high-reasoning closed-source+0.309±0.014+0.315±0.01378.1%±1.4% 0.560±0.021 0.604±0.020 0.4%±0.4%
DeepSeek-V4-Flash-nothink 284B+0.241±0.022+0.306±0.013 73.4%±1.6% 0.538±0.022 0.543±0.020 5.0%±1.4%
GPT-5.4-mini-high-reasoning closed-source+0.111±0.025+0.212±0.013 72.3%±1.8% 0.465±0.023 0.457±0.020 8.4%±1.8%
Table 11.In-distribution held-out evaluation, full results(3buyers,3items,𝑇=7).
Model Params Reward↑
Seller Surplus
Extraction
Ratio
Item
Deal
Rate
Deal on
Top Buyer
Rate
Optimal-Pair
Offer Coverage
Rate
Instruction
Violation
Rate
Qwen3-30B-A3B-Instruct-2507-trained (Ours) 30B +0.444 +0.493 70.8% 0.594 0.699 3.3%
Qwen3-30B-A3B-Instruct-2507-untrained 30B −0.187 +0.240 74.1% 0.384 0.378 34.5%
Kimi-K2.6-thinking 1T+0.322 +0.345 75.9% 0.398 0.402 1.7%
DeepSeek-V4-Pro-nothink 1.6T+0.308+0.347 81.5% 0.417 0.426 2.9%
DeepSeek-V4-Flash-thinking 284B+0.268+0.353 77.1% 0.388 0.398 6.3%
GPT-5.4-high-reasoning closed-source+0.265+0.26582.8% 0.363 0.4390.0%
DeepSeek-V4-Flash-nothink 284B+0.204+0.326 78.0% 0.392 0.422 9.2%
Kimi-K2.6-nothink 1T+0.140+0.328 82.0% 0.426 0.420 14.2%
DeepSeek-V4-Pro-thinking 1.6T+0.133+0.396 79.0% 0.418 0.444 18.8%
GPT-5.4-mini-high-reasoning closed-source+0.035+0.212 78.3% 0.354 0.381 14.6%
Table 12.Out-of-distribution Env. 1, Expanded Standard (5buyers,5items, 𝑇= 12, uniform valuation)with the
diverse buyer pool. Baselines sorted byReward(descending); best per column in bold, second-best underlined (Instruction
Violation Rateis lower-is-better). Metric definitions in Section 6. Standard errors in Table 13.

Learning to Sell•41
Model Params Reward↑
Seller Surplus
Extraction
Ratio
Item
Deal
Rate
Deal on
Top Buyer
Rate
Optimal-Pair
Offer Coverage
Rate
Instruction
Violation
Rate
Qwen3-30B-A3B-Instruct-2507-trained (Ours) 30B +0.444±0.022 +0.493±0.013 70.8%±1.3% 0.594±0.017 0.699±0.014 3.3%±1.2%
Qwen3-30B-A3B-Instruct-2507-untrained 30B −0.187±0.039 +0.240±0.012 74.1%±1.7% 0.384±0.020 0.378±0.018 34.5%±3.1%
Kimi-K2.6-thinking 1T+0.322±0.016 +0.345±0.012 75.9%±1.4% 0.398±0.016 0.402±0.015 1.7%±0.8%
DeepSeek-V4-Pro-nothink 1.6T+0.308±0.018+0.347±0.011 81.5%±1.1% 0.417±0.016 0.426±0.015 2.9%±1.1%
DeepSeek-V4-Flash-thinking 284B+0.268±0.024+0.353±0.011 77.1%±1.3% 0.388±0.017 0.398±0.015 6.3%±1.6%
GPT-5.4-high-reasoning closed-source+0.265±0.010+0.265±0.01082.8%±1.1% 0.363±0.016 0.439±0.0150.0%±0.0%
DeepSeek-V4-Flash-nothink 284B+0.204±0.027+0.326±0.012 78.0%±1.2% 0.392±0.017 0.422±0.015 9.2%±1.9%
Kimi-K2.6-nothink 1T+0.140±0.032+0.328±0.011 82.0%±1.1% 0.426±0.017 0.420±0.016 14.2%±2.3%
DeepSeek-V4-Pro-thinking 1.6T+0.133±0.037+0.396±0.012 79.0%±1.3% 0.418±0.018 0.444±0.016 18.8%±2.5%
GPT-5.4-mini-high-reasoning closed-source+0.035±0.029+0.212±0.010 78.3%±1.5% 0.354±0.017 0.381±0.016 14.6%±2.3%
Table 13.Out-of-distribution (5buyers,5items,𝑇=12, uniform valuation), full results.
Model Params Reward↑
Seller Surplus
Extraction
Ratio
Item
Deal
Rate
Deal on
Top Buyer
Rate
Optimal-Pair
Offer Coverage
Rate
Instruction
Violation
Rate
Qwen3-30B-A3B-Instruct-2507-trained (Ours) 30B +0.438 +0.483 69.5% 0.550 0.699 3.0%
Qwen3-30B-A3B-Instruct-2507-untrained 30B −0.129 +0.253 75.4% 0.349 0.329 30.5%
Kimi-K2.6-thinking 1T+0.303 +0.337 74.8% 0.418 0.406 2.5%
DeepSeek-V4-Pro-nothink 1.6T+0.281+0.37181.9% 0.433 0.459 6.5%
GPT-5.4-high-reasoning closed-source+0.260+0.260 81.5% 0.378 0.4580.0%
DeepSeek-V4-Flash-nothink 284B+0.238+0.310 78.2% 0.367 0.419 5.5%
DeepSeek-V4-Flash-thinking 284B+0.208+0.327 74.1% 0.384 0.409 9.0%
Kimi-K2.6-nothink 1T+0.148+0.312 81.3% 0.366 0.370 12.5%
DeepSeek-V4-Pro-thinking 1.6T+0.141+0.384 77.7% 0.444 0.426 17.6%
GPT-5.4-mini-high-reasoning closed-source−0.042+0.198 73.1% 0.366 0.357 20.0%
Table 14.Out-of-distribution Env. 2, Expanded Musical (held-out Musical Instruments category)(5buyers,5items,
𝑇= 12, uniform valuation). Baselines sorted byReward(descending); best per column in bold, second-best underlined
(Instruction Violation Rateis lower-is-better). Metric definitions in Section 6. Standard errors in Table 15.
Model Params Reward↑
Seller Surplus
Extraction
Ratio
Item
Deal
Rate
Deal on
Top Buyer
Rate
Optimal-Pair
Offer Coverage
Rate
Instruction
Violation
Rate
Qwen3-30B-A3B-Instruct-2507-trained (Ours) 30B +0.438±0.023 +0.483±0.015 69.5%±1.5% 0.550±0.019 0.699±0.015 3.0%±1.2%
Qwen3-30B-A3B-Instruct-2507-untrained 30B −0.129±0.042 +0.253±0.013 75.4%±1.7% 0.349±0.021 0.329±0.018 30.5%±3.3%
Kimi-K2.6-thinking 1T+0.303±0.020 +0.337±0.014 74.8%±1.6% 0.418±0.018 0.406±0.016 2.5%±1.1%
DeepSeek-V4-Pro-nothink 1.6T+0.281±0.027+0.371±0.01381.9%±1.2% 0.433±0.018 0.459±0.017 6.5%±1.7%
GPT-5.4-high-reasoning closed-source+0.260±0.012+0.260±0.012 81.5%±1.2% 0.378±0.017 0.458±0.0170.0%±0.0%
DeepSeek-V4-Flash-nothink 284B+0.238±0.025+0.310±0.013 78.2%±1.3% 0.367±0.018 0.419±0.017 5.5%±1.6%
DeepSeek-V4-Flash-thinking 284B+0.208±0.029+0.327±0.013 74.1%±1.4% 0.384±0.019 0.409±0.017 9.0%±2.0%
Kimi-K2.6-nothink 1T+0.148±0.033+0.312±0.013 81.3%±1.3% 0.366±0.018 0.370±0.017 12.5%±2.3%
DeepSeek-V4-Pro-thinking 1.6T+0.141±0.039+0.384±0.015 77.7%±1.5% 0.444±0.020 0.426±0.018 17.6%±2.7%
GPT-5.4-mini-high-reasoning closed-source−0.042±0.035+0.198±0.012 73.1%±1.6% 0.366±0.020 0.357±0.017 20.0%±2.8%
Table 15.Out-of-distribution on held-out Musical Instruments (5/5/𝑇=12), full results.
H Qualitative Example: Untrained versus Trained Seller on an Identical Instance
This section presents one evaluation instance played end-to-end by two sellers: the untrained base model
(Section H.2) and a trained checkpoint (Section H.3); Figure 2 in the main text excerpts the first two seller turns

42•Liu et al.
Model Params Reward↑
Seller Surplus
Extraction
Ratio
Item
Deal
Rate
Deal on
Top Buyer
Rate
Optimal-Pair
Offer Coverage
Rate
Instruction
Violation
Rate
Qwen3-30B-A3B-Instruct-2507-trained (Ours) 30B +0.559 +0.586 80.6% 0.534 0.727 1.7%
Qwen3-30B-A3B-Instruct-2507-untrained 30B −0.065 +0.313 89.5% 0.318 0.450 28.7%
Kimi-K2.6-thinking 1T+0.443 +0.449 90.7% 0.403 0.508 0.4%
GPT-5.4-high-reasoning closed-source+0.400+0.40095.0% 0.412 0.553 0.0%
DeepSeek-V4-Pro-thinking 1.6T+0.367+0.505 93.3% 0.420 0.534 9.2%
DeepSeek-V4-Pro-nothink 1.6T+0.337+0.414 94.6% 0.394 0.504 5.4%
Kimi-K2.6-nothink 1T+0.322+0.42995.0% 0.422 0.517 7.5%
DeepSeek-V4-Flash-thinking 284B+0.298+0.435 92.8% 0.397 0.465 9.6%
DeepSeek-V4-Flash-nothink 284B+0.287+0.373 93.9% 0.383 0.479 6.2%
GPT-5.4-mini-high-reasoning closed-source+0.193+0.284 92.5% 0.365 0.447 7.1%
Table 16.Out-of-distribution Env. 3, Buyer Heavy (5buyers,3items, 𝑇= 12), uniform valuation. Baselines sorted by
Reward(descending); best per column in bold, second-best underlined (Instruction Violation Rateis lower-is-better). Metric
definitions in Section 6. Standard errors in Table 17.
Model Params Reward↑
Seller Surplus
Extraction
Ratio
Item
Deal
Rate
Deal on
Top Buyer
Rate
Optimal-Pair
Offer Coverage
Rate
Instruction
Violation
Rate
Qwen3-30B-A3B-Instruct-2507-trained (Ours) 30B +0.559±0.022 +0.586±0.018 80.6%±1.5% 0.534±0.021 0.727±0.017 1.7%±0.8%
Qwen3-30B-A3B-Instruct-2507-untrained 30B −0.065±0.040 +0.313±0.015 89.5%±1.6% 0.318±0.022 0.450±0.022 28.7%±2.9%
Kimi-K2.6-thinking 1T+0.443±0.015 +0.449±0.014 90.7%±1.3% 0.403±0.019 0.508±0.019 0.4%±0.4%
GPT-5.4-high-reasoning closed-source+0.400±0.014+0.400±0.01495.0%±0.9% 0.412±0.019 0.553±0.019 0.0%±0.0%
DeepSeek-V4-Pro-thinking 1.6T+0.367±0.031+0.505±0.014 93.3%±1.0% 0.420±0.020 0.534±0.020 9.2%±1.9%
DeepSeek-V4-Pro-nothink 1.6T+0.337±0.025+0.414±0.015 94.6%±1.0% 0.394±0.019 0.504±0.019 5.4%±1.5%
Kimi-K2.6-nothink 1T+0.322±0.027+0.429±0.01495.0%±0.9% 0.422±0.020 0.517±0.019 7.5%±1.7%
DeepSeek-V4-Flash-thinking 284B+0.298±0.031+0.435±0.015 92.8%±1.1% 0.397±0.020 0.465±0.020 9.6%±1.9%
DeepSeek-V4-Flash-nothink 284B+0.287±0.025+0.373±0.014 93.9%±1.0% 0.383±0.019 0.479±0.019 6.2%±1.6%
GPT-5.4-mini-high-reasoning closed-source+0.193±0.025+0.284±0.014 92.5%±1.2% 0.365±0.019 0.447±0.019 7.1%±1.7%
Table 17.Out-of-distribution (5buyers,3items,𝑇=12), full results.
of the trained episode. The two episodes share the instance exactly—the same three-item catalog, the same seller
costs, and the same hidden valuation matrixB—while the buyer turns are independently sampled rollouts, so
the buyers’ messages differ across the two transcripts. In this episode no buyer’s opening offers were resampled
by the first-offer noise. Transcript conventions:TalkandActionlines are quoted verbatim from the episode
records; the seller’sThoughtis quoted verbatim here (the main-text figure shows an abridged version); buyer
Thoughtfields are omitted; in the valuation tables, bold marks each item’s highest valuation. The seller’sThought
is private—each buyer sees only theTalkandActionof the messages targeted at it.
H.1 Episode Information
The seller-side episode constants and item catalog, as the seller prompt presents them (the full dataset records of
this catalog appear in Section E.3):
Per-episode constants and item catalog (verbatim seller-prompt content)
m = 3 buyers n = 3 items
K = 3 per-buyer message cap T = 7 total seller-message budget (T < m*K)

Learning to Sell•43
Model Params Reward↑
Seller Surplus
Extraction
Ratio
Item
Deal
Rate
Deal on
Top Buyer
Rate
Optimal-Pair
Offer Coverage
Rate
Instruction
Violation
Rate
Qwen3-30B-A3B-Instruct-2507-trained (Ours) 30B +0.326 +0.343 46.4% 0.728 0.817 1.3%
Qwen3-30B-A3B-Instruct-2507-untrained 30B −0.089 +0.189 46.8% 0.568 0.377 23.3%
Kimi-K2.6-thinking 1T+0.238 +0.248 49.6% 0.573 0.465 0.8%
DeepSeek-V4-Pro-nothink 1.6T+0.213+0.23951.7% 0.580 0.520 2.1%
Kimi-K2.6-nothink 1T+0.211+0.253 51.4% 0.596 0.527 3.3%
GPT-5.4-high-reasoning closed-source+0.195+0.195 50.4% 0.513 0.5030.0%
DeepSeek-V4-Flash-nothink 284B+0.182+0.234 49.6% 0.546 0.476 4.2%
DeepSeek-V4-Flash-thinking 284B+0.097+0.248 47.6% 0.536 0.472 12.1%
GPT-5.4-mini-high-reasoning closed-source+0.049+0.144 48.7% 0.478 0.416 8.3%
DeepSeek-V4-Pro-thinking 1.6T−0.183+0.289 50.3% 0.610 0.571 36.7%
Table 18.Out-of-distribution Env. 4, Item Heavy (3buyers,5items, 𝑇= 7), uniform valuation. Baselines sorted by
Reward(descending); best per column in bold, second-best underlined (Instruction Violation Rateis lower-is-better). Metric
definitions in Section 6. Standard errors in Table 19.
Model Params Reward↑
Seller Surplus
Extraction
Ratio
Item
Deal
Rate
Deal on
Top Buyer
Rate
Optimal-Pair
Offer Coverage
Rate
Instruction
Violation
Rate
Qwen3-30B-A3B-Instruct-2507-trained (Ours) 30B +0.326±0.015 +0.343±0.012 46.4%±1.0% 0.728±0.019 0.817±0.015 1.3%±0.7%
Qwen3-30B-A3B-Instruct-2507-untrained 30B −0.089±0.034 +0.189±0.011 46.8%±1.2% 0.568±0.024 0.377±0.021 23.3%±2.7%
Kimi-K2.6-thinking 1T+0.238±0.012 +0.248±0.009 49.6%±0.9% 0.573±0.020 0.465±0.019 0.8%±0.6%
DeepSeek-V4-Pro-nothink 1.6T+0.213±0.015+0.239±0.01051.7%±0.8% 0.580±0.020 0.520±0.019 2.1%±0.9%
Kimi-K2.6-nothink 1T+0.211±0.017+0.253±0.009 51.4%±0.9% 0.596±0.020 0.527±0.019 3.3%±1.2%
GPT-5.4-high-reasoning closed-source+0.195±0.009+0.195±0.009 50.4%±0.9% 0.513±0.020 0.503±0.0190.0%±0.0%
DeepSeek-V4-Flash-nothink 284B+0.182±0.019+0.234±0.010 49.6%±0.9% 0.546±0.021 0.476±0.019 4.2%±1.3%
DeepSeek-V4-Flash-thinking 284B+0.097±0.028+0.248±0.011 47.6%±1.1% 0.536±0.022 0.472±0.020 12.1%±2.1%
GPT-5.4-mini-high-reasoning closed-source+0.049±0.022+0.144±0.009 48.7%±1.0% 0.478±0.022 0.416±0.019 8.3%±1.8%
DeepSeek-V4-Pro-thinking 1.6T−0.183±0.041+0.289±0.013 50.3%±1.1% 0.610±0.025 0.571±0.023 36.7%±3.1%
Table 19.Out-of-distribution (3buyers,5items,𝑇=7), full results.
# Item catalog (private — buyers see only list prices, never your cost)
- video_recorders_1: ANNKE 3K Lite 8 Channel Hybrid 5-in-1 Security Digital Video Recorder, H.265+... — list $169.99, your
cost $55.99
- video_recorders_2: Lorex 4K Ultra HD 8-Channel Fusion Series PoE Network Video Recorder with 2TB... — list $249.99, your
cost $100.00
- video_recorders_3: ZOSI H.265+ 8 Channel 5MP Lite 1080p CCTV DVR Recorder Without HDD, Hybrid Ca... — list $55.99, your cost
$42.07
The catalog economics of the instance and the realized allocations of the two episodes:
H.2 Untrained Baseline
Hidden buyer valuationsB 𝑖,𝑗
Item 1 Item 2 Item 3
Buyer 1 $147.60 $193.57$45.66
Buyer 2$193.18 $252.12$22.60
Buyer 3 $122.97 $149.76 $43.99
Turn 1 — all three buyers open on the cheapest item.

44•Liu et al.
Model Params Reward↑
Seller Surplus
Extraction
Ratio
Item
Deal
Rate
Deal on
Top Buyer
Rate
Optimal-Pair
Offer Coverage
Rate
Instruction
Violation
Rate
Qwen3-30B-A3B-Instruct-2507-trained (Ours) 30B +0.452 +0.497 69.9% 0.366 0.737 3.0%
Qwen3-30B-A3B-Instruct-2507-untrained 30B −0.215 +0.260 74.4% 0.276 0.446 37.7%
Kimi-K2.6-thinking 1T+0.317 +0.334 73.6% 0.289 0.481 1.3%
DeepSeek-V4-Pro-nothink 1.6T+0.293+0.337 77.8% 0.313 0.515 3.3%
GPT-5.4-high-reasoning closed-source+0.272+0.27879.8% 0.311 0.547 0.4%
DeepSeek-V4-Pro-thinking 1.6T+0.251+0.405 75.9% 0.288 0.519 10.9%
DeepSeek-V4-Flash-nothink 284B+0.187+0.319 78.3% 0.280 0.490 10.0%
Kimi-K2.6-nothink 1T+0.176+0.338 79.0% 0.289 0.493 12.1%
DeepSeek-V4-Flash-thinking 284B+0.088+0.339 75.0% 0.285 0.498 18.8%
GPT-5.4-mini-high-reasoning closed-source+0.053+0.215 75.6% 0.276 0.479 13.3%
Table 20.Out-of-distribution Env. 5, Item Correlation: per-item valuation multiplier 𝜇𝑗∼U[ 0.5, 2] (5buyers,5items,
𝑇= 12). Baselines sorted byReward(descending); best per column in bold, second-best underlined (Instruction Violation Rate
is lower-is-better). Metric definitions in Section 6. Standard errors in Table 21.
Model Params Reward↑
Seller Surplus
Extraction
Ratio
Item
Deal
Rate
Deal on
Top Buyer
Rate
Optimal-Pair
Offer Coverage
Rate
Instruction
Violation
Rate
Qwen3-30B-A3B-Instruct-2507-trained (Ours) 30B +0.452±0.022 +0.497±0.015 69.9%±1.3% 0.366±0.017 0.737±0.014 3.0%±1.1%
Qwen3-30B-A3B-Instruct-2507-untrained 30B −0.215±0.040 +0.260±0.014 74.4%±1.8% 0.276±0.019 0.446±0.019 37.7%±3.1%
Kimi-K2.6-thinking 1T+0.317±0.015 +0.334±0.011 73.6%±1.5% 0.289±0.016 0.481±0.015 1.3%±0.7%
DeepSeek-V4-Pro-nothink 1.6T+0.293±0.019+0.337±0.011 77.8%±1.2% 0.313±0.015 0.515±0.015 3.3%±1.2%
GPT-5.4-high-reasoning closed-source+0.272±0.012+0.278±0.01179.8%±1.3% 0.311±0.015 0.547±0.016 0.4%±0.4%
DeepSeek-V4-Pro-thinking 1.6T+0.251±0.030+0.405±0.012 75.9%±1.3% 0.288±0.016 0.519±0.016 10.9%±2.0%
DeepSeek-V4-Flash-nothink 284B+0.187±0.028+0.319±0.012 78.3%±1.3% 0.280±0.015 0.490±0.016 10.0%±1.9%
Kimi-K2.6-nothink 1T+0.176±0.030+0.338±0.012 79.0%±1.2% 0.289±0.016 0.493±0.016 12.1%±2.1%
DeepSeek-V4-Flash-thinking 284B+0.088±0.035+0.339±0.013 75.0%±1.4% 0.285±0.017 0.498±0.017 18.8%±2.5%
GPT-5.4-mini-high-reasoning closed-source+0.053±0.028+0.215±0.010 75.6%±1.4% 0.276±0.016 0.479±0.016 13.3%±2.2%
Table 21.Out-of-distribution with per-item valuation multiplier𝜇 𝑗∼U[0.5,2], full results.
Buyer 1
Talk:Let me propose $45.66 for video_recorders_3.
Action:[BUY]video_recorders_3 $45.66
Buyer 2
Talk:I propose $10.00 for video_recorders_3.
Action:[BUY]video_recorders_3 $10.00
Buyer 3
Talk:Let’s start with a proposal for the third item. How about $35 for video_recorders_3?
Action:[BUY]video_recorders_3 $35.00

Learning to Sell•45
Model Params Reward↑
Seller Surplus
Extraction
Ratio
Item
Deal
Rate
Deal on
Top Buyer
Rate
Optimal-Pair
Offer Coverage
Rate
Instruction
Violation
Rate
Qwen3-30B-A3B-Instruct-2507-trained (Ours) 30B +0.449 +0.499 70.7% 0.372 0.739 3.3%
Qwen3-30B-A3B-Instruct-2507-untrained 30B −0.150 +0.299 74.1% 0.289 0.409 34.6%
Kimi-K2.6-thinking 1T+0.349 +0.372 74.5% 0.292 0.500 1.7%
DeepSeek-V4-Pro-nothink 1.6T+0.304+0.361 80.0% 0.263 0.482 4.2%
GPT-5.4-high-reasoning closed-source+0.297+0.297 79.5% 0.283 0.536 0.0%
DeepSeek-V4-Pro-thinking 1.6T+0.293+0.444 79.8% 0.274 0.512 10.5%
DeepSeek-V4-Flash-nothink 284B+0.271+0.344 79.1% 0.274 0.485 5.4%
DeepSeek-V4-Flash-thinking 284B+0.266+0.394 78.0% 0.258 0.489 9.2%
Kimi-K2.6-nothink 1T+0.184+0.35981.8% 0.253 0.505 12.9%
GPT-5.4-mini-high-reasoning closed-source+0.066+0.224 75.9% 0.260 0.467 12.9%
Table 22.Out-of-distribution Env. 6, Buyer Correlation: per-buyer generosity multiplier 𝛾𝑖∼U[ 0.5, 2] (5buyers,
5items, 𝑇= 12). Baselines sorted byReward(descending); best per column in bold, second-best underlined (Instruction
Violation Rateis lower-is-better). Metric definitions in Section 6. Standard errors in Table 23.
Model Params Reward↑
Seller Surplus
Extraction
Ratio
Item
Deal
Rate
Deal on
Top Buyer
Rate
Optimal-Pair
Offer Coverage
Rate
Instruction
Violation
Rate
Qwen3-30B-A3B-Instruct-2507-trained (Ours) 30B +0.449±0.022 +0.499±0.015 70.7%±1.4% 0.372±0.017 0.739±0.014 3.3%±1.2%
Qwen3-30B-A3B-Instruct-2507-untrained 30B −0.150±0.041 +0.299±0.015 74.1%±1.6% 0.289±0.019 0.409±0.019 34.6%±3.1%
Kimi-K2.6-thinking 1T+0.349±0.017 +0.372±0.012 74.5%±1.4% 0.292±0.015 0.500±0.016 1.7%±0.8%
DeepSeek-V4-Pro-nothink 1.6T+0.304±0.021+0.361±0.011 80.0%±1.2% 0.263±0.015 0.482±0.016 4.2%±1.3%
GPT-5.4-high-reasoning closed-source+0.297±0.012+0.297±0.012 79.5%±1.2% 0.283±0.015 0.536±0.016 0.0%±0.0%
DeepSeek-V4-Pro-thinking 1.6T+0.293±0.031+0.444±0.013 79.8%±1.2% 0.274±0.015 0.512±0.016 10.5%±2.0%
DeepSeek-V4-Flash-nothink 284B+0.271±0.023+0.344±0.012 79.1%±1.3% 0.274±0.015 0.485±0.016 5.4%±1.5%
DeepSeek-V4-Flash-thinking 284B+0.266±0.028+0.394±0.013 78.0%±1.2% 0.258±0.015 0.489±0.016 9.2%±1.9%
Kimi-K2.6-nothink 1T+0.184±0.031+0.359±0.01281.8%±1.2% 0.253±0.015 0.505±0.016 12.9%±2.2%
GPT-5.4-mini-high-reasoning closed-source+0.066±0.028+0.224±0.011 75.9%±1.4% 0.260±0.016 0.467±0.016 12.9%±2.2%
Table 23.Out-of-distribution with per-buyer generosity multiplier𝛾 𝑖∼U[0.5,2], full results.
Item 1 (ANNKE) Item 2 (Lorex) Item 3 (ZOSI)
List price𝑃 list,𝑗 $169.99 $249.99 $55.99
Seller costC 𝑗 $55.99 $100.00 $42.07
Untrained outcome (Section H.2) Buyer 2 @ $100.00 unsold Buyer 1 @ $45.66
Trained outcome (Section H.3) Buyer 1 @ $140.00 Buyer 2 @ $240.00 Buyer 3 @ $43.99
Table 24. Catalog economics and realized allocations for the appendix instance (the hidden valuation matrix appears with
each transcript, Section H.2 and Section H.3). Buyer 2 holds the top valuation onbothhigh-value items but can close at most
one deal, so the surplus-maximizing assignment routes Item 1 to Buyer 1, Item 2 to Buyer 2, and Item 3 to Buyer 3—exactly
the allocation the trained seller realizes. The untrained seller instead spends Buyer 1 on the cheapest item and Buyer 2 on
the mid item, after which no remaining buyer can afford the highest-margin Lorex.
Seller (untrained) — turn 1
Thought:Buyer 1’s offer of $45.66 for video_recorders_3 is above cost ($42.07) and close to list price ($55.99), making
it the most viable candidate for immediate closure. Buyer 2’s $10 offer is below cost and thus unacceptable. Buyer 3’s

46•Liu et al.
$35 offer is below cost and also unacceptable. Thus, only Buyer 1’s offer can be accepted. Since all three buyers are
active and have bid on the same item, I must act carefully to avoid violating rules. I will close the deal with Buyer 1 on
video_recorders_3 at $45.66 and then redirect the others to the remaining items.
Target:Buyer 1
Talk:Thank you for your offer. I accept your proposal of $45.66 for video_recorders_3. The deal is closed.
Action:[DEAL]video_recorders_3 $45.66
Seller (untrained) — turn 1
Thought:Buyer 1 is satisfied. Buyer 2 and Buyer 3 both offered below cost for video_recorders_3, which is unprocessable.
I must now pitch the remaining items to them. Buyer 2’s low offer suggests they may be budget-conscious; Buyer 3’s
offer was more reasonable but still below cost. Since Buyer 2 has a weak position and no successful bid yet, I should
target them first to maximize the chance of a sale. I will pitch video_recorders_1, which has a healthy margin (list $169.99,
cost $55.99), at $100 — well below list but above cost and a reasonable midpoint. This may hook Buyer 2, who seems
eager. Buyer 3 can be approached later if needed.
Target:Buyer 2
Talk:I can offer video_recorders_1 at $100. Would you be interested?
Action:[SELL]video_recorders_1 $100.00
Turn 2.
Buyer 2
Talk:Yes, I accept your offer of $100 for video_recorders_1.
Action:[DEAL]video_recorders_1 $100.00
Seller (untrained) — turn 2
Thought:Buyer 1 and Buyer 2 are satisfied. Only Buyer 3 remains active and has not closed any item. They offered
$35 for video_recorders_3, which is below cost ($42.07), so no deal was possible. However, they are still interested and
may be open to other items. I should now pitch video_recorders_2 — the remaining item — which has a high list price
($249.99) and a solid margin (cost $100.00). I’ll propose $150, a moderate price that’s well above cost and below list, to
test willingness. Since Buyer 3 is the only remaining buyer and has a history of making low bids, this could signal value.
If accepted, I maximize revenue; if not, I may need to drop it further, but I must avoid below-cost offers. Proceed with
one final pitch.
Target:Buyer 3
Talk:I can offer video_recorders_2 at $150. Would you like to close this deal?
Action:[SELL]video_recorders_2 $150.00
Turn 3 — the last buyer exits; the Lorex goes unsold.
Buyer 3
Talk:I can’t accept $150 — it exceeds my budget. I’ll pass.
Action:[QUIT]
Outcome.The untrained seller accepts Buyer 1’s opening bid on the cheapest item immediately ($45.66, a
$3.59 margin), then sells Item 1 to Buyer 2 at a self-proposed $100—although Buyer 2’s hidden valuation for
the Lorex (Item 2) was $252.12. With both buyerssatisfied, the only remaining buyer, Buyer 3, cannot afford

Learning to Sell•47
the Lorex (a $149.76 valuation against the $150 quote) and quits: the highest-margin item goes unsold. By (1),
R= (100−55.99)+(45.66−42.07) (169.99−55.99)+(249.99−100)+(55.99−42.07) = 47.60 277.91 =0.171.
H.3 Trained Seller
Hidden buyer valuationsB 𝑖,𝑗
Item 1 Item 2 Item 3
Buyer 1 $147.60 $193.57$45.66
Buyer 2$193.18 $252.12$22.60
Buyer 3 $122.97 $149.76 $43.99
Turn 1 — all three buyers open on the cheapest item.
Buyer 1
Talk:How about $40 for video_recorders_3?
Action:[BUY]video_recorders_3 $40.00
Buyer 2
Talk:I’d like to propose $15 for video_recorders_3 — is that acceptable?
Action:[BUY]video_recorders_3 $15.00
Buyer 3
Talk:Let’s start with video_recorders_3. I propose $35. Is that acceptable?
Action:[BUY]video_recorders_3 $35.00
Seller (trained) — turn 1
Thought:Buyer 1’s offer of $40 for item 3 is below my cost ($42.07) — violation if accepted. Buyer 2’s $15 is also below
cost — invalid. Buyer 3’s $35 is still below cost. None of the opening [BUY] offers for video_recorders_3 are acceptable. I
must reject all three for item 3. However, I can pitch the other two items (1 and 2) to any buyer. Since all buyers are
active and none have closed an item yet, I should initiate negotiations on items 1 and 2. Buyer 1 offered the lowest
for item 3 but may be willing to pay more for item 1 or 2. Buyer 2 is very aggressive on item 3 but may have budget
elsewhere. Buyer 3’s offer is closest to cost but still insufficient. I should target Buyer 1 first — they were first to act and
may be serious. I’ll pitch video_recorders_1 at $160 (close to list) and video_recorders_2 at $230 (also near list), to test
their willingness. If they reject, I can adjust. I must avoid selling item 3 below cost, so I won’t accept any offer for it
unless it’s≥$42.07. For now, I’ll focus on the two higher-value items. I’ll start with Buyer 1 to maximize early leverage.
Target:Buyer 1
Talk:Thank you for your opening. I cannot accept your $40 offer for video_recorders_3 as it is below my cost. However,
I am willing to negotiate on video_recorders_1 and video_recorders_2. I propose $160 for video_recorders_1 and $230
for video_recorders_2. Please let me know if you can meet either price.
Action:[SELL]video_recorders_1 $160.00, video_recorders_2 $230.00
Turn 2 — first close.

48•Liu et al.
Buyer 1
Talk:How about $140 for video_recorders_1?
Action:[BUY]video_recorders_1 $140.00
Seller (trained) — turn 2
Thought:Buyer 1 has now submitted a new [BUY] for video_recorders_1 at $140, which is above my cost ($55.99) but
below my proposed $160. Since this is a valid offer (≥ cost and≤ list), I can accept it to close the deal and secure revenue.
Accepting this deal locks in $140 for item 1, which contributes positively to the reward numerator. However, I must
consider opportunity cost: if I reject this and try to push for a higher price, I risk losing the sale entirely, especially since
Buyer 1 may be the only one interested in item 1. Moreover, Buyer 1 has already shown interest in two items (item 3 and
now item 1), suggesting they are active and budgeted. Accepting $140 now gives me certainty and frees up my message
budget for targeting Buyers 2 and 3 on the remaining items. I should accept this [BUY] to close item 1 immediately and
avoid further risk. After this, I’ll shift focus to Buyer 2 and Buyer 3 for items 2 and 3. Item 3 is still available, and though
all three buyers initially bid below cost, I can now propose a fair price (≥$42.07) to Buyer 2 or 3. Buyer 2 offered $15 for
item 3 — clearly low — but may have budget for item 2. Buyer 3 offered $35, still below cost, but closer. I’ll target Buyer 2
next, as they’ve only engaged on item 3 so far and may be open to item 2. I’ll propose video_recorders_2 at $240 (near
list) to Buyer 2. If rejected, I can adjust or pivot to Buyer 3. But first, I must finalize the deal with Buyer 1 on item 1. I’ll
accept their $140 offer immediately to secure the sale and move forward.
Target:Buyer 1
Talk:I accept your offer of $140 for video_recorders_1. The deal is closed. Item 1 has been sold, and I will no longer
pitch it to you or others.
Action:[DEAL]video_recorders_1 $140.00
Seller (trained) — turn 2
Thought:Buyer 1 is now satisfied and no longer active — their turn is complete. I have successfully sold video_recorders_1
for $140, which is above my cost ($55.99) and contributes positively to the reward. Remaining items: video_recorders_2
(list $249.99, cost $100.00) and video_recorders_3 (list $55.99, cost $42.07). Both are still available. Buyer 2 has only
engaged on video_recorders_3 with a $15 offer (below cost — invalid), and has not shown interest in item 2. Buyer 3
similarly only bid on item 3 at $35 (still below cost). Neither buyer has expressed interest in item 2, so I must initiate
negotiations on it. Buyer 2 is my best remaining target — they are active, have not closed an item, and have not yet
been pitched on item 2. I should now pitch video_recorders_2 to Buyer 2 at $240 (very close to list price) to test their
willingness. If they reject, I can adjust downward or pivot to Buyer 3. However, I must be cautious: Buyer 2 previously
offered only $15 for item 3, suggesting they may have a very low budget — but that doesn’t necessarily mean they can’t
afford item 2. It’s possible they are strategic or have budget constraints on low-value items. Since item 2 has a high list
price and high cost, it’s a more valuable target. I should also consider item 3: although all three initial offers were below
cost, I can now propose a fair price (≥$42.07) to either Buyer 2 or Buyer 3. But item 3 is low-value; selling it at $50 would
only yield $8.93 profit, while item 2 at $240 yields $140 profit — a much better return. Therefore, I should prioritize item
2. I’ll target Buyer 2 first with a strong pitch on item 2 at $240. If they reject, I’ll then pitch item 3 to Buyer 3 at $50 (near
list, above cost) as a fallback. But first, I must act on item 2 with Buyer 2 to maximize potential reward. I’ll send a [SELL]
to Buyer 2 with video_recorders_2 at $240, and leave item 3 open for later if needed.
Target:Buyer 2
Talk:I have closed video_recorders_1 with Buyer 1. I now wish to negotiate for video_recorders_2, which is still available.
I propose a price of $240 for this item, near its list price of $249.99. Please let me know if you can accept this or propose
a counter.
Action:[SELL]video_recorders_2 $240.00
Turn 3 — second close.

Learning to Sell•49
Buyer 2
Talk:Yes, I accept your offer of $240 for video_recorders_2.
Action:[DEAL]video_recorders_2 $240.00
Seller (trained) — turn 3
Thought:Both video_recorders_1 and video_recorders_2 have now been sold: the first to Buyer 1 at $140, the second to
Buyer 2 at $240 — both valid deals above cost and within list price. This secures significant profit:
- Item 1: $140 - $55.99 = $84.01 profit
- Item 2: $240 - $100.00 = $140.00 profit
Total profit so far: $224.01
Only video_recorders_3 remains unsold, with list price $55.99 and cost $42.07. The potential profit from selling it is
$13.92. Buyer 3 is the only active buyer left and has previously submitted a [BUY] for item 3 at $35 — which is below
my cost ($42.07), so it was invalid and cannot be accepted. However, since Buyer 3 is still active and has not closed an
item, they remain a viable target for item 3. I can now pitch item 3 directly to them. I must propose a price≥ $42.07 to
avoid violation. The list price is $55.99, so a reasonable pitch would be $50 (close to list, above cost). If Buyer 3 accepts,
I gain an additional $13.92 profit. If they reject, I cannot sell the item to anyone else, and it will remain unsold — but
that’s acceptable as long as I don’t violate rules. Since I have 4 messages remaining and Buyer 3 can receive up to 3
more, I have ample room to negotiate. I should act now to capture the final profit. I’ll send a [SELL] to Buyer 3 offering
video_recorders_3 at $50, which is fair and within the bounds. If they reject, I may attempt a lower price (e.g., $45), but I
must not go below $42.07. However, starting at $50 gives a strong anchor. Buyer 3 has already shown interest in this
item, so they may be willing to pay closer to list. I’ll proceed with the pitch immediately to maximize the chance of
closing the catalog. The reward is maximized when more items are sold at higher prices, so securing this final sale is
critical. I’ll act now.
Target:Buyer 3
Talk:Only video_recorders_3 remains available. I can now offer it to you at $50, which is above my cost of $42.07 and
close to the list price of $55.99. Please confirm if you can accept this price, or propose a counter within the valid range.
Action:[SELL]video_recorders_3 $50.00
Turn 4 — the catalog clears.
Buyer 3
Talk:I can only go up to $43.99. Can you accept $43.99?
Action:[BUY]video_recorders_3 $43.99
Seller (trained) — turn 4
Thought:Buyer 3 has now submitted a valid [BUY] for video_recorders_3 at $43.99, which is above my cost of $42.07
and below the list price of $55.99 — a perfectly acceptable offer. This is the final open item, and accepting it will close
the catalog successfully. The profit from this sale will be $43.99 - $42.07 = $1.92, which, while small, is still positive
and contributes to the reward numerator. Since this is a valid deal and the item has not yet been sold, I must accept it
to maximize the total reward. Delaying or rejecting would result in leaving the item unsold, which would reduce the
numerator without any benefit. Moreover, Buyer 3 is the only remaining active buyer, and they have already made a
binding offer. Accepting this [BUY] completes the transaction and ensures all three items are sold. The overall reward
will be calculated as:
Numerator: (140 - 55.99) + (240 - 100) + (43.99 - 42.07) = 84.01 + 140 + 1.92 = 225.93
Denominator: (169.99 - 55.99) + (249.99 - 100) + (55.99 - 42.07) = 114 + 149.99 + 13.92 = 277.91
Reward R = 225.93 / 277.91≈0.813 — a strong result.

50•Liu et al.
By accepting this final offer, I secure the highest possible reward given the buyers’ constraints. I have used 5 out of 7
seller messages (turns 1–4), with 2 remaining, but no further actions are needed — all items are now sold or closed. I will
conclude with a [DEAL] to finalize the last transaction. No further negotiation is required. I must act promptly to avoid
violating message limits or missing the opportunity.
Target:Buyer 3
Talk:I accept your offer of $43.99 for video_recorders_3. The deal is closed. All three items have now been sold, and the
episode is complete.
Action:[DEAL]video_recorders_3 $43.99
Outcome.All three items close, each with the buyer prescribed by the surplus-maximizing assignment (Table 24):
Item 1 to Buyer 1 at $140, Item 2 to Buyer 2 at $240 (96%of list), and Item 3 to Buyer 3 at $43.99—that buyer’s
exact valuation. By (1),R= (140−55.99)+(240−100)+(43.99−42.07) (169.99−55.99)+(249.99−100)+(55.99−42.07) = 225.93 277.91 =0.813.
