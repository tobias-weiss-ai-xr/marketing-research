---
title: Demand Curvature and Pass-Through in Multiproduct Oligopoly
url: https://arxiv.org/abs/2604.21423
category: consumer-behavior
subcategory: empirical
date: 2026-04
venue: ''
authors:
- Paul S. Koh
source: arxiv
pdf_url: https://arxiv.org/pdf/2604.21423
pages: 75
chars: 123876
fetched_at: '2026-11-08T13:17:57+00:00'
kb_version: 1
---

# Demand Curvature and Pass-Through in Multiproduct Oligopoly

Demand Curvature and Pass-Through in Multiproduct Oligopoly ∗
Paul S. Koh †
September 13, 2026
Abstract
Economic interventions change firms’ pricing incentives, but their effects depend on how those
incentives propagate across products and firms. This paper develops tractable characterizations
of that propagation under multiproduct Bertrand competition. A decomposition of the pricing
system isolates demand curvature, substitution, and ownership, linking the equilibrium response
matrix to commonly used empirical demand models. It yields approximations with explicit
error bounds and separates individual adjustment from equilibrium feedback. Small-share limits
reveal when interactions disappear and when substitution within nests or selection among
heterogeneous consumers preserves them. For nested logit, a closed-form response reduces the
limiting product-level system to averages within firm–nest groups, exposing the direction of
price spillovers. The same framework organizes local responses to changes in costs, demand, and
ownership. The results clarify which features of demand support simple incidence predictions
and which interactions those predictions must retain.
Keywords: Pass-through, demand curvature, multiproduct oligopoly, differentiated products.
∗I thank Jinhyuk Lee, Aviv Nevo, Devesh Raval, and the participants of the 2026 KASIO Summer Conference and
Korean Econometric Society Summer Conference for helpful comments. All errors are mine.
†School of Economics, Yonsei University. Email:paulkoh9@gmail.com.
1
arXiv:2604.21423v2  [econ.GN]  14 Sep 2026

1 Introduction
Economic interventions change the incentives to set prices. Their consequences depend on how
those incentives propagate through a market: a firm may reprice other products in its portfolio,
competitors may respond, and consumers may substitute toward products that the intervention
does not directly affect. This propagation is common to otherwise different questions about market
outcomes and welfare. Pass-through provides a way to study it by separating a change in pricing
incentives from the equilibrium response to that change (Weyl and Fabinger, 2013). The challenge
in multiproduct markets is to make the resulting response matrix tractable without discarding the
interactions that matter for the question at hand.
Demand elasticity alone does not answer this question. In simulated cereal data, Miravete
et al. (2023) obtain similar average elasticities and relative markups across estimated demand
specifications, but substantially different pass-through predictions. A firm’s response to a cost
change depends on how a price adjustment changes its marginal incentive to raise price further. For
a monopolist selling one product, demand curvature governs this adjustment (Bulow and Pfleiderer,
1983). With differentiated products, changing one price also changes the sensitivity of demand
to other prices. These mixed derivatives affect the value of sales diverted within a portfolio and
the incentives of competitors to reprice. Ownership determines which effects a firm internalizes;
equilibrium combines the resulting adjustments. Thus, even detailed knowledge of substitution at
observed prices leaves a substantive role for assumptions about how substitution changes as prices
move.
This paper develops a tractable characterization of local price responses under multiproduct
Bertrand competition. The characterization links the equilibrium response matrix to own-price
curvature, changes in substitution, and product ownership. It supplies two ways to simplify that
matrix: a sequence of approximations with explicit error control, and analytical limits tied to widely
used demand specifications. The objective is to make first-order analysis easier to implement and
interpret in these models. A firm’s response with rival prices fixed and its response after rivals
adjust are distinct objects; likewise, small unconditional shares and weak substitution among the
remaining purchases are distinct restrictions. Keeping these distinctions explicit identifies which
interactions a useful simplification must retain.
2

The starting point is a decomposition of the pricing system. Normalizing each first-order
condition by its own-price demand slope separates the price derivative of that condition into a
baseline own-price term, a demand-curvature and substitution term, and an ownership term. The
ownership term records both the internalization of diverted sales and changes in diversion as
prices adjust. Inverting this system gives the equilibrium pass-through matrix. The decomposition
therefore traces how demand shape and product portfolios jointly transmit a pricing incentive,
including its effects on products not directly affected by the intervention. In mixed logit, these
derivatives reflect both individual choice responses and changes in the composition of buyers. Cost
shocks provide the initial representation; a general intervention enters through a different change in
the pricing conditions.
The distinction between individual adjustment and equilibrium feedback has a direct economic
implication. A firm’s profit curvature characterizes its local adjustment to a cost change when
rival prices are fixed, but does not by itself determine the equilibrium response. A quadratic-
utility duopoly illustrates the difference at a Nash equilibrium: fixed-rival own-cost pass-through
is one-half, whereas a common cost increase passes through at four-fifths. Both firms choose
globally optimal prices, and the common-cost response holds exactly over a finite range of cost
changes. Across the example’s demand family, baseline quantities, markups, and own-profit curvature
remain unchanged while equilibrium pass-through varies with substitution. The example illustrates
established strategic feedback; the decomposition identifies how that feedback enters the response
matrix and its approximations.
The decomposition also yields a sequence of approximations that adds successive interactions to
a diagonal baseline. A Neumann expansion supplies an exact remainder and an error bound under an
explicit contraction condition. For common-coefficient multinomial logit, I establish convergence at
every interior equilibrium, allowing multiproduct ownership. In a numerical exercise with 1,000 logit
configurations with heterogeneous product characteristics and costs, the first interaction correction
has a mean relative matrix error of0.323%. This exercise measures approximation of the local
response; separate finite-cost experiments assess the additional error from using a local derivative to
predict a discrete change. The analytical error bounds give sufficient conditions under which the
approximation is justified beyond this logit benchmark. A residual bound also evaluates a proposed
3

response to a particular shock and, when sufficiently tight, certifies the sign of a local price or
price-index effect.
Small-share limits reveal a different source of simplification and its limits. Shares may fall because
the outside option becomes more attractive, prices rise, or demand approaches a boundary. These
experiments need not leave the same consumers or substitution patterns in the market. Along the
specified fixed-dimensional paths, logit and lognormal mixed logit yield identity unit-pass-through
limits, whereas CES yields a diagonal limit above one. Cross-product effects can nevertheless survive
when every product’s unconditional share vanishes. In nested logit, substitution and ownership
within a disappearing nest continue to determine the limiting response; gamma mixing can preserve
interaction along a common high-price ray. Small shares alone therefore do not justify treating
products as independent for incidence analysis. The economically relevant question is whether
substitution among the remaining purchases disappears with them. In nested logit, the surviving
response admits a closed form based on cost averages within firm–nest groups. It reveals nonnegative
cross-firm and nonpositive within-firm cross-price responses in the limiting nest, while a common
cost change passes through one for one. This reduction preserves economically relevant spillovers
without requiring a product-level matrix inversion.
The applications show how the same response system can be used across economic questions.
A general incentive formula covers smooth changes in costs, demand, and ownership. A demand
intervention affects pricing through both its effect on sales and its effect on price sensitivities;
observing the first effect alone is generally insufficient. A demand-translation example shows how
changes in willingness to pay map into prices through the cost pass-through matrix. The remaining
applications distinguish unit from percentage incidence, derive revenue-weighted consumer-surplus
expressions under the small-share benchmarks, and connect ownership incentives to local merger
predictions. These results link the general first-order approach to explicit calculations in empirical
demand models, conditional on the demand derivatives and pricing behavior used to evaluate them.
1.1 Related Literature
The paper builds on the theory of incidence under imperfect competition. Bulow and Pfleiderer
(1983) establish the role of demand curvature in monopoly pass-through. Weyl and Fabinger (2013)
relate pass-through to conduct and welfare, developing both symmetric and asymmetric analyses,
4

with a matrix characterization in Appendix C. Adachi and Fabinger (2022) characterize welfare
incidence for multiple policy instruments and heterogeneous firms. On a given one-dimensional
demand curve, the Bulow–Pfleiderer index used here and Weyl and Fabinger’s marginal-consumer-
surplus elasticity encode the same curvature information. The contribution here concerns tractability
within multiproduct Bertrand models: the decomposition makes the derivative requirements explicit,
the approximation bounds control omitted interactions, and the model-specific limits identify when
those interactions simplify. The general use of pass-through for interventions is the starting point of
the analysis.
The retail literature studies curvature-dependent responses to manufacturer trade deals (Tyagi,
1999) and own-brand and cross-brand pass-through (Besanko et al., 2005). Moorthy (2005) derives a
matrix characterization for competing multiproduct retailers and separates cost-induced substitution
incentives from internal and external strategic complementarity. His explicit nested-logit solution
distinguishes product-, retailer-, and marketwide shocks: a cost increase on one product at one
retailer lowers the other product’s price at that retailer and raises both prices at its competitor.
These mechanisms are antecedents of the analysis here. The present decomposition identifies their
demand-curvature and ownership components and studies approximations and limiting responses
under specified demand systems.
Alexandrov and Bedre-Defolie (2017) analyze the LeChatelier–Samuelson principle in games
and conditions under which additional adjustments amplify responses. Pass-through also has an
established role in merger analysis. Froeb et al. (2005) connect the price effects of mergers to the
pass-through of efficiencies; Jaffe and Weyl (2013) develop local price and welfare approximations
using merger pass-through. Miller et al. (2016, 2017) evaluate related prediction methods. The
present analysis exposes the interaction terms omitted by low-order approximations and connects
them to demand shape and ownership in empirical models. The merger application retains Jaffe
and Weyl’s distinction between merger pass-through and ordinary premerger cost pass-through.
A closely related literature examines demand shape and counterfactual sensitivity. Mrázová
and Neary (2017) organize firm behavior through elasticity and convexity. Miravete et al. (2023)
connect demand specification to differentiated-product incidence, and Miravete et al. (2026) explain
how preference heterogeneity shapes curvature and develop a more flexible demand specification.
Their demand-derivative calculations and selection mechanisms are antecedents of the mixed-logit
5

interpretation below. The present analysis connects those derivatives to the multiproduct pricing
Jacobian and gives conditions for assessing omitted interactions in a particular local response.
It thereby helps interpret specification-sensitive incidence predictions without attributing their
quantitative differences to a single channel. Birchall et al. (2024) use a Box–Cox transformation
to relax restrictions on substitution and curvature, while Compiani (2022) estimates multiproduct
demand nonparametrically and examines sensitivity across tax and product-portfolio counterfactuals.
These contributions motivate the focus here on the derivative combinations entering equilibrium
pricing and the restrictions under which they simplify.
Armstrong and Vickers (2018) derive tractable multiproduct pricing and pass-through results
for monopoly and Cournot competition. Armstrong and Vickers (2023) characterize feasible
multiproduct-monopoly pass-through matrices and show how price responses can have counterin-
tuitive signs. The present analysis studies asymmetric multiproduct Bertrand competition with
constant marginal costs, developing approximations and demand-specific limits for its local response
system.
Nocke and Schutz (2018, 2025) exploit aggregative structure to analyze multiproduct oligopoly
and mergers, including logit and CES demand. Their nested extension allows firms that own entire
nests and firms confined to part of a single nest. Garrido (2024) allows arbitrary overlap between
firms and nests and develops a reduced pricing system using common markups within firm–nest
groups. The nested calculation here studies a specified vanishing-share limit of this pricing structure
and expresses the resulting local cost response through group averages, making its spillover signs
explicit. The general local decomposition does not require aggregative demand.
Sangani (2026) documents complete pass-through in levels for common cost shocks and studies
demand restrictions underlying pass-through in levels and percentages. This comparison is especially
relevant to the small-share and percentage-incidence results. A common-shock response restricts
a weighted sum of columns of the pass-through matrix; it need not determine the response to a
shock affecting only some products. The present framework retains this distinction when deriving
model-specific limits and applying them to incidence.
Finally, MacKay et al. (2014) study bias in reduced-form pass-through estimates, and Dearing
et al. (2026) connect the relevance of instruments for conduct tests to the features of pass-through
those instruments target, including their relevance for counterfactuals. Their work addresses what
6

observed variation reveals about pricing behavior. The present results are conditional comparative
statics: they specify which demand derivatives and equilibrium interactions a prediction requires.
Identifying those objects from observed shocks is a separate empirical task.
Section 2 introduces the model. Section 3 characterizes pass-through and separates fixed-rival
responses from equilibrium feedback. Sections 4 and 5 develop the series approximation and small-
share limits. Section 6 presents the applications, and Section 7 concludes. The appendices contain
proofs, model-specific derivations, numerical illustrations, and supplementary directional bounds.
2 Setup
2.1 Model
Consider a Bertrand–Nash pricing game among multiproduct firms selling differentiated products.
LetJ ={1,...,J} denote the set of inside goods, and letj = 0denote the outside option. Firmf
produces the subsetJf⊆Jand earns profit
Πf(p) =
∑
l∈Jf
(pl−cl)ql(p),(1)
wherep l,c l, andql(p)denote price, constant marginal cost, and demand for productl.
The analysis is local to an interior Bertrand–Nash equilibrium that admits an equilibrium
continuation after sufficiently small cost changes. Demand is twice continuously differentiable in
a neighborhood of this point, withqj > 0and ∂qj/∂pj < 0. The full Jacobian of the pricing
first-order conditions is nonsingular, so the implicit function theorem makes this continuation locally
unique and differentiable among solutions to the pricing conditions. These assumptions do not
require global uniqueness; first-order conditions alone need not be sufficient for equilibrium. The
general characterization accommodates smooth demand with heterogeneous product tastes and price
sensitivities; the distributional restrictions in the model-specific limits are additional assumptions.
At the equilibrium, each firm’s first-order conditions require, for eachj∈Jf,
∂Πf
∂pj
=q j(p) +
∑
l∈J
Ωjl(pl−cl)∂ql(p) ∂pj = 0,(2)
7

whereΩis the symmetric J×J ownership matrix withΩjl = 1if products j and l are owned by
the same firm and0otherwise. Stacking (2) overj∈J f yields
∇pf Πf(p) =q f(p) +J qf (p)⊤(pf−cf) =0,(3)
whereq f(p)is the vector of demands for firmf’s products, andJqf (p)≡ ∂qf (p) ∂p⊤ f is the within-firm
Jacobian with typical elementJqf,kj(p) = ∂qk(p) ∂pj .
Stacking (2) across all firms gives the system
F(p)≡q(p) + ∆(p)(p−c) =0,(4)
where∆(p) ≡ Ω◦ Jq(p)⊤ (◦ denotes the Hadamard product) andJq(p)≡ ∂q(p) ∂p⊤ . All pass-through
calculations below evaluate this system at the equilibrium under study. When discussing a sequence
of equilibria, marginal costs may vary along the sequence; an arbitrary path of prices is not itself an
equilibrium path.
2.2 Definition of the Pass-Through Matrix
I now introduce the main object of interest, the pass-through matrix, which describes how per-unit
taxes or cost shocks affect equilibrium prices. Recall that the firms’ pricing equations are
F(p) =0⇔q j + (pj−cj)∂qj ∂pj + ∑ l∈J\{j} Ωjl(pl−cl)∂ql ∂pj = 0,∀j∈J.
To derive the pass-through matrix, it is convenient to rewrite the first-order conditions in a form
that is quasilinear in marginal costs:
f(p)≡−
(
Jdiag q (p) )−1F(p) =0⇔ − qj ∂qj/∂pj −(pj−cj)+ ∑ l∈J\{j} Ωjl(pl−cl)Dj→l = 0,∀j∈J,
(5)
whereJ diag q (p)is a J×J diagonal matrix with(j,j )entry ∂qj(p)/∂pj, andDj→l≡− ∂ql/∂pj ∂qj/∂pj is the
diversion ratio from productjtol.
8

Now consider a vector of per-unit taxest= (t1,...,t J)so that productj’s marginal cost becomes
cj +tj. The post-tax equilibrium satisfies
f(p) + Λ(p)t=0,(6)
where Dj→j =−1, soD= [ Dj→k]j,k∈J includes this diagonal convention andΛ(p)≡− Ω◦ D(p)is
the ownership-internalized diversion matrix.1 Differentiating (6) with respect tot⊤ gives
∂f(p)
∂p⊤
∂p
∂t⊤ + Λ(p) +
J∑
m=1
(∂Λ(p)
∂pm
t
)(∂pm(t)
∂t⊤
)
=0.
Evaluating the expression att=0and rearranging (assuming thatJ f is invertible) yields the
pass-through matrix
∂p
∂t⊤ =−J−1 f Λ,(7)
whereJ f≡ ∂f(p) ∂p⊤ . Write this matrix asΨ.2 Its entryΨjk is the local equilibrium price response of
product j to a unit cost increase on productk, allowing all firms to reprice. Becausefdepends on
first derivatives of demand,Ψgenerally requires second derivatives as well. Existing taxes can be
included in baseline costs; the formula is then evaluated at zeroincrementaltax. A finite policy
change requires following the equilibrium branch or resolving the post-policy equilibrium.
Remark 1(The direction of the cost shock).A local cost changet=τ zinduces dp/dτ = Ψz. For
a uniform per-unit shock,z=1, so each price response is a row sum ofΨ. Complete pass-through
of this common shock meansΨ1=1; this condition alone does not implyΨ =I. For a proportional
cost changedc=c dτ at positive prices and costs, the vector of percentage price responses is
diag(p)−1Ψc. Thus both the units of measurement and the direction of the shock matter when
comparing pass-through restrictions across demand systems (Moorthy, 2005; Sangani, 2026).
1Equivalently,Λ jl = Ωjl ∂ql/∂pj ∂qj /∂pj =−Ω jlDj→l. If firms are single-product producers, thenΛ =I.
2Up to row normalization and the choice of cost-shock columns, this is the comparative-static systemP =−H−1C
in Moorthy (2005, equation (2)). HisH is the Jacobian of the unnormalized pricing conditions and hisC records their
derivatives with respect to the specified cost changes. Normalization changes the representation, not the equilibrium
response.
9

2.3 The Monopoly Curvature Benchmark
For a single product with downward-sloping residual demandq(p)and constant marginal cost, the
first-order condition givesp−c=−q/q ′. At this stationary point,
π′′(p) = 2q′(p) + (p−c)q′′(p) =q′(p)(2−κ(p)),
where the Bulow–Pfleiderer index is
κ(p) := q(p)q′′(p) q′(p)2 ≤2.(8)
The inequality is the second-order necessary condition. Under the strict conditionκ< 2, differenti-
ating the pricing equation gives3
∂p
∂t = 1 2−κ .(9)
More convex demand makes the marginal profit response to a price increase less negative,
increasing cost pass-through. In a multiproduct firm, the relevant profit curvature depends on the
direction of joint price adjustment. In oligopoly, rival responses add a further source of amplification.
The next section separates these two mechanisms.
3 Characterization of Pass-Through
3.1 A Structural Decomposition of Pass-Through
A product’s pricing equation balances its own lost sales against margins and sales recaptured
elsewhere in the firm’s portfolio. Differentiating that equation separates two sources of change: the
curvature of residual demand, and the way ownership makes diversion to other products valuable.
The following decomposition keeps both sources visible before the full pricing system is inverted. Its
purpose is to expose which parts of an empirical demand specification govern the response: fitting
3For the same downward-sloping demand curve, this is also the formula in Weyl and Fabinger (2013). Let
p = P (q)be inverse demand and let ms(q) = −qP′(q)denote marginal consumer surplus. Under their inverse-
elasticity convention,1/ϵms =qms′(q)/ms(q) = 1 +qP′′(q)/P′(q) = 1−κ BP, whereκBP =q(p)q′′(p)/q′(p)2. Thus
1/(1 + 1/ϵms) = 1/(2−κ BP). In oligopoly, the common-price demand path used in a symmetric incidence calculation
generally differs from an own-price demand curve holding other prices fixed. The scalar identity applies to the same
curve; it does not equate curvature across these paths.
10

substitution at a price vector disciplines the slopes, while the mixed derivatives determine how
pricing incentives change away from that vector.
Use qj,k =∂qj/∂pk and qj,kl =∂2qj/∂pk∂pl. Wherever the relevant first derivatives are nonzero,
define
κj kl := qjqj,kl qj,kqj,l .(10)
This index measures changes in a demand slope relative to the corresponding first-order effects. Its
own-price case is the Bulow–Pfleiderer index.4 The matrix characterization itself does not require
nonzero cross-price slopes.
Lemma 1(Decomposition of the FOC Jacobian).For twice continuously differentiable demand
withq j >0andq j,j <0, the normalized pricing Jacobian satisfies
Jf =−2I+K+C,(11)
where
Kjk =



qjqj,jj/q2 j,j, j=k,
−qj,k/qj,j +qjqj,jk/q2 j,j, j̸=k,
(12)
Cjk =



∑
l̸=j
Ωjl(pl−cl)∂Dj→l ∂pj , j=k,
ΩjkDj→k +
∑
l̸=j
Ωjl(pl−cl)∂Dj→l ∂pk , j̸=k. (13)
Whenq j,k̸= 0, the off-diagonal entry also equalsKjk =δ jk(1−κ j kj), withδjk =−q j,k/qj,j.
Proof.See Appendix A.1.
The baseline−2I comes from differentiating own demand divided by its own slope and the own
markup. The matrixKis the demand-side correction: its diagonal measures own-price curvature; its
off-diagonal entries combine the effect of another price on demand with its effect on the own-demand
4When the denominators exist,κj kl = 1 +∂kl logq j/(∂k logq j∂l logq j). Directional curvature can then be written as
κj(v) =
∑
k,lωjkl(v)κj kl, whereωjkl(v) = (vkqj,k)(vlqj,l)/( ∑ mvmqj,m)2. The weights sum to one but can be negative,
so this is an affine combination, not necessarily an average with positive weights.
11

slope. The expanded definition in(12) remains valid for independent demands and for cross-price
slopes that vanish at the evaluation point.5
The matrixCrecords additional terms from multiproduct ownership. Its direct-diversion term
reflects that changing another owned price changes the margin on recaptured sales. Its markup-
weighted diversion derivatives reflect how the price change reallocates lost sales across the portfolio.
Both are absent with single-product ownership, butKcan still create strategic interaction across
single-product firms. Thus a change in a portfolio can alter incidence even with demand held fixed,
and a change in mixed curvature can alter incidence even with baseline substitution and ownership
held fixed. These are the separate economic channels represented by the decomposition.
Preference heterogeneity and the pricing Jacobian.For mixed-logit demand, the derivative
terms have an interpretation at finite prices. Letsij(p)be typei’s probability of buyingj, with a
fixed type distributionF and market sizeM, so thatqj =M
∫
sijdF. Write Ej for expectation over
types weighted bysij/
∫
sijdF. With differentiation under the integral justified and the displayed
moments finite,
∇2 p logqj =E j[∇2 p logsij] + Covj(∇p logsij).(14)
The first term averages changes in individual choice sensitivities. The covariance term records how
repricing changes the composition of buyers. Its diagonal is nonnegative, whereas its off-diagonal
entries can have either sign. Both own and cross curvature therefore depend on the consumers
purchasing the product, not just its aggregate share.
This is a reformulation of standard mixture differentiation; the own-price calculation corresponds
to Miravete et al. (2023, equation (14)) and Miravete et al. (2026, equation (16)). Here its role is to
identify the components enteringK, which equilibrium pricing combines with ownership throughC
andΛ. Appendix A.1 derives the identity and its mixed-logit specializations. The calculation allows
jointly distributed product tastes and price sensitivities; it requires neither small shares nor the
scalar-mixing restrictions used later for the ray limits.
Together withΨ =−J−1 f Λ, the decomposition maps these primitives into equilibrium responses.
A pricing direction that produces little change in the first-order conditions can generate a large price
5The slope ratioδjk =−qj,k/qj,j and diversion ratioDj→k =−qk,j/qj,j need not coincide. They coincide when
cross-price derivatives are symmetric, as for differentiable quasilinear demand. No symmetry assumption is used in
the decomposition.
12

response if the cost shock loads on that direction. The next two subsections distinguish within-firm
profit curvature from the feedback that couples firms’ pricing decisions.
3.2 Directional Profit Curvature
The full pricing Jacobian describes equilibrium interactions. To interpret its within-firm blocks,
fix rivals’ prices and vary firmf’s prices alongp f +tv. Write ϕj,v(t) = qj(pf +tv, p−f)and
Φf,v(t) = Πf(pf +tv,p −f). Letm j =p j−cj denote an absolute markup. Define
Sf(v) :=−v⊤Jqfv, M j(v) := mj qj ϕ′ j,v(0)2, M f(v) := ∑ j∈Jf Mj(v),
where Jqf = (J qf +J⊤ qf )/2. The slope term Sf captures the first-order loss of sales along the
price direction. The weightMj equals product j’s variable profit times its squared directional
semi-elasticity.
For any direction withMf(v)>0, define
Rf(v) := Sf(v) Mf(v), κ f(v) :=
∑
j∈Jfmjϕ′′ j,v(0)
Mf(v) .
The second definition is valid even when a product has zero first-order demand response alongv. If
everyϕ′ j,v(0)is nonzero, it also has the weighted-curvature representation
κf(v) =
∑
j∈Jf
λj(v)κj(v), λ j(v) = Mj(v) Mf(v), κ j(v) = qjϕ′′ j,v(0) ϕ′ j,v(0)2 .
Nonnegative markups make these weights nonnegative and sum to one. Defining the aggregate
directly avoids undefined products of a zero weight and an undefined product-level curvature.
Lemma 2(Directional curvature and the second-order condition).Supposeqj > 0and mj≥ 0for
allj∈J f. For every directionvwithM f(v)>0,
Φ′′ f,v(0) =M f(v) ( κf(v)−2R f(v) ) .(15)
13

Consequently the directional second-order condition is equivalent to
κf(v)≤2R f(v).(16)
If all markups are positive andJqf is nonsingular, thenMf(v)> 0for every nonzero v, and the
profit Hessian is negative semidefinite if and only if this inequality holds for every such direction.
Proof.See Appendix A.2.
The ratioRf compares the first-order sales effect with the scale on which demand curvature
enters profits. For one product, the first-order condition impliesMf(v) = Sf(v) =−q′(p)v2, so
Rf(v) = 1and the inequality reduces to κ≤ 2. With multiple products, the threshold varies
with the direction because different joint price changes induce different reallocations of sales. Here
“stability” refers to an individual firm’s local profit curvature, not dynamic stability or invertibility of
the whole pricing game. Appendix D gives additional bounds under symmetric demand derivatives.
Remark 2(Directional law of demand).If demand satisfies(q(p ′)− q(p))⊤(p′− p)≤ 0, its
symmetric Jacobian is negative semidefinite. Every principal submatrix then has the same property,
giving Sf(v)≥ 0. To see this, setp′ =p+ tw, divide the inequality byt2, and lett→ 0. This
condition holds for Hicksian demand at fixed utility and for quasilinear Marshallian demand. Income
effects can invalidate it for general Marshallian demand; it is not imposed automatically on every
system considered here.
3.3 Fixed-Rival Responses and Equilibrium Feedback
The scalar formula (9) extends to a firm’s response holding rival prices fixed. This is a local
fixed-rival derivative. Full equilibrium pass-through additionally allows those rivals to adjust.
Fix firmf and a tax perturbationdtf. WriteJ ff =∂ff/∂p⊤ f for the within-firm pricing block
andΛ f for the corresponding principal submatrix ofΛ. The fixed-rival response solves
Jffdpf + Λfdtf = 0.
LetW f =−Jdiag qf ≻ 0, define∥x∥Wf = (x⊤Wfx)1/2, and, for a nonzero response, set ˆvf =
dpf/∥dpf∥Wf.
14

Proposition 1(Directional fixed-rival response).At an interior stationary point with nonnegative
markups and a negative definite own-firm profit Hessian, hold rivals’ prices fixed and letdpf denote
the derivative along the resulting branch of strict local profit maxima. Fordpf̸= 0and Mf(ˆvf)> 0,
∥dpf∥Wf =
ˆv⊤ f WfΛfdtf
Mf(ˆvf)
(
2Rf(ˆvf)−κ f(ˆvf)
).(17)
Proof.See Appendix A.3.
When this local branch remains globally optimal, the derivative is also the firm’s best-response
derivative. The denominator is minus the own-firm profit curvature along the realized response
direction. Holding the direction and projected tax impulse fixed, a smaller denominator produces a
larger response. The direction itself is determined by the pricing system, however, so this identity
does not replace the matrix calculation with an independently known scalar.6
To recover equilibrium pass-through, letD be the block diagonal ofJ f containing the full
within-firm blocks, and setE=J f−D. When these blocks are invertible, define
T=−D −1E,Ψ BR =−D−1Λ.
FactoringJ f =D(I−T)gives the exact identity
Ψ = (I−T) −1ΨBR.(18)
Thus own-firm curvature governs the fixed-rival response, while the remaining inverse captures
strategic feedback across firms. Ifρ(T )< 1, successive powers ofT represent successive rounds of
rival adjustment. This additional condition does not follow from each firm’s second-order condition.
A quadratic-utility duopoly gives a globally defined illustration. Appendix A.3 specifies consumer
demand at all nonnegative prices, including the possibility of zero purchases. When both products
are purchased, demand is
qi = 3−2β−p i +βp k, k̸=i,0≤β <1.
6For one product letW =−q′ > 0. Then ˆv= sgn(dp)/ √ W,R(ˆv) =M(ˆv) = 1, and the numerator issgn(dp) √ Wdt .
Since∥dp∥ W =
√
W|dp|, cancelling these factors givesdp=dt/(2−κ).
15

At marginal costs(1, 1), prices(2, 2)form a Nash equilibrium: each firm’s price is its unique globally
optimal response to the rival’s price over allpi≥0. Quantities and markups are one. Throughout
this family, own-demand slopes are−1, own BP curvature is zero, and own-profit curvature is−2
at the equilibrium. Thus fixed-rival own-cost pass-through is always1/2. Equilibrium pass-through
instead satisfies
Jf =

 −2β
β−2

,Ψ = 1 4−β 2

 2β
β2

,Ψ1= 1 2−β 1.
As substitution strengthens, rival adjustment raises common-cost pass-through even though the
individual curvature benchmark is unchanged. Atβ= 3/4, the three responses are distinct:
∂pi
∂ci
⏐⏐⏐⏐
pk fixed
= 1 2,Ψ ii = 32 55,(Ψ1) i = 4 5.
The best-response slope with respect to the rival’s price isβ/2 = 3/8; this feedback turns the initial
one-half response into four-fifths when both costs rise. In fact, for common cost incrementst∈ [0, 1],
prices pi(t) = 2 + 4t/5form a Nash equilibrium. The example therefore illustrates equilibrium
amplification over a finite range, with no restriction confining firms to prices near the baseline.
This is an illustration of the established role of strategic feedback in incidence (Moorthy, 2005;
Alexandrov and Bedre-Defolie, 2017). It isolates the dependence of equilibrium pass-through on
substitution while holding the individual curvature benchmark fixed. For approximation, the relevant
question is how much of the joint response is omitted when rival adjustment is suppressed.
4 Finite-Series Approximation of the Pass-Through Matrix
The economic value of an approximation is that it identifies which interactions are needed for a
prediction and checks the error from leaving others out. This section uses the decomposition to
organize the equilibrium response into a direct adjustment and successive rounds of interaction.
The Neumann expansion is standard matrix algebra; its application here associates each term with
demand and ownership effects, supplies error bounds, and establishes convergence throughout the
interior common-coefficient logit model. When the full pricing Jacobian is known, a linear solve
16

remains a direct way to compute a particular response. The expansion is useful for interpreting
that response and assessing a simpler approximation.
4.1 Neumann Expansion and Error Control
Separate the normalized pricing Jacobian into its diagonal and off-diagonal parts:
A=−2I+K diag +C diag,B=K off +C off.(19)
ThusJ f =A+B. The diagonal contains own-price curvature and own-price diversion reallocation.
The remaining entries contain cross-price interactions, including those within a multiproduct firm.
WithAinvertible, define
Γ =−BA−1.(20)
The order matters:J f = (I−Γ)A, soΨ =−A −1(I−Γ) −1Λ.
Proposition 2(Neumann representation and truncation error).SupposeAis invertible and
ρ(Γ)<1. Then
Ψ =−A−1
∞∑
m=0
ΓmΛ.(21)
For integerK≥0, define the order-Kapproximation as
ΨK =−A−1
K∑
m=0
ΓmΛ.
Its exact remainder is
Ψ−Ψ K =−A−1ΓK+1(I−Γ) −1Λ.(22)
If∥Γ∥≤η <1in a consistent submultiplicative matrix norm, then
∥Ψ−Ψ K∥≤∥A −1∥∥Λ∥ηK+1 1−η .(23)
For a particular cost directionh, the same bound replaces∥Λ∥ with∥Λh∥ and the left side with
∥(Ψ−Ψ K)h∥, using the compatible vector norm.
Proof.See Appendix A.4.
17

The first two approximations are
Ψ0 =−A−1Λ,(24)
Ψ1 =−A−1Λ +A−1BA−1Λ.(25)
The leading term removes propagation through off-diagonal pricing derivatives, while retaining
ownership in the initial tax loadingΛ. The next term adds one round of interaction. Equivalently,
set T =−A−1B=A −1ΓA. ThenΨ K =∑K m=0TmΨ0, so each power acts directly on a vector of
price responses. These product-level rounds differ from the firm-level rounds in(18), whose baseline
retains entire within-firm blocks.
The convergence restriction is additional to equilibrium regularity and the firms’ second-order
conditions. Spectral radius below one ensures eventual convergence, but a small spectral radius
alone need not make low-order terms small for a nonnormal matrix. The norm bound provides an
operational sufficient condition and retains the size of the diagonal inverse and tax loading. It also
clarifies the meaning of “first order”:Ψ1 retains one round of feedback, whereas everyΨKh is a
localprediction in the size of the policy change. The bound does not control extrapolation to a large
finite policy change. Nor must adding a term reduce each entry’s error in every demand system.
Example 1(An interior logit benchmark).Consider multinomial logit with common price coefficient
α >0, sharessj > 0, and positive outside share. LetSf = ∑ j∈Jfsj and S = ∑ jsj < 1. The
first-order conditions imply a common within-firm markupmf = 1/[α(1−S f)]. In fact,
fj =
1/α−m j +∑ l∈Jfslml
1−s j
, j∈J f.
At equilibrium the numerator vanishes. Differentiating it while keeping costs fixed gives
Ajj =− 1 1−s j , B jk =



0, k̸=j, k∈J f,
Sfsk
(1−s j)(1−S f), k /∈Jf.
The within-firm off-diagonal pricing derivatives cancel at equilibrium. This cancellation shows why
an ownership-aware baseline can be accurate even before adding rival feedback. Ownership still
18

affects bothSf andΛ. In particular(Ψ 0)jj = 1−sj,(Ψ 0)jk =−sk for another product in the same
firm, and other entries vanish.
The similar propagation matrixT =−A−1Bhas nonnegative cross-firm entriesTjk =Sfsk/(1−
Sf)and zero within-firm entries. Consequently
ρ(Γ) =ρ(T)≤∥T∥ ∞ = max f
Sf(S−S f)
1−S f
≤max
f
Sf <1.(26)
Thus the expansion converges at every such interior logit equilibrium, including multiproduct
ownership. This bound concernsT, not necessarily∥Γ∥∞. Ifη =∥T∥∞, the equivalent representation
gives the shock-specific certificate
∥(Ψ−Ψ K)h∥∞≤ ηK+1 1−η ∥Ψ0h∥∞.
For three single-product firms with shares(0.20,0.15,0.10),
Ψ≈

 0.801530 0.032300 0.023147 0.028612 0.851403 0.016713
0.018289 0.014908 0.900793

 ,Ψ 1≈

 0.800000 0.031875 0.022500 0.028235 0.850000 0.015882
0.017778 0.014167 0.900000

 .
The order-1 correction captures most cross-product responses in this example. More broadly,
Appendix C reports 1,000 validated six-product logit configurations: mean relative matrix error
for order 1 is0.323%. Logit’s exact within-firm cancellation makes this a favorable benchmark,
not evidence of universal accuracy in flexible demand systems. The appendix reports finite-policy
checks separately. Exact aggregation for logit and CES is an established route to tractability (Nocke
and Schutz, 2018, 2025); the calculation here uses logit to make the convergence restriction and the
contributions of successive interactions explicit.
Remark 3(Block-diagonal refinement).When within-firm interactions are substantial, the block
decomposition in(18) may give a more informative baseline. Ifρ(T )< 1, its Neumann expansion is
Ψ =∑ m≥0T mΨBR. The same remainder argument applies, with firm blocks replacing diagonal
entries.
19

4.2 Checking a Particular Response
A researcher may need the response of one price, a price index, or the price component of consumer
welfare rather than every element ofΨ. The same contraction argument gives a check on the
particular calculation. Write the linearized pricing system as
Jfx+b= 0,
where x is the exact local price response andbis the intervention’s change in pricing incentives at
fixed prices. For a cost directionh,b= Λ h; Section 6.1 gives the loading for other interventions.
For any proposed approximationˆx, define its residualr=J fˆx+b.
Suppose T =−A−1Bsatisfies ∥T∥≤η < 1in the matrix norm induced by the chosen vector
norm. SinceJ f =A(I−T),
x− ˆx=−(I−T) −1A−1r,∥x− ˆx∥≤ ∥A−1r∥ 1−η .
For a fixed vector of weightsℓ, the dual norm gives
⏐⏐ℓ⊤(x− ˆx) ⏐⏐≤∥ℓ∥∗ ∥A−1r∥ 1−η =:E ℓ.(27)
Consequently,|ℓ⊤ˆx|>E ℓ establishes the sign of the local scalar response. This is a computational
consequence of the contraction condition: an approximation can be adequate for a particular
economic conclusion even when a bound on the entire matrix is uninformative. Choosingℓ =ej
checks a product’s price response; suitable fixed weights check a price index. Choosingℓ =−q
checks the price-mediated consumer-welfare component when that interpretation applies. The check
conditions on the pricing derivatives and intervention loading. Estimation uncertainty, direct utility
effects, and extrapolation to a finite policy change require separate treatment. Applied to estimated
demand, this bound can establish that interactions omitted by a simpler calculation do not overturn
a particular price or index prediction. It provides a conditional check on the importance of feedback
rather than inferring that importance from own-curvature estimates alone.
20

5 Small-Share Limits of Pass-Through
Small product shares do not by themselves imply weak strategic interaction. The relevant question
is how shares become small and which substitution patterns survive along that path. This section
compares demand specifications through the resulting limits of the normalized pricing Jacobian. In
some fixed-product experiments, pass-through becomes diagonal; in others, cross-product effects
and ownership remain relevant even when every inside share vanishes.
The analysis distinguishes demand derivatives evaluated along a price sequence from equilibrium
comparative statics. All matrix limits below keep the number of products fixed. To interpret a
demand-side limit as equilibrium pass-through, the sequence must consist of interior equilibria,
possibly supported by changing costs, and the limiting full pricing Jacobian must be nonsingular. A
demand-evaluation path alone does not establish those equilibrium conditions.
These comparisons connect the local decomposition to the demand-shape concerns in Miravete
et al. (2023, 2026); Compiani (2022). The issue is which restrictions a specification places on
the matrix used for a counterfactual, even when its baseline elasticities appear reasonable. I first
isolate the demand-side terms, distinguish baseline curvature from an entire normalized profile, and
then incorporate ownership. The final nested-logit calculation shows how to retain the remaining
interactions in a simple formula.
5.1 A Semi-Elasticity Representation of Pass-Through with Single-Product
Firms
When each firm produces a single product,Λ = I andC=0, so Lemma 1 implies that the
pass-through matrix simplifies to
∂p
∂t⊤ =−J−1 f =−[−2I+K] −1,
so the entries ofJf≡∂f/∂p ⊤ are
Jf,jk =



−2 +κj jj, k=j,
δjk
(
1−κ j kj ) , k̸=j. (28)
21

Thus, with single-product firms, the behavior of pass-through is governed by the diagonal and
off-diagonal entries of the normalized pricing Jacobian in (28).
A convenient way to study these objects under small-share asymptotics is through semi-elasticities.
For each productj, define
ηjj(p) :=∂ j logqj(p) = ∂pjqj(p) qj(p) , η jk(p) :=∂ k logqj(p) = ∂pkqj(p) qj(p) , k̸=j.
Thusηjj is the own semi-elasticity of demand for productj, which is negative under downward-
sloping demand, and ηjk is the cross semi-elasticity of demand for productj with respect to
pk.
Lemma 3(Semi-elasticity representation of the normalized pricing Jacobian).Assume demand is
positive and twice continuously differentiable, with a negative own-price derivative. For each product
j,
−2 +κj jj(p) =−1 + ∂pjηjj(p) ηjj(p)2 .
For eachk̸=j,
δjk(p)
(
1−κ j kj(p) ) = ∂pjηjk(p) ηjj(p)2 .
When a cross derivative is zero, the off-diagonal expression is understood through the continuous
combined formula
δjk(1−κ j kj) = qj∂jkqj (∂jqj)2− ∂kqj ∂jqj ,
which does not require division by a cross slope.
Proof.See Appendix A.5.
Lemma 3 shows that the normalized pricing Jacobian is governed by two local growth-rate objects.
The diagonal term depends on the normalized derivative of the own semi-elasticity,∂pjηjj/η2 jj, while
the off-diagonal term depends on the normalized derivative of the cross semi-elasticity,∂pjηjk/η2 jj.
This representation is helpful because it rewrites the Jacobian in terms of the local evolution of
economically interpretable demand sensitivities, rather than raw second derivatives of demand. In
particular, for small-share analysis, the key question is not the absolute size of these derivatives, but
22

how own and cross semi-elasticities change relative to the square of the own semi-elasticity along
the specified sequences of price vectors.
5.2 Baseline Curvature and Normalized Demand Profiles
Consider a sequence of price vectorsp(n) along which inside shares vanish. Suppose the normalized
coefficients converge:
−2 +κj jj(p(n))→−1 +a j, δ jk(p(n))(1−κ j kj(p(n)))→b jk.
These are assumptions on a demand system and a particular sequence; smoothness and small shares
alone do not guarantee their existence. The numbersaj and bjk describe derivatives at the baseline
price vectors. An entire own-price demand profile requires information about derivatives away from
those baselines.
To make the distinction precise, letλj,n :=−ηjj(p(n)) > 0and vary only product j’s price
by t/λj,n. This measures the price change in units of the inverse baseline semi-elasticity, so the
normalized log-demand slope at zero is always−1. Define
pj,n(t) :=p (n) + t λj,n ej, E j,n(t) := ηjj(pj,n(t)) ηjj(p(n)) , Q j,n(t) := qj(pj,n(t)) qj(p(n)) ,
Under the uniform-neighborhood conditions stated in Proposition 4, normalized curvature is
asymptotically constant on an intervalIcontaining zero. The resulting profile is
Qj,n(t)−→



e−t, a j = 0,
(1 +ajt)−1/aj, a j̸= 0,
uniformly on compact subintervals ofI∩{t : 1 +ajt> 0}. Appendix A.6 gives the full conditions,
the associated semi-elasticity limits, and the proof.
The uniform neighborhood assumptions do the substantive work. Under them,aj = 0gives
an exponential profile,aj > 0gives a power profile, and aj < 0gives a profile tending to zero
as t↑− 1/aj, if the common domain extends to that boundary. Compact convergence before the
23

boundary does not imply a literal choke price in each original demand curve. Nor does a baseline
value ofaj establish any of these profiles without the neighborhood assumptions.
More generally, writeAj,n(t) =−E′ j,n(t)/Ej,n(t)2. The exact identities
1
Ej,n(t) = 1 +
∫ t
0
Aj,n(u)du, Q j,n(t) = exp
[
−
∫ t
0
Ej,n(u)du
]
show why the entire functionAj,n, rather than only its value at zero, matters for demand away from
the baseline. At the baseline, the precise local implication is
Qj,n(t) = 1−t+ 1 2κj jj(p(n))t2 +on(t2).
Thusaj compares baseline curvature with the exponential benchmark. This distinction matters for
counterfactuals: a local derivative concerns behavior at the baseline, whereas extrapolation along a
price path requires demand shape away from it. Gamma mixed logit and nested logit below show
why a baseline curvature index cannot substitute for that additional information.
5.3 Common Demand Systems and Small-Share Paths
Table 1 compares the limiting demand-side entries for explicit experiments. Logit, CES, and mixed
logit are evaluated along positive common-price raysp(n) = λnp, with fixed mean utilities and
λn→∞ . Linear and fixed-weight Stone LA/AIDS demand instead approach a feasible boundary
for one product. Nested logit lets all nest shares vanish while conditional shares within nests
converge. Appendix B states the demand systems and proves the limits. In the mixed-logit
specifications, mixing is over a scalar price coefficient, with no random coefficients on other product
attributes. Those limits concern the specified mixtures and do not cover unrestricted correlated
random-coefficient demand.
Logit and lognormal mixed logit share the demand-side limit−I; CES has limit−(1− 1/σ)I.
With single-product firms these yield unit pass-through limits ofI, I, andσ/(σ− 1)I, respectively,
along regular equilibrium sequences. Their similarity in matrix structure does not mean that
they impose identical finite-share curvature or approximation errors. In mixed logit, the buyer-
composition terms in(14) can remain substantial at finite prices. The lognormal high-price-ray
24

Table 1: Demand-Side Limits Under Specified Small-Share Experiments
Model and experimentlim(−2 +κ j jj) limδ jk(1−κ j kj),k̸=j
Positive common-price ray; fixed finite product set
Logit−1 0
Lognormal mixed logit−1 0
CES,σ >1−1 + 1/σ0
Gamma mixed logit−1 +∂ jj logH j/ℓ2 j ∂jk logH j/ℓ2 j
Feasible boundary for productj
Linear demand−2−β jk/βjj
Stone LA/AIDS−2− cjkAjk/Ajj
Vanishing nest shares; stable conditional shares
Nested logit−1−σz j(1−z j)/B2 j σzjzk/B2 j within nest
0across nests
Notes:All entries concern the demand-side matrix−2I +K. For gamma mixing,
Hj is the integral in Proposition 6, evaluated at the fixed rayp, and ℓj =
−∂j logH j > 0. Its baseline curvature correction can have either sign. For Stone
LA/AIDS, weights are fixed,Ajk =γjk−β jωk,Ajj < 0, andcjk = limp (n) j /p(n) k ∈
(0,∞ ). Those boundary statements are rowwise. For nested logit,zj is the limiting
conditional share andBj = 1−σz j. Turning these entries into equilibrium pass-
through additionally requires the full ownership terms and a nonsingular limiting
pricing Jacobian.
result therefore does not require the finite-market pass-through predictions studied by Miravete
et al. (2023, 2026) to be near the identity. Its restrictions concern a particular selection experiment,
rather than small observed shares alone.
Gamma mixed logit gives a different mechanism. Along the common ray, relevant consumers
have price sensitivity of order1/λn. Rival inside products can therefore retain substantial conditional
choice probabilities for the consumers who remain, even though aggregate shares vanish. Demand is
regularly varying along that ray,
qj(λp)∼ Mβr Γ(r)λ−rHj(p),
but own-price perturbations change relative prices. The resulting normalized residual-demand profile
is
Qj(t) = Hj(p+te j/ℓj) Hj(p) , t>−ℓ jpj,
25

which generally has nonconstant normalized curvature. In particular,aj =∂jj logHj/ℓ2 j need not be
positive. With two equally attractive products,r = 2, δ1 =δ2 = 10, and ray prices(1, 1), numerical
quadrature givesaj≃− 0.188. A common-ray power law therefore does not determine whether
residual demand is more or less curved than the exponential benchmark. This sensitivity to the
mixing distribution complements the demand-curvature comparisons in Miravete et al. (2026).
Boundary experiments preserve a different source of interaction. Linear and Stone LA/AIDS
demand retain cross-slope ratios in the normalized Jacobian as productj’s demand or expenditure
share approaches zero. These are statements about a feasible rowwise boundary; they do not
automatically describe a simultaneously feasible whole-market equilibrium limit. A finite choke-price
interpretation further requires finite positive limiting prices.
Finally, nested logit preserves substitution within nests. Its negative baseline curvature correction
does not imply a finite-choke normalized profile. Writingz =zj andB = 1−σz, the actual own-price
profile is
Qj(t) =e−t/B( 1−z+ze −t/B)−σ,
which is positive at every finitet. Appendix B.4 derives this profile and the corresponding ownership
limit. The common lesson is that small-share pricing depends on the limiting experiment and the
substitution patterns it preserves, not on a scalar tail label alone.
5.4 Extension to Multiproduct Firms
With multiproduct ownership,
P=−J −1 f Λ,J f =−2I+K+C.
The demand-side limit of−2I +Kis only one part of this system. A diagonal demand-side limit
does not imply that diversion or its markup-weighted derivatives vanish.
A sufficient set of conditions is transparent. At fixed dimension, suppose the demand-side
diagonal entries converge to−dj, withdj > 0, the off-diagonal demand-side entries vanish, and, for
all relevant indicesℓ̸=jandk,
Dj→ℓ→0,(p ℓ−cℓ)∂pkDj→ℓ→0.
26

ThenC→0,Λ→I, and continuity of matrix inversion gives
P→diag(d −1 j ).
Appendix B verifies these ownership conditions for logit, CES, and lognormal mixed logit along the
stated rays, provided markups grow at most proportionally to the price scale. This is a fixed-product
experiment in which total inside demand vanishes; it does not cover a growing product set with
small individual shares but substantial total firm shares.
Nested logit provides a useful case in which within-nest diversion survives. LetSfg be firm
f’s limiting share within nestg, letα >0be the common price coefficient, and letσ∈ [0, 1)be
the nesting parameter. Proposition 8 shows that products in the same firm–nest group have the
common limiting markup
m∗ fg = 1−σ α(1−σS fg ).
Ownership changes markups through the share of within-nest substitution internalized by the firm.7
The limiting pass-through matrix is block diagonal by nest, and every block has row sums equal
to one: a common cost increase within a nest is passed through fully. If one firm owns the entire
nest, its limiting markup is the constant1/α, and the block is the identity. Under split ownership,
product-specific shocks can still produce within-nest spillovers. Thus surviving substitution creates
scope for ownership to matter, while the cost-shock direction and ownership pattern determine its
actual incidence.
5.5 A Group-Average Formula for Nested-Logit Incidence
The surviving within-nest interactions have a simple economic representation. Fix a nestg in the
limit of Proposition 8. Letzj be its limiting conditional product shares, with∑ j∈Jgzj = 1, and
write Sf =∑ j∈Jf∩Jgzj for the firm’s share of this nest. The following implication reduces the
limiting response to averages within ownership groups.
7For a firm confined to one nest, this is the vanishing-nest limit of the markup formula in Nocke and Schutz (2025,
Appendix B, equation (B12)), after restoring price units. For arbitrary firm–nest overlaps, the same limiting markup
follows from the reduced pricing equations in Garrido (2024). Proposition 8 derives the limiting price-response matrix;
the following corollary expresses its action through group averages.
27

Corollary 1(Nested-logit group responses).Under the conditions of Proposition 8, fix a cost
directionhwithin nestg. Define
χf =
[
1 + σSf
(1−σS f)2
]−1
, hf =
∑
k∈Jf∩Jgzkhk
Sf
forS f >0,
and
Dg =
∑
f:S f>0
Sfχf, H g =
∑
f:S f>0
Sfχf
Dg
hf.
The limiting local response is
(P∗ gh)j =h j + (1−χ f)(Hg−hf), j∈J f∩Jg, S f >0.(29)
For a group withSf = 0, the response is simplyhj. Within the nest, cross-firm pass-through entries
are nonnegative, within-firm off-diagonal entries are nonpositive, and0<(P∗ g )jj≤1.
Proof.See Appendix B.5.
The response has two parts: the product’s own cost change and a common markup adjustment
within its firm–nest group. That adjustment compares the group’s average cost change with a
weighted average across the nest. If only one product’s cost rises, rival groups raise prices weakly,
while its owner weakly lowers the prices of other products in the same group. For a common cost
change, the two averages coincide and every price moves one for one. If a firm owns the entire nest,
the averages coincide for every cost direction andP∗ g =I. A product withzj = 0can still share its
positive-share group’s markup adjustment; an individual zero share is different from a zero group
share.
Related spillover signs already appear in Moorthy (2005, equation (6)). In his displayed nested-
logit solution, each of two retailers owns all the brands in its nest, and there is no outside good. A
cost increase on one brand at one retailer generates a negative within-retailer cross-price response
and positive cross-retailer responses; a common cost change passes through fully. Here, nest shares
vanish relative to an outside option, and ownership can be split within nests or span several nests.
The identity block under complete ownership of a vanishing nest reflects the disappearance of
28

between-nest diversion along this path. It does not contradict the cross-retailer responses in his
market with positive retailer shares.
Computing a limiting response requires group averages rather than a product-level matrix
inversion, while preserving the sign and size of the remaining portfolio spillovers. The formula is
an implication of the specified nested benchmark, not an approximation guarantee at positive nest
shares. Appendix C evaluates that separate approximation question.
6 Applications
A response matrix is useful across economic questions because different interventions can change
the same pricing conditions. This section first specifies that common calculation, then applies it to
demand shifts, incidence with revenue and margin data, and ownership changes. The distinction
between an intervention’s initial incentive and the matrix that transmits it follows the general
incidence approach of Weyl and Fabinger (2013); Adachi and Fabinger (2022) and the local merger
approach of Jaffe and Weyl (2013). The contribution here is to evaluate and interpret that
transmission through the demand and ownership structure developed above.
6.1 General Changes in Pricing Incentives
Let a scalar parameterθ smoothly change demand, product-specific marginal costs, or the weights
on internalized profits. Keep the product set fixed and suppose the pricing equations admit a
differentiable equilibrium branch at the baseline, withJf nonsingular. The own-price demand slopes
remain negative locally, and demand is twice continuously differentiable in prices andθ. Write
Fj(p,θ) =q j(p,θ) +
∑
l
Ωjl(θ)(pl−cl(θ))ql,j(p,θ), f j =−F j/qj,j,
whereΩ jj = 1. At equilibriumFj = 0, so differentiation at fixed prices gives the incentive loading
bj :=∂ θfj =− qj,θ +∑ l Ωjlmlql,jθ +∑ l Ωjl,θmlql,j−∑ l Ωjlcl,θql,j qj,j .(30)
29

All terms are evaluated at the baseline. The derivative of the normalization drops out because it
multipliesF j = 0. Implicit differentiation therefore yields
dp
dθ =−J−1 f b.(31)
For a pure cost change,b= Λc θ. More generally, ifΛis invertible, the vector h = Λ−1bis a
cost-equivalent incentive and the response isΨh. Equation (31) remains valid without this extra
invertibility condition. The Neumann approximation in Section 4 applies directly withbreplacing
Λh.
The demand terms in(30) identify what a demand-changing intervention requires. Its effect on
sales, qj,θ, is only one component; the effect on price sensitivities,ql,jθ, also changes the marginal
value of repricing. This distinction matters for smooth changes in product quality, consumer
exposure, or other demand shifters. An experiment that measures sales effects at unchanged prices
need not reveal the resulting pricing response. The formula specifies the additional derivatives
required, conditional on the maintained pricing model.
A demand-translation illustration.Suppose the intervention has the particular formq(p,θ ) =
Q(p−vθ ), with fixed costs and ownership and a fixed vectorv in price units. Setting~p =p−vθ
changes effective marginal costs to~c =c −vθ , while preserving every markup and demand function
in the transformed pricing problem. Hence
dp
dθ = (I−Ψ)v.(32)
For a shift in only productk’s willingness to pay, its own price response is(1− Ψkk)vk, and another
product’s response is−Ψjkvk. The identity shows how the same matrix governs a demand-side
intervention with a different initial incentive. Additive mean-utility changesβjθ in logit with a
common price coefficientα provide an example, withvj =βj/α. Arbitrary demand shifts, including
changes in price sensitivities, instead require the general loading above.
For interventions that change utility directly,−q⊤dpmeasures only the price-mediated consumer-
welfare effect. The direct utility effect must also enter a total welfare calculation. The next two
applications hold demand primitives fixed and state the welfare interpretation needed there.
30

6.2 Consumer Welfare with Revenue and Margin Data
Revenues and relative margins can be more readily available than separate product prices and
quantities. This motivates expressing incidence in percentage units, as in the related merger
application of Koh (2025). The transformation itself is exact. Using it with limited data, however,
requires restrictions on pass-through: revenues and margins alone do not identify demand curvature
or the equilibrium response matrix. Here logit and CES provide transparent examples of what those
restrictions imply.
Assume positive baseline prices and marginal costs, and define proportional cost shifters by
cj(τj) =c jeτj,Ψ τ≡ ∂logp ∂τ⊤ .
A differentialdτj is a proportional marginal-cost change. LetΨdenote unit-cost pass-through, and
write ˆp= diag(p j)and ˆc= diag(c j).
Lemma 4(Percentage pass-through and unit-cost pass-through).At a regular interior equilibrium
with positive prices and costs, and atτ=0,
Ψτ =ˆp−1Ψˆc.
Proof.See Appendix A.7.
Each column of this expression converts a proportional cost change into a unit-cost change;
each row converts the resulting price change into a proportional price change. It is a change of
coordinates, rather than an identification result.
To interpret model comparisons such as the finite cost experiment in Miravete et al. (2023,
Section 4.2), both the shock and the reported units must be matched. A common proportional cost
change has local price responseΨcand percentage responseΨτ 1= ˆp−1Ψc. A finite cost change
additionally requires an equilibrium calculation or control of the linearization error. The following
model-specific limits clarify the relation between unit and percentage pass-through.
31

Lemma 5(Unit-cost pass-through under logit and CES).Fix a finite number of products, an
ownership structure, and demand parameters. Consider sequences of regular interior equilibria with
positive prices and costs and nonnegative markups.
(i) Under multinomial logit with a common price coefficient, if quantity shares satisfy∥s∥→ 0,
then
Ψlogit =I+O(∥s∥).
(ii) Under finite-market CES with substitution parameterσ > 1, if expenditure shares satisfy
∥w∥→0and all relative pricesp j/pk remain uniformly bounded, then
ΨCES = σ σ−1 I+O(∥w∥).
Proof.See Appendix A.8.
These are sequences of equilibria, potentially supported by changing costs. Evaluating demand
at arbitrary high prices with fixed costs does not by itself produce such a sequence. Fixed product
dimension also matters: small individual shares need not eliminate portfolio effects when the number
of products grows.
Proposition 3(Percentage pass-through under logit and CES).Under the corresponding hypotheses
of Lemma 5, assume in addition that relative pricespj/pk and cost sharescj/pj remain uniformly
bounded. Then
Ψτ logit = diag(1−µ j) +O(∥s∥),
Ψτ CES =I+O(∥w∥),
whereµ j = (pj−cj)/pj is the relative margin.
Proof.See Appendix A.9.
The comparison concerns limiting responses. In logit, a unit-cost increase is approximately
passed through one-for-one, so percentage pass-through is the cost share1−µ j. Under CES,
unit-cost pass-through approachesσ/(σ− 1)while the cost share approaches(σ− 1)/σ; these factors
32

cancel. Bounded relative prices and cost shares control the rescaling error without requiring absolute
prices to stay bounded.
A finite-share CES benchmark.Exact percentage pass-through of one holds under the separate
assumption of exogenous isoelastic residual demandq =Ap−σ with A fixed, since optimal price is
then σc/(σ− 1). Single-product ownership alone does not impose this assumption. With one inside
CES product and a fixed outside alternative, demand and expenditure share are
q(p) = Bap−σ
1 +ap 1−σ, w= ap1−σ 1 +ap 1−σ.
The firm’s own elasticity magnitude isE =σ− (σ− 1)w, notσ. The first-order condition gives
c=p(E−1)/E. Since
dw
dlogp =−(σ−1)w(1−w), dlogc dlogp = 1 + (σ−1) 2w(1−w) E(E−1) = σ E,
exact percentage pass-through is
dlogp
dlogc = E σ = 1− σ−1 σ w.(33)
It is below one at a positive inside share and tends to one as that share vanishes. A cost-induced price
increase lowers the firm’s share, making residual demand more elastic and reducing the percentage
markup. For example,σ = 2,B = 2,a = 1,p = 1, andc = 1/3give w = 1/2, unit-cost pass-through
9/4, and percentage pass-through3/4. In a market with several firms, this scalar calculation holds
rivals’ prices fixed; full equilibrium requires the matrix response. Figure 5 illustrates the scalar
formula.
Local consumer-welfare accounting.Let Rj =pjqj. WritedCS for the consumer-welfare dif-
ferential in baseline monetary units. Under quasilinear preferences this is the usual consumer-surplus
differential. With income effects, including the standard expenditure-based CES interpretation, it
is the first-order money-metric welfare change at the baseline; no globally integrable Marshallian
33

consumer-surplus function is presumed. In either interpretation,
dCS=−q ⊤dp=−R ⊤Ψτdτ.
With uniformly bounded revenues along the fixed-dimensional sequences above,
dCSlogit =−
∑
j
Rj(1−µ j)dτj +O(∥s∥∥dτ∥),(34)
dCSCES =−
∑
j
Rjdτj +O(∥w∥∥dτ∥).(35)
These remainders describe error in the local welfare derivative caused by the small-share approxima-
tion. Replacing a differential by a finite cost change introduces a separate linearization error. Even
with a single inside CES product, the finite-share revenue weight is the factor in (33), rather than
one.
The formulas show what revenue and margin data can support under maintained demand
restrictions. They do not establish those restrictions or reveal the share-based approximation error
from revenues and margins alone. Moreover,µj is a product’s price-minus-marginal-economic-cost
margin divided by price. An accounting profit margin, or an average over products priced separately,
is not automatically this object. An application must justify the mapping from the observed accounts
to products, pricing portfolios, and marginal costs.
6.3 Local Merger Analysis
A merger changes the sales that a firm internalizes when setting each price. The resulting incentive
shift can be written in the same units as a cost shock. This connection underlies upward-pricing-
pressure analysis (Farrell and Shapiro, 2010) and the multiproduct first-order approach of Jaffe and
Weyl (2013). The purpose here is to express the distinction between cost and merger responses
through the demand and ownership decomposition, and to clarify when its approximations apply.
The incentive change and its exact local response.Hold demand and marginal costs fixed,
and letΩ pre andΩ post describe premerger and postmerger ownership. Letp0 be a regular premerger
equilibrium andm=p − cthe vector of absolute markups. The shift in the normalized pricing
34

equations is
gj(p) =f j(p; Ωpost)−f j(p; Ωpre)
=
∑
l̸=j
(Ωpost jl −Ω pre jl )(pl−cl)Dj→l(p),(36)
or, writingΛa = Λ(p; Ωa),
g(p) = (Λpre−Λ post)m.(37)
For substitutes and positive markups, newly internalized diversion creates upward pricing pressure
on the merging firms’ products. Products with unchanged ownership incentives have zero entries in
g, but their equilibrium prices can still respond through the pricing Jacobian.
To distinguish a derivative from a completed merger, introduce an incentive parameterη:
f(p,η) =f(p; Ω pre) +ηg(p).
Atη = 0this is the premerger system, and atη = 1it is the postmerger system. Between these
endpoints it interpolates the newly internalized profit weights. The implicit-function theorem gives
the exact derivative at the baseline,
dp
dη
⏐⏐⏐⏐
η=0
=−[J pre(p0)]−1g(p0),J a = ∂f(p; Ωa) ∂p⊤ .(38)
IfΛ pre(p0)is invertible, define the cost-equivalent vector
tmerger = [Λpre(p0)]−1g(p0).
Then (38) equalsΨ pretmerger. For premerger single-product firms,Λ pre = I and this vector is
simplyg. The normalized incentive shift and its local response remain well defined even when a
cost-equivalent vector cannot be recovered by inversion.
Why the postmerger Jacobian differs.Jaffe and Weyl (2013) distinguish the matrix that
transmits merger incentives from ordinary premerger cost pass-through and study conditions under
which the latter approximates the former. In the normalization used here, one Newton step for the
35

postmerger system atp0 is
∆pN =−[J pre(p0) +gp(p0)]−1g(p0),g p = ∂g ∂p⊤,(39)
provided the displayed matrix is nonsingular. Since the demand componentKis invariant to
ownership at fixed prices, Lemma 1 implies
gp(p) =C(p; Ω post)−C(p; Ω pre).
Equivalently, its(j,k)entry is
(gp)jk = (Λpre−Λ post)jk + ∑
l
ml
∂(Λpre−Λ post)jl
∂pk
.
The first term records the change in the margins on newly internalized sales; the second records
how diversion changes with prices. This is the ownership part of the difference between the two
Jacobians.
The exact derivative in(38) is invariant to a smooth, nonsingular row rescaling of the pricing
equations at their baseline zero. The finite Newton approximation(39) need not be: premerger prices
generally do not solve the postmerger equations, so derivatives of a price-dependent normalization
enter its Jacobian. Thus(39) specifies an approximation in this paper’s normalization; it is not an
assertion that all formulations of a postmerger Newton step coincide.
Approximation, information, and welfare.The approximation results earlier in the paper
can simplify the inverse in a local merger calculation when their conditions hold. Logit, for
example, has an identity limit for unit-cost pass-through along the fixed-dimensional small-share
sequences considered here. Such limits help interpret the simulation evidence on pricing-pressure
approximations in Miller et al. (2017). They do not identify curvature from slopes alone, or establish
that an elasticity-based diagonal correction is more accurate than the identity. A retained feedback
term is useful when its approximation error is controlled or its performance is validated in the
relevant demand environment.
36

Three distinct uncertainties remain in an application: measurement of the incentive vector and
pricing derivatives, approximation of the local inverse, and extrapolation from the local derivative
to the completed merger. A good approximation to the first two objects does not bound the third.
If an equilibrium path exists and remains regular overη∈[0,1], its exact price change satisfies
p(1)−p(0) =−
∫ 1
0
[Jpre(p(η)) +ηgp(p(η))]−1g(p(η))dη.
The baseline formula replaces this changing integrand by its value at zero. A finite-merger application
therefore requires control of that movement or a check against solved counterfactual equilibria.
For a small incentive change, the consumer-welfare differential isdCS =−q⊤dp, under the
monetary interpretation given above. With unchanged costs, the change in aggregate operating
profit is
dPS=q ⊤dp+m ⊤Gdp,G= ∂q ∂p⊤.
The quantity-adjustment term cannot generally be omitted. Nor can the envelope theorem for each
premerger firm’s own pricing choices be applied to the combined profit of the newly merged entity
at premerger prices: those prices need not maximize its joint profit. Under quasilinear preferences,
total surplus changes bydW =m⊤Gdpwhen costs and product characteristics are unchanged.
These accounting identities keep the welfare calculation separate from the approximation used to
obtain the price response.
7 Conclusion
The same change in pricing incentives can have different market-wide effects depending on how
demand and ownership transmit it across products. This paper develops a tractable representation of
that transmission under multiproduct Bertrand competition. The normalized pricing system makes
own curvature, changes in substitution, and portfolio internalization explicit. The approximation
and limiting results then establish when a simpler calculation retains the interactions needed for
incidence analysis.
Two findings guide that simplification. Individual profit curvature describes a firm’s adjustment
with rivals fixed, while equilibrium feedback determines how those adjustments combine. Small
37

unconditional shares likewise leave open whether consumers continue to substitute within a nest or
among products purchased by a selected group of consumers. The logit and CES benchmarks yield
diagonal limits under the stated experiments, while nested logit and gamma mixing can preserve
cross-product responses. In the nested case, a group-average formula retains those spillovers without
a product-level matrix inversion.
These results connect the general use of pass-through in first-order analysis to explicit features of
empirical demand models. Once an intervention’s effect on pricing incentives is specified, the same
local response system applies to changes in costs, demand, or ownership. The series remainder and
residual bound assess approximation of that response; model-specific limits reveal which demand
restrictions support familiar incidence benchmarks. The welfare and merger applications illustrate
how these ingredients enter substantive calculations, with the direct effects of an intervention and
the extrapolation to a finite change treated separately.
This interpretation helps explain how specification-sensitive demand derivatives enter incidence
predictions and how the effects of omitted interactions can be assessed. The framework also
identifies an empirical priority. A policy prediction may depend on mixed demand derivatives or
incentive shifts that the available variation only weakly disciplines. Establishing which conclusions
remain valid under that uncertainty requires additional identification or robustness results. The
characterization here provides a basis for that work by specifying the relevant combinations of
demand shape, ownership, and equilibrium feedback.
Disclosure of AI UseThe author used OpenAI’s ChatGPT to assist with literature searches,
mathematicalchecks, coding, anddraftingandrevisingthetext. Theauthorretainssoleresponsibility
for the paper’s content, including its arguments, results, references, and any errors.
References
Adachi, Takanori and Michal Fabinger (2022) “Pass-through, welfare, and incidence under imperfect
competition,”Journal of Public Economics, 211, 104589.
Alexandrov, Alexei and Özlem Bedre-Defolie (2017) “LeChatelier–Samuelson principle in games
and pass-through of shocks,”Journal of Economic Theory, 168, 44–54.
Armstrong, Mark and John Vickers (2018) “Multiproduct Pricing Made Simple,”Journal of Political
Economy, 126 (4), 1444–1471, 10.1086/697902.
38

(2023) “Multiproduct Cost Pass-Through: Edgeworth’s Paradox Revisited,”Journal of
Political Economy, 131 (10), 2645–2665, 10.1086/724573.
Besanko, David, Jean-Pierre Dubé, and Sachin Gupta (2005) “Own-brand and cross-brand retail
pass-through,”Marketing Science, 24 (1), 123–137.
Birchall, Cameron, Debashrita Mohapatra, and Frank Verboven (2024) “Estimating Substitution
Patterns and Demand Curvature in Discrete-Choice Models of Product Differentiation,”Review
of Economics and Statistics, 10.1162/rest_a_01463, Advance online publication, June 14.
Bulow, Jeremy I and Paul Pfleiderer (1983) “A note on the effect of cost changes on prices,”Journal
of Political Economy, 91 (1), 182–185.
Compiani, Giovanni (2022) “Market Counterfactuals and the Specification of Multiproduct Demand:
A Nonparametric Approach,”Quantitative Economics, 13 (2), 545–591, 10.3982/QE1653.
Dearing, Adam, Lorenzo Magnolfi, Daniel Quint, Christopher Sullivan, and Sarah Waldfogel (2026)
“Learning Firm Conduct: Pass-Through as a Foundation for Instrument Relevance,”https://www.
lorenzomagnolfi.com/files/papers/LearningFirmConduct.pdf, Working paper, April 9.
Farrell, Joseph and Carl Shapiro (2010) “Antitrust Evaluation of Horizontal Mergers: An Economic
Alternative to Market Definition,”The B.E. Journal of Theoretical Economics, 10 (1), 10.2202/
1935-1704.1563.
Froeb, Luke, Steven Tschantz, and Gregory J Werden (2005) “Pass-through rates and the price
effects of mergers,”International Journal of Industrial Organization, 23 (9-10), 703–715.
Garrido, Francisco (2024) “An aggregative approach to pricing equilibrium among multi-product
firms with nested demand,”The RAND Journal of Economics, 55 (3), 359–374, 10.1111/
1756-2171.12472.
Jaffe, Sonia and E Glen Weyl (2013) “The first-order approach to merger analysis,”American
Economic Journal: Microeconomics, 5 (4), 188–218.
Koh, Paul S. (2025) “Merger Analysis with Unobserved Prices,” 10.48550/arXiv.2404.07684,
arXiv:2404.07684, version 6, August 30.
MacKay, Alexander, Nathan H Miller, Marc Remer, and Gloria Sheu (2014) “Bias in reduced-form
estimates of pass-through,”Economics Letters, 123 (2), 200–202.
Miller, Nathan H, Marc Remer, Conor Ryan, and Gloria Sheu (2016) “Pass-through and the
prediction of merger price effects,”The Journal of Industrial Economics, 64 (4), 683–709.
(2017) “Upward pricing pressure as a predictor of merger price effects,”International
Journal of Industrial Organization, 52, 216–247.
Miravete, Eugenio J, Katja Seim, and Jeff Thurk (2023) “Pass-through and tax incidence in
differentiated product markets,”International Journal of Industrial Organization, 90, 102985,
10.1016/j.ijindorg.2023.102985.
(2026) “Elasticity and curvature of discrete choice demand models,” https://
eugeniomiravete.com/PDF/MST_Curvature.pdf, Working paper, January.
39

Moorthy, Sridhar (2005) “A general theory of pass-through in channels with category management
and retail competition,”Marketing Science, 24 (1), 110–122.
Mrázová, Monika and J Peter Neary (2017) “Not so demanding: Demand structure and firm
behavior,”American Economic Review, 107 (12), 3835–3874.
Nocke, Volker and Nicolas Schutz (2018) “Multiproduct-firm oligopoly: An aggregative games
approach,”Econometrica, 86 (2), 523–557.
(2025) “An Aggregative Games Approach to Merger Analysis in Multiproduct-Firm
Oligopoly,”The RAND Journal of Economics, 56 (3), 233–250.
Sangani, Kunal (2026) “Complete Pass-Through in Levels,”The Quarterly Journal of Economics,
141 (2), 1077–1135, 10.1093/qje/qjag014.
Tyagi, Rajeev K (1999) “A characterization of retailer response to manufacturer trade deals,”
Journal of Marketing Research, 36 (4), 510–516.
Weyl, E Glen and Michal Fabinger (2013) “Pass-through as an economic tool: Principles of incidence
under imperfect competition,”Journal of Political Economy, 121 (3), 528–583.
Appendix
A Proofs
The proofs follow the order of the main results. The first three establish the pricing decomposition
and distinguish individual profit curvature from equilibrium feedback. The next group establishes
the approximation and demand-profile results. The final proofs justify the incidence transformations
and their logit and CES limits.
A.1 Proof of Lemma 1
Writeq j,k =∂q j/∂pk andq j,kl =∂ 2qj/∂pk∂pl. The normalized equation is
fj =− qj qj,j −(pj−cj) + ∑ l̸=j Ωjl(pl−cl)Dj→l.
The quotient rule gives
∂pj
(
− qj
qj,j
)
=−1 + qjqj,jj
q2 j,j , ∂ pk
(
− qj
qj,j
)
=− qj,k
qj,j
+ qjqj,jk
q2 j,j (k̸=j).
40

The own markup contributes another−1on the diagonal. Differentiating the ownership term yields
1{k̸=j}Ω jkDj→k +
∑
l̸=j
Ωjl(pl−cl)∂Dj→l ∂pk .
Together these derivatives are exactly−2I +K+C. When qj,k̸= 0, substitutingδjk =−qj,k/qj,j
andκj kj =qjqj,kj/(qj,kqj,j)gives Kjk =δjk(1−κj kj). The expanded expression remains defined when
the cross slope is zero.
Mixed-logit buyer composition.For (14), supposesij > 0is twice continuously differentiable
on an open price neighborhood. Assume integrable envelopes justify differentiating its integral twice
and thatsij∥∇logs ij∥2 is integrable there. Let ¯sj = ∫ sijdF, wij = sij/¯sj, andgij =∇p logsij.
Sinceq j =M¯sj with fixedM,
∇p logqj =E j[gij], ∂ pkwij =w ij
(
gij,k−Ej[gij,k]
)
.
Differentiating the first identity, including the derivative of these weights, yields
∂pkpl logqj =E j[∂pkpl logsij] +Ej[gij,kgij,l]−E j[gij,k]Ej[gij,l],
which proves (14). Writingηjj =∂ pj logqj <0, the quotient rule also gives
Kjj = 1 +∂pjpj logqj η2 jj , K jk = ∂pjpk logqj η2 jj (k̸=j).
Thus the mixture identity supplies exactly the log-demand derivatives entering the demand compo-
nent of the pricing Jacobian.
For a specialization, let typei’s utility from productj be vij−α ipj +ϵij, withαi > 0, the
outside option’s deterministic utility normalized to zero, and independent type-I extreme-value
choice shocks. The joint distribution of(αi,vi1,...,v iJ)is otherwise unrestricted subject to the
stated integrability conditions. Setaij =αi(1−sij). Individual logit derivatives givegij,j =−aij,
gij,k =α isik fork̸=j, and
∂pjpj logsij =−α 2 isij(1−s ij), ∂ pjpk logsij =α 2 isijsik (k̸=j).
41

Consequently,
Kjj =κ j jj = 1 + Varj(aij)−E j[α2 isij(1−s ij)] Ej[aij]2 ,
Kjk = Ej[α2 isijsik]−Cov j(aij,αisik) Ej[aij]2 , k̸=j.
The own-price expression balances a nonnegative variance component against individual logit log-
concavity. A change in the preference distribution can alter both components; the expression does
not assert a monotone effect of every increase in heterogeneity. The cross-price expression shows why
own curvature alone does not determine the demand-side interaction terms. These are finite-price
derivative identities, not assertions about the size of equilibrium spillovers in a particular estimated
model. The general mixture identity also allows nonlinear price utility; its individual Hessian then
includes the corresponding utility-curvature terms.
A.2 Proof of Lemma 2
Along the pathpf +tv, profits areΦ f,v(t) =∑ j∈Jf (mj +tvj)ϕj,v(t). Differentiating twice gives
Φ′′ f,v(0) = 2 ∑
j
vjϕ′ j,v(0) + ∑
j
mjϕ′′ j,v(0) =−2S f(v) +Mf(v)κf(v).
The equality∑ jvjϕ′ j,v(0) = v⊤Jqfv =−Sf(v)uses that a quadratic form depends only on the
symmetric part. The aggregate definition ofκf applies wheneverMf(v)> 0, including directions
with zero product-level first derivatives. Factoring outMf(v)yields the identity and the equivalent
directional inequality.
If all markups are positive,Mf(v) = (J qfv)⊤ diag(mj/qj)(Jqfv). Nonsingularity ofJ qf then
givesMf(v)> 0for every nonzerov. The equivalence with negative semidefiniteness of the profit
Hessian follows by testing its quadratic form in every direction.
42

A.3 Proof of Proposition 1
Let Hf =∇2 pf p⊤ f Πf andF f =∇pf Πf. Sincef f =W−1 f Ff, differentiation at a stationary point
removes the derivative of the normalizing matrix and gives
Wf Jff =H f.
In particular, strict negative definiteness ofHf makes the own-firm pricing block invertible. The
implicit function theorem gives a differentiable branch of stationary prices with rivals fixed, and
continuity of the Hessian makes these prices strict local profit maxima. Premultiplying its fixed-rival
response equation byˆv⊤ f Wf and writingdpf =aˆvf, wherea=∥dp f∥Wf >0, gives
a(−ˆv⊤ fHf ˆvf) = ˆv⊤ f WfΛfdtf.
By Lemma 2,−ˆv⊤ fHf ˆvf =M f(ˆvf)[2Rf(ˆvf)−κ f(ˆvf)]>0. Division proves (17).
A globally defined example of strategic feedback.Let0≤β < 1. A quasilinear consumer
chooses nonnegative quantities to maximizeuβ(q)−p ⊤q, where
uβ(q1,q 2) = 3−2β 1−β (q1 +q 2)− q2 1 + 2βq1q2 +q 2 2 2(1−β 2) .
The utility Hessian is negative definite, and the objective tends to minus infinity as∥q∥→∞ .
Consumer demand is therefore uniquely defined at every nonnegative price vector. When both
quantities are positive, the consumer’s first-order conditions give
qi = 3−2β−p i +βp k, k̸=i.
At boundaries, demand is determined by the nonnegativity constraints in the consumer’s problem;
the affine expressions are not extended to negative quantities. In a neighborhood of(p1,p 2) = (2, 2),
both goods are purchased, and demand is smooth, downward sloping, and substitutable.
Each firm sells one product, has marginal cost one, and can choose any nonnegative price. Fix
its rival’s price atpk = 2. For1≤p i≤ 3, demand for its own good is3−pi, while its rival’s demand
43

is1 + β(pi− 2)> 0. Atpi≥ 3, its own demand is zero. Thus, for prices at or above cost, its profit is
πi(pi,2) =



(pi−1)(3−p i) = 1−(p i−2) 2,1≤p i≤3,
0, p i≥3.
Prices below cost yield nonpositive profit. Hencepi = 2is the unique globally optimal response
to pk = 2, proving that(2, 2)is a Nash equilibrium over unrestricted nonnegative prices. Baseline
quantities and markups are one,qi,i =−1,q i,ii = 0, andπi,ii =−2.
Within the positive-demand region, the normalized pricing condition is
fi = 3−2β+c i−2pi +βp k = 0.
The Jacobian has diagonal−2and off-diagonal β, with eigenvalues−2±β <0. Differentiation gives
Ψ = 1 4−β 2

 2β
β2

.
These derivatives describe a branch of Nash equilibria, not merely stationary points. To see this, at
the baseline both quantities are strictly positive when firmi prices at its cost and the rival charges
two: they are2and1 −β . This remains true for costs and rival prices sufficiently near the baseline.
Starting at cost, an increase inpi lowers its own demand and raises rival demand until its own
quantity reaches zero. Profit on this interval is a strictly concave quadratic; above the choke price it
is zero, and below cost it is nonpositive. The nearby solution to the pricing conditions is therefore
the unique global best response to the nearby rival price. The matrix formula accordingly gives
equilibrium cost derivatives.
Forβ = 3/4, a finite common-cost experiment can also be verified directly. Setci = 1 +t for
t∈ [0, 1]and p∗ i = 2 + 4t/5. At these prices, each quantity and markup is1−t/ 5> 0. Holding
the rival atp∗ k, demand evaluated atpi =ci is2 − 2t/5for firm i and1 /4−t/ 20for its rival, both
positive. Forpi≥c i, own demand therefore remains affine until it reaches zero, while rival demand
44

stays positive. The unique maximizer of the resulting profit quadratic is
pi = (3/2) + (3/4)p∗ k +ci 2 = 2 + 4 5t.
It yields positive profit and dominates every below-cost or zero-demand deviation. This proves the
asserted Nash equilibrium and exact four-fifths common-cost pass-through throughoutt∈[0,1].
A.4 Proof of Proposition 2
The factorizationJ f = (I− Γ)A, withΓ =−BA−1, givesΨ =−A−1(I− Γ)−1Λ. Sinceρ(Γ)< 1,
the Neumann series for(I− Γ)−1 converges. Subtracting the terms with powers0throughK leaves
∞∑
m=K+1
Γm = ΓK+1(I−Γ) −1,
which proves the exact remainder, preserving the order ofA−1 andΛ. If ∥Γ∥≤η < 1, submulti-
plicativity and the geometric series bound this tail byηK+1/(1−η ). Multiplying by the bounds on
A−1 andΛ, or onΛhfor a fixed direction, proves the stated inequalities.
A.5 Proof of Lemma 3
Sinceη jj(p) = ∂jqj(p) qj(p) , differentiating with respect topj gives
∂jηjj(p) = qj(p)∂jjqj(p)−(∂ jqj(p))2 qj(p)2 .
Dividing byηjj(p)2 = (∂jqj(p))2 qj(p)2 yields
∂jηjj(p)
ηjj(p)2 = qj(p)∂jjqj(p) (∂jqj(p))2 −1 =κ j jj(p)−1,
which gives the first identity.
Next, fork̸=j,η jk(p) = ∂kqj(p) qj(p) , so
∂jηjk(p) = qj(p)∂kjqj(p)−∂ kqj(p)∂jqj(p) qj(p)2 .
45

Dividing byηjj(p)2 = (∂jqj(p))2/qj(p)2 gives
∂jηjk(p)
ηjj(p)2 = qj(p)∂kjqj(p) (∂jqj(p))2 − ∂kqj(p) ∂jqj(p).
Usingδ jk(p) =− ∂kqj(p) ∂jqj(p) andδ jk(p)κj kj(p) =− qj(p)∂kjqj(p) (∂jqj(p))2 , we obtain
∂jηjk(p)
ηjj(p)2 =−δ jk(p)κj kj(p) +δjk(p) =δ jk(p) ( 1−κ j kj(p) ) ,
as claimed. If a cross slope vanishes, the preceding combined expression remains well defined and
provides the stated continuous extension.
A.6 Normalized Demand Profiles: Statement and Proof
Use the normalized price pathpj,n(t) =p (n) + (t/λj,n)ej, whereλj,n =−η jj(p(n))>0, and define
Ej,n(t) = ηjj(pj,n(t)) ηjj(p(n)) , G jk,n(t) = ηjk(pj,n(t)) λj,n , Q j,n(t) = qj(pj,n(t)) qj(p(n)) .
The following conditional benchmark supplies the demand-profile statement used in Section 5.
Proposition 4(Constant-curvature normalized profiles).Let I be a common open interval contain-
ing zero. Suppose that, eventually on every compact subinterval ofI, demand alongpj,n(t)is positive,
twice continuously differentiable, and has a negative own-price derivative. Assume, uniformly on
those compact subintervals,
− E′ j,n(t) Ej,n(t)2→a j, G′ jk,n(t) Ej,n(t)2→b jk (k̸=j),
where the limits are constants, and supposeGjk,n(0)→ρ jk. Then:
(i) The baseline normalized Jacobian coefficients converge to−1 +aj andb jk, respectively.
(ii) On every compact subinterval ofI∩{t: 1 +a jt>0},
Ej,n(t)→ 1 1 +ajt, G jk,n(t)→



ρjk +bjkt, a j = 0,
ρjk + bjk aj
(
1− 1 1 +ajt
)
, a j̸= 0,
46

uniformly.
(iii) On the same compact subintervals,
Qj,n(t)→Q j(t) :=



e−t, a j = 0,
(1 +ajt)−1/aj, a j̸= 0,
uniformly.
Proof.
Part (i).By Lemma 3, −2 +κj jj =−1 + ∂pjηjj η2 jj , and δjk(1−κj kj) = ∂pjηjk η2 jj . From the definitions of
Ej,n andG jk,n,
− E′ j,n(t) Ej,n(t)2 = ∂pjηjj
(
p(n) j +t/λj,n,p (n) −j )
ηjj
(
p(n) j +t/λj,n,p (n) −j )2 ,
and, for eachk̸=j,
G′ jk,n(t)
Ej,n(t)2 =
∂pjηjk
(
p(n) j +t/λj,n,p (n) −j )
ηjj
(
p(n) j +t/λj,n,p (n) −j )2 .
Evaluating att= 0and using the assumed convergence therefore gives
∂pjηjj(p(n))
ηjj(p(n))2 →a j, ∂pjηjk(p(n)) ηjj(p(n))2 →b jk.
Substituting into the identities above yields
−2 +κj jj(p(n))→−1 +a j, δ jk(p(n)) ( 1−κ j kj(p(n)) ) →b jk.
Part (ii).Fix a compact subinterval K⊂I∩{t : 1 +ajt> 0}. Enlarge it, if necessary, to the
compact interval joiningK to zero; this interval remains inside the same domain. All uniform
bounds below are taken on that enlarged interval. Define
cj,n(t) :=− E′ j,n(t) Ej,n(t)2.
47

By assumption,cj,n→a j uniformly onK. SinceE j,n(0) = 1,
(
1
Ej,n(t)
)′
=c j,n(t), 1 Ej,n(0) = 1,
so
1
Ej,n(t) = 1 +
∫ t
0
cj,n(s)ds.
Uniform convergence ofcj,n implies
sup
t∈K
⏐⏐⏐⏐⏐ 1 Ej,n(t)−(1 +a jt) ⏐⏐⏐⏐⏐→0.
Because1 +a jtis bounded away from zero onK, inversion is continuous, and hence
Ej,n(t)→E j(t) :=



1, a j = 0,
1
1 +ajt, a j̸= 0,
uniformly onK.
Next fixk̸=j, and define
djk,n(t) :=
G′ jk,n(t)
Ej,n(t)2.
By assumption,djk,n→b jk uniformly onK. SinceE j,n→E j uniformly onK, it follows that
G′ jk,n(t) =d jk,n(t)Ej,n(t)2→b jkEj(t)2
uniformly onK. IfG jk,n(0)→ρ jk, then
Gjk,n(t) =G jk,n(0) +
∫ t
0
G′ jk,n(s)ds
impliesG jk,n→G jk uniformly onK, where
Gjk(t) =ρ jk +
∫ t
0
bjkEj(s)2ds.
48

Evaluating the integral gives
Gjk(t) =



ρjk +bjkt, a j = 0,
ρjk + bjk aj
(
1− 1 1 +ajt
)
, a j̸= 0.
Part (iii).From the definition ofQ j,n,
Q′ j,n(t)
Qj,n(t) = 1 λj,n ηjj ( p(n) j +t/λj,n,p (n) −j ) =−E j,n(t), Q j,n(0) = 1.
Hence
Qj,n(t) = exp
(
−
∫ t
0
Ej,n(s)ds
)
.
SinceE j,n→E j uniformly onK, we obtain
Qj,n(t)→Q j(t) := exp
(
−
∫ t
0
Ej(s)ds
)
uniformly onK. Substituting the expression forEj yields
Qj(t) =



e−t, a j = 0,
(1 +ajt)−1/aj, a j̸= 0.
This completes the proof.
A.7 Proof of Lemma 4
Becausecj(τj) =cjeτj, we havedc= ˆcdτ at τ =0. Since an additive unit tax shock and an additive
marginal-cost shock enter the pricing system in the same way, the unit-cost pass-through matrix
also givesdp= Ψdc.Therefore,dlogp= ˆp−1dp= ˆp−1Ψˆcdτ,soΨ τ =ˆp−1Ψˆc.
A.8 Proof of Lemma 5
All bounds below concern a fixed finite number of products and the equilibrium sequences in the
statement. RecallΨ =−J −1 f Λ.
49

Logit.Diversion satisfies Dj→l = sl/(1−s j), soΛ = I +O(∥s∥). At equilibrium, Example 1
gives diagonal pricing derivatives−1/(1−sj), zero off-diagonal derivatives within each firm, and
Sfsk/[(1−sj)(1−Sf)]across firms. Since Sf =O(∥s∥), it follows thatJf =−I +O(∥s∥). Inversion
around−IyieldsΨ =I+O(∥s∥).
CES.Let Ej =σ− (σ− 1)wj, withσ >1. The normalized pricing equations and diversion ratios
are
fj = pj Ej −(pj−cj) + ∑ l̸=j Ωjl(pl−cl)(σ−1)w l Ej pj pl , D j→l = (σ−1)w l Ej pj pl .
Bounded relative prices implyΛ =I+O(∥w∥). Share derivatives are
∂pkwl = (1−σ)w l pk ( 1{l=k}−w k ) .
Differentiatefj keeping costs fixed. The own derivative ofpj/Ej− (pj−cj)is −(σ− 1)/σ +O(∥w∥)
and its off-diagonal derivatives areO(∥w∥). Each derivative of the ownership sum is alsoO(∥w∥):
every term contains an expenditure share, while(pl−cl)/pl and relative prices are bounded. Thus
Jf =− σ−1 σ I+O(∥w∥).
The diagonal remainder need not beO(wj)alone, because the firm’s other product shares enter it.
Inversion around the nonsingular scalar matrix gives
Ψ = σ σ−1 I+O(∥w∥).
Both inversions are valid for sufficiently small shares, with constants depending on the fixed demand
parameters and the stated bounds.
A.9 Proof of Proposition 3
Lemma 4 givesΨτ =ˆp−1Ψˆc. If a remainder matrixEisO(ϵ), then its scaled entry is
(ˆp−1Eˆc)jk =E jk ck pk pk pj =O(ϵ),
50

by the bounds on cost-to-price and relative-price ratios. Absolute prices and costs need not remain
bounded.
Under logit, Lemma 5 givesΨ =I+O(∥s∥). Therefore, writingµ j = (pj−cj)/pj,
Ψτ logit = diag(cj/pj) +O(∥s∥) = diag(1−µ j) +O(∥s∥).
Under CES the same lemma givesΨ =σ/(σ− 1)I +O(∥w∥). Dividing the equilibrium pricing
equation bypj yields
µj = 1 σ−(σ−1)w j + ∑ l̸=j Ωjlµl (σ−1)w l σ−(σ−1)w j .
Bounded relative margins and fixed dimension implyµj = 1/σ +O(∥w∥), hencecj/pj = (σ− 1)/σ +
O(∥w∥). Combining this with the scaled remainder bound gives
Ψτ CES =I+O(∥w∥).
This is a small-share limit for finite-market CES, not an exact identity at positive shares.
B Proofs for the Model-Specific Small-Share Limits
This appendix verifies the entries in Table 1 and the ownership restrictions needed to interpret them
as pass-through. The ray calculations isolate selection among consumers who continue purchasing;
the boundary calculations retain local cross slopes; the nested-logit calculation retains substitution
within a group. Together they explain why superficially similar small shares can imply different
equilibrium responses. Throughout, recall the identities
−2 +κj jj(p) =−1 + ∂pjηjj(p) ηjj(p)2 ,(40)
and, fork̸=j,
δjk(p)
(
1−κ j kj(p) ) = ∂pjηjk(p) ηjj(p)2 .(41)
Thus, for each model, it suffices to characterize the limiting behavior of the normalized derivatives
of own and cross semi-elasticities.
51

It is useful to distinguish between two kinds of small-share limits. For logit, CES, and mixed logit,
the natural limit is along arayp(n) =λnp, λn→∞ , with fixedp∈R J ++, so relative prices remain
fixed and all inside shares vanish. By contrast, for linear and AIDS demand, the natural small-share
limit is aboundary limitin which productj’s quantity in the linear model, or expenditure share in
the Stone specification, tends to zero while remaining nonnegative; these models are not naturally
analyzed by sending all prices to infinity along a common ray.
B.1 Ray Limits: Logit and CES
The first set of examples considers ray limits of the formp(n) =λnp, λn→∞ , for a fixed vector
p∈R J ++. Along such a sequence, relative prices remain fixed while all prices diverge proportionally.
For logit and CES demand, this implies that inside shares vanish and yields a well-defined small-share
limit.
Proposition 5(Ray limits with fixed relative prices).Fixp ∈R J ++ and letp (n) = λnpwith
λn→∞.
(i)Logit.Suppose
qj(p) =M exp(δj−αpj) 1 +∑J ℓ=1 exp(δℓ−αpℓ), α>0.
Then, for eachj,
−2 +κj jj(p(n))→−1, δ jk(p(n)) ( 1−κ j kj(p(n)) ) →0 (k̸=j).
(ii)CES.Suppose
qj(p) = B pj exp
(
δj−(σ−1) logp j
)
1 +∑J ℓ=1 exp ( δℓ−(σ−1) logp ℓ ), σ >1.
Then, for eachj,
−2 +κj jj(p(n))→−1 + 1 σ, δ jk(p(n)) ( 1−κ j kj(p(n)) ) →0 (k̸=j).
52

Proof.(i) Logit.Let
sj(p) = exp(δj−αpj) 1 +∑J ℓ=1 exp(δℓ−αpℓ), q j(p) =Ms j(p).
Then
ηjj(p) =−α(1−s j(p)), η jk(p) =αs k(p) (k̸=j),
so
∂pjηjj(p) =−α 2sj(p)(1−s j(p)), ∂ pjηjk(p) =α 2sj(p)sk(p).
Hence
∂pjηjj(p)
ηjj(p)2 =− sj(p) 1−s j(p), ∂pjηjk(p) ηjj(p)2 = sj(p)sk(p) (1−s j(p))2.
Alongp (n) = λnpwith λn→∞ , sj(p(n))→ 0for every j, so both expressions converge to0.
Applying (40)–(41) yields the claim.
(ii) CES.Write
xj(p) =e δjp−(σ−1) j , b j(p) = xj(p) 1 +∑J ℓ=1xℓ(p), q j(p) = B pj bj(p).
Then
ηjj(p) =−σ+ (σ−1)b j(p) pj , η jk(p) = σ−1 pk bk(p) (k̸=j).
Moreover,
∂pjbj(p) =−(σ−1) bj(p)(1−b j(p)) pj , ∂ pjbk(p) = (σ−1) bj(p)bk(p) pj (k̸=j),
so a direct calculation gives
∂pjηjj(p)
ηjj(p)2 = σ−(σ−1)b j(p)−(σ−1) 2bj(p)(1−b j(p)) [−σ+ (σ−1)b j(p)]2 ,
and, fork̸=j,
∂pjηjk(p)
ηjj(p)2 = (σ−1) 2 [−σ+ (σ−1)b j(p)]2 pj pk bj(p)bk(p).
53

Alongp (n) = λnp, we havebj(p(n))→ 0for every j, whilep(n) j /p(n) k = pj/pk remains constant.
Therefore
∂pjηjj(p(n))
ηjj(p(n))2 → 1 σ, ∂pjηjk(p(n)) ηjj(p(n))2 →0.
Applying (40)–(41) completes the proof.
Multiproduct ownership along the same rays.Suppose these price vectors are interior
equilibria with markupsm(n) ℓ =O(λ n). For logit,
Dj→ℓ = sℓ 1−s j (ℓ̸=j),
and its price derivatives are bounded by a constant timesDj→ℓ. Since every share decays exponen-
tially along a positive ray,Dj→ℓ→0andm ℓ∂kDj→ℓ→0. For CES,
Dj→ℓ = (σ−1)(p j/pℓ)bℓ σ−(σ−1)b j .
Fixed relative prices andbℓ→ 0imply Dj→ℓ→ 0. Differentiating this expression gives∂kDj→ℓ =
O(bℓ/λn), so its markup-weighted derivatives also vanish. Consequently the limiting unit pass-
through matrices areIfor logit andσ/(σ−1)Ifor CES, for any fixed ownership partition. These
limits do not assert exact diagonal pass-through at finite shares.
B.2 Ray Limits: Mixed Logit
The lower tail of the random price coefficient determines which consumers remain relevant as prices
rise. Lognormal and gamma mixing provide contrasting examples under the same fixed-product,
fixed-utility experiment.
Proposition 6(Ray limits for mixed logit).Fix finite mean utilitiesδj, a fixed finite product set,
andp∈R J ++. Letp (n) =λ np, whereλn→∞, and consider
qj(p) =M
∫ eδj−αpj
1 +∑ ℓeδℓ−αpℓ dF(α).
54

(a) If logα∼N (µ,v ), with v > 0, the demand-side diagonal entries converge to−1and the
off-diagonal entries converge to zero.
(b) Ifα∼Gamma(r,β), with shaper>0and rateβ >0, define
Ψj(z;p) = eδj−zpj
1 +∑ ℓeδℓ−zpℓ , H j(p) =
∫ ∞
0
zr−1Ψj(z;p)dz, ℓ j =−∂ j logHj(p)>0.
Then
−2 +κj jj(λnp)→−1 + ∂jj logHj ℓ2 j , δ jk(1−κ j kj)(λnp)→ ∂jk logHj ℓ2 j (k̸=j).
The limits depend on the ray and generally retain interactions between products. The own
curvature correction has no universal sign.
Proof.Writes j(α,p) =e δj−αpj/(1 +∑ ℓeδℓ−αpℓ).
(a) Lognormal mixing.For nonnegative integers m, letLm(x) = E[αme−xα]. The moment
scales, rather than only the demand-level tail, are needed to compare derivatives. Completing the
square iny= logαgives
Lm(x) = emµ+m2v/2 √ 2πv ∫ R exp [ −xey− (y−µ−mv) 2 2v ] dy.
Let wm =W (vxeµ+mv), whereW (z)eW(z) =z. The exponent is minimized atym =µ +mv−w m,
wherexe ym =w m/v. Expanding about this minimum on the scale √ v/(1 +wm)yields
logLm(x) =mµ+ m2v 2 − w2 m + 2wm 2v − 1 2 log(1 +wm) +o(1).(42)
For completeness, after the changey =ym +u
√
v/(1 +wm), the quadratic term isu2/2and the
cubic remainder on each boundedu-interval isO(w−1/2 m ). Convexity of the exponent bounds the two
tails outside an expanding neighborhood of the minimum. The rescaled integral therefore converges
to
√
2π, giving (42).
55

For clarity, the exponent’s exact increase about its minimum, writingw =wm and h =y−y m,
is
D(h) = w v (eh−1−h) + h2 2v.
Set h =au, witha =
√
v/(1 +w). ThenD(au)→u 2/2uniformly on bounded intervals. Convexity
and the limiting derivatives atu = 1and u =−1give uniform exponential tail bounds. These
bounds remain integrable after multiplication byekau for fixedk = 1, 2and sufficiently large w,
justifying convergence of the first two tilted moments as well as the integral itself.
The same concentration aboutym, including its first two exponential moments, implies
Lm(cx)
Lm(x) =x−log(c)/v+o(1)→0 (c>1), Lm+1(x) Lm(x) ∼ wm vx =O(logx/x), L0(x)L2(x) L1(x)2 →1.
(43)
In the first expression the decay is a fixed power, up to a subpower factor; no faster-than-every-power
bound is used.
Set x =λnpj. Expanding1/(1 +∑ ℓeδℓ−αλnpℓ)about one bounds the demand error by a finite
sum ofL0(λn(pj +pℓ)). Differentiating once or twice gives the same bounds withL1 or L2. The
first limit in (43) therefore gives
qj∼Me δjL0(x),−∂ jqj∼Me δjL1(x), ∂ jjqj∼Me δjL2(x).
Thusκ j jj→1.
Fork̸=j, setc= (p j +pk)/pj >1. Product-share bounds inside the integrals give
|∂kqj|≤CL 1(cx),|∂ jkqj|≤CL 2(cx).
The quotient rule andη2 jj∼[L 1(x)/L0(x)]2 then bound the normalized cross derivative by
C
{L2(cx)L0(x)
L1(x)2 + L1(cx) L1(x) } −→0,
using (43). Lemma 3 proves part (a).
56

(b) Gamma mixing.LetC r =Mβ r/Γ(r). The substitutionz=λ nαgives
qj(λnp) =C rλ−r n
∫ ∞
0
zr−1e−βz/λ nΨj(z;p)dz.
The kernel and its first two price derivatives are bounded in a neighborhood of the fixed positive
ray by constants times(1 +z2)e−az, for somea> 0. Dominated convergence therefore applies to
the demand and derivative integrals. Remembering that derivatives with respect to the actual price
vector introduce one factorλ−1 n each, we obtain
qj(λnp)∼C rλ−r n Hj(p),
∂kqj(λnp) =C rλ−r−1 n ∂kHj +o(λ−r−1 n ), ∂ jkqj(λnp) =C rλ−r−2 n ∂jkHj +o(λ−r−2 n ).
Consequentlyη jj =−λ−1 n ℓj +o(λ−1 n )and
∂jηjk(λnp) =λ−2 n ∂jk logHj +o(λ−2 n ).
Here ℓj > 0follows by differentiating the strictly decreasing own-price kernel under the integral.
Substitution in the semi-elasticity identities proves part (b).
What common-ray regular variation does and does not imply.For gamma mixing, the
selected consumers haveα of order1/λn, so their conditional probabilities of rival products need
not vanish. This accounts for the dependence onHj(p). Equivalently,
Hj(p) =e δjΓ(r)p−r j Cj(p), C j(p) = 1 Γ(r) ∫ ∞ 0 ur−1e−u 1 +∑ ℓeδℓ−(pℓ/pj)udu.
With no rival inside goods,Cj is constant and the own correction is1/r. With rivals, derivatives of
Cj can overturn the sign of this correction. For instance, in the symmetric two-product example in
the main text, differentiating the one-dimensional integral gives∂jj logHj/ℓ2 j≃−0.188.
57

The same dominated-convergence argument, uniformly on compact positive-price neighborhoods,
gives the normalized own-price profile
Qj(t) = Hj(p+te j/ℓj) Hj(p) , t>−ℓ jpj.
This profile changes relative prices, whereas the common-ray experiment holds them fixed. It need
not have constant curvature. These are demand-derivative results for everyr >0; equilibrium
incidence additionally requires an admissible interior equilibrium and a nonsingular limiting pricing
Jacobian. For example, the one-product limit has a zero pricing-Jacobian limit atr = 1, so a finite
inverse limit cannot be inferred there.
Lognormal diversion and ownership terms.Suppose, in addition, that the ray is a sequence
of interior equilibria and markups areO(λn). Letx =λnpj, c = (pj +pℓ)/pj > 1, andℓ̸ =j. The
preceding moment bounds imply
Dj→ℓ =O
(L1(cx)
L1(x)
)
→0.
The quotient rule, applied directly to−∂jqℓ/∂jqj, gives for everyk
|∂kDj→ℓ|≤C
{L2(cx)
L1(x) + L1(cx)L2(x) L1(x)2
}
.
SinceL 2(x)/L1(x) =O(logx/x), it follows that
λn|∂kDj→ℓ|≤O(logλ n)L1(cx) L1(x) −→0.
Thus every markup-weighted diversion derivative vanishes. For a fixed ownership partition,C→ 0
andΛ →I ; combined with part (a), this givesP→I . The result establishes a limit, not a
finite-share accuracy ranking between diagonal approximations. Convergence is pointwise in the
fixed ray and mixing parameters and can be slow: the decay rate in(43) depends on relative prices
and mixing dispersion. The identity limit therefore need not be an accurate approximation at
empirically relevant shares.
58

B.3 Boundary Limits: Linear and AIDS
The remaining examples are most naturally analyzed along feasible boundary sequences: quantity
demand tends to zero in the linear model, while expenditure share tends to zero in the Stone
specification. A vanishing expenditure share also implies vanishing quantity if absolute prices have
finite positive limits. The proposition states the weaker conditions sufficient for the normalized-
derivative limits.
Proposition 7(Boundary limits for linear and AIDS demand).Fix productj.
(i)Linear demand.Suppose
qj(p) =γ j−
J∑
ℓ=1
βjℓpℓ, β jj >0.
Let{p (n)}n≥1 be any sequence in the domain{qj >0}such thatq j(p(n))↓0.Then
−2 +κj jj(p(n))→−2, δ jk(p(n)) ( 1−κ j kj(p(n)) ) →− βjk βjj (k̸=j).
In fact, these expressions are constant on{qj > 0}, so the limits do not depend on the particular
boundary sequence.
(ii)LA/AIDS with Stone index.Suppose
qj(p) = B pj wj(p), w j(p) =α j + J∑ ℓ=1 γjℓ logpℓ +βj log ( B PS(p) ) ,
where the Stone price index is
logP S(p) =
J∑
ℓ=1
ωℓ logpℓ,
J∑
ℓ=1
ωℓ = 1,
with fixed weightsωℓ. Let{p (n)}n≥1 be a sequence such that
wj(p(n))↓0, p(n) j
p(n) k →cjk∈(0,∞) (k̸=j),
59

and assume
γjj−βjωj <0.
Then
−2 +κj jj(p(n))→−2,
and, for eachk̸=j,
δjk(p(n)) ( 1−κ j kj(p(n)) ) →−cjk γjk−βjωk γjj−βjωj .
Proof.(i) Linear demand.Since qj(p) =γj−∑J ℓ=1βjℓpℓ, we haveηjj(p) =− βjj qj(p), andηjk(p) =
− βjk qj(p) for k̸ =j. Differentiating with respect topj, ∂pjηjj(p) =− β2 jj qj(p)2 and ∂pjηjk(p) =−βjkβjj qj(p)2.
Therefore
∂pjηjj (p)
ηjj (p)2 =−1and
∂pjηjk(p)
ηjj (p)2 =−βjk βjj . Applying (40)–(41) gives−2 +κj jj(p) =−2and
δjk(p)
(
1−κj kj(p) ) =−βjk βjj , for everypwith qj(p)> 0. In particular, the same limits hold along
any sequence withqj(p(n))↓0.
(ii) LA/AIDS with Stone index.DefineAjk :=γjk−βjωk. Since qj(p) = B pj wj(p), we have
logqj(p) = logB−logp j + logwj(p),and therefore
ηjk(p) =− 1{j=k} pj + 1 wj(p)∂pkwj(p).
BecauselogP S(p) =∑J ℓ=1ωℓ logpℓ,it follows that∂ pkwj(p) = Ajk pk .Therefore
ηjj(p) = Ajj−wj(p) pjwj(p) , η jk(p) = Ajk pkwj(p) (k̸=j).
Along the stated sequence,wj(p(n))→0, so
ηjj(p(n))∼ Ajj
p(n) j wj(p(n)) , η jk(p(n)) = Ajk p(n) k wj(p(n)) .
Since∂ pjwj(p) =A jj/pj, we obtain
∂pjηjj(p) = wj(p)2−Ajjwj(p)−A 2 jj p2 jwj(p)2 ,
60

and hence
∂pjηjj(p)
ηjj(p)2 = wj(p)2−Ajjwj(p)−A 2 jj (Ajj−wj(p))2 →−1.
Applying (40) yields
−2 +κj jj(p(n))→−2.
Fork̸=j,
∂pjηjk(p) =− AjkAjj pkpjwj(p)2,
so
∂pjηjk(p)
ηjj(p)2 =− pj pk AjkAjj (Ajj−wj(p))2.
Along the sequence,wj(p(n))→0andp (n) j /p(n) k →cjk, so
∂pjηjk(p(n))
ηjj(p(n))2 →−cjk
Ajk
Ajj
=−cjk
γjk−βjωk
γjj−βjωj
.
Applying (41) yields
δjk(p(n)) ( 1−κ j kj(p(n)) ) →−cjk γjk−βjωk γjj−βjωj .
This proves the claim.
Scope and interpretation.These are rowwise statements about productj, conditional on a
feasible sequence. They neither assert that all product demands can vanish simultaneously nor
establish a nonsingular full pricing Jacobian. In the Stone specification, the weights are held fixed.
If a finite-price boundary interpretation is desired, additionally requirep(n) k →¯pk∈ (0,∞ ); then
quantityq j also vanishes and the semi-elasticity divergence rates stated below apply.
Linear demand is the simplest boundary case. As productj’s demand approaches zero, the
own semi-elasticity and cross semi-elasticities with nonzeroβjk diverge at rateq−1 j , and their
own-price derivatives diverge at rateq−2 j . A zero cross coefficient gives identically zero cross terms.
After normalization, however, these divergences cancel exactly. The diagonal term converges to
−2, while the off-diagonal term converges to−βjk/βjj. Thus the small-share limit preserves the
relative cross-slope structure of the linear demand system. In this sense, linear demand can remain
non-diagonal even near the boundary: substitution patterns continue to matter at first order.
61

Under finite positive limiting prices, LA/AIDS exhibits a similar boundary logic, but with richer
dependence on the sequence by which productj’s expenditure share vanishes. Aswj(p(n))↓ 0, the
own semi-elasticity and cross semi-elasticities with nonzeroAjk diverge likew−1 j , and their own-price
derivatives diverge likew−2 j . Cross terms withAjk = 0are identically zero. The normalized diagonal
term therefore converges to the same boundary benchmark−2. The off-diagonal term, however,
depends not only on the demand primitivesγjk and βj, but also on the limiting relative price ratio
cjk and the Stone-index weightsωk. The term γjk−β jωk is the relevant log-price derivative of
wj with respect topk, so the limit preserves the first-order substitution structure encoded by the
LA/AIDS system rather than washing it out.
Taken together, these two examples show that boundary-type demand systems behave very
differently from logit-type ray limits. In logit and CES, off-diagonal interaction terms vanish
asymptotically, so the limiting Jacobian becomes diagonal. In linear and LA/AIDS demand, by
contrast, nonzero cross slopes generate normalized off-diagonal terms that survive. Small shares
therefore do not imply asymptotic independence across products: in boundary models, substitution
patterns continue to shape pass-through even as productj’s quantity demand or expenditure share
becomes arbitrarily small.
B.4 Nested Logit with Multiproduct Ownership
Letproductsbelongtoafixedfinitecollectionofnests. Underthestandardnested-logitnormalization,
define
vj = exp
(δj−αpj
1−σ
)
, V g =
∑
j∈Jg
vj, z j = vj Vg(j) , s g = V 1−σ g 1 +∑ hV 1−σ h , q j =Ms g(j)zj,
where α> 0and0 ≤σ < 1are fixed. The outside alternative has normalized attractiveness one.
This specification makes the price scale explicit:−qj/∂jqj contains the factor(1−σ)/α.
Proposition 8(Nested-logit benchmark).Fix an ownership partition and consider a sequence of
interior equilibria for the demand system above, allowing costs to vary. Supposesg→ 0for every
62

nest andzj→¯zj∈[0,1]for every product. Write
B∗ j = 1−σ¯zj, S fg = ∑
ℓ∈Jf∩Jg
¯zℓ.
Then:
(i) The demand-side matrix−2I+Khas the block-diagonal limit
Jd,∗ jk =



−1− σ¯zj(1−¯zj) (B∗ j )2 , k=j,
σ¯zj ¯zk
(B∗ j )2, k̸=j, g(k) =g(j),
0, g(k)̸=g(j).
Diversion converges to
D∗ j→k =



−1, k=j,
σ¯zk/B∗ j, k̸=j, g(k) =g(j),
0, g(k)̸=g(j),
Λ∗ =−Ω◦D ∗.
(ii) Products in firm–nest group(f,g)have the common limiting markup
m∗ fg = 1−σ α(1−σS fg ).(44)
In particular, limiting markups lie between(1−σ)/αand1/α.
(iii) Define the matrixL∗ by
L∗ jk =



−σ¯zk
(
1{k∈J f(j)}−S f(j),g(j)
)
(1−σS f(j),g(j) )2 , g(k) =g(j),
0, g(k)̸=g(j).
(45)
ThenI−L ∗ is nonsingular and equilibrium unit pass-through satisfies
P−→P ∗ := (I−L ∗)−1.(46)
63

The limit is block diagonal by nest, and each block satisfiesP∗ g 1=1. If a firm owns the entire
nest,P ∗ g =I.
Proof.SetB j = 1−σz j−(1−σ)s j. Direct differentiation gives
ηjj =− αBj 1−σ , ∂ kzℓ =− α 1−σ zℓ(1{ℓ=k}−z k) (g(k) =g(ℓ)),
with ∂kzℓ = 0across nests. Own and cross derivatives ofη, combined with Lemma 3, give part (i).
For example,
∂jηjj
η2 jj =− σzj(1−z j) B2 j − (1−σ)s j Bj ,
and the second term vanishes. The exact off-diagonal diversion ratios are
Dj→k =



σzk + (1−σ)s k
Bj
, g(k) =g(j),
(1−σ)s k
Bj
, g(k)̸=g(j),
k̸=j.
These converge to the displayed values becauseBj→B∗ j≥1−σ >0.
The normalized first-order conditions areΛm=b, where
bj =− qj ∂jqj = 1−σ αBj −→ 1−σ αB∗ j .
Every row ofΛ∗ is strictly diagonally dominant: its off-diagonal absolute row sum is at most
σ(1−¯zj)
1−σ¯zj
<1.
HenceΛ∗ is nonsingular, andm→(Λ ∗)−1b∗. Multiplying limiting rowjbyB ∗ j gives
m∗ j−σ ∑
ℓ∈Jf(j)∩Jg(j)
¯zℓm∗ ℓ = 1−σ α .
All products in a firm–nest group therefore have the same markup. Solving the resulting scalar
equation proves (44).
64

For pass-through, write the demand-implied markup field as m(p) = Λ(p) −1b(p). In the
neighborhood of the sequence, the normalized pricing equations are
f= Λ(p){m(p)−(p−c−t)}.
At equilibrium, differentiating givesJf = Λ(∂m/∂ p⊤−I ). Entries ofΛ, b, and their first derivatives
are rational functions of s and z, with denominators bounded away from zero. In addition,
∂ksj =O(sj). Thus the derivative limit follows by differentiating the limiting markup field, not by
an unsupported interchange of a limit and a derivative. Within group(f,g),
∂kSfg =− α 1−σ zk(1{k∈J f}−S fg ) (k∈J g),
which, substituted into (44), yields∂m/∂p⊤→L∗.
It remains to verify nonsingularity. If(I−L ∗ g)v = 0, the identical rows ofL∗ g within a firm–nest
group imply thatvj =uf within that group. For groups with positiveSf =Sfg, these common
values satisfy
(1 +Af)uf−Af
∑
h
Shuh = 0, A f := σSf (1−σS f)2≥0.
The group matrixdiag(1 +A)−AS⊤ is strictly diagonally dominant, with dominance margin one.
Hence alluf = 0. For a zero-share group, the corresponding rows ofL∗ g are zero, so its coordinates
also vanish. ThusI−L ∗ is nonsingular. Continuity of inversion now proves (46).
Finally,L∗ g1= 0because ∑ k∈Jg ¯zk = 1and ∑ k∈Jf∩Jg ¯zk =Sfg. ThereforeP∗ g 1=1. If a single
firm owns the nest,Sfg = 1and every entry ofL∗ g is zero, givingP∗ g =I.
The normalization in(44) matters economically. For example, two equally popular products in
one nest withσ = 1/2, α = 1, and a common owner have limiting markup one and identity pass-
through. Cross-nest effects vanish even when ownership spans nests, because cross-nest diversion
and its derivatives vanish while limiting markups remain bounded. Within a nest, split ownership
can sustain product-specific spillovers.
Normalized residual demand.The same model also separates baseline curvature from a full
normalized profile. Fix j, letz = ¯zj, B = 1−σz , and displace only its price byt/[−ηjj(p(n))].
65

The ratio of the new to the oldvj tends to e−t/B, while the ratio of the nest sums tends to
T (t) = 1−z +ze−t/B. Since the outside alternative dominates aggregate nest shares, the resulting
demand ratio is
Qj(t) =e−t/BT(t)−σ.
This holds uniformly on boundedt-intervals and is positive for every finitet. Its conditional share
isz(t) =ze −t/B/T(t), and its normalized curvature is
Aj(t) =− σz(t)[1−z(t)] [1−σz(t)] 2 .
Except in degenerate cases, this function changes witht. Consequently the negative baseline value
Aj(0)does not satisfy the constant-profile hypothesis of Proposition 4, and it does not imply a
finite normalized choke point.
B.5 Proof of Corollary 1
Fix a nest and suppress its index. Letx = P∗ gh, X = ∑ j∈Jgzjxj, and, forSf > 0, let xf =
S−1 f ∑ j∈Jf∩Jgzjxj. Define Af = σSf/(1−σS f)2, soχf = (1 +Af)−1. All group averages and
group sums below concern groups withSf >0. The matrixL ∗ in Proposition 8 gives
xj =h j +Af(X− xf).
Averaging within groupfyields
xf =χ fhf + (1−χ f)X.
Averaging again across the nest and using∑ fSf = 1gives DgX = ∑ fSfχfhf. Since χf > 0,
Dg > 0and X = Hg. Substituting back proves (29). If Sf = 0, the corresponding row ofL∗
vanishes, givingxj =h j without defining a group average.
Forjin a positive-share groupf, the matrix entries are
(P∗ g )jk =1{j=k}+ (1−χ f)zk
(
χf(k)
Dg
− 1{f(k) =f} Sf
)
.
66

Across firms this expression is nonnegative. Within a firm,Dg≥S fχf, so off-diagonal entries are
nonpositive. On the diagonal,
1≥(P ∗ g )jj≥1−(1−χ f)zj Sf ≥χ f >0.
These inequalities also cover zero-share individual products in a positive-share group. Zero-share
groups have identity rows, completing the proof.
C Numerical Illustrations
Each exercise addresses a distinct use of the theory: how many interaction terms a local prediction
needs, how far that derivative extrapolates to a finite cost change, which within-nest responses
survive small shares, and how percentage incidence differs from unit incidence. The exercises use
simulated demand and cost primitives throughout. Their purpose is to check these mechanisms in
transparent benchmarks, rather than estimate an empirical policy effect.
C.1 Logit Approximation and Finite Cost Changes
There are six products and two firms, each owning three products. Ownership is fixed, while
product characteristics and costs differ. Demand is multinomial logit with outside utility zero and
common price coefficientα = 1. In each of 100 baseline markets, I drawδ(0) j ∼N (1.2, 0.42)and
cj∼U [0.2, 0.8]independently across products. A common utility shift takes ten equally spaced
values from0to −6, yielding 1,000 configurations. This fixed-dimensional experiment reduces inside
shares by making the outside option more attractive relative to all inside goods.
The equilibrium solver uses the common markup within each firm:mf(1−Sf) = 1/α, whereSf
is the firm’s total quantity share. Every accepted solution also satisfies the original product pricing
conditions, normalized by own-price demand slopes, with maximum absolute residual below10−10.
Pass-through is computed analytically and checked independently against differentiated pricing
conditions and re-solved equilibria after small product-specific cost perturbations.
67

Writing the normalized pricing Jacobian asJf =A +B, with diagonalA, defineΓ =−BA−1.
The Neumann approximations are
ˆΨK =−A−1
K∑
k=0
ΓkΛ, K∈{0,1,2}.
Table 2 compares these with the exact local derivative and the identity approximation. The order-1
mean matrix error is0.323%, with a maximum of3.139%. These results describe this logit calibration,
whose substitution structure is particularly tractable.
Table 2: Accuracy of local pass-through matrix approximations
Approximation Mean error (%) Maximum error (%)
NeumannK= 02.285 12.375
NeumannK= 10.323 3.139
NeumannK= 20.057 0.847
Identity 8.905 28.247
Figure 1 plots relative Frobenius errors against the feedback norm. Higher-order truncations
reduce errors in this exercise; this does not establish a universal ordering of errors across different
demand systems.
68

0
4
8
12
0.0 0.1 0.2 0.3
Feedback norm
Relative Frobenius error (%)
Neumann K = 0 Neumann K = 1 Neumann K = 2
Figure 1: Neumann approximation errors across logit configurations
Notes:Each point represents one configuration and truncation order. The vertical axis is100∥ˆΨK− Ψ∥F/∥Ψ∥F;
the horizontal axis is∥Γ∥∞. No fitted curve is imposed. The reproduction separately checks the convergence
norm and the absolute-error remainder bound.
Figure 2 considers per-unit cost changes of0.1on all products, firm 1’s products, or product 1.
It compares averages of the local predictionsΨdt, ˆΨ1dt, anddt. The identity tends to overstate
average responses as shares rise in this design. Agreement in averages need not imply accuracy for
individual products; full response-vector errors are also reported in the reproduction output.
69

(a) All products (b) Firm 1 products (c) Product 1
0% 5% 10% 0% 5% 10% 0% 5% 10%
0.014
0.015
0.016
0.042
0.046
0.050
0.08
0.09
0.10
Average product share
Average local price response
Exact derivative Neumann K = 1 Identity
Figure 2: Average local price responses under three cost directions
Notes:Prices are averaged over all six products. Configurations are placed in 20 equal-count bins by average
product share, using the same bins for every method and scenario. Lines connect within-bin means. OnlyK = 1
enters the Neumann curve; the exact derivative is counted once per configuration and scenario. All curves are
local predictions, not re-solved finite-tax equilibria.
A separate exercise re-solves equilibrium after per-unit taxes of0.01,0 .1, and0.25on affected
products. Figure 3 measures the relative Euclidean error ofΨdtagainst the actual finite equilibrium
price change. At tax0 .1, mean errors across scenarios range from0 .179%to0 .444%. This
linearization error is distinct from the error due to approximating the matrixΨ.
70

(a) All products (b) Firm 1 products (c) Product 1
0.01 0.1 0.25 0.01 0.1 0.25 0.01 0.1 0.25
0
1
2
3
Per-unit tax on affected products
Finite-change prediction error (%)
Figure 3: Local derivative predictions versus finite-tax equilibria
Notes:Each box summarizes 1,000 configurations. Boxes indicate medians and interquartile ranges; whiskers
extend to observations within 1.5 interquartile ranges. The denominator is the Euclidean norm of the actual
price change. All 9,000 post-tax equilibria satisfy normalized pricing conditions to within10−10.
C.2 The Nested-Logit Benchmark
There are two nests of three products,α = 1, σ = 0.6, baseline utilities(1.1, 0.6, 0.9, 1.3, 0.8, 0.4),
and costs(0.4, 0.6, 0.3, 0.5, 0.4, 0.7). A common utility shift varies from0to −12in unit steps.
Three ownership structures are compared: single-product firms; portfolios with ownership vector
(1,1,2,1,2,2); and one owner per complete nest.
For this nested-logit specification, the sufficiency result of Garrido (2024) implies that a finite
solution of the pricing first-order conditions is a Nash equilibrium. The numerical checks assess
residuals and local derivatives without assuming equilibrium uniqueness.
As both nest shares vanish, letzk be productk’s limiting conditional share andSfg firm f’s
conditional share in nestg. The limiting common markup within a firm–nest group is
m∗ fg = 1−σ α(1−σS fg ).
I solve these equations jointly with conditional demand. IfL∗ is the derivative of the limiting markup
function with respect to product prices, evaluated at equilibrium, then the limiting pass-through is
71

(I−L ∗)−1, where
L∗ jk =− σzk[1{f(j) =f(k)}−S f(j),g(j) ] (1−σS f(j),g(j) )2
when j and k are in the same nest, and zero otherwise. The pass-through matrix(I−L ∗)−1 has
row sums equal to one. Whole-nest ownership yieldsL∗ = 0and identity limiting pass-through.
Figure 4 shows convergence to this block limit. With single-product firms or portfolios spanning
nests, the identity retains nonzero error as unconditional shares vanish. When one firm owns each
entire nest, the identity and block limit coincide. These conclusions concern the stated limiting
experiment.
(a) Single-product
firms
(b) Portfolios across
nests
(c) One owner
per nest
1e-4 1e-2 1e-4 1e-2 1e-4 1e-2
0
10
20
30
40
Average product share (log scale)
Relative matrix error (%)
Block limit Identity
Figure 4: Nested-logit limits under alternative ownership structures
Notes:Relative Frobenius errors compare the finite-market local derivative with the block limit or identity.
There are 13 configurations per ownership structure. The horizontal axis is logarithmic. Finite-market solutions
satisfy normalized pricing conditions and firm-level second-order conditions. Both curves coincide in the last
panel.
C.3 Finite-Market CES Percentage Pass-Through
For one inside product and a fixed outside alternative, consider
q(p) = Bap−σ
1 +ap 1−σ, w= ap1−σ 1 +ap 1−σ, σ >1.
72

The residual elasticity magnitude isE =σ− (σ− 1)w. The monopoly conditionp−c =p/E implies
dlogp
dlogc = E σ = 1− σ−1 σ w.
Percentage pass-through is below one at positive finite shares and approaches one asw→ 0. For
example, σ = 2and w = 1/2give3 /4. Exact unity instead holds for exogenous isoelastic residual
demand with a fixed multiplicative demand shifter.
0.2
0.4
0.6
0.8
1.0
0% 25% 50% 75%
Inside expenditure share
Percentage pass-through
σ = 2σ = 4σ = 8
Figure 5: Exact percentage pass-through with finite-market CES demand
Notes:Curves show1 − [(σ− 1)/σ]w for σ = 2, 4, 8. Each point is calibrated top = 1using a =w/(1−w )
and c = 1− 1/E. Re-solving after positive and negative log-cost perturbations verifies the derivative at 183
configurations. The dotted line is the small-share limit of one.
D Bounds on the Directional Stability Ratio
This appendix supports the interpretation of portfolio curvature in Section 3. It identifies a markup
direction that reproduces the scalar benchmark and shows how substitution or complementarity
orders the threshold in other directions. These bounds concern an individual firm’s second-order
condition; equilibrium feedback is governed separately by (18).
73

The key object is the directional stability ratioRf(v). Letmf =pf−cf and Gf =∂qf(p)/∂p⊤ f .
Evaluate these objects at an interior stationary point satisfyingqf +G⊤ fmf = 0. Suppose that
qj >0andm j >0for allj∈J f, and thatGf is symmetric and negative definite. Define
Df := diag
(
mj
qj
)
j∈Jf
, H f :=−D 1/2 f GfD1/2 f .
ThenH f is symmetric and positive definite.
Proposition 9(Bounds onR f(v)).Under the conditions above, for every nonzero directionv,
Rf(v) = z⊤Hfz z⊤H2 fz, z:=D −1/2 f v,
and hence
1
λmax(Hf)≤R f(v)≤ 1 λmin(Hf).
Moreover,1is an eigenvalue of Hf and Rf(mf) = 1. If the firm’s products are substitutes, so that
∂qj/∂pk≥0for allj̸=k, thenλ min(Hf) = 1and
1
λmax(Hf)≤R f(v)≤1.
If instead the firm’s products are complements, so that∂qj/∂pk≤ 0for all j̸ =k, thenλmax(Hf) = 1
and
1≤R f(v)≤ 1 λmin(Hf).
Proof.Under symmetry,
Sf(v) =−v⊤Gfv, M f(v) =v⊤GfDfGfv.
Writingv =D1/2 f z therefore givesSf(v) = z⊤Hfz and Mf(v) = z⊤H2 fz, which yields the stated
representation ofRf(v). Expandingzin an orthonormal eigenbasis ofH f gives
Rf(v) =
∑
rλrz2 r∑
rλ2rz2r .
74

This is a weighted average of1/λr, with weights proportional toλ2 rz2 r, and therefore lies between
1/λmax(Hf)and1/λ min(Hf).
At an interior stationary point, symmetry impliesqf +Gfmf = 0. Since mf =Dfqf, letting
y=D 1/2 f qf =D−1/2 f mf gives
Hfy=−D 1/2 f Gfmf =D 1/2 f qf =y.
Thus1is an eigenvalue of Hf, with strictly positive eigenvectory, and taking v = mf gives
Rf(mf) = 1.
Ifproductsaresubstitutes, theoff-diagonalelementsof Hf arenonpositive. Choose a>λ max(Hf).
Then K =aI−H f is entrywise nonnegative and satisfiesKy = (a− 1)y. By Perron–Frobenius,
ρ(K) =a− 1. Since the eigenvalues ofK are a−λ r(Hf), it follows thatλmin(Hf) = 1. The stated
bound follows.
If products are complements,Hf is entrywise nonnegative andHfy =y with y≫ 0. Perron–
Frobenius therefore impliesρ(Hf) = 1. SinceHf is symmetric and positive definite,λmax(Hf) = 1,
which gives the final bound.
Proposition 9 identifiesRf = 1as a natural multiproduct analogue of the single-product bench-
mark. Under symmetric demand effects, substitution weakly lowers the directional threshold in the
second-order condition,κf(v)≤ 2Rf(v), relative to the monopoly bound2, whereas complementarity
weakly raises it.
75
