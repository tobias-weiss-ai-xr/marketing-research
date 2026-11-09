---
title: 'Toward User-Centered Agentic Recommendation: When Does Platform Competition Benefit Users?'
url: https://arxiv.org/abs/2611.04203
category: ai-marketing
subcategory: framework
date: 2026-11
venue: ''
authors:
- Kehan Zheng
- Deyao Hong
- Qian Li
- Jun Zhang
- Jie Jiang
source: arxiv
pdf_url: https://arxiv.org/pdf/2611.04203
pages: 37
chars: 92249
fetched_at: '2026-11-08T13:36:39+00:00'
kb_version: 1
---

# Toward User-Centered Agentic Recommendation: When Does Platform Competition Benefit Users?

Proceedings of Machine Learning Research 1–37
Toward User-Centered Agentic Recommendation: When Does
Platform Competition Benefit Users?
Kehan Zheng1∗, Deyao Hong1∗, Qian Li2
Jun Zhang2, Jie Jiang2, Hongning Wang1†
1Tsinghua University 2Tencent Inc.
zhengkh24@mails.tsinghua.edu.cn,hongdy22@mails.tsinghua.edu.cn,
hw-ai@tsinghua.edu.cn
Abstract
Conventional recommender systems operate within platform-specific catalogs, limiting
access to potentially valuable resources across platforms. We propose user-centered agentic
recommendation, aparadigminwhichuseragentscomparerecommendationsfromcompeting
platform agents, and formalize their interaction as a repeated game. Platforms strategically
modify descriptions without changing intrinsic item value, while each user agent assesses
platform credibility using feedback from consumed items only. Our analysis shows that
expanded resource access need not improve user welfare: strategic misrepresentation and
limited verification can offset the benefits of platform competition. We quantify when
platform credibility assessment allows users to benefit from broader access despite strategic
exaggeration. Our analysis identifies resource and reporting conditions that guarantee higher
average welfare than the original platform with an interaction budget linear in platform
count. Experiments on synthetic and Amazon-grounded markets show that credibility
assessment can improve finite-horizon utility, while its benefits depend on market size and
mechanism parameters.
Keywords:User-centered agentic recommendation, recommender system, welfare analysis,
game theory
1. Introduction
Most recommender systems organize choice within a platform: they learn from user interac-
tions, rank items in their own catalogs, and collect feedback on the resulting recommendations.
Finding alternatives across platforms remains the user’s responsibility. Advances in large
language models (LLMs) and agents suggest a different organization. Recommendation
agents combine planning and tool use (Wang et al., 2024), and can interpret personal informa-
tion need and mediate interactions with recommenders (Xu et al., 2025), motivating recent
proposals for user-centered services and personalization beyond platform boundaries (Zhang
et al., 2026; Lin et al., 2026).
In this work, we proposeuser-centered agentic recommendation: a personal user agent
solicits recommendations from multiple platform agents to find the most relevant resource
on the user’s behalf. Each platform retains its private catalog and responds independently.
The user agent brings these responses together at the point of choice, without requiring
competitors to share catalogs or a central service to control their resources. Recommendation
∗ Equal contribution.
† Corresponding author.
©K. Zheng, D. Hong, Q. Li, J. Zhang, J. Jiang & H. Wang.
arXiv:2611.04203v1  [cs.AI]  3 Nov 2026

Zheng et al.
thus moves from ranking within a platform already chosen by the user to comparing what
different platforms offer for the same request.
This expanded access creates a new difficulty. Platforms competing for selection can
improve how a resource is described without changing what the user actually receives.
Platform credibility assessment offers a way to discount such mismatch, but each interaction
can only verify the consumed resource, echoing the information problem of experience
goods (Nelson, 1970). Adding platforms expands the set of assessments needed without
increasing the feedback available to each user; strategically changing the descriptions can also
make past assessments less useful. This raises a central question:When does user-centered
agentic recommendation benefit users compared with staying on a single platform?
We model repeated interactions between users with different interests and platforms
offering different resources. Platforms compete for exposure by changing the descriptions of
their recommended resources, not the resources themselves. Correspondingly, each user agent
learns from the target user’s consumption and uses this experience to assess the credibility of
the platforms. We compare the utility users receive when staying on their original platform,
and also against the situation when accurate item description is available.
Without the platform’s credibility assessment on the user agent side, there is a weak
Nash equilibrium in which every platform claims the highest possible relevance, so that
users cannot distinguish better resources through the descriptions. Credibility assessment
limits this loss. Our welfare bound separates the cost of countering platforms’ strategic
overstatement. Most importantly, this allows user side tolerance of adaptive descriptions,
provided that the gap between reported and actual relevance stays within a specified range
for each user and platform, without requiring truthful reporting.
At fixed mechanism parameters, the sample complexity of user agent’s learning about the
platforms’ strategic behavior grows linearly with the number of platforms and falls inversely
with interactions per user. Thus, when the benefit of accurate comparison exceeds the
allowance for changing overstatement, enough feedback guarantees expected welfare at least
as high as staying on the original platform. For a fixed positive margin, an interaction budget
proportional to platform count suffices. A matching example shows why this cost matters:
users can initially be worse off despite access to a better resource. The linear dependence
cannot generally be improved for the studied mechanism.
Experiments on synthetic and Amazon dataset distinguish access to better resources
from benefits users actually receive. In the synthetic market, platform credibility assessment
reduces reporting losses and improves average utility over the original platform by the end
of the simulated horizon. In the Amazon dataset, credibility assessment also helps correct
overstatements, but observed mean utility remains below the original platform. Controlled
markets connect the welfare guarantee to the feedback budget: retaining a valuable resource
while adding low-value platforms requires more interactions for the guarantee utilities, and
observed gains can occur before they are certified. These findings support a conditional
answer to our question, not a universal benefit from competition.
2. Related Work
LLM-based recommendation and strategic presentation.Recommendation agents
combine planning, tools, and knowledge (Wang et al., 2024), support personal instructions (Xu
2

User-Centered Agentic Recommendation
et al., 2025), and motivate user-centered services (Zhang et al., 2026) and cross-platform per-
sonalization (Lin et al., 2026). Magentic Marketplace studies consumer assistants interacting
with competing service agents under different search and manipulation conditions (Bansal
et al., 2025). Presentation affects generated-answer visibility (Aggarwal et al., 2024), supplier
promotion (Kumar and Lakkaraju, 2024; Nestaas et al., 2025), recommendation rankings (Fi-
landrianos et al., 2025), and shopping choices (Allouah et al., 2025); gains can diminish
as adoption spreads (Puerto et al., 2025). These effects vary across strategies and mod-
els (Filandrianos et al., 2025), rather than establishing a universally monotone response to
exaggeration. We separate presentation from resource value to study welfare under repeated
interaction and personal feedback.
Strategic competition and information economics.Strategic recommendation studies
content-provider mediation (Ben-Porat and Tennenholtz, 2018), top-K price of anarchy (Yao
et al., 2023a), and welfare-aligned rewards (Yao et al., 2023b). Learning-platform competition
need not align with user utility (Jagadeesan et al., 2023). Information economics examines
acquisition costs (Stigler, 1961), search diversion (Hagiu and Jullien, 2011), and strategic
communication (Crawford and Sobel, 1982). In Bayesian persuasion, Collina et al. (2026)
identify utility and information conditions for competing providers’ equilibrium outcomes to
approach aligned-provider welfare. Strategic bandits address dynamic context misreports
using post-selection rewards (Kleine Buening et al., 2024b) and screen strategic click rates
using post-click feedback (Kleine Buening et al., 2024a), obtaining equilibrium guarantees
through screening or exclusion. We fix resource-generation rules and analyze reports under
softmax choice and platform credibility assessment; Appendix D compares mechanisms in an
overlapping submodel with the same observable feedback.
Credibility assessment and consumption feedback.Consumption provides quality
information for experience goods (Nelson, 1970); reputation links future returns to quality in-
centives (Shapiro, 1983), while online feedback aggregates transaction experience (Dellarocas,
2003). The Influence Limiter uses target-specific reputations to constrain raters’ influence
on predictions (Resnick and Sami, 2007). We instead use each user’s own record to correct
reports about exogenous resources, guiding selection using consumed-item feedback only.
Our proof bounds welfare distortion through consumption events without requiring minimum
exposure. Policy-regret analyses account for how deviations affect future feedback (Arora
et al., 2018); our welfare guarantees instead apply under a bounded-gap condition.
3. A Model of User-Centered Agentic Recommendation
We studym user agents (UAs) andn platform agents (PAs) interacting overT rounds with
a fixed relevance functionr. Figure 1 illustrates the interaction and feedback.
Users and platforms.User j and platform i have fixed interest centers uj, ci ∈R d,
respectively.1 In round t, the user drawsqj,t ∼Q j, and the platform retrievesaji,t ∼ Ri(· |
j, qj,t)from its private resources. The fixed ruleRi may deterministically select the best
local query match. Retrieved items can differ across users and rounds, but their attributes
remain fixed.
1. Centers describe generation before normalization or retrieval; Appendix D specifies the resource and
information assumptions.
3

Zheng et al.
User j
Needs and consumption
User Agent UAj
One user agent, multiple platforms
Platform Agents {PAi}n i=1
Separate resources; competing descriptions
Interests u j
Current query
q j,t∼ Q j
Broader access
through one agent
Consumption
a jI j,t ,t
One selected
resource
Broadcast query
q j,t
Cross-platform comparison
S ji,t = A ji,t− ω ji,t
Report Record Score
A j1,t ω j1,t S j1,t
A ji,t ω ji,t S ji,t
A jn,t ω jn,t S jn,t
Agent-mediated choice
I j,t = arg maxi{S ji,t + ε ji,t}
ε ji,t i.i.d.∼ Gumbel(0, ν)
Platform credibility assessment
ω j1,t ω j2,t ω j3,t ω ji,t ω jn,t
Update only the consumed record.
PA1 A j1,t a j1,t
R1
λ1,t
PA2 A j2,t a j2,t
R2
λ2,t
PA3 A j3,t a j3,t
R3
λ3,t
PAn A jn,t a jn,t
Rn
λn,t
PAi Report Candidate Resources
A ji,t a ji,t
Ri
λi,t
a ji,t∼ Ri(·| j, q j,t )
A ji,t = r ji,t + λi,t (1− r ji,t )
Descriptions do not change true candidate value.
Each λi,t is shared across users in round t.
Query
Same query to all PAs
Reports{A ji,t}n i=1
I j,t
Consumed value only
r jI j,t ,t
Next round t + 1
Within round t Feedback and next-round credibility update One personal loop for each j∈ [m]
Figure 1: Interaction for userj in roundt. The UA compares recommendations from multiple
PAs; after consumption, only its credibility record for the selected platform is
updated.
Relevance function.The fixed function r : Rd ×R d → [0, 1]gives consumption value
rji,t = r(qj,t, aji,t). This value varies with the query and retrieved candidate; expectations
average over their generation rules. A platform can make an unchanged resource appear
more relevant through its description. To isolate this presentation effect without modeling
the text itself, platformi chooses a description intensityλi,t ∈ [0, 1], shared across users in
roundt. We model the resultingreported relevanceby the bounded interpolation
Aji,t =r ji,t +λ i,t(1−r ji,t).(1)
The intensity fills a fractionλi,t of the remaining gap to1: zero is truthful and one reports
maximal relevance, without changingrji,t or incurring a direct cost. Equation (1) models
platform behavior for analysis; neither this map nor current intensities are supplied to the UA.
It observes reports before choice and only the consumed candidate’s true value afterward.
Recommendation policy.For each query, the UA compares candidates from all platforms.
It usesplatform credibility assessmentto account for inflated reports: a user-specific correction
ωji,t summarizes overstatement observed in past consumption, giving scoreSji,t = Aji,t −ω ji,t.
A larger correction discounts the report more heavily. Each UA maintains its own records,
so different users may assess the same platform differently.
4

User-Centered Agentic Recommendation
To capture choice variability at the same scores, we use the random-utility logit model (Mc-
Fadden, 1974; Yao et al., 2023a) with fresh i.i.d. shocksεji,t ∼Gumbel (0, ν), independent of
the pre-choice state:
Ij,t = arg max i∈[n] {Sji,t +ε ji,t}.(2)
Gumbel noise yields tractable selection probabilities, with a larger scaleν >0making choices
less sensitive to score differences.
User utility.We evaluate recommendations by the true value of the consumed resource,
not its reported relevance. Conditional on the pre-choice state, userj’s expected consumption
utility in roundtis
Uj,t :=E εj,t

rjIj,t,t

=
nX
i=1
Pr
εj,t
(Ij,t =i)r ji,t.(3)
The expectation holds current candidates, reports, and credibility corrections fixed; the
shocks affect choice but do not enter consumption utility.
Platform utility.We measure platform payoff by value-weighted engagement, reflecting
both user selection and delivered value. Under policiesπ = (π1, . . . , πn), platform i’s round
payoff and cumulative objective are
ui,t =
mX
j=1
1{Ij,t =i}r ji,t, J T i (π) =E π
" TX
t=1
ui,t
#
.(4)
Policies may adapt to locally available history, queries, and candidates; Appendix D formalizes
their information constraints.
Platform credibility assessment.Records start at ωji,1 = 0. At round end, the UA
observes the consumed candidate’s exact value and updates only that platform’s record by
exponential averaging:
ωji,t+1 =ω ji,t +η1{I j,t =i}(A ji,t −r ji,t −ω ji,t),0< η≤1.(5)
The rate η weights each newly verified discrepancy; unselected records neither change nor
decay. The credibility correction summarizes past overstatement rather than the latent
intensityλ i,t, and can lag changes in descriptions, queries, and retrieved items.
Definition 3.1 (Actual, calibrated, and original-system utility)Let ιj ∈ [n]be user
j’s original platform, fixed before outcomes and retained in the new market. LetI 0 j,t denote
the choice in(2)with scores replaced by true relevance. The three average utilities are
UT (n) = 1 mT mX j=1 TX t=1 E[Uj,t],
U 0 T (n) = 1 mT mX j=1 TX t=1 E[rjI 0 j,t,t],
BT = 1 mT mX j=1 TX t=1 E[rjιj ,t].
(6)
5

Zheng et al.
Expectations include resource, policy, and choice randomness. Calibration uses the same
candidates and noise scale, solely as an analytical reference; it provides no additional feedback
to the UA. The original system retains the same candidate-generation rule but restricts each
user toι j.
Our research question is:When does platform competition improve user utility over
using a single fixed platform, so thatUT (n) ≥B T, and how does this depend on market size,
interaction horizon, and credibility updates?
4. Welfare Analysis
Cross-platform access can improve available resources, but strategic reports can distort choice.
Using Definition 3.1, write
GainT (n) :=U 0 T (n)−B T ,Distortion T (n) :=U 0 T (n)−U T (n).(7)
The change relative to the original platform decomposes as
∆UT (n) :=U T (n)−B T =Gain T (n)−Distortion T (n).(8)
GainT measures the benefit of calibrated choice, whereasDistortionT measures the effect of
reporting and credibility correction; both are signed. We examine resource opportunities and
competitive distortion, then bound the loss using consumption feedback.
4.1. Resource opportunities and competitive distortion
Let Mj,t(n) := maxi≤n rji,t be the best candidate value for userj in roundt. Compare nested
markets on the same query and resource realization, retaining incumbent candidates when a
platform enters. Abbreviating Mn = Mj,t(n)and x = rj,n+1,t gives the marginal resource
opportunity
Mn+1 −M n = (x−M n)+.(9)
An entrant is valuable insofar as it supplies what the existing market lacks. For a fixed entrant
and resource realization, enlarging the incumbent pool weakly reduces this opportunity,
without requiring independence or identical distributions.
Appendix A.4 derives distributional expressions under conditional independence and
growth rates under additional common-upper-tail conditions. These quantify available
resources, not consumption utility.
From availability to consumption.In the calibrated benchmark, choices use true
relevance but can still select a lower-value resource because of randomness. Hence
GainT (n) = 1 mT X j,t E[Mj,t(n)−r jιj ,t]
− 1 mT X j,t E[Mj,t(n)−r jI 0 j,t,t]. (10)
The first term is the gain over the original platform if the user always consumes the best
available resource. The second subtracts the value lost because random choice may select a
worse candidate, even with accurate scores. Better available resources therefore need not
translate into higher utility.
6

User-Centered Agentic Recommendation
Competitive reporting can erase the comparison value.Even the value attainable
under calibrated choice can be lost through strategic reporting. Disable credibility updates
and keepω ji,t = 0. Letπ max denote the profile in which every platform always chooses the
shared intensityλ i,t = 1.
Proposition 4.1 (Competition without credibility assessment)Under the platform
payoff in(4), πmax is a weak Nash equilibrium of the mechanism without credibility assessment
over admissible finite-horizon policies. Its welfare is
U off T (πmax) = 1 mT X j,t E " 1 n nX i=1 rji,t # .(11)
Against competitors reporting1, no unilateral policy achieves a selection probability
above1 /n. Identical reports induce uniform choice, discarding the premium from favoring
better candidates (Appendix A.2). This equilibrium risk motivates credibility assessment;
the proposition does not assert convergence of platform learning.
4.2. Welfare protection from consumption feedback
Only consumed resources are verified, so infrequently selected platforms can retain inaccurate
records. We bound the loss from actual consumption rather than require every record to
become accurate. The report–value gapdji,t := Aji,t −r ji,t = λi,t(1 −r ji,t)changes with
both the platform’s action and the resource. The next condition bounds its range.
Assumption 4.2 (Bounded gap amplitude)There is a deterministic δ∈ [0, 1]such
that, almost surely over the induced trajectories,
max
s,t≤T
|dji,s −d ji,t| ≤δfor allj∈[m], i∈[n].(12)
The condition restricts variation rather than the level of overstatement, allowing large
persistent discrepancies without requiring convergence. A smallδ is an additional condition
that adaptive reporting need not satisfy. The universally valid choiceδ = 1may yield an
uninformative bound.
The verification budget for one personal record is
Ψ(ν, η) :=
∞X
k=0

1−exp

− (1−η) k
ν

≤ 1 νη .(13)
The index k counts previous consumptions of that platform, not elapsed rounds. Atη = 1,
the first factor(1−η) 0 is interpreted as one, givingΨ(ν,1) = 1−e −1/ν.
Theorem 4.3 (Finite-horizon welfare guarantee)Under Assumption 4.2, the mecha-
nism of Section 3 satisfies
UT (n)−B T ≥Gain T (n)−min

1, nΨ(ν, η) T + δ 2ν  . (14)
The same error term also bounds the absolute distortion|U0 T (n)−U T (n)|.
7

Zheng et al.
The verification costnΨ(ν, η)/T decreases with accumulated consumption, whileδ/(2ν)
accounts for mismatch from changing gaps that feedback need not eliminate. The guarantee
covers every admissible, possibly adaptive profile satisfying the amplitude condition, without
requiring equilibrium or truthful reporting. Corollary B.4 gives the simpler transient bound
n/(νηT).
Why consumption feedback suffices.After separating gap variation, score errors are
weighted by theactualselection probabilities. In expectation, this charges loss to consumed
resources, precisely those whose records update. Afterk previous consumptions, a pair’s
error beyond the gap range is at most(1−η )k, with charge at most1−exp (−(1 −η )k/ν).
Its total charge is bounded byΨ(ν, η); summing overmn records and averaging overmT
interactions yields nΨ(ν, η)/T. No minimum exposure or unconsumed-value feedback is
needed (Appendix B).
When the protected gain is positive.Theorem 4.3 answers the welfare question
whenever calibrated gain covers the distortion budget. LetG be any deterministic lower
bound onGain T (n)for the same market, temperature, and horizon.
Corollary 4.4 (A sufficient budget for user benefit)Under Assumption 4.2, if
GainT (n)≥G > δ/(2ν), thenU T (n)≥B T whenever
T≥ nΨ(ν, η) G−δ/(2ν) .(15)
For a fixed positive marginG−δ/ (2ν), the sufficient interaction budget grows linearly
with market size; a smaller margin requires proportionally more interactions. Both the gain
certificate and the amplitude condition must cover the evaluated horizon.
Appendix B.5 derives explicit gain bounds under resource-separation or heterogeneous-
support conditions, instantiated in Appendix E.6. These expose a temperature tradeoff: less
random choice exploits resource differences more strongly but increases sensitivity to gap
variation. The reporting restrictions remain imposed conditions, not consequences of payoff
maximization.
4.3. The cost of personalized verification
The n/T dependence reflects separate user–platform records: each additional platform creates
another record, but a user supplies onlyT verifications. More users add records and feedback
proportionally, so the ratio does not becomen/(mT ). At η = 1,Ψ( ν, 1) ≤ 1and the transient
bound isn/Teven at low temperature.
8

User-Centered Agentic Recommendation
The following cold-start market shows this cost even with constant values and gaps
(δ = 0). It uses a prescribed maximal-reporting profile, not an equilibrium under credibility
assessment.
Proposition 4.5 (Cold-start loss under market expansion)Fix c∈ (0, 1)and n≥ 4.
For one user, let the original platform have constant valuec, one additional platform have
value1, and the remaining n− 2platforms have value0. All reports equal1, η = 1, and all
credibility corrections start at zero. For everyν >0, atT=⌊n/2⌋,
UT (n)≤ 2(1 +c) n , n > 2(1 +c) c =⇒U T (n)< BT =c.(16)
The best available value nevertheless exceeds the original platform’s value by the constant
1−c.
Unverified reports continue attracting consumption even after the best resource is found:
initial utility can beO(1/n)despite a constant resource advantage (Appendix C).
At fixed temperature, this family also dilutes calibrated choice. WithTn = ⌊n/2⌋ and
νn = 1/(2 logn )for both choice rules, however,U 0 Tn(n) → 1while UTn(n) ≤ 2(1 + c)/n→ 0
(Corollary C.2).
In this same family,δ = 0andΨ( νn, 1) = 1 −n −2. Theorem 4.3 also guarantees positive
net utility atT≥Cn , for every fixedC >1/(1−c)and all sufficiently largen (Corollary C.3).
Thus a linear budget is enough and its order cannot be reduced for this mechanism and
reporting family. This does not establish optimality across UA mechanisms or matching
η, ν, δdependencies.
5. Experiments
We evaluate access gains, reporting losses and recovery through personal consumption
feedback.
Comparisons and protocol.We compare the original fixed platform and cross-platform
choice with or without platform credibility assessment. Evaluator-only frontiers and calibrated
choice at the same temperature separate availability from selection; neither supplies UA
feedback. Net utility relative to the original platform decomposes into calibrated gain and
distortion as in (8).
We use 128 users, 4,096 rounds, 12 seeds, and nested marketsn∈ {2, 4, 8, 16, 32}. Unless
stated otherwise, ν = 0 .1and η = 0 .2. Platform behavior spans fixed heterogeneous
intensities, maximal reporting, and Exp3 learning over five intensities from zero to one (Auer
et al., 2002). Original platforms are assigned by profile–catalog affinity among the first two
catalogs before queries are drawn and retained at every width.
Comparisons reuse resources and original assignments within seeds. PA actions are held
fixed in fixed-policy comparisons; learning PAs adapt to separate feedback histories. We
report conditional expected consumption utility, with sampled choices generating feedback,
and pointwise 95% Student-tintervals over seeds (Appendix E.1).
9

Zheng et al.
5.1. Synthetic markets
Setup.Users and platforms have heterogeneous interest centers in eight dimensions. Each
platform has 24 private items drawn around its center. For each query drawn around a user’s
center, the platform samples four local items and submits the best query match. True value
is cosine similarity rescaled to[0,1](Appendix E.2).
2 4 8 16 32
Platforms
0.00
0.08
0.16
Gain over original platform
Synthetic: 4,096 rounds
Resource frontier
Calibrated choice
Credibility assessment
Without assessment
2 4 8 16 32
Platforms
−0.02
0.00
0.02
0.04
0.06
Gain over original platform
Amazon: Qwen embedding: 4,096 rounds
Resource frontier
Calibrated choice
Credibility assessment
Without assessment
1 64 256 1024 4096
Interaction rounds
−0.04
0.00
0.04
0.08
Cumulative average net gain
Learning platforms; market width 16
Calibrated choice
Credibility assessment
Without assessment
1 64 256 1024 4096
Interaction rounds
−0.024
−0.018
−0.012
−0.006
0.000
Cumulative average net gain
Learning platforms; market width 16
Calibrated choice
Credibility assessment
Without assessment
12 independent seeds; bands: pointwise 95% intervals. Assessment contrasts paired within seed.
2 4 8 16 32
Platforms
0.00
0.08
0.16
Gain over original platform
Synthetic: 4,096 rounds
Resource frontier
Calibrated choice
Credibility assessment
Without assessment
2 4 8 16 32
Platforms
−0.02
0.00
0.02
0.04
0.06
Gain over original platform
Amazon: Qwen embedding: 4,096 rounds
Resource frontier
Calibrated choice
Credibility assessment
Without assessment
1 64 256 1024 4096
Interaction rounds
−0.04
0.00
0.04
0.08
Cumulative average net gain
Learning platforms; market width 16
Calibrated choice
Credibility assessment
Without assessment
1 64 256 1024 4096
Interaction rounds
−0.024
−0.018
−0.012
−0.006
0.000
Cumulative average net gain
Learning platforms; market width 16
Calibrated choice
Credibility assessment
Without assessment
12 independent seeds; bands: pointwise 95% intervals. Assessment contrasts paired within seed.
Figure 2: Synthetic markets under learning PAs: gains across market widths atT = 4096
(left) and cumulative average net utility atn= 16(right).
Broader access does not remove reporting losses.Expanding the market improves
both the frontier and calibrated choice, yet mean utility without assessment remains below
the original platform at every tested width (Figure 2, left). These trajectories illustrate the
risk in Section 4.1, without establishing convergence to its equilibrium.
Credibility assessment improves comparison without requiring honesty.Credibil-
ity assessment turns the negative mean gain positive by the final horizon (Figure 2, right).
This does not require honesty: under fixed maximal reporting, every report remains one, yet
utility exceeds the original platform (Table 1). Scores1−ω ji,t distinguish platforms through
personal feedback even when reporting actions never improve. Useful comparison need not
mean exact recovery of current item values.
Learning PAs reach net gain0.048with interval[0 .039, 0.058], despite negative cumulative
gain at 64 rounds. About one third of users still lose relative to the original platform, so
average benefit is not universal (Appendices E.4–E.5).
Both broad-market environments fall outside the useful gap-amplitude guarantee at the
tested temperatures (Appendix E.1). Their width sweeps change resources and PA learning
as well as verification, so the results describe empirical behavior rather than isolate ann/T
effect.
Market size and the guaranteed benefit region.A separate controlled market tests
Theorem 4.3 with an original platform, a preferred platform and weaker alternatives. We
vary market width, preferred quality and reporting-range widtha. PAs draw intensities
independently in[1 −a, 1]each round, without adapting to UA actions. Certificates use
analytical supports, not observed extrema (Appendix E.6).
10

User-Centered Agentic Recommendation
Unlike broad-market expansion, weaker entrants here do not improve the best resource.
Calibrated gain barely changes, but distortion rises from0.005to0 .056between 4 and 32
platforms (Table 4). Changes in calibrated choice also reduce net gain, so verification costs
are not isolated.
Widening the reporting range can remove the positive certificate with little observed
net-utility change: the theorem covers all admissible policies satisfying the range condition,
not just this random policy. Widening[1−a, 1]also lowers mean intensity, so this is not
an isolated variation effect. In a separate test with restricted Exp3, the first saved positive
net-gain interval occurs at 128 rounds, versus 1,465 certified by Corollary 4.4. The certificate
gives a guaranteed region, not the empirical benefit boundary (Appendix E.6).
5.2. Amazon-grounded markets
Setup.We construct virtual markets from Amazon Reviews 2023 Musical Instruments
metadata and positive training interactions (Hou et al., 2026). A single frozen Qwen3-
Embedding-0.6B representation (Zhang et al., 2025) embeds 2,048 candidate products and
users’ training profiles. Clustering the product vectors gives 32 private catalogs; these
are virtual platforms, not observed sellers. Queries vary around each user’s profile, and
each platform samples four eligible products and submits the best query match. Value
is cosine similarity rescaled to[0, 1], a semantic proxy rather than observed satisfaction
(Appendix E.3).
2 4 8 16 32
Platforms
0.00
0.08
0.16
Gain over original platform
Synthetic: 4,096 rounds
Resource frontier
Calibrated choice
Credibility assessment
Without assessment
2 4 8 16 32
Platforms
−0.02
0.00
0.02
0.04
0.06
Gain over original platform
Amazon: Qwen embedding: 4,096 rounds
Resource frontier
Calibrated choice
Credibility assessment
Without assessment
1 64 256 1024 4096
Interaction rounds
−0.04
0.00
0.04
0.08
Cumulative average net gain
Learning platforms; market width 16
Calibrated choice
Credibility assessment
Without assessment
1 64 256 1024 4096
Interaction rounds
−0.024
−0.018
−0.012
−0.006
0.000
Cumulative average net gain
Learning platforms; market width 16
Calibrated choice
Credibility assessment
Without assessment
12 independent seeds; bands: pointwise 95% intervals. Assessment contrasts paired within seed.
2 4 8 16 32
Platforms
0.00
0.08
0.16
Gain over original platform
Synthetic: 4,096 rounds
Resource frontier
Calibrated choice
Credibility assessment
Without assessment
2 4 8 16 32
Platforms
−0.02
0.00
0.02
0.04
0.06
Gain over original platform
Amazon: Qwen embedding: 4,096 rounds
Resource frontier
Calibrated choice
Credibility assessment
Without assessment
1 64 256 1024 4096
Interaction rounds
−0.04
0.00
0.04
0.08
Cumulative average net gain
Learning platforms; market width 16
Calibrated choice
Credibility assessment
Without assessment
1 64 256 1024 4096
Interaction rounds
−0.024
−0.018
−0.012
−0.006
0.000
Cumulative average net gain
Learning platforms; market width 16
Calibrated choice
Credibility assessment
Without assessment
12 independent seeds; bands: pointwise 95% intervals. Assessment contrasts paired within seed.
Figure 3: Amazon semantic markets under learning PAs: gains across market widths at
T= 4096(left) and cumulative average net utility atn= 16(right).
Smaller resource advantages change the value of access.Amazon resource frontiers
improve with width, but calibrated choice has negative mean gain at every tested width under
the default temperature (Figure 3, left). This contrast precedes reporting and correction: at
n = 16, the mean frontier improvement over the original platform is0.039versus0 .178in
synthetic markets. Amazon’s choice gap of0.046exceeds this resource-access benefit (10).
Reducing distortion need not beat the original platform.Credibility assessment
improves utility under all three PA conditions, including unchanged maximal reporting
11

Zheng et al.
(Table 2). Under learning PAs, remaining distortion is smaller than in synthetic markets, but
even zero distortion cannot overcome Amazon’s negative calibrated gain. The final net-gain
interval,[ −0.0160, 0.0004], includes zero despite positive paired benefit over uncorrected
reports, establishing neither average benefit nor harm relative to the original platform.
Choice depends on value differences relative to temperature. Loweringν from0 .1to
0.03on unchanged Amazon resources makes both calibrated and actual mean gains positive,
although the latter interval still includes zero (Appendix E.5). Under Exp3, lower temperature
improves mean utility in both markets despite increasing distortion, balancing selectivity
against reporting sensitivity. Net gain, not distortion alone, determines user benefit.
Sensitivity to the value proxy.Sparse observed ratings show weak or negative associa-
tions with semantic relevance in the examined cohorts. With the same retrieval process and
a frozen rating-trained outcome model, credibility assessment again improves on uncorrected
reports, while average net utility over the original platform becomes positive (Appendix E.8).
Thus the correction benefit persists across proxies, but whether users beat their original
platform depends on the outcome model; neither simulation establishes actual consumer
welfare.
6. Discussion and Conclusion
User-centered agentic recommendation expands resource access while leaving personal feed-
back limited. Consumption-event accounting bounds welfare loss under platform credibility
assessment without requiring minimum exposure. Resource and reporting conditions give
explicit benefit regions; a cold-start family matches the linear dependence on market size
for this mechanism. Parameterized experiments also expose substantial slack: failure of the
certificate does not imply failure of the market.
The guarantees concern expected average welfare under fixed resource-generation rules,
scalar reports, exact consumption feedback, zero-initialized records, and a bounded range
of reporting discrepancies. Within this scope, the analysis quantifies how resource advan-
tages and personal verification costs jointly determine the benefits of platform competition.
Alternative-update comparisons appear in Appendix E.7. The Amazon study evaluates
simulated outcomes under specified value proxies rather than observed consumer welfare.
AI use statement
We used generative AI tools to polish the manuscript, assist with writing experimental
code, and help identify potential errors in the theoretical analysis. The authors take
responsibility for the final content of this work, including the theoretical claims, experimental
implementation, and reported results.
References
Pranjal Aggarwal, Vishvak Murahari, Tanmay Rajpurohit, Ashwin Kalyan, Karthik
Narasimhan, and Ameet Deshpande. GEO: Generative engine optimization. InPro-
ceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining,
12

User-Centered Agentic Recommendation
pages 5–16. Association for Computing Machinery, 2024. doi: 10.1145/3637528.3671900.
URLhttps://doi.org/10.1145/3637528.3671900.
Amine Allouah, Omar Besbes, Josué D. Figueroa, Yash Kanoria, and Akshit Kumar. What
is your AI agent buying? evaluation, biases, model dependence, & emerging implications
for agentic e-commerce.arXiv preprint arXiv:2508.02630, 2025. doi: 10.48550/arXiv.2508.
02630. URLhttps://arxiv.org/abs/2508.02630.
Raman Arora, Michael Dinitz, Teodor Vanislavov Marinov, and Mehryar Mohri. Policy regret
in repeated games. InAdvances in Neural Information Processing Systems, volume 31,
2018. URL https://proceedings.neurips.cc/paper_files/paper/2018/hash/8643c
8e2107ba86c47371e037059c4b7-Abstract.html.
Peter Auer, Nicolò Cesa-Bianchi, Yoav Freund, and Robert E. Schapire. The nonstochastic
multiarmed bandit problem.SIAM Journal on Computing, 32(1):48–77, 2002. doi: 10.1137/
S0097539701398375. URL https://epubs.siam.org/doi/10.1137/S0097539701398375.
Gagan Bansal, Wenyue Hua, Zezhou Huang, Adam Fourney, Amanda Swearngin, Will
Epperson, Tyler Payne, Jake M. Hofman, Brendan Lucier, Chinmay Singh, Markus Mobius,
Akshay Nambi, Archana Yadav, Kevin Gao, David M. Rothschild, Aleksandrs Slivkins,
Daniel G. Goldstein, Hussein Mozannar, Nicole Immorlica, Maya Murad, Matthew Vogel,
Subbarao Kambhampati, Eric Horvitz, and Saleema Amershi. Magentic marketplace: An
open-source environment for studying agentic markets.arXiv preprint arXiv:2510.25779,
2025. doi: 10.48550/arXiv.2510.25779. URLhttps://arxiv.org/abs/2510.25779.
Omer Ben-Porat and Moshe Tennenholtz. A game-theoretic approach to recommendation
systems with strategic content providers. InAdvances in Neural Information Processing
Systems, volume 31, 2018. URLhttps://proceedings.neurips.cc/paper/2018/hash
/a9a1d5317a33ae8cef33961c34144f84-Abstract.html.
Natalie Collina, Surbhi Goel, Aaron Roth, Emily Ryu, and Mirah Shi. Emergent alignment
via competition. InInternational Conference on Machine Learning, 2026. URLhttps:
//arxiv.org/abs/2509.15090.
Vincent P. Crawford and Joel Sobel. Strategic information transmission.Econometrica, 50(6):
1431–1451, 1982. doi: 10.2307/1913390. URLhttps://www.jstor.org/stable/1913390.
Chrysanthos Dellarocas. The digitization of word of mouth: Promise and challenges of online
feedback mechanisms.Management Science, 49(10):1407–1424, 2003. doi: 10.1287/mnsc
.49.10.1407.17308. URL https://pubsonline.informs.org/doi/10.1287/mnsc.49.10.
1407.17308.
Giorgos Filandrianos, Angeliki Dimitriou, Maria Lymperaiou, Konstantinos Thomas, and
Giorgos Stamou. Bias beware: The impact of cognitive biases on LLM-driven product
recommendations. InProceedings of the 2025 Conference on Empirical Methods in Natural
Language Processing, pages 22397–22426. Association for Computational Linguistics, 2025.
doi: 10.18653/v1/2025.emnlp-main.1140. URL https://aclanthology.org/2025.emnl
p-main.1140/.
13

Zheng et al.
Andrei Hagiu and Bruno Jullien. Why do intermediaries divert search?The RAND Journal
of Economics, 42(2):337–362, 2011. doi: 10.1111/j.1756-2171.2011.00136.x. URL
https://onlinelibrary.wiley.com/doi/10.1111/j.1756-2171.2011.00136.x.
Yupeng Hou, Jiacheng Li, Xiangjun Fu, Zhankui He, An Yan, Xiusi Chen, and Julian
McAuley. Bridging language and items for retrieval and recommendation: Benchmarking
LLMs as semantic encoders. InProceedings of the 64th Annual Meeting of the Association
for Computational Linguistics (Volume 1: Long Papers), pages 3251–3265. Association
for Computational Linguistics, 2026. doi: 10.18653/v1/2026.acl-long.147. URLhttps:
//aclanthology.org/2026.acl-long.147/.
Meena Jagadeesan, Michael I. Jordan, and Nika Haghtalab. Competition, alignment, and
equilibria in digital marketplaces. InProceedings of the AAAI Conference on Artificial
Intelligence, volume 37, pages 5689–5696, 2023. doi: 10.1609/aaai.v37i5.25706. URL
https://ojs.aaai.org/index.php/AAAI/article/view/25706.
Thomas Kleine Buening, Aadirupa Saha, Christos Dimitrakakis, and Haifeng Xu. Bandits
meet mechanism design to combat clickbait in online recommendation. InInternational
Conference on Learning Representations, pages 10275–10303, 2024a. URLhttps://proc
eedings.iclr.cc/paper_files/paper/2024/hash/2ac879d1865475a7abc8dfc7a9c15c
27-Abstract-Conference.html.
Thomas Kleine Buening, Aadirupa Saha, Christos Dimitrakakis, and Haifeng Xu. Strategic
linear contextual bandits. InAdvances in Neural Information Processing Systems, vol-
ume 37, pages 116638–116675. Curran Associates, Inc., 2024b. doi: 10.52202/079017-3703.
URL https://proceedings.neurips.cc/paper_files/paper/2024/hash/d390199c28b
467315b454789b6584f19-Abstract-Conference.html.
Aounon Kumar and Himabindu Lakkaraju. Manipulating large language models to increase
product visibility.arXiv preprint arXiv:2404.07981, 2024. URLhttps://arxiv.org/ab
s/2404.07981.
Jiacheng Lin, Kun Qian, Arvind Srinivasan, Tian Wang, Fang Han, Changran Hu, Junze
Liu, Ziyi Wang, Hanwen Xu, Mengmeng Xue, Shuo Yang, Hansi Zeng, Simon Sinong
Zhan, Kai Zhong, Weiqi Zhang, Dakuo Wang, Tianhao Wang, and Zhiyuan Li. LLM
agents enable user-governed personalization beyond platform boundaries.arXiv preprint
arXiv:2605.09794, 2026. URLhttps://arxiv.org/abs/2605.09794.
Daniel McFadden. Conditional logit analysis of qualitative choice behavior. In Paul Zarembka,
editor,Frontiers in Econometrics, pages 105–142. Academic Press, New York, 1974. URL
https://eml.berkeley.edu/reprints/mcfadden/zarembka.pdf.
Phillip Nelson. Information and consumer behavior.Journal of Political Economy, 78(2):
311–329, 1970. doi: 10.1086/259630. URLhttps://www.journals.uchicago.edu/doi/
10.1086/259630.
Fredrik Nestaas, Edoardo Debenedetti, and Florian Tramèr. Adversarial search engine
optimization for large language models. InInternational Conference on Learning Repre-
14

User-Centered Agentic Recommendation
sentations, pages 4857–4888, 2025. URLhttps://proceedings.iclr.cc/paper_files/
paper/2025/hash/0f12b3c36a781120c4f60e90e855868d-Abstract-Conference.html.
Haritz Puerto, Martin Gubri, Tommaso Green, Seong Joon Oh, and Sangdoo Yun. C-SEO
bench: Does conversational SEO work? InAdvances in Neural Information Processing
Systems, volume 38. Curran Associates, Inc., 2025. doi: 10.52202/085713-0923. URL
https://papers.neurips.cc/paper_files/paper/2025/hash/27aa3aeff0f8460a7b43
d30fa6c5c032-Abstract-Datasets_and_Benchmarks_Track.html.
Paul Resnick and Rahul Sami. The influence limiter: Provably manipulation-resistant
recommender systems. InProceedings of the 2007 ACM Conference on Recommender
Systems, RecSys ’07, pages 25–32. Association for Computing Machinery, 2007. doi:
10.1145/1297231.1297236. URLhttps://doi.org/10.1145/1297231.1297236.
Carl Shapiro. Premiums for high quality products as returns to reputations.The Quarterly
Journal of Economics, 98(4):659–679, 1983. doi: 10.2307/1881782. URLhttps://doi.or
g/10.2307/1881782.
George J. Stigler. The economics of information.Journal of Political Economy, 69(3):213–225,
1961. doi: 10.1086/258464. URL https://www.journals.uchicago.edu/doi/10.1086/
258464.
Yancheng Wang, Ziyan Jiang, Zheng Chen, Fan Yang, Yingxue Zhou, Eunah Cho, Xing
Fan, Yanbin Lu, Xiaojiang Huang, and Yingzhen Yang. RecMind: Large language model
powered agent for recommendation. InFindings of the Association for Computational
Linguistics: NAACL 2024, pages 4351–4364. Association for Computational Linguistics,
2024. doi: 10.18653/v1/2024.findings-naacl.271. URL https://aclanthology.org/2024.
findings-naacl.271/.
Wujiang Xu, Yunxiao Shi, Zujie Liang, Xuying Ning, Kai Mei, Kun Wang, Xi Zhu, Min
Xu, and Yongfeng Zhang. iAgent: LLM agent as a shield between user and recommender
systems. InFindings of the Association for Computational Linguistics: ACL 2025, pages
18056–18084. Association for Computational Linguistics, 2025. doi: 10.18653/v1/2025.fin
dings-acl.928. URLhttps://aclanthology.org/2025.findings-acl.928/.
Fan Yao, Chuanhao Li, Denis Nekipelov, Hongning Wang, and Haifeng Xu. How bad is
Top-K recommendation under competing content creators? InProceedings of the 40th
International Conference on Machine Learning, volume 202 ofProceedings of Machine
Learning Research, pages 39674–39701. PMLR, 2023a. URLhttps://proceedings.mlr.
press/v202/yao23b.html.
Fan Yao, Chuanhao Li, Karthik Abinav Sankararaman, Yiming Liao, Yan Zhu, Qifan Wang,
Hongning Wang, and Haifeng Xu. Rethinking incentives in recommender systems: Are
monotone rewards always beneficial? InAdvances in Neural Information Processing
Systems, volume 36, 2023b. URLhttps://proceedings.neurips.cc/paper_files/pap
er/2023/hash/ebfabf372037aaa4a8d92c9b457ece3e-Abstract-Conference.html.
15

Zheng et al.
Luankang Zhang, Hang Lv, Qiushi Pan, Kefen Wang, Yonghao Huang, Xinrui Miao, Yin
Xu, Wei Guo, Yong Liu, Hao Wang, and Enhong Chen. The next paradigm is user-
centric agent, not platform-centric service.arXiv preprint arXiv:2602.15682, 2026. URL
https://arxiv.org/abs/2602.15682.
Yanzhao Zhang, Mingxin Li, Dingkun Long, Xin Zhang, Huan Lin, Baosong Yang, Pengjun
Xie, An Yang, Dayiheng Liu, Junyang Lin, Fei Huang, and Jingren Zhou. Qwen3 embedding:
Advancing text embedding and reranking through foundation models.arXiv preprint
arXiv:2506.05176, 2025. URLhttps://arxiv.org/abs/2506.05176.
16

User-Centered Agentic Recommendation
Appendix A. Resource Access: Proofs and Calibrated-Gain Bounds
Conditional choice notation.All conditional quantities below are evaluated at a realized
pre-choice state, including the current queries, candidates, descriptions, and credibility
records. This conditioning does not hold candidate values fixed across rounds. Write
dji,t :=A ji,t −r ji,t for the report–value gap and define
eji,t :=d ji,t −ω ji,t, S ji,t =r ji,t +e ji,t.(17)
Let rj,t = (rji,t)n i=1 and ej,t = (eji,t)n i=1. The Gumbel choice rule gives the probability map
and consumption-value operator
pi(v) := exp(vi/ν)Pn
k=1 exp(vk/ν) , p ji,t =p i(rj,t +e j,t),(18)
Uν(r,e) :=
nX
i=1
pi(r+e)r i.(19)
Here pji,t is conditional on the pre-choice state and averages only the fresh choice randomness.
Actual conditional utility isUj,t = Uν(rj,t,e j,t), and calibrated conditional utility isUν(rj,t, 0).
Lemma B.1 derives the probabilities.
A.1. Calibrated gains from candidate moments
The frontier in Section 4.1 quantifies available resources. The following optional certificate
instead evaluates calibrated choice through candidate moments. For each user and round,
define the mean and variance across the realized candidate values:
¯rj,t := 1 n nX i=1 rji,t, V j,t := 1 n nX i=1 (rji,t −¯rj,t)2.(20)
Proposition A.1 (Gains from calibrated comparison)For the resource process in
Section 3 and anyν >0,
GainT (n)≥ 1 mT X j,t E h ¯rj,t −r jιj ,t + (1−e −1/ν)Vj,t i .(21)
No independence or identical-distribution assumption on candidate values is required.
Denote the right-hand side of (21) byGn. It is one possible certificateG in Corollary 4.4,
not a requirement of that result. The first term is the change in average candidate quality
relative to the original platform, and the second lower-bounds the selection premium over
uniform choice. The certificate can be nonpositive even when calibrated gain is positive.
Holding average-quality change and temperature fixed, a larger expected cross-platform
variance raises this lower bound; it does not order the actual utilities of arbitrary markets.
Expectations are taken after evaluating each query’s candidate pool.
ProofFix a realized candidate-value vector r∈ [0, 1]n for one user and round. By the
Gumbel choice identity in Lemma B.1, its calibrated conditional utility is
c:=
Pn
i=1 rieri/ν Pn
i=1 eri/ν .
17

Zheng et al.
Suppress the user and round indices and write
¯r:= 1 n X i ri, V:= 1 n X i (ri −¯r)2, b:=c−¯r, κ:= 1−e −1/ν.
The definition ofcgives
1
n
X
i
(ri −c)e (ri−c)/ν = 0, b= 1 n X i (ri −c)  e(ri−c)/ν −1  .
We claim that, for everyz∈[−1,1],
z(ez/ν −1)≥κz 2.
For z≥ 0, the inequalitiesez/ν − 1 ≥z/ν and1 /ν≥κ prove the claim. Forz = −a≤ 0
witha∈[0,1], concavity ofa7→1−e −a/ν implies
1−e −a/ν ≥a(1−e −1/ν) =aκ.
Multiplication by a proves the same claim for negativez. Since ri, c∈ [0, 1], it applies to
eachr i −c, giving
b≥ κ n X i (ri −c) 2
=κ

V+ (c−¯r) 2 =κ(V+b 2)≥κV.
Thus calibrated conditional utility is at least¯r+ κV for every realized vector. Apply this
inequality to rj,t, subtract the same-round valuerjιj ,t of the original platform, and take
expectations and the average over users and rounds. Definition 3.1 then yields (21). The
argument uses no independence, identical-distribution, or constant-value assumption: the
expectation is taken after evaluating calibrated utility and the cross-platform variance at
each realized vector.
A.2. Proof of Proposition 4.1
ProofIn the without-assessment mechanism, credibility corrections are identically zero.
Fix any platformi and any admissible, possibly randomized and history-dependent deviation
π′ i, while every other platform uses the constant policyλk,t = 1. For every pre-choice state
reached under this deviation, all rivals report1, whereasAji,t = rji,t + λi,t(1 −r ji,t) ≤ 1.
Fresh Gumbel choice randomness therefore gives the conditional probability
p′ ji,t = eAji,t /ν eAji,t /ν + (n−1)e 1/ν ≤ 1 n .
Asr ji,t ≥0, the deviating platform’s conditional expected round payoff is at most
mX
j=1
rji,tp′ ji,t ≤ 1 n mX j=1 rji,t.
18

User-Centered Agentic Recommendation
This holds for every shared intensity chosen by the deviation, including choices based on
current candidates and all admissible past feedback. The joint query and candidate law is
independent of description policies, so the resource expectations on the right are unchanged
by the deviation. Summing over rounds and taking expectations yields
J T,off i (π′ i,π max −i )≤ 1 n mX j=1 TX t=1 E[rji,t] =J T,off i (πmax).
The equality holds because all scores equal1under πmax, so each platform is selected
with conditional probability1/n. Since the comparison covers every admissible full-horizon
unilateral deviation, πmax is a weak Nash equilibrium. The proof permits dependencies
across platforms, users, and rounds; it does not require a fixed realized resource vector.
Under the same all-maximal policy profile, each user’s conditional expected consumption
value is n−1 P i rji,t = ¯rj,t. Averaging gives (11). Consequently, the difference between
calibrated utility and this equilibrium’s utility is exactly the average selection premium over
uniform choice. Applying the pointwise inequality proved above gives
U 0 T (n)−U off T (πmax)≥ 1−e −1/ν mT X j,t E[Vj,t].(22)
This quantifies the comparison value lost at the without-assessment equilibrium. The
result does not assert dominance against arbitrary history-responsive rivals, uniqueness, or
convergence of a learning process.
A.3. Marginal value of an additional candidate
Proposition A.2 (The value of an additional candidate)Fix a user, a round, and
a temperature ν > 0. For values r1, . . . , rn, let Zn = Pn i=1 eri/ν, u0 n = Uν(r, 0), and
Mn = maxi≤n ri. Adding a candidate of valuex∈[0,1]changes calibrated utility by
u0 n+1 −u 0 n = ex/ν Zn +e x/ν (x−u 0 n),(23)
The corresponding frontier increment is(9).
ProofFor the calibrated choice rule, adding valuexgives
u0 n+1 = Znu0 n +xe x/ν Zn +e x/ν .
Subtracting u0 n proves Equation (23). Its coefficient is strictly positive, so the sign of
the increment is the sign ofx−u 0 n. The frontier identity follows directly fromMn+1 =
max{Mn, x}.
19

Zheng et al.
A.4. Resource-frontier results and proofs
To quantify the opportunity for heterogeneous platforms, writeFji,t(x) := Pr(rji,t ≤x|q j,t).
Proposition A.3 (Marginal resource opportunity)Suppose candidate values are con-
ditionally independent across platforms givenqj,t, with conditional CDFsFji,t that need not
coincide. Then
E[Mj,t(n+ 1)−M j,t(n)|q j,t] =
Z 1
0
nY
i=1
Fji,t(x)

1−F j,n+1,t(x)

dx.(24)
At each quality threshold, the integrand is the probability that no incumbent exceeds
it while the entrant does. Thus the marginal value of a platform depends on its resources
relative to the entire incumbent pool, not on a representative platform distribution.
An explicit rate in market width follows under an additional common-upper-tail bench-
mark. Suppose the conditional distributions share right endpoint1and, for almost every
query, satisfy
c−xα ≤1−F ji,t(1−x)≤c +xα,0< x≤x 0,(25)
where c−, c+, α >0and x0 ∈ (0, 1]are uniform over users, rounds, queries, and a fixed nested
sequence of platforms. Platforms may remain heterogeneous within these bounds.
Corollary A.4 (Growth under a common upper tail)Under the conditional indepen-
dence in Proposition A.3 and the uniform tail condition(25), asn→ ∞,
E[1−M j,t(n)|q j,t] = Θ(n−1/α),(26)
E[Mj,t(n+ 1)−M j,t(n)|q j,t] = Θ(n−1−1/α).(27)
The constants are uniform, so the same orders hold after averaging over users, rounds, and
queries.
The exponent α describes the scarcity of near-optimal resources: a larger exponent gives
a slower approach to the upper endpoint. These rates quantify diminishing opportunities
at the market scale, although different heterogeneous entrants need not have successively
smaller increments.
Proposition A.3 allows discrete or continuous candidate values. Corollary A.4 additionally
requires the common-endpoint, uniform upper-tail benchmark. Given a query and a realized
finite catalog, candidate values have finite support and cannot satisfy (25) withα >0: a
maximum below1violates the positive lower tail bound, whereas an atom at1violates the
upper bound asx↓0. Thus these rates do not certify the fixed-catalog experiments.
The upper-tail benchmark is nevertheless compatible with immutable items when its
expectation includes random resource initialization. For example, fix a query and indepen-
dently draw one item valueXi ∼Unif [0, 1]per platform at initialization, retaining that item
forever. With r(q, a) = clip[0,1](a)and aji,t = Xi, the conditional CDF before conditioning
on the realized items is continuous uniform in every round. No item changes across rounds.
More generally, any such interpretation must verify conditional independence and the tail
bounds under the same conditioning. The rates describe the opportunity term in (10), not a
growth law for calibrated or actual utility.
20

User-Centered Agentic Recommendation
ProofFix a user, round, and query, and take all probabilities and expectations in this proof
conditional on that query. WriteRi = rji,t, Mn = maxi≤n Ri, and Fi(x) = Pr(Ri ≤x|q j,t).
No independence across users or rounds is required.
Exact marginal opportunity.ForX=R n+1, the pointwise identity
(X−M n)+ =
Z 1
0
1{Mn ≤x < X}dx
holds because all values lie in[0, 1]. The same-entrant comparison in Section 4.1 is also
pointwise: under a common resource realization, nested nonempty incumbent setsS ⊆ T
not containing entrantksatisfy
(Rk −max i∈T Ri)+ ≤(R k −max i∈S Ri)+.
Taking conditional expectations preserves the inequality without an independence assumption.
This compares the same entrant against two incumbent sets; it does not compare different
entrants along a heterogeneous arrival sequence.
Tonelli’s theorem and conditional independence across platforms give
E[Mn+1 −M n] =
Z 1
0
Pr(Mn ≤x, X > x)dx
=
Z 1
0
" nY
i=1
Fi(x)
#
[1−F n+1(x)]dx.
This proves Equation (24), including distributions with atoms.
Distance to the upper endpoint.Now impose Equation (25) with constants uniform
over the nested platform sequence and all conditioning queries. Set
b= min{x 0,(2c +)−1/α}, ρ= 1−c −bα ∈[1/2,1).
ForY n = 1−M n and0< x≤b, conditional independence yields
(1−c +xα)n ≤Pr(Y n ≥x) =
nY
i=1
Fi(1−x)≤e −nc−xα .(28)
The non-strict inequality inYn ≥x respects possible atoms; endpoints do not affect the tail
integral. Forx > b, monotonicity of the CDFs givesPr(Yn ≥x)≤ρ n. Hence
E[Yn]≤
Z ∞
0
e−nc−xα dx+ρ n
= Γ

1 + 1 α  (nc−)−1/α +ρ n.
For the lower bound,c+xα ≤ 1/2on[0 , b], so log(1 −c +xα) ≥ −2c+xα. Restricting the
integral to[0, bn−1/α]gives
E[Yn]≥
Z bn−1/α
0
e−2nc+xα dx
≥be −2c+bα n−1/α.
The exponentially smallρn is dominated byn−1/α asn→ ∞, proving the first rate.
21

Zheng et al.
Marginal rate.Subtracting twoΘbounds does not determine the order of an increment.
Instead, change variables in the exact marginal formula to obtain
E[Mn+1 −M n] =
Z 1
0
" nY
i=1
Fi(1−x)
#
[1−F n+1(1−x)]dx.
On[0 , b], apply Equation (28) to the product and the two-sided tail condition to the new
platform. Beyondb, bound the integrand byρn. The upper bound is
E[Mn+1 −M n]≤c +
Z ∞
0
xαe−nc−xα dx+ρ n
= c+
α Γ

1 + 1 α  (nc−)−1−1/α +ρ n.
The corresponding lower bound is
E[Mn+1 −M n]≥c −
Z bn−1/α
0
xαe−2nc+xα dx
≥ c−bα+1e−2c+bα
α+ 1 n−1−1/α.
These establish the second rate. Every constant depends only on(c−, c+, x0, α), not on
platform identity, the user, round, or query. Taking expectations over queries and averaging
over users and rounds therefore preserves both orders. The argument requires conditional
independence, but nowhere requires identical platform distributions.
A.5. Why frontier rates are not calibrated-gain rates
Remark A.5 (A frontier rate need not be a utility rate)For an illustrative i.i.d.
continuous uniform benchmark,Pr(Mn ≤x) =x n on[0,1], and hence
E[Mn] =
Z 1
0
(1−x n)dx= n n+ 1 .
For any fixedν >0, the strong law of large numbers applies to the bounded variablesRieRi/ν
and eRi/ν. Their sample means converge almost surely, and the denominator has a strictly
positive limit. Thus
u0 n − →
R 1
0 xex/ν dx R 1
0 ex/ν dx almost surely.
Since0 ≤u 0 n ≤ 1, bounded convergence also gives convergence of expectations. Evaluating
the two integrals,
Z 1
0
ex/ν dx=ν(e 1/ν −1),
Z 1
0
xex/ν dx=νe 1/ν −ν 2(e1/ν −1),
gives
E[Mn] = n n+ 1 − →1,E[u 0 n]− →1−ν+ 1 e1/ν −1 .(29)
22

User-Centered Agentic Recommendation
It is strictly below1because e1/ν − 1 > 1/ν. This example does not impose identical
distributions on the main model: even a simple access benchmark does not justify identifying
the frontier rate with a calibrated-gain rate at fixed temperature.
Appendix B. Proofs of the Consumption-Based Welfare Results
We derive the choice probabilities and perturbation bounds, prove the consumption-based
welfare guarantee, and give computable verification budgets and resource-based gain certifi-
cates.
B.1. From Gumbel choice to selection probabilities
Lemma B.1 (Gumbel choice probabilities)Conditional on the pre-choice state, let
S1, . . . , Sn be fixed scores and letεi be independentGumbel(µ, ν)shocks with common location
µand scaleν >0. IfI= arg max i(Si +ε i), then
Pr(I=i) = exp(Si/ν)P
k exp(Sk/ν) .
ProofThe Gumbel cumulative distribution and density are
F(x) = exp
h
−e−(x−µ)/ν
i
, f(x) = 1 ν e−(x−µ)/νF(x).
Ties have probability zero. Conditioning onεi =xand using independence gives
Pr(I=i) =
Z ∞
−∞
f(x)
Y
k̸=i
F(x+S i −S k)dx.
Sety=e −(x−µ)/ν. Thenf(x)dx=−e −y dy, so reversing the integration limits yields
Pr(I=i) =
Z ∞
0
exp

−y

1 + X
k̸=i
e(Sk−Si)/ν



 dy
= 1P
k e(Sk−Si)/ν = eSi/ν P k eSk/ν .
The common location cancels. For fixed true valuesri, it follows thatE[rI ] = P i Pr(I = i)ri,
which gives (19) upon substitutingSi = ri + ei. The expectation does not include the choice
shock in the reward.
B.2. Softmax perturbations
The following lemmas provide the two comparisons used in Theorem 4.3. All vectors refer to
one user and one round.
23

Zheng et al.
Lemma B.2 (Nonnegative reweighting) Let v∈R n be arbitrary base scores,z≥ 0
score increments, andr∈ [0, 1]n rewards. Let p0 and p be the softmax distributions ofv and
v+zat temperatureν >0. Then
|⟨p−p 0,r⟩| ≤ X
i
pi(1−e −zi/ν)≤ 1 ν X i pizi.(30)
ProofPut Z = P i pie−zi/ν ∈ (0, 1]. Direct normalization givesp0 i = pie−zi/ν/Z. If Z <1,
the vector qi = pi(1 −e −zi/ν)/(1 −Z )is a probability distribution andp = Zp0 + (1 −Z )q.
Both expected rewards lie in[0, 1], so their difference is at most1−Z in absolute value. The
final bound follows from1−e −x ≤x for x≥ 0. If Z = 1, positivity of softmax probabilities
implies zi = 0for every i, and the distributions agree. The argument requires no relation
between the base scoresvand the true rewardsr.
Lemma B.3 (Relative score perturbations)For r∈ [0, 1]n, b∈R n, and ν >0, write
osc(x) = maxi xi −min i xi. Then
|Uν(r,b)− Uν(r,0)| ≤osc(r) min

1, osc(b) 4ν  .(31)
ProofLetp (s) i ∝exp((r i +sb i)/ν)fors∈[0,1]. Differentiating the normalization gives
d
ds
X
i
p(s) i ri = 1 ν Covp(s)(r,b).
A random variable supported on an interval of lengthL has variance at mostL2/4: subtract
the interval midpoint and bound the resulting second moment. Cauchy–Schwarz therefore
bounds the absolute covariance byosc(r) osc(b)/4. Integration proves the linear bound. The
other bound follows because both expected rewards lie betweenmini ri andmax i ri.
B.3. Proof of Theorem 4.3
We first establish the theorem’s absolute distortion guarantee:
|DistortionT (n)| ≤min

1, nΨ(ν, η) T + δ 2ν  .(32)
Combining this bound with (8) yields (14).
ProofFix a trajectory on which Assumption 4.2 holds and putaji = mins≤T dji,s. This
path-dependent minimum is a proof aid, not an algorithmic input. If pair(j, i)has been
selectedNtimes before roundt, expanding the convex-combination update (5) gives
aji[1−(1−η) N ]≤ω ji,t ≤a ji +δ,−δ≤e ji,t ≤δ+a ji(1−η) N .(33)
Forη= 1, the product interpretation gives(1−η) N = 1whenN= 0and0otherwise.
24

User-Centered Agentic Recommendation
Define pre-choice auxiliary variables
bji,t = min{eji,t, δ}, z ji,t = (eji,t −δ) +.
Then e = b + z, b∈ [−δ, δ], and z≥ 0. Apply Lemma B.2 between scoresr + b + z and
r + b, and Lemma B.3 betweenr + b and r. The first comparison is weighted by the actual
selection probabilities:
|Uν(rj,t,e j,t)− Uν(rj,t,0)| ≤
X
i
pji,t(1−e −zji,t /ν) + δ 2ν .(34)
Let Ft be the complete pre-choice analysis state, including current values, reports, and
credibility records; it is not the UA’s observation. Sinceδ is deterministic andz is determined
by the current state, fresh choice randomness gives
E[1−e −zjIj,t,t/ν | Ft] = X
i
pji,t(1−e −zji,t /ν).
On the( k + 1)st selection of a pair, (33) impliesz≤a ji(1 −η )k ≤ (1 −η )k. Thus, pathwise,
X
{t:Ij,t=i}
(1−e −zji,t /ν)≤ X
k≥0

1−exp

− (1−η) k
ν

= Ψ(ν, η).(35)
Take the triangle inequality for the averaged distortion, substitute the conditional-expectation
identity, sumoverthe mnpairs, anddivideby mT in(34). Thisproves(32), withtruncationat
1because both utilities lie in[0, 1]. Substitution in (8) proves the net-welfare bound (14). The
future-dependent aji enters only the pathwise upper bound, not the conditional-expectation
substitution.
The welfare bound concerns expectations; the pathwise accounting step does not turn it
into a realized or high-probability guarantee.
Corollary B.4 (Linearized welfare bound)Under Assumption 4.2,
|DistortionT (n)| ≤min

1, n νηT + δ 2ν  .(36)
ProofApply1 −e −x ≤x termwise in (13) to obtainΨ(ν, η) ≤ν −1 P k≥0(1 −η )k = 1/(νη ),
and substitute into (32).
Comparison with the without-assessment equilibrium.For the same resource market
and temperature, combining (22) with (32) gives, for every admissible credibility-assessment
game profile satisfying Assumption 4.2,
UT (n)−U off T (πmax)≥ 1−e −1/ν mT X j,t E[Vj,t]
−min

1, nΨ(ν, η) T + δ 2ν  . (37)
This follows by adding and subtractingU 0 T (n). It compares the profile with the specified
without-assessment equilibrium, without requiring the credibility-assessment game profile to
be an equilibrium.
25

Zheng et al.
B.4. Evaluating the verification budget
The budget in (13) retains the nonlinear cost of changing a selection distribution. It is a
property of the existing mechanism, not an additional algorithmic parameter.
Proposition B.5 (Budget evaluation and certification)For every ν >0,0 < η≤ 1,
and integerK≥1,
0≤Ψ(ν, η)−
K−1X
k=0

1−exp

− (1−η) k
ν

≤ (1−η) K
νη .(38)
Under Assumption 4.2, if a deterministic certificateG satisfies GainT (n) ≥G > δ/(2ν)in
the evaluated market and horizon, then
T≥ nΨ(ν, η) G−δ/(2ν) =⇒U T (n)≥B T .(39)
ProofBound the omitted terms by(1 −η )k/ν and sum their geometric tail to obtain (38).
Substituting the assumed gain certificate into Theorem 4.3 and solving forT proves (39),
equivalently Corollary 4.4.
At ν = 0.1and η = 0.2, this yieldsΨ(ν, η) ≈ 13.405600945, compared with1/(νη ) = 50.
The refinement reduces the verification allowance but leaves the gap-amplitude requirement
unchanged.
B.5. Certificates from resource and reporting conditions
Theorem 4.3 requires a gap-amplitude bound, while Corollary 4.4 also requires positive
calibrated gain. The following certificates derive both from explicit resource and reporting
conditions. They are sufficient conditions on a market, not extra observations supplied to
the UA and not predictions of strategic behavior.
Proposition B.6 (Heterogeneous support certificate) Suppose deterministic inter-
vals satisfy, almost surely throughout the evaluated horizon,
rji,t ∈[L ji, Hji]⊆[0,1], λ i,t ∈[λ − i , λ+ i ]⊆[0,1].
The platform intensity remains shared across users and may otherwise adapt arbitrarily. Set
δsup := max j,i

λ+ i (1−L ji)−λ − i (1−H ji) 	 .(40)
For each user choose a reference platformkj, putL min j = mini Lji, and define
Gsup j :=L min j −H jιj + Ljkj −L min j 1 + P i̸=kj exp((Hji −L jkj )/ν) ,
Gsup := 1 m mX j=1 Gsup j . (41)
26

User-Centered Agentic Recommendation
Then Assumption 4.2 holds withδ = δsup and GainT (n) ≥G sup. Hence, if Gsup > δsup/(2ν),
T≥ nΨ(ν, η) Gsup −δ sup/(2ν) =⇒U T (n)≥B T .(42)
ProofThe map λ(1 −r )is increasing in λ and decreasing in r on the given domain.
Therefore each pair’s gap stays in
[λ− i (1−H ji), λ+ i (1−L ji)],
which proves (40), simultaneously for all users under a shared platform action. Conditional
on any candidate realization, calibrated choice gives
p0 jkj ,t = 1 1 + P i̸=kj exp((rji,t −r jkj ,t)/ν) ≥ 1 1 + P i̸=kj exp((Hji −L jkj )/ν) .
Every candidate has value at leastLmin j , and candidate kj has value at leastLjkj. Thus
calibrated conditional utility minus the original value is at least
Lmin j +p 0 jkj ,t(Ljkj −L min j )−H jιj ≥G sup j .
The multiplier Ljkj −L min j is nonnegative, so the probability lower bound preserves the
inequality. Average over candidates, rounds, and users to prove (41); apply Corollary 4.4 to
obtain (42).
Independence, identical distributions, and deterministic candidate values are unnecessary.
The certificate is valid for any reference kj, although choosing a platform with a high
lower endpoint makes it useful. In particular, distinct users may have distinct reference
platforms. The intervals must cover the induced distributions, not merely the values observed
in one simulation. For example, if reporting lies in[1 −a, 1]and a pair’s value lies in
[v−w, v+w]⊆[0,1], its gap range is at most
2w+a(1−v−w).(43)
This expression separates resource spread from allowed reporting variation; neither is inferred
from a no-regret property.
Corollary B.7 (Resource margins and temperature)Let n≥ 2. Suppose that almost
surely, for every user and round, a best candidateksatisfies
rjk,t −r jιj ,t ≥g >0, r jk,t −r ji,t ≥γ >0 (i̸=k).
The constantsg, γare uniform, butkmay depend on the candidate realization. Then
GainT (n)≥g− (n−1)e −γ/ν 1 + (n−1)e −γ/ν .(44)
If Assumption 4.2 also holds, the following conditions are sufficient forUT (n)≥B T:
3δ
2g ≤ν≤ γ log((n−1)(3−g)/g) , T≥ 3nΨ(ν, η) g .(45)
27

Zheng et al.
ProofFix a realized candidate vector and abbreviate its best value by M. With x =
(n− 1)e−γ/ν, calibrated choice selects the best candidate with probability at least1/(1 + x).
Since all values lie in[0, 1], its expected shortfall fromM is at mostx/(1 + x). Subtract the
original value and then average to obtain (44).
For (45), note that0< g≤ 1and the logarithm is positive. Its temperature upper bound
implies x≤g/ (3 −g )and hence x/(1 + x) ≤g/ 3. The lower bound givesδ/(2ν) ≤g/ 3,
while the horizon condition givesnΨ(ν, η)/T≤g/ 3. Substitution in Theorem 4.3 proves the
result.
The temperature interval in (45) can be empty: its feasibility requires
3δ
2g log (n−1)(3−g) g ≤γ.
This is a sufficient compatibility test between resource separation, market size, and reporting
variation, not a necessary condition or an optimal temperature rule. The heterogeneous
interval certificate can be substantially tighter because it retains each competitor’s separation.
Uniform positive margins exclude realizations in which no candidate improves on the original
platform; they are not implied by the resource-center model.
Appendix C. Verification Cost of Market Expansion
This appendix proves the cold-start obstruction in Section 4.3, extends it to other horizons,
and separates it from the loss due to stochastic choice. Values and reports are constant
throughout; the construction does not require changing descriptions or an alternating resource
process.
C.1. Cold-start bound for a general horizon
We prove Proposition 4.5 through the following more general bound.
Lemma C.1 (Finite-horizon cold-start bound)In the market of Proposition 4.5, for
everyν >0and1≤T≤n−2,
UT (n)≤ 1 +c T  Hn−1 −H n−T−1  , H k := kX s=1 1 s , H 0 := 0.(46)
ProofAll reports equal one, which is feasible under (1) by takingλi = 1; the platform with
true value one has zero gap regardless of its intensity. Withη = 1, a zero-value platform
has score one until first consumption and score zero thereafter. The value-one platform
always has score one. The original platform’s score is one before its first consumption andc
thereafter.
Before round t, at most t− 1distinct zero-value platforms have been consumed. For
1 ≤t≤n− 1, there are consequently at leastn−t− 1unverified zero-value platforms.
Together with the value-one platform, they contribute at least(n−t )e1/ν to the softmax
normalizer. Only the value-one platform and the original platform contribute to its value-
weighted numerator, and their scores are at most one. LetFt denote the complete pre-choice
28

User-Centered Agentic Recommendation
analysis state; this does not require the UA to observe unconsumed values. Conditional on
that state,
E[rIt,t | Ft] =
P
i rieSi,t/ν P
i eSi,t/ν ≤ (1 +c)e 1/ν (n−t)e 1/ν = 1 +c n−t .(47)
No independence between successive choices or uniform coverage is used. For1≤T≤n− 2,
take expectations and average to obtain
UT (n)≤ 1 +c T TX t=1 1 n−t
= 1 +c T  Hn−1 −H n−T−1  ≤ 1 +c n−T .(48)
For n≥ 4, the choiceT = ⌊n/2⌋ lies in this range andn−T≥n/ 2, giving (16). Since the
old platform’s value is alwaysc, BT = c; the strict inequality follows whenn >2(1 + c)/c.
The best available value is one at every round, proving the claimed constant resource-frontier
gain. The proof uses continued softmax competition between unverified reports and the best
platform; a different user-agent rule need not obey the bound.
C.2. Separating verification from stochastic choice
At a fixed temperature, calibrated utility also decreases as the market expands in this
construction. The following joint market–temperature family keeps calibrated choice nearly
efficient and uses the same temperature for actual choice.
Corollary C.2 (Cold-start loss with nearly efficient calibrated choice)Fix c∈
(0,1). For every integern≥4, use the market and policies of Proposition 4.5, with
Tn =⌊n/2⌋, ν n = 1 2 logn .(49)
Evaluate actual and calibrated utility at this same temperature. Then
1−U 0 Tn(n)≤(1−c)n −2(1−c) + 1 n , U Tn(n)≤ 2(1 +c) n .(50)
Consequently, asn→ ∞,
DistortionTn(n)→1,Gain Tn(n)→1−c, U Tn(n)−B Tn → −c.(51)
The calibrated choice becomes nearly efficient while actual utility vanishes over the
same horizon and resource process. This is a joint parameter-family counterexample, not
a fixed-temperature large-market conclusion or a claim that a fixed market fails forever.
It also does not establish a dynamic equilibrium. The limitation is specific to the stated
mechanism: a different user agent need not keep undiscovered reports competing with a
discovered value-one resource.
29

Zheng et al.
ProofFor the market in Proposition 4.5, fully calibrated softmax utility is constant across
rounds and equals
U 0 T (n) = e1/ν +ce c/ν e1/ν +e c/ν +n−2 .(52)
Its shortfall from one satisfies
1−U 0 T (n) = (1−c)e c/ν +n−2 e1/ν +e c/ν +n−2 ≤(1−c)e −(1−c)/ν + (n−2)e −1/ν.(53)
Setν=ν n = 1/(2 logn). Thene −(1−c)/νn =n −2(1−c) ande −1/νn =n −2, so
1−U 0 Tn(n)≤(1−c)n −2(1−c) + n−2 n2 ≤(1−c)n −2(1−c) + 1 n .(54)
Proposition 4.5 applies at every positive temperature and therefore givesUTn(n) ≤ 2(1 +c)/n
at this sameνn. Since c∈ (0, 1)is fixed independently of n, the calibrated utility converges
to one and the nonnegative actual utility converges to zero. Finally,BTn = c for every n.
Substitution into the definitions ofDistortionandGainproves (51).
This comparison uses one joint sequence(n, Tn, νn)for both systems. In contrast, for
any fixed ν >0, the numerator of (52) is constant while its denominator grows linearly in
n, and the calibrated utility tends to zero. Thus neither a fixed-temperature large-market
conclusion nor interchange of long-run and low-temperature limits is used.
C.3. Matching the order of the interaction budget
Corollary C.3 (A linear budget in the same cold-start family)Fix c∈ (0, 1)and
use the market and reporting profile of Proposition 4.5, withη = 1and νn = 1/(2 logn )for
everyn≥4. Forn >2(1 +c)/cand1≤T≤ ⌊n/2⌋,
UT (n)≤ 2(1 +c) n < c=B T .(55)
Conversely, for every fixedC >1/(1−c), all sufficiently largensatisfy
T≥Cn=⇒U T (n)> BT .(56)
Both statements concern expected cumulative-average utility under the same mechanism,
resources, and prescribed reporting profile.
ProofFor T≤ ⌊n/2⌋, Lemma C.1 and (48) giveUT (n) ≤ (1 + c)/(n−T ) ≤ 2(1 + c)/n.
The stated restriction onnmakes this smaller thanc.
In this market each gap is constant, soδ = 0. Since η = 1,Ψ( νn, 1) = 1−e −1/νn = 1−n −2.
Calibrated utility is independent ofT, and (53) gives, for everyT,
GainT (n)≥1−c−(1−c)n −2(1−c) − 1 n .
ForT≥Cn, Theorem 4.3 therefore implies
UT (n)−B T ≥1−c−(1−c)n −2(1−c) − 1 n − 1−n −2 C .(57)
30

User-Centered Agentic Recommendation
Its right-hand side converges to1−c− 1/C > 0, which proves (56). The convergence is
uniform over horizonsT≥Cnbecause no remaining term depends onT.
Thus the ordern of a sufficient interaction budget cannot be reduced uniformly within
this family: budgets o(n)eventually belong to the short-budget regime, whereas a large
enough constant multiple ofn suffices. This does not identify the earliest crossing time, give
a per-user realized safety guarantee, or prove an information-theoretic lower bound for other
recommendation mechanisms. It matches only the market-width order in the displayed joint
temperature family; it does not establish necessity of the separateη, ν, or δ dependencies.
Appendix D. Additional Model Details
The query and candidate process has a fixed joint law independent of description policies;
independence across platforms, users, or rounds is not required. Before normalization or
retrieval, raw queries and resources take the formuj + ξ and ci + ζ, with fixed perturbation
laws satisfying Eξ = Eζ = 0. Thus the centers need not equal the means of normalized
queries or retrieved candidates.
Definition D.1 (Admissible platform policy)A policy πi chooses a possibly random-
ized λi,t using the queries received, its own current candidates, and its past submissions and
payoff feedback. It cannot condition on current UA choice shocks or future observations.
Users’ credibility records and competing platforms’ resources are not disclosed to the platform.
Non-disclosure does not rule out inference from available feedback. A unilateral deviation
in J T i regenerates subsequent choices, feedback, and credibility records rather than holding
the realized history fixed.
Comparison with screening mechanisms.For one user with fixed positive resource
values, value-weighted engagement and selection count induce identical platform preferences.
Inthisoverlappingsubmodel, themechanismofKleineBueningetal.(2024b, AppendixA)can
detect misreports from consumed rewards without knowing the reporting map. Its incentive
guarantee combines exclusion with greedy selection and a terminal uniform-allocation phase;
these operations change the choice rule studied here. When values vary across users or
rounds, the payoff equivalence no longer holds in general.
Appendix E. Experimental Details
E.1. Shared interaction and evaluation protocol
We use the mechanism and default settings of Sections 3 and 5, with seeds 1200–1211. The
without-assessment condition keepsω≡ 0. Nested markets reuse the firstn platforms of a
maximum-width resource stream, retaining original assignments. Queries, local retrieval, PA
sampling and UA choice use separate random streams. Across mechanisms, resources and
sampling uniforms are paired, but learning actions adapt to their own feedback histories.
Saved horizons T∈ {1, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096} are cumulative prefixes,
not independent replications or retuned learners. Parameter grids and representations are
fixed before simulation.
31

Zheng et al.
Platform behavior.Fixed heterogeneous PAs draw λi ∼Unif [0.25, 0.95]once. A maximal-
reportingconditionsetsallintensitiestoone. LearningPAsuseExp3over {0, 0.25, 0.5, 0.75, 1}.
With weightsw ia,1 = 1and full horizonH= 4096, the probabilities and update are
γ= min
(
1,
s
5 log 5
(e−1)H
)
,
ρia,t = (1−γ) wia,tP
b wib,t
+ γ 5 ,
logw ia,t+1 = logw ia,t + γ 5 1{a=ℓ i,t}(ui,t/m) ρia,t .
(58)
Here ℓi,t is the sampled action andui,t is the realized payoff in (4). PAs observe only their own
aggregate payoffs, not competing resources, credibility records or counterfactual rewards. The
finite grid is an experimental choice; these runs do not establish policy regret or convergence.
Estimation and uncertainty.Within each seed, utility averagesP i pji,trji,t over users
and prefix rounds, conditional on sampled histories. This is an evaluator quantity: sampled
choices generate PA rewards and credibility updates. All benchmarks use the same candidates;
neither unconsumed values nor the reporting formula are supplied to the UA.
Net gains and mechanism differences are computed within seed. Pointwise95%intervals
use t11,0.975 times the standard error over 12 seeds, without multiplicity adjustment. Amazon
intervals condition on its frozen data and representation; synthetic seeds also redraw centers
and catalogs. Users, rounds and prefixes are not independent replications. Negative-net-gain
user fractions describe within-seed heterogeneity, not failure probabilities for the population-
average guarantee.
Fixed-policycontrastsisolatescorecorrection; Exp3contrastsincludebehavioralresponses.
Width sweeps also change resources and the payoff scale per platform, so they do not isolate
verification speed. Full configurations and seed-level outputs are retained in the experiment
artifacts.
Relation to the welfare guarantee.The broad-market queries have full spherical support,
local sampling permits repeated items, and Exp3 assigns positive probability to intensities
zero and one. For broad-market Exp3 and T≥ 2, no deterministic δ < 1is therefore
uniformly valid; fixed intensity instead has essential gap rangeλi. These runs test empirical
behavior beyond the useful small-amplitude guarantee, not its certified budget. Observed
ranges are not almost-sure certificates. Appendix E.6 supplies a bounded-support test. Finite
catalogs also need not satisfy the common-upper-tail assumptions, so measured frontier gains
do not test their asymptotic rate.
E.2. Synthetic resource generator
Write unit(v) = v/∥v∥ 2. User and platform centers are independent unit-normalized standard
Gaussian vectors inR8. Each platform has 24 private items:
vik = unit(ci + 0.35zik), q j,t = unit(uj + 0.20ξj,t), z ik, ξj,t ∼ N(0, I8).(59)
Items are drawn once; query innovations are fresh each round. For each query, each platform
draws four local indices uniformly with replacement and submits the item with largest query
32

User-Centered Agentic Recommendation
cosine. Value is(1 + qT j,tvaji,t )/2. This fixed rule is independent of descriptions and sees no
competing catalog. Centers are pre-normalization locations, not means of query-conditioned
candidates.
The original platform is assigned before queries by
ιj ∈arg max i∈{1,2} uT j

1
24
24X
k=1
vik
!
.(60)
It supplies exactly the same subsequent candidates in the original and expanded markets
and is not optimized retrospectively over all 32 platforms.
E.3. Amazon data and semantic resources
Data and representation.The Amazon Reviews 2023 Musical Instruments 5-core release
contains 511,836 ratings, split globally by timestamp into approximately80/10/10training,
validation and test portions. We retain 2,048 text-covered training-eligible products and 256
users with at least three positive text-covered training interactions. The inherited product
subset used MF-derived strata, but neither its old catalog labels nor MF predictions define
the semantic market.
Frozen Qwen3-Embedding-0.6B (Zhang et al., 2025) embeds titles, categories, features and
descriptions, excluding reviews and rating statistics. Inputs are capped at 1,200 characters
and 256 tokens; last non-padding token pooling and L2 normalization yield 1,024 dimensions.
The cache covers 3,616 products, including profile items outside the candidate universe; its
manifest records the model revision.
Platforms and original assignments.Euclidean KMeans forms 32 virtual catalogs.
Among five predetermined starts with 40 Lloyd iterations and at least eight items per catalog,
minimum inertia selects the partition before simulation. Catalog sizes range from 16 to 185;
platform centers are empirical vector means, not observed seller attributes.
Each seed samples 128 users and permutes catalogs. User centers average up to eight
most recent training products rated at least four stars, then normalize. As in (60), the
original platform maximizes profile–catalog affinity among the first two catalogs, using each
catalog’s size. This simulated assignment precedes queries and is retained at every width.
Queries and local retrieval.For the unit profileu j andd= 1024, draw
qj,t = unit

uj + 0.5√ d ξj,t

, ξ j,t ∼ N(0, Id).(61)
Each platform samples four products uniformly with replacement from its own catalog,
excluding products the user rated during training, and submits the best current-query cosine
match. The simulated value is
rji,t = 1 + cos(qj,t, vaji,t ) 2 .(62)
Interpretation.The LLM supplies representations, not strategic text or feedback; con-
sumption reveals the selected semantic proxy exactly. Generated outcomes are not observed
consumer counterfactuals. Inherited sampling, full-period 5-core filtering, uncertain metadata
timing and possible pretraining overlap limit interpretation. Held-out ratings do not tune
the mechanism.
33

Zheng et al.
E.4. Platform-policy comparisons
Table 1: Credibility assessment effects in
synthetic markets.
PA
Without
assessment
With
assessment Change
Fixed−0.007 0.055 0.062
Maximal−0.062 0.030 0.092
Exp3−0.039 0.048 0.087
Table 2: Credibility assessment effects in
Amazon markets.
PA
Without
assessment
With
assessment Change
Fixed−0.013−0.008 0.005
Maximal−0.016−0.009 0.007
Exp3−0.014−0.008 0.007
Seed means at n = 16, T = 4096, ν = 0.1and η = 0.2. Without assessment and With assessment give
net utility relative to the original platform; Change is their paired difference before rounding. All paired
pointwise 95% intervals for Change exclude zero. Fixed denotes heterogeneous fixed intensities; Maximal sets
all intensities to one. These two conditions hold PA actions unchanged across mechanisms, whereas Exp3
comparisons include platform responses. Amazon uses the semantic value proxy.
Synthetic net-gain intervals are[0.0455, 0.0643]under fixed reporting and[0 .0390, 0.0576]
under Exp3; Amazon intervals are[−0.0166,− 0.0001]and[ −0.0160, 0.0004]. Thus positive
paired assessment benefits need not imply benefit over the original platform. Negative-
net-gain user fractions average29.2%/33.1%for synthetic fixed/Exp3 and67 .5%/66.5%for
Amazon.
E.5. Choice-temperature sensitivity
Across the tested temperatures, lower values improve calibrated and actual mean gains in
both markets under Exp3, despite larger distortion (Table 3). Better selection can outweigh
increased reporting sensitivity, but Amazon’s actual net-gain interval atν = 0.03still crosses
zero. Resources are reused across temperatures; PA actions adapt to each UA’s feedback
history.
E.6. Controlled certificate experiments
Shared bounded-support construction.Each platform submits ai = ei. User j’s query
center has coordinates0 .4at its original platform1, h at a preferred platformi⋆ j ̸= 1, 2,
and0 .1elsewhere. Queries add independent coordinate noise uniform on[−0.01, 0.01], with
r(q, a) = clip[0,1](qTa). Candidates and query laws are fixed. Each PA selects one intensity
in[1 −a, 1]per round, shared across users; this restriction is imposed, not induced by
competition. Both protocols use 128 users, 4,096 rounds, 12 seeds,ν= 0.1andη= 0.2.
Support-based certificate.The value supports are[0 .39, 0.41],[ h− 0.01, h+ 0.01]and
[0.09,0.11]for the original, preferred and remaining platforms. Proposition B.6 gives
δ= 0.02 + 0.89a,
G= 0.09−0.41 + h−0.1 1 + exp((0.42−h)/0.1) + (n−2) exp((0.12−h)/0.1) .(63)
The widest gap interval is[(1 −a )0.89, 0.91], at a low-value platform. The reciprocal
denominator bounds the preferred platform’s calibrated selection probability using its lowest
34

User-Centered Agentic Recommendation
Table 3: Choice-temperature sensitivity with Exp3 PAs and credibility assessment, atn = 16,
T = 4096and η = 0.2. Value columns are in units of10−3. Means and pointwise
95% intervals for actual net gain use 12 seeds.
Marketν
Calibrated
gain
Actual
net gain 95% CI Distortion
Synthetic0.03 165.2 99.8 [89.8,109.8] 65.4
0.10 92.5 48.3 [39.0,57.6] 44.2
0.30 4.4−11.9 [−20.3,−3.6] 16.3
Amazon0.03 12.8 6.1 [−1.9,14.1] 6.7
0.10−6.6−7.8 [−16.0,0.4] 1.2
0.30−12.9−13.3 [−21.8,−4.9] 0.4
value and competitors’ highest values. Every resource is worth at least0.09, the preferred
resource adds at leasth− 0.1, and the original is worth at most0.41. Thus G is an analytical
lower bound, not a measured gain.
ForG > δ/(2ν), Corollary 4.4 gives the certified budget
Tcert =
 nΨ(ν, η)
G−δ/(2ν)

.
At( n, h, a) = (16, 0.9, 0.05), δ = 0.0645, G >0.468981andΨ(0 .1, 0.2) < 13.405602by (38).
Substitution gives a certified budget of 1,465 rounds and net gain above0.0941at T = 4096.
All certificates use analytical supports and conservative rounding, not observed extrema.
RestrictedExp3.Thefirstprotocolfixes( n, h, a) = (16, 0.9, 0.05), withpreferredidentities
cyclically assigned to platforms3, . . . ,16, and runs (58) on{0.95, 0.9625, 0.975, 0.9875, 1}.
Final net gain is0.4658, with interval[0.4657, 0.4659], versus −0.2210without assessment.
The first saved positive interval occurs at 128 rounds, while the 64-round interval is negative.
This observed transition is not a stopping-time guarantee; the analytical budget covers every
admissible policy in the interval.
Market, resource and reporting sweeps.The second protocol retains preferred plat-
forms 3 or 4 at every width. Intensities are drawn independently fromUnif[1 −a, 1]each
round, independently of UA actions: these are open-loop, not learning policies. Table 4
varies one parameter around(16,0.9,0.05), giving seven settings and 84 seeded runs.
Entrants do not improve the best resource, so the width sweep combines choice dilution
and verification effects. Increasinga also lowers mean intensity, not just widening its range.
Observed gains remain positive even when no finite budget is certified.
E.7. Alternative calibration with matched forgetting
We compare (5) with an affine gap predictor using matched forgetting, initialization and
score range. For one user–platform record, index verified consumptions bys = 1, . . . , k, with
35

Zheng et al.
Table 4: Observed net utility and theoretical guarantees in the controlled synthetic market at
T = 4096. The base is(n, h, a) = (16, 0.9, 0.05); other rows change one parameter.
Lower bounds are rounded down. All observed-net-gain interval half-widths are
below0 .0001over 12 seeds. A dash means no finite positive-gain budget is certified.
Setting
Calibrated
gain
Observed
net gain
Certified
lower bound
Certified
rounds
Base0.493 0.466 0.0941,465
n= 4 0.496 0.491 0.137357
n= 32 0.489 0.433 0.0363,034
h= 0.60 0.140 0.120−0.305—
h= 0.75 0.327 0.301−0.084—
a= 0 0.493 0.465 0.316582
a= 0.10 0.493 0.466−0.129—
reportsA s, gapsd s =A s −r s andρ= 1−η. Before its next consumption, fit
(ˆak, ˆbk)∈arg min a,b
(
ρka2 +η
kX
s=1
ρk−s(ds −a−bA s)2 +κb 2
)
, κ= 0.01.(64)
The score isA−clip [0,1](ˆak + ˆbkA), with zero initial coefficients and the same temperature
as EMA. Only the consumed record updates, at round end; unconsumed records do not
decay. Neither intensities nor the reporting formula are supplied, and regularization is fixed
in advance. Restrictingb = 0recovers the zero-initialized EMA exactly. The extension uses
the current report as a predictor, unlike lagged EMA.
Comparisons reuse the original resources and seeds. Fixed-policy comparisons share
actions; Exp3 populations learn separately under each UA. Tables 5 and 6 report paired
differences.
Table 5: Calibration in synthetic markets.
PA Mean 95% CI
Fixed4.94 [4.86,5.02]
Exp3−0.32 [−0.47,−0.16]
Restricted Exp322.82 [22.74,22.90]
Table 6: Calibration in Amazon markets.
PA Mean 95% CI
Fixed0.13 [0.11,0.15]
Exp3−0.29 [−0.32,−0.25]
Entries report affine gap calibration minus EMA utility in10−3 units; positive values favor affine calibration.
Both use matched forgetting, withm = 128, n = 16and T = 4096. CIs are paired pointwise 95% intervals
over 12 seeds. Fixed denotes heterogeneous fixed intensities; Exp3 uses the full action grid. Restricted Exp3
uses the controlled synthetic market. Amazon values use the semantic outcome proxy.
Neither update uniformly dominates. Affine calibration performs better under fixed
reporting and restricted Exp3; broad-market Exp3 slightly favors EMA. These comparisons
test sensitivity to predictor form, not optimality among all same-feedback methods.
36

User-Centered Agentic Recommendation
E.8. Observed ratings and outcome-model sensitivity
Observed-rating check.Using the same chronological split (timestamp ties enter the later
split), an existing diagnostic covers 130 test ratings from 58 eligible users. Training-profile
cosine, used because review-time queries are unobserved, has Spearman correlation0.101
with ratings, with interval[−0.117,0.265]. Restricting to unseen pairs in the 2,048-product
universe leaves 19 ratings from 15 users.
A broader cohort requires at least ten training ratings overall and three positive training
ratings within that universe; profiles use up to eight latest positives. Of 1,717 eligible users,
92 contribute 119 unseen test ratings. Correlation is−0.185, with interval[−0.349,− 0.006].
Both 95% intervals use 2,000 user-cluster bootstrap draws, conditional on frozen data and
representation. These sparse diagnostics are not new untouched tests or validation of
consumer satisfaction; missing ratings are not negative outcomes.
A separate rating-derived outcome proxy.We retain the Qwen catalogs, queries,
retrieval, candidatesandoriginalassignments, butreplacerelevancebyafrozen32-dimensional
biased matrix-factorization prediction, clipped to[0, 1]. The outcome model is trained on
training ratings and selected by validation RMSE; it is not a second recommendation-side
embedding. Reports, feedback, PA payoff and welfare all use the replacement. The UA sees
only consumed outcomes, not the predictor; the original platform is not reoptimized.
Results and scope.At n = 16, m = 128, T = 4096, ν = 0.1and η = 0.2, assessment
improves utility over uncorrected reports by0.00330under fixed reporting and0 .00225
under Exp3, with paired intervals[0 .00238, 0.00421]and[0 .00197, 0.00253]. Net gains
over the original platform are0.01314and0 .00858, with intervals[0.00679, 0.01949]and
[0.00238, 0.01477]. Correction benefits persist, but the positive net gains contrast with the
semantic-proxy results: their sign depends on the outcome model.
The rating proxy is not demonstrably better: its normalized RMSE on the complete warm-
start test split is0.2951, versus0 .2948for a bias-only model. Predictions are not observed
counterfactuals, and inherited product selection makes the two proxies non-independent
market samples. The data limitations in Appendix E.3 remain. The mechanism intervals
measure variability over 12 simulation seeds conditional on frozen data and models, not
uncertainty about real consumer welfare.
37
