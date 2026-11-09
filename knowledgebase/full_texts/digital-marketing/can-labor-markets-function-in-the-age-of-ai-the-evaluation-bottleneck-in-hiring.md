---
title: Can Labor Markets Function in the Age of AI? The Evaluation Bottleneck in Hiring
url: https://arxiv.org/abs/2609.30058
category: digital-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Itai Ashlagi
- Ramesh Johari
- Jon Kleinberg
- Anushka Murthy
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.30058
pages: 41
chars: 81931
fetched_at: '2026-11-08T13:20:21+00:00'
kb_version: 1
---

# Can Labor Markets Function in the Age of AI? The Evaluation Bottleneck in Hiring

Can Labor Markets Function in the Age of AI? The Evaluation
Bottleneck in Hiring
Preliminary Draft – Comments Welcome!
Itai Ashlagi, Ramesh Johari, Jon Kleinberg, Anushka Murthy
September 25, 2026
Abstract
AI-assisted job-search tools have become increasingly popular by making it easier to find
and apply to jobs. But by making it easier for applicants to generate and tailor application
materials, they can also reduce how informative those materials are about applicant fit. We
study this tradeoff in a hiring market where applicants differ in experience and latent match
quality and firms use noisy application materials to decide whom to screen. We ask how AI
affects downstream screening and hiring, and which applicants are most adversely affected. As
application materials become less informative, a Bayesian firm rationally relies more heavily on
coarse observables such as prior experience. Among the four applicant types defined by experi-
ence and compatibility for the job, inexperienced-compatible applicants are the most exposed:
they lack observable experience and lose the individualized information that could distinguish
them from other inexperienced candidates. When screening is costly, these changes can also gen-
erate inefficient screening failures in which firms screen no applicants or screen only experienced
applicants. We then show that multistage hiring can arise as an endogenous firm response: a
relatively inexpensive intermediate assessment allows firms to acquire new evidence of fit before
costly full screening. This can restore screening opportunities that disappear under one-stage
hiring and give inexperienced-compatible applicants a path to screening. Our results show how
AI can shift the central friction in hiring from submitting applications to obtaining credible
evaluation, creating entry barriers for high-fit workers without prior experience. Multistage hir-
ing can endogenously arise in response, restoring evaluation opportunities that would otherwise
disappear and helping preserve market functioning.
1 Introduction
There has been a proliferation of AI-assisted job-search tools. Applicants increasingly use AI
systems to draft resumes and cover letters, tailor materials to specific vacancies, search across
platforms, and submit applications at scale [19, 46]. Yet the experience of many job seekers and
employers has not improved accordingly. Recent accounts describe applicants submitting large
numbers of applications with little response, while firms report receiving growing volumes of in-
creasingly similar and difficult-to-verify materials [1, 36, 45]. Critics have consequently warned that
AI-mediated hiring may push firms toward relying on existing brand-name signals and referral net-
works rather than a more open and meritocratic labor market [17]. This concern is especially salient
for new labor-market entrants: recent college graduates continue to face elevated unemployment
and underemployment [25].
1
arXiv:2609.30058v1  [cs.GT]  24 Sep 2026

These developments point to a tension in AI-mediated job search. AI can make it easier for
workers to enter an applicant pool without necessarily making it easier for firms to determine which
applicants are good matches. Indeed, if widespread AI assistance makes written applications less
individually informative, the central friction in hiring may shift from submitting an application to
the provision and generation of credible, individualized evidence of fit.
Recent evidence suggests that AI weakens applicant-generated signals. Galdin and Silbert [28]
find that customized applications predicted hiring before the introduction of large language models
but became less valuable afterward; eliminating the signaling value of written applications can
make hiring substantially less meritocratic. Studying the rollout of an AI-assisted cover-letter
tool, Cui et al. [22] find that AI increased tailoring and callbacks but reduced tailoring’s predictive
content, shifting employers to rely more heavily on past work history and potentially disadvantaging
new workers. More generally, Cowgill et al. [20] show that sender-side access to generative AI
reduces screening accuracy on average, although its effects depend on how AI changes the relative
informativeness of experts’ and non-experts’ messages. Together, these studies suggest that AI can
weaken applicant-generated signals and shift the evidence firms use for screening.
This paper develops a model of how such a change in the information structure affects access
to screening and hiring. While a large literature studies the effects of automation and AI on
tasks, productivity, wages, employment, and vacancy creation [2, 3, 11, 12, 15, 26, 51], we focus
on job search and screening. We consider a firm with a vacancy and heterogeneous potential
applicants. Greater AI saturation lowers applicants’ costs of applying, reduces the informativeness
of application materials, and raises the firm’s effective cost of identifying compatible candidates.
Applicants differ in observable experience and latent match quality. The firm observes experience
and noisy application materials, forms Bayesian posterior beliefs about compatibility, and chooses
whom to screen.
Our first set of results shows how degrading individualized information can create an entry bar-
rier for compatible workers without prior experience. As application materials become noisier, the
firm places less weight on applicant-specific evidence and more on experience-based priors. Inexpe-
rienced applicants therefore need stronger favorable evidence to overcome experienced applicants’
prior advantage. This mechanism is analogous to classic models of statistical discrimination [4, 44],
but with respect to applicant experience.
This reweighting is privately rational but disproportionately harms inexperienced-compatible
candidates. As individualized signals deteriorate they lose the evidence that could offset the lower
prior associated with inexperience. As a result, increasing AI saturation can harm labor-market
entry even for workers who are good matches.
We then show that private screening can be inefficient. The firm screens applicants only when
the expected private value of doing so exceeds the screening cost, but it does not internalize the
worker’s surplus from a successful match. This creates a gap between the firm’s privately optimal
screening cutoff and the socially efficient screening cutoff, resulting in some applicants who are
worth screening being rejected. We characterize two resulting market failures: one in which the
firm screens no applicant even though a social planner would screen at least one, and another in
which the firm excludes all submitted inexperienced-compatible applicants even though screening
at least one of them would increase expected total surplus. As application materials become
uninformative, applicants’ posterior compatibility converges toward their experience-group priors.
These failures can therefore arise systematically: screening either shuts down or continues only for
experienced applicants while excluding inexperienced-compatible candidates.
2

Finally, we study whether a multistage hiring process can mitigate these failures. Rather than
making hiring decisions entirely from increasingly noisy application materials, firms may create
lower-stakes opportunities for applicants to generate additional credible evidence of fit. In our
model, this takes the form of a relatively inexpensive intermediate assessment, such as a work-
sample task, live skill test, or structured preliminary interview, which allows the firm to acquire
additional applicant-specific information before undertaking costly full evaluation. More broadly,
internships, predoctoral positions, and other temporary or probationary roles may serve a related
function by allowing workers—particularly those with limited prior experience—to demonstrate
their match quality through performance.
We characterize an intermediate-assessment region consisting of applicants whose posterior
compatibility is too low to justify immediate full screening but high enough that acquiring an
additional signal is valuable. These applicants are rejected under one-stage hiring but can advance
under multistage hiring after a favorable intermediate assessment. When this region is nonempty,
the firm strictly prefers a multistage hiring process, which can avoid the screening failures that occur
under one-stage hiring. It also gives inexperienced-compatible applicants who would otherwise be
rejected a positive-probability path to screening and hiring. At high levels of AI saturation, this
benefit extends to nearly all submitted inexperienced-compatible applicants.
Taken together, our results explain why easier application need not improve job access or wel-
fare. As applicant-generated materials become less informative, firms rely more on experience-based
priors and allocate costly evaluation more selectively, disproportionately harming inexperienced-
compatible applicants. Nevertheless, we find a hopeful feasible path forward: we show that multi-
stage hiring emerges as a privately beneficial firm response that creates a new channel for credible,
individualized evidence, and gives inexperienced workers an opportunity to demonstrate fit before
firms rely on coarse experience-based priors.
2 Related Literature
Our paper connects three streams of research: AI, signaling, and screening in labor markets; di-
rected and sequential search; and statistical discrimination and talent discovery.
AI and labor-market signaling.We build on classic models of signaling, screening, and cheap
talk [21, 24, 47, 49]. Recent evidence shows that generative AI can weaken applicant-generated
signals and change the information employers use [20, 22, 28]. We study how this deterioration
affects access to costly individualized screening and whether multistage evaluation can mitigate the
resulting screening failures. Closest to our work, Jungbauer [35] studies how AI-induced deterio-
ration in initial-stage screening signals disrupts assortative matching. Jungbauer also shows that
the optimal redesign of a common screening signal need not restore pre-AI levels of informative-
ness. In contrast, we study how degraded initial information affects access to costly individualized
evaluation across experience groups, and how multistage hiring processes can adapt when initial
applicant signals become less informative.
Directed and sequential searchOur model also relates to work on directed search, decen-
tralized matching, and sequential information acquisition. Classic job-search models study costly
search under uncertainty [39], while directed and competitive search models study decentralized
3

markets in which workers direct applications based on observable opportunities and expected com-
petition [5, 16, 29, 40, 43, 53]. Related work on online labor markets shows how application costs,
congestion, and screening frictions shape applicant and employer behavior [8, 23, 27, 30, 31]. Most
closely, Arnosti et al. [8] study a decentralized market in which applicants pay to apply and employ-
ers pay to screen. We focus on an additional information friction: the signals firms use to decide
whom to screen can themselves become less informative.
The firm’s problem also has a sequential-search interpretation. Our one-stage baseline special-
izes Weitzman [52] to hiring: the firm orders applicants by posterior compatibility and inspects
them until it finds an acceptable candidate or further inspection is not worthwhile. The multi-
stage model allows partial information acquisition before full screening, connecting to sequential
inspection problems such as Aouad et al. [7] and to hiring models with intermediate assessments
or interviews [10, 33, 34, 37]. We study how the value of this sequential evaluation changes as
applicant-generated information deteriorates and experience generates heterogeneous prior beliefs
about fit.
Statistical discrimination and entry barriersOur entry-barrier results are closely related
to statistical discrimination. When firms observe noisy individual signals, they may rationally
condition decisions on observable characteristics correlated with expected productivity [4, 9, 44].
In our setting, experience plays this role: as applicant-generated materials become less informative,
the firm places greater weight on experience-group priors. High-fit inexperienced applicants are
especially harmed because they lose the applicant-specific information that could distinguish them
from lower-fit workers in the same group.
Related employer-learning models study how firms initially rely on observable characteristics
and update as better information arrives [6]. We instead study whether applicants receive the
costly information acquisition needed to overcome an unfavorable prior. This connects to work on
inefficient talent discovery and certification in entry-level labor markets [38, 42, 48, 50].
Although our baseline is static, reduced access to interviews and jobs may also limit inexperi-
enced workers’ ability to accumulate the experience firms increasingly rely on, potentially reinforc-
ing initial disparities [13, 18, 41]. Related to us, Hu and Chen [32] show that temporary two-stage
hiring can shift a market toward a more equitable long-run equilibrium; our multistage process
instead generates additional applicant-specific information before full screening.
3 Model
We study a firm with one vacancy andn >1 potential applicants. AI saturation is modeled by an
exogenous parameterq∈[0,1), which affects three screening and application primitives described
below: the application-cost scalec a(q), the varianceσ 2 m(q) of the noise in the application-materials
signalm i, and the effective firm screening costc s(q).
Environment and payoffs.If the firm hires a compatible applicant, the firm receives payoff
vF >0. The hired applicant receives payoffv A >0. We interpretv F andv A as the respective
gains to the firm and applicant from a compatible match, relative to their outside options, so total
surplus from a compatible match isv F +v A. If no hire occurs, no match surplus is generated;
applicants still bear any application costs they have incurred, and the firm still bears any screening
costs it has incurred.
4

Applicants.Applicantihas observable experience
ei ∈ {0,1},
wheree i = 1 denotes experienced ande i = 0 denotes inexperienced. Let
λe = Pr(ei =e), λ 0 +λ 1 = 1.
Applicantialso has latent match qualityz i ∈R. Match quality is not observed by the firm
before screening. Applicant compatibility is given by
ki =1{z i ≥0}.
The firm seeks to hire an applicant withk i = 1. We refer to the pair (e i, ki)∈ {0,1}2 as applicant
i’s realized type. Thus (1,1) denotes an experienced-compatible applicant, (1,0) an experienced-
incompatible applicant, (0,1) an inexperienced-compatible applicant, and (0,0) an inexperienced-
incompatible applicant.
Priors and application materials.Conditional on experience,
zi |e i =e∼ N(µe, σ2 z ), e∈ {0,1},(1)
withµ 1 > µ0 >0. Thus experienced applicants have higher expected match quality.
Conditional on applying, applicantigenerates a materials signal
mi =z i +ε i, ε i ∼ N(0, σ2 m(q)).(2)
Application decisions.Applicantiobserves her experiencee i and application costc a(q)ηi before
applying, but does not observez i. Letd i ∈ {0,1}denote applicanti’s application decision. If she
applies, she pays
ca(q)ηi.
The cost scalingsη i are nonnegative, withη i |e i =ehaving CDFF e onR +, and capture id-
iosyncratic differences in the time, effort, or opportunity costs applicants face when preparing
and submitting an application. We assume these scalings are independent of match quality and
application signal noise conditional on experience.
Let
αe(q) := Pr(di = 1|e i =e)
denote the equilibrium group-specific application rate. Given application rates (a 0, a1), let
Ve(q;a 0, a1) :=v A Pr(hired|e i =e, di = 1;q, a0, a1)
denote the expected value of applying for an applicant from experience groupe. An applicant
with experienceeapplies if and only if
Ve(q;a 0, a1)≥c a(q)ηi.
Thus, whenc a(q)>0, equilibrium application rates satisfy
5

αe(q) =F e
 Ve(q;α 0(q), α1(q))
ca(q)

.
Whenc a(q) = 0, we choose a tie-breaking convention that selects
αe(q) = 1.
Firm screening technology .The firm observes (e i, mi) for each submitted application. Screen-
ing applicanticosts
cs(q)
and revealsz i perfectly. The firm must screen an applicant before hiring them.
Let
pi = Pr(ki = 1|m i, ei)
denote applicanti’s posterior compatibility.
Assumptions.We complete the model specification by describing how AI saturation affects the
key primitives, and by imposing a regularity condition that ensures positive participation by both
experience groups.
The following assumption captures the idea that as AI tools become more prevalent, submitted
materials become less individually informative about latent match quality.
Assumption 3.1(AI saturation lowers signal informativeness).The signal-noise varianceσ 2 m(q)
is strictly increasing inq.
The next assumption captures the contrasting effects of AI on costs faced by the two sides of
the market. AI tools can reduce the time and effort required to generate applications, lowering
applicants’ effective cost of applying. At the same time, AI may increase the firm’s effective cost
of identifying compatible applicants, for example because AI-generated application materials can
become more homogeneous or less informative.
Assumption 3.2(AI saturation lowers application costs and raises effective screening costs).The
application-cost scalec a(q) is strictly decreasing inq, and the effective screening costc s(q) is strictly
increasing inq.
The final assumption on the distribution of experience groups and application costs ensures
that both experience groups apply with positive probability; we expand more on this at the end of
Section 4.
Assumption 3.3(Positive participation assumptions).Both experience groups occur with positive
probability,
λe >0, e∈ {0,1},
and zero lies in the support of each experience-specific application-cost distribution:
Fe(x)>0 for everyx >0, e∈ {0,1}.
6

Timing.The timing is as follows.
First, for each applicanti, their experiencee i, latent match qualityz i, and application cost
scalingη i are sampled, independently across applicants. Applicants observe (e i, ηi) but do not
observez i.
Second, applicants decide whether to apply. Applicants who apply payc a(q)ηi.
Third, submitted applications generate materials signalsm i, and the firm observes (e i, mi) for
each applicant in the realized pool of applications.
Fourth, the firm forms posterior compatibility beliefsp i = Pr(ki = 1|m i, ei) and chooses whom
to screen. Screening costsc s(q) per applicant and revealsz i. The firm hires the first compatible
applicant it screens, if any, and applicant and firm values are realized.
4 Bayesian Reweighting and Firm Screening
In this section, we characterize how AI saturation changes the firm’s posterior beliefs and optimal
one-stage screening decisions.
Posterior beliefs and Bayesian reweighting.Among submitted applicants, the firm updates
from the experience-group prior in Equation (1) using the materials signal in Equation (2).
Let
∆µ :=µ 1 −µ 0 >0
denote the experience-group prior difference. Define
κ(q) := σ2 z
σ2z +σ 2m(q)
and
σ2 post(q) := σ2 z σ2 m(q) σ2z +σ 2m(q) .
For each applicant, define the posterior-mean score
Si(q) :=E[z i |m i, ei;q].
Finally, let
θ(q) := (1−κ(q))∆ µ.
The following result describes how the firm updates their posterior after receiving an application.
Proposition 4.1(Bayesian reweighting toward experience).Fixqwithσ 2 m(q)>0. Conditional
on a given level of AI saturation and applicanti’s materialsm i and experiencee i, the firm assigns
them a posterior compatibility probability given by:
pi(q) = Φ
 Si(q)
σpost(q)

,
where
Si(q) =κ(q)m i + (1−κ(q))µ ei = (1−κ(q))µ 0 +θ(q)e i +κ(q)m i.
7

For any submitted applicantsiandj,
pi(q)≥p j(q)⇐ ⇒S i(q)≥S j(q).
Under Assumption 3.1, for anyeq > q,
κ(eq)< κ(q), θ(eq)> θ(q),
and
θ(q)
κ(q) = ∆µ σ2 m(q) σ2z
is strictly increasing inq.
The proposition formalizes the statistical-discrimination mechanism. As application materials
become noisier, the firm’s Bayes-optimal response is to place less weight on the applicant-specific
materials signal and more weight on the applicant’s prior experience. Equivalently, the amount of
materials evidence required to offset the prior difference between experienced and inexperienced
applicants increases with AI saturation.
Optimal one-stage screening.Suppose the firm receivesMsubmitted applications and ob-
serves posterior compatibilities for each applicant in the realized pool. Relabel the submitted
applicants so that
p1(q)≥p 2(q)≥ · · · ≥pM (q).
Define the firm’s private screening cutoff by
pF (q) := cs(q) vF .
The following proposition characterizes the firm’s optimal one-stage screening rule. 1
Proposition 4.2(Optimal one-stage screening rule).Fixqand a realized applicant pool. Suppose
vF >0and considerp F (q) := cs(q) vF ∈(0,1). The firm’s optimal screening policy is to order appli- cants by decreasing posterior compatibility and screen them sequentially until either a compatible
applicant is found or no remaining applicant satisfies
pi(q)≥p F (q).
Equivalently, the firm’s screening list consists of applicants whose posterior compatibility satisfies
pi(q)≥p F (q) = cs(q) vF .
Under Assumption 3.2, for everyeq > q,
pF (eq)> pF (q).
1This problem is a binary-payoff special case of Weitzman’s Pandora problem; see [52]. Each applicant is a “box,”
screening is inspection, and the hidden payoff isv F ki. To remain self-contained, we give a direct proof of the optimal
screening rule.
8

The result follows from comparing the marginal value of screening the next applicant to the
marginal screening cost. Conditional on reaching applicantn, screening is profitable exactly when
vF pn ≥c s(q).
Thus the posterior compatibility cutoff is given by
pF (q) = cs(q) vF .
Proposition 4.2 implies that the firm can equivalently use a score cutoff. Since
pi = Φ
 Si(q)
σpost(q)

and Φ is strictly increasing, the posterior cutoffp i ≥p F (q) is equivalent to
Si(q)≥s F (q),
where
sF (q) :=σ post(q)Φ−1  pF (q)  .
Thus the firm may equivalently rank applicants by their posterior-mean scores and include applicant
iin its screening list if and only ifS i(q)≥s F (q).
Positive application rates.We end this section by noting that the results in the following
sections require only that applicants from both experience groups submit applications with positive
probability. Assumption 3.3 ensures that this occurs for anyqsuch thatp F (q)∈(0,1). Because the
Gaussian materials signal has full support, an applicant from either experience group has positive
probability of being compatible and drawing materials that place their posterior abovepF (q). There
is also positive probability that every other potential applicant is incompatible. Hence
Ve(q;α 0, α1)>0, e∈ {0,1},
and therefore
αe(q)>0, e∈ {0,1}.
5 Impact on Workforce Entry and Market Failure
Section 4 shows that noisier application materials shift the firm toward experience-based priors and
change its screening decisions. We now show that the effects of this reweighting are uneven across
the applicant pool: inexperienced-compatible applicants are especially exposed, and sufficiently
high AI saturation can generate screening failures in which the firm forgoes screening anyone or
screens only experienced candidates.
9

5.1 Shortlisting Exposure
Recall that applicants have realized types
(e, k)∈ {0,1}2,
whereedenotes experience andkdenotes compatibility. Although compatibility is observed only
after screening, conditioning on realized compatibility allows us to identify which types are helped
or harmed by the firm’s Bayes-optimal scoring rule. By Proposition 4.1, the firm’s posterior-mean
score is
Si(q) =E[z i |m i, ei;q] =κ(q)m i + (1−κ(q))µ ei.
Higher AI saturation lowersκ(q), so the firm places less weight on application materials and
more weight on experience. We first study how this reweighting changes the average score of each
realized type. We then study how higher AI saturation affects the probability that an applicant
clears the firm’s posterior screening threshold.
Conditional mean score.For applicants who apply, define the conditional mean score of type
(e, k) by
¯Sek(q) :=E[S i(q)|e i =e, k i =k, d i = 1].
Because applicants do not observez i before applying and the application costs are indepen-
dent of match quality conditional on experience, conditioning on application does not change the
distribution ofz i within an experience group. Hence,
¯Sek(q) =κ(q)µ ek + (1−κ(q))µ e,
where
µek :=E[z i |e i =e, ki =k].
For AI saturation levelsq,˜q, let ∆ ¯Sek(q,eq) := ¯Sek(˜q)− ¯Sek(q) denote the change in conditional
mean score.
Proposition 5.1(Conditional mean score effects).Consider AI saturation levelsq <eq. Under
Assumption 3.1,
∆ ¯Sek(q,eq) = [κ(eq)−κ(q)] (µek −µ e).
Moreover,
∆ ¯S01(q,eq)<∆ ¯S11(q,eq)<0<∆ ¯S00(q,eq)<∆ ¯S10(q,eq).
Proposition 5.1 shows that among the four realized types, inexperienced-compatible applicants
face the largest negative change in their conditional mean score. In particular, Bayesian reweighting
toward experience creates an entry barrier for new but high-fit candidates.
The intuition behind the result is that conditional on experience, compatible applicants have
above-average match quality:µ e1 > µe. Asκ(q) falls, their favorable individualized information re-
ceives less weight, so their conditional mean scores fall. Incompatible applicants have below-average
match quality so reducing the weight on individualized information raises their mean posterior
scores. Within the pool of compatible applicants, inexperienced-compatible applicants experience
a greater decrease than experienced-compatible applicants because their experience-group prior
has a lower mean. In other words, they don’t have pre-existing experience to compensate for the
decreased weight given to their application materials.
10

Probability of clearing the screening threshold.The mean-score result captures how AI
saturation shifts the average position of each realized type in the firm’s screening score. However,
inclusion in the firm’s screening list is instead a threshold event: applicantiis included only if
pi(q)≥p F (q).
We therefore next study the probability that a type-(e, k) applicant clears the shortlisting score
threshold. To separate the effect of declining signal informativeness from movement in the firm’s
screening threshold, we study the standardized match quality and application materials across
experience groups.
Fix an experience groupeand define
Xi := zi −µ e σz , Y i(q) := mi −µ ep σ2z +σ 2m(q) .
Conditional one i =e, both variables are standard normal, with correlation
r(q) := σzp
σ2z +σ 2m(q) .
Thusr(q) summarizes how informative application materials are about match quality. Under
Assumption 3.1,r(q) is strictly decreasing inq.
Compatibility is equivalent to
Xi ≥a e, a e :=− µe σz .
Sinceµ 1 > µ0, we havea 1 < a0.
The firm’s screening cutoff can also be expressed in units of the standardized materials signal.
Since
Si(q) =µ e +σ zr(q)Yi(q),
and
pi(q) = Φ
 Si(q)
σpost(q)

,
the condition
pi(q)≥p F (q)
is equivalent to
Yi(q)≥b e(q),
where
be(q) := σpost(q)Φ−1  pF (q)  −µ e σzr(q) .
Thusb e(q) is the number of within-group standard deviations by which an applicant’s materials
must exceed their experience-group mean to enter the firm’s screening list.
Forb∈Randr∈(0,1), let (X, Y) be a standard bivariate normal pair with correlationr, and
define
ψe1(b, r) := Pr(Y≥b|X≥a e),
11

and
ψe0(b, r) := Pr(Y≥b|X < a e).
The screening-list inclusion probability of a submitted type-(e, k) applicant is therefore
Pr

pi(q)≥p F (q)|e i =e, k i =k, d i = 1  =ψ ek (be(q), r(q)).
Proposition 5.2(Signal informativeness and relative experience thresholds).Supposep F (q)∈
(0,1),σ 2 m(q)>0, andσ 2 m(q)is differentiable with
dσ2 m(q)
dq >0.
For eache∈ {0,1},b∈R, andr∈(0,1),
∂ψe1(b, r)
∂r >0, ∂ψe0(b, r) ∂r <0.
Moreover,
b0(q)−b 1(q) = ∆µ σzr(q) ,
and hence
d
dq [b0(q)−b 1(q)] =− ∆µr′(q) σzr(q)2 >0.
The first part of Proposition 5.2 isolates the effect of increased AI saturation on threshold clear-
ing probability through changing signal informativeness while holding the standardized screening
threshold fixed. Because increasing AI saturation reduces signal informativeness, i.e.,r ′(q)<0,
noisier application materials reduce the probability that a compatible applicant clears a fixed thresh-
old and increase this probability for an incompatible applicant. The second part identifies how
AI saturation affects the threshold clearing probability by changing the relative experience-group
thresholds. The standardized threshold for inexperienced applicants is higher compared to experi-
enced applicants, and this difference grows as application materials become less informative.
Inexperienced-compatible applicants are therefore the only group on the adverse side of both
of these mechanisms: compatibility makes them vulnerable to the decline in signal informative-
ness, while inexperience requires them to clear a higher relative screening threshold compared to
experienced applicants.
5.2 Market Failure
The preceding results show that inexperienced-compatible applicants are especially exposed to the
loss of individualized information at the shortlisting stage. We now show that the firm’s privately
optimal screening decision can also be socially inefficient.
The source of inefficiency is that the firm does not internalize the worker’s surplus from a
successful match. The firm receives valuev F from hiring a compatible applicant, while total surplus
from a compatible match isv F +v A. Recall from Proposition 4.2 that the firm’s private screening
cutoff is
pF (q) = cs(q) vF .
12

Define the following screening cutoff; in the next proposition, we show it is the cutoff a social
planner would use:
pP (q) := cs(q) vF +v A .
We suppose throughout this subsection thatv F >0,v A >0, andp F (q)∈(0,1). Then it follows
that
0< pP (q)< pF (q)<1.
Proposition 5.3(Firm and social planner screening cutoffs).Fixqand a realized applicant pool.
The social planner’s optimal screening rule is to order applicants by decreasing posterior compati-
bility and include applicantiin the screening list if and only if
pi(q)≥p P (q).
Consequently, applicantiis included in the planner’s screening list but not the firm’s screening list
if and only if
pP (q)≤p i(q)< pF (q).
The difference between the private and social screening cutoffs is
pF (q)−p P (q) = vAcs(q) vF (vF +v A) >0.
Thus the preceding shows that there is a nonempty range of applicants whom the planner would
screen but the firm would reject. Under Assumption 3.2, the gap between the private and social
screening cutoffs increases with AI saturation:
d
dq

pF (q)−p P (q)  = vAc′ s(q) vF (vF +v A) >0.
Higher effective screening costs therefore expand the range of posterior compatibilities for which
screening is socially valuable but privately unprofitable.
Two screening-failure events.We first characterize two screening-failure events conditional on
the firm’s realized pool of submitted applications. We eventually show that these screening-failure
events occur with probability approaching one in the high-AI limit. LetA(q) denote the submitted
applicant pool. WhenA(q) is nonempty, define
pmax(q) := max
i∈A(q)
pi(q).
This is the highest posterior compatibility among submitted applications.
Proposition 5.4(No-hire screening failure).SupposeA(q)is nonempty and
pP (q)< pmax(q)< pF (q).
Then the firm’s screening list is empty, while the social planner’s screening list is nonempty.
13

Under the conditions of this result, the firm screens no applicants sincep max(q)< p F (q) and
hence makes no hire. However, a social planner would screen at least the applicant with posterior
compatibilityp max(q) and would hire that applicant if they are compatible. Thus the firm does not
screen anyone even though screening and potential hiring would increase expected total surplus.
A more targeted failure occurs when the firm excludes all inexperienced-compatible applicants
from screening even though at least one such applicant is socially worth screening. Let
A01(q) :={i∈ A(q) :e i = 0, ki = 1}
denote the set of submitted inexperienced-compatible applicants. WhenA 01(q) is nonempty, let
pmax 01 (q) := max i∈A01(q) pi(q)
be the highest posterior compatibility across the inexperienced-compatible applicants.
Proposition 5.5(Inexperienced-compatible screening failure).SupposeA 01(q)is nonempty and
pP (q)< pmax 01 (q)< pF (q).
Then no inexperienced-compatible applicant is included in the firm’s screening list, while at least
one inexperienced-compatible applicant is included in the social planner’s screening list.
Under the conditions of Proposition 5.5, inexperienced-compatible candidates can therefore
be fully excluded from screening even though screening and potentially hiring an inexperienced-
compatible candidate would increase expected total surplus.
The preceding two propositions characterize the conditions under which the two screening fail-
ures occur. On their own, however, these fixed-pool conditions do not imply that the failures are
systematically likely to arise. We therefore turn next to the high-AI limit, where we show that
the same failure events can occur with probability approaching one as individualized information
disappears.
Screening failures in the high-AI limit.We now turn to the central result of this subsection.
Although the preceding propositions characterize when the two failures occur for a realized pool, the
high-AI limit shows that these failures can occur with probability approaching one. As application
materials lose their informativeness, applicants’ posterior compatibility probabilities collapse to-
ward their experience-group priors. Screening therefore increasingly depends on coarse group-level
information rather than applicants’ realized compatibility, allowing the private and social screening
thresholds to generate persistent screening failures.
For each experience group, define the prior compatibility probability
πe := Pr(ki = 1|e i =e) = Φ
 µe
σz

.
Becauseµ 1 > µ0,π 1 > π0. Consider a sequence{q n}such that
σ2 m(qn)→ ∞
and
pF (qn)→p F ∞ ∈(0,1).
14

Since
pP (q) = vF
vF +v A
pF (q),
the social cutoff converges to
pP ∞ := vF vF +v A pF ∞,
where 0< pP ∞ < pF ∞ <1. The following lemma shows that when application materials become unin-
formative, individual posterior compatibility converges to the prior associated with the applicant’s
experience group.
Lemma 5.6(High-noise posterior pooling).For any fixed submitted applicant with realized type
(e, k),
pi(qn)→π e
in probability, conditional on
ei =e, k i =k, d i = 1.
Consequently, for any fixed finite submitted poolB,
max
i∈B
|pi(qn)−π ei| →0
in probability, conditional on the realized types inB.
Note that the convergence in the above lemma holds even after conditioning on an applicant’s
realized compatibility: the firm cannot recover that compatibility from increasingly noisy materials.
Now fix a finite submitted poolB, viewed as given at the screening stage, and condition on its
realized applicant types. Define
πmax B := max i∈B πei.
Also define
B01 :={i∈ B:e i = 0, ki = 1},B 1 :={i∈ B:e i = 1}.
Corollary 5.7(High-noise screening failures).The following statements hold along the sequence
{qn}.
(i) Ifp P ∞ < πmax B < pF ∞, then
Pr

pP (qn)<max i∈B pi(qn)< pF (qn)

→1.
(ii) SupposeB 01 is nonempty. Ifp P ∞ < π0 < pF ∞, then
Pr

pP (qn)<min i∈B01 pi(qn)≤max i∈B01 pi(qn)< pF (qn)

→1.
If, in addition,B 1 is nonempty andp F ∞ < π1, then
Pr

min
i∈B1
pi(qn)> pF (qn)>max i∈B01 pi(qn)

→1.
15

Part (i) implies that, conditional on the submitted poolB, the no-hire screening failure in
Proposition 5.4 occurs with probability approaching one. Part (ii) implies that every submitted
inexperienced-compatible applicant lies below the firm’s cutoff but above the social cutoff with
probability approaching one. Thus the inexperienced-compatible screening failure in Proposition
5.5 occurs with probability approaching one. Under the additional condition
π0 < pF ∞ < π1,
the firm continues to include experienced applicants in its screening list while excluding all sub-
mitted inexperienced-compatible applicants. The limiting outcome is therefore a screening failure
concentrated on inexperienced candidates rather than a complete shutdown of screening.
Taken together, these results show that the screening failures identified above can arise with
probability approaching one as AI saturation grows. As application materials become uninforma-
tive, the firm can no longer distinguish compatible from incompatible applicants within an experi-
ence group, and posterior beliefs collapse toward group-level priors. The hiring process is therefore
governed increasingly by observable experience rather than realized compatibility. Depending on
the location of the experience-group priors relative to the private and social screening cutoffs, this
produces either a complete shutdown of privately provided screening or continued screening of
experienced applicants alongside the systematic exclusion of inexperienced-compatible applicants.
6 Multistage Hiring as a Response to AI-Induced Entry Barriers
The preceding section shows that AI saturation can raise entry barriers by making written appli-
cation materials less informative and full screening more expensive. This section studies a firm
response: adding a cheaper intermediate assessment before costly full screening. Examples include
live skill tests, work-sample exercises, or other verifiable tasks that are harder for AI-generated
application materials to mimic.
We show that the firm strictly benefits from adding an intermediate screening stage and that
doing so can restore hiring opportunities for inexperienced-compatible applicants who are disad-
vantaged by degraded initial signals. These benefits become especially strong as AI saturation
grows.
6.1 Multistage Screening
After observing (m i, ei) and forming the baseline posterior
pi(q) := Pr(ki = 1|m i, ei;q),
the firm may pay an intermediate-assessment cost
cℓ(q)∈[0, c s(q))
to observe an additional signala i. After observing this signal, the firm’s posterior compatibility
belief is
epi(q) := Pr(ki = 1|m i, ei, ai;q).
The firm may then reject the applicant or pay the full screening costc s(q), which reveals compati-
bility perfectly.
16

Submitted applications remain available until the vacancy is filled or the firm terminates search,
and retaining an unassessed application in the pool is costless. Let
Π1S(q) and Π M S(q)
denote the sets of feasible one-stage and multistage policies, respectively, conditional on the realized
submitted poolA(q) and the pre-assessment information{(m i, ei) :i∈ A(q)}observed by the firm.
For any feasible policyπ, letU(π;q) denote the firm’s expected payoff underπ, conditional on this
information and net of all intermediate-assessment and full-screening costs. Define
U 1S,∗(q) := sup
π∈Π1S (q)
U(π;q)
and
U M S,∗(q) := sup
π∈ΠM S(q)
U(π;q).
Because the firm can implement any one-stage policy by never using the intermediate assess-
ment,
Π1S(q)⊆Π M S(q).
Consequently,
U M S,∗(q)≥U 1S,∗(q).(3)
This inequality follows directly from nesting. The results in the next subsection therefore focus
on conditions under which the inequality is strict and the intermediate assessment is used with
positive probability.
The value of the intermediate assessment comes from its ability to refine the firm’s posterior
before the full screening cost is incurred. By iterated expectations,
E[epi(q)|m i, ei;q] =p i(q).
Thus the refined posterior is a mean-preserving refinement of the baseline posterior.
To isolate the value of this refinement, suppose the vacancy remains open and applicantiis the
firm’s only remaining option. If the firm’s current posterior compatibility belief isx, its optimal
continuation payoff without an intermediate assessment is
fq(x) := (vF x−c s(q))+ =v F

x−p F (q)  + ,
where
(y)+ := max{y,0}
and
pF (q) = cs(q) vF
is the one-stage screening cutoff from Proposition 4.2.
Becausef q is convex, Jensen’s inequality implies
E[f q (epi(q))|m i, ei;q]≥f q (pi(q)).
This is the standard “value-of-information” [14]: before accounting for the cost of acquiring it, an
additional posterior refinement cannot lower the firm’s optimal expected continuation payoff.
17

The firm administers the intermediate assessment to applicantiwhenever the expected value
of the additional information is at least as large as the assessment cost:
E[f q (epi(q))|m i, ei;q]−f q (pi(q))≥c ℓ(q).
The next subsection specializes the assessment to a binary signal and characterizes the applicants
whose posterior compatibility lies below the one-stage hiring cutoff but for whom the firm would
strictly prefer to administer the assessment if the applicant were the firm’s only remaining option.
6.2 A Binary Assessment and Multistage Screening
To identify which below-cutoff applicants can benefit from the additional stage, for simplicity we
consider a binary intermediate assessment with outcome
Ai ∈ {H, L},
whereHis favorable andLis unfavorable.
For each experience groupe∈ {0,1}, assume
Pr(Ai =H|k i = 1, ei =e, mi;q) =τ e,
and
Pr(Ai =H|k i = 0, ei =e, mi;q) =ℓ e,
where
0≤ℓ e < τe ≤1.
Thus, conditional on experience and compatibility, application materials do not provide additional
information about the assessment outcome. The parametersτ e andℓ e may differ across experience
groups butτ e > ℓe requires that within each experience group, compatible applicants are more
likely to pass.
For an experience-eapplicant with pre-assessment posterior compatibilityp∈(0,1), Bayes’ rule
gives the posterior compatibility probability following a favorable outcome:
pe H (p) := τep τep+ℓ e(1−p) ,
and the posterior following an unfavorable outcome:
pe L(p) := (1−τ e)p (1−τ e)p+ (1−ℓ e)(1−p) .
Becauseτ e > ℓe,
pe H (p)> p > pe L(p).
We next consider the continuation problem in which the vacancy remains open and an applicant
is the firm’s only remaining option. Recall that the firm’s one-stage screening cutoff is
pF (q) = cs(q) vF .
For each experience groupe, define the intermediate-assessment cutoff
pA e (q) := cℓ(q)/vF +ℓ epF (q) τe  1−p F (q)  +ℓ epF (q) .(4)
18

Lemma 6.1(Binary intermediate-assessment cutoff).Fixqsuch thatp F (q)∈(0,1)and fix an
experience groupe∈ {0,1}. Consider an applicant with pre-assessment posteriorp < p F (q)who is
the firm’s only remaining option.
The firm weakly prefers to administer the intermediate assessment and proceed to full screening
only followingHif and only if
p≥p A e (q).
The preference is strict if the inequality above is strict.
This lemma suggests a simple continuation rule for screening: if the vacancy remains open and
a remaining applicant has posterior compatibility
p∈(p A e (q), pF (q)),
then the firm administers the intermediate assessment. After a favorable outcomeH, the applicant’s
posterior rises above the full-screening cutoff, so the firm proceeds to full screening. After an
unfavorable outcomeL, the applicant remains below the cutoff and is rejected.
This rule does not characterize the globally optimal order of assessment and screening when
multiple applicants remain. In that problem, the firm’s decision may depend on the continuation
values generated by its other options. Nevertheless, this rule is useful because it identifies a set of
below-cutoff applicants who are valuable whenever they become the only remaining option. It also
provides a feasible multistage policy that can be used to prove strict adoption of the multistage
technology.
Corollary 6.2(Strict ex ante value of multistage hiring).Supposeσ 2 m(q)>0and that, for some
e∈ {0,1},
λeαe(q)>0
and
cℓ(q)< vF pF (q)  1−p F (q)  (τe −ℓ e).
Then
E

U M S,∗(q)−U 1S,∗(q)  >0.
Consequently, the firm strictly prefers access to the multistage technology ex ante, and every ex
ante optimal multistage policy administers the intermediate assessment with positive probability.
To establish Corollary 6.2, observe that the condition onc ℓ(q) in the statement of the corollary
implies
pA e (q)< pF (q).
Because the Gaussian application signal has full support, conditional on experienceeand submis-
sion, posterior compatibility places positive probability on

pA e (q), pF (q)  .
Thus there is positive probability that the submitted pool contains an experience-eapplicant who
is rejected under one-stage hiring but is strictly worth assessing if reached.
A feasible multistage policy can first replicate the optimal one-stage policy. If no hire occurs
and such an applicant remains available, the firm can then administer the intermediate assessment.
This policy strictly improves the firm’s payoff on a positive-probability event. Since the globally
optimal multistage policy performs at least as well as this feasible policy, access to the intermediate
assessment has strictly positive ex ante value.
19

6.3 Implications for Screening Failure
Section 5.2 showed that applicants satisfying
pP (q)< pi(q)< pF (q)
are socially worth screening but are rejected under one-stage hiring. Lemma 6.1 shows that under
multistage hiring, an experience-eapplicant is strictly worth assessing when they are the firm’s
only remaining option whenever
pA e (q)< pi(q)< pF (q).
Thus, for applicants in experience groupe, multistage hiring creates a path to screening for those
satisfying
max
n
pP (q), pA e (q) o < pi(q)< pF (q).
In particular, if
pA e (q)≤p P (q),
then every experience-eapplicant who is strictly socially worth screening but rejected under one-
stage hiring is strictly worth assessing if they become the firm’s only remaining option.
Corollary 6.3(Multistage hiring mitigates one-stage screening failures).Fixqand a realized
submitted pool.
(i) Suppose the one-stage process exhibits the no-hire screening failure in Proposition 5.4. If there
exists a submitted applicantisuch that
max
n
pP (q), pA ei (q) o < pi(q)< pF (q),
then
U M S,∗(q)> U1S,∗(q) = 0.
Consequently, an optimal multistage policy administers the intermediate assessment with pos-
itive probability and proceeds to full screening with positive probability.
(ii) Suppose the one-stage process exhibits the inexperienced-compatible screening failure in Propo-
sition 5.5. If
pmax 01 (q)> pA 0 (q),
then there exists an applicanti∈ A 01(q)satisfying
pP (q)< pi(q)< pF (q)
and
pi(q)> pA 0 (q).
At any history at which the vacancy remains open and applicantiis the firm’s only remaining
option, an optimal multistage policy administers the intermediate assessment and proceeds to
full screening followingH.
20

The corollary above shows that multistage hiring can mitigate the market failures where no
applicants are screened or where no inexperienced-compatible applicants are screened.
For part (i), the firm can improve strictly on one-stage hiring by assessing the applicant identified
in the statement and otherwise terminating search. By Lemma 6.1, this feasible policy has strictly
positive expected payoff, whereas the optimal one-stage policy screens no one and receives zero.
Thus introducing the intermediate assessment restores screening that would otherwise not occur.
Part (ii) establishes a different form of mitigation. When an inexperienced-compatible applicant
lies above the assessment cutoff but below the firm’s one-stage screening cutoff, the applicant is
excluded under one-stage hiring but becomes worth assessing if reached while the vacancy remains
open. The intermediate assessment therefore creates a route to full screening that is absent under
the one-stage process. The next subsection shows that such a history occurs with positive ex ante
probability, implying a strictly positive gain in the applicant’s hiring probability.
6.4 Implications for Inexperienced-Compatible Applicants
We now quantify the benefit of multistage hiring for inexperienced-compatible applicants. These
applicants are high-fit matches, but they are precisely the group most exposed to the adverse effects
of AI on screening in one-stage hiring.
Leth 1S i denote the indicator that applicantiis hired under the one-stage technology, and let
hM S,∗ i denote the indicator that applicantiis hired under a globally optimal multistage policy.
Probabilities are evaluated ex ante over the other potential applicants, their application decisions,
the realized application pool, the firm’s screening and assessment decisions, and any intermediate-
assessment signals.
For a submitted inexperienced-compatible applicant with baseline posteriorp, define the hiring-
probability gain from optimal multistage hiring by
G∗ 01(p;q) := Pr  hM S,∗ i = 1|e i = 0, ki = 1, di = 1, pi =p 
−Pr

h1S i = 1|e i = 0, ki = 1, di = 1, pi =p  .
The key observation is that an inexperienced-compatible applicant satisfying
pA 0 (q)< pi(q)< pF (q)
has zero probability of being hired under one-stage hiring but has a strictly positive path to hiring
under an optimal multistage policy. In particular, if the vacancy remains open until the applicant
becomes the firm’s only remaining option, Lemma 6.1 implies that the firm strictly prefers to
administer the intermediate assessment. A favorable assessment then leads to full screening and,
because the applicant is compatible, to hiring. Proposition C.1 in Appendix C formalizes this
argument and gives an explicit positive lower bound on the applicant’s hiring-probability gain.
To measure how many inexperienced-compatible applicants fall into this region, define
ν01(q) := Pr

pA 0 (q)< pi(q)< pF (q)|e i = 0, ki = 1, di = 1  .
Thusν 01(q) is the share of submitted inexperienced-compatible applicants who are rejected under
one-stage hiring but have a strictly positive path to hiring under multistage hiring. Whenever
pA 0 (q)< pF (q),
21

the full support of the Gaussian materials signal implies
ν01(q)>0.
Moreover, every applicant in this region obtains a strictly positive hiring-probability gain under
optimal multistage hiring. Corollary C.2 in Appendix C states this finite-qresult formally.
We now turn to the main result of this subsection. In the high-AI limit, the share of inexperienced-
compatible applicants who benefit from multistage hiring can converge to one. Recall that
π0 = Pr(ki = 1|e i = 0) = Φ
 µ0
σz

is the inexperienced-group prior compatibility probability.
Corollary 6.4(Almost all inexperienced-compatible applicants benefit in the high-AI limit).Let
{qn}satisfy
σ2 m(qn)→ ∞
and
pF (qn)→p F ∞ ∈(0,1).
Suppose
lim sup
n→∞
pA 0 (qn)< π0 < pF ∞.
Then
ν01(qn)→1.
Consequently,
Pr (G∗ 01 (pi(qn);q n)>0|e i = 0, ki = 1, di = 1)→1.
As application materials become uninformative, the pre-assessment posterior of a submitted
inexperienced-compatible applicant converges toπ 0. Ifπ 0 remains strictly above the assessment
cutoff and strictly below the one-stage screening cutoff, almost every submitted inexperienced-
compatible applicant is rejected under one-stage hiring but obtains a strictly positive hiring-
probability gain under optimal multistage hiring. Thus the benefit of the additional screening
stage is not confined to an exceptional set of applicants: in the high-AI limit, it extends to almost
the entire inexperienced-compatible group.
When the high-noise screening-failure condition from Section 5.2 also holds, i.e.,
pP ∞ < π0 < pF ∞,
the intermediate stage benefits the same inexperienced-compatible applicants who are socially worth
screening but rejected under one-stage hiring.
7 Conclusion
AI-assisted job search changes the hiring market not only by affecting how many applications
workers submit, but also by changing what firms can infer from those applications. In our model,
less informative application materials lead firms to rely more heavily on applicants’ experience.
22

Inexperienced-compatible applicants are especially harmed as they lose the individualized evidence
that could distinguish them from others with little experience. Because firms do not internalize
workers’ surplus from a successful match, they may also reject applicants who are socially worth
screening. In very noisy, high-AI environments, these failures can become systematic: the firm may
screen no one or screen only experienced applicants.
Multistage hiring can mitigate this problem. A sufficiently informative and inexpensive inter-
mediate assessment allows firms to acquire new evidence of fit before committing to costly full
screening. We identify conditions under which this option strictly increases firm payoffs and gives
some inexperienced-compatible applicants rejected under one-stage hiring a positive-probability
path to employment. As AI saturation becomes sufficiently high, this benefit extends to almost all
such applicants. Expanding evaluation opportunities can therefore serve firms’ interests as well as
those of applicants otherwise excluded.
Our results highlight that easier access to applying is not the same as access to credible eval-
uation. Preserving access for high-potential workers without conventional experience therefore
requires attention to the design of screening and hiring processes. As application signals deterio-
rate, multistage hiring processes that create additional opportunities to demonstrate fit can help
restore market functioning by reopening evaluation and hiring opportunities that would otherwise
disappear.
References
[1] Danielle Abril. Employers to job seekers: Your AI r´ esum´ e isn’t fooling anyone.The Washing-
ton Post, February 2026. URLhttps://www.washingtonpost.com/technology/2026/02/
21/ai-resume-jobs/. Accessed June 14, 2026.
[2] Daron Acemoglu and Pascual Restrepo. The race between man and machine: Implications of
technology for growth, factor shares, and employment.American Economic Review, 108(6):
1488–1542, 2018. doi: 10.1257/aer.20160696.
[3] Daron Acemoglu and Pascual Restrepo. Robots and jobs: Evidence from US labor markets.
Journal of Political Economy, 128(6):2188–2244, 2020. doi: 10.1086/705716.
[4] Dennis J. Aigner and Glen G. Cain. Statistical theories of discrimination in labor markets.In-
dustrial and Labor Relations Review, 30(2):175–187, 1977. doi: 10.1177/001979397703000204.
[5] James Albrecht, Pieter A. Gautier, and Susan Vroman. Equilibrium directed search with
multiple applications.The Review of Economic Studies, 73(4):869–891, 2006. doi: 10.1111/j.
1467-937X.2006.00400.x.
[6] Joseph G. Altonji and Charles R. Pierret. Employer learning and statistical discrimination.
The Quarterly Journal of Economics, 116(1):313–350, 2001. doi: 10.1162/003355301556329.
[7] Ali Aouad, Jingwei Ji, and Yaron Shaposhnik. The Pandora’s Box problem with sequential
inspections.Operations Research, 2026. doi: 10.1287/opre.2024.0733. URLhttps://doi.org/
10.1287/opre.2024.0733. Articles in Advance; earlier version available as SSRN 3726167.
23

[8] Nick Arnosti, Ramesh Johari, and Yash Kanoria. Managing congestion in matching markets.
Manufacturing & Service Operations Management, 23(3):620–636, 2021. doi: 10.1287/msom.
2020.0927.
[9] Kenneth J. Arrow. The theory of discrimination. In Orley Ashenfelter and Albert Rees,
editors,Discrimination in Labor Markets, pages 3–33. Princeton University Press, Princeton,
NJ, 1973.
[10] Elliott Ash, Soumitra Shukla, and Jason Sockin. Interviews. Working Paper 12229, CESifo,
2025. URLhttps://papers.ssrn.com/sol3/papers.cfm?abstract_id=5684489.
[11] David H. Autor. Why are there still so many jobs? the history and future of workplace
automation.Journal of Economic Perspectives, 29(3):3–30, 2015. doi: 10.1257/jep.29.3.3.
[12] David H. Autor, Frank Levy, and Richard J. Murnane. The skill content of recent technological
change: An empirical exploration.The Quarterly Journal of Economics, 118(4):1279–1333,
2003. doi: 10.1162/003355303322552801.
[13] Jackie Baek and Ali Makhdoumi. The feedback loop of statistical discrimination, 2025.
URLhttps://papers.ssrn.com/sol3/papers.cfm?abstract_id=4658797. Working paper;
SSRN version last revised June 5, 2025.
[14] David Blackwell. Equivalent comparisons of experiments.The Annals of Mathematical Statis-
tics, 24(2):265–272, 1953. doi: 10.1214/aoms/1177729032.
[15] Erik Brynjolfsson, Danielle Li, and Lindsey R. Raymond. Generative AI at work.The Quarterly
Journal of Economics, 140(2):889–942, 2025. doi: 10.1093/qje/qjae044.
[16] Kenneth Burdett, Shouyong Shi, and Randall Wright. Pricing and matching with frictions.
Journal of Political Economy, 109(5):1060–1085, 2001. doi: 10.1086/322835.
[17] Tomas Chamorro-Premuzic. AI has made hiring worse—but it can still help.
Harvard Business Review, January 2026. URLhttps://hbr.org/2026/01/
ai-has-made-hiring-worse-but-it-can-still-help. Accessed June 14, 2026.
[18] Stephen Coate and Glenn C. Loury. Will affirmative-action policies eliminate negative stereo-
types?The American Economic Review, 83(5):1220–1240, 1993.
[19] Tor Constantino. Why AI is a double-edged sword for 2025 job seekers—new research.
Forbes, March 2025. URLhttps://www.forbes.com/sites/torconstantino/2025/03/11/
why-ai-is-a-double-edged-sword-for-2025-job-seekers---new-research/. Accessed
June 14, 2026.
[20] Bo Cowgill, Pablo Hern´ andez-Lagos, and Nataliya Langburd Wright. Does AI cheapen talk?
theory and evidence from global entrepreneurship and hiring.Management Science, 2026. doi:
10.1287/mnsc.2024.07027. URLhttps://doi.org/10.1287/mnsc.2024.07027. Articles in
Advance.
[21] Vincent P. Crawford and Joel Sobel. Strategic information transmission.Econometrica, 50(6):
1431–1451, 1982. doi: 10.2307/1913390.
24

[22] Jingyi Cui, Gabriel Dias, and Justin Ye. Signaling in the age of AI: Evidence from cover
letters, 2025. URLhttps://arxiv.org/abs/2509.25054.
[23] Steven J. Davis and Brenda Samaniego de la Parra. Application flows. Working Paper 32320,
National Bureau of Economic Research, 2024. URLhttps://www.nber.org/papers/w32320.
[24] Joseph Farrell and Matthew Rabin. Cheap talk.Journal of Economic Perspectives, 10(3):
103–118, 1996. doi: 10.1257/jep.10.3.103.
[25] Federal Reserve Bank of New York. The labor market for recent college graduates. Research
data feature, 2026. URLhttps://www.newyorkfed.org/research/college-labor-market.
Accessed June 14, 2026.
[26] Edward W. Felten, Manav Raj, and Robert Seamans. Occupational, industry, and geographic
exposure to artificial intelligence: A novel dataset and its potential uses.Strategic Management
Journal, 42(12):2195–2217, 2021. doi: 10.1002/smj.3286.
[27] Andrey Fradkin, Monica Bhole, and John J. Horton. Competition avoidance versus herding in
job search: Evidence from large-scale field experiments on an online job board.Management
Science, 72(2):1305–1323, 2026. doi: 10.1287/mnsc.2023.02483. Published online June 4, 2025.
[28] Ana”is Galdin and Jesse Silbert. Making talk cheap: Generative AI and labor market signaling,
2025. URLhttps://arxiv.org/abs/2511.08785.
[29] Manolis Galenianos and Philipp Kircher. Directed search with multiple job applications.Jour-
nal of Economic Theory, 144(2):445–471, 2009. doi: 10.1016/j.jet.2008.06.007.
[30] John J. Horton and Shoshana Vasserman. Job-seekers send too many applications: Experi-
mental evidence and a partial solution. Working paper; superseded by Horton, Vasserman,
and Watt (2024), 2021. URLhttps://john-joseph-horton.com/papers/autopause.pdf.
[31] John J. Horton, Shoshana Vasserman, and Mitchell Watt. Reducing congestion in labor mar-
kets: A case study in simple market design. Working paper; revise and resubmit, American
Economic Journal: Microeconomics, 2024. URLhttps://john-joseph-horton.com/.
[32] Lily Hu and Yiling Chen. A short-term intervention for long-term fairness in the labor market.
InProceedings of the 2018 World Wide Web Conference, WWW ’18, pages 1389–1398, Repub-
lic and Canton of Geneva, CHE, 2018. International World Wide Web Conferences Steering
Committee. doi: 10.1145/3178876.3186044.
[33] Brian Jabarian and P¨ ellumb Reshidi. Choice as signal: Designing ai adoption in labor market
screening. Working paper, 2025.
[34] Jens Josephson and Joel D. Shapiro. Costly interviews.International Journal of Industrial
Organization, 45:10–15, 2016. doi: 10.1016/j.ijindorg.2015.12.001.
[35] Thomas Jungbauer. Better applications, worse matching: Artificial intelligence and talent
allocation. Working paper, 2026.
[36] Deborah Kearns. AI was supposed to fix the job search. it’s breaking it instead.Quartz,
November 2025. URLhttps://qz.com/ai-job-searches-careers. Accessed June 14, 2026.
25

[37] Rebecca Lessem and Robert A. Miller. Matching job applicants to vacancies: An em-
pirical model of multistage hiring. Working paper, March 18, 2026, 2026. URLhttps:
//www.comlabgames.com/ramiller/working_papers/interviews_and_hiring.pdf.
[38] Danielle Li, Lindsey Raymond, and Peter Bergman. Hiring as exploration.The Review of
Economic Studies, 93(2):1200–1240, 2026. doi: 10.1093/restud/rdaf040.
[39] John J. McCall. Economics of information and job search.The Quarterly Journal of Eco-
nomics, 84(1):113–126, 1970. doi: 10.2307/1879403.
[40] Espen R. Moen. Competitive search equilibrium.Journal of Political Economy, 105(2):385–
411, 1997. doi: 10.1086/262077.
[41] Andrea Moro and Peter Norman. A general equilibrium model of statistical discrimination.
Journal of Economic Theory, 114(1):1–30, January 2004. doi: 10.1016/S0022-0531(03)00100-6.
[42] Amanda Pallais. Inefficient hiring in entry-level labor markets.The American Economic
Review, 104(11):3565–3599, 2014. doi: 10.1257/aer.104.11.3565.
[43] Michael Peters. Ex ante price offers in matching games: Non-steady states.Econometrica, 59
(5):1425–1454, 1991. doi: 10.2307/2938374.
[44] Edmund S. Phelps. The statistical theory of racism and sexism.The American Economic
Review, 62(4):659–661, 1972.
[45] Robert Half. Robert half survey: 67% of HR leaders report AI-generated applications
are slowing hiring. Press release, March 2026. URLhttps://press.roberthalf.com/
2026-03-10-Robert-Half-survey-67-of-HR-leaders-report-AI-generated-applications-are-slowing-hiring.
Accessed June 14, 2026.
[46] Ricardo Rodriguez. AI and the job search: How candidates are using tech to gain an edge. Soft-
ware Finder Resource Center, June 2026. URLhttps://softwarefinder.com/resources/
ai-and-the-job-search. Accessed June 14, 2026.
[47] Michael Spence. Job market signaling.The Quarterly Journal of Economics, 87(3):355–374,
1973. doi: 10.2307/1882010.
[48] Christopher T. Stanton and Catherine Thomas. Landing the first job: The value of in-
termediaries in online hiring.The Review of Economic Studies, 83(2):810–854, 2016. doi:
10.1093/restud/rdv042.
[49] Joseph E. Stiglitz. The theory of “screening,” education, and the distribution of income.The
American Economic Review, 65(3):283–300, 1975.
[50] Marko Tervi¨ o. Superstars and mediocrities: Market failure in the discovery of talent.The
Review of Economic Studies, 76(2):829–850, 2009. doi: 10.1111/j.1467-937X.2008.00522.x.
[51] Michael Webb. The impact of artificial intelligence on the labor market. SSRN Working Paper,
2020. URLhttps://ssrn.com/abstract=3482150.
26

[52] Martin L. Weitzman. Optimal search for the best alternative.Econometrica, 47(3):641–654,
1979. doi: 10.2307/1910412.
[53] Randall Wright, Philipp Kircher, Benoit Julien, and Veronica Guerrieri. Directed search and
competitive search equilibrium: A guided tour.Journal of Economic Literature, 59(1):90–148,
2021. doi: 10.1257/jel.20191505.
A Proofs for Section 4
Proof of Proposition 4.1.Fixqand a submitted applicantiwith experiencee i =e. Because the
application decision depends on (e i, ηi) andη i is independent of (z i, εi) conditional on experience,
application is uninformative about match quality and the materials signal conditional on experience.
Thus,
zi |m i, ei =e, di = 1;q d=z i |m i, ei =e;q.
Under (1) and (2), standard Gaussian updating gives
zi |m i, ei =e;q∼ N

Si(q), σ2 post(q)  ,
where
σ2 post(q) =
 1
σ2z + 1 σ2m(q) −1 = σ2 z σ2 m(q) σ2z +σ 2m(q)
and
Si(q) =σ 2 post(q)
 µe
σ2z + mi σ2m(q) 
=κ(q)m i + (1−κ(q))µ e,
with
κ(q) = σ2 z
σ2z +σ 2m(q) .
Let
∆µ :=µ 1 −µ 0 >0.
Since
µe =µ 0 + ∆µe,
the posterior mean can equivalently be written as
Si(q) = (1−κ(q))µ 0 +θ(q)e i +κ(q)m i,
where
θ(q) = (1−κ(q))∆ µ.
Compatibility is the eventk i = 1 if and only ifz i ≥0. Therefore,
pi(q) = Pr(ki = 1|m i, ei;q)
= Pr(zi ≥0|m i, ei;q)
= Φ
 Si(q)
σpost(q)

.
27

Becauseσ post(q)>0 and Φ is strictly increasing, for any submitted applicantsiandj,
pi(q)≥p j(q)⇐ ⇒S i(q)≥S j(q).
Now considereq > q. By Assumption 3.1,
σ2 m(eq)> σ2 m(q).
It follows immediately that
κ(eq) = σ2 z
σ2z +σ 2m(eq)< σ2 z σ2z +σ 2m(q) =κ(q).
Since ∆µ >0,
θ(eq) = (1−κ(eq))∆µ >(1−κ(q))∆ µ =θ(q).
Finally,
θ(q)
κ(q) = ∆µ
1−κ(q)
κ(q)
= ∆µ σ2 m(q) σ2z .
Assumption 3.1 therefore implies thatθ(q)/κ(q) is strictly increasing inq.
Proof of Proposition 4.2.Fixqand a realized pool ofMsubmitted applications. Write
V:=v F andc:=c s(q).
By assumption,V >0. Conditional on the observed application information, applicantiis com-
patible with probabilityp i(q). Because applicant primitives are independent across applicants,
compatibility realizations are independent conditional on the firm’s observed information.
We first establish the optimal ordering. Consider two applicantsiandjwho are screened con-
secutively, conditional on the vacancy remaining open when the firm reaches them. The probability
that at least one of the two applicants is compatible, and the probability that both applicants are
incompatible, do not depend on their order. Thus the expected hiring payoff and the continuation
value after both applicants fail are the same under either order.
If the firm screensibeforej, its expected screening cost over these two applicants is
c+ (1−p i(q))c.
If it screensjbeforei, the corresponding expected cost is
c+ (1−p j(q))c.
Hence the expected-payoff difference between placingibeforejand placingjbeforeiis
c

pi(q)−p j(q)

.
Therefore,
pi(q)≥p j(q)
28

implies that placingiweakly beforejis optimal. Repeated pairwise interchanges imply that
applicants can be ordered so that
p1(q)≥p 2(q)≥ · · · ≥pM (q).
Now suppose the firm screens the firstLapplicants in this order, unless it discovers a compatible
applicant earlier. Its expected payoff is
UL(q) =V

1−
LY
j=1
(1−p j(q))

 −c
LX
ℓ=1
ℓ−1Y
j=1
(1−p j(q)),
where the empty product is equal to one. The first term is the firm’s expected hiring payoff, and
the second is its expected total screening cost.
The marginal payoff from adding applicantLto the end of the screening list is
UL(q)−U L−1(q) =
L−1Y
j=1
(1−p j(q)) [V pL(q)−c].
The product preceding the bracket is the probability that applicantLis reached. It is nonnegative.
Thus applicantLis weakly worth including if and only if
V pL(q)≥c.
SubstitutingV=v F andc=c s(q) gives
pL(q)≥ cs(q) vF =p F (q).
Because applicants are ordered by decreasing posterior compatibility, once an applicant fails
this inequality, every remaining applicant also fails it. Hence the firm optimally screens applicants
sequentially in decreasing order of posterior compatibility until either it finds a compatible applicant
or no remaining applicant satisfies
pi(q)≥p F (q).
At equality the firm is indifferent; the proposition adopts the tie-breaking convention that an
indifferent applicant is included in the screening list.
Finally, under Assumption 3.2, for everyeq > q,
cs(eq)> cs(q).
Sincev F >0,
pF (eq) =cs(eq) vF > cs(q) vF =p F (q).
29

B Proofs for Section 5
Proof of Proposition 5.1.Because applicants do not observez i before applying and application
costs are independent of (z i, εi) conditional on experience, conditioning on submission does not
change the distribution of (z i, mi) within an experience group. Hence
E[mi |e i =e, ki =k, di = 1] =E[z i |e i =e, ki =k] =µ ek,
where we useE[ε i] = 0. Therefore,
¯Sek(q) =κ(q)µ ek + (1−κ(q))µ e.
Forq <eq,
∆ ¯Sek(q,eq) = ¯Sek(eq)−¯Sek(q)
= [κ(eq)−κ(q)] (µek −µ e).
It remains to establish the ordering of these changes. Define
te := µe σz .
Sincez i |e i =e∼ N(µe, σ2 z ) and compatibility is the eventz i ≥0, the conditional means are
µe1 =µ e +σ z
ϕ(te)
Φ(te)
and
µe0 =µ e −σ z
ϕ(te)
Φ(−te) .
Thus
µe1 −µ e =σ z
ϕ(te)
Φ(te) >0
and
µe0 −µ e =−σ z
ϕ(te)
Φ(−te) <0.
The inverse Mills ratio
ϕ(t)
Φ(t)
is strictly decreasing int, while
ϕ(t)
Φ(−t)
is strictly increasing int. Sinceµ 1 > µ0, we havet 1 > t0 and therefore
µ01 −µ 0 > µ11 −µ 1 >0,
while
µ10 −µ 1 < µ00 −µ 0 <0.
30

By Assumption 3.1,
κ(eq)−κ(q)<0.
Multiplying the preceding inequalities by this negative quantity gives
∆ ¯S01(q,eq)<∆ ¯S11(q,eq)<0<∆ ¯S00(q,eq)<∆ ¯S10(q,eq),
as required.
Proof of Proposition 5.2.Fix an experience groupe. Recall that
Xi = zi −µ e σz , Y i(q) = mi −µ ep σ2z +σ 2m(q) .
Conditional one i =e, (X i, Yi(q)) is standard bivariate normal with correlation
r(q) = σzp
σ2z +σ 2m(q) .
Fora, b∈Randr∈(−1,1), let
Φ2(a, b;r) = Pr(X≤a, Y≤b)
denote the standard bivariate normal CDF, and letϕ 2(a, b;r) denote its density. The standard
derivative identity
∂
∂r Φ2(a, b;r) =ϕ2(a, b;r)>0
implies
∂
∂r Pr(X≥a e, Y≥b) =ϕ 2(ae, b;r)>0.
Since Pr(X≥a e) does not depend onr,
∂ψe1(b, r)
∂r = ϕ2(ae, b;r) Pr(X≥a e) >0.
Similarly,
Pr(X < ae, Y≥b) = Pr(Y≥b)−Pr(X≥a e, Y≥b).
The first term is independent ofr, so
∂ψe0(b, r)
∂r =− ϕ2(ae, b;r) Pr(X < ae) <0.
We next derive the relative standardized thresholds. By the definition ofY i(q),
mi =µ e +
p
σ2z +σ 2m(q)Y i(q).
Because
κ(q) = σ2 z
σ2z +σ 2m(q)
31

and
r(q) = σzp
σ2z +σ 2m(q) ,
the posterior-mean score can be written as
Si(q) =µ e +σ zr(q)Yi(q).
The screening condition
pi(q)≥p F (q)
is equivalent to
Si(q)≥σ post(q)Φ−1  pF (q)  .
Therefore it is equivalent to
Yi(q)≥b e(q),
where
be(q) = σpost(q)Φ−1  pF (q)  −µ e σzr(q) .
The term involving the posterior cutoff is common across experience groups, so
b0(q)−b 1(q) = µ1 −µ 0 σzr(q) = ∆µ σzr(q) .
Differentiating gives
d
dq [b0(q)−b 1(q)] =− ∆µr′(q) σzr(q)2 .
Assumption 3.1 impliesr ′(q)<0, and ∆ µ >0, so
d
dq [b0(q)−b 1(q)]>0.
Proof of Proposition 5.3.At the screening stage, application costs are sunk. A compatible hire
generates total surplus
vF +v A.
Thus the planner’s screening problem has exactly the same structure as the firm’s problem in
Proposition 4.2, except that the value of discovering a compatible applicant isv F +v A rather than
vF .
The same pairwise-interchange argument therefore implies that the planner screens applicants
in decreasing order of posterior compatibility. Conditional on reaching applicanti, the expected
marginal social value of screening is
(vF +v A)pi(q)−c s(q).
Hence the planner screens applicantiif and only if
pi(q)≥ cs(q) vF +v A =p P (q).
32

Becausev A >0,
pP (q) = cs(q) vF +v A < cs(q) vF =p F (q).
Thus an applicant is included in the planner’s screening list but not the firm’s if and only if
pP (q)≤p i(q)< pF (q).
Proof of Proposition 5.4.Suppose
pP (q)< pmax(q)< pF (q).
Since every submitted applicant satisfies
pi(q)≤p max(q)< pF (q),
Proposition 4.2 implies that the firm’s screening list is empty.
On the other hand, an applicant attainingp max(q) satisfies
pmax(q)> pP (q).
By Proposition 5.3, the social planner includes this applicant in its screening list. Hence the
planner’s screening list is nonempty while the firm’s is empty.
Proof of Proposition 5.5.Suppose
pP (q)< pmax 01 (q)< pF (q).
Every submitted inexperienced-compatible applicant satisfies
pi(q)≤p max 01 (q)< pF (q),
so none is included in the firm’s screening list.
An applicant attainingp max 01 (q) satisfies
pmax 01 (q)> pP (q),
so Proposition 5.3 implies that this applicant is included in the planner’s screening list. Hence at
least one submitted inexperienced-compatible applicant is socially worth screening but excluded by
the firm.
Proof of Lemma 5.6.Fix an applicant with experiencee i =eand realized compatibilityk i =k.
Recall that
Si(q) =κ(q)m i + (1−κ(q))µ e =µ e +κ(q)(z i −µ e) +κ(q)ε i.
Along a sequenceq n such that
σ2 m(qn)→ ∞,
we have
κ(qn) = σ2 z σ2z +σ 2m(qn) →0.
33

Conditional on (e i =e, ki =k),z i has a truncated normal distribution and therefore has finite
second moment. Hence
κ(qn)(zi −µ e)→0
in probability.
Also,
Var (κ(qn)εi) =κ(q n)2σ2 m(qn) = σ4 z σ2 m(qn) (σ2z +σ 2m(qn))2 →0.
Therefore,
κ(qn)εi →0
in probability, and consequently
Si(qn)→µ e
in probability conditional on (e i =e, ki =k).
Moreover,
σ2 post(qn) = σ2 z σ2 m(qn) σ2z +σ 2m(qn) →σ 2 z .
Since
pi(qn) = Φ
 Si(qn)
σpost(qn)

,
the continuous mapping theorem gives
pi(qn)→Φ
 µe
σz

=π e
in probability.
Application is independent of (z i, mi) conditional on experience, so the same convergence holds
conditional ond i = 1.
For any fixed finite submitted poolB,
max
i∈B
|pi(qn)−π ei| →0
in probability by a union bound over the finitely many applicants.
Proof of Corollary 5.7.By Lemma 5.6, conditional on the realized types in the fixed finite submit-
ted poolB,
max
i∈B
|pi(qn)−π ei| →0
in probability.
For part (i), it follows that
max
i∈B
pi(qn)→π max B
in probability. By assumption,
pP ∞ < πmax B < pF ∞,
while
pP (qn)→p P ∞, p F (qn)→p F ∞.
34

The strict inequalities therefore imply
Pr

pP (qn)<max i∈B pi(qn)< pF (qn)

→1.
Proposition 5.4 then gives the no-hire screening failure with probability approaching one.
For part (ii), every applicant inB 01 has experiencee= 0. Hence
max
i∈B01
|pi(qn)−π 0| →0
in probability. If
pP ∞ < π0 < pF ∞,
then
Pr

pP (qn)<min i∈B01 pi(qn)≤max i∈B01 pi(qn)< pF (qn)

→1.
Thus every submitted inexperienced-compatible applicant lies below the firm’s cutoff and above
the planner’s cutoff with probability approaching one.
Finally, ifB 1 is nonempty and
pF ∞ < π1,
then
min
i∈B1
pi(qn)→π 1
in probability. Combining this convergence with
max
i∈B01
pi(qn)→π 0
and
π0 < pF ∞ < π1
gives
Pr

min
i∈B1
pi(qn)> pF (qn)>max i∈B01 pi(qn)

→1.
C Proofs and Supporting Results for Section 6
Proof of Lemma 6.1.Fixq, experience groupe, and a pre-assessment posterior
p < pF (q).
Write
V:=v F , p F (q) = cs(q) V .
The probability of a favorable assessment outcome is
Pr(Ai =H|p, e) =τ ep+ℓ e(1−p).
35

Bayes’ rule gives
pe H (p) = τep τep+ℓ e(1−p)
and
pe L(p) = (1−τ e)p (1−τ e)p+ (1−ℓ e)(1−p) .
Becauseτ e > ℓe,
pe H (p)> p > pe L(p).
Sincep < pF (q), it follows immediately that
pe L(p)< pF (q),
so the firm never proceeds to full screening followingLin the one-applicant continuation problem.
Consider the policy that administers the intermediate assessment and proceeds to full screening
only followingH. Its expected payoff is
−c ℓ(q) + Pr(Ai =H|p, e) [V pe H (p)−c s(q)]
=−c ℓ(q) + [τep+ℓ e(1−p)]

V τep τep+ℓ e(1−p) −c s(q) 
=−c ℓ(q) +V τep−c s(q) [τep+ℓ e(1−p)].
Substituting
cs(q) =V pF (q)
gives
−cℓ(q) +V
h
p

τe(1−p F (q)) +ℓ epF (q)  −ℓ epF (q) i .
This payoff is nonnegative if and only if
p≥ cℓ(q)/V+ℓ epF (q) τe(1−p F (q)) +ℓ epF (q) =p A e (q).
It is strictly positive if and only if
p > pA e (q).
For anyp≥p A e (q), the preceding inequality also implies that a favorable assessment raises
the posterior above the full-screening cutoff, so screening followingHis optimal. Thus, among
applicants satisfyingp < pF (q), the firm weakly prefers assessment if and only if
p≥p A e (q),
with strict preference when
pA e (q)< p < pF (q).
Finally, there exist below-cutoff applicants for whom assessment is strictly preferred if and only
if
pA e (q)< pF (q).
36

Substituting the definition ofp A e (q) and rearranging,
pA e (q)< pF (q)⇐ ⇒ cℓ(q) V < pF (q)(1−p F (q))(τe −ℓ e).
Multiplying byV=v F gives
cℓ(q)< vF pF (q)(1−p F (q))(τe −ℓ e),
as required.
Proof of Corollary 6.2.Suppose that for some experience groupe,
λeαe(q)>0
and
cℓ(q)< vF pF (q)(1−p F (q))(τe −ℓ e).
By Lemma 6.1,
pA e (q)< pF (q).
Conditional one i =eandd i = 1, the application-materials signal has full support onR.
Moreover, posterior compatibility
pi(q) = Pr(ki = 1|m i, ei =e;q)
is continuous and strictly increasing inm i, with limits zero and one asm i → −∞andm i → ∞,
respectively. Hence
Pr

pA e (q)< pi(q)< pF (q)|e i =e, di = 1  >0.
Becauseλ eαe(q)>0, there is positive probability that the submitted pool contains such an
applicant. Consider a feasible multistage policy that first replicates the optimal one-stage policy.
If the vacancy remains open after the one-stage screening list is exhausted, the policy administers
the intermediate assessment to one such below-cutoff applicant.
Conditional on reaching this applicant, Lemma 6.1 implies that the assessment has strictly
positive expected value. There is positive probability that the vacancy remains open until this
point; for example, the event that all other potential applicants are incompatible has strictly
positive probability. Therefore this feasible policy weakly improves on the optimal one-stage policy
at every history and strictly improves on it with positive probability.
It follows that
E

U M S,∗(q)−U 1S,∗(q)  >0.
If an ex ante optimal multistage policy never administered the intermediate assessment, it would
be a feasible one-stage policy and could achieve at most the one-stage value. Hence every ex ante
optimal multistage policy must administer the intermediate assessment with positive probability.
Proof of Corollary 6.3.For part (i), suppose the one-stage process exhibits the no-hire screening
failure. Then every submitted applicant satisfies
pi(q)< pF (q),
37

and the optimal one-stage payoff is
U 1S,∗(q) = 0.
Suppose there exists a submitted applicantisatisfying
max
n
pP (q), pA ei (q) o < pi(q)< pF (q).
The firm can ignore all other applicants and treatias its only remaining option. By Lemma 6.1,
administering the intermediate assessment then has strictly positive expected payoff. Hence there
exists a feasible multistage policy with strictly positive payoff, so
U M S,∗(q)>0 =U 1S,∗(q).
Any optimal multistage policy must therefore administer an intermediate assessment with posi-
tive probability. Because a favorable assessment outcome has positive probability and raises the
posterior abovep F (q), the firm also proceeds to full screening with positive probability.
For part (ii), suppose the one-stage process exhibits the inexperienced-compatible screening
failure and
pmax 01 (q)> pA 0 (q).
Choose an applicanti∈ A01(q) attainingp max 01 (q). By the definition of the one-stage failure,
pP (q)< pi(q)< pF (q).
Together with the assumed inequality,
pA 0 (q)< pi(q)< pF (q).
At any history at which the vacancy remains open andiis the firm’s only remaining option, Lemma
6.1 implies that the firm strictly prefers to administer the intermediate assessment. FollowingH,
the posterior exceedsp F (q) and the firm proceeds to full screening.
Proposition C.1(Hiring gain for below-cutoff inexperienced-compatible applicants).Fixqand
suppose
pA 0 (q)< p < pF (q).
Then
Pr

hM S,∗ i = 1|e i = 0, ki = 1, di = 1, pi(q) =p  ≥τ 0χn−1,
where
χ:= Pr(k i = 0) =
X
e∈{0,1}
λeΦ

− µe
σz

>0.
By contrast,
Pr

h1S i = 1|e i = 0, ki = 1, di = 1, pi(q) =p  = 0.
Consequently,
G∗ 01(p;q)≥τ 0χn−1 >0.
38

Proof.Fix a submitted inexperienced-compatible applicantisatisfying
pA 0 (q)< pi(q)< pF (q).
Under one-stage hiring, Proposition 4.2 implies thatiis not included in the firm’s screening list.
Hence
Pr

h1S i = 1|e i = 0, ki = 1, di = 1, pi(q)  = 0.
Now consider the multistage process. Let
E−i :={k j = 0 for everyj̸=i}
be the event that all othern−1 potential applicants are incompatible. Applicant primitives are
independent across applicants, so conditional on the tagged applicant’s type, submission decision,
and posterior,
Pr(E−i) =χ n−1.
OnE −i, no other applicant can fill the vacancy. Because retaining an unassessed application is
costless, applicantican remain available while the firm evaluates its other options. If the vacancy
remains open untiliis the firm’s only remaining option, Lemma 6.1 implies that administering
the intermediate assessment has strictly positive value. Thus an optimal multistage policy cannot
terminate search whileiremains available.
Conditional onk i = 1, applicantireceives a favorable intermediate assessment with probability
τ0.
FollowingH, the applicant’s posterior exceedsp F (q), so full screening is strictly profitable. Screen-
ing reveals thatk i = 1, and the firm hires the applicant. Therefore,
Pr

hM S,∗ i = 1|e i = 0, ki = 1, di = 1, pi(q)  ≥τ 0χn−1.
Subtracting the zero one-stage hiring probability gives
G∗ 01(pi(q);q)≥τ 0χn−1 >0.
Corollary C.2(Positive share of inexperienced-compatible applicants helped).Supposeσ 2 m(q)>0
and
pA 0 (q)< pF (q).
Then
ν01(q)>0.
Moreover,
Pr (G∗ 01(pi(q);q)>0|e i = 0, ki = 1, di = 1)≥ν 01(q)>0.
39

Proof.Suppose
σ2 m(q)>0
and
pA 0 (q)< pF (q).
Conditional on
ei = 0, k i = 1, d i = 1,
the materials signalm i has a continuous density that is strictly positive onR. Moreover,
pi(q) = Pr(ki = 1|m i, ei = 0;q)
is a continuous and strictly increasing function ofmi whose range is (0,1). Therefore the conditional
distribution ofp i(q) places positive probability on every open subinterval of (0,1).
In particular,
ν01(q) = Pr

pA 0 (q)< pi(q)< pF (q)|e i = 0, ki = 1, di = 1  >0.
For every posterior in this interval, Proposition C.1 implies
G∗ 01(pi(q);q)>0.
Hence
Pr (G∗ 01(pi(q);q)>0|e i = 0, ki = 1, di = 1)≥ν 01(q)>0.
Proof of Corollary 6.4.By Lemma 5.6, conditional on
ei = 0, k i = 1, d i = 1,
we have
pi(qn)→π 0
in probability.
By assumption,
lim sup
n→∞
pA 0 (qn)< π0 < pF ∞,
and
pF (qn)→p F ∞.
Therefore there existsε >0 such that for all sufficiently largen,
pA 0 (qn)< π0 −ε < π0 +ε < pF (qn).
Consequently,
ν01(qn) = Pr

pA 0 (qn)< pi(qn)< pF (qn)|e i = 0, ki = 1, di = 1 
≥Pr (|p i(qn)−π 0|< ε|e i = 0, ki = 1, di = 1)→1.
40

Thus
ν01(qn)→1.
Finally, Proposition C.1 implies
G∗ 01(pi(qn);q n)>0
whenever
pA 0 (qn)< pi(qn)< pF (qn).
Therefore,
Pr (G∗ 01(pi(qn);q n)>0|e i = 0, ki = 1, di = 1)≥ν 01(qn)→1.
41
