---
title: 'InfoBid: A Simulation Framework for Studying Information Disclosure in Auctions with Large Language
  Model-based Agents'
url: https://arxiv.org/abs/2503.22726
category: consumer-behavior
subcategory: empirical
date: 2025-03
venue: ''
authors:
- Yue Yin
source: arxiv
pdf_url: https://arxiv.org/pdf/2503.22726
pages: 10
chars: 46849
fetched_at: '2026-11-08T13:14:37+00:00'
kb_version: 1
---

# InfoBid: A Simulation Framework for Studying Information Disclosure in Auctions with Large Language Model-based Agents

The AAAI 2025 Workshop on Economics of Modern ML: Markets, Incentives, and Generative AI (MarketsGenAI)
InfoBid: A Simulation Framework for Studying Information Disclosure in
Auctions with Large Language Model-based Agents
Yue Yin
Independent Researcher, San Francisco
yueyin.io@gmail.com
Abstract
In online advertising systems, publishers often face a trade-
off in information disclosure strategies: while disclosing
more information can enhance efficiency by enabling optimal
allocation of ad impressions, it may lose revenue potential by
decreasing uncertainty among competing advertisers. Simi-
lar to other challenges in market design, understanding this
trade-off is constrained by limited access to real-world data,
leading researchers and practitioners to turn to simulation
frameworks. The recent emergence of large language mod-
els (LLMs) offers a novel approach to simulations, providing
human-like reasoning and adaptability without necessarily re-
lying on explicit assumptions about agent behavior modeling.
Despite their potential, existing frameworks have yet to inte-
grate LLM-based agents for studying information asymmetry
and signaling strategies, particularly in the context of auc-
tions. To address this gap, we introduce InfoBid, a flexible
simulation framework that leverages LLM agents to examine
the effects of information disclosure strategies in multi-agent
auction settings. Using GPT-4o, we implemented simulations
of second-price auctions with diverse information schemas.
The results reveal key insights into how signaling influences
strategic behavior and auction outcomes, which align with
both economic and social learning theories. Through Info-
Bid, we hope to foster the use of LLMs as proxies for human
economic and social agents in empirical studies, enhancing
our understanding of their capabilities and limitations. This
work bridges the gap between theoretical market designs and
practical applications, advancing research in market simula-
tions, information design, and agent-based reasoning while
offering a valuable tool for exploring the dynamics of digital
economies.
Introduction
Today, display advertising drives a multi-billion-dollar mar-
ket where publishers like Google and Meta sell user impres-
sions to advertisers such as Coca-Cola, Amazon, and Nike.
These impressions are sold via real-time auctions, where ad-
vertisers (bidders) submit bids, and the publisher (auction-
eer) allocates the impressions and collects payments based
on the auction’s outcome. A defining feature of such markets
is information asymmetry: publishers possess rich informa-
tion about users—such as browsing history, interests, and
Copyright © 2025, Association for the Advancement of Artificial
Intelligence (www.aaai.org). All rights reserved.
demographic information—and also rich information about
advertisers, potentially enabling the publishers to infer ad-
vertisers’ specific targeting goals, budget and requirement
on return. Advertisers, on the other hand, have limited visi-
bility into the auction environment and must rely on signals
provided by the publisher to make their bidding decisions.
With such dynamics, the publisher may reveal partial details
about a user’s characteristics or the level of competition in
the auction. This deliberate disclosure of information, also
known as signaling, shapes advertisers’ expectations and
bidding strategies. For example, advertisers selling luxury
watches may place higher bids on keywords (i.e., signals) as-
sociated with affluent consumers, as these users align more
closely with their target audience, representing higher po-
tential value. By selectively revealing information, auction-
eers can influence bidders’ perceptions and bidding strate-
gies, which in turn impacts auction outcomes. This raises a
central question: What information should be disclosed to
optimize auction outcomes, whether for the auctioneer
revenue, bidder surplus, or overall social welfare?
Theoretical research has provided foundational insights
into market design and strategic behavior in advertising auc-
tions, with contributions from both academic researchers, in-
cluding Nobel laureates (Vickrey 1961; Myerson 1981), and
leading industry practitioners (Liu et al. 2021; Ostrovsky
and Schwarz 2011; He et al. 2021). There is also a signif-
icant area of study focusing on information asymmetry and
signaling strategy, exploring topics such as public vs. private
information, equilibrium behavior under various informa-
tion structures, the design of optimal signaling mechanisms,
and algorithmic methods to derive these signals (Emek et al.
2014; Bergemann et al. 2022; Cheng et al. 2015; Badani-
diyuru, Bhawalkar, and Xu 2018; Milgrom and Weber 1982;
Milgrom 2010; Levin and Milgrom 2010; Feinberg and Ten-
nenholtz 2005) .
Despite these advances, a significant empirical gap re-
mains, particularly in understanding how signaling and in-
formation asymmetry influence bidding behavior in prac-
tical settings. This challenge is not unique to information
disclosure but extends to broader aspects of market design
in online environments, characterized by sequential, inter-
dependent interactions among multiple strategic agents, as
seen in systems like advertising platforms and recommen-
dation engines. Real-world validation is constrained by lim-
1
arXiv:2503.22726v1  [cs.GT]  26 Mar 2025

ited access to proprietary data and the high cost of online ex-
periments, both in terms of operations and user experience
impact. As a result, researchers have turned to simulation
environments to bridge this gap, with notable frameworks
developed by Amazon (Jeunen, Murphy, and Allison 2023),
eBay (Nguyen et al. 2023), Uber (Yue Yin 2023) and Google
(Ie et al. 2019), etc.
However, existing simulation frameworks face notable
limitations. Many of these frameworks focus on bidding
strategies, reserve price optimization, or auction formats,
while lack the exploration of the effect of information dis-
closure strategies. Second, the simulated agents (bidders) are
typically guided by pre-determined assumptions, i.e., their
decision-making processes are parametrized with a limited
set of predefined rules or structures. These assumptions may
be encoded through heuristic models, structured stochastic
processes, or parametrized frameworks such as neural net-
works. While these approaches provide tractable models of
agent behavior, they often lack the richness and adaptability
of human decision-making, as well as the interpretability of
reasoning that characterizes rational human agents.
The emergence of large language models (LLMs), such
as GPT-4, offers a promising solution to the limitations
of traditional agent-based models, particularly in address-
ing the challenges of adaptability and human-like reason-
ing (openai 2024; Feizi et al. 2023; Touvron et al. 2023;
Zeng et al. 2023). Unlike conventional approaches that rely
on parametrized assumptions, LLMs enable the creation of
adaptive agents capable of reasoning with limited input as-
sumptions, making nuanced decisions, and providing inter-
pretable explanations for their actions. Early applications of
LLM-based agents in simulation frameworks have demon-
strated such frameworks’ potential to enhance the realism
and interpretability of competitive environments, including
auctions (Chen et al. 2023; Zhao et al. 2024). However, ex-
isting frameworks have not yet incorporated information dis-
closure strategies into LLM-driven simulations, particularly
in the context of online advertising auctions. This represents
a significant gap, as understanding the interplay between sig-
naling strategies and agent behavior is crucial for advancing
both theoretical insights and practical applications in auction
design.
In this paper, we address the critical gap in understanding
the role of information disclosure in auctions by introducing
InfoBid, a simulation framework that leverages LLM-based
agents (using GPT-4o) to study strategic behavior under in-
formation asymmetry in multi-agent auctions. A critical fo-
cus of this study is to see whether these LLM-based agents
exhibit rational behavior, relying on their inherent reason-
ing capabilities rather than pre-parameterized assumptions
or explicitly encoded decision-making processes. Therefore,
our experiments are designed to provide minimal public in-
formation and avoid imposing explicit assumptions about
agents’ internal models. Instead, agents are tasked with rea-
soning based on disclosed information and their own knowl-
edge. Within this setup, we systematically explore diverse
private signaling strategies, ranging from full disclosure,
which reveals precise valuations of an advertisement, to se-
lective pooling, which aggregates and shares approximate
signals, to randomized pooling, which probabilistically dis-
closes information. These strategies allow us to analyze how
information impacts key auction outcomes—such as rev-
enue, bidder surplus, and social welfare—and to observe the
reasoning and adaptability of LLM-based agents under vary-
ing scenarios.
Findings
Our key findings after running a few simulations under this
framework are the following:
• Rationality Analysis on Agent’s Decision-making: We
find that bidder behavior reflects both alignment with and
deviations from truthful bidding under various signaling
strategies. Specifically, revealing relative positions dis-
rupts truthful bidding, as bidders adjust their bids based
on perceived advantage in the competition. However, our
results suggest that adding richer information, such as the
average true valuation within tiers, mitigates these devi-
ations and stabilizes bidding. These findings echo social
learning theories, such as social comparison and anchor-
ing effects.
• Agents’ Reasoning : Our analysis of bidders’ expla-
nations reveals that LLM-based agents do not explic-
itly consider competitors’ values or strategies in their
decision-making. While this behavior aligns with the
theoretical expectation in second-price auctions, where
truthful bidding is the dominant strategy, we don’t know
whether these outcomes stem from the agents’ trained ra-
tionality or limitations in perceiving competitive dynam-
ics. Exploring these aspects in alternative auction for-
mats, such as first-price auctions, could provide valuable
insights into their reasoning capabilities and adaptability.
• Revenue and Social Welfare Analysis: Our results indi-
cate that Pool-High strategies targeting high percentiles
and incorporating average true values in pooled infor-
mation yield the highest auctioneer revenue. This aligns
with theoretical insights from economic literature, as the
strategy intensifies competition among top-tier bidders
and extract high information rents, driving revenue gains.
Additionally, we find that social welfare improves with
increased information disclosure to high-value bidders,
underscoring the importance of transparency in achiev-
ing efficient resource allocation. Together, these findings
suggest that carefully designed signaling strategies can
simultaneously enhance auctioneer revenue and social
welfare outcomes.
Contributions
The contributions of this paper are three-fold:
1. Framework for LLM-Based Information Strategies: We
pioneer a simulation framework that integrates informa-
tion disclosure strategies into LLM-based agents, offer-
ing a novel testbed for studying auction mechanism in
online advertising markets.
2. Development of a Simulated Environment: The frame-
work provides a flexible and scalable environment to ex-
plore various auction setups, information structures, and
2

Auctioneer
Agent
Bidding
Agents
"Your
value
is
0.7"
"Your
value
is
unknown"
Disclose
information
Submit
bid
I
bid
0.7
I
bid
0.8
"Bidder
2
win
and
pay
0.7"
"Bidder
2
win
and
pay
0.7"
Information
Example
of
an
information
disclosure
strategy:
1.
Fully
disclose
each
bidder's
true
value
if
it
is
?
0.7
,
while
withholding
information
for
values
>
0.7;
2.
Hide
the
total
number
of
bidders
participating
in
the
auction.
Figure 1: Information flow between auctioneer and bid-
ders in an example auction. Gray-colored messages repre-
sent private information, such as Your value is 0.7 provided
individually to bidders by the auctioneer. Green-colored text
represents sealed bids submitted privately by bidders to the
auctioneer, such as I bid 0.7 or I bid 0.8. Blue-colored mes-
sages signify public information, such as the auctioneer an-
nouncing, Bidder 2 wins and pays 0.7, visible to all partici-
pants. This example showcases a specific disclosure strategy,
including conditions for revealing true values and withhold-
ing total bidder count.
agent behaviors, bridging the gap between theoretical in-
sights and empirical validation.
3. Novel Insights into Agent Behavior and Economic The-
ory: Our study reveals how LLM agents reason and
adapt to information asymmetry, producing behaviors
that align with auction theory. These findings not only
validate the utility of LLM-based simulations but also
guide future research on agent behavior, mechanism de-
sign, and market efficiency.
Methodology
The InfoBid framework is an extensible simulation envi-
ronment designed to study the impact of information dis-
closure strategies on agents’ strategic behavior and auction
outcomes. The framework comprises several key compo-
nents: Agents, which include the auctioneer and multiple
bidders, each with distinct roles and decision-making capa-
bilities; Information Structure, which specifies the infor-
mation to be disclosed, pooled, or hidden, shaping the strate-
gic dynamics of the auction; and theAuction and Signaling
Process, which manages the flow of information and bids
between agents, simulating real-world auction interactions.
These components, together with configurable simulation
parameters, make InfoBid a versatile testbed for exploring
the relationships between auction design, information asym-
metry, and strategic decision-making. Additionally, InfoBid
supports the creation and evaluation of diverse information
disclosure policies, providing a scalable and flexible plat-
form for advancing research in market simulations and auc-
tion outcome.
Agent Design
Auctioneer The auctioneer serves as the central entity re-
sponsible for managing the auction process and typically
holds more information than the bidders. Two settings are
widely studied in the literature (Emek et al. 2014):
• Known-Valuations: In this setting, the auctioneer pos-
sesses complete knowledge of all bidders’ true valuations
for the auctioned item. These valuations are often de-
rived from detailed item characteristics or bidder profiles
that the auctioneer has exclusive access to. For example,
in online advertising, the auctioneer (e.g., the publisher)
might have accurate predictions of how much each adver-
tiser values an impression based on user demographics,
historical click-through rates, or conversion likelihoods.
With full knowledge of bidder valuations, the auction-
eer can precisely tailor disclosure strategies—such as re-
vealing exact values, pooling certain groups, or selec-
tively sharing information—to maximize specific objec-
tives, such as auctioneer revenue or social welfare.
• Bayesian Setting: The auctioneer does not know the ex-
act valuations of the bidders but operates with a prior
belief about these valuations. For instance, the auction-
eer might know general characteristics of the item being
auctioned but be uncertain about how different types of
bidders—such as cost-sensitive or quality-focused par-
ticipants—value the item. These bidder types are not di-
rectly observable to the auctioneer, introducing an addi-
tional layer of complexity.
Bidder Bidder agents represent the participants in the auc-
tion and are tasked with formulating strategic bids based
on the signals received from the auctioneer and their own
knowledge. Unlike the auctioneer, bidders lack information
about the auctioned item and are unaware of their true val-
uations. In this study, we employ GPT-4o as the reasoning
engine for bidders, with the temperature set to 0 to ensure
reproducibility. Bidders generate their bids in two steps: (1)
estimate their true valuations based on the provided signals
and their own knowledge. For instance, a signal such as”You
are among the high value bidders”may lead a bidder to infer
a relatively high valuation while remaining uncertain about
its precise value; (2) formulate their bids based on these es-
timated values. For example, a bidder estimating their valu-
ation at 0.75 might bid slightly below this value to account
for uncertainty while remaining competitive. Additionally,
bidders are required to explain their bidding decisions.
Information Structure
The information structure in our framework is designed to
capture the strategic flow of data between the auctioneer and
bidders, highlighting the interplay between shared and indi-
vidualized information. It is categorized as follows:
• Public Information: Public information is shared among
all agents (including the auctioneer and all bidders) and
serves as a common reference point for their decision-
making. In this study, public information may include:
– Auction Rules: The mechanism governing the auction,
such as whether it is a first-price or second-price auc-
3

tion, the number of bidders, and whether ties are bro-
ken randomly or systematically;
– Common Prior on Bidders’ Distribution: For example,
bidders and the auctioneer may agree that valuations
are uniformly distributed over [0, 1]. Also, if the en-
vironment assumes bidders have different types (e.g.,
”high-budget” vs. ”low-budget” bidders), the prior dis-
tribution of these types may also be common knowl-
edge;
– Public Knowledge of the Signaling Map: The sig-
naling map describes how realized random states
(e.g., bidders’ valuations) are transformed into sig-
nals disclosed to bidders. For example, the signal-
ing map might specify that high-value bidders (e.g.,
those above the 80th percentile) will have their infor-
mation pooled, while low-value bidders (e.g., those
below the 80th percentile) will have their valuations
fully disclosed. This map may be publicly known and
shapes the bidders’ expectations of the auction’s infor-
mational context.
– Auction outcome: After each round, the auctioneer re-
veals the auction results, which are accessible to all
bidders. This includes the name or identifier of the bid-
der who won the item and The final price paid for the
item, typically determined by the second-highest bid
in a second-price auction.
• Private Information: Private information is exclusive to
each individual bidder and remains hidden from others,
allowing the auctioneer to strategically influence person-
alized bidding behavior through tailored signals. In our
framework, private information pertains primarily to a
bidder’s valuation of the auctioned item. The auction-
eer may disclose this information using various signaling
strategies, including:
– Full Disclosure: The auctioneer reveals the exact value
of a bidder’s true valuation. For example, a bidder
might be informed, ”Your valuation for this item is
0.7. ”This approach eliminates uncertainty for the bid-
der, encouraging truthful bidding behavior.
– Selective pooling involves aggregating information
and sharing approximate signals with specific groups
of bidders, allowing the auctioneer to influence their
bidding strategies indirectly. For instance, tiered pool-
ing might provide relative placement information,
such as stating, “You are among the top value bidders”
or “Your value falls into the low tier,” rather than re-
vealing precise valuations. Alternatively, randomized
pooling introduces an additional layer of uncertainty
by selectively disclosing pooled information to certain
bidders without a deterministic pattern.
Auction and Signaling Process
InfoBid employs a structured six-phase pipeline, from ini-
tializing the auction context to announce the auction out-
come, to simulate the auction and signaling process, pro-
viding a comprehensive approach to analyzing the effects of
information disclosure strategies on auction outcomes and
bidder behavior. Detailed introduction of the phases is in
Appendix.
Experiments
Simulation Design
In this study, we focus on the Known-Valuation setting,
where the auctioneer has complete knowledge of each bid-
der’s true valuation for the auctioned item. For simplicity,
the experiments include 10 bidders, with each bidder’s val-
uation for a given item independently drawn from a uniform
distribution over [0, 1].
We adopt a sealed-bid second-price auction without a re-
serve price—a widely recognized auction format used in
both theoretical and applied contexts (Vickrey 1961). In this
mechanism, bidders submit private bids without knowledge
of others’ bids. The bidder with the highest bid wins the
item but pays the second-highest bid. This format incen-
tivizes bidders to bid truthfully according to their perceived
valuations, providing a robust framework to analyze how
various information disclosure strategies influence strategic
decision-making.
By default, the auctioneer publicly shares the following
information to establish a common context for all partici-
pants:
1. The auction type (sealed-bid second-price) and the num-
ber of bidders.
2. The common prior that all bidders’ valuations for each
item are independently drawn from a uniform distribu-
tion over [0, 1].
The experiments systematically vary the private signaling
strategies used to communicate information about bidders’
valuations. Importantly, these signaling strategies are not
shared as public knowledge, meaning bidders must rely
solely on the default public information, the private signals
they receive, and any implicit reasoning capabilities derived
from their pretrained knowledge. They do not have explicit
knowledge of the information other bidders receive. The ex-
perimented private signaling strategies include the following
(For further details on the prompts used in each scenario, re-
fer to the Appendix)
• Full disclosure: bidders receive their exact valuation;
• Tiered pooling (”Pool-High” and ”Pool-Low”): bidders
are grouped into quantile-based tiers. For instance, the
”Pool-High” strategy provides pooled information to bid-
ders whose true valuations fall within the higher per-
centiles while fully disclosing valuations to the remain-
ing bidders. The mathematical formulation of ”Pool-
High” is shown in Eq. 1, where F (vi) is the cumulative
distribution function (CDF) ofvi, q is the quantile thresh-
old, and p(vi) represents the pooled information. Sim-
ilarly, the Pool-Low strategy applies pooling to lower-
valued bidders, selectively revealing their positional con-
text. Tiered pooling includes two variants of pooled in-
formation: 1) Tier-only information, where bidders are
informed solely of their relative position within a tier,
e.g., “You are among the high tier of bidders.”; 2) Tier
and average value information, where bidders receive
4

their relative position along with the average true valu-
ation within their tier, e.g., “You are among the high tier
of bidders, and the average valuation in your tier is 0.8.”
s(i)
vi F (vi) < q,
p(vi) F (vi) ≥ q (1)
• Randomized pooling: randomly pooling bidder informa-
tion and selectively disclosing it based on predefined
probabilities (Eq. 2)
s(i) =
vi with probability q,
p(vi) with probability 1 − q, (2)
Both tiered pooling and randomized pooling are param-
eterized using a set of probalistic threshold ( q in the equa-
tion). These thresholds control either the quantile boundaries
for tiered pooling or the probability of information disclo-
sure in randomized pooling, enabling direct comparisons be-
tween the two approaches.
To ensure robust findings, each simulation configuration
is executed over 100 independent rounds. In each round, a
new item is introduced, and bidders are assigned fresh val-
uations drawn from the uniform distribution, ensuring inde-
pendent and identically distributed (i.i.d.) conditions across
rounds. For simplicity, the framework does not incorporate
iterative learning across rounds, treating each round as an
isolated snapshot of decision-making process. See Appendix
for a list of simulation variants configurations in our study.
Evaluation Metrics
To analyze the effectiveness of information disclosure strate-
gies and bidding behaviors, we evaluate the following met-
rics for each configuration:
• Bid Deviation from Rational Behavior: In a second-
price sealed-bid auction, rational behavior is defined as
bidding truthfully, i.e., submitting a bid equal to the bid-
der’s estimated true value. This metric evaluates the ex-
tent to which submitted bids align with the bidder’s es-
timated valuation. Bid deviation is quantified as the per-
centage of cases where a bidder’s submitted bid is greater
than, equal to, or less than their estimated value, pro-
viding insights into deviations from theoretically optimal
bidding behavior.
• Revenue: Revenue is calculated as the price paid by the
winning bidder in each round, summed over all rounds in
the simulation. This metric provides insight into the auc-
tioneer’s performance under different disclosure strate-
gies.
• Social Welfare: Social welfare is defined as the sum
of the true valuations of the winning bidders across all
rounds. Mathematically, it can be expressed as:
SocialW elf are=
RX
r=1
vr
where R is the total number of auction rounds, and vr
represents the true valuation of the winning bidder in
round r. This metric evaluates the overall efficiency of
the auction in allocating items to bidders with the high-
est valuations.
Figure 2: Impact of Signaling Strategies on Bid Devia-
tion Behavior The chart illustrates the percentage of devi-
ated bidding behavior across various signaling strategies, as
represented on the x-axis. The y-axis denotes the propor-
tion of bids categorized into three groups: truthful bidding
(where the bid value equals the estimated value), overbid-
ding (where the bid value exceeds the estimated value), and
underbidding (where the bid value is lower than the esti-
mated value). Each bar is derived from 4000 bid records.
Results
Bidder’s Rationality Analysis The analysis of rationality
in this study can be divided into two aspects: (1) the rational
inference of valuations, where bidders estimate their value
based on disclosed information, and (2) the rational bidding
behavior, defined as submitting bids that align with the in-
ferred valuations. While theoretical equilibrium prescribes
truthful bidding—submitting bids equal to the estimated val-
uation—agents may deviate depending on the disclosed in-
formation and their interpretation of it.
First, we quantitatively analyze the extent to which bid-
ders’ submitted bids align with their inferred valuations as
illustrated by figure 2. Under full information, bidders con-
sistently engage in truthful bidding, submitting bids pre-
cisely equal to their estimated valuations. This outcome val-
idates the rational behavior of LLM agents’ ability to rea-
son logically and bid optimally when provided with unam-
biguous and complete information. Similarly, in random-
ized pooling—where signals lack relative standing or po-
sitional details but indicate whether a value is pooled or
disclosed—truthful bidding also achieves 100% consistency.
The absence of comparative information simplifies decision-
making, as agents cannot infer additional competitive nu-
ances, leading them to align their bids with their estimated
values.
In contrast, tiered information disclosure disrupts this
equilibrium. Under the ”Pool-High” strategy—where high-
value bidders are pooled and informed of their relative posi-
tion—bidders tend to underbid. Conversely, the ”Pool-Low”
strategy, which pools low-value bidders and informs them of
their tier, prompts overbidding. These behaviors align with
social comparison theory, which suggests that individuals
adjust their actions based on their perceived position rela-
tive to others(Tor and Garcia 2023; Garcia, Tor, and Schiff
2013). High-value bidders in the ”Pool-High” tier, aware of
the intense competition within their group, may bid conser-
5

Figure 3: Revenue Comparison Across Disclosure Strategies and Scenarios. The x-axis represents the average probability
of full disclosure under various scenarios. For instance, pooling bidders with values above the 20th percentile corresponds to
a full disclosure probability of 0.2. The y-axis shows the average revenue generated per round for each configuration. The
chart compares four disclosure strategies: Full Disclosure (depicted as a horizontal line); Pool-High and Pool-Low with each
strategy evaluated across different cut-off values; Random, where bidders are randomly selected for full disclosure without
providing additional information to the remaining bidders.
vatively to avoid overpaying. Conversely, low-value bidders
in the ”Pool-Low” tier may perceive an opportunity to com-
pete more aggressively, resulting in overbidding.
The inclusion of additional value information, such as the
average true valuation within the pooled tier, further reduces
deviations from truthful bidding. This richer information in-
stills greater confidence in bidders’ valuations, resulting in
more stable and consistent bidding behavior. Analyzing bid-
ding records reveals numerous instances where agents up-
date their estimated valuations to align with the provided
average value and subsequently bid accordingly (see the fol-
lowing example). This behavior reflects the anchoring effect
(Tversky, Kahneman, and Slovic 1982), a cognitive bias in
which individuals rely heavily on reference points—such as
disclosed average values—when making decisions. By an-
choring their bids to these provided values, bidders demon-
strate a clear reliance on structured information to guide
their strategies.
Second, we delve into bidders’ explanations (see Ap-
pendix for examples) to understand how their beliefs are
updated based on accessible information. Interestingly, the
records reveal no references to the values or potential behav-
iors of other bidders (as illustrated in the example below).
This suggests that the LLM-based agents’ decision-making
processes do not explicitly incorporate strategic reasoning
about competitors. Notably, in the context of second-price
auctions, this behavior aligns with theoretical expectations,
as bidding truthfully to one’s estimated value is the domi-
nant strategy and should not be influenced by the potential
actions or valuations of competitors.
Given that my true value is in the high-value tier
and the average value of bidders in this tier is
0.6657625810811798, I estimate my true value to
be around this average. In a second-price auction,
the optimal strategy is to bid your true value. There-
fore, I bid 0.6657625810811798, aligning with my
estimated true value.
However, it remains unclear whether this observed behav-
ior is a result of the trained rationality of LLM agents or due
to a limitation in their reasoning capabilities that prevents
them from factoring competition into their decision-making.
We did not extensively analyze this in the present study, but
it presents an interesting avenue for future research. For in-
stance, shifting to a first-price auction, where strategic rea-
soning about competitors is critical, could provide further
insights into the agents’ capabilities and the impact of dif-
ferent auction formats on their decision-making processes.
Revenue analysis The revenue results, illustrated in Fig-
ure 4, reveal distinct patterns across the different informa-
tion disclosure strategies. The Pool-Low strategy and Full
Disclosure consistently generate similar revenue outcomes.
This similarity arises because both strategies effectively re-
veal the true valuations of the highest bidders. As long as
these bidders bid truthfully, they secure the winning bid, re-
sulting in comparable revenue levels across these strategies.
In contrast, the Pool-High strategy exhibits increasing
revenue as the percentage of disclosed information rises.
This effect stems from the likelihood that top bidders will
more accurately estimate their true valuations with addi-
tional information. As we see in the rationality analysis,
without full disclosure, high-value bidders often rely on
pooled signals, leading to conservative value estimations. As
6

Figure 4: Social welfare Comparison Across Disclosure Strategies and Scenarios. The x-axis represents the average proba-
bility of full disclosure under various scenarios. For instance, pooling bidders with values above the 20th percentile corresponds
to a full disclosure probability of 0.2. The y-axis shows the average revenue generated per round for each configuration. The
chart compares four disclosure strategies: Full Disclosure (depicted as a horizontal line); Pool-High and Pool-Low with each
strategy evaluated across different cut-off values; Random, where bidders are randomly selected for full disclosure without
providing additional information to the remaining bidders.
more information is disclosed, their bid accuracy improves,
driving up revenue.
When pooled information includes only the tier, bidding
records suggest that high-value bidders typically estimate
their bids a stable constant (our bidding records suggest
0.75, which happens to be the average value from a uni-
form distribution drawing [0.5, 1]), resulting in stable rev-
enue across quantiles. However, when pooled information
includes both the tier and the average true value within the
tier, the additional detail creates significant information rents
for top-tier bidders. For instance, pooling the top two bid-
ders yields a higher average true value than pooling the top
five bidders because the smaller subset is concentrated at the
upper end of the value distribution. As we see from the ra-
tionality analysis, the higher average shapes bidder’s belief
and incentivizes aggressive bidding among top-tier bidders,
leading to revenue gains. These findings align with theoret-
ical results from Bergemann et al., which demonstrate that
strategically designed information disclosure—such as pool-
ing and signaling—can generate higher revenue than full
disclosure by effectively balancing uncertainty and compe-
tition.
Social Welfare Analysis The social welfare results, also
shown in Figure 4, provide insights into how information
disclosure strategies influence the overall efficiency of the
auction system. Social welfare, defined as the total true value
obtained by the winning bidders, serves as a critical metric
for evaluating resource allocation efficiency—ensuring that
items are awarded to those who value them most.
The Pool-High strategy consistently underperforms com-
pared to other strategies at lower thresholds. This under-
performance is due to the reduced transparency caused by
pooling information for high-value bidders, which limits
their ability to bid effectively, thereby reducing allocation
efficiency. However, as the threshold increases (e.g., 0.8),
the transparency improves, and social welfare outcomes un-
der Pool-High approach those of Full Disclosure, reflecting
more efficient allocation. Similarly, for the Random-pooling
strategies, social welfare increases with the probability of
full disclosure.
Conversely, the Full Disclosure and Pool-Low strategies
consistently yield higher social welfare by ensuring that
high-value bidders—who contribute most significantly to
social welfare—receive adequate information. The stability
of social welfare under Pool-Low across thresholds indicates
that pooling information for lower-value bidders has mini-
mal adverse impact, provided high-value bidders are suffi-
ciently informed.
Conclusion
In this paper, we propose InfoBid, a simulation framework
leveraging large language models (LLMs) to explore the ef-
fects of information disclosure strategies in auction environ-
ments. Through simulations with diverse signaling strate-
gies, we demonstrate the critical role of targeted information
disclosure to selective bidders in shaping auction outcomes.
Additionally, our analysis highlights the importance of ex-
amining agents’ reasoning processes to uncover their capa-
bilities and limitations. By aligning with both economic and
social learning theories, our findings offer valuable insights
into optimizing auction outcomes through strategic informa-
tion disclosure. This study advocates for future research to
further understand and enhance LLM agents’ strategic rea-
soning, advancing their application in market design and be-
yond.
7

References
Badanidiyuru, A.; Bhawalkar, K.; and Xu, H. 2018. Tar-
geting and signaling in ad auctions. In Proceedings of the
twenty-ninth annual ACM-SIAM symposium on discrete al-
gorithms, 2545–2563. SIAM.
Bergemann, D.; Heumann, T.; Morris, S.; Sorokin, C.; and
Winter, E. 2022. Optimal information disclosure in classic
auctions. American Economic Review: Insights, 4(3): 371–
388.
Chen, J.; Yuan, S.; Ye, R.; Majumder, B. P.; and Richardson,
K. 2023. Put your money where your mouth is: Evaluating
strategic planning and execution of llm agents in an auction
arena. arXiv preprint arXiv:2310.05746.
Cheng, Y .; Cheung, H. Y .; Dughmi, S.; Emamjomeh-Zadeh,
E.; Han, L.; and Teng, S.-H. 2015. Mixture Selection, Mech-
anism Design, and Signaling. arXiv:1508.03679.
Emek, Y .; Feldman, M.; Gamzu, I.; PaesLeme, R.; and Ten-
nenholtz, M. 2014. Signaling schemes for revenue maxi-
mization. ACM Transactions on Economics and Computa-
tion (TEAC), 2(2): 1–19.
Feinberg, Y .; and Tennenholtz, M. 2005. Anonymous bid-
ding and revenue maximization. The BE Journal of Theoret-
ical Economics, 5(1): 000010220215345981061.
Feizi, S.; Hajiaghayi, M.; Rezaei, K.; and Shin, S. 2023.
Online Advertisements with LLMs: Opportunities and Chal-
lenges. arXiv preprint arXiv:2311.07601.
Garcia, S. M.; Tor, A.; and Schiff, T. M. 2013. The psy-
chology of competition: A social comparison perspective.
Perspectives on psychological science, 8(6): 634–650.
He, Y .; Chen, X.; Wu, D.; Pan, J.; Tan, Q.; Yu, C.; Xu, J.; and
Zhu, X. 2021. A unified solution to constrained bidding in
online display advertising. In Proceedings of the 27th ACM
SIGKDD Conference on Knowledge Discovery & Data Min-
ing, 2993–3001.
Ie, E.; Hsu, C.-w.; Mladenov, M.; Jain, V .; Narvekar, S.;
Wang, J.; Wu, R.; and Boutilier, C. 2019. Recsim: A config-
urable simulation platform for recommender systems. arXiv
preprint arXiv:1909.04847.
Jeunen, O.; Murphy, S.; and Allison, B. 2023. Off-Policy
Learning-to-Bid with AuctionGym. In Proceedings of the
29th ACM SIGKDD Conference on Knowledge Discovery
and Data Mining, 4219–4228.
Levin, J.; and Milgrom, P. 2010. Online advertising: Het-
erogeneity and conflation in market design. American Eco-
nomic Review, 100(2): 603–607.
Liu, X.; Yu, C.; Zhang, Z.; Zheng, Z.; Rong, Y .; Lv, H.;
Huo, D.; Wang, Y .; Chen, D.; Xu, J.; et al. 2021. Neural
auction: End-to-end learning of auction mechanisms for e-
commerce advertising. In Proceedings of the 27th ACM
SIGKDD Conference on Knowledge Discovery & Data Min-
ing, 3354–3364.
Milgrom, P. 2010. Simplified mechanisms with an appli-
cation to sponsored-search auctions. Games and Economic
Behavior, 70(1): 62–70.
Milgrom, P. R.; and Weber, R. J. 1982. A theory of auc-
tions and competitive bidding. Econometrica: Journal of
the Econometric Society, 1089–1122.
Myerson, R. B. 1981. Optimal auction design. Mathematics
of operations research, 6(1): 58–73.
Nguyen, P. H.; Gligorijevic, D.; Borah, A.; Adalinge, G.; and
Bagherjeiran, A. 2023. Practical Budget Pacing Algorithms
and Simulation Test Bed for eBay Marketplace Sponsored
Search. In AdKDD@ KDD.
openai. 2024. GPT-4 Technical Report. arXiv:2303.08774.
Ostrovsky, M.; and Schwarz, M. 2011. Reserve prices in in-
ternet advertising auctions: A field experiment. In Proceed-
ings of the 12th ACM conference on Electronic commerce ,
59–60.
Tor, A.; and Garcia, S. M. 2023. The neuroscience of social
comparison and competition. Cognitive, Affective, & Behav-
ioral Neuroscience, 23(3): 920–943.
Touvron, H.; Lavril, T.; Izacard, G.; Martinet, X.; Lachaux,
M.-A.; Lacroix, T.; Rozi `ere, B.; Goyal, N.; Hambro, E.;
Azhar, F.; et al. 2023. Llama: Open and efficient founda-
tion language models. arXiv preprint arXiv:2302.13971.
Tversky, A.; Kahneman, D.; and Slovic, P. 1982. Judgment
under uncertainty: Heuristics and biases. Cambridge.
Vickrey, W. 1961. Counterspeculation, auctions, and com-
petitive sealed tenders. The Journal of finance, 16(1): 8–37.
Yue Yin. 2023. Accelerating Advertising Optimization: Un-
leashing the Power of Ads Simulation. https://www.uber.
com/blog/unleashing-the-power-of-ads-simulation/. Ac-
cessed: 2024-11-21.
Zeng, A.; Liu, X.; Du, Z.; Wang, Z.; Lai, H.; Ding, M.; Yang,
Z.; Xu, Y .; Zheng, W.; Xia, X.; Tam, W. L.; Ma, Z.; Xue,
Y .; Zhai, J.; Chen, W.; Zhang, P.; Dong, Y .; and Tang, J.
2023. GLM-130B: An Open Bilingual Pre-trained Model.
arXiv:2210.02414.
Zhao, Q.; Wang, J.; Zhang, Y .; Jin, Y .; Zhu, K.; Chen, H.;
and Xie, X. 2024. CompeteAI: Understanding the Competi-
tion Dynamics of Large Language Model-based Agents. In
Forty-first International Conference on Machine Learning.
8

Appendix
Details of the Framework
Auction and Signaling Process In this section, we introduce the detailed auction and signaling process used in our frame-
work:
1. Auction Context Initialization: In this initial phase, the auctioneer gathers all relevant information for the current auction
round.
2. Information Disclosure: The auctioneer discloses information to bidders according to the pre-defined strategy. This process
includes public information, such as the number of participants or common priors, and private signals tailored to each bidder.
3. Signal Reception and Belief Update : Upon receiving the disclosed information, bidders analyze received information to
update their beliefs about their true valuations and adapt bidding decision strategically. This process is operationalized
through LLMs.
4. Bid Generation and Submission: Guided by their updated beliefs, bidders generate their bids for the current auction round.
This process is operationalized also through LLMs.
5. Bid Collection and Auction Execution : The auctioneer collects all submitted bids and runs the auction based on the
configured mechanism.
6. Outcome Announcement After executing the auction, the auctioneer publicly announces the results, potentially including
the winner’s identity and the price paid.
Prompt Inputs to Bidder Agents
Information Structure
1. Default public information : You are a rational bidder in a second-price auction.
The auction is one-time: you submit the bid and will receive the results.
As a prior, you don’t know your true value towards the current item. You
only know your true-value falls between [0, 1]. Auctioneer may give you more
information. The value of the item for each bidder is independently drawn
from a uniform distribution over [0, 1] and the auction will consist of 10
bidders, including you. This is common knowledge to all bidders. However,
your exact value is private and known only to you, based on signals or
disclosed information provided by the auctioneer.
2. Private signaling:
• Full Disclosure: Your true value towards this current auctioned item is {current
average value }
• Tiered Disclosure without Average Tier Value: Your true value towards this current
auctioned item is not disclosed due to your value is being in the {POOL
LEVEL} value tier. This indicates your value towards this item is {POOL
LEVEL}er than some of other bidders, but the exact value will remain
unknown.
• Tiered Disclosure with Average Tier Value: Your true value towards this current auctioned
item is not disclosed due to your value is being in the {POOL LEVEL } value
tier. This indicates your value towards this item is {POOL LEVEL }er than
some of other bidders, but the exact value will remain unknown. The average
value of all bidders in the same tier with you is {TIER AVG VALUE }.
• Randomized Pool: You have no information about your true value.
Bidding Instruction
Based on this information, submit a bid between 0 and 1, and provide the
following details in your response: name: your name as a bidder. bid: Your
bid for this round (a value between 0 and 1). estimated value: Your estimate
of your true value based on the information received. explanation: A brief
explanation of how you decided at your bid. Please return your response in the
provided format
9

Simulation Variants
Table 1 in illustrates the specific configurations in our simulation design.
Factor Variations
Number of Bidders 10
Value Disclosure Strategy Full Disclosure, Pool-High, Pool-Low, Randomized Pooling
Threshold Quantiles 0.2, 0.4, 0.6, 0.8
Pooled Information for Tiered Pooling Tier Only, Tier and Average Value Information
Repetitions per Configuration 100
Table 1: Simulation Variations
Bidder’s Reasoning
Examples of Bidder’s Explanation on Bidding Decision
1. Explanation under Full Disclosure : In a second-price auction, the optimal strategy
is to bid your true value. This is because if you win, you will pay the
second-highest bid, not your own. Therefore, bidding your true value
maximizes your utility, ensuring you win the item if the second-highest
bid is less than or equal to your true value. Given my true value is
0.3568638462861372, I will bid exactly this amount.
2. Explanation under Tiered Pooling:
• Bid truthfully on the disclosed average value: Given the information that my value is
in the low value tier and the average value of bidders in this tier is
0.17774305518631073, I estimate my true value to be around this average.
In a second-price auction, the optimal strategy is to bid your true
value. Therefore, I will bid 0.17774305518631073, aligning my bid with my
estimated true value..
• Bid apart from the estimated value : Given that my value is in the high value tier
and the average value of this tier is 0.6610732108060862, I estimate
my true value to be slightly above this average, at around 0.7. In a
second-price auction, the optimal strategy is to bid your true value.
However, since I don’t know my exact value, I will bid the average of my
tier, 0.6610732108060862, as it is a reasonable estimate of my true value.
3. Explanation under Randomized Pooling:
• Bid without any information disclosed: Without specific information about my true
value, I assume the expected value of my true value is the midpoint of the
distribution, which is 0.5. In a second-price auction, the optimal strategy
is to bid your true value. Therefore, I bid 0.5, which is my estimated
value based on the uniform distribution assumption.
10
