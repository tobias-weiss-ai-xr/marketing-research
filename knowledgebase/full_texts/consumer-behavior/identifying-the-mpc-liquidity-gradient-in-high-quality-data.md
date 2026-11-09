---
title: Identifying the MPC-Liquidity Gradient in High-Quality Data
url: https://arxiv.org/abs/2607.07055
category: consumer-behavior
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Mikael Carlsson
- Marco D'Amico
- Erik Öberg
- Oskar N. Skans
- Karl Walentin
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.07055
pages: 55
chars: 109399
fetched_at: '2026-11-08T13:04:08+00:00'
kb_version: 1
---

# Identifying the MPC-Liquidity Gradient in High-Quality Data

Identifying the MPC-Liquidity Gradient in High-Quality
Data∗
Mikael Carlsson†, Marco D’Amico ‡, Erik ¨Oberg§,
Oskar N. Skans¶, Karl Walentin∥
July 9, 2026
Abstract
We estimate the gradient of the Marginal Propensity to Consume (MPC) with respect to
liquidity using a new estimator designed for administrative data with negligible measure-
ment error in income. We derive a state-dependent consumption pass-through equation
from the canonical buffer-stock model, and show that the pass-through coefficient of this
equation can be used to construct tight bounds on the MPC conditional on the rele-
vant state. We recover latent permanent and transitory income shocks with a Kalman
smoother and use them as regressors in an empirical representation of the consumption
equation. The Kalman-shock estimator identifies the theoretical pass-through coefficient
under the assumption of negligible measurement error in income, and attains the mini-
mum variance within the class of estimators that are linear in household income histories,
including the canonical GMM estimator by Blundell et al. (2008) and recent refinements
thereof. Applying the method to Swedish administrative tax registers, we show that
consumption responses to transitory shocks have a sharp negative and convex gradient
with respect to cash-on-hand; the associated annual MPC falls from 0.7 in the lowest
cash-on-hand decile to 0.3 in the top decile. The permanent-shock pass-through is close
to one across the cash-on-hand distribution. These patterns are not visible when using
traditional, less efficient, estimators.
JEL classification:D15, E21, J11.
Keywords:Marginal Propensity to Consume, Semi-structural Methods, Microdata.
∗We thank Jeppe Druedahl, Johan Gustafsson, Hannes Malmberg, Christian Matthews, Chris Moser, Azeem
Shaikh, Fredrik S¨ avje and Gianluca Violante for helpful discussions. We are also thankful for comments from
participants at multiple seminars and conferences. We are grateful for financial support from Riksbankens
Jubileumsfond (program M23-0019) and Handelsbankens Forskningsstiftelse (project P25-0018). The opinions
expressed in this article are the sole responsibility of the authors and should not be interpreted as reflecting
the views of Sveriges Riksbank.
†† Uppsala University, UCLS and Sveriges Riksbank, mikael.carlsson@nek.uu.se; ‡ Uppsala University,
marco.damico@nek.uu.se; § Uppsala University, University of Oslo, UCLS and CESifo, erik.oberg@nek.uu.se; ¶ Uppsala
University and UCLS, oskar.nordstrom skans@nek.uu.se; ∥ Uppsala University and Sveriges Riksbank, karl.walentin@nek.uu.se.
arXiv:2607.07055v1  [econ.GN]  8 Jul 2026

1 Introduction
The marginal propensity to consume (MPC) is a key link between household income fluctua-
tions and aggregate demand. It matters for the size of fiscal multipliers, the transmission of
monetary policy, and the amplification of macroeconomic shocks. It is also a key statistic for
distinguishing consumption-savings theories and for disciplining heterogeneous-agent models
used for counterfactual policy analysis. As a consequence, a rapidly evolving literature has
focused on documenting the level and distribution of the MPC.
A central branch of this literature employs the “semi-structural” approach, pioneered by
Blundell et al. (2008) (henceforth BPP), and later refined by Commault (2022) (henceforth
BPP-C). The key insight in these papers is that, under a linear consumption rule, the pass-
through of transitory income shocks to consumption can be estimated using linear combina-
tions of the household’s income history (“covariance restrictions”). These estimators were
developed primarily for survey data where income is measured with error and where sample
sizes limit the scope for estimating heterogeneous treatment effects. In that environment,
robustness to measurement error is central.
Recent papers apply these semi-structural estimators to large administrative datasets to
estimate MPCs and MPC gradients, including Ganong et al. (2025), Bilbiie et al. (2025), and
Crawley and Kuchler (2023). In these settings, income histories are precisely measured, and
sample sizes are large enough to study heterogeneity directly. Robustness to severe income
measurement error remains useful, but efficiency and state dependence become more valuable.
This paper adapts the semi-structural approach to a modern data-rich environment. First,
we derive a state-dependent pass-through equation from a canonical buffer-stock consumption
problem, and show how the pass-through coefficient bounds the MPC conditional on the
relevant state. The state variables include cash-on-hand normalized by permanent income,
which we take as our measure of liquidity. Second, we show that Kalman-smoothed shocks
identify the pass-through coefficient and give the minimum-variance signal in the class of
identifying signals that are linear in the household’s income history, which includes BPP
and BPP-C. Third, we apply the estimator to Swedish administrative data on income, wealth,
and budget-constraint-imputed consumption. The main empirical result is a sharp and convex
negative MPC gradient with respect to normalized cash-on-hand: MPCs fall especially quickly
at low levels of cash-on-hand and then flatten out higher in the distribution. A traditional
BPP-style estimator is too imprecise to detect this gradient in our data.
Our theoretical contribution is to connect state-dependent pass-through coefficients to
MPCs, building on the consumption-growth approximation of Blundell et al. (2013) and Arel-
2

lano et al. (2017). We start from a permanent-transitory MA(k) income process and a buffer-
stock consumption-savings problem in the tradition of Deaton (1991) and Carroll (1997).
A linear approximation of the consumption policy gives the pass-through equation. This
equation generalizes the BPP specification by allowing pass-through coefficients to vary with
predetermined household states, especially cash-on-hand normalized by permanent income.
The coefficient on a transitory income innovation cannot mechanically be translated into the
MPC with respect to current income, because such innovations may also contain news about
future income wheneverk >0. However, when the persistence of transitory income shocks is
modest, as in our data, the pass-through coefficient delivers tight bounds on the MPC with
respect to current cash-on-hand. The framework also accommodates liquid/illiquid-asset mod-
els with non-convex adjustment costs, provided that the consumption equation is estimated
conditional on no adjustment in the illiquid account, which we observe in our data.
Our estimator of the state-dependent pass-through coefficient is based on retrieving the
latent permanent and transitory income shocks using a Kalman smoother, inspired by recent
work applying such smoothers to recover shocks from income data (Braxton et al., 2025).
Relative to existing estimators, the advantage of this approach is that we use the full income
history, both past and future, to recover household-level income shocks. Specifically, we
first estimate the parameters of a common permanent-transitory income process from pooled
income-growth moments. We then use the Kalman smoother to form linear predictions of
the latent permanent and transitory shocks. Finally, we regress consumption growth on the
recovered shocks, allowing the coefficients to vary with predetermined state variables.
This procedure is especially well suited for high-quality administrative income data. Under
negligible income measurement error, the Kalman-smoothed shock is the best linear prediction
of the latent shock from the household’s income history, even when the underlying shock
distributions are leptokurtotic (as emphasized in Guvenen et al. (2021)). This projection
identity implies that the population coefficient on the recovered transitory shock identifies the
pass-through coefficient and that the Kalman-smoothed signal has minimum variance within
the class of identifying signals that are linear in household income histories, a class that
includes the BPP and the refined BPP-C estimator. Notably, however, with non-negligible
income measurement error, the Kalman smoother will not be able to distinguish noise from
transitory income shocks, and our approach will therefore be plagued by attenuation bias
when applied to survey data.
We apply the estimator to data from the Swedish administrative tax registers for 2000–
3

2007, covering the universe of tax-paying individuals.1 The data contain income, transfers, de-
mographics, and wealth, and allow us to impute consumption expenditures from the household
budget constraint, following Browning and Leth-Petersen (2003) and Kolsrud et al. (2020).
Our baseline sample focuses on singles, which avoids complications in estimating household
income processes. The results are, however, robust to including multi-member households.
The estimates show a steep and convex cash-on-hand gradient. The average yearly MPC
is about 0.5, ranging roughly 0.7 in the bottom decile of the cash-on-hand distribution to
roughly 0.3 in the top decile, with most of the decline concentrated at low levels of normalized
cash-on-hand. Because these spending responses include some durable purchases, such as cars,
the magnitudes are not far from what one would expect from a calibrated two-asset buffer-
stock savings model, widely used in the macroeconomic literature. When the MPC gradient
by cash-on-hand is decomposed into income and liquid financial wealth components, liquid
financial wealth emerges as the primary driver.
The efficiency property of our estimator is essential for detecting the empirical gradient.
We show this by estimating the same cash-on-hand gradient in the MPC using the BPP-
C estimator. This estimator, as the original BPP estimator, sacrifices efficiency to ensure
robustness to measurement error in income and misspecification of the consumption policy.
It achieves this by only exploiting the covariance between current consumption growth and
distant future income growth, instead of using the full income history as we do. Because of
limited persistence in the transitory shocks, the BPP-C estimator is much less precise than
our estimator and its bootstrapped standard errors are very large. As a consequence, it fails
to detect the gradient in our data. Moreover, while the BPP-C estimates are sensitive to the
assumed lag length of the income process, our estimates remain stable and precise.
We also present results for the consumption response to permanent income shocks. The
same logic underpinning the identification and efficiency results for the transitory pass-through
coefficient also applies to the permanent-shock pass-through coefficient. Also for this param-
eter, the best linear projection of the permanent shock on the income history is the Kalman-
smoothed permanent shock. Here, we find that the consumption response is flat and centered
around one over the cash-on-hand distribution. This pattern is also consistent with the buffer-
stock model interpretation.
Broadly, our paper extends the large and long-standing research program on testing models
of consumption-savings behavior (Modigliani and Brumberg, 1954; Friedman, 1957; Hall, 1978;
Deaton, 1991). The evidence, showing a steep liquidity gradient of consumption responses with
1The same data have been used to study consumption behavior in Flod´ en et al. (2021) and Di Maggio et al.
(2020).
4

respect to transitory income shocks, but a flat gradient with respect to permanent shocks, is
consistent with the canonical incomplete-markets model used widely in the household finance
and macroeconomic literatures.
More narrowly, we make three distinct contributions. First, in terms of methodology, the
paper extends the literature on semi-structural estimators for consumption functions asso-
ciated with Blundell et al. (2008), Arellano et al. (2017), Commault (2022), and Crawley
and Kuchler (2023). We provide a refined methodology for recovering state-dependent pass-
through coefficients and MPCs in data with little measurement error in income. Second, it
complements natural-experiment evidence on MPCs using tax rebates, lottery wins, and un-
employment spells (Johnson et al., 2006; Parker et al., 2013; Misra and Surico, 2014; Fagereng
et al., 2021; Patterson, 2023; Fagereng et al., 2024; Golosov et al., 2024; Boehm et al., 2025).
Those designs are powerful, but they often identify responses to particular shocks or among
selected populations, and it is not clear to what extent they carry over to other settings. Many
of these papers do not detect a clear gradient with respect to liquid assets. In contrast, our
estimates use all yearly variation in earnings, taxes, and transfers and we obtain a signifi-
cant and steep cash-on-hand gradient. Third, the results provide empirical discipline for the
liquidity/MPC channel in heterogeneous-agent macroeconomic models (see, e.g., Kaplan and
Violante (2022) and Auclert (2025)).
The rest of the paper proceeds as follows. Section 2 derives the pass-through equation and
MPC bounds. Section 3 presents the estimator and its properties in terms of identification,
consistency and efficiency. Section 4 describes the Swedish administrative data. Section 5
presents the results. The final section concludes.
2 Identifying Assumptions
In this section, we describe our empirical target and the basic assumptions that allow us to
estimate the MPC. We first derive a state-dependent pass-through equation as a linear approx-
imation of the canonical buffer-stock consumption model (Deaton, 1991; Carroll, 1997), and
then state the additional restrictions that allow us to map a properly estimated consumption
effect of transitory income innovations into MPC bounds. Our approach builds on the linear
approximation in Blundell et al. (2013). The purpose of grounding the pass-through equation
in the buffer-stock consumption model is not to impose a parametric consumption rule. It is
to discipline which state variables are needed to interpret the local response to a new income
innovation.
5

Assumption 2.1(Income process).For individualiin periodt, income (Y i,t) is the product
of a deterministic component (Y d i,t), a permanent stochastic component (P i,t), and a transitory
stochastic component (exp(νi,t)):
Yi,t =Y d i,tPi,t exp(νi,t),(1)
Pi,t =P i,t−1 exp(ηi,t),(2)
νi,t =
kX
j=0
θjεi,t−j, θ 0 = 1.(3)
The permanent innovation (η i,t) and transitory innovation (ε i,t) are mean zero with finite
variances, the transitory component follows an MA(k) process with coefficientsθ j, and the
income-process parameters are common across households.
Assumption 2.1 follows the permanent-transitory representation used in the semi-structural
MPC literature. Permanent shocks shift the level of future income, while transitory shocks
have an MA(k) effect on income. The common-parameter restriction is what makes it pos-
sible to estimate the income process from pooled income-growth moments and then recover
household-level shocks.
Assumption 2.2(Budget set).Households allocate current cash-on-hand (M i,t) between con-
sumption (C i,t) and next-period assets (A i,t+1):2
Ci,t +A i,t+1 =M i,t,(4)
Mi,t = (1 +r)A i,t +Y i,t.(5)
Assumption 2.3(Consumption behavior).Consumption is given by a normalized consump-
tion policy (c):
Ci,t =P i,tc(mi,t,s i,t) (6)
where
c(mi,t,s i,t)≡ Ci,t
Pi,t
, m i,t ≡ Mi,t
Pi,t
,s i,t ≡(ε i,t, . . . , εi,t−k+1).(7)
This consumption policy is the standard implication of a buffer-stock savings model with
CRRA preferences, a linear budget constraint, and borrowing constraints, as in Deaton (1991)
2Here we handle the interest rateras constant. Note that all aggregate time-varying features, including
the interest rate that in theory should have a (minor) impact on the MPC, are neutralized in the empirical
work through year fixed effects and the fact that our deciles are defined through year-specific cash-on-hand
boundaries. Thus, our estimates of each decile-specific MPC capture the average MPC for each decile across
all years in our data.
6

and Carroll (1997). Consumption scales linearly with permanent income, holding the state
variables constant. The state variables are cash-on-hand normalized by permanent income
(mi,t), and the transitory-income state vector (s i,t) contains the recent transitory innovations
that help forecast future income.
In a two-asset model with both liquid wealth and illiquid wealth (as in Kaplan and Violante,
2014a), commonly used in the modern macroeconomic literature, the state space is larger. In
these settings, households also decide whether to adjust illiquid positions, and consumption
responses are typically very different conditional on adjustment relative to non-adjustment.
Our empirical implementation deals with this by focusing on periods without housing trans-
actions, which is the main component of illiquid wealth in Sweden. In the extended two-asset
version of the Deaton-Carroll buffer-stock consumption model, the relevant state variables
conditional on not adjusting the illqiuid position are still normalized cash-on-hand and the
transitory income state vector, as assumed here.
Combining Assumptions 2.1–2.3 gives the pass-through equation. Taking logs and first-
differencing the consumption policy gives
∆ logC i,t =η i,t + logc(m i,t,s i,t)−logc(m i,t−1,s i,t−1).(8)
The budget constraint implies the law of motion
mi,t = 1 +r exp(ηi,t) (mi,t−1 −c(m i,t−1,s i,t−1)) +Y d i,t exp(νi,t).(9)
Conditioning on the predetermined observed state (m i,t−1,s i,t−1) and linearizing with respect
to the new innovations (η i,t, εi,t) gives the following result.
Proposition 1(Pass-through equation).Under Assumptions 2.1–2.3, the first-order approx-
imation to consumption growth aroundη i,t =ε i,t = 0is
∆ logC i,t ≈λ(m i,t−1,s i,t−1)ηi,t +γ(m i,t−1,s i,t−1)εi,t.(10)
The coefficientλis the pass-through of permanent income shocks. The coefficientγis the
pass-through of transitory income shocks and can be written as
γ(mi,t−1,s i,t−1) =Y d i,t exp(ν0 i,t) ∂logc(m i,t,s i,t) ∂mi,t + ∂logc(m i,t,s i,t) ∂s(1) i,t ,(11)
whereν 0 i,t ≡ Pk j=1 θjεi,t−j is the predetermined transitory component ands (1) i,t ≡ε i,t is the
7

current transitory innovation. 3
Proof:See Appendix Section A.
Equation (10) is a state-dependent generalization of the consumption-growth equation
in Blundell et al. (2008). In their specification, log consumption growth similarly depends
linearly on permanent and transitory income shocks, assumed to be common for the entire
population. Here the same two shocks enter consumption growth, but the coefficients are
functions of the household’s predetermined state. Note that the pass-through coefficientsγ
andλare elasticities, and not dollar-to-dollar MPCs. The conversion factor between the two
is the consumption-to-income ratio Cit Yit .
The expression forγin Equation (11) illustrates that this pass-through coefficient is a
composite of two effects. The first term is the cash-on-hand channel: a transitory innovation
raises current resources. The second term is a news channel: the same innovation may also
change expected future income through the MA component. Estimatingγidentifies the total
response to the transitory innovation. To recover the latent information in this coefficient
about the response as an MPC with respect to current cash-on-hand, we need to bound the
importance of the news channel. We do this under the assumption that increased income
today does not decrease income in the future,
Pk
j=1 θj

≥0.
Assumption 2.4(Bounded response to news).For
Pk
j=1 θj

≥0, for all states(m i,t,s i,t),
0≤ ∂logc(m i,t,s i,t)
∂s(1) i,t ≤
 kX
j=1
θj
!
Y d i,t exp(ν0 i,t) ∂logc(m i,t,s i,t) ∂mi,t .(12)
Assumption 2.4 states that good news about future income does not raise current con-
sumption more than receiving the corresponding income today. This is a weak implication of
standard consumption-savings logic: cash-on-hand can be consumed immediately, while news
about future income must be smoothed through the intertemporal budget constraint. The
assumption becomes less restrictive when the transitory component is only weakly persistent,
because then the news channel is small.
Using the conversion factor together with Assumption 2.4, we arrive at the following bounds
for the MPC with respect to changes in current cash-on-hand.
3We have suppressed the dependence ofγonY d i,t here as we remove the deterministic part of (”residualize”)
log income and log consumption in our empirical application.
8

Proposition 2(Bounds on the MPC).Under Assumptions 2.1–2.4, the MPC with respect to
current cash-on-hand satisfies
1
1 + Pk j=1 θj
Ci,t
Yi,t
γ(mi,t−1,s i,t−1)≤M P Ci,t ≤ Ci,t
Yi,t
γ(mi,t−1,s i,t−1).(13)
Proof:See Appendix Section A.
Proposition 1 and Proposition 2 guide the empirical analysis. The empirical section es-
timatesγas a function of the predetermined state and then converts it into MPC bounds
using (13). In our application, the estimated persistence of transitory income is modest, so
the lower and upper bounds are tight.
3 Estimation
To recover the cash-on-hand gradient in the MPC, we need to estimate the state-dependent
pass-through coefficientγin Equation (10). This section describes how we estimate it.
The key premise of our approach is that income is measured with little error. This premise
is justified in administrative data, where the main income components are tax-based and
third-party reported. It is less suitable for survey data, for which canonical estimators were
originally developed, such as BPP and the refined BPP-C. Those estimators sacrifice precision
in order to remain robust to income measurement error. We instead use the full income history
to recover the latent shocks as precisely as possible.
Our estimation procedure has three steps. First, we estimate the common income process
from pooled income-growth moments. Second, we recover household-level permanent shocks
bηi,t and transitory shocksbεi,t using the Kalman smoother based on household income histories.
Third, we estimate the empirical counterpart of the theoretical pass-through equation using
the recovered shocks, within cells of the predetermined state variables:
∆ logC i,t =µ+b η(·)bηi,t +b ε(·)bεi,t +u i,t.(14)
Equation (14) is written with generic population regression coefficientsb η(·) andb ε(·).
The residualu i,t captures variation in consumption behavior orthogonal to the income-history
signal, such as taste shocks and independent measurement error in consumption.
There is no mechanical reason why the coefficientb ε(·) in the estimating equation (14)
needs to inform us about the theoretical pass-through coefficientγ(·) in Equation (10). Here,
the regressors are recovered signals rather than the latent shocks themselves. Using the fact
9

that the Kalman smoother provides the best linear projection of the latent shocks, we prove
identification and efficiency under the assumption of no measurement error in income or the
underlying state variables. We then show that the bias resulting from relevant magnitudes of
measurement errors in income, or estimated state variables, are small.
3.1 Income Process Parameters
The first step of our procedure is to estimate the income process parameters. We estimate
(θ1, . . . , θk, σ2 ε , σ2 η) from pooled autocovariances of residual income growth, following standard
practice. An MA(k) transitory component in income levels implies an MA(k+ 1) component
in income growth:
∆ logY i,t =η i,t +
k+1X
j=0
ψjεi,t−j,(15)
whereψ 0 = 1,ψ j =θ j−θj−1 for 1≤j≤k, andψ k+1 =−θ k. Leta ℓ ≡Cov(∆ logY i,t+ℓ,∆ logY i,t)
denote the autocovariance of income growth at lagℓ. The autocovariances satisfy
a0 =σ 2 η +σ 2 ε
k+1X
j=0
ψ2 j ,(16)
aℓ =σ 2 ε
k+1X
j=ℓ
ψjψj−ℓ, ℓ= 1, . . . , k+ 1.(17)
We choose the values of (θ 1, . . . , θk, σ2 ε ) that match the nonzero autocovariancesa 1, . . . , ak+1,
and then recoverσ 2 η from the variance identity (16).
3.2 Kalman smoothing
The second step is to recover the latent shocks. Conditional on the income process parameters,
we write (15) as a standard state-space model with state vector
αi,t = (ηi,t, εi,t, εi,t−1, . . . , εi,t−k−1)′.(18)
and denote each household income history with
yi = (∆ logY i,1, . . . ,∆ logYi,Ti)′.
We run a Kalman filter followed by a fixed-interval smoother. Appendix B gives the state-
10

space implementation details. The filter forms one-sided predictions using income growth
up to datet. The smoother uses the full income path, including future income growth, to
decompose observed income changes into permanent and transitory shocks.
The recovered shocks form the best linear projection of the latent state ony i. By best
linear projection, we mean that Proj(X|Z) = Cov(X,Z) Var(Z) −1Z, given thatXandZ
have been centered. One may therefore interpret the recovered shocks as the permanent and
current-transitory components of this projection:
(bηi,t,bεi,t) = Proj ((ηi,t, εi,t)|y i).(19)
This interpretation is valid for any distribution of the latent shocks with finite variances and
serially uncorrelated innovations. This is reassuring, because household income changes are
in general not well described by a normal distribution, as highlighted by the recent literature
on income process estimation, see, e.g., Guvenen et al. (2021). Our estimator only uses the
covariance structure of the income process, and not the full distribution of income shocks.
With Gaussian shocks, however, the interpretation of the recovered shocks strengthens: the
recovered shocks are in that case conditional expectations, not merely best linear predictions.
Figure 1 illustrates the logic of the Kalman smoother, interpreted as a model-based event-
study filter. Around each date, the income path is compared to the dynamic footprints of
permanent and transitory shocks. A permanent shock leaves a persistent change in income.
A transitory shock leaves the MA footprint (a “spike”) implied by the estimatedθ’s. The
smoother assigns the date-tshock the best linear prediction implied by these footprints, using
all available dates rather than a single future-income moment. The same observed income
movement can be decomposed differently depending on what happens before and after the
date of interest, and thus both past and future income growth are essential to forming the
prediction.
3.3 Identification
The recovered shock is a generated regressor. The key projection identity in Equation (19) is
nevertheless enough for the population coefficient in (14) to identify the pass-through coeffi-
cientγ, provided that the pass-through equation is correctly specified after conditioning on
the true state, the permanent shock is controlled for, and the residual consumption-growth
component is orthogonal to the income-history signal.
Proposition 3(Identification of the pass-through coefficient).Let the state-dependent pass-
11

Figure 1: Dynamic footprints of income shocks
Notes:The transitory shock is illustrated with a small MA(1) component, calibrated to the persistence
estimated in our baseline income process.
through equation hold within a state cell, or after partialling out state controls, and suppose
that income is measured without error. Suppose also that the residual componentω i,t is or-
thogonal to the income-history signal after conditioning on the state and the permanent-shock
component. Let
bεi,t = Proj(εi,t |y i),y i = (∆ logY i,1, . . . ,∆ logYi,Ti)′.
Then the population coefficientb ε(·)in Equation(14)equalsγin Equation(10).
Proof:See Appendix Section C.
The intuition is that the shock obtained from the Kalman smoother is a noisy signal of the
true transitory shock, but the noise is the projection error. By construction, this projection
error is orthogonal to the signal itself. Therefore the covariance between the signal and the
true shock equals the variance of the signal. Once the permanent shock and the state variables
have been controlled for, this is the covariance restriction needed for the regression coefficient
onbεi,t to recoverγ.
The permanent-shock control is essential. If it is omitted, the probability limit of the
transitory coefficient contains the omitted-variable term
γ+λ Cov(bεi,t, ηi,t) Var(bεi,t) .(20)
12

The point is not that the underlying shocks are correlated. By assumption,η i,t andε i,t
are orthogonal. The issue is that the estimated signals are both constructed from the same
observed income history. The smoothed transitory signal can therefore be correlated with
the permanent shock component, even when the latent innovations are orthogonal. Thus the
estimator is not a regression of consumption growth on the transitory signal alone. It is a
regression of consumption growth on the transitory signal after accounting for the permanent
shock and the state variables that define the pass-through coefficient.
3.4 Efficiency
The same projection logic also gives an efficiency result. Consider estimators that consistently
identifyγusing signals or instruments that are linear functions of the observed income history,
which includes our projection estimator. Within this class, our estimator is the most efficient
one.
Proposition 4(Minimum-variance linear income-history signal).Among all valid scalar in-
strumentsZ i,t =a ′yi that are linear in the income history and identifyγ, the projection signal
bεi,t = Proj(εi,t |y i)
minimizes the asymptotic variance of the IV estimator ofγ. For any admissibleZ i,t,
Avar(bγ(Z))
Avar(bγ(bε))= ρ2(bεi,t, εi,t) ρ2(Zi,t, εi,t) ≥1.(21)
Equality holds if and only ifZ i,t is proportional tobεi,t.
Proof:See Appendix Section C.
The intuition is simple. Precision is governed by how strongly the identifying signal is
correlated with the latent transitory shock. The best linear projection is, by definition, the
linear combination of the income history that maximizes this correlation, which is the Kalman-
smoothed shock. All other valid linear income-history signals use less information, or use the
same information with non-optimal weights.
The same logic underpinning our identification and efficiency results for the transitory
pass-through coefficientγalso applies to the permanent-shock pass-through coefficientλ. The
best linear projection of the permanent shock on the income history is the Kalman-smoothed
permanent shock, and all other valid linear income-history signals use less information, or
13

use the same information with non-optimal weights. We focus on the transitory pass-through
coefficient in the main text because it is the key object of interest for the MPC gradient.
3.5 Relation to BPP and BPP-C
The class of estimators that consistently identifyγusing linear income-history signals includes
most estimators in the literature. In particular, it includes the BPP estimator and the refined
BPP-C estimator. The BPP-C estimator is adopted in recent studies using administrative
data such as Bilbiie et al. (2025) and Ganong et al. (2025).
BPP estimates pass-through from covariance restrictions implied by the permanent-transitory
income process. The key idea is to use future income growth to isolate the transitory compo-
nent of current income growth. Future income growth is orthogonal to the current permanent
shock, because a permanent shock changes the level of future income but not future income
growth. At the same time, future income growth is correlated with the current transitory
shock because the transitory component leaves a finite dynamic footprint in income growth.
In our notation, the BPP instruments are selected elements of the income history,
ZBP P i,t =R tyi = (∆ logY i,t+1,∆ logY i,t+2, . . . ,∆ logYi,t+q)′,y i = (∆ logY i,1, . . . ,∆ logYi,Ti)′.
HereR t is a selection matrix. The moment condition for the transitory pass-through can be
written as
E
h
ZBP P i,t

^∆ logC i,t −γε i,t
i
= 0,
or equivalently as a set of covariance restrictions using the model-implied vector Cov(ZBP P i,t , εi,t),
which is why BPP fits into our comparison class. Although their estimator is written as a
GMM, every moment is built from a linear function of the income history. With optimal
GMM weighting, the estimator uses an effective scalar signalw ′ZBP P i,t =w ′Rtyi, which is still
linear iny i.
The virtue of the BPP moments is robustness. By relying on future income growth rather
than contemporaneous income growth, the estimator avoids the direct contamination that
classical income measurement error creates at datet. The cost is that the selected future
leads need not be the most informative linear combination of the household’s income path.
The Kalman-smoothed shock uses the same income process, but combines all dates at which
a transitory shock leaves a footprint.
The BPP-C estimator starts from the same logic but asks which future-income moment
remains valid when log consumption growth is allowed to also respond (linearly) to past
14

transitory shocks. This is particularly relevant in settings where one cannot condition on the
relevant state variables, which is typically the case in small-sample survey data such as the
PSID. Without state-dependence, Equation (10) implies that consumption is a random walk,
which is not consistent with standard theory.
If past transitory shocks also affect current consumption growth, some future-income mo-
ments are correlated with both the current transitory shock and the past shocks entering
consumption growth. The BPP-C estimator therefore selects the future lead that filters out
both the permanent shock and the past transitory shocks. With an MA(k) transitory income
component, this robust moment uses
Z C i,t = ∆ logY i,t+k+1.
This instrument is a single element of the same income-history vector,Z C i,t =ι ′ t+k+1yi, and is
therefore also linear in income history.
Relative to BPP, the virtue of the BPP-C estimator is thus not only robustness to mea-
surement error in income, but also robustness to misspecification of the consumption function.
The price of BPP-C’s robustness is an even weaker signal: it uses only one future-income re-
alization, namely the most distant realization that still contains information. The cost is that
this distant lead can be a weak signal: its identifying covariance is governed by the last MA
coefficient, which is small when transitory-income persistence is modest. BPP-C can therefore
suffer from a weak-instrument problem, as we illustrate in Section 5.
In contrast, our projection estimator uses the full dynamic footprint of the transitory shock
and is more efficient. Moreover, our approach addresses Commault (2022)’s misspecification
critique of BPP by allowing for state-dependence. If there are other behavioral channels
through which past transitory shocks affect current consumption growth not encapsulated by
Assumption 2.3, our approach remains valid as long as these past shocks are also controlled
for when estimating Equation (14). 4
3.6 Income measurement error implies a (favorable) bias-variance
trade-off
Propositions 3 and 4 give identification and efficiency assuming no measurement error in
income. The administrative data used here likely contains very limited measurement error,
4Maintaining the assumptions of no measurement error in income and a correctly specified state-conditioned
consumption equation, it is possible to use near-lead income growth as an instrument together with ex-post
bias correction to recover the true pass-through coefficient. We elaborate on this in Appendix Section F.4.
15

but we cannot guarantee it is zero. It may also be interesting to ask what happens when
implementing our estimator in settings with substantial income measurement error, such as
the PSID and other survey data.
With measurement error in income, the Kalman-smoothed shock is computed from a con-
taminated income history and the estimator can be biased. Intuitively, with i.i.d. measurement
error, the Kalman smoother will not be able to distinguish noise from short-lived transitory
income shocks; both would look like spikes in the income growth history, as in the left panel
of Figure 1. The resulting shock series thus contains noise, and the projection estimator will
feature attenuation bias, in contrast to the robust BPP and BPP-C estimators. Nevertheless,
the estimator is still very efficient as it uses more information to recover the shocks.
Appendix D describes two simulation exercises that quantify this trade-off. The first mim-
ics survey data, where income and consumption measurement errors are i.i.d. and independent.
In that setting, the BPP-C estimator remains centered on the true pass-through coefficient,
while the naive linear-projection estimator is attenuated as income measurement error rises.
The second mimics budget-constraint imputation (as in our data), where income measurement
error mechanically enters imputed consumption. In that setting, the same error appears in
both the income and consumption equations, and the naive linear-projection estimator can be
biased upward. Across both simulations, the bias is very small and the confidence intervals
for the BPP-C estimator are much larger than for the “naive” linear-projection estimator for
all reasonable levels of income measurement error.
3.7 Measurement error in the state variables implies (small) atten-
uation bias
The preceding identification argument treats the predetermined state variables as observed.
In the empirical implementation, however, the state is partly estimated. This matters because
the cash-on-hand gradient in the MPC is identified from differences in pass-through coefficients
across state cells. Per proposition 3, noise stemming from the estimation in a state variable
does not generally bias the average pass-through coefficient, but it mixes households across
true state cells. If the true pass-through coefficient is decreasing in the state, observations
assigned to a low-state cell include some households whose true state is higher, and observa-
tions assigned to a high-state cell include some households whose true state is lower. This
attenuates the estimated gradient toward zero, and that estimated gradient should therefore
be interpreted as a conservative lower bound of the true gradient’s magnitude.
In this paper, we are primarily interested in how the pass-through coefficient and its asso-
16

ciated MPC vary with one of the state variables: normalized cash-on-hand. For normalized
cash-on-hand, the measurement-error problem has a useful special structure. Recall that
normalized cash-on-hand is defined asm i,t = Mi,t Pi,t , whereM i,t is cash-on-hand andP i,t is
permanent income. In our data, the liquid-wealth component ofM i,t is observed in the reg-
isters, whileP i,t is recovered from the estimated income process. After residualizing income
(removingY d), we can write log income as logY i,t = logP i,t +ν i,t, whereν i,t is the transitory
income component. The smoothed permanent-income estimate can similarly be written as
log bPi,t = logY i,t −bνi,t. It follows that
logbmi,t −logm i,t =bνi,t −ν i,t.
Thus, the sorting error in normalized cash-on-hand is the recovery error in the transitory
income component.
This identity bounds the magnitude of the problem. Since the Kalman-smoothed transi-
tory component is the linear projection ofν i,t on the income history, the projection error is
orthogonal to the recovered component. In particular,
Var(bνi,t −ν i,t) = Var(νi,t)(1−R 2 ν),
whereR 2 ν ∈[0,1] is the reliability of the recovered transitory component. Under the baseline
MA(1) specification,ν i,t =ε i,t+θ1εi,t−1. The Singles estimates in Table 2 imply sd(νi,t)≃0.11;
the corresponding number for Households is also about 0.11. This is an upper bound on the
log cash-on-hand sorting error before using the information in the household’s income history.
To interpret the scale, the empirical standard deviation of log normalized cash-on-hand is
about 0.32 in both samples, which means that worst case attenuation of a linear slope under
classical measurement error is about 11 percent. 5 The Kalman smoother reduces this error
5A simple classical-error calculation gives the interpretation. If logbmi,t = logm i,t+ei,t withe i,t independent
of logm i,t and sd(ei,t)≤0.11, then
Corr(logbmi,t,logm i,t)≥
s
Var(logm i,t)
Var(logm i,t) + 0.112 .
For a linear pass-through gradient in log cash-on-hand, the corresponding upper bound on slope attenuation
is
Var(logm i,t)
Var(logm i,t) + 0.112 .
These formulas are illustrative because the empirical estimator bins observations into deciles and the Kalman
recovery error need not be exactly classical.
17

further in proportion to the reliability of the recovered transitory component, meaning that
the actual attenuation is likely much smaller.
4 Data and Measurement
4.1 Data Description
Our empirical analysis uses yearly observations from Swedish administrative registers linked
at the individual and household level over 2000–2007. The main source is LISA, which merges
tax and transfer registers for the universe of individuals aged 16 and above and provides annual
information on labor earnings, capital income, transfers, taxes, and rich socio-demographic
characteristics. We link LISA to complementary wealth registers covering financial and real
assets. We keep the exposition concise here, and provide all relevant details in Appendix E.
We impute consumption from income and wealth using the household budget constraint,
Ci,t =Y i,t −S i,t,
whereY i,t is disposable income andS i,t captures active saving flows (net asset purchases and
net debt repayment). Savings are constructed asset by asset using quantity- and price-based
approaches so that passive valuation changes do not mechanically enter consumption, following
Kolsrud et al. (2020) and Browning and Leth-Petersen (2003). Appendix E reports all details
in this procedure and compares the resulting aggregate series to national accounts and survey
consumption.
Our measure of disposable income includes all non-capital income, net of taxes and trans-
fers. We do not include capital income, which is endogenous to consumption and saving
decisions. We residualize log income and log consumption before constructing growth rates
using standard characteristics following Blundell et al. (2008), including time fixed effects.
Wealth is measured in terms of the financial position of households at the end of each cal-
endar year. The wealth register reports only position above 10,000 SEK (∼1200 USD). Obser-
vations below 10,000 SEK are thus treated as zeros. We measure wealth in three components.
Liquid wealth(A liq i,t ) is the sum of all financial assets, including bank deposits, listed securities,
and other marketable financial positions. It does not include the pension claims within the
public pension system, as these claims are not accessible prior to retirement.Net illiquid
wealth(A illiq i,t ) is housing and other non-marketable real assets, primarily owner-occupied and
co-operative dwellings valued at register prices, net of all debt (which mainly consists of mort-
18

gages and government-provided student debt).Net total wealth(A net i,t ) sums liquid wealth and
net illiquid wealth.
We work with two estimation samples.Singlesis our baseline sample: individuals aged 30–
65 who are not married or cohabiting and who satisfy basic data-quality restrictions.House-
holdsadds married and cohabiting couples observed in the same dwelling. For households, we
estimate the income processes on the joint income of the household members, after residualiz-
ing with respect to characteristics of the household head. We selected Singles as our baseline
sample to avoid any issues with income process estimation that result from residualization
and within-household insurance.
When estimating the second stage consumption function equation (14), both samples ex-
clude individual-year observations with transactions in illiquid assets, that is, housing and
co-operative-apartment purchases and sales. We do this because we assume a single liquid as-
set when deriving our estimating equation. From the perspective of a model that also includes
illiquid assets, as in Kaplan and Violante (2014b) and Bayer et al. (2019), our pass-through
coefficients should be interpreted as conditional on not adjusting the illiquid account.
4.2 Descriptive Statistics
Table 1 reports medians and means for the Households and Singles estimation samples. Mone-
tary values are expressed in 2003 SEK, when 1 SEK∼0.12 USD. Average consumption tracks
disposable income closely in both samples, which is in line with the very low Swedish aggre-
gate savings rate. Specifically, the aggregate savings rate as a fraction of disposable income
was 2% on average during 1999–2007. 6 For income, consumption, and wealth, medians are
significantly lower than means, reflecting the fat right tails of all distributions.
Figure 2 plots the distributions of net total wealth, net illiquid wealth, and liquid wealth.
Wealth is highly skewed in both samples: medians are modest in Table 1, while the right tails
are long, especially for Households. The panels for net illiquid wealth cap the vertical axis
to make the tail visible. A large share of observations have zero measured net illiquid wealth
(recall the cap from below at 10,000 SEK), reflecting the discrete nature of home ownership.
Figure 3 plots the distributions of consumption, disposable income, and lagged cash-on-hand.
6Note that the aggregate savings rate, unlike our microdata sample, includes the dissaving of retired
individuals.
19

Figure 2: Distribution of wealth components
(a) Net total wealth, households
 (b) Net total wealth, singles
(c) Net illiquid wealth, households
 (d) Net illiquid wealth, singles
(e) Liquid wealth, households
 (f) Liquid wealth, singles
Notes:Kernel density estimates pool household-year observations over 2000–2007. Variables are in
thousand 2003 SEK. Peaks in the liquid-wealth panels are capped to show tail behavior.
20

Table 1: Summary statistics
Households Singles
Median Mean Median Mean
Share of males (%) 48.28 48.28 57.31 57.31
Male age 44.00 45.42 45.00 45.83
Female age 48.00 47.71 52.00 49.51
Household size 1.00 1.68 1.00 1.00
Disposable income 188,357 215,397 164,131 171,506
Cash on hand 224,643 1,441,242 190,357 273,404
Consumption 192,074 244,084 163,389 192,607
Net total wealth 20,424 1,499,607 8,090 317,870
Liquid wealth 12,536 1,278,938 8,294 148,760
Illiquid wealth 0 173,537 0 127,667
Notes:Monetary values are in 2003 SEK. Samples pool household-year observations over
2000–2007 (Households: 8,037,370; Singles: 5,631,963). Means are sensitive to top wealth
observations.
21

Table 2: Income-process moments and baseline MA(1) parameter estimates
A. Singles: moments
∆ lnyt ∆ lnyt+1 ∆ lnyt+2
∆ lnyt
0.0301
(0.0299, 0.0303)
-0.0074
(-0.0075, -0.0073)
-0.0026
(-0.0027, -0.0025)
∆ct
0.0218
(0.0216, 0.0220)
-0.0037
(-0.0039, -0.0036)
-0.0022
(-0.0024, -0.0021)
N1,724,757
B. Singles: parameters
θ σ 2 ϵ σ2 η
Estimate
0.2191
(0.2140, 0.2242)
0.0123
(0.0122, 0.0125)
0.0097
(0.0094, 0.0099)
N1,724,757
C. Households: moments
∆ lnyt ∆ lnyt+1 ∆ lnyt+2
∆ lnyt
0.0293
(0.0292, 0.0294)
-0.0072
(-0.0073, -0.0071)
-0.0026
(-0.0026, -0.0025)
∆ct
0.0222
(0.0221, 0.0223)
-0.0039
(-0.0040, -0.0038)
-0.0023
(-0.0024, -0.0022)
N3,060,626
D. Households: parameters
θ σ 2 ϵ σ2 η
Estimate
0.2213
(0.2176, 0.2249)
0.0120
(0.0119, 0.0121)
0.0095
(0.0093, 0.0096)
N3,060,626
5 Empirical Results
We first present results concerning the income process of the household and then estimates of
the consumption pass-through coefficients and state-dependent MPCs. For all results using
estimated pass-through coefficients, standard errors are bootstrapped, clustered at the level
of the household. The bootstrap procedure is applied to the entire estimation procedure,
from the extraction of the shocks through the second-stage estimation of Equation (14). The
resulting standard errors therefore account for estimation error in the generated regressors, the
Kalman-smoothed shocks, as well as uncertainty about the distribution of the second-stage
OLS residuals. For the income-process estimates, we report conventional analytical standard
errors.
5.1 Income-Process Estimates and the State Variable Distribution
Table 2 reports the income-process moments and baseline MA(1) parameter estimates. The
estimates are very similar in the Singles and Households samples.
Income growth has a large contemporaneous variance and negative first and second auto-
covariances, with the second smaller in absolute value. We conclude that the lag length of the
MA(k) transitory income process is therefore at most 2. We select the MA(1) specification
as our baseline, and show that our results are robust to selecting an MA(2) specification in
Appendix F. Since transitory persistence determines the width of the MPC bounds in Propo-
sition 2, the documented small persistence in transitory income means that we can retrieve
tight MPC bounds from the pass-through coefficients.
22

Figure 3: Distribution of consumption, disposable income, and cash-on-hand
(a) Consumption and income, households
 (b) Consumption and income, singles
(c) Lagged cash-on-hand, households
 (d) Lagged cash-on-hand, singles
Notes:Kernel density estimates are pooled over 2000–2007. Variables are in thousand 2003 SEK.
23

These estimates are broadly aligned with previous evidence on the time-series properties of
disposable income, but the magnitudes of both the variances and autocovariances are smaller
compared to US survey evidence, which is expected when there is less measurement error.
In the PSID-based estimates reported by Commault (2022), which use the same data as
Blundell et al. (2008), the autocovariances of annual log income growth have the same shape
as in Table 2: a large contemporaneous variance and negative covariances at the first two
leads. Accordingly, Commault (2022) selects an MA(1) specification.7 Our Swedish covariance
estimates are lower in absolute value, with a contemporaneous variance around 0.03 rather
than 0.066 and first- and second-lead covariances roughly one-third to one-half as large. The
larger covariances at short horizons in the PSID likely reflect i.i.d. measurement error in
income. They are similarly comparable to the other cross-country survey-based disposable-
income estimates in Krueger et al. (2010), but with variances at the low end of the range.
With an estimated income process, we apply the Kalman smoother and retrieve the un-
derlying shocks. The level of permanent income is initialized using lagged observed dispos-
able income and then constructed recursively from the recovered permanent shocks, bPi,t =
bPi,t−1 exp(bηi,t). With these estimates, we can then construct the central state variable used to
estimate the heterogeneity in consumption response: cash-on-hand normalized by permanent
income. Figure 4 shows the distribution of this variable. As expected, the distribution peaks
between 1 and 2, indicating that cash-on-hand for the bulk of households is between one and
two years of permanent income, and contains a fat tail with some households holding liquid
wealth worth several years of permanent income.
5.2 Pass-Through Coefficients
Under the MA(1) baseline, the predetermined state is (mi,t−1, εi,t−1). We partition observations
into a 10×10 grid using lagged normalized cash-on-hand and the lagged transitory shock.
We retrieve the Kalman-smoothed permanent and transitory shock signals from the pooled
sample, and then estimate Equation (14) within these cells. The figures below collapse the grid
to cash-on-hand profiles by averaging over the lagged-transitory-shock bins. The horizontal
coordinate for each point is not the decile number, but the observation-count-weighted average
of lagged normalized cash-on-hand,m i,t−1, among observations in that cash-on-hand bin.
Figure 5 reports the baseline MA(1) pass-through profiles. The transitory pass-through
7Statistical significance is not a good criterion for selecting the lag length in administrative data, since
the large sample size and low measurement error mean that the covariance at almost all leads is statistically
significant.
24

Figure 4: Distribution of lagged normalized cash-on-hand
(a) Households
 (b) Singles
Notes:Kernel density estimates pool household-year observations over 2000–2007. Cash-on-hand
is normalized by permanent income, constructed using the MA(1) income-process estimates. The
horizontal axis can therefore be interpreted as multiples of yearly permanent income.
coefficient declines with cash-on-hand in both samples, which is the direct source of the MPC
gradient below. The permanent-shock pass-through is much flatter and is centered around
one over most of the distribution. This pattern is consistent with the buffer-stock model
interpretation: cash-on-hand matters most for the response to transitory resources, while
permanent shocks shift lifetime resources and therefore have a more uniform effect across the
distribution.
5.3 MPC Gradients by Cash-on-Hand
We convert the transitory pass-through coefficient into the bounds on the MPC in Proposi-
tion 2 and average across the lagged-shock bins within each cash-on-hand decile. The figures
below report the lower bounds. Becauseθ 1 is around 0.22 in both samples, the upper bounds
are obtained by multiplying the plotted profiles by about 1.22. The slope of the profile is there-
fore not affected by the bound conversion: the conversion scales all deciles within a sample by
the same factor.
Figure 6 shows the main result. The projection estimator produces a steep downward
yearly MPC profile for Singles. The profile is convex in average normalized cash-on-hand:
most of the decline occurs at low cash-on-hand levels, while the profile is flatter over the
upper part of the distribution. The lower (upper) bound is 0.68 (0.83) in the lowest cash-
on-hand decile and about 0.31 (0.38) in the highest decile. The gradient is clearly downward
sloping and precisely estimated. The population-average lower bound is about 0.47, with an
25

Figure 5: Pass-through coefficients by cash-on-hand
Notes:Panels report Singles and Households. Estimates are computed within decile bins of lagged
normalized cash-on-hand; the horizontal axis plots the observation-count-weighted average normalized
cash-on-hand in each bin. Each panel shows permanent- and transitory-shock pass-through coefficients
from the OLS projection estimator. Shaded regions show 95 percent confidence intervals based on
bootstrap standard errors clustered at the household level.
upper bound of about 0.58.
The Households panel repeats the exercise for the broader household sample. The level
of the MPC is slightly higher in the upper part of the cash-on-hand distribution than in the
Singles sample, but the main pattern is the same: a large drop at low levels of normalized
cash-on-hand followed by a flatter profile further out in the distribution. The lower (upper)
bound declines from about 0.65 (0.80) in the first decile to about 0.40 (0.48) in the tenth
decile.
The empirical gradient is the pattern predicted by buffer-stock consumption models. House-
holds with little (permanent-income normalized) cash-on-hand have limited self-insurance and
respond strongly to transitory income changes. Households with more cash-on-hand can
smooth the same shock over time, so their current consumption response is smaller. The
estimates therefore connect the pass-through equation in Proposition 1 to the key macroeco-
nomic object emphasized by heterogeneous-agent models: the cross-sectional distribution of
liquid resources shapes aggregate demand transmission.
At the same time, the level of the response, even though it refers toyearlyMPC, is
substantial even at the upper end of the cash-on-hand distribution. This tendency for the
top cash-on-hand decile is stronger for the Household sample (0.40) than the Singles sample
(0.31). It is higher than one might expect from a single-asset, single-good model, where
households with substantial liquid resources behave more like permanent-income consumers.
26

Figure 6: MPC by cash-on-hand
Notes:Estimates show lower bounds of the MPC, and are computed within decile bins of lagged
normalized cash-on-hand; the horizontal axis plots the observation-count-weighted average normalized
cash-on-hand in each bin. Shaded regions show 95 percent confidence intervals based on bootstrap
standard errors clustered at the household level.
However, our outcome is an expenditure measure rather than nondurable consumption alone,
and it includes durable purchases such as cars and furniture. As emphasized by Maxted et al.
(2025), durable expenditures make the marginal propensity to spend significantly larger than
the MPC predicted by a model with only one nondurable consumption good. They derive a
conversion factor using a standard two-good model. Using their parameter values, the implied
conversion factor between a yearly nondurable+durable MPX and the yearly nondurable MPC
is about 1.5. Our baseline singles estimates would thus imply a gradient of the lower bound of
the yearly nondurable MPC from about 0.45 in the first decile to 0.21 in the last decile, with
a population average of 0.32, which is not far from what is implied by a standard calibration
of a two-asset buffer-stock model (Kaplan and Violante, 2014a).
5.4 MPC Gradients: Income or Liquid Wealth
Permanent-income normalized cash-on-hand is the sum of normalized liquid wealth and nor-
malized disposable income. Figure 7 partitions observations by the permanent-income-normalized
components of lagged cash-on-hand while continuing to average over the remaining state vari-
ables. The liquid-wealth gradient is steep in both samples. In the Singles sample, the lower-
bound MPC falls from about 0.70 at the bottom of the liquid-wealth-component distribution
to close to zero at the top. In the Households sample, the same gradient declines from about
27

Figure 7: MPC by components of cash-on-hand
Notes:Estimates show lower bounds of the MPC, and are computed within decile bins of the relevant
permanent-income-normalized cash-on-hand component; the horizontal axis plots the observation-
count-weighted average component divided by permanent income in each bin. Shaded regions show
95 percent confidence intervals based on bootstrap standard errors clustered at the household level.
0.77 to about 0.24. That fact the number of points is fewer than 10 reflects that liquid wealth
is below the detection limit of 10 000 SEK for a large share of the sample, consistent with the
descriptive statistics in Table 1.
There is less variation in MPC across the disposable-income component, and the profile is
non-monotone. For both Singles and Households, the lower-bound MPC falls from the bottom
of the normalized disposable-income-component distribution through the middle deciles and
then rises again at the top. This comparison suggests that the main driver of the cash-on-hand
gradient in Figure 6 is the gradient in liquid wealth, rather than the gradient in disposable
income.
5.5 Comparison to BPP-C
Figure 8 compares the baseline projection estimator for Singles with the corresponding BPP-
C estimator, which uses ∆ logY i,t+2 as the single instrument for estimating the pass-through
28

Figure 8: MPC by cash-on-hand: OLS-LP versus BPP
Notes:Estimates show lower bounds of the MPC for Singles, and are computed within decile bins
of lagged normalized cash-on-hand; the horizontal axis plots the observation-count-weighted average
normalized cash-on-hand in each bin. OLS-LP uses the Kalman-smoothed transitory shock. BPP-
C uses the distant future-income-growth instrument. Shaded regions show 95 percent confidence
intervals based on bootstrap standard errors clustered at the household level.
coefficient under the MA(1) baseline. We only show it for the Singles sample as the bootstrap-
ping is computationally very time-consuming for the estimator, the corresponding graph for
households without bootstrapped standard errors is shown in Appendix F. This estimator is
designed to be robust to income measurement error, but it uses a weaker income signal. Con-
sistent with Proposition 4, the IV profile is much less precise—the standard errors span the
entire range of the y-axis–and we cannot reject a flat profile. The large standard errors reflect
the weak identifying covariance underlying the BPP-C estimator. With an MA(1) transitory
income process, the distant-lead covariance used by BPP-C is proportional to the persistence
parameterθ 1, which is only about 0.22 in our sample. 8
5.6 Comparison to previous estimates
Our baseline (Singles sample) average estimated MPC (nondurable MPC) lower and upper
bounds are about 0.47 (0.32) and 0.58 (0.39); in the Households sample, the corresponding
8Asθ 1 approaches zero, both the numerator and denominator of the covariance-ratio estimator are dom-
inated by sampling variation; in the zero-persistence limit, the estimator behaves like a ratio of zero-mean
normal variables and has Cauchy-like heavy tails with no finite mean.
29

bounds are about 0.54 (0.36) and 0.66 (0.44). The average nondurable MPC estimates are
above older estimates on PSID data using semi-structural methods (e.g. Blundell et al. (2008)),
but in line with Commault (2022), who reports an MPC of 0.32. The total expenditure MPC
estimates are also in line with semi-structural estimates from administrative data, such as
Crawley and Kuchler (2023), which reports an annual MPC of 0.64. They are on the lower
end compared to the literature on tax rebates; Johnson et al. (2006) estimate that households
spent about two-thirds of the tax rebate within two quarters, while Parker et al. (2013) find
even larger total expenditure responses to the 2008 stimulus payments once durable purchases
are included.
The distinctive feature of our estimates is the steepness of the cash-on-hand gradient.
Qualitatively, this is consistent with the broader evidence that liquid resources are central
for consumption smoothing. However, the gradient here is steeper compared to many papers,
including both older survey-based estimates (Johnson et al., 2006; Parker et al., 2013) and
more recent papers using special income shocks and experimental designs (Fuster et al., 2021;
Fagereng et al., 2021; Boehm et al., 2025). Our estimates are more similar to Crawley and
Kuchler (2023), who find a strong negative relationship between liquid wealth and the total
expenditure MPC in Danish administrative data, and Ganong et al. (2025), who find that
consumption smoothing of typical labor-income shocks improves sharply with liquid wealth in
US transaction data. In numbers: the lower-bound MPC estimates in our data fall by about
0.37 from the first to the last cash-on-hand decile in the baseline sample, which is very close
to the fall in Ganong et al. (2025) across liquid-wealth deciles, and somewhat smaller than
the 0.48 decline across liquid-wealth quintiles in Crawley and Kuchler (2023).
The pattern with a flatter gradient in studies using special income shocks and experimental
designs suggests that the source of income variation may matter for how households respond.
Ordinary earnings fluctuations are part of the income risk that households routinely face, so
households with substantial liquid resources may be able to smooth them more effectively.
Special payments (lottery wins, tax rebates), by contrast, are typically positive, salient, some-
times large, and often tied to unusual timing or design features; they may also trigger durable
purchases to a larger extent and be tied to specific behavioral spending channels (especially
for lottery winnings). These features can raise spending responses among liquid or affluent
households and thereby flatten the estimated gradient by liquid resources, as suggested by
the role of new vehicles in Misra and Surico (2014) and the transfer-design effects in Boehm
et al. (2025). This interpretation is necessarily cautious, since the studies also differ in their
horizons, consumption concepts, shock sizes, and wealth definitions.
30

6 Conclusion
This paper develops a semi-structural method for estimating state-dependent MPCs in admin-
istrative data with precisely measured income histories. We derive a pass-through equation
from a canonical buffer-stock model, show how transitory-shock pass-through bounds the
MPC conditional on household state variables, and estimate the relevant income shocks using
a Kalman smoother. Under negligible income measurement error, this estimator is identi-
fied and has minimum variance within the class of consistent estimators that are linear in
household income histories, including BPP-style estimators.
Applying the method to Swedish administrative data, we find a steep negative MPC gradi-
ent with respect to cash-on-hand normalized by permanent income. The average yearly MPC
is high, around one half, but the response is much larger among households with little cash-
on-hand than among households at the top of the distribution: in the baseline Singles sample,
the lower bound falls from about 0.68 in the bottom decile to about 0.31 in the top decile. The
pattern is similar for the broader household sample and robust to richer income-process spec-
ifications. This suggests that liquidity is an important determinant of consumption responses
to ordinary income risk.
References
Manuel Arellano, Richard Blundell, and St´ ephane Bonhomme. Earnings and consump-
tion dynamics: A nonlinear panel data framework.Econometrica, 85(3):693–734, 2017.
doi: https://doi.org/10.3982/ECTA13795. URLhttps://onlinelibrary.wiley.com/
doi/abs/10.3982/ECTA13795.
Adrien Auclert. HANK: A new core of usable macroeconomics.AEA Papers and Proceed-
ings, 115:153–157, 2025. doi: 10.1257/pandp.20251114. URLhttps://www.aeaweb.org/
articles?id=10.1257/pandp.20251114.
Christian Bayer, Ralph Luetticke, Lien Pham-Dao, and Volker Tjaden. Precautionary sav-
ings, illiquid assets, and the aggregate consequences of shocks to household income risk.
Econometrica, 87(1):255–290, 2019. doi: 10.3982/ECTA13601. URLhttps://doi.org/
10.3982/ECTA13601.
Florin O. Bilbiie, Sigurd Mølster Galaasen, Refet S. G¨ urkaynak, Mathis Maehlum, and
Krisztina Molnar. HANKSSON. mimeo, University of Cambridge, 2025.
31

Richard Blundell, Luigi Pistaferri, and Ian Preston. Consumption inequality and partial
insurance.American Economic Review, 98(5):1887–1921, December 2008. doi: 10.1257/
aer.98.5.1887. URLhttps://www.aeaweb.org/articles?id=10.1257/aer.98.5.1887.
Richard Blundell, Hamish Low, and Ian Preston. Decomposing changes in income risk using
consumption data.Quantitative Economics, 4(1):1–37, 2013. doi: 10.3982/QE44. URL
https://onlinelibrary.wiley.com/doi/abs/10.3982/QE44.
Johannes Boehm, Etienne Fize, and Xavier Jaravel. Five facts about MPCs: Evidence from
a randomized experiment.American Economic Review, 115:1–42, 2025.
J. Carter Braxton, Kyle Herkenhoff, Jonathan Rothbaum, and Lawrence Schmidt. Changing
income risk across the us skill distribution: Evidence from a generalized kalman filter.
American Economic Review, 115(12):4438–75, December 2025. doi: 10.1257/aer.20231656.
URLhttps://www.aeaweb.org/articles?id=10.1257/aer.20231656.
Martin Browning and Søren Leth-Petersen. Imputing consumption from income and wealth
information.Economic Journal, 113(488):F282–F301, 2003.
Christopher D. Carroll. Buffer-stock saving and the life cycle/permanent income hypothesis.
Quarterly Journal of Economics, 112(1):1–55, 1997.
Jeanne Commault. Does consumption respond to transitory shocks? reconciling natural
experiments and semistructural methods.American Economic Journal: Macroeconomics,
14:96–122, 2022.
Edmund Crawley and Andreas Kuchler. Consumption heterogeneity: Micro drivers and macro
implications.American Economic Journal: Macroeconomics, 15:314–341, 2023.
Angus Deaton. Saving and liquidity constraints.Econometrica, 59(5):1221–1248, 1991.
Marco Di Maggio, Amir Kermani, and Kaveh Majlesi. Stock market returns and consumption.
Journal of Finance, 75(6):3175–3219, 2020. doi: 10.1111/jofi.12968.
Andreas Fagereng, Martin B. Holm, and Gisle J. Natvik. Mpc heterogeneity and household
balance sheets.American Economic Journal: Macroeconomics, 13(4):1–54, October 2021.
Andreas Fagereng, Helene Onshuus, and Kjersti N. Torstensen. The consumption expenditure
response to unemployment: Evidence from norwegian households.Journal of Monetary
Economics, 146, 2024.
32

Martin Flod´ en, Matilda Kilstr¨ om, J´ osef Sigurdsson, and Roine Vestman. Household debt and
monetary policy: Revealing the cash-flow channel.Economic Journal, 131(636):1742–1771,
2021. doi: 10.1093/ej/ueaa135.
Milton Friedman.A Theory of the Consumption Function. Princeton University
Press, Princeton, NJ, 1957. URLhttps://www.nber.org/books-and-chapters/
theory-consumption-function.
Andreas Fuster, Greg Kaplan, and Basit Zafar. What would you do with$500? spending
responses to gains, losses, news, and loans.Review of Economic Studies, 88:1760–1795,
2021. doi: 10.1093/restud/rdaa076.
Peter Ganong, Damon Jones, Pascal Noel, Diana Farrell, Fiona Greig, and Chris Wheat.
Liquid wealth and consumption smoothing of typical labor income shocks.Working paper,
2025.
Mikhail Golosov, Michael Graber, Magne Mogstad, and David Novgorodsky. How americans
respond to idiosyncratic and exogenous changes in household wealth and unearned income.
Quarterly Journal of Economics, 139(2):1321–1395, 2024. doi: 10.1093/qje/qjad053. URL
https://doi.org/10.1093/qje/qjad053.
Fatih Guvenen, Fatih Karahan, Serdar Ozkan, and Jae Song. What do data on millions of u.s.
workers reveal about lifecycle earnings dynamics?Econometrica, 89(5):2303–2339, 2021.
doi: 10.3982/ECTA14603. URLhttps://doi.org/10.3982/ECTA14603.
Robert E. Hall. Stochastic implications of the life cycle-permanent income hypothesis: Theory
and evidence.Journal of Political Economy, 86(6):971–987, 1978. doi: 10.1086/260724. URL
https://doi.org/10.1086/260724.
David S. Johnson, Jonathan A. Parker, and Nicholas S. Souleles. Household expenditure and
the income tax rebates of 2001.American Economic Review, 96(5):1589–1610, December
2006. doi: 10.1257/aer.96.5.1589. URLhttps://www.aeaweb.org/articles?id=10.1257/
aer.96.5.1589.
Greg Kaplan and Giovanni L. Violante. A model of the consumption response to fiscal
stimulus payments.Econometrica, 82(4):1199–1239, 2014a. doi: https://doi.org/10.3982/
ECTA10528. URLhttps://onlinelibrary.wiley.com/doi/abs/10.3982/ECTA10528.
33

Greg Kaplan and Giovanni L. Violante. A model of the consumption response to fiscal
stimulus payments.Econometrica, 82(4):1199–1239, 2014b. doi: https://doi.org/10.3982/
ECTA10528.
Greg Kaplan and Giovanni L. Violante. The marginal propensity to consume in
heterogeneous agent models.Annual Review of Economics, 14:747–775, 2022.
doi: 10.1146/annurev-economics-080217-053444. URLhttps://doi.org/10.1146/
annurev-economics-080217-053444.
Jonas Kolsrud, Camille Landais, and Johannes Spinnewijn. The value of registry data for
consumption analysis: An application to health shocks.Journal of Public Economics, 189:
104088, 2020. ISSN 0047-2727.
Dirk Krueger, Fabrizio Perri, Luigi Pistaferri, and Giovanni L. Violante. Cross-sectional
facts for macroeconomists.Review of Economic Dynamics, 13(1):1–14, 2010. doi: 10.
1016/j.red.2009.12.001. URLhttps://www.sciencedirect.com/science/article/pii/
S1094202509000726.
Peter Maxted, David Laibson, and Benjamin Moll. A simple framework for MPCs and MPXs.
Manuscript, December 2025, 2025.
Kanishka Misra and Paolo Surico. Consumption, income changes, and heterogeneity: Evidence
from two fiscal stimulus programs.American Economic Journal: Macroeconomics, 6:84–106,
2014.
Franco Modigliani and Richard Brumberg. Utility analysis and the consumption function:
An interpretation of cross-section data. In Kenneth K. Kurihara, editor,Post-Keynesian
Economics, pages 388–436. Rutgers University Press, New Brunswick, NJ, 1954.
Jonathan A. Parker, Nicholas S. Souleles, David S. Johnson, and Robert McClelland. Con-
sumer spending and the economic stimulus payments of 2008.American Economic Review,
103(6):2530–53, October 2013. doi: 10.1257/aer.103.6.2530. URLhttps://www.aeaweb.
org/articles?id=10.1257/aer.103.6.2530.
Christina Patterson. The matching multiplier and the amplification of recessions.American
Economic Review, 113(4):982–1012, 2023. doi: 10.1257/aer.20210254. URLhttps://www.
aeaweb.org/articles?id=10.1257/aer.20210254.
34

A Proofs for Identification and MPC Bounds
A.1 Pass-Through Equation
Proof of Proposition 1.Fix the predetermined observed state (m i,t−1,s i,t−1). From (8), con-
sumption growth can be written as
∆ logC i,t =η i,t + logc(m i,t,s i,t)−logc(m i,t−1,s i,t−1),
wherem i,t is given by (9) ands i,t is the MA state implied bys i,t−1 and the new transitory
innovationε i,t.
Linearize this expression with respect to (η i,t, εi,t) aroundη i,t =ε i,t = 0. Letν 0 i,t ≡Pk
j=1 θjεi,t−j denote the predetermined transitory component, and let ¯s(si,t−1) denote the
period-tMA state whenε i,t = 0. The derivatives of normalized cash-on-hand at this point are
∂mi,t
∂ηi,t

0
=−(1 +r) (m i,t−1 −c(m i,t−1,s i,t−1)), ∂mi,t
∂εi,t

0
=Y d i,t exp(ν0 i,t),
where the second equality usesθ 0 = 1.
The coefficient on the permanent shock is therefore
λ(mi,t−1,s i,t−1) = 1−(1 +r) (m i,t−1 −c(m i,t−1,s i,t−1)) ∂logc(m i,t,s i,t) ∂mi,t ,
with the derivative evaluated at
(mi,t,s i,t) =

g(mi,t−1,s i,t−1,0, ν0 i,t), ¯s(si,t−1)  .
The coefficient on the transitory shock is
γ(mi,t−1,s i,t−1) =Y d i,t exp(ν0 i,t) ∂logc(m i,t,s i,t) ∂mi,t + ∂logc(m i,t,s i,t) ∂s(1) i,t ,
evaluated at the same point. This gives (10) and (11).
35

A.2 MPC Bound from Pass-Through
Proof of Proposition 2.Let
Ξi,t ≡Y d i,t exp(ν0 i,t) ∂logc(m i,t,s i,t) ∂mi,t ,
with all objects evaluated at the linearization point in Proposition 1. This is the log-consumption
response generated by the cash-on-hand channel of a transitory innovation. By (11),
γ(mi,t−1,s i,t−1) = Ξi,t + ∂logc(m i,t,s i,t) ∂s(1) i,t .(22)
Assumption 2.4 implies
Ξi,t ≤γ(m i,t−1,s i,t−1)≤

1 +
kX
j=1
θj
!
Ξi,t.(23)
It remains to translate Ξ i,t into the MPC. At the linearization point,
Ci,t =P i,tc(mi,t,s i,t), Y i,t =Y d i,tPi,t exp(ν0 i,t).
Hence
Ci,t
Yi,t
Ξi,t = c(mi,t,s i,t) Y d i,t exp(ν0 i,t) Y d i,t exp(ν0 i,t) 1 c(mi,t,s i,t) ∂c(mi,t,s i,t) ∂mi,t = ∂c(mi,t,s i,t) ∂mi,t .(24)
Sincem i,t =M i,t/Pi,t andC i,t =P i,tc(mi,t,s i,t), the last expression in (24) is the MPC with
respect to current cash-on-hand. Multiplying (23) byC i,t/Yi,t and substituting (24) gives
(13).
B State-Space and Kalman Smoother Details
B.1 Setup
We illustrate the Kalman smoother using the baseline MA(1) case. The income process implies
∆ logY i,t =η i,t +ψ 0εi,t +ψ 1εi,t−1 +ψ 2εi,t−2,
36

where
ψ0 = 1, ψ 1 =θ 1 −1, ψ 2 =−θ 1.
The same logic applies for generalk, with income growth having an MA(k+ 1) transitory
component.
Define
αi,t =

 ηi,t εi,t εi,t−1
εi,t−2

 .
Then the MA(1) model can be written as
αi,t =Tα i,t−1 +Ru i,t,u i,t =

ηi,t
εi,t
!
,Var(u i,t) =

σ2 η 0
0σ 2 ε
!
,
and
T=

 0 0 0 0 0 0 0 0 0 1 0 0
0 0 1 0

 , R=

 1 0 0 1 0 0
0 0

 .
The observation equation is
∆ logY i,t =Zα i,t,Z= (1, ψ 0, ψ1, ψ2).
HereZis the 1×4 row vector that maps the state into observed income growth. The matrices
TandRshift lagged transitory shocks through the state vector and inject the new permanent
and transitory innovations.
B.2 Kalman Filter and Smoother Implementation
Given (θ1, σ2 ε , σ2 η), the objects computed by the filter are the one-sided linear prediction of the
state and its prediction-error covariance. Let
bαi,t|s ≡Proj(α i,t |∆ logY i,1:s), P t|s ≡Var(α i,t − bαi,t|s).
37

Under joint normality, bαi,t|s is also the conditional expectationE(α i,t |∆ logY i,1:s). The
one-step-ahead prediction from information throught−1 is
bαi,t|t−1 =T bαi,t−1|t−1, P t|t−1 =T Pt−1|t−1T ′ +RVar(u i,t)R′.(25)
After observing ∆ logY i,t, the filter computes the forecast error, its variance, and the Kalman
gain,
vi,t = ∆ logY i,t −Z bαi,t|t−1, F t =ZP t|t−1Z′,K t =P t|t−1Z′F −1 t .
HereK t is the 4×1 Kalman-gain vector that maps the scalar forecast error into the state
update. The filtered state is then
bαi,t|t = bαi,t|t−1 +K tvi,t, P t|t =P t|t−1 −K tFtK′ t.(26)
Thus the filter uses only current and past income growth. It delivers the best one-sided
estimate of the state at each date, together with the uncertainty in that estimate.
The fixed-interval smoother then works backward fromT i to date 1. Define
Jt =P t|tT ′P −1 t+1|t.
The Rauch–Tung–Striebel recursion computes the two-sided state mean and covariance as
bαi,t|Ti = bαi,t|t +J t
 bαi,t+1|Ti − bαi,t+1|t  ,(27)
Pt|Ti =P t|t +J t

Pt+1|Ti −P t+1|t

J ′ t.(28)
This second pass is what makes future income growth informative about the date-tshock:
observations afterthelp distinguish a persistent permanent innovation from the finite MA
footprint of a transitory innovation.
The recovered shocks used in the second stage are the first two elements of the smoothed
state,
bηi,t =e ′ 1 bαi,t|Ti,bε i,t =e ′ 2 bαi,t|Ti,(29)
wheree 1 ande 2 select the permanent and current transitory innovations fromα i,t. These are
the regressors in Equation (14).
Under joint normality, these smoothed states are conditional expectations. Without nor-
mality, the same algorithm computes the best linear predictions implied by the second mo-
ments of the state-space model.
38

C Minimum-Variance Linear Signal Result
C.1 Setup and Admissible Estimator Class
This appendix states the projection argument behind Propositions 3 and 4. Let
yi = (∆ logY i,1, . . . ,∆ logYi,Ti)′
denote the observed income-growth history for householdi. Fix a datetand letε i,t denote the
latent transitory shock. The permanent-shock component and the state controls are either
included directly in the regression or partialled out. To keep notation compact, write the
remaining pass-through equation as
^∆ logC i,t =γε i,t +e i,t.(30)
The projection signal is
bεi,t ≡Proj(ε i,t |y i).(31)
Writing Σy ≡Var(y i) andc t ≡Cov(y i, εi,t), the projection in (31) is
bεi,t =c ′ tΣ−1 y yi.(32)
The comparison class consists of IV or GMM procedures whose identifying signal is linear
in the income history. For a scalar signalZ i,t =a ′yi, the population IV estimand is
γ(Z) = Cov(Zi,t, ^∆ logC i,t) Cov(Zi,t, εi,t) .(33)
This notation also covers linear GMM procedures. IfZ i,t is a vector of linear income-history
moments andWis the population weighting matrix, the corresponding one-parameter GMM
estimand is the ratio in (33) evaluated at the composite scalar signal
Si,t = Cov(Zi,t, εi,t)′WZ i,t.(34)
Thus, within the admissible class, GMM differs from scalar IV only in the choice of linear
combination of income-history signals.
We maintain that, after conditioning on the state and the permanent-shock component,
ei,t is orthogonal to all such income-history signals.
39

C.2 Identification of the Projection Estimand
Proof of Proposition 3.After partialling out the permanent shock and state controls, the pop-
ulation coefficient onbεi,t is
Cov(bεi,t, ^∆ logC i,t)
Var(bεi,t) .(35)
Using the maintained pass-through equation (30), the coefficient in (35) equals
γ Cov(bεi,t, εi,t) Var(bεi,t) + Cov(bεi,t, ei,t) Var(bεi,t) .(36)
The second term in (36) is zero becausebε i,t is a linear function ofy i and the residual is
orthogonal to admissible income-history signals. The first ratio in (36) is one because the
projection residualε i,t −bεi,t is orthogonal to every linear function ofy i, includingbεi,t. Hence
Cov(bεi,t, εi,t) = Var(bεi,t).
If the permanent shock is omitted, the same calculation gives (20), which is why the
empirical specification includes the recovered permanent-shock component rather than treating
the transitory signal as the only relevant income innovation.
C.3 Minimum-Variance Linear Income-History Signal
Proof of Proposition 4.For any admissible scalar instrumentZ i,t =a ′yi, the standard IV
expansion gives
Avar(bγ0(Z))∝ Var(Zi,t) Cov(Zi,t, εi,t)2 = 1 σ2 ε ρ2(Zi,t, εi,t) .(37)
Thus minimizing asymptotic variance is equivalent to maximizing the squared correlation
betweenZ i,t andε i,t.
ForZ i,t =a ′yi,
ρ2(Zi,t, εi,t) = (a′ct)2
(a′Σya)σ2 ε .
By Cauchy–Schwarz in the inner product induced by Σ y,
(a′ct)2 ≤(a ′Σya)(c′ tΣ−1 y ct),
40

with equality if and only ifais proportional to Σ −1 y ct. Therefore the maximal squared corre-
lation is attained by
Z ∗ i,t =c ′ tΣ−1 y yi =bεi,t.(38)
Substituting (38) into (37) gives (21).
D Measurement Error Simulations
The simulations evaluate the premise that income is measured accurately enough for the
projection estimator to be useful. For this exercise, we assume that transitory income is
MA(1) in levels, as in our baseline sample, and take the income-process parameters from
Table 2 and the estimated consumption-function parameters from Figure 5. The robust BPP-
C estimator therefore uses the two-period-ahead income growth instrument, ∆ logY i,t+2. We
compare BPP-C to a naive linear-projection estimator that ignores income measurement error
when constructing the Kalman-smoothed shock.
We model measurement error in log income as an i.i.d. classical shockξ t, so that observed
income growth contains the MA(1) componentξ t −ξ t−1. The noise share is
Var(ξt −ξ t−1)
Var(∆ logyobs t ) = 2σ2 ξ Var(∆ logyobs t ) .(39)
The scale in (39) is chosen to match the validation evidence. In survey settings such as
the PSID, where income and consumption are collected separately, validation studies by
Bound et al. (1994) and Pischke (1995) imply substantial measurement error in earnings
changes, roughly in the range of 15–20 percent. In Nordic administrative registers, the rele-
vant range is much lower. Kapteyn and Ypma (2007), Meijer et al. (2012), and Kristensen
and Westergaard-Nielsen (2007) point to very accurate register earnings conditional on correct
matching, suggesting that 0–2 percent is the empirically plausible range for population-wide
register applications.
These validation facts motivate two simulation exercises. First, we present a simulation
exercise that mimics survey data, where income and consumption measurement errors are
i.i.d. and independent. The independent-error simulation varies the noise share from 0 to
20 percent, covering the survey range. Second, we present a simulation exercise that mimics
budget-constraint imputation (as in our data), where income measurement error mechanically
enters imputed consumption. The budget-constraint imputation simulation focuses on 0 to 5
percent, because the register concern is not mainly that income error is large. It is that any
41

Figure 9: Bias-variance trade-off with income measurement error
Notes:Each point uses 1,000 simulated samples with 30,421 observations per sample.
remaining income error enters imputed consumption mechanically through the household bud-
get constraint, creating a cross-equation correlation between measurement error in observed
income and observed consumption.
Figure 9 summarizes the simulation results. The figure reports the estimator behavior over
repeated samples as the income-noise share varies. Each point in the figure is based on 1,000
simulated samples with 30,421 observations per sample. It illustrates the bias-variance trade-
off: the projection estimator uses a stronger signal but is exposed to misspecification when
income measurement error is ignored, while BPP-C remains robust but becomes imprecise.
D.1 Independent Measurement Error
The first simulation corresponds to a survey setting in which income and consumption are
measured separately. Observed income growth is contaminated by an i.i.d. income error
42

ξt −ξ t−1, while observed consumption growth has an independent measurement error:
∆ logy obs t =η t +ε t −(1−θ 1)εt−1 −θ 1εt−2 +ξ t −ξ t−1,(40)
∆ logc obs t =λη t +γε t +ζ t −ζ t−1.(41)
The BPP-C estimator remains centered onγbecause the two-period-ahead instrument is not
contaminated by the contemporaneous MA(1) measurement-error term. The cost is precision:
as the noise share rises, the transitory-shock variance consistent with the observed income
moments falls, weakening the long-horizon first stage. The naive projection estimator is in-
stead attenuated toward zero because income measurement error inflates the variance of the
recovered transitory signal without creating a corresponding covariance with consumption
growth.
D.2 Budget-Constraint Imputation
We impute consumption from income and wealth using the household budget constraint. This
means that any measurement error in income enters observed consumption mechanically:
∆ logc obs t =λη t +γε t +ζ t −ζ t−1 +ξ t −ξ t−1.(42)
The sameξ t therefore appears in both observed income growth (40) and observed consumption
growth (42). BPP-C remains robust because the contamination is concentrated at short lags.
The naive projection estimator now faces two forces. The contaminated income history still
attenuates the recovered shock, but the same contamination also enters imputed consumption
and raises the numerator of the pass-through regression. In the simulation, the second force
dominates over the register-relevant range, so the naive projection estimator overstatesγas
the income noise share rises.
E Data Appendix
E.1 Register Sources and Linkages
The longitudinal dataset LISA (Longitudinal Integrations Database for Sickness Insurance and
Labour Market Studies) is provided by Statistics Sweden and merges several administrative
and tax registers for the universe of Swedish individuals aged 16 and above. LISA contains
43

annual information on labor earnings, capital income, transfers, taxes, and socio-demographic
variables such as age, education, occupation, marital status, and municipality of residence.
We link LISA to complementary asset registers. The wealth register (F¨ orm¨ ogenhetsreg-
istret) covers the period 1999–2007, when Sweden levied a comprehensive wealth tax and the
tax administration collected balance-sheet information for the entire population. It reports
end-of-year balance values for financial assets, listed securities, real estate, and liabilities. On
the asset side, it provides aggregate positions by instrument, such as bank deposits, bonds,
equities, and mutual funds. On the liability side, it includes total outstanding debt, including
mortgages, consumer credit, and student loans. Financial institutions were legally required to
report this information directly to the tax authority for the administration of the wealth tax.
The KURU register provides more disaggregated security-level information. It records
holdings by International Securities Identification Number (ISIN), including the quantity held
for securities that Statistics Sweden can match to a market price. Housing registers include
Fastighetsprisstatistiken, which records transaction prices for owned real estate, and KU55,
which records co-operative-apartment transactions. These sources are merged to the individual
and household level using personal identification numbers and dwelling identifiers.
E.2 Consumption Imputation
We impute consumption from the household budget constraint,
Ci,t =Y i,t −S i,t,(43)
whereC i,t is consumption,Y i,t is disposable income, andS i,t is savings. To construct our
measure of disposable income, we start from the LISA measure of income, which includes
employment-related earnings, including wages, vacation pay, severance payments, and wage
income for self-employed workers and business owners as well as capital income. Business losses
for small business owners and independent contractors are included from 2004 onward. We
add government transfers, including unemployment benefits, sickness and disability benefits,
pension benefits, housing benefits, child benefits, and smaller transfer programs, and deduct
all taxes. We subtract the change in cumulative student debt, since these are automatic
payments, and capital income, since it is endogenous to the consumption–savings decision and
would make identification of transitory shocks problematic. Our final measure of disposable
income is the same as in Kolsrud et al. (2020), except that our subtraction of capital income
is based on the summary measure “kapinc”, net of taxes, whereas they use the gross value of
44

the more narrow measure “KIRANTA”, which does not include capital gains.
Conceptually, savings should captureactiverebalancing—net purchases of assets and net
debt repayment—and should not mechanically reflectpassivechanges in wealth due to asset
price movements. This distinction matters because the registers typically report end-of-year
positions, sometimes in quantities and sometimes only in values, while transactions and intra-
year trading are not directly observed. We therefore use two complementary approaches.
Quantity approach.When end-of-year holdings are observed in quantitiesA i,k,t for asset
kand a corresponding market pricep k,t is available, net purchases are
SQ i,k,t =p k,t (Ai,k,t −A i,k,t−1).
An increase in holdings during yeartis treated as saving and therefore reduces imputed
consumption, whereas a reduction in holdings is treated as dissaving and increases imputed
consumption. If the household holds the same quantity over the year,S Q i,k,t = 0 even when
prices move. The main limitation is that quantities are observed only at the end of the year, so
this approach values the net annual change in holdings at the end-of-year price and abstracts
from the timing of trades within the year.
Price approach.When only balance valuesW i,k,t =p k,tAi,k,t are observed, or asset-specific
prices are unavailable, we infer net purchases by subtracting passive valuation changes:
SP i,k,t = ∆Wi,k,t − ∆pk,t pk,t−1 Wi,k,t−1.
Here ∆X t ≡X t −X t−1. The term (∆p k,t/pk,t−1)Wi,k,t−1 is the change in wealth that would
arise purely from applying the asset price movement to last year’s position. The residualS P i,k,t
is interpreted as the household’s net purchase flow. If an asset-specific price is unavailable, we
use a category-level price index as in Kolsrud et al. (2020). When quantities and prices are
observed consistently for the same security, the two approaches are algebraically equivalent;
in practice they differ because some holdings are observed only in aggregates or prices are not
matchable at the relevant level of detail.
Financial assets.Fixed-price instruments, such as bank accounts, money-market funds,
and similar products, enter through changes in reported end-of-year balances. For bank ac-
counts, consumption out of these assets is inferred from balance changes between yearst−1
45

andt, together with interest income on deposits, which is already included in the income
measure. Liabilities are treated analogously: changes in outstanding debt, net of interest pay-
ments that are already part of the income measure, are interpreted as consumption financed
through borrowing or saving through debt repayment.
For stocks, bonds, and mutual funds, we supplement the wealth register with KURU.
Swedish financial institutions must report each client’s ISIN-level holdings and the quantity
held. Statistics Sweden registers securities for which it can match a market price, so the
register omits non-listed assets such as private business equity or shares in closely held, non-
traded companies. Existing evidence, see Bach et al. (2020), suggests that such unlisted
securities are negligible for the vast majority of households in Sweden and only represent a
substantial share of wealth for a very small fraction of the population at the absolute top of
the wealth distribution. For listed financial instruments, we use closing prices from LSEG
Refinitiv Eikon Datastream on the last trading day of December. Datastream covers a broad
set of instruments across major asset classes, including active and delisted exchange-traded
instruments. For securities in KURU that cannot be matched to a price, we use the price
approach with an aggregate price index.
For options, warrants, and tax-favoured capital-insurance accounts, we observe the total
balance rather than quantities. We therefore apply a price-based method with an aggregate
price index to impute the associated consumption flows. For tax-deferred private pension
accounts, we observe contributions and withdrawals but not the underlying balance. Since
the object of interest is the consumption flow, these inflows and outflows are sufficient to
construct the relevant series.
For the stock of total financial wealth, we use the maximum of financial wealth extracted
from Datastream and financial wealth in the wealth register. This uses the most accurate
source for each individual, as it minimizes the problem of omitting the value of instruments
whose value was missing in the wealth registry. Datastream financial wealth is substantially
larger than wealth-register financial wealth, mostly because Datastream covers foreign-traded
stocks and other instruments that Statistics Sweden did not fully value in the wealth register.
The difference is concentrated among wealthy individuals; after trimming the top one percent
by financial wealth, Datastream financial wealth remains roughly twice as large as the wealth-
register measure. The stock of total financial wealth is used to stratify the population in
heterogeneity analysis, not to impute consumption.
Real assets.We separate real assets into owned real estate and co-operative apartments.
Owned real estate includes stand-alone houses, semi-detached houses, bungalows, terrace
46

houses, second homes, commercial real estate, apartment buildings, industrial plants, and
farming properties. Co-operative apartments are treated separately because Swedish apart-
ment residents commonly buy a share in a housing co-operative rather than legally owning
the property itself.
For owned real estate, we use Fastighetsprisstatistiken to observe acquisitions and sales
and classify transactions into primary housing, second homes, farms, and commercial real
estate. LetK H i,t denote acquisitions andS H i,t sales. The real-estate saving flow entering the
budget constraint is
∆Hi,t =K H i,t −S H i,t,
so net purchases reduce imputed consumption and net sales increase it. The implementation
differs by period because registry detail changes. For 2004 onward, all parties involved in
each transfer are observed, so transaction values can be assigned at the individual level using
party-level participation. For 2000–2003, party information is more limited, so household-
level transaction values are allocated using ownership shares from the wealth register, using
contemporaneous shares on the purchase side and lagged shares on the sale side.
For co-operative apartments, KU55 records sales with transferred shares and sale values,
which we use to construct individual-level sale proceeds. These are combined with housing
flows to construct a co-op-adjusted housing flow from 2004 onward. For 2005–2007, we ad-
ditionally impute missing co-op purchase values for individuals with persistent positive co-op
wealth in adjacent years. The imputation has two steps. First, we estimate a purchase-
probability model using household demographics, disposable income, changes in household
size, debt and co-op wealth changes, year effects, age-bin controls, regional controls, and in-
dicators for related housing transactions. Second, conditional on observables, we estimate
expected purchase prices and form an imputed co-op flow as the difference between observed
sale values and predicted purchase values for individuals with sufficiently high predicted pur-
chase probability. The imputed flow is scaled by observed ownership shares and merged back
to the person-year panel.
We also account for housing services through imputed rents. Following the approach used
by Statistics Sweden for national accounts, imputed rent is based on potential rental income
from subletting the house, computed as square-metre living space multiplied by a square-metre
rental value that varies by region, construction period, and dwelling category. Since individual
imputed rents are not observed in our data, we assign aggregate imputed rents to households
based on the value of their primary real estate in the wealth tax register.
47

Figure 10: Registry consumption, national accounts, and household budget survey (HUT)
Notes:The figure reports per-capita consumption. All series are in 2003 SEK.
E.3 Consumption Validation
Figure 10 compares our registry-based per-capita consumption measure to the national-accounts
series and the Household Budget Survey (HUT). The national-accounts series is obtained by
taking nominal household consumption expenditure under ESA2010, in current SEK millions
by durability and year, and dividing by the number of individuals in MONA. The HUT series
is obtained by dividing household consumption by household size and weighting observations
by survey weights. All series are expressed in 2003 SEK.
The registry measure lies between the survey and national-accounts series throughout the
sample period. The survey provides direct measures of bi-weekly consumption expenditures at
the time the household is surveyed. In the national accounts, consumption is computed from
several sources, including HUT survey information, registry information, and V AT receipts.
A main difference relative to the national accounts is that some investments are treated as
expenditures in our measure and as investment in the national accounts. In contrast with
survey data, both the national accounts and the registry measure include imputed rents. The
three series are therefore broadly comparable in levels over the sample period.
48

E.4 Income and Wealth Variables
Disposable income (Y i,t).Annual disposable income sums labor earnings and government
transfers, net of taxes. Labor earnings include wages, vacation pay, severance payments,
and wage income for self-employed workers and business owners. For the income measure
used in the income shocks estimation, we subtract capital income because it is endogenous to
consumption and saving decisions.
Consumption (C i,t).Registry consumption is imputed from Equation (43) using the sav-
ings flows described above.
Liquid wealth (Aliq i,t ).Liquid wealth is financial wealth plus checking-account balances plus
capital-insurance wealth.
Net illiquid wealth (A illiq i,t ).Net illiquid wealth is real estate assets minus total debt and
cumulative student debt.
Net total wealth (Anet i,t ).Net total wealth is financial wealth plus checking-account balances
plus capital-insurance wealth plus real estate assets, minus total debt and cumulative student
debt:
Anet i,t =A fin i,t +A checking i,t +A capins i,t +A real i,t −Debt i,t −StudentDebt i,t.
Cash-on-hand (M i,t).Cash-on-hand at the start of yeartis
Mi,t = (1 +r)A liq i,t +Y i,t.
The term (1 +r)A liq i,t is the end-of-year-t−1 liquid-asset position observed in the registers;
returns overt−1 are already embedded in this stock, so the interest rateris not observed or
imputed separately.
Normalized cash-on-hand (mi,t).Normalized cash-on-hand divides cash-on-hand by smoothed
permanent income:
mi,t = Mi,t
Pi,t
,
whereP i,t is the permanent-income component recovered from the estimated income process.
49

E.5 Sample Construction and Restrictions
The imputation of consumption is carried out on the full population. For the main analysis,
we restrict the sample to individuals aged 30–65 with non-missing income, consumption, and
wealth data. We drop observations with non-positive imputed consumption. We also exclude
observations with extreme income or consumption growth rates.
Singles (baseline).The baselineSinglessample comprises one-person households, exclud-
ing married or registered-partner cases, that satisfy the age and data-quality restrictions above.
Households.TheHouseholdssample includes household heads, defined as the highest-
income earner, in stable household structures. Income, consumption, and wealth are ag-
gregated to the household level.
Housing and co-operative-apartment exclusions.For both subsamples, we exclude
observations involved in housing or co-operative-apartment transactions before estimating
Equation (14). This restriction aligns the sample with the identifying restriction in the main
text by focusing on periods without active illiquid-asset adjustment.
Detrended growth rates.For estimation, we prepare balanced lead-lag moments and de-
trended growth components. We residualize log income and log consumption using flexible
controls: time effects, cohort, family composition, employment status, education-time inter-
actions, region effects, and lagged controls. The corresponding growth rates are then built
from first differences and enter the income-process estimation and the second-stage MPC
regressions.
F Additional Results and Robustness
F.1 Household and MA(2) Income-Process Estimates
Table 3 reports the MA(2) income-process estimates used in the robustness exercises. The
estimated second MA parameter is small relative to the first:θ 2 = 0.0694 for Singles andθ 2 =
0.0642 for Households. The income-growth autocovariance at the third lead is correspondingly
small. The MA(2) specification therefore allows a richer transitory-income footprint, but it
does not point to a fundamentally different income process.
50

Table 3: MA(2) income-process moments and parameter estimates
A. Singles: moments
∆ lnyt ∆ lnyt+1 ∆ lnyt+2 ∆ lnyt+3
∆ lnyt
0.0297
(0.0295, 0.0299)
-0.0072
(-0.0073, -0.0070)
-0.0026
(-0.0027, -0.0025)
-0.0009
(-0.0010, -0.0008)
∆ct
0.0214
(0.0212, 0.0216)
-0.0035
(-0.0037, -0.0034)
-0.0023
(-0.0024, -0.0021)
-0.0006
(-0.0008, -0.0005)
N1,155,414
B. Singles: parameters
θ1 θ2 σ2 ϵ σ2 η
Estimate
0.3056
(0.2982, 0.3130)
0.0694
(0.0636, 0.0751)
0.0142
(0.0140, 0.0145)
0.0077
(0.0074, 0.0080)
N1,155,414
C. Households: moments
∆ lnyt ∆ lnyt+1 ∆ lnyt+2 ∆ lnyt+3
∆ lnyt
0.0288
(0.0286, 0.0289)
-0.0069
(-0.0070, -0.0069)
-0.0026
(-0.0027, -0.0026)
-0.0008
(-0.0009, -0.0008)
∆ct
0.0218
(0.0216, 0.0219)
-0.0036
(-0.0037, -0.0035)
-0.0024
(-0.0025, -0.0023)
-0.0006
(-0.0007, -0.0005)
N2,150,175
D. Households: parameters
θ1 θ2 σ2 ϵ σ2 η
Estimate
0.3041
(0.2988, 0.3094)
0.0642
(0.0601, 0.0683)
0.0137
(0.0136, 0.0139)
0.0076
(0.0074, 0.0078)
N2,150,175
F.2 MA(2) MPC Profiles
Under MA(2), the state is (m i,t−1, εi,t−1, εi,t−2). We partition observations into a 10×5×2
grid and average across the two lagged-shock dimensions to obtain cash-on-hand decile pro-
files. Figure 11 shows that the MA(2) estimates preserve the main result. The projection
estimates decline sharply with cash-on-hand in both samples, and the future-income IV es-
timates remain substantially less precise. For the BPP-C estimates in this figure, we report
(incorrect) non-bootstrap confidence intervals because bootstrapping the full MA(2) BPP-C
estimation procedure is computationally very demanding.
F.3 Pass-Through Profiles
Figure 12 reports the estimated MA(2) pass-through coefficients before the MPC conversion,
corresponding to the baseline MA(1) profiles in Figure 5. The transitory pass-through remains
downward sloping in cash-on-hand for both Singles and Households, while the permanent-
shock pass-through is comparatively flat. Thus the richer income-process specification pre-
serves the pass-through pattern that generates the MPC gradient.
F.4 Comparison to BPP-C with bias-correction
This final comparison asks how much precision is lost by imposing the robust BPP-C lead
restriction relative to a near-lead restriction. For a future-income horizonh, define the future-
income instrument and the IV estimator as
Zi,t(h) = ∆ logY i,t+h, γ IV (h) = Cov(Zi,t(h),∆ logC i,t) Cov(Zi,t(h),∆ logY i,t) .
51

Figure 11: MPC by cash-on-hand, MA(2)
Notes:Estimates show lower bounds of the MPC, and are computed within decile bins of lagged nor-
malized cash-on-hand; the horizontal axis plots the observation-count-weighted average normalized
cash-on-hand in each bin. The projection estimator uses the Kalman-smoothed transitory shock and
reports 95 percent confidence intervals based on bootstrap standard errors clustered at the household
level. BPP-C uses the distant future-income-growth instrument and reports the (incorrect) conven-
tional non-bootstrap confidence intervals because bootstrapping the full MA(2) BPP-C estimation
procedure is computationally very demanding.
With an MA(k) transitory income component, the BPP-C restriction uses the distant lead
h=k+ 1:h= 2 under MA(1) andh= 3 under MA(2). This lead filters out the permanent
shock and the lagged transitory shocks that may enter consumption growth, which makes
it robust to misspecification of the consumption equation. The cost is that the identifying
covariance is proportional to the last MA coefficient, so the instrument becomes weak when
transitory persistence is modest.
A shorter lead is more precise but is mechanically biased under the MA income process.
However, this bias can be corrected knowing the parameters of the income process. Under
the baseline MA(1) process and the state-conditioned pass-through equation used in the main
text,
plimγ IV (1) = γ0
1−θ 1
.
and thus the bias-corrected estimate is
bγIV,1,bc 0 = (1− bθ1)bγIV (1).
For the MA(2) robustness specification, Figure 13 reports the one-lead bias-corrected estimate.
52

Figure 12: Pass-through by cash-on-hand, MA(2)
Notes:Columns report Singles and Households; rows report permanent- and transitory-shock pass-
through coefficients from the OLS projection estimator. Estimates are computed within decile bins
of lagged normalized cash-on-hand; the horizontal axis plots the observation-count-weighted average
normalized cash-on-hand in each bin. Shaded regions show 95 percent confidence intervals based on
bootstrap standard errors clustered at the household level.
The correction multiplies the one-lead estimate byB 1(bθ1, bθ2)/(1− bθ1), whereB 1(θ1, θ2)≡
−Cov(∆ logY i,t+1,∆ logY i,t)/Var(ε i,t).
This bias correction is not a generic replacement for BPP-C. It relies on a correctly spec-
ified state-conditioned consumption equation: lagged transitory shocks must be included in
the predetermined state rather than enter the omitted part of consumption growth. It also
relies on negligible income measurement error. With classical measurement error in income,
the near-lead covariance contains an additional noise term, and the same scalar correction no
longer recoversγ 0 unless that noise variance is known. Figure 13 should therefore be read as a
comparison between the precise, bias-corrected near-lead instrument under these maintained
assumptions and the more robust but weaker distant-lead BPP-C instrument. We use (incor-
rect) standard asymptotic confidence intervals in this comparison because bootstrapping the
full set of near- and distant-lead BPP-C estimates is computationally very demanding.
53

Figure 13: Near- versus distant-lead future-income IV estimates
Notes:Estimates show lower bounds of the MPC, and are computed within decile bins of lagged
normalized cash-on-hand; the horizontal axis plots the observation-count-weighted average normalized
cash-on-hand in each bin. The near-lead instrument applies the analytical bias correction under the
state-conditioned pass-through equation, using the +1 lead in both MA(1) and MA(2). The distant-
lead instrument follows the robust BPP-C restriction, using the +2 lead under MA(1) and the +3 lead
under MA(2). Shaded regions use (incorrect) standard asymptotic confidence intervals for all gradients
because bootstrapping the full set of near- and distant-lead BPP-C estimates is computationally very
demanding.
Appendix References
Laurent Bach, Laurent E Calvet, and Paolo Sodini. Rich pickings? risk, return, and skill
in household wealth.American Economic Review, 110:2703–2747, 2020. doi: 10.2307/
26966314. URLhttps://www.jstor.org/stable/10.2307/26966314.
John Bound, Charles Brown, Greg J Duncan, and Willard L Rodgers. Evidence on the
validity of cross-sectional and longitudinal labor market data.Journal of Labor Economics,
12:345–368, 1994.
Arie Kapteyn and Jelmer Y. Ypma. Measurement error and misclassification: A comparison
of survey and administrative data.Journal of Labor Economics, 25(3):513–551, 2007. doi:
10.1086/513298. URLhttps://doi.org/10.1086/513298.
54

Jonas Kolsrud, Camille Landais, and Johannes Spinnewijn. The value of registry data for
consumption analysis: An application to health shocks.Journal of Public Economics, 189:
104088, 2020. ISSN 0047-2727.
Nicolai Kristensen and Niels Westergaard-Nielsen. A large-scale validation study of measure-
ment errors in longitudinal survey data.Journal of Economic and Social Measurement, 32:
65–92, 2007.
Erik Meijer, Susann Rohwedder, and Tom Wansbeek. Measurement error in earnings data:
Using a mixture model approach to combine survey and register data.Journal of Business
& Economic Statistics, 30(2):191–201, 2012. doi: 10.1198/jbes.2011.08166. URLhttps:
//pmc.ncbi.nlm.nih.gov/articles/PMC3604906/.
J¨ orn-Steffen Pischke. Measurement error and earnings dynamics: Some estimates from the
psid validation study.Journal of Business & Economic Statistics, 13(3):305–314, 1995. doi:
10.1080/07350015.1995.10524599. URLhttps://www.jstor.org/stable/1392190.
55
