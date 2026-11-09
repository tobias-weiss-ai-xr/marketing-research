---
title: 'REFLEX: Reflexive Equilibrium Fixed-point Learning for Endogenous eXchanges'
url: https://arxiv.org/abs/2608.16155
category: ai-marketing
subcategory: measurement
date: 2026-08
venue: ''
authors:
- Vignesh Nagarajan
- Shriraghav Ashok
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.16155
pages: 8
chars: 41039
fetched_at: '2026-11-08T13:26:56+00:00'
kb_version: 1
---

# REFLEX: Reflexive Equilibrium Fixed-point Learning for Endogenous eXchanges

REFLEX: Reflexive Equilibrium Fixed-point Learning for
Endogenous eXchanges
Analytic Stability Boundaries for Performative Market Making in OTC Corporate Bond Markets
Vignesh Nagarajan∗†
Texas A&M University
Brown Foundation Scholar
College Station, TX, USA
vigneshn26@tamu.edu
Shriraghav Ashok†
University of California, Berkeley
Haas School of Business
Berkeley, CA, USA
sashok24@berkeley.edu
Abstract
In over-the-counter corporate bond markets, dealers compete for
client trades by quoting bid and ask prices. Tighter quotes attract
more business, but also informed customers more likely to trade
ahead of adverse price moves, leaving the dealer holding the risk.
As dealers increasingly use machine learning to set quotes, they
retrain these models on the trades their own quotes attract, creat-
ing a feedback loop in which each model reshapes the market that
generates its next training data. The question is therefore not only
whether a quoting model performs well, but whether the market
it creates stays stable as the model learns from it. Existing per-
formative prediction theory gives a sharp stability condition, yet
expresses it through abstract properties of the learning objective
a trading desk cannot measure before deployment. We introduce
Reflex, a framework that replaces those unobservable quantities
with three measurable features of dealer behavior: how strongly
trading volume responds to tighter quotes, how sharply the dealer’s
objective bends around its optimum, and how quickly informed
flow increases as spreads narrow.Reflexcombines these into a
single retraining modulus, a pre-deployment stability margin esti-
mated from a desk’s own quote and execution history that predicts
whether repeated retraining will converge or amplify itself. In sim-
ulation, predicted and measured stability agree within8%, and
competing dealers increase instability by1.74× with two and3.16×
with three, as predicted. Where ordinary retraining becomes unsta-
ble at modulus1.21, a structurally anchored correction converges as
blind retraining collapses. Calibrated over36years of public market
data, stability headroom falls roughly4 .4× for investment grade
and4 .3× for high yield from calm to crisis regimes. Ultimately,
Reflexturns an abstract convergence theorem into a market-level
safety margin that can be evaluated before an automated quoting
system goes live.
CCS Concepts
•Computing methodologies → Machine learning;•Applied
computing→ Economics;•Theory of computation → Market
equilibria.
∗Corresponding author.
†Both authors contributed equally to this research.
ICAIF ’26, Milan, Italy
2026. ACM ISBN 978-x-xxxx-xxxx-x/YYYY/MM
https://doi.org/10.1145/nnnnnnn.nnnnnnn
Keywords
performative prediction, market making, OTC corporate bonds,
retraining stability, systemic risk, machine-checked proofs
1 Introduction
Corporate bonds trade over the counter. A client requests a quote,
a dealer posts a half-spreadℎ, and the dealer’s inventory absorbs
the flow. Quoting on these desks is increasingly algorithmic, and
quoting policies are increasingly fit to historical flow.
That flow is not exogenous. A tighter quote wins more volume,
and it also summons more informed, or “toxic, ” flow that picks the
dealer off before adverse price moves. A wider quote starves both
channels. The policy𝜙 therefore induces the distribution𝐷(𝜙) it
will next be trained on. Fitting on the induced flow, redeploying,
and refitting is exactlyrepeated risk minimization(RRM) in the
sense of performative prediction [1]. RRM converges to a perfor-
matively stable point if and only if 𝜀<𝛾/𝛽 , where𝜀 bounds the
sensitivity of the distribution map and𝛾,𝛽 are the strong convexity
and smoothness of the loss.
The theorem is sharp, but its constants are Lipschitzassumptions.
A desk cannot evaluate𝜀,𝛽, or𝛾 before deploying, so it cannot know
whether its own retraining cadence is stable. Similarly, a supervisor
watching many dealers retrain against one shared pool of informed
flow cannot know whether competition among learners is manu-
facturing systemic fragility. Post-trade TRACE reporting reveals
the spreads that result, not the retraining loop that produced them.
Both questions are quantitative, and answering either needs the
constants themselves. We compute a market-level stability margin
for algorithmic liquidity provision, which puts the problem in the
AI-governance and systemic-risk scope of AI in finance.
To address these limitations, this paper introduces REFLEX (Re-
flexive Equilibrium Fixed-point Learning for Endogenous eXchanges),
which realizes performative predictioninsidea structural OTC
market-making model in the Guéant–Lehalle–Fernández-Tapia
(GLFT) family. It derives the loop constants from microstructure
primitives, then checks every closed form against a learned simula-
tor loop. We contribute six results, each derived and then confirmed
or falsified by experiment:
R1 An analytic stability boundary.We give 𝛾,𝛽, and𝜀 in closed
form from fill-curve curvature, P&L scale, and toxic-flow
slope, so the modulus𝑚=𝜀𝛽/𝛾 is known before deployment.
Measured moduli track it within8%where the loop contracts.
R2 A performative-gradient (PerfGD) correction, closed-form and
estimated. One extra scalar per step converges past the RRM
arXiv:2608.16155v1  [cs.LG]  17 Aug 2026

ICAIF ’26, November 14–17, 2026, Milan, Italy Vignesh Nagarajan and Shriraghav Ashok
boundary, and its structurally anchored learned counterpart
settles at the realized performative optimum where blind
retraining collapses.
R3 A multi-dealer boundary𝜀<𝛾/(𝑁 eff𝛽). Competition destabi-
lizes the market a factor𝑁eff before any single dealer would,
and a genuine shared-pool market measures1.74× and3.16×
amplification at𝑁=2,3.
R4 Finite-sample robust certificates.An 𝑂( 1/√𝑛) ambiguity ra-
dius bought by common random numbers (CRN) issues sta-
ble, unstable, orundecidedverdicts, separating statistical
from structural uncertainty.
R5 Factor-model scaling.The 𝑑×𝑑 modulus matrix has spectral
boundary𝜌(𝑀)< 1at 𝑂(𝑑𝑘 2) cost, and𝜌(𝑀) is flat from8
to128bonds on our calibration.
R6 Lazy deployment.The 𝐾-step retraining map𝜇(𝐾)=−𝑚+
𝑐𝐾(1+𝑚) yields deadbeat and maximal-stability cadences
in closed form. Both parameter-free predictions land on the
measured probe.
The system side contributes anun-blindedlearned market-response
operator whose training identifies𝑑𝐷/𝑑𝜙 . It adds three indepen-
dent instruments for 𝜀: a CRN best-response probe, an entropic
optimal-transport estimate [2–4], and a fitted informed-flow curve
[5]. It calibrates the simulator to 36 years of public market data
[6, 7], and it builds a verification layer of 66 numerical proof cer-
tificates plus Lean 4 [8, 9] formal skeletons. Negative results and
proxy-level data provenance are reported as such throughout.
2 Related Work
Perdomo et al. [ 1] established the convergence of RRM and its
stochastic variants [10], and later work estimates the distribution
response𝑑𝐷/𝑑𝜙 to optimize performative risk directly [ 11, 12].
The framework now reaches decision-dependent stochastic opti-
mization [13], distributions that carry their own dynamics [14, 15],
bandit feedback [16], multi-agent decision-dependent games [17],
and robust formulations; see [18] for a survey. In all of it,(𝜀,𝛽,𝛾)
stay abstract constants of an unspecified loss.
On the market-making side, Avellaneda and Stoikov [ 19] and
Guéant et al. [ 20] derived closed-form optimal quotes under ex-
ponential fill intensities, and later work added multi-asset dimen-
sionality reduction [21], adverse selection and price reading [22],
the stochastic-control toolkit [23], and the empirical anatomy of
flow–price interaction [5]. These models take the flow response to
quoting as a fixed input, so the learning loop that re-estimates the
market from its own induced data falls outside their scope.
To our knowledge, no prior work computes the performative
constants from market structure.
3 Market Model and the Retraining Loop
One deployment is one period of quoting by a dealer posting half-
spreadℎ. Skew is zero for the scalar theory, and the multi-bond lift
is R5. With𝜌 the latent liquidity ratio, benign notional follows the
GLFT exponential fill curve and informed notional a spread-gated
channel:
𝑈(ℎ)=𝐴𝜌𝑒 −𝑘ℎ, 𝜏(ℎ)=𝜌 ¯𝑔𝐼𝑏+𝛼𝑓𝐼𝑒 −𝑐𝑡ℎ ,(1)
where𝐴,𝑘 are the arrival rate and demand elasticity,𝐼𝑏,𝐼 the base
and feedback informed intensities,𝛼 adversarial informativeness,𝑓
the toxicity-feedback gain (our control variable),𝑐𝑡 the toxic spread
decay, and ¯𝑔∈( 0, 1) the mean of the informed traders’ tanh signal
gate. Informed flow trades with the signal, so each unit costs the
dealer an adverse-selection severity𝜓> 0, a state constant from
the same Gaussian gate integrals. The expected one-deployment
objective, with P&L scale 𝑃, quoting-cost weight 𝑤, anchorℎref,
and inventory-variance curvature𝜆𝑞≥0, is
𝐽(ℎ;𝑇)=𝑃

ℎ𝐴𝜌𝑒−𝑘ℎ+ℎ𝑇−𝜓𝑇−𝑤(ℎ−ℎ ref)2−𝜆𝑞  .(2)
The frozen toxic level𝑇 is what makes the learner structurally blind.
Within a deployment the fitted model conditions on the deployed
regime, so the dealer best-responds to𝑇=𝜏(ℎ dep) while only the
benign channel varies with the candidateℎ. Retraining is therefore
a cobweb map,
ℎ𝑡+1 =BR(ℎ 𝑡):=arg max ℎ 𝐽 ℎ;𝜏(ℎ 𝑡), 𝑚:=

BR′(ℎ∗)

,(3)
which contracts to the performatively stable spreadℎSP if and only
if𝑚< 1. The simulator realizes (1) to (3) with multi-bond flow,
an informed-flow saturation cap, and a liquidity field thatinflates
with realized flow. The frozen closed forms omit those endogenous
channels, and the measurements below make them visible.
4 Closed-Form Stability Theory
We state the objects the experiments test, each with the argument
it rests on. All six follow from the one-deployment objective (2) by
differentiation and the implicit-function theorem.
R1 (analytic boundary).Differentiating (2), the three Perdomo
constants are closed forms in the configuration:
𝛾=𝑃

2𝑤+𝐴𝜌𝑘𝑒 −𝑘ℎ(2−𝑘ℎ)+𝜆 𝑞  , 𝛽=𝑃,
𝜀(ℎ)=𝜌 ¯𝑔𝛼𝑓𝐼𝑐 𝑡𝑒−𝑐𝑡ℎ.(4)
Curvature is fill-curve curvature plus quoting-cost stiffness, smooth-
ness is the P&L scale, and 𝜀 is the toxic-flow slope |𝑑𝜏/𝑑ℎ| . The
implicit-function theorem gives BR′ =−𝜀𝛽/𝛾 , an oscillatory cob-
web, hence
𝑚(ℎ∗)= 𝜀𝛽 𝛾 = 𝜌 ¯𝑔𝛼𝑓𝐼𝑐 𝑡𝑒−𝑐𝑡ℎ∗ 2𝑤+𝐴𝜌𝑘𝑒 −𝑘ℎ∗ (2−𝑘ℎ ∗)+𝜆 𝑞 ,(5)
with𝑃 cancelling andℎ∗ the self-consistent fixed point of (3). The
loop is stable if and only if𝑚< 1. Every term is evaluable before
any loop is run, so the boundary is aprediction.
Derivation and regularity.On the quoting interval the frozen-
𝑇 objective is 𝐶2 and strongly concave, 𝜕11𝐽=−𝛾< 0, so its
maximiser is interior and unique and𝜕1𝐽(ℎ𝑡+1 ;𝜏(ℎ𝑡))= 0defines
BR implicitly. Differentiating inℎ𝑡 gives BR′ =−𝜕 1𝑇𝐽𝜏′/𝜕11𝐽 , and
(2)–(1) supply𝜕1𝑇𝐽=𝛽 and𝜏′ =−𝜀 , which is (5); stability is then
Banach contraction. R3, R5 and R6 reuse this step with𝜕1𝑇𝐽 replaced
by a rank-one coupling, by Γ−1𝐸, and by the𝐾-step warm-started
map.
Two structural corollaries matter for honest measurement. First,
adverse selection (𝜓𝑇 ) is constant inℎ within a deployment, so it
sets the profit level and the echo-chamber gap of R2 but drops out of
the boundary. Second, the modulussaturatesat the self-consistent
fixed point: widening spreads decay 𝜀(ℎ∗) exponentially, and at
default-like constants it never crosses1. This is defensive widening,

REFLEX: Analytic Stability Boundaries for Performative Market Making ICAIF ’26, November 14–17, 2026, Milan, Italy
so measured instability describes the retraining map at theoperating
spread, and we report it that way.
R2 (PerfGD correction).The performative objective is Φ(ℎ)=
𝐽(ℎ ;𝜏(ℎ)) . Un-blinding adds one closed-form term to the blind
gradient𝐺(ℎ)=𝜕 1𝐽(ℎ;𝜏(ℎ)):
Φ′(ℎ)=𝐺(ℎ)+Δ(ℎ),Δ(ℎ)=−𝛽(ℎ−𝜓)𝜀(ℎ),(6)
where Δ=𝜕 𝑇𝐽·(𝑑𝜏/𝑑ℎ) is the distribution-response term, supplied
entirely by the R1 closed forms, so the corrected ascent costs one
scalar more per step than RRM [11]. Its convergence is governed
not by the cobweb modulus but by the objective curvature at the
performative optimumℎ PO,
𝛾PO =𝛾+𝛽𝜀(2+𝑐 𝑡𝜓−𝑐 𝑡ℎPO),(7)
which stays positive where𝑚> 1, so the corrected loop converges
beyond the RRM boundary. The stable-versus-optimal separation,
the “echo-chamber gap” of [12], isℎSP−ℎPO =𝛽𝜀(ℎ SP−𝜓)/(𝛾+𝛽𝜀)=
𝑂(𝜀)in decision space and𝑂(𝜀 2)in value.
R3 (multi-dealer systemic risk).𝑁 dealers share one informed
pool with toxic spillover𝜅∈[ 0, 1], so flow displaced by one dealer’s
widening lands on the others. The joint best-response Jacobian is a
rank-one common-mode coupling. Its differential eigenvalues carry
(1−𝜅)𝑚 1 and its common mode−𝑚1𝑁eff with𝑁eff = 1+𝜅(𝑁− 1),
so the joint loop is stable if and only if
𝜀< 𝛾 𝑁eff𝛽, 𝑁 𝑐 =1/𝑚 1 (8)
is the critical dealer count at which a market of individually stable
dealers (𝑚1 < 1) turns systemically unstable. Competition manufac-
tures a synchronized cobweb, making fragility a market property
rather than a desk property.
R4 (robust boundary).With 𝑛 probe estimates of 𝜀 (sample
mean ˆ𝜀𝑛, std𝑠), the certificate
ˆ𝜀𝑛+𝛿𝑛 < 𝛾 𝛽, 𝛿 𝑛 = 𝑧1−𝑎𝑠√𝑛 ,(9)
declaresstable; ˆ𝜀𝑛−𝛿𝑛 >𝛾/𝛽 declaresunstable; anything between
isundecided. The parametric 𝑂( 1/√𝑛) radius is bought by the CRN
pairing of the probe, since a naive finite difference of indepen-
dent runs achieves only 𝑂(𝑛−1/3) after bias–variance balancing.
Pinning a crossing needs 𝑛req =𝑂(Δ −2) in the distance Δ to the
boundary, so statistical uncertainty is separated from structural un-
certainty by construction. A distribution-free quantile calibration of
𝛿𝑛, new here, shows𝑧𝑠 is conservative except under contamination
(Sec. 6.7).
R5 (factor scaling).For 𝑑 bonds, stability is governed by the
modulus matrix 𝑀=𝛽Γ −1𝐸 with𝐸=diag(𝜀 𝑖) and Γ the cross-
bond curvature, and the loop contracts if and only if𝜌(𝑀)< 1. A
𝑘-factor covariance makes Γ diagonal-plus-low-rank, so𝜌(𝑀) costs
𝑂(𝑑𝑘 2) by Woodbury, with truncation error linear in the residual
factor variance𝜆𝑘+1(𝐶). Large universes therefore stay certifiable
at practical cost.
R6 (lazy deployment).Suppose each deployment takes only 𝐾
inner gradient steps on the frozen-𝑇 objective (step𝜂ℎ, contraction
𝑐= 1−𝜂ℎ𝛾), warm-started from the deployed spread instead of the
exact best response. The outer map slope becomes
𝜇(𝐾)=−𝑚+𝑐 𝐾(1+𝑚),(10)
a one-parameter interpolation from inertia at𝜇( 0)= 1to the exact
cobweb as 𝜇→−𝑚 . Three consequences follow in closed form.
Adeadbeatcadence 𝐾db =ln 𝑚/( 1+𝑚) /ln𝑐 gives 𝜇= 0and
one-shot convergence. For𝑚> 1a stability window 𝐾≤𝐾 max =
ln(𝑚− 1)/(𝑚+ 1)/ln𝑐 keeps an RRM-unstable market stable, the
quantitative form of the greedy-versus-lazy gap in [1, 10]. And an
observer who fits the plain boundary to a lazy loop reads a two-
brancheffectivecurvature 𝛾eff(𝐾)=𝛾𝑚/|𝜇(𝐾)| , under-estimating
stiffness below the equal-modulus cadence and over-estimating it
above.
5 Experimental Setup
5.1 Learned Operator and the Four Loop Modes
The simulator is a multi-bond OTC market with benign and in-
formed clients, inventory, an informed-flow saturation cap, and a
latent liquidity field inflated by realized flow. The learned market-
response operator 𝑇𝜃 (MLP heads over per-bond features) pre-
dicts next-deployment flow distributions conditioned on a per-
deploymentpolicy summary, and is fit over a sliding window of
past deployments. With window≥ 2the derivative of its prediction
w.r.t. the summary, the learned𝑑𝐷/𝑑𝜙 , is identified by automatic
differentiation; a single-window fit is structurally blind and supplies
the RRM baseline.
Four retraining modes close the loop.(i)Blind RRM refits on
the latest induced flow.(ii)PerfGD-analyticuses the closed-form
Δ of (6) as a surrogate gradient.(iii)PerfGD-learnedconsumes
the free-form learned𝑑𝐷/𝑑𝜙 and is reported as a negative result.
(iv)PerfGD-structuralnever asks the network for a derivative. It
instead fits the theory’s own response families
ˆ𝜏(ℎ)= ˆ𝐶0+ ˆ𝐶1𝑒− ˆ𝑐ℎ, ˆ𝑢(ℎ)= ˆ𝐴𝑢𝑒− ˆ𝑘𝑢ℎ,(11)
plus the realized severity ˆ𝜓, to the loop’sowndeployment history
(per-bond, per-step samples over a 12-deployment window; a small
quote jitter supplies the within-deployment identification the echo
chamber cannot destroy). It then ascends ˆΦ′ = ˆ𝐺+ ˆΔ with step
1/ ˆ𝛾PO under a trust region (35%relative step cap) and an anti-echo
freeze that refuses to steer on unidentified fits. Both safeguards
come from failures we measured: exponential response fits on a
narrow spread window are line-degenerate and extrapolate badly,
and the unconstrained early ascent rails against its spread cap.
5.2 Three Instruments for𝜀and the Probe
Protocol
Three independent instruments estimate𝜀. (a) TheCRN best-response
proberuns paired deployments at ℎref±𝛿 under common random
numbers. Its finite difference of best responses estimates 𝑚, and
therefore𝜀= ˆ𝑚𝛾/𝛽 , while a signed𝐾-step variant measures𝜇(𝐾)
for R6. (b) Theoptimal-transportestimate ˆ𝜀=𝑊 1
𝐷(ℎ+𝛿),𝐷(ℎ−𝛿) /2𝛿
is the exact Wasserstein sensitivity of performative prediction, com-
puted via debiased log-domain Sinkhorn divergences [ 2, 3] with
the blur setscale-relatively(0 .02× pooled std, tuned against the
exact 1-D quantile𝑊1; Sec. 6.7). (c) Thefitted informed-flow curve
bins realized toxic notional against deployed spread, fits (1), and
differentiates [5].
A pre-run audit showed three protocol facts that matter at first
order, and all three are enforced here. Probe at the operating spread

ICAIF ’26, November 14–17, 2026, Milan, Italy Vignesh Nagarajan and Shriraghav Ashok
rather than the analytic fixed point. Keep collection jitter at0.05,
since at0 .2the BR probe inflates ∼3×. And report medians and
interquartile ranges (IQR) over 8 seeds with the R4 robust bands at
every grid point. We sweep the gain𝑓 rather than adversariality𝛼.
High𝛼 drives the dealer to wide spreads where𝑒−𝑐𝑡ℎ has decayed, so
the𝛼-response is non-monotone (measured hump0.08→ 1.83→
0.67). That confound is the quantitative case for 𝑓 as the control
variable.
5.3 Real-Data Calibration and Provenance
The simulator is calibrated per (rating × volatility regime) on a
public, verified panel. It combines∼36years of daily and∼70years
of monthly series (CBOE VIX as the𝜎proxy and regime classifier,
WTI, the Fed H.15 10-year, Shiller equity data, gold and CPI) with
the TRACE-derived corporate-bond factors of [6], whose liquidity
risk factor is the primary𝜀 proxy, and monthly returns for 212 real-
CUSIP bonds. Half-spread proxies combine VIX-implied spreads
with the illiquidity add-on of [7, 24], and𝜆(ℎ)=𝐴𝑒 −𝑘ℎ intensities
are fit per cell by maximum likelihood.
On provenance, plainly: this is not trade-level TRACE. Dealer-
side prints, per-dealer inventories, and per-bond(𝐴,𝑘) would re-
quire TRACE Enhanced. Only(𝐴,𝑘,𝜎,ℎ) are data-identified here,
the toxic channel is structurally scaled by documented ratios, and
the crisis-regime intensity fit is degenerate (𝑘= 0,𝑛= 74days) and
flagged wherever it binds. Regimeorderingof the boundary is data-
driven; absolute critical gains are not. Calibrated configurations
run in per-$100-par units, and every probe width, tolerance, and
OT blur is scale-relative by convention.
5.4 Verification Layer
Every load-bearing identity, inequality, and dynamical claim of R1–
R6 is re-derived numerically by 66proof certificates, run on both the
raw and the calibrated real-unit configurations: central differences
of thecomposedbest-response map against the assembled −𝜀𝛽/𝛾
with no shared code path, eigensolves against spectral formulas,
Monte-Carlo rate fits against claimed exponents, and the dynamics
run rather than assumed.
Building the layer caught real errors before the paper-grade run.
It surfaced a convention mismatch in which the 1-D frozen-gradient
helpers omit the inventory curvature, so their slopes are governed
by𝛾−𝑃𝜆 𝑞. It also falsified two first drafts: an “always-stiffer” claim
for𝛾eff, replaced by the two-branch law of R6, and a mis-signed
heavy-tail prediction for the R4 radius. The logical skeletons of all
six results are additionally formalized in Lean 4 against mathlib
[8, 9]. These are reviewed statements whose compilation is pending
a toolchain, so the numerical certificates remain the verification of
record. The full suite (152 tests, 11 experiments) runs CPU-only in
∼25minutes, deterministic from (configuration, seed).
6 Results
6.1 Machine-Checked Identities
Table 1 summarizes the certificates. All 66 pass, with worst residuals
far inside tolerance. The one excluded cell is deliberate. The R2
beyond-boundarydemo dynamicscertificate pins absolute raw-unit
constants, and imposing those on per-$100-par calibrated units is
Table 1: Numerical proof certificates (raw + calibrated real-
unit configurations). Each family’s worst residual sits inside
its stated tolerance.
Certificate family raw calib. worst resid. tol.
R1 analytic boundary 5/5 5/56.8×10 −2 8×10−2
R2 PerfGD identities 4/4 4/41.3×10 −6 2×10−2
R2 PerfGD demo dynamics 4/4 –1.4×10 −11 1×10−3
R3 multi-dealer 6/6 6/62.2×10 −16 1×10−9
R4 robust boundary 7/7 7/73.2×10 −2 1×10−1
R5 factor scaling 3/3 3/30.0 1×10 −9
R6 lazy deployment 6/6 6/61.1×10 −16 1×10−12
Figure 1: The daily market-fragility index, 1990–2026: the
R1 closed forms evaluated on real data. Top: fragility(𝒕)=
median(𝜺∗)/𝜺∗(𝒕) for IG (solid) and HY (dashed), with the
Lehman and COVID-freeze dates marked. Bottom: the VIX
spine, colored by volatility regime. The crisis plateau reflects
the degenerate crisis-cell fit and is flagged, not hidden.
exactly the class of unit bug the conventions forbid. It excludes
itself, and the calibrated pass proves the identities in real units.
6.2 A Real-Data Fragility Index (1990–2026)
Because R1 is a closed form in observables, it can be evaluated on
every trading day of the panel. Figure 1 plots the resulting index,
fragility(𝑡)=median(𝜀 ∗)/𝜀∗(𝑡) , and Table 2 gives the per-regime
summary. Three results hold up under every caveat below. First, the
stability headroom𝜀∗ =𝛾/𝛽 collapses∼4.4× for investment grade
(IG) and∼4.3× for high yield (HY) from calm to crisis. Second, HY
sits more than10× below IG ineveryregime, which is a level effect
rather than a crisis effect. Third, the modulus atobservedspreads
falls into crisis (IG0.85→ 0.14), so dealers widen faster than the
toxic channel steepens. Defensive widening is visible in real data.
The index saturates at a crisis plateau because of the degenerate
crisis fit. The GFC and the March-2020 COVID freeze are flagged at
the same ceiling, so intra-crisis ranking is explicitly not identified.
Per-cell a-priori boundaries span 𝜀∗ = 465→ 2.2from IG-calm
to HY-crisis while the fixed-point modulus stays regime-invariant
(≈0.066) by construction, so the regime story lives entirely in the
headroom.

REFLEX: Analytic Stability Boundaries for Performative Market Making ICAIF ’26, November 14–17, 2026, Milan, Italy
Table 2: Per-regime stability headroom𝜺∗ =𝜸/𝜷 and modulus
at observed spreads, evaluated on the 1990–2026 panel.
regime𝜀 ∗ IG 𝜀∗ HY 𝑚IG(ℎobs)𝑚 HY(ℎobs)
calm 1207.7 93.5 0.847 0.592
normal 739.2 61.3 0.870 0.563
elevated 594.4 45.9 0.520 0.367
stress 477.3 35.6 0.223 0.163
crisis 275.9 21.8 0.139 0.091
Table 3: Three-way 𝜺 triangulation at the operating spread,
against the closed form at the a-priori (A2) and at the realized
deployment state (𝝆=2.32,|𝒈|=0.446).
instrument ˆ𝜀vs. realized
closed form, a-priori state (𝜌=1) 0.7640.44×
closed form,realized state1.7261.00
CRN best-response slope 0.5080.29×
Sinkhorn/𝑊1 4.5782.65×
Fitted informed-flow curve 4.0112.32×
6.3 Predict-Then-Verify: the Boundary Crossing
Figure 2 is the headline falsification test. We sweep the gain𝑓 (7
values× 8 seeds), overlay the a-priori curve (5), and measure the
modulus with the CRN probe. In the contracting regime the agree-
ment is quantitative: measured median0.390against predicted0 .426
at𝑓= 2, an8%gap. The measured crossing sits at 𝑓∗≈ 3.17against
the a-priori4.70, and that gap is not free. The triangulation in Ta-
ble 3 independently measures the deployment’s own flow inflating
the liquidity field to𝜌≈ 2.3, and the closed form evaluated at that
realizedstate predicts𝑓 ∗≈2.8–3.0, bracketing the measurement.
The R4 certificates grade the grid exactly as the seed bands
warrant: stable through𝑓= 2, unstable at𝑓= 4, undecided where
beyond-boundary readings scatter. At𝑓= 8the eight seeds span
0.03–2.05, because past the boundary the probe is a finite-difference
diagnostic rather than a local slope. The fixed-point curve itself
saturates at0.61, so the measured instability is a property of the
retraining map at the operating spread, exactly as R1 predicts.
The two distribution-space instruments agree with each other
within14%and sit2 .3–2.7× above the realized-state closed form.
That residual is the state-feedback channel any frozen-state closed
form omits by construction, so the analytic boundary is alower
anchorrather than an unbiased point prediction. For a stability
certificate, erring low is the safe direction.
6.4 Competition Amplifies Instability (R3)
We probe agenuine 𝑁 -dealer market sharing one informed pool
rather than an analytic shortcut; the environment reduces bit-for-
bit to the single-dealer market at𝑁= 1. CRN joint-mode probes
measure the common-mode slope against the predicted 𝑁eff𝑚1
(Table 4). Amplification is1.74× at𝑁=2and3 .16× at𝑁=3against
predicted2and3, within13%and5%. The differential mode is dead
at full spillover ((1−𝜅)𝑚 1 = 0), so the instability is purely the
synchronized systemic channel.
Figure 2: Predict-then-verify phase diagram over the feed-
back gain 𝒇 : measured modulus (median, IQR band, and R4
robust band over 8 seeds) against the a-priori closed form
at the probe spread and the saturating fixed-point curve,
with the measured (𝒇∗≈ 3.17) and predicted (4 .70) crossings
marked.
Figure 3: The R3 systemic surface: joint modulus 𝒎𝑵 =
𝑵eff 𝒎1 over the (𝒇 , 𝑵) grid at full spillover ( 𝜿= 1), with
the 𝒎𝑵 = 1boundary contour. Gains that are comfortably
stable for a single dealer cross the systemic boundary as the
dealer count grows; the probes of Table 4 measure the first
rows of this surface on the simulated market.
The analytic surface in Figure 3 puts the critical dealer count at
𝑁𝑐≈ 7.9for the default single-dealer modulus, and the simulated
three-dealer cobweb already oscillates against its cap. For a super-
visor this matters directly: each desk can satisfy its own stability
check while the market as a whole violates (8), so fragility has to
be certified at the market level.
6.5 Closing the Loop-Level Gap: Structural
PerfGD (R2)
The demo regime is genuinely RRM-unstable (𝑓= 6, slow toxic
decay, cobweb modulus1 .21). There the blind cobweb provably
diverges while the corrected 1-D ascent converges, in closed form.

ICAIF ’26, November 14–17, 2026, Milan, Italy Vignesh Nagarajan and Shriraghav Ashok
Table 4: Measured common-mode retraining slope on the
shared-pool market versus the R3 prediction 𝑵eff 𝒎1 (full
spillover,𝜿=1).
𝑁measured predicted differential mode
1 0.786 0.786 –
2 1.369 1.571 0.0034
3 2.480 2.357 0.0032
Table 5: Loop outcomes in the RRM-unstable demo regime
(10 deployments, common seed; convergence verified against
independent structural fits).
mode finalℎoutcome
blind RRM 0.16 echo-chamber collapse
PerfGD-analytic 0.36 no settle (operator gradient)
PerfGD-learned 0.66 no settle (negative result)
PerfGD-structural 3.19 converges to realized optimum
The open question is whether alearnedloop can realize that cor-
rection. Figure 4 and Table 5 answer it from a common seed.
Blind RRM collapses into the echo chamber, ending at half-spread
0.16. PerfGD-analytic and the free-form PerfGD-learned mode both
fail to settle, because each consumes the operator’s implied objec-
tive gradient. The run’s seam diagnostics show why. The free-form
learned toxic slope starts right-signed (−0.84against analytic−1.79),
then flips sign and hovers near zero. The network has ample ca-
pacity; what it lacks is identification off the deployed regime. The
structural mode never asks it for a derivative. Fitting(11) to its own
deployment history, it climbs under the trust region andconverges
to the realized performative optimumat ℎ= 3.193, with late steps
falling0.35→ 0.02. That is within0.7%of its own running estimate
ˆℎPO = 3.172, and its fitted slope tracks the analytic shape (−1.33
against−2.00at the final iterate) while strengthening as the fit
window widens.
Benchmark honesty.The frozen-reference closed-form optimum
(ℎPO = 1.641) isnotthe target. In this high-intensity regime the
realized market differs from the frozen closed forms at first order
through channels they omit by construction: informed-flow sat-
uration, the 𝜌≈ 2.3liquidity inflation of Sec. 6.3, and severity
drift. The loop is therefore verified againstindependent structural
fitson fresh controlled deployments spanning the operating range.
Against those fits the settle point (i) zeroes their corrected gradient
(residual < 30%of its start value), (ii) sits strictly inside their blind
stable point (< 0.85× ˆℎSP, the realized echo-chamber gap, closed),
and (iii) brackets their independent optimum estimate. We claim
only this much: un-blinding is proven in closed form, and the struc-
turally anchored learned loop realizes it at loop level against the
realized-market benchmark, while the free-form correction remains
a documented negative result. What closed the gap was anchoring
the response model, not enlarging it.
6.6 Lazy Deployment Stabilizes an Unstable
Market (R6)
At a beyond-boundary configuration (𝑓= 5, exact-BR anchor ˆ𝑚=
1.205 > 1measured on the same seeds), the signed CRN 𝐾-step
probe traces 𝜇(𝐾) for𝐾∈ {1, 2, 3, 5, 8, 12, 20} (Figure 5). A one-
parameter fit of (10) gives inner contraction𝑐= 0.661, and both
parameter-free predictions land. The deadbeat sign flip is predicted
at𝐾db = 1.46, and measured medians run+0.021at 𝐾=1and−0.064
at𝐾=2. The stability-window exit is predicted at𝐾max = 5.75, and
measured|𝜇|is0.695at𝐾=5(inside) and1.541at𝐾=8(outside).
Laziness therefore keeps this RRM-unstable market measurably
stable for 𝐾≲ 6and inherits the cobweb’s divergence beyond,
which makes retrainingcadencea stability control. The measured
𝛾eff/𝛾 falls monotonically through1between 𝐾= 5and 𝐾= 8,
the stiff branch of the two-branch law. Beyond-boundary per-seed
scatter is large by construction, so the medians carry the result.
The clean tight-fit demonstration lives in the contracting regime,
where measured+0.78/+0.70/+0.37meet fitted+0.88/+0.68/+0.36
at𝐾=1/3/8, and it is locked in the test suite.
6.7 Scaling and Estimator Tuning
Factor scaling (R5).With per-bond volatilities dispersed at the data-
calibrated cross-sectional coefficient of variation, 𝜌(𝑀) is flat at
≈0.50from 𝑑= 8to128bonds (Figure 6) and pinned to the worst
scalar modulus. On this calibration correlation does not manufac-
ture cross-sectional instability, and the fragile mode is idiosyncratic.
The Woodbury path computes𝑑= 128in0 .12s and matches the
dense eigensolve to machine precision; the truncation bound holds
with 3–4 orders of magnitude of slack.
Sinkhorn blur (R1 instrument).Against the exact 1-D quantile 𝑊1,
the debiased-divergence bias is U-shaped in the scale-relative blur
at a fixed iteration budget, with log-domain under-convergence
below the minimum and entropic over-blur above it. The minimum
sits at0 .02× std, giving6 .1%ground-truth bias and1 .2%on the
config’s CRN samples. We bake that in as the default, and being
scale-relative it transfers to real-unit configurations unchanged.
Robust radius (R4).Across normal, heavy-tailed, and skewed
estimate distributions the𝑧𝑠 radius over-covers (0.99–1.00at95%
nominal). Only contamination from railed-probe patterns degrades
both radii (0.938), the honest𝑛req limit. On the actual CRN probe
estimates the quantile/𝑧𝑠 multiplier is0 .50, so𝑧𝑠 is binding and
adequately calibrated. We keep the quantile-guarded radius for
suspected contamination.
7 Conclusion
This paper proposes REFLEX, which makes the performative-prediction
stability condition something a desk can evaluate. We compute
(𝜀,𝛽,𝛾) from microstructure primitives, extend the boundary in
closed form to correction, competition, finite samples, dimension,
and cadence, verify each extension predict-then-verify against a
learned loop, evaluate it as a daily fragility index on 36 years of
real market data, and machine-check the identities end to end.
Two of the findings should carry past this model. Competition
among retraining dealers amplifies instability by the effective dealer
count, which makes certification of algorithmic liquidity provision

REFLEX: Analytic Stability Boundaries for Performative Market Making ICAIF ’26, November 14–17, 2026, Milan, Italy
Figure 4: Left: half-spread trajectories of the four learned retraining loops from a common seed in the RRM-unstable regime
(the frozen-reference 𝒉PO and 𝒉SP lines are context, not the benchmark; Sec. 6.5). Blind RRM collapses; the structurally anchored
loop converges to the realized performative optimum. Right: the three-way ML↔theory seam, showing the free-form learned,
structurally fitted, and analytic toxic slopes logged at every deployment. The free-form slope flips sign and hovers near zero;
the structural fit tracks the analytic shape.
Figure 5: Lazy deployment at a beyond-boundary configuration ( ˆ𝒎= 1.205). Left: the measured signed 𝑲 -step map (medians
over seeds; faint dots are per-seed readings) against the one-parameter fit 𝝁(𝑲)=−𝒎+𝒄 𝑲(1+𝒎) with 𝒄= 0.661, its 𝑲→∞
asymptote−𝒎, and the predicted deadbeat cadence. Right: the implied effective curvature 𝜸eff(𝑲)/𝜸 , predicted against measured,
with the stiff branch decaying through the exact-RRM line between𝑲=5and𝑲=8.
a market-level rather than a desk-level problem. And a learned cor-
rected loop stabilizes where blind retraining collapses only when
its response model is anchored to market structure. The free-form
alternative fails with the same data and more capacity, so a desk
should spend its modelling budget on structural anchoring rather
than on network capacity.
These results hold under idealizing assumptions. First, the cali-
bration is proxy-level rather than trade-level TRACE: VIX-implied
spreads, no per-dealer inventories, a structurally scaled toxic chan-
nel, and a degenerate crisis cell (𝑘= 0). Regime ordering is there-
fore data-driven while absolute critical gains are not, and TRACE
Enhanced calibration removes that limit. Second, at default-like
constants the self-consistent fixed point never destabilizes because
dealers widen defensively, so measured crossings describe the re-
training map at the operating spread. Beyond the boundary, probe
readings are finite-difference diagnostics with seed-level bifurca-
tion, so medians with robust bands carry the results, and moduli are
comparable within a protocol rather than across protocols. Third,
the structural loop’s optimum is therealizedone, benchmarked
against independent structural fits rather than the frozen-reference
closed form, with the gap attributed to saturation, liquidity inflation,
and severity drift. Its convergence is to the noise ball of an estimated

ICAIF ’26, November 14–17, 2026, Milan, Italy Vignesh Nagarajan and Shriraghav Ashok
Figure 6: Factor-model scaling (R5) with data-calibrated per-bond dispersion. Left: 𝝆(𝑴) is flat in universe size from 𝒅= 8to128
bonds and pinned to the worst scalar modulus, far below the 𝝆= 1boundary (dotted). Right: the truncation bound 𝑶(𝝀 𝒌+1(𝑪))
against the measured error|𝝆−𝝆 𝒌| at 𝒅= 128, showing three to four orders of magnitude of slack at every retained-factor
count𝒌.
gradient, and the free-form learned correction remains a negative
result by design. Finally, the Lean 4 skeletons are reviewed but
not yet compiled, so the 66 numerical certificates are the verifica-
tion of record. Future work: trade-level calibration, inventory-state
loop dynamics under state-dependent performativity, richer policy
classes, and compiling the formal layer.
Reproducibility
The full framework is openly available: 1 the six derivation doc-
uments D1–D6, the simulator, the operator, all four loop modes,
the estimator suite, the calibration pipeline with its data catalogue,
the 66-certificate verification layer, the Lean sources, and the illus-
trated reports of both paper-grade runs. All results in this paper
are regenerated by one command (run_all –profile full,∼25
CPU-minutes, deterministic from configuration and seed).
References
[1] Juan C. Perdomo, Tijana Zrnic, Celestine Mendler-Dünner, and Moritz Hardt.
2020. Performative Prediction. InProceedings of the 37th International Conference
on Machine Learning (ICML) (PMLR, Vol. 119). arXiv:2002.06673.
[2] Marco Cuturi. 2013. Sinkhorn Distances: Lightspeed Computation of Optimal
Transport. InAdvances in Neural Information Processing Systems (NeurIPS), Vol. 26.
[3] Jean Feydy, Thibault Séjourné, François-Xavier Vialard, Shun-ichi Amari, Alain
Trouvé, and Gabriel Peyré. 2019. Interpolating between Optimal Transport
and MMD using Sinkhorn Divergences. InProceedings of the 22nd International
Conference on Artificial Intelligence and Statistics (AISTATS) (PMLR, Vol. 89).
[4] Gabriel Peyré and Marco Cuturi. 2019. Computational Optimal Transport.Foun-
dations and Trends in Machine Learning11, 5–6 (2019), 355–607.
[5] Rama Cont, Arseniy Kukanov, and Sasha Stoikov. 2014. The Price Impact of
Order Book Events.Journal of Financial Econometrics12, 1 (2014), 47–88.
[6] Alexander M. Dickerson, Philippe Mueller, and Cesare Robotti. 2023. Priced Risk
in Corporate Bonds.Journal of Financial Economics150, 2 (2023).
[7] Nils Friewald, Rainer Jankowitsch, and Marti G. Subrahmanyam. 2012. Illiquidity
or Credit Deterioration: A Study of Liquidity in the US Corporate Bond Market
during Financial Crises.Journal of Financial Economics105, 1 (2012), 18–36.
[8] Leonardo de Moura and Sebastian Ullrich. 2021. The Lean 4 Theorem Prover and
Programming Language. InAutomated Deduction – CADE 28 (Lecture Notes in
Computer Science, Vol. 12699). Springer.
1https://github.com/vignesh-nagarajan-vn/REFLEX/
[9] The mathlib Community. 2020. The Lean Mathematical Library. InProceedings of
the 9th ACM SIGPLAN International Conference on Certified Programs and Proofs
(CPP).
[10] Celestine Mendler-Dünner, Juan C. Perdomo, Tijana Zrnic, and Moritz Hardt.
2020. Stochastic Optimization for Performative Prediction. InAdvances in Neural
Information Processing Systems (NeurIPS), Vol. 33. arXiv:2006.06887.
[11] Zachary Izzo, Lexing Ying, and James Zou. 2021. How to Learn when Data Reacts
to Your Model: Performative Gradient Descent. InProceedings of the 38th Interna-
tional Conference on Machine Learning (ICML) (PMLR, Vol. 139). arXiv:2102.07698.
[12] John P. Miller, Juan C. Perdomo, and Tijana Zrnic. 2021. Outside the Echo Cham-
ber: Optimizing the Performative Risk. InProceedings of the 38th International
Conference on Machine Learning (ICML) (PMLR, Vol. 139). arXiv:2102.08570.
[13] Dmitriy Drusvyatskiy and Lin Xiao. 2023. Stochastic Optimization with Decision-
Dependent Distributions.Mathematics of Operations Research48, 2 (2023).
arXiv:2011.11173.
[14] Qiang Li and Hoi-To Wai. 2022. State-Dependent Performative Prediction with
Stochastic Approximation. InProceedings of the 25th International Conference on
Artificial Intelligence and Statistics (AISTATS) (PMLR, Vol. 151). arXiv:2110.00800.
[15] Gavin Brown, Shlomi Hod, and Iden Kalemaj. 2022. Performative Prediction in a
Stateful World. InProceedings of the 25th International Conference on Artificial
Intelligence and Statistics (AISTATS) (PMLR, Vol. 151). arXiv:2011.03885.
[16] Meena Jagadeesan, Tijana Zrnic, and Celestine Mendler-Dünner. 2022. Regret
Minimization with Performative Feedback. InProceedings of the 39th International
Conference on Machine Learning (ICML) (PMLR, Vol. 162). arXiv:2202.00628.
[17] Adhyyan Narang, Evan Faulkner, Dmitriy Drusvyatskiy, Maryam Fazel, and
Lillian J. Ratliff. 2022. Multiplayer Performative Prediction: Learning in Decision-
Dependent Games.arXiv preprint arXiv:2201.03398(2022).
[18] Moritz Hardt and Celestine Mendler-Dünner. 2023. Performative Prediction: Past
and Future.arXiv preprint arXiv:2310.16608(2023).
[19] Marco Avellaneda and Sasha Stoikov. 2008. High-Frequency Trading in a Limit
Order Book.Quantitative Finance8, 3 (2008), 217–224.
[20] Olivier Guéant, Charles-Albert Lehalle, and Joaquin Fernández-Tapia. 2013. Deal-
ing with the Inventory Risk: A Solution to the Market Making Problem.Mathe-
matics and Financial Economics7, 4 (2013), 477–507.
[21] Philippe Bergault and Olivier Guéant. 2021. Size Matters for OTC Market Makers:
General Results and Dimensionality Reduction Techniques.Mathematical Finance
31, 1 (2021). arXiv:1907.01225.
[22] Alexander Barzykin, Philippe Bergault, Olivier Guéant, and Fanny Lemmel. 2025.
Optimal Quoting under Adverse Selection and Price Reading.arXiv preprint
arXiv:2508.20225(2025).
[23] Álvaro Cartea, Sebastian Jaimungal, and José Penalva. 2015.Algorithmic and
High-Frequency Trading. Cambridge University Press.
[24] Jack Bao, Jun Pan, and Jiang Wang. 2011. The Illiquidity of Corporate Bonds.The
Journal of Finance66, 3 (2011), 911–946.
