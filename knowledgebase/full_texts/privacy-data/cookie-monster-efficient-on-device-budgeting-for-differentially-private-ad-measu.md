---
title: 'Cookie Monster: Efficient On-Device Budgeting for Differentially-Private Ad-Measurement Systems'
url: https://arxiv.org/abs/2405.16719
category: privacy-data
subcategory: measurement
date: 2024-11
venue: ''
authors:
- Pierre Tholoniat
- Kelly Kostopoulou
- Peter McNeely
source: arxiv
pdf_url: https://arxiv.org/pdf/2405.16719
pages: 27
chars: 127540
fetched_at: '2026-11-08T12:59:43+00:00'
kb_version: 1
---

# Cookie Monster: Efficient On-Device Budgeting for Differentially-Private Ad-Measurement Systems

Cookie Monster: Efficient On-device Budgeting for
Differentially-Private Ad-Measurement Systems
Pierre Tholoniat*
Columbia University
Kelly Kostopoulou*
Columbia University
Peter McNeely
Columbia University
Prabhpreet Singh Sodhi
Columbia University
Anirudh Varanasi
Columbia University
Benjamin Case
Meta Platforms, Inc.
Asaf Cidon
Columbia University
Roxana Geambasu
Columbia University
Mathias Lécuyer
University of British Columbia
Abstract
With the impending removal of third-party cookies from ma-
jor browsers and the introduction of new privacy-preserving
advertising APIs, the research community has a timely oppor-
tunity to assist industry in qualitatively improving the Web’s
privacy. This paper discusses our efforts, within a W3C com-
munity group, to enhance existing privacy-preserving adver-
tising measurement APIs. We analyze designs from Google,
Apple, Meta and Mozilla, and augment them with a more
rigorous and efficient differential privacy (DP) budgeting
component. Our approach, called Cookie Monster, enforces
well-defined DP guarantees and enables advertisers to con-
duct more private measurement queries accurately. By fram-
ing the privacy guarantee in terms of an individual form of
DP, we can make DP budgeting more efficient than in current
systems that use a traditional DP definition. We incorporate
Cookie Monster into Chrome and evaluate it on microbench-
marks and advertising datasets. Across workloads, Cookie
Monster significantly outperforms baselines in enabling more
advertising measurements under comparable DP protection.
CCS Concepts: • Security and privacy;
Keywords: Differential Privacy, Budgeting, Measurement
ACM Reference Format:
Pierre Tholoniat*, Kelly Kostopoulou*, Peter McNeely, Prabhpreet
Singh Sodhi, Anirudh Varanasi, Benjamin Case, Asaf Cidon, Roxana
Geambasu, and Mathias Lécuyer. 2024. Cookie Monster: Efficient
On-device Budgeting for Differentially-Private Ad-Measurement
Systems. In ACM SIGOPS 30th Symposium on Operating Systems
Principles (SOSP ’24), November 4–6, 2024, Austin, TX, USA.ACM,
New York, NY , USA, 27 pages.https://doi.org/10.1145/3694715.
3695965
Permission to make digital or hard copies of part or all of this work for
personal or classroom use is granted without fee provided that copies are not
made or distributed for profit or commercial advantage and that copies bear
this notice and the full citation on the first page. Copyrights for third-party
components of this work must be honored. For all other uses, contact the
owner/author(s).
SOSP ’24, November 4–6, 2024, Austin, TX, USA
© 2024 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-1251-7/24/11.
https://doi.org/10.1145/3694715.3695965
1 Introduction
Web advertising is undergoing significant changes, present-
ing a major opportunity to enhance online privacy. For years,
numerous entities, often without users’ knowledge, have ex-
ploited Web protocol vulnerabilities, such as third-party cook-
ies and remote fingerprinting, to track user activity across
the Web. This data has been used to target individuals with
ads and assess ad campaign performance. Two key shifts
are reshaping this landscape. First, major browsers are mak-
ing it more difficult to track users across websites. Apple’s
Safari and Mozilla’s Firefox blocked third-party cookies in
2019 [20] and 2021 [30], respectively, while Google Chrome
will soon facilitate users’ choice of disabling these cookies [6].
Additionally, browsers are strengthening defenses against IP
tracking [19] and remote fingerprinting [30, 2, 39].
Second, acknowledging the critical role online advertising
plays in the Web economy – and the impossibility of perfect
tracking protection – browsers are introducing explicit APIs
to measure ad effectiveness and enhance ad delivery while
protecting individual privacy. Early designs, like Apple’s
PCM [32] and Google’s FLoC [8], focused on intuitive but not
rigorous privacy methods, resulting in limited adoption due
to poor utility [42] or privacy [17]. Recently, browsers have
shifted to theoretically-sound privacy technologies – such
as differential privacy (DP), secure multi-party computation
(MPC), and trusted execution environments (TEEs) – in the
hope of achieving better privacy-utility tradeoffs.
However, substantial challenges remain in implementing
these privacy technologies at Web scale. The research com-
munity now has a timely opportunity – and responsibility – to
assist industry in refining these technologies to deliver both
strong privacy protections and meet advertising needs. Only
by addressing these challenges can we hope to drive adoption
of privacy-preserving APIs, remove incentives for individual
tracking, and meaningfully improve Web privacy.
This paper focuses on our efforts to analyze and enhance
current ad-measurement APIs(a.k.a., attribution-measurement
APIs), which enable advertisers to measure and optimize the
effectiveness of their ad campaigns based on how often people
*These authors contributed equally to this work.
1
arXiv:2405.16719v5  [cs.CR]  1 Oct 2024

who view or click certain ads go on to purchase the adver-
tised product. While separatead-targeting APIsare also under
development [9], we concentrate on ad-measurement APIs.
The W3C’s Private Advertising Technology Community
Group (PATCG) [35] is working towards an interoperable
standard for private ad-measurement APIs. Leading proposals
include Google’s Attribution Reporting API (ARA) [3], Meta
and Mozilla’s Interoperable Private Attribution (IPA) [21],
Apple’s Private Ad Measurement (PAM) [34], and a hybrid
proposal [18]. Our first contribution is a systematization of
these proposals into abstract models, followed by a compar-
ative analysis to identify opportunities for improving their
privacy-utility tradeoffs (§2).
We focus on the differential privacy (DP) component, present
in all four systems. DP is used to ensure advertisers cannot
learn too much about any single user through measurement
queries. Each system employs a privacy loss budget, account-
ing for the privacy loss incurred by each query. Once the
budget is exhausted, further queries are blocked. This pro-
cess, called DP budgeting, is handled centrally in IPA, but in
the other systems, DP budgeting is done separately by each
device. We observe that thison-device budgeting cannot be
formalized under standard DP and instead requires a variant,
individual DP (IDP) or personalized DP [13], for proper for-
malization. Our formal modeling and analysis of on-device
budgeting under IDP form our second contribution (§4).
Through our IDP formalization, we uncover optimizations
that enhance utility in on-device budgeting systems, allow-
ing advertisers to execute more accurate queries under the
same DP budget. IDP enables devices to maintain their own,
separate DP guarantees and to account for privacy loss based
on the device’s data. This lets a device deduct zero privacy
loss if it lacks relevant data for a query. Notably, one such
optimization is already used in ARA, though without formal
justification. Our third contribution is providing formal proof
for this optimization as well as other, novel optimizations that
can further improve the privacy-utility tradeoff.
Our final contribution is a prototype implementation of
our optimized DP budgeting system, called Cookie Monster,
integrated into ARA within Chrome (§3, §5). Cookie Mon-
ster is the first ad-measurement system to enforce a fixed,
user-time DP guarantee [24], improving on the event-level
guarantees of ARA. We evaluate Cookie Monster on mi-
crobenchmarks and advertising datasets (§6), showing that
it delivers×1.16–2.88 better query accuracy compared to a
user-time version of ARA and substantially outperforms IPA,
which exhausts its budget very early. Our prototype is avail-
able at https://github.com/columbia/cookiemonster and
has been incorporated into a W3C draft report on privacy-
preserving attribution from Mozilla [33].
2 Review of Ad-Measurement APIs
We review the designs of privacy-preserving ad-measurement
systems considered for a potential interoperable standard at
Mar 25-31
Apr 1-7
0.2
0.4
0.6
0.8
1.0
0.0
Mar 18-24
Apr 8-14
Fig. 1. Privacy loss dashboard. Screenshot from our Chrome implementa-
tion of Cookie Monster (minimally edited for visibility).
PATCG: Meta and Mozilla’s IPA, Google’s ARA, Apple’s
PAM, and Meta and Mozilla’s Hybrid. ARA and IPA are
implemented; PAM and Hybrid exist only as design docs. We
abstract their functionality for comparison and articulate the
improvement opportunity addressed in this paper.
2.1 Example Scenario
We use a fictitious scenario to illustrate the motivation and
requirements of ad-measurement systems from two key per-
spectives: Ann, a web user, and Nike, an advertiser measuring
ad campaign effectiveness. While real-world players like first-
party ad platforms (e.g., Meta) and ad-techs (e.g., Criteo)
typically run measurement queries on behalf of advertisers,
for simplicity, we assume the advertiser performs its own
measurements. We discuss the other players in Appendix A.
User perspective. Ann visits various publisher sites, such
as nytimes.com and facebook.com, where she sees ads. She
understands that ads fund the free content she enjoys and oc-
casionally finds them useful, like when she clicked on a Nike
ad for running shoes on nytimes.com and later purchased a
pair. However, Ann values her privacy and expectsno cross-
site tracking, meaning no site should track her across different
websites. She also expects limited within-site linkability, pre-
venting even a single site from linking her activities across
cookie-clearing browsing sessions (e.g., incognito sessions).
Ann accepts that some privacy loss is necessary for effec-
tive advertising but expects it to be explicitly bounded and
transparently reported by her browser.
Fig. 1 shows a screenshot of the privacy loss dashboard we
developed for Cookie Monster in Chrome, where Ann can
monitor the privacy loss resulting from various sites and inter-
mediaries querying her ad interactions, including impressions
(e.g., ad views and clicks) and conversions (e.g., purchases,
cart additions). While Ann may not grasp the concept of dif-
ferential privacy that underpins the reported privacy loss, she
trusts her browser to always enforce protective bounds on it.
Advertiser perspective. Nike runs multiple ad campaigns for
its running shoes, some emphasizing shock-absorbing technol-
ogy, others focusing on aesthetics. Nike seeks to understand
2

which campaigns perform best across different demograph-
ics and contexts (e.g., publisher sites, content types). In the
past, Nike used third-party cookies and device fingerprint-
ing1 to track individuals from ad impressions to purchases,
attributing purchase value using an attribution function, such
as last-touch (giving all credit to the last impression) or equal
credit (splitting value among recent impressions). Using such
attribution reports from many users, Nike measured the pur-
chase value attributed to different campaigns and optimized
future ad targeting.
Now that third-party cookies are disabled on multiple
browsers and fingerprinting is harder, Nike is transitioning
to ad-measurement APIs, expecting similar attribution mea-
surements with comparable accuracy. Nike understands that
ad measurement has always involved some imprecision (e.g.,
due to cookie clearing or fraud), so its expectation of accuracy
from these APIs is not stringent. Nike plans to conduct numer-
ous attribution measurements over time to adjust to changing
user preferences and product offerings. These measurements
are single-advertiser summation queries, a key query type that
ad-measurement systems aim to support.
2.2 Ad-Measurement Systems
IPA, ARA, PAM, and Hybrid aim to balance user privacy
with utility for advertisers and other Web-advertising parties
(referred to as queriers). Utility is defined as the number of
accurate measurement queries a querier can execute under a
privacy constraint. Despite variations in terminology, privacy
properties, and mechanisms, these systems share key similari-
ties. A commonality is the use of DP techniques, with ARA
focusing on event-level DP, while IPA, PAM, and Hybrid
emphasize user-time DP. This paper focuses on user-time DP,
applied per querier site, as defined in §4.2.3.
Common architecture.The high-level architecture of all four
systems is similar (see Fig. 2a). All systems act as intermedi-
aries between user devices and sites. Previously, these parties
collected impression and conversion events directly, matched
them through third-party cookies, performed attribution, and
aggregated reports. To break these privacy-infringing direct
data flows, ad-measurement systems interpose a DP querying
interface over impression and conversion data.
All systems include three core components: (1) the attri-
bution function, which matches conversions to relevant im-
pressions on the same device and assigns conversion value to
impressions based on an attribution logic like last-touch; (2)
DP query execution, which aggregates reports and adds noise
for DP guarantees; and (3) DP budgeting, which tracks pri-
vacy loss from each query using DP composition and enforces
a maximum on total privacy loss, called a DP budget.
A key difference is where these components are executed.
In IPA, all components run off-device within an MPC in-
volving multiple helper servers. In ARA, PAM, and Hybrid,
1The example is fictitious, as are claims regarding the companies mentioned.
attribution and DP budgeting occur on-device, while DP query
execution is off-device, in an MPC (PAM, Hybrid) or TEE
(ARA). The MPC/TEE is trusted not to leak inputs, and the
devices are trusted to safeguard their own data. The placement
of attribution and DP budgeting is crucial for this paper.
Off-device budgeting (IPA).Fig. 2b illustrates IPA, which
operates in a standard centralized-DP setting. The MPC han-
dles all three functions, while the device’s role is limited to
generating a match key to link impressions and conversions.
For example, when nytimes.com sends an ad for Nike shoes to
Ann’s device 1○, the device responds with a match key, secret-
shared and encrypted toward the MPC helper servers 2○.
When Ann later purchases the shoes on nike.com, her de-
vice sends the same key to the MPC, also secret shared and
encrypted toward the helpers. Periodically, NYtimes sends
batches of encrypted impression match keys to Nike, who can-
not directly match these with its conversion match keys due
to the encryption and secret sharing. Instead, Nike collects
its conversion match keys and NYtimes’ impression match
keys into batches and submits them to the MPC, specifying
the privacy budget 𝜖 to spend on the query 3○. The MPC
checks the budget, matches impressions to conversions, ap-
plies the attribution function with an 𝐿1 cap for sensitivity
control, aggregates the data, and adds DP noise to enforce
𝜖-DP. The MPC tracks and deducts Nike’s privacy budget,
refusing further queries once the budget is exhausted until the
per-site budget is “refreshed” (e.g., daily).
On-device budgeting (ARA, PAM, Hybrid). Fig. 2c shows
the on-device architecture, which operates in a rather non-
standard DP setting. While DP query execution occurs cen-
trally on the MPC or TEE, attribution and DP budgeting
are done separately on each device. Every device maintains
a timeseries database of impression and conversion events.
When Ann sees an ad for Nike on nytimes.com, her device
records it locally 1○. Later, when she buys shoes on nike.com,
Nike requests an attribution report from her device. Ann’s
device checks its database for relevant impressions, applies
the attribution function with an𝐿1 cap, and sends an attribu-
tion report 2○, either secret-shared and encrypted toward the
helper parties (for MPC) or directly encrypted to a TEE. Nike
aggregates attribution reports from multiple users, submits
them to the MPC or TEE, which performs DP aggregation,
adding noise based on Nike’s𝜖 parameter 3○. The MPC/TEE
ensures each report is used only once for sensitivity control.
DP budgeting in on-device systems differs from central-
ized DP by accounting for privacy loss when the advertiser
requests a conversion report, prior to query execution. When
Nike requests a report, it specifies the 𝜖 parameter for the
future query. The device checks Nike’s budget locally, gen-
erates and encrypts the report (with secret sharing if MPC is
used), includes𝜖 as authenticated data, and deducts 𝜖 from
Nike’s local budget. Since the budget is spent at the device,
each report can only be used once, so the device includes a
3

(c) On-device budgeting architecture (ARA, PAM, Hybrid)
DP query execution
MPC
DP budgeting
attribution function
Querier
(Publisher/
Advertiser/
Ad-tech)
② encrypted I/C
match keys
③ batch of encrypted
I/C match keys,
query, ε
MPC/TEE
Querier
(Publisher/
Advertiser/
Ad-tech)
② encrypted
attribution
reports (ε as
auth data)
① impression (I),
conversion (C) events
PublishersPublishers
 PublishersAdvertisers
 Publisher
sAd-techs
Devices
impressions,
conversions
attribution reports
(encrypted),
  queries
(a) Common architecture
Ad-Measurement API
(ARA, IPA, PAM, Hybrid)
Runtimes
MPC
/TEE
on-device
attribution function
DP budgeting
Functions
DP query execution
(b) Off-device budgeting architecture (IPA)
IPA
IPA
IPA
εG
DP query execution
I/C events
attribution
function
εG 1
DP
budgeting
③  batch of encrypted
attribution reports,
query, ε
I/C events
attribution
function
DP
budgeting
I/C events
attribution
function
DP
budgeting
εG 2 εG 3
① impression (I),
conversion (C) events
(ε specified for C       )
Fig. 2. Architectures of ad-measurement systems. Common structure, with a key difference in where attribution and DP budgeting occur: off-device (IPA) vs.
on-device (ARA, PAM, Hybrid).
unique nonce with every report in authenticated data and the
MPC/TEE tracks report nonces to prevent reuse.
Threat models. The threat models differ based on whether
an MPC or TEE is used. In all cases, MPC/TEE systems are
trusted to protect inputs and intermediate states. For MPC, the
deployment models assume either a three-party, malicious,
honest-majority MPC protocol (IPA, Hybrid) [21] or a two-
party malicious protocol (PAM). The querier selects MPC
parties from a browser-configured list, typically relatively
trusted Web organizations like Cloudflare. The device secret
shares the report and encrypts it toward the chosen parties
after report generation.
2.3 Improvement Opportunity
On-device budgeting systems offer certain advantages over
off-device systems but also present a key challenge, which
we aim to address. First, on-device systems can enhance user
transparency by putting the user’s device in control of per-site
budgets and the tracking of privacy losses incurred by the
user due to specific attribution reports the device releases to
various querier sites, as seen in the Cookie Monster privacy
loss dashboard (Fig. 1). In contrast, in IPA, the device can
only track the encrypted match keys returned by the device,
not the specific privacy losses users incur through subsequent
matching and aggregation in the MPC.
Second, on-device systems allow for finer-grained bud-
geting. While off-device systems enforce a global site-wide
budget𝜖𝐺, on-device systems maintain a per-device budget
𝜖𝐺 𝑑 , which is only consumed for queries involving that de-
vice. This granularity enables Nike, for instance, to continue
querying other users’ reports even if it exhausts Ann’s budget.
However, this behavior requires formalization under the less
standard (but equally protective) privacy definition known
as individual DP (IDP) [13], which allows enforcement of a
separate privacy guarantee for each device.
The challenge lies in formalizing the data, query, and
system model that capture the behavior of on-device ad-
measurement systems, and in proving its IDP properties. This
formalization then opens opportunities for further optimizing
DP budgeting in on-device systems by deducting privacy loss
based on the device’s data. However, it also requires keep-
ing the remaining privacy budgets on each device private,
as revealing these budgets leaks data. This paper presents a
formally-justified, practical and efficient DP budgeting mod-
ule, Cookie Monster, designed for on-device systems like
ARA, PAM, and Hybrid, which maximizes utility while main-
taining DP guarantees.
3 Cookie Monster Overview
The design of Cookie Monster is guided by three princi-
ples. First, it must enforce well-defined DP guarantees at
an industry-accepted granularity. We adopt a fixed “user-time”
DP guarantee for each querier, supported by IPA, PAM, and
Hybrid, and recognized by Apple, Meta, and Mozilla as the
minimum acceptable. Second, Cookie Monster must support
similar use cases and queries as existing systems. We focus on
the single-advertiser measurement query from §2.1, though
we briefly discuss in Appendix A how a multi-advertiser op-
timization query might apply. Finally, Cookie Monster must
not introduce new vectors for illicit tracking, given increas-
ing browser efforts to prevent tracking both across sites and
within-site across cookie refreshes.
Fig. 3 presents Cookie Monster’s architecture with an ex-
ample execution overlaid. We describe each aspect below.
3.1 Architecture
Cookie Monster adopts on-device budgeting, similar to ARA,
PAM, and Hybrid. DP query execution occurs off device, in
an MPC or TEE, trusted not to leak inputs or intermediate
states. Since Cookie Monster does not modify this compo-
nent, it is omitted from Fig. 3; we think of it as a trusted
aggregation service. Cookie Monster modifies the on-device
component, based on ARA in our prototype. While the ex-
ternal APIs remain unchanged, we modify: (1) the on-device
events database to support a “user-time” guarantee, and (2)
the internals of the attribution function and DP budgeting to
enforce this guarantee efficiently.
4

DP budgeting
(per querier)
DP budgeting
(per querier)
attribution
function
device-
epoch
events
data
DP budgeting
(per querier)
Publisher
(nytimes.
com)
Publisher
(bbc.com)
 Price:$60-100
Advertiser
(nike.com)
time
(epochs)Dd e1 Dd e2 Dd e3 Dd e4
I1 I2 C1
@e1: I1
Ad
@e4: C1, with params:
output_dimension m=2,
attribution_window_epochs E=[e1…e4],
conversion_value=70,
max_conversion_value=100,
ε=0.01
@e2: I2
time
(epochs)
εG d
Algorithm (summary): check for relevant
impressions in epochs E with sufficient budget
ε*70/100, deducting individual privacy loss in each
epoch with relevant impressions.
individual
device-epoch
privacy loss
(nike.com)
encrypted
attribution
report
ρ={(I2,70),
(0,0)}
Ad
Cookie Monster (on device d)
(guarantee: individual device-epoch εG d-DP
for each querier)
Fig. 3. Cookie Monster architecture and example execution (red overlay).
§3.1 describes the architecture and §3.2 the example execution. Notation:
@𝑒1 :𝐼1 indicates that Ann’s device receives an impression𝐼1 of a Nike shoe
ad from nytimes.com in epoch𝑒1. Red dotted arrows show the attribution
function’s search for impressions over epochs𝑒1−𝑒4.
Cookie Monster enforces individual device-epoch𝜖𝐺 𝑑 -DP
for each querier site, formally defined in §4.2.3. This device-
epoch granularity aligns with traditional “user-time” from DP
literature [24, 26, 27], though we rename it to reflect that a
user’s complete activity is not directly observable by a device
or browser, the scope in which Cookie Monster operates.
We partition the on-device events database into time-based
epochs, such as weeks or months. In each epoch𝑒, device𝑑
collects impression and conversion events into adevice-epoch
database 𝐷𝑒 𝑑. Queriers submit multiple queries over time,
accessing data from one or more epochs. For each epoch 𝑒,
Cookie Monster ensures that no querier learns more about
device𝑑’s data in𝑒 than permitted by an𝜖𝐺 𝑑 -DP guarantee.
The DP budgeting in Cookie Monster is implemented using
privacy filters [37], which ensure that the cumulative privacy
loss from a series of queries does not exceed a pre-specified
budget. For each querier, Cookie Monster maintains multiple
filters – one for each device-epoch database. Fig. 3 shows
these filters for nike.com. Each filter is initialized with a
privacy budget𝜖𝐺 𝑑 and monitors cumulative privacy loss for
queries involving data from that epoch.
In on-device systems, privacy loss is accounted for when
the attribution report is generated, not when the query is exe-
cuted. The attribution function is responsible for generating
these reports. Upon a conversion, the function checks for
relevant impressions in the device-epoch databases within a
specified attribution window. Privacy filters prevent use of
impression data from epochs with insufficient budget.
For epochs with sufficient budget, the filter allows access
to the device-epoch data and deducts privacy loss. Under stan-
dard centralized DP, this loss would be𝜖, the DP parameter
enforced later by the MPC or TEE during aggregation. How-
ever, our theoretical analysis of on-device budgeting reveals
that viewing the system under an individual-DP lens opens
opportunities to optimize privacy accounting, often allow-
ing deductions of “less than 𝜖.” §4 outlines our theoretical
analysis, a major contribution in this paper. We dedicate the
remainder of this section to providing the systems view of
our theory, including an execution example (§3.2), Cookie
Monster’s algorithm, which is backed by our theory (§3.3),
and a discussion on mitigating IDP-induced bias (§3.4).
3.2 Execution Example
The red overlay in Fig. 3 illustrates the attribution function’s
operation for the example from §2.1. Ann receives two im-
pressions of Nike shoe ads: one in epoch 𝑒1 and another in
𝑒2, with no impressions in 𝑒3. Later, in epoch𝑒4, Ann buys
the shoes, and nike.com registers a conversion𝐶1. It requests
an attribution report with parameters: the set of epochs𝐸 to
search for impressions, the maximum number of impressions
𝑚 to attribute value to, the conversion value ( $70), and 𝜖,
the privacy parameter enforced by the MPC or TEE when
executing the aggregation query.
The shoes’ price ranges by color, with a maximum of $100.
While Ann’s conversion is $70, Nike’s query will include
conversions up to $100. Thus, for a summation query with
the Laplace mechanism, the noise added to the aggregate
depends on 100/𝜖, where 100 is the global sensitivity of the
summation (i.e., the largest change any device-epoch can
contribute). Ann, with a purchase of $70, can only contribute
up to $70 across her device-epochs.
Here, IDP lets us optimize privacy loss based onindividual
sensitivity, the maximum change that a specific device-epoch
can make on the query output. In this case, Ann’s device
only deducts𝜖′ = $70/$100∗𝜖 from the privacy filters of the
epochs in the attribution window𝐸. This is one optimization
enabled by IDP. Another is that if no relevant impressions
exist in an epoch (e.g., 𝑒3 in Fig. 3), we need not deduct
anything, since the individual sensitivity for that epoch is 0
and thus its privacy loss is also 0. §4.3 formalizes global and
individual sensitivities and details further optimizations.
In Fig. 3, Cookie Monster’s attribution function checks
epochs𝑒1−𝑒4 for relevant impressions. In𝑒1, access to data
𝐷𝑒1 𝑑 is denied because the filter has exhausted nike.com’s bud-
get. In𝑒2, the filter allows access, and a relevant impression𝐼2
is found, deducting𝜖′ (shown as a red square in the𝑒2 filter).
In𝑒3, there is budget, but no relevant impression is found,
so no deduction occurs. Finally, in𝑒4, where the conversion
happened but no impression occurred, then through a for-
malization of publicly available information that we support
(§4.1), we can justify that no privacy loss occurs in𝑒4.
5

The final attribution report assigns the $70 value to the
single impression𝐼2 and includes a null value for the second
attribution, as Nike requested two. If no impressions were
found, or Nike also ran out of budget in 𝑒2, the attribution
function would return a report with two null values to avoid
leaking information about ad presence.
3.3 Algorithm
Listing 1 shows how Cookie Monster computes an attribu-
tion report. The compute_attribution_report function
receives an attribution_request, which encapsulates all
querier-provided parameters, sanitized by the device. Key
parameters include:
1. the window of epochs to search for relevant events
(epochs parameter);
2. the requested privacy budget (requested_epsilon);
3. logic for selecting relevant events (select_relevant
_events);
4. the attribution policy, such as last-touch or equal-credit
(compute_attribution);
5. two global sensitivity parameters: report_global
_sensitivity, the maximum change a device-epoch
can make to the output of the report generation func-
tion, and query_global_sensitivity, the maxi-
mum across all devices and reports;
6. p-norm, based on the DP mechanism in MPC/TEE, e.g.,
1-norm for Laplace and 2-norm for Gaussian.
All parameters follow a predefined protocol, and while the
algorithm is general enough to handle different mechanisms
and p-norm sensitivities, our DP result (Thm. 1) focuses on
pure DP, assuming the Laplace mechanism and𝐿1 sensitivity.
Computing an attribution report consists of four steps.
Step 1: Cookie Monster invokes the querier-provided
select_relevant_events to select relevant events from
each separate epoch in the attribution window, such as im-
pressions with a specific campaign ID.
Step 2: For each epoch, Cookie Monster computes the
individual privacy loss resulting from the querier’s query,
following the IDP optimizations in Thm. 4. Three cases:
1. if the epoch has no relevant events, privacy loss is zero;
2. if a single epoch is considered, privacy loss is propor-
tional to the𝐿𝑝-norm of the attribution function output;
3. if multiple epochs are considered, privacy loss is pro-
portional to the report’s global sensitivity.
The privacy loss is scaled by requested_epsilon and the
query’s global sensitivity. In §3.2, the report’s global sensitiv-
ity is 70, and the query’s global sensitivity is 100.
Step 3: For each epoch, we attempt to deduct the computed
privacy loss from the querier’s budget for that epoch, ensuring
atomic, thread-safe checks. If the filter has sufficient budget,
the epoch’s events are used for attribution; otherwise, they
are dropped. The justification for dropping contributions is
provided in Theorem 1.
Step 4: The attribution function is applied across events
from all epochs, following the querier’s policy. The device
ensures that the attribution computation: (1) respects the
querier’s specified report_global_sensitivity by clip-
ping the attribution histogram to ensure its 𝐿𝑝-norm is ≤
report_global_sensitivity, and (2) produces encrypted
outputs indistinguishable from others. For (2), the device en-
sures a fixed dimension for the attribution report by padding
or dropping elements. For instance, if only one relevant im-
pression is found but two are requested, the output vector is
padded with a null entry.
# Global variables: events_database, privacy_filters.
def compute_attribution_report(attribution_request):
relevant_events_per_epoch = {}
for epoch in attribution_request.epochs:
relevant_events = attribution_request.select_relevant_events(
events_database[epoch]) # Step 1
individual_privacy_loss = compute_individual_privacy_loss(
relevant_events, attribution_request) # Step 2
filter_status = privacy_filters[attribution_request.
querier_site][epoch].check_and_consume(
individual_privacy_loss) # Step 3
if filter_status == "out_of_budget":
relevant_events = {}
relevant_events_per_epoch[epoch] = relevant_events
return attribution_request.compute_attribution(
relevant_events_per_epoch) # Step 4
def compute_individual_privacy_loss(epoch_events,
attribution_request):
if epoch_events == {}: # Case 1 in Theorem 4
return 0
if len (attribution_request.epochs) == 1: # Case 2 in Theorem 4
individual_sensitivity = attribution_request.pnorm(
attribution_request.compute_attribution(relevant_events))
else: # Case 3 in Theorem 4
individual_sensitivity = attribution_request.
report_global_sensitivity
return attribution_request.requested_epsilon *
individual_sensitivity / attribution_request.
query_global_sensitivity
Code Listing 1. Cookie Monster Algorithm
For the example in §3.2, this algorithm is invoked with an
attribution_request where querier_site = “nike.com,”
epochs =[𝑒1−𝑒4], report_global_sensitivity = 70,
query_global_sensitivity = 100. Function select
_relevant_events filters impressions by campaign ID,
pnorm returns the L1-norm of the attribution histogram, and
compute_attribution divides the conversion value of 70
across at most two impressions, padding with nulls as needed.
This attribution function has sensitivity 70.
3.4 Bias Implications of IDP
The execution example and algorithm demonstrate Cookie
Monster’s budget savings, confirmed in Section 6, where we
show that these savings allow more accurate queries than
ARA and IPA under the same privacy guarantees. However,
IDP can introduce bias into query results. Since privacy loss
and remaining budgets depend on data, they must remain
hidden from advertisers. When a device exhausts its budget
for an epoch, it continues participating in queries with “null”
data, protecting privacy but potentially introducing bias. For
example, Nike’s report should have included two impressions,
but running out of budget in epoch𝑒1 meant𝐼1 wasn’t returned,
altering the report undetectably.
6

This bias is a general challenge for all systems operating
on IDP, including all existing ad-measurement systems with
on-device budgeting – although this challenge is not always
acknowledged or handled. Indeed, ARA incorporates code
to send null reports when budgets are exhausted and its doc-
umentation states that these nulls must be sent to preserve
privacy [16]. Such nulls would add bias to query results. In
absence of proper IDP formulation, a rudimentary justifica-
tion we have seen for sending nulls in on-device systems is
to prevent revealing budget exhaustion, which could facili-
tate remote fingerprinting, a concern actively addressed by
browsers. Our paper reveals a deeper issue: these systems
inherently operate under IDP, and IDP systems must keep
budgets hidden, which can lead to bias. Acknowledging this
bias opens pathways to mitigate it.
Any (DP or IDP) system must tolerate some error. In ad
measurement, high error tolerance is common due to factors
like tracking inaccuracies and fraud. The goal is to equip
queriers with tools that rigorously bound errors from both DP
noise and IDP bias, allowing for informed decision-making.
Previous work on centralized-budgeting IDP has developed
methods to bound bias using global sensitivity [14] and peri-
odic DP counting queries [45, 14]. These approaches require
adaptation to on-device budgeting, given the lack of central-
ized privacy-loss tracking and non-i.i.d. report sampling. We
leave it for future work to develop advanced bias-management
tools and here only present a rudimentary approach, which
we implement in Cookie Monster and evaluate in §6.5 as
a proof-of-concept that bias can be effectively managed in
on-device budgeting systems.
Our approach adds a side query to each attribution query,
which bounds potential error from out-of-budget epochs. With
each report, the querier requests a boolean flag indicating
whether the report could be affected by an out-of-budget
epoch. This flag is bundled with the attribution report, secret-
shared, and encrypted toward the MPC/TEE. The querier
receives a DP-aggregated count of how many reports could
be erroneous out of its total batch. With the count, the querier
computes a high-probability upper bound on the error from
both DP noise and IDP bias. The querier can then filter the
results of its queries based on this error bound, ignoring those
with unacceptable error. Formalization and proof of this mech-
anism’s correctness are deferred to Appendix F.
Consider last-touch attribution. If no epoch in the attribu-
tion window is out of budget or an impression is found in a
later epoch, the device returns a 0-valued error assessment,
indicating no bias. If no impression is found in epochs later
than the out-of-budget epoch, the device returns a 1-valued
error assessment, signaling potential bias. This information is
encrypted and only accessible to the querier after DP aggre-
gation by the MPC/TEE.
This mechanism lets queriers manage IDP-induced error
rigorously, though it consumes additional privacy budget. In
Steps 3 and 4 of Listing 1, each epoch that is not out of bud-
get must deduct privacy loss for the side query. Fortunately,
since the side query is a count query with lower sensitivity
than the main query, Cookie Monster’s optimizations still
provide benefits. Our evaluation shows that even with bias
detection, Cookie Monster consumes less privacy and incurs
lower errors compared to ARA and IPA (§6.5).
4 Formal Modeling and Analysis
This section outlines the theoretical analysis behind Cookie
Monster’s design, divided into three parts: §4.1 introduces
a formal model that captures the behavior of on-device bud-
geting systems, including Cookie Monster but also ARA
and PAM. §4.2 analyzes this model under IDP, proving that
Cookie Monster bounds cross-site leakage and within-site
linkability. Finally, §4.3 details and justifies the optimizations
enabled by IDP, both ones inherently employed in ARA and
new ones that our theory uncovers.
4.1 Formal System Model
To rigorously analyze privacy properties and identify opti-
mization opportunities in on-device budgeting systems for
ad measurement, we must establish a formal model of their
behavior. Current ad-measurement systems lack such models,
preventing formal analysis or justification of optimizations.
Although our model is tailored to Cookie Monster, it can also
serve as a foundation for analyzing other systems.
We define the data and queries Cookie Monster operates
on, from the perspective of a fixed querier (e.g., advertiser,
publisher, or ad-tech). Appendix §C formalizes the end-to-
end algorithm, incorporating these models and the Cookie
Monster behavior outlined in §3. Since this algorithm is used
solely to prove the DP guarantees in §4.2, we omit it here.
4.1.1 Data Model
Our data model is based on conversion and impression events
collected by user devices and grouped by the time epoch in
which they occurred. We view the data available to queriers
as a database of such device-epoch groups of events, coming
from many devices and defined formally as follows.
Conversion and impression events (F). Consider a domain
of impression eventsI and a domain of conversion events
C. A set of impression and conversion events𝐹 is a subset of
I∪C . The powerset of events isP(I∪C) :={𝐹 :𝐹⊂I∪C} .
Device-epoch record (x). Consider a set of epochs E and
a set of devicesD. We define the domain for device-epoch
recordsX :=D×E×P(I∪C) . That is, a device-epoch
record𝑥 =(𝑑,𝑒,𝐹 ) contains a device identifier𝑑, an epoch
identifier𝑒, and a set of impression and conversion events𝐹.
Database (D). A database is a set of device-epoch records,
𝐷⊂X , where a device-epoch appears at most once. That is,
∀𝑑,𝑒 ∈D×E ,|{𝐹⊂I∪C :(𝑑,𝑒,𝐹 )∈ 𝐷}|≤ 1. We denote
the set of all possible databases by D. This will be the domain
of queries in Cookie Monster. Given a database𝐷∈ D and
7

𝑥∈X ,𝐷+𝑥 denotes that device-epoch record𝑥 is added to
database𝐷 that initially did not include it.
Device-epoch events data (De d, DE d). Given a database𝐷∈ D,
we define 𝐷𝑒 𝑑 ⊂I∪C as𝐷𝑒 𝑑 = 𝐹 if there exist (a unique)
𝐹 such that(𝑑,𝑒,𝐹 )∈ 𝐷, and 𝐷𝑒 𝑑 =∅ otherwise. Think of
this as the event data of device𝑑 at epoch𝑒. We also define
𝐷𝐸 𝑑 :=(𝐷𝑒 𝑑)𝑒∈𝐸∈P(I∪C) |𝐸| the events of device𝑑 over a
set of epochs𝐸 (typically a contiguous window of epochs).
Public events (𝑃). A key innovation in Cookie Monster’s
data model is to support incorporation of side information
that can be reliably assumed as available to the querier. For
example, an advertiser such as Nike can reliably know when
someone places a product into a cart (i.e, a conversion oc-
curred), though depending on whether the user is logged in
or not, Nike may or may not know who did that conversion.
We model such side information as a domain of public
events for a querier, denoted𝑃⊆I∪C .𝑃 is a subset of all
possible events, that will be disclosed to the querier if they
occur in the system. We donot assume that the querier knows
the devices on which events in𝑃 occur, and different queriers
can have knowledge about different subsets of events. Such
side information is typically not modeled explicitly in DP
systems, as DP is robust to side information. Cookie Monster
also offers such robustness to generic side information. How-
ever, we find that additionally modeling the “public” events
known to the querier has two key benefits. First, it opens DP
optimizations that leverage this known information to con-
sume less privacy budget. Second, it lets us formally define
within-site linkability and adapt our design to provide a DP
guarantee against such linkability.
4.1.2 Query Model
In on-device systems, queries follow a specific format: first
the attribution function runs locally to generate an attribution
report, on a set of devices with certain conversions; then, the
MPC sums the reports together and returns the result with
DP noise. Formally, we define three concepts: attribution
function, attribution report, and query.
Attribution function, a.k.a. attribution (A). Fix a set of
events relevant to the query𝐹𝐴∈P(I∪C) , and𝑘,𝑚 ∈ N∗
where𝑘 is a number of epochs. An attribution function is
a function 𝐴 :P(I∪C) 𝑘 → R𝑚 that takes 𝑘 event sets
𝐹1,...,𝐹 𝑘 from𝑘 epochs and outputs an𝑚-dimensional vector
𝐴(𝐹1,...,𝐹 𝑘), such that only relevant events contribute to𝐴.
That is, for all(𝐹1,...,𝐹 𝑘)∈P(I∪C) 𝑘, we have:
𝐴(𝐹1,...,𝐹 𝑘) =𝐴(𝐹1∩𝐹𝐴,...,𝐹 𝑘∩𝐹𝐴).
Attribution report, a.k.a. report (𝜌). This is where the non-
standard behavior of on-device budgeting systems, which
deduct budget only for devices with specific conversions,
becomes apparent. Intuitively, we might consider attribution
reports as the “outputs” of an attribution function. However, in
the formal privacy analysis, we must account for the fact that
only certain devices self-select to run the attribution function
(and thus deduct budget). We model this in two steps. First, we
introduce a conceptual report identifier,𝑟, a unique random
number that the device producing this report generates and
shares with the querier at report time.
Second, we define an attribution report as a function over
the whole database𝐷, that returns the result of an attribution
function𝐴 for a set of epochs𝐸 only for one specific device
𝑑 as uniquely identified by a report identifier 𝑟. Formally,
𝜌𝑟 : 𝐷 ∈ D↦→ 𝐴(𝐷𝐸 𝑑). At query time, the querier selects
the report identifiers it wants to include in the query (such as
those associated with a type of conversion the querier wants
to measure), and devices self-select whether to deduct budget
based on whether they recognize themselves as the generator
of any selected report identifiers. Defining attribution reports
on𝐷 lets us account for this self-selection in the analysis.
Query (Q). Consider a set of report identifiers𝑅⊂ Z, and a
set of attribution reports(𝜌𝑟)𝑟∈𝑅 each with output in R𝑚. The
query for(𝜌𝑟)𝑟∈𝑅 is the function𝑄 : D→ R𝑚 is defined as
𝑄(𝐷) := ˝ 𝑟∈𝑅𝜌𝑟(𝐷) for𝐷∈ D.
4.1.3 Instantiation in Example Scenario
To make our data and query models concrete, we instantiate
the scenarios from §2.1.
User Ann’s data, together with that of other users, populates
dataset 𝐷. Each device Ann owns has an identifier 𝑑, and
events logged from epoch𝑒 go into observation𝑥 =(𝑑,𝑒,𝐹 ).
𝐹 = 𝐼∪𝐶 is the set of all events logged on that device dur-
ing that epoch, including impressions (𝐼) shown to Ann by
various publishers, and conversions (𝐶) with various adver-
tisers. Other devices of Ann, other epochs, and other users’
device-epochs, constitute other records in the database.
The advertiser, Nike, can observe some of Ann’s behavior
on its site. As a result, any such behavior logged in 𝐶 on
nike.com constitutes public information for querier Nike. This
might include purchases, putting an item in the basket, as well
as associated user demographics (e.g., when Ann is logged-
in). However, Nike cannot observe impression or conversion
events on other websites. As a result, for this querier 𝑃 =
CNike, which denotes all possible events that can be logged
on nike.com. Each actual event in this set (e.g., 𝐹∩C Nike,
including Ann’s purchase) is associated with an identifier𝑟
in Cookie Monster. Using these identifiers, Nike can analyze
the relative effectiveness of two ad campaigns𝑎1 and𝑎2 on
a given demographics for a product 𝑝, such as the shoes
Ann bought. First, Nike defines the set of relevant events
for the shoe-buying conversion; these are any impressions of
𝑎1 and𝑎2. Nike uses these relevant events in an attribution
function𝐴 :P(I∪C) |𝐸|→ R2 that looks at epochs in 𝐸
and returns, for example, the count (or value) of impression
events corresponding to ads 𝑎1 and𝑎2. Third, using the set
of report identifiers𝑟 from purchases of𝑝 from users in the
target demographic, Nike constructs a query𝑄 that will let it
directly compare the proportion of purchases associated with
ad campaign𝑎1 versus campaign𝑎2.
8

4.2 IDP Formulation and Guarantees
With Cookie Monster’s data and query models defined, we
now formalize and prove its privacy guarantees using individ-
ual DP. After introducing our neighboring relation in §4.2.1,
we briefly define traditional DP for reference in §4.2.2, fol-
lowed by individual DP in §4.2.3. In §4.2.4, we state the
IDP guarantees for Cookie Monster, which imply protection
against both cross-site tracking and within-site linkability.
4.2.1 Neighboring Databases
A DP guarantee establishes the neighboring database rela-
tion, determining the unit of protection. In our case, this unit is
the device-epoch record. To account for the existence of pub-
lic event data (§4.1.1), we constrain neighboring databases
to differ by one device-epoch record while preserving pub-
lic information. This ensures that a database containing an
arbitrary device-epoch record is indistinguishable from a data-
base containing a device-epoch record with the same public
information but no additional data.
Neighboring databases under public information (𝐷∼𝑃 𝑥
𝐷′). Given𝐷,𝐷′∈ D,𝑥 =(𝑒,𝑑,𝐹)∈X and𝑃⊂I∪C , we
write𝐷∼𝑃 𝑥 𝐷′ if there exists 𝐷0∈ D such that{𝐷,𝐷′} =
{𝐷0+(𝑒,𝑑,𝐹),𝐷 0+(𝑒,𝑑,𝐹 ∩𝑃)}. This definition corresponds
to a replace-with-default definition [14] combined with La-
bel DP [15]. Although public data is baked into our neigh-
boring relation, which makes it specific to each individual
querier, we have proven that composition across queriers is
still possible, which is important to reason about collusion
(Appendix §D.3).
4.2.2 DP Formulation (for Reference)
In DP, noise must be applied to query results based on the
query’s sensitivity–the worst-case difference between two
neighboring databases. Traditional DP mechanisms rely on
global sensitivity.
Global sensitivity. Fix a query𝑞 : D→ R𝑚 for some𝑚 (so
𝑞 could be either a query or an individual report in our for-
mulation). We define the global𝐿1 sensitivity of𝑞 as follows:
Δ(𝑞) := max
𝐷,𝐷′∈D:∃𝑥∈X,𝐷′=𝐷+𝑥 ∥𝑞(𝐷)− 𝑞(𝐷′)∥ 1. (1)
Device-epoch DP.When scaling DP noise to the global sen-
sitivity under our neighboring definition, we can provide
device-epoch DP. Fix 𝜖 > 0 and 𝑃 ⊂ I∪C . A random-
ized computation M : D → R𝑚 satisfies device-epoch
𝜖-DP if for all databases 𝐷,𝐷′ ∈ D such that 𝐷 ∼𝑃 𝑥 𝐷′
for some 𝑥 ∈X , for any set of outputs 𝑆 ⊆ R𝑚 we have
Pr[M(𝐷)∈ 𝑆]≤ 𝑒𝜖 Pr[M(𝐷′)∈ 𝑆]. This is the traditional
DP definition, instantiated for our neighboring relation.
4.2.3 IDP Formulation
Since queries are aggregated from reports computed on-
device with known data, we would prefer to scale the DP
noise to the individual sensitivity, which is the worst case
change in a query result triggered by the specific data for
which we are computing a report.
Individual sensitivity. Fix a function𝑞 : D→ R𝑚 for some
𝑚 (so𝑞 could be either a query or an individual report in
our formulation) and𝑃⊂I∪C . Fix𝑥∈X . We define the
individual𝐿1 sensitivity of𝑞 for𝑥 as follows:
Δ𝑥(𝑞) := max 𝐷,𝐷′∈D:𝐷′=𝐷+𝑥 ∥𝑞(𝐷)− 𝑞(𝐷′)∥ 1. (2)
While we cannot directly scale the noise to individual sen-
sitivity, we can scale the on-device budget consumption us-
ing this notion of sensitivity. That is, for a fixed and known
amount of noise that will be added to the query, a lower indi-
vidual sensitivity means that less budget is consumed from a
device-epoch. This approach provides a guarantee of individ-
ual 2 DP [13, 14] for a device-epoch, defined as follows.
Individual device-epoch DP. Fix𝜖 > 0,𝑃 ⊂I∪C , and
𝑥∈X . A randomized computationM : D→ R𝑚 satisfies
individual device-epoch𝜖-DP for𝑥 if for all databases𝐷,𝐷′∈
D such that𝐷∼𝑃 𝑥 𝐷′, for any set of outputs𝑆⊆ R𝑚 we have
Pr[M(𝐷)∈ 𝑆]≤ 𝑒𝜖 Pr[M(𝐷′)∈ 𝑆].
Intuitively, IDP ensures that, from the point of view of
a fixed device-epoch 𝑥, the associated data 𝐹 is as hard to
recover from query results as it would be under DP.
4.2.4 IDP Guarantees
Through IDP, we prove two main properties of Cookie Mon-
ster: (1) Individual DP guarantee, which implies bounds on
cross-site leakage, demonstrating that the API cannot be used
to reveal cross-site activity; and (2) Unlinkability guarantee,
which implies bounds on within-site linkability, demonstrat-
ing that the API cannot be used even by a first-party site to
distinguish whether a set of events is all on one device vs.
spread across two devices. Proofs are in Appendix §D.
For the IDP guarantee, we give two versions. First, a
stronger version under a mild constraint on the class of al-
lowed queries, specifically that∀𝑖,∀𝐹, 𝐴(𝐹1, ...,𝐹𝑖−1,𝐹𝑖∩𝑃,
𝐹𝑖+1, ...,𝐹𝑘) = 𝐴(𝐹1, ...,𝐹𝑖−1,∅,𝐹𝑖, ...,𝐹𝑘). A sufficient condi-
tion is to ensure that queries leverage public events only
through their report identifier, i.e.,𝐹𝐴∩𝑃 =∅. The queries
from the scenarios we consider (§2.1) satisfy this property.
Second, a slightly weaker version of the DP guarantee with
increased privacy loss, but with no constraints on the query
class, which is useful when considering colluding queriers.
Theorem 1 (Individual DP guarantee). Fix a set of public
events 𝑃 ⊂ I∪C , and budget capacities (𝜖𝐺 𝑑)𝑑∈D . Case
1: If all the queries use attribution functions 𝐴 satisfying
∀𝑖,∀𝐹, 𝐴(𝐹1, ...,𝐹𝑖−1,𝐹𝑖∩𝑃,𝐹𝑖+1, ...,𝐹𝑘) =𝐴(𝐹1, ...,𝐹𝑖−1,∅,𝐹𝑖,
...,𝐹𝑘), then for𝑥∈X on device𝑑, Cookie Monster satisfies
individual device-epoch𝜖𝐺 𝑑 -DP for𝑥 under public informa-
tion 𝑃. Case 2: For general attribution functions, Cookie
Monster satisfies individual device-epoch 2𝜖𝐺 𝑑 -DP for𝑥 un-
der public information𝑃.
2While referred to as Personalized Differential Privacy (PDP) in some papers
[13], we use the term Individual Differential Privacy (IDP), as it better reflects
the concept and aligns with individual sensitivity, the basis of the definition.
This recent paper [14] also uses IDP terminology.
9

Intuitively, the information gained on cross-site (private
to the querier) events in device-epoch𝑥 under the querier’s
queries is bounded by𝜖𝐺 𝑥 (or 2𝜖𝐺 𝑥 without query constraints).
Theorem 2 (Unlinkability guarantee). Fix budget capac-
ities(𝜖𝐺 𝑑)𝑑∈D . Take any 𝑑0,𝑑 1 ∈ D,𝑒 ∈ E, and 𝐹1 ⊂ 𝐹0.
Denote 𝑥0 := (𝑑0,𝑒,𝐹 0),𝑥 1 := (𝑑1,𝑒,𝐹 1),𝑥 2 := (𝑑0,𝑒,𝐹 0\
𝐹1) ∈ X. For any 𝐷,𝐷′ ∈ D such that{𝐷,𝐷′} = {𝐷0+
𝑥0,𝐷 0+𝑥1+𝑥2} for some𝐷0∈ D, instantiationM of Cookie
Monster, and𝑆 ⊂ 𝑅𝑎𝑛𝑔𝑒(M) we have: Pr[M(𝐷) ∈𝑆] ≤
𝑒2𝜖𝐺 𝑑0+𝜖𝐺 𝑑1 Pr[M(𝐷′)∈ 𝑆].
Intuitively, linking a set of events across two devices—
compared to detecting these events on one device—is only
made easier by the amount of budget on the second device;
Cookie Monster does not introduce additional privacy loss
for linkability, above what is revealed through DP queries.
4.3 IDP Optimizations
IDP allows discounting the DP budget based on individual
sensitivity, which is never greater but often smaller than global
sensitivity. The easiest way to grasp this opportunity is to vi-
sualize and compare the definitions of global and individual
sensitivities for reports and queries. Recall that Cookie Mon-
ster enforces a bound on reports by capping each coordinate
in the attribution function’s output to a querier-provided max-
imum. Given this cap, we prove the following formulas for
both sensitivities (proofs in Appendix §E):
Theorem 3 (Global sensitivity of reports and queries).
Fix a report identifier𝑟, a device𝑑𝑟 , a set of epochs 𝐸𝑟 , an
attribution function𝐴 and the corresponding report𝜌 :𝐷↦→
𝐴(𝐷𝐸𝑟 𝑑𝑟 ). We have:
Δ(𝜌) = max∥𝐴(𝐹1, ...,𝐹𝑘)
𝑖∈[𝑘],𝐹1,...,𝐹𝑘∈P(I∪C)
−𝐴(𝐹1, ...,𝐹𝑖−1,∅,𝐹𝑖+1, ...,𝐹𝑘)∥ 1
Next, fix a query 𝑄 with reports(𝜌𝑟)𝑟∈𝑅 such that each
device-epoch participates in at most one report. We have
Δ(𝑄) = max𝑟∈𝑅 Δ(𝜌𝑟).
Theorem 4 (Individual sensitivity of reports and queries).
Fix a device-epoch record 𝑥 =(𝑑,𝑒,𝐹 ) ∈X. Fix a report
identifier𝑟, a device 𝑑𝑟 , a set of epochs 𝐸𝑟 ={𝑒1,...,𝑒 𝑘},
an attribution function 𝐴 with relevant events 𝐹𝐴, and the
corresponding report𝜌 :𝐷↦→𝐴(𝐷𝐸𝑟 𝑑𝑟 ).
We have: Δ𝑥(𝜌) = max∥𝐴(𝐹1, ...,𝐹𝑖−1,𝐹,
𝐹1,...,𝐹𝑖−1,𝐹𝑖+1,...,𝐹𝑘∈P(I∪C)
𝐹𝑖+1, ...,𝐹𝑘)−
𝐴(𝐹1, ...,𝐹𝑖−1,∅,𝐹𝑖+1, ...,𝐹𝑘)∥ 1 if𝑑 =𝑑𝑟 and𝑒 =𝑒𝑖∈ 𝐸𝑟 , and
Δ𝑥(𝜌) = 0 otherwise.
In particular,
Δ𝑥(𝜌)≤
 

0 if𝑑 =𝑑𝑟,𝑒∈𝐸𝑟 and𝐹∩𝐹𝐴 =∅
∥𝐴(𝐹)− 𝐴(∅)∥ 1 if𝑑 =𝑑𝑟 and𝐸𝑟 ={𝑒}
Δ(𝜌) if𝑑 =𝑑𝑟,𝑒∈𝐸𝑟 and𝐹∩𝐹𝐴 ≠∅
Next, fix a query 𝑄 with reports(𝜌𝑟)𝑟∈𝑅. Then we have:
Δ𝑥(𝑄)≤ ˝ 𝑟∈𝑅 Δ𝑥(𝜌𝑟). In particular, if𝑥 participates in at
most one report𝜌𝑟 , then: Δ𝑥(𝑄) = Δ𝑥(𝜌𝑟).
This theorem justifies both the inherent optimization used
by all on-device systems and the new optimizations added in
Cookie Monster.
Inherent on-device optimization. The condition𝑑 =𝑑𝑟 in
Thm. 4 explains why, under IDP, on-device budgeting systems
deduct privacy loss only for devices that participate in a query.
This is more efficient than off-device systems like IPA, which,
under traditional DP, must deduct budget based onΔ(𝑄) from
all devices, regardless of their participation (Thm. 3).
New optimization examples. First, devices that participate
in a query but have no relevant data ( i.e., 𝐹∩𝐹𝐴 = ∅ or
𝐴(𝐹) =𝐴(∅) in Thm. 4) do not incur budget loss. This is why,
in the example from § 3.2, we don’t deduct from epoch 𝑒3,
which has no Nike impressions. Second, a device’s individual
sensitivity depends only on reports it participates in (Δ𝑥(𝑄) =
Δ𝑥(𝜌𝑟)), whereas global sensitivity depends on all reports in
the query ( Δ(𝑄) = max𝑟∈𝑅 Δ(𝜌𝑟)). For instance, since the
report𝜌 typically depends on the public information 𝐹∩𝑃
of a record(𝑑,𝑒,𝐹 ), we use a $70 cap instead of $100 in the
Nike example. Third, if an attribution spans only one epoch
(or is broken into single-epoch reports), individual sensitivity
can be further reduced based on the private information 𝐹.
For example, if Nike measures the average impression-to-
conversion delay (0 to 7 days) in a single epoch and a record
𝑥 has one impression only 1 day before the conversion, its
individual budget will be 1/7th of the global budget.
5 Chrome Prototype
We integrated Cookie Monster into Google Chrome by modi-
fying ARA. We disabled ARA’s impression-level budgeting,
added epoch support, and extended ARA’s database to in-
clude a table for privacy filters for each epoch-querier pair.
Unlike ARA, which supports only last-touch attribution and
fetches only the latest impression, our implementation re-
trieves all impressions related to the conversion, groups them
by epoch, and identifies epochs with no relevant data to avoid
unnecessary budget consumption.
6 Evaluation
We seek to answer three key questions:
Q1: How do optimizations impact budget consumption?
Q2: How do optimizations impact query accuracy?
Q3: How effective is bias measurement?
We also evaluate Cookie Monster’s runtime overhead, but
provide these results in Appendix B as they are not vital to
our main hypotheses in this paper.
6.1 Methodology
We evaluate Cookie Monster on three datasets—a microbench-
mark and two realistic advertising datasets from PATCG and
Criteo—and compare its privacy budget consumption and
query accuracy against two baselines. The first baseline is
IPA-like, our own prototype implementing IPA’s centralized
budgeting and query execution. The second is ARA-like,
10

a version of ARA providing device-epoch-level guarantees.
ARA-like includes the inherent optimization of all on-device
systems but excludes the new optimizations in §4.3.
Scenario-driven methodology.We conduct our evaluation by
enacting the scenario from §2.1. An advertiser (Nike) runs ad
campaigns and repeatedly measures their efficacy. Each time
a customer purchases quantity𝐶 of a product, Nike requests
an attribution report, specifying the relevant ad campaigns.
Nike requests reports over some attribution window and uses
last-touch attribution. If no relevant impression is found, the
report value is 0; otherwise, it is𝐶. Nike batches reports and
submits them to the aggregation service for a DP summation
query using the Laplace mechanism. In our experiments, Nike
repeatedly performs queries on report batches of size𝐵, which
varies by dataset. Once𝐵 reports are gathered, Nike runs its
query. This is repeated over time as more batches of𝐵 reports
are gathered. This is also repeated for each product, e.g., 10 in
the microbenchmark/PATCG and a variable number in Criteo.
When requesting an attribution report for a conversion,
Nike must specify the requested privacy budget,𝜖 – the same
value for all reports in a batch. Since the MPC uses the
Laplace mechanism to ensure𝜖-DP, Nike selects𝜖 to achieve
acceptable accuracy. We assume Nike chooses𝜖 in an attempt
to keep query error within 5% (𝛼 = 0.05) of the true value with
99% probability (𝛽 = 0.01), which corresponds to roughly
0.02 RMSRE. The formula for𝜖 is:𝜖 = Δ ln(1/𝛽)/(𝛼·𝐵· ˜𝑐),
where Δ is the maximum value for𝐶 and ˜𝑐 is Nike’s rough
estimate of the average𝐶.
Our specific method is: we run repeated, single-advertiser
summation queries on fixed-size batches of attribution reports,
using last-touch attribution and a privacy budget calibrated as
described above. Default parameters include: a 7-day epoch
size, a 30-day attribution window, and a global privacy budget
per epoch of𝜖𝐺 = 1.
Microbenchmark dataset. To methodically evaluate Cookie
Monster, under a range of conditions, more or less favorable
to our optimizations, we create a synthetic dataset with 40,000
conversions across 10 products over 120 days. We expose two
knobs: Knob1, the user participation rate per query, deter-
mines the fraction of users who are assigned conversions rele-
vant for a particular query;Knob2, the number of impressions
per user per day. These knobs impact budget allocation across
IPA-like, ARA-like, and Cookie Monster. Lower Knob1 in-
creases opportunities for fine-grained accounting in ARA-like
and Cookie Monster. Lower Knob2 allows Cookie Monster
to conserve privacy by not deducting from epochs with no
relevant impressions, a key optimization over ARA-like.
PATCG dataset.To evaluate Cookie Monster under more re-
alistic conditions, we resort to the PATCG and Criteo datasets.
PATCG is a synthetic dataset released by the namesake W3C
community group [31], which contains 24M conversions from
a single advertiser over 30 days. This dataset represents a
large advertiser, with only 1% of conversions attributed to
impressions. There are 16M distinct users, and each user sees
an average of 3.2 impressions. Users who convert take part in
1.5 conversions on average.
Criteo dataset. The Criteo dataset [41] is sampled from a
90-day log of live ad impressions and conversions recorded
by the Criteo ad-tech. The dataset includes data from 292 ad-
vertisers with 12M impression records and 1.3M conversion
records. There are 10M unique users. The dataset provides op-
portunities for evaluating Cookie Monster in some additional
dimensions compared to PATCG and the microbenchmark.
In particular, the Criteo dataset contains data from multiple
advertisers of widely distinct sizes, i.e., having a wide range
in terms of number of impressions (1–2.6M impressions) and
conversions per advertiser (0–478k conversions). However,
since the dataset is heavily subsampled, missing many im-
pressions, we also evaluate Cookie Monster on augmented
versions of this dataset, in which we add synthetic impres-
sions to compensate for the missing impressions that might
otherwise favor Cookie Monster ’s optimizations.
6.2 Microbenchmark Evaluation (Q1)
We use the microbenchmark to evaluate the impact of individual-
sensitivity optimizations on privacy budget consumption across
a range of controlled workloads (question Q1).
Varying user participation rate per query (knob1). We
first vary the user participation rate per query. With a default
batch size of 2,000 reports and 10 products (queried twice,
totaling 20 queries), we create 40,000 conversions. Knob1
controls how these conversions are assigned to users, indi-
rectly determining the total number of users. A lower knob1
favors on-device budgeting, as it spreads the 40,000 conver-
sions across more users, creating more privacy filters for the
advertiser. For example, with knob1 = 1, each user partici-
pates in all 20 query batches, requiring a minimum of 2,000
users, while knob1 = 0.001 generates 2M users. In the PATCG
dataset, users convert with a 0.05 daily rate, corresponding to
knob1 = 0.1, which we use as default in other experiments.
Fig. 4a and 4b show the average and maximum budget
consumption across all device-epochs requested through the
20 queries. Qualitatively, the average budget consumption
is a much more useful metric to assess the efficiency of the
three systems, but we include the maximum because it re-
duces IDP guarantees to standard DP guarantees, thereby
providing a more apples-to-apples comparison between on-
device and off-device budgeting. Recall that IPA-like does not
distribute budget consumption across devices but has a cen-
tralized privacy filter for each epoch, from which it deducts
budget upon executing each query. As a result, increasing user
participation per query (knob1) does not impact its budget
consumption, which is always higher than the other methods’.
Cookie Monster consistently consumes the least budget due
to its optimizations, with greater improvements as user par-
ticipation increases (lower knob1), since more device-epochs
11

0.001 0.01 0.1 1.0
5
0.01
2
5
0.1
2
5
0.001 0.01 0.1 1.0
0
0.2
0.4
0.6
0.8
0.001 0.01 0.1 1.0
2
5
0.01
2
5
0.1
2
5
0.001 0.01 0.1 1.0
0
0.2
0.4
0.6
0.8
Cookie Monster
 ARA-like (on-device)
 IPA-like (off-device)
fraction of users per query fraction of users per query user impressions per day user impressions per day
avg. budget (log)
max budget
avg. budget (log)
max budget
(a) Avg. budget varying knob1 (b) Max. budget varying knob1 (c) Avg. budget varying knob2 (d) Max. budget varying knob2
Fig. 4. Budget consumption on the microbenchmark. (a) and (b) show average and maximum budget consumption across all device-epochs, respectively, as
a function of the fraction of users that participate per query (knob1); value of knob2 is constant 0.1. (c) and (d) show the same metrics as a function of user
impressions per day (knob2); value of knob1 is constant 0.1.
lack relevant impressions and don’t deduct budget. Even un-
der the max budget metric, on-device systems outperform
IPA-like, with Cookie Monster being the most efficient.
Varying the number of impressions per user per day
(knob2). We now fix knob1 at 0.1 and vary the number of
impressions per user per day (knob2). In PATCG, users see an
average of 3.22 ads over 30 days, giving knob2 a value of 0.1.
Fig. 4c and 4d confirm that Cookie Monster’s optimizations
are most effective when users have fewer impressions.
Thus, Cookie Monster reduces budget consumption com-
pared to baselines, especially when budget is spread across
many users and when users have fewer impressions.
6.3 PATCG Evaluation (Q1, Q2)
We use the PATCG dataset to evaluate Cookie Monster’s
impact on budget consumption (Q1) and query accuracy (Q2).
This dataset links impressions and conversions to attributes,
with values uniformly sampled from 0 to 9, representing 10
potential products. Nike queries each product eight times
over the four months spanning the dataset, totaling 80 queries
with batch sizes between 280,000 and 303,009 reports. Large
batch sizes accommodate the low attribution rate (1% of
impressions relevant to conversions), assuming Nike adjusts
batch sizes accordingly.
Fig. 5a illustrates the average privacy budget consumed
by each system as 80 queries are submitted for execution
by the advertiser. The x-axis represents the order of queries,
with points indicating budget consumption. IPA-like executes
only a small fraction of queries (3.75%) due to its coarse-
grained, population-level accounting, leading to early budget
depletion. ARA-like and Cookie Monster, with finer-grained,
individual-level accounting, execute all queries and resulting
in smoother and lower average budget consumption. Cookie
Monster shows up to 206 times lower average budget con-
sumption compared to ARA-like, highlighting the benefits of
its individual-sensitivity optimizations.
Next, we assess query accuracy (Q2). On-device systems
(ARA-like and Cookie Monster) hide budgets when depleted,
which can affect query accuracy, while IPA-like explicitly
rejects queries with exhausted budgets. As in our experiments,
privacy budgets are set to aim for high accuracy in the Laplace
mechanism, we expect IPA’s executed queries to have errors
within the 0.02 mark. In contrast, ARA and Cookie Monster
may incur additional errors when epochs run out of budget,
leading to nullified or incomplete reports.
Fig. 5b shows the CDF of root mean square relative er-
ror (RMSRE), defined as
√︁
E[(M(𝐷)− 𝑄(𝐷)) 2/𝑄(𝐷)2] for
an estimateM(𝐷) of the query output 𝑄(𝐷). This metric
captures both Laplace-induced and IDP-bias-induced errors.
The CDF shows query errors for each system. IPA-like’s
line ends at 3.75% of queries, aligning with its budget con-
straints but maintaining within the 5% error mark. Cookie
Monster consistently exhibits lower errors than ARA-like due
to its budget conservation, resulting in fewer nullified reports
and reduced bias. This is true without any bias mitigation
strategies. In §6.5, we show that even with bias measurement
running alongside every query, Cookie Monster still outper-
forms ARA-like (which has no bias measurement) in terms
of budget consumption and query accuracy.
Finally, we explore how epoch length affects performance.
Longer epochs strengthen device-epoch privacy guarantees
but slow budget refreshing, leading to more query rejections
in IPA and increased bias in on-device systems without miti-
gation. Fig. 5c evaluates RMSRE measures (median, first and
third quartiles, and range) as epoch length varies. IPA-like’s
query execution drops to 1.25% at one-month epochs, while
Cookie Monster and ARA-like complete all queries but with
increasing errors. Cookie Monster’s budget conservation re-
sults in fewer altered or nullified reports, maintaining lower
error degradation compared to ARA-like as epochs grow.
6.4 Criteo Evaluation (Q1, Q2)
The Criteo dataset enables evaluation across diverse adver-
tisers. It includes 1.3M conversions from 292 advertisers,
with conversions ranging from 0 to 478k per advertiser. To
achieve meaningful accuracy under DP, an advertiser needs
a minimum number of reports. We set this minimum to 350,
allowing us to formulate at least one query for 109 adver-
tisers. Advertisers with more than 350 conversions wait to
accumulate 350 reports per batch for each query, resulting
in 898 queries across these advertisers using the attribute
“product-category-3” as a product ID.
12

(a) Avg. budget consumed across all device-epochs (b) CDF of RMSRE (c) RMSRE as a function of epoch length
Fig. 5. Budget consumption and query accuracy on the PATCG dataset. (a) Average budget consumption across all device-epochs as a function of the
number of queries submitted by the advertiser. (b) CDF of RMSRE with a 7-day epoch. (c) RMSRE median (horizontal lines), first and third quartiles (boxes),
and max/min (top/bottom range markers) as epoch length increases.
(a) CDF of budget on Criteo. (b) CDF of RMSRE. (c) RMSRE as function of epoch length. (d) CDF of budget on Criteo++.
Fig. 6. Budget consumption and query accuracy on Criteo. (a) CDF of per-device average budget consumption across epochs for all devices and advertisers.
(b) CDF of RMSREs for a 7-day epoch. (c) RMSRE metrics with varying epoch length (see Fig. 5c for format). (d) The same CDF as in (a), but for the Criteo++,
showing the impact of synthetic impression augmentation on Cookie Monster’s performance.
Fig. 6a shows a CDF of per-device average budget con-
sumption across epochs, where the distribution covers all de-
vices and all advertisers; that is, there is a single data point cor-
responding to each device and advertiser pair, which indicates
the average consumption across epochs within an advertiser’s
filters on a given device by the end of the workload. Lower
values indicate better performance. Cookie Monster conserves
the most privacy budget, with 95% of device-advertiser pairs
having more capacity left compared to both baselines.
Fig. 6b presents the CDF of RMSREs for all 898 queries.
IPA-like completes only a small fraction of queries but with
good accuracy. ARA-like and Cookie Monster accept all
queries, potentially at the expense of higher error; however,
Cookie Monster’s error distribution remains better than ARA-
like’s, with errors within IPA-like’s range for up to 96% of
queries. This results from Cookie Monster’s optimizations
that conserve budget and avoid introducing bias.
Fig. 6c examines how RMSRE varies with epoch length.
Longer epochs increase contention on per-epoch filters. De-
spite this, Cookie Monster’s optimizations show substantial
benefits, with minimal RMSRE increase (25% increase from
1-day to 60-day epoch for median RMSRE). Although maxi-
mum RMSRE increases with epoch length, Cookie Monster’s
performance remains superior to ARA-like.
Recall that the Criteo dataset is heavily subsampled, so
there is the possibility that missing impressions may amplify
the benefit of our optimizations. To assess Cookie Monster’s
performance in scenarios with more relevant impressions,
we augment the Criteo dataset with synthetic impressions
for each conversion. The results, shown in Fig. 6d, compare
the CDFs of budget consumption with varying augmentation
levels. The behavior of IPA-like and ARA-like remains un-
changed by augmentation, as they do not optimize for missing
relevant impressions. For Cookie Monster, budget efficiency
decreases as more synthetic impressions are added, approach-
ing ARA-like’s performance at 9 extra impressions per con-
version. The impressions are uniformly distributed across the
attribution window, ensuring that most epochs have relevant
impressions for most conversions, so Cookie Monster’s opti-
mization is eliminated and its behavior follows ARA-like’s.
6.5 Bias Measurement (Q3)
We evaluate Cookie Monster’s bias measurement technique
using our microbenchmark with default knob settings (0.1)
and an increased query load to measure significant bias. Specif-
ically, we use 60 days and repeat each query 40 times.
Fig. 7a shows the budget overhead incurred by bias mea-
surement. The bias measurement’s counts are scaled to have
10% the sensitivity of the original query, so the overall sensi-
tivity of the query/side-query combination increases by 10%.
The average consumed budget goes from 0.36 without bias
measurement to 0.43 with bias measurement; this is more
than a 10% increase since some epochs that originally paid
zero budget through our IDP optimization, now pay for bias
counts.
Fig. 7b shows the CDF of RMSREs across all 400 queries,
with a log scale on the y-axis to highlight smaller differences
13

0
0.2
0.4
0.6
0.8
1
20 40 60 80 100
0.01
2
5
0.1
2
5
1
2
5%
100%
100%
11% 30%
38% 48%
 N/A   0.02 0.05 0.1 0.2
0.01
2
5
0.1
2
5
1
2
IPA-like (oﬀ-device) ARA-like (on-device) Cookie Monster w/o bias measurement Cookie Monster w/ bias measurement
Cookie Monster w/ bias measurement (estimation of error)
% of queries Error estimation cutoﬀ
avg. budget
RMSRE query error (log)
RMSRE query error (log)
(a) Avg. budget consumed (b) CDF of RMSRE (c) RMSRE as function of error estimation cutoff.
Fig. 7. Budget consumption and query accuracy with bias measurement on the microbenchmark. (a) Average budget consumed across all device-epochs.
(b) CDF of true RMSRE for executed queries, alongside Cookie Monster’s RMSRE estimation from bias measurement (light-purple line). (c) Quartiles of true
RMSRE, where queries with error estimate above a given cutoff are rejected by Cookie Monster with bias measurement.
among Cookie Monster variants compared to ARA. Due to
the heavy query load, IPA executes only 5% of the queries
and ARA ultimately returns empty reports, resulting in a
relative error of 1. Cookie Monster without bias measurement
plateaus at 0.2 error. Cookie Monster with bias measurement
shows a similar trend to Cookie Monster without it, albeit
with increased error, because the higher sensitivity of the
query leads additional epochs to run out of budget. However,
the bias measurements let queriers compute an estimate of
the error, which, although noisy (as it is also differentially
private), generally serves as an upper bound on true RMSRE.
Queriers can compare this estimate to a predetermined cutoff
and reject queries exceeding it. Fig. 7c displays the quartiles
of true RMSREs after rejecting queries based on estimated
RMSRE cutoffs. For instance, using a cutoff of 0.05 enables
queriers to limit bias, achieving a maximum error of 0.04
(down from 0.21), but only accepting 30% of the queries.
Rejected queries still consume budget, as rejection is a post-
processing step.
Thus, even with rudimentary bias measurement, Cookie
Monster offers substantial benefits over IPA while maintain-
ing lower real error than ARA. While we validated our tech-
nique on a microbenchmark with increased query load, apply-
ing it to real-life datasets remains an open challenge. Future
work could enhance our technique by scheduling bias mea-
surements or using DP threshold comparison mechanisms.
7 Related Work
DP systems. Most DP systems operate in the centralized-
DP model, where a trusted curator runs queries using global
sensitivity [12]. Some implement fine-grained accounting
through parallel composition [29, 26, 27, 25], a coarse form
of individual DP (IDP) that lacks optimizations like those
in Cookie Monster. Others function in the local-DP model,
where devices randomize their data locally [23], and there-
fore inherently do on-device budgeting but have higher utility
costs. Distributed systems like [38, 28] emulate the central
model with cryptographic constructions; like IPA, they main-
tain a single privacy filter, not leveraging IDP to conserve
budget. [4] uses the shuffle model [7] to combine local ran-
domization with a minimal trusted party. Cookie Monster
operates in the central model with on-device budgeting and
uses an IDP formalization to enable new optimizations.
Private ads measurement. Several proposals exist for pri-
vate ad measurement systems. Apple’s PCM [22] relies on
entropy limits for privacy. Meta and Mozilla’s IPA [5] uses
centralized budgeting, while Google’s ARA [3] and Apple’s
PAM [34] utilize on-device budgeting. ARA has primarily
focused on optimizing in-query budget and utility. [10] opti-
mizes a single vector-valued hierarchical query, whereas [1]
assumes a simplified ARA with off-device impression-level
DP guarantees, efficiently bounding each impression’s con-
tribution for queries known upfront. [11] offers a framework
for attribution logic and DP neighborhood relations, propos-
ing clipping strategies for bounding global sensitivity. Our
work optimizes on-device budgeting across queries, using
tighter individual sensitivity bounds. Our method is agnostic
to how these bounds are enforced, potentially benefiting from
clipping algorithms [10, 1, 11].
IDP was introduced in the centralized-DP setting, where
a trusted curator manages individual budgets and leverages
individual sensitivity to optimize privacy accounting [13, 14].
IDP is used for SQL-like queries and gradient descent. The
literature emphasizes the need to keep individual budgets
private. [45] studies the release of DP aggregates over these
budgets while [13] notes that out-of-budget records must be
dropped silently, leaving bias analysis for future work.
8 Conclusion
Web advertising is at a crossroads, with a unique opportunity
to enhance online privacy through new, privacy-preserving
APIs from major browser vendors. We show that a novel
individual DP formulation can significantly improve privacy
budgeting in on-device systems. However, further progress is
needed in query support, error management, and scalability.
Our paper provides foundational insights and formal analysis
to guide future research and industry collaboration.
Acknowledgements
We thank the anonymous reviewers for their constructive
feedback and the Meta and Mozilla IPA teams, particularly
Ben Savage and Martin Thompson, for their ongoing input.
14

Special thanks to PATCG participants, especially Luke Win-
strom, for their feedback on early proposals. This work was
supported by NSF grants EEC-2133516, CNS-2106530, CNS-
2104292, NSERC RGPIN-2022-04469, Google, Microsoft,
Sloan Faculty Fellowships, and an Onassis Foundation Schol-
arship. Co-author Geambasu was partially employed by Meta
during this project.
References
[1] Hidayet Aksu et al. Summary Reports Optimization
in the Privacy Sandbox Attribution Reporting API .
Nov. 22, 2023. arXiv: 2311.13586 [cs].
[2] Apple, Inc. Apple announces powerful new privacy
and security features . https : / / www. apple . com /
newsroom/2023/06/apple-announces-powerful-
new-privacy-and-security-features/ . 2023.
[3] Attribution Reporting API (ARA)) . https : / / github.
com/WICG/attribution-reporting-api/blob/main/
AGGREGATE.md. 2022.
[4] Andrea Bittau et al. “Prochlo: Strong Privacy for Ana-
lytics in the Crowd”. In: Proceedings of the 26th Sym-
posium on Operating Systems Principles. SOSP ’17.
Shanghai, China: Association for Computing Machin-
ery, 2017, pp. 441–459. ISBN : 9781450350853. DOI:
10.1145/3132747.3132769. URL: https://doi.org/
10.1145/3132747.3132769.
[5] Benjamin Case et al. Interoperable Private Attribution:
A Distributed Attribution and Aggregation Protocol .
Cryptology ePrint Archive, Paper 2023/437. https :
//eprint.iacr.org/2023/437. 2023. URL: https://eprint.
iacr.org/2023/437.
[6] Anthony Chavez. A new path for Privacy Sandbox on
the web. https://privacysandbox.com/news/privacy-
sandbox-update/. 2024.
[7] Albert Cheu et al. “Distributed Differential Privacy
via Shuffling”. In: Advances in Cryptology – EURO-
CRYPT 2019 . Ed. by Yuval Ishai and Vincent Rij-
men. Cham: Springer International Publishing, 2019,
pp. 375–403. ISBN : 978-3-030-17653-2.
[8] Google Chrome. Federated Learning of Cohorts (FLoC).
https://privacysandbox.com/proposals/floc/.
[9] Google Chrome. Protected Audience API overview .
https://developers.google.com/privacy-sandbox/
relevance/protected-audience.
[10] Matthew Dawson et al.Optimizing Hierarchical Queries
for the Attribution Reporting API. Comment: Appeared
at AdKDD 2023 workshop; Final proceedings version.
Nov. 27, 2023. arXiv: 2308.13510 [cs].
[11] John Delaney et al. Differentially Private Ad Conver-
sion Measurement. 2024. arXiv:2403.15224 [cs.CR].
[12] Cynthia Dwork and Aaron Roth. “The Algorithmic
Foundations of Differential Privacy”. In: Foundations
and Trends® in Theoretical Computer Science 9.3-4
(2013), pp. 211–407. ISSN : 1551-305X, 1551-3068.
DOI: 10.1561/0400000042.
[13] Hamid Ebadi, David Sands, and Gerardo Schneider.
“Differential Privacy: Now It’s Getting Personal”. In:
Proceedings of the 42nd Annual ACM SIGPLAN -
SIGACT Symposium on Principles of Programming
Languages. POPL ’15: The 42nd Annual ACM SIG-
PLAN SIGACT Symposium on Principles of Program-
ming Languages. Mumbai India: ACM, Jan. 14, 2015,
pp. 69–81. ISBN : 978-1-4503-3300-9. DOI: 10.1145/
2676726.2677005.
[14] Vitaly Feldman and Tijana Zrnic. “Individual Privacy
Accounting via a Rényi Filter”. In:Advances in Neural
Information Processing Systems. Ed. by M. Ranzato et
al. V ol. 34. Curran Associates, Inc., 2021, pp. 28080–
28091.
[15] Badih Ghazi et al. “Deep Learning with Label Differ-
ential Privacy”. In: Advances in Neural Information
Processing Systems. V ol. 34. Curran Associates, Inc.,
2021, pp. 27131–27145.
[16] Google. Attribution Reporting API with Aggregatable
Reports. https : / / github. com / WICG / attribution -
reporting - api / blob / main / AGGREGATE . md #
contribution-bounding-and-budgeting/. 2024.
[17] Google’s FLoC Is a Terrible Idea. https://www.eff.
org/deeplinks/2021/03/googles-floc-terrible-idea .
2021.
[18] Hybrid Proposal. https://github.com/patcg-individual-
drafts/hybrid-proposal. 2024.
[19] iCloud Private Relay Overview. https://www.apple.
com/icloud/docs/iCloud_Private_Relay_Overview_
Dec2021.pdf. 2021.
[20] Intelligent Tracking Prevention 2.3. https://webkit.
org/blog/9521/intelligent-tracking-prevention-2-
3/. 2019.
[21] Interoperable Private Attribution (IPA)). https://github.
com/patcg-individual-drafts/ipa. 2022.
[22] Introducing Private Click Measurement, PCM. https:
//webkit.org/blog/11529/introducing-private-click-
measurement-pcm/. 2021.
[23] Shiva Prasad Kasiviswanathan et al. “What Can We
Learn Privately?” In:SIAM Journal on Computing40.3
(2011), pp. 793–826. DOI: 10.1137/090756090. URL:
https://doi.org/10.1137/090756090.
[24] Daniel Kifer et al.Guidelines for Implementing and Au-
diting Differentially Private Systems. Tech. rep. 2020.
[25] Nicolas Küchler et al. “Cohere: Privacy Management
in Large Scale Systems”. In: CoRR abs/2301.08517
(2023). DOI: 10.48550/ARXIV.2301.08517. arXiv:
2301.08517. URL: https://doi.org/10.48550/arXiv.
2301.08517.
[26] Mathias Lecuyer et al. “Privacy Accounting and Qual-
ity Control in the Sage Differentially Private Machine
15

Learning Platform”. In: Proceedings of the ACM Sym-
posium on Operating Systems Principles (SOSP). 2019.
[27] Tao Luo et al. “Privacy Budget Scheduling”. In:15th
USENIX Symposium on Operating Systems Design
and Implementation (OSDI 21) . USENIX Associa-
tion, July 2021, pp. 55–74. ISBN : 978-1-939133-22-9.
URL: https://www.usenix.org/conference/osdi21/
presentation/luo.
[28] Elizabeth Margolin et al. “Arboretum: A Planner for
Large-Scale Federated Analytics with Differential Pri-
vacy”. In: Proceedings of the 29th Symposium on Op-
erating Systems Principles. SOSP ’23. , Koblenz, Ger-
many, Association for Computing Machinery, 2023,
pp. 451–465. ISBN : 9798400702297. DOI: 10.1145/
3600006.3624566. URL: https://doi.org/10.1145/
3600006.3624566.
[29] Frank D. McSherry. “Privacy Integrated Queries: An
Extensible Platform for Privacy-Preserving Data Anal-
ysis”. In: Proceedings of the 2009 ACM SIGMOD In-
ternational Conference on Management of Data. SIG-
MOD ’09. New York, NY , USA: Association for Com-
puting Machinery, June 29, 2009, pp. 19–30. ISBN :
978-1-60558-551-2. DOI: 10.1145/1559845.1559850.
[30] Over a decade of anti-tracking work at Mozilla. https:
//blog.mozilla.org/en/privacy-security/mozilla-
anti-tracking-milestones-timeline/. 2022.
[31] PATCG Attribution Synthetic Data . https : / / docs .
google.com/document/d/1Vxq4LrMe3A2WIlu-
7IYP1Hycr_nz3_qTpPAICX9fLcw. 2024.
[32] Privacy Preserving Ad Click Attribution For the Web.
https://webkit.org/blog/8943/privacy-preserving-
ad-click-attribution-for-the-web/ . 2019.
[33] Privacy-Preserving Attribution: Level 1. https://private-
attribution.github.io/api/. 2024.
[34] Private Ad Measurement (PAM). https://github.com/
patcg-individual-drafts/private-ad-measurement .
2023.
[35] Private Advertising Technology Community Group .
https://www.w3.org/community/patcg. 2024.
[36] Ryan Rogers et al. “Privacy odometers and filters: pay-
as-you-go composition”. In:Proceedings of the 30th In-
ternational Conference on Neural Information Process-
ing Systems. NIPS’16. Barcelona, Spain: Curran Asso-
ciates Inc., 2016, pp. 1929–1937.ISBN : 9781510838819.
[37] Ryan M Rogers et al. “Privacy Odometers and Filters:
Pay-as-you-go Composition”. In: Advances in Neural
Information Processing Systems. Ed. by D. Lee et al.
V ol. 29. Curran Associates, Inc., 2016.
[38] Edo Roth et al. “Orchard: differentially private analyt-
ics at scale”. In: Proceedings of the 14th USENIX Con-
ference on Operating Systems Design and Implemen-
tation. OSDI’20. USA: USENIX Association, 2020.
ISBN : 978-1-939133-19-9.
[39] Google Privacy Sandbox.Privacy Sandbox for the Web.
https://privacysandbox.com/intl/en_us/open-web.
2023.
[40] Selenium. https://www.selenium.dev/. 2024.
[41] Marcelo Tallis and Pranjul Yadav. “Reacting to Varia-
tions in Product Demand: An Application for Conver-
sion Rate (CR) Prediction in Sponsored Search”. In:
arXiv preprint arXiv:1806.08211 (2018).
[42] Understanding Apple’s Private Click Measurement .
https://blog.mozilla.org/en/mozilla/understanding-
apples-private-click-measurement/. 2022.
[43] Salil Vadhan and Wanrong Zhang. “Concurrent Com-
position Theorems for Differential Privacy”. In: Pro-
ceedings of the 55th Annual ACM Symposium on The-
ory of Computing . STOC 2023. Orlando, FL, USA:
Association for Computing Machinery, 2023, pp. 507–
519. ISBN : 9781450399135. DOI: 10.1145/3564246.
3585241. URL: https://doi.org/10.1145/3564246.
3585241.
[44] Weighted Aggregate Logistic Regression. https://github.
com / patcg - individual - drafts / ipa / blob / main /
logistic_regression.md. 2024.
[45] Da Yu et al. “Individual Privacy Accounting for Dif-
ferentially Private Stochastic Gradient Descent”. In:
Transactions on Machine Learning Research (Apr. 27,
2023). ISSN : 2835-8856.
16

Note: This appendix has not been peer-reviewed.
A Additional Use Cases
Our scenario from §2.1 included the limited perspective of a
single advertiser, Nike. Correspondingly, our system execu-
tion example (§3.2) and formal-model instantiation example
(§4.1.3) focused only on Nike’s perspective. However, there
are many other players, with distinct perspectives, in the Web
advertising ecosystem, such as: first-party content providers
that are also advertising platforms, like Meta, which seek
to ad placement from multiple advertisers; and third-party
ad-techs like Criteo that seek to optimize ad placement across
many publishers and advertisers. In this section we discuss the
Meta perspective, which our theory can readily support. We
are still working on reasoning through the theory to support
an intermediary ad-tech perspective.
Ad-tech perspective.In addition to advertising on nytimes.com,
Nike also advertises on Meta, a content provider (a.k.a. pub-
lisher or ad-tech) that runs its own, in-house advertising plat-
form. Ann uses Meta’s facebook.com site to read posts related
to running and other interests. To show her the most relevant
ads, the site requires her to log into her account and then
tracks her activity within the site to build a profile of her
interests. Ann accepts that Meta learns about her interests as
she interacts with content on the site while logged into her
account; however, Ann expects Meta not to be tracking her
across other sites on the Web, and also to not be linking her
interactions as part of different accounts. For example, while
Meta may learn that Ann is passionate about running, and
hence may show her the Nike running-shoe ad, Meta should
not be able to tell whether Ann later buys the shoes, as that
conversion occurs on nike.com. Still, to maximize the effec-
tiveness of ads (and return on Nike’s ad spend), Meta needs
to be able to train a machine learning (ML) model that can
predict, given a user profile and a context, which ad coming
from which advertiser would be most effective to show, in
terms of maximizing the likelihood of an eventual conversion.
This model-training procedure can be thought of as bringing
together many attributions reports corresponding to impres-
sions that occur on one or more publishers (facebook.com
here, but also potentially instagram.com) and conversions that
occur on the many advertiser sites buying ads through Meta.
This type of multi-advertiser, optimization query is a second
class of queries that ad-measurement APIs aim to support
without exposing cross-site information and while limiting
within-site linkability (to meet expectations when the user
switches accounts).
Instantiation of ad-tech’s perspective (in formal system
model from §4.1). Meta is symmetric with Nike, on the
display side. The querier’s public information will be 𝑃 =
IMeta. In our scenario, Meta is interested in learning ML
models to better target ads to its users, using conversions as
a metric to optimize. To this end, Meta can learn a logistic
regression mapping public (to Meta) features from its users
and attributes of ads (together denoted 𝑋𝑑 for device𝑑), to
conversion labels. This is possible under Cookie Monster’s
queries by defining an attribution function𝐴 that returns𝑋𝑑
is there is a conversion, zero otherwise, and using algorithms
to fit logistic regressions under known features but private
labels [44].
B Cookie Monster Performance Overhead
We measure the performance overhead of Cookie Monster
compared to Google’s ARA. Cookie Monster iterates over all
impressions relevant to a conversion to identify which privacy
filters will consume budget, whereas ARA tracks only the
most recent impression. We compare two versions of Chrome
running Cookie Monster and ARA, using Selenium [40] to
interact with a publisher and generate impressions across
20 epochs. Varying the number of impressions from 10 to
100, we measure the time to create a report upon triggering a
conversion. ARA consistently reports at 5.4 ms, while Cookie
Monster’s reporting time increases linearly from 9.1 ms to
57.3 ms based on the number of impressions. This presents
a side channel that should be addressed in the future, such
as enforcing a constant runtime, to avoid revealing whether
relevant impressions were found on the device.
C Formal Model of Cookie Monster Algorithm
Alg. 1 describes the formal view of Cookie Monster, whose
privacy guarantees we establish in §4.2.4. Cookie Monster
answers a stream of the querier’s queries by generating re-
ports based on a device’s data in the queried epochs and
an attribution function 𝐴 passed in the query. It does so
while the querier still has available budget. The function
GenerateReport in Alg. 1 models this logic of privacy bud-
get checks and consumption, followed by report creation if
enough budget is available. The attribution function 𝐴 has
bounded sensitivity (defined in §4.2.3), enforced through clip-
ping. Function AnswerQuery then sums reports together to
compute the final query value. DP noise is added to the result
before returning it to the querier (see the output of Alg. 1).
The algorithm captures the fact that reports that do not con-
tribute to a query are not actually generated (the summation
is over𝑟∈𝑅). This is how all on-device systems inherently
work (not only Cookie Monster), and it’s an important opti-
mization that preserves privacy budget, as reports that are not
generated do not consume budget. Yet, as previously men-
tioned, it is very non-standard behavior for DP, so its privacy
justification, which we do in the next section, requires both
the formalization of reports with unique identifiers𝑟 and an
individual DP framework.
We instantiate the filter methods and the ComputeIndivid-
ualBudget function for the Laplace distribution in the next
section (§D).
17

Algorithm 1 Cookie Monster Algorithm
Config
Public events𝑃⊂I∪C
Parametrized noise distributionL
Device-epoch budget capacity(𝜖𝐺 𝑥)𝑥∈X
Input
Database𝐷
Stream of interactively chosen queries𝑄1,...,𝑄 𝑘
function Main(𝐷,𝑄 1,...,𝑄 𝑘)
𝑆 =∅
for(𝑑,𝑒,𝐹 )∈ 𝐷 do
for𝑓∈𝐹∩𝑃 do
Generate report identifier𝑟
$
←𝑈(Z)
Save mapping from𝑟 to the device that gener-
ated it:𝑑𝑟←𝑑
𝑆←𝑆∪{( 𝑟,𝑓 )}
output𝑆 // report identifiers and public events𝐷∩𝑃
for𝑖∈[ 𝑘] do
output AnswerQuery(𝑄𝑖)
// Collect, aggregate and noise reports to answer𝑄𝑖
function AnswerQuery(report identifiers𝑅, target epochs
(𝐸𝑟)𝑟∈𝑅, attribution functions(𝐴𝑟)𝑟∈𝑅 and noise parameter
𝜎)
for𝑟∈𝑅 do
𝜌𝑟← GenerateReport(𝑑𝑟,𝐸𝑟,𝐴𝑟)
Sample𝑋∼L( 𝜎)
return ˝ 𝑟∈𝑅𝜌𝑟+𝑋
// Generate report and update on-device budget
function GenerateReport(𝑑,𝐸,𝐴 )
for𝑒∈𝐸 do
𝑥←(𝑑,𝑒,𝐷 𝑒 𝑑)
ifF𝑥 is not defined then
Initialize filterF𝑥 with capacity𝜖𝐺 𝑥
𝜖𝑥← ComputeIndividualBudget(𝑥,𝑑,𝐸,𝐴, L,𝜎)
ifF𝑥. tryConsume(𝜖𝑥) =𝐻𝑎𝑙𝑡 then
𝐹𝑒←∅
else
𝐹𝑒←𝐷𝑒 𝑑
𝜌←𝐴((𝐹𝑒)𝑒∈𝐸) // Clipped attribution report
return𝜌
D Proofs of Privacy Guarantees (§4.2.4)
Filter and budget semantics for Laplace.In this section, we
focus on the Laplace noise distribution:L(𝜎) = Lap(𝜎/
√
2).
We use pure differential privacy accounting, hence the budgets
are real numbers 𝜖 > 0. To track the budget of adaptively
chosen queries, we use a Pure DP filter [36]. For a budget
capacity𝜖𝐺, this filter simply adds up the budget consumed
by the first𝑘 queries, and outputs Halt for the next query with
budget𝜖𝑘+1 if:
𝜖1+···+ 𝜖𝑘+𝜖𝑘+1 >𝜖𝐺 (3)
Finally, for a datapoint𝑥, a report𝜌 =(𝑑,𝐸,𝐴), the Laplace
distributionL and a standard deviation𝜎, we have:
ComputeIndividualBudget(𝑥,𝑑,𝐸,𝐴, L,𝜎) = Δ
√
2
𝜎 (4)
where Δ is an upper bound on the individual sensitivity of
the report Δ𝑥(𝜌). We provide such upper bounds in §4.3.
Finally, we use a slightly more general way of initializing
budget capacities, by setting one capacity for each possible
record(𝜖𝐺 𝑥)𝑥∈X . In the body of the paper we set the same
capacity for all the records belonging to the same device 𝑑:
(𝜖𝐺 𝑥)𝑑∈D . For practical purposes it is enough to set capacities
at the device level, but using per-record capacities simplifies
certain proofs, such as Thm. 7.
D.1 Individual DP Guarantees (Thm. 1)
To prove Thm. 1 from §4.2.4, we need to define an intermedi-
ary “inner" privacy game Alg. 2, which we analyze in Thm. 5.
Next, we define another “outer" privacy game Alg. 3, that is
a generalized version of Alg. 1 and internally calls Alg. 2.
Finally, Thm. 6 and Thm. 7 imply Thm. 1.
Theorem 5 (IDP of Alg. 2 when removing𝑥). Fix a device-
epoch budget capacity (𝜖𝐺 𝑥)𝑥∈X for every possible record
𝑥∈X . For any opt-out record𝑥∈X , for any adversaryA,
and𝑉 0,𝑉 1 defined by Alg. 2, for all𝑣∈ Supp(𝑉) we have:

ln  Pr[𝑉 0 =𝑣] Pr[𝑉 1 =𝑣] 

≤𝜖𝐺 𝑥 (5)
Proof. Fix an upper bound on the number of epochs and
queries per epoch𝑒max,𝑘 max. Fix an opt-out record
𝑥 =(𝑑0,𝑒 0,𝐹 0)∈X and an adversaryA. Take𝑉 0,𝑉 1 the view
ofA in Alg. 2. Consider a view𝑣∈ Supp(𝑉 1). We have:
ln
 Pr[𝑉 0 =𝑣]
Pr[𝑉 1 =𝑣]

= ln
 𝑒maxÖ
𝑒=1
𝑘maxÖ
𝑘=1
Pr[𝑉 0 𝑒,𝑘 =𝑣𝑒,𝑘|𝑣<𝑒,𝑘]
Pr[𝑉 1 𝑒,𝑘 =𝑣𝑒,𝑘|𝑣<𝑒,𝑘]
!
(6)
where, for𝑒∈[ 𝑒max],𝑘 ∈[ 𝑘max],𝑏∈{ 0, 1} and𝑣𝑒,𝑘 we
have:
Pr[𝑉𝑏 𝑒,𝑘 =𝑣𝑒,𝑘|𝑣<𝑒,𝑘]
= Pr[𝑉𝑏 𝑒,𝑘 =𝑣𝑒,𝑘|𝑉𝑏 1,1 =𝑣1,1,...,𝑉 𝑏 𝑒,𝑘−1 =𝑣𝑒,𝑘−1]
Even though data and query parameters are adaptively
chosen, they only depend on the adversary A (fixed) and
its previous views, which are fixed once we condition on
𝑣<𝑒,𝑘. Take the database 𝑏𝐷≤𝑒 and the query parameters 𝑅,
(𝜌𝑟,𝑑𝑟,𝐸𝑟,𝐴𝑟)𝑟∈𝑅,𝜎 corresponding toA conditioned on𝑣<𝑒,𝑘.
Note𝜖𝑥0 the state (accumulated privacy loss) of F𝑥0 in the
world with𝑏 = 1 before answering query𝑒,𝑘 .
On one hand, if (𝑑0,𝑒 0) ∉ {(𝑑𝑟,𝑒),𝑟 ∈ 𝑅,𝑒 ∈ 𝐸𝑟}, we
observe that for all 𝑟 ∈ 𝑅, 0𝐷𝑒𝑟 𝑑𝑟 = 1𝐷𝑒𝑟 𝑑𝑟 , because 0𝐷≤𝑒 and
18

Algorithm 2 Inner Privacy Game
Config
Parametrized noise distributionL
Device-epoch budget capacity(𝜖𝐺 𝑥)𝑥∈X
Upper bound on number of epochs𝑒max
Upper bound on number of queries per epoch𝑘max
Input
Challenge bit𝑏∈{ 0, 1}
Opt-out device𝑥0 =(𝑑0,𝑒 0,𝐹 0)∈X
AdversaryA
Output
View𝑉𝑏 =(𝑣𝑏 1,1,...,𝑣 𝑏 1,𝑘max ,𝑣𝑏 2,1,... ) ofA
𝐷←∅
for𝑒∈[ 𝑒max] do
// Generate data for the epoch𝑒
Receive a database𝐺 for epoch𝑒 fromA
if𝑒 =𝑒0 and(𝑑0,𝑒 0) ∉𝐺 then
𝐺 0←𝐺+(𝑑0,𝑒 0,∅),𝐺 1←𝐺+(𝑑0,𝑒 0,𝐹 0)
else
𝐺𝑏←𝐺
𝐷←𝐷+𝐺𝑏
// Answer queries after epoch𝑒
for𝑘∈[ 𝑘max] do
Receive query𝑄𝑘 fromA with corresponding in-
dices𝑅, devices(𝑑𝑟)𝑟∈𝑅, target epochs(𝐸𝑟)𝑟∈𝑅, attribution
functions(𝐴𝑟)𝑟∈𝑅 and noise std-dev𝜎.
for𝑟∈𝑅 do
// Compute report for𝑟
for𝑒∈𝐸𝑟 do
𝑥←(𝑑𝑟,𝑒,𝐷 𝑒 𝑑𝑟 )
ifF𝑥 is not defined then
Initialize filterF𝑥 with capacity𝜖𝐺 𝑥
𝜖𝑥← ComputeIndividualBudget(𝑥,𝑑,𝐸,𝐴, L,𝜎)
ifF𝑥. tryConsume(𝜖𝑥) =𝐻𝑎𝑙𝑡 then
𝐹𝑒←∅
else
𝐹𝑒←𝐷𝑒 𝑑
𝜌𝑟←𝐴((𝐹𝑒)𝑒∈𝐸)
// Aggregate and noise reports to answer𝑄𝑘
Sample𝑋∼L( 𝜎)
Send𝑣𝑏 𝑒,𝑘 = ˝ 𝑟∈𝑅𝜌𝑟+𝑋 toA
1𝐷≤𝑒 differ at most on 𝑥0 =(𝑑0,𝑒 0,𝐹 0). In this case, ∀𝑟 ∈
𝑅,𝜌𝑟(0𝐷≤𝑒) = 𝜌𝑟(1𝐷≤𝑒), and hence Pr[𝑉 0 𝑒,𝑘 = 𝑣𝑒,𝑘|𝑣<𝑒,𝑘] =
Pr[𝑉 1 𝑒,𝑘 =𝑣𝑒,𝑘|𝑣<𝑒,𝑘].
On the other hand, suppose that we have 𝑟1,...,𝑟 ℓ (pro-
cessed in this order) such that for all 𝑖∈[ ℓ] we have𝑑𝑟𝑖 =
𝑑0,𝑒 0∈𝐸𝑟𝑖 .
We pose ˆ𝑅 ⊂ 𝑅 the set of reports that do not pass the
filter in the world with 𝑏 = 1. (In the world with 𝑏 = 0,
the filter for (𝑑0,𝑒 0,∅) has no effect on 𝜌𝑟(0𝐷≤𝑒) because
whether it halts or not we have𝐹𝑒0 =∅). For𝑟 ∉ ˆ𝑅, we have
𝜌𝑟(0𝐷≤𝑒) =𝜌𝑟(1𝐷≤𝑒) because both worlds use𝐹𝑒0 =∅.
Hence, we have:
∥
∑︁
𝑟∈𝑅
𝜌𝑟(0𝐷≤𝑒)− 𝜌𝑟(1𝐷≤𝑒)∥ 1 =∥ ∑︁
𝑟∈ ˆ𝑅
𝜌𝑟(0𝐷≤𝑒)− 𝜌𝑟(1𝐷≤𝑒)∥ 1
≤
∑︁
𝑟∈ ˆ𝑅
Δ𝑥𝜌𝑟 (7)
since 0𝐷≤𝑒 and 1𝐷≤𝑒 differ at most on𝑥 =(𝑑0,𝑒 0,𝐹 0).
Take𝑋 0∼𝑋 1∼ Lap(𝑏) with𝑏 =𝜎/ √ 2. We have:
Pr[𝑉 0 𝑒,𝑘 =𝑣𝑒,𝑘|𝑣<𝑒,𝑘]
Pr[𝑉 1 𝑒,𝑘 =𝑣𝑒,𝑘|𝑣<𝑒,𝑘] = Pr[˝ 𝑟∈𝑅𝜌𝑟(0𝐷≤𝑒)+ 𝑋 0 =𝑣𝑒,𝑘] Pr[˝ 𝑟∈𝑅𝜌𝑟(1𝐷≤𝑒)+ 𝑋 1 =𝑣𝑒,𝑘]
(8)
By property of the Laplace distribution, combining Eq. 7
and Eq. 8 gives:

 Pr[𝑉 0 𝑒,𝑘 =𝑣𝑒,𝑘|𝑣<𝑒,𝑘] Pr[𝑉 1 𝑒,𝑘 =𝑣𝑒,𝑘|𝑣<𝑒,𝑘]

≤ ∑︁ 𝑟∈ ˆ𝑅 Δ𝑥𝜌𝑟/𝑏 (9)
By definition of ComputeIndividualBudget, we have𝜖𝑟 =
Γ𝑥,𝑟/𝑏 where Δ𝑥𝜌𝑟 ≤ Γ𝑥,𝑟 . Thus, we get ˝ 𝑟∈ ˆ𝑅 Δ𝑥𝜌𝑟/𝑏 ≤˝
𝑟∈ ˆ𝑅𝜖𝑟 .
Taking the sum over all queries, we get:
| ln
 Pr[𝑉 0 =𝑣]
Pr[𝑉 1 =𝑣]

|≤
𝑒max∑︁
𝑒=1
𝑘max∑︁
𝑘=1
∑︁
𝑟∈ ˆ𝑅𝑒,𝑘
𝜖𝑟 (10)
≤𝜖𝐺 𝑥 (11)
where Eq. 11 is by definition of a Pure DP filter. □
Theorem 6 (IDP of Alg. 3 when replacing 𝑥0 by 𝑥1 for
fixed public information). Fix a device-epoch budget capac-
ity(𝜖𝐺 𝑥)𝑥∈X for every possible record 𝑥 ∈X . Fix a set of
public events𝑃⊂I∪C .
For any pair of records𝑥0 =(𝑑0,𝑒 0,𝐹 0),𝑥 1 =(𝑑1,𝑒 1,𝐹 1)∈
X such that𝑒0 =𝑒1 and𝐹0∩𝑃 =𝐹1∩𝑃, for any adversary
B, and𝑊 0,𝑊 1 defined by Alg. 3, for all𝑤∈ Supp(𝑊 1) we
have:

ln  Pr[𝑊 0 =𝑣] Pr[𝑊 1 =𝑣] 

≤𝜖𝐺 𝑥0+𝜖𝐺 𝑥1 (12)
Proof. Fix an upper bound on the number of epochs and
queries per epoch𝑒max,𝑘 max. Take a record pair𝑥0,𝑥 1∈X , an
adversaryB,𝑊 0,𝑊 1 defined by Alg. 3 and𝑤∈ Supp(𝑊 1).
We define𝑣 :=(𝑤1,1,...,𝑤 1,𝑘max,𝑤 2,1,...,𝑤 𝑒max,𝑘max the trun-
cated version of the view𝑤 without nonce information (steps
with𝑘 = 0).
We have:
19

Algorithm 3 Outer Privacy Game
Config
Parametrized noise distributionL
Device-epoch budget capacity(𝜖𝐺 𝑥)𝑥∈X
Upper bound on number of epochs𝑒max
Upper bound on number of queries per epoch𝑘max
Public events𝑃⊂I∪C
Input
Pair of records 𝑥0 =(𝑑0,𝑒 0,𝐹 0),𝑥 1 =(𝑑1,𝑒 1,𝐹 1)∈X
such that𝑒0 =𝑒1 and𝐹0∩𝑃 =𝐹1∩𝑃
Challenge bit𝑐
AdversaryB
Output
View𝑊𝑐 =(𝑤𝑐 1,0,𝑤𝑐 1,1,...,𝑤 𝑐 1,𝑘max ,𝑤𝑐 2,0,𝑤𝑐 2,1,... ) ofB
Initialize Alg. 2 with same configuration, challenge bit
𝑏 = 1, opt-out device𝑥𝑐 and adversaryA (whose behavior
is defined next)
for𝑒∈[ 𝑒max] do
// Generate data for the epoch𝑒
Receive a database𝐺 for epoch𝑒 fromB
AskA to submit𝐺
if𝑒 =𝑒0 and(𝑑0,𝑒 0) ∉𝐺 and(𝑑1,𝑒 1) ∉𝐺 then
// At this point,A also adds𝑥𝑐 in his own game
𝐺𝑐←𝐺+𝑥𝑐
else
𝐺𝑐←𝐺
// Release public information
𝑆 =∅
for(𝑑,𝑒,𝐹 )∈ 𝐺𝑐 do
for𝑓∈𝐹∩𝑃 do
Generate report nonce𝑟
$
←𝑈(Z)
Save device corresponding to nonce𝑑𝑟←𝑑
𝑆←𝑆∪{( 𝑟,𝑓 )}
Send𝑤𝑐 𝑒,0 =𝑆 toB
// Answer queries after epoch𝑒
for𝑘∈[ 𝑘max] do
Receive query 𝑄𝑘 fromB with corresponding
nonces 𝑅, target epochs (𝐸𝑟)𝑟∈𝑅, attribution functions
(𝐴𝑟)𝑟∈𝑅 and noise std-dev𝜎.
AskA to send 𝑄𝑘 with devices(𝑑𝑟)𝑟∈𝑅, receive
(𝑣𝑥𝑐)1 𝑒,𝑘
Send𝑤𝑐 𝑒,𝑘 =(𝑣𝑥𝑐)1 𝑒,𝑘 toB
ln
 Pr[𝑊 0 =𝑤]
Pr[𝑊 1 =𝑤]

= ln
 𝑒maxÖ
𝑒=1
𝑘maxÖ
𝑘=1
Pr[𝑊 0 𝑒,𝑘 =𝑤𝑒,𝑘|𝑤<𝑒,𝑘]
Pr[𝑊 1 𝑒,𝑘 =𝑤𝑒,𝑘|𝑤<𝑒,𝑘]
!
+ ln
 𝑒maxÖ
𝑒=1
Pr[𝑊 0 𝑒,0 =𝑤𝑒,0|𝑣<𝑒,0]
Pr[𝑊 1 𝑒,0 =𝑤𝑒,0|𝑤<𝑒,0]
!
(13)
Take𝑒∈[ 𝑒max],𝑘 ∈[ 𝑘max],𝑐∈{ 0, 1}. Take the database
𝑐𝐷≤𝑒 corresponding toB conditioned on𝑤<𝑒,𝑘.B receives
two types of results:
• If𝑘 = 0,𝑊𝑐 𝑒,𝑘 is about nonces and public events. We de-
note by𝑍 the random variable that returns{(𝑈𝑓,𝑓),𝑓 ∈
𝐹} with i.i.d.𝑈𝑓 ∼U( Z). Since𝐹0∩𝑃 = 𝐹1∩𝑃, we
have:
Pr[𝑊 0 𝑒,𝑘 =𝑤𝑒,𝑘|𝑤<𝑒,𝑘] = Pr[𝑍 =𝑤𝑒,𝑘]
= Pr[𝑊 1 𝑒,𝑘 =𝑤𝑒,𝑘|𝑤<𝑒,𝑘] (14)
• For𝑘 > 0,𝑊𝑐 𝑒,𝑘 is the noisy answer to a query. In Alg. 3,
we instantiateA as a valid adversary for Alg. 2 with
opt-out record𝑥𝑐 and challenge bit𝑏 = 1 (i.e.,𝑥𝑐 is in-
cluded in the database). We denote by(𝑉𝑥𝑐)1 𝑒,𝑘 the view
of this adversaryA, and by definition of the truncated
view𝑣, we have:
Pr[𝑊𝑐 𝑒,𝑘 =𝑤𝑒,𝑘|𝑤<𝑒,𝑘] = Pr[(𝑉𝑥𝑐)1 𝑒,𝑘 =𝑣𝑒,𝑘|𝑣<𝑒,𝑘] (15)
Thanks to Eq. 14 and Eq. 15, Eq. 13 becomes:
ln
 Pr[𝑊 0 =𝑤]
Pr[𝑊 1 =𝑤]

= ln

Pr[𝑉 1 𝑥0 =𝑣]
Pr[𝑉 1𝑥1 =𝑣]
!
= ln

Pr[𝑉 1 𝑥0 =𝑣]
Pr[𝑉 0𝑥1 =𝑣]
!
+ ln

Pr[𝑉 0 𝑥1 =𝑣]
Pr[𝑉 1𝑥1 =𝑣]
!
(16)
We now show that Pr[𝑉 0 𝑥1 = 𝑣] = Pr[𝑉 0 𝑥0 = 𝑣]. Take
𝑒∈[ 𝑒max],𝑘∈[ 𝑘max], and condition on a prefix𝑣<𝑒,𝑘. Then,
the only difference between(𝑉𝑥0)0 𝑒,𝑘 and(𝑉𝑥1)0 𝑒,𝑘 is the under-
lying database in Alg. 2, that we denote respectively𝐷 and
𝐷′. There exists a database 𝐺 such that 0𝐷≤𝑒 =𝐺+ 1[𝑒≤
𝑒0](𝑑0,𝑒 0,∅) and 0𝐷′≤𝑒 =𝐺+1[𝑒≤𝑒1](𝑑1,𝑒 1,∅). Either way,
for a report𝜌𝑟 and a database D, adding device-epoch records
with empty events does not change the value of 𝜌𝑟(𝐷). In-
deed, by definition𝐷𝑒 𝑑 already returns∅ if(𝑑,𝑒) ∉𝐷. Hence,˝
𝑟∈𝑅𝜌𝑟(0𝐷≤𝑒) = ˝ 𝑟∈𝑅𝜌𝑟(0𝐷′≤𝑒) = ˝ 𝑟∈𝑅𝜌𝑟(𝐺).
Thus,
ln

Pr[𝑉 1 𝑥0 =𝑣]
Pr[𝑉 0𝑥1 =𝑣]
!
= ln

Pr[𝑉 1 𝑥0 =𝑣]
Pr[𝑉 0𝑥0 =𝑣]
!
(17)
Finally, by Thm. 5, Eq. 16 becomes:

ln  Pr[𝑊 0 =𝑣] Pr[𝑊 1 =𝑣] 

≤𝜖𝐺 𝑥0+𝜖𝐺 𝑥1 (18)
□
Theorem 7 (Tighter Thm. 6 with constraint on queries). Fix
a set of public events 𝑃 ⊂ I∪C , and budget capacities
(𝜖𝐺 𝑥)𝑥∈X .
20

Take any𝑥 =(𝑑,𝑒,𝐹 ) ∈X, and define 𝑥𝑃 :=(𝑑,𝑒,𝐹 ∩
𝑃). Suppose that all the attribution functions𝐴 verify∀𝑖,∀𝐹,
𝐴(𝐹1, ...,𝐹𝑖−1,𝐹𝑖∩𝑃,𝐹𝑖, ...,𝐹𝑘) =𝐴(𝐹1, ...,𝐹𝑖−1,∅,𝐹𝑖, ...,𝐹𝑘).
Then, for the record pair(𝑥,𝑥𝑃), for any adversaryB, for
𝑊 0,𝑊 1 defined by Alg. 3 and for all𝑤∈ Supp(𝑊 1) we have:

ln  Pr[𝑊 0 =𝑣] Pr[𝑊 1 =𝑣] 

≤𝜖𝐺 𝑥 (19)
Proof. First, we show that under such queries with𝐹𝐴∩𝑃 =∅,
for any𝑥∈X , Alg. 3 produces the same output on 𝜖𝐺 𝑥𝑃 = 0
and𝜖𝐺 𝑥𝑃 > 0.
Take any𝑥 =(𝑑0,𝑒 0,𝐹)∈X , and define𝑥𝑃 :=(𝑑0,𝑒 0,𝐹∩𝑃).
Take a report𝜌 with an attribution function𝐴 that is executed
on𝑑0 and𝐸 such that𝑒0∈ 𝐸. If𝜖𝐺 𝑥𝑃 = 0, Alg. 3 sets𝐹𝑒0 =∅
and returns 𝜌 = 𝐴((𝐹𝑒)𝑒∈𝐸\{𝑒0}||∅) . If𝜖𝐺 𝑥𝑃 > 0 andF𝑥𝑃 has
enough budget, Alg. 3 sets 𝐹𝑒0 = 𝐹∩𝑃 and returns 𝜌 =
𝐴((𝐹𝑒)𝑒∈𝐸\{𝑒0}||𝐹∩𝑃). Thanks to the constraint on 𝐴, we
have𝐴((𝐹𝑒)𝑒∈𝐸\{𝑒0}||∅) =𝐴((𝐹𝑒)𝑒∈𝐸\{𝑒0}||𝐹∩𝑃).
Finally, we conclude with Thm. 6. □
D.2 Unlinkability Guarantees (Thm. 2)
Definition 1 (Unlinkability privacy game). We define a vari-
ant of Alg. 3 by applying the following modifications:
• We do not require𝐹0∩𝑃 = 𝐹1∩𝑃 anymore, and we
define𝑥2 :=(𝑑0,𝑒 0,𝐹 0\𝐹1)
• If𝑐 = 1, after receiving𝐺 fromB, if𝑒 =𝑒0 and𝑥2 ∉𝐺,
we perform𝐺←𝐺+𝑥2.
In this variant, B tries to distinguish between World 0 in
which the database is 𝐺+𝑥0 = 𝐺+(𝑑0,𝑒 0,𝐹 0), and World
1 in which the database is 𝐺+𝑥1+𝑥2 = 𝐺+( 𝑑1,𝑒 1,𝐹 1)+
(𝑑0,𝑒 0,𝐹 0\𝐹1). In World 0, all the events in𝐹0 are located on
the same device, while in World 1 there are some events on
device𝑑0 and some events on device𝑑1.
Theorem 8 (Unlinkability guarantees). Fix a set of public
events𝑃⊂I∪C , and budget capacities(𝜖𝐺 𝑥)𝑥∈X .
Take any𝑑0,𝑑 1∈D ,𝑒∈E ,𝐹0⊂I∪C and𝐹1⊂𝐹0, and
pose𝑥0 :=(𝑑0,𝑒,𝐹 0),𝑥 1 :=(𝑑1,𝑒,𝐹 1),𝑥 2 :=(𝑑0,𝑒,𝐹 0\𝐹1)∈X .
Take any adversaryB for the game from Def. 1 with record
triple(𝑥0,𝑥 1,𝑥 2), and note𝑈 0,𝑈 1 the views ofB.
Then, for all𝑢∈ Supp(𝑈 1) we have:

ln  Pr[𝑈 0 =𝑢] Pr[𝑈 1 =𝑢] 

≤𝜖𝐺 𝑥0+𝜖𝐺 𝑥1+𝜖𝐺 𝑥2 (20)
This bounds the ability ofB to tell whether all the events
𝐹0 (both public and private) belong to a single device or not.
Proof. Take𝑢∈ Supp(𝑈 1). Similar to Thm. 6, the nonce and
public information follow the same distribution in𝑈 0 and𝑈 1,
and the rest of the view corresponds to an execution of Alg. 2
with challenge bit𝑏 = 1. Hence we have:
ln
 Pr[𝑈 0 =𝑢]
Pr[𝑈 1 =𝑢]

= ln

Pr[𝑉 1 𝑥0 =𝑣]
Pr[𝑉 1𝑥1,𝑥2 =𝑣]
!
(21)
where𝑢,𝑉 1 𝑥0,𝑉 1 𝑥1,𝑥2 are defined as follows:
• 𝑣 is the truncated version of 𝑢 obtained by removing
the nonces and public information.
• 𝑉𝑏 𝑥0 is the view of the adversary A defined in Alg. 3
with𝑏∈{ 0, 1}, that if𝑏 = 1 inserts the opt-out record
𝑥0 in the database submitted byB.
• 𝑉𝑏 𝑥1,𝑥2 is the view of the adversaryA′ defined in Def. 1
with𝑏∈{ 0, 1}, that if𝑏 = 1 inserts the opt-out record
𝑥1 in the database submitted byB extended with𝑥2.
• 𝑉𝑏 𝑥2 the view of the adversaryA” defined in Alg. 3 with
𝑏∈{ 0, 1}, that if𝑏 = 1 inserts the opt-out record𝑥2 in
the database submitted byB.
With the same reasoning as in Thm. 6 (Eq. 17), we have
𝑉 0 𝑥0∼𝑉 0 𝑥2. We also have𝑉 0 𝑥1,𝑥2 =𝑉 1 𝑥2. Thus, Eq. 21 becomes:
ln
 Pr[𝑈 0 =𝑢]
Pr[𝑈 1 =𝑢]

= ln

Pr[𝑉 1 𝑥0 =𝑣]
Pr[𝑉 1𝑥1,𝑥2 =𝑣]
Pr[𝑉 0 𝑥1,𝑥2 =𝑣]
Pr[𝑉 1𝑥2 =𝑣]
Pr[𝑉 0 𝑥2 =𝑣]
Pr[𝑉 0𝑥0 =𝑣]
!
We conclude with Thm. 5. □
Theorem 9 (Simplified Expression for Thm. 8) . Fix a set
of public events𝑃⊂I∪C , and budget capacities(𝜖𝐺 𝑥)𝑥∈X .
Take any 𝑑0,𝑑 1 ∈ D, 𝑒 ∈ E, 𝐹1 ⊂ 𝐹0 ⊂ 𝑃 (i.e., all the
events we consider here are public events), and pose 𝑥0 :=
(𝑑0,𝑒,𝐹 0),𝑥 1 := (𝑑1,𝑒,𝐹 1),𝑥 2 := (𝑑0,𝑒,𝐹 0\𝐹1) ∈ X. Take
any adversaryB for the game from Def. 1 with record triple
(𝑥0,𝑥 1,𝑥 2), and note 𝑈 0,𝑈 1 the views of B. Suppose that
all the attribution functions𝐴 submitted byB have relevant
events sets𝐼∪𝐶 that verify𝐹𝐴∩𝑃 =∅
Then, for all𝑢∈ Supp(𝑈 1) we have:

ln  Pr[𝑈 0 =𝑢] Pr[𝑈 1 =𝑢] 

 = 0 (22)
Proof. First, we observe that𝐹0∩𝐹𝐴 =𝐹1∩𝐹𝐴 =(𝐹0\𝐹1)∩
𝐹𝐴 =∅. Then, by applying the same reasoning as Thm. 7, we
can suppose without loss of generality that𝜖𝐺 𝑥0 =𝜖𝐺 𝑥1 =𝜖𝐺 𝑥2 = 0.
We conclude with Thm. 8. □
D.3 Privacy Guarantees Under Colluding Queriers
We show that, as in DP, colluding parties can be analyzed us-
ing DP composition. This property is not immediate, because
queriers in Cookie Monster possess side information that they
use to define queries with good IDP properties. Informally,
for a record𝑥 on device𝑑, the collusion of𝑛 parties with bud-
get𝜖𝐺1 𝑑 ,...,𝜖 𝐺𝑛 𝑑 is 2𝜖𝐺1 𝑑 +···+ 2𝜖𝐺𝑛 𝑑 -DP for𝑥 under the joint
public information. We can remove the factor 2 when queries
never look at the public data from any colluding querier.
21

Theorem 10 (Colluding Queriers). Fix𝑛 > 1 a number of
colluding queriers ( i.e., adversaries from Alg. 3). For sim-
plicity, we suppose that the data is not adaptively chosen,
allowing us to see each querier as an interactive mechanism
with viewM↔ 𝑖 (𝐷) when executed on a database𝐷∈ D. Fix
a set of public events 𝑃𝑖⊂I∪C for each querier𝑖∈[ 𝑛],
and budget capacities(𝜖𝐺𝑖 𝑥 )𝑥∈X . Define𝑃 :=𝑃1∪···∪ 𝑃𝑛.
For any pair of records𝑥0 =(𝑑0,𝑒 0,𝐹 0),𝑥 1 =(𝑑1,𝑒 1,𝐹 1)∈
X such that𝑒0 =𝑒1 and𝐹0∩𝑃 = 𝐹1∩𝑃, for any database
𝐷∈ D with(𝑑0,𝑒 0) ∉𝐷,(𝑑1,𝑒 1) ∉𝐷, for any adversaryM
that concurrently executesM↔ 1 ,..., M↔ 𝑛 on the same data
(potentially interleaving and adaptively choosing queries),
for all𝑆∈ Range(M) we have:
Pr[M(𝐷+𝑥0)∈ 𝑆]≤ exp
 𝑛∑︁
𝑖=1
𝜖𝐺𝑖 𝑥0+𝜖𝐺𝑖 𝑥1
!
Pr[M(𝐷+𝑥1)∈ 𝑆]
(23)
When the attribution functions used by any querier satisfy
∀𝑖,∀𝐹, 𝐴(𝐹1, ...,𝐹𝑖−1,𝐹𝑖∩𝑃,𝐹𝑖, ...,𝐹𝑘) =𝐴(𝐹1, ...,𝐹𝑖−1,∅,𝐹𝑖, ...,𝐹𝑘),
and when𝑥1 =(𝑑0,𝑒 0,𝐹 0∩𝑃), then we can remove the 𝜖𝐺𝑖 𝑥1
term.
In such a case of colluding queriers, the constraint that
∀𝐹, 𝐴(𝐹∩𝑃) =𝐴(∅) is more restrictive than merely asking
∀𝐹,𝐴𝑖(𝐹∩𝑃𝑖) =∅ for a single querier as in Thm. 7. For
instance, the queries we describe in §4.1.3 will not verify this
constraint if an advertiser and a publisher collude. However,
the guarantee under general queries of 2˝𝑛 𝑖=1𝜖𝐺𝑖 𝑑 -DP still
applies.
Proof. The key observation is that Thm. 6 shows that Alg. 3 is
in particular DP under a more restrictive Change One neigh-
borhood relation over the union of the public information
across queriers. We can then compose𝑛 mechanisms under
this restrictive neighborhood relation.
More formally, fix 𝑄 ⊂ I∪C and 𝑥 = (𝑑,𝑒,𝐹 ),𝑥′ =
(𝑑′,𝑒′,𝐹′) ∈X. We define the following neighborhood re-
lation over databases. For 𝐷,𝐷′ ∈ D, we say 𝐷 𝑄 ∼
𝑥,𝑥′ 𝐷 if
𝑒 = 𝑒′, 𝐹∩𝑄 = 𝐹′∩𝑄, and there exists 𝐷0 ∈ D such
that𝐷 = 𝐷0+𝑥 and𝐷′ = 𝐷0+𝑥′ or vice versa. Consider
𝑥0 =(𝑑0,𝑒 0,𝐹 0),𝑥 1 =(𝑑1,𝑒 1,𝐹 1)∈X such that𝑒0 = 𝑒1. For
all𝑖∈[ 𝑛], we have𝐹0∩𝑃 =𝐹1∩𝑃 =⇒ 𝐹0∩𝑃𝑖 =𝐹1∩𝑃𝑖,
and thus:
∀𝐷,𝐷′∈ D,𝐷 𝑃 ∼
𝑥0,𝑥1
𝐷 =⇒ 𝐷
𝑃𝑖
∼
𝑥0,𝑥1
𝐷 (24)
Thm. 6 shows the interactive mechanismM↔ 𝑖 is𝜖𝐺𝑖 𝑥0+𝜖𝐺𝑖 𝑥1 -
DP under the
𝑃𝑖
∼
𝑥0,𝑥1
relation. Thanks to Eq. 24, M↔ 𝑖 is also
𝜖𝐺𝑖 𝑥0+𝜖𝐺𝑖 𝑥1 -DP under the 𝑃 ∼ 𝑥0,𝑥1 relation. Note that this conclusion
would not be true if we had proved Thm. 6 under the replace-
with-default definition𝐷∼𝑄 𝑥 𝐷′ introduced in §4.1.1.
Next, the adversary that concurrently executes the𝑛 queriers
is operating a concurrent composition of interactive mecha-
nismsM↔ 1 ,..., M↔ 𝑛 . Thanks to the concurrent composition
theorem [43], the resulting mechanismM is ˝𝑛 𝑖=1𝜖𝐺𝑖 𝑥0+𝜖𝐺𝑖 𝑥1 -
DP under the
𝑃
∼
𝑥0,𝑥1
relation.
□
E Proofs for IDP Optimizations (§4.3)
Theorem 11 (Global sensitivity of reports) . Fix a report
identifier𝑟, a device 𝑑𝑟 , a set of epochs 𝐸𝑟 , an attribution
function𝐴 and the corresponding report 𝜌 : 𝐷↦→ 𝐴(𝐷𝐸𝑟 𝑑𝑟 ). We have:
Δ(𝜌) = max∥𝐴(𝐹1, ...,𝐹𝑘)
𝑖∈[𝑘],𝐹1,...,𝐹𝑘∈P(I∪C)
−𝐴(𝐹1, ...,𝐹𝑖−1,∅,𝐹𝑖+1, ...,𝐹𝑘)∥ 1
If𝐴 has𝑚-dimensional output and verifies∀F∈P(I∪
C)𝑘,∀𝑖 ∈ [𝑚],𝐴(F)𝑖 ∈ [0,𝐴 max], then we have Δ(𝜌) ≤
𝑚𝐴max.
Proof. Take such a report 𝜌. We enumerate the requested
epochs from 1 to𝑘 =|𝐸𝑟|:𝐸𝑟 ={𝑒1,...,𝑒 𝑘}.
First, by definition of the global sensitivity, we have:
Δ(𝜌) = max
𝐷,𝐷′∈D:∃𝑥∈X,𝐷′=𝐷+𝑥 ∥𝜌(𝐷)− 𝜌(𝐷′)∥ 1 (25)
= max
𝐷,𝐷′∈D:∃𝑥∈X,𝐷′=𝐷+𝑥 ∥𝐴(𝐷𝐸𝑟 𝑑𝑟 )− 𝐴((𝐷′)𝐸𝑟 𝑑𝑟 )∥ 1 (26)
= max
𝐷,𝐷′∈D:∃𝑥=(𝑑𝑟,𝑒,𝐹)∈X :𝑒∈𝐸𝑟,𝐷′=𝐷+𝑥 ∥𝐴(𝐷𝐸𝑟 𝑑𝑟 )− 𝐴((𝐷′)𝐸𝑟 𝑑𝑟 )∥ 1
(27)
since for 𝑥 = (𝑑,𝑒,𝐹 ) with𝑑 ≠ 𝑑𝑟 or𝑒𝑟 ∉ 𝐸𝑟 we have
𝐴(𝐷𝐸𝑟 𝑑𝑟 ) =𝐴((𝐷′)𝐸𝑟 𝑑𝑟 ). Next, we show that the two following sets are equal:
•{( 𝐷𝐸𝑟 𝑑𝑟 ),(𝐷′)𝐸𝑟 𝑑𝑟 )|𝐷,𝐷′∈ D :∃𝑥 =(𝑑𝑟,𝑒,𝐹)∈X :𝑒∈
𝐸𝑟,𝐷′ =𝐷+𝑥}
•{(( 𝐹1, ...,𝐹𝑖−1,∅,𝐹𝑖+1, ...,𝐹𝑘),(𝐹1, ...,𝐹𝑘))|𝑖∈[ 𝑘],𝐹 1,
...,𝐹 𝑘∈P(I∪C)}
On one hand, take 𝐷,𝐷′∈ D such that there exists 𝑥 =
(𝑑𝑟,𝑒,𝐹)∈X verifying𝑒𝑟 ∈ 𝐸𝑟 and𝐷′ = 𝐷+𝑥. We pose
𝐹𝑗 := (𝐷′)𝑒𝑗 𝑑𝑟 for𝑒𝑗 ∈ 𝐸𝑟 . If 𝑥 has epoch 𝑒 = 𝑒𝑖 ∈ 𝐸𝑟 for some𝑖, then we have𝐹𝑖 = 𝐹. Hence, since𝐷 must not con-
tain(𝑑𝑟,𝑒), we have: 𝐷𝐸𝑟 𝑑𝑟 = (𝐹1, ...,𝐹𝑖−1,∅,𝐹𝑖+1, ...,𝐹𝑘) and
(𝐷′)𝐸𝑟 𝑑𝑟 =(𝐹1, ...,𝐹𝑘).
Reciprocally, take 𝐹1, ...,𝐹𝑘 ∈ P(I∪C) and 𝑖 ∈ [𝑘].
We define𝐷′ :={(𝑑𝑟,𝑒 1,𝐹 1),..., (𝑑𝑟,𝑒𝑘,𝐹𝑘)} and𝐷′ := 𝐷\
(𝑑𝑟,𝑒𝑖,𝐹𝑖). We have𝐷,𝐷′∈ D and there is𝑥 =(𝑑𝑟,𝑒𝑖,𝐹𝑖)∈X
such that𝐷′ =𝐷+𝑥.
Thus both sets are equal, and the maximum becomes:
Δ(𝜌) = max∥𝐴(𝐹1, ...,𝐹𝑘)
𝑖∈[𝑘],𝐹1,...,𝐹𝑘∈P(I∪C)
−𝐴(𝐹1, ...,𝐹𝑖−1,∅,𝐹𝑖+1, ...,𝐹𝑘)∥ 1
(28)
22

Finally, suppose that𝐴 has output in R𝑚. Take F, F′. We
have∥𝐴(F)−𝐴(F′)∥ 1 = ˝𝑚 𝑖=1|𝐴(F)𝑖−𝐴(F′)𝑖|. For𝑖∈[ 𝑚] we
have𝐴(F)𝑖 ∈[ 0,𝐴 max] so𝐴(F)𝑖−𝐴(F′)𝑖 ∈[− 𝐴max,𝐴 max].
Hence∥𝐴(F)− 𝐴(F′)∥ 1≤𝑚𝐴max.
This upper bound on Δ(𝜌) can be refined if𝐴 has certain
properties, such as being a histogram query. □
Theorem 12 (Global sensitivity of queries). Fix a query𝑄
with corresponding report identifiers𝑅 and reports, devices
and epoch windows(𝜌𝑟,𝑑𝑟,𝐸𝑟)𝑟∈𝑅.
Δ(𝑄)≤ max
𝑑,𝑒
∑︁
𝑟∈𝑅:𝑑=𝑑𝑟,𝑒∈𝐸𝑟
Δ(𝜌𝑟) (29)
In particular, if each device-epoch participates in at most
one report, then Δ(𝑄) = max𝑟∈𝑅 Δ(𝜌𝑟).
Proof. Take such a query𝑄. We observe that
Δ(𝑄) = max
𝐷,𝐷′∈D:∃𝑥∈X,𝐷′=𝐷+𝑥 ∥𝑄(𝐷)− 𝑄(𝐷′)∥ 1 (30)
= max
𝑥∈X
max
𝐷,𝐷′∈D:𝐷′=𝐷+𝑥 ∥𝑄(𝐷)− 𝑄(𝐷′)∥ 1 (31)
Take𝑥 =(𝑑,𝑒,𝐹 ) ∈X. For 𝑟 ∈ 𝑅 such that 𝑑 ≠ 𝑑𝑟 or
𝑒 ∉𝐸𝑟 , we have𝜌𝑟(𝐷) =𝜌𝑟(𝐷′). Thus:
∥𝑄(𝐷)− 𝑄(𝐷′)∥ 1 =∥ ∑︁
𝑟∈𝑅
𝜌𝑟(𝐷)− 𝜌𝑟(𝐷′)∥ 1 (32)
=∥
∑︁
𝑟∈𝑅:𝑑=𝑑𝑟,𝑒∈𝐸𝑟
𝜌𝑟(𝐷)− 𝜌𝑟(𝐷′)∥ 1 (33)
Using the triangle inequality and the definition of Δ(𝜌) we
get:
∥𝑄(𝐷)− 𝑄(𝐷′)∥ 1≤ ∑︁
𝑟∈𝑅:𝑑=𝑑𝑟,𝑒∈𝐸𝑟
∥𝜌𝑟(𝐷)− 𝜌𝑟(𝐷′)∥ 1 (34)
≤
∑︁
𝑟∈𝑅:𝑑=𝑑𝑟,𝑒∈𝐸𝑟
Δ(𝜌𝑟) (35)
This bound is independent on𝐷,𝐷′ so:
max
𝐷,𝐷′∈D:𝐷′=𝐷+𝑥 ∥𝑄(𝐷)− 𝑄(𝐷′)∥ 1≤ ∑︁ 𝑟∈𝑅:𝑑=𝑑𝑟,𝑒∈𝐸𝑟 Δ(𝜌𝑟) (36)
Finally, this does not involve𝐹 so we can replace the max
over𝑥 =(𝑑,𝑒,𝐹 ) by a max over(𝑑,𝑒):
max
𝑥∈X
max
𝐷,𝐷′∈D:𝐷′=𝐷+𝑥 ∥𝑄(𝐷)− 𝑄(𝐷′)∥ 1≤ max 𝑑,𝑒
∑︁
𝑟∈𝑅:𝑑=𝑑𝑟,𝑒∈𝐸𝑟
Δ(𝜌𝑟)
(37)
If each device-epoch participates in at most one report, then
this becomes Δ(𝑄)≤ max𝑟 Δ(𝜌𝑟). For each𝑟 there exists a
pair𝐷,𝐷′ such that∥𝜌𝑟(𝐷)− 𝜌𝑟(𝐷′)∥ 1 = Δ(𝜌𝑟). Taking the
max across reports shows that the upper bound on Δ(𝑄) is
tight in this case.
□
Theorem 13 (Individual sensitivity of reports). Fix a report
identifier𝑟, a device 𝑑𝑟 , a set of epochs 𝐸𝑟 , an attribution
function𝐴 with relevant events 𝐹𝐴, and the corresponding
report 𝜌 : 𝐷 ↦→ 𝐴(𝐷𝐸𝑟 𝑑𝑟 ). Fix a device-epoch record 𝑥 =
(𝑑,𝑒,𝐹 )∈X .
If the report requests a single epoch𝐸𝑟 ={𝑒𝑟}, we have:
Δ𝑥(𝜌) =
(
∥𝐴(𝐹)− 𝐴(∅)∥ 1 if𝑑 =𝑑𝑟 and𝑒 =𝑒𝑟
0 otherwise (38)
Otherwise, we have:
Δ𝑥(𝜌)≤
(
Δ(𝜌) if𝑑 =𝑑𝑟 and𝑒∈𝐸𝑟 and𝐹∩𝐹𝐴 ≠∅
0 otherwise
(39)
Proof. Fix such a report 𝜌 and𝑥∈( 𝑑,𝑒,𝐹 )∈X . Consider
any𝐷,𝐷′∈ D such that𝐷′ =𝐷+𝑥. We have𝜌(𝐷) =𝐴(𝐷𝑒𝑟 𝑑𝑟 )
and𝜌(𝐷′) =𝐴((𝐷′)𝑒𝑟 𝑑𝑟 )
• First, suppose that the report requests a single epoch𝑒𝑟 .
– If𝑑 =𝑑𝑟 and𝑒 =𝑒𝑟 , then since𝐷+𝑥∈ D we must
have(𝑑𝑟,𝑒𝑟) ∉ 𝐷, and thus 𝐷𝑒𝑟 𝑑𝑟 =∅. On the other
hand, we have(𝐷′)𝑒𝑟 𝑑𝑟 =𝐹. Thus,∥𝜌(𝐷)− 𝜌(𝐷′)∥ 1 =
∥𝐴(𝐹)− 𝐴(∅)∥ 1
– If 𝑑 ≠ 𝑑𝑟 or 𝑒 ≠ 𝑒𝑟 , then (𝐷′)𝑒𝑟 𝑑𝑟 = 𝐷𝑒𝑟 𝑑𝑟 . Hence
∥𝜌(𝐷)− 𝜌(𝐷′)∥ 1 = 0.
These equalities are independent on 𝐷,𝐷′, so taking
the max gives Δ𝑥(𝜌) =∥𝐴(𝐹)− 𝐴(∅)∥ 1 if𝑑 =𝑑𝑟 and
𝑒 =𝑒𝑟 , and 0 otherwise.
• Second, suppose that the report requests an arbitrary
range of epochs𝐸𝑟 .
– If 𝑑 ≠ 𝑑𝑟 or 𝑒 ≠ 𝐸𝑟 , then (𝐷′)𝐸𝑟 𝑑𝑟 = 𝐷𝐸𝑟 𝑑𝑟 . Hence
∥𝜌(𝐷)− 𝜌(𝐷′)∥ 1 = 0.
– If𝑑 =𝑑𝑟 and𝑒 =𝑒𝑖∈ 𝐸𝑟 and𝐹∩𝐹𝐴 =∅, we have
(𝐷′)𝐸𝑟 𝑑𝑟 =(𝐷𝑒1 𝑑𝑟 , ...,𝐷𝑒𝑖−1 𝑑𝑟 ,𝐹,𝐷 𝑒𝑖+1 𝑑𝑟 , ...,𝐷𝑒𝑘 𝑑𝑟 ). By defini-
tion of 𝐼𝐴∪𝐶𝐴, we have 𝐴((𝐷′)𝐸𝑟 𝑑𝑟 ) = 𝐴(𝐷𝑒1 𝑑𝑟 ∩
𝐹𝐴, ...,𝐷𝑒𝑖−1 𝑑𝑟 ∩𝐹𝐴,𝐹 ∩𝐹𝐴,𝐷𝑒𝑖+1 𝑑𝑟 ∩𝐹𝐴, ...,𝐷𝑒𝑘 𝑑𝑟 ∩𝐹𝐴).
We also have𝐷𝐸𝑟 𝑑𝑟 =(𝐷𝑒1 𝑑𝑟 , ...,𝐷𝑒𝑖−1 𝑑𝑟 ,∅,𝐷𝑒𝑖+1 𝑑𝑟 , ...,𝐷𝑒𝑘 𝑑𝑟 ).
Since 𝐹∩𝐹𝐴 =∅ =∅∩ 𝐹𝐴, we get 𝐴((𝐷′)𝐸𝑟 𝑑𝑟 ) =
𝐴(𝐷𝐸𝑟 𝑑𝑟 ) i.e.,∥𝜌(𝐷)− 𝜌(𝐷′)∥ 1 = 0.
– Otherwise, we must have𝑑 =𝑑𝑟 and𝑒∈𝐸𝑟 and𝐹∩
𝐹𝐴 ≠∅. In that case,∥𝜌(𝐷)− 𝜌(𝐷′)∥ 1 =∥𝐴(𝐷𝑒1 𝑑𝑟 , ...,
𝐷𝑒𝑖−1 𝑑𝑟 ,𝐹,𝐷 𝑒𝑖+1 𝑑𝑟 , ...,𝐷𝑒𝑘 𝑑𝑟 )− 𝐴((𝐷𝑒1 𝑑𝑟 , ...,𝐷𝑒𝑖−1 𝑑𝑟 ,∅,𝐷𝑒𝑖+1 𝑑𝑟 ,
...,𝐷𝑒𝑘 𝑑𝑟 ))∥ 1. The first two identities are independent on 𝐷,𝐷′, so
taking the max gives Δ𝑥(𝜌) = 0. Unfortunately, the
third identity depends on𝐷,𝐷′. Taking the max gives:
23

Δ𝑥(𝜌) = max∥𝐴(𝐹1, ...,𝐹𝑖−1,𝐹,
𝐹1,...,𝐹𝑖−1,∅,𝐹𝑖+1,...,𝐹𝑘∈P(I∪C)
𝐹𝑖+1, ...,𝐹𝑘)
−𝐴(𝐹1, ...,𝐹𝑖−1,∅,𝐹𝑖+1, ...,𝐹𝑘)∥ 1
≤ max∥𝐴(𝐹1, ...,𝐹𝑖−1
𝑖∈[𝑘],𝐹1,...,𝐹𝑘∈P(I∪C)
,𝐹,𝐹 𝑖+1, ...,𝐹𝑘)
−𝐴(𝐹1, ...,𝐹𝑖−1,∅,𝐹𝑖+1, ...,𝐹𝑘)∥ 1
= Δ(𝜌)
thanks to Thm. 11. Although we can technically keep
the first equality to get a tighter expression for Δ𝑥(𝜌),
for common attribution functions Δ(𝜌) is just as tight
(e.g., if the attribution cap is attained because of another
possible epoch𝐹𝑗,𝑗 ≠𝑖).
□
Theorem 14 (Individual sensitivity of queries). Fix a query
𝑄 with corresponding report identifiers𝑅 and reports(𝜌𝑟)𝑟∈𝑅.
Fix a device-epoch record𝑥 =(𝑑,𝑒,𝐹 )∈X . We have:
Δ𝑥(𝑄)≤
∑︁
𝑟∈𝑅
Δ𝑥(𝜌𝑟) (40)
In particular, if𝑥 participates in at most one report𝜌𝑟 , then
Δ𝑥(𝑄) = Δ𝑥(𝜌𝑟).
Proof. The inequality is immediate by triangle inequality and
definition of individual sensitivity. When𝑥 participates in at
most one report 𝜌𝑟 , we get Δ𝑥(𝜌 ˆ𝑟) = 0 for ˆ𝑟 ≠ 𝑟, and thus
Δ𝑥(𝑄)≤ Δ𝑥(𝜌𝑟). The inequality is tight in that case. □
F IDP-Induced Bias Detection
Since individual privacy budgets depend on the data, they
must be kept private. That is why Cookie Monster silently
replaces out-of-budget device-epoch data by ∅ instead of
raising an exception like IPA. This missing data induces a
bias in the query answers and increases the overall error.
IDP-induced bias. Consider a query𝑄 with report identifiers
𝑅, target epochs(𝐸𝑟)𝑟∈𝑅, attribution functions(𝐴𝑟)𝑟∈𝑅 and
noise parameter𝜎. For a database𝐷, the true result is𝑄(𝐷) =˝
𝑟∈𝑅𝐴𝑟(𝐷𝐸𝑟 𝑑𝑟 ). When a device-epoch(𝑑𝑟,𝑒) is out of budget, Cookie Monster drops it, i.e., Alg. 1 uses𝐹𝑒 =∅ instead of
𝐹𝑒 =𝐷𝑒 𝑑𝑟 . We pose:
˜𝑄(𝐷) := ∑︁
𝑟∈𝑅
𝐴𝑟((𝐹𝑒)𝑒∈𝐸𝑟) (41)
We denote byM(𝐷) the value returned by AnswerQuery:
M(𝐷) := ˜𝑄(𝐷)+ 𝑋 where𝑋 ∼L( 𝜎) has mean zero and
variance𝜎 2. Hence, Alg. 1 returns an estimate for𝑄(𝐷) with
the following bias:
E[M(𝐷)− 𝑄(𝐷)] = ˜𝑄(𝐷)− 𝑄(𝐷) (42)
Detecting bias with global sensitivity. When no device-
epoch is out of budget, Alg. 1 returns an unbiased estimate.
We can guarantee that no device-epoch is out of budget by
keeping track of a budget consumption bound as follows. As-
sume we know (1) a lower bound𝜖𝐺 on the individual budget
capacity:∀𝑥∈ 𝐷,𝜖𝐺 𝑥 ≥ 𝜖𝐺, and (2) an upper bound on the
individual budget for each report𝑟 in each query𝑘:𝜖𝑘,𝑟 𝑥 ≤𝜖𝑘,𝑟 .
Then, for all𝑥∈𝐷, ˝ 𝑘,𝑟𝜖𝑘,𝑟≤𝜖𝐺 =⇒ ˝ 𝑘,𝑟𝜖𝑘,𝑟 𝑥 ≤𝜖𝐺 𝑥 .
In practice, the individual budget can be bounded by using
the fact that the individual sensitivity is upper bounded by the
(data-independent) global sensitivity. Hence, a querier can
run its own off-device budgeting scheme to detect the earliest
potentially biased query. This approach does not consume
any budget since it only relies on public query information.
However, once˝ 𝑘,𝑟𝜖𝑘,𝑟 >𝜖𝐺 this approach doesn’t guarantee
that queries are biased (or unbiased).
Estimating bias with DP counting. To get a more granular
estimate of the bias, we can run a special query counting the
number of reports that contain an out-of-budget epoch, as
follows. Given a query𝑄 with output in R𝑚, we atomically
execute(𝑄0,𝑄) as a single query with output in R𝑚+1, where
𝑄0(𝐷) := ˝ 𝑟∈𝑅𝜅· 1[∃𝑒∈ 𝐸𝑟 :𝐷𝑒 𝑑𝑟 =∅]. Prepending a side query to𝑄 gives a high probability bound on the bias.
Results. Thm. 15 formally states the general high probabil-
ity bound on the bias described above. Thm. 16 specializes
Thm. 15 to last-touch attribution. These side queries increase
the privacy budget, as stated in Thm. 17. Finally, Thm. 18
shows that expressions in Thm. 15 and Thm. 16 can use
tighter bounds from for certain common attribution functions.
Theorem 15. Take a query𝑄 with report identifiers𝑅, param-
eters(𝑑𝑟,𝐸𝑟,𝐴𝑟,𝜌𝑟)𝑟∈𝑅, and output inR𝑚. Fix𝜅 > 0, a param-
eter to control the precision of the bound. For𝑟∈𝑅, we define
ˆ𝐴𝑟 :P(I∪C)→ R𝑚+1 by: ˆ𝐴𝑟(𝐹1,...,𝐹 𝑘)0 =𝜅·˝𝑘 𝑖=1 1[𝐹𝑖 =
∅] and∀𝑖 ∈ [𝑚+ 1], ˆ𝐴𝑟(𝐹1,...,𝐹 𝑘)𝑖 = 𝐴𝑟(𝐹1,...,𝐹 𝑘)𝑖. We
pose𝑄0(𝐷) := ˝ 𝑟∈𝑅𝜅· 1[∃𝑒∈ 𝐸𝑟 : 𝐷𝑒 𝑑𝑟 =∅], and denote
by(M0(𝐷),M(𝐷)) the output of Alg. 1 on (𝑄0,𝑄), using
Laplace noise with standard deviation𝜎.
For a report𝜌 with attribution function𝐴 over𝑘 epochs,
we also define:
Δmax(𝜌𝑟) := max
F,F′∈P(I∪C) 𝑘 :∀𝑖∈[𝑘],F′ 𝑖 =F𝑖 or F′ 𝑖 =∅ ∥𝐴(F)− 𝐴(F′)∥ 1
(43)
That is, Δmax(𝜌𝑟) is the maximum L1 change that happens
in a report when we remove any number of epochs from a
device. By comparison, the global sensitivity Δ(𝜌𝑟) is the
maximum change that happens when we remove a single
device-epoch from the database. For certain attribution func-
tions, such as last touch attribution, Δmax(𝜌𝑟) = Δ(𝜌𝑟), as
detailed next in Thm. 18.
Then, for any𝛽∈( 0, 1), with probability 1−𝛽 we have:
∥E[M(𝐷)− 𝑄(𝐷)]∥1≤M0(𝐷)+ 𝜎 ln(1/𝛽)/
√
2
𝜅 max 𝑟∈𝑅 Δmax(𝜌𝑟)
24

Proof. First, we remark thatM0(𝐷) is an unbiased estimate
of ˜𝑄0(𝐷), by definition of ˜𝑄0 which is the output of𝑄0 after
dropping out-of-budget epochs from 𝐷. ˜𝑄0(𝐷) can then be
used to get an upper bound on the number of reports contain-
ing at least one out-of-budget epoch. Indeed, when𝑑𝑟,𝑒 runs
out of budget, ˆ𝐴𝑟 receives𝐹𝑟,𝑒 =∅ in Alg. 1. Hence:
˜𝑄0(𝐷)/𝜅 =|{𝑟∈𝑅 :∃𝑒∈𝐸𝑟,𝐹𝑟,𝑒 =∅}| (44)
=| ˜𝑅| (45)
where ˜𝑅 :={𝑟∈𝑅 :∃𝑒∈𝐸𝑟,𝐹𝑟,𝑒 =∅}| .
Second, we can use ˜𝑄0(𝐷) to bound the bias as follows:
∥E[M(𝐷)− 𝑄(𝐷)]∥1 =∥ ˜𝑄(𝐷)− 𝑄(𝐷)∥ 1 (46)
=∥
∑︁
𝑟∈𝑅
𝐴(𝐹𝑟,𝑒 1,...,𝐹 𝑟,𝑒𝑘)− 𝐴(𝐷𝑒1 𝑑𝑟 ,...,𝐷 𝑒𝑘 𝑑𝑟 ∥1 (47)
≤
∑︁
𝑟∈𝑅
∥𝐴(𝐹𝑟,𝑒 1,...,𝐹 𝑟,𝑒𝑘)− 𝐴(𝐷𝑒1 𝑑𝑟 ,...,𝐷 𝑒𝑘 𝑑𝑟 ∥1 (48)
=
∑︁
𝑟∈𝑅:𝐴(𝐹𝑟,𝑒 1,...,𝐹𝑟,𝑒𝑘)≠𝐴(𝐷𝑒1 𝑑𝑟,...,𝐷 𝑒𝑘 𝑑𝑟)
∥𝐴(𝐹𝑟,𝑒 1,...,𝐹 𝑟,𝑒𝑘) (49)
−𝐴(𝐷𝑒1 𝑑𝑟 ,...,𝐷 𝑒𝑘 𝑑𝑟 ∥1
The set of altered reports {𝑟 ∈ 𝑅 : 𝐴(𝐹𝑟,𝑒 1,...,𝐹 𝑟,𝑒𝑘) ≠
𝐴(𝐷𝑒1 𝑑𝑟 ,...,𝐷 𝑒𝑘 𝑑𝑟 )} is not directly accessible through our count- ing query, but it is a subset of the set of reports containing
empty epochs. These two sets are not necessarily equal, be-
cause certain epochs could be empty in the original database
(unless the application programmatically enforces 𝐷𝑒 𝑑𝑟 ≠∅
by adding a special heartbeat event 𝑓0∈ 𝐹 in every active
device-epoch), and some out-of-budget epochs can leave the
final report value unchanged. In other words:
{𝑟∈𝑅 :𝐴(𝐹𝑟,𝑒 1,...,𝐹 𝑟,𝑒𝑘) ≠𝐴(𝐷𝑒1 𝑑𝑟 ,...,𝐷 𝑒𝑘 𝑑𝑟 }⊂ ˜𝑅 (50)
Hence, we have:
∥E[M(𝐷)− 𝑄(𝐷)]∥1≤
∑︁
𝑟∈ ˜𝑅
∥𝐴(𝐹𝑟,𝑒 1,...,𝐹 𝑟,𝑒𝑘)− 𝐴(𝐷𝑒1 𝑑𝑟 ,...,𝐷 𝑒𝑘 𝑑𝑟 ∥1
(51)
≤| ˜𝑅| max
𝑟∈𝑅
Δmax(𝜌𝑟) (52)
≤( ˜𝑄0(𝐷)/𝜅) max 𝑟∈𝑅 Δmax(𝜌𝑟) (53)
thanks to Eq. 45.
Finally, we can use a tail bound to get a high probability
bound on the expected bias. The knob 𝜅 controls the preci-
sion of the out-of-budget count: higher 𝜅 gives a more pre-
cise estimate but consumes more budget. More precisely, for
Laplace noise with standard deviation𝜎, for an absolute error
𝜏 = 𝜎 ln(1/𝛽) 𝜅 √ 2 in the number of potentially biased reports and a
failure probability target𝛽∈( 0, 1), we have:
Pr[|M 0(𝐷)/𝜅− ˜𝑄0(𝐷)/𝜅| >𝜏] =𝛽 (54)
We conclude by injecting Eq. 54 into Eq. 53.
□
Theorem 16. Consider the setting defined in Thm. 15. Ad-
ditionally, suppose that 𝐴 performs last touch attribution,
where epochs identifiersE⊆ N are ordered chronologically.
We replace𝑄0 by the following counting query: 𝑄0(𝐷) :=˝
𝑟∈𝑅𝜅· 1[∃𝑖∈𝐸𝑟 :𝐷𝑖 𝑑𝑟 =∅∧∀ 𝑗∈𝐸𝑟 : 𝑗 >𝑖,𝐷 𝑗 𝑑𝑟 ∩𝐹𝐴 =∅]. Then, we also have:
∥E[M(𝐷)− 𝑄(𝐷)]∥1≤M0(𝐷)+ 𝜎 ln(1/𝛽)/
√
2
𝜅 max 𝑟∈𝑅 Δmax(𝜌𝑟)
Proof. The only difference with Thm. 15 is that Eq. 45 be-
comes:
˜𝑄0(𝐷)/𝜅 =| ˜𝑅| (55)
where ˜𝑅 :={𝑟 ∈ 𝑅 :∃𝑖 ∈ 𝐸𝑟,𝐹𝑟,𝑖 =∅∧∀ 𝑗 ∈ 𝐸𝑟 : 𝑗 >
𝑖,𝐷 𝑗 𝑑𝑟 ∩𝐹𝐴 =∅}| . Importantly, this new definition of ˜𝑅 still verifies the same identity as Eq. 50:
{𝑟∈𝑅 :𝐴(𝐹𝑟,𝑒 1,...,𝐹 𝑟,𝑒𝑘) ≠𝐴(𝐷𝑒1 𝑑𝑟 ,...,𝐷 𝑒𝑘 𝑑𝑟 )}⊂ ˜𝑅 (56)
Indeed, let’s show that𝐴(𝐹𝑟,𝑒 1,...,𝐹 𝑟,𝑒𝑘) ≠𝐴(𝐷𝑒1 𝑑𝑟 ,...,𝐷 𝑒𝑘 𝑑𝑟 )
=⇒ 𝑟∈ ˜𝑅. Consider a report𝑟∈𝑅\ ˜𝑅. By definition of ˜𝑅 we
have for all𝑖∈𝐸𝑟 ,
𝐹𝑟,𝑖 ≠∅∨∃ 𝑗 >𝑖 :𝐹𝑗∩𝐹𝐴 ≠∅ (57)
We now use the assumption that 𝐴 performs last-touch
attribution to show𝐴(𝐹𝑟,𝑒 1,...,𝐹 𝑟,𝑒𝑘) =𝐴(𝐷𝑒1 𝑑𝑟 ,...,𝐷 𝑒𝑘 𝑑𝑟 ).
• If𝐷𝑒1 𝑑𝑟 ,...,𝐷 𝑒𝑘 𝑑𝑟 contain no attributable impressions, then
𝐴(𝐹𝑟,𝑒 1,...,𝐹 𝑟,𝑒𝑘) =𝐴(𝐷𝑒1 𝑑𝑟 ,...,𝐷 𝑒𝑘 𝑑𝑟 ). • Otherwise, denote by𝑖 the epoch containing the last-
touch, i.e., the most recent relevant event𝑓∈𝐹𝐴, that
should get full attribution. By definition of 𝑖,∀𝑗 >
𝑖,𝐷 𝑗 𝑑𝑟 ∩𝐹𝐴 =∅. But since 𝑟 ∈ 𝑅\ ˜𝑅, Eq. 57 implies
𝐹𝑟,𝑖 ≠∅. Thus𝐹𝑟,𝑖 =𝐷𝑖 𝑑𝑟 , and since more recent epochs 𝑗 > 𝑖 do not contain relevant events, the full attribu-
tion value is allocated to the same event in both cases:
𝐴(𝐹𝑟,𝑒 1,...,𝐹 𝑟,𝑒𝑘) =𝐴(𝐷𝑒1 𝑑𝑟 ,...,𝐷 𝑒𝑘 𝑑𝑟 ).
The rest of the proof is identical. □
Theorem 17 (Sensitivity of augmented queries). Consider
a query(𝑑𝑟,𝐸𝑟,𝐴𝑟,𝜌𝑟)𝑟∈𝑅 augmented by a side query such
that each report ˆ𝜌𝑟 : 𝐷↦→( 𝜌 0 𝑟(𝐷),𝜌𝑟(𝐷))∈ R𝑚+1 verifies
𝜌 0 𝑟(𝐷)∈[ 0,𝜅] for some fixed𝜅 > 0.
Take𝑥 =(𝑑,𝑒,𝐹 )∈X . We have:
Δ𝑥( ˆ𝜌𝑟)≤ 𝜅· 1[𝑑 =𝑑𝑟,𝑒∈𝐸𝑟 and𝐹 ≠∅]+ Δ𝑥(𝜌𝑟) (58)
Proof. First, we have:
Δ𝑥( ˆ𝜌𝑟)≤ Δ𝑥(𝜌 0 𝑟)+ Δ𝑥(𝜌𝑟) (59)
25

because for all𝐷,𝐷′ such that𝐷′ =𝐷+𝑥 we have∥ ˆ𝜌𝑟(𝐷′)−
ˆ𝜌𝑟(𝐷)∥ 1≤∥ 𝜌 0 𝑟(𝐷′)−𝜌 0 𝑟(𝐷)∥ 1+∥𝜌𝑟(𝐷′)−𝜌𝑟(𝐷)∥ 1≤ Δ𝑥(𝜌 0 𝑟)+
Δ𝑥(𝜌𝑟).
Second, we have:
Δ𝑥(𝜌 0 𝑟)≤
(
𝜅 if𝑑 =𝑑𝑟,𝑒∈𝐸𝑟 and𝐹 ≠∅
0 otherwise (60)
Indeed, consider𝐷,𝐷′ such that𝐷′ =𝐷+𝑥.
• If𝐹 =∅,𝑑 ≠𝑑𝑟 , or𝑒 ∉𝐸𝑟 we have𝜌 0 𝑟(𝐷) =𝜌 0 𝑟(𝐷′) for
all such𝐷,𝐷′ so Δ𝑥(𝜌 0 𝑟) = 0.
• If 𝐹 ≠ ∅, 𝑑 = 𝑑𝑟 and 𝑒 ∈ 𝐸𝑟 we have: ∥𝜌 0 𝑟(𝐷′)−
𝜌 0 𝑟(𝐷)∥ 1≤𝜅.
□
Instantiation. Side queries in both Thm. 15 and Thm. 16
follow the form from Thm. 17, with𝜌 0 𝑟(𝐷) =𝜅· 1[∃𝑒∈𝐸 :
𝐷𝑒 𝑑𝑟 =∅] in Thm. 15 and𝜅· 1[∃𝑖∈𝐸𝑟 :𝐷𝑖 𝑑𝑟 =∅∧∀ 𝑗∈𝐸𝑟 :
𝑗 >𝑖,𝐷 𝑗 𝑑𝑟 ∩𝐹𝐴 =∅] in Thm. 16. Moreover, for these queries,
the inequality in Eq. 60 is an equality if|𝐸| > 1. For instance,
consider𝐷 ={(𝑑𝑟, ˆ𝑒,𝐹), ˆ𝑒∈ 𝐸𝑟\{𝑒}},𝐷′ ={(𝑑𝑟, ˆ𝑒,𝐹), ˆ𝑒∈
𝐸𝑟}. This means that every requested device-epoch that has
budget left and contains data should pay additional budget for
the DP count.
Theorem 18 (Sensitivity for certain histogram attribution
functions). Consider an attribution function𝐴 of the follow-
ing form. First,𝐴 attributes a positive value 𝑎F(𝑓) to each
relevant event𝑓∈𝐹1∩𝐹𝐴∪···∪ 𝐹𝑘∩𝐹𝐴. Next, each event is
mapped to a one-hot vector𝐻(𝑓)∈ R𝑚 (i.e.,𝐻(𝑓)∈{ 0, 1}𝑚
and∥𝐻(𝑓)∥ 1 = 1). Finally, the attribution is the weighted
sum:
𝐴(𝐹1,...,𝐹 𝑘) =
𝑘∑︁
𝑖=1
∑︁
𝑓∈𝐹𝑖∩𝐹𝐴
𝑎F(𝑓)· 𝐻(𝑓) (61)
We define:
𝐴max := max
F∈P(I∪C) 𝑘
𝑘∑︁
𝑖=1
∑︁
𝑓∈𝐹𝑖∩𝐹𝐴
𝑎F(𝑓) (62)
Consider any attribution report𝜌𝑟 with attribution function
𝐴 with output in R𝑚.
• If𝑚 = 1 or𝑘 = 1, we have
Δ(𝜌𝑟)≤ Δmax(𝜌𝑟)≤ 𝐴max (63)
Moreover, if there existsFmax =(∅,..., ∅,{𝑓0},∅,..., ∅)
containing a single relevant event 𝑓0∈ 𝐹𝐴 such that
𝐴max is attained, i.e.,𝑎Fmax(𝑓0) =𝐴max, then
Δ(𝜌𝑟) = Δmax(𝜌𝑟) =𝐴max (64)
• If𝑚≥ 2 and𝑘≥ 2, we have:
Δ(𝜌𝑟)≤ Δmax(𝜌𝑟)≤ 2𝐴max (65)
Moreover, if there existsFmax =(∅,..., ∅,{𝑓0},∅,..., {𝑓1},∅)
and F′ max =(∅,..., ∅,{𝑓0},∅,..., ∅) such that𝑎Fmax(𝑓0) =
𝐴max,𝑎F′max(𝑓1) =𝐴max and𝐻(𝑓0) ≠𝐻(𝑓1), then:
Δ(𝜌𝑟) = Δmax(𝜌𝑟) = 2𝐴max (66)
Proof. Consider a report𝜌𝑟 with such an attribution function
𝐴. First, we observe that𝐴(∅) = 0∈ R𝑚, because of Eq. 61.
We start by upper bounding Δmax(𝜌𝑟). Take F, F′∈P(I∪
C)𝑘 :∀𝑖∈[ 𝑘], F′ 𝑖 = F𝑖 or F′ 𝑖 =∅.
• If𝑚 = 1, for any event 𝑓 we have 𝐻(𝑓) = 1. Since
𝑎F(𝑓) ≥ 0, we have: ˝𝑘 𝑖=1 ˝ 𝑓∈𝐹𝑖∩𝐹𝐴𝑎F(𝑓)· 𝐻(𝑓)−˝
𝑓∈𝐹′ 𝑖∩𝐹𝐴𝑎F′(𝑓)· 𝐻(𝑓)≤ ˝𝑘 𝑖=1 ˝ 𝑓∈𝐹𝑖∩𝐹𝐴𝑎F(𝑓)· 1≤
𝐴max and ˝𝑘 𝑖=1 ˝ 𝑓∈𝐹𝑖∩𝐹𝐴𝑎F(𝑓)·𝐻(𝑓)−˝ 𝑓∈𝐹′ 𝑖∩𝐹𝐴𝑎F′(𝑓)·
𝐻(𝑓)≥− ˝ 𝑓∈𝐹′ 𝑖∩𝐹𝐴𝑎F′(𝑓)·1≥−𝐴max. Hence,∥𝐴(F)−
𝐴(F′)∥ 1≤𝐴max, and thus Δmax≤𝐴max.
• If𝑘 = 1, we have F′ =𝐹1 or∅. In the first case,∥𝐴(F)−
𝐴(F′)∥ 1 = 0≤𝐴max. In the second case,
∥𝐴(F)− 𝐴(F′)∥ 1 =∥𝐴(F)∥ 1 (67)
≤
∑︁
𝑓∈𝐹1∩𝐹𝐴
𝑎F(𝑓)∥𝐻(𝑓)∥ 1 (68)
≤𝐴max (69)
Hence Δmax≤𝐴max.
• If𝑚≥ 2, we have:
∥𝐴(F)− 𝐴(F′)∥ 1 =∥
𝑘∑︁
𝑖=1
∑︁
𝑓∈𝐹𝑖∩𝐹𝐴
𝑎F(𝑓)· 𝐻(𝑓) (70)
−
∑︁
𝑓∈𝐹′ 𝑖∩𝐹𝐴
𝑎F′(𝑓)· 𝐻(𝑓)∥ 1 (71)
≤
𝑘∑︁
𝑖=1
∑︁
𝑓∈𝐹𝑖∩𝐹𝐴
𝑎F(𝑓)∥𝐻(𝑓)∥ 1 (72)
+
𝑘∑︁
𝑖=1
∑︁
𝑓∈𝐹′ 𝑖∩𝐹𝐴
𝑎F′(𝑓)∥𝐻(𝑓)∥ 1 (73)
≤ 2𝐴max (74)
This is true for any such F, F′, so Δmax≤ 2𝐴max.
Next, we lower bound Δmax.
• If𝑚 = 1 or𝑘 = 1, and if there existsFmax =(∅,..., ∅,{𝑓0},
∅,..., ∅) such that𝑎Fmax(𝑓0) =𝐴max, we have
Δmax(𝜌𝑟) = max
F,F′∈P(I∪C) 𝑘 :∀𝑖∈[𝑘],F′ 𝑖 =F𝑖𝑜𝑟 F′ 𝑖 =∅ ∥𝐴(F)− 𝐴(F′)∥ 1
(75)
≥∥ 𝐴(Fmax)− 𝐴(∅)∥ 1 (76)
=∥𝐴max·𝐻(𝑓0)− 0∥1 (77)
=𝐴max (78)
(in fact this is true even when𝑚 ≠ 1 and𝑘 ≠ 1).
26

• If𝑚≥ 2 and𝑘 ≥ 2, and there exists 𝑓0,𝑓 1 such that
removing 𝑓1 shifts the attribution to 𝑓0, and 𝐻(𝑓0) ≠
𝐻(𝑓1), then:
Δmax(𝜌𝑟)≥∥ 𝐴(Fmax)− 𝐴(F′ max)∥ 1 (79)
=∥𝐴max·𝐻(𝑓0)− 𝐴max·𝐻(𝑓1)∥ 1 (80)
= 2𝐴max (81)
We now focus on Δ(𝜌𝑟). First, we have Δ(𝜌𝑟)≤ Δmax(𝜌𝑟),
because if we note𝑁 :={F, F′∈P(I∪C) 𝑘 :∃𝑖∈[ 𝑘] : F′ 𝑖 =
∅∧∀ 𝑗 ≠𝑖, F′ 𝑖 = F𝑖} and𝑁 max :={F, F′∈P(I∪C) 𝑘 :∀𝑖∈
[𝑘], F′ 𝑖 = F𝑖 or F′ 𝑖 =∅} we have𝑁⊂𝑁 max.
Second, the pairs of databases Fmax, F′ max exhibited in
Eq. 75 and Eq. 79 happen to belong to both 𝑁 and 𝑁 max,
so the upper bounds hold. □
Instantiation. In particular, the upper bounds from Thm. 18
apply when the attribution function𝐴 distributes a predeter-
mined conversion value across impressions (e.g., last-touch,
first-touch, uniform, etc.), maps each impression to a bin
(e.g.,𝐻(𝑓) is a one-hot encoding of one of𝑚 campaign iden-
tifiers), and then sums up the value in each bin. The resulting
report𝜌𝑟(𝐷)∈ R𝑚 contains a histogram of the total attributed
conversion value per bin.
The first tightness result (Eq. 64) applies if there exists an
impression that can be fully attributed. The second tightness
result (Eq. 66) applies if there exists two impressions 𝑓0,𝑓 1
with different one-hot encodings, such that removing𝑓1 shifts
the maximum attribution value𝐴max to𝑓0 (e.g., in last-touch
attribution).
Note that we allow𝐴max to have any value, and we don’t
require every database to be fully attributed. This is a slight
generalization of [10], which defines an attribution rule that
requires ˝𝑘 𝑖=1 ˝ 𝑓∈𝐹𝑖∩𝐹𝐴𝑎F(𝑓) = 1.
27
