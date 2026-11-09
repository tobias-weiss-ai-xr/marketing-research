---
title: Information Aggregation with AI Agents
url: https://arxiv.org/abs/2604.20050
category: ai-marketing
subcategory: empirical
date: 2026-04
venue: ''
authors:
- Spyros Galanis
source: arxiv
pdf_url: https://arxiv.org/pdf/2604.20050
pages: 80
chars: 206459
fetched_at: '2026-11-08T13:01:04+00:00'
kb_version: 1
---

# Information Aggregation with AI Agents

Information Aggregation with AI Agents ∗
Spyros Galanis †
September 28, 2026
Abstract
Can Large Language Models (AI agents) aggregate dispersed private information through
trading and reason about the knowledge of others by observing price movements? We conduct
a controlled experiment where AI agents trade in a prediction market after receiving private
signals, across four information structures of increasing complexity. We find that although the
median market is effective at aggregating information in the easy information structures, perfor-
mance deteriorates in the harder structures, suggesting that AI agents struggle in environments
where more than two levels of interactive reasoning are required, a ceiling close to the one doc-
umented in human subjects. Consistent with our theoretical predictions, market accuracy does
not improve from allowing cheap talk communication, changing the duration of the market, or
strategic prompting; initial price has little average effect but matters in the very hard structure.
We also find that “smarter” AI agents perform better at aggregation and are more profitable.
Surprisingly, giving them feedback about past performance does not improve aggregation. A
further wave of markets, run three months later with capability-frontier models, aggregates in-
formation more often in the three easier structures but not in the hardest one, where higher
capability replaces markets that are confidently wrong with markets that hedge near 0.5.
JEL: C91, D82, D83, D84, G14, G41
Keywords: Information Aggregation, AI Agents, Large Language Models, Prediction Markets,
Experiments
1 Introduction
Recent advancements in Large Language Models (LLMs) have enabled the development of AI agents
capable of autonomously executing complex tasks. They can gather private information and reason
about necessary steps based on their prompts, execute actions by invoking external tools and col-
laborating with other agents, and evaluate the success of their actions. Soon, they will be tasked to
trade securities in financial markets, leveraging their private information.1 Sheng et al. (2026) show
∗I would like to thank Andis Sofianos, Diego Marino-Fages, Michael Vlassopoulos, Alessandro Mennuni, Christos
Ioannou and participants at Durham, Southampton, the Durham Edinburgh York workshop, DIRDI Impact and
Invention Conference, and the AI in Finance and Accounting workshop for useful comments. This research is based
on work funded under ESRC grant ES/V004425/1.
†Department of Economics, University of Durham, spyros.galanis@durham.ac.uk.
1Robinhood, one of the biggest retail trading platforms in the U.S., announced in May 2026 that customers can
connect their own AI agents to their account to automate trading and credit card purchases.
1
arXiv:2604.20050v4  [econ.GN]  25 Sep 2026

that hedge funds that adopt generative AI earn 2-4% higher annualized abnormal returns than non-
adopters. Firms are already delegating substantive work to them, and the evidence suggests that
the gains are uneven across tasks. In a field experiment inside a large consulting firm, Dell’Acqua
et al. (2026) find sizeable improvements in quality and speed on tasks that lie inside the capability
frontier of the model, but a deterioration in performance on tasks that lie just outside it.
However, a critical open question remains: to what extent can they reason about the private
information of others (humans or AI agents) when observing their actions (buy or sell orders)?
This is fundamental for deploying AI agents in financial markets, otherwise information may not
get aggregated and prices may diverge from the real value of assets. As Hayek (1945) argues, a
well-functioning pricing system that aggregates information is necessary to achieve efficient out-
comes. Moreover, prices in secondary markets affect real outcomes through their informational role:
managers, capital providers, and regulators learn from prices and use them to guide their decisions,
hence less informative prices feed back into worse outcomes (Bond et al., 2012).
WestudyinformationaggregationbyrunningacontrolledexperimentwithAIagentswhoreceive
private information and trade a security in a prediction market, which pays 0 or 1 based on the
outcome of a Yes/No question. The conjunction of everyone’s information reveals the true value of
the security. Is trading activity enough to drive the price of the security close to its true value, so
that information aggregates?
The intuition behind information aggregation is simple. If the price of a security is high and
a trader thinks its value is low, he will sell, otherwise he will buy. The other traders observe the
price movements and try to infer the private information that led to the buy or sell orders. After
incorporating this (now public) information into their own private information, traders will buy or
sell and the process continues, until all private information is aggregated. However, this aggregation
requires that traders are sophisticated enough to form higher order beliefs about what others know,
what they know about what others know, and so on, in order to interpret their actions and update
their knowledge and beliefs.
Reasoning about the private information of others by observing their actions is a fundamental
human ability, but it is not obvious that AI agents are trained to emulate it. On the one hand, they
already demonstrate impressive capabilities on several domains and Large Language Models (LLMs)
can be prompted to optimise (Yang et al., 2023). On the other hand, partly because they are trained
using Reinforcement Learning from Human Feedback (RLHF), they can emulate human behaviour
in games (Park et al., 2023) and experiments (Horton, 2023), which is not always sophisticated, and
suffer from the same behavioral biases as humans (Bini et al., 2025).
We vary several conditions in the experiment and measure their impact on information aggre-
gation, or market accuracy. The first is the complexity of the information and payoff structure.
There are three traders and three signals, and we consider four levels of difficulty. In the easiest,
each trader needs to reason about the signal of only one other trader to determine whether the
answer to the question is Yes or No. The hardest is a version of the well-known “dirty faces” puzzle,
where each trader gets two signals so interactive reasoning is more complex (Weber, 2001). The
other conditions are allowing AI agents to post public comments, to measure the effect of cheap talk
communication; prompting them to be strategic (forward-looking) or myopic to measure whether
AI agents can implement a strategy over many periods; changing the initial price (0.3,0.5,0.7) to
examine whether price manipulation has an adverse effect; and altering the duration of the market
(3, 6, and 9 rounds) to examine if more trading helps or confuses AI agents.These treatments gen-
erate a total of 144 different market configurations, and we run each configuration at least 12 times,
2

with a diverse set of AI agents, generating 1772 prediction markets in total. We then run an infor-
mation provision treatment, where we inform AI agents, before they trade, about the qualitative
results from the first wave, on which factors were effective on information aggregation and profits,
generating another 1728 prediction markets.
For all four information structures, we construct securities which are ‘separable’.2 Using a result
from Ostrovsky (2012), this allows us to have a sharp theoretical prediction: if AI agents are rational
and sophisticated then information will get aggregated in all Nash equilibria, for any initial price
and irrespective of whether the traders are myopic or strategic, or whether they communicate.
We employ eight LLMs for our main analysis: Claude Haiku 3.5 and 4.5, Gemini 2.5 and 3 Flash,
GPT-4o and GPT-5 mini, gemma3:4b, and qwen3:8b. As a measure of each model’s capabilities,
we adopt the Artificial Analysis Intelligence Index (Artificial Analysis Team, 2025), one of the most
comprehensive publicly available syntheses of model capabilities. The intelligence index integrates
ten evaluation suites, combining performance across reasoning, mathematics, coding, and agentic
workflowtasks, amongothers. Weformtwelveteamsofthreetraders. Eightteamsarehomogeneous,
comprising traders using the same model. The remaining four teams feature a variety of models,
enabling us to test whether “diversity” of intelligence has an impact on information aggregation or
profits.
Our first main finding (Result 1) is that, although the median market is effective in the two
easy structures, the more complex environments we study are associated with worse information
aggregation.3 In particular, the median market across all structures assigns probability 0.91 to the
correct outcome, that is, it prices the winning security (the one that eventually pays 1, whether Yes
or No) at 0.91. In the Easy and Medium structures this probability is almost 1, suggesting that AI
agents understand them completely. In the Hard structure, it drops to 0.73, hence noticeably worse
but still better than random guessing. In the Very Hard structure, however, it drops to 0.5, which is
completely uninformative. Given that the securities are separable in all structures, our hypothesis
that complexity does not influence information aggregation is rejected. These findings align with
related human experiments (Nagel, 1995; Weber, 2001; Kneeland, 2015) demonstrating that most
participants perform up to two steps of iterated reasoning.
We conducted our baseline experiment in January 2026. However, given the rapid pace of
innovation in artificial intelligence, model architectures are updated almost quarterly. To assess
external validity, we conducted an out-of-sample extension of 576 markets in April 2026 using three
newly released capability-frontier models: GPT-5.4, Claude Opus 4.6, and Gemini 3.1 Pro (Section
6.5). Although we find that frontier models are better at aggregating information in the three
easier structures, in the Very Hard structure they perform similarly to the first-wave models, where
capability changes the composition of the failures rather than their frequency: markets that were
confidently wrong are replaced by markets that hedge near 0.5 (Result 13). This suggests that the
deterioration we document in Result 1 is not an artifact of the models available when the first wave
was run.
Our second main finding is to confirm our hypothesis that the following factors do not have
a statistically significant impact on information aggregation: prompting AI agents to be strategic
2Informally, a security is separable if there is no prior belief and candidate price at which every trader’s conditional
expectation of the security equals that price while its value still varies across the states the prior considers possible;
at any uninformative price, some trader has information that moves his expectation away from it. Appendix SA.1
gives the formal definition.
3The average market fares very poorly across all structures, but this is driven mostly by the performance of the
upper 20% tail of the log-error distribution.
3

versus myopic, cheap talk communication, and changing the duration of the market (Results 2, 3,
5). The initial price has no detectable average effect, although it matters in the Very Hard structure
(Result 4).
Our third finding concerns the role of agent intelligence in information aggregation and profits.
Given that interactive reasoning requires sophisticated agents, our hypothesis was that intelligence
would positively impact information aggregation. Indeed, we find that the average intelligence of
the group is associated with a lower average log error (Result 6). To quantify this result, we ran
two quantile regressions, using the median and the upper 20% tail of the log-error distribution.
Although the tail log error is reduced, the impact on the median is statistically insignificant. This
result suggests that the role of intelligence is not to improve the performance of the typical market,
but to avoid the few markets that misprice the security completely, trading at 1 (0) when the
true value is 0 (1). Moreover, we find that the individual profits of an AI agent increase with
his intelligence but decrease as the average intelligence of the group increases. These results are
consistent with previous experiments with humans (Corgnet et al., 2018), yet the Intelligence Index
does not specifically test for interactive reasoning tasks, which is surprising.
An important question is whether AI agents can leverage feedback from past play to improve
future performance. To examine this, we run a later-wave information provision treatment in
which a new wave of AI agents receives qualitative summaries based on the empirical outcomes
of the previous 1,772 markets, using the same model versions as in the first wave. Contrary to
recent literature suggesting that LLMs successfully improve when given performance histories (Yang
et al., 2023), we do not find evidence that this information provision is associated with improved
information aggregation in our setting (Result 11).
Given our result that strategic prompting does not influence information aggregation, we further
examine whether this is because AI agents act strategically but there is no impact on information
aggregation, as predicted by economic theory, or they are just unable to act strategically. We do
this by examining the public messages they post and the private messages that are only visible by
their future selves. AI agents could act strategically if the public and private messages differ. For
example, they could post public messages in order to lie about their signal or withhold information,
when prompted to be strategic. If they understand the dynamic nature of the market, they could use
their private messages to instruct their future selves on how to implement a multi-round strategy,
or be more inclined to publicly reveal their signal in the last round they are trading.
We introduce three measures of communication strategy: semantic alignment between private
and public messages (cosine similarity), information hoarding (word gap between public and pri-
vate), and direct deception, measured by the information revealed about the trader’s signal from
his public message, as judged by an AI agent ex post. We find that while the strategic treatment
has no effect, the agents’ behavior shows that they do have some understanding of the strategic
nature of the environment. In 99% of markets, agents on average hoard information, generating
public announcements that are significantly shorter and semantically detached from their internal
private reasoning. Furthermore, making agents aware of prior experimental outcomes widens the
word gap and increases direct deception.
Our text analysis also reveals what initially appears to be a sophisticated inter-temporal com-
munication strategy. Rather than maintaining a constant rate of deception, AI agents display a
distinct “sawtooth” pattern of revelation: they reveal little in the opening rounds, but their prob-
ability of truthful revelation increases at specific intervals (Rounds 3, 6, and 9). At first glance,
this mimics a sophisticated agent who selectively reveals more only when the financial penalty for
4

honesty drops to zero. However, closer analysis shows that this sawtooth pattern is not consis-
tent with dynamic planning, as it persists even when we restrict our sample to 9-round markets.
Agents prematurely drop their deception in Rounds 3 and 6, acting as if the game is ending, before
reverting to high-deception baseline behaviors in the subsequent rounds. Moreover, because the
trading order is fixed, each trader has his own final trading opportunity (for example, Rounds 4
and 5 for the first two traders in six-round markets), at which revealing his signal is costless; yet
no trader increases revelation there. This suggests that AI agents do not fully grasp the dynamic
nature of the market and they cannot plan ahead. Rather than executing a cohesive inter-temporal
plan via backward induction, the models appear constrained by pattern matching and limitations
in multi-step reasoning tasks (Dziri et al., 2023).
The inability to plan ahead aligns with recent findings in the computer science literature demon-
stratingthatLLMslackthecapacityforautonomousmulti-stepplanninganddynamicstatetracking
(Valmeekam et al., 2023; Kambhampati et al., 2024). It can also explain why the strategic prompt-
ing does not produce any change in behavior. We instruct AI agents to be strategic by telling them
to maximise their payoff in the current and all future rounds where they trade. If they cannot plan
ahead, then they cannot devise a multi-period strategy.
We conclude by motivating our choice of the prediction market as the most suitable experimen-
tal microstructure to study information aggregation with AI agents. First, these mechanisms are
widely used in the real world for forecasting and asset pricing. Historically employed to predict
political events (Iowa Electronic Markets) and used by major corporations (Cowgill and Zitzewitz,
2015) and governments (The Economist, 2021), prediction markets have recently experienced rapid
growth in adoption and volume. Platforms such as Polymarket and Kalshi now facilitate substan-
tial trading volumes, serving as real-time aggregators of public sentiment. Notably, Diercks et al.
(2026) demonstrate that Kalshi markets achieve accuracy comparable to, or exceeding, professional
forecasts for CPI and GDP releases. Furthermore, the pricing mechanism powering these markets,
the Market Scoring Rule (MSR), is mathematically equivalent to the Constant Function Market
Maker, a special case of the Automatic Market Maker (AMM) used extensively in decentralized
finance (DeFi) and blockchain trading (Frongillo et al., 2024). Lehar and Parlour (2025) show
theoretically and empirically that AMMs have some advantages over limit order markets, such as
providing more stable liquidity during extreme market events, and exhibiting smaller price impact
with lower volatility.
Second, theMSRprovidesastructuredenvironmentthateliminatesstandardmarketmicrostruc-
ture frictions. In traditional continuous double auctions, an agent must submit a limit order and
endure execution risk while waiting for a counterparty. The MSR, conversely, acts as an automated,
inventory-based market maker, deterministically adjusting prices and guaranteeing instant liquidity
for any buy or sell order.4 This design is well suited to evaluating AI agents. Because LLMs lack
persistent endogenous memory and cannot asynchronously “wait” for an order to fill, sequential
trading against a deterministic AMM matches their autoregressive processing. By guaranteeing liq-
uidity and removing execution latency, our design isolates the price discovery process from standard
market-microstructure frictions, so that failures to aggregate information cannot be attributed to
execution risk, counterparty search, or liquidity timing. Residual non-reasoning channels, such as
prompt comprehension or the mapping of beliefs into trades, are mitigated by providing each trader
with explicit price-impact calculations for candidate trades (Section 2).
Finally, the MSR framework provides a benchmark that does not rely on the presence of exoge-
4See Ostrovsky (2012) and Galanis et al. (2024) for examples.
5

nous noise traders or strategic market makers. In traditional sequential trade models or strategic
auction frameworks (Kyle, 1985; Glosten and Milgrom, 1985), information revelation is inherently
confounded by the necessity of noise or liquidity trader volume to prevent market failure and pro-
vide strategic camouflage for informed agents. In contrast, our model provides tractable predictions
regarding price paths, trading volume, and agent profits under myopic behavior, while theoretically
predicting information aggregation across all Nash equilibria.
1.1 Literature
Our paper contributes to several strands of the literature. The first studies under which conditions
information gets aggregated. Ostrovsky (2012) and Chen et al. (2012) show that in a market with
either myopic or strategic traders, separable securities are both necessary and sufficient for informa-
tion aggregation, using both the model of Kyle (1985) and the Market Scoring Rule (McKelvey and
Page (1990), Hanson (2003, 2007)), which is directly applicable to prediction markets. Information
aggregation is based on the “we cannot agree to disagree” and “no trade” theorems of Aumann
(1976), Milgrom and Stokey (1982), and Geanakoplos and Polemarchakis (1982).
Plott and Sunder (1988) provide one of the first laboratory studies of information aggregation,
showing that markets with human traders aggregate diverse private information in some environ-
ments, such as with a complete set of contingent claims, but not in others. Page and Siemroth
(2021) find that prices incorporate almost all public information but less than 50% of private infor-
mation held by traders, using 664 experimental markets drawn from five studies. Rasooly and Rozzi
(2025) conduct a field experiment with humans, where prices are randomly shocked in 817 predic-
tion markets, finding that the effect was persistent even after 60 days. Bossaerts et al. (2024) study
field prediction markets that use the same logarithmic market scoring rule as the current paper, and
identify informed traders from their trading behaviour alone. They find that informed traders are
a small minority of participants, that only these traders earn the profits an informed trader should
earn in this mechanism, and that markets containing them forecast better than markets that do
not. Galanis et al. (2024) show theoretically and experimentally that ambiguity aversion can lead to
no information aggregation with separable securities, but a new class, strongly separable securities,
overcomes this limitation. We contribute to this literature by conducting the first, to our knowledge,
experiment that studies information aggregation with AI agents that trade in a prediction market.
A related experimental literature measures the depth of interactive reasoning that human sub-
jects display, using guessing games (Nagel, 1995; Costa-Gomes and Crawford, 2006), the cognitive
hierarchy model (Camerer et al., 2004), the dirty faces game (Weber, 2001), and ring games (Knee-
land, 2015), and consistently finds that most subjects perform no more than two steps of interactive
reasoning. We similarly find that in the Very Hard structure, which emulates the dirty faces game
and requires more than two steps of interactive reasoning, even the most capable models struggle
to aggregate information.
ThesecondstrandstudiestheimpactofalgorithmicandAIpoweredtradingonmarketefficiency.
An established empirical literature finds that algorithmic and high-frequency trading improve liq-
uidity and price discovery (Hendershott et al., 2011; Brogaard et al., 2014), although Weller (2018)
shows that algorithmic trading can reduce information acquisition, so that prices reflect less fun-
damental information. Closer to our setting, Colliard et al. (2025) show using experiments that
algorithmic market makers struggle to learn competitive pricing strategies, resulting in less compet-
itive market outcomes. Dou et al. (2025) show with simulation experiments that AI speculators, the
integration of algorithmic trading with reinforcement-learning algorithms, collude with each other,
6

undermining competition and market efficiency. Dugast and Foucault (2025) show that data abun-
dance increases price informativeness. The current paper shows that AI agents struggle to reason
interactively as the environment becomes more complex, hence market efficiency is reduced.
The third strand applies machine learning and LLMs to financial markets. Gu et al. (2020)
demonstrate significant economic gains for investors who use machine learning forecasts, whereas
Lopez-Lira and Tang (2025) show that ChatGPT 4 can predict stock market reactions from news
headlines, and that performance improves with model size. Closest to our paper are experiments
that place LLM agents in laboratory asset markets designed to elicit bubbles with human partici-
pants. Henning et al. (2025) find that, in a classic experimental finance paradigm, LLM traders are
“textbook-rational”: unlike human subjects, who consistently generate bubbles, they price the asset
near its fundamental value. Saxena et al. (2026) document a wider spectrum of behaviors, ranging
from coordination on the fundamental value to speculative bubbles, with advanced models adapting
to, and exploiting, less sophisticated counterparts. Our results also qualify the textbook-rationality
finding. In our setting, AI agents fail to behave according to the textbook prediction, even though
the Very Hard structure is a version of the dirty faces puzzle, whose solution is almost certainly
part of their training data. One explanation is that if the game is not presented in a format similar
to a text they have read, they cannot make the connection.
The fourth strand is at the intersection of economics and computer science. One branch studies
how AI agents behave in economically interesting problems (Chen et al. (2023), Bini et al. (2025)),
whereasanotherstudieshowexperimentationwithLLMscanprovideinsightsabouthumanbehavior
(Charness et al. (2023), Korinek (2023), Bail (2024), Manning et al. (2024)). We contribute to this
strand by conducting one of the first experiments with prediction markets and LLMs.
The paper is organised as follows. Section 2 describes the main elements of the prediction market
and the teams of AI agents that are used in the experiment. Section 3 discusses the experimen-
tal design, including the four information structures, and Section 4 lists our general hypotheses.
Section 5 describes the data and we present our results in Section 6. Section 7 concludes. In the
Supplementary Appendix, we provide the full prompts and run robustness checks.
2 Preliminaries
This section introduces the information and payoff structure, the prompt design, the AI agents and
the notion of information aggregation. The next section details our experimental design.
2.1 Information and Payoff Structure
In each prediction market there are three agents, who trade sequentially for 3,6, or 9 rounds. Agent
1 trades in rounds 1,4, and 7, agent 2 trades in rounds 2,5, and 8, and agent 3 trades in rounds
3,6, and 9. The information structure is determined by 3 signals,da, db, dc, each with two possible
realisations, 0 (‘No’) and 1 (‘Yes’). A state of natureωis determined by the realisation of these
three signals. Hence, the state spaceΩ ={a, b, c, d, e, f, g, h}consists of 8 states, shown in Table
2. For example, statea= (1,1,1)realises when all three signals resolve to Yes. In all treatments,
traders have a common uniform prior onΩand each signal resolves to 1 with probability0.5. The
draws of each signal are independent. There are two tradable assets, which are complementary.
The first asset,X: Ω→R(‘betting on Yes’, or Yes shares), pays 1 if the answer to the prediction
market question is Yes, and0otherwise. The second asset,X′ (‘betting on No’, or No shares), pays
7

1 if the answer to the question is No, and 0 otherwise. Therefore, the price ofXis always 1 minus
the price ofX ′. An information and payoff structure (structure in short) determines which signals
are received by which trader, and on which states the answer to the question is Yes, so thatXpays
1. Section 3.1 describes the four structures we use in the experiment.
2.2 Logarithmic Market Scoring Rule
At the beginning of the market an initial price between 0 and 1 is set forX(the Yes shares) by the
market maker. The price of the No shares is set accordingly. Each trader is endowed with £1000
and they trade sequentially in each round. When it is his turn, a trader can buy or sell Yes and No
shares, as well as do nothing (Hold). The pricing mechanism uses the Logarithmic Market Scoring
Rule (LMSR). The price of Yes ispY = eηqY eηqY +eηqN , whereηis a liquidity parameter andq Y , qN
denote the number of outstanding Yes and No shares.5 The LMSR is a special case of a Market
Scoring Rule (MSR) (McKelvey and Page (1990), Hanson (2003, 2007)). Because the LMSR uses
the Logarithmic Scoring Rule, which is proper, it has the following property. If the trader is risk
neutral and myopic, so that he only maximises the expected value of his payoff for the current
round, then he will trade up to the point where the price of the Yes shares is equal to his posterior
belief that the answer to the prediction market question is Yes. We call this the myopically optimal
price.
2.3 Information Aggregation
Traders receive their private information before trading, by learning the realisation of their signals.
The four information and payoff structures we employ are described in detail in Section 3.1. In all
structures, the conjunction of the knowledge of the three traders reveals the true value ofX.6 This
means that if traders communicated truthfully, the true value of Yes (0 or 1) would be revealed. If
traders are myopic and this is common knowledge, then the true value ofXis revealed in 3 rounds,
after everyone has traded once, as we show in Section 3.2. However, agents can be strategic and
although in some treatments they are allowed to exchange information publicly, this is cheap talk.
We say thatinformation gets aggregatedat stateωif the price ofXin the final round is equal
(or very close) to the true value of Yes, which isX(ω).
The main purpose of this paper is to test our theoretical predictions about the market charac-
teristics that improve or hinder information aggregation. Our measure of success for a market is
therefore the logarithmic error,−[yln(p) + (1−y) ln(1−p)], between the true value ofXat state
ω, denotedy=X(ω), and the final price ofXin the market, denotedp. 7 We also examine the
trade volume and profitability of traders in markets.
5The liquidity parameter (we useη= 0.01) determines how quickly the price ofXchanges when a trader buys
or sells. See Cultivate Labs (2021) for an explanation of how the logarithmic MSR is implemented in practice and
Schlegel et al. (2026) for axiomatic foundations.
6This assumption is made by several papers in the literature, such as Plott and Sunder (1988) and Ostrovsky
(2012).
7When calculating the logarithmic error in the data,pis restricted to be in[ϵ,1−ϵ],ϵ= 10 −15, so that we avoid
having an infinite error. The maximum error with this restriction is around34.5.
8

2.4 AI Agents
We conducted our experiment with a variety of Large Language Models (LLMs). For the first
two waves, we employed eight distinct models. The first six were accessed through an Application
Programming Interface (API) and are closed-weight models: Claude Haiku 3.5, Claude Haiku 4.5,
Gemini 2.5 Flash, Gemini 3 Flash, GPT-4o, and GPT-5 mini. The last two were open-weight
models and they were run locally: gemma3:4b, and qwen3:8b.8 We formed twelve teams of three
traders each, which participated in every treatment at least once. Eight teams were homogeneous,
each comprising traders using the same model. The remaining four teams featured a variety of
models; in these heterogeneous teams, the models in Table 1 are listed in trading order (the first
listed model is trader 1, and so on), and the assignment of models to positions is fixed across all
markets. As a measure of each model’s capabilities, we adopted the Artificial Analysis Intelligence
Index (Artificial Analysis Team, 2025), accessed on January 6, 2026.9 This is one of the most
comprehensive and publicly available syntheses of model capabilities. It combines performance
across reasoning, knowledge, mathematics, coding, instruction following, long-context reasoning
and agentic workflow tasks.10 See Table 1 for details, where we also report the average intelligence
and standard deviation for all heterogeneous teams. Finally, for all models we set temperature at
1. This is the default, neutral setting in many APIs, so that text generation is neither too rigid
(deterministic) nor chaotic. In the Supplementary Appendix, Figures SA.4 and SA.5 show the
performance of each model in terms of log error and profits.
In Section 6.5, we report the results from a third wave of 576 markets that we ran in April 2026,
with three frontier models: GPT-5.4, Claude Opus 4.6, and Gemini 3.1 Pro, to check for robustness
of our main results and in particular Result 1. The Artificial Intelligence Indices, accessed in April
2026, are not comparable with those accessed in January 2026 for the previous LLMs, as different
tests and evaluations of models are added over time. Therefore, we keep the analysis separate.
2.5 Prompt Design
When chatting back and forth with an LLM, it appears as if it can recall the conversation and answer
accordingly. However, inherently an LLM has no memory, it just ‘reads’ the whole conversation
every time it is called to answer. This means that whenever we call an AI agent to trade in a round,
we need to dynamically generate a prompt that describes the prediction market, lists the trading
history and previous private or public comments, calculates the trader’s portfolio and price impact
of various trades, specify the trader’s goal and ask for a reply.
The prompt we construct in each round contains the following parts. Part one provides the
details of the market, such as the question, whether comments are allowed, who participates, how
many rounds there are in the market and what is the current round. Part two describes the public
8In open-weight models the parameters are available for modification and they can be run locally. However, they
are not open-source, because the code or the training data are not necessarily released.
9The intelligence scores were accessed athttps://artificialanalysis.ai/evaluations/
artificial-analysis-intelligence-index. Note that the scores change over time as new models and new
evaluations are added. The intelligence index encompasses many studies which evaluate the performance of LLMs
across reasoning, knowledge, mathematics, coding, instruction following, long-context reasoning and agentic workflow
tasks. Some of these are: MMLU-Pro (Wang et al., 2024) , GPQA Diamond (Rein et al., 2024), HLE Phan et al.
(2025), AIME 2025, SciCode (Tian et al., 2024), LiveCodeBench (Jain et al., 2024), IFBench (Pyatkin et al., 2025),
Terminal-Bench Hard, andτ2-Bench Telecom (Barres et al., 2025).
10See Appendix A in Kim et al. (2025) for details.
9

Table 1: AI Models, Team Compositions and Intelligence
Team Composition Average Intelligence (Standard Deviation)
Homogeneous Teams (3 Identical Agents)
3x Gemini 3 Flash 46 (0)
3x GPT-5 mini 41 (0)
3x Claude Haiku 4.5 30 (0)
3x Gemini 2.5 Flash 21 (0)
3x GPT-4o 19 (0)
3x qwen3:8b 15 (0)
3x Claude Haiku 3.5 12 (0)
3x gemma3:4b 7 (0)
Heterogeneous Teams (Mixed Agents)
Claude Haiku 4.5, Gemini 3 Flash, GPT-5 mini 39 (8.1)
Gemini 3 Flash, GPT-4o, qwen3:8b 26.6 (16.8)
Gemini 2.5 Flash, GPT-4o, Claude Haiku 3.5 17.3 (4.7)
gemma3:4b, qwen3:8b, Claude Haiku 3.5 11.3 (4)
Frontier Teams, April 2026 (Section 6.5)
3x GPT-5.4 57 (0)
3x Gemini 3.1 Pro 57 (0)
3x Claude Opus 4.6 53 (0)
GPT-5.4, Claude Opus 4.6, Gemini 3.1 Pro 55.7 (2.3)
Notes:GPT-4ocorrespondstothe“gpt-4o-2024-08-06” version, GPT-5minitothe“gpt-5-mini-2025-
08-07” version, Claude Haiku 4.5 to the “claude-haiku-4-5-20251001” version, and Claude Haiku 3.5
tothe“claude-3-5-haiku-20241022” version, andgemini2.5tothe“gemini-2.5-flash-preview-09-2025”.
Gemini 3 Flash corresponds to the “gemini-3-flash-preview" version that was released on December
17, 2025. Models gemma3:4b and qwen3:8b are open-weight models that were downloaded and run
locally, whereas the other models were accessed through an API. All eight models have the same
version number throughout the experiments. The frontier teams correspond to the “gpt-5.4-2026-03-
05”, “claude-opus-4-6”, and “gemini-3.1-pro-preview” versions; their intelligence scores were accessed
in April 2026 and are not comparable to the January 2026 scores of the other teams, as evaluations
are added to the index over time.
10

information, which is shared with all traders, and the private information that is shared with the
current trader. The third part provides an explanation of prediction markets, including what are
the Yes and the No shares. Part four provides an objective for the trader, to be either myopic or
strategic (see Section 3.3).
Part five provides the history of trades up to now, the public comments that have been posted,
and the current portfolio of the trader. As we do not rely on LLMs doing their own mathematical
calculations, the prompt informs the current trader about the maximum number of Yes and No
shares he can buy and sell, as well as the price impact from various trades, for example buying 25%
of the maximum shares he can buy. This provides a comprehensive description of how the price
will move after the AI agent trades. Part six enumerates the qualitative results from the first wave
of the experiment, and it only appears in the Experiment Disclosure treatment. The last part asks
the trader for his trading decision (buy, sell, or do nothing), a private justification, and a public
comment (if it is allowed by the market). See Supplementary Appendix SA.10 for an example of a
prompt.
2.6 Market implementation
We ran our experiments using a prediction market platform, which was originally developed for
running private prediction markets with humans. For this paper, we implemented in Python an
Application Programming Interface (API) which allowed the programmatic execution of trades, as
well as providing access to past trades and calculating the price impact for hypothetical trades to
inform AI agents. We then created a program which creates a new market for each combination
of the given parameters: teams of AI agents, number of rounds, initial price, structure, strategic,
comments allowed. It then orchestrates the trading in rounds, invoking the LLMs using the relevant
APIs, retrieving past trades and comments, calculating price impact for various trades, generating
prompts dynamically for the current trader and executing trades through the API. The final output
for each market is a text file containing all prompts and decisions of the traders, and a CSV file
containing all trades which we use for our quantitative analysis. In the Supplementary Appendix,
Figure SA.1 provides a graphical representation.
3 Experimental Design
Our experimental design focused on six dimensions. The first was the information and payoff
structure that was presented to the traders. We considered four structures (t3s111y2, t3s110,
t3s111, t3s111o2ye2) that are successively more complex, as we explain in Section 3.1. The second
dimension specified the number of trading rounds: three, six and nine. Given that there are three
traders in all markets, each AI agent trades once if there are three rounds, twice with six rounds
and three with nine rounds. The order of trading is always fixed, so trader 1 trades first, then
trader 2 and trader 3. The third dimension related to whether we prompted the AI agents to be
myopic, so that they are instructed to maximise the current round’s payoff, or strategic, so that
they maximise the sum of payoffs from all rounds where they trade. In principle, they are able to
carry out a strategy across rounds as they can post a private message to their future self.
The fourth dimension was whether public comments were allowed in the market, so that traders
can communicate their private information. The fifth dimension related to the initial price of Yes,
set by the uninformed market maker: we implemented three initial prices, 0.3, 0.5, and 0.7. Recall
11

that the true value of Yes is either 0 or 1. Running this first wave, 4x3x2x2x3 experimental design,
generated results that we included in the last, “Experiment Disclosure” treatment. In this treatment,
AI agents were informed about the qualitative results of the first wave, before trading. Note that
the disclosure wave was necessarily run after the first wave had concluded, so it is a sequential, later-
wave treatment rather than a contemporaneously randomized factor; we discuss the implications
for interpretation in Section 6.3. In summary, we applied a 4x3x2x2x3x2 experimental design to
examine the impact on information aggregation of the difficulty in reasoning about the private
information of others, the initial price, the length of trading, the communication, the information
provision, and explicitly prompting traders to be strategic or myopic.
3.1 Information and payoffs
In this section, we describe the four information and payoff structures that we presented to the
traders. See the Supplementary Appendix for the exact wording of the generated prompts. There
are three signals,da, db, dc, that take two values{0,1}, and they are drawn independently, each with
probability 0.5. Each signal is framed as a Yes/No question. For example,da is the question “Will
sales in country A exceed 1 million?”. The prediction market question is “Will Company X post
next quarter profits that exceed 1 million”, and the answer depends on the realisations of the three
signals. There are therefore 8 possible states, denoted{a, b, c, d, e, f, g, h}, uniquely determined by
the realisations of these three signals. For example, statea= (1,1,1)specifies that all signals resolve
to Yes. The first part of Table 2 depicts the realisations of the three signals and the 8 states. We
say that securityXpays 1 if the answer to the prediction market question is Yes, and 0 otherwise.
A structure specifies the information partition of each trader, the value ofXat each state,
and the realisations of the three signals that determine the true state. The four structures we
consider have the following common characteristics. First, in all states, if the three traders could
talk truthfully and combine their private information, the true value ofXwould become common
knowledge. Second, if traders are myopic, so that the price ofXis always the expected value of
the last person who traded, and everyone being myopic is common knowledge, then the price of
Xbecomes equal to the true value ofXat the end of the third round, when everyone has traded
once. Third, the information and payoff structure (but not the true state) are publicly announced.
Finally, the structures become successively harder as traders need to reason about what others know
and how public information evolves as they trade.
The four structures are t3s111y2, t3s110, t3s111, and t3s111o2ye2.11 The first three specify
the same information structure for the three traders, depicted in Table 2. In particular, trader 1
is privately informed aboutd a, trader 2 is privately informed aboutdb, and trader 3 is privately
informed aboutd c. The partition cells for each trader are depicted in red and black. Trader 1’s
informationpartitionis{{a, b, c, d},{e, f, g, h}}, thetwocellsdenotedinredandblack, andsimilarly
for traders 2 and 3.
The information structure of t3s111o2ye2 specifies that trader 1 is privately informed aboutdb
11The naming of the structures follows this logic: “t3” stands for 3 traders, whereas “s111” and “s110” specify the
realisations of the three signals and therefore the true state. In the first three structures an agent is informed about
his own signal (e.g. trader 1 is informed aboutda, trader 2 aboutdb), except in the last structure where “o2” specifies
that an agent is informed about the two other signals (e.g. trader 1 is informed aboutdb andd c). The “y2” specifies
that at least 2 signals must resolve to Yes so thatXpays 1, whereas “ye2” specifies that exactly 2 signals must resolve
to Yes. In structures t3s110 and t3s111 all three signals must resolve to Yes forXto pay 1. Note that these names
are never revealed to the AI agents.
12

Table 2: Information Structures
States a b c d e f g h
Signals Realisations
da 1 1 1 1 0 0 0 0
db 1 1 0 0 1 1 0 0
dc 1 0 1 0 1 0 1 0
t3s111y2, t3s110, t3s111 Information Structure
Trader 1 a b c d e f g h
Trader 2 a b c d e f g h
Trader 3 a b c d e f g h
t3s111o2ye2 Information Structure
Trader 1 a b c d e f g h
Trader 2 a b c d e f g h
Trader 3 a b c d e f g h
Payoff of Yes (X=)
t3s111y2 1 1 1 0 1 0 0 0
t3s110 1 0 0 0 0 0 0 0
t3s111 1 0 0 0 0 0 0 0
t3s111o2ye2 0 1 1 0 1 0 0 0
andd c, trader 2 is privately informed aboutda andd c, and trader 3 is privately informed about
da andd b. Note that each trader has four partition cells, depicted in the last part of Table 2. For
example, the information partition of Trader 2 is{{a, c},{b, d},{e, g},{f, h}}. This feature makes
interactive reasoning much harder than in the other three structures.
The true value ofXin each state is given in the last part of Table 2, for each structure. In
structure t3s111y2,Xpays 1 if at least two signals resolve to Yes, whereas in t3s110 and t3s111 all
three signals need to resolve to Yes. In the last structure, t3s111o2ye2,Xpays 1 only when exactly
two signals resolve to Yes. We denote with blue the true state in each structure.
3.2 Myopic Prices
To provide a benchmark and understand how the structures compare in terms of complexity, we
derive the equilibrium prices in the first three rounds for each structure, in the case where all traders
are myopic and this is common knowledge. Because the logarithmic scoring rule that we employ in
the prediction market is a proper scoring rule, it has the following property. If a trader is myopic,
so that he only cares about the payoff of the current round, the optimal trading is to move the price
so that it is equal to his expected value ofX, which in this case is equal to his posterior belief that
the answer to the question is Yes. Moreover, this optimal behavior does not depend on what the
previous price is.
Table 3 denotes the true state in blue and the payoff function ofX, for each structure. For
example, t3s111y2 describes that the answer to the prediction market question is Yes if at least two
signals resolve to Yes, hence the payoff function isX= (1,1,1,0,1,0,0,0). We denote with blue
13

the true state, which isa= (1,1,1)in this structure. Trader 1 is informed that his signalda is Yes,
hence he considers states{a, b, c, d}to be possible. His posterior belief about Yes is 0.75, hence he
trades Yes/No shares up until the price of Yes is 0.75.12 A price of 0.75 reveals to everyone that
{e, f, g, h}are impossible, because in that case the price would be 0.25. In other words, the public
information that is revealed in Round 1 is{a, b, c, d}. Trader 2 combines this public information
with his private information,{a, b, e, f}, to deduce that the true state is in{a, b}. As both pay 1,
trader 2 trades so that the price of Yes is 1. Trader 3 deduces that the true value of Yes is 1 and
his trades do not move the price. In all subsequent rounds (if there are any), the price does not
change.
The myopic prices for the other structures are computed similarly. We say that t3s111y2 is the
easiest structure because each trader needs to only reason about the signal of one other trader, in
order to determine the price ofX. In structures t3s110 and t3s111, the traders need to reason about
the signals of everyone else. The only exception is trader 3 in structure t3s110, who receives a 0
signal and therefore immediately deduces that the answer is No, independently of what others have
traded. For that reason, we consider t3s110 to be easier than t3s111.
Structuret3s111o2ye2isthemostdifficultintermsofreasoningaboutothers. First, thepartition
cells for each trader are four, instead of two. Second, reasoning about which state is no longer
possible requires complex counterfactuals. Finally, the myopic price stays the same from round 1
to round 2; however, the public information set shrinks. This may be difficult for the LLMs to
process when reasoning about the private information of others. The true state isaand it is mutual
knowledge (all three traders know it) that statesdandhare impossible. In the first round, the
myopic price of 0.5 makes it common knowledge thatdandhare impossible, otherwise the price
would be 0. In round 2, the myopic price stays the same at 0.5, which makes it common knowledge
thatbis impossible, otherwise (and given thatdis impossible), the price would be 1. Statefis
also excluded because the price would be 0 otherwise.
Although the structure is complex, it is derived from the following well-known “dirty faces” (or
girls with red hats) puzzle (Geanakoplos, 1992; Weber, 2001). Its popularity suggests it is likely
part of the training sets of LLMs used in the experiment.13 However, by looking at the private and
public justifications of the AI agents, it seems that no one made the connection.
It is described as follows. There are three girls who wear either a red or a white hat. They can
only see the hat of the other two girls but not their own. The true state is that all hats are red and
it is therefore mutual knowledge that there is at least one red hat. When asked, each girl announces
she does not know the colour of her hat. The teacher then announces that there is at least one red
hat, a fact that is mutual (but not common) knowledge. Then, the first girl announces that she
does not know the colour of her hat, and so does the second girl. Although these announcements do
not change after the teacher’s announcement, the public knowledge shrinks and the third girl (if she
is very sophisticated) deduces that her hat is red. The teacher’s announcement makes it common
knowledge that the state ‘all hats are white’ is impossible. This prompts the gradual reduction in
the public knowledge, so that in the third round the action changes as well.
12Whether he buys or sells Yes or No shares depends on the previous price. For example, if the initial price of the
market was 0.9 for Yes, he would buy No shares as he has no Yes shares to sell. If the initial price was 0.4, he would
buy Yes shares. In both cases, his trades would drive the price of Yes to 0.75.
13When we asked each LLM, on a separate session, to describe the puzzle, they were fairly accurate.
14

Table 3: Myopic Price of Yes and Public Information
Myopic price Public information Volume Profits
t3s111y2 - Easy
Payoff:X= (1,1,1,0,1,0,0,0)
Trader 1 0.75(a, b, c, d)110 £46
Trader 2 1(a, b)880 £29
Trader 3 1(a, b)0 £0
t3s110 - Medium
Payoff:X= (1,0,0,0,0,0,0,0)
Trader 1 0.25(a, b, c, d)110 £46
Trader 2 0.5(a, b)110 -£41
Trader 3 0b990 £69
t3s111 - Hard
Payoff:X= (1,0,0,0,0,0,0,0)
Trader 1 0.25(a, b, c, d)110 -£64
Trader 2 0.5(a, b)110 £69
Trader 3 1a990 £69
t3s111o2ye2 - Very Hard
Payoff:X= (0,1,1,0,1,0,0,0)
Trader 1 0.5(a, e),(b, f),(c, g)56 £6
Trader 2 0.5(a, c),(e, g)0 £0
Trader 3 0a990 £69
Notes: The table depicts the myopically optimal price per round, the public information that is revealed,
the volume (number of shares) and the profit of the AI agent who trades at that round. We denote
with blue the true state. The myopic price ofXis the expected value ofXgiven the private and public
information for each trader. It reveals information to all other traders, who use it to form their updated
beliefs and trade, and it does not depend on the previous price, however the profits and volume do. For
trader 1, the volume and profits are averaged over the three possible initial prices, 0.3, 0.5, and 0.7. For
the other two traders, volume and profits are the same because trader 1 always moves the price to the
same level, irrespective of the initial price. Where the myopic price is 0 or 1, benchmark volumes and
profits are computed by truncating the price at 0.00005 and 0.99995, since reaching the boundary exactly
requires unbounded share purchases under LMSR.
15

3.3 Myopic vs. Strategic Horizons
The number of periods can influence whether an AI agent acts strategically but the prompt itself
may also have that power. We altered the prompt to test whether the AI agents can act strategically
if they are instructed to do so, and whether this has an impact on information aggregation. We
provided the following prompts.
•Myopic treatment:Use reasoning to determine your belief q, then choose your action (Buy,
Sell, or Hold: Yes and No shares). Maximize your expected payoff in this round only, based
on your belief q and the current price p, ignoring future rounds.
•Strategic treatment:Use reasoning to determine your belief q, then choose your action
(Buy, Sell, or Hold: Yes and No shares). Maximize the sum of your expected payoffs over all
trading rounds, based on your belief q and the current price p. Consider how your current
trade affects the price and the beliefs of others in future rounds.
4 General hypotheses
In order to formulate our hypotheses, we use the following result by Ostrovsky (2012), adapted to
our setting.
Theorem 1.If securityXis separable under information structureΠ, then for any prior distribu-
tionµ, for any strictly proper scoring rules, initial pricey0, and discount factorγ∈(0,1], in any
Nash equilibrium, information gets aggregated.
In Appendix SA.1, we formally define the notion of separability and show that the securities in
all four structures are separable. Given that the logarithmic is a proper scoring rule, this theorem
says that information should get aggregated in all four structures, irrespective of their complexity.14
Hypothesis 1.Information aggregation is unaffected by the complexity of the structure.
The theorem specifies that whether traders are myopic or strategic does not matter. In the
strategic treatment we instruct traders to maximise their payoffs over all future rounds. This is
consistent with a discount factor ofγ= 1, although we do not mention this term in the prompt.
The myopic treatment is consistent withγ= 0. Although the theoretical model excludes a zero
discount factor, it is straightforward to show that asγconverges to 0, traders will behave almost
myopically and reveal their expectations almost truthfully.
Hypothesis 2.Information aggregation is unaffected by prompting AI agents to be strategic or
myopic.
The theoretical model does not allow traders to post comments. However, it is straightforward
to show that this should not hinder information aggregation. Roughly, the reason is that if there is
no information aggregation in the long term, separability implies that at least one trader is able to
achieve strictly positive profits, irrespective of what other traders do or say.
14The implicit assumption of full rationality is indispensable. For example, Galanis and Kotronis (2021) show
that information aggregation may fail if traders are boundedly rational and unaware of some dimensions of their
uncertainty.
16

Hypothesis3.Information aggregation is unaffected by allowing AI agents to post public comments.
A direct application of Theorem 1 ensures that the initial price should not impact information
aggregation.
Hypothesis4.Information aggregation is unaffected by manipulating the initial price of the market.
An important difference from the theoretical model is that it specifies infinitely many rounds
of trading, whereas in the current experiment we have up to 9. Although it is impossible to have
infinitely many rounds in an experiment, we could simulate an infinite horizon by specifying that, in
every round, the game ends with some probabilityp.15 We chose not to include this extra treatment
for the following two reasons. First, the prompt is already long and complicated, so it is not clear
that AI agents would be able to understand and act differently if we added this detail. Second, we
considered that it would be more interesting and practical to understand the effect of lengthening
the duration of the market on information aggregation.
Hypothesis 5.Information aggregation is unaffected by the duration of the market.
We now turn to the role of intelligence on market outcomes. We conjecture that information
aggregation improves as AI agents become smarter, as they should be able to reason better about
the information of others. Furthermore, since greater accuracy leads to higher profits, individual
profits should rise with intelligence. Corgnet et al. (2018) show in a market experiment with
human participants that ‘smarter’ traders are also more profitable. They measure intelligence with
three metrics. Fluid intelligence measures their ability to compute correctly and draw statistical
inferences. Cognitive reflection measures their ability to avoid behavioral biases and update their
beliefs when observing market orders. Theory of the Mind measures whether they can correctly
assess the informational content of trades.
Hypothesis 6.Information aggregation improves as the average intelligence of the group increases.
Hypothesis 7.Individual profits are positively correlated with an agent’s own intelligence, but
negatively correlated with the average intelligence of the market.
The following hypotheses are derived by assuming that traders play the myopic equilibrium.
Table 3 describes the myopically optimal prices, trading volume, and profits, for each of the four
structures and for each trader, using the formulas derived in Supplementary Appendix SA.5. Recall
that the initial price is 0.3, 0.5, or 0.7, which influences both the trading volume and the profits
of the first trader. The other two traders are unaffected because the first trader always moves the
price to the same level, irrespective of the initial price. By computing the average trading volume
for each structure and the average profits for each trader, we formulate the next two hypotheses.
Table SA.8 summarises all calculations. Note that the following hypotheses implicitly assume that
all traders are myopic, hence all markets resolve in round 3 and there is no trading in subsequent
rounds.
The average trading volume across all initial prices is as follows: Easy (990), Medium (1210),
Hard (1210), Very Hard (1046). We therefore have the following hypothesis.
Hypothesis 8.Trading volume is ordered from lowest to highest as follows: Easy (t3s111y2) <
Very Hard (t3s111o2ye2) < Medium (t3s110) = Hard (t3s111).
15See Galanis et al. (2024) for such an experiment with humans in a prediction market.
17

We also compute the average profits for each trader, across all structures and initial prices:
Trader 1 (9), Trader 2 (14), and Trader 3 (52).
Hypothesis 9.Profits are positive for all traders and ordered, from lowest to highest, as follows:
Trader 1 < Trader 2 < Trader 3.
A distinctive feature of the prediction market is that it is ‘constant-sum’ in profits: the sum of
the profits of all traders depends only on the initial pricep0, the final pricep 1, and the realized
outcome, irrespective of how prices fluctuate in between. Under the myopic benchmark the final
price equals the true value of the security in every structure, hence total profits are identical across
structures and average profits are always 25, as shown in Table SA.8. If aggregation fails, the final
price diverges from the true value and total profits fall, so the following hypothesis is a joint test of
the myopic full-aggregation benchmark.
Hypothesis 10.Average profits are not correlated with the difficulty of the structure.
Can AI agents improve their market performance by receiving feedback from historical play?
Yang et al. (2023) propose an information provision technique that leverages LLMs as iterative
optimizers: by updating an LLM’s prompt with a history of past actions and their relative suc-
cess, the model self-corrects, outperforming human-designed prompts by up to 50%. Galanis and
Mikhalishchev (2026) show that market accuracy improves as the cost of acquiring more information
decreases.
Building on these mechanisms, we postulate that providing AI agents with aggregated historical
data about market dynamics will enable them to form more accurate predictions, thereby strictly
improving information aggregation. However, the anticipated effect on individual profitability is
ambiguous. Because this informational shock is provided uniformly across all agents in the market,
no single trader gains an asymmetric informational advantage.
Hypothesis 11.The effect of information provision on information aggregation is positive.
Hypothesis 12.The effect of information provision on individual profits is zero.
5 Data
The dataset consists of observations from 4,076 prediction markets, comprising 12,228 trader-market
observations (three traders per market). Our main sample pools the first wave and the disclosure
wave (3,500 markets) from January 2026; the third wave of 576 markets with the April 2026 frontier
models is kept separate and analyzed in Section 6.5. Table 4 summarises the key market-level
variables, where the upper panel describes the first wave (1772 markets), the middle panel describes
both waves, and the bottom panel describes the third wave.16
We focus on the first wave because the statistics do not change when the second wave is added.
A defining characteristic of the data is the extreme skewness in market performance metrics. While
the median logarithmic score is low (0.089), indicating that the typical market converges to a high-
probability estimate of the correct outcome, the mean score is substantially higher (5.18), driven by
a small subset of markets with extreme errors, where the logarithmic penalty creates scores as high
16With 12 teams of AI agents, the first wave should have consisted of 4x3x2x2x3x12 = 1728 markets. The extra
44 markets were due to a coding error. We decided to keep these markets for completeness.
18

as 34.54. A similar pattern is observed in the Squared Error, where the mean (0.266) is significantly
larger than the median (0.007).
Trading activity varied substantially across sessions. The average market generated a volume
of approximately 1,859 shares traded, though this ranged from inactive markets (0 volume) to very
active markets reaching over 14,290 shares. The teams of AI agents had a mean intelligence score
of 23.56 (SD = 12.2), spanning a range from 7 to 46.
Supplementary Appendix Table SA.10 breaks down market outcomes by information structure
and duration, for the first wave, for both waves, and for the third wave of 576 markets with the
April 2026 frontier models. The data for the first wave (and similarly for both waves) reveal a strict
hierarchy of difficulty, consistent with our experimental design. In the Easy structure (t3s111y2),
markets performed reliably well, with a Mean Squared Error (MSE) as low as 0.07 (for 6 rounds)
and a ‘Crash Rate’ (markets with a log error above 20) of only 1.4%. As complexity increases,
performance degrades sharply and monotonically. In the Medium structure (t3s110), the average
error nearly triples (MSE≈0.2), and by the Very Hard structure (t3s111o2ye2), the market fails
to aggregate information: the MSE reaches 0.43, suggesting a final price of 0.65 when the true
value of the security is 0, whereas the Crash Rate rises to over 19%. The table also serves as a
randomization check. The Average Intelligence (Avg IQ) column shows that agent capabilities are
evenly distributed across all treatment cells in the first two waves (varying tightly between 22.9 and
23.8), indicating that the observed differences in performance are driven by the structural difficulty
of the task and not by chance imbalances in agent composition.
5.1 Methodological Considerations
For our primary OLS specifications, we use CR2 cluster-robust standard errors clustered at the
AI team composition level, featuring small-sample degrees of freedom adjustments (Pustejovsky
and Tipton, 2018). This approach conservatively estimates treatment effects by accounting for
intra-cluster correlation within specific AI teams. For our auxiliary quantile regressions in the
main text, which assess typical market behavior (Q50) and worst-case tail risk (Q80), we report
bootstrapped standard errors (B=200 resamples) rather than analytical cluster-robust standard
errors. Estimating analytical clustered variance matrices for quantile regressions requires local error
density estimation that is usually unstable and fragile in finite samples. Consequently, we employ
standard XY-pair bootstrapping for these specific models. We emphasize that the primary purpose
of these quantile specifications is to demonstrate the behavioral stability of the point estimates
across the error distribution, rather than to serve as exact clustered inference.
Furthermore, because several of our core theoretical propositions predict a null result, relying
solely on conservative CR2 adjustments could theoretically favour our hypotheses by making it
artificially easy to fail to reject the null. We address this concern in two complementary ways.
First, Section 6.6 reports an ex-ante power analysis that computes the minimum detectable effect
(MDE) for each treatment null by Monte Carlo simulation through the exact CR2/Satterthwaite
estimator used in the paper, so that each failure to reject can be read against the smallest effect
the design could have detected.
Second, we stress-test the findings under strictly less conservative variance assumptions: for
market-level outcomes we re-estimate the OLS models with unclustered HC1 standard errors, and
for individual-level outcomes with CR1 errors clustered at the unique market level, which removes
the panel-level team penalty while retaining intra-market dependence. The corresponding tables are
reported in the Supplementary Appendix. The primary null results for communication, strategic
19

Table 4: Descriptive Statistics
Statistic (First Wave) N Mean St. Dev. Min Median Max
Squared Error 1,772 0.266 0.382 0 0.007 1
Logarithmic Score 1,772 5.181 11.770 0 0.089 34.540
Trading Volume 1,772 1,859 1,824 0 1,298 14,290
Avg. Intelligence (Group) 1,772 23.562 12.205 7 19 46
Intelligence SD 1,772 2.875 5.030 0 0 16.862
Initial Squared Error 1,772 0.274 0.164 0.090 0.250 0.490
Initial Logarithmic Score 1,772 0.745 0.347 0.357 0.693 1.204
Statistic (Both Waves) N Mean St. Dev. Min Median Max
Squared Error 3,500 0.277 0.390 0 0.010 1
Logarithmic Score 3,500 5.571 12.152 0 0.105 34.540
Trading Volume 3,500 1,898 1,828 0 1,353 14,290
Avg. Intelligence (Group) 3,500 23.668 12.216 7 19 46
Intelligence SD 3,500 2.847 4.993 0 0 16.862
Initial Squared Error 3,500 0.275 0.164 0.090 0.250 0.490
Initial Logarithmic Score 3,500 0.748 0.348 0.357 0.693 1.204
Statistic (Third Wave, Frontier) N Mean St. Dev. Min Median Max
Squared Error 576 0.149 0.275 0 0 1
Logarithmic Score 576 2.303 8.099 0 0 34.540
Trading Volume 576 1,105 935.245 0 1,164 6,271
Avg. Intelligence (Group) 576 55.667 1.634 53 56.333 57
Intelligence SD 576 0.577 1.001 0 0 2.309
Initial Squared Error 576 0.277 0.165 0.090 0.250 0.490
Initial Logarithmic Score 576 0.751 0.349 0.357 0.693 1.204
Notes:The third-wave panel reports the 576 markets run in April 2026 with the frontier
models. Its intelligence scores use the April 2026 vintage of the Artificial Analysis Intelligence
Index, which is not comparable to the January 2026 scores in the first two panels.
20

prompting, the average initial-price contrasts, and extended market duration (9 rounds) hold even
under these less restrictive assumptions; the Very Hard×low-initial-error interaction of Result
4 likewise remains significant under HC1 (β= 2.861,p <0.01). Conversely, when the team-
level clustering penalty is removed, the 6-round duration, experiment disclosure, and the Medium
information structure cross the threshold into statistical significance in the information aggregation
OLS, and the order of trading becomes statistically significant for individual profits. Because these
alternative specifications assume independence across separate market sessions, ignoring the intra-
team correlation inherent in our multi-round, agent-based panel design, they naturally produce
smaller standard errors. We therefore interpret these differences as evidence that the affected
estimates are sensitive to the assumed correlation structure, rather than as a basis for stronger
causal claims.
An alternative method for addressing the issue of a small number of clusters would be to sig-
nificantly expand the array of LLMs employed, from 12 to more than 40. However, this approach
introduces two limitations. First, we intentionally selected models exclusively from the leading
frontier laboratories (Anthropic, Google, and OpenAI) alongside two capable open-weight models.
Expanding the baseline to a much larger quantity of models would have necessitated including pe-
ripheral, lower-tier agents. Had we done so, any observed breakdown in information aggregation
could be easily dismissed as a failure to exclude less competent LLMs. By restricting our sample
strictly to established models, we ensure that failures in information aggregation represent genuine
limitations of frontier models. Second, expanding the sample to over 40 teams would cause the num-
ber of simulated markets to jump from 3,500 to more than 12,000. This scaling would significantly
increase computational overhead and compromise our ability to perform rigorous manual auditing.
Finally, we deliberately refrain from estimating pooled regressions that combine the January
and April cohorts. While pooling would ostensibly increase statistical power, doing so requires
controlling for baseline model capabilities across generations. However, traditional standardized
benchmark indices that comprise the Artificial Intelligence Index (e.g., MMLU, HumanEval) fail to
maintain reliable cross-generational consistency between early-2025 and mid-2026 models. Because
these static benchmarks are non-stationary, using them to construct a unified intelligence metric
across differing vintages would introduce substantial measurement error. By restricting our analysis
to cohort-specific distributions and matched relative performance tests, we ensure our findings
remain robust to the rapid deprecation of static AI benchmarks.
6 Results
We first report our results from the first wave (1772 markets), for information aggregation (Section
6.1), and trading volume and profits (Section 6.2), ignoring the information provision treatment. In
Section 6.3, we describe the information provision treatment, using the full sample of 3500 markets.
It turns out that most of our results are robust when running the same regressions in the full sample.
The graphs that we show use the full sample. In Section 6.4, we examine how AI agents use the
public and private comments, whereas in Section 6.5 we conduct a robustness check with the three
frontier models from April 2026.
21

6.1 Information Aggregation
We present our main results for information aggregation in Table 5. Column (1) presents an OLS
regression where the dependent variable is log error (the logarithmic scoring rule error). Because
the log error has a wide range (from 0 to 34.5), the mean estimator is highly sensitive to outliers,
when markets crash by pricing the securityXat 0 when its true value is 1.17 Columns (2) and
(3) present Quantile Regressions that allow us to inspect specific parts of the error distribution.
Column (2) estimates the model at the median (τ= 0.5), representing the typical market outcome.
This estimator is robust to outliers, filtering out the effect of crashes to reveal how the typical agent
behaves under varying conditions. Column (3) estimates the model at the 80th percentile (τ= 0.8),
representing the tail risk.
We employ a mixed-contrast coding specification across all three models. For the primary design
variables, Structure and Market Duration, we use treatment contrasts, setting the easiest structure
(t3s111y2) and the shortest duration (3 Rounds) as the reference baseline. Consequently, coefficients
for these variables represent the marginal penalty of increasing complexity or duration relative to
this baseline. For the other conditions, Initial Log Error, Strategic, and Comments, we employ sum
contrasts (deviation from the mean). In this specification, coefficients represent the deviation of a
specific condition (e.g., Medium Initial Error) from the global average of that variable, rather than
from an arbitrary reference group. Thus, the model intercept captures the predicted log-error of
the baseline market design (Easy Structure, Short Duration) under average starting conditions for
the sum-contrast variables, evaluated at zero group intelligence; predictions for the average baseline
market are obtained by adding the intelligence terms at their sample means.18
In our OLS specification, we observe that as the structure becomes highly difficult, the average
log error increases. The intercept (7.548) is evaluated at zero group intelligence, which lies out-
side the observed range (7 to 46), and should not be read directly as the average Easy baseline.
Evaluated at the sample mean intelligence (23.6), the predicted baseline log error is approximately
2.5, consistent with the raw Easy three-round cell in Supplementary Appendix Table SA.10: even
the average Easy market exhibits noticeable mispricing, driven by a small number of crashed mar-
kets. Using this baseline, the Medium structure shows no statistically significant increase in error
(β= 2.200, p >0.1). While the Hard (β= 5.327, p <0.05) and Very Hard (β= 6.658, p <0.05)
structures generate large increases in log error relative to the baseline, post-estimation Wald tests
using CR2 small-sample adjustments reveal that the means of the adjacent structures are statis-
tically indistinguishable. Accounting for finite-cluster penalties, we fail to reject the equality of
coefficients between Medium and Hard (F1,11 = 0.62, p= 0.448), as well as between Hard and Very
Hard (F1,11 = 0.095, p= 0.764).
This extreme variance suggests that the mean effect is driven by crash markets rather than a
uniform shift in behavior. To disentangle typical market behavior from these outliers, we analyze
the median(τ= 0.5). The intercept of the median regression (≈0.018; the intelligence terms are
negligible at the median, so the zero-intelligence evaluation is immaterial here) implies that the
typical baseline market converges close to the truth (implied probability≈98%). The Medium
17Recall that the log error between actual (y) and predicted (p) is−(yln(p) + (1−y) ln(1−p)), where the predicted
probability is bounded,p∈[ϵ,1−ϵ],ϵ= 10 −15, to avoid having an infinite log error.
18An alternative specification would be to have the Squared Error as the dependent variable, instead of the Log
Error. However, because our prediction market uses the logarithmic scoring rule, AI agents try to minimise Log Error
to maximise their profits, hence the Log Error seems more appropriate. The disadvantage of this approach is the
sensitivity of the mean estimator to outliers, hence we also employ the two quantile regressions.
22

Table 5: Information Aggregation Without Disclosure
Dependent variable:
Log Error
Mean (OLS) Median (Q50) Tail Risk (Q80)
(1) (2) (3)
Constant 7.548 ∗∗∗ (2.185) 0.018 (0.019) 3.170 ∗∗ (1.138)
Comments Allowed−0.191 (0.319)−0.001 (0.003)−0.000 (0.032)
Duration: 6 Rounds−1.817 (1.172)−0.001 (0.005)−0.057 (0.177)
Duration: 9 Rounds−0.627 (1.250)−0.001 (0.005)−0.028 (0.165)
Strategic Prompt 0.053 (0.292) 0.001 (0.003) 0.000 (0.113)
Medium (t3s110) 2.200 (2.635)−0.000 (0.003) 0.038 (1.808)
Hard (t3s111) 5.327 ∗ (2.317) 0.286 ∗∗ (0.106) 12.470 . (7.451)
Very Hard (t3s111o2ye2) 6.658 ∗ (2.974) 0.700 ∗∗∗ (0.084) 21.771 ∗∗∗ (4.744)
Initial Error: Low 0.014 (0.120) 0.000 (0.004) 0.000 (0.069)
Initial Error: Medium 0.225 (0.186)−0.000 (0.003)−0.000 (0.063)
Average Intelligence−0.221 ∗∗∗ (0.059)−0.0004 (0.0004)−0.069 ∗∗ (0.025)
Intelligence SD 0.044 (0.227)−0.0003 (0.0003)−0.052 ∗ (0.026)
6 Rounds x Strategic−0.067 (0.261)−0.001 (0.004) 0.000 (0.128)
9 Rounds x Strategic 0.076 (0.385)−0.001 (0.004) 0.028 (0.161)
Medium Struct x Initial Error (Low) 1.309 (1.279)−0.000 (0.005) 0.019 (3.595)
Hard Struct x Initial Error (Low) 0.504 (0.682) 0.032 (0.124) 19.889 (12.267)
Very Hard x Initial Error (Low) 2.861 . (1.623) 0.013 (0.167) 10.425 ∗ (5.186)
Medium Struct x Initial Error (Medium)−0.725 . (0.436) 0.000 (0.004) 0.019 (1.810)
Hard Struct x Initial Error (Medium)−0.236 (0.715) 0.077 (0.149)−9.945 (12.141)
Very Hard x Initial Error (Medium)−0.337 (1.021)−0.007 (0.083) 10.080 (9.342)
Observations 1,772 1,772 1,772
R2 0.115
Notes: .p<0.1; ∗p<0.05; ∗∗p<0.01; ∗∗∗p<0.001. Q50 and Q80 are quantile regressions. Q50 models
the median log error, whereas Q80 models the upper 20% tail of the log error distribution (the worst-
performing markets). OLS model uses CR2 cluster-robust standard errors clustered by exact AI team
composition, featuring small-sample degrees of freedom adjustments. Quantile models report standard
bootstrapped standard errors due to small-cluster convergence constraints. All three models use a
mixed-contrast specification. Rounds and Structure use treatment contrasts with Round 3 and Struc-
ture t3s111y2 as baselines. All other controls (Initial Error, Strategic, Comments) use sum contrasts,
where coefficients represent deviations from the grand mean.
23

structure performs similarly well. However, at the Hard structure, typical success drops (implied
probability≈75%, p <0.01). At the Very Hard structure, the median error penalty expands to
0.700 (p <0.001), dropping the implied probability to≈50%. While linear restrictions confirm
that the mean effects are statistically indistinguishable due to extreme variance, bootstrapped Wald
tests on the median distributions confirm the strict tiered deterioration. The median deterioration
from Medium to Hard is highly significant (χ2 = 7.26, p= 0.007), as is the subsequent deterioration
from Hard to Very Hard (χ2 = 9.58, p= 0.002). Thus, while the Very Hard structure produces
extreme errors in the average market, it causes the typical market to be no better than a coin toss.
In summary, we reject the hypothesis that information aggregates across all market structures.
Figure 1 shows the mean and median log errors across the four structures.
Result1.Information aggregation deteriorates strictly at higher levels of complexity. While extreme
outliers obscure the mean effects, the typical (median) market follows a tiered deterioration: Easy
≈Medium < Hard < Very Hard.
This failure threshold can be benchmarked against the experimental evidence on the depth of
interactivereasoninginhumans. TheVeryHardstructureisaversionofthedirtyfacespuzzle, whose
laboratory analogue is studied by Weber (2001). He finds that although almost all subjects behave
consistently with the theoretical prediction in the simplest case, compliance declines considerably
as more steps of iterated rationality are required, in line with earlier evidence that subjects rarely
perform more than two steps. Using ring games that identify orders of rationality directly, Kneeland
(2015) estimates that 93% of subjects are rational, but only 44% are third-order and 22% fourth-
order rational. The level-k and cognitive hierarchy literatures reach a similar conclusion, placing
the typical depth of human strategic reasoning at one to two levels (Nagel, 1995; Costa-Gomes and
Crawford, 2006; Camerer et al., 2004). Read against this benchmark, the tiered deterioration of
Result 1 mirrors this human pattern: the median market aggregates information when each trader
needs to reason only about his own signal, or about the signal of only one other trader, but breaks
down when he needs to reason about the two signals of two other agents, hence requiring more than
two levels of interactive reasoning. In this respect, AI agents do not appear to relax the cognitive
constraint that limits interactive reasoning in human experiments.
While Figure 1 demonstrates the magnitude of the final aggregation error, Figure 2 illustrates
the dynamic mechanism behind this failure. By plotting the empirical price paths against the the-
oretical myopic equilibrium derived in Section 3.2, we observe a clear divergence from the myopic
benchmark. In the Easy and Medium structures, the High-Intelligence agents tightly track the my-
opically optimal prices. However, in the Hard and Very Hard structures, this tracking deteriorates.
Rather than following the theoretical price to 1 or 0, the smartest agents anchor their prices near 0.5,
a trajectory consistent with difficulty in higher-order reasoning. Conversely, the Low-Intelligence
(red) agents have a similar price trajectory that converges to 0.75 in both Hard and Very Hard,
even though the true value is 1 in the former and 0 in the latter. This suggests that any apparent
‘success’ in complex structures reflects noisy trading rather than sophisticated interactive reasoning.
Our results confirm the hypothesis that neither communication nor strategic prompting signif-
icantly influences information aggregation. The main effect of Comments Allowed is statistically
insignificant in the OLS model (β=−0.191, p >0.47), as well as in the median and tail-risk quantile
regressions. Similarly, the Strategic Prompt coefficient is statistically indistinguishable from zero
(β= 0.053, p >0.8). This lack of significance holds even when controlling for interaction effects
with duration, suggesting that the core aggregation mechanism is robust to these variations.
24

Median = 100% Median = 100% Median = 75% Median = 50%
0
5
10
15
Easy (Baseline) Medium Hard Very Hard
Estimated Increase in Mean Log Error (vs. Easy)
OLS and Q50 coefficients (relative to Easy)
Effect of Information Structure on Information Aggregation
Figure 1:The Complexity Effect.Point estimates and 95% CR2 confidence intervals represent
the OLS mean marginal effect of the structure. Text labels indicate the Q50 median marginal
effects, displayed as implied probabilities (p=e-log error).
Hard Very Hard
Easy Medium
1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
Trading Round
Price of YES Shares
Benchmark Theoretical Myopic Price
AI Group Intelligence High Intelligence Medium Intelligence Low Intelligence
Empirical vs. Theoretical Prices
Figure 2:Myopically Optimal and Actual Prices Across Structures.Smarter markets
tightly track the myopically optimal prices in the Easy and Medium structures, but revert to 0.5 in
the Hard and Very Hard. Low-intelligence markets perform better in the Hard structure but this
seems more an artifact of noisy trading rather than sophisticated interactive reasoning.
25

Result 2.Information aggregation is unaffected by prompting AI agents to be strategic or myopic.
Result 3.Information aggregation is unaffected by allowing AI agents to post public comments.
Communication and strategic prompting may fail to influence information aggregation for at
least two reasons. The first is that highly sophisticated AI agents behave according to the theoretical
predictions. The second is that they are not very sophisticated, so they fail to understand the
prompt, or they cannot plan ahead and implement a strategic plan. To understand their thought
process better, we conduct a text analysis of their public comments and private justifications in
Section 6.4.
The initial log error is the log error between the initial price and the true value ofX. The
low initial log error is when the initial price is 0.7 and the true value ofXis 1, or the initial
price is 0.3 and the true value is 0, whereas the medium initial log error is when the initial price
is 0.5. We observe no significant main effect of the low initial log error on market performance
(β= 0.01, p >0.9), and similarly for the medium initial log error. This suggests that under average
conditions, information aggregation is not strongly related to the initial price.
This average result does not hold in the most complex environment. The interaction between the
Very Hard structure and the low initial log error (Very Hard×Initial Error (Low)) generates a large,
positive, and statistically significant coefficient in both the OLS mean regression (β= 2.86, p <0.1)
and the 80th percentile tail regression (β= 10.42, p <0.05). This positive coefficient indicates
that, in the most complex environment, markets that begin with a more accurate price signal (lower
initial error) end with worse performance than those starting with higher error. The magnitude
of this effect in the tail model (β= 10.42) is very high, suggesting that for fragile markets, a low
initial error does not act as an anchor for truth. This effect is absent in the median regression
(β= 0.01, p >0.9), suggesting that the ‘typical’ market ignores the initial price, which is consistent
with the theory. It is interesting to note that, when human participants are ambiguity averse,
Galanis et al. (2024) show theoretically and experimentally that the initial price can also degrade
information aggregation.
Result 4.On average, information aggregation is unaffected by manipulating the initial price of
the market, but the initial price matters in the Very Hard structure.
Our results support the hypothesis that information aggregation does not deteriorate when
the number of rounds increases, which is consistent with the theory. Furthermore, the quantile
regressions (Models 2 and 3) show no effect of duration on the median or 80th percentile.
Result 5.Information aggregation is unaffected by the duration of the market.
Our analysis strongly supports the hypothesis that average intelligence improves information
aggregation(Figure3). IntheOLSspecification, AverageIntelligenceisahighlysignificantpredictor
of market success (β=−0.221, p <0.001), with smarter teams achieving consistently lower log
errors. This means that an increase from the lower intelligence scores (7) teams to the highest (46)
reducesthelogarithmicerrorpenaltyby8.6points. Becauselogarithmicscoringscalesexponentially,
an 8.6 reduction in error implies that the smartest agents assign a probability to the true outcome
that is roughlye 8.6 (over 5,000 times) larger than the probability assigned by the least intelligent
agents. Part of this multiplier is mechanical, reflecting the exponential scale of the logarithmic error;
the more informative reading is that intelligence acts primarily as a safeguard against extreme
26

0
10
20
30
10 20 30 40
Average Intelligence of Agents
Final Logarithmic Score
Trend Type Average (OLS) Median (Quantile)
Mean (Red) vs. Median (Green) Log Error Trends
Figure 3:The Intelligence Effect.As the AI agents become smarter, information aggregation
(mean log error) improves, but the median log error is unaffected. Points are jittered horizontally
to show density of markets with the same intelligence.
mispricing, preventing low-intelligence agents from confidently driving the security price in the
opposite direction.
Figure 4 maps how AI agents, grouped in three intelligence tiers, discover the true value of the
security. The probability of the true state is the price of Yes if the answer is Yes and the price
of No if the answer is No. The High Intelligence cohort (green line) exhibits rapid informational
efficiency, sharply converging toward the true state and subsequently stabilizing. In contrast, the
Low Intelligence cohort (red line) exhibits a ‘sawtooth’ trajectory, indicating noisy, inefficient belief
updating.
While higher intelligence improves performance on average, the quantile regressions reveal that
this is driven primarily by tail risk mitigation rather than universal optimisation. We find no
significant effect of intelligence on the median market(β≈0, p >0.5), suggesting that typi-
cal markets reach an accuracy ceiling regardless of marginal gains in cognition. However, intelli-
gence plays a critical role in the tail of the distribution (Q80), where it significantly reduces error
(β=−0.069, p <0.01). This implies that average intelligence acts as a form of crash protection:
improving the bottom markets rather than the median. The Intelligence SD (Standard Devia-
tion) measures whether increasing the diversity of the group improves information aggregation.
We found an effect only in the tail of the distribution (Q80), where it significantly reduces error
(β=−0.052, p <0.05).
Result 6.Information aggregation improves as the average intelligence increases.
27

6.2 Trading Volume and Profits
In Table 6, we report two regressions, on trading volume and individual profits, using the same
independent variables as in the previous models on information aggregation. We first find that
trading volume across structures broadly aligns with myopic theoretical predictions, though with
notable statistical caveats. First, while point estimates suggest volume increases from the Easy
baseline to the Very Hard structure, this difference is completely statistically insignificant (p>0.1).
Second, both the Hard and Medium structures generate marginally significantly more volume than
the Easy baseline (p<0.1). Consistent with Hypothesis 8, a post-estimation Wald test using the
CR2 cluster-robust variance-covariance matrix fails to reject equality between the Hard and Medium
coefficients (p= 0.332), indicating that trading volume between the Hard and Medium structures
is statistically indistinguishable. The Very Hard coefficient is too imprecisely estimated to be
statistically distinguished from either the Easy baseline or the Hard and Medium structures, so the
placement of Very Hard in the ordering below reflects point estimates rather than pairwise tests.
Result 7.Trading volume is ordered, from lowest to highest, as follows: Easy≈Very Hard < Hard
≈Medium.
Second, we reject Hypothesis 9 that individual profits are positive. The average realized profit
per trader is−46, and the covariate-adjusted position-specific estimates reported below are signif-
icantly negative for the first two trading positions, so that on average, participation in the market
generates financial losses. See Figure SA.5 for a breakdown of profits by AI model, where the only
model with positive profits is Gemini 3 Flash. However, an analysis of the trading sequence reveals
a clear pattern by trading position. At first glance, the coefficients for trading second or third
appear statistically indistinguishable from the baseline first-mover (p >0.1). Yet, the point esti-
mates diverge: trading second carries a−42.1penalty, while trading third yields a77.4premium. A
post-estimation Wald test, using CR2 errors clustered at the unique market level (the level at which
the three competing positions are correlated; see the note to Figure SA.2), rejects equality between
the second and third trading positions (p <0.001). Under the more conservative team-composition
clustering with small-sample corrections, the position-level losses reported below remain significant
(trader 1:p≈0.01; trader 2:p <0.001), while the second-versus-third contrast weakens to marginal
significance (p= 0.076); the late-mover advantage is therefore robust in sign and magnitude, but its
statistical significance depends on the assumed correlation structure, consistent with our discussion
in Section 5.1.
To test our theoretical prediction that all market participants should generate weakly positive
profits, we calculated the estimated marginal means for profit across all three trading positions.
Applying one-sided tests using the market-level CR2 variance-covariance matrix (Ha: Profit<0),
we reject the theoretical baseline for agents who trade first and second. The first mover generates a
highly significant loss (Estimated Profit=−57.7, p <0.001), as does the second mover (Estimated
Profit=−99.8, p <0.001). The third trader is the only participant to extract positive value from
the market (Estimated Profit= 19.7). See Figure SA.2 for an illustration.
Result 8.Market participation generates losses for the first two traders and profits for the third.
Trading third yields a significant financial advantage over trading second.
We also reject Hypothesis 10 that average profits are uncorrelated with the difficulty of the
structure. AsshowninTable6, thenegativecoefficientobservedintheMedium(β=−30.5, p >0.1)
treatment is not statistically significant relative to the Easy baseline. However, as complexity
28

increases further, profits decline. Post-estimation Wald tests using the market-level CR2 matrix
reject equality between the Medium and Hard structures (p <0.001), as well as between the
Hard and Very Hard structures (p= 0.015). This suggests that once complexity crosses a certain
threshold, average profits decrease. This is theoretically consistent with Result 1: worse information
aggregation equates to an increasing divergence between the final market price and the true value
of the security, mechanically resulting in lower average profits.
Result 9.Individual profits decrease as the structure becomes more complex: Easy≈Medium >
Hard > Very Hard.
3−Round Markets 6−Round Markets 9−Round Markets
1 2 3 1 2 3 4 5 6 1 2 3 4 5 6 7 8 9
0%
25%
50%
75%
100%
Trading Round
Probability of True State
Group Intelligence High Intelligence Medium Intelligence Low Intelligence
Tracking the average price assigned to the TRUE outcome over time
Price Discovery Trajectory by Intelligence Tier
Figure 4:The Price Discovery Trajectory.The vertical axis is the market price of the security
that pays 1 in the realized state, and the horizontal axis is the trading round. The three panels
correspond to 3-, 6-, and 9-round markets. Lines group markets by team intelligence cohort; higher-
intelligence teams are closer to the true value across horizons.
The analysis of individual agent profitability (Table 6, Column 2) reveals that financial success
in these markets is primarily driven by relative rather than absolute cognitive advantage. We
find a strong positive effect of individual intelligence on profit (β= 14.08, p <0.001), coupled
with a nearly equal and opposite negative effect from the average intelligence of the market (β=
−11.02, p <0.001). This confirms Hypothesis 7 that agents benefit significantly from their own
cognitive capacity, but suffer from the intelligence of their competitors.
Result 10.Individual profitability is driven by relative cognitive advantage: an agent’s profits
increase with their own intelligence, but decrease as the average intelligence of their competitors
rises.
6.3 Information Provision
To test Hypotheses 11 and 12, we introduce an information provision treatment (e.g., Berg et al.
(1995), Cai et al. (2009)). Specifically, we use the empirical results from our initial baseline sample
(1,772 markets) to construct a disclosure prompt. This summary information is then provided to
an independent, non-overlapping later-wave sample of 1,728 new markets. By pooling the baseline
29

Table 6: Trading Volume and Profits Without Disclosure
Dependent variable:
Trading Volume Individual Profits
(1) (2)
Constant 1,795.988 . (1,064.073)−80.719 ∗ (31.683)
Comments Allowed 85.077 ∗ (42.516) 2.723 (4.048)
Duration: 6 Rounds 543.398 ∗∗∗ (108.871) 2.447 (20.007)
Duration: 9 Rounds 1,037.835 ∗∗∗ (192.429)−5.396 (17.292)
Strategic Prompt−65.396 . (36.642)−0.491 (2.876)
Medium (t3s110) 308.391 . (174.854)−30.548 (33.429)
Hard (t3s111) 128.183 . (74.893)−69.955 ∗ (32.035)
Very Hard (t3s111o2ye2) 55.372 (266.568)−98.904 ∗ (42.381)
Initial Error: Low−180.641 ∗∗ (68.906)−10.767 ∗∗ (3.809)
Initial Error: Medium−14.704 (34.607)−4.386 (2.691)
Average Intelligence−27.925 (24.667)−11.019 ∗∗∗ (2.252)
Individual Intelligence 14.079 ∗∗∗ (2.150)
Intelligence SD 22.347 (41.617) 0.606 (2.473)
Trades Second−42.127 (28.229)
Trades Third 77.390 (55.932)
6 Rounds x Strategic 9.810 (55.547)−1.725 (4.474)
9 Rounds x Strategic 87.983 (62.172)−3.680 (4.496)
Medium Struct x Initial Error (Low) 273.357 . (158.440)−21.173 (19.587)
Hard Struct x Initial Error (Low) 87.880 (70.669)−13.015 (10.054)
Very Hard x Initial Error (Low) 414.759 (264.776)−32.672 (23.473)
Medium Struct x Initial Error (Med) 41.568 (67.534) 4.394 (4.099)
Hard Struct x Initial Error (Med) 62.984 (55.047) 11.491 (8.982)
Very Hard x Initial Error (Med)−238.720 (401.800)−1.778 (11.232)
Observations 1,772 5,316
R2 0.104 0.060
Notes: .p<0.1; ∗p<0.05; ∗∗p<0.01; ∗∗∗p<0.001. Column 1 is a market-level regression where the depen-
dent variable is total trading volume, measured as the absolute quantity of shares traded in the market.
Column 2 is a trader-level regression where the dependent variable is the trader’s realized LMSR profit.
Both models use CR2 cluster-robust standard errors clustered by exact AI team composition, featuring
small-sample degrees of freedom adjustments. Rounds, Information Structure, and Trader Position
(Model 2 only) use treatment contrasts, with ‘Round 3’, ‘t3s111y2’ (Easy), and ‘Trades First’ serving
as their respective baselines. All other controls (Initial Error, Strategic, Comments) use sum contrasts,
where coefficients represent deviations from the grand mean.
30

and treatment samples, we estimate the association between this disclosure prompt and market
outcomes using a treatment indicator.
Sequential later-wave comparisons can be confounded by secular model or platform changes,
prompt-context changes, or other implementation differences. We reduce this concern by using
identical, version-pinned LLM models across both the baseline and treatment samples via a state-
less API, so the models have no endogenous memory of the baseline markets. Nevertheless, because
the disclosure was not randomized within a single contemporaneous wave, we interpret the esti-
mates as later-wave disclosure associations rather than as strictly equivalent to within-wave random
assignment.
In Supplementary Appendix SA.4 we report the Experiment Disclosure prompt, which was
dynamically generated based on which model was trading. Supplementary Appendix Table SA.6
presents the mixed-contrast regression models for information aggregation across the full, pooled
sample of 3,500 markets, introducing a dummy variable for the Experiment Disclosure treatment.
We find no support for Hypothesis 11. The provision of historical market data yields no statistically
significant improvement in market accuracy across the mean (β= 2.075, p >0.1), the median
(β=−0.00004, p >0.1), or the tail-risk distributions. Furthermore, the interaction term between
Disclosure and Average Intelligence is null. Within the limits of this later-wave comparison, even the
most highly capable LLMs in our sample did not detectably improve their probability estimations
in response to the explicit strategic feedback.
Result 11.Information provision has a null effect on information aggregation.
Supplementary Appendix Table SA.7 replicates this analysis for market activity and individual
profitability. Consistent with Hypothesis 12, the disclosure treatment has no statistically observable
impact on either trading volume (β= 171.9, p >0.1) or individual profits (β=−21.05, p >0.1).
Providing all participants with the exact same strategic heuristics did not generate a measurable
advantage for any individual trader.
Result 12.Information provision has a null effect on individual profits.
Finally, analyzing the pooled sample of 3,500 markets confirms that all primary findings from
the first wave of experiments are highly robust. The baseline market mechanics remain unchanged:
strategic prompting, communication, initial price, and market duration have no significant impact
on information aggregation. Conversely, the structural complexity of the market continues to sig-
nificantly hinder aggregation, while higher average intelligence strictly improves it.
6.4 Public and Private Comments
Our finding that strategic prompting does not influence information aggregation is consistent with
our theoretical prediction that being myopic or strategic does not have an impact. However, this
null result may also be driven by the inability of LLMs to execute dynamic plans (Kambhampati
et al., 2024). In our experiment, a strategic agent could coordinate an inter-temporal plan by leaving
instructions for its future self in the private comments. Alternatively, he could manipulate com-
petitors by deceiving them in public comments, either by lying outright or by hoarding information
(revealing less in public than in private).
To investigate these behavioral mechanics, we construct three measures of communication strat-
egy. First, we compute thecosine similaritybetween an agent’s private and public messages, a
31

standard natural language processing metric for semantic alignment ranging from 0 (divergent) to
1 (identical) (Manning and Schutze, 1999).19
Second, we measureinformation hoardingvia the word gap (the number of words in the
private minus the public message). In markets where public messages are allowed, private messages
average 83.5 words while public messages average only 40; private messages are longer on average
in 99% of markets, and strictly longer in 94% of individual messages (Figure SA.3).
Finally, we measure explicitdeception. Using an LLM-as-a-judge methodology, we task our
most capable model in the first wave, Gemini 3 Flash, with evaluating, in every round of every
comments-allowed market, whether the public comment truthfully reveals the agent’s private signal
(Truthful Revelation), avoids disclosing the signal (Information Withholding), or states the opposite
of the true signal (Lying).20 We estimate an ordered logit model across these three hierarchical
categories, where positive coefficients indicate a shift toward withholding or lying.
Table 7 presents the pooled models for cosine similarity (OLS, Column 1), information hoarding
(OLS,Column2), anddeception(OrderedLogit, Column3). Thestrategicprompthasastatistically
insignificant effect on cosine similarity and only marginally increases information hoarding by less
than one word (β= 0.788, p <0.1). In the Supplementary Appendix Tables SA.3, SA.4, and
SA.5, we report the same regressions when splitting the sample by market duration (3, 6, and 9
rounds). We find that even this weak, marginal effect on the word gap fails to survive consistently
when splitting the sample by market duration; it retains the same sign in all three subsamples but
it is statistically significant only in the 9-round markets. Thus, we do not find robust evidence
that the strategic prompt changes the communication metrics, and the design cannot distinguish
whether agents are unable or unwilling to implement more complex deceptive strategies. Individual
intelligence similarly provides mixed results, correlating with less explicit lying but marginally more
information hoarding. Moreover, information hoarding and deception increase as the structure
becomes more complex.
The Experiment Disclosure treatment does, however, change communication behavior. Disclos-
ing the past history widens the gap between private and public messages (14.8words, p<0.001) and
increases deception (0.86,p <0.001). Recall that one of the qualitative results we disclosed was
that public comments have no effect on information aggregation.
Finally, by modelling the current round as a categorical variable, the regression uncovers a
pattern which is consistent with end-of-horizon disclosure, but also with simpler round-number
heuristics. Rather than exhibiting a simple linear decay in deception and information hoarding over
time, there is a “sawtooth” pattern. Agents are most deceptive and guarded in Round 1. However,
the probability of truthful revelation increases significantly, indicated by large negative coefficients,
at Rounds 3, 6, and 9 (p < 0.001). These increases coincide with the scheduled final rounds of the
short, medium, and long market treatments. In the intervening rounds (e.g., Rounds 4, 5, and 7),
concealment rates rise back toward the Round 1 baseline. This suggests that AI agents understand
that in the final round revealing the truth will not have an adverse effect on their profits.
Because the trading order is fixed, this pattern admits a sharper test. Each trader has hisown
final trading opportunity, and these differ by position: in a six-round market, trader 1 trades for
the last time in Round 4 and trader 2 in Round 5; in a nine-round market, in Rounds 7 and 8
19Each text is transformed into a vector, where a dimension is a unique word and its value is the number of times
it appears in the text. The cosine of the angle between the two vectors measures the lexical overlap between the two
texts, a standard proxy for their semantic similarity, ranging from 0 (very different) to 1 (very similar).
20Note that for structure t3s111o2ye2 we asked twice, as there are two signals for each trader.
32

respectively. Once a trader has no further trades, revealing his private signal cannot reduce his
profits, irrespective of what he knows or believes about the other signals: his LMSR payoff depends
only on his existing holdings and the realised outcome. A trader who reasons about his own horizon
should therefore reveal at his final move, whatever his position. This prediction fails for traders 1
and 2. In the deception models split by duration (Table SA.5), the revelation response at trader 1’s
final move is weak (Round 4:−0.278in six-round markets) or statistically null (Round 7:−0.183
in nine-round markets), and null at trader 2’s (Round 5:−0.145; Round 8:−0.062). By contrast,
Round 6 spikes strongly (−0.615,p <0.001) even in nine-round markets, where it is terminal for
nobody: the trader acting in Round 6 trades again in Round 9, so protecting his information rents
dictates concealment there. Revelation thus tracks the salient round numbers 3, 6, and 9, which
are the possible market durations stated in the prompt, rather than any trader’s actual horizon,
individual or aggregate.21 Agents behave as if rounds that are multiples of three could be terminal,
even when the horizon is known to be nine rounds, and fail to exploit the costless revelation available
at their own final moves, which provides evidence against backward induction over their individual
trading horizons.
6.5 Robustness with Frontier AI Models
The rapid pace of innovation in AI is evidenced by the frequent release of new models every few
months. To test whether the failure of information aggregation in complex environments (Result
1) is a transient artifact of older AI capabilities, we conducted in April 2026 an out-of-sample
robustness check using a cohort of frontier LLMs. This subsample comprises 576 markets played
across all four structures (Easy, Medium, Hard, and Very Hard). We employ four distinct teams:
three homogeneous markets populated by GPT-5.4, Claude Opus 4.6, and Gemini 3.1 Pro, and a
heterogeneous team containing one agent of each model. Rather than comparing average log errors
across the two cohorts, which is sensitive to the small number of markets that crash, we describe
both cohorts by classifying each market according to how close to the truth its final price ends up.
We define four mutually exclusive and exhaustive categories, using the final pricepand the true
valuevof the security. A marketaggregatesif|p−v|<0.1, it isconfidently wrongif|p−v|>0.9,
ithedgesif|p−v|lies within 0.1 of 0.5, and it ispartialotherwise. 22 We report three groups of
markets: all twelve teams of the first wave, the foursmartestteams of the first wave, ranked by the
average Artificial Analysis intelligence index accessed in January 2026, and the four frontier teams
of April 2026.23 Table SA.9 reports the shares and Figure 5 displays them.24
21Rounds 3, 6, and 9 are always trader 3’s turns, so a round-number heuristic cannot be fully separated from
behavior specific to the third trading position. The distinction is immaterial for our conclusion: under either inter-
pretation, no trader conditions his revelation on his own remaining trading opportunities, which is the hallmark of
backward induction. The failure of traders 1 and 2 to reveal at their own final moves is identified from their own
turns and is unaffected by this equivalence.
22In the Very Hard structure, tightening the tolerance to 0.05 gives aggregation shares of 17.3%, 20.8% and 15.3%
for the three groups below, and loosening it to 0.2 gives 19.6%, 25.0% and 17.4%, against 18.7%, 22.2% and 16.7%
at the tolerance we use, so the difference is small.
23These are: 3x Gemini 3 Flash, 3x GPT-5 mini, the mixed team of Claude Haiku 4.5, Gemini 3 Flash and GPT-5
mini, and 3x Claude Haiku 4.5, with index values of 46, 41, 39 and 30, as shown in Table 1. The index is used only
within the first wave and only at that single access date, since the scores of the April models were accessed later and
are not comparable. Selecting instead the four teams with the lowest realized mean log error gives 19.4% of markets
aggregating in the Very Hard structure, so the picture does not depend on the selection rule.
24Figures SA.6 and SA.7 in the Supplementary Appendix report the mean squared error by structure for each team
of the two cohorts.
33

Table 7: Agent Communication Strategy: Text Similarity, Word Gap, and Deception
Dependent variable:
Cosine Similarity (OLS) Word Gap (OLS) Deception (Ordered Logit)
(1) (2) (3)
Constant 0.324 ∗∗∗ (0.043) 33.880 ∗ (15.423)
Strategic Prompt−0.003 (0.002) 0.788 . (0.416) 0.006 (0.036)
Round 2 0.030 ∗ (0.014)−13.194 . (7.874)−0.398 ∗∗∗ (0.074)
Round 3 0.004 (0.013)−25.105 ∗ (9.969)−0.665 ∗∗∗ (0.076)
Round 4 0.030 ∗ (0.012)−12.247 ∗∗ (3.723)−0.205 ∗∗ (0.079)
Round 5 0.040 ∗∗ (0.015)−23.619 ∗∗ (7.966)−0.160 . (0.082)
Round 6 0.005 (0.016)−30.972 ∗∗ (9.860)−0.560 ∗∗∗ (0.091)
Round 7 0.038 . (0.020)−18.893 ∗∗∗ (5.068)−0.201 ∗ (0.101)
Round 8 0.047 ∗∗ (0.015)−26.708 ∗∗ (8.346)−0.081 (0.099)
Round 9 0.033 . (0.019)−32.644 ∗∗∗ (9.907)−0.487 ∗∗∗ (0.112)
Duration: 6 Rounds 0.002 (0.005)−0.468 (0.906)−0.036 (0.093)
Duration: 9 Rounds−0.002 (0.005)−1.072 (0.866)−0.017 (0.094)
Medium (t3s110)−0.022 ∗∗ (0.007)−1.213 (1.063) 1.198 ∗∗∗ (0.108)
Hard (t3s111) 0.002 (0.006) 2.417 ∗ (1.099) 0.907 ∗∗∗ (0.124)
Very Hard (t3s111o2ye2) 0.001 (0.008) 5.666 ∗∗∗ (1.423) 1.369 ∗∗∗ (0.103)
Experiment Disclosure 0.010 (0.018) 14.858 ∗∗∗ (3.174) 0.861 ∗∗∗ (0.074)
Initial Error 0.002 (0.012) 2.867 (2.227) 0.268 (0.208)
Individual Intelligence 0.001 (0.002) 0.844 . (0.484)−0.004 . (0.002)
Observations 10,620 10,620 13,189
R2 0.027 0.156
Notes: .p<0.1; ∗p<0.05; ∗∗p<0.01; ∗∗∗p<0.001. Column 1 reports cosine similarity between private
and public messages, ranging from 0 (semantically different) to 1 (identical). Column 2 reports the
word gap, defined as private-message word count minus public-message word count. Column 3 is an
ordered logit where the deception outcome is ordered Truthful Revelation<Information Withholding
<Lying, so positive coefficients indicate a shift toward withholding or lying. Column 3 has more
observations because the Very Hard structure contains two private signals per trader and is judged
separately for each signal. All models use a mixed-contrast specification. Treatment contrast baselines
are: Round 1 for Round, 3 Rounds for Duration, Easy (t3s111y2) for Structure, and No Disclosure for
Experiment Disclosure. The Strategic Prompt variable uses sum contrasts, representing the deviation
from the grand mean, whereas Initial Error is mean-centered. Columns 1 and 2 (OLS) report CR2
cluster-robust standard errors in parentheses, clustered by exact AI team composition with small-
sample degrees of freedom adjustments. Column 3 (Ordered Logit) reports CR1 cluster-robust standard
errors clustered at the market level to account for intra-market correlation across competing agents and
repeated communication rounds.
34

The frontier models are more capable in the first three structures than those of the first wave.
In the Easy structure the share of markets that aggregate rises from 68.5% to 80.6%, and no frontier
market is confidently wrong, against 5.8% in the first wave. In the Medium structure every one of
the 144 frontier markets aggregates, against 69.3%, and the 15.2% of first-wave markets that were
confidently wrong disappear entirely. The frontier cohort also outperforms the four smartest teams
of the first wave in the Easy, Medium and Hard structures, at 80.6% against 66.0%, 100% against
86.8%, and 51.4% against 43.8%.
In the Very Hard structure, however, the frontier group does not perform better. The share of
markets that aggregate is 18.7% for the first wave, 22.2% for its four smartest teams, and 16.7%
for the frontier cohort. What changes with capability is not the frequency of aggregation but the
composition of the failures. The share of markets that are confidently wrong falls from 30.3% to 9.0%
and 10.4%, while the share that hedge near 0.5 rises from 37.6% to 56.2% and 66.0%. Two thirds
of frontier markets in the hardest structure therefore end at a price that conveys no information
about the state, and the gain from capability consists of avoiding the confident mispricing of the
weaker models rather than of pricing the security correctly more often. Figure 6 makes the same
point in terms of the aggregation share alone: the three groups separate in the Easy and Medium
structures and get very close in the Very Hard structure.
January 2026, all teams January 2026, four smartest April 2026, frontier
Easy Medium Hard Very Hard Easy Medium Hard Very Hard Easy Medium Hard Very Hard
0%
25%
50%
75%
100%Share of markets
Aggregates Partial Hedges near 0.5 Confidently wrong
The share of markets that aggregate in the Very Hard structure does not rise
Capability replaces confident error with indecision
Figure 5:January vs. April Cohorts.Each market is classified by the distance between its final
price and the true value of the security. As capability rises, from all twelve teams of the first wave to
its four smartest teams and then to the frontier cohort, confidently wrong markets are replaced by
markets that hedge near 0.5, while the share of markets that aggregate in the Very Hard structure
does not rise.
Result 13.Capability replaces confident error with indecision rather than with information aggre-
gation. Moving from the first wave to its smartest teams and then to the frontier cohort, the share
of Very Hard markets that are confidently wrong falls from 30.3% to 9.0% and 10.4% and the share
that hedge near 0.5 rises from 37.6% to 56.2% and 66.0%, while the share that aggregate remains
35

0%
25%
50%
75%
100%
Easy Medium Hard Very Hard
Share of markets that aggregate
January 2026, all teams January 2026, four smartest April 2026, frontier
Capability buys the easier structures, not the hardest one
Figure 6:Aggregation by Structure and Group.The share of markets whose final price lies
within 0.1 of the true value of the security. The gain from capability is concentrated in the Easy
and Medium structures and disappears in the Very Hard structure.
36

between 16.7% and 22.2%. Two thirds of the frontier markets in the Very Hard structure end at a
price close to 0.5.
Read together with Result 1, this suggests that the deterioration we document is not an artifact
of the models available when the first wave was run. Capability gains are spent where the required
depthofinteractivereasoningislow, andwherethatdepthrisestheadditionalcapabilityshowsupas
a reluctance to move the price away from 0.5 rather than as an ability to infer the private information
of others from their orders. The market becomes less confidently wrong without becoming more
informative, which is a benign failure for a trader and an unhelpful one for anyone who reads prices
to learn about the state.
6.6 Statistical Power and Minimum Detectable Effects
Several of our central findings are null results: communication, strategic prompting, the initial
price, and market duration do not significantly improve information aggregation. Because a failure
to reject is informative only to the extent that the design could have detected an effect had one
been present, we compute the minimum detectable effect (MDE) for each treatment null by Monte
Carlo simulation operating through the exact CR2/Satterthwaite estimator used in our main spec-
ifications. On the mean, the design is well powered for communication and duration: it detects a
comments effect of0.83log-error units (about 7% of the outcome standard deviation) and duration
effects of roughly2.0units (about 17%), so these nulls are informative. For strategic prompting,
the joint MDE for the main effect and its duration interactions is1.09log-error units, so we can
rule out large strategic effects but not small ones, and the initial-price contrasts are not detectable
on the mean. The quantile specifications are better powered, because they are robust to the small
number of “crash” markets that dominate the sampling variance of the mean. In the Very Hard
structure the median MDE for strategic prompting is0.36against a baseline median log error of
0.69, so that null is informative and not an artifact of a floor; in the Hard structure the median
MDE (0.38) exceeds the baseline error (0.28), so the null is uninformative there and we make no
tail claims. Supplementary Appendix SA.2 reports the simulation design and the full set of MDEs,
by specification and by information structure.
7 Conclusion
Understanding whether AI agents can reason interactively and aggregate information is important
for several reasons. First, the informational efficiency of prices is a basic property of financial
markets, and AI agents are increasingly participating in them, as well as being deployed in firms.
Second, an essential ability of AI agents is to make predictions, hence it is natural to examine
whether this ability can be improved by making them trade in a prediction market. Finally, the
capacitytoreasonabouttheprivateinformationofothersbyobservingtheiractionsisafundamental
human quality. While it is tempting to anthropomorphize highly capable AI models and assume
they inherently possess these higher-order interactive reasoning skills, empirical evidence remains
scarce.
This paper provides experimental evidence on information aggregation and interactive reasoning
among autonomous AI agents within a prediction market framework. Consistent with economic the-
ory, we find little evidence that cheap talk communication, market duration, or strategic prompting
materially improve market accuracy; initial price has little average effect but matters in the Very
37

Hard structure. Markets perform worse in the harder information and payoff structures. While
the median AI team successfully solves the Easy and Medium structures, performance deteriorates
sharply in the Hard and Very Hard environments. This suggests that current LLMs do not yet
demonstrate the hyper-rational interactive reasoning capabilities often assumed in economic theory.
Instead, they exhibit interactive reasoning capabilities comparable to human subjects in similar
experiments.
Within our main sample, the intelligence index is positively associated with information aggre-
gation. A robustness check with a cohort of frontier models released in April 2026 shows that they
aggregate information more often than the first-wave models in the three easier structures, but not
in the Very Hard structure. There, higher capability raises the share of markets that hedge near 0.5
and lowers the share that are confidently wrong, without raising the share that aggregate (Result
13).
At the individual level, an agent’s profitability is more closely related to relative than absolute
cognitive advantage. Higher individual intelligence is associated with higher profits, while higher
average team intelligence is associated with lower individual profits. Furthermore, the order of
trading matters: traders who move third earn higher profits than those who move second, consistent
with a late-mover advantage in this design.
Our later-wave disclosure exercise also reveals limitations in how LLMs process feedback from
past play in this setting. Contrary to recent literature suggesting LLMs can self-improve via itera-
tive prompting, we find that providing agents with information about past play does not improve
market accuracy. In the message-based outcomes, the disclosure condition is associated with more
information hoarding and deceptive communication.
Finally, text analysis of the agents’ private and public messages shows that they struggle to
act strategically and show no sign of designing or executing a dynamic plan. They reveal more
information as the game approaches the end, indicating that they have some understanding about
itsdynamicnature. However, theyalsoexhibitasawtoothpatternofrevelationthatspikesinrounds
3, 6, and 9, which are always trader 3’s turns, even when the game ends in 9 rounds, whereas traders
1 and 2 do not reveal more when it is their last period. This suggests that their reasoning may rely
on token-matching heuristics instead of backward induction.
Ultimately, our findings suggest a nuanced frontier for trading with AI agents. While they
demonstrate competence in basic market mechanics and, within our main sample, perform better
when the team has a higher intelligence index, their difficulty with strategic communication and
multi-step interactive reasoning indicates a significant distance until they resemble the sophisticated
agents usually assumed in economic theory.
References
Artificial Analysis Team (2025). Artificial analysis long context reason-
ing benchmark. Available athttps://artificialanalysis.ai/evaluations/
artificial-analysis-long-context-reasoning.
Aumann, R. (1976). Agreeing to disagree.Annals of Statistics, 4:1236–1239.
Bail, C. A. (2024). Can generative ai improve social science?Proceedings of the National Academy
of Sciences, 121(21):e2314021121.
38

Barres, V., Dong, H., Ray, S., Si, X., and Narasimhan, K. (2025).τ2-bench: Evaluating conversa-
tional agents in a dual-control environment.arXiv preprint arXiv:2506.07982.
Berg, J., Dickhaut, J., and McCabe, K. (1995). Trust, reciprocity, and social history.Games and
economic behavior, 10(1):122–142.
Bini, P., Cong, L. W., Huang, X., and Jin, L. J. (2025). Behavioral economics of ai: Llm biases and
corrections.Available at SSRN 5213130.
Bond, P., Edmans, A., and Goldstein, I. (2012). The real effects of financial markets.Annual Review
of Financial Economics, 4(1):339–360.
Bossaerts, F., Yadav, N., Bossaerts, P., Nash, C., Todd, T., Rudolf, T., Hutchins, R., Ponsonby,
A.-L., and Mattingly, K. (2024). Price formation in field prediction markets: The wisdom in the
crowd.Journal of Financial Markets, 68:100881.
Brogaard, J., Hendershott, T., and Riordan, R. (2014). High-frequency trading and price discovery.
The Review of Financial Studies, 27(8):2267–2306.
Cai, H., Chen, Y., and Fang, H. (2009). Observational learning: Evidence from a randomized
natural field experiment.American Economic Review, 99(3):864–882.
Camerer, C. F., Ho, T.-H., and Chong, J.-K. (2004). A cognitive hierarchy model of games.The
quarterly journal of economics, 119(3):861–898.
Charness, G., Jabarian, B., and List, J. A. (2023). Generation next: Experimentation with ai.
Technical report, National Bureau of Economic Research.
Chen, Y., Liu, T. X., Shan, Y., and Zhong, S. (2023). The emergence of economic rationality of
gpt.Proceedings of the National Academy of Sciences, 120(51):e2316205120.
Chen, Y., Ruberry, M., and Vaughan, J. W. (2012). Designing informative securities.arXiv preprint
arXiv:1210.4837.
Colliard, J.-E., Foucault, T., and Lovo, S. (2025). Algorithmic pricing and liquidity in securities
markets.HEC Paris Research Paper No. FIN-2022-1459.
Corgnet, B., Desantis, M., and Porter, D. (2018). What makes a good trader? on the role of
intuition and reflection on trader performance.The Journal of Finance, 73(3):1113–1137.
Costa-Gomes, M. A. and Crawford, V. P. (2006). Cognition and behavior in two-person guessing
games: An experimental study.American economic review, 96(5):1737–1768.
Cowgill, B. and Zitzewitz, E. (2015). Corporate prediction markets: Evidence from Google, Ford,
and Firm X.The Review of Economic Studies, 82(4):1309–41.
Cultivate Labs (2021). How does the logarithmic market scoring rule
(lmsr) work?https://www.cultivatelabs.com/prediction-markets-guide/
how-does-logarithmic-market-scoring-rule-lmsr-work. Accessed: 04-17-2021.
39

Dell’Acqua, F., McFowland III, E., Mollick, E., Lifshitz, H., Kellogg, K. C., Rajendran, S., Krayer,
L., Candelon, F., and Lakhani, K. R. (2026). Navigating the jagged technological frontier: Field
experimental evidence of the effects of artificial intelligence on knowledge worker productivity
and quality.Organization Science, 37(2):403–423.
Diercks, A. M., Katz, J. D., and Wright, J. H. (2026). Kalshi and the rise of macro markets.
Technical report, National Bureau of Economic Research.
Dou, W. W., Goldstein, I., and Ji, Y. (2025). Ai-powered trading, algorithmic collusion, and price
efficiency. Technical report, National Bureau of Economic Research.
Dugast, J. and Foucault, T. (2025). Equilibrium data mining and data abundance.The Journal of
Finance, 80(1):211–258.
Dziri, N., Lu, X., Sclar, M., Li, X. L., Jiang, L., Lin, B. Y., Welleck, S., West, P., Bhagavatula, C.,
Le Bras, R., et al. (2023). Faith and fate: Limits of transformers on compositionality.Advances
in neural information processing systems, 36:70293–70332.
Frongillo, R., Papireddygari, M., and Waggoner, B. (2024). An axiomatic characterization of
CFMMs and equivalence to prediction markets. In15th Innovations in Theoretical Computer
Science Conference (ITCS 2024), pages 51:1–51:21.
Galanis, S., Ioannou, C. A., and Kotronis, S. (2024). Information aggregation under ambiguity:
theory and experimental evidence.Review of Economic Studies, 91(6):3423–3467.
Galanis, S. and Kotronis, S. (2021). Updating awareness and information aggregation.B.E. Journal
of Theoretical Economics, 21:613–635.
Galanis, S. and Mikhalishchev, S. (2026). Information aggregation with costly information acquisi-
tion.Mimeo.
Geanakoplos, J. (1992). Common knowledge.The Journal of Economic Perspectives, 6(4):53–82.
Geanakoplos, J. and Polemarchakis, H. (1982). We can’t disagree forever.Journal of Economic
Theory, 28:192–200.
Glosten, L. R. and Milgrom, P. R. (1985). Bid, ask and transaction prices in a specialist market
with heterogeneously informed traders.Journal of financial economics, 14(1):71–100.
Gu, S., Kelly, B., and Xiu, D. (2020). Empirical asset pricing via machine learning.The Review of
Financial Studies, 33(5):2223–2273.
Hanson, R. (2003). Combinatorial information market design.Information Systems Frontiers,
5(1):107–119.
Hanson, R. (2007). Logarithmic market scoring rules for modular combinatorial information aggre-
gation.Journal of Prediction Markets, 1(1):3–15.
Hayek, F. A. (1945). The use of knowledge in society.The American Economic Review, 35(4):519–
530.
40

Hendershott, T., Jones, C. M., and Menkveld, A. J. (2011). Does algorithmic trading improve
liquidity?The Journal of Finance, 66(1):1–33.
Henning, T., Ojha, S. M., Spoon, R., Han, J., and Camerer, C. F. (2025). Llm trading: Analysis of
llm agent behavior in experimental asset markets.arXiv preprint arXiv:2502.15800.
Horton, J. J. (2023). Large language models as simulated economic agents: What can we learn from
homo silicus? Technical report, National Bureau of Economic Research.
Jain, N., Han, K., Gu, A., Li, W.-D., Yan, F., Zhang, T., Wang, S., Solar-Lezama, A., Sen, K., and
Stoica, I. (2024). Livecodebench: Holistic and contamination free evaluation of large language
models for code.arXiv preprint arXiv:2403.07974.
Kambhampati, S., Valmeekam, K., Guan, L., Verma, M., Stechly, K., Bhambri, S., Saldyt, L. P.,
and Murthy, A. B. (2024). Position: Llms can’t plan, but can help planning in llm-modulo
frameworks. InForty-first International Conference on Machine Learning.
Kim, Y., Gu, K., Park, C., Park, C., Schmidgall, S., Heydari, A. A., Yan, Y., Zhang, Z., Zhuang,
Y., Malhotra, M., et al. (2025). Towards a science of scaling agent systems.arXiv preprint
arXiv:2512.08296.
Kneeland, T. (2015). Identifying higher-order rationality.Econometrica, 83(5):2065–2079.
Korinek, A. (2023). Generative ai for economic research: Use cases and implications for economists.
Journal of Economic Literature, 61(4):1281–1317.
Kyle, A. S. (1985). Continuous auctions and insider trading.Econometrica, 53:1315 – 1335.
Lehar, A. and Parlour, C. (2025). Decentralized exchange: The uniswap automated market maker.
The Journal of Finance, 80(1):321–374.
Lopez-Lira, A. and Tang, Y. (2025). Can chatgpt forecast stock price movements? return pre-
dictability and large language models.Journal of Financial Economics. Forthcoming.
Manning, B. S., Zhu, K., and Horton, J. J. (2024). Automated social science: Language models as
scientist and subjects. Technical report, National Bureau of Economic Research.
Manning, C. and Schutze, H. (1999).Foundations of statistical natural language processing. MIT
press.
McKelvey, R. D. and Page, T. (1990). Public and private information: An experimental study of
information pooling.Econometrica, 58:1321–1339.
Milgrom, P. and Stokey, N. (1982). Information, trade, and common knowledge.Journal of Eco-
nomic Theory, 26:17–27.
Nagel, R. (1995). Unraveling in guessing games: An experimental study.The American economic
review, 85(5):1313–1326.
Ostrovsky, M. (2012). Information aggregation in dynamic markets with strategic traders.Econo-
metrica, 80(6):2595–2647.
41

Page, L. and Siemroth, C. (2021). How much information is incorporated into financial asset prices?
experimental evidence.The Review of Financial Studies, 34(9):4412–4449.
Park, J. S., O’Brien, J., Cai, C. J., Morris, M. R., Liang, P., and Bernstein, M. S. (2023). Gen-
erative agents: Interactive simulacra of human behavior. InProceedings of the 36th annual acm
symposium on user interface software and technology, pages 1–22.
Phan, L., Gatti, A., Han, Z., Li, N., Hu, J., Zhang, H., Zhang, C. B. C., Shaaban, M., Ling, J., Shi,
S., et al. (2025). Humanity’s last exam.arXiv preprint arXiv:2501.14249.
Plott, C. R. and Sunder, S. (1988). Rational expectations and the aggregation of diverse information
in laboratory security markets.Econometrica, pages 1085–1118.
Pustejovsky, J. E. and Tipton, E. (2018). Small-sample methods for cluster-robust variance estima-
tion and hypothesis testing in fixed effects models.Journal of Business & Economic Statistics,
36(4):672–683.
Pyatkin, V., Malik, S., Graf, V., Ivison, H., Huang, S., Dasigi, P., Lambert, N., and Hajishirzi, H.
(2025). Generalizing verifiable instruction following.arXiv preprint arXiv:2507.02833.
Rajtmajer, S., Griffin, C., Wu, J., Fraleigh, R., Balaji, L., Squicciarini, A., Kwasnica, A., Pennock,
D., McLaughlin, M., Fritton, T., et al. (2022). A synthetic prediction market for estimating
confidence in published work. InProceedings of the AAAI Conference on Artificial Intelligence,
volume 36, pages 13218–13220.
Rasooly, I. and Rozzi, R. (2025). How manipulable are prediction markets?arXiv preprint
arXiv:2503.03312.
Rein, D., Hou, B. L., Stickland, A. C., Petty, J., Pang, R. Y., Dirani, J., Michael, J., and Bowman,
S. R. (2024). Gpqa: A graduate-level google-proof q&a benchmark. InFirst Conference on
Language Modeling.
Saxena, M., Pangallo, M., Hommes, C., Caccioli, F., and del Rio-Chanona, R. M. (2026). Ma-
chine spirits: Speculation and adaptation of llm agents in asset markets.arXiv preprint
arXiv:2604.18602.
Schlegel, C., Kwaśnicki, M., and Mamageishvili, A. (2026). Axioms for constant function market
makers.Mathematical Finance.
Sheng, J., Sun, Z., Yang, B., and Zhang, A. L. (2026). Generative ai and asset management.The
Review of Financial Studies, page hhag050.
The Economist (2021). How spooks are turning to superforecasting in the cosmic
bazaar.https://www-economist-com.ezphost.dur.ac.uk/science-and-technology/2021/
04/15/how-spooks-are-turning-to-superforecasting-in-the-cosmic-bazaar. Accessed:
04-17-2021.
Tian, M., Gao, L., Zhang, S., Chen, X., Fan, C., Guo, X., Haas, R., Ji, P., Krongchon, K., Li, Y.,
et al. (2024). Scicode: A research coding benchmark curated by scientists.Advances in Neural
Information Processing Systems, 37:30624–30650.
42

Valmeekam, K., Marquez, M., Sreedharan, S., and Kambhampati, S. (2023). On the planning abil-
ities of large language models-a critical investigation.Advances in neural information processing
systems, 36:75993–76005.
Wang, Y., Ma, X., Zhang, G., Ni, Y., Chandra, A., Guo, S., Ren, W., Arulraj, A., He, X., Jiang,
Z., et al. (2024). Mmlu-pro: A more robust and challenging multi-task language understanding
benchmark.Advances in Neural Information Processing Systems, 37:95266–95290.
Weber, R. A. (2001). Behavior and learning in the “dirty faces” game.Experimental Economics,
4(3):229–242.
Weller, B. M. (2018). Does algorithmic trading reduce information acquisition?The Review of
Financial Studies, 31(6):2184–2226.
Yang, C., Xuezhi, W., Lu, Y., Liu, H., Le, Q. V., Zhou, D., and Chen, X. (2023). Large language
models as optimizers. InThe Twelfth International Conference on Learning Representations.
43

Supplementary Appendix
Information Aggregation with AI Agents
SA.1 Separability
In this section we define the notion of separability and show that the securities are separable in all
four structures of the experiment. We consider a finite state spaceΩand a set of tradersIwith
n=|I|. Traderi’s initial private information is represented by partitionΠ i ofΩ. LetΠ i(ω)be a
partition element ofΠ i that containsω, so thatω∈Π i(ω)∈Π i. When the true state isω∈Ω,
Tradericonsiders all states inΠ i(ω)⊆Ωto be possible. We assume that the join (the coarsest
common refinement) of partitionsΠ ={Π 1, . . .Πn}consists of singleton sets so that T
i∈I
Πi(ω) =ω
for allω∈Ω, which means that the traders’ pooled information always reveals the true state. Note
that this assumption is satisfied in all four structures of the experiment. LetEµ[X|Π i(ω)]be the
expected value of securityX, conditional on private informationΠi(ω)and priorµ. LetSupp(µ)
be the support ofµ.
Definition 1.A securityXis called non-separable under information structureΠif there exists
probability distributionµand valuev∈Rsuch that:
(i)X(ω)̸=vfor someω∈Supp(µ),
(ii)E µ[X|Π i(ω)] =vfor alli= 1, ..., nandω∈Supp(µ).
Otherwise, it is called separable.
For structures t3s111 and t3s110, the securityXis Arrow-Debreu, paying 1 in one state and 0
otherwise. Ostrovsky (2012) shows that Arrow-Debreu securities are separable irrespective of the
information structure. For the other two structures, we will use the following characterization of
separable securities by Ostrovsky (2012). It specifies thatXis separable if and only if, for anyv,
we can find numbersλi(Πi(ω)), for eachiandω, such that the sum over all traders has the same
sign as the difference ofX(ω)−v. Intuitively, for anyvand at eachω, all traders “vote” and the
sign of the sum of the votes has to agree with the sign of the difference between the value of the
security andv.
Proposition 1(Ostrovsky (2012)).SecurityXis separable under partition structureΠif and only
if, for everyv∈R, there exist functionsλ i : Πi →Rfori= 1, . . . , nsuch that, for every stateω
withX(ω)̸=v,
(X(ω)−v)
X
i∈I
λi(Πi(ω))>0.
Suppose thatvis strictly between0and1. For structure t3s111y2, assignλ 1 = 1to partition
cells{a, b, c, d},{a, b, e, f},{a, c, e, g}andλ2 =−1to all other cells. For structure t3s111o2ye2,
assignλ 1 =−1to cells{a, e},{a, c},{a, b},λ 2 =−10to cells{d, h},{f, h},{g, h}, andλ 3 = 4to
all other cells. Then, it is straightforward to check that the inequality(X(ω)−v)P
i∈I
λi(Πi(ω))>0
is satisfied for both structures and all states. Ifv≥1orv≤0, then(X(ω)−v)has the same sign
for allωwithX(ω)̸=v, so finding appropriateλis trivial.
1

SA.2 Statistical Power and Minimum Detectable Effects
Several of our central findings are null results: communication, strategic prompting, the initial
price, and market duration do not significantly improve information aggregation. Because a failure
to reject is informative only to the extent that the design could have detected an effect had one
been present, we report an ex-ante power analysis that quantifies the smallest effect each test can
detect. We deliberately avoid closed-form power formulas (e.g., those based on the non-central
Fdistribution), because they assume independent and identically distributed errors and would
substantially overstate power by ignoring both the intra-team correlation and the small number
of clusters (G= 12) that govern our CR2/Satterthwaite inference. Instead, we compute power
by Monte Carlo simulation operating through the exact estimator and inference used in our main
specifications.
For each treatment coefficient we hold the design matrix fixed, inject a known effect of mag-
nitudeδ, and regenerate the outcome by resampling residuals in two components, a cluster-level
shock and a within-cluster deviation, so that both the intra-team correlation and the pronounced
right-skew of the log-error distribution are preserved. We then re-estimate the model, apply the
CR2/Satterthwaite test, and record whether it rejects at the 5% level; repeating this1,000times
yields the rejection probability (power) at eachδ. The minimum detectable effect (MDE) is the
value ofδat which power reaches 80%. Under the null (δ= 0) the simulated rejection rate is close
to the nominal level (between 0.04 and 0.07 across coefficients), confirming that the CR2 procedure
is correctly sized rather than mechanically conservative.
Table SA.1 reports the MDEs for the mean (OLS), median (Q50), and tail (Q80) specifications.
For the mean outcome, the design is well powered for communication and duration: it detects a
comments effect of0.83log-error units (about 7% of the outcome standard deviation) and duration
effects of roughly2.0units (about 17%). These nulls are therefore informative, as effects of the mag-
nitude that would be economically meaningful would have been detected. For strategic prompting,
the relevant test of the strategic-prompting hypothesis is the joint nullity of the main effect and
its interactions with duration; the joint MDE is1.09log-error units, so we can rule out strategic
effects larger than roughly one log-error unit on the mean, though not smaller ones. The initial-price
contrasts are the least precisely estimated on the mean: their effects are not detectable within the
simulated range, reflecting that these contrasts enter an interaction with the information structure
and are identified off limited within-cell variation. The common thread is that the mean outcome
is the least precise of the three, because its sampling variance is dominated by a small number of
“crash” markets; the quantile specifications, which are robust to these outliers, are correspondingly
better powered.
The median (Q50) specification is well powered throughout, with pooled MDEs near0.01log-
error units. This precision is partly mechanical, however: in the Easy and Medium structures the
typical market already aggregates, so the median log error sits at zero and there is little room for
any treatment to move it. To separate this floor from genuine precision, Table SA.2 re-estimates the
quantile MDEs separately within each structure. In the Hard and Very Hard structures, the median
log error sits well above zero (0.28 and 0.69), creating room for treatments to matter. However, the
strategic MDE at the median in the Hard structure is 0.38, which exceeds the baseline error of 0.28,
indicating that the design lacks the power to reliably detect even a complete correction to perfect
accuracy in this specific setting. By contrast, in the Very Hard structure, the MDE of 0.36 is well
below the median outcome of 0.69. The null for strategic prompting is therefore highly informative
in the most complex environment: strategic prompting does not meaningfully improve the typical
2

Table SA.1: Minimum Detectable Effects for the Treatment Nulls
CR2 SE MDE: Mean (% of SD) MDE: Median MDE: Tail
(OLS) (OLS, sim.) (Q50) (Q80)
Comments Allowed 0.319 0.810 6.9% 0.009 0.107
Duration: 6 Rounds 1.172 2.031 17.3% 0.014 0.379
Duration: 9 Rounds 1.250 2.117 18.0% 0.014 0.298
Strategic Prompt 0.292 1.376 11.7% 0.008 0.215
Initial Error (Low) 0.120>1.2 — 0.012 0.165
Initial Error (Medium) 0.186>1.9 — 0.009 0.190
Notes: The MDE is the smallest true effect detectable with 80% power atα= 0.05, expressed in log-error
units. The Mean (OLS) column is from Monte Carlo simulation (1,000replications) operating through the
CR2/Satterthwaite estimator; the outcome standard deviation is11.8. For the Strategic Prompt, the table
reports the single-coefficient MDE for comparability across rows; the joint MDE for the main effect and its
duration interactions is1.09. The initial-error effects are not detectable within the simulated grid (±10CR2
standard errors), so no value is reported. The Low and Medium rows are the two estimated sum-contrast
deviations of the initial log error; the High deviation is the omitted level, equal to minus the sum of the other
two. The Median (Q50) and Tail (Q80) columns are not simulated: they report the analytic MDE, equal to
2.802times the bootstrapped standard error (200replications) of the corresponding quantile regression. The
1,000Monte Carlo replications apply only to the OLS mean column; the200replications refer to the quantile-
regression bootstrap and match the bootstrapped inference used elsewhere in the paper.
Very Hard market, and this failure is not an artifact of a statistical floor. By contrast, the tail
(Q80) is well powered only in the Easy structure; in the harder structures the crash-driven variance
inflates the bootstrapped standard errors, so tail MDEs become large (up to19log-error units in
the Hard structure). We accordingly refrain from making tail claims about strategic prompting or
initial price in the Hard structure, where crash-driven variance inflates the tail MDEs. However, in
the Very Hard structure, the tail MDE for the low initial price drops to 3.48, providing adequate
power to detect the large mispricings (β= 10.42) reported in Result 4.
Table SA.2: Minimum Detectable Effects by Information Structure
Median Median (Q50) MDE Tail (Q80) MDE
Structure Log Err. Strategic Init. (Low) Init. (Med.) Strategic Init. (Low) Init. (Med.)
Easy 0.00 0.04 0.01 0.00 0.21 0.15 0.15
Medium 0.00 0.01 0.02 0.02 3.07 4.79 2.50
Hard 0.28 0.38 0.16 0.17 19.26 8.48 6.45
Very Hard 0.69 0.36 0.43 0.40 1.67 3.48 2.66
Notes: Analytic MDE= 2.802×the bootstrapped standard error (200replications) from quantile regressions
estimated separately within each structure, in log-error units. A median log error near zero indicates that the
typical market already aggregates (a floor), so the corresponding MDE is uninformative; a median log error
above zero indicates room for treatments to move outcomes, so a small MDE represents an informative null.
Taken together, the power analysis disciplines the interpretation of our nulls. The nulls for
communication and duration are informative on the mean: effects larger than roughly0.8and
2.0log-error units, respectively, would have been detected. The null for strategic prompting is
informative at the typical market specifically in the Very Hard structure, where the design detects
effects as small as 0.36 log-error units (well below the baseline error of 0.69). In the Hard structure,
3

however, the median MDE (0.38) exceeds the baseline error (0.28), rendering the null uninformative
for the typical market. On the mean, we can exclude only large strategic effects, and we make no tail
claims in either complex structure. The null for the initial price is the weakest overall: on the pooled
mean, its average effect is not detectable. However, the structure-specific divergence identified in
Result 4 is adequately powered. Specifically, the design is well powered to detect an effect on the
typical (median) Very Hard market, as its MDE is small (0.40−0.43). Simultaneously, the tail
is adequately powered (Very Hard Q80 MDE of 3.48) to detect the large mispricings (β= 10.42)
associated with the initial price in the worst-performing markets. This pattern is consistent with
our broader finding that the informational content of these markets resides in the typical outcome
and the tail behaves idiosyncratically.
SA.3 Robustness Checks by Market Duration
In this section we report the text-analysis regressions of Table 7 estimated separately for markets
lasting 3, 6, and 9 rounds.
4

Table SA.3: Robustness Check: Cosine Similarity by Market Duration (CR2 Standard Errors)
Dependent variable:
Cosine Similarity (Public, Private)
3-Round 6-Round 9-Round
(1) (2) (3)
Constant 0.331 ∗∗∗ (0.058) 0.311 ∗∗∗ (0.044) 0.329 ∗∗∗ (0.042)
Strategic Prompt−0.004 (0.004)−0.003 (0.004)−0.003 (0.004)
Round 2 0.025 . (0.014) 0.033 ∗ (0.015) 0.032 ∗ (0.013)
Round 3 0.005 (0.016) 0.005 (0.014) 0.003 (0.014)
Round 4 0.029 . (0.015) 0.032 ∗∗ (0.011)
Round 5 0.042 ∗∗ (0.016) 0.039 ∗∗ (0.014)
Round 6 0.009 (0.017) 0.003 (0.018)
Round 7 0.039 ∗ (0.018)
Round 8 0.047 ∗∗∗ (0.013)
Round 9 0.032 . (0.019)
Medium (t3s110)−0.017 (0.014)−0.015 (0.010)−0.029 ∗∗∗ (0.008)
Hard (t3s111)−0.006 (0.010) 0.012 (0.010)−0.001 (0.007)
Very Hard (t3s111o2ye2) 0.001 (0.015) 0.005 (0.010)−0.001 (0.007)
Experiment Disclosure 0.004 (0.019) 0.011 (0.019) 0.011 (0.018)
Initial Error 0.009 (0.026) 0.001 (0.016) 0.001 (0.012)
Individual Intelligence 0.001 (0.002) 0.001 (0.002) 0.001 (0.002)
Observations 1,776 3,552 5,292
R2 0.015 0.034 0.029
Notes: .p<0.1; ∗p<0.05; ∗∗p<0.01; ∗∗∗p<0.001. CR2 cluster-robust standard errors, clustered by AI
team composition, are reported in parentheses. The model uses a mixed-contrast specification. Treat-
ment contrast baselines are: Round 1 for Round, Easy (t3s111y2) for Structure, and No Disclosure for
Experiment Disclosure. The Strategic Prompt variable uses sum contrasts, representing the deviation
from the grand mean, whereas Initial Error is mean-centered.
5

Table SA.4: Robustness Check: Word Gap by Market Duration (CR2 Standard Errors)
Dependent variable:
Word Gap
3-Round Markets 6-Round Markets 9-Round Markets
(1) (2) (3)
Constant 31.127 . (17.734) 35.468 ∗ (15.756) 32.393 ∗ (14.326)
Strategic Prompt 0.682 (0.596) 0.114 (0.480) 1.282 ∗ (0.645)
Round 2−13.385 (8.313)−12.328 (8.341)−13.802 . (7.461)
Round 3−24.149 ∗ (10.091)−25.950 ∗ (10.454)−24.945 ∗ (9.743)
Round 4−12.730 ∗∗ (3.883)−11.833 ∗∗ (4.002)
Round 5−23.211 ∗∗ (8.601)−24.144 ∗∗ (7.531)
Round 6−31.712 ∗∗ (10.433)−30.467 ∗∗ (9.379)
Round 7−18.861 ∗∗∗ (5.144)
Round 8−26.700 ∗∗∗ (8.090)
Round 9−32.712 ∗∗∗ (9.620)
Medium (t3s110)−2.959 (2.270)−3.839 ∗ (1.759) 1.157 (1.207)
Hard (t3s111) 0.958 (2.769)−0.100 (1.270) 4.582 ∗∗ (1.554)
Very Hard (t3s111o2ye2) 3.865 (2.826) 4.459 ∗∗∗ (1.302) 7.073 ∗∗∗ (1.788)
Experiment Disclosure 12.640 ∗∗∗ (2.191) 15.753 ∗∗∗ (3.654) 14.981 ∗∗∗ (3.707)
Initial Error 2.330 (2.853) 2.005 (4.383) 3.618 ∗ (1.491)
Individual Intelligence 1.050 . (0.578) 0.813 . (0.486) 0.796 . (0.452)
Observations 1,776 3,552 5,292
R2 0.143 0.152 0.159
Notes: .p<0.1; ∗p<0.05; ∗∗p<0.01; ∗∗∗p<0.001. CR2 cluster-robust standard errors, clustered by AI
team composition, are reported in parentheses. The model uses a mixed-contrast specification. Treat-
ment contrast baselines are: Round 1 for Round, Easy (t3s111y2) for Structure, and No Disclosure for
Experiment Disclosure. The Strategic Prompt variable uses sum contrasts, representing the deviation
from the grand mean, whereas Initial Error is mean-centered.
6

Table SA.5: Robustness Check: Propensity to Deceive by Market Duration
Dependent variable:
Deception
3-Round 6-Round 9-Round
(1) (2) (3)
Strategic Prompt−0.039 (0.066) 0.006 (0.056) 0.020 (0.056)
Round 2−0.426 ∗∗∗ (0.126)−0.364 ∗∗ (0.130)−0.388 ∗∗ (0.126)
Round 3−0.628 ∗∗∗ (0.130)−0.696 ∗∗∗ (0.134)−0.645 ∗∗∗ (0.131)
Round 4−0.278 ∗ (0.120)−0.114 (0.115)
Round 5−0.145 (0.125)−0.161 (0.124)
Round 6−0.510 ∗∗∗ (0.137)−0.615 ∗∗∗ (0.140)
Round 7−0.183 (0.125)
Round 8−0.062 (0.124)
Round 9−0.482 ∗∗∗ (0.140)
Medium (t3s110) 1.703 ∗∗∗ (0.242) 0.917 ∗∗∗ (0.172) 1.270 ∗∗∗ (0.163)
Hard (t3s111) 1.650 ∗∗∗ (0.268) 0.693 ∗∗∗ (0.199) 0.853 ∗∗∗ (0.190)
Very Hard (t3s111o2ye2) 1.994 ∗∗∗ (0.230) 1.093 ∗∗∗ (0.160) 1.401 ∗∗∗ (0.157)
Experiment Disclosure 0.693 ∗∗∗ (0.139) 0.790 ∗∗∗ (0.117) 0.971 ∗∗∗ (0.118)
Initial Error 0.552 (0.401) 0.113 (0.323) 0.284 (0.332)
Individual Intelligence 0.013 ∗∗ (0.004)−0.009 ∗ (0.004)−0.007 ∗ (0.004)
Observations 2,203 4,410 6,576
Notes: .p<0.1; ∗p<0.05; ∗∗p<0.01; ∗∗∗p<0.001. Ordered logit estimates predicting deception, ordered
as Truth<Withhold<Lie. Positive coefficients indicate a shift toward higher propensities of with-
holding or lying. All specifications employ a mixed-contrast framework: treatment contrasts are used
for Round, Structure, and Experiment Disclosure, with Round 1, Easy (t3s111y2), and No Disclosure
serving as the respective omitted baselines. The Strategic Prompt indicator uses sum contrasts (repre-
senting deviations from the grand mean), while the Initial Error continuous variable is mean-centered.
Standard errors reported in parentheses are CR1 cluster-robust standard errors clustered at the unique
market level (‘slug’) to account for intra-market correlation across competing agents and repeated com-
munication rounds.
7

SA.4 Information Provision
This section reports the two regression tables for the information provision treatment discussed in
Section 6.3, estimated on the pooled sample of 3,500 markets. First, we display the text appended
to the prompt in the Experiment Disclosure treatment, which was dynamically generated based on
which model was trading.25 We provided qualitative historical guidance in the prompt, without
specifying a trading strategy:
=== Experimental Findings & Strategic Context ===
Before trading, all traders are informed about the following qualitative
results from a study of over 1,700 similar prediction markets involving LLM
agents. Use them to guide your decisions.
Definition of market accuracy: denotes how close is the last price of the
Yes shares to the true value of the Yes shares, and similarly for the No
shares.
Definition of Intelligence: Agents are scored on the "Artificial Analysis
Intelligence Index" (reasoning, math, coding). The observed range in our
study is 7 (Low) to 46 (High).
1. Intelligence
* Your Intelligence (trader_2): 46
* Intelligence of trader_1: 30
* Intelligence of trader_3: 41
* Average Group Intelligence: 39.00
Result 1 shows that higher individual intelligence directly correlates
with higher profits.
2. Market Complexity
* We ranked the market structures by complexity of reasoning: Level 1
(Easiest) < Level 2 < Level 3 < Level 4 (Hardest).
* Current Status: You are trading in a Level 4 market.
Result 2 shows that as complexity rises, trader profits decrease and
the market becomes less accurate.
3. Market Design
* Result 3: Trading order significantly impacts profitability. The most
profitable position is 3rd, followed by 1st, with 2nd being the least
25The qualitative summaries provided in the information treatment were constructed using provisional analysis
(employing HC1 robust standard errors) immediately following the first wave of the experiment. While our final, more
conservative CR2 clustered specifications render some adjacent structural boundaries statistically indistinguishable
(e.g., the effect of Easy and Medium on market accuracy), the directional point estimates for the treatment parameters
remain identical. Consequently, the information provided represents a valid, directionally accurate heuristic regarding
the historical market environment. In particular, the prompt’s Result 7 states an unqualified null for the initial price,
reflecting the provisional average estimate; our final analysis (Result 4) qualifies this with a Very Hard-specific
interaction that the provisional analysis had not identified. The provisional analysis is reported in Section 2 of the
Supplementary Appendix.
8

profitable (3rd > 1st > 2nd).
* Result 4: Higher average group intelligence leads to a more accurate
market but lower individual profits.
* Neutral Factors: The following factors have no statistically significant
effect on market accuracy:
* Result 5: Posting public comments has no effect on market accuracy.
* Result 6: Being "myopic" (maximize profits on current round only) vs.
"strategic" (maximize profits for current and all future rounds) has no
effect on market accuracy.
* Result 7: The initial price of the market has no effect on market
accuracy.
* Result 8: Increasing the duration of the market (9 rounds vs 3) has no
effect on market accuracy.
9

Table SA.6: Information Aggregation With Disclosure
Dependent variable:
Log Error
Mean (OLS) Median (Q50) Tail Risk (Q80)
(1) (2) (3)
Constant 7.196 ∗∗∗ (2.061) 0.018 ∗ (0.008) 5.638 ∗∗∗ (0.954)
Comments Allowed−0.318 (0.258)−0.001 (0.001)−0.014 (0.038)
Duration: 6 Rounds−1.550 (1.118)−0.001 (0.001)−0.107 (0.112)
Duration: 9 Rounds−0.328 (1.183)−0.001 (0.001)−0.019 (0.086)
Strategic Prompt 0.007 (0.231) 0.001 (0.001) 0.007 (0.064)
Medium (t3s110) 2.772 (3.002)−0.00001 (0.001) 0.075 (0.971)
Hard (t3s111) 5.222 ∗ (2.225) 0.206 ∗ (0.093) 11.809 . (6.577)
Very Hard (t3s111o2ye2) 7.192 ∗ (3.332) 0.697 ∗∗∗ (0.024) 20.126 ∗∗∗ (5.325)
Initial Error: Low 0.123 (0.198) 0.00000 (0.001) 0.008 (0.046)
Initial Error: Medium 0.234 (0.236)−0.00001 (0.001)−0.003 (0.048)
Experiment Disclosure 2.075 (1.963)−0.00004 (0.008) 0.980 (4.638)
Average Intelligence−0.218 ∗∗∗ (0.058)−0.0004 ∗ (0.0002)−0.123 ∗∗∗ (0.021)
Intelligence SD−0.012 (0.223)−0.0003 ∗∗ (0.0001)−0.102 ∗∗∗ (0.020)
6 Rounds x Strategic−0.083 (0.294)−0.001 (0.001)−0.021 (0.093)
9 Rounds x Strategic 0.182 (0.286)−0.001 (0.001) 0.014 (0.084)
Medium Struct x Init. Error (Low) 0.657 (0.786)−0.00000 (0.001) 0.003 (1.897)
Hard Struct x Init. Error (Low) 0.120 (0.474) 0.045 (0.097)−8.149 (11.199)
Very Hard x Init. Error (Low) 1.665 (1.222) 0.008 (0.047) 9.638 ∗ (4.721)
Medium Struct x Init. Error (Med)−0.399 (0.378) 0.00001 (0.001) 0.006 (0.957)
Hard Struct x Init. Error (Med) 0.187 (0.594)−0.077 (0.130) 18.273 (11.427)
Very Hard x Init. Error (Med)−0.321 (0.975)−0.004 (0.024) 8.923 (6.687)
Disclosure x Av. Intelligence−0.053 (0.061) 0.00000 (0.0002)−0.023 (0.109)
Observations 3,500 3,500 3,500
R2 0.119
Notes: .p<0.1; ∗p<0.05; ∗∗p<0.01; ∗∗∗p<0.001. Q50 and Q80 are quantile regressions. Q50 mod-
els the median log error, whereas Q80 models the upper 20% tail of the log error distribution (the
worst-performing markets). OLS model uses CR2 cluster-robust standard errors clustered by exact AI
team composition, featuring small-sample degrees of freedom adjustments. Quantile models use boot-
strapped standard errors. All three models use a mixed-contrast specification. Rounds, Structure, and
Experiment Disclosure use treatment contrasts with Round 3, Structure t3s111y2, and No Disclosure as
baselines. All other controls (Initial Error, Strategic, Comments) use sum contrasts, where coefficients
represent deviations from the grand mean.
10

Table SA.7: Trading Volume and Agent Profitability With Disclosure
Dependent variable:
Trading Volume Individual Profits
(1) (2)
Constant 1,757.638 . (1,057.684)−77.335 ∗ (30.791)
Comments Allowed 36.269 (29.026) 3.552 (2.747)
Duration: 6 Rounds 563.399 ∗∗∗ (104.689) 3.359 (17.416)
Duration: 9 Rounds 1,080.922 ∗∗∗ (209.860)−12.727 (19.250)
Strategic Prompt−37.028 . (21.233)−0.345 (2.338)
Medium (t3s110) 316.783 ∗ (156.405)−35.852 (38.603)
Hard (t3s111) 212.977 ∗∗ (67.246)−71.160 ∗ (32.793)
Very Hard (t3s111o2ye2) 43.866 (267.233)−101.644 ∗ (45.614)
Initial Error: Low−145.678 ∗ (66.395)−12.168 ∗∗∗ (3.042)
Initial Error: Medium 44.294 (56.922)−5.193 (3.645)
Experiment Disclosure 171.986 (137.059)−21.052 (14.316)
Average Intelligence−28.182 (24.757)−11.057 ∗∗∗ (1.855)
Individual Intelligence 14.091 ∗∗∗ (1.787)
Intelligence SD 24.293 (40.089) 1.154 (2.467)
Trades Second−39.316 (32.790)
Trades Third 74.604 (53.060)
6 Rounds x Strategic−26.283 (34.055)−0.524 (3.928)
9 Rounds x Strategic 45.471 (41.863)−5.343 (3.828)
Medium Struct x Initial Error (Low) 166.553 (110.724)−9.165 (10.672)
Hard Struct x Initial Error (Low) 69.433 (64.362)−6.278 (7.583)
Very Hard x Initial Error (Low) 349.973 (261.708)−18.174 (15.738)
Medium Struct x Initial Error (Med)−28.194 (77.289) 2.954 (4.152)
Hard Struct x Initial Error (Med) 93.975 (73.295) 2.619 (8.980)
Very Hard x Initial Error (Med)−252.898 (441.683) 1.676 (11.363)
Disclosure x Average Intelligence−3.394 (5.256) 0.493 (0.445)
Observations 3,500 10,500
R2 0.110 0.059
Notes: .p<0.1; ∗p<0.05; ∗∗p<0.01; ∗∗∗p<0.001. Both models use CR2 cluster-robust standard er-
rors clustered by exact AI team composition, featuring small-sample degrees of freedom adjustments.
Rounds, Information Structure, Experiment Disclosure, and Trader Position use treatment contrasts,
with ‘Round 3’, ‘t3s111y2’, No Disclosure, and ‘Trades First’ serving as their respective baselines. All
other controls (Initial Error, Strategic, Comments) use sum contrasts, where coefficients represent de-
viations from the grand mean.
11

SA.5 Theoretical Myopic Profits and Volume
In this section, we derive the theoretical profits and trading volume for all four structures, if all
agents are myopic and this is common knowledge. Letpstart denote the price of Yes in the previous
round (or the initial price we are in the first round) andpend denote the price after the AI agents
conducts his trades. Theηparameter represents the liquidity sensitivity parameter, which is set to
0.01 (Rajtmajer et al., 2022; Galanis et al., 2024).
Under the Logarithmic Market Scoring Rule (LMSR), the price of a binary contract is strictly
a function of the difference in outstanding shares. The quantity of Yes shares,∆q, required to shift
the market probability frompstart top end is given by
∆q= 1 η ln  pend(1−p start) pstart(1−p end) 
The cost of buying these Yes shares is
Cost= 1 η ln  1−p start 1−p end 
If the market resolves to Yes (yielding a payout of 1 per share), the trader’s net profit is the
total payout minus the initial cost. If it resolves to No, the Yes shares are worthless and the net
profit is simply the negative cost:
ProfitYes = ∆q−Cost= 1 η ln  pend pstart 
ProfitYes =−Cost= 1 η ln  1−p end 1−p start 
The calculations for buying No shares are similar. If a trader wishes to reduce the price of Yes
fromp start top end (wherep end < pstart) and he has no Yes shares to sell, he must acquire No shares.
The quantity of No shares,∆qno, required to decrease the Yes price topend is given by:
∆qno = 1 η ln  pstart(1−p end) pend(1−p start) 
The capital required to execute this transaction depends entirely on the ratio of the starting
and ending “Yes” probabilities, mirroring the profit function of the opposing side:
Costno = 1 η ln  pstart pend 
If the market resolves to No’ (yielding a payout of 1 per share), the trader’s net profit is the total
payout minus the initial cost. If the market resolves to Yes, then the profit from this transaction is
the negative cost:
ProfitNo = ∆qno −Cost no = 1 η ln  1−p end 1−p start 
ProfitNo =−Cost no =− 1 η ln  pstart pend 
Using these formulas, we calculate the average profits and trading volume for each structure and
trader, which we report in Table 3.
12

Table SA.8: Average Volume and Profits
Average over Easy Medium Hard Very Hard Average over
initial prices t3s111y2 t3s110 t3s111 t3s111o2ye2 structures
Volume 990 1210 1210 1046 1115
Trader 1 Volume 110 110 110 56 97
Trader 2 Volume 880 110 110 0 275
Trader 3 Volume 0 990 990 990 743
Trader 1 Profits 46 46 -64 6 9
Trader 2 Profits 29 -41 69 0 14
Trader 3 Profits 0 69 69 69 52
Average Profits 25 25 25 25 25
Notes:Entries are deterministic myopic benchmark calculations from the theoretical LMSR
price path, averaged over the three initial prices used in the experiment. Volume is the absolute
quantity of shares traded. Profits are realized LMSR profits in experimental payoff units.
13

SA.6 Supplementary Graphs and Tables
LLM Providers
Gemini
2.5 Flash, 3 Flash
OpenAI
GPT-4o, GPT-5-mini
Claude
Haiku 3.5, 4.5
Ollama
Gemma3:4b, Qwen3:8b
AI Agents
Trader 1
LLM Provider A
Trader 2
LLM Provider B
Trader 3
LLM Provider C
Configuration Layer
traders.yaml
market_maker.yaml
llm_providers.yaml
Grid Parameters
Price, Info Structures,
Strategic, Rounds, Comments
Model Combinations
Orchestration Layer
Orchestrator
Market State Manager Dynamic Prompt Generator
Prediction Market Platform
Market Data
Prices, Positions
Market Maker
Price Calculator
LMSR Algorithm
Platform
API Client
Output & Logging
Session Logs Trades CSVs
Figure SA.1:Prediction market platform.The figure summarizes the automated workflow.
The experimental grid creates a market for each team, structure, duration, initial price, strategic-
prompt condition, and communication condition; the agent orchestrator calls the relevant LLM API,
constructs the trader-specific prompt from private signals, public history, private memory, portfolio
information, and hypothetical price impacts, submits trades and comments through the API, and
exports text and trade logs for analysis.
14

Wald Test: p < 0.001
−100
−50
0
50
100
Trader 1
(First Mover)
Trader 2
(Intermediate)
Trader 3
(Last Mover)
Estimated Profit (£)
Bars represent covariate−adjusted empirical profits. Diamonds indicate myopic optimums.
Estimated Profits vs. Myopic Profits
Figure SA.2:The Trading Position Effect.Bars represent covariate-adjusted estimated marginal
means (EMMs) of profit for each trading position, derived from the primary OLS specification.
Error bars indicate 95% confidence intervals constructed using CR2 cluster-robust standard errors
clustered at the unique market level. Unlike the team-composition clustering of Table 6, we cluster
the position contrasts at the market level because they are within-market comparisons among the
three competing traders, and team-composition clustering would leave only 12 clusters for trader-
level marginal-mean inference. Black diamonds denote the theoretically optimal myopic profit for
each respective position. The annotated bracket reports the result of a post-estimation Wald test
(p<0.001), confirming a highly significant late-mover advantage for the third trader relative to the
second.
15

0.00
0.01
0.02
0.03
0 50 100 150
Number of Words
Density
Message Type
Private Reasoning
Public Justification
Private messages are longer than public messages
Density Plot of the Length of Messages
Figure SA.3:Length of Private and Public Messages.The figure plots kernel densities of
message length, measured by word count on the horizontal axis, separately for private reasoning
messages and public comments. The distribution shows that private messages are typically longer
than public comments.
Table SA.9: Information Aggregation, by Group and Structure
Structure Group N Aggregates Partial Hedges Confidently wrong
Easy January 2026, all teams 432 68.5% 21.8% 3.9% 5.8%
Easy January 2026, four smartest 144 66.0% 30.6% 3.5% 0.0%
Easy April 2026, frontier 144 80.6% 19.4% 0.0% 0.0%
Medium January 2026, all teams 475 69.3% 10.9% 4.6% 15.2%
Medium January 2026, four smartest 144 86.8% 9.0% 2.8% 1.4%
Medium April 2026, frontier 144 100.0% 0.0% 0.0% 0.0%
Hard January 2026, all teams 432 44.0% 21.3% 8.3% 26.4%
Hard January 2026, four smartest 144 43.8% 31.9% 8.3% 16.0%
Hard April 2026, frontier 144 51.4% 21.5% 8.3% 18.8%
Very Hard January 2026, all teams 433 18.7% 13.4% 37.6% 30.3%
Very Hard January 2026, four smartest 144 22.2% 12.5% 56.2% 9.0%
Very Hard April 2026, frontier 144 16.7% 6.9% 66.0% 10.4%
Notes:A market aggregates if the absolute distance between the final price and the true value of the
security is below 0.1, it is confidently wrong if that distance exceeds 0.9, it hedges if the distance lies
within 0.1 of 0.5, and it is partial otherwise. The first group comprises all twelve teams of the first
wave, excluding the information provision treatment, and the second group is the subset of four teams
with the highest intelligence index in January 2026, so their markets are counted in both rows. The
third group comprises the four frontier teams of April 2026.
16

claude−3−5−haiku−20241022 (12)
gemma3:4b (7)
qwen3:8b (15)
gemini−2.5−flash (21)
gpt−5−mini (41)
claude−haiku−4−5−20251001 (30)
gpt−4o (19)
gemini−3−flash−preview (46)
0.0 0.2 0.4
Mean Squared Error
Homogeneous Markets Only
Market Accuracy by AI Model
Figure SA.4: Mean Squared Error by AI Model
gemma3:4b (7)
qwen3:8b (15)
gemini−2.5−flash (21)
claude−haiku−4−5−20251001 (30)
claude−3−5−haiku−20241022 (12)
gpt−4o (19)
gpt−5−mini (41)
gemini−3−flash−preview (46)
−200 −100 0 100
Mean Profit (£)
Figure SA.5: Average Profits by AI Model
17

gpt−5−mini qwen3:8b
gemma3:4b gpt−4o
gemini−2.5−flash gemini−3−flash−preview
claude−3−5−haiku−20241022 claude−haiku−4−5−20251001
Easy
Medium
Hard
Very Hard
Easy
Medium
Hard
Very Hard
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
Information Structure
Mean Squared Error
Homogeneous Markets Only
Baseline Model Performance by Complexity
Figure SA.6: Mean Squared Error by Structure and Model
18

gpt−5.4−2026−03−05 Mixed Team (All 3)
claude−opus−4−6 gemini−3.1−pro−preview
Easy
Medium
Hard
Very Hard
Easy
Medium
Hard
Very Hard
0.0
0.2
0.4
0.6
0.0
0.2
0.4
0.6
Information Structure
Mean Squared Error
Frontier Team Performance by Complexity
Figure SA.7: Mean Squared Error by Structure and Frontier Model
19

SA.7 Market Outcomes by Treatment Cell
This section reports the market outcomes by information structure and market duration discussed
in Section 5.
Table SA.10: Market Outcomes by Information Structure and Duration
Structure Rounds N MSE SE (Sq Er) Mean Log SE (Log) Crash Rate Avg Volume Avg IQ
First Wave
Easy 3 144 0.108 0.023 2.56 0.73 6.9% 1,255 23.8
6 144 0.070 0.018 0.69 0.34 1.4% 1,808 23.8
9 144 0.078 0.018 1.58 0.58 4.2% 2,102 23.8
Medium 3 159 0.183 0.027 3.56 0.80 9.4% 1,508 23.0
6 160 0.200 0.029 3.80 0.82 10.0% 2,065 22.9
9 156 0.202 0.030 4.69 0.92 12.8% 2,639 23.1
Hard 3 144 0.387 0.036 9.30 1.24 25.7% 1,328 23.8
6 144 0.319 0.034 4.80 0.92 11.8% 1,865 23.8
9 144 0.332 0.035 6.70 1.10 18.1% 2,356 23.8
Very Hard 3 145 0.464 0.032 8.82 1.19 23.4% 1,229 23.7
6 144 0.433 0.032 7.46 1.12 19.4% 1,752 23.8
9 144 0.436 0.032 8.56 1.19 22.9% 2,354 23.8
Both Waves
Easy 3 288 0.131 0.018 2.76 0.53 7.3% 1,264 23.8
6 288 0.081 0.013 1.15 0.34 2.8% 1,844 23.8
9 288 0.081 0.014 1.39 0.37 3.5% 2,140 23.8
Medium 3 303 0.173 0.020 3.46 0.57 9.2% 1,521 23.4
6 304 0.212 0.021 4.62 0.65 12.5% 2,072 23.3
9 300 0.223 0.022 5.75 0.73 16.0% 2,650 23.4
Hard 3 288 0.407 0.026 9.50 0.88 26.0% 1,377 23.8
6 288 0.307 0.024 4.52 0.63 11.1% 1,995 23.8
9 288 0.339 0.025 6.95 0.78 18.8% 2,515 23.8
Very Hard 3 289 0.469 0.023 9.21 0.85 24.6% 1,234 23.7
6 288 0.450 0.023 8.30 0.82 21.9% 1,739 23.8
9 288 0.456 0.023 9.39 0.87 25.3% 2,408 23.8
Third Wave (Frontier Models, April 2026)
Easy 3 48 0.016 0.005 0.07 0.02 0.0% 920 55.7
6 48 0.010 0.003 0.05 0.01 0.0% 1,226 55.7
9 48 0.003 0.001 0.03 0.01 0.0% 1,281 55.7
Medium 3 48 0.000 0.000 0.00 0.00 0.0% 1,121 55.7
6 48 0.000 0.000 0.00 0.00 0.0% 1,475 55.7
9 48 0.000 0.000 0.00 0.00 0.0% 1,532 55.7
Hard 3 48 0.263 0.053 5.36 1.76 14.6% 795 55.7
6 48 0.306 0.057 6.17 1.85 16.7% 1,274 55.7
9 48 0.314 0.058 5.52 1.75 14.6% 1,575 55.7
Very Hard 3 48 0.358 0.045 4.34 1.51 10.4% 379 55.7
6 48 0.267 0.037 3.39 1.37 8.3% 891 55.7
9 48 0.255 0.031 2.69 1.20 6.2% 794 55.7
Notes: The crash rate measures the percentage of markets that have a log error above 20. The Avg IQ
column in the third-wave panel uses the April 2026 vintage of the Artificial Analysis Intelligence Index,
which is not comparable to the January 2026 scores used in the first two panels.
20

SA.8 Randomization Balance Checks
To ensure that differences in market performance were driven by the structure and not by exoge-
nous starting conditions, we tested for balance in initial pricing errors across treatment groups.
The results are reported in Table SA.11. An OLS regression of initial squared error on information
structure reveals no significant systematic differences (F(3,3496) = 0.231, p= 0.875). The regres-
sion explains only 0.02% of the variance in initial conditions (R2 = 0.0002) and we find no evidence
of imbalances in the randomization procedure.
Table SA.11: Randomization Balance Checks
Dependent variable:
Average Intelligence Initial Squared Error
(1) (2)
Medium (t3s110)−0.412−0.005
(0.580) (0.008)
Hard (t3s111) 0.000 0.000
(0.589) (0.008)
Very Hard (t3s111o2ye2)−0.010−0.0002
(0.588) (0.008)
Constant 23.778 ∗∗∗ 0.277∗∗∗
(0.416) (0.006)
Robust F-Statistic 0.252 (df = 3; 3496) 0.231 (df = 3; 3496)
Observations 3,500 3,500
R2 0.0002 0.0002
Notes: .p<0.1; ∗p<0.05; ∗∗p<0.01; ∗∗∗p<0.001. F-test checks joint significance
of all treatments. Standard errors in parentheses are HC1 heteroskedasticity-
consistent. Because experimental treatments were assigned via a perfectly bal-
anced full-factorial grid across all agents, cluster-robust standard errors are not
applied to baseline balance verifications to prevent artificial variance shrinkage
and matrix rank-deficiency.
21

SA.9 Robustness to Alternative Standard Error Specifications
This section replicates the primary regression analyses from the main text to assess whether the
conclusions are sensitive to the conservative variance penalties imposed by our primary estimation
strategy. In the main text, the OLS models utilize CR2 cluster-robust standard errors clustered
by exact AI team composition to account for broad panel-level correlation. Here, we relax that
assumption. For market-level outcomes (Volume and Information Aggregation), we apply unclus-
tered HC1 robust standard errors, assuming independent error distributions across unique markets.
For individual-level outcomes (Trader Profits, Cosine Similarity, and Word Gap), we apply CR1
cluster-robust standard errors clustered at the unique market level. This relaxes the broad AI-
team panel assumption while accounting for the mechanical, micro-level intra-market correlation
inherent among competing agents.26 Because these adjustments apply solely to the post-estimation
variance-covariance matrix, the point estimates remain, by definition, mathematically identical to
those reported in the main text.
The primary estimates for communication, strategic prompting, initial price, and extended du-
ration (9 rounds) remain statistically insignificant even under these less restrictive inference spec-
ifications. Conversely, when the clustering penalty is removed, the 6-round duration, experiment
disclosure, and the Medium information structure cross the threshold into statistical significance in
the information aggregation OLS (Tables SA.12, SA.14). Similarly, the order of trading is statisti-
cally significant for individual profits under market-level clustering (Tables SA.13, SA.15). Because
HC1 assumes strictly independent observations, ignoring the heavy intra-cluster correlation inher-
ent in our multi-round, agent-based panel data, it produces smaller standard errors. We therefore
interpret these results as evidence that several estimates are sensitive to the assumed correlation
structure rather than as a basis for stronger causal claims.
26We omit the Deception (Ordered Logit) model altogether because we already apply CR1 errors clustered at the
market level in the main paper.
22

Table SA.12: Information Aggregation Without Disclosure (HC1 Standard Errors)
Dependent variable:
Log Error
Mean (OLS) Median (Q50) Tail Risk (Q80)
(1) (2) (3)
Constant 7.548 ∗∗∗ (0.714) 0.018 (0.019) 3.170 ∗∗ (1.138)
Comments Allowed−0.191 (0.265)−0.001 (0.003)−0.000 (0.032)
Duration: 6 Rounds−1.817 ∗∗ (0.639)−0.001 (0.005)−0.057 (0.177)
Duration: 9 Rounds−0.627 (0.677)−0.001 (0.005)−0.028 (0.165)
Strategic Prompt 0.053 (0.487) 0.001 (0.003) 0.000 (0.113)
Medium (t3s110) 2.200 ∗∗∗ (0.573)−0.000 (0.003) 0.038 (1.808)
Hard (t3s111) 5.327 ∗∗∗ (0.730) 0.286 ∗∗ (0.106) 12.470 . (7.451)
Very Hard (t3s111o2ye2) 6.658 ∗∗∗ (0.713) 0.700 ∗∗∗ (0.084) 21.771 ∗∗∗ (4.744)
Initial Error: Low 0.014 (0.493) 0.000 (0.004) 0.000 (0.069)
Initial Error: Medium 0.225 (0.508)−0.000 (0.003)−0.000 (0.063)
Average Intelligence−0.221 ∗∗∗ (0.018)−0.0004 (0.0004)−0.069 ∗∗ (0.025)
Intelligence SD 0.044 (0.060)−0.0003 (0.0003)−0.052 ∗ (0.026)
6 Rounds x Strategic−0.067 (0.639)−0.001 (0.004) 0.000 (0.128)
9 Rounds x Strategic 0.076 (0.676)−0.001 (0.004) 0.028 (0.161)
Medium Struct x Initial Error (Low) 1.309 (0.844)−0.000 (0.005) 0.019 (3.595)
Hard Struct x Initial Error (Low) 0.504 (1.039) 0.032 (0.124) 19.889 (12.267)
Very Hard x Initial Error (Low) 2.861 ∗∗ (1.050) 0.013 (0.167) 10.425 ∗ (5.186)
Medium Struct x Initial Error (Medium)−0.725 (0.803) 0.000 (0.004) 0.019 (1.810)
Hard Struct x Initial Error (Medium)−0.236 (1.047) 0.077 (0.149)−9.945 (12.141)
Very Hard x Initial Error (Medium)−0.337 (1.022)−0.007 (0.083) 10.080 (9.342)
Robust F-Statistic 12.84 ∗∗∗ (df = 19; 1752)
Observations 1,772 1,772 1,772
R2 0.115
Notes: .p<0.1; ∗p<0.05; ∗∗p<0.01; ∗∗∗p<0.001. Q50 and Q80 are quantile regressions. Q50 models
the median log error, whereas Q80 models the upper 20% tail of the log error distribution (the worst-
performing markets). OLS model uses HC1 robust standard errors. Quantile models use bootstrapped
standard errors. All three models use a mixed-contrast specification. Rounds and Structure use treat-
ment contrasts with Round 3 and Structure t3s111y2 as baselines. All other controls (Initial Error,
Strategic, Comments) use sum contrasts, where coefficients represent deviations from the grand mean.
23

Table SA.13: Trading Volume and Profits Without Disclosure (HC1 and CR1 Standard Errors)
Dependent variable:
Trading Volume Individual Profits
(1) (2)
Constant 1,795.988 ∗∗∗ (126.550)−80.719 ∗∗∗ (10.174)
Comments Allowed 85.077 ∗ (41.093) 2.723 (3.479)
Duration: 6 Rounds 543.398 ∗∗∗ (83.763) 2.447 (8.182)
Duration: 9 Rounds 1,037.835 ∗∗∗ (106.092)−5.396 (8.482)
Strategic Prompt−65.396 (53.805)−0.491 (5.302)
Medium (t3s110) 308.391 ∗∗ (114.608)−30.548 ∗∗∗ (7.264)
Hard (t3s111) 128.183 (119.400)−69.955 ∗∗∗ (8.990)
Very Hard (t3s111o2ye2) 55.372 (118.947)−98.904 ∗∗∗ (9.678)
Initial Error: Low−180.641 (115.824)−10.767 ∗ (5.326)
Initial Error: Medium−14.704 (120.252)−4.386 (5.892)
Average Intelligence−27.925 ∗∗∗ (2.657)−11.019 ∗∗∗ (1.423)
Individual Intelligence 14.079 ∗∗∗ (1.402)
Intelligence SD 22.347 ∗∗∗ (6.159) 0.606 (0.638)
Trades Second−42.127 ∗∗ (13.506)
Trades Third 77.390 ∗∗∗ (10.973)
6 Rounds x Strategic 9.810 (83.760)−1.725 (8.181)
9 Rounds x Strategic 87.983 (106.100)−3.680 (8.474)
Medium Struct x Initial Error (Low) 273.357 . (159.892)−21.173 . (11.208)
Hard Struct x Initial Error (Low) 87.880 (165.985)−13.015 (13.145)
Very Hard x Initial Error (Low) 414.759 ∗ (166.635)−32.672 ∗ (13.956)
Medium Struct x Initial Error (Med) 41.568 (162.442) 4.394 (10.453)
Hard Struct x Initial Error (Med) 62.984 (172.088) 11.491 (12.328)
Very Hard x Initial Error (Med)−238.720 (161.232)−1.778 (14.261)
Robust F-Statistic 14.158 ∗∗∗ (df = 19; 1752) 21.293 ∗∗∗ (df = 22; 5293)
Observations 1,772 5,316
R2 0.104 0.060
Notes: .p<0.1; ∗p<0.05; ∗∗p<0.01; ∗∗∗p<0.001. Model 1 (market-level) utilizes HC1 heteroskedasticity-
consistent robust standard errors. Model 2 (trader-level) utilizes CR1 cluster-robust standard errors
clustered at the market level to account for intra-market profit correlation across competing agents.
Rounds, Information Structure, and Trader Position (Model 2 only) use treatment contrasts, with
‘Round 3’, ‘t3s111y2’ (Easy), and ‘Trades First’ serving as their respective baselines. All other controls
use sum contrasts, representing deviations from the grand mean.
24

Table SA.14: Information Aggregation With Disclosure (HC1 Standard Errors)
Dependent variable:
Log Error
Mean (OLS) Median (Q50) Tail Risk (Q80)
(1) (2) (3)
Constant 7.196 ∗∗∗ (0.678) 0.018 ∗ (0.008) 5.638 ∗∗∗ (0.954)
Comments Allowed−0.318 (0.194)−0.001 (0.001)−0.014 (0.038)
Duration: 6 Rounds−1.550 ∗∗∗ (0.469)−0.001 (0.001)−0.107 (0.112)
Duration: 9 Rounds−0.328 (0.492)−0.001 (0.001)−0.019 (0.086)
Strategic Prompt 0.007 (0.353) 0.001 (0.001) 0.007 (0.064)
Medium (t3s110) 2.772 ∗∗∗ (0.436)−0.00001 (0.001) 0.075 (0.971)
Hard (t3s111) 5.222 ∗∗∗ (0.528) 0.206 ∗ (0.093) 11.809 . (6.577)
Very Hard (t3s111o2ye2) 7.192 ∗∗∗ (0.521) 0.697 ∗∗∗ (0.024) 20.126 ∗∗∗ (5.325)
Initial Error: Low 0.123 (0.379) 0.00000 (0.001) 0.008 (0.046)
Initial Error: Medium 0.234 (0.386)−0.00001 (0.001)−0.003 (0.048)
Experiment Disclosure 2.075 ∗ (0.929)−0.00004 (0.008) 0.980 (4.638)
Average Intelligence−0.218 ∗∗∗ (0.018)−0.0004 ∗ (0.0002)−0.123 ∗∗∗ (0.021)
Intelligence SD−0.012 (0.043)−0.0003 ∗∗ (0.0001)−0.102 ∗∗∗ (0.020)
6 Rounds x Strategic−0.083 (0.469)−0.001 (0.001)−0.021 (0.093)
9 Rounds x Strategic 0.182 (0.492)−0.001 (0.001) 0.014 (0.084)
Medium Struct x Init. Error (Low) 0.657 (0.631)−0.00000 (0.001) 0.003 (1.897)
Hard Struct x Init. Error (Low) 0.120 (0.751) 0.045 (0.097)−8.149 (11.199)
Very Hard x Init. Error (Low) 1.665 ∗ (0.757) 0.008 (0.047) 9.638 ∗ (4.721)
Medium Struct x Init. Error (Med)−0.399 (0.619) 0.00001 (0.001) 0.006 (0.957)
Hard Struct x Init. Error (Med) 0.187 (0.765)−0.077 (0.130) 18.273 (11.427)
Very Hard x Init. Error (Med)−0.321 (0.746)−0.004 (0.024) 8.923 (6.687)
Disclosure x Av. Intelligence−0.053 . (0.028) 0.00000 (0.0002)−0.023 (0.109)
Robust F-Statistic 23.324 ∗∗∗ (df = 21; 3478)
Observations 3,500 3,500 3,500
R2 0.119
Notes: .p<0.1; ∗p<0.05; ∗∗p<0.01; ∗∗∗p<0.001. Q50 and Q80 are quantile regressions. Q50 models
the median log error, whereas Q80 models the upper 20% tail of the log error distribution (the worst-
performing markets). OLS model uses HC1 robust standard errors. Quantile models use bootstrapped
standard errors. All three models use a mixed-contrast specification. Rounds, Structure, and Ex-
periment Disclosure use treatment contrasts with Round 3, Structure t3s111y2, and No Disclosure as
baselines. All other controls (Initial Error, Strategic, Comments) use sum contrasts, where coefficients
represent deviations from the grand mean.
25

Table SA.15: Trading Volume and Agent Profitability With Disclosure (HC1 and CR1 Standard
Errors)
Dependent variable:
Trading Volume Individual Profits
(1) (2)
Constant 1,757.638 ∗∗∗ (111.920)−77.335 ∗∗∗ (9.855)
Comments Allowed 36.269 (29.192) 3.552 (2.501)
Duration: 6 Rounds 563.399 ∗∗∗ (59.237) 3.359 (5.635)
Duration: 9 Rounds 1,080.922 ∗∗∗ (74.985)−12.727 ∗ (6.256)
Strategic Prompt−37.028 (37.713)−0.345 (3.769)
Medium (t3s110) 316.783 ∗∗∗ (80.555)−35.852 ∗∗∗ (5.418)
Hard (t3s111) 212.977 ∗ (84.670)−71.160 ∗∗∗ (6.670)
Very Hard (t3s111o2ye2) 43.866 (83.509)−101.644 ∗∗∗ (6.698)
Initial Error: Low−145.678 . (79.281)−12.168 ∗∗ (4.122)
Initial Error: Medium 44.294 (87.228)−5.193 (4.473)
Experiment Disclosure 171.986 (133.412)−21.052 (13.080)
Average Intelligence−28.182 ∗∗∗ (2.715)−11.057 ∗∗∗ (1.052)
Individual Intelligence 14.091 ∗∗∗ (1.019)
Intelligence SD 24.293 ∗∗∗ (4.342) 1.154 ∗ (0.458)
Trades Second−39.316 ∗∗∗ (9.748)
Trades Third 74.604 ∗∗∗ (8.064)
6 Rounds x Strategic−26.283 (59.237)−0.524 (5.634)
9 Rounds x Strategic 45.471 (74.986)−5.343 (6.253)
Medium Struct x Initial Error (Low) 166.553 (111.310)−9.165 (7.934)
Hard Struct x Initial Error (Low) 69.433 (116.184)−6.278 (9.572)
Very Hard x Initial Error (Low) 349.973 ∗∗ (117.514)−18.174 . (9.513)
Medium Struct x Initial Error (Med)−28.194 (117.353) 2.954 (7.820)
Hard Struct x Initial Error (Med) 93.975 (125.327) 2.619 (9.608)
Very Hard x Initial Error (Med)−252.898 ∗ (116.905) 1.676 (9.699)
Disclosure x Average Intelligence−3.394 (3.917) 0.493 (0.394)
Robust F-Statistic 27.855 ∗∗∗ (df = 21; 3478) 38.592 ∗∗∗ (df = 24; 10475)
Observations 3,500 10,500
R2 0.110 0.059
Notes: .p<0.1; ∗p<0.05; ∗∗p<0.01; ∗∗∗p<0.001. Model 1 (Market Level) reports HC1
heteroskedasticity-consistent robust standard errors. Model 2 (Individual Level) reports CR1 cluster-
robust standard errors clustered at the market level to account for intra-market correlation among
competing traders. Rounds, Information Structure, Experiment Disclosure, and Trader Position use
treatment contrasts, with ‘Round 3’, ‘t3s111y2’, No Disclosure, and ‘Trades First’ serving as their
respective baselines. All other controls (Initial Error, Strategic, Comments) use sum contrasts, where
coefficients represent deviations from the grand mean. Both specifications report adjusted robust Wald
F-statistics.
26

Table SA.16: Agent Communication Strategy: Text Similarity and Word Gap (CR1 Standard
Errors)
Dependent variable:
Cosine Similarity (OLS) Word Gap (OLS)
(1) (2)
Constant 0.324 ∗∗∗ (0.009) 33.880 ∗∗∗ (2.495)
Strategic Prompt−0.003 (0.003) 0.788 (0.769)
Round 2 0.030 ∗∗∗ (0.004)−13.194 ∗∗∗ (1.129)
Round 3 0.004 (0.004)−25.105 ∗∗∗ (1.228)
Round 4 0.030 ∗∗∗ (0.005)−12.247 ∗∗∗ (1.284)
Round 5 0.040 ∗∗∗ (0.005)−23.619 ∗∗∗ (1.272)
Round 6 0.005 (0.005)−30.972 ∗∗∗ (1.318)
Round 7 0.038 ∗∗∗ (0.006)−18.893 ∗∗∗ (1.426)
Round 8 0.047 ∗∗∗ (0.006)−26.708 ∗∗∗ (1.455)
Round 9 0.033 ∗∗∗ (0.006)−32.644 ∗∗∗ (1.436)
Duration: 6 Rounds 0.002 (0.007)−0.468 (2.072)
Duration: 9 Rounds−0.002 (0.007)−1.072 (2.077)
Medium (t3s110)−0.022 ∗∗ (0.007)−1.213 (2.021)
Hard (t3s111) 0.002 (0.007) 2.417 (2.204)
Very Hard (t3s111o2ye2) 0.001 (0.007) 5.666 ∗ (2.264)
Experiment Disclosure 0.010 . (0.005) 14.858 ∗∗∗ (1.543)
Initial Error 0.002 (0.016) 2.867 (4.688)
Individual Intelligence 0.001 ∗∗∗ (0.0002) 0.844 ∗∗∗ (0.043)
Observations 10,620 10,620
R2 0.027 0.156
F Statistic (df = 17; 10602) 17.560 ∗∗∗ 115.223∗∗∗
Notes: .p<0.1; ∗p<0.05; ∗∗p<0.01; ∗∗∗p<0.001. All models use a mixed-contrast specification. Treat-
ment contrast baselines are: Round 1 for Round, 3 Rounds for Duration, Easy (t3s111y2) for Structure,
and No Disclosure for Experiment Disclosure. The Strategic Prompt variable uses sum contrasts, rep-
resenting the deviation from the grand mean, whereas Initial Error is mean-centered. Both models
report CR1 cluster-robust standard errors in parentheses, clustered at the market level to account for
intra-market correlation across competing agents and repeated communication rounds.
27

Table SA.17: Robustness Check: Cosine Similarity by Market Duration (CR1 Standard Errors)
Dependent variable:
Cosine Similarity (Public, Private)
3-Round 6-Round 9-Round
(1) (2) (3)
Constant 0.331 ∗∗∗ (0.015) 0.311 ∗∗∗ (0.012) 0.329 ∗∗∗ (0.012)
Strategic Prompt−0.004 (0.005)−0.003 (0.004)−0.003 (0.004)
Round 2 0.025 ∗∗∗ (0.006) 0.033 ∗∗∗ (0.007) 0.032 ∗∗∗ (0.007)
Round 3 0.005 (0.007) 0.005 (0.007) 0.003 (0.007)
Round 4 0.029 ∗∗∗ (0.007) 0.032 ∗∗∗ (0.007)
Round 5 0.042 ∗∗∗ (0.007) 0.039 ∗∗∗ (0.007)
Round 6 0.009 (0.007) 0.003 (0.007)
Round 7 0.039∗∗∗ (0.007)
Round 8 0.047∗∗∗ (0.007)
Round 9 0.032∗∗∗ (0.007)
Medium (t3s110)−0.017 (0.014)−0.015 (0.012)−0.029 ∗∗ (0.011)
Hard (t3s111)−0.006 (0.015) 0.012 (0.012)−0.001 (0.011)
Very Hard (t3s111o2ye2) 0.001 (0.015) 0.005 (0.012)−0.001 (0.011)
Experiment Disclosure 0.004 (0.010) 0.011 (0.009) 0.011 (0.008)
Initial Error 0.009 (0.031) 0.001 (0.025) 0.001 (0.024)
Individual Intelligence 0.001 ∗ (0.0004) 0.001 ∗∗∗ (0.0003) 0.001 ∗∗ (0.0003)
Observations 1,776 3,552 5,292
R2 0.015 0.034 0.029
Adjusted R2 0.010 0.030 0.026
F Statistic 2.919 ∗∗ (df = 9; 1766) 10.269 ∗∗∗ (df = 12; 3539) 10.390 ∗∗∗ (df = 15; 5276)
Notes: .p<0.1; ∗p<0.05; ∗∗p<0.01; ∗∗∗p<0.001. CR1 cluster-robust standard errors are reported in
parentheses, clustered at the market level to account for intra-market correlation across multiple mes-
saging rounds. The model uses a mixed-contrast specification. Treatment contrast baselines are: Round
1for Round, Easy (t3s111y2)forStructure, andNo DisclosureforExperimentDisclosure. TheStrategic
Prompt variable uses sum contrasts, representing the deviation from the grand mean, whereas Initial
Error is mean-centered.
28

Table SA.18: Robustness Check: Word Gap by Market Duration (CR1 Standard Errors)
Dependent variable:
Word Gap
3-Round Markets 6-Round Markets 9-Round Markets
(1) (2) (3)
Constant 31.127 ∗∗∗ (4.020) 35.468 ∗∗∗ (3.612) 32.393 ∗∗∗ (3.234)
Strategic Prompt 0.682 (1.533) 0.114 (1.282) 1.282 (1.173)
Round 2−13.385 ∗∗∗ (2.072)−12.328 ∗∗∗ (1.942)−13.802 ∗∗∗ (1.876)
Round 3−24.149 ∗∗∗ (2.185)−25.950 ∗∗∗ (2.128)−24.945 ∗∗∗ (2.082)
Round 4−12.730 ∗∗∗ (1.861)−11.833 ∗∗∗ (1.884)
Round 5−23.211 ∗∗∗ (2.012)−24.144 ∗∗∗ (1.943)
Round 6−31.712 ∗∗∗ (2.154)−30.467 ∗∗∗ (1.984)
Round 7 −18.861∗∗∗ (1.731)
Round 8 −26.700∗∗∗ (1.945)
Round 9 −32.712∗∗∗ (1.966)
Medium (t3s110)−2.959 (4.020)−3.839 (3.378) 1.157 (3.080)
Hard (t3s111) 0.958 (4.548)−0.100 (3.755) 4.582 (3.296)
Very Hard (t3s111o2ye2) 3.865 (4.419) 4.459 (3.765) 7.073 ∗ (3.474)
Experiment Disclosure 12.640 ∗∗∗ (3.068) 15.753 ∗∗∗ (2.582) 14.981 ∗∗∗ (2.353)
Initial Error 2.330 (9.170) 2.005 (7.834) 3.618 (7.168)
Individual Intelligence 1.050 ∗∗∗ (0.085) 0.813 ∗∗∗ (0.071) 0.796 ∗∗∗ (0.066)
Observations 1,776 3,552 5,292
R2 0.143 0.152 0.159
Adjusted R2 0.139 0.149 0.157
F Statistic 32.824 ∗∗∗ (df = 9; 1766) 52.842 ∗∗∗ (df = 12; 3539) 66.700 ∗∗∗ (df = 15; 5276)
Notes: .p<0.1; ∗p<0.05; ∗∗p<0.01; ∗∗∗p<0.001. CR1 cluster-robust standard errors are reported in
parentheses, clustered at the market level to account for intra-market correlation across multiple mes-
saging rounds. The model uses a mixed-contrast specification. Treatment contrast baselines are: Round
1for Round, Easy (t3s111y2)forStructure, andNo DisclosureforExperimentDisclosure. TheStrategic
Prompt variable uses sum contrasts, representing the deviation from the grand mean, whereas Initial
Error is mean-centered.
29

SA.10 Prompts
In this section, we provide excerpts from the prompts that are given to the AI agents. The following
describes the public and private information that is provided to each agent in the four structures.
In the Supplementary appendix we provide the full prompt for one market.
SA.10.1 t3s111y2
Public Information: "The prediction market question has two answers: Yes and No. There are
three relevant dimensions to this prediction market question: dimension d_a: Will sales in country
A exceed 1 million? dimension d_b: Will sales in country B exceed 1 million? dimension d_c:
Will sales in country C exceed 1 million? The answer to each dimension is either true, with
probability 0.5, or false, with probability 0.5. Dimensions are independent, hence the probability
of a dimension d resolving to true is independent of whether the other dimensions resolve to true
or false. In summary, there are eight states of the world, depending on whether d_a, d_b, or d_c
are true or false. The answer to the prediction market question of whether the profits of Company
X will exceed 1 million is Yes if at least two dimensions (d_a,d_b,d_c) resolve to true. If more
than one dimension resolves to false, then the answer to the question is No. There are three traders
in the market. trader_1 is privately informed whether d_a is true or not, Trader_2 is privately
informed whether d_b is true or not, and Trader_3 is privately informed whether d_c is true or
not. All three traders assign the same prior probabilities to each dimension resolving to true or
false."
Private Information: trader_1: "A true state has now occurred. You (trader_1) are now
informed truthfully and privately that d_a is true." trader_2: "A true state has now occurred.
You (trader_2) are now informed truthfully and privately that d_b is true." trader_3: "A true
state has now occurred. You (trader_3) are now informed truthfully and privately that d_c is
true."
SA.10.2 t3s111
Public Information: The prediction market question has two answers: Yes and No. There are
three relevant dimensions to this prediction market question: dimension d_a: Will sales in country
A exceed 1 million? dimension d_b: Will sales in country B exceed 1 million? dimension d_c:
Will sales in country C exceed 1 million? The answer to each dimension is either true, with
probability 0.5, or false, with probability 0.5. Dimensions are independent, hence the probability
of a dimension d resolving to true is independent of whether the other dimensions resolve to true
or false. In summary, there are eight states of the world, depending on whether d_a, d_b, or d_c
are true or false. The answer to the prediction market question of whether the profits of Company
X will exceed 1 million is Yes if all three dimensions (d_a,d_b,d_c) resolve to true. If at least one
dimension resolves to false, then the answer to the question is No. There are three traders in the
market. Trader_1 is privately informed whether d_a is true or not, Trader_2 is privately informed
whether d_b is true or not, and Trader_3 is privately informed whether d_c is true or not. All
three traders assign the same prior probabilities to each dimension resolving to true or false.
Private Information: trader_1: "A true state has now occurred. You (trader_1) are now
informed truthfully and privately that d_a is true." trader_2: "A true state has now occurred.
You (trader_2) are now informed truthfully and privately that d_b is true." trader_3: "A true
30

state has now occurred. You (trader_3) are now informed truthfully and privately that d_c is
true."
SA.10.3 t3s110
Public Information: "The prediction market question has two answers: Yes and No. There are
three relevant dimensions to this prediction market question: dimension d_a: Will sales in country
A exceed 1 million? dimension d_b: Will sales in country B exceed 1 million? dimension d_c:
Will sales in country C exceed 1 million? The answer to each dimension is either true, with
probability 0.5, or false, with probability 0.5. Dimensions are independent, hence the probability
of a dimension d resolving to true is independent of whether the other dimensions resolve to true
or false. In summary, there are eight states of the world, depending on whether d_a, d_b, or d_c
are true or false. The answer to the prediction market question of whether the profits of Company
X will exceed 1 million is Yes if all three dimensions (d_a,d_b,d_c) resolve to true. If at least one
dimension resolves to false, then the answer to the question is No. There are three traders in the
market. Trader_1 is privately informed whether d_a is true or not, Trader_2 is privately informed
whether d_b is true or not, and Trader_3 is privately informed whether d_c is true or not. All
three traders assign the same prior probabilities to each dimension resolving to true or false."
Private Information: trader_1: "A true state has now occurred. You (trader_1) are now
informed truthfully and privately that d_a is true." trader_2: "A true state has now occurred.
You (trader_2) are now informed truthfully and privately that d_b is true." trader_3: "A true
state has now occurred. You (trader_3) are now informed truthfully and privately that d_c is
false."
SA.10.4 t3s111o2ye2
Public Information: "The prediction market question has two answers: Yes and No. There are
three relevant dimensions to this prediction market question: dimension d_a: Will sales in country
A exceed 1 million? dimension d_b: Will sales in country B exceed 1 million? dimension d_c:
Will sales in country C exceed 1 million? The answer to each dimension is either true, with
probability 0.5, or false, with probability 0.5. Dimensions are independent, hence the probability of
a dimension d resolving to true is independent of whether the other dimensions resolve to true or
false. In summary, there are eight states of the world, depending on whether d_a, d_b, or d_c are
true or false. The answer to the prediction market question of whether the profits of Company X
will exceed 1 million is Yes if exactly two of the three dimensions (d_a,d_b,d_c) resolve to true. If
all three dimensions resolve to true, or at least two dimensions resolve to false, then the answer to
the question is No. There are three traders in the market. Trader_1 is privately informed whether
d_b and d_c are true or not, Trader_2 is privately informed whether d_a and d_c are true or
not, and Trader_3 is privately informed whether d_a and d_b are true or not. All three traders
assign the same prior probabilities to each dimension resolving to true or false."
Private Information: trader_1: "A true state has now occurred. You (trader_1) are now
informed truthfully and privately that d_b and d_c are true." trader_2: "A true state has now
occurred. You (trader_2) are now informed truthfully and privately that d_a and d_c are true."
trader_3: "Atruestatehasnowoccurred. You(trader_3)arenowinformedtruthfullyandprivately
that d_a and d_b are true."
31

SA.10.5 Full prompt in a round
The following is part of the report that was generated for market with slug ‘5gw55w’, describing
the prompt which is sent to the trader in Round 4, their actions and the execution of the trades.
The complete report for this market, containing every prompt, every private and public message,
and every trade, is included in the replication package.
Note that the public and private information, as well as the explanation of what is a prediction
market, are repeated in every round, as a “new” LLM is invoked in every round. This is similar
to the case where a user chats with an LLM. Since the LLM has no memory, it reads the entire
transcript of the conversation every time it is called to answer. The prompt also includes a history
of prices and public messages, the private messages of the previous iterations of the same trader,
a calculation of the price impact from various trades, and a report of the current portfolio of the
trader.
32

You are trader_1, a participant in the following prediction market.

=== PREDICTION MARKET ===
Question: Will Company X post next quarter profits that exceed 1 million?
Description:
Comments allowed: Yes
Current Round: 4
Total Rounds in the Market: 6
Participants: trader_1, trader_2, trader_3

Participants trade sequentially and in the order specified above. After
the last participant trades, the first participant trades again, and so
on, until we reach the last round and the market ends. The other
participants in this prediction market are: trader_2, trader_3.

Public Information: The prediction market question has two answers: Yes
and No. There are three relevant dimensions to this prediction market
question: dimension d_a: Will sales in country A exceed 1 million?
dimension d_b: Will sales in country B exceed 1 million? dimension d_c:
Will sales in country C exceed 1 million? The answer to each dimension is
either true, with probability 0.5, or false, with probability 0.5.
Dimensions are independent, hence the probability of a dimension d
resolving to true is independent of whether the other dimensions resolve
to true or false. In summary, there are eight states of the world,
depending on whether d_a, d_b, or d_c are true or false. The answer to
the prediction market question of whether the profits of Company X will
exceed 1 million is Yes if at least two dimensions (d_a,d_b,d_c) resolve
to true. If more than one dimension resolves to false, then the answer to
the question is No. There are three traders in the market. Trader_1 is
privately informed whether d_a is true or not, Trader_2 is privately
informed whether d_b is true or not, and Trader_3 is privately informed
whether d_c is true or not. All three traders assign the same prior
probabilities to each dimension resolving to true or false.

Your Private Information (only shared with you): A true state has now
occurred. You (trader_1) are now informed truthfully and privately that
d_a is true.

Your previous private reasoning (only visible to you):
  [Round 1] I know d_a is true. For the market to resolve Yes, at least 2
of 3 dimensions must be true. Since d_a is true, I need at least 1 more
dimension (d_b or d_c) to be true. The probability of at least one of d_b
or d_c being true is 1 - P(both false) = 1 - 0.25 = 0.75. My true belief
q = 0.75, but current price p = 0.50. This is a significant edge. I
should buy Yes shares aggressively. Buying around 534 shares (50% of max)
will push the price to approximately 0.995, which is still below my true
belief. This aggressive position reflects my informational advantage and
positions me well for future rounds. Other traders will observe this
price movement and may update their beliefs, but my information advantage
should persist through the remaining rounds.

=== What is a prediction market? ===

A prediction market is a platform where participants can buy and sell
shares in the outcome of a specific event, with a binary question that
has two possible outcomes: Yes or No.
The current price of a “Yes” share, denoted p, represents the market’s
current belief that the event will resolve to “Yes.”
For example, if p = 0.65, the market assigns a 65% chance to “Yes” and a
35% chance to “No.”

Rules and reasoning process
Interpret the question.
Understand what “Yes” and “No” mean in this market.
Form your own belief.
Based on the question, historical prices, trader comments, and any
reasoning you can infer, assign your own subjective probability q that
the outcome will be “Yes.”

This market operates on a Logarithmic Market Scoring Rule (LMSR) with a
specific liquidity parameter (beta = 0.01).

The current price of "YES" is determined by comparing the total shares
sold for "YES" against the total shares sold for "NO." Specifically, the
price is the exponential of the "YES" shares divided by the sum of the
exponentials of both "YES" and "NO" shares. Consequently, as the number
of shares held in a specific outcome increases relative to the other, the
price of that outcome rises.

Initial Prices: The market does not always start at a 0.5/0.5 prices for
Yes and No. It may be initialized with "offset" shares to reflect a
specific starting likelihood (e.g., 0.8/0.2) by the market maker, so it
is as if the market maker has bought some Yes or No shares initially.

Cost & Slippage: The cost to purchase shares is not linear (Price ×
Quantity). Instead, it is calculated by measuring the difference in the
market's total cost function before and after the trade. As you buy more
shares of an outcome, the price for each subsequent share incrementally
increases. This phenomenon is known as "price impact" or "slippage."

You can only sell shares you own, and you can only buy shares if you have
enough cash.
Payoffs:
If the final outcome is Yes, each “Yes” share pays 1, each “No” share
pays 0.
If the final outcome is No, each “No” share pays 1, each “Yes” share pays
0.
Market dynamics:
When the price of “Yes” rises, traders are collectively assigning higher
probability to “Yes.”
But beware: some traders may act strategically and try to manipulate
prices.
Use price history and comments to infer whether movements reflect genuine
information or strategic behavior.

=== YOUR OBJECTIVE ===
Use reasoning to determine your belief q, then choose your action (Buy,
Sell, or Hold: Yes and No shares). Maximize the sum of your expected
payoffs over all trading rounds, based on your belief q and the current
price p. Consider how your current trade affects the price and the
beliefs of others in future

rounds.
You will also be asked to provide your reasoning for your decision, which
will be shared privately with you in future rounds where you trade. If
public comments are allowed in the market, you can also post a public
justification for your action that other participants can see.

=== PUBLIC INFORMATION ===
This section contains all publicly available market data, generated by
the participants: trader_1, trader_2, trader_3.

Current Prices
  Yes: £1.00 per share
  No: £0.00 per share

Trade History (oldest first):
trader_1 bought 534 Yes shares, price went from £0.50 to £1.00 on 2026-
01-10 19:13:14
trader_2 bought 500 Yes shares, at £1.00 on 2026-01-10 19:13:59
trader_3 bought 500 Yes shares, at £1.00 on 2026-01-10 19:14:44

Market Comments (3 total, most recent first):
  [2026-01-10 19:14:44] trader_3: I believe the probability of Company X
exceeding 1 million in profits is very high. My analysis indicates a
substantial likelihood of success, and the current market pricing
presents a compelling opportunity. I am taking a significant position in
Yes shares.
  [2026-01-10 19:13:59] trader_2: I believe the probability of Company X
exceeding 1 million in profits is substantially higher than the current
market price reflects. Given the market dynamics and available
information, I am taking a significant position in Yes shares to
capitalize on this opportunity.
  [2026-01-10 19:13:14] trader_1: Based on my analysis, I believe the
probability of Company X exceeding 1 million in profits is significantly
higher than the current market price of 0.50 suggests. I am taking a
substantial position in Yes shares.

=== YOUR CURRENT PORTFOLIO ===
Portfolio for trader_1:
  Cash: £534.84
  Yes: 534 shares (value at current prices: £534.00, payoff: £534.00 if
Yes wins, £0.00 if No wins)
  No: 0 shares (value at current prices: £0.00, payoff: £0.00 if Yes
wins, £0.00 if No wins)
  Total Portfolio Value: £1068.84

Given the current prices and your cash balance, you can afford to buy up
to:

YES shares: 534 (total cost: £534.00)
NO shares: 2068 (total cost: £534.48)

Note: These calculations account for price increases as you buy more
shares.

Maximum sellable shares (based on shares you currently own):

Yes: 534 shares

No: 0 shares

=== PRICE IMPACT OF TRADES ===
This shows how prices would change if you buy or sell shares:

Yes shares:
  Buy 1: £1.000 → £1.000 (+0.0%)
  Buy 5: £1.000 → £1.000 (+0.0%)
  Buy 10: £1.000 → £1.000 (+0.0%)
  Buy 20: £1.000 → £1.000 (+0.0%)
  Buy (around 25% of max buyable) 134: £1.000 → £1.000 (+0.0%)
  Buy (around 50% of max buyable) 267: £1.000 → £1.000 (+0.0%)
  Buy (around 75% of max buyable) 400: £1.000 → £1.000 (+0.0%)
  Buy (max buyable) 534: £1.000 → £1.000 (+0.0%)
  Sell 1: £1.000 → £1.000 (-0.0%)
  Sell 5: £1.000 → £1.000 (-0.0%)
  Sell 10: £1.000 → £1.000 (-0.0%)
  Sell 20: £1.000 → £1.000 (-0.0%)
  Sell (around 25% of max sellable) 134: £1.000 → £1.000 (-0.0%)
  Sell (around 50% of max sellable) 267: £1.000 → £1.000 (-0.0%)
  Sell (around 75% of max sellable) 400: £1.000 → £1.000 (-0.0%)
  Sell (max sellable) 534: £1.000 → £1.000 (-0.0%)

No shares:
  Buy 1: £0.000 → £0.000 (+1.0%)
  Buy 5: £0.000 → £0.000 (+5.1%)
  Buy 10: £0.000 → £0.000 (+10.5%)
  Buy 20: £0.000 → £0.000 (+22.1%)
  Buy (around 25% of max buyable) 517: £0.000 → £0.000 (+17490.8%)
  Buy (around 50% of max buyable) 1034: £0.000 → £0.007 (+3073792.0%)
  Buy (around 75% of max buyable) 1551: £0.000 → £0.542 (+249112376.4%)
  Buy (max buyable) 2068: £0.000 → £0.995 (+457087674.2%)

Note: These are simulations only. Actual prices may vary slightly due to
concurrent trades.

=== TRADING RULES ===
  • You can BUY, SELL, or HOLD
  • The price may change after each share (market impact)
  • You can only buy if you have sufficient cash
  • You can only sell shares you own

=== YOUR DECISION ===
Analyze the market and your portfolio, then respond with a JSON object:
{
  "action": "BUY or SELL or HOLD",
  "instrument_id": "the ID number of the instrument (4702 for Yes, 4703
for No)",
  "size": "number of shares",
  "public_justification": "brief explanation of your reasoning that you
want everyone to know (this will be posted as a market comment visible to
everyone)",
  "private_reasoning": "brief explanation of your reasoning that only you
will see (this will NOT be posted as a comment; it will only be visible
to you in your next turn)"
}

Important: Only output valid JSON. No other text.

----------------------------------------

Decision by trader_1 at 2026-01-10T19:14:52.477159:
  Action: HOLD
  Instrument ID: 4702
  Size: 0 shares
  Public justification: The market price of Yes shares has reached £1.00,
which reflects extremely high confidence in the outcome. I have already
established a substantial position (534 Yes shares) that represents a
significant portion of my portfolio. At this price level, any further
buying would expose me to considerable downside risk if new information
emerges suggesting lower probability of success. The other traders have
also taken large positions, suggesting market consensus has formed. I
will hold my current position and observe how trader_3's information
(dimension d_c) and any subsequent price movements develop before making
additional trades in future rounds.
  Private reasoning: My true belief q = 0.75 based on d_a being true (I
need at least 1 of d_b or d_c to be true). The current price p = 1.00
significantly exceeds my belief. This suggests either: (1) trader_2 and
trader_3 have received positive signals about d_b and d_c respectively,
or (2) they are over-confident based on my large initial buy signal.
Either way, at p = 1.00, there is limited upside and substantial downside
if the outcome resolves to No. My 534 Yes shares already capture
substantial value if my belief is correct (expected payoff: 534 × 0.75 =
400.5). Adding more positions at p = 1.00 would be inefficient risk
allocation. I should hold and preserve optionality for rounds 5 and 6.

*************************************************************************
*******
ROUND 5
*************************************************************************
*******

--- Round 5: trader_2 ---

Portfolio for trader_2:
  Cash: £500.48
  Instrument 4702 (Yes): 500.0 shares
  Instrument 4703 (No): 0.0 shares

Prompt sent to trader_2:
----------------------------------------
You are trader_2, a participant in the following prediction market.

=== PREDICTION MARKET ===
Question: Will Company X post next quarter profits that exceed 1 million?
Description:
Comments allowed: Yes
Current Round: 5
Total Rounds in the Market: 6
Participants: trader_1, trader_2, trader_3

Participants trade sequentially and in the order specified above. After
the last participant trades, the first participant trades again, and so
on, until we reach the last round and the market ends. The other
participants in this prediction market are: trader_1, trader_3.
