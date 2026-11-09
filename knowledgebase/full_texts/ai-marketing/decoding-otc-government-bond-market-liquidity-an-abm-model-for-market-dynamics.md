---
title: 'Decoding OTC Government Bond Market Liquidity: An ABM Model for Market Dynamics'
url: https://arxiv.org/abs/2501.16331
category: ai-marketing
subcategory: empirical
date: 2024-12
venue: ''
authors:
- Alicia Vidler
- Toby Walsh
source: arxiv
pdf_url: https://arxiv.org/pdf/2501.16331
pages: 7
chars: 39752
fetched_at: '2026-11-08T13:14:12+00:00'
kb_version: 1
---

# Decoding OTC Government Bond Market Liquidity: An ABM Model for Market Dynamics

Decoding OTC Government Bond Market
Liquidity: An ABM Model for Market Dynamics
1st Alicia Vidler
dept. Engineering
UNSW, Australia
a.vidler@unsw.edu.au
2nd Toby Walsh
dept.Engineering
UNSW, Australia
t.walsh@unsw.edu.au
Abstract—The over-the-counter (OTC) government bond mar-
kets are characterised by their bilateral trading structures, which
pose unique challenges to understanding and ensuring market
stability and liquidity. In this paper, we develop a bespoke
ABM that simulates market-maker interactions within a stylised
government bond market. The model focuses on the dynamics of
liquidity and stability in the secondary trading of government
bonds, particularly in concentrated markets like those found
in Australia and the UK. Through this simulation, we test key
hypotheses around improving market stability, focusing on the
effects of agent diversity, business costs, and client base size.
We demonstrate that greater agent diversity enhances market
liquidity and that reducing the costs of market-making can
improve overall market stability. The model offers insights
into computational finance by simulating trading without price
transparency, highlighting how micro-structural elements can
affect macro-level market outcomes. This research contributes
to the evolving field of computational finance by employing
computational intelligence techniques to better understand the
fundamental mechanics of government bond markets, providing
actionable insights for both academics and practitioners.
Index Terms —Bond market simulations, liquidity, market
stability, Agent-based modelling, Agentic AI
I. I NTRODUCTION
The liquidity of OTC government bond markets plays a
critical role in the functioning of modern financial systems,
influencing both market stability and economic policy im-
plementation. Unlike equity markets, which are centralised
and provide large amounts of public transaction data, OTC
bond markets operate through decentralised networks of par-
ticipants, with comparatively little public data, often creating
challenges in understanding market dynamics and liquidity
flows. Liquidity, in this context, refers to the ease with which
bonds can be bought or sold within a reasonable time frame, or
rather ”liquidity is the ability to trade when you want to trade”
[1]. Despite its importance, market liquidity in OTC bond
markets remains difficult to quantify and predict, particularly
during periods of stress when liquidity can evaporate suddenly,
triggering broader financial instability [2].
To address this, we propose an ABM designed to simulate
the micro-level interactions of key participants (clients and
market makers) within the OTC government bond market.
This work is funded in part by an ARC Laureate grant FL200100204
ABM’s are particularly suited to this challenge, as they allow
the examination of complex, decentralised systems where indi-
vidual behaviours and local interactions give rise to emergent
phenomena at the macro scale [3]. A particular challenge for
researches of bilateral bond markets is that data in this field is
sparse and bond trade level data is not freely available [2]. To
address this we model the dynamics between market makers,
the data for which is partially available to the public, isolating
their trading behaviours and liquidity provision through agent
to agent trading and client interaction. In addition to liquidity,
we are also concerned with the related concept of market
stability. The World Bank defines financial market stability as
”the absence of system-wide episodes in which the financial
system fails to function” [4], with the International Monetary
Fund going so far as to define the stability of certain financial
markets, such as that of the UK system as a ”global public
good” [5].
In this study, we first design an ABM that is able to
replicate observable Australian market characteristics. We se-
lect the Australian government bond OTC market to design
our bespoke ABM, leverage its unique blend of international
relevance and local specificity. Whilst smaller than the UK,
or Canada, the Australian market shares essential structural
features with larger ones due to their common heritage of
British market design. Like the UK, the Australian market
is characterised by a small number of key market makers
(MM), operating in a decentralised, over-the-counter regulated
framework. The Australian market offers a relative richness
and accessibility of data. Detailed reports from the Australian
Office of Financial Management (AOFM) and other gov-
ernment bodies provide a public picture of market activity,
such as aggregated MM market share and market structure.
This comparative level of transparency allows for stylised
calibration of ABMs, making the Australian bond market an
attractive choice for academic study. There is no reason to
suppose that results formed on the Australian market cannot
be generalised to other markets (e.g. UK, Canada).
In this paper, we investigate key aspects of market liquidity
and stability. First, we examine how the diversity of mar-
ket makers influences these factors. Our simulations reveal
that increasing the heterogeneity of market makers—through
varying trading costs and client base sizes—enhances market
trading, liquidity, and stability more effectively than merely©2024 IEEE. Personal use of this material is permitted. Permission from
IEEE must be obtained for all other uses, in any current or future media,
including reprinting/republishing this material for advertising or promotional
purposes, creating new collective works, for resale or redistribution to servers
or lists, or reuse of any copyrighted component of this work in other works.
Dec 15, 2024
arXiv:2501.16331v1  [q-fin.TR]  15 Dec 2024

increasing their number. Diverse agent characteristics promote
more frequent interactions and stabilise liquidity provision.
In contrast, markets populated by homogeneous agents, re-
gardless of their quantity, tend to become fragile and unstable
after a certain number of trading steps. This underscores the
importance of fostering diversity in trading behaviours and
strategies to maintain a resilient market structure.
Our second key hypothesis explores the impact of reducing
operational costs for agents and expanding their client bases.
We find that lowering business costs for market makers leads
to a more stable and liquid market by boosting transaction
volumes and extending the duration of stable operations. These
findings highlight the nuanced relationship between agent
characteristics, market design, and liquidity, offering insights
into regulatory policies that could enhance market efficiency.
The paper is organised as follows. In Section 2, we review
the literature on ABM design and bond market modelling.
Section 3 introduces our custom ABM, detailing how we
represent key market features within a framework inspired by
Axtell’s Sugarscape model. Section 4 presents our results. Fi-
nally, Section 5 concludes with a brief summary and discusses
areas for future research 1.
II. L ITERATURE REVIEW : B OND MARKETS AND AGENTS
Agent-based models lack a consensus approach for calibra-
tion [6]. The bilateral nature of bond market trades hinders
direct observation of agents’ utility functions and policies
[7], impeding the application of machine learning techniques
successfully used in calibrating ABMs for observable markets
like foreign exchange [8]–[10]. These techniques often rely
on features absent in bilateral bond markets, such as homoge-
neous agent classes, observable environments, or comprehen-
sive regulatory data [11]–[13].
Global bond markets, including the Australian government
bond market, involve diverse participants acting as agents:
banks as trading facilitators (market makers), institutional
investors (debt purchasers), and trading firms like hedge
funds (clients) [14]. Unlike centralized equity exchanges,
bond trading occurs over-the-counter (OTC) across fragmented
electronic platforms. The Australian bond market exemplifies
this decentralised landscape, lacking a dominant trading venue
and operating through opaque bilateral transactions facilitated
by the four major retail banks designated as market makers
[15], while being systemically important to both Australia and
the global trading landscape [16].
Government bond prices are significantly impacted by cen-
tral banks’ interest rate policies, inflation expectations [17],
and periodic interest payments, unlike stock markets driven by
supply and demand. Although bond prices inversely relate to
market-expected yields and can price in potential rate changes,
they largely reflect current rate policies—publicly available
information. Holding a bond provides interest returns, making
access to bond market liquidity more important, as returns can
be generated by holding the asset. Our contribution is to model
1Code available :https://github.com/AliVidl/ABM-for-Bond-Markets
the movement of bonds across market participants, focusing
on liquidity flow characteristics.
A. Market Micro-structure and Trading Venues
The lack of publicly available data for empirical validation
is a key challenge in simulating bilateral markets like bond
markets [2]. While macro trading data indicates domestic mar-
ket makers traded between themselves on average 27.23% of
all secondary market bond turn over in Australia since 2016 2,
granular details on individual trades and participant strategies
remain obscured. Bilateral transactions are mediated through a
handful of electronic messaging platforms [15]. Recent efforts
to launch a joint venture centralising bond market transaction
data collection [18] underscore possibilities for future research.
In line with regulatory demands for transaction visibility [19],
our work offers a fresh modelling approach to the evolving
market micro structure. Due to the current lack of data, our
model relies on stylised facts and government documentation.
B. Bond trading modelling
Literature on bond markets predominantly addresses bond
pricing models [17], [20]–[23] and alternative pricing methods
[24], with limited exploration of market design aspects [25]–
[27]. Prior to 2008, bond markets grappled with interest
rate volatility and uncertainty, making bond price models
crucial. Recent work using ABMs to simulate interactions
between interdependent agents [28]–[31] discusses challenges
in capturing the complex dynamics across various applications.
Integrating concepts of the Adaptive Market Hypothesis [32],
ABM frameworks like SugarScape [33] and MESA [34]–[37]
have been applied to study artificial societies and complex
systems. Our contribution combines and expands these areas to
bond trading and liquidity provision in OTC markets without
price transparency.
Recent advancements include incorporating reinforcement
learning techniques to train agent models in financial mar-
kets, often reducing participants to two homogeneous groups:
liquidity providers or consumers [9], [38]. Our work moves
beyond this binary categorisation to include heterogeneous
agents for increased model richness.
C. Crisis and Market Structure Research
Studies examining market structure and liquidity in the UK
government bond market [2] provide a detailed analysis of
the 2022 UK gilt market crisis, underscoring the fragility
of government bond markets and inspiring our modelling.
The work highlights risks posed by concentrated market
makers and sudden liquidity evaporation, paralleling crises
in other sovereign bond markets, including U.S. Treasury
market disruptions in 2020 [19], [39]. These events reveal
vulnerabilities in OTC markets where liquidity providers strug-
gled during extreme volatility, emphasising the critical role
of regulatory frameworks and market design in maintaining
stability, particularly in markets dominated by a few key
participants. A major contribution of our model to existing
2https://www.aofm.gov.au/data-hub

ABM literature is exploring liquidity in an OTC government
bond market to understand how diverse factors contribute to
stability or fragility. A growing body of literature is examining
the efficiency of markets and the potential for ”chaos” to be
a distinct market feature [38] [40]. Adding to the complexity
of market microstructure analysis.
III. M ODEL : A B ESPOKE ABM I MPLEMENTATION BASED
ON SUGARSCAPE
We build a bespoke ABM, drawing heavily from Sug-
arscape, the model introduced by [33] used to simulate com-
plex, artificial societies through agent-environment interac-
tions. Many adaptations of this work exist [34]–[37], [41].
The model’s ability to represent small populations of heteroge-
neous agents, interacting asynchronously, aligns closely with
the bilateral structure of government bond markets, making it
an ideal foundation for the bespoke ABM used in this research.
Other ABM model frameworks were considered (such as [42]),
however these tend to require extensive calibration and do
not suit the bilateral market focus of this study. To develop
our bespoke model, several open-source tools were leveraged,
including repositories from GitHub [43], [44] following the
framework provided by [34].
A. Agents
The model consists of N agents, representing market mak-
ers (MM’s). We will use the term agent and MM inter-
changeable in this paper. In the Australian market, four key
institutional market makers dominate, reflecting a structure
where fewer MMs interact with a large number of clients,
as noted by [45]. Additionally we model a cost structure for
agents to represent fixed operational costs incurred by agents
per time step.
1) Vision: Client base and breadth: All financial firms
have clients, and in the case of MM’s these are the firms
and people they are required to buy and sell bonds with
under the terms of their government registration. Within the
model we characterise the difference in MM size through their
different client breadth (i.e. grid vision range) vi, determining
how far they can access client resources across the landscape.
For an agent at position (xi, yi), the set of visible cells is:
Vi = {(x, y) | |x − xi| ≤vi and |y − yi| ≤vi}. This range
is randomly assigned as vi ∼ Uniform(1, 49) such that the
maximum any MM can access is the whole of the grid (i.e.
less than 50 units) and remains constant during the simulation.
2) Cost of Doing Business: Metabolism: Each MM incurs a
cost at each time step, representing various business overheads,
modelled as a form of metabolism. The bond and cash
holdings of an agent i at each time step are updated as follows:
Ab(t+1) =Ab(t)+( br −mb), Ac(t+1) =Ac(t)+( cr −mc).
Where mb and mc represent the bond and cash metabolic
rates. These costs are assigned at the start and remain constant,
influencing an agent’s ability to survive and stay in business.
B. Clients
Clients are represented by static locations a 50x50 grid,
totaling 2,500 distinct clients based on data from [2]. Each
grid cell (x, y) corresponds to a client holding bonds B(x,y)
and cash C(x,y), modelled as a tuple: Ci = R(x,y) =
(B(x,y), C(x,y)). Each client is assigned a heterogeneous quan-
tity of a generic government bond, and cash amount. Bonds
and cash are distributed in mounds across the grid, with values
decreasing from the centre of the mounds outward upon the
grid. Due to the lack of observable real-world distribution of
bondholders, we chose to concentrate resources in four distinct
regions on the grid. Future research may refine this assumption
as more data becomes available.
C. MM servicing clients
Market makers (MMs) are assigned a fixed client range,
modeled as a form of grid ”vision,” allowing them to ”see”
client locations within a maximum grid distance at each stage.
This enables MMs to locate client resources within their field
of vision on the grid. Agents exit the market when either
their bond or cash holdings reach zero ( Ab = 0 or Ac = 0).
MMs acquire bonds and cash from passive clients, reflecting
the key aspect of over-the-counter (OTC) markets where all
client trading involves a market maker—a feature effectively
captured in our ABM design.
D. Market Maker Trading
After servicing clients at each time step, market makers
(MMs) consider potential trades with other agents within their
field of vision, provided the trade improves welfare for both
parties. Welfare improvement addresses imbalances in cash or
bonds held by an MM, aligning with rational and legal trading
behaviour as outlined in finance literature and regulations [46].
Each agent’s welfare for bonds and cash is calculated as:
W elf areai,b = A
mb
mb +mc
b , W elf areai,c = A
mc
mb +mc
c .
Where Ab and Ac are the agent’s accumulations of bonds
and cash, and mb and mc are the respective costs. Small cost
values relative to initial accumulations are used.
For a trade to occur, agents compare the product of their
current welfare to the potential new welfare after the trade:
ˆW elf areai,b × ˆW elf areai,c ≥ W elf areai,b × W elf areai,c
This condition must hold for both trading agents, ensuring mu-
tual welfare improvement. This eliminates the need for a price
mechanism, as agents trade based on relative needs, reflecting
the limited price transparency in the modelled markets.
Agents compare their Marginal Rate of Substitution (MRS),
indicating their relative need for bonds or cash. Trades occur
when agents have offsetting needs, and the exchange quan-
tity is determined using the geometric mean of their MRS,
reducing bias from extreme values as proposed by [47].
The MRS for an agent ai is defined as MRS ai = (
Ac
mc ) Ab
mb
. A
higher MRS reflects a stronger preference for cash over bonds,
and vice versa, based on survival needs in the model.
Definition 1. We define an ABM formally as: M =
⟨N, L, S, P, D, A, f, T⟩, where N = {a1, a2, . . . , an} is the
set of market making agents, with n = 4 in this case. L

represents the set of landscape states, each containing assets
R = {br, cr}, corresponding to bond and cash quantities of
individual clients. Each agent ai has a state Si, which includes
bond and cash usage (i.e. their individual cost structure) rates
mb, mc, accumulations Ab, Ac, and a client base breadth vi.
The perception functions Pi map the landscape and other
agents’ states to a perceived state, pij : L ∪ S →R, while
the decision rules Di map perceptions and states to actions,
dik : Pi × Si → Ai. Agent actions Ai include client servicing,
trading with other market makers, and ceasing operations.
The landscape evolves according to the transition function
f : L × A → L, with no bond or cash replenishment, and
the model progresses through discrete time steps, T = N.
E. Model Dynamics
The model dynamics are governed by the iterative interac-
tions of the components in M. At t = 0, MMs are randomly
assigned positions on a grid X × Y , with no preferential
locations, simulating the varying client access that MM’s
experience daily. Each MM perceives the environment L and
the states of other agents S within their field of vision, then
selects an action based on its decision rule. MMs’ accumulated
bonds and cash are decremented to cover business costs, set at
the inception of each epoch. MMs also have the option to trade
with each other when a utility difference exists, exchanging
bonds or cash based on perceived liquidity imbalances between
their holdings. If an MM’s resources are depleted ( Ab = 0or
Ac = 0), they cease operations.
After each action, the landscape and agent states are up-
dated, adjusting resource variables br and cr accordingly. The
process iterates across all agents and over time until all agents
have ceased operations or the maximum time T is reached.
The ABM does not allow any agent coalition formation, in
light with real world regulatory constraints on market makers.
Our model makes key assumptions to streamline its design.
First, clients are passive, always ready to trade, and fully
transparent about their resources within their client base. While
this simplifies interactions and limits realism, it allows the
focus to remain on agent-to-agent interactions, justified by the
lack of available data on client holdings. Second, we assume
that market makers (MMs) truthfully reveal their resource
levels to others and do not store data about previous accumu-
lations, aligning with market regulations on fair dealing. We
do not model MM strategic coalition formation, which can be
contrary to policy [48]. These assumptions simplify the model
by avoiding complex information exchange dynamics and fit
within the regulated bond trading environment.
F . Available Data
Publicly available data from the AOFM reports the amount
of MM to MM trading as a share of total secondary mar-
ket trading in Australian government bonds. This data is
released quarterly, with data available at a quarterly level from
September 2016 to June 2024, aggregated across all market
participants. See Table I and Figure 1.
Statistic Value (%)
Mean 27.23
Median 27.27
Quarterly Std Dev 4.54
Minimum 15.94
Maximum 36.69
First Quartile (Q1) 23.85
Third Quartile (Q3) 30.17
Interquartile Range (IQR) 6.33
TABLE I: Aggregated quarterly Summary Statistics of Inter-
bank trading volume market share: Sep 2016 to June 2024
Sep 16Mar 17Sep 17Mar 18Sep 18Mar 19Sep 19Mar 20Sep 20Mar 21Sep 21Mar 22Sep 22Mar 23Sep 23Mar 24
20
30
40
Quarter
Interbank Percentage (%)
Interbank Percentage
Fig. 1: Quarterly Interbank Percentage of Secondary Aus-
tralian Government Bond Trading
IV. R ESULTS
We calibrated our ABM to the Australian MM environment,
successfully replicating the observed first and second order
attributes. Using the design and model variables listed in Table
II, we conducted 100 simulations (epochs), producing over
200,000 agent interactions. We explored calibration sets oppor-
tunistically rather than exhaustively testing all permutations of
model variables, which would be intractable. We refer to this
configuration as the ”Australian calibration” or (Hypothesis
1: HP1).
Our simulations reveal a median MM-to-MM trading oc-
currence of 28.74% of all interactions. This median trading
activity aligns closely with data published by the Australian
Office of Financial Management (AOFM), which reports an
eight-year average interbank bond turnover of 27.3% of traded
volumes. This close correspondence validates our model’s
ability to replicate real-world trading patterns.
The results demonstrate a high degree of variance across
simulations, as illustrated in Figure 2. This variance is ex-
pected given the large degrees of freedom in the initial calibra-
tions for each simulation. On average, the trading frequency
in the model aligns closely with reported aggregate trading
volumes, serving as a reasonable approximation for such
an opaque market. Further research is needed to determine
whether these factors contribute to the market ”chaos” Ad-
ditionally, we note that the reported figures are aggregated
over three months of daily trading without reporting variance
or week-to-week volatility. Nevertheless, the range of trading

interactions remains broad, with summary statistics provided
in Table III (rounded to two decimal places).
Variable Description
Number of Agents 4
Client Breadth 1 to 50 units (random)
Cost 1 to 5 units per time step (random)
Initial Resource Accumulation 35 to 55 units (random)
Size of Client Base 2500 clients
Trading Occurrence Median 28.74% per model simulation
Number of Simulations Over 100
Time Steps per Simulation Up to 1500
Agent Moves per Trading Hour Approximately 200
Simulation Order Asynchronous and randomised
TABLE II: Summary of Variables in the Simulation
0%10%19%29%38%48%57%67%76%86%
0
10
20
% of each Simulation that trades
Simulations
Frequency
0
20
40
60
80
100
Cumulative %
Cumulative %
Fig. 2: A=4 Distribution across Runs by Trading Percent
Statistic Epoch Trade Percentage
Median 28.54
Std Dev 27.48
Min 1.22
25% 11.03
50% 28.54
75% 59.77
Max 95.11
TABLE III: Summary Statistics for Epoch Trade Percentage
A. Market Makers Numbers: Do we need more?
We explore the hypothesis that agent diversity, rather than
simply increasing the number of agents, has a positive impact
on interactions and trading liquidity. To illustrate our findings,
we report two examples, each consisting of 100 simulation
epochs of agent models.
• (Hypothesis 2: HP2) - We keep N = 4 and maintain
the same costs but reduce the possible range of client
base sizes from a theoretical maximum of 50 units to
just 5 units. In each epoch, agents are randomly assigned
a value within this reduced range for the duration of the
simulation. By narrowing the range from 1–50 units to
1–5 units, we significantly decrease the maximum client
base size and reduce agent-to-agent diversity in client
base sizes (as agents can now assume only one of 5
possible client size values instead of 50). The result is
a series of simulations where almost no MM-to-MM
trading occurs. In fact, over 73% of epochs exhibit no
market maker trading whatsoever (see figure 3). This
contrasts with the Australian calibration, where agents
with client ranges of 1–50 units engage in MM-to-MM
trading on average 28% of the time, and 100% of epochs
display some market maker trading, however small.
0% 1% 2% 3% 4% 5% 6% 7% 8% 9%10%
0
50
100
150
% of each Simulation that trades
Simulations
Frequency
0
20
40
60
80
100
Cumulative %
Cumulative %
Fig. 3: A=4 Client and Cost reduction (median 0.8%). Stress-
ing the Australian calibration to much lower client breadth and
business cost effectively shuts down market maker trading to
zero in 73% of epochs with an average trade amount of less
than 1% of all activity
• (Hypothesis 3: HP3) To test the impact of number of
clients, We keep the same reduced client base and same
business costs as in HP2 but increase agents to 16 (or 4
times as many). We see more trades than in HP2, but
still far fewer MM to MM trades than the Australian
calibration set - just 6.418% of the time (see figure 4).
0% 2% 4% 6% 8% 9%11%13%15%17%
0
10
20
% of Each Simulation that Trades
Simulations
Frequency
0
20
40
60
80
100
Cumulative %
Cumulative %
Fig. 4: N = 16 - distribution of trade occurrences, as a
percentage for each simulation. Cumulative distribution shows
a mean of just 6.49% as reported
Whilst not a complete analysis of all possibilities, these two
specific examples demonstrate that the number of agents
cannot make up for the benefits that come from having a wide

variety of agent client sizes, such as in HP1. We document that
by increasing agents, while reducing client size and keeping
cost levels (and range) low, dramatically reduce trading in all
epochs. As agents select a level from a lower range of client
options, reducing client breath has the impact of decreasing
agent heterogeneity also. Market makers in these scenarios
simply have less differentiation between themselves also. Even
when increasing the number of agents to 16 (significantly
beyond that of our Australian market calibration of just 4), we
see that the amount of trading between agents is significantly
reduced from 28% in HP1 to under 7% in HP3 and virtually
halted in HP2. From this we conclude that increasing the
heterogeneity of market makers rather than simply the number
of agents contributes to greater market trading activity and
hence liquidity.
B. Impact of lowering Agent costs and Market Stability
The concept of agent lifespan, in terms of time steps, was
evaluated in relation to stability and liquidity provision. The
results demonstrate that low agent costs tend to enhance agent
longevity, which can be associated with higher stability in
market trading. We utilise the two tests again, this time looking
at populations of 4 agents across 100 epochs where client
breadth is set to be diverse (1 - 50 units in line with HP1)
but costs are set to be higher (with a range of 5-10 units).
This test can then be directly compared to the tests using the
Australian MM calibration simulations, which has the same
calibration set but a cost range of just 1- 5 units.
• HP1 the Australian market calibration, approximately
27.2% of interactions are between market makers. Also,
68% of epochs had at least one agent still servicing clients
and ”alive” at the maximum time step of t = 1500. We
can see in figure5b and figure5a that agents in epochs
where they had lower costs have longer life spans.
(a) Impact of cash costs
 (b) Impact of bond costs
• (Hypothesis 4: HP4) - We stress costs to double the
level in HP1. The results are quite stark: average life
spans of each epoch is less 17 time steps, with less
than 4,000 interactions across all 100 epochs. Individual
epochs show significant early collapse (around 10 or so
time steps), but, across a small number of time steps,
there is a large degree of trading with other market
makers (median of 46%). The key outcome appears to be
that increasing (doubling) costs significantly weakens the
trading landscape (see figure6) leading to situations where
Fig. 6: High costs, very short life span: Market Instability
the landscape fails to function, meeting the definition of
instability provided by the World Bank [4].
V. S UMMARY , C ONCLUSIONS AND FUTURE WORK
Our work contributes to the literature by offering a sim-
ulation framework that captures key elements of OTC bond
market structure, while also accounting for liquidity and
market stability concerns. By leveraging a bespoke ABM,
we replicate observable market phenomena in the Australian
government bond market. This allows us to explore theoretical
scenarios that can inform policy decisions, such as the impact
of market maker client diversity and cost structures.
Maintaining stable market functioning is not only vital for
societal functions, but is also essential for regulatory bodies,
such as the World Bank, International Monetary Fund and
Bank of England. Balancing client servicing and agent-to-
agent trade is fundamental to ensure the network’s viability.
We show that MM trading can be effectively halted in 73%
of simulations ( HP2) when client ranges are reduced to
a maximum of 10% of the Australian market calibration.
However, increasing the number of agents in this scenario from
4 to 16 ( HP3) improves liquidity but it remains significantly
less activity and liquidity than HP1 - the Australian market
calibration.
Our final conjecture tests the impact of trading costs on
stability looking at MM trading and lifespan. We see in HP4,
that doubling trading costs from the simulations in HP1,
produce drastically smaller lifespans of agents (HP1 over 68%
of agents lived past 1500 time steps, in HP4, no agent lived
beyond just 17 time steps. From this we conclude the markets
with lower costs find stability easier to maintain.
Future work may explore enhancing the model’s richness
and accuracy by incorporating more comprehensive market
data as it becomes available. Additionally, we intend to explore
alternative approaches to model client behaviours and asset
distributions to further enrich our model’s ability to reflect
real-world market behaviour. Additional analysis of market
internal mechanisms will also be carried out.

REFERENCES
[1] L. Harris, Trading and Exchanges: Market Microstructure for Practi-
tioners. Oxford University Press, New York, 2003.
[2] G. Pinter, “An anatomy of the 2022 gilt market crisis,” SSRN Electronic
Journal, vol. Bank of England Working Paper 1019, 2023.
[3] M. Wooldridge, An Introduction to MultiAgent Systems, Second Edition .
John Wiley and Sons, 2009.
[4] W. B. Group, “Financial stability,” accessed: [25 Sep 2024].
[Online]. Available: https://www.worldbank.org/en/publication/gfdr/
gfdr-2016/background/financial-stability
[5] B. of England, “Financial stability in focus: The fpc’s approach
to assessing risks in market-based finance,” 2023, accessed: [25
Sep 2024]. [Online]. Available: https://www.bankofengland.co.uk/
financial-stability-in-focus/2023/october-2023
[6] P. Avegliano and J. S. Sichman, “Using surrogate models to calibrate
agent-based model parameters under data scarcity,” inProceedings of the
18th International Conference on Autonomous Agents and MultiAgent
Systems, 2019, pp. 1781–1783.
[7] K. Boggess, S. Kraus, and L. Feng, “Toward policy explanations for
multi-agent reinforcement learning,” arXiv preprint arXiv:2204.12568 ,
2022.
[8] L. Ardon, N. Vadori, T. Spooner, M. Xu, J. Vann, and S. Ganesh,
“Towards a fully rl-based market simulator,” Proceedings of the Second
ACM International Conference on AI in Finance , Nov 2021. [Online].
Available: http://dx.doi.org/10.1145/3490354.3494372
[9] N. Vadori, L. Ardon, S. Ganesh, T. Spooner, S. Amrouni, J. Vann, M. Xu,
Z. Zheng, T. Balch, and M. Veloso, “Towards multi-agent reinforcement
learning driven over-the-counter market simulations,” 2022.
[10] S. Ganesh, N. Vadori, M. Xu, H. Zheng, P. Reddy, and M. Veloso,
“Reinforcement learning for market making in a multi-agent dealer
market,” arXiv preprint arXiv:1911.05892 , 2019.
[11] P. Bank, I. Ekren, and J. Muhle-Karbe, “Liquidity in competitive dealer
markets,” Mathematical Finance, vol. 31, no. 3, p. 827–856, Apr 2021.
[Online]. Available: http://dx.doi.org/10.1111/mafi.12305
[12] A. Barzykin, P. Bergault, and O. Gu ´eant, “Algorithmic market making in
foreign exchange cash markets with hedging and market impact,” arXiv
preprint arXiv:2106.06974, 2021.
[13] R. Cont and M. S. Muller, “A stochastic partial differential equation
model for limit order book dynamics,” SIAM Journal on Financial
Mathematics, vol. 12, no. 2, pp. 744–787, 2021.
[14] B. of England, “Gemm guidebook: A guide to the roles of the
dmo and primary dealers in the uk government bond market,”
Bank Of England , December 2004. [Online]. Available: https:
//dmo.gov.uk/media/22bbjndz/guidebook200921.pdf
[15] Australian Financial Review, “Bond market players call
time on $6 trillion aussie exchange,” 2023, accessed:
2023-04-23. [Online]. Available: https://www.afr.com/chanticleer/
bond-market-players-call-time-on-6-trillion-aussie-exchange-20230525-p5db5n
[16] R. B. of Australia, “Government-bond-markets-in-advanced-
economies-during-the-pandemic,” Reserave Bank of Australia , 2021.
[Online]. Available: www.rba.gov.au/publications/bulletin/2021/sep/
government-bond-markets-in-advanced-economies-during-the-pandemic.
html
[17] D. Duffie and K. J. Singleton, “Modeling term structures of defaultable
bonds,” Review of Financial Studies , 1999.
[18] TradeWeb, “Bloomberg, marketaxess and tradeweb sign joint
venture agreement,” 2023, accessed: 2023-04-23. [Online]. Avail-
able: https://www.tradeweb.com/newsroom/media-center/news-releases/
bloomberg-marketaxess-and-tradeweb-sign-joint-venture-agreement
[19] D. Duffie, “Still the World’s Safe Haven?” Hutchins Working Paper ,
vol. 62, 2020.
[20] F. A. Longstaff and E. S. Schwartz, “A simple approach to valuing risky
fixed and floating rate debt,” Journal of Finance , 1995.
[21] F. Black and J. C. Cox, “Valuing corporate securities: Some effects of
bond indenture provisions,” Journal of Finance , 1976.
[22] R. C. Merton, “On the pricing of corporate debt: The risk structure of
interest rates,” Journal of Finance , 1974.
[23] J. Liang, H.-M. Yin, X. Chen, and Y . Wu, “On a corporate bond
pricing model with credit rating migration risksand stochastic interest
rate,” Quantitative Finance and Economics , vol. 1, no. 3, pp. 300–319,
2017. [Online]. Available: https://www.aimspress.com/article/doi/10.
3934/QFE.2017.3.300
[24] C. Albanese and A. Vidler, “Dynamic conditioning and credit
correlation baskets,” University Library of Munich, Germany, MPRA
Paper, 2008. [Online]. Available: https://EconPapers.repec.org/RePEc:
pra:mprapa:8368
[25] K. Braun-Munzinger, Z. Liu, and A. Turrell, “An agent-based model of
corporate bond trading,” Quantitative Finance, 2018.
[26] C. Collver, “An application of agent-based modeling to market structure
policy: the case of the u.s. tick size pilot program and market maker
profitability,” SEC, 2017.
[27] Y . Lin, J. Xue, and L. Raschid, “Predicting the behavior of dealers in
over-the-counter corporate bond markets,” ICAIF, 2020.
[28] S. Bai, W. Raskob, W. Raskob, T. M ¨uller, and T. M ¨uller, “Agent based
model,” Radioprotection, 2020.
[29] G. Fagiolo, M. Guerini, F. Lamperti, A. Moneta, and A. Roventini, “Val-
idation of agent-based models in economics and finance,” Simulation
Foundations, Methods and Applications , 2017.
[30] J. Lussange, A. Belianin, S. Bourgeois-Gironde, and B. Gutkin, “Learn-
ing and cognition in financial markets: A paradigm shift for agent-based
models,” IntelliSys, 2020.
[31] A. Vermeir and H. Bersini, “Best practices in programming agent-based
models in economics and finance,” Lecture Notes in Economics and
Mathematical Systems, 2015.
[32] A. W. Lo, “The adaptive markets hypothesis: Market efficiency from an
evolutionary perspective,” The Journal of Portfolio Management , 2004.
[33] J. M. Epstein and R. L. Axtell, Growing Artificial Societies: Social
Science from the Bottom Up , ser. MIT Press Books. The MIT
Press, 1996. [Online]. Available: https://ideas.repec.org/b/mtp/titles/
0262550253.html
[34] T. D. Pike, “Multi-level mesa.” arXiv: Multiagent Systems , 2019.
[35] David Masad and Jacqueline Kazil, “Mesa: An Agent-Based Modeling
Framework,” in Proceedings of the 14th Python in Science Conference ,
Kathryn Huff and James Bergstra, Eds., 2015, pp. 51 – 58.
[36] T. Pike, S. Golden, D. Lowdermilk, B. Luong, and B. Rosado, “Growing
the simulation ecosystem: introducing mesa data to provide transparent,
accessible, and extensible data pipelines for simulation development,”
SIMULATION, 2021.
[37] J. Kazil, D. Masad, D. Masad, and A. Crooks, “Utilizing python for
agent-based modeling: The mesa framework,” SBP-BRiMS, 2020.
[38] W. A. Brock and C. H. Hommes, “Heterogeneous beliefs and routes to
chaos in a simple asset pricing model,” Journal of Economic Dynamics
and Control, vol. 22, no. 8, pp. 1235–1274, 1998.
[39] T. U. T. Department and Board, “Recent Disruptions and potential
reforms in the U.S Treasury market: A STAFF PROGRESS REPORT,”
U.S Federal Reserve, no. May, 2011.
[40] L. Inglada-perez, “A comprehensive framework for uncovering non-
linearity and chaos in financial markets: Empirical evidence for four
major stock market indices,” Entropy, vol. 22, no. 12, pp. 1–26, 2020.
[41] R. L. Axtell and J. D. Farmer, “Agent-Based Modeling in Economics
and Finance: Past, Present, and Future,” Journal of Economic Literature,
pp. 1–96, 2022.
[42] T. Balch and team, “Abides (agent-based interactive discrete event
simulation),” 2020, a high-performance, agent-based market simulation
platform. [Online]. Available: https://github.com/abides-sim/abides
[43] J. Kazil, D. Masad, and A. Crooks, “Utilizing python for agent-based
modeling: The mesa framework,” in Social, Cultural, and Behavioral
Modeling, R. Thomson, H. Bisgin, C. Dancy, A. Hyder, and M. Hussain,
Eds. Cham: Springer International Publishing, 2020, pp. 308–317.
[44] J. Kehoe, “The specification of sugarscape,” CoRR, vol. abs/1505.06012,
2015. [Online]. Available: http://arxiv.org/abs/1505.06012
[45] J. Cheshire, “Market Making in Bond Markets,” RBA Bulletin March
Quater 2015 , no. March, pp. 63–74, 2015. [Online]. Available:
https://rba.gov.au/publications/bulletin/2015/mar/7.html
[46] B. of England, “Official Operations in the Gilt Market An Operational
Notice ,” Bank of England , vol. December, 2023.
[47] C. D. RICH, “The rationale of the use of the geometric average
as an investment index,” Journal of the Institute of Actuaries
(1886-1994), vol. 74, no. 2, pp. 338–339, 1948. [Online]. Available:
http://www.jstor.org/stable/41138034
[48] TP ICAP, “Best execution,” May 2021, accessed: [2 Jan 2024].
[Online]. Available: https://tpicap.comBestExecution.pdf
