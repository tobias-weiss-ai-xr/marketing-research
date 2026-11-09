---
title: 'Signed Exposure: Fair Routing of Algorithmic Attention When Attention Can Harm'
url: https://arxiv.org/abs/2609.29513
category: digital-marketing
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Daria Leshchikova
- Valentina V. Kuskova
- Dmitry Zaytsev
- Valerii Klimov
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.29513
pages: 12
chars: 41440
fetched_at: '2026-11-08T13:21:06+00:00'
kb_version: 1
---

# Signed Exposure: Fair Routing of Algorithmic Attention When Attention Can Harm

Leshchikova et al., 2027
SIGNEDEXPOSURE: FAIRROUTING OFALGORITHMIC
ATTENTIONWHENATTENTIONCANHARM
Daria Leshchikova
Fleamily, Inc
Wilmington, DE, USA
Valentina V . Kuskova & Dmitry Zaytsev
Lucy Family Institute for Data & Society
University of Notre Dame
Notre Dame, IN, USA
Valerii Klimov
Fleamily, Inc
Wilmington, DE, USA
ABSTRACT
Fairness-of-exposure treats algorithmic attention as a good to be distributed eq-
uitably. But when an autonomous agent initiates contact, attention issigned: it
delivers value to a willing receiver and imposes burden on an unwilling one. We
formalize routing under signed exposure and show that a fair distribution of atten-
tion need not be a fair distribution ofunwantedattention. Our central result is an
incompatibility: within signed-exposure routing, exposure parity (equal contact
rates across groups) and burden parity (equal unwanted-contact rates) generically
cannot hold at once, and the two are separated by a band that widens as rout-
ing grows more selective. A second result shows measurement error is itself a
fairness mechanism: group-differential noise in receptivity scores simultaneously
inflates a group’s exposure and degrades whom it selects, so an apparent exposure-
fairness gain is a hidden burden transfer. Calibrating to a public dating-platform
survey (n=2,499) that, to our knowledge, uniquely measures receive-side recep-
tivity to conversational agents, we find exposure parity costs only0.2–2.3%of
yield yet moves the per-capita burden ratio to1.7×: the tension is between fair-
ness notions, not between fairness and efficiency. Finally, the burden-parity policy
is computable by bisection and learnable online: a plug-in learner recovers it at a
2.3%empirical regret premium. The operative design choice in signed-exposure
markets is not efficiency versus fairness butwhichfairness.
1 INTRODUCTION
Autonomous agents that converse on a user’s behalf are moving into matching platforms, messaging
products, and outreach tools. Wherever they ship, a routing policy decides who receives machine-
initiated contact. The fairness literature has a well-developed answer for allocation problems of this
shape: treat exposure as a scarce good and distribute it equitably (Singh & Joachims, 2018; Biega
et al., 2018). That answer carries a premise so natural it is rarely stated: that being selected is good
for the selected. For algorithmic attention the premise fails. A person who welcomes agent-mediated
contact receives value from being routed to; a person who does not receives an unwanted machine
solicitation. Exposure issigned, and its sign is the receiver’s own willingness. A fair distribution
of attention, then, need not be a fair distribution ofunwantedattention; and, we show, it generically
cannot be both.
This would be a philosophical quibble if willingness were uniform or idiosyncratic. It is neither.
In a public microdataset that, to our knowledge, uniquely measures receive-side receptivity to con-
versational agents (a bilingual survey of2,499active users of a dating platform, released with full
psychometric documentation (Leshchikova et al.)), willingness to engage another person’s agent
varies widely across individuals and systematically across groups: women’s receive receptivity sits
0.30standard deviations below men’s. Any routing policy therefore chooses, implicitly or explicitly,
1
arXiv:2609.29513v1  [cs.CY]  25 Aug 2026

Leshchikova et al., 2027
both a distribution of algorithmic attention and a distribution of its unwanted residue, and the two
cannot be chosen independently.
We formalize routing in signed-exposure markets and characterize what fairness can and cannot
mean there. Four results.(i)The yield–parity frontier is nearly flat: equalizing group exposure rates
costs0.2–2.3%of engagement yield in the data, because the frontier’s slope depends onmarginal,
not mean, group receptivity (Proposition 1). The efficiency-versus-fairness framing is empirically
vacuous here.(ii)What is not vacuous is the choice between fairness notions: exposure parity
and burden parity are generically incompatible (Theorem 2). Equalizing who receives attention
forces the lower-receptivity group deeper into its own distribution, so equalized exposure arrives
with a1.7×per-capita burden ratio; an explicit band of exposure ratios separates the two pari-
ties, and it widens as routing becomes more selective.(iii)Measurement error is itself a fairness
mechanism (Theorem 3): group-differential noise in receptivity scores simultaneously inflates the
noisier group’s exposure and degrades whom it selects, so an apparent exposure-fairness gain is in
substance a burden transfer. No pooled score transformation escapes this: group-blind transforma-
tions are provably inert, and posterior-mean shrinkage fails on the opposite margin from raw scores
(Proposition 4). The noise itself we measure rather than assume: the released model’s posterior
standard deviations show near-equity by gender and a7.5%differential by language form.(iv)Con-
strained optima are computable by bisection after sorting (Proposition 5), and the constraint survives
learning: a plug-in learner that estimates its own burden-parity constraint from feedback converges
to parity at a2.3%empirical regret premium (30 seeds), while unconstrained exploration transiently
over-burdens the lower-receptivity group exactly as the static noise theory predicts (Proposition 6).
The practical upshot inverts the usual fairness conversation. Platforms deploying agent routing do
not face a painful efficiency–fairness trade-off; they face a value choice between two parities that
cannot coexist, with an efficient algorithm for any point on the menu, one thatlearnsthe burden-
parity point from feedback when propensities are unknown. They also face a measurement-equity
audit obligation, since unequal score precision quietly redistributes burden even under nominally
fair allocation. These conclusions bear on disclosure and opt-in policy, on the auditing of scoring
systems, and on any learning system whose exploration imposes contact on people who did not ask
for it.
2 RELATED WORK
Fairness of exposure in ranking and recommendation.The allocation of attention as a fairness
object originates in fair top-kranking (Zehlike et al., 2017) and matures into exposure-based formu-
lations: Singh & Joachims (2018) allocate expected exposure across items in proportion to merit,
Biega et al. (2018) amortize individual exposure over ranking sequences, Diaz et al. (2020) make
expected exposure the evaluation target itself, and deployed systems operationalize demographic
exposure constraints at scale (Geyik et al., 2019). Dynamic and two-sided extensions control expo-
sure under learned relevance (Morik et al., 2020) and balance producer against consumer interests
(Patro et al., 2020; S¨uhr et al., 2019); Zehlike et al. (2022) survey the area. Throughout this literature
exposure is a good: more of it benefits the exposed, and fairness means distributing it. Our setting
breaks the premise: exposure carries the sign of the receiver’s willingness, and Theorem 2 shows
that once exposure is signed, its equitable distribution and the equitable distribution of its harms are
generically incompatible objectives rather than one objective seen twice.
Impossibility results in algorithmic fairness.Sharp incompatibilities between fairness criteria are
foundational for classification: calibration cannot coexist with balanced error rates under unequal
base rates (Kleinberg et al., 2017; Chouldechova, 2017), and different worldviews about measure-
ment provably demand different mechanisms (Friedler et al., 2021). This incompatibility, specific
to signed-exposure routing rather than a claim across all mechanisms, differs from the classification
impossibilities in locus and driver. It attaches to theallocationlayer rather than to properties of a
predictor; it is driven by first-moment differences in group receptivity rather than base rates; and it
is quantitative rather than binary: the incompatible parities are separated by an explicit band(r ∗,1)
whose width is a comparative static in the routing budget, collapsing as selectivity relaxes.
Fairness and measurement.A second foundational line locates fairness failures in measurement
itself: proxy label choice misallocates care at scale (Obermeyer et al., 2019), unmodeled constructs
undermine fairness claims (Jacobs & Wallach, 2021), and noisy labels distort fairness evaluation
2

Leshchikova et al., 2027
(Fogliato et al., 2020). Closest to our Theorem 3 are selection models with group-dependent score
distortion: multiplicative implicit bias in estimates (Kleinberg & Raghavan, 2018) and, especially,
group-differential estimationvariance, which alters who clears a selection bar (Emelianov et al.,
2020). We extend this line in three directions: the selection externality is two-sided (noise moves a
group’s exposure and its burden in the same direction, Theorem 3(iii)); the shrinkage escape route
is closed (posterior-mean and raw-score routing fail on opposite margins, Proposition 4); and the
noise quantities are measured rather than assumed: group-specific psychometric posteriors from the
released measurement model, showing near-equity by gender and a7.5%language differential.
Fair sequential allocation.Meritocratic fairness in bandits (Joseph et al., 2016) constrains which
arms may be preferred during learning; constrained exploration more broadly is formalized through
bandits with knapsacks (Badanidiyuru et al., 2018). Our Proposition 6 constrains a different object:
not the meritocracy of selection but the distribution of exploration’sexternality, the burden that
uncertain routing imposes on unwilling receivers. Our experiments show unconstrained learning
transiently misallocates exactly this quantity, in the direction the static noise theory predicts.
Reciprocal matching and agentic systems.Reciprocal recommendation conditions relevance on
both sides’ preferences (Palomares et al., 2021), and two-sided marketplace fairness balances stake-
holder groups (S ¨uhr et al., 2019; Patro et al., 2020); autonomous conversational agents sharpen
the receive side into a first-class design surface, since the routed object now initiates interaction
rather than awaiting it. Prior two-sided work thus already recognizes that exposure and utility can
diverge; what it does not model is unwanted, algorithmicallyinitiatedcontact as a receiver-side neg-
ative externality, and it does not characterize the resulting exposure–burden parity geometry or its
interaction with estimation uncertainty. Those are the contributions here. We build on the public
receptivity dataset of Leshchikova et al., whose released propensities and measurement diagnostics
supply our calibration and, to our knowledge among the few public sources of ground truth for
receive-side willingness toward agent-mediated contact.
3 SETUP
A unit mass of receivers is partitioned into groupsg∈ {A, B}with population sharesπ g. Each
receiverjhas anengagement propensitye j ∈[0,1]: the probability that an algorithmically routed
contact is welcome. Within groupg, propensities follow distributionF g with survival quantile func-
tionQ g(t)(thet-th upper quantile) andtop-mean function
mg(t) =E[e|e≥Q g(t)]t∈(0,1],
the mean propensity of groupg’s most receptive fractiont. Eachm g is continuous and strictly
decreasing whereverF g is non-degenerate.
Arouting policyat budgetqselects a measurable setSof receivers with total massq; each selected
receiver absorbs one unit of exposure. Writetg for the fraction of groupgselected, so P g πgtg =q.
Define:
exposure (per-capita) ofg t g =|S∩g|/(π gN),
burden per selected receiverb g = 1−¯e g(S),
per-capita group burdenh g =t g bg,
yield per contactY= 1 q P g πgtg ¯eg(S),
exposure ratior=t A/tB,burden ratioβ=h A/hB,
where¯eg(S)is the mean propensity of the selected members ofg. We keep these three distinct
throughout:t g (who is contacted),b g (how unwelcome the contact is, per selected receiver), and
hg =t gbg (their product, the group’s per-capita unwanted-contact burden). Exposure parity is
r= 1; burden parity isβ= 1. Exposure here issigned: a routed contact delivers valuee j and
imposes burden1−e j, so fairness has two natural currencies: who receives algorithmic attention
(r= 1:exposure parity) and who absorbs its unwanted residue (β= 1:burden parity).
Generalized burden (benefit and harm need not be complementary).A reader might worry that
defining burden as1−e j makes value and harm exact complements, so the incompatibility is an
artifact of that choice. It is not. Take signed contact utilityu j =e jvj −(1−e j)cj with independent
3

Leshchikova et al., 2027
benefitv j ≥0and harm intensityc j ≥0; the burden object is(1−e j)cj, and willingnesse j,
benefitv j, and harmc j may vary independently. Under group-constant harm intensitiesc g, per-
capita group burden ish g =c gtg(1−¯eg) =c gtgbg, the parity function of Theorem 1(ii) becomes
ϕg(t) =c g t(1−m g(t)), still strictly increasing, andeveryresult below carries over, with the
simultaneous-parity conditionm A(q) =m B(q)replaced byc A(1−m A(q)) =c B(1−m B(q)).
The incompatibility does not depend on complementarity: it survives whenever groups differ in
willingness or in harm intensity. We adopt the unit normalization (vg =c g = 1) for exposition and
speak ofexpected unwanted-contact burdenthroughout.
4 THE FLAT FRONTIER AND THE PARITY INCOMPATIBILITY
Proposition 1(Within-group threshold optimality and the frontier).Fix budgetqand any exposure
ratior >0, which determines(t A, tB)byt A =rt B andπ AtA +π BtB =q. Among all policies
with these group fractions, yield is maximized by selecting each group’s toptg fraction by propensity,
giving
Y ⋆(q, r) = 1 q h πAtA mA(tA) +π BtB mB(tB) i ,
and the frontier’s slope satisfies
∂Y ⋆
∂r ∝Q A(tA)−Q B(tB),
the difference between the two groups’marginalpropensities at their respective admission thresh-
olds.
Proof.For fixed(t A, tB)the objective is additive across receivers, so the selection problem sep-
arates by group and is a fractional-knapsack instance: the top-t g set maximizes each group term.
For the slope, increaserby moving massdµfromB’s marginal admitted receivers (propen-
sityQ B(tB)) toA’s marginal excluded receivers (propensityQ A(tA)); the yield changes by
[QA(tA)−Q B(tB)]dµ/q.
Why the empirical frontier is flat.The slope depends on the gap between marginal, not mean,
propensities. When the group distributions overlap substantially, threshold receptivities at parity-
relevant depths nearly coincide even though group means differ; in the calibrated data the yield
loss from movingr 0 →1is0.2–2.3%across budgets. The efficiency cost of exposure fairness is
second-order; what is first-order is the next section.
Theorem 1(Exposure–burden parity incompatibility).Under the optimal group-threshold policies
of Proposition 1 at budgetq:
(i) Exposure parity (r= 1, sot A =t B =q) impliesβ= 1−m A(q) 1−m B(q) , which equals1iff
mA(q) =m B(q).
(ii) Burden parity (β= 1) holds ifft A

1−m A(tA)

=t B

1−m B(tB)

. Ifm A(t)< mB(t)
for alltin the relevant range, every burden-parity solution hast A < tB, i.e.r ∗ <1.
(iii) Consequently exposure parity and burden parity hold simultaneously iffm A(q) =m B(q).
Whenever the top-fraction means differ, the two parity conditions select disjoint policies,
separated by the band(r ∗,1)in whichneitherparity holds.
Proof.(i) Witht A =t B =q,h g =q(1−m g(q)); take the ratio. (ii) The burden-parity equation
is as stated by definition ofh g. Defineϕ g(t) =t(1−m g(t)); eachϕ g is continuous and strictly
increasing, since adding lower-propensity receivers raises both selected mass and mean burden per
selected receiver. Ifm A < mB pointwise thenϕ A(t)> ϕ B(t)for everyt, soϕ A(tA) =ϕ B(tB)
forcest A < tB by monotonicity. (iii) Immediate from (i) and (ii):r= 1withβ= 1requires
mA(q) =m B(q); conversely if the means differ atq, (i) givesβ̸= 1atr= 1while (ii) places
the burden-parity point strictly belowr= 1; existence ofr ∗ in(r 0,1)follows from continuity of
r7→β(r)andβ(r 0)<1< β(1)whenAis the lower-propensity group andr 0 is the unconstrained
(pooled-threshold) ratio.
4

Leshchikova et al., 2027
Proposition 2(Existence, uniqueness, and monotone geometry).Within the group-threshold family
at budgetq, the burden ratioβ(r)is continuous and strictly increasing on the feasible range ofr.
Consequently, wheneverβ(r 0)<1< β(1), which holds iff groupAbears strictly less per-capita
burden at the unconstrained optimum and strictly more under exposure parity, the burden-parity
pointr ∗ exists, is unique, and lies strictly in(r 0,1).
Proof.Fixq. Asrincreases,t A strictly increases andt B strictly decreases (both are continuous
inrthrough the budget identityπ AtA +π BtB =qwitht A =rt B). By the strict monotonicity
ofϕ g(t) =t(1−m g(t))established in Theorem 1(ii),h A =ϕ A(tA)strictly increases andh B =
ϕB(tB)strictly decreases, soβ=h A/hB is strictly increasing and continuous. Existence and
uniqueness of the root ofβ(r) = 1on(r 0,1)follow from the intermediate value theorem and strict
monotonicity.
Scarcity and the band (empirical comparative static).In the data the band1−r ∗(q)widens
monotonically as the budget shrinks (0.09→0.17→0.30asq: 0.50→0.25→0.10; identically
ordered under the soft coding). A sufficient analytical condition is that the top-mean gapm B(t)−
mA(t)grows ast→0; since this is a tail assumption on the receptivity distributions rather than a
consequence of the model, we report the comparative static as a calibrated regularity of the data and
state the tail condition explicitly where it is used.
Empirical parity points (public release, strict coding).
Budgetq r 0 (unconstr.)r ∗ (burden parity) band1−r ∗ βatr=1yield lossr 0 →1
0.10 0.54 0.70 0.30 1.69−2.3%
0.25 0.66 0.83 0.17 1.29−0.6%
0.50 0.80 0.91 0.09 1.13−0.2%
Soft coding replicates the pattern (r∗ = 0.70/0.81/0.88;βat parity= 1.74/1.37/1.21).
0.6 0.7 0.8 0.9 1.0 1.1 1.2
exposure-rate ratio r (women / men)
0.3
0.4
0.5
0.6yield per contact
(a) Yield is nearly invariant to r
q = 0.10
q = 0.25
q = 0.50
0.6 0.7 0.8 0.9 1.0 1.1 1.2
exposure-rate ratio r (women / men)
0.6
0.8
1.0
1.2
1.4
1.6
1.8per-capita burden ratio (women / men)
(b) Burden parity (circles) vs exposure parity (squares)
Figure 1: Signature: flat yield; disjoint parities.
5 MEASUREMENT NOISE CONVERTS EXPOSURE INTO BURDEN
Routing operates on estimates. Let each receiver’s latent receptivity beθ, with engagement proba-
bilitye(θ)strictly increasing, and let groupg’s latent distribution beN(µ g, s2 g). The router observes
ˆθ=θ+ε,ε∼N(0, σ 2 g)independent across receivers, and applies a pooled thresholdτchosen so
that total selected mass isq. Writev g =
q
s2g +σ 2g,x g = (τ−µ g)/vg, reliabilityρ g =s 2 g/v2 g, and
λ=φ/ ¯Φfor the Gaussian hazard.
Theorem 2(Noise decomposition of exposure and targeting).Assume Gaussian latent receptivity
θ∼N(µ g, s2 g)within groups, Gaussian score noise ˆθ=θ+ε,ε∼N(0, σ 2 g), a probit engagement
5

Leshchikova et al., 2027
linke(θ) = Φ((θ−b)/c), and the scarce regimex g = (τ−µ g)/vg >0with marginal selected
engagement above one half. Under pooled-threshold routing at budgetq, using the standardized
quantitiest g, bg, hg of Section 3:
(i) Group exposure ist g = ¯Φ(xg), and for a group below the threshold on average (x g >0,
the scarce regime),∂t g/∂vg =φ(x g)x g/vg >0at fixedτ; and at fixedbudgetq, with the
threshold adjusting to keepP g πgtg =q, the effect remains strictly positive and equals the
fixed-τeffect scaled by the other group’s share of threshold sensitivity:
dtA
dvA

q
= φ(xA)x A
vA
· πBφ(xB)/vB
πAφ(xA)/vA +π Bφ(xB)/vB
>0 (x A >0).
(ii) The selected members’ mean latent receptivity is
E[θ| ˆθ≥τ, g] =µ g + s2 g vg λ(xg) =µ g +s g √ρg λ(xg),
strictly decreasing inσ g: noise attenuates within-group targeting by the square root of
reliability.
(iii) Consequently a group’s noise differential raises all three quantities together: asσ A grows,
exposuret A rises (part i) and burden per selected receiverb A = 1−E[e(θ)|sel, A]
rises (part ii, via the probit link), so per-capita group burdenh A =t AbA rises on both
factors. Noise-induced exposure is exposure of the wrong members: it converts attention
into burden.
Proof.(i)t g = Pr( ˆθ≥τ) = ¯Φ(xg)since ˆθ∼N(µ g, v2 g); differentiatex g inv g to get∂x g/∂vg =
−xg/vg, hence∂t g/∂vg =φ(x g)xg/vg. (ii)(θ, ˆθ)is bivariate normal withCov =s 2 g, soE[θ|
ˆθ=u] =µ g +ρ g(u−µ g); integrating over the truncated tail,E[θ| ˆθ≥τ] =µ g +ρ g vgλ(xg) =
µg + (s2 g/vg)λ(xg). Monotonicity inσ g:s 2 g/vg decreases inv g, whileλ(x g)decreases asx g
falls withv g (forx g >0); both factors move down. For the budget-adjusted form of (i): totally
differentiate the budget identity,π A dtA +π B dtB = 0withdt g =φ(x g)

(xg/vg)dv g −dτ /vg

anddv B = 0; solve fordτand substitute. (iii) Monotonicity of the selected mean ofe(θ)requires
more than the mean ofθ: we prove it for the probit linke(θ) = Φ

(θ−b)/c

(the fitted logistic link
is numerically indistinguishable on the calibrated range, and all experiments verify the conclusion
directly). Represente(θ) = Pr(W≤(θ−b)/c)withW∼N(0,1)independent, soE[e(θ)|
ˆθ≥τ, g] =E[m(Z)|Z≥x g]whereZ= ( ˆθ−µ g)/vg andm(z) = Φ  (µg + (s2 g/vg)z−
b)
q
c2 +s 2g(1−ρ g)  is the conditional engagement given the standardized score. Two channels
move the selected mean down asσg grows. First,m(z)falls pointwise forz >0in the region where
its numerator is positive: the slopes 2 g/vg shrinks and the conditional spreads 2 g(1−ρ g)grows.
Second, the fixed-τselection becomes less stringent asv g grows (xg falls), andE[m(Z)|Z≥x]
is increasing inxfor any increasingm(truncated-mean monotonicity). Both channels are negative
under the stated regime (xg >0, marginal selected engagement above one half), which the calibrated
parameters satisfy throughout the sweep.
Proposition 3(Group-blind transformations are inert; shrinkage fails the opposite margin).(i) For
any strictly increasingh:R→Rapplied to all scores (agroup-blindtransformation), thresh-
old routing onh( ˆθ)at budgetqselects exactly the receivers selected by routing on ˆθ: group-blind
monotone transformations change neither exposure nor targeting. (ii) Among group-aware transfor-
mations, posterior-mean shrinkage ˆθEB g =µ g +ρ g(ˆθ−µ g)gives group-gscores standard deviation
ρgvg =s 2 g/vg < sg < vg. Fix the budgetqand compare three routing systems, each with its
ownbudget-clearing pooled threshold: routing on true scores (θ, the noiseless benchmark), on raw
noisy scores ( ˆθ), and on posterior-mean scores ( ˆθEB). With a single group’s noiseσ g growing and
the other’s fixed, in the scarce regime raw-score routing strictly over-exposes the noisier group rel-
ative to the noiseless benchmark and posterior-mean routing strictly under-exposes it, both under
the respective budget-adjusted thresholds, not at a commonτ. (iii) Every transformation that is
strictly increasing within each group selects each group’s top members by ˆθand therefore inherits
6

Leshchikova et al., 2027
the targeting attenuation of Theorem 2(ii) unchanged; transformations reallocate exposure across
groups but cannot restore within-group targeting. Restoring the noiselessallocationrequires explic-
itly group-dependent thresholds (the policies of Proposition 1); no transformation, group-blind or
group-aware, restores the noiselessselection.
Proof.(i) A strictly increasinghpreserves the pooled order of scores, hence the top-qset. (ii) The
noisier group’s effective score SD isv g > sg under raw routing,s 2 g/vg < sg under posterior-mean
routing, ands g under the noiseless benchmark, while the other group’s effective SD is identical
across all three systems. By the budget-adjusted derivative of Theorem 2(i), groupg’s exposure is
strictly increasing in its own effective SD at fixedq; the orderings 2 g/vg < sg < vg thus orders
the three systems’ exposures, with the noiseless benchmark strictly between. The threshold dif-
fers across systems, and the ordering survives because Theorem 2(i) signs the effect under exactly
that budget adjustment. (iii) Selection within groupgunder any within-group strictly increasing
transformation is by ˆθrank; Theorem 2(ii) depends only on that rank and onρ g.
Claim Evidence type Source
Exposure/burden incompatibility (Thm. 1) theorem n/a
Existence/uniqueness ofr ∗ (Prop. 2) theorem n/a
Group receptivity differs (0.30SD) empirical survey + fitted model
Flat frontier (0.2–2.3%) empirical (calibrated) released propensities
Parity pointsr ∗, β+ bootstrap CIs empirical (calibrated) released propensities
Differential-noise mechanism (Thm. 2) theorem (stated assumptions) n/a
Magnitude of noise effect semi-synthetic calibrated to posteriors
Non-Gaussian robustness synthetic matched moments
Plug-in learner behavior simulation empirical propensities as truth
Table 1: Provenance of each result: what is proved, what is measured on the public release, and
what is calibrated or simulated.
Calibration to the release.Posterior SDs ofθ recv computed under the released model are near-
identical by gender (0.367vs.0.365; reliabilities0.858/0.876), a measurement-equity finding worth
reporting in its own right, and modestly language-differential (0.390EN vs.0.363RU, ratio1.075).
A semi-synthetic sweep calibrated to the fitted group parameters (µ F =−0.17, sF = 0.99;µ M =
0.06, sM = 1.06; baseσ= 0.37;q= 0.10;e(θ)the fitted Y4 top-category response function)
confirms the theory to within simulation error throughout (Figure 2): doubling the women’s mea-
surement noise raises their exposure ratio from0.62to0.90while their selected members’ mean
latent receptivity falls from1.60to1.24, the per-capita burden ratio flips from0.73to1.61, and
yield declines. This is an apparent fairness improvement that is, in substance, a burden transfer.
1.0 1.5 2.0
noise multiplier  on women
0.6
0.7
0.8
0.9
1.0exposure-rate ratio r (F/M)
observed EN/RU
differential
simulation
theory
1.0 1.5 2.0
noise multiplier  on women
0.75
1.00
1.25
1.50
1.75per-capita burden ratio (F/M)
1.0 1.5 2.0
noise multiplier  on women
1.2
1.3
1.4
1.5
1.6selected women: mean true
Noise inflates exposure while converting it to burden (q = 0.10, calibrated)
Figure 2: Noise sweep, calibrated.
7

Leshchikova et al., 2027
6 COMPUTING CONSTRAINED OPTIMA
Corollary 1(Bisection recovers any parity-constrained optimum).By the strict monotonicity of
β(r)established in Proposition 2, for any targetβ † in the feasible range the yield-optimal group-
threshold policy meeting it is unique and found by bisection onr: after sorting within groups
(O(nlogn)), each iterate costsO(1)with cumulative-sum tables andlog 2(1/ϵ)iterates suffice. The
same routine computes exposure-constrained, burden-constrained, or band-constrained (r∈[r ∗,1])
optima.
On the release, the routine verifiesβ’s monotonicity overr∈[0.45,1.3]and recovers the burden-
parity pointr ∗ = 0.70(bootstrap 90% CI[0.65,0.78]) atq= 0.10in fifty iterations. An uncertainty-
aware variant routes on posterior exceedance probabilitiesPr(θ≥τ g |data), which by Proposition 3
cannot be replicated by any pooled transformation of point scores.
7 FAIR EXPLORATION
When propensities must be learned from engagement feedback, exploration itself distributes burden:
uncertain receivers are routed precisely because they are uncertain, and early-round estimation noise
is measurement noise in the sense of Theorem 2.
Algorithm (plug-in burden-constrained learning).At each roundt, maintain Beta posteriors over
each receiver’s propensity; letˆej(t)be the posterior means. Compute theestimatedburden-parity
ratioˆr∗ t by running the bisection of Corollary 1 on the plug-in burden curveˆβt(r)(group cumulative
sums of the sortedˆej(t)); allocate group counts atˆr∗ t ; within each group, route by Thompson sam-
ples, reserving a vanishing fractionγ t =t −1/2 of each group’s slots for uniform exploration. The
constraint is thuslearned, not supplied: the algorithm never observes true propensities or the true
r∗. Forced exploration guarantees the coverage that the regret and violation bounds require; without
it we state only the empirical behavior.
Proposition 4(Consistency of plug-in burden-constrained learning).Consider the plug-in policy
with forced-exploration rateγ t =t −1/2 on a finite pool with Bernoulli feedback, and suppose
(A1)β ′(r∗)≥c >0, the margin guaranteed strictly by Proposition 2 wheneverr ∗ is interior.
Forced exploration ensures each receiver is routedΩ(
√
T)times, so the propensity estimates satisfy
maxj |ˆej(t)−e j| →0almost surely. Then the estimated constraint is consistent,ˆr∗ t →r ∗ a.s., and
the per-round burden gap|h A,t −h B,t| →0; the time-averaged constraint violationV T /T→0.
We state consistency rather than a rate: the ˜O( √ T)scaling of both regret and cumulative violation
is observed empirically below but requires a self-bounding argument for the adaptive threshold that
we do not claim here.
Calibrated experiment (real pool,n=2,499, strict propensities as ground truth;T=250,q=0.10;30
seeds, bands are 5th–95th percentiles; Figure 3): the plug-in estimateˆr ∗ t starts uninformative (1.01
att=1) and converges to0.710±0.008against the true0.706; final cumulative burden ratio1.027
[1.003,1.046]at cumulative regret36.0 [35.2,36.8]versus35.2 [34.4,36.1]unconstrained: a2.3%
premium for a learned constraint. Unconstrained Thompson drifts to the unconstrained ratio (0.794)
after an early transient above parity (the live form of Theorem 2’s mechanism), and the exposure-
parity policy converges to a1.47burden ratio. The static incompatibility of Theorem 1 persists
under learning, and the burden-parity point is learnable at negligible cost; the choice among parities,
not the price of learning, is the operative design decision.
7.1 ROBUSTNESS AND STRESS TESTS
Three batteries probe whether the parity geometry is a Gaussian artifact, a sampling ac-
cident, or a knife-edge of one budget (Figure 4).Budget sweep with bootstrap un-
certainty.Acrossq∈ {0.02,0.05,0.10,0.20,0.40}, the burden-parity point rises mono-
tonically (r ∗ = 0.61,0.67,0.70,0.80,0.88) and the burden ratio at exposure parity falls
(2.11,1.88,1.69,1.38,1.17);300-replicate bootstrap90%intervals excluder ∗ = 1andβ= 1
at every budget (e.g.r ∗ ∈[0.50,0.72]atq=0.02;β∈[1.12,1.21]atq=0.40), so the incompati-
bility is not a sampling accident, and the reported yield losses remain small throughout (0.3–3.7%).
Noise phase diagram.Over the planeσ F /σM ∈[1,2.5]×q∈[0.02,0.5], calibrated Gaussian
8

Leshchikova et al., 2027
0 100 200
round
0
10
20
30
40cumulative regret
Thompson (unconstrained)
plug-in burden-constrained
exposure parity (r = 1)
0 100 200
round
0.8
1.0
1.2
1.4cumulative burden ratio (F/M)
0 100 200
round
0.70
0.75
0.80
0.85
0.90
0.95
1.00
estimated r * t
Figure 3: Plug-in burden-constrained learning, 30 seeds: regret (left), cumulative burden ratio (cen-
ter), and convergence of the learnedˆr∗ t to the true parity point (right, dashed).
theory maps group exposure: the exposure-parity contour (r=1) is reachable by noise alone at small
budgets (the masquerade of Theorem 2), while the unconstrained-ratio contour marks where noise
has not yet moved allocation.Non-Gaussian stress.Replacing the latent Gaussians with logis-
tic, heavy-tailed (t 3), and bimodal-mixture populations matched in location and scale preserves
the band’s existence and its widening under scarcity in every case; heavy tails compress the band
somewhat, and no distribution eliminates it. The signed-exposure geometry is structural, not distri-
butional.
0.1 0.2 0.3 0.4
budget q
0.2
0.4
0.6
0.8
1.0exposure ratio
r * (q)
r0(q)
0.2 0.4
budget q
1.0
1.2
1.4
1.6
1.8
2.0
2.2
2.4
noise ratio F/ M
0.1 0.2 0.3 0.4
budget q
0.10
0.15
0.20
0.25
0.30
0.35
band width 1 r *
gauss
logistic
t3
mixture
0.6
0.8
1.0
1.2
1.4
1.6
exposure ratio r
Figure 4: Stress tests. Left:r ∗(q)andr 0(q)with bootstrap bands; the gap to1is the incompatibility
band. Center: exposure ratio over the noise-ratio×budget plane; contours markr=r 0 andr= 1.
Right: band width1−r ∗ by budget under four latent distributions.
8 DISCUSSION AND LIMITATIONS
Our empirical quantities are stated-preference propensities from one platform’s user base; they mea-
sure willingness, not behavior, and the release’s demographic granularity limits group analysis to a
binary gender variable and coarse age bands. The theory is broader than the calibration: Proposi-
tions 1–5 need only monotone top-mean functions, and the Gaussian forms of Theorem 3 extend to
any monotone link at the cost of closed forms. We emphasize what the results do not say: the band
(r∗,1)is a menu, not a verdict: selecting exposure parity, burden parity, or an interior point is a
value judgment about whose interests algorithmic attention serves, and our contribution is to price
the menu and expose the incompatibility that prevents ordering everything at once. Signed-exposure
optimization applies to populations for whom contact is institutionally permissible but receptivity is
uncertain; explicit opt-out and consent restrictions dominate the optimization and must be enforced
as hard constraints before any fairness objective is considered. Within that scope, the structure
applies wherever machine-initiated contact meets heterogeneous willingness: cold outreach, notifi-
cation targeting, solicitation, and any agentic system that opens conversations people did not start.
9

Leshchikova et al., 2027
ETHICS STATEMENT
All analyses use a public, anonymized dataset released under CC BY with a documentedk≥5
anonymity audit; no new human data were collected. Group analyses respect the release’s granular-
ity and are reported as properties of routing policies, not of people. The routing machinery studied
here is dual-use: the same thresholds that equalize burden could be tuned to concentrate it, and
we discuss constraints precisely so that deployment conversations have a vocabulary for the second
margin. We make no claim that any parity point is universally correct.
AI USAGEDISCLOSURE
Generative AI tools were used in this work for three purposes: copy-editing author-written text for
readability, assisting with the writing and debugging of analysis code, and formatting bibliographic
references. No task in the required-disclosure category involved generative AI, and no substantive
content, methodology, analysis, or result was AI-generated. AI-assisted edits were checked against
the original text to confirm meaning and claims were unchanged; AI-assisted code was read, tested,
and verified by the authors to reproduce the reported results; and formatted references were checked
against original sources. We take responsibility for the final content of this work.
REFERENCES
Ashwinkumar Badanidiyuru, Robert Kleinberg, and Aleksandrs Slivkins. Bandits with knapsacks.
Journal of the ACM, 65(3), 2018.
Asia J. Biega, Krishna P. Gummadi, and Gerhard Weikum. Equity of attention: Amortizing individ-
ual fairness in rankings. InProc. SIGIR, pp. 405–414, 2018. doi: 10.1145/3209978.3210063.
Alexandra Chouldechova. Fair prediction with disparate impact: A study of bias in recidivism
prediction instruments.Big Data, 5(2):153–163, 2017.
Fernando Diaz, Bhaskar Mitra, Michael D. Ekstrand, Asia J. Biega, and Ben Carterette. Evaluating
stochastic rankings with expected exposure. InProc. CIKM, pp. 275–284, 2020.
Vitalii Emelianov, Nicolas Gast, Krishna P. Gummadi, and Patrick Loiseau. On fair selection in the
presence of implicit variance. InProc. EC, pp. 649–675, 2020. doi: 10.1145/3391403.3399482.
Riccardo Fogliato, Alexandra Chouldechova, and Max G’Sell. Fairness evaluation in presence of
biased noisy labels. InProc. AISTATS (PMLR 108), pp. 2325–2336, 2020.
Sorelle A. Friedler, Carlos Scheidegger, and Suresh Venkatasubramanian. The (im)possibility of
fairness: Different value systems require different mechanisms for fair decision making.Commu-
nications of the ACM, 64(4), 2021.
Sahin Cem Geyik, Stuart Ambler, and Krishnaram Kenthapadi. Fairness-aware ranking in search
and recommendation systems with application to linkedin talent search. InProc. KDD, 2019.
Abigail Z. Jacobs and Hanna Wallach. Measurement and fairness. InProc. FAccT, 2021.
Matthew Joseph, Michael Kearns, Jamie Morgenstern, and Aaron Roth. Fairness in learning: Classic
and contextual bandits. InProc. NeurIPS, 2016.
Jon Kleinberg and Manish Raghavan. Selection problems in the presence of implicit bias. InProc.
ITCS (LIPIcs 94), pp. 33:1–33:17, 2018. doi: 10.4230/LIPIcs.ITCS.2018.33.
Jon Kleinberg, Sendhil Mullainathan, and Manish Raghavan. Inherent trade-offs in the fair determi-
nation of risk scores. InProc. ITCS, 2017.
Daria Leshchikova, Valentina V . Kuskova, Dmitry Zaytsev, and Valerii Klimov. Two-sided recep-
tivity to conversational AI agents in online dating: Bilingual survey data (Fledge.Love). Zenodo,
doi:10.5281/zenodo.21971273.
10

Leshchikova et al., 2027
Marco Morik, Ashudeep Singh, Jessica Hong, and Thorsten Joachims. Controlling fairness and bias
in dynamic learning-to-rank. InProc. SIGIR, 2020.
Ziad Obermeyer, Brian Powers, Christine V ogeli, and Sendhil Mullainathan. Dissecting racial bias
in an algorithm used to manage the health of populations.Science, 366(6464):447–453, 2019.
Iv´an Palomares, Carlos Porcel, Luiz Pizzato, Ido Guy, and Enrique Herrera-Viedma. Reciprocal
recommender systems: Analysis of state-of-art literature, challenges and opportunities towards
social recommendation.Information Fusion, 69:103–127, 2021.
Gourab K. Patro, Arpita Biswas, Niloy Ganguly, Krishna P. Gummadi, and Abhijnan Chakraborty.
Fairrec: Two-sided fairness for personalized recommendations in two-sided platforms. InProc.
WWW, 2020.
Ashudeep Singh and Thorsten Joachims. Fairness of exposure in rankings. InProc. KDD, pp.
2219–2228, 2018. doi: 10.1145/3219819.3220088.
Tom S¨uhr, Asia J. Biega, Meike Zehlike, Krishna P. Gummadi, and Abhijnan Chakraborty. Two-
sided fairness for repeated matchings in two-sided markets: A case study of a ride-hailing plat-
form. InProc. KDD, 2019.
Meike Zehlike, Francesco Bonchi, Carlos Castillo, Sara Hajian, Mohamed Megahed, and Ricardo
Baeza-Yates. Fa*ir: A fair top-k ranking algorithm. InProc. CIKM, pp. 1569–1578, 2017.
Meike Zehlike, Ke Yang, and Julia Stoyanovich. Fairness in ranking: A survey.ACM Computing
Surveys, 2022.
A EXPERIMENTAL DETAILS AND DEFERRED MATERIAL
Proofs of Propositions 1, 4, 5 and Theorems 2, 3 appear inline in the main text. This ap-
pendix records experimental settings: frontier and parity computations use the released strict-coding
propensities (n=2,499; soft coding replicates all findings withr ∗ = 0.70/0.81/0.88andβat ex-
posure parity1.74/1.37/1.21); the noise sweep uses4×10 5 draws per point, group parameters
(µF , sF , µM , sM ) = (−0.17,0.99,0.06,1.06), baseσ= 0.37, engagement link the fitted Y4 top-
category response function, seed 7; the bandit experiment uses the real pool,T=250,q=0.10,
Beta(1,1)priors, Bernoulli feedback, seeds1000–1029with paired policy streams. Stress tests:
bootstrap resamples respondents with replacement (B=300, seed 3); the phase diagram uses the
calibrated group parameters of Section 7.1 with the budget-adjusted pooled threshold; synthetic
populations use4×10 4 draws per group matched to the calibrated location and scale (logistic scale
0.551s;t 3 scaled by
√
3; mixture0.3N(µ+1.2,0.5 2) + 0.7N(µ−0.5,0.7 2)), engagement via the
fitted Y4 link. Propensities are model-derived quantities from the public release; bootstrap intervals
quantify sampling variability, and the released notebooks provide the fold structure for out-of-fold
recomputation.
B PROOF OFPROPOSITION4
WriteN j(t)for receiverj’s routing count. The forced-exploration schedule routes a uniformly ran-
domγ t =t −1/2 fraction of each group’s slots; since each group receivesΘ(qN)slots per round,
every receiver’s expected forced-exploration count through roundTisΩ
P
t≤T t−1/2 = Ω( √ T),
and a Chernoff bound with Borel–Cantelli givesN j(T) = Ω(
√
T)for alljalmost surely. Hence
maxj |ˆej(t)−e j| →0a.s. (SLLN per receiver, finite pool). The plug-in burden curve is uniformly
consistent,sup r | ˆβt(r)−β(r)| →0, because each group’s cumulative-sum curve converges uni-
formly and the ratio map is continuous on the compact feasible range (bounded away from zero
burden in the scarce regime). By (A1) and the strict monotonicity of Proposition 2, the mapβ7→r ∗
is continuous atr ∗, soˆr∗ t →r ∗ a.s. The per-round burden gap is a continuous function of the allo-
cation ratio and the (converging) selected-group means, hence|h A,t −h B,t| →0; Ces`aro averaging
givesV T /T→0. This establishes consistency. We do not claim a
√
Trate: bounding P t |ˆr∗ t −r ∗| requires controlling the adaptive threshold’s fluctuations through a self-bounding argument, which
we leave to future work and probe empirically in Section 7.1 and Figure 3.
11

Leshchikova et al., 2027
C REPRODUCIBILITY
Every number, table, and figure derives from the public deposit (DOI in the dataset citation)
via scripts included in the supplementary material with fixed seeds; the semi-synthetic and ban-
dit experiments state their generative parameters in Appendix A, and theory-versus-simulation
agreement is reported alongside each experiment. Supplementary material is also available via
https://anonymous.4open.science/r/Signed_Exposure.
12
