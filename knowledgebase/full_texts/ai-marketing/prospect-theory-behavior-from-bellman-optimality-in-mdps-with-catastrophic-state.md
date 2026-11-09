---
title: Prospect-Theory Behavior from Bellman Optimality in MDPs with Catastrophic States
url: https://arxiv.org/abs/2606.00970
category: ai-marketing
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Yujiao Chen
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.00970
pages: 12
chars: 35435
fetched_at: '2026-11-08T13:36:25+00:00'
kb_version: 1
---

# Prospect-Theory Behavior from Bellman Optimality in MDPs with Catastrophic States

Prospect-Theory Behavior from Bellman Optimality
in MDPs with Catastrophic States
Yujiao Chen
Massachusetts Institute of Technology
Cambridge, MA 02139, USA
yujiaoch@mit.edu
Abstract
We study risk-neutral control in Markov decision processes with an absorbing
catastrophic state. Even though rewards are linear and the agent has no utility cur-
vature, probability weighting, or framing dependence, standard Bellman optimality
produces three prospect-theory-like signatures: an S-shaped value-function profile
(convex near catastrophe, concave in the far field), an endogenous loss-sensitivity
coefficient λ∗(S)>1 , and a reflection-effect policy reversal. Across 495 parame-
ter configurations, the optimal policy plays safe near catastrophe in positive-drift
(growth) regimes despite the risky action’s higher immediate expected value, and
plays risky near catastrophe in negative-drift (decline) regimes despite the safe
action’s lower immediate expected loss. We derive a closed-form expression for
the asymptotic loss-aversion plateau ¯λ= lim S→∞ λ∗(S) that depends only on win
probability p, payoff asymmetry r=|∆ ℓ/∆w|, and discount factor β, and matches
numerical solutions to R2 = 0.999. The mechanism does not require asymmetric
payoffs. Across a sweep of (p, β)at three asymmetry levels, the asymmetry share
of ¯λ above unity has median 4.6% at r= 1.25 and rises to 13.9% at r= 2 ,
with the boundary contribution exceeding the asymmetry contribution in every
(p, β, r)cell tested. The phenomena persist under tabular Q-learning—a model-free
agent reproduces V ∗ at correlation 0.98 in growth and 1.00 in decline—and un-
der stochastic transitions with Gaussian, heavy-tailed Student-t3, and asymmetric
skew-normal noise up to 50% of the step size, where the asymptotic plateau tracks
the closed-form prediction within 0.41% for safe-channel noise and within 9.6%
for risky-channel or both-channel noise. These results identify absorbing failure
states as a sufficient structural mechanism for prospect-theory-like behavior under
optimal control.
1 Introduction
Sequential decisions made near absorbing failure states can produce strong asymmetries between
gains and losses even for risk-neutral agents. We formalize this observation in a Markov decision
process with linear rewards and an absorbing catastrophe boundary, and show that standard Bellman
optimality alone generates three prospect-theory-like signatures: an S-shaped value-function profile
(convex near catastrophe, concave in the far field), an endogenous loss-sensitivity coefficient, and
a reflection-effect policy reversal. The mechanism is purely dynamic: continuation values make
downside risk disproportionately consequential near irreversible failure, even when the agent has no
utility curvature, probability weighting, or framing dependence.
Prospect theory [Kahneman and Tversky, 1979, Tversky and Kahneman, 1992] documents three
robust patterns in human decision-making under risk: an S-shaped value function (concave for gains,
convex for losses); loss aversion (λ≈2.25 , so that losses loom roughly twice as large as equivalent
gains); and the reflection effect (risk aversion in gains, risk seeking in losses). These patterns are
Preprint.
arXiv:2606.00970v2  [cs.AI]  30 Jun 2026

typically interpreted as evidence for nonlinear preferences or distorted probability perception. We
do not argue that the present mechanism explains human behavior, nor do we claim to reproduce
prospect theory in full; probability weighting, framing, and reference dependence remain outside
the model. Our contribution is structural and normative—a class of environments in which prospect-
theory-like patterns are optimal under standard Bellman objectives—and is meant to sit alongside the
psychological accounts rather than displace them.
Consider a decision-maker choosing between a safe action (deterministic payoff ∆s) and a risky
action (win ∆w with probability p, lose ∆ℓ with probability 1−p). Two natural regimes arise. In
growth( E[risky]>∆ s >0 ), both actions improve the agent’s position, but risky offers higher
expected value. Indecline( E[risky]<∆ s <0 ), both actions deteriorate the agent’s position,
but safe deteriorates less. Local expected-value comparisons therefore favor risky in growth and
safe in decline. An absorbing catastrophe boundary, however, can invert these local rankings: the
continuation value depends on how close the agent is to irreversible failure, and that proximity can
outweigh the one-step expected payoff. Near catastrophe in growth, the agent may optimally lock in
smaller gains to avoid a large downside jump; near catastrophe in decline, the safe action only leads
to certain ruin more slowly, so optimal play may be to gamble. The same Bellman equation thus
produces risk aversion in gains and risk seeking in losses as a consequence of environment structure
alone. Catastrophe risk—an effectively absorbing threshold corresponding to outcomes like death,
bankruptcy, or exclusion—is the class of environments we focus on.
1.1 Contributions
1. Three prospect-theory signatures from Bellman optimality.Across 495 configurations, standard
Bellman optimality with linear rewards produces an S-shaped value-function profile in growth, state-
dependent loss sensitivity ( λ∗(S)>1 ), and a reflection-effect policy reversal across growth and
decline (Section 3).
2. The reflection effect arises from continuation values, not preferences.The Bellman-optimal
agent plays safe near catastrophe in growth despite risky’s higherimmediateexpected value, and
gambles near catastrophe in decline despite safe’s lowerimmediateexpected loss. The same agent
and objective yield opposite risk attitudes when environmental drift changes sign.
3. A closed-form formula for asymptotic loss aversion, with the boundary alone sufficient.
Theorem 1 gives ¯λ= (z −r −1)/(1−z) where z solves β[pz+ (1−p)z −r] = 1 ; Proposition 1
establishes scale invariance, and Proposition 2 proves ¯λ >1 for all r≥1 in growth. The formula
matches simulations at R2 = 0.999. Across a (p, β)×r sweep, the boundary contribution exceeds
the asymmetry contribution in every one of48cells tested (Section 4).
4. Robustness to learning and stochasticity.The theoretical phenomena survive tabular Q-learning
(correlation 0.98 in growth, 1.00 in decline) and stochastic transitions under Gaussian, heavy-tailed,
and asymmetric noise up to 50% of the step size, where the asymptotic plateau deviates from the
closed-form prediction by at most9.6%(Section 5).
1.2 Related work
Closest to our work are literatures on sequential decision-making with ruin or absorbing failure.Risk-
sensitive MDPs[Howard and Matheson, 1972, Borkar, 2002] modify the objective by introducing
nonlinear utility or exponential transforms; we keep a standard risk-neutral Bellman objective and
show that the environment alone induces prospect-theory-like behavior.Kelly criterion[Kelly, 1956]
and classical ruin analyses study survival and bet sizing under ruin but do not derive a state-dependent
loss-aversion coefficient or the joint appearance of an S-shaped value function and the reflection effect.
Ergodicity economics[Peters, 2019] emphasizes how absorbing losses and multiplicative dynamics
alter long-run growth, which is closely related in spirit, but does not characterize the geometry of V ∗
we study here.Evolutionary accounts[Robson, 2001, Hintze et al., 2015] argue that risk attitudes
can be adaptive but do not derive them as exact Bellman-optimal policies.Reference-dependent
models[K ˝oszegi and Rabin, 2006] take loss aversion as primitive; here a prospect-theory-like λ∗(S)
is endogenous.Safe RL[García and Fernández, 2015, Altman, 1999, Saunders et al., 2018] studies
absorbing failure states, constraints, and safety guarantees near catastrophe, but its emphasis is
typically on constraint satisfaction rather than the geometry of V ∗ and the behavioral signatures it
implies.
2

A growing empirical literature finds that the loss-aversion coefficient varies systematically with the
structure of the gamble. Meta-analyses by Brown et al. [2024] and Yechiam and Zeif [2025] report
that estimated λ depends on the gain/loss range used in elicitation; Walasek and Stewart [2015] show
experimentally that loss aversion can be attenuated or reversed by manipulating the symmetry of
the choice set; Yechiam and Hochman [2013] and Mukherjee et al. [2017] document attentional and
reference-point mechanisms tied to gamble structure rather than to a stable preference parameter; and
Gal and Rucker [2018] synthesize evidence against a universal 2:1 ratio. Our closed-form formula
(4) speaks directly to these patterns by isolating a boundary-induced contribution that is present
even at r= 1 and quantifying how intrinsic asymmetry adds to it. To our knowledge, no prior work
isolates a structural mechanism that jointly produces the S-shaped value-function profile, endogenous
loss aversion, and the reflection effect under standard Bellman optimality, and characterizes that
mechanism analytically.
2 Model
We study a catastrophe-boundary MDP with state spaceS={S cat, Scat+1, . . .}(the upper bound ¯S is
a computational truncation; all theoretical statements are for the semi-infinite extension with ¯S=∞ ).
Without loss of generality we fix Scat = 0. Two actions are available:safe(deterministic transition
S′ =S+ ∆ s) andrisky( S′ =S+ ∆ w with probability p, S′ =S+ ∆ ℓ with probability 1−p,
where ∆w >0>∆ ℓ). The state Scat is an absorbing catastrophe with V ∗(Scat) =V cat ≤0 . Rewards
are linear in the state increment, the discount factor is β∈(0,1) , and the agent is risk-neutral. The
Bellman optimality equation is
V ∗(S) = max n ∆s +β V∗(S+ ∆ s)| {z }
Q∗ safe(S)
, p

∆w +β V∗(S+ ∆ w)  + (1−p)  ∆ℓ +β V∗(S+ ∆ ℓ)  | {z }
Q∗ risky(S)
o
,
(1)
with V ∗(S) =V cat for S≤S cat. To quantify the asymmetry induced by the value function, we define
theendogenous loss sensitivityas the ratio of value drops to value gains,
λ∗(S) = |V ∗(S)−V ∗(S+ ∆ ℓ)| |V ∗(S+ ∆ w)−V ∗(S)| ,(2)
the MDP analogue of the prospect-theory loss-aversion coefficient λ. We emphasize that λ∗(S) is
a value-function slope ratio, not a utility ratio, and should not be interpreted as a direct estimate of
the psychological parameter λ; the comparison we draw is structural. Unlike a primitive preference
parameter, λ∗(S) is state-dependent: it varies across the state space, peaks near the policy boundary
in growth environments, and converges in the far field to ¯λ= lim S→∞ λ∗(S)>1.
We study two regimes:growth( E[risky]>∆ s >0 ), where both actions improve the agent’s state
but risky offers higher immediate expected value, anddecline( E[risky]<∆ s <0 ), where both
actions deteriorate the state but safe has lower immediate expected loss. A local one-step comparison
that ignores continuation values would therefore favor risky in growth and safe in decline. We show
that standard Bellman optimality with an absorbing boundary systematicallyoverturnsthese local
rankings near catastrophe. We solve the system by value iteration to tolerance 10−10 across 495
parameterizations organized into 14 experimental series (Appendix A).
3 Prospect-theory signatures from Bellman optimality
3.1 Growth environments: S-curve and endogenous loss aversion
In growth, near the catastrophe boundary, continuation values make the downside jump disproportion-
ately costly, so the Bellman-optimal agent chooses safe despite the risky action’s higher immediate
expected return. The resulting V ∗(S) is S-shaped—convex near catastrophe and concave in the far
field (Figure 1)—a consequence of the Bellman equation rather than an assumption. Three structural
features of the S-shape have closed-form explanations: a convex safe zone, a curvature kink at the
policy boundary|∆ ℓ|, and fading scallops in the far field.
Convexity in the safe zone (S <|∆ℓ|).Within the safe zone, the agent takes the safe action at
every state, so V ∗ satisfies the recurrence V ∗(S) = ∆s +β V∗(S+ ∆ s). Telescoping from state S
3

Figure 1:Growth environment: Bellman-optimal caution near catastrophe( ∆s = +1, ∆w =
+24, ∆ℓ =−30 , p= 0.65 , β= 0.95 , Vcat =−100 ).Left:value-function profile V ∗(S), convex near
catastrophe and concave far away.Center: λ∗(S) plateaus at ≈2.23 .Right:the agent voluntarily
plays safe for 30 states (=|∆ ℓ|) even though the risky action has higher immediate expected value.
to the safe-zone edge yields
V ∗(S) = ∆s(1−β d) 1−β +β d V ∗(S+d∆ s), d=  |∆ℓ| −S ∆s  ,(3)
where d is the number of safe steps required to exit the safe zone. (When ∆s divides |∆ℓ| −S—in
particular for ∆s = 1, as in our figures—S+d∆ s =|∆ ℓ| exactly.) Because the risky zone offers
far higher growth (E[risky]≫∆ s), we have V ∗(S+d∆ s)≫∆ s/(1−β) , and the dominant term
βd V ∗(S+d∆ s) is convex in S: each step toward the risky zone is exponentially more valuable
than the last, since the high-return risky action is one fewer discounted step away.
Curvature kink at S=|∆ ℓ|.At this threshold, the risky action’s loss outcome S+ ∆ ℓ transitions
from landing inside the catastrophe region (S+ ∆ ℓ ≤S cat for S <|∆ℓ|) to landing strictly above it
(S+ ∆ ℓ > Scat for S >|∆ℓ|). Below |∆ℓ|, each risky loss is catastrophic, creating the steep convex
escape ramp. Strictly above |∆ℓ|, the loss outcome has finite value, and diminishing returns from
distance dominate—the curve bends concave. The transition is a discrete change in loss consequences
manifest as a finite jump in the discrete second difference ∆2V ∗(S) =V ∗(S+1)−2V ∗(S) +
V ∗(S−1) at S=|∆ ℓ|, where the optimal action switches from safe to risky. We refer to this
policy-boundary discontinuity as the S-curve’s “inflection” for brevity.
Scalloping in the far field.In the risky zone, V ∗(S) depends on V ∗(S+ ∆ ℓ) through the Bellman
equation. As S crosses each multiple k|∆ℓ|, the loss destination S+ ∆ ℓ = (k−1)|∆ ℓ| crosses
a boundary where V ∗ has a curvature discontinuity inherited from the previous generation. At
S=k|∆ ℓ|, catastrophe is reachable in exactly k consecutive losses (probability (1−p)k), so each
additional |∆ℓ| of distance adds one more “loss buffer.” The amplitude of these scallops decays
geometrically: the concavity spike at the k-th multiple is attenuated by a factor of ρ|∆ℓ| =z r per
generation, where z∈(0,1) is the unique decaying root of the characteristic equation derived in
Section 4. For the baseline (p= 0.65 , β= 0.95 , r= 1.25 ), this gives zr ≈0.53 , in good agreement
with the empirically measured ratios of consecutive V ′′ peaks. The scallops fade into the smooth
concave far field.
The S-shape directly induces an endogenous loss asymmetry. The loss sensitivity λ∗(S) peaks near
the safe-zone boundary and settles to a plateau ¯λ >1 in the far field (Figure 1, center). The numerical
value depends on (p, β, r); the closed-form Section 4 identifies the boundary-induced contribution
that is present even atr= 1.
3.2 Decline environments: the hail Mary effect
In decline (E[risky]<∆ s <0 ), both actions deteriorate the state, but safe has lower immediate
expected loss. A local comparison therefore favors safe. Near catastrophe, however, the Bellman-
optimal policy reverses: the safe action is no refuge because it leads to certain ruin only more slowly,
so the agent gambles because a risky win is the only action that can push catastrophe further into the
future, and discounting makes deferred catastrophe strictly preferable. We refer to this as thehail
Maryeffect (risk-seeking-near-ruin); it parallels risk seeking in losses from prospect theory. Because
4

Figure 2:Decline environment: the hail Mary effect( ∆s =−16 , ∆w = +30 , ∆ℓ =−50 ,
p= 0.40 , β= 0.95 , Vcat =−100,000 ).Left:staircase-shaped V ∗(S).Center:periodic λ∗(S).
Right:the agent gambles desperately in the 16 states nearest catastrophe—risk seeking in losses. A
local expected-loss comparison would favor safe, yet the Bellman-optimal policy gambles.
both actions have negative expected drift, the absorbing boundary is reached with probability one
under any policy [Puterman, 1994]; the optimal policy maximizes expected discounted reward by
delaying—not escaping—ruin. In all 69 decline configurations tested, the states nearest catastrophe
arealwaysrisky.
Unlike in growth, an S-curve does not arise in decline. Instead, V ∗ is a concave staircase (Figure 2).
Two structural differences from growth explain this pattern.
No convex region.In growth, convexity arose because the safe zone acted as a discounted approach
ramp to the high-value risky zone (equation 3). In decline, the near-boundary zone is instead the
hail Mary region, where the agent takes theriskyaction. The risky action’s value near catastrophe is
dominated by the constant catastrophe penalty: Q∗ risky(S) =p[∆ w +β V∗(S+ ∆ w)] + (1−p)[∆ℓ +
β Vcat]. Since Vcat is a fixed constant, V ∗(S) near the boundary varies only through V ∗(S+ ∆ w),
which changes slowly becauseS+∆ w sits far from catastrophe. There is no exponential amplification
as in the growth safe zone, so no convexity appears.
Staircase at |∆s| intervals.Away from the boundary, the agent takes the safe action, which jumps
|∆s| states toward catastrophe. This creates a modular recurrence, V ∗(S) = ∆s +β V∗(S− |∆s|),
linking every state to the one |∆s| steps closer. At every multiple of |∆s|, the safe-action destination
crosses a policy boundary inherited from the hail Mary region, producing a sharp rise followed by
a flat plateau—the staircase. The step height decays by exactly β per period, producing overall
concavity: the marginal value of distance from catastrophe diminishes as βk, so V ∗ has a concave
envelope.
3.3 The reflection effect is optimal policy switching
The same Bellman equation and the same risk-neutral objective produce opposite risk attitudes
depending on environmental drift, overturning opposite local action rankings in the two regimes:
Local benchmarkBellman-optimal policyPT analogue
Growth (E[risky]>∆ s >0) Risky everywhereSafe near boundaryRisk aversion in gains
Decline (E[risky]<∆ s <0) Safe everywhereRisky near boundaryRisk seeking in losses
This is the reflection effect as a property of continuation values rather than preference curvature.
4 A closed-form formula for asymptotic loss aversion
The loss sensitivity λ∗(S) is not constant: it spikes near the safe-zone boundary and decays to an
asymptotic plateau ¯λ in the far field. We derive a closed-form expression for this terminal value,
validate it numerically, and then use it to decompose ¯λ into a boundary contribution (the symmetric
case) and an asymmetry contribution.
5

Theorem 1(Closed-form asymptotic loss aversion).Under the model of Section 2 and the growth
conditionE[risky]>∆ s >0, the limit ¯λ= lim S→∞ λ∗(S)exists and satisfies
¯λ= z−r −1 1−z , β  p z+ (1−p)z−r = 1, z∈(0,1),(4)
wherer=|∆ ℓ|/∆w andzis the unique root of the characteristic equation in(0,1).
Proof. Far-field optimality of risky.As S→ ∞, V ∗(S)→V ∞ :=E[risky]/(1−β) (the boundary-
free value of always playing risky). Hence Q∗ risky(S)−Q ∗ safe(S)→E[risky]−∆ s >0 by the growth
hypothesis, so risky is uniquely optimal for allSbeyond someS 0.
Linear recurrence.Define u(S) =V ∞ −V ∗(S)≥0 . For S≥S 0, the Bellman equation reduces to
u(S) =β[p u(S+ ∆ w) + (1−p)u(S+ ∆ ℓ)], a linear homogeneous recursion with non-negative
coefficients.
Characteristic equation and unique decaying real root.The exponential ansatz u(S) =Cρ S yields
f(ρ) :=β[pρ ∆w + (1−p)ρ ∆ℓ ] = 1. Each summand ρa is convex for a a positive integer or a <0
(so a(a−1)≥0 ), hence f is convex on ρ >0; it diverges as ρ→0 + and as ρ→ ∞, and equals
β <1atρ= 1. Thereforefcrosses1exactly once in(0,1), at a unique real rootρ ∗ ∈(0,1).
Dominant-mode asymptotics.The recursion is a finite-span linear difference equation with strictly pos-
itive coefficients. By standard renewal-theoretic / Perron-root asymptotics for such recurrences [e.g.,
Feller, 1971, Ch. XI], any non-negative solution that decays to zero is asymptotically proportional to
the minimal positive real root of the characteristic equation. Hence
u(S)∼C(ρ ∗)S
for someC >0, whereρ ∗ ∈(0,1)is the unique root identified above.
Limit existence and value.From u(S)∼C(ρ ∗)S, the ratios u(S+ ∆ w)/u(S)→(ρ ∗)∆w and
u(S+ ∆ ℓ)/u(S)→(ρ ∗)∆ℓ. Substituting into λ∗(S) = (u(S+ ∆ ℓ)−u(S))/(u(S)−u(S+ ∆ w))
yields λ∗(S)→((ρ ∗)∆ℓ −1)/(1−(ρ ∗)∆w ). The substitution z= (ρ ∗)∆w ∈(0,1) , with r=
|∆ℓ|/∆w giving(ρ ∗)∆ℓ =z −r, produces the displayed expression.
Proposition 1(Scale invariance). ¯λdepends on(∆ w,∆ ℓ)only through the ratior=|∆ ℓ|/∆w.
Proof. The substitution z=ρ ∆w rewrites both the characteristic equation and the formula for ¯λ in
Theorem 1 purely in terms of(p, β, r).
Proposition 2(Loss aversion always emerges for r≥1 ).Under the assumptions of Theorem 1 and
r≥1, ¯λ >1strictly.
Proof. By Theorem 1, ¯λ >1⇐ ⇒z−r −1>1−z⇐ ⇒z −r +z >2 . For z∈(0,1) , AM–GM
givesz −1 +z >2strictly. Forr >1andz∈(0,1),z −r > z−1, soz −r +z >2a fortiori.
Validation.Equation (4) achieves R2 = 0.999 against the simulated ¯λ plateaus from all 343
growth-environment value iteration solutions, with median relative error 0.14%. Four controlled
experiments (Figure 3) isolate the role of each parameter.Discount factor β (panel a): lower β raises
¯λ, because risky-loss steps put catastrophe within one or two periods (its near-term contribution to
V ∗ is barely discounted), while risky-win steps yield payoff that accrues over manyfutureperiods of
continued play (all discounted by powers of β); impatience downweights the gain-side flow faster
than the loss-side catastrophe penalty, raising the slope ratio.Win probability p (panel b), varied
via payoff spread at fixed r and E[risky], is the dominant driver: ¯λ is monotonic in p, collapsing
toward unity as p→0.5 + and diverging as p→1 .Asymmetry ratio r (panel c) adds to the boundary
contribution; evenr <1produces ¯λ >1whenp > r/(1 +r).Joint payoff scaling(panel d) leaves
¯λ invariant, confirming Proposition 1. Probability structure (p, β)thus drives ¯λ; payoff magnitude
does not.
6

Figure 3:Parameter sensitivity of V ∗(S) (top) and λ∗(S) (bottom).Each column isolates one
degree of freedom.(a)Discount factor β.(b)Payoff spread at fixed r= 1 , E[risky] = 5: as p→0.5 ,
¯λfalls.(c)Asymmetry ratior: ¯λscales withr; evenr <1yields ¯λ >1.(d)Scale invariance.
4.1 Symmetric vs. asymmetric gambles
Theorem 1 yields a clean decomposition of¯λ into aboundary contribution, present even for symmetric
payoffs, and anasymmetry contribution, introduced byr >1. Define
¯λsym(p, β) :=¯λ(p, β, r=1), σ(p, β, r) := ¯λ(p, β, r)−¯λsym(p, β) ¯λ(p, β, r)−1 ,(5)
the asymmetric plateau and the asymmetry share, respectively. The numerator is the increment from
the symmetric to the asymmetric case at fixed (p, β); the denominator normalizes by the gap above
unity, soσmeasures the fraction of ¯λ−1attributable tor >1.
Symmetric case (boundary alone).For r= 1 , eq. (4) reduces to ¯λsym = 1/z∗, where z∗ ∈(0,1)
solves β[pz+ (1−p)/z] = 1 . By Proposition 2, ¯λsym >1 throughout the symmetric growth regime
(p >1/2 ). Worked values at β= 0.95 : 1.55 at p= 0.55 , 2.14 at p= 0.65 , 4.34 at p= 0.80 ,
diverging as p→1 . So an absorbing boundary applied to a perfectly symmetric risky/safe choice
already produces a slope ratio of similar order to the empirical prospect-theory estimate λ≈2.25
[Tversky and Kahneman, 1992]—no preference or payoff asymmetry required.
Asymmetric case (boundary plus asymmetry).For r >1 , ¯λ rises further. Table 1 re-
ports descriptive statistics for σ swept over p∈ {0.55,0.60,0.65,0.70,0.75,0.80} and β∈
{0.85,0.90,0.95,0.99}at three asymmetry levels (growth-feasible cells only).
Table 1: Asymmetry shareσ(eq. 5) across the(p, β)grid, by asymmetry levelr.
r nmedianσmeanσIQR range
1.25 20 4.6% 5.8% [2.6%,8.7%] [0.4%,13.5%]
1.50 16 8.3% 8.9% [5.1%,12.8%] [0.9%,18.6%]
2.00 12 13.9% 14.7% [10.1%,20.4%] [2.2%,26.5%]
In every one of the48 (p, β, r)cells tested, the boundary contribution ¯λsym −1 exceeds the asymmetry
contribution ¯λ− ¯λsym. The asymmetry share grows monotonically with r but stays below 30% even
at r= 2 . The boundary therefore dominates ¯λ across realistic parameters and across small to large
asymmetry.
Connection to behavioral-economics empirics.This decomposition matches an empirical pattern.
Walasek and Stewart [2015] show experimentally that estimated λ can be tuned from below unity
to well above two by manipulating the symmetry of the choice set, and meta-analyses by Brown
et al. [2024] and Yechiam and Zeif [2025] document the same dependence in observational data.
Equation (4) implies that, in any sequential setting with absorbing failure, effective loss aversion
7

0 20 40 60 80 100 120
State (S)
30
40
50
60
70
80
90
100
110Value
Growth: Value Function
(corr=0.980)
Exact V * (s)
Q-learning V(s)
0 20 40 60 80 100 120
State (S)
Safe
RiskyPolicy
Growth: Policy
(agreement: 84.1%)
Exact: Safe
Exact: Risky
Q-learning: Safe
Q-learning: Risky
0 20 40 60 80 100 120
State (S)
0
2
4
6
8
10
12
Loss Sensitivity (s)
Growth: Loss Sensitivity
Exact * (s)
Q-learning (s)
Exact mean=2.396
Q-learning mean=2.703
0 20 40 60 80 100 120
State (S)
80000
60000
40000
20000
0
Value
Decline: Value Function
(corr=1.000)
Exact V * (s)
Q-learning V(s)
0 20 40 60 80 100 120
State (S)
Safe
RiskyPolicy
Decline: Policy
(agreement: 89.4%)
Exact: Safe
Exact: Risky
Q-learning: Safe
Q-learning: Risky
0 20 40 60 80 100 120
State (S)
0
2
4
6
8
10
12
Loss Sensitivity (s)
Decline: Loss Sensitivity
Exact * (s)
Q-learning (s)
Exact mean=2.076
Q-learning mean=1.935
Figure 4:Q-learning reproduces all phenomena.Top:growth (correlation 0.980).Bottom:decline
(correlation 1.000). A model-free agent discovers the same S-shape, loss aversion, and policy
structure.
has a boundary-induced component determined by (p, β)to which payoff asymmetry r adds further;
controlled symmetric gambles isolate the boundary, and asymmetric gambles measure the additional
contribution.
5 Robustness
The theoretical claims so far were established under exact value iteration with deterministic transitions.
We now show that they survive (i) a model-free agent with no knowledge of the transition kernel, and
(ii) stochastic transitions whose distribution and channel of action we vary.
5.1 Tabular Q-learning
A tabular Q-learning agent (ϵ-greedy with constant ϵ= 0.5 ; learning rate α= 0.01 ; 5×10 5 episodes;
max 2,000 steps per episode; optimistic Q-initialization at max(E[risky],∆ s)/(1−β) ; uniform
random start state; episode terminates on entering Scat) with no knowledge of the transition model
reproduces all qualitative features (Figure 4). On the canonical Figure 1 growth and Figure 2 decline
configurations with ¯S= 1000 , Pearson correlation between V Q and V ∗ is 0.980 in growth and 1.000
in decline. The S-shape, safe zone, hail Mary region, and λ∗ >1 all emerge from learning rather
than from exact computation. We treat Q-learning as a qualitative reproduction of the mechanism;
the closed-form formula (4) remains the recommended estimator when the transition model is known.
The reproduction is bundled in the supplementary archive ( code/run_qlearning_figure.py);
each configuration runs in approximately30seconds on a single CPU.
5.2 Stochastic transitions
To check that the prospect-theory signatures do not depend on the deterministic transition model
in (1), we perturb each transition’s destination by additive integer-valued noise on the asymmetric
baseline (p= 0.65 , β= 0.95 , r= 1.25 , ∆w = 8, ∆ℓ =−10 , ∆s = 1, Vcat =−100 ; closed-form
prediction ¯λcf ≈2.23 ). The integer state space is preserved by distributing probability mass over
neighboring states: for nominal destination S+ ∆ a +ξ with ξ∼F σ, the discrete transition kernel
is P(S ′′) =F σ(S′′ + 0.5)−F σ(S′′ −0.5) , truncated and renormalized. We sweep three noise
families—Gaussian N(0, σ2), heavy-tailed Student- t3 rescaled to match Gaussian variance, and
asymmetric skew-normal (α= 2 , variance-matched, zero-mean)—applied to (a) the safe action only,
(b) risky only, or (c) both, withσ∈ {0,0.10,0.25,0.50} · |∆ℓ|.
8

Table 2 reports the maximum relative deviation of ˆ¯λ from the noiseless closed-form prediction across
the σ sweep. Three patterns hold across all three noise distributions: (1) safe-channel noise alone
leaves ¯λ essentially unchanged (≤0.41% even at σ= 0.5|∆ ℓ|); (2) risky-channel noise (alone or
combined with safe) reduces ¯λ monotonically, by at most 9.6% at σ= 0.5|∆ ℓ|; (3) the qualitative
S-shape, hail Mary region, and policy boundary are unchanged at every noise level. Qualitative
behavior is invariant to the noise distribution; the quantitative plateau varies modestly (within ≈10%
at the largest noise level), and the difference between Gaussian, heavy-tailed, and asymmetric noise
is small.
Table 2: Maximum relative deviation of ˆ¯λ from the closed-form prediction ¯λcf ≈2.23 across
σ∈ {0,0.10,0.25,0.50} · |∆ℓ|. Asymmetric baseline (p= 0.65,β= 0.95,r= 1.25).
Noise distribution Safe only Risky only Both
Gaussian0.36% 9.54% 9.57%
Student-t3 (heavy-tailed)0.41% 9.00% 8.98%
Skew-normal (asymmetric,α= 2)0.38% 9.35% 9.30%
6 Discussion
We have shown that an absorbing catastrophe boundary is structurally sufficient for three prospect-
theory-like signatures to emerge under standard Bellman optimality, with linear rewards and no
preference asymmetry. The claim is one of sufficiency, not exclusivity: probability weighting,
framing, and reference dependence may still play independent roles in human behavior, and we do
not argue that observed human loss aversion is itself optimal. The mechanism extends from literal
catastrophes (bankruptcy, extinction) to effectively absorbing psychological or institutional thresholds
[K˝oszegi and Rabin, 2006]. The decomposition in Section 4.1 aligns with empirical evidence that
measured loss aversion varies with payoff asymmetry [Brown et al., 2024, Yechiam and Zeif, 2025,
Walasek and Stewart, 2015, Gal and Rucker, 2018, Yechiam and Hochman, 2013, Mukherjee et al.,
2017]: ¯λ has a boundary-induced component determined by (p, β)and an asymmetry component
that depends on r, rather than a fixed psychological constant. For reinforcement learning, the result
implies that conservative or desperate behavior near absorbing failure can emerge from continuation
values alone, with no need to hand-code “safe” behavior into the agent’s preferences.
Limitations and broader impact.The model is one-dimensional with binary actions, known
transitions, and a single boundary; probability weighting, framing, and the endowment effect are
outside its scope, and the analogy between sequential MDP decisions and one-shot gambles is
structural rather than literal. Empirical validation requires environments whose forward-looking drift
can be experimentally manipulated; we leave this and extensions to higher dimensions, continuous
actions, partial observability, and deep RL to future work. Recognizing that risk-seeking or risk-averse
behavior near irreversible failure can be rational rather than pathological may inform safety-constraint
design for RL systems and help interpret loss-averse human choices in high-stakes settings; we see
no direct negative societal impact specific to this work.
References
E. Altman.Constrained Markov Decision Processes. Chapman and Hall/CRC, 1999.
V . S. Borkar. Q-learning for risk-sensitive control.Mathematics of Operations Research, 27(2):294–
311, 2002.
A. L. Brown, T. Imai, F. Vieider, and C. F. Camerer. Meta-analysis of empirical estimates of loss
aversion.Journal of Economic Literature, 62(2):485–516, 2024.
W. Feller.An Introduction to Probability Theory and Its Applications, Vol. II. John Wiley & Sons,
2nd edition, 1971.
D. Gal and D. D. Rucker. The loss of loss aversion: Will it loom larger than its gain?Journal of
Consumer Psychology, 28(3):497–516, 2018.
9

J. García and F. Fernández. A comprehensive survey on safe reinforcement learning.Journal of
Machine Learning Research, 16:1437–1480, 2015.
A. Hintze, R. S. Olson, C. Adami, and R. Hertwig. Risk sensitivity as an evolutionary adaptation.
Scientific Reports, 5:8242, 2015.
R. A. Howard and J. E. Matheson. Risk-sensitive Markov decision processes.Management Science,
18(7):356–369, 1972.
D. Kahneman and A. Tversky. Prospect theory: An analysis of decision under risk.Econometrica,
47(2):263–291, 1979.
J. L. Kelly. A new interpretation of information rate.Bell System Technical Journal, 35(4):917–926,
1956.
B. K ˝oszegi and M. Rabin. A model of reference-dependent preferences.Quarterly Journal of
Economics, 121(4):1133–1165, 2006.
S. Mukherjee, A. Sahay, V . S. Pammi, and N. Srinivasan. Is loss-aversion magnitude-dependent?
Measuring prospective affective judgments regarding gains and losses.Judgment and Decision
Making, 12(1):81–89, 2017.
O. Peters. The ergodicity problem in economics.Nature Physics, 15(12):1216–1221, 2019.
M. L. Puterman.Markov Decision Processes. John Wiley & Sons, 1994.
A. J. Robson. The biological basis of economic behavior.Journal of Economic Literature, 39(1):11–
33, 2001.
W. Saunders, G. Sastry, A. Stuhlmüller, and O. Evans. Trial without error: Towards safe RL via
human intervention. InAAMAS, 2018.
A. Tversky and D. Kahneman. Advances in prospect theory: Cumulative representation of uncertainty.
Journal of Risk and Uncertainty, 5(4):297–323, 1992.
L. Walasek and N. Stewart. How to make loss aversion disappear and reverse: Tests of the decision-
by-sampling origin of loss aversion.Journal of Experimental Psychology: General, 144(1):7–11,
2015.
E. Yechiam and G. Hochman. Losses as modulators of attention: Review and analysis of the unique
effects of losses over gains.Psychological Bulletin, 139(2):497–518, 2013.
E. Yechiam and D. Zeif. Loss aversion is not robust: A re-meta-analysis.Journal of Economic
Psychology, 107:102801, 2025.
10

A Complete parameter summary
Table 3: Organization of 495 configurations across 14 experimental series.
Series Description Qty Key variables Primary finding
1 Ratio sweep 15|∆ ℓ/∆w|λ ∗ scales withr
2 Symmetric payoffs 15r= 1.0,β,ELoss aversion without asymmetry
3A–C Beta sweep 57βMonotone decrease
4V cat locality 12V cat Zero effect on plateau
5 State space 8 ¯SStable for ¯S≥200
7 Drift sweep 10∆ s Phase transition
8 Phase transition 15∆ s =E[risky]Sharp discontinuity
9–10 Loss/Win sweep 30∆ ℓ,∆ w Validates ratio scaling
11 Probability sweep 15pVia expected payoff
17 Heatmaps 175β×r,∆ s ×rInteraction effects
18E[risky]sweep 33E[risky]Secondary effect
19–20 Interaction 110E×r,E×βSeparable contributions
Total–495– –
B Value iteration algorithm
Algorithm 1:MDP value iteration.
Input:(S cat, ¯S, Vcat,∆ s,∆ w,∆ ℓ, p, β, ϵ)
Output:V ∗,π ∗,λ ∗
1. InitializeV(S)←0forS > S cat;V(S cat)←V cat.
2.Repeat:
Vold ←V
ForS=S cat + 1to ¯S:
Q∗ safe ←∆ s +β·V old(clamp(S+ ∆ s, Scat, ¯S))
Q∗ risky ←p[∆ w +β·V old(clamp(S+ ∆ w, Scat, ¯S))] + (1−p)[∆ℓ +β·V old(clamp(S+ ∆ ℓ, Scat, ¯S))]
V(S)←max(Q ∗ safe, Q∗ risky)
Until∥V−V old∥∞ < ϵ.
3. Extractπ ∗(S) = arg max(Q∗ safe, Q∗ risky)andλ ∗(S)via (2).
where clamp(x,lo,hi) = min(max(x,lo),hi).
C Additional figures
11

Figure 5:Robustness to stochastic transitions.Safe-zone width, hail Mary zone width, and λ∗ are
virtually unchanged from 0% to 50% Gaussian noise on transitions. Section 5.2 extends this analysis
to heavy-tailed and asymmetric noise distributions and to per-channel sweeps; the quantitative
summary is in Table 2.
12
