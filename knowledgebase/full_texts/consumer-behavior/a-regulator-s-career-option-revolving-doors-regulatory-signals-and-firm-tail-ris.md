---
title: 'A Regulator''s Career Option: Revolving Doors, Regulatory Signals, and Firm Tail Risk'
url: https://arxiv.org/abs/2610.08804
category: consumer-behavior
subcategory: empirical
date: 2026-08
venue: ''
authors:
- G. Charles-Cadogan
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.08804
pages: 26
chars: 70744
fetched_at: '2026-11-08T13:17:52+00:00'
kb_version: 1
---

# A Regulator's Career Option: Revolving Doors, Regulatory Signals, and Firm Tail Risk

A Regulator’s Career Option: Revolving Doors,
Regulatory Signals, and Firm Tail Risk ∗
G. Charles-Cadogan †
Working Paper
October 8, 2026
Abstract
This paper develops a model of revolving doors in which a regulator designs policy signals that
affect a regulated firm’s capital structure while holding an implicit career option to leave public
service and join the regulated firm or its advisers. The model has three linked mechanisms.
First, regulatory signals alter the firm’s admissible pricing and leverage choices by changing
the tradeoff between consumer surplus and firm profit. Second, because the regulator’s outside
payoff is convex in the value of the regulated firm, the value of the regulator’s career option
increases with firm value, leverage, and signal-induced volatility. Third, when signal-induced
volatility raises the option vega of firm equity, the same mechanism can increase tail risk and
lower distance to default. A proof-of-concept calibration illustrates the model’s leverage-vega
warning regions and shows how a regulator-induced signal can move a firm from a go-leverage
region into an early-warning or crash-risk region. The calibration is extended with maturity
comparisons, a sensitivity grid over compensation convexity and initial leverage, a bank-like
parameter anchor, stochastic signal simulations, and a stopping-horizon diagnostic. External
evidence from federal payroll data on post-employment restrictions supports the model’s career-
option primitive, while the exercises also organize historical regulatory failures: Lehman Broth-
ers as a regulatory-vacuum case, Silicon Valley Bank as a distorted-signal and weak-supervision
case, and Signature Bank as a converted-signal case in which post-public-service incentives and
lighter oversight coincided with rapid growth, uninsured-deposit exposure, and tail risk. The
model does not predict collapse dates; it helps explain and predict when regulatory forbearance,
weak debt penalties, and career-option incentives can delay binding oversight until firms cross
a leverage-vega warning threshold.
Keywords: career option, revolving door, capital structure, leverage, vega, managerial com-
pensation
JEL Classification Codes: G01, G18, G28, G38, J24, J44, J45, L51
∗This paper benefited from the detailed comments of Samuel Myers, Jr. and Gary Dymski. We thank seminar
participants at the University of Leicester and conference participants at the Academy for Behavioral Finance &
Economics (Robert B. Durand, discussant), the Southern Finance Association (Rachel Graefe-Anderson, discussant),
the ESSA Biennial Meeting, and the Midlands Economic Theory and Applications Workshop. We are also grateful to
Paul Kupiec, Leonard Nakamura, Doug Robertson, Ernesto Dal B´ o, Oliver Martin, Tony Leiman, Linwood Tauheed,
Michael Crew, Rebel Cole, Asha Sundaram, Peter Hammond, and Haim Abraham for their valuable comments and
advice. Any errors which may remain are ours. We gratefully acknowledge the research support of the Institute for
Innovation and Technology Management.
†University of Leicester, School of Business, Leicester, LE2 1RQ; Tel: +44 (0)116 229 7385; e-mail: go-
cadog@gmail.com
arXiv:2610.08804v1  [econ.GN]  18 Aug 2026

Contents
1 Introduction 1
2 The Model 3
2.1 Welfare effects of embedding regulator signals in capital structure . . . . . . . . . . . 3
2.2 Stock options with regulatory signalling . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.3 Valuation of regulator career option and capital structure of the firm . . . . . . . . . 8
2.3.1 Regulator career option pricing with signalling . . . . . . . . . . . . . . . . . 9
2.3.2 Bankruptcy warning signals: Firm vega and leverage . . . . . . . . . . . . . . 10
3 Proof-of-Concept Calibration 12
3.1 Robustness and quantitative comparative statics . . . . . . . . . . . . . . . . . . . . 15
3.2 Historical regulatory-signal diagnostics . . . . . . . . . . . . . . . . . . . . . . . . . . 18
4 Conclusion 19
Appendices 19
A Abstract legislative mechanism design for embedding regulator signals 19
References 21
List of Figures
1 Mechanism sketch: regulatory signal, firm response, and career-option feedback . . . 3
2 Impact of regulator signalθon price (p) and firm profits Π . . . . . . . . . . . . . . 5
3 Optimal Capital Structure Under Static Theory with Perpetual Debt . . . . . . . . . 11
4 Firm vega (ϑ) and leverageLfor given risk signalσ(θ) with early warning and
bankruptcy windows . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
5 Proof-of-concept calibration diagnostics . . . . . . . . . . . . . . . . . . . . . . . . . 14
6 Linear and quadratic proof-of-concept signal paths . . . . . . . . . . . . . . . . . . . 15
7 Maturity and parameter-sensitivity diagnostics . . . . . . . . . . . . . . . . . . . . . 16
8 Stochastic signal and stopping-horizon diagnostics . . . . . . . . . . . . . . . . . . . 17
9 Regulator’s abstract mechanism design . . . . . . . . . . . . . . . . . . . . . . . . . . 20
List of Tables
1 Proof-of-concept leverage-vega classification . . . . . . . . . . . . . . . . . . . . . . . 14
2 Quadratic-signal proof-of-concept classification . . . . . . . . . . . . . . . . . . . . . 15
3 Robustness calibration summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
ii

1 Introduction
This paper studies a revolving-door problem in which a regulator can affect a firm’s capital
structure while contemplating a future move to that firm, a lobbying organization, or an affili-
ated consultancy. The model is not a claim that all regulators behave opportunistically. It is a
mechanism-design and contingent-claim model of a particular conflict: when the regulator’s fu-
ture labor-market payoff is convex in the regulated firm’s value, regulatory discretion can create
incentives to favor signals that raise firm value, leverage, and option-like compensation.
The players are a regulator, a regulated firm, and the public. The regulator chooses a regu-
latory signalθor, more generally, a state-dependent signals(ω, θ) that affects the firm’s admissible
strategy space. The firm observes or infers the signal and chooses pricing, leverage, or investment
actions from the induced strategy set. The public receives consumer surplus and bears part of
the cost of distorted regulation. The regulator maximizes a value function that includes consumer
surplus, firm profit, and the private value of a career option to quit and join the regulated firm.
The firm maximizes profit subject to the strategic environment induced by the regulator’s signal.
The model therefore has two connected incentive problems: the public-sector welfare problem and
the regulator’s private option-value problem.
The central object is the regulator’s implicit career option. If the regulator can leave public
office and receive an equity-linked payoff from the regulated firm, then the payoff resembles a call
option with value (αV−K) +, whereVis firm value,Kis the regulator’s current compensation or
outside strike value, and 0< α <1 is the share of firm value embedded in the future compensa-
tion package. Regulatory signals matter because they affectV, leverageD/V, and signal-induced
volatilityσ(s(θ)). A signal that raises firm value or volatility can therefore increase the value and
vega of the regulator’s career option even when it also raises firm tail risk.
The paper delivers three theoretical claims. First, regulatory signals embedded in firm
capital structure can divide the firm’s strategy space into consumer-surplus and firm-profit regimes.
Second, the regulator’s career option is increasing in firm value and is more valuable for levered firms
when the regulator’s future payoff is tied to equity-like compensation. Third, under an information-
based option-pricing interpretation, signal-induced volatility raises the vega of the option on firm
value and can generate a leverage-vega warning region in which firm value-at-risk is higher than it
would be without regulatory capture.
The calibration does not estimate a causal effect or assert that a particular industry episode
followed the model. It illustrates how the model’s primitives generate the qualitative regions im-
plied by the propositions: a go-leverage region, an early-warning region, and a crash or bankruptcy
region. The extended exercises then show how those regions respond to maturity, leverage, compen-
sation convexity, bank-like parameter anchors, stochastic signal realizations, and quitting-horizon
choices. This structure also provides a diagnostic language for prominent financial failures in which
delayed, missing, or distorted regulatory signals allowed leverage, duration risk, uninsured-deposit
dependence, or other tail exposures to accumulate before binding intervention occurred.
The paper relates first to classic theories of revolving doors and regulatory capture (Che,
1995; Salant, 1995; Stigler, 1971). Recent work has sharpened this literature by distinguishing
several mechanisms. De Chiara and Schwarz (2021) develop a dynamic theory in which a fu-
ture private-sector job can dominate hidden transfers as a capture device because the revolving
door publicly signals the firm’s willingness to reward lenient regulators. Kempf (2020) shows that
revolving-door incentives can also operate through reputational and accuracy incentives in credit-
rating labor markets, which is an important counterweight to one-sided capture interpretations.
Katic and Kim (2024) show that regulator-to-firm mobility can improve regulatory outcomes for
firms, but that the advantage is concentrated just before the mobility event. Emery and Faccio
1

(2025) map executive-branch revolving-door appointments into corporate positions and show that
firms are more likely to receive procurement contracts after appointing recent former regulators,
while some contracts become more costly through renegotiation. Yates and Cardin-Trudeau (2021)
emphasize “lobbying from within” and entry-side cultural capture, while Heims and Moxon (2024)
argue that capture claims require evidence on the mechanism by which private influence changes
regulatory decisions. These recent papers motivate the present model’s focus on the timing and
mechanism of the regulator’s private payoff rather than on a blanket assertion of capture.
The paper also connects to regulation and capital structure (Spiegel and Spulber, 1994; Bor-
tolotti et al., 2011), political connections and financial firms (Braun and Raddatz, 2010; Lucca et al.,
2014; Lambert, 2017), and option-based interpretations of firm equity and compensation (Merton,
1974; Hull, 2006). Recent financial-regulation evidence is especially close to the paper’s mecha-
nism. Hirtle and Kovner (2022) review the supervisory literature and emphasize that supervision
uses soft information to discipline bank risk-taking. Kim et al. (2018) show that leveraged-lending
guidance affected closely supervised banks but also shifted risk toward nonbanks, illustrating why
an apparently binding regulatory signal can move risk rather than eliminate it. Colonnello et al.
(2023) study reverse revolving doors in European bank supervision and report that former financial-
industry executives on supervisory boards are associated with positive bank valuation effects, lower
regulatory capital, and faster bank growth before the Single Supervisory Mechanism. Haselmann
et al. (2018) show how elite social networks can distort bank credit allocation, reinforcing the pa-
per’s emphasis on network-mediated regulatory and financing advantages. Berchtold et al. (2026)
find that politically experienced directors reduce the sensitivity of corporate investment to policy
uncertainty, especially for irreversible investment, which supports the model’s claim that political
and regulatory human capital can change firm policy under uncertainty. Schram and Ule (2024)
show experimentally that regulatory independence can reduce electoral holdup but can also en-
trench capture when policymakers’ objectives align with regulated owners. The contribution here
is to connect these strands in a compact mechanism: a regulator’s policy signal changes firm strat-
egy and capital structure, while the regulator’s future labor-market payoff has the convexity of an
option on the regulated firm.
Direct empirical evidence on federal employees supports the model’s career-option primitive.
Kalmenovitz et al. (2025) use payroll records on 22 million federal employees and the salary thresh-
old that triggers post-employment restrictions under 18 U.S.C.§207 to show significant bunching
just below the restriction cutoff. In agencies with broad regulatory powers, limited political super-
vision, and frequent interaction with high-paying industries, they estimate that 49% of regulators
respond to revolving-door incentives and sacrifice 7.4% of wage potential to preserve private-sector
opportunities. They also find that revolving regulators initiate fewer enforcement actions and issue
rules with lower compliance costs. In the language of the present model, their evidence verifies
the maintained economic object: the outside job opportunity is valuable before exit, regulators
trade current public compensation against future private-sector option value, and the incentive is
associated with softer regulatory signals.
The rest of the paper proceeds as follows. In Section 2 we introduce the model and derive
the regulator’s career-option mechanism. In Section 3 we provide a proof-of-concept calibration of
leverage, vega, and warning regions. In Section 4 we conclude. The appendix states the abstract
legislative mechanism that supports the regulator’s signalling problem.
2

2 The Model
The model has three primitive objects: a regulator typeθ∈Θ, a state of natureω∈Ω, and
a regulatory signals(ω, θ) that maps the regulator’s information and type into a strategy space
Gfor the firm. The firm responds to the induced strategy space by choosing prices, leverage, or
investment policies. The regulator values public welfare, but also holds an implicit career option
C:G→Xwhose payoff is increasing in the regulated firm’s value. Thus regulatory signals affect
both the firm’s strategy set and the regulator’s private option value. The propositions below first
formalize the abstract career option, then show how welfare tradeoffs, leverage, option value, and
vega interact.
Regulator
typeθ
Policy signal
s(ω, θ)
Firm strategy set
G(s)
Firm choices
p, D, V, σ
Public payoff
CS(p)
Firm profit
Π(p, V, D)
Career option
C(s) = (αV−K) +
Signal-induced capital-structure channel
Figure 1: Mechanism sketch: regulatory signal, firm response, and career-option feedback
Notes:The regulator’s signal changes the firm’s feasible strategy set. Firm choices affect consumer
surplus, firm profit, firm value, leverage, and volatility. Because the regulator’s outside payoff is convex
in firm value, the career option feeds back into the regulator’s signal incentives.
Proposition 2.1(Regulator’s abstract career option on regulated firms).LetΩbe a sample space
for states of nature,Θbe a type space for regulators,Ga strategy space, andM= (G, C)be an
abstract legislation mechanism in Definition A.1, andsbe a regulatory signalling function such that
s: Ω×Θ→G. Letfsignify the regulator’s unobservable choice function. So thatf: Ω×Θ→X
is a stochastic choice function mapped into outcome space. Specifically, letC:G− →Xbe the
regulator’s career [call] option on regulated firms. We claim that the abstract value of the option is
given by the legislative mechanism:
f(ω, θ)∼= (C◦s)(ω, θ)
where ∼= represents an isomorphism.
Proof.See Section A.
Remark2.1.Technically, the legislative mechanism is supposed to induce the firm to engage in
some action for the regulator’s benefit. As we will see in the sequel, that “something“ is profit
maximization or leverage. Section 2.1 illustrates application of elements of this abstract proposition,
□
2.1 Welfare effects of embedding regulator signals in capital structure
Without loss of generality, for the purpose of exposition, in this subsection our analysis is based
on deterministic parameterizations. Furthermore, we assume that the form is monopolistically
competitive so it can execute a pricing strategy. Here, the regulator wants to maximize her social
welfare function, i.e. value function, comprised of consumer surplus (CS) and the firm profits (Π)
3

[s]he affects by embedding regulatory signalsθin the firm’s capital structure. That is, through
choices and regulatory decisions the regulator attempts to affect firm equity values. Our motivation
for the welfare function is based on Spiegel and Spulber (1994, pg. 427), who state:
[T]he regulator establishes the regulated price by maximizing a welfare function, taking
the firm’s investment and capital structure as given. The balancing of consumers’ and
investors’ interests is made explicit by assuming that the welfare function is a weighted
sum of consumers’ surplus and firm profits. Then, the regulated firm produces its
output and the regulated market clears. The focus of this article is on characterizing
the subgame equilibrium of the regulatory game.
See also Baron and Myerson (1982, pg. 916). However, in our model capital structure is embedded
with regulatory signals and our equilibrium is based on a reversed game theory, i.e. mechanism
design approach.1 This is a source of “market friction” consistent with the tradeoff hypothesis of
capital structure theory, i.e., “tradeoff theory looks at how businesses balance the pros and cons
of different forms of financing” (Kwan, 2009). We show below, that that is indeed the case. For
example, as regulators tradeoff welfare for firm profit, the price strategy space is affected. However,
the latter is tied to the firms activity ratio (e.g., sales/(total assets)) which is a key predictor of
bankruptcy (e.g., Altman, 1984) in tradeoff theory otherwise known as the static theory of capital
structure which examines tradeoff between corporate tax shields and expected bankruptcy costs of
leverage.
Consistent with Spiegel and Spulber (1994, pg. 429, equation (6)), we identify the following
primitives used to construct our criterion function.
Primitives
p≜price of firm output
k≜firm capital investment
D≜nominal amount of debt owed to bondholders
E≜market value of the firm equity
ρ≜debt/distress penalty weight in the regulator value function
Unlike Spiegel and Spulber (1994, pg. 428), who letEbe the market value of new equity, andBbe
the market value of bonds, we let the firm’s capitalkbe its valueV(θ) which is a combination of
debtD(θ), and market value of equityE(θ). In that way, the market value of equity is transmitted
through firm value for a given amount of debt. Assuming no transfers or taxes, Spiegel and Spulber
(1994, pg. 429, equation (6)) posit a “utilitarian welfare function” which we modify to construe as
our regulator value function written as
W(p, V(θ), D(θ)) =CS(p) +bΠ(p, V(θ), D(θ))−ρD(θ) (2.1)
V(θ) =D(θ) +E(θ) (2.2)
whereCS(p) is consumer surplus; 0< b <1 is a welfare weight; Π(p, V(θ), D(θ)) is firm profits;
andρ >0 is the regulator’s penalty weight on debt or expected distress exposure.
Assumption 2.2.A.1 Debt is signal dependent,D θ ≥0. In the high-leverage region,L(θ) =
D(θ)/V(θ)satisfiesL θ >0, equivalentlyD θ/D > Vθ/V.
1We thank Gary Dymski for motivating clarification of this point.
4

A.2 Regulator signals favor firm capital and profits through the firm-value and leverage channels,
i.e.Π V >0,V θ >0, andbΠ V Vθ + (bΠD −ρ)D θ >0over the relevant region. This includes
the case in which debt or distress is weakly penalized, so that leverage-taking is not fully
internalized.
A.3 Consumer surplus decreases in price,CS p <0.
□
Figure 2: Impact of regulator signalθon price (p) and firm profits Π
Consumer

Price strategy space

Profits
Quantity
0
dp
dq >  0
dp
dq <
Price (p)
0p ¶P ¶ =
ˆp
 regulator signalq
  regulato
0
Firm
In regulator induced price strategy spaceG low ={0< p≤ˆp}the rate of price changep θ
relative to regulator signalθis decreasing. ForG high ={ˆp < p≤p∗}the rate of price change
is increasing (and consumer surplus is falling), and firm profits are ultimately maximized at
p∗. An admissible [price] strategy space for consumer welfare firm profit tradeoffs is the
supportG=G low ∪G high.
Under Theorem 2.2, the regulator signal is channeled through firm value and debt. The effective
total differential of (2.1) is given by
d(W(p, V(θ), D(θ))) =CSp dp+b{Π p dp+ Π V Vθ dθ+ Π DDθ dθ} −ρDθ dθ.(2.3)
Equate the left hand side to 0, and let subscripts denote partial derivatives. Then
(CS p +bΠ p)dp+{bΠ V Vθ + (bΠD −ρ)D θ}dθ= 0,
dp
dθ =p θ = bΠV Vθ + (bΠD −ρ)D θ |CS p| −bΠp .(2.4)
5

The term (bΠ D −ρ)D θ is the incremental debt channel. If debt or distress is weakly penalized
relative to its private profit contribution, this term amplifies the price-signal response. Ifρis large,
it dampens or can reverse the response.
The price-signal ratio induced by regulator signalθin (2.4), informs the firm about ad-
missible pricing strategies, leverage, and profits depicted in Figure 2. There, in the price range
Glow ={0< p≤ˆp}the rate of price changep θ relative toθis decreasing. This implies that
consumer surplus is increasing. However, firm profits are not being maximized. In the range
Ghigh ={ˆp < p≤p∗}the rate of price change is increasing (and consumer surplus is falling), and
firm profits are ultimately maximized atp ∗. At which point the darker shaded region is the loss
in consumer surplusCS(p) or consumer welfare sacrificed for firm profits. Thus, regulator signals
allow the firm to adopt a pricing strategy in either one of the price ranges according to whether the
regulator’s focus is on maximizing consumer welfare at the expense of firm profits or vice versa. 2
In other words, an admissible [price] strategy space is the supportG=G low ∪G high.
The same signal also has a capital-structure implication. SinceL(θ) =D(θ)/V(θ),
Lθ = DθV(θ)−D(θ)V θ V(θ) 2 .(2.5)
Thus leverage rises when debt grows faster than firm value,D θ/D > Vθ/V. This is the relevant
revolving-door mechanism: if debt-taking is not heavily penalized in the regulator value func-
tion, the firm can move toward a highly levered region. Higher leverage can increase the convex
value of equity-linked career compensation, but it also reduces the distance-to-default component
log(V(θ)/D(θ)) in the option and default calculations below.
Since the value of the regulator’s career option is tied to firm profit, we should expect
regulators who plan to exercise that option to send signals that support pricing in the range
Ghigh. The revolving-door literature provides examples consistent with this mechanism. Dal B´ o
(2006, pp. 217-218) report that former FCC commissioners who take industry employment “increase
their support for industry interest by nearly 11 percent during their last year in office”. In that
case, consumer welfare is sacrificed for regulator career goals. See, e.g., Kane (2011, pg. 8), who
summarizes a related issue thus: “The importance of political, bureaucratic, andcareer interests
in regulatory decision- makingallows such firms to screen regulatory appointments and to distort
regulatory policiesex anteand to reshape their enforcementex post” (emphasis added). We
summarize these results in
Proposition 2.3(Regulator’s career goal and tradeoff between consumer welfare and firm profit).
Assume that there are no transfer payments. Letθbe a regulator signal, andW(p, V(θ), D(θ)) =
CS(p) +bΠ(p, V(θ), D(θ))−ρD(θ)be the regulator’s value function, wherepis the price of the
firm’s product,CS(p)is consumer surplus,Πis a profit function as indicated,V(θ)is firm value
with embedded regulator signal,D(θ)is debt, andρ >0is the debt/distress penalty weight. If The-
orem 2.2 holds, then regulator signals induce dichotomous decreasing and increasing price regimes
in strategy spaceG={G low ∪G high}, whereG low ={(0,ˆp]}andG high ={(ˆp, p∗]}. Moreover,
regulators will trade consumer welfare for firm profits in increasing price regimesG high in order to
enhance the value of their career optionC:G− →Xto quit and join firm management.□
In the proof-of-concept exercise below, the high-price region is interpreted abstractly as a firm-
profit region.
2Zimper and Hassan (2012) introduced a model in which regulators learn about firms’ price collusion strategies
through dynamic price dividend ratios.
6

2.2 Stock options with regulatory signalling
In this section, we apply Theorem 2.1 in the context of what we now know about the firms capital
structure embedded with regulator signals. Where possible we suppress theωnotation since it is
acknowledged by the probability distributions in the formulae that follow. We retain Theorem 2.2
as it pertains to signal-dependent firm value and debt. With few exceptions, the assumptions below
are consistent with Merton (1974, pg. 450).
We note in passing that regulator signals are a source of market friction that affects capital
structure. Since the firm responds to the signal(s) it receives from the regulator, letV(s(θ)) be the
value of the firm. The notation here is slightly more general than (2.2). Suppose that the regulator’s
potential “managerial compensation” with the firm would be the equity stakeαV,0< α <1, upon
a career change. IfK∈Xis the “value” of the regulators compensation package in her current
position as regulator, then [s]he may want to exercise a career [call] option at timet. The abstract
topological lifting in Figure 9 in Section A shows that (suppressingω) the choice function at time
treduces to
f(t;θ) = (αV(t, s(θ))−K,0) + (2.6)
More formally, that abstract [call] option compensation scheme takes the form
C(t;s(θ ∗)) = max
θ
(αV(t;s(θ))−K,0) + (2.7)
or in the alternative
C(τ ∗;s(θ)) = sup
τ∈T,θ∈Θ
(αV(τ, s(θ))−K,0) + (2.8)
where,θ ∗ is the type of regulator who maximizes her option,τ∈ Tis a stopping time andτ ∗ is the
optimal stopping time in the setTof all possible quitting times for the regulator. The foregoing is
summarized in the following
Lemma 2.4(Regulator’s career call option).The regulator’s career call optionC(t, s(θ))increases
when embedded regulatory signals increases firm valueV(t, s(θ))and it is evaluated asC(τ ∗;s(θ ∗)) =
supτ∈T maxθ∈Θ(αV(τ, s(θ))−K,0) +.
Of courseV(t, s(θ)|Ft) is the value of the firm at timetgiven the “filtration” of informationF t, and
it has to be discounted from some “terminal date”T. To keep it simple, assume that the option is
a European type 3 so that it will be exercised at a “known” terminal date, and that the strike price
isK. The regulator exercises a call option based on her type with the premium as indicated. It
should be noted in passing that on the other side of the regulator’s call option contract is a third
party guarantor who holds an offsetting put contract. Namely, the regulating agency or taxpayers.
See, e.g., Merton (1977). Since firm value is reflected by the price of the firms stocks, the regulator’s
action is functionally equivalent to a stock option. 4 In this case, the stock price reflects the signals
from the regulator. More on point, from (2.2) we find (suppressingt) that the firm’s equity is given
by:
E(s(θ)) =V(s(θ))−D(s(θ)) (2.9)
3For the purpose of this paper, the added complexity of American style option pricing may cause us to loose sight
of the forest for the trees. See, e.g., Myneni (1992) for a taxonomy of American option pricing.
4See Hall and Murphy (2000).
7

So the regulator’s virtual call option is based on
αE(s(θ)) + = max{αV(s(θ))−αD(s(θ)),0}(2.10)
This implies that the strike price in (2.7) based on the value of the regulator’s pre-industry compen-
sation package, must be compared to the firm’s debt before [s]he exercises her option. Specifically,
we must consider whether
K−αD(s(θ))≶0 (2.11)
This implies that we also need a model of dynamic stock prices with information signalling. That
issue is addressed in the sequel.
2.3 Valuation of regulator career option and capital structure of the firm
Consistent with (2.10), Merton (1974, pp. 453-454) showed that the option value of the equity in a
firm with valueVand debtDis given by
f(V, τ) =VΦ(x 1)−Dexp(−rτ)Φ(x 2) (2.12a)
x1 = log V D + (r+ σ2 2 )τ σ√τ (2.12b)
x2 =x 1 −σ √τ(2.12c)
wheref(V, τ) is option value of firm equity,ris a risk free rate,τ=T−tfor exercise dateTfor
a European call option priced at timet; and Φ is the cumulative normal. From the outset we note
that
αf(V, τ) =αVΦ(x 1)−αDexp(−rτ)Φ(x 2) (2.13)
The right hand side of that equation is isomorphic to a call option
C(·) = (αV−αD,0) + (2.14)
So the regulator’s valuation rests on comparing his current compensation packageKto the psuedo-
strike priceαDthat depends on the firm’s debt. That is, the exercise of her career option rests on
the evaluation
(αV−K,0) + ≷(αV−αD,0) + (2.15)
Here, we assume that the regulator knowsV, Kandαbut she does not know whatDwill be on
the strike date. Thus, in (2.11) if the regulator believes thatK < αDso that (αV−K,0) + >
(αV−αD,0) +, then her valuation of the firm is greater than its actual value. Arguably, at this stage
the regulator would be interested in legislation that induces the firm to report its debt truthfully.
So she would be inclined to exercise her career option to quit and join the firm or she would stay
otherwise. What is more, the regulator now has incentive to design a legislative mechanism that
increases firm leverage. So she looks more favorably at levered firms because a highly levered firm
increases the value of her career option. This prediction is consistent with the theoretical possibility
that privately controlled firms use leverage strategically to obtain better regulatory outcomes. See,
e.g., Bortolotti et al. (2011). Therefore, in the sequel we assume thatK < αD.
8

2.3.1 Regulator career option pricing with signalling
Becauseθis unobservable, its presence in firm value, i.e. stock price, implies that it may follow a
hidden Markov process. To account for this possibility, we turn to the information-based stock price
model of Guo (2001) and Shepp (2002) on the canonical probability measure space (Ω,F,F, P) with
filtration F. In the context of our model, the Shepp-Guo model is parameterized as
dV(t, ω)
V(t, ω) =µ(s(t, θ))dt+σ(s(t, θ))dW(t, ω) (2.16)
where the regulatory signals(t, θ) is a hidden Markov process. To simplify matters we assume that
s(t, θ) =s(θ). That is, the signal is not time dependent. In that case, the problem is reduced to
one of an American style option where the regulator embeds a deterministic signal in the value of
the firm, and she can exercise her option to join the hitherto regulated firm at any time. Thus,
firm value dynamics in (2.16) is given by
dV(t, ω)
V(t, ω) =µ(s(θ))dt+σ(s(θ))dW(t, ω) (2.17)
More on point, Shepp (2002, pg. 1373) and Guo (2001) introduce evidence that information asym-
metry is dispositive of volatility dynamics, and the activity of insiders leads to increased volatility.
In which case we assume that regulator signals increases volatility of firm value. That is
Assumption 2.5.σ(s(θ))> σ□
This assumption is consistent with Boyle et al. (2011), who find that high volatility firms should
use more stock options to compensate their executives. Furthermore, Cadogan and Cole (2014)
show how former regulators embed signals in capital structure and use index option compensation
contracts to increase compensation. Thus, using the formulae in (2.12), we find that
f(V(s(θ)), τ) =V(s(θ))Φ(x 1(s(θ)))−D(s(θ)) exp(−rτ)Φ(x 2(s(θ))) (2.18a)
x1(s(θ)) =
log V(s(θ)) D(s(θ)) + (r+ σ(s(θ))2 2 )τ
σ(s(θ))√τ (2.18b)
x2(s(θ)) =x 1(s(θ))−σ(s(θ)) √τ(2.18c)
Thus we must compare the value of the option on the firm with embedded regulator signal to the
value without signal. To do that we turn to option Greeks by examining the vega (ϑ) of the option
on the firm. 5 That is, for the mean zero normal distribution functionϕ, let
ϑ(0) = ∂f(V, τ) ∂σ =V ϕ(x1)√τ(2.19)
ϑ(s(θ)) = ∂f(V(s(θ)), τ) ∂σ(s(θ)) =V(s(θ))ϕ(x 1(s(θ)))√τ(2.20)
According to Theorem 2.5 information based vega is larger than plain vanilla vega. 6 Thus,
ϑ(s(θ))> ϑ(0)⇒V(s(θ))ϕ(x 1(s(θ)))√τ > V ϕ(x1)√τ(2.21)
⇒ V(s(θ)) V > ϕ(x1) ϕ(x1(s(θ))) (2.22)
5See Hull (2006, pg. 361) for derivation of formula for vega.
6Chesney et al. (2012) also introduced the concept of “asset volatility vega” which is higher than plain vanilla
“equity volatility vega”.
9

Under Theorem 2.4 a more levered firm with embedded regulator signals enhances regulator career
option so we expectV(s(θ))> V. Thus, we have
V(s(θ))
V >max

1, ϕ(x1) ϕ(x1(s(θ)))  (2.23)
The right hand side of the equation above is satisfied if
ϕ(x1)
ϕ(x1(s(θ))) >1⇒exp

−

x2 1
2 − x1(s(θ))2 2 !! >1 (2.24)
⇒ −x1(s(θ))<−x 1 andx 1(s(θ))> x1 (2.25)
Following the distance-to-default interpretation of option-based credit models,−x 1 is an inverse
distance-to-default index. The analysis below provides a theoretical explanation for why regulator-
induced volatility can lower that distance and raise tail-risk exposure.
2.3.2 Bankruptcy warning signals: Firm vega and leverage
At this juncture we assume the static theory of capital structure (with perpetual debt) (Jordan
et al., 2017, pp. 437-439), stated as a lemma below, in order to motivate the internal consistency
of our probability of firm bankruptcy.
Lemma 2.6(Tradeoff theory of capital structure).LetV L be the value of the levered firm, andV U
its unlevered value;T c be corporate tax andDbe the firm’s debt,r D be the interest rate on debt,
bp(θ)be the probability of bankruptcy with regulator signalθ, andCbe the cost of firm distress, thus
VL(θ) =V U +T cD−r −1 D bp(θ)×C.
Figure 3 is a typical sketch of a levered firm’s value when faced with a tax shield and expected
cost of firm distress under the static theory of capital structure with perpetual debt. Firm value is
increasing in regulator signal, i.e.,∂V L/∂θ >0, prior to the optimal capital structureD ⋆/E⋆, and
decreases thereafter. This implies that∂b p(θ)<0 when firm value is increasing and∂b p(θ)/∂θ >0
when firm value is decreasing. So regulator induced probability of bankruptcy is countercyclical.
The analysis that follows is based on Cadogan and Cole (2014). The foregoing arguments show
that the information based vega for the option value of the firm is dispositive of regulator incentive
to leverage regulated firms. See also Armstrong and Vashishtha (2012). According to Kolmogorov
Inequality, see, e.g., Athreya and Lahiri (2006, Thm. 8.3.1, pg. 249), under Theorem 2.5, ifφis the
lower tail fraction of total tail probability, then for some threshold valueλ, and assuming maximal
probability thresholds, we have the nonparametric result
bp(θ) = Pr

max
θ
{x1(s(θ))}<−λ

=φ Var(x1(s(θ))) λ2 (2.26)
=φ ˜σ2 x1(θ) λ2 > φVar(x1) λ2 =φ ˜σ2 x1 λ2 (2.27)
where ˜σ2 x1(θ) and ˜σ2 x1 are the variances ofx 1(s(θ)) andx 1 respectively. The result in (2.27) is
important because it says that the “large deviation probability” for firm value at risk included in
x1(ωb, s(θ)), i.e. tail risk in bad statesω b ∈Ω, is greater than the corresponding probability if
there was no regulatory signals or “regulatory capture“ embedded in capital structure. To see this
10

Figure 3: Optimal Capital Structure Under Static Theory with Perpetual Debt

0

Firm Value (V)
Optimal Capital Structure under
Static Theory with Perpetual Debt
rewriteV(s(θ)) in (2.18) asV(θ) so that after algebraic reduction we have
lim
σ(θ)→∞
Pr
n
max
θ
V(θ)<max
θ
D(θ) exp

−λσ(θ)√τ−  r+ σ2(θ) 2  τ o > φ˜σ2 x1 λ2 (2.28)
⇒Pr{max
θ
V(θ)<0}> φ 1 λ2σ2τ Var  ln V D  ,|λ|<


Var

ln V D

σ2τ


1
2
(2.29)
where ˜σ2 x1 = 1 σ2τ Var(ln V D ). The denominator isσ 2τ, notD 2τ, becausex 1 normalizes the log-
leverage term byσ √τ. The relationship in (2.29) is equivalent to a bankruptcy condition involving
leverage D V . It says that if regulator signalsθinduce too much volatility, i.e. uncertainty, in firm
valueV(θ), then the probability that the value of the firm is negative, i.e. it goes bankrupt when
V(θ)<0, is greater than a given threshold without regulator signals. Thus we have proven the
following
Proposition 2.7(Bankruptcy condition).Assume that regulatory capture exists so that regulators
embed regulatory signalsθin firm capital structure. Then firm distance to defaultx 1(ωb, θ)in bad
states of nature is greater thanx 1(ωb)–the value it would be in non-regulatory capture regimes–and
the probability of bankruptcy is higher than it would be in the absence of regulator signals.□
Remark2.2.This proposition should not be interpreted to mean that in a world with no regulation,
11

firm value-at-risk will be lower than if there is regulation. The proposition is based on an assumption
of “regulatory capture“. The absence of regulatory capture though necessary, is not a sufficient
condition to support deregulation.□
The leverage-vega diagram in Figure 4 is a schematic implication of the model rather than a
data plot. We assume that the vega for equity-linked compensation is tied to firm performance and
that it is rolled over the life of the firm. The relationship between vega and firm leverageL= D V
is implied by (2.19) and (2.20). Thus, critical time points occur whereϑ(L(t|σ(θ))) =L(t|σ(θ))
in vega-leverage space. Vega attains a maximum for some value ofL. The roots of the equations
in (2.19) and (2.20) can be obtained by superimposing a plot ofϑandLon the same schematic
diagram. Figure 4 provides a proof-of-concept sketch of that procedure for a root att ⋆.
The sketch suggests that the rate of increase in firm leverage dL dt , and the rate of increase of
firm vega dϑ dt conditioned on regulator signal dependent riskσ(θ), may be dispositive of bankruptcy
as well. It shows that the rate of diminishing returns to vega begins just after maximum vega
ϑmax, att ∗, even though the rate of firm leverage is increasing. However, beyond some critical
point (L c, ϑc) (a root of say (2.20)) the firm is so highly levered that it goes bankrupt. So the
period (t ∗, tc] is a time when warning signals of possible bankruptcy takes place. These artifacts of
vega and leverage are summarized thus:
Proposition 2.8(Menu of firm response to leverage induced regulator signals).Let(L(t|σ(θ))
andϑ(L(t|σ(θ)))be time dependent firm leverage and vega respectively for a given risk profileσ(θ)
induced by regulator signalθ. Critical time points are given by the solution toϑ(L(t|σ(θ))) =
L(t|σ(θ)), and induce the following menu of firm response to leverage and regulator signal:
A1 Go leverage window: dϑ dt > dL dt andL < ϑ
A2 Early warning window: dϑ dt < dL dt andL < ϑ
A3 Crash or bankruptcy window: dϑ dt < dL dt andL > ϑ
3 Proof-of-Concept Calibration
This section provides a proof-of-concept calibration. The purpose is not to estimate the model
or to fit an observed sample. The purpose is to show how the theoretical objects in Theorems 2.3,
2.4, 2.7 and 2.8 can be evaluated in a simple numerical environment.
Normalize initial firm value toV 0 = 1, set the regulator’s equity-linked share toα= 0.05,
and let the regulator’s current compensation strike beK= 0.030. Let a regulatory signalθ≥0
affect firm value, debt, and volatility through
V(θ) =V 0{1 + 0.08θ},(3.1)
D(θ) =D 0{1 + 0.15θ},(3.2)
σ(θ) =σ 0{1 + 0.30θ},(3.3)
whereD 0 = 0.55 andσ 0 = 0.20. This calibration intentionally imposesD θ/D > Vθ/V: debt grows
at rate 0.15/(1 + 0.15θ) while firm value grows at rate 0.08/(1 + 0.08θ) over the grid. Hence the
proof of concept is in the weak-penalty leverage channel of Theorem 2.2. The parameterρis not
separately calibrated in the option-value exercise; it is maintained as small enough that the net
termbΠ V Vθ + (bΠD −ρ)D θ remains positive. The regulator’s career option payoff is
C(θ) =

αV(θ)−K
+.(3.4)
12

Figure 4: Firm vega (ϑ) and leverageLfor given
risk signalσ(θ) with early warning and
bankruptcy windows
Firm leverage

Firm vega

Early warning
window

time
Go leverage window

Crash of bankruptcy
window

Lc, ϑc are the critical points for firm leverage and vega. Beyond that the firm’s stock price
crashes or it goes bankrupt. Att ⋆ vega is at a maximum. In time period (0, t ⋆] leverage is
encouraged. In period (t ⋆, tc] leverage should proceed with caution. At timet > t c the firm is at
risk for bankruptcy.
The leverage ratio isL(θ) =D(θ)/V(θ), and the signal-adjusted Black–Scholes–Merton vega proxy
is
ϑ(θ) =V(θ)ϕ(x 1(θ))√τ , x 1(θ) = log(V(θ)/D(θ)) + (r+σ(θ) 2/2)τ σ(θ)√τ ,(3.5)
withr= 0.03 andτ= 1. These values are illustrative and are chosen only to display the comparative
statics of the model.
The proof-of-concept classification follows Theorem 2.8. A signal is in the go-leverage region
whendϑ/dθ > dL/dθandL < ϑ. It is in the early-warning region whendϑ/dθ < dL/dθandL < ϑ.
It is in the crash region whendϑ/dθ < dL/dθandL > ϑ. In a discrete grid, the derivatives can be
approximated by first differences. Thus the model can be implemented by evaluating the following
table of theoretical objects.
13

0.0 0.5 1.0 1.5 2.0
0.0
0.1
0.2
0.3
0.4
0.5
0.6
Proof−of−concept leverage, vega, and career−option payoff
Regulatory signal θ
Scaled model quantity
Leverage ratio
Scaled vega proxy
Career−option payoff
Go Warning
Crash−risk
(a) Signal path
alpha
0.02
0.04
0.06
0.08
0.10
theta
0.0
0.5
1.0
1.5
2.0
C
0.00
0.02
0.04
0.06
Career−option payoff surface (b) Career-option surface
Figure 5: Proof-of-concept calibration diagnostics
Notes:Panel (a) plots leverage, the scaled vega proxy, and the regulator’s career-option payoff along the
signal path. Panel (b) plots the career-option payoff over the regulatory signalθand the equity-linked
compensation shareα. The plots are illustrative diagnostics for the model, not estimates.
Table 1: Proof-of-concept leverage-vega classification
SignalV(θ)D(θ)L(θ)C(θ) Region
θ= 0.0 1.000 0.550 0.550 0.020 Baseline
θ= 0.5 1.040 0.591 0.568 0.022 Go leverage
θ= 1.0 1.080 0.633 0.586 0.024 Go leverage
θ= 1.5 1.120 0.674 0.602 0.026 Early warning
θ= 2.0 1.160 0.715 0.616 0.028 Crash-risk window
Notes:The numbers are an illustrative calibration, not estimates. The region labels summarize the
qualitative inequalities in Theorem 2.8. The example shows how a regulator-induced signal can raise both
the value of the regulator’s career option and the firm’s leverage-risk exposure.
The table illustrates the mechanism. Asθrises, firm value increases, but debt and volatility
increase more aggressively. The regulator’s option value rises because the payoff is convex in firm
value. At the same time, leverage rises and the vega-leverage relation moves toward the warning
region. The proof-of-concept shows the theoretical mechanism: signals can move a firm across
leverage-vega regions, while applied work would be needed to determine whether a particular firm
or industry followed that path.
The preceding calibration uses a linear signal path. To show how nonlinear signals change
the mechanism, consider a quadratic signal map
sq(θ) =θ+γθ 2, γ= 0.40,(3.6)
and let firm value, debt, and volatility depend ons q(θ) rather than directly onθ:
Vq(θ) =V 0{1 + 0.08sq(θ)},(3.7)
Dq(θ) =D 0{1 + 0.15sq(θ)},(3.8)
σq(θ) =σ 0{1 + 0.30sq(θ)}.(3.9)
The marginal signal effect is now state dependent,s ′ q(θ) = 1 + 2γθ. Thus the option-value and
leverage channels accelerate at high signal intensities. Economically, this means that a modest
14

signal may have a small effect nearθ= 0, while a stronger signal can move the firm rapidly into
the early-warning or crash-risk region.
The quadratic signal is not a Bayesian information signal. It is a reduced-form nonlinear
signal-response map, similar in spirit to threshold and smooth-transition specifications used to
capture nonlinear policy and state responses in applied dynamics (Hansen, 1999; Terasvirta, 1994;
van Dijk et al., 2002; Hamilton, 2016). A Bayesian reputation-learning version, in which firms
update beliefs about a regulator’s type from repeated signals, is conceptually natural but would
require a separate belief-state law of motion and equilibrium learning problem. We therefore leave
that extension outside the present proof-of-concept calibration.
0.0 0.5 1.0 1.5 2.0
0.0 1.0 2.0 3.0
Signal map
θ
Effective signal
Linear: s(θ) = θ
Quadratic: sq(θ) = θ + 0.4θ2
0.0 0.5 1.0 1.5 2.0
0.2 0.3 0.4 0.5 0.6
Proof−of−concept response
θ
Leverage / scaled option payoff
Linear leverage
Quadratic leverage
10 x linear option
10 x quadratic option
Figure 6: Linear and quadratic proof-of-concept signal paths
Notes:The left panel compares the linear signals(θ) =θwith the quadratic signals q(θ) =θ+ 0.40θ 2.
The right panel compares leverage and the scaled career-option payoff under the two signal maps. The
quadratic signal amplifies both leverage and private option value at highθ.
Table 2: Quadratic-signal proof-of-concept classification
Signals q(θ)V q(θ)D q(θ)L q(θ)C q(θ) Region
θ= 0.0 0.000 1.000 0.550 0.550 0.020 Baseline
θ= 0.5 0.600 1.048 0.600 0.572 0.022 Go leverage
θ= 1.0 1.400 1.112 0.666 0.598 0.026 Early warning
θ= 1.5 2.400 1.192 0.748 0.628 0.030 Crash-risk window
θ= 2.0 3.600 1.288 0.847 0.658 0.034 Crash-risk window
Notes:The nonlinear signal uses the same primitive parameters as Table 1, but replacesθbys q(θ) =
θ+ 0.40θ 2. Relative to the linear calibration, the quadratic signal accelerates the movement into warning
and crash-risk regions because debt, volatility, and career-option value rise more quickly at high signal
intensity.
3.1 Robustness and quantitative comparative statics
The preceding tables use one normalized path. To make the proof-of-concept less depen-
dent on a single deterministic calibration, this subsection reports five additional numerical checks.
These checks are still illustrative rather than estimated. They show how the warning regions move
15

with time-to-maturity, leverage, compensation convexity, stochastic signal realizations, and quitting
horizons.
First, because the vega expression in (2.20) depends explicitly onτ, the calibration is
repeated forτ∈ {1,3,5}years. Longer maturities raise the option’s exposure to volatility and
alter the signal intensity at which the tail-risk proxy becomes material. Second, the fixed values
α= 0.05 andD 0/V0 = 0.55 are replaced by a grid withα∈[0.01,0.20] andD 0/V0 ∈[0.30,0.80].
For each grid point, the critical signalθ ⋆ is the first signal intensity at which the distance-to-default
proxy falls below 1.5 and the regulator’s private option payoff is positive. Third, the deterministic
signal is replaced by a stochastic signal draw,θ∼Γ(2.4,0.38) truncated to the calibration range,
with small multiplicative disturbances to firm value, debt, and volatility. This produces an empirical
distribution for distance-to-default rather than a single path.
0.0 0.5 1.0 1.5 2.0
0.00 0.02 0.04 0.06 0.08 0.10
Vega and maturity
θ
Vega proxy
tau=1
tau=3
tau=5
0.0 0.5 1.0 1.5 2.0
0.00 0.01 0.02 0.03 0.04
Default−tail proxy
θ
Tail−risk proxy
tau=1
tau=3
tau=5
(a) Maturity effects
0.05 0.10 0.15 0.20
0.3 0.4 0.5 0.6 0.7 0.8
Critical signal θ*
α
L0 = D0 V0
 0.5
 1
 1.5
darker = lower threshold
blank = no crossing (b) Sensitivity grid
Figure 7: Maturity and parameter-sensitivity diagnostics
Notes:Panel (a) repeats the vega and tail-risk calculations forτ= 1,3,5. Panel (b) reports the critical
signal thresholdθ ⋆ over the equity-linked compensation shareαand initial leverageD 0/V0. Darker regions
indicate lower critical thresholds. Blank regions do not cross the selected warning threshold on the grid.
The sensitivity grid is the most direct robustness check. It shows that the warning boundary
is not a knife-edge implication of the baseline normalization. When initial leverage and volatility
are closer to bank-like values, a smaller regulatory signal is sufficient to move the firm toward the
warning region. Conversely, when the firm begins with low leverage or the equity-linked compensa-
tion share is small, the private option payoff and the leverage-vega warning criterion are less tightly
aligned.
The same strike,K= 0.030, is used in the stopping-horizon panel. This avoids changing
the payoff normalization across exercises and makes the horizon grid informative: the career option
is in the money for sufficiently long horizons and sufficiently strong signals, so the plot shows how
quitting horizon and signal intensity affect option value.
16

Monte Carlo distance−to−default
Distance−to−default proxy
Frequency
2 3 4 5
0 200 400 600 800
DD=1.5
0 2 4 6 8 10
0.000 0.002 0.004 0.006
Stopping horizon, K=0.03
τ
Career−option value
theta=0.5
theta=1
theta=1.5
theta=2
Figure 8: Stochastic signal and stopping-horizon diagnostics
Notes:The left panel reports a Monte Carlo distribution of the distance-to-default proxy under stochastic
signal realizations and noisy value, debt, and volatility paths. The dashed line marksDD= 1.5. The
right panel reports the regulator’s career-option value as a function of the quitting horizonτfor several
signal intensities, using the baseline strikeK= 0.030. The stopping-horizon plot is a grid diagnostic for
the optimal quitting-time logic in Theorem 2.4; it is not a full dynamic programming solution.
Table 3: Robustness calibration summary
Statistic Baseline Bank-like Stochastic signal
Initial leverageD 0/V0 0.55 0.65 random path
Asset volatilityσ 0 0.20 0.25 noisyσ(θ)
Criticalθforp d >5%,τ= 1 – 0.48 –
Monte Carlo Pr{DD <1.5}– – 0.008
Monte Carlo Pr{DD <1.0}– – 0.000
Median tail-risk proxy – – 0.0075
95th percentile tail-risk proxy – – 0.0431
Notes:The bank-like anchor setsD 0/V0 = 0.65 andσ 0 = 0.25, values closer to large regulated financial
firms than the normalized baseline. The stochastic signal column uses 10,000 simulated signal draws
with small noise added to value, debt, and volatility. The tail-risk proxy is Φ(−DD), whereDDis the
distance-to-default proxy generated fromx 1 in (2.12b).
The robustness exercises give three takeaways. First, the maturity parameter matters:
longer option horizons change the vega profile and therefore the warning boundary. Second, industry
anchoring matters: the bank-like calibration crosses the 5% tail-risk threshold at a much lower
signal intensity than the normalized baseline. Third, stochastic signals convert the deterministic
warning-region story into a probability statement; in the reported simulation, about 0.8% of paths
fall belowDD= 1.5, while the upper tail of the default-risk proxy remains materially larger than
the median. Thus the calibration remains a proof of concept, but it now shows how the model can
be stress-tested before moving to a full empirical implementation.
17

3.2 Historical regulatory-signal diagnostics
Our model does not claim to forecast the exact dates of institutional failures: it is more
diagnostic. It identifies settings in which the regulatory signal is absent, softened, or converted into
a profit-favoring signal, while the firm moves toward high leverage, high option vega, and lower
distance to default. Three recent financial episodes illustrate the three channels.
Lehman Brothers is the regulatory-vacuum case. Before its 2008 failure, Lehman was not su-
pervised by the Federal Reserve as a bank holding company. The Federal Reserve later emphasized
that it was not Lehman’s supervisor and that Lehman was overseen through the SEC’s voluntary
Consolidated Supervised Entity program rather than through Federal Reserve consolidated super-
vision (Bernanke, 2010). The SEC similarly described the CSE program as an attempt to fill a
statutory gap for large investment-bank holding companies that lacked a consolidated supervisor,
and concluded after 2008 that voluntary regulation did not work (U.S. Securities and Exchange
Commission, 2008). In the language of the model, the relevant signal was not an affirmative com-
mand to take risk but the absence of a binding debt and liquidity penalty. A weak or missing
penalty on leverage lets the firm remain in the go-leverage region until market stress reveals that
distance to default has become too small.
Silicon Valley Bank is the distorted-signal case. Greg Becker, president and chief executive
officer of SVB Financial Group and Silicon Valley Bank, was elected as a Class A director of the
Federal Reserve Bank of San Francisco in 2019 (Federal Reserve Bank of San Francisco, 2019).
The point is not that this board role mechanically caused the bank’s failure; rather, it illustrates a
conflict channel in which the regulated industry is close to the institution that supplies supervisory
signals. The Federal Reserve’s post-failure review found that SVB’s board and management failed
to manage interest-rate, liquidity, and governance risks, that supervisors did not fully appreciate
the bank’s vulnerabilities as it grew, and that the tailoring approach after the Economic Growth,
Regulatory Relief, and Consumer Protection Act reduced standards and promoted a less assertive
supervisory stance (Board of Governors of the Federal Reserve System, 2023). The same review
emphasized that SVB invested largely uninsured deposits in longer-maturity securities and became
acutely exposed when interest rates rose. In the model’s terms, the regulatory signal permitted
a balance-sheet path in which leverage and duration exposure increased while distance to default
weakened.
Signature Bank is the converted-signal case. Former Representative Barney Frank, co-
author of the Dodd–Frank Act, joined Signature Bank’s board after leaving Congress; press cov-
erage at the time of the 2018 regulatory rollback noted that Signature stood to benefit from the
higher asset threshold for enhanced regulation and that Frank had received compensation from the
bank, while Frank denied that the board role changed his policy views (Stein, 2018). The FDIC’s
post-failure review concluded that Signature’s failure was rooted in poor management, rapid and
unrestrained growth, inadequate risk management, overreliance on uninsured deposits, and vulner-
ability to crypto-industry deposit volatility; it also found that supervisory efforts could have been
more timely, forward-looking, and forceful (Federal Deposit Insurance Corporation, 2023). This is
consistent with the model’s converted-signal mechanism: a public-regarding regulatory stance can
become a softer post-agency signal when the agent’s future payoff is tied to the regulated firm’s
value.
The cases above are illustrative; they are not proof that the model is the sole explanation for
any failure. Lehman represents a missing supervisory signal, SVB a distorted and weakly enforced
supervisory signal, and Signature a converted signal mediated by post-public-service incentives
and light oversight. The threshold evidence in Kalmenovitz et al. (2025) gives the empirical proof
for the model’s key incentive channel: when the legal restriction lowers the future value of the
18

revolving-door option, regulators behave as if that option is valuable and alter current choices to
preserve it. In all three historical cases, the relevant prediction is the same: when the debt penalty
is weak and the regulator’s effective signal does not bind early, a firm can cross the leverage-vega
warning region before the public constraint arrives.
4 Conclusion
This paper develops a theoretical model of a regulator’s career option to quit and join a regu-
lated firm. The model links regulatory signals, firm pricing and leverage choices, and the convexity
of future labor-market compensation. When the regulator’s outside opportunity resembles a call
option on firm value, signals that increase firm value, leverage, or volatility can increase the value
of the regulator’s private career option. The same signals may increase value-at-risk in bad states
when they push leverage and vega into the warning or crash regions described in the model.
The proof-of-concept calibration illustrates the model’s comparative statics. It shows how a
regulator-induced signal can raise the career-option payoff while moving the firm from a go-leverage
region into an early-warning or crash-risk region. The exercise is deliberately modest: it clarifies
the internal mechanism and provides a template for future quantitative implementation.
The model suggests several directions for further research. One can estimate the signal
process in settings where regulatory decisions and post-agency employment outcomes are observed;
characterize optimal quitting times for regulators with career options; design contracts or cooling-
off rules that reduce option-like incentives for regulatory capture; and test whether leverage-vega
warning regions predict distress after regulatory forbearance. A Bayesian reputation-learning ex-
tension, in which firms update beliefs about regulator type from observed signals, is also natural;
however, it would add a belief-state variable and updating law, so it is left outside the present
mechanism. The main theoretical message is that revolving-door incentives are not merely static
conflicts of interest. When future compensation is convex in regulated firm value, regulatory signals
can become state-contingent financial claims embedded in the firm’s capital structure.
A Abstract legislative mechanism design for embedding regulator
signals
The main advantage of formulating the problem in the context of an abstract legislative mech-
anism is it allows us to plug in select variables in the reduced form so that we can examine a
taxonomy of regulator signals. In the sequel we define incentive compatibility and participation
constraints for our regulator. And we characterize the revelation principle which induces a regulator
[and firm] to report its type truthfully. Suffice it to say that in the sequel, the regulator designs an
implicit game or indirect legislative mechanism–consistent with maximizing her welfare function–in
which she frames the strategies or choices available to a firm. In order for the firm’s participation
constraint to be binding, the price of its product must be at least equal to its marginal cost. This
is consistent with the revelation principle in Baron and Myerson (1982, pg. 913). In which case,
the firm’s incentive compatibility constraint rests on its ability to maximize profits in that milieu. 7
By contrast, the regulator reports her type truthfully in order to maximize her career option. The
interested reader is referred to Baliga and Sj¨ ostr¨ om (2008) for a brief exposition or B¨ orgers (2008)
for a more detailed exposition on mechanism design theory, and Dal B´ o (2006, pg. 208, Appendix)
for details on application and implementation in the context of a revolving door model.
7We thank Sam Myers Jr. for clarification on this point.
19

State
ω∈Ω
Regulator type
θ∈Θ
Signal map
s: Ω×Θ→G
Strategic space
G
Career-option rule
C:G→X
Direct choice rule
f: Ω×Θ→X
Outcome space
X
s(ω, θ) C
direct mechanism
f ∼= C◦s
Indirect legislative mechanism
Figure 9: Regulator’s abstract mechanism design
Notes:The regulator’s type and the state of nature determine a signal into the strategic spaceG. The
career-option rule maps the induced strategic outcome intoX. The dashed path is the equivalent direct
choice rule, summarized byf ∼= C◦s.
Definition A.1(Mechanism).A mechanismM= (G, C) defines a set of feasible strategic actions
Gavailable to an agent in outcome spaceXwith outcome ruleC:G→X.□
That said, let Θ be a type space for regulators, and Ω be a sample space or states of nature,
Fbe theσ-field of Borel measurable subsets of Ω, andPa probability measure on Ω. LetXbe an
outcome space, andfbe a stochastic choice function such thatf: Ω×Θ→Xis a direct legislative
mechanism. Based on her type, the regulator sends a state dependent signalsinto some strategic
spaceG, i.e.s: Ω×Θ→G. For instance, the spaceGmay comprise the signals(ω, θ) obtained
from the regulator’s welfare maximization; a menu of price (p) dependent profits Π(p) for the firm,
and the strategic formg. So that
G={s(ω, θ),Π(p), g}(A.1)
However, that signals(ω, θ) is subject to the vagaries of the state of nature. Nonetheless, it might
be favorable regulation or deregulation. On the basis of interactions inG, i.e. the firms response,
the regulator maps a payoff functionCintoX, i.eC:G→X. These mappings are depicted in
Figure 9.
Definition A.2((PC): Regulator’s participation constraint).
LetKbe the compensation package of the regulator, assumed fixed over the epoch of career
mobility, andV(ω,Π(p(θ))) be the value of the firm as a function of price dependent profits. The
regulator will participate in exercise of a state contingent career [call] option when
C(s(ω, θ)) = (αV(ω,Π(p(θ)))−K) +
for some equity stake 0< α <1□
Definition A.3((IC): Regulator’s incentive compatibility constraint).
Letθbe the regulator’s true type and ˆθbe any other reported type. Let (Ω,F, P) be a probability
space for states of nature. Then for some eventA∈ Fwe have
Z
A
C(s(ω, θ))dP(ω)≥
Z
A
C(s(ω, ˆθ))dP(ω)
That is, the regulator has incentive to reveal her true type because the expected value of her career
option is greater than the expected value if she does not.□
Figure 9 depicts an indirect mechanism, i.e. “topological lifting” of the stochastic choice function
f. That is, for someω∈Ω we have a composite functionC◦sthat is functionally equivalent tof.
20

Definition A.4(Revelation principle).
Given any feasible career option mechanismC:G→X, there exist a feasible direct legislative
mechanismf: Ω×Θ→Xsuch that forA∈ Fwe have
f(ω, θ)∼= (C◦s)(ω, θ) (A.2)Z
A
f(ω, θ)dP(ω) =
Z
A
(C◦s)(ω, θ)dP(ω) (A.3)
□
With full information the regulator’s [options] contract can be described by the direct
mechanismf. There is no signalling or need for the regulator to implement a set of rules for the
firm. Because everyone knows that regardless of the state of nature Ω, the regulator will quit and
join the regulated firm for a payoff inX. However, that scenario may be associated with a
”P-negligible event, i.e. small probability of occurrence for probability measurePon Ω, in the
Borel subsetsFof Ω. However, with asymmetric information we need to design an option
contract inG-space so that its value isC(s(ω, θ)), ω∈Ω, θ∈Θ. The elements of that state
dependent contract must include firm value and other ”observable” regulatory signaling variables.
For instance, abstract signals can represent the regulator’s effect on taxes, sales, reporting rules,
capital treatment, or other corporate liabilities that affect reported earnings and market value.
References
Altman, E. I. (1984). A further empirical investigation of the bankruptcy cost question.Journal
of Finance 39(4), 1067–1089.
Armstrong, C. S. and R. Vashishtha (2012). Executive stock options, differential risk-taking
incentives, and firm value.Journal of Financial Economics 104(1), 70 – 88.
Athreya, K. B. and S. N. Lahiri (2006).Measure Theory and Probability Theory. New York, N.Y.:
Springer-Verlag.
Baliga, S. and T. Sj¨ ostr¨ om (2008). Mechanism design (new developments). In S. N. Durlauf and
L. E. Blume (Eds.),The New Palgrave Dictionary of Economics. Basingstoke: Palgrave
Macmillan.
Baron, D. P. and R. B. Myerson (1982, Jul.). Regulating a Monopolist with Unknown Costs.
Econometrica 50(4), pp. 911–930.
Berchtold, D., B. Bowler, P. Brockman, Z. Li, and J. Tresl (2026). Navigating policy uncertainty:
Politically experienced directors and corporate investment.Journal of Corporate Finance 99,
103008.
Bernanke, B. S. (2010). Lessons from the failure of lehman brothers. Testimony before the
Committee on Financial Services, U.S. House of Representatives. Available at Federal Reserve
testimony.
Board of Governors of the Federal Reserve System (2023). Review of the federal reserve’s
supervision and regulation of silicon valley bank. Available at Federal Reserve SVB review.
B¨ orgers, T. (2008). Introduction to the Theory of Mechanism Design. Mimeo. Available at
http://www-personal.umich.edu/ tborgers/LectureNotes.pdf.
21

Bortolotti, B., C. Cambini, L. Rondi, and Y. Spiegel (2011). Capital Structure and Regulation:
Do Ownership and Regulatory Independence Matter?Journal of Economics & Management
Strategy 20(2), 517–564.
Boyle, P. P., R. Jha, S. Kennedy, and W. Tian (2011). Stock and Option Proportions in
Executive Compensation.Quarterly Journal of Finance 01(01), 169–203.
Braun, M. and C. Raddatz (2010). Banking On Politics: When Former High-Ranking Politicians
Become Bank-Directors.World Bank Economic Review 24, 234–279.
Cadogan, G. and J. A. Cole (2014). Bankruptcy Risk Induced By Career Concerns of Regulators.
Financial Research Letters 11, 259–271.
Che, Y. (1995). Revolving Doors and the Optimal Tolerance for Agency Collusion.RAND
Journal of Economics, 378–397.
Chesney, M., J. Stromberg, and A. F. Wagner (2012, September). Risk-taking incentives and
losses in the financial crisis. Swiss Finance Institute Research Paper No. 10-18. Available at
http://papers.ssrn.com/sol3/papers.cfm?abstract id=1595343.
Colonnello, S., M. Koetter, A. Sclip, and K. Wagner (2023). The Reverse Revolving Door in the
Supervision of European Banks. Technical report, University Ca’ Foscari of Venice,
Department of Economics Research Paper Series No. 12/2022. Available at
https://ssrn.com/abstract=4269101.
Dal B´ o, E. (2006, Summer). Regulatory Capture: A Review.Oxford Review of Economic
Policy 22(2), 203–225.
De Chiara, A. and M. A. Schwarz (2021). A Dynamic Theory of Regulatory Capture. Technical
report, CESifo Working Paper No. 8968. Available at https://ssrn.com/abstract=3815456.
Emery, L. P. and M. Faccio (2025). Exposing the revolving door in executive branch agencies.
Journal of Financial and Quantitative Analysis 60(4), 1625–1655.
Federal Deposit Insurance Corporation (2023). Fdic’s supervision of signature bank. Available at
FDIC Signature Bank review.
Federal Reserve Bank of San Francisco (2019). Leadership and membership announcements for
the federal reserve bank of san francisco’s board of directors. Available at Federal Reserve Bank
of San Francisco announcement.
Guo, X. (2001). Information and option pricings.Quantitative Finance 1(1), 38–44.
Hall, B. J. and K. J. Murphy (2000). Optimal Exercise Prices for Executive Stock Options.
American Economic Review 90(2), 209–214.
Hamilton, J. D. (2016). Macroeconomic regimes and regime shifts. In J. B. Taylor and H. Uhlig
(Eds.),Handbook of Macroeconomics, Volume 2A, pp. 163–201. Elsevier.
Hansen, B. E. (1999). Threshold effects in non-dynamic panels: Estimation, testing, and
inference.Journal of Econometrics 93(2), 345–368.
Haselmann, R., D. Schoenherr, and V. Vig (2018). Rent seeking in elite networks.Journal of
Political Economy 126(4), 1638–1690.
22

Heims, E. and S. Moxon (2024). Mechanisms of Regulatory Capture: Testing Claims of Industry
Influence in the Case of Vioxx.Regulation & Governance 18(1), 139–157. Available at
https://doi.org/10.1111/rego.12531.
Hirtle, B. and A. Kovner (2022). Bank Supervision.Annual Review of Financial Economics 14,
39–56. Available at https://doi.org/10.1146/annurev-financial-111620-022516.
Hull, J. (2006).Options, Futures, and Other Derivatives(6th ed.). New Jersey: Prentice-Hall, Inc.
Jordan, B. D., S. A. Ross, and R. W. Westerfield (2017).Essentials of Corporate Finance(9th
ed.). New York, NY: McGraw-Hill.
Kalmenovitz, J., S. Vij, and K. Xiao (2025). Closing the revolving door.Journal of Finance.
Forthcoming. Available at SSRN: 4275137 or DOI: 10.2139/ssrn.4275137.
Kane, E. J. (2011, Fall). Unfair Distributional Effects Of Making Taxpayers Bail Out Insolvent
And Ungrateful Financial Firms.Newsletter No. 7. Center for The Study of Financial
Regulation, Mendoza College of Business, University of Notre Dame.
Katic, I. V. and J. W. Kim (2024). Caught in the Revolving Door: Firm-Government Employee
Mobility as a Fleeting Regulatory Advantage.Organization Science 35(1), 281–306. Available
at https://doi.org/10.1287/orsc.2023.1669.
Kempf, E. (2020). The job rating game: Revolving doors and analyst incentives.Journal of
Financial Economics 135(1), 41–67.
Kim, S., M. C. Plosser, and J. A. C. Santos (2018). Macroprudential policy and the revolving
door of risk: Lessons from leveraged lending guidance.Journal of Financial Intermediation 34,
17–31.
Kwan, S. (2009, Dec). Capital Structure in Banking.Economic Letter 37, 1–4. Federal Reserve
Bank–San Francisco.
Lambert, T. (2017, March). Lobbying on Regulatory Enforcement Actions: Evidence from
Banking.Management Science. Forthcoming.
Lucca, D., A. Seru, and F. Trebbi (2014). The Revolving Door and Worker Flows in Bank
Regulation.Journal of Monetary Economics 65, 17–32.
Merton, R. C. (1974, May). On the pricing of corporate debt: The risk structure of interest rates.
Journal of Finance 29(2), 449–470.
Merton, R. C. (1977). An Analytic Derivation of the Cost of Deposit Insurance And Loan
Guarantees: An Application of Modern Option Pricing Theory.Journal of Financial
Economics 1, 3–11.
Myneni, R. (1992). The Pricing of The American Option.Annals of Applied Probability 2(1),
1–23.
Salant, D. (1995). Behind the Revolving Door: A New View of Public Utility Regulation.RAND
Journal of Economics, 362–377.
23

Schram, A. and A. Ule (2024). Regulatory Independence May Limit Electoral Holdup but
Entrench Capture.Public Choice 198, 403–425. Available at
https://doi.org/10.1007/s11127-023-01136-y.
Shepp, L. A. (2002, June). A Model for Stock Price Fluctuations Based on Information.IEEE
Transactions Information Theory 48(6), 1372–1378.
Spiegel, Y. and D. Spulber (1994, Autumn). The Capital Structure of a Regulated Firm.RAND
Journal of Economics, 424–440.
Stein, J. (2018). A lot of people heard what barney frank said about the new banking law. few
knew he works for a bank.Washington Post. Available at Washington Post article.
Stigler, G. J. (1971, Spring). The Theory of Economic Regulation.Bell Journal of Economics and
Management Science 2(1), pp. 3–21.
Terasvirta, T. (1994). Specification, estimation, and evaluation of smooth transition
autoregressive models.Journal of the American Statistical Association 89(425), 208–218.
U.S. Securities and Exchange Commission (2008). Chairman cox announces end of consolidated
supervised entities program. Press Release 2008-230. Available at SEC Press Release 2008-230.
van Dijk, D., T. Terasvirta, and P. H. Franses (2002). Smooth transition autoregressive
models—a survey of recent developments.Econometric Reviews 21(1), 1–47.
Yates, S. and ´E. Cardin-Trudeau (2021). Lobbying “from Within”: A New Perspective on the
Revolving Door and Regulatory Capture.Canadian Public Administration 64(2), 301–319.
Available at https://doi.org/10.1111/capa.12412.
Zimper, A. and S. Hassan (2012). Can industry regulators learn collusion structures from
information-efficient asset markets?Economics Letters 116(1), 1 – 4.
24
