---
title: On the Optimality of Mental Accounting
url: https://arxiv.org/abs/2610.12587
category: consumer-behavior
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Jarrod Burgh
- Emerson Melo
- Matthew Shum
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.12587
pages: 23
chars: 58864
fetched_at: '2026-11-08T13:16:53+00:00'
kb_version: 1
---

# On the Optimality of Mental Accounting

On the Optimality of Mental Accounting
Jarrod Burgh
Grinnell
Emerson Melo
Indiana
Matthew Shum
Caltech, Amazon
October 12, 2026
Abstract
Mental accounting is usually explained by self-control, and two-stage budgeting by separable
preferences. In this paper, we propose a third explanation based on sellers’ market power.
A consumer who commits to spend a fixed number of dollars in a category has unit-elastic
demand, so a seller in that category gains nothing by restricting quantity. A consumer who
instead targets a fixed physical quantity has perfectly inelastic demand, a case that a monopolist
can exploit. We characterize the commitments that remove a seller’s incentive to mark up
prices, and show that the fixed dollar budget is the least restrictive. We then show that what
matters is budget rigidity rather than separability of preferences. A consumer who re-optimizes
her category budget when prices change is insulated from market power only if categories are
substitutes; a rigid budget insulates her in every case. Mental accounting can therefore be
read as a commitment device against markups, a rationale that is separate from the self-control
motive in the existing literature.
1 Introduction
Consumers often divide their spending into category budgets and treat those budgets as binding.
They decline to move money from the “dining out” envelope to the “electronics” envelope even
when doing so would make them better off.
Two strands of literature explain this behavior. The first, due to Thaler [1985] and developed
in Shefrin and Thaler [1988] and Thaler [1999], treats mental accounts as a bookkeeping device
that helps with self-control. The second, following Gorman [1959] and Deaton and Muellbauer
[1980], shows that weakly separable preferences let the consumer’s problem be solved in two stages:
allocate income across groups, then optimize within each group given that group’s budget.
Both literatures focus on what mental accounts do to the consumer’s cognition or preferences.
We ask a different question:what does a dollar budget do to the market the consumer faces?
The answer turns on the shape of demand that a commitment produces. A seller facing a
buyer with a fixed dollar budget cannot profit from restricting supply. In this scenario, the buyer’s
demand is unit-elastic, so her total spending does not vary with price. On the other hand, a seller
facing a buyer with a fixed physical-quantity target faces perfectly inelastic demand and profits by
1
arXiv:2610.12587v1  [econ.GN]  8 Oct 2026

raising the price to the buyer’s reservation value. The form of the commitment, dollars or units,
determines whether the seller has any power over the buyer.
We develop this observation in six results. We first characterize the full class of spending
commitments that leave a seller with no profitable markup: a commitment has this property—we
call itmarkup-proof—if and only if the buyer’s expenditure is nonincreasing in price, equivalently
if and only if her demand is everywhere weakly elastic (Proposition 1). Furthermore, among all
markup-proof commitments, the fixed dollar budget is the least restrictive, delivering weakly more
consumption at every price than any alternative with the same property (Proposition 2). This
characterization is the budget-commitment counterpart of the buyer-optimal demand of Condorelli
and Szentes [2020], in which a buyer who chooses her value distribution also ends up with unit-
elastic demand; what is new here is that the commitment takes the form of a dollar budget inside a
multi-category consumer problem. What insulates the consumer from market power is the rigidity
of the budget rather than separability of preferences: a consumer who re-optimizes her group
expenditure as prices change is markup-proof only when groups are substitutes, which under a
CES upper stage means an elasticity of substitution of at least one; when groups are complements,
her expenditure on a groupriseswith its price and the seller’s revenue rises toward her entire
income (Proposition 3). When the commitment is endogenous, the consumer prefers to budget
when the markup she avoids exceeds the value of the flexibility she gives up (Proposition 4), and
this incentive is strongest where competition is weakest, disappearing as the category becomes
competitive (Proposition 6). The same incentive combines additively with a cost of tracking prices:
a consumer who finds attention costly needs less market power to justify committing, and vice
versa (Proposition 5).
Taken together, these results give a market-structure rationale for mental accounting and two-
stage budgeting. Committing to a category-level dollar budget turns a consumer who would present
quantity-target demand, which a seller can mark up, into one who presents unit-elastic demand,
which a seller cannot. The argument requires no self-control problem and no present bias. It applies
to a fully patient, dynamically consistent consumer.
The paper proceeds as follows. Section 2 presents the pricing mechanism, characterizes markup-
proof commitments, and reinterprets mental accounting. Section 3 builds on the Gorman–Deaton
foundation and shows that rigidity, rather than separability, confers markup-proofness. Section 4
makes the budget choice endogenous, derives a comparative statics result on market concentration,
and shows how a cost of attention interacts with market power in the decision to commit. Section 5
discusses the literature, and Section 6 concludes. Proofs are in Appendix A; supporting derivations,
including extensions to many buyers and qualifications on when budgeting fails, are in Appendix B.
2 Budget commitment versus quantity commitment
Consider a seller of a good with zero marginal cost and fixed supplys >0, facing a single buyer
with a constant per-unit valuev.
2

A budget-capped buyer.Suppose the buyer has a fixed dollar budgetbto spend in this market.
She buys as many units as her budget allows wheneverp≤v, so her demand is
q(p) = b p ,
a rectangular hyperbola with elasticityε(p) = 1 at everyp≤v. Revenue isp q(p) =b, which does
not vary with price. The seller never prices below the market-clearing pricep c =b/s, and earns
the same revenue at every price in [p c, v]. Restricting quantity below supply yields him no gain.
A quantity-capped buyer.Suppose instead the buyer wants a fixed quantitySand has reser-
vation valuec. Her demand is the step function
q(p) =S·1{p < c},
soε(p) = 0 forp < c. Revenuep Srises linearly with price up toc, so the seller raises the price to
the buyer’s reservation value.
2.1 Which commitments are markup-proof
Both cases are instances of a more general principle. Let the buyercommitto aspending rule: a
nonincreasing demand functionq:R + →R + withq(p) = 0 forp > v, describing what she buys at
each posted price. Writee(p) =p q(p) for her expenditure andp c(s) = min{p:q(p)≤s}for the
price that clears supplys. The seller posts a pricepto maximizeR(p) =p·min{q(p), s}.
Call the spending ruleqmarkup-proofif for every supply levels >0 the clearing pricep c(s)
maximizes the seller’s revenue, so that the seller never gains by holding quantity below capacity.
The following result characterizes the class of markup-proof rules.
Proposition 1(Which commitments are markup-proof).Letqbe a spending rule that is continuous
on{p:q(p)>0}. Thenqis markup-proof if and only ife(p) =p q(p)is nonincreasing on[0, v],
equivalently if and only ifε(p)≥1at every price at whichqis differentiable.
Continuity is a regularity condition. It holds for the budget rule and for the mixed rule of
Appendix B.5, and it cannot be dispensed with. 1
The budget ruleq(p) =b/psatisfies the characterization witheexactly constant. The quantity
rule, being discontinuous, lies outside the scope of the proposition, but it fails to be markup-proof
directly, as the footnote 1 indicates.
1A spending rule with a downward jump yields the seller strictly higher revenue just below the jump than at the
clearing price. The quantity-target rule is the leading example: it is discontinuous at its reservationc, and at any
supplys < Sits clearing price iscitself, at which the buyer has already withdrawn and revenue is zero, whereas
posting slightly less thancyields approximatelycs. Such rules can be accommodated by defining the seller’s problem
over left limits, at the cost of additional notation that the argument does not require.
3

0 1 2 3 4 5 6
price p
0
1
2
3
4
5
6quantity demanded
supply s
pc = b/s
Budget cap: demand q = b/p
(unit elastic, = 1)
q(p) = b/p
0 1 2 3 4 5 6
price p
0
1
2
3
4
5
6quantity demanded
reservation c
Quantity cap: demand q = S
(perfectly inelastic, = 0)
q(p) = S 1{p < c}
0 1 2 3 4 5 6
price p
0
2
4
6
8revenue p q(p)
clearing pc: revenue
peaks, then flat (indifferent)
Revenue under budget cap
0 1 2 3 4 5 6
price p
0
2
4
6
8revenue p q(p)
seller keeps raising p
up to c: no clearing motive
Revenue under quantity cap
Demand and monopoly revenue: budget cap (left) vs. quantity cap (right)
Figure 1:Demand (top) and monopoly revenue (bottom) for a single buyer under a budget cap (left) and a quantity
cap (right), with the same reservation price and the same quantity and spend at the reference price. Budget-capped
revenue peaks at the clearing price and stays flat up to the reservation. Quantity-capped revenue keeps rising to the
reservation, so the seller has no reason to clear the market. See Appendix B.1 for details.
The economic mechanism behind the characterization is the link between elasticity and marginal
revenue. For a seller with zero marginal cost,
d
dp

p q(p)

=q(p)

1−ε(p)

,
so a price increase raises revenue exactly whenε <1. Budget-capped and quantity-capped demand
can agree at a single reference price: a budgetband a quantityS=b/pcoincide there. They
diverge once price moves away from that point, and it is this divergence, not the level of demand,
that determines whether a markup pays.
Corollary 1(No allocative distortion).Under a markup-proof spending rule the seller’s revenue-
maximizing quantity equals the competitive quantity, so the deadweight loss usually associated with
monopoly distortion is zero. Under the budget rule the seller’s revenue isbat every price in[p c, v].
4

A markup-proof rule therefore does more than transfer surplus from seller to buyer; it removes
the quantity distortion entirely.
Many rules are markup-proof; however, not all of them are equally advantageous for the buyer.
Among rules that satisfy the same affordability constraint, the budget rule occupies a distinguished
position.
Proposition 2(The budget rule is the least restrictive markup-proof commitment).Fixb >0and
consider all markup-proof spending rules satisfyinge(p)≤bfor allp. The budget ruleq(p) =b/p
is pointwise maximal among them. It delivers weakly more consumption at every pricep≤vthan
any other markup-proof, affordable rule, and it is the unique rule attaining this bound.
The buyer therefore faces no trade-off between markup-proofing and consumption at the point
of purchase. She could commit in other ways, for instance by undertaking to withdraw above
some price, but each alternative secures the same immunity only at the cost of lower consumption.
Committing to spend a fixed number of dollars is the weakest commitment that removes the seller’s
markup entirely, which is a reason to expect budgeting to take that form in practice.
2.2 Mental accounting as a commitment against markups
Propositions 1 and 2 characterize a buyer solely in terms of her spending rule. We now specialize
that rule to the two behavioral assumptions at issue, and ask what form a consumer’s within-
category demand takes under each.
Following Gorman [1959], we consider a consumer with incomem >0 to allocate acrossK
spending categories, each served by sellers with some degree of market power.
Without mental accounts.The consumer treats income asfully fungibleand forms a target
quantity in each category: a number of restaurant meals per month, a certain wardrobe, etc. Facing
a seller in categoryk, she is aquantity-capped buyer, and her demand is close to perfectly inelastic
up to her reservation value. Her spending rule is not markup-proof, so any seller with market power
can raise price toward that reservation.
With mental accounts.The consumer partitions her income into category budgetsb 1, . . . , bK,
with PK k=1 bk =m, and treats each as a hard limit, independent of what she could reallocate from
elsewhere. Facing a seller in categoryk, she is abudget-capped buyer, and her demand is the unit-
elastic hyperbolaq k(p) =b k/p. Her spending rule is markup-proof, and by Proposition 2 it is the
least restrictive rule with that property.
Observation 1.A consumer who commits to category-level dollar budgets converts her within-
category demand from perfectly inelastic to unit-elastic. By Propositions 1 and 2, this removes any
seller’s incentive to restrict supply and mark up price within that category, and does so at the least
cost in foregone consumption among all commitments with that property.
5

The familiar cost of mental accounting is misallocation. A rigid budget can leave money unspent
in one category while a more valuable opportunity in another goes unfunded, which is precisely
the fungibility violation that Thaler [1985] documents and that standard theory treats as an error.
The observation above is that this cost purchases something in return: within each category, the
consumer denies the seller the responsiveness he would require in order to raise price profitably.
Section 4 states the trade-off explicitly and gives the condition under which it favors budgeting.
This rationale differs from the self-control rationale. A perfectly patient, dynamically consistent
consumer facing no risk of temptation still has reason to adopt category budgets, provided she
expects to face sellers with market power. The two rationales are complementary, and either one
alone suffices to rationalize the behavior.
3 Rigidity versus separability
Two-stage budgeting appears to offer a fully rational route to the same object—a group-level
dollar budget—without invoking any behavioral departure from fungibility. This section shows that
separability generates budget but not necessarily markup-proofness, which depends on whether the
budget responds to prices.
If a consumer’s preferences overKgroups of goods are weakly separable, Gorman [1959] and
Deaton and Muellbauer [1980] show that her problem decomposes. She first allocates her incomem
across groups. She then chooses her within-group bundle to maximize a group-specific subutility,
subject to spending exactly the amount allocated. Separability makes the group budget a sufficient
statistic for within-group behavior: the composition of her purchases within groupkdepends on
prices elsewhere only through the amount she has allocated to groupk.
Separability alone does not make the budget markup-proof, however. The reason is that the
first-stage allocation is itself a function of prices. WritingP k for the group-kprice index, her
expenditure on groupkis
ek =E k(P1, . . . , PK, m).
A rational consumer re-optimizes her budget when prices move, so her group expenditure need
not be invariant to the price a within-group seller posts. Proposition 1 requires expenditure to be
nonincreasing in price, which is a restriction on how the first-stage allocation responds.
3.1 A CES upper-stage
To determine what that restriction amounts to, we specialize the first stage. Let the upper-stage
aggregator be CES,
U(Q 1, . . . , QK) =
PK
k=1 αk Q(σ−1)/σ k σ/(σ−1) , α k >0 fork= 1, . . . , K, σ >0,(1)
6

whereQ k is the group-kcomposite andσis the elasticity of substitution across groups. Standard
CES demand gives
Qk = ασ k P −σ k P 1−σ m, P≡ P j ασ j P 1−σ j 1/(1−σ) .(2)
Group expenditure ise k =P kQk =w km, where the budget share is
wk = ασ k P 1−σ kP
j ασ j P 1−σ j .(3)
Writex k ≡α σ k P 1−σ k for groupk’s term in the denominator of (3) andA −k ≡ P j̸=k ασ j P 1−σ j for
the remaining terms. Holding the other groups’ prices fixed, group-kexpenditure as a function of
the seller’s price is
ek(Pk) =m xk xk +A −k =m ασ k P 1−σ k ασ k P 1−σ k +A −k .(4)
Since∂lnx k/∂lnP k = 1−σ, differentiating (3) gives the share elasticity
∂lnw k
∂lnP k
= (1−σ)(1−w k),(5)
and becausee k =w kmwithmfixed, the expenditure elasticity is the same:
∂lne k
∂lnP k
= (1−σ)(1−w k) = 1−η k,(6)
whereη k ≡ −∂lnQk/∂lnP k is the uncompensated own-price elasticity of composite demand. Re-
arranging (6) yields the identity on which the results of this section rest:
ηk −1 = (σ−1)(1−w k),equivalentlyη k =σ(1−w k) +w k.(7)
Proposition 1 requiresη k ≥1. Sincew k ∈(0,1) implies 1−w k >0, (7) shows that this holds if
and only ifσ≥1. The threshold is therefore independent of the budget share, although the margin
by which it is satisfied is not, as discussed below.
Proposition 3(Rigidity, not separability, makes the budget markup-proof).Consider a consumer
who budgets in two stages with the CES upper stage(1), and suppose the seller in question is the
sole supplier of groupk, so thatP k is his posted price ande k(Pk)in(4)is his revenue. Then:
(i)(Substitutes,σ >1.)η k = 1 + (σ−1)(1−w k)>1, expendituree k(Pk)is strictly decreasing,
and the consumer’s spending rule is markup-proof. The seller’s revenue is maximized at the
clearing price, ande k(Pk)→0asP k → ∞.
(ii)(Cobb–Douglas,σ= 1.)η k = 1ande k =α kmfor everyP k. The rule is markup-proof, on
the boundary of the characterization, and pointwise maximal in the sense of Proposition 2.
The two-stage consumer is observationally indistinguishable from a rigid mental accountant.
7

(iii)(Complements,σ <1.)η k = 1−(1−σ)(1−w k)<1, expendituree k(Pk)is strictly increasing,
and the rule is not markup-proof. The seller’s revenue is strictly increasing in price at every
price, with supremum equal to the consumer’s entire income:
sup
Pk>0
ek(Pk) = lim Pk→∞ ek(Pk) =m.
A rigid mental account, which holdse k fixed atb k by construction, yieldsε= 1and is markup-proof
for everyσ, and caps the seller’s revenue atb k.
Part (iii) makes the magnitude of the exposure explicit. A consumer with complementary spend-
ing groups who re-optimizes rationally presents the group-kmonopolist with a revenue function
that is increasing in price throughout, and the only bound on what he collects is her income. The
rigid account, by contrast, bounds his revenue atb k, so the amount at stake in the decision to fix
the budget ism−b k, the expenditure the re-optimizing consumer remains willing to redirect toward
groupk. CES preferences admit no choke price, which is why income rather than a reservation
value provides the bound; a finite reservation value would truncate the seller’s price at that value,
leaving the direction of the incentive unchanged. Cases (ii) and (iii) also locate the two commitment
forms of Section 2 within a single family: the Cobb–Douglas case reproduces the mental accountant
exactly, and the quantity-target buyer arises as a limiting case of complementarity, as the following
corollary records.
Corollary 2(The Leontief limit is the quantity-target buyer).Asσ→0the upper stage becomes
Leontief and(7)givesη k →w k. For a category with a small budget share, composite demand
is close to perfectly inelastic and group expenditure rises almost proportionally with price. The
consumer of Section 2.2 who forms quantity targets rather than budgets thus corresponds to the
σ→0, small-w k limit of this family.
Exercise 1 in Appendix B.6 works through a two-group example with complements, computing
the seller’s price, the quantity he withholds, and the utility the re-optimizing consumer loses relative
to a rigid account.
3.2 Why substitutes generate markup-proofness and complements do not
The identity (7) decomposes the condition into two factors, both of which must be present to
generate markup-proofness.
The first factor,σ−1, measures whether the consumer’s substitution response is strong enough
to reduce her expenditure on a group whose price has risen. An increase inP k affectse k =P kQk
through two channels: the price paid per unit of the composite rises, raising expenditure, while
the quantity purchased falls, lowering it. The second channel dominates only whenη k >1, and
substitutability across groups is what makes the quantity response large enough for it to do so.
The second factor, 1−w k, measures the share of expenditure allocated outside the category, and
therefore the scope available for reallocation. Asw k →1 the category absorbs the entire budget
8

and (7) yieldsη k →1 for everyσ: absent an alternative destination for the funds, even a consumer
with a high elasticity of substitution behaves as though she held a fixed budget. Re-optimization
requires both a willingness to reallocate expenditure and somewhere to reallocate it.
Complementarity is the configuration a seller would prefer. When groups are complements, the
goods in groupkraise the marginal value of expenditure elsewhere, so the consumer values her
purchases across groups only in combination. An increase inP k raises the cost of that combination,
and her optimal response is to increase expenditure on groupkwhile reducing it elsewhere. Her
expenditure on groupkthen rises with its price, which is precisely the response from which a
monopolist profits. The mental accountant declines to reallocate, so her expenditure remains
constant and the seller gains nothing from raising price.
This inverts the standard interpretation of the fungibility violation. It is the re-optimizing
consumer’s flexibility that the seller exploits, while the mental accountant’s refusal to revise her
budget amounts to a refusal to respond, and expenditure that does not respond cannot be marked
up. The rigidity is therefore not a cost incurred alongside the benefit but the source of the benefit
itself.
We close this section pointing out two further and important implications of our analysis.
First, when groups are strict substitutes (σ >1) the rational consumer’s expenditure is strictly
decreasing inP k, so her rule is markup-proof but not pointwise maximal. By Proposition 2 she
consumes strictly less at high prices than a fixed budget would deliver, so demand more elastic
than unit-elastic removes the markup at a cost in consumption. The rigid mental account is the
boundary case that attains the bound.
Second, the rational and behavioral accounts of budgeting can now be compared on a common
footing. Both produce a group-level dollar budget at the point of sale, and what determines the
elasticity a within-group seller faces is the price-responsiveness of that budget rather than the
cognitive process that generates it.
4 The endogenous choice of a budget
The results so far take the consumer’s commitment as given. We now ask when she would choose
to make it, which requires weighing the markup she avoids against the flexibility she surrenders.
Consider a consumer with incomemfacing two categories,k= 1,2. She is small relative to
each market, so she takes prices as given. Letpdenote the competitive price she faces in either
category when her spending rule is markup-proof.
Her per-unit values are uncertain when she commits. With equal probability the state isA,
in which her values are (v H , vL), orB, in which they are (v L, vH ), withv H > vL >0. Write
¯v= 1 2 (vH +v L) for her mean value and ∆ =v H −¯v= 1 2 (vH −v L)>0 for its dispersion.
Undercommitmentshe fixes budgets (b 1, b2) withb 1 +b 2 =mbefore the state is realized, and
by Proposition 1 faces the clearing pricepin each category. Underno commitmentshe keeps the
flexibility to direct her whole income to whichever category turns out to be high-value, but she
9

presents a quantity-target rule, which is not markup-proof, and the seller marks price up to some
pN > p. She spends her entire income either way, so the two regimes can be compared by the gross
value of the goods she obtains.
Proposition 4(When budgeting is optimal).Under commitment the consumer’s optimal budgets
are symmetric,b 1 =b 2 =m/2, and every split yields the same expected payoff¯v m/p. She prefers
to commit if and only if
pN
p >1 + ∆ ¯v,
that is, if and only if the markup she avoids exceeds one plus the coefficient of dispersion of her
values. The value of commitment is increasing in the seller’s market powerp N /pand decreasing
in the dispersion∆.
The previous result makes explicit the fact that the trade-off is between two distinct benefits.
Rigidity costs the consumer the option to concentrate her spending where it turns out to be most
valuable, a loss proportional to ∆. It buys her the difference between the competitive and the
marked-up price, a gain proportional top N /p. She budgets when market power is large relative to
the dispersion of her values, and remains flexible otherwise. The structure of this trade-off parallels
the commitment-versus-flexibility tension in Galperti [2019], with market power in place of the
self-control problem as the source of the demand for commitment.
Costly attention and the value of commitment.Proposition 4 isolates the market-power
motive for committing by charging non-commitment only the cost of forgone flexibility, ∆. K˝ oszegi
and Matˇ ejka [2020] identify a second cost of not committing: tracking prices well enough to redirect
income optimally is itself costly. The two motives combine additively in the consumer’s decision.
Suppose that under no commitment, learning which category has realized the high valuev H
requires the consumer to pay an attention costκ≥0, denominated in the same units as her payoff,
while committing requires no such cost since her splitb 1 =b 2 =m/2 is optimal regardless of the
state. An uncommitted consumer who does not payκcan do no better than guess the state, and
guessing is dominated by committing whenever the seller has genuine market power, so the only
choice worth comparing to commitment is payingκto learn the state and reoptimize.
Proposition 5(The value of commitment under costly attention).Under the stated attention cost,
the consumer prefers to commit if and only if
pN
p >1 + ∆ ¯v− pN κ m¯v.
The right-hand side is strictly decreasing inκ: any positive attention cost makes commitment easier
to justify than under Proposition 4, and the two thresholds coincide atκ= 0.
Market power and attention cost act as substitutes on the margin of whether to commit. A
consumer facing weak market power may still rigidify if tracking prices is sufficiently onerous, and
10

a consumer with negligible attention costs may still rigidify if market power is sufficiently strong;
a consumer facing both frictions needs less of either one to justify budgeting than she would if she
faced only one. This makes formal the complementarity between the two rationales described in
Section 5: rather than two competing explanations for the same behavior, they are two additive
terms in a single commitment decision.
Comparative statics in market structure.Proposition 4 takesp N as exogenous. Making it
a function of the intensity of competition lets the value of budgeting be evaluated as a function of
market structure.
Supposen≥1 symmetric sellers compete in the category the consumer does not commit to,
withntreated as a continuous index of competitive intensity. Take the markup implied by Cournot
competition with linear demand, where the Lerner index scales as 1/n:
pN (n) =p+ vH −p n .
Atn= 1 this recovers Proposition 4 exactly, withp N (1) =v H . Asn→ ∞,p N (n)→p.
The competitive pricepdoes not require annsubscript: under commitment the buyer is budget-
capped, and Proposition 7 establishes that no seller gains from marking up against a budget-capped
buyer, regardless of the number of competitors he faces. The comparative static therefore operates
entirely through the no-commitment side of the comparison.
Proposition 6(Budgeting and market concentration).Letp N (n) =p+ (v H −p)/nforn≥1, and
suppose¯v > p. Then there is a threshold
n∗ = (vH −p) ¯v p∆
such that the consumer prefers to commit if and only ifn < n ∗. The value of commitment,
V(n) = ¯vm/p−v H m/pN (n), is strictly decreasing inn, strictly positive atn= 1, and satisfies
V(n)→ −m∆/p <0asn→ ∞.
The incentive to form a tight category budget is therefore strongest where competition is weak-
est, and vanishes as the category approaches perfect competition. A standard concentration mea-
sure such as the Herfindahl–Hirschman index is proportional to 1/nfor symmetric firms, so the
model delivers a testable prediction: mental-accounting behavior should be more common, and
category budgets tighter, in more concentrated categories, and should weaken as local competition
intensifies.
A fully microfounded version would replace the reduced-form markup with an explicit oligopoly
model, possibly with private information on both sides. The qualitative comparative static does
not depend on that choice, since it follows from any markup function decreasing innthat converges
top.
11

5 Related literature
We now place our models and results in the context of existing work on mental accounting, buyer-
optimal demand and buyer commitment, separability, and pricing to budget-constrained buyers.
5.1 Mental accounting.
Thaler [1985] and Thaler [1999] introduce mental accounting and document its departures from
fungibility. Shefrin and Thaler [1988] develop the planner-doer model in which mental accounts
serve as a self-control device. Koch and Nafziger [2016] model narrow psychological accounts as
commitments against a consumer’s own future temptation. Galperti [2019] derives good-specific
budgeting from the joint demand for commitment (against self-control problems) and flexibility
(against uncertainty in intratemporal trade-offs). Prelec and Loewenstein [1998] model the hedonic
coupling between the pleasure of consumption and the pain of paying. In each of these accounts the
friction being solved is internal to the consumer—a conflict between present and future selves, or
between certainty and flexibility—and none considers the consumer’s problem facing a seller with
market power.
5.2 Budgeting in dollars or in units.
K˝ oszegi and Matˇ ejka [2020] is the closest work to our framework. They show that a consumer
who finds it costly to track prices adopts a rigid, category-level dollar budget once the relevant
elasticity of substitution crosses a threshold (one-half in their baseline quadratic specification), and
that once adopted, her category expenditure isexactlyconstant across realized prices, not merely
less responsive (their Proposition 3 and Corollary 1). That object is mechanically identical to ours:
exactly constant expenditure is exactly theε= 1 case of Proposition 1, so a K˝ oszegi-Matˇ ejka hard
budget is markup-proof in our sense as soon as it is adopted. The two papers therefore agree
entirely on what rigidity delivers, and differ on why a consumer would want it. Their elasticity
threshold governs whether a consumer with a fixed cost of attention chooses to become rigid at all,
in place of reoptimizing every period at no cost; our threshold in Proposition 3 instead asks, of a
consumer who already reoptimizes for free, whether her ordinary, price-responsive demand happens
to be markup-proof anyway. Hence, the market-power motive we identify operates on the same
margin as their attention-cost motive—whether to commit at all—rather than on the margin of
what a given commitment delivers once made. Our result in Proposition 5 makes the two motives
jointly formal: each lowers the bar the other must clear on its own, so a consumer facing weak
market power may still rigidify if attention is sufficiently costly, and a consumer with negligible
attention costs may still rigidify if market power is sufficiently strong.
A related literature studies how a buyer’s limited attention shapes a seller’s pricing. Ravid
[2020] shows that a rationally inattentive buyer facing a take-it-or-leave-it offer earns a strictly
positive payoff, and Cusumano et al. [2024] study price competition among sellers facing a ratio-
nally inattentive consumer. In these papers the buyer’s leverage comes from how she processes
12

information; in ours it comes from the rigidity of her budget, and Proposition 5 shows that an
attention cost and market power enter the decision to commit additively.
5.3 Buyer-optimal demand.
The closest antecedent to Section 2 is Condorelli and Szentes [2020], in which a buyer chooses
the distribution of her valuation before a monopolist makes a take-it-or-leave-it offer. The buyer-
optimal distribution generates unit-elastic demand, the seller is indifferent across an interval of
prices, and trade occurs with probability one.?obtain the same unit-elastic structure when the
buyer instead chooses what to learn about a fixed valuation, and the equal-revenue distribution plays
a related role in the buyer-optimal segmentation of?. Proposition 1, Corollary 1, and Proposition 2
should be read as the budget-commitment counterpart of this result. There the buyer commits to
a value distribution and here to a spending rule, and in both cases the seller’s incentive to mark
up disappears because the buyer’s expenditure does not rise with price. The contribution of the
present note lies in the object through which the commitment is made—a dollar budget, the object
the mental-accounting literature documents—and in embedding it in a multi-category consumer
problem, which is what permits the comparison between rigid and re-optimized budgets in Section 3
and the comparative statics of Section 4.
5.4 Buyer commitment against sellers.
A broader literature studies how buyers obtain better terms by limiting their own responsiveness.
?shows that buyer groups, by committing to purchase exclusively from one seller, intensify price
competition even when their members have heterogeneous preferences.??studies principals who
impose budget constraints on the bidders acting for them; there the budget resolves an agency
problem between principal and bidder rather than a pricing problem between buyer and seller,
which is the margin studied here.
5.5 Separability and two-stage budgeting.
Gorman [1959] and Deaton and Muellbauer [1980] establish the separability conditions under which
two-stage budgeting is valid. A subsequent literature, including Blackorby et al. [1978] and the
revealed-preference characterizations of weak separability in Quah [2012] and Cherchye et al. [2015],
studies when separability can be tested nonparametrically from demand data. That literature
treats separability as a property of preferences to be identified or exploited computationally, and
does not connect it to the pricing power of sellers within a group. Proposition 3 indicates why the
distinction matters: separability governs whether the group budget is a sufficient statistic, while
markup-proofness turns on whether that budget responds to prices. The elasticity on which that
proposition rests,η k =σ(1−w k) +wk, has the same form as the share-dependent demand elasticity
in nested-CES models of oligopoly with a unit-elastic upper tier [?], and the requirement that this
elasticity exceed one for a monopolist’s markup to be finite is standard in that literature. Our use
13

of it differs: we read the thresholdσ≥1 as the condition under which a re-optimizing consumer’s
group budget is markup-proof, and contrast it with a rigid budget, which is markup-proof for every
σ.
5.6 Pricing to budget-constrained buyers.
The demand-side mechanism we build on—that budget-constrained rather than quantity-constrained
buyers remove a seller’s incentive to mark up price—follows from the revenue-optimality result for
competitive pricing in budget-constrained Fisher markets established by Finster et al. [2025], and
is applied to advertising exchanges (where advertisers declare budgets rather than click quotas) in
Melo et al. [2026]. To our knowledge no existing paper connects this pricing-side mechanism to
mental accounting or to Gorman–Deaton separability; the contribution of this note is that connec-
tion.
6 Discussion
This note offers a market-structure rationale for category-level dollar budgeting, a behavior that has
been explained almost entirely by appeal to the consumer’s internal psychology. The rationale is
complementary to the existing ones: a consumer with severe self-control problems and a consumer
with none can both benefit from mental accounts, for different reasons, and a consumer facing both
frictions has more reason still.
In Appendix B.3 we derive a mechanism-design implication sharpens the point: a revenue-
maximizing seller who could design what buyers commit to would prefer quantity targets, while
a buyer who anticipates this prefers a dollar budget. Mental accounting and two-stage budgeting
may be read, in this light, as a demand-side response to the seller’s side of that problem, adopted
because the dollar budget is the buyer-optimal commitment to make.
Proposition 3 suggests a sharper reading of the behavioral evidence. What the literature records
as a failure of fungibility is what makes the commitment binding: a budget that adjusts to prices,
as a fully rational separable consumer’s would, is markup-proof only when her spending groups are
substitutes, while a budget she refuses to revise is markup-proof in every case and caps the seller’s
revenue at the budget rather than at her income. The observed rigidity is not incidental to the
practice but constitutive of its value.
The argument as developed here is largely static. Proposition 6 endogenizes the markup and
shows that the incentive to budget is strongest where competition is weakest and vanishes as the
category becomes competitive, yielding the testable prediction that mental-accounting behavior
should track local market concentration. That result rests on a reduced-form markup rather than
a fully specified oligopoly game with private information on both sides. Extending it to such a
setting, and to the many-buyer, many-seller case more generally, is a natural next step.
14

References
Charles Blackorby, Daniel Primont, and R Robert Russell. Duality, separability, and functional
structure: Theory and economic applications.North-Holland, 1978.
Laurens Cherchye, Thomas Demuynck, and Bram De Rock. Revealed preference tests for weak
separability: An integer programming approach.Journal of Econometrics, 186(1):129–141, 2015.
Daniele Condorelli and Bal´ azs Szentes. Information design in the holdup problem.Journal of
Political Economy, 128(2):681–709, 2020.
Carlo M Cusumano, Francesco Fabbri, and Ferdinand Pieroth. Competing to commit: Markets
with rational inattention.American Economic Review, 114(1):285–306, 2024.
Angus Deaton and John Muellbauer.Economics and Consumer Behavior. Cambridge University
Press, 1980.
Simon Finster, Paul W Goldberg, and Edwin Lock. Competitive and revenue-optimal pricing with
budgets.Theoretical Economics, 20:1135–1153, 2025. doi: 10.3982/TE5913.
Simone Galperti. A theory of personal budgeting.Theoretical Economics, 14(1):173–210, 2019.
William M Gorman. Separable utility and aggregation.Econometrica, 27(3):469–481, 1959.
Alexander K Koch and Julia Nafziger. Goals and bracketing under mental accounting.Journal of
Economic Theory, 162:305–351, 2016.
Botond K˝ oszegi and Filip Matˇ ejka. Choice simplification: A theory of mental budgeting and naive
diversification.The Quarterly Journal of Economics, 135(2):1153–1207, 2020.
Emerson Melo, Matthew Shum, and Rakesh Vohra. One-shot pricing for hands-off-the-wheel ad-
vertising markets. Working paper, 2026.
Drazen Prelec and George Loewenstein. The red and the black: Mental accounting of savings and
debt.Marketing Science, 17(1):4–28, 1998.
John K-H Quah. A revealed preference test for weakly separable preferences.University of Oxford
Department of Economics Discussion Paper, 2012.
Doron Ravid. Ultimatum bargaining with rational inattention.American Economic Review, 110
(9):2948–2963, 2020.
Hersh M Shefrin and Richard H Thaler. The behavioral life-cycle hypothesis.Economic Inquiry,
26(4):609–643, 1988.
Richard Thaler. Mental accounting and consumer choice.Marketing Science, 4(3):199–214, 1985.
15

Richard H Thaler. Mental accounting matters.Journal of Behavioral Decision Making, 12(3):
183–206, 1999.
A Proofs
Proof of Proposition 1.Fixs >0 and letp c =p c(s). Forp≤p c we haveq(p)≥s, so supply binds
andR(p) =p s, which is strictly increasing; the seller therefore never posts a price belowp c. For
p≥p c we haveq(p)≤s, so demand binds andR(p) =p q(p) =e(p). Hencep c is revenue-optimal
if and only ife(p)≤e(p c) for allp≥p c.
Suppose first thateis nonincreasing. Continuity ofqgivesq(p c) =s, soR(p c) =p cs, and hence
R(p) =ps≤p cs=R(p c) forp≤p c, whileR(p) =e(p)≤e(p c) =R(p c) forp≥p c. Thusp c is
revenue-optimal, and sinceswas arbitrary,qis markup-proof.
Conversely, supposeeis not nonincreasing, so there existp 1 < p2 in [0, v] withe(p 2)> e(p1).
Sets=q(p 1) and letp c =p c(s). Sinceq(p 1)≤swe havep c ≤p 1, and sinceqis nonincreasing with
q(pc)≤s=q(p 1) andp c ≤p 1, it follows thatq(p c) =q(p 1). Therefore
e(pc) =p c q(pc) =p c q(p1)≤p 1 q(p1) =e(p 1)< e(p 2).
Becausep 2 > p1 ≥p c andq(p 2)≤q(p 1) =s, demand binds atp 2, soR(p 2) =e(p 2)> e(pc) =R(p c).
The seller therefore strictly prefersp 2 to the clearing price at this supply level, andqis not markup-
proof.
Finally, whereqis differentiable,e ′(p) =q(p)  1−ε(p)  withε(p) =−q ′(p)p/q(p), soe ′ ≤0 if
and only ifε≥1.
Proof of Corollary 1.By the argument above, under a markup-proof rule the seller’s revenue is
maximized atp c(s), at whichq(p c) =s: the entire capacity is sold, which is the competitive
quantity. Since marginal cost is zero, total surplus is maximized when all units are transferred,
so the allocative distortion is zero. Under the budget rulee≡bon [0, v], soR(p) =bfor every
p∈[p c, v].
Proof of Proposition 2.Letqbe markup-proof and affordable, with expendituree(p) =p q(p)≤b
for allp, andenonincreasing by Proposition 1. Sinceq(p) =e(p)/p, at each fixedpthe buyer’s
consumption is increasing ine(p), so a pointwise-maximal rule is one with pointwise-maximal expen-
diture. Affordability boundse(p)≤bfor everyp, and the constant functione≡bis nonincreasing,
hence markup-proof, and attains this bound at every price. Thereforeq ∗(p) =b/pis markup-proof,
affordable, and satisfiesq ∗(p)≥q(p) for allp≤vand any competing markup-proof affordableq.
Uniqueness: ifqattains the bound at everyp≤vthene(p) =bfor all suchp, soq(p) =b/p.
Proof of Proposition 3. Step 1: expenditure and its elasticity.Under two-stage budgeting the con-
16

sumer’s group-kexpenditure ise k =P kQk. Taking logarithms and differentiating in lnP k,
∂lne k
∂lnP k
= 1 + ∂lnQ k
∂lnP k
= 1−η k,(8)
whereη k =−∂lnQ k/∂lnP k. Hence∂e k/∂Pk ≤0 if and only ifη k ≥1. A within-group seller
who raises his price raisesP k, so by Proposition 1 the consumer’s within-group spending rule is
markup-proof exactly when group expenditure is nonincreasing inP k, that is, whenη k ≥1. This
step uses onlye k =P kQk and is therefore independent of the CES specialization.
Step 2: the CES share elasticity.With the aggregator (1), cost minimization over the up-
per stage gives the demands (2) and hence the shares (3). Writex k =α σ k P 1−σ k andA −k =P
j̸=k ασ j P 1−σ j , so thatw k =x k/(xk +A −k) and∂lnx k/∂lnP k = 1−σ. Then
∂lnw k
∂lnP k
= ∂lnx k
∂lnP k
− xk
xk +A −k
· ∂lnx k
∂lnP k
= (1−σ)

1−w k

,
which is (5). Sincee k =w kmwith income fixed,∂lne k/∂lnP k =∂lnw k/∂lnP k, and comparing
with (8) gives
1−η k = (1−σ)(1−w k)⇐ ⇒η k = 1 + (σ−1)(1−w k) =σ(1−w k) +w k,
which is (7). As a check, the compensated own-price elasticity of CES composite demand isσ(1−wk)
and CES preferences are homothetic, so the income elasticity is one and the Slutsky decomposition
gives the sameη k =σ(1−w k) +w k.
Step 3: the three cases.Sincew k ∈(0,1), we have 1−w k >0, so (7) gives
ηk ≥1⇐ ⇒(σ−1)(1−w k)≥0⇐ ⇒σ≥1,
with strict inequality in each direction. Monotonicity ofe k follows from (4): the mapx7→mx/(x+
A−k) is strictly increasing, andx k =α σ k P 1−σ k is strictly decreasing inP k whenσ >1, constant when
σ= 1, and strictly increasing whenσ <1. Hencee k is strictly decreasing, constant, or strictly
increasing inP k in the three cases respectively.
For the limits, ifσ >1 thenx k →0 asP k → ∞, soek →0. Ifσ= 1 thenx k =α k and
wk =α k/ P j αj, which is independent of all prices; normalizing P j αj = 1 givese k =α km. If
σ <1 thenx k → ∞asPk → ∞, sowk →1 and
ek(Pk) =m xk xk +A −k ↗m.
Becausee k is the sole supplier’s revenue and is strictly increasing with supremumm, the seller has
a strict incentive to raise price at every price, and by Proposition 1 the rule is not markup-proof.
Step 4: the rigid account.A rigid mental account fixese k =b k independently ofP k, soe(p)≡b k
is constant,ε= 1, and by Proposition 1 the rule is markup-proof for everyσ. The seller’s revenue
17

isb k at every price he might post.
Proof of Corollary 2.Letσ→0 in (7):η k =σ(1−w k) +wk →w k. Sincew k <1, the limit satisfies
ηk <1, so by Proposition 1 the rule is not markup-proof, and by (6) the expenditure elasticity is
1−w k >0. For a category with a small budget share the elasticityη k ≈0 and the expenditure
elasticity≈1, which are the values of the quantity-target ruleq(p) =S·1{p < c}of Section 2 on
p < c.
Proof of Proposition 4.Under commitment the consumer faces pricepin each category and receives
qk =b k/p. In stateAher payoff is (v H b1 +v Lb2)/pand in stateBit is (v Lb1 +v H b2)/p. Averaging
over the two equally likely states,
E[payoff] = 1 2p  (vH +v L)b1 + (vL +v H )b2  = (vH +v L)(b1 +b 2) 2p = ¯v m p ,
which is independent of the split; the symmetric splitb 1 =b 2 =m/2 is therefore optimal, and
every other split is equally good ex ante. Under no commitment she learns the state and directs
all income to the high-value category, obtainingv H m/pN . Comparing,
¯v m
p > vH m pN ⇐ ⇒pN p > vH ¯v = ¯v+ ∆ ¯v = 1 + ∆ ¯v.
The right-hand side is increasing in ∆ and the condition is easier to satisfy asp N /prises, giving
the stated comparative statics.
Proof of Proposition 5.Under commitment the consumer’s payoff is ¯vm/p, unaffected byκsince no
attention is required. Under no commitment, a consumer who guesses the state, choosing a category
independently of its realization, obtains 1 2 vH m/pN + 1 2 vLm/pN = ¯vm/pN ; sincep N > pwhenever
the seller has genuine market power, this is strictly less than ¯vm/p, so guessing is dominated
by committing and is never chosen. A consumer who instead paysκto learn the state obtains
vH m/pN −κ, as in Proposition 4 net of the attention cost. Comparing the two remaining options,
¯vm
p > vH m pN −κ⇐ ⇒ ¯v p + κ m > vH pN ⇐ ⇒pN p > vH ¯v − pN κ m¯v = 1 + ∆ ¯v− pN κ m¯v,
usingv H /¯v= 1 + ∆/¯vas in the proof of Proposition 4. The right-hand side is strictly decreasing
inκsincep N , m,¯v >0, and settingκ= 0 recovers the threshold of Proposition 4.
Proof of Proposition 6.Substitutingp N (n) into the commitment condition of Proposition 4,
pN (n)
p >1 + ∆ ¯v ⇐ ⇒vH −p np > ∆ ¯v ⇐ ⇒n <(vH −p)¯v p∆ =n ∗.
For monotonicity ofV,p N (n) is strictly decreasing innsincev H > p, sov H m/pN (n) is strictly
increasing inn, andV(n) = ¯vm/p−v H m/pN (n) is strictly decreasing inn. Atn= 1,p N (1) =v H ,
18

soV(1) = ¯vm/p−m=m(¯v−p)/p >0 since ¯v > pby assumption. Asn→ ∞,p N (n)→p, so
V(n)→¯vm/p−v H m/p=m(¯v−v H )/p=−m∆/p <0, usingv H −¯v= ∆.
B Supporting derivations
B.1 Single buyer
A seller with zero marginal cost and fixed supplysfaces one buyer. If the buyer has a fixed dollar
budgetband constant per-unit valuev, she spends her entire budget whenever pricep≤v: demand
isq(p) =b/p. Its elasticity is
ε(p) =− dq dp · p q =−  − b p2  · p b/p = 1 (p≤v),
so revenuep q(p) =bis constant inpon this range. The seller’s revenue, allowing for the supply
cap, is
R(p) =p·min{q(p), s}=



p s p≤p c (supply binds),
b p c ≤p≤v(budget binds),
0p > v(buyer exits),
wherep c =b/sis the market-clearing price.Ris strictly increasing forp < p c and constant for
p∈[p c, v].
If instead the buyer has a fixed physical quantity targetS≤sand reservation valuec, demand
is the step functionq(p) =S·1{p < c}, withε(p) = 0 forp < c. Revenue isR(p) =p Sforp < c
andR(p) = 0 forp > c: strictly increasing up to the reservation, so the seller prefers to raise price
toc.
Figure 1 plots both cases, usingb= 6,s= 2,v= 4 (sop c = 3) for the budget-capped buyer
andS= 2,c= 4 for the quantity-capped buyer.
B.2 Many buyers
Proposition 7(Exclusion never pays under budget caps).Consider finitely many buyers indexed
byi, and a seller with zero marginal cost. If each buyer is budget-capped with budgetb i and
reservationv i, aggregate revenue at any price above the clearing price equals P i:vi≥p bi, which is
constant inpbetween consecutive reservations and falls by exactlyb j aspcrossesv j. Excluding
any buyer is therefore a strict revenue loss, and the clearing price is revenue-optimal. If instead
each buyer is quantity-capped with targetS i and reservationc i, aggregate revenue above the clearing
price isp P i:ci≥p Si, and excluding a low-reservation buyer is generally profitable.
Proof.With budget caps, buyericontributesq i(p) =b i/pwhilev i ≥pand nothing otherwise,
so her expenditure isb i whenever she is active. Aggregate expenditure is thusE(p) = P i:vi≥p bi,
constant on any interval containing no reservation value and dropping byb j atp=v j. Since
19

each remaining buyer’s payment is already pinned at her own budget, buyerj’s exit generates
no offsetting increase, soEis nonincreasing and strictly lower abovev j than below. Applying
Proposition 1 to the aggregate rule gives revenue-optimality of the clearing price.
With quantity caps, each active buyer contributesS i irrespective ofp, so aggregate expenditure
isp P i:ci≥p Si, which is strictly increasing inpbetween consecutive reservations. Raising price past
cj forfeitsc jSj but raises the price paid by every remaining, still price-inelastic buyer; whenever
the latter effect dominates, which occurs generally when the excluded buyer’s reservation is low
relative to those of the others, exclusion raises revenue.
B.3 Mechanism design
Proposition 7 has an implication for the commitment a revenue-maximizing seller would prefer
buyers to adopt, were he able to design it. A seller who could induce buyers to report and commit
to a fixed physical quantity, rather than a fixed dollar budget, would prefer to do so, since quantity
commitments constitute the case in which excluding a marginal buyer and raising price on the
remainder is profitable. A buyer who anticipates this prefers to commit to a dollar budget, since a
genuine budget commitment forecloses that strategy.
Relabeling a quantity target as a dollar amount evaluated at current prices does not remove the
asymmetry. What matters is how the commitment responds as price moves away from its current
level, and only a genuine budget commitment requires demand, and hence marginal revenue, to
contract as price rises.
Remark 1(Robustness to nonlinear pricing).The results of Section 2 restrict the seller to a single
linear posted price. For a single buyer with a known budget, this restriction costs the seller noth-
ing.?, Proposition 1 show that when the seller can offer an arbitrary nonlinear tariff, menu of
lotteries, or financing scheme to a budget-constrained buyer whose budget is known, the revenue-
maximizing mechanism is still a single take-it-or-leave-it price, equal to the smaller of the uncon-
strained monopoly price and the budget. There is no scope for price discrimination to extract more
than linear pricing already delivers, which is precisely the conclusion of Corollary 1 that revenue is
pinned atb. The single-buyer case therefore survives the move from posted pricing to fully optimal
mechanism design.
Proposition 7 is more fragile, because it is stated for linear pricing only. Once budgets and
valuations are private information held by a population of buyers,?and its extension to general
type distributions in?show that a revenue-maximizing seller does generally discriminate, using
menus of lotteries and budget-contingent prices, because private budgets create the same screening
problem that private valuations do. This does not overturn the aggregation logic, which concerns
only how a seller restricted to a single posted price treats budget- versus quantity-capped buyers,
but it means the result should be read as a statement about linear pricing, with the fully optimal
many-buyer mechanism left as an open extension.
20

B.4 When the budget fails to be markup-proof
Two qualifications on the main results deserve statement.
The budget must be tight.Suppose the consumer’s category budget isX k but she also has
an underlying physical need forS k units. Her demand is
qk(p) = min{Xk/p, Sk},
with a kink atp=X k/Sk (Figure 2). Below the kink the physical need binds and demand is
perfectly inelastic. Above it the budget binds and demand is unit-elastic.
0 1 2 3 4 5 6 7
price p
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0
4.5quantity demanded
kink at p = X/S
Mixed cap: q(p) = min{X/p, S}
whichever constraint binds sets the elasticity
p < X/S: quantity binds, q = S ( = 0)
p > X/S: budget binds, q = X/p ( = 1)
Figure 2:A consumer with both a category budgetX k and a physical needS k: demandq(p) = min{X k/p, Sk}has
a kink atp=X k/Sk. Below the kink the quantity need binds and demand is perfectly inelastic. Above it the budget
binds and demand is unit-elastic. See Appendix B.5.
Remark 2.Mental accounting makes the consumer’s spending rule markup-proof in categoryk
only when the category budget istightrelative to her underlying quantity need, that is, only when
the budget rather than the physical quantity limits her purchases at the prices she faces. A generous
budget, set well above what she would spend on the quantity she wants, provides no markup-proofing.
This also indicates where mental accounting should and should not be observed. Discretionary
categories with flexible quantities and many potential purchases, such as dining out, entertainment,
and clothing, are the ones in which a tight dollar budget can bind before a physical quantity target
does. They are also the categories in which mental accounting is most often reported. Categories
involving a single large, indivisible commitment, such as a home or an insurance policy, do not offer
room for the budget to bind at the margin, and mental accounting in the Thaler sense is less salient
there. Two-stage budgeting still describes the allocation across such groups at a coarser level.
21

The seller’s technology .The results assume zero marginal cost and capacity-constrained sup-
ply, which is the case of a seller who wishes to sell his entire endowment. With strictly positive
marginal cost the seller’s profit from a budget-capped buyer isb−c q(p), which is increasing inp,
so he raises price toward the buyer’s reservation value and sells less. Revenue remains pinned atb,
so he extracts no more, but the buyer receives fewer units.
Budget commitment therefore bounds what a seller can collect under any cost structure. It
delivers the full competitive quantity when marginal cost is negligible relative to price, which is the
empirically relevant case for capacity services and digital goods.
B.5 Mixed case derivation
A buyer with both a budgetXand a physical quantity targetShas demandq(p) = min{X/p, S}.
Forp < X/Sthe budget would buy more thanSunits, so the quantity cap binds:q(p) =Sand
ε(p) = 0. Forp > X/Sthe budget buys fewer thanSunits, so the budget cap binds:q(p) =X/p
andε(p) = 1. The two regimes meet at the kinkp=X/S(Figure 2, drawn withX= 8 andS= 2,
so the kink lies atp= 4).
Expenditure ise(p) =pSbelow the kink ande(p) =Xabove it, soeis increasing on the first
segment and constant on the second. By Proposition 1 the rule is markup-proof only if the relevant
price range lies aboveX/S. A budget that does not bind at the prices the buyer actually faces
provides no markup-proofing, since the quantity cap binds first and demand is inelastic where it
matters.
B.6 A worked example with complements
Exercise 1.LetK= 2,σ= 1 2 ,α 1 =α 2 = 1 2 , incomem= 100, andP 2 = 1. Group 1 is supplied by
a single seller with zero marginal cost, capacitys= 50, and a price cap ¯P= 9, which plays the role
of the finite reservation value discussed after Proposition 3. Compare a consumer who re-optimizes
her budgets in two stages with a rigid mental accountant who fixes ¯e1 = ¯b2 = 50.
(a) Show that the re-optimizing consumer’s group-1 expenditure ise 1(P) = 100
√
P /(
√
P+ 1).
Computee 1,w 1, andη 1 atP∈ {1,4,9}, and confirm thatη 1 <1 throughout.
(b) Find the seller’s revenue-maximizing price, revenue, and quantity sold against each consumer.
(c) Compare the two consumers’ utilities.
(d) Repeat (a)–(c) withσ= 2.
Solution.(a)Withα 1 =α 2 the factorα σ k cancels in (4), andP 1−σ k = √Pk, soe 1(P) =
m
√
P /(
√
P+ 1) withm= 100. The budget share isw 1 =
√
P /(
√
P+ 1) and, by (7),η 1 =
22

1
2 (1−w 1) +w 1 = 1 2 (1 +w 1):
P 1 4 9
e1(P) 50 66.7 75
w1 1/2 2/3 3/4
η1 3/4 5/6 7/8
Sincew 1 <1,η 1 <1 at every price, and expenditure rises with price as in Proposition 3(iii).
(b)Against the re-optimizing consumer, group-1 demand isQ 1(P) =e 1(P)/P= 100/
√
P(
√
P+
1)

, which equalss= 50 atP= 1, so the clearing price isp c = 1. Above it demand binds
and revenuee 1(P) is strictly increasing, so the seller posts the cap ¯P= 9, collects 75, and sells
Q1 = 75/9 = 25/3 units, leaving 125/3 units of capacity unsold. Against the rigid accountant,
Q1 = 50/P, the clearing price is againp c = 1, and revenue equals 50 at everyP∈[1,9]; by
Proposition 1 the clearing price is revenue-maximizing, and at it the seller sells his full capacity of
50 units.
(c)Withσ= 1 2 the aggregator (1) isU= (α 1Q−1 1 +α 2Q−1 2 )−1. The re-optimizing consumer
faces (P1, P2) = (9,1) and spends (75,25), so (Q 1, Q2) = (25/3,25) and
U flex =  1 2 · 3 25 + 1 2 · 1 25 −1 = 12.5.
The rigid accountant faces (1,1) and spends (50,50), so (Q 1, Q2) = (50,50) andU rigid = 50. The
rigid budget coincides with what the re-optimizing consumer would choose at competitive prices;
her willingness to revise it is what lets the seller raise the price, and she loses three quarters of her
utility as a result. The seller gains 25 in revenue, the differencee 1( ¯P)−¯e 1, and the allocative loss
is the unsold capacity.
(d)Withσ= 2,α σ k = 1 4 cancels andP 1−σ k = 1/Pk, soe 1(P) = 100/(1 +P), which is strictly
decreasing, andη 1 = 2(1−w 1) +w 1 = 1.5 atP= 1. The seller’s revenue above the clearing price
pc = 1 is decreasing, so he clears atP= 1, collects 50, and sells 50 units. Both consumers then
obtain (Q 1, Q2) = (50,50) andU= ( 1 2 √ 50 + 1 2 √ 50)2 = 50. With substitutes, flexibility costs the
consumer nothing, as in Proposition 3(i).
23
