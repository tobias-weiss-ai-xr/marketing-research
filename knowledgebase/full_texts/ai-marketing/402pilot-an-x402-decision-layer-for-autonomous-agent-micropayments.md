---
title: '402Pilot: An x402 Decision Layer for Autonomous Agent Micropayments'
url: https://arxiv.org/abs/2608.01341
category: ai-marketing
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Yin Li
- Yanbo He
- Boo-Ho Yang
- Rav Lawana
- Ziyue Li
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.01341
pages: 16
chars: 71112
fetched_at: '2026-11-08T13:21:17+00:00'
kb_version: 1
---

# 402Pilot: An x402 Decision Layer for Autonomous Agent Micropayments

402Pilot: An x402 Decision Layer for Autonomous Agent Micropayments
Yin Li1, Yanbo He1, Boo-Ho Yang2, Rav Lawana3,
Ziyue Li4, Wei Zeng1, Jing Tang1, Fugee Tsung1,5∗
1The Hong Kong University of Science and Technology (Guangzhou), Guangzhou, China
2MOVENSYS Inc., Seongnam-si, Republic of Korea
3Schneider Electric, Shanghai, China
4Technical University of Munich, Munich, Germany
5The Hong Kong University of Science and Technology, Hong Kong, China
yligt@connect.hkust-gz.edu.cn, yhe376@connect.hkust-gz.edu.cn, byang@movensys.com,
rav.lawana@se.com, ziyue.li@tum.de, weizeng@hkust-gz.edu.cn, jingtang@hkust-gz.edu.cn,
season@ust.hk
Abstract
Programmable-payment protocols such as x402 enable per-
request micropayments, but they do not determine which
payableserviceanautonomousagentshouldbuyunderafinite
wallet. We formulate this buyer-side problem asagent-native
payment decision-making: contextual provider selection un-
derwalletpressure,chosen-onlypaidfeedback,andchanging
market conditions. We propose 402Pilot, a protocol-agnostic
buyer-sidedecisionlayerbetweenautonomousagentsandpay-
mentexecutionthatimplementspurchasingpoliciesforselect-
ing among payable providers. We instantiate it with PA-DCT,
a payment-aware discounted contextual Thompson-sampling
policy that adapts purchasing decisions under wallet pres-
sure while learning from post-payment feedback. To evaluate
buyer-side payment policies, we introduce 402Pilot-Bench,
a frozen-replay benchmark spanning 823 tasks, five hetero-
geneous provider pipelines, and three market regimes, each
evaluatedover30pairedseeds.PA-DCTachievesthestrongest
fixed-wallet adaptive trade-off among non-oracle policies: it
maintains competitive service quality while spending only
39–43%ofthewalletandreallocatesspendingasmarketcon-
ditions change. It attains the best non-oracle PA-gap/Tunder
thepriceshockandthebestmeanandworst-caseranksacross
the nine scenario–metric combinations of quality, ROI, and
PA-gap/T. Comparisons with learning baselines and compo-
nent ablations further support the effectiveness and design
of the proposed decision policy. These results suggest that
programmablepaymentmustbecomplementedbybuyer-side
decision-makingcapableoflearningservicevalueandadapt-
ing purchasing decisions accordingly.
Code and data— https://github.com/MCCodeAI/402Pilot
1 Introduction
The rapid development of x402 brings protocol capabili-
ties that traditional payment flows do not support: machine-
readablepaymentrequirements,per-requestmicropayments,
and low-friction settlement. With further advances such as
x402 V2 (Reppel, Roscoe, and Nickerson 2025), additional
capabilities—service discovery, dynamic service metadata,
and pricing—are exposed to agents through programmatic
∗Corresponding author.
interfaces, making buyer-side service selection an immedi-
ate practical problem.
Several lines of prior work supply pieces of this prob-
lem, but not the full buyer-side setting. Budgeted, contex-
tual,andnon-stationarybanditsoffertoolsforlearningunder
resource constraints, task-dependent conditions, and chang-
ing environments (Badanidiyuru, Kleinberg, and Slivkins
2018; Agrawal and Goyal 2013; Qi, Wang, and Zhu 2023).
Cost-aware LLM routing similarly considers quality–cost
trade-offs, but typically does not model repeated purchas-
ing decisions under a persistent wallet and post-payment
feedback (Chen, Zaharia, and Zou 2024; Ong et al. 2025).
These directions do not jointly capture a protocol-mediated
paid-feedback loop in which the buyer selects and pays for
one service, then learns only from the outcome and cost of
that selection. Payment protocols address execution, while
auction mechanisms study strategic provider bidding (Patra
etal.2026);neitherprovidesanonlinespendingpolicyfora
single autonomous buyer. Existing work therefore does not
jointlyaddressthebuyer-siderequirementsofagent-operated
micropayments.
Werefertothisbuyer-sidesettingasagent-nativepayment
decision-making: an autonomous agent repeatedly makes
irreversible purchasing decisions among payable providers
under task context and wallet pressure, learns from the per-
formance and cost of each selected service, and adapts to
market changes. Unlike human-operated selection, this pro-
cess must run continuously without human resetting, retun-
ing, or comparison of unchosen outcomes. Micropayments
also make repeated low-cost purchases possible, allowing
theagenttoaccumulatefeedbackovermanyfine-grainedde-
cisions. These properties make autonomous micropayment
an online economic decision problem, not only a settlement
problem.
We introduce 402Pilot as a protocol-agnostic buyer-side
decision layer between the agent and the payment stack. For
each request, it derives the task context and obtains the af-
fordable provider set, then applies a buyer policy to select a
provider.402Pilotforwardstheselectionforpaymentexecu-
tion and converts the resulting service outcome and receipt
into learning feedback.
arXiv:2608.01341v1  [cs.AI]  2 Aug 2026

We instantiate this policy as PA-DCT (Payment-Aware
Discounted Contextual Thompson Sampling), a contextual
banditthatmaintainsdiscountedposteriorsoverserviceutil-
ityandrealizedcost.ItusesThompsonsamplingforprovider
selectionunderwalletpressureanddiscountsolderobserva-
tions to adapt as market conditions change.
We evaluate buyer-side policies on402Pilot-Bench, a re-
producible frozen-replay benchmark with823tasks, five
heterogeneous provider pipelines, and stationary, reliability-
shock, and price-shock scenarios, each evaluated over30
pairedseeds.Amongthenon-oraclepolicies,PA-DCTdeliv-
ers the strongest fixed-wallet adaptive trade-off: it maintains
competitive quality while using only39–43%of the avail-
able wallet across all three scenarios and reallocates spend-
ing appropriately as reliability and prices change. Against
both non-learning policies and learning baselines, it attains
thebestmeanrank(3.3/10)andbestworst-caserank(6/10)
acrosstheninescenario–metriccomparisonsofquality,ROI,
andPA-gap/T.AblationsfurtherclarifyhowPA-DCT’scom-
ponents contribute to solvency, adaptation, and robustness.
We make three contributions.
C1.Weformulateagent-nativepaymentdecision-making,
a new buyer-side online decision problem for autonomous
micropaymentagents,andintroduce402Pilotasthemissing
decision layer above payment execution (§3–§4).
C2.We instantiate 402Pilot with PA-DCT, a payment-
awarediscountedcontextualThompson-samplingpolicythat
jointly handles wallet pressure, task context, and reliability
and price drift, yielding adaptive provider selection under
market change (§5).
C3.We introduce402Pilot-Benchfor reproducible eval-
uation of buyer-side payment policies used by autonomous
agents. Itsfrozen-replay design supports comparisonsunder
paid feedback, finite budgets, and market shocks (§6).
2 Related Work
Programmable payment protocols and discovery.Pro-
grammable payment protocols expose the execution sub-
strate for agent payments. x402 embeds per-request pay-
ment into HTTP, and its V2 release adds discovery and ser-
vice metadata for payable APIs (Reppel, Roscoe, and Nick-
erson 2025). AP2 provides a payment-agnostic authoriza-
tion framework for agent-led commerce (Parikh and Sura-
paneni 2025); A2A–x402 brings x402-style cryptocurrency
paymentsintotheAgent-to-Agentprotocol(GoogleAgentic
Commerce 2025); and A402 binds cryptocurrency payment
to service execution through atomic service channels (Li
etal.2026).ArecentSoKorganizesblockchain-basedagent
paymentsarounddiscovery,authorization,execution,andac-
counting (Zhang et al. 2026). These systems make payable
services discoverable and executable, but leave the buyer’s
spendingpolicyoutsidetheprotocol.402Pilottakesthatpol-
icy as its object of study.
Budgeted, contextual, and non-stationary bandits.
Classical bandit methods provide relevant algorithmic tools
for this setting. Budgeted Thompson Sampling samples
reward and cost posteriors under a finite budget (Xia
et al. 2015), while bandits with knapsacks give a broader
constrained-resourceformulation(Badanidiyuru,Kleinberg,
andSlivkins2018).Contextualbanditsestimateactionvalue
from task features, with Contextual Thompson Sampling
and LinUCB as canonical examples (Agrawal and Goyal
2013; Li et al. 2010). Contextual bandits with knapsacks
combinecontextwithresourceconstraints(AgrawalandDe-
vanur 2016). For non-stationary environments, discounted
and sliding-window methods discount or window old obser-
vations (Garivier and Moulines 2011; Trovò et al. 2020; Qi,
Wang, and Zhu 2023), and weighted linear bandits extend
this idea to drifting contextual rewards (Russac, Vernade,
and Cappé 2019). However, none of these methods com-
bines budget awareness, task context, and drift adaptation
within a protocol-mediated paid-feedback loop.
Cost-aware LLM routing and provider selection.Fru-
galGPT uses cascades to reduce inference cost while pre-
serving quality, while RouteLLM, Hybrid LLM, AutoMix,
MixLLM, and LLM Bandit learn prompt-to-model as-
signments from quality, preference, cost, or latency sig-
nals (Chen, Zaharia, and Zou 2024; Ong et al. 2025; Ding
etal.2024;Aggarwaletal.2024;Wangetal.2025;Li2025).
Thesemethodstypicallyoperatewithinafixedservingstack
with known candidates and listed prices. 402Pilot instead
studies wallet-constrained endpoint selection with chosen-
only feedback on realized outcomes and costs. Reverse-
auctionworkconsidersstrategicproviderbidding(Patraetal.
2026), whereas 402Pilot assumes posted prices and focuses
on a single buyer’s online spending policy.
3 Buyer-Side Decision Problem
We formalize buyer-side payment decision-making as a se-
quentialprovider-selectionprobleminwhichanautonomous
buyermustallocateafinitewalletacrosscompetingservices.
3.1 Decision Setting
A single autonomous buyer interacts withKpayable
providers over a horizon ofTrounds, starting with wallet
balanceB 0 =B.Atroundt∈ {0, . . . , T−1},ataskarrives
with contextx t ∈ X, whileBt denotes the buyer’s current
wallet balance.
Each providera∈ {1, . . . , K}carries a chargepa,t. The
buyer may select only from the affordable set
At ={a∈ {1, . . . , K}:pa,t ≤B t}.(1)
IfA t =∅, the interaction terminates. Letτ≤Tdenote the
resulting number of completed purchases.
LetH t denote the information available before selection,
includingthecurrenttaskcontext,walletstate,affordableset,
anyprovidermetadataexposedbeforepayment,andfeedback
from previous purchases. An admissible policy selects only
affordable providers:
at ∼π t(· |Ht),supp (π t(· |Ht))⊆ At.(2)
LetΠ adm denote the class of admissible policies.
The selected provider produces
(qt, ft)∼ Dat,t (· |xt),(3)

whereq t ∈[0,1]is the realized task quality andft ∈ {0,1}
indicatespaidnon-delivery:theserviceischargedbutreturns
no usable output. After payment, the buyer observes(qt, ft)
and the realized chargect =p at,t, and the wallet evolves as
Bt+1 =B t −c t.(4)
Outcomes and realized costs are observed only for the se-
lectedprovider,yieldingchosen-onlypaidfeedback.Provider
outcome distributions and charges may change over time
without announced change points.
3.2 Buyer Objective
The realized service utility is
ut =q t −νf t,(5)
whereν≥0penalizespaidnon-delivery.Therealizedcharge
is normalized as
ect = clip
 ct
cmax
,0,1

, c max >0,(6)
wherec max is a fixed normalization constant.
Letλ t >0denotewalletpressure,computedfromthecur-
rent balancerelative to aspending plan. Itrises whencumu-
lative spending runs ahead of plan and falls when spending
runs behind. Its normalized value is
λnorm,t = λt 1 +λ t ∈(0,1).(7)
The payment-aware reward for a completed purchase is
rt = (1−λ norm,t)u t −λ norm,tect.(8)
Thus, increasing wallet pressure shifts weight from service
utility to payment.
The buyer seeks an admissible policy maximizing ex-
pected cumulative payment-aware reward over the served
rounds:
π⋆ ∈arg max
π∈Πadm
Eπ
"τ−1X
t=0
rt
#
.(9)
Thisformulationisindependentofanyparticulardecisionor
learning algorithm.
4 The 402Pilot Decision Layer
Tooperationalizethisdecisionprocess,weintroduce402Pi-
lot, a policy-agnostic layer between agent buyers and the
payment stack. It implements provider selection and post-
payment learning through interchangeable buyer policies.
Figure 1 shows the per-round decision flow.
Upstream components provide a task request and candi-
date payment requirements
Qt ={(a, pa,t)}K a=1.
Thecontextencodermapstherequesttox t,whilethewallet
usesQ t to derive the affordable setAt and wallet pressure
λt. Wallet pressure compares cumulative spending with the
expected budget trajectory:
λt =



λ0, t= 0,
λ0 exp

α
 (B−B t)/B
t/T −1

, t >0,
(10)
whereλ 0 >0is the baseline pressure andα≥0con-
trolsitssensitivitytodeviationsfromthespendingplan.The
exponential form keeps pressure positive and smoothly in-
creases cost sensitivity as overspending grows. The policy
then invokesselect(x t,A t)→a t ∈ At and passes the
selected provider to the underlying payment substrate, such
as x402, for execution and settlement. After the transaction,
the outcome scorer converts the provider response and pay-
ment receipt into the realized utilityut and chargec t. The
wallet recordsc t, and the policy receives the post-payment
feedback throughupdate(xt, at, ut, ct).
The interface restricts selection toAt and exposes feed-
back only for the chosen provider, consistent with the af-
fordability and chosen-only feedback setting in Section 3.
It supports diverse buyer policies, including heuristic,
optimization-based, and learning-based approaches.
5 The PA-DCT Policy
As a concrete buyer policy within 402Pilot, we introduce
Payment-Aware Discounted Contextual Thompson Sam-
pling (PA-DCT), a contextual bandit. PA-DCT operates as
a continual decision loop: it maintains discounted Bayesian
posteriors over provider utility and cost, draws Thompson
samples,anduseswalletpressuretoselectamongaffordable
providers.Aftereachtransaction,realizedutilityandcostup-
date the posteriors, allowing the policy to adapt as provider
performance and prices change.
5.1 Discounted Utility and Cost Posteriors
PA-DCT conditions its estimates on task context through
a discrete bucket mapk t =k(x t)∈ {1, . . . , Kb}. For
each provider–context pair(a, k), it maintains two dis-
countedBayesianposteriors:aQ-posterioroverrealizedutil-
ityu t =q t −νf t and a C-posterior over realized costct.
Each cell stores a shared effective countna,k t , a utility
sumS a,k t ,andacostsumS c a,k t .Eachcompletedtransaction
contributesoneobservationtobothposteriors.Toremainre-
sponsive to changing reliability and prices, PA-DCT applies
acommondiscountfactorγ∈(0,1]toeverycellatthestart
of each round. The selection-time statistics are
¯na,k t =γn a,k t−1,
¯Sa,k t =γS a,k t−1,
¯Sa,k c,t =γS c a,k t−1.
(11)
The Q-posterior uses prior meanµ0,q, prior varianceσ 2 0,q,
and likelihood varianceσ2 q. Its posterior variance and mean
are
Σa,k q =

1
σ2 0,q + ¯na,k t σ2q !−1 ,
θa,k q = Σa,k q

µ0,q
σ2 0,q +
¯Sa,k t
σ2q
!
.
(12)
whereθ a,k q andΣ a,k q denotetheposteriormeanandvariance
of the utility model, respectively.
The C-posterior follows the same Normal–Normal con-
struction. Its posterior mean and variance(θa,k c ,Σ a,k c )are

402Pilot decision layer
protocol stack + provider
Agent
Candidate
quotes
Context
encoder
policy.select
(xt, 𝒜t) → a t
Wallet policy.update (xt, at, ut, ct) Outcome scorer
ut = q t − fν t
x402
stack
Provider
task
context
(xt)
chosen arm
(at)
pay
+ callquery λt
affordable
set (𝒜t)
quotes
(𝒬t) outcome (qt, ct, ft)
response
+ receipt
record_spend
(ct)
Figure1:The402Pilotper-rounddecisionflow.UpstreamcomponentssupplyataskandpayablecandidatesQ t.Within402Pilot,
the context encoder derives the task contextxt, while the wallet separately exposes the affordable setAt and wallet pressure
λt. The policy selectsat; the payment substrate executes the selected transaction; and the returned response and receipt yield
(qt, ft, ct). The layer then reportsct to the wallet and passes(xt, at, ut, ct)to the policy update. The figure shows x402 as the
payment substrate, but the same boundary can be implemented by another programmable-payment substrate.
computed analogously using priorN(¯ca, σ2 0,c), likelihood
varianceσ 2 c,anddiscountedcostsum ¯Sa,k c,t .Theinitialspeci-
ficationcost¯ca definesthecostprior,whileobservedreceipt
charges continually update the posterior as provider prices
change.
All provider–context cells are discounted once per round,
including those not selected in the current round, so stale
evidence gradually loses influence over time.
5.2 Selection Rule
At decision time, PA-DCT implementsselectusing the
task contextxt, the affordable provider setAt, and the wal-
let pressureλ t. Writeλ norm =λ norm,t for the normalized
walletpressureinEq.(7).Thecontextbucketdeterminesthe
corresponding provider–context cells, from which Thomp-
son samples are drawn as
ˆua,kt ∼ N  θa,kt q ,Σ a,kt q  ,
ˆca,kt ∼ N  θa,kt c ,Σ a,kt c  . (13)
Thesampledcostisfirstnormalized,afterwhichthesampled
utility and normalized cost are combined into the following
payment-aware reward:
eˆc a,kt = clip  ˆca,kt /cmax,0,1  ,
ˆra = (1−λ norm)ˆua,kt −λ normeˆc a,kt . (14)
The sampled reward in Eq. (14) is the pre-payment coun-
terpart of the realized reward in Eq. (8): it replaces realized
Algorithm 1PA-DCT policy loop.
Require:Initial specification costs¯ca; discountγ; normal-
izerc max.
Require:Context encoderk(·)and Q/C posterior priors.
1:for(a, k)∈ {1, . . . , K} × {1, . . . , Kb}do
2:n a,k ←0;S a,k ←0;S c a,k ←0
3:foreach served roundtwithA t ̸=∅do
4:Receivex t andA t
5:For all(a, k), multiplyn a,k,S a,k, andSc a,k byγ
6:Readλ t;k t ←k(x t);λ norm ←λ t/(1 +λ t)
7:fora∈ A t do
8:ComputetheQ/Cposteriorparametersfor(a, k t)
9:Sampleˆu a,kt andˆca,kt using Eq. (13)
10: eˆc a,kt ←clip(ˆca,kt /cmax,0,1)
11:ˆr a ←(1−λ norm)ˆua,kt −λ normeˆc a,kt
12:Selecta t ←arg max a∈At ˆra
13:Receive realized(u t, ct)
14:n at,kt += 1;S at,kt +=u t;S c at,kt +=c t
utilityandnormalizedcostwithThompsonsamples.Aswal-
letpressureincreases,selectionbecomesprogressivelymore
cost-sensitive while remaining driven by posterior samples
ratherthanfixedcostthresholds.Theproviderwiththehigh-
est sampled reward is selected:at = arg maxa∈At ˆra.

5.3 Learning from Post-Payment Feedback
After the selected transaction completes, PA-DCT imple-
mentsupdateusing the realized utilityu t and receipt cost
ct. The task is mapped to the corresponding context bucket
kt, and the observations are incorporated only into the se-
lected provider–context cell:
nat,kt t = ¯nat,kt t + 1,
Sat,kt t = ¯Sat,kt t +u t,
Sc at,kt t = ¯Sat,kt c,t +c t.
(15)
Allotherprovider–contextcellsretaintheirdiscountedstatis-
tics from Eq. (11).
Algorithm 1 summarizes the PA-DCT policy loop. Ap-
pendix B provides formal support for its key components
and discusses the scope of the analysis.
6 Evaluation
Evaluating buyer-side payment policies requires a bench-
mark with diverse tasks, heterogeneous providers, control-
lablemarketscenarios,andreproducibleexecution.Existing
LLM benchmarks do not jointly satisfy these requirements,
soweconstruct402Pilot-Benchbyextendingpublicdatasets
with multiple provider pipelines, prices, and market dynam-
ics. Under its frozen-replay design, multiple responses are
pre-generated and scored for each task–provider pair, then
sampledfromthesamefrozenpoolacrosspolicies,enabling
reproducible comparisons without live-inference variabil-
ity. Since frozen replay abstracts payment execution, a local
x402witnessseparatelyvalidatesthedecision-layerinterface
against an actual HTTP 402 payment flow; implementation
details appear in Appendix G.
6.1 Experimental Setup
Benchmark.402Pilot-Benchcontains823effective tasks
across the four datasets in Table 1 (Chen et al. 2021; Yang
et al. 2018; Joshi et al. 2017; Köpf et al. 2023), which de-
fine the task buckets used by PA-DCT. Utility scores are
normalizedto[0,1]usingthedataset-specificmetricsshown
in the table. For each task–provider pair, we cache five in-
dependently generated responses with precomputed utility
scores.Acrossthefiveprovidersdescribedbelow,thisyields
823tasks×5providers×5responses= 20,575scored re-
sponses.Allscenariosreplaythesametaskpoolandresponse
cache; only realized failures and effective prices change.
Providers.Table2summarizesthefiveproviders.P-cheap,
P-mid, and P-premium represent different price–quality lev-
els.P-advandP-flakysimulatetwoproblemsthatbuyersmay
faceinanopenservicemarket:fraudulentormisrepresented
service quality, and unstable service that may fail after pay-
ment.BecausebothhavethesamelistedpriceasP-mid,their
true performance must be learned from observed outcomes.
Scenario design.The scenarios test whether a policy can
maintainausefulallocationwhenproviderconditionsremain
stable or change without warning. S1 is stationary. In S2, P-
midexperiencesareliabilityshock,witha30%forced-failure
Dataset / task type Tasks Utility metric
HumanEval / coding 164 Execution-based pass@1
HotpotQA / multi-hop
QA
220 Max normalized EM/F1
TriviaQA-web /
closed-form web QA
219 Max normalized EM/F1
OpenAssistant /
open-ended QA
220 Cached LLM-as-judge
Total 823–
Table 1: Composition of 402Pilot-Bench.
Provider Price Pipeline
P-cheap0.0005qwen3.5-flash; uniform prompt;cheap tier
P-mid0.002GPT-5.4-mini; uniform prompt;mid tier
P-premium0.01GPT-5.4; uniform prompt;premium tier
P-adv0.002GPT-5.4-mini;60%adversarialprompt;fluent
wrong answers
P-flaky0.002GPT-5.4-mini; 40% timeout injection;billed
timeouts
Table 2: Provider set used in 402Pilot-Bench. P-mid, P-adv,
and P-flaky share the same price tier and base model.
rate from rounds 3,000 to 5,500 before recovery. In S3, P-
premium’spricedropsfrom$0.01to$0.002atround1,000,
testing whether the policy shifts toward a newly attractive
provider.
Each policy is evaluated forT= 10,000rounds with a
$50 budget over 30 paired seeds. This budget is deliberately
binding: at the initial premium price, it covers only 5,000
of the 10,000 rounds. For each seed, all policies are evalu-
ated using the same task order, cached-response draws, and
scenario changes.
Hyperparameters.The discount factorγ, paid-non-
delivery penaltyν, and cost scalecmax most directly govern
the policy’s adaptation, failure penalty, and cost normaliza-
tion. The discount factorγ= 0.999provides an effective
memoryofabout10 3 rounds,balancingresponsivenesswith
stable estimation. The paid-non-delivery penaltyν= 0.5
makes billed failures materially worse without overwhelm-
ingthe[0,1]utilitysignal.Thecostscalec max = $0.01maps
the initial premium price to 1 and keeps all lower prices on
the same normalized scale. All remaining settings are fixed;
complete notation and values appear in Appendix A, with
sensitivity analyses in Appendix D.
Comparators.The comparators cover non-learning poli-
cies, learning policies, and an oracle upper bound. The
non-learning group includes Random, three fixed-arm poli-
cies,andBudgetRule,capturinguninformedselection,static
provider preferences, and a hand-crafted wallet rule. Bud-
getRuleswitchesfromP-premiumtoP-midandthenP-cheap
whentheremainingbudgetfallsbelow50%and20%,respec-
tively.
The learning group covers the main capabilities relevant
tobuyer-siderouting.ContextualDS-TS(Qi,Wang,andZhu

2023)tracksutilitydriftbutlackswalletpressure;Contextual
BTS (Xia et al. 2015) learns utility and cost under a finite
budgetbutdoesnotdiscountstaleobservations;PM-Greedy,
inspiredbyFrugalGPT-stylerouting(Chen,Zaharia,andZou
2024), routes using listed prices rather than learned realized
costs; and LinCBwK-Adapt (Agrawal and Devanur 2016)
combines context and budget constraints but lacks explicit
drift discounting.
ThereplayTrueOracleselectstheaffordablearmwiththe
highest realized payment-aware reward and is reported only
as an unattainable upper bound. Implementation details and
replay adaptations of all comparators appear in Appendix F.
6.2 Metrics
Evaluatingbuyer-sidedecisionsunderafixedwalletrequires
considering both the service quality delivered and how the
budget is used. We therefore report complementary metrics
coveringdeliveredquality,walletconsumption,spendingef-
ficiency,andperformancerelativetothereplayupperbound.
Table 3 gives their calculations.
Full-horizonmeanqualitymeasurestheservicequalityde-
liveredoverallTrounds,withroundsafterbudgetexhaustion
counted as zero. Budget use captures the share of the initial
walletconsumed.ROImeasuresthequalityobtainedperdol-
lar spent and is used as an efficiency diagnostic rather than
anoptimizationobjective.PA-gap/Tmeasurestheper-round
cumulative payment-aware reward gap relative to the replay
True Oracle, providing an empirical replay counterpart of
the buyer objective in Eq. (9).
Metric Calculation Meaning
¯qT ↑(1/T) P t<τ qt Mean quality; exhausted
rounds count as zero.
Budget use100 P t<τ ct/BWallet share spent.
ROI↑ P t<τ qt/ P t<τ ct Quality per dollar; effi-
ciency only.
PA-gap/T↓(R TO T −R π T )/TGaptoreplayTrueOracle.
Table 3: Evaluation metrics.
6.3 Main Results
PA-DCTdeliversthestrongestfixed-walletadaptivetrade-off
on 402Pilot-Bench: it maintains competitive service quality
under controlled spend and reallocates in the right direction
whenreliabilityorpriceschange.Acrossthethreescenarios
in Table 4, PA-DCT consistently uses only39–43%of the
walletwhileremainingamongthestrongestnon-oraclepoli-
ciesonPA-gap/T,includingthebestnon-oracleresultinS3.
Together, these results show that the objective of buyer-side
payment decision-making is not to maximize service qual-
ity in every market, but to learn when additional quality is
worthpayingforunderafinitewallet.Accordingly,PA-DCT
is not intended to maximize pointwise quality in every sce-
nario:policiessuchasLinCBwK-Adaptandpremium-heavy
rules occasionally achieve higher absolute quality, but only
by consuming substantially more of the wallet, resulting in
weaker payment-aware trade-offs.
The three scenarios highlight different aspects of PA-
DCT’s behavior. In the stationary market (S1), Always-P-
mid achieves the best non-oracle PA-gap/Twith similarly
low budget use, reflecting the advantage of a fixed policy
whenitsselectedtiermatchesastablemarket.PA-DCTpays
a modest exploration cost but still uses only42%of the
wallet; by contrast, BudgetRule and LinCBwK-Adapt ob-
tain slightly higher quality while consuming80%and93%,
respectively. This highlights the role of wallet pressure in
preserving long-horizon budget efficiency. In the reliabil-
ity shock (S2), PA-DCT is not significantly different from
the numerically best non-oracle baseline, Always-P-cheap,
on PA-gap/T, while delivering substantially higher service
quality(0.761vs.0.610)throughreallocationawayfromthe
failingmid-tierprovider.Thishighlightstheroleofreliability
adaptation in preserving service quality. In the price shock
(S3), PA-DCT achieves the best non-oracle PA-gap/T. Sev-
eral learning baselines attain slightly higher absolute qual-
ity, but their gains come with substantially worse PA-gap/T
(0.195–0.264vs.0.121) and lower ROI. This highlights the
roleofpriceadaptationinreallocatingpurchasesasprovider
prices change while keeping spending under control.
Appendix E provides a direct view of these allocation
shifts, showing PA-DCT moving away from P-mid during
the outage, returning after recovery, and shifting toward dis-
counted P-premium after the price promotion.
A closer look at the three types of baselines shows how
their underlying design principles are reflected in the ex-
perimental results. Among the non-learning policies, fixed-
arm strategies perform well only when their selected tier
matchesthemarket,whileBudgetRulefollowswalletthresh-
oldsratherthanproviderfeedback.TheThompson-sampling
baselines expose a split between adaptation and budget con-
trol. Contextual DS-TS responds to market changes but ex-
hausts the wallet in S1 and S2, whereas Contextual BTS
preservesthewalletbutremainsnearthecheaptierandthere-
fore misses the discounted premium opportunity in S3. The
cost-aware learning baselines provide the strongest quality
comparison, but not the strongest payment-aware trade-off.
PM-Greedy and LinCBwK-Adapt achieve competitive qual-
ity, but consistently at the cost of substantially higher wallet
consumption and worse PA-gap/T. Taken together, these re-
sults show that none of the baselines simultaneously main-
tainsbudgetdisciplineandadaptseffectivelyacrossreliabil-
ityandpricechanges.Theablationstudybelowseparatesthe
roles of PA-DCT’s components in achieving this balance.
6.4 Ablation Study
TheablationsfurtherclarifytheroleofeachPA-DCTcompo-
nent.Tocomplementtheendpointmetrics,AdaptTmeasures
the number of post-shock rounds required for sustained re-
covery (lower is better); complete ablation definitions and
results appear in Appendix C. Payment-aware ranking pri-
marily preserves full-horizon solvency: removing it (−P)
exhausts every S1/S2 wallet and increases PA-gap/Tfrom
0.166to0.878in S2, while full-horizon mean quality falls
from0.761to0.517. Adaptation depends on both temporal
discounting and realized-cost learning. Removing discount-
ing(−D)slowsS2recoveryby53%(1,467→2,249rounds),

S1 Stationary S2 Mid Outage S3 Premium Promo
Policy¯q T ↑
Budget
use (%) ROI↑
PA-gap/T
↓¯q T ↑
Budget
use (%) ROI↑
PA-gap/T
↓¯q T ↑
Budget
use (%) ROI↑
PA-gap/T
↓
Random0.688 66 209 0.365 0.676 66 205 0.375 0.688 37 370 0.274
Always-P-cheap0.610 101,2200.167 0.610 101,220 0.1640.610 101,2200.195
Always-P-mid0.819 40 4100.1010.757 40 379 0.174 0.819 40 410 0.129
Always-P-premium0.433 100 87 1.072 0.433 100 87 1.0700.86556 309 0.400
BudgetRule0.83180 208 0.692 0.769 80 192 0.722 0.859 56 307 0.405
Contextual DS-TS0.559 100 112 0.858 0.514 100 103 0.884 0.840 48 349 0.264
Contextual BTS0.612 10 1,187 0.169 0.612 10 1,187 0.166 0.612 10 1,187 0.197
PM-Greedy0.732 90 179 0.542 0.627 99 128 0.660 0.836 44 384 0.198
LinCBwK-Adapt0.824 93 180 0.4570.796100 159 0.515 0.836 45 377 0.195
PA-DCT (ours)0.797 42 378 0.133 0.761 43 357 0.166 0.831 39 4290.121
True Oracle (UB)0.901 32 561 0.000 0.901 33 551 0.000 0.906 25 722 0.000
Table 4: Main results on 402Pilot-Bench, averaged over30paired seeds. Rows are grouped as non-learning baselines, learning
baselines,PA-DCT,andthereplayupperbound.Boldmarksthebestnon-oracleentryinthequality,ROI,andPA-gap/Tcolumns.
whereas replacing learned realized costs with specification
prices(−C post)largelyeliminatespriceadaptationinS3,re-
ducingpost-shockP-premiumselectionfrom66.1%to3.6%
and increasing PA-gap/Tfrom0.121to0.144.
Context and Thompson sampling mainly improve adapta-
tion efficiency and robustness. Removing contextual buck-
eting (−C) delays S3 AdaptT from200to398rounds with
little change in endpoint performance. Replacing Thomp-
son sampling with posterior means (−TS) increases the S1
PA-gap/Tstandard deviation from0.004to0.046and de-
lays S3 AdaptT from200to2,232rounds, with only24/30
seeds reaching the AdaptT threshold. Overall, the ablations
assigndistinctoperationalrolestothecomponents:payment
awareness preserves solvency, discounting and realized-cost
learningenableadaptation,contextacceleratesrecovery,and
Thompson sampling improves robustness.
7 Discussion and Future Work
Recent advances in programmable payment protocols and
community-driven reputation mechanisms provide an in-
creasingly capable infrastructure for agentic commerce. Our
results suggest that infrastructure alone is not sufficient for
autonomous payment, because agents must still decide how
toallocatealimitedbudgetasservicevalueandmarketcon-
ditionsevolve.Thismotivatesbuyer-sidedecision-makingas
a distinct layer between agents and payment protocols. PA-
DCT serves as an initial instantiation of this decision layer
rather than a definitive solution; future work may explore
reinforcementlearning,foundation-model-basedpolicies,or
other decision mechanisms within the same framework.
Our evaluation emphasizes reproducible policy compar-
ison rather than complete deployment validation. Frozen
replay isolates buyer-side decision quality under identical
service traces, while the local x402 witness demonstrates
end-to-end integration with an HTTP 402 payment loop.
Extending evaluation to controlled live-market deployments
remains important future work.
Thebenchmarkalsocoversafinitesetofproviders,tasks,
and market conditions, and learning quality ultimately de-
pends on the reliability of outcome feedback. Future work
shouldexpandthebenchmarktobroaderindustrialscenarios,
richerproviderecosystems,morecomplexmarketdynamics,
and more reliable outcome evaluation.
8 Conclusion
Programmable payment protocols enable agents to execute
payments, but they do not determine what is worth paying
for. We introduced 402Pilot as a buyer-side decision layer
between agents and payment protocols, together with PA-
DCTasaninitialpayment-awaredecisionpolicyforbudget-
constrainedserviceselection.Evaluationon402Pilot-Bench
showedthatPA-DCTachievesastrongfixed-wallettrade-off
whileadaptingitspurchasingdecisionsunderreliabilityand
price changes. These results establish buyer-side decision-
making as a new research direction for agentic commerce
andmotivatefutureworkonricherdecisionpolicies,broader
benchmarks, and real-world deployment.
References
Aggarwal, P.; Madaan, A.; Anand, A.; Potharaju, S. P.;
Mishra, S.; Zhou, P.; Gupta, A.; Rajagopal, D.; Kappagan-
thu, K.; Yang, Y.; Upadhyay, S.; Faruqui, M.; and Mausam.
2024. AutoMix: Automatically Mixing Language Models.
InAdvances in Neural Information Processing Systems, vol-
ume 37.
Agrawal, S.; and Devanur, N. R. 2016. Linear Contextual
BanditswithKnapsacks. InAdvancesinNeuralInformation
Processing Systems, volume 29.
Agrawal, S.; and Goyal, N. 2013. Thompson Sampling for
Contextual Bandits with Linear Payoffs. InProceedings of
the30thInternationalConferenceonMachineLearning,vol-
ume28ofProceedingsofMachineLearningResearch,127–
135. PMLR.
Badanidiyuru,A.;Kleinberg,R.;andSlivkins,A.2018.Ban-
ditswithKnapsacks.JournaloftheACM,65(3):13:1–13:55.
Chen, L.; Zaharia, M.; and Zou, J. 2024. FrugalGPT: How
to Use Large Language Models While Reducing Cost and

ImprovingPerformance.TransactionsonMachineLearning
Research.
Chen, M.; Tworek, J.; Jun, H.; Yuan, Q.; Pinto, H. P. d. O.;
Kaplan, J.; Edwards, H.; Burda, Y.; Joseph, N.; Brockman,
G.; Ray, A.; Puri, R.; Krueger, G.; Petrov, M.; Khlaaf, H.;
Sastry, G.; Askell, A.; Mishkin, P.; Chan, B.; Gray, S.; Ry-
der, N.; Pavlov, M.; Power, A.; Kaiser, L.; Bavarian, M.;
Winter, C.; Tillet, P.; Such, F. P.; Cummings, D.; Plappert,
M.; Chantzis, F.; Barnes, E.; Herbert-Voss, A.; Guss, W. H.;
Nichol, A.; Paino, A.; Tezak, N.; Tang, J.; Babuschkin, I.;
Balaji, S.; Jain, S.; Saunders, W.; Hesse, C.; Carr, A. N.;
Leike, J.; Achiam, J.; Misra, V.; Morikawa, E.; Radford, A.;
Knight,M.;Brundage,M.;Murati,M.;Mayer,K.;Welinder,
P.; McGrew, B.; Amodei, D.; McCandlish, S.; Sutskever, I.;
and Zaremba, W. 2021. Evaluating Large Language Models
Trained on Code.arXiv preprint arXiv:2107.03374.
Ding, D.; Mallick, A.; Wang, C.; Sim, R.; Mukherjee, S.;
Rühle,V.;Lakshmanan,L.V.S.;andAwadallah,A.H.2024.
HybridLLM:Cost-EfficientandQuality-AwareQueryRout-
ing. InInternational Conference on Learning Representa-
tions.
Garivier, A.; and Moulines, E. 2011. On Upper-Confidence
Bound Policies for Switching Bandit Problems. InAlgorith-
mic Learning Theory (ALT 2011), volume 6925 ofLecture
Notes in Computer Science, 174–188. Springer.
Google Agentic Commerce. 2025. A2A x402 Ex-
tension. https://github.com/google-agentic-commerce/a2a-
x402. GitHubrepository,releasev0.1.0.Accessed:2026-05-
19.
Joshi, M.; Choi, E.; Weld, D. S.; and Zettlemoyer, L. 2017.
TriviaQA: A Large Scale Distantly Supervised Challenge
Dataset for Reading Comprehension. InProceedings of the
55th Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), 1601–1611.
Köpf, A.; Kilcher, Y.; von Rütte, D.; Anagnostidis, S.; Tam,
Z. R.; Stevens, K.; Barhoum, A.; Nguyen, D.; Stanley, O.;
Nagyfi, R.; ES, S.; Suri, S.; Glushkov, D.; Dantuluri, A.;
Maguire, A.; Schuhmann, C.; Nguyen, H.; and Mattick, A.
2023. OpenAssistant Conversations: Democratizing Large
Language Model Alignment. InAdvances in Neural Infor-
mation Processing Systems, volume 36, 47669–47681. Red
Hook, NY, USA: Curran Associates, Inc.
Li, L.; Chu, W.; Langford, J.; and Schapire, R. E. 2010. A
Contextual-Bandit Approach to Personalized News Article
Recommendation. InProceedings of the 19th International
Conference on World Wide Web, 661–670. ACM.
Li,Y.2025.LLMBandit:Cost-EfficientLLMGenerationvia
Preference-Conditioned Dynamic Routing.arXiv preprint
arXiv:2502.02743.
Li, Y.; Wang, L.; Wang, K.; Yang, Z.; Wang, K.; Guan, Z.;
and Gao, J. 2026. A402: Binding Cryptocurrency Payments
toService ExecutionforAgentic Commerce.arXivpreprint
arXiv:2603.01179.
Ong,I.;Almahairi,A.;Wu,V.;Chiang,W.-L.;Wu,T.;Gon-
zalez,J.E.;Kadous,M.W.;andStoica,I.2025. RouteLLM:
LearningtoRouteLLMswithPreferenceData. InTheThir-
teenth International Conference on Learning Representa-
tions.
Parikh, S.; and Surapaneni, R. 2025. Powering AI
Commerce with the New Agent Payments Protocol
(AP2). https://cloud.google.com/blog/products/ai-machine-
learning/announcing-agents-to-payments-ap2-protocol.
Google Cloud Blog. Accessed: 2026-05-19.
Patra, P.; Damle, S.; Padala, M.; and Gujar, S. 2026. Truth-
ful Reverse Auctions for Adaptive Selection via Contextual
Multi-Armed Bandits. InProceedings of the 25th Inter-
national Conference on Autonomous Agents and Multiagent
Systems,578–586.InternationalFoundationforAutonomous
Agents and Multiagent Systems.
Qi, H.; Wang, Y.; and Zhu, L. 2023. Discounted Thomp-
son Sampling for Non-Stationary Bandit Problems.arXiv
preprint arXiv:2305.10718.
Reppel, E.; Roscoe, C.; and Nickerson, J. 2025. Introduc-
ing x402 V2: Evolving the Standard for Internet-native Pay-
ments. https://x402.org/x402-v2-launch/. Accessed: 2026-
07-29.
Russac,Y.;Vernade,C.;andCappé,O.2019. WeightedLin-
ear Bandits for Non-Stationary Environments. InAdvances
in Neural Information Processing Systems, volume 32.
Trovò, F.; Paladino, S.; Restelli, M.; and Gatti, N. 2020.
Sliding-Window Thompson Sampling for Non-Stationary
Settings.Journal of Artificial Intelligence Research, 68:
311–364.
Wang, X.; Liu, Y.; Cheng, W.; Zhao, X.; Chen, Z.; Yu, W.;
Fu, Y.; and Chen, H. 2025. MixLLM: Dynamic Routing
in Mixed Large Language Models. InProceedings of the
2025 Conference of the Nations of the Americas Chapter of
theAssociationforComputationalLinguistics:HumanLan-
guageTechnologies(Volume1:LongPapers),10912–10922.
Albuquerque, New Mexico: Association for Computational
Linguistics.
Xia,Y.;Li,H.;Qin,T.;Yu,N.;andLiu,T.-Y.2015. Thomp-
son Sampling for Budgeted Multi-Armed Bandits. InPro-
ceedings of the 24th International Joint Conference on Arti-
ficial Intelligence, 3960–3966.
Yang, Z.; Qi, P.; Zhang, S.; Bengio, Y.; Cohen, W. W.;
Salakhutdinov, R.; and Manning, C. D. 2018. HotpotQA:
ADatasetforDiverse,ExplainableMulti-HopQuestionAn-
swering. InProceedings of the 2018 Conference on Empiri-
cal Methods in Natural Language Processing, 2369–2380.
Zhang, Y.; Xiang, Y.; Lei, Y.; Wang, Q.; Qiu, T.; Sun, Y.;
Zarkov,S.;Yuen,T.H.;Deppeler,A.;Yu,J.;andLam,K.-Y.
2026. SoK: Blockchain Agent-to-Agent Payments.arXiv
preprint arXiv:2604.03733.

A Notation and Locked Settings
This appendix collectsthe notation and lockedexperimental
settings used throughout the paper and Appendix B.
B Proofs
Thisappendixprovidesformalsupportforthemainanalytical
properties of PA-DCT rather than a complete analysis of the
replaysystem.Specifically,weestablishrewardboundedness
(Prop.1),posteriorconsistencyinthestationaryno-discount
regime(Prop.2),astationarywell-specifiedregretreduction
(Thm.1),andafixed-scheduleadaptationrateafteranabrupt
change (Thm. 2). The regret theorem is intentionally stated
for a clean version of the score; §B.7 records the gap to the
full empirical setting.
B.1 Shared assumptions
Weusethenotationof§3and§5ofthemainpaper,summa-
rized in Appendix A. All regret sums below are over served
rounds with nonempty affordable set; if a wallet exhausts
early, replaceTby the served horizonτ. The formal claims
use the following assumptions. Different results require dif-
ferentsubsetsoftheseassumptions;onlythestationaryregret
theorem relies on the stronger assumptions (A2′)–(A3′) in-
troduced below.
(A1)Stationary or piecewise-stationary cells.Conditional
on the chosen armaand bucketk, and averaging over
the exogenous task draw within that bucket, observations
are independent across pulls and the joint distribution of
(qt, ct, ft)is identical within each phase.
(A2)Sub-Gaussian noise.The utilityu t given cell(a, k)is
σu-sub-Gaussianaroundmeanµ a,k u ;therealizedcostc tis
σc,true-sub-Gaussian around meanµa,k c . The policy uses
fixed proxy variancesσ2 q , σ2 c, possibly different from the
true variances.
(A3)Bounded means.|µ a,k u | ≤1andµ a,k c ∈[0, cmax]for
every(a, k).
The stationary regret reduction further uses two restric-
tionsthatarenotneededbytheboundedness,consistency,or
adaptation claims:
(A2′)Well-specifiedproductmodel.Thepolicy’sproxylike-
lihoods are the true likelihoods: utility and cost obser-
vations are conditionally independent Gaussians around
(µa,k u , µa,k c )with variancesσ 2 q =σ 2 u andσ 2 c =σ 2 c,true,
andthepriorfactorizesasthepolicy’sindependentGaus-
sian Q/C priors.
(A3′)Clean score.The regret reduction is stated for the
unclipped score(1−λ norm)ˆua,k −λ normˆca,k/cmax, or
equivalently for trajectories on which the implementa-
tion’s cost-sample clip in the PA-DCT sampled reward
(Eq. (14) of the main paper) is inactive.
The posterior arguments use the Normal–Normal mean
identities
θa,k q = κqµ0,q +S a,k t
κq +n a,k t , θ a,k c = κc¯ca +S c a,k t κc +n a,k t ,(16)
whereκ q =σ 2 q /σ2 0,q andκ c =σ 2 c /σ2 0,c. We write a single
na,k t because each selected call supplies one utility and one
cost observation. If quality and cost discounts are split, the
same formulas apply to the two posteriors with their own
effective counts.
B.2 Proposition 1: reward boundedness
Proposition 1(Reward boundedness).For every roundt
with0≤ν≤1, the payment-aware reward satisfiesr t ∈
[−1,+1].
Proof.Sinceq t ∈[0,1],f t ∈ {0,1}, and0≤ν≤1, we
haveu t =q t whenf t = 0andu t =q t −ν∈[−1,1]when
ft = 1. Thus|u t| ≤1; also˜ct ∈[0,1]andλ norm ∈(0,1).
Hence|r t| ≤(1−λnorm)|ut|+λ norm|˜ct| ≤(1−λnorm) +
λnorm = 1.
B.3 Proposition 2: posterior consistency
Proposition 2(Posterior consistency, stationary regime).
Fix(a, k)and assume the utility distribution at(a, k)is
stationary with finite variance and meanµa,k u . With no dis-
count (γ= 1), the Q-posterior meanθa,k q converges almost
surely toµa,k u as the cell’s pull countna,k → ∞. The same
holds for the C-posterior andµa,k c .
Proof.Let{u (i) t }n i=1betheutilityobservationsincell(a, k)
afternpulls. By (A1), observations within this stationary
cellarei.i.d.;thestronglawoflargenumbersthereforegives
Sa,k t /na,k t =n −1 P i u(i) t →µ a,k u almost surely. Divid-
ing the first expression in Eq. (16) byna,k t in numerator
and denominator givesθa,k q →µ a,k u becauseκ q/na,k t →0.
The cost posterior is identical with¯ca, Sc a,k t , κc in place of
µ0,q, Sa,k t , κq.
B.4 Lemma: discounted effective sample size
Lemma 1(Effective sample size).For anyγ∈(0,1)and
any sequence of pulls of cell(a, k),
na,k t ≤ 1−γ t+1 1−γ ≤ 1 1−γ .
The first bound is tight when(a, k)is pulled at every round.
Proof.IfT a,k t ⊆ {0, . . . , t}is the set of pull rounds for
cell(a, k), the round-based discount rule givesn a,k t =P
s∈T a,k t γt−s ≤ Pt j=0 γj = (1−γ t+1)/(1−γ).
B.5 Stationary analysis
We now turn from posterior properties to the stationary
decision rule. Under the well-specified product-Gaussian
model and clean-score restriction, PA-DCT induces a two-
dimensional linear Gaussian Thompson-sampling problem.
Theorem 1(Clean-score regret reduction to Gaussian
Thompson sampling).Under (A1), (A2′), (A3′), andγ= 1,

Symbol Meaning Domain / locked value
Rounds, arms, and context
t, TRound index and horizont∈ {0, . . . , T−1};T= 10,000
a, KProvider arm and number of armsK= 5: P-cheap, P-mid, P-premium, P-adv, P-flaky
at Arm selected at roundt a t ∈ At
xt Task context Released encoder:d= 7(task-type one-hot, difficulty, and
two wallet features drawn fromHt)
Ht Pre-selection information available to the policy Context, wallet state, affordable set, exposed provider
metadata, and past purchase feedback
k(xt), Kb Task-type bucket map used by PA-DCT T1/T2/T3a/T3b;K b = 4
Payment loop and feedback
Qt Quoted candidate set from discovery/pricing Provider–price pairs before selection
pa,t Provider charge at roundtMay drift; used for affordability and may be exposed as
listed-price metadata
At Affordable set, exposed as a mask before selectionA t ={a:p a,t ≤B t}
qt Observed quality of the chosen arm[0,1]
ft Paid non-delivery flag (timeout, parse failure){0,1}
ct Realized chargec t =p at,t, in USDC
B, Bt Initial and remaining budgetB= $50;B t+1 =B t −c t
τCompleted purchases before termination or horizon endτ≤T
Reward and wallet pressure
νFailure penalty in utilityν= 0.5
ut Utility: failure-penalized quality; updates the Q-posterioru t =q t −νf t
cmax,˜ct Cost normalizer and normalized costc max = $0.01;˜ct = clip(ct/cmax,0,1)
burn_devt Deviation of the realized spend rate from the linear planburn_dev t = (B−Bt)/B t/T −1fort >0;burn_dev 0 = 0
α, λ0 Budget-pressure schedule constantsα= 2.0,λ 0 = 1
λt, λnorm Raw and normalized wallet-pressure weightsλ t =λ 0 exp(αburn_dev t);λ norm =λ t/(1 +λ t)
rt Payment-aware rewardr t = (1−λ norm)ut −λ norm˜ct
PA-DCT posteriors and selection
¯ca Initially listed cost of armaPrior mean of the C-posterior
µ0,q, σ2 0,q, σ2 q Q-prior mean, prior variance, and likelihood variance0.5,1.0,0.09
σ2 0,c, σ2 c C-prior variance and likelihood variance10 −4,10 −6
na,k t ,¯na,k t Post-feedback and selection-time discounted counts of cell
(a, k)
Shared by the Q- and C-posteriors
Sa,k t , Sc a,k t Discounted utility and cost sums (barred: selection-time) New observations update only the chosen arm–bucket cell
γCommon discount of the Q- and C-posteriors0.999in main results
θa,k q ,Σ a,k q Q-posterior mean and variance Normal–Normal posterior over utility
θa,k c ,Σ a,k c C-posterior mean and variance Normal–Normal posterior over realized cost
ˆua,k,ˆca,k Thompson samples drawn at decision time From the Q- and C-posteriors
ˆra Decision-time sampled payment-aware reward Mirrorsr t with sampled utility and clipped sampled cost
Reported evaluation quantities
¯qT Full-horizon mean quality Exhausted rounds count asq t = 0
Rπ T ,PA-Reg T Cumulative PA reward and empirical PA-regretPA-Reg T =R Oracle T −R π T; reported as PA-gap/T
ROIQuality per dollar Efficiency diagnostic only
AdaptTShock-response diagnostic in S2/S3 Rounds to the first qualifying ROI window; defined in
Appendix C
Table5:Compactnotationlegend.Definitionsremaininthemaintext;thistablerecordsconventionsandthelockedvaluesused
in all reported experiments.
define thepolicy-state PA-regretof clean-score PA-DCT
against the wallet-coupled oracle as
gt(a) := (1−λ norm)µ a,kt u −λ norm µa,kt c /cmax,
PA-RegT :=
T−1X
t=0

gt(a⋆ t )−g t(at)  ,
(17)
wherea ⋆ t ∈arg max a∈At gt(a)at the policy’s wallet pres-
sureλ norm, anda t is PA-DCT’s chosen arm. Conditional
on the bucket-visit sequence, clean-score PA-DCT reduces
to per-bucket Gaussian Thompson sampling with a time-
varying linear context. For a bucket visitedTk times,
E
h
PA-Regcellk Tk
i
≤C 0
p
K Tk logT k,(18)
for a constantC 0 depending on the prior and likelihood
variances and oncmax. Aggregating acrossKb buckets withP
k Tk =Tgives
E[PA-RegT ]≤C
p
K Kb TlogT .(19)

Proof.For a visit to bucketk, writewt =λ norm and define
the observed feature
ϕt = (1−w t,−w t/cmax), θ a,k = (µa,k u , µa,k c ).
Theng t(a) =ϕ ⊤ t θa,k. Under (A2′), the independent Q/C
Thompson samples used by PA-DCT imply
(1−w t)ˆua,k −w tˆca,k/cmax
∼ N

ϕ⊤ t (θa,k q , θa,k c ),(1−w t)2Σa,k q +w 2 t Σa,k c /c2 max  ,
which is exactly the product-Gaussian posterior sample of
ϕ⊤ t θa,k. This identifies the sampled score with a Gaussian
posterior draw for the induced linear payoff.
The featureϕ t, bucketk t, and affordable setAt are ob-
served before sampling. Bucket visits are determined by the
exogenous task stream in §3, so conditioning on a bucket
subsequencedoesnotintroducepolicy-dependentcontextse-
lection;thewalletpressureandaffordablesetarepredictable
statesharedbythepolicy-statecomparatorinEq.(17).There-
foretheper-roundgapisthestandardcontextualThompson-
sampling regret for at mostKarms.
Consequently,oneachbucketsubsequencetheclean-score
policy is mathematically equivalent to Gaussian Thompson
samplingontheinducedlinearpayoff.ApplyingtheBayesian
regret bound forK-armed Gaussian-prior Thompson sam-
pling(LattimoreandSzepesvári2020,Ch.36)givesEq.(18);
the underlying confidence-bound decomposition of poste-
rior sampling (Russo and Van Roy 2014, Prop. 1) carries
overbecauseϕ t andA t areH t-measurable,sotheposterior-
matching identity holds conditionally onHt. Summing over
buckets and using Cauchy–Schwarz,
X
k
p
Tk logT k ≤
p
KbTlogT .
This gives Eq. (19).
B.6 Nonstationary analysis
We next isolate how exponential discounting removes stale
evidenceafteranabruptchange.Theresultpermitsanyfixed
or reward-noise-independent revisit schedule, followed by a
continuous-pull corollary with an explicit recovery horizon.
Theorem 2(Adaptation rate under an abrupt change, fixed
schedule).Fixγ∈(0,1)and cell(a, k). Suppose the true
utility mean shifts between roundst⋆ −1andt ⋆, with pre-
shock meanµold, post-shock meanµnew, and∆ =|µ old −
µnew|.Consideranyfixed,orreward-noise-independent,pull
scheduleforthiscellcoveringpre-andpost-shockpulls,with
post-shock pull rounds{s1 <· · ·< sm} ⊆[t⋆, t]. Define
A:=γ t−t⋆+1na,k t⋆−1,
B:=
mX
i=1
γt−si ,
κq :=σ 2 q /σ2 0,q.
HereAisthediscountedmassofstalepre-shockobservations
andBis the mass of new post-shock observations. Then the
Bayesian Q-posterior mean satisfies

 E[θa,k q,t ]−µ new

 ≤ A∆ +κ q|µ0,q −µ new| κq +A+B ,(20)
where the expectation is over observation noise for the fixed
schedule.
Remark1 (Two regimes).The bound (20) separates a prior
term from a stale-data term. Whenκq ≫A+B, the prior
controls the bias. Whenκq ≪A+B, the leading term is
∆A/(A+B), which is reduced by discounting and by new
post-shock pulls.
Corollary 1(Recovery horizon, data-dominated regime).
Suppose(a, k)is pulled at every post-shock round, so
ℓ:=t−t ⋆ + 1 =m,andassumethedata-dominatedregime
κq ≪A+B. Then

 E[θa,k q,t ]−µ new

 ≲∆γ ℓ +O  κq/(A+B)  ,
and the leading stale-data term is at mostδonce
ℓ≥ log(∆/δ) log(1/γ) =O  log(∆/δ)/(1−γ)  .
Proof of Theorem 2.Because the entire pull schedule is
fixedorindependentoftherewardnoise,conditioningonthe
pulltimesdoesnotchangethemeanoftheincludedobserva-
tions; in particular, the pre-shock massna,k t⋆−1 is determined
by the schedule. From Eq. (16),
θa,k q,t = κqµ0,q +S a,k t
κq +n a,k t .
Splitting the discounted mass into pre- and post-shock pulls
givesn a,k t =A+BandE[S a,k t ] =Aµ old +Bµ new.Hence
E[θa,k q,t ]−µ new = κq(µ0,q −µ new) +A(µ old −µ new) κq +A+B .
Taking absolute values and using|µold −µ new|= ∆gives
Eq. (20).
Proof of Corollary 1.Ifthecellispulledateverypost-shock
round, thenB= Pℓ−1 j=0 γj = (1−γ ℓ)/(1−γ)andA=
γℓna,k t⋆−1. By Lemma 1,na,k t⋆−1 ≤1/(1−γ), so
A
A+B ≤ γℓ/(1−γ) γℓ/(1−γ) + (1−γ ℓ)/(1−γ) =γ ℓ.
Substituting this into Eq. (20) yields the displayed bound;
solving∆γ ℓ ≤δgives the stated horizon.
Remark2 (Cost-posterior analogue).The same calculation
appliestorealized-costshocks:replace(µ old, µnew, µ0,q, κq)
with(µ c old, µc new,¯ca, κc)andusetheC-posteriorstatisticun-
der the same locked discountγ. This is the algebra behind
S3-stylepricechangesoncethechangedarmispulledagain;
we state the utility version to avoid duplicating notation.
B.7 Scope of the formal analysis
The results above are component-level formal support, not
a complete regret theorem for the full replay system. The
stationaryregretreductionassumesawell-specifiedproduct-
Gaussian model,γ= 1, and the clean score with inactive

cost-sample clipping; the implemented clipped scorer coin-
cides with this policy on trajectories where the clip is inac-
tive. The adaptation result is conditional on a fixed, noise-
independentpullschedule:itexplainshowdiscountedposte-
riorsforgetstaleevidenceafterachangedarmisrevisited,but
it does not prove an unconditional Thompson-sampling re-
visit rate or a cumulative piecewise-stationary regret bound.
Finally,thetheorem’scomparatorusesthepolicy’sownwal-
let pressure and affordable set, whereas the empiricalTrue
Oraclehas its own wallet trajectory.
C Detailed Ablation Study
Thisappendixreportsthefullmetricsbehindthecomponent-
role analysis in §6.4 of the main paper. The four primary
variants each modify one component of Full PA-DCT:−P
removes payment-aware ranking and scores providers by
sampled utility alone;−Dremoves discounting (γ= 1);
−Cremoves contextual bucketing by collapsing the four
task-type buckets into one; and−TSreplaces Thompson
samples with posterior means. The additional price-shock
diagnostic−C post retains wallet pressure but pins the cost
estimate to the specification cost¯ca and is evaluated only in
S3. PA-gap/Tand full-horizon mean quality are reported as
endpoint metrics, whereas ROI and AdaptT serve as diag-
nostics.AdaptTisthenumberofroundsaftertheshockuntil
the first trailing-200ROI window reaches95%of pre-shock
ROIinS2or110%inS3.WeaverageAdaptToverseedsthat
cross the threshold and report the corresponding hit count
out of30.
Two reading notes accompany Table 6. First, the−Prow
inS2reportsAdaptToveronlythe14/30seedsthatreached
the ROI threshold before exhausting the wallet. Its reported
AdaptT is thereforeconditional on the successful subsetand
should not be compared directly with the full-hit rows. Sec-
ond,−Pand Contextual DS-TS in Table 4 implement the
samewallet-pressure-freeselectionrulethroughindependent
codepathsandRNGstreams.TheirPA-gap/Tvaluesdifferby
atmost0.007acrossscenarios,providinganimplementation-
level consistency check.
D Sensitivity and Robustness Checks
This appendix reports the sensitivity checks behind the
locked configuration in §6.1 of the main paper. We first
sweep the four exposed selection scalars one at a time on
S1, use the ablation panel for the cross-scenario discount
check, and treat posterior variances,T, andBas fixed cali-
bration constants rather than per-scenario tuning knobs. We
then examine comparator-specific sweeps, the SW-TS diag-
nostic, and paired-seed statistical checks. Throughout, the
goal is to verify that the locked configuration is a reason-
able calibration, not to search for a better one. Comparator
implementation details remain in Appendix F.
D.1 Targeted S1 sensitivity sweep
Each non-default row in Table 7 changes one scalar while
holding the others fixed, using10seeds atT= 10,000. The
TrueOracleisrecomputedforeachcellwiththesameνand
cmax as the tested policy, so PA-gap/Tremains comparable
within the sweep.
The sweep supports two narrow claims. First, the locked
policy is not brittle: no cell bankrupts the wallet,¯qT stays
within[0.753,0.802],andPA-gap/Tremainsinthesameor-
derofmagnitude.Second,thevisibleleversaretheintended
ones: shorter memory worsens stationary performance, and
largerαspends more aggressively;νandc max have smaller
effects in the tested range.
D.2 Discount factorγ
The cross-scenario check uses the−Drows of Table 6: full
PA-DCT setsγ= 0.999, while−Dsetsγ= 1. On S1,
no discount is slightly better on the stationary endpoints,
but discounting shortens AdaptT in both shock scenarios
(1,467vs.2,249rounds in S2;200vs.279in S3). This is
the empirical counterpart of Cor. 1, where stale evidence
decays asγ ℓ after a changed arm is revisited. The default
γ= 0.999correspondstoaneffectivehorizonof1/(1−γ) =
103 rounds, chosen to retain S1 evidence while still reacting
inside the S2 outage window.
D.3 Other locked constants
The failure penaltyν= 0.5gives billed timeouts a cost
beyond their zero quality score; the sweep shows that halv-
ing or doubling it barely moves the metrics. Likewise, the
pressure schedule usesα= 2andλ 0 = 1, soλ norm = 0.5
whenspendingisonplanandrisessmoothlyundersustained
overshoot; the sweep confirms the expected spend trade-off
betweenα= 1andα= 4. The normalizerc max = $0.01is
the highest listed provider price, and the half/double sweep
does not change the qualitative conclusion.
Theposteriorpriorandlikelihoodvariancesareintention-
ally not swept: the Q-posterior uses a broad mid-range prior
withmoderateproxynoise,whiletheC-posteriorusesatight
priorandlikelihoodbecauserealizedcostisnearlydetermin-
isticexceptattheS3priceshock.WealsodonotsweepTor
B: the released benchmark fixesT= 10,000, andB= $50
is calibrated so that a premium-only policy hits the budget
cliff in the second half of the run.
D.4 Comparator sensitivity sweeps
Table 8 sweeps the PM-Greedy thresholdθ PM and the
LinCBwK-Adapt exploration coefficientβ; the main table
uses the locked settingsθPM = 0.7andβ= 1.0. Reducing
eitherθ PM orβimproves the corresponding comparator’s
PA-gap/Tin every scenario. For reference, PA-DCT’s mean
PA-gap/Tvalues in the main results (Table 4 of the main
paper) are0.133,0.166, and0.121in S1–S3. Across these
comparator sweeps, PA-DCT retains the lowest mean PA-
gap/Tamong the tested settings, with the margin largest in
S1/S2 and narrower in S3.
D.5 SW-TS diagnostic
SW-TS adapts sliding-window Thompson sampling (Trovò
et al. 2020) to our admissible loop. It maintains a non-
contextual Gaussian reward posterior per arm over utility
observations from the lastW= 1000global rounds and

Scenario Variant
PA-gap/T
↓ROI↑
Mean quality
↑
AdaptT
(rounds)↓
S1 Full0.133±0.004 378 0.797n/a
S1−P0.855±0.058 111 0.555 ‡ n/a
S1−D0.109±0.008 412 0.810n/a
S1−C0.116±0.003 390 0.812n/a
S1−TS 0.130±0.046 535 0.740n/a
S2 Full0.166±0.006 357 0.761 1,467(30/30)
S2−P0.878±0.050 103 0.517 ‡ 1,611(14/30)
S2−D0.170±0.012 399 0.745 2,249(30/30)
S2−C0.158±0.006 368 0.761 1,176(30/30)
S2−TS 0.175±0.048 537 0.687 1,125(30/30)
S3 Full0.121±0.004 429 0.831 200(30/30)
S3−P0.259±0.036 351 0.840 200(30/30)
S3−D0.114±0.009 426 0.838 279(30/30)
S3−C0.109±0.003 425 0.848 398(29/30)
S3−TS 0.145±0.025 552 0.742 2,232(24/30)
S3−C post 0.144±0.005 423 0.797 200(30/30)
Table 6: Full component-ablation metrics on 402Pilot-Bench. PA-gap/Tis mean±SD over30paired seeds; ROI and quality
entries are means. AdaptT is the mean elapsed rounds over hit seeds (hits/30), is lower-bounded by200, and is a diagnostic
rather than an endpoint.‡ indicates that all30seeds exhausted the wallet beforeT;n/adenotes a scenario without a shock.
Setting¯q T Budget % ROI PA-gap/T
default0.796±0.001 42.2±0.3 377.5±2.1 0.1328±0.0013
γ= 0.99 0.753±0.001 49.8±0.2 302.4±1.3 0.2087±0.0013
γ= 0.9995 0.801±0.002 40.8±0.4 392.6±3.3 0.1218±0.0016
ν= 0.25 0.795±0.001 42.1±0.4 377.6±3.0 0.1329±0.0018
ν= 1.0 0.797±0.001 42.1±0.3 378.7±2.3 0.1324±0.0014
α= 1.0 0.788±0.002 36.7±0.3 430.3±3.1 0.1045±0.0011
α= 4.0 0.802±0.001 54.7±0.4 293.5±2.0 0.1781±0.0016
cmax = 0.005 0.787±0.001 41.9±0.4 375.9±3.0 0.1567±0.0028
cmax = 0.02 0.800±0.001 50.5±0.3 316.8±1.9 0.1490±0.0021
Table 7: One-at-a-time S1 sensitivity of PA-DCT. Means±SE over10seeds; each non-default row perturbs a single scalar.
samples one utility draw per affordable arm. The window is
indexed by global rounds: observations are timestamped by
global round index and pruned once older thanWrounds,
whether or not the arm was recently pulled; if an arm’s ac-
tivewindowisempty,theposteriorrevertstotheprior(mean
0.5,variance1.0,likelihoodvariance0.09).SW-TSdoesnot
learncostandhasnowallet-pressureterm;theaffordable-set
mask is its only budget signal.
Table9reportstheSW-TSendpointmetrics.Forbankrupt
seeds,aggregatemetricsarecomputedoverthefullhorizon,
with post-bankruptcy rounds contributing zero quality and
nofurtherspend.Withoutwalletpressure,SW-TSrepeatedly
selects high-quality expensive arms; in S1/S2 this drains the
wallet for all30seeds.
D.6 Paired-seed statistical comparisons
For each scenario–metric pair, we compare PA-DCT with
eachbaselineusingthe30within-seeddifferences.Reported
p-values use two-sided paired normal-approximation tests.
As a robustness check against skew from early budget ex-
haustion,wealsocompute95%paired-bootstrapconfidence
intervals with10,000resamples; these intervals support the
same conclusions.
PA-DCT’s S3 improvements over Always-P-mid on qual-
ity, ROI, and PA-gap/Tare significant (allp <10−20), as is
itsS2qualitygainoverAlways-P-mid(p= 1.67×10 −3).Its
S1PA-gap/TdisadvantageagainstAlways-P-midisalsosig-
nificant, consistent with exploration cost. In S2, PA-DCT’s
PA-gap/Tis not distinguishable from Always-P-cheap (p=
0.17) or Contextual BTS (p= 0.86). Against PM-Greedy,
LinCBwK-Adapt, and Contextual DS-TS, its PA-gap/Tad-
vantage is significant in all three scenarios.
E Allocation Dynamics under Market Shocks
Aggregatemetricssummarizetheoverallquality–costtrade-
off but do not show how the policy reallocates over time.
Figure 2 reports PA-DCT’s provider-allocation trajectories
across the three market scenarios. S1 serves as a station-
ary control; S2 shows withdrawal from and return to P-
mid around the outage; and S3 shows migration toward
discounted P-premium. These trajectories complement the
AdaptT diagnostic in Table 6 by showing when and how

Setting Scenario¯q T Budget % PA-gap/T
PM-Greedy quality thresholdθPM
θPM = 0.6S10.776 55.3 0.244
θPM = 0.6S20.733 80.6 0.364
θPM = 0.6S30.793 35.4 0.152
θPM = 0.7S10.732 89.5 0.542
θPM = 0.7S20.627 98.7 0.660
θPM = 0.7S30.836 43.9 0.198
θPM = 0.8S10.667 94.6 0.684
θPM = 0.8S20.581 99.1 0.763
θPM = 0.8S30.836 46.8 0.243
LinCBwK-Adapt exploration coefficientβ
β= 0.5S10.803 70.0 0.312
β= 0.5S20.773 83.5 0.386
β= 0.5S30.806 37.8 0.164
β= 1.0S10.824 93.0 0.457
β= 1.0S20.796 99.9 0.515
β= 1.0S30.836 44.5 0.195
β= 2.0S10.832 100.0 0.515
β= 2.0S20.800 100.0 0.533
β= 2.0S30.854 45.7 0.197
Table 8: One-at-a-time sensitivity sweeps for PM-Greedy
and LinCBwK-Adapt. Means over30paired seeds.
Scenario¯q T Budget % ROI PA-gap/TBankrupt
S10.483 100.0 97 0.981 30/30
S20.466 100.0 93 0.986 30/30
S30.855 52.3 328 0.324 0/30
Table 9: SW-TS appendix results. Means over30paired
seeds; bankruptcy is the number of seeds that exhausted the
wallet beforeT= 10,000.
provider allocation changes.
F Extended Comparators
F.1 Comparator Implementations
Thissectiondescribeshoweachcomparatorisimplemented
in402Pilot-Benchunder the common frozen-replay eval-
uation protocol. Where necessary, standard algorithms are
minimally adapted to operate under replay while preserving
their original decision principles. All non-oracle implemen-
tations receive the same task context and hard affordable-set
mask. After each decision, the loop reveals only the chosen
provider’s failure-penalized utility and realized receipt cost;
each implementation uses only the signals specified below.
No comparator observes counterfactual cached outcomes,
and no learning comparator uses a forced round-robin warm
start.
Randomandfixed-armpolicies.WeimplementRandom
by sampling uniformly from the affordable set. Always-P-
cheap, Always-P-mid, and Always-P-premium return their
namedproviderwhenitisaffordableandotherwisereturnthe
first provider in the runtime’s fixed affordable-set ordering.
These policies ignore context and replay feedback.
Figure 2: PA-DCT provider-allocation shares overT=
10,000rounds in, from top to bottom, the stationary mar-
ket (S1), reliability-shock scenario (S2), and price-shock
scenario (S3). In S1, P-mid remains dominant after initial
exploration.In S2,the policyshiftsaway fromP-midduring
its outage and returns after recovery. In S3, it reallocates to-
ward discounted P-premium.
BudgetRule.We implement BudgetRule as a determinis-
tic wallet-threshold policy. It selects P-premium when the

remaining-budget fraction is above0.50, P-mid when it lies
in(0.20,0.50],andP-cheapotherwise.Ifthetargettierisun-
available, it selects the affordable provider with the highest
catalog price. It ignores context and replay feedback.
Contextual DS-TS.In our implementation, Contextual
DS-TS adapts discounted Thompson sampling (Qi, Wang,
and Zhu 2023) to four task buckets and continuous util-
ity feedback. It maintains one Gaussian utility posterior per
provider–task-bucket cell, discounts every cell’s sufficient
statisticsonceperreplayround,andsamplesoneutilityvalue
for each affordable provider in the current bucket. Only the
chosen cell is updated. Receipt cost and wallet state do not
enter the rule beyond the runtime’s affordable-set mask.
Contextual BTS.In our replay implementation, Contex-
tual BTS adapts budgeted Thompson sampling (Xia et al.
2015) to four task buckets and continuous utility and cost
feedback. It maintains stationary Gaussian utility and cost
posteriors for each provider–task-bucket cell, with each cost
prior centered at that provider’s catalog price. For every
affordable provider, it samples both quantities and selects
the largest sampled utility-to-cost ratio; the sampled cost is
flooredat10 −6 USDC.Onlythechosencellisupdatedfrom
itsutilityandreceiptcost,andwalletstateentersonlythrough
affordability.
PM-Greedy.PM-Greedy is implemented as a price-
metadata router inspired by cheapest-sufficient rout-
ing (Chen, Zaharia, and Zou 2024). For each provider–task-
bucket cell, it keeps a per-pull window of the500most re-
cent observed utilities; a cell with no observations yet uses
theoptimisticestimate1.Amongaffordableproviderswhose
mean utility is at least0.7, it selects the one with the lowest
scenario-aware posted price, breaking price ties by higher
estimated utility. If none clears the threshold, it selects the
highest-utility provider, breaking ties by lower posted price.
Receipt cost is not used for learning, and the affordable-set
mask is the only wallet signal.
LinCBwK-Adapt.Our replay adaptation of
LinCBwK (Agrawal and Devanur 2016) is an admis-
sible empirical comparator rather than a reproduction of the
fulltheoreticalalgorithm.Withthefour-dimensionalone-hot
task context, its linear reward and cost models reduce to
stationary Gaussian/ridge estimates for each provider–task-
bucket cell. It normalizes receipt cost byc max = $0.01
and scores affordable providers byUCB r −µLCB c.
Before each selection,µis increased by0.01when the
remaining-budget fraction is below the remaining-horizon
fraction and decreased by0.01otherwise, subject to the
range[0,100]. Only the chosen cell’s utility and normalized
receipt cost are updated; no temporal forgetting is applied.
Replay True Oracle.We implement the replay True Ora-
clewithanindependentwallettrajectory.Forthesamereplay
taskandcached-responseversion,itinspectstherealizedout-
comeofeveryprovideraffordableunderthatwallet,evaluates
each using the oracle wallet’s current payment pressure, and
selects the provider with the highest payment-aware reward.
Only the selected receipt is charged. This counterfactual ac-
cess makes the oracle unattainable and suitable only as an
upper bound.
F.2 Comparator Configurations
Table10reportsthefixedconfigurationsofcomparatorswith
explicitpolicyparameters,includingtheappendix-onlySW-
TS diagnostic of Appendix D.5.
Alignment and numerical guards.Contextual DS-TS
sharesPA-DCT’sQ-prior,likelihoodvariance,anddiscount.
Contextual BTS shares PA-DCT’s Q/C prior settings and
likelihood variances but removes discounting, reducing dif-
ferencesduesolelytopriorcalibration.LinCBwK-Adaptin-
stead uses narrower ridge-style prior variances and does not
seeditsnormalized-costpriorfromcatalogprices.The10 −6
cost floors in Contextual BTS and LinCBwK-Adapt prevent
sampledorlower-confidencecostsnearzerofromdestabiliz-
ing their selection scores.
G x402 Integration Witness
The released artifact includes a local x402 integration wit-
nessforthePaymentExecutorboundarydescribedin§4
of the main paper. The witness demonstrates that a selected-
provider purchase can execute as a real HTTP 402 quote–
pay–receiptloop.Itisseparatefrom402Pilot-Benchandcon-
tributes no reported measurements. The local setup consists
of an Anvil fork containing USDC contract state, a Python
x402 facilitator for verifying and settling exact EVM pay-
ments, a FastAPI resource server exposing x402-protected
provider endpoints, and anX402PaymentExecutor
adapter that maps the HTTP 402 exchange to a 402Pilot
Outcome.
Runtime environment.The reported benchmark experi-
ments are deterministic, CPU-only frozen-replay runs con-
ductedonaMacBookProwithanAppleM2Maxand32GB
unified memory. The released artifact pins the software de-
pendencies and exact versions. The integration witness ad-
ditionally requires a local Anvil instance, the Python x402
facilitator, and the FastAPI resource server. Runningbash
scripts/witness_smoke.shexercises both the un-
paid HTTP 402 response and a paid request, and verifies a
valid payment receipt together with the corresponding de-
crease in the buyer’s local Anvil USDC balance.

Comparator Configuration
BudgetRule High and low remaining-budget thresholds are0.50and0.20, respectively.
Contextual DS-TSK b = 4; Q-prior mean, prior variance, and likelihood variance(0.5,1.0,0.09); wall-clock discount
γ= 0.999.
Contextual BTSK b = 4; Q settings(0.5,1.0,0.09); C-prior mean¯ca; C-prior and likelihood variances(10−4,10 −6);γ= 1;
sampled-cost floor10−6 USDC.
PM-GreedyK b = 4; per-pull windowW= 500; utility thresholdθPM = 0.7; optimistic initial estimateˆuinit = 1.
LinCBwK-AdaptK b = 4; reward and normalized-cost prior means0.5; corresponding prior and likelihood variances0.09;
γ= 1;c max = $0.01;β= 1.0; dual stepη= 0.01and range[0,100]; cost-LCB floor10 −6.
SW-TS diagnostic Non-contextual; wall-clock windowW= 1000; reward-prior mean and variance(0.5,1.0); likelihood
variance0.09.
Table10:Comparatorconfigurationsusedinthereportedexperiments.Parametersarefixedacrossscenariosandrandomseeds
unless explicitly varied in Appendix D.
References
Agrawal, S.; and Devanur, N. R. 2016. Linear Contextual
BanditswithKnapsacks. InAdvancesinNeuralInformation
Processing Systems, volume 29.
Chen, L.; Zaharia, M.; and Zou, J. 2024. FrugalGPT: How
to Use Large Language Models While Reducing Cost and
ImprovingPerformance.TransactionsonMachineLearning
Research.
Lattimore, T.; and Szepesvári, C. 2020.Bandit Algorithms.
Cambridge University Press.
Qi, H.; Wang, Y.; and Zhu, L. 2023. Discounted Thomp-
son Sampling for Non-Stationary Bandit Problems.arXiv
preprint arXiv:2305.10718.
Russo, D.; and Van Roy, B. 2014. Learning to Optimize via
Posterior Sampling.Mathematics of Operations Research,
39(4): 1221–1243.
Trovò, F.; Paladino, S.; Restelli, M.; and Gatti, N. 2020.
Sliding-Window Thompson Sampling for Non-Stationary
Settings.Journal of Artificial Intelligence Research, 68:
311–364.
Xia,Y.;Li,H.;Qin,T.;Yu,N.;andLiu,T.-Y.2015. Thomp-
son Sampling for Budgeted Multi-Armed Bandits. InPro-
ceedings of the 24th International Joint Conference on Arti-
ficial Intelligence, 3960–3966.
