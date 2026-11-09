---
title: Linear Demand Systems are Consistent with Discrete Choice
url: https://arxiv.org/abs/2610.13785
category: consumer-behavior
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Afonso Rodrigues
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.13785
pages: 44
chars: 102713
fetched_at: '2026-11-08T13:17:11+00:00'
kb_version: 1
---

# Linear Demand Systems are Consistent with Discrete Choice

Linear Demand Systems are Consistent with Discrete
Choice
Afonso Rodrigues ∗
October 12, 2026
Abstract
Aggregate linear demand systems can be micro-founded by a population of heterogeneous con-
sumers making discrete choices. They can also be extended to incorporate income effects, enabling
the study of subsets of goods within a wider unspecified assortment. I show how we can structurally
estimate this class of models using only market-level data. The distribution of consumer preferences
is recovered by disciplining the corner solutions with aggregate terms only. This approach allows
for the same richness of Berry, Levinsohn, and Pakes (1995) [BLP] while retaining the analytical
and computational advantages of linear demand: it does not require exogenously fixing market size,
allows for heterogeneity in choice sets, and results in a flexible substitution matrix which varies as
consumer types enter and exit the market. The discrete-choice microfoundation facilitates welfare
analysis and the flexible measurement of markups and cost pass-throughs, among a wide range of
other applications.
JEL: C35, D43, L10
Keywords: linear demand, discrete choice, aggregation, corner solutions, structural estimation,
income effects
∗Düsseldorf Institute for Competition Economics, Heinrich-Heine-Universität Düsseldorf (af-
boro@dice.hhu.de). A portion of this work was carried out during the author’s doctoral studies at the
University of Oxford. There are no relevant or material financial interests that relate to the research de-
scribed in this paper.
1
arXiv:2610.13785v1  [econ.GN]  9 Oct 2026

1 Introduction
The main contribution of this paper is to investigate the conditions under which an ag-
gregate linear demand system for differentiated goods can be derived from a population
of heterogeneous consumers making discrete choices.1 More broadly, the paper shows that
the tractability of linear demand need not come at the expense of heterogeneous consumer
preferences, flexible substitution patterns, or economically meaningful welfare and policy
counterfactuals.
Producing a discrete-choice microfoundation for linear demand is not in of itself novel.
Hotelling (1929), Salop (1979), Chen and Riordan (2007), and Bos and Vermeulen (2022)
provide settings in which discrete consumer choice generates linear or piecewise-linear de-
mand: consumers have a one-dimensional distribution of valuation differences and can only
choose between pairs of alternatives, occasionally including the outside good. These are
remarkably restrictive kinds of consumer heterogeneity which impose tight conditions, par-
ticularly on cross-price effects. The literature suggests this may be unavoidable: Jaffe and
Weyl (2010) show that linear demand cannot arise from discrete choice if we assume con-
sumer valuations have a smooth, full-dimensional density across products; Armstrong and
Vickers (2015) furthermore confirm linear demand requires some restriction on the support
of consumer valuations.
As a result, these models have remained primarily a tool for theoretical research. In
empirical work, aggregate linear demand is more often represented via a representative con-
sumer with quasilinear quadratic utility (Amir, Erickson, and Jin, 2017; Choné and Lin-
nemer, 2020). Examples include Melitz and Ottaviano (2008) in international trade; and
Pinkse, Slade, and Brett (2002), Thomassen, Smith, Seiler, and Schiraldi (2017), and Pelle-
grino (2025) in industrial organisation. However, while allowing full flexibility in cross-price
effects, the model cannot incorporate income effects, produces inflexible cost pass-throughs,
and assumes homogeneity in consumer preferences, making it impractical for policy assess-
ments and analyses.
The main novelty of this paper is therefore primarilygeneralisability; to produce a
discrete-choice microfoundation that can yield a fully flexible demand system which may
be structurally estimated without a representative consumer assumption. I show this can be
achieved by choice of a suitable distribution for the idiosyncrasies in tastes across individual
consumers: aggregate linear demand arises when consumers are uniformly distributed over
how much weight they place on a personal (cardinal) ranking of the products relative to their
characteristics. Once aggregated, heterogeneity in the one-dimensional orderings allows rich
substitution patterns mimicking full-dimensional valuations.
Income effects appear if the marginal utility of income across consumers is locally con-
stant and differs in slope at the relevant pre- and post-purchase consumption levels. I show
1McFadden (1974), Daly and Zachary (1978), McFadden and Train (2000), and Anderson, de Palma, and
Thisse (1989) do so for the multinomial, nested, and mixed logit, and Constant Elasticity of Substitution
(CES) utility respectively.
2

these can then be modelled as an intercept in the matrix of product characteristics inside the
aggregate demand function. Incorporating income effects allows the linear demand system to
operate as an incomplete demand system (LaFrance, 1985) while remaining fully consistent
with utility maximization theory. This holds nice properties in settings where researchers
wish to analyse competition amongst a subset of an entire assortment of available alterna-
tives.
Consumer heterogeneity follows from the discrete choice microfoundation, but implies
heterogeneous corner solutions. Discussions of corner solutions in aggregate linear demand
are often neglected in favour of assuming an interior Nash equilibrium (Choné and Linnemer,
2020), removing any role for consumer heterogeneity. Different individual consumers reach-
ing their corner solution - e.g. as price increases - produce kinks at different points in the
aggregate demand function; without corners, there are no kinks, and the aggregate parame-
ters are at best a (weighted) mean of individual parameters.
To address this, I introduce a novel tool to model corner solutions directly, which allows
aggregate linear demand estimation to recover the full distribution of consumer preferences.
It relies on the set of possibleordinalorderings, or permutations, of the set of goods. I
demonstrate how the full model can be disciplined using only aggregate terms by sketch-
ing out a methodology for the structural estimation of the aggregate demand system using
market-level data exclusively. The methodology follows a step-by-step process: (1) estimate
an initial unconstrained linear demand system using excluded instruments; (2) decompose
the unconstrained demand Jacobian into simulated one-dimensional permutations, whose av-
erage reproduces the estimated unconstrained system exactly; (3) introduce a distribution of
heterogeneity in characteristic preferences; and (4) solve the implied corner problem for each
simulated permutation, aggregate the resulting corner corrections, and jointly re-estimate
the constrained demand and heterogeneity parameters by simulated GMM.
The model shows potential for a wide range of applications, including where linear de-
mand has previously not seen significant use. One common concern is the analysis of con-
sumer welfare, particularly due to the possibility that counterfactual welfare changes depend
on the path taken through the price vector. I show how the discrete-choice microfoundation
enables welfare analysis by providing a corresponding expected-surplus representation. A
second common concern is that linear demand implies constant cost pass-through: condi-
tional on product characteristics and firm ownership, equilibrium pass-through is usually
invariant to the level of prices and marginal costs. Corner solutions relax this restriction
by introducing endogenous demand curvature. As prices change, different consumer seg-
ments reach product-level zero-demand constraints, changing the active demand Jacobian
and therefore the degree of cost pass-through. This allows pass-throughs to depend on price
and marginal cost, and rise beyond a half or even above one. The model’s properties are also
valuable in settings where demand and equilibrium prices must be evaluated repeatedly, such
as models of endogenous entry and exit and durable-goods competition. They can facilitate
the analysis of large choice sets in retail markets, network-based substitution structures, and
endogenous participation in platform markets.
3

2 Main result
LetN= 0,1, . . . , Nbe the set of inside goods and the outside option, wheren= 0is
the outside option. LetX∈R N×K be the matrix of observed product characteristics, and
letp∈R N be the vector of inside-good prices.
For the sake of exposition, we partition the total mass of consumersHinto segments
indexed byh∈ H. Within each segment, letrindex individual consumers. Every individual
consumer chooses exactly one alternative fromN. For an individual consumerrbelonging
to segmenth, the indirect utility obtained from inside goodiis:
uhri =x ′ iβh −p i| {z }
≡νhi, deterministic inside-good utility
+εhri (1)
whereβ h ∈R K is the consumer-segment-specific vector of preference coefficients for the
observed characteristics, andεhri is an individual-specific idiosyncratic valuation. Normalise
the utility of the outside option (νh0 =x ′ 0β−p 0 = 0) and let:
εhr = (εhr0, . . . , εhrN )′ ∼F h(ε|X,ξ h)(2)
whereξ h represents any segment-specific terms governing the distribution of idiosyn-
cratic preferences. These terms may determine, for example, the dispersion of idiosyncratic
valuations, their correlation across products, or the extent to which consumers in segmenth
distinguish between similar products. The dependence ofFh onXfurthermore permits the
εhr to change withN: e.g., idiosyncratic valuations for two products may be more strongly
correlated when the products have similar observed characteristics.
Individual consumerrchooses alternative with the highest indirect utility:
i∗ hr = arg max i∈N {νhi +ε hri}(3)
The resulting inside-good choice probabilities for segmenthare:
zhi(ν h, X) = Pr[i= arg max i∈N {νhi +ε hri} |h, X,νh](4)
We can re-write segment-level inside-good choice probabilities as the maximiser of a
segment-level choice problem. Consider a candidate vector for segmenthwith the usual
properties:
z= (z 1, . . . , zN )′ :
NX
i=1
zi ≤1, zi ≥0∀i= 1, . . . N(5)
With unit demand and discrete choice, eachzi specifies that a fractionzi of the consumers
in segmenthmust choose inside goodi, whilez 0 = 1−1 ′zspecifies the fraction choosing
the outside option.
Segment-level choice probabilities are the result of consumers sorting themselves into
whichever alternative yields them the highest indirect utility. To re-write segment-level
4

inside-good choice probabilities as the maximiser of a segment-level choice problem, there
must be a way for a segment-level "social planner" to allocate them similarly, given data over
individual consumer preferences. Naturally, for a given candidatez, consumers should be
assigned to each product in order to make those shares consistent with the greatest possible
aggregate idiosyncratic utility; otherwise, the decision of the segment-level "social planner"
and that of the individual consumers will differ. In that sense, the "social planner" needs to
work backwards so that, conditional on an observed candidatezand given the distribution
of idiosyncratic errors, it may identify which consumers most likely bought each good such
that the segment as a whole deliversz.
LetP h(z)be a possible collection of partitions{A 0, A1, . . . , AN }of the idiosyncratic-
preference space of consumer segmenthsatisfying:
Fh(Ai |X,ξ h) =
Z
Ai
dFh(ε|X,ξ h) =z i Fh(A0 |X,ξ h) = 1−1 ′z∀i= 1, . . . , N(6)
The setA i represents one possible set of consumers assigned to alternativeigiven our
assignment rule. Unit demand and discrete choice require the size of each setAi to equal the
corresponding choice share. The candidatezenters the assignment problem by determining
the size of each group of consumers assigned to each product. In this sense,Fh provides
the correspondence between the observed market share of each good to the set of specific
consumers which bought it. Think of theεof each consumer as different pieces of cake.
Consumers are partitioned based on what size piece they received for each good, and keep
only the piece of cake corresponding to the good of their partition. Then, the total size
of all pieces in each partition of each good must be equivalent to the segment-level choice
probability of that good.
To obtain the collection of partitions which correspond to a given candidatez, define:
Zh(z, X,ξh) = sup
AiN i=0∈Ph(z)
{
NX
i=0
Z
Ai
εi dFh(ε|X,ξ h)}(7)
The functionZ h(z, X,ξh)is the greatest aggregate idiosyncratic utility attainable while
delivering the choice shares specified byz. The maximising partition assigns each product
to those consumers for whom that product has the strongest idiosyncratic advantage relative
to the alternatives. This structure follows from transport theory, and is equivalent to the
allocation of a continuously distributed mass - in this case, of consumers - to finitely many
destinations - in this case, products - subject to capacity/mass constraints - in this case,
product shares (more on this in Galichon and Salanié, 2022; and Bonnet, Galichon, Hsieh,
O’Hara, and Shum, 2022).
Now note the following (see Rockafellar, 1970; Hofbauer and Sandholm, 2002; Fosgerau,
Melo, de Palma, and Shum, 2020):
5

Proposition 1: The segment-level choice probabilities generated by the underlying addi-
tive random-utility model admit the equivalent perturbed utility representation:
zh(ν, X) = arg max
z:PN i=1 zi≤1,zi≥0∀i=1,...N {ν ′ hz+Z h(z, X,ξh)}
For each candidatez, the termv ′zrecords the systematic utility associated with those
shares, whileZh(z, X,ξh)records the greatest idiosyncratic utility attainable by sorting con-
sumers across products in a manner consistent with those shares.
Now consider the following question: under what conditions does this optimisation de-
liver segment-level linear demand? Notably,Zh(z, X,ξh)is concave. 2 IfZ h(z, X,ξh)were
quadratic inz, (8) would resemble quadratic utility, commonly used to reproduce linear
demand from a representative consumer’s preferences (see Amir, Erickson, and Jin, 2017;
and Choné and Linnemer, 2020). Turns out, there is a particular class of random-utility
distributions which makes this possible.
Assume that we observelocal substitutionfor a particular product category and can
represent it through a consumer-segment-specific, one-dimensional Hotelling-style ordering
of products:
αhi1 < αhi2 < . . . < αhiN < α0 = 0(8)
Consumers are said to exhibit local substitution if alternatives can be arranged accord-
ing to an ordering of similarity such that, when a preferred product becomes unavailable or
sufficiently unattractive, substitution is concentrated on the nearest available alternative in
that ordering (for evidence of this in e.g. the automobile industry, see Berry, Levinsohn, and
Pakes, 2004, and Grieco, Murry, and Yurukoglu, 2024).
We can place additional structure on the idiosyncratic errorsεhri such that:
εhri =α i(X,ξ h)ϵhr ϵhr ∼U[0,1](9)
withα h0 = 0.3 Consumers within a segment therefore differ along a one-dimensional taste
coordinateϵ hr, while the locations{α hi}N i=0 determine how the alternatives are positioned
along that taste dimension. Under this distribution, the optimal assignment of consumers
2Consider two feasible share vectorszand ez, together with assignments attaining their corresponding
values ofZ h. For anyλ∈[0,1], apply the first assignment to a fractionλof the segment and the second
assignment to the remaining fraction1−λ. This produces the combined sharesλz+ (1−λ) ezand delivers
aggregate idiosyncratic utilityλZh(z, X,ξh) + (1−λ)Zh(ez, X,ξh). BecauseZ h selects the best assignment
consistent with the combined shares, it must satisfyZ h(λz+ (1−λ) ez, X,ξh)≥λZ h(z, X,ξh) + (1−
λ)Zh(ez, X,ξh).
3This is equivalent to assumingsingle-crossing preferences- i.e., as the consumer-specific idiosyncratic
preference term rises, the utility-maximising alternative for that consumer "moves through" the products
according to their ordering on theα-line a single time; anduniform latent heterogeneity.
6

to products yields:
Zh(z, X,ξh) = sup
Ai∈Ph(z)
NX
i=0
Z
Ai
αhiϵ dϵ
=
NX
i=1
αhi
Z P
j:αhj ≤αhi zj
P
j:αhj <αhi zj
ϵ dϵ
=− 1 2
NX
i=1
|αhi|z2 i − X
i<j
min{|αhi|,|α hj|}zizj
=− 1 2
NX
i=1
NX
j=1
zizj[|αhi|+|α hj| − |αhi −α hj| 2 ]
=− 1 2 z′Mh(X,ξ h)z,for{M h}ij = |αhi|+|α hj| − |αhi −α hj| 2
(10)
The element{M h}ij has a simple geometric interpretation: it is the length of the overlap
between the intervals joining0toα hi and0toα hj on the segment’s taste line. The segment-
level choice problem therefore becomes exactly:
zh = arg max z≥0,1 ′z≤1

ν ′ hz− 1 2 z′Mhz  =M −1 h (Xβ h −p)(11)
with the latter equality representing the unconstrained case, where the probability con-
straints are slack. Thus, exact linear stochastic choice follows from a random-utility model
in which the marginal sorting cost associated with expanding product shares is linear.
Theαterms enter as a product-specific penalty. They can be understood as introducing
a product identity to how products derive their utility from the characteristics they hold.
Without the cardinal ordering with theαs, two goods with the same observed character-
istics are the same; with the ordering - and note thatαcan depend on their respective
product characteristics as well - indirect utilities receive a product-specific adjustment. This
somewhat changes the definition ofν, to the maximum indirect utility a consumer in their
respective segment can derive from a good while remaining within that segment.
Figure 1 provides a useful two-good, two-segment illustration of this section’s core result.
Two consumer segments differ both in preferences for characteristics and how they order
goods outside those preferences, represented by the x-axis. The y-axis is the total indirect
utility of each good. At higherε hr we have consumers where the cardinal ordering holds
greater weight - this can be sufficient to upend the initial ordering for a consumer of that
segment. On the left, this means a consumer going from preferring good 2 (in green), to good
1 (in yellow), to finally preferring to not buy anything at all (the outside option, in blue). On
the right, the segment starts preferring good 1, then good 2, and finally the outside option.
These movements along the y-axis produce these goods’ respective market shares for each
segment, the bars observed at the bottom of each of these sub-figures. The cardinal ordering
can be perceived as a penalty of varying strengths on the deterministic utility derived from
7

the product characteristics, shifting indirect utility orderings without loss of generality.
The sub-figure on the bottom reproduces what aggregate demand looks like for a popu-
lation composed of 45% consumers in segment1and 55% consumers in segment2, with a
kink at the reservation price of segment1. The price increase offers an additional dimension
- notice how when price of good 2 increases, only the market share of good 1 changes in
the sub-figure on the left - reflecting the idea of local substitution. Consumers of good 2
in segment 1 only move to the outside option after rejecting both good 2 and good 1. The
same does not apply in the sub-figure on the right, where we see substitution to good 1 and
the outside option.
Figure 1:Two-good, two-segment example under a price increase
The one-dimensional representation of the cardinal ranking is visibly imposing structure
onM −1 h within any individual consumer segment. Let:
dh,ikik+1 =|α hik+1 −α hik|(12)
be the distance between consecutive alternatives. GivenM h, the respective response
8

matrixL h, including the outside option, is as follows:
Lh =
1′M −1 h 1−(M −1 h 1)′
−M −1 h 1M −1 h

=
N−1X
k=0
1
dh,ikik+1
(eik −e ik+1)(eik −e ik+1)′.(13)
Note that this implies two key properties:
{M −1 h }ij ={L h}ij =
(
− 1 |αhi−αhj | ifi, jare consecutive
0otherwise
≤0,∀i̸=j(14)
and
Lh1N+1 = 0 ={L h}i0 +
NX
j=1
{M −1 h }ij
⇒ {M−1 h 1}i =−{L h}i0 =
(
1
|αhi−α0| ifi,0are consecutive
0otherwise
≥0,∀i
⇔M −1 h 1≥0
(15)
For a particular segment, alternatives are only substitutes when they are adjacent on that
segment’s taste line. Yet this segment-level sparsity disappears under aggregation. Different
consumer segments may order the products differently, so different pairs of alternatives
may be adjacent for different segments. However, the conditions in (14) and (15) survive
aggregation. Letµ h be segment weights and define:
M −1 = X
h∈H
µhM −1 h (16)
Then:
[M −1]ij =
Z
H
{M −1 h }ij, dµ(h)≤0,∀i̸=j, M −11=
Z
H
M −1 h 1, dµ(h)≥0 (17)
In fact, aggregation can generate any symmetric positive-definiteM −1 which satisfies
theserestrictions. Toseethis, consideranysymmetricpositive-definitematrixM −1 satisfying
(17). Define its full(N+ 1)×(N+ 1)response matrix:
L−1 =
1′M −11−(M −11)′
−M −11M −1

=
X
0≤i<j≤N
wij(ei −e j)(ei −e j)′, w ij ≡ −{L−1}ij >0.
(18)
Now consider all possible one-dimensional orderingsPof theN+ 1alternatives, and let
nij be the number of such orderings in whichiandjare adjacent. Choose any positive
segment weightsλP satisfying P P λP = 1. For every pairi, jthat is adjacent in orderingP,
choose their distance on that segment’s line to satisfy:
dP,ij = λP nij
wij
⇔ 1 dP,ij = wij λP nij .(19)
9

The distance between adjacent alternatives in the segment will be increasing in the seg-
ment weight, the number of alternatives, and decreasing in their desired substitution weight.
The response matrix generated by segmentPis therefore:
L−1 P = X
i,jadjacent inP
wij
λP nij
(ei −e j)(ei −e j)′.(20)
Aggregating across these segments gives:
X
P
λP L−1 P = X
P
X
i,jadjacent inP
wij
nij
(ei −e j)(ei −e j)′
=
X
0≤i<j≤N
wij(ei −e j)(ei −e j)′
=L −1
(21)
The second equality follows because each pairi, jis adjacent in exactlynij of the order-
ings. Taking the inside-good block, we recoverM−1 = P P λP M −1 P .
The importance of this is clear. We have shown that any symmetric positive-definite
M −1 satisfying (14) and (15) can be generated exactly by a finite mixture of these globally
quadratic one-dimensional random-utility segments. In Section 4.3, I show how this aggre-
gate term can be used to discipline the sum of individual corner corrections, needed once
we impose non-negativity constraints on segment-level choice probabilities. In Section 5.4, I
explore the aggregate demand implications of some well-known network graphs, whereMis
interpreted as an adjacency matrix.
This completes our proof that segment-level choice probabilities can be framed via a
linear demand system. Under what conditions can we aggregate across segments to obtain
aggregate linear demand?
Aggregate demand is:
q(p, X) =
X
h∈H
µhM −1 h (Xβ h −p).(22)
Suppose characteristic preferences satisfyE[βh |ξ h] =β. 4 Then, it follows that:
q(p, X) =
"X
h∈H
µhM −1 h
#
(Xβ−p) =M −1(Xβ−p)(23)
forM −1 = P h∈H µhM −1 h .
4This does not requireβ h =βfor every segment; it requires only that the conditional mean of char-
acteristic preferences does not vary systematically with the primitivesξh governing the segment’s demand
responsiveness.
10

The model can incorporate heterogeneous choice sets across consumer segments. To see
this, letJ h be the set of inside goods available to segmenth. A goodj /∈ Jh is therefore
structurally unavailable to that segment and has zero choice probability at every price;
it is not at a price-induced corner. The setC h(p, X)⊆ Jh contains only corners among
goods which the segment could in principle purchase; permanent choice-set exclusions can
be directly incorporated in the aggregateM −1 via individualM 1 h. ForS h theN× |J h|
selection matrix which matches the goods inJh into the full product space, and starting
from fM −1 h as the|J h| × |Jh|unconstrained demand Jacobian for segmenth:
M −1 h ≡S h fM −1 h S′ h ⇒M −1 =
Z
Sh fM −1 h S′ h dµ(h)(24)
We explore how this matrix architecture can used to allow for discrete choice models
over baskets of goods - and how this may be an avenue for introducing complementarities
between goods - in Section 5.7.
We have worked throughout with consumer segments. Albeit useful, the segmentation
of consumers is not necessary for any of the arguments in this section or the paper. Rather
than segment-level choice probabilities,z h could instead be a consumer-level probability
of choosing amongst available alternatives prior to drawingεh. While we have separated
the segment-levelαorderings from consumer-levelϵthroughout this section, both can be
consumer-specific in practice. All points would then follow through via expected value.
Nonetheless, because discussing concepts likeZcan be less intuitive without segments, we
retain the segmentation rationale for the rest of the paper.
3 Extensions
3.1 Income effects
In this section, I introduce income effects to aggregate linear demand. This is not so much
a problem in models such as Hotelling (1929), Salop (1979), or Chen and Riordan (2007),
yet as mentioned above the more common tool for linear demand estimation is quasilinear
(i.e. income-effect-free) quadratic utility.
Allowing for income effects has an important implication: that linear demand systems
may successfully operateincomplete demand system, where demand for a set of inside goods
can be analysed without specifying consumers’ entire consumption vector (Epstein, 1982;
LaFrance, 1985). The goal is to find general conditions under which we can include income
into a discrete-choice microfoundation without affecting the functional form for aggregate
linear demand we used above. This relaxes the very restrictive conditions that the previous
literature targeting broader integrability requires (LaFrance, 1985), focusing instead on ag-
gregation made possible by discrete choice.
Lety hr be the income of consumerrin segmenthand letg(y hr −p i)be their utility
from residual income consumption. We are going to use the simplifying assumption that the
11

idiosyncratic utility term is distributed across consumers independently from income, i.e.:
Fh(ε|y) =F h(ε)(25)
The utility from buying interior goodi:
uhri =x ′ iβh +g(y hr −p i) +ε hri,∀i= 1, . . . , N uhr0 =g(y hr) +ε hr0 (26)
After normalising relative to the outside option, we have:
νhri =x ′ iβh +g(y hr −p i)−g(y hr)(27)
Now let∆g(y hr,p) = (g(y hr −p 1)−g(y hr), . . . , g(yhr −p N )−g(y hr))′. From (11) and (25),
it follows that the segment-level inside-good choice probabilities can be obtained conditional
on the distribution ofyhr. To see how, definezh(y)the segment-hchoice probability among
consumers with incomeyhr =y. Then we can write:
zh(y) = arg max z≥0,1′z≤1 {vh(y)′z− 1 2 z′Mhz}=M −1 h ν h(y) =M −1(Xβ−∆g(y,p))(28)
with slack probability constraints. Lastly, the actual segment-hchoice probabilities are
just the mixture of these income-conditional choice probabilities:
zh =
Z
M −1 h (Xβ h + ∆g(y,p))dF Y|h (y)
=M −1 h (Xβ h +
Z
∆g(yhr,p)dF Y|h (y))
=M −1 h (Xβ h +E Y [∆g(yhr,p)|h])
(29)
Lastly, aggregating across segments, we obtain:
q(p, X, y) =
X
h
µhM −1 h (Xβ h +E Y [∆g(yhr,p)|h])(30)
Under what additional conditions does the above expression simplify further into aggre-
gate linear demand?
One way to recover linear demand is to impose a simple local restriction on the utility
from residual income. Suppose that, over the relevant range,g(·)is linear both around each
consumer’s pre-purchase incomeyhr and over the range containing all post-purchase residual
incomesy hr −p i, with different slopes. Then, for consumerr:
g(yhr −p i)−g(y hr) = (a1 hr −a 0 hr) + (λ1 hr −λ 0 hr)yhr| {z }
≡η hr
−λ1 hrpi,∀i= 1, . . . , N
⇒∆g(y hr,p) =η hr1−λ 1 hrp
(31)
Under a monotonically concaveg(·),λ 1 ≥λ 0 >0. The intercept and slope of the differ-
ence can vary across consumers. By allowingyhr andy hr −p i across all goods to belong to
12

different sections ofg(·)with different slope and intercept, these restrictions can either be
taken literally or interpreted as a first-order approximation tog(·).
The difference in the slope ofg(·)at the pre- and post-purchase residual income is what
produces the income effect in indirect utility:
∂uhri
∂pi
=−λ 1 hr ∂uhri ∂yhr =λ 1 hr −λ 0 hr ⇒ ∂uhri ∂pi =−λ 0 hr − ∂uhri ∂yhr (32)
This contrasts with the standard quasi-linear specification of utility, where a price change
leaves the marginal utility of income constant (equal toλ0 hr) which yields no income effects.
With these functional form assumptions ong(·), we can re-write our segment-level choice
probabilities:
zh =M −1 h (Xβ h +E Y [∆g(yhr,p)|h]) =M −1 h (Xβ h +η h1−λ 1 hp)(33)
forη h ≡E[η hr|h]andλ 1 h ≡E[λ 1 hr|h]. Further normalisations drop theλ 1 h frompby
correctingM −1 h ,β h,andη h - we do so going forward without altering their notation.
Our last step is to assume:
E[(βh, ηh, λ1 h)|ξh] = (β, η, λ1)(34)
which allows us to write our final expression for aggregate linear demand. Then:
Proposition 2: Under aprice increase,we can separate income from substitution effects
in aggregate linear demand by decomposing the Marshallian price derivative using the Slutsky
equation:
∂q(p, X,y)
∂p =−M −1 =− X h µh[λ1 hM −1 h −(λ 1 h −λ 0 h)·diag(M −1 h 1)] | {z }
substitution effect
−
X
h
µh(λ1 h −λ 0 h)·diag(M −1 h 1)
| {z }
income effect
The intuition here is that, outside substitution effects, price increases decrease residual
income; they shift all inside goods relative to the outside option, and therefore only gener-
ate switching from inside-good to outside-good purchases. The consumers affected by this,
those who shift their choice following the price increase, are current purchasers who decide
not to purchase anymore. This means that the pre-change choice is for the same good whose
inside-outside boundary is crossed, delivering(λ1 h −λ 0 h)·diag(M −1 h 1).
For completeness, a marginal price decrease gives a different compensated derivative,
and thus a different substitution effect. While with a price increase the consumers who
switch their choice are current inside-good buyers moving to the outside option, with a price
decrease we observe only the opposite move. This means that, at the pre-change choice,
dM hri = 0, meaningE[(D ydM hr)dM ′ hr |h] = 0, and thusD − p zH h =−λ 1 hM −1 h =D pzM h - no income
13

effect in that instance.
Under the conditions which deliver aggregate linear demand, income entersq(p, X)as
a market-level demand shock. Notably, we have produced income effects without creating
Slutsky asymmetry, due to these operating exclusively through the inside–outside margin.
This is significant, in that the model maintains the conditions required for welfare analysis
with consumer surplus without path dependence (Tirole, 1988).
3.2 Corner solutions
The aggregate linear demand system derived above assumes that the probability con-
straints in each segment’s choice problem are slack. In this section, I relax the non-negativity
constraints while retaining the same discrete-choice microfoundation. The goal is to char-
acterise aggregate demand when some segment-level product shares reach zero. While this
means departing from aggregate linear demand in general, it is the microfounded linearity
of unconstrained demand that (1) facilitates analysis of non-linear corner solutions, and, as
we see later, (2) constrains them sufficiently for structural estimation.
From (11), recall that the actual segment-level choice probabilities can be derived as
follows:
zh(p, X) = arg max z≥0,1 ′z≤1

(Xβ h −p) ′z− 1 2 z′Mhz  (35)
To isolate product-level corner solutions, suppose throughout the rest of the paper that
the outside-option constraint remains slack; that is to say, there is always a small set of
consumers who do not purchase. The only relevant constraints are thereforezhj ≥0,∀h, j.
For any price vector, letCh(p, X)≡ {i:zhi(p, X) = 0}be the set of inside goods that
are at a corner for segmenth, of size|C h|dependent on price and product characteristics
(references to those are dropped from the subscript). The setCh may contain any number
of products. The Karush-Kuhn-Tucker conditions are:
Mhzh =Xβ h −p+λ h, λ hj ≥0, z hj ≥0, λ hjzhj = 0,∀j(36)
forλ h ≥0be the vector of multipliers on the non-negativity constraints. The binding
constraints require:
0 ={z I h}|Ch|×1 +{M −1 h }|Ch|×|Ch|{λh}|Ch|×1 ⇒ {λ h}|Ch|×1 =−({M −1 h }|Ch|×|Ch|)−1{zI h}|Ch|×1
(37)
for{·} |Ch|×|Ch| and{·} |Ch|×1 operators which select the rows and columns indexed by those
goods inC h from the object they are related to. The subscripts therefore contain informa-
tiononthedimensionsofmatricesandvectorsimpactedbythesetofinsidegoodsatacorner.
Segment-level demand is then:
zh(p, X) =zI h(p, X)− {M−1 h }N×|C h|({M −1 h }|Ch|×|Ch|)−1{zI h}|Ch|×1 = (M C h )−1(Xβ h −p)
(38)
14

forM −1 Ch ≡M −1 h − {M−1 h }N×|C h|({M −1 h }|Ch|×|Ch|)−1{M −1 h }′ |Ch|×N the effective demand Ja- cobian associated with setCh for pricepand product characteristicsX. A product whose
choice probability has reached zero automatically stops contributing its own- and cross-price
responses, while the remaining goods continue to satisfy a linear demand.
This gives us an exact decomposition of aggregate demand. Under the same aggregation
condition used above for the interior model, we may write aggregate demand as follows:
q(p, X) =M−1(Xβ−p)− X
h
µh{M −1 h }N×|C h|({M −1 h }|Ch|×|Ch|)−1{M −1 h (Xβ h −p)} |Ch|×1
=M −1(Xβ−p) +κ(p, X)
(39)
forκ(p, X)the aggregate correction generated by segment-level non-negativity con-
straints. Unlike unconstrained demand, which only depends onE[β h|ξh] =β, the corner
correction depends on the full distribution ofβparameters, since heterogeneity in preferences
determines which constraints bind. Conditional on a fixed setCh, segment-level demand re-
mains linear, with price derivative−M−1 Ch . Aggregating across segments, we therefore obtain,
wherever the derivatives exist:
Dpq(p, X) =−
X
h
µhM −1 Ch , D pκ(p, X) =M−1 − X
h
µhM −1 Ch (40)
With finitely many segments, demand is continuous and piecewise linear, with changes
in its Jacobian whenever segment-level constraints become binding or cease to bind. With
continuous heterogeneity, however, these changes need not occur at the same prices across
segments. In our context, this gives us smoothness:
Proposition 3: If, at any given prices, there is no positive mass of segments exactly at
the threshold where a product starts or stops being purchased, then aggregate demandq(p, X)
is continuously differentiable in that region.
Proposition 3 does not impose any particular distribution of consumer preferences or
product orderings. However, that there be no positive mass of segments at thresholds re-
quires segment-level changes in the demand Jacobian that are sufficiently dispersed across
prices. Such dispersion is especially dependent on heterogeneity in segment-specific product
orderings, distances between alternatives, or characteristic preferences. This is because, from
the KKT conditions, the prices at which constraints become binding or cease to bind depend
onβ h. Continuous heterogeneity in these preferences therefore ensure that no positive mass
of segments changes its binding constraints at exactly the same prices, provided the relevant
thresholds vary nontrivially withβh. We explore this next.
4 Sketch of structural estimation with market-level data
The model as developed above requires demand estimation of a piecewise linear system,
and the separate estimation of the interior linear demand function with the corner distance
15

densities. In this section, I sketch out one way to identify and estimate each parameter and
distribution. I will assume we observe only market-level, anonymised transaction data over
multiple periods.
4.1 Parameterising unconstrained linear demand
One of the first issues to address is the fact that, without consumer-level data, we can-
not identify or estimate any segment-level parameters. Suppose that we observe aggregate
quantitiesq t, pricesp t, product characteristicsX t, and excluded instruments over periods
t= 1, . . . , T. We do not observe consumer segments, their choice sets, or their segment-level
choice probabilities. Without consumer-level data, the objects associated with those seg-
ments are not parameters which we can separately identify or estimate. Their role is instead
to place structure on the aggregate demand function.
In (39), the objects appearing insideκ(p, X)are defined at the segment level and are
not observed in aggregate data. We can therefore estimate only their aggregate effect. The
discrete-choice microfoundation is nevertheless useful because it imposes considerable struc-
ture on what this correction can look like.
The first step in estimation is to obtain a parsimonious initial estimate of the uncon-
strained linear component of the demand system. To do so, I will rely on the fact that we
have allowed the distribution of individual idiosyncratic errors,Fh(ε|X,ξ h), and therefore
Zh(zh, X,ξh)andultimatelyM h(X,ξ h), todependatleastpartiallyonX. Thisseemsappro-
priate: more similar goods are presumably more likely to be adjacent in the one-dimensional
taste line, and therefore consumers may hold correlated idiosyncratic preferences for them.
LetKbethenumberofobservedproductcharacteristicsandwritetheQRdecomposition:
Xt =Q tRt, Q ′ tQt =I K,(41)
whereQ t is aN×Korthonormal matrix andR t is aK×Kupper triangular matrix. I
make use of Lemma 1 from Rodrigues (2026):
Lemma 1 (Rodrigues, 2026): Any symmetric positive definite matrixM t that de-
pends in part on observed product characteristicsXand imposes no arbitrary structure on
unobserved dimensions admits the following representation:
Mt =Q tDQ′ t +ρ(I−Q tQ′ t),(42)
whereDis aK×Ksymmetric positive-definite matrix andρ >0.
After inversion and some re-arranging, a regression of unconstrained demand may con-
16

sequently be written as follows:
mt(θ)≡M −1 t (Xtβ−p t) =Q tD−1Rtβ− 1 ρ pt −Q t

D−1 − 1 ρ I  Q′ tpt
⇒q t(θ) =m t(θ) +κ(p t, Xt,θ) +v t
(43)
forθ= (β ′, ρ,vech(D−1)′) ′ andv t the unobserved error term. The number of parameters at
this point isK(K+3) 2 + 1, so the dimension of the unconstrained demand problem grows only
with the number of characteristics rather than with the number of goods.
4.2 Addressing price endogeneity
For identification, we need to overcome endogeneity which may arise from a correlation
between prices and the unobserved error termvt =q t −M −1 t (Xtβ−p t)−κ(p t, Xt). This
is not a uniquely difficult issue for linear demand systems to overcome. Let there be a
candidate instrument matrixP I t, with number of dimensionsJequal to the number of
unobserved parameters. These can be used in the standard way to address endogeneity in
prices, through e.g. product-specific moments:
Ht = diag(pI ′ 1t, . . . ,pI ′ N t)∈R N×N J ⇒E[H ′ tvt] =E([p I 1tv1t . . .pI N tvN t]′) =0(44)
This produces the following moments and the initial nonlinear-GMM estimator, respec-
tively:
g0,T (θ) = 1 T
TX
t=1
H ′ tv(0) t (θ) bθ (0) = arg min θ∈Θ g0,T (θ)′W0g0,T (θ).(45)
whereW 0 is a specified positive-definite weighting matrix andΘimposes the demand
restrictions described above. The problem is nonlinear becauseQtD−1Rtβis bilinear inD −1
andβ. Further moments may be added; this is just one example.
One concern raised in Gandhi and Nevo (2021) is that it may not be possible to find
sufficient (non-collinear) instruments to address endogenous prices when all goods’ enter the
demand function of all other goods. As can be seen in (43), however, prices enter as a vector;
and their direct impact and through substitution with other goods - in the second to last
and last terms of that equation respectively - can be separated byQtQ′ t in the last term.
However, and crucially, when corners are present,v(0) t (θ0) =v t +κ(p t, Xt)and the in-
struments will therefore not be orthogonal to the omitted correction:E[H′ tκt]̸=0. We must
characterise the corner correction, doing so only using the market-level data available.
4.3 Accounting for corner solutions
The purpose of the initial corner-excluding estimator will instead be to provide a disci-
plined starting value for the full corner-adjusted estimator. To construct that estimator, we
17

return to a unique characteristic of our main result. Recall that every symmetric positive-
definiteM −1 t satisfying the discrete-choice restrictions above can be generated by a finite
mixture of globally quadratic one-dimensional random-utility segments. As before, define
the associated full(N+ 1)×(N+ 1)response matrix:
Lt =
1′M −1 t 1−(M −1 t 1)′
−M −1 t 1M −1 t

=
X
0≤i<j≤N
wij,t(ei −e j)(ei −e j)′ (46)
for
wij,t ≡ −[Lt]ij,∀0≤i < j≤N.(47)
Once again, letPbe the set of one-dimensional orderings of theN+ 1alternatives,
includingtheoutsideoption. WeuseRsimulatedpermutations,π 1, . . . , πR, eachrepresenting
one possible arrangement of the alternatives along a segment’s taste line. Under uniform
draws, the probability that two distinct alternatives are adjacent is:
Pr(i∼ πr j) = 2N! (N+ 1)! = 2 N+ 1 .
To allow some pairs to be adjacent more frequently than others, we allow the complete
orderings themselves to have different probabilities. These probabilities are drawn jointly
from a symmetricDirichlet(δ/|P|, . . . , δ/|P|), forδa parameter for total concentration,
which controls how tightly the randomly drawn ordering probabilities cluster around equal
probabilities. Asδ→ ∞, the probabilities of the different orderings approach uniformity,
and every pair has adjacency probability2/(N+ 1). Asδ→0, probability concentrates on a
single randomly favoured ordering, making its adjacent pairs much more frequent than other
pairs. There are|P|= (N+ 1)!probabilities, each with Dirichlet parameterδ/|P|, and they
sum to one. We draw this probability distribution once, then drawπ1, . . . , πR independently
conditional on it.5
Adjacency frequencies are obtained directly from the simulated permutations. The under-
lying random numbers are held fixed throughout estimation; ifδchanges, the permutations
are regenerated using those same random numbers. Let:
ˆnij =
RX
r=1
1{i∼ πr(δ) j},(48)
bethenumberofdistinctpermutationsinwhichi, jareadjacent, where1{i∼ πr(δ) j}indi-
cateswhetheriandjareadjacentinpermutationπ r drawnfromDirichlet(δ/|P|, . . . , δ/|P|).
This definition applies to all pairs, including those involving the outside option.6 For every
adjacent pair under orderingπr, define:
dr,ij,t =λ πr
ˆnij
wij,t
(49)
5The permutations can be generated without enumeratingP. Drawπ1 uniformly. At drawr≥2, draw
a uniform permutation with probabilityδ/(δ+r−1); otherwise, select one of the previousr−1draws
uniformly and repeat its ordering. Selection is among previous draws, including repetitions. This generates
the same joint distribution as the Dirichlet specification (Blackwell and MacQueen, 1973).
6Note that the construction below requiresˆnij >0wheneverw ij,t >0.
18

forλ πr a permutation weight satisfyingPR r=1 λπr = 1and1 ′zP <1. Construct:
Lr,t =
X
0≤i<j≤N, i∼πr (δ)j
wij,t
λπr ˆnij
(ei −e j)(ei −e j)′ (50)
The inside-good block ofLr,t defines the response matrixM−1 r,t associated with simulated
orderingπ r. Conditional on the coverage requirement, this construction has the following
exact finite-simulation property:
RX
r=1
λπrLr,t =
RX
r=1
X
i∼πr (δ)j
wij,t
ˆnij
(ei −e j)(ei −e j)′
=
X
0≤i<j≤N
wij,t
ˆnij
" RX
r=1
1{i∼ πr j}
#
(ei −e j)(ei −e j)′
=
X
0≤i<j≤N
wij,t(ei −e j)(ei −e j)′
=L t
(51)
Taking the inside-good block therefore gives:
RX
r=1
λπrM −1 r,t =M −1 t (52)
Thus, the simulated response matrices reproduce the candidate aggregateM−1 t exactly,
even for finiteR. The matricesM−1 r,t are numerical integration objects, rather than separately
estimated parameters of observed consumer segments. Their role is to provide a structured
decomposition of the aggregate unconstrained demand from which the segment-level corner
corrections can be computed. Note how the manner in which we weigh each permutation
cancels out - our results therefore generalise across any such weight. Thewij,t are uniquely
implied byL t, yet the way that weight is allocated across the different permutations con-
tainingi, jis not. This is not a problem as it cancels out.
Now, while the permutation method above addresses heterogeneity in the segment-level
M −1 h terms, the location of a segment choice probabilities relative to corner boundaries de-
pends also on preferences parametersβh. Our corner correction depends not just onβ, but
its distribution in the consumer population. Notably, both the distributions of preference
heterogeneity and permutation need to be specified if we wish to obtain uniqueness of the
simulated corner correction term.
For each simulated orderingπr, letℓ= 1, . . . , Sindex draws from the conditional distri-
bution of characteristic preferences and write:
βrℓ =β+ Γζ rℓ E[ζ rℓ |ξ r] =0E[ζ rℓζ′ rℓ |ξ r] =I K (53)
theΓaK×Kthe Cholesky factor of the variance-covariance matrix ofβ rℓ. The mean
coefficient remainsβ, whileΓgoverns the heterogeneity in characteristic tastes which is rel-
evant for the corner correction. For simplicity, letΓ = diag(σ1, . . . , σK), forσ k ≥0,∀kas a
19

baseline.7
It follows from (53) that:
1
S
SX
ℓ=1
βrℓ =β(54)
Therefore, using (52), and for unconstrained zero-price demandsrℓ,t ≡M −1 r,t Xtβrℓ:
1
S
RX
r=1
λπr
SX
ℓ=1
srℓ,t =
RX
r=1
λπrM −1 r,t Xt
"
1
S
SX
ℓ=1
βrℓ
#
=
RX
r=1
λπrM −1 r,t Xtβ
=M −1 t Xtβ
≡ st
(55)
At observed prices, unconstrained demand for draw(r, ℓ)is:
zI rℓ,t =M −1 r,t (Xtβrℓ −p t) =s rℓ,t −M −1 r,t pt (56)
Averaging over the simulated orderings and random coefficients gives:
1
S
RX
r=1
λπr
SX
ℓ=1
zI rℓ,t = 1 S
RX
r=1
λπr
SX
ℓ=1
srℓ,t −
RX
r=1
λπrM −1 r,t pt
=M −1 t Xtβ−M −1 t pt
=M −1 t (Xtβ−p t)
=m t(θ)
(57)
In other words, the random-coefficient simulation reproduces exactly the aggregate un-
constrained demand system implied by the initial model, while allowing the latent demands
around that mean to be heterogeneous. This is key for our following step: completing the
argument that we can use aggregate terms to fully constraint the corner correction, and
therefore eliminate price endogeneity. It is key because unconstrained demand enters the
corner correction directly, as we saw in e.g. (39).
The setC rℓ,t is obtained directly from the Karush-Kuhn-Tucker conditions. For draw
(r, ℓ), we obtain unconstrained demandzI rℓ,t from (56). The goods for whichz I i,rℓ,t ≤0
7Additional details: a bounded symmetric mixing distribution provides a convenient specification of
heterogeneity in preferences for characteristics, with boundedness in particular making the assumption of
slackness in the outside option condition1′zh <1possible. For example, the components ofζ rℓ may be
independently distributed, e.g.ζrℓk ∼U[−
√
3,
√
3]which gives zero mean and unit variance. The simulation
may be constructed so that the conditional-mean restriction is satisfied exactly for finiteS, for example by
conditioning the draws on1 S PS ℓ=1 ζrℓ =0for everyr.
20

provide an initial candidate active set. Given any candidate setC, the implied constrained
demand and corresponding multipliers are:
zrℓ,t(C) =z I rℓ,t − {M−1 rℓ,t}N×|C rℓ,t|({M −1 rℓ,t}|Crℓ,t|×|Crℓ,t|)−1{zI rℓ,t}|C|×1
λrℓ,t,|C|×1 =−({M −1 rℓ,t}|Crℓ,t|×|Crℓ,t|)−1{zI rℓ,t}|C|×1 (58)
In theory, to obtain the realised setCrℓ,t we would have to repeatedly updateCuntil
zrℓ,t,|C|×1 =0(remainingzpositive)andλ rℓ,t,|C|×1 ≥0(remainingλequaltozero), producing
the exact draw-level corner correction:
κrℓ,t =−{M −1 rℓ,t}N×|C rℓ,t|({M −1 rℓ,t}|Crℓ,t|×|Crℓ,t|)−1{zI rℓ,t}|Crℓ,t|×1 (59)
While straightforward as a solution and parallelisable, it is still computationally demand-
ing, especially for large choice sets. Instead, we can exploit the one-dimensional structure
of the idiosyncratic valuations underlying each simulated permutation to obtain the con-
strained choice probabilities directly, without iterating over candidate corner sets.
Recall from (12) that the positionsαi,r,t <0for all inside goods andα 0,r,t = 0can be
recovered from the distancesd r,ij,t defined in (49), up to the normalisation of the outside
option. For two alternativesiandi+ 1, withα i,r,t < αi+1,r,t, their utility functions intersect
at:
ϵ∗ i,i+1,rℓ,t = νi,rℓ,t −ν i+1,rℓ,t αi+1,r,t −α i,r,t = νi,rℓ,t −ν i+1,rℓ,t dr,i,i+1,t (60)
To obtain the corner corrections, start from the alternative with lowestαinπr, and com-
pare each successive alternative. If their intersection occurs before the point at which the
first alternative becomes optimal - e.g. ifϵ∗ i,i+1 ≤ϵ ∗ i−1,i - that alternativeiis removed, and
the comparison is repeated with its predecessor. Otherwise, the new alternative is added to
anenvelope. 8
LetB rℓ,t = (b1, . . . , bm)be this envelope, the resulting sequence of retained alternatives,
ordered by increasingαi,r,t. Define the intersection between consecutive retained alternatives
as:
τk,rℓ,t = νbk,rℓ,t −ν bk+1,rℓ,t
αbk+1,r,t −α bk,r,t
, k= 1, . . . , m−1(61)
withτ 0,rℓ,t =−∞andτ m,rℓ,t = +∞. To derive the corresponding choice probabilities,
note that, by construction of the envelope, each retained alternativebk maximises utility
between its intersections with the preceding and succeeding retained alternatives. E.g., since
αbk−1,r,t < αbk,r,t < αbk+1,r,t, we have:
ubk,rℓ,t(ϵ)≥u bk−1,rℓ,t(ϵ)⇔ϵ≥τ k−1,rℓ,t
ubk,rℓ,t(ϵ)≥u bk+1,rℓ,t(ϵ)⇔ϵ≤τ k,rℓ,t
8By envelope here we mean the upper envelope of the lines in the segment graphs of Figure 1, which
corresponds to what a given consumer segment purchases at eachε.
21

with the first and last alternatives bounded by the uniform distribution. The set of idiossyn-
cratic errors for which a given alternativebk maximises utility over all available alternatives
is:
Ek,rℓ,t ={ϵ∈[0,1] :τ k−1,rℓ,t ≤ϵ≤τ k,rℓ,t}
= [0,1]∩[τ k−1,rℓ,t, τk,rℓ,t]
= [max{0, τk−1,rℓ,t},min{1, τk,rℓ,t}],
(62)
The corresponding choice probability is simply the length of this interval:
zbk,rℓ,t = Pr (ϵ∈ Ek,rℓ,t)
=
Z 1
0
1{τ k−1,rℓ,t ≤ϵ≤τ k,rℓ,t}dϵ
= max{min{1, τk,rℓ,t} −max{0, τk−1,rℓ,t},0}.
(63)
The clipping at zero and one reflects the bounds of the support ofϵ. Alternatives which
never maximise utility over this interval receive zero demand. The realised corner set is
therefore obtained immediately asCrℓ,t ={i∈ N \ {0}:zi,rℓ,t = 0}. The exact permutation-
draw-level corner correction follows directly from the difference between constrained and
unconstrained demandκ rℓ,t =z rℓ,t −z I rℓ,t.
The corresponding predicted aggregate demand and simulated corner correction are then:
bqR,S,t(θ,σ, δ) =m t(θ) + bκR,S,t(θ,σ, δ) bκR,S,t(θ,σ, δ) = 1 S
RX
r=1
λπr
SX
ℓ=1
κrℓ,t (64)
Note that the second equation is independent ofλrℓ,t, asκ rℓ,t ∝ 1 λπr in the same way that
these cancel out above.9
4.4 Estimation procedure
At last, define the simulated residual:
vR,S,t(θ,σ, δ) =q t −m t(θ)− bκR,S,t(θ,σ, δ)(65)
and the corresponding moments:
gR,S,T (θ,σ, δ) = 1 T
TX
t=1
H ′ tvR,S,t(θ,σ, δ)(66)
Each instrument generates a separate restriction for each product. The number of periods
determines the observations used to estimate these averages. The final simulated GMM
estimator is:
{ˆθ, ˆσ, ˆδ}= arg min
θ,σ,δ∈E
gR,S,T (θ,σ, δ)′WT gR,S,T (θ,σ, δ)(67)
9This implies that once the set of permutations is fixed, changing their probabilities has no effect on
aggregate demand or the corner correction. In other words, if we could calculate every sample permutation,
δwould no longer be a source of variation and could be set toδ= 1. Instead, we keepδand instead simulate
only a sample of all possible permutations for computational simplicity.
22

whereEimposes positive definiteness, the inverse-matrix sign and row-sum restrictions,
and the admissible domains of the heterogeneity parameters.
The initial corner-excluding estimator in (45) provides the natural starting point for solv-
ing (67). At a candidate(θ (m),σ (m), δ(m)), the algorithm constructsM −1 t and st, updates
the edge weightsw ij,t, constructs the impliedM −1 r,t and random coefficientsβ rℓ for every
simulation draw, computess rℓ,t andz I rℓ,t, solves the associated Karush-Kuhn-Tucker prob-
lems, forms bκR,S,t, and reevaluates the GMM objective. The nonlinear optimizer therefore
performs the required iteration between the unconstrained demand parameters, random-
coefficient dispersion, and the corner correction automatically.10
The resulting estimator therefore retains the simplicity of the interior linear demand sys-
temwhileallowingtheaggregatedemandJacobiantochangeendogenouslyascornersbecome
binding. The first-stage nonlinear GMM provides starting values for the unconstrained linear
component. The one-dimensional random-utility representation then produces segment-level
demand Jacobian matrices, and heterogeneity in characteristic preferences establishes latent
distances from corner boundaries. Applying the exact Karush-Kuhn-Tucker solution draw by
draw and averaging the resulting corrections producesκ(p, X). Neither consumer segments
nor their parameters are observed or recovered, but the aggregate nonlinear demand system
continues to satisfy the restrictions implied by the underlying discrete-choice model.
4.5 Including income effects
The structural estimation above can be extended to incorporate the income effects devel-
oped earlier with only a minor modification. Recall that, after the normalisation introduced
there, segment-level unconstrained demand can be written as:
zI h =M −1 h (Xβ h +η h1−p)(68)
whereη h captures heterogeneity across segments in the utility contribution associated
with residual income. Since neither consumer segments nor individual incomes are observed
in the market-level data, we instead directly specify a joint distribution for the segment-
level characteristic preferences and income-related utility term. Generalising the random-
coefficient specification above, we get:
10A useful numerical warm start is to make this iteration explicit. Given(θ(m),σ (m), δ(m)), first calculate
bκ(m) R,S,t ≡ bκR,S,t(θ(m),σ (m), δ(m)), and then, holding this correction fixed, update the interior parameters:
θ(m+1) = arg min
θ
(
1
T
TX
t=1
H ′ t
h
qt − bκ(m) R,S,t −m t(θ) i)′ WT ( 1 T TX t=1 H ′ t h qt − bκ(m) R,S,t −m t(θ) i) .
Conditional onθ (m+1), the dispersion parametersσcan then be updated by minimising the simulated
GMM criterion with respect toσ. Repeating these steps several times enables the joint minimisation in (67).
Statistical inference is based on the joint estimator rather than on this preliminary fixed-point sequence.
23

βh
ηh

=
β
η

+ Γζh (69)
whereΓ, now a(K+ 1)×(K+ 1)matrix, retains its earlier interpretation. Assume the
ζdistribution has the following moments:
E[ζ h |ξ h] = 0E[ζ hζ′ h |ξ h] =I K+1 Var
βh
ηh

= ΓΓ′ ≡Σ =
Σββ Σβη
Σηβ σ2 η

(70)
Estimating the joint distribution directly is advantageous: the vectorΣ βη allows the
income-related utility term to be correlated with each element ofβh. Thus, for example,
segments with systematically largerηh may also place systematically greater weight on par-
ticular observed product characteristics. The remaining elements ofΣββ continue to allow
arbitrary taste heterogeneity unrelated toηh.
Implementation then proceeds exactly as above. For each simulated orderingrand
heterogeneity drawℓ, jointly draw:
βrℓ
ηrℓ

=
β
η

+ Γζrℓ (71)
The same Karush-Kuhn-Tucker procedure can then be applied tozI rℓ,t to determine the
set of binding non-negativity constraints and the associated corner correction. No other
modification to the simulated corner estimator is required. Once estimated, the joint dis-
tribution of(β h, ηh)can be held fixed when evaluating counterfactual changes in prices or
product characteristics, with the corresponding corner sets recomputed under each counter-
factual.
How we approach income effects has implications for the model’s status as an incomplete
demand system. Over time,g(·)is likely to vary as omitted goods vary in e.g. prices. This
variation can be incorporated into the model by allowingηto be time-varying througha1 and
a0, which preserves time invariance in the demand Jacobian and characteristics parameters.
Furthermore, note that variation in the prices or characteristics of omitted products may
enter the regression error when those products substitute with inside goods. If we wish to
keep an incomplete demand system, the instrument orthogonality condition requires care
to ensure that instruments for inside-product prices are not correlated with such omitted
variation.
4.6 Computational complexity
When corner corrections are deemed unnecessary, evaluating the unconstrained demand
system has complexityO(T N K), whereTis the number of markets,Nthe number of inside
goods, andKthe number of observed product characteristics, conditional on the relevant
matrix factorisations. The full model requires integrating over simulated product orderings
and heterogeneous preferences, but the one-dimensional discrete-choice representation allows
24

each draw-level corner correction to be calculated without an updating procedure.
What about the full model? LetRbe the number of simulated permutations andSthe
number of preference draws per permutation. For each markettand draw(r, ℓ), constructing
the deterministic utility vectorν rℓ,t requiresO(N K)operations. Conditional on the per-
mutationπ r and its associated distances, the constrained choice probabilities can then be
recovered from the envelope approach presented in Section 4.3; there, since the alternatives
are already ordered by their slopesαi,r,t, each alternative enters and leaves the envelope at
most once, so constructing it and recovering all constrained probabilities requiresO(N)oper-
ations. The unconstrained probabilitieszI rℓ,t =M −1 r,t ν rℓ,t can likewise be calculated inO(N)
operations, sinceM −1 r,t has nonzero off-diagonal entries only between alternatives adjacent
inπ r. Theexactcornercorrection,κ rℓ,t =z rℓ,t−z I rℓ,t, requiresnoadditionalmatrixinversion.
Thus, conditional on the simulated permutations and their associated corrections, eval-
uating the full demand system has computational complexityO(T RSN(K+ 1)). For com-
parison, letIbe the average number of iterations required for the BLP inversion to match
predicted market shares to their observed counterparts. Holding constant the total num-
ber of simulated market-consumer evaluationsC, a standard simulated BLP implementa-
tion requiresO(CN K)operations to construct the individual utility indices andO(CN I)
operations to perform the share inversion. Its corresponding computational complexity is
thereforeO(CN(K+I)), where the full model presented in this paper is correspondingly
O(CN(K+ 1)).
The distinction is not merely the number of operations, but also their application. In the
full model, theT RSsimulated corner problems are independent conditional on the demand
parameters, and can therefore be evaluated in parallel before their corrections are aggre-
gated. BLP can similarly parallelise calculations across simulated consumers and markets,
but successive share-inversion iterations within each market depend on the preceding itera-
tion. The inversion step furthermore introduces simulation error to BLP estimation (Berry,
Linton, and Pakes, 2004), requiring additional work to address.
This confers it substantial computational advantages over alternative demand models
such as BLP. As such, it may be of interest particularly in applications where computational
complexity is a major bottleneck. We discuss these in the next section.
5 Applications
5.1 Welfare analysis
We can use the demand system estimated in the previous section to evaluate counter-
factual changes in consumer welfare. We consider a setting without income effects once
again, though doing so requires a minimal extension in the same line as the previous section.
Crucially, I will show how welfare analysis does not require us to interpret the simulated
consumer segments used in estimation as observed or separately identified objects. We ob-
25

serve only market-level prices, characteristics, and quantities, and care only about aggregate
consumer welfare.
From before:
q(p, X) =M−1(X)(Xβ−p) +κ(p, X)(72)
whereκ(p, X)is the aggregate correction generated by segment-level corner solutions.
The discrete-choice microfoundation gives this demand system a corresponding surplus rep-
resentation. For a simulated orderingrand preference drawℓ, let:
vrℓ(p, X) =Xβrℓ −pM r(X) =

M −1 r (X) −1 (73)
Note that it follows from (51) and the later derivations in Section 4.3 thatM−1 r is a
function ofλ πr, which we can keep track of by writingMr =λ πr fMr.
The inversion required to obtainMr is made computationally parsimonious through the
low-dimensional approach usingXexpounded in Lemma 1. The expected surplus associated
with this draw is:
Vrℓ(p, X) = max z≥0,1 ′z≤1

vrℓ(p, X)′z− λπr
2 z′ fMr(X)z

(74)
Themaximiserisexactlythechoice-probabilityvectorz rℓ(p, X)obtainedfromtheKarush-
Kuhn-Tucker problem used to construct the corner correction in the previous section. Under
these conditions, note thatVrℓ(p, X) = 1 λπr eVrℓ(p, X), foreVrℓ(p, X)independent of the per- mutation weight.
Aggregate consumer surplus is then approximately:
W(p, X) = 1 S
RX
r=1
λπr
SX
ℓ=1
Vrℓ(p, X) =1 S
RX
r=1
SX
ℓ=1
Vrℓ(p, X)(75)
which confirms the independence from permutation weights as above.
For the sake of example, consider a price counterfactual. By the envelope theorem:
∇pVrℓ(p, X) =−zrℓ(p, X)⇒ ∇ pW(p, X) =−q(p, X)(76)
Consequently, for a change fromp0 top 1, holdingXfixed, we obtain:
∆Wp =−
Z 1
0
q

p0 +s∆p, X ′ ∆pds∆p≡p 1 −p 0 (77)
Notably, this is independent of anything segment-specific. The discrete-choice micro-
foundation guarantees that this line integral is a difference in surplus rather than a path-
dependent area under an arbitrary system of demands. Substituting the estimated demand
decomposition yields:
∆Wp =−

M −1(X)(Xβ−p 0) ′ ∆p+ 1 2 ∆p′M −1(X)∆p− Z 1 0 κ(p0 +s∆p, X)′∆pds(78)
26

The estimated structural model suppliesκ(p, X)at each point along the path, so the
remaining integral can be evaluated numerically.
Let us consider another counterfactual, changes in product characteristics. This requires
slightly more structure; in general, it cannot be welfare-valued from aggregate quantities
alone. HoldingM r fixed, a characteristic change has the draw-level envelope effect:
dVrℓ =z ′ rℓ dXβ rℓ.(79)
With heterogeneousβ rℓ:
1
S
RX
r=1
λπr
SX
ℓ=1
z′ rℓdXβ rℓ ̸=q ′dXβ(80)
Aggregate demand reveals how many consumers choose each product, but not which
characteristic coefficients are attached to those consumers. The substitution matrix itself
changes with characteristics, as permitted byMr(X).
Thankfully, this is precisely where the structural estimation in the preceding section
becomes useful. For a general counterfactual from(p0, X0)to(p 1, X1), we hold fixed the
underlying simulation draws(r, ℓ), including their preference coefficients, but recompute
Mr(X)and the associated corner set. Lastly, we calculate:
∆W= 1 S
RX
r=1
λπr
SX
ℓ=1

Vrℓ(p1, X1)−V rℓ(p0, X0)  (81)
This gives the model-implied welfare effect of both price and characteristic changes while
preserving the heterogeneity that was used to fit aggregate corner behaviour. It does not
require us to recover the true consumer segments themselves.
In conclusion, our estimated multi-product aggregate demand system can be used for
welfare analysis regardless of whether the relevant counterfactual remains in the interior or
crosses onto a case where one or more goods receive zero demand.
5.2 Multi-product pricing and cost pass-through
The model above can be combined with a model of firm behaviour to deliver optimal
prices, markups, and cost pass-through estimates. Consider differentiated-products Bertrand
competition. LetJ f be the set of products owned by firmf, letccollect constant marginal
costs, and define the ownership matrixΩ, withΩij = 1when productsiandjare owned by
the same firm and zero otherwise. Firmf’s variable profit is then:
πf (p) = (pf −c f )′qf (p, X)(82)
BecauseM −1 p,X is symmetric, the first-order conditions for all firms can be stacked as
follows:
q(p, X)−∆(p, X)(p−c) =0∆(p, X)≡Ω⊙M −1 p,X (83)
27

Thus, at any interior optimum:
p−c= ∆(p, X) −1q(p, X)⇒p f −c f ={M −1 p,X}−1 |Jf |×|Jf |qf (p, X),∀f(84)
Note that∆(p, X)isin most applications asparse matrix; despite the possibility ofhigher
dimensions for settings with many goods, this property minimises computational concerns.
The standard multi-product markup inversion remains available; the only difference is
that the relevant demand Jacobian is the corner-adjusted one. Marginal costs can be re-
covered from observed prices and quantities onceM−1 p,X is known, and equilibrium variable
profits satisfy:
πf =q ′ f {M −1 p,X}−1 |Jf |×|Jf |qf (85)
The unconstrained linear case is especially straightforward; it is well-known that optimal
multi-product prices are available in closed form. However, with corner solutions, a global
closed form is not available becauseM−1 p,X, and so∆(p, X), changes with prices. Instead,
optimal pricing requires solving the followingN-dimensional system:
M −1(Xβ−p) +κ(p, X)−∆(p, X)(p−c) =0(86)
What about cost pass-through? It is well-understood that linear demand usually in-
troduces significant restrictions on these. Conditional onXand ownership, unconstrained
demand has a constant Jacobian, with equilibrium cost pass-through independent of price
and cost levels: ∂p∗
∂c =

M −1 + ∆I−1 ∆I (87)
This inflexibility is undesirable; in the limiting case in which a single firm owns all
products,∆ I =M −1, we get:
∂p∗
∂c = 1 2 I(88)
Corner solutions relax precisely this restriction. Implicitly differentiating the firms’ first-
order conditions yields:
∂p
∂c =

M −1 p,X + ∆(p, X) + Ξ(p,c) −1 ∆(p, X)(89)
forΞ ·k(p,c)≡ ∂∆(p,X) ∂pk (p−c). Pass-through now depends on the prevailing price vector because a cost shock can move consumers towards or across segment-level corner boundaries,
changing the active demand Jacobian. The aggregate corner correctionκ(p, X)now deter-
mines how pass-through. With finitely many segment types, pass-through is locally constant
between corner boundaries and changes when a boundary is crossed; with sufficiently rich
heterogeneity, these changes are smoothed and pass-through varies continuously with prices.
The model consequently retains the tractability of linear demand where it is useful -
including a closed-form multi-product pricing benchmark - without imposing constant pass-
through globally. Corner solutions are not a panacea however; the resulting pass-through is
flexible, but not unrestricted. This is clearest in the single-product case:
dp
dc = M −1 p,X 2M −1 p,X −q ′′(p)(p−c) (90)
28

Without corners,q ′′(p) = 0and the familiar one-half pass-through obtains. With cor-
ner solutions, consumers progressively leave the market as price rises, soq′′(p)≥0: the
demand curve locally flattens as additional corners bind. Pass-through can therefore rise
above one half, can equal full pass-through, and may exceed one when curvature is suf-
ficiently strong, subject to the second-order condition. Thus, the model does not permit
an arbitrary pass-through parameter - for example, the single-product mechanism does not
generate pass-through anywhere between zero and one - but it removes the much stronger
restriction that pass-through must be constant at one half. As for the the multi-product case,
there are no comparable bounds: own- and cross-cost pass-through are jointly determined
byM −1 p,X, ownership, and by the way corner solutions change the demand Jacobian.
These results require no additional estimates. The multi-product pricing system there-
fore amounts to evaluating these estimated objects and solving theN-dimensional first-order
conditions. Cost pass-through additionally requires the local derivative ofM−1 p,X, but this is
the same demand curvature identified by our full demand specification with corner correc-
tions. No consumer-level data or separate supply-side demand estimation is required. Given
an ownership matrix and Bertrand conduct, marginal costs can themselves be recovered from
observed prices and quantities through the markup inversion above; additional supply-side
structure is needed only if one wishes to model marginal costs themselves or conduct cost
counterfactuals away from the observed equilibrium.
5.3 Merger analysis
The model developed in this paper offers an alternative framework for the simulation
of horizontal mergers between firms producing differentiated goods. Its main advantages
arise from three properties of the demand system: it can be estimated without requiring
the researcher to pre-specify a market size; it permits flexible substitution patterns across
products; and, through heterogeneous corner solutions, it allows substitution patterns and
demand curvature to change endogenously as prices adjust following a merger, including
enabling zero demand.
Consider a merger between two firms competing in prices. LetΩ 0 be the pre-merger
ownership matrix andΩ1 the post-merger matrix, with the merger changing the ownership
indicators for products that were previously controlled by separate firms. Assume initially
that product characteristics and marginal costs remain unchanged. The merger affects equi-
librium prices because the merged firm internalises substitution between products previously
owned by separate firms.
From Section 5.2, the pre-merger first-order conditions under differentiated-products
Bertrand competition are:
q(p0, X)−Ω⊙M −1 p,X(p0 −c 0) =q(p 0, X)−∆(p0, X; Ω0)(p0 −c 0) = 0(91)
Given the estimated demand system and observed pre-merger prices and quantities,
marginal costs can be recovered through the standard markup inversion:
c0 =p 0 −∆(p 0, X; Ω0)−1q(p0, X)(92)
29

The post-merger equilibrium can then be calculated by replacing the ownership matrix
while holding the estimated demand primitives fixed. Allowing also for possible merger-
specific marginal-cost efficiencies, represented byc1, post-merger prices satisfy:
M −1(Xβ−p 1) +κ(p 1, X)−∆(p1, X; Ω1)(p1 −c 1) = 0(93)
When corner solutions are present, the problem requires solving the post-merger first-
order conditions while recomputing the aggregate corner correction and the associated de-
mand Jacobian at each candidate price vector. This is economically important. Under the
discrete-choice microfoundation developed here, price increases induce different consumer
segments to stop purchasing particular products, changing the set of alternatives between
which consumers substitute, and therefore changing the demand Jacobian. Price increases
need not be governed by the same local substitution patterns observed before the merger.
The second advantage, as mentioned earlier, concerns the treatment of the outside op-
tion. BLP estimation requires a measure of the total potential market size to construct
the outside-good share. This introduces a modelling choice that can affect the estimated
demand response to price changes. The approach proposed here instead lets the demand
system to be estimated directly using observed aggregate quantities. Substitution towards
the outside option is disciplined by the row sums of the estimated demand response matrix,
rather than by a separately constructed outside-good market share. The researcher therefore
does not need to specify a market size simply to normalise observed quantities into choice
probabilities. This property is particularly useful when the researcher observes only a subset
of the products available to consumers.
Furthermore, the model allows merger-induced changes in consumer and producer welfare
to be assessed using the same estimated demand system. For a merger that changes prices
fromp 0 top 1, holding product characteristics fixed, the change in aggregate consumer surplus
is:
∆W=−
Z 1
0
q

p0 +s(p 1 −p 0), X ′ (p1 −p 0)ds(94)
As established in Section 5.1, the discrete-choice microfoundation guarantees that this
expression corresponds to a difference in expected surplus and is independent of the integra-
tion path. The estimated corner correction enters the welfare calculation directly, allowing
the counterfactual to account for consumers who cease purchasing particular products as
prices rise.
5.4 Network theory
In this section, let us assume sufficiently rich preference heterogeneity to smooth the
segment-level kinks into continuously differentiable aggregate demand, and consider what
aggregate demand looks like for some specific types of unconstrained demand Jacobians. We
can lean on the network economics interpretation ofM−1 as approximately an adjacency
30

matrix, and consider some well-known network graphs. To do so, we will make use of tree-
distance matrices, where:
M=γ dT (i,j) (95)
ford T (i, j)the number of links on the unique path between nodesiandj, the nodes
being the goods in the market.
The most basic matrix is the complete graph:
dcomplete(i, j) = 1⇒M complete =


1γ· · · · · ·γ
γ1γ· · ·γ
...γ ... · · · · · ·
... ... ... ... ...
γ γ· · · · · ·1

 (96)
It is equivalent to the assumption that all goods are equally imperfect substitutes. An-
other common matrix is the Kac–Murdock–Szegö (KMS) matrix (Kac, Murdock, and Szegö,
1953), explored in some depth in Amir, Erickson, and Jin, (2017):
dKM S(i, j) =|i−j| ⇒M KM S=


1γ γ 2 · · ·γn−1
γ1γ· · ·γ n−2
γ2 γ1· · ·γ n−3
... ... ... ... ...
γn−1 γn−2 γn−3 · · ·1

 (97)
This matrix is equivalent to a line graph, a one dimensional ordering with equal distance
γat each segment of the line. The spokes graph, popularised in Chen and Riordan (2007)
and otherwise known as the star graph, can be defined as follows, for good 1 the center node
of the graph:
dspokes(i, j) =



0ifi=j
1ifi= 1, j̸= 1orj= 1, i̸= 1
2ifi, j̸= 1, i̸=j
⇒M spokes =


1γ γ· · ·γ
γ1γ 2 · · ·γ2
γ γ 2 1· · ·γ 2
... ... ... ... ...
γ γ 2 γ2 · · ·1


(98)
This is also known as a core-periphery graph, very popular in network economics. It can
be thought of as equivalent to a central good with a unique combination of characteristics, in
the product category surrounded by a periphery of goods, each relating to the central good
by some unique deviation along one particular characteristic.
The spider graph is a related graph that also introduces asymmetry across goods: a
central nodecwithkarms of potentially different lengthsℓ 1, . . . , ℓk. By labeling each non-
central node by(a, r), whereaidentifies its arm andrits distance from the center, we
31

obtain:
dspider(c, c) = 0
dspider(c,(a, r)) =r
dspider((a, r),(b, s)) =
(
|r−s|ifa=b
r+sifa̸=b
⇒e.g. Mspider =


1γ γ 2 γ3 γ3 γ4
γ1γ γ 2 γ2 γ3
γ2 γ1γ γ γ 2
γ3 γ2 γ1γ 2 γ
γ3 γ2 γ γ 2 1γ 3
γ4 γ3 γ2 γ γ 3 1


(99)
The example codified inMspider is one such setting with 6 goods and links(1,2),(2,3),
(3,4),(3,5), and(4,6), yielding a central node at 3 and three arms of lengths 2, 2, and 1.
The central good (in this case 3) has three direct competitors, while goods 2 and 4 have two
each and goods 1, 5, and 6 have only one. Such asymmetries are common in reality, making
this a graph of particular interest.
Lastly, we consider the bridge graph, which is useful to express product categories with
clusters of goods in greater competition within-cluster than between clusters (e.g. bio vs
non-bio products, open- vs closed-source software). LetLandRbe the sets of nodes on the
left and right of the graph respectively. letcL ∈Landc R ∈Rbe the centers of each side.
Defining the depth of each node ash(i), equal to 0 ifi∈ {cL, cR}, equal to 1 if not, we get
the following distance function:
dbridge(i, j) =



0ifi=j
h(i) +h(j)ifi̸=h, i, j∈Lori, j∈R
1 +h(i) +h(j)ifi∈L, j∈R,or vice-versa
⇒e.g. Mbridge =


1γ γ γ γ 2 γ2
γ1γ 2 γ2 γ3 γ3
γ γ 2 1γ 2 γ3 γ3
γ γ 2 γ2 1γ γ
γ2 γ3 γ3 γ1γ 2
γ2 γ3 γ3 γ γ 2 1

 (100)
The example codified inMbridge is just one such setting with 6 goods,L={1,2,3}and
R={4,5,6}, with centers at nodes 1 and 4, and links(1,2),(1,3),(1,4),(4,5), and(4,6).
Tree-distance matrices can be inverted using the following formula:
M −1 T = 1 1−γ 2 [diag(1 + (deg(i)−1)γ 2)−γG t](101)
forG t the implied binary adjacency matrix of each graph, equal to 1 where two nodes
share a link and zero otherwise, anddeg(i)the number of links of a given nodei.
For this section, we will work with 6 goods, which implies6! = 720possible permuta-
tions and2 6 = 64possibleC. We setδ= 1as theλ π weights cancel out once we consider
every possible permutation. We setX=I(as many goods as product characteristics) and
32

obtain thex ′ jβh =β hjs across all permutations by drawing from a Uniform distribution
U[0.05,0.15]. We will focus on good 1’s aggregate demand function, keeping all other goods’
prices fixed atp2 =. . .=p6 = 0.05while varyingp 1. We will setγat three different points:
0.1,0.15,and0.24- higherγraise issues for satisfying the conditions in (17) across some of
the networks.
One important concern is that the presence of zeroes in some of the unconstrained de-
mand Jacobians implied by the networks above. These effectively block certain permutations
from existing: ifM −1 ij = 0, then no permutation can haveiandjadjacent, as it would im-
ply a positive weight for that permutations’M −1 P and therefore a positive weight for the
aggregateM −1. To address this, any permutation which implies a forbidden adjacency is
truncated, with all products with a higher|α|than that of the good with the lowest|α|of
the pair being removed from that permutation. This simulates that permutation’s choice
set.11
The results for each network and good 1 are below:
Figure 2:Economic networks and respective aggregate demand graphs for good 1
Aggregate demand is stated as market shares as we do not specify market size; the use of
permutation weights, which sum up to 1, substitutes for consumer segment weights, which
sum up toHand are generally unobserved (asHitself is).
Our model can thus provide theoretical researchers with a way to study variations in
market structure with the tools of network theory within a rationalisable model. A strand of
the network literature studying welfare-maximising market interventions (Galeotti, Golub,
and Goyal, 2020) appears particularly promising for integration. However, the conditions of
11An alternative approach to addressing zeros could be to remove any contradicting permutations outright.
Except for the complete network and the KMS line, all orderings have forbidden inside-good adjacencies
across the other networks. Using our truncation approach, each network, respectively, has 720, 34, 30, 36,
and 36 distinct retained paths.
33

gross substitution imposed by discrete choice appear to rule out some applications (Galeotti,
Golub, Goyal, Talamàs, and Tamuz, 2026).
5.5 Models of entry and exit
Market structure - i.e. the number of firms, their sizes, the products they offer in a given
market - and how it ties to market competition is of great interest to IO economists. Many
high-quality surveys of this literature exist since at least Bresnahan (1989) (and Berry and
Reiss, 2007, more recently), with surveys of stylised facts on entry available since at least
Geroski (1995). In the 1990s and early 2000s, several papers on static models of market
entry and oligopolistic competition tackled well-known issues with multiplicity of equilibria
in simultaneous entry, such as Bresnahan and Reiss (1990, 1991), Berry (1992), Seim (2006),
and Ciliberto and Tamer (2009).
In the 2010s and 2020s, empirical models ofmulti-stage portfolioentry and exit under
multi-productoligopoly, with the clearest potential for policy and economic research, are the
newer development: Eizenberg (2014), Wollmann (2018), Fan and Yang (2025), and Mon-
tag (2026) most recently. These papers attempt to endogenise what goods and respective
characteristics are introduced by firms onto specific markets, addressing issues related to
combinatorial computational complexity. Combinatorial complexity follows from entry-no
entry decisions across every possible combination of product characteristics.
A fully dynamic game with a fully-specified endogenous product design stage has faced
a key bottleneck: a reliance on BLP demand estimation12. Akchen and Misic (2026) find
exact Logit-based product design to be NP-hard, with design instead tackled in Operations
Research and Marketing literatures via heuristics and near optimality. In IO, not only does
this prevent extensions from multi-stage to dynamic models of firm behaviour, it severely
restricts separate identification of concepts of interest, such as endogenous sunk versus fixed
fixed costs. The computational complexity of BLP also implies strong restrictions on the
number of products one can analyse.
The present paper introduces an alternative discrete-choice-based demand system that
alleviates these computational constraints. In particular, the characteristics-based represen-
tation of the demand matrix in Lemma 1 allows the number of demand parameters to grow
with the number of observed characteristics rather than with the number of products.
Rodrigues (2026) exploits this structure to develop a dynamic model of endogenous prod-
uct design, entry, and pricing under multi-product oligopoly. The computational gains are
substantial whether non-negativity constraints are or not slack. The representation reduces
the inversion of the demand matrix to operations on a matrix whose dimension depends
only on the number of characteristics, avoiding repeated inversion of large product-level
matrices as the choice set changes. Conditional on product characteristics and market struc-
ture, Bertrand equilibrium prices and quantities can be obtained through linear algebra
12Aguirregabiria and Ho (2012) and Rossi (2023) are important exceptions.
34

rather than repeatedly solving non-linear pricing problems. These gains are particularly
consequential in a dynamic setting, where firms must evaluate equilibrium profits and con-
tinuation values across numerous candidate designs, entry configurations, and future market
states. Moreover, continuous characteristics can be optimised conditional on discrete design
choices, considerably reducing the combinatorial burden associated with searching over pos-
sible product configurations. While the enumeration of simultaneous entry outcomes and
the calculation of continuation values remain computationally demanding, the simplification
of the underlying demand and pricing problems makes each branch of the dynamic game
substantially less costly to evaluate.
5.6 Durable goods
The durable goods literature provides another natural application for aggregate linear
demand. Durable goods introduce an inherently dynamic dimension to competition: cur-
rent sales affect the stock of goods available in future periods, while consumers’ expectations
about future prices, product quality, and resale values influence current purchasing decisions.
The use of linear demand in this literature is not new. Bulow (1982), for example, relies
on linear demand to study how the inability of durable-goods monopolists to commit to
future production can distort output, investment, and product durability. The challenge has
instead been to reconcile the tractability of these theoretical models with the heterogeneous
preferences and product differentiation required for empirical analysis.
A substantial empirical literature has developed dynamic models of durable-goods mar-
kets (see e.g. Esteban and Shum, 2007; Chen, Esteban, and Shum, 2013; Gowrisankaran
and Rysman, 2012; Gavazza and Lanteri, 2021). Much like with dynamic entry models, a
significant difficulty in extending these models is computational complexity. Studying dy-
namic firm behaviour requires incorporating changes in installed stocks, demand for product
replacements, and implications for prices of new and used goods sold by the firm, as well
as those sold by competitors. Interactions must be evaluated repeatedly across different
states, candidate action profiles, and counterfactual equilibria. The computational gains
from the full model presented in this paper could therefore facilitate richer dynamic mod-
els of multi-product competition, endogenous durability, replacement, and secondary-market
equilibrium.
5.7 Retail and large choice sets
Retail markets provide a particularly demanding setting for structural demand estima-
tion. A supermarket or online retailer may offer hundreds or thousands of differentiated
products. At the same time, the most accessible data often consist of market-level data,
rather than the choices and complete shopping baskets of individual households over time.
The demand model developed here has two especially useful theoretical properties in this
setting: estimating the demand for the goods of interest does not require the researcher to
construct an outside-option share, and the system can be treated as an incomplete demand
system.
35

In conventional discrete-choice applications such as BLP, the researcher typically con-
verts observed sales into shares using a measure of potential market size. ForHt one such
measure, the outside share is computed ass0t = 1− PNt j=1 qjt/Ht. It is often unclear what
counts asH t. Mismeasurement affects estimated price sensitivity, diversion ratios, markups,
pass-through, and welfare counterfactuals (Nevo, 2000; Huang and Rojas, 2014). How this
measure is calculated is at the discretion of the researcher, which can raise disputes in real-
world merger cases (see e.g. Baker, 2007). In contrast, the demand equation in (39) directly
relates the quantities of observed inside goods to their prices and characteristics. Estimation
does not require assigning a quantity to non-purchase or constructings0t as an additional de-
pendent variable. The inside-good response matrix already disciplines substitution towards
that alternative through (15).
The second theoretical property is closely related. Incomplete demand systems can spec-
ify demands for a subset of all consumption goods without modelling the entire allocation of
the consumer’s budget (Epstein, 1982; LaFrance, 1985). In the present model, purchases of
the inside products are evaluated against utility from residual income, and I have shown ear-
lier how locally differing marginal utilities before and after purchase allow for income effects
without abandoning the linear interior demand structure. The remaining consumption bun-
dle need not be decomposed into a set of priced products and separately estimated demand
equations. This is particularly appealing for retail applications: a researcher interested in
the price of breakfast cereals should not necessarily have to specify the joint demands for
everything else purchased. Current practice sidesteps this entirely, obscuring considerations
such as product-specific cross-category effects. Here aggregate linear demand can provide
not just potential computational advantages, but enable heterogeneous choice sets across the
consumer population, and the building of more robust measures of product substitution and
market structure.
Furthermore, the model can be extended to the case where retail transactions involve
multi-unit, multi-product, cross-category purchases in a single transaction. LetAbe an
N×number of unique baskets product–basket incidence matrix, where each column spec-
ifies the quantities of individual products contained in a feasible basket. Consumers now
choose among baskets rather than individual products, with basket pricesA ′p. Apply-
ing the same discrete-choice construction at the basket level yields interior basket demand
z(p) =M −1 B (XBβ−A ′p), implying aggregate product demand and its Jacobian:
q(p) =Az(p) ∂q ∂p =−AM −1 B A′ (102)
Although baskets are substitutes as choice alternatives, individual products may exhibit
complementarities through joint purchases. This is one way to maintain the rationalisability
conditions imposed by our discrete-choice microfoundation while introducing complementar-
ities of use in cases such as Galeotti, Golub, Goyal, Talamàs, and Tamuz (2026). Corner
corrections can likewise be applied at the basket level before aggregation into product de-
mand.
Computational tractability would naturally depend on a parsimonious representation
36

of the feasible basket set. On this, Rodrigues (2025) provides a complementary route to
aggregate linear demand for these types of decisions via continuous choice. In that setting
corner correction is also far more computationally tractable, though it does not identify the
distribution of heterogeneous preferences.
5.8 Economics of platforms
The economics of platforms and two-sided markets literature often relies on linear de-
mand systems derived from individual discrete choice to characterise equilibrium prices and
study externalities. However, the tractability of these models often depends on full market
coverage, where all consumers participate in one of the available platforms. This assumption
rules out market expansion: changes in prices reallocate a fixed population across platforms
without affecting the total number of participants. Since consumers’ decisions to participate
in one side of the market affect the attractiveness of platforms to the other side, full cover-
age is especially problematic for a fuller understanding of the interplay between market size,
network effects, and equilibrium prices. Recent contributions continue to face this difficulty,
even when analysing alternative demand systems (Peitz and Sato, 2026).
The present paper explicitly incorporates an outside option, allowing changes in prices
and product characteristics to affect both substitution between platforms and total mar-
ket participation. When a platform becomes sufficiently unattractive that some consumer
segments exit, the corner correction developed above adjusts the unconstrained demand Ja-
cobian to account for the resulting changes in substitution, including movements towards
the outside option itself.
6 References
Aguirregabiria, V., & Ho, C.-Y. (2012). A dynamic oligopoly game of the US airline industry:
Estimation and policy experiments. Journal of Econometrics, 168(1), 156–173.
Akchen, İ., & Mišić, V. (2026). Exact logit-based product design. Management Science.
Amir, R., Erickson, P., & Jin, J. (2017). On the microeconomic foundations of linear demand
for differentiated products. Journal of Economic Theory, 169, 641–665.
Anderson, S., de Palma, A., & Thisse, J.-F. (1989). Demand for differentiated products, discrete
choice models, and the characteristics approach. The Review of Economic Studies, 56(1), 21–35.
Armstrong, M., & Vickers, J. (2015). Which demand systems can be generated by discrete
choice? Journal of Economic Theory, 158, 293–307.
Baker, J. (2007). Market definition: An analytical overview. Antitrust Law Journal, 74(1),
129–173.
37

Berry, S. (1992). Estimation of a model of entry in the airline industry. Econometrica, 60(4),
889–917.
Berry, S., Levinsohn, J., & Pakes, A. (1995). Automobile prices in market equilibrium. Econo-
metrica, 63(4), 841–890.
Berry, S., Levinsohn, J., & Pakes, A. (2004). Differentiated products demand systems from a
combination of micro and macro data: The new car market. Journal of Political Economy, 112(1),
68–105.
Berry, S., Linton, O., & Pakes, A. (2004). Limit theorems for estimating the parameters of
differentiated product demand systems. The Review of Economic Studies, 71(3), 613–654.
Berry, S., & Reiss, P. (2007). Empirical models of entry and market structure. In M. Armstrong
& R. Porter (Eds.), Handbook of industrial organization (Vol. 3, pp. 1845–1886). Elsevier.
Blackwell, D., & MacQueen, J. (1973). Ferguson distributions via Pólya urn schemes. The
Annals of Statistics, 1(2), 353–355.
Bonnet, O., Galichon, A., Hsieh, Y.-W., O’Hara, K., & Shum, M. (2022). Yogurts choose con-
sumers? Estimation of random-utility models via two-sided matching. The Review of Economic
Studies, 89(6), 3085–3114.
Bos, I., & Vermeulen, D. (2022). On the microfoundation of linear oligopoly demand. The B.E.
Journal of Theoretical Economics, 22(1), 1–15.
Bresnahan, T. (1989). Empirical studies of industries with market power. In R. Schmalensee &
R. Willig (Eds.), Handbook of industrial organization (Vol. 2, pp. 1011–1057). Elsevier.
Bresnahan, T., & Reiss, P. (1990). Entry in monopoly market. The Review of Economic Stud-
ies, 57(4), 531–553.
Bresnahan, T., & Reiss, C. (1991). Entry and competition in concentrated markets. Journal of
Political Economy, 99(5), 977–1009.
Bulow, J. (1982). Durable-goods monopolists. Journal of Political Economy, 90(2), 314–332.
Chen, J., Esteban, S., & Shum, M. (2013). When do secondary markets harm firms? American
Economic Review, 103(7), 2911–2934.
Chen, Y., & Riordan, M. (2007). Price and variety in the spokes model. The Economic Journal,
117(522), 897–921.
Choné, P., & Linnemer, L. (2020). Linear demand systems for differentiated goods: Overview
and user’s guide. International Journal of Industrial Organization, 73, Article 102663.
Ciliberto, F., & Tamer, E. (2009). Market structure and multiple equilibria in airline markets.
38

Econometrica, 77(6), 1791–1828.
Daly, A., & Zachary, S. (1978). Improved multiple choice models. In D. Hensher & M. Dalvi
(Eds.), Determinants of travel choice (pp. 321–362). Saxon House.
Eizenberg, A. (2014). Upstream innovation and product variety in the U.S. home PC market.
The Review of Economic Studies, 81(3), 1003–1045.
Epstein, L. (1982). Integrability of incomplete systems of demand functions. The Review of
Economic Studies, 49(3), 411–425.
Esteban, S., & Shum, M. (2007). Durable-goods oligopoly with secondary markets: The case of
automobiles. The RAND Journal of Economics, 38(2), 332–354.
Fan, Y., & Yang, C. (2025). Estimating discrete games with many firms and many decisions:
An application to merger and product variety. Journal of Political Economy, 133(6), 1886–1931.
Fosgerau, M., Melo, E., de Palma, A., & Shum, M. (2020). Discrete choice and rational inat-
tention: A general equivalence result. International Economic Review, 61(4), 1569–1589.
Galeotti, A., Golub, B., & Goyal, S. (2020). Targeting interventions in networks. Econometrica,
88(6), 2445–2471.
Galeotti, A., Golub, B., Goyal, S., Talamàs, E., & Tamuz, O. (2026). Robust market interven-
tions. Journal of Political Economy.
Galichon, A., & Salanié, B. (2022). Cupid’s invisible hand: Social surplus and identification in
matching models. The Review of Economic Studies, 89(5), 2600–2629.
Gandhi, A., & Nevo, A. (2021). Empirical models of demand and supply in differentiated prod-
ucts industries. In K. Ho, A. Hortaçsu, & A. Lizzeri (Eds.), Handbook of industrial organization
(Vol. 4, pp. 63–139). Elsevier.
Gavazza, A., & Lanteri, A. (2021). Credit shocks and equilibrium dynamics in consumer durable
goods markets. The Review of Economic Studies, 88(6), 2935–2969.
Geroski, P. (1995). What do we know about entry? International Journal of Industrial Organi-
zation, 13(4), 421–440.
Gowrisankaran, G., & Rysman, M. (2012). Dynamics of consumer demand for new durable
goods. Journal of Political Economy, 120(6), 1173–1219.
Grieco, P., Murry, C., & Yurukoglu, A. (2024). The evolution of market power in the U.S.
automobile industry. The Quarterly Journal of Economics, 139(2), 1201–1253.
Hofbauer, J., & Sandholm, W. (2002). On the global convergence of stochastic fictitious play.
Econometrica, 70(6), 2265–2294.
39

Hotelling, H. (1929). Stability in competition. The Economic Journal, 39(153), 41–57.
Huang, D., & Rojas, C. (2014). Eliminating the outside good bias in logit models of demand
with aggregate data. Review of Marketing Science, 12(1), 1–36.
Jaffe, S., & Weyl, E. (2010). Linear demand systems are inconsistent with discrete choice. The
B.E. Journal of Theoretical Economics, 10(1).
Kac, M., Murdock, W., & Szegő, G. (1953). On the eigen-values of certain Hermitian forms.
Journal of Rational Mechanics and Analysis, 2, 767–800.
LaFrance, J. (1985). Linear demand functions in theory and practice. Journal of Economic
Theory, 37(1), 147–166.
McFadden, D. (1974). Conditional logit analysis of qualitative choice behavior. In P. Zarembka
(Ed.), Frontiers in econometrics (pp. 105–142). Academic Press.
McFadden, D.(1978). Modellingthechoiceofresidentiallocation. InA.Karlqvist, L.Lundqvist,
F.Snickars, &J.Weibull(Eds.), Spatialinteractiontheoryandplanningmodels(pp. 75–96). North-
Holland.
McFadden, D., & Train, K. (2000). Mixed MNL models for discrete response. Journal of Ap-
plied Econometrics, 15(5), 447–470.
Melitz, M., & Ottaviano, G. (2008). Market size, trade, and productivity. The Review of Eco-
nomic Studies, 75(1), 295–316.
Montag, F. (2026). Mergers, foreign competition, and jobs: Evidence from the US appliance
industry. American Economic Review, 116(6), 2085–2119.
Nevo, A. (2000). A practitioner’s guide to estimation of random-coefficients logit models of
demand. Journal of Economics & Management Strategy, 9(4), 513–548.
Peitz, M., & Sato, S. (2026). Asymmetric platform oligopoly. The RAND Journal of Economics,
57(1), 60–77.
Pellegrino, B. (2025). Product differentiation and oligopoly: A network approach. American
Economic Review, 115(4), 1170–1225.
Pinkse, J., Slade, M., & Brett, C. (2002). Spatial price competition: A semiparametric ap-
proach. Econometrica, 70(3), 1111–1153.
Rockafellar, R. (1970). Convex analysis. Princeton University Press.
Rodrigues, A.(2025). Consumerchoiceovershoppingbaskets[Preprint]. arXiv. https://arxiv.org/abs/2511.11846
40

Rodrigues, A.(2026). Endogenousproductdesign[Preprint]. arXiv. https://arxiv.org/abs/2602.02833
Rossi, F. (2023). Mergers with endogenous product choice: The case of the ready-to-eat cereal
industry. Quantitative Marketing and Economics, 21(1), 1–64.
Salop, S. (1979). Monopolistic competition with outside goods. The Bell Journal of Economics,
10(1), 141–156.
Seim, K. (2006). An empirical model of firm entry with endogenous product-type choices. The
RAND Journal of Economics, 37(3), 619–640.
Thomassen, Ø., Smith, H., Seiler, S., & Schiraldi, P. (2017). Multi-category competition and
market power: A model of supermarket pricing. American Economic Review, 107(8), 2308–2351.
Tirole, J. (1988). The theory of industrial organization. MIT Press.
Wollmann, T. (2018). Trucks without bailouts: Equilibrium product characteristics for com-
mercial vehicles. American Economic Review, 108(6), 1364–1406.
41

A Appendix
A.1 Proofs
Proposition 1.Fix a consumer segmenthand a matrix of product characteristicsX. Assume
that:
EFh[max i∈N |εi| |X,ξh]<∞,(103)
thatF h(ε|X,ξ h)is non-atomic, and that ties occur with probability zero. Define the segment’s
surplus function:
Vh(v, X,ξh) =
Z
max
i∈N
vi +ε i dFh(ε|X,ξ h),(104)
wherev 0 = 0. Then:
Vh(v, X,ξh) = sup
AiN i=0
{
NX
i=0
Z
Ai
(vi +ε i)dF h(ε|X,ξ h)}
= sup
z:PN i=1 zi≤1,,zi≥0∀i=1,...,N sup AiN i=0∈Ph(z) {
NX
i=0
viFh(Ai |X,ξ h) +
NX
i=0
Z
Ai
εi dFh(ε|X,ξ h)}
= sup
z:PN i=1 zi≤1,,zi≥0∀i=1,...,N {v′z+ sup AiN i=0∈Ph(z) [
NX
i=0
Z
Ai
εi dFh(ε|X,ξ h)]}
= sup
z:PN i=1 zi≤1,,zi≥0∀i=1,...,N {v′z+Z h(z, X,ξh)}
= max
z:PN i=1 zi≤1,,zi≥0∀i=1,...,N {v′z+Z h(z, X,ξh)}.
(105)
The first equality follows because the pointwise utility-maximising regions:
A∗ i (v) ={ε:v i +ε i > vj +ε j,∀j̸=i}(106)
attain the supremum over partitions. Since ties occur with probability zero, these regions form
a partition up to a set of measure zero and satisfy:
Fh(A∗ i (v)|X,ξ h) =zhi(v, X).(107)
Under the maintained assumptions, the Williams-Daly-Zachary theorem (McFadden, 1978) im-
plies:
∇vVh(v, X,ξh) =zh(v, X).(108)
By convex duality, the set of maximisers is the subdifferential ofVh atv. SinceV h is differen-
tiable:
∂vVh(v, X,ξh) =zh(v, X)(109)
Therefore, we can conclude:
zh(v, X) = arg max
z:PN i=1 zi≤1,,zi≥0∀i=1,...,N {v′z+Z h(z, X,ξh)}.(110)
42

□
Proposition 3.For an individual consumer, the Slutsky equation for a price increase can be
written, in matrix notation:
DpdM hr =D + p dH hr −(D ydM hr)dM ′ hr (111)
ford hr theN×1vector of individual choice indicators, with at most one non-zero element
on thei ∗ r-th row;D + p the right-hand compensated price derivative; and superscripts referring to
Marshallian and Hicksian terms. Sincedhr is discrete, these are not ordinary pointwise derivatives;
they are zero away from indifference boundaries and undefined at the boundary. The equation above
should therefore be understood in terms of boundary changes evaluated at the pre-change choice.
By taking expectations on these boundary contributions overF(ε), we can however obtain ordinary
derivatives of segment-hchoice probabilities:
DpzM h =D pzH hr| {z }
substitution effect
−E[(D ydM hr)dM ′ hr |h]| {z }
income effect
(112)
Notice thatz h cannot be obtained separately in the income effect term, which explains its
absence in (35). Let us characteriseE[(DydM hr)dM ′ hr |h]. From (11), we obtain, foryh =E[y hr|h]:
E
 ∂dM hri
∂yhr
|h

= ∂zhi
∂yhr
= ∂zhi
∂yh
∂yh
∂yhr
= ∂zhi
∂yh
= (λ1 h −λ 0 h)(M −1 h 1)i (113)
with
E
 ∂dM hri
∂yhr
dM hrj |h

=
(
(λ1 h −λ 0 h)(M −1 h 1)i ifi=j
0otherwise (114)
In matrix form:
E
h
(DydM hr)dM ′ hr |h i = (λ1 h −λ 0 h)·diag(M −1 h 1)(115)
Substituting into the segment-level Slutsky equation gets us the compensated response to a
marginal increaseD pzH h , our substitution effect:
DpzM h =D + p zH h −E[(D ydM hr)dM ′ hr |h]
⇔D pzM h =D + p zH h −(λ 1 h −λ 0 h)·diag(M −1 h 1)
⇔ −λ1 hM −1 h =D + p zH h −(λ 1 h −λ 0 h)·diag(M −1 h 1)
⇔D + p zH h =−λ 1 hM −1 h + (λ1 h −λ 0 h)·diag(M −1 h 1)
(116)
Aggregating across segments yields (35). This completes the proof.□
Proposition 3.Since0⪯M −1 Ch ⪯M −1 h , the segment-level price responses, including across changes in the binding constraints, are bounded in norm:
X
h
µh||M −1 h || ≤ X
h
µhtr(M −1 h ) = tr(M−1)<∞(117)
The last inequality follows fromM−1 being a well-defined finite matrix.
Now consider any sequence of pricespn →p. As per the proposition statement, at any given
43

prices, almost every segment is sufficiently far from a change in its binding constraints. In other
words, for almost every segmenth, sufficiently small price changes do not alterCh, such that:
M −1 Ch(pn,X) − →M−1 Ch(p,X) (118)
Since these matrices are bounded away from infinity. By the dominated convergence theorem,
where we may interchange a limit and an integral provided the quantities inside the integral are
bounded by an integrable function, we have the necessary conditions to differentiate under aggre-
gation:
lim
n→∞
Dpq(pn, X) =−
X
h
µh lim n→∞ M −1 Ch(pn,X) =D pq(p, X)(119)
Thus, the aggregate demand Jacobian is continuous.□
44
