---
title: 'Big Bird: Resilient Privacy Budgeting Across Untrusted Web Domains'
url: https://arxiv.org/abs/2506.05290
category: privacy-data
subcategory: measurement
date: 2025-06
venue: arXiv (Cornell University)
authors:
- Pierre Tholoniat
- Alison Caulfield
- Giorgio Cavicchioli
source: arxiv
pdf_url: https://arxiv.org/pdf/2506.05290
pages: 35
chars: 164529
fetched_at: '2026-11-08T12:59:11+00:00'
kb_version: 1
---

# Big Bird: Resilient Privacy Budgeting Across Untrusted Web Domains

Big Bird: Resilient Privacy Budgeting Across Untrusted
Web Domains
Pierre Tholoniat∗
Columbia University
Alison Caulfield∗
Columbia University
Giorgio Cavicchioli
Columbia University
Mark Chen
Columbia University
Benjamin Case
Meta Platforms, Inc.
Asaf Cidon
Columbia University
Roxana Geambasu∗
Columbia University
Mathias Lécuyer
University of British Columbia
Martin Thomson
Mozilla
Abstract
The W3C Attribution API is an emerging standard for
privacy-preserving advertising measurement. Its current
privacy architecture enforces individual differential privacy
(IDP) independently for each domain (e.g., an advertiser)
issuing queries. We show that this guarantee is unsound
under realistic system behavior: it fails under cross-querier
data adaptivity and can also fail when shared limits are
enforced across queriers. The issue is not the on-device
accounting model itself – device-epoch IDP – but treating
each querying domain in isolation. We propose Big Bird, a
privacy-budget manager that makes global device-epoch
IDP – enforced jointly across all domains – both sound and
deployable for Attribution. Big Bird addresses the main ob-
stacle to global enforcement in open multi-querier systems:
denial-of-service depletion of a shared global budget by
Sybil web domains. Its key insight is that benign Attribution
workloads have a stock-and-flow structure: impressions
create potential privacy loss, conversions realize it, and
meaningful budget consumption should be tied to genuine
user actions across distinct web domains. Big Bird enforces
this structure with privacy-loss-based quotas on impression
and conversion sites and a per-user-action cap on how many
quotas can be activated, ensuring that adversarial impact
scales with genuine user interactions rather than with the
number of Sybil domains. We implement Big Bird in Rust,
integrate it into Firefox’s Attribution prototype, and evaluate
it theoretically and empirically on real ad-tech data. We
show that Big Bird provides rigorous global device-epoch
IDP, formal resilience to depletion attacks, and utility for
benign queriers under attack.
∗Contributions made at Columbia University. P.T. is now at Google. A.C.
and R.G. were also affiliated with Microsoft and Meta, respectively.
This work is licensed under a Creative Commons Attribution 4.0 Interna-
tional License.
SOSP ’26, Prague, Czech Republic
©2026 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-2585-2/26/09
https://doi.org/10.1145/3830418.3843897
CCS Concepts:•Security and privacy;
Keywords:Differential Privacy, Web, Measurement
ACM Reference Format:
Pierre Tholoniat, Alison Caulfield, Giorgio Cavicchioli, Mark Chen,
Benjamin Case, Asaf Cidon, Roxana Geambasu, Mathias Lécuyer,
and Martin Thomson. 2026. Big Bird: Resilient Privacy Budget-
ing Across Untrusted Web Domains. InSymposium on Operat-
ing Systems Principles (SOSP ’26), September 29–October 2, 2026,
Prague, Czech Republic.ACM, New York, NY, USA, 35 pages.https:
//doi.org/10.1145/3830418.3843897
1 Introduction
An important new standard is taking shape at the W3C: the
Attribution API, designed to enable privacy-preserving ad-
vertising measurement at web scale [ 33, 43]. Advertising
measurement is a core economic function of the web, yet
today it relies heavily on cross-site tracking mechanisms
such as third-party cookies and fingerprinting, which under-
mine user privacy and have proven difficult to regulate or
replace. Attribution aims to provide a principled alternative:
a browser-mediated interface for cross-site measurement
that replaces raw data collection with structured, differen-
tially private aggregation.
At a high level, Attribution enables tasks such as con-
version attribution measurement – linking ads viewed on
content sites to purchases on seller sites – while ensuring
that only noisy aggregate statistics are released. Browsers
mediate all raw-data flows, store user activity locally, and re-
lease encrypted reports that are aggregated with differential
privacy (DP), eliminating the need for cross-site tracking or
centralized user-level data collection.
A key feature of Attribution is device-side privacy account-
ing based on individual differential privacy (IDP), which we
developed for Attribution in prior work, Cookie Monster [43].
Each browser enforces a per-epoch privacy budget for each
querier (e.g., an advertiser), deducting privacy loss before
releasing reports. This design offers strong utility by charg-
ing privacy loss only when a user meaningfully contributes
to a query, and it has been adopted as the foundation of the
emerging standard – including its per-querier enforcement
scope. The standard is being developed with participation
arXiv:2506.05290v4  [cs.CR]  13 Sep 2026

from all major browsers; as of August 2026 it is in Wide-Area
Review, en route to Candidate Recommendation.
Given its role as aweb standard– not merely an implemen-
tation, and likely to be deployed across billions of devices
– scrutinizing Attribution’s privacy guarantees is essential
and urgent. We therefore ask: are its guarantees sound, and
can they be enforced robustly in practice?
Contribution 1:We show that Attribution’s central privacy
guarantee – device-epoch IDP enforced per querier – is fun-
damentally unsound under realistic system behavior. The
issue is not IDP or the device-epoch unit, but per-querier
enforcement. In multi-querier systems, privacy guarantees
must account for interactions across queriers. We identify
two failure modes: (1) cross-querier data adaptivity in stream-
ing settings causes privacy loss to exceed per-querier bounds,
even without collusion; and (2) introducing shared limits
across queriers, a common defense against collusion, also
violates per-querier guarantees. We prove these results in a
general DP system model, showing that the problem is not
specific to Attribution but reflects a fundamental mismatch
between per-querier enforcement and deployment realities.
Focusing on Attribution, we therefore advocate global
device-epoch IDP – enforced across all queriers – as the
sound privacy foundation. However, global enforcement in-
troduces a key systems challenge. In open environments
where any domain can invoke the API, a shared global pri-
vacy budget becomes vulnerable to denial-of-service deple-
tion: adversarial domains can exhaust users’ budgets, pre-
venting benign measurement.
Contribution 2:We present Big Bird, a global privacy-
budget manager for Attribution that provides both rigorous
global IDP enforcement and resilience to depletion attacks by
untrusted web domains. Big Bird is based on a key structural
insight: legitimate Attribution workloads exhibit a stock-
and-flow pattern of privacy consumption, where impressions
create potential privacy loss (stock) and conversions realize
it (flow), tied to genuine user actions across sites. Attacks
violate this structure by generating stock and flow without
corresponding user activity.
Big Bird restores this structure using coordinated, IDP-
aligned quotas on impression sites, conversion sites, and
per-user-action domain participation. These constraints en-
sure that privacy-budget consumption – whether benign or
adversarial – scales with genuine user interactions rather
than with the number of attacker-controlled (Sybil) domains.
We implement Big Bird in Rust as a generic IDP budget
management library,pdslib, integrate it into Firefox’s At-
tribution prototype, analyze it theoretically, and evaluate
it empirically on real ad-tech data. Our results show that
Big Bird enforces rigorous global device-epoch IDP, achieves
formal resilience to depletion attacks, and preserves utility
for benign workloads under attack.
user’s browser
aggregate results
aggregation
service⑦
MPC / TEE
+ DP
Attribution
Attribution
another
user’s
browser
⑥ encrypted reports
Attribution histogram returned
encrypted to adtech1.ex:
{ impression_1: $30,
  impression_2: $30,
 … other imp.:    $0 }
⑧
⑨
batch
saveImpression()
news.ex
① ③
⑤measureConversion()
Impression Store
impression
sites
conversion
sites
intermediary
sites
blog.ex
②
Report Generation Algorithm
(Alg. 1 of Cookie Monster paper)
(4.1) Retrieve matching impressions per epoch,
excluding ones from the current user action.
(4.2) Compute epoch-level IDP loss. Check
and deduct:
● Per-querier, per-epoch budgets
● Global, per-epoch budgets
Suppress epoch contribution if out of budget.
(4.3) Generate histogram attributing conversion
value to impressions across all epochs.
④
saveImpression()
shoes.ex
$60
ad-tech1.
ex
adtech1.
ex
encrypted report
Fig. 1. Attribution API architecture.
Both contributions are now part of the Attribution draft.1
Following the recommendation in §3.4, the specification
added a section recording our results as limitations of per-
querier semantics and discussing their implications [ 35].
The draft also adopted the Big Bird algorithm from §4 (Alg.
2) as its budget-management mechanism [ 34]. The latter
resolved an open issue [ 19]—DoS depletion of the global
safety limits—that the editors had flagged as a blocker to
the standard’s reaching the Wide-Area Review stage, which
it has since reached. We also release our source code as a
reference implementation for the standard as well as for
broader use cases: pdslib athttps://github.com/columbia/
pdslib, Firefox integration athttps://github.com/columbia/
pdslib-firefox, and experimental infrastructure athttps://
github.com/columbia/bigbird. Indeed, while we focus on
Attribution, our results have broader implications for DP
systems in untrusted querier settings: (1) multi-granularity
enforcement is fundamentally unsound, and (2) global bud-
get management requires depletion defenses aligned with
the structure of benign workloads. We view Big Bird as one
step toward this broader design space.
2 Background
2.1 Attribution API Architecture
W3C Attribution is a privacy-preserving, browser-based
interface for cross-site conversion measurement. Figure 1
shows the workflow, involving four principals, where .ex
denotes fictional example domains: (1)impression sites(e.g.,
news.ex,blog.ex) register shown ads via saveImpression();
(2)conversion sites(e.g.,shoes.ex) call measureConversion()
to request encrypted reports of which ads a user saw; (3)
intermediaries(e.g.,adtech.ex) receive encrypted reports; and
(4)aggregation services(e.g., divviup.org) aggregate reports
1B.C. and M.T. are specification editors [ 33]. All changes described here
were proposed, discussed, and adopted through the W3C public process.

and add DP noise using trusted MPC or TEE.
The browser mediates all information flows: impressions
are stored locally, conversions trigger encrypted reports, and
aggregators release only DP-protected statistics. A typical
sequence is: 1 – 2 impression sites record ads; 3 a conver-
sion site calls measureConversion(); 4 the browser fetches
relevant impressions, checks local privacy budgets, and 5
generates encrypted reports; 6 – 9 reports are batched, ag-
gregated, and released with DP noise via an aggregation
service.
Critically,privacy enforcement happens on-device. Before
releasing a report, the browser deducts the corresponding pri-
vacy loss from a localprivacy budget store, returning null re-
ports when budget is exhausted (4.2). This enforcement uses
an algorithm presented in the Cookie Monster paper [43].
2.2 Cookie Monster Accounting
Our prior work, Cookie Monster [43], proposed usingindi-
vidual differential privacy (IDP)[ 13, 14, 22] for efficient, on-
device privacy accounting in Attribution, and the accounting
it introduced is the one the standard adopted. We summarize
it here because both of this paper’s contributions build on it:
§3 revisits the scope of its guarantee, and §4 builds a budget
manager on top of its accounting.
Under IDP, each browser maintains its own privacy bud-
gets and deducts privacy loss based on the user’s actual
data contribution (theindividual sensitivity), rather than a
population-wide worst-case bound (thesensitivity) as in tra-
ditional DP. This distinction enables a crucial optimization
for Attribution. Advertising signals are sparse: many users
see ads but never convert; many conversions have no match-
ing impression; and users purchase different products and
therefore participate in different queries. Cookie Monster’s
accounting exploits this sparsity. Each device partitions its
data into non-overlapping epochs (e.g., one week), and when
a conversion occurs, the browser charges privacy lossonly
for epochs containing at least one impression relevant to that
conversion. If an epoch contains no such impression, the con-
version incurszeroprivacy loss for that device-epoch. When
a charge is applied, it is bounded by (value / maxValue)×𝜖 ,
using parameters from themeasureConversion()call.
This contrasts with traditional DP, where privacy loss
is charged for every query based on population-level sen-
sitivity, even if a device contributed no relevant data. For
Attribution, avoiding charges in irrelevant epochs is essen-
tial for utility: it reduces privacy loss for typical users and
allows many measurements before budgets are exhausted.
2.3 Queriers and Privacy Guarantees
Attribution performs privacy accountingwith respect to a
querier– the entity on whose behalf aggregation occurs. In
today’s API, the querier is theadvertisermeasuring its own
conversions. A planned extension will addintermediaries
as queriers for cross-advertiser queries (e.g., for training
ad-placement models). Each browser therefore maintains
per-epoch budgets per querier. We showed in Cookie Monster
that,when queriers are modeled in isolation, such per-querier
budgets satisfy device-epoch-level IDP [43].
The Attribution specification acknowledges a well-known
limitation: if queriers collude, their privacy losses add. To
mitigate this, the API introducesglobal safety limits– per-
epoch budgets spanning all queriers. In the current design,
per-querier budgets remain the primary enforcement mech-
anism, with global limits viewed as defense-in-depth.
3 Contribution 1: Per-Querier DP Analysis
Attribution’s focus on per-querier enforcement, with global
limits as defense-in-depth, is not unique. Several DP systems
have similarly proposed per-querier or per-analyst enforce-
ment [15, 16, 24, 43, 44] to align guarantees with organiza-
tional boundaries. Such guarantees are intuitively appealing,
especially when queriers can reasonably be assumed to act
independently and not collude (e.g., competing organizations
or scientists under IRB restrictions). Some of these systems
also, like Attribution, enforce DP at multiple granularities
for defense-in-depth [15, 24, 44].
Our analysis of per-querier guarantees – developed ini-
tially for Attribution but generalized here to broader DP
systems – shows that their limitations extend beyond col-
lusion. Any DP analysis has three components: (1) a for-
mal privacy property (definition, privacy unit, enforcement
scope), (2) a model of system behavior specifying how data
is generated and queried, and (3) a proof that the modeled
system satisfies the property. If the behavioral model omits
deployment-relevant behaviors that affect data generation
or querying, the proof may still be correctrelative to the
model, while the stated privacy property fails to capture the
system’s actual semantics.
We identify two recurring modeling gaps in analyses of
per-querier DP. First, existing models typically treat each
querier in isolation, neglecting cross-querier influences on
data generation that naturally arise in streaming systems.
Second, when per-querier budgets and shared limits coexist,
prior work has generally modeled them separately, overlook-
ing how their joint enforcement shapes system behavior.
When these omitted behaviors are modeled, per-querier
guarantees become unsound: even without collusion, a sin-
gle querier’s view can reveal more about the dataset than
the per-querier budget permits. This does not render per-
querier budgets useless – they remain valuable engineering
constraints – but it does mean their formal guarantees rest
on stronger assumptions than previously recognized. More
broadly, these results reinforce a key takeaway: rigorous
privacy analysis relies as much onfaithful system modeling
as on the mathematics of the DP proof itself.

3.1 Multi-Querier System Model
We define a generic model for a multi-querier DP system, not
specific to Attribution. Alg. 1 shows a system with𝐾 queriers
(𝑄 1,...,𝑄 𝐾), each with its own privacy budgetF𝑘, interact-
ing with a shared database𝐷 over discrete time steps𝑡. The
model accommodates both streams and static databases: a
data generation processG may append new data to 𝐷 at
each step, while in the static caseG outputs nothing after
the initial step. It supports both per-querier enforcement,
viaF𝑘, and an abstract shared limitL, which can represent
a global budget. At each step, querier𝑘 selects a query𝑄𝑘 𝑡
based only on itsownpast results, thereby explicitlyexclud-
ing intentional collusion. The query executes only if bothF𝑘
andL approve, in which case the querier receives result𝑉𝑘 𝑡 ;
otherwise it receives a data-independent result⊥.
To analyze DP, we introduce achallenge bit𝜒 that governs
whether a particular record 𝑥0 is added to the database at
time𝑡0. Neither the queriers nor G see 𝜒, but as queriers
issue queries, their views may reveal information about it,
modeling the leakage of an individual’s presence through DP
query results. Privacy loss quantifies how hard it is for an ad-
versary to distinguish between𝜒= 0and 𝜒= 1, whether the
adversary controls a single querier (per-querier guarantees)
or all queriers (global guarantees).
Formally, Alg. 1 satisfies𝜖-DP for querier𝑘∈[𝐾] if for
∀𝑥0∈X,∀𝑡 0∈[𝑡 max],∀G,∀(Q 1,...,Q 𝑛+1),∀𝑆⊆R 𝑡max:

ln  Pr[𝑉𝑘,(𝜒=0) ∈𝑆] Pr[𝑉𝑘,(𝜒=1) ∈𝑆] 

 ≤𝜖.
By contrast, a global guarantee would bound Pr[𝑉(𝜒=0)∈𝑆] Pr[𝑉(𝜒=1)∈𝑆] , if
for exampleLwere implemented as a global budget.
We next analyze per-querier guarantees and show two
orthogonal cases in which they degrade linearly with the
number of queriers. These correspond to conditions(A)and
(B)in Alg. 1: adaptive data generation in streaming settings,
and the presence of a shared limit in addition to per-querier
budgets. By toggling these conditions on and off, we isolate
the effect of each on per-querier guarantees. Appendix A.3
extends these results to IDP budgets, as used in Attribution.
3.2 Failure Mode 1: Adaptive Data Generation
We first consider the case where data is generated over time
with no shared limits (L always outputsTRUE). Adaptivity
in data generation – where new data depends on past DP
query results – has been studied in both streaming [11, 18,
21] and interactive [16, 26, 28, 43] systems. Modeling such
adaptivity is essential because it both directly affects DP
analyses, as prior work shows, and is inevitable in streaming
systems. For instance, a movie recommender may use prior
DP measurements to suggest a film, and the user’s decision
to watch it then becomes new data for future measurement.
Line 9 of Alg. 1 captures data adaptivity for multi-querier
systems:𝐷𝑡←G(𝑉 1 <𝑡,...,𝑉 𝐾 <𝑡), meaning data can depend
not only on one querier’s past results but also on others’.
This cross-querier dependency arises even without collu-
Alg. 1Formal model of a generic multi-querier, pure-DP system
1:Input
2: Challenge bit𝜒∈{0,1}
3: In-or-out record𝑥 0 to be inserted at time𝑡 0
4: Data generation processG
5: QueriersQ 1,...,Q 𝐾
6: Per-querier budgets (modeled as pure-DP filters)F 1,...,F 𝐾
7: Shared limitL
8:for𝑡∈[𝑡 max]do
//Data generation model:
// (A) Cross-querier data adaptivity
9:𝐷 𝑡←G(𝑉 1 <𝑡,...𝑉 𝐾 <𝑡)//new data depends onallpast results
10:if𝑡=𝑡 0 and𝜒=1then//insert in-or-out record on challenge
11:𝐷 𝑡←𝐷𝑡+𝑥 0
//Query execution model:
12:for𝑘∈[𝐾]do
13:𝑞 𝑘 𝑡 ←Q 𝑘(𝑉𝑘 <𝑡)//𝑄 𝑘 selects query based onits ownpast results
// (B) Shared-limit enforcement
14:ifF 𝑘(𝑞𝑘 1,···,𝑞 𝑘 𝑡)∧L(𝑞 1 1,···,𝑞 𝐾 1,···𝑞 𝑘 𝑡)then
15:𝑉 𝑘 𝑡 ←𝑞𝑘 𝑡(𝐷≤𝑡)
16:else
17:𝑉 𝑘 𝑡 ←⊥
18:return𝑉 1,...,𝑉 𝐾
sion, through user behavior or mechanisms like auctions.
For example, news.ex may show an impression for either
shoes.ex or hats.ex, depending on bids shaped by prior DP
results from both sites.
We prove that under this model, per-querier budgets (for-
malized as privacy filters [38]) with capacity𝜖 do not suffice:
Theorem 3.1(Per-querier guarantees are unsound under adaptive data gen-
eration).Consider Alg. 1, with 𝐾=𝑛+ 1queriers, where eachF𝑘 is a pure-DP
filter with capacity𝜖> 0, and whereL always outputsTRUE(i.e.,no shared
limit). Denote by𝑉𝑛+1,(𝜒) the view ofQ𝑛+1 on challenge bit 𝜒. Then, there
exists𝜖′ > 0such that ∃𝑥0∈X,∃𝑡 0∈[𝑡 max],∃G,∃Q 1,...,Q 𝑛+1,∃𝑆⊆
R𝑡max :

ln  Pr[𝑉𝑛+1,(𝜒=0) ∈𝑆] Pr[𝑉𝑛+1,(𝜒=1) ∈𝑆] 

 ≥𝜖+𝑛𝜖 ′.
Thm. 3.1 shows that with per-querier budgets of capacity
𝜖, privacy loss can exceed𝜖, withexcess loss growing linearly
in the number of queriers. This arises not from collusion but
from worst-case analysis that DP must account for. The proof,
given in Appendix A.1, works by constructing an example
of data generation and querying processes that exhibits that
much excess loss. While the theorem addresses only pure-
DP guarantees (yielding a linear increase in excess loss), the
result likely extends to approximate DP (with excess loss
growing with the square root of the number of queriers).
Prior analyses overlooked this point. ARA’s implemen-
tation supports multiple adtechs [17], but its proof models
only a single querier [16], effectively defining data genera-
tion asG(𝑉𝑘 <𝑡) for a fixed 𝑘 rather than our more general
G(𝑉 1 <𝑡,...,𝑉 𝐾 <𝑡). Cookie Monster, by contrast, allowed mul-
tiple queriers but modeled a static dataset in its proof [43].
3.3 Failure Mode 2: Shared Limits
We next consider the case where a shared limit is added to
a system with per-querier enforcement (line 14 in Alg. 1).

Such limits have been proposed in both static [15, 44] and
streaming [24] DP systems as defense-in-depth against col-
lusion. We instantiateL as a pure-DP filter shared across
all queriers, which lets us quantify the excess privacy loss.
The same reasoning, however, applies to other shared-limit
mechanisms, such as caps on the total number of queries or
rate limiters or quotas spanning subsets of queriers.
We show that even without data adaptivity, per-querier
privacy loss can exceed𝜖 in the presence of a shared budget.
To isolate this effect from Thm. 3.1, we restrict attention to
static databases (G returns∅ after the first time step). In this
setting, the shared budget acts as a cross-querier leakage
channel, enabling excess loss that, as before, grows linearly
with the number of queriers covered by the shared limit:
Theorem 3.2(Per-querier guarantees are unsound under adaptive query
budgets with shared limits).Take 𝑛+ 1queriers, with per-querier filters with
capacity𝜖, and a shared filter with capacity𝜖𝑔 <(𝑛+ 1)𝜖 . There exists𝜖′ > 0
such that for all 𝑛≥ 4 ln 2 (1−𝑒−𝜖/2) 2 , there existsG that returns∅ after the first
time step, such that∃𝑥 0∈X,∃𝑡 0∈[𝑡 max],∃Q 1,...,Q 𝑛+1,∃𝑆⊆R 𝑡max :

ln  Pr[𝑉𝑛+1,(𝜒=0) ∈𝑆] Pr[𝑉𝑛+1,(𝜒=1) ∈𝑆] 

 ≥𝜖+𝑛𝜖 ′.
The proof constructs an attack that induces this excess loss.
While it may appear to rely on collusion, the same leakage
can arise inadvertently. At a high level, multiple queriers
spend part of their budgets on an initial measurement and
issue a follow-up query only when the result is high (e.g.,
measuring ad exposure and conditionally computing a his-
togram). The shared filter then encodes this signal: it is more
likely to be exhausted when the true value is high, since more
queriers issue follow-up queries. A new querier can thus in-
fer this information from whether its own query is accepted
or rejected, exceeding the privacy bound of its local budget.
For IDP, rejection is not directly observable, requiring a more
subtle argument (see §A.2 for DP and IDP proofs).
This effect has been missed in prior work on multi-
granularity enforcement, either because it was not formal-
ized at all [15] or because per-querier and global limits were
analyzed in isolation or under non-adaptive queriers [24, 44].
Conceptually, this is like treating the two conditions in
F𝑘(𝑞𝑘 1,···,𝑞 𝑘 𝑡)∧L(𝑞 1 1,...,𝑞 𝐾 1,...,𝑞 𝑘 𝑡) as if they acted in-
dependently, when in real systems they are necessarily
enforced jointly.
3.4 Siloing Assumption and Takeaways
It is natural to ask whether any conditions – realistic or not
– could make per-querier enforcement sound. Appendix A.4
presents one such condition (Thm. A.3), thesiloing assump-
tion: each querier operates on a completely disjoint data
stream, and shared limits are disabled or so loose that they
never block queries. Under these constraints, per-querier DP
is sound in our general model (Alg. 1).
These constraints are almost certainly unattainable in
practice. Worse, attempting to engineer them – for example
by weakening or removing shared limits – undermines the
goal of strong user privacy. We therefore strongly recom-
mendagainstdoing so.
Instead, the takeaways are three-fold.First, Attribu-
tion should explicitly acknowledge the semantic limitations
of per-querier enforcement. Second, per-querier budgets
should be complemented with global enforcement; our sec-
ond contribution – and the remainder of this paper – shows
how to do so robustly and efficiently. Attribution has since
adopted both: the specification now records the semantic
limitations of per-querier enforcement [ 35], and specifies
global enforcement managed by the algorithm of §4 [ 34].
Third, a broader lesson for the research community: rigorous
privacy analysis depends as much onfaithful system model-
ingas on DP mathematics. While this is well-understood in
formal methods, the DP literature often relies on oversim-
plified models to keep proofs simple. Our results highlight
why modeling fidelity must become a first-class concern in
DP systems research.
4 Contribution 2: Global IDP with Big Bird
Global enforcement escapes the failures of §3 because both
are failures of scope, not of DP accounting. Thm. 3.1 and
Thm. 3.2 exhibit leakage that a per-querier budget cannot see:
information routed through the data stream or through the
shared limit, and thus outside the budget meant to bound it. A
global budget has no analogous outside channel—it accounts
for the joint information released across all queriers, so cross-
querier channels are inside the quantity being bounded, not
a way around it. This section therefore claims a global guar-
antee only, and shows that sound global device-epoch IDP
is achievable under a system model we make as comprehen-
sive as we can (Thm. 4.2). Per-querier budgets remain in
the design as engineering constraints protecting utility, not
privacy; the caveats of §3 apply to them here as anywhere.
Global enforcement does, however, introduce a new sys-
tems challenge: in open, multi-querier settings with un-
trusted participants, a shared global budget becomes vul-
nerable todepletion attacks—a denial-of-service (DoS) on
utility rather than privacy. In Attribution,anyweb domain
can invoke the API, allowing an attacker controlling many
Sybil domains to act as distinct queriers, exhaust users’ bud-
gets, and block benign measurement. Although Attribution
introduces global safety limits for privacy, it leaves their
management unspecified and identifies DoS depletion as a
key roadblock to deployment [19].
We presentBig Bird, a global budget manager for Attribu-
tion that makes device-epoch IDP both sound and deployable.
Its key idea is to align budget consumption with the struc-
ture of legitimate workloads: impressions create potential
privacy loss, conversions realize it, and meaningful consump-
tion should scale with genuine user actions across distinct
sites. Big Bird enforces this via IDP-aligned quotas on im-
pression and conversion sites and a per-user-action cap on

page
visit
x.ex
page
visit
y.ex
null
report
auto-redirects
(same user)
saveImpres
sion()
Attribution API
globalsybil1. ex x.ex
measureConversion()
sybil2.
ex
sybil3.
ex
y.ex
(a)Sybils as conversion sites
page
visit
x.ex
page
visit
y.ex
null
report
(same user)
Attribution API
globalsybil1. ex x.ex sybil2. ex sybil3. ex y.ex
sybil1.ex
sybil2.ex
sybil3.ex
embedded in
page (b)Sybils as intermediaries
Fig. 2. Example attacks.Sybils deplete the global budget from a single user
action by acting as (a) conversion sites or (b) intermediaries. Per-querier and
global budgets are shown as batteries (filled = available, empty = drained).
domain participation, while preserving device-epoch IDP.
4.1 Threat Model
Global budgets are ashared resource, and on the web, attacker
identities are weak (Attribution uses eTLD+1 domain names)
and browser API use is generally open. An attacker can
exploit this by registering manySybil domain namesand
coordinating them to deplete a device’s global budget. If this
occurs on many devices, benign queriers are locked out of
measurement, yielding a DoS based on the privacy layer.
Example attacks.Fig. 2 shows two example DoS deple-
tion attacks effective against current Attribution. In Fig. 2a,
a malicious sitex.exuses aggressive redirection: when a
user visitsx.ex, it registers impressions under many Sybil
domains posing as conversion sites, then auto-redirects the
user through them. Each Sybil calls measureConversion(),
consuming global budget. Since Attribution does per-querier
checks, it can spend up to𝜖querier; with𝜖global/𝜖querier Sybils,
x.excan exhaust a user’s global budget from a single visit.
When the user later visits a legitimate merchant (e.g.,y.ex),
that merchant receives null reports – both useless and bi-
ased. Ifx.exattracts many users even once, it can disable
Attribution for benign queriers across the epoch.
Attacks need not be so overt. An attacker can instead
embed many Sybil intermediaries (Fig. 2b), each requesting
reports and drawing from distinct per-querier budgets. More
subtly, it can pace Sybil activity over time or across repeated
visits to gradually drain users’ budgets, making the attack
harder to detect.
Generic attack model.The preceding examples illustrate
specific tactics that an attacker can use to deplete global
budgets in Attribution. Our objective, however, is to build
defenses at the budget-management layer that withstand a
broader class of attackers, regardless of how tactics evolve.
We thus model a generic attacker that controls a set of do-
mains visited by genuine users and aims to degrade the
accuracy of benign queriers’ measurements on genuine user
data by exhausting the global budget on users’ devices. We
characterize theattacker’s strengthalong three dimensions:
(i) how many domains it controls; (ii) how many intentional
user actions it can induce across those domains; and (iii) how
many distinct genuine users perform these actions.
Resilience goal.The attacker’s impact in the Fig. 2 examples
isdisproportionate to its strength: the attacker is weak along
one or more dimensions yet still depletes a device’s global
budget. Our goal is torestore proportionalityalong all three
dimensions of strength: depletion should scale not with Sybil
count alone, but with genuine user actions and with the
number of users it is able to attract, so that an attacker must
be strong along all three dimensions to deplete substantially.
We further require that this holds regardless of how the
attacker behaves or what it knows, without assuming that
benign traffic looks any particular way.
Assumptions.We exclude two classes of threats from our
model. First, we do not address bot-drivenpoisoningattacks
in which adversaries fabricate impressions or conversions
(including null reports) to skew aggregates. These attacks
degrade data quality rather than deplete global budgets on
genuine devices, and defending against them requires mech-
anisms orthogonal to global-budget management, such as
recently proposed fraud prevention for Attribution [6]. Our
focus is on preserving measurement availability for genuine-
user data – a prerequisite for meaningful measurement even
without the poisoning threat.
Second, we protect only benign sites that do not directly
or transitively partner with malicious ones (e.g., by em-
bedding attacker-controlled intermediaries or serving their
ads). Big Bird operates purely at the global-budget layer and
has no visibility into partner relationships or ad-network
governance; attacks that exploit such partnerships require
ecosystem-level controls (registration, contracts), not bud-
get logic. Our aim is to confine adversarial impact to sites
that interact with Sybils, while unrelated benign sites retain
utility.
4.2 Candidate Approaches
The research challenge is to add DoS depletion resilience
without overconstraining benign workloads, violating
device-epoch IDP, or undermining its optimizations. Naïve
approaches fail on at least one of these fronts.
Rate-limit API calls.One could cap how many impressions
a site may log or how many reports it may request per time
unit. However, API calls are a poor proxy for privacy loss.
Under IDP, consumption depends on a user’s actual data con-
tribution, and many events incur zero loss: most impressions
never lead to conversions, and many conversions have no
attributable impression. These would still count against an
API-call limit, disabling IDP’s sparsity benefits. Worse, sites
cannot know in advance which events will incur loss, so such
caps force conservative throttling of legitimate activity and
degrade utility. Any fixed limit therefore either suppresses
benign workloads or must be set so loosely that attackers
operate beneath it.

Rate-limit total budget consumption.A more aligned
approach is to cap budget consumption itself, e.g., by limit-
ing how much global budget can be spent over short time
windows. This blocks bursty attacks like those in Fig. 2, but
fails against paced strategies that spread consumption over
time. For example, a site can exploit repeated or prolonged
user presence (e.g., an open tab) to gradually drain budget
via redirects or intermediary requests. Extending the time
window to catch such attacks risks making the limiter it-
self a DoS target. Moreover, setting the cap below 𝜖querier
harms benign workloads, especially small advertisers that
may legitimately consume their budget in bursts.
Cap total budget consumption per user action.A key
weakness in Fig. 2 is that a single user action can drain
a user’s entire global budget. A natural fix is to cap bud-
get per user action: each action initializes a budget 𝜖action,
shared across all queriers triggered by that action. This ties
consumption to a meaningful unit, but still allows a single
high-engagement site to deplete budget over many interac-
tions with the same user. Among candidate approaches, this
is closest to Big Bird.
Interactions of caps with device-epoch IDP.We find it
easy to define caps that violate device-epoch IDP by coupling
decisions across epochs. For example, §C presents a natural
but IDP-violating variant of the preceding approach: capping
total budget consumption across all epochs following a user
action. Any defense must therefore ensure that both checks
and consequences are confined to a single epoch; in this
paper, we show how to do so.
4.3 Big Bird Design
Based on the limitations of alternative approaches, we estab-
lish four principles for Big Bird’s design.P1:Limits should
trackIDP budget consumption, not proxies such as API-call
counts, since IDP budget consumption is not always corre-
lated to the number of API calls.P2:Defenses should target
minimal, intrinsic properties of legitimate Attribution use, not
specific attack tactics (e.g., redirection chains, embedded
intermediaries, fast-fire vs. slow-burn attacks) or specula-
tive assumptions about benign workloads (e.g., that benign
traffic will never involve redirections or more than𝑥 inter-
mediaries). This keeps defenses robust as both attacks and
benign workloads evolve.P3:Global-budget use should be
ultimately tied to intentional user actions across distinct first-
party sites, since that is what Attribution is meant to measure.
P4:Attribution’s device-epoch IDP must be preserved.
Key insight: stock-and-flow.Fig. 3 illustrates this pattern.
The Attribution API is intended to measureuser interactions
across distinct first-party sites, such as impression and con-
version sites. In normal Attribution use (Fig. 3a), privacy
loss should only be consumed when there is something to
measure: a user visits one site (and sees an ad) and later visits
a distinct site (and converts there). That creates a stock-and-
flow pattern for privacy budget consumption: (1)stockis
page visit
shoes.ex
Attribution API
news.ex
saveImpression() measureConversion()
creates stock triggers flow
page visit
(same user)
global
budget
(a)Privacy loss in normal use
page visit
Attribution API
x.ex
automated
stocks &
flows
global
budget
 (b)Privacy loss in attack
Fig. 3. Stock-and-flow pattern of budget consumption in Attribution.
(a) Normal use: user actions on impression sites create stock and user
actions on conversion sites trigger flows. (b) Attacks break this pattern by
automatically creating many stocks and flows from very few user actions.
created when the user visits an impression site and the site
saves an impression; and (2)flowis triggered when a user vis-
its a conversion site and the site requests a report. Non-zero
privacy loss is realized only whenboth steps occur, a property
afforded by the IDP mechanism. By contrast, attacks disrupt
this structure (Fig. 3b) by coalescing domains or automat-
ing stock creation and flow triggering (e.g.,via automatic
redirections or embedded intermediaries), allowing substan-
tial global budget consumption from minimal user actions.
Big Bird restores this pattern with privacy-loss-based quotas
that capstock creationandflow triggeringfor every caller
alike, ultimately tying both tointentional user actions.
Big Bird architecture.Fig. 4 shows the Big Bird architecture.
It sits as a management layer around Attribution’s global
budgets and protects them from depletion by enforcing quo-
tas that restore the expected stock-and-flow pattern, in each
epoch: (1)impression-site quotaslimit how much stock any
one domain can contribute; (2)conversion-site quotaslimit
how much flow a domain can trigger; and (3) aper-action
domain caplimits how many new domains can create quotas
in the context of a single user action.
The first two quotas are privacy budgets implemented as
IDP filters, just like global and per-querier budgets. How-
ever, their purpose is not privacy; they protect the global
budget from depletion. These quotas account for individ-
ual privacy loss in a manner aligned with the global budget
(principleP1), and constrain stock creation and flow trigger-
ing according to the expected structure of benign behavior
(P2). The per-action domain cap is not a privacy budget;
it simply restricts the number of quota budgets activated
under different domains from a single user action. Together,
these three quotas constrain consumption of the global bud-
get, forcing the attacker to behave within the bounds of
expected workload, and tie this restricted consumption to
something tangible, such as intentional user actions across
sites (P3). §4.4 formalizes the resilience properties afforded
by this quota architecture, while our evaluation quantifies

adtech2.ex
shoes.exnews.ex
saveImpre-
ssion()
blog.ex
(all actions are from
the same user)
encrypted
reportssaveImpre- ssion()
① ② ③
⑤
Report Generation Process
(4.1) (~as in Attribution) Retrieve matching impressions
per epoch, excluding ones from the current user action.
(4.2) Big Bird per-epoch resilience checks and privacy
loss accounting (Alg. 2):
(4.3) (as in Attribution) Generate histogram attributing
the conversion’s value to impressions across all epochs.
books.ex
shoes.ex
news.ex shoes.ex
blog.ex
impression-site
quota budgets
conversion-site
quota budgets
global
budget
books.ex
social.ex
adtech.ex
adtech2.ex
④
Big Bird
per-querier  budgets
(as in Attribution)
(i) (j) (i) (j)
adtech.ex
measureConversion()
books.ex
per-action domain cap
Fig. 4. Big Bird architecture. Depicts budget structure for a single epoch,
though in reality privacy and quota budgets exist for each epoch.
them empirically. Finally, our quota enforcement is done
separately for each epoch, ensuring that Big Bird preserves
device-epoch IDP, a property we discuss in §4.5 (P4).
Example execution.Fig. 4 shows the workflow. 1 – 2 A
user sees ads on news.ex and blog.ex. 3 After purchasing
on shoes.ex, two measureConversion() calls are issued: (i)
one for shoes.ex (to measure a creative) and (j) one for
adtech.ex (to optimize its placement model). 4 Big Bird
processes each call by selecting relevant impressions and
attempting to deduct budgets atomically per epoch: querier,
global, conversion-site, and matching impression-site quotas.
If any deduction fails, that epoch’s contribution is dropped.
5 Two encrypted reports are returned, one per querier.
Reports (i) and (j) use parameters: epsilon=0.2 (pri-
vacy budget requested), value=75 (conversion value), and
maxValue=150 (maximum conversion value). Assume the
relevant impressions occur in epochs𝑒1and 𝑒2, while the
conversion occurs in 𝑒3. Tab. 1 shows the remaining bud-
get and quota capacities after releasing reports (i) and (j),
assuming all budgets start at the listed capacities. For report
(i), following the IDP rule used in Attribution, each rele-
vant epoch incurs privacy loss(value/maxValue)·𝜖= 0.1,
while other epochs incur none. Only sites with matching
impressions ( news.ex in 𝑒1and blog.ex in 𝑒2) consume
epoch
querier
𝜖querier =0.5 global 𝜖global =4 imp-quota 𝜖imp-quota =2 conv-quota 𝜖conv-quota =0.75 shoes.ex adtech.ex adtech2.ex news.ex blog.ex shoes.ex
e1 0.4 0.4 0.4 3.8 1.8 2 0.55
e2 0.4 0.4 0.4 3.8 2 1.8 0.55
e3 0.5 0.5 0.5 4 2 2 0.75
Tab. 1. Quota and budget states after example execution.
impression-site quota. Since all budgets for𝑒1and 𝑒2have
sufficient capacity, deductions commit atomically in each
epoch, and the histogram is generated from these epochs.
Report (j) performs the same computation but deducts from
adtech.ex’s querier budget instead ofshoes.ex’s.
Big Bird algorithm.Alg. 2 enforces quotas while preserving
device-epoch IDP. Each user action creates a context uaCtx,
shared across all API calls causally triggered by that action.
Browsers already have notions of intentional user action,
namely the user-activation API [5], often used to gate access
to various APIs. Within each uaCtx, Big Bird bounds the
number of distinct first-party domains, not API calls. This
prevents attackers from spawning many Sybil domains while
allowing arbitrary activity within each domain. This matches
normal web behavior: a benign user action may involve
one or two redirects (e.g., email links or short URLs), but is
not expected to traverse many domains. As a result, small
per-action domain cap values (e.g., 2–3) should comfortably
support benign workloads while preventing attackers from
spawning many distinct quotas to fuel depletion.
Privacy accounting occurs in measureConversion(). For
each epoch in the attribution window, the function (i)
matches impressions, (ii) computes device-epoch IDP loss
for the conversion and the finer-grained device-epoch–
impression-site losses used by impression-site quotas, and
(iii) attempts to deduct all relevant budgets in a singleatomic
transaction. The finer-grained accounting prevents wasting
quota on impression sites that displayed no relevant impres-
sions. If any deduction fails, that epoch’s data contribution
is dropped with no budget impact; otherwise, all deductions
commit atomically. This prevents budget waste, preserves
the stock-and-flow structure, and ensures that decisions
based on one epoch’s data never affect another’s privacy
accounting.
A subtle but critical constraint shapes Alg.2’s structure.
A natural alternative would be to enforce the per-action do-
main cap by computing, inside measureConversion(), how
many impression-site quotas supply stock and how many
conversion-site quotas trigger flow for the report, and to
nullify the entire report if this exceeds a threshold. Big Bird
deliberately avoids this. A single report may aggregate im-
pressions and conversions from multiple epochs, and any
check that reasons about those epochs jointly would couple
their outcomes and thus their privacy losses. Because device-
epoch IDP requires each epoch’s privacy loss to depend only
on that epoch’s data, such cross-epoch checks are unsound.
Instead, Big Bird enforces the per-action domain cap us-
ingstrict per-epoch separation. The count of activated quotas

Alg. 2Big Bird algorithm
defonUserAction(uaCtx)
accessedSites[uaCtx][e]←∅for each epoch e
defsaveImpression(uaCtx, impSite, impression)
e = getCurrentEpoch()
if|accessedSites[uaCtx][e]∪{impSite}|>𝜅 action then
return//can’t allow new quotas from this user action
accessedSites[uaCtx][e]∪={impSite}
ImpressionStore[e].add(uaCtx, impression) //save uaCtx
return
defmeasureConversion(uaCtx, impSites, querier, convSite, params)
//Separately for each epoch, match impressions and do budget
//checks and privacy accounting (Steps (4.1)-(4.3) in Fig. 4).
for𝑒∈params.attributionWindowdo
//Check the per-action domain cap.
if|accessedSites[uaCtx][e]∪convSite|>𝜅 action then
𝐼𝑒←∅//drop epoch’s impression data from consideration
CONTINUE
accessedSites[uaCtx][e]∪={convSite}
//Match impressions, filtering out impressions that querier and convSite
//are not permitted to measure, including impressions from this uaCtx.
𝐼𝑒←MatchingFn(uaCtx, ImpressionStore[e], params)
//Compute IDP loss at two granularities w/ Cookie Monster algo.
𝜖𝑒←computeEpochLoss(𝐼𝑒, params)
for𝑖∈impSitesdo
𝜖𝑖 𝑒←computeEpochImpSiteLoss(𝐼𝑒[𝑖], params)
//Execute budget checks & deductions as a transaction.
tx = beginTransaction()
ifquerierBudget[e][querier].tryConsume(𝜖𝑒, tx)and
globalBudget[e].tryConsume(𝜖𝑒, tx)and
convQuota[e][convSite].tryConsume(𝜖𝑒, tx)and
(impQuota[e][𝑖].tryConsume(𝜖𝑖 𝑒, tx)∀𝑖∈impSites)then
tx.commit() //all budgets deducted successfully
else//a budget deduction failed
tx.abort() //undo any other budget deductions
𝐼𝑒←∅//drop epoch’s impression data from consideration
//Generate attribution histogram from remaining impressions
returnAttributionFn(𝐼 𝑒1,...,𝐼 𝑒𝑤)//𝑒 𝑖∈params.attributionWindow
is maintained not only per uaCtx but alsoper epoch. If the
cap is exceeded in epoch𝑒, Big Bird nullifies only epoch𝑒’s
data contribution, forcing its privacy loss to zero while leav-
ing all other epochs unaffected. No check aggregates privacy
consumption across epochs, and no failure in one epoch prop-
agates to another. This preserves device-epoch IDP while
still enforcing meaningful DoS limits tied to user actions.
Finally, we note a subtlety of the atomic check-and-deduct
procedure, specifically for impression-site quota deductions
within an epoch. As shown in §5, atomicity strengthens re-
silience by forcing attackers to be selective about which
Sybil impressions they declare as relevant: a single impres-
sion whose impression-site quota is exhausted suffices to
nullify the entire epoch’s contribution, preventing any global-
budget consumption. This same mechanism can, however,
harm benign workloads: if multiple impression sites are rel-
evant in an epoch and one exhausts its quota, the querier
cannot obtain attribution information from the remaining
sites even if they retain budget. Supporting finer-grained
“Normal” workload parameters:
M:max # of impression sites contributing nonzero loss in an epoch.
N:max # of conversion sites requesting nonzero loss from an epoch.
n:max # of conversion sites requesting nonzero loss from (epoch, impSite).
r:max budget consumed by an intermediary’s cross-advertiser queries on a single
conversion site, as a fraction of the intermediary’s𝜖 querier.
Cap Capacity configuration
Per-querier filter 𝜖querier: configuration parameter
Global filter 𝜖global =max(𝑁,𝑛·𝑀)(1+𝑟)𝜖 querier
Impression-site quota 𝜖imp-quota =𝑛(1+𝑟)𝜖 querier
Conversion-site quota 𝜖conv-quota =(1+𝑟)𝜖 querier
per-action domain cap 𝜅action =2or3
Tab. 2. Big Bird budget configurations.
behavior – e.g., selectively nullifying only the depleted im-
pression site’s contribution while preserving device-epoch
IDP – appears feasible, but we leave its design to future work.
Our strongest-attacker experimental results in §5 provide
an upper bound on resilience if impression-site quotas are
removed from the atomic transaction.
Quota configuration.We choose quota capacities via a
utility-first approach: specify workload requirements, then
select the smallest values that satisfy them. Taking the
querier budget𝜖querier and intermediary fraction 𝑟 as base
parameters, and using browser-tunable parameters that
reflect expected benign workload scale, we define four con-
straints: (i) a conversion site must be able to spend its full
querier budget, and intermediaries may spend a fraction
𝑟 of that, giving 𝜖conv-quota ≥ (1+𝑟)𝜖 querier; (ii) no single
conversion site should drain the global budget, so with 𝑁
expected conversion sites per epoch, 𝜖global≥𝑁𝜖 conv-quota;
(iii) likewise, the global budget should exceed an impres-
sion site’s stock, so with 𝑀 expected impression sites,
𝜖global≥𝑀𝜖 imp-quota; and (iv) because multiple conversion
sites may query the same impression site, a fan-out parame-
ter𝑛requires𝜖 imp-quota≥𝑛𝜖 conv-quota.
We then minimize𝜖global subject to these constraints, yield-
ing the capacities in Tab. 2 and a tight global-privacy guar-
antee consistent with utility. Configuring Big Bird is thus a
three-step procedure: (1) choose the base parameters𝜖querier
and𝑟; (2) conservatively estimate the workload parameters
𝑀,𝑁,𝑛 from a production sample at a chosen percentile; and
(3) derive all quota capacities in closed form from Tab. 2. The
percentile is the only real knob, trading utility against the
tightness of𝜖global. §5.2 instantiates this procedure on Criteo.
4.4 Resilience Guarantee
Big Bird restores proportionality between attacker impact
and strength along the three dimensions in §4.1. Its re-
silience, stated in Thm. 4.1, stems from: (a) per-domain
quota limits, (b) user-action-based quota creation, and (c)
bounded-sensitivity DP aggregation. Indeed, Attribution
serves population-levelDP queriesin which each device-
epoch contributes only through a report withbounded
sensitivity. As a result, even if an attacker depletes budget on
some device-epochs, the resulting error in a benign query

scales only with the number of affected device-epochs.
Theorem 4.1(Resilience to DoS depletion – proof in B.4).Consider an
attacker who (1) creates 𝑀 adv and𝑁 adv imp-quota and conv-quota
quotas, respectively; (2) collects 𝑈 adv user actions across the quotas’ domains
for device𝑑; and (3) depletes budget from𝑘device-epochs.
Denote by 𝜖 adv global the maximum budget that the attacker can consume
from theglobal budgeton any epoch from 𝑑. Denote by∥𝑄(𝐷)− ˜𝑄(𝐷)∥
the error induced by the attacker, for a query𝑄 where reports have sensitivity
Δand at most𝑚reports belong to any single device. Then, we have:
(i)𝜖 adv global≤min(𝑀 adv𝜖imp-quota, 𝑁adv𝜖conv-quota)
(ii)𝜖 adv global≤(1+𝑟)𝜖 querier·𝜅 action·𝑈 adv
(iii)∥𝑄(𝐷)− ˜𝑄(𝐷)∥≤𝑚·𝑘·Δ, and𝑘≤𝑈 adv/⌈ 𝜖global 𝑛(1+𝑟)𝜖 querier·𝜅action⌉.
(i) Even if user actions were free, the global budget that
an attacker can drain on a given device-epoch is capped
by how many impression-site and conversion-site quotas
it has managed to create, scaled by their capacities. This is
the stock-and-flow constraint: to move global budget, the
attacker must both create stock (impression-site quotas) and
trigger flow (conversion-site quotas), and each is individually
bounded. (ii) We connect this to intentional user actions
via the per-action domain cap. Each user action can create
at most𝜅action new quotas of each type, and only within a
single epoch. Across𝑈 adv actions, the attacker can therefore
unlock at most𝑂(𝜅 action·𝑈 adv) useful quotas, which yields
the stated bound on 𝜖adv global. This enforces proportionality
to user actions: substantial depletion now requires many
genuine user interactions, not just many cheap domains.
(iii) We lift the guarantee from a single device-epoch to the
query level. With bounded report sensitivity Δ, even if the
attacker fully depletes the global budget on𝑘 device-epochs,
its impact on any aggregate is linear in𝑘.𝑘 itself is bounded
by the number of actions across devices.
Limitations.We identify two limitations of the resilience
guarantees provided by Big Bird. First, resilience assumes
the attacker cannot scale simultaneously along all three
strength dimensions. Enforcing this ultimately requires API-
governance mechanisms beyond budget management. For in-
stance, browsers could require API invokers to register with
trusted authorities to limit Sybil domains, or adopt a conser-
vative definition ofuser activationto ensure that interactions
the user did not intend as attribution actions (e.g., clickjack-
ing, deceptive UI, automatic redirects, or invisible frames)
do not trigger budget consumption. Our contribution is to
expose the necessary control pointswithin the privacy-budget
layer so that, when combined with governance mechanisms,
Attribution can be rigorously hardened against attacks.
Second, Thm. 4.1 bounds depletion of theglobalbudget,
but quota budgets themselves may still be targeted – al-
beit only in ways excluded by our threat model (§4.1). For
example, a malicious intermediary could exhaust its own
conversion-site quota to block other intermediaries, or target
the impression-site quota of a site that embeds its ads. These
attacks are localized: the impact is confined to queriers inter-
acting (directly or transitively) with the affected site, while
unrelated sites retain access to the global budget. Moreover,
our quota configuration dampens such effects: exhausting
an impression-site quota requires fan-out across𝑛 conver-
sion sites, while exhausting a conversion-site quota requires
(1+𝑟) queriers. Fully addressing quota-targeting attacks will
require Attribution to support mechanisms for managing
and subdividing quotas (e.g., per-partner allocation) to pre-
vent abuse. We leave this to future work, as it likely requires
integration with ecosystem-level constructs such as business
relationships and auction pricing.
4.5 Privacy Guarantee
Our privacy analysis of Big Bird aims for a high-fidelity
model that provides confidence that the design satisfies
global device-epoch-level IDP. We capture: individual DP;
on-device report generation with centralized noise addition;
all public information exposed by the protocol; query, bud-
get, and data adaptivity; multiple epochs and queriers; the
atomic interaction of multiple budgets within a single trans-
action; and user-action-based limits on how many quotas
may be invoked. To our knowledge, this is one of the most
faithful system models in the DP literature. Appendix B gives
two versions: a simplified one for educational use (§B.5) and
the complete version for formal analysis (§B.2). Using the
complete model, we prove that Big Bird preservesglobal
device-epoch IDP: Here and below, Pr[𝑉=𝑣] denotes the
joint density or probability mass at𝑣, as appropriate.
Theorem 4.2(Global IDP Guarantee – proof in §B.3).Consider 𝑥∈X
withglobal budgetcapacity 𝜖global. Then, Big Bird satisfies individual device-
epoch𝜖global-DP for𝑥 under public informationC. That is, for every data
generation processG and all queriersA1,...,A 𝑘 , the output𝑉(𝜒) of Alg. 7
under challenge bit𝜒satisfies, for all𝑣∈R 𝑒max×(𝑡 max+1)×𝐵 :

ln  Pr[𝑉(0) =𝑣] Pr[𝑉(1) =𝑣] 

≤𝜖 global.
4.6 Prototype as Reference Implementation
We implement Big Bird both as a reference implementation
for the emerging W3C standard and as a foundation for
broader deployments, including in mobile OS location ana-
lytics. The implementation has two components. (1)pdslib
is a general-purpose IDP Rust library that subsumes Cookie
Monster and Big Bird while exposing a generic interface
beyond Attribution. Clients (websites or mobile apps) reg-
ister events (e.g., ad views, location visits), request reports
(e.g., attributions, model updates), and receive encrypted,
privacy-budgeted responses. (2) An integration in Firefox’s
Attribution prototype [32] replaces report counting with full
IDP and resilient enforcement based on pdslib. Mobile rec-
ommendation workloads, which share sparsity and structure
with advertising, are a promising future instantiation.
5 Evaluation
We evaluate Big Bird’s utility and resilience on a real-world
Criteo dataset, simulating DoS attackers inspired by Fig. 2a.

Our evaluation asks two questions: (1) How do quota con-
figurations affect benign-query utility, both without attack
and under a fixed-strength attack? (2) How does attacker
strength along different resource dimensions translate into
damage to benign queries?
5.1 Methodology
Dataset.CriteoPrivateAd [ 40] is a 30-day snapshot of pro-
duction traffic (104M impressions across 220k publisher sites
and 10k conversion sites) released for benchmarking W3C’s
Attribution API. To our knowledge, it is the only real-world
dataset with multiple conversion sites—a requirement for
exercising Big Bird’s conversion-site quotas. The dataset in-
cludes timing, contextual features, conversions, and a daily-
reset device ID. Because impressions are subsampled, most
devices appear only once. Using Criteo’s resampling method,
we reconstruct the device-level distribution, yielding1.4M
devices,4.6M impressions, and5.6M conversions. The median
device has 2 impressions and 4 conversions. While realistic,
the dataset reflects a single intermediary and likely underes-
timates load in multi-intermediary deployments.
Benign workload.We evaluate single-advertiser measure-
ment, where each batch of conversions produces a DP his-
togram over five contextual buckets. We evaluate utility us-
ing RMSRE𝜏 [2], the root mean squared relative error across
buckets, clipping counts below 𝜏= 5%of batch size. This
captures both DP noise (common across baselines) and bias
from budget/quota depletion. To ensure low-noise baselines,
we (i) restrict to advertisers with≥ 100conversions/day (526
total), (ii) batch∼10 days of conversions (capped at 8,000),
and (iii) set 𝜖 to target RMSRE𝜏 ≈ 5%, similar to how we
expect an advertiser would tune their measurement.
Attack workload.We inject synthetic adversarial traffic
atop real events. The attacker is given impression and conver-
sion streams for the 10 busiest sites, reusing timestamps and
device IDs to simulate organic traffic. Each event is treated
as a user action enabling budget depletion. The attacker con-
trols a pool of Sybil domains (25 by default) and, per user
action, triggers a redirection chain (bounded by𝜅action). Each
Sybil registers one fresh impression and requests a report
on a previously unqueried impression with𝜖=𝜖 querier.
A naive attacker that references all Sybils per action is
neutralized by Big Bird’s atomic deductions: a single over-
quota Sybil invalidates the entire request, consuming zero
global budget. We confirm this empirically and focus on
two stronger strategies. TheRandom Attackersamples a
subset of Sybils per conversion (35% by default, minimizing
atomic rejection), modeling limited tracking capabilities. The
Omniscient Attackerhas perfect knowledge of each de-
vice’s remaining quotas and uses only Sybils with remaining
quota, eliminating rejection waste and representing the opti-
mal attack within the Attribution interface. Because these
capabilities—perfect repeat-user recognition and full visibil-
ity into every device’s quota state—are ones real attackers
will likely lack, we read omniscient-attacker error as a de-
liberate worst-case ceiling rather than a typical operating
point; real attackers fall between the two extremes.
Baselines and defaults.We compare Big Bird to two base-
lines spanning the utility–privacy spectrum: (1)Attribution
w/o global budget(Cookie Monster [ 43]), which enforces per-
querier IDP but no shared limit. It is immune to depletion
and serves as theutility ceiling, but lacks global privacy guar-
antees. (2)Attribution w/ global budget, which adds a shared
privacy filter but no quota mechanisms, representing the
strongest defense without Big Bird.
Unless stated otherwise, we set𝜖querier = 1.0,𝜖global = 8.0,
𝜖imp-quota = 2.0, and 𝜖conv-quota = 1.0. We use 𝜅action = 2
and 25 Sybils at maximum popularity. Epochs are one day,
matching Criteo’s daily device-ID reset.
5.2 Quota Configuration on Criteo
Tab. 3. Workload params in Criteo.
%ile ˜𝑁 ˜𝑀 ˜𝑛 𝜖global 𝜖imp-quota
p50 2 1 2 2 2
p80 4 2 2 4 2
p85 4 2 4 8 4
p90 4 3 4 12 4
p95 6 3 4 12 4
p99 8 4 8 32 8
We instantiate the three-
step configuration pro-
cedure of §4.3 (“Quota
configuration” header)
on Criteo.Step (1):we
use 𝜖querier = 1(our
default from §5.1) and,
because our evaluation
models only single-advertiser queries, 𝑟= 0, giving
𝜖conv-quota =𝜖 querier; general workloads would set𝑟> 0.Step
(2):the distributions of 𝑁,𝑀,𝑛 across devices could be com-
puted exactly by running full conversion attribution, but a de-
ployer can instead use cheap, conservative per-device statis-
tics that upper-bound them: unique impression sites (˜𝑀≥𝑀 ),
unique conversion sites ( ˜𝑁≥𝑁 ), and unique conversion sites
per (device, impression-site) pair ( ˜𝑛≥𝑛 ); Tab. 3 reports these
statistics at several percentiles.Step (3):the same table shows
the resulting capacities; e.g., the p85 estimates( ˜𝑁, ˜𝑀, ˜𝑛)=
(4, 2, 4) yield𝜖global =max( ˜𝑁, ˜𝑛 ˜𝑀)( 1+𝑟)𝜖 querier = 8and
𝜖imp-quota = ˜𝑛( 1+𝑟)𝜖 querier = 4. Only these values are
Criteo-specific: the procedure itself is dataset-driven, and
any browser vendor can run it on its own production sample.
The percentile choice governs the tradeoff between quota
size (and thus utility) and the tightness of the global DP guar-
antee𝜖global. Supporting 100% of devices maximizes utility,
since it expects no quota-induced errors, but yields very loose
𝜖global. The 85th percentile offers a balanced configuration:
tight enough for a single-digit 𝜖global = 8while avoiding
quota errors for the vast majority of devices. As in §5.3,
setting𝜖imp-quota below the table value (e.g., 𝜖imp-quota = 2
instead of 4) substantially improves resilience at a negligi-
ble utility cost: the resulting slack in𝜖global ensures enough
budget is left for benign queries even under attack.
5.3 Utility and Resilience with Quota Configuration
We fix all default parameters and sweep the impression-site
quota𝜖imp-quota and per-action domain cap 𝜅action to deter-

(a)Benign error without attack
 (b)Error causes without attack
(c)Benign error under attack
 (d)Error causes under attack
Fig. 5. Utility and resilience with quota configuration.(a), (b): Benign
error and root causeswithout attack. (c), (d): Benign error and root causes
under the random attacker.
mine the range of quota values that preserve benign utility
while confining the attacker.
Benign error without attack (Fig. 5a, Fig. 5b).We first
measure utility in a purely benign setting, varying the
impression-site quota at 𝜖global = 8(derived from the p85
workload in Tab. 3 with𝜖querier = 1). Fig. 5a plots median and
95th-percentile RMSRE𝜏 as𝜖imp-quota grows. Both Attribution
baselines, which lack impression-site quotas, show constant
and identical error across 𝜖imp-quota (median 5.2%). Their
agreement confirms that the global budget alone does not
reduce utility without an attack, an important sanity check
that isolates quota effects from global-budget effects. In
contrast, Big Bird performs poorly at𝜖imp-quota = 0.5, where
aggressive quota exhaustion produces null reports (median
error 14.0%, a 2.7× increase). Once𝜖imp-quota reaches 2, quotas
no longer affect accuracy: Big Bird matches the baselines
at 5.2%. This holds through arbitrarily large quota values,
including Big Bird with the impression-site quota disabled
entirely. The p85 quotas from Tab. 3 therefore suffice for
normal operation and appear conservative, suggesting that
true workload parameters for most devices are well below
the upper-bound estimates we use to size𝑁,𝑀, and𝑛.
Fig. 5b breaks down the bias component of Big Bird’s
RMSRE𝜏 by attributing each blocked report to the first budget
in priority order that was exhausted. At𝜖imp-quota = 0.5, the
impression-site quota blocks 16.2% of reports, explaining the
elevated error in Fig. 5a. At𝜖imp-quota = 1, this drops to 0.8%.
For𝜖imp-quota≥ 2, the impression-site quota blocks fewer
than 0.002% of reports; the only residual blocking comes from
per-querier budgets (2.8% of reports). This residual appears
in all baselines, and is inherent to IDP systems when device
contributions exhaust the querier’s budget. The takeaway
is that, once quotas are sized to the p85 workload, Big Bird
introduces no bias beyond what the underlying Attribution
accounting already imposes.
Benign error under attack (Fig. 5c, Fig. 5d).We next eval-
uate resilience when an attacker targets the global budget.
Fig. 5c reports error for benign queries.
Attribution w/o global budget is unaffected (median 5.2%),
as expected: without a global budget, there is nothing to
deplete. But this immunity comes at the cost of no global
privacy guarantee (§3). Attribution w/ global budget suffers
severe degradation: its median RMSRE𝜏 reaches 48.5%, a9.3×
increase, and its p95 reaches 87.6%. This confirms Big Bird’s
premise: simply adding a global budget to fix per-querier
unsoundness is trivially defeated by Sybil attacks.
In contrast, Big Bird achieves near-baseline utilityandthe
privacy guarantee of a system with a global budget. With a
well-sized quota, it nearly matches Attribution w/o global
budget at a median of 5.5% and a p95 of 14.8%. Moreover,
Big Bird is robust across a meaningful range of impression-
site quota values 𝜖imp-quota ∈ [1, 2], for which the budget
the attacker can consume remains well below𝜖global, leaving
substantial slack in the global budget even after the attack.
We also observe that, as in the benign case, quotas that are
too small degrade utility. But under attack, quotas that aretoo
largealso degrade utility, for a fundamentally different rea-
son: they allow the attacker to route enough traffic through
Sybils to drain the global budget despite the quota mecha-
nism. At𝜖imp-quota = 3, median error rises to 12.5% and by
𝜖imp-quota = 5it plateaus near 20.1%. Fig. 5d corroborates this
transition: for𝜖imp-quota up to 2, fewer than 1% of benign re-
ports are blocked by global-budget depletion; at𝜖imp-quota = 3
this rises to approximately 11%, and at𝜖imp-quota = 4to ap-
proximately 19%, dominating all other error sources.
Impact of per-action domain cap and attacker strategy.
We now fix𝜖imp-quota = 2(our default) and sweep𝜅action from
1 to 4 to evaluate how the per-action domain cap impacts util-
ity under attack. Additionally, we compare the omniscient
attacker to the random attacker, revealing how adversary
sophistication affects resilience. Fig. 6a shows that across
both attackers, 𝜅action = 1keeps median benign RMSRE 𝜏
at or below 10.0%, and𝜅action = 2(our default) at or below
28.6%. Both remain far below the unprotected Attribution
API (48.3–48.4%).𝜅action = 1minimizes worst-case error at
the expense of flexibility in the benign case, allowing only
one site per user action. Big Bird’s quota mechanism provides
the structural foundation for resilience, bounding depletion
even against the optimal attacker. Atomic deduction dramat-
ically reduces damage against more realistic adversaries: the
random attacker achieves only 5.4% at𝜅action = 2, versus the
omniscient attacker’s 28.6%.
5.4 Impact of Attacker Strength
The preceding section fixed attacker strength and varied
the defense configuration. We now fix the defense (𝜅action =

(a)Impact of per-action domain cap(b)Impact of Sybil domains(c)Impact of site popularity
Fig. 6. (a) Impact of per-action domain cap and (b), (c) attacker strength on resilience.(b) Number of attacker-controlled Sybil domains capable of
accessing the API and (c) popularity of the attacker-controlled sites in terms of number of user actions across all distinct users in the Criteo dataset.
2, 𝜖imp-quota = 2) and vary attacker resources to test the
guarantee from §4.1: damage should scale with the number
of Sybil domains (dimension (i)) and the volume of genuine
user traffic the attacker attracts (dimensions (ii) and (iii)).
Number of Sybil domains (Fig. 6b).We vary the attacker’s
Sybil pool from 5 to 100 domains, holding site popularity
at maximum. The random attacker rises only from 5.2% at
5 Sybils to 6.4% at 100, as the tight 𝜖imp-quota = 2quota
sharply limits per-domain budget consumption regardless of
pool size. The omniscient attacker saturates early: RMSRE𝜏
reaches 29.4% at 10 Sybils and remains flat through 100. With
perfect tracking, 10 domains already exhaust the available
per-device quota headroom; additional Sybils provide no
benefit once the global budget becomes the bottleneck. This
matches Thm. 4.1(i): depletion is bounded by the product of
domain count and quota capacity, so once𝑀adv·𝜖 imp-quota
exceeds the global budget, extra Sybils add nothing.
Site popularity (Fig. 6c).We vary which of Criteo’s busiest
sites the attacker controls, from the top 10 sites to ranks
41–50. Lower-ranked sites have fewer user actions and fewer
distinct users, jointly exercising dimensions (ii) and (iii) of
the threat model. The random attacker falls from 5.4% to 5.2%,
remaining near baseline across all ranks — the tight source
quota renders the random attacker essentially harmless re-
gardless of popularity. The omniscient attacker falls from
29.0% to 10.9%, a2.7× reduction. This confirms that damage
scales with the volume of genuine user traffic the attacker
attracts, as Thm. 4.1(ii–iii) bounds depletion as a function of
𝑈 adv and the number of affected devices. This dimension is
critical: attracting genuine traffic requires costly real-world
investment, unlike cheap domain registration.
6 Additional Related Work
§3 covers DP enforcement granularities. Other work follows.
Ad-measurement APIs.Our primary application is the
W3C Attribution API. Cookie Monster [ 43] introduced
device-epoch IDP accounting. Google’s ARA line [2, 10, 16],
IPA [30], PAM [ 3], and Hybrid [ 31] explored alternative,
albeit now obsolete, privacy architectures. In these pro-
posals, per-querier enforcement is treated as a natural
semantic, with collusion recognized as the primary limita-
tion. We show that evenwithoutcollusion, per-querier DP
is unsound. Attribution’s measurement-only scope, with
targeting unsupported, is being debated [ 20]; the debate
concerns what the standard should protect, not whether its
guarantees hold. We argue that measurement is a sensible
place to start, separable from targeting and already treated
distinctly by some U.S. privacy laws [8].
Privacy budget management.This paper contributes to
the broad challenge ofprivacy budget management, a crucial
but understudied area in DP. Budget allocationwithina query
is well studied [1, 27], but managing budgetsacrossqueriers,
especially untrusted ones, remains relatively unexplored. Pu-
jol et al . [36, 37] balance utility across analysts sharing a
global budget, but without per-analyst utility assurances.
Relevant systems include those for global budget schedul-
ing [23, 28, 42], but none of these works address a Sybil DoS
threat. Finally, work on privacy filters [12, 14, 25, 29, 38] pro-
vides building blocks on which Big Bird implements budgets.
DoS and quota mechanisms.DoS defense is studied ex-
tensively in systems and networking (e.g., [4, 9, 39, 41]), and
quotas are ubiquitous for conventional resources. But these
approaches do not apply directly to privacy budgets, whose
consumption reflectsdata contribution, not request volume.
To our knowledge, no work treats privacy budgets as aDoS
targetand provides Sybil-resilient budget management that
preserves DP semantics and utility. Big Bird’s novelty does
not rest on the notion of quota, but on how the quotaarchi-
tectureis shaped by DP semantics and workload structure.
7 Conclusions
We study DP enforcement in the W3C Attribution draft stan-
dard for privacy-preserving advertising and find that its cur-
rent reliance on per-querier device-epoch IDP is not a sound
foundation: even without collusion, realistic multi-querier
behaviors such as cross-querier adaptivity and shared lim-
its can violate its guarantees. We therefore advocate global
device-epoch IDP and present Big Bird, a budget manager
that makes it deployable by tying privacy-budget consump-
tion to the stock-and-flow structure of benign workloads
via IDP-aligned quotas and per-action domain caps. Our re-
sults show that Big Bird achieves rigorous global privacy,
resilience to depletion attacks, and strong utility under ad-
versarial conditions. Both contributions are now part of the
draft standard and have broader implications for DP systems
in open, untrusted environments.

Acknowledgments
We thank the anonymous reviewers and the PATCG/PATWG
participants for their constructive feedback. Nikos Goutzou-
lias contributed to the implementation of an early prototype.
This work was supported by NSF grant CNS-2143868, NSF
Cooperative Agreement No. EEC-2133516, and Google, Meta,
Microsoft, and Sloan Faculty Fellowships. Co-author Lécuyer
acknowledges the Canada CIFAR AI Chair program and Amii.
Co-author Geambasu was partially employed by Meta dur-
ing this project, and subsequently by Google; the work was
done exclusively in the context of Geambasu’s Columbia
University research.
References
[1] John M. Abowd, Robert Ashmead, Ryan Cumings-Menon, Simson
Garfinkel, Micah Heineck, Christine Heiss, Robert Johns, Daniel Kifer,
Philip Leclerc, Ashwin Machanavajjhala, Brett Moran, William Sexton,
Matthew Spence, and Pavel Zhuravlev. 2022. The 2020 Census Disclo-
sure Avoidance System TopDown Algorithm.Harvard Data Science
ReviewSpecial Issue 2 (6 2022). doi:10.1162/99608f92.529e3cb9
[2] Hidayet Aksu, Badih Ghazi, Pritish Kamath, Ravi Kumar, Pasin Ma-
nurangsi, Adam Sealfon, and Avinash V. Varadarajan. 2024. Sum-
mary Reports Optimization in the Privacy Sandbox Attribution Re-
porting API.Proc. Priv. Enhancing Technol.2024, 4 (2024), 605–621.
doi:10.56553/POPETS-2024-0132
[3] Apple. 2023. Private Ad Measurement (PAM).https://github.com/
patcg-individual-drafts/private-ad-measurement.
[4] Nirav Atre, Hugo Sadok, Erica Chiang, Weina Wang, and Justine
Sherry. 2022. SurgeProtector: Mitigating Temporal Algorithmic
Complexity Attacks using Adversarial Scheduling. InProceedings
of the 2022 Conference of the ACM Special Interest Group on Data
Communication (SIGCOMM). ACM, New York, NY, USA, 723–738.
doi:10.1145/3544216.3544250
[5] Marcos Caceres. 2023. The User Activation API.https://webkit.org/
blog/13862/the-user-activation-api/.
[6] Rutchathon Chairattana-Apirom, Stefano Tessaro, and Nirvan Tyagi.
2025. Fraud Mitigation in Privacy-Preserving Attribution. Cryptology
ePrint Archive, Paper 2025/1891.https://eprint.iacr.org/2025/1891
[7] T.-H. Hubert Chan, Elaine Shi, and Dawn Song. 2011. Private and
Continual Release of Statistics.ACM Transactions on Information and
System Security14, 3 (2011), 26:1–26:24. doi:10.1145/2043621.2043626
[8] Colorado General Assembly. 2025. Colorado Privacy Act, Section 6-
1-1303 (25)(b)(IV).https://law.justia.com/codes/colorado/title-6/fair-
trade-and-restraint-of-trade/article-1/part-13/section-6-1-1303/.
[9] Scott A. Crosby and Dan S. Wallach. 2003. Denial of Ser-
vice via Algorithmic Complexity Attacks. In12th USENIX Security
Symposium (USENIX Security 03). USENIX Association, Washing-
ton, D.C.https://www.usenix.org/conference/12th-usenix-security-
symposium/denial-service-algorithmic-complexity-attacks
[10] Matthew Dawson, Badih Ghazi, Pritish Kamath, Kapil Kumar, Ravi
Kumar, Bo Luan, Pasin Manurangsi, Nishanth Mundru, Harikesh
Nair, Adam Sealfon, and Shengyu Zhu. 2023. Optimizing Hierarchi-
cal Queries for the Attribution Reporting API. InProceedings of the
Workshop on Data Mining for Online Advertising (AdKDD 2023) Co-
Located with the 29th ACM SIGKDD Conference on Knowledge Discovery
and Data Mining (KDD 2023), Long Beach, CA, USA, August 7, 2023
(2023)(CEUR Workshop Proceedings, Vol. 3556), Abraham Bagherjeiran,
Nemanja Djuric, Kuang-chih Lee, Linsey Pang, Vladan Radosavlje-
vic, and Suju Rajan (Eds.). CEUR-WS.org.https://ceur-ws.org/Vol-
3556/adkdd23-dawson-optimizing-ceur-paper.pdf
[11] Sergey Denisov, H. Brendan McMahan, John Rush, Adam Smith,
and Abhradeep Guha Thakurta. 2022. Improved Differential Pri-
vacy for SGD via Optimal Private Linear Operators on Adaptive
Streams.Advances in Neural Information Processing Systems35 (2022),
5910–5924.https://papers.nips.cc/paper_files/paper/2022/hash/
271ec4d1a9ff5e6b81a6e21d38b1ba96-Abstract-Conference.html
[12] David Durfee and Ryan M Rogers. 2019. Practical Differentially Private
Top-k Selection with Pay-what-you-get Composition. InAdvances
in Neural Information Processing Systems, H. Wallach, H. Larochelle,
A. Beygelzimer, F. d'Alché-Buc, E. Fox, and R. Garnett (Eds.), Vol. 32.
Curran Associates, Inc., 3527–3537.
[13] Hamid Ebadi, David Sands, and Gerardo Schneider. 2015. Differential
Privacy: Now It’s Getting Personal. InProceedings of the 42nd Annual
ACM SIGPLAN-SIGACT Symposium on Principles of Programming Lan-
guages(Mumbai India, 2015-01-14). ACM, 69–81. doi:10.1145/2676726.
2677005
[14] Vitaly Feldman and Tijana Zrnic. 2021. Individual Privacy Accounting
via a Rényi Filter. InAdvances in Neural Information Processing Sys-
tems(2021), M. Ranzato, A. Beygelzimer, Y. Dauphin, P.S. Liang, and
J. Wortman Vaughan (Eds.), Vol. 34. Curran Associates, Inc., 28080–
28091.https://proceedings.neurips.cc/paper_files/paper/2021/file/
ec7f346604f518906d35ef0492709f78-Paper.pdf
[15] Marco Gaboardi, James Honaker, Gary King, Jack Murtagh, Kobbi
Nissim, Jonathan Ullman, and Salil Vadhan. 2018. PSI ({\Psi}): A Private
Data Sharing Interface. (2018). arXiv:1609.04340 [cs, stat]http://arxiv.
org/abs/1609.04340
[16] Badih Ghazi, Charlie Harrison, Arpana Hosabettu, Pritish Kamath,
Alexander Knop, Ravi Kumar, Ethan Leeman, Pasin Manurangsi, Mar-
iana Raykova, Vikas Sahu, and Phillipp Schoppmann. 2025. On the
Differential Privacy and Interactivity of Privacy Sandbox Reports.Pro-
ceedings on Privacy Enhancing Technologies2025, 3 (2025), 382–397.
doi:10.56553/popets-2025-0104
[17] Google. 2022.Attribution Reporting: Full System Overview. Privacy
Sandbox.https://privacysandbox.google.com/private-advertising/
attribution-reporting/system-overview
[18] Abhradeep Guha Thakurta and Adam Smith. 2013. (Nearly) Optimal
Algorithms for Private Online Learning in Full-information and Bandit
Settings. InAdvances in Neural Information Processing Systems(2013),
Vol. 26. Curran Associates, Inc.https://proceedings.neurips.cc/paper/
2013/hash/c850371fda6892fbfd1c5a5b457e5777-Abstract.html
[19] Charlie Harrison. 2025. Safety limits enable possible DOS attacks.
https://github.com/w3c/attribution/issues/69.
[20] Kyle Hogan, Alishah Chator, Gabriel Kaptchuk, Mayank Varia, and
Srinivas Devadas. 2026. Making Sense of Private Advertising: A Princi-
pled Approach to a Complex Ecosystem.Proc. Priv. Enhancing Technol.
2026, 1 (2026), 450–469. doi:10.56553/POPETS-2026-0023
[21] Palak Jain, Sofya Raskhodnikova, Satchit Sivakumar, and Adam Smith.
2023. The Price of Differential Privacy under Continual Observation.
InProceedings of the 40th International Conference on Machine Learning
(2023-07-03). PMLR, 14654–14678.https://proceedings.mlr.press/v202/
jain23b.html
[22] Zach Jorgensen, Ting Yu, and Graham Cormode. 2015. Conserva-
tive or Liberal? Personalized Differential Privacy. In2015 IEEE 31st
International Conference on Data Engineering(2015-04). 1023–1034.
doi:10.1109/ICDE.2015.7113353
[23] Nicolas Küchler, Emanuel Opel, Hidde Lycklama, Alexander Viand,
and Anwar Hithnawi. 2024. Cohere: Managing Differential Privacy in
Large Scale Systems. In2024 IEEE Symposium on Security and Privacy
(SP). IEEE, 991–1008. doi:10.1109/SP54263.2024.00122
[24] Nicolas Küchler, Alexander Viand, Hidde Lycklama, and Anwar Hith-
nawi. 2025. DPolicy: Managing Privacy Risks Across Multiple Releases
with Differential Privacy. In2025 IEEE Symposium on Security and
Privacy (SP)(2025-05). 3950–3968. doi:10.1109/SP61157.2025.00256
[25] Mathias Lécuyer. 2021. Practical Privacy Filters and Odometers with
Rényi Differential Privacy and Applications to Differentially Private

Deep Learning. arXiv:2103.01379 [stat.ML]https://arxiv.org/abs/2103.
01379
[26] Mathias Lécuyer, Riley Spahn, Kiran Vodrahalli, Roxana Geambasu,
and Daniel Hsu. 2019. Privacy Accounting and Quality Control in the
Sage Differentially Private Machine Learning Platform. InProceedings
of the 27th ACM Symposium on Operating Systems Principles (SOSP).
ACM, 181–195. doi:10.1145/3341301.3359639
[27] Chao Li, Michael Hay, Vibhor Rastogi, Gerome Miklau, and Andrew
McGregor. 2010. Optimizing linear counting queries under differential
privacy. InProceedings of the Twenty-Ninth ACM SIGMOD-SIGACT-
SIGART Symposium on Principles of Database Systems(Indianapolis,
Indiana, USA)(PODS ’10). Association for Computing Machinery, New
York, NY, USA, 123–134. doi:10.1145/1807085.1807104
[28] Tao Luo, Mingen Pan, Pierre Tholoniat, Asaf Cidon, Roxana Geambasu,
and Mathias Lécuyer. 2021. Privacy Budget Scheduling. In15th USENIX
Symposium on Operating Systems Design and Implementation (OSDI
21). USENIX Association, 55–74.https://www.usenix.org/conference/
osdi21/presentation/luo
[29] Ryan McKenna, Brett Mullins, Daniel Sheldon, and Gerome Miklau.
2022. AIM: an adaptive and iterative mechanism for differentially
private synthetic data.Proc. VLDB Endow.15, 11 (July 2022), 2599–
2612. doi:10.14778/3551793.3551817
[30] Meta and Mozilla. 2022. Interoperable Private Attribution (IPA).https:
//github.com/patcg-individual-drafts/ipa.
[31] Meta and Mozilla. 2024. Hybrid Proposal.https://github.com/patcg-
individual-drafts/hybrid-proposal.
[32] Mozilla. 2024. Experiment: Privacy-Preserving Attribution Measure-
ment API.https://github.com/mozilla/explainers/tree/main/archive/
ppa-experiment.
[33] Andrew Paseltiner, Andy Leiserson, Benjamin Case, Benjamin Savage,
Charlie Harrison, and Martin Thomson. 2026. Attribution Level 1.
https://w3c.github.io/attribution/.
[34] Andrew Paseltiner, Andy Leiserson, Benjamin Case, Benjamin Savage,
Charlie Harrison, and Martin Thomson. 2026. Attribution Level 1, 4.2.1.
Privacy Budget Store.https://www.w3.org/TR/2026/WD-attribution-
20260813/#s-privacy-budget-store.
[35] Andrew Paseltiner, Andy Leiserson, Benjamin Case, Benjamin Savage,
Charlie Harrison, and Martin Thomson. 2026. Attribution Level 1, 7.1.1.
Formal Analysis of Privacy Properties and Their Limitations.https:
//www.w3.org/TR/2026/WD-attribution-20260813/#formal-analysis.
[36] David Pujol, Albert Sun, Brandon Fain, and Ashwin Machanavajjhala.
2022. Multi-Analyst Differential Privacy for Online Query Answering.
Proc. VLDB Endow.16, 4 (2022), 816–828. doi:10.14778/3574245.3574265
[37] David Pujol, Yikai Wu, Brandon Fain, and Ashwin Machanavajjhala.
2021. Budget sharing for multi-analyst differential privacy.Proc. VLDB
Endow.14, 10 (June 2021), 1805–1817. doi:10.14778/3467861.3467870
[38] Ryan Rogers, Aaron Roth, Jonathan Ullman, and Salil Vadhan. 2016.
Privacy odometers and filters: pay-as-you-go composition. InPro-
ceedings of the 30th International Conference on Neural Information
Processing Systems(Barcelona, Spain)(NIPS’16). Curran Associates
Inc., Red Hook, NY, USA, 1921–1929.
[39] C.L. Schuba, I.V. Krsul, M.G. Kuhn, E.H. Spafford, A. Sundaram, and
D. Zamboni. 1997. Analysis of a denial of service attack on TCP.
InProceedings. 1997 IEEE Symposium on Security and Privacy (Cat.
No.97CB36097). 208–223. doi:10.1109/SECPRI.1997.601338
[40] Mehdi Sebbar, Corentin Odic, Mathieu Léchine, Aloïs Bissuel, Nicolas
Chrysanthos, Anthony D’Amato, Alexandre Gilotte, Fabian Höring,
Sarah Nogueira, and Maxime Vono. 2025. CriteoPrivateAds: A
Real-World Bidding Dataset to Design Private Advertising Systems.
arXiv:2502.12103 [cs.CR]https://arxiv.org/abs/2502.12103
[41] Oliver Spatscheck and Larry L. Peterson. 1999. Defending Against
Denial of Service Attacks in Scout. In3rd Symposium on Operating
Systems Design and Implementation (OSDI 99). USENIX Association,
New Orleans, LA, 59–72.https://www.usenix.org/conference/osdi-
99/defending-against-denial-service-attacks-scout
[42] Pierre Tholoniat, Kelly Kostopoulou, Mosharaf Chowdhury, Asaf
Cidon, Roxana Geambasu, Mathias Lécuyer, and Junfeng Yang. 2025.
DPack: Efficiency-Oriented Privacy Budget Scheduling. InProceedings
of the Twentieth European Conference on Computer Systems(Rotterdam,
Netherlands)(EuroSys ’25). Association for Computing Machinery,
New York, NY, USA, 1194–1209. doi:10.1145/3689031.3696096
[43] Pierre Tholoniat, Kelly Kostopoulou, Peter McNeely, Prabhpreet Singh
Sodhi, Anirudh Varanasi, Benjamin Case, Asaf Cidon, Roxana Geam-
basu, and Mathias Lécuyer. 2024. Cookie Monster: Efficient On-Device
Budgeting for Differentially-Private Ad-Measurement Systems. InPro-
ceedings of the ACM SIGOPS 30th Symposium on Operating Systems
Principles(New York, NY, USA, 2024-11-15)(SOSP ’24). Association for
Computing Machinery, 693–708. doi:10.1145/3694715.3695965
[44] Shufan Zhang and Xi He. 2023. DProvDB: Differentially Private Query
Processing with Multi-Analyst Provenance.Proc. ACM Manag. Data1,
4, Article 267 (Dec. 2023), 27 pages. doi:10.1145/3626761

Note: This appendix has not been peer-reviewed.
A Per-Querier DP Analysis (§3 Proofs)
A.1 Data Adaptivity
We provide more details on the model introduced in §3.2.
Our formalism with a data generation process follows ex-
isting work [ 26]. Other adaptive stream definitions have
been proposed [18, 21]. Adaptive data generation definitions
capture stronger adversaries than non-adaptive adjacency
definitions for streams [7]. Note that when there is only one
querier, a single adversary can be both the data generation
process and the querier.
Without loss of generality, the opt-out record and the time
at which it is inserted are known upfront. We could letG
adaptively decide when and what to insert, while enforcing
that this happens at most once, but this decision would not
actually depend on the challenge bit and would therefore
follow a distribution known byGupfront.
Thm. 3.1 shows that data adaptivity results in excess
per-querier privacy loss growing linearly in the number
of queriers. The proof exhibits queriers and a data gener-
ation process, where results from queriers Q1,...,Q 𝑛 are
first encoded into the dataset itself.Q𝑛+1 later decodes this
information to gain additional confidence about the value
of𝜒 beyond what its own queries should allow according to
the per-querier filter.
Theorem 3.1.Consider Alg. 1, whereF𝑘 are instantiated with
pure DP filters [ 38], each with capacity 𝜖. Denote by𝑉(𝜒) the
output of the algorithm on challenge bit𝜒.
When𝐾= 1, Alg. 1 reduces to single-querier fully adaptive
composition on adaptively generated streams. We have:
∀𝑥0∈X,∀𝑡∈[𝑡 max],∀G,∀Q 1,
∀𝑆⊆R 𝑡max,

ln  Pr[𝑉 1,(0) ∈𝑆] Pr[𝑉 1,(1) ∈𝑆] 

≤𝜖.
However, for𝐾=𝑛+1>1, there exists𝜖 ′ >0such that:
∃𝑥0∈X,∃𝑡 0∈[𝑡 max],∃G,∃(Q 1,...,Q 𝑛+1),
∃𝑆⊆R 𝑡max,

ln  Pr[𝑉𝑛+1,(0) ∈𝑆] Pr[𝑉𝑛+1,(1) ∈𝑆] 

 =𝜖+𝑛𝜖 ′ >𝜖.
Proof. When𝐾= 1, we are exactly in the setting of Lécuyer
et al. [26]. Briefly, when data can change adaptively based
on past results, inserting a single record can have cascading
effects on future data and future queries. Still, after condi-
tioning on a prefix𝑉 1 1,...,𝑉 𝑡 𝑡 , the databases in both worlds
differ only by at most one record.
Now, consider𝐾=𝑛+ 1with 𝑛> 0. Take𝑥0 = 1and
𝑡0 = 1. Without loss of generality, take𝑡max = 2andX={ 1}.
We use histogram notation for the database, but sinceX is a
singleton, we write𝐷∈N instead of𝐷∈N X. In multiset no-
tation, we could take˝ 𝑥∈𝐷 𝑥 to get an integer representation
of the database. DefineGandQ 1,...,Q 𝑛,Q𝑛+1 as follows:
1. At𝑡=1:
a. The data generation process does not return any
data:G(∅,...,∅)=∅ . Thus 𝐷1 = 1if 𝜒= 1, and
𝐷1 =0otherwise, that is:
𝐷1 =𝜒(1)
b. For𝑘∈{ 1..𝑛},Q𝑘 submits𝑞𝑘 1 :𝐷↦→𝐷+Lap( 1/𝜖),
which consumes𝜖from the per-querier filterF 𝑘.
c.Q 𝐾 submits a query that consumes no budget from
the per-querier filter:Q 𝐾(∅)=𝑞 𝐾 1 :𝐷↦→0.
2. At𝑡=2:
a. The data generation process inserts up to 𝑛 new
records, conditionally on outputs 𝑉 1 1,...,𝑉 𝑛 1 from
Q1,...,Q 𝑛:G(𝑉 1 1,...,𝑉 𝐾 1)=|{𝑘∈{ 1..𝑛} : 𝑉𝑘 1 >
1/2}|. That is:
𝐷2 =
𝑛∑︁
𝑘=1
1[𝐷 1+𝑍𝑘 >1/2](2)
where𝑍𝑘∼Lap( 1/𝜖). Since𝑉𝑘 1 is more likely to be
greater than1/2if 𝜒= 1,𝐷2 is more likely to be high
if𝜒= 1. In other words,G encodes whatQ1,...,Q 𝑛
have learned into the dataset itself.
b. For𝑘∈{ 1..𝑛},Q𝑘 submits a query that consumes
no budget from the per-querier filter:Q𝑘(𝑉𝑘 1)=𝑞 𝑘 2 :
𝐷↦→0.
c.Q 𝐾 submits a query that consumes 𝜖 from the
per-querier filter F𝐾:Q𝐾(𝑉𝐾 1)=𝑞 𝐾 2 : 𝐷↦→
𝐷+Lap(1/𝜖), and therefore:
𝑉𝐾 2 =𝐷 1+𝐷 2+𝑍(3)
where𝑍∼Lap( 1/𝜖). We will show that𝑉𝐾 2 is dispro-
portionally more likely to be high if 𝜒= 1. In other
words,Q𝐾 retrieves the information encoded into
the dataset, that originally came fromQ 1,...,Q 𝑛.
Recall that Pr[𝑍𝑘 > 1/2]= 1 2𝑒−𝜖/2. Also, Pr[1+𝑍 𝑘 >
1/2]=Pr[−𝑍 𝑘 < 1/2]= 1− 1 2𝑒−𝜖/2, since−𝑍𝑘∼𝑍 𝑘. Set𝑝 :=
1
2𝑒−𝜖/2.𝐷2 follows a binomial distribution: 𝐷(0) 2 ∼B(𝑛,𝑝)
and𝐷 (1) 2 ∼B(𝑛,1−𝑝)∼𝑛−B(𝑛,𝑝). Hence, Eq. 3 gives: (
𝑉𝐾,(0) 2 ∼B(𝑛,𝑝)+Lap(1/𝜖)
𝑉𝐾,(1) 2 ∼1+𝑛−B(𝑛,𝑝)+Lap(1/𝜖) (4)
We already have E[𝑉𝐾,(0) 2 ]=𝑛𝑝<𝑛/ 2and E[𝑉𝐾,(1) 2 ]=
1+𝑛( 1−𝑝)> 1+𝑛/ 2. We now exhibit an event for which
𝑉𝐾,(0) 2 ≪𝑉 𝐾,(1) 2 .
Take𝐵∼ B(𝑛,𝑝) . Take 𝑁≥𝑛+ 1. Recall that since
𝑍∼Lap(𝜖) , for all𝑧≥ 0and 𝑡∈R such that𝑧+𝑡≥ 0, we
have:
Pr[𝑍≥𝑧]=𝑒 𝜖𝑡 Pr[𝑍≥𝑧+𝑡](5)
On one hand, we have Pr[𝑉 0≥𝑁]=Pr[𝐵+𝑍≥𝑁]=

Pr[𝑍≥𝑁−𝐵] . On the other hand, Pr[𝑉 1≥𝑁]=Pr[ 1+𝑛−
𝐵+𝑍≥𝑁]=Pr[𝑍≥𝑁− 1−𝑛+𝐵] . Since𝑁− 1−𝑛+𝐵≥ 0,
we have: Pr[𝑍≥𝑁− 1−𝑛+𝐵]=𝑒 𝜖 Pr[𝑍≥𝑁−𝑛+𝐵] .
Hence,
Pr[𝑉 1≥𝑁]
Pr[𝑉 0≥𝑁] =𝑒𝜖 Pr[𝑍≥𝑁−𝑛+𝐵] Pr[𝑍≥𝑁−𝐵] (6)
For all𝑘∈[ 0,𝑛] we have𝑁−𝑛+𝑘≥ 0and 𝑁−𝑘≥ 0,
so we can compute the exact probabilities:
Pr[𝑍≥𝑁−𝑛+𝐵]=
𝑛∑︁
𝑘=0
𝑛
𝑘

𝑝𝑘(1−𝑝) 𝑛−𝑘 Pr[𝑍≥𝑁−𝑛+𝑘]
=
𝑛∑︁
𝑘=0
𝑛
𝑘

𝑝𝑘(1−𝑝) 𝑛−𝑘 1 2𝑒−(𝑁−𝑛+𝑘)𝜖
= 1 2𝑒−𝑁𝜖 𝑛∑︁ 𝑘=0 𝑛 𝑘  𝑝𝑘(1−𝑝) 𝑛−𝑘(𝑒𝜖)𝑛−𝑘
=(𝑝+(1−𝑝)𝑒 𝜖)𝑛
Similarly,
Pr[𝑍≥𝑁−𝐵]=
𝑛∑︁
𝑘=0
𝑛
𝑘

𝑝𝑘(1−𝑝) 𝑛−𝑘 Pr[𝑍≥𝑁−𝑘]
= 1 2𝑒−𝑁𝜖 𝑛∑︁ 𝑘=0 𝑛 𝑘  𝑝𝑘(1−𝑝) 𝑛−𝑘(𝑒𝜖)𝑘
=(𝑝𝑒 𝜖+1−𝑝) 𝑛
Hence,
Pr[𝑉 1≥𝑁]
Pr[𝑉 0≥𝑁] =𝑒𝜖
𝑝+(1−𝑝)𝑒 𝜖
𝑝𝑒𝜖+1−𝑝
𝑛
Moreover, we have:
𝑝+(1−𝑝)𝑒 𝜖−(𝑝𝑒 𝜖+1−𝑝)=(1−2𝑝)𝑒 𝜖−(1−2𝑝)
=(1−2𝑝)(𝑒 𝜖−1)
>0
since𝑝< 1/2and 𝜖> 0. Define𝜖′ :=ln  𝑝+(1−𝑝)𝑒 𝜖 𝑝𝑒𝜖+1−𝑝  > 0.
Then:
ln
 Pr[𝑉 1≥𝑁]
Pr[𝑉 0≥𝑁]

=𝜖+𝑛𝜖 ′
□
A.2 Shared Limits
Since we know that data adaptivity already threatens per-
querier budget semantics, we consider a simpler setting
where data is known upfront. Alg. 3 presents this variant
of Alg. 1. Thm. 3.2 then shows that adding a shared filter
results in excess per-querier privacy loss, also growing lin-
early in the number of queriers. The proof exhibits𝑛 queriers
Q1,...,Q 𝑛 that first ask queries. These queriers then adap-
tively encode what they have learned into the privacy param-
eters of their next queries. The shared privacy filter tracks
privacy loss across queriers, so the state of that filter now
depends on all queriers’ past queries. Finally, a querierQ𝑛+1
can decode the information stored into the shared filter by ob-
serving whether its own queries get rejected by the shared fil-
ter. This givesQ𝑛+1 additional information about the dataset,
beyond what its own per-querier filter allows. This happens
without different queriers sharing their DP outputs, which is
what people have referred to as collusion before. In fact, even
ifQ1,...,Q 𝑛 do not follow a particular strategy, andQ𝑛+1
doesn’t know about them,Q𝑛+1’s view can still be impacted
beyond what its per-querier filter allows.
Alg. 3Formal model for shared limits
1:Input
2:Database𝐷
3:QueriersQ 1,...,Q 𝐾
4:Per-querier filtersF 1,...,F 𝐾
5:Shared limitL
6:Output
7:View𝑉=(𝑉 1,...,𝑉 𝐾)∈R 𝑡max×𝐾 of allQ 𝑘
8:for𝑡∈[𝑡 max]do
9:for𝑘∈[𝐾]do
//Query based onQ 𝑘 ’sownprevious results
10:𝑞 𝑘 𝑡←Q 𝑘(𝑉𝑘 <𝑡)
//Execute if (1) Q𝑘 has enough budget and (2) shared
limit accepts the query.
11:ifF 𝑘(𝑞𝑘 1,...,𝑞 𝑘 𝑡)∧L(𝑞 1 1,...,𝑞 𝐾 1,...𝑞 𝑘 𝑡)then
12:𝑉 𝑘 𝑡 ←𝑞𝑘 𝑡(𝐷)
13:else
14:𝑉 𝑘 𝑡 ←⊥
Theorem 3.2.Take 𝐾=𝑛+ 1 > 1, per-querier filters with ca-
pacity𝜖 and shared filter with capacity𝜖𝑔 <(𝑛+ 1)𝜖 (allowing
executions that trigger the shared limit).
For𝑛 large enough that⌈𝑛 2𝑒−𝜖/2⌉<𝑛/ 2, there exists neigh-
boring databases𝐷,𝐷 ′ such that:
∃(Q 1,...,Q 𝑛+1),∃𝑆⊆R 𝑡max,

ln  Pr[𝑉𝑛+1,(0) ∈𝑆] Pr[𝑉𝑛+1,(1) ∈𝑆] 

 >𝜖.
Moreover, there exists 𝜖′ > 0and neighboring databases
𝐷,𝐷′ such that for all𝑛≥ 4 ln 2 (1−𝑒−𝜖/2) 2 ,
∃(Q 1,...,Q 𝑛+1),∃𝑆⊆R 𝑡max,

ln  Pr[𝑉𝑛+1,(0) ∈𝑆] Pr[𝑉𝑛+1,(1) ∈𝑆] 

≥𝜖+𝑛𝜖 ′.
Proof. Consider𝐷= 0,𝐷′ = 1fromNX =N withX={ 1}.
DefineQ1,...,Q 𝑛 as follows. Take𝜖0,𝜖 1,𝜖 2 > 0that we will
calibrate later.
1. At𝑡=1:
a. For𝑘∈{ 1..𝑛},Q𝑘 submits𝑞𝑘 1 :𝐷↦→𝐷+Lap( 1/𝜖1),
which consumes𝜖 1.
b. Then,Q𝑛+1 submits a query that consumes all but
𝜖0 from its budget: Q𝑛+1(∅)=𝑞 𝑛+1 1 : 𝐷↦→𝐷+
Lap(1/(𝜖−𝜖 0)).
2. At𝑡=2:

a. For𝑘∈{ 1..𝑛},Q𝑘 submits a query that consumes
no budget if 𝑉𝑘 1 was small, or 𝜖2 if𝑉𝑘 1 was large:
Q𝑘(𝑉𝑘 1)=𝑞 𝑘 2 :𝐷↦→1[𝑉 𝑘 1 > 1/2](𝐷+Lap( 1/𝜖2)).
In other words, Q𝑘 encodes the information it
learned at𝑡= 1into the shared limit itself, through
the adaptively chosen budget associated with its
request at time𝑡=2.
b.Q 𝑛+1 submits a query that attempts to consume
𝜖0:Q𝑛+1(𝑉𝑛+1 1 )=𝑞 𝑛+1 2 : 𝐷↦→𝐷+Lap( 1/𝜖0), and
therefore𝑉𝑛+1 2 ∼𝐷+Lap( 1/𝜖0) if the shared limit
and the per-querier filter both accept the query, and
𝑉𝑛+1 2 =⊥ otherwise. In other words,Q𝑛+1 retrieves
the information encoded into the shared limit that
originally came fromQ 1,...,Q 𝑛’s own requests.
Now, we configure𝜖1 and𝜖2 to ensure that no query prior
to𝑉𝑛+1 2 gets filtered. That is,𝜖−𝜖 0+𝑛(𝜖 1+𝜖 2)≤𝜖 𝑔 =𝑛 0𝜖
and𝜖1+𝜖 2≤𝜖 . To saturate the global filter when the first𝑛
queriers all ask for𝜖 2, we want:
𝜖−𝜖 0+𝑛(𝜖 1+𝜖 2)=𝜖 𝑔 (7)
This means that the state 𝑓𝑛,(𝜒) 2 of the shared filter just
before query𝑡=2,𝑘=𝑛+1, on input𝐷 (𝜒) , is:
𝑓𝑛 2 =𝑛𝜖 1+𝜖−𝜖 0+
𝑛∑︁
𝑘=1
Pr[𝑉𝑘 1 >1/2]𝜖 0 (8)
Set𝑝= 1 2𝑒−𝜖/2. We have: (
𝑓𝑛,(0) 2 ∼𝑛𝜖 1+𝜖−𝜖 0+B(𝑛,𝑝)𝜖 2
𝑓𝑛,(1) 2 ∼𝑛𝜖 1+𝜖−𝜖 0+(𝑛−B(𝑛,𝑝))𝜖 2 (9)
In particular,E[𝑓 𝑛,(0) 2 ]=𝜖−𝜖 0+𝑛(𝜖 1+𝑝𝜖2) and E[𝑓 𝑛,(1) 2 ]=
𝜖−𝜖 0+𝑛(𝜖 1+( 1−𝑝)𝜖 2). We take𝜖2 so thatQ𝑛+1 is more
likely to trigger the global filter on𝐷(1) and more likely to
succeed on𝐷 (0) :
𝑛𝜖1+𝜖−𝜖 0+𝑛𝜖 2/2+𝜖 0 =𝜖𝑔 (10)
Subtracting Eq. 7 from Eq. 10, we get 𝜖0−𝑛𝜖 2/2 = 0,
i.e.,𝜖 2 =2𝜖 0/𝑛.
Define𝐵(𝜒) ∼𝜒(𝑛−𝐵)+( 1−𝜒)𝐵 , the number of queriers
that ask for𝜖2 at𝑡= 2, with𝐵∼B(𝑛,𝑝) as in the proof of
Thm. 3.1. By construction,𝜖0 passesQ𝑛+1’s per-querier filter,
so we can only return⊥ if𝜖0 hits the shared filter’s capacity:
𝑉𝑛+1,(𝜒) 2 =⊥ ⇐⇒𝑓 𝑛,(0) 2 +𝜖 0 >𝜖 𝑔 (11)
⇐⇒𝑛𝜖 1+𝜖−𝜖 0+𝐵(𝜒)𝜖2+𝜖 0 >𝜖−𝜖 0+𝑛(𝜖 1+𝜖 2)
(12)
⇐⇒𝐵 (𝜒)𝜖2+𝜖 0 >𝑛𝜖 2 (13)
⇐⇒2𝐵 (𝜒)/𝑛+1>2(14)
⇐⇒𝐵 (𝜒) >𝑛/2(15)
We now upper-bound Pr[𝐵(0) >𝑛/ 2] and lower-bound
Pr[𝐵(1) >𝑛/2]. By Hoeffding’s inequality, we have:
Pr[𝐵(0) >𝑛/2]=Pr[𝐵>𝑛/2](16)
≤Pr[𝐵≥𝑛/2](17)
=Pr[𝐵−𝑛𝑝≥𝑛(1/2−𝑝)](18)
≤exp(−2(1/2−𝑝) 2𝑛)(19)
(20)
Similarly:
Pr[𝐵(1) >𝑛/2]=Pr[𝑛−𝐵>𝑛/2](21)
=1−Pr[𝐵≥𝑛/2](22)
≥1−exp(−2(1/2−𝑝) 2𝑛)(23)
Finally, set𝑆={(𝑣,⊥),𝑣> 1}. Since Pr[𝑉𝑛+1,(1) 1 > 1]=
𝑒𝜖−𝜖 0 Pr[𝑉𝑛+1,(0) 1 > 1] and𝑉𝑛+1,(𝜒) 1 and𝑉𝑛+1,(𝜒) 2 are indepen-
dent, we get:
Pr[𝑉𝑛+1,(1) ∈𝑆]
Pr[𝑉𝑛+1,(0) ∈𝑆] =𝑒𝜖−𝜖 0 Pr[𝑉𝑛+1,(1) 2 =⊥] Pr[𝑉𝑛+1,(0) 2 =⊥] (24)
=𝑒𝜖−𝜖 0 Pr[𝐵(1) >𝑛/2] Pr[𝐵(0) >𝑛/2] (25)
≥𝑒 𝜖−𝜖 0 exp(2(1/2−𝑝) 2𝑛)−1  (26)
Now, since the median of𝐵 is⌊𝑛𝑝⌋ or⌈𝑛𝑝⌉, we already
have Pr[𝐵(0) >𝑛/ 2]< 1/2 <Pr[𝐵 (1) >𝑛/ 2] when⌈𝑛𝑝⌉<
𝑛/2, which happens for𝑛 large enough or𝑝 small enough
(i.e.,𝜖large enough).
We can get a more informative bound asymptotically. Set
𝛼𝑛 :=exp((1/2−𝑝) 2𝑛). We have Pr[𝑉𝑛+1,(1)∈𝑆] Pr[𝑉𝑛+1,(0)∈𝑆] ≥𝛼 2 𝑛− 1. For
𝛼𝑛 large enough, for instance any𝛼𝑛≥ 2, we have𝛼 2 𝑛−1≥𝛼 𝑛.
We have𝛼𝑛≥ 2 ⇐⇒𝑛≥ ln 2 (1/2−𝑝) 2 = 4 ln 2 (1−𝑒−𝜖/2) 2 , so for such
𝑛we get:
Pr[𝑉𝑛+1,(1) ∈𝑆]
Pr[𝑉𝑛+1,(0) ∈𝑆] (27)
≥𝑒 𝜖−𝜖 0𝛼𝑛 (28)
=𝑒𝜖−𝜖 0(exp(1/2−𝑝) 2))𝑛 (29)
That is:

ln  Pr[𝑉𝑛+1,(0) ∈𝑆] Pr[𝑉𝑛+1,(1) ∈𝑆] 

≥𝜖+𝑛𝜖 ′ >𝜖(30)
with𝜖′ :=(1/2−𝑝) 2 >0.
□
Remark about atomicity.We clarify notation for Alg. 1,
Line 14, where a query is executed only if both the per-
querier filter and the shared limit permit it. The joint condi-
tion
F𝑘(𝑞𝑘 1,...,𝑞 𝑘 𝑡)∧L(𝑞 1 1,...,𝑞 𝐾 1,...,𝑞 𝑘 𝑡)

means that each filter takes its decision independently. In
particular, ifF𝑘 accepts a query𝑞𝑘 𝑡 whileL rejects it,𝑞𝑘 𝑡 will
not be executed, butF𝑘 will not know that fact when it is
time to make a decision about𝑞𝑘 𝑡+1. That meansF𝑘 can be
overly conservative, by deducting budget for queries that
are in fact not executed. While this preserves privacy, it can
hurt utility. We propose a solution to this conundrum in §4,
thanks to a new form of atomic filter that is designed to
avoid spending per-querier budget needlessly. This can be
modeled by a new object (F𝑘◦L)(𝑞 1 1,...,𝑞 𝐾 1,...𝑞 𝑘 𝑡) that
has access to all the previous queries. The shared state in
this object means that per-querier budgets act as heuristics
(as opposed to formal per-querier DP guarantees) unless a
dedicated siloing assumption holds.
A.3 Extension to Individual DP filters
The model from Alg. 1 considers standard filters [38], where
queriers can directly observe whether a query gets rejected.
However, systems such as Cookie Monster [43] or ARA [16]
operate under individual DP filters [14], which behave differ-
ently. Because an IDP budget depends on the data itself, IDP
filters cannot return⊥ explicitly when they are out of bud-
get. Instead, they silently drop the out-of-budget individuals
from the dataset and return a noisy answer.
This raises the question: since filter outputs are not visible
under IDP, do shared limits still leak extra information? We
give a positive answer. First, we adapt the formalism to IDP
filters in Alg. 4, with changes from Alg. 3 in blue. Next,
Thm. A.1 shows a variant of Thm. 3.2 for IDP filters. Finally,
Thm. 3.1 immediately applies since the counterexample from
the proof does not trigger any filter, and therefore works
identically under IDP filters.
Theorem A.1.Take 𝐾=𝑛+ 1 > 1, per-querier individual
filters with capacity𝜖 and shared individual filter with capacity
𝜖𝑔 <(𝑛+ 1)𝜖 (allowing executions that trigger the shared limit).
There exists𝜖′ > 0and neighboring databases 𝐷,𝐷′ such
that
∃(Q 1,...,Q 𝑛+1),∃𝑆⊆R 𝑡max,

ln  Pr[𝑉𝑛+1,(0) ∈𝑆] Pr[𝑉𝑛+1,(1) ∈𝑆] 

≥𝜖+𝑛𝜖 ′.
Proof. We modify the execution from the proof for Thm. 3.2
to match IDP semantics, where records get dropped condi-
tionally on past results. This emulates a form of data adap-
tivity, except that datasets𝑆𝑛+1 2 now differ because of shared
filters for various records, instead of through a data genera-
tion process. We then reuse the calculation from the proof
of Thm. 3.2.
The changes in execution are as follows:
•𝐷 ′ contains𝑛+ 1distinct records{𝑥0,𝑥 1,...,𝑥 𝑛} and𝐷
only contains{𝑥1,...,𝑥 𝑛}. We no longer have𝐷∈N ,
instead𝐷∈N X withX={𝑥 0,...,𝑥 𝑛}.
• At𝑡= 1, queriers submit 𝑞𝑘 1 : 𝐷↦→|{𝑥∈𝐷 : 𝑥=
Alg. 4Formal model for shared limits with IDP filters
1:Input
2:Database𝐷
3:QueriersQ 1,...,Q 𝐾
4:Per-querier individual filters(F 1 𝑥,...,F 𝐾 𝑥)𝑥∈𝐷
5:Shared limit(L 𝑥)𝑥∈𝐷
6:Output
7:View𝑉=(𝑉 1,...,𝑉 𝐾)∈R 𝑡max×𝐾 of allQ 𝑘
8:for𝑡∈[𝑡 max]do
9:for𝑘∈[𝐾]do
//Query based onQ 𝑘 ’sownprevious results
10:𝑞 𝑘 𝑡←Q 𝑘(𝑉𝑘 <𝑡)
//Execute if (1) Q𝑘 has enough budget and (2) shared
limit accepts the query.
11:𝑆 𝑘 𝑡 ←𝐷
12:for𝑥∈𝐷do
13:ifF 𝑘 𝑥(𝑞𝑘 1,...,𝑞 𝑘 𝑡)∧L 𝑥(𝑞1 1,...,𝑞 𝐾 1,...𝑞 𝑘 𝑡)then
//Drop out-of-budget records.
14:𝑆 𝑘 𝑡 ←𝑆 𝑘 𝑡\{𝑥}
15:𝑉 𝑘 𝑡 ←𝑞𝑘 𝑡(𝑆𝑘 𝑡)
𝑥0}|+Lap( 1/𝜖). This consumes 𝑥0’s full individual
budget.
•At𝑡=2:
– For𝑘∈[𝑛] , querier𝑘 requests𝑥𝑘 with full budget,
conditionally on past results. That is:
Q𝑘(𝑉𝑘 1)=𝑞 𝑘 2 :𝐷↦→1[𝑉 𝑘 1 ≤ 1/2]·(|{𝑥∈𝐷 :𝑥=
𝑥𝑘}|+Lap(1/𝜖))
– Finally, querier 𝑛+ 1requests all the records
𝑥1,...,𝑥 𝑛:
Q𝑛+1(𝑉𝑛+1 1 )=𝑞 𝑛+1 2 : 𝐷↦→ |{𝑥∈𝐷 : 𝑥∈
{𝑥1,...,𝑥 𝑛}}|+Lap(1/𝜖)
Since{𝑥1,...,𝑥 𝑛} are present in both worlds,𝑉𝑛+1,(1) and
𝑉𝑛+1,(0) differ only by the points that get dropped at Line 14.
Point𝑥𝑘 gets dropped only if𝑉𝑘 1 ≤ 1/2, which is more likely
to happen in world 0 (on input𝐷). More precisely, we have:
𝑉𝑛+1,(0) ∼𝐵+𝑍and𝑉 𝑛+1,(1) ∼𝑛−𝐵+𝑍(31)
with 𝐵∼ B(𝑛,𝑝) with 𝑝= 1 2 exp(−𝜖/ 2) and 𝑍∼
Lap(1/𝜖).
This is exactly the same situation as Eq. 6, where the𝑒𝜖
factor comes from the privacy loss at𝑡= 1. We conclude the
same way.
□
A.4 Querier-Siloing Assumption
Lemma A.2.Consider Alg. 1 with 𝐾∈N , per-querier filters
with capacity 𝜖> 0and shared limit L. Suppose that the

following assumption holds:
∀𝑘∈[𝐾],∀𝑢,𝑤∈R 𝑡 :𝑢 𝑘 =𝑤 𝑘,(32)
L

𝑞1 1,...,𝑞 𝐾 1,...,𝑞 1 𝑡(𝑢1 <𝑡),...𝑞 𝑘 𝑡(𝑢𝑘 <𝑡)  ·𝑞𝑘 𝑡(𝐷≤𝑡(𝑢<𝑡))
=L

𝑞1 1,...,𝑞 𝐾 1,...,𝑞 1 𝑡(𝑤 1 <𝑡),...𝑞 𝑘 𝑡(𝑤𝑘 <𝑡)  ·𝑞𝑘 𝑡(𝐷≤𝑡(𝑤<𝑡))
Then, for all𝑘∈[𝐾]:
∀𝑥0∈X,∀𝑡 0∈[𝑡 max],∀G,∀(Q 1,...,Q 𝑛+1),
∀𝑆⊆R 𝑡max,

ln  Pr[𝑉𝑘,(0) ∈𝑆] Pr[𝑉𝑘,(1) ∈𝑆] 

≤𝜖.
In other words, if querier 𝑘’s results don’t depend on other
queriers, either through data or shared limits, then Alg. 1 is
per-querier𝜖-DP for querier𝑘.
Proof. Take𝑥∈X ,G,Q1,...,Q 𝐾,𝑘∈[𝐾] , and𝑣𝑘∈R 𝑡 max.
We have:
Pr[𝑉𝑘 =𝑣 𝑘]=
𝑡maxÖ
𝑡=1
Pr[𝑉𝑘 𝑡 =𝑣 𝑘 𝑡|𝑉𝑘 1 =𝑣 𝑘 1,...,𝑉 𝑘 𝑡−1 =𝑣 𝑘 𝑡−1]
Take𝑡∈[𝑡 max]. We now express𝑉𝑘 𝑡 in terms of queries
and filter decisions, since the filter properties are necessary
for the privacy proof. Without loss of generality, we treat
filters as functions that return 0 for reject and 1 for accept at
Line 14, and we output0instead of ⊥ at Line 17. Hence, we
can express𝑉 𝑘 𝑡 as:
𝑉𝑘 𝑡 =F 𝑘(𝑞𝑘 1,...,𝑞 𝑘 𝑡)·L(𝑞 1 1,...,𝑞 𝐾 1,...𝑞 𝑘 𝑡)·𝑞 𝑘 𝑡(𝐷≤𝑡)(33)
The terms in this expression depend on various variables:
• Once we condition on 𝑣𝑘 1,...,𝑣 𝑘 𝑡−1 , we know the
queries asked byQ 𝑘:
𝑞𝑘 1 =Q 𝑘(),𝑞𝑘 2 =Q 𝑘(𝑣𝑘 1),...,𝑞 𝑘 𝑡 =Q 𝑘(𝑣𝑘 1,...,𝑣 𝑘 𝑡−1).(34)
• As a consequence,F𝑘(𝑞𝑘 1,...,𝑞 𝑘 𝑡) is also fully deter-
mined by𝑣 𝑘 1,...,𝑣 𝑘 𝑡−1 .
• However,L(𝑞 1 1,...,𝑞 𝐾 1,...𝑞 𝑘 𝑡) can depend on other
queriers’ past results𝑉𝑖 𝑡 for𝑖≠𝑘 , since these outputs
are used to select𝑞𝑖 𝑡.
• Similarly,𝐷≤𝑡 can also depend on other queriers’ past
results.
Pose𝑉 ≠𝑘 :=(𝑉 𝑗 𝑖)𝑖∈[𝑡],𝑗∈[𝐾]\{𝑘} . By the law of total proba-
bility, we have:
Pr[𝑉𝑘 𝑡 =𝑣 𝑘 𝑡 |𝑉 𝑘 <𝑡 =𝑣 𝑘 <𝑡]
=
∫
𝑣≠𝑘∈R𝑡×(𝐾−1)
Pr[𝑉𝑘 𝑡 =𝑣 𝑘 𝑡 |𝑉 𝑘 <𝑡 =𝑣 𝑘 <𝑡,𝑉 ≠𝑘 =𝑣 ≠𝑘]
·Pr[𝑉 ≠𝑘 =𝑣 ≠𝑘]𝑑𝑣 ≠𝑘 (35)
Take any𝑣 ≠𝑘∈R 𝑡×(𝐾−1) . Define𝑢∈R 𝑡×𝐾 by concate-
nating𝑣𝑘 and𝑣 ≠𝑘 such that𝑢𝑘 =𝑣 𝑘 and𝑢≠𝑘 =𝑣 ≠𝑘. Thanks
to Eq. 33 with explicit conditioning on all past results, we
have:
Pr[𝑉𝑘 𝑡 =𝑣 𝑘 𝑡|𝑉𝑘 1 =𝑣 𝑘 1,...,𝑉 𝑘 𝑡−1 =𝑣 𝑘 𝑡−1,𝑉 ≠𝑘 =𝑣 ≠𝑘]
=F 𝑘(𝑞𝑘 1,...,𝑞 𝑘 𝑡(𝑢𝑘 <𝑡))
·L

𝑞1 1,...,𝑞 𝐾 1,...,𝑞 1 𝑡(𝑢1 <𝑡),...𝑞 𝑘 𝑡(𝑢𝑘 <𝑡) 
·𝑞𝑘 𝑡(𝐷≤𝑡(𝑢<𝑡)) (36)
Define ˜𝑣∈R 𝑡×𝐾 by concatenating 𝑣𝑘 and(⊥,...,⊥)∈
R𝑡×(𝐾−1) . We have ˜𝑣𝑘 =𝑢𝑘, so by Eq. 32, Eq. 36 becomes:
Pr[𝑉𝑘 𝑡 =𝑣 𝑘 𝑡|𝑉𝑘 1 =𝑣 𝑘 1,...,𝑉 𝑘 𝑡−1 =𝑣 𝑘 𝑡−1,𝑉 ≠𝑘 =𝑣 ≠𝑘](37)
=F 𝑘(𝑞𝑘 1,...,𝑞 𝑘 𝑡( ˜𝑣𝑘 <𝑡))(38)
·L

𝑞1 1,...,𝑞 𝐾 1,...,𝑞 1 𝑡( ˜𝑣 1 <𝑡),...𝑞 𝑘 𝑡( ˜𝑣𝑘 <𝑡)  (39)
·𝑞𝑘 𝑡(𝐷≤𝑡( ˜𝑣<𝑡)) (40)
This term is independent of𝑣 ≠𝑘, so we can express it as a
function of𝑣𝑘 <𝑡 and take it out of the integral at Eq. 35, which
gives:
Pr[𝑉𝑘 𝑡 =𝑣 𝑘 𝑡|𝑉𝑘 1 =𝑣 𝑘 1,...,𝑉 𝑘 𝑡−1 =𝑣 𝑘 𝑡−1](41)
=

F𝑘(𝑞𝑘 1,...,𝑞 𝑘 𝑡)·L(𝑞 1 1,...,𝑞 𝑘 𝑡)·𝑞 𝑘 𝑡(𝐷≤𝑡)   𝑣𝑘 <𝑡  (42)
Now we can bound the per-querier privacy loss:

ln  Pr[𝑉𝑘 =𝑣 𝑘] Pr[𝑉𝑘 =𝑣 𝑘] 

=

ln  𝑡maxÖ 𝑡=1 Pr[𝑉𝑘,(0) 𝑡 =𝑣 𝑘 𝑡|𝑉𝑘,(0) 1 =𝑣 𝑘 1,...,𝑉 𝑘,(0) 𝑡−1 =𝑣 𝑘 𝑡−1] Pr[𝑉𝑘,(1) 𝑡 =𝑣 𝑘 𝑡|𝑉𝑘,(1) 1 =𝑣 𝑘 1,...,𝑉 𝑘,(1) 𝑡−1 =𝑣 𝑘 𝑡−1] !

≤
𝑡max∑︁
𝑡=1

 ln '››››
«
Pr

F𝑘(𝑞𝑘 1,...,𝑞𝑘 𝑡)·L(𝑞 1 1,...,𝑞𝑘 𝑡)
·𝑞𝑘 𝑡(𝐷(0) ≤𝑡){𝑣𝑘 <𝑡}=𝑣𝑘 𝑡

Pr

F𝑘(𝑞𝑘 1,...,𝑞𝑘 𝑡)·L(𝑞 1 1,...,𝑞𝑘 𝑡)
·𝑞𝑘 𝑡(𝐷(1) ≤𝑡){𝑣𝑘 <𝑡}=𝑣𝑘 𝑡

“ﬁﬁﬁﬁ
‹

≤
𝑡max∑︁
𝑡=1

ln  Pr[F 𝑘(𝑞𝑘 1,...,𝑞 𝑘 𝑡)·𝑞 𝑘 𝑡(𝐷(0) ≤𝑡){𝑣𝑘 <𝑡}=𝑣 𝑘 𝑡] Pr[F 𝑘(𝑞𝑘 1,...,𝑞 𝑘 𝑡)·𝑞 𝑘 𝑡(𝐷(1) ≤𝑡){𝑣𝑘 <𝑡}=𝑣 𝑘 𝑡] !

 (43)
The last inequality comes from what follows.L(𝑞 1 1,...,𝑞 𝑘 𝑡)
is entirely determined by𝑣𝑘 <𝑡 and thus identical in the nu-
merator and denominator. For 𝑡 whereL(𝑞 1 1,...,𝑞 𝑘 𝑡)= 1,
theL factor is one and can be omitted from the product. For

𝑡whereL(𝑞 1 1,...,𝑞 𝑘 𝑡)=0, we have:

 ln '››››
«
Pr

F𝑘(𝑞𝑘 1,...,𝑞𝑘 𝑡)·L(𝑞 1 1,...,𝑞𝑘 𝑡)
·𝑞𝑘 𝑡(𝐷(0) ≤𝑡){𝑣𝑘 <𝑡}=𝑣𝑘 𝑡

Pr

F𝑘(𝑞𝑘 1,...,𝑞𝑘 𝑡)·L(𝑞 1 1,...,𝑞𝑘 𝑡)
·𝑞𝑘 𝑡(𝐷(1) ≤𝑡){𝑣𝑘 <𝑡}=𝑣𝑘 𝑡

“ﬁﬁﬁﬁ
‹

=0≤

ln  Pr[F 𝑘(𝑞𝑘 1,...,𝑞 𝑘 𝑡)·𝑞 𝑘 𝑡(𝐷(0) ≤𝑡){𝑣𝑘 <𝑡}=𝑣 𝑘 𝑡] Pr[F 𝑘(𝑞𝑘 1,...,𝑞 𝑘 𝑡)·𝑞 𝑘 𝑡(𝐷(1) ≤𝑡){𝑣𝑘 <𝑡}=𝑣 𝑘 𝑡] !

The rest of the proof is identical to standard filter guar-
antees on adaptively generated data. Suppose the filter uses
an upper bound𝜖𝑖 on the privacy loss for each query at step
𝑖∈[𝑡 max]:

ln  Pr[𝑞𝑘 𝑖(𝐷(0) ≤𝑖){𝑣𝑘 <𝑖}=𝑣 𝑘 𝑖] Pr[𝑞𝑘 𝑖(𝐷(1) ≤𝑖){𝑣𝑘 <𝑖}=𝑣 𝑘 𝑖] !

≤𝜖𝑖(𝑣𝑘 <𝑖)(44)
Then, by definition of pure DP filters, we get the following
recursive property for 𝑡∈ [𝑡 max]:F𝑘(𝑞𝑘 1,...,𝑞 𝑘 𝑡)= 1iff˝
𝑖<𝑡F𝑘(𝑞𝑘 1,...,𝑞 𝑘 𝑡)·𝜖 𝑖(𝑣𝑘 <𝑖)+𝜖 𝑡(𝑣𝑘 <𝑡)≤𝜖.
We conclude by applying this property at 𝑡=𝑡 max in
Eq. 43:

ln  Pr[𝑉𝑘 =𝑣 𝑘] Pr[𝑉𝑘 =𝑣 𝑘] 

≤𝜖
□
Theorem A.3.Suppose that the following two assumptions
hold:
1. Querier𝑘’s queries operate on a restricted data stream
that only depends on its own past results. That is, 𝐷𝑡←
G(𝑉 1 <𝑡,...𝑉 𝐾 <𝑡)is of the following form:
𝐷 1 𝑡←G(𝑉 1 <𝑡),...,𝐷 𝐾 𝑡 ←G(𝑉 𝐾 <𝑡)
with𝑞𝑘 𝑡(𝐷≤𝑡)=𝑞 𝑘 𝑡(𝐷𝑘 ≤𝑡).
2. Shared limits do not filter 𝑘’s reports depending on other
queriers’ results:
∀𝑘∈[𝐾],∀𝑢,𝑤∈R 𝑡 :𝑢 𝑘 =𝑤 𝑘,
L

𝑞1 1,...,𝑞 𝐾 1,...,𝑞 1 𝑡(𝑢1 <𝑡),...𝑞 𝑘 𝑡(𝑢𝑘 <𝑡) 
=L

𝑞1 1,...,𝑞 𝐾 1,...,𝑞 1 𝑡(𝑤 1 <𝑡),...𝑞 𝑘 𝑡(𝑤𝑘 <𝑡) 
Sufficient conditions for this property include queriers
being non-adaptive, never reaching the shared limit, or
operating on disjoint sets of devices (for on-device ac-
counting with IDP filters).
Then condition Eq. 32 holds, and thus per-querier guarantees
hold.
Proof.The first point implies:
𝑞𝑘 𝑡(𝑣𝑘 <𝑡)(𝐷≤𝑡(𝑣 <𝑡))=𝑞 𝑘 𝑡(𝑣𝑘 <𝑡)(𝐷≤𝑡(𝑣𝑘 <𝑡))
Combining this with the second point, we directly get the
assumption:
∀𝑘∈[𝐾],∀𝑢,𝑤∈R 𝑡 :𝑢 𝑘 =𝑤 𝑘,(45)
L

𝑞1 1,...,𝑞 𝐾 1,...,𝑞 1 𝑡(𝑢1 <𝑡),...𝑞 𝑘 𝑡(𝑢𝑘 <𝑡)  ·𝑞𝑘 𝑡(𝐷≤𝑡(𝑢<𝑡))
=L

𝑞1 1,...,𝑞 𝐾 1,...,𝑞 1 𝑡(𝑤 1 <𝑡),...𝑞 𝑘 𝑡(𝑤𝑘 <𝑡)  ·𝑞𝑘 𝑡(𝐷≤𝑡(𝑤<𝑡))
□
B Global IDP with Big Bird (§4 Proofs)
B.1 Data and query model for Big Bird
This section sets up the formalism that underpins the main
theorems, proved in subsequent sections and evoked in the
body of the paper. We begin by defining Big Bird’s data
and query model, broadly adapted from Cookie Monster’s
formalism. We then provide useful properties that will be
needed in subsequent sections. Indeed, while Cookie Monster
analyzes global and individual sensitivities of queries at the
device-epoch level, Big Bird additionally needs such analyses
at the device-epoch-site level.
Definition B.1(User actions, sites and events).Let U be
the set of user-action identifiers,S the set of site identifiers,
I the set of impression payloads andC the set of conversion
payloads.
Aneventis either an impression event (𝑢,𝑖,imp) or a con-
version event(𝑢,𝑐,b,conv):
•𝑢∈U is the user action that caused the impression or
conversion. The same user action can cause multiple
events, and is denoted uaCtx in the body of the paper.
On a fixed device, all accepted impression events car-
rying the same user-action identifier occur in a single
epoch.
•𝑖∈S (resp.𝑐∈S ) is the impression (resp. conversion)
site where the event occurred.
• Conversions contain the set of queriersb⊂S that will
receive the conversion report. (bis a singleton unless
we use the optimization from §D.)
• The payload imp∈ I or conv∈ C can be used to
define concrete attribution functions.
We write sets of all impression events and all conversion
events as follows:
Fimp :=U×S×I,F conv :=U×S×P(S)×C,
and we writeF:=F imp∪F conv for the set of all events.
Definition B.2(Database of device-epoch records).Let D
be the set of device identifiers andE the set of epoch iden-
tifiers. A database𝐷 is a set of device-epoch records where
each record𝑥=(𝑑,𝑒,𝐹)∈X=D×E×P(F) contains a
device𝑑, an epoch𝑒 and a set of impression and conversion
events𝐹⊂F . We write D for the set of all databases where
each(𝑑,𝑒)pair appears at most once.

Definition B.3(Conversion-site and impression-site event
sets from events).For any event set𝐹, define:
ImpSites(𝐹):={𝑖∈S:∃𝑢∈U,imp∈I,(𝑢,𝑖,imp)∈𝐹},
ConvSites(𝐹):={𝑐∈S:∃𝑢∈U,b⊂S,conv∈C,
(𝑢,𝑐,b,conv)∈𝐹}.
Furthermore, for any user action 𝑢∈U , define the user-
action-scoped variants of these sets:
ImpSites𝑢(𝐹):={𝑖∈S:∃imp∈I,(𝑢,𝑖,imp)∈𝐹},
ConvSites𝑢(𝐹):={𝑐∈S:∃b⊂S,conv∈C,
(𝑢,𝑐,b,conv)∈𝐹},
and let AccessedSites𝑢(𝐹) :=ImpSites𝑢(𝐹)∪ConvSites 𝑢(𝐹) .
We also write ImpActions(𝐹) :={𝑢∈U :∃𝑖∈S,imp∈
I,(𝑢,𝑖,imp)∈𝐹} for the user actions that saved the impres-
sions of𝐹.
We now define queries and reports, with a slight adap-
tation of Cookie Monster’s definitions to our per-site se-
mantics. While Cookie Monster comes with an arbitrary
set of public events𝑃 for each querier𝑏, here for simplicity
we assume that all the conversions for a querier are pub-
lic. Using Cookie Monster’s terminology, that means we set
𝑃 :={(𝑢,𝑐, b,conv) ∈F conv : 𝑏∈ b}. Also, while Cookie
Monster defines a set ofrelevant events, potentially including
conversions, in Def. B.5 we only considerrelevant impres-
sionsfor simplicity. In particular, this hardcodes "Case 1"
from [43, Thm. 1].
Definition B.4(Neighboring databases). 𝐷∼ 𝑥 𝐷′ iff data-
base𝐷′ is obtained from𝐷 by removing all impression events
of a single device-epoch𝑥. All conversion events are identical
for𝐷and𝐷 ′.
Definition B.5(Attribution function, adapted from Cookie
Monster).Fix a set ofrelevant impressions 𝐹𝐴⊂F imp such
that there exists𝐺𝐴⊂S×I with𝐹𝐴 =U×𝐺 𝐴 (i.e.,user
actions play no role in defining relevant impressions). Fix
𝑘,𝑚∈N ∗ where𝑘 is a number of epochs. Anattribution
functionis a function 𝐴 :P(F)𝑘→R 𝑚 that takes𝑘 event
sets𝐹1,...,𝐹 𝑘 from𝑘 epochs and outputs an𝑚-dimensional
vector𝐴(𝐹 1,...,𝐹 𝑘), such that onlyrelevant eventscontribute
to𝐴. That is, for all(𝐹 1,...,𝐹 𝑘)∈P(F) 𝑘, we have:
𝐴(𝐹 1,...,𝐹 𝑘)=𝐴(𝐹 1∩𝐹𝐴,...,𝐹 𝑘∩𝐹𝐴).(46)
In particular, conversion events never contribute to𝐴.
Definition B.6(Report identifier and attribution report,
same as Cookie Monster).Fix a domain of report identifiers
Z. Consider a mapping𝑑(·) : Z→D from report identifiers
to devices that gives the device𝑑𝑟 that generated a report𝑟.
Given an attribution function𝐴, a set of epochs𝐸 and a
report identifier𝑟∈Z , theattribution report 𝜌𝑟,𝐴,𝐸 , or𝜌𝑟 for
short, is a function over the whole database𝐷defined by:
𝜌𝑟 :𝐷∈D↦→𝐴(𝐷 𝐸 𝑑𝑟),(47)
When several reports are in play, we write 𝐴𝑟 ,𝐸𝑟 and𝐹𝐴𝑟
for the attribution function, the set of epochs and the set of
relevant impressions attached to report𝑟, so that𝜌𝑟 :𝐷↦→
𝐴𝑟(𝐷𝐸𝑟 𝑑𝑟 ). The mechanism also stores, with each identifier, the conversion site𝑐𝑟 and the opaque action context𝑢𝑟 of the
measureConversion request that created𝑟 (Alg. 7). Neither
changes the function𝜌𝑟 :𝑢𝑟 is only used for the per-action
domain cap.
Definition B.7(Query, same as Cookie Monster).Consider
a set of report identifiers𝑅⊂Z , and a set of attribution re-
ports(𝜌𝑟)𝑟∈𝑅 each with output in R𝑚. Thequeryfor (𝜌𝑟)𝑟∈𝑅
is the function𝑄 : D→R 𝑚 defined as𝑄(𝐷) := ˝ 𝑟∈𝑅 𝜌𝑟(𝐷)
for𝐷∈D.
Definition B.8(Device-epoch sensitivity, same as Cookie
Monster).Fix a report 𝜌 : D→R 𝑚 for some𝑚. We define
theindividual 𝐿1 sensitivity of𝜌 for a device-epoch 𝑥∈X as
follows:
Δ𝑥(𝜌):=max 𝐷,𝐷′∈D:𝐷′∼𝑥𝐷 ∥𝜌(𝐷)−𝜌(𝐷 ′)∥ 1.(48)
We also define thedevice-epoch global 𝐿1 sensitivity of𝜌
as follows:
Δ(𝜌):=max
𝑥∈X
Δ𝑥(𝜌)(49)
Definition B.9(Device-epoch-impression-site sensitivity).
Fix a report 𝜌 : D→R 𝑚 for some𝑚, and an impression
site𝑖∈S . We define theindividual 𝐿1 sensitivity of𝜌 for a
device-epoch-site𝑥∈X,𝑖∈Sas follows:
Δ𝑥,𝑖(𝜌):=max 𝐷,𝐷′∈D:𝐷′∼𝑥,𝑖𝐷 ∥𝜌(𝐷)−𝜌(𝐷 ′)∥ 1 (50)
where𝐷∼ 𝑥,𝑖 𝐷′ iff database 𝐷′ is obtained from 𝐷 by
removing all impression events on a single site𝑖of a single
device-epoch𝑥. Equivalently, there exists𝐷0∈D , a record
𝑥∈ X such that{𝐷,𝐷′}={𝐷 0+𝑥,𝐷 0+𝑥 𝑖→∅}, where
𝑥𝑖→∅ :=(𝑑,𝑒,𝐹 𝑖→∅) is the record obtained by removing all
the impressions on𝑖from𝑥.
We also define thedevice-epoch-site global 𝐿1 sensitivity of
𝜌as follows:
Δ𝑖(𝜌):=max 𝑥∈X Δ𝑥,𝑖(𝜌)(51)
To simplify subsequent results, we define some notation:
Definition B.10(Zeroing-out).Fix a vector of impression
setsF =(𝐹 1,...,𝐹 𝑘)∈P(F imp)𝑘 for any𝑘> 0. For𝑖∈S
and𝑗∈[𝑘]we define:
• F𝑗→∅ :=(𝐹 1,...,𝐹 𝑗−1,∅,𝐹 𝑗+1,...,𝐹 𝑘),i.e.,we zero-out
the𝑗th epoch.

• F𝑗,𝑖→∅ :=(𝐹 1,...,𝐹 𝑗−1,𝐹 𝑗\I𝑖,𝐹 𝑗+1,...,𝐹 𝑘),i.e.,we
zero-out all the impressionsI𝑖 :={(𝑢,𝑖,imp) : 𝑢∈
U,imp∈I}belonging to site𝑖from the𝑗th epoch.
Plugging Def. B.5 into Def. B.8 and Def. B.9 immediately
gives:
Lemma B.11(Global sensitivity of reports).Fix a device 𝑑,
a set of 𝑘 epochs𝐸, an attribution function 𝐴 and the corre-
sponding report𝜌:𝐷↦→𝐴(𝐷 𝐸 𝑑). We have:
Δ(𝜌)=max
F∈P(F imp)𝑘,𝑗∈[𝑘] ∥𝐴(F)−𝐴(F 𝑗→∅)∥ 1.(52)
Moreover, for any impression site𝑖∈Swe have:
Δ𝑖(𝜌)=max
F∈P(F imp)𝑘,𝑗∈[𝑘] ∥𝐴(F)−𝐴(F 𝑗,𝑖→∅)∥ 1.(53)
Theorem B.12(Individual sensitivity of reports per epoch-site).
Fix a report identifier𝑟 , with device𝑑𝑟 , epochs𝐸𝑟 ={𝑒 (𝑟) 1 ,...,𝑒 (𝑟) 𝑘 },
attribution function𝐴𝑟 and relevant impressions 𝐹𝐴𝑟 , and let
𝜌𝑟 be the corresponding report from Eq. 47. Fix an impression
site𝑖∈S and a device-epoch record 𝑥=(𝑑,𝑒,𝐹)∈X , and
write𝐹𝑖 :=𝐹∩I 𝑖 for the impressions of 𝑥 on site𝑖. Finally, let
𝐼𝑟(𝑥):=ImpSites(𝐹∩𝐹 𝐴𝑟)(54)
be the impression sites of 𝑥 that can contribute to 𝜌𝑟 . We can
upper bound the individual sensitivity of 𝜌𝑟 per epoch-site as
follows:
Δ𝑥,𝑖(𝜌𝑟)≤
 

0if𝑑≠𝑑 𝑟 ,𝑒∉𝐸 𝑟 ,
or𝑖∉𝐼 𝑟(𝑥),
∥𝐴𝑟(𝐹𝑖)−𝐴 𝑟(∅)∥ 1 if𝑑=𝑑 𝑟 ,𝐸𝑟 ={𝑒}
and𝐼𝑟(𝑥)={𝑖},
Δ𝑖(𝜌𝑟)if𝑑=𝑑 𝑟 ,𝑒∈𝐸 𝑟 ,
𝑖∈𝐼 𝑟(𝑥), and
|𝐸𝑟|≥2or|𝐼 𝑟(𝑥)|≥2.
(55)
Proof.By Def. B.9, each pair(𝐷,𝐷 ′)in the maximum defin-
ing Δ𝑥,𝑖(𝜌𝑟) satisfies{𝐷,𝐷′}={𝐷 0+𝑥,𝐷 0+𝑥𝑖→∅} for some
𝐷0 ∈D , where 𝑥𝑖→∅ =(𝑑,𝑒,𝐹\I 𝑖). Since 𝐷0+𝑥∈D ,
the database𝐷0 has no record at(𝑑,𝑒) . W.l.o.g we assume
𝐷=𝐷 0+𝑥 and𝐷′ =𝐷 0+𝑥𝑖→∅ . We now take the three cases
in turn.
• Case 1: 𝑑≠𝑑 𝑟 , or 𝑒∉𝐸 𝑟 , or 𝑖∉𝐼 𝑟(𝑥) .If 𝑑≠𝑑 𝑟 ,
then𝐷 and𝐷′ only differ in a record of device𝑑, so
𝐷𝐸𝑟 𝑑𝑟 =(𝐷 0)𝐸𝑟 𝑑𝑟 =(𝐷 ′)𝐸𝑟 𝑑𝑟 . If𝑒∉𝐸 𝑟 , then𝐷 and𝐷′ only differ in an epoch that 𝜌𝑟 does not read, and again
𝐷𝐸𝑟 𝑑𝑟 =(𝐷 ′)𝐸𝑟 𝑑𝑟 . Finally, suppose𝑖∉𝐼 𝑟(𝑥) , and assume
𝑑=𝑑 𝑟 and𝑒∈𝐸 𝑟 . The records at(𝑑,𝑒) do differ, but
not in any relevant impression: 𝐹∩𝐹 𝐴𝑟 contains no
impression on site𝑖, so
(𝐹\I 𝑖)∩𝐹 𝐴𝑟 =(𝐹∩𝐹 𝐴𝑟)\I 𝑖 =𝐹∩𝐹 𝐴𝑟.(56)
Then Eq. 46 gives𝐴𝑟(𝐷𝐸𝑟 𝑑𝑟 )=𝐴 𝑟((𝐷′)𝐸𝑟 𝑑𝑟 ).
• Case 2:𝑑=𝑑 𝑟 ,𝐸𝑟 ={𝑒} and𝐼𝑟(𝑥)={𝑖} .Here 𝑘= 1
and𝜌𝑟(𝐷)=𝐴 𝑟(𝐷𝑒 𝑑𝑟 ). As𝐷0 has no record at(𝑑𝑟,𝑒) ,
we get𝐷𝑒 𝑑𝑟 =𝐹 and(𝐷′)𝑒 𝑑𝑟 =𝐹\I 𝑖. Since site𝑖 has all
the relevant impressions of𝑥, we have𝐹∩𝐹 𝐴𝑟 ⊆I𝑖,
and therefore
𝐹∩𝐹 𝐴𝑟 =𝐹𝑖∩𝐹𝐴𝑟,(𝐹\I 𝑖)∩𝐹 𝐴𝑟 =∅.(57)
Eq. 46 then gives 𝐴𝑟(𝐹)=𝐴 𝑟(𝐹𝑖) and𝐴𝑟(𝐹\I 𝑖)=
𝐴𝑟(∅) , so every pair (𝐷,𝐷′) yields the same value
∥𝐴𝑟(𝐹𝑖)−𝐴 𝑟(∅)∥ 1.
• Case 3: 𝑑=𝑑 𝑟 ,𝑒∈𝐸 𝑟 ,𝑖∈𝐼 𝑟(𝑥) , and |𝐸𝑟| ≥2or
|𝐼𝑟(𝑥)|≥ 2.Let 𝑗∈ [𝑘] be the index of 𝑒 in𝐸𝑟 and
F:=𝐷 𝐸𝑟 𝑑𝑟 , so that(𝐷 ′)𝐸𝑟 𝑑𝑟 =F 𝑗,𝑖→∅ and
∥𝜌𝑟(𝐷)−𝜌 𝑟(𝐷′)∥ 1 =∥𝐴 𝑟(F)−𝐴 𝑟(F𝑗,𝑖→∅)∥ 1≤Δ 𝑖(𝜌𝑟),
(58)
by Eq. 53. Unlike in the first two cases, this quantity de-
pends on𝐷0 (through the events that the other epochs
of𝐸𝑟 contribute toF). Taking the maximum over 𝐷0
can only give back the global bound Δ𝑖(𝜌𝑟) in the
worst case.
□
Next, we show that Δ𝑖(𝜌)≤ 2Δ(𝜌) for any report. For
reports using certain attribution functions, we can have a
tighter Δ𝑖(𝜌)=Δ(𝜌) bound, but it does not hold in general.
Lemma B.13(Relation between Device-Epoch-Site and De-
vice-Epoch Sensitivities).For any report 𝜌 with attribution
function𝐴, let𝐹 denote the full dataset, 𝐹𝑗 denote all data in 𝐹
pertaining to epoch 𝑗, and𝐹𝑗,𝑖 denote all data in 𝐹𝑗 pertaining
to site𝑖. The following inequality holds:
Δ𝑖(𝜌)≤2Δ(𝜌)(59)
Proof. Recall the definition of device-epoch-site global sensi-
tivity:
Δ𝑖(𝜌)=max
F∈P(F imp)𝑘,𝑗∈[𝑘] ∥𝐴(F𝑗,𝑖→∅)−𝐴(F)∥ 1.(60)
We can decompose this expression using the triangle in-
equality:
∥𝐴(F𝑗,𝑖→∅)−𝐴(F)∥ 1 (61)
=∥𝐴(F𝑗,𝑖→∅)−𝐴(F 𝑗→∅)+𝐴(F 𝑗→∅)−𝐴(F)∥ 1 (62)
≤∥𝐴(F𝑗,𝑖→∅)−𝐴(F 𝑗→∅)∥ 1+∥𝐴(F 𝑗→∅)−𝐴(F)∥ 1 (63)
For the first term, note that 𝐴( F𝑗,𝑖→∅) uses events 𝐹𝑗,¬𝑖
from epoch 𝑗 where𝐹𝑗,¬𝑖 =𝐹 𝑗\𝐹 𝑗,𝑖 , while 𝐴( F𝑗→∅) uses
no events from epoch 𝑗. Since 𝐹𝑗,¬𝑖 ⊆𝐹 𝑗 and all events
from epoch 𝑗 for a given device come from a single device-
epoch record, we can view this as the change from adding a
single record containing events𝐹𝑗,¬𝑖 . This is bounded by the
definition ofΔ(𝜌):
∥𝐴(F𝑗,𝑖→∅)−𝐴(F 𝑗→∅)∥ 1≤Δ(𝜌).(64)
The second term represents the sensitivity to removing

events from the entire epoch𝑗. In the individual DP setting
with device-epoch records, all events from epoch𝑗 for a given
device come from a single device-epoch record. Removing
this entire record corresponds exactly to one of the cases
considered in the definition ofΔ(𝜌). Therefore:
∥𝐴(F𝑗→∅)−𝐴(F)∥ 1≤Δ(𝜌).(65)
Therefore, substituting the two upper bounds into Eq. (63):
Δ𝑖(𝜌)≤Δ(𝜌)+Δ(𝜌)=2Δ(𝜌).(66)
□
B.2 Comprehensive Big Bird Model
Overview.Big Bird manages per-site and global privacy fil-
ters using the quota mechanisms described in §4.3. Alg. 5 de-
picts the functionality triggered on receiving a report request
(i.e., measureConversion() and getReport()). Big Bird
checks and consumes budget from the relevant filters and
prunes the resulting report based on filter status. First,
Big Bird ensures all filters and quotas are initialized. Sec-
ond, it computes the privacy losses incurred both at the
epoch level [43, §C] and at the epoch-impression-site level
(Def. B.14). Third, it checks whether all filters have sufficient
budget and attempts to consume it. To avoid wasting budget
from some filters (or quotas) when other filters are out of
budget, Big Bird uses a transactional protocol to deduct pri-
vacy losses from multiple filters atomically. Alg. 6 formalizes
this: if any filter cannot afford its share of the privacy loss,
the report is zeroed out, and no budget is consumed from
any filter for that report.
Enforcing the per-action domain cap.In addition
to the filter-based budget checks, Big Bird enforces a
per-action domain cap cap on the number of distinct sites
that can access the Attribution API within a single user
action context (Def. B.1). This mechanism limits adversar-
ial creation of quota filters. As formalized in Alg. 5, the
per-action domain cap check occursbeforethe atomic filter
check: if the check fails, the epoch’s data is zeroed out
(𝐹𝑒←∅ , using the zeroing-out notation from Appendix B.1),
and no filters are accessed for that epoch.
Subroutines.Def. B.15, B.14, B.16 and Alg. 6 define sub-
routines used in Alg. 5. The first two definitions rely on the
sensitivity bounds from Thm. B.12 (for the impression-site
quota) and [43] (for the filters and the other quotas).
Definition B.14(EpochImpSiteBudget).Let 𝑥=(𝑑,𝑒,𝐹)∈
X be a device-epoch record,𝑖∈S an impression site,𝜌 an
attribution report, and𝜆> 0the Laplace noise scale applied
to𝜌. Given the upper bound ˜Δ𝑥,𝑖(𝜌)≥Δ 𝑥,𝑖(𝜌) on the per-
epoch-site individual sensitivity given by Thm. B.12, we can
upper bound the epoch-site privacy loss consumed by𝜌 at
(𝑥,𝑖)by
EpochImpSiteBudget(𝑥,𝑖,𝜌,𝜆):=
˜Δ𝑥,𝑖(𝜌)
𝜆 .(67)
Definition B.15(EpochBudget, from [ 43]).Fix a device-
epoch record 𝑥∈ X , 𝜌 an attribution report, and 𝜆> 0
the Laplace noise scale applied to𝜌. Given the upper bound
˜Δ𝑥(𝜌)≥Δ 𝑥(𝜌) on the per-epoch individual sensitivity given
by [43], the individual privacy loss for device-epoch record
𝑥is:
EpochBudget(𝑥,𝜌,𝜆):=
˜Δ𝑥(𝜌)
𝜆 (68)
Definition B.16(Privacy filter F , adapted from [38]).Pri-
vacy filters track privacy loss of adaptively chosen mecha-
nisms against a predetermined budget. We adapt the standard
definition for pure DP privacy filters and define a filterF as
a stateful object storing its remaining capacity, initialized to
𝜖initial (the filter capacity).
We then recursively defineF.canConsume ,F.tryConsume
and passF,𝑗 , the indicator that the𝑗th budget was granted, for
a sequence of adaptively chosen privacy budgets𝜖1,𝜖 2,... ,
as follows:
•F.canConsume(𝜖 𝑗): ReturnsTRUEif the filter can ac-
commodate additional privacy loss𝜖𝑗,i.e., 𝜖𝑗≤𝜖 initial−˝
𝑗′<𝑗 𝜖𝑗′ ·passF,𝑗′ where𝜖 initial is the filter capacity.
•F.tryConsume(𝜖 𝑗): Calls canConsume(𝜖𝑗). If suc-
cessful, sets passF,𝑗 = 1to deduct 𝜖𝑗 from the filter’s
remaining capacity; otherwise, sets passF,𝑗 =0.
By definition of canConsume we obtain the followingca-
pacity invariant:
∑︁
𝑗
𝜖𝑗passF,𝑗≤𝜖 initial.(69)
Definition B.17(Per-action domain cap K).We define a
domain capas a stateful object K⊆S , initialized to∅ with
a cap𝜅 action and two methods, for a domain𝑠∈S:
•K.canAdmit(𝑠) ⇐⇒ |K∪{𝑠}|≤𝜅 action,
•K.tryAdmit(𝑠) : ifK.canAdmit(𝑠) , setK←K∪{𝑠} ;
otherwise leaveKunchanged.
Note that only the first admission for a given domain
can be rejected, and the invariant|K|≤𝜅 action bounds the
number of distinct domains.
Definition B.18(Per-device-epoch state F(𝑑,𝑒) ).For each
device-epoch record𝑥=(𝑑,𝑒,𝐹) , we maintain four families
of pure DP filters (global, per querier𝑏, per conversion site𝑐,
per impression site𝑖) and domain caps for each user action
𝑢. We denote the resulting stateF𝑑,𝑒:
F𝑑,𝑒 :=

F global 𝑑,𝑒 , F querier[𝑏] 𝑑,𝑒  𝑏∈S, F conv-quota[𝑐] 𝑑,𝑒  𝑐∈S,
F imp-quota[𝑖] 𝑑,𝑒  𝑖∈S, K𝑑,𝑒[𝑢] 𝑢∈U  ,(70)
We lazily initialize these filters/cap instantiated with re-
spective capacities𝜖global,𝜖 querier,𝜖 imp-quota,𝜖conv-quota,𝜅action.
We make two remarks. First, the state F𝑑,𝑒 can change
depending on the adversary’s queries, even when the under-

Alg. 5Big Bird algorithm on a single device
1:Input
2: Device𝑑with growing on-device database𝐷 𝑑←∅
3: State (F𝑑,𝑒)𝑒∈E lazily initialized with
caps𝜖 global,𝜖 querier,𝜖 imp-quota,𝜖 conv-quota,𝜅 action
4: defSaveImpression(𝑖,imp,𝑢)
5:𝑒←CurrentEpoch()
6:ifF 𝑑,𝑒.K[𝑢].canAdmit(𝑖)=FALSEthen
7:return//Silently reject impression if cap exceeded
8:F 𝑑,𝑒.K[𝑢].tryAdmit(𝑖)
9: //Store impression event
10:𝐷 𝑒 𝑑←𝐷 𝑒 𝑑∪{(𝑢,𝑖,imp)}
11:return
//Generate report and update on-device budget
12: defGenerateReport(𝐷,𝜌,𝜆,𝑢,𝑏)
13: Read𝜌 to get device𝑑, conversion site𝑐, target epochs𝐸, attribution
function𝐴with relevant impressions𝐹 𝐴.
14:for𝑒∈𝐸do
15:𝑥←(𝑑,𝑒,𝐷 𝑒 𝑑)
16:ifF 𝑑,𝑒.K[𝑢].canAdmit(𝑐)=FALSEthen//Def. B.18
17:𝐹 𝑒←∅//Zero out epoch if per-action domain cap exceeded
18:continue//Skip to next epoch
19:F 𝑑,𝑒.K[𝑢].tryAdmit(𝑐)
20:𝐹 𝑒←𝐷 𝑒 𝑑∩𝐹𝐴 //Effective relevant impressions
21:i 𝑒←ImpSites(𝐹 𝑒)//Effective impression sites
22:𝜖 𝑥←EpochBudget(𝑥,𝜌,𝜆)//Def. B.15
23:𝜖 i x←{}
24:for𝑖∈i 𝑒 do
25:𝜖 𝑖 𝑥←EpochImpSiteBudget(𝑥,𝑖,𝜌,𝜆)//Def. B.14
26:𝜖 i x[𝑖]←𝜖 𝑖 𝑥
//Check and update filters/quotas atomically (Alg. 6)
27: if AtomicFilterCheckAndConsume(F𝑥,𝑏,𝑐, i𝑒,𝜖𝑥,𝜖 i x)=FALSE
then
28:𝐹 𝑒←∅//Empty the epoch if any check fails
29: ˆ𝜌←𝐴((𝐹 𝑒)𝑒∈𝐸)//Clipped attribution report
30:return ˆ𝜌
31:
lying data is fixed (e.g.,when the data is generated in chunks
epoch by epoch). Second, since the pair(𝑑,𝑒) appears only
once in valid databases, we can index by 𝑥=(𝑑,𝑒,𝐹) to
obtain the sameF𝑥 even as𝐹 changes,e.g.,when new events
are added to the same device.
B.3 Global Privacy Guarantees
We now state and prove the privacy guarantees, stated for
a formal privacy game modeling Alg. 5 execution over the
whole system.
Execution model.Alg. 7 presents an abstract model of
Big Bird’s operation, capturing how it answers queries se-
quentially for all queriers. At each time step𝑡, querier𝑘 can
formulate a query𝑄𝑘 𝑡 , which is a batch of reports as defined
in Def. B.7. When a querier has nothing to ask, it can send
an empty query with zero sensitivity.AnswerQuery then pro-
cesses each individual report𝜌𝑟 (for𝑟∈𝑅 , where𝑅 is the set
of report identifiers in𝑄𝑘 𝑡 ). For each report, GenerateReport
creates an individual clipped attribution report. Finally, re-
Alg. 6AtomicFilterCheckAndConsume
1:Input
2: BudgetsF𝑥, querier 𝑏, conversion site 𝑐, impression
sitesi
3:𝜖 𝑥: epoch-level privacy loss
4:𝜖 i x: epoch-site-level privacy loss
5://Phase 1: check if all filters can consume (Def. B.16)
6:ifF querier[𝑏] 𝑥 .canConsume(𝜖𝑥)=FALSEthen
7:returnFALSE
8:ifF global 𝑥 .canConsume(𝜖𝑥)=FALSEthen
9:returnFALSE
10:ifF conv-quota[𝑐] 𝑥 .canConsume(𝜖𝑥)=FALSEthen
11:returnFALSE
12:for𝑖∈ido
13:ifF imp-quota[𝑖] 𝑥 .canConsume(𝜖 i x[𝑖])=FALSEthen
14:returnFALSE
15://Phase 2: consume from all filters (Def. B.16)
16:F querier[𝑏] 𝑥 .tryConsume(𝜖 𝑥)
17:F global 𝑥 .tryConsume(𝜖 𝑥)
18:F conv-quota[𝑐] 𝑥 .tryConsume(𝜖 𝑥)
19:for𝑖∈ido
20:F imp-quota[𝑖] 𝑥 .tryConsume(𝜖 i x[𝑖])
21:returnTRUE
ports are summed and noised before returning the query
result.
At Line 13, world 𝜒= 0skips all the impressions on
(𝑑0,𝑒 0), following the neighboring relation from Def. B.4,
and every other call is executed identically in both worlds.
Theorem 4.2.Consider 𝑥∈ X with global filter capacity
𝜖global. Then, Big Bird satisfies individual device-epoch 𝜖global-
DP for 𝑥 with respect to the neighboring relation in Defini-
tion B.4. That is, for all data generation processes G, for all
queriersQ1,...,Q 𝐾 , the output𝑉(𝜒) of Alg. 7 under challenge
bit𝜒verifies:
∀𝑣∈R 𝑒max×(𝑡 max+1)×𝐾,

ln  Pr[𝑉(0) =𝑣] Pr[𝑉(1) =𝑣] 

≤𝜖 global.(71)
Proof. Take the in-or-out device-epoch 𝑥=(𝑑 0,𝑒 0,𝐹) ∈
X. Denote by 𝑥C =(𝑑 0,𝑒 0,𝐹∩F conv) the device-epoch
obtained by keeping only public events from 𝑥, where
public events are the set of all conversions. Take 𝑣∈
R𝑒max×(𝑡 max+1)×𝐾 and 𝜒∈ { 0, 1}. 𝑣 is the vector of val-
ues returned at different points in Alg. 7. We split it
into 𝑣=(𝑣 1,0,𝑣 1,1,...,𝑣 1,𝑡max,...,𝑣 𝑒,0,...𝑣 𝑒,𝑡) where 𝑣𝑒,0 =
(𝑣 1 𝑒,0,...,𝑣 𝐾 𝑒,0) is a value for the output from Line 22 of Alg. 7
(public events from epoch 𝑒 for each querier 𝑘∈ [𝐾] ),
and 𝑣𝑒,𝑡 =(𝑣 1 𝑒,𝑡,...,𝑣 𝐾 𝑒,𝑡), where 𝑣𝑘 𝑒,𝑡 is the output for the
query𝑄𝑘 𝑡 for querier𝑘 at step𝑡 from epoch𝑒 (Line 27). By
conditioning over past outputs at each time step(𝑒,𝑡,𝑘)∈

Alg. 7Formalism for DP analysis
1:Input
2: Challenge bit𝜒∈{0,1}
3: In-or-out device-epoch(𝑑 0,𝑒 0)
4: Data generation processG
5: QueriersQ 1,...,Q 𝐾
6:Output
7: View𝑉=(𝑉 1,...,𝑉 𝐾)∈R 𝑒max×(𝑡 max+1)×𝐾 of allQ 𝑘
8:for𝑒∈[𝑒 max]do
//Devices and events for epoch𝑒, generated fromall previous results
9:𝐺←G(𝑉 1 <𝑒,...𝑉 𝐾 <𝑒)
//View of each querier, initialized empty for conversions
10:(𝑉 𝑘 𝑒,0)𝑘∈[𝐾] =(∅) 𝑘∈[𝐾]
11:for(𝑑,𝑓)∈𝐺do
12:if𝑓=(𝑢,𝑖,imp)∈F imp then
13:if𝜒=0and𝑑=𝑑 0,𝑒=𝑒 0 then
14:skip//Keep impression events out in World 0
15:else
16:SaveImpression(𝑖,imp,𝑢)on𝑑
17:else
//Each querier receives its conversions and corresponding report identifiers
18:𝐷 𝑒 𝑑←𝐷 𝑒 𝑑+𝑓, with𝑓=(𝑢,𝑐,b,conv)
19: Generate report identifier𝑟
$
←𝑈(Z)
//Save the device and action context that generated𝑟
20:(𝑑 𝑟,𝑢𝑟)←(𝑑,𝑢)
21:for𝑘∈bdo
22:𝑉 𝑘 𝑒,0←𝑉 𝑘 𝑒,0∪{(𝑟,𝑓)}//Output conversion and report identifier
23: //Queriers ask queries, round robin
24:for𝑡∈[𝑡 max]do
25:for𝑘∈[𝐾]do
//Querier𝑘chooses based onits own previous results
26:𝑄 𝑘 𝑡,𝜆𝑘 𝑡 ←Q 𝑘(𝑉𝑘 ≤𝑒,<𝑡)
27:𝑉 𝑘 𝑒,𝑡←AnswerQuery(𝐷 ≤𝑒,𝑄𝑘 𝑡,𝜆𝑘 𝑡,𝑘)
28: //Collect, aggregate and noise reports to answer𝑄
29: defAnswerQuery(𝐷,𝑄,𝜆,𝑏)
30:(𝜌 𝑟)𝑟∈𝑅 ←𝑄//Get report identifiers from𝑄
31:for𝑟∈𝑅do
32: ˆ𝜌𝑟←GenerateReport(𝐷,𝜌 𝑟,𝜆,𝑢 𝑟,𝑏)
33: Sample𝑋∼Lap(𝜆)
34:return ˝ 𝑟∈𝑅 ˆ𝜌𝑟+𝑋
[𝑒max]×{0,...,𝑡 max}×[𝐾]we get:
Pr[𝑉(𝜒) =𝑣](72)
=
𝑒maxÖ
𝑒=1
𝑡maxÖ
𝑡=0
𝐾Ö
𝑘=1
Pr[𝑉𝑘,(𝜒) 𝑒,𝑡 =𝑣 𝑘 𝑒,𝑡|𝑣 <𝑘 ≤𝑒,<𝑡].(73)
Take𝑒∈[𝑒 max],𝑡∈[𝑡 max] and𝑘∈[𝐾] . By Algorithm 7,
we have:
Pr[𝑉𝑘,(𝜒) 𝑒,𝑡 =𝑣 𝑘 𝑒,𝑡|𝑣 <𝑘 ≤𝑒,<𝑡](74)
=Pr[AnswerQuery(𝐷 (𝜒),𝑄𝑘 𝑡,𝜆𝑘 𝑡,𝑘;F 𝑘,(𝜒) 𝑒,𝑡 )=𝑣 𝑘 𝑒,𝑡],(75)
where the database𝐷(𝜒) , the query𝑄𝑘 𝑡 with associated noise
𝜆𝑘 𝑡 and the stateF𝑘,(𝜒) 𝑒,𝑡 are functions of past results𝑣 <𝑘 ≤𝑒,<𝑡 .
The generated data and the queries are chosen byG andQ𝑘
conditionally on past results but independently of 𝜒. The
database can depend on 𝜒, but only at(𝑑0,𝑒 0), since world0
skips the impression saves on that device-epoch at Line 13.
The state can also depend on𝜒, albeit in a limited fashion,
since we have:
∀𝑥′∈𝐷 (0)∩𝐷(1),(F 𝑘,(0) 𝑒,𝑡 )𝑥′ =(F 𝑘,(1) 𝑒,𝑡 )𝑥′ (76)
Indeed, Alg. 5 shows that the budget spent for 𝑥′ at
each step only depends on past queries, which are identical
in both worlds once we condition on 𝑣 <𝑘 ≤𝑒,<𝑡 , and on the
record𝑥′ itself, which is identical in both worlds. This is
thanks to device-epoch level accounting in Def. B.15, B.14.
The same holds for domain caps K𝑑′,𝑒′[𝑢]: even though
GenerateReport iterates over the whole window 𝐸, each
iteration reads and writes onlyK𝑑′,𝑒′[𝑢], decides from that
entry, and skips only that epoch if it hits the cap.
Let 𝜌𝑟(𝐷 ;F)=GenerateReport(𝐷,𝜌 𝑟,𝜆 ;F) denote the
filtered report returned by Alg. 5, which maintains the state
F. Then:
Pr[𝑉𝑘,(𝜒) 𝑒,𝑡 =𝑣 𝑘 𝑒,𝑡|𝑣 <𝑘 ≤𝑒,<𝑡]
=Pr
 ∑︁ 𝑟∈𝑅𝑘 𝑒,𝑡 𝜌𝑟(𝐷(𝜒) ;F (𝜒) 𝑒,𝑡,𝑟)+𝑋 𝑒,𝑡 =𝑣 𝑘 𝑒,𝑡  ,(77)
where𝑋𝑒,𝑡 is the Laplace noise added at time𝑒,𝑡.
We omit the𝑒,𝑡,𝑘 indices when they are clear from context.
We denote by 𝐷 the database generated conditionally on
𝑣 <𝑘 ≤𝑒,<𝑡 before adding the in-or-out record, giving: 𝐷(0) =
𝐷+𝑥 C and𝐷(1) =𝐷+𝑥 for𝑒≥𝑒 0 (and𝐷(0) =𝐷 (1) for
𝑒<𝑒 0). By Def. B.5, since𝐹𝐴⊆F imp and𝐹∩F conv∩F imp =∅ ,
we have:
𝜌𝑟(𝐷(0) ;F (0) 𝑟 )=𝜌 𝑟(𝐷+(𝑑 0,𝑒 0,𝐹∩F conv∩𝐹𝐴))
=𝜌 𝑟(𝐷;F (0) 𝑟 )
By Alg. 5, remark that the state(F(0) 𝑟 )𝑥′ for𝑥′∈{𝑥,𝑥 C}
has no impact on the output: replacing the corresponding
data by∅ at Line 17 (when hitting a per-action domain cap)
or Line 28 (when running out of budget or quota) is a no-op.
Combining this observation with Eq. 76 gives:
𝜌𝑟(𝐷(0) ;F (0) 𝑟 )=𝜌 𝑟(𝐷;F (1) 𝑟 )(78)
We can now bound the privacy loss at step𝑒,𝑡,𝑘:

ln  Pr[𝑉𝑘,(0) 𝑒,𝑡 =𝑣 𝑘 𝑒,𝑡|𝑣 <𝑘 ≤𝑒,<𝑡] Pr[𝑉𝑘,(1) 𝑒,𝑡 =𝑣 𝑘 𝑒,𝑡|𝑣 <𝑘 ≤𝑒,<𝑡] !

 (79)
≤

 ln '›› « Pr h˝ 𝑟∈𝑅𝑘 𝑒,𝑡 𝜌𝑟(𝐷;F (1) 𝑟 )+𝑋 𝑒,𝑡 =𝑣 𝑘 𝑒,𝑡 i Pr h˝ 𝑟∈𝑅𝑘 𝑒,𝑡 𝜌𝑟(𝐷+𝑥;F (1) 𝑟 )+𝑋 𝑒,𝑡 =𝑣 𝑘 𝑒,𝑡 i “ﬁﬁ ‹

 (80)
We now omitF(1) 𝑟 since it is present on both sides. Take
𝑟∈𝑅 𝑡. We define the boolean pass𝑟 by pass𝑟 = 0if 𝐹𝑒 is ze-

roed out (either by the domain cap at Line 17 or by the atomic
check at Line 28), in the world where𝑥 is present. Ifpass𝑟 = 0,
we have𝜌𝑟(𝐷+𝑥)=𝜌 𝑟(𝐷) because of Alg. 5, Line 28. Other-
wise, if pass𝑟 =1, we have ∥𝜌𝑟(𝐷+𝑥)−𝜌 𝑟(𝐷)∥1≤Δ 𝑥(𝜌𝑟).
Hence,
∥𝜌𝑟(𝐷)−𝜌 𝑟(𝐷+𝑥)∥≤Δ 𝑥(𝜌𝑟)pass𝑟 (81)
Thus by triangle inequality followed by Def. B.15 we have:
∥
∑︁
𝑟∈𝑅𝑡
𝜌𝑟(𝐷)−
∑︁
𝑟∈𝑅𝑡
𝜌𝑟(𝐷+𝑥)∥≤
∑︁
𝑟∈𝑅𝑡
Δ𝑥(𝜌𝑟)pass𝑟 (82)
≤
∑︁
𝑟∈𝑅𝑡
𝜆𝑘 𝑡·𝜖𝑟 pass𝑟 (83)
And since𝑋𝑡∼Lap(𝜆 𝑘 𝑡), by property of the Laplace dis-
tribution Eq. 80 becomes:

ln  Pr[𝑉𝑘,(0) 𝑒,𝑡 =𝑣 𝑘 𝑒,𝑡|𝑣 <𝑘 ≤𝑒,<𝑡] Pr[𝑉𝑘,(1) 𝑒,𝑡 =𝑣 𝑘 𝑒,𝑡|𝑣 <𝑘 ≤𝑒,<𝑡] !

≤ ∑︁ 𝑟∈𝑅𝑡 𝜖𝑟 pass𝑟 (84)
We can now bound the total privacy loss. First, we use
Eq. 72 and the fact that the outputs𝑣𝑘 𝑒,0 at Line 22 are identical
across both worlds by definition of𝑥C to drop indices where
𝑡=0:

ln  Pr[𝑉(0) =𝑣] Pr[𝑉(1) =𝑣] 

 (85)
=

ln  𝑒maxÖ 𝑒=1 𝑡maxÖ 𝑡=0 𝐾Ö 𝑘=1 Pr[𝑉𝑘,(0) 𝑒,𝑡 =𝑣 𝑘 𝑒,𝑡|𝑣 <𝑘 ≤𝑒,<𝑡] Pr[𝑉𝑘,(1) 𝑒,𝑡 =𝑣 𝑘 𝑒,𝑡|𝑣 <𝑘 ≤𝑒,<𝑡] !

 (86)
=

 𝑒max∑︁ 𝑒=1 𝑡max∑︁ 𝑡=1 𝐾∑︁ 𝑘=1 ln  Pr[𝑉𝑘,(0) 𝑒,𝑡 =𝑣 𝑘 𝑒,𝑡|𝑣 <𝑘 ≤𝑒,<𝑡] Pr[𝑉𝑘,(1) 𝑒,𝑡 =𝑣 𝑘 𝑒,𝑡|𝑣 <𝑘 ≤𝑒,<𝑡] !

 (87)
By triangle inequality and Eq. 84, we get:

ln  Pr[𝑉(0) =𝑣] Pr[𝑉(1) =𝑣] 

 (88)
≤
𝑒max∑︁
𝑒=1
𝑡max∑︁
𝑡=1
𝐾∑︁
𝑘=1
∑︁
𝑟∈𝑅𝑡
𝜖𝑟 pass𝑟 (89)
Finally, each𝜖𝑟 pass𝑟 is an amount granted byF global 𝑑0,𝑒0 , so its capacity invariant Eq. 69 gives:
𝑒max∑︁
𝑒=1
𝑡max∑︁
𝑡=1
𝐾∑︁
𝑘=1
∑︁
𝑟∈𝑅𝑡
𝜖𝑟 pass𝑟≤𝜖 global (90)
Hence we have shown Eq. 71.□
B.4 DoS Resilience
This section proves our main resilience result for Big Bird’s
quota-based online algorithm: Thm. 4.1. First, Lem. B.19
shows that the 2-PC check (Alg. 6) ensures (1) atomic con-
sumption across all filters relevant to a query, and (2) when
all filters have sufficient budget, each consumes an amount
proportional to its level-specific sensitivity either at epoch
or at epoch-site level. Next, Lem. B.21 and B.23 bound the
total privacy budget the adversary can consume from the
global budget at any device-epoch, using the atomic con-
sumption guarantees of Lem. B.19. These first two lemmas
give Thm. 4.1(i). Lem. B.24 then connects user actions to ob-
tain Thm. 4.1(ii), and Lem. B.25 lifts the bound to the query
level for Thm. 4.1(iii).
B.4.1 Preliminaries.
Notation.Everything in this section (§B.4) is stated inside
one fixed execution of Alg. 7. Let 𝑠max :=𝑒 max𝑡max𝐾. We
index the queries from Alg. 7 by𝑠∈[𝑠 max] instead of triples
(𝑒,𝑡,𝑘) , so each execution of AnswerQuery is associated
with a unique𝑠, with corresponding report identifiers𝑅𝑠 and
querier𝑏𝑠.
For a device-epoch𝑥=(𝑑,𝑒,𝐹) , a query𝑠 and𝑟∈𝑅 𝑠 we
write𝑐𝑟 for the conversion site of𝑟,i𝑟,𝑒 =ImpSites(𝐹∩𝐹 𝐴𝑟)
for its effective impression sites (i.e.,𝐼𝑟(𝑥) from Thm. B.12),
𝜖𝑟,𝑠 and𝜖𝑖 𝑟,𝑠 (for𝑖∈ i𝑟,𝑒 ) for the losses computed at Line 22
and Line 25, and pass𝑟,𝑠 ∈ {0, 1} for the indicator that
GenerateReport zeroes 𝐹𝑒 at neither Line 17 nor Line 28.
Each of𝜖𝑟,𝑠 and𝜖𝑖 𝑟,𝑠 is0when Alg. 5 does not compute it at
𝑥. When the report index is clear from context, we drop 𝑟
and write𝑐𝑠,i𝑠,𝜖 𝑖 𝑠 and pass𝑠.
Lemma B.19(Atomic filter check guarantees).Fix a device-
epoch record𝑥=(𝑑,𝑒,𝐹) , a query𝑠 and𝑟∈𝑅 𝑠 , with querier
𝑏=𝑏 𝑠 . Using the definition of pass𝑟,𝑠 and Alg. 6, we have:
(a)F querier[𝑏] 𝑑,𝑒 ,F global 𝑑,𝑒 andF conv-quota[𝑐𝑟] 𝑑,𝑒 each grant ex-
actly𝜖𝑟,𝑠 pass𝑟,𝑠 ;
(b) for each𝑖∈i 𝑟,𝑒 ,F imp-quota[𝑖] 𝑑,𝑒 grants exactly𝜖 𝑖 𝑟,𝑠 pass𝑟,𝑠 .
Proof. We prove both properties together. Fix𝑟∈𝑅 𝑠 with
pass𝑟,𝑠 = 1. By Alg. 6, the atomic check returnsTRUE exactly
when all Phase 1 checks pass and all Phase 2 operations
execute. For this report, with conversion site𝑐𝑟 , querier𝑏𝑠,
and impression sitesi𝑟,𝑒 , Phase 2 calls:
•F querier[𝑏𝑠] 𝑥 .tryConsume(𝜖 𝑟,𝑠)
•F global 𝑥 .tryConsume(𝜖 𝑟,𝑠)
•F conv-quota[𝑐𝑟] 𝑥 .tryConsume(𝜖 𝑟,𝑠)
•For each𝑖∈i 𝑟,𝑒 :F imp-quota[𝑖] 𝑥 .tryConsume(𝜖 𝑖 𝑟,𝑠)
Note that𝜖𝑟,𝑠 is the device-epoch-level individual privacy loss
computed for this specific report𝑟 (e.g.,, via EpochBudget in
Line 22 of Alg. 5). Similarly, each𝜖𝑖 𝑟,𝑠 is the device-epoch-site-
level individual privacy loss for impression site𝑖 relevant to
this report𝑟 (via EpochImpSiteBudget in Alg. 5). Therefore,
when pass𝑟,𝑠 = 1, the conversion-site quota filter (for 𝑐𝑟 ),
the per-site filter (for𝑏𝑠), and the global budget all consume
exactly the same amount𝜖𝑟,𝑠 . Concurrently, each relevant
impression-site quota filter (for𝑖∈ i𝑟,𝑒 ) consumes its specific
amount𝜖𝑖 𝑟,𝑠 , which is proportional to its sensitivity at the
epoch-impression-site level for this report𝑟.□
B.4.2 Number of sites.With these atomic guarantees we
can bound how much of the global budget can be depleted

at any device-epoch𝑥∈X . The main isolation result is in
Thm. 4.1, which uses Lem. B.21, B.22 and B.23.
Definition B.20(Budget consumed and quotas charged).
Fix a device-epoch𝑥=(𝑑,𝑒,𝐹) , andanyset of reports R𝑠⊆
𝑅𝑠 for each query𝑠∈[𝑠 max].
LetR+ :={(𝑠,𝑟) : 𝑠∈[𝑠 max], 𝑟∈R 𝑠,pass 𝑟,𝑠 = 1} the
reports that pass the filters. Then, we define:
𝜖global(R):=
∑︁
(𝑠,𝑟)∈R +
𝜖𝑟,𝑠,(91)
𝐶(R):=
Ø
(𝑠,𝑟)∈R +
{𝑐𝑟},
𝑁(R):=|𝐶(R)|,
𝐼(R):=
Ø
(𝑠,𝑟)∈R +
i𝑟,𝑒,
𝑀(R):=|𝐼(R)|.(92)
Def. B.20 defines what a group of report consumes. When
reports are associated with an attacker, this defines the im-
pact of the attacker, but the definition itself does not involved
any notion of attacker. By Lem. B.19, reports R consume
𝜖global(R) fromF global 𝑑,𝑒 , and they charge the domains𝐶(R)
and𝐼(R) . In the lemmas below, we takeR to be the reports
an adversary elicits and note: Radv =(𝑅 adv 𝑠 )𝑠∈[𝑠 max] with
𝑅adv 𝑠 ⊆𝑅 𝑠, writing𝜖adv global :=𝜖 global(R adv) and likewiseR+ adv,
𝐶adv,𝑁 adv,𝐼adv,𝑀 adv. Note that𝐼adv contains every impres-
sion site charged by an attacker-elicited report, even honest
impression sites that happen to allow malicious conversion
sites to query their impressions. This corresponds to the
threat model from §4.1, where 𝐼adv∪𝐶 adv is the set of do-
mains directly controlled by, or transitively partnering with
the attacker.
Lemma B.21(Conversion-site quotas bound).Fix a device-
epoch𝑥=(𝑑,𝑒,𝐹) and an adversary that elicits the reports
Radv. By Def. B.20, these charge 𝑁 adv distinctconv-quotafil-
ters and consume𝜖 adv global fromF global 𝑑,𝑒 .
Then, we have:
𝜖adv global≤𝑁 adv𝜖conv-quota.(93)
Proof.By definition of𝜖 adv global we have:
𝜖adv global = ∑︁
𝑠∈[𝑠 max]
∑︁
𝑟∈R 𝑠 :pass𝑟,𝑠 =1
𝜖𝑟,𝑠
=
∑︁
𝑠∈[𝑠 max]
∑︁
𝑟∈R 𝑠
𝜖𝑟,𝑠 pass𝑟,𝑠
Then we use the definition of𝐶adv to sum over all reports
𝑅𝑠 instead ofR 𝑠⊂𝑅 𝑠:
𝜖adv global≤ ∑︁
𝑐∈𝐶 adv
∑︁
𝑠∈[𝑠 max]
∑︁
𝑟∈𝑅𝑠
𝑐𝑟 =𝑐
𝜖𝑟,𝑠 pass𝑟,𝑠
≤
∑︁
𝑐∈𝐶 adv
𝜖conv-quota
where the last step comes from Lem. B.19(a): each𝑟 grants
𝜖𝑟,𝑠 pass𝑟,𝑠 toF global 𝑑,𝑒 and the same amount toF conv-quota[𝑐𝑟] 𝑑,𝑒 ,
followed by the capacity invariant Eq. 69.
The definition of𝑁 adv finally gives𝜖adv global≤𝑁 adv𝜖conv-quota.
□
Lemma B.22(Impression-site quota allocation consistency).
Fix a device-epoch 𝑥=(𝑑,𝑒,𝐹) , a query 𝑠 and a report𝑟∈𝑅 𝑠 ,
and take ˜Δ𝑥,𝑖(𝜌𝑟) as in Eq. 55 with2 Δ(𝜌𝑟) as an upper bound
forΔ𝑖(𝜌𝑟)(Lem. B.13). We have:
𝜖𝑟,𝑠≤
∑︁
𝑖∈i𝑟,𝑒
𝜖𝑖 𝑟,𝑠 (94)
Proof. Write𝜆 for the noise scale of query 𝑠, so that𝜖𝑟,𝑠 =
˜Δ𝑥(𝜌𝑟)/𝜆 and 𝜖𝑖 𝑟,𝑠 = ˜Δ𝑥,𝑖(𝜌𝑟)/𝜆 (Def. B.15, B.14). We go
through the different cases for the upper bound onΔ 𝑥(𝜌𝑟):
• If𝑑≠𝑑 𝑟 ,𝑒∉𝐸 𝑟 , or𝐹∩𝐹 𝐴𝑟 =∅ , then𝜖𝑟,𝑠 = 0. In that
case, by Thm. B.12 we also have𝜖𝑖 𝑟,𝑠 = 0for all 𝑖. This
covers in particulari𝑟,𝑒 =∅ , sincei𝑟,𝑒 =ImpSites(𝐹∩
𝐹𝐴𝑟).
•Otherwisei 𝑟,𝑒 ≠∅, and we fix any𝑖∈i 𝑟,𝑒 :
–If𝑑=𝑑 𝑟 and𝐸𝑟 ={𝑒}:
∗ Ifi 𝑟,𝑒 ={𝑖} , we have 𝜖𝑟,𝑠 =𝜖 𝑖 𝑟,𝑠 =∥𝐴 𝑟(𝐹)−
𝐴𝑟(∅)∥ 1/𝜆.
∗ Else, we have 𝜖𝑖 𝑟,𝑠 = 2Δ(𝜌𝑟)/𝜆≥ ∥𝐴 𝑟(𝐹)−
𝐴𝑟(∅)∥ 1/𝜆=𝜖 𝑟,𝑠 .
–Else, we have𝜖 𝑖 𝑟,𝑠 =2Δ(𝜌 𝑟)/𝜆≥Δ(𝜌 𝑟)/𝜆≥𝜖 𝑟,𝑠 .
In each case𝜖𝑟,𝑠≤𝜖 𝑖 𝑟,𝑠 , and the remaining terms of the
sum are non-negative.
□
Note that the upper bound in Lem. B.22 can be quite loose.
Since the impression-site quota has no privacy meaning and
is only used through Lem. B.22 to obtain isolation guarantees,
instead of using per-epoch-site privacy loss we could use
any heuristic that also satisfies Lem. B.22’s𝜖𝑟,𝑠≤ ˝ 𝑖∈i𝑟,𝑒𝜖𝑖 𝑟,𝑠 .
For instance, we could divide𝜖𝑟,𝑠 uniformly acrossi𝑟,𝑒 .
Lemma B.23(Impression-site quotas bound).Fix a device-
epoch𝑥=(𝑑,𝑒,𝐹) and an adversary that elicits the reports
Radv. By Def. B.20, these charge𝑀 adv distinctimp-quotafilters
and consume𝜖 adv global fromF global 𝑑,𝑒 .
Then, we have:
𝜖adv global≤𝑀 adv𝜖imp-quota.(95)
Proof. By definition of𝜖adv global, and then by Lem. B.22 applied
to each report, we have:

𝜖adv global = ∑︁
𝑠∈[𝑠 max]
∑︁
𝑟∈R 𝑠
𝜖𝑟,𝑠 pass𝑟,𝑠
≤
∑︁
𝑠∈[𝑠 max]
∑︁
𝑟∈R 𝑠
∑︁
𝑖∈i𝑟,𝑒
𝜖𝑖 𝑟,𝑠 pass𝑟,𝑠
Then we use the definition of𝐼adv, which containsi𝑟,𝑒 for
every report with pass𝑟,𝑠 = 1, to sum over all reports 𝑅𝑠
instead ofR 𝑠⊂𝑅 𝑠:
𝜖adv global≤ ∑︁
𝑖∈𝐼 adv
∑︁
𝑠∈[𝑠 max]
∑︁
𝑟∈𝑅𝑠
𝑖∈i𝑟,𝑒
𝜖𝑖 𝑟,𝑠 pass𝑟,𝑠
≤
∑︁
𝑖∈𝐼 adv
𝜖imp-quota
where the last step comes from Lem. B.19(b): each𝑟 grants
𝜖𝑖 𝑟,𝑠 pass𝑟,𝑠 toF imp-quota[𝑖] 𝑑,𝑒 for each𝑖∈ i𝑟,𝑒 , followed by the
capacity invariant Eq. 69.
The definition of𝑀 adv finally gives𝜖adv global≤𝑀 adv𝜖imp-quota.
□
We can now combine Lem. B.21 and B.23 to obtain our
main isolation theorem:
Theorem 4.1(i) (Resilience to DoS depletion).Fix a
device-epoch𝑥=(𝑑,𝑒,𝐹) and an adversary that elicits the re-
portsRadv. By Def. B.20, these charge 𝑀 adv distinctimp-quota
filters and𝑁 adv distinctconv-quotafilters.
Then, the adversary’s consumption 𝜖adv global fromF global 𝑑,𝑒 sat-
isfies:
𝜖adv global≤min(𝑀 adv𝜖imp-quota, 𝑁adv𝜖conv-quota).(96)
Proof. The conversion-side bound is Lem. B.21 and the
impression-side bound is Lem. B.23, and we take their
minimum.□
B.4.3 Number of user actions.We now bound the num-
ber of sites by the user actions that resulted in quota deduc-
tions.
Lemma B.24(Quotas per user action).Fix a device-epoch
𝑥=(𝑑,𝑒,𝐹) and an adversary that elicits the reports Radv.
Separate the actions that carry their conversions from those
that saved the impressions they read at𝑥:
Uadv conv :={𝑢𝑟 :(𝑠,𝑟)∈R + adv},
Uadv imp := Ø
(𝑠,𝑟)∈R + adv
ImpActions(𝐹∩𝐹 𝐴𝑟).
Write 𝑈 adv conv :=|U adv conv|, 𝑈 adv imp :=|U adv imp|, and 𝑈 adv :=
|U adv conv∪U adv imp|. Then,
𝑁 adv≤𝜅 action𝑈 adv conv,(97)
𝑀 adv≤𝜅 action𝑈 adv imp,(98)
𝑁 adv,𝑀 adv≤𝜅 action𝑈 adv.(99)
Proof. For any𝑐∈𝐶 adv, some(𝑠,𝑟)∈R + adv has𝑐𝑟 =𝑐 , so the
GenerateReport path for that measureConversion request
passedF𝑑,𝑒.K[𝑢𝑟].canAdmit(𝑐) . Hence𝑐∈K 𝑑,𝑒[𝑢𝑟] with
𝑢𝑟∈U adv conv.
Similarly, for any𝑖∈𝐼 adv, there is𝑟 such that𝑖∈ i𝑟,𝑒 =
ImpSites(𝐹∩𝐹 𝐴𝑟). Hence𝐹∩𝐹 𝐴𝑟 contains an impression
(𝑢,𝑖,imp) with𝑢∈ImpActions(𝐹∩𝐹 𝐴𝑟)⊆U adv imp. That event
was stored by an accepted SaveImpression, which passed
F𝑑,𝑒.K[𝑢].canAdmit(𝑖), so𝑖∈K 𝑑,𝑒[𝑢].
Finally, each cap contains at most𝜅action domains (Def. B.17).
Hence the first bound (Eq. 97) comes from 𝐶adv with the
caps indexed byUadv conv, and the second bound (Eq. 98) comes
from𝐼 adv with the caps indexed byU adv imp.
The third bound (Eq. 99) takes the union.□
We now prove the main graceful degradation theorem,
which bounds the adversary’s budget consumption as a func-
tion of the number of user actions they can elicit.
Theorem 4.1(ii) (Graceful degradation).Consider an at-
tacker collecting 𝑈 adv user actions across their domains for
device𝑑. Under the configuration of Table 2, the budget 𝜖adv global
that this attacker can consume from theglobal budgetis upper-
bounded by:
𝜖adv global≤(1+𝑟)𝜖 querier×𝜅 action×𝑈 adv.(100)
Proof. By Lem. B.24, and using the configuration from Ta-
ble 2, where 𝜖imp-quota =𝑛( 1+𝑟)𝜖 querier and 𝜖conv-quota =
(1+𝑟)𝜖 querier,
𝑀 adv𝜖imp-quota≤𝑛(1+𝑟)𝜖 querier×𝜅 action×𝑈 adv
𝑁 adv𝜖conv-quota≤(1+𝑟)𝜖 querier×𝜅 action×𝑈 adv.
The limiting factor is𝑁 adv𝜖conv-quota, and applying part (i)
of Thm. 4.1 yields the result.□
Note that under the additional assumption that no domain
both saves an impression and measures a conversion un-
der the same user action, each charged quota filter would
occupy a distinct domain cap slot, giving 𝑀 adv+𝑁 adv ≤
𝜅action𝑈 adv. Part (i) of Thm. 4.1 would then give𝜖adv global≤( 1+
𝑟)𝜖 querier min(𝑛𝑀 adv,𝑁 adv) ≤ 𝑛 𝑛+1(1+𝑟)𝜖 querier𝜅action𝑈 adv.
We do not make this assumption, and Thm. 4.1(ii) uses the
weaker bound above.
B.4.4 Number of devices.
Lemma B.25(Query error from depleted device-epochs).
Take a database𝐷 with filter stateF , and let ˜F be obtained
fromF by depleting 𝜖global at𝑘 distinct device-epochs. Let
𝑄= ˝ 𝑟∈𝑅 𝜌𝑟 be a query in which Δ(𝜌𝑟)≤Δ for every𝑟 , and
at most𝑚reports belong to any one device. Then
∥𝑄(𝐷;F)−𝑄(𝐷; ˜F)∥ 1≤𝑚·𝑘·Δ.
Proof. Take a query 𝑄 : 𝐷↦→ ˝ 𝑟∈𝑅 𝜌𝑟(𝐷) as defined in
Def. B.7. Take a database𝐷 and filter statesF, ˜F where ˜F

is obtained fromF by depleting𝜖global for𝑘 distinct device-
epochs. For a report𝜌𝑟 , we denote by𝜌𝑟(𝐷 ;F) the filtered
report returned by GenerateReport in Alg. 5. Similarly, we de-
note by𝑄(𝐷 ;F) := ˝ 𝑟∈𝑅 𝜌𝑟(𝐷 ;F) the filtered query before
adding noise.
Consider a single report identifier 𝑟∈𝑅 , with attri-
bution function 𝐴𝑟 over 𝑛𝑟 :=|𝐸 𝑟| epochs. We have
𝜌𝑟(𝐷 ;F)=𝐴 𝑟(𝐹 1,...,𝐹 𝑛𝑟) where 𝐹1,...,𝐹 𝑛𝑟 are the rel-
evant events from𝐷 after passing the filter check based on
F in Alg. 5. Now, without loss of generality, suppose that
the first𝑘𝑟 epochs for that report are depleted in ˜F . This
causes the filter check to fail for these epochs, returning:
𝜌𝑟(𝐷; ˜F)=𝐴 𝑟(∅,...,∅,𝐹 𝑘𝑟+1,...,𝐹 𝑛𝑟).
For 𝑗∈{ 0,...,𝑘 𝑟}, writeF (𝑗) :=(∅,...,∅,𝐹 𝑗+1,...,𝐹 𝑛𝑟)
for the input with the first 𝑗 epochs zeroed out, so that
𝜌𝑟(𝐷 ;F)=𝐴 𝑟(F(0)) and 𝜌𝑟(𝐷 ; ˜F)=𝐴 𝑟(F(𝑘𝑟)). Consec-
utive inputsF(𝑗−1) andF(𝑗) differ in a single epoch, so by
definition of global sensitivity (Def. B.8) each step is bounded
by Δ(𝜌𝑟)≤Δ . After telescoping over the𝑘𝑟 depleted epochs
and applying the triangle inequality we get:
∥𝜌𝑟(𝐷;F)−𝜌 𝑟(𝐷; ˜F)∥ 1 =
 𝑘𝑟∑︁
𝑗=1
𝐴𝑟(F(𝑗−1))−𝐴 𝑟(F(𝑗))  1
≤
𝑘𝑟∑︁
𝑗=1
∥𝐴𝑟(F(𝑗−1))−𝐴 𝑟(F(𝑗))∥ 1
≤𝑘𝑟·Δ
Putting this together, we get:
∥𝑄(𝐷;F)−𝑄(𝐷; ˜F)∥ 1 =
 ∑︁
𝑟∈𝑅
𝜌𝑟(𝐷;F)−𝜌 𝑟(𝐷; ˜F)

1
≤
∑︁
𝑟∈𝑅
∥𝜌𝑟(𝐷;F)−𝜌 𝑟(𝐷; ˜F)∥ 1
≤
∑︁
𝑟∈𝑅
𝑘𝑟·Δ
≤𝑚·𝑘·Δ
where ˝ 𝑟∈𝑅 𝑘𝑟≤𝑚·𝑘 : each report reads depleted epochs
only on its own device, so each of the 𝑘 depleted device-
epochs is counted by at most the𝑚 reports belonging to that
device.□
Theorem 4.1(iii) (Bounded query impact).Consider the
setting of Lemma B.25 with an attacker collecting 𝑈 adv user
actions across their domains for device 𝑑, whose own reports
deplete theglobal budgetat each of the 𝑘 device-epochs. Under
the configuration of Table 2, the error induced by the attacker
is bounded by:
∥𝑄(𝐷;F)−𝑄(𝐷; ˜F)∥ 1≤𝑚·𝑘·Δ,
where
𝑘≤𝑈 adv/⌈ 𝜖global
𝑛(1+𝑟)𝜖 querier·𝜅 action
⌉.
Proof.Lemma B.25 covers the first statement.
Denote by 𝑋dep the𝑘 depleted device-epochs, and take
𝑥∈𝑋 dep, writing𝑀 adv 𝑥 and𝑈 adv imp(𝑥) for the corresponding
quantities at 𝑥. The attacker’s own reports consume the
whole capacity ofF global 𝑥 , so𝜖adv global =𝜖 global at𝑥. By Lem. B.23
and Eq. 98, and using the configuration from Table 2 where
𝜖imp-quota =𝑛(1+𝑟)𝜖 querier:
𝜖global≤𝑀 adv 𝑥 𝜖imp-quota≤𝑛(1+𝑟)𝜖 querier×𝜅 action×𝑈 adv imp(𝑥).
Rearranging gives 𝑈 adv imp(𝑥) ≥ 𝜖global 𝑛(1+𝑟)𝜖 querier·𝜅action , and
𝑈 adv imp(𝑥) is an integer, so we can round the right-hand
side up. By Def. B.1, all the impressions of one action on𝑑
belong to a single device-epoch. The device-epochs of𝑋dep
therefore draw disjoint sets of actions from the𝑈 adv actions
collected on𝑑:
𝑈 adv≥ ∑︁
𝑥∈𝑋 dep
𝑈 adv imp(𝑥)≥𝑘
 𝜖global
𝑛(1+𝑟)𝜖 querier·𝜅 action

,
which gives the bound on𝑘.□
B.5 Simplified model (for educational purposes)
Alg. 8 shows a simplified version of the full Big Bird sys-
tem model that we analyze formally, but one in line with
the generic model from §3.1. The purpose of including this
simplified version is educational: it provides easy-to-read un-
derstanding of how one can represent key aspects of system
behavior in modeling.
First, the budgets’ IDP semantics are visible in the 𝑥∈
X subscript at Line 7, where 𝑥 corresponds to a device-
epoch. This indicates that the filters are each maintained
on each device and for each epoch. Second, privacy loss
is computed at a finer granularity (Line 21) for imp-quota
than for the other budgets. Third, Big Bird uses a shared
limit (L in §3) consisting of a collection of privacy bud-
gets and quota budgets, denotedF . At Line 22,(F global 𝑥 ◦
···◦F imp-quota 𝑥 [𝑖])(𝜖𝑥,𝜖𝑖 𝑥) denotes the atomic check and
consumption of budgets performed for each record (device-
epoch). For comparison,F global 𝑥 (𝜖𝑥)∧···∧F imp-quota 𝑥 [𝑖](𝜖𝑖 𝑥)
would check budgets independently, potentially spending
from one but not the other, which harms utility. We show
that this atomicity, never previously studied, preserves global
IDP.
C Examples of Cap Interactions with
Device-Epoch IDP
To illustrate how easy it is for seemingly reasonable DoS
caps to violate device-epoch IDP, we present a natural but in-
correct instantiation of “capping global-budget consumption
per user action, ” followed by its corrected form.

Alg. 8Simplified version of Big Bird formal model.
1:Input
2:Challenge bit𝜒∈{0,1}
3:In-or-out record𝑥 0 to be inserted at time𝑡 0
4:Public informationC
5:Data generation processG
6:QueriersQ 1,...,Q 𝐾
7: IDP budgets for each𝑥∈X :F global 𝑥 ,(F querier 𝑥 [𝑘])𝑘∈[𝐾] ,
(F conv-quota 𝑥 [𝑐])𝑐∈[S] ,(F imp-quota 𝑥 [𝑖])𝑖∈[S]
8:for𝑡∈[𝑡 max]do
//Data generation model:
9:𝐷 𝑡←G(𝑉 1 <𝑡,...𝑉 𝐾 <𝑡)//new data depends onallpast results
10:if𝑡=𝑡 0 then
//On challenge, insert in-or-out record...
11:if𝜒=0then
12:𝐷 𝑡←𝐷 𝑡+𝑥 0∩C//...with public events only
13:else
14:𝐷 𝑡←𝐷 𝑡+𝑥 0 //...with public and private events
//Query execution model:
15:for𝑘∈[𝐾]do
16:𝑞 𝑘 𝑡←Q 𝑘(𝑉𝑘 <𝑡)//Abstract query over whole database
17:𝑆 𝑘 𝑡 ←𝐷
18:for𝑥∈𝐷do
//Compute device-epoch loss and device-epoch-impSite loss (for
imp-quota)
19:𝜖 𝑥←EpochBudget(𝑥,𝑞 𝑘 𝑡)
20:for𝑖∈ido
21:𝜖 𝑖 𝑥←EpochImpSiteBudget(𝑥,𝑖,𝑞 𝑘 𝑡)
//Atomic transaction across all budgets
22: if (F global 𝑥 ◦ Fquerier 𝑥 [𝑘] ◦ Fconv-quota 𝑥 [𝑐] ◦
F imp-quota 𝑥 [i])(𝜖𝑥,𝜖 i 𝑥)then
23:𝑆 𝑘 𝑡 ←𝑆 𝑘 𝑡\{𝑥}//Drop out-of-budget record
24:𝑉 𝑘 𝑡 ←𝑞𝑘 𝑡(𝑆𝑘 𝑡)
25:return𝑉 1,...,𝑉 𝐾
Faulty instantiation.Alg. 9 tries to cap the total
privacy consumption generated by all reports within a
single user-action context. A natural approach would be
to cap thecumulativeprivacy lossacross all epochsac-
cessed by reports following that user action. The algorithm
does exactly this by maintaining a single accumulator,
consumedPrivacy[uaCtx], that aggregates privacy
loss over every epoch touched by any report in that uaCtx.
If, during the execution of a report, this cumulative loss
would exceed the cap𝜖action, the algorithm halts and returns
a null report, AttributionFn(∅,...,∅).
While intuitive, this design inadvertently couples epochs:
whether data from epoch 𝑒 is included in the report now
depends on privacy consumption inotherepochs accessed
earlier in the same uaCtx. This violates device-epoch IDP,
which requires that privacy loss in epoch𝑒depend only on
that epoch’s data. In effect, a querier’s interactions in epoch
Alg. 9Non-IDP capping of budget consumption per user
action
defonUserAction( )
uaCtx = createUserContext()
consumedPrivacy[uaCtx]←0
returnuaCtx
defmeasureConversion(uaCtx, impSites, querier, convSite, params)
for𝑒∈params.attributionWindowdo
𝐼𝑒←MatchingFn(ImpressionStore[e], params)
//Compute IDP loss w/ Cookie Monster algo.
𝜖𝑒←computeEpochLoss(𝐼𝑒, params)
//Ensure that total privacy consumed in this user-action context across
//all epochs stays within the cap. If it exceeds, stop execution and return
//a null report.
ifconsumedPrivacy[uaCtx]+𝜖 𝑒 >𝜖𝑎𝑐𝑡𝑖𝑜𝑛 then
returnAttributionFn(∅,...,∅)//cap exceeded, return null report
consumedPrivacy[uaCtx]+=𝜖 𝑒
//Then deduct from per-epoch global budgets and per-querier budgets.
tx = beginTransaction()
ifquerierBudget[e][querier].tryConsume(𝜖𝑒, tx)and
globalBudget[e].tryConsume(𝜖𝑒, tx)then
tx.commit()
else
tx.abort()
𝐼𝑒←∅
//Generate attribution histogram from remaining impressions
returnAttributionFn(𝐼 𝑒1,...,𝐼 𝑒𝑤)//𝑒 𝑖∈params.attributionWindow
𝑒1 can suppress contributions from epoch𝑒2, which means
that privacy loss accounted for𝑒2 now depends on data in
𝑒1, violating IDP.
Correct instantiation.Alg. 10 restores IDP soundness
for this candidate approach by isolating capsper epoch. Each
user-action context maintains a separate tracker for every
epoch:
consumedPrivacy[uaCtx][e].
When epoch𝑒’s loss in this uaCtx exceeds𝜖action, only that
epoch’s contribution is nullified; all other epochs proceed
independently. This preserves the required per-epoch sepa-
rability: the decision to include or exclude epoch𝑒 depends
solely on that epoch’s data and budgets, not on privacy loss
incurred elsewhere. This same principle underlies Big Bird’s
per-action domain cap design (Alg. 2), where checks are
carefully partitioned per epoch and user-action contexts
never span epoch boundaries. Together, these mechanisms
ensure that resilience mechanisms do not inadvertently break
device-epoch IDP.
D Cross-report Privacy Loss Optimization
In §B, we presented a general algorithm where queriers
pay for each report separately. It is common for conver-
sion sites to embed multiple intermediaries and to perform
attribution once across impressions displayed by all inter-
mediaries. When multiple reports for the same conversion
involve disjoint impression sets (e.g.,across intermediaries),

Alg. 10Correct, IDP-respecting capping of budget consumption
per user action
defonUserAction( )
uaCtx = createUserContext()
consumedPrivacy[uaCtx][𝑒]←0for each epoch𝑒
returnuaCtx
defmeasureConversion(uaCtx, impSites, querier, convSite, params)
for𝑒∈params.attributionWindowdo
𝐼𝑒←MatchingFn(ImpressionStore[e], params)
//Compute IDP loss w/ Cookie Monster algo.
𝜖𝑒←computeEpochLoss(𝐼𝑒, params)
//Ensure that privacy consumed per epoch in this user-action context
//stays within the cap. If it exceeds, eliminate the epoch’s data from
//consideration for this report.
ifconsumedPrivacy[uaCtx][e]+𝜖 𝑒 >𝜖𝑎𝑐𝑡𝑖𝑜𝑛 then
𝐼𝑒←∅//nullify contribution of this epoch to the report
consumedPrivacy[uaCtx][e]+=𝜖 𝑒
//Then deduct from per-epoch global budgets and per-querier budgets.
tx = beginTransaction()
ifquerierBudget[e][querier].tryConsume(𝜖𝑒, tx)and
globalBudget[e].tryConsume(𝜖𝑒, tx)then
tx.commit()
else
tx.abort()
𝐼𝑒←∅
//Generate attribution histogram from remaining impressions
returnAttributionFn(𝐼 𝑒1,...,𝐼 𝑒𝑤)//𝑒 𝑖∈params.attributionWindow
defonEpochChange(uaCtx)
destroyUserContext(uaCtx)
we prove that one need not double-count against shared
budgets (global, conversion-site, and impression-site quotas).
Indeed, the combination of reports from different interme-
diaries reveals no more than a single attribution across in-
termediaries. We present the intuition first with an example
and then with detailed formalism and proofs.
D.1 Example
We modify the example in Fig. 4 and §4.3 as follows. Instead
of working with a single intermediary adtech.ex, shoes.ex
works with both adtech.ex and adtech2.ex. adtech.ex dis-
plays impressions on news.ex, and adtech2.ex on blog.ex.
Upon conversion, attribution is still computed across all rel-
evant impressions, spanning both intermediaries. For shoes
.ex’s own measurement queries, accounting is unchanged
since intermediaries operate on shoes.ex’s behalf and are
not queriers themselves. As before, adtech.ex can request
an additional report (j) measuring its own impressions for
placement optimization purposes. Here, adtech.ex receives
a report containing a histogram with attributed value 30 (for
the impression on news.ex). Additionally, adtech2.ex can
measure its own impressions and receive a report (k) con-
taining a histogram with attributed value 30. Naively, one
would expect a cumulative deduction of 0.9 from the global
budget (three reports). Yet, one can observe that the two
intermediary reports are shards of a single report with attrib-
uted value 60, because adtech.ex and adtech2.ex receive
disjoint bins of the histogram. Leveraging this observation,
we show that it is possible to deduct only 0.6 from the global
budget. The same optimization applies to shared quotas.
D.2 Problem Statement
The example in §D.1 admits a cross-report optimization,
which we formalize here. We define variations of Alg. 7
and Alg. 5 in §D.3. We focus on histogram reports, defined
in §D.4, and show that paying only once for a sequence of
properly correlated histogram reports still satisfies global
IDP guarantees in §D.5. We leave the generalization to other
queries for future work.
D.3 Algorithm
Overview.Alg. 11 updates the formalism from Alg. 7. Instead
of generating a report immediately upon conversion, the
first querier to request a report attached to a report identifier
𝑟 calls MeasureConversion to create a stateful attribution
object 𝛼𝑟 , which pays upfront for any valid sequence of
histogram reports over non-overlapping impressions.
MeasureConversion performs attribution using the pre-
specified attribution function𝑎 and the noise scale𝜆, which
give an upper bound on the total leakage of any sequence
of future reports applying𝑎 on disjoint sets of impressions.
All shared privacy loss is charged upfront and atomically at
MeasureConversion time, before any querier-specific inter-
action occurs. We run a modified two-phase commit protocol
to deduct budget from all shared filters (global and quota
filters), but not from querier-local filters, which are charged
separately. 2 Finally,𝛼𝑟 stores the attribution function 𝑎F
with corresponding impressionsF, the privacy parameters 𝜆,
and the support𝑆of impressions requested so far.
GetReport allows a querier to receive a report from 𝑟,
once the attribution object 𝛼𝑟 has been created.𝛼𝑟 is only
created once, and is reused every time a querier requests
a report from𝑟. GetReport checks that privacy parameters
match what was committed in the attribution object, and
that impressions are not queried twice. If these checks pass,
GetReport spends querier budget and computes the report
using the predefined attribution function𝑎 stored in𝛼𝑟 . We
update the support of impressions 𝑆←𝑆⊔𝑆 𝜌 in𝛼𝑟 each
time a new report𝜌requests impressions in𝑆 𝜌⊂I.
Subroutine.We define AtomicFilterCheckAndConsume2 as
in Alg. 6, except that querier filters are not part of the atomic
commit. That is, we do not take𝑏 as an input, and we delete
Line 6 and Line 16 from Alg. 6.
2The querier budget is left out of the 2PC because we don’t know ahead of
time which queriers will request a report, and we don’t want to block some
queriers if other queriers are out of budget.

Alg. 11Updated formalism for cross-report optimization
(diff with Alg. 7)
1://Collect, aggregate and noise reports to answer𝑄
2:defAnswerQuery(𝐷,𝑄,𝜆,𝑏)
3:(𝜌 𝑏 𝑟)𝑟∈𝑅 ←𝑄//Get report identifiers from𝑄
4:for𝑟∈𝑅do
5:if𝛼 𝑟 is not definedthen
6://Initialize attribution object
7:𝛼 𝑟←MeasureConversion(𝐷,𝜌 𝑏 𝑟,𝜆)
8:𝜌 𝑏 𝑟(𝐷),𝛼 𝑟←GetReport(𝛼 𝑟,𝜌𝑏 𝑟,𝜆,𝑏)
9:Sample𝑋∼L(𝜆)
10:return ˝ 𝑟∈𝑅 𝜌𝑏 𝑟(𝐷)+𝑋
D.4 Histogram reports definition and properties
The following definitions (Def. D.1 and D.2) are adapted from
[43, Thm. 18]. Histogram reports distribute a positive value
across impressions, map each impression to a bucket, and
then sum up the attributed value in each bucket. Lem. D.3
gives the global sensitivity of such histogram reports, which
is bounded by the maximum attributable value.
Definition D.1(Scalar attribution function).Fix a number
of epochs𝑘> 0. Ascalar attribution functionis a function
𝑎 :P(I)𝑘×I→R + that attributes a positive value𝑎F(𝑓)
to each impression𝑓∈I , depending on all the impressions
in𝑘epochsF∈P(I) 𝑘.
For a scalar attribution function𝑎, we define itsmaximum
attributable value𝑎 max as follows:
𝑎max :=max
F∈P(I) 𝑘
𝑘∑︁
𝑗=1
∑︁
𝑓∈F 𝑗
𝑎F(𝑓)(101)
Definition D.2(Histogram report).Consider a scalar attri-
bution function𝑎 :P(I)𝑘×I→R +, a support set of im-
pressions𝑆⊂I , an output dimension𝑚> 0, and a one-hot
encoding function𝐻 that maps each event𝑓 to one of𝑚 buck-
ets. That is,𝐻 :I→{ 0, 1}𝑚 such that∀𝑓∈I,||𝐻(𝑓)|| 1 = 1.
First, we define𝐴𝑎,𝑆,𝐻 :P(I) 𝑘→R𝑚 as follows:
𝐴(F)=
𝑘∑︁
𝑗=1
∑︁
𝑓∈F 𝑗
1[𝑓∈𝑆]𝑎 F(𝑓)·𝐻(𝑓)(102)
𝐴𝑎,𝑆,𝐻 is a well-defined attribution function (in the sense
of Def. B.5).
Second, for a device𝑑 and a set of epochs𝐸, we define the
histogram reportassociated with𝐴 𝑎,𝑆,𝐻 as in Def. B.6:
𝜌:𝐷↦→𝐴 𝑎,𝑆,𝐻(𝐷𝐸 𝑑)(103)
Next, Lem. D.3 and D.4 give two preliminary properties
of histogram reports that will be used in Thm. D.5.
Lemma D.3(Histogram sensitivity).Consider a histogram
Alg. 12Big Bird algorithm (on-device) with cross-report
optimization for histogram reports
1:Input
2: Filter and quota capacities 𝜖global, 𝜖querier, 𝜖imp-quota,
𝜖conv-quota
3:defMeasureConversion(𝐷,𝜌,𝜆,b)
4: Read𝜌 to get device𝑑, epoch𝐸, conversion site𝑐, im-
pression sitesi, histogram attribution function 𝐴𝑎𝜌,𝑆𝜌,𝐻𝜌
with scalar attribution function𝑎, support impressions
𝑆and histogram bin mapping𝐻.
5:for𝑒∈𝐸do
6:𝑥←(𝑑,𝑒,𝐷 𝑒 𝑑)
7:ifF 𝑥 is not definedthen
8:F 𝑥←InitializeFilters(𝜖 global,𝜖 querier,
𝜖imp-quota,𝜖 conv-quota)
9:𝜖 𝑥←2𝑎 max/𝜆
10:𝜖 i x←{𝑖: 2𝑎 max/𝜆,𝑖∈i}
11: if AtomicFilterCheckAndConsume2(F𝑥,𝑐, i,𝜖𝑥,𝜖 i x)=
FALSEthen
12:𝐹 𝑒←∅//Empty the epoch if any filter check fails
13:return𝛼=(𝑎 F,F,𝜆,∅)//Start with𝑆 𝛼 =∅
14:
15:defGetReport(𝛼,𝜌,𝜆)
16: Read𝛼 to get attribution function𝑎𝛼, impressionsF𝛼,
noise scale𝜆𝛼.
17: Read𝜌 to get device𝑑, querier𝑏, target epochs𝐸, his-
togram attribution function𝐴𝑎,𝑆,𝐻 with scalar attribu-
tion function𝑎, support impressions 𝑆 and histogram
bin mapping𝐻.
18:if𝑆∩𝑆 𝛼 ≠∅∨𝜆≠𝜆 𝛼∨𝑎𝜌 ≠𝑎 𝛼 then
19:𝜌←𝐴(∅,...,∅)//Null report if inconsistent with𝛼
20:return𝜌
21:for𝑒∈𝐸do
22:𝑥←(𝑑,𝑒,F 𝛼𝑒)
23:𝜖 𝑥←EpochBudget(𝑥,𝜌,𝜆)//Querier budget only
24:ifF querier[𝑏] 𝑥 .tryConsume(𝜖 𝑡 𝑥)=FALSEthen
25:𝐹 𝑒←∅
26:else
27:𝐹 𝑒←F 𝛼𝑒
28:𝛼←(𝑎 𝛼,F,𝜆,𝑆 𝛼⊔𝑆𝜌)//Update impression support
29:𝜌←𝐴 𝑎,𝑆,𝐻((𝐹𝑒)𝑒∈𝐸)//Clipped attribution report
30:return𝜌,𝛼
report𝜌 with associated attribution function 𝐴𝑎,𝑆,𝐻 . We have:
Δ(𝜌)≤2𝑎 max (104)
Proof. Take a report 𝜌 with scalar attribution function 𝑎,
device𝑑 and epochs𝐸. Consider two neighboring databases

𝐷,𝐷′ and denoteF:=𝐷 𝐸 𝑑 andF′ :=𝐷′𝐸 𝑑 . We have:
∥𝜌(𝐷)−𝜌(𝐷 ′)∥ 1 =∥𝐴 𝑎,𝑆,𝐻(F)−𝐴 𝑎,𝑆,𝐻(F′)∥ 1 (105)
=
 𝑘∑︁ 𝑗=1 ∑︁ 𝑓∈F 𝑗 𝑎F(𝑓)·𝐻(𝑓)− 𝑘∑︁ 𝑗=1 ∑︁ 𝑓∈F′ 𝑗 𝑎F′(𝑓)·𝐻(𝑓)  1 (106)
≤
𝑘∑︁
𝑗=1
∑︁
𝑓∈F 𝑗
𝑎F(𝑓)∥𝐻(𝑓)∥+
𝑘∑︁
𝑗=1
∑︁
𝑓∈F′ 𝑗
𝑎F′(𝑓)∥𝐻(𝑓)∥(107)
≤2𝑎 max (108)
Even though this bound holds even for non-neighboring
databases, [43, Thm. 18] provides mild conditions under
which the bound is tight.□
D.5 Privacy proof
Lemma D.4(Correlated histogram sensitivity).Fix a device-
epoch𝑥=(𝑑,𝑒,𝐹) and a database 𝐷. Fix a report identifier
𝑟∈Z corresponding to a histogram attribution object 𝛼𝑟 . Fix
a sequence of reports 𝜌1,...,𝜌 𝑛 that request a report from 𝑟 ,
ordered lexicographically by time and querier (𝑡,𝑏) . In partic-
ular, MeasureConversion is called for 𝜌1 and then reused for
subsequent reports. ˝𝑛 𝑖=1∥𝜌𝑖(𝐷)−𝜌 𝑖(𝐷+𝑥)∥/𝜆 𝑖 represents
the total contribution over reports computed from𝛼𝑟 , each with
its own requested noise scale 𝜆𝑖 . Denote by pass1 the output of
the 2PC for𝑥in Alg. 12.
We have:
𝑛∑︁
𝑖=1
∥𝜌𝑖(𝐷)−𝜌 𝑖(𝐷+𝑥)∥/𝜆 𝑖
≤pass 1·2𝑎 max/𝜆1 (109)
Proof. If pass1 = 0, then𝜌𝑖(𝐷)=𝜌 𝑖(𝐷+𝑥) because in both
cases the data for𝑥 is zeroed out (𝐹𝑒 =∅ at Line 12), which
completes the proof in this case.
Now, suppose that pass1 = 1. Take a report𝜌𝑖 with scalar
attribution function𝑎𝑖 and support impressions 𝑆𝑖. These
only depend on past results𝑣<𝑡𝑖,𝑏𝑖 . If𝑆𝑖∩(𝑆 1∪···∪𝑆 𝑖−1)≠∅ ,
𝜆𝑖 ≠𝜆 1 or𝑎𝑖 ≠𝑎 1, then 𝜌𝑖(𝐷)=𝐴(∅,...,∅)=𝜌 𝑖(𝐷+𝑥) .
Also, if𝑥=(𝑑,𝑒,𝐹) is not queried by 𝜌𝑖 (𝑑≠𝑑 𝑖 or𝑒∉𝐸 𝑖),
then𝜌 𝑖(𝐷)=𝜌 𝑖(𝐷+𝑥).
Denote by𝐼 the set of remaining reports satisfying𝑆𝑖∩
(𝑆1⊔···⊔𝑆 𝑖−1)=∅ ,𝜆𝑖 =𝜆 1,𝑎𝑖 =𝑎 1,𝑑𝑖 =𝑑 , and𝑒∈𝐸 𝑖. We
have:
𝑛∑︁
𝑖=1
∥𝜌𝑖(𝐷)−𝜌 𝑖(𝐷+𝑥)∥/𝜆 𝑖 (110)
=
∑︁
𝑖∈𝐼
∥𝜌𝑖(𝐷)−𝜌 𝑖(𝐷+𝑥)∥/𝜆 1 (111)
=
∑︁
𝑖∈𝐼
∥
𝑘∑︁
𝑗=1
∑︁
𝑓∈F 𝑗
1[𝑓∈𝑆 𝑖]𝑎F(𝑓)𝐻 𝑖(𝑓)−(112)
𝑘∑︁
𝑗=1
∑︁
𝑓∈F′ 𝑗
1[𝑓∈𝑆 𝑖]𝑎F′(𝑓)𝐻 𝑖(𝑓)∥/𝜆 1 (113)
≤
∑︁
𝑖∈𝐼
𝑘∑︁
𝑗=1
∑︁
𝑓∈F 𝑗
1[𝑓∈𝑆 𝑖](𝑎 F(𝑓)+𝑎 F′(𝑓))/𝜆 1 (114)
≤
𝑘∑︁
𝑗=1
∑︁
𝑓∈F 𝑗
1[𝑓∈⊔ 𝑖∈𝐼𝑆𝑖](𝑎 F(𝑓)+𝑎 F′(𝑓))/𝜆 1 (115)
≤2𝑎 max/𝜆1 (116)
by Def. D.1 and using the fact that the𝑆𝑖 are disjoint so
each impression is counted at most once.
□
Theorem D.5.Consider 𝑥∈X withglobal budgetcapac-
ity𝜖global. For simplicity, because we are considering a global
guarantee, we consider a non-adaptive data generation process
in Alg. 11, which defines a mechanism 𝑞. Then,𝑞 satisfies indi-
vidual device-epoch𝜖global-DP for𝑥 under public information
C.
Proof. Denote by 𝑥C =(𝑑,𝑒,𝐹∩C) the device-epoch ob-
tained by keeping only public eventsC from𝑥, where public
events are the set of all conversions.
Take𝑣∈Range(𝑞) . As in Thm. 4.2, we want to show that:

ln  Pr[𝑞(𝐷+𝑥 C)=𝑣] Pr[𝑞(𝐷+𝑥)=𝑣] 

≤𝜖 global.(117)
Using Bayes’ rule and𝜌(𝐷+𝑥 C)=𝜌(𝐷) , as in Thm. 4.2,
we have:

ln  Pr[𝑞(𝐷+𝑥 C)=𝑣] Pr[𝑞(𝐷+𝑥)=𝑣] 

 (118)
=

ln  ˛𝑡max 𝑡=1 ˛ 𝑏∈𝑆 Pr[˝ 𝑟∈𝑅𝑏 𝑡 𝜌𝑏 𝑟,𝑡(𝐷)+𝑋 𝑏 𝑡 =𝑣 𝑏 𝑡] ˛𝑡max
𝑡=1
˛
𝑏∈𝑆 Pr[˝ 𝑟∈𝑅𝑏 𝑡 𝜌𝑏 𝑟,𝑡(𝐷+𝑥)+𝑋 𝑏 𝑡 =𝑣 𝑏 𝑡]
!

(119)
≤
𝑡max∑︁
𝑡=1
∑︁
𝑏∈𝑆

ln  Pr[˝ 𝑟∈𝑅𝑏 𝑡 𝜌𝑏 𝑟,𝑡(𝐷)+𝑋 𝑏 𝑡 =𝑣 𝑏 𝑡] Pr[˝ 𝑟∈𝑅𝑏 𝑡 𝜌𝑏 𝑟,𝑡(𝐷+𝑥)+𝑋 𝑏 𝑡 =𝑣 𝑏 𝑡] !

 (120)
where each query𝑄𝑏 𝑡 ={𝜌 𝑏 𝑟,𝑡,𝑟∈𝑅 𝑏 𝑡} is chosen adaptively,
potentially based on previous results𝑣𝑏 1,...,𝑣 𝑏 𝑡−1 . Since the
filters and attribution functions are identical for𝐷 and𝐷+𝑥
when we condition on past results, we write 𝜌𝑏 𝑟,𝑡(𝐷) for

simplicity instead of𝜌 𝑏 𝑟,𝑡(𝐷;F𝑣<𝑡,𝛼𝑣<𝑡)).
Fix𝑡∈[𝑡 max] and𝑏∈S . Without the optimization, as
in Eq. 84, the device would pay for each report sent to any
querier, which would give:

ln  Pr[˝ 𝑟∈𝑅𝑏 𝑡 𝜌𝑏 𝑟,𝑡(𝐷)+𝑋 𝑏 𝑡 =𝑣 𝑏 𝑡] Pr[˝ 𝑟∈𝑅𝑏 𝑡 𝜌𝑏 𝑟,𝑡(𝐷+𝑥)+𝑋 𝑏 𝑡 =𝑣 𝑏 𝑡] !

 (121)
≤
∑︁
𝑟∈𝑅𝑏 𝑡
Δ𝑥(𝜌𝑏 𝑟,𝑡)pass𝑏 𝑟/𝜆𝑏 𝑡 (122)
Instead of upper-bounding the difference ∥𝜌𝑏 𝑟,𝑡(𝐷) −
𝜌𝑏 𝑟,𝑡(𝐷+𝑥)∥ for each report by Δ𝑥(𝜌𝑟) separately, which
takes a maximum over all𝐷 right away, we keep information
about𝐷 a bit longer. This will allow us to leverage the fact
that reports𝜌𝑏 𝑟,𝑡 across different time steps and queriers tied
to the same identifier𝑟are correlated:

ln  Pr[˝ 𝑟∈𝑅𝑏 𝑡 𝜌𝑏 𝑟,𝑡(𝐷)+𝑋 𝑏 𝑡 =𝑣 𝑏 𝑡] Pr[˝ 𝑟∈𝑅𝑏 𝑡 𝜌𝑏 𝑟,𝑡(𝐷+𝑥)+𝑋 𝑏 𝑡 =𝑣 𝑏 𝑡] !

 (123)
≤
∑︁
𝑟∈𝑅𝑏 𝑡
∥𝜌𝑏 𝑟(𝐷)−𝜌 𝑏 𝑟(𝐷+𝑥)∥/𝜆 𝑏 𝑡 (124)
For a report identifier 𝑟∈Z , we now define T𝑟 , which
keeps track of all queriers that requested a report from𝑟 and
the time steps at which they requested it:
T𝑟 :={(𝑡,𝑏)∈[𝑡 max]×S:𝑟∈𝑅 𝑏 𝑡}(125)
This notation allows us to swap the sums, after putting
Eq. 124 into Eq. 120:

ln  Pr[𝑞(𝐷+𝑥 C)=𝑣] Pr[𝑞(𝐷+𝑥)=𝑣] 

 (126)
≤
𝑡max∑︁
𝑡=1
∑︁
𝑏∈𝑆
∑︁
𝑟∈𝑅𝑏 𝑡
∥𝜌𝑏 𝑟(𝐷)−𝜌 𝑏 𝑟(𝐷+𝑥)∥/𝜆 𝑏 𝑡 (127)
=
∑︁
𝑟∈Z
∑︁
(𝑡,𝑏)∈T𝑟
∥𝜌𝑏 𝑟(𝐷)−𝜌 𝑏 𝑟(𝐷+𝑥)∥/𝜆 𝑏 𝑡 (128)
Fix a report identifier 𝑟∈Z corresponding to a his-
togram attribution object 𝛼𝑟 . Denote by (𝑡0,𝑏 0) the first
time-step/querier pair that requests a report from𝑟, thereby
calling MeasureConversion. By Lem. D.4, we have:
∑︁
(𝑡,𝑏)∈T𝑟
∥𝜌𝑏 𝑟(𝐷)−𝜌 𝑏 𝑟(𝐷+𝑥)∥/𝜆 𝑏 𝑡≤pass𝑏0 𝑟,𝑡 0·Δ𝑥(𝛼𝑟)/𝜆𝑏0 𝑡0
(129)
Finally, sincepass𝑏0 𝑟,𝑡 0 implies that𝜖𝑏0 𝑟,𝑡 0 =Δ𝑥(𝛼𝑟)/𝜆𝑏0 𝑡0 passes
the global budget, by the definition of global budget, Eq. 128
becomes:

ln  Pr[𝑞(𝐷+𝑥 C)=𝑣] Pr[𝑞(𝐷+𝑥)=𝑣] 

 (130)
≤
∑︁
𝑟∈Z
pass𝑏0 𝑟,𝑡 0𝜖𝑏0 𝑟,𝑡 0 (131)
≤𝜖 global (132)
which concludes the proof.□
Remark.Lem. D.3 and D.4 show that for histogram reports
with𝑘> 1epochs, Alg. 12 spends up to|b| times less budget
than Alg. 5 when|b| queriers request reports from the same
conversion with a single report identifier𝑟. This is because
the privacy loss in these cases is proportional to Δ(𝜌)=
2𝑎max. For histogram reports with a single epoch, we can use
the individual sensitivity, which renders this optimization
unnecessary.
