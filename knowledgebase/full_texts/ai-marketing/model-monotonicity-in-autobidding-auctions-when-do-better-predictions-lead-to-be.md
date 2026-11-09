---
title: 'Model Monotonicity in Autobidding Auctions: When Do Better Predictions Lead to Better Outcomes?'
url: https://arxiv.org/abs/2605.31036
category: ai-marketing
subcategory: measurement
date: 2026-05
venue: ''
authors:
- Ashwinkumar Badanidiyuru
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.31036
pages: 18
chars: 65576
fetched_at: '2026-11-08T13:28:42+00:00'
kb_version: 1
---

# Model Monotonicity in Autobidding Auctions: When Do Better Predictions Lead to Better Outcomes?

Model Monotonicity in Autobidding Auctions:
When Do Better Predictions Lead to Better Outcomes?
Ashwinkumar Badanidiyuru 1
Abstract
Online advertising platforms rely on machine
learning models to predict click-through rates
(pCTR) and conversion rates (pCVR) for auction
mechanisms. We introduce a novel framework
to study the interaction between recommender
system model quality, auction format, and au-
tobidder behavior. We formalize when model
improvements—defined via a refinement relation
inspired by filtrations in probability theory—lead
to improvements in platform-level Evaluation Cri-
teria Metrics (ECM) such as revenue, welfare, or
liquid welfare. Our main contributions are: (1) a
formal definition of model improvement based on
cluster refinement, and (2) a systematic charac-
terization of ECM monotonicity across different
combinations of bidder types (tCPA, max-CPA),
auction formats (first-price, second-price, VCG),
and budget constraints. We show that first-price
auctions with uniform bidding guarantee revenue
monotonicity for tCPA bidders without budgets
(via Jensen’s inequality), while second-price auc-
tions and budget constraints can break this prop-
erty. We provide full numerical constructions for
the non-monotonicity results. Our findings have
practical implications for advertising platforms
seeking to align model improvements with busi-
ness outcomes.
1. Introduction
Online advertising platforms generate hundreds of billions
of dollars in annual revenue by matching advertisers with
users through sophisticated auction mechanisms. At the
heart of these systems lies a critical interplay between three
components: (1) machine learning models that predict user
1Uber Technologies, Inc., San Francisco, CA, USA.
Correspondence to: Ashwinkumar Badanidiyuru <ashwinku-
marbv@uber.com>.
Proceedings of the 43 rd International Conference on Machine
Learning, Seoul, South Korea. PMLR 306, 2026. Copyright 2026
by the author(s).
behavior, such as click-through rate (pCTR) and conversion
rate (pCVR) models; (2) auction mechanisms that allocate
ad impressions and determine prices; and (3) autobidding
systems that bid on behalf of advertisers according to their
specified objectives. Understanding how improvements in
one component propagate through this system to affect
platform-level outcomes is essential for both theoretical
understanding and practical system design.
Advertising platforms continually invest in improving their
prediction models, with the natural expectation that better
predictions lead to better outcomes. However, the relation-
ship between model quality and platform metrics is far from
straightforward. When a platform deploys a more accu-
rate pCTR model, the change affects not only the auction
mechanism’s allocation decisions but also the behavior of
autobidders, which adapt their bidding strategies to the new
predictions. This creates a complex feedback loop where
the ultimate effect on platform metrics—such as revenue,
advertiser welfare, or efficiency—depends on the intricate
interaction between all three components.
1.1. Motivation and Central Question
Consider a platform that improves its conversion prediction
model, enabling finer-grained distinctions between users.
Intuitively, one might expect that more accurate predictions
should lead to more efficient allocations and higher revenue.
Yet this intuition can fail. A refined model may enable some
autobidders to target only the most valuable impressions
more precisely, potentially reducing the competitive pres-
sure that drives revenue. Alternatively, budget-constrained
advertisers might exhaust their budgets more quickly on
high-value users, leaving lower-value users unserved. These
scenarios illustrate that the relationship between model qual-
ity and platform outcomes is subtle and depends critically
on the auction format, bidder objectives, and resource con-
straints.
This motivates our central research question:When do im-
provements in prediction models lead to improvements in
platform-level Evaluation Criteria Metrics (ECM)?We re-
fer to this property asECM monotonicityor simplymodel
monotonicity. Understanding when this property holds—
and when it fails—has significant implications for platform
1
arXiv:2605.31036v1  [cs.GT]  29 May 2026

Model Monotonicity in Autobidding Auctions
design, model deployment decisions, and the alignment of
technical improvements with business objectives.
1.2. Our Contributions
We make two main contributions in this paper:
Novel Problem Formulation.We introduce a formal
framework for studying the interaction between model qual-
ity, auction mechanisms, and autobidder behavior. Central
to our approach is a definition ofmodel refinementinspired
by filtrations in probability theory. We model prediction
systems as partitioning a universe U of users into clusters,
where the model predicts the average conversion probability
for each cluster. A model MA refinesa model MB if each
cluster of MA is contained in a cluster of MB—that is,
MA makes finer distinctions between users. This definition
captures the intuitive notion that MA provides “more infor-
mation” than MB, while being mathematically tractable for
analysis.
Within this framework, we consider two types of autobidders
that reflect common industry practice:
• Target CPA (tCPA) bidders: Advertisers specify a
target cost-per-acquisition and seek to maximize con-
version volume subject to maintaining an average CPA
at or below their target.
•MAX-CPA bidders: Advertisers specify a maximum
willingness-to-pay per conversion and seek to maxi-
mize total value, where each conversion’s value equals
the advertiser’s maximum CPA.
Following standard autobidding practice (Aggarwal et al.,
2024), we assume tCPA targets equal true per-conversion
values (vi =t i), ensuring welfare equals revenue for tCPA
bidders without budgets under FPA with multiplier µi = 1.
We study these bidder types across multiple auction formats
(first-price, VCG—which is equivalent to second-price for
single-item auctions) and under both unconstrained and
budget-constrained settings.
Systematic Characterization of ECM Monotonicity.
We provide a comprehensive analysis of when model re-
finement leads to improvements in platform-level metrics,
with our systematic characterization in Table 1. We find
that monotonicity israre—only three settings guarantee it:
(1) tCPA bidders without budgets under FPA (via Jensen’s
inequality), (2) MAX-CPA bidders without budgets under
VCG (welfare only), and (3) LP-based fractional alloca-
tion with budgets (welfare monotonic; for tCPA, surrogate
revenue also monotonic; not incentive compatible). In all
remaining settings studied—including VCG for tCPA bid-
ders and FPA with budget constraints—monotonicity fails.
We provide explicit numerical constructions for these non-
monotonicity results.
Key Insights.Our results yield several insights: (1) Mono-
tonicity is rare—only three settings guarantee it, so plat-
forms should not assume model improvements translate to
metric improvements. (2) FPA provides the only revenue
monotonicity guarantee (for tCPA without budgets), while
VCG provides the only welfare guarantee (for MAX-CPA
without budgets). (3) A fundamental trade-off exists be-
tween incentive compatibility and monotonicity with budget
constraints. (4) Model improvements should be validated
through simulation or A/B testing.
Conflict of Interest Disclosure.The author is employed
by Uber, which operates advertising systems that use auction
mechanisms.
2. Related Work
Our work studies model monotonicity in autobidding auc-
tions, connecting several research areas. We briefly survey
the most relevant literature, referring readers to standard
references for foundational concepts.
Autobidding.The theoretical study of autobidding was
initiated by Aggarwal et al. (2019), who analyzed con-
strained autobidding and established foundational equilib-
rium concepts. Aggarwal et al. (2024) provide a compre-
hensive survey covering equilibrium analysis, mechanism
design, and learning in autobidding systems. Recent work
extends to multi-channel settings (Deng et al., 2023) and
dynamics with budget and ROI constraints (Lucier et al.,
2024). These works analyze autobidder behavior given fixed
prediction models; our work studies how changes in model
quality affect equilibrium outcomes.
First-Price Auctions and Pacing.The shift to first-price
auctions has motivated substantial work on pacing equilibria
(Conitzer et al., 2022) and efficiency in non-truthful settings
(Liaw et al., 2023; 2024). Deng et al. (2024) empirically
study bid-scaling strategies across auction formats. Our
positive result for tCPA bidders under FPA connects to this
literature, while our negative results highlight limitations of
first-price mechanisms.
VCG and Welfare.The VCG mechanism (Vickrey, 1961;
Clarke, 1971; Groves, 1973) achieves welfare-optimal allo-
cations with dominant-strategy incentive compatibility. Our
welfare monotonicity result for MAX-CPA bidders under
VCG builds on these classical efficiency properties. Mehta
(2022) shows that randomization can improve efficiency
beyond VCG in autobidding contexts.
2

Model Monotonicity in Autobidding Auctions
Value Maximizers and Liquid Welfare.Max-CPA bid-
ders are a form of value maximizers (Wilkens et al., 2016).
For budget-constrained settings, liquid welfare (Dobzin-
ski & Paes Leme, 2014) provides an appropriate efficiency
benchmark; Colini-Baldeschi et al. (2026) study optimal liq-
uid welfare guarantees for autobidding agents with budgets.
Our negative results for budget-constrained settings show
that even liquid welfare fails to be monotonic.
Prediction Models in Advertising.Vasile et al. (2017)
observe that prediction accuracy may not align with busi-
ness objectives due to downstream auction effects—a theme
central to our work. While prior work focuses on learning
better predictions or bidding strategies (Ma et al., 2018; Cai
et al., 2017), we study when improving predictions actually
improves platform outcomes.
Positioning.To our knowledge, this is the first work to
formally study when prediction model improvements guar-
antee platform metric improvements in autobidding settings.
Our key finding—that monotonicity holds only in a small
set of specific cases—provides theoretical foundations for
understanding the complex dynamics of model deployment
in advertising platforms.
3. Model Definition and Problem Setting
We formalize the problem setting for studying the interac-
tion between prediction model quality and platform-level
outcomes in autobidding auctions. Our framework draws
on concepts from probability theory, specifically filtrations
and refinements (Hardy et al., 1952; Durrett, 2019).
3.1. Problem Setting
We consider an online advertising platform that hosts auc-
tions to display advertisements to users. Let U denote the
user universe, a finite set of users. Each user u∈ U and
advertiser i∈ Aare associated with true (unobservable) be-
havioral parameters ctri(u),cvr i(u)∈[0,1] representing
click-through and conversion rates for that advertiser–user
pair.
A set of advertisers A={1, . . . , n}compete for ad slots,
each with private value vi ∈R ≥0 per conversion and con-
straints such as target CPA (tCPA) or maximum CPA. Adver-
tisers employautobiddingsystems (Aggarwal et al., 2019;
2024) that automatically determine bids based on the plat-
form’s predicted values pCTR(u)and pCVR(u).
Assumption 3.1(Value Equals Target for tCPA Bid-
ders).For target CPA (tCPA) bidders, we assume the per-
conversion value vi equals the target ti. This ensures that,
without budget constraints and under first-price auctions
with multiplier µi = 1 , welfare equals revenue for tCPA
bidders, since the expected value vi ·p i,C equals the target
paymentt i ·p i,C.
3.2. Prediction Models
We formalize prediction models using a partition-based
framework that captures prediction granularity.
Definition 3.2(User Partition).Apartitionof U is a col-
lection P={C 1, . . . , Ck} of non-empty, pairwise disjoint
subsets with Sk j=1 Cj =U . For each cluster C∈ P, we de-
fine itsweight wC :=|C|/|U |, representing the probability
mass (or relative size) of cluster C under the uniform user
distribution.
Definition 3.3(Prediction Model).Aprediction model M
is defined by a partition PM of U. For each advertiser
i∈ Aand cluster C∈ PM, the model outputs thepredicted
conversion probability:
pi,C := 1 |C| X u∈C pi(u),(1)
where pi(u) = ctri(u)·cvr i(u) is the true conversion prob-
ability for advertiser i and user u. This quantity pi,C is the
primitive used in all auction analysis: bidders bid based on
pi,C, and all theoretical results in this paper are stated in
terms ofp i,C.
This definition captures the intuition that a prediction model
groups users into clusters and assigns the same predicted
conversion probability to all users within a cluster. The
model iscalibrated: predictions equal true cluster aver-
ages (Ma et al., 2018; Gneiting & Raftery, 2007). Crucially,
this paper studies the effect ofrefining a perfectly calibrated
information structurerather than the effect of stochastic
prediction error or miscalibration. (See Section A.1 for
implementation details.)
Example 3.4(Extreme Models).Thecoarsest model
P={U } predicts a single global average: pi,U =
1
|U |
P
u∈U pi(u) for all advertisers i. Thefinest model
P={{u}:u∈ U } predicts exact advertiser-specific
conversion probabilities: pi,{u} =p i(u) for each user u and
advertiseri.
3.3. Model Refinement
We define when one prediction model is “better” than an-
other, inspired by filtrations in probability theory (Durrett,
2019). Unlike pointwise metrics (log-likelihood, AUC),
model refinement provides a partial order under which
proper scoring losses improve in expectation for calibrated
nested partitions, enabling provable guarantees.
Definition 3.5(Model Refinement).A prediction model
MA refinesmodel MB (written MA ⪰ MB) if every
cluster in PMA is contained in some cluster of PMB. We
say thatM A isfinerandM B iscoarser.
3

Model Monotonicity in Autobidding Auctions
This captures feature-set refinements: for example, a model
segmenting users by {age, location} induces a coarser parti-
tion than a model that additionally uses {browsing history},
provided the added feature only splits existing clusters.
The refinement relation forms a partial order (reflexivity,
transitivity, antisymmetry follow from standard set theory).
In probability theory, a finer partition corresponds to a finer
σ-algebra, capturing the idea that a finer model has access
to more discriminative information.
The refinement definition captures a strong notion of model
improvement: if MA ⪰ MB, then for any advertiser i and
any concave Bayes risk H associated with a proper scoring
loss,
X
C∈PMA
wCH(p i,C)≤
X
C∈PMB
wCH(p i,C).
This follows from Jensen’s inequality because each coarse
prediction is the weighted average of the refined predictions
within that coarse cluster. Thus refinement improves all
proper scoring losses in their loss orientation (Gneiting &
Raftery, 2007).
3.4. Evaluation Criteria Metric (ECM)
Definition 3.6(Evaluation Criteria Metric).AnEvaluation
Criteria Metric( ECM) aggregates auction outcomes. For a
model M, let xi(u;M)∈ {0,1} denote the allocation and
πi(u;M)≥0 the payment for advertiser i on user u. We
consider:
•Revenue:Revenue(M) := P u∈U P i∈A πi(u;M)
• Welfare: Welfare(M) := P u∈U P i∈A xi(u;M)·
vi ·p i,u
• Liquid Welfare: LiquidWelfare(M) :=P
i∈A min (Bi, P u xi(u;M)·v i ·p i,u)
Here pi,u denotes the true conversion probability for adver-
tiser i and user u, and Bi is advertiser i’s budget (Dobzin-
ski & Paes Leme, 2014). In proofs, we write metrics as
weighted sums over clusters (see Section A.1).
For each setting, let Φsetting(M) denote the outcome map-
ping that selects allocations and payments induced by model
Munder that setting’s behavioral convention.
Definition 3.7(ECM Monotonicity).An ECM ismonotone
with respect to model refinement for a given auction format
and bidder type if, for all models MA,M B with MA ⪰
MB: ECM(Φsetting(MA))≥ECM(Φ setting(MB)), where
the ECM is evaluated on the allocations and payments se-
lected by the outcome mapping for that setting (see Theo-
rem 4.10).
Remark3.8 (Setting-Dependent Outcome Mappings).The
outcome mapping Φsetting :M →(allocations,payments)
varies by setting. For tCPA settings, Φ selects equilibrium
outcomes under the binding-constraint convention. For
MAX-CPA FPA,Φ compares designated feasible multiplier
profiles across models without claiming a full equilibrium
characterization. Our characterization in Table 1 is thus a
taxonomy of Φ-monotonicity results across these conven-
tions. This heterogeneity reflects the different behavioral
assumptions appropriate to each setting.
3.5. Central Question
We study which combinations of (auction format, bidder
type, ECM) exhibit monotonicity:
• Auction formats:First-price (FPA), VCG mechanism
(equivalent to SPA for single-item auctions).
• Bidder types:Target CPA (tCPA) and Maximum CPA
(max-CPA).
•Budget constraints:Present or absent.
Central Question:For which combinations is the ECM
monotone with respect to model refinement?
A positive answer ensures that better models lead to better
outcomes. A negative answer reveals misalignment: improv-
ing predictions can paradoxically hurt platform objectives.
We provide a systematic characterization in Section 5, with
proofs for positive results and numerical constructions for
non-monotonicity results.
4. Auction Mechanisms and Bidder Models
We formalize the auction mechanisms and bidder models
underlying our analysis. For comprehensive background on
auction theory, see Krishna (2009); for autobidding systems,
see Aggarwal et al. (2019).
4.1. Auction Environment
Consider advertisers A={1, . . . , n}competing for impres-
sions across a user population partitioned into clusters P
by prediction model M. For each advertiser i and cluster
C, the platform observes predicted conversion probability
pi,C, defined as the cluster-averaged conversion probability
(Theorem 3.3). We assume the model is well-calibrated
within each cluster.
4.2. Bidder Models
Definition 4.1(tCPA Bidder).Atarget cost-per-acquisition
(tCPA)bidder i has target ti >0 and seeks to maximize
conversions subject to average cost per conversion≤t i.
4

Model Monotonicity in Autobidding Auctions
Definition 4.2(MAX-CPA Bidder).Amaximum cost-per-
acquisition (MAX-CPA)bidder i has per-conversion value
vi >0 and maximizes total expected value (conversions
times vi) minus total payment. This bidder obtains positive
surplus from an impression only when expected cost per
conversion satisfies π/pi,C ≤v i, where π denotes the per-
impression payment.
The key distinction: tCPA bidders maximize conversions
subject to an average cost constraint; MAX-CPA bidders
maximize quasi-linear utility (value minus payment). Either
type may have a budget constraint Bi >0 limiting total
expenditure.
4.3. Uniform Bidding
Definition 4.3(Uniform Bidding).Underuniform bidding,
bidder i selects multiplier µi ≥0 and bids bi(C) =µ i ·t i ·
pi,C (tCPA) orb i(C) =µ i ·v i ·p i,C (MAX-CPA).
For MAX-CPA bidders, we define theeffective multiplier
gi :=µ i ·v i, so bids simplify tob i(C) =g i ·p i,C.
Lemma 4.4(Optimal Multiplier for tCPA in FPA).For
a tCPA bidder without budget constraints in a first-price
auction, the optimal uniform multiplier isµ ∗ i = 1.
Proof Sketch. In FPA with uniform bidding bi(C) =µ i ·
ti ·p i,C, the CPA in any won cluster is µi ·t i. Thus µi ≤1
is required for feasibility. Since conversions increase with
µi, the optimal choice isµ i = 1.
4.4. Auction Formats
Definition 4.5(First-Price Auction (FPA)).The highest
bidder wins and pays their bid: i∗ = arg maxi bi, payment
πi∗ =b i∗. (Ties broken by lowest index.)
Definition 4.6(Second-Price Auction (SPA)).The high-
est bidder wins and pays the second-highest bid: i∗ =
arg maxi bi, paymentπ i∗ = maxj̸=i∗ bj.
Remark4.7 (SPA-VCG Equivalence).For single-item auc-
tions, SPA and VCG are equivalent mechanisms: both allo-
cate to the highest bidder and charge the second-highest bid.
The VCG payment equals the externality imposed on other
bidders, which for a single item is precisely the second-
highest bid. Hence, all results stated for VCG in single-item
settings apply equally to SPA.
Definition 4.8(VCG Mechanism).VCG computes the
welfare-maximizing allocation and charges each winner
their externality (the welfare loss imposed on others).
Definition 4.9(LP Allocation Benchmark).TheLP al-
location benchmarkis a centralized fractional allocation-
and-payment rule that directly chooses allocation variables
xi,C ∈[0,1] subject to supply and budget feasibility con-
straints. Unlike FPA, SPA, or VCG, this benchmark is not a
strategic auction mechanism: it assumes the platform knows
the relevant bidder parameters and optimizes allocations and
surrogate payments directly. We use it only as a comparison
point for monotonicity under budget constraints.
4.5. Evaluation Criteria Metrics
We use the revenue, welfare, and liquid welfare metrics from
Theorem 3.6. In the auction analysis, welfare is written
cluster-wise as P i E[1[iwins]·v i ·p i,C], and liquid welfare
caps each bidder’s contribution at their budget.
4.6. Equilibrium Concept
Assumption 4.10(Equilibrium Convention).Bidders
choose uniform multipliers µi to optimize their objective
(conversions subject to CPA ≤t i for tCPA; quasi-linear
utility for MAX-CPA) taking others’ multipliers as given.
We assume an equilibrium exists. When multiple equilibria
preserve the same allocation, our positive results hold for
all such equilibria; counterexamples exhibit one valid equi-
librium (typically with binding CPA constraints for trans-
parency), except for MAX-CPA FPA which uses designated
feasible multiplier profiles without a full equilibrium claim.
For FPA with tCPA bidders, symmetric equilibrium corre-
sponds toµ i = 1(truthful bidding).
5. Main Results
This section presents our main theoretical contributions: a
systematic characterization of when model refinement leads
to improved platform metrics. We state all positive results
with proof sketches (full proofs in Section A) and reference
the detailed numerical constructions in Section 6 for non-
monotonicity results.
5.1. Summary of Results
Our main finding is that ECM monotonicity depends crit-
ically on the interaction between three factors: (1) bidder
type (tCPA vs. MAX-CPA), (2) auction format (FPA, SPA,
VCG), and (3) presence of budget constraints. Table 1 sum-
marizes our systematic characterization. The table reports
the auction and benchmark settings analyzed in this paper,
rather than an exhaustive enumeration of every possible bud-
geted mechanism variant. Note that monotonicity is defined
relative to a setting-dependent outcome mappingΦsetting; see
Theorem 3.8 for details on how outcomes are determined in
each row.
1For unconstrained settings, welfare is standard social welfare.
For budget-constrained settings, welfare refers to liquid welfare
(Theorem 3.6), which caps each bidder’s contribution at their bud-
get.Outcome selection:For tCPA auction settings (rows 1–3),
ECM is evaluated at equilibrium multipliers where the binding
constraint (CPA or budget) determines each bidder’s multiplier;
5

Model Monotonicity in Autobidding Auctions
Table 1.Monotonicity of ECM under model refinement.
✓indicates monotonicity holds; × indicates a non-monotonicity
construction exists; — indicates metric not defined for this setting.
Results assume uniform bidding. For budget-constrained settings,
welfare refers to liquid welfare.1
Bidder Type Auction Revenue Welfare
tCPA FPA✓ ✓
tCPA VCG (= SPA)× ×
tCPA + Budget FPA× ×
tCPA + Budget LP✓ ✓
MAX-CPA FPA † × ×
MAX-CPA VCG×✓
MAX-CPA + Budget FPA † × ×
MAX-CPA + Budget LP —✓
5.2. Positive Results: Monotonicity Guarantees
We begin with our positive results, establishing conditions
under which model refinement provably improves platform
metrics.
5.2.1. FIRST-PRICEAUCTION WITH TCPA BIDDERS
Our first main result shows that FPA with tCPA bidders and
uniform bidding satisfies revenue monotonicity.
Theorem 5.1(FPA Revenue Monotonicity).Consider tCPA
bidders without budget constraints using uniform bidding
with optimal multiplier µi = 1 in a first-price auction. If
model MA is a refinement of modelMB (i.e., MA ⪰ MB),
then:
Rev(MA)≥Rev(M B).(2)
Proof Sketch. With µi = 1, bidder i bids bi(C) =t i ·p i,C,
so revenue is Rev(M) = P C∈P wC ·max i ti ·p i,C. The
function f(p) = max i ti ·p i is convex. When MA refines
MB, each coarse cluster C B splits into sub-clusters with
weights summing to wCB and calibration-preserving proba-
bilities. By Jensen’s inequality applied to this convex f, the
finer model’s revenue cannot be smaller. See Section A for
the complete proof.
The following theorem establishes that uniform bidding
with µ= 1 is optimal for tCPA bidders in FPA who seek to
maximize conversions subject to their tCPA constraint.
Theorem 5.2(FPA Optimality for tCPA Bidders).For tCPA
bidders without budget constraints in a first-price auction,
uniform bidding with multiplier µi = 1 (i.e., bidding bi =
ti ·p i,C) is:
when unconstrained, µ= 1 is used. The dagger marks the MAX-
CPA FPA rows (rows 5 and 7), where ECM compares designated
feasible multiplier profiles across models without a full equilib-
rium claim (see Theorem 4.10); for MAX-CPA VCG (row 6),
equilibrium multipliers are used. For tCPA + Budget LP, revenue
refers to surrogate first-price payments under the LP allocation.
1. Optimal given the tCPA constraint: maximizes conver-
sions while satisfying the target CPA.
2. Revenue-maximizing among uniform bidding equilib-
ria: lower multipliers result in lower bids and lower
revenue.
3. Welfare-maximizing: achieves the maximum possible
social welfare.
Proof Sketch. (1)With bi(C) =µ i ·t i ·p i,C, the CPA per
won cluster is µi ·t i, so µi ≤1 is required. Since con-
versions increase with µi, optimality requires µi = 1.(2)
At µ= 1 , bids are maximal under the CPA constraint.
(3)Allocation goes to arg maxi ti ·p i,C, which is welfare-
maximizing since value equalst i ·p i,C.
Corollary 5.3(FPA Welfare Monotonicity for tCPA).Un-
der the conditions of Theorem 5.1 and Theorem 3.1 (vi =t i),
with the optimal FPA multiplier µi = 1 , welfare is also
monotone: Welfare(MA)≥Welfare(M B).
Proof. For tCPA bidders bidding bi =t i ·p i,C with vi =
ti, revenue equals welfare (the winner pays exactly their
expected value vipi,C). Thus welfare monotonicity follows
directly from revenue monotonicity.
Remark5.4 (Incentive Compatibility in Autobidding
(IC-ROS)).FPA with uniform bidding isincentive compati-
ble with respect to return-on-spend constraints(IC-ROS) in
the terminology of Aggarwal et al. (2024). This autobidding-
specific notion of IC means that, when tCPA targets ti and
budgets Bi are private information but predicted conversion
probabilities pi,C are public, each bidder’s optimal strategy
is to truthfully report their constraints to the autobidding
system. The autobidder then bids bi =µ i ·t i ·p i,C, maxi-
mizing conversions subject to the reported constraints. This
differs from classical dominant-strategy incentive compati-
bility (DSIC), which applies to quasi-linear utilities; tCPA
bidders have non-linear objectives (conversion maximiza-
tion subject to cost constraints).
5.2.2. VCG MECHANISM WITHMAX-CPA BIDDERS
The VCG mechanism provides welfare monotonicity guar-
antees specifically for MAX-CPA bidders.
Theorem 5.5(VCG Welfare Monotonicity for MAX-CPA).
Consider MAX-CPA bidders without budget constraints. Un-
der the VCG mechanism, ifM A ⪰ MB, then:
Welfare(MA)≥Welfare(M B).(3)
Proof Sketch. VCG allocates to maximize welfare, and
truthful bidding (µi = 1) is dominant for MAX-CPA bid-
ders. Welfare is Welfare(M) = P C∈P wC ·max i vi ·p i,C,
6

Model Monotonicity in Autobidding Auctions
which has identical structure to FPA revenue with vi replac-
ing ti. By the same Jensen argument (since maxi vi ·p i is
convex), refinement cannot decrease welfare.
Remark5.6 (VCG Revenue Non-Monotonicity).VCG rev-
enue monotonicity doesnothold for MAX-CPA bidders.
VCG payments depend on the externality imposed on other
bidders, which can increase or decrease under model refine-
ment. See Section B.3 for a counterexample.
Remark5.7 (VCG with tCPA Bidders).For tCPA bidders,
VCG provides monotonicity forneitherrevenue nor wel-
fare. The issue is that tCPA bidders do not have fixed per-
conversion values—their effective value depends on the
tCPA constraint binding status across clusters. Model re-
finement can change which clusters are binding, leading to
non-monotonic outcomes. See Section B.1 for a counterex-
ample.
5.3. Negative Results: Non-Monotonicity
We now state our negative results. Detailed numerical con-
structions are provided in Section 6, with full calculations
in Section B.
5.3.1. VCG/SPA NON-MONOTONICITY FOR TCPA
Theorem 5.8(VCG/SPA Non-Monotonicity for tCPA).
There exist instances with tCPA bidders where VCG
(equivalently, SPA for single-item auctions) exhibits non-
monotonicity in both revenue and welfare:
MA ⪰ MB but Rev(M A)<Rev(M B),(4)
MA ⪰ MB but Welfare(M A)<Welfare(M B).(5)
The key intuition for SPA/VCG non-monotonicity is that
payments depend on thesecond-highestbid (the external-
ity). Model refinement can cause the ranking of bidders to
change across sub-clusters in ways that reduce competitive
pressure, thereby reducing payments. For tCPA bidders
specifically, the mismatch between tCPA constraints and
VCG’s welfare-maximizing allocation compounds this ef-
fect. See Section B.1 for a counterexample demonstrating a
6.2% decrease in both revenue and welfare.
Theorem 5.9(VCG Revenue Non-Monotonicity for
MAX-CPA).There exist instances with MAX-CPA bidders
where VCG welfare is monotone but revenue is not:
MA ⪰ MB but Rev(M A)<Rev(M B).(6)
VCG payments are externality-based: each winner pays the
welfare loss they impose on others. Model refinement can re-
duce competition in certain clusters, decreasing externalities
and thus payments. See Section B.3 for a counterexample.
5.3.2. BUDGETCONSTRAINTSBREAKMONOTONICITY
Theorem 5.10(FPA with Budget Non-Monotonicity).
There exist instances with tCPA bidders having budget con-
straints where model refinement decreases FPA revenue:
MA ⪰ MB but Rev(M A)<Rev(M B).(7)
With budgets, the optimal multiplier is no longerµ= 1 . Bid-
ders must pace to avoid depleting their budget too quickly.
Model refinement can change competitive dynamics—in
particular, revealing segments where a budget-constrained
bidder can win more auctions with lower bids. See Sec-
tion B.2 for a numerical counterexample demonstrating a
16.8% revenue decrease.
5.3.3. LP MONOTONICITY WITHBUDGET
CONSTRAINTS
Theorem 5.11(LP Benchmark Monotonicity).Consider
a centralized LP benchmark that chooses fractional alloca-
tions and surrogate payments directly, rather than modeling
strategic bidder behavior in an auction. The LP explic-
itly enforces budget feasibility through linear constraints
of the form P C wCxi,Caipi,C ≤B i, where ai is a bidder-
specific constant (e.g., ti for tCPA surrogate payments or
vi for MAX-CPA value budgets). This LP-based fractional
allocation benchmark guarantees welfare monotonicity. De-
fine:
WelfareLP(M) :=
X
i∈A
X
C∈P
wC ·x ∗ i,C ·v i ·p i,C,(8)
where x∗ ={x ∗ i,C} is the optimal LP solution. For tCPA
bidders (wherev i =t i), we additionally define:
RevLP(M) :=
X
i∈A
X
C∈P
wC ·x ∗ i,C ·t i ·p i,C.(9)
Note: RevLP is asurrogate metricrepresenting payments
assigned by the LP benchmark, not equilibrium revenue
from a strategic auction (see Theorem 5.12). For tCPA
bidders at µi = 1, these surrogate payments coincide with
first-price payments and RevLP =Welfare LP sincev i =t i.
IfM A ⪰ MB, then:
• For tCPA or MAX-CPA bidders: WelfareLP(MA)≥
WelfareLP(MB).
•For tCPA bidders only: Rev LP(MA)≥Rev LP(MB).
Proof Sketch. Aliftingargument: given optimal xB for
MB, construct feasible xA for MA by copying each al-
location to all sub-clusters ( xA i,C′ =x B i,C for C ′ ⊆C ).
Calibration preservation ensures supply, budget, and objec-
tive all match. Thus the refined optimum cannot be smaller.
See Section B.5.
7

Model Monotonicity in Autobidding Auctions
Remark5.12 (LP as a Non-Strategic Benchmark).Unlike
FPA with uniform bidding (Theorem 5.4), LP-based alloca-
tion isnotincentive compatible and should be interpreted
as a centralized allocation-and-payment benchmark, not an
equilibrium statement about rational autobidders. The plat-
form must know each bidder’s private target ti (or value vi)
and budget Bi to solve the allocation LP, and bidders may
have incentives to misreport these values. The monotonicity
result is therefore about feasibility-preserving allocation un-
der refinement: any feasible coarse LP solution can be lifted
to the refined partition while preserving the LP’s explicit
linear constraints.
5.3.4. MAX-CPA NON-MONOTONICITY INFPA
Theorem 5.13(FPA Non-Monotonicity for MAX-CPA Un-
der Designated Profiles).There exist instances with MAX-
CPA bidders in FPA and two feasible uniform-multiplier
profiles (one for each model) such that both revenue and
welfare decrease under model refinement:
MA ⪰ MB but Rev(M A)<Rev(M B),(10)
MA ⪰ MB but Welfare(M A)<Welfare(M B).
(11)
Unlike tCPA bidders (who optimally set µ= 1 under FPA
without budgets), MAX-CPA bidders strategically shade
their bids, and their multipliers can differ across models.
This row is not a full equilibrium characterization; it shows
that once feasible multiplier profiles are allowed to vary with
the information structure, the Jensen monotonicity argument
no longer protects either revenue or welfare. Note that with
truly fixedmultipliers across models, revenue would be
monotone by the same Jensen argument as Theorem 5.1.
See Section B.4 for a numerical counterexample demon-
strating 66% revenue loss and 0.09% welfare loss under
model refinement, together with additive-regret calculations
for the displayed profiles.
5.3.5. LIQUIDWELFARENON-MONOTONICITY
Theorem 5.14(Liquid Welfare Non-Monotonicity).There
exist instances with MAX-CPA bidders having budgets
where model refinement decreases liquid welfare:
MA ⪰ MB but
LiquidWelfare(MA)<LiquidWelfare(M B).(12)
The counterexample in Section B.4 demonstrates this: with
sufficiently large (non-binding) budgets, liquid welfare
equals standard welfare, so the 0.09% welfare decrease
applies. More generally, liquid welfare non-monotonicity
can also arise via a “crowding out” effect where a budget-
constrained high-value bidder displaces an unconstrained
bidder.
5.4. Discussion
Among strategic auction mechanisms, our results reveal that
monotonicity is rare: only FPA with tCPA bidders without
budgets guarantees both revenue and welfare monotonic-
ity, while VCG with MAX-CPA bidders without budgets
guarantees welfare monotonicity only. Separately, the cen-
tralized LP benchmark guarantees welfare monotonicity
with budgets, and for tCPA bidders also guarantees surro-
gate revenue monotonicity. All remaining auction settings
studied exhibit non-monotonicity due to: (1) externality-
based VCG payments, (2) budget-induced bid shading, or
(3) tCPA-VCG misalignment. For platforms, this implies
FPA with tCPA autobidders is the safest strategic auction
choice, and model improvements should be validated via
A/B testing rather than assumed to improve metrics.
6. Counterexamples
This section summarizes the numerical counterexamples
establishing non-monotonicity. Full calculations appear in
Section B.
Representative Counterexample: VCG/SPA Revenue
and Welfare Non-Monotonicity.Two tCPA bidders with
tA = 10, tB = 1. Four auctions (one impression each) with
conversion probabilities:
Auction 0 Auction 1 Auction 2 Auction 3
Bidder A 0.20 0.05 0.01 0.01
Bidder B 0.08 0.30 0.03 0.70
Under thecoarse model(partition {{0,1},{2,3}} ), equilib-
rium multipliers yield: A wins {0,1} , B wins {2,3} , with
both bidders exactly at their tCPA. Revenue= 3.23, Welfare
=t A ·0.25 +t B ·0.73 = 3.23 (where 0.25 = 0.20+0.05
and 0.73 = 0.03+0.70 are total conversions across won
auctions).
Under thefine model(singletons), equilibrium multipliers
shift: A wins only auction 0, B wins {1,2,3} , again with
both at tCPA. Revenue = 3.03, Welfare =t A ·0.20 +t B ·
1.03 = 3.03(where1.03 = 0.30+0.03+0.70).
Result: Both revenue and welfare decrease by 6.2% despite
MA ⪰ MB. The intuition: refinement reallocates high-
value impressions (auction 1) from the high-t bidder to the
low-t bidder, reducing value-weighted conversions. Full
calculations in Section B.1.
Key Insights.VCG/SPA payments depend on competi-
tion, which refinement can reduce. Budgets change utiliza-
tion patterns, potentially eliminating competition in some
segments (though LP-based allocation guarantees mono-
tonicity per Theorem 5.11).
8

Model Monotonicity in Autobidding Auctions
7. Conclusion
We introduced a formal framework for studying when im-
provements in prediction models lead to improvements in
platform-level metrics in autobidding systems. Our central
finding is striking:model monotonicity is rare.
Summary.We formalized model improvement through
a refinement relation inspired by filtrations in probability
theory, and systematically analyzed ECM monotonicity
across bidder types, auction formats, and budget constraints.
Of all settings studied, onlythreeguarantee monotonic-
ity: (1) tCPA bidders without budgets under FPA with uni-
form bidding at µ= 1 (revenue and welfare monotonic);
(2) MAX-CPA bidders without budgets under VCG (wel-
fare monotonic only—not revenue); (3) tCPA or MAX-
CPA bidders with budgets under LP-based fractional al-
location (welfare monotonic; for tCPA, surrogate revenue
also monotonic). All remaining settings studied—including
VCG/SPA for tCPA bidders and FPA with budgets—exhibit
non-monotonicity (verified numerically). For MAX-CPA
FPA, we provide a numerical counterexample under desig-
nated feasible multiplier profiles demonstrating 66% rev-
enue loss and 0.09% welfare loss; this counterexample also
establishes liquid welfare non-monotonicity when using
non-binding budgets.
Incentive Compatibility Trade-off.Our positive results
reveal a fundamental trade-off between monotonicity and
incentive compatibility. FPA with uniform bidding is incen-
tive compatible—bidders choose their multipliers privately
without revealing targets or budgets to the platform—but
only guarantees monotonicity without budget constraints.
LP-based allocation handles budgets and guarantees mono-
tonicity, but requires the platform to know private values
(ti, vi, Bi) to compute the optimal allocation, making it in-
centive incompatible. No known mechanism achieves both
properties simultaneously with budget constraints.
Implications.Better models do not always yield bet-
ter outcomes—platforms should validate improvements
through simulation. Budget constraints broadly break mono-
tonicity, and no auction format provides universal guaran-
tees. The interaction between ML models, auctions, and
autobidders creates dynamics where component-level im-
provements may not translate to system-level gains.
Acknowledgements
The author thanks the anonymous reviewers for their helpful
feedback.
Impact Statement
This paper presents work whose goal is to advance the under-
standing of interactions between machine learning models,
auction mechanisms, and automated bidding systems in on-
line advertising. While our results are theoretical and do
not propose a deployed system, they have potential impli-
cations for advertising platform design. More informative
prediction models can improve allocation quality, but can
also enable finer targeting, alter competitive pressure among
advertisers, and interact with budget constraints in ways
that affect market concentration and access to impressions.
These effects may also raise fairness and privacy concerns
when refined prediction models rely on sensitive or highly
granular user features. Our results therefore support care-
ful system-level validation of model changes rather than
evaluating prediction quality in isolation.
References
Aggarwal, G., Badanidiyuru, A., and Mehta, A. Autobid-
ding with constraints. InProceedings of the 15th In-
ternational Conference on Web and Internet Economics
(WINE), pp. 17–30. Springer, 2019. doi: 10.1007/
978-3-030-35389-6 2.
Aggarwal, G., Badanidiyuru, A., Balseiro, S., Bhawalkar,
K., Deng, Y ., Feng, Z., Goel, G., Liaw, C., Lu, H., Mah-
dian, M., Mao, J., Mehta, A., Mirrokni, V ., Paes Leme,
R., Perlroth, A., Piliouras, G., Schneider, J., Schvartzman,
A., Sivan, B., Spendlove, K., Teng, Y ., Wang, D., Zhang,
H., Zhao, M., Zhu, W., and Zuo, S. Auto-bidding and
auctions in online advertising: A survey.SIGecom Ex-
changes, 22(1):159–183, 2024. doi: 10.1145/3699824.
3699838.
Cai, H., Ren, K., Zhang, W., Malialis, K., Wang, J., Yu,
Y ., and Guo, D. Real-time bidding by reinforcement
learning in display advertising. InProceedings of the
Tenth ACM International Conference on Web Search and
Data Mining, pp. 661–670. ACM, 2017. doi: 10.1145/
3018661.3018702.
Clarke, E. H. Multipart pricing of public goods.Public
Choice, 11(1):17–33, 1971. doi: 10.1007/BF01726210.
Colini-Baldeschi, R., Klumper, S., Kroll, T., Leonardi, S.,
Sch¨afer, G., and Tsikiridis, A. Optimal type-dependent
liquid welfare guarantees for autobidding agents with
budgets. InProceedings of the 2026 Annual ACM-SIAM
9

Model Monotonicity in Autobidding Auctions
Symposium on Discrete Algorithms (SODA), pp. 1795–
1823. SIAM, 2026. doi: 10.1137/1.9781611978971.64.
Conitzer, V ., Kroer, C., Panigrahi, D., Schrijvers, O., Stier-
Moses, N. E., Sodomka, E., and Wilkens, C. A. Pacing
equilibrium in first price auction markets.Management
Science, 68(12):8515–8535, 2022. doi: 10.1287/mnsc.
2022.4310.
Deng, Y ., Golrezaei, N., Jaillet, P., Liang, J. C. N., and
Mirrokni, V . Multi-channel autobidding with budget and
ROI constraints. InProceedings of the 40th International
Conference on Machine Learning (ICML), volume 202
ofProceedings of Machine Learning Research, pp. 7617–
7644. PMLR, 2023.
Deng, Y ., Mao, J., Mirrokni, V ., Teng, Y ., and Zuo, S. Non-
uniform bid-scaling and equilibria for different auctions:
An empirical study. InProceedings of the ACM Web
Conference 2024, pp. 256–266. ACM, 2024. doi: 10.
1145/3589334.3645659.
Dobzinski, S. and Paes Leme, R. Efficiency guarantees
in auctions with budgets. InAutomata, Languages, and
Programming (ICALP), volume 8572 ofLecture Notes
in Computer Science, pp. 392–404. Springer, 2014. doi:
10.1007/978-3-662-43948-7 33.
Durrett, R.Probability: Theory and Examples. Cambridge
University Press, fifth edition, 2019.
Gneiting, T. and Raftery, A. E. Strictly proper scoring
rules, prediction, and estimation.Journal of the American
Statistical Association, 102(477):359–378, 2007. doi:
10.1198/016214506000001437.
Groves, T. Incentives in teams.Econometrica, 41(4):617–
631, 1973. doi: 10.2307/1914085.
Hardy, G. H., Littlewood, J. E., and P´olya, G.Inequalities.
Cambridge University Press, second edition, 1952.
Krishna, V .Auction Theory. Academic Press, second edi-
tion, 2009.
Liaw, C., Mehta, A., and Perlroth, A. Efficiency of non-
truthful auctions in auto-bidding: The power of random-
ization. InProceedings of the ACM Web Conference
2023, pp. 3561–3571. ACM, 2023. doi: 10.1145/3543507.
3583492.
Liaw, C., Mehta, A., and Zhu, W. Efficiency of non-truthful
auctions in auto-bidding with budget constraints. InPro-
ceedings of the ACM Web Conference 2024, pp. 223–234.
ACM, 2024. doi: 10.1145/3589334.3645636.
Lucier, B., Pattathil, S., Slivkins, A., and Zhang, M. Au-
tobidders with budget and ROI constraints: Efficiency,
regret, and pacing dynamics. InProceedings of Thirty
Seventh Conference on Learning Theory, volume 247 of
Proceedings of Machine Learning Research, pp. 3642–
3643. PMLR, 2024.
Ma, X., Zhao, L., Huang, G., Wang, Z., Hu, Z., Zhu, X.,
and Gai, K. Entire space multi-task model: An effective
approach for estimating post-click conversion rate. InThe
41st International ACM SIGIR Conference on Research
& Development in Information Retrieval, pp. 1137–1140.
ACM, 2018. doi: 10.1145/3209978.3210104.
Mehta, A. Auction design in an auto-bidding setting: Ran-
domization improves efficiency beyond VCG. InPro-
ceedings of the ACM Web Conference 2022, pp. 173–181.
ACM, 2022. doi: 10.1145/3485447.3512062.
Vasile, F., Lefortier, D., and Chapelle, O. Cost-sensitive
learning for utility optimization in online advertising auc-
tions. InProceedings of the ADKDD’17 Workshop, pp.
8:1–8:6. ACM, 2017. doi: 10.1145/3124749.3124751.
Vickrey, W. Counterspeculation, auctions, and competitive
sealed tenders.The Journal of Finance, 16(1):8–37, 1961.
doi: 10.1111/j.1540-6261.1961.tb02789.x.
Wilkens, C. A., Cavallo, R., Niazadeh, R., and Taggart, S.
Mechanism design for value maximizers.arXiv preprint
arXiv:1607.04362, 2016.
10

Model Monotonicity in Autobidding Auctions
A. Proofs of Main Positive Results
This appendix contains complete proofs of the two main positive theorems for the strategic auction settings stated in
Section 5 (the LP benchmark proof appears in Section B.5). Both proofs rely on Jensen’s inequality applied to convex
functions (Hardy et al., 1952).
A.1. Implementation Notes and Additional Remarks
pCTR/pCVR Implementation.In practice, platforms may predict CTR and CVR separately: pCTRM(u) := 1
|C|
P
u′∈C ctr(u′) and pCVRM(u) := 1 |C| P u′∈C cvr(u′). However, our analysis uses only the cluster-averaged conver-
sion probabilityp i,C. The product of cluster-averaged CTR and CVR does not generally equalp i,C.
Per-User vs. Per-Cluster Notation.ECM definitions sum over users u∈ U. In proofs, we equivalently write metrics
as weighted sums over clusters: Revenue(M) = P C∈P wC ·Rev(C) where wC =|C|/|U |. Since all users in a cluster
receive identical bids and allocations, per-user sums reduce to per-cluster weighted sums.
Tie-Breaking.Ties are broken by advertiser index (lowest index wins). This deterministic rule ensures well-defined
allocations and is standard in mechanism design (Krishna, 2009).
A.2. Proof of Theorem 5.1 (FPA Revenue Monotonicity for tCPA)
Proof. Consider tCPA bidders without budget constraints using uniform bidding with optimal multiplier µi = 1. Each
bidderibids:
bi(C) =t i ·p i,C (13)
wheret i is the target CPA andp i,C is the predicted conversion probability in clusterC.
In a first-price auction, the winner pays their bid, so revenue from clusterCis:
Rev(C) = max
i∈A
bi(C) = max i∈A ti ·p i,C.(14)
Total expected revenue under modelMwith partitionPis:
Rev(M) =
X
C∈P
wC ·max i∈A ti ·p i,C.(15)
Now suppose MA ⪰ MB, meaning the partition PA refines PB. For each cluster C B ∈ PB, there exist sub-clusters
{C A 1 , . . . , CA k } ⊆ PA that partitionC B. By the definition of refinement and calibration:
kX
j=1
wCA j =w CB ,(16)
kX
j=1
wCA j ·p i,CA j =w CB ·p i,CB ∀i∈ A.(17)
Defineλ j =w CA j /wCB, so P j λj = 1and P j λjpi,CA j =p i,CB.
Define the function f:R n →R by f(p 1, . . . , pn) = maxi ti ·p i. This function is convex as the pointwise maximum of
linear functions.
By Jensen’s inequality applied to the convex functionf:
kX
j=1
λj ·f(p 1,CA j , . . . , pn,CA j )≥f


kX
j=1
λjp1,CA j , . . . ,
kX
j=1
λjpn,CA j

 (18)
=f(p 1,CB , . . . , pn,CB ) = max i ti ·p i,CB .(19)
11

Model Monotonicity in Autobidding Auctions
Therefore:
kX
j=1
wCA j ·max i ti ·p i,CA j ≥w CB ·max i ti ·p i,CB .(20)
Summing over all clustersC B ∈ PB:
Rev(MA)≥Rev(M B).(21)
A.3. Proof of Theorem 5.5 (VCG Welfare Monotonicity for MAX-CPA)
Proof.Under VCG, the mechanism allocates to maximize welfare. In each clusterC, the allocation is:
i∗(C) = arg max
i∈A
vi ·p i,C (22)
wherev i is bidderi’s value per conversion. The welfare from clusterCis:
W(C) = max
i∈A
vi ·p i,C.(23)
Total welfare under modelMwith partitionPis:
Welfare(M) =
X
C∈P
wC ·max i vi ·p i,C.(24)
This expression has identical structure to FPA revenue in Theorem 5.1, withvi replacing ti. The function g(p) = maxi vi ·p i
is convex (pointwise maximum of linear functions).
By the identical Jensen’s inequality argument as in the proof of Theorem 5.1:
Welfare(MA)≥Welfare(M B)(25)
wheneverM A ⪰ MB.
B. Counterexample Details
This appendix provides detailed calculations for the counterexamples in Section 6.
B.1. VCG/SPA Revenue and Welfare Non-Monotonicity for tCPA
For single-item auctions, VCG and SPA are equivalent mechanisms (see Theorem 4.7). We provide a counterexample
demonstrating thatbothrevenue and welfare can decrease under refinement.
Setup:Four auctions u∈ {0,1,2,3} (one impression each). Two tCPA bidders A, Bwith targets tA = 10 , tB = 1 .
Uniform tCPA bidding: each bidder chooses a scalar goalg j and bidsb u,j =g j ·ˆpu,j whereˆpis the platform’s prediction.
True conversion probabilities:
Auction 0 Auction 1 Auction 2 Auction 3
BidderA0.20 0.05 0.01 0.01
BidderB0.08 0.30 0.03 0.70
Model B (Coarse):Partition{{0,1},{2,3}}. Predictions are cluster averages:
Cluster{0,1}: ˆp A = (0.20 + 0.05)/2 = 0.125,ˆp B = (0.08 + 0.30)/2 = 0.19(26)
Cluster{2,3}: ˆp A = (0.01 + 0.01)/2 = 0.01,ˆp B = (0.03 + 0.70)/2 = 0.365(27)
12

Model Monotonicity in Autobidding Auctions
Equilibrium (both at tCPA):Bidders choose uniform multipliers to maximize expected conversions subject to expected
CPA ≤t i, taking others’ multipliers as given. In SPA, any multipliers in an interval preserve the allocation; we exhibit an
equilibrium with both CPA constraints binding to make the welfare and revenue calculations transparent. The following
multipliers constitute such an equilibrium:Awins{0,1},Bwins{2,3}:
gB = tA ·(p 0,A +p 1,A) ˆp0,B + ˆp1,B = 10×0.25 0.38 = 6.579(28)
gA = tB ·(p 2,B +p 3,B) ˆp2,A + ˆp3,A = 1×0.73 0.02 = 36.5(29)
Best-response verification:Each bidder’s multiplier is set so their CPA constraint binds exactly. Increasing the multiplier
would cause the bidder to win additional auctions where their cost-per-conversion exceeds their target, violating feasibility.
For each bidder, the best-responsesetincludes all multipliers that preserve the same winning set while satisfying the CPA
constraint; among these, we select the CPA-binding multiplier as a canonical equilibrium. Other equilibria with the same
allocation exist within these intervals.
Verification:Bids in {0,1} : bA = 36.5×0.125 = 4.56 , bB = 6.579×0.19 = 1.25 (A wins). Bids in {2,3} : bA = 0.365,
bB = 2.40 (B wins). Both CPAs bind: A pays 2.50 for 0.25 conversions (CPA = 10 =t A); B pays 0.73 for 0.73
conversions (CPA= 1 =t B).
Rev(MB) = 2.50 + 0.73 = 3.23(30)
Welfare(MB) =t A ·0.25 +t B ·0.73 = 2.50 + 0.73 = 3.23(31)
Model A (Fine):Partition into singletons{{0},{1},{2},{3}}, soˆp i,j =p i,j.
Equilibrium (both at tCPA):Allocation:Awins only{0},Bwins{1,2,3}. From CPA constraints:
gB = tA ·p 0,A ˆp0,B = 10×0.20 0.08 = 25(32)
gA = tB ·(p 1,B +p 2,B +p 3,B) ˆp1,A + ˆp2,A + ˆp3,A = 1×1.03 0.07 = 14.71(33)
Best-response verification:As in the coarse model, each bidder’s CPA constraint binds exactly. Increasing either multiplier
would cause that bidder to win additional auctions violating their CPA target. Best-response sets are intervals preserving
the winning set; we select CPA-binding multipliers as canonical. The same allocation persists across all equilibria in these
intervals.
Verification:Auction 0: bA = 2.94, bB = 2.0 (A wins). Auctions 1,2,3: B wins (e.g., auction 1: bA = 0.74, bB = 7.5).
CPAs bind:Apays2.0for0.20conversions (CPA= 10);Bpays1.03for1.03conversions (CPA= 1).
Rev(MA) = 2.0 + 1.03 = 3.03(34)
Welfare(MA) =t A ·0.20 +t B ·1.03 = 2.0 + 1.03 = 3.03(35)
Non-monotonicity:Both revenue and welfare decrease: 3.23→3.03 (6.2% loss). Both bidders win ≥1 auction and are
exactly at tCPA in both conditions. Welfare decreases because refinement reallocates auction 1 (whereA has high value
tAp1,A = 0.5vsB’s valuet Bp1,B = 0.3) from high-tbidderAto low-tbidderB.
B.2. FPA Revenue Non-Monotonicity with Budgets
For the FPA counterexample with budget constraints (Theorem 5.10):
Setup:Four auctions, two advertisers. First-price auction with uniform bidding:b i(u) =α i ·ˆpi,u.
• Advertiser 1: BudgetB 1 = 3.185, targett 1 = 8.674(tCPA non-binding; budget binds under these multipliers).
• Advertiser 2: BudgetB 2 =∞, targett 2 = 1.662.
13

Model Monotonicity in Autobidding Auctions
Budget model:The budget Bi is a deterministic ex ante constraint on total expected payment across all auctions:P
u∈U xi(u)·b i(u)≤B i, where xi(u)∈ {0,1} indicates whether advertiser i wins auction u. No pacing or ran-
domization is used; bidders commit to a single multiplier αi applied uniformly. The budget-binding multiplier is the
maximumα i such that expected spend equalsB i given the allocation induced by(α 1, α2).
True conversion probabilities:
Auctionq 1 q2
1 0.516 0.559
2 0.027 0.850
3 0.560 0.617
4 0.555 0.330
Model B (Coarse):Partition{1,2},{3,4}.
Predictions:ˆp 1,{1,2} = 0.2715,ˆp 1,{3,4} = 0.5575(36)
ˆp2,{1,2} = 0.7045,ˆp 2,{3,4} = 0.4735(37)
Candidate multiplier profile:α 1 = 2.8565(budget binding),α 2 =t 2 = 1.662.
Advertiser 1’s bids:b 1({1,2}) = 0.7755,b 1({3,4}) = 1.5925.
Advertiser 2’s bids:b 2({1,2}) = 1.1709,b 2({3,4}) = 0.7870.
Winners: Advertiser 2 wins auctions 1,2; Advertiser 1 wins auctions 3,4.
Revenue: Rev(MB) = 2×1.1709 + 2×1.5925 = 5.5268.
Model A (Fine):Singleton partition (predictions equal true probabilities).
Candidate multiplier profile:α 1 = 1.9528(budget binding),α 2 =t 2 = 1.662.
Advertiser 1’s bids:b 1(1) = 1.0076,b 1(2) = 0.0527,b 1(3) = 1.0936,b 1(4) = 1.0838.
Advertiser 2’s bids:b 2(1) = 0.9291,b 2(2) = 1.4127,b 2(3) = 1.0255,b 2(4) = 0.5485.
Winners: Advertiser 1 wins auctions 1,3,4; Advertiser 2 wins auction 2.
Revenue: Rev(MA) = 1.0076 + 1.4127 + 1.0936 + 1.0838 = 4.5977.
Profile justification and best-response analysis:In both models, Advertiser 1’s budget binds, determining their multiplier
by budget exhaustion. In Model B, this yields α1 = 2.8565 with spend =B 1 = 3.185. Given this α1, Advertiser 2’s
best-responsesetis an interval: all α2 ∈(1.10,∞) preserve winning {1,2} (threshold: α2 > b1({1,2})/ˆp2,{1,2} ≈1.10 ).
We define a canonical equilibrium selection that picks α2 =t 2 = 1.662—the conversion-maximizing choice that exactly
binds the tCPA constraint. For Advertiser 1, we define the canonical selection as the maximal multiplier that exhausts
their budget (α1 = 2.8565). The profile (2.8565,1.662) is one Nash equilibrium selected from the continuum of equilibria
within the best-response intervals; the same selection convention applies to Model A withα 1 = 1.9528.
Result:Revenue decreases by(5.5268−4.5977)/5.5268 = 16.8%.
Mechanism:Under the coarse model, Advertiser 1’s low predicted probability in cluster {1,2} means they lose these
auctions despite high α1. Under the fine model, Advertiser 1 can win auction 1 (high true probability) with a lower α1.
The budget-constrained advertiser wins more auctions but pays less per auction, while the unconstrained advertiser loses a
high-payment auction (auction 1). Net effect: total revenue decreases.
Liquid welfare calculation:Liquid welfare is P i min(Bi,welfare i) where welfarei = P u∈Wi ti ·p i,u (Advertiser i’s total value from won impressionsW i).
Model B:Advertiser 1 wins {3,4} : welfare = 8.674×(0.560 + 0.555) = 9.67 , capped at min(3.185,9.67) = 3.185 .
Advertiser 2 wins{1,2}: welfare= 1.662×(0.559 + 0.850) = 2.34. Total:3.185 + 2.34 = 5.53.
Model A:Advertiser 1 wins {1,3,4} : welfare = 8.674×(0.516 + 0.560 + 0.555) = 14.15 , capped at 3.185. Advertiser 2
wins{2}: welfare= 1.662×0.850 = 1.41. Total:3.185 + 1.41 = 4.60.
Liquid welfare decreases by (5.53−4.60)/5.53 = 16.8% , matching revenue. The decrease arises because model refinement
14

Model Monotonicity in Autobidding Auctions
lets the budget-constrained advertiser win auction 1 (displacing the unconstrained advertiser), but the budget cap prevents
extracting additional value while the unconstrained advertiser loses conversions.
B.3. VCG Revenue Non-Monotonicity for MAX-CPA
For the VCG counterexample with MAX-CPA bidders (Theorem 5.9):
Setup:v 1 = 10,v 2 = 8. Segments withw 1 =w 2 = 0.5:
S1 S2
Bidder 1 0.2 0.6
Bidder 2 0.5 0.1
Model B (Coarse):
v1p1 = 10×0.4 = 4.0, v 2p2 = 8×0.3 = 2.4(38)
VCG payment= 2.4,Welfare= 4.0(39)
Model A (Fine):
S1 :v 1p1 = 2.0, v 2p2 = 4.0⇒Bidder 2 wins, payment= 2.0(40)
S2 :v 1p1 = 6.0, v 2p2 = 0.8⇒Bidder 1 wins, payment= 0.8(41)
Results:
Rev(MA) = 0.5×2.0 + 0.5×0.8 = 1.4<2.4 =Rev(M B)(42)
Welfare(MA) = 0.5×4.0 + 0.5×6.0 = 5.0>4.0 =Welfare(M B)(43)
This confirms that VCG welfare is monotonic for MAX-CPA (as proven in Theorem 5.5), but revenue is non-monotonic.
The revenue decrease is 41.7%.
B.4. FPA Non-Monotonicity for MAX-CPA
We provide a numerical counterexample demonstrating that FPA with MAX-CPA bidders can exhibit non-monotonicity in
both revenue and welfare under model-dependent feasible multiplier profiles (Theorem 5.13). This is not a full equilibrium
characterization; we report additive-regret calculations below to show that the profiles are near best responses in this instance.
Setup:Two impression types H (high-value) and L (low-value) with probabilities Pr(H) = 0.9 and Pr(L) = 0.1. Two
MAX-CPA bidders:
Advertiser Valuev i pi(H)p i(L)
1 600 0.2 0.01
2 10 0.02 0.5
Model B (Coarse):The coarse model pools both impression types. Calibrated predictions:
ˆp1 = 0.9×0.2 + 0.1×0.01 = 0.181(44)
ˆp2 = 0.9×0.02 + 0.1×0.5 = 0.068(45)
Expected values per impression:v 1 ˆp1 = 108.6,v 2 ˆp2 = 0.68.
Under uniform bidding, consider multipliers (g1, g2) = (0.68/0.181,10)≈(3.7569,10) . Bidder 1 bids b1 =
(0.68/0.181)×0.181 = 0.68 and Bidder 2 bids b2 = 10×0.068 = 0.68 . With ties broken by lowest index, Bidder
1 wins all impressions.
15

Model Monotonicity in Autobidding Auctions
Revenue:Rev(M B) = 0.68.
Welfare:Bidder 1 captures all value: Welfare(M B) =v 1 ˆp1 = 108.6.
Model A (Fine):The fine model distinguishesHandLimpressions.
In segmentH:v 1p1(H) = 600×0.2 = 120,v 2p2(H) = 10×0.02 = 0.2.
In segmentL:v 1p1(L) = 600×0.01 = 6,v 2p2(L) = 10×0.5 = 5.
Under the fine model, consider the multiplier profile(g 1, g2) = (1,1).
Profile justification:With (g1, g2) = (1,1) : Bidder 1’s bid in H is 0.2>0.02 (Bidder 2’s bid), so Bidder 1 wins H;
Bidder 2’s bid in L is 0.5>0.01 (Bidder 1’s bid), so Bidder 2 wins L. Other multiplier profiles also preserve this allocation
whenever the ratio satisfies 0.1< g1/g2 <50 . As stated in Theorem 4.10, MAX-CPA FPA counterexamples use designated
feasible multipliers without full equilibrium claims; non-monotonicity arises because different information structures can
induce different shading profiles.
With these multipliers:
SegmentH:b 1(H) = 1×0.2 = 0.2,b 2(H) = 1×0.02 = 0.02. Bidder 1 wins.
SegmentL:b 1(L) = 1×0.01 = 0.01,b 2(L) = 1×0.5 = 0.5. Bidder 2 wins.
Revenue:
Rev(MA) = 0.9×0.2 + 0.1×0.5 = 0.18 + 0.05 = 0.23(46)
Welfare:
Welfare(MA) = 0.9×120 + 0.1×5 = 108 + 0.5 = 108.5(47)
Results:
Revenue decrease: 0.68−0.23 0.68 = 66.2%(48)
Welfare decrease: 108.6−108.5 108.6 = 0.09%(49)
Additive-regret calculation.In the coarse model, (g1, g2) = (0.68/0.181,10) is a threshold best-response profile under
the stated tie-breaking rule: Bidder 1 wins all impressions at the lowest bid that ties Bidder 2, and Bidder 2 would obtain
non-positive surplus by outbidding. In the fine model, (g1, g2) = (1,1) is not an exact Nash equilibrium. However, its
additive best-response regrets are small in the scale of the instance. Bidder 1’s utility is 0.9(120−0.2) = 107.82 ; by
lowering g1 to just above 0.1, Bidder 1 still wins H and obtains utility approaching 0.9(120−0.02) = 107.982 , a gain of at
most 0.162. Bidder 2’s utility is 0.1(5−0.5) = 0.45 ; by lowering g2 to just above 0.02, Bidder 2 still wins L and obtains
utility approaching 0.1(5−0.01) = 0.499 , a gain of at most 0.049. Thus the fine profile is an approximate best-response
profile, not an exact equilibrium.
Mechanism:The key insight is that model refinement enablesmarket segmentationthat reduces competitive pressure.
Under the coarse model, Bidder 1 faces competition across all impressions and must bid at the pooled threshold to win.
Under the fine model, each segment becomes a near-monopoly in bid space: Bidder 1 dominates H (bid 0.2 vs. 0.02) and
Bidder 2 dominates L (bid 0.5 vs. 0.01). This segmentation allows both bidders to shade their bids more ( g1 =g 2 = 1),
dramatically reducing payments. The welfare loss is minimal because the fine model still allocates efficiently within each
segment; the small loss arises from Bidder 2 winning segmentLwhere Bidder 1 has slightly higher value (6 vs. 5).
B.5. LP Benchmark Monotonicity Proof
This appendix provides the complete proof of Theorem 5.11, showing that a centralized LP allocation-and-payment
benchmark guarantees revenue and welfare monotonicity under model refinement. This is not an equilibrium claim about
strategic autobidders; the LP directly enforces the relevant feasibility constraints.
16

Model Monotonicity in Autobidding Auctions
LP for tCPA Bidders:For tCPA bidders, the LP maximizes total welfare subject to a surrogate-payment budget:
max
xi,C ≥0
X
i∈A
X
C∈P
wC ·x i,C ·t i ·p i,C (maximize total welfare) (50)
s.t.
X
C∈P
wC ·x i,C ·t i ·p i,C ≤B i ∀i∈ A(budget constraint: spend≤B i) (51)
X
i∈A
xi,C ≤1∀C∈ P(supply constraint) (52)
xi,C ∈[0,1]∀i∈ A, C∈ P(53)
Here, the LP’s surrogate payment for bidder i in cluster C equals ti ·p i,C per impression, matching truthful tCPA first-price
payments atµ i = 1.
LP for MAX-CPA Bidders:For MAX-CPA bidders, the LP maximizes welfare subject to a value-budget/liquid-welfare
feasibility constraint:
max
xi,C ≥0
X
i∈A
X
C∈P
wC ·x i,C ·v i ·p i,C (maximize total welfare) (54)
s.t.
X
C∈P
wC ·x i,C ·v i ·p i,C ≤B i ∀i∈ A(budget constraint) (55)
X
i∈A
xi,C ≤1∀C∈ P(supply constraint) (56)
xi,C ∈[0,1]∀i∈ A, C∈ P(57)
Remark (Budget semantics):The LP result should be read as a centralized allocation-and-payment benchmark. It explicitly
enforces feasibility constraints of the calibrated linear form P C wCxi,Caipi,C ≤B i, where ai is fixed for bidder i. For
tCPA bidders at µi = 1, the surrogate payment tipi,C coincides with value per impression. For MAX-CPA bidders, the LP
welfare result uses the analogous value-budget/liquid-welfare constraint vipi,C. Strategic auction spend budgets, where
actual payments depend on the auction format and other bidders’ bids, are handled separately in the FPA and VCG rows of
Table 1.
Proof of Theorem 5.11.Letx B ={x B i,CB }be an optimal solution for the coarse modelM B.
Construct a feasible solution xA for the refined model MA by copying each coarse allocation fraction to every sub-cluster:
for each coarse clusterC B ∈ PB with refined sub-clusters{C A 1 , . . . , CA k }, define
xA i,CA j :=x B i,CB for alli∈ Aandj= 1, . . . , k.(58)
(1) Supply feasibility.For any refined clusterC A j ⊆C B:
X
i
xA i,CA j = X
i
xB i,CB ≤1,(59)
so all refined supply constraints hold.
(2) Budget feasibility.For any advertiseri:
X
C∈PA
wC ·x A i,C ·t i ·p i,C = X
CB ∈PB
kX
j=1
wCA j ·x B i,CB ·t i ·p i,CA j (60)
=
X
CB ∈PB
xB i,CB ·t i ·


kX
j=1
wCA j ·p i,CA j

 .(61)
17

Model Monotonicity in Autobidding Auctions
By calibration preservation, Pk j=1 wCA j ·p i,CA j =w CB ·p i,CB. Thus:
=
X
CB ∈PB
xB i,CB ·t i ·w CB ·p i,CB = X
CB ∈PB
wCB ·x B i,CB ·t i ·p i,CB ≤B i.(62)
All budget constraints hold. (The argument is identical for MAX-CPA withv i replacingt i.)
(3) Objective preservation.The same calculation shows the refined solution achieves exactly the same objective value:
X
C∈PA
X
i
wC ·x A i,C ·t i ·p i,C = X
CB ∈PB
X
i
wCB ·x B i,CB ·t i ·p i,CB .(63)
Sincex A is feasible forM A, the refined optimum cannot be smaller.
tCPA case:With objective P wCxi,Ctipi,C:
RevLP(MA)≥Rev LP(MB).(64)
MAX-CPA case:With objective P wCxi,Cvipi,C (welfare):
WelfareLP(MA)≥Welfare LP(MB).(65)
The algebra is identical in both cases, substitutingv i fort i.
B.6. Notes on Liquid Welfare
Liquid Welfare:The counterexample in Section B.4 establishes liquid welfare non-monotonicity: with sufficiently large
(non-binding) budgets, liquid welfare equals standard welfare, so the 0.09% welfare decrease applies directly. More generally,
non-monotonicity can also arise via a “crowding out” effect where a budget-constrained high-value bidder displaces an
unconstrained bidder, and the constrained bidder’s capped contribution is less than the displaced bidder’s full contribution.
C. Open Problems
Our work suggests several directions for future research:
1.Approximate monotonicity—can we bound the magnitude of monotonicity violations?
2.Incentive-compatible monotonic mechanisms—do mechanisms exist that achieve both properties?
3. Calibration and misspecification—how do the positive and negative results change when prediction models are
imperfectly calibrated or only approximately refine one another?
4. Multi-slot auctions—which monotonicity results extend to multi-slot formats such as generalized second-price or
generalized first-price auctions?
5. Equilibrium selection—can stronger equilibrium-based characterizations be obtained for first-price auctions with
MAX-CPA bidders, where pure equilibria and selection can be delicate?
6. Empirical prevalence—how often do the non-monotonic effects identified by the counterexamples arise in simulations
or deployed advertising systems?
7.Learning dynamics—how do model changes affect autobidder learning and convergence?
8.Heterogeneous populations—what happens with mixed tCPA/MAX-CPA bidder populations?
18
