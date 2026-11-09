---
title: Auction-based allocation of routes in capacity-constrained networks
url: https://arxiv.org/abs/2610.20125
category: consumer-behavior
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Gergely Csáji
- Dávid Csercsik
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.20125
pages: 34
chars: 68232
fetched_at: '2026-11-08T13:17:41+00:00'
kb_version: 1
---

# Auction-based allocation of routes in capacity-constrained networks

Auction-based allocation of routes in capacity-constrained networks
Gergely Csáji
HUN-REN Institute for Computer Science and Control,
Kende u. 13-17., H-1111 Budapest;
Budapest University of Technology and Economics,
Műegyetem rkp. 3., H-1111, Budapest
csajigergely@sztaki.hu
Dávid Csercsik∗
ELTE Centre for Economic and Regional Studies, Institute of Economics,
Tóth Kálmán u. 4., H-1097 Budapest
Tel.: +36-1 309 26 52 Fax: +36-1 319 31 36
Pázmány Péter Catholic University, Faculty of Information Technology and Bionics, Práter u. 50/A 1083
Budapest, Hungary
Tel.: +36-1 886 47 00 Fax: +36-1 886 47 24
csercsik.david@krtk.elte.hu
Abstract
We study the route-set allocation problem between end nodes in capacity-constrained flow net-
works with transfer costs. We introduce anorigin–destination(OD) bidding language, in which a
participant bids for bounded conic combinations of inlet–outlet–quantity licences and the mech-
anism performs the routing through a network-flow optimising winner-determination problem.
We then study payment rules for the OD mechanism. Under arestrictedmodel with openly and
uniformly priced sources and bidders who are indifferent to the source of the gas, the Vickrey–
Clarke–Groves (VCG) payment is core-stable; the key structural fact is that in this regime some
optimal aggregate flows never use a physical pipe in both directions, so the winner-determination
problem reduces to a single-commodity network flow whose value is submodular in the set of
active bidders. If source access is allowed to depend on the individual consumer – a realistic
feature, e.g. when gas deals are embedded in bilateral political bargaining – the reduction fails
and VCG payments may lie strictly outside the core. For this general model we propose adual
(nodal) pricingrule derived from the shadow prices of the flow-conservation constraints, and
prove it is always core-stable, at the cost of dominant-strategy incentive compatibility. Illustra-
tive examples accompany each result.
Keywords:Auctions/bidding, Networks, OR in energy, Mechanism design, Core stability
∗Corresponding author
1
arXiv:2610.20125v1  [econ.TH]  14 Oct 2026

1. Introduction
1.1. Motivation and background
The allocation of scarce transport capacity in a network, where the medium is steerable – gas
pipelines, freight corridors, data links – is a mechanism design problem in which the goods (edge
capacities) are complements: a participant who is required to ship goods to their desired destina-
tion values a capacity product only as part of a complete route from a source to its consumption
point. The same structure – endpoint demand over a shared, capacitated network – underlies
auction designs for bandwidth and inter-domain traffic (Belzarena, Ferragut, & Paganini, 2009;
Maillé & Tuffin, 2007) and for railway paths (Stojadinović, Bošković, Trifunović, & Janković,
2019), as discussed in Section 1.3. The current European practice for natural gas pipelines allo-
cates capacity through simultaneous ascending clock auctions on the PRISMA platform, a design
whose shortcomings under a dominant supplier are well documented (Takácsné Tóth, Kotek, &
Kaderják, 2017).
As an alternative, the concept ofconvex combinatorial auction(CCA) has been proposed
(Csercsik, 2022), which exploits the divisibility of pipeline capacity: bidders submit route–
quantity bids, and the clearing assigns each participant a convex combination of its submitted
bids by solving a single linear program, with payments determined by the Vickrey–Clarke–Groves
(VCG)principle. Relativetotheascendingclockauction, theCCAallocatesonlyusablecapacity,
attains higher resulting utility, allows a more efficient utilisation of the available infrastructure
and reduces the bidding burden.
The CCA framework is characterised by one important structural limitation that motivates
the present paper. Each participant must determine the set of routes on which it is willing to
bid in advance; the mechanism then optimises only over convex combinations of these predefined
routes. In the example networks of Csercsik (2022) the route set is fixed a priori, and the
paper itself lists “the routes considered in the auction” as an exogenous input and flags their
determination as future work. Because the number of source–sink routes in a network grows
exponentially with its size, complete enumeration is infeasible for realistic instances, and any
incomplete enumeration can, as we show, induce inefficient results in terms of welfare.
1.2. Contributions
The paper is organised around two models of source access, treated in two main parts.
1.The general model (Section 4).When source access or price may depend on the
consumer, bidders evaluate each source differently. Accordingly, we introduce an origin–
destination (OD) bidding language of (inlet, outlet, quantity) licences, with the WDP –
2

a network-flow linear program – performing the routing; this removes the route enumera-
tion of the convex combinatorial auction of Csercsik (2022), whose fixed route sets can be
strictly suboptimal (Section 6.1, Example 17). In this model, VCG payments can lie strictly
outside the core (Example 19). More generally, such a failure requires a departure from
source indifference; dedicated access and inlet-specific quantity caps are two ways this can
occur (Proposition 20). We therefore propose adual (nodal) pricingrule read off the flow-
conservation shadow prices and prove it is always core-stable (Theorem 23), at the cost of
dominant-strategy incentive compatibility – an unavoidable trade-off – but core-selecting in
the spirit of Day and Milgrom (2008).
2.The restricted model (Section 5).Sources are openly and uniformly priced and the
good is homogeneous, so a consumer is indifferent towhichsource supplies it. A bidder
then submits atomicquantity–pricelicences describing its inverse demand at its own sink,
and the winner-determination problem (WDP) is a single-commodity min-cost flow. We
prove that the coalition value is submodular in the set of bidders, so the Vickrey–Clarke–
Groves (VCG) payment is core-stable (Proposition 16). The proof is elementary: an exchange
argument (Lemma 13) shows optimal flows can be chosen such that they do not oppose on any
edges, and a linear-programming (LP) duality argument on the node potentials (Lemma 15)
yields submodularity directly. We also show that this positive result genuinely needs source
indifference, and inlet-specific quantity caps may undermine submodularity (Examples 11–
12).
The remainder of the paper is organised as follows. Section 2 introduces the network model
and Section 3 the auction-theoretic preliminaries (core and VCG). Section 4 formulates the OD
bidding language and the general winner-determination problem. Section 5 studies the restricted
model and establishes the core stability of VCG. Section 6 compares the OD mechanism with
route enumeration, exhibits failures of VCG beyond source indifference, and introduces dual
pricing. Section 7 discusses incentives, counter-directed flows and the scope of the results, and
Section 8 concludes.
1.3. Related work
Auction-based allocation of divisible capacity on a network, with endpoint (rather than link-
by-link)biddingandpricesderivedfromtheoptimisationduals, hasprecedentoutsidethenatural
gas literature. The bandwidth-auction design of Belzarena et al. (2009) can be regarded as closest
to the present mechanism: users place a single bid for an end-to-end connection “oblivious to the
internal topology”, the operator solves a capacity-constrained allocation, and per-route prices
3

are read off the Lagrange multipliers of the link constraints. This approach structurally aligns
the endpoint bidding language and dual pricing proposed in the current article; the underlying
idea of pricing shared network capacity by the shadow prices (Lagrange multipliers) of the link
constraints is the network-utility-maximisation tradition of Kelly, Maulloo, and Tan (1998). Two
features separate their setting from ours and locate our contribution. First, the good considered
in Belzarena et al. (2009) is indivisible (a circuit), so their allocation is an integer program
whose convex relaxation isnotexact. Rounding must be applied, and no exact dual price
exists. In our model capacity is divisible, the WDP is an exact linear program, and its duals
are genuine competitive-equilibrium prices – which is precisely what makes the core-stability
guarantee available. Second, they adopt a first-price rule and explicitly decline VCG, observing
thatonascarcelink“thegeneralizedVickreyauctionwouldchargeapriceequaltothehighestbid
left out. . .hence the network receives zero revenue”. This phenomenon is related to the generally
known low-revenue pathology of VCG, which may imply that the VCG-induced outputs may lie
outside the core (Day & Milgrom, 2008). On the other hand, the application of a first-price
rule (i.e. a “pay-as-bid” approach) has straightforward drawbacks related to strategic bidding
(Tierney, Schatzki, & Mukerji, 2008). Belzarena et al. (2009) furthermore argue that computing
the VCG prices is demanding, since an integer program must be solved in the case of each
player. Scepticism about VCG for network pricing is independently documented by Maillé and
Tuffin (2007), who argue it “can hardly be applied” to inter-domain and ad hoc networks for
two reasons: with capacity constraints and single-path routing the allocation (and theN+1
pricing optimizations) is NP-hard, and without them VCG violates budget balance, requiring
the operator to inject money. The divisible, multi-path (network-flow) formulation presented in
this paper dissolves this first objection – the WDP is a polynomial linear program, so the VCG
allocation and payments are all tractable.
In addition, in contrast to Belzarena et al. (2009), Maillé and Tuffin (2007) and (Csercsik,
2022), we also consider the question of stability and propose a core-stable payment rule. The
impossibility framing of Moulin and Shenker (2001) (efficiency, incentive compatibility, individual
rationality and budget balance cannot hold jointly) is consistent with our design: the dual-
price rule relaxes dominant-strategy incentive compatibility, not budget balance or individual
rationality.
Auction and combinatorial-market designs for network-path allocation also appear in other
regulated infrastructures, notably railway capacity allocation (Shahmohammadi, Fakhrzad, Hos-
seini Nasab, & Ghannadpour, 2024; Stojadinović et al., 2019), where competing operators bid
for train paths through a shared, capacitated network. In the setting of railway capacity allo-
4

cation, a train path is a rigid sequence of track segments and time slots, far less substitutable
than fungible gas flow, so the route bundle is characterised by an intrinsic complementarity and
indivisibility. In contrast, our contribution is designed for fungible and divisible commodities
like gas or bandwidth. In the following we will primarily consider the context of natural gas
networks, and define the assumptions of the proposed model accordingly.
2. Network model
We work with the network abstraction of the model used in Csercsik (2022). LetG= (N, E)
be a directed graph: nodesNrepresent market areas – the entry–exit zones within which capacity
is booked and traded, whose efficiency is analysed by Keller, Kuper, and Mulder (2019) – and
each edgee∈Erepresents a directed capacity product with maximal transfer capacity¯q e ≥0
and per-unit transfer costc t e ≥0. A subsetN s ⊆Nof nodes aresources; sources∈N s can
inject gas at per-unit costcs s ≥0. The good ishomogeneous– gas of identical quality (calorific
value) regardless of source – so a unit delivered to a consumer is equally valuable whatever inlet it
entered through; sources differ only in price and location, not in the good itself. The remaining
nodes hostconsumers(bidders) or are purely intermediate. Each biddericonsumes at some
noden i (no consumption node is shared by two bidders) and, in line with the piecewise-constant
inverse-demand curves used in Csercsik (2022), has a concave, piecewise-linear, nondecreasing
willingness-to-pay.
LetPdenote the set of physical pipes. Each pipeline is modelled by a pair of oppositely
directededgeswithindependentnonnegativecapacities; aphysicalflowusesatmostonedirection
of a pipe at a time. We distinguish two capacity conventions and treat both:
Directed-arc (no netting).Each directed edge has its own capacity constraint on its own
nonnegative flow.
Netting.Counter-directed flows on the two arcs of a pipe cancel, so the capacity constraint
binds thenetflow, as in Eq. (7) of Csercsik (2022).
Under the directed-arc convention, opposite directional capacity bookings are treated as inde-
pendent and may coexist; under netting, they are aggregated into physical net flow.
2.1. Two source regimes
The distinction that organises the paper is how sources may be accessed by consumers.
Definition 1(General model with (potentially) dedicated sources).The accessibility and/or
price of a source may depend on the individual consumer: bidderiaccesses sourcesat price
5

cs s,i ∈R ≥0 ∪ {+∞}(+∞encoding inaccessibility). The restricted model is the special case
cs s,i =c s s for alliwith, in addition, source indifference.
Consumer-dependent access is not a purely artificial idea; it is motivated by practical rel-
evance. In natural gas trading, long-term supply relationships, take-or-pay contracts, and the
embedding of gas deals in bilateral political bargaining all affect the effective price at which a
given importer can draw from a given source specific to that importer in the period for which
capacityisallocated; thegeopoliticaldiscussionofBilgin(2009)ispreciselyaboutsuchconsumer-
specific access. Our results identify source indifference, rather than divisibility or network size,
as the boundary of the positive guarantee: consumer-specific access and inlet-specific caps are
distinct ways to cross that boundary.
Definition 2(Restricted modelR).Every node is source-only, consumer-only, or intermediate;
every source is openly accessible to every bidder at aconsumer-independentposted pricecs s; and,
the good being homogeneous, each bidder isindifferent to the sourceof its gas – it values only
the quantity delivered to its own sink, not the inlet through which it entered. This is the regime
of Csercsik (2022).
3. Preliminaries: core and VCG
We recall the two solution concepts of auction theory used in the paper. Let the set of players
beI∪ {0}, whereIis the set of bidders and0the auctioneer (holder of all capacity). Anoutcome
is an ordered pair of an allocation (A) and a payment vectorP. The payoff or utility of playeri
isu i =V i(A)−p i, whereV i(A)is the valuation of items received by playeriin allocationA.
In our case, a bidder’s total paymentpi may be decomposed into three streams with dis-
tinct recipients, and only one of them contributes to the income of the auctioneer. Thesource
paymentsrepresent income to the gas suppliers (or, for positioned gas, are the shipper’s own
sunk acquisition cost); thetransfer paymentsare paid to the local transmission system operators
(TSOs), who under the EU third-party-access principle set and collect these regulated tariffs on
their own infrastructure; and thecapacity paymentsCC i – the charge for the scarce capacity
licences – accrue to the auctioneer. Source and transfer payments are therefore pass-throughs,
not auctioneer income; their explicit form in terms of the source costsc s and transfer costs
ct is given with the winner-determination problem in Section 4.1 (eq. (1)). Accordingly the
auctioneer’s payoff is
u0 =
X
i
CCi,
the sum of capacity payments only, in line with the income of the auctioneer in the model of
Csercsik (2022). As shown in Section 6.3, under the dual price this equals the congestion rent
6

P
a∈P (λ+⋆ a ¯q+ a +λ −⋆ a ¯q− a )≥0, so the auctioneer earns exactly the scarcity value of the binding
capacity constraints and nothing in the absence of congestion. Suppliers and TSOs are paid
precisely their costs and are treated as cost sinks rather than players in the proposed model.
Consequently, the coalition valuew(S)below is equal to thenet welfare(valuations minus source
and transfer costs), which is exactly the objective of the WDP.
Definition 3(Coalition value).ForS⊆I, the coalition valuew(S)is the optimum of the
winner-determination program in force – see eq. (1) in the restricted model (Section 5), and eq.
(1) in the general model (Section 4) – the maximal net welfare attainable when the bidders inS
are served over the full network, withw(S) = 0if the auctioneer is absent. We setw(∅) = 0.
Definition 4(Core).An outcome with payoffs(ui)i∈I , u0 is in thecoreif it is feasible (P i∈I ui +
u0 =w(I)), individually rational (ui ≥0), andunblocked: for every coalitionS⊆I,
u0 +
X
i∈S
ui ≥w(S).
Equivalently, no coalition of the auctioneer with a set of bidders could, on its own, guarantee its
members more than they receive.
Definition 5(VCG payment).Under the VCG (Clarke pivot) rule (Clarke, 1971; Groves, 1973;
Vickrey, 1961), the allocation maximises total reported value and bidderipays the externality
it imposes,
pVCG i =w(I\ {i})−  w(I)−V i(Ai)  ,
the difference between the others’ best value withoutiand their value withipresent. VCG is
efficient and dominant-strategy incentive compatible (DSIC).
A classical sufficient condition links the two. Ifwissubmodularover bidders – equivalently,
bidders are substitutes in the sense of Ausubel and Milgrom (2002, 2006) – then the VCG payoff
vector lies in the core and is its bidder-optimal point; see also Bikhchandani and Ostroy (2002)
for the underlying linear-programming characterisation. Conversely, whenwis not submodular,
VCG revenue can be so low that a coalition blocks, and VCG leaves the core – the phenomenon
that motivates the concept of core-selecting auctions (Day & Milgrom, 2008).
4. The general model: OD bidding and winner determination
We first formulate the general allocation problem, allowing source access and source prices to
dependonthebidder. Therestrictedmodelwillthenbeobtainedbyimposingsourceindifference.
7

4.1. The OD bidding language
Instead of enumerating routes between potentially multiple sources and a consumer’s destina-
tion, a bidder describes only where gas may enter and where it is to be delivered; the mechanism
chooses the route.
Definition 6(OD licence).Anatomic licenceof bidderiis a tupleb= (o b, qb, vb): an inlet node
ob, the bidder’s outlettb =n i, a maximum quantityqb ≥0, and a gross per-unit valuevb ≥0.
Acceptingbat leveld b ∈[0, qb]injectsd b units ato b, delivers them atni, and contributesv bdb
to gross value.
Definition 7(Bid region).Bidderisubmits a finite setB i of atomic licences and an overall cap
QT i . Its accepted vector ranges over the bounded polytope
Pi =
n
di ∈R Bi ≥0 :d b ≤q b ∀b, X
b∈Bi
db ≤Q T i
o
.
The reported gross valuation isVi(di) = P b∈Bi vbdb.
Example 8.For a bidder consuming at nodeC, the statement “I want up to2units fromAto
my nodeC, worthv 1 each; or up to3units fromBtoC, worthv 2 each; but at most4units
in total” corresponds to the licences(A,2, v1)and(B,3, v 2)withQ T = 4. The bidder names no
path.
Source access is encoded inBi: a bidder that cannot use sourcesnames no license originating
there.
4.2. General winner determination
Recall thatPis the set of physical pipes. Give each pipea∈ Pan arbitrary reference
orientationa + = (ua, va)and reverse orientationa− = (va, ua), with directional capacities¯q+ a ,¯q− a
and nonnegative costsct,+ a , ct,− a . Writef + i,a, f− i,a ≥0for bidderi’s directional flows andAfor the
incidence matrix of the resulting directed arc set⃗E={a +, a− :a∈ P}, which is the directed
edge setEof Section 2 with its orientation made explicit. In the netting convention,g+ a , g− a form
a nonnegative split of the aggregate net flow. For a coalitionS⊆I, the general WDP is
8

w(S) = max
d,f,g
X
i∈S
Vi(di)−
X
a∈P

ct,+ a g+ a +c t,− a g− a  − X
i∈S
X
b∈Bi
cs ob,idb
s.t.
X
a∈ ⃗E
An,afi,a =1[n=n i]
X
b∈Bi
db −
X
b∈Bi:ob=n
db ∀i∈S,∀n(π i,n),
X
i∈S

f + i,a −f − i,a  =g + a −g − a ∀a∈ P(τ a),
g+ a ≤¯q+ a ∀a∈ P(λ + a ),
g− a ≤¯q− a ∀a∈ P(λ − a ),
db ≤q b ∀i∈S,∀b∈ B i (αb),
X
b∈Bi
db ≤Q T i ∀i∈S(β i),
d, f, g+, g− ≥0.
Thus netting is imposed on the two directions of thesame physical pipe, not on a single
directed arc. The directed-arc convention is obtained from (1) by deletingg+, g− and the net-
flow identity, imposing
X
i∈S
f + i,a ≤¯q+ a , X
i∈S
f − i,a ≤¯q− a (a∈ P),
and replacing the transfer-cost term byP a,σ∈{+,−} ct,σ a P i f σ i,a. The conservation equation says
exactly that bidderiinjectsd b at each licence inlet and withdrawsDi = P b∈Bi db at its sink
ni. Both capacity conventions give linear programs. LP (1) definesw(S)in the general model;
a coalition without the auctioneer controls no capacity and has value zero.
Remark9.Consider a route-CCA of Csercsik (2022) defined on the same network, with the
same source access, costs, capacity convention, and bidder quantity restrictions as the OD WDP.
If every enumerated route is a valid path from its stated inlet to the bidder’s sink, then every
allocationfeasibleforthatroute-CCAcanbeembeddedintheODWDPbyroutingeachaccepted
quantity along its enumerated path. Consequently, the route-CCA feasible set is contained in
the OD feasible set and
w(I)≥w CCA(I).
Conversely, if the route-CCA enumerates all feasible inlet–sink paths, then an optimal OD flow
can be decomposed into path flows for the individual bidders. Since transfer costs are nonnega-
tive, flow circulations that do not contribute to any delivery can be omitted without decreasing
welfare. Each remaining path component corresponds to an enumerated route of the route-CCA,
and assigning its flow value to that route reproduces the same accepted quantities, network loads,
9

and welfare. Hence every optimal OD allocation has an equivalent allocation in the completely
enumerated route-CCA, so
w(I)≤w CCA(I).
Therefore, under complete route enumeration,
w(I) =w CCA(I).
Thus the advantage of the OD formulation is not a relaxation of the allocation problem: it repre-
sents the complete-route optimum without requiring the bidders to enumerate an exponentially
large family of paths.
5. The restricted model: quantity–price licences and core-stable VCG
Throughout this section we are in the restricted modelR(Definition 2): sources are open
and uniformly priced, and each bidder is indifferent to which source supplies its (homogeneous)
gas.
5.1. Quantity–price licences
Definition 10(Atomic licences and inverse demand).InRa bidderi(consuming atn i) submits
a finite setBi of atomicquantity–pricelicences, each a pairb= (q b, vb): up toq b units delivered
atn i, worthv b each. With acceptance levelsd b ∈[0, qb]and total deliveryD i = P b∈Bi db,
the reported value isV i(di) = P b∈Bi vbdb. Ordering the licences by decreasingv b makesV i a
concave, piecewise-linear, nondecreasing function ofDi – the bidder’s inverse demand curve. We
writeP i ={d i ≥0 :d b ≤q b ∀b, P b∈Bi db ≤Q T i }. If no additional total cap is desired, set
QT i = P b∈Bi qb, so the last inequality is redundant.
5.2. Why source indifference matters
Open, uniformly priced sources are not by themselves enough for the results below: if a
bidder could attachinlet-specificquantity caps to its licences, both the no-opposing-flows lemma
(Section 5.3) and submodularity would fail. Source indifference (no per-inlet caps) is exactly
what rules this out.
Example 11(Per-source caps may induce opposing flows).Let a single bidirectional pipe join
AandB, with a zero-cost source at each end. Bidder1consumes atAbut may draw at most
1/4from the source atAand up to1from the source atB; bidder2is the mirror image atB.
Each wants one unit. Serving both requires bidder1to import at least3/4of a unitB→A
and bidder2to import at least3/4of a unitA→B, so the pipe carries flow inbothdirections
10

at the optimum. The source-swap that would remove the opposition – reroute bidder1to draw
fromA– is infeasible, as it violates bidder1’s cap of1/4atA.
Example 12(Submodularity fails under per-source caps).Take sourcess A, sB and arcss A →
A e1 − →Be2 − →TandsB →B, withe 1, e2 of capacity1(Figure 1); all costs zero. BidderY
consumes atB; biddersXandZconsume at distinct nodest X andt Z, reached fromTby
uncapacitated zero-cost arcs, so their gas must crosse2. Each wants at most one unit at value
1, with inlet-specific capsX: at most1froms A and 1 4 froms B;Y: same asX;Z: at most 1 4
froms A and1froms B. Solving the flow problem per coalition givesw(X) = 1,w(X, Z) = 1,
w(X, Y) = 3 2,w(X, Y, Z) = 2, so
w(X, Y) +w(X, Z) =5 2 <3 =w(X, Y, Z) +w(X),
violating submodularity: the caps makeYandZcomplements.
sA A B T
sB
e1 e2
Y
tX
tZ
X
Z
Figure 1: Example 12. With inlet-specific caps the coalition value is not submodular; source indifference removes
the effect.
Both failures come from the same feature – an inlet-specific cap forces a bidder onto a particu-
lar source, manufacturing a counter-directed import (Example 11) or a complementarity between
otherwise-independent bidders (Example 12). Neither is present under source indifference, which
is why Definition 10 admits only sink-side caps.
5.3. Existence of optimal flows that do not oppose
Lemma 13(No opposing flows).InR, every netting-feasible allocation can be converted into a
directed-arc feasible allocation with the same deliveries and weakly greater welfare, in which no
pipe carries flow in both directions.
Proof.Fix a netting-feasible allocation and a physical pipea. Write its gross directional flows
asx + a , x− a ≥0and its net flow asz a =x + a −x − a. Cancelδ a = min{x+ a , x− a }and retain
ex+ a = [za]+,ex − a = [−za]+.
11

At the two endpoints, the contribution to net inflow is unchanged; hence every node balance
is unchanged. The netting boundsza ≤¯q+ a and−z a ≤¯q− a imply the separate directed bounds
ex+ a ≤¯q+ a andex− a ≤¯q− a . Nonnegative transfer costs weakly decrease (and under the net-flow cost
convention are unchanged). Most importantly, the source injections, accepted quantitiesdi, and
deliveriesD i are untouched, so every atomic capdb ≤q b and total cap P b db ≤Q T i remains
feasible. The resulting aggregate flow may be decomposed into source–sink paths and the paths
ending atn i assigned to bidderi; source indifference makes this assignment valid because no
bidder-specific origin constraint remains. Applying this cancellation pipe by pipe proves the
claim.
Corollary 14(Netting is inert inR).InRthe netting and directed-arc models attain the same
optimum.
Proof.Every directed-arc feasible solution is netting-feasible: if its flows onaarex + a , x− a, then
za =x + a −x − a ≤x + a ≤¯q+ a and−z a ≤x − a ≤¯q− a . Netting can only weakly reduce its transport cost,
sow net ≥w dir. Conversely, Lemma 13 convertsanynetting-feasible solution, including a netting
optimum, into a directed-arc feasible solution of weakly greater welfare. Thusw dir ≥w net,
proving equality.
5.4. Restricted winner determination
We may therefore formulate the restricted WDP using directed arcs. Add a super-sourceZ∗
and an uncapacitated source arc(Z∗, s)for everys∈N s. Let
E∗ = ⃗E∪ {(Z∗, s) :s∈N s},
and define the per-unit arc cost by
ce =



ct e, e∈ ⃗E,
cs s, e= (Z ∗, s), s∈Ns.
Writef e ≥0for the single-commodity flow on every arce∈E ∗, and letδ−(n)andδ +(n)denote
the incoming and outgoing arcs ofnin the extended graph. The source arcs are uncapacitated,
while the transport arcs retain their capacities¯qe. For each coalitionS⊆I, the restricted WDP
is the linear program
12

w(S) = max
d,f
X
i∈S
X
b∈Bi
vbdb −
X
e∈E∗
cefe (1)
s.t.
X
e∈δ+(n)
fe −
X
e∈δ−(n)
fe +
X
i∈S
ni=n
Di −1[n=Z ∗] X
i∈S
Di = 0∀n∈N∪ {Z ∗}(π n),
fe ≤¯qe ∀e∈ ⃗E(λ e),
db ≤q b ∀i∈S,∀b∈ B i (αb),
X
b∈Bi
db ≤Q T i ∀i∈S(β i),
d, f≥0.
Parentheses denote the corresponding dual variables. Thus there is a free conservation dual
πn ateverynode, includingZ ∗, sources, and intermediate nodes. A licence names no inlet: the
single-commodity flow chooses the source. LP (1) defines the restricted coalition value and, by
Corollary 14, also the value under netting.
5.5. Submodularity and core-stability
Lemma 15(Submodularity of the coalition value).InR, the coalition valuewof(1)is mono-
tone and submodular overI.
Proof.ByCorollary14weusethedirected-arcformulation; allbidderssharethesingle-commodity
flow. Forr∈Rset
ϕi(r) = max di∈Pi {Vi(di)−rD i}, D i =
X
b∈Bi
db,
which is nonincreasing inr. The LP dual of (1) is
min
π,λ,α,β
X
e∈ ⃗E
¯qeλe +
X
i∈S
 X
b∈Bi
qbαb +Q T i βi

s.t.λ e +π u −π v ≥ −ct e, e= (u, v)∈ ⃗E,
πZ∗ −π s ≥ −cs s, s∈N s,
αb +β i +π ni −π Z∗ ≥v b, i∈S, b∈ B i,
λe, αb, βi ≥0.
(2)
Normaliseπ Z∗ = 0. Minimising overλe ≥0contributes¯q e[πv −πu −ct e]+ to the reduced objective,
and we may chooseλe = [πv −π u −c t e]+ (also when¯qe = 0). The source arcs giveπs ≤c s s.
For fixed node potentialsπ, the dual variablesαb andβ i associated with bidderisolve the
13

separate optimisation problem
min
α,β
X
b∈Bi
qbαb +Q T i βi
s.t.α b +β i ≥v b −π ni, b∈ B i,
αb ≥0, β i ≥0.
(Di(πni))
But this is exactly the LP dual ofmax{Vi(di)−π niDi |d i ∈P i}. Therefore, by strong duality,
min
αb,βi



X
b∈Bi
qbαb +Q T i βi |(α, β)∈D i(πni)


 = max di∈Pi {Vi(di)−π niDi}=ϕ i(πni).
Thus, after minimizing over the bidder-specific dual variablesαb andβ i, biddericontributes
simplyϕ i(πni)to the reduced dual objective. Hence
w(S) = min
π∈Π
(
H(π) +
X
i∈S
ϕi(πni)
)
,(3)
where
H(π) =
X
e=(u,v)
¯qe[πv −π u −c t e]+,Π ={π:π Z∗ = 0, πs ≤c s s ∀s∈N s}.
For two potential vectorsπ, ρ, letπ∧ρandπ∨ρdenote their componentwise minimum and
maximum. We first note that
H(π) +H(ρ)≥H(π∧ρ) +H(π∨ρ).(4)
It suffices to check one arce= (u, v). Ifπ, ρare ordered the same way atuandvthe two sides
coincide; otherwise, sayπu ≤ρ u andπ v ≥ρ v, theleftargumentsof[·] + areπ v−πu−ct e, ρv−ρu−ct e
and the right onesρv −π u −c t e, πv −ρ u −c t e; the two pairs have equal sum and the left pair
majorises the right, so convexity of[·]+ gives the arc inequality, and summing yields (4).
Now letD S(π) =H(π) + P i∈S ϕi(πni). Since eachϕ i is nonincreasing, for allA, B⊆Iand
π, ρ∈Π,
DA(π) +D B(ρ)≥D A∩B(π∧ρ) +D A∪B(π∨ρ) :(5)
bidders inA∩Bcontribute the same two terms on each side; fori∈A\B,ϕ i(πni)≥
ϕi(max{πni, ρni}), symmetrically forB\A; theHterms obey (4). NoteΠis closed under
∧,∨.
The primal (1) is feasible (d= 0) and bounded (Pi bounded, capacities finite), so strong
duality holds and the outer minimum in (3) is attained; letπA, πB attain it forA, B. Then
w(A) +w(B) =D A(πA) +DB(πB)≥D A∩B(πA ∧π B) +DA∪B(πA ∨π B)≥w(A∩B) +w(A∪B),
14

using (5) andw(S)≤D S(π)for everyπ∈Π. Thuswis submodular; monotonicity holds since
a bidder may deliver zero.
Proposition 16(VCG is core-stable inR).In the restricted model the coalition valuewof(1)
is submodular over bidders. Consequently the VCG payment vector lies in the core and is its
bidder-optimal point (Ausubel & Milgrom, 2002, 2006).
6. Consequences beyond source indifference
We now use the general OD formulation of Section 4 to compare it with route enumeration,
exhibit failures of VCG core stability, and derive a dual pricing rule.
6.1. Route enumeration is a source of inefficiency
Example 17(Diamond with an un-enumerated alternate route).Consider Figure 2. Node1
hosts a sources(price0). Capacities are1on every edge. Transfer costs:c t = 0ona:1→2,
c:2→4,e:2→5, andc t = 1onb:1→3,d:3→4. ConsumerC 1 at node4and consumerC 2 at node
5each demand1unit, with valuesv 1 = 10,v 2 = 8. Both cheapest routes (C1 via{a, c},C 2 via
{a, e}) traverse the shared edgea.
1 2
3 4
5
a(0)
b(1) c(0)
d(1)
e(0)
s
C1
C2
Figure 2: Example 17. Edge labels show name and transfer cost. Both consumers’ cheapest routes share edgea;
C1 has an alternate route{b, d}of cost2.
Route-CCA under cheapest-route enumeration.Ifeachbidderenumeratesonlyitscheapestroute,
both name a bundle containinga. The clearing solvesmax{10x1 + 8x2 :x 1 +x 2 ≤1}and serves
onlyC 1, resulting in a welfare of10units, andC 2 is left unserved although the network could
carry it.
OD mechanism.With OD bidsC 1:(1→4,10)andC 2:(1→5,8), the WDP routesC 1 over the
costlier{b, d}(net10−2 = 8) andC 2 over{a, e}(net8), serving both resulting in a welfare of
16units.
15

The gap of6is caused solely by bounded enumeration: hadC 1 also listed{b, d}the route-
CCA would reach16too. Since the number of routes is exponential, no fixed enumeration is safe
in general; the OD mechanism attains the complete-enumeration optimum at polynomial size,
because the WDP performs the substitution across paths that the bidder would otherwise have
to anticipate.
Remark18.Example 17 illustrates the efficiency deficit implied by thebidding languageand
nothing else. In this particular case its VCG payments are in fact core-stable (the contested
resource is a single edge, a substitution rather than a complementarity conflict). Thepayment
defect requires a different structure, exhibited in Section 6.2.
6.2. Dedicated sources: VCG may leave the core
We now show that the source-indifference restriction in Proposition 16 cannot be dropped
from its guarantee: in the general model, VCG can be strictly outside the core. The mechanism
is complementarity. InRthe no-opposing-flows lemma (Lemma 13) rests on source indiffer-
ence. Consumer-dependent access removes that indifference and can therefore reintroduce the
complementarity exhibited below; inlet-specific caps, as in Example 12, are another way to do
so.
Example 19(Series network with dedicated entry).Series network1→2→3with edges
e1:1→2,e 2:2→3, each of capacity1and transfer cost0(Figure 3). Node1carries gas usable by
all; node2carries adedicatedentry point available only to the bidder positioned to inject there
(a distinct incoming pipeline or liquefied natural gas (LNG) berth, not an open source). Three
unit licences of value2:
X= (1→3), Y= (1→2), Z= (2→3).
Xneeds both edges;Yneedse 1 alone;Zneedse 2 alone. Because the node-2entry is dedicated,
Xcannot bypasse 1 by sourcing at node2– the maneuver that, inR, would dissolve the
complementarity.
1 2 3
e1 e2
Figure 3: Example 19.Xbids1→3(both edges),Ybids1→2,Zbids2→3.
WDP.Withf X +f Y ≤1one 1 andf X +f Z ≤1one 2, maximising2(f X +f Y +f Z)gives
fY =f Z = 1,f X = 0: welfare4.
16

VCG.RemovingY, the others’ best is2(eitherXtakes the pair orZtakese 2); withYpresent
they already obtain2, soY’s externality is0. By symmetryZpays0. Total VCG revenue is0.
Core violation.The coalition{0, X}can guarantee itself2(Xwould pay up to2for the two
edges), so the core requiresp Y +p Z ≥2. VCG collects0<2: the VCG outcome isstrictly
outside the core. Herewis not submodular –X’s two edges are complements – which is possible
precisely because the node-2entry is dedicated, so Lemma 13 and hence Proposition 16 do not
apply.
Proposition 20(The source-indifference boundary).A strict VCG core violation cannot occur
in the restricted modelR. Once source indifference is dropped, it may occur through consumer-
dependent source access or prices, or through inlet-specific quantity restrictions. Consumer-
dependent source access can therefore produce a failure, but is not necessary for one.
Proof.Proposition 16 rules out a violation inR, whereas Example 19 supplies one with dedicated
access. For inlet-specific caps, use Example 12, where additionallyw(Y, Z) = 2. At the grand-
coalition optimum biddersY, Zare served andXis not. Their VCG payments are
pY =w(X, Z)−(2−1) = 0, p Z =w(X, Y)−(2−1) = 1 2 .
The auctioneer therefore receives1/2, while the unserved bidderXhas utility zero. But coalition
{0, X}can attainw(X) = 1>1/2, so it blocks. This failure uses zero, hence consumer-
independent, source prices; it is caused solely by the inlet-specific caps.
6.3. Dual (nodal) pricing
Since VCG can leave the core in the general model, and since core stability is a natural
requirement for a regulated allocation (no coalition of the regulator with a group of shippers
should be able to improve on the outcome), we adopt a payment rule that targets the core
directly, following the core-selecting philosophy of Day and Milgrom (2008). The rule reads
prices off the dual of the WDP.
6.3.1. The rule
Let(π ⋆, λ+⋆, λ−⋆)be an optimal dual of (1). The conservation duals inducenodal prices: for
a licenceb∈ Bi with inleto b, delivered to bidderi’s sinkni, let
µ⋆ b =c s ob,i +π ⋆ i,ni −π ⋆ i,ob
be the delivered marginal price of a unit entering atob and consumed atni. Bidderipays
pi =
X
b∈Bi
d⋆ b µ⋆ b ,(6)
17

the nodal spread on each licence times the quantity delivered on it. Of this payment, the
source and transfer components ofµ⋆ b are forwarded to the suppliers and the local TSOs (per the
third-party-access split of Section 3); the auctioneer retains only the congestion component, so
its total income (as shown later in Theorem 23) is
X
i
CCi =
X
a∈P

λ+⋆ a ¯q+ a +λ −⋆ a ¯q− a  ≥0,
the scarcity rent of the binding capacity constraints. In particular, when no capacity binds
(λ+⋆ =λ −⋆ ≡0) every payment passes through to suppliers and TSOs and the auctioneer
collects nothing – a capacity auction earns only the scarcity it actually rations, and is revenue-
adequate on its capacity account without ever being subsidised.
Remark21 (Why nodal, not per-edge).Per-bidder flow on an edge is not determined by the WDP
(equivalent optima reshuffle routing among same-OD bidders), so a per-edge charge is ill-posed –
and under netting it can even change sign with counterflow. The nodal charge (6) depends only
on the accepted OD quantities and the node prices; for any selected optimal dual, the charge is
decomposition-invariant. This is the locational-marginal-pricing convention of electricity markets
adapted to capacity licences.
6.3.2. Core-stability
Remark22 (Intuition).Core stability of the dual prices rests on a competitive-equilibrium ar-
gument. By LP strong duality, an optimal allocation and an optimal dual satisfy complemen-
tary slackness. At the nodal pricesµ ⋆, each bidder’s accepted bundle maximises its surplus
Vi(di)−µ ⋆ ·d i overP i, and the optimal flow maximises the network’s profit, i.e. its revenue at
the nodal prices net of source and transfer costs, which equals the congestion rent. That the
dual of a linear allocation program supplies equilibrium prices supporting a core outcome is the
package-assignment view of combinatorial markets (Bikhchandani & Ostroy, 2002), rooted in
the assignment game, where competitive prices coincide with the core (Shapley & Shubik, 1971).
The welfare of any coalition can be split into the surplus of its members at the equilibrium prices
and the network’s profit at the same prices; neither part can exceed its equilibrium value, so
no coalition can block. Theorem 23 makes this argument precise for both capacity conventions.
Since it relies only on dual feasibility and complementary slackness, it holds for every optimal
dual and requires no restriction on source access. The same argument applies to the restricted
problem (1), where the nodal price paid by bidderiisπ⋆ ni.
For bidderiwe writeµ ⋆·d i = P b∈Bi µ⋆ b db, the licence-indexed inner product, so thatpi =µ ⋆·d ⋆ i;
for a delivery profiley= (y i)i∈I,µ ⋆ ·y= P i µ⋆ ·y i.
18

Theorem 23(Dual pricing is core-stable).In the general model, under either the netting or the
directed-arc capacity convention, let(d⋆, f⋆), together withg⋆ under netting, be an optimal WDP
allocation, and choose any optimal dual of the corresponding WDP. The payments(6)obtained
from its conservation potentials support a core outcome.
Proof.We give the duals and the complementary-slackness argument explicitly. Throughout the
proof,i∈I,b∈ B i, anda∈ Phas reference orientationa + = (ua, va)and reverse orientation
a− = (v a, ua). The dual variables of the atomic and total bid bounds areαb ≥0andβ i ≥0.
The conservation potentialsπi,n are free. Define
µb(π) =c s ob,i +π i,ni −π i,ob.(7)
Under netting, the exact dual of the grand-coalition instance of (1) is
(Dnet) min π,τ,λ,α,β
X
a∈P
(¯q+ a λ+ a + ¯q− a λ− a ) + X
i∈I

 X
b∈Bi
qbαb +Q T i βi


s.t. α b +β i +µ b(π)≥v b ∀i, b∈ Bi,
τa +π i,ua −π i,va ≥0∀i, a,
−τ a +π i,va −π i,ua ≥0∀i, a,
λ+ a −τ a ≥ −ct,+ a ∀a,
λ− a +τ a ≥ −ct,− a ∀a,
λ+, λ−, α, β≥0, π, τfree.
(8)
Indeed, the five displayed constraint groups are respectively the dual constraints associated with
the primal variablesd b, f+ i,a, f− i,a, g+ a , andg − a . Notice that the second and third inequalities are
opposites. Hence every feasible netting dual satisfies
τa =π i,va −π i,ua ∀i, a.(9)
Under separate directed-arc capacities, the net-flow variablesg± andτare absent, transport
cost is paid on the bidder flows, and the exact dual is
19

(Ddir) min π,λ,α,β
X
a∈P
(¯q+ a λ+ a + ¯q− a λ− a ) + X
i∈I

 X
b∈Bi
qbαb +Q T i βi


s.t. α b +β i +µ b(π)≥v b ∀i, b∈ Bi,
λ+ a +π i,ua −π i,va ≥ −ct,+ a ∀i, a,
λ− a +π i,va −π i,ua ≥ −ct,− a ∀i, a,
λ+, λ−, α, β≥0, πfree.
(10)
The primal is feasible (take every variable equal to zero), and its objective is bounded above
because everyP i is bounded and all costs are nonnegative. Hence both formulations have opti-
mal primal and dual solutions, strong duality holds, and any optimal primal–dual pair satisfies
complementary slackness. Fix such a pair and henceforth add⋆to all of its variables.
Bidder optimality.At pricesµ ⋆ b =µ b(π⋆), bidderi’s maximum attainable surplus is
Ui(µ⋆) = max di∈Pi
X
b∈Bi
(vb −µ ⋆ b )db.(11)
The exact dual of this bidder problem is
min
α,β



X
b∈Bi
qbαb +Q T i βi :α b +β i ≥v b −µ ⋆ b , α b, βi ≥0


 .(12)
This is exactly bidderi’s block of either global dual. The relevant complementary-slackness
equations are
α⋆ b (qb −d ⋆ b ) = 0, β ⋆ i

QT i − X
b
d⋆ b
!
= 0,(13)
d⋆ b  α⋆ b +β ⋆ i +µ ⋆ b −v b  = 0.(14)
They show thatd ⋆ i and((α ⋆ b )b∈Bi, β⋆ i )are feasible for (11) and (12) and have equal objectives.
Consequentlyd ⋆ i solves the bidder problem, and
ui =V i(d⋆ i )−µ ⋆ ·d ⋆ i =U i(µ⋆)≥0,(15)
where nonnegativity follows becausedi = 0is feasible.
20

Network optimality under netting.Callanonnegativeprofiley= (y i)i∈I deliverableifthenetwork
constraints admit flows that inject and withdraw its quantities; the bid-region constraintsyi ∈P i
are not imposed on this network production set. Letybe any such profile, and letbf ,bgbe any
netting-feasible flows delivering it. Multiplying bidderi’s conservation equations byπ ⋆ i,n and
summing over nodes gives the identity
X
b∈Bi
(π⋆ i,ni −π ⋆ i,ob)yb = X
a∈P
h
(π⋆ i,va −π ⋆ i,ua) bf + i,a + (π⋆ i,ua −π ⋆ i,va) bf − i,a
i
.(16)
Using (7), (9), and the net-flow identity, the network’s revenue net of source and transfer cost is
therefore
µ⋆ ·y− X
i,b
cs ob,iyb − X
a
(ct,+ a bg+ a +c t,− a bg− a )
=
X
a

(τ ⋆ a −c t,+ a )bg+ a + (−τ⋆ a −c t,− a )bg− a 
≤
X
a
(λ+⋆ a bg+ a +λ −⋆ a bg− a )≤ X
a
(λ+⋆ a ¯q+ a +λ −⋆ a ¯q− a ).(17)
The first inequality is precisely the last two constraint groups ofDnet, and the second uses primal
capacity feasibility. At the optimal flow both inequalities are equalities. Indeed, complementary
slackness gives
g+⋆ a (λ+⋆ a −τ ⋆ a +c t,+ a ) = 0, λ +⋆ a (¯q+ a −g +⋆ a ) = 0,
g−⋆ a (λ−⋆ a +τ ⋆ a +c t,− a ) = 0, λ −⋆ a (¯q− a −g −⋆ a ) = 0.
Network optimality under directed capacities.For any directed-feasible(y,bf), the same potential
identity and the two arc constraints ofDdir yield
µ⋆ ·y− X
i,b
cs ob,iyb − X
i,a
(ct,+ a bf + i,a +c t,− a bf − i,a)
≤
X
a

λ+⋆ a X
i
bf + i,a +λ −⋆ a X
i
bf − i,a
!
≤
X
a
(λ+⋆ a ¯q+ a +λ −⋆ a ¯q− a ).(18)
For example, the coefficient ofbf + i,a on the first line isπ⋆ i,va −π ⋆ i,ua −c t,+ a , which is at mostλ+⋆ a by
Ddir; the reverse direction is identical. Complementary slackness,
21

f +⋆ i,a (λ+⋆ a +π ⋆ i,ua −π ⋆ i,va +c t,+ a ) = 0, λ +⋆ a (¯q+ a − X
i
f +⋆ i,a ) = 0,
f −⋆ i,a (λ−⋆ a +π ⋆ i,va −π ⋆ i,ua +c t,− a ) = 0, λ −⋆ a (¯q− a − X
i
f −⋆ i,a ) = 0,
makes both inequalities in (18) equalities at the optimal flow.
Thus, under either convention, ifC(y)denotes the minimum source and transport cost of
deliveringy, then
R(µ⋆) := max
ydeliverable
{µ⋆ ·y−C(y)}= X
a∈P
(λ+⋆ a ¯q+ a +λ −⋆ a ¯q− a ).(19)
The maximum is attained byd⋆ and its optimal flow. Since payments cover source and transfer
costs as pass-throughs, the auctioneer retains exactly this network profit:
u0 =
X
i
pi −C(d ⋆) =R(µ ⋆)≥0.(20)
The core inequalities.Equations (15) and (20), along with strong duality, give payoff feasibility:
u0 +
X
i∈I
ui =
X
i∈I
Vi(d⋆ i )−C(d ⋆) =w(I).
Now fix a coalitionS⊆Iand any profiled= (d i)i∈S that it can deliver, settingdi = 0outside
S. Then
X
i∈S
Vi(di)−C(d) =
X
i∈S

Vi(di)−µ ⋆ ·d i  +  µ⋆ ·d−C(d) 
≤
X
i∈S
Ui(µ⋆) +R(µ ⋆) = X
i∈S
ui +u 0.
The first bound uses bidder optimality separately for everyi∈Sand network optimality for the
coalition’s deliverable profile. Maximising the left side over all coalition-feasible profiles gives
w(S)≤u 0 +
X
i∈S
ui,
which is the core constraint. Together with payoff feasibility and individual rationality, this
proves the result in the general model.
Remark24 (Degeneracy).Theorem 23 shows every optimal dual yields acorepoint; under
degeneracy the dual is non-unique, so thepayment vectoris not unique – a choiceamongcore
22

points, not a threat to core membership. A canonical selection (lexicographic, or the bidder-
optimal core point of Day and Milgrom (2008), computed for instance by the quadratic core-
selecting rule of Day and Cramton (2012)) can be layered on top for determinacy and fairness.
6.3.3. Illustrative examples
We reuse the series network of Example 19 and then exhibit the counter-directed (credit) case.
In the following examples, we work with reduced WDP formulations obtained by eliminating flow
variables through conservation equations and omitting redundant constraints. These formula-
tions are exact projections of the corresponding full WDPs. Moreover, the optimal reduced
dual solutions considered below admit objective-preserving extensions to the full WDP duals, as
verified by the explicit construction of conservation potentials. Consequently, the resulting dual
prices are valid for the original market.
Example 25(Dual pricing repairs Example 19).Let us first recall the primal problem written
in full in the case of example . Usingx, y, z∈[0,1]for the accepted quantities (each also the
flow of that bidder), the WDP (after dropping redundant constraints) becomes
w(I) = max 2x+ 2y+ 2z
s.t.x+y≤1 (λ 1), x+z≤1 (λ 2),0≤x, y, z≤1 (α X , αY , αZ).
(21)
As discussed earlier, the unique optimum is
x⋆ = 0, y ⋆ =z ⋆ = 1, w(I) = 4.
The LP dual of (21) is
minλ 1 +λ 2 +α X +α Y +α Z
s.t.α X +λ 1 +λ 2 ≥2
αY +λ 1 ≥2, α Z +λ 2 ≥2
λ, α≥0.
(22)
Using the optimal primal, complementary slackness determines the optimal duals:
(i)y ⋆ = 1>0: they-constraint is tight,α Y = 2−λ 1; sinceα Y ≥0,λ 1 ≤2. Likewisez ⋆ >0
givesα Z = 2−λ 2 andλ 2 ≤2.
(ii)x ⋆ = 0<1: the cap ofXis slack, soα X = 0, and dual feasibility forxbecomesλ1 +λ 2 ≥2.
(iii) Both capacity constraints are tight at the primal optimum, soλ1, λ2 may be positive.
23

For any such(λ1, λ2)the dual objective equalsλ 1 +λ 2 + 0 + (2−λ 1) + (2−λ 2) = 4 =w(I), so
all of them are optimal. Hence the set of optimal duals is
Λ⋆ =  (λ1, λ2) : 0≤λ 1 ≤2,0≤λ 2 ≤2, λ 1 +λ 2 ≥2 	 ,(23)
withα X = 0,α Y = 2−λ 1,α Z = 2−λ 2. In words: each edge price is at most2because the
accepted bidder who uses it alone values it at2, and the two prices together are at least2because
the rejected bidderX, who needs both, values the pair at2. The dual is degenerate: the primal
optimum is a vertex at which more constraints are tight than there are variables.
Let us use the following two observations
•O1: Complementary slackness in the general directed WDP for a flow variable says: if
bidderiships a positive amount on arc(u, v), then
πi,v −π i,u =c t (u,v) +λ (u,v).
Summing along the path a unit actually uses, the potential difference between inlet and
sink equalstotal transfer cost plus total congestion price along the path. Hence
µb =c s ob,i|{z}
supplier
+ P e∈path ct e | {z }
TSOs
+ P e∈path λe | {z }
capacity charge
.
Under netting, the dual forces one common price gapτa per physical pipeafor all bidders,
and the same decomposition holds withτa in place ofct +λ(a unit travellingagainstthe
reference orientation picks up−τa).
•O2: For each licence, the dual hasαb ≥0(shadow value of its capqb) withαb +βi +µb ≥v b,
and complementary slackness gives:
–a licence accepted at a positive level satisfiesvb =µ b +α b +β i, henceµ b ≤v b (no total
caps bind in the examples, soβi = 0);
–a licence accepted strictly below its cap hasαb = 0, henceµb ≥v b if rejected andµb =v b
if partially accepted.
Potentials and nodal prices.All costs are zero, so by O1 a common potential can be chosen for
all bidders:
π1 = 0, π 2 =λ 1, π 3 =λ 1 +λ 2.
(Bidder-specific potentials could differ only forX, who ships nothing and pays nothing, so this
choice is without loss for the payments.) The nodal prices are
µX =π 3 −π 1 =λ 1 +λ 2, µ Y =π 2 −π 1 =λ 1, µ Z =π 3 −π 2 =λ 2,
24

with all source prices zero. O2 is visible directly: the rejectedXfacesµX ≥2 =v X; the accepted
Y, Zfaceµ Y , µZ ≤2.
Payments, utilities and revenue.OnlyYandZreceive gas, so
pY =λ 1, p Z =λ 2, p X = 0,
and since there are no source or transfer costs, the payments are pure capacity charges. Utilities
and auctioneer revenue:
uX = 0, u Y = 2−λ 1, u Z = 2−λ 2, u 0 =p Y +p Z =λ 1 +λ 2,
andu 0 =λ 1 ·1 +λ 2 ·1is exactly the congestion rent P e λe ¯qe. Payoffs add up to the welfare:
u0 +u X +u Y +u Z = (λ1 +λ 2) + 0 + (2−λ 1) + (2−λ 2) = 4.
The core.Writep Y , pZ for the payments. Since the payoffs sum to4, the core constraints
u0 + P i∈S ui ≥w(S)read:
coalition with0 u0 + P i∈S ui w(S) condition
{0} pY +p Z 0 pY +p Z ≥0
{0, X} pY +p Z 2 pY +p Z ≥2
{0, Y} 2 +p Z 2 pZ ≥0
{0, Z} 2 +p Y 2 pY ≥0
{0, X, Y} 2 +p Z 2 pZ ≥0
{0, X, Z} 2 +p Y 2 pY ≥0
{0, Y, Z} 4 4 —
{0, X, Y, Z} 4 4 — (feasibility)
Together with individual rationality (uY , uZ ≥0, i.e.p Y , pZ ≤2), the core in payment space is
C=

(pY , pZ) : 0≤p Y ≤2,0≤p Z ≤2, p Y +p Z ≥2

.
Comparing with (23): underpY =λ 1,p Z =λ 2 the set of dual-price outcomes coincides with the
corein this example (Figure 4). The only binding economic condition is the one for{0, X}: the
auctioneer together with the rejected bidder could sell the two edges toXfor2, soYandZ
together must pay at least2.
25

Why VCG fails here.VCG chargesYits externality. WithoutY, the others obtainw({X, Z}) =
2; withYpresent they obtainw(I)−2 = 2; hencep VCG Y = 0, and symmetricallypVCG Z = 0. The
point(0,0)violatesp Y +p Z ≥2: the coalition{0, X}blocks. Each ofYandZis individually
not pivotal (removing one of them,Xstill cannot be served because the other occupies an edge),
but jointly they displaceX. Dual prices cannot make this mistake, because the price of the path
1→3isµ X =λ 1 +λ 2, which must coverX’s value wheneverXis rejected.
pY =λ 1
pZ =λ 2
1
1
2
2
VCG
symmetric
seller-optimal
C= Λ ⋆
Figure 4: Series example: the coreC(shaded) and the set of dual-price outcomesΛ ⋆ coincide. The segment
pY +p Z = 2is the set of bidder-optimal core points; VCG lies outside.
Example 26(A consumer earns a credit under netting).Let us assume a line1−2−3, pipes
e1 ={1,2}ande 2 ={2,3}with reference orientations1→2and2→3respectively, zero
transfer costs, and netting convention.q + e1 = ¯q− e1 = 10units (it will be uncongested), while
¯q+ e2 = ¯q− e2 = 1. An open source at node1sells gas at price2.
bidder inlet sink valuationvsource price net value
A1 3 10 2 8
B1 3 8 2 6
C1 3 6 2 4
D3(own gas)1 3 0 3
Each licence has quantity1.Dis a positioned shipper: it holds its own gas at node3, whose
acquisition cost is sunk, so its source price in the model iscs 3,D = 0; the node-3gas isnotan
open source forA, B, C.
The winner-determination LP and its solution.Writea, b, c, d∈[0,1]for the accepted quantities.
Source payments are pass-throughs, so the welfare objective uses net values. Under netting, the
capacity constraint ofe2 applies to thenetforward flow, i.e. the forward shipments ofA, B, C
26

1 2 3
A, B:2units
D:1unit
A, B:2units
D:1unit
source, price2
D’s sink
sinks ofA, B, C
D’s gas
net flow one2:2−1 = 1 = ¯q + e2
Figure 5: Optimal gross flows. Under netting only the net forward flow2−1 = 1counts against the capacity of
e2.
minus the backward shipment ofD:
w(I) = max 8a+ 6b+ 4c+ 3d
s.t.a+b+c−d≤1 (λ),0≤a, b, c, d≤1 (α A, . . . , αD)
(24)
(the backward-capacity constraintd−(a+b+c)≤¯q − e2 and the constraints ofe1 never bind and
are omitted).
AcceptingDis worth3directlyandraises the room for forward shipments from1to2. The
best use of two forward units isAandB(8 + 6), so
a⋆ =b ⋆ =d ⋆ = 1, c ⋆ = 0, w(I) = 8 + 6 + 3 = 17.
(WithoutD, only one forward unit fits and it goes toA: welfare8.) The relevant coalition values
are as
S {A} {B} {D} {A, B} {A, D} {B, D} {A, B, C} {A, B, D}I
w(S) 8 6 3 8 11 9 8 17 17
Note thatwis not submodular: the marginal value ofBis0when added to{A}but6when
added to{A, D}.BandDare complements, becauseD’s counterflow creates the room thatB
uses.
The dual and all its optimal solutions.The dual of (24) is
minλ+α A +α B +α C +α D
s.t.α A +λ≥8, α B +λ≥6, α C +λ≥4, α D −λ≥3, λ, α≥0.
(25)
Note the sign inD’s constraint:denters the capacity constraint with coefficient−1. Comple-
mentary slackness gives:
(i)a ⋆, b⋆, d⋆ >0: their constraints are tight, soα A = 8−λ,α B = 6−λ,α D = 3 +λ.
Nonnegativity ofα B givesλ≤6.
27

(ii)c ⋆ = 0<1:α C = 0, and feasibility forcgivesλ≥4.
The dual objective is thenλ+ (8−λ) + (6−λ) + 0 + (3 +λ) = 17 =w(I)for everyλ∈[4,6].
Hence
λ⋆ ∈[4,6] :(26)
the congestion price lies between the net value of the bestrejectedforward bidder (C,4) and
that of the worstacceptedone (B,6), the usual uniform-price interval. WithoutDthe optimum
serves onlyAand the optimal duals areλ∈[6,8](betweenBandA).
WithoutDthe marginal forward unit isB’s, which is rejected, soλ≥6. WithD,Bis
accepted andCbecomes the marginal rejected bidder, so the price range moves down to[4,6].
More capacity (here created by counterflow) means a lower scarcity price.
Potentials and nodal prices.In the netting dual of the general WDP, each physical pipeahas one
free price gapτa =π i,va −πi,ua, common to all bidders, withλ+ a −τa ≥ −ct,+ a andλ − a +τa ≥ −ct,− a ,
and complementary slackness on the net-flow variablesg± a :
•Pipee 1: net forward flowg + e1 = 2−1 = 1>0, below capacity, soλ + e1 = 0andτ e1 =
ct,+ +λ + e1 = 0.
•Pipee 2: net forward flowg+ e2 = 1 = ¯q+ e2, soτ e2 =c t,+ +λ + e2 =λwithλ∈[4,6]; the backward
direction is slack,λ− e2 = 0.
Normalisingπ i,1 = 0for each bidder givesπ i,2 = 0andπ i,3 =λfor alli. The nodal prices are
µA =µ B =µ C =c s 1,· +π ·,3 −π ·,1 = 2 +λ,
µD =c s 3,D +π D,1 −π D,3 = 0 + 0−λ=−λ.
D’s unit travels against the reference orientation ofe2, so it picks up−τe2 =−λ: the reversed
spread.
Payments, decomposition and revenue.
bidder paymentp i =µ i to supplier to TSOs capacity charge utilityu i
A 2 +λ 2 0λ 10−(2 +λ) = 8−λ
B 2 +λ 2 0λ 8−(2 +λ) = 6−λ
C 0 (rejected) 0 0 0 0
D −λ 0 0−λ 3−(−λ) = 3 +λ
total 4 0λ
28

Withλ= 4:AandBeach pay6(of which4is the capacity charge), andDis paid4, so its
utility is3 + 4 = 7.
Revenue adequacy.The auctioneer keeps the capacity charges:u0 =λ+λ−λ=λ. This equals
the congestion rentλ + e2 ¯q+ e2 =λ·1, as the dual-pricing rule guarantees in general. Forλ= 4:
4 + 4−4 = 4. The credit toDis financed out of the forward shippers’ capacity charges; supplier
and TSO payments are untouched.
Feasibility.u 0 + P i ui =λ+ (8−λ) + (6−λ) + 0 + (3 +λ) = 17 =w(I)for everyλ∈[4,6].
The core.For eachλ∈[4,6]the dual-price payoffs areu= (8−λ,6−λ,0,3 +λ),u 0 =λ. All
16core inequalities hold for everyλ∈[4,6], as theorem 23 for dual pricing predicts. Atλ= 4
the coalitions{0, A}and{0, B}are tight.
Comparison with VCG.Here VCG also paysD, and more. The VCG capacity charges are
CCA =w({B, C, D})−(17−8) = 13−9 = 4,
CCB =w({A, C, D})−(17−6) = 15−11 = 4,
CCC =w({A, B, D})−17 = 0,
CCD =w({A, B, C})−(17−3) = 8−14 =−6.
SoDreceives6under VCG, but the auctioneer collects only4 + 4−6 = 2, and the coalition
{0, A}blocks:u 0 +u A = 2 + (8−4) = 6<8 =w({A})(so do{0, B}and{0, C}). This is the
complementarity betweenBandD: VCG rewardsDwith its full marginal contribution, which
includesB’s value, and the total is too generous. Under the dual pricesDreceivesλ∈[4,6],
and the auctioneer keeps the congestion rent.
7. Discussion
The results presented above leave several design choices open, and we discuss the most im-
portant of them in turn.
A first set of questions concerns incentives. Core stability and dominant-strategy incentive
compatibility cannot, in general, be obtained simultaneously: VCG secures the latter but, as
Example 19 shows, not necessarily the former, whereas dual pricing secures the core at the price
of dominant-strategy incentive compatibility. Under the payment rule (6), truthful bidding is
optimal for a price-taking bidder, that is, for a bidder who treats the nodal pricesµ⋆ as given.
This is the natural benchmark in markets with many participants, but a large bidder that is
pivotal on a congested edge can, in principle, influence the dual prices through its bids. When
29

the dual is degenerate and the payment vector is therefore not unique (Remark 24), selecting the
bidder-optimal core point (Day & Cramton, 2012; Day & Milgrom, 2008) minimises the residual
incentive to deviate and is the natural refinement of the rule. Whether such a canonical core
selection can be obtained in closed form from the duals of the winner-determination problem,
rather than by solving a secondary optimisation problem, remains an open question.
A second design choice concerns counter-directed flows. Throughout the paper we have
carried two capacity conventions, netting and separate directed arcs. In the restricted model
the two conventions coincide (Corollary 14), so the choice is immaterial there. In the general
model, netting yields weakly higher welfare but admits negative payments, that is, credits for
counterflow (Example 26), whereas the directed-arc convention excludes such credits at some
welfare cost. The latter is arguably closer to regulatory practice, since EU entry–exit capacity
is booked per directed point. As the nodal pricing rule is well defined under both conventions,
we make the choice explicit rather than resolve it, and leave it to the regulator.
The scope of the mechanism is determined by the nature of the transported good. Replacing
route enumeration by routing within the winner-determination problem is sound because gas
is fungible: any unit delivered to a bidder’s sink is as good as any other, so the mechanism is
free to choose and split paths. Where the good is an intrinsically rigid bundle – a train path
occupying a specific sequence of track segments and time slots (Stojadinović et al., 2019), or an
all-or-nothing wavelength – the relaxation underlying the OD language is no longer exact: the
route bundle constitutes a genuine complementarity, the winner-determination problem acquires
integrality constraints, and both the exactness of the dual prices and the core-stability guarantee
may be lost. Our results are therefore sharpest for divisible and substitutable transport services
such as gas or bandwidth.
Finally, the two shortcomings of the convex combinatorial auction of Csercsik (2022) ad-
dressed in this paper share a common origin. Route-based bidding hard-codes bundles that the
mechanism should be free to form or dissolve: a route is an indivisible combination of edges, and
an inlet-specific bid fixes the origin of the gas. The OD language dissolves the route bundle and
thereby closes the efficiency gap illustrated in Example 17. Departures from source indifference,
whether through dedicated sources or through inlet-specific caps, may expose a residual comple-
mentarity between bidders; these are precisely the situations in which VCG may leave the core,
and in which the flow-conservation duals restore core stability.
30

8. Conclusion and future work
This paper analyses the problem of transport capacity allocation in capacity-constrained
networks through auctions in which participants bid for delivery rather than for individual ca-
pacity products. Addressing the flaws of the convex combinatorial auction framework presented
in Csercsik (2022), we showed that requiring bidders to enumerate their routes in advance may
lead to strictly inefficient allocations, and we proposed an origin–destination bidding language
in which bidders specify where gas may enter and where it is to be delivered, while the routing
is determined by a network-flow linear program. Because this winner-determination problem
remains a linear program of polynomial size, the language attains the welfare of complete route
enumeration without its combinatorial burden.
On the payment side, we identified source indifference as the boundary of a positive result.
When sources are openly accessible at uniform prices and bidders value only the quantity de-
livered to their own sink, some optimal aggregate flows never use a pipe in both directions, the
winner-determination problem reduces to a single-commodity flow, and an elementary argument
based on node potentials shows that the coalition value is submodular in the set of bidders;
consequently, the VCG outcome lies in the core. Once bidders face consumer-specific access to
sources or inlet-specific quantity caps, this property may fail and VCG payments may lie strictly
outside the core. For this general setting we proposed a dual (nodal) pricing rule derived from
the shadow prices of the flow-conservation constraints, and proved that every optimal dual yields
a core outcome under both capacity conventions considered, with the auctioneer’s revenue equal
to the congestion rent of the binding capacity constraints.
8.1. Future work
Several directions remain open. First, the analysis has been illustrated on stylised examples;
applying the mechanism to a realistic network, such as the European gas transmission system,
would require the estimation of inverse demand functions and would allow a quantitative com-
parison with current allocation practice. Second, the incentive properties of dual pricing deserve
further study, including the extent to which large bidders can influence nodal prices and the com-
putation of a canonical core point. In addition, the present model treats consumers as the only
strategic participants; including producers on the supply side leads to a combinatorial double
auction over origin–destination licences, which may be considered as a natural extension of the
current work. Furthermore, the model used in the current work assumed a steerable medium, an
assumption that does not hold for electricity-type infrastructure networks, where the physical
properties of the network elements determine the resulting flows for a given input-output pat-
31

tern. Studying the problem of auction-based capacity allocation in Kirchoff-type networks can
also mean a plausible continuation of the current wok.
Acknowledgements
Dávid Csercsik thanks Robert Day for discussions about the flaws and limitations of the
original convex combinatorial auction (Csercsik, 2022) during the Dagstuhl 2025 Seminar series.
Funding
Gergely Csáji was supported by the Ministry of Innovation and Technology of Hungary from
the National Research, Development and Innovation Fund, by grants STARTING 153093 and
FK 145838.
CRediT authorship contribution statement
Gergely Csáji:Methodology, Formal analysis, Validation, Writing - Original Draft, Writing
- Review & Editing, Visualization.Dávid Csercsik:Conceptualization, Methodology, Valida-
tion, Writing - Original Draft, Writing - Review & Editing.
Declaration of competing interest
The authors declare that they have no known competing financial interests or personal rela-
tionships that could have appeared to influence the work reported in this paper.
Declaration of generative AI and AI-assisted technologies in the manuscript prepa-
ration process
DuringthepreparationofthisworktheauthorsusedClaude(Anthropic)tosupportliterature
research, language improvement and formatting of the manuscript. After using this tool, the
authors reviewed and edited the content as needed and take full responsibility for the content of
the published article.
References
Ausubel, L. M., & Milgrom, P. (2002). Ascending auctions with package bidding.Frontiers of
Theoretical Economics,1(1), Article 1. https://doi.org/10.2202/1534-5963.1019
Ausubel, L. M., & Milgrom, P. (2006). The lovely but lonely Vickrey auction. In P. Cramton,
Y. Shoham, & R. Steinberg (Eds.),Combinatorial Auctions(pp. 17–40). MIT Press.
32

Belzarena, P., Ferragut, A., & Paganini, F. (2009). Network bandwidth allocation via dis-
tributed auctions with time reservations. InProceedings of IEEE INFOCOM 2009,
the 28th Conference on Computer Communications.Rio de Janeiro, Brazil: IEEE.
https://doi.org/10.1109/INFCOM.2009.5062238
Bikhchandani, S., & Ostroy, J. M. (2002). The package assignment model.Journal of Economic
Theory,107(2), 377–406. https://doi.org/10.1006/jeth.2001.2957
Bilgin, M. (2009). Geopolitics of European natural gas demand: Supplies from Russia, Caspian
and the Middle East.Energy Policy,37(11), 4482–4492. https://doi.org/10.1016/j.enpol
.2009.05.070
Clarke, E. H. (1971). Multipart pricing of public goods.Public Choice,11, 17–33.
https://doi.org/10.1007/BF01726210
Csercsik, D. (2022). Convex combinatorial auction of pipeline network capacities.Energy
Economics,111, 106084. https://doi.org/10.1016/j.eneco.2022.106084
Day, R. W., & Cramton, P. (2012). Quadratic core-selecting payment rules for combinatorial
auctions.Operations Research,60(3), 588–603. https://doi.org/10.1287/opre.1110.1024
Day, R. W., & Milgrom, P. (2008). Core-selecting package auctions.International Journal of
Game Theory,36(3–4), 393–407. https://doi.org/10.1007/s00182-007-0100-7
Groves, T. (1973). Incentives in teams.Econometrica,41(4), 617–631. https://doi.org/10.2307/
1914085
Keller, J. T., Kuper, G. H., & Mulder, M. (2019). Mergers of Germany’s natural gas mar-
ket areas: Is transmission capacity booked efficiently?Utilities Policy,56, 104–119.
https://doi.org/10.1016/j.jup.2018.11.005
Kelly, F. P., Maulloo, A. K., & Tan, D. K. H. (1998). Rate control for communication networks:
Shadow prices, proportional fairness and stability.Journal of the Operational Research
Society,49(3), 237–252. https://doi.org/10.1057/palgrave.jors.2600523
Maillé, P., & Tuffin, B. (2007). Why VCG auctions can hardly be applied to the pricing
of inter-domain and ad hoc networks. In3rd EuroNGI Conference on Next Generation
Internet Networks (NGI 2007)(pp. 36–39). Trondheim, Norway. https://doi.org/10.1109/
NGI.2007.371195
Moulin, H., & Shenker, S. (2001). Strategyproof sharing of submodular costs: Budget balance
versus efficiency.Economic Theory,18(3), 511–533. https://doi.org/10.1007/PL00004200
Shahmohammadi, M., Fakhrzad, M. B., Hosseini Nasab, H., & Ghannadpour, S. F. (2024).
An intelligent auction-based capacity allocation algorithm in shared railways.Journal of
Ambient Intelligence and Humanized Computing,15(4), 2565–2579. https://doi.org/10
33

.1007/s12652-024-04773-3
Shapley, L. S., & Shubik, M. (1971). The assignment game I: The core.International Journal
of Game Theory,1(1), 111–130. https://doi.org/10.1007/BF01753437
Stojadinović, N., Bošković, B., Trifunović, D., & Janković, S. (2019). Train path congestion
management: Using hybrid auctions for decentralized railway capacity allocation.Trans-
portation Research Part A: Policy and Practice,129, 123–139. https://doi.org/10.1016/
j.tra.2019.08.013
Takácsné Tóth, B., Kotek, P., & Kaderják, P. (2017).Evaluating the 6 March
PRISMA capacity auctions(Tech. Rep.). Regional Centre for Energy Policy Re-
search (REKK). Retrieved fromhttps://rekk.hu/article/145/evaluating-the-6
-march-prisma-capacity-auctions
Tierney, S. F., Schatzki, T., & Mukerji, R. (2008).Uniform-pricing versus pay-as-bid in wholesale
electricity markets: Does it make a difference?(Tech.Rep.). NewYorkIndependentSystem
Operator.
Vickrey, W. (1961). Counterspeculation, auctions, and competitive sealed tenders.The Journal
of Finance,16(1), 8–37. https://doi.org/10.1111/j.1540-6261.1961.tb02789.x
34
