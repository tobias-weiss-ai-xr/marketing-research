---
title: 'RECAST: Model Reconstruction via Counterfactual-Aware Wasserstein Geometry under Limited Data'
url: https://arxiv.org/abs/2606.27948
category: ai-marketing
subcategory: measurement
date: 2026-06
venue: ''
authors:
- Xuan Zhao
- Lena Krieger
- Zhuo Cao
- Arya Bangun
- Hanno Scharr
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.27948
pages: 25
chars: 95654
fetched_at: '2026-11-08T13:28:01+00:00'
kb_version: 1
---

# RECAST: Model Reconstruction via Counterfactual-Aware Wasserstein Geometry under Limited Data

RECAST: Model Reconstruction via
Counterfactual-Aware Wasserstein Geometry under Limited Data
Xuan Zhao * 1 Lena Krieger * 1 2 Zhuo Cao 1 Arya Bangun 1 Hanno Scharr 1 Ira Assent 1 3
Abstract
Counterfactual explanations (CFs) help under-
stand machine learning models by identifying
minimal input changes that would lead to alterna-
tive model outcomes. Recent work demonstrates
their utility for reconstructing black-box models,
enabling third-party auditing of opaque decision
systems for fairness and accountability. Still, CF-
based reconstruction may suffer from decision
boundary shifts, overfitting, and restrictive as-
sumptions requiring online query access to tar-
get platforms. We proposeREconstruction via
Counterfactual-Aware waSserstein opTimiza-
tion (RECAST)under limited data and restricted
access, a behavioral surrogate model based on
Wasserstein barycentric prototypes. Our approach
addresses decision boundary shifts by incorporat-
ing CFs as informative, though less representa-
tive, samples for both classes, maintaining high
surrogate fidelity in low-sample regimes without
requiring online access during reconstruction. To
enhance fairness auditing, our method enables sys-
tematic group fairness diagnostics. Experiments
on real-world datasets and various setups show
thatRECASTeffectively achieves high fidelity
and query efficiency, as well as stable results even
when the access is limited and noisy.
1. Introduction
Machine-Learning-as-a-Service (MLaaS) platforms have
democratized access to AI systems in high-stakes decision-
making systems. Such systems can be audited by reconstruc-
tion, i.e., creation of a surrogate model to closely mimic the
*Equal contribution 1IAS-8, Forschungszentrum J¨ulich, Ger-
many 2LMU Munich, Munich Center for Machine Learn-
ing (MCML), Germany 3Department of Computer Science,
Aarhus University, Denmark. Correspondence to: Xuan
Zhao <xu.zhao@fz-juelich.de>, Lena Krieger <l.krieger@fz-
juelich.de>.
Proceedings of the 43 rd International Conference on Machine
Learning, Seoul, South Korea. PMLR 306, 2026. Copyright 2026
by the author(s).
0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5
f1
0
1
2
3
4f2
Class 0 Class 1 CF
Figure 1.CFs (x) are generated for class 0 (blue) samples - minimal
changes that flip the target’s prediction from class 0 → class 1
(pink). Naively treating these as class 1 training samples shifts the
surrogate’s boundary (solid line) toward class 0, causing class 0
samples to be misclassified as class 1. This isoverconfidence: the
surrogate becomes overly certain about class 1 in regions where
the target (dashed line) is not. We instead treat CFs asless certain
samples, giving them less influence than true class 1 samples.
behaviour of the target model, enabling independent investi-
gation of model behavior, including transparency, account-
ability, and fairness concerns such as fairwashing (A¨ıvodji
et al., 2021). Reconstruction under limited access is funda-
mentally a problem of stability: conclusions about model
behavior should remain invariant across all models that
are behaviorally indistinguishable from the observed data.
While studied as model extraction attacks (MEA) (Tram`er
et al., 2016; Gong et al., 2020; Carlini et al., 2024; Ferry
et al., 2024) in adversarial contexts, reconstruction is cru-
cial to understand model behaviour in high-stakes decision-
making systems as required by the EU AI Act1. In addition
to transparency and accountability, the AI Act also aims to
improve diversity and fairness. One way to achieve this is
through model reconstruction, by examining how sensitive
groups are distributed relative to the learned decision ge-
ometry. Recent work leverages counterfactual explanations
(CFs), i.e., minimally modified instances that attain a de-
sired prediction, for model reconstruction (A ¨ıvodji et al.,
2020; Wang et al., 2022; Dissanayake & Dutta, 2024). This
line of work features two main advantages: CFs naturally
encode boundary-adjacent information, and improve query
efficiency by providing pairs of closely related instances
with contrasting predictions.
1artificialintelligenceact.eu/chapter/3
1
arXiv:2606.27948v1  [cs.LG]  26 Jun 2026

RECAST: Model Reconstruction via Counterfactual-Aware Wasserstein Geometry under Limited Data
However, existing CF-based reconstruction approaches face
critical limitations. First, decision boundary shifts occur,
when surrogate models trained on CFs as full class samples
(A¨ıvodji et al., 2020) become overconfident in regions where
the CFs are located. Then, the learned decision boundary
is shifted incorrectly (Fig. 1), due to margin-based gener-
alization (Shokri et al., 2021), and worsens with one-sided
CFs. Two-sided CFs could mitigate this (Wang et al., 2022),
but typically platforms do not provide them: rejected loan
applicants receive explanations on how to achieve approval,
but approved applicants do not learn how their application
might have been denied (A¨ıvodji et al., 2020; Dissanayake
& Dutta, 2024). Second, neural network-based methods
such as Counterfactual Clamping Attacks (Dissanayake &
Dutta, 2024), are prone to overfitting when limited training
data is available. As data is usually costly in this setting,
constrained by strict query budgets to limit API costs and
rate limits, data efficiency is critical. Third, under low-
query and one-sided CF settings, decision boundaries are
statistically non-identifiable, rendering recovery or approxi-
mation of decision boundaries (Dissanayake & Dutta, 2024;
Khouna et al., 2025) inapplicable: multiple classifiers may
exhibit indistinguishable input–output behavior while hav-
ing substantially different decision surfaces. Also, data is
potentially noisy, as MLaaS platforms may return imperfect
or perturbed outputs (Liang et al., 2024). We assume this is
a passive observation problem and do not model interactions
with a strategic platform using adversarial threat models.
For effective reconstruction of a binary classifier with
limited or noisy data, we proposeREconstruction via
Counterfactual-Aware waSserstein opTimization (RE-
CAST)which incorporates CFs assoftsamples for both
classes. We leverage Wasserstein barycenters as prototypes
for each class to capture the underlying structure of each
class distribution in a data-efficient manner, suitable for
low-data regimes and noisy samples. To detect asymmetric
treatment and decision disparities, we adapt a group fairness
diagnostic, based on the reconstructed model, that compares
how different sensitive groups (e.g., gender or race) are
positioned relative to the barycentric decision geometry.
Our main contributions include:
• OurModel REconstruction via Counterfactual Con-
strained Wasserstein Geometry (RECAST)solution
to behavioral reconstruction via counterfactual-aware
Wasserstein barycentric prototypes.
• Empirical validation of effectiveness ofRECASTin
various settings, including four datasets, different target
model classes, CF generators, and noisy data, demon-
stratinghigh fidelityandquery efficiency.
• A geometry-basedfairness diagnosticto characterize
distributional disparities across sensitive groups under
distribution shift.
Table 1.Model reconstruction using CFs. RECAST intentionally
avoids explicit boundary recovery and instead focuses on func-
tionality reconstruction, which is better posed underone-sided
CFs,offline accessandlow-query settings. ∗ paper studies only
neural networks. + requires prior knowledge about the distribution.
SAMPLES: A¨ıvodji et al. (2020).
Method One-sided CFs Model agnostic Behavior-centric Access?
DualCF✗ ✗ ✓Online
TRA✓ ✗ ✗Online
CCA✓ ✓ ✗Online
SAMPLES✓ ✓ ∗ ✓Offline +
RECAST (Ours)✓ ✓ ✓Offline
2. Related Work
Model extraction attacks (MEAs) aim to reconstruct hidden
models from queries to an MLaaS platform (Liang et al.,
2024; Zhao et al., 2025).
In our work, we focus on functionally equivalent extraction,
i.e., recovering a surrogate model whose predictions match
those of the target model (A¨ıvodji et al., 2020) underoffline
access, i.e., based on a fixed sample set constructed without
any prior knowledge.
Existing work usually requiresinteractive onlinequery ac-
cess to the target modelduringthe reconstruction process,
often not available in practice (Table 1).
Early methods focused on recovering model parameters
or explicitly approximating decision boundaries through
costly extensive querying (Pal et al., 2020; Jagielski et al.,
2020). More recent ones employ CFs, i.e., a minimally
modified instance for an input that attains the desired predic-
tion, for instance suggesting an income increase to secure
a loan otherwise rejected. A ¨ıvodji et al. (2020), here re-
ferred to as SAMPLES, use CFs asfulllabeled data. The
approach is vulnerable to decision boundary shift, i.e., it
over-confidently assesses samples that lie very close to the
decision boundary and are thereforelessrepresentative (see
Fig. 1). In practice, typically only one-sided CFs are avail-
able, to support users in understanding negative outcomes,
while avoiding information leak about the hidden model.
Recent works, particularly those leveraging CFs, often adopt
a boundary-centric perspective. They aim to infer the geom-
etry of the target classifier decision boundary, e.g., with a
modified entropy loss that treats CFs as in-between classes
(CCA (Dissanayake & Dutta, 2024)) or divide the input
space into subspaces and incorporate locally optimal CFs
(TRA (Khouna et al., 2025)).
However, the non-identifiability effect (Orekondy et al.,
2019; Tram`er et al., 2016) means that under finite samples,
different classifiers can exhibit identical or nearly identical
classification behavior while having fundamentally different
decision boundaries. Another line of work (A ¨ıvodji et al.,
2020; Wang et al., 2022) thus emphasizes behavior-centric
2

RECAST: Model Reconstruction via Counterfactual-Aware Wasserstein Geometry under Limited Data
reconstruction, to reproduce the input–output behavior of
the target model rather than its decision geometry. How-
ever, earlier approaches that include CFs, require access to
two-sided CFs, e.g., training on pairs, consisting of CFs
and CFs for CFs (DualCF (Wang et al., 2022)) or are chal-
lenged by decision boundary shifts (SAMPLES (A ¨ıvodji
et al., 2020)). We propose a behavior-centric approach, that
addresses these limitations, by reconstructing class-level be-
havior from CFs, which naturally encode boundary-adjacent
information, using Wasserstein-based prototypes.
While superficially related to classical learning under
data selection bias (Heckman, 1979; Shimodaira, 2000;
Zadrozny, 2004), the setting differs in two fundamental
aspects. First, the target decision boundary is statistically
non-identifiable under offline, one-sided CF access, whereas
classical reweighting assumes an identifiable target approxi-
mated via ERM on reweighted samples. Second, CFs may
overshoot or be systematically biased (see Figure 2), ren-
dering them unreliable as boundary samples. Margin-based
methods such as SVMs rely precisely on reliability. CFs in-
stead encode directional distributional constraints between
class-conditional distributions, which RECAST handles at
distribution level via Wasserstein surrogates rather than via
sample-level reweighting or margin maximization.
3. The RECAST Method
We start by defining the problem of model reconstruction
in low-query regime and with one-sided CF, then describe
how our new RECAST approach leverages Wasserstein op-
timization under CF-consistent uncertainty (Section 3.1) to
learn class conditional prototypes (Section 3.2), which we
employ in a barycentric prototype classifier (Section 3.3).
Finally, we adapt a threshold invariant fairness diagnostic to
a Wasserstein geometry perspective (Section 3.4).
Problem Setting.We study reconstruction of a binary
black-box classifier m:X→ {0,1} , with predictions
m(x) =I[ˆym(x)≥0.5] , where ˆym are (unobserved) pre-
diction scores. Information sources are restricted to:
Offline collection of labeled inputs. We are provided with
a set of labeled inputs {(x, m(x))}, that can be grouped
by class into Dc :={x:m(x) =c} for c∈ {0,1}. Our
access is restricted tooffline, i.e., no access to the target
classifierduringreconstruction.
One-sided CFs. Additionally, we receive a set of
reject-to-accept, i.e., one-sided, CFs Dcf :={x cf },
corresponding to inputs x such that m(x) = 0
and ˆym(xcf )≥0.5 . One-sided CFs are xcf ∈
argminx′∈X cost(x,x ′)s.t.ˆy m(x′)≥0.5, where
cost(x,x ′) is a user-specified cost measuring the magnitude
of the input change, for inputs x with prediction m(x) = 0.
Our goal is to reconstruct a surrogate model ˆmthat is con-
sistent with the information provided by these limited ob-
servations, i.e., toreducedisagreement ratePrunderµ:
Pr
x∼µ

m(x)̸= ˆm(x)

.
Observation(Non-identifiability). In binary classification
with one-sided CF access and limited queries, multiple data-
generating distributions can induce identical observable
data while differing in their decision boundaries, render-
ing boundary recovery statistically ill-posed.Given this
non-identifiability, reconstruction quality can only be as-
sessed in terms of behavioral agreement with the target
model, rather than recovery of a unique decision boundary.
Such non-identifiability is well known in classical black-
box model reconstruction under finite queries (Tram`er et al.,
2016; Orekondy et al., 2019). CFs provide richer informa-
tion than label queries, but a related ambiguity persists under
one-sided CF access, as they do not uniquely constrain the
underlying decision surface.
Accordingly, we reconstruct distributional class-level behav-
ior: we aim to reduce disagreement between target model
and reconstructed model rather than decision boundaries,
and model this behavior through a CF-consistent distribu-
tional geometry over probability measures.
Although CFs are defined at the individual level, their im-
pact on model reconstruction is inherently distributional, as
they constrain the admissible perturbations between class-
conditional data distributions. This naturally motivates a
Wasserstein-geometricview that measures distributional dif-
ferences via minimal-cost transport, rather than parametric
or pointwise prototype constructions. Prior work has lever-
aged optimal transport to model counterfactual distributions
in a similar distributional setting (You et al., 2025). How-
ever, such approaches focus on generating or characterizing
CFs themselves, whereas our objective is fundamentally dif-
ferent: we use CFs as structural constraints for reconstruct-
ing class-level decision behavior, which uses a Wasserstein
geometry over class-conditional measures.
Recent CF-based reconstruction methods (Dissanayake &
Dutta, 2024; Khouna et al., 2025) assume that CFs lie near
the decision boundary. In practice, however, constraints
such as immutable features often force CFs to overshoot
the boundary, as illustrated in Figure 2. Since the location
of CFs relative to the decision boundary is unknown, they
cannot be reliably treated as boundary points. Moreover,
when a CF lies on the boundary, assigning it a hard label in-
duces bias (Figure 1). RECAST therefore treats CFs as soft,
cross-class constraints, which is less sensitive to the location
of the CFs relative to the boundary. Since prototypes aggre-
gate distributional information across all available samples,
they average out sample-level noise while preserving the
3

RECAST: Model Reconstruction via Counterfactual-Aware Wasserstein Geometry under Limited Data
Figure 2.Kernel density estimates of target model scores ˆym(x) for both class inputs, CFs; common CF methods. Concentration well
above decision threshold 0.5 means CFs overshoot the boundary, confirming RECAST’s approach of avoiding near-boundary assumptions.
structure relevant to the target’s decisions. This aggregation
effectively increases the usable signal per query, mitigating
overfitting in low-query regimes.
3.1. CF-consistent Uncertainty
Definition 3.1(CF-consistent feasible set).Let Pc be the
empirical class-conditional distributions and Pcf theone-
sidedCF distribution. For each classc∈ {0,1}, we define
Cc =
n
µ∈P 2(X) :W 2(µ,P c)≤ε c, W2(µ,P cf )≤δ c
o
,
as theCF-consistent feasible set, where P2(X) denotes
the set of probability measures on X with finite sec-
ond moments, and W2 denotes the 2-Wasserstein distance
(App. A.1). Radii εc and δc encode the uncertainty induced
by finite samples, noisy queries, and imperfect CF genera-
tion; chosen appropriately, feasible sets Cc are non-empty.
The resulting uncertainty set over joint distributions is
U=

µ:µ(· |y=c)∈C c, c∈ {0,1}

.
This construction induces a lens-shaped ambiguity set in
Wasserstein space (Figure 3). Distributionally Wasserstein
robust optimization (WRO) under Wasserstein ambiguity
sets is the minimization of the worst case expected loss
over all distributions within a Wasserstein ball around an
empirical distribution (Mohajerin Esfahani & Kuhn, 2018;
Blanchet et al., 2019; Gao & Kleywegt, 2023).
Relation to Wasserstein robustness.Classical
Wasserstein-robust optimization (WRO) optimizes
over a single Wasserstein ball centered at an empirical distri-
bution, with radius that can be statistically calibrated from
data. In our setting, however, the ambiguity radii cannot be
reliably calibrated from limited one-sided CF data. Thus,
our CF-consistent feasible set is theintersection of two
Wasserstein balls: one centered at the class-conditional data
distribution and one centered at the counterfactual distribu-
tion, where BW2 (P, r) ={µ∈P 2(X) :W 2(µ,P)≤r}
denotes the Wasserstein ball of radius r centered at P.
This two-anchor construction encodes not only sampling
uncertainty but alsogeometric constraints induced by CFs,
yielding alens-shaped ambiguity setrather than a single
ball. As a result, robustness in our setting is governed by
0
1
cf
0
1
0.5
Figure 3.CF-consistent Wasserstein lens.All points in the
figure correspond to probability distributions in Wasserstein space.
Each class c is associated with a CF-consistent feasible set Cc =
BW2 (Pc, εc)∩B W2 (Pcf , δc), given by the intersection (colored
face) of a Wasserstein ball centered atPc (dashed circle) and a ball
centered at Pcf (dotted circle). Although CFs are one-sided, Pcf
acts as shared geometric anchor that constrains both classes.
therelative geometrybetween Pc and Pcf, rather than by a
single ambiguity radius.
3.2. Robust Barycenters
Theorem 3.2(Minimizers of Robust Risk Bounds).Let
(Q0,Q 1)∈P 2(X) 2 denote any pair of class-conditional
reconstruction distributions, let U⊂P 2(X) 2 denote the
CF-consistent uncertainty set (Definition 3.1), which con-
tains all class conditional data generating distributions con-
sistent with the observed samples and CFs. For any such re-
construction (Q0,Q 1)∈P 2(X) 2, the worst-casedistribu-
tional reconstruction risk Rc(Qc) = supµ∈Cc W 2 2 (µ,Q c),
admits a tractable Wasserstein-robust upper bound. The
minimizers are the solutions to the optimization problem
min
(Q0,Q1)
X
c∈{0,1}

(1−λ c)W 2 2 (Qc,P c) +λ cW 2 2 (Qc,P cf )  .
Minimizing this objective is not equivalent to solving the
constrained robust problem directly, but yields a geometry-
aware surrogate whose minimizers are stable under CF-
consistent perturbations. We measure reconstruction risk in
Wasserstein distance to ensure consistency with the geome-
try of the uncertainty set.
Remark3.3 (Geometric uniqueness).Without additional
regularity assumptions, the minimizer of Theorem 3.2 does
not need be unique as a probability measure. Nevertheless,
all minimizers lie on the same Wasserstein displacement
geodesic between Pc and Pcf , and therefore lead to a unique
CF-identifiable Wasserstein distance geometry.
4

RECAST: Model Reconstruction via Counterfactual-Aware Wasserstein Geometry under Limited Data
Barycentric form.For each c∈ {0,1}, the optimal Q⋆ c
satisfies
Q⋆ c = argmin
µ∈P2(X)

(1−λ c)W 2 2 (µ,P c)+λ cW 2 2 (µ,P cf )  (1)
i.e., Q⋆ c is the 2-Wasserstein barycenter of Pc and Pcf
(App. A.2).
Proof idea.For each class c, a worst-case risk is
Rc(Qc) = sup µ∈Cc W 2 2 (µ,Q c). Using standard inequali-
ties in Wasserstein space, this worst-case risk admits a robust
upper bound by a convex combination of W 2 2 (Qc,P c) and
W 2 2 (Qc,P cf ). Optimizing this bound yields the Wasserstein
barycenter in Eq. (1), and separability across classes gives
the objective in Theorem 3.2. The full proof is given in
App. A.3.
Importantly, our formulation does not require explicit spec-
ification of the uncertainty radii εc and δc. In our deriva-
tion (App. A.3), their relative effect is absorbed into the
data-dependent mixing weight λc: selecting an optimal λc
corresponds to selecting optimal radii, and λc determines
the location of the CF-consistent Wasserstein barycenter.
Canonical instantiation of λc.To better illustrate the
role of λc, we rewrite the class-specific objective (Theo-
rem 3.2) in an equivalent normalized form by dividing by
(1−λ c):
min
(Q0,Q1)
X
c∈{0,1}

W 2 2 (Qc,P c) + λc 1−λ c W 2 2 (Qc,P cf )  .
This form makes explicit that the influence of CF informa-
tion is governed by the ratioλ c/(1−λ c).
Theorem 3.2 yields a family of robust barycenters{Q⋆ c (λc)}.
In classical Wasserstein robust optimization, one would
select λc (equivalently, the ambiguity radius) to tighten the
bound with respect to the true risk. However, under one-
sided CF access and limited data, such statistical calibration
is fundamentally infeasible.
In this regime, λc is not uniquely identifiable from data
within the CF-consistent uncertainty set. We consequently
instantiate λc through the observable Wasserstein geometry
of the three anchor distributions. Let A=W 2 2 (Pcf ,P c) and
B=W 2 2 (Pcf ,P 1−c). The relative geometry induces the
relation λc 1−λc = B A+B , yielding the closed-form expression
λc = B A+2B .
From this perspective, the ratioλ c/(1−λ c)modulates the
contribution of one sided CF samples assoft cross-classsig-
nals: it increases as Pcf is away from the opposite class1−c ,
and decreases when it is relatively distant from class c. The
formulation degrades gracefully at boundary cases: when
Pcf =P 1, the weights reduce to λ1 = 0 and λ0 = 1, CFs
0 1 2 3 4 f1
0
1
2
f2
0 1 2 3 4 f1
0
1
2
f2
Class 0 0
 Class 1 1
 cf
 0
 1
 0.5
Figure 4.Top: Full original dataset and decision tree classification
(blue and pink); CFs as x (orange); points available for reconstruc-
tion circled (black).Bottom: Decision region between barycenters:
Q0 (blue), Q1 (pink); black circles midpoints along the optimal
transport path (grey lines), indicating the decision regionQ 0.5.
carry then no influence on Q⋆ 0, and the formulation reduces
to standard binary classification. The case εc =δ c = 0
would require Pc =P cf, which contradicts the reject-to-
accept CF setting and renders the problem ill-posed. When
Pcf lies approximately equidistant between the two class
distributions, the resulting ratio assigns comparable influ-
ence to both classes. To set λc appropriately, we consider
the following stability:
Lemma 3.4(Stability along the barycentric geodesic).For
class c∈ {0,1}, let (Q⋆ c (λ))λ∈[0,1] denote a constant-speed
Wasserstein geodesic between Pc and Pcf. Then, function
λc 7→R c(Q⋆ c (λc)) is Lipschitz continuous on [0,1] , with
Lipschitz constant
Lc = 2

εc +W 2(Pc,P cf )

W2(Pc,P cf ).
Consequently, small perturbations of λc lead to proportion-
ally small changes in the worst-case risk. Proof in App. A.4.
As a direct consequence, for any (unobservable) optimizer
λ⋆ c ∈[0,1] of the robust upper bound along the barycentric
geodesic, the suboptimality of a chosenλ c is bounded as
Rc(Q⋆ c (λc))−R c(Q⋆ c (λ⋆ c ))≤L c |λc −λ ⋆ c |.
This result ensures that the canonical instantiation remains
behaviorally stable even under under small variations of λc.
3.3. Barycentric Prototype Classifier
Definition 3.5(CF-consistent behavioral equivalence).Two
different classifiers m1, m2 arebehaviorally equivalent
(w.r.t. one-sided CF access), if ∀µ∈U,Pr x∼µ

m1(x)̸=
m2(x)

= 0, where the probability denotes the disagree-
ment rate of the two different models underµ.
The CF-consistent uncertainty setU contains multiple class-
conditional distributions that are indistinguishable from the
observed data.Any valid pointwise decision rule must there-
fore be invariant over all(µ0, µ1)∈U of class-conditional
data generating distributions, and cannot depend on quanti-
ties (such as densities or likelihoods) that vary within this
5

RECAST: Model Reconstruction via Counterfactual-Aware Wasserstein Geometry under Limited Data
set.In contrast, Wasserstein distances are invariant to CF-
unidentifiable variations, making W2(δx, ˆQc) a natural CF-
identifiable score. This is because CF-consistent uncertainty
constrains only how probability mass can be transported in
the input space, while leaving its local density unspecified;
density-based quantities vary under such unidentifiable rear-
rangements, whereas Wasserstein distances depend solely
on the induced transport geometry.
Given the reconstructed class prototypes ( ˆQ0, ˆQ1), a CF-
identifiable decision statistic is given by the 2-Wasserstein
distance from a Dirac mass to the class prototypes:
ˆm(x) := arg min
c∈{0,1}
W2

δx, ˆQc

,(2)
where δx denotes the Dirac measure at an input x. This
classifier should be interpreted as a canonical representative
of the CF-consistent behavioral equivalence class, rather
than a uniquely identifiable ground-truth decision rule.Im-
portantly, the proposed framework does not restrict the form
of the final decision mechanism, provided it operates solely
on CF-identifiable geometric quantities.
The stability of the barycentric classifier follows directly
from the Wasserstein geometry. By Corollary A.4 in
App. A.3, the induced pointwise decision score is Lipschitz
continuous with respect to perturbations of the prototype
distributions under W2. This stability, combined with the
distributional smoothing induced by the barycentric aggrega-
tion, yields a uniform bound on the prediction disagreement
between the classifiers. Thus, for any Q′ c distribution in
CF-consistent feasible set Cc: W2(Qc,Q ′ c)≤ p Rc(Qc),
and small reconstruction risks Rc(Qc) imply small varia-
tions in the classification behavior across all CF-consistent
realizations.
This classification rule induces a decision region in Wasser-
stein space. Let T denote an optimal transport map from
ˆQ0 to ˆQ1. The Wasserstein geodesic between the two
class prototypes is given by the displacement interpolation
Qγ :=

(1−γ)Id+γT

#
ˆQ0, γ∈[0,1]. The decision
region is characterized by the midpoint of this geodesic,
Q0.5 =

1
2 Id+ 1 2 T  # ˆQ0, which represents the distribu-
tion equidistant from both class prototypes in Wasserstein
distance (Figure 4). In this geometric view, ˆQ0 and ˆQ1 act
as distributionalprototypes, summarizing the CF-consistent
class-conditional geometry. Classification is performed by
comparing the Wasserstein distance of a point to these pro-
totypes, yielding a prototype-based classifier in Wasserstein
space. For the overall geometric relationship between CF-
consistent lens and barycentric prototypes see Figure 3.
3.4. Threshold-invariant Fairness Diagnostic
RECAST also supports fairness auditing by adapting a
threshold-invariant fairness diagnostic in the perspective
of Wasserstein geometry. Given the barycentric class pro-
totypes (Q⋆ 0, Q⋆ 1), we define a Wasserstein-geometric score
p:X→(0,1)as:
p(x) =σ

W2(δx, Q⋆ 0)−W 2(δx, Q⋆ 1) 
where σ denotes the sigmoid function. Based on Chen & Wu
(2020), we adapt Threshold Invariant Demographic Parity
(TIDP) and Threshold Invariant Equalized Odds (TIEO), i.e.,
equal selection rates and equal prediction accuracy across
sensitive attributes independent of a decision threshold, in
the perspective of Wasserstein geometry. In contrast to
previous work, our score operates on entire score distribu-
tions, capturing disparities that persist across all decision
thresholds. We quantify group-level disparities by compar-
ing the distributions of this score across sensitive groups
that share a sensitive attribute S∈ {0,1} . We compute
the Wasserstein-1 distance between the score distributions
conditioned on different values of S to assess TIDP, and
between score distributions conditioned on both S and the
label Y∈ {0,1} to assess TIEO. As the scores are induced
by barycentric prototypes defined over the CF-consistent
feasible sets, the resulting fairness diagnostics are evaluated
with respect to a shared uncertainty-aware decision geome-
try and quantify how different groups are positioned relative
to the barycentric decision geodesic. Equations in App. A.7.
Summary.Under one-sided CF access the target decision
boundary is fundamentally non-identifiable, so reconstruc-
tion cannot recover a unique ground-truth classifier. RE-
CAST therefore (i) constructs a CF-consistent Wasserstein
uncertainty set, (ii) computes ˆQc as Wasserstein barycen-
ters, and (iii) predicts with the classification rule, Eq. (2).
Minimizing the resulting Wasserstein reconstruction risk
promotes stability of decision behavior under CF-consistent
perturbations, yielding reduced prediction disagreement.
4. Experiments
We evaluate RECAST across four real-world datasets, three
target model families, and multiple CF generation methods,
assessing fidelity, robustness, and fairness preservation.
4.1. Experimental Setup
Data.We study four publicly available binary classifica-
tion datasets, that are often used in literature and cover a
variety of properties, e.g., dimensionalities, dataset size, and
tasks: Adult Income (Becker, 1996), COMPAS (Angwin
et al., 2016), HELOC (FICO, 2018), and California Hous-
ing (Pace & Barry, 1997). We include exploratory cases on
additional data modalities in App. C.6 and C.7.
Baselines.To the best of our knowledge, there is limited
prior work on reconstruction restricted data access and only
6

RECAST: Model Reconstruction via Counterfactual-Aware Wasserstein Geometry under Limited Data
one-sided CFs (Table 1). As such, we adapt three repre-
sentative baselines tooffline-only, i.e., no querying during
reconstruction. A ¨ıvodji et al. (2020), referred to asSAM-
PLES, incorporates CFs as ordinary samples.CCA, Coun-
terfactual Clamping Attack, modifies entropy loss to explic-
itly incorporate CFs (Dissanayake & Dutta, 2024). TRA
(Khouna et al., 2025) assumes prior knowledge that the tar-
get classifier is a decision tree with axis-parallel splits, and
is therefore included only when such structural information
is available; in contrast, RECAST and the other baselines
operate without access to this form of model-specific prior.
For all baselines, we use hyperparameters recommended in
the original papers.
Barycentric prototype computation.We compute the
barycenters Qc using optimization Algorithm 1 in
App. A. We optimize an entropically regularized (Sinkhorn-
smoothed) surrogate of the Wasserstein barycenter objective
for computational efficiency, following standard practice in
optimal transport (Chizat et al., 2020), theoretical guarantees
and an ablation regarding the blur parameter are included
in App. A.5 and A.6. All solver settings and hyperparame-
ters are kept fixed across experiments. All implementation
details, including initialization, solver settings, and hyper-
parameters also in App. B. Code is available online.2
Reconstruction.As target models, we studyneural net-
works (MLP), logistic regression (LR), and tree-based clas-
sifiers (DT)trained on 80% of the original datasets, which
remains unknown during the reconstruction phase. In each
experiment, we randomly sample a certain query size, e.g.,
100 instances from class 0 and 100 from class 1, as D0,
D1, resp. From class 0 samples various CF methods are
used to generate CFs Dcf. We evaluate the reconstructed
models on a held-out reference set Dref, disjoint from the
reconstruction data.
We usefidelity(A ¨ıvodji et al., 2020) rather than accuracy as
our primary metric: a surrogate that faithfully mimics the tar-
get model’s decision, including its systematic errors, should
score highly regardless of ground-truth label agreement,
since behavioral reconstruction, not predictive performance
is the relevant objective for reconstruction (see App. C.3 for
a joint comparison).
Fidelity between the target model m and the surrogate ˆm
on a reference setD ref is defined as:
Fidm,Dref( ˆm) = 1 |Dref| X x∈Dref I[0,1] [m(x) = ˆm(x)].
We repeat each experiment ten times with different random
seeds and report the mean and variance of our method. In
2https://github.com/zhaoxuan00707/ce_
reconstruction
addition to the balanced setting, we conduct supplementary
experiments with imbalanced D0 and D1; see results in
App. B.
CF Generation.We evaluate several CF generation meth-
ods, including MCCF (Wachter et al., 2017), which seeks
CFs with minimal input changes. In our implementation,
we add an ℓ1 regularization term to encourage sparse input
changes. DiCE (Mothilal et al., 2020) ensures actionability
by enforcing immutable features. To improve robustness un-
der model shifts, we adopt ROAR (Upadhyay et al., 2021).
For realism, we apply 1-Nearest-Neighbor from the desired
class and C-CHV AE (Pawelczyk et al., 2020), which uses
variational autoencoders. Details in App. B.
Robustness Evaluation Protocol.Since RECAST is de-
rived under CF-consistent uncertainty, we evaluate not only
average fidelity under i.i.d. test data, but also robustness
under distributional shifts. Although our uncertainty is spec-
ified over training distributions, its effect manifests as sensi-
tivity to distributional shifts during test. We thus evaluate
robustness by probing fidelity under perturbations of the
test distribution, which operationalizes different plausible
realizations of the underlying Qc. Specifically, for each
reference test set Dref, we construct a family of shifted test
sets Dref ={x+ϵ:x∈D ref , ϵ∼N(0, τ 2I)}, with
noise levelsτ∈ {0.05,0.1,0.2,0.4}.
Although average fidelity is a widely used metric for model
reconstruction, it can be dominated by samples far from
the decision threshold, whose predictions are inherently sta-
ble under perturbations. Consequently, high overall fidelity
may mask disagreement in decision-sensitive regions. We
thus also evaluate robustness on a near-threshold subset
where the target model likely exhibits higher uncertainty.
Although the true decision boundary is not identifiable,
|ˆym(x)−0.5| ≤γcaptures inputs most susceptible to distri-
butional perturbations (Blanchet et al., 2024). We define the
near-threshold set as Dnear ={x∈D ref :|ˆym(x)−0.5| ≤
γ}, with γ= 0.05 . We report fidelity on both the full set
Dref and on Dnear. Note that access to the target model’s
continuous output scores is used only during the evaluation
phase to construct diagnostic subsets Dnear, and is neither
available nor used during the reconstruction phase. We ad-
ditionally evaluate robustness under cross-domain covariate
shift, details of that protocol are in App. C.4.
Fairness Diagnostic Protocol.For each distribution-shift
level τ, we report the absolute difference between the fair-
ness diagnostics for target modelm and reconstructed model
ˆmover the corresponding shifted reference set Dref. We
show how well the reconstructed models preserve the origi-
nal decision disparities, and assess their use for auditing.
7

RECAST: Model Reconstruction via Counterfactual-Aware Wasserstein Geometry under Limited Data
Table 2.Fidelity. Multilayer perceptron (MLP), logistic regression (LR), decision tree (DT) target models, low-query size 100. RECAST
consistently achieves higher (in one case comparable) fidelity across datasets and target models. TRA only feasible with DT target.
Dataset MLP (Target Model) LR (Target Model) DT (Target Model)
SAMPLES CCA RECAST (Ours) SAMPLES CCA RECAST (Ours) SAMPLES CCA RECAST (Ours) TRA
Adult In.0.801±0.035 0.843±0.0200.908±0.0340.909±0.008 0.816±0.0250.913±0.0330.819±0.017 0.827±0.0180.894±0.0400.842±0.020
COMPAS0.415±0.060 0.765±0.0200.855±0.0220.543±0.004 0.785±0.0260.821±0.0470.396±0.003 0.657±0.0270.869±0.0490.826±0.007
HELOC0.427±0.121 0.644±0.0570.696±0.0780.551±0.013 0.670±0.0130.798±0.0250.620±0.008 0.702±0.0230.772±0.0290.702±0.024
Housing0.459±0.1020.716±0.0700.712±0.121 0.477±0.001 0.656±0.0140.789±0.0940.554±0.012 0.619±0.0340.774±0.1490.654±0.015
Figure 5.Fidelity (mean ± std) of surrogate models on real-world datasets under varying query sizes. RECAST with superior performance.
Ablation Study.We conduct an ablation study on differ-
ent prototype constructions, distance metrics, and CFs inte-
gration strategies in RECAST with all details in App. C.1.
4.2. Reconstruction Fidelity
Table 2 summarizesfidelityresults across target classifiers,
with query size 100 and MCCF as CF generation method.
In almost all cases, our method achieves superior fidelity to
SAMPLESandCCA, comparable in one. We also study how
the amount of available training data influences the perfor-
mance of the reconstructed models with query sizes from
25 to 400 in Figure 5. Notably, our approach demonstrates
a clear advantage when the query size is small, highlighting
its efficiency in low-query regimes.
4.3. Effect of CF Geometry
RECAST consistently achieves high fidelity across CF gen-
eration strategies, see Table 3. Baseline methods exhibit
substantially larger fluctuations, indicating sensitivity to
the properties of CFs. Unlike baselines, RECAST neither
interprets CFs as true samples (SAMPLES) nor assumes
proximity to the decision boundary (CCA), properties that
depend on the generator, illustrated in Figure 2.
4.4. Robustness under Perturbations
We study robustness along two axes:behavioral stability
under additive perturbations of the test distribution andgen-
eralizationunder realistic distribution shift across domains.
Both test whether RECAST’s behavioral agreement with the
target model holds beyond the reconstruction setting. Dis-
agreement between a reconstructed surrogate and the target
model may arise when perturbations cause inputs to cross de-
cision surfaces, an effect most pronounced near the decision
threshold. As the perturbation strength increases, fidelity
decreases for all methods (see Figure 6). Still, RECAST
degrades substantially more gracefully than the baselines,
and SAMPLES and CCA suffer pronounced performance
drops even under moderate noise. This gap is even more pro-
nounced in the near-threshold region Dnear most sensitive
to perturbations.
Along the second axis, we evaluate robustness under real-
istic distribution shift using Folktables ACSIncome dataset
(Ding et al., 2021), training on California 2018 data and
evaluating on Michigan 2014, a setting that combines both
geographical and temporal variation (see App. C.4,Table 7).
RECAST consistently achieves highest fidelity across query
budgets (100 and 150), while SAMPLES leads on accuracy
but lags notably on fidelity, consistent with the distinction
drawn above, where accuracy and fidelity capture funda-
mentally different objectives. These results confirm that
RECAST maintains strong behavioral consistency with the
target model even under substantial distribution shifts.
Table 3.Fidelity, varying counterfactual generation methods on
Adult, query size 100, target MLP. RECAST shows robustness
with high fidelity across diverse CF generators.
CF Generation Baselines
SAMPLES CCA RECAST (Ours)
MCCF0.793 0.8930.913
DiCE0.9330.903 0.923
ROAR0.735 0.7350.910
1-Nearest-Neighbor0.712 0.8350.916
C-CHV AE0.357 0.8170.923
8

RECAST: Model Reconstruction via Counterfactual-Aware Wasserstein Geometry under Limited Data
Figure 6.Robustness to additive noise on Adult. Fidelity as a
function of the noise level τ for both full reference set Dref and
near-threshold subset Dnear, which captures decision-sensitive
inputs.∆denotes the fidelity drop betweenτ= 0andτ= 0.4.
4.5. Fairness Diagnostics
The goal of the proposed fairness diagnostics is to assess
whether a reconstructed surrogate preserves the fairness-
related behavior of the target model, under CF-consistent
distributional uncertainty.These diagnostics are thus in-
tended solely for auditing purposes and do not constitute
fairness performance or debiasing claims. Figure 7 reports
the fairness diagnostic error between the reconstructed sur-
rogate and the target model under increasing perturbations.
Lower values indicate that the surrogate more faithfully
preserves the fairness characteristics of the target model.
RECAST consistently exhibits smaller diagnostic consis-
tency gap and more graceful degradation with noise.
4.6. Effect of Query Budget
RECAST is designed for limited query access and one-
sided CFs, where direct reconstruction of the target model
is fundamentally sample-inefficient and the decision bound-
ary is not statistically identifiable. To make this regime
explicit, we additionally study how reconstruction perfor-
mance varies with available query budget.
Specifically, we compare RECAST with a no CFs baseline
over number of queried labeled instances, and identify the
crossover point at which direct supervised reconstruction
becomes competitive (Figure 9, App. C.5). This analysis re-
veals a clear practical boundary: in low-query regimes, CFs
provide crucial decision-relevant information that cannot be
recovered from samples alone, enabling RECAST to sub-
stantially outperform both CF-based and non-CF baselines.
As the query budget increases and empirical samples begin
to adequately cover decision-relevant regions, the advantage
of CF-based reconstruction naturally diminishes, and sim-
pler supervised models become sufficient. Note that with
sufficient data, the Wasserstein mixing weights could be
Figure 7.Absolute fairness (DTIDP (solid) and DTIEO (dashed))
differences between reconstructed and target model as a function
of noise level τ. Lower values mean more faithful preservation of
target model fairness characteristics.
calibrated via classical WRO methods, but this lies beyond
the scope of the low-query regime studied here.
In privacy-sensitive auditing contexts, where datasets are
small, access is restricted, and queries are costly, such high-
capacity approaches become infeasible, making lightweight,
geometry-driven reconstruction methods such as RECAST
particularly relevant in practice.
We acknowledge that Wasserstein distance can be computa-
tionally demanding in large-scale settings. However, in the
low-data regimes considered here, this cost is not a practical
bottleneck. In runtime experiments (App. C.8), we observe
training times near linear in query size.
5. Conclusion and Future Work
We propose RECAST, a model reconstruction approach
grounded in Wasserstein geometry that captures relation-
ships between data distributions, enabling the formation of
robust class prototypes that effectively represent both la-
beled data and CFs, under one-sided CF access and limited
query budgets.
In our experiments, we demonstrate that RECAST maintains
high fidelity in small data regimes, where overfitting and
poor generalization are prevalent concerns. Importantly,
RECAST is not designed to compete with large-query model
extraction: it is designed for reconstruction scenarios where
data is scarce, access is restricted, and CFs are the only
boundary-relevant signal.
Our approach is currently limited to binary classification,
which is common in literature since most applications con-
sider accept-reject decision. Extending RECAST to multi-
class settings, and leveraging prior knowledge constitute
interesting directions for future work.
9

RECAST: Model Reconstruction via Counterfactual-Aware Wasserstein Geometry under Limited Data
Acknowledgements
This work was partially funded by project W2/W3-108 Ini-
tiative and Networking Fund of the Helmholtz Association.
We gratefully acknowledge the computing time granted
through project XAI (No. 65881) on the supercomputer
JURECA at J¨ulich Supercomputing Centre (JSC).
Impact Statement
This work studies classifier reconstruction under restricted
data access and one-sided CF supervision, a setting that
arises naturally when interacting with black-box or propri-
etary decision systems. By characterizing what aspects of
model behavior are fundamentally identifiable under such
constraints, our framework enables high-fidelity reconstruc-
tion of decision behavior, supporting the auditing and in-
vestigation of deployed models for fairness, bias, and ac-
countability concerns in settings with limited model access.
Importantly, our approach does not aim to recover a unique
ground-truth classifier or individual training examples, but
instead focuses on CF-identifiable behavioral structure de-
rived from distributional and counterfactual information.
The primary impact of our work involves reducing the barri-
ers to model reconstruction. Organizations and communities
affected by ML decision-making systems, e.g., loan appli-
cations, hiring, or healthcare, often lack resources to audit
the systems they rely on. Our approach offers these groups
a practical tool to investigate issues, such as disparate im-
pact, discrimination, or violations of fairness principles in
deployed models, even when model owners are unwilling
or unable to grant direct access.
Our work supports the regulatory landscape around responsi-
ble, transparent and accountable AI, as policymakers world-
wide establish requirements for algorithmic impact assess-
ments and accountability.
While our method does introduce security considerations for
information leakage, the societal benefit of enabling fairness
investigations outweighs these concerns in contexts involv-
ing high-stakes decisions affecting vulnerable populations.
Our work is likely to advance the field toward the establish-
ment of more trustworthy and responsible AI systems by
improving accountability.
References
Agueh, M. and Carlier, G. Barycenters in the wasserstein
space.SIAM J. Math. Anal., 43(2):904–924, 2011. doi:
10.1137/100805741. URL https://doi.org/10.
1137/100805741.
A¨ıvodji, U., Bolot, A., and Gambs, S. Model extraction
from counterfactual explanations.CoRR, abs/2009.01884,
2020.
A¨ıvodji, U., Arai, H., Gambs, S., and Hara, S. Char-
acterizing the risk of fairwashing. pp. 14822–
14834, 2021. URL https://proceedings.
neurips.cc/paper/2021/hash/
7caf5e22ea3eb8175ab518429c8589a4-
Abstract.html.
Angwin, J., Larson, J., Mattu, S., and Kirchner, L. Prop-
ublica compas recidivism risk score data and analysis.
https://www.propublica.org/article/
machine-bias-risk-assessments-in-
criminal-sentencing, 2016.
Becker, B. Adult data set. https://archive.ics.
uci.edu/dataset/2/adult, 1996.
Blanchet, J. H., Kang, Y ., and M., K. R. A. Robust
wasserstein profile inference and applications to machine
learning.J. Appl. Probab., 56(3):830–857, 2019. doi:
10.1017/JPR.2019.49. URL https://doi.org/10.
1017/jpr.2019.49.
Blanchet, J. H., Cui, P., Li, J., and Liu, J. Stability evaluation
through distributional perturbation analysis. InICML.
OpenReview.net, 2024.
Carlini, N., Paleka, D., Dvijotham, K. D., Steinke, T.,
Hayase, J., Cooper, A. F., Lee, K., Jagielski, M.,
Nasr, M., Conmy, A., Wallace, E., Rolnick, D., and
Tram`er, F. Stealing part of a production language model.
2024. URL https://openreview.net/forum?
id=VE3yWXt3KB.
Chen, M. and Wu, M. Towards threshold invariant fair
classification. InUAI, volume 124 ofProceedings of
Machine Learning Research, pp. 560–569. AUAI Press,
2020.
Chizat, L., Roussillon, P., L ´eger, F., Vialard, F., and
Peyr´e, G. Faster wasserstein distance estimation with
the sinkhorn divergence. In Larochelle, H., Ranzato,
M., Hadsell, R., Balcan, M., and Lin, H. (eds.),Ad-
vances in Neural Information Processing Systems 33:
Annual Conference on Neural Information Processing
Systems 2020, NeurIPS 2020, December 6-12, 2020,
virtual, 2020. URL https://proceedings.
neurips.cc/paper/2020/hash/
17f98ddf040204eda0af36a108cbdea4-
Abstract.html.
Deng, L. The MNIST database of handwritten digit images
for machine learning research [best of the web].IEEE
Signal Process. Mag., 29(6):141–142, 2012. doi: 10.
1109/MSP.2012.2211477. URL https://doi.org/
10.1109/MSP.2012.2211477.
10

RECAST: Model Reconstruction via Counterfactual-Aware Wasserstein Geometry under Limited Data
Ding, F., Hardt, M., Miller, J., and Schmidt, L. Retiring
adult: New datasets for fair machine learning.Advances
in Neural Information Processing Systems, 34, 2021.
Dissanayake, P. and Dutta, S. Model reconstruction using
counterfactual explanations: A perspective from polytope
theory. In Globersons, A., Mackey, L., Belgrave, D., Fan,
A., Paquet, U., Tomczak, J. M., and Zhang, C. (eds.),
Advances in Neural Information Processing Systems 38:
Annual Conference on Neural Information Processing
Systems 2024, NeurIPS 2024, Vancouver, BC, Canada,
December 10 - 15, 2024, 2024. URL http://papers.
nips.cc/paper_files/paper/2024/hash/
97d539aa02b82c52d4a9eda62e1c6435-
Abstract-Conference.html.
Dwork, C., Hardt, M., Pitassi, T., Reingold, O., and Zemel,
R. Fairness through awareness. InProceedings of the 3rd
innovations in theoretical computer science conference,
pp. 214–226, 2012.
Feldman, M., Friedler, S. A., Moeller, J., Scheidegger, C.,
and Venkatasubramanian, S. Certifying and removing dis-
parate impact. Inproceedings of the 21th ACM SIGKDD
international conference on knowledge discovery and
data mining, pp. 259–268, 2015.
Ferry, J., Fukasawa, R., Pascal, T., and Vidal, T. Trained ran-
dom forests completely reveal your dataset. InForty-first
International Conference on Machine Learning, ICML
2024, Vienna, Austria, July 21-27, 2024. OpenReview.net,
2024. URL https://openreview.net/forum?
id=cc72Vnfvoc.
Feydy, J., S´ejourn´e, T., Vialard, F., Amari, S., Trouv´e, A.,
and Peyr´e, G. Interpolating between optimal transport and
MMD using sinkhorn divergences. In Chaudhuri, K. and
Sugiyama, M. (eds.),The 22nd International Conference
on Artificial Intelligence and Statistics, AISTATS 2019,
16-18 April 2019, Naha, Okinawa, Japan, volume 89 of
Proceedings of Machine Learning Research, pp. 2681–
2690. PMLR, 2019. URL http://proceedings.
mlr.press/v89/feydy19a.html.
FICO. Explainable machine learning challenge dataset,
2018. URL https://community.fico.
com/s/explainable-machine-learning-
challenge.
Gao, R. and Kleywegt, A. J. Distributionally robust stochas-
tic optimization with wasserstein distance.Math. Oper.
Res., 48(2):603–655, 2023. doi: 10.1287/MOOR.2022.
1275. URL https://doi.org/10.1287/moor.
2022.1275.
Gong, X., Wang, Q., Chen, Y ., Yang, W., and Jiang,
X. Model extraction attacks and defenses on cloud-
based machine learning models.IEEE Commun.
Mag., 58(12):83–89, 2020. doi: 10.1109/MCOM.
001.2000196. URL https://doi.org/10.1109/
MCOM.001.2000196.
Hardt, M., Price, E., and Srebro, N. Equality of opportunity
in supervised learning.Advances in neural information
processing systems, 29, 2016.
Heckman, J. J. Sample selection bias as a specification error.
Econometrica: Journal of the econometric society, pp.
153–161, 1979.
Jagielski, M., Carlini, N., Berthelot, D., Kurakin, A., and
Papernot, N. High accuracy and high fidelity extraction
of neural networks. In29th USENIX security symposium
(USENIX Security 20), pp. 1345–1362, 2020.
Jigsaw. Jigsaw toxic comment classification chal-
lenge. https://www.kaggle.com/c/jigsaw-
toxic-comment-classification-
challenge, 2018.
Khouna, A., Ferry, J., and Vidal, T. From counterfactuals to
trees: Competitive analysis of model extraction attacks.
CoRR, abs/2502.05325, 2025. doi: 10.48550/ARXIV .
2502.05325. URLhttps://doi.org/10.48550/
arXiv.2502.05325.
Liang, J., Pang, R., Li, C., and Wang, T. Model extraction
attacks revisited. In Zhou, J., Quek, T. Q. S., Gao, D., and
C´ardenas, A. A. (eds.),Proceedings of the 19th ACM Asia
Conference on Computer and Communications Security,
ASIA CCS 2024, Singapore, July 1-5, 2024. ACM, 2024.
doi: 10.1145/3634737.3657002. URL https://doi.
org/10.1145/3634737.3657002.
McCann, R. J. A convexity principle for interacting gases.
Advances in mathematics, 128(1):153–179, 1997.
Mohajerin Esfahani, P. and Kuhn, D. Data-driven distribu-
tionally robust optimization using the wasserstein met-
ric: Performance guarantees and tractable reformulations.
Mathematical Programming, 171(1):115–166, 2018.
Mothilal, R. K., Sharma, A., and Tan, C. Explaining ma-
chine learning classifiers through diverse counterfactual
explanations. InFAccT, pp. 607–617. ACM, 2020.
Orekondy, T., Schiele, B., and Fritz, M. Knockoff nets:
Stealing functionality of black-box models. InCVPR, pp.
4954–4963. Computer Vision Foundation / IEEE, 2019.
Pace, R. K. and Barry, R. Sparse spatial autoregressions,
1997. URL https://www.dcc.fc.up.pt/
˜ltorgo/Regression/cal_housing.html.
Data retrieved from the StatLib repository.
11

RECAST: Model Reconstruction via Counterfactual-Aware Wasserstein Geometry under Limited Data
Pal, S., Gupta, Y ., Shukla, A., Kanade, A., Shevade, S., and
Ganapathy, V . Activethief: Model extraction using active
learning and unannotated public data. InProceedings of
the AAAI conference on artificial intelligence, volume 34,
pp. 865–872, 2020.
Pawelczyk, M., Broelemann, K., and Kasneci, G. Learning
model-agnostic counterfactual explanations for tabular
data. InWWW, pp. 3126–3132. ACM / IW3C2, 2020.
Shimodaira, H. Improving predictive inference under covari-
ate shift by weighting the log-likelihood function.Jour-
nal of statistical planning and inference, 90(2):227–244,
2000.
Shokri, R., Strobel, M., and Zick, Y . On the privacy risks of
model explanations. InAIES, pp. 231–241. ACM, 2021.
Tram`er, F., Zhang, F., Juels, A., Reiter, M. K., and Risten-
part, T. Stealing machine learning models via predic-
tion apis. InUSENIX Security Symposium, pp. 601–618.
USENIX Association, 2016.
Upadhyay, S., Joshi, S., and Lakkaraju, H. Towards robust
and reliable algorithmic recourse. InNeurIPS, pp. 16926–
16937, 2021.
Wachter, S., Mittelstadt, B. D., and Russell, C. Counterfac-
tual explanations without opening the black box: Auto-
mated decisions and the GDPR.CoRR, abs/1711.00399,
2017.
Wang, Y ., Qian, H., and Miao, C. Dualcf: Efficient model
extraction attack from counterfactual explanations. In
FAccT, pp. 1318–1329. ACM, 2022.
You, L., Cao, L., Nilsson, M., Zhao, B., and Lei, L. Distri-
butional counterfactual explanations with optimal trans-
port. InAISTATS, volume 258 ofProceedings of Machine
Learning Research, pp. 1135–1143. PMLR, 2025.
Zadrozny, B. Learning and evaluating classifiers under
sample selection bias. InProceedings of the twenty-first
international conference on Machine learning, pp. 114,
2004.
Zhao, K., Li, L., Ding, K., Gong, N. Z., Zhao, Y ., and Dong,
Y . A survey on model extraction attacks and defenses for
large language models. InProceedings of the 31st ACM
SIGKDD Conference on Knowledge Discovery and Data
Mining V . 2, pp. 6227–6236, 2025.
12

RECAST: Model Reconstruction via Counterfactual-Aware Wasserstein Geometry under Limited Data
A. Wasserstein Distance and Barycenters
A.1. Wasserstein Distance
We briefly recall the notions from optimal transport that are required for the formulation and analysis of our reconstruction
framework, in particular Definition 3.1 and Theorem 3.2. Let P2(Rd) denote the set of probability measures on Rd with
finite second moments.
2-Wasserstein distance.Forµ, ν∈P 2(Rd), the squared2-Wasserstein distance is defined as
W 2 2 (µ, ν) := inf γ∈Π(µ,ν)
Z
Rd×Rd
∥x1 −x 2∥2 2 dγ(x1, x2),(3)
whereΠ(µ, ν)denotes the set of couplings (transport plans) with marginalsµandν.
The Wasserstein distance induces a geometry on probability measures that accounts for both mass displacement and spatial
structure, and is therefore well suited for comparing distributions arising from localized perturbations such as counterfactual
examples.
Monge formulation.When there exists a measurable transport map T:R d →R d such that T#µ=ν , the optimal
transport problem admits the equivalent Monge formulation
T= arg min
T#µ=ν
Z
Rd
∥x−T(x)∥ 2 2 dµ(x).(4)
In general, such a map need not exist; however, the Kantorovich formulation in(3) always remains well defined and is the
form used throughout this work.
A.2. Wasserstein Barycenter
Given a finite collection of probability measures{µi}N i=1 ⊂P 2(Rd) and nonnegative weights{λi}N i=1 satisfying PN i=1 λi =
1, the Wasserstein barycenter is defined as
µ∗ = arg min
µ∈P2(Rd)
NX
i=1
λiW 2 2 (µ, µi).(5)
The barycenter µ∗ provides a distributional prototype that summarizes the input measures in Wasserstein space. Unlike
Euclidean averaging, this formulation aligns probability mass prior to aggregation, enabling the resulting prototype to reflect
decision-relevant geometric structure induced by the target classifier.
In our setting, the input measures correspond to distributions derived from counterfactual perturbations. These perturbations
encode geometric information about the decision behavior of the black-box model, allowing the barycenter to serve as a
behaviorally meaningful class-level representation without requiring explicit recovery of the decision boundary.
A.2.1. RELEVANT PROPERTIES
We summarize only the properties required for the theoretical results in Section 3.
•Existence.If eachµ i ∈P 2(Rd), then a Wasserstein barycenterµ ∗ exists.
• Convexity of the objective.The barycenter objective in Eq. (5) is convex in µ, ensuring that all minimizers attain the
same optimal value.
• Non-uniqueness.The barycenter may not be unique; however, as shown in Theorem 3.2, this non-identifiability does
not affect the induced decision rule, which depends only on Wasserstein distance values rather than on a particular
minimizer.
13

RECAST: Model Reconstruction via Counterfactual-Aware Wasserstein Geometry under Limited Data
A.3. Robust Risk Bounds and Barycentric Optima
We begin by proving Theorem 3.2, which establishes that the minimizers of a CF-consistent robust risk upper bound admit
a Wasserstein barycentric form. The subsequent results in this subsection further clarify the geometric interpretation and
stability properties of these barycentric optima.
Proof of Theorem 3.2.
Proof.Fix a classc∈ {0,1}. We derive a tractable upper bound on the CF-consistent worst-case risk
Rc(Qc) := sup
µ∈Cc
W 2 2 (µ,Q c),C c ={µ:W 2(µ,P c)≤ε c, W2(µ,P cf )≤δ c}.
For anyµ∈C c, the triangle inequality yields
W2(µ,Q c)≤W 2(Qc,P c) +ε c, W 2(µ,Q c)≤W 2(Qc,P cf ) +δ c.
Consequently,
W 2 2 (µ,Q c)≤min n W2(Qc,P c) +ε c 2 ,  W2(Qc,P cf ) +δ c 2o .
Since for anyα c ∈[0,1]and anya, b≥0,min{a, b} ≤(1−α c)a+α cb, we obtain
W 2 2 (µ,Q c)≤(1−α c)  W2(Qc,P c) +ε c 2 +α c  W2(Qc,P cf ) +δ c 2 .
To control the cross terms, we apply Young’s inequality: for anyη1, η2 >0and anya≥0,
2εca≤η 1a2 + ε2 c η1 ,2δ ca≤η 2a2 + δ2 c η2 .
Applying this inequality to the two squared terms yields

W2(Qc,P c) +ε c
2
≤(1 +η 1)W 2 2 (Qc,P c) +  1 + 1 η1  ε2 c,

W2(Qc,P cf ) +δ c
2
≤(1 +η 2)W 2 2 (Qc,P cf ) +  1 + 1 η2  δ2 c .
Combining the above bounds, we obtain for allµ∈C c,
W 2 2 (µ,Q c)≤(1−α c)(1 +η 1)W 2 2 (Qc,P c) +α c(1 +η 2)W 2 2 (Qc,P cf ) +K c,
where
Kc = (1−α c)

1 + 1 η1  ε2 c +α c  1 + 1 η2  δ2 c
is independent ofQ c.
Taking the supremum overµ∈C c yields the robust upper bound
Rc(Qc)≤(1−α c)(1 +η 1)W 2 2 (Qc,P c) +α c(1 +η 2)W 2 2 (Qc,P cf ) +K c.
SinceK c does not depend onQ c, minimizing this bound is equivalent to minimizing its quadratic part. Defining
λc = αc(1 +η 2) (1−α c)(1 +η 1) +α c(1 +η 2) ∈[0,1],
we obtain the barycentric objective
(1−λ c)W 2 2 (Qc,P c) +λ cW 2 2 (Qc,P cf ),
whose minimizer is the 2-Wasserstein barycenter ofP c andP cf with weights(1−λ c, λc).
14

RECAST: Model Reconstruction via Counterfactual-Aware Wasserstein Geometry under Limited Data
Existence and interpretation of barycentric optima.Theorem 3.2 shows that minimizing a suitable robust upper bound
on the CF-consistent worst-case risk leads to a Wasserstein barycentric prototype. We formalize this consequence below and
clarify the role of the associated bounding parameters.
Lemma A.1(Barycentric optima induced by robust bounds).For each class c∈ {0,1}, consider the CF-consistent
worst-case risk
Rc(Qc) := sup
µ∈Cc
W 2 2 (µ,Q c),C c ={µ:W 2(µ,P c)≤ε c, W2(µ,P cf )≤δ c}.
There exist parameters αc ∈[0,1] and η1, η2 >0 such that the minimizer of a valid robust upper bound on Rc(Qc) is given
by the2-Wasserstein barycenter betweenP c andP cf with weight
λc = αc(1 +η 2) (1−α c)(1 +η 1) +α c(1 +η 2) .
Equivalently, for this choice of parameters,
arg min
Qc
n
(1−λ c)W 2 2 (Qc,P c) +λ cW 2 2 (Qc,P cf ) o
minimizes a robust upper bound on the CF-consistent worst-case riskR c(Qc).
Proof. This result follows directly from the proof of Theorem 3.2. For any αc ∈[0,1] and η1, η2 >0 , the derivation above
yields a robust upper bound of the form
Rc(Qc)≤(1−α c)(1 +η 1)W 2 2 (Qc,P c) +α c(1 +η 2)W 2 2 (Qc,P cf ) +K c,
whereK c is independent ofQ c.
Since multiplication of the objective by a positive constant does not affect its minimizers, the quadratic part of the bound
can be renormalized to yield the barycentric objective with weight
λc = αc(1 +η 2) (1−α c)(1 +η 1) +α c(1 +η 2) .
RemarkA.2 (Barycentric lens of CF-consistent optima).For any fixedη 1, η2 >0, the mapping
αc 7− →λc = αc(1 +η 2) (1−α c)(1 +η 1) +α c(1 +η 2)
is continuous and strictly increasing from [0,1] to [0,1] . Consequently, by varying αc, the induced barycentric weight
λc ranges over the entire unit interval. Thus, every Wasserstein barycenter along the geodesic betweenPc and Pcf is the
minimizer of some CF-consistent robust upper bound onR c.
Geometrically, the family of robust optima fills the Wasserstein “lens” induced by the intersection BW2 (Pc, εc)∩
BW2 (Pcf , δc), justifying the barycentric prototype interpretation used in Figure 3.
RemarkA.3 (Why no explicit bound tuning is required).Different choices of the bounding parameters (αc, η1, η2) lead
to different robust upper bounds but induce barycentric optima that lie on the same Wasserstein geodesic betweenPc and
Pcf . In practice, we therefore bypass explicit bound tuning and instead select the barycentric weight λc directly from the
empirical geometry, yielding a CF-consistent representative of the robust equivalence class.
Canonical barycentric classifier.Given the surrogate pair(Q ∗ 0,Q ∗ 1), we define the canonical barycentric classifier
ˆm(x) = arg min
c∈{0,1}
W2(δx,Q ∗ c ).
15

RECAST: Model Reconstruction via Counterfactual-Aware Wasserstein Geometry under Limited Data
Corollary A.4(Stability of the induced decision score).Let Q= (Q 0,Q 1) and Q′ = (Q ′ 0,Q ′ 1) be two pairs of class-
conditional prototypes. Define the decision score
∆Q(x) :=W 2(δx,Q 1)−W 2(δx,Q 0),
and the induced classifier
ˆmQ(x) :=I[∆ Q(x)≤0].
Then, for allx∈X,

∆Q(x)−∆ Q′(x)

 ≤W 2(Q0,Q ′ 0) +W 2(Q1,Q ′ 1).
Consequently, for anyL-Lipschitz lossϕ:R→[0,1],

Ex∼PX [ϕ(∆Q(x))]−E x∼PX [ϕ(∆Q′(x))]

 ≤L(W 2(Q0,Q ′ 0) +W 2(Q1,Q ′ 1)).
Proof.By the triangle inequality of the Wasserstein distance,

W2(δx,Q c)−W 2(δx,Q ′ c)

 ≤W 2(Qc,Q ′ c)forc∈ {0,1}.
Subtracting the two class scores yields the first inequality. The second inequality follows directly from the Lipschitz
continuity ofϕand Jensen’s inequality.□
Remark.If there exists a reference distributionµ c ∈C c such thatR c(Qc)≤ε c, then
W2(Qc, µc)≤ √εc.
Hence, reconstruction error measured by E(Q 0,Q 1) =R 0(Q0) +R 1(Q1) controls the stability of the induced decision
score up to O(√ε). This provides a geometric interpretation of why minimizing the barycentric objective promotes
behavioral stability under CF-consistent uncertainty.
A.4. Proof of Lemma 3.4
Proof.Fixλ, λ ′ ∈[0,1]and define
gλ(µ) :=W 2 2 (µ, Q⋆ c (λ)).
By definition of the supremum,

Rc(Q⋆ c (λ))−R c(Q⋆ c (λ′))

 =

 sup
µ∈Cc
gλ(µ)−sup
µ∈Cc
gλ′(µ)

≤sup
µ∈Cc

gλ(µ)−g λ′(µ)

.
For any fixed µ∈C c, let a:=W 2(µ, Q⋆ c (λ)) and b:=W 2(µ, Q⋆ c (λ′)). Using the identity |a2 −b 2|=|a−b|(a+b)
together with the reverse triangle inequality forW 2, we obtain

gλ(µ)−g λ′(µ)

 ≤  a+b  W2  Q⋆ c (λ), Q⋆ c (λ′)  .
Next, sinceC c ={µ:W 2(µ, Pc)≤ε c, W2(µ, Pcf )≤δ c}, we have for anyµ∈C c andλ∈[0,1],
W2(µ, Q⋆ c (λ))≤W 2(µ, Pc) +W 2(Pc, Q⋆ c (λ))≤ε c +W 2(Pc, Pcf ),
where the last inequality follows from the fact that (Q⋆ c (λ))λ∈[0,1] is a Wasserstein geodesic between Pc and Pcf . An
analogous bound holds forW 2(µ, Q⋆ c (λ′)). Moreover, by the constant-speed property of the geodesic,
W2

Q⋆ c (λ), Q⋆ c (λ′)  =|λ−λ ′|W 2(Pc, Pcf ).
Combining these bounds yields

gλ(µ)−g λ′(µ)

 ≤2  εc +W 2(Pc, Pcf )  W2(Pc, Pcf )|λ−λ ′|.
Taking the supremum overµ∈C c concludes the proof.
16

RECAST: Model Reconstruction via Counterfactual-Aware Wasserstein Geometry under Limited Data
Algorithm 1Optimization for discrete prototypes used in experiments
Require: Encoded point clouds D0,D 1,D cf ⊂R d; support size M; iterations Tmax; learning rate η; random seed s;
Sinkhorn parametersblur.
Ensure:Prototypes bQ0, bQ1.
1:Set seeds.
2: Define entropic OT surrogate fW 2 2 (·,·) using Sinkhorn with parameters blur and uniform weights for all discrete
measures.
3:foreach classc∈ {0,1}do
4:Deriveλ c using fW 2 2 betweenD cf,D c, andD 1−c.
5:end for
6:
7: Initialization.For each class c∈ {0,1}, randomly sample M points without replacement from Dc to initialize the
support locationsQ c ∈R M×d ; set support weights to uniform (fixed)
8:Initialize Adam optimizer over support locations{Q 0,Q 1}with learning rateη.
9:fort= 1toT max do
10:L 0 ←(1−λ 0) fW 2 2 (Q0,D 0) +λ 0 fW 2 2 (Q0,D cf ).
11:L 1 ←(1−λ 1) fW 2 2 (Q1,D 1) +λ 1 fW 2 2 (Q1,D cf ).
12:L←L 0 +L 1.
13:Take an Adam step on the support locations ofQ 0,Q 1 to minimizeL.
14:end for
15:Set bQ0 ←Q 0
16:Set bQ1 ←Q 1
17:return bQ0, bQ1
A.5. Theoretical Guarantee of Convergence and Sinkhorn Divergence
Let P0,P 1,P cf ∈P 2(X) be probability measures with finite second moments supported on a compact metric space
X⊆R d andλ c ∈[0,1]constants. Assume the optimization is carried out over the 2-Wasserstein spaceW 2(X).
RemarkA.5.Our loss functionLdefined as:
L(Q 0,Q 1) =
X
c∈{0,1}

(1−λ c)W 2 2 (Qc,P c) +λ cW 2 2 (Qc,P cf )  ,
admits a unique minimizer(Q ⋆ 0,Q ⋆ 1)∈P 2(X)×P 2(X).
We can decompose the loss functionL(Q 0,Q 1)in two independent parts
LQ0 +L Q1 ,
with
LQc =

(1−λ c)W 2 2 (Qc,P c) +λ cW 2 2 (Qc,P cf )  ,forc∈ {0,1},
which is essentially a version of a Wasserstein barycenter in Eq. (5) with µ=Q c, λi =λ c,(1−λ c), N= 2 , and µ1 and µ2
the probability measures with finite second moments Pc and Pcf respectively. It is also shown that the optimal solution for
p= 2 , is the geodesic curve provided by the McCann’s interpolant (McCann, 1997; Agueh & Carlier, 2011). As a sum of
two Wasserstein barycentersL(Q 0,Q 1)admits thus an optimal solution(Q ∗ 0,Q ∗ 1).
ApproximationTheoretical results in Sections 3.1- 3.3 are derived for the exact 2-Wasserstein distanceW 2. In practice,
we replace W2 with the Sinkhorn divergence Sϵ to obtain a smooth and computationally efficient objective using entropic
regularization. This corresponds to optimizing a regularized (smoothed) approximation of the Wasserstein barycenter
problem rather than the exact Wasserstein DRO objective. As ϵ→0 , the Sinkhorn divergence converges to W2, and
the solution approaches the true Wasserstein barycenter. For a regularization parameter ϵ, the entropically regularized
Wasserstein distance is defined as follows:
W 2 ϵ,2(µ, ν) := min γ∈Π(µ,ν)
Z
∥y−x∥ 2 2dγ(x, y)
| {z }
transport cost
+ϵH(γ|µ⊗ν)| {z }
relative entropy
,
17

RECAST: Model Reconstruction via Counterfactual-Aware Wasserstein Geometry under Limited Data
Sinkhorn divergence is defined as:
Sϵ(µ, ν) :=W2 ϵ,2(µ, ν)− 1 2 W 2 ϵ,2(µ, µ)−1 2 W 2 ϵ,2(ν, ν).
The modified loss function is then
Lϵ(Q0,Q 1) =
X
c∈{0,1}

(1−λ c)Sϵ(Qc,P c) +λ cSϵ(Qc,P cf )

.
Approximation quality increases as ϵ→0 : W 2 ϵ,2(µ, ν)→W 2 2 (µ, ν), therefore the minimizers of Lϵ(Q0,Q 1) converge to
the minimizers ofL(Q 0,Q 1).
Chizat et al. (2020) show that for ϵ≈n −1/(d′+4), they achieve with probability 1−θ that |Sϵ,n −W 2 2 |≲n −2/(d′+4) +
n−1/2p log(2/θ), with n being the number of independent samples in Rd and d′ denoting 2⌊d/2⌋. When choosing
n≳log(2/θ)ε −(d′+4)/2, they achieve the desired ε-accuracy with 1−θ . Thus they conclude a computational complexity
ofO(n 2/(ϵε)).
A.6. Sensitivity to Sinkhorn Regularization
The Sinkhorn algorithm introduces a regularization parameter ϵ that controls the trade-off between computational efficiency
and approximation of the exact Wasserstein distance.
We ablate the blur parameter on Adult (query size n= 50 ) by sweeping the Sinkhorn blur (ϵ) from 0.2 to 0.005. Fidelity
remains stable across the range of values, while the reference-set mean margin Ex|W2(x, Q∗ 1)−W 2(x, Q∗ 0)| decreases
slightly from 82.66 to 81.08. This indicates that smaller blur leads to a modest reduction in margin, while the predicted
labels remain largely unchanged, signaling stable decision behavior despite changes in regularization.
A.7. Fairness
Let P denote the data-generating distribution over (X, Y, S), where S∈ {0,1}is the sensitive attribute, X the random input
variable, andY∈ {0,1}the class label as a random variable with realizationsy∈ {0,1}.
Demographic parity (Dwork et al., 2012; Feldman et al., 2015) describes that the probability of an individual to be assigned
to a classyshould not depend on the sensitive groupS:
Demographic ParityP( ˆY=y|S= 0) =P( ˆY=y|S= 1).
Equalized Odds (Hardt et al., 2016) describes that the prediction accuracy should not depend on the sensitive groupS:
Equalized Odds
(
P( ˆY= 1|S= 0, Y= 0) =P( ˆY= 1|S= 1, Y= 0)
P( ˆY= 1|S= 0, Y= 1) =P( ˆY= 1|S= 1, Y= 1).
We adaptthreshold-invariant demographic parity disparity(TIDP) andthreshold-invariant equalized odds disparity
(TIEO) from Chen & Wu (2020). Specifically, we definethreshold-invariant demographic parity disparity(TIDP) as the
Wasserstein-1 distance between the score distributions conditioned on different values ofS:
DDTIDP =W 1
 p#P(X|S= 0),
p#P(X|S= 1)

.
Analogously,threshold-invariant equalized odds disparity(TIEO) compares the score distributions conditioned on both S
and the labelY∈ {0,1}:
DDTIEO(y) =W 1
 p#P(X|S= 0, Y=y),
p#P(X|S= 1, Y=y)

.
These diagnostics capture disparities that persist across all decision thresholds, as they operate on entire score distributions.
Moreover, they quantify how different sensitive groups are positioned relative to the barycentric decision geodesic.
18

RECAST: Model Reconstruction via Counterfactual-Aware Wasserstein Geometry under Limited Data
B. Experimental Setup
The following subsections deal with datasets, and implementation as well as experiment details.
B.1. Description and Pre-processing of Real-World Benchmark Datasets
To evaluate our framework, we employ four well-known publicly available tabular datasets:Adult Income,California
Housing,COMPAS, andHELOC. Below are their key characteristics:
• Adult Income: Derived from the 1994 U.S. Census, this dataset captures demographic and financial attributes such
as education level, marital status, age, and annual earnings. The classification task involves predicting whether an
individual’s income exceeds $50,000 (denoted asy= 1). The original dataset consists of 32,561 entries, with 24,720
labeled as y= 0 and 7,841 as y= 1 . To balance the classes, we randomly selected 7,841 samples fromy= 0 , resulting
in a final dataset of 15,682 entries. The dataset includes 6 numerical and 8 categorical features, with the latter converted
to integer encodings. All features were normalized to[0,1].
• California Housing Prices(Housing): The dataset consists of data for houses in a district in California collected in the
1990 census. The dataset consists of 20,640 samples and 9 features. The target variable is the average house value, we
transform it into a binary target variable by setting the median house value as a threshold.
• COMPAS: Developed to study racial bias in recidivism prediction algorithms, this dataset contains 6,172 entries with
20 numerical features. The target variable, is recid divides the data into 3,182 (y= 0 ) and 2,990 (y= 1 ) samples.
Feature values were normalized to[0,1].
• Home Equity Line of Credit(HELOC): This dataset records credit risk assessments for customers seeking home
equity loans. It comprises 10,459 entries, each with 23 numerical features. The prediction target, is at risk
identifies customers likely to default. The dataset is moderately imbalanced, with 5,000 samples for y= 0 and 5,459
fory= 1.
Pre-processing.We adopt a unified data loading and pre-processing pipeline across all datasets. For each dataset, we
construct training, validation, and test splits using stratified sampling, holding out 20% for testing and 20% of the remaining
data for validation. Target labels are standardized by stripping whitespace and removing trailing punctuation where
applicable. Features containing missing indicators (e.g., “?”, or dataset-specific sentinel values) are mapped to NaN, infinite
values are removed, and rows with missing targets are discarded. Features are then automatically partitioned into continuous
and categorical variables based on data type. Continuous features are median-imputed and scaled using a RobustScaler with
the 5–95 percentile range, while categorical features are imputed with the most frequent value and one-hot encoded with
unknown-category handling. All transformations are fit on the training split only and applied to validation and test data. We
further store metadata such as output feature names, continuous and categorical index locations, one-hot category mappings,
and scaler parameters, which are subsequently used both for model training and for decoding counterfactual examples back
into raw feature space. For the California Housing dataset, we follow prior work and binarize the target at the median value
to obtain a balanced binary prediction task.
Importantly, we do not assume access to the target model’s internal pre-processing pipeline.While a unified pipeline is
used within each experimental run to ensure internal consistency, the reconstruction model does not share or reuse the exact
feature transformations employed by the target model. In this sense, pre-processing is treated as an integral part of the
black-box system and is not exposed to the auditor.
We note that most existing model reconstruction and CF-based extraction methods implicitly assume that the attacker
operates in the same feature representation as the target model, and therefore do not explicitly study the effect of pre-
processing or representation misalignment. In practice, however, differences in normalization, encoding, imputation, or
feature engineering can substantially alter the geometry of the input space and thereby impact reconstruction performance.
This distinction is particularly relevant when reproducing prior baselines: we observe that reconstruction fidelity can be
noticeably lower than the values reported in earlier work, which we attribute in part to the absence of shared pre-processing
assumptions. We view this setting as more reflective of realistic auditing scenarios, where the feature transformation pipeline
is typically proprietary and inaccessible.
19

RECAST: Model Reconstruction via Counterfactual-Aware Wasserstein Geometry under Limited Data
B.2. Implementation Details
All experiments were implemented in Python 3.12 and conducted on a workstation equipped with an NVIDIA RTX 3090
GPU, with 124 GB of RAM running on Ubuntu 24.04. We used the following libraries for the implementation: pandas,
scikit-learn, geomloss, numpy, torch and official code for the CF generation methods. Hyperparameters are set
according to a grid search. Our code is included in the supplementary material.
B.3. Experiment Details
The following sections present details regarding the experiment setup.
Target classifiers.Across all datasets, we treat several standard tabular models as black-box target classifiers. Following
the experimental protocol in the main paper, we train a logistic regression model (LR), a multilayer perceptron (MLP), and
tree-based classifiers on the pre-processed feature representations obtained from our ColumnTransformer pipeline. The LR
model is implemented as a single linear layer with a sigmoid output, optimized using Adam and a binary cross-entropy
loss with logits, with early stopping on validation loss. The main MLP consists of two hidden layers with 20 and 10 units,
respectively, with ReLU activations and a dropout rate of 0.1, followed by a single-unit output layer; it is trained with Adam,
a learning rate of10 −3 and weight decay of10 −4, again with early stopping. For tree-based targets, we employ a decision
tree (DT) with maximum depth 6 and minimum leaf size 20. All models are trained on the training split only and evaluated
on the held-out test split using fidelity as the primary metric.
Baselines.We compare our method against several representative reconstruction baselines that incorporate counterfactual
explanations. Most of them are designed for interactive online access, however, since our setting is constrained to offline-only,
we adapt the baselines and restrict them to offline data too. The first baseline,SAMPLES, follows A ¨ıvodji et al. (2020)
and simply augments the observed labeled samples with their CFs, treating CFs as ordinary labeled points when training
standard classifiers such as LR, MLP and DT on the pre-processed features. The second baseline,CCA(Counterfactual
Clamping Attack), implements the counterfactual clamping loss of Dissanayake & Dutta (2024): we train a small neural
surrogate network with hidden layers of sizes (20,10,5) and ReLU activations, followed by a sigmoid output, on tri-valued
labels y∈ {0,0.5,1}, where 0.5 denotes CFs. For regular samples (y∈ {0,1}) we use standard binary cross-entropy, while
CFs are encouraged to have predictions above a threshold k= 0.5 via the clamping objective, which only penalizes CFs
whose predicted probability does not exceed k. For completeness, we also report results for TRA (Khouna et al., 2025),
which is competitive in our setting but restricted to tree-based models; we therefore instantiate TRA only for tree targets and
include it as an additional baseline in the appendix.
CF generation methods.We implement several CF generators in a unified framework. The1-Nearest-Neighbor(1NN)
method searches over a pool of raw samples whose predicted label matches the desired outcome and selects the point with
minimal mixed cost (ℓ1 distance on continuous features plus Hamming distance on categorical features). The differentiable
MCCFvariant optimizes a CF directly in encoded feature space using gradient-based updates on a scaled representation, with
continuous dimensions updated freely and categorical groups projected to (approximate) one-hot vectors via straight-through
Gumbel–Softmax; the objective trades off a prediction loss that pushes the output to the target class against an ℓ1-style
proximity term. OurDiCEimplementation follows a randomized search strategy in encoded space, sampling perturbations
of continuous dimensions and randomly flipping categorical one-hot entries only for a specified subset of features, and
returns the first candidate that achieves the desired prediction with minimal raw-space cost. ForC-CHVAE, we train a tabular
V AE in encoded space and then optimize in the latent space to find codes whose decoded samples both lie close to the
original point (in encoded distance) and are classified as the target label; successful decoded candidates are mapped back to
raw feature space via the inverse preprocessing pipeline. Finally,ROARis implemented as a robust MCCF-style optimizer in
encoded space replacing the standard prediction term with a robust probability under weight noise, aggregating predictions
over multiple noisy parameter draws (either by averaging or worst-case aggregation), while using the same continuous and
categorical distance regularizers; this yields CFs that remain valid under moderate target-model parameter shifts.
As shown in Fig. 2, CF generation methods exhibit substantial variability in the prediction scores assigned by the target
model, with some overshooting the decision threshold. CCA assumes that CFs lie close to the decision boundary and
leverages such near-boundary samples to shape the surrogate decision surface. When CFs instead yield prediction scores
far above 0.5, this assumption is violated and reconstruction performance deteriorates. By contrast, RECAST neither
interprets CFs as true samples (likeSAMPLES) nor assumes proximity to the decision boundary. Instead, it incorporates CF
20

RECAST: Model Reconstruction via Counterfactual-Aware Wasserstein Geometry under Limited Data
information through CF-consistent distributional geometry, which enables stable reconstruction even under heterogeneous
CF generation behaviors.
Wasserstein Barycenter ComputationWe compute entropically regularized Wasserstein costs using the
SamplesLoss("sinkhorn", p=2) implementation from GeomLoss (Feydy et al., 2019), which provides a dif-
ferentiable Sinkhorn approximation of W2 between empirical measures. To construct interpretable class representations, the
experiment leverages 2-Wasserstein distances using the Sinkhorn algorithm implemented in thegeomloss library. The
objective is to learn two barycenters Q0 and Q1 that serve as prototypical representatives of each class in the transformed
feature space. The loss function incorporates the following components: Wasserstein distance from class 0 samples to Q0
and Q1. Each barycenter is initialized with M support points (default M= 50 ). Unless stated otherwise, all experiments
use a fixed support size of M= 50 . Optimization is performed using the Adam optimizer with a learning rate of 0.01
for 200 epochs. The formulation of the loss function follows Equation 3.2 from Section 3, with all Wasserstein distances
replaced by their entropically regularized Sinkhorn surrogates.
Hyperparameter Sensitivity.We conduct an extensive ablation study to assess the sensitivity of RECAST with respect
to its optimization and regularization parameters. Specifically, we perform a grid search over the learning rate η∈
{10−3,5×10 −3,10 −2}, the number of training epochs {100,200,400} . In addition, since Wasserstein barycenters are
computed via an entropically regularized Sinkhorn approximation, we evaluate the effect of the entropic regularization
parameterblur∈ {10−3,5×10 −3,10 −2,5×10 −2}.
Unless stated otherwise, we fix η= 10 −2, blur= 5×10 −2, and train for 200 epochs in all experiments, which we
found to provide stable numerical behavior in practice. Figure 8 illustrates the convergence behavior of the objective in
Equation 3.2 on the Adult dataset under different query sizesk.
Figure 8.Loss convergence over epochs on Adult dataset.
RepetitionAll quantitative analyses were averaged across 10 independent repetitions to account for variability in sampling
and model behavior.
21

RECAST: Model Reconstruction via Counterfactual-Aware Wasserstein Geometry under Limited Data
C. Additional Experiments
This section of the Appendix includes additional experiments, that could not be included in the main paper due to space
limitations.
C.1. Ablation Study
We conduct a ablation study to assess RECAST with respect to its design choices. First, we analyze the role of the
class-conditional weighting λc by selectively disabling each component. As shown in Table 4, removing either component
degrades fidelity, while disabling both leads to substantial performance loss, highlighting their complementary roles. Second,
we replace Wasserstein barycenters with other prototype constructions, such as the Euclidean mean, medoid-based prototypes
and MMD. Here, CFs can only be included as labeled data. We emphasize that this difference is not a design choice but a
structural limitation of the compared prototype representations. Euclidean mean and medoid prototypes operate on point
estimates and do not admit a natural mechanism to incorporate CFs as soft, distributional constraints. These alternatives
consistently underperform, particularly in low-query regimes, underscoring the importance of Wasserstein geometry for
capturing CF-induced distributional structure. However, MMD can be plugged in our design easily with similar λc, with
only Wasserstein distance changed to MMD. Finally, we evaluate the effect of counterfactual information by removing CFs
from the reconstruction. As shown in Table 4, excluding CFs leads to a substantial drop in fidelity, supporting their role in
shaping boundary-relevant geometry rather than pinpointing the boundary itself. Sensitivity to optimization hyperparameters
(learning rate and training epochs) is reported in Appendix C.
Table 4.Ablation study of RECAST (Adult, MLP, query size = 100).
Method Variant CFs Prototypeλ c Loss↓Fidelity (%)↑
RECAST (Full)✓Wasserstein Ours2.18 90.8
Fixed λc 1−λc ✓Wasserstein λc 1−λc = 0.52.61 88.7
Euclidean prototype✓Euclidean mean – 3.12 82.4
Medoid prototype✓Medoid – 2.88 84.1
Maximum Mean Discrepancy✓RBF-MMD Similar to Ours 2.65 87.3
No CFs×Wasserstein – 3.05 81.6
C.2. Imbalanced Data
In our main experiments, we used the same value of query size for D0, D1, and Dcf. To evaluate the robustness of our
approach under imbalanced data conditions, we conducted additional experiments using varying sample sizes for the
counterfactual dataset. These experiments simulate more realistic, unbalanced settings in which the sizes of D0, D1, and
Dcf may differ, while the total number of natural samples satisfies |D0|+|D 1|= 200 . As shown in Table 5, our method
maintains strong performance even under these imbalanced conditions.
Table 5.Fidelity under different class imbalance ratios.
20% class 0 : 80% class 1 80% class 0 : 20% class 1
Dataset SAMPLES CCA RECAST (Ours) SAMPLES CCA RECAST (Ours)
Adult In. 0.751±0.017 0.793±0.0180.848±0.030 0.702±0.016 0.762±0.0230.819±0.027
COMPAS 0.385±0.007 0.715±0.0180.795±0.020 0.352±0.011 0.638±0.0220.738±0.025
HELOC 0.397±0.014 0.604±0.0520.646±0.071 0.365±0.016 0.561±0.0450.592±0.059
Housing 0.429±0.0080.666±0.065 0.662±0.112 0.391±0.0100.624±0.0570.615±0.088
C.3. Experiments including Accuracy
Table 6 reports target model accuracy alongside surrogate accuracy and fidelity for RECAST, SAMPLES, and CCA on
the Adult and COMPAS datasets at query sizes n= 100 and n= 150 , using logistic regression as the target model and
1-nearest-neighbor as the CF method. We report both metrics because they capture different objectives: accuracy measures
predictive performance against ground-truth labels, whereas fidelity measures agreement with the target model’s predictions,
including its errors. Consequently, the two metrics need not correlate, a surrogate can achieve high fidelity while having
lower task accuracy if the target model itself makes systematic errors. RECAST achieves the highest fidelity across both
22

RECAST: Model Reconstruction via Counterfactual-Aware Wasserstein Geometry under Limited Data
Table 6.Target model accuracy, surrogate accuracy, and fidelity at query sizes n= 100 and n= 150 on Adult and COMPAS. Accuracy
and fidelity need not correlate: fidelity measures agreement with the target model’s predictions (including its errors), not ground-truth
label accuracy. Best surrogate results per dataset and query size inbold.
Dataset Method Target Acc. n= 100n= 150
Acc. Fid. Acc. Fid.
Adult
Samples 0.8463 0.7463 0.7800 0.7488 0.7679
CCA 0.8463 0.5598 0.5097 0.5318 0.4797
RECAST 0.84630.7741 0.8400 0.7700 0.8600
COMPAS
Samples 0.66960.59830.7004 0.5424 0.7518
CCA 0.6696 0.5405 0.5441 0.5376 0.5398
RECAST 0.6696 0.55800.7560 0.5770 0.7860
Table 7.Accuracy and fidelity on Folktables (ACSIncome) under cross-domain distribution shift (train: CA 2018, evaluate: MI 2014) at
query sizes 100 and 150.
Reconstruction Query size = 100 Query size = 150
Acc. Fid. Acc. Fid.
SAMPLES0.73560.86410.74990.8596
CCA 0.7302 0.6362 0.7251 0.6251
RECAST 0.64730.86610.72540.8886
datasets and query sizes, while remaining competitive on accuracy, demonstrating that behavioral agreement with the target
is not achieved at the expense of predictive performance.
C.4. Additional Experiments on Distribution shifts
To investigate robustness under realistic distribution shift, we conduct an additional experiments using Folkstables (Ding
et al., 2021). We train a logistic-regression target model on ACSIncome data from California (CA), 2018 (acc=0.7860),
and evaluate reconstruction under shift to Michigan (MI), 2014, a setting that combines both geographical and temporal
variation. We generate CFs using 1-nearest-neighbour and evaluate the performance (fidelity and accuracy) on query budget
(100, 150).
Results are shown in Table 7. RECAST consistently achieves higher fidelity across query budgets (100 and 150), demonstrat-
ing robust recovery under distribution shift. SAMPLES leads on accuracy but trails substantially on fidelity, consistent with
the pattern observed in Section C.3, accuracy and fidelity capture different objectives, and fidelity is the primary measure
of reconstruction quality. These results demonstrate that RECAST maintains strong behavioral consistency even under
substantial distribution shifts.
C.5. Crossover Between RECAST and No-CF Reconstruction
We investigate when CF supervision becomes less critical for model reconstruction under increasing data availability.
Specifically, we compare RECAST with a no-CF baseline trained solely on natural samples, as the number of available
samples grows.
We fix a target model trained on the Adult dataset and evaluate reconstruction fidelity, defined as the fraction of test instances
on which the surrogate and the target model produce identical predictions. For the no-CF baseline, we use a decision tree
surrogate, which exhibits stable behavior in low-sample regimes while allowing increased expressivity as more data become
available.
Figure 9 illustrates a crossover pattern. In low-data regimes, CF-based reconstruction achieves substantially higher fidelity,
highlighting its strong sample-efficiency advantage. As the number of natural samples increases, the performance gap
narrows and reverses aroundn≈1000samples per class, where the no-CF surrogate attains comparable or higher fidelity.
This pattern reflects a trade-off between data efficiency and surrogate expressivity in audit-oriented reconstruction settings.
Counterfactual supervision provides informative local constraints when observational data are scarce, but yields diminishing
benefits once sufficient coverage of the input space is available.
23

RECAST: Model Reconstruction via Counterfactual-Aware Wasserstein Geometry under Limited Data
Figure 9.Crossover between CF-based and no-CF reconstruction on the Adult dataset. CF-based reconstruction achieves higher fidelity in
low-data regimes, while the no-CF decision tree surrogate improves with increased natural samples and surpasses the CF-based method
aroundn≈1000per class.
C.6. Data Modalities / High-Dimensional Data
Our framework is generally applicable to any data modality that can be embedded as vectors, e.g., pixel representations of
visual data. Thus, we can apply RECAST to high-dimensional datasets after transforming the input data to latent space.
To show this, we perform an additional proof-of-concept on the well-known MNIST dataset (Deng, 2012). We load
the dataset from the sklearn library, normalize the pixel values to be in-between [0,1] and reduce the classification
problem to binary (e.g., classification between 0 and 1). For the target classifier, we employ 66% to train a standard sklearn
MLP-classifier and generate CFs as the nearest neighbor belonging to the other class. RECAST is then trained on a subset
of the training set in pixel-space (d= 784 ). Across different binary tasks and sample sizes (around 100 - 500), RECAST
consistently achieves a fidelity around 0.7 or higher, see Figure 10.
C.7. Language Case Study: Reconstruction under One-Sided Textual CFs
We present an exploratory case study on reconstruction for text-based classifiers under limited access. The target model is a
binary classifier m:R d → {0,1}trained on fixed text embeddings. Texts x∈X are mapped to embeddings ψ(x)∈R d
using a frozen LLM-based encoder. During reconstruction, the target model is accessed only through discrete label queries
m(ψ(x)).
Representation space.Since optimal transport is not defined over raw text, all reconstruction is performed in the
embedding space induced byψ. The embedding model is fixed and shared across all methods.
100 200 300 400 500
Sample Size (Both Classes)
0.70
0.75
0.80
0.85
0.90
0.95
1.00Fidelity
0-1
0-8
1-7
3-5
3-6
3-8
4-7
5-8
Figure 10.Fidelity results for various sample sizes and binary classification problems within the MNIST dataset.
24

RECAST: Model Reconstruction via Counterfactual-Aware Wasserstein Geometry under Limited Data
0 500 1000 1500 2000
Sample Size (Both Classes)
20
40
60Runtime (seconds)
Dataset
MNIST
Adult
Adult (10)
Adult (50)
Figure 11.Runtime for RECAST across different datasets and configurations. Each RECAST model is trained for 500 epochs.
Task and target model.We consider a toxicity classification task (Jigsaw, 2018). A binary classifier m is trained on
embeddingsψ(x)obtained from a standard toxicity dataset and is treated as a black-box model during reconstruction.
One-sided textual CFs.To emulate one-sided recourse, CFs are generated only for toxic instances with m(ψ(x)) = 0. For
each such input x, a single textual CF xcf is produced using an LLM-based rewriting prompt that aims to minimally modify
the text toward a non-toxic outcome. The resulting text is embedded via ψ, and the CF is retained only if m(ψ(xcf )) = 1.
This yields three offline datasets:D 0 ={x:m(ψ(x)) = 0},D 1 ={x:m(ψ(x)) = 1}, andD cf ={x cf :x∈D 0}.
Reconstruction .We apply RECAST in the embedding space to compute class prototypes Q0 and Q1 using the barycentric
objective.
Evaluation.We evaluate query budgets of 100, 150, and 200 samples per class. Reconstruction fidelity is consistently
lower than in tabular settings, typically saturating around 80%. We attribute this to strong representation compression: text
inputs are mapped to fixed embeddings and further reduced to a50-dimensional space.
C.8. Runtime
To investigate runtime, we vary the number of samples used to train RECAST. The runtime experiments are performed on a
MacBook Pro with 24 GB RAM and an Apple M4 Pro. We first split the full dataset in 33% test and 67% training data. Then
we take different fractions, of the training set to train RECAST. We include MNIST (d= 784 ) and three versions of adult
(d= 14 before pre-processing, d= 104 with one-hot-encoding) with varying feature sets (d= 104, d= 50, d= 10) to
account for different sample dimensionalities. Each RECAST instance is trained for 500 epochs. Note that implementation
improvements like early stopping could improve these runtimes, however we want to focus on a fair comparison and trained
each instance the same amount of epochs. To mitigate influence of background tasks, we performed 5 runs per configuration.
While the complexity of our approach is high in theory, we observe, see Figure 11, that the runtime in practice grows near
linear with the number of samples. We additionally see that the number of features, compare adult with 104, 50, and 10
features, has even less impact on the runtime.
25
