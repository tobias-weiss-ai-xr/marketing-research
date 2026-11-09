---
title: On the QUEST for Uncertainty Quantification via Highest Density Regions
url: https://arxiv.org/abs/2606.19569
category: ai-marketing
subcategory: measurement
date: 2026-06
venue: ''
authors:
- Sam Goring
- Tom Kuipers
- Nicola Paoletti
- David S. Watson
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.19569
pages: 27
chars: 91370
fetched_at: '2026-11-08T13:28:48+00:00'
kb_version: 1
---

# On the QUEST for Uncertainty Quantification via Highest Density Regions

On the QUEST for Uncertainty Quantification via
Highest Density Regions
Sam Goring
King’s College London
sam.goring@kcl.ac.uk
Tom Kuipers
Northeastern University London
t.kuipers@northeastern.edu
Nicola Paoletti
King’s College London
nicola.paoletti@kcl.ac.uk
David S. Watson
King’s College London
david.watson@kcl.ac.uk
Abstract
Uncertainty quantification (UQ) is essential for reliable decision -making in
safety-critical applications in probabilistic machine learning. For regression prob-
lems, dominant scalar UQ approaches—notably, those based on proper scoring
rules—measure uncertainty via pointwise predictive risk. This can lead to coun-
terintuitive results when the target statistic is not the conditional expectation. We
propose an alternative framework, in which uncertainty is characterised by the
volume of the most probable subset of a distribution’s support. QUEST (Quantify-
ing Uncertainty via highest dEnSiTy regions) is a novel approach to UQ based on
the concentration of Lebesgue measure at a distribution’s peak(s), evaluated at one
or more values of a robustness parameter α. We establish connections between our
measures and classical statistics from information theory and economics. We show
that, unlike popular alternatives based on proper scoring rules, QUEST measures
of epistemic and aleatoric uncertainty satisfy a set of axioms adapted from the UQ
literature, including monotonicity under distributional spread and invariance to
location shifts. Selective prediction benchmarks confirm that QUEST performs
favourably against standard measures such as variance and differential entropy.
1 Introduction
Uncertainty quantification (UQ) is crucial for making reliable decisions in safety-critical settings with
probabilistic machine learning techniques [25, 37]. In scalar-valued UQ, entropy-based measures
have long been the uncertainty measure (UM) of choice for classification tasks [21, 28, 8], although
that consensus has been challenged by recent works [56, 46]. These analyses have been extended to
regression settings [5], where proper scoring rules (PSRs) [15] provide a unified conceptual approach
[30, 4]. These methods operationalise UQ as the pointwise risk of predicting with a particular model
as opposed to the true distribution [12].
Despite their theoretical appeal, PSR-based measures can lead to counterintuitive results, particularly
when the target statistic is not the conditional expectation. Consider the task of estimating the
conditionalmode, better known as the maximum a posteriori (MAP) value. MAP inference arises
naturally in many settings, e.g. reinforcement learning and Bayesian modelling. When distributions
are unimodal and symmetric, means and modes coincide and standard regression methods can be
safely deployed. However, means and modes can diverge arbitrarily in the presence of outliers,
multimodality, or heavily skewed data. In these settings, conditional expectations may lie in a region
of low probability density, meaning standard regressors will make predictions that are unlikely or
Preprint.
arXiv:2606.19569v1  [cs.LG]  17 Jun 2026

Normal Skewed Bimodal
−2.5 0.0 2.5 0 1 2 3 4 5 0 10 20
0.00
0.05
0.10
0.15
0.0
0.2
0.4
0.6
0.0
0.1
0.2
0.3
0.4
x
Density
HDR
μ ± σ
Figure 1: Comparison of confidence sets for the mean (blue, defined as the interval µ±σ ) and the
mode (red, defined as the (1−α) -high density region, or HDR). The two coincide for symmetric,
unimodal distributions such as the standardNormal. InSkeweddata, however, variance grows due
to tail area mass. InBimodaldistributions, the HDR may be disconnected, while confidence intervals
can assign positive weight to low-density regions. For all three settings, we fixα= 2Φ(−1)≈0.317 ,
whereΦis the standard normal CDF, so that the HDR coincides withµ±σin the left panel.
even impossible (see Fig. 1). Under such conditions, the MAP is arguably a more informative and
useful statistical target than the conditional expectation.
How should we characterise the uncertainty of MAP predictions? Using a standard plug-in estimator
like variance could substantially overstate the uncertainty in some cases, as is evident in Fig. 1.
This reflects a more general shortcoming with many common UM methods, which fail to properly
prioritise concentration of measure. We start from the basic premise that a valid UM ought to track
this fundamental property, with uncertainty increasing as a monotonic function of a distribution’s
spread. This volume-centric perspective suggests a novel framework for UQ.
We introduce QUEST, a family of UMs based on the Lebesgue measure of a distribution’s highest
density region. QUEST aligns with intuition in the motivating examples above and offers a flexible,
interpretable alternative to PSR-based approaches. We develop measures of aleatoric, epistemic,
and total uncertainty within this framework. Our primary contributions are: (1)Conceptual:We
propose an interpretation of uncertainty based on density concentration and a user-supplied robustness
parameter α. (2)Methodological:We introduce novel measures of local and global uncertainty
in terms of highest density regions, and establish their relationship to well-studied statistics from
information theory and econometrics. (3)Theoretical:We show that QUEST measures of epistemic
and aleatoric uncertainty are sound w.r.t. a set of UM axioms adapted from previous works [56, 44, 5].
(4)Empirical:Selective prediction benchmarks confirm that QUEST performs favourably against
variance and differential entropy, the dominant UM methods in use today for regression.
2 Related work
Uncertainty quantification in regressionMany authors have developed frameworks for represent-
ing uncertainty in regression via second-order distributions [33, 35] (formally defined in Section 3) or
ensembles [13, 31, 2]. Common summary statistics for measuring the uncertainty encoded by such
distributions include variance and differential entropy.
However, unlike in the classification setting, where many authors have investigated the empirical and
theoretical performance of UMs [21, 28, 56, 44], regression uncertainty has received relatively little
attention. Theoretical analysis, in the form of axiomatic assessment, extends existing frameworks
from the classification literature [56, 44] to the regression setting [5, 4]. Empirical validation typically
involves downstream tasks, such as selective prediction [12]; active learning [12, 2]; out of distribution
[12, 46, 1, 33] and adversarial sample detection [ 46, 1]; low correlation between UMs [ 12]; and
alignment with expected behaviour on toy datasets [31, 35, 51, 33, 2].
Proper scoring rulesExisting approaches to UQ in regression have been shown to fit a unified
framework when viewed as optimality targets for proper scoring rules (PSRs) [12, 4]. Introduced by
Gneiting and Raftery [15], PSRs measure uncertainty as the expected pointwise risk of predicting with
the learned distribution. Within the PSR framework, the choice of loss function informs the relevant
UM. Optimising theBrier score—the PSR corresponding to squared error loss—yields variance
as the optimal expected score. However, the Brier score is proper only for the mean functional.
2

By contrast, thelog scoreis strictly proper for the full distribution, and its optimal expected value
recovers differential entropy (formally defined below). Variance and differential entropy thus emerge
as the natural UMs under squared error and log loss, respectively.
Though loss functions from robust statistics (e.g., Huber loss [ 22] or the maximum correntropy
criterion [11]) may occasionally converge on the MAP, this is not generally guaranteed. On the
contrary, Heinrich [19] has shown that the mode functional is notelicitable—in other words, there is
no loss or scoring function under which the mode is the Bayes predictor. Thus the PSR framework is
uniquely ill-suited to UQ in MAP problems.
Set-based UQThe use of sets to quantify uncertainty has been explored through conformal
prediction (CP) and credal sets. CP provides finite sample probabilistic guarantees on prediction
correctness, via a predictive set [ 53]. CP does not explicitly disentangle aleatoric and epistemic
uncertainties [45], and its ability to measure the former has been questioned [17]. Credal sets utilise
an alternative uncertainty representation based on imprecise probability theory [54]. UMs of credal
classifiers have been developed based on volume- [ 43] and distance-based measures [ 16]; PSRs
[20]; as well as entropy and the generalised Hartley measure [55]. Works at the intersection of these
approaches provide methods for constructing credal sets [6, 27] and explore links between CP and
imprecise high density regions (IHDRs) [7]. Caprio et al. [7] find that a classic transductive CP region
at level α is the IHDR at level α. Though similarly rooted in volume-centric measures, this work is
situated within both the imprecise probability and set-valued uncertainty measurement traditions. In
contrast, though utilising a set-based representation, QUEST does not rely on imprecise probabilities
and provides scalar-valued UMs.
3 Preliminaries
NotationLet X ⊆Rd be a continuous feature space. We denote by pθ(x) the probability density
function (pdf) evaluated at X=x under the distribution parametrised by θ∈Θ⊆R k (though we
occasionally suppress the dependence on θ for notational convenience). We assume the existence
of some θ∗ such that the true density is pθ∗ (x). For example, if X is Gaussian, then θ∗ =  µ∗, σ∗
would represent the true mean and standard deviation. We write P(X∈A) as shorthand forR
x∈A p(x)dx, whereA⊆ X. We denote a Dirac mass atX=xviaδ x.
Highest density regionsLet p be a pdf with support X ⊆Rd. Then the distribution’s (1−α) -
highest density region(HDR) is defined as Cα :={x∈ X:p(x)≥t α(p)}, where tα(p) is the largest
constant such that P(X∈C α)≥1−α [24]. Such a set is maximally informative w.r.t. p, providing
the tightest possible localisation of X for a fixed confidence level [3]. HDRs are volume-minimizing
among measurable sets with fixed mass, and are unique up to null sets when the threshold level set
has zero Lebesgue measure. They come with strong coverage guarantees via the Ghosh-Pratt lemma
[14, 42]. We observe that the HDR must contain the true mode for anyα <1.
Second-order distributionsIn line with related works [ 56, 5] we assume a bi-level uncertainty
representation in which an agent learns a distributionoverdistributions. Specifically, the learner
assigns a degree of belief to each possible θ∈Θ . These beliefs are represented by a second-order
distribution Q∈ Q(Θ)with pdf q, where Q(Θ) is the space of probability distributions over Θ. To
continue with our Gaussian example above, q would represent the uncertainty of our estimators for
µ∗ and σ∗. We assume that (i) θ∗ ∈Θ ; and (ii) our method for estimating θ∗ isconsistent(i.e.,
guaranteed to converge on the true value w.p.1).
Uncertainty typologyAleatoric uncertainty (AU) is the uncertainty inherent to a given data
generating process (DGP), which cannot be reduced through sampling or learning.Epistemic
uncertainty (EU) is the uncertainty that is reducible in principle, ultimately going to zero in the limit
of infinite data under assumptions (i) and (ii).Total uncertainty (T U)represents a combination of
AUandEU, possibly but not necessarily in the form of a simple sum [56].
Information theoryWe briefly review definitions for several fundamental information the-
oretic quantities [ 9, 41]. Thedifferential entropyof a continuous variable X is defined as
h(p) :=−
R
X p(x) logp(x)dx . When comparing distributions, we often use thecross-entropy
3

h(p, q) :=−
R
X p(x) logq(x)dx , which is equivalent to h(p) plus the KL-divergence between p and q. The latter is a famous example of an f-divergence, a family of distributional dissimilarity
measures of the form
Df (p||q) :=
Z
X
f
 p(x)
q(x)

q(x)dx,
where f: (0,∞)→R is a convex function with f(1) = 0 . Setting f(t) =tlogt recovers the
KL-divergence; other choices give the total variation distance (f(t) =|t−1|/2 ), Hellinger distance
(f(t) = (
√
t−1) 2), andχ 2-divergence (f(t) = (t−1) 2), among others.
4 QUEST Measures
Our guiding intuition is that statisticalconfidenceamounts to placing large portions of probability
mass in a relatively small region, while statisticaluncertaintyamounts to dispersing that mass more
widely across the distribution’s support. So stated, the claim may seem uncontroversial—yet we
show that popular risk-based measures do not always respect this basic requirement. We begin by
introducing two related measures that quantify uncertainty via HDRs: a local measure, which we call
α-volume, and a global measure, which we callintegrated volume.
α-volumeFor pdf p with support X ⊆Rd and (1−α) -HDR Cα, the α-volumeis defined as
Vα(p) :=λ(C α), where λ is the d-dimensional Lebesgue measure. Small values indicate high
concentration of density (low uncertainty), while large values indicate low concentration (high
uncertainty). By convention, whenC α =∅(e.g. whenp=δ x), we setV α(p) = 0.
This statistic is closely related to differential entropy, which is often proposed as a natural information
theoretic UM [9, 47, 12]. However, this measure suffers from several drawbacks. First, unlike its
discrete counterpart, differential entropy can be negative. This is a simple consequence of the fact
that, whereas probabilitymassis necessarily bounded on the unit interval, probabilitydensitycan
exceed 1. Since many authors take it as axiomatic that any valid UM must be non-negative [56, 44, 5],
this rules out h directly. Second, differential entropy is sensitive to tail area fluctuations in ways that
may not reflect meaningful uncertainty. A density with light tails and a density with heavy tails can
look identical near the mode yet have very different entropies.
α-volume resolves both shortcomings. The precise relationship between our proposed measure and
differential entropy is given by the following proposition. (All proofs in Section A.)
Proposition 4.1.For any pdfponX ⊆R d and anyα∈(0,1)such thatV α(p)<∞:
logV α(p) =h(p α, uα),
wherep α :=p(· |X∈C α)andu α is the uniform density onC α.
Thus when density is flat within the HDR, α-volume reduces to a trimmed estimator of an exponenti-
ated entropy functional. Exponentiating guarantees nonnegativity, while trimming makes the statistic
robust to tail area behaviour.
Integrated volumeIn settings where the choice of α is unclear, or where the degree of concentration
across a range of confidence levels is of interest, we define the integrated volume measure as
IV(p) :=
R 1
0 Vα(p)dα . This quantity summarises the entire α7→V α(p) function—what we call the coverage curve—and provides a global assessment of concentration. (For a visual example, see
Section E.) Curves that quickly approach zero as α grows suggest more densely concentrated (and
therefore less uncertain) distributions. We remark that integrated volume is finite for any distribution
with bounded support, as well as those with unbounded support and tails that decay at an appropriate
rate (e.g., subexponential). For heavier-tailed distributions with infinite support, we can trim the
lower limit of the integral with someε >0.
The coverage curve and summary statistic IV(p) are closely related to theLorenz curveandGini
coefficient(respectively), two common tools for measuring income inequality [ 48, 10]. The Lorenz
curve L: [0,1]→[0,1] plots the cumulative share of total income held by the bottom z-fraction
of a population, ordered from poorest to richest. By construction, L is non-decreasing, convex,
and satisfies L(0) = 0, L(1) = 1. Perfect equality corresponds to the diagonal L(z) =z ; greater
4

Table 1: QUEST measures of uncertainty. T Umeasures require specification of an admissible
f-divergence and corresponding functiong f ; see main text.
Aleatoric Epistemic Total
LocalV α(pθ∗ )V α(q)V α(pθ∗ )·g f

Df (p∗ α ||ˆpα) 
GlobalIV(p θ∗ )IV(q) R 1 0 Vα(pθ∗ )·g f  Df (p∗ α ||ˆpα)  dα
inequality corresponds to curves that sag below the diagonal. The Gini coefficient is a scalar summary
G:= 1−2
R 1
0 L(z)dz , which measures the area between the Lorenz curve and the diagonal, normalised so thatG= 0for perfect equality andG→1as inequality grows.
To translate these notions to densities, we treat the densityp as an income distribution: the “population”
is the support X= [0,1] d with subsets quantified by their Lebesgue measure, and the “income” at
each location x is the probability density p(x).1 Sorting locations from lowest to highest density and
accumulating mass yields theLorenzp-curve:
Lp(z) :=
Z
{x:p(x)≤qp(z)}
p(x)dx, z∈[0,1],
where qp(z) is the z-quantile of the density values under Lebesgue measure on X . Intuitively, Lp(z)
is the total probability mass in the z-fraction of the support with the lowest density values. TheGini
p-coefficientG p is defined as above, plugging in the Lorenzp-curve forL.
Proposition 4.2.Letpbe a density on[0,1] d. Then we have the following two identities.
(a) For every α∈(0,1) , the Lorenz p-curve satisfies Lp

1−V α(p)

=α . Equivalently, the
curves α7→V α(p) and z7→L p(z) are related by the coordinate flip(α, Vα)7→(1−V α, α).
(b) The Ginip-coefficient satisfiesG p = 1−2·IV(p).
Thus with pdfs on bounded support, the coverage curve is geometrically equivalent to the Lorenz
curve, while integrated volume is a linear function of the corresponding Gini coefficient. Together
with Prop. 4.1, these results provide a conceptual and a quantitative bridge between our volume-
centric approach and classical tools from information theory and economics.
QUEST MeasuresWith these definitions in place, we introduce the QUEST measures of uncer-
tainty (see Table 1). AU is quantified via the α-volume and integrated volume of the ground truth
distribution pθ∗ for local and global assessments, respectively. This captures the intuition that the
irreducible uncertainty of a given DGP is encoded by the concentration of measure on its support.
We define EU similarly, this time operating over the second-order pdf q. This reflects the inherent
subjectivity of EU in our framework. This deviates from standard practice, according to which EU
is conceived as a sort of residual—what remains after we subtract AU from T U. Such approaches
have no way of describing the epistemic similarity between agents who are equally confident in their
predictions, despite incurring different errors. We revisit this point in Section 7 below.
It would make little sense to simply add AU and EU to obtain T Uin our framework, given that p
and q are defined over entirely different spaces. Instead, we propose an interaction between first-
and second-order uncertainty. Given some set of observations D, define the posterior predictive
distribution ˆp(x) :=
R
θ pθ(x|θ)q(θ| D)dθ . Let C ∗ α, ˆCα be the (1−α) -HDRs for pθ∗ and ˆp, respectively, and define the conditional pdfs:
p∗ α :=p θ∗ (· |X∈C ∗ α),ˆp α := ˆp(· |X∈ˆCα).
We say that an f-divergence is T U-admissibleif it is bounded above by some Mf <∞ and
finite for distributions with arbitrary support overlap (equivalently, f(0)<∞ and f ′(∞)<∞ ).
Let gf : [0, Mf )7→[1,∞) be a continuous, strictly increasing function with gf (0) = 1 and
limD→Mf gf (D) =∞ . Then local and global T Umeasures are given by the formulae in Table 1.
1The following Prop. 4.2 holds (with minor amendments) for any density with bounded support. The unit volume
assumption is simply for convenience.
5

As a concrete example, plugging in the TV distance and defining gf (D) = (1−D) −1 gives
Vα(pθ∗ )/  1−d T V(p∗ α,ˆpα)  for localT U. For further examples of admissible function-divergence
pairs, see Section D.
This measure is motivated by the intuition that T Uought to depend on objective facts ( θ∗) and
subjective beliefs (q) in such a way that it converges to AU when the two align (i.e., when p∗ α = ˆpα),
but grows without limit as error increases. This holds for standard additive decompositions via
variance or information-theoretic quantities. However, our volume-centric approach requires a
multiplicative penalty to respect the units ofAU.
Choosing α Our framework introduces a hyperparameter α for local UMs. Since α controls the
strength of the coverage guarantee, it may be tempting to adopt a frequentist perspective and think
of this parameter as a sort of type I error rate for the mode. This is a valid interpretation in MAP
inference settings. A more general alternative, however, is that α is arobustnessparameter—it
controls the degree of tail area fluctuations that a user deems practically irrelevant for UQ. Such
trimmed estimators are widely used in robust statistics [ 22]. Users who are unsure what value to
select may find it informative to inspect the coverage curve directly in search of kinks or plateaus.
5 Axiomatic Assessment
We take an axiomatic approach to assessing the QUEST framework. Our axioms closely track those
of Wimmer et al. [56], who initiated the axiomatic UQ research program with their paper on measures
for classification; Sale et al. [44], who extended and refined the axioms; and Bülte et al. [5], who
updated the axioms for regression.
Partial orderingA key step in formalising these axioms is establishing a partial order on distri-
butions in terms of relative uncertainty. Bülte et al. [5] do this directly via the variance, which is
unsatisfying in at least two respects. First, variance offers an incomplete picture of distributional
uncertainty. Consider the case of the Cauchy distribution, for which the second moment is undefined.
It is plainly evident that some Cauchy densities are more concentrated than others (see Fig. 2A), yet
variance provides no tools for distinguishing between them. Second, and perhaps more troubling, this
variance-based partial ordering effectively guarantees the conclusion the authors aim to secure—that
variance-based UMs satisfy those same axioms.
To avoid this circularity, we ground our partial ordering in a primitive notion of distributional
spread that is independent of any specific uncertainty functional and holds for arbitrary continuous
distributions. We begin with the equivalence relation.
Definition 5.1(Spread-equivalence).Let p, p′ be pdfs on Rd with supports X,X ′. We say that p′ is
spread-equivalenttop, writtenp∼p ′, iff:
∀t:λ

{x:p(x)> t}

=λ

{x:p ′(x)> t}  .
Spread-equivalent distributions are equally concentrated at all density thresholds. To allay concerns
that Defn. 5.1 smuggles in our preferred measure of uncertainty, we point out that spread-equivalence
can be restated in terms of a natural and widely accepted divergence-theoretic condition: that a
distribution’s spread should be quantifiable in terms of its deviation from uniformity. The following
proposition makes this precise.
Proposition 5.1.Let p, p′ be pdfs on Rd with supports X,X ′. For thresholds 0< τℓ < τu <∞ ,
define
Xτ :={x:τ ℓ ≤p(x)≤τ u},X ′ τ :={x:τ ℓ ≤p ′(x)≤τ u},Y τ :=X τ ∪ X′ τ ,
and let uτ denote the uniform density on Yτ . Write pτ and p′ τ for the densities of p and p′ conditional
onX τ andX ′ τ , respectively. Thenp∼p ′ iff, for every pair(τ ℓ, τu)and everyf-divergenceD f :
Df (pτ ∥uτ ) =D f (p′ τ ∥uτ ).
The universal quantification over thresholds and f-divergences makes Prop. 5.1 especially potent.
Next, we define a partial order on distributions based on the following notion of dispersion.
6

0.0
0.2
0.4
0.6
−4 −2 0 2 4
x
Density
Scale
γ = 0.5
γ = 1
γ = 2
(A)
infA p
supB p
infA p'
supB p'
Original density p Levelled density p'
−5.0 −2.5 0.0 2.5 5.0 −5.0 −2.5 0.0 2.5 5.0
0.0
0.2
0.4
0.6
x
Density
A: mass removed
B: mass added
(B)
Figure 2:(A)Three Cauchy densities with increasing scale parameters. Levelling correctly orders the
distributions by their relative uncertainty, whereas variance is undefined for all three.(B)Illustrative
example of levelling on a bimodal distribution, where mass is redistributed from a peak to a valley.
Definition 5.2(Levelling).Let p, p′ be pdfs on Rd with supports X,X ′. We say that p′ is alevelling
ofp, writtenp⪯p ′, if either of the following conditions holds.
L1: There are regionsA⊂ XandB⊆ X ′ \Asuch that:
(a)P(X∈A)−P ′(X∈A) =P ′(X∈B)−P(X∈B)≥0;
(b) for allx̸∈A∪B, p(x) =p ′(x);
(c) for allx∈A, p(x)≥p ′(x); and
(d)inf A p≥sup B pandinf A p′ ≥sup B p′.
L2: There exists some densityp ′′ ∼psuch thatp ′′ ⪯p ′ viaL1.
Ifp⪯p ′ andp ′ ̸⪯p, then we say thatp ′ is astrict levellingofp, and writep≺p ′.
Intuitively, a levelling of p is a sort of Robin Hood transfer that “flattens” a pdf by redistributing
from high- to low-density regions, possibly on an expanded support. Items (a) and (b) of L1 are
conservation-of-mass principles, guaranteeing that any reduction of mass in A is exactly offset by an
increase of mass in B, with no further changes beyond these subsets (see Fig. 2B). L1(c) ensures that
we do not redistribute mass within A in such a way that density increases in a subregion despite the
transfer to B. L1(d) is a level-set condition, which states that we can only redistribute to the point of
equality between subsets—possibly less, but no more. This prevents us from replacing one peak with
another. L2 allows us to compare distributions that we otherwise could not, e.g. pdfs with opposite
skew. We remark that ⪯ is reflexive and transitive, but antisymmetric only up to spread-equivalence.
Thus ⪯ is a preorder on pdfs that induces a partial order on equivalence classes. In addition, levelling
is closed under spread-equivalence: ifp⪯p ′,p∼p 0, andp ′ ∼p ′ 0, thenp 0 ⪯p ′ 0.
With spread and levelling defined, we adapt the following definitions from previous works [56, 44, 5].
Definition 5.3(Spreads and shifts).Let θ∼Q, θ ′ ∼Q ′ be random vectors with Q, Q′ ∈ Q(Θ). We
say thatQ ′ is a:
•mean-preserving spreadofQiffq⪯q ′ andE Q[θ] =E Q′[θ′].
•spread-preserving location shiftofQiffq∼q ′ andE Q[θ]̸=E Q′[θ′].
We now introduce the modified axioms.
A0:T U, AUandEUshould be non-negative.
A1: For allQ∈ Q(Θ), EU(q)≥EU(δ θ) = 0.
A2: Ifq ℓ ⪯q⪯q u, thenEU(q ℓ)≤EU(q)≤EU(q u).
A3: Ifp ℓ ⪯p⪯p u, thenAU(p ℓ)≤AU(p)≤AU(p u).
A4: If Q′ is a mean-preserving spread of Q, then EU(q)≤EU(q ′) (weak) or
EU(q)< EU(q ′)(strict); the same holds forT U.
A5: IfQ ′ is a spread-preserving location shift ofQ, thenEU(q) =EU(q ′).
AxiomA0is a basic requirement intended to preserve the interpretability of UMs.
A1 formalizes the intuition that epistemic uncertainty is minimized by a Dirac mass on some θ∈Θ .
As noted above, the second-order distribution for a consistent learning procedure approaches δθ∗ as
sample size grows.
7

A2 and A3 share a similar structure and should be taken in tandem. They say that partial orderings
on second- and first-order distributions imply corresponding inequalities of epistemic and aleatoric
uncertainty, respectively. These axioms are justified by Defn. 5.2—the flatter and more spread out a
distribution is, the greater its uncertainty.
A4 and A5 are intended to capture the intuition that transformations that only impact a distribution’s
spread should increase uncertainty, while those that only impact location should not.
Theorem 5.1(Soundness).QUEST measures of AU and EU satisfy axioms A0-A5 for all α∈(0,1) ,
with weak inequality in the case of A4. Global EU satisfies A4 (strict) iff q≺q ′. QUEST T U
violatesA4(weak and strict).
The result is noteworthy because alternative measures of AU and EU for regression generally fail to
satisfy some of these axioms. For example, differential entropy violates A0, while variance violates
A2. Both measures violate the strict version of A4. Other results depend on limiting the analysis to
an exponential family of distributions; for full results, see [5].
Some mean-preserving spreads can reduce T Uin our framework. Specifically, this occurs when
the original model is overconfident, leading to improved calibration under a levelling of q. This is a
feature, not a bug—T Ushould reward belief revisions that bring an agent’s predictions closer to the
truth, even at the cost of increasing EU . Otherwise, we must either reward miscalibration or abandon
our commitment to a subjective EU measure. We choose to bite neither bullet, and instead reject A4
as unsuitable forT U. For further discussion on the uncertainty axioms, see Section F.
6 Experiments
Code for reproducing all results is available online.2 We evaluate UMs in settings designed to isolate
behaviour under unimodal and multimodal distribution structure. We focus onselective prediction, in
which predictions are made on only the top proportion r of most certain samples as ranked by some
UM. A good measure should lead to monotonically increasing loss on a test set asrincreases.
DesignGiven a training dataset D:={x i, yi}n i=1 sampled from a synthetic DGP, our goal is
to estimate the MAP y∗ := argmax y pθ∗ (y|x) 3 for each x∈ X in a test set. Methods are
provided access to the same deep ensemble [ 31], designed with mixture of experts (MoE) layers
[26], to produce a posterior predictive ˆp(y|x) :=
R
θ pθ(y|x)q(θ|x,D)dθ . We compute MAP estimates ˆyvia grid search over ˆpand evaluate performance using the log-likelihood ratio loss
L(ˆy) = logpθ∗ (y∗ |x)−logp θ∗ (ˆy|x). We report loss–retention curves in Fig. 3, where lower area
under the curve denotes a more accurate UM.
We use three DGPs of increasing structural complexity: unimodal Gaussian, unimodal skewed and
multimodal mixture. Our ensemble has M= 10 networks with K= 3 experts per network, where
each expert is a conditional unimodal Gaussian estimator. Evaluated UMs include T Umeasures of
variance, differential entropy, local QUEST (α-volume) and global QUEST (integrated volume). We
assess performance from the perspective of a density oracle with access topθ∗; results using maximum
likelihood approximations are reported in Section B.4. We repeat each experimental configuration 20
times, and plot average values with their associated standard errors. Further detail can be found in
Section B where we also provide details of a supplementary active learning experiment.
ResultsWe hypothesised that QUEST would provide more reliable uncertainty rankings by meas-
uring density concentration around dominant high-density regions, thereby improving performance
in selective prediction. The inability of pointwise risk estimators to correctly quantify uncertainty is
expected to be more pronounced in skewed and multimodal settings. We find that global QUEST
demonstrates superior performance above not only the random baseline, but variance, entropy and
local QUEST in all trials. (Poor performance across UMs in the Gaussian setting is likely attributable
to the unnecessary complexity of a deep MoE ensemble for this case.) Local QUEST fares no worse
than competitors in all settings and in the bimodal outperforms variance. Results of supplementary
active learning experiment shows QUEST performance in line with that of variance and entropy.
2https://github.com/sjgoring/modal-uq-public.
3We predictY|x, hence we change from speaking of distributionsX,Θto conditional distributionsY|X,Θ|X.
8

Normal Skewed Bimodal
0.25 0.50 0.75 1.00 0.25 0.50 0.75 1.00 0.25 0.50 0.75 1.00
0.00
0.01
0.02
0.03
0.04
0.05
0.00
0.02
0.04
0.00
0.02
0.04
0.06
Proportion retained
Selective loss
Variance Entropy QUEST (α=0.1) QUEST (global) Random
Figure 3: Selective learning curves for deep MoE ensembles on three different DGPs. Shading
represents standard errors across 20 trials.
7 Discussion
At a conceptual level, QUEST makes two independent contributions. First, we propose a volume-
centric UQ framework that quantifies uncertainty via concentration of measure at one or several
thresholds α. Second, we adopt a purely subjective notion of EU that is not truth-relative. Though
these components could in principle be decoupled, we present them as a unified whole. The former
follows from basic geometric intuitions; the latter from careful reflection on the proposed UM axioms.
For a more sustained discussion on those axioms and the trade-offs they imply, see Section F.
Several limitations merit acknowledgment. First, our theoretical results assume densities are ab-
solutely continuous w.r.t. Lebesgue measure, ruling out distributions with atoms or support on
lower-dimensional submanifolds. Extending the framework to handle such cases—for example, via
reference measures other than Lebesgue—is a natural direction for future work. Second, α-volume
and integrated volume can be costly to compute for high-dimensional or non-analytic densities,
where HDR boundaries must be approximated numerically. Efficient estimation procedures, perhaps
leveraging recent advances in normalising flows [38] or score-based density estimation [49], would
substantially broaden the framework’s applicability.
Our experimental results rely on access to an oracle density, which is unavailable outside of experi-
mental settings. The question of how to evaluate UMs without access to such privileged information
is somewhat fraught; see [ 47]. Common options include Bayesian model averaging, maximum
likelihood estimation, or alternative hybrids. Each method has its strengths and weaknesses, but
we judge such debates to be orthogonal to our main focus, which is the introduction of a new UQ
framework. Systematically examining the impact of such choices on measure performance is a
promising direction for future work.
HDRs come with optimal false coverage guarantees via the Ghosh-Pratt lemma [14, 42]. A related
result is that HDRs are intrinsically linked to acceptance regions for uniformly most powerful tests
[32]. Investigating the link between hypothesis testing and uncertainty quantification may provide
more machinery for UQ. Similarly, the connection to Lorenz dominance suggests that other tools
from the inequality measurement literature—Atkinson indices, generalized entropies—may yield
further insights for UQ. Whilst there has been some work on volumetric measures of uncertainty (e.g
[43]), we hope that QUEST will spur further investigation into the geometric foundations of UQ.
8 Conclusion
We have introduced QUEST, a framework for uncertainty quantification grounded in the Lebesgue
measure of highest density regions. By centering UQ on density concentration rather than pointwise
predictive risk, QUEST avoids the pathologies of PSR-based measures. We established connections
between our measures and classical statistics from information theory and economics, showing that
QUEST sits naturally within a broader analytical tradition. Our axiomatic analysis demonstrates
that QUEST measures of AU and EU are sound w.r.t. a standard set of UQ axioms, while our
experiments show favourable performance against state-of-the-art alternatives in selective prediction.
Future work will explore extensions to statistical inference, as well as generalizations that do not
require second-order distributions.
9

Ethics and AI Safety statement
This work develops methods for uncertainty quantification (UQ), which can improve the reliability of
AI systems and support safer decision-making by reducing overconfident or erroneous predictions.
Such improvements are particularly valuable in domains where safety criteria are well-established
(e.g. healthcare or engineering systems).
However, the concept of “safety” is not universally agreed upon, particularly in socio-technical
domains such as social media, surveillance, or automated decision-making. In such settings, the same
UQ techniques may be used to support applications that some stakeholders consider harmful—for
example, by enabling more effective targeting, filtering, or behavioural influence.
As methodological researchers, we have limited control over downstream applications of these
techniques. Nevertheless, we recognise that UQ methods are dual-use: while they can reduce harmful
outcomes, they may also increase the effectiveness or credibility of systems deployed in ethically
contested contexts.
This work meets the ethical requirements of King’s College London and is primarily motivated
by applications in domains with widely accepted safety objectives. We emphasise, however, the
importance of careful consideration when applying these methods, including transparency about
uncertainty, appropriate domain-specific evaluation, and awareness of potential societal impacts.
We encourage practitioners and users of this work to critically assess both the benefits and risks of
deploying UQ-enabled systems in their specific context.
Acknowledgments and Disclosure of Funding
SG is supported by UK Research and Innovation [grant number EP/S023356/1], in the UKRI Centre
for Doctoral Training in Safe and Trusted Artificial Intelligence.4 DSW was supported by EPSRC
grant number UKRI918. We gratefully acknowledge the use of the CREATE HPC system for
conducting our experiments [29].
References
[1] Alexander Amini, Wilko Schwarting, Ava Soleimany, and Daniela Rus. Deep Eviden-
tial Regression. InAdvances in Neural Information Processing Systems, volume 33, pages
14927–14937, 2020. URL https://proceedings.neurips.cc/paper_files/paper/2020/hash/
aab085461de182608ee9f607f3f7d18f-Abstract.html.
[2] Lucas Berry and David Meger. Epistemic Uncertainty Estimation in Regression Ensemble Models
with Pairwise Epistemic Estimators.Advances in Neural Information Processing Systems, 38:64503–
64536, April 2026. URL https://proceedings.neurips.cc/paper_files/paper/2025/hash/
5d45a97ec44d8232bf718e92aab99a47-Abstract-Conference.html.
[3] Lawrence D. Brown, George Casella, and J. T. Gene Hwang. Optimal Confidence Sets, Bioequi-
valence, and the Limaçon of Pascal.Journal of the American Statistical Association, 90(431):
880–889, September 1995. ISSN 0162-1459. doi: 10.1080/01621459.1995.10476587. URL
https://doi.org/10.1080/01621459.1995.10476587. Publisher: ASA Website _eprint: ht-
tps://doi.org/10.1080/01621459.1995.10476587.
[4] Christopher Bülte, Yusuf Sale, Gitta Kutyniok, and Eyke Hüllermeier. Uncertainty Quantification for
Regression: A Unified Framework based on kernel scores, October 2025. URL http://arxiv.org/
abs/2510.25599. arXiv:2510.25599 [cs].
[5] Christopher Bülte, Yusuf Sale, Timo Löhr, Paul Hofman, Gitta Kutyniok, and Eyke Hüllermeier. An
Axiomatic Assessment of Entropy- and Variance-based Uncertainty Quantification in Regression, May
2025. URLhttp://arxiv.org/abs/2504.18433. arXiv:2504.18433 [cs].
[6] Michele Caprio, David Stutz, Shuo Li, and Arnaud Doucet. Conformalized Credal Regions for Classifica-
tion with Ambiguous Ground Truth.Transactions on Machine Learning Research, November 2024. ISSN
2835-8856. URLhttps://openreview.net/forum?id=L7sQ8CW2FY.
4www.safeandtrustedai.org.
10

[7] Michele Caprio, Yusuf Sale, and Eyke Hüllermeier. Conformal prediction regions are imprecise highest
density regions. InProceedings of the Fourteenth International Symposium on Imprecise Probabilities:
Theories and Applications, pages 47–59. PMLR, May 2025. URL https://proceedings.mlr.press/
v290/caprio25b.html.
[8] Harrison Charpentier, Ransalu Senanayake, Mykel Kochenderfer, and Stephan Günnemann. Disentangling
Epistemic and Aleatoric Uncertainty in Reinforcement Learning. InICML 2022 Workshop on Distribution-
Free Uncertainty Quantification, 2022. URLhttp://arxiv.org/abs/2206.01558.
[9] Thomas M. Cover and Joy A. Thomas.Elements of Information Theory. John Wiley & Sons, Hoboken,
NJ, second edition, 2006.
[10] Frank A. Cowell.Measuring Inequality. Oxford University Press, Oxford, third edition, 2011.
[11] Yunlong Feng, Xiaolin Huang, Lei Shi, Yuning Yang, and Johan A.K. Suykens. Learning with the
maximum correntropy criterion induced losses for regression.Journal of Machine Learning Research, 16
(30):993–1034, 2015.
[12] Alexander Fishkov, Kajetan Schweighofer, Mykyta Ielanskyi, Nikita Kotelevskii, Mohsen Guizani, and
Maxim Panov. Uncertainty Quantification for Regression using Proper Scoring Rules, September 2025.
URLhttp://arxiv.org/abs/2509.26610. arXiv:2509.26610 [cs].
[13] Yarin Gal and Zoubin Ghahramani. Dropout as a bayesian approximation: Representing model uncertainty
in deep learning. InProceedings of The 33rd International Conference on Machine Learning, pages
1050–1059, 2016.
[14] Jayanta Kumar Ghosh. On the Relation Among Shortest Confidence Intervals of Different Types.
Calcutta Statistical Association Bulletin, 10(4):147–152, September 1961. ISSN 0008-0683, 2456-
6462. doi: 10.1177/0008068319610404. URL https://journals.sagepub.com/doi/10.1177/
0008068319610404.
[15] Tilmann Gneiting and Adrian E Raftery. Strictly Proper Scoring Rules, Prediction, and Estimation.
Journal of the American Statistical Association, 102(477):359–378, March 2007. ISSN 0162-1459, 1537-
274X. doi: 10.1198/016214506000001437. URL http://www.tandfonline.com/doi/abs/10.1198/
016214506000001437.
[16] Xabier Gonzalez-Garcia, Siu Lun Chau, Julian Rodemann, Michele Caprio, Krikamol Muandet, Humberto
Bustince, Sébastien Destercke, Eyke Hüllermeier, and Yusuf Sale. Quantification of Credal Uncertainty: A
Distance-Based Approach, March 2026. URLhttp://arxiv.org/abs/2603.27270. arXiv:2603.27270
[cs].
[17] Misgina Tsighe Hagos and Claes Lundstrom. Performance of Conformal Prediction in Capturing Aleatoric
Uncertainty. In2026 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV), pages
2954–2963, Los Alamitos, CA, USA, March 2026. IEEE Computer Society. doi: 10.1109/W ACV61042.
2026.00289. URLhttps://doi.ieeecomputersociety.org/10.1109/WACV61042.2026.00289.
[18] Charles R. Harris, K. Jarrod Millman, Stéfan J. van der Walt, Ralf Gommers, Pauli Virtanen, David
Cournapeau, Eric Wieser, Julian Taylor, Sebastian Berg, Nathaniel J. Smith, Robert Kern, Matti Picus,
Stephan Hoyer, Marten H. van Kerkwijk, Matthew Brett, Allan Haldane, Jaime Fernández del Río, Mark
Wiebe, Pearu Peterson, Pierre Gérard-Marchant, Kevin Sheppard, Tyler Reddy, Warren Weckesser, Hameer
Abbasi, Christoph Gohlke, and Travis E. Oliphant. Array programming with NumPy.Nature, 585(7825):
357–362, September 2020. doi: 10.1038/s41586-020-2649-2. URL https://doi.org/10.1038/
s41586-020-2649-2.
[19] C. Heinrich. The mode functional is not elicitable.Biometrika, 101(1):245–251, 2014.
[20] Paul Hofman, Yusuf Sale, and Eyke Hüllermeier. Quantifying Aleatoric and Epistemic Uncertainty: A
Credal Approach. InICML 2024 Workshop on Structured Probabilistic Inference & Generative Modeling,
July 2024. URLhttps://openreview.net/forum?id=MhLnSoWp3p.
[21] Neil Houlsby, Ferenc Huszár, Zoubin Ghahramani, and Máté Lengyel. Bayesian Active Learning for
Classification and Preference Learning, December 2011. URL http://arxiv.org/abs/1112.5745.
arXiv:1112.5745 [cs, stat].
[22] Peter Huber and Elvezio Ronchetti.Robust Statistics. Wiley & Sons, New York, Second edition, 2009.
[23] J. D. Hunter. Matplotlib: A 2d graphics environment.Computing in Science & Engineering, 9(3):90–95,
2007. doi: 10.1109/MCSE.2007.55.
11

[24] Rob J. Hyndman. Computing and Graphing Highest Density Regions.The American Statistician, 50(2):120–
126, 1996. ISSN 0003-1305. doi: 10.2307/2684423. URL https://www.jstor.org/stable/2684423.
Publisher: [American Statistical Association, Taylor & Francis, Ltd.].
[25] Eyke Hüllermeier and Willem Waegeman. Aleatoric and epistemic uncertainty in machine learning: an
introduction to concepts and methods.Machine Learning, 110(3):457–506, 2021.
[26] Robert A. Jacobs, Michael I. Jordan, Steven J. Nowlan, and Geoffrey E. Hinton. Adaptive mixtures of
local experts.Neural Computation, 3(1):79–87, 1991.
[27] Alireza Javanmardi, David Stutz, and Eyke Hüllermeier. Conformalized Credal Set Predictors.Ad-
vances in Neural Information Processing Systems, 37:116987–117014, December 2024. doi: 10.
52202/079017-3714. URL https://proceedings.neurips.cc/paper_files/paper/2024/hash/
d42a8bf2f40555d4a5120300f98c88f6-Abstract-Conference.html.
[28] Alex Kendall and Yarin Gal. What Uncertainties Do We Need in Bayesian Deep Learning for Computer
Vision?, October 2017. URLhttp://arxiv.org/abs/1703.04977. arXiv:1703.04977 [cs].
[29] King’s College London. King’s Computational Research, Engineering and Technology Environment
(CREATE), 2022. URLhttps://doi.org/10.18742/rnvf-m076. Retrieved March 2, 2022.
[30] Nikita Kotelevskii, Vladimir Kondratyev, Martin Taká ˇc, Eric Moulines, and Maxim Panov.
From Risk to Uncertainty: Generating Predictive Uncertainty Measures via Bayesian Es-
timation.International Conference on Learning Representations, 2025:92468–92504,
May 2025. URL https://proceedings.iclr.cc/paper_files/paper/2025/hash/
e6f32e64b9c27d153b46c94f0fe22b56-Abstract-Conference.html.
[31] Balaji Lakshminarayanan, Alexander Pritzel, and Charles Blundell. Simple and Scalable Predictive
Uncertainty Estimation using Deep Ensembles. InAdvances in Neural Information Processing Systems,
volume 30. Curran Associates, Inc., 2017. URL https://proceedings.neurips.cc/paper_files/
paper/2017/hash/9ef2ed4b7fd2c810847ffa5fa85bce38-Abstract.html.
[32] E.L. Lehmann and Joseph P. Romano.Testing Statistical Hypotheses. Springer, New York, Third edition,
2005.
[33] Andrey Malinin, Sergey Chervontsev, Ivan Provilkov, and Mark Gales. Regression Prior Networks,
December 2020. URLhttp://arxiv.org/abs/2006.11590. arXiv:2006.11590 [cs].
[34] Albert W. Marshall, Ingram Olkin, and Barry C. Arnold.Inequalities: Theory of Majorization and Its
Applications. Springer Series in Statistics. Springer, New York, second edition, 2011.
[35] Nis Meinert and Alexander Lavin. Multivariate Deep Evidential Regression, February 2022. URL
http://arxiv.org/abs/2104.06135. arXiv:2104.06135 [cs].
[36] V olodymyr Mnih, Koray Kavukcuoglu, David Silver, Andrei A Rusu, Joel Veness, Marc G Bellemare,
Alex Graves, Martin Riedmiller, Andreas K Fidjeland, Georg Ostrovski, et al. Human-level control through
deep reinforcement learning.Nature, 518(7540):529–533, 2015.
[37] Kevin P. Murphy.Probabilistic Machine Learning: An introduction. The MIT Press, Cambridge, 2022.
[38] George Papamakarios, Eric Nalisnick, Danilo Jimenez Rezende, Shakir Mohamed, and Balaji Lakshmin-
arayanan. Normalizing flows for probabilistic modeling and inference.Journal of Machine Learning
Research, 22(57):1–64, 2021.
[39] Adam Paszke, Sam Gross, Francisco Massa, Adam Lerer, James Bradbury, Gregory Chanan, Trevor
Killeen, Zeming Lin, Natalia Gimelshein, Luca Antiga, Alban Desmaison, Andreas Köpf, Edward Z. Yang,
Zach DeVito, Martin Raison, Alykhan Tejani, Sasank Chilamkurthy, Benoit Steiner, Lu Fang, Junjie Bai,
and Soumith Chintala. Pytorch: An imperative style, high-performance deep learning library.CoRR,
abs/1912.01703, 2019. URLhttp://arxiv.org/abs/1912.01703.
[40] F. Pedregosa, G. Varoquaux, A. Gramfort, V . Michel, B. Thirion, O. Grisel, M. Blondel, P. Prettenhofer,
R. Weiss, V . Dubourg, J. Vanderplas, A. Passos, D. Cournapeau, M. Brucher, M. Perrot, and E. Duchesnay.
Scikit-learn: Machine learning in Python.Journal of Machine Learning Research, 12:2825–2830, 2011.
[41] Yury Polyanskiy and Yihong Wu.Information Theory: From Coding to Learning. Cambridge University
Press, 2025.
[42] John W. Pratt. Shorter Confidence Intervals for the Mean of a Normal Distribution with Known Variance.
The Annals of Mathematical Statistics, 34(2):574–586, 1963. ISSN 0003-4851. URL https://www.
jstor.org/stable/2238404.
12

[43] Yusuf Sale, Michele Caprio, and Eyke Höllermeier. Is the volume of a credal set a good measure for
epistemic uncertainty? InProceedings of the Thirty-Ninth Conference on Uncertainty in Artificial
Intelligence, pages 1795–1804. PMLR, July 2023. URL https://proceedings.mlr.press/v216/
sale23a.html.
[44] Yusuf Sale, Viktor Bengs, Michele Caprio, and Eyke Hüllermeier. Second-order uncertainty quantification:
A distance-based approach. InForty-first International Conference on Machine Learning, 2024.
[45] Yusuf Sale, Alireza Javanmardi, and Eyke Hüllermeier. Aleatoric and Epistemic Uncertainty in Conformal
Prediction. InProceedings of the Fourteenth Symposium on Conformal and Probabilistic Prediction with
Applications, pages 784–786. PMLR, August 2025. URL https://proceedings.mlr.press/v266/
sale25a.html.
[46] Kajetan Schweighofer, Lukas Aichberger, Mykyta Ielanskyi, and Sepp Hochreiter. Introducing an Im-
proved Information-Theoretic Measure of Predictive Uncertainty. InNeurIPS 2023 Workshop on Math-
ematics of Modern Machine Learning, November 2023. URL https://openreview.net/forum?id=
c71B6zW70d.
[47] Kajetan Schweighofer, Lukas Aichberger, Mykyta Ielanskyi, and Sepp Hochreiter. On information-
theoretic measures of predictive uncertainty. InProceedings of the Forty-First Conference on Uncertainty
in Artificial Intelligence, 2025.
[48] Amartya Sen.On Economic Inequality. Clarendon Press, Oxford, 1997.
[49] Yang Song, Sahaj Garg, Jiaxin Shi, and Stefano Ermon. Sliced score matching: A scalable approach to
density and score estimation. InProceedings of The 35th Uncertainty in Artificial Intelligence Conference,
pages 574–584, 2020.
[50] J Terry, Benjamin Black, Nathaniel Grammel, Mario Jayakumar, Ananth Hari, Ryan Sullivan, Luis S
Santos, Clemens Dieffendahl, Caroline Horsch, Rodrigo Perez-Vicente, et al. Pettingzoo: Gym for multi-
agent reinforcement learning.Advances in Neural Information Processing Systems, 34:15032–15043,
2021.
[51] Matias Valdenegro-Toro and Daniel Saromo Mori. A Deeper Look into Aleatoric and Epistemic Uncertainty
Disentanglement. In2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
(CVPRW), pages 1508–1516, June 2022. doi: 10.1109/CVPRW56347.2022.00157. URL https://
ieeexplore.ieee.org/abstract/document/9857056. ISSN: 2160-7516.
[52] Pauli Virtanen, Ralf Gommers, Travis E. Oliphant, Matt Haberland, Tyler Reddy, David Cournapeau,
Evgeni Burovski, Pearu Peterson, Warren Weckesser, Jonathan Bright, Stéfan J. van der Walt, Matthew
Brett, Joshua Wilson, K. Jarrod Millman, Nikolay Mayorov, Andrew R. J. Nelson, Eric Jones, Robert
Kern, Eric Larson, C J Carey, ˙Ilhan Polat, Yu Feng, Eric W. Moore, Jake VanderPlas, Denis Laxalde,
Josef Perktold, Robert Cimrman, Ian Henriksen, E. A. Quintero, Charles R. Harris, Anne M. Archibald,
Antônio H. Ribeiro, Fabian Pedregosa, Paul van Mulbregt, and SciPy 1.0 Contributors. SciPy 1.0:
Fundamental Algorithms for Scientific Computing in Python.Nature Methods, 17:261–272, 2020. doi:
10.1038/s41592-019-0686-2.
[53] V . V ovk, A. Gammerman, and G. Shafer.Algorithmic Learning in a Random World. Springer-Verlag, New
York, 2005. ISBN 978-0-387-00152-4. doi: 10.1007/b106715. URL http://link.springer.com/10.
1007/b106715.
[54] Peter Walley.Statistical reasoning with imprecise probabilities. London ; New York :
Chapman and Hall, 1991. ISBN 978-0-412-28660-5. URL http://archive.org/details/
statisticalreaso0000wall.
[55] Kaizheng Wang, Fabio Cuzzolin, Shireen K. Manchingal, Keivan Shariatmadar, David Moens,
and Hans Hallez. Credal Deep Ensembles for Uncertainty Quantification.Advances
in Neural Information Processing Systems, 37:79540–79572, December 2024. doi: 10.
52202/079017-2525. URL https://proceedings.neurips.cc/paper_files/paper/2024/hash/
911fc798523e7d4c2e9587129fcf88fc-Abstract-Conference.html.
[56] Lisa Wimmer, Yusuf Sale, Paul Hofman, Bernd Bischl, and Eyke Hüllermeier. Quantifying aleatoric and
epistemic uncertainty in machine learning: Are conditional entropy and mutual information appropriate
measures? InProceedings of the 39th Conference on Uncertainty in Artificial Intelligence, pages 2282–
2292, 2023.
13

A Proofs
In this section, we include proofs for all propositions and theorems.
Proposition. For any pdfponX ⊆R d and anyα∈(0,1)such thatV α(p)<∞:
logV α(p) =h(p α, uα),
wherep α :=p(· |X∈C α)andu α is the uniform density onC α.
Proof. On Cα we have uα(x) = 1/Vα(p), hence logu α(x) =−logV α(p) for every x∈C α. The conditional
densityp α is supported onC α and integrates to one, so
h(pα, uα) =−
Z
Cα
pα(x) logu α(x)dx
= logV α(p)·
Z
Cα
pα(x)dx
= logV α(p),
which is the claimed identity.
Remark(Decomposition into entropy and KL). Using the standard relation h(p, r) =h(p) +DKL(p∥r) for
any densityqand referencer, the proposition rewrites as
logV α(p) =h(p α) +D KL(pα ∥u α),
exposing log HDR volume as the conditional entropy on the HDR plus a divergence term measuring deviation of
pα from uniform onC α.
Proposition. Letpbe a density on[0,1] d. Then we have the following two identities.
(a) For every α∈(0,1) , the Lorenz p-curve satisfies Lp

1−V α(p)

=α . Equivalently, the curves
α7→V α(p)andz7→L p(z)are related by the coordinate flip(α, Vα)7→(1−V α, α).
(b) The Ginip-coefficient satisfiesG p = 1−2·IV(p).
Proof. The strategy is to identify the set {x:p(x)≤q p(1−V α(p))} as the complement of the HDR Cα(p),
then evaluate the Lorenz curve at this point directly.
Letz ∗ := 1−V α(p). SinceV α(p)∈(0,1)for anyα∈(0,1)on the unit cube, we havez ∗ ∈(0,1).
Step 1:The quantile qp(z∗) equals the HDR threshold. Define thesurvival function of the density µp : [0,∞)→
[0,1]by
µp(t) :=λ

{x:p(x)> t}

,
whereλdenotes Lebesgue measure. By definition,
qp(z∗) = inf  t≥0 :λ({x:p(x)≤t})≥z ∗	 .
The set{x:p(x)≤t}has Lebesgue measure1−µ p(t), sinceλ(X) = 1. So
qp(z∗) = inf{t≥0 : 1−µ p(t)≥z ∗}= inf{t≥0 :µ p(t)≤1−z ∗ =V α(p)}.
Recall that the HDR threshold at level α is defined as tα(p) = sup

t≥0 :
R
{p≥t
	 p dλ≥1−α} , and the
HDR is Cα =

x:p(x)≥t α(p)

with Vα(p) =λ(C α). Under the level-set condition λ({p=t}) = 0 for
allt >0, 5 we haveλ(C α) =λ({p > tα(p)}) =µ p(tα(p)), hence
µp(tα(p)) =V α(p).
Combined with the fact that µp is strictly decreasing on the range of HDR thresholds under our stated regularity
condition, this givesinf{t≥0 :µ p(t)≤V α(p)}=t α(p), and thereforeq p(z∗) =t α(p).
Step 2:Thep-Lorenz curve evaluation. By definition,
Lp(z∗) =
Z
{x:p(x)≤qp(z∗)}
p(x)dx=
Z
{x:p(x)≤tα(p)}
p(x)dx.
5This condition ensures that HDRs are uniquely defined and that Vα is absolutely continuous in α. This assumption
is convenient but not necessary. For densities with plateaus, the proof extends by taking the minimal HDR at each point
and replacing the change of variables argument in Step 3 below with a Lebesgue-Stieltjes formulation. The conclusion is
unchanged.
14

Under the level-set condition, the sets {p≤t α} and {p < tα} differ by a Lebesgue null set, and the latter is the
complement of the HDRC α ={p≥t α}. So
Lp(z∗) =
Z
Ccα
p(x)dx= 1−
Z
Cα
p(x)dx= 1−(1−α) =α.
Substitutingz ∗ = 1−V α(p)gives the claimed identity of item (a).
Step 3:Evaluating the p-Gini coefficient.By (a), the Lorenz curve Lp and the coverage curve are related by the
coordinate flipL p(1−V α(p)) =α. We compute the Gini coefficient by a change of variables.
By definition,
Gp = 1−2
Z 1
0
Lp(z)dz.
Substitute z= 1−V α(p), so dz=−V ′ α(p)dα , where V ′ α denotes the derivative of Vα with respect to α. By
(a), Lp(z) =α at this substitution. The integration limits transform: as α ranges over (0,1) , z= 1−V α(p)
ranges from 1−V 0(p) = 0 at α= 0 (since V0(p) = 1 on the unit cube) to 1−V 1(p) = 1 at α= 1 (since
V1(p) = 0). Note thatV α is non-increasing inα, soV ′ α ≤0and−V ′ α ≥0.
The integral becomes
Z 1
0
Lp(z)dz=
Z 1
0
α·(−V ′ α(p))dα.
Integrate by parts withf(α) =αandg ′(α) =−V ′ α(p), hencef ′(α) = 1andg(α) =−V α(p):
Z 1
0
α·(−V ′ α(p))dα=  α·(−V α(p)) 1 0 + Z 1 0 Vα(p)dα= (−V 1(p))−0 +IV(p) =IV(p),
usingV 1(p) = 0.
Therefore,
Gp = 1−2·IV(p),
which concludes the proof.
Proposition.Letp, p′ be pdfs onR d with supportsX,X ′. For thresholds0< τ ℓ < τu <∞, define
Xτ :={x:τ ℓ < p(x)≤τ u},X ′ τ :={x:τ ℓ < p′(x)≤τ u},Y τ :=X τ ∪ X′ τ ,
and let uτ denote the uniform density onYτ . Write pτ , p′ τ for the conditional densities ofp, p′ on their respective
level-set windows. Thenp∼p ′ if and only if, for every threshold pair(τ ℓ, τu)and everyf-divergenceD f :
Df (pτ ||u τ ) =D f (p′ τ ||u τ ).
Proof. For thresholds (τℓ, τu) where Vτ :=λ(X τ ) and V ′ τ :=λ(X ′ τ ) are both positive, write Wτ :=λ(Y τ ),
mτ :=
R
Xτ p dλ, m′ τ := R X ′τ p′ dλ. Let µp(t) :=λ({p > t}) denote the level-set volume function, so spread-equivalence assertsµ p ≡µ p′.
Step 1: Divergence decomposition.Sincep τ vanishes outsideX τ butu τ =W −1 τ is positive throughoutY τ :
Df (pτ ∥uτ ) = 1 Wτ
Z
Xτ
f
 Wτ p(x)
mτ

dx+ f(0) (Wτ −V τ ) Wτ .
Multiplying through byW τ , the divergence equality is equivalent to
Af (p, τ)−f(0)V τ =A f (p′, τ)−f(0)V ′ τ ,(1)
where
Af (p, τ) :=
Z
Xτ
f
 Wτ p(x)
mτ

dx.
Step 2: Forward direction.Supposeµ p ≡µ p′. Then for any window:
Vτ =µ p(τℓ)−µ p(τu) =V ′ τ ,
15

so the f(0)V τ terms in Eq. 1 match. By layer-cake, using λ({p > s} ∩ Xτ ) =V τ for s < τℓ, =µ p(s)−µ p(τu)
fors∈[τ ℓ, τu], and= 0fors≥τ u:
mτ =τ ℓVτ +
Z τu
τℓ
µp(s)ds−(τ u −τ ℓ)µp(τu),
which depends only onµ p on[τ ℓ, τu]and at the endpoints. Spread-equivalence therefore givesm τ =m ′ τ .
The conditional CDF ofp(X)givenX∈ X τ (withXuniform onX τ ) at levels∈[τ ℓ, τu]equals
µp(s)−µ p(τu)
Vτ
,
which is determined by µp alone. Spread-equivalence gives equality of these CDFs across p and p′.
Combined with Wτ /mτ =W τ /m′ τ being a deterministic monotone rescaling, the two random variables
Wτ p(X)/m τ |X∈ Xτ andW τ p′(X ′)/m′ τ |X ′ ∈ X′ τ are equal in distribution. Hence
Af (p, τ) =Vτ E

f

Wτ p(X)
mτ


 X∈ Xτ  =V ′ τ E  f  Wτ p′(X′) m′τ 

 X ′ ∈ X′ τ  =A f (p′, τ),
which together withV τ =V ′ τ gives Eq. 1.
Step 3: Reverse direction.Suppose that Df (pτ ||u τ ) =D f (p′ τ ||u τ ) for every f-divergence and threshold
pairτ= (τ ℓ, τu). Define
Y:= Wτ p(X) mτ , Y ′ := Wτ p(X) m′τ .
Since τℓ >0, τu <∞ , and mτ , m′ τ ∈(0,∞) , both Y and Y ′ are supported on compact subsets of (0,∞) . Let
ν, ν′ denote their respective laws.
Rearranging the divergence decomposition of Step 1 gives
Wτ Df (pτ ||u τ ) =V τ E

f(Y)

+f(0)(W τ −V τ ),
and analogously forp ′ τ . Since the divergences are equal by assumption, we have
Vτ E

f(Y)

+f(0)(W τ −V τ ) =V ′ τ E  f(Y ′)  +f(0)(W τ −V ′ τ ).
Rearranging gives
Vτ E

f(Y)

−f(0) =V ′ τ E  f(Y ′)  −f(0).
Consider the family of power divergences fk(t) =t k −1 for integers k≥2 . These functions are convex and
satisfyf k(1) = 0. Sincef k(0) =−1, the preceding equation becomes
Vτ E

Y k =V ′ τ E  Y ′k , k≥2.
This is the key moment identity. Let K⊂(0,∞) be a compact interval containing the supports of both ν and
ν′. Define a finite signed measureσonKby
dσ(y) :=y 2 Vτ , dν(y)−V ′ τ , dν′(y)  .
For every integerj≥0, the moment identity withk=j+ 2gives
Z
K
yj, dσ(y) =Vτ E[Y j+2]−V ′ τ E[Y ′j+2] = 0.
Thus every polynomial has zero integral with respect to σ. Since polynomials are dense in C(K) by the
Weierstrass approximation theorem, it follows that
Z
K
g(y), dσ(y) = 0
for every continuous functiong∈C(K). Henceσ= 0as a finite signed measure onK.
Because K⊂(0,∞) , the function y7→y −2 is bounded and continuous on K. Multiplying by y−2, we obtain
Vτ dν=V ′ τ dν′.
Taking total masses on both sides yields
Vτ =V ′ τ ,
since ν and ν′ are probability measures. Therefore, for every admissible threshold pair(τℓ, τu), λ(Xτ ) =λ(X ′ τ ).
Equivalently, we have
λ{x:τ ℓ < p(x)≤τ u}=λ{x:τ ℓ < p′(x)≤τ u}.
16

In terms of the superlevel-volume functions
µp(t) :=λ{x:p(x)> t}, µ p′ (t) :=λ{x:p ′(x)> t}.
This says that
µp(τℓ)−µ p(τu) =µ p′ (τℓ)−µ p′ (τu)
for all0< τ ℓ < τu <∞, up to the usual endpoint convention for level sets. Hence the difference
∆(t) :=µ p(t)−µ p′ (t)
is constant on(0,∞). Sincepandp ′ are probability densities, Markov’s inequality gives
µp(t)≤ 1 t , µ p′ (t)≤ 1 t ,
and therefore both µp(t) and µp′ (t) converge to 0 as t→ ∞. The constant value of ∆(t) must therefore be 0.
Thus
µp(t) =µ p′ (t)for allt >0,
which is precisely spread-equivalence,p∼p ′.
Theorem(Soundness). QUEST measures of AU and EU satisfy axioms A0-A5 for all α∈(0,1) , with weak
inequality in the case ofA4. GlobalEUsatisfiesA4(strict) iffq≺q ′.T UviolatesA4(weak and strict).
Proof.We begin by deriving a crucial lemma, which will be repeatedly invoked below.
Lemma(Partial ordering). Suppose that p⪯p ′. Then (a) for any α∈(0,1), V α(p)≤V α(p′); and (b)
IV(p)≤IV(p ′), with equality in both cases iffp∼p ′.
Proof. Our strategy is to show that levelling implies an ordering on cumulative density profiles, from which the
HDR-volume inequalities follow directly.
For a densityponX ⊆R d, define the survival function of the densityµ p : [0,∞)→[0,∞]by
µp(t) :=λ

{x∈ X:p(x)> t}

,
where λ denotes Lebesgue measure. Markov’s inequality gives µp(t)≤1/t for t >0, so µp is finite on (0,∞) .
The decreasing rearrangement ofpis
p↓(r) := inf{t≥0 :µ p(t)≤r}, r≥0.
This function is non-increasing, right-continuous, and equimeasurable withp, meaning
λ

{x:p(x)> t}

=λ 1

{r:p ↓(r)> t} 
for allt≥0, whereλ 1 denotes one-dimensional Lebesgue measure. Define the cumulative profile
P(r) :=
Z r
0
p↓(s), ds, r≥0.
The functionPis non-decreasing, continuous, and bounded above by1. DefineP ′ analogously fromp ′.
Step 1: HDR volume in terms of the cumulative profile.Under the level-set assumption λ({p=t}) = 0 for
allt >0, the HDR threshold
tα(p) := sup

t:
Z
p≥t
p dλ≥1−α

satisfies
Z
Cα(p)
p dλ=
Z Vα(p)
0
p↓(s)ds=P  Vα(p)  = 1−α.
The first equality follows from equimeasurability of p and p↓, since the HDR corresponds to the upper level set
of p, or equivalently to the initial segment of its decreasing rearrangement. Thus, with the usual generalized
inverse convention,
Vα(p) =P −1(1−α) := inf{r≥0 :P(r)≥1−α}.
The same representation holds forp ′:
Vα(p′) =P ′−1(1−α).
17

The level-set assumption is convenient but not essential. If p has plateaus, we take Vα(p) to be the minimal
HDR volume and interpret the preceding display using the generalized inverse; the same argument then goes
through by right-continuity.
Step 2: Levelling implies majorization.We first consider the case where p⪯p ′ via L1. Let A and B be the
donor and recipient regions in Defn. 5.2. Define
a(x) :=p(x)−p ′(x)≥0, x∈A
b(x) :=p ′(x)−p(x)≥0, x∈B.
ByL1(a), mass is conserved:
Z
A
a(x), dλ(x) =
Z
B
b(x), dλ(x).
By L1(b), p and p′ agree outside A∪B . Thus, to compare the spread of p and p′, it suffices to compare the loss
onAwith the gain onB.
We use the standard positive-part characterization of majorization [34]: for non-negative integrable functions
with equal total integral,p ↓ majorizesp ′↓ iff
Z
(p−c) + dλ≥
Z
(p′ −c) + dλ∀c≥0.
Fixc≥0. The loss in the positive-part functional caused by lowering the density onAis
Lc :=
Z
A

(p(x)−c) + −(p ′(x)−c) + 	 dλ(x).
Using(u−c) + −(v−c) + =
R u
v 1{s > c}dsforu≥v, this can be written as
Lc =
Z
A
Z p(x)
p′(x)
1{s > c}ds dλ(x).
Similarly, the gain onBis
Gc :=
Z
B

(p′(x)−c) + −(p(x)−c) + 	 dλ(x)
=
Z
B
Z p′(x)
p(x)
1{s > c}ds dλ(x).
Recall that L1(d) prevents level crossing. If x∈A , then every removed layer has height s∈[p ′(x), p(x)]. If
y∈B, then every added layer has heightr∈[p(y), p ′(y)]. ByL1(d),
inf
A
p≥sup
B
pandinf
A
p′ ≥sup
B
p′,
so every removed layer lies weakly above every added layer:
s≥p ′(x)≥inf
A
p′ ≥sup
B
p′ ≥p ′(y)≥r.
Moreover, the total volume of removed layers equals the total volume of added layers, since
Z
A
Z p(x)
p′(x)
ds dλ(x) =
Z
A
a(x)dλ(x) =
Z
B
b(x)dλ(x) =
Z
B
Z p′(x)
p(x)
ds dλ(x).
Because the removed layer-volume lies entirely at heights weakly above the added layer-volume, thresholding at
any levelccan count no more added layer-volume than removed layer-volume. Hence
Gc ≤L c ∀c≥0.
It follows that Z
(p−c) + dλ−
Z
(p′ −c) + dλ=L c −G c ≥0.
Therefore Z
(p−c) +, dλ≥
Z
(p′ −c) +, dλ∀c≥0.
By the positive-part characterization,p ↓ majorizesp ′↓. Equivalently,
P(r) =
Z r
0
p↓(s)ds≥
Z r
0
p′↓(s)ds=P ′(r)∀r≥0.
18

Table 2: QUEST measures of uncertainty. (Reproduced from table 1 for convenience)
Aleatoric Epistemic Total
LocalV α(pθ∗ )V α(q)V α(pθ∗ )·g f

Df (p↓ α ||ˆpα) 
GlobalIV(p θ∗ )IV(q) R 1 0 Vα(pθ∗ )·g f  Df (p↓ α ||ˆpα)  dα
Now suppose p⪯p ′ via L2. Then there exists a density p′′ such that p′′ ∼p and p′′ ⪯p ′ via L1. Since
spread-equivalent densities have the same decreasing rearrangement, p′′↓ =p ↓ and hence P ′′ =P . Applying
the precedingL1argument top ′′ andp ′ gives
P(r) =P
′′
(r)≥ P′(r)∀r≥0.
Thusp⪯p ′ impliesP ≥ P′ pointwise.
Step 3: Cumulative profile ordering implies HDR-volume ordering.Fix α∈(0,1) . Since P(r)≥ P′(r) for
every r≥0 , the profile P reaches the level 1−α no later than P ′. Using the generalized inverse representation
from Step 1,
Vα(p) = inf{r:P(r)≥1−α} ≤inf{r:P ′(r)≥1−α}=V α(p′).
This proves (a).
If p∼p ′, then p↓ =p ′↓, hence P=P ′ and Vα(p) =V α(p′) for every α. Conversely, if Vα(p) =V α(p′) for
every α∈(0,1) , then the generalized inverse profiles agree on (0,1) , so P=P ′ on the relevant range. Hence
p↓ =p ′↓ almost everywhere, which is equivalent top∼p ′.
Step 4: Integrated volume.Integrating the pointwise inequality from Step 3 gives
IV(p) =
Z 1
0
Vα(p)dα≤
Z 1
0
Vα(p′)dα=IV(p ′).
This proves (b).
If p∼p ′, then Vα(p) =V α(p′) for every α, so IV(p) =IV(p ′). Conversely, suppose IV(p) =IV(p ′).
Since Vα(p)≤V α(p′) for every α, the non-negative function Vα(p′)−V α(p) integrates to zero over (0,1) .
Hence Vα(p) =V α(p′) for almost every α. By right-continuity of α7→V α(p) and α7→V α(p′), equality
extends to everyα∈(0,1). By the equality statement in Step 3,p∼p ′.
With this lemma established, we return to our axiomatic assessment. We reprint our table of QUEST measures
above for reference.
A0: T U, AUand EU should be non-negative.Non-negativity is immediate from the QUEST definitions, as
volume and divergence are always bounded below by0.
A1: For all Q∈ Q(Θ), EU(q)≥EU(δθ) = 0.A Dirac mass has zero volume, and so EU(δ θ) = 0 on both
local and global measures. The inequality follows from the non-negativity ofEUin general (A0).
A2: If qℓ, q, qu satisfy qℓ ⪯q⪯q u, then EU(q ℓ)≤EU(q)≤EU(q u).This follows from the partial ordering
lemma, withEUmeasured byV α(q)(local) andIV(q)(global).
A3: If pℓ, p, pu satisfy pℓ ⪯p⪯p u, then AU(p ℓ)≤AU(p)≤AU(p u).This follows from the partial
ordering lemma, withAUmeasured byV α(pθ∗ )(local) andIV(p θ∗ )(global).
A4: If Q′ is a mean-preserving spread of Q, then EU(q)≤EU(q ′) (weak) or EU(q)< EU(q ′) (strict); the
same holds for T U.For global EU , both inequalities follow immediately from the partial ordering lemma and
Defn 5.3, with strict inequality iff q≺q ′. For local EU , only the weak inequality is satisfied, since levelling
may occur strictly below the (1−α) -HDR threshold and therefore imply no reduction in Vα(q). For T U, we
construct a simple counterexample. Suppose that pθ∗ is standard normal, with q consisting of a Dirac mass at
ˆµ= 1,ˆσ= 0. In this case, T Uis infinite, as true parameter values are assigned zero density by the second-order
distribution. A mean-preserving spread of q that expands this distribution to include µ∗ = 0, σ∗ = 1 in its
(1−α) -HDR will reduce the f-divergence between p∗ α and ˆpα, resulting in lower T U. More generally, any
levelling ofqthat improves calibration at levelαwill reduce the inflation factorg f

Df (p∗ α ||ˆpα)  .
A5: If Q′ is a spread-preserving location shift of Q, then EU(q) =EU(q ′).This follows from the partial
ordering lemma and the antisymmetry property of partial orders.
19

B Additional Experimental Details
This appendix provides extended details for the selective prediction evaluation.
Selective prediction evaluates whether uncertainty measuresrankpredictions by reliability. Given uncertainty
scores u(x) on a fixed test set, we sort test points byu(x) and retain a subset Sr at retention proportion r∈[0,1]
(i.e., the least uncertainrfraction). Loss at retentionris
L(r) = 1 |Sr| X (x,y)∈Sr ℓ(ˆy(x), y),(2)
for a suitable loss ℓ(·,·) , where ˆy(x)is the prediction of the model for x. We report loss–retention curves (see
below for definition of loss).Each experimental configuration is repeated 20 times. Seeds are set such that the
results are reproducible.
B.1 Data
We construct three datasets targeting distinct behaviours of uncertainty measures. 1500 data points are sampled,
and split randomly such that ntrain = 1000 and ntest = 500 . For each MoE model, the training data is
bootstrap sampled to increase ensemble diversity. The resulting training sample is of size ntrain. The equations
governing the data generating processes are outlined below
Unimodal GaussianWe generate unimodal Gaussian conditionals to test that QUEST does not degrade
performance in settings where variance and differential entropy are appropriate proxies for uncertainty in a
density concentration/modal perspective.Expected outcome:variance, entropy, and QUEST exhibit similar
ranking quality and downstream performance.
Y|x∼ N(µ(x), σ2 G(x))
σG(x) =
p
s2 +δ 2(x), s= 0.2, δ(x) = 0.5 +|x|
µ(x) = sin(πx), X∼Uniform[−2,2]
Unimodal skewedWe generate unimodal conditionals with marked skewness. The aim is to create regions
where dispersion-based measures are dominated by tail mass rather than local density concentration.Expected
outcome:variance and differential entropy can mis-rank uncertainty due to tail sensitivity, whereas QUEST
improves ranking by focusing on concentration near dominant high-density regions.
Y|x=µ(x) +σ(x)·Z, Z∼SkewNormal(α(x))
σ(x) = 0.3 + 0.2|x|, α(x) = 5·sign(x)
p
|x|
µ(x) = sin(πx), X∼Uniform[−2,2]
noteZis a standardised SkewNormal distribution, with mean 0 and variance 1.
Multimodal mixtureWe generate input-dependent two-component Gaussian mixtures: Because the density
is known, conditional modes and ground-truth uncertainty-related quantities can be computed exactly (or to
arbitrary numerical precision).Expected outcome:variance and differential entropy can mis-rank uncertainty
due to bi-modal nature of the data erroneously inflating these measures, whereas QUEST improves ranking by
correctly focusing on concentration near local modes.
Y|x∼ 1 2 N(µ(x)−δ(x), s 2) + 1 2 N(µ(x) +δ(x), s2)
s= 0.2, δ(x) = 0.5 +|x|
µ(x) = sin(πx), X∼Uniform[−2,2]
B.2 Ensemble of mixture of experts
For our model we utilise an ensemble ofM= 10 independently trained mixture of expert models. The predictive
distribution is given by:
p(y|x) = 1 M
MX
m=1
p(m)(y|x),
where each membermis a mixture ofK= 3unimodal Gaussian experts:
p(m)(y|x) =
KX
k=1
g(m) k (x)N  y|µ (m) k (x),(σ (m) k (x))2 .
20

Table 3: Mixture-of-Experts hyperparameters for the cgmm-based MoE implementation. Bold entries
indicate values that are differ fromcgmmdefaults.
Parameter Value Explanation
n_components3 Number of experts per MoE member
covariance_type fullCovariance structure for each expert
shared_covariance FalseWhether experts share a covariance matrix
mean_function affineExpert mean-function class
reg_covar10 −4 Covariance regularization for numerical stability
gating_penalty10 −2 L2 penalty on gating weights
gating_max_iter50 Maximum optimization iterations for gating updates
gating_penalty_bias NoneOptional bias penalty term
gating_tol10 −6 Gating convergence tolerance
gating_init_scale0.1 Initial scale for gating parameters
max_iter200 Maximum EM iterations
tol10 −4 EM convergence tolerance
n_init1 Number of random initializations
init_params kmeansInitialization method
Hereg (m) k (x)are softmax gating weights:
g(m) k (x) = exp(a(m) k (x)) PK
j=1 exp(a(m) j (x)) .
a(m) k (x) denotes the unnormalized gating score for expert k in ensemble member m, and the corresponding
mixture weight is obtained by a softmax transformation, where the score is defined as:
a(m) k (x) = logα (m) k + logN  y|µ (m) k (x),(σ (m) k (x))2 .
where α(m) k ≥0 are mixture weights of the experts, learnt via the EM algorithm with k-means initialisation.
Note
KX
k=1
α(m) k = 1.
Each modelmis trained independently via the EM agorithm, maximising log loss over the parameter space:
L(m) =
NX
n=1
logp (m)(yn |x n).
We utilise the MoE implementation from the packagecgmm(see section B.6), and create an ensemble of these
within our code. EachcgmmMoE is trained with hyper-parameters outlined in table 3.
B.3 Uncertainty Measures
Computation of uncertainty measures utilises empirical density samples, with grid based approximations when
no closed form analytic solution exists (e.g. for obtaining highest density regions). We state the measures as
utilised in our computations in table 4. Note we use the Oracle perspective in the selective prediction experiment.
Entries with p∗ do not require this to be approximated as would usually happen in settings without access to the
true density. For the calculation of α volume and integrated volume we require the computation of the highest
Table 4: Uncertainty measures as computed for our experiments
TU AU EU
VarianceAU+EUVar(p ∗) (E[p ∗]−E[ˆp])2
Differential EntropyAU+EUh(p ∗)KL(p ∗||ˆp)
QUEST-localV α(p∗)/  1−d T V(p∗ α,ˆpα)  Vα(p∗)V α(q)
QUEST-global
R
α∈[0,1] Vα(p∗)/  1−d T V(p∗ α,ˆpα)  dα R α Vα(p∗)dα R α Vα(q)dα
21

Normal Skewed Bimodal
0.25 0.50 0.75 1.00 0.25 0.50 0.75 1.00 0.25 0.50 0.75 1.00
0.02
0.03
0.04
0.05
0.02
0.03
0.04
0.05
0.01
0.02
0.03
0.04
0.05
0.06
Proportion retained
Selective loss
Variance TU Entropy TU QUEST TU (α=0.1) QUEST TU (global) Random
Figure 4: Selective learning curves for deep MoE ensembles on three different DGPs. Shading
represents standard errors across 20 trials. Instead of the obtaining the oracle density, the model takes
the maximum likelihood estimator from among the M= 10 ensemble members and uses this as a
plug-in estimate ofp ∗.
density region of densities p∈P or q∈ Q, 1st and 2nd order distributions respectively. We compute the HDR
via a grid approximation6, the pseudo-code for which is outlined in algorithm 1.
Algorithm 1Grid-based approximation of Highest Density Region (HDR) at levelα
Require:Density functionp(y|x)(orq(θ|x)), gridG={y i}N i=1 (or{θ i}N i=1 7), levelα∈(0,1)
Ensure:Approximate HDR set bCα
1:Let∆Vdenote the grid cell volume
2:Evaluate densities:d i ←p(y i|x)for ally i ∈ G
3:Sort grid points in descending order of density:d (1) ≥d (2) ≥ · · · ≥d(N)
4:Initialise cumulative mass:M←0
5:Initialise set: bCα ← ∅
6:fori= 1toNdo
7:Add point: bCα ← bCα ∪ {y(i)}
8:Update mass:M←M+d (i) ·∆V
9:ifM≥1−αthen
10:break
11:end if
12:end for
13:return bCα
B.4 Additional results: Without Oracle
Fig. 4 shows the sensitivity of QUEST TU measures to knowledge of p∗. The advantage seen in Fig. 3 is
reversed, with local QUEST performing comparably to competitors while the former frontrunner, global QUEST,
lags behind in unimodal settings (although it retains a slight advantage in bimodal settings). This suggests both
that QUEST TU is sensitive to the quality of the model’s estimate of p∗, and that the properties which make
QUEST suited to bimodal data offset some of this sensitivity in settings to which the measure is well suited. The
interaction between DGP and inferential choices for approximatingp ∗ is an important area for further study.
B.5 Compute requirements
Experiments utilised 20 CPU cores on a high performance computer running for a maximum of 24 hours.
Maximum memory use was 100GB per repeat. Disk storage requirements were approximately 20GB. No
substantial additional compute requirements were need, e.g. for preliminary/failed experiments.
6Note the grid approximation does not suffer a curse of dimensionality issue as we always have 1D first order conditional
distributions, and our models are such that we have a 2D second order conditional distribution (i.e. we have two model
parameters). For models providing more dimensions techniques such as Monte Carlo sampling make the procedure feasible,
but this is outside of the scope of this paper.
7We now drop the equivalence with θ. Simply substitute y for θ in what follows to obtain the algorithm for an HDR of a
2nd order distribution.
22

B.6 Language and code assets
We make the experimental code publicly available herehttps://github.com/sjgoring/modal-uq-public .
It is written in Python, and we gratefully acknowledge here the use of the following libraries: numpy [18], scipy
[52], joblib [link], matplotlib [23], scikit-learn [40], torch [39], cgmm [link].
C Supplementary experiment
We now provide details of, and results from, a supplementary active learning experiment.
C.1 Active learning
We use a pool-based procedure with labelled setD L and unlabeled poolD U . At each acquisition round:
1. Train the model onD L.
2. Compute acquisition scoresa(x)onx∈ D U using a chosen uncertainty measure.
3. Select the top-kpoints bya(x)and add them (with labels) toD L.
Performance is tracked on a fixed test set after each acquisition round. Unless otherwise stated: initial labelled
size= 200, batch sizek= 200, and number of rounds= 200, giving a final pool size|D L|= 1200.
As with the selective prediction experiment we repeat each experiment 20 times, averaging the reported loss
over each of the repeats and reporting standard errors via the shaded regions of the graphs.
C.2 Data
We utilise the three synthetic data sets from the selective prediction experiment, and introduce one new data
set—theMulti-Particle Environement. We provide an extended description of the modified simple_adversary
environment. The base environment from PettingZoo’s MPE suite [50] is a 2D continuous-control setting in
which agents move according to second-order motion dynamics with collisions enabled. The agents have a
discrete action space which corresponds to applying a fixed force in a particular cardinal direction, as well as a
no-opaction.
The environment contains onegood(ego) agent, one or more stationary adversaries acting as obstacles, and
a single goal landmark. At reset, the goal is placed within a bounded square region, the ego is placed in an
opposing region with a minimum separation from the goal, and obstacles staggered perpendicularly along ⃗ τopt.
This constructive placement guarantees that the optimal trajectory is geometrically obstructed, requiring the
good agent to deviate and resulting in multimodal behaviour suitable for our test cases. An example is shown in
Fig. 5.
The ego is trained with a Deep Q Network (DQN) [36] policy under a shaped reward which combines a dense
goal-seeking term −∥pego −p goal∥, a quadratic soft-hinge avoidance term −w·max(0, R−d) 2/R where d is
the distance to the nearest adversary and R a safety radius, and a goal-reaching bonus when the ego enters a
small ball around the goal. The weights are tuned so that the agent prefers both detours rather than collisions
and goal-seeking rather than being overly cautious.
For each of n_states initial world configurations, we run n_traj independent rollouts under fixed ϵ-greedy
execution. The input x is the world state including positions and velocities of all entities, flattened. The target
y is computed by projecting the ego position at every timestep onto the perpendicular of ⃗ τopt, identifying the
timestep of maximum absolute deviation, and recording the signed value at that point (left being negative, right
being positive). Variance across rollouts from each initial state comes from ϵ-greedy stochasticity acting on
a symmetric layout: when the obstacle lies close to ⃗ τopt, left and right detours have similar expected return,
and small early perturbations push the policy onto one branch. The resulting per-state distribution p(y|x) is
approximately multimodal.
C.3 Model and uncertainty Measures
We utilise the ensemble mixture of experts model as outlined in section B.2, and utilise the epistemic uncertainty
variants of the measure families outlined in Table 4.
23

Figure 5: Example MPE initial world configuration with sample trajectories, optimal trajectory and
maximum lateral displacement shown.
C.4 Evaluation metric
We evaluate model performance using average absolute distance between the predicted and true mode over
points in the test setx test, that is:
L(ˆy|x) =
X
x∈xtest
1
|xtest| |(y∗|x)−(ˆy|x)|
where as in Section B y∗ = arg maxy, p∗(y|x),ˆy= arg max y,ˆp(y|x) , and p∗ is the true density and ˆpthe
learnt density. See Sections B.5 and B.6 for compute requirements and code assets.
C.5 Results and interpretation
Fig. 6 shows QUEST performance inline with competitor measures on these 4 data sets. As in the selective
prediction experiment, the Oracle density is utilised. This ensures the best possible uncertainty measurement
(w.r.t faithfulness to the true value) for both the variance and differential entropy measures of EU. The Oracle
is of no use to QUEST–which we might think would put it at a disadvantage–the measure of 2nd order HDR
volume is wholly subjective. Yet despite this, both QUEST measures hold their own and perform equally well
whilst their competitors are maximally boosted by the presence of the Oracle. A line of further enquiry is to see
the effect of various inferential choices (see Schweighofer et al. [47], Fishkov et al. [12]) required to estimate
the Oracle distribution on the performance of variance/entropy. We suspect this might be where QUEST begins
to exhibit superior relative performance.
D Admissible measures ofT U
While total variation distance offers a particularly transparent choice—bounded by 1 and easily interpreted
as the maximum probability disagreement on any event—several other f-divergences satisfy the admissibility
conditions of Section 4 and yield equally validT Uconstructions. We sketch three alternatives here.
Thesquared Hellinger distanceuses f(t) = (
√
t−1) 2, with f(0) = 1 and f ′(∞) = 1 , both finite. The
resulting divergenceH 2(p, q) = R (√p− √q)2 dxis bounded above byM f = 2, with the maximum attained
for distributions with disjoint support. The natural penalty function isg f (D) = 1/(1−D/2), giving:
TUH :=V α(pθ∗ )· 1 1−H 2(p∗α,ˆpα)/2 .
24

0 1 2 3 4 5
Round
0.335
0.340
0.345
0.350
0.355
0.360Mean absolute error
mpe  (D_init=200, rounds=5, seeds=20)
ent_eu
quest_eu_01
quest_eu_g
random
var_eu
Mode absolute error
0 1 2 3 4 5
Round
1.20
1.25
1.30
1.35
1.40
1.45
1.50
1.55Mean absolute error
gaussian  (D_init=200, rounds=5, seeds=20)
ent_eu
quest_eu_01
quest_eu_g
random
var_eu
Mode absolute error
0 1 2 3 4 5
Round
0.10
0.12
0.14
0.16
0.18
0.20
0.22
0.24Mean absolute error
mpe  (D_init=200, rounds=5, seeds=20)
ent_eu
quest_eu_01
quest_eu_g
random
var_eu
0 1 2 3 4 5
Round
0.425
0.430
0.435
0.440
0.445
0.450
0.455
0.460Mean absolute error
skewed  (D_init=200, rounds=5, seeds=20)
Mode absolute error
0 1 2 3 4 5
Round
0.10
0.12
0.14
0.16
0.18
0.20
0.22
0.24Mean absolute error
mpe  (D_init=200, rounds=5, seeds=20)
ent_eu
quest_eu_01
quest_eu_g
random
var_eu
0 1 2 3 4 5
Round
1.55
1.56
1.57
1.58
1.59
1.60Mean absolute error
bimodal  (D_init=200, rounds=5, seeds=20)
Mode absolute error
Figure 6: Active learning experiment with ensemble MoE model across four datasets. Pool labelling
conducted by EU measures from the variance, entropy, QUEST-local and QUEST-global families.
All measures are compared to a random baseline.
TheJensen-Shannon divergenceis a symmetrized version of KL: JSD(p, q) =1 2 DKL(p∥m) + 1 2 DKL(q∥m)
where m= (p+q)/2 . It corresponds to f(t) = 1 2 [tlogt−(t+ 1) log t+1 2 ], with f(0) =f ′(∞) = log 2/2, givingM f = log 2. The penaltyg f (D) = 1/(1−D/log 2)yields:
TUJS :=V α(pθ∗ )· 1 1−JSD(p ∗α,ˆpα)/log 2 .
Thetriangular discrimination(aka Le Cam distance) uses f(t) = (t−1) 2/(t+ 1) , with f(0) = 1 and
f ′(∞) = 1, givingM f = 2. The penaltyg f (D) = 1/(1−D/2)yields:
TU∆ :=V α(pθ∗ )· 1 1−∆(p ∗α,ˆpα)/2 ,
where∆(p, q) =
R
(p−q) 2/(p+q)dx.
In practice, the choice between these constructions reflects a modeling decision about which kind of calibration
error is most important to detect. We default to the TVD-based measure in the main text for its interpretive
simplicity and its historical primacy in statistical distance literatures.
E Further remarks on levelling
Levelling represents a principled and general concept of spread with several notable advantages. First, it applies to
distributions of bounded or unbounded support, as well as distribution pairs with identical or distinct (potentially
even disjoint) support. Second, it preserves the intuition that a Dirac mass and the uniform distribution represent
natural limits. To see this, observe that levelling can never produce a Dirac mass, whereas for fixed support X , a
uniform p is maximally levelled. (Both properties follow from L1.(c).) Finally, because levelling does not rely
on a distribution’s moments, it is well-defined even for densities with infinite variance, such as the Cauchy.
To see this, consider the examples in Fig. 2(A), which differ only in their scale parameter γ. Levelling captures
the intuitive ordering of these densities by their concentration. For any pairpγ and pγ′ with γ < γ′, condition L1
25

0
1
2
3
4
5
0.00 0.25 0.50 0.75 1.00
x
Density
Beta(0.5, 0.5)
Beta(2, 2)
(A)
0
1
2
3
4
5
0.00 0.25 0.50 0.75 1.00
Cumulative volume
Density (sorted)
(B)
0.00
0.25
0.50
0.75
1.00
0.00 0.25 0.50 0.75 1.00
alpha
alpha−volume
(C)
Figure 7: Beta(0.5,0.5) and Beta(2,2) are incomparable w.r.t. levelling.(A)Density curves for
both distributions.(B)Decreasing rearrangements cross.(C)Coverage curves therefore cross as well.
holds with A the central region where pγ exceeds pγ′, and B the tails where the relationship reverses. The two
densities cross at the unique points where their values coincide; on A, pγ’s mass is excess relative to pγ′, and
this mass is exactly redistributed to the tails B in pγ′, satisfying L1’s mass-conservation and level-set conditions.
Variance fails to make these comparisons because it is undefined for all three densities, while levelling correctly
identifies the orderingp 1/2 ≺p 1 ≺p 2.
We remark that levelling imposes apartialorder on distributions, as there exist some pdf pairs such that neither
is a levelling of the other. This occurs when their decreasing rearrangements (and therefore coverage curves)
cross, as in the case of Beta(0.5,0.5) and Beta(2,2) (see Fig. 7). This means that levelling is notstrictlymore
general than variance, as there are cases (such as this one) where variance gives a partial order while levelling
abstains. In particular, we have Var

Beta(2,2)

<Var

Beta(0.5,0.5)

. Note that these distributions are still
comparable w.r.t. local QUEST measures at anyfixed α—the incomparability arises because our ordering flips
as α varies (see Fig. 7(C)). As for the global measure, we have IV(Beta(1/2,1/2)) = 1−2/π≈0.363 and
IV(Beta(2,2)) = 0.375. ThusIVand variance give opposing results in this case.
Perhaps more interestingly, we can construct examples wherelevellingand variance render contradictory verdicts.
This occurs, for instance, whenp is a bimodal distribution with sharp peaks spaced far apart, whilep′ redistributes
mass from those peaks to the centre, subject to L1 constraints. This will tend toreducevariance, despite the
fact that p≺p ′. Appealing to the intuition that “spread” should track “distance-to-uniformity”, we argue that
variance renders the wrong judgment in this case.
F Further remarks on uncertainty axioms
Alternative axiomsAlthough our axiom A1 accords with that of Wimmer et al. [56] and Sale et al. [44],
QUEST measures do not satisfy a stronger version proposed by Bülte et al. [5]:
A1∗:EU(q) = 0iffq=δ θ.
Specifically, we respect the reverse but not the forward direction of this biconditional. The latter fails, for
instance, on Dirac mixtures or joint distributions with support on a submanifold. These are cases of measure
zero sets that do not correspond to any single Dirac mass. We can generalize the point by proposing our own
modified biconditional:
A1′:EU(q) = 0iffλ  supp(q)  = 0,
which QUEST measures do satisfy. (Entropy and variance, however, do not.) While A1′ may be a reasonable
axiom to adopt, we do not develop the point any further here.
Another proposed axiom is due to Sale et al. [44]:
A6: For allp, q, (i)AU(p)≤T U(p, q)and (ii)EU(q)≤T U(p, q).
QUEST measures satisfy A6.(i) but not A6.(ii), since a flat second-order distribution may result in a well-
calibrated predictor. However, the inequality is arguably nonsensical in our setting, since the k-dimensional
Lebesgue measure on the lhs is not obviously comparable to the d-dimensional Lebesgue measure on the right.
Thus this axiom is inappropriate for our framework.
Should EU be purely subjective?Given that T Udecreases as model calibration improves—an undisputed
premise, as far as we are aware—all UQ methods face a choice. Either (1) decide that T Uis fully determined
by AU and EU , in which case the latter is necessarily truth-relative; or (2) embrace a subjective notion of
EU , at the cost of complicating the classical uncertainty typology. We argue that (1) conflates calibration
and confidence. Agents who are confidently miscalibrated and confidently well-calibrated experience similar
26

subjective uncertainty (e.g., agents A, Bwith qA =δ θ, qB =δ θ∗ for some θ̸=θ ∗). UQ frameworks that
choose (1) over (2) have no way of properly diagnosing such cases.
A plausible objection runs as follows. Whatever the functional form of T U, it should surely be monotone in EU .
Since AU is fixed by the DGP, this means thatEU should track some notion of error or miscalibration. On a
purely subjective measure, an irrational agent may fail to update q properly given evidence, leading to decreased
EUbut increasedT U. This is nonsensical. Call thisthe monotonicity objection.
The monotonicity objection implicitly assumes something like the additive decomposition of T U, which holds
for variance- and entropy-based measures. Whatever the merits of this view—which has been challenged by
recent works [34, 56]—it should not be assumed upfront, but rather derived from first principles. To do otherwise
when attempting to formalize UQ would be to beg the question. Interestingly, our framework accords with the
intuition of the monotonicity objection when θ∗ ∈Θ and the agent has a consistent learning procedure. In
this setting, q will tend to concentrate around true parameter values as data accumulates, ensuring a monotone
relationship between epistemic and total uncertainty. We point out that model misspecification and/or irrational
belief updates are genuine problems, but hardly unique to our framework—these would cause headaches for any
effort to model uncertainty.
So the objection loses force when a single agent learns over time. But what about a comparison between two
separate agents, one of whom is more confident in their predictions than the other? On QUEST measures, the
more confident agent by definition has lower EU , even if their predictions are wildly miscalibrated. We argue
that this is exactly what a good uncertainty measure should do, otherwise we have no language for disambiguating
what is the same and what is different between agents who are equally sure of their models, despite vastly
different empirical performance. We locate the similarity in EU and the difference in T U, which directly
rewards the better calibrated model. The trade-off is that we lose the monotonicity property in general—not in
the case of a single consistent learner, but possibly when comparing multiple models. This is why T Ufails to
satisfyA4.
As a final comment, we anticipate a question as to why we define EU in terms of q rather than the posterior
predictive ˆp. The answer is simple. We may be confident that σ is very large (low subjective uncertainty, high
Vα(ˆp)) or very uncertain about µ but with fixed small σ (high subjective uncertainty, low Vα(ˆp)). The true focus
of a subjective uncertainty measure is therefore the second-order distributionq, not the posterior predictive.
27
