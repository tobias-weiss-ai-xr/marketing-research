---
title: A Multi-agent Market Model Can Explain the Impact of AI Traders in Financial Markets -- A New Microfoundations
  of GARCH model
url: https://arxiv.org/abs/2409.12516
category: ai-marketing
subcategory: empirical
date: 2024-09
venue: ''
authors:
- Kei Nakagawa
- Masanori Hirano
- Kentaro Minami
- Takanobu Mizuta
source: arxiv
pdf_url: https://arxiv.org/pdf/2409.12516
pages: 16
chars: 39552
fetched_at: '2026-11-08T13:17:47+00:00'
kb_version: 1
---

# A Multi-agent Market Model Can Explain the Impact of AI Traders in Financial Markets -- A New Microfoundations of GARCH model

A Multi-agent Market Model Can Explain the
Impact of AI Traders in Financial Markets – A
New Microfoundations of GARCH model
Kei Nakagawa1[0000−0001−5046−8128], Masanori Hirano2[0000−0001−5883−8250],
and Kentaro Minami3 and Takanobu Mizuta4[0000−0003−4329−0645]
1 Nomura Asset Management Co,Ltd., Japankei.nak.0315@gmail.com
2 Preferred Netqorks, Inc., Japanresearch@mhirano.jp
3 PayPay Corporation, Japanresearch@ktrmnm.jp
4 SPARX Asset Management Co., Ltd., Japanmizutata@gmail.com
Abstract. The AI traders in financial markets have sparked signifi-
cant interest in their effects on price formation mechanisms and market
volatility,raisingimportantquestionsformarketstabilityandregulation.
Despite this interest, a comprehensive model to quantitatively assess the
specific impacts of AI traders remains undeveloped. This study aims to
address this gap by modeling the influence of AI traders on market price
formation and volatility within a multi-agent framework, leveraging the
concept of microfoundations. Microfoundations involve understanding
macroeconomic phenomena, such as market price formation, through the
decision-making and interactions of individual economic agents. While
widely acknowledged in macroeconomics, microfoundational approaches
remain unexplored in empirical finance, particularly for models like the
GARCH model, which captures key financial statistical properties such
as volatility clustering and fat tails. This study proposes a multi-agent
market model to derive the microfoundations of the GARCH model, in-
corporating three types of agents: noise traders, fundamental traders,
and AI traders. By mathematically aggregating the micro-structure of
these agents, we establish the microfoundations of the GARCH model.
We validate this model through multi-agent simulations, confirming its
ability to reproduce the stylized facts of financial markets. Finally, we
analyze the impact of AI traders using parameters derived from these
microfoundations, contributing to a deeper understanding of their role
in market dynamics.
Keywords: AI Trader · GARCH model · microfundation · financial
market · simulation
1 Introduction
The advancement of various machine learning algorithms has markedly increased
the presence of AI traders in financial markets, drawing significant attention to
This paper does not reflect the view of the organizations the authors belong to. All
errors in this paper are the responsibility of the authors.
arXiv:2409.12516v1  [q-fin.CP]  19 Sep 2024

2 K. Nakagawa et al.
their potential impact on these markets. Understanding how AI traders influ-
ence price formation mechanisms and market volatility is crucial for maintaining
market stability and informing regulatory perspectives [17,18]. However, a com-
prehensive model to quantitatively capture the specific impacts of AI traders
has not yet been fully established. In this study, we aim to model the effects of
the presence and decision-making processes of AI traders on market price for-
mation mechanisms and volatility, utilizing a multi-agent modeling framework
and leveraging the concept of microfoundations.
The effort to understand macroeconomic phenomena, such as market price
formation, through the decision-making and interactions of economic agents, is
known as microfoundations. In macroeconomics, the significance of microfoun-
dations has been widely recognized, leading to the development of numerous
macroeconomic models incorporating microfoundations [14,13]. Conversely, at-
tempts to provide microfoundations for price fluctuation models in empirical fi-
nance are relatively sparse. For instance, the GARCH (Generalized AutoRegres-
sive Conditional Heteroscedasticity) model, an extension of the ARCH model [8],
is extensively used in finance to model conditional variance in various empirical
studies [23,11]. This is because the GARCH model effectively reproduces typical
financial statistical properties, known as stylized facts [6], such as volatility clus-
tering5 and fattails6. While [21] provides microfoundations for theARCHmodel,
the microfoundations for the GARCH model remain underexplored. Specifically,
it is unclear how the parameters of the GARCH model arise from the micro-level
decision-making processes or the proportions of different investors. The validity
of multi-agent modeling is often evaluated based on its ability to reproduce these
stylized facts [4].
Our objective is to construct the GARCH model through microfoundations
and ensure that our model can reproduce the stylized facts of financial mar-
kets represented by the GARCH model. The validity of multi-agent modeling
is evaluated based on whether they can reproduce the stylized facts[4]. We aim
to construct the GARCH model throgh microfoundations and ensure that our
model can reproduce the stylized facts of financial markets represented by the
GARCH model.
Based on the above, we propose a multi-agent market model that can analyze
the impact of AI traders on financial markets by deriving the microfoundations
of the GARCH model. Our multi-agent market model includes three types of
agents: noise traders, fundamental traders, and AI traders. By mathematically
solving the aggregation of the micro-structure of the multi-agent market model,
5 This refers to the phenomenon where large (resp. small) changes in asset prices
are often followed by large (resp. small) changes, indicating that volatility tends to
cluster together over time. This results in periods of high volatility and periods of
low volatility within financial markets.
6 This refers to the statistical property of a probability distribution where the tails
(extremes) are fatter than those of a normal distribution. Fat tails are often quanti-
fied using kurtosis, a measure of the "tailedness" of the distribution. Distributions
with high kurtosis exhibit fat tails, indicating a greater likelihood of observing values
far from the mean.

A New Microfoundations of GARCH model 3
we demonstrate the microfoundations of the GARCH(1,1) model. Furthermore,
through multi-agent simulations, we validate the multi-agent market model and
confirm the replication of market stylized facts. Finally, we discuss the impact
of AI traders using parameters derived from the microfoundations.
2 Related Work
Research on the impact of traders on financial markets has increased significantly
with the rapid expansion of new technologies such as algorithmic trading and AI.
Various approaches have been employed to evaluate the influence of traders on
the market. We review key prior studies on the impact of traders, their analysis
using multi-agent models, and the perspective of microfoundations, highlighting
the positioning of this study.
This study aims to bridge the gap in understanding the impacts of AI traders
on market price formation and volatility by leveraging a multi-agent modeling
approach grounded in microfoundations. Previous research has extensively ex-
plored high-frequency trading and various trader types, but the specific quan-
titative impacts of AI traders remain underexplored. Our work addresses this
gap by developing a novel multi-agent market model that includes noise traders,
fundamental traders, and AI traders, capturing their decision-making processes
and interactions to analyze their collective influence on financial markets.
We develop the concept of microfoundations to the GARCH(1,1) model,
demonstrating how its parameters can arise from the micro-level behaviors of
different traders. This bridges a crucial gap in empirical finance, where the mi-
crofoundations of the GARCH model have been underexplored. By providing
new insights into how AI traders affect market volatility and price formation, our
research offers valuable information for market stability and regulatory frame-
works. This study advances the theoretical understanding of AI traders’ impact
and addresses the existing gap in empirical finance, offering practical implica-
tions for market participants and policymakers.
2.1 Impact of T raders on the Market
The initial research on the impact of traders primarily focused on high-frequency
trading (HFT). Hendershottet al.[12] demonstrated that HFT improves market
liquidity and reduces trading costs. However, it has also been suggested that
HFT could increase market volatility [3]. These studies imply that the impact
of traders on the market is not straightforward.
Other research has explored the broader impact of various types of traders.
For instance, Kirilenkoet al.[15] analyzed the role of different trader types in the
flashcrashof2010,showinghowtheirinteractionscontributedtoextrememarket
events. These studies highlight the complex dynamics and potential systemic
risks posed by different trading strategies.

4 K. Nakagawa et al.
2.2 Multi-Agent Models for Market Analysis
To analyze the impact of traders, multi-agent models have been widely used.
Lebaron et al. [16] studied the effect of interactions among agents with differ-
ent trading strategies on market dynamics using an artificial market. This re-
search demonstrated the utility of agent-based models in capturing the emergent
properties of financial markets. Chenet al.[4] employed an agent-based model
to evaluate the influence of algorithmic traders on market price formation and
volatility. Their work showed how the inclusion of algorithmic traders can lead
to different market behaviors and identified key factors that influence these out-
comes. These studies provide a foundational understanding of how agent-based
modeling can be applied to financial markets to assess the impact of traders.
2.3 Microfoundations Perspective
Farmer et al. [10] provided a microfoundational approach to price formation
by modeling the behavior of heterogeneous agents and their impact on market
prices. Similarly, Luxet al. [19] developed a model that captured the scaling
laws observed in financial markets by incorporating the interactions of traders
with different strategies. They argued that heterogeneous agents and their inter-
actions are necessary to replicate stylized facts through a multi-agent simulation
study. Because they utilized simulation rather than mathematical analysis, their
methods are a bit different from those of the microfoundation, but their moti-
vation is very similar. These studies illustrate the potential of microfoundations
to explain observed market phenomena through the lens of individual agent be-
havior.
3 Multi-agent Market Model
In this section, we define the decision-making model for each trader and the
price determination process used in our multi-agent market model.
3.1 Return Model
The return model rt we use in this study is GARCH(1,1) [2], which is widely
used in financial markets analysis and defined as:
rt = f (xt−1, It−1) + ut (1)
ut = σtεt, εt ∼ N (0, 1) (2)
σ2 t = ω + αu2 t−1 + βσ 2 t−1 (3)
where rt is the return at timet, xt−1 and It−1 are the fundamental variable and
the set of information (e.g., historical return, sentiment indicators) available for
prediction up to timet − 1.
f is an appropriate function for explaining future returns based on funda-
mental values and exogenous information.

A New Microfoundations of GARCH model 5
This setting is consistent with the semi-strong form of efficient market hy-
pothesis [9], i.e., the assumption that all publicly available information is taken
into account in the asset return.ut = rt − f (xt−1, It−1) is the residual term.
Furthermore, ω >0 and α + β <1 are necessary for satisfying the stationarity
of the GARCH model.ω and α mean the constant volatility and the sensitivity
to past return shocks, respectively.β is the dependence on past volatility, which
is necessary to replicate volatility clustering.
The expected returnsEt−1[rt] and the varianceVt−1[rt] are calculated as:
Et−1[rt] = Et−1[f (xt−1, It−1)] + Et−1[ut] = f (xt−1, It−1) (4)
Vt−1[rt] := Et−1[(rt − Et−1[rt])2] = ω + αu2 t−1 + βσ 2 t−1. (5)
Hereafter, Et−1[·] is the conditional expectation andVt−1[·] is the conditional
variance up to timet − 1.
3.2 T rader Model
We assume the existence of three types of traders in our market model:
1. Noise traders who provide liquidity,
2. F undamental traders who make decisions based on fundamental variables,
3. AI traders who make decisions based on the model predictions learned from
past market time series.
Noise T radersNoise traders are based on the existence of traders who generate
orders probabilistically due to exogenous reasons [24]. These exogenous reasons
include investment adjustments over individual traders’ life cycles, portfolio re-
balancing for hedging purposes, and passive investment strategies that follow
indices, such as indices weighted by market capitalization.
We assume that noise traders place orders uniformly, irrespective of the fun-
damental prices. Consequently, noise traders play the role of providing liquidity.
F undamental T raders Next, we assume the existence of risk-averse funda-
mental traders who make decisions based on the fundamental variablext−1 at
the previous time stept − 1. Specifically, we assume the utility functionU (·) of
the returns for the fundamental tradersrF,t at the time step t. These traders
are risk-averse investors, meaning that their utility function satisfiesU ′ > 0 and
U ′′ < 0.
Here, we employ the utility functionU depending on the mean and standard
deviation (not variance) of their returnsrF,t. Furthermore, we assume that:
Et−1[rF,t] = g(xt−1) (6)
Vt−1[rF,t] = σ2 t−1 (7)
where g is a monotonic function and σt−1 is defined previous section. That
means, when fundamental traders obtain information at timet−1, they generally

6 K. Nakagawa et al.
suppose a monotonically expected return on the fundamental variable, and the
variance of this return isσ2 t−1 available at timet − 1. Thus, the expected utility
U of the fundamental traders can be written as follows:
Et−1[U (rF,t)] = Et−1[rF,t] − λ
q
Vt−1[rF,t] = g(xt−1) − λσt−1 (8)
where the risk aversion coefficient isλ >0.
In the field of finance, the risk-averse expected utility is generally described
by the mean and variance[20]. Note that for fundamental traders in this study,
utility function is based on the mean and standard deviation. In general, the use
of the mean and standard deviation instead of the mean and variance for the risk-
averse utility function can be justified under certain conditions [25]. Specifically,
(1) if the utility function is a quadratic function ofr, or (2) if the probability
distribution of r is normal. However, these are quite strong assumptions. In
particular, since the aim of this study is to reproduce stylized facts, normality
cannot be required. Therefore, in this paper, we assume the following, which is a
more relaxed condition that includes the normal distribution: The standardized
probability distribution ofrF,t is independent of the values of the expected value
and the standard deviation. The lemma 1 justifies this condition.
Lemma 1. If the standardized probability distribution of the random variabler
is independent of the values of the expected valueµ and the standard deviation
σ, i.e., if the probability distributionϕ(ϵ) of ϵ = (r − µ)/σ does not depend on
µ and σ, then an increase in the standard deviation results in a decrease in the
expected utility (allowing the use of the standard deviation as a risk measure).
Proof. The proof is given in the Appendix.
AI T raders AI traders are assumed to train each own prediction modelh that
effectively explains the past return seriesrt, t= 1, · · ·, T. We assumed that they
also have a utilityM (·) based on the model.
That is, under a certain loss functionL, the modelh is trained by minimizing
the following:
min
h
X
t
L(rt, h(xt−1, It−1)) (9)
where It−1 is the set of information available for prediction up to timet − 1 as
the same as that in the previous section.
In this study, we use the squared loss functionL(x, y) = ( x − y)2, which is
commonly used in regression tasks. Therefore, we minimize:
min
h
X
t
(rt − h(xt−1, It−1))2 (10)
to train the modelh.
Next, let the utility function of the returnsrA,t for the AI traders be denoted
by M (·). These traders are assumed to be risk-averse investors, meaning that

A New Microfoundations of GARCH model 7
M ′ > 0 and M ′′ < 0. Similar to fundamental traders, we assume that theM of
rA,t is determined by its mean and standard deviation. Furthermore, we assume
that rA,t is given by the modelh as follows:
Et−1[rA,t] = h(xt−1, It−1) (11)
Vt−1[rA,t] = Et−1

(rt−1 − Et−1[h(xt−2, It−2)])2 (12)
This means when AI traders obtain available information until timet − 1, they
estimate an expected return based on the model. Moreover, the risk is assumed
to be the prediction error (standard deviation) of the model available at time
t − 1:
p
Vt−1[rA,t]. Thus, the expected utility of AI traders can be written as:
Et−1[M (rA,t)] = Et−1[rA,t] − γ
q
Vt−1[rA,t] (13)
= h(xt−1, It−1) − γEt−1 |rt−1 − Et−1[h(xt−2, It−2)]| (14)
where γ(> 0) is a risk aversion coefficient. The utility is based on the prediction
value, penalized for the prediction deviation from the modelh.
3.3 Pricing Model
Our model employs a simple price model based on the order imbalance, which
is proposed in a previous work [22].
In the price model, the price returnrt based on the order imbalance is cal-
culated as:
rt = ρ Ab t − As t
Ab t + As t (15)
where Ab t is the total buy orders,As t is the total sell orders, andρ is the constant
coefficient of the order imbalance.
Moreover, Ab t , As t are defined as:
Ab t = 1 2 S (1 + p1Et−1[U (rF,t)] + p2Et−1[M (rA,t)])
+ 1 2 kS(1 + p1Et−1[U (rF,t)] + p2Et−1[M (rA,t)])εt (16)
As t = 1 2 S (1 − p1Et−1[U (rF,t)] − p2Et−1[M (rA,t)])
− 1 2 kS(1 + p1Et−1[U (rF,t)] + p2Et−1[M (rA,t)])εt (17)
where S, kare constant variables representing the liquidity,p1 and p2 are the
ratios of fundamental and AI traders over noise traders, respectively.p1 + p2
indicates the ratio of investors who take liquidity from the market to those who
provide liquidity (noise traders). Additionally,Et−1[U (rF,t)] and Et−1[M (rA,t)]
are the utility functions of fundamental and AI traders defined by equations (8)

8 K. Nakagawa et al.
and (18), respectively. The first term represents the constant total order quan-
tities placed by noise, fundamental, and AI traders. The second term represents
the difference in buy and sell orders due to demand-supply imbalances. The
constant k indicates the order quantities generated due to demand-supply im-
balances relative to the constant total order quantities, which highly affects how
much demand and supply imbalances take liquidity from the market. A larger
value of k implies lower liquidity.
4 Theoretical Analysis: The Microfoundations of
GARCH
In this section, we derive the microfoundations of GARCH based on the multi-
agent market model explained in the previous section. The final goal of this
section is to derive the GARCH parameters (f, ω, α, β) in equation (3) using the
parameters defined in the previous section.
First, Et−1[h(·)] = f (·) is reasonably assumed because the effort to find well-
predictable model h is the same as the finding the ground truth function f.
Thus, equation (13) can be re-formulated as:
Et−1[M (rA,t)] = h(xt−1, It−1) − γEt−1 |rt−1 − Et−1[h(xt−2, It−2)]| (18)
= h(xt−1, It−1) − γ |rt−1 − f (xt−2, It−2)| (19)
= h(xt−1, It−1) − γ |ut−1| (20)
Since the total volume of buy and sell orders is given by the equations (16)
and (17), substituting them into the equation (15) in the pricing model as:
rt = ρ(p1Et−1[U (rF,t)] + p2Et−1[M (rA,t)])
+ ρk {1 + p1Et−1[U (rF,t)] + p2Et−1[M (rA,t)]]} εt (21)
= ρ(p1(g(xt−1) − λσt−1) + p2(h(xt−1, It−1) − γ|ut−1|))
+ ρk{1 + p1(g(xt−1) − λσt−1) + p2(h(xt−1) − γ|ut−1|))}εt. (22)
Therefore, Et−1[rt] and Vt−1[rt] can be derived as:
Et−1[rt] = ρ(p1(g(xt−1) − λσt−1) + p2(h(xt−1) − γ|ut−1|)), (23)
Vt−1[rt] = ρ2k2(1 + p2 1g(xt−1)2 + p2 2h(xt−1)2) + ρ2k2p2 2γ2u2 t−1 + ρ2k2p2 1λ2σ2 t−1.
(24)
Compared with equations (4) and (5) in the GARCH(1,1) model, we can prove
the following theorem.
Theorem 1 (Microfoundation of GARCH Model). The parameters of the
equation (3) are given by the microfoundation as:
ω = ρ2k2{1 + p2 1g(xt−1)2 + p2 2h(xt−1, It−1)2}, (25)
f = ρ{p1(g(xt−1) − λσt−1) + p2(h(xt−1, It−1) − γ|ut−1|)}, (26)
α = ρ2k2p2 2γ2, β = ρ2k2p2 1λ2 (27)

A New Microfoundations of GARCH model 9
Theorem 1 provides a significant contribution to understanding the microfoun-
dations of the GARCH(1,1) model by linking it to the behaviors and interactions
of different types of traders in a financial market. Several key insights and im-
plications can be drawn from this theorem:
In a market where noise, fundamental, and AI traders exist, there are
Constant volatility(ω ̸= 0): The parameter ω represents the constant com-
ponent of volatility in the GARCH model. According to the theorem,ω is
influenced by the aggregate behaviors of noise, fundamental, and AI traders.
This implies that even in the absence of external shocks, the inherent trading
activities of these agents contribute to a baseline level of market volatility.
Incorporation of information( f ̸= 0): The parameter f in the theorem in-
dicates that fundamental variables and available information up to timet−1
are incorporated into market returns. This aligns with the semi-strong form
of the efficient market hypothesis, suggesting that market prices reflect all
publicly available information.
Sensitivity to past shocks( α ̸= 0): The parameter α signifies the market’s
sensitivity to past price shocks. The theorem shows thatα is directly related
to the trading activities of AI traders, particularly their risk aversions. The
existence of AI traders is also amplifying market responses to past events.
V olatility clustering(β ̸= 0): The parameter β represents the persistence of
volatility over time. The theorem linksβ to the dependence on past volatility,
driven by fundamental traders’ risk aversions. The volatility clustering is
a crucial characteristic of financial markets, and this theorem provides a
microfoundational explanation for this phenomenon.
Below, we derive the results of the microfoundations of the GARCH model
when we assume the non-existence of each trader based on Theorem 1.
When only the noise traders exist in markets ( p1 = 0, p2 = 0), Theorem
1 can be reformulated as:
ω = ρ2k2, (28)
f = α = β = 0. (29)
We can derive the following proposition:
Proposition 1 (Microfoundation of the GARCH model in a market
with only noise traders). When only the noise traders exist in markets (p1 =
0, p2 = 0), there are
Constant volatility(ω ̸= 0): The volatility ω depends on the variance of the
order imbalance (ρ) and liquidity (k).
Exclusion of information( f = 0): The parameter f being zero indicates that
information has no impact on market prices when only noise traders are
present. This contrasts with markets where fundamental and AI traders are
active, suggesting that the presence of noise traders alone does not incorpo-
rate information into asset pricing.

10 K. Nakagawa et al.
Absence of response to past shocks( α = 0): The parameterα being zero sig-
nifies that the market does not exhibit sensitivity to past price shocks when
only noise traders are present.
No V olatility Clustering(β = 0): The parameter β being zero indicates the
absence of volatility clustering in a market with only noise traders because
noise traders’ actions do not create persistent volatility patterns.
When the noise and fundamental traders exist in markets ( p1 >
0, p2 = 0), Theorem 1 can be reformulated as:
ω = ρ2k2(1 + p2 1g(xt−1)2), (30)
f = ρp1(g(xt−1) − λσt−1), (31)
α = 0, β= ρ2k2p2 1λ2. (32)
This leads to the following proposition:
Proposition 2 (Microfoundation of the GARCH model in a market
with the noise and fundamental traders). When the noise and fundamental
traders exist in markets (p1 > 0, p2 = 0), the following are satisfied:
Constant volatility(ω ̸= 0): The parameter ω is influenced by the order im-
balance (ρ) and liquidity (k), as well as the trading activities of fundamental
traders.
Incorporation of F undamental Information( f ̸= 0): The presence of fun-
damental traders ensures that fundamental variables are reflected in market
prices. This is crucial for market efficiency.
No Response to Past Shocks( α = 0): The absence of AI traders means that
the market does not exhibit sensitivity to past price shocks.
V olatility Clustering(β ̸= 0): The parameter β being non-zero indicates that
volatility clustering occurs in markets with noise and fundamental traders.
The presence of fundamental traders, who react to fundamental variables,
contributes to this persistent volatility pattern.
When the noise and AI traders exist in markets ( p1 = 0, p2 > 0),
theorem 1 can be reformulated as:
ω = ρ2k2(1 + p2 2h(xt−1, It−1)2), (33)
f = ρp2(h(xt−1, It−1) − γ|ut−1|), (34)
α = ρ2k2p2 2γ2, β= 0 (35)
We can derive the following proposition:
Proposition 3 (Microfoundation of the GARCH model in a market
with the noise and AI traders). When the noise and AI traders exist in
markets (p1 = 0, p2 > 0), the following are satisfied:

A New Microfoundations of GARCH model 11
Constant volatility ( ω ̸== 0): The parameterω is influenced by the order im-
balance (ρ) and liquidity (k), as well as the presence of AI traders.
Incorporation of Information ( f ̸= 0): The parameter f being non-zero in-
dicates that the information processed by AI traders is incorporated into mar-
ket prices. This suggests that the trading strategies of AI traders ensure that
their predictive information is reflected in asset pricing.
Response to Past Shocks ( α ̸= 0): The parameterα being non-zero signifies
that the market exhibits sensitivity to past price shocks due to the presence of
AI traders. This shows the role of AI traders in amplifying market responses
to historical price movements.
No V olatility Clustering ( β = 0): The parameter β being zero indicates the
absence of volatility clustering in a market with only noise and AI traders
because their actions do not create persistent volatility patterns.
5 Simulation Experiment
5.1 Experimental Settings
In the previous section, we discuss the mathematical structure without a spe-
cific definition for g and h for fundamental and AI traders. In this section, we
temporarily define those functions and other parameters and check how the nu-
merical simulation works well by checking stylized facts, which are well-known
phenomena in financial markets.
For the parameters, we employedρ = 4, k = 0.4, p1 = 0.2, p2 = 0.4, λ = 1.2,
γ = 1 .2. Those parameters are empirically decided, andp1 and p2 are set to
satisfy the situation that enough liquidity traders exist in the simulation. The
fundamentalvariable xt wasgeneratedbyarandomvariablefollowingastandard
normal distribution. The log utility function is employed forg:
g(xt−1) = log(1 + max(−0.99, xt−1)). (36)
For h, the auto-regressive (AR) process is assumed:
h(xt−1, It−1) = 0.1xt−1. (37)
We simulate the return series ˆrt based on equation (15). We evaluate the
validity of the multi-agent market model based on whether it can reproduce
stylized facts [4].
We evaluate several stylized facts usingˆrt: negative skewness, higher kur-
tosis than the normal distribution (leptokurtic), non-normality (Kolmogorov-
Smirnov; KS test), and positive autocorrelation of the square of returns (volatil-
ity clustering). The generated time series length is denoted byˆT = 1000.
The skewness is defined as:
Skewness =
1
ˆT
P ˆT
t=1(ˆrt − ¯r)3

1
ˆT
P ˆT
t=1(ˆrt − ¯r)2
3/2 (38)

12 K. Nakagawa et al.
where ¯r is the mean of the return series. A negative skewness value indicates a
distribution with a long tail on the left side (the loss side), suggesting that small
losses occur frequently along with occasional large losses.
The kurtosis is defined as:
Kurtosis =
1
ˆT
P ˆT
t=1(ˆrt − ¯r)4

1
ˆT
P ˆT
t=1(ˆrt − ¯r)2
2 (39)
A high kurtosis value means that the distribution of returns is sharper than a
normal distribution, indicating that values near the center (mean) are concen-
trated, and extreme values (very high returns or very large losses) occur more
frequently than expected.
The KS test evaluates whether the return series follows a normal distribution.
The KS test statistic is defined as:
KS statistics = sup
x
|Fˆrt (x) − Fnormal(x)| (40)
where Fˆrt (x) is the empirical cumulative distribution function (CDF) ofˆrt and
Fnormal(x) is the CDF of the normal distribution with the same mean and vari-
ance as ˆrt. The KS test would reject the null hypothesis if the returns exhibit
non-normal characteristics.
The τ-order autocorrelation of the square of returns is defined as:
Autocorrelation(τ ) =
P ˆT
t=τ +1(ˆr2 t − ¯r2)(ˆr2 t−τ − ¯r2) P ˆT
t=1(ˆr2 t − ¯r2)2
(41)
for lag tau. This measure indicates the presence of volatility clustering, where
large price changes are likely to be followed by other large price changes. The
1st-order autocorrelation is defined byτ = 1.
These stylized facts are derived from previous works, such as [7], and pro-
vide a comprehensive evaluation of the multi-agent market model’s ability to
reproduce real market behaviors.
5.2 Simulation Results
Table 1: Statistics on generated return series.∗p<0.1; ∗∗p<0.05; ∗∗∗p<0.01.
Skewness (< 0) -1.880***
Kurtosis (> 3) 9.230***
KS statistics 0.788***
1st-order autocorrelation (> 0) 0.367***
Table 1 summarizes the statistics for the generated return series, with signif-
icance levels indicated by asterisks.

A New Microfoundations of GARCH model 13
The results from Table 1 demonstrate that the multi-agent market model
successfully generates return series that exhibit key stylized facts observed in
real financial markets. The significant negative skewness and high kurtosis in-
dicate that the generated returns can capture the asymmetric and heavy-tailed
nature of financial returns. The significant KS statistic further confirms that the
generatedreturnsdonotfollowanormaldistribution,aligningwithempiricalob-
servations in financial data. The positive autocorrelation of the square of returns
suggests that the generated returns effectively replicate volatility clustering.
The sample paths of the generated return series are shown in Figure 1a. The
histograms of returns are also shown in Figure 1b. These visual representations
further support the statistical findings summarized in Table 1. The distribution
of returns exhibits a non-normal, heavy-tailed property, with noticeable skewness
to the left, indicating frequent small losses and occasional large losses. The return
series demonstrates periods of high volatility interspersed with periods of relative
calm, reflecting the volatility clustering.
(a) Generated return time-series
(b)Thereturndistributionofthe
generated return series
Fig.1: Comparison of generated return time-series and their distribution
6 Discussion
Firstly, the new multi-agent market model proposed in this study is consistent
with some previous studies. Our model covers a wide range of models, includ-
ing some previous works, because the functions of each trader are not defined
specifically, especially in AI traders. For example, Chiarellaet al. [5] proposed
a model based on fundamental trends and noise traders. Because AI traders’
definition can cover the trend predicting traders, it also can be covered by our
theory. Therefore, our microfoundations could be applicable to a wide range of
models.
Second, this study newly achieves the microfoundation of the GARCH model,
and our proposed model has been proven valid through theoretical analysis and

14 K. Nakagawa et al.
Table 2: Comparison of Market with Different Trader Types
Market Type Baseline
V olatility (ω)
Incorporation
of
Information
(f )
Response to
Past Shocks
(α)
V olatility
Clustering ( β)
Only Noise
Traders
(p1 = 0, p2 = 0)
Eq. (28) - - -
Noise and
Fundamental
Traders
(p1 > 0, p2 = 0)
Eq. (30) Eq. (31) - Eq. (32)
Noise and AI
Traders
(p1 = 0, p2 > 0)
Eq. (33) Eq. (34) - Eq. (35)
Noise,
Fundamental,
and AI Traders
(p1 > 0, p2 > 0)
Eq. (25) Eq. (26) Eq. (27) Eq. (27)
multi-agent simulations. Previously, the GARCH model was purely empirical,
lacking theoretical validation. However, through our microfoundation, we have
provided a theoretical basis for the GARCH model. This represents significant
progress in the field of financial markets, as the GARCH model is widely used
in various applications.
Third, our microfoundation revealed many insights into the previously unex-
plained parameters in the GARCH model. Through our microfoundations, these
parameters can now be explained using parameters related to micromechanisms
in financial markets. This provides a clearer understanding of market dynamics.
According to our results, if more fundamental traders exist in a market,
volatility clustering appears much more. If the ratio of fundamental tradersp1
increased, β in the GARCH model would increase according to theorem 1. Orig-
inally, β is the autocorrelation coefficient for volatility according to equation 3.
Therefore, a high ratio of fundamental tradersp1 means that the strength of the
volatility clustering becomes high.
Moreover,whenmoreAItradersexistinamarket,amoresignificantresponse
to the shock would happen, and overshooting tends to happen more. If the ratio
of AI tradersp2 increased, α in the GARCH model would increase according to
theorem 1. Originally,α is the coefficient for the square of diffusion termu2 t−1 in
the equation 3. Therefore, if there exist more AI traders in markets, the response
to the exogenous diffusion, i.e., market shocks, becomes bigger, and the market
turbulence becomes bigger than the expected market shocks.
Table 2 summarizes our results derived from our microfoundations regarding
the different trader types in the market.

A New Microfoundations of GARCH model 15
7 Conclusion
In this study, we proposed a novel multi-agent market model incorporating fun-
damental traders, noise traders, and AI traders. Our model, rooted in mar-
ket micro-structure, reveals new microfoundations of the GARCH(1,1) model.
Throughbothmathematicalanalysisandextensivesimulationstudies,wedemon-
strated that our multi-agent model can derive the GARCH formula and replicate
key stylized facts observed in financial markets, such as volatility clustering and
fat tails.
Our findings highlight the ability of the new microfoundations to describe
marketstructuresandthedynamicsresultingfromdifferentproportionsoftrader
types, including AI traders and their decision-making. Our model offers insights
into how various trader interactions contribute to market behavior and volatility.
Future research directions include extending this framework to multivariate
GARCH models[1] to capture more complex market dynamics. Moreover, this
study employs a very simple and basic pricing model based on order imbalance as
equation 15. Therefore, we should also consider the other pricing models such as
the double auction market mechanism as the same as the actual markets. Finally,
estimating the actual proportions of different types of traders in real-world mar-
kets remains a critical area for further investigation. These efforts will enhance
our understanding of the impact of AI traders and other market participants,
ultimately contributing to more stable and efficient financial markets.
References
1. Bauwens, L., Laurent, S., Rombouts, J.V.: Multivariate garch models: a survey.
Journal of applied econometrics21(1), 79–109 (2006)
2. Bollerslev, T.: Generalized autoregressive conditional heteroskedasticity. Journal
of econometrics 31(3), 307–327 (1986)
3. Brogaard, J., et al.: High frequency trading and its impact on market quality.
Northwestern University Kellogg School of Management Working Paper66, 10
(2010)
4. Chen, S.H., Chang, C.L., Du, Y.R.: Agent-based economic models and economet-
rics. The Knowledge Engineering Review27(2), 187–219 (2012)
5. Chiarella,C.,Iori, G.:A simulation analysisofthe microstructureof doubleauction
markets. Quantitative Finance2(5), 346–353 (2002).https://doi.org/10.1088/
1469-7688/2/5/303
6. Cont, R.: Empirical properties of asset returns: stylized facts and statistical issues.
Quantitative finance 1(2), 223 (2001)
7. Cont, R.: Empirical Properties of Asset Returns: Stylized Facts and Statistical
Issues. Quantitative Finance 1(2), 223–236 (2001). https://doi.org/10.1080/
713665670
8. Engle, R.F.: Autoregressive conditional heteroscedasticity with estimates of the
variance of united kingdom inflation. Econometrica: Journal of the econometric
society pp. 987–1007 (1982)
9. Fama, E.F.: Efficient capital markets. Journal of finance25(2), 383–417 (1970)
10. Farmer, J.D., Joshi, S.: The price dynamics of common trading strategies. Journal
of Economic Behavior & Organization49(2), 149–171 (2002)

16 K. Nakagawa et al.
11. Francq, C., Zakoian, J.M.: GARCH models: structure, statistical inference and
financial applications. John Wiley & Sons (2019)
12. Hendershott, T., Jones, C.M., Menkveld, A.J.: Does algorithmic trading improve
liquidity? The Journal of finance66(1), 1–33 (2011)
13. Hoover, K.D.: Reductionism in economics: Intentionality and eschatological justi-
fication in the microfoundations of macroeconomics. Philosophy of Science82(4),
689–711 (2015)
14. Janssen, M.: Microfoundations: A critical inquiry. Routledge (2005)
15. Kirilenko, A., Kyle, A.S., Samadi, M., Tuzun, T.: The flash crash: High-frequency
trading in an electronic market. The Journal of Finance72(3), 967–998 (2017)
16. LeBaron, B.: Evolution and time horizons in an agent-based stock market. Macroe-
conomic dynamics 5(02), 225–254 (2001)
17. Lee,J.:Accesstofinanceforartificialintelligenceregulationinthefinancialservices
industry. European Business Organization Law Review21(4), 731–757 (2020)
18. Leitner, G., Singh, J., van der Kraaij, A., Zsámboki, B.: The rise of artificial in-
telligence: benefits and risks for financial stability. Financial Stability Review1
(2024)
19. Lux, T., Marchesi, M.: Scaling and criticality in a stochastic multi-agent model of
a financial market. Nature397(6719), 498–500 (1999)
20. Markowitz, H.M., Todd, G.P.: Mean-variance analysis in portfolio choice and cap-
ital markets, vol. 66. John Wiley & Sons (2000)
21. Mizuta, T.: Micro-foundation of arch model. Available at SSRN 2710457 (2016)
22. Mizuta, T., Yagi, I., Izumi, K.: Development of an evaluation method for ar-
tificial market settings considering a realistic pricing mechanism. Transactions
of the Japanese Society for Artificial Intelligence27(6), 320–327 (2012). https:
//doi.org/10.1527/tjsai.27.320
23. Nakagawa, K.,Imamura, M., Yoshida,K.: Risk-basedportfolioswith largedynamic
covariance matrices. International Journal of Financial Studies6(2), 52 (2018)
24. Peress, J., Schmidt, D.: Glued to the tv: Distracted noise traders and stock market
liquidity. The Journal of Finance75(2), 1083–1133 (2020)
25. Tobin, J., et al.: The theory of portfolio selection. The theory of interest rates364,
364 (1965)
A Proof of lemma 1
Proof. Refer to [25]. Sinceϕ(ϵ) does not depend onµ and σ, the expected utility
can be expressed as a function ofµ and σ:
E[U ] = Eµ,σ[U ] =
Z ∞
−∞
U (µ + σϵ)ϕ(ϵ)dϵ (42)
By differentiating this with respect toσ and showing that the derivative is non-
positive:
∂Eµ,σ[U ]
∂σ =
Z ∞
−∞
U ′(µ + σϵ)ϵϕ(ϵ)dϵ ≤ 0 (43)
To prove this, letU ′(µ) = c. Since U is risk-averse, U ′ is a decreasing function.
Therefore, in the region whereϵ <0, c < U′(µ + σϵ), and in the region where
ϵ ≥ 0, c ≥ U ′(µ+σϵ).Thus,theintegralin(43)isnotgreaterthan R cϵϕ(ϵ)dϵ = 0,
proving the lemma.
