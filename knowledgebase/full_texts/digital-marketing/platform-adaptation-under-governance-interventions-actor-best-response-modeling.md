---
title: 'Platform Adaptation Under Governance Interventions: Actor Best-Response Modeling and an External
  Public-Case Benchmark'
url: https://arxiv.org/abs/2608.15131
category: digital-marketing
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Wesley Shu
- Peng Wei
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.15131
pages: 21
chars: 59500
fetched_at: '2026-11-08T13:09:02+00:00'
kb_version: 1
---

# Platform Adaptation Under Governance Interventions: Actor Best-Response Modeling and an External Public-Case Benchmark

Platform Adaptation Under Governance Interventions: Actor
Best-Response Modeling and an External Public-Case Benchmark
Wesley Shu∗1 and Peng WEI †2
1The Institute of Energetic Paradigm
2College of Plant Protection, Southwest University
Abstract
Digital platforms govern by changing rules: rankings, monetization thresholds, moderation
standards, veriﬁcation systems, disclosure requirements, appeal processes, and access policies.
These interventions are rarely absorbed passively. Creators, sellers, advertisers, moderators,
users, developers, and strategic operators adapt to the new reward surface. This paper develops
a platform-adaptation model for evaluating governance interventions as transitions in adaptive
multi-actor information systems. The model represents actor best response, strategic gaming
opportunity, moderation burden, user-incentive movement, enforcement response, externality
formation, and downstream platform stability. We evaluate the model on 72 external public
platform-governance cases covering media monetization, ranking systems, veriﬁcation, delivery
platforms, marketplaces, app stores, community platforms, and creator ecosystems. Across 9
methods and 648 method-case evaluations, the full platform-adaptation simulator achieves mean
adaptation quality of 0.836338, compared with 0.669731 for a risk-register baseline, 0.589457
for causal-loop analysis, 0.492750 for generic governance critique, 0.369492 for engagement-only
optimization, and 0.331965 for baseline policy review. Paired comparisons show a win rate of 1.00
against all tested baselines and channel ablations. The contribution is an information-systems
theory and measurement framework showing why platform governance evaluation fails when it
treats policy rules as static controls rather than interventions into adaptive actor-response ﬁelds.
Keywords: platform governance; digital platforms; algorithmic management; actor adaptation;
moderation burden; strategic gaming; information systems; benchmark instrumentation.
1 Introduction
Digital platforms are governed through rules. A platform changes its ranking algorithm, adjusts
monetization eligibility, raises or lowers moderation thresholds, redesigns veriﬁcation, modiﬁes seller
requirements, restricts API access, alters app-store review practices, or introduces new appeal
procedures. In each case the rule is not merely a compliance text. It changes the reward surface
of the platform. Actors who depend on the platform observe the new constraints and incentives,
infer what is now rewarded or penalized, and alter their behavior. A rule that looks sensible at
∗Corresponding author: shu@energeticparadigm.org
†weipeng2019@swu.edu.cn
1
arXiv:2608.15131v1  [cs.AI]  15 Aug 2026

the moment of announcement can therefore produce a diﬀerent state after creators, sellers, users,
moderators, advertisers, developers, and strategic operators respond.
This adaptive response is not peripheral. It is the core control problem of platform governance.
A moderation rule changes the workload and ambiguity faced by moderators. A ranking rule
changes the strategies that creators and sellers use to become visible. A monetization threshold
changes the tradeoﬀ between compliance, opacity, and gaming. A veriﬁcation system changes
trust signals and impersonation incentives. A delivery-platform policy changes driver behavior,
customer expectations, and externalized cost. These responses can improve stability, but they can
also displace harm, create new loopholes, or increase the burden of enforcement.
Information-systems research is especially well positioned to study this problem because plat-
forms are socio-technical systems, not merely markets or software products. Platform governance
joins technical architecture, boundary resources, organizational control, algorithmic management,
complementor incentives, moderation work, and network externalities ( Tiwana, 2013; Gawer, 2014;
Eaton et al. , 2015; Wareham et al. , 2014; Henfridsson & Bygstad , 2013; Kellogg et al. , 2020). Yet
many governance-evaluation methods still reason as if the rule has a direct eﬀect on the outcome.
They ask whether a policy targets the right abuse, reduces a visible cost, improves an engagement
metric, or names the major risk. Those questions are necessary, but insuﬃcient. The missing
question is: what post-rule actor-response ﬁeld does the intervention create?
This paper develops and evaluates a platform-adaptation model for that question. The model
treats a governance intervention as a transition operator on a platform state. The immediate
policy action is only one component of the transition. The next state depends on actor best
responses, gaming opportunities, moderation burden, enforcement capacity, user incentives, ex-
ternalities, and stability consequences. The paper then evaluates whether methods recover these
transition mechanisms using an external public-case benchmark of 72 platform-governance episodes
and 648 method-case evaluations.
The paper makes four contributions. First, it provides a theoretical account of platform gov-
ernance as actor best-response transition control. Second, it formalizes platform adaptation con-
structs that connect governance interventions to downstream stability: gaming opportunity, mod-
eration burden, user incentive shift, enforcement response, externality risk, and platform-stability
consequences. Third, it introduces a reproducible external public-case benchmark for evaluating
whether governance methods identify these mechanisms. Fourth, it shows empirically that a full
platform-adaptation simulator outperforms baseline policy review, engagement-only optimization,
static cost-beneﬁt analysis, generic governance critique, causal-loop analysis, risk-register analysis,
and two ablated versions of the model.
The claim is bounded. The benchmark is grounded in public platform-governance cases; it is
not a private ﬁeld experiment, private platform-log analysis, or deployed policy intervention. It
therefore does not claim exact prediction of platform outcomes. It evaluates a more speciﬁc and
practically important capability: whether a governance-evaluation method can identify the actor
adaptation channels and downstream platform-stability consequences that a static policy review
tends to miss.
2

2 Theoretical Background
2.1 Digital platforms as governed socio-technical systems
Digital platforms coordinate interactions among multiple actor groups through technical architec-
ture, rules, interfaces, algorithms, boundary resources, and economic incentives ( Tiwana, 2013;
Ghazawneh & Henfridsson , 2013; Eaton et al. , 2015; Ceccagnoli et al. , 2012; Wareham et al. , 2014).
They are not only two-sided markets; they are governed information infrastructures whose sta-
bility depends on participation, complementor investment, user trust, enforcement capacity, and
the continuous management of externalities ( Parker & Van Alstyne , 2005; Rochet & Tirole , 2003;
Eisenmann et al. , 2006; de Reuver et al. , 2018).
The platform literature has emphasized the tension between openness and control. Openness
supports innovation, complementor entry, and network eﬀects, but it also increases coordination
diﬃculty, quality variance, and governance burden ( Boudreau, 2010, 2012; Benlian et al. , 2015;
Gawer & Cusumano , 2014). Control can reduce abuse and preserve quality, but it can also reduce
participation or shift costs to dependent actors. This tension is dynamic because platform actors
adapt to the governance regime. Boundary resources, APIs, ranking systems, moderation standards,
and monetization policies become objects of strategic interpretation and optimization ( Ghazawneh
& Henfridsson , 2013; Eaton et al. , 2015; Tiwana et al. , 2010).
2.2 Algorithmic management and rule-mediated control
Algorithmic management research shows that digital control is often mediated through rankings,
scores, ratings, incentives, task allocation, visibility, and automated enforcement ( Lee et al. , 2015;
Kellogg et al. , 2020; Mohlmann & Zalmanson , 2017; Rosenblat & Stark , 2016; Wood et al. , 2019).
These controls are powerful because they govern behavior at scale. They are also contested because
actors learn the system, interpret its signals, and adapt under uncertainty. Platform governance
therefore operates through a feedback relation: the platform modiﬁes rules, actors learn and re-
spond, the platform observes consequences, and governance is revised again.
This feedback relation diﬀers from a conventional policy-eﬀect view. In a static view, the rule
is the cause and the observed outcome is the eﬀect. In an adaptive view, the rule changes the
incentive environment; actors choose responses; their responses interact; and the observed outcome
is a post-response equilibrium or disequilibrium. A platform rule can therefore fail even when it
correctly identiﬁes the original problem.
2.3 Governance failure as adaptation failure
Platform governance failure often appears as a mismatch between intended rule eﬀect and realized
post-response behavior. A rule intended to reduce low-quality content may lead creators to optimize
for permissible but low-value signals. A monetization threshold intended to reward reliability may
shift strategic eﬀort toward threshold gaming. A veriﬁcation rule intended to increase trust may
create new impersonation incentives. A marketplace ranking change intended to improve relevance
may increase seller manipulation. A moderation rule intended to reduce harm may increase appeal
burden and reduce enforcement consistency.
3

These failures share a common structure. The governance method evaluates the policy against
the current state, but the platform actually operates in the state produced after actor adaptation.
The relevant unit of analysis is therefore not only policy quality, but transition quality. A useful
platform-governance method should estimate whether a rule moves the platform toward a stable
post-response state.
3 Theory Development
3.1 Core constructs
We deﬁne six constructs for platform-adaptation evaluation.
Actor best response is the expected behavioral adjustment of a platform actor after a gov-
ernance intervention. Actors include creators, sellers, developers, advertisers, moderators, users,
workers, and strategic adversaries. Best response does not imply perfect rationality; it denotes the
directional adaptation that becomes locally attractive under the new rule.
Gaming opportunity is the extent to which the intervention creates proﬁtable loopholes,
metric substitutions, evasive strategies, or new optimization targets. Gaming opportunity is high
when actors can preserve beneﬁts while avoiding the intended constraint.
Moderation burden is the enforcement, review, ambiguity, appeals, and operational load that
the intervention shifts onto human or automated moderation systems. It includes both volume and
complexity.
User-incentive shift is the expected movement in user attention, trust, reporting, switching,
or participation behavior after the rule changes.
Externality formation is the creation or displacement of costs outside the actor who beneﬁts
from the rule response. Examples include user harm, seller crowding, creator instability, labor
burden, misinformation spillovers, and reduced trust.
Platform stability is the downstream condition of the platform after actor response, enforce-
ment response, and externality formation. It is not equivalent to engagement. Engagement can
rise while stability falls.
3.2 Propositions
Proposition 1 (Actor-response gap). A governance-evaluation method that scores only the policy’s
stated intent and immediate target will systematically overestimate policy quality when the rule
creates proﬁtable post-rule actor responses that are not represented in the evaluation.
Proposition 2 (Gaming displacement) . When a policy constrains a visible behavior but leaves
an adjacent reward path open, strategic actors will tend to shift eﬀort toward the adjacent path,
producing apparent compliance with reduced platform stability.
Proposition 3 (Moderation-burden relocation) . A governance intervention can reduce visible
abuse while increasing moderation ambiguity, appeal load, or enforcement inconsistency. Such in-
terventions can degrade platform stability even when the primary abuse metric improves.
4

Proposition 4 (Engagement-instability divergence). Engagement metrics can move in the opposite
direction from platform stability when the rule increases attention while also increasing gaming,
externality cost, or participant mistrust.
Proposition 5 (Adaptive control advantage). A method that jointly represents actor best response,
gaming opportunity, moderation burden, enforcement response, externality formation, and stability
consequences will recover platform-adaptation quality more accurately than methods that represent
only visible policy costs, engagement movement, causal loops, or listed risks.
4 Mechanism Logic: From Rule Change to Platform State
4.1 Incentive reorientation
The ﬁrst mechanism is incentive reorientation. Platform rules do not merely permit or prohibit be-
havior; they change the relative payoﬀ of observable strategies. A creator who previously optimized
for volume may shift toward advertiser-safe language, a seller may shift toward ranking-compatible
inventory signals, and a developer may shift toward whichever boundary resource remains available
after an access-policy change. The relevant question is not whether the actor agrees with the rule,
but whether the rule makes a new strategy attractive enough to be adopted. This is why a gover-
nance intervention must be evaluated as a change in the incentive ﬁeld rather than as an isolated
compliance statement.
Incentive reorientation is especially important for digital platforms because the platform often
governs through algorithmic visibility and access rather than direct command. The actor does
not need full knowledge of the algorithm to adapt. Partial observability is enough. Once actors
infer that a signal is rewarded, they experiment, imitate, and diﬀuse tactics. The post-rule state is
therefore shaped by learning and imitation as much as by formal policy.
4.2 Gaming and adjacent substitution
The second mechanism is adjacent substitution. A rule may close one route while leaving a neigh-
boring route open. When actors can preserve beneﬁts by moving to an adjacent tactic, the rule may
produce apparent compliance without reducing the underlying instability. This is common in rank-
ing systems, recommendation systems, seller markets, creator monetization, review systems, and
veriﬁcation regimes. The platform sees the targeted behavior decline, but the strategic objective
survives in a new form.
Adjacent substitution is why static policy review is structurally weak. A static review asks
whether the targeted behavior is addressed. An adaptation review asks whether the actor objective
has been neutralized, displaced, or made harder to detect. The distinction matters because many
platforms have limited visibility into the full actor response space. A rule that reduces one visible
abuse channel may increase the value of a less visible channel, thereby shifting enforcement cost
into a region where moderation is slower or less consistent.
5

4.3 Moderation burden as endogenous cost
The third mechanism is moderation-burden relocation. Many governance interventions create work.
They generate appeals, ambiguous edge cases, borderline classiﬁcations, manual review queues, user
reports, and consistency problems. This burden is not merely an implementation cost; it changes
the stability of the platform. A rule that cannot be enforced consistently may teach actors that
the enforcement regime is noisy. A rule that creates high appeal burden may slow resolution and
damage trust. A rule that requires diﬃcult interpretation may produce inconsistent treatment
across user groups or domains.
Treating moderation burden as endogenous changes the evaluation problem. The platform can-
not evaluate only whether the rule is normatively desirable or whether it targets the right category
of harm. It must evaluate whether the enforcement system can carry the burden generated by the
actor-response ﬁeld. If moderation capacity is below the burden created by the rule, the governance
intervention can create instability even when its policy intent is sound.
4.4 Externality displacement
The fourth mechanism is externality displacement. Platforms often reduce one cost by moving it
to another actor group. A seller-policy change can reduce buyer risk while increasing seller compli-
ance cost. A monetization rule can increase advertiser conﬁdence while increasing creator income
volatility. A ranking change can improve user relevance while increasing strategic manipulation
among creators. A veriﬁcation policy can reduce friction for some legitimate actors while increas-
ing impersonation risk elsewhere. The platform-level outcome depends on whether the displaced
cost is absorbed, ampliﬁed, or converted into distrust.
Externality displacement is central to information-systems theory because it shows that the plat-
form is a coupled socio-technical system. A local optimization does not remain local. Costs move
through technical architecture, market incentives, user expectations, and organizational processes.
A useful evaluation method must therefore ask who pays for the intervention, who learns to exploit
it, and which group exits, reduces participation, or changes behavior as a result.
4.5 Stability as post-response viability
The ﬁfth mechanism is post-response viability. Platform stability is not the same as policy com-
pliance, engagement, or short-term metric improvement. Stability means that the platform can
continue to coordinate actor groups without excessive gaming, externality accumulation, modera-
tion overload, or trust erosion. A stable rule may reduce engagement in the short term if it removes
low-quality incentives. An unstable rule may increase engagement by rewarding conﬂict, attention
gaming, or strategic participation.
This distinction motivates the benchmark’s primary metric. Overall platform-adaptation quality
rewards methods that identify the transition mechanisms shaping the post-response state. The
score is not designed to reward rhetorical sophistication. It rewards accurate identiﬁcation of who
adapts, how gaming becomes proﬁtable, where moderation burden moves, what externalities form,
how enforcement responds, and whether the downstream state is stable.
6

5 Platform-Adaptation Model
Let et denote the platform state before a governance intervention. Let at denote the intervention,
such as a ranking change, monetization rule, moderation threshold, veriﬁcation policy, seller re-
quirement, API rule, or appeal procedure. Let I denote the set of platform actor groups. For actor
group i ∈ I , the post-rule response is represented as
Bi,t+1 = BRi(at, et; Gt, Mt, Ut, Xt, Et),
where Gt is gaming opportunity, Mt is moderation burden, Ut is user-incentive movement, Xt is
externality risk, and Et is enforcement response. The next platform state is
et+1 = F (et, at, B1,t+1, . . . , Bn,t+1, Gt, Mt, Ut, Xt, Et, ϵt).
Platform stability is scored as a downstream state property:
Splatf orm = WuUuser + WcUcreator + WpUplatf orm − Cgaming − Cexternality − Cmoderation − Dinstability.
This representation is intentionally operational. It does not assume that all platform consequences
can be reduced to a single utility function. Instead, it forces the evaluation method to state which
response channels are expected to change and how those changes aﬀect stability.
5.1 Evaluation algorithm
1. Identify the governance intervention and aﬀected actor groups.
2. Encode the pre-intervention platform state: dependency, visibility, enforcement capacity, mod-
eration ambiguity, and externality exposure.
3. Estimate actor best responses under the new rule.
4. Estimate gaming opportunity, moderation burden, user-incentive movement, enforcement re-
sponse, and externality formation.
5. Score the expected post-response platform state.
6. Compare the score against baseline governance methods under the locked rubric.
6 Research Design
6.1 External public-case benchmark
The benchmark contains 72 external public cases. Each case is grounded in a public platform-
governance episode and combines a source episode with a policy-change type such as ranking
change, monetization rule, moderation threshold, veriﬁcation policy, marketplace rule, app-store
access rule, or appeal process. The benchmark covers media monetization, media ranking, social
7

Governance Intervention → Actor Incentive Shift → Best Responses
↓
Gaming Opportunity Moderation Burden User Incentives Enforcement
Response
↓
Externality F ormation → Post-Response Platform Stability
Figure 1: Platform-adaptation evaluation pipeline. A governance intervention is evaluated by its post-
response transition, not only by its stated target.
veriﬁcation, delivery platforms, digital marketplaces, marketplace ranking, community platforms,
creator platforms, and related platform-governance domains.
The benchmark does not use synthetic cases for the main empirical claim. Public sources pro-
vide the episode grounding, while the locked rubric speciﬁes what counts as accurate adaptation
reasoning. The source manifest is included in the package. The full appendix summarizes the 72
cases by domain, policy type, expected best response, and expected failure mode.
6.2 Compared methods
Nine methods are evaluated: baseline platform-policy review, engagement-only optimizer, generic
governance critique, static cost-beneﬁt review, risk-register baseline, causal-loop baseline, platform-
adaptation simulator without the strategic-gaming channel, platform-adaptation simulator without
the moderation-burden channel, and the full platform-adaptation simulator. The set intention-
ally includes both weak and strong baselines. The risk-register baseline is important because it
represents a plausible governance practice: naming hazards and mitigations. The causal-loop base-
line is important because it represents feedback reasoning without the full actor-response channel
structure.
6.3 Rubric and scoring
Each method-case output is scored on creator-adaptation accuracy, moderation-burden accuracy,
user-incentive accuracy, engagement-dynamics accuracy, strategic-gaming accuracy, externality-
prediction accuracy, enforcement-response accuracy, platform-stability accuracy, overall platform-
adaptation quality, and control eﬃciency. The primary metric is mean overall platform-adaptation
quality. Secondary metrics diagnose which channels produce diﬀerences among methods.
Construct validity is protected by three design choices. First, the rubric separates adaptation
channels rather than collapsing all quality into a vague governance score. Second, ablations remove
individual channels, allowing the test to identify whether strategic gaming and moderation burden
add explanatory power. Third, paired comparisons evaluate within-case diﬀerences, reducing the
risk that method rankings are artifacts of case mix.
8

6.4 Case construction and source grounding
The external cases were constructed to avoid two common weaknesses in platform-governance evalu-
ation. The ﬁrst weakness is purely synthetic scenario design, where the researcher controls both the
case and the expected answer. The second weakness is anecdotal case selection, where examples
are chosen because they ﬁt the preferred theory. The benchmark instead uses public platform-
governance episodes and converts them into repeated policy-change instances under a ﬁxed case
schema. Each row includes a public source basis, domain, policy-change type, adaptation shock,
actor-dependency indicators, moderation burden, gaming opportunity, externality risk, enforcement
probability, expected best response, and expected failure mode.
The purpose of this design is not to claim that public cases provide the same evidentiary depth
as internal platform logs. They do not. The purpose is to create an externally grounded test
bed where multiple governance-evaluation methods face the same cases, same rubric, same scoring
dimensions, and same validation script. This makes the comparison reproducible. It also makes
the claim falsiﬁable: if a method cannot recover expected adaptation channels in public cases, it is
unlikely to be reliable in more complex private operational settings.
6.5 Why the baseline set matters
The baseline set is chosen to represent distinct governance logics. Baseline policy review represents
the minimal static interpretation of a platform rule. Engagement-only optimization represents the
common managerial error of treating visible attention as policy success. Static cost-beneﬁt review
represents a more formal but still comparatively non-adaptive evaluation style. Generic governance
critique represents broad concern without mechanism-speciﬁc transition modeling. Causal-loop
analysis represents feedback awareness. Risk-register analysis represents structured hazard naming.
The two ablations test whether the full model’s advantage depends speciﬁcally on strategic-gaming
and moderation-burden channels.
This structure creates a ladder of increasingly sophisticated governance reasoning. If the full
model only outperformed the weakest baseline, the result would be uninteresting. The key result is
that the full model outperforms risk-register analysis, causal-loop analysis, and channel ablations.
That pattern suggests that the advantage is not simply more words, more caution, or more feedback
language. It comes from representing the coupled transition from rule change to actor response to
platform state.
6.6 Statistical treatment
The benchmark reports aggregate means, bootstrap 95 percent conﬁdence intervals using 2,000
resamples, paired diﬀerences, paired t statistics, domain summaries, and failure analysis. The
package includes row-level method scores, action scores, bootstrap intervals, source manifest, do-
main summary, failure analysis, runner, and validator.
9

7 Results
7.1 Aggregate results
Table 1 reports the main aggregate benchmark results. The full platform-adaptation simulator
achieves the highest overall platform-adaptation quality and the highest scores on creator adapta-
tion, strategic gaming, moderation burden, and platform-stability accuracy.
Table 1: External public-case benchmark aggregate results.
Method Cases Overall Creator Gaming Moderation Stability
Full platform-adaptation simulator 72 0.836338 0.857607 0.856807 0.854240 0.793115
No moderation-burden channel 72 0.729647 0.827756 0.826956 0.610945 0.549820
No strategic-gaming channel 72 0.716135 0.827179 0.590129 0.823813 0.526438
Risk-register baseline 72 0.669731 0.641012 0.713245 0.732419 0.651604
Causal-loop baseline 72 0.589457 0.597036 0.561924 0.586646 0.592449
Generic governance critique 72 0.492750 0.485318 0.467397 0.500529 0.501272
Static cost-beneﬁt review 72 0.440505 0.432070 0.399090 0.475792 0.450715
Engagement-only optimizer 72 0.369492 0.441623 0.240894 0.311165 0.280944
Baseline policy review 72 0.331965 0.334886 0.300503 0.367864 0.327728
The full model outperforms the risk-register baseline by 0.166607 mean quality points and the
causal-loop baseline by 0.246881. The gap against engagement-only optimization is 0.466846. This
ﬁnding supports the proposition that visible engagement is not a reliable substitute for platform-
stability evaluation.
7.2 Paired comparisons
Table 2 reports paired comparisons. The full model wins every paired comparison over the listed
baselines and ablations across all 72 cases.
Table 2: Paired comparisons against the full platform-adaptation simulator.
Comparison Mean gain Win rate t statistic Min Max
Full model vs baseline platform policy review 0.504374 1.00 668.16 0.489055 0.517360
Full model vs engagement only optimizer 0.466846 1.00 667.45 0.451755 0.478433
Full model vs generic governance critique 0.343588 1.00 467.26 0.331810 0.355264
Full model vs static cost beneﬁt 0.395834 1.00 601.01 0.382143 0.405996
Full model vs risk register baseline 0.166607 1.00 290.94 0.155235 0.177158
Full model vs causal loop baseline 0.246881 1.00 385.59 0.234569 0.258390
Full model vs ep no gaming channel 0.120203 1.00 102.71 0.098762 0.139968
Full model vs ep no moderation channel 0.106691 1.00 88.88 0.085414 0.122510
The ablation results are theoretically informative. Removing the strategic-gaming channel re-
duces quality by 0.120203. Removing the moderation-burden channel reduces quality by 0.106691.
These are not cosmetic features. They are core mechanisms through which governance interventions
succeed or fail.
7.3 Bootstrap conﬁdence intervals
The full model’s conﬁdence interval is separated from those of the risk-register baseline, causal-
loop baseline, generic governance critique, static cost-beneﬁt review, engagement-only optimizer,
10

Table 3: Bootstrap 95 percent conﬁdence intervals for overall platform-adaptation quality.
Method Mean 95 percent CI
Full platform-adaptation simulator 0.836338 [0.834914, 0.837822]
No moderation-burden channel 0.729647 [0.726655, 0.732904]
No strategic-gaming channel 0.716135 [0.713204, 0.718859]
Risk-register baseline 0.669731 [0.668365, 0.671116]
Causal-loop baseline 0.589457 [0.588078, 0.590901]
Generic governance critique 0.492750 [0.491057, 0.494391]
Static cost-beneﬁt review 0.440505 [0.439047, 0.441987]
Engagement-only optimizer 0.369492 [0.367944, 0.371069]
Baseline policy review 0.331965 [0.330286, 0.333587]
and baseline policy review. The intervals are also separated from the two channel ablations.
7.4 Domain-level results
Table 4: Domain-level performance summary.
Domain Full model Risk register Causal loop Engagement only
community platform 0.836131 0.672008 0.586358 0.375220
creator monetization 0.834768 0.669516 0.589766 0.369750
creator platform 0.835802 0.670249 0.589864 0.371126
delivery platform 0.837464 0.670163 0.583123 0.371292
digital marketplace 0.841829 0.670968 0.589935 0.370444
marketplace ranking 0.836930 0.669234 0.589348 0.368711
media monetization 0.829034 0.666352 0.585832 0.370427
media ranking 0.837550 0.668010 0.591326 0.371851
mobile ecosystem 0.832219 0.664655 0.589514 0.366041
mobile marketplace 0.836762 0.671350 0.590495 0.371385
mobility platform 0.837237 0.667588 0.590559 0.370079
publishing platform 0.841213 0.672467 0.591953 0.370432
reviews marketplace 0.838604 0.669899 0.590066 0.367415
search ranking 0.840229 0.669545 0.589208 0.366771
short-video ranking 0.830849 0.666594 0.588132 0.371018
social incentives 0.832426 0.673250 0.585644 0.368829
social moderation 0.835928 0.668447 0.591484 0.365599
social ranking 0.838466 0.675541 0.595645 0.367728
social veriﬁcation 0.835143 0.670228 0.591920 0.369624
travel marketplace 0.834311 0.667766 0.587547 0.367845
The domain results show that the full model’s advantage is not driven by a single platform type.
The same mechanism appears across creator monetization, media ranking, marketplaces, delivery
platforms, community governance, and other platform settings.
8 Construct Validity and Robustness
A benchmark for platform governance must answer a construct-validity question: why does the
score measure platform adaptation rather than general rhetorical quality? The rubric addresses
this problem by assigning separate scores to observable adaptation channels. A method can receive
credit for naming a risk without receiving credit for identifying actor best response. It can receive
credit for describing engagement eﬀects without receiving credit for strategic-gaming prediction.
It can receive credit for describing a moderation rule without receiving credit for anticipating
11

moderation burden. This separation matters because governance failure often arises when one
visible policy target improves while another hidden channel deteriorates.
The comparison design also protects against false conﬁdence. The risk-register baseline is not
a straw man; it performs better than generic governance critique, static cost-beneﬁt analysis,
engagement-only optimization, and baseline policy review. The causal-loop baseline is also mean-
ingful because it captures feedback reasoning. The full model’s advantage over these baselines
therefore indicates that actor best response, gaming, moderation burden, enforcement response,
and externality channels add measurement value beyond generic caution or feedback language.
The limitations are equally important. Public cases provide credible external grounding, but they
do not provide private platform logs or controlled deployment outcomes. The locked rubric improves
reproducibility, but future work should add independent expert annotation, inter-rater reliability,
and prospective validation on new governance interventions. The current evidence supports method-
level construct recovery, not exact forecasting of future platform outcomes.
9 Theoretical Contributions to Information Systems Research
This paper contributes to information-systems research in three ways.
First, it reframes platform governance as adaptive transition control. Prior platform research
emphasizes openness, complementor participation, boundary resources, architecture, and gover-
nance mechanisms ( Tiwana, 2013; Eaton et al. , 2015; Ghazawneh & Henfridsson , 2013; Wareham
et al. , 2014). This paper adds a transition-centered account: governance interventions should be
evaluated by the post-rule actor-response ﬁeld they create. The rule is not the end of governance;
it is the beginning of adaptation.
Second, it distinguishes platform stability from engagement and immediate policy ﬁt. IS research
has long recognized that technology eﬀects are enacted through organizational and social structures
(Orlikowski, 1992; Markus & Silver , 2008; Yoo et al. , 2010). In platform settings, the same prin-
ciple means that engagement, compliance, or visible risk reduction can be misleading if they are
not evaluated alongside gaming opportunity, externality formation, and moderation burden. The
empirical results show that engagement-only optimization performs poorly on adaptation quality.
Third, it introduces a reproducible measurement framework for platform-governance adaptation.
Platform-governance research often relies on case interpretation, legal analysis, or economic model-
ing. Those approaches remain essential. The present benchmark adds a complementary instrument:
a locked rubric and external public-case dataset for comparing methods on their ability to recover
actor-response mechanisms.
10 Managerial Implications
The ﬁndings have practical implications for platform governance teams.
First, policy review should include an explicit actor-response map. Before deploying a ranking,
monetization, moderation, veriﬁcation, or marketplace rule, the platform should ask which actor
groups gain or lose, what responses become proﬁtable, and what new signals will be optimized.
12

Second, platforms should treat moderation burden as a primary design variable. A rule that
appears eﬀective but increases ambiguity, appeal volume, or enforcement inconsistency may reduce
long-term stability.
Third, engagement should not be used as a suﬃcient proxy for governance success. Engagement
can rise because actors exploit a rule, because controversy increases attention, or because quality
deterioration has not yet reached the switching threshold. Platform stability requires a broader
measure.
Fourth, risk registers should be connected to transition mechanisms. Naming a risk is not
equivalent to modeling how the risk emerges after actors respond. The benchmark shows that
risk-register reasoning is useful but incomplete.
Finally, platform teams should use pre-deployment simulation and post-deployment audit to-
gether. Simulation can identify likely adaptation channels, while audit can test whether predicted
responses actually occurred.
11 Discussion
11.1 Why risk registers help but do not solve adaptation
The risk-register baseline is the strongest conventional baseline in the benchmark. This is substan-
tively meaningful. Risk registers force analysts to name hazards and mitigations, and this improves
over generic policy review. However, the benchmark shows that risk naming is not equivalent to
adaptation modeling. A risk register can identify that gaming, moderation burden, or user trust
may be concerns, but it may not specify how a rule creates a proﬁtable response path, how that
response shifts enforcement load, or how externalities accumulate across actor groups.
The diﬀerence is between listing risks and modeling transitions. A list can be correct but
incomplete if it does not represent the control mechanism by which the risk emerges. In platform
governance, the mechanism is usually not a single failure point. It is a coupled sequence: a rule
changes incentives, actors adapt, moderation burden moves, enforcement responds, externalities
form, and the platform stabilizes or destabilizes. The full model outperforms the risk-register
baseline because it is organized around this sequence.
11.2 Why engagement is a dangerous governance proxy
The engagement-only optimizer performs poorly because engagement can be produced by stability
or instability. User attention may increase when the platform improves relevance, but it may also
increase when conﬂict, sensationalism, manipulation, or controversy rises. A policy that increases
engagement can still damage long-term trust, creator quality, moderation capacity, or ecosystem
resilience. This result is not a rejection of engagement metrics. It is a rejection of engagement as
a suﬃcient governance proxy.
For platform managers, the implication is direct. Engagement should be interpreted together
with adaptation indicators. If engagement rises while gaming opportunity, moderation burden,
appeal volume, or externality risk also rise, the platform may be harvesting short-term attention
13

at the expense of longer-term stability. The benchmark’s poor engagement-only results formalize
this intuition in a reproducible evaluation setting.
11.3 From policy evaluation to transition design
The broader theoretical implication is that platform governance should move from policy evaluation
to transition design. Policy evaluation asks whether a rule is well motivated. Transition design
asks what state the platform will enter after actors respond. This diﬀerence shifts managerial
attention from rule text to response architecture. It encourages platform teams to ask how actors
will learn the rule, which signals they will optimize, what ambiguity moderators must resolve, and
how externalities will propagate.
Transition design also clariﬁes why governance is iterative. A platform cannot eliminate adap-
tation. It can design rules whose adaptation paths are less harmful, easier to observe, and easier
to correct. The goal is not static control, but stable feedback: detect response, identify gaming,
adjust enforcement, and preserve ecosystem value across actor groups.
12 Boundary Conditions and Limitations
The paper’s evidence is externally grounded but bounded. The benchmark uses public platform-
governance cases rather than private operational logs. It evaluates whether methods identify ex-
pected adaptation mechanisms under a locked rubric; it does not claim causal identiﬁcation of
real-world treatment eﬀects. The cases cover multiple platform domains, but they do not exhaust
all platform types, jurisdictions, or cultural settings. The method should be further tested on
prospective interventions, private platform data, expert-coded cases, and longitudinal policy out-
comes.
The benchmark also relies on method outputs generated under a structured evaluation protocol.
Strong human analysts using a risk register or causal-loop analysis could perform better than
automated or standardized versions of those baselines. This is why the claim is not that risk
registers or causal loops are useless. The claim is that platform governance evaluation improves
when those tools are embedded in a model of actor best response, gaming opportunity, moderation
burden, enforcement response, externality formation, and downstream stability.
13 Conclusion
Platform governance is an adaptive control problem. Rules change incentives; actors adapt; and the
platform’s downstream state depends on the coupled response ﬁeld that emerges after the interven-
tion. This paper develops a platform-adaptation model and evaluates it on 72 external public cases
across 9 methods and 648 method-case scores. The full platform-adaptation simulator outperforms
baseline policy review, engagement-only optimization, static cost-beneﬁt analysis, generic gover-
nance critique, causal-loop analysis, risk-register analysis, and two channel ablations. The evidence
supports a bounded but important claim: governance evaluation is stronger when it models actor
best response, strategic gaming, moderation burden, user-incentive shifts, enforcement response,
externality formation, and platform-stability consequences as coupled transition mechanisms.
14

Data and Code A vailability
The complete reproducibility artifact for this study combines the benchmark evidence and sup-
porting source materials into a single public archive. It contains the 72 external public platform-
governance cases, platform-adaptation rubric, source manifest, benchmark runner, validator, row-
level method scores, action scores, aggregate results, bootstrap conﬁdence intervals, paired compar-
isons, domain summaries, failure analysis, veriﬁcation metadata, shared schemas, construct-validity
documentation, and SHA-256 manifest. No synthetic cases are used as the main evidence layer.
The complete archive is permanently available on Zenodo at DOI: 10.5281/zenodo.21945303.
15

A Coding Rubric and Validation Protocol
Rubric dimension Operational meaning
Creator adaptation ac-
curacy
Identiﬁes how creators, sellers, developers, workers, or other
supply-side actors adapt to the intervention.
Moderation-burden ac-
curacy
Identiﬁes review volume, ambiguity, appeal burden, enforcement
inconsistency, or operational moderation load created by the rule.
User-incentive accu-
racy
Identiﬁes changes in user trust, attention, participation, switching,
reporting, or consumption incentives.
Engagement-dynamics
accuracy
Distinguishes visible engagement movement from stability-
enhancing platform outcomes.
Strategic-gaming accu-
racy
Identiﬁes loopholes, metric gaming, evasion, or optimization paths
created by the rule.
Externality-prediction
accuracy
Identiﬁes displaced costs, harms, trust erosion, ecosystem instabil-
ity, or burden shifted to non-beneﬁting actors.
Enforcement-response
accuracy
Identiﬁes how the platform can or cannot enforce the rule under
realistic capacity and observability constraints.
Platform-stability ac-
curacy
Estimates whether the post-response platform state is more or less
stable after coupled actor responses.
Overall adaptation
quality
Integrates the channel scores into the primary benchmark metric.
Control eﬃciency Measures whether the method identiﬁes high-leverage control
points without unnecessary governance complexity.
B External Public-Case Summary
Table 6: Summary of the 72 external public benchmark cases. The evidence package contains full source
URLs and row-level scores.
Case Domain Policy type Expected best response Expected failure mode
p15_ext_001 media monetization ranking_change loophole_search incentive_gaming
p15_ext_002 media monetization monetization_rule strategic_reoptimization moderation_backlog
p15_ext_003 media monetization moderation_threshold strategic_reoptimization moderation_backlog
p15_ext_004 media ranking ranking_change strategic_reoptimization incentive_gaming
p15_ext_005 media ranking monetization_rule strategic_reoptimization moderation_backlog
p15_ext_006 media ranking moderation_threshold strategic_reoptimization incentive_gaming
p15_ext_007 social veriﬁcation ranking_change strategic_reoptimization engagement_gain_stability_loss
p15_ext_008 social veriﬁcation monetization_rule strategic_reoptimization engagement_gain_stability_loss
p15_ext_009 social veriﬁcation moderation_threshold compliance_and_workaround moderation_backlog
p15_ext_010 social moderation ranking_change compliance_and_workaround incentive_gaming
p15_ext_011 social moderation monetization_rule strategic_reoptimization incentive_gaming
p15_ext_012 social moderation moderation_threshold strategic_reoptimization moderation_backlog
p15_ext_013 social ranking ranking_change strategic_reoptimization moderation_backlog
p15_ext_014 social ranking monetization_rule strategic_reoptimization incentive_gaming
p15_ext_015 social ranking moderation_threshold strategic_reoptimization engagement_gain_stability_loss
p15_ext_016 social incentives ranking_change strategic_reoptimization engagement_gain_stability_loss
p15_ext_017 social incentives monetization_rule strategic_reoptimization moderation_backlog
p15_ext_018 social incentives moderation_threshold compliance_and_workaround moderation_backlog
p15_ext_019 short-video ranking ranking_change loophole_search incentive_gaming
p15_ext_020 short-video ranking monetization_rule strategic_reoptimization moderation_backlog
p15_ext_021 short-video ranking moderation_threshold strategic_reoptimization incentive_gaming
16

Case Domain Policy type Expected best response Expected failure mode
p15_ext_022 community platform ranking_change strategic_reoptimization incentive_gaming
p15_ext_023 community platform monetization_rule strategic_reoptimization engagement_gain_stability_loss
p15_ext_024 community platform moderation_threshold strategic_reoptimization engagement_gain_stability_loss
p15_ext_025 mobile ecosystem ranking_change strategic_reoptimization incentive_gaming
p15_ext_026 mobile ecosystem monetization_rule strategic_reoptimization incentive_gaming
p15_ext_027 mobile ecosystem moderation_threshold compliance_and_workaround moderation_backlog
p15_ext_028 mobile marketplace ranking_change compliance_and_workaround moderation_backlog
p15_ext_029 mobile marketplace monetization_rule strategic_reoptimization incentive_gaming
p15_ext_030 mobile marketplace moderation_threshold strategic_reoptimization moderation_backlog
p15_ext_031 mobile marketplace ranking_change strategic_reoptimization engagement_gain_stability_loss
p15_ext_032 mobile marketplace monetization_rule strategic_reoptimization engagement_gain_stability_loss
p15_ext_033 mobile marketplace moderation_threshold strategic_reoptimization moderation_backlog
p15_ext_034 marketplace ranking ranking_change strategic_reoptimization incentive_gaming
p15_ext_035 marketplace ranking monetization_rule strategic_reoptimization moderation_backlog
p15_ext_036 marketplace ranking moderation_threshold compliance_and_workaround incentive_gaming
p15_ext_037 mobility platform ranking_change loophole_search incentive_gaming
p15_ext_038 mobility platform monetization_rule strategic_reoptimization moderation_backlog
p15_ext_039 mobility platform moderation_threshold strategic_reoptimization engagement_gain_stability_loss
p15_ext_040 delivery platform ranking_change strategic_reoptimization engagement_gain_stability_loss
p15_ext_041 delivery platform monetization_rule strategic_reoptimization incentive_gaming
p15_ext_042 delivery platform moderation_threshold strategic_reoptimization moderation_backlog
p15_ext_043 marketplace ranking ranking_change strategic_reoptimization moderation_backlog
p15_ext_044 marketplace ranking monetization_rule strategic_reoptimization incentive_gaming
p15_ext_045 marketplace ranking moderation_threshold compliance_and_workaround moderation_backlog
p15_ext_046 marketplace ranking ranking_change compliance_and_workaround incentive_gaming
p15_ext_047 marketplace ranking monetization_rule strategic_reoptimization engagement_gain_stability_loss
p15_ext_048 marketplace ranking moderation_threshold strategic_reoptimization engagement_gain_stability_loss
p15_ext_049 travel marketplace ranking_change strategic_reoptimization incentive_gaming
p15_ext_050 travel marketplace monetization_rule strategic_reoptimization moderation_backlog
p15_ext_051 travel marketplace moderation_threshold strategic_reoptimization incentive_gaming
p15_ext_052 search ranking ranking_change strategic_reoptimization incentive_gaming
p15_ext_053 search ranking monetization_rule strategic_reoptimization moderation_backlog
p15_ext_054 search ranking moderation_threshold compliance_and_workaround moderation_backlog
p15_ext_055 reviews marketplace ranking_change loophole_search engagement_gain_stability_loss
p15_ext_056 reviews marketplace monetization_rule strategic_reoptimization engagement_gain_stability_loss
p15_ext_057 reviews marketplace moderation_threshold strategic_reoptimization moderation_backlog
p15_ext_058 reviews marketplace ranking_change strategic_reoptimization moderation_backlog
p15_ext_059 reviews marketplace monetization_rule strategic_reoptimization incentive_gaming
p15_ext_060 reviews marketplace moderation_threshold strategic_reoptimization moderation_backlog
p15_ext_061 digital marketplace ranking_change strategic_reoptimization incentive_gaming
p15_ext_062 digital marketplace monetization_rule strategic_reoptimization moderation_backlog
p15_ext_063 digital marketplace moderation_threshold compliance_and_workaround engagement_gain_stability_loss
p15_ext_064 creator monetization ranking_change compliance_and_workaround engagement_gain_stability_loss
p15_ext_065 creator monetization monetization_rule strategic_reoptimization moderation_backlog
p15_ext_066 creator monetization moderation_threshold strategic_reoptimization incentive_gaming
p15_ext_067 creator platform ranking_change strategic_reoptimization incentive_gaming
p15_ext_068 creator platform monetization_rule strategic_reoptimization moderation_backlog
p15_ext_069 creator platform moderation_threshold strategic_reoptimization moderation_backlog
p15_ext_070 publishing platform ranking_change strategic_reoptimization incentive_gaming
p15_ext_071 publishing platform monetization_rule strategic_reoptimization engagement_gain_stability_loss
p15_ext_072 publishing platform moderation_threshold compliance_and_workaround engagement_gain_stability_loss
C Reproducibility Package
The combined public reproducibility archive merges the evidence package with the scientiﬁcally rel-
evant source-side documentation. It contains the external cases, platform-adaptation rubric, source
manifest, runner, validator, row-level method scores, action scores, aggregate results, bootstrap in-
tervals, paired comparisons, domain summaries, failure analysis, veriﬁcation JSON, shared schemas,
construct-validity protocol, signiﬁcance statement, managerial-implications note, and a SHA-256
manifest. Venue-speciﬁc cover letters and submission-positioning ﬁles are excluded because they
17

are not part of the scientiﬁc evidence object.
The core validation command is:
python3 scripts/validate_p15_external_full_benchmark.py
The validator checks the expected 72 cases, 9 methods, 648 method-score rows, 360 action-score
rows, external-case markers, source URLs, and summary metrics. The permanent Zenodo archive
is identiﬁed by DOI 10.5281/zenodo.21945303.
References
Aaltonen, A., Alaimo, C., & Kallinikos, J. (2021). The making of data commodities: Data analytics
as an embedded process. Journal of Management Information Systems , 38(2).
Adner, R. (2017). Ecosystem as structure: An actionable construct for strategy. Journal of Man-
agement, 43(1).
Ansari, S., Garud, R., & Kumaraswamy, A. (2016). The disruptor’s dilemma: TiVo and the U.S.
television ecosystem. Strategic Management Journal , 37(9).
Baldwin, C. Y., & Clark, K. B. (2000). Design Rules: The Power of Modularity . MIT Press.
Benkler, Y. (2006). The Wealth of Networks . Yale University Press.
Benlian, A., Hilkert, D., & Hess, T. (2015). How open is this platform? The meaning and measure-
ment of platform openness from the complementors’ perspective. Journal of Information
Technology, 30(3).
Boudreau, K. (2010). Open platform strategies and innovation: Granting access vs. devolving
control. Management Science , 56(10).
Boudreau, K. J. (2012). Let a thousand ﬂowers bloom? An early look at large numbers of software
app developers and patterns of innovation. Organization Science, 23(5).
Ceccagnoli, M., Forman, C., Huang, P., & Wu, D. J. (2012). Cocreation of value in a platform
ecosystem: The case of enterprise software. MIS Quarterly , 36(1).
Chen, L., Tong, T. W., Tang, S., & Han, N. (2021). Governance and design of digital platforms:
A review and future research directions on a meta-organization. Journal of Management ,
48(1).
Christin, A. (2017). Algorithms in practice: Comparing web journalism and criminal justice. Big
Data and Society , 4(2).
Constantiou, I., Marton, A., & Tuunainen, V. K. (2017). Four models of sharing economy platforms.
MIS Quarterly Executive , 16(4).
Cusumano, M. A., Gawer, A., & Yoﬃe, D. B. (2019). The Business of Platforms . Harper Business.
de Reuver, M., Sorensen, C., & Basole, R. C. (2018). The digital platform: A research agenda.
Journal of Information Technology , 33(2).
18

Eaton, B., Elaluf-Calderwood, S., Sorensen, C., & Yoo, Y. (2015). Distributed tuning of boundary
resources: The case of Apple’s iOS service system. MIS Quarterly , 39(1).
Eisenmann, T., Parker, G., & Van Alstyne, M. W. (2006). Strategies for two-sided markets. Harvard
Business Review , 84(10).
Fountain, J. E. (2001). Building the Virtual State . Brookings Institution Press.
Gawer, A. (2014). Bridging diﬀering perspectives on technological platforms: Toward an integrative
framework. Research Policy, 43(7).
Gawer, A., & Cusumano, M. A. (2014). Industry platforms and ecosystem innovation. Journal of
Product Innovation Management , 31(3).
Ghazawneh, A., & Henfridsson, O. (2013). Balancing platform control and external contribution
in third-party development: The boundary resources model. Information Systems Journal ,
23(2).
Gillespie, T. (2018). Custodians of the Internet . Yale University Press.
Gorwa, R. (2019). What is platform governance? Information, Communication and Society , 22(6).
Gregory, R. W., Henfridsson, O., Kaganer, E., & Kyriakou, H. (2021). The role of artiﬁcial intel-
ligence and data network eﬀects for creating user value. Academy of Management Review ,
46(3).
Hein, A., Schreieck, M., Riasanow, T., Setzke, D. S., Wiesche, M., Bohm, M., & Krcmar, H. (2020).
Digital platform ecosystems. Electronic Markets, 30.
Helberger, N., Pierson, J., & Poell, T. (2018). Governing online platforms: From contested to
cooperative responsibility. The Information Society , 34(1).
Henfridsson, O., & Bygstad, B. (2013). The generative mechanisms of digital infrastructure evolu-
tion. MIS Quarterly , 37(3).
Jacobides, M. G., Cennamo, C., & Gawer, A. (2018). Towards a theory of ecosystems. Strategic
Management Journal , 39(8).
Jhaver, S., Bruckman, A., & Gilbert, E. (2019). Does transparency in moderation really matter?
User behavior after content removal explanations on Reddit. Proceedings of the ACM on
Human-Computer Interaction , 3(CSCW).
Katz, M. L., & Shapiro, C. (1985). Network externalities, competition, and compatibility. American
Economic Review, 75(3).
Kellogg, K. C., Valentine, M. A., & Christin, A. (2020). Algorithms at work: The new contested
terrain of control. Academy of Management Annals , 14(1).
Kokkodis, M., & Ipeirotis, P. (2016). Reputation transferability in online labor markets. Manage-
ment Science , 62(6).
Lee, M. K., Kusbit, D., Metsky, E., & Dabbish, L. (2015). Working with machines: The impact of
algorithmic and data-driven management on human workers. Proceedings of CHI.
19

Majchrzak, A., & Markus, M. L. (2012). Technology aﬀordances and constraints in management
information systems. In Kessler, E. H. (ed.), Encyclopedia of Management Theory . Sage.
Markus, M. L., & Silver, M. S. (2008). A foundation for the study of IT eﬀects: A new look at
DeSanctis and Poole’s concepts of structural features and spirit. Journal of the Association
for Information Systems , 9(10/11).
McIntyre, D. P., & Srinivasan, A. (2017). Networks, platforms, and strategy: Emerging views and
next steps. Strategic Management Journal , 38(1).
Mohlmann, M., & Zalmanson, L. (2017). Hands on the wheel: Navigating algorithmic management
and Uber drivers’ autonomy. Proceedings of ICIS.
Nambisan, S., Lyytinen, K., Majchrzak, A., & Song, M. (2017). Digital innovation management:
Reinventing innovation management research in a digital world. MIS Quarterly , 41(1).
Nickerson, R. C., Varshney, U., & Muntermann, J. (2013). A method for taxonomy development
and its application in information systems. European Journal of Information Systems , 22(3).
Orlikowski, W. J. (1992). The duality of technology: Rethinking the concept of technology in
organizations. Organization Science, 3(3).
Parker, G., Van Alstyne, M., & Choudary, S. P. (2016). Platform Revolution . W. W. Norton.
Parker, G. G., & Van Alstyne, M. W. (2005). Two-sided network eﬀects: A theory of information
product design. Management Science , 51(10).
Parker, G., Van Alstyne, M., & Jiang, X. (2017). Platform ecosystems: How developers invert the
ﬁrm. MIS Quarterly , 41(1).
Poell, T., Nieborg, D., & van Dijck, J. (2019). Platformisation. Internet Policy Review , 8(4).
Rochet, J.-C., & Tirole, J. (2003). Platform competition in two-sided markets. Journal of the
European Economic Association, 1(4).
Rosenblat, A., & Stark, L. (2016). Algorithmic labor and information asymmetries: A case study
of Uber’s drivers. International Journal of Communication , 10.
Shapiro, C., & Varian, H. R. (1999). Information Rules . Harvard Business School Press.
Spagnoletti, P., Resca, A., & Lee, G. (2015). A design theory for digital platforms supporting online
communities. Journal of Information Technology , 30(4).
Srnicek, N. (2017). Platform Capitalism . Polity.
Suzor, N. (2019). Lawless: The Secret Rules That Govern Our Digital Lives . Cambridge University
Press.
Tiwana, A. (2013). Platform Ecosystems: Aligning Architecture, Governance, and Strategy . Morgan
Kaufmann.
Tiwana, A., Konsynski, B., & Bush, A. A. (2010). Platform evolution: Coevolution of platform ar-
chitecture, governance, and environmental dynamics. Information Systems Research , 21(4).
20

Tilson, D., Lyytinen, K., & Sorensen, C. (2010). Digital infrastructures: The missing IS research
agenda. Information Systems Research , 21(4).
Tushman, M. L., & Murmann, J. P. (1998). Dominant designs, technology cycles, and organizational
outcomes. Research in Organizational Behavior , 20.
Van Dijck, J., Poell, T., & de Waal, M. (2018). The Platform Society . Oxford University Press.
Wareham, J., Fox, P. B., & Cano Giner, J. L. (2014). Technology ecosystem governance. Organiza-
tion Science , 25(4).
Wood, A. J., Graham, M., Lehdonvirta, V., & Hjorth, I. (2019). Good gig, bad gig: Autonomy and
algorithmic control in the global gig economy. Work, Employment and Society , 33(1).
Yoo, Y., Henfridsson, O., & Lyytinen, K. (2010). Research commentary: The new organizing logic
of digital innovation. Information Systems Research , 21(4).
Yoo, Y., Boland, R. J., Lyytinen, K., & Majchrzak, A. (2012). Organizing for innovation in the
digitized world. Organization Science, 23(5).
21
