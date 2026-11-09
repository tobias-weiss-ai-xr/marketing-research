---
title: 'CSTrader: A Testbed for Language-Grounded Trading in a Community-Driven Virtual Asset Market'
url: https://arxiv.org/abs/2606.31461
category: ai-marketing
subcategory: empirical
date: 2026-06
venue: ''
authors:
- Yao Shi
- Kingfung Luo
- Nan Tang
- Yuyu Luo
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.31461
pages: 19
chars: 67667
fetched_at: '2026-11-08T13:03:21+00:00'
kb_version: 1
---

# CSTrader: A Testbed for Language-Grounded Trading in a Community-Driven Virtual Asset Market

CSTrader: A Testbed for Language-Grounded Trading in a
Community-Driven Virtual Asset Market
Yao SHI*† Kingfung Luo*† Nan Tang† Yuyu Luo†
Abstract
Niche asset markets, such as Counter-Strike 2
(CS2) weapon skins, are small, volatile, and
heavily driven by community discussions and
platform rules. These properties make them
hard for traditional quantitative models, but
provide an ideal testbed for studying how large
language models (LLMs) turn unstructured text
into trading actions. We present CSTrader, a
multi-agent framework for language-grounded
trading in the CS2 skin market. The system
first integrates heterogeneous signals from var-
ious sources, then uses specialized agents for
technical analysis, liquidity, events, and (re-
versed) sentiment, and finally applies risk con-
trol, transaction friction, and portfolio manage-
ment agents to produce buy, sell, or hold deci-
sions under realistic trading frictions. We build
a live-like evaluation environment with real
CS2 data from a highly volatile period and eval-
uate several recent LLM backbones. Across
models, CSTrader consistently outperforms
both a falling market index (-15.62%) and sim-
ple single-prompt LLM baselines, achieving
up to a 7.58% cumulative return with con-
trolled risk. Ablation studies show that liquid-
ity, reversed sentiment, and transaction friction
agents are crucial for turning noisy language
signals into stable profits, suggesting that niche,
language-driven markets are a useful bench-
mark for future language-to-action research.
Code is available at: https://github.com/
IatomicreactorI/CSGOTrading
1 Introduction
The Appeal of Niche Assets.Many niche as-
sets provide high investment returns. Examples
include Non-Fungible Tokens (NFTs) (Wang et al.,
2021) and collectibles (Valeonti et al., 2021). These
assets usually have high volatility and low trad-
ing volumes. Prices depend heavily on news and
*Equal contribution.
†Hong Kong University of Science and Technology
(Guangzhou).
the behavior of a small group of investors, and
they have specific rules such as high transaction
fees and “trade lock” periods. Skins in the game
Counter-Strike 2 (CS2) are a typical example of
this asset class (Hardenstein, 2017), with a large,
retail-driven market that remains underanalyzed
by institutional investors (Greer et al., 2019). An
overview of the CS2 skin market, including its
scale, asset categories, and trading mechanisms is
provided in Appendix A.
LLMs for Trading.Recent progress in large lan-
guage models (LLMs) has changed financial anal-
ysis through better document understanding and
decision-making capabilities (Liu et al., 2023; Wu
et al., 2024; Yu et al., 2024b). Traditional machine
learning (ML) is good at forecasting time-series
data, but LLMs can interpret earnings calls, pol-
icy news, and market sentiment. Researchers have
used LLMs for financial statements and stock trad-
ing (Kim et al., 2024; Li et al., 2024a; Xiao et al.,
2024). Multi-agent trading systems have shown
good results in several financial markets (Li et al.,
2025a; Berti et al., 2025; Wang et al., 2024b; Li
et al., 2025b). However, most of these systems fo-
cus on traditional stock markets. This leaves niche
assets in real-world trading scenarios mostly ig-
nored. The CS2 market has not received enough
attention in LLM-based trading research.
Challenges of Niche Assets Trading.Trading
CS2 skins is different from trading stocks. Most
trades are driven by game updates and social-
mediated sentiment on platforms like Reddit.
These assets often have low liquidity, which means
prices can change quickly with small trades (Greer
et al., 2019; Hardenstein, 2017; Martinelli, 2017).
Effective trading in this market requires a mix of
cross-domain reasoning and strategies that are sen-
sitive to specific platform rules. Traditional stock
trading approaches often lack these capabilities. At
the same time, these properties make the CS2 mar-
arXiv:2606.31461v1  [cs.AI]  30 Jun 2026

Before After
LLMs
Signals
Multi-Agent
...
...
Info Perception Layer
Real Time
Market
Social Media
Official
Events
Reasoning Layer
Operation Layer
CSTrader
Figure 1: Overview of CSTrader. Our framework takes heterogeneous signals (real-time market prices, social media
discussions, and official events) as inputs to a structured multi-agent LLM system, and turns them into trading
decisions that significantly improve portfolio performance in the CS2 skin market.
ket an ideal stress test for the ability of models to
connect unstructured text, platform rules, and nu-
merical price dynamics in real-time environment.
Limitations of Existing Methods.Current ap-
proaches have three main limitations when dealing
with niche assets.
• Traditional ML-based methods focus only on
historical price movements. They ignore the
“patch notes” and community events that drive
the CS2 market.
• LLM-based methods (Ko and Lee, 2024;
Wang et al., 2024a) can analyze events, but
they struggle with integrated decision-making.
They do not account for the specific rules
of niche asset markets, such as high fees or
“trade lock” periods, which leads to poor be-
havior in markets like CS2.
• Backtesting methods often lack realism.
Many systems use historical data in a way that
allows “cheating”. A trading system needs to
run in a real-world environment to prove it is
effective.
Rethinking.Neither traditional ML nor single
LLMs satisfy the three requirements for CS2 trad-
ing: processing diverse data, making adaptive deci-
sions under high volatility, and managing portfolio-
level risk. These problems are especially serious
during periods of market stress. Instead of propos-
ing yet another domain-specific method, we view
the CS2 skin market as an idea testbed for language-
grounded decision making. Our goal is to build
a realistic, online-like evaluation environment in
which different LLM-based trading agents can be
deployed under the same market frictions and data
streams and compared fairly. This perspective leads
to the following research question:How should
we design such an evaluation framework, and
what kinds of LLM-based agents can effectively
exploit language signals in this setting?
Our Proposal.We address this question by build-
ing a realistic evaluation framework for language-
driven trading, instantiated on the CS2 skin mar-
ket, and by using it to systematically test different
trading agents. An overview of the our CSTrader
concept is shown in Figure 1. Our approach has
three components:
• Language-driven market as testbed:We se-
lect the CS2 skin market as a representative
language-driven niche asset market, integrate
price time series with community and plat-
form text, and expose them as a unified stream
of observations that preserves real-world con-
straints such as fees and trade locks.
• Flexible evaluation environment:We design
an environment interface that is agnostic to the
internal architecture of the trading agent. In
this work, we instantiate it with single-prompt
LLM baselines and a structured multi-agent
LLM policy, while keeping the interface ex-
tensible to other model classes.
• A structured multi-agent LLM policy:As a
concrete instantiation, we develop CSTrader,
a multi-agent LLM policy that decomposes
perception, reasoning, and risk-aware portfo-
lio control into interacting agents; CSTrader

serves as a strong, interpretable baseline
within our framework.
Although our framework is instantiated on CS2,
the same design applies to other language-driven
asset classes such as NFTs and collectibles.
Contributions.The design of CSTrader and the
surrounding framework addresses the unique chal-
lenges of language-driven, niche markets and aims
to provide insights that go beyond a single applica-
tion. Our main contributions are:
• A realistic evaluation framework for
language-grounded trading.We frame
language-driven markets such as CS2 skins
as testbeds for language-grounded decision
making and build an environment that
streams heterogeneous textual and numerical
signals while enforcing real-world frictions
(transaction fees and trade-lock rules).
• A structured multi-agent LLM baseline.
Within this framework, we propose CSTrader,
a multi-agent LLM trading policy that struc-
tures language understanding, market reason-
ing, and risk control into interacting agents
with explicit natural-language rationales.
• Superior performance on real-world CS2
market data.We conduct experiments on real
CS2 skin market data during a highly volatile
period and show that our structured multi-
agent LLM agents consistently outperform
both the overall market index (which declines
by15.62%) and simple single-prompt LLM
baselines, achieving up to a7.58%cumulative
return with controlled volatility.
2 Methodology
Our system design takes inspiration from the The-
ory of Reflexivity introduced by George Soros.
This theory suggests that the biases of market par-
ticipants and the actual market events create a feed-
back loop where each influences the other. This is
particularly relevant for the CS2 skin market be-
cause prices are often driven by social trends and
community hype rather than just physical utility.
By monitoring both the “market echoes” on social
media and the “hard data” from official updates,
our framework attempts to navigate this feedback
loop. An overview of the three-tier architecture is
shown in Figure 2.
The architecture consists of a three-tier frame-
work. The Information Perception Layer col-
lects and cleans heterogeneous data from multiple
sources. The Reasoning Layer employs different
agents to analyze the market from technical, social,
and event-based perspectives. Finally, the Opera-
tion Layer acts as the core of the system by inte-
grating these insights with a memory mechanism
to execute trades.
2.1 Information Perception Layer
This layer captures diverse data streams to ensure
that all trading decisions are based on the most
recent market evidence. The collected information
is cleaned and transformed into standardized inputs
for the Reasoning Layer 2.2.
We categorize the output of this layer into three
data types: (1)market price data, consisting of
daily OHLCV(Open, High, Low, Close, V olume)
records for target assets; (2)community sentiment
text, formed by unstructured discussions from so-
cial platforms such as Reddit; and (3)official event
news, including Steam announcements and game
updates that may affect supply and demand. Imple-
mentation details and data schemas are provided in
the appendix.
2.2 Reasoning Layer
This layer uses five specialized agents to provide
multi-dimensional analysis. Each agent produces a
standardized signal, such as “Bullish”, “Bearish”,
or “Neutral”, along with a short natural-language
justification.
Technical Agent:The Technical Agent summarizes
price behavior using trend, mean-reversion, mo-
mentum, volatility, and volume-level indicators to
forecast short- and medium-term movements. Con-
cretely, it combines exponential moving averages,
Bollinger-band style mean reversion, RSI-type mo-
mentum, volatility regimes, and support/resistance
levels; full formulas and hyperparameters are given
in the appendix.
Sentiment Agent: The Sentiment Agent reads Red-
dit discussions from CS2 trading forums and con-
verts them into a short-term sentiment signal for
each skin. It selects high-quality, recent posts for
the target ticker and returns a bullish, bearish, or
neutral view together with an explanation when
data is sparse or noisy.
Reversed Sentiment Agent: To capture herd effects,
the Reversed Sentiment Agent applies a contrar-

Market Data
Community
Sentiment Text
Official Event News
(Steam Updates)
API Data
API Data
 Web Scraping Data
Data Processing &
Encapsulation
Technical
Agent
(Multi-Agent Analysis)
(Autonomous Decision)
Sentiment
Agent
Reversed
Sentiment
Agent
Liquidity
Agent
Event
Agent
?
TIER1: Information Perception Layer TIER2: Reasoning Layer
TIER3: Operation Layer
Agent Signals
Bullish
Neutral
Bearish
Positive
Negative
 Negative
Portfolio Management Agent
Positive
Safe
Unsafe
Positive
Negative
(Final Decision Maker)
HOLDSELLBUY
DecisionFinal
ORChoose 4  Reasoning Agents for Analysis
Risk Control Agent
Portfoli o
History
Updat e
Portfolio
Decision
Memory
Transaction Friction Agent
Decision &  Analysis Record Stored
Decisions
History
Agent
Reasonin g
History
Dat a
History
Risk Level :
0. 1 to 1 .0
Risk Level :
0. 1 to 1 .0
2 %  Friction
Recent Trading History
Neutral
 Neutral
 Neutral
 Neutral
Figure 2: Architecture of CSTrader. The framework is organized into three tiers: TIER1: an Information Perception
Layer that aggregates market, community, and official event data into standardized inputs; TIER2: a Reasoning
Layer where multiple specialized agents (technical, liquidity, event, sentiment, and reversed sentiment) produce
discrete signals with justifications; and TIER3: an Operation Layer that uses risk control, transaction friction, and
portfolio management agents with decision memory to integrate these signals into final buy, sell, or hold actions.
ian lens to the standard sentiment output: strong
optimism can signal an overheated market, while
widespread pessimism can indicate undervaluation.
This agent therefore often inverts community mood,
helping CSTrader avoid buying into bubbles and
exploit overreactions.
Liquidity Agent: The Liquidity Agent estimates
how easily a skin can be traded without large price
impact by combining recent trading volume with
Reddit engagement. It flags “liquidity traps”—
items with high listed prices but little real demand—
and downweights or blocks trades in such assets.
Event Agent: The Event Agent monitors recent of-
ficial Steam news and major CS2 updates, focus-
ing on changes to drop pools, item supply, and
game visibility. It classifies each news window as
bullish, bearish, or neutral for a given skin, indicat-
ing whether fundamentals are likely to improve or
deteriorate in the near term.
2.3 Operation Layer
The Operation Layer translates analytical signals
into concrete trades while respecting risk and mar-
ket frictions.
Risk Control Agent: The Risk Control Agent aggre-
gates signals from the Reasoning Layer together
with the current portfolio state to propose an “op-
timal position ratio” for each skin. It upweights
defensive evidence during uncertain periods and
downweights aggressive signals, keeping exposure
within safe bounds; its full prompt and decision
rules are listed in the appendix.
Transaction Friction Agent:The Transaction Fric-
tion Agent encodes platform fees into the decision
process. Using the 2% representative sell fee de-
rived from Appendix Table 4, it checks whether ex-
pected profits remain positive after costs and blocks
small, frequent trades that would lose money once
fees are applied.
Portfolio Management Agent: The Portfolio Man-
agement Agent is the final decision maker. It com-
bines the suggested position ratio, friction-aware
profit check, available cash, and a short decision
memory of recent trades to output a discrete ac-
tion (buy, sell, or hold) and trade size. The agent
can override risky recommendations (for example,
when prices deviate sharply from recent history) to
maintain a stable, consistent strategy over time.

3 Experiment Setting
3.1 Setup
We conduct our experiments using real-world data
from the Counter-Strike 2 global official market.
Data Acquisition: Our system integrates market
data and community events from two main digi-
tal sources. We track the whole market through the
Steam JSON API to collect daily OHLCV(Open,
High, Low, Close, V olume) candles. For commu-
nity sentiment, the system uses the Reddit API to
monitor specific subreddits (such as “GlobalOffen-
siveTrade” and “csgomarketforum”). Also, since
the Reddit API only supports (looking back) from
the current time, we use a “sliding time window”
strategy to align social discussions with specific
trading dates.
Base Model: We deploy six of the latest LLMs
as our framework’s base model from various
providers. The knowledge cutoff dates and capabil-
ities of each model are summarized in Table 1.
Trading Configuration: The initial capital for the
simulation is $10,000. The trading period cov-
ers a time of high market volatility. During this
time, the general CS2 skin market index dropped
by 15.62%. We conduct the experiment during a
period of high market volatility, specifically from
September 25 to November 15. We use the over-
all market index (CSQAQ, 2024) as our primary
baseline to evaluate the effectiveness of the multi-
agent system. This index tracks the average price
movements of a broad set of assets and serves as a
benchmark for passive investment. Its construction
is described in Appendix E.
3.2 Evaluation Metrics
We use several standard metrics (Yu et al., 2024b;
Xiong et al., 2025) to evaluate the performance of
each strategy: (1) Cumulative Return (CR) (Hull,
2012): The total percentage change in the port-
folio value; (2) Sharpe Ratio (SR) (Sharpe, 1994):
The risk-adjusted return, calculated using a 2% risk-
free rate; (3) Annualized V olatility (A V) (Cochrane,
1991): The standard deviation of daily returns,
showing price fluctuations; (4) Maximum Draw-
down (MDD) (Ang et al., 2006): The largest peak-
to-trough decline in the portfolio value. (5) Alpha
(α) (Jensen, 1968): the excess return that represents
the specific profit generated by the model reasoning
beyond the overall market. (6) Beta ( β) (Jensen,
1968): the measure of market risk that compares
the volatility of the portfolio to the overall market.
We use Alpha ( α) and Beta ( β) to compare the
performance and risk profiles of different model
backbones against the overall market. The formal
definitions of these metrics are in Appendix D.
4 Live Trading Discussion
We now discuss what the live trading experiments
reveal about CS2 as a niche market and about the
behavior of different agent and configurations.
4.1 Performance Against Overall Market
Our system demonstrates high resilience in a de-
clining market. Figure 3 visualizes the portfolio
value lines of different LLM backbones and the
overall market over the test period. While the CS2
market index fell by 15.62%, CSTrader configu-
rations based on strong LLMs achieved positive
returns and substantially smaller drawdowns, as
summarized in Table 2. This confirms that the
framework can extract “alpha” from a niche, event-
driven market that is difficult for traditional quanti-
tative models.
The largest shock is the CS2 “Trade Up” update
on October 25, which causes a sharp market crash
followed by a slow, partial recovery of the index.
In contrast, most CSTrader portfolios recover faster
and stabilize above the break-even line, suggesting
that multi-agent reasoning over technical, senti-
ment, liquidity, and event signals helps navigate
sudden regime changes effectively.
4.2 Findings for Agents on Niche Market
Characteristics
The CS2 market is a niche category where prices of-
ten do not reflect “actual value” due to high volatil-
ity, thin liquidity, and community bias. The ab-
lation results in Figure 4 and Table 3 show that
several agents are particularly important.
First, the Liquidity Agent improves the “real-
ization ability” of the portfolio by discouraging
purchases of items that are easy to list but hard to
sell, reflecting the prevalence of “liquidity traps” in
CS2 skins. Second, the Reversed Sentiment Agent
consistently outperforms the Sentiment Agent, in-
dicating a strong herd effect: following Reddit
hype tends to buy into bubbles, whereas contrarian
signals better capture value opportunities. Third,
adding the Event Agent has limited or even neg-
ative impact on returns, suggesting that official
Steam news is quickly priced in and offers little

Break-Even Line
CS2 “Trade Up” Update
Wipes $2 Billion from
Skin Market
CS2 Market Recovery
After Biggest Crash
Market Keeps Flourishing due
to the Rising Popularity of CS2
Qwen
Kimi
GPT
Gemini
Grok
DeepSeek
Claude
Overall
Market
Figure 3: Asset value trajectories of CSTrader with different LLM backbones compared to the overall CS2 market
index over the evaluation period. All strategies start from an initial capital of $10,000 (break-even line). The
CS2 “Trade Up” update on October 25 triggers a sharp market crash that wipes out a large portion of the skin
market value, followed by a partial recovery. While the overall market remains below break-even, most CSTrader
configurations recover faster and maintain higher asset values.
12k
11k
10k
9k
12k
11k
10k
10.1 10.8 10.15 10.22 11.1 11.8 11.15 10.1 10.8 10.15 10.22 11.1 11.8 11.15 10.1 10.8 10.15 10.22 11.1 11.8 11.1510.1 10.8 10.15 10.22 11.1 11.8 11.15
9k Total Assets ($)Total Assets ($)
Simple Prompts
Technical + Reversed Sentiment
+ Liquidity + Friction
Technical + Sentiment +
Liquidity + Event + Friction
Technical + Reversed Sentiment
+ Liquidity + Event + Friction
Technical + Reversed Sentiment
+ Liquidity + No Friction
Technical + Friction Technical + Sentiment + Friction Technical + Sentiment + Liquidity + Friction
Figure 4: Asset value trajectories of CSTrader under different agent combinations (Qwen-Max backbone). Each
panel shows the total portfolio value over time for one set of agents.

Table 1: Summary of LLM backbones used as base models in CSTrader. For each provider, we list the model name,
release date, knowledge cut-off, Elo rating, and whether the model is open source.
Providers Models Release Date Knowledge Cut-off Elo Open Source
DeepSeek DeepSeek-V3.2 (Liu et al., 2025a) Dec 2025 Aug 2025 1421
Alibaba Qwen-Max (Yang et al., 2025) Sep 2025 Jan 2025 1441
Kimi Moonshot-v1 (Moonshot AI, 2025) Jan 2025 Feb 2024 1260
Google Gemini-3-flash-preview (Google, 2025) Dec 2025 Jan 2025 1470
OpenAI GPT-5-mini (OpenAI, 2025) Aug 2025 May 2024 1443
Anthropic Claude-sonnet-4 (Anthropic, 2024) May 2025 Jan 2025 1420
xAI Grok-4.1-fast-reasoning (xAI, 2024) Nov 2025 Jul 2025 1482
Table 2: Performance of CSTrader with different LLM backbones on the CS2 skin market. We report cumulative
return (CR), Sharpe ratio (SR), maximum drawdown (MDD), annualized volatility (A V), beta (β) relative to the
overall market index, and alpha (α) capturing excess return over the market.
Models CR (%) SR MDD (%) A V (%)β α(%)
Claude-sonnet-4 7.580.49 25.9 79.81 0.47 66.86
Moonshot-v1 4.50 0.28 26.71 72.35 0.39 43.62
GPT-5-mini 4.29 0.19 35.71 99.95 0.59 54.25
Qwen-Max 3.83 0.42 17.04 38.86 0.20 28.47
DeepSeek-V3.2 -2.89 -0.16 39.74 106.10 0.65 21.71
Gemini-3-flash-preview -5.65 -0.32 34.20 88.19 0.55 4.41
Grok-4.1-fast-reasoning -6.48 -0.38 32.42 82.93 0.51 -1.09
Overall Market -15.62 -0.41 58.21 145.50 1.00 0.00
Table 3: Ablation study on agent combinations for CSTrader with Qwen-Max as the base model. We report
cumulative return (CR), Sharpe ratio (SR), maximum drawdown (MDD), and annualized volatility (A V) for different
subsets of agents.
Agent Combinations|Base Model: Qwen CR(%) SR MDD(%) A V
Simple Prompts -11.50 -0.75 26.71 65.57
Technical + Friction 1.62 0.09 19.86 50.59
Technical + Sentiment + Friction -10.77 -1.22 18.58 37.68
Technical + Sentiment + Liquidity + Friction 0.38 -0.06 11.66 29.00
Technical + Reversed Sentiment + Liquidity + Friction 5.94 0.53 19.52 54.48
Technical + Sentiment + Liquidity + Event + Friction 1.34 0.07 17.72 44.48
Technical + Reversed Sentiment + Liquidity + No Friction 21.96 1.66 31.06 95.04
Technical + Reversed Sentiment + Liquidity + Event + Friction 3.83 0.42 17.04 38.86
unique edge. Finally, explicitly modeling a 2%
transaction fee with the Transaction Friction Agent
closes the gap between idealized and realistic re-
turns and pushes the system toward less frequent,
higher-conviction trades. Together, these obser-
vations suggest that success in niche digital asset
markets hinges less on reacting to public news and
more on counteracting market inefficiencies.
4.3 Comparison between Base Models
Finally, we compare different LLM backbones
under the same CSTrader framework. Table 2
shows that stronger reasoning models, such as
Claude-sonnet-4, achieve the highest returns and
alpha, while more conservative models like Qwen-
Max offer the best risk-adjusted stability with low
volatility and beta. Aggressive backbones (e.g.,
DeepSeek-V3.2) can perform well in rising mar-
kets but are more exposed to crashes, and weaker
models (e.g., Gemini-3-flash-preview) struggle to
select profitable items even when timing is approx-
imately correct. Overall, these results suggest that
both backbone quality and risk preference shape
performance, and that our framework is sensitive
enough to reveal these differences.

5 Related Work
5.1 LLMs for Financial Analysis
Recent studies show that LLMs are becoming use-
ful tools in financial markets. A large group of
research projects focuses on investment analysis.
For example, FinGPT (Liu et al., 2023) and Fin-
Robot (Yang et al., 2024) transform financial data
into research reports. Other models like LLMFac-
tor (Wang et al., 2024a), XBRL Agent (Han et al.,
2024), and FinSphere (Han et al., 2025) help sys-
tems understand specific domains using real-time
and multimodal data.
In the field of portfolio management, models
like FinMem (Yu et al., 2024a) and EconAgent (Li
et al., 2023) use LLMs to make consistent trading
decisions. Single-agent frameworks, such as Flag-
Trader (Xiong et al., 2025), QuantAgent (Wang
et al., 2024b), and FinAgent (Zhang et al., 2024),
focus on creating and executing concrete trading
strategies. More recently, multi-agent architectures
like TradeAgents (Xiao et al., 2024), FinCon (Yu
et al., 2024b), CryptoTrade (Li et al., 2024b), and
DeepFund (Li et al., 2025a) explore how multi-
ple agents can work together to control risks in
volatile markets. Although these methods show
strong potential for financial analysis and invest-
ment, most existing studies remain grounded in
traditional stock markets, and niche investment
markets are still currently left largely unexplored.
5.2 Investment Research on Niche Assets
Beyond traditional equities, a growing body of
work studies quantitative trading and risk in niche
or alternative asset classes. For cryptocurrencies,
recent research links investor attention and mul-
timodal social sentiment to volatility and volume
dynamics (Gadirli et al., 2024; Liu et al., 2025b;
Roumeliotis et al., 2024), and designs multi-agent
LLM frameworks for automated crypto portfolio
management (Luo et al., 2025). Other studies ex-
tend LLM-based forecasting to carbon credit mar-
kets (Chen et al., 2024) and bond yields (Walia
et al., 2025), or tailor sentiment models to fixed-
income news (Barter et al., 2025). Emerging work
on illiquid collectibles, such as luxury watches,
highlights the diversification and liquidity fric-
tions of these markets (Weisskopf and Masset,
2025). Closest to our setting, Guede-Fernández
et al. (2025) build AI-driven algorithmic trading
systems for digital game assets in the Counter-
Strike 2 skin market, showing that deep models
can exploit liquidity and pricing frictions in virtual
economies. Together, these studies demonstrate
that niche assets, including virtual items, exhibit
distinct microstructure and information channels
compared with mainstream stocks, motivating spe-
cialized, data-driven trading frameworks.
6 Conclusion
In this paper, we study CS2 skins as a representa-
tive niche, language-driven asset market and use it
to build a realistic testbed for language-grounded
trading. We design CSTrader, a three-tier multi-
agent LLM framework that connects heterogeneous
signals from market data, community discussions,
and official events to concrete buy, sell, and hold
decisions under real-world trading frictions.
Our experiments on real CS2 market data show
that CSTrader is robust in a volatile and declining
market. Across several strong LLM backbones, our
system consistently outperforms the overall market
index and simple single-prompt LLM baselines,
achieving positive cumulative returns and high al-
pha while controlling risk. Ablation studies further
reveal that agents for liquidity, reversed sentiment,
and transaction friction are crucial for turning noisy
language signals into stable profits.
This work suggests that niche, language-driven
markets are a useful testbed for studying how
LLMs turn text into long-horizon financial actions.
In future work, we plan to extend our framework
to other virtual asset markets, integrate classical
quantitative models as additional agents, and ex-
plore live trading deployments to better understand
how language-based decision systems behave un-
der continuously changing conditions.
7 Limitation and Future Work
Despite these promising results, our study has sev-
eral limitations. First, we focus on a single virtual
asset market (CS2 skins) and a liquidity-filtered
subset of items, so the observed behaviors may
not directly transfer to larger or regulated finan-
cial markets. Second, our evaluation is based on
historical backtests over a relatively short, highly
volatile window around the “Trade Up” update,
without explicitly modeling order-book dynamics,
slippage, or execution latency beyond a simple 2%
transaction fee. Third, CSTrader currently relies on
prompt-engineered agents built on top of a small
set of frontier LLM backbones; we do not fine-tune
models or systematically search over agent archi-

tectures and hyperparameters. Finally, while we
compare against naive single-prompt LLMs and a
passive market index, we do not include strong clas-
sical quantitative or reinforcement-learning trading
baselines.
These limitations open up several directions for
future work. One direction is to extend CSTrader
to other virtual economies and small-cap financial
instruments, and to run longer-horizon evaluations
that cover multiple market regimes. Another is
to enrich the environment with more realistic mi-
crostructure, including order-book snapshots, exe-
cution constraints, and alternative fee schedules, to
better approximate live trading conditions. On the
modeling side, we plan to explore learning-based
agents that combine LLM reasoning with trainable
decision layers or offline reinforcement learning,
as well as hybrid systems that integrate classical
quantitative signals as first-class agents. Finally,
we would like to study human-in-the-loop and in-
terpretability aspects of multi-agent LLM traders,
for example by analyzing failure cases, agent in-
teractions, and explanation quality when strategies
are deployed in or near live markets.
References
Andrew Ang, Joseph Chen, and Yuhang Xing. 2006.
Downside risk.The review of financial studies,
19(4):1191–1239.
Anthropic. 2024. Claude 4: Technical report. https:
//www.anthropic.com/news/claude-4. Includes
Claude Sonnet 4 and other Claude 4 family models.
Toby Barter, Zheng Gao, Eva Christodoulaki, Jing Chen,
and John Cartlidge. 2025. Bondbert: What we learn
when assigning sentiment in the bond market. In
Proceedings of the 18th International Conference on
Agents and Artificial Intelligence (ICAART).
Leonardo Berti, Bardh Prenkaj, and Paola Velardi. 2025.
Trades: Generating realistic market simulations with
diffusion models.arXiv preprint arXiv:2502.07071.
Rui Chen, Haiqi Jiang, Tingyu Guo, and Chenyou Fan.
2024. Can large language models forecast carbon
price movements? evidence from chinese carbon
markets.SSRN Electronic Journal. Preprint.
John H Cochrane. 1991. V olatility tests and efficient
markets: A review essay. Technical report, National
Bureau of Economic Research.
CSQAQ. 2024. Calculation formula of market index.
Accessed: 2026-01-05.
Farid Gadirli, Minjia Chen, and Getinet Haile. 2024.
Investor attention and cryptocurrency volatility: A
machine learning and econometric analysis.SSRN
Electronic Journal. Preprint.
Google. 2025. Gemini 3 flash best for frontier in-
telligence at speed. https://deepmind.google/
models/gemini/flash/.
Nancy Greer, Matthew Rockloff, Matthew Browne, Ner-
ilee Hing, and Daniel L King. 2019. Esports betting
and skin gambling: A brief history.Journal of Gam-
bling Issues, 43.
Federico Guede-Fernández, Yash Wagle, Pedro Dias,
Ana Paula Giordano, Lúcio Henriques, Gonçalo
Costa, and Salomé Azevedo. 2025. Artificial intelli-
gence for algorithmic trading digital assets: Evidence
from the counter-strike 2 skin market.Frontiers in
Artificial Intelligence, 8.
Shijie Han, Haoqiang Kang, Bo Jin, Xiao-Yang Liu, and
Steve Y Yang. 2024. Xbrl agent: Leveraging large
language models for financial report analysis. InPro-
ceedings of the 5th ACM International Conference
on AI in Finance, pages 856–864.
Shijie Han, Changhai Zhou, Yiqing Shen, Tianning Sun,
Yuhua Zhou, Xiaoxia Wang, Zhixiao Yang, Jingshu
Zhang, and Hongguang Li. 2025. Finsphere: A
conversational stock analysis agent equipped with
quantitative tools based on real-time database.arXiv
preprint arXiv:2501.12399.
Taylor Stanton Hardenstein. 2017. " skins" in the game:
Counter-strike, esports, and the shady world of online
gambling.UNLV Gaming LJ, 7:117.
John Hull. 2012.Risk management and financial in-
stitutions,+ Web Site, volume 733. John Wiley &
Sons.
Michael C Jensen. 1968. The performance of mutual
funds in the period 1945–1964.The Journal of Fi-
nance, 23(2):389–416.
Alex Kim, Maximilian Muhn, and Valeri Nikolaev.
2024. Financial statement analysis with large lan-
guage models.arXiv preprint arXiv:2407.17866.
Hyungjin Ko and Jaewook Lee. 2024. Can chatgpt
improve investment decisions? from a portfolio
management perspective.Finance Research Letters,
64:105433.
Changlun Li, Yao Shi, Yuyu Luo, and Nan Tang.
2025a. Deepfund: Will LLM be professional at
fund investment? A live arena perspective.CoRR,
abs/2503.18313.
Nian Li, Chen Gao, Mingyu Li, Yong Li, and Qing-
min Liao. 2023. Econagent: large language model-
empowered agents for simulating macroeconomic
activities.arXiv preprint arXiv:2310.10436.
Xiang Li, Zhenyu Li, Chen Shi, Yong Xu, Qing Du,
Mingkui Tan, and Jun Huang. 2024a. Alphafin:
Benchmarking financial analysis with retrieval-
augmented stock-chain framework. InProceedings

of the 2024 joint international conference on compu-
tational linguistics, language resources and evalua-
tion (LREC-COLING 2024), pages 773–783.
Xiangyu Li, Yawen Zeng, Xiaofen Xing, Jin Xu, and Xi-
angmin Xu. 2025b. Hedgeagents: A balanced-aware
multi-agent financial trading system. InCompanion
Proceedings of the ACM on Web Conference 2025,
pages 296–305.
Yuan Li, Bingqiao Luo, Qian Wang, Nuo Chen, Xu Liu,
and Bingsheng He. 2024b. CryptoTrade: A reflective
LLM-based agent to guide zero-shot cryptocurrency
trading. InProceedings of the 2024 Conference on
Empirical Methods in Natural Language Processing,
pages 1094–1106, Miami, Florida, USA. Association
for Computational Linguistics.
Aixin Liu, Aoxue Mei, Bangcai Lin, Bing Xue, Bingx-
uan Wang, Bingzheng Xu, Bochao Wu, Bowei Zhang,
Chaofan Lin, Chen Dong, and 1 others. 2025a.
Deepseek-v3. 2: Pushing the frontier of open large
language models.arXiv preprint arXiv:2512.02556.
Chenghao Liu, Aniket Mahanti, Ranesh Naha, Guang-
hao Wang, and Erwann Sbai. 2025b. Enhancing
cryptocurrency sentiment analysis with multimodal
features.arXiv preprint arXiv:2508.15825.
Xiao-Yang Liu, Guoxuan Wang, Hongyang Yang, and
Daochen Zha. 2023. Fingpt: Democratizing internet-
scale data for financial large language models.arXiv
preprint arXiv:2307.10485.
Yichen Luo, Yebo Feng, Jiahua Xu, Paolo Tasca, and
Yang Liu. 2025. LLM-powered multi-agent system
for automated crypto portfolio management.arXiv
preprint arXiv:2501.00826.
Desirée Martinelli. 2017. Skin gambling: Have we
found the millennial goldmine or imminent trouble?
Gaming Law Review, 21(8):557–565.
Moonshot AI. 2025. How to use moonshot v1. https:
//platform.moonshot.cn/docs/introduction.
OpenAI. 2025. Introducing gpt-5 for de-
velopers. https://openai.com/index/
introducing-gpt-5-for-developers/ . In-
cludes GPT-5 mini and other lightweight variants.
Konstantinos I. Roumeliotis, Nikolaos D. Tselikas, and
Dimitrios K. Nasiopoulos. 2024. LLMs and NLP
models in cryptocurrency sentiment analysis: A com-
parative classification study.Big Data and Cognitive
Computing, 8(6):63.
William F Sharpe. 1994. The sharpe ratio, the journal
of portfolio management.Stanfold University, Fall.
Foteini Valeonti, Antonis Bikakis, Melissa Terras, Chris
Speed, Andrew Hudson-Smith, and Konstantinos
Chalkias. 2021. Crypto collectibles, museum fund-
ing and openglam: challenges, opportunities and the
potential of non-fungible tokens (nfts).Applied Sci-
ences, 11(21):9931.
Jaskaran Singh Walia, Aarush Sinha, Srinitish Srini-
vasan, and Srihari Unnikrishnan. 2025. Predict-
ing liquidity-aware bond yields using causal gans
and deep reinforcement learning with llm evaluation.
arXiv preprint arXiv:2502.17011.
Meiyun Wang, Kiyoshi Izumi, and Hiroki Sakaji. 2024a.
Llmfactor: Extracting profitable factors through
prompts for explainable stock movement prediction.
arXiv preprint arXiv:2406.10811.
Qin Wang, Rujia Li, Qi Wang, and Shiping Chen.
2021. Non-fungible token (nft): Overview, evalu-
ation, opportunities and challenges.arXiv preprint
arXiv:2105.07447.
Saizhuo Wang, Hang Yuan, Lionel M Ni, and Jian Guo.
2024b. Quantagent: Seeking holy grail in trading by
self-improving large language model.arXiv preprint
arXiv:2402.03755.
Jean-Philippe Weisskopf and Philippe Masset. 2025.
Time is money: An investment in luxury watches.
SSRN Electronic Journal.
Qilong Wu, Xiaoneng Xiang, Hejia Huang, Xuan Wang,
Yeo Wei Jie, Ranjan Satapathy, Bharadwaj Veeravalli,
and 1 others. 2024. Susgen-gpt: A data-centric llm
for financial nlp and sustainability report generation.
arXiv preprint arXiv:2412.10906.
xAI. 2024. Grok-4 technical overview. https://x.ai/
blog. Includes Grok-4.1 fast-reasoning and other
Grok-4 series models.
Yijia Xiao, Edward Sun, Di Luo, and Wei Wang. 2024.
Tradingagents: Multi-agents llm financial trading
framework.arXiv preprint arXiv:2412.20138.
Guojun Xiong, Zhiyang Deng, Keyi Wang, Yupeng Cao,
Haohang Li, Yangyang Yu, Xueqing Peng, Mingquan
Lin, Kaleb E Smith, Xiao-Yang Liu, and 1 others.
2025. Flag-trader: Fusion llm-agent with gradient-
based reinforcement learning for financial trading.
arXiv preprint arXiv:2502.11433.
An Yang, Anfeng Li, Baosong Yang, Beichen Zhang,
Binyuan Hui, Bo Zheng, Bowen Yu, Chang
Gao, Chengen Huang, Chenxu Lv, and 1 others.
2025. Qwen3 technical report.arXiv preprint
arXiv:2505.09388.
Hongyang Yang, Boyu Zhang, Neng Wang, Cheng Guo,
Xiaoli Zhang, Likun Lin, Junlin Wang, Tianyu Zhou,
Mao Guan, Runjia Zhang, and 1 others. 2024. Fin-
robot: an open-source ai agent platform for finan-
cial applications using large language models.arXiv
preprint arXiv:2405.14767.
Yangyang Yu, Haohang Li, Zhi Chen, Yuechen Jiang,
Yang Li, Denghui Zhang, Rong Liu, Jordan W Su-
chow, and Khaldoun Khashanah. 2024a. Finmem: A
performance-enhanced llm trading agent with layered
memory and character design. InProceedings of the
AAAI Symposium Series, volume 3, pages 595–597.

Yangyang Yu, Zhiyuan Yao, Haohang Li, Zhiyang Deng,
Yuechen Jiang, Yupeng Cao, Zhi Chen, Jordan Su-
chow, Zhenyu Cui, Rong Liu, and 1 others. 2024b.
Fincon: A synthesized llm multi-agent system with
conceptual verbal reinforcement for enhanced finan-
cial decision making.Advances in Neural Informa-
tion Processing Systems, 37:137010–137045.
Wentao Zhang, Lingxuan Zhao, Haochong Xia, Shuo
Sun, Jiaze Sun, Molei Qin, Xinyi Li, Yuqing Zhao,
Yilei Zhao, Xinyu Cai, and 1 others. 2024. A multi-
modal foundation agent for financial trading: Tool-
augmented, diversified, and generalist. InProceed-
ings of the 30th ACM SIGKDD Conference on Knowl-
edge Discovery and Data Mining, pages 4314–4325.
A CS2 Skin Market Overview
The CS2 skin market is one of the largest and
most mature virtual-asset economies worldwide
and is often described by players as an “electronic
stock market”. Skins are purely cosmetic items that
change the appearance (and sometimes audio) of
weapons, knives, gloves, or agents without affect-
ing gameplay statistics such as damage or accuracy,
which preserves competitive fairness. Each indi-
vidual skin instance is characterized by continuous
attributes such as float value and pattern index, so
that even two copies of the “same” skin can differ
visually and in market price.
Community trackers (e.g., PriceEmpire) esti-
mate that, by late 2025, the notional market capi-
talization of tradable CS2 skins is on the order of
4–5 billion USD. Valve is reported to earn more
than one billion USD per year from key sales and
marketplace fees. The ecosystem contains several
hundred thousand distinct items and a daily active
player base between roughly 600K and 1.5M, with
peak concurrent players exceeding 1.8M. The mar-
ket is dominated by retail participants—ordinary
players and collectors—with limited institutional
participation, leading to high volatility, sentiment-
driven flows, and pronounced liquidity frictions.
A.1 Item Attributes and Categories
CS2 skins are organized along several key axes that
jointly determine their value:
Rarity.Item rarity is discretized into tiers that
roughly correspond to color codes in the user inter-
face, from low to high: Consumer Grade (white),
Industrial Grade (light blue), Mil-Spec (blue), Re-
stricted (purple), Classified (pink), Covert (red),
and Extremely Rare (gold, mostly knives and
gloves). Higher rarity implies lower drop prob-
ability and typically higher price.
Wear level and float value.Visual wear is di-
vided into five canonical categories: Factory New
(FN), Minimal Wear (MW), Field-Tested (FT),
Well-Worn (WW), and Battle-Scarred (BS). Un-
derneath, each skin instance has a continuous float
value in the range [0.00,1.00] , with lower values
corresponding to less visible wear. Market prices
are highly sensitive to float, especially for FN and
MW items near the lower end of the range.
Pattern index.For many skins (e.g., Case Hard-
ened, Fade, Crimson Web), the game samples a
random pattern index that determines the exact tex-
ture overlay. Certain pattern configurations (such

as all-blue “Blue Gem” Case Hardened knives) are
extremely rare and command large premiums over
otherwise similar items.
Asset categories.The core tradable assets are
weapon skins for popular rifles, pistols, and sniper
rifles such as AK-47, M4A1-S, and AWP, which
form the backbone of many portfolios. Gold-tier
knives and gloves, with an overall drop probabil-
ity of roughly 0.26%, act as high-value pillars of
the market, with individual items ranging from
hundreds to tens of thousands of USD. Stickers
and capsules—especially early tournament series
such as Katowice 2014—are highly speculative
collectibles, with some individual stickers valued
at tens or even hundreds of thousands of USD.
Additional categories include agent skins (which
change the player model), sprays, weapon cases,
keys, medals, and newer cosmetic features such as
charms and temporary rental-style access.
A.2 Acquisition Mechanics
Players obtain skins via several mechanisms that
have direct implications for supply dynamics and
player behavior:
Weekly drops.Eligible accounts with Prime
Status receive a “weekly drop” when they level up
once per week. The drop presents a small menu of
items, typically including a weapon case, a low-tier
skin, and graffiti options, from which the player
can select two items. This mechanism provides a
slow, steady inflow of low- to mid-tier items.
Case opening (gacha).The dominant mecha-
nism for injecting new high-value items is open-
ing weapon cases. Players must purchase keys
(priced around 2.5 USD) to open cases obtained
via drops or the market. Valve publicly states ap-
proximate rarity probabilities: Covert (red) items
have a drop chance on the order of 0.64%, while
gold-tier knives and gloves collectively have a prob-
ability around 0.26%. From a financial perspective,
case opening is a negative-expected-value gamble,
but the possibility of extremely rare, high-value
drops sustains very large aggregate volume.
Trade-up contracts.Players can exchange ten
skins of the same rarity tier for one skin of the
next-higher tier via an in-game “trade-up contract”.
In a 2025 update, Valve introduced a new form
of trade-up that allows combining a set of Covert
(red) skins to obtain knives or gloves. This change
temporarily drove up demand and prices for cer-
tain Covert items and caused sharp dislocations in
the knife and glove markets, illustrating how rule
changes propagate through the ecosystem.
A.3 Market Size, Venues, and Frictions
The primary trading venue is the official Steam
Community Market. Trades are denominated
in regional fiat currencies but settled into non-
withdrawable Steam Wallet balances, meaning that
realized profits can only be reinvested within the
Steam ecosystem. Steam charges a fee of roughly
15% on each sale (around 10% to Valve and 5% to
the game developer), which makes high-frequency
trading expensive compared with traditional bro-
kerage accounts.
To combat fraud, money laundering, and auto-
mated arbitrage, Valve imposes strict trade-lock
rules. Items obtained via trades, market purchases,
or case openings cannot be traded again for seven
days. In practice, certain sequences of transactions
yield an effective holding period close to T+14.
Accounts without Steam Guard mobile authentica-
tion face even longer delays (up to 15 days) before
trades are confirmed. These frictions slow portfolio
turnover and create a gap between mark-to-market
valuations and realizable proceeds.
Outside the official marketplace, a network of
third-party peer-to-peer (P2P) platforms provides
alternative liquidity and cash-out channels. In main-
land China, NetEase BUFF is the dominant market-
place, enabling RMB cash withdrawals and charg-
ing relatively low fees (typically 1–3%). Interna-
tionally, platforms such as Skinport, CS.MONEY ,
CSFloat, and Tradeit.gg match buyers and sellers
via Steam trade offers, sometimes with support
for credit cards or cryptocurrencies. Very high-
end items (e.g., rare souvenir AWP Dragon Lore
or unique pattern knives) are often traded privately
through brokers or OTC-style deals rather than pub-
lic listings.
In 2025 Valve also introduced a rental-like cos-
metic access system, in which players can tem-
porarily use certain skins by paying a small fixed
fee (roughly the price of a key). This mechanism
lowers the barrier to experiencing premium cosmet-
ics while preserving scarcity of permanent owner-
ship, further enriching the ecosystem of use cases
around skins.
A.4 Risks and Market Dynamics
The CS2 skin market is exposed to several sources
of risk that directly influence trading strategies:
Update and policy risk.Game-balance patches,
new case releases, and rule changes (such as mod-

ifications to trade-up contracts or trade-lock poli-
cies) can cause sudden repricing of whole item
classes. For example, adjustments to trade-up rules
have previously led to multi-hundred-million-USD
swings in estimated market capitalization within
days.
Price volatility and liquidity.Many items
are thinly traded, with large gaps between list-
ing prices and actual executed trades. Liquidity
is highly skewed toward a small subset of meta-
relevant skins and iconic collectibles, while long
tails of items exhibit “liquidity traps” where nomi-
nal prices are high but buy-side depth is shallow.
Security and regulatory risk.Common threats
include phishing websites, API token hijacking,
and impersonation scams that exploit Steam’s trad-
ing workflows. In addition, national regulations
on loot boxes and virtual-item gambling (e.g., re-
strictions in certain European countries) can affect
case-opening volumes and platform policies, with
second-order effects on prices.
Overall, the CS2 skin ecosystem functions as
a large-scale digital collectibles market with a
rich set of microstructural frictions, heterogeneous
venues, and strongly language-driven information
flows. These properties motivate our choice of CS2
as a challenging testbed for language-grounded
trading agents.
B Agent Instruction
B.1 Prompt Template
Planner Agent
You are a planner agent that decides which an-
alysts to perform based on the your knowledge
of the ticker and features of analysts.
Here is the ticker:
- {ticker}
Here are the available analysts:
- {analysts}
You must provide your decision as a structured
output with the following fields:
- analysts: selected analyst_name list
- justification: brief explanation of your se-
lection
Technical Agent
You are a technical analyst evaluating items in
CS2 market using multiple technical analysis
strategies.
The following signals have been generated
from our analysis:
Price Trend Analysis:
-Trend Following: {analysis[trend]}
Mean Reversion and Momentum:
-Mean Reversion:
{analysis[mean_reversion]}
-RSI: {analysis[rsi]}
-Volatility: {analysis[volatility]}
Volume Analysis: {analysis[volume]}
Support and Resistance Levels:
{analysis[price_levels]}
Provide structured output:
- signal:
["Bullish","Bearish","Neutral"]
- justification: Brief explanation of your anal-
ysis
Sentiment Analyst
You are a sentiment analyst evaluating items
in CS2 market based on Reddit discussions.
Analyze Reddit discussions for {ticker}
({post_count} posts).
- Direct posts:price trends, demand/supply
factors
- General posts:overall market mood → in-
fer impact on {ticker}
- Focus on content sentiment, not just up-
votes/comments
- If posts <5 : return "Neutral" and explain
data limits
Reddit discussions:
- {reddit_posts}
Give a short-term (1-2 weeks) sentiment:
Bullish/Bearish/Neutral.
Provide structured output:

- signal:
["Positive","Negative","Neutral"]
- justification: Brief explanation of your anal-
ysis
Reversed Sentiment Agent
You are a contrarian sentiment analyst for CS2
market items. Apply reverse sentiment analy-
sis based on the contrarian hypothesis.
Original sentiment signal: {original_signal}
Original justification: {original_justification}
Contrarian Hypothesis:
- Overly bullish Reddit chatter can signal
market overheating→potentially bearish
- Negative chatter can indicate overselling→
potentially bullish
- Neutral sentiment remains neutral
Your task:
- Reverse the signal direction (Bullish →
Bearish, Bearish → Bullish, Neutral →
Neutral)
- Provide a justification explaining the con-
trarian interpretation
Evaluate the reversed sentiment for {ticker}
based on the contrarian hypothesis.
Provide structured output:
- signal:
["Positive","Negative","Neutral"]
- justification: Brief explanation of your anal-
ysis
Event Agent
You are an event analyst for CS2 items. Ana-
lyze Steam news for price impact on {ticker}.
Impact Assessment (priority order):
1. Supply mechanism (strongest):Drop pool,
crate/box, rarity, trade-up path changes
2. Visibility/popularity (moderate):New
crates, team stickers, weapon balance
changes
3. Market sentiment (indirect):Player influx,
major updates, speculative activity
Signal:
- Bullish:Increases scarcity/visibility or pos-
itive sentiment
- Bearish:Increases supply, decreases visi-
bility, or negative sentiment
- Neutral:No clear impact, insufficient data
({news_count} items), or mixed signals
Steam News ({news_count} items):
- {steam_news}
Evaluate event impact for short-term (1–2
weeks) price movement of {ticker}. Specify
which news items and factors influenced your
signal.
Provide structured output:
- signal:
["Positive","Negative","Neutral"]
- justification: Brief explanation of your anal-
ysis
Liquidity Analyst (CS2 Market)
You are a liquidity analyst for CS2 items. An-
alyze liquidity based on trading volume and
Reddit engagement.
Analysis:
- {trading_volume_analysis}
- {reddit_engagement_analysis}
Thresholds:
- Volume:High ≥ {volume_high}, Low <
{volume_low}
- Reddit:High (score ≥ {reddit_high_score}
orcomments ≥ {reddit_high_comments}),
Low (score < {reddit_low_score}andcom-
ments<{reddit_low_comments})
-Min posts:{reddit_min_posts}
Signal:
- Bullish:High volumeORstrong engage-
ment (both→higher confidence)
- Bearish:Low volumeORweak engage-
ment (both→higher confidence)
- Neutral:Mixed/conflicting indicators or
insufficient data

Evaluate liquidity (bullish/bearish/neutral) for
{ticker}. Explain which indicators contributed
most.
Provide structured output:
- signal: ["Safe","Unsafe","Neutral"]
- justification: Brief explanation of your anal-
ysis
Portfolio Management Agent
You are a portfolio manager making final trad-
ing decisions based on decision memory and
the provided optimal position ratio.
Decision memory:
- {decision_memory}
Current Price: {current_price}
Holding Shares: {current_shares}
Tradable Shares: {tradable_shares}
Rules:
- Iftradable_shares>0: you may buy.
- Iftradable_shares<0: you may sell.
- Iftradable_shares≈0: chooseHold.
You must provide your decision as a structured
output with the following fields:
- action: One of ["Buy","Sell","Hold"]
- shares: Number of shares to buy or sell, set
0 for hold
- price: The current price of the ticker
- justification: Briefly explain your decision
Your response should be well-reasoned and
consider all aspects of the analysis.
Transaction Friction Agent
You are a portfolio manager making final trad-
ing decisions based on decision memory and
the provided optimal position ratio.
Decision memory:
- {decision_memory}
Current Price: {current_price}
Holding Shares: {current_shares}
Tradable Shares: {tradable_shares}
Trading friction: selling fee {transac-
tion_fee_rate_pct:.2f}% (applies to sells only).
Rules:
- If tradable_shares> 0: you may buy (no
fee on buy).
- If tradable_shares< 0: you may sell;
ensure expected downside risk outweighs
sell fee.
- If tradable_shares≈ 0 or expected gain
<sell-fee impact: chooseHold.
- Ensure expected profit after (sell) fees is
positive; otherwiseHold.
You must provide your decision as a structured
output with the following fields:
- action: One of ["Buy","Sell","Hold"]
- shares: Number of shares to buy or sell, set
0 for hold
- price: The current price of the ticker
- justification: Briefly explain your decision,
explicitly noting how the 2% sell fee im-
pacted the choice
Your response should be well-reasoned and
consider all aspects of the analysis.
Risk Control Agent
You are a professional risk control analyst.
Please evaluate the risk of the ticker and set the
optimal position ratio based on analyst signals
and portfolio state.
Here are the analyst signals:
- {ticker_signals}
Here is the portfolio state:
- {portfolio}
The position ratio range: [ 0,
{max_position_ratio} ], the minimum
step is 0.05.
- If you observe more bullish signals, you can
set a larger position ratio.
- If you observe more bearish signals, you
can set a smaller position ratio.
You must provide your control recommenda-
tion as a structured output with the following
fields:

- optimal_position_ratio: The optimal ratio
of the position value to the total portfolio
value
- justification: A brief explanation of your
recommendation
Your response should be well-reasoned and
consider all aspects of the analysis.
C table
D Formal Definition of Evaluation
Metrics
We evaluate each strategy using daily portfolio val-
ues and several standard financial metrics. Let Vt
denote the portfolio value at the end of trading day
t, and V0 be the initial capital. We define the simple
daily return as
rt = Vt −V t−1 Vt−1 ,(1)
and use it as the basis for all subsequent metrics.
D.1 Cumulative Return (CR)
The cumulative return over the full backtest horizon
withTtrading days is defined as
CR = VT −V 0
V0
×100%,(2)
which measures the total percentage change in port-
folio value from the start to the end of the evalua-
tion period.
D.2 Sharpe Ratio (SR)
We compute the Sharpe ratio using the excess daily
return over a constant annual risk-free rate rf (set
to 2% in our experiments). First, we convert the
annual risk-free rate into an effective daily rate
under the standard 252 trading-day convention:
rf,d = (1 +r f )1/252 −1.(3)
Let ¯rbe the mean of daily returns rt, and σr be
their standard deviation. The annualized Sharpe
ratio is then
SR = ¯r−rf,d
σr
×
√
252,(4)
which measures the risk-adjusted return of the strat-
egy.
D.3 Annualized Volatility (A V)
We use the standard deviation of daily returns to
measure volatility. The annualized volatility (in
percentage) is
A V =σr ×
√
252×100%,(5)
which reflects the magnitude of typical price fluc-
tuations on an annualized basis.
D.4 Maximum Drawdown (MDD)
Maximum drawdown captures the worst peak-
to-trough loss over the evaluation horizon. Let
Mt = max 1≤k≤t Vk be the running maximum of
the portfolio value up to day t. The drawdown at
daytis
Dt = Mt −V t Mt ,(6)
and the maximum drawdown is
MDD = max
1≤t≤T
Dt ×100%,(7)
representing the largest percentage decline from a
historical peak.
D.5 Alpha (α) and Beta (β)
We estimate alpha and beta relative to the overall
CS2 market index. Let r(p) t denote the portfolio’s
daily return and r(m) t the market index daily return.
Using the same daily risk-free rate rf,d as above,
we define excess returns
R(p) t =r (p) t −r f,d, R (m) t =r (m) t −r f,d.(8)
We adopt the standard CAPM formulation
R(p) t =α+βR (m) t +ε t,(9)
and estimate α and β via ordinary least squares
over the backtest window. Equivalently,
β= Cov(R(p), R(m)) Var(R(m)) ,(10)
α= R(p) −β R(m),(11)
where R(p) and R(m) are the sample means of the
excess returns. For presentation in Table 2, we
report α in percentage terms. A positiveα indicates
excess return beyond what is explained by exposure
to the overall market, while β measures sensitivity
to market movements (market risk).

Table 4: Comparison of major CS2 skin trading platforms and their fee structures. We summarize representative
selling and buyer fees, along with key features that influence effective transaction costs and liquidity, which motivate
our choice of a 2% friction level in the Transaction Friction Agent.
Platform Selling Fee Buyer Fee Key Features
Steam Market(offical) 15% N/A Official. Highest fees and funds are locked
to the Steam Wallet (cannot be cashed out).
Buff 2.5% 1% Cash-out fee Highest liquidity globally. Uses P2P (Peer-
to-Peer) trading.
YouPin 2%-3% 1% Cash-out fee Known for its “Lease-to-Play” system
alongside standard P2P trading.
IGXE 2%-3.5% 1% Cash-out fee Alternatives to Buff with occasional pro-
motions and bot-delivery options.
CSFloat 2% Varies (Low) Minimalist P2P site; excellent for high-tier
items and specific "float" hunting.
Skinport 6%-12% 0% for Buyers Extremely buyer-friendly; the listed price
is the final price.
DMarket 5%-7% Varies Integrates trades for multiple games and
blockchain assets.
SkinBaron 2%-15% Varies Very strict KYC/safety regulations. Com-
petitive fees for items≥ C1000.
E Construction of the CS2 Market Index
We follow the CSQAQ index provider to construct
a dimensionless overall CS2 market index that
tracks the average price movement of a broad set
of tradable items.
E.1 Constituent Selection and Baseline
Let I denote the set of items included in the index.
The universe is constructed by selecting all items
whose on-sale quantity on the platform exceeds a
given liquidity threshold (greater than 50 listings at
the time of construction), which yields |I|=N=
11,269items in our snapshot.
The index is anchored to a baseline date t0 cor-
responding to 1 January 2021. On this date, the
index level is fixed to
I(t 0) = 1000.(12)
For each item i∈ I, let Pi(t) denote its market
price at date t. If an item was already listed on the
baseline date, we take
Pi(t0)(13)
as its initial reference price. If an item was not yet
listed on t0, we use its first observed transaction or
listing price as the initial reference priceP i(t0).
E.2 Index Level at Timet
At any later datet, the gross return of itemi relative
to its initial reference price is
Ri(t) = Pi(t) Pi(t0) .(14)
The index level is then defined as the equal-
weighted average of these gross returns, scaled by
the baseline value 1000:
I(t) = 1000× 1 N X i∈I Ri(t) = 1000× 1 N X i∈I Pi(t) Pi(t0) .
(15)
This construction removes the effect of different
absolute price levels and puts all items on the same
dimensionless scale before averaging.
E.3 Rationale
If we simply summed raw prices P i Pi(t) to form
the index, very expensive items would dominate
the index movement, and cheap items would have
negligible influence. By normalizing each price by
its initial reference price and then averaging, the
index measures the average relative change across
items rather than total market capitalization. As a
result, the CS2 market index is not equal to the to-
tal market value or the sum of all item floor prices;
instead, it is a dimensionless indicator that summa-
rizes typical percentage changes in item prices over
time.

F Additional Experimental Analysis
F.1 Performance Against Overall Market
(Extended)
Our system demonstrates high resilience in a de-
clining market. During the test period, the over-
all CS2 market index fell by 15.62%. Under the
same conditions, our multi-agent framework sig-
nificantly outperformed this benchmark across al-
most all backbone models. As reported in Table 2,
Claude-sonnet-4 achieved the highest cumulative
return of 7.58%, while even the least successful
model, Grok-4.1-fast-reasoning, experienced a loss
of only 6.48%. This confirms that the system is
much more stable than the general market.
The market volatility was largely driven by spe-
cific official events. As illustrated in Figure 3, the
CS2 “Trade Up” update on October 25 caused a
massive market crash that wiped out a large portion
of the skin market value. While the overall mar-
ket struggled to recover, our multi-agent configura-
tions showed a much faster and stronger recovery
trend. This performance highlights that multi-agent
systems are effective at navigating sudden, event-
driven shocks in this specific market.
Unlike traditional securities markets, the CS2
market has a relatively small volume and shallow
depth. Quantitative trading is not common here
because of scale limits and platform-specific rules.
In this environment, most trades are driven by in-
dividual emotions and sudden event news. Our
system has a strong ability to collect information
and perform reasoning, allowing it to adapt to the
unique rules of the virtual asset market and ob-
tain high “alpha returns”, with the top-performing
model achieving an alpha of 66.86%.
F.2 Agent-Level Findings (Extended)
The CS2 market is a niche category where prices of-
ten do not reflect “actual value” due to high volatil-
ity and community bias. By testing different combi-
nations of agents, we discovered several important
market traits. Figure 4 and Table 3 show how each
agent affects the outcome.
Liquidity and the Realization Gap: By adding the
Liquidity Agent, we observe a significant perfor-
mance increase from 8923.05 to 10038.36 in final
asset value. This agent improves the “realization
ability” of the portfolio by preventing the system
from buying items that are easy to list but hard to
sell. The result highlights a specific market charac-
teristic: many CS2 items suffer from a “liquidity
trap” where listed prices are high but actual buyer
demand is low.
The Herd Effect in Community Sentiment: When
we enable only the Sentiment Agent, its perfor-
mance is poor. However, when we enable the Re-
versed Sentiment Agent, the final return jumps to
10593.76. Reversing community signals actually
leads to better results than following them. This
observation reveals that the CS2 market is heav-
ily driven by a “herd effect”, where widespread
optimism often leads to “market bubbles”. By iden-
tifying and countering this irrational hype, the sys-
tem protects the portfolio from buying at artificial
peaks.
Official News as a Trading Inhibitor: After adding
the Event Agent to the system, we observe a perfor-
mance decrease from 10593.76 to 10383.21. Our
investigation shows that official Steam updates of-
ten act as an “inhibitor” of profit. Official news
is a form of “common knowledge” that is quickly
priced in by all participants, and therefore contains
little unique profit opportunity for a trading system.
This demonstrates that the CS2 market is highly
efficient with respect to official news, making these
signals less useful for high-return strategies.
The Impact of Transaction Friction: The data
shows a large difference between “ideal” returns
and “realistic” returns. When we do not con-
sider trading costs, the profit appears much higher
(12196.48). However, once we include the 2%
transaction fee, the return is about 14% lower at
10593.76. This confirms that transaction fees can-
not be ignored in CS2 trading. These costs do more
than simply erode profit: they directly influence the
decision-making process. If a model ignores fees,
it may suggest frequent, small trades that appear
profitable on paper. In contrast, the Transaction
Friction Agent recognizes that a 2% fee can turn a
small gain into a net loss, forcing the system to be
more selective and often to choose “Hold” instead
of inefficient “Sell” actions.
F.3 Backbone Behavior (Extended)
We also examine how different LLM backbones
behave under the same CSTrader framework. The
models fall into four broad categories based on
their risk preferences and analytical focus.
Smart Models: The first category includes models
likeClaude-sonnet-4, which are effective at iden-
tifying specific market opportunities after a crisis.
During the early stage of the experiment, Claude

maintains a cautious stance with high cash reserves,
resulting in performance that stays near the break-
even line. After the market crash on October 25,
the model accurately identifies a recovery opportu-
nity. By increasing its position size at the optimal
time, Claude achieves the highest CR of 7.58% and
the highest α of 66.86%, showing a strong abil-
ity to find “alpha returns” during periods of high
uncertainty.
Stable and Risk-Averse Models: The second cate-
gory is represented byQwen-Max, which follows
a conservative and disciplined style. This model
prioritizes risk management and maintains strict
rules for entering and exiting positions. Its asset
value curve is the most stable among all profitable
models, with the lowest A V of 38.86% and the low-
est β of 0.20. Although its final CR of 3.83% is not
the highest, its high SR of 0.42 demonstrates that
it offers the best risk-adjusted stability in a volatile
market.
Aggressive Models: Models likeDeepSeek-V3.2
exhibit an aggressive trading style with high capi-
tal utilization. Early in the experiment, DeepSeek
maintains near-full positions, which leads to high
performance during the flourishing phase. How-
ever, this aggressive style also results in the highest
A V of 106.10% and the highest β of 0.65. Dur-
ing the crash on October 25, DeepSeek suffers the
largest losses and ranks near the bottom for sev-
eral days. Although it partially recovers afterward,
its final CR remains negative at -2.89%, indicat-
ing that aggressive backbones struggle with risk
control during sudden shocks.
Weak Analysis and Selection Models: The final
category includes models likeGemini-3-flash-
preview, which show weak analysis of market
potential and item dynamics. Although Gemini
increases its position size after the market dip, its
final CR of -5.65% is underwhelming. The model
appears to struggle in selecting the correct assets
within the CS2 market; even when it approximately
times the market, the chosen items do not gain
enough value to offset previous losses. This in-
dicates that effective trading in this niche market
requires not only timing but also a strong ability
to identify which specific items have the highest
growth potential.
