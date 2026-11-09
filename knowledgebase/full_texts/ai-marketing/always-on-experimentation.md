---
title: Always-On Experimentation
url: https://arxiv.org/abs/2609.38695
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Ricardo J. Sandoval
- David Arbour
- Avi Feller
- Michael I. Jordan
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.38695
pages: 38
chars: 107910
fetched_at: '2026-11-08T13:20:24+00:00'
kb_version: 1
---

# Always-On Experimentation

Always-On Experimentation
Ricardo J. Sandoval ⋆, David Arbour †, A vi Feller⋆, and Michael I. Jordan ⋆‡
⋆University of California, Berkeley
†Adobe Research
‡Inria, Paris
October 1, 2026
Abstract
Generative AI has dramatically accelerated the rate at which new treatments—from novel phar-
maceuticals to online marketing campaigns—can be conceived and deployed. As a result, modern
experimentation platforms often run continuously, with treatments added as they are ready and
removed when they underperform. We formalize this “Always-On” experimental setting, in which
treatments can be dynamically generated, added to, and removed from a running experiment, and
study the statistical problem of deciding whether to accept or reject each treatment while controlling
for the false discovery rate. We develop sequential tests that achieve time-uniform Type-I error control
under arbitrary stopping times and “predictable” treatment schedules. Our approach builds on the
testing-by-betting framework: we construct test supermartingales for testing the average treatment
effect of each treatment, and show that the construction of these test supermartingales is growth-rate
optimal in an almost-sure sense.
1 Introduction
Generative AI has the promise to accelerate the rate of scientific discovery. It has reduced the barrier
to the conception of new treatments, making it easier for practitioners to generate new hypotheses “on
the fly.” Existing experimentation frameworks, however, have not been designed for an era in which
treatments can be easily and dynamically generated. Rather, to guarantee statistical validity existing
methods typically require practitioners to know all treatments prior to starting the experiment and do
not afford practitioners the freedom to continuously monitor the experiment in order to decide when to
remove a treatment. In this work we introduceAlways-On Experimentation, a statistical design framework
suited for the era in which the conception of treatments is no longer the bottleneck in the experimentation
pipeline.
500 1000 2000 3000 4000 5000
Maximum observations assigned
to each treatment
−30
−20
−10
0
Difference in true discoveries
(Always-On − platform trials)
500 1000 2000 3000 4000 5000
Maximum observations assigned
to each treatment
−20%
0%
20%
40%
60%
Participatns saved relative
to platform trials
Figure 1:(Left)Depiction of an instance of Always-On experimentation in which four treatments were added
and removed at different points in the experiment.(Middle & Right)Always-On experimentation achieves the
same level of power as platform trials while reducing the number of units needed to perform such discoveries. For
information about simulation setup and further simulations, see Section A.1.
1
arXiv:2609.38695v1  [stat.ME]  30 Sep 2026

Our Always-On design is based on simple desiderata: practitioners should have the flexibility to add
and remove treatments at any point in time from a continuously running experiment. Such flexibility
should be coupled with the ability tocontinuously monitorthe experiment and decide to introduce
or remove treatments in a data-driven manner, all while maintaining statistical validity. In our case,
statistical validity consists of two components: controlling the type-I error for each treatment that has
been introduced to the experiment, for the entire duration of the experiment; and safeguarding against
multiple comparisons, since potentially multiple treatments will be tested within the same experiment. Our
paper formalizes the Always-On design and describes how it satisfies these desiderata while maintaining
statistical validity.
The rest of the paper is organized as follows. Section 2 connects the Always-On design to the existing
experimental designs literature. Section 3 presents our Always-On design. Section 3.1 formalizes the
design and instantiates it within the testing-by-betting framework. Section 3.2 describes how we tackle
the multiple testing problem within our Always-On framework. Section 4 instantiates the Always-On
framework in a setting where experimental units are only observed once for the entire duration of the
experiment. We describe the target estimands and our estimators within this setting, and we present
a strategy to construct “powerful” test statistics that enjoy an almost sure and asymptotic notion of
growth-rate optimality. In Section 5 we present the performance of Always-On experimentation in a
semi-synthetic experiment.
2 Related Work
Platform trials.Platform trials from biomedical research [4, 64, 52] focus on evaluating a range of
interventions for a single disease or condition. Like Always-On experimentation, platform trials facilitate
the addition and removal of interventions from a continuously running experiment. Platform trials,
however, typically operate under a master protocol that prespecifies the timing or rules governing interim
analyses and adaptations, including when treatment arms may be stopped or added [see, for example,
1]. By contrast, Always-On experimentation permits continuous monitoring and allows treatments to be
added or removed at arbitrary times, provided these decisions depend only on past data.
Online multiple testing.Our Always-On design is a particular instantiation of the general online
multiple testing framework introduced by Foster and Stine[17]. Most work on online multiple testing
(e.g., [24, 25, 39, 57, 65]) has considered a setting in which hypotheses are tested sequentially; that is, a
hypothesis must either be accepted or rejected before a new hypothesis is tested. Zrnic et al.[68] and
Fischer et al.[16] relaxed the synchronous testing requirement and considered settings in which hypotheses
need not be accepted or rejected before others are introduced, and they provided algorithms to control
the online false discovery rate (or other related error metrics). Our framework’s multiple testing setting is
most similar to that of the latter two works as treatments can be added to the experiment at any point
and their futility need not be determined before other treatments are introduced. Rather, treatment arms
can remain active throughout the experiment until enough evidence is gathered to declare the treatment a
discovery or a decision is made to remove the treatment from the experiment. Robertson et al.[45] and
Zehetmayer et al.[67] study how existing algorithms that control the online false discovery rate can be
used within platform trials and evaluate their performance empirically.
Online experimentation and multi-armed bandits.Modern experimentation platforms at technol-
ogy companies run experimentation continuously [28], motivating our Always-On framework. A common
approach is to run a single experiment that consists of multiple arms, typically referred to as A/B/n
tests. Bartroff and Song[2] focus on a setting in which data arrives sequentially and are interested in
testing a predetermined set of hypotheses while controlling for the false discovery rate. They extend the
procedure due to Benjamini and Hochberg[3] to a setting in which data arrives sequentially. Jamieson
and Jain [23] consider a setup in which they get to dynamically sample from the available treatment
arms, with the goal of minimizing the number of samples needed to exceed a threshold on the proportion
of true discoveries while controlling for the false discovery rate. Lin et al.[31] recently studied active
2

sampling in a multiple testing setting for a more general class of hypotheses; they proposed a new adaptive
data collection algorithm and analyzed its sample complexity for discovering all non-null hypotheses.
Multi-armed bandits are another common approach for testing multiple treatments simultaneously in
online platforms. The focus of these tests is to allocate units dynamically to the best performing arm
in order to minimize (or maximize) some metric such as regret. Yang et al.[66] propose a framework
in which best-arm multi-armed bandits are sequentially tested with the aim of identifying the best arm
within each instance while controlling the online false discovery rate. Recently, Sandoval et al.[51], Imbens
et al.[22] and Bharti et al.[5] study a sequential hypothesis testing setting in which data can be sampled
from multiple arms, and it is of interest to determine quickly whether any of the arms is non-null.
3 Always-On experimentation
We study a design that affords the flexibility to add and remove treatments from a running experiment.
We introduce the construct ofsub-experiments, which we define to be those points in time in which
treatments are added and removed from the running experiment, and note that the total number of
sub-experiments t∈N need not be known a priori. Nonetheless, throughout this paper we assume the total
number of sub-experiments is finite, meaning thatt <∞. In each sub-experiments∈ [t] := {1, . . . , t},
the statistician tests the treatments belonging to theset of active treatmentsAs, and we assume that
the control—which we denote as0—is always present in each sub-experiment.1 In other words, in each
sub-experiment s∈ [t]the statistician has access to thefiniteset As ∪ {0}, where |As ∪ {0}|<∞.
We denote the set of treatments that were at some point active in the experiment (that consisted oft
sub-experiments) as A := St s=1 As. Since not all treatments are active in the same set of sub-experiments,
we letT t(a) :={s∈[t]|a∈ A s}be the set of sub-experiments in which treatmenta∈ Awas active.
We assume units enter the experiment sequentially, and denote asIs the set of units that participated
in the experiment during sub-experiment s∈ [t]whose size we represent as ns := |Is|. We remark
that the setsIs could consist of different or the same units—settings that we consider in Section 4 and
Section B, respectively. We use the notationIs(j)to denote the set of the first j∈ [ns]units that
have entered sub-experiments. Furthermore, we denote the set of all units that have been part of the
experiment starting from sub-experiment one up to sub-experiments as I1:s := Ss r=1 Ir, and if s = t
(i.e., the last sub-experiment that has been run) we will use the shorthandI ≡ I1:t. Lastly, we denote as
I1:s(j) := Ss−1 r=1 Ir ∪ Is(j)the set of all units that have appeared in sub-experiments one up tos− 1and
thosejunits whom have entered sub-experiments.
We adopt the potential outcomes framework [34, 48] and assume each uniti∈ Ihas potential outcomes
Yi(z) ∈R for eachz ∈ Z, where Z denotes the set of all possible treatment paths. We will instantiate the
set Z in the sections to come. Additionally, for the rest of the paper we make the following assumption
on the potential outcomes.
Assumption 1.We assume the potential outcomes for each unit are independently and identically
distributed:(Y i(z))z∈Z ∼Pfor eachi∈ I.
We emphasize that Assumption 1 is only with respect to how the units themselves are sampled and not
on any putative dependence between their potential outcomes. Indeed, the potential outcomes(Yi(z))z∈Z
for each unit can be highly dependent.
Because the set of active treatments differs across sub-experiments and to avoid temporal drift that
might result from running the experiment over time, we perform a new series of treatment assignments
in every sub-experiment. That is, in each sub-experiments∈ [t]we randomly assign the treatments
from the set As ∪ {0}to those units in Is. Throughout, we denote the treatment assignment unit
i∈ Is received in sub-experiments as Ai,s ∈ As ∪ {0}. This treatment assignment induces the observed
outcome for uniti∈ Is, which we denote asYi,s, and defer its formal definitions to Sections B and 4.
The filtration that arises in Always-On experimentation is with respect to the outcomes and treatment
assignments that we have observed thus far in the experiment. More formally, we denote the filtration
1For simplicity of exposition we assume that all treatments within the experiment are compared against the same control,
but our framework can be easily modified so that each sub-experiment can have a potentially different control.
3

for sub-experiment s∈ [t]based on all the units that have been part of the experiment, including thej
units that have entered sub-experiments, as Fj,s := σ

(Ai,r, Yi,r)i∈Ir ,A r
s−1
r=1
,(A i,s, Yi,s)i∈Is(j)

. We
slightly overload notation, denoting the filtration with respect to observed outcomes and assignments from
the previous s− 1sub-experiments as Fs−1 := σ

(Ai, Yi)i∈Ir ,A r
s−1
r=1

, with F0 = {∅,Ω} as the trivial
σ-algebra.
In addition to Assumption 1 we make the following assumptions on the treatment assignments.
Assumption 2(Assumptions on the treatment assignments).Let Ai,s ∈ As ∪ {0}denote the treatment
assignment unit i∈ Ireceived in sub-experiments∈ [t], and letZs:t denote the set of treatment paths
in sub-experiment s up to t—with their respective potential outcomes beingYi(z)for eachz ∈ Zs:t and
i∈ I. We assume the following conditions hold for each sub-experiments∈ [t]and unit i∈ I:( i)
Ai,s ⊥ ⊥(Yi(z))z∈Zs:t | Fi−1,s (conditional ignorability) ;( ii)for some deterministic constant ps ∈ (0, 1), PRCTs (Ai,s = a| Fs−1) ≥p s > 0for each a∈ As ∪ {0}(positivity), where PRCTs (Ai,s = a| Fs−1)
denotes the conditional probability of being assigned treatmenta∈ As when the treatment assignment is
sampled from the randomization distribution represented byRCTs.
The assumptions from Assumption 2 are common in the causal inference literature, and are satisfied
by design given that we have control over the treatment assignments in the setting we study.
We letπs := (πs(a))a∈As∪{0} be thepropensity scoreover the set of active treatments and control in
sub-experiment s, where we defineπs(a) := PRCTs (Ai,s = a| Fs−1)for each a∈ As ∪ {0}. In addition to
Assumption 2, which tells us thatπs(a) ∈ (0, 1)for each a∈ As ∪{0}, we assume thatP a∈As∪{0} πs(a) = 1
and that the propensity scoreπs is determined (i.e., fixed) at the beginning of each sub-experiments
and that it isFs−1-measurable. This means that the propensity score can be a function of the data seen
in previous sub-experiments, but once the current sub-experiment starts it can no longer be modified
(until the start of the next sub-experiment). Having defined the propensity score, we model the treatment
assignment as follows: in every sub-experiments we commit to drawing the treatment assignments from a
categorical distribution over the set of active treatments. LettingRCTs := CategoricalAs∪{0}(πs), the
treatment assignment for uniti∈ Is in sub-experimentsis drawni.i.dasA i,s ∼RCT s. To simplify the
notation used throughout the rest paper, we writePRCT :=P ⊗RCT 1 ⊗ · · · ⊗RCTt to denote the joint
law of the potential outcomes and treatment assignments under the induced experimental design.
In addition to our assumptions on the treatment assignments and propensity scores, we make the
following assumptions for the treatment schedule.
Assumption 3(Assumptions on the treatment schedule).We make the following assumptions on how
the treatments are added and removed from the experiment:(i)Let a∈ As be a treatment active in
sub-experiments∈[t]. Then, the decision to keep treatmentain sub-experiments+ 1isF s-measurable;
(ii)Let A′ s be the set of new treatments to be added in sub-experiments. We assume that the decision to
add these treatments to the experiment isFs−1-measurable.
Assumption 3 has to do with the information available to us when deciding to add and remove
treatments, and it tells us that such decisions cannot depend on future information. Otherwise, these
decisions can be arbitrary. For example, a decision to remove a treatment from the experiment could
be based on the belief, formed from the evidence gathered, that such treatment will not yield a higher
expected outcomes than any other active treatment in the experiment.
We formally state the data collection protocol of Always-On experimentation in Algorithm 2, which
can be found in Section A. In the following section we introduce the type of hypotheses tests we consider,
and describe how to construct sequential anytime valid test statistics.
3.1 Testing by betting in Always-On experimentation
Rather than pursuing accurate estimates of the average treatment effects, our goal is to create powerful
test statistics that allow us to determine as quickly as possible whether each of the treatments added to
4

the experiment is effective. In this section we provide an informal introduction to the concepts that are
needed to obtain such statistics; for formal definitions see Sections B and 4.
For each of the active arms in sub-experiments∈ [t], a∈ As, we are interested in testing whether
their treatment effectψP(a) ∈R is greater than some thresholdδ∈R . We therefore run a hypothesis test
for each of the active armsa∈ As, where under the nullP(a)the treatment effect is less than or equal to
the threshold δ while under the alternativeQ(a)the treatment effect is greater thanδ. That is, for each
treatmenta∈ Athe null and alternative hypotheses take the following form
P(a) :={P|ψ P(a)≤δ}versusQ(a) :={P|ψ P(a)> δ},(1)
and we additionally define the setsP:= S a∈A P(a)andQ := S a∈A Q(a).
Given that we are interested in testing each of the active arms, we construct a test supermartin-
gale: a supermartingale that is almost surely nonnegative and whose expectation is upper bounded
by one. We first introduce some additional notation. For sub-experiments∈ Tt(a)we let ˇNa(s) :=P
i∈Is 1{A i,s =aorA i,s =0} be the number of units in sub-experiments which were assigned to the
treatment a∈ As or the control. Furthermore, we letNa(t) := P s∈Tt(a) ˇNa(s)be the total number of units which have been assigned to either treatmenta∈ Aor the control over those sub-experiments in
which treatment a has been active. Let bψi,s(a)be the estimator of the treatment effect of treatment
a∈ As,(( λi,s)i∈Is )s∈Tt(a) be a predictable process (which we also refer to as aportfolio), and for each
sub-experiment s let gs : R→R ≥0 be a Fs−1-measurable nondecreasing function that maps a real-valued
variable into the positive reals. Having introduced the necessary concepts, we now present the form of the
test statistics—to test the hypotheses given in(1)—that we consider for each treatmenta∈ Athroughout
the rest of the paper:
WNa(t) :=
Y
s∈Tt(a)
W ˇNa(s) whereW ˇNa(s) :=
Y
i∈Is

1−λ i,s +λ i,sgs( bψi,s(a))/gs(δ)
ξi,s(a)
,(2)
where we have used the shorthandξi,s(a) :=1{A i,s =aorA i,s =0}.
The test statistic from(2) pools together the information from those units which received the treatment
a∈ Aand those which received the control across the different sub-experiments. The following lemma
states that this test statistic is a test supermartingale; see Section D.1 for the proof.
Lemma3.1.Fix an arm a∈ Aand a distributionP∈ P(a). Suppose thatEPRCT[gs( bψi,s(a)) | Fi−1,s, ξi,s(a) =
1] = gs(ψP(a))for each s∈ [t]and that Assumptions 1 to 3 hold. Then, the processWNa(t) forms a test
P(a)-supermartingale.
This statistic(2) is a particular instantiation of a test supermartingale commonly used for testing the
mean of bounded random variables (see for example [62, 19, 35, 49, 56, 9, 36, 37, 50]) and which is in fact
the only admissible test supermartingale for such problems [10].
Lemma 3.1 together with Ville’s inequality allow us to conclude that we are able to achieve time-uniform
type-I error rate control when it comes to testing each individual treatment; see Equation (15) in Section C
for a formal definition. However, in Always-On experimentation we are interested in testing multiple
treatments a∈ A, which means that we are in a multiple testing setting and must also aim to control a
metric that takes this into account. In the following section we describe how we address multiple testing
in Always-On experimentation.
3.2 Multiple testing in Always-On experimentation
Recall that we are interested in testing whether the treatment effect of each of the arms that have been
added to the experiment is greater than some pre-determined threshold. This means that the experiment
could consist of multiple hypothesis tests, one for each of the treatments that was added. Given that we
do not know a priori the number of treatments that will be tested, we must control an error metric that is
compatible with the flexibility sought after in Always-On experimentation. The online false discovery
rate [17] affords such flexibility and, as such, we use it as our error metric in Always-On experimentation.
5

In the rest of this section we adapt the notion of online false discovery rate to Always-On experimentation
and provide an algorithm that controls it.
For a distributionP ∈ P ∪ Q, we letH0 ⊆ Abe the set of treatments that are null underPbased on
the hypotheses from(1), or those from(11) in Section B. We letDs be the set of discoveries that have
been made up to sub-experiments∈ [t](i.e., the set of treatmentsa∈ Ss r=1 Ar that have been declared
as non-null), and we note howD1 ⊆ · · · ⊆ Dt. Thefalse discovery rate[3] for the setDis defined as
FDR(D) :=E PRCT
 |D ∩ H0|
|D| ∨1

.
That is, the false discovery rate is the expected proportion of treatments that have been incorrectly
declared as discoveries. Our aim is, thus, to produce discovery setsDs so that the false discovery rate of
each sub-experiment, and thus the overall experiment, is controlled at some levelα∈ (0, 1); more formally,
our goal is to obtain the following guarantee:
FDR(Ds)≤αfor alls∈[t].(3)
To control the variant of the online false discovery rate given in(3), we adapt the asynchronous
e-LOND algorithm due to Xu and Ramdas[65] to Always-On experimentation. Our algorithm to control
the online false discovery rate is given in Algorithm 1.
Algorithm 1Online false discovery rate control in Always-On experimentation
Input:Confidence levelα∈(0,1).
1. Choose a sequence of nonnegative reals,(γr)∞ r=1, such thatP∞ r=1 γr ≤1.
2. Initialize the hypothesis counter:c= 0.
foreach sub-experiments= 1, . . . , tdo
3. Determine the set of new treatments to be tested:A′ s :=A s \ Ss−1 r=1 Ar
foreacha∈ A ′ s do
4. Update the hypothesis counter:c=c+ 1and setγ a :=γ c.
5. Compute the confidence level:αa :=αγ a (|Ds−1|+ 1)
end
end
Notice how Algorithm 1 produces confidence levels for each of the treatments added to the experiment.
We, in turn, use these confidence levels for each treatment arma∈ Ato construct their level-αa sequential
tests for each sub-experiments∈[t],
ϕ(α) s (a) :=1  WNa(s) ≥1/α a 	 .(4)
As soon asϕ(α) s (a) = 1we declare treatment a a discovery and remove it from the experiment. When we
combine this procedure with Algorithm 1, we can guarantee that the online false discovery rate from(3)
is correctly controlled.
Proposition 3.2.Fix a confidence level α∈ (0, 1)and a distributionP ∈ P ∪ Q. Suppose Assumptions 1
to 3 hold, and for each treatmenta∈ Aand any sub-experiments∈ [t], letWNa(s) be its test supermartingale
as defined in(2). Then if we use Algorithm 1 to select the confidence levels for each treatment and use
the sequential level-αtest as defined in(4), we have that for alls∈[t],FDR(D s)≤α.
6

The proof of Proposition 3.2, given in Section D.2, explicitly handles scenarios in which treatments can
be added to the experiment based on past observations, as well as instances in which the evidence used to
declare hypotheses as discoveries (i.e., the test supermartingales) evolves over time. From Proposition 3.2
we can conclude that as long as we select the confidence levels for each treatment using Algorithm 1
and use test supermartingales within our sequential tests, then we can control the false discovery rate in
Always-On experimentation. Hence, the section to follow is solely focused on constructing log-optimal
test supermartingales. To build our understanding, in the main text we consider a setting in which units
are only observed once for the entirety of the experiment, and in Section B we consider a setting in which
units are repeatedly observed throughout the experiment.
4 Constructing Powerful Tests for Always-On Experimentation
We now consider a setting in which units are only observed once across the overall experiment, and
describe how to construct test supermartingales that are growth-rate optimal. We first make explicit the
assumptions that we impose throughout this section.
Assumption 4.We make the following assumptions on the units that are observed in each sub-experiment
s∈ [t]:( i)If a unit participated in sub-experiments, then this means that they have not and will not
participate in any other sub-experiments′ ∈ [t].( ii)The potential outcomes of the units take their values
from the unit interval:Yi(z)∈[0,1], for eachi∈ I s andz∈ Z.
A consequence of Assumption 4 is that the units’ outcomes do not depend on past treatments—as
they can only receive one treatment per experiment. Therefore, in this setting the set of all possible
treatment paths takes the formZ = A ∪ {0}, and the observed outcome for uniti∈ Is is given by
Yi,s ≡Y i,s(Ai,s) := P a∈A∪{0} 1{A i,s =a}Y i,s(a).
In the present setting, we are interested in testing whether the average treatment effect under
distributionP ∈ P ∪ Q, defined for anya∈ Aas ψP(a) := EP [Y1(a)−Y 1(0)], is less than the threshold
δ∈ [−1, 1]. The average treatment effect is unobservable as it depends on both the potential outcome
under treatment a and under control for each unit. Nonetheless, under Assumptions 1, 2 and 4 it is
an identifiable quantity, meaning that under each sub-experiments∈ [t]and letting i∈ Is: ψP(a) =
EPRCT [Yi,s |A i,s =a]−E PRCT [Yi,s |A i,s =0].
We use a slightly modified Horvitz-Thompson estimator [20] (also known as inverse propensity
weighting) to estimate the average treatment effect for each treatment in sub-experiments using the data
of uniti∈ Is. For each treatmenta∈ As it takes the form
bψi,s(a) :=Y i,s
 1{A i,s =a}
bπs(a) − 1{A i,s =0} bπs(0)  ,(5)
where the modified propensity scores for testing the average effect of treatmentatake the form
bπs(a) := πs(a) πs(a) +π s(0) andbπ s(0) := πs(0) πs(a) +π s(0) .(6)
We have slightly abused the notation and made implicit within the definition of the propensity score
for the control the fact that it depends on the treatment being tested. An important property of the
Horvitz-Thompson estimator from (5) is that it is conditionally unbiased.
Lemma 4.1.Fix a distributionP ∈ P ∪ Qand a sub-experiments∈ [t]. Under Assumptions 1 to 4 we
have that for any treatmenta∈ As and unit i∈ Is, the Horvitz-Thompson estimator(5) is a conditionally
unbiased estimator:E PRCT
h
bψi,s(a)

 Fi−1,s, ξi,s(a) = 1 i =ψ P(a).
Under our assumption that the potential outcomes are bounded within the unit interval, the Horvitz-
Thompson estimator is almost surely bounded as−1/bπs(0) ≤ bψi,s(a) ≤ 1/bπs(a). In addition, to use
the test supermartingale from(2), we must ensure that the random variables (and also threshold) are
7

almost surely nonnegative. For this reason, for each sub-experiments∈ Tt(a)we define the transform
gs : [−1/bπs(0),1/bπs(a)]→R ≥0 as follows:
gs(x) := 1 +bπs(0)x .(7)
We use the map from(7) and the Horvitz-Thompson estimator from(5) in the test statistics defined in
(2). Doing so leads to the following proposition, whose proof is given in Section D.4, which states that the
test statistics given in (2) are test supermartingales.
Proposition 4.2.Fix an arm a∈ Aand a distributionP ∈ P(a). Let WNa(t) be the test statistic from
(2) constructed using the Horvitz-Thompson estimator given in(5) and transform defined in(7). Then,
under Assumptions 1 to 4,WNa(t) forms a testP(a)-supermartingale.
Proposition 4.2 allows us to conclude that we can achieve time-uniform type-I error rate control in the
present setting. Nevertheless, we are also interested in constructing test supermartingales that exhibit a
large growth rate whenever we are under the alternative, no matter the treatment schedule and units that
were part of the experiment.
To evaluate the growth-rate optimality of test supermartingales in Always-On experimentation, we
hold the schedule of the overall experiment fixed. More specifically, we assume that the number of
sub-experiments t∈N as well as the sets of active treatmentsAs in each sub-experiments∈ [t]are fixed
and that the only growing quantity is the number of units that participate in each sub-experiment. To
denote a growing number of units in each sub-experiment, we definent := mins∈[t] ns to be the minimum
number of units in any of the sub-experiments. Thus,nt → ∞implies that ns → ∞for all s∈ [t]. Under
the present setting, we assess the growth-rate optimality of test supermartingales that use the estimator
from (5) and transform from (7) with respect to the following comparator class:
W(a) :={W:Wis a testP(a)-supermartingale of the form (2)},(8)
for each treatment a∈ A. Having defined the necessary concepts, we now introduce the notion of
log-optimality in dynamic experiments.
Definition 4.3(Almost-sure log-optimality in Always-On experimentation).Fix an arma∈ Aand a
distributionQ ∈ Q(a). Let W(a)be the class defined in(8). We say that the test supermartingaleWNa(t)
isQ RCT-almost surely log-optimalwith respect to the classW(a), if for anyfWNa(t) ∈ W(a),
lim inf
nt→∞
1
Na(t)

log

WNa(t)

−log

fWNa(t)

≥0Q RCT-almost surely.
IfN a(t) = 0, then we say that the growth rates ofWNa(t) and fWNa(t) are equivalent.
To construct growth-rate optimal test supermartingales, in the sense of Definition 4.3, we run
independent copies of the Universal Portfolio algorithm [11] (as given in(17)) for each arma∈ Aand
restart the algorithms corresponding to the treatments in the active set of arms in every sub-experiment
s∈ [t]. More explicitly, in every sub-experiments∈ [t]and for each unit i∈ Is we compute the portfolio
corresponding to treatmenta∈ As as
λi,s(a)≡UP

W (λ) ˇNa(s;i−1)

whereW (λ) ˇNa(s;i−1) := Y
j∈Is(i−1)
h
(1−λ) +λg s( bψj,s(a))/gs(δ)
iξj,s(a)
,(9)
where we denote the portfolios as a function ofa in order to make it explicit that the portfolios are
computed independently across treatment arms. In the following theorem we establish the almost sure
log-optimality of our test supermartingales when we select the portfolios using the strategy established in
(9).
Theorem 4.4.Fix the treatment schedule for the experiment and an arma∈ A. Let WNa(t) be a testP(a)-
supermartingale of the form(2) constructed using the transformed Horvitz-Thompson estimators(5) and
thresholds (7), and whose portfolios are selected using the strategy from(9). Suppose that Assumptions 1
to 4 hold. Then, for anyQ∈ Q(a), WNa(t) isQ RCT-almost sure log-optimal in the sense of Definition 4.3.
8

The proof of Theorem 4.4 can be found in Section D.5. It consists of deriving a nonasymptotic inequality
on the absolute difference betweenWNa(t) and the process that has oracle access to the numeraire portfolios
(see Section C.1 for more details on these objects). The idea behind the proof resembles those found
in [63] and [51], but departs from these works as the number of data points used to construct the test
supermartingale WNa(t) is random under the present setting. Importantly, Theorem 4.4 establishes that
no matter what the treatment schedule is, the way in which we are constructing the test supermartingales
(i.e., selecting the portfolios) ensures that there is no other test supermartingale within the comparator
class W(a)that could achieve a limiting growth-rate larger than ours. This includes a test supermartingale
that has oracle access to and uses the numeraire portfolios for each treatment arm in each sub-experiment,
as can be seen in Figure 2.
5 Semi-Synthetic Experiments
To test the efficacy of the proposed methods in realistic settings we constructed a set of semi-synthetic
experiments using the Upworthy Research Archive [33], which is a corpus of randomized headline
experiments that were run on an online platform between 2013 and 2015. Treatments consist of headline
image combinations that were shown to users with at least 1,000 impressions with click through rate being
the outcome of interest. On average each month contains 634 treatments per month. We construct a
semi-synthetic Always-On experiment by assembling all tests that occurred within a given calendar month
(18 total months), and using the observed timestamp for each treatment as the starting time within the
overall Always-On experiment. See Section A.2 for details.
0.0 0.2 0.4 0.6 0.8 1.0
Fraction of window traffic
10−6
10−5
10−4
10−3
10−2
FDR (log scale)
α = 0.05
(a) FDR over time
Proposed (Ours)
Oracle
Uncorrected†
Peeking†
Ours Sans Reward
Group Sequential
0.0 0.2 0.4 0.6 0.8 1.0
Fraction of window traffic
0
25
50
75
100
125
150
175Mean true discoveries
(b) Power: true discoveries over time
Proposed (Ours)
Oracle
Uncorrected†
Peeking†
Ours Sans Reward
Group Sequential
103 104 105 106 107
Na (arm sample size)
0.0002
0.0003
0.0004
0.0005
0.0006
0.0007
0.0008Growth-rate, log(WNa )/Na
(c) Growth-rate
Proposed (Ours)
UP without restart
Oracle
Figure 2: (a) FDR over window traffic, with10concurrent treatments. (b) Mean true discoveries over window
traffic, with10concurrent treatments. (c) Empirical growth-rates for our proposed process, one that selects the
portfolios via the Universal Portfolio algorithm but without restarting the algorithm in each sub-experiment, and
a process that has oracle access to the numeraire portfolios.
We compare the proposed method to an oracle that has access to the true treatment effects, to an
ablation of our method that ignores the discovery term from the confidence schedule (which we denote as
“Ours Sans Reward”), to a version of our method without false discovery rate correction (“uncorrected”);
and to early peeking in which results are monitored without correction (“peeking”). Figures 2 and 6 show
the results. Consistent with our theoretical results, the proposed method controls the false discovery rate
(FDR) below the nominalα = 0.05level across the traffic levels. By contrast, the uncorrected variants
have an order-of-magnitude worse FDR control. We also see that our method discovers roughly 1,900
true effects per replication across the 18 months (see also Figure 6), 12% more than the ablated version
without reward and within 30% of the oracle. Finally, the group sequential baseline has a lower false
discovery rate at the cost of a substantially more conservative discovery rate.
9

6 Conclusion
In this work we introduced a statistical framework to run randomized experiments in a way that allows
treatments to be dynamically added and removed. The goal in our framework is to test the effectiveness
of treatments while simultaneously controlling the online false discovery rate. As such, we based our
framework on the sequential hypothesis testing-by-betting literature, and showed how to construct test
supermartingales that test whether the treatment effect is greater than some threshold. We considered
two settings: one in which each unit is observed at most once within the same experiment and another in
which the experiment is run over the same set of units. We provided strategies to select the portfolios
under these two settings that result in growth-rate optimal test supermartingales, no matter the treatment
schedule. Furthermore, we provided and analyzed an algorithm that controls the online false discovery
rate in the Always-On setting. Finally, experiments conducted using semi-synthetic data based on the
Upworthy repository of online experiments provide additional evidence that the proposed methodology
closely follows theory in empirical settings.
We envision that our Always-On framework will be useful in settings that encompass drug discovery,
experimentation in tech companies, and testing for (emerging) capabilities of LLMs, amongst many others.
To further improve the power of our framework, we outline some interesting directions for future work.
One direction for future work is how to adaptively select the propensity scores to maximize the number
of discoveries made in the experiment. A second direction for future work is designing the treatment
schedule; that is, coming up with strategies to remove treatments from the experiment while controlling
for the type-II error.
Acknowledgments
We would like to thank Keegan Harris, Emma Pierson, Lei Shi, Ritwik Sinha, Vasilis Syrgkanis, Ryan Tib-
shirani, Nikos Vlassis, Serena Wang, and Ian Waudby-Smith for insightful conversations. MJ acknowledges
funding from the European Union (ERC-2022-SYG-OCEAN-101071601). Views and opinions expressed
are however those of the author(s) only and do not necessarily reflect those of the European Union or the
European Research Council Executive Agency. Neither the European Union nor the granting authority
can be held responsible for them.
10

References
[1] Adaptive Platform Trials Coalition. Adaptive platform trials: definition, design, conduct and reporting
considerations.Nature Reviews Drug Discovery, 18(10):797–807, 2019.
[2] J. Bartroff and J. Song. Sequential tests of multiple hypotheses controlling false discovery and
nondiscovery rates.Sequential analysis, 39(1):65–91, 2020.
[3] Y. Benjamini and Y. Hochberg. Controlling the false discovery rate: a practical and powerful approach
to multiple testing.Journal of the Royal statistical society: series B (Methodological), 57(1):289–300,
1995.
[4] S. M. Berry, J. T. Connor, and R. J. Lewis. The platform trial: an efficient strategy for evaluating
multiple treatments.JAMA, 313(16):1619–1620, 2015.
[5] B. Bharti, A. Pal, and J. Sulam. Global sequential testing for multi-stream auditing.arXiv preprint
arXiv:2602.21479, 2026.
[6] I. Bojinov, A. Rambachan, and N. Shephard. Panel experiments and dynamic causal effects: A finite
population perspective.Quantitative Economics, 12(4):1171–1214, 2021.
[7] A. Boruvka, D. Almirall, K. Witkiewitz, and S. A. Murphy. Assessing time-varying causal effect
moderation in mobile health.Journal of the American Statistical Association, 113(523):1112–1121,
2018.
[8] L. Breiman. Optimal gambling systems for favorable games. InFourth Berkeley Symposium: University
of California, 1961.
[9] B. Chugg, S. Cortes-Gomez, B. Wilder, and A. Ramdas. Auditing fairness by betting.Advances in
Neural Information Processing Systems, 36:6070–6091, 2023.
[10] E. Clerico. On the optimality of coin-betting for mean estimation.International Journal of
Approximate Reasoning, page 109550, 2025.
[11] T. M. Cover. Universal portfolios.Mathematical Finance, 1(1):1–29, 1991.
[12] T. M. Cover and E. Ordentlich. Universal portfolios with side information.IEEE Transactions on
Information Theory, 42(2):348–363, 1996.
[13] T. M. Cover and J. A. Thomas.Elements of Information Theory. John Wiley & Sons, 1999.
[14] D. A. Darling and H. E. Robbins. Confidence sequences for mean, variance, and median.Proceedings
of the National Academy of Sciences, 58 1:66–8, 1967.
[15] C. P. Farrington and G. Manning. Test statistics and sample size formulae for comparative binomial
trials with null hypothesis of non-zero risk difference or non-unity relative risk.Statistics in medicine,
9(12):1447–1454, 1990.
[16] L. Fischer, Z. Xu, and A. Ramdas. An online generalization of the (e-) benjamini-hochberg procedure.
arXiv preprint arXiv:2407.20683, 2024.
[17] D. P. Foster and R. A. Stine. α-investing: a procedure for sequential control of expected false
discoveries.Journal of the Royal Statistical Society Series B: Statistical Methodology, 70(2):429–444,
2008.
[18] P. Grünwald, R. de Heide, and W. Koolen. Safe testing.Journal of the Royal Statistical Society B
(with discussion), 86(5):1091–1128, 2024.
[19] H. Hendriks. Test martingales for bounded random variables.arXiv preprint arXiv:2109.08923, 2021.
11

[20] D. G. Horvitz and D. J. Thompson. A generalization of sampling without replacement from a finite
universe.Journal of the American Statistical Association, 47(260):663–685, 1952.
[21] S. R. Howard, A. Ramdas, J. McAuliffe, and J. Sekhon. Time-uniform, nonparametric, nonasymptotic
confidence sequences.The Annals of Statistics, 49(2):1055–1080, 2021.
[22] G. Imbens, L. Masoero, A. Rakhlin, T. S. Richardson, and S. Vijaykumar. Demonstration experiments.
arXiv preprint arXiv:2603.06941, 2026.
[23] K. Jamieson and L. Jain. A bandit approach to sequential experimental design with false discovery
control.Advances in Neural Information Processing Systems, 31, 2018.
[24] A. Javanmard and A. Montanari. On online control of false discovery rate.arXiv preprint
arXiv:1502.06197, 2015.
[25] A. Javanmard and A. Montanari. Online rules for control of false discovery rate and false discovery
exceedance.The Annals of statistics, 46(2):526–554, 2018.
[26] I. Karatzas and C. Kardaras. The numéraire portfolio in semimartingale financial models.Finance
and Stochastics, 11:447–493, 2007.
[27] J. L. Kelly. A new interpretation of information rate.The Bell System Technical Journal, 35(4):
917–926, 1956.
[28] R. Kohavi, D. Tang, and Y. Xu.Trustworthy Online Controlled Experiments: A Practical Guide to
A/B Testing. Cambridge University Press, 2020.
[29] M. Larsson, A. Ramdas, and J. Ruf. The numeraire e-variable and reverse information projection.
The Annals of Statistics, 53(3):1015–1043, 2025.
[30] P. Liao, P. Klasnja, A. Tewari, and S. A. Murphy. Sample size calculations for micro-randomized
trials in mhealth.Statistics in medicine, 35(12):1944–1971, 2016.
[31] Z. Lin, W. Ma, Z. Ren, and Y. Wei. Sample-efficient multiple testing with adaptive data collection.
arXiv preprint arXiv:2609.26651, 2026.
[32] J. B. Long Jr. The numeraire portfolio.Journal of Financial economics, 26(1):29–69, 1990.
[33] J. N. Matias, K. Munger, M. A. Le Quere, and C. Ebersole. The upworthy research archive, a time
series of 32,487 experiments in us media.Scientific Data, 8(1):195, 2021.
[34] J. Neyman. Sur les applications de la théorie des probabilités aux experiences agricoles: Essai des
principes.Roczniki Nauk Rolniczych, 10(1):1–51, 1923.
[35] F. Orabona and K.-S. Jun. Tight concentrations and confidence sequences from the regret of universal
portfolio.IEEE Transactions on Information Theory, 70(1):436–455, 2023.
[36] A. Podkopaev and A. Ramdas. Sequential predictive two-sample and independence testing.Advances
in Neural Information Processing Systems, 36:53275–53307, 2023.
[37] A. Podkopaev, P. Blöbaum, S. Kasiviswanathan, and A. Ramdas. Sequential kernelized independence
testing. InInternational Conference on Machine Learning, pages 27957–27993. PMLR, 2023.
[38] A. Ramdas and R. Wang. Hypothesis testing with e-values.Foundations and Trends®in Statistics,
1(1-2):1–390, 2025.
[39] A. Ramdas, T. Zrnic, M. Wainwright, and M. Jordan. Saffron: an adaptive algorithm for online
control of the false discovery rate. InInternational conference on machine learning, pages 4286–4294.
PMLR, 2018.
12

[40] A. Ramdas, J. Ruf, M. Larsson, and W. Koolen. Admissible anytime-valid sequential inference must
rely on nonnegative martingales.arXiv preprint arXiv:2009.03167, 2020.
[41] A. Ramdas, P. Grünwald, V. Vovk, and G. Shafer. Game-theoretic statistics and safe anytime-valid
inference.Statistical Science, 38(4):576–601, 2023.
[42] H. Robbins. Statistical methods related to the law of the iterated logarithm.The Annals of
Mathematical Statistics, 41(5):1397–1409, 1970.
[43] H. Robbins and D. Siegmund. Iterated logarithm inequalities and related statistical procedures.
Mathematics of the Decision Sciences, 2:267–279, 1968.
[44] H. Robbins and D. Siegmund. The expected sample size of some tests of power one.The Annals of
Statistics, 2(3):415–436, 1974.
[45] D. S. Robertson, J. M. Wason, F. König, M. Posch, and T. Jaki. Online error rate control for platform
trials.Statistics in Medicine, 42(14):2475–2495, 2023.
[46] J. M. Robins. Correcting for non-compliance in randomized trials using structural nested mean
models.Communications in Statistics-Theory and methods, 23(8):2379–2412, 1994.
[47] J. M. Robins. Optimal structural nested models for optimal sequential decisions. InProceedings of
the Second Seattle Symposium in Biostatistics: analysis of correlated data, pages 189–326. Springer,
2004.
[48] D. B. Rubin. Estimating causal effects of treatments in randomized and nonrandomized studies.
Journal of Educational Psychology, 66(5):688, 1974.
[49] J. J. Ryu and A. Bhatt. On confidence sequences for bounded random processes via universal
gambling strategies.IEEE Transactions on Information Theory, 2024.
[50] J. J. Ryu, J. Kwon, B. Koppe, and K.-S. Jun. Improved offline contextual bandits with second-order
bounds: Betting and freezing.arXiv preprint arXiv:2502.10826, 2025.
[51] R. J. Sandoval, I. Waudby-Smith, and M. I. Jordan. Multi-armed sequential hypothesis testing by
betting.arXiv preprint arXiv:2603.17925, 2026.
[52] M. Santacatterina, F. M. Giron, X. Zhang, and I. Díaz. Identification and estimation of causal effects
using non-concurrent controls in platform trials.Statistics in Medicine, 44(6):e70017, 2025.
[53] S. Senn.Cross-over Trials in Clinical Research. Wiley, 2nd edition, 2002.
[54] G. Shafer and V. Vovk.Probability and finance: it’s only a game!, volume 491. John Wiley & Sons,
2005.
[55] G. Shafer and V. Vovk.Game-theoretic foundations for probability and finance. John Wiley & Sons,
2019.
[56] S. Shekhar and A. Ramdas. Nonparametric two-sample testing by betting.IEEE Transactions on
Information Theory, 70(2):1178–1203, 2023.
[57] J. Tian and A. Ramdas. Addis: an adaptive discarding algorithm for online fdr control with
conservative nulls.Advances in neural information processing systems, 32, 2019.
[58] J. Ville. Étude critique de la notion de collectif.Bulletin of the American Mathematical Society, 45
(11):824, 1939.
[59] A. Wald. Sequential tests of statistical hypotheses.The Annals of Mathematical Statistics, 16(2):
117–186, 1945.
13

[60] A. Wald.Sequential Analysis. Wiley, New York, 1947.
[61] Q. Wang, R. Wang, and J. Ziegel. E-backtesting.Management Science, 2025.
[62] I. Waudby-Smith and A. Ramdas. Estimating means of bounded random variables by betting.Journal
of the Royal Statistical Society Series B, 86(1):1–27, 2024.
[63] I. Waudby-Smith, R. Sandoval, and M. I. Jordan. Universal log-optimality for general classes of
e-processes and sequential hypothesis tests.arXiv preprint arXiv:2504.02818, 2025.
[64] J. Woodcock and L. M. LaVange. Master protocols to study multiple therapies, multiple diseases, or
both.New England Journal of Medicine, 377(1):62–70, 2017.
[65] Z. Xu and A. Ramdas. Online multiple testing with e-values. InInternational Conference on Artificial
Intelligence and Statistics, pages 3997–4005. PMLR, 2024.
[66] F. Yang, A. Ramdas, K. G. Jamieson, and M. J. Wainwright. A framework for multi-a (rmed)/b
(andit) testing with online fdr control.Advances in Neural Information Processing Systems, 30, 2017.
[67] S. Zehetmayer, M. Posch, and F. Koenig. Online control of the false discovery rate in group-sequential
platform trials.Statistical Methods in Medical Research, 31(12):2470–2485, 2022.
[68] T. Zrnic, A. Ramdas, and M. I. Jordan. Asynchronous online testing of multiple hypotheses.Journal
of Machine Learning Research, 22(33):1–39, 2021.
14

A Further Information on Always-On Experimentation
In this section we provide further details about our Always-On experimentation framework. Recall that
one of our goals in proposing this framework is to give practitioners the flexibility to add and remove
treatments from a running experiment. We formalize the data collection protocol of the Always-On
experimentation framework in Algorithm 2.
Algorithm 2Data collection protocol
Nature samples the potential outcomes(Yi(z))z∈Z ∼Pfor unitsi∈ I.
foreach sub-experiments= 1, . . . , tdo
1. Determine the set of active treatmentsAs.
2. Choose the propensity scoreπs := (πs(a))a∈As∪{0}.
foreach uniti∈ Is do
3. Randomly draw the treatment assignmentAi,s ∼RCT s ≡Categorical As∪{0}(πs).
4. Observe the outcomeYi,s.
end
end
As we described in Section 3.1, the data collected according to Algorithm 2 is used to construct
test supermartingales for each of the active treatments. An important concept—which we expand on in
Section C—in testing by betting is that of portfolio regret, as it provides a sufficient condition for achieving
asymptotic almost sure log-optimality. Nonetheless, in Always-On experimentation we must consider a
modified definition of portfolio regret. More specifically, we must consider a definition of portfolio regret
for a particular sub-experiments∈[t]with respect to a particular arma∈ As.
Definition A.1(Per-sub-experiment portfolio regret).Fix a sub-experiment s∈ [t], a treatmenta∈ As,
and let (Ai,s, Yi,s)i∈Is be the data collected in sub-experiments. Let W ˇNa(s) form a process of the form (2). We define theper-sub-experiment portfolio regretfor treatmentain sub-experimentsto be
R ˇNa(s) := max λ∈[0,1]
X
i∈Is
ξi,s(a) log

1−λ+λg s( bψi,s(a))/gs(δ)

−log

W ˇNa(s)

,
where we recall thatξi,s(a) :=1{A i,s =aorA i,s =0}.
The reason we must now consider a per-sub-experiment and per-arm definition of portfolio regret is
because each sub-experiment has a particular joint distribution over the potential outcomes and treatment
assignments. These different distributions, in turn, induce their own numeraire portfolios (see Section C.1),
which means that for each sub-experiment we must construct processes that are “competitive” against
those that have oracle access to these numeraire portfolios. Waudby-Smith et al.[63] showed that to
construct processes that are competitive against an oracle that has access to the numeraire portfolios
is to use algorithms that select the portfolios in such a way that the test supermartingales they induce
enjoysub-linearportfolio regret; hence, explaining our portfolio selection strategy from Section 4. In the
following subsection we present experiments whose aim is to provide some empirical comparison between
Always-On experimentation and platform trials.
A.1 Simulations to compare Always-On experimentation versus platform
trials
Conceptually, Always-On experimentation is a way to run platform trials while allowing for continuous
monitoring and arbitrary treatment schedules. In this section we explore what is the price we have to pay
15

in Always-On experimentation relative to platform trials.
To understand the price to pay, we run various simulations comparing our Always-On experimentation
framework to an adapted version of the platform trials design from [67]. More specifically, we use the
gs-LOND algorithm proposed by Zehetmayer et al.[67] in conjunction with the O’Brien–Fleming boundary
to allow for interim analyses in a multiple testing setting. Furthermore, we use the Farrington-Manning
test [15] as our statistic to assess the effect of each treatment in the platform trial, as we consider Bernoulli
outcomes within our simulations.
In the simulations we compare the difference in true discoveries made by our Always-On experimentation
framework against the true discoveries made by the specification of the platform trial described in the
previous paragraph. In each of the simulations we introduce a total of 60 treatments to the experiment,
where 30 of them are under the null while the rest are under the alternative. In each of the simulations,
we endow all the treatments under the alternative with the same effect (and similarly for those under the
null) and vary the effect of the treatments under the alternative across simulations.
In the simulations we vary the maximum number of units allowed to be enrolled into a treatment
(i.e., the cap on the number of units that can be assigned to each treatment) and consider different
“peeking schedules” (i.e., number of times at which the test statistic can be computed) for always-on
experimentation. Treatments are removed as soon as they are declared a discovery or whenever they hit
the cap on the allowed number of units. Below we present the results of simulations for different treatment
effects when testing that the effect is greater than the thresholdδ= 0.05.
500 1000 2000 3000 4000 5000
Maximum observations assigned
to each treatment
−30
−20
−10
0
Difference in true discoveries
(Always-On − platform trials)
500 1000 2000 3000 4000 5000
Maximum observations assigned
to each treatment
−20%
0%
20%
40%
60%
Participatns saved relative
to platform trials
Figure 3: The true treatment effect of all30treatments under the alternative is equal to0.25. The interim analysis
in the platform trials only take place when50%of the maximum number of units allowed for each treatment have
been observed.
500 1000 2000 3000 4000 5000
Maximum observations assigned
to each treatment
−30
−20
−10
0
Difference in true discoveries
(Always-On − platform trials)
500 1000 2000 3000 4000 5000
Maximum observations assigned
to each treatment
−20%
0%
20%
40%
60%
Participatns saved relative
to platform trials
Figure 4: The true treatment effect of all30treatments under the alternative is equal to0.55. The interim analysis
in the platform trials only take place when50%of the maximum number of units allowed for each treatment have
been observed.
We are also interested in understanding the effect of being able to perform more interim analyses in
platform trials has on the difference in true discoveries and the units needed to make such discoveries.
16

Figure 5 depicts the effect that being able to perform more interim analyses in platform trials has on the
difference in true discoveries with Always-On experimentation and the relative number of participants
needed to make such discoveries.
500 1000 2000 3000 4000 5000
Maximum observations assigned
to each treatment
−30
−20
−10
0
Difference in true discoveries
(Always-On − platform trials)
500 1000 2000 3000 4000 5000
Maximum observations assigned
to each treatment
−20%
0%
20%
40%
60%
Participatns saved relative
to platform trials
500 1000 2000 3000 4000 5000
Maximum observations assigned
to each treatment
−30
−20
−10
0
Difference in true discoveries
(Always-On − platform trials)
500 1000 2000 3000 4000 5000
Maximum observations assigned
to each treatment
−20%
0%
20%
40%
60%
Participatns saved relative
to platform trials
Figure 5: The true treatment effect of all30treatments under the alternative is equal to0.35. In the top row we
only perform one interim analysis when50%of the maximum number of units allowed for each treatment have
been observed. In the bottom row we perform interim analyses when25%,50%, and75%of the maximum number
of units allowed for each treatment have been observed.
A.2 Further information about the semi-synthetic experiment.
We fix a maximum number of concurrent treatments at ten, and create a queue in which a treatment
is allowed to enter only after another treatment has been removed. Within each month, the control
mean is simulated by taking the median click-through-rate (CTR) of all of the controls tested throughout
the month, i.e., CTR0 = median(CTR0,j), where j indexes the individual tests run that month. The
outcomes are then simulated using the historical CTRs for each of the treatments, using the relative lift,
ρa = CTRa/CTR0,j, where a indexes the treatment andj is the corresponding test for treatmenta. We
then use the same proportion with respect to the constructed always-on control,CTRsim a = ρa ·CTR 0. A
treatment is removed from an experiment either when it has been declared statistically significant with
respect to the control or once it exceeds the total observation budget, i.e., the number of impressions it
received in the dataset,Na ≥N max a . Every month was run with 200 replications each.
B Always-On Experimentation for Testing Treatment Histories
In this section we focus on a setting in which it is of interest to test whether there exists a treatment
history for which a treatment induces a positive treatment effect. For this reason, the experiment is run
over the same set of units—meaning that units receive multiple treatments throughout their experiment.
This, in turn, implies that the observed outcomes are now functions of the history of treatments (or
treatment path) a unit has received. We define thetreatment historyof uniti starting in sub-experiment
r∈ [t]and going up to sub-experiments∈ [t], such thatr≤s , asZ i,r:s := (Ai,r, . . . , Ai,s). We denote the
17

10−610−510−410−310−2
1 − FDR (log scale, decreasing rightward)
1000
1500
2000
2500
3000Mean true discoveries
Proposed (Ours)
Ours Sans Reward
Oracle
Uncorrected
Peeking
Group Sequential
α = 0.05
Validity-power tradeoff
Figure 6: Validity and power at the primary traffic level (10concurrent treatments): mean false discovery rate and
mean true discoveries per replication.
set of all observable treatment histories starting in sub-experimentr and going up to sub-experiments as
Zr:s :=
n
(ar, . . . , as)∈(A ∪ {0})s−r+1

 ∀j∈[r:s], a j ∈ Aj ∪ {0} o .
Since units can receive more than one treatment in the experiment, we must now worry about carryover
effects, and denote asℓ∈N 0 the duration (in terms of sub-experiments) of the carryover effects—see [53, 6]
for examples of other settings in which carryover effects are of concern. Having carryover effects that last
for ℓ sub-experiments implies that theeffectivetreatment history of uniti∈ Iin sub-experiment s∈ [t]
is given byZi,s ≡ Zi,s−ℓ:s := (Ai,s−ℓ, . . . , Ai,s), and the effective set of observable treatment histories is
Zs−ℓ:s—where we remark that ifℓ≥s, then we lets−ℓ= 1.
We assume each uniti∈ Ihas potential outcomesYi(z)for eachz ∈ St s=1 Zs−ℓ:s. Given that the
carryover effects last forℓ sub-experiments, the observed outcome for uniti in sub-experiment s now
takes the formYi,s := Yi(Zi,s) = P z∈Zs−ℓ,s 1{Z i,s =z}Y i(z). In the present setting we assume that the potential outcomes can take only a finite number of outcome levels.
Assumption 5(Finite number of outcome levels).We assume all potential outcomes take a finite number
of outcome levels, and that they take their values from the set{0, . . . , m}for some m∈N such that
m <∞.
For the rest of the paper, we define the shorthandYi,r:s := (Yi,r, . . . , Yi,s) to denote the outcomes
that have been observed for uniti starting from sub-experimentr and going up to sub-experiments. We
define the history of observed outcomes and treatments for uniti∈ IasH i,r:s := (Yi,r:s,Z i,r:s), where
for the first sub-experiment and instances in whichℓ = 0these histories are empty. Furthermore, we
denote the set ofobservedhistories starting in sub-experiment r∈ [t]and going up to sub-experiment
s∈[t]asH r:s :={H i,r:s ,∀i∈[n]}, and we use the shorthandH s ≡ Hs−ℓ+1:s.
In addition to assuming that the outcomes are functions of only the pastℓ treatments, we impose the
following Markovian assumption on the distribution from which the outcomes are sampled.
Assumption 6(Markov distribution over outcomes).Fix a distributionP ∈ P ∪ Q, let ℓ∈N 0 be the
duration of the carryover effects, and define the realized history for uniti from sub-experiment r up to
sub-experiment s− 1ash i,r:s−1 := (yi,r:s−1,z i,r:s−1). We say that the distribution over the outcomes is
ℓ-Markovif for each sub-experiment s∈ [t], treatment a∈ As, and outcome valuey∈ {0, . . . , m}it holds
that
PP (Yi(Zi,s−ℓ:s−1, a) =y|H i,1:s−1 =h i,1:s−1) =P P (Yi(Zi,s−ℓ:s−1, a) =y|H i,s−ℓ:s−1 =h i,s−ℓ:s−1).
18

A consequence of Assumption 6 is that the expected outcomes are alsoℓ-Markov—i.e., only depend on
the treatments and observed outcomes from the pastℓ sub-experiments. We leverage this assumption
and define our target estimand with respect to the histories from the setHs−1. More formally, in
sub-experiment s∈ [t], we define theper-sub-experiment treatment effectfor eacha∈ As for those units
whose historyH i,s−1 ≡H i,s−ℓ:s−1 is equal toh∈ Hs−1 as
ψP(a,h) :=E P [Y1(Z1,s−ℓ:s−1, a)−Y1(Z1,s−ℓ:s−1,0)|H 1,s−1 =h].(10)
Our estimand from(10) captures the effect of a treatmenta∈ As when compared against the control and
when we condition on the history of realized outcomes and treatments that were assigned throughout the
past ℓ sub-experiments. For the first sub-experiment we can see how the per sub-experiment treatment
effect simplifies toψP(a) := EP [Y1(a)−Y 1(0)], which is the standard average treatment effect for treatment
a∈ A1. We note how the estimand in(10) resembles the blip function [46, 47]; albeit, it only contrasts
the outcome under treatmenta against the control in sub-experiments and not two different treatment
regimes. Moreover, our estimand is analogous to the proximal effect from micro-randomized trials [30, 7],
but differs from the proximal effect because these estimands typically condition on the availability of units
and a summary of the pre-treatment history.
In the present Always-On setting, we slightly modify the hypotheses tests from(1) and test for each
treatmenta∈ Athe following null versus alternative hypotheses
P(a) :={P| ∀h∈ H(a), ψP(a,h)≤δ}versusQ(a) :={P| ∃h∈ H(a), ψP(a,h)> δ}, (11)
where H(a) := S s∈Tt(a) Hs−1 with H0 = {∅}. We remark thatH(a)is partially observed throughout the experiment and that it is only fully observed until the last sub-experiment in which treatmenta
was active. This is due to the fact thatH(a)consists of all possible histories that were observed in the
sub-experiments in which treatmenta was active, and we can only determine all these histories until after
the experiment as a whole comes to an end.
The hypotheses from(11) depend on the per-sub-experiment treatment effect, a quantity that we
must estimate. For each sub-experiments∈ [t]we use the Horvitz-Thompson estimator to estimate the
per-sub-experiment treatment effect for treatmenta∈ As for those units whose treatment histories were
h∈ Hs−1 and this takes the form
bψi,s(a,h) :=Y i,s
 1{A i,s =a}
bπs(a) − 1{A i,s =0} bπs(0)  ,(12)
where the modified propensity scores for testing the average treatment effect of treatmenta are defined
as in(6). We remark that the observed outcomeYi,s is a function of both the treatment historyZi,s−1
and the treatment assignment in sub-experiments; that is Yi,s ≡Y i (Zi,s−ℓ:s−1, Ai,s). Furthermore,
Yi,s can be dependent on the observed outcomesYi,s−1 =y s−1 encoded in the historyh. Under the
present construction, the estimator from(12) is a conditionally unbiased estimator for the per-sub-
experiment treatment effect—where the conditioning is on the filtrationFi−1,s and inclusion indicator
ξi,s(a,h) :=1{(A i,s =aorA i,s =0) andH i,s−1 =h}being one.
Lemma B.1.Fix a distributionP ∈ P ∪ Q, a sub-experiment s∈ [t], and an arm a∈ As. Under
Assumptions 1 to 3, 5 and 6, the Horvitz-Thompson estimator from(12) for unit i∈ Is belonging to strata
h ∈ Hs−1 is a conditionally unbiased estimator, meaning thatEPRCT
h
bψi,s(a,h)

 Fi−1,s, ξi,s(a,h) = 1 i =
ψP(a,h).
The proof of Lemma B.1 can be found in Section D.6. The Horvitz-Thompson estimator in the present
setting takes its values from the intervalbψi,s(a) ∈[−m/bπs(0), m/bπs(a)], which means that we must again
apply a transformation so that its values are almost surely nonnegative. In this setting, the transformation
function for each sub-experiments∈ Tt(a),g s : [−m/bπs(0), m/bπs(a)]→R ≥0, is given by
gs(x) :=m+bπ s(0)x .(13)
Using the map from(13) alongside the estimator from(12) in the test statistic given in(2) results in a
testP(a)-supermartingale.
19

Proposition B.2.Fix an arm a∈ Aand a distributionP ∈ P(a). Let WNa(t) be the test statistic from
(2) constructed using the Horvitz-Thompson estimator from(12) and the transform defined in(13). Then,
under Assumptions 1 to 3, 5 and 6,WNa(t) forms a testP(a)-supermartingale.
Proof. Proposition B.2 follows immediately from Lemma B.1, Lemma 3.1 when the inclusion event
conditioned on is{ξi,s(a,h) = 1}, where ξi,s(a, h) := 1{(A i,s =aorA i,s =0) andH i,s−1 =h} , and the
fact thatg s(·)is a non-decreasing linear map for eachs∈[t].■
As in the main text, one of our goals is to construct powerful test statistics. Nonetheless, the comparator
class we consider in this section is one whose test supermartingales are constructed using the estimator
from (12) and transform from (13). For each treatmenta∈ A, we denote it as
W(a) :={W:Wis a testP(a)-supermartingale of the form (2)}.
In the present setting, we can no longer follow the same strategy to select the portfolios as that from
the main text. This is because in the present setting we get to run the experiment over the same set
of units; thus, we get to repeatedly observe the same unit and must take into account the temporal
dependency this induces—since the potential outcomes for each unit can be dependent with each other.
Assumptions 5 and 6 alongside our carryover effect assumption limit the extent of the temporal dependency.
More specifically, the temporal dependency in sub-experiments is encoded in the historyh∈ Hs−1. As a
consequence, each historyh ∈ Hs−1 and treatment a∈ As pair induces (possibly) different numeraire
portfolios. For this reason, in the present setting we must control a version of per-sub-experiment portfolio
regret that takes into account each historyh∈ Hs−1.
Definition B.3(Per-sub-experiment and history portfolio regret).Fix a sub-experiment s∈ [t], a
treatment a∈ As, and let( Ai,s, Yi,s)i∈Is be the data collected in sub-experiments. Let W ˇNa,h form a
process of the form(2) but just over those units whose history is equal toh∈ Hs−1. We define the
per-sub-experiment and history portfolio regretfor treatmenta and historyh ∈ Hs−1 in sub-experiment s
to be
R ˇNa,h(s) := max λ∈[0,1]
X
i∈Is
ξi,s(a,h) log

1−λ+λg s( bψi,s(a,h))/g s(δ)

−log

W ˇNa,h(s)

,
where we have definedξi,s(a,h) :=1{(A i,s =aorA i,s =0) andH i,s−1 =h}.
Hence, we must now select the portfolios in such a way that controls the per-sub-experiment and
history portfolio regret. To do so, we now use independent copies of the universal portfolio algorithm for
each history in each sub-experiment. Hence, the portfolio for arma∈ As in sub-experiment s∈ [t]for
uniti∈ Is whose history ish∈ Hs−1 is given by
λi,s(a,h)≡UP

W (λ) ˇNa,h(s;i−1)

(14)
whereW (λ) ˇNa,h(s;i−1) := Y
j∈Is(i−1)
h
(1−λ) +λg s( bψj,s(a,h))/g s(δ)
iξj,s(a,h)
.
This strategy results in test supermartingales that are asymptotically almost sure log-optimal.
Theorem B.4.Fix the treatment schedule for the experiment and an arma∈ A. Let WNa(t) be a test
P(a)-supermartingale of the form(2) constructed using the transformed Horvitz-Thompson estimators and
thresholds given in(12) and (13), respectively, and whose portfolios are selected using the strategy from
(14). Suppose that Assumptions 1 to 3, 5 and 6 hold. Then, for anyQ∈ Q(a), WNa(t) isQ RCT-almost
sure log-optimal—in the sense of Definition 4.3—within the classW(a).
We provide the proof of Theorem B.4 in Section D.7. It follows similar steps to the proof of Theorem 4.4,
but controls the additional complexity that arises from running the experiment over the same set of units.
Hence, Theorem B.4 states that regardless of the treatment schedule, we can construct powerful test
statistics in Always-On experimentation even in settings where we get to repeatedly test over the same set
of units.
20

C Sequential hypothesis testing by betting
We now review some important concepts of sequential hypothesis testing by betting—a research program
whose inception can be traced back to the works of Abraham Wald [59, 60] and Herbert Robbins and
colleagues [14, 43, 42, 44]. For in-depth reviews, see the books of Shafer and Vovk [54, 55], Ramdas and
Wang [38], and the review paper of Ramdas et al. [41].
Let( Yn)n∈N be a sequence of i.i.d. random variables on a filtered space(Ω,F ), where F ≡(Fn)n∈N0
is the filtration generated by(Yn)n∈N and F0 = {Ω,∅} is the trivial sigma-algebra. We are particularly
interested in testing some null hypothesis—which is represented by the collection of distributionsP—
against an alternative—from a collection of distributionsQ—such that P ∩ Q= ∅. In testing by betting,
one fixes a desired type-I error rateα∈ (0, 1)and aims to construct a binary-valuedF-adapted map
(ϕ(α) n )n∈N, where ϕ(α) n = 1should be interpreted as “reject the null” andϕ(α) n = 0as “do not reject.” The
map ϕ(α) n is commonly referred to as the “level-α sequential test.” Importantly, it is desired that the
level-αsequential test provides the following guarantee:
sup
P∈P
PP

∃n∈N:ϕ (α) n = 1  ≤αor equivalentlysup
P∈P
PP

ϕ(α) τ = 1  ≤α ,(15)
where τ is an arbitrary F-stopping time, meaning that {τ=n} ∈ Fn for any n∈N . One way of
constructing such tests is viatest supermartingales.
Definition C.1(Test supermartingales).Let( Wn)n∈N be an F-adapted process, meaning thatWn is Fn-
measurable for eachn∈N . For a given distributionP∈ P, we say that(Wn)n∈N is a testP-supermartingale
if:
(i)(W n)n∈N0 is aP-supermartingale, meaning thatE P [Wn | Fn−1]≤W n−1 P-almost surely,
(ii)W n ≥0for everyn∈NP-almost surely, and
(iii)E P [W1]≤1.
We say that(Wn)n∈N0 is a testP-supermartingale if it is a testP-supermartingale for everyP∈ P.
In this work we focus on test supermartingales that take the following form
Wn :=
nY
i=1
[(1−λ i) +λ iEi],(16)
where( λn)n∈N is a[0 , 1]-valued predictable process (in the sense thatλn is Fn−1-measurable for every
n∈N ), and( En)n∈N are sequential e-variables under the null hypothesis P—meaning that En is
nonnegative withP-probability one andE P [En | Fn−1]≤1for everyP∈ P.
Level-α sequential tests can be constructed by thresholding testP-supermartingales at1 /α, and
Ramdas et al.[40] show that this is the only admissible way to construct level-α sequential tests. More
specifically, letting ϕ(α) n := 1{W n ≥1/α} we can satisfy the type-I error control from(15) by appealing
to Ville’s inequality for nonnegative supermartingales [58]:
sup
P∈P
PP

∃n∈N:ϕ (α) n = 1  = sup
P∈P
PP (∃n∈N:W n ≥1/α)≤αE P [W1]≤α .
Indeed, many of the sequential tests that have been proposed in the literature have been constructed in
this way, and we refer the reader to [42, 44, 21, 62, 35, 63, 51] for a non-exhaustive list of examples.
The level-α sequential test (ϕ(α) n ) surfaces the following interpretation of the test supermartingaleWn:
it is our evidence against the nullP. For this reason, it is of interest to obtain test supermartingales that
diverge to infinity as quickly as possible under the alternative. Test supermartingales with large growth
rates are, therefore, considered powerful—a designation that can be traced back to the works of Kelly[27],
Breiman [8], and Long Jr[32]. A more recent literature has made connections between large growth rates
and hypothesis testing [18, 62, 29, 63, 35, 61], and most recently Waudby-Smith et al.[63] introduce the
following definition ofalmost-sure (growth-rate) log-optimalityof test supermartingales.
21

Definition C.2(Almost sure log-optimality [63]).Fix a null P and an alternative Q. ForQ ∈ Q, a
P-test supermartingale W≡ (Wn)n∈N is said to beQ-log-optimal in a class of test supermartingalesW if
for anyW ′ ∈ W′,
lim inf
n→∞
 1
n log (Wn)− 1 n log (W′ n)  ≥0Q-almost surely.
We say thatWisQ-log-optimal if the same process isQ-log-optimal for everyQ∈ Q.
Instantiating the class of test supermartingalesWreferenced in Definition C.2 as
W ′ :={W:Wis a testP-supermartingale of the form given in (16)},
Waudby-Smith et al.[63] showed2 that a sufficient condition to achieve log-optimality with respect toW
is to select theportfolios(λ n)n∈N using algorithms that enjoy sub-linear portfolio regret.
Definition C.3(Portfolio regret).Let( en)n∈N be a deterministic sequence lying in[0,∞ ). We define the
portfolio regretof the real sequence(Wn)n∈N as
Rn ≡ Rn(Wn) := max λ∈[0,1]
nX
i=1
log ((1−λ) +λe i)−log (W n).
Importantly, the Universal Portfolio algorithm from Cover[11] achieves sub-linear portfolio regret [12],
meaning thatR n =o(n), and it computes the portfolios as
UP(W (λ) n−1) :=
R
λ∈[0,1] λW (λ) n−1dF(λ) R
λ∈[0,1] W (λ) n−1dF(λ) ,(17)
where F (·)is set to be the Beta(1/2, 1/2)distribution, and W (λ) n−1 := Qn−1 i=1 [(1−λ) +λE i]. Hence, to
achieve the notion of optimality defined in Definition C.2 it is sufficient to select the portfolios(λn)n∈N
using Cover’s Universal Portfolio algorithm from (17).
C.1 Numeraire Portfolios
In this section we briefly review numeraire portfolios [32, 26, 29], objects that are fundamental to many of
our proofs. To ease the notation in the discussion and proofs to follow, we employ the following shorthand
throughout the appendix:
λi,t := (1−λ i,t λi,t)⊤ andE i,t(a) :=  1g t( bψi,t(a))/gt(δ) ⊤ ,
for all treatment armsa∈ A, with analogous notation for the setting in which units can be repeatedly
observed in the experiment (see Section B). The above notation allows us to write the process from(2) in
the following compact form
WNa(t) =
Y
s∈Tt(a)
Y
i∈Is

λ⊤ i,sEi,s(a) ξi,s(a) .
Numeraire portfolios are those portfolios which maximize the expected logarithmic increment under
the distribution generating the data—which can also be thought of as those portfolios which maximize
the growth-rate of the test supermartingale. In our Always-On setting it is the case that the random
variables we work with are generated by different distributions, as the distributions over the active set of
treatments differ across sub-experiments. For this reason, every sub-experiments∈ [t]has its own set of
2Waudby-Smith et al.[63] provide their results for a more general class of test supermartingales than that in(16), but we
focus our discussion on test supermartingales of the form (16) to avoid introducing any extra notation.
22

numeraire portfolios corresponding to each of the active armsa∈ As. Hence, the numeraire portfolios for
the setting considered in Section 4 are defined as
λ(Q) s (a) := arg max
λ∈△1
EQRCT
h
log

λ⊤E1,s(a) 

 Fs−1, ξ1,s(a) = 1 i ,(18)
for each s∈ [t]and a∈ As. The numeriare portfolios for the setting considered in Section B are defined in
a similar way, but under that setting we endow each arma∈ As and historyh ∈ Hs−1 in sub-experiment
s∈ [t]their own numeraire portfolio. That is, in sub-experiments∈ [t], we define the numeraire portfolio
under treatmenta∈ As for those unitsi∈ Is with historyh∈ Hs−1 as,
λ(Q) s (a,h) := arg max
λ∈△1
EQRCT
h
log

λ⊤Ei,s(a,h) 

 Fs−1, ξi,s(a,h) = 1 i .(19)
An important property of numeraire portfolios is that for any otherλ∈ △d, the expected sub-optimality
ratio is upper bounded by one.
Lemma C.4.Fix a sub-experiment s∈ [t]and treatment a∈ As. Suppose that Assumptions 1 to 3 hold.
Then, for any uniti∈ Is andλ∈ △1 we have that
EQRCT
"
λ⊤Ei,s(a)
λ(Q) s (a)⊤Ei,s(a)

 Fi−1,s, ξi,s(a) = 1 # ≤1.
Furthermore, suppose that Assumption 6 also holds. We then have that for any historyh∈ Hs−1 the
following inequality holds for anyλ∈ △1 and those unitsi∈ Is with historyh,
EQRCT
"
λ⊤Ei,s(a,h)
λ(Q) s (a,h) ⊤Ei,s(a,h)

 Fi−1,s, ξi,s(a,h) = 1 # ≤1.
Proof. The proofs of both statements follow from the definitions of their numeraire portfolios—given in
(18) and (19)—and from [13, Theorem 15.2.2].■
In addition to “inducinge-values” under the alternative distribution, numeraire portfolios help charac-
terize certain optimality quantities of test supermartingales, but we defer a detailed treatment of this fact
to the work of Waudby-Smith et al. [63].
D Proofs of the Main Results
In this section we present the proofs of our main results. Some of the proofs to follow make use of processes
that have oracle access to either the numeraire portfolios or the best in hindsight portfolios. We define
these processes below. The proofs of the results from Section 4 make use of the process that has access to
the numeraire portfolios in each sub-experiment
W (Q) Na(t) := Y
s∈Tt(a)
Y
i∈Is

λ(Q) s (a)⊤Ei,s(a) ξi,s(a) ,
where λ(Q) s (a)is defined as in Equation (18) for eachs∈ [t]and a∈ As. The second process is one that
uses the best in hindsight portfolio for each of the active treatment arms in every sub-experiment:
W ⋆ Na(t) := Y
s∈Tt(a)
Y
i∈Is

λ⋆ s(a)⊤Ei,s(a) ξi,s(a) whereλ ⋆ s(a) := arg max
λ∈△1
X
i∈Is
ξi,s(a) log

λ⊤Ei,s(a)  .
We slightly abuse the notation and define the two analogous oracle processes used in the proofs of the
results from Section B as follows—where the processes that has oracle access to the numeraire portfolios
in each sub-experiment and for each strata in that sub-experiment is given by
W (Q) Na(t) := Y
s∈Tt(a)
Y
i∈Is
Y
h∈Hs−1

λ(Q) s (a,h) ⊤Ei,s(a,h) ξi,s(a,h) ,(20)
23

where λ(Q) s (a, h)is defined as in Equation (19) for eachs∈ [t], a∈ As, andh ∈ Hs−1. While the second
process is the one that has oracle access to the best in hindsight portfolio for each of the active treatment
arms in every sub-experiment and for each stratumh∈ Hs−1 takes the form
W ⋆ Na(t) := Y
s∈Tt(a)
Y
i∈Is
Y
h∈Hs−1

λ⋆ s(a,h) ⊤Ei,s(a,h) ξi,s(a,h)
where for eachs∈[t]andh∈ H s−1 ,λ ⋆ s(a,h) := arg max
λ∈△1
X
i∈Is
ξi,s(a,h) log

λ⊤Ei,s(a,h)  .
It will be clear from context which of these processes we are invoking in each of the proofs.
D.1 Proof of Lemma 3.1
Proof of Lemma 3.1.To show thatWNa(t) (given in(2)) forms a test supermartingale we must argue
that WNa(t) is nonnegative almost surely, that it forms a supermartingale, and that its mean is upper
bounded by one. Indeed, nonnegativity follows by construction so all it remains to show is thatWNa(t) is
aP-supermartingale and that its mean is upper bounded by one.
We start by showing thatWNa(t) is aP-supermartingale. To do so, we first notice howWNa(t) can be
equivalently characterized as
WNa(t) =
tY
s=1

W ˇNa(s)
1{a∈As}
.
Let n⋆ be the, fixed and arbitrary, index of the last unit to enter the experiment—which corresponds to
the index of the last unit to enter sub-experimentt—and n⋆ − 1correspond to the index of the second to
last unit to enter the experiment. The conditional expectation ofWNa(t) simplifies to
EPRCT

WNa(t)

 Fn⋆−1,t  =E PRCT h W ˇNa(t) 

 Fn⋆−1,t i t−1Y
s=1

W ˇNa(s)
1{a∈As}
.
From Assumption 3 we have that the decision to keep treatmenta in sub-experiment t is Ft−1-measurable,
which means that ifa /∈ At then EPRCT

WNa(t)

 Fn⋆−1,t  = WNa(t−1) PRCT-almost surely. On the other
hand, ifa∈ At we have that the conditional expectation term is equal to
EPRCT
" Y
i∈It

λ⊤ i,tEi,t(a) ξi,t(a)

 Fn⋆−1,t #
=E PRCT

λ⊤ n⋆,tEn⋆,t(a) ξn⋆ ,t

 Fn⋆−1,t 
| {z }
(21).(1)
Y
i∈It(n⋆−1)

λ⊤ i,tEi,t(a) ξi,t(a) .(21)
We now focus on (21).(1)and apply to law of total expectation to see how it can be upper bounded as
(21).(1) =P PRCT (ξn⋆,t = 1| Fn⋆−1,t)E PRCT
h
λ⊤ n⋆,tEn⋆,t(a)

 Fn⋆−1,t, ξn⋆,t(a) = 1 i
+P PRCT (ξn⋆,t = 0| Fn⋆−1,t)E PRCT [1| Fn⋆−1,t, ξn⋆,t = 0]
=P PRCT (ξn⋆,t = 1| Fn⋆−1,t) ((1−λ n⋆,t)
+λn⋆,tEPRCT
h
gt( bψn⋆,t(a))

 Fn⋆−1,t, ξn⋆,t(a) = 1 i /gt(δ)  (22)
+ (1−P PRCT (ξn⋆,t = 1| Fn⋆−1,t))
=P PRCT (ξn⋆,t = 1| Fn⋆−1,t) ((1−λ n⋆,t) +λ n⋆,tgt(ψP(a))/gt(δ))(23)
+ (1−P PRCT (ξn⋆,t = 1| Fn⋆−1,t))
≤P PRCT (ξn⋆,t = 1| Fn⋆−1,t) ((1−λ n⋆,t) +λ n⋆,t) + (1−P PRCT (ξn⋆,t = 1| Fn⋆−1,t))(24)
= 1,
24

where (22) follows from the predictability of the portfolios and the transformationgt(·)on the threshold δ;
(23) follows from the assumption thatEPRCT
h
gt( bψn⋆,t(a))

 Fn⋆−1,t, ξn⋆,t(a) = 1 i = gt(ψP(a)); and(24)
follows because under the null,P(a),ψ P(a)≤δ.
Putting the previous steps together we can conclude that
EPRCT

WNa(t)

 Fn⋆−1, t  ≤W Na(t−1)

 Y
i∈It(n⋆−1)

λ⊤ i,tEi,t(a) ξi,t(a)


a∈At
,
which shows thatWNa(t) is a supermartingale. Instantiating the above for the first sub-experiment with
only one unit, and through similar arguments we can conclude thatEPRCT

λ⊤ 1,1E1,1(a) ξ1,1(a) ≤ 1,
which completes the proof. ■
D.2 Proof of Proposition 3.2
We handle the proofs of the online false discovery rate control for Sections B and 4 simultaneously. To
do so, we introduce the variableJs(a)for sub-experiments∈[t]. Under the setting of Section 4 it takes
the form Js(a) := 1{a∈ H0}, which indicates that the treatmenta is null. For the setting considered in
Section B, the variable takes the formJs(a) := 1
n
ψP(a,h)≤δ,∀h∈ S r∈Ts(a) Hr−1 o which states that
the effect of treatmenta under all of the histories observed up until sub-experiments is less than the
threshold δ. We note howJs(a)under both settings is Fs−1-measurable. With this notation at hand, we
proceed to prove Proposition 3.2
Proof of Proposition 3.2.Fix a distributionP∈ P ∪Q, a sub-experiments∈ [t], and defineAs := Ss r=1 Ar.
We start by noting how the number of false discoveries can be written as
|Ds ∩ H0|=
X
a∈As
Js(a)1

WNa(s) ≥1/α a

,
where we recall that for any treatmenta∈ As, the treatment is removed from the experiment as soon as
its test supermartingale surpasses the threshold. This is equivalent to “freezing” the test supermartingale
for treatment a; that is, for all subsequent sub-experiments the value of the test supermartingale is not
updated.
By the definition of sub-experiments, we know thatDs ⊇ Ds−1 for alls∈ [t]where D0 = ∅. This implies
that |Ds| ≥ |Ds−1| for alls∈ [t], where|∅| = 0. Let s0(a) := min{r∈[s]|a∈ A r} be the sub-experiment
in which treatmenta was introduced. We therefore have the inequalities|Ds| ≥

Ds0(a)

 ≥

Ds0(a)−1

, and
use these inequalities to upper bound the proportion of false discoveries as
|Ds ∩ H0|
|Ds| ∨1 =
X
a∈As
Js(a)1

WNa(s) ≥1/α a

|Ds| ∨1
≤
X
a∈As
Js(a)1

WNa(s) ≥1/α a

Ds0(a)−1

 + 1
≤
X
a∈As
Js(a)αaWNa(s)

Ds0(a)−1

 + 1 .(25)
Recall the definition ofαa :=αγ a

Ds0(a)−1

 + 1  . Substituting the definition ofαa into (25) gives us
(25)=
X
a∈As
Js(a)αγa

Ds0(a)−1

 + 1  WNa(s)

Ds0(a)−1

 + 1
=
X
a∈As
αJs(a)γaWNa(s) .
25

The above upper bounds are deterministic, which allow us to upper bound the false discover rate as
FDR(Ds)≤E PRCT

 X
a∈As
αJs(a)γaWNa(s)

 .
We now focus on the upper bound on the false discovery rate and note how due to the law of total
expectation it can be equivalently written as
EPRCT

 X
a∈As
αJs(a)γaWNa(s)


=E PRCT

EPRCT

 X
a∈A′s
αJs(a)γaWNa(s) +
X
a∈As−1
αJs(a)γaWNa(s)

 Fs−1    
=E PRCT

 X
a∈A′s
EPRCT

αJs(a)γaWNa(s)

 Fs−1 

 +E PRCT

 X
a∈As−1
EPRCT

αJs(a)γaWNa(s)

 Fs−1 

 ,
(26)
where the last equality follows from theFs−1-measurability of the treatments inAs and the linearity of
expectations.
We now notice two facts. First, from the definitions ofJs(a)we have that it isFs−1-measurable and
that it satisfiesJs(a) ≤J s−1(a). Second, for thosea∈ As for which {Js(a) = 1} (i.e., a is considered to
be under the null in sub-experiments) the following inequality holds
EPRCT

Js(a)WNa(s)

 Fs−1  ≤J s(a)WNa(s−1) ≤J s−1(a)WNa(s−1) ,(27)
where the first inequality follows fromWNa(s) being a test supermartingale for thosea∈ As for which
{Js(a) = 1}. By the law of iterated expectation and the inequality from(27), we can conclude that for
those a∈ As for which {Js(a) = 1}, EPRCT

Js(a)WNa(s)

≤ 1. On the other hand, for thosea∈ As for
which{J s(a) = 0}we have thatE PRCT

Js(a)WNa(s)

 Fs−1  = 0.
The previous arguments allow us to conclude that
(26)≤αE PRCT

 X
a∈A′s
γa

 +E PRCT

 X
a∈As−1
αJs−1(a)γaWNa(s−1)

 .
By continuously applying the above arguments to the resulting upper bounds, we end up with the following
inequality
EPRCT

 X
a∈As
αJs(a)γaWNa(s)

 ≤αE PRCT


sX
r=1
X
a∈A′r
γa

 .(28)
Since the sequence(γr)∞ r=1 is chosen to satisfy the inequalityP∞ r=1 γr ≤ 1, we have that the upper bound
in (28) can be further upper bounded as
αEPRCT


sX
r=1
X
a∈A′r
γa

 ≤αE PRCT
" ∞X
r=1
γr
#
≤α .
Hence, we can conclude that
FDR(Ds)≤α .
Since the choice ofs∈[t]was arbitrary, we have that
FDR(Ds)≤αfor alls∈[t],
completing the proof. ■
26

D.3 Proof of Lemma 4.1
Proof of Lemma 4.1.Fix aP ∈ P ∪ Q, a sub-experiments∈ [t], and any treatmenta∈ As. Our goal is to
show that the Horivtz-Thompson estimator from(5) is conditionally unbiased when we condition on the
filtration and the event that the inclusion indicator is equal to one. Hence, we can write the conditional
expectation as
EPRCT
h
bψi,s(a)

 Fi−1,s, ξi,s(a) = 1 i =E PRCT  Yi(a) 1{A i,s =a} bπs(a)

 Fi−1,s, ξi,s(a) = 1 
−E PRCT

Yi(0) 1{A i,s =0} bπs(0)

 Fi−1,s, ξi,s(a) = 1  .
We now focus on the conditional expectation under treatmenta. Due to the Fs−1-measurability of
πs(a)and πs(0)—and hence of bπs(a)—alongside the conditional conditional ignorability assumption
(Assumption 2.(i)) we can further rewrite the conditional expectation as
EPRCT

Yi(a) 1{A i,s =a} bπs(a)

 Fi−1,s, ξi,s(a) = 1 
= 1 bπs(a) EPRCT [Yi(a)| Fi−1,s, ξi,s(a) = 1]E PRCT [1{A i,s =a} | Fi−1,s, ξi,s(a) = 1].(29)
Since units are independent and identically distributed together with the conditional ignorability assump-
tion (Assumption 2.(i)) we have the identityEPRCT [Yi(a)| Fi−1,s, ξi,s(a) = 1] =E P [Y1(a)].
We now turn our attention to the conditional expectation of the indicator. The conditional expectation
oftheindicatorfollowstheidentity EPRCT [1{A i,s =a} | Fi−1,s, ξi,s(a) = 1] = PPRCT (Ai,s =a| Fi−1,s, ξi,s(a) = 1).
Since we are conditioning on the event{ξi,s(a) = 1} we know thatAi,s = a or Ai,s = 0. This, in turn,
implies that
PPRCT (Ai,s =a| Fi−1,s, ξi,s(a) = 1) = πs(a) πs(a) +π s(0) ≡bπs(a).
The above arguments imply that (29) is equal to
1
bπs(a) EPRCT [Yi(a)| Fi−1,s, ξi,s(a) = 1]E PRCT [1{A i,s =a} | Fi−1,s, ξi,s(a) = 1] =E P [Y1(a)].
Through the same set of steps we can conclude that
EPRCT

Yi,s(0) 1{A i,s =0} bπs(0)

 Fi−1,s, ξi,s(a) = 1  =E P [Y1(0)].
Hence, all of the above steps imply that
EPRCT
h
bψi,s(a)

 Fi−1,s, ξi,s(a) = 1 i =ψ P(a),
completing the proof of Lemma 4.1.■
D.4 Proof of Proposition 4.2
Proof of Proposition 4.2.Proposition 4.2 is an immediate consequence of Lemmas 3.1 and 4.1, and the
fact thatg s(·)is a non-decreasing linear map for eachs∈[t].■
D.5 Proof of Theorem 4.4
In this subsection we present the proof of Theorem 4.4. Nonetheless, before providing the proof we present
the following lemma (whose proof is given in Section E.1) that is central to the proof of Theorem 4.4.
27

Lemma D.1.Fix an arm a∈ Aand a probabilityQ ∈ Q(a). Let t∈N denote the number of sub-
experiments that have transpired in the experiment, and letR ˇNa(s) := log  ˇNa(s) + 1  /2 + log (2) be the
upper bound on the portfolio regret of the Universal Portfolio algorithm [12] used to select the portfolios
under treatment a in each sub-experiment s∈ Tt(a). Then, under Assumptions 1 to 4 the following
inequality holds for anyε >0,
PQRCT

sup
nt≥m
1
Na(t)

log  WNa(t)  −log  W (Q) Na(t) 

 ≥ε !
≤
∞X
nt=m
exp


−2(1−exp{−ε})
X
s∈Tt(a)
nsps


 +P QRCT

 sup
nt≥m
1
Na(t)
X
s∈Tt(a)
R ˇNa(s) ≥ε

 .
With Lemma D.1 in hand, we now proceed to prove Theorem 4.4. The proof follows two steps. In
the first step, we show that the normalizedlog

WNa(t)

and log

W (Q) Na(t)

are almost surely equivalent
as the total number of units who enter the experiment goes to infinity. In the second step, we use the
aforementioned result to show that in the limit no other processfWNa(t) can exhibit a larger growth rate
thanW Na(t).
Proof of the almost sure equivalence with the oracle process.We begin by upper bounding the following
probability for anyε >0,
PQRCT

sup
nt≥m
1
Na(t)

log  WNa(t)  −log  W (Q) Na(t) 

 ≥ε ! .(30)
From Lemma D.1 we have that
(30)≤
X
nt=m
exp


−2(1−exp{−ε})
X
s∈Tt(a)
nsps



| {z }
(31).(1)
+P QRCT

 sup
nt≥m
1
Na(t)
X
s∈Tt(a)
R ˇNa(s) ≥ε


| {z }
(31).(2)
.(31)
We now recall the fact that for any random variables(Xn)n∈N drawn from a distributionP,
PP

lim
n→∞
|Xn|= 0

= 1if and only if∀ε >0,lim
m→∞
PP

sup
n≥m
|Xn|> ε

= 0.
Hence, as we takem→ ∞we can see that(31).(1) → 0almost surely. Similarly, we have that(31).(2) → 0
asm→ ∞, which follows from Lemma E.1. Thus, we can conclude that
lim
nt→∞
1
Na(t)

log

WNa(t)

−log

W (Q) Na(t)

= 0Q RCT-almost surely.(32)
■
Proof of the log-optimality ofWNa(t).We begin by lower bounding the difference as
lim inf
nt→∞
1
Na(t)

log

WNa(t)

−log

fWNa(t)

= lim inf
nt→∞
1
Na(t)

log

WNa(t)/W (Q) Na(t)

+ log

W (Q) Na(t)/fWNa(t)

≥lim inf
nt→∞
1
Na(t) log

WNa(t)/W (Q) Na(t)

| {z }
(33).(1)
+ lim inf
nt→∞
1
Na(t) log

W (Q) Na(t)/fWNa(t)

| {z }
(33).(2)
(33)
28

Notice how(33).(1) = 0which follows from the proof of the almost sure equivalence betweenWNa(t) and
the oracle process—the result which is given in (32). Hence, all it remains to show is that (33).(2)≥0.
From the arm-wise numeraire property [51, Lemma B.1] we have that for anyεnt >0,
PQRCT

fWNa(t)/W (Q) Na(t) ≥ε nt

≤ 1 εnt ,
from which we can also conclude that
PQRCT
 1
Na(t) log

fWNa(t)/W (Q) Na(t)

≥ 1 Na(t) log  εnt  ≤ 1 εnt .
Lettingε nt =n 2 t and summing overnt we can see how
∞X
nt=1
PQRCT

1
Na(t) log

fWNa(t)/W (Q) Na(t)

≥ 2 log

nt

Na(t)
!
≤
∞X
nt=1
1
n2 t = π2 6 .
Hence, by the Borel-Cantelli lemma we have that
PQRCT

lim sup
nt→∞

1
Na(t) log

fWNa(t)/W (Q) Na(t)

− 2 log

nt

Na(t)
!
>0
!
= 0.
By Lemma E.5 and the definition ofnt it is the case that2log

nt

/Na(t) → 0Q RCT-almost surely, which
together with the above arguments we can conclude that
lim inf
nt→∞
1
Na(t) log

W (Q) Na(t)/fWNa(t)

≥0Q RCT-almost surely.
Putting all of the previous steps together we can conclude that
lim inf
nt→∞
1
Na(t)

log

WNa(t)

−log

fWNa(t)

≥0Q RCT-almost surely,
completing the proof of the log-optimality ofWNa(t).■
D.6 Proof of Lemma B.1
Proof of Lemma B.1.Fix a distributionP ∈ P ∪ Q, a sub-experiments∈ [t], a treatment arma∈ As,
and a historyh ∈ Hs−1. Taking the conditional expectation of the Horvitz-Thompson estimator for
treatmentafor units whose history is equal tohin sub-experiments, we have that:
EPRCT
h
bψi,s(a,h)

 Fi−1,s, ξi,s(a,h) = 1 i
=E PRCT

Yi,s
 1{A i,s =a}
bπs(a) − 1{A i,s =0} bπs(0) 

 Fi−1,s, ξi,s(a,h) = 1 
=E PRCT

Yi(Zi,s−ℓ:s−1, Ai,s)
 1{A i,s =a}
bπs(a) − 1{A i,s =0} bπs(0) 

 Fi−1,s, ξi,s(a,h) = 1  ,(34)
where the second equality follows from the definition of the observed outcome in sub-experiments. Due
to the linearity of expectation we can see how (34) can be rewritten as:
(34)=E PRCT
 Yi(Zi,s−ℓ:s−1, a)1{Ai,s =a}
bπs(a)

 Fi−1,s, ξi,s(a,h) = 1 
−E PRCT
 Yi(Zi,s−ℓ:s−1,0)1{A i,s =0}
bπs(0)

 Fi−1,s, ξi,s(a,h) = 1  .
29

Focusing on the first summand we can see how it can be further simplified to:
EPRCT
 Yi(Zi,s−ℓ:s−1, a)1{Ai,s =a}
bπs(a)

 Fi−1,s, ξi,s(a,h) = 1 
= EPRCT [Yi(Zi,s−ℓ:s−1, a)| Fi−1,s, ξi,s(a,h) = 1]E PRCT [1{A i,s =a} | Fi−1,s, ξi,s(a,h) = 1] bπs(a)
= EPRCT [Yi(Zi,s−ℓ:s−1, a)| Fi−1,s, ξi,s(a,h) = 1]bπs(a) bπs(a)
=E P [Yi(Zi,s−ℓ:s−1, a)| Fi−1,s, ξi,s(a,h) = 1],
where the first equality follows from the independence of the treatment assignment (Assumption 2)
and the Fs−1-measurability of the propensity score. The second equality follows because the treatment
assignments in each sub-experiment are drawn from the same distribution no matter which historyhthe
unit experiences, and since conditioning on the event{ξi,s(a,h) = 1} implies that Ai,s = a or Ai,s = 0.
Hence, we have that
EPRCT [1{A i,s =a} | Fs−1, ξi,s(a) = 1] =P PRCT (Ai,s =a| Fs−1, ξi,s(a) = 1) = πs(a) πs(a) +π s(0) ≡bπs(a).
Through the same set of steps one can show that
EP
 Yi(Zi,s−ℓ:s−1,0)1{A i,s =0}
bπs(0)

 Fi−1,s, ξi,s(a,h) = 1  =E P [Yi(Zi,s−ℓ:s−1,0)| Fi−1,s, ξi,s(a,h) = 1].
Hence, putting the previous steps together we have that
EP
h
bψi,s(a,h)

 Fi−1,s, ξi,s(a,h) = 1 i =E P [Yi(Zi,s−ℓ:s−1, a)−Yi(Zi,s−ℓ:s−1,0)| Fi−1,s, ξi,s(a,h) = 1].
The result follows by noting how the potential outcomes for uniti are independent from those of
all other units j∈ I (such that j̸ = i) as well as their treatment assignments. Furthermore, from
Assumption 2.(i)and Assumption 6 we have that the expected outcomes in the current sub-experiments
only depend on the observed outcomes and treatment assignments from the previousℓ sub-experiments.
We therefore have that
EP [Yi(Zi,s−ℓ:s−1, a)−Yi(Zi,s−ℓ:s−1,0)| Fi−1,s, ξi,s(a,h)]
=E P [Yi(Zi,s−ℓ:s−1, a)−Yi(Zi,s−ℓ:s−1,0)|H i,s−1 =h]≡ψ P(a,h),
completing the proof. ■
D.7 Proof of Theorem B.4
In this subsection we present the proof of Theorem B.4. It follows the same steps as the proof of
Theorem 4.4, but we provide them here for the sake of completeness. Nonetheless, before providing the
proof we state the following lemma (whose proof is given in Section E.2) that plays a central role in the
proof of Theorem B.4.
Lemma D.2.Fix an arm a∈ Aand a probabilityQ ∈ Q(a). Let t∈N denote the number of sub-
experiments that were run, and letR ˇNa,h(s) := log  ˇNa,h(s) + 1  /2 + log (2) be the upper bound on the
portfolio regret of the Universal Portfolio algorithm used to select the portfolios under treatmenta, for
historyh, in each sub-experiment s∈ Tt(a). Then, under Assumptions 1 to 3, 5 and 6 the following
inequality holds for anyε >0,
PQRCT

sup
nt≥m
1
Na(t)

log  WNa(t)  −log  WNa(t) (Q)

 ≥ε !
≤
∞X
nt=m
exp


−2(1−exp{−ε})
X
s∈Tt(a)
nsps


 +P QRCT

 sup
nt≥m
1
Na(t)
X
s∈Tt(a)
X
h∈Hs−1
R ˇNa,h(s) ≥ε

 .
30

Having stated Lemma D.2, we now prove Theorem B.4. The proof proceeds in two steps. In the
first step, we show thatWNa(t) is almost surely equivalent to a process that has oracle access to all the
numeraire portfolios, W (Q) Na(t). We then use this result in the second step to argue about the log-optimality
of our process.
Proof of the almost sure equivalence with the oracle process.We begin by upper bounding the following
probability for anyε >0,
PQRCT

sup
nt≥m
1
Na(t)

log  WNa(t)  −log  W (Q) Na(t) 

 ≥ε ! .(35)
From Lemma D.2 we have that
(35)≤
X
nt=m
exp


−2(1−exp{−ε})
X
s∈Tt(a)
nsps



| {z }
(36).(1)
+P QRCT

 sup
nt≥m
1
Na(t)
X
s∈Tt(a)
X
h∈Hs−1
R ˇNa,h(s) ≥ε


| {z }
(36).(2)
.
(36)
We now recall the fact that for any random variables(Xn)n∈N drawn from a distributionP,
PP

lim
n→∞
|Xn|= 0

= 1if and only if∀ε >0,lim
m→∞
PP

sup
n≥m
|Xn|> ε

= 0.
Hence, as we takem→ ∞we can see that(36).(1) → 0almost surely. Similarly, we have that(36).(2) → 0
asm→ ∞, which follows from Lemma E.2. Thus, we can conclude that
lim
nt→∞
1
Na(t)

log

WNa(t)

−log

W (Q) Na(t)

= 0Q RCT-almost surely,(37)
completing the proof of the almost sure equivalence between our process and the oracle process.■
Proof of the log-optimality ofWNa(t).We begin by lower bounding the difference as
lim inf
nt→∞
1
Na(t)

log

WNa(t)

−log

fWNa(t)

= lim inf
nt→∞
1
Na(t)

log

WNa(t)/W (Q) Na(t)

+ log

W (Q) Na(t)/fWNa(t)

≥lim inf
nt→∞
1
Na(t) log

WNa(t)/W (Q) Na(t)

| {z }
(38).(1)
+ lim inf
nt→∞
1
Na(t) log

W (Q) Na(t)/fWNa(t)

| {z }
(38).(2)
(38)
Notice how(38).(1) = 0which follows from the proof of the almost sure equivalence betweenWNa(t) and
the oracle process (37). Hence, all it remains to show is that (38).(2)≥0.
From the arm-wise numeraire property [51, Lemma B.1] we have that for anyεnt >0,
PQRCT

fWNa(t)/W (Q) Na(t) ≥ε nt

≤ 1 εnt ,
from which we can also conclude that
PQRCT
 1
Na(t) log

fWNa(t)/W (Q) Na(t)

≥ 1 Na(t) log  εnt  ≤ 1 εnt .
31

Lettingε nt =n 2 t and summing overnt we can see how
∞X
nt=1
PQRCT

1
Na(t) log

fWNa(t)/W (Q) Na(t)

≥ 2 log

nt

Na(t)
!
≤
∞X
nt=1
1
n2 t = π2 6 .
Hence, by the Borel-Cantelli lemma we have that
PQRCT

lim sup
nt→∞

1
Na(t) log

fWNa(t)/W (Q) Na(t)

− 2 log

nt

Na(t)
!
>0
!
= 0.
By Lemma E.5 and the definition ofnt it is the case that2log

nt

/Na(t) → 0 RCT-almost surely, which
together with the above arguments we can conclude that
lim inf
n→∞
1
Na(t) log

W (Q) Na(t)/fWNa(t)

≥0Q RCT-almost surely.
Putting the steps together we can conclude that
lim inf
nt→∞
1
Na(t)

log

WNa(t)

−log

fWNa(t)

≥0Q RCT-almost surely,
completing the proof of the log-optimality ofWNa(t).■
E Auxiliary Results
E.1 Proof of Lemma D.1
Proof of Lemma D.1.Our aim is to control the following probability for anyε >0,
PQRCT

sup
nt≥m
1
Na(t)

log  WNa(t)  −log  W (Q) Na(t) 

 ≥ε ! .(39)
We start by upper bounding it by the probability of the upper and lower deviations
(39)≤P QRCT

sup
nt≥m
1
Na(t) log

WNa(t)/W (Q) Na(t)

≥ε
!
| {z }
(40).(1)
+P QRCT

sup
nt≥m
1
Na(t) log

W (Q) Na(t)/WNa(t)

≥ε
!
| {z }
(40).(2)
,
(40)
and we proceed by analyzing the terms in the upper bound independently.
We first analyze (40).(1), and proceed as follows:
(40).(1)≤
∞X
nt=m
PQRCT
 1
Na(t) log

WNa(t)/W (Q) Na(t)

≥ε

=
∞X
nt=m
PQRCT

WNa(t)/W (Q) Na(t) ≥exp{N a(t)ε} 
=
∞X
nt=m
PQRCT

exp{−N a(t)ε}

WNa(t)/W (Q) Na(t)

≥1

≤
∞X
nt=m
EQRCT
h
exp{−N a(t)ε}

WNa(t)/W (Q) Na(t)
i
≤
∞X
nt=m
exp


−2(1−exp{−ε})
X
s∈Tt(a)
nsps



32

where the first inequality follows from a union bound, the second inequality is due to Markov’s inequality,
and the third inequality is due to Lemma E.3.
We now turn our attention to(40).(2), and recall that by definitionlog

W ⋆ Na(t)

≥log

W (Q) Na(t)

.
Hence, we have the following series of upper bounds
(40).(2)≤P QRCT

sup
nt≥m
1
Na(t)

log

W ⋆ Na(t)

−log

WNa(t)

≥ε
!
=P QRCT

 sup
nt≥m
1
Na(t)

 X
s∈Tt(a)
" X
i∈Is
ξi,s(a) log

λ⋆ s(a)⊤Ei,s(a)  − X
i∈Is
ξi,s(a) log

λi,s(a)⊤Ei,s(a) 
#
 ≥ε


≤P QRCT

 sup
nt≥m
1
Na(t)
X
s∈Tt(a)
R ˇNa(s) ≥ε

 ,
where the second inequality follows because for each arm and in each sub-experiment we run a new
instance of the Universal Portfolio algorithm [11] whose upper bound on the portfolio regret is denoted by
R ˇNa(s) for each sub-experiments∈ Tt(a).
Putting the above steps together we have that
PQRCT

sup
nt≥m
1
Na(t)

log  WNa(t)  −log  W (Q) Na(t) 

 ≥ε !
≤
∞X
nt=m
exp


−2(1−exp{−ε})
X
s∈Tt(a)
nsps


 +P QRCT

 sup
nt≥m
1
Na(t)
X
s∈Tt(a)
R ˇNa(s) ≥ε

 ,
completing the proof. ■
E.2 Proof of Lemma D.2
Proof of Lemma D.2.Our aim is to control the following probability for anyε >0,
PQRCT

sup
nt≥m
1
Na(t)

log  WNa(t)  −log  W (Q) Na(t) 

 ≥ε ! .(41)
We start by upper bounding it by the probability of the upper and lower deviations
(41)≤P QRCT

sup
nt≥m
1
Na(t) log

WNa(t)/W (Q) Na(t)

≥ε
!
| {z }
(42).(1)
+P QRCT

sup
nt≥m
1
Na(t) log

W (Q) Na(t)/WNa(t)

≥ε
!
| {z }
(42).(2)
,
(42)
and we proceed by analyzing the terms in the upper bound independently.
33

We first analyze (42).(1), and proceed as follows:
(42).(1)≤
∞X
nt=m
PQRCT
 1
Na(t) log

WNa(t)/W (Q) Na(t)

≥ε

=
∞X
nt=m
PQRCT

WNa(t)/W (Q) Na(t) ≥exp{N a(t)ε} 
=
∞X
nt=m
PQRCT

exp{−N a(t)ε}

WNa(t)/W (Q) Na(t)

≥1

≤
∞X
nt=m
EQRCT
h
exp{−N a(t)ε}

WNa(t)/W (Q) Na(t)
i
≤
∞X
nt=m
exp


−2(1−exp{−ε})
X
s∈Tt(a)
nsps



where the first inequality is due to a union bound, the second inequality is due to Markov’s inequality,
and the third inequality is due to Lemma E.3.
We now turn our attention to(42).(2). Notice how by definition ofλ⋆ s(a, h)and λ(Q) s (a, h)we have
the following upper bound for eachs∈ Tt(a),
X
h∈Hs−1
X
i∈Is
ξi,s(a,h) log

λ⋆ s(a,h) ⊤Ei,s  ≥ X
h∈Hs−1
X
i∈Is
ξi,s(a,h) log

λ(Q) s (a,h) ⊤Ei,s

.
From the portfolio regret of the Universal Portfolio algorithm [12] we have that for eachs∈ Tt(a),
X
h∈Hs−1
X
i∈Is
ξi,s(a,h) log

λ⋆ s(a,h) ⊤Ei,s  − X
h∈Hs−1
X
i∈Is
ξi,s(a,h) log

λi,s(a,h) ⊤Ei,s  ≤ X
h∈Hs−1
R ˇNa,h(s) .
Putting the inequalities from the above two displays together allows us to upper bound (42).(2)as
(42).(2)≤P QRCT

 sup
nt≥m
1
Na(t)
X
s∈Tt(a)
X
h∈Hs−1
R ˇNa,h(a) ≥ε

 .
Hence, all of the above steps allow us to conclude that
PQRCT

sup
nt≥m
1
Na(t)

log  WNa(t)  −log  W (Q) Na(t) 

 ≥ε !
≤
∞X
nt=m
exp


−2(1−exp{−ε})
X
s∈Tt(a)
nsps


 +P QRCT

 sup
nt≥m
1
Na(t)
X
s∈Tt(a)
X
h∈Hs−1
R ˇNa,h(s) ≥ε

 ,
completing the proof. ■
E.3 Path-wise control of portfolio regret
Lemma E.1.Fix a distributionP ∈ P ∪ Qand for anyn∈N let Rn := log (n+ 1)/ 2 + log (2) denote
the portfolio regret bound from the Universal Portfolio algorithm [12]. We then have that for anyε >0,
lim
m→∞
PPRCT

 sup
nt≥m
X
s∈Tt(a)
R ˇNa(s)
Na(t) ≥ε

 = 0.
34

Proof. Fix a distributionP ∈ P ∪ Q. We start by upper bounding the normalized experiment-wide regret
as X
s∈Tt(a)
1
Na(t) R ˇNa(s) =
X
s∈Tt(a)
ˇNa(s)
Na(t)
R ˇNa(s)
ˇNa(s) ≤
X
s∈Tt(a)
R ˇNa(s)
ˇNa(s) ,
where the inequality follows from the definition ofNa(t) = P s∈Tt(a) ˇNa(s)which implies that for any
s∈ Tt(a), ˇNa(s)/Na(t)≤1.
From assumption we have that for everys∈ [t], ns → ∞as nt → ∞. When combined with Lemma E.4,
which tells us that ˇNa(s)→ ∞PRCT-almost surely asns → ∞, we can conclude that
X
s∈Tt(a)
R ˇNa(s)
Na(t) ≤
X
s∈Tt(a)
R ˇNa(s)
ˇNa(s) →0P RCT-almost surely
because Rn = log (n+ 1)/ 2 + log (2) for every n∈N . Since the convergence holds pathwise we can
conclude that asm→ ∞,
sup
nt≥m
X
s∈Tt(a)
R ˇNa(s)
Na(t) →0P RCT-almost surely,
which in turn implies that for anyε >0asm→ ∞,
1


 sup nt≥m
X
s∈Tt(a)
R ˇNa(s)
Na(t) ≥ε


 →0P RCT-almost surely.
Putting all of the above steps together we have that asm→ ∞,
PPRCT

 sup
nt≥m
X
s∈Tt(a)
R ˇNa(s)
Na(t) ≥ε

 =E PRCT

1


 sup nt≥m
X
s∈Tt(a)
R ˇNa(s)
Na(t) ≥ε




 →0,
completing the proof. ■
Lemma E.2.Fix a distributionP ∈ P ∪ Qand for anyn∈N let Rn := log (n+ 1)/ 2 + log (2) denote
the portfolio regret bound from the Universal Portfolio algorithm [12]. We then have that for anyε >0,
lim
m→∞
PPRCT

 sup
nt≥m
X
s∈Tt(a)
X
h∈Hs−1
R ˇNa,h(s)
Na(t) ≥ε

 = 0.
Proof. Fix a distributionP ∈ P ∪ Q. We start by upper bounding the normalized experiment-wide regret
as X
s∈Tt(a)
X
h∈Hs−1
R ˇNa,h(s)
Na(t) =
X
s∈Tt(a)
X
h∈Hs−1
ˇNa(s)
Na(t)
R ˇNa,h(s)
ˇNa(s) ≤
X
s∈Tt(a)
X
h∈Hs−1
R ˇNa,h(s)
ˇNa(s) ,
where the inequality follows from the definition ofNa(t) = P s∈Tt(a) ˇNa(s)which implies that for any
s∈ Tt(a), ˇNa(s)/Na(t) ≤ 1. Recall that Rn = log (n+ 1)/ 2 + log (2) for every n∈N . Since Rn is
nondecreasing we have that for anyh∈ Hs−1,R ˇNa,h(s) ≤R ˇNa(s). This in turn implies that
X
s∈Tt(a)
X
h∈Hs−1
R ˇNa,h(s)
ˇNa(s) ≤
X
s∈Tt(a)
|Hs−1|
R ˇNa(s)
ˇNa(s) .
We note how|Hs−1|<∞ (i.e., is finite) which is a consequence of Assumption 5 and our assumption that
the carryover effects last forℓ sub-experiments. From assumption we have that for everys∈ [t], ns → ∞
35

as nt → ∞. Hence, from the finiteness of|Hs|, the sublinearity ofRn, and Lemma E.4, which tells us
that ˇNa(s)→ ∞PRCT-almost surely asns → ∞, we can conclude that asnt → ∞,
X
s∈Tt(a)
|Hs−1|
R ˇNa(s)
ˇNa(s) →0P RCT-almost surely.
Since the convergence holds pathwise we can conclude that asm→ ∞,
sup
nt≥m
X
s∈Tt(a)
X
h∈Hs−1
R ˇNa,h(s)
Na(t) →0P RCT-almost surely,
which in turn implies that for everyε >0asm→ ∞,
1


 sup nt≥m
X
s∈Tt(a)
X
h∈Hs−1
R ˇNa,h(s)
Na(t) ≥ε


 →0P RCT-almost surely.
Putting all of the above steps together we have that asm→ ∞,
PPRCT

 sup
nt≥m
X
s∈Tt(a)
X
h∈Hs−1
R ˇNa,h(s)
Na(t) ≥ε

 =E PRCT

1


 sup nt≥m
X
s∈Tt(a)
X
h∈Hs−1
R ˇNa,h(s)
Na(t) ≥ε




 →0,
completing the proof. ■
E.4 Upper bound on the expected exponential decay as a function of the
number of units in a treatment arm.
In this subsection we present an upper bound on the expected exponential decay as a function of the
number of units assigned to a treatment arm when multiplied by the sub-optimality ratio of wealth
processes. We prove the result for the setting in which units are classified into different strata in each
sub-experiment, as the same result in which units are not stratified in each sub-experiment follows as a
consequence.
Lemma E.3.Fix the total number of sub-experimentst∈N , an arma∈ Aand a distributionQ ∈ Q(a).
Let W (Q) Na(t) be the process that has oracle access to the numeraire portfolios in every sub-experiment, as
defined in(20). We then have that
EQRCT
h
exp{−N a(t)ε}

WNa(t)/W (Q) Na(t)
i
≤exp


−2 (1−exp{−ε})
X
s∈Tt(a)
nsps


 .
Proof. Fix the total number of sub-experimentst∈N , an arma∈ A, and a distributionQ ∈ Q(a). Let
n⋆ be the index of the last unit to enter the experiment andn⋆ − 1be the index of the second to last unit
to enter the experiment. The law of iterated expectation gives us the following identity on the expectation
EQRCT
h
exp{−N a(t)ε}

WNa(t)/W (Q) Na(t)
i
=E QRCT
h
EQRCT
h
exp{−N a(t)ε}

WNa(t)/W (Q) Na(t)


 Fn⋆−1,t ii .
For now, we will focus on the conditional expectation, which simplifies to
EQRCT
h
exp{−N a(t)ε}

WNa(t)/W (Q) Na(t)


 Fn⋆−1,t i
=E QRCT
h
exp

−ε ˇNa(t) 	  W ˇNa(t)/W (Q) ˇNa(t) i1{a∈At}

 Fn⋆−1,t  (43)
·

WNa(t−1)/W (Q) Na(t−1)

exp{−N a(t−1)ε}.
36

Further focusing on the conditional expectation from(43), we can see that ifa /∈ At then (43) = 1.
Otherwise, ifa∈ At, the conditional expectation from (43) decomposes into
(43)=E QRCT

 Y
h∈Ht−1
exp{−εξ n⋆,t(a,h)}

λ⊤ n⋆,tEn⋆,t(a)
λ(Q) t (a,h) ⊤En⋆,t(a)
!ξn⋆ ,t(a,h)

 Fn⋆−1,t   (44)
·
Y
i∈It(n⋆−1)
Y
h∈Ht−1

λ⊤ i,tEi,t(a)
(λ(Q) t (a,h)) ⊤Ei,t(a)
!ξi,t(a,h) Y
i∈It(n⋆−1)
Y
h∈Ht−1
exp{−εξ i,t(a,h)}.
Focusing on the conditional expectation from(44) we have that conditioning on the filtrationFn⋆−1,t
only the inclusion indicator,ξn⋆,t(a, h), corresponding toHn⋆,t−1 =hwill not be equal to zero—as the
filtration includes the history of unitn⋆, which determines the strata the unit belongs to. Nonetheless,
the event {An⋆,t =aorA n⋆,t =0} is still random as the treatment assignments are randomly assigned in
each sub-experiment. Hence, focusing on the inclusion indicator for whichHn⋆,t−1 =hand applying the
law of total expectation we have that
EQRCT

exp{−εξ n⋆,t(a,h)}

λ⊤ n⋆,tEn⋆,t(a)
λ(Q) t (a,h) ⊤En⋆,t(a)
!ξn⋆ ,t(a,h)

 Fn⋆−1,t  
=P QRCT (ξn⋆,t(a,h) = 0| Fn⋆−1,t)
+P QRCT (ξn⋆,t(a,h) = 1| Fn⋆−1,t) exp{−ε}E QRCT
"
λ⊤ n⋆,tEn⋆,t(a)
λ(Q) t (a,h) ⊤En⋆,t(a)

 Fn⋆−1,t, ξn⋆,t(a,h) = 1 #
≤P QRCT (ξn⋆,t(a,h) = 0| Fn⋆−1,t) +P QRCT (ξn⋆,t(a,h) = 1| Fn⋆−1,t) exp{−ε}
= 1−P QRCT (ξn⋆,t(a,h) = 1| Fn⋆−1,t) (1−exp{−ε})
≤exp{−P QRCT (ξn⋆,t(a,h) = 1| Fn⋆−1,t) (1−exp{−ε})},
where the first inequality follows from the numeraire property ofλ(Q) t (a, h)[ 13, Theorem 15.2.2] (see also
[63, 51]) and the second inequality follows from1 +x≤exp{x}for allx∈R.
Notice how PQRCT (ξn⋆,t(a,h) = 1| Fn⋆−1,t) = πt(a) + πt(0), which follows from the fact that condi-
tioning on Fn⋆−1,t the realization ofHn⋆,t−1 is known and fixed. Thus, from Assumption 2 we have that
PQRCT (ξn⋆,t(a) = 1| Fn⋆−1,t)≥2p t, which leads to the following upper bound
exp{−P QRCT (ξn⋆,t(a) = 1| Fn⋆−1,t) (1−exp{−ε})} ≤exp{−2p t(1−exp{−ε})}.
Recursively applying the above arguments we get the following inequality
EQRCT
h
exp{−N a(t)ε}

WNa(t)/W (Q) Na(t)
i
≤exp


−2 (1−exp{−ε})
X
s∈Tt(a)
nsps


 ,
proving Lemma E.3. We end the proof by noting that the same result follows for the setting in which
units are not stratified in each sub-experiment. This is because in this setting the process no longer has
the product over strata in each sub-experiment, which as we argued above has no effect on the conditional
probability of the inclusion indicators and, thus, the effective sample size per treatment arm.■
E.5 Almost sure infinite per-arm allocation
Lemma E.4.Fix a sub-experiment s∈ [t]and a treatment a∈ As. Recall the definitionsns := |Is| and ˇNa(s) := P i∈Is 1{A i,s =aorA i,s =0} , where Ai,s ∼Categorical As∪{0}(πs). Under Assumption 2 we have that
ˇNa(s)→ ∞asn s → ∞.
37

Proof. We define the shorthandRCTs := CategoricalAs∪{0}(πs). By the strong law of large numbers we
have that
lim
ns→∞
ˇNa(s)
ns
=P RCTs (Ai,s =aorA i,s =0) RCT s-almost surely.
Indeed, notice how the probability can be written as:
PRCTs (1{A i,s =aorA i,s =0}= 1) =P RCTs (Ai,s =aorA i,s =0)
=P RCTs (Ai,s =a) +P RCTs (Ai,s =0)>0,
where the second equality follows from the fact that the events{Ai,s =a} and {Ai,s =0} are mutually
exclusive, and the inequality is due to Assumption 2 which tells us thatPRCTs (Ai,s =a)> 0and
PRCTs (Ai,s =0)> 0. Hence, we can conclude thatˇNa(s) → ∞almost surely asns → ∞, completing the
proof. ■
Lemma E.5.Fix a treatment a∈ Aand recall thatt := arg mins∈[t] ns. Then, under Assumption 2 and
the data collection protocol from Algorithm 2 we have that
Na(t)→ ∞asn t → ∞.
Proof of Lemma E.5.Fix a treatment a∈ A. We start by recalling the definitiont := arg mins∈[t] ns,
from which we can see how
nt → ∞implies thatn s → ∞,∀s∈[t].
Hence, together with the definitionNa(t) := P s∈Tt(a) ˇNa(s)and Lemma E.4 it implies that
Na(t)→ ∞asn t → ∞,
completing the proof. ■
38
