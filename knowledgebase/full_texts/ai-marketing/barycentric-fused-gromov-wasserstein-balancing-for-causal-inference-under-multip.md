---
title: Barycentric Fused Gromov-Wasserstein Balancing for Causal Inference under Multiple Treatments
url: https://arxiv.org/abs/2608.22024
category: ai-marketing
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Yuki Murakami
- Takumi Hattori
- Kohsuke Kubota
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.22024
pages: 26
chars: 100760
fetched_at: '2026-11-08T13:07:03+00:00'
kb_version: 1
---

# Barycentric Fused Gromov-Wasserstein Balancing for Causal Inference under Multiple Treatments

Barycentric Fused Gromov-Wasserstein Balancing
for Causal Inference under Multiple Treatments
Yuki Murakami1, Takumi Hattori1, Kohsuke Kubota2,
1 NTT DOCOMO, INC., Tokyo, Japan
2 Yokohama City University, Kanagawa, Japan
yuuki.murakami.xg@nttdocomo.com, takumi.hattori.zw@nttdocomo.com, kubota.kos.oy@yokohama-cu.ac.jp
Abstract
Estimatingheterogeneoussingleandinteractiontreatmentef-
fects from observational data under multiple simultaneous
treatments is crucial for decision-making. To mitigate esti-
mation variance, previous studies balance representation dis-
tributions between every pair of treatment patterns. How-
ever, such pairwise balancing scales quadratically with the
number of treatment patterns and fails to preserve consis-
tent local proximity structures across patterns, which de-
gradescounterfactualestimation.Toaddressthesechallenges,
we propose the Causal Inference for Heterogeneous Single
and Interaction Treatment Effects Network (CIHSI-Net), a
deep learning framework built on a novel Barycentric Fused
Gromov-Wasserstein Balancing (BFG-WB) objective. BFG-
WB aligns the representation distribution of each treatment
patternwithasharedWassersteinbarycenter,achievingglobal
alignmentwhilereducingthecomputationalcomplexityfrom
quadratic to linear, and its Fused Gromov-Wasserstein dis-
crepancypreservesthelocalproximitystructuresessentialfor
reliable heterogeneous effect estimation. Simulation studies
show that CIHSI-Net consistently outperforms state-of-the-
art baselines, and an application to real-world marketing data
demonstrates its practical utility in complex multi-treatment
scenarios.
1 Introduction
Estimating heterogeneous single and interaction treatment
effects under multiple simultaneous treatments is important
in many domains, such as healthcare and marketing. For ex-
ample, optimizing combination drug therapies requires un-
derstanding how these effects vary due to physiological dif-
ferences (e.g. Gradman et al. 2010; Sever et al. 2006). Simi-
larly, in marketing, promotion effectiveness depends heavily
on user attributes and their interactions (e.g. Blake, Nosko,
and Tadelis 2015; Lesscher, Lobschat, and Verhoef 2021).
Giventhatrandomizedtrialsareofteninfeasibleduetoethi-
calconcernsandthehighcostsassociatedwiththecombina-
torial explosion of treatment options, analytical frameworks
that can accurately estimate these effects from observational
data are essential for decision-making in real-world applica-
tions.
To enable such accurate estimation from observational
data, representation balancing with deep learning has
emergedasapromisingapproachtoaddresstheinherentse-
lection bias. This approach mitigates distributional discrep-
ancies between treatment and control groups by learning a
balanced representation (e.g. Shalit, Johansson, and Sontag
2017;Yaoetal.2018).Recently,CausalInferenceforSingle
and Interaction Treatment Effects Network (CISI-Net) ex-
tended this approach to the multiple-treatment setting (Mu-
rakami,Hattori,andKubota2025).Tohandlemultipletreat-
ments,thisapproachadoptsapairwisebalancingstrategythat
aligns distributions between specific pairs of treatment pat-
terns,whileintegratingataskembeddingnetworktoencode
the unique contributions of single and interaction effects.
However, existing pairwise balancing methods face
three critical limitations. First, they struggle to achieve
global alignment because reducing the discrepancy for one
treatment-pattern pair may increase the discrepancies be-
tween other treatment-pattern pairs, leaving residual imbal-
ancethatcanincreaseestimationvariance.Second,pairwise
constraintsgenerallydonotencourageconsistentlocalprox-
imity structures across all treatment patterns, and such in-
consistent geometric distortions can degrade heterogeneous
effect estimation (Cao, Zhang, and Li 2026; Wang et al.
2025; Yao et al. 2018). Third, the quadratic computational
complexity from matching all pairs makes these methods
impracticalforlarge-scaleapplicationswithnumeroustreat-
ment combinations.
To address these challenges, we propose the Causal In-
ference for Heterogeneous Single and Interaction Treatment
Effects Network (CIHSI-Net), which minimizes global dis-
tributional discrepancies while preserving local proximity
structures.CentraltoCIHSI-NetisanovelBarycentricFused
Gromov-WassersteinBalancing(BFG-WB)objective,which
aligns the representation distributions of each treatment pat-
tern to a shared Wasserstein barycenter (Agueh and Car-
lier 2011) using the Fused Gromov-Wasserstein (FGW) dis-
crepancy (Titouan et al. 2019; Vayer et al. 2020). This ap-
proach achieves global alignment and preserves local prox-
imity structures by accounting for both feature values and
geometry, while reducing computational complexity from
quadratic to linear.
Simulation results demonstrate that CIHSI-Net consis-
tently outperforms state-of-the-art baselines in estimating
both heterogeneous single and interaction effects. Further-
more, ablation studies confirm the critical contribution of
BFG-WB, and application to real-world marketing data val-
idates the practical utility of the proposed framework.
arXiv:2608.22024v1  [stat.ME]  22 Aug 2026

2 Related Work
Wereviewexistingresearchfromtwoperspectives:represen-
tation balancing methods and deep learning-based methods
for multiple treatments. First, deep learning-based represen-
tation balancing mitigates estimation variance arising from
selection bias in observational data by reducing the discrep-
ancybetweentherepresentationsofthetreatmentandcontrol
groups.OptimalTransport(OT)-basedregularization,which
globally aligns the representation distributions across treat-
ment groups, has proven effective for estimating the hetero-
geneous causal effect (Shalit, Johansson, and Sontag 2017;
Li et al. 2023). Motivated by the reliance of counterfactual
inference on local smoothness, recent extensions encourage
the preservation of local proximity structures within each
distribution by keeping input-space neighbors adjacent after
balancing (Yao et al. 2018, 2019) or by guiding the cross-
groupalignmentusinglocalneighborhoodgeometries(Wang
et al. 2025; Cao, Zhang, and Li 2026).
However, extending this pairwise balancing paradigm to
themultiple-treatmentsettingfacesfundamentallimitations.
For global alignment, balancing each pair of treatment pat-
terns separately (Murakami, Hattori, and Kubota 2025) al-
lows the alignment of one pair to degrade that of another,
leavingaresidualimbalance(Gong,Nie,andXu2022;Lian
et al. 2021), with a cost quadratic in the number of pat-
terns. For local structure preservation, pairwise objectives
promote geometric consistency only within pairs, not across
alltreatmentpatterns(Liu,Shao,andFu2016;Lu,Xing,and
Chen2025).Consequently,inamultiple-treatmentsetting,a
unified framework achieving scalable global balancing with
local geometry preservation remains an open challenge.
Second, instead of relying on pseudo-samples via data
augmentation (e.g. Qian, Curth, and van der Schaar 2021),
wefocusonarchitecture-drivenapproachesthatintrinsically
capture treatment interactions. These methods typically rely
on either separate outcome networks (e.g. Parbhoo, Bauer,
andSchwab 2021)orlatent-variable generativemodels(e.g.
Saini et al. 2019; Zou et al. 2020). However, separate net-
works often yield unstable estimates for rare treatment pat-
terns due to isolated parameters (Chu et al. 2022), while
latent-variablemethodssufferreducedrobustnesswhengen-
erative assumptions fail (Rissanen and Marttinen 2021).
Consequently, there remains a need for an architecture that
achieves efficient parameter sharing without strong genera-
tive assumptions.
To fulfill these needs, we propose a novel framework,
CIHSI-Net. The following section defines the problem set-
ting and the causal estimands necessary for our framework.
3 Preliminaries
Heterogeneous Effects under Multiple Treatments
Weformulatetheproblemofestimatingheterogeneoussingle
and interaction treatment effects under multiple treatments
with the potential outcomes framework (Rubin 2005). Let
D={(x i,t i, yi)}N i=1 denote an observed dataset ofNin-
dependent units. Here,X∈ X ⊆Rd denote the covariate
vector andT∈ T={0,1} K denote the vector ofKsi-
multaneousbinarytreatments,withrealizationsxandt.For
each uniti, a potential outcomeYi(t)∈Rexists for every
t∈ T,butonlythefactualoutcomey i =Y i(ti)isobserved.
LetY(t)andYrepresentthecorrespondingpopulation-level
random variables for the potential and factual outcomes, re-
spectively.
To identify causal effects of interest from the observed
data, we adopt the following three assumptions commonly
used in observational studies (Imbens and Rubin 2015).
Assumption 1(Stable Unit Treatment Value Assumption).
(1) no interference, meaning that the outcome of one unit is
unaffected by the treatment assignments of other units; and
(2) consistency of treatment, meaning that the potential out-
comescorrespondtowell-definedanduniquetreatments(i.e.,
yi =Y i(ti)).
Assumption2(Ignorability).Foranytreatmentpattern,the
potentialoutcomeisindependentoftheassignedtreatmentT
giventheobservedcovariatesX.Formally,forallt,Y(t)⊥
T|X.
Assumption 3(Overlap).Every unit has a non-zero prob-
ability of receiving any treatment pattern given its observed
covariates. Formally, for alltandx,0< P(T=t|X=
x)<1.
Based on these assumptions, we define our estimands of
interest: the Conditional Average Single Effect (CASE) and
the Conditional Average Interaction Effect (CAIE). Both es-
timands are defined using the conditional expected potential
outcome given by
µ(x,t) :=E  Y(t)|X=x  .(1)
First, the CASE for treatmentkquantifies the marginal ef-
fect of applying treatmentkin isolation compared to the
control group (no treatment). This estimand extends the
standard conditional average treatment effect in the single-
treatment setting (Abrevaya, Hsu, and Lieli 2015) to the
multi-treatment setting. The CASE is defined as
τCASE(k,x) :=µ(x,t +k)−µ(x,0),(2)
wheret +k is the one-hot vector for treatmentk.
Second, the CAIE quantifies interactions among a subset
of treatmentsS⊆ {1, . . . , K}(where|S| ≥2). We adopt
the additive scale, which aligns with decision-making based
on absolute outcome differences (e.g., revenue), and extend
theAverageInteractionEffect(AIE)(EgamiandImai2019)
to the conditional setting as follows.
τCAIE(S,x) :=
X
Q⊆S
(−1)|S|−|Q| µ  x,t (+Q)  ,(3)
wheret (+Q) denotes a vector with ones at indices inQand
zeros elsewhere. For example, in a two-treatment setting,
τCAIE({1,2},x)measures the deviation of the joint effect
att= (1,1)from the sum of the single effects of(1,0)and
(0,1).
We now establish that the estimands defined above are
identifiable from the joint distribution of the observed data
(x,t, y)under the stated assumptions.
Proposition1.UnderAssumptions1-3,CASEandCAIEare
identifiable from the observed data.
The proof is provided in Appendix A.1.

Figure 1: Illustration of neighborhood switching under
Wasserstein-basedrepresentationbalancing.Thegrayarrows
showOTcorrespondences.Wassersteinminimizationaligns
the two distributions but can map neighboring points to dis-
tant locations, distorting within-distribution neighborhood
relations; a structure-preserving match such asj↔j′ would
be desirable.
Motivation for Representation Balancing
Representation balancing mitigates estimation variance by
minimizing distributional discrepancies across treatment
groups. A widely adopted metric is the Wasserstein dis-
tance (e.g. Cheng et al. 2022; Shalit, Johansson, and Sontag
2017),whichusesOTtomeasuretheminimaltransformation
cost between distributions.
However, because the Wasserstein distance minimizes
only the aggregate point-to-point transport cost, it does not
explicitly account for local proximity structures within each
distribution (Wang et al. 2025). Here, the local proximity
structuresrefertotherelativegeometricrelationshipsamong
units within a specific treatment pattern. Consequently, as
illustrated in Figure 1, neighbors in one distribution may be
mappedtoscatteredlocationsinanother,potentiallyleading
to structural collapse.
This disruption of local proximity structures degrades the
accuracy of causal effect estimation. Counterfactual predic-
tion typically relies on the assumption of local smoothness,
where units with similar representations yield similar out-
comes (Li et al. 2019; Xu and Mannor 2012). Therefore, ac-
curate estimation of counterfactual outcomesY(t)benefits
from (i) reducing distributional discrepancies (global align-
ment) and (ii) ensuring that neighborhood consistency is
maintained across treatment patterns (local structure preser-
vation).
This issueis particularly criticalin themultiple-treatment
setting. When pairwise balancing is applied across numer-
ous treatment patterns, local structure preservation becomes
inconsistent, where the structural distortion may vary sig-
nificantly depending on the pair being aligned. Such non-
uniformity destabilizes the reference neighbors used for in-
ference, thereby degrading the estimation of heterogeneous
single and interaction effects.
To address these challenges, we propose a novel frame-
work that simultaneously achieves global alignment and lo-
cal structure preservation. We introduce a new architecture
incorporatingtheFGWdiscrepancytosatisfythesedualob-
jectives in the following section.
4 CIHSI-Net: The Proposed Framework
Barycentric Fused Gromov-Wasserstein Balancing
To overcome the limitations of pairwise balancing, we pro-
pose BFG-WB. BFG-WB functions as a regularization term
within our proposed CIHSI-Net, designed to achieve two
critical objectives simultaneously: (i) reducing estimation
variance induced by distributional imbalances globally by
aligning all treatment representations to a common anchor,
and(ii)preservinglocalproximitystructurestoensurestable
heterogeneous effect estimation.
Formally, BFG-WB minimizes the weighted sum of dis-
crepancies between the representation distribution of each
treatment patterntand a shared Wasserstein barycenterR∗ b.
UnlikestandardapproachesthatusetheWassersteindistance,
weemploytheFGWdiscrepancy(Titouanetal.2019;Vayer
etal.2020).Byintegratingthefeature-basedWassersteindis-
tancewiththestructure-basedGromov-Wassersteindistance,
the FGW discrepancy enables us to simultaneously achieve
global distribution alignment (Objective (i)) and local struc-
ture preservation (Objective (ii)). The BFG-WB regulariza-
tion termLϕ is defined as follows.
Lϕ =
X
t∈T
wtF(R t,R ∗ b ),(4)
whereR ∗ b is the Wasserstein barycenter, andRt denotes
the representation distribution onRfor treatment patternt.
F(·,·)measurestheFGWdiscrepancybetweentwodistribu-
tions,andw t >0isaweightsatisfying P t∈T wt = 1.Inthe following, we detail the two core components: the Wasser-
stein barycenterR∗ b and the FGW discrepancyF(·,·).
Wasserstein Barycenter.Following the formulation in
(Agueh and Carlier 2011), we define the Wasserstein
barycenterR ∗ b as the centroid distribution that minimizes
the weighted sum of squared Wasserstein distances from the
representation distributionsRt as follows.
R∗ b = argmin
Rb
X
t∈T
λtW 2 2 (Rt,R b),(5)
whereW 2(·,·)is the 2-Wasserstein distance (see Ap-
pendix A.3.1 for its definition).R b denotes a barycenter
candidate distribution, andλt ≥0represents the weight for
treatment patterntsatisfying P t∈T λt = 1.
Crucially, the introduction of the Wasserstein barycenter
R∗ b resolvestheoptimizationconflictsinpairwisebalancing.
In standard pairwise approaches, minimizing the discrep-
ancy for one pair of treatments may inadvertently increase
it for another due to differing OT plans, which leads to per-
sistent local imbalances associated with selection bias. In
contrast, our approach adopts a “star-shaped” (See Figure 2)
alignment strategy where all representation distributions are
updated toward a single, fixed reference (barycenter)R∗ b.
This alignment strategy promotes coherent alignment and
effectivelymitigatesestimationvarianceacrossalltreatment
patterns (See Appendix A.3.2).
Fused Gromov-Wasserstein Discrepancy.With the
barycenterR ∗ b established as the global anchor, we employ

Figure 2: Conceptual illustration of BFG-WB. The gray ar-
rows show a subset of OT correspondences. By evaluating
the FGW discrepancy, the alignment is encouraged to pre-
serve within-distribution neighborhood relations.
the FGW discrepancy to measure the discrepancy between
the representation distributionRt of each treatment pattern
tandR ∗ b. The FGW discrepancy integrates the Wasserstein
distance(forglobaldistributionalignment),whichevaluates
featurevalues,andtheGromov-Wassersteindistance(forlo-
cal proximity structure preservation), which evaluates the
geometric structure within distributions, under a single OT
planπ (t). Specifically, the FGW discrepancyF(Rt,R ∗ b )is
defined as follows.
F(R t,R ∗ b ) = inf π(t)∈Π(Rt,R∗ b )
"
η
Z
c(t)(r,z)dπ (t)(r,z)
+ (1−η)
Z Z
d(t) b (r,r ′,z,z ′)dπ (t)(r,z)dπ (t)(r′,z ′)
#
,
(6)
whereΠ(R t,R ∗ b )denotes the set of all couplings on
R × Rwith marginalsRt andR ∗ b. Here,r,r ′,z,z ′ ∈ R
withr,r ′ ∼R t andz,z ′ ∼R ∗ b. The first term ac-
counts for global distribution alignment, wherec(t)(r,z) =
∥r−z∥ 2 measures the Euclidean distance between fea-
tures. The second term accounts for local proximity struc-
turepreservation.Specifically,wedefined (t) b (r,r ′,z,z ′) :=
d(t)(r,r ′)−d (b)(z,z ′) 2 , whered(t)(r,r ′) =∥r−r ′∥2
andd (b)(z,z ′) =∥z−z ′∥2representthewithin-distribution
distances (local geometry) within the treatment representa-
tiondistributionandthebarycenter,respectively.Thehyper-
parameterη∈(0,1]controls the trade-off between the first
term(globaldistributionalignment)andthesecondterm(lo-
cal proximity structure preservation).
ThesecondterminEquation(6)playsanimportantrolein
ourframework.Thistermincursalowcostonlywhenpairsof
pointsthatarecloseintherepresentationspaceoftreatmentt
arematchedtopairsthataresimilarlycloseinthebarycenter,
thereby penalizing structure-blind matching based solely on
feature similarity. This mechanism mitigates distortions in
neighborhood geometry by aligning each distribution to the
localproximitystructureofthebarycenter.Asaresult,itpre-
vents counterfactual prediction from being performed using
neighborhoods that mix units with different heterogeneity
patterns.Thisconsistencysignificantlyimprovestheestima-
tion stability of heterogeneous causal effects, because such
estimation depends on covariate-conditioned counterfactual
prediction.
Beyond its methodological advantages in estimation vari-
ance reduction and structure preservation, BFG-WB of-
fers a significant practical benefit: computational efficiency.
Whereas pairwise balancing requires comparing all pairs of
treatment patterns, our star-shaped strategy compares each
patternonlywiththebarycenter.Weformalizethisadvantage
in the following proposition.
Proposition 2(Computational Efficiency).LetL= 2 K de-
notethenumberoftreatmentpatternsderivedfromKbinary
treatments,andletoneevaluationdenotethecomputationof
a single OT-based discrepancy between two empirical dis-
tributions. Per training step, standard pairwise balancing
requires
L
2

=O(L 2)evaluations, whereas BFG-WB re-
quires at most(Lb + 1)L=O(L)evaluations, whereL b
denotes a fixed upper bound on the number of barycenter-
update iterations and is independent ofL.
AdetailedderivationisprovidedinAppendixA.2,andwe
empiricallyverifythisscalabilityadvantagethroughruntime
comparisons in Appendix D.1
Theoretical Analysis
In this section, we demonstrate that BFG-WB provides the-
oretically sound error control for estimating both CASE and
CAIE from observational data. Although accurate causal ef-
fect estimation requires controlling for prediction errors un-
derallpossibletreatmentpatterns,counterfactualprediction
errors cannot be minimized directly because only factual
outcomes are observed.
To bridge this gap, we draw upon the theoretical frame-
work of representation-based causal inference (Wang et al.
2025).Akeyinsightfromthisliteratureisthattheprediction
error on the unobserved target domain (counterfactuals) is
theoretically bounded by the error on the observed source
domain (factuals) plus a discrepancy measure between their
distributions. Motivated by this principle, we derive upper
boundsfortheestimationerrorsofCASEandCAIEthatare
expressible solely through observational quantities. Specif-
ically, we demonstrate that these errors are bounded by the
sumofthefactualpredictionerrorandthedistributionaldis-
crepancies, which are explicitly minimized by the proposed
BFG-WB.
The accuracy of the estimated CASE and CAIE is as-
sessed using the integrated squared error with respect to the
marginal covariate distributionp(x). These metrics quan-
tify the expected squared deviation between the estimated
and true causal effects, defined analogously to the Precision
in Estimation of Heterogeneous Effects (PEHE) (Hill 2011)
usedinsingle-treatmentstudies.Formally,theestimationer-
rors of CASE and CAIE are defined as follows.
ϵCASE(k) =
Z
X
(ˆτCASE (k,x)−τ CASE (k,x)) 2 p(x)dx,
(7)

ϵCAIE(S) =
Z
X
(ˆτCAIE (S,x)−τ CAIE (S,x)) 2 p(x)dx,
(8)
whereˆτCASE(·)andˆτ CAIE(·)denote the estimated CASE
andCAIE.Foreachtreatmentpatternt,theexpectedpredic-
tion error of the factual outcome is defined as follows.
ϵ(t) F =
Z
X
l(x,t)p(x|t)p(t)dx,(9)
wherel(x,t) =
R
Y(t)−ˆµ(x,t)
2
p

Y(t)|x

dY(t)
denotes the conditional expected squared prediction loss,
andˆµ(x,t)denotes the estimate ofµ(x,t).
Formally, we establish the upper bounds forϵCASE and
ϵCAIE as follows.
Theorem1(UpperBoundforCASE).SupposethatAssump-
tions 1–3 and the auxiliary conditions in Appendix A.3.1
hold (in particular, the expected squared lossl(x,t)isBϕ-
Lipschitz in the representation space), and that the weights
in Equation(4)are uniform, i.e.,w t = 2−K. Then, for any
k∈ {1, . . . , K},
ϵCASE(k)≤2
(
1
p(t+k) ϵ(t+k) F + 1 p(0) ϵ(0) F + 22K η BϕLϕ
)
.
Theorem 2(Upper Bound for CAIE).Under the same as-
sumptions as Theorem 1, consider an interaction setS⊆
{1, . . . , K}with|S| ≥2. Let(at)t∈T be a constant vector
reflectingthecombinatorialstructureofS(a t ∈ {−1,0,1}).
The estimation errorϵCAIE(S)is bounded by:
ϵCAIE(S)≤
 X
t∈T
a2 t
! (X
t∈T
1
p(t) ϵ(t) F
+ 2K+1
η Bϕ

2K −1  Lϕ
)
.
The detailed proofs for Theorem 1 and Theorem 2 are
providedinAppendixA.3.Thesetheoremsdemonstratethat
the estimation errors for CASE and CAIE are theoretically
upper-bounded by the sum of the factual prediction error
ϵ(t) F and the distributional discrepancy termLϕ. Crucially,
theseboundsexplicitlyhighlighttheinverseprobabilityterm
1/p(t), which formalizes the vulnerability of causal infer-
encetoraretreatmentpatterns.Furthermore,thedependence
on2 K in these bounds reflects the inherent combinatorial
complexity of estimating causal effects over all treatment
patterns. By aligning all treatment-pattern representation
distributions to a single fixed anchorR∗ b, our star-shaped
strategy efficiently minimizes all pairwise Wasserstein dis-
crepancies via the triangle inequality. Simultaneously, the
Gromov-Wasserstein component of the FGW discrepancy
preserves local proximity structures within the representa-
tion space. This structural preservation makes the Lipschitz
continuity assumption (Bϕ) more plausible in practice, sup-
porting counterfactual inference from nearby factual sam-
ples. Together, these results show that BFG-WB provides
both computational efficiency and a principled mechanism
for controlling the estimation errors of CASE and CAIE.
Figure3:ThearchitectureofCIHSI-Net.Themodelconsists
of three components: the representation learning networkϕ,
the task embedding networktw, and the outcome prediction
networkh. BFG-WB is a regularization term applied to the
latent representationϕ(x).
Network Architecture and Training Objective
We implement our proposed method using CIHSI-Net, a
neural network architecture designed to achieve both accu-
rateoutcomepredictionandrobustrepresentationbalancing.
AsillustratedinFigure3,thenetworkconsistsofthreecom-
ponents: a representation learning networkϕ:R d →R dr
regularized by BFG-WB, a task embedding networktw :
RK →R dt that captures treatment similarities, and the out-
come prediction networkh:R dr+dt →Rthat estimates
outcomes from the concatenated features.
Theentirenetworkisoptimizedbyminimizingacompos-
ite loss functionLthat balances factual prediction accuracy
with the distributional alignment constraints derived in our
theoretical analysis as follows.
L=L y +αL ϕ +β∥w∥ 2 2,(10)
wherethefirsttermL yrepresentsthefactualoutcomepredic-
tionerror,thesecondtermL ϕ istheBFG-WBregularization
term,andthethirdtermisanL2regularizationtermapplied
to the network weights. The coefficientsαandβare hy-
perparameters that control the strength of the corresponding
terms.
The outcome prediction lossLy is designed to align with
theerrorboundsestablishedinTheorems1and2.Guidedby
our theoretical analysis, which reveals that prediction errors
on rare treatment patterns are amplified by the inverse prob-
ability1/p(t), we employ an inverse-frequency weighted
mean squared error to counteract this imbalance as follows.
Ly = 1 N
NX
i=1
1
ˆp(ti) (yi −ˆyi)2,(11)
whereˆp(ti) = 1 N PN j=1 I[ti =t j]represents the empirical
frequency of the treatment pattern assigned to uniti.
5 Simulation Experiments
We evaluate our CIHSI-Net using simulation datasets to (i)
compare estimation accuracy with state-of-the-art baselines
and (ii) clarify the contributions of its components through
ablation studies.

Datasets.To assess estimation accuracy under selection
bias and heterogeneous effects, we generate two types of
simulationdatasetsfollowingtheprotocolinMurakami,Hat-
tori, and Kubota (2025). Simulation 1 (With Interactions) is
generatedwithcomplexinteractioneffectsamongtreatments
and serves as the primary benchmark for evaluating CASE
andCAIEestimation.Simulation2(WithoutInteractions)is
generated without interaction effects and tests the model’s
robustness by verifying that it does not produce spurious in-
teractioneffectswhennoneexist.Wefixthenumberoftreat-
mentsatK= 3andthesamplesizeatN= 50,000.Detailed
data generation processes are provided in Appendix B.
Experimental Setup.We compare CIHSI-Net with three
representative multi-treatment causal inference methods:
Task Embedding–based Causal Effect Variational Autoen-
coder(TECE-VAE)(Sainietal.2019),NeuralCounterfactual
RelationEstimation(NCoRE)(Parbhoo,Bauer,andSchwab
2021),andCISI-Net(Murakami,Hattori,andKubota2025).
Implementationdetailsforallbaselinesandthehyperparam-
eters of CIHSI-Net are provided in Appendix C. The same
network hyperparameter settings are applied across all ex-
periments. For CIHSI-Net, we setαin Equation (10) to 1.0
andηin Equation (6) to 0.6 for comparative experiments,
while fixingα= 1.0and varyingηfor ablation studies.
All models, including baselines, are trained using stan-
dard optimization protocols with 60% training, 10% valida-
tion, and 30% test data. A sensitivity analysis regarding the
regularization coefficients is presented in Appendix D.5.
Evaluation Metrics.Performance is evaluated using the
integrated squared errors for CASE and CAIE, as defined
in Equations (7) and (8). To ensure statistical reliability, we
report average metrics over 100 independent runs.
Accuracy Comparison against Baselines.Table 1 shows
ϵCASE andϵ CAIE of the proposed and baseline methods
across two simulation datasets. Across all simulation set-
tings, the proposed method consistently achieves the lowest
estimation errors for both CASE and CAIE, outperforming
all baseline methods. CIHSI-Net maintains high accuracy
regardless of whether interaction effects are present, and its
advantage over the baselines is most pronounced forϵCAIE,
indicating that BFG-WB is particularly beneficial for inter-
action treatment effect estimation. Further analysis in Ap-
pendix D.4 demonstrates that our CIHSI-Net effectively re-
ducesdistributionaldiscrepancies(measuredbyWasserstein
distance) while preserving local proximity structures (mea-
sured by Gromov-Wasserstein distance), thereby contribut-
ing to superior estimation performance. Moreover, CIHSI-
Net maintains its CASE and CAIE estimation advantage as
Kincreases to eight, demonstrating its scalability (see Ap-
pendix D.2), and achieves the best overall estimation perfor-
mance in the semi-synthetic setting (see Appendix D.6).
AblationStudy.Toverifythecontributionofeachcompo-
nentinourproposedmethod,weconductedanablationstudy
by varying the alignment strategy (with or without Wasser-
stein barycenter) and the discrepancy metric (Wasserstein
distance (W), Gromov-Wasserstein discrepancy (GW), and
FGW discrepancy (FGW)). Table 2 summarizes the results.
Detailed results forϵ CASE andϵ CAIE are reported in Ap-
pendix D.3.
First, the combination of the Wasserstein barycenter and
FGW discrepancy (No.7) consistently achieves the lowest
averageestimationerrorsforbothCASEandCAIE.Second,
methods using the Wasserstein barycenter generally outper-
formtheirpairwisecounterparts(compareNo.5-7withNo.2-
4).Thisfindingsuggeststhatpairwisediscrepancyminimiza-
tion is insufficient for globally reducing representation im-
balanceacrosstreatmentpatterns,whereasbarycentricalign-
mentmoreeffectivelymitigatesimbalance-drivenestimation
variance. Third, regarding the discrepancy metric, while the
FGW discrepancy fails to improve or even yields slightly
inferior results compared to the Wasserstein distance in the
pairwise setting (No.4 vs No.2), it improves performance
when combined with the Wasserstein barycenter (No.7 vs
No.5). These findings suggest that the structural preserva-
tion capability of FGW discrepancy is effective only when
supported by the global alignment provided by the Wasser-
stein barycenter.
6 Application to Multiple Marketing
Promotions
We apply CIHSI-Net to a real-world dataset from a mobile
payment platform to validate its effectiveness in capturing
heterogeneous causal effects. The dataset includes three si-
multaneouslyconductedpromotions:twoofflinepromotions
by the same merchant group (CP1, CP2) and one online pro-
motionbyadifferentmerchantgroup(CP 3).Theoutcomeis
definedasthetotalpaymentamountduringthepromotionpe-
riod,standardizedforconfidentiality.Usercovariatesinclude
71 features derived from service usage history and demo-
graphics. To analyze heterogeneity, we stratify users into 11
groups based on their payment amount in the pre-promotion
month. Hyperparameters are set to the best-performing con-
figuration from the simulation study (Section 5). Detailed
dataset statistics and preprocessing procedures are provided
in Appendix E.1.
Figure4showstheestimatedCASEandCAIEacrossuser
groupsobtainedfromasinglealgorithmrun.Thetoppanelin
Figure4showsthatallestimatedCASEsarepositive.Theon-
linepromotionCP 3exhibitsthestrongesteffectforlow-usage
users.Thisresultisconsistentwithfindingsthatonlineincen-
tives effectively encourage increased service spending, even
among users with little service experience (Blake, Nosko,
and Tadelis 2015; Langen and Huber 2023). In contrast, the
offline promotions (CP1, CP2) show modest increases for
higher-usage groups. These results suggest that user groups
for whom effects are strongly observed may differ across
channels and promotion designs.
The bottom panel in Figure 4 highlights the capabil-
ity of CIHSI-Net to capture complex interaction structures.
Whereas theestimated interactionbetween same-grouppro-
motions (τCAIE({1,2})) remains positive but declines with
usage, cross-group interactions show mixed patterns. No-
tably, the estimated three-way interactionτCAIE({1,2,3})
shifts from negative for low-usage users to positive for high-
usage users. This result suggests that, for users who regu-

ϵCASE ϵCAIE
Sim. Methodk= 1k= 2k= 3 S={1,2}S={2,3}S={1,3}S={1,2,3}
1
TECE-VAE 1.82±0.09 1.91±0.10 1.80±0.14 3.58±0.11 3.27±0.10 3.30±0.10 6.80±0.18
NCoRE 0.28±0.06 0.30±0.06 0.25±0.05 0.52±0.10 0.33±0.10 0.37±0.10 0.56±0.14
CISI-Net 0.22±0.04 0.24±0.03 0.19±0.06 0.31±0.07 0.11±0.04 0.15±0.08 0.31±0.08
CIHSI-Net 0.19±0.04 0.21±0.04 0.18±0.10 0.28±0.05 0.08±0.05 0.12±0.04 0.24±0.04
2
TECE-VAE 1.60±0.05 1.65±0.09 1.58±0.16 3.01±0.05 2.65±0.08 2.69±0.09 5.50±0.15
NCoRE 0.26±0.05 0.28±0.09 0.24±0.07 0.34±0.12 0.30±0.09 0.27±0.10 0.35±0.12
CISI-Net 0.16±0.04 0.19±0.070.16±0.05 0.08±0.08 0.07±0.04 0.07±0.05 0.11±0.09
CIHSI-Net 0.14±0.04 0.17±0.03 0.16±0.12 0.06±0.04 0.06±0.03 0.06±0.03 0.09±0.04
Table 1: Comparison of mean estimation errors and standard deviations forϵCASE andϵ CAIE in two simulation datasets. Here,
k∈ {1,2,3}indexes individual treatments, andS⊆ {1,2,3}(with|S| ≥2) denotes treatment combinations.
No. WB Penalty type Averageϵ CASE Averageϵ CAIE
1✗None 0.27±0.06 0.24±0.02
2✗W 0.22±0.03 0.22±0.03
3✗GW 0.25±0.06 0.24±0.03
4✗FGW 0.22±0.02 0.23±0.02
5✓W 0.22±0.04 0.21±0.02
6✓GW 0.22±0.04 0.22±0.03
7✓FGW0.19±0.04 0.18±0.02
Table 2: Ablation study results on simulation dataset 1. Av-
erageϵ CASE and Averageϵ CAIE denote the means of the
reportedϵ CASE andϵ CAIE values, respectively. WB indi-
cates whether the Wasserstein barycenter is used. Penal-
ties: Wasserstein (W), Gromov-Wasserstein (GW), Fused
GW (FGW), and None.
larly use the service, conducting more promotions simulta-
neously may yield complementary effects, whereas for low-
usageusers,presentingmultipleincentivesmaydivideatten-
tion (like choice overload (Chernev, Böckenholt, and Good-
man 2015)) and result in a negative interaction effect. Addi-
tional sensitivity and uncertainty analyses in Appendix E.2
show that the qualitative CASE and CAIE patterns remain
stable across the BFG-WB hyperparametersαandηand
are broadly consistent under bootstrap confidence intervals.
Theseresultshighlighttheimportanceofcapturingtreatment
effect heterogeneity and demonstrate the practical utility of
CIHSI-Net in revealing complex behavioral mechanisms,
such as coexisting synergistic and cannibalistic interactions
that vary substantially across user groups.
To further validate the generalizability of our CIHSI-Net,
we extended our analysis to a second real-world scenario in-
volvingpromotionsfromcompetingmerchants.Duetospace
constraints, detailed results demonstrating the detection of
cannibalization are provided in Appendix E.3.
7 Conclusion
This study addresses the limitations of pairwise balancing
in multi-treatment causal inference by proposing Causal
Inference for Heterogeneous Single and Interaction Treat-
mentEffectsNetwork(CIHSI-Net).ByintroducingBarycen-
tric Fused Gromov-Wasserstein Balancing (BFG-WB), our
Figure 4: Estimated CASE (top) and CAIE (bottom) across
user groups stratified by pre-promotion service usage.
framework achieves scalable global alignment via a Wasser-
stein barycenter while preserving local proximity structures
through the FGW discrepancy. Experiments on simulation
datasets demonstrate that CIHSI-Net outperforms baselines
in estimating heterogeneous single and interaction effects,
and a real-world marketing application illustrates its prac-
tical utility in multi-treatment settings. Several directions
remain for future work. First, a promising extension is to
replace the Wasserstein barycenter with an FGW barycen-
ter to unify global alignment and structural preservation,
enabling more consistent alignment of feature distributions
andwithin-distributiongeometry.Second,itwillbevaluable
toconnectCIHSI-Nettodownstreamdecision-making,such
as uplift-based allocation for combinatorial treatment.

References
Abrevaya, J.; Hsu, Y.-C.; and Lieli, R. P. 2015. Estimating
ConditionalAverageTreatmentEffects.JournalofBusiness
& Economic Statistics, 33(4): 485–505.
Agueh,M.;andCarlier,G.2011. BarycentersintheWasser-
steinSpace.SIAMJournalonMathematicalAnalysis,43(2):
904–924.
Ascarza, E. 2018. Retention Futility: Targeting High-Risk
Customers Might be Ineffective.Journal of Marketing Re-
search, 55(1): 80–98.
Blake, T.; Nosko, C.; and Tadelis, S. 2015. Consumer het-
erogeneity and paid search effectiveness: A large-scale field
experiment.Econometrica, 83(1): 155–174.
Breugelmans, E.; and Liu-Thompkins, Y. 2017. The effect
of loyalty program expiration policy on consumer behavior.
Marketing Letters, 28(4): 537–550.
Cao, F.; Zhang, J.; and Li, X. 2026. PITE: Multi-Prototype
Alignment for Individual Treatment Effect Estimation. In
Proceedings of the AAAI Conference on Artificial Intelli-
gence, volume 40, 19871–19879.
Chauhan, V. K.; Clifton, L.; Nigam, G.; and Clifton, D. A.
2025. Individualised Treatment Effects Estimation with
Composite Treatments and Composite Outcomes. In2025
47thAnnualInternationalConferenceoftheIEEEEngineer-
ing in Medicine and Biology Society (EMBC), 1–7. IEEE.
Cheng, M.; Liao, X.; Liu, Q.; Ma, B.; Xu, J.; and Zheng, B.
2022. Learning Disentangled Representations for Counter-
factualRegressionviaMutualInformationMinimization. In
Proceedings of the 45th International ACM SIGIR Confer-
enceonResearchandDevelopmentinInformationRetrieval,
SIGIR ’22, 1802–1806. New York, NY, USA: Association
for Computing Machinery. ISBN 9781450387323.
Chernev,A.;Böckenholt,U.;andGoodman,J.2015. Choice
overload: A conceptual review and meta-analysis.Journal
of Consumer Psychology, 25(2): 333–358.
Cho, H. J.; Chae, J.; Yoon, S.-H.; and Kim, D.-S. 2022.
Aging and the Prevalence of Polypharmacy and Hyper-
Polypharmacy Among Older Adults in South Korea: A Na-
tional Retrospective Study During 2010–2019.Frontiers in
Pharmacology, Volume 13 - 2022.
Chu, Z.; Ding, H.; Zeng, G.; Huang, Y.; Yan, T.; Kang,
Y.; and Li, S. 2022. Hierarchical Capsule Prediction Net-
work for Marketing Campaigns Effect. InProceedings of
the 31st ACM International Conference on Information &
KnowledgeManagement,CIKM’22,3043–3051.NewYork,
NY, USA: Association for Computing Machinery. ISBN
9781450392365.
Clevert,D.-A.;Unterthiner,T.;andHochreiter,S.2016. Fast
andAccurateDeepNetworkLearningbyExponentialLinear
Units (ELUs). arXiv:1511.07289.
Cuturi, M.; and Doucet, A. 2014. Fast Computation of
Wasserstein Barycenters. In Xing, E. P.; and Jebara, T.,
eds.,Proceedings of the 31st International Conference on
Machine Learning, volume 32 ofProceedings of Machine
Learning Research, 685–693. Bejing, China: PMLR.
Djulbegovic, B.; Elqayam, S.; Reljic, T.; Hozo, I.; Miladi-
novic, B.; Tsalatsanis, A.; Kumar, A.; Beckstead, J.; Taylor,
S.; and Cannon-Bowers, J. 2014. How do physicians decide
totreat:anempiricalevaluationofthethresholdmodel.BMC
Medical Informatics and Decision Making, 14(1): 47.
Dorotic, M.; Fok, D.; Verhoef, P. C.; and Bijmolt, T. H. A.
2021. Synergistic and cannibalization effects in a partner-
ship loyalty program.Journal of the Academy of Marketing
Science, 49(5): 1021–1042.
Efron, B.; and Tibshirani, R. J. 1994.An introduction to the
bootstrap. Chapman and Hall/CRC.
Egami,N.;andImai,K.2019. CausalInteractioninFactorial
Experiments: Application to Conjoint Analysis.Journal of
the American Statistical Association, 114(526): 529–540.
Freidlin, B.; Korn, E. L.; Gray, R.; and Martin, A. 2008.
Multi-Arm Clinical Trials of New Agents: Some Design
Considerations.Clinical Cancer Research, 14(14): 4368–
4371.
Genevay, A.; Peyre, G.; and Cuturi, M. 2018. Learning
Generative Models with Sinkhorn Divergences. In Storkey,
A.; and Perez-Cruz, F., eds.,Proceedings of the Twenty-
First International Conference on Artificial Intelligence and
Statistics, volume 84 ofProceedings of Machine Learning
Research, 1608–1617. PMLR.
Gong, F.; Nie, Y.; and Xu, H. 2022. Gromov-Wasserstein
Multi-modal Alignment and Clustering. InProceedings of
the 31st ACM International Conference on Information &
Knowledge Management, CIKM ’22, 603–613. New York,
NY, USA: Association for Computing Machinery. ISBN
9781450392365.
Gradman,A.H.;Basile,J.N.;Carter,B.L.;andBakris,G.L.
2010. Combination therapy in hypertension.Journal of the
American Society of Hypertension, 4(2): 90–98.
Hill, J. L. 2011. Bayesian Nonparametric Modeling for
Causal Inference.Journal of Computational and Graphi-
cal Statistics, 20(1): 217–240.
Imbens, G. W.; and Rubin, D. B. 2015.Causal inference
in statistics, social, and biomedical sciences. Cambridge
university press.
Kingma,D.P.;andBa,J.2017.Adam:AMethodforStochas-
tic Optimization. arXiv:1412.6980.
Kubota, K.; and Hoshino, T. 2025. Impact of lottery pro-
motion wins and losses: evidence from a promotion in a
mobile payment service.Asia Pacific Journal of Marketing
and Logistics, 1–19.
Kubota, K.; Ochiai, K.; and Hoshino, T. 2025. Causal effect
of lottery promotions on post-win payments: Evidence from
a large field experiment.Innovative Marketing, 21(2): 225–
236.
Langen,H.;andHuber,M.2023. Howcausalmachinelearn-
ingcanleveragemarketingstrategies:Assessingandimprov-
ingtheperformanceofacouponcampaign.Plosone,18(1):
e0278937.
LeCun,Y.;Bengio,Y.;andHinton,G.2015. Deeplearning.
Nature, 521(7553): 436–444.

Lesscher, L.; Lobschat, L.; and Verhoef, P. C. 2021. Do of-
flineandonlinegohandinhand?Cross-channelandsynergy
effects of direct mailing and display advertising.Interna-
tional Journal of Research in Marketing, 38(3): 678–697.
Li,J.;Jing,M.;Lu,K.;Zhu,L.;andShen,H.T.2019. Local-
ity Preserving Joint Transfer for Domain Adaptation.IEEE
Transactions on Image Processing, 28(12): 6103–6115.
Li, Q.; Wang, Z.; Liu, S.; Li, G.; and Xu, G. 2023. Causal
Optimal Transport for Treatment Effect Estimation.IEEE
Transactions on Neural Networks and Learning Systems,
34(8): 4083–4095.
Lian, X.; Jain, K.; Truszkowski, J.; Poupart, P.; and Yu, Y.
2021. Unsupervised multilingual alignment using Wasser-
steinbarycenter.InProceedingsoftheTwenty-NinthInterna-
tional Joint Conference on Artificial Intelligence, IJCAI’20.
ISBN 9780999241165.
Liu, H.; Shao, M.; and Fu, Y. 2016. Structure-Preserved
Multi-source Domain Adaptation. In2016 IEEE 16th Inter-
national Conference on Data Mining (ICDM), 1059–1064.
Liu, Y. 2007. The Long-Term Impact of Loyalty Programs
on Consumer Purchase Behavior and Loyalty.Journal of
Marketing, 71(4): 19–35.
Lu,M.;Xing,L.;andChen,B.2025. Measuringgeneralized
divergenceformultipledistributionswithapplicationtodeep
clustering.Pattern Recognition, 157: 110864.
Murakami, Y.; Hattori, T.; and Kubota, K. 2025. Multiple
TreatmentsCausalEffectsEstimationwithTaskEmbeddings
and Balanced Representation Learning. arXiv:2511.09814.
Muralidharan,K.;Romero,M.;andWüthrich,K.2025. Fac-
torialDesigns,ModelSelection,and(Incorrect)Inferencein
Randomized Experiments.The Review of Economics and
Statistics, 107(3): 589–604.
Nair, V.; and Hinton, G. E. 2010. Rectified linear units im-
prove restricted boltzmann machines. InProceedings of the
27th International Conference on International Conference
on Machine Learning, ICML’10, 807–814. Madison, WI,
USA: Omnipress. ISBN 9781605589077.
Parbhoo,S.;Bauer,S.;andSchwab,P.2021. NCoRE:Neural
CounterfactualRepresentationLearningforCombinationsof
Treatments. arXiv:2103.11175.
Parmar, M. K. B.; Barthel, F. M.-S.; Sydes, M.; Langley,
R.; Kaplan, R.; Eisenhauer, E.; Brady, M.; James, N.; Book-
man, M. A.; Swart, A.-M.; Qian, W.; and Royston, P. 2008.
SpeedinguptheEvaluationofNewAgentsinCancer.JNCI:
Journal of the National Cancer Institute, 100(17): 1204–
1214.
Qian, Z.; Curth, A.; and van der Schaar, M. 2021. Estimat-
ing Multi-cause Treatment Effects via Single-cause Pertur-
bation. InRanzato,M.;Beygelzimer,A.;Dauphin,Y.;Liang,
P.; and Vaughan, J. W., eds.,Advances in Neural Informa-
tion Processing Systems, volume 34, 23754–23767. Curran
Associates, Inc.
Rissanen, S.; and Marttinen, P. 2021. A critical look at
the consistency of causal estimation with deep latent vari-
able models. InProceedings of the 35th International Con-
ference on Neural Information Processing Systems, NIPS
’21. Red Hook, NY, USA: Curran Associates Inc. ISBN
9781713845393.
Rubin, D. B. 2005. Causal Inference Using Potential Out-
comes.Journal of the American Statistical Association,
100(469): 322–331.
Saini, S. K.; Dhamnani, S.; Srinivasan, A.; Ibrahim, A. A.;
and Chavan, P. 2019. Multiple Treatment Effect Estimation
using Deep Generative Model with Task Embedding. In
The World Wide Web Conference, WWW ’19, 1601–1611.
NewYork,NY,USA:AssociationforComputingMachinery.
ISBN 9781450366748.
Schweisthal,J.;Frauen,D.;Melnychuk,V.;andFeuerriegel,
S.2023. ReliableOff-PolicyLearningforDosageCombina-
tions. In Oh, A.; Naumann, T.; Globerson, A.; Saenko, K.;
Hardt,M.;andLevine,S.,eds.,AdvancesinNeuralInforma-
tion Processing Systems, volume 36, 67900–67924. Curran
Associates, Inc.
Sever, P.; Dahlöf, B.; Poulter, N.; Wedel, H.; Beevers, G.;
Caulfield, M.; Collins, R.; Kjeldsen, S.; Kristinsson, A.;
McInnes, G.; Mehlsen, J.; Nieminem, M.; O’Brien, E.; and
Östergren, o. b. o. t. A. S. C. M., Jan. 2006. Potential syn-
ergy between lipid-lowering and blood-pressure-lowering in
theAnglo-ScandinavianCardiacOutcomesTrial.European
Heart Journal, 27(24): 2982–2988.
Shalit, U.; Johansson, F. D.; and Sontag, D. 2017. Estimat-
ing individual treatment effect: generalization bounds and
algorithms. InPrecup,D.;andTeh,Y.W.,eds.,Proceedings
of the 34th International Conference on Machine Learning,
volume 70 ofProceedings of Machine Learning Research,
3076–3085. PMLR.
Sriperumbudur, B. K.; Fukumizu, K.; Gretton, A.;
Schölkopf,B.;andLanckriet,G.R.G.2010.Non-parametric
estimation of integral probability metrics. In2010 IEEE In-
ternational Symposium on Information Theory, 1428–1432.
Thakral,N.;andTô,L.T.2023.Whenareestimatesindepen-
dent of measurement units?Boston University-Department
of Economics.
Titouan, V.; Courty, N.; Tavenard, R.; Laetitia, C.; and Fla-
mary, R. 2019. Optimal Transport for structured data with
applicationongraphs. InChaudhuri,K.;andSalakhutdinov,
R., eds.,Proceedings of the 36th International Conference
onMachineLearning,volume97ofProceedingsofMachine
Learning Research, 6275–6284. PMLR.
Tsuboi,Y.;Sakai,Y.;Shimizu,R.;andGoto,M.2024. Mul-
tiple treatment effect estimation for business analytics using
observational data.Cogent Engineering, 11(1): 2300557.
Vayer,T.;Chapel,L.;Flamary,R.;Tavenard,R.;andCourty,
N.2020. FusedGromov-WassersteinDistanceforStructured
Objects.Algorithms, 13(9).
Villani, C.; et al. 2008.Optimal transport: old and new,
volume 338. Springer.
Wang, H.; Chen, Z.; Liu, Z.; Chen, X.; Li, H.; and Lin, Z.
2025. Proximity Matters: Local Proximity Enhanced Bal-
ancing for Treatment Effect Estimation. InProceedings of
the 31st ACM SIGKDD Conference on Knowledge Discov-
ery and Data Mining V.2, KDD ’25, 2927–2937. New York,

NY, USA: Association for Computing Machinery. ISBN
9798400714542.
Xu,H.;andMannor,S.2012. Robustnessandgeneralization.
Machine Learning, 86(3): 391–423.
Xu,J.;Li,Z.;Du,B.;Zhang,M.;andLiu,J.2020. Reluplex
mademorepractical:LeakyReLU.In2020IEEESymposium
on Computers and Communications (ISCC), 1–7.
Yamada, M.; Takezawa, Y.; Sato, R.; Bao, H.; Kozareva, Z.;
and Ravi, S. 2022. Approximating 1-Wasserstein Distance
with Trees. arXiv:2206.12116.
Yao, L.; Li, S.; Li, Y.; Huai, M.; Gao, J.; and Zhang, A.
2018. Representation Learning for Treatment Effect Esti-
mation from Observational Data. In Bengio, S.; Wallach,
H.;Larochelle,H.;Grauman,K.;Cesa-Bianchi,N.;andGar-
nett, R., eds.,Advances in Neural Information Processing
Systems, volume 31. Curran Associates, Inc.
Yao, L.; Li, S.; Li, Y.; Huai, M.; Gao, J.; and Zhang, A.
2019. ACE:AdaptivelySimilarity-PreservedRepresentation
LearningforIndividualTreatmentEffectEstimation.In2019
IEEE International Conference on Data Mining (ICDM),
1432–1437.
Zou, H.; Cui, P.; Li, B.; Shen, Z.; Ma, J.; Yang, H.; and He,
Y. 2020. Counterfactual Prediction for Bundle Treatment.
InLarochelle,H.;Ranzato,M.;Hadsell,R.;Balcan,M.;and
Lin, H., eds.,Advances in Neural Information Processing
Systems, volume 33, 19705–19715. Curran Associates, Inc.

Barycentric Fused Gromov-Wasserstein Balancing
for Causal Inference under Multiple Treatments (Supplementary Material)
A Proofs of Theoretical Results
A.1 Proof of Proposition 1
Lemma 1.Under Assumptions 1-3, the conditional expected potential outcomeµ(x,t)is identifiable from the observed data.
Proof.Theidentifiabilityoftheconditionalexpectedpotentialoutcomeisastandardresultinthepotentialoutcomeframework.
TheequalityholdsdirectlyfromAssumptions1and2,whileAssumption3ensurestheconditionalexpectedpotentialoutcome
is well-defined. For a detailed derivation, see, for example, Murakami, Hattori, and Kubota (2025).
■
Using Lemma 1, we prove that CASE and CAIE are identifiable.
Proof.Recall that the CASE for treatmentk, denoted asτCASE(k,x), is defined as
τCASE(k,x) :=µ(x,t +k)−µ(x,0),
wheret +k istheone-hotvectorfortreatmentk.Similarly,recallthattheCAIEforasetoftreatmentsS,denotedasτ CAIE(S,x),
is defined as
τCAIE(S,x) :=
X
Q⊆S
(−1)|S|−|Q| µ  x,t (+Q)  .
wheret (+Q) corresponds to the treatment vector where treatments in the subsetQare active.
According to Lemma 1, for any treatment vectort∈ {0,1}K, the termµ(x,t)is identifiable from the observed data as
E[Y|X=x,T=t].Bothτ CASE(k,x)andτ CAIE(S,x)areconstructedaslinearcombinationsofµ(x,t)forspecificvalues
oft. Since every termµ(x,t)in these equations is identifiable, any linear combination of them is also identifiable from the
observed data. Therefore, CASE and CAIE are identifiable.
■
A.2 Proof of Proposition 2
Proof.LetL= 2 K denote the total number of treatment patterns derived fromKbinary treatments.
Standard pairwise balancing evaluates an OT-based discrepancy for every unordered pair of distinct treatment-pattern repre-
sentation distributions. Therefore, the total number of evaluations per training step is
Npair =
L
2

= L(L−1) 2 =O(L 2).
For BFG-WB, the total number of evaluations consists of two components. First, for Wasserstein barycenter estimation, each
barycenter-update iteration solves one OT problem between the current barycenter and each of theLinput treatment-pattern
distributions(CuturiandDoucet2014).Therefore,underafixediterationbudgetofatmostL b barycenter-updateiterations,the
number of OT evaluations required for barycenter estimation satisfiesNbary ≤L bLwhereL b is independent ofL.
Second,afterthebarycenterhasbeenestimated,BFG-WBevaluatesoneFGWdiscrepancybetweentheestimatedbarycenter
and each treatment-pattern representation distribution. Hence, this step requiresNFGW =Ladditional evaluations. Conse-
quently, the total number of OT-based discrepancy evaluations required by BFG-WB per training step satisfies
NBFG-WB =N bary +N FGW ≤L bL+L= (L b + 1)L.
BecauseL b is fixed independently ofL, it follows that
NBFG-WB =O(L).
Thus, standard pairwise balancing requires a quadratic number of evaluations inL, whereas BFG-WB requires at most a linear
number of evaluations. ■
A.3 Proof of Theorems 1 and 2
This appendix details the proofs of Theorems 1 and 2, organized into three parts. First, we summarize the notation, definitions,
and key assumptions used throughout the proofs. Next, we present supporting lemmas that establish intermediate inequalities
connectingcounterfactuallosseswithdistributionaldiscrepancies.Finally,buildingontheseresults,weprovidethemainproofs
of Theorems 1 and 2, which demonstrate how barycenter-based balancing yields the stated upper bounds.

A.3.1 Setup and Definitions
Notation and setup.Letϕ:X → R ⊂R dr be the representation map, whereRis the representation space. For each
treatmentpatternt∈ T,wedenotebyp(x|t)thecovariatedistributionconditionalonT=t,anddefineR t asthedistribution
onRofr=ϕ(x)whenx∼p(x|t). Throughout the theoretical analysis,R t denotes the population distribution onR; in
practice, we use its empirical distribution computed from the observed samples in the treatment patternt. Given(x,t), we
formthepredictorinputbyconcatenatingtherepresentationandthetaskembeddingt w(t),anddefinethepointpredictorofthe
potential outcome asˆµ(x,t) :=h([ϕ(x), tw(t)])wherehis the outcome prediction network and[·,·]denotes concatenation.
Definition 1.For covariatesxand treatment patternt, define the conditional expected squared lossl(x,t) =
R
Y(t)−
ˆµ(x,t)
2
p

Y(t)|x

dY(t).The expected factual loss undertand the expected counterfactual loss for predicting outcomes
undertusing covariates drawn from other treatment patterns are:
ϵ(t) F =
Z
X
l(x,t)p(x|t)p(t)dx,(A.1)
ϵ(t) CF = X
t′∈T,t ′̸=t
Z
X
l(x,t)p(x|t ′)p(t ′)dx.(A.2)
Definition2.LetPandQbeprobabilitymeasuresonR ⊂R dr withfinitep-thmoments.Thep-Wassersteindistanceisdefined
as
Wp(P, Q):=

inf
π∈Π(P,Q)
Z
R×R
∥r−r ′∥p 2 dπ(r, r′)
1/p
,
whereΠ(P, Q)denotes the set of all couplings onR × Rwith marginalsPandQ.
Definition 3.LetFbe a class of real-valued functions onR. For two distributionsPandQonR, the integral probability
metric (IPM) induced byFis defined as
IPMF (P, Q) = sup
f∈F

 Z
R
f(r) (dP(r)−dQ(r))

 .
Assumption 1(Stable Unit Treatment Value Assumption).(1) no interference, meaning that the outcome of one unit is
unaffected by the treatment assignments of other units; and (2) consistency of treatment, meaning that the potential outcomes
correspond to well-defined and unique treatments (i.e.,yi =Y i(ti)).
Assumption 2(Ignorability).For any treatment pattern, the potential outcome is independent of the assigned treatmentT
given the observed covariatesX. Formally, for allt,Y(t)⊥T|X.
Assumption3(Overlap).Everyunithasanon-zeroprobabilityofreceivinganytreatmentpatterngivenitsobservedcovariates.
Formally, for alltandx,0< P(T=t|X=x)<1.
Assumption 4(Invertible representation map).The representation mapϕ:X → R ⊂Rdr is one-to-one onX. Without loss
of generality, we assume thatRis the image ofXunderϕ. Hence, there exists an inverse mapΨ :R → Xsuch that
Ψ(ϕ(x)) =x(∀x∈ X).
Assumption 5(Lipschitz loss in representation space).There exists a constantBϕ >0such that, for anyt∈ T, the function
gt(r) := 1 Bϕ l  Ψ(r),t 
belongs to the class of1-Lipschitz functions onR.
A.3.2 Supporting Lemmas
We present supporting lemmas and clarify their connections to the proofs of the main theorems. The lemmas can be grouped
into three categories.
First, Lemmas 2 and 3 relate counterfactual outcome losses to the corresponding factual outcome losses, plus Wasserstein
distances between treatment-specific representation distributions. Lemma 2 serves as a technical preparation for Lemma 3: it
shows that the increase in the expected outcome prediction loss fort′ under covariates (and thus representations) fromtis
controlled by the Wasserstein distance between the representation distributions oftandt′.
Lemma 2.Under Assumptions 1-5 , for anyt,t′ ∈ T, we have
Z
X
l(x,t ′)p(x|t)dx≤
Z
X
l(x,t ′)p(x|t ′)dx+B ϕW1(Rt,R t′).

Proof.By the definition ofRt and the Assumption 4, we obtain
Z
X
l(x,t ′)p(x|t)dx=
Z
R
l(Ψ(r),t ′)dR t(r),
Z
X
l(x,t ′)p(x|t ′)dx=
Z
R
l(Ψ(r),t ′)dR t′(r).
Therefore, we can rewrite the difference of expectations as an integral overRas follows.
Z
X
l(x,t ′)p(x|t)dx−
Z
X
l(x,t ′)p(x|t ′)dx
=
Z
R
l

Ψ(r),t ′  dRt(r)−dR t′(r) 
=B ϕ
Z
R
gt′(r)  dRt(r)−dR t′(r) 
≤B ϕ

 Z
R
gt′(r)  dRt(r)−dR t′(r) 

≤B ϕIPMF (Rt,R t′)(by Assumption 5),
whereF= Lip 1(R)denotes the set of all1-Lipschitz functions onR. By the Kantorovich-Rubinstein duality (Villani et al.
2008), the IPM over1-Lipschitz functions equals the 1-Wasserstein distance,
IPMF (Rt,R t′) =W 1(Rt,R t′).
Accordingly, we have Z
X
l(x,t ′)p(x|t)dx≤
Z
X
l(x,t ′)p(x|t ′)dx+B ϕW1(Rt,R t′).
■
Buildingonthisresult,Lemma3upper-boundsthecounterfactualoutcomelossfortreatmentpatterntbyitsfactualoutcome
loss plus Wasserstein discrepancies to other treatment patterns.
Lemma 3.Under the Assumptions 1-5, for any treatment patternt∈ T, the expected counterfactual loss satisfies
ϵ(t) CF ≤
 1
p(t) −1

ϵ(t) F +B ϕ X
t′̸=t
W1(Rt,R t′).
Proof.Applying Lemma 2 to eacht′ yields
Z
X
l(x,t)p(x|t ′)dx≤
Z
X
l(x,t)p(x|t)dx+B ϕ W1(Rt,R t′).(A.3)
Multiplying both sides of (A.3) byp(t′)and summing overt′ ̸=t, we obtain
ϵ(t) CF ≤ X
t′̸=t
p(t′)
Z
X
l(x,t)p(x|t)dx+B ϕ
X
t′̸=t
p(t′)W1(Rt,R t′)
=

X
t′̸=t
p(t′)


Z
X
l(x,t)p(x|t)dx+B ϕ
X
t′̸=t
p(t′)W1(Rt,R t′)
= (1−p(t))
Z
X
l(x,t)p(x|t)dx+B ϕ
X
t′̸=t
p(t′)W1(Rt,R t′)
=
 1
p(t) −1

ϵ(t) F +B ϕ X
t′̸=t
p(t′)W1(Rt,R t′)(by Definition in Equation (A.1))
≤
 1
p(t) −1

ϵ(t) F +B ϕ X
t′̸=t
W1(Rt,R t′).
where the last inequality holds becausep(t′)≤1andW 1(·,·)≥0.■

Second,Lemma4providesanupperboundonaggregatediscrepanciesacrossmultipletreatmentpatternsintermsofdistances
to a common Wasserstein barycenter. This bound demonstrates that the sum of all pairwise discrepancies can be controlled by
reducing the discrepancies between each representation distribution and the Wasserstein barycenter. This is exactly what our
barycenter-based regularization termLϕ enforces.
Lemma 4.LetTdenote the set of all treatment patterns with|T |= 2K. For anyp≥1, the following inequality holds:
X
{t,t′}∈( T 2 )
Wp(Rt,R t′)≤  2K −1  X
t∈T
Wp(R∗ b ,R t),
whereR ∗ b is a Wasserstein barycenter of{Rt}t∈T.
Proof.By the triangle inequality for thep-Wasserstein distance defined in Definition 2, for anyt,t′ ∈ T,
Wp(Rt,R t′)≤W p(Rt,R ∗ b ) +W p(R∗ b ,R t′).
Summing the above inequality over allorderedpairs(t,t′)witht̸=t ′ yields
X
t̸=t′
Wp(Rt,R t′)≤
X
t̸=t′
{Wp(Rt,R ∗ b ) +W p(R∗ b ,R t′)}
= (|T | −1)
X
t∈T
Wp(Rt,R ∗ b ) + (|T | −1) X
t∈T
Wp(R∗ b ,R t),
since eacht∈ Tappears exactly|T | −1times as the first element of an ordered pair.
Using the symmetry ofWp, we haveP t∈T Wp(Rt,R ∗ b ) = P t∈T Wp(R∗ b ,R t), and thus
X
t̸=t′
Wp(Rt,R t′)≤2(|T | −1)
X
t∈T
Wp(R∗ b ,R t).
Finally, noting thatP t̸=t′ Wp(Rt,R t′) = 2 P {t,t′}∈( T 2 ) Wp(Rt,R t′), we obtain
X
{t,t′}∈( T 2 )
Wp(Rt,R t′)≤(|T | −1)
X
t∈T
Wp(R∗ b ,R t) =  2K −1  X
t∈T
Wp(R∗ b ,R t),
which completes the proof. ■
Although this lemma holds for any anchor distribution, using the Wasserstein barycenter can yield a smaller right-hand side,
leading to a tighter anchor-based bound.
Third, Lemma 5 provides an upper bound that relates the above Wasserstein discrepancies to the FGW discrepancy adopted
in our objective, thereby allowing us to control the Wasserstein terms via FGW. Whereas replacing the Wasserstein terms with
anFGW-basedupperboundmayloosenthetheoreticalbound,introducingFGWiscrucialinpracticebecauseitencouragesthe
preservation of local proximity structures in the representation space.
Lemma 5.Let0< η≤1and letF(·,·)be the FGW discrepancy defined in Equation(6). Then, for any treatment pattern
t∈ T,
W1(Rt,R ∗ b )≤ 1 η F(R t,R ∗ b ).
Proof.For any couplingπ∈Π(R t,R ∗ b ), write the FGW objective asJ(π) =ηA(π) + (1−η)B(π), whereA(π)is the
feature-based transport cost andB(π)≥0is the structural term. By Definition 2,
A(π)≥inf
eπ∈Π(Rt,R∗ b ) A(eπ) =W1(Rt, R∗ b ).
Therefore,J(π)≥ηW 1(Rt,R ∗ b ).Takingtheinfimumoverπ∈Π(R t,R ∗ b )yieldsF(R t,R ∗ b )≥ηW 1(Rt,R ∗ b ),whichproves
the result. ■
Combining Lemmas 2 - 5, we can upper-bound the counterfactual outcome losses terms in Theorems 1 and 2 by the
corresponding factual outcome losses plus the barycenter-based regularizer (via Lemma 4) and the FGW discrepancy term in
our objective (via Lemma 5). We then obtain the stated bounds by substituting these inequalities into the decompositions used
in the proofs of Theorems 1 and 2.

A.3.3 Main Proofs: Theorems 1 and 2
Using the above lemmas, we prove Theorems 1 and 2.
Theorem 1(Upper bound for CASE).Suppose that Assumptions 1–3 and the auxiliary conditions in Appendix A.3.1 hold (in
particular, the expected squared lossl(x,t)isBϕ-Lipschitz in the representation space), and that the weights in Equation(4)
are uniform, i.e.,wt = 2−K. Then, for anyk∈ {1, . . . , K},
ϵCASE(k)≤2
 1
p(t+k) ϵ(t+k) F + 1 p(0) ϵ(0) F + 22K η BϕLϕ  .
Proof.By definition in Equation (7), we rewrite
ϵCASE(k) =
Z
X
h
ˆµ(x,t+k)−µ(x,t +k)

−

ˆµ(x,0)−µ(x,0)
	i2
p(x)dx.
Therefore, we have
ϵCASE(k)≤2
Z
X
h
ˆµ(x,t+k)−µ(x,t +k)
	2
+

ˆµ(x,0)−µ(x,0)
	2i p(x)dx
= 2
X
t′∈T
Z
X

ˆµ(x,t+k)−µ(x,t +k)
	2
p(x|t ′)p(t ′)dx+ 2 X
t′∈T
Z
X

ˆµ(x,0)−µ(x,0)
	2
p(x|t ′)p(t ′)dx
≤2

ϵ(t+k) F +ϵ (t+k) CF  + 2  ϵ(0) F +ϵ (0) CF  (by the Definition of Equations (A.1) and (A.2))
≤2
 1
p(t+k) ϵ(t+k) F + 1 p(0) ϵ(0) F

+ 2Bϕ

 X
t′̸=t+k
W1(Rt+k ,R t′) +
X
t′̸=0
W1(R0,R t′)

 (by Lemma 3),
where we use(ˆµ(x,t)−µ(x,t))2 ≤l(x,t), which follows from the law of total variance.
ToconnecttheremainingWassersteintermstotheBFG-WBregularization,weupperboundthepairwisesumsbybarycenter-
based discrepancies. LetR∗ b denote the Wasserstein barycenter over{Rt}t∈T. For any fixedt∈ T, by the triangle inequality
ofW 1,
X
t′̸=t
W1(Rt,R t′)≤
X
t′̸=t
n
W1(Rt,R ∗ b ) +W 1(Rt′,R ∗ b ) o
= (2K −1)W 1(Rt,R ∗ b ) + X
t′̸=t
W1(Rt′,R ∗ b )
= (2K −2)W 1(Rt,R ∗ b ) + X
t′∈T
W1(Rt′,R ∗ b ).
(A.4)
Applying (A.4) tot=t +k andt=0and summing them yields
X
t′̸=t+k
W1(Rt+k ,R t′) +
X
t′̸=0
W1(R0,R t′)≤(2 K −2) n W1(Rt+k ,R ∗ b ) +W 1(R0,R ∗ b ) o + 2 X
t′∈T
W1(Rt′,R ∗ b )
≤2 K X
t∈T
W1(Rt,R ∗ b )
≤ 2K
η
X
t∈T
F(R t,R ∗ b )
≤ 22K
η Lϕ.
■
Theorem 2(Upper Bound for CAIE).Under the same assumptions as Theorem 1, consider an interaction setS⊆ {1, . . . , K}
with|S| ≥2. Let(a t)t∈T be a constant vector reflecting the combinatorial structure ofS(at ∈ {−1,0,1}). The estimation
errorϵ CAIE(S)is bounded by:
ϵCAIE(S)≤
 X
t∈T
a2 t
! (X
t∈T
1
p(t) ϵ(t) F + 2K+1 η Bϕ (2K −1)L ϕ
)
.

Proof.
ϵCAIE(S) =
Z
X
(X
t
at

ˆµ(x,t)−µ(x,t)

)2
p(x)dx(by Definition in Equation (8))
≤
 X
t
a2 t
! X
t
Z
X

ˆµ(x,t)−µ(x,t)
2
p(x)dx(by Cauchy–Schwarz)
=
 X
t
a2 t
! X
t
X
t′
Z
X

ˆµ(x,t)−µ(x,t)
2
p(x|t ′)p(t ′)dx
=
 X
t
a2 t
! X
t



Z
X

ˆµ(x,t)−µ(x,t)
2
p(x|t)p(t)dx+
X
t′̸=t
Z
X

ˆµ(x,t)−µ(x,t)
2
p(x|t ′)p(t ′)dx



≤
 X
t
a2 t
! X
t



Z
X
l(x,t)p(x|t)p(t)dx+
X
t′̸=t
Z
X
l(x,t)p(x|t ′)p(t ′)dx



=
 X
t
a2 t
! X
t

ϵ(t) F +ϵ (t) CF

(by Definition in Equations (A.1) and (A.2))
≤
 X
t
a2 t
! X
t


ϵ(t) F +
 1
p(t) −1

ϵ(t) F +B ϕ X
t′̸=t
W1(Rt,R t′ )



Note thatP t P t′̸=t W1(Rt,R t′)counts each unordered pair{t,t′}twice. Hence,
X
t
X
t′̸=t
W1(Rt,R t′) = 2
X
{t,t′}∈( T 2 )
W1(Rt,R t′).
By substituting this identity into the previous inequality, we have
ϵCAIE(S) =
 X
t
a2 t
!  

X
t
1
p(t) ϵ(t) F + 2Bϕ X
{t,t′}∈( T 2 )
W1(Rt,R t′)



≤
 X
t
a2 t
! (X
t
1
p(t) ϵ(t) F + 2Bϕ(2K −1) X t W1(Rt,R ∗ b ) ) (by Lemma 4)
≤
 X
t
a2 t
! (X
t
1
p(t) ϵ(t) F + 2 η Bϕ(2K −1) X t F(R t,R ∗ b ) ) (by Lemma 5)
=
 X
t
a2 t
! (X
t
1
p(t) ϵ(t) F + 2K+1 η Bϕ (2K −1)L ϕ
)
.
■
Although the two theorems could be subsumed under a general linear-contrast bound, presenting them separately clarifies
how BFG-WB controls the estimation errors of both single and interaction treatment effects. Together, these bounds provide
a principled decomposition that motivates the training objective in Equation (10) by linking factual prediction errors and the
BFG-WB discrepancy to the estimation errors of both estimands.
It is important to note the connection between these theoretical bounds and our empirical design. Assumptions 4 and 5
are idealized conditions; they follow the standard setting adopted in representation-based causal inference (Shalit, Johansson,
and Sontag 2017; Wang et al. 2025). Assumption 5 concerns the smoothness of the loss over the representation space, and is
more plausible when nearby representations correspond to units with similar outcomes. By penalizing distortions of within-
distribution neighborhoods, the proposed BFG-WB objective is designed to encourage representations of this kind, which we
examine empirically in Appendix D.4

B Data Generating Process
Wedescribethedata-generatingprocess(DGP)forthesimulationdatasetsusedinSection5toevaluatetheabilityofthemodels
to estimate CASE and CAIE accurately and stably under selection bias. We generate two datasets under covariate-dependent
treatmentassignmentandvaryonlywhethertheoutcomefunctioncontainsinteractioneffects.Simulation1includesinteraction
effects among treatments in the outcome generation, which serves as the primary benchmark for CASE and CAIE estimation.
Simulation 2 excludes interaction effects to assess the model’s robustness and its ability to avoid inducing false interaction
effects.
In two scenarios, the simulation data follow the same functional form for covariate generation, treatment assignment, and
outcomegeneration.ThenumberoftreatmentsKisfixedat3,andthesamplesizeNissetto50,000.Weintroducetheindicator
variablesHto reflect realistic conditions where treatment assignment depends on covariates (Ascarza 2018; Djulbegovic et al.
2014).
x(j) i,n ∼N(c (j) n ,1 2), x (j) i,u ∼U(−1,1),x i = (xi,n,x i,u),
H (v) i =I  x(v) i +x (v+1) i >1  , v= 1,2,3,
H i = (H (1) i , H(2) i , H(3) i ),
t(k) i ∼Bern  σ  w⊤ tk xi +w ⊤ H,kH i −1  , k= 1,2,3,
ti = (t(1) i , t(2) i , t(3) i ),
Yi ∼ N

f(x i,t i, l),12 , l∈ {0,1},
wherej∈ {1, . . . ,15}andc(j) n are drawn from the uniform distributionU(−1,1).I(·)is the indicator function,σ(·)is the
sigmoidfunctiondefinedasσ(x) = 1/(1 + exp(−x)).w tk andw H,k aretheweightvectorswhoseelementsareindependently
drawn from the uniform distributionU(−0.5,0.5). The outcome-generating functionfis defined as follows:
f(x i,t i, l) =w⊤ x xi + (x(1) i + 1)t(1) i + 1.2(x(2) i + 1)t(2) i
+ 0.8(x(3) i + 1)t(3) i +l n (x(4) i + 0.5)t(1) i t(2) i
−0.5(x (5) i −0.1)t (1) i t(3) i + 0.3(x(6) i + 0.1)t(2) i t(3) i
+ 0.7(x(7) i + 1)t(1) i t(2) i t(3) i
o
+ 2,
wherevectorw x istheweightvectorwhoseelementsareindependentlydrawnfromtheuniformdistributionU(−1,1),andthe
parameterl∈ {0,1}determines whether interaction effect terms are included (l= 1) or excluded (l= 0). We define the case
wherel= 1as the first scenario and the case wherel= 0as the second scenario.
C Implementation Details
This section provides the implementation details necessary to reproduce the simulation results reported in Section 5. We first
specify the network architectures of the proposed CIHSI-Net, including representation learning, task embedding, and outcome
prediction subnetworks. Subsequently, we outline the optimization protocols, hyperparameter settings, and the implementation
configurations for the baseline methods.
CIHSI-Net Architecture and Training.All neural networks within CIHSI-Net are constructed using fully connected (FC)
layers(LeCun,Bengio,andHinton2015)withLeakyReLUactivationfunctions(Xuetal.2020).Thespecificarchitecturesare
as follows.
•Representation Learning Networkϕ: Consists of two hidden layers with 100 units each. The output dimension is set to
64. Crucially, we apply batch normalization with a fixed scale to the output of the representation learning network because
the BFG-WB regularization is sensitive to feature scaling, similar to the balancing regularization in Shalit, Johansson, and
Sontag (2017).
•TaskEmbeddingNetworkt w:Consistsoftwohiddenlayerswith100unitseach,outputtingafive-dimensionalembedding
vector.
•Outcome Prediction Networkh: Consists of two hidden layers with 100 units each. It takes the concatenated output ofϕ
andt w as input.
Duringtraining,theWassersteinbarycenterisestimatedforeachmini-batchasafree-supportW 2 2 barycenterwith16uniformly
weighted support points, using the treatment-pattern-specific empirical representation distributions. In all experiments, the
weightsλ t inEquation(5)aresetuniformlyacrossthetreatmentpatternsincludedinthebarycentercomputation.TheBFG-WB

Algorithm 1: The computation workflow of CIHSI-Net with BFG-WB
Input:observed dataD={(x i,t i, yi)}N i=1; representation mappingϕ; task embedding mappingtw; outcome mappingh.
Parameters:α: strength of BFG-WB regularization;η: FGW trade-off parameter;β: strength ofL 2 regularization;
{λt}t∈{0,1}K: Wasserstein barycenter weights;{wt}t∈{0,1}K: BFG-WB weights.
Output:L: the learning objective of CIHSI-Net.
1R i ←ϕ(x i)
2R t ← {Ri |t i =t}for eacht∈ {0,1} K
3R ∗ b ←arg min Rb P t∈T λtW 2 2 (Rt,R b)
4L ϕ ← P t∈T wtF(R t,R ∗ b )
5bp(t)← 1 N PN i=1 I[ti =t]for eacht∈ {0,1} K
6CalculateL y following (11) withbp(t)and outcome mappingh
7L ← Ly +αL ϕ +β∥w∥ 2 2
Hyperparameter Candidate values Selected value
BFG-WB coefficientα{0.1,0.5,1.0,1.5,2.0,5.0}1.0
FGW trade-offη{10 −5,0.1,0.2, . . . ,0.9,1.0}0.6
Number of units per FC hidden layer{20,50,100}100
Table A1: Hyperparameter search ranges and selected values.
weights are also set uniformly aswt = 2 −K for all treatment patterns. We compute the barycenter through iterative updates
with a maximum of 100 iterations. The optimization procedure of CIHSI-Net is encapsulated in Algorithm 1.
All models are trained with Adam optimizer (Kingma and Ba 2017) for a maximum of 300 epochs, with an early stopping
patiencesetto15epochs.Unlessotherwisespecified,weusedalearningrateof10 −4,abatchsizeof256,andanL2regularization
of10 −5. Data splitting is performed by random shuffling, allocating 60% for training, 10% for validation, and 30% for testing.
Table A1 summarizes the candidate values considered for each hyperparameter. For CIHSI-Net, the final configuration are
selected as the one that achieved the lowest validation loss on Simulation 1.
Baseline Methods Selection and Implementation.To enable a comprehensive comparison, we implemented the following
three baseline methods. These methods cover complementary modeling paradigms: TECE-VAE adopts a latent-variable gener-
ativeapproach,NCoREexplicitlymodelsrelationsamongtreatmentcombinations,andCISI-NetemployspairwiseWasserstein
balancing across treatment patterns. In particular, CISI-Net is the closest baseline to CIHSI-Net and enables us to directly
evaluate the contribution of replacing pairwise balancing with the proposed barycenter-based BFG-WB objective. For each
model, we set the hyperparameters as follows.
•TECE-VAE:The latent dimension is set to 25, and the task embedding network has three hidden layers with 200 units
and ELU activation (Clevert, Unterthiner, and Hochreiter 2016). The task embedding network produces a five-dimensional
embedding vector.
•NCoRE:EachinteractionsubnetworkisimplementedastwoFClayerswith200unitsperlayerandReLUactivation(Nairand
Hinton 2010). The representation learning network has two hidden FC layers with 200 units and outputs a 100-dimensional
vector.
•CISI-Net:CISI-Net has three neural networks, all of which are built using FC layers and leaky ReLU activation. Each
networkconsistsoftwohiddenlayerswith100unitseach.Thetaskembeddingnetworkoutputsafive-dimensionalembedding
vector.Thebalancingpenaltycoefficientαissetto0.1,andtheIntegralProbabilityMetrics(IPM)usedinthepenaltyisthe
1-Wasserstein distance (Sriperumbudur et al. 2010).
All baseline models are tuned and trained under conditions comparable to CIHSI-Net to ensure a fair evaluation.
We excluded other methods to ensure a focused and fair comparison for the following reasons:
•Some methods have been empirically shown to underperform the baselines adopted in this study. In particular, methods
originally developed for single-treatment settings, such as Treatment-Agnostic Representation Network (TARNet) (Shalit,
Johansson,andSontag2017)andCounterfactualRegression(CFR)(Shalit,Johansson,andSontag2017),havebeenshownin
previousexperimentstobeoutperformedbymethodsspecificallydesignedformultiplesimultaneoustreatments(Murakami,
Hattori, and Kubota 2025; Saini et al. 2019).
•Somemethodsrelyonadditionalassumptionsthatarenotadoptedinourproblemsetting,suchasthesequentialignorability
assumption used in Single-cause Perturbation (Qian, Curth, and van der Schaar 2021).

MethodK= 2K= 3K= 4K= 5K= 6K= 8
CISI-Net 5.98 15.08 31.09 138.54 125.62 1529.83
CIHSI-Net 8.21 9.02 13.92 22.71 23.01 48.32
TableA2:Wall-clocktrainingtimeperepoch(s/epoch)forCISI-Net(pairwisebalancing)andCIHSI-Net(BFG-WB),evaluated
withK∈ {2,3,4,5,6,8}treatmentsunderthesamehardwareandtrainingconfiguration.ForeachK,bothmethodsaretrained
with the same batch size, while the batch size is adjusted across different values ofK. Times are averaged across all observed
epochs in 100 trials with early stopping (max 300 epochs, patience = 15).
•Somemethodstargetdifferentestimandsordatastructures,suchasH-learner,whichconsidersmultipleoutcomes(Chauhan
et al. 2025).
•Some methods share modeling paradigms and limitations similar to those already represented by the selected baselines, and
therefore provide limited additional insight; Variational Sample Re-weighting (Zou et al. 2020), for example, represents a
latent-variable approach similar to TECE-VAE.
•Some methods employ architectures closely related to those of the selected baselines but are not applicable to binary
treatments. For example, the Dosage Combination Network (Schweisthal et al. 2023) is architecturally similar to CISI-Net
butisspecificallydesignedforcombinationsofcontinuoustreatmentdosagesandthereforecannotbedirectlyappliedtothe
binary treatment setting considered here.
Furthermore,conventionalinverseprobabilityweightingbasedanddoublyrobustestimators,arenotincludedbecauseprevious
empirical comparisons have shown them to be outperformed by TARNet or CFR (Shalit, Johansson, and Sontag 2017).
Hardware and Software EnvironmentsAll experiments are conducted in a single-GPU computing environment running
Ubuntu22.04.5LTSonanx86_64architecture.TheenvironmentareequippedwithoneNVIDIAL4GPUwith23GBofGPU
memory,12virtualCPUscorrespondingtoanIntelXeonprocessoroperatingat2.20GHz,and52GBofsystemmemory.CUDA
compatibility version is 13.0. All methods are implemented in Python 3.12, and the neural network models are implemented
primarily using TensorFlow 2.20.0.
D Additional Simulation Results
D.1 Comparison of Computing Speed
OneadvantageofimplementingBFG-WBwithinCIHSI-Netisitslowercomputationalcostrelativetoexistingpairwisebalancing
methods. OT-based discrepancy evaluation, as used in representation balancing, requires solving optimization problems. This
requirement often introduces a significant bottleneck during model training (Genevay, Peyre, and Cuturi 2018; Yamada et al.
2022). If the number of treatments is denoted asK, the total number of possible treatment patterns isL= 2K. The number of
OTcomputationsrequiredfordiscrepancyevaluationinpairwisebalancingincreasesquadraticallywiththenumberoftreatment
patterns, specifically following the combination formula
2K
2

=O(L 2). In contrast, BFG-WB reduces the required number of
OTcomputationstoO(L)anddemonstratesalinearincreaseincomputationcountrelativetothenumberoftreatmentpatterns.
Todeterminewhetherthistheoreticalreductionincomputationtranslatesintoameasurabledecreaseinactualtrainingtime,we
compare the required training time.
WecomparecomputationalcostsusingtheCISI-NetandCIHSI-Netwithsimulationdataset1(detailedinAppendixB).The
number of treatments K is set toK∈ {2,3,4,5,6,8}to verify the scaling of training time as the number of treatment patterns
increasesto2 K.Foreachsetting,weconduct100independenttrialsusingdifferentrandomseedsfordatageneration.Eachtrial
follows the hyperparameters and training protocol described in Appendix C. To ensure that each mini-batch contains at least
four samples from each treatment pattern, we adjust the batch size according toK: 256 forK∈ {2,3,4,5}, 1024 forK= 6,
and 2048 forK= 8. We compute the training time per epoch (s/epoch) from the wall-clock measurements and compare the
actual training time required for each method by averaging over all epochs across 100 trials. Table A2 summarizes the results.
TableA2demonstratesthatthecomputationaladvantageofCIHSI-Netbecomesclearasthenumberoftreatmentsincreases.
For small treatment settings such asK= 2, this advantage is limited, and CIHSI-Net is slightly slower than CISI-Net due to
the overhead of computing the barycenter-based discrepancy. However, fromK= 3onward, CIHSI-Net consistently achieves
shorter training times than CISI-Net. The gap generally becomes more pronounced asKincreases. For example, whenK= 5,
CISI-Netrequires138.54[s/epoch],whereasCIHSI-Netrequiresonly22.71[s/epoch].Althoughthewall-clocktimeofCISI-Net
decreases slightly fromK= 5toK= 6because the batch size increases from 256 to 1024, thereby reducing the number of
mini-batch updatesper epoch,CIHSI-Net remainssubstantially fasterin bothsettings. AtK= 8, thiscomputational advantage
becomes particularly pronounced: CISI-Net requires 1529.83 [s/epoch], whereas CIHSI-Net requires only 48.32 [s/epoch].
These results suggest that CIHSI-Net offers practical advantages in training time, particularly in settings with an increased
number of treatments.

D.2 Scalability to a Larger Number of Treatments
We investigate the scalability of the proposed method by evaluating whether its estimation accuracy remains superior to that of
existing multiple-treatment methods as the treatment dimension increases. Multiple-treatment settings are practically relevant
because many real-world studies involve the simultaneous evaluation of multiple treatments, which requires the estimation of
numerous causal effects (Parmar et al. 2008; Freidlin et al. 2008). Therefore, we compare the estimation accuracy of each
method under different values ofK.
In this scalability analysis, we set the number of treatments toK∈ {2,4,6,8}. This range is chosen to reflect realistic
multiple-treatmentsettings, sinceempirical applicationsrarely involvemore thanten simultaneoustreatments (Choet al.2022;
Freidlin et al. 2008; Muralidharan, Romero, and Wüthrich 2025; Tsuboi et al. 2024). Therefore, setting the maximum number
of treatments toK= 8provides a practically meaningful evaluation range while still requiring the methods to handle a rapidly
increasing number of treatment patterns. Across all settings, we use a common functional form for treatment assignment and
outcomegeneration,andfixthesamplesizeatN= 50,000.Thecovariates,treatmentassignments,andoutcomesaregenerated
according to the following data-generating process:
x(j) i,n ∼N(c (j) n ,1 2), x (j) i,u ∼U(−1,1),x i = (xi,n,x i,u),
H (v) i =I  x(v) i +x (v+1) i >1  ,H i = (H (1) i , H(2) i , H(3) i ),
t(k) i ∼Bern  σ  w⊤ tk xi −w ⊤ H H i  ,t i = (t(1) i , . . . , t(K) i ),
Yi ∼ N

g(xi,t i),0.1 2 ,
wherej∈ {1, . . . ,15}denotes the covariate index,v∈ {1,2,3}, andk∈ {1, . . . , K}.I(·)is the indicator function,σ(·)is the
sigmoid function defined asσ(x) = 1/(1 + exp(−x)). The elements ofwtk are independently drawn fromU(−0.5,0.5), and
the elements ofwH are independently drawn fromU(−1,1). The outcome generating functiongis defined as follows:
g(xi,t i) =w ⊤ x xi + X
∅̸=S⊆{1,...,K}
|S|≤K
τS(xi)
Y
k∈S
t(k) i + 2, τS(xi) =w S

1 +x (jS ) i

,
wherej S ∈ {1, . . . ,30}denotesacovariateindexrandomlyassignedtoeachsubsetS.Thevectorw x isaweightvectorwhose
elementsareindependentlydrawnfromtheuniformdistributionU(−1,1),andeachw S isindependentlydrawnfromU(0.2,1.0)
with a randomly assigned sign. This setup induces treatment assignment bias throughHi and heterogeneous treatment effects
throughτ S(xi).
All model hyperparameters are kept identical to those described in Appendix C. The only exception is the batch size, which
is adjusted depending onK. Specifically, to ensure that each batch contains at least four samples from each treatment pattern,
we set the batch size to 256 forK∈ {2,4}, 1024 forK= 6, and 2048 forK= 8. This adjustment is necessary to obtain
stable empirical estimates of the balancing regularization terms, because the number of treatment patterns increases as2K. We
exclude TECE-VAE from this scalability analysis because it does not show competitive performance in the main simulation
results reported in Section 5.
FigureA1showstheaverageϵ CASEandϵ CAIEover50trialsacrossvaryingnumbersoftreatmentsK∈ {2,4,6,8}.CIHSI-Net
consistently achieves the lowest estimation errors for both CASE and CAIE across all values ofK, which demonstrates that the
proposed method maintains high estimation accuracy even asKincreases. Crucially, the performance gap between CIHSI-Net
and CISI-Net becomes larger asKincreases, and CIHSI-Net achieves this higher accuracy with substantially shorter training
time than CISI-Net, as shown in Table A2. This tendency suggests that pairwise balancing becomes unstable as the number of
treatment patterns grows, whereas the barycenter-based alignment in CIHSI-Net provides a more consistent global reference
across treatment patterns. These results demonstrate that CIHSI-Net improves both estimation accuracy and computational
efficiency in settings with many treatment patterns, supporting its scalability for multiple-treatment causal inference.
D.3 Detailed Results of Ablation Study
Inthissection,weprovidethedetailedvaluesforϵ CASE andϵ CAIE.AlthoughtheaverageresultsinSection5clarifytheoverall
tendency,thedetailedresultsfurtherconfirmwhethertheobservedimprovementisconsistentacrossindividualCASEandCAIE
estimation errors. Table A3 shows the detailed ablation results on simulation dataset 1.
The detailed results also show that the combination of the Wasserstein barycenter and the FGW discrepancy achieves the
lowestestimationerrorsacrossallreportedCASEandCAIEerrors.TheseresultsareconsistentwiththediscussioninSection5
and provide additional support for the design of BFG-WB.
D.4 Analysis of Representation Discrepancy
We investigate the effectiveness of the proposed method in reducing distributional discrepancies across treatment patterns
compared to existing approaches. Minimizing these discrepancies serves two critical objectives essential for accurate causal

   
K




$YHUDJHHUURU
$ YHUDJH CASE
   
K






$YHUDJHHUURU
$ YHUDJH CAIE
1&R5( &,6,1HW &,+6,1HW
Figure A1: AverageϵCASE (left) andϵCAIE (right) under varying numbers of treatmentsK∈ {2,4,6,8}.
ϵCASE ϵCAIE
No. WB Penalty typek= 1k= 2k= 3 S={1,2}S={2,3}S={1,3}S={1,2,3}
1✗None 0.28±0.08 0.29±0.04 0.25±0.09 0.36±0.03 0.12±0.04 0.16±0.03 0.31±0.04
2✗W 0.22±0.04 0.24±0.03 0.19±0.06 0.31±0.07 0.11±0.04 0.15±0.08 0.31±0.08
3✗GW 0.25±0.03 0.28±0.04 0.23±0.10 0.35±0.03 0.12±0.06 0.16±0.04 0.32±0.05
4✗FGW 0.23±0.04 0.25±0.03 0.19±0.05 0.33±0.04 0.12±0.06 0.16±0.04 0.31±0.04
5✓W 0.22±0.03 0.24±0.03 0.19±0.08 0.30±0.04 0.10±0.05 0.15±0.09 0.28±0.07
6✓GW 0.22±0.04 0.24±0.03 0.19±0.08 0.32±0.06 0.10±0.04 0.16±0.05 0.29±0.06
7✓FGW0.19±0.04 0.21±0.04 0.18±0.10 0.28±0.05 0.08±0.05 0.12±0.04 0.24±0.04
Table A3: Ablation study result on simulation dataset 1. WB indicates whether the Wasserstein barycenter is used. Penalties:
Wasserstein (W), Gromov-Wasserstein (GW), Fused GW (FGW), and None.
inference:(i)reducingselectionbiasarisingfromtreatmentassignmentimbalances,whichcorrespondstominimizingdistribu-
tional discrepancy (assessed via Wasserstein distance), and (ii) preserving local proximity structures to stabilize the estimation
of heterogeneous causal effects, which corresponds to maintaining geometric consistency (assessed via Gromov-Wasserstein
distance).
To empirically verify these properties, we compute these two metrics (the Wasserstein distance and the Gromov-Wasserstein
distance) for every unique pair of treatment patterns on the dataset of Simulation 1 described in Section 5. We compare three
methods: CISI-Net (without balancing), CISI-Net (with pairwise balancing), and our proposed CIHSI-Net (with BFG-WB).
Figure A2 displays the boxplots of pairwise Wasserstein and Gromov-Wasserstein distances calculated across all treatment
pairs. As shown in the left panel (Wasserstein distance), CIHSI-Net consistently achieves the lowest median and variance of
discrepancies across representation distributions compared to the baselines. Whereas standard CISI-Net reduces discrepancies
relative to the non-balanced model, it fails to match the compactness achieved by CIHSI-Net. This result suggests that simply
extending pairwise balancing is insufficient for achieving comprehensive alignment in multiple-treatment settings. The right
panel (Gromov-Wasserstein distance) further illustrates the advantage of our CIHSI-Net. CIHSI-Net exhibits lower structural
discrepanciesthanCISI-Net.Thisresultindicatesthatindependentpairwisealignmentcandistortthelocalproximitystructures
within the representation space. In contrast, by aligning all distributions toward a shared Wasserstein barycenter, CIHSI-Net
effectivelymitigatesbothdistributionaldivergenceandlocalstructuralinconsistency.Theseresultsempiricallydemonstratethe
superiority of CIHSI-Net in handling multiple treatments.
D.5 Sensitivity Analysis forαandη
To examine the sensitivity of CIHSI-Net to the key hyperparameters in BFG-WB, we conduct a sensitivity analysis over
the regularization strengthαand the FGW trade-off parameterη. This analysis clarifies how the balance between global
alignmentandlocalstructurepreservationaffectsestimationaccuracy,andassesseswhetherCIHSI-Netremainsstableacrossa
reasonable range of hyperparameter choices. Varyingα∈ {0.1,0.5,1.0,1.5,2.0,5.0}, we cover weak to strong regularization
via BFG-WB, which examines the trade-off between representation balancing and outcome prediction accuracy. Additionally,
to compare the relative contributions of local structure preservation and feature-wise distribution alignment, we varyη∈

Figure A2: Distribution of pairwise Wasserstein (left) and Gromov-Wasserstein distances (right) between representation dis-
tributions for all unique treatment pairs. We compare CISI-Net (without balancing), CISI-Net (with pairwise balancing), and
CIHSI-Net (ours). Lower values indicate better alignment across treatment patterns.
{10−5,0.1,0.2, . . . ,0.9,1.0}. Here, largerηplaces more weight on feature-wise Wasserstein alignment, whereas smaller
ηemphasizes the Gromov-Wasserstein-based structural term. We includeη= 10 −5 as a near-boundary configuration that
approximates GW-only alignment while remaining within the theoretical domainη∈(0,1].
Figure A3 summarizes the sensitivity results overαandη, averaged over 100 trials. The results indicate that estimation
performance depends on bothαandη, which emphasizes the importance of appropriately selecting their combination. For
0.5< η <0.8,ϵCASE andϵ CAIE remainsmall,suggestingthatamoderateemphasisonfeature-basedalignmentwhileretaining
structural preservation is beneficial for causal effect estimation. At the near-boundary settingη= 10−5, the estimation errors
remain competitive for some estimands but are not consistently minimized across metrics and values ofα. This pattern is
consistent with the theoretical role ofη: because the error bounds contain a factor of1/η, they become increasingly loose as
ηapproaches zero and cease to provide finite control at the GW-only boundaryη= 0. With respect toα, accurate estimation
of both CASE and CAIE is achieved when1.0≤α≤1.5. Weak balancing regularization, such asα= 0.1, tends to result in
insufficientcorrectionofselectionbiasandlargerestimationerrorsacrossallmetrics.Conversely,atα= 5.0,CASEestimation
errors increase, while CAIE estimation errors are reduced. This may be interpreted as stronger selection bias affecting units
receiving multiple treatments simultaneously, where strong balancing effectively estimated interaction treatment effects.
D.6 Evaluation on Semi-Synthetic Dataset
We conduct an additional semi-synthetic experiment to evaluate the proposed method under a more realistic setting while
retainingaccesstoground-truthcausaleffects.Whereasthefullysyntheticsimulationsallowustoevaluatetheproposedmethod
undercontrolleddata-generatingprocesses,theymaynotfullyreflectthecovariatedistributionandtreatmentimbalanceobserved
inreal-worlddata.ThepurposeofthisexperimentistoverifywhetherCIHSI-NetcanaccuratelyestimatebothCASEandCAIE
when the covariates and treatment assignments follow an empirical distribution, while the outcome-generation mechanism is
known.
We construct a semi-synthetic dataset using the real covariates and observed treatment assignments from Dataset A used in
Section 6. Specifically, we pair Dataset A’s real covariates and treatment assignments with a known synthetic outcome function
that includes nonlinear heterogeneous effects for both CASE and CAIE. Letxi ∈R 71 denote the observed covariates for unit
i. The observed treatment vectorti = (t(1) i , t(2) i , t(3) i )∈ {0,1}3 is kept fixed from the original data. The observed outcome is
then generated from the following semi-synthetic data-generating process:
yi =g(x i,t i) +ε i, ε i ∼ N(0,0.52).
The outcome generating functiongis defined as:
g(xi,t) = tanh(x ⊤ i W g +b g) + X
∅̸=S⊆{1,2,3}
gS(xi)
Y
k∈S
tk,
where, for each non-empty subsetS⊆ {1,2,3},g S(xi) =w S tanh(x⊤ i W S +b S)represents the heterogeneous treatment
effect function. The elements ofWg andW S are independently drawn fromN(0,12), and the bias termsbg andb S are drawn
fromN(0,0.5 2). The coefficientwS is independently drawn fromU(−1,1)for each non-empty subsetS. This construction

Figure A3: Sensitivity analysis of hyperparametersαandηon simulation dataset 1. The top row showsϵCASE(1)-ϵ CASE(3),
the middle row showsϵCAIE({1,2})-ϵ CAIE({1,3}), and the bottom panel showsϵCAIE({1,2,3}).
preserves the covariate distribution and treatment imbalance of the original data while providing known ground-truth CASE
and CAIE values.
We use the same model architectures, hyperparameters, and training protocol as those described in Appendix C. The data
wasrandomlysplitinto60%training,10%validation,and30%testsets,withallreportedevaluationsperformedonthetestset.
To ensure statistical reliability, we report average metrics over 100 independent runs.
Table A4 shows the results of the semi-synthetic experiment. Overall, CIHSI-Net achieves the strongest performance among
the baseline methods under the empirical covariate distribution and observed treatment assignments of Dataset A. Although
CISI-NetandNCoREobtainthelowesterrorforsomeindividualϵ CASE,CIHSI-NetremainscompetitiveforCASEandachieves
the best results for allϵCAIE. When the errors are averaged over theϵCASE andϵ CAIE, CIHSI-Net obtains the lowest overall
errors, suggesting that the proposed barycenter-based balancing is effective for estimating both single and interaction effects in
the semi-synthetic setting. This result suggests that CIHSI-Net remains robust even when the treatment assignment imbalance
is inherited from real-world data.
E Real-world Datasets and Additional Results
In this section, we provide supplementary details and additional results for the real-world marketing application. We first
describe the dataset specifications, preprocessing steps, and experimental protocols common to both Dataset A and Dataset B.
Subsequently, we present the analysis results for Dataset B, which involves promotions from competing merchants.

ϵCASE ϵCAIE
Methodk= 1k= 2k= 3 S={1,2}S={2,3}S={1,3}S={1,2,3}
TECE-VAE 1.23±0.09 1.25±0.06 1.28±0.07 3.22±0.46 1.82±0.08 1.62±0.17 4.00±0.34
NCoRE 0.98±0.160.98±0.07 0.78±0.05 2.94±0.48 1.29±0.28 1.37±0.14 5.73±1.20
CISI-Net0.79±0.011.13±0.04 0.96±0.12 1.49±0.14 1.21±0.21 0.96±0.021.49±0.11
CIHSI-Net 0.81±0.02 1.02±0.07 0.78±0.07 1.45±0.07 1.09±0.08 0.96±0.04 1.45±0.06
TableA4:Semi-syntheticexperimentresultsusingDatasetA’srealcovariatesandobservedtreatmentassignments.Boldvalues
indicate the best performance, and underlined values indicate the second-best performance for each metric.
E.1 Details of Real-World Application
Dataset Description and Treatment Assignment.The dataset is derived from a mobile payment platform and involves
multipleconcurrentmarketingpromotions.Weutilizethisproprietarydatasetbecauseexistingpubliclyavailablecausalinference
benchmarks focus primarily on single-treatment scenarios and lack the complex, simultaneous multiple-treatment interactions
observed in real-world marketing environments.
•Dataset A (reported in Section 6): This dataset includes three marketing promotions that were simultaneously conducted:
twoofflinepromotionsorganizedbythesamemerchantgroup(denotedasCP 1andCP 2)andoneonlinepromotionconducted
by another merchant group (denoted as CP3). Each promotion is represented by a binary treatment indicator, which results
in2 3 = 8distinct treatment patterns. The observed sample proportions were approximately 2% for CP1 only, 15% for CP2
only, 42% for CP3 only, 0.2–1% for two-promotion combinations, 0.2% for all three promotions simultaneously, and the
remainder as the control group.
•DatasetB(reportedinthisappendix):Thisdatasetincludestwomarketingpromotionsconductedbytwodifferentmerchants
in the same industry (denoted as CP4 and CP5), yielding22 = 4treatment patterns. The observed sample proportions were
approximately 29% for CP4 only, 4% for CP5 only, 1% for both promotions, and the remainder as the control group.
For both datasets, the control group consists of users who were not exposed to any of the promotion during the treatment
period and who satisfied the positivity assumption, randomly drawn from users with at least one mobile payment transaction
in the month preceding the promotions. Additionally, the preprocessing and experimental protocol described below are applied
identically to both datasets.
Outcome Definition and Preprocessing.The outcome variableYis defined as the total payment amount during the one-
month period following the promotion implementation. To ensure numerical stability and protect data confidentiality,Ywas
standardized to have zero mean and unit variance. This preprocessing preserves the sign of the estimated causal effect and
ensures interpretational consistency between the standardized scale and the original scale because the standardization is an
affine transformation (Thakral and Tô 2023; Murakami, Hattori, and Kubota 2025). The covariates consist of 71 variables,
including service usage histories and user demographic attributes.
User Stratification for Heterogeneity Analysis.To analyze heterogeneous treatment effects, we stratified users based on
their total payment amount in the month before the promotions. Users were grouped into intervals of 5,000 JPY (e.g., 0–5,000,
5,000–10,000). Users with usage exceeding 50,000 JPY were aggregated into a single high-usage group, resulting in a total
of 11 distinct strata. This grouping strategy allows us to examine how the sensitivity to marketing incentives varies with prior
engagement levels.
Experimental Configuration.For the real-world application, we employed the same hyperparameter configuration that
achieved the best performance in the simulation experiments (Section 5). This approach was chosen to evaluate the method’s
robust performance under a reproducible setting without dataset-specific tuning. The dataset was randomly split into 60%
training, 10% validation, and 30% test sets, with all reported evaluations performed on the test set.
E.2 Sensitivity and Uncertainty Analysis on Dataset A
Thisappendixreportsadditionalsensitivityanduncertaintyanalysesfortheestimatedcausaleffectsinthereal-worldapplication
on Dataset A. In real-world observational data, the ground-truth causal effects are unavailable, and the reliability of the results
cannot be assessed through direct estimation errors as in the simulation studies. Therefore, it is important to examine whether
theestimatedcausal-effectpatternsremainstableunderdifferentmodelconfigurationsandsamplingvariability.Weevaluatethe
sensitivity of the estimated CASE and CAIE to key BFG-WB hyperparameters and compute bootstrap confidence intervals for
the estimated causal effects. These analyses provide complementary evidence on the robustness of the real-world application.
For the sensitivity analysis, we focus on two key hyperparameters related to BFG-WB: the regularization strengthαin
Equation (10) and the FGW trade-off parameterηin Equation (6). We evaluate nine hyperparameter configurations by varying
α∈ {0.5,1.0,1.5}andη∈ {0.5,0.6,0.7}while keeping the other model configurations fixed. For each configuration, the
data are randomly split into 60% training, 10% validation, and 30% test sets, and all reported evaluations are performed on
the test set. To quantify uncertainty, we compute bootstrap confidence intervals by repeating the entire estimation pipeline





(VWLPDWHGFDXVDOHIIHFW
= 0.5
          
*URXSLQGH[




(VWLPDWHGFDXVDOHIIHFW




          
*URXSLQGH[








          
*URXSLQGH[








(VWLPDWHGFDXVDOHIIHFW
= 1.0
          
*URXSLQGH[




(VWLPDWHGFDXVDOHIIHFW




          
*URXSLQGH[








          
*URXSLQGH[








(VWLPDWHGFDXVDOHIIHFW
= 1.5
          
*URXSLQGH[




(VWLPDWHGFDXVDOHIIHFW




          
*URXSLQGH[








          
*URXSLQGH[




= 0.5
 = 0.6
 = 0.7
&$6(WRSSDQHOV

CASE(1)
 CASE(2)
 CASE(3)
&$,(ERWWRPSDQHOV

CAIE({1, 2})
 CAIE({1, 3})
 CAIE({2, 3})
 CAIE({1, 2, 3})
Figure A4: Sensitivity and uncertainty analysis of the estimated causal effects in the real-world application on Dataset A. The
rows correspond to the BFG-WB regularization strengthα∈ {0.5,1.0,1.5}, and the columns correspond to the FGW trade-off
parameterη∈ {0.5,0.6,0.7}. In each panel, the top subpanel reports the estimated CASE and the bottom subpanel reports the
estimated CAIE across user groups. The shaded regions represent bootstrap confidence intervals.

Figure A5: In dataset B, estimated CASEs for CP4 and CP5 (left) and the estimated CAIE for{CP4,CP5}(right) across user
groups stratified by pre-promotion service usage. The outcomes are standardized.
for each hyperparameter configuration (Efron and Tibshirani 1994; Kubota and Hoshino 2025). We repeat this procedure
1,000 times for each hyperparameter configuration. We then aggregate the test-set estimates for each bootstrap replication and
constructconfidenceintervalsfromtheempiricaldistributionoftheresultingaggregatestatistics.FigureA4showstheestimated
CASE and CAIE with bootstrap confidence intervals under the nine hyperparameter configurations ofα∈ {0.5,1.0,1.5}and
η∈ {0.5,0.6,0.7}.
Althoughsomeindividualconfidenceintervalsincludezero,theoveralltreatment-effectpatternsremainstableacrossdifferent
hyperparametersettings.Inparticular,theestimatedeffectspreservethesamequalitativetrendsobservedinthemainreal-world
analysis,suchasthesignreversalofthethree-wayinteractioneffectfromnegativeforlow-usageuserstopositiveforhigh-usage
users. This suggests that the empirical findings are not driven by a specific choice of the BFG-WB regularization strength
or the FGW trade-off parameter. Moreover, the consistency of the estimated CASE and CAIE patterns across the bootstrap
replications suggests that CIHSI-Net captures the primary interaction structures in the real-world application. These results
provide additional evidence that the real-world findings are robust to both hyperparameter variation and sampling variability.
E.3 Additional Results on Dataset B
FigureA5showstheestimatedcausaleffectsofdatasetBonastandardizedoutcomescale.TheleftpanelinFigureA5showsthat
bothestimatedsingle-treatmenteffectsarepositiveacrossallusergroups.TheestimatedeffectofCP 5 isconsistentlylargerthan
thatofCP 4,andforbothpromotions,theeffectsizesgraduallydecreaseasthepre-promotionusagelevelincreases.Thispattern
suggeststhatCP 4andCP 5areeffectiveatinducingbehavioralchangesamonglow-usageusers,whereastheirincrementaleffects
are limited for high-usage users whose service usage is already established. This heterogeneity is consistent with established
findings in marketing research (e.g. Breugelmans and Liu-Thompkins 2017; Kubota, Ochiai, and Hoshino 2025; Liu 2007),
which suggests that light users typically possess a greater capacity to increase their transaction volume, whereas heavy users
are often constrained by saturation in their activity levels. Collectively, the contrast with Dataset A (see Section 6) highlights
that treatment effect heterogeneity is highly context-dependent, varying significantly based on promotion characteristics and
competitive dynamics.
The right panel in Figure A5 shows that the estimated interaction effectτCAIE({4,5})is consistently negative across all
groups, which suggests that promotions offered by competing merchants in the same industry may induce a reallocation of
spending across merchants (cannibalization). The results of this cannibalization are consistent with previous research (Dorotic
etal.2021).IncontrasttotheCASEresults,theabsolutemagnitudeofthenegativeinteractionbecomessmallerforhigher-usage
groups, indicating that the degree of cannibalization is mitigated as usage increases. This trend suggests that cannibalization
maybeweakeramonghigh-usageusersbecausetheirbehaviorofusingmultiplemerchantsisalreadyestablished.Overall,these
additional results suggest that CIHSI-Net serves as a practical analysis tool by flexibly uncovering heterogeneous single and
interaction effects across user groups.
