---
title: Unified Sharp Bounds on Probabilities of Causation
url: https://arxiv.org/abs/2610.27398
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Xin Shu
- Ang Li
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.27398
pages: 13
chars: 37341
fetched_at: '2026-11-08T13:31:09+00:00'
kb_version: 1
---

# Unified Sharp Bounds on Probabilities of Causation

Unified Sharp Bounds on Probabilities of Causation
Xin Shu Ang Li
Department of Computer Science, Florida State University
xs24a@fsu.edu, angli@cs.fsu.edu
Abstract
Probabilities of causation (PoCs) have developed steadily, from the binary mea-
sures first introduced by Pearl to the non-binary setting recently studied by Shu et
al. As the theory has matured, PoCs have found applications in a growing range
of areas, including personalized medicine, marketing and legal attribution. Shu et
al. proposed closed-form bounds for multi-valued treatments and outcomes and
proved them valid, but left their sharpness in high dimensions open. We close
this gap with a mathematical proof. We further show thatPNS,PSub,PRepand
PNare all special cases of a single, more general formula. Combined with their
equivalence classes, this settles the question of sharp bounds for discrete PoCs
from experimental and observational data: in every dimension, they are given in
closed form by a single theorem.
1 Introduction
Many decisions turn on how a particular individual would respond to different treatments, not on
how the population responds on average. A retailer may want to know whether a customer would
buy at one price but not at another; a marketer may want to know whether someone would answer an
e-mail campaign but ignore a phone call. Questions of this kind are probabilities of causation (PoCs)
[Pearl, 1999]. They concern a unit’s outcomes under several treatments at once, and since we never
observe more than one of these for the same unit, PoCs are in general not point-identified. Experi-
mental dataP(y ixj )and observational dataP(x j, yi)only determine an interval, and the quantity of
interest is thesharpinterval, i.e. the set of all values consistent with the data.
When treatment and outcome are binary, the sharp bounds have long been known [Tian and Pearl,
2000]. They were derived with Balke’s linear-programming method [Balke, 1995, Balke and Pearl,
1997] and later proved analytically [Li and Pearl, 2019, 2022]. Once the variables take more than
two values, things get harder. Balke’s program still applies, but it needs one variable for every pair
of response type and received treatment, which forn-valued variables meansn n ·nvariables. It
can therefore only be solved for smalln, and it gives no closed form. Zhang et al. [2022] solve an
optimisation problem for each instance, and Li and Pearl [2024] give recursive bounds that are valid
but not sharp. Shu et al. [2026] derived closed-form bounds for four families of PoCs,PNS(k),
PSub(k, p),PRep(k, q)andPN(k, p, q), and showed that equivalence classes and relabelling re-
duce general discrete PoCs to these four. They proved the bounds valid in every dimension and
checked numerically that they are sharp for three- and four-valued variables, but whether they are
sharp in general was left as a conjecture. The difficulty is that a direct proof has to handle the vertices
of a polytope whose dimension grows faster than exponentially inn.
Contributions.
• We prove that the closed-form bounds of Shu et al. [2026] forPNS(k),PSub(k, p),PRep(k, q)
andPN(k, p, q)are sharp in every dimension.
1
arXiv:2610.27398v1  [cs.AI]  19 Oct 2026

• We prove two lemmas that make the sharpness proof manageable. The first reduces Balke’s pro-
gram fromn n ·nvariables to2 k ·n, and the second reduces the2 k candidate cuts for the lower
bound to justk+ 2.
• We show that all four families, together with their relabellings, are special cases of one general
formula, which gives the sharp bounds for any such query in closed form.
Section 4 gives the full proof forPNS(k), and extends it to the other three families. Section 5
combines all four into a single theorem.
2 Preliminaries
This section recalls the definitions of probabilities of causation and the notation of structural causal
models (SCMs) [Galles and Pearl, 1998, Halpern, 2000]. Readers who know SCMs can skip it.
In an SCM, counterfactuals have a precise meaning. The statement “Ywould have beenyhadX
beenx” is writtenY x =y, where the subscriptxrefers to a hypothetical intervention. To keep the
notation short, we writey x,y x′,y ′ x andy ′ x′ for the eventsY x =y,Y x′ =y,Y x =y ′ andY x′ =y ′.
Throughout,Xis the treatment andYthe outcome. Unless stated otherwise, experimental data are
causal effects such asP(y x), and observational data are joint probabilities such asP(x, y).
WhenXandYare binary, we writexandx ′ forX=true andX=false, andyandy ′ forY=true
andY=false. Pearl [1999] defined three basic probabilities of causation.
Definition 1(Probabilities of causation [Pearl, 1999]).
PN
∆
=P(y ′ x′ |x, y),PS ∆ =P(y x |y ′, x′),PNS ∆ =P(y x, y′ x′).
PNS is the probability thatyresponds toxin both directions:yoccurs withxand fails to occur
without it. It therefore captures both the sufficiency and the necessity ofxfory. Tian and Pearl
[2000] obtained tight bounds on PN, PS and PNS with Balke’s linear-programming method [Balke,
1995], and Li and Pearl [2019, 2022] later proved these bounds analytically.
Now letXandYeach takenvalues. Li and Pearl [2024] named four multi-valued probabilities of
causation, PNS, PSub, PRep and PN, and gave recursive bounds for them. Shu et al. [2026] kept the
names but rewrote each quantity so that thej-th counterfactual always pairsy j withx j:
PNS(k) =P(y 1x1 , . . . , ykxk )(probability of necessity and sufficiency),
PSub(k, p) =P(y1x1 , . . . , ykxk , xp)(probability of substitute),
PRep(k, q) =P(y1x1 , . . . , ykxk , yq)(probability of replacement),
PN(k, p, q) =P(y1x1 , . . . , ykxk , xp, yq)(probability of necessity),
withk≤nandp̸=jfor1≤j≤k. HerePNS(k)is the probability that the same individual would
have outcomey j underx j for everyj= 1, . . . , k. Shu et al. [2026] derived closed-form bounds for
all four quantities, and by their equivalence-class and replaceability theorems, any discrete PoC can
be brought into one of these four forms. We refer to Shu et al. [2026] for the bounds and the two
theorems, in this paper we prove that the bounds are sharp.
3 Notation and Definition
The treatmentXtakes valuesx 1, . . . , xn and the outcomeYtakes valuesy 1, . . . , yn; as in Shu
et al. [2026], unequal cardinalities are handled by adding values of probability zero. We write
[n] ={1, . . . , n}. The indexiruns over outcomes andj, ℓover treatments;pdenotes an additional
treatment andqan additional outcome.
We work in structural causal models without further structural assumptions, and we reason with
events throughout. With a slight abuse of notation, we writex j for the event{X=x j}, i.e. that the
unit received treatmentx j, andy i for the event{Y=y i}, i.e. that the observed outcome isy i. The
counterfactual eventy ixj means “underx j the outcome would bey i”; for fixedjthese events form
a partition. If we arrange the observational probabilitiesP(x j, yi)in a table with one column per
treatment and one row per outcome, the eventx j is thej-thcolumnand each entryQ ij := (xj, yi)
2

is acell; as forb ij, the first index ofQis the row and the second the column. The columns partition
the sample space, soP(E) = P j P(E, xj)for every eventE.
We now introduce new notations for probabilities:
aij =P(y ixj )(experimental), b ij =P(x j, yi)(observational), c j =P(x j) = P i bij,(1)
The two kinds of data are linked byconsistency[Galles and Pearl, 1998, Pearl, 2009, 2010]: a unit
that receivedx j has outcomey i exactly when its potential outcome underx j isy i, i.e.x j ∩y ixj =
xj ∩y i. Hence
bij =P(Q ij) =P

xj, yixj

.(2)
Acompatible modelis a joint law of a response typeR= (R 1, . . . , Rn)∈[n] n, whereR j :=Y xj ,
and a received treatmentX∈[n], withP(R j =i) =a ij andP(R j =i, X=j) =b ij; the observed
outcome isR X. LetMbe the set of compatible models, assumed non-empty.
A valuer= (r 1, . . . , rn)∈[n] n ofRis also called a response type; it lists an individual’s outcome
under every treatment (r ℓ =imeansy ixℓ holds). It is a function from treatments to outcomes, so there aren n types.
Let’s fix1≤k≤nand put
Aj :=y jxj , S:= T j≤k Aj,
αj :=a jj , β j :=b jj ,
dj :=α j −β j, s j := 1−c j −d j.(3)
By (2),A j ∩x j isthe observed cellQ jj = (xj, yj), soβ j is the only observed part ofA j. ButA j
is defined for every individual, whichever treatment it actually received, so it also has mass outside
columnx j. This mass isd j =P(A j \x j) =P(A j)−P(A j, xj), and it is spread over the other
columnsx ℓ,ℓ̸=j. We write
mjℓ :=P(A j, xℓ)
for the mass ofA j in columnx ℓ. Thusm jj =β j, P ℓ̸=j mjℓ =d j and0≤m jℓ ≤c ℓ. Only the
diagonal entrym jj is observed; forℓ̸=j,m jℓ is not determined by the data.
Each of the four familiesPNS,PSub,PRepandPNhas the formθ=P(S, G)for some factual
eventG, i.e. a union of cells:
PNS(k):G= Ω,PSub(k, p):G=x p,
PRep(k, q):G=y q,PN(k, p, q):G= (x p, yq),(4)
withp > k. HereΩdenotes the whole sample space. Queries with other target outcomes reduce to
these by relabelling. LetΘ :={θ(M) :M∈ M}.
LetG:={(i, ℓ) :Q iℓ ⊆G}be the set of cells that make up the factual eventG(all cells forPNS,
columnpforPSub, rowqforPRep, the single cellQ qp forPN); a pair(i, ℓ)∈ Grefers to rowi
(the observed outcome) and columnℓ(the received treatment). For a response typer∈[n] n, let
W(r) :={j≤k:r j =j} ⊆[k]
record which of the targetsA1, . . . , Ak it satisfies. Call a triple(W, i, ℓ), withW⊆[k]andi, ℓ∈[n],
consistentif, wheneverℓ≤k,ℓ∈W⇐ ⇒i=ℓ. This is consistency: a unit that receivedx ℓ
(ℓ≤k) satisfiesA ℓ if and only if its observed outcome isy ℓ.
Lemma 2.For everyj≤k,
sj = 1−c j −d j ≥0.(⋆)
Proof.Sinceb ij =P(x j, yixj )≤P(y ixj ) =a ij, P i aij = 1and P i bij =c j,
sj = (1−a jj )−(c j −b jj ) =
X
i̸=j
aij −
X
i̸=j
bij =
X
i̸=j
(aij −b ij)≥0.
This inequality is the key to the lower bound: in Lemma 14 it rules out all candidate lower bounds
except the three in Theorem 7.
3

Definition 3.Anadmissible systemis a probability space with a partition into cellsQ iℓ,i, ℓ∈[n],
whereQ iℓ plays the role of the observed cell(x ℓ, yi)and hasP(Q iℓ) =b iℓ; columnsx ℓ := S i Qiℓ; and eventsA 1, . . . , Ak withP(A j) =α j andA j ∩x j =Q jj , the last condition playing the role of
consistency. Thevalueof an admissible system isθ=P(S, G), computed in that system, withG
read as the corresponding union of cells (i.e.G=x p inPSub(k, p)). As before,m jℓ =P(A j, xℓ)
denotes the mass ofA j in columnx ℓ.
The two programs.Recall thatG={(i, ℓ) :Q iℓ ⊆G}is the set of cells that make up the factual
eventG(all cells forPNS, columnpforPSub, rowqforPRep, the single cellQ qp forPN). A
compatible model is determined by the joint probabilitiesP(R=r, X=ℓ)[Balke and Pearl, 1997,
Tian and Pearl, 2000].
Balke’s programtreats each of them as a variableh 1(r, ℓ)≥0, one for every response typer∈[n] n
and received treatmentℓ∈[n], i.e.n n ·nvariables:
max/minθ(h 1) :=
X
r:W(r)=[k]
X
ℓ
1{(rℓ, ℓ)∈ G}h1(r, ℓ)
s.t.
X
r:r j =i
X
ℓ
h1(r, ℓ) =aij,
X
r:r j =i
h1(r, j) =bij (i, j∈[n]).
(5)
An experimental constraint sums over all received treatments, so it only involves the response type
r. An observational constraint looks at a single column, so it also needs the received treatmentℓ. We
cannot dropℓbecause the observational data cannot be written down without it, and they do carry
information. If treatment were assigned independently of the response type, as in a randomized trial,
thenb ij =c j aij and the observational data would tell nothing new. They help only when the choice
of treatment depends on the response type, i.e. under confounding.
Thereduced programhas one variableh 2(W, i, ℓ)≥0for every consistent triple, i.e. at most2k ·n 2
variables:
max/minθ(h 2) :=
X
(i,ℓ)∈G
h2([k], i, ℓ)
s.t.
X
W∋j
X
i,ℓ
h2(W, i, ℓ) =αj (j≤k),
X
W
h2(W, i, ℓ) =biℓ (i, ℓ∈[n]).
(6)
Recall that[n] ={1, . . . , n}. The reduced program keeps the experimental constraints only forajj
(j≤k), and keeps all observational constraints P W h2(W, i, ℓ) =biℓ. It drops everya ij with i̸=j, or whenj > k.
Forj≤k, these constraints and consistency give three more identities. The columnx j has massc j,
the part of it insideA j has massβ j, and the rest has massc j −β j:
X
W
X
i
h2(W, i, j) =cj,
X
W∋j
X
i
h2(W, i, j) =bjj =β j,
X
W̸∋j
X
i
h2(W, i, j) =cj −β j.(7)
The feasible set of (5) is a polytope andθis linear, soΘ = [min Θ,max Θ]and the sharp bounds
are the two optima of (5). Shu et al. [2026] used this program to check sharpness numerically for
n≤4.
Lemma 4(Reduction).For each of the four families, Balke’s program(5)and reduced program(6)
attain exactly the same set of values ofθ. In particular they have the same maximum and the same
minimum, so the sharp bounds can be computed from the reduced program. Equivalently,Θequals
the set of values of admissible systems.
The last sentence holds because they both describe the same thing. In an admissible system, the
eventsA 1, . . . , Ak cut each cellQ iℓ into pieces. Each piece is labelled by the setW⊆[k]of events
that contain it, andh 2(W, i, ℓ)is its mass. Conversely, cutting the cells according to a feasibleh 2
gives an admissible system, see Appendix.
4

Proof idea.Both inclusions are constructive (see Appendix).Merging: given a feasibleh 1, group-
ing the response types byW(r)and by the observed outcome gives a feasibleh 2 with the same
value.Splitting: given a feasibleh 2, we keepW, the observed outcome and the received treatment
of each block fixed, and draw every other coordinater j independently from an explicit distribution
built from the data. The constraints of (6) are exactly what makes the result satisfy all constraints of
(5).
Corollary 5.ForPNS(k),Gcontains all cells, so onlyh 2(W, ℓ) :=P i h2(W, i, ℓ)matters, and the reduced program is equivalent to
max/min P ℓ h2([k], ℓ)
s.t. P W∋j P ℓ h2(W, ℓ) =αj, X
W∋j
h2(W, j) =βj (j≤k),
P
W h2(W, ℓ) =cℓ (ℓ∈[n]),
(8)
with2 k ·nvariables. The sharp bounds onPNS(k)are therefore functions of(α 1, . . . , αk, β1, . . . ,
βk, c1, . . . , cn)alone, data sharing these2k+nnumbers yield the same program as in(8).
The proof of Corollary 5 is in Appendix. The corollary also shortens the equivalence-class argu-
ments of Shu et al. [2026]: adding outcome or treatment values of probability zero leaves(α, β, c)
unchanged up to empty columns.
Sharpness principle.Soundness and attainability together give sharpness.
Lemma 6(Sharpness).If every admissible system has value≤Uand equality holds for at least
one admissible system, thenmax Θ =Uis a sharp upper bound. The same holds with≥L, and
min Θ =Lis a sharp lower bound.
Proof.By Lemma 4,Uis a valid upper bound:θ(M)≤Ufor allM∈ M. Suppose someU ′
satisfied (H1)θ(M)≤U ′ for everyM∈ Mand (H2)U ′ < U. The attaining system gives, via
Lemma 4, a modelM 0 ∈ Mwithθ(M 0) =U, and (H1) applied toM 0 givesU≤U ′ < U, a
contradiction. The lower bound is symmetric.
4 Main results
In this section, we first prove sharpness of the bounds onPNS(k)and then extend it to the other
three families.
4.1 Problem Statement
Soundness of the bounds for all four families,PNS,PSub,PRepandPN, was proved by Shu et al.
[2026]. We prove completeness, which together with soundness shows that the bounds are sharp.
We restate thePNS(k)theorem in our notation below.
Theorem 7(PNS(k)).Forθ=P(y 1x1 , . . . , ykxk ),Θ = [L, U], where
L= max
n
0|{z}
L1
, P j≤k αj −(k−1) | {z }
L2
,max
i≤k

βi + P j≤k, j̸=i(αj +c j −β j)−(k−1) 
| {z }
L3
o
,
U= min
n P
j≤k βj + P ℓ>k cℓ | {z }
U1
,min
j≤k
αj
| {z }
U2
,min
I⊆[k],|I|≥2
1
|I|−1
P
j∈I dj
| {z }
U3
o
.
We writeU 3 over subsetsIto make clear that its indices are distinct. A repeated index would give
an invalid bound.
5

4.2 The upper bound proof
By Lemma 4 we can work with admissible systems, and by Lemma 6 the proof splits into two
parts, soundness (Corollary 9) and attainability (Lemma 11). Soundness was shown by Shu et al.
[2026]; we re-derive it here because the same three properties drive the construction in Lemma 11.
Throughout, letθ ℓ :=P(S, xℓ)denote the part ofθthat lies in columnℓ.
Proposition 8.Every admissible system satisfies:
(Prop1) Pn ℓ=1 θℓ =θ;
(Prop2)0≤θ j ≤β j forj≤k, and0≤θ ℓ ≤c ℓ forℓ > k;
(Prop3)θ−θ j ≤d j forj≤k.
Proof.(Prop1) The columnsx 1, . . . , xn partition the space, soSis the disjoint union of the sets
S∩x ℓ. (Prop2) Forj≤k,S⊆A j givesS∩x j ⊆A j ∩x j, which has massβ j. Forℓ > k,
S∩x ℓ ⊆x ℓ, which has massc ℓ. (Prop3) By (Prop1),θ−θ j =P(S\x j). SinceS⊆A j,
S\x j ⊆A j \x j, which has massα j −β j =d j.
Corollary 9(Soundness).Every admissible system satisfiesθ≤U.
Proof.We derive each of the three upper bounds in Theorem 7 from Proposition 8.
•U 1.By (Prop1) and (Prop2),θ= P j≤k θj + P ℓ>k θℓ ≤ P j≤k βj + P ℓ>k cℓ =U 1.
•U 2.By (Prop3) and (Prop2),θ≤θ j +d j ≤β j +d j =α j for everyj≤k. Henceθ≤
minj≤k αj =U 2.
•U 3.LetI⊆[k]with|I| ≥2. Summing (Prop3) overj∈Igives|I|θ− P j∈I θj ≤ P j∈I dj.
By (Prop1) andθ ℓ ≥0(Prop2), P j∈I θj ≤θ. Hence(|I| −1)θ≤ P j∈I dj, i.e.
θ≤ 1 |I|−1 P j∈I dj. Minimising overIgivesθ≤U 3.
Thereforeθ≤min{U 1, U2, U3}=U.
Lemma 10(Column allocation).Letθ≥0, and for every columnj∈[n]put
θj :=
(θ−d j)+, j≤k,
0, j > k, θj :=
βj, j≤k,
cj, j > k.
There existθ 1, . . . , θn withθ j ∈[θ j, θj]for everyjand Pn j=1 θj =θif and only ifθ≤U.
Proof.The interval[θ j, θj]is exactly the range allowed forθ j by Proposition 8: the upper end
comes from (Prop2), and forj≤kthe lower end comes from (Prop3),θ j ≥θ−d j, together with
θj ≥0.
If every interval is non-empty, the sum P j θj withθ j ∈[θ j, θj]takes exactly the values in P
j θj, P j θj  . Hence a solution exists if and only if the following three conditions hold.
•Every interval is non-empty.Forj > kthis is automatic. Forj≤k,(θ−d j)+ ≤β j ⇐ ⇒θ≤
βj +d j =α j. So this condition isθ≤U 2.
•The upper ends are large enough:θ≤ P j θj = P j≤k βj + P j>k cj =U 1.
•The lower ends are small enough: P j θj = P j≤k (θ−d j)+ ≤θ. Since P j≤k (xj)+ =
maxI⊆[k]
P
j∈I xj, this says|I|θ− P j∈I dj ≤θ, i.e.(|I| −1)θ≤ P j∈I dj, for everyI⊆[k].
This is automatic for|I| ≤1, and for|I| ≥2it isθ≤U 3.
The three conditions together areθ≤min{U 1, U2, U3}=U.
Lemma 11(Attainability).There exists an admissible system withθ=U.
6

N1
N2
N3
T
i Gi
fit:P( T i Gi) = P i gi −2c ℓ
overlap
N1
N2
N3
wrap: T i Gi =∅
Figure 1: Lemma 12 in one column of massc ℓ, witht= 3. We place the complementsN i one after
another on a circle of circumferencec ℓ. If they fit, they do not overlap and the union bound holds
with equality. If they do not fit, they wrap around and cover the whole column, so the intersection is
empty.
Proof.Setθ:=U(a target the construction must hit, not an assumption).
Step 1 (how much ofSlies in each column).By Lemma 10, chooseθ 1, . . . , θn withθ ℓ ∈[θ ℓ, θℓ]
and P ℓ θℓ =U.
Step 2 (how much of eachA j lies in each column).Forj≤kletm jj :=β j and choosem jℓ ∈
[θℓ, cℓ]forℓ̸=j, summing tod j. This is possible because each interval is non-empty (θℓ ≤ θℓ ≤c ℓ),
the lower ends are small enough ( P ℓ̸=j θℓ =U−θ j ≤d j, sinceθ j ≥θ j = (U−d j)+), and the
upper ends are large enough ( P ℓ̸=j cℓ = 1−c j ≥d j by (⋆)). Moreoverm jj =β j = θj ≥θ j.
Henceθ ℓ ≤m jℓ ≤c ℓ for allj, ℓ, andP ℓ mjℓ =β j +d j =α j.
Step 3 (arrangement inside each column).In columnℓplace a blockK ℓ of massθ ℓ. Forℓ≤kput
Kℓ insideQ ℓℓ (possible sinceθ ℓ ≤β ℓ) and setA ℓ ∩x ℓ :=Q ℓℓ. For everyj̸=ℓ, letA j containK ℓ,
and onx ℓ \K ℓ letA j occur independently with probability(m jℓ −θ ℓ)/(cℓ −θ ℓ)∈[0,1]. Then
P(Aj ∩x ℓ) =m jℓ for allj, ℓ, soP(Aj) =α j andA j ∩x j =Q jj : the system is admissible.
EveryA j contains every block, soθ≥ P ℓ θℓ =U. By Corollary 9,θ≤U. Henceθ=U.
By Lemma 6,max Θ =U, so the upper bound ofPNS(k)is sharp.
4.3 The lower bound proof
For the upper bound we could build a maximiser directly, by putting as much mass as possible into
the intersection. The lower bound is harder. If we pushA 1, . . . , Ak apart in one column, their
mass has to go to other columns, where it may overlap with another event, so we cannot treat the
columns one at a time. We therefore take a dual approach. In Section 4.3.1, Fr ´echet bounds in each
column turn the problem into a flow problem. Section 4.3.2 then uses max-flow/min-cut to write the
minimum as a maximum over cuts, and Section 4.3.3 shows that onlyk+ 2of these cuts can be
positive.
Fork= 1,θ=α 1 is identified andL=U=α 1. So we will only consider cases whenk≥2
below.
4.3.1 Column-wise Fr ´echet
Recall that the columnx ℓ has massc ℓ =P(x ℓ) = P i biℓ, the total mass of its cellsQ iℓ = (xℓ, yi), i∈[n].
Lemma 12(Column-wise Fr ´echet [Fr´echet, 1951]).Fix a columnx ℓ and letG 1, . . . , Gt ⊆x ℓ be
events. ThenP( T i Gi)≥ P i P(Gi)−(r−1)c ℓ. Conversely, for any massesg i ∈[0, cℓ]there is
an arrangement insidex ℓ withP(G i) =g i andP( T i Gi) = ( P i gi −(r−1)c ℓ)+. If someG i
must be a union of cells, this is still possible, and arrangements in different columns can be chosen
independently.
7

s
A1
A2
A3
x1
x2
x3
x4
t
d1
d2
d3
f1
f2
f3
f4
capacityc ℓ
Figure 2: The network of Lemma 13 fork= 3,n= 4. EachA j must place massd j =P(A j \x j)
in the columnsx ℓ,ℓ̸=j, at mostc ℓ in each. There is no edge fromA j tox j, because inside its own
columnA j is fixed to the cell of massβ j. Columnx ℓ can absorb up tof ℓ for free, and any inflow
beyond that adds toθ.
Proof.LetN i :=x ℓ \G i be the complement ofG i inside the column. By De Morgan and the union
bound,P( T i Gi) =c ℓ −P( S i Ni)≥c ℓ − P i(cℓ −g i). For the converse, view the column as a circle of circumferencec ℓ and layN 1, . . . , Nr end to end as arcs of lengthscℓ −g i (Figure 1). If they
fit, they are disjoint and the bound is an equality. Otherwise they wrap around and together cover the
whole circle, so every point lies in someN i and T i Gi =∅. If someG i must equal a union of cells (for instanceA j ∩x j = (xj, yj)whenj≤k), its complementN i is the union of the remaining cells
of the column; since only the masses of the cells are prescribed, we place these cells side by side on
the arc assigned toN i, whose length equals their total mass. Finally, distinct columns are disjoint,
so the arrangements in different columns do not interact and can be chosen simultaneously.
By pigeonhole the complements fit disjointly iff the bracket is non-negative, so(·) + is not an artifi-
cial truncation. As in Section 4.2, the inequality holds for every arrangement and gives the bound,
and a suitable arrangement attains it.
4.3.2 Flow and cuts
For the lower bounds withk≥2we use the transportation setT:={m∈R k×n :m jj =
βj, P ℓ̸=j mjℓ =d j,0≤m jℓ ≤c ℓ}. Recall thatd j =α j −β j =P(A j \x j) =P(A j)−P(A j, xj)
is the mass ofA j outside its own columnx j. In the tablem, rowjdescribes howA j is spread over
the columns: its diagonal entry ism jj =β j, and its off-diagonal entriesm jℓ,ℓ̸=j, must add up to
exactlyd j. We also use the column inflowe ℓ := P j≤k, j̸=ℓmjℓ, the mass that the other rows place
in columnℓ; summing over all off-diagonal cells by rows or by columns givesD:= P ℓ eℓ = P j dj.
In the proof of the lower bound, Lemma 12 will give, for each columnℓ, a lower bound of the form
(eℓ −f ℓ)+, wheref ℓ ≥0depends only on the data; forPNS(k)it isf ℓ = (k−1)c ℓ −β ℓ1{ℓ≤k}.
We callf ℓ thefree capacityof columnℓ: inflow up tof ℓ costs nothing, and each unit beyond it adds
one toθ. The lower bound is therefore a minimisation of P ℓ(eℓ −f ℓ)+ over the transportation set. The next lemma, stated for arbitraryf 1, . . . , fn ≥0, rewrites this minimisation as a maximisation
over the2 k subsetsJ⊆[k].
Lemma 13(Max-flow/min-cut).Letf 1, . . . , fn ≥0. For a set of rowsJ⊆[k], put
∆(J) :=
X
j∈J
dj −
nX
ℓ=1
min

|J\ {ℓ}| ×cℓ, fℓ

.
Then
min
m∈T
nX
ℓ=1

eℓ −f ℓ
+
= max
J⊆[k]
∆(J).
HereJis any set of rows, i.e. of targetsA j. The rows inJmust send out P j∈J dj in total, while
columnℓcan absorb free of cost at mostmin(|J\ {ℓ}| ×c ℓ, fℓ)of it: at mostc ℓ from each row
8

j∈Jwithj̸=ℓ, and at mostf ℓ altogether. So∆(J)is the part of the rows inJthat cannot be
absorbed for free, and each∆(J)is a lower bound on the cost. In the proof,Jappears as the set of
rows on the source side of a cut.
Proof.Consider the network of Figure 2, in which the source feeds rowjwith capacityd j, rowj
feeds columnℓ̸=jwith capacityc ℓ =P(x ℓ)(sincem jℓ =P(A j ∩x ℓ)≤c ℓ), and columnℓfeeds
the sink with capacityf ℓ. Letφbe the value of a maximum flow. Since(e−f) + =e−min(e, f)
and P ℓ eℓ =D, everym∈ Tsatisfies P ℓ(eℓ −f ℓ)+ =D− P ℓ min(eℓ, fℓ).
minm∈T
P
ℓ(eℓ −f ℓ)+ ≥D−φ: everym∈ Thas cost at leastD−φ.Fixm∈ T. We turn it into a flow by letting rowjsend to columnℓ̸=jthe amount
ηjℓ :=m jℓ λℓ, λ ℓ :=
min(eℓ, fℓ)/eℓ, e ℓ >0,
0, e ℓ = 0,
that is, the inflows of columnℓare scaled down by the common factorλ ℓ ∈[0,1]. This flow respects
every capacity: rowjships P ℓ̸=j ηjℓ ≤ P ℓ̸=j mjℓ =d j; on each arcη jℓ ≤m jℓ ≤c ℓ; and column
ℓreceives P j̸=ℓ ηjℓ =λ ℓeℓ = min(e ℓ, fℓ)≤f ℓ. Its value is P ℓ min(eℓ, fℓ), andφis the largest
value of any flow, so X
ℓ
(eℓ −f ℓ)+ =D− X
ℓ
min(eℓ, fℓ)≥D−φ.
minm∈T
P
ℓ(eℓ −f ℓ)+ ≤D−φ: somem∈ Thas cost at mostD−φ.Take a maximum flow, and letη jℓ ≥0be the amount it sends from rowjto columnℓ̸=j. Write
ηj :=
X
ℓ̸=j
ηjℓ, φ ℓ :=
X
j̸=ℓ
ηjℓ
for the total amount rowjships and the total amount columnℓreceives, respectively. So thatP
ℓ φℓ =φ, and the capacities giveη j ≤d j,η jℓ ≤c ℓ andφ ℓ ≤f ℓ.
Completing the flow to a tablem∈ T.Rowjmust placed j in the columnsℓ̸=j, and the flow
already placesη j there. The room left in its cells is X
ℓ̸=j
(cℓ −η jℓ) = (1−c j)−η j ≥d j −η j
by (⋆). So we can choosem jℓ ∈[η jℓ, cℓ]forℓ̸=jwith P ℓ̸=j mjℓ =d j; together withm jj :=β j
this givesm∈ T.
Bounding its cost.Sincem jℓ ≥η jℓ, the inflow of columnℓsatisfiese ℓ ≥φ ℓ, andφ ℓ ≤f ℓ. Hence
(eℓ −f ℓ)+ ≤e ℓ −φ ℓ: ife ℓ ≥f ℓ, thene ℓ −f ℓ ≤e ℓ −φ ℓ; ife ℓ < fℓ, then0≤e ℓ −φ ℓ. Summing
overℓ, X
ℓ
(eℓ −f ℓ)+ ≤ X
ℓ
eℓ −
X
ℓ
φℓ =D−φ.
Computingφby a minimum cut.A cut splits the nodes into a source side and a sink side, and its
capacity is the total capacity of the arcs that go from the source side to the sink side. LetJ⊆[k]be
the set of rows on the source side.
• Each rowj /∈Jis on the sink side, so the arc from the source to rowjis cut, at costd j.
• Each columnℓis placed on the cheaper side. On the source side, its arc to the sink is cut,
at costf ℓ. On the sink side, the arcs into it from the rows ofJare cut; there are|J\ {ℓ}|of
them (the number of elements ofJ\ {ℓ}), each of capacitycℓ, at total cost|J\ {ℓ}| ×cℓ.
The cheapest cut with row setJtherefore has capacity P j /∈Jdj + P ℓ min(|J\ {ℓ}| ×cℓ, fℓ). By
the max-flow/min-cut theorem [Ford and Fulkerson, 1956],φequals the minimum of this overJ.
SinceD− P j /∈Jdj = P j∈J dj,
D−φ= max
J⊆[k]
h X
j∈J
dj −
X
ℓ
min

|J\ {ℓ}| ×cℓ, fℓ
i
= max
J⊆[k]
∆(J).
9

Lemma 13 expresses the lower bound as a maximum over all2k setsJ⊆[k], whereas the published
bounds list three expressions; the gap is closed by (⋆) alone. We now show that, whenfℓ ≥(k−2)c ℓ
for everyℓ, every setJwith|J| ≤k−2gives∆(J)≤0. Since∆(∅) = 0, such sets never attain
the maximum, and it suffices to consider thek+ 2setsJ=∅,J= [k]\ {i}(i≤k) andJ= [k].
Lemma 14(Small cuts).Iff ℓ ≥(k−2)c ℓ for everyℓand|J| ≤k−2, then∆(J) =− P j∈J sj ≤ 0.
Proof.Let|J| ≤k−2. For every columnℓwe have|J\ {ℓ}| ≤ |J| ≤k−2, so|J\ {ℓ}| ×cℓ ≤
(k−2)c ℓ ≤f ℓ, and each minimum in∆(J)equals|J\ {ℓ}| ×c ℓ. Since|J\ {ℓ}|=|J| −1for
ℓ∈Jand|J\ {ℓ}|=|J|forℓ /∈J, and P ℓ cℓ = 1,
nX
ℓ=1
|J\ {ℓ}| ×cℓ =|J| −
X
j∈J
cj.
Hence
∆(J) =
X
j∈J
dj − |J|+
X
j∈J
cj =
X
j∈J
(dj +c j −1) =−
X
j∈J
sj ≤0,
where the last inequality is by applying (⋆).
4.3.3 Proof of the lower bound
Now, let’s finish the proof of the sharpness of lower bound.
Reduction to a flow.By Lemma 12 in columnℓ, applied to the eventsA j ∩x ℓ (j≤k),
θℓ ≥
 P
j mjℓ −(k−1)c ℓ
+
= (eℓ −f ℓ)+, f ℓ := (k−1)c ℓ −β ℓ1{ℓ≤k}.
Equality holds for a suitable arrangement, simultaneously in all columns. Hencemin Θ =
minm∈T
P
ℓ(eℓ −f ℓ)+, where everym∈ Tis realised by some admissible system. We havef ℓ ≥ (k−2)c ℓ ≥0becauseβ ℓ ≤c ℓ. By Lemmas 13 and 14,min Θ = max{0,∆([k]\ {i})i≤k,∆([k])}.
Evaluating the two cut families.By Lemma 14, everyJwith|J| ≤k−2has∆(J)≤0, so
apart from∆(∅) = 0, only sets with at leastk−1elements can give a positive value. These are
J= [k]\ {i}fori≤k, andJ= [k]. Recall that∆(J) = P j∈J dj − P ℓ min  |J\ {ℓ}| ×cℓ, fℓ 
withf ℓ = (k−1)c ℓ −β ℓ1{ℓ≤k}, and that P ℓ cℓ = 1.
•J= [k]\ {i}for somei≤k. We compute the minimum column by column:
–forℓ=i,|J\ {ℓ}|=k−1and the minimum is(k−1)c i −β i =f i;
–forℓ≤k,ℓ̸=i,|J\ {ℓ}|=k−2andf ℓ ≥(k−2)c ℓ, so the minimum is(k−2)c ℓ;
–forℓ > k,|J\ {ℓ}|=k−1andf ℓ = (k−1)c ℓ, so the minimum is(k−1)c ℓ.
Adding these up gives(k−1) P ℓ cℓ − P j≤k, j̸=icj −β i = (k−1)− P j≤k, j̸=icj −β i.
Hence, usingd j =α j −β j,
∆([k]\ {i}) =βi +
X
j≤k, j̸=i
(dj +c j)−(k−1) =β i +
X
j≤k, j̸=i
(αj +c j −β j)−(k−1).
•J= [k]. We also compute column by column:
–forℓ≤k,|J\ {ℓ}|=k−1and the minimum is(k−1)c ℓ −β ℓ =f ℓ;
–forℓ > k,|J\ {ℓ}|=kand the minimum ismin(kc ℓ,(k−1)c ℓ) = (k−1)c ℓ.
Adding these up gives(k−1)− P j≤k βj, hence
∆([k]) =
X
j≤k
dj −(k−1) +
X
j≤k
βj =
X
j≤k
αj −(k−1).
Together with∆(∅) = 0, these are exactly the three terms ofL:∆(∅) = 0 =L 1,∆([k]) =L 2,
andmax i≤k ∆([k]\ {i}) =L3. Thusmin Θ =L, and with Section 4.2, Theorem 7 is proved.
10

4.4 The other three families
The same argument works for targets of the formP(S, G)whenG̸= Ω. By Lemma 4, we apply
admissible systems again. We restate the bounds of Shu et al. [2026] in our notation, and give the
full proofs in Appendix. Throughout, we use the canonical form, in whichp > k.
PSub(k, p)andPN(k, p, q).G=x p forPSub, andG= (x p, yq) =Q qp ⊆x p forPN. We write
γ:=P(G), soγ=c p forPSubandγ=b qp forPNby consistency. The target isθ=P(S, G), and
the bounds are
max
n
0,
X
j≤k
(αj +c j −β j) +γ−k
o
≤θ≤min
n
γ,min
j≤k
dj
o
.(9)
PRep(k, q).The target isθ=P(S, y q). By consistency, only the cells of rowqin columnq(if
q≤k) and in the columnsℓ > kcan meetS; their total mass is
T:=β q1{q≤k}+
X
ℓ>k
bqℓ,
and the bounds are
θ≥max
n
0,
X
j≤k
(αj +c j −β j) +T−k,1{q≤k}
h
βq +
X
j≤k, j̸=q
(αj +c j −β j)−k+ 1
io
,
(10)
θ≤min
n
T, α q (ifq≤k),min j≤k, j̸=q dj
o
.(11)
Theorem 15.For any compatible data and any admissiblepandq, the bounds(9)onPSub(k, p)
andPN(k, p, q)and the bounds(10)–(11)onPRep(k, q)are sharp for everyk≥1.
ForPRep(k, q)withk= 1, the max-flow argument of Section 4.3 does not apply, since the free
capacityf q =−β q is negative, but sharpness still holds and follows from Theorem 17. The full
proofs of sharpness for these three families are given in the appendix.
So far each target form pairsx j withy j. A general query may pairx j with any outcome, for
exampleP(y 3x1 , y1x2 ). Shu et al. [2026] obtain its bounds from the canonical ones by substitution:
for a targety ixj , they useP(y ixj )in place ofP(y jxj )andP(x j, yi)in place ofP(x j, yj).
Proposition 16.Substitution gives the sharp bounds forPNS(k),PSub(k, p)andPN(k, p, q). For
PRep(k, q), it gives the sharp bounds when at most one target has the formyqxj . Theorem 17 covers
the remaining case, in which more than one target has the formy qxj , for example when bothy qx1
andy qx2 appear.
A complete proof follows from Theorem 17; see Appendix.
5 Unified results
In this section, we extend our main result and summarize the four families into one theorem.
The sharp bounds of the four families (Theorem 7 forPNS(k)and (9)–(11) for the other three), are
four instances of a single statement. The four families differ only in the factual eventG, and the
proofs above useGin one place: through the part ofGin each column that can still meetSonce
consistency is taken into account. The statement below also allows arbitrary target outcomes, so it
covers relabelled queries as well.
The general notation.Here, we keepGto be a factual event, and change the target outcome to
i1, . . . , ik ∈[n], we allowi u =i v foru, v∈[k]andu̸=v. We also change the notation ofA j we
defined in Section 3 as
Aj :=y ij xj .
According to this newA j, we have
S:= T j≤k Aj, θ:=P(S, G), α j :=a ij j, β j :=b ij j,
11

and keepd j =α j −β j,c j =P(x j)ands j = 1−c j −d j.
With the newα j andβ j, we haves j = (1−a ij j)−(c j −b ij j), which involves the other rows
i̸=i j of columnj. By consistency,b ij ≤a ij for everyiandj, summing over these rows gives
sj = P i̸=ij (aij −b ij)≥0, so (⋆) still holds. The proof of Lemma 4 also remains valid with the
target outcomejreplaced byi j throughout, soΘis still the set of values of admissible systems with
the change of notationA j ∩x j =Q ij j.
For a target columnx j withj≤k. Every unit in this column receivedx j, so by consistency its
outcome underx j is simply its observed outcome. We letE j denote whenA j holds, and letF j
denote whenA j fails on the rest of the column,
Ej :=Q ij j = (xj, yij ), F j :=x j \E j.
Let
C:=G\ S j≤k Fj.
Thenθcan be rewritten asθ=P(S, C), since no unit inF j can be inS, so we can dropF j fromG
and the value ofθstays the same. Write
γℓ :=P(C, xℓ)
for the mass ofCin columnℓ, andγ:=P(C) = P ℓ γℓ. In a target column onlyE j can remain, so γj =β j ifE j ⊆Gandγ j = 0otherwise. In a columnℓ > knothing is dropped,C=G, soγ ℓ is
just the mass ofGin that column.
Theorem 17(Unified form).In every compatible pair of tables, for everyk≥1, all target outcomes
i1, . . . , ik and every factual eventG,Θ = [L G, UG], where
LG = max
n
0|{z}
L1
, γ− P j≤k sj | {z }
L2
,max
i≤k

γi − P j≤k, j̸=isj 
| {z }
L3
o
,
UG = min
n
γ|{z}
U1
,min
j≤k
(dj +γ j)
| {z }
U2
,min
I⊆[k],|I|≥2
1
|I|−1
P
j∈I dj
| {z }
U3
o
.
Whenk= 1, the termU 3 is absent andL 3 =γ 1.
The theorem depends onGonly through the vector(γ 1, . . . , γn), which records whereGsurvives
consistency. For the canonical families (ij =j,p > k):
familyG γ j (j≤k)γ ℓ (ℓ > k)γ=P(C)
PNS(k) Ωβ j cℓ
P
j≤k βj + P ℓ>k cℓ
PSub(k, p)x p 0c p1{ℓ=p}c p
PN(k, p, q) (x p, yq) 0b qp1{ℓ=p}b qp
PRep(k, q)y q βq1{j=q}b qℓ T=β q1{q≤k}+ P ℓ>k bqℓ
ForPSubandPN,γis theγ=P(G)of (9), and forPRepit isT.
Substituting these values into Theorem 17 and using P ℓ cℓ = 1recovers four families. ForPSub, PNandPRepthe termU 3 is redundant, since an average of thed j overIis never smaller than
minj dj, and everyL 3 term withγ i = 0is non-positive.
The proof of Theorem 17 is given in Appendix.
6 Conclusion
We have proved the conjecture of Shu et al. [2026]: their closed-form bounds are sharp in all di-
mensions. The proof also explains why the bounds take the form they do. The upper bounds are
exactly the conditions under which the mass ofScan be spread over the columns, and the lower
bounds come from the only cuts that can bind. We further derived single formula that contains all
four families as special cases. Together with the equivalence classes of Shu et al. [2026], it gives
sharp bounds for any discrete PoC in every dimension. Our results use only experimental and obser-
vational data, with no further assumptions. Additional assumptions such as monotonicity, or extra
information such as covariates could tighten the bounds and can be a future research direction.
12

References
Alexander Balke and Judea Pearl. Bounds on treatment effects from studies with imperfect compli-
ance.Journal of the American Statistical Association, 92(439):1171–1176, 1997.
Alexander Abraham Balke.Probabilistic Counterfactuals: Semantics, Computation, and Applica-
tions. PhD thesis, University of California, Los Angeles, 1995.
Lester R. Ford and Delbert R. Fulkerson. Maximal flow through a network.Canadian Journal of
Mathematics, 8:399–404, 1956.
Maurice Fr ´echet. Sur les tableaux de corr ´elation dont les marges sont donn ´ees.Annales de
l’Universit´e de Lyon, Section A, 14:53–77, 1951.
David Galles and Judea Pearl. An axiomatic characterization of causal counterfactuals.Foundations
of Science, 3:151–182, 1998.
Joseph Y . Halpern. Axiomatizing causal reasoning.Journal of Artificial Intelligence Research, 12:
317–337, 2000.
Ang Li and Judea Pearl. Unit selection based on counterfactual logic. InProceedings of the Twenty-
Eighth International Joint Conference on Artificial Intelligence (IJCAI), 2019.
Ang Li and Judea Pearl. Unit selection with causal diagram. InProceedings of the AAAI Conference
on Artificial Intelligence, volume 36, pages 5765–5772, 2022.
Ang Li and Judea Pearl. Probabilities of causation with nonbinary treatment and effect. InProceed-
ings of the AAAI Conference on Artificial Intelligence, volume 38, pages 20465–20472, 2024.
Judea Pearl. Probabilities of causation: Three counterfactual interpretations and their identification.
Synthese, 121:93–149, 1999.
Judea Pearl.Causality. Cambridge university press, 2009.
Judea Pearl. On the consistency rule in causal inference: axiom, definition, assumption, or theorem?
Epidemiology, 21(6):872–875, 2010.
Xin Shu, Shuai Wang, and Ang Li. Identification of probabilities of causation: From recursive
to closed-form bounds. InProceedings of the Thirty-Fifth International Joint Conference on
Artificial Intelligence, IJCAI-2026, page 4063–4070. International Joint Conferences on Artificial
Intelligence Organization, 2026. doi: 10.24963/ijcai.2026/452. URLhttp://dx.doi.org/10.
24963/ijcai.2026/452.
Jin Tian and Judea Pearl. Probabilities of causation: Bounds and identification.Annals of Mathe-
matics and Artificial Intelligence, 28(1–4):287–313, 2000.
Junzhe Zhang, Jin Tian, and Elias Bareinboim. Partial counterfactual identification from observa-
tional and experimental data. InInternational Conference on Machine Learning (ICML), pages
26548–26558, 2022.
13
