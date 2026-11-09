---
title: Automation, Income Incidence, and Capital Accumulation in Incomplete Markets
url: https://arxiv.org/abs/2605.05127
category: consumer-behavior
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Erhan Bayraktar
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.05127
pages: 50
chars: 112846
fetched_at: '2026-11-08T13:04:32+00:00'
kb_version: 1
---

# Automation, Income Incidence, and Capital Accumulation in Incomplete Markets

Automation, Income Incidence, and Capital Accumulation in
Incomplete Markets
Erhan Bayraktar∗
July 2026
Abstract
This paper studies how automation changes the stationary distribution of income, consump-
tion, and wealth in an incomplete-market economy. An automating sector trades off productivity
gains and labor-cost savings against adoption costs. Households differ by skill and wealth, save
in a capital/equity claim, and face uninsurable skill risk. Competitive factor prices and aggregate
capital clear jointly with household Hamilton–Jacobi–Bellman equations and the stationary
Kolmogorov forward equation. Automation affects consumption through labor-income incidence,
precautionary saving, skill mobility, ownership of automation rents, and the stationary capital
stock. In an adverse-incidence scenario with high exposure, adverse reskilling, capital obsoles-
cence, and concentrated ownership, decentralized automation lowers stationary consumption and
capital relative to the no-automation allocation. With stronger productivity and complementarity,
lower obsolescence, and broader ownership, automation raises output, consumption, and capital.
Reversing the assumed skill-mobility response also raises consumption, output, and capital
substantially at a fixed automation intensity. A proxy diagnostic combining U.S. evidence on AI
adoption, investment, labor-income pass-through, equity ownership, and marginal propensities
to consume places the current economy near the boundary between the two scenarios. The
model provides a quantitative framework for separating automation’s aggregate gains from its
distributional incidence.
Keywords.Artificial intelligence; automation; heterogeneous agents; incomplete markets; station-
ary equilibrium; capital accumulation; income incidence; ownership.
AMS subject classifications (2020).91B50; 91B40; 91B70; 91A13; 91A15; 49L20; 35Q91;
65M06.
JEL classifications.C63; D31; E21; E24; E27; E60; H21; J23; J24; O33.
1 Introduction
Automation affects more than production. It changes who receives labor income, who owns the
resulting rents, and how much households save. In an incomplete-market economy those changes
alter the stationary wealth distribution, the capital stock, and factor prices. This paper asks when
productivity, task exposure, skill mobility, capital obsolescence, and rent ownership combine to raise
or lower stationary consumption and capital.
∗Department of Mathematics, University of Michigan. Email: erhan@umich.edu. Supported in part by the National
Science Foundation.
1
arXiv:2605.05127v2  [econ.GN]  31 Jul 2026

The mechanism is an income-incidence channel in a real, flexible-price general equilibrium.
Automation changes the allocation of output among consumption, replacement investment, adoption
costs, and claims accruing outside the household sector. Labor-income risk and rent ownership then
shape household consumption and saving:
automation =⇒labor income, skill risk, and rent ownership
=⇒household consumption and saving policies
=⇒stationary wealth, capital, and factor prices.
The model combines an automating sector with a continuous-time incomplete-market household
block. Households differ by wealth and by a two-state skill process. They choose consumption and
saving, and their invariant distribution solves a KFE. A competitive final-good firm determines
wages and the productive-capital return. Automation also generates rents; the share passed through
to domestic asset holders determines the gap between the productive-capital return and the return
received by households. The stationary equilibrium is computed by resolving the HJB–KFE and
market-clearing system for each automation intensity.
The first contribution is to connect the task-based automation literature to heterogeneous-
agent capital accumulation. Automation displaces some paid tasks and complements others, as
in Acemoglu and Restrepo [2018, 2019, 2020b,a]. In Bewley–Huggett–Aiyagari economies, income
risk and incomplete insurance determine saving and capital [Bewley, 1986, Huggett, 1993, Aiyagari,
1994]. Here the automation technology changes both the level and composition of labor income, so
the stationary distribution becomes part of the incidence calculation. The ownership channel adds
a second margin: households may lose labor income yet gain through claims on productive capital
and automation rents.
In incomplete-market economies, pecuniary price effects can generate constrained inefficiency
when they interact with missing markets or financial constraints. Establishing such inefficiency
requires a welfare and feasibility benchmark of the kind developed by Geanakoplos and Polemarchakis
[1986] and D´ avila and Korinek [2018]. The present analysis instead characterizes the incidence of
automation across stationary competitive equilibria.
The second contribution is a transparent decomposition of two scenario families. Theadverse-
incidencescenario combines high low-skill exposure, automation-induced obsolescence, adverse
reskilling, and concentrated ownership. Theproductivity-led capital-growthscenario combines
stronger productivity and high-skill complementarity with lower obsolescence and exposure. These
are comparative-static scenarios, not two structural estimates. Their role is to show which assump-
tions account for the sign of the stationary consumption and capital responses.
The third contribution is computational. The numerical method follows the continuous-time
HJB–KFE finite-difference approach of Achdou et al. [2022]. The appendix states the finite-grid
equilibrium actually solved, gives sufficient conditions for existence and conditional uniqueness on
that grid, and reports market-clearing and residual checks. The contribution lies in the automation
application, equilibrium decomposition, and reproducible scenario analysis. The empirical extension
then maps the model’s incidence terms into a transparent proxy diagnostic using current U.S. data.
The quantitative exercises use empirical guideposts for the skill wage ratio, AI exposure, and
equity ownership. Automation elasticities governing reskilling and obsolescence remain scenario
parameters, so the analysis reports neutral and reversed skill-mobility cases alongside the adverse-
reskilling baseline. The reported allocations are stationary comparisons. A reduced-form policy
index over consumption and exposed labor income organizes the instrument experiments; it is a
political-economy criterion rather than a household-welfare ordering.
The paper proceeds as follows. Section 2 gives a diagnostic benchmark. Section 3 defines
2

the stationary heterogeneous-agent equilibrium. Section 4 reports the numerical scenarios and
robustness exercises. Section 5 studies tax, rebate, and ownership incidence. Section 6 develops the
empirical regime diagnostic and policy experiment. Section 7 describes the replication code, and
Section 8 concludes. The appendix documents the finite-difference method, finite-grid equilibrium
result, and empirical validation exercises.
2 Diagnostic Benchmark
There is a unit mass of households split into skill groups s∈ {U, H}, where U denotes low-skilled
or unskilled workers and H denotes high-skilled workers. The automation intensity is a∈ [0,¯a].
Automation has three primitive effects. First, it raises Hicks-neutral productivity in the sense of a
multiplicative technology shifter [Hicks, 1932, Acemoglu, 2008],
Z(a) =Z 0 exp(ψZa), ψ Z >0.
Second, it reduces paid low-skill human tasks and complements high-skill paid tasks,
hU (a) = exp(−χU a), h H (a) = exp(βH a),
withχ U >0 andβ H >0. Third, it changes production-task services,
ℓU (a) = exp(−ξU a), ℓ H (a) = exp(ηH a).
The distinction between hs and ℓs is important. The firm pays wages on paid human tasks H, but
production uses total task servicesL, which include automated task services. Define
L(a) =
X
s
msesℓs(a), H(a) =
X
s
mseshs(a).
Output is
Y(a, K) =Z(a)K αL(a)1−α.
The efficiency-unit wage is
w(a, K) = (1−α)Z(a)K αL(a)−α,
and total collective wage bill is
B(a, K) =w(a, K)H(a).
The exposed low-skill collective wage bill is
BU (a, K) =w(a, K)mU eU hU (a).
A representative automating firm choosesafrom
Π(a;K, w) =Z(a)K αL(a)1−α −wH(a)−ϕa− κ 2 a2 −P(a),
where P (a) is a policy payment. Holding ( K, w) fixed, the private marginal benefit of automation is
M(a;K, w) =

ψZ + (1−α) La(a) L(a)  Y(a, K) | {z }
productivity and production-task effect
+w[−H a(a)]| {z }
labor-cost effect
.
3

The private first-order condition is
M(a;K, w)−ϕ−κa−P a(a) = 0.
Let
ι=P a(a)
denote the marginal implementation wedge. A positive ι discourages automation. A negative ι
subsidizes automation.
For comparison, define a reduced-form policy-maker index over stationary household-side out-
comes:
aP ∈arg max
a∈[0,1]
Gµ(a), G µ(a) =λC(a) +µB U (a),
where C(a) is household consumption and BU (a) is labor income received by exposed low-skilled
workers. The parameters λ, µ≥0 are political-economy weights, not household preference parameters.
Accordingly, aP is only the maximizer of this index. It is not a planner allocation, and the ordering
ofa P and the private choice has no efficiency content.
For any interior index target aP , the marginal payment that implements it in the firm’s static
first-order condition is
ι∗ =M(a P ;K, w)−ϕ−κa P .
At a boundary target aP = 0, any tax above the minimal deterrent value ¯τ= M (0; K, w) −ϕ
implements the boundary.
The diagnostic comparison is summarized by the derivative
G′ µ(a) =λC a(a) +µB U,a(a).
When the private residual F (a) = M (a; K, w) −ϕ−κa has a unique root, the sign of this derivative
at that root indicates whether the index continues to rise or has begun to fall. Appendix A.5
decomposes the derivative into low- and high-skill exposure, mobility, productivity, and depreciation
terms. The decomposition organizes the channels before prices, saving, and the wealth distribution
are allowed to adjust.
3 Stationary Heterogeneous-Agent General Equilibrium
3.1 Households
Time is continuous. A unit mass of households has wealth k≥k and skill state s∈ S= {U, H}.
The skill state follows
Q(a) =
−qU H(a)q U H(a)
qHU (a)−q HU (a)

, q U H(a) =q 0e−ζa, q HU (a) =q 0eζa.
The baseline ζ >0 is an adverse-reskilling scenario: automation lowers the transition rate from U
to H and raises the reverse rate. This direction is not imposed as an empirical fact. Section 4.2
reportsζ= 0 andζ <0, the latter representing AI-assisted upward mobility.
Letg s(k) be the stationary density. Aggregate capital is
K=
X
s
Z
kgs(k)dk.
4

Lowercase k is an individual household’s asset state; uppercase K is the integral of those assets
across the stationary distribution and equals productive capital in equilibrium. Production-task
labor and paid human-task labor are
L(a;g) =
X
s
Z
esℓs(a)gs(k)dk, H(a;g) =
X
s
Z
eshs(a)gs(k)dk.
The wage-cost exposure index is
ΛH (a;g) =−H a(a;g) =−
X
s
Z
esh′ s(a)gs(k)dk.(3.1)
A household in statesreceives labor income
yL s (a) =we shs(a).
The variable w is a wage per efficiency unit, not a literal common wage paid to every worker.
High-skilled households can earn more becausee H > eU and because AI raisesh H (a).
3.2 Prices and market clearing
The final-good firm is competitive and has Cobb–Douglas technology
Y=Z(a)K αL1−α.
Given (K, L, a), it solves
max
K,L

Z(a)K αL1−α −(r+δ(a))K−wL 	 ,
where
δ(a) =δ 0 +δ Aa.
The term δAa captures obsolescence and reorganization of legacy physical capital when AI is adopted.
This is why the model can generate lower stationary K in the high-automation equilibrium even
though automation raisesZ(a). The first-order conditions are
r=αZ(a)K α−1L1−α −δ(a), w= (1−α)Z(a)K αL−α.
Constant returns imply zero pure profits for the final-good firm:
Y−(r+δ(a))K−wL= 0.
Thus r is the real return on productive capital, or the investment opportunity. The price of installed
capital is normalized to one, so household wealth and aggregate capital are measured in units of
the final good. Consequently, the model has a real capital return r, but no separate Tobin’s q or
stock-market price for capital [Tobin, 1969].
Automation creates a rent by reducing paid human tasks below total production-task services.
Let
ΦA(a) =ϕa+ κ 2 a2
be the real resource cost of automation. Net automation rents are
ΠA(a;g) =w[L(a;g)−H(a;g)]−Φ A(a)−τ a.
5

A shareθ E ∈[0,1] is owned by domestic households, so the household asset return is
R=r+θ E
ΠA(a;g)
K .
A low-skilled but wealthy household can therefore be partly insulated from automation through
capital and automation-rent income.
If the policy is a literal tax, fiscal closure is required. The firm pays τ a. A fraction ωT is lost to
administrative or political-economy frictions, and the remaining part is rebated through a schedule
Ts(k):
Ts(k) = (1−ω T )τ a bs(k), b s(k)≥0,
X
s
Z
bs(k)gs(k)dk= 1.(3.2)
The function bs(k) is the rebate kernel: bs(k) = 1 gives a lump-sum rebate, while kernels increasing
or decreasing in income generate proportional or progressive rebates. Here Ts(k) is the household
rebate generated by the tax revenue.
Given a stationary environment (a, w, R, T, Q), a household starts from (k, s) and solves
Vs(k) = sup
{ct}t≥0
Ek,s
Z ∞
0
e−ρtu(ct)dt

subject to
˙kt =Rk t +we sthst(a) +T st(kt)−c t, k t ≥k ,
and the Markov transition matrixQ(a). The corresponding stationary HJB is
ρVs(k) = max c≥0
(
u(c) +V ′ s (k)[Rk+we shs(a) +T s(k)−c] + X
s′
qss′(a)[Vs′(k)−V s(k)]
)
,
where
u(c) = c1−γ
1−γ .
The optimality condition and savings drift are
u′(cs(k)) =V ′ s (k), ˙ks(k) =Rk+we shs(a) +T s(k)−c s(k).
Thus the law of motion fork is the household budget constraint evaluated at the optimal consumption
policy. The productive-capital return r is the marginal product net of depreciation. The household
return R additionally includes the domestically owned share of automation rents; hence R and r
coincide only when that rent yield is zero. The stationary Kolmogorov forward equation is
0 =−∂ k[ ˙ks(k)gs(k)] + X
s′
qs′s(a)gs′(k)−
X
s′
qss′(a)gs(k).
The stationary goods-market-clearing condition is
E goods ≡Y−  C+δ(a)K+ Φ A(a) +ω T τ a+ (1−θ E)ΠA(a;g)  = 0. (3.3)
The residual in (3.3) is the Walrasian accounting identity for the one-good economy [Arrow and
Debreu, 1954, Mas-Colell et al., 1995]. Once household budgets, firm zero profit, the government
budget, and capital-market clearing hold, the goods market clears by Walras’ law; because the
model has automation costs, fiscal leakage, and foreign ownership, the residual is reported explicitly
in the numerical results.
6

3.3 Firm automation and the stationary fixed point
Taking prices and the household distribution as given, the automating sector choosesafrom
Π(a) =Z(a)K αL(a;g) 1−α −wH(a;g)−Φ A(a)−P(a).
The private marginal benefit of automation, before policy, is
M(a;g, K, w) =

ψZ + (1−α) La(a;g) L(a;g)  Y+wΛ H (a;g).
Thus the firm’s automation first-order condition is
M(a;g, K, w)−ϕ−κa−ι= 0, ι=P a(a).(3.4)
The derivative in (3.4) is the sector’s direct profit derivative at fixed (g, K, w), not the total derivative
of aggregate consumption or prices. The decentralized economy has ι = 0. Numerically, for each
candidate a the household and market-clearing block is resolved, the direct profit derivative is
evaluated at those stationary objects, anda D is a root of (3.4).
Definition 1(Stationary competitive equilibrium).For a fixed policy rule, a stationary equilibrium
is a collection
{a, r, w, R, K, Vs, cs, gs, Ts}s∈{U,H}
such that: (i) Vs and cs solve each household’s infinite-horizon problem; (ii) gs is invariant under the
induced savings drift and skill transitions; (iii) the final-good firm satisfies its static factor-demand
conditions; (iv) household asset supply equals productive capital K; (v) fiscal and goods-market
accounts clear; and (vi) a satisfies the automating sector’s private optimality condition, including
any policy payment.
Households continue to move across wealth and skill states in a stationary equilibrium, while the
cross-sectional distribution remains invariant. Appendix A.6 establishes existence and conditional
uniqueness for the finite-grid system used in the computation. Transition dynamics and dynamic
policy are natural extensions of the stationary analysis.
3.4 Policy-maker index and equilibrium derivative
This subsection defines the reduced-form index used in the quantitative comparisons. The full
stationary economy determines prices, capital, consumption policies, skill masses, and the wealth
distribution jointly. For each automation valuea, write
ga, K(a), L(a), H(a), C(a), w(a), r(a), R(a)
for the corresponding market-clearing objects. The policy-maker index is
Gstat µ (a) =λC(a) +µB U (a), B U (a) =w(a)
Z
eU hU (a)ga U (k)dk,
where BU (a) is the collective wage bill paid to exposed low-skilled households. The marginal object
is therefore
dGstat µ (a)
da =λC a(a) +µB U,a(a).
7

This derivative is the bridge between the diagnostic benchmark and the computation. It ranks
stationary allocations under the chosen political-economy weights. If the index target aP is interior,
the wedge that implements it is obtained by evaluating the private condition (3.4) at the target:
ι∗ =M(a P ;g aP , K(aP ), w(aP ))−ϕ−κa P .
Ifa P = 0, the minimal boundary tax is
¯τ=M(0;g 0, K(0), w(0))−ϕ.
The derivative Ca(a) is a total equilibrium derivative, not a partial derivative holding prices or
the distribution fixed:
Ca(a) =
X
s
Z ∂cs(k, a)
∂a ga s (k)dk+ X s Z cs(k, a)∂g a s (k) ∂a dk.
The first term is the change in consumption policies at a fixed distribution. The second term is
the change in the stationary distribution. The numerical section evaluates this total derivative by
resolving the stationary market-clearing HJB–KFE system across automation values.
Appendix A.5 gives a stripped-down no-wealth-heterogeneity benchmark in which K(a), w(a),
and the skill masses can be eliminated analytically. That benchmark provides closed-form sign
conditions and predicted automation levels. The finite-grid heterogeneous-agent equilibrium used in
the numerical section is treated separately in Appendix A.6.
4 Stationary Numerical Results
This section organizes the quantitative evidence into four related exercises. The baseline describes
the technology and market-clearing mechanics. The regime comparison contrasts adverse-incidence
with productivity-led capital growth. The incidence results report wealth distributions, consump-
tion functions, and stationary consumption-equivalent comparisons. Section 5 then studies fiscal
instruments and ownership. Figures 1–4 show the technology, labor-income, and market-clearing
mechanics. Figure 5 and Tables 5–14 show goods-market accounting and the two AI regimes. Figures
11–13 show distributional incidence and consumption smoothing in the adverse-incidence baseline.
The productivity-led figures in Subsection 4.5 repeat the same analysis for the capital-growth case.
4.1 Calibration and data discipline
The baseline calibration is
α= 0.36, δ 0 = 0.06, δ A = 0.25, Z 0 = 1, ψ Z = 0.18,
ρ= 0.15, γ= 2, ϕ= 0.01, κ= 0.52.
Skill efficiencies are
eU = 0.75, e H = 1.25,
so eH /eU = 1.67, close to the BLS and Pew high-/low-wage ratios discussed in the introduction.
Task functions are
hU (a) =e −3.20a, h H (a) =e 0.35a,
ℓU (a) =e −2.50a, ℓ H (a) =e 0.55a.
8

Thus automation both displaces low-skilled paid tasks and complements high-skilled labor. This
sign combination creates a private benefit for high-skill users and a strong adoption incentive; it is
one scenario rather than a necessary feature of automation. High-skilled workers nevertheless remain
a minority in the computed high-automation economy. The automation-dependent transition rates
make the stationary mass of high-skilled households about 0.313 at the decentralized allocation,
while the low-skilled mass is about 0.687. Hence high-skilled workers benefit per capita, but there
are fewer of them and they do not form the main consumption base. The cost parameters are
selected so that the adverse-incidence scenario produces a decentralized automation index near one
half. The index is a task-technology intensity. It should not be read as a literal employment share.
The exponential specifications are reduced-form constant-semi-elasticity functions. They preserve
positivity and make the exposure parameters transparent; they are not derived from an organizational
model of AI adoption. The signs h′ U , ℓ′ U < 0 and h′ H , ℓ′ H > 0 define a displacement/complementarity
scenario, while their magnitudes are selected scenario inputs. The same is true of δA and ζ. The
baseline jointly selects strong low-skill exposure, adverse reskilling, and legacy-capital obsolescence,
so it should be interpreted as an adverse-incidence stress test rather than a central estimate.
Table 1 lists the full baseline calibration. The symbol θE denotes domestic ownership/pass-
through of automation rents. The baseline policy has τ = 0. Positive taxes are introduced only in
the fiscal experiments in Section 5.
Table 1: Full baseline parameter list
Symbol Meaning Baseline value
αcapital share in final-good production 0.36
Z0 baseline productivity 1.00
ψZ productivity gain from automation 0.18
δ0 baseline depreciation 0.06
δA automation-induced obsolescence of legacy capital 0.25
ρhousehold discount rate 0.15
γcoefficient of relative risk aversion 2.00
ϕlinear resource cost of automation 0.01
κconvex resource cost of automation 0.52
eU , eH skill efficiency levels (0.75, 1.25)
χU , βH paid-task exposure/complementarity inh s(a) (3.20, 0.35)
ξU , ηH production-task exposure/complementarity inℓ s(a) (2.50, 0.55)
q0, ζtransition-rate level and automation tilt (0.50, 0.75)
λpolicy-index weight on aggregate consumption 0.60
µpolicy-index weight on exposed low-skill labor income 1.00
θE domestic ownership/pass-through share of automation rents 0.45
ωT fiscal friction/loss share from tax collection 0.15
τautomation tax in baseline / fiscal experiments 0 / varied
The parameter θE deserves special interpretation. It is not the fraction of households who
own stocks. It is the share of net automation rents that is passed through to domestic households
through capital and equity claims. The value θE = 0.45 is the central pass-through benchmark.
The value θE = 0.15 is retained as a low-pass-through robustness case, while θE = 0.75 is a high
domestic-ownership case. This distinction matters because U.S. equity ownership is domestically
large but highly concentrated; moreover, automation rents may be retained inside firms, capitalized
into prices, accrue to managers and suppliers, or be owned by foreign investors. The calibration
therefore separates the aggregate ownership share from the distribution of ownership across wealth
groups.
9

Interpreting the productivity shifter.The choice of Z(a) should be read as a calibrated
technology shifter, not as a direct estimate of the mechanical productivity effect of every AI
application. With
Z(a) =Z 0eψZ a,
a full-index productivity gain ofg Z corresponds to
ψZ = log(1 +g Z).
For example, a 15 percent full-adoption productivity gain corresponds to ψZ ≃ 0.14. The baseline
value ψZ = 0.18 therefore implies a roughly 20 percent full-index gain. That is deliberately moderate
relative to highly optimistic AI forecasts. Goldman Sachs Research has estimated that generative
AI could raise global GDP by about 7 percent and, in later labor-market work, that full adoption
could raise labor productivity in developed markets by around 15 percent. McKinsey estimates that
generative AI could add$2.6–$4.4 trillion annually and contribute additional productivity growth
depending on adoption and redeployment of labor [Goldman Sachs Research, 2023, 2026, McKinsey
Global Institute, 2023]. Figure 1 therefore reports Z(a) under three interpretations: an empirical
guidepost, the baseline calibration, and a productivity-led counterfactual.
0.0 0.2 0.4 0.6 0.8 1.0
Automation intensity a
1.0
1.1
1.2
1.3
1.4
1.5Z(a)/Z(0)
Interpreting the productivity shifter
Goldman 15% full-adoption guidepost ( Z = 0.14)
Baseline paper calibration ( Z = 0.18)
Productivity-led capital-growth scenario ( Z = 0.40)
Figure 1: Interpreting Z(a) = Z0eψZ a. The baseline productivity gain is moderate; the productivity-
led scenario deliberately allows stronger output gains.
The baseline political-economy weights areλ= 0.6 andµ= 1, and the calculations also report
µ = 0. These weights affect only the reduced-form policy index; they do not enter household utility
or the decentralized equilibrium.
Before Table 2, the marginal propensity to consume (MPC) terminology is defined mathematically.
The reported MPC is the local wealth derivative of the consumption policy,
MPCk s (k, a) =∂cs(k, a) ∂k .(4.1)
10

Thus a “high-MPC exposed group” means that households losing labor income have steep consump-
tion functions near the borrowing constraint. Labor-income and policy changes are evaluated by
resolving the full stationary equilibrium.
Table 2: Empirical targets and model discipline
Object Empirical discipline Model use
Skill wage ratio BLS reports 2024 median weekly earnings of$1,543
for bachelor’s-degree workers and$930 for high-school
workers. Pew reports$33/hour in high-AI-exposure
jobs versus$20/hour in least-exposed jobs.
Sete H /eU = 1.67.
AI complementar-
ity
Pew reports that AI exposure is concentrated among
higher-paid, college-educated workers.
Motivates, but does not
identify, the scenario
h′ H (a) > 0 and ℓ′ H (a) > 0.
High-MPC expo-
sure
Fiscal evidence emphasizes large MPCs among liquidity-
constrained and hand-to-mouth households.
Low-wealth households
have high local MPCs
from the HJB solution.
Equity ownership The Federal Reserve Distributional Financial Accounts
track concentrated corporate-equity ownership.
Vary domestic ownership
θE.
Skill mobility No causal target is imposed for the effect of AI on
reskilling.
Report adverse, neutral,
and reversed mobility tilts.
Capital obsoles-
cence
No direct estimate disciplinesδ A. Vary δA across stress-test
and productivity-led sce-
narios.
4.2 Skill-mobility robustness
The sign of the skill-transition response is consequential. Table 3 holds automation fixed at the
baseline decentralized intensity a = 0 .526 and resolves the stationary equilibrium under three
transition tilts. The baseline ζ = 0.75 shifts mass toward the low-skill state. The neutral case sets
ζ = 0. The reversed case ζ = −0.75 represents AI-assisted upward mobility. All other parameters
are unchanged.
Table 3: Skill-mobility robustness at fixed automationa= 0.526
Mobility tiltζ m U mH K C Y r
Reversed / upward -0.75 0.312 0.688 2.896 1.162 1.822 0.0350
Neutral 0.00 0.500 0.500 2.687 0.889 1.503 0.0099
Adverse baseline 0.75 0.688 0.312 2.036 0.609 1.088 0.0009
Each row resolves the household HJB–KFE and market-clearing system at the same a. Absolute capital-market
residuals are below 5×10 −5, and absolute goods-market residuals are below 3×10 −7.
Reversing the mobility tilt substantially raises the high-skill mass, consumption, output, and
capital at the same automation intensity. The adverse transition matrix is therefore one driver of
the baseline outcome, not an innocuous normalization. This sensitivity is why the quantitative
results are presented as scenario comparisons rather than as a general prediction about AI.
11

4.3 Baseline equilibrium and why firms automate
For any policy τ , the automation number reported in the decentralized row is endogenous conditional
on the scenario parameter vector. It is the firm’s profit-maximizing stationary choice after the
household distribution and interest rate have cleared. I denote it by aD(τ ). In the no-tax baseline,
aD =a D(0) solves the firm condition (3.4):
Ea(a,0) =

ψZ + (1−α) La(a;g a) L(a;g a)  Y(a) +w(a)Λ H (a;g a)−ϕ−κa= 0.
Here ga, K(a), w(a), and r(a) are the stationary market-clearing objects associated with that value
of automation. The superscript D denotes the decentralized stationary Aiyagari/Huggett allocation,
not a planner choice. Table 4 compares it with the maximizer of the reduced-form policy index.
Table 4: Stationary allocations in the adverse-incidence scenario
Allocationa K L H r R w Y C B
Decentralized 0.526 2.036 0.674 0.565 0.001 0.006 1.055 1.088 0.609 0.597
Policy-index target 0.000 2.540 1.000 1.000 0.138 0.138 0.895 1.399 1.246 0.895
The policy index uses ( λ, µ) = (0 .6, 1). The minimal boundary tax that implements its a = 0 target is
¯τ= 0.589, and it collects zero revenue in that stationary allocation. The absolute goods-market residual is
below 10−7 in both rows.
The decentralized firm chooses aD = 0.526, while the policy index is maximized at aP = 0 under
the reported weights. Figure 2 shows that high-skilled labor income rises sharply with automation.
At the decentralized allocation, low-skilled labor income per worker is about 0 .147, while high-skilled
labor income is about 1 .586. At a = 0, the corresponding values are 0 .671 and 1 .119. The direct
productivity, complementarity, and labor-cost terms explain the private choice; the stationary
comparison records the accompanying incidence across skill and wealth groups.
In this adverse-incidence scenario, moving from a = 0 to the decentralized intensity lowers
low-skilled income, stationary consumption, and the capital stock. Capital falls from 2 .540 to 2 .036.
This comparison reflects several simultaneous assumptions: automation raises Z(a), but it also
reduces production-task labor, increases effective depreciation through δ(a), and shifts the skill
distribution towardU. It should not be attributed to a standalone aggregate-demand force.
12

0.0 0.2 0.4 0.6 0.8
Automation intensity a
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75Labor income per worker
Low-skill labor income yL U
High-skill labor income yL H
Productivity Z(a)
1.000
1.025
1.050
1.075
1.100
1.125
1.150
1.175
Productivity
Automation exposure and high-skill complementarity
Figure 2: Automation exposure and high-skill complementarity. Low-skilled labor income falls with
automation, while high-skilled labor income rises. This is the private benefit that makes automation
attractive to firms and high-skilled workers.
0.0 0.2 0.4 0.6 0.8
Automation intensity a
0.2
0.4
0.6
0.8
1.0
1.2Index, normalized at a = 0
Productivity gains and exposed-worker incidence
Z(a) productivity
C(a)/C(0) consumption
Y(a)/Y(0) output
yL U(a)/yL U(0)
aD
aP
Figure 3: Productivity and stationary-allocation responses. The figure reports the market-clearing
stationary equilibrium associated with each automation value up toa= 0.90.
13

0.0 0.2 0.4 0.6 0.8
Automation intensity a
0.0
0.5
1.0
1.5
2.0
2.5Level / rate
Market-clearing quantities and investment return
Capital K
Production labor L
Paid tasks H
Return r
Household return R
Decentralized
Policy-index target
Figure 4: Market-clearing quantities and investment return. The interest rate depends on production
labor relative to capital and on automation-induced depreciation, not on capital scarcity alone.
Figures 3 and 4 should be read together. Figure 3 shows rising productivity together with
falling consumption and the collective wage bill in the adverse-incidence scenario. Figure 4 shows
the market-clearing adjustment. Capital falls at high a, while production labor L also falls and
depreciation δ(a) rises. The investment return is therefore determined by the full marginal-product
and resource-accounting system.
4.4 Goods-market accounting
A useful way to understand the numbers is to ask where output goes. The one-good accounting
condition is
Y=C+δ(a)K+ Φ A(a) +ω T τ a+ (1−θ E)ΠA.
In the baseline no-tax economy, τ = 0, so the fiscal term is zero. Table 5 and Figure 5 report
the accounting decomposition. As automation rises, consumption falls, replacement investment
becomes a larger share of output because δ(a) rises, and foreign rent leakage can become relevant
when automation rents are not fully domestically owned. The final good is the numeraire, so the
model does not literally say that consumption goods become cheaper. The real statement is that
automation changes the feasible allocation of final-good output between consumption, replacement
investment, automation costs, and rents.
14

Table 5: Resource accounting along the automation grid
a Z K L Y C δ(a)K y L U yL H
0.00 1.000 2.540 1.000 1.399 1.246 0.152 0.671 1.119
0.25 1.046 2.249 0.822 1.235 0.916 0.276 0.324 1.312
0.50 1.094 2.062 0.674 1.103 0.636 0.381 0.159 1.560
0.75 1.145 1.738 0.550 0.952 0.392 0.430 0.075 1.802
0.90 1.176 1.476 0.485 0.851 0.269 0.421 0.046 1.887
a=0.00 a=0.25 a=0.50 a=0.75 a=0.90
0.0
0.2
0.4
0.6
0.8
1.0
1.2Final good units
Stationary goods-market accounting
Output Y
Consumption C
Replacement (a)K
Automation cost A
Foreign rent leakage
Figure 5: Stationary goods-market accounting. Output is split into consumption, replacement
investment, real automation costs, and foreign-owned automation rents. The plotted bars sum to
output up to the numerical residual.
4.5 Productivity-led capital growth
The baseline adverse-incidence case is not the only possible outcome. This subsection repeats the
Section 4 analysis under a stronger productivity shifter, stronger high-skill complementarity, weaker
low-skill exposure, and much lower automation-induced obsolescence. Table 6 lists the parameter
changes. All other parameters, including the ownership benchmark θE = 0.45, are held at their
baseline values unless reported. This is the disciplined optimistic case: artificial intelligence raises
productivity enough that households save more, capital grows, and aggregate consumption rises.
Table 7 states how the diagnostic benchmark in Appendix A.5 guides the two full-equilibrium
numerical regimes.
Table 8 reports the automation levels implied by the no-wealth-heterogeneity diagnostic bench-
mark and compares them with the stationary heterogeneous-agent computation. The diagnostic
calculation sets ¯r= 0.138, equal to the no-automation market-clearing return in the full model, and
uses C(a) = mU (a)yL U (a) + mH (a)yL H (a). Thus there is no wealth distribution or wealth-dependent
MPC in this calculation. In the adverse-incidence case, the policy-index maximizer lies below the
private root because the low-skill incidence term dominates. The full stationary GE computation
15

Table 6: Parameter changes for the productivity-led capital-growth case
Parameter Meaning Adverse-incidence baseline Productivity-led case
ψZ Hicks-neutral productivity gain 0.18 0.40
χU low-skill paid-task exposure 3.20 1.50
ξU low-skill production-task exposure 2.50 0.70
βH high-skill paid-task complementarity 0.35 0.70
ηL H high-skill production-task complementar-
ity
0.55 1.00
δA automation-induced capital obsolescence 0.25 0.02
κconvex automation cost 0.52 3.00
The productivity-led case is a counterfactual parameter regime that combines stronger productivity and
complementarity with lower exposure and obsolescence.
Table 7: How the primitive diagnostic is used in the numerical regimes
Regime Primitive forces in the diagnostic de-
composition
Full stationary-GE check
Adverse-incidence Large low-skill exposure χU , ξU , large
obsolescence δA, and the adverse mo-
bility tilt make the negative low-skill
term ΓU dominate.
Solve the HJB–KFE fixed point;
record the ordering of aD and aP ,
changes in aggregate C, and low-skill
low-wealth consumption.
Productivity-led capital
growth
Larger productivity gain ψZ, high-
skill complementarity (βH , ηL H ), and
lower obsolescence weaken the neg-
ative exposed-household term and
strengthen ΓH .
Solve the same fixed point; check
whether K, C, Yrise and then sep-
arately test whether low-skill low-
wealth households are protected.
16

yields the same ordering, aD = 0.526 and aP = 0. In the productivity-led case both diagnostic
choices are positive, and the full model moves both values upward once capital accumulation,
ownership, and market clearing are reintroduced.
Table 8: No-wealth diagnostic benchmark versus full stationary GE
Regime diagnostica D diagnostica P full GEa D full GEa P
Adverse-incidence baseline 0.419 0.000 0.526 0.000
Productivity-led capital growth 0.376 0.201 0.427 0.375
The diagnostic benchmark ignores asset heterogeneity, fiscal rebates, and automation-rent ownership. It
solves the closed-form private residual F (a) = M(a) −ϕ−κa and maximizes the reduced-form index
λC(a) + µBU (a). The full GE columns are the computational results from the stationary market-clearing
HJB–KFE economy.
Table 9 reports the stationary allocation at a = 0 and the decentralized automation allocation
under the productivity-led parameter vector. In this case, the decentralized firm chooses positive
automation, output rises, aggregate consumption rises, and the stationary capital stock rises.
Capital deepening lowers the investment return r. The household asset return R includes domestic
automation-rent ownership and may differ fromr.
Table 9: Productivity-led capital-growth case: stationary aggregates
Allocationa K L H Y C B r R w
No automation 0.000 2.540 1.000 1.000 1.399 1.246 0.895 0.138 0.138 0.895
Decentralized automation 0.427 4.144 1.025 0.841 2.011 1.474 1.055 0.106 0.101 1.255
Here B = wH is the collective wage bill. The fall in r reflects capital deepening. The lower value of R relative
to r occurs because net automation rents Π A are negative in this particular capital-growth counterfactual
after real automation costs are netted out.
The household budget equation explains how low-capital households fund consumption in any of
the stationary experiments:
˙ks(k) =Rk+we shs(a) +T s(k)−c s(k).
For a low-capital household, Rk is small, so consumption is financed mainly by labor income and
transfers, with the borrowing constraint preventing persistent negative drift at the lower boundary.
Group-level income tables should not be read as closed budgets for each skill group, because
households move between skill states carrying their assets with them. The aggregate household
budget and the goods-market constraint close in the whole economy, not separately within each
skill group.
Figures 6–10 repeat the same analysis used for the baseline case. Figure 6 groups the aggregate
and asset-market information together: panel (a) plots
KD/K0, C D/C0, Y D/Y 0, B D/B0,
where superscript 0 denotes the no-automation allocation under the same parameter vector; panel
(b) plots the no-automation and decentralized values of
r=αZ(a)K α−1L1−α −δ(a), R=r+θ EΠA/K,
and the dividend yield R−r . Figure 7 decomposes group income sources and consumption. The first
two bars in Figure 7 are the no-automation allocation and the last two bars are the decentralized
automation allocation. Figures 9 and 10 report wealth densities and consumption functions.
17

Capital K
Consumption C Output Y Wage bill B
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6Decentralized / no automation
(a) Aggregate ratios
Productive return r Household return R Dividend yield R − r
0.00
0.02
0.04
0.06
0.08
0.10
0.12
0.14Rate
(b) Asset-market returns
No automation (a = 0)
Decentralized
Productivity-led case: aggregates and returns
Figure 6: Productivity-led capital-growth case: aggregate ratios and returns. Panel (a) shows that
decentralized automation raises capital, consumption, output, and the collective wage bill relative
to no automation. Panel (b) shows that the productive return r and household return R can fall
when capital becomes abundant, even though aggregate output and consumption rise.
No automationLow No automationHigh DecentralizedLow DecentralizedHigh
0.0
0.5
1.0
1.5
2.0
2.5Per-capita flow
Productivity-led case: group income and consumption
Consumption
Labor income
Capital income
Figure 7: Productivity-led capital-growth case: group income and consumption. The first two
bars are the no-automation allocation and the last two bars are the decentralized automation
allocation. Bars show per-capita labor income weshs(a) and capital income Rk; markers show mean
consumption. The figure explains why the optimistic regime can raise aggregate consumption even
though low-skilled task income is still reduced. Tiny automation-dividend components are omitted
from the plot when they are visually negligible.
Aggregate abundance does not automatically imply distributional protection of exposed poor
18

households. The relevant object is not only aggregate consumption C, but consumption conditional
on skill and low wealth. Define the low-wealth cutoff ¯kL = 1.20, the bottom part of the no-automation
wealth distribution in this calibration, and compute
¯cP s,≤¯kL =
R ¯kL
k cP s (k)gP s (k)dk R ¯kL
k gPs (k)dk , P∈ {0, D}.
Table 10 reports this conditional consumption statistic. The productivity-led case raises aggregate
consumption, but low-skill low-wealth consumption falls relative to the no-automation allocation.
This is the sense in which the optimistic case establishes an aggregate-abundance possibility, while
distributional protection of poor exposed workers still requires broad pass-through, ownership, or
tax-and-rebate transfers. Table 10 reports the conditional means, and Figure 8 plots the same
comparison.
Table 10: Productivity-led case: low-wealth conditional consumption
Allocation Group Cell mass MeankLabor income Mean consumption
No automation Low skill 0.180 0.649 0.671 0.844
No automation High skill 0.148 0.729 1.119 1.051
Decentralized Low skill 0.161 0.590 0.496 0.702
Decentralized High skill 0.040 0.757 2.115 1.129
The table conditions on households with k≤ 1.20. The key row is low skill under decentralized automation:
aggregate C rises in the productivity-led regime, but consumption of low-skill low-wealth households falls
because they have little asset income and their labor income remains exposed.
No automationLow No automationHigh DecentralizedLow DecentralizedHigh
0.0
0.2
0.4
0.6
0.8
1.0Mean consumption for k ≤ 1.20
Productivity-led case: low-wealth conditional consumption
Figure 8: Productivity-led case: conditional consumption among low-wealth households. The plotted
statistic is ¯cP s,≤¯kL with ¯kL = 1.20. The figure makes explicit that aggregate abundance need not
protect low-skill low-wealth households absent broad ownership or transfers.
19

0 2 4 6 8 10 12
Assets k
0.00
0.02
0.04
0.06
0.08
0.10Density
Productivity-led case: stationary wealth distributions
Low skill, a=0
High skill, a=0
Low skill, decentralized
High skill, decentralized
Figure 9: Productivity-led capital-growth case: stationary wealth distributions gs(k). Both the
no-automation and decentralized distributions are plotted. Higher aggregate saving shifts the
distribution toward larger asset holdings, but the low-wealth region near the borrowing constraint
remains relevant for distributional incidence.
0 2 4 6 8 10 12
Assets k
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0Consumption c_s(k)
Productivity-led case: consumption functions
Low skill, a=0
High skill, a=0
Low skill, decentralized
High skill, decentralized
Figure 10: Productivity-led capital-growth case: consumption functions cs(k). Solid lines are the
no-automation allocation and dashed lines are the decentralized automation allocation. Read this
figure together with Figure 9: consumption at a given k is only half of the distributional question;
the densityg s(k) tells where households actually are.
20

A tax has a different stationary incidence in the productivity-led regime than in the adverse-
incidence regime. In the capital-growth case, moving from decentralized automation to the no-
automation allocation reduces C from 1.474 to 1.246 and reduces K from 4.144 to 2.540. Thus a
tax that eliminates automation supports exposed labor income but sacrifices productivity growth
and capital accumulation in this scenario. Positive-revenue taxes with targeted transfers illustrate
the distributional tradeoff without being labeled optimal policy.
4.6 Distributional incidence and consumption smoothing
The key distributional state is ( s, k), not skill alone. A low-skilled household with high wealth
owns capital and may be partly protected. A high-skilled household with little wealth still depends
on labor income. The local marginal propensity to consume out of wealth is defined in (4.1).
This wealth-MPC is computed from the finite-difference consumption policy and is used mainly
in the fiscal-incidence exercise, especially Table 17 and Figure 22. It is an incidence statistic
that summarizes the immediate consumption support from transfers. The consumption-equivalent
gain from policy P relative to the decentralized allocation is the constant proportional increase in
consumption in the decentralized allocation that would make the household indifferent between the
two allocations. It is defined by
V P s (k) = (1 +CE s(k))1−γV D s (k),
so that, forγ̸= 1,
CEs(k) =
 V P s (k)
V Ds (k)
1/(1−γ)
−1.
Group-level CE uses the decentralized distribution as weights. Table 11 reports these distributional
effects for the adverse-incidence baseline.
Table 11: Distributional incidence of the implementing policy
Group Mass Meank y L,D yL,P cD cP cP /cD −1 CE
Low bottom 0.353 0.56 0.147 0.671 0.287 0.822 1.86 1.98
Low middle 0.169 2.07 0.147 0.671 0.568 1.111 0.96 1.49
Low top 0.165 3.89 0.147 0.671 0.825 1.387 0.68 1.36
High bottom 0.083 0.75 1.586 1.119 0.595 1.055 0.77 1.32
High middle 0.084 2.10 1.586 1.119 0.811 1.268 0.56 1.18
High top 0.145 4.17 1.586 1.119 1.084 1.576 0.45 1.15
The table reports comparisons between stationary environments, weighted by the decentralized distribution.
The largest CE differences occur for low-skill bottom-wealth households. These are not transition-path welfare
effects.
Figure 11 plots the stationary wealth density gs(k) separately for each skill group and policy
regime. The solid curves are the decentralized distribution; the dashed curves correspond to
implementation of the policy-index target. Figure 12 then reports consumption conditional on
wealth, and Figure 13 plots the difference. Reading the three figures together shows both incidence
and smoothing: low-wealth households have the largest local consumption response, while high-
wealth households smooth with asset income.
21

0 2 4 6 8 10
Assets k
0.00
0.05
0.10
0.15
0.20Density
Stationary wealth densities
Low skill, no policy
High skill, no policy
Low skill, policy
High skill, policy
Figure 11: Stationary wealth densities with and without the implementing policy. The policy
changes not only current income but also the long-run distribution of wealth.
0 2 4 6 8 10
Assets k
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5Consumption c_s(k)
Consumption policy functions
Low skill, no policy
High skill, no policy
Low skill, policy
High skill, policy
Figure 12: Consumption policy functions with and without the policy. This is the numerical evidence
on consumption smoothing: consumption is increasing in wealth, and low-wealth households have
higher local MPCs.
22

0 2 4 6 8 10
Assets k
0.0
0.2
0.4
0.6
0.8
1.0Change in consumption
Consumption pass-through by wealth
Low skill: policy minus no policy
High skill: policy minus no policy
Figure 13: Policy-induced consumption change as a function of wealth. The plotted object is
cP s (k) −c D s (k); the horizontal zero line denotes no consumption change. Low-wealth households
have the largest local consumption response.
4.7 Static benchmark versus stationary GE
Section 2 separates the firm’s direct profit derivative from the derivative of the policy index.
The no-wealth benchmark in Appendix A.5 expresses their ordering in primitive exposure and
productivity terms, while the stationary GE block recomputes prices and the wealth distribution.
In the diagnostic benchmark, the private firm pushes automation to the upper grid value. In the
stationary economy, capital-market clearing, depreciation, and the wealth distribution moderate the
private choice to aD = 0.526. The reduced-form index is maximized at aP = 0 in both calculations.
The heterogeneous-agent model additionally reports exposure by wealth, capital adjustment, and
consumption smoothing. Table 12 summarizes the comparison.
Table 12: Static benchmark versus stationary heterogeneous-agent GE,λ= 0.6
Model privateaindexa P K D K P C D C P BD BP
Static benchmark 0.900 0.000 – – 0.903 0.895 0.903 0.895
Stationary Aiyagari/Huggett GE 0.526 0.000 2.036 2.540 0.609 1.246 0.597 0.895
4.8 Synthesis: two stationary scenario families
Table 13 summarizes the parameter forces behind the two scenario families, and Table 14 reports the
corresponding computed examples. The productivity-led case arises when the productivity gain ψZ,
high-skill complementarity (h′ H , ℓ′ H ), and domestic ownership θE are large. The adverse-incidence
case combines strong exposure, adverse mobility, obsolescence, and concentrated ownership. These
are stationary comparative statics; the model does not map either case into a short-run forecast.
23

Table 13: Parameter regimes that separate the two views of AI
Object Productivity-led AI Adverse-incidence
Productivity and high-
skill channel
High ψZ, high h′ H (a), high ℓ′ H (a).
High-skilled workers gain and pro-
ductivity gains are broad.
Moderate ψZ. High-skilled workers
gain, but low-skilled income losses
are larger.
Exposure and mobility Low or moderate χU ; neutral or up-
ward mobility; exposed households
have assets or transfers.
High χU ; adverse mobility; exposed
households are low wealth and high-
MPC.
Ownership High domestic ownership θE, broad
participation in capital and automa-
tion rents.
Low or concentrated ownership; eq-
uity income mainly insulates wealthy
households.
Stationary outcome Automation raises output, consump-
tion, and capital.
Automation raises high-skill income
but lowers consumption and capital
in the reported stress test.
Table 14: Computed examples of the two AI regimes
Regimeψ Z δA aD K D/K 0 C D/C 0 Y D/Y 0 yD H /y0 H
Adverse-incidence baseline 0.18 0.25 0.526 0.801 0.488 0.778 1.417
Productivity-led capital-growth case 0.40 0.02 0.427 1.631 1.183 1.438 1.890
Figure 14 compares the two computed regimes by plotting the ratios KD/K0, CD/C0, Y D/Y 0,
andB D/B0. Figure 15 then reports the parameter values behind the two scenario calculations.
KD /K0 CD /C0 YD /Y0
High-skill income ratio
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75Ratio to no automation
T wo AI regimes in the same stationary GE model
Adverse-incidence
Productivity-led
Figure 14: Two AI regimes in the same stationary GE model. Bars above one mean that decentralized
AI adoption raises the object relative to the no-automation allocation under the same parameter
vector.
24

Productivity / high-skillcomplementarity
Exposure of
high-MPC workers Domestic ownership
dispersion Predicted net
consumption e
ffect
−0.8
−0.6
−0.4
−0.2
0.0
0.2
0.4
0.6
0.8
Index
A visual regime map
Productivity-led AI
Adverse-incidence
Figure 15: Parameter values behind the two AI regimes. The horizontal axis gives the primitive
parameter symbols and the corresponding values for the productivity-led and adverse-incidence
cases. Bars report the numerical values used in the scenario calculations; colors, markers, and
hatches distinguish regimes in both color and black-and-white print.
5 Taxes, Rebate Rules, and Ownership Incidence
The implementing object is the marginal derivative that enters the firm automation condition (3.4).
For a literal automation taxP(a) =τ a, this derivative is
Pa(a) =τ,
so the tax shifts the firm’s first-order condition by τ . But a tax is also a fiscal object. If automation
remains positive, the government collects τ a; if tax collection is costly, ωT τ ais dissipated; and
the remaining amount is rebated through Ts(k) as in (3.2). Unless otherwise stated, the fiscal
experiments use θE = 0.45, λ = 0.6, µ = 1, and ωT = 0.15. Table 15 reports interior tax experiments.
These are not the boundary implementation; they are designed to show fiscal incidence when revenue
is actually collected.
The reported consumption-equivalent (CE) statistics compare household value functions across
stationary environments and aggregate them using the decentralized stationary distribution. They
are not welfare measures along a transition path from one invariant distribution to another. A
dynamic policy evaluation would require the transition of prices and the wealth distribution, which
is outside the model solved here.
The rebate looks small in the figures because it is a flow tax on the remaining automation base.
A large marginal tax can change firm behavior a lot by changing the first-order condition, but the
revenue it collects is τ a(τ ). If the tax pushes automation close to zero, the tax base disappears. In
the boundary implementation a = 0, revenue and rebates are exactly zero. In the interior example
τ = 0.10, revenue is only 0 .0393, and the friction-adjusted lump-sum rebate is 0 .0334 per person.
That is visible when plotted separately, but it is small relative to high-skilled labor income and total
consumption.
25

Table 15: Tax and fiscal-friction sensitivity, lump-sum rebates
τ ω T a Crevenue rebate lost avg. CE
0.10 0.15 0.393 0.763 0.0393 0.0334 0.0059 0.406
0.20 0.15 0.284 0.891 0.0567 0.0482 0.0085 0.735
0.589 0.15 0.000 1.246 0.0000 0.0000 0.0000 1.562
Figures 16–18 separate the three fiscal objects. Figure 16 shows the behavioral response aD(τ ).
Figure 17 reports the stationary CE comparison. Figure 18 reports tax revenue and dissipated
resources. This separation is important because a tax can have a large marginal effect on firm
behavior while raising little revenue when the automation base shrinks.
0.0 0.1 0.2 0.3 0.4 0.5 0.6
Tax
0.0
0.1
0.2
0.3
0.4
0.5Automation a( )
Automation response to a literal tax
T = 0.0
T = 0.15
Figure 16: Automation response to a literal automation tax. The tax reduces the automation base
a(τ), so the revenue base also shrinks.
Rebate rules change incidence. A lump-sum rebate returns the same flow to every household.
A labor-income-proportional rebate gives more to high labor-income households. A total-income-
proportional rebate also favors high-wealth households. Table 16 compares rebate rules. The same
marginal tax has a similar automation effect but different distributional effects. The final row
reports the pro-consumption progressive case with τ = 0.20; it is included in the same table to
compare the aggregate effect of targeting rebates to low-wealth and low-earnings households.
Figure 19 shows the same positive-tax experiment by group. It is included because the rebate is
numerically small in aggregate plots. The figure makes clear that the rebate is a separate household
flow, but also that it is small relative to labor and capital income.
Figure 20 reports the corresponding progressive-rebate income components. The progressive
rebate is visible in the low-skill bottom-wealth cell because the kernel targets low wealth and low
labor income.
26

0.0 0.1 0.2 0.3 0.4 0.5 0.6
Tax
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6Average CE
Consumption-equivalent gains from tax experiments
T = 0.0
T = 0.15
Figure 17: Stationary consumption-equivalent comparisons for tax experiments. These compare
value functions under invariant environments; they do not include transition-path welfare.
0.0 0.1 0.2 0.3 0.4 0.5 0.6
Tax
0.00
0.01
0.02
0.03
0.04
0.05Flow
Revenue a( )
0.0 0.1 0.2 0.3 0.4 0.5 0.6
Tax
0.000
0.002
0.004
0.006
0.008Flow
Loss T a( )
Tax revenue and dissipated resources ( T = 0.15)
Figure 18: Tax revenue and dissipated resources. A stationary flow is a per-period flow measured in
units of the final good. The boundary tax deters automation and therefore collects zero revenue in
the stationary allocation.
Table 16: Rebate-rule comparison and pro-consumption rebate case
Rulea K Crebate lost avg. CE
Lump-sum 0.393 1.991 0.763 0.0334 0.0059 0.406
Labor-income proportional 0.400 2.102 0.759 0.0340 0.0060 0.343
Total-income proportional 0.401 2.115 0.759 0.0341 0.0060 0.340
Progressive pro-consumption 0.284 2.025 0.899 0.0482 0.0085 0.735
27

Low bottom Low middle
Low top
High bottom High middle
High top
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6Per-capita stationary flow
Interior tax experiment with lump-sum rebates
Labor income weshs(a)
Capital income Rk
Tax rebate Ts(k)
Figure 19: Interior tax experiment with lump-sum rebates. The figure reports per-capita labor
income weshs(a), capital income Rk, and the tax rebate Ts(k) for τ = 0 .10 and ωT = 0 .15.
Automation dividends are omitted because their per-capita flow is below 2 × 10−4 in this experiment
and would not be visually informative.
Low bottom Low middle
Low top
High bottom High middle
High top
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6Per-capita stationary flow
Interior tax experiment with progressive rebates ( = 0.20)
Labor income weshs(a)
Capital income Rk
Progressive rebate Ts(k)
Figure 20: Interior tax experiment with progressive rebates. The figure reports the same income
components as Figure 19, but the rebated revenue is targeted toward low-wealth and low-labor-
income households. The tax is τ = 0.20, the fiscal friction is ωT = 0.15, and the rebate kernel is
proportional to exp(−ϱ kk−ϱ yyL s ) withϱ k = 0.55 andϱ y = 2.
28

A pro-consumption progressive rebate.The government need not rebate revenue equally or
in proportion to income. To illustrate a policy aimed directly at households with low savings and
low earnings, define a progressive rebate kernel
bP s (k) = exp[−ϱkk−ϱ yyL s (a)]P
s′
R
exp[−ϱkk′ −ϱ yyL s′(a)]gs′(k′)dk ′ .
This kernel gives more of the rebated revenue to low-wealth and low-labor-income households. For
a skill-wealth cell ( s, b), where s∈ {U, H}indexes skill and b indexes the bottom, middle, or top
wealth bin, define the average transfer
T sb =
R
Bb Ts(k)gs(k)dkR
Bb gs(k)dk .
Table 17 reports this T sb, the cell average wealth MPC MPCsb, and the first-round product
MPCsbT sb. The example below uses τ = 0.20, ωT = 0.15, ϱk = 0.55, and ϱy = 2. The equilibrium
automation response is pinned down by the marginal tax, while the rebate rule reallocates the
after-tax revenue. Table 17 and Figure 21 show that a targeted rebate delivers much larger direct
consumption support to the low-skill bottom-wealth group because that group receives a larger
transfer and has the highest local MPC.
Table 17: Progressive rebate case study,τ= 0.20,ω T = 0.15
Rule and group Transfer MPC MPC×transfer Interpretation
Lump-sum, low bottom 0.048 0.283 0.0137 equal rebate
Progressive, low bottom 0.112 0.283 0.0316 targeted support
Lump-sum, high top 0.048 0.142 0.0068 equal rebate
Progressive, high top 0.004 0.142 0.0006 little support
Figure 22 reports a first-round consumption-support diagnostic for each skill-wealth cell ( s, b),
wheresis skill andbis the wealth bin:
supportsb = MPCsb T sb ¯csb ,
where T sb is the average tax rebate received by the cell, MPCsb is the average local marginal
propensity to consume computed from the HJB consumption policy, and ¯csb is average consumption
in the same cell. The numerator approximates the immediate consumption response to the transfer,
and the denominator scales that response by the cell’s average consumption. The left bracket groups
the low-skill cells and the right bracket groups the high-skill cells. Long-run effects continue to
operate through saving, prices, and the stationary distribution.
5.1 Domestic ownership and the asset-return channel
The model does not contain a separate stochastic stock-price index. The household asset is a claim
to productive capital and domestic automation rents, with installed capital priced at one. Thus the
asset-market objects are the aggregate capital stock K, the productive-capital return r, and the
household asset return
R=r+θ E
ΠA
K .
29

Low bottomLow middle
Low top
High bottomHigh middle
High top
0.00
0.02
0.04
0.06
0.08
0.10Transfer flow
Per-capita transfers
lump-sum
progressive low-wealth/low-earnings
Low bottomLow middle
Low top
High bottomHigh middle
High top
0.000
0.005
0.010
0.015
0.020
0.025
0.030MPC T
Approximate consumption support
lump-sum
progressive low-wealth/low-earnings
Figure 21: Progressive rebate case study. The left panel reports per-capita transfers. The right
panel multiplies the transfer by the local MPC to show approximate consumption support. The
progressive rule supports low-wealth, low-earnings households much more strongly than a lump-sum
rebate.
Low bottom Low middle Low top High bottom High middle High top
0.00
0.01
0.02
0.03
0.04
0.05
0.06
0.07Approx. support / consumption
Low-skill households High-skill households
Progressive tax-and-rebate: targeted support diagnostic
Figure 22: Targeted-support diagnostics for the progressive rebate. Bars report MPCsbT sb/¯csb. The
left bracket groups low-skill households and the right bracket groups high-skill households.
30

The dividend yield from domestic automation rents is
dividend yield =R−r=θ E
ΠA
K .
I report both R and the dividend yield because R is the total return received by households, while
R−r isolates the ownership channel. This is the channel through which wealthy households,
including wealthy low-skilled households, may benefit from automation even when exposed labor
income falls.
Domestic ownership matters because wealthy households own capital and automation rents. The
main benchmark uses θE = 0.45, while the table below reports the low-pass-through case 0 .15 and
higher pass-through cases. Table 18 varies θE, the domestic ownership share of net automation
rents. Higher domestic ownership raises the household asset return R relative to the productive
capital return r, slightly increases capital accumulation in this calibration, and partially insulates
owners. It does not eliminate adverse incidence for low-wealth exposed households, because they
own little capital.
Table 18: Domestic ownership sensitivity, decentralized no-tax equilibrium
θE aD KD rD RD CD div. yield
0.00 0.523 1.993 0.0045 0.0045 0.602 0.0000
0.15 0.524 2.007 0.0033 0.0050 0.604 0.0017
0.30 0.525 2.022 0.0022 0.0055 0.607 0.0034
0.45 0.526 2.036 0.0010 0.0060 0.609 0.0050
0.60 0.527 2.050 -0.0002 0.0065 0.611 0.0067
The aggregate effects of θE in Table 18 are intentionally small in this calibration: changing
ownership reallocates automation rents, but it does not directly change the firm’s technology or the
tax. For that reason I do not plot the aggregate series separately. The economically relevant object
is the ownership wedge in household returns.
Figure 23 isolates the domestic-ownership channel. It does not say that ownership changes the
technology much; instead it shows how ownership changes the return received by households. This
is the channel through which high-wealth households can be protected even when exposed labor
income falls.
5.2 Instrument comparison at the policy-index target
The derivative of the firm’s policy payment, Pa(a; X), enters its automation condition. If one takes
the reduced-form index target aP as a political-economy objective, an interior target is implemented
only if
Pa(aP ;X P ) =M(a P ;X P )−ϕ−κa P ,
where M (a; X) is the private marginal benefit from automation before policy. A literal automation
tax has
P(a;X) =τ a, P a(a;X) =τ.
A retained-labor subsidyσper unit of paid human task input has
P(a;X) =τ a−σH(a;g),
31

0.0 0.1 0.2 0.3 0.4 0.5 0.6
Domestic ownership share E
0.000
0.001
0.002
0.003
0.004
0.005
0.006
0.007Rate
Domestic ownership and household returns
Productive return r
Household return R
Dividend yield R r
Figure 23: Domestic ownership and household returns. The productive capital return r is the
investment opportunity from the competitive firm. The household asset return is R = r + θEΠA/K.
The plotted wedge R−r is the channel through which domestic ownership insulates wealthy
households.
so, using the exposure index Λ H defined in (3.1),
Pa(a;X) =τ+σΛ H (a;g).
Two policy schedules P and eP implement the same interior index target only if they generate the
same marginal payment at the target state,
Pa(aP ;X P ) = ePa(aP ;X P ) =ι P .
For example, a pure automation tax implements the target with τ = ιP . A pure retained-labor
subsidy, withP S(a;X) =−σH(a;g), implements the same target if
σ= ιP
ΛH (aP ;g P ) ,Λ H (aP ;g P )>0.
The two instruments are equivalent only at the target margin; they need not have the same revenue,
distributional incidence, or off-equilibrium effects. The calculation implements the reduced-form
index target and allows the incidence of different instruments to be compared.
Fiscal closure determines who ultimately bears or receives the tax revenue. A tax can be rebated
to households, dissipated through administrative frictions, spent on public goods, or transferred to
another claimant. In the boundary implementation, revenue is zero because a = 0. In the interior
experiments, revenue is positive and the rebate rule materially affects stationary incidence and
household value comparisons.
32

6 A Proxy Regime Diagnostic for the Current AI Economy
The model implies that the relevant empirical question is not only whether automation raises
measured productivity, but whether the decentralized automation choice leaves the demand-weighted
objective increasing or decreasing. Leta D denote the private automation choice. Define
Dµ(a)≡ ∂ ∂a [λC(a) +µB U (a)],
where C(a) is aggregate household consumption after prices, the stationary distribution, and the
interest rate have adjusted, and BU (a) is the exposed wage bill defined in Section 3.4. In the
empirical proxy below, changes in exposed labor income are the data-side analogue of changes in
BU (a). Under a local single-crossing condition, Dµ(aD) > 0 places the policy-index target locally
above the decentralized choice, whileD µ(aD)<0 places it locally below.
For the empirical implementation, let bins b∈ Bindex households by occupation, education,
wealth, age, and industry. Let ηb denote the marginal propensity to consume of bin b, let ωK b denote
the share of automation rents or equity gains accruing to that bin, and let ∆ ayL b,t, ∆ aBU,t, and
∆aΠt denote local changes in bin labor income, the exposed wage-bill analogue, and automation
rents around the current automation margin. The empirical analogue is
bDµ,t =λ X
b∈B
bηb
h \∆ayL b,t +bωK b,t\∆aΠt i +µ \∆aBU,t.
Table 19 reports the proxy calibration for the contemporary United States. Current AI diffusion
is no longer negligible, but it remains concentrated. The Census BTOS AI supplement reports AI
use by 18% of firms, or 32% when employment-weighted, during November 2025–January 2026
[Bonney et al., 2026]. The Real-Time Population Survey reports work-related GenAI use by about
41% of workers in November 2025, and the Survey of Business Uncertainty reports that 78% of the
labor force works at firms using AI [Allen, 2026]. The private investment signal is strong, but broad
pass-through remains mixed: BLS reports nonfarm business productivity growth of 0.8% annualized
in 2026Q1 and 2.9% over the year, while real hourly compensation fell 0.5% in the quarter and the
labor share was 54.1% [U.S. Bureau of Labor Statistics, 2026].
Combining the ownership and MPC statistics gives the equity-rent demand pass-through
bηK = 0.874(0.008) + 0.126(0.075) = 0.016442.
Thus, one additional dollar of capitalized AI rent generates about 1.6 cents of consumption demand
under this two-group mapping. Because direct microdata linking current AI use to identified
labor-income changes are not yet sufficient to estimate ∆ ayL b structurally, I classify the current
economy with a normalized sensitivity calibration. Normalizing the AI capital-rent gain to one
dollar, the baseline uses \∆aY L broad = 0.005, \∆aBU = −0.025, λ = 1, and µ = 1. These values are
transparent sensitivity inputs, not estimates of realized aggregate effects on GDP, consumption,
employment, or total labor income. This gives
bDbase µ,2026 = [0.016442 + 0.005]−0.025 =−0.003558.
The current economy is therefore close to the boundary but slightly on the adverse-incidence side.
The classification is moderate-confidence: current evidence points to substantial task augmentation,
while capitalized AI rents remain concentrated and broad labor-income pass-through has not yet
clearly dominated the incidence channel.
33

Table 19: Proxy calibration for the current AI regime
Model object Empirical proxy Current calibration signal
Automation intensitya t Firm and worker use of AI AI use is incomplete but
material: 18% firm adoption,
32% employment-weighted
firm adoption, and 41%
employment-weighted worker-
task use in the Census AI
supplement [Bonney et al.,
2026].
Private marginal benefit
M(a)
Equipment, software, and data-center
investment
The private return sig-
nal is strong: 2026Q1
equipment investment rose
17.2%, intellectual-property-
products investment rose
13.0%, and data-center in-
vestment rose more than 22%
annualized [U.S. Department
of the Treasury, 2026].
Broad productivity pass-
through
Labor productivity, compensation, and
labor share
Productivity growth is pos-
itive but broad labor pass-
through is incomplete: pro-
ductivity rose 0.8% annual-
ized, real hourly compensa-
tion fell 0.5%, and the labor
share was 54.1% [U.S. Bureau
of Labor Statistics, 2026].
Ownership of automation
rentsω K b
Corporate equity and mutual-fund own-
ership by wealth group
AI-rent claims are likely to be
concentrated: in 2025Q3, the
top 1% held 50.2% of corpo-
rate equities and mutual fund
shares, the 90th–99th per-
centiles held 37.2%, and the
bottom 50% held 1.1% [Board
of Governors of the Federal
Reserve System, 2026c,a,b].
MPC weightsη b MPC heterogeneity by wealth and in-
come
The Fed estimates an MPC
out of wealth of 0.8 cents per
dollar for the top income quin-
tile and 7.5 cents per dollar
for the other quintiles [Beach
et al., 2025].
34

Table 20 gives the scale of the number. In the normalization used here, the positive demand
channels add 0 .021442: 0 .016442 from equity-rent demand pass-through and 0 .005 from broad
labor-income pass-through. The exposed-worker loss subtracts 0 .025. Thus the positive channels
offset 85.8% of the exposed loss, leaving a residual negative gap of 0 .003558, or 14.2% of the exposed
loss. Because the calculation is normalized to one dollar of AI rents, the residual gap is 0.36 cents
per dollar of normalized AI rents. If AI rents were 1%, 5%, or 10% of GDP, the corresponding
GDP-equivalent gaps would be 0.0036%, 0.0178%, and 0.0356% of GDP. These are scale translations
of the local diagnostic, rather than estimates of realized aggregate effects.
In economic terms, gains accruing to firms, investors, and complementary workers almost offset
the calibrated loss of exposed workers, but do not fully do so. The economy is close to the boundary
between the productivity-led and adverse-incidence scenarios.
Table 20: Scale of the current AI-regime statistic
Quantity Value
Positive demand channels,bηK + \∆aY L broad 0.0214
Exposed labor-income loss,| \∆aY L U |0.0250
Residual negative gap,| bDµ|0.0036
Residual gap per dollar of normalized AI rent 0.36 cents
Positive-channel offset rate 85.8%
Residual gap as share of exposed loss 14.2%
GDP-equivalent gap if AI rents equal 1% of GDP 0.0036% of GDP
GDP-equivalent gap if AI rents equal 5% of GDP 0.0178% of GDP
GDP-equivalent gap if AI rents equal 10% of GDP 0.0356% of GDP
Because bDbase µ,2026 is a calibrated sufficient-statistic value rather than a regression coefficient,
Table 21 reports calibration uncertainty bands, not frequentist confidence intervals. Holding the
exposed-group loss fixed at −0.025, the statistic crosses zero if broad labor-income pass-through rises
from the baseline 0 .005 to 0 .008558. Holding broad pass-through fixed at 0 .005, the statistic crosses
zero if the exposed wage-bill loss is milder than −0.021442. Thus the baseline is only 0 .003558
normalized units from the boundary, and the sign is informative but not yet statistically settled.
Table 21: Calibration uncertainty bands for the current AI regime
Assumption set Broad labor term Exposed labor term bDµ Sign result
Baseline point 0.005−0.025−0.0036 negative
Exposed-loss band 0.005 [−0.035,−0.015] [−0.0136,0.0064] crosses zero
Broad-pass-through band [0.000,0.015]−0.025 [−0.0086,0.0064] crosses zero
Joint labor-pass-through band [0.000,0.015] [−0.035,−0.015] [−0.0186,0.0164] crosses zero
6.1 Interpretation of the current diagnostic
The baseline value bDbase µ,2026 = −0.003558 is close to zero. It therefore motivates a boundary-
regime experiment rather than a large intervention: monitor labor-income pass-through and rent
concentration, and vary the strength of rent recycling with the sign and magnitude of the updated
statistic. The next subsection specifies that experiment.
35

6.2 Policy experiment: state-contingent AI-rent recycling
The proxy diagnostic suggests a state-contingent instrument experiment. In a productivity-led
regime the surcharge is zero. In an adverse-incidence regime a surcharge on concentrated automation
rents is paired with transfers to high-MPC households. The experiment changes the firm’s first-order
condition and the household incidence of automation rents at the same time.
A practical policy is anAI-rent rebate: a surcharge on concentrated AI rents, paired with a
refundable worker rebate or payroll-tax credit targeted to high-MPC workers and households in
high-exposure labor-market cells. In the notation of the model, the surcharge is the tax wedge τ in
the firm’s automation condition,
M(a, τ)−ϕ−κa−τ= 0,
and the rebate is a transfer rule that raises C(a) by directing revenue to bins with high ηb. The
policy does not tax ordinary capital accumulation or block productivity-improving AI. It taxes the
part of the return that is most likely to be capitalized into concentrated equity claims and recycles
the revenue toward the households whose spending has the largest aggregate-demand effect.
The implementable version has four components.
(i) T ax base.Apply the surcharge only to large firms or consolidated groups with substantial
AI-related intangible, software, data-center, or automation-capital income. The base should
be incremental rents rather than gross AI investment: profits or markups above a pre-
adoption benchmark, above-normal returns on AI-intensive intangible capital, or a formula
apportionment based on AI-related capital expenditure and excess operating margin. This
avoids penalizing ordinary productivity investment and avoids requiring the government to
classify every task as automated.
(ii) Revenue recycling.Return the revenue through a refundable worker credit, an expanded
earned-income-tax-credit-style payment, or a payroll-tax rebate. The target is not a universal
transfer to all households, but a transfer weighted toward low-wealth, high-MPC workers and
households in occupations or industries with high AI exposure. In the model this raises P b ηbTb,
where Tb is the transfer received by bin b. The United States already uses refundable credits,
including the earned income tax credit, to deliver income support to low- and moderate-income
workers [Internal Revenue Service, 2026].
(iii) Exposure adjustment.Let the transfer weight depend on observable exposure indicators:
occupation-level AI exposure, industry AI adoption, local labor-market displacement, and
earnings losses relative to a pre-AI trend. This makes the policy closer to wage insurance than
to a static redistribution program. Workers who experience wage losses from AI adoption
receive larger rebates, while workers in complementary occupations receive smaller or no
additional payments.
(iv) Automatic trigger.Activate or strengthen the surcharge-rebate rule when bDµ,t becomes
negative, or when observable sufficient statistics move in the same direction: rapid AI
investment, concentrated equity gains, weak labor-income pass-through, and declining labor
share. If bDµ,t > 0, the surcharge can be reduced or suspended. Thus the policy is state-
contingent rather than permanently anti-automation.
The rent-recycling experiment differs from a tax on AI inputs. An input tax can reduce
productivity-enhancing adoption even when Dµ(aD) > 0. The rent surcharge instead targets the
distribution of income claims and is activated only when the proxy statistic is negative. In that
36

case, a positive τ moves the private automation choice toward aP , while the high-MPC rebate
raises the consumption pass-through from the remaining automation surplus. The calculation is a
model-based instrument comparison; implementation would require a measurable rent base and an
empirically validated exposure rule.
7 Replication code
The replication code is available at
https://github.com/ebayr/automation-demand-externality.
The repository contains the Python scripts used to solve the stationary HJB–KFE systems, compute
the tax and ownership experiments, generate the tables, and reproduce the figures. The skill-mobility
robustness table is generated by resolving the same public solver after setting ζ∈ {−0.75, 0, 0.75}
and clearing its solution cache between cases.
8 Conclusion
Automation changes stationary allocations through productivity, task substitution and complemen-
tarity, skill transitions, capital obsolescence, precautionary saving, and ownership of automation
rents. In the adverse-incidence scenario, decentralized automation lowers low-skill income, consump-
tion, and capital relative to the no-automation allocation. In the productivity-led scenario, output,
consumption, and capital rise.
The mobility robustness exercise shows why these results should be stated conditionally. Holding
automation fixed at the baseline intensity, reversing the skill-transition tilt raises the high-skill
population share, stationary consumption, output, and capital substantially. The adverse mobility
specification and the obsolescence parameter are therefore important scenario assumptions rather
than secondary details.
The proxy empirical diagnostic places the current U.S. economy close to the boundary between
the productivity-led and adverse-incidence scenarios. Positive demand channels offset most of
the normalized exposed-worker loss, while concentrated equity ownership limits the consumption
pass-through from AI rents. The diagnostic is deliberately reported with sensitivity bands because
modest changes in broad labor-income pass-through reverse its sign.
The main quantitative conclusion is that the long-run effect of automation cannot be inferred from
its productivity effect alone. Labor-income exposure, reskilling, obsolescence, and rent ownership
jointly determine consumption, saving, and capital accumulation. The reduced-form policy index
and the rent-recycling experiment show how alternative fiscal closures distribute the remaining
gains. A full welfare analysis of transition paths is a distinct next step.
A Computational Appendix
A.1 Stationary system
For given (a, τ), the numerical equilibrium solves for
{Vs(k), cs(k), ˙ks(k), gs(k), Ts(k)}s∈{U,H}, K, L, H, C, Y, r, w, R.
37

The HJB, KFE, and factor-pricing equations are those stated in the text. Capital-market clearing is
Khh(r, a, τ) = X
s
Z
kgr,a,τ s (k)dk=K f irm(r, a),
where firm capital demand is obtained from
r+δ(a) =αZ(a)K α−1L1−α,
so
Kf irm(r, a) =L(a;g)
 αZ(a)
r+δ(a)
1/(1−α)
.
The goods-market residual reported by the code is
E goods =Y−[C+δ(a)K+ Φ A(a) +ω T τ a+ (1−θ E)ΠA].
A.2 Numerical implementation parameters and upwind scheme
The numerical parameters are kept out of Table 1 because they are not economic primitives. Table
22 reports the baseline grid and solver settings used for the stationary computations.
Table 22: Numerical implementation parameters
Object Symbol or code name Value
Asset grid sizeJ31
Asset lower boundk 0
Asset upper bound ¯k18
Grid spacing ∆k18/(31−1) = 0.60
Automation grid for reported searchesA61 points on [0,0.90]
HJB implicit pseudo-time step ∆ 1000
HJB maximum iterations – 20
HJB tolerance – 10 −5
Minimum consumption floor – 10 −10
Interest-rate root tolerance – approximately 3×10 −5
Automation-root tolerance – approximately 5×10 −4
For a candidate (r, a, τ), the HJB is discretized by an implicit upwind finite-difference scheme.
Let
Is,j =Rk j +we shs(a) +T s(kj)
denote non-consumption income at grid point ( kj, s). Given a value-function iterate Vs,j, define
forward and backward derivatives
D+Vs,j = Vs,j+1 −V s,j ∆k , D −Vs,j = Vs,j −V s,j−1 ∆k .
The candidate consumption policies are
c+ s,j = (D+Vs,j)−1/γ, c − s,j = (D−Vs,j)−1/γ,
and the corresponding drifts are
s+ s,j =I s,j −c + s,j, s − s,j =I s,j −c − s,j.
38

The upwind derivative uses D+V when the drift points to the right, D−V when it points to the left,
and the state-constraint derivative u′(Is,j) when the drift is locally zero. Boundary derivatives are
chosen so that the savings drift does not leave the grid:
˙ks(k1)≥0, ˙ks(kJ )≤0.
After the upwind direction is chosen, write the selected drift ass s,j =I s,j −c s,j, with
s+ s,j = max{ss,j,0}, s − s,j = min{ss,j,0}.
The drift contribution to the generator is
(Akv)s,j =
s+ s,j
∆k (vs,j+1 −v s,j) +
−s− s,j
∆k (vs,j−1 −v s,j),
with the boundary terms suppressed when j = 1 or j = J and the no-outflow condition imposed.
The skill-switching contribution is
(Aqv)s,j =
X
s′̸=s
qss′(a)(vs′,j −v s,j),
so the full generator isA=A k +A q. The implicit HJB step solves
[(ρ+ 1/∆)I− A]V new =u(c) + 1 ∆ V old,
iterating until the sup-norm change inVis below the tolerance in Table 22.
The resulting drift matrix and the skill-transition matrix Q(a) define the finite-state generator
A(r, a, τ). The stationary distribution solves
A(r, a, τ)⊤g= 0,1 ⊤g= 1,
where one row of the linear system is replaced by the normalization condition.
A.3 Calibration mechanics and scenario construction
The calibration is not a structural estimation exercise. It is a disciplined quantitative illustration
and a set of scenario exercises. Each parameter is tied either to a standard macro value, an empirical
guidepost, or a scenario dimension. The mechanics are as follows. First, the skill-efficiency ratio
eH /eU is chosen to match the high-/low-education wage ratio discussed in the introduction. Second,
the exposure and complementarity parameters χU , βH , ξU , ηL H are chosen so that automation sharply
reduces low-skilled paid tasks while increasing high-skilled task value. This creates the two-sided AI
debate in the model: firms and high-skilled workers have a genuine reason to adopt, while exposed
low-wealth households lose income. Third, ψZ is mapped into a full-index productivity gain through
eψZ − 1. Fourth, δA governs whether automation makes legacy capital obsolete. Fifth, θE is varied
because domestic ownership of AI rents is a distributional object. Sixth, the tax and rebate exercises
varyτ,ω T , and the rebate kernelb s(k) while holding technology primitives fixed.
For each proposed parameter vector, the code solves the full stationary fixed point. The
calibration is rejected if capital-market clearing fails, if the goods-market residual is not near zero, or
if the decentralized automation residual does not have a well-defined root. Prices are functions of the
distribution through market clearing, and the stationary distribution is obtained from the HJB–KFE
system. Gu et al. (2024) emphasize precisely this structure: heterogeneous-agent equilibria require
agent optimization, KFE consistency, and market-clearing prices as functions of aggregate states
and distributions [Gu et al., 2024].
Table 23 lists the public URLs for the empirical guideposts used in the calibration discussion.
39

Table 23: Empirical guideposts and report URLs used in the calibration discussion
Source Object used in the paper URL
BLS Education Pays Education wage premia used to disci-
plinee H /eU .
https://www.bls.gov/careeroutlook/2025/dat
a-on-display/education-pays.htm
BLS CPS Table 37b Employment and earnings by educa-
tion.
https://www.bls.gov/cps/cpsaat37b.htm
Pew Research Center AI exposure and earnings by occupa-
tion.
https://www.pewresearch.org/social-trends/
2023/07/26/earnings-of-workers-with-more-o
r-less-exposure-to-ai/
Federal Reserve DF A Distribution of corporate equity and
mutual-fund ownership.
https://www.federalreserve.gov/releases/z1
/dataviz/dfa/distribute/chart/
Treasury TIC Foreign holdings of U.S. securities.https://home.treasury.gov/data/treasury-i
nternational-capital-tic-system
Stanford AI Index AI business-adoption and investment
evidence.
https://hai.stanford.edu/ai- index/2025- a
i-index-report
Goldman Sachs Research Productivity-upside guidepost for gen-
erative AI.
https://www.goldmansachs.com/insights/arti
cles/generative-ai-could-raise-global-gdp
-by-7-percent
McKinsey Global Institute Generative-AI productivity and adop-
tion scenarios.
https://www.mckinsey.com/mgi/our-research/
the-economic-potential-of-generative-ai-t
he-next-productivity-frontier
Gu–Lauriere–Merkel–
Payne
Continuous-time heterogeneous-agent
master-equation methods.
https://arxiv.org/abs/2406.13726
(i) Production parameters.The capital share is α = 0.36, a standard Cobb–Douglas value.
Baseline depreciation is δ0 = 0.06. Automation-induced obsolescence δA is varied because AI
may make legacy capital less useful in the adverse-incidence regime but need not do so in the
productivity-led regime.
(ii) Preferences.The coefficient of relative risk aversion is γ = 2. The discount rate ρ = 0.15 is
the household discount rate in the stationary finite-grid economy. This value is not meant to
be an annual time-preference estimate. It is a numerical calibration for the model period used
here: with the coarse asset grid, strong automation-induced labor-income risk, and a single
capital/equity asset, much lower values of ρ push precautionary saving and aggregate capital
toward the grid boundary. The parameter is therefore chosen so that the computed economy
has a nondegenerate wealth distribution, an interior market-clearing interest rate, and a stable
HJB–KFE solution. The admissible choice is not arbitrary: ρ >0, the market-clearing interest
rate must lie inside the searched interval, the no-outflow boundary conditions must hold, and
the goods-market residual must be close to zero.
(iii) Skill efficiencies.The ratio eH /eU = 1.67 is chosen to match the approximate earnings
ratio between bachelor’s-degree workers and high-school workers in Bureau of Labor Statistics
education-earnings data. It is also close to the Pew high-AI-exposure versus low-exposure
wage comparison.
(iv) Automation technology.The productivity function is Z(a) = Z0eψZ a. A full-index
productivity gain gZ maps into ψZ = log(1 +gZ). The baseline uses a moderate gain, while the
productivity-led case uses a larger ψZ. The functions hU , hH , ℓU , ℓH encode low-skill exposure
and high-skill complementarity; they are varied across the two AI regimes.
(v) Automation costs.The parameters ϕ and κ govern linear and convex real costs of automation.
They are set so that the decentralized baseline has an automation index near one half. In the
productivity-led counterfactual, κ is higher to avoid pushing the model mechanically to the
upper automation boundary when productivity gains are large.
40

(vi) Skill mobility .The parameters q0 and ζ govern automation-dependent skill transitions. The
baseline ζ >0 is an adverse-reskilling scenario; Table 3 also reports neutral and reversed tilts.
(vii) Policy index.The parameters λ and µ are not preference primitives of households. They
define a reduced-form political-economy index over aggregate consumption C and the exposed
collective wage billB U ; that index is not a welfare criterion.
(viii) Ownership and fiscal closure.The central pass-through value is θE = 0.45. The robustness
cases 0.15 and 0 .75 represent low and high domestic pass-through of automation rents. The
fiscal friction ωT = 0.15 is a scenario parameter measuring administrative or political-economy
leakage from tax revenue.
A.4 Pseudo-code
1. Choose an asset grid and an automation grid.
2. For each (a, τ), guessr.
3. Compute Kf irm(r, a), w(r, a), labor income weshs(a), net automation rent Π A, dividend yield
θEΠA/K, tax revenueτ a, and rebate scheduleT s(k).
4. Solve the HJB by implicit upwind finite differences.
5. Construct the generator for (k, s) and solve the stationary KFE.
6. Compute household capital supplyK hh.
7. UpdateruntilK hh =K f irm.
8. StoreK, L, H, C, Y, B, BU , r, w, R, g, V, cand the goods-market residual.
9. Solve the decentralized automation residual.
10. Compute the reduced-form policy-index target by maximizingG µ(a).
11. Compute incidence by skill and wealth bins using the decentralized distribution as weights.
An aggregate-shock extension would add a law of motion for the distribution and a master-
equation block to this stationary HJB–KFE computation.
A.5 Diagnostic no-wealth-heterogeneity benchmark
This appendix gives a no-wealth-heterogeneity benchmark that serves as a diagnostic comparison
for the quantitative model. The benchmark suppresses precautionary saving, wealth-dependent
marginal propensities to consume, ownership of automation rents, fiscal rebates, and the stationary
wealth distribution. Those objects are present in the finite-grid heterogeneous-agent economy of
Appendix A.6. The purpose of the simplified environment is transparency: capital, wages, and skill
masses can be eliminated analytically, so the derivative of the reduced-form policy index can be
read from primitive exposure and productivity parameters.
Skill transitions are taken as primitive,
qU H(a) = ¯qU He−ζU a, q HU (a) = ¯qHU eζH a,
41

with stationary masses
mU (a) = qHU (a) qU H(a) +q HU (a) , m H (a) = 1−m U (a).
Production-task labor and paid-task labor are
L(a) =m U (a)eU e−ξU a +m H (a)eH eηL H a,
H(a) =m U (a)eU e−χU a +m H (a)eH eβH a.
Technology and depreciation are
Z(a) =Z 0eψZ a, δ(a) =δ 0 +δ Aa.
In this benchmark the representative Euler condition pins down the productive-capital return at a
required return ¯r. Cobb–Douglas factor pricing then gives
K(a) =L(a)
 αZ(a)
¯r+δ(a)
1/(1−α)
,
w(a) = (1−α)Z(a) 1/(1−α)
 α
¯r+δ(a)
α/(1−α)
.
Thus wages and capital are equilibrium objects in the diagnostic benchmark; they are not held fixed.
Group labor incomes are
yL U (a) =w(a)e U e−χU a, y L H (a) =w(a)e H eβH a.
The local consumption approximation is
C(a) =C 0 +η U mU (a)yL U (a) +η C H mH (a)yL H (a), η U , ηC H ∈[0,1],
and the reduced-form policy index is
Gµ(a) =λC(a) +µm U (a)yL U (a).
Define
ωw(a) = dlogw(a) da = ψZ 1−α − α 1−α δA ¯r+δ(a),
so that
dlogy L U (a)
da =ω w(a)−χ U , dlogy L H (a) da =ω w(a) +β H .
Finally set
ΓU (a) = (ληU +µ)y L U (a)  m′ U (a) +m U (a)(ωw(a)−χ U )  ,
ΓH (a) =λη C H yL H (a)  m′ H (a) +m H (a)(ωw(a) +β H )  .
The private automation residual in the diagnostic benchmark is
F(a) =M(a)−ϕ−κa,M(a) =

ψZ + (1−α) L′(a) L(a)  Y(a) +w(a)[−H ′(a)].
42

Derivative decomposition.In the no-wealth-heterogeneity benchmark,
G′ µ(a) = ΓU (a) + ΓH (a).
If the private residual F has a unique root aD on an interval I, the policy index Gµ is single-peaked,
and
ΓU (a)− >Γ H (a)+ for alla∈I,
thena P < aD. Conversely, if
ΓH (a)+ >Γ U (a)− for alla∈I,
and the positive productivity/high-skill term dominates on the relevant interval, then aP > aD
whenever the private root lies in that interval.
The stationary masses follow from the invariant distribution of the two-state Markov chain.
Since the skill masses are functions of a, both the level and the derivative of L(a) and H(a) are
determined by primitive transition and exposure parameters. The Euler condition r(a) = ¯r, together
with the Cobb–Douglas capital first-order condition
¯r+δ(a) =αZ(a)K(a) α−1L(a)1−α,
gives the displayed expression for K(a). Substituting this expression into the wage first-order
condition
w(a) = (1−α)Z(a)K(a) αL(a)−α
gives the displayed expression for w(a), so wages and capital adjust within the diagnostic benchmark.
Differentiating logw (a) gives ωw(a). Differentiating group labor incomes gives the two labor-
income elasticities. Differentiating
Gµ(a) =λ

C0 +η U mU (a)yL U (a) +η C H mH (a)yL H (a)  +µm U (a)yL U (a)
yields G′ µ(a) = ΓU (a) + ΓH (a). A negative derivative on the interval containing the private root
places the index maximizer to its left; a positive derivative places the maximizer to its right.
A.6 Finite-grid existence and conditional uniqueness
The result below is deliberately stated for the finite-grid stationary economy that is actually
computed. It is not a global uniqueness theorem for the infinite-dimensional heterogeneous-agent
economy.
For fixed (r, a, τ), let A(r, a, τ) denote the finite-state generator over grid points ( kj, s), and let
gr,a,τ denote its invariant distribution. Define
EK(r, a, τ) =Khh(r, a, τ)−Kf irm(r, a).
After market clearing inr, define the reduced automation residual
Ea(a, τ) =M(a, τ)−ϕ−κa−τ,
where M(a, τ) is the private marginal automation benefit after the stationary distribution and
interest rate have adjusted.
Proposition 1(Finite-grid stationary equilibrium).Fix a compact asset grid KJ = {k1, . . . , kJ },
an automation interval[0,¯a], and an interest-rate intervalR= [r , r]⊂(−δ(¯a), ρ). Suppose:
43

(i) for each( r, a, τ), the finite-grid discounted HJB has a unique solution and the induced policy
is continuous in(r, a, τ);
(ii) the upwind scheme satisfies no-outflow boundary conditions, ˙ks(k1)≥0and ˙ks(kJ )≤0;
(iii)q U H(a)>0andq HU (a)>0for alla∈[0,¯a];
(iv) for eacha,E K(·, a, τ)is continuous and changes sign onR;
(v) the reduced automation residualE a(·, τ)is continuous and changes sign on[0,¯a].
Then a finite-grid stationary equilibrium exists. If EK(·, a, τ)is strictly monotone for each a, and
Ea(·, τ)is strictly decreasing on[0 ,¯a], then the market-clearing interest rate and decentralized
automation rate are unique.
Proof. Fix (r, a, τ). The finite-grid HJB is a discounted finite-state control problem. The discount
rate ρ >0 and assumption (i) give a unique value function and policy. Assumption (ii) keeps the
savings drift inside the compact grid. Assumption (iii) makes the skill process irreducible; combined
with the upwind transition matrix, the generator has an invariant distribution on its communicating
class. HenceK hh(r, a, τ) andKf irm(r, a) are well defined.
By assumption (iv), EK is continuous in r and changes sign on a compact interval. The
intermediate value theorem gives a market-clearing interest rate. Strict monotonicity gives uniqueness
of that interest rate. Given the market-clearing interest rate for each a, the reduced automation
residual is well defined. Assumption (v) and the intermediate value theorem give an automation
root. Strict monotonicity of Ea gives uniqueness. Combining the HJB policy, invariant distribution,
market-clearing interest rate, and automation root yields a finite-grid stationary equilibrium.
For the reported calibration, the finite-grid conditions are checked directly. Table 24 reports
the residual and derivative checks on the automation grid. The reduced residual changes sign
between a = 0.510 and a = 0.525, and its numerical derivative is negative throughout the grid. The
goods-market residuals are below 10 −7 in absolute value.
Table 24: Numerical verification of finite-grid equilibrium conditions
Object Value
Ea(0,0) 0.5887
Ea(0.90,0) -0.2483
Root bracket fora D [0.510, 0.525]
maxa ∂M(a,0)/∂aon grid -0.0502
maxa ∂Ea(a,0)/∂aon grid -0.5702
Goods residual, decentralized allocation−5.85×10 −8
Goods residual, policy-index allocation−4.44×10 −10
Figure 24 visualizes the reduced automation residual used in Table 24. A sufficient monotonicity
condition is
κ >sup
a∈[0,¯a]
∂M(a, τ)
∂a .
This inequality says that the convex marginal cost is large enough, relative to the slope of the
equilibrium marginal benefit, to make the firm’s reduced first-order-condition residual strictly
decreasing. Hence the decentralized automation choice is unique whenever the residual crosses zero.
44

0.0 0.2 0.4 0.6 0.8
Automation a
0.2
0.0
0.2
0.4
0.6
Firm residual E_a(a,0)
Reduced automation residual after market clearing
Figure 24: Reduced automation residual after market clearing. The residual crosses zero once on
the computed grid and is decreasing throughout the grid.
The monotonicity condition is used to obtain a unique interior decentralized automation level.
If the reduced marginal benefit of automation is not decreasing sufficiently fast, the model may
instead admit multiple stationary automation equilibria or a boundary solution. Economically,
this corresponds to increasing returns, threshold effects, or organizational complementarities in
AI adoption. In that case aD should be defined as a global maximizer of firm value over the
compact automation interval, and the numerical exercise should report all local roots or local
maximizers when they exist. Multiple roots correspond to multiple AI-adoption regimes; an analysis
of equilibrium selection across those regimes is left for future work.
A.7 Empirical statistics and validation tests for the proxy regime diagnostic
This appendix describes the statistics used to classify the current AI economy and the validation
tests used to check the proxy regime diagnostic. The exercise is deliberately a sign test rather than a
full structural estimate. The structural model determines which sign matters; the empirical exercise
uses observable proxies to classify the sign of the local statistic.
A.7.1 Statistic
The target statistic is
Dµ(aD) = ∂ ∂a [λC(a) +µB U (a)]

 a=aD .
The economy is classified as a productivity-complementarity regime if Dµ(aD) > 0, an adverse-
incidence regime if Dµ(aD) < 0, and a boundary regime if Dµ(aD) is close to zero. In the empirical
implementation, household cells b∈ B are indexed by occupation, education, wealth, age, and
45

industry. The statistic is approximated by
bDµ,t =λ X
b∈B
bηb
h \∆ayL b,t +bωK b,t\∆aΠt i +µ \∆aBU,t.
The first bracket captures the demand value of labor-income changes and capital-rent changes. The
final term captures distributional concern for the exposed wage bill, the empirical analogue of BU (a).
This decomposition is useful because the available data are strongest for AI adoption, investment,
equity ownership, and MPC heterogeneity, and weakest for the causal current-period mapping from
AI adoption to labor-income changes.
A.7.2 Proxy construction
The statistic uses five groups of proxies.
(i) Automation intensity.Firm-level and worker-level AI adoption measures come from the
Census BTOS AI supplement and the Real-Time Population Survey. The Census supplement
reports AI use by 18% of firms during November 2025–January 2026, 32% when employment-
weighted, and worker-task AI use by firms representing 41% of employment [Bonney et al.,
2026]. The Real-Time Population Survey reports work-related GenAI use by about 41% of
workers in November 2025 [Allen, 2026].
(ii) Private marginal benefit.The calibration proxies M(a) with AI-related investment. It
uses 2026Q1 growth in real business equipment investment, intellectual-property-products
investment, and data-center investment [U.S. Department of the Treasury, 2026].
(iii) Broad pass-through.Labor productivity, real compensation, and labor share are aggregate
pass-through diagnostics. In 2026Q1, nonfarm business labor productivity rose 0.8% annualized
and 2.9% year over year, but real hourly compensation fell 0.5% and the labor share was
54.1% [U.S. Bureau of Labor Statistics, 2026].
(iv) Ownership of automation rents.The calibration uses Federal Reserve Distributional
Financial Accounts shares of corporate equities and mutual fund shares. In 2025Q3, the top
1% held 50.2%, the 90th–99th wealth percentiles held 37.2%, and the bottom 50% held 1.1%
[Board of Governors of the Federal Reserve System, 2026c,a,b].
(v) MPC weights.MPC-out-of-wealth estimates discipline the demand value of capitalized AI
rents. The calibration uses Federal Reserve estimates of 0.8 cents per dollar for the top income
quintile and 7.5 cents per dollar for the other quintiles [Beach et al., 2025].
Combining the ownership and MPC statistics gives the equity-rent pass-through
bηK = (0.502 + 0.372)(0.008) +  1−(0.502 + 0.372)  (0.075) = 0.016442.
This means that a dollar of capitalized AI rent produces about 1.6 cents of consumption demand
under the two-group mapping used in the calibration. The low value is a consequence of rent
concentration among low-MPC equity owners.
46

A.7.3 Baseline sign diagnostic
The baseline sensitivity calculation normalizes the capital-rent gain to one dollar and sets λ = µ = 1.
Because the causal current-period labor-income effect of AI is not yet separately identified, the
baseline is boundary-oriented: a small positive broad labor-income effect, 0 .005, and a modest
exposed wage-bill loss, −0.025. These are normalized sensitivity inputs, not estimates of realized
aggregate GDP, consumption, employment, or total labor-income effects. The resulting statistic is
bDbase µ,2026 = [0.016442 + 0.005]−0.025 =−0.003558.
The current economy is therefore classified as close to the boundary but slightly on the adverse-
incidence side. Its sensitivity to the labor-income inputs motivates the calibration bands reported
next.
A.7.4 Calibration uncertainty bands
The confidence language in the main text should be read as calibration uncertainty, not as a
conventional confidence interval. The current exercise does not estimate bDµ,t from a sampling design
with standard errors. Instead, Table 21 holds the equity-rent pass-through bηK = 0.016442 fixed
and varies the two labor-pass-through inputs around the baseline. The table is generated from
data/current us uncertainty bands.csv. It shows that the baseline negative value is close to
zero: modestly stronger broad labor pass-through or modestly milder exposed-worker losses would
move the statistic to the productivity-complementarity side. This is why the empirical classification
is stated as near-boundary and slightly adverse-incidence rather than as a precise estimated sign.
A.7.5 Sensitivity tests
Table 25 reports the sensitivity tests. The optimistic augmentation case assumes broad labor
complementarity and small exposed-group losses, so the statistic is positive. The pessimistic
displacement case assumes negative broad labor pass-through and larger exposed-group losses, so the
statistic is negative. The broad productivity-dividend case mimics an electrification-style episode,
while the neutral boundary case mechanically sets the statistic close to zero.
Table 25: Sensitivity tests for the empirical regime statistic
Scenario bDµ Classification
Baseline near-boundary adverse incidence -0.0036 Adverse-incidence:a P < aD
Augmentation optimistic 0.0439 Productivity-complementarity:a P > aD
Displacement pessimistic -0.0336 Adverse-incidence:a P < aD
Broad productivity dividend 0.0764 Productivity-complementarity:a P > aD
Neutral boundary 0.0000 Boundary:D µ ≈0
The sensitivity tests show that AI adoption alone does not determine the classification. The sign
changes when broad labor-income pass-through becomes sufficiently positive. With concentrated
rent ownership and incomplete labor-income pass-through, the current calibration lies slightly on
the adverse-incidence side of the boundary.
A.7.6 Historical validation tests
The historical validation test asks whether the classifier assigns familiar automation episodes to
plausible regimes. This appendix implements the exercise as a proxy backtest rather than only as a
47

qualitative sign check. The backtest uses the same reduced statistic,
bDhist µ = [∆aC K + [∆aY L,broad + [∆aY L,exposed ,
where the first term is the demand value of capital-rent pass-through, the second term is broad
labor-income pass-through, and the third term is the exposed-group labor-income term. This is
still not a full structural historical estimation exercise: the historical episodes do not have the same
household-bin microdata as the current U.S. AI episode, and the units of automation differ across
robots, electrification, computerization, and steam mechanization. The object is a transparent proxy
estimate used to test the classifier’s sign.
The current-data calibration fixes the capital-rent demand pass-through at
bηK = (0.502 + 0.372)(0.008) + [1−(0.502 + 0.372)](0.075) = 0.016442.
For the current AI row, the backtest uses the same baseline inputs as the main empirical classification:
0.016442 + 0.005−0.025 =−0.003558.
For the industrial-robot row, the calculation uses the reduced-form estimates in Acemoglu and
Restrepo [2020a]: one additional robot per thousand workers reduces wages by 0.42 percent and the
employment-population ratio by 0.2 percentage points. With a baseline employment-population
ratio of 0.60, the employment margin is approximately −0.002/0.60 = −0.0033. Because the paper
does not separately estimate a capital-rent pass-through term, the robot backtest uses the observable
labor-income channel only:
−0.0042−0.0033 =−0.0075.
For older episodes without directly comparable microdata, the backtest uses conservative proxy
values disciplined by the sign evidence: the industrial revolution is coded as near-boundary because
productivity gains were real but early wage pass-through lagged [Crafts, 2022]; electrification is coded
as a broad-productivity-dividend case because gains became broad after diffusion, complementary
capital deepening, education, and new tasks [Goldin and Katz, 2008]; and computerization is coded
as boundary/mixed because routine-task automation generated polarization rather than a single
aggregate sign [Autor and Dorn, 2013].
Table 26: Historical proxy backtest for the proxy regime diagnostic
Episode bDhist µ Pred. Target Source basis
British industrial revolu-
tion
0.0000 boundary boundary Crafts (2022)
Electrification and mass
production
0.0764 positive productivity-complementarity Goldin and Katz (2008)
Computerization and
ICT
0.0000 boundary mixed Autor and Dorn (2013)
Industrial robots -0.0075 negative adverse-incidence Acemoglu and Restrepo
(2020)
Current generative AI -0.0036 negative adverse-incidence Current-U.S. calibration
The backtest classifies the main historical cases in the expected direction. Counting the
computerization row as a mixed/boundary case, the generated backtest records four direct sign
matches and one mixed/boundary match, with no sign misses. The strongest quantitative validation
is the robot row, where the labor-income inputs come directly from reduced-form employment and
wage estimates. The weakest rows are the older historical episodes, where the exercise is best read
as a disciplined sign check rather than as a fully identified estimate of the general-equilibrium
derivative.
48

References
Daron Acemoglu.Introduction to Modern Economic Growth. Princeton University Press, 2008.
Daron Acemoglu and Pascual Restrepo. Artificial intelligence, automation and work. NBER Working Paper
24196, National Bureau of Economic Research, 2018.https://www.nber.org/papers/w24196.
Daron Acemoglu and Pascual Restrepo. Automation and new tasks: How technology displaces and reinstates
labor.Journal of Economic Perspectives, 33(2):3–30, 2019. doi: 10.1257/jep.33.2.3.
Daron Acemoglu and Pascual Restrepo. Robots and jobs: Evidence from US labor markets.Journal of
Political Economy, 128(6):2188–2244, 2020a. doi: 10.1086/705716.
Daron Acemoglu and Pascual Restrepo. The wrong kind of AI? artificial intelligence and the future
of labour demand.Cambridge Journal of Regions, Economy and Society, 13(1):25–35, 2020b. doi:
10.1093/cjres/rsz022.
Yves Achdou, Jiequn Han, Jean-Michel Lasry, Pierre-Louis Lions, and Benjamin Moll. Income and wealth
distribution in macroeconomics: A continuous-time approach.Review of Economic Studies, 89(1):45–86,
2022. doi: 10.1093/restud/rdab002.
S. Rao Aiyagari. Uninsured idiosyncratic risk and aggregate saving.Quarterly Journal of Economics, 109(3):
659–684, 1994. doi: 10.2307/2118417.
Jeffrey S. Allen. Monitoring ai adoption in the u.s. economy. Feds notes, Board of Governors of the Federal
Reserve System, 2026. URL https://www.federalreserve.gov/econres/notes/feds-notes/monitor
ing-ai-adoption-in-the-u-s-economy-20260403.html.
Kenneth J. Arrow and Gerard Debreu. Existence of an equilibrium for a competitive economy.Econometrica,
22(3):265–290, 1954. doi: 10.2307/1907353.
David H. Autor and David Dorn. The growth of low-skill service jobs and the polarization of the u.s. labor
market.American Economic Review, 103(5):1553–1597, 2013. doi: 10.1257/aer.103.5.1553.
Samara Beach, William L. Gamber, and Patrick Moran. Wealth heterogeneity and consumer spending. Feds
notes, Board of Governors of the Federal Reserve System, 2025. URL https://www.federalreserve.gov
/econres/notes/feds-notes/wealth-heterogeneity-and-consumer-spending-20250805.html.
Truman F. Bewley. Stationary monetary equilibrium with a continuum of independently fluctuating consumers.
In Werner Hildenbrand and Andreu Mas-Colell, editors,Contributions to Mathematical Economics in
Honor of Gerard Debreu. North-Holland, 1986.
Board of Governors of the Federal Reserve System. Share of corporate equities and mutual fund shares held by
the 90th to 99th wealth percentiles, 2026a. URL https://fred.stlouisfed.org/series/WFRBSN09149.
Retrieved from FRED, Federal Reserve Bank of St. Louis; series WFRBSN09149.
Board of Governors of the Federal Reserve System. Share of corporate equities and mutual fund shares held
by the bottom 50% (1st to 50th wealth percentiles), 2026b. URL https://fred.stlouisfed.org/seri
es/WFRBSB50203. Retrieved from FRED, Federal Reserve Bank of St. Louis; series WFRBSB50203.
Board of Governors of the Federal Reserve System. Share of corporate equities and mutual fund shares held
by the top 1% (99th to 100th wealth percentiles), 2026c. URL https://fred.stlouisfed.org/series/W
FRBST01122. Retrieved from FRED, Federal Reserve Bank of St. Louis; series WFRBST01122.
Kathryn Bonney, Cory Breaux, Emin Dinlersoz, Lucia Foster, John Haltiwanger, and Aditya Pande. The
microstructure of ai diffusion: Evidence from firms, business functions, and worker tasks. CES Working
Paper CES-WP-26-25, U.S. Census Bureau, Center for Economic Studies, 2026. URL https://www2.cen
sus.gov/library/working-papers/2026/adrm/ces/CES-WP-26-25.pdf.
49

Nicholas Crafts. Slow real wage growth during the industrial revolution: Productivity paradox or pro-rich
growth?Oxford Economic Papers, 74(1):1–23, 2022. doi: 10.1093/oep/gpab020.
Eduardo D´ avila and Anton Korinek. Pecuniary externalities in economies with financial frictions.Review of
Economic Studies, 85(1):352–395, 2018. doi: 10.1093/restud/rdx010.
John D. Geanakoplos and Heraklis M. Polemarchakis. Existence, regularity, and constrained suboptimality
of competitive allocations when the asset market is incomplete. In Walter P. Heller, Ross M. Starr, and
David A. Starrett, editors,Uncertainty, Information, and Communication: Essays in Honor of Kenneth J.
Arrow, volume 3, pages 65–96. Cambridge University Press, 1986. doi: 10.1017/CBO9780511983566.007.
Claudia Goldin and Lawrence F. Katz.The Race between Education and Technology. Harvard University
Press, 2008.
Goldman Sachs Research. Generative AI could raise global GDP by 7 percent. https://www.goldmansachs
.com/insights/articles/generative-ai-could-raise-global-gdp-by-7-percent , 2023. Research
note.
Goldman Sachs Research. How will AI affect the US labor market? https://www.goldmansachs.com/ins
ights/articles/how-will-ai-affect-the-us-labor-market, 2026. Research note.
Zhouzhou Gu, Mathieu Lauri` ere, Sebastian Merkel, and Jonathan Payne. Global solutions to master equations
for continuous time heterogeneous agent macroeconomic models, 2024. https://arxiv.org/abs/2406.1
3726.
John R. Hicks.The Theory of Wages. Macmillan, 1932.
Mark Huggett. The risk-free rate in heterogeneous-agent incomplete-insurance economies.Journal of
Economic Dynamics and Control, 17(5–6):953–969, 1993. doi: 10.1016/0165-1889(93)90005-M.
Internal Revenue Service. Earned income tax credit (EITC), 2026. URL https://www.irs.gov/credits-d
eductions/individuals/earned-income-tax-credit-eitc.
Andreu Mas-Colell, Michael D. Whinston, and Jerry R. Green.Microeconomic Theory. Oxford University
Press, 1995.
McKinsey Global Institute. The economic potential of generative AI: The next productivity frontier.
https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/the-economic-potential
-of-generative-ai-the-next-productivity-frontier, 2023. Report.
James Tobin. A general equilibrium approach to monetary theory.Journal of Money, Credit and Banking, 1
(1):15–29, 1969. doi: 10.2307/1991374.
U.S. Bureau of Labor Statistics. Productivity and costs: First quarter 2026, preliminary, 2026. URL
https://www.bls.gov/news.release/pdf/prod2.pdf.
U.S. Department of the Treasury. Economic policy statements to tbac: 2026, 2nd quarter, 2026. URL
https://home.treasury.gov/news/press-releases/sb0486.
50
