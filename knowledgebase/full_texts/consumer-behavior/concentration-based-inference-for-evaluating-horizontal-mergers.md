---
title: Concentration-Based Inference for Evaluating Horizontal Mergers
url: https://arxiv.org/abs/2407.12924
category: consumer-behavior
subcategory: empirical
date: 2024-07
venue: ''
authors:
- Paul S. Koh
source: arxiv
pdf_url: https://arxiv.org/pdf/2407.12924
pages: 36
chars: 64826
fetched_at: '2026-11-08T13:08:20+00:00'
kb_version: 1
---

# Concentration-Based Inference for Evaluating Horizontal Mergers

Concentration-Based Inference for Evaluating Horizontal Mergers∗
Paul S. Koh†
September 20, 2025
Abstract
Antitrust authorities routinely rely on market concentration measures to assess the potential
adverse effects of mergers on consumer welfare. Using a first-order approximation argument
with logit and CES demand, I derive the relationship between the welfare effect of a merger on
consumer surplus and the change in the Herfindahl-Hirschman Index (HHI). My results suggest
that merger harm is correlated with the merger-induced change in HHI, and the proportionality
coefficient depends on the price responsiveness parameter, market size, and the distribution of
market shares within and across the merging firms. I present numerical validation of my formula
along with an empirical illustration.
Keywords: Merger, Herfindahl-Hirschman index, consumer surplus, upward pricing pressure
JEL Codes: D43, L13, L41, L44
∗I thank Dan Greenfield, Devesh Raval, Ted Rosenbaum, David Schmidt, Charles Taragin, Shawn Ulrick, and
Brett Wendling for their helpful comments. Much of this article was written during the author’s tenure at the U.S.
Federal Trade Commission; the views expressed in this paper are those of the author and do not necessarily represent
those of the Federal Trade Commission or any of its Commissioners. All errors are mine.
†School of Economics, Yonsei University. Seoul, Republic of Korea. Email:paulkoh9@gmail.com.
1
arXiv:2407.12924v5  [econ.GN]  23 Sep 2025

1 Introduction
Concentration measures have played a critical role during merger enforcement at the screening
stage and in court proceedings. In the United States,Merger Guidelines, jointly drafted by the
Department of Justice and the Federal Trade Commission, state how the agency uses the pre-merger
level of Herfindahl-Hirschman index (HHI) and merger-induced changes in HHI (often denoted
∆HHI) to presume anticompetitive mergers.
Previous works in the merger analysis literature have recognized the positive correlation be-
tween the changes in HHI and unilateral effects in both homogeneous and differentiated products
settings (Kim and Singal, 1993; Froeb and Werden, 1998; Prager and Hannan, 1998; Shapiro, 2010;
Ashenfelter, Hosken and Weinberg, 2015; Miller, Remer, Ryan and Sheu, 2017b; Miller and Sheu,
2021; Spiegel, 2021; Bhattacharya, Illanes and Stillerman, 2023).1 More recently, Nocke and Whin-
ston (2022) has shown that compensating synergies that offset market power effects of mergers can
be expressed in terms of ∆HHI in both the Cournot and Bertrand cases. Nocke and Schutz (2025)
shows how ∆HHI relates to merger welfare effects in differentiated products settings.
This paper contributes to the broad literature on concentration measures and market power by
providing a novel characterization of how HHI measures relate to merger welfare effects in multi-
product oligopoly settings with logit and CES demand. Using the first-order approach arguments
` a la Jaffe and Weyl (2013), I show
∆CS≈ −ρ∆HHI,(1)
where ∆CSis the change in consumer surplus, ∆HHIis the change in HHI computed with pre-
merger market shares (in quantity if the demand is logit and in revenue if CES), andρis the
proportionality coefficient whose value depends on the market size, price responsiveness parameter,
and the distribution of market shares across and within the merging firms. 2 Equation (1) provides
a simple but novel angle for understanding how mergers with the same value of ∆HHI may differ
in their impact on consumer welfare based on prior knowledge of industry statistics (i.e., market
size, price elasticity, and the distribution of firm sizes).
1In particular, Shapiro (2010) shows that, with logit demand, the sum of the approximate diversion ratios is
sj +s k + 2sjsk ors j +s k + ∆HHI. My derivation is different from his. I also focus on the welfare effects of mergers.
2The first-order approach to merger analysis has gained significant popularity due to its tractability; see, e.g.,
Farrell and Shapiro (2010), Valletti and Zenger (2021), and Koh (2025).
2

Formula (1) provides a simple tool for connecting ∆HHI to predicted consumer harm at the
merger screening stage. I show how the proportionality coefficientρcan be derived directly from
the merging firms’ product-level shares and the price responsiveness parameter, including how to
compute the merger pass-through matrix under both logit and CES demand systems. I build
on Miller et al. (2017b)’s insight that when estimating merger pass-through rates is difficult, it
is reasonable to approximate the merger pass-through matrixMwith an identity matrix. Unlike
Miller et al. (2017b), however, I show that the approximation is theoretically valid and can be refined
when the demand is CES. Specifically, I prove thatM→Iunder logit demand andM→ σ σ−1 I
under CES demand as the merging firms’ market shares approach zero, whereσis the elasticity of
substitution. These results provide new theoretical support for the approximation by Miller et al.
(2017b), and I present numerical evidence showing its accuracy and practical usefulness.
The closest work to this paper is Nocke and Schutz (2025), which also shows (1) holds using
second-order Taylor expansions around small shares and monopolistic competition conduct. How-
ever, their version ofρdepends only on the market size and price responsiveness parameter. My
first-order approach-based derivation, which relies on a different Taylor approximation employed
by the first-order approach literature, shows howρalso depends on thedistributionof merging
firms’ shares.3 Monte Carlo simulation shows that my approach can improve the prediction power
relative to Nocke and Schutz (2025)’s approach. My results corroborate the findings of Nocke and
Whinston (2022) and Nocke and Schutz (2025) that the unilateral effects of horizontal mergers are
directly linked to the change in HHI but also demonstrate that pre-merger market shares may still
retain relevance even after conditioning on the change in HHI.
The rest of the paper is organized as follows. Section 2 describes the model and reviews the
first-order approach to merger analysis. Section 3 presents the main proposition that characterizes
ρin (1) as a simple function of market size, price responsiveness parameter, and the distribution
of shares within and across firms. Section 4 analyzes the behavior of the proportionality coefficient
ρwith respect to model primitives and merging firms’ market shares. Section 5 compares my
results to those of Nocke and Schutz (2025). Section 6 considers an empirical application to the
Heinz/Beech-Nut merger to demonstrate the usefulness of my framework. Section 7 concludes. All
3To be clear, Jaffe and Weyl (2013)’s first-order Taylor approximation argument relies on a small upward pricing
pressure assumption but not a small market share assumption.
3

proofs are in Appendix A.
2 Model
2.1 Setup
I consider a Bertrand-Nash pricing game of multiproduct firms with differentiated products. 4 Each
firmf’s profit function is given by
Πf (p) =
X
l∈Jf
(pl −c l)ql(p),(2)
wherep l,c l, andq l(p) represent productl’s price, (constant) marginal cost, and quantity demanded
given price vectorp, respectively;J f is the set of products produced by firmf.
Following Nocke and Schutz (2018), I consider multinomial logit (MNL) and constant elasticity
of substitution (CES) demand functions, under which the demand for productjis given by
qj(p) =



exp(vj −αpj )
1+P l∈J exp(vl−αpl) N(MNL)
vj p−σ j
1+P l∈J vlp1−σ l Y(CES)
,(3)
whereNandα >0 (resp.Yandσ >1) are the market size and price responsiveness parameters
in the MNL (resp. CES) model, respectively. In typical applications,NandYrepresent the
total number of purchase opportunities (e.g., annual units sold) and the total category expenditure
(e.g., annual sales) in the relevant product/geographic market. 5 In each model,v j is the term
that captures productj’s quality. Note that the denominators in (3) also reflect the standard
normalization of the value of the outside option. 6
4Here, “multiproduct” means that a firm may offer multiple product varieties rather than conglomerate-type
products and sales.
5I treat market size as exogenous. While the hypothetical monopolist test (HMT) may play a role in delineating
market boundaries and size, my approach can be more practically applied to candidate market definitions at the
screening stage. See, for example, Koh (2024) for a sensitivity analysis framework regarding market definition.
6I review Nocke and Schutz (2018)’s aggregative games framework in Online Appendix A for readers less familiar
with the framework. I also refer readers to Caradonna et al. (2024) Online Appendix A for an excellent review of the
aggregative games framework.
4

2.2 First-Order Approximation of Merger Welfare Effects
I approximate the impact of mergers on consumer surplus using the first-order approach of Jaffe
and Weyl (2013). This method utilizes pre-merger data to calculate margins and diversion ratios,
translates them into predicted price changes using a merger pass-through matrix, and then infers
the resulting effects on consumer welfare. Formally, the process unfolds as follows.
Suppose firmsAandBmerge. The upward pricing pressure (UPP) of productj∈ J A is defined
as
UPP j ≡
X
l∈JB
(pl −c l)Dj→l,(4)
whereD j→l ≡ −(∂ql/∂pj)/(∂qj/∂pj) is the quantity diversion ratio from productjtol(Farrell
and Shapiro, 2010). The definition of upward pricing pressure is symmetric for productsj∈ J B.
Jaffe and Weyl (2013) show that predicting merger-induced price changes from upward pricing
pressures (net of efficiencies) requires amerger pass-through matrix, which captures how these
pressures spread across prices. They derive the first-order approximation ∆p≈M·UPP, where
Mis the merger pass-through matrix andUPPis the vector of upward pricing pressures for the
merging firms’ products. 7
Once the analyst obtains these UPP-based predicted price changes, the total impact on con-
sumer surplus can be approximated by summing across products:
∆CS≈
X
j∈JA∪JB
∆CS j,
where ∆CS j ≈ −∆pj ×q j for allj∈ J A ∪ JB. Thus, this framework connects post-merger price
effects to the underlying diversion ratios and margins, which in turn reflect the merging firms’
pre-merger market shares.
7Formally, the merger pass-through matrix is defined asM=−(∂h(p pre)/∂p)−1, whereh(p post) = 0 characterizes
the post-merger profit maximization conditions, with eachh j normalized to be quasilinear in marginal cost of product
j. As observed by Koh (2025), in the case of CES demand, it is more convenient to work with the merger pass-
through matrix defined asM=−(∂h(˜p pre)/∂˜p)−1, where ˜pj ≡logp j. This in turn yields %∆p≈M·GUPPI, where
(%∆p)j = ∆pj/pj is the percentage change in price of productjandGUPPI j ≡UPP j/pj.
5

2.3 Small-Share Approximation of Merger Pass-Through Matrix
The accuracy of the first-order approach depends on the availability of the merger pass-through
matrixM, which is often difficult to estimate due to its reliance on demand curvature. While
Mcan be expressed using market shares and the price responsiveness parameter under logit or
CES demand, the required matrix inversion makes closed-form solutions unwieldy. 8 The next
lemma offers a key simplification, allowing the first-order approach to be applied without explicitly
calculatingM.
Lemma 1.If the merging firms’ market shares approach zero, the merger pass-through matrix
converges toM→φI, whereφ= 1under MNL demand andφ= σ σ−1 under CES demand.
Proof.See Appendix A.1.
Lemma 1 provides theoretical support for the approximationM≈Iproposed by Miller et al.
(2017b), who use simulation evidence to show that the diagonal elements of the pass-through matrix
generally dominate the off-diagonal terms.9 My results refine their approach by showing that under
CES demand, this approximation should be scaled by a factor of σ σ−1 >1. This adjustment reflects
that CES demand typically implies higher pass-through rates than logit demand, allowing the Miller
et al. approximation to be tailored more accurately to the CES setting.
Lemma 1 suggests that it is reasonable to approximate each merger price effect as ∆pj ≈φUPP j.
To assess the performance of this approach, I repeat the Monte Carlo simulation exercise from Miller
et al. (2017b) and evaluate its accuracy. 10 Figure 1 shows thatφUPP j closely predicts the actual
merger price effects ∆p j when the UPPs are small, which typically occurs when the merging firms
have small market shares. Under logit demand, the approximation remains accurate across a wide
range of UPP values. In contrast, under CES demand, it tends to understate the actual price effects
as UPP increases, consistent with the findings of Miller et al. (2017b). 11 Overall, Figure 1 indicates
8See Online Appendix B for a full characterization of the merger pass-through matrix under logit and CES
demand.
9Miller et al. (2017b)’s approximation ∆p j ≈UPP j has been proven helpful for practitioners because pass-
through rates are usually difficult to estimate (Farrell and Shapiro, 2010; Jaffe and Weyl, 2013; Weyl and Fabinger,
2013; Miller et al., 2016, 2017b,a; Koh, 2025).
10I explain the simulation details in Appendix B. Note that Miller et al. (2017b) does not study the case of CES
demand. The result for logit is consistent with Miller et al. (2017a); see their Figure 2.
11In the case of CES demand, the predicted merger price effects may be conservative, likely because focusing only
on first-order effects overlooks the strong iterative effects that arise under convex demand.
6

that usingM≈φIoffers a straightforward and practical way to apply the first-order approach
without directly estimating the merger pass-through matrix.
Figure 1: Accuracy of the ∆p j ≈φUPP j Approximation
(a) Logit (φ= 1)
 (b) CES (φ= σ σ−1 )
Notes: The figures compare the accuracy of theφUPP j against the true price change ∆p j simulated from mergers
following the Monte Carlo simulation design of Miller et al. (2017b).
2.4 Limitations
The first-order approach to merger analysis has important limitations. First, by construction, it
only captures the direct response of the merging firms to the merger, without accounting for equi-
librium feedback effects between them or allowing for strategic reactions by non-merging rivals.
Second, it also focuses exclusively on unilateral effects, abstracting from the possibility of coor-
dinated conduct. Finally, estimating merger pass-through rates may be challenging in practice;
although Lemma 1 provides a useful alternative, it can generate bias when the merging firms’
shares are large. 12
Its main advantage, however, lies in its simplicity: it provides a sufficient-statistics framework
that links pre-merger information—such as market concentration measures in this paper—to pre-
dictions about post-merger price effects and consumer harm. In the following sections, I show that
this framework offers a clear characterization of how changes in the HHI translate into losses in
consumer surplus.
12Miller et al. (2017b) also shows that the first-order approach may underpredict merger price effects when the
demand function is convex, as in the case of CES demand. The first-order approach may overpredict merger price
effects when prices are strategic substitutes, which can arise in random coefficient logit models, but such examples
are not well-documented in the literature.
7

3 Consumer Surplus and HHI
3.1 Review of HHI
The Herfindahl-Hirschman Index (HHI) is defined as
HHI=
X
f∈F
s2 f .
Here,s j denotes the share of productj, which may be based on either quantity or revenue. The
total share of firmfis given bys f = P j∈Jf sj, whereJ f is the set of products sold by firm
f. I uses Q j ands R j to distinguish between quantity and revenue shares, respectively. Under the
logit framework,s Q j =q j/N. Under the CES framework,s R j =p jqj/Y. 13 Note that I keep the
HHI scaled between 0 and 1, rather than multiplying by 10,000 as is commonly done to improve
readability.
If firmsAandBmerge, the resulting change in the HHI is given by
∆HHI AB = 2sAsB.
This calculation is based on pre-merger market shares and does not account for any shifts in
market shares that may occur in the post-merger equilibrium. 14 However, as I show below, using
pre-merger shares in this way is logically consistent with the first-order approach, which relies solely
on pre-merger information to predict potential merger harm.
3.2 Relationship between Consumer Surplus and HHI
The following proposition, which is the main result of this paper, shows that ∆HHI AB is closely
related to the impact of the merger on consumer surplus predicted by the first-order approach.
Proposition 1.Suppose firmsAandBmerge, and there is no merger-specific synergy. The
13The shares are calculated with the outside option. Shares excluding the outside option can be computed as
˜sf =s f /(1−s 0).
14Specifically,HHI post −HHI pre = ((sA +s B)2 + P f̸=A,B s2 f )−(s 2 A +s 2 B + P f̸=A,B s2 f ) = 2sAsB.
8

first-order approximation to the merger-induced change in consumer surplus is
∆CS=



−V MNL 0 ρMNL 1 ρMNL 2 ∆HHI Q AB (MNL)
−V CES 0 ρCES 1 ρCES 2 ∆HHI R AB (CES)
,(5)
where
V0 ≡



N
α (MNL)
Y
σ−1 (CES)
,(6)
ρ1 ≡



1
(1−sA)(1−sB) (MNL)
σ
σ−1
( σ σ−1 −sR A)( σ σ−1 −sR B) (CES)
,(7)
ρ2 ≡



P
j,l∈JA∪JB Mjl sj sl

1
2 Il∈JA
sl/(1−sl)
sA/(1−sA) + 1 2 Il∈JB sl/(1−sl) sB/(1−sB)

(MNL)
P
j,l∈JA∪JB
σ−1
σ Mjl
sR j
sR l

1
2 Il∈JA
sR l /( σ σ−1 −sR l )
sR A/( σ σ−1 −sA) + 1 2 Il∈JB sR l /( σ σ−1 −sR l ) sR B/( σ σ−1 −sR B)  (CES) .(8)
Proof.See Appendix A.2.
Proposition 1 shows that ∆CSis proportional to ∆HHI AB, with the proportionality coefficient
determined by the market size, price responsiveness parameter, and the distribution of market
shares across and within firms (the latter relevant when merging firms are multiproduct producers).
Thus, equation (5) provides a means to directly translate ∆HHI AB into statements about harm to
consumers using data from the merging firms.
First,V 0 converts ∆HHI AB into monetary units, as it is the product of market size and the
inverse of the price responsiveness parameter. Second,ρ 1 serves as a cross-firm scaling factor,
reflecting the interaction of total shares across firms. Finally,ρ 2 functions as a within-firm scaling
factor, capturing how shares are distributed among products within multiproduct firms.
I defer further interpretation and comparative statics analysis for the components of the pro-
portionality coefficients to Section 4. In Section 5, I compare equation (5) with the formula de-
rived by Nocke and Schutz (2025). Finally, I provide an empirical example in Section 6 using the
Heinz/Beech-Nut merger in the U.S. market for baby food.
Remark 1(Compact Representation).Recallingφ= 1 if MNL andφ= σ σ−1 if CES, the first-order
9

approximation to the merger welfare effect to consumers (5) can be compactly written as
∆CS=−V 0ρ1ρ2∆HHI,where
ρ1 ≡ φ (φ−s A)(φ−s B) ,and
ρ2 ≡
X
j,l∈JA∪JB
 Mjl
φ
 sj
sl
 1
2 Il∈JA
sl/(φ−s l)
sA/(φ−s A) + 1 2 Il∈JB sl/(φ−s l) sB/(φ−s B)  .
Remark 2(Single-Product Case).If the merging firms are producers of single productsρ 2 boils
down toρ 2 = 1 2φ (MAA +M AB sA sB +M BA sB sA +M BB ). Further assumingM≈φIsimplifies this
expression toρ 2 ≈1. In this case, expression (5) reduces to ∆CS≈ −V 0

φ
(φ−sA)(φ−sB)

∆HHI AB,
which provides a simple and direct way to connect ∆HHI AB to consumer harm based on firm-level
shares.
Remark 3(Merger Screening Decision Rule).In the spirit of the first-order approach, equation (5)
allows the analyst to estimate total consumer harm using only data from the merging firms. If the
agency seeks to evaluate consumer harm net of potential merger-specific cost savings, the formula
can be adjusted to incorporate marginal cost reductions. 15 This provides a clear decision rule: the
agency should block the proposed merger if the net impact on consumer surplus is negative. Unlike
the traditional screening rule, which relies solely on the level and change in HHI, this approach
explicitly incorporates efficiency considerations, offering a more nuanced and economically grounded
assessment of merger effects.
4 Analysis of the Proportionality Coefficient
Two mergers with the same value of ∆HHI may have different proportionality coefficients due to
differences in the distribution of shares of the merging firms. To sharpen the intuition behind how
the proportionality coefficients behave, I analyze how the proportionality coefficient in (5) depends
on the market size, consumer price responsiveness, and the distribution of shares across and within
firms.
15The net upward pricing pressure for a productj∈ JA ∪ JB isUPP net j =UPP j −∆c j, where ∆cj =c pre j −c post j >
0 is the savings from marginal cost. Then since ∆p net ≈M·UPP net =M·(UPP−∆c), we get ∆CS net ≈
−∆pnet⊤q≈ −UPP⊤M ⊤q+ ∆c ⊤M ⊤q. Since, (5) =−UPP ⊤M ⊤q, accounting for potential cost efficiency amounts
to adding back ∆c ⊤M ⊤q >0 to (5). UsingM≈φI, the cost savings term can be further simplified as ∆c ⊤M ⊤q≈
φ P j∈JA∪JB ∆cjqj.
10

4.1 Monetary Scaling Factor
The termV 0 in (6) serves as a monetary scaling factor that translates ∆HHIAB into monetary units.
It equals the product of market size and the inverse of the price responsiveness parameter. Under
the logit model, the price responsiveness parameterαrepresents the marginal utility of income, so
1/αconverts utility units to monetary units (e.g., dollars), and multiplying byNscales the per-
capita measure to the total market. In the CES case, the marginal utility of income is (σ−1)/Y,
so multiplying byY /(σ−1) converts welfare changes in utils to monetary units.16 Viewed this way,
−ρ1ρ2∆HHI AB can be interpreted as the change in consumer utility caused by the merger.
Comparative statics with respect toV 0 are straightforward: consumer harm increases with
market size and with less price-sensitive demand. In particular, more inelastic demand means
consumers offer weaker resistance to post-merger price increases, shifting a greater share of the
burden onto them.
4.2 Cross-Firm Scaling Factor
The termρ 1 in (7) serves as a cross-firm scaling factor, reflecting the interaction of total shares
across firms. The following proposition studies the behavior ofρ 1 with respect to the merging firms’
firm-level shares.
Proposition 2.Suppose thats f < φforf=A, B.
1.ρ 1 →1/φas the merging firms’ shares approach zero.
2.ρ 1 is increasing in the merging firms’ shares.
3.ρ 1 is strictly convex in the merging firms’ shares.
Proof.See Appendix A.3.
Proposition 2.1 implies that approximationρ 1 ≈1/φis valid when the merging firms’ shares
are small; this result will be of particular interest when comparing my formula to that of Nocke
and Schutz (2025) in Section 5. Proposition 2.2 provides a direction of howρ 1 behaves as merging
firms’ shares get larger.
16The indirect CES utility isV(p, Y) =Y /P(p), whereP(p) is the CES price index. Letu= (σ−1) logV(p, Y)
be the log-cardinalized utility scaled by (σ−1). The marginal utility of income is then∂u/∂Y= (σ−1)/Y.
11

Proposition 2.3 implies that a merger between two equally sized firms is less harmful than one
between a dominant firm and a much smaller rivalif the two mergers produce the same level of
∆HHI AB. In an asymmetric merger, the larger firm raises its price on a large base of sales, while
the smaller firm raises its price sharply on a smaller base of sales. These effects compound, leading
to a greater overall loss of consumer welfare. In contrast, when the merging firms are similar in
size, both price increases tend to be more moderate, producing less harm.
To build intuition, consider a simple example with single-product firms under logit demand.
Suppose there are two mergers, one between firms with market shares (s A, sB) = (0.2,0.2) and
another between firms with shares (s A, sB) = (0.8,0.05). Both mergers generate the same change
in concentration, ∆HHI AB = 2sAsB = 0.08. Even though ∆HHI AB is identical, the mergers differ
in their implications forρ 1.
Figure 2 plots the combinations of (sA, sB) that yield ∆HHI AB = 0.08. The solid line represents
this set, while the dashed lines show the level curves ofρ 1 passing through the symmetric and
asymmetric cases. In the symmetric case,ρ 1 ≈1.56, whereas in the asymmetric case,ρ 1 ≈5.26.
Thus, the asymmetric merger produces a much higher value ofρ 1, indicating greater potential
harm.
Figure 2: Exampleρ 1 for Symmetric vs. Asymmetric Firm Shares
Symmetric
Asymmetric
0.00
0.25
0.50
0.75
1.00
0.00 0.25 0.50 0.75 1.00
sA
sB
Notes:This figure illustrates that a merger between firms with asymmetric shares can generate a higher value ofρ 1
than a merger between firms with symmetric shares, even when both have the same ∆HHI. The solid line represents
the set of (s A, sB) pairs satisfying 2s AsB = 0.08. The inner dashed line shows the level curve of 1 (1−sA)(1−sB ) passing
through (s A, sB) = (0.2,0.2), while the outer dashed line shows the corresponding level curve passing through
(sA, sB) = (0.8,0.05).
12

This pattern arises because reducing one firm’s share by a small amount allows for a much
larger increase in the other firm’s share to keep ∆HHI AB constant. The trade-off is therefore not
one-to-one, and as asymmetric increases, the combined sharess A +s B can grow substantially even
though ∆HHI AB remains fixed.17
To compare the consumer harm, assume that the upward pricing pressure closely approximates
the actual price change (∆p j ≈UPP j), so that the effect ofρ 2 can be ignored. In the symmetric
merger, (UPP A,UPP B) = (0.3125/α,0.3125/α). In the asymmetric merger, (UPP A,UPP B) =
(0.2632/α,4.2105/α). In the asymmetric case, the larger firm applies a modest price increase to a
substantial customer base, while the smaller firm applies a steep increase to a smaller base. The
effects combine to generate a much larger total loss in consumer welfare. The change in consumer
surplus is ∆CS= 0.125(N/α) in the symmetric merger and ∆CS= 0.4211(N/α) in the asymmetric
merger.18 Thus, even though both mergers have the same ∆HHIAB, the asymmetric merger is more
than three times as harmful to consumers.
The idea that two mergers can generate the same ∆HHI while yielding very different values
ofρ 1 applies more broadly. Define the set of share combinations that yield a given change in
concentration:
S(c 0,∆ 0)≡ {(sA, sB) : 2s AsB = ∆0, sA +s B ≤c 0},(9)
where the restrictions A +s B ≤c 0 prevents shares from becoming too arbitrary. For each pair of
(sA, sB) in this set, there is a corresponding value ofρ 1. Figure 3 plots the upper and lower bounds
ofρ 1 forc 0 = 0.9. The lower bound occurs when the merging firms are symmetric, while the upper
bound occurs when shares are highly asymmetric. 19 As the figure demonstrates, the cross-firm
coefficientρ 1 can vary substantially depending on how market shares are distributed between the
merging firms, particularly when ∆HHI is small.
17A more precise statement would require comparing the curvatures of the level curve of ∆HHI AB and that ofρ 1.
18If firmAmergers with firmB, the upward pricing pressure for single-product firmAfacing logit demand with
price sensitivity parameterαisUPP A =D A→B ×m B = sB 1−sA × 1 α(1−sB ) . Approximating the price increase as
∆pA ≈UPP A, the resulting change in consumer surplus is ∆CS A ≈UPP A ×q A = N α sAsB (1−sA)(1−sB ) , whereq A =s AN. ∆CS B can be derived symmetrically.
19Note thatS(c 0,∆ 0) is non-empty only ifc 2 0/2≥∆ 0. On an (s A, sB) plane, the level curve of 2s AsB = ∆ 0
crosses the lines A +s B =c 0 only ifc 2 0/2≥∆ 0. It is straightforward to verify thatρ MNL 1 is minimized when
sA =s B =
p
∆0/2 and maximized whens A = 1 2 (c0 − p c2 0 −2∆ 0) ands B = 1 2 (c0 + p c2 0 −2∆ 0). The lower and
upper bounds areρ MNL 1 = 1 (1− √ ∆0/2)2 and ρMNL 1 = 2 ∆0−2c0+2 .
13

Figure 3: Upper and Lower Bound ofρ M N L 1 forc 0 = 0.9
2
4
6
8
10
0.0 0.1 0.2 0.3 0.4
∆0
ρ1 MNL
Notes: This figure illustrates that mergers with the same ∆HHI can differ substantially in their values ofρ 1. The
upper contour represents the maximum value ofρ 1 for a given ∆HHI= ∆ 0, which occurs when the merging firms’
shares are most asymmetric. The lower contour represents the minimum value ofρ 1, attained when the merging
firms’ shares are symmetric.
4.3 Within-Firm Scaling Factor
The termρ 2 in (8) serves as a within-firm scaling factor, capturing how market share is distributed
across the products of a multi-product firm. In principle,ρ 2 depends on both within-firm share
distribution and cross-firm interactions through the merger pass-through matrixM. However,
drawing on Miller et al. (2017b)’s observation that the diagonal elements ofMtend to dominate
the off-diagonal elements, we can approximate the matrix byM≈φI(as supported by Lemma 1).
Under this simplification,ρ 2 simplifies to:
ρ2 ≈ 1 2 X l∈JA sl/(φ−s l) sA/(φ−s A) + 1 2 X l∈JB sl/(φ−s l) sB/(φ−s B) .
Here,ρ 2 is the average of two additively separable components, each depending only on the dis-
tribution of product-level shares within a firm (holding the total firm share fixed). If each firm
produces a single product,ρ 2 collapses toρ 2 ≈1. Thus,ρ 2 becomes relevant primarily when firms
operate multiple products. 20
The following result establishes that approximatingρ 2 as 1 is reasonable when merging firms
have small market shares, regardless of the number of products.
Proposition 3.ρ 2 →1as the merging firms’ market shares approach zero.
Proof.See Appendix A.4.
20Without the approximation of the merger pass-through matrix,ρ 2 = 1 2φ (MAA +M AB sA sB +M BA sB sA +M BB )
(see Remark 2). Thus, even for single-product firms,ρ 2 can depend on the merging firms’ shares. However, when
the shares are small,M≈ρI, making this dependence minor and supporting the interpretation ofρ 2 as primarily a
scaling factor for multiproduct settings.
14

Proposition 3 implies that for mergers involving small firms, analysts can safely use the approx-
imationρ 2 ≈1 without calculating the merger pass-through matrix.
Further analytical comparative statics forρ 2 are difficult because it is a complex function of
product- and firm-level shares, which also affect the pass-through matrix. To better understand
its behavior, I rely on simulations under the logit demand model. 21 In these simulations, I set the
price responsiveness parameter toα= 1. Importantly, I do not impose the simplificationM≈φI
when calculatingρ 2; instead, I compute the exact merger pass-through matrix.
I first examine the case where each firm produces a single product, even thoughρ 2 is typically
interpreted in a multi-product setting. This exercise clarifies the role of cross-firm share interactions
that operate through the pass-through matrix.
Figure 4 uses contour plots to display howρ 2 and the productρ 1 ×ρ 2 vary with the firms’ shares
(sA, sB). Figure 4a shows that, as predicted by Proposition 3,ρ 2 ≈1 when both firms’ shares are
small. However,ρ 2 is nonlinear and non-monotonic, with its value depending in a complex way on
the relative shares of the two firms. Increasing asymmetry between firms’ shares (holding ∆HHI
fixed) generally increasesρ 2, but the effect can be ambiguous in certain regions. Yet, Figure 4b
shows that, when considering the combined termρ 1 ×ρ 2, increasing asymmetry unambiguously
raises the value ofρ 1 ×ρ 2 for a fixed ∆HHI.
Figure 4: The Values ofρ 2 andρ 1 ×ρ 2 in Single-Product Logit Case
0.0
0.2
0.4
0.6
0.8
0.0 0.2 0.4 0.6 0.8
sA
sB
ρ2
0.9
1.2
1.5
1.8
(a)ρ 2
0.0
0.2
0.4
0.6
0.8
0.0 0.2 0.4 0.6 0.8
sA
sB
ρ1 × ρ2
2.5
5.0
7.5 (b)ρ 1 ×ρ 2
Notes: The figure shows how the values ofρ 2 andρ 1 ×ρ 2 vary with respect to (sA, sB) under the single-product logit
demand assumption. I constrain the set of (s A, sB) to be those satisfyings A +s B ≤0.8.
Next, I analyze howρ 2 behaves when each firm produces multiple products with symmetric
product-level shares. This exercise clarifies the role of total shares in multi-product firms and the
21I find similar patterns under the CES demand assumption.
15

number of products they produce. Suppose each firm has a total market shares f and producesJ
products, so that each product has a shares j =s f /J. Figure 5 plotsρ 2 andρ 1 ×ρ 2 as functions
ofs f andJ. Figure 5a remains non-monotonic in firm shares, consistent with the single-product
results in Figure 4a. Increasing the number of productsJraisesρ 2 for a fixeds f , but the effect is
negligible unless the firms have very large market shares. On the other hand, Figure 5b shows that
the combined termρ 1 ×ρ 2 is monotonic in firm shares. Having more products has only a minor
effect unless the firms are very large.
Figure 5: The Values ofρ 2 andρ 1 ×ρ 2 for Symmetric Multiproduct Firms
0.85
0.90
0.95
1.00
1.05
1 2 3 4 5 6 7 8 9 10
Number of Products (J)
ρ2
Share
0.05
0.1
0.15
0.2
0.25
0.3
(a)ρ 2
1.00
1.25
1.50
1.75
2.00
1 2 3 4 5 6 7 8 9 10
Number of Products (J)
ρ1 × ρ2
Share
0.05
0.1
0.15
0.2
0.25
0.3 (b)ρ 1 ×ρ 2
Notes: This figure plots the values ofρ 2 andρ 1 ×ρ 2 assuming symmetric firms that produceJproducts with equal
market shares under the logit demand assumption. “Share” indicates the value of each firm’s shares f .
The simulations show thatρ2 is typically close to one when merging firms have small or moderate
market shares, supporting the practical approximationρ 2 = 1. Whileρ 2 can exhibit nonlinear and
non-monotonic behavior—particularly for large firms or highly uneven product mixes—these effects
are generally modest and only become significant when firm shares are very large. Moreover, its
influence is dominated byρ 1, as the combined termρ 1 ×ρ 2 rises predictably with firm size and
asymmetry, holding ∆HHI fixed. Thus, in most merger analyses,ρ 2 acts as a minor adjustment
factor, and the key variation in outcomes is driven primarily byρ 1.
16

5 Comparison to Nocke and Schutz (2025)
5.1 Comparison of Formulas
Equation (5) in Proposition 1 aligns with the findings of Nocke and Whinston (2022) and Nocke
and Schutz (2025): consumer harm from a merger is proportional to ∆HHI. Specifically, Nocke
and Schutz (2025) Proposition 8 shows that when market shares are small, the market power effect
of a merger without synergies can be approximated as
∆CS≈



−V MNL 0 ∆HHI AB (MNL)
−V CES 0 σ−1 σ ∆HHI R AB (CES)
,(10)
where the proportionality coefficient is constant and does not depend on the merging firms’ indi-
vidual market shares.
The key difference between their result in (10) and my expression in (5) lies in the underly-
ing approximation method. Nocke and Schutz (2025) relies on a second-order Taylor expansion
around the limit of small market shares and monopolistic competition. By contrast, equation (5)
is derived using the first-order approach of Farrell and Shapiro (2010) and Jaffe and Weyl (2013).
This distinction matters: Proposition 1 shows that, in my framework, pre-merger market share
distributions directly affect merger harm through the scaling factorsρ 1 andρ 2. In other words,
even conditional on ∆HHI, the way market shares are distributed—both across and within the
merging firms—remain economically relevant.
Importantly, the two formulations are fully consistent in the limit of small market shares. From
Propositions 2 and 3, as (s A, sB)→(0,0), we haveρ 1 →1/φandρ 2 →1. Substituting these limits
into equation (5) yields ∆CS→ V0 ρ HHI AB, which exactly matches the characterization in equation
(10). Thus, my result is consistent with Nocke and Schutz (2025) but provides a richer picture of
how share distribution shapes merger effects when firms have non-negligible market shares.
17

5.2 Monte Carlo Experiment
I run Monte Carlo experiments to examine how my formula (5) performs relative to Nocke and
Schutz (2025)’s formula (10). I follow the simulation design in Miller et al. (2017b). 22 I apply
my approximationM≈φI(Lemma 1) to gauge how they perform without requiring the analyst
to calculate pass-through rates, which are generally complex functions of model parameters and
data.23
Monte Carlo experiments indicate that Proposition 1 improves upon the approximation in Nocke
and Schutz (2025). Figure 6 compares the two approaches: their formula in (10) and my first-order
approach in (5). For the logit case, the Nocke-Schutz formula tends to underestimate the welfare
effects (Figure 6a). My approach provides a closer approximation on average, although it can
exhibit greater variance and occasionally overestimate welfare effects when the actual change in
consumer surplus is large (Figure 6b). This difference arises because (10) omits theρ MNL 1 term,
which is always greater than one. The CES results are similar. Again, the Nocke-Schutz formula
underestimates the true effects (Figure 6c). In contrast, the first-order approach performs quite
well, with a dense clustering of points along the 45-degree line (Figure 6d)
Figure 7 reports the distribution of prediction error, defined as the percentage deviation between
the predicted and actual change in consumer welfare. 24 For the logit (CES) case, the average
errors are -36% (-28%) for the Nocke-Schutz approach and -4% (-10%) for the first-order approach,
respectively. Overall, the first-order approach substantially improves the accuracy of linking ∆HHI
to predicted changes in consumer welfare from mergers, offering a much closer fit than the Nocke-
Schutz approximation.
22I consider a market with six single-product firms. I randomly draw the share and margin of firm 1 and use these
to calibrate the model parameters. I then simulate a merger between firms 1 and 2 and compute the resulting change
in consumer surplus, normalizing the market size so thatV 0 = 1. Appendix B provides further details on the Monte
Carlo experiments.
23In Appendix C, I also examine the role of model misspecification. I find that using the MNL formula generally
predicts a larger consumer welfare loss from a merger than the CES formula.
24Specifically, for each simulation, I calculate the prediction error as log(∆CS predicted/∆CS actual).
18

Figure 6: Comparison of Nocke-Schutz and First-Order Approach
(a) Nocke-Schutz (Logit)
 (b) First-Order Approach (Logit)
(c) Nocke-Schutz (CES)
 (d) First-Order Approach (CES)
Notes: This figure compares the performance of the Nocke-Schutz formula ∆CS NS =−(V 0/φ)∆HHI AB and my first-
order approach-based formula ∆CS FOA =−V 0ρ1ρ2∆HHI AB after settingρ 2 = 1 in predicting the actual consumer
welfare loss due to mergers.
Figure 7: Distribution of Prediction Errors in the Nocke-Schutz and First-Order Approach
(a) Logit
 (b) CES
Notes: This figure plots the distribution of prediction errors of the Nocke-Schutz formula and my first-order approach-
based formula. For each simulation draw, the prediction error is measured as log(∆CS predicted/∆CS actual).
19

6 An Empirical Example:Heinz/Beech-NutMerger
To demonstrate how my framework can be applied in practice, I consider the proposed merger
between Heinz and Beech-Nut in the U.S. baby food market. 25 In 2000, H.J. Heinz announced
plans to acquire Beech-Nut for$185 million. At the time, the U.S. baby food market was valued
between$865 million and$1 billion annually and was dominated by three firms: Gerber with a
65% market share, Heinz with 17.4%, and Beech-Nut with 15.4% (measured by revenue). Had
the merger proceeded, the industry would have effectively become a duopoly, with the combined
Heinz-Beech-Nut entity controlling 98% of the market (Chen, 2010).
The Federal Trade Commission challenged the merger under Section 7 of the Clayton Act,
arguing that reducing the number of major competitors from three to two would significantly
harm competition. Heinz defended the deal by claiming substantial merger-specific efficiencies.
In particular, it argued that closing Beech-Nut’s outdated plant and streamlining production and
distribution would lower costs, enabling the merged firm to compete more effectively against Gerber.
However, the D.C. Circuit ultimately rejected these arguments, ruling that the claimed efficiencies
were not sufficient to offset the likely competitive harm. In response, Heinz abandoned the merger
in 2001.
For tractability, I model Heinz and Beech-Nut as single-product firms facing constant elasticity
of substitution (CES) demand and assume there are no merger-specific efficiencies. 26 To be con-
servative, I set the total market size toY= $865 million, corresponding to the lower bound of the
estimated industry size. Based on the pre-merger market share, the change in concentration im-
plied by the merger is ∆HHI= 0.0536. Using this value, I compute estimates of consumer harm by
∆CS=−ρ∆HHI, whereρ=V 0ρ1ρ2 is the proportionality coefficient for translating concentration
changes to consumer surplus loss. I estimateρ 2 along with the CES merger pass-through matrix
without relying onM≈φI.
Table 1 reports these estimates for different values of the CES price responsiveness parameter,
σ.27 The results indicate that consumer harm would range from$19.10 million to$36.68 million
annually, depending on the assumed level of consumer price sensitivity. As expected, harm is
25I choose this example because it aligns well with the theoretical framework of the paper, and firm-level market
share data is readily available.
26Product-level share data are not publicly available.
27Information on firms’ margin, which is not publicly available, can produce an estimate ofσ.
20

greater when consumers are less price sensitive.
Table 1: Annual Consumer Harm Calculation for theHeinz/Beech-NutMerger
σ φ1/φ V 0 ρ1 ρ2 ρ∆HHI∆CS
1.5 3.00 0.33 1730.00 0.37 1.09 703.16 0.0536 -$37.68m
2.0 2.00 0.50 865.00 0.59 1.04 531.37 0.0536 -$28.48m
2.5 1.67 0.60 576.67 0.73 1.00 426.72 0.0536 -$22.87m
3.0 1.50 0.67 432.00 0.84 0.98 356.39 0.0536 -$19.10m
Notes:ρ 2 is calculated with the pass-through matrix. Note thatρ=V 0ρ1ρ2 and
∆CS=−ρ∆HHI.
Recall that as market shares approach zero,ρ 1 →1/φandρ 2 →1. Table 1 shows that while the
approximationρ 2 ≈1 is generally reasonable, the approximationρ 1 ≈1/φcan be quite inaccurate.
This suggests that if an analyst wishes to adopt a simple, fast approach without computing the full
merger pass-through matrix, settingρ 2 = 1 is a defensible simplification; this finding is consistent
with the simulation results reported in Section (5).
7 Conclusion
This paper develops simple formulas linking changes in HHI to the consumer welfare effects of
mergers in differentiated product markets with multi-product firms. Using a first-order approach, I
show that merger-induced changes in consumer surplus are proportional to changes in HHI, with the
proportionality coefficient determined by market size, the price responsiveness parameter, and the
distribution of the merging firms’ shares. These results bridge concentration-based merger screening
tools, commonly used by antitrust agencies, with the unilateral effects framework rooted in the
standard Bertrand-Nash pricing model, providing a clearer theoretical foundation for interpreting
changes in market concentration.
21

Appendix
A Proofs
A.1 Proof of Lemma 1
In the logit case, the merger pass-through matrix is defined asM=−

∂h(ppre)
∂p
−1
whereh(p)
is a function that characterizes the post-merger FOC such thath(p post) = 0 but normalized to
be quasilinear in marginal cost. By expressing each ∂hj (p) ∂pk withj, k∈ JA ∪ JB as a function of
quantity-based shares and the price sensitivity parameterα, it can be verified that ∂hj ∂pj → −1 as
the shares converge to zero, and ∂hj ∂pk →0 for any pairj̸=k. 28 Thus, ∂h ∂p → −I, which givesM=I.
In the CES case, the merger pass-through matrix is defined asM=−

∂h( ˜ppre)
∂˜p
−1
, where
˜pj ≡logp j andh(˜p) is a function that characterizes the post-merger FOC such thath(˜p post) = 0
but normalized to be quasilinear in relative marginsm j ≡ pj −cj pj . Similar to the logit case, one
can express each ∂hj (˜p) ∂˜pk withj, k∈ JA ∪ JB as functions of revenue-based shares and the price
sensitivity parameterσ. It can be verified that ∂hj ∂˜pj → −σ−1 σ as the shares converge to zero, and
∂hj
∂˜pk →0 for any pairj̸=k. Thus, ∂h ∂˜p→ −  σ−1 σ  I, which givesM→ σ σ−1 I.
A.2 Proof of Proposition 1
Before proceeding to the proof, I show how absolute (resp. relative) margins relate to firms’ shares
in the logit (resp. CES) case. In Nocke and Schutz (2018), the authors define the “ι-markups” as
µf ≡



α(pj −c j),∀j∈ J f (MNL)
σ pj −cj pj ,∀j∈ J f (CES)
.(11)
Theι-markups use the fact that with logit (resp. CES) demand, firms charge constant absolute
(relative) margins across their products. Nocke and Schutz (2025) equation (5) shows that
µf = 1 1−α ∗sf (12)
28I characterize the merger pass-through matrix under the logit and CES demand assumptions in Online Appendix
B.
22

holds in equilibrium, whereα ∗ = 1 under logit andα ∗ = σ−1 σ under CES. 29 Combining (11) and
(12) implies
pj −c j = 1 α(1−s Q f ) ,∀j∈ J f (13)
in the case of logit, and
pj −c j
pj
= 1 1 + (1−s R f )(σ−1) ,∀j∈ J f (14)
in the case of CES.
A.2.1 Logit
Under logit demand, quantity diversion ratio isD j→k = sQ k 1−sQ j and firms’ absolute margins satisfy
(13). Then I can write the upward pricing pressure ofj∈ J A as
UPP j =
X
k∈JB
(pk −c k)Dj→k =
X
k∈JB
1
α(1−s Q B)
sQ k
1−s Q j = sQ B α(1−s Q B)(1−s Q j ) .
Thus, for an arbitrary productj∈ J A ∪ JB, I can express its upward pricing pressure as
UPP j =I j∈JA
sQ B
α(1−s Q B)(1−s Q j ) +I j∈JB
sQ A
α(1−s Q A)(1−s Q j ) .
Next, given that the first order price effect on an arbitrary productjis ∆pj = P k∈JA∪JB Mjk UPP k,
we have
∆CS j =−∆p j ×q j
=−

 X
k∈JA∪JB
Mjk UPP k

 sQ j N
=−

 X
k∈JA∪JB
Mjk

Ik∈JA
sQ B
α(1−s Q B)(1−s Q k ) +I k∈JB
sQ A
α(1−s Q A)(1−s Q k )
!
 sjN
=−
 N
α
  sQ AsQ B
(1−s Q A)(1−s Q B)
! X
k∈JA∪JB
Mjk
sQ j
sQ k

Ik∈JA
sQ k /(1−s Q k )
sQ A/(1−s Q A) +I k∈JB
sQ k /(1−s Q k )
sQ B/(1−s Q B)
!
.
29Also see the derivation in the Online Appendix A of Caradonna et al. (2024).
23

Finally, using ∆CS= P j∈JA∪JB ∆CS j gives
∆CS=−
 N
α
  sQ AsQ B
(1−s Q A)(1−s Q B)
! X
j,k∈JA∪JB
Mjk
sQ j
sQ k

Ik∈JA
sQ k /(1−s Q k )
sQ A/(1−s Q A) +I k∈JB
sQ k /(1−s Q k )
sQ B/(1−s Q B)
!
=−
 N
α
  ∆HHI Q AB
(1−s Q A)(1−s Q B)
! X
j,k∈JA∪JB
Mjk
sQ j
sQ k

1
2 Ik∈JA
sQ k /(1−s Q k )
sQ A/(1−s Q A) + 1 2 Ik∈JB sQ k /(1−s Q k ) sQ B/(1−s Q B) ! .
A.2.2 CES
Under a CES preference assumption, upward pricing pressure has a close relationship withrevenue
diversion ratios, defined asD R j→l ≡ −(∂Rl/∂pj)/(∂Rj/∂pj). Koh (2025) shows that forj̸=k,
(1 +ϵ −1 jj )DR j→k =D j→k pk pj ,(15)
whereϵ jj = (∂qj/∂pj)/(qj/pj) is productj’s own-price elasticity of demand. Plugging in (15) into
the GUPPI (GUPPI j ≡UPP j/pj) equation gives
GUPPI j = (1 +ϵ −1 jj ) X
l∈JB
mlDR j→l.(16)
I can simplify theGUPPI j expression as follows. Under CES demand, the revenue diversion
ratio isD R j→l = sR l 1−sR j (Koh, 2025; Caradonna et al., 2024) and the relative margins satisfy (14).
Using the fact that
Rj =
vjp1−σ j
1 + P l∈J vlp1−σ l Y,
I can also show that the own-price elasticity of revenue isϵ R jj = ∂sR j ∂pj pj sR j =−(1−s R j )(σ−1).Then,
sinceϵ R jj =ϵ jj + 1 (Koh, 2025), I have
1 +ϵ −1 jj = ϵR jj ϵR jj −1 = (1−s R j )(σ−1) 1 + (1−s R j )(σ−1) .
24

Then,GUPPI j forj∈ JA simplifies to
GUPPI j = (1 +ϵ −1 jj ) X
k∈JB
mkDR j→k
=

(1−s R j )(σ−1)
1 + (1−s R j )(σ−1)
! X
k∈JB
1
1 + (1−s R B)(σ−1)
sR k
1−s R j
= (σ−1)s R B
(1 + (1−s R j )(σ−1))(1 + (1−s R B)(σ−1)) .
In sum,GUPPI j for an arbitraryj∈ JA ∪ JB can be rewritten as
GUPPI j =I j∈JA
(σ−1)s R B
(1 + (1−s R j )(σ−1))(1 + (1−s R B)(σ−1))
+I j∈JB
(σ−1)s R A
(1 + (1−s R j )(σ−1))(1 + (1−s R A)(σ−1)) .
Next, lettingR j =p jqj,
∆CS j =−∆p j ×q j
=− ∆pj
pj
×R j
=−

 X
k∈JA∪JB
Mjk GUPPI k

 sR j Y
=−
 Y
σ−1
  ∆HHI R AB
( σ σ−1 −s R A)( σ σ−1 −s R B)
!
×
X
k∈JA∪JB
Mjk
sR j
sR k
 1
2 Ik∈JA
sR k /(1 + (1−s R k )(σ−1))
sR A/(1 + (1−s R A)(σ−1)) + 1 2 Ik∈JB sR k /(1 + (1−s R k )(σ−1)) sR B/(1 + (1−s R B)(σ−1)) 
Finally, since ∆CS= P j∈JA∪JB ∆CS j, summing over the above expression overj∈ JA ∪ JB gives
the desired expression.
A.3 Proof of Proposition 2
First, thatρ 1 = φ (φ−sA)(φ−sB) → 1 φ as (s A, sB)→(0,0) is straightforward from the definition of
ρ1. Second, the positive monotonicity ofρ 1 with respect to the merging firms is trivial. Finally,
verifying thatρ 1 is strictly convex in (sA, sB) ifs A < φands B < φis also straightforward and can
25

be checked by examining the positive definiteness of the Hessian, which is
H=


2φ
(φ−sA)3(φ−sB)
φ
(φ−sA)2(φ−sB)2
φ
(φ−sA)2(φ−sB)2
2φ
(φ−sA)(φ−sB)3

 .
A.4 Proof of Proposition 3
To capture the assumption that the market shares are approaching zero, I assume merging firms’
product-level shares are approaching zero at the same rate. Lets j =γ jsf , whereγ j >0 is a
constant such that P j∈Jf γj = 1. Thus, I can consider the behavior ofρ 2 ass f →0 forf=A, B.
I also assume that the two firms’ shares are approaching zero at the same rate. Then, for each
l∈ JA ∪ JB, I have
sl
1−sl
sf
1−sf
=
γlsf
1−γlsf
sf
1−sf
= γl(1−s f ) 1−γ lsf sf ↓0 − →γl.
Recalling from Lemma 1 thatM→φIas the shares approach zero, I have
ρ2 = 1 φ X j,l∈JA∪JB Mjl sj sl  1 2 Il∈JA sl/(φ−s l) sA/(φ−s A) + 1 2 Il∈JB sl/(φ−s l) sB/(φ−s B) 
→ 1 φ X l∈JA∪JB φ  1 2 Il∈JAγl + 1 2 Il∈JB γl  = X l∈JA∪JB γl 2 = 1,
where the last equality follows from having P l∈JA γl = 1 and P l∈JB γl = 1.
B Simulation
I follow the simulation steps in Miller et al. (2017b) with a slight modification. The overall steps
are described as follows.
1. Setk= 6 as the number of firms. Assume all pre-merger prices are equal to one. 30 Draw
a random length-(k+ 1) vector of shares from the Dirichlet distribution with parameter
θ= (1, ...,1)∈R 7. The shares represent quantity shares in the case of MNL and revenue
shares in the case of CES. Note that outside option is included. Draw relative marginm 1
30Setting all pre-merger prices to one allows us to equate the absolute change and the relative change in price.
26

from the uniform distribution with support [0.3,0.6]. I assume all firms’ pre-merger prices
are equal to 1.
2. Using the observed shares and margin of firm 1, identify (calibrate) the price responsiveness
parameter (αfor MNL andσfor CES) and the pre-merger values of{µ f }f∈F ,{T f }f∈F , and
Has follows. (See Caradonna et al. (2024) for derivations.)
•In the MNL case, I use
H← 1 1− P f∈F sf (17)
µf ← 1 1−s f ,∀f∈ F(18)
Tf ←Hs f exp
 1
1−s f

,∀f∈ F(19)
α←µ 1/(p1 −c 1) =µ 1/m1 (20)
•In the CES case, I use
H← 1 1− P f∈F sR f (21)
σ←
 1
m1
−1
  1
1−s R 1

+ 1 (22)
µf ← 1 1− σ−1 σ sR f ,∀f∈ F(23)
Tf ←s R f H  1− µf σ 1−σ ,∀f∈ F(24)
I also compute the upward pricing pressure using pre-merger values of margins and shares.
3. I assume Firms 1 and 2 merge without synergy. LetT M ≡T 1 +T 2 be the type of the merged
firm. I solve for the post-merger equilibrium using the system of equations described in Online
Appendix A.
4. Using the pre-merger and post-merger equilibrium values, I calculate the actual price in-
creases and changes in consumer surplus. The change in consumer surplus is calculated after
normalizingV 0 = 1 in both logit and CES cases.
27

5. I repeat the above 50,000 times. I discard observations that fail to find the post-merger
equilibrium due to numerical issues. 31
C Misspecification
Considering demand function misspecification is crucial in merger analysis because inaccurate as-
sumptions about how consumers substitute between products can bias estimates of diversion ratios,
pass-through rates, and price elasticities. This not only distorts predictions of post-merger prices
but also misstates changes in consumer surplus, which depend on the full shape of the demand
curve. As a result, regulators may mistakenly approve harmful mergers, block beneficial ones, or
design ineffective remedies, underscoring the importance of testing alternative demand models to
ensure credible and robust welfare assessments.
I briefly discuss the implications of model misspecification in the context of the simulation
exercise presented in Section 5. The simulation setting is convenient because pre-merger prices are
normalized to one, allowing me to treat quantity shares and revenue shares as equivalent. Recall
that under the single-agent assumption and the approximationM≈φI, the consumer welfare
effect of a merger can be expressed as ∆CS≈ −V0 ×r(φ)×∆HHI AB, wherer(φ)≡ φ (φ−sA)(φ−sB) .
Note thatr(φ) is strictly decreasing inφ, as taking the derivative givesr ′(φ) = sAsB−φ2 (φ−sA)2(φ−sB)2 <0.
Sinceφ= 1 under the multinomial logit model,φ= σ σ−1 >1 under the CES model, and
r(φ) decreases withφ, it follows that|∆CS MNL|>|∆CS CES |. In other words, applying the MNL
formula yields a larger predicted merger harm than using the CES formula. This result aligns with
the earlier finding that the first-order approach with CES demand tends to underpredict merger
price and welfare effects relative to MNL.
Figure 8 illustrates this relationship by plotting predicted ∆CS MNL against ∆CS CES (with
V0 = 1). Overall, the MNL formula produces systematically higher welfare loss predictions. While
the relative rankings of mergers are often preserved across the two models, they are not always
identical. Since the gap between the two approximations is zero whenφ= 1 and widens asφ
increases, we can infer that whether the rankings remain consistent depends on the estimated value
of CES price responsiveness parameterσ.
31Although using multiple starting points can improve the chance of convergence, I instead chose to increase the
number of simulation experiments.
28

Figure 8: The Impact of Demand Misspecification on Prediction of Merger Welfare Effects
(a) When DGP is Logit
 (b) When DGP is CES
References
Ashenfelter, Orley C, Daniel S Hosken, and Matthew C Weinberg (2015) “Efficiencies brewed:
pricing and consolidation in the US beer industry,”The RAND Journal of Economics, 46 (2),
328–361.
Bhattacharya, Vivek, Gast´ on Illanes, and David Stillerman (2023) “Merger effects and antitrust
enforcement: Evidence from US retail,”Available at SSRN 4410802.
Caradonna, Peter, Nathan Miller, and Gloria Sheu (2024) “Mergers, entry, and consumer welfare,”
Georgetown McDonough School of Business Research Paper(3537135).
Chen, Viola (2010) “The evolution of the baby food industry, 2000–2008,”Journal of Competition
Law and Economics, 6 (2), 423–442.
Farrell, Joseph and Carl Shapiro (2010) “Antitrust evaluation of horizontal mergers: An economic
alternative to market definition,”The BE Journal of Theoretical Economics, 10 (1), 1–41.
Froeb, Luke M and Gregory J Werden (1998) “A robust test for consumer welfare enhancing mergers
among sellers of a homogeneous product,”Economics Letters, 58 (3), 367–369.
Jaffe, Sonia and E Glen Weyl (2013) “The first-order approach to merger analysis,”American
Economic Journal: Microeconomics, 5 (4), 188–218.
Kim, E Han and Vijay Singal (1993) “Mergers and market power: Evidence from the airline
industry,”The American Economic Review, 549–569.
Koh, Paul (2025) “Merger Analysis with Unobserved Prices,”arXiv preprint arXiv:2404.07684.
Koh, Paul S (2024) “Market Definition: A Sensitivity Analysis,”arXiv preprint arXiv:2407.12774.
Miller, Nathan H, Matthew Osborne, and Gloria Sheu (2017a) “Pass-through in a concentrated
industry: empirical evidence and regulatory implications,”The RAND Journal of Economics, 48
(1), 69–93.
Miller, Nathan H, Marc Remer, Conor Ryan, and Gloria Sheu (2016) “Pass-through and the pre-
diction of merger price effects,”The Journal of Industrial Economics, 64 (4), 683–709.
29

(2017b) “Upward pricing pressure as a predictor of merger price effects,”International
Journal of Industrial Organization, 52, 216–247.
Miller, Nathan H and Gloria Sheu (2021) “Quantitative methods for evaluating the unilateral effects
of mergers,”Review of Industrial Organization, 58, 143–177.
Nocke, Volker and Nicolas Schutz (2018) “Multiproduct-firm oligopoly: An aggregative games
approach,”Econometrica, 86 (2), 523–557.
(2025) “An Aggregative Games Approach to Merger Analysis in Multiproduct-Firm
Oligopoly,”The RAND Journal of Economics, 56 (3), 233–250.
Nocke, Volker and Michael D Whinston (2022) “Concentration thresholds for horizontal mergers,”
American Economic Review, 112 (6), 1915–1948.
Prager, Robin A and Timothy H Hannan (1998) “Do substantial horizontal mergers generate signif-
icant price effects? Evidence from the banking industry,”The Journal of Industrial Economics,
46 (4), 433–452.
Shapiro, Carl (2010) “The 2010 horizontal merger guidelines: From hedgehog to fox in forty years,”
Antitrust LJ, 77, 49.
Spiegel, Yossi (2021) “The Herfindahl-Hirschman Index and the Distribution of Social Surplus,”
The Journal of Industrial Economics, 69 (3), 561–594.
Valletti, Tommaso and Hans Zenger (2021) “Mergers with differentiated products: Where do we
stand?”Review of Industrial Organization, 58, 179–212.
Weyl, E Glen and Michal Fabinger (2013) “Pass-through as an economic tool: Principles of incidence
under imperfect competition,”Journal of political economy, 121 (3), 528–583.
30

Online Appendix for
Concentration-Based Inference for Evaluating Horizontal Mergers
Paul S. Koh
September 20, 2025
A Review of Aggregative Games Framework
I review Nocke and Schutz (2018)’s aggregative games framework, which I use as a framework for
the simulation exercises described in the paper.
A.1 Model Primitives
I consider Nocke and Schutz (2018)’s aggregative games framework with CES/MNL demand. 32 A
multiproduct-firm oligopoly model is specified as a tuple
⟨J,F,(c j)j∈J , y, V0, H0,(h j)j∈J ⟩.(25)
Jis a finite set of products;Fis a finite set of firms that form a partition overJto represent
product ownership;c j is the marginal cost of producing productj∈ J;yis the representative
consumer’s income;V 0 >0 is the market size parameter;H 0 ≥0 is a baseline utility parameter 33;
finally,h j :R ++ →Ris defined as
hj(pj) =



exp(vj −αp j) (MNL)
vjp1−σ j (CES)
,
whereα >0 andσ >1 are the price responsiveness parameters that determine the price elasticities
and the substitutability of products.
Model primitives in (25) determine consumer demand functions as follows. The representative
32I also refer the readers to the appendix of Caradonna et al. (2024) for a practitioner’s guide to the aggregation
games framework of Nocke and Schutz (2018).
33logH 0 is interpreted as the value of the outside option. Typical empirical models setH 0 = 1.
A1

consumer’s quasilinear indirect utility function isy+V(p), whereV(p)≡V 0 logH(p) andH(p)≡
H0 + P j∈J hj(pj). The functionV(p) measures consumer welfare at pricep. Nocke and Schutz
(2018) refers toH=H(p) as the industry (market) aggregator. Applying Roy’s identity to the
indirect utility function gives the demand function:
qj(p) =V 0
−h′ j(pj)
H(p) .(26)
Demand functions in (3) are consistent with (26) ifH 0 = 1 andV 0 is given by (6).
A.2 Equilibrium Characterization
Nocke and Schutz (2018) shows that type aggregation property of logit and CES demand systems
can be used to summarize the equilibrium. The model primitives determine each firm’s type as
Tf ≡



P
l∈Jf exp(vl −αc l) (MNL)
P
l∈Jf vlc1−σ l (CES)
.(27)
With these demand systems, each firm finds it optimal to apply the same markup to all of its
products. To characterize the Bertrand equilibrium, it is convenient to define “ι-markups” as
µf ≡



α(pj −c j)∀j∈ J f (MNL)
σ pj −cj pj ∀j∈ Jf (CES)
.(28)
Theι-markups are proportional to the actual markups, either in levels (MNL) or percentages
relative to price (CES). The market aggregatorHis defined as
H≡



1 + P j∈J exp(vj −αp j) (MNL)
1 + P j∈J vjp1−σ j (CES) .(29)
Lets f = P j∈Jf sj be the market share of firmf. Nocke and Schutz (2018) shows that the
Bertrand equilibrium can be characterized as ({µ f }f∈F ,{s f }f∈F , H) (a vector ofι-markup, firm-
A2

level market shares, and a market aggregator) satisfying the following system of equations:
1 =



µf

1− Tf H exp(−µf )  (MNL)
µf

1− σ−1 σ Tf H (1− µf σ )σ−1  (CES) ,∀f∈ F,(30)
sf =



Tf
H exp (−µf ) (MNL)
Tf
H

1− 1 σ µf σ−1 (CES) ,∀f∈ F,(31)
1 = 1 H + X f∈F sf .(32)
A unique solution to this system of equations is guaranteed to exist. The equilibrium price of
each product is determined by the equilibrium value ofµ f . Firm-level profits can be expressed as
Πf =V 0(µf −1).(33)
The consumer surplus is determined by the value of the market aggregator:
CS(H) =V 0 log(H).(34)
B Merger Pass-Through Matrix Under Logit and CES
B.1 Logit
This section characterizes the pass-through matrix under the logit assumption. Recall that the
merger pass-through matrix is defined asM≡ −

∂h(ppre)
∂p
−1
, whereh(p post) = 0 characterizes
the post-merger FOC; eachh j(p) is normalized to be quasilinear in marginal cost. Let the merged
A3

firm’s profit function be P l∈JA∪JB (pl −c l)ql. For eachj∈ JA ∪ JB,
hj(p) =−q j
 ∂qj
∂pj
−1
−(p j −c j)−
X
l∈JA∪JB\j
(pl −c l)
 ∂ql
∂pj
 ∂qj
∂pj
−1
=−s j
 ∂sj
∂pj
−1
−(p j −c j)−
X
l∈JA∪JB\j
(pl −c l)
 ∂sl
∂pj
 ∂sj
∂pj
−1
=−s j
 −1
αsj(1−s j)

−(p j −c j)−
X
l∈JA∪JB\j
(pl −c l) (αsjsl)
 −1
αsj(1−s j)

= 1 α(1−s j) −(p j −c l) + X l∈JA∪JB\j (pl −c l) sl 1−s j .
Note that I useq j =s jNand ∂sj ∂pk =−α(I{j=k} −s j)sk (so that ∂sj ∂pj =−αs j(1−s j) and
∂sk
∂pj =αs jsk ifj̸=k).
The next step is to characterize ∂hj ∂pk forj, k∈ JA ∪ JB so that I can construct the (J A ∪ JB)×
(JA ∪ JB) matrix ∂h(p) ∂p . First, since d dx

1
1−x

= 1 (1−x)2 , ∂(pj −cj ) ∂pj = 1, and ∂(pl−cl) ∂pj = 0 ifl̸=j,
∂hj
∂pj
= 1 α 1 (1−s j)2 ∂sj ∂pj −1 + X l∈JA∪JB\j (pl −c l)  ∂sl ∂pj 1 1−s j +s l 1 (1−s j)2 ∂sj ∂pj 
= 1 α 1 (1−s j)2 (−αsj(1−s j))−1 + X l∈JA∪JB (pl −c l)  αslsj 1−s j +s l 1 (1−s j)2 (−αsj(1−s j)) 
=− sj
1−s j
−1
= −1 1−s j .
Next, fork̸=j,
∂hj
∂pk
= 1 α 1 (1−s j)2 ∂sj ∂pk + X l∈JA∪JB\j  ∂(pl −c l) ∂pk sl 1 1−s j + (pl −c l) ∂sl ∂pk 1 1−s j + (pl −c l)sl 1 (1−s j)2 ∂sj ∂pk 
= sjsk
(1−s j)2 +
X
l∈JA∪JB\j

I{l=k} sl
1−s j
+ (pl −c l)(−α(I{l=k} −sk)sl) 1 1−s j + (pl −c l) αslsjsk (1−s j)2

.
The pre-merger margin for each productjowned by firmfcan be calculated as (p j −c j) = 1 α(1−sf ) .
Thus, the matrix ∂h(ppre) ∂p and thus the merger pass-through matrix can be calculated from the pre-
merger shares (s j)j∈JA∪JB and the price responsiveness parameterα.
A4

In the special case of single-product firms, we can calculate the pass-through matrix as
M= (1−s A)3(1−s B)3
(1−s A −s B)(1−s A −s B + 2sAsB)


1
1−sB
sAsB
(1−sA)2(1−sB)
sAsB
(1−sA)(1−sB)2
1
1−sA

 .
B.2 CES
Under the CES demand assumption, the merger pass-through matrix is defined asM≡ −

∂h(˜p)
∂˜p
−1

˜p=˜ppre
,
where ˜pj ≡logp j, and eachh j(˜p) is normalized to be quasilinear in relative marginsm j = pj −cj pj .
As shown in Koh (2025), for eachj∈ J A ∪ JB,
hj(˜p) =−ε−1 jj −m j + (1 +ε −1 jj ) X
l∈JA∪JB\j
mlDR j→l,
whereε jj ≡ ∂qj ∂pj pj qj is the own-price elasticity of demand andD R j→l =− ∂Rl/∂pj ∂Rj /∂pj is the revenue
diversion ratio from productjto productl. Under the CES demand assumption, the revenue
diversion ratio and the own-price elasticity can be simplified asD R j→l = sR l 1−sR j andε jj = (1−
sR j )(1−σ)−1.
Let us characterize the matrix of ∂hj (˜p) ∂˜pk forj, k∈ JA ∪ JB. First,
∂hj
∂˜pj
=−

∂ε−1 jj
∂˜pj
!
− ∂mj
∂˜pj
+
∂(1 +ε −1 jj )
∂˜pj
X
l∈JA∪JB\j
mlDR j→l + (1 +ε −1 jj ) X
l∈JA∪JB\j
ml
∂D R j→l
∂˜pj
.
Koh (2025) shows that
∂ε−1 jj
∂˜pj =ε −2 jj sR j (1−s R j )(1−σ) 2, ∂ε−1 jj ∂˜pk = (−1)ε−2 jj sR j sR k (1−σ) 2, ∂mj ∂˜pj = 1−m j,
∂D R j→k
∂˜pj = 0, and
∂D R j→k
∂˜pk = (1−σ)

sR k (1−sR k )
1−sR j −
(sR k )2sR j
(1−sR j )2

. Then,
∂hj(˜p)
∂˜pj
=−ε −2 jj sR j (1−s R j )(1−σ) 2 −(1−m j) +ε −2 jj sR j (1−s R j )(1−σ) 2 X
l∈JA∪JB\j
mlDR j→l.
A5

Next, fork̸=j,
∂hj(˜p)
∂˜pk
=−

∂ε−1 jj
∂˜pk
!
+
∂(1 +ε −1 jj )
∂˜pk
X
l∈JA∪JB\j
mlDR j→l + (1 +ε −1 jj ) X
l∈JA∪JB\j

∂ml
∂˜pk
DR j→l +m l ∂D R j→l ∂˜pk !
=−

∂ε−1 jj
∂˜pk
!
+
∂(1 +ε −1 jj )
∂˜pk
X
l∈JA∪JB\j
mlDR j→l + (1 +ε −1 jj )

∂mk
∂˜pk
DR j→k +m k ∂D R j→k ∂˜pk !
+ (1 +ε −1 jj ) X
l∈JA∪JB\{j,k}
ml
∂D R j→l
∂˜pk
=ε −2 jj sR j sR k (1−σ) 2 + (−ε−2 jj sR j sR k (1−σ) 2) X
l∈JA∪JB\j
ml
sR l
1−s R j
+ (1 +ε −1 jj )

(1−m k) sR k 1−s R j +m k(1−σ)  sR k (1−s R k ) 1−s R j − (sR k )2sR j (1−s R j )2 !!
+ (1 +ε −1 jj ) X
l∈JA∪JB\{j,k}
ml(σ−1)

sR l sR k
1−s R j +
sR l sR j sR k
(1−s R j )2
!
Note that
∂D R j→l
∂˜pk = (σ−1)

sR l sR k 1 1−sR j +s R l (1−s R j )−2sR j sR k

forl̸=j, kand that that the pre-
merger relative marginm j = pj −cj pj for each productjowned by firmfcan be calculated asm j =
 1
σ
  1
1− σ−1 σ sf

=
 1
σ
  σ σ−1σ
σ−1 −sf

.34 Thus, the matrix ∂h(˜ppre) ∂˜p and thus the merger pass-through
matrix can be calculated from the pre-merger shares (s j)j∈JA∪JB and the price responsiveness
parametersσ.
34See the derivation in the Online Appendix A of Caradonna et al. (2024).
A6
