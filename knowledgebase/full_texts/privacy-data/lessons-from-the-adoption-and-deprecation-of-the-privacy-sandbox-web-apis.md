---
title: Lessons from the Adoption and Deprecation of the Privacy Sandbox Web APIs
url: https://arxiv.org/abs/2606.26390
category: privacy-data
subcategory: measurement
date: 2026-06
venue: arXiv (Cornell University)
authors:
- Yohan Beugin
- Paul Barford
- Patrick McDaniel
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.26390
pages: 19
chars: 98212
fetched_at: '2026-11-08T12:58:22+00:00'
kb_version: 1
---

# Lessons from the Adoption and Deprecation of the Privacy Sandbox Web APIs

Longitudinal Adoption and Deprecation of the
Privacy Sandbox Web APIs
Yohan Beugin
University of Wisconsin-Madison
ybeugin@cs.wisc.edu
Paul Barford
University of Wisconsin-Madison
pb@cs.wisc.edu
Patrick McDaniel
University of Wisconsin-Madison
mcdaniel@cs.wisc.edu
Abstract—While several web actors have been trying to reduce
web tracking for years, it remains unclear how to achieve
both desirable levels of utility and privacy. In 2019, Google
launched the Privacy Sandbox initiative to balance that trade-
off and find privacy alternatives to common use cases such as
advertising. Yet, in late 2025, Google canceled the project and
deprecated most of the newly introduced APIs. Despite its end,
the Privacy Sandbox represents a unique opportunity to learn
about how the ecosystem reacted to the proposed changes. In
this paper, we present a longitudinal measurement and analysis
study of the Privacy Sandbox APIs to characterize their adoption
and deprecation over the past seven years by different web
actors. Leveraging historical HTTP Archive crawls and public
Chrome telemetry data, we offer the largest study of its kind
into the prevalence of each Privacy Sandbox feature, during
their entire respective lifetime (5+ years for some), on popular
websites (CrUX top 100k), and as experienced by Chrome users
during their browsing journey. Our results showcase an adoption
that remained limited and uneven across the years; only few
web actors implemented very specific APIs, and in disparate
manners. We motivate our interpretation of these results by
considering the incentives (interest, resources, timeline, etc.) and
risks (potential trade-offs, privacy violations, and legal exposure,
etc.) for these actors. Finally, our analysis also yields a few
actionable recommendations for the next generation of web
privacy-enhancing technologies.
I. INTRODUCTION
Despite web browsers deploying several privacy solutions
over the years, web tracking continues to be a pervasive
practice today, as it remains unclear how to achieve both
desirable levels of utility and privacy for web actors and
users [89]. In August 2019, Google launched the Privacy
Sandbox initiative to reduce“cross-site and cross-app tracking
while helping to keep online content and services free for
all”[44]. As part of this project, Google proposed several
alternative mechanisms to restrict the use of third-party cook-
ies (TPC) and fingerprinting techniques on Chrome while still
supporting advertising, conversion measurement, and fraud
detection use cases [34].
Google’s initiative represents one of the largest experiments
on deploying web privacy-enhancing techniques in recent
years and on exploring with the community mechanisms
to balance such privacy and utility trade-offs. However, in
October 2025, Google ultimately announced the continuing
support for TPC in Chrome and the deprecation of most of
the newly introduced APIs [24]. Despite its end, the Privacy
Sandbox experiment offers a unique perspective into how the
ecosystem used (and abandoned) the proposed changes.
In this paper, we present a longitudinal measurement and
analysis study of the Privacy Sandbox to shed light on the
adoption and deprecation over the years by different web
actors of its technologies when they were available in Chrome.
Through such observations, we obtain valuable insights about
how this global initiative was adopted or not, which also yield
actionable recommendations for the next generation of web
privacy-enhancing technologies. Our study leverages historical
and public datasets to offer the largest study of its kind into the
prevalence of each Privacy Sandbox feature over its lifetime
in Chrome (5+ years for some). Among other sources, we
query historical crawls from the HTTP Archive to analyze the
adoption and/or deprecation of each proposal on the top 100k
websites (per CrUX rank). We also use public and aggregated
Chrome telemetry to gain a view of the Privacy Sandbox
features encountered by Chrome users while browsing.
Our results (overview in Table I) showcase a general adop-
tion of the Privacy Sandbox that remained limited and very
uneven across the years depending on the considered API. We
observe that most adoption rates reached about their maximum
and stagnated before Google postponed the deprecation of
TPC. We find that the majority of adopters have been present
since the early days of the initiative and that significant efforts
appear to have been deployed by them to test and implement
the proposed mechanisms. However, we detect continuing use
of theUA Client HintsAPI which weakens the provided
protections of UA reduction efforts, usage ofUA Client
Hintsrequires further justification due to its browser finger-
printing risks. Finally, without TPC deprecation in Chrome,
we expect that other external incentives will be needed to
encourage further adoption of the rest of the supported APIs.
Our analysis sheds light on the overall limited and uneven
adoption of the Privacy Sandbox APIs by a few specific
web actors. More broadly, the Privacy Sandbox illustrates the
limitations of“fix it in the browser”remedies and disparities
across browser vendors. Despite Google’s initial objective of
“making the web more private”, today, tracking and TPC
limitations in Chrome remain largely opt-in, while they have
been enabled by default on other browsers like Brave, Firefox,
and Safari. Our contributions are as following:
arXiv:2606.26390v2  [cs.CR]  3 Sep 2026

TABLE I: Study findings and recommendations (more details in each respective section).
Finding Metric Recommendation
API Adoption (Section IV)
(F1) API adoption is highly uneven. 5 only>11.7%page loads. (R3) Future efforts should concentrate on advertising use cases.
(F2) Adoption rose after introduction of APIs, but peaked and stagnated by Q3 2024. See Figures 2, 7, 8, and 9. (R4) The community will be reluctant to adopt future privacy proposals from Google as well as other actors.
API Adopters (Section V)
(F3) The majority of adopters were active starting in the early days of the initiative. 295 attestations, 73RWSsets, top adopters consistent years apart. (R5) Securing long term commitment from early adopters is important to encourage further adoption by others.
Supported APIs (Section VI)
(F4) Most supported APIs have low usage. ≤5.2%of page loads. (R6) External incentives and economics changes may be needed to encourage adoption of the supported APIs and future ones.(F5) CHIPSadoption is driven by actors with large coverage of the web. ∼34.5%of page loads, but only6.7%of TPC on average.
(F6) UA Client Hintsis being abused for browser fingerprinting. >62%of page loads. (R7) Continuing use ofUA Client Hintsshould be justified and user-friendly controls to disable the API must be provided.
Other Recommendations
Background (Section II)Discussion (Section VII)
(R1) Proposals should be precisely evaluated before deployment. (R8) Consent and legal implications should be part of API design.
(R2) Proposals should not be exploitable from a technical aspect. (R9) Privacy protections should be deployed by default to users.
•We perform the largest longitudinal measurement analysis
study of its kind on the adoption (HTTP Archive) and
usage (Chrome Telemetry) of the Privacy Sandbox.
•We report on which APIs were adopted, by whom,
and how, and interpret our findings within their broader
context, i.e., with respect to the development timeline of
the proposals, their prior analyses, but also the incentives
and risk factors that web actors must consider, and the
protections deployed by other browsers in the meantime.
•We highlight privacy issues and violations, such as API
call prior to user consent, continuing use ofUA Client
Hints, and its abuse for browser fingerprinting.
•We offer a few actionable recommendations for the next
generation of web privacy-enhancing technologies.
•Finally, we open-source our entire measurement approach
as a reproducible artifact to encourage further exploration
and extensions of this work (see Appendix A).
II. BACKGROUND ON THEPRIVACYSANDBOX
Next, we provide details about the Privacy Sandbox and
its proposals (with related adoption work described in Sec-
tion VIII). For more background on web tracking overall, we
refer to the following SoK from Vekaria et al. [89].
A. Objectives & Timeline
Google launched the Privacy Sandbox initiative in August
2019 to reduce the use of identifiers while still supporting
cross-site and cross-app use cases such as ad targeting, conver-
sion measurement, and fraud detection [34], [83]. The project
was initially created for the web with more than 25 features
developed to deprecate TPC in Chrome by 2022. Proposals
were later extended to the Android platform (6 features total)
to discontinue the Advertising ID and limit the access scope
of third-party library and SDKs [59].
Over the years, some of these new web mechanisms were
directly implemented and shipped in Chrome. Google often
did so without reaching consensus with other browsers (e.g.,
Timeline Overview
Aug 2019.Launch of the Privacy Sandbox [83], [34].
Jan 2020.Google plans phase-out support for TPC within
two years and first origin trials (OT) by end 2020 [84].
Jan 2021.UK’s Competition and Markets Authority (CMA)
investigates Google’s proposals in Chrome [25].
1 Apr 2022.Start of unified OT in Chrome Beta [60].
2 Jul 2022.TPC deprecation delayed to Q3 or Q4 2024,
expansion of the OT to Chrome stable users in August, and
general availability for APIs in Q3 2023 [19].
3 Oct 2022.5% of stable users are now in the OT [46].
Apr 2023.Enrollment required forAttribution
Reporting,Fenced Frames,Private
Aggregation,Protected Audience,Shared
Storage,Topicsand attest no cross-site tracking [49].
4 May 2023.General APIs availability starting July 2023,
TPC deprecation for 1% of users starting Q1 2024. Full
deprecation still planned for Q3 or Q4 2024 [20].
5 Sep 2023.Attribution Reporting,Fenced
Frames,Private Aggregation,Protected
Audience,Shared Storage, andTopicsship by
default in Chrome 115 [21].
6 Jan 2024.TPC restricted for 1% of Chrome users [28].
7 Apr 2024.Google announces that, after all, TPC will not
be deprecated in Chrome by the end of Q4 2024 [51].
8 Jul 2024.No TPC deprecation considered anymore, new
TPC consent mechanism planned instead [22].
Apr 2025.Google restates that TPC will not be deprecated
and announces not rolling out the new TPC standalone
prompt. Unclear future for Privacy Sandbox APIs [23].
9 Oct 2025.Most APIs are marked for deprecation and
TPC will continue to be supported in Chrome. CMA releases
Google from its commitments [24].
10 Jan 2026.Deprecation ofAttribution
Reporting,Private Aggregation,Protected
Audience,RWS,Shared Storage, andTopicsin
Chrome 144 [57], [56], [55], [54], [53], [52] and complete
removal in Chrome 152 in August 2026.
Fig. 1: Privacy Sandbox timeline overview
2

TABLE II: Overview of the 13 main Privacy Sandbox proposals (in chronological order) measured in this paper. Note: APIs
without a deprecated date are still supported in Chrome. See Section VIII for an overview of related work on adoption.
API [Explainer] Use Case Dates Related Work
Testing Shipping Deprecated Adoption Other
FLoC[37] Ad targeting - 2021-03 2021-08 [90] [80], [30], [81], [8], [68], [88]
UA Client Hints[31] Access reduced UA features - 2021-03 - [85], [94], [90], [63] [64]
FedCM[40] Single Sign-On login 2022-06 2022-11 - [61] [93]
CHIPS[43] Opt-in partitioned cookies 2022-03 2023-05 - [9], [13], [97], [61] -
Private State Tokens[38] Ad fraud prevention 2020-07 2023-07 - [61] [2]
RWS[36] Cross-site relationships 2021-03 2023-07 2026-01 [71], [9], [66] -
Attribution Reporting[35] Ad conversion measurement 2022-04 2023-07 2026-01 [90], [61] [69], [1], [26], [96]
Private Aggregation[47] Cross-site measurement 2022-04 2023-07 2026-01 [61] -
Protected Audience[42] Ad retargeting 2022-04 2023-07 2026-01 [82], [79], [17], [90], [66], [67], [61] [2], [87], [70]
Topics[48] Ad targeting 2022-04 2023-07 2026-01 [90], [66], [67], [79], [91], [61] [29], [18], [86], [65], [4], [11], [10], [27]
Fenced Frames[41] Isolated iframes 2022-05 2023-07 - [61] -
Storage Access[39] Legitimate third-party storage - 2023-07 - [61] -
Shared Storage[45] Cross-site restricted storage 2022-08 2023-07 2026-01 [61] [75]
Brave, Mozilla, Safari) and despite external evaluations un-
covering limitations in the privacy claims being made [12].
As evidenced by the timeline overview in Figure 1, the initial
deprecation date for TPC support in Chrome was postponed
several times. Ultimately, Google ended the project in October
2025 by announcing the deprecation of all but 6 of the APIs
and the continuing support for TPC in Chrome [24], [59].
B. Privacy Analyses of Proposals
Given its potential impact on the online ecosystem and
users’ privacy, the Privacy Sandbox has attracted the attention
of many researchers across the years. Google itself released
several whitepapers and preliminary analyses of some propos-
als [80], [30], [29], [18], [69], [1], [26]. However, these were
often performed on private browsing history data or on public
but out-of-domain datasets, with results reported in aggregate
rather than showing the entire distribution, as well as at times
with unclear methodology steps, assumptions, and limitations.
As a result, these issues led to active points of contention
with the research community around the reproducibility of
Google’s claims and results. This is perhaps best illustrated
by the evaluations ofTopicsfor which Google released
a synthetic dataset of users profiles only 2 years after it
had already been shipped by default to Chrome users [27].
In response to Google attempting to standardize through the
W3C some proposals, other browser vendors often published
their own rebuttals and counter analyses [81], [86], [87].
Finally, different academic researchers also produced a series
of publications outlining the potential privacy leakage, cross-
site tracking risk, and privacy-utility tension associated with
these new mechanisms [8], [68], [88], [65], [4], [11], [10],
[70], [2], [64], [93], [75], [96]. We refer to Table II for a more
precise mapping between these works and each proposal.
Recommendation R1-Privacy guarantees of new web
features should be precisely identified and evaluated in
a reproducible manner before deployment to real users.
Unbiased research can help to improve these mechanisms
but need representative datasets and realistic testbeds.
C. Web Proposals Overview
More than 25 web features were developed by Google
as part of the Privacy Sandbox. Among them, 18 made
it to general availability (i.e., were shipped at some point
by default in Chrome stable) and 7 others—that were
never implemented—were abandoned following Google’s
deprecation announcement in October 2025. From the 18
features shipped in Chrome, 5 correspond to specific policy
changes and were not, on their own, APIs that could be
directly implemented by publishers and advertisers (e.g.,
bounce tracking mitigations, default partitioning, etc.). The
remaining 13 APIs are considered at the core of Google’s
efforts for the web; we focus on them in the rest of the paper.
Next, we briefly describe their main use cases as envisioned
by Google (past or present tense in these explanations
mirror the deprecated or still supported status of each API,
respectively). Please see Table II for respective timelines and
existing related work (described further in Section VIII) for
each Privacy Sandbox API. For more details on how each
proposal actually works, see the following technical report by
Beugin and McDaniel [12].
Attribution Reporting(formerlyConversion
Measurement).This API allowed advertisers and ad tech
providers to measure ad conversions without TPC. Chrome
kept track of source (ad click, view, or touch) and trigger
(purchase or conversion) events and linked them into coarse
event-level or summary reports. Random noise and a time
delay were added to reports to prevent linkage with real users’
identities. Summary reports would be received in batches by
the API caller that then must use an aggregation service to
obtain the corresponding aggregated report.
Cookies Having Independent Partitioned
State (CHIPS).Web developers can opt in to save the
cookies they set into partitioned storage, i.e., in a separate
3

cookie jar per top-level site. Partitioned cookies allow for the
legitimate use of TPC as they can only be accessed by the
same third party and from the same top-level site where they
were set in the first place.CHIPSis the only one of the 13
proposals also implemented in Firefox and Safari.
Federated Credential Management (FedCM).
This mechanism enables identity providers to build an SSO-
login infrastructure facilitated by compatible web browsers
without the use of TPC or redirects. A relying party can
allow users to sign in using the credentials of an account they
have on a trusted third-party identity provider. The browser
mediates the requests and information exchanged between
both parties through the API.
Federated Learning of Cohorts (FLoC).One
of the very first proposals from the project,FLoCaimed
at enabling interest-based advertising without TPC. Chrome
would assign users to a specific cohort every week based
on their browsing history. A central server would enforce
k-anonymity, checking that the cohort had enough users or
merging it with other cohorts until satisfied. Finally, API
callers would be able to observe the cohort IDs of users.
Fenced Frames.This API isolatediframes, with a strict
boundary between the embedded content and the embedding
page, preventing access to each other’s context’sDOM. This is
achieved by the browser mapping theFenced Frameto an
opaque URL and restricting access to the resources available
from inside it. They are intended to be used byProtected
AudienceorShared Storageto prevent publishers
from learning about an ad auction winner or the ad displayed.
Private Aggregation.Similar toAttribution
Reporting, this proposal was meant to measure more
general single and cross-site events, supporting other APIs,
such asShared StorageorProtected Audience.
Private State Tokens(formerlyTrust Tokens).
These tokens enable trust in a user’s authenticity to be
conveyed in a cross-site manner to combat fraud and
bots. An issuer website verifies that a user meets some
definition of trustworthiness through a challenge (e.g.,
solving a CAPTCHA, logging into an account, performing a
transaction, etc.). If completed successfully, the web browser
is issued a token that proves cryptographically that the user
is trusted by the issuer service. On the redeemer side, the
website only needs to verify that the user has a valid and
recent token from a trusted issuer and redeem these tokens as
needed without challenging users again.
Protected Audience(formerlyFLEDGE).This API
provided a real-time bidding infrastructure for ad retargeting
by relying on a new storage mechanism in the browser
calledinterest groups. When users browsed the web and
interacted with specific products, advertisers could request the
users’ browser to add them to a specificinterest group
that contains ads for the corresponding or similar product.
Later, when a user would visit a website with an available
ad space, Chrome would locally execute the ad auction logic
for allinterest groupsusers belong to and display the
ad for the winning bid.
Related Website Sets (RWS)(formerlyFirst
Party Sets).These represented declared relationships by
companies among websites and services they owned. Chrome
would vet and use these to decide when to allow or deny
access to specific third-party storage.
Shared Storage.This API provided the needed data
storage, processing, and sharing solution to allow cross-site
information sharing, but without the use of identifiers. This
was done by allowing unlimited, cross-site storage write
access with privacy-preserving read access from only within
aworklet. Worklets were to offer a secure environment for
processing shared storage data, although direct data sharing
with the associated context was not permitted.
Storage Access.Allows cross-origin content to request
storage access as if they were in first-party context. Chrome
automatically grants storage access in intra-RWScontexts
(e.g., iframe whose embedded and top-level sites belong to
the sameRWS) or prompts users otherwise.
Topics.Successor toFLoC, this API required Chrome to
classify websites visited by users into categories of interest
picked from a taxonomy curated of sensitive topics by
Google. Advertisers could then observe some of the recent
top users’ topics and use them to perform an ad auction.
Google claimed that users had plausible deniability due
to noisy topics being sometimes returned andk-anonymity
protections from other users sharing their same interests.
User-Agent (UA) Client Hints.Several web
browsers minimized identifying information shared through
theUAheader. This API allows servers to explicitly request
access to features (also designated as hints) not exposed
anymore by default by Chrome. The idea is that low-entropy
UAhints are shared during the initial request, then servers can
explicitly ask Chrome for more hints, technically allowing the
browser to mediate access to higher entropy hints. However,
the proposal fails to explain how to perform this mediation
and Google decided to not pursue another project called
Privacy Budget[92] that may have been part of a
solution. Thus, Chrome currently honors every request to
obtain moreUAhints.
D. Attestation
In August 2023, Google started to mandate enrollment
from all developers and third-parties that wanted to use
and call the following APIs:Attribution Reporting,
Private Aggregation,Protected Audience,
Shared Storage, andTopics. This new requirement
appeared to be Google’s solution to address potential
privacy violations and abuse of the APIs [78]. It required
API callers to host an attestation file at a specific
/.well-known/privacy-sandbox-attestation.json
URL under the domain the calls would originate from and to
certify that they would not attempt re-identifying users [50].
On the other side, Chrome contained an allow-list to verify if
an origin triggering one of these APIs was authorized to do
so before returning the result.
4

Recommendation R2-Rather than using an attestation
mechanism with unclear enforcement and legal outcomes if
violated, proposals should not be exploitable.
III. METHODOLOGY
A. Research Questions
Our main research objectives are (a)to shed light on the
adoption of the Privacy Sandbox APIs during the full time
period they were available in Chrome, and (b)obtain insights
and make suggestions about how and why the Privacy Sandbox
might have failed. We more specifically ask the following:
RQ1. What was the general adoption of these APIs over their
availability period? (Section IV)
RQ2. Who adopted the Privacy Sandbox APIs, which APIs
did they use, and how? (Section V)
RQ3. Which supported APIs remain and why? (Section VI)
To answer these, we carry out a measurement analysis of
the adoption ofallPrivacy Sandbox web APIs during their
entireavailability period (overview of findings in Table I). This
provides us with a systematic view into how the ecosystem
reacted as a whole to the proposed changes. This is in contrast
with prior work (see Section VIII) that focused on just an
individual proposal, a subset of APIs, and/or on a narrower
time period, thus limiting prior insights to localized trends.
B. Data Collection
In order to obtain access to historical and longitudinal data
on Privacy Sandbox adoption, we leverage all relevant publicly
available datasets at our disposal. Mainly, we derive our
results from theChrome TelemetryandHTTP Archivedatasets.
We also use version control information from achromium
source tree component and from Google’sRWSopen-source
repository to obtain the lists of some API adopters. Below,
we describe each dataset and corresponding data collection
methodology in more details, a discussion of related ethics
considerations can be found in Appendix IX.
1) List of APIs:We start by collecting details on how to in-
voke each of the 13 identified proposals from Table II by going
through their respective explainer, developer documentation,
and Chrome feature tracking status page. An overview of the
permissions policy directives, JavaScript (JS) methods, HTML
attributes, and HTTP headers detected in our measurement can
be found in Table XI in Appendix.
2) Blink Features:Google monitors the usage on the web
of existing and newBlinkfeatures by instructing Chrome to
record in telemetry reports when one is used and detected
in the wild. TheChrome Statusplatform 1 reports aggregated
statistics such as daily usage of each feature of interest from
Chrome users with telemetry turned on, across all platforms
(Android, Windows, Mac, ChromeOS, and Linux) and chan-
nels (stable, beta, and dev) [32].
Chrome Telemetry.All APIs that we are measuring, except
RWS, have one or several of theirBlinkfeatures monitored this
1https://chromestatus.com/
way. Table III presents an overview of theChrome Telemetry
dataset we derive from these statistics for each API. Dates
range from January 29, 2020 (i.e., towards the start of the
initiative) to April 30, 2026, covering the full time period
of the Privacy Sandbox initiative: from its start to after the
deprecation of most of the APIs in January 2026, prior to
conducting the analysis and submitting this paper. This offers
us a unique perspective into the daily percentage of page
loads across real users’ browsing journeys where one of these
APIs was actually used and not only implemented (RQ1
& RQ3). In practice, in the rest of the paper, we average these
daily percentages to report monthly or quarterly results, and
combine all features under their parent API.
TABLE III: Overview of theChrome Telemetrydataset.
Number of Unique Dates
API Features Entries Days Earliest Latest
Attribution Report.5 5 167 2 011 2020-10-02 2026-04-30
CHIPS1 1 433 1 433 2022-03-24 2026-04-30
FLoC1 656 656 2021-02-27 2026-04-16
FedCM17 10 769 1 470 2022-02-18 2026-04-30
Fenced Frames8 3 938 1 613 2021-08-01 2026-04-30
Private Aggregation6 6 335 1 241 2022-11-10 2026-04-30
Private State Tokens4 7 936 2 105 2020-06-19 2026-04-30
Protected Audience4 3 029 1 482 2022-03-31 2026-04-30
Shared Storage23 12 558 1 413 2022-06-17 2026-04-30
Storage Access30 14 863 1 922 2020-06-10 2026-04-30
Topics6 5 333 1 475 2022-04-04 2026-04-30
UA Client Hints30 46 618 2 192 2020-01-29 2026-04-30
All131 118 635 2 193 2020-01-29 2026-04-30
3) HTTP Archive (HA):Every month, the HA project 2
crawls millions of websites whose URLs come from the
Chrome UX Report (CrUX) to record several web performance
metrics (e.g., page loads and sizes, resources types, requests
made, etc.) [6]. The results are made publicly available through
a Google BigQuery database. These crawls are performed
from Google Cloud locations in the United States through a
Chrome instance on desktop and (emulated Android) mobile
device. The crawler is non-interactive with the page visited
(e.g., no click on any element or consent banner) and stateless
(i.e., every visit is performed from a fresh Chrome instance
with an empty cache and in a logged out state) [7]. Thus,
HA results usually represent a lower bound on the exact
number of adopters and adoption rates over time, as more
page interactivity could yield further APIs calls.
HA-blink.Similar toChrome Telemetry, the HA crawler also
detects if aBlinkfeature has been used on a page. As a result,
we derive theHA-blinkdataset that corresponds to the usage
of Privacy Sandbox APIs features detected on the top 100k
pages each month from both desktop and mobile devices.
In practice, in thisHA-blinkdataset we find evidence of the
first use of a Privacy Sandbox API in March 2021, as shown
by Table IV. This provides us with the prevalence of Privacy
Sandbox features on top websites as a proxy for what real users
encounter during their own browsing journey (RQ1 & RQ3).
2https://httparchive.org/
5

TABLE IV: Overview of theHA-blinkdataset.
Number of Unique Crawls
API Features Entries Crawls Earliest Latest
Desktop
Attribution Reporting3 50 32 2021-06 2026-04
FedCM9 202 41 2022-11 2026-04
Fenced Frames2 46 23 2024-06 2026-04
Private State Tokens2 63 58 2021-03 2026-04
Protected Audience3 49 23 2024-06 2026-04
Shared Storage10 164 23 2024-06 2026-04
Storage Access13 200 30 2023-11 2026-04
Topics4 87 23 2024-06 2026-04
UA Client Hints29 1 282 60 2021-05 2026-04
All (desktop)75 2 143 62 2021-03 2026-04
HA-requests.To answer RQ2 and RQ3, we not only want to
know on which pages some APIs are being invoked, but also
who is responsible for the call and how it is implemented.
For that, we need to query the HTTP traffic data collected
during HA crawls for the presence of one or several of the
Privacy Sandbox APIs and for all different ways to use them
(see Table XI in Appendix). As an example, forTopics, we
check ifSec-Browsing-Topicsis sent via an HTTP request
header or if thedocument.browsingTopicsJS method is
called. Thus, we need to analyze HTTP response headers, but
also check if the HTTP response itself (of typescriptor
html) contains JS code implementing one of the APIs.
A traditional problem is that this syntactic approach by
string matching is usually error-prone, because, we can not
distinguish whether a JS method was called or not (e.g.,
method name present in a branch not executed in practice
or in a comment). Moreover, parsing naively all HA requests
results since the existence of the Privacy Sandbox initiative
would be very cost prohibitive for our analysis.
Here, our main insight is that we can leverage the prior
detection of theBlinkPrivacy Sandbox features to guide us on
which requests from which pages should be further scrutinized.
This helps us reduce query costs and control for incorrect
detections (see discussion in Appendix IX). Thus, we only
run our syntactic matching on all root pages of the top 100k
websites crawled since March 2021 from a desktop client
onto which one of the feature in theHA-blinkdataset has
been detected. We name the derived datasetHA-requestsand
provide an overview of it in Table V. This dataset allows us to
obtain more details such as which first- or third-party resources
implemented one of the APIs. Thereafter, for readability, we
combine all JS calls and HTTP headers under their parent API.
4) Open-source Repositories:In addition to theHAand
Chrome Telemetrydatasets, we also leverage public version
control information from achromiumsource tree component 3
and theRWSrepository 4. This allows us to collect the longi-
tudinal edits made to the attestation andRWSlists that were
shipped with all Chrome instances (RQ2).
3privacy sandbox/privacy sandbox attestations
4https://github.com/GoogleChrome/related-website-sets
TABLE V: Parameters and totals for theHA-requestsdataset.
Name Value
Parameters
Clientdesktop
Date 2021-03 to 2026-04
is root pagetrue
Rank 100k
Typescriptorhtml
Total
Pages parsed 8 403 906
Responses headers parsed 10 645 599 709 (∼1 TB in size)
Responses body parsed 173 959 865 (∼45 TB in size)
Pages with detection 4 325 971
Responses headers with detection 200 274 714
Responses body with detection 18 772 657
IV. API ADOPTION(RQ1)
Chrome Telemetry.Figure 2 shows the general evolution
over time of the percentage of page loads onto which one
of the features associated with one of the Privacy Sandbox
APIs is detected. Note that this result on its own is the
most complete report of the longitudinal adoption rates of the
Privacy Sandbox APIs that we are aware of. From it, we can
observe a very uneven situation as only 5 APIs were ever
present on more than 11.7% of page loads, and if we exclude
them, it appears that adoption and usage by the ecosystem of
Google’s initiative remained very limited.
Finding F1-The adoption of Privacy Sandbox APIs
is highly uneven with the most usage forUA Client
Hints,CHIPS,Attribution Reporting,Topics,
andShared Storage, whereas the remaining APIs have
seen very little to almost no use.
While we discussCHIPSandUA Client Hintsin
more details in Section VI, it is worth mentioning here that the
next 3 other APIs in number of usage have to do with web use
cases that would have likely been directly the most impacted
by TPC deprecation, i.e., ad targeting (Topics), conversion
measurement (Attribution Reporting), and cross-site
storage (Shared Storage). For the other APIs, their usage
level may be indicative of a failure to convince on their
functionality and usability beyond the specific tests carried
out by third parties (see further discussion in Section VII-A).
Recommendation R3-Future attempts at web privacy-
enhancing technologies should concentrate on the main use
cases of advertising and conversion measurement.
Regarding trends over time, we observe that adoption
rates start increasing in real Chrome user page loads around
the Q2 and Q3 of 2023. This is somewhat expected as this
moment (see Figure 1) corresponds with Google announcing
that they will start deprecating TPC for a small percentage of
Chrome users starting early 2024, as well as with the general
availability of theAttribution Reporting,Fenced
Frames,Private Aggregation,Protected
Audience,Shared Storage, andTopicsAPIs in
Chrome 115. These two announcements combined have
6

Q1
2020
Q2 Q3 Q4 Q1
2021
Q2 Q3 Q4 Q1
2022
Q2 Q3 Q4 Q1
2023
Q2 Q3 Q4 Q1
2024
Q2 Q3 Q4 Q1
2025
Q2 Q3 Q4 Q1
2026
Q2
date
0
10
20
30
40
50
60% page loads
❶ ❷ ❸ ❹ ❺ ❻ ❼ ❽ ❾ ❿
API
Attribution Reporting
CHIPS
FLoC
FedCM
Fenced Frames
Private Aggregation
Private State T okens
Protected Audience
Shared Storage
Storage Access
T opics
UA Client Hints
Fig. 2: General adoption rates (quarterly percentage of page loads) over time fromChrome Telemetrydataset (log-scale
in Figure 7). Vertical numbered lines correspond to major development events (see Figure 1).
likely incentivized some actors to start experimenting with
and implementing the APIs in preparation for the impact
of TPC deprecation on their use cases, which was at that
time still planned for the second half of 2024. However,
we observe that this trend did not continue; by Q3 of
2024, adoption across the board has largely stabilized and
reached about its maximum rates over the full time period
of the Privacy Sandbox initiative. Indeed, in the coming
months and quarters afterwards, we observe that rates have
stagnated, with some APIs usage (e.g.,Topics) already
starting to decrease. Again, several factors could be taken
into account here (see further discussion in Section VII-A),
but Google’s announcements with respect to the development
of the initiative are strong indicators of the reasons why:
in Q2 2024, TPC deprecation was postponed for a second
time, before being canceled altogether in Q3 2024. Finally,
in Q4 2025, Google announced the deprecation of most of
the Privacy Sandbox APIs for January 2026, explaining the
adoption drop towards the end of our measurement period.
HA-blink.For interested readers, we report in Appendix C
similar longitudinal adoption results that have been obtained
on our other datasetHA-blink.
Finding F2-Adoption rose after introduction of the APIs
in 2023, but usage already peaked or stagnated by Q3 2024
when Chrome TPC deprecation was abandoned.
Recommendation R4-After this failed TPC deprecation
in Chrome, new efforts will need to address the fact that
the community will be reluctant to adopt future privacy
proposals from Google and perhaps from others too.
V. API ADOPTERS(RQ2)
Jul Sep Nov 2025 Mar May Jul
230
240
250
260Origins enrolled
1 5 10 15 20 25
File version (228 origins in v0)
−10
0
10
Fluctuations
Additions
Removals
Fig. 3: Number of enrolled origins from Jun’24 to Jul’25 and
fluctuations between attestations file versions.
Attestation List.Figure 3 reports on the number of origins
enrolled in the attestation process managed by Google. We
7

observe that a total of 295 unique entities were at some
point enrolled to be able to call the following 5 APIs:
Attribution Reporting,Private Aggregation,
Protected Audience,Shared Storage, and
Topics. In practice, at any given point that number
oscillated between 228 to 266 origins (mean of 256 origins).
This indicates that a relatively few number of additions (i.e.,
newcomers) and removals (i.e., departures) occurred over
time beyond the initial large set of first origins enrolled.
Figure 4 shows an UpSet plot 5 of all the different combina-
tions of the 5 APIs that these 295 origins asked to enroll for.
We also report on the categories of these origins as classified
byForcepoint 6. These categories indicate as expected that the
most prominent adopters were advertisers or entities linked to
some sort of online services, e.g., analytics, hosting, news, or
search providers. Additionally, we observe that if the majority
of origins enrolled to call all 5 APIs, others only requested
specific combinations based on their needs. After the default
5 APIs mentioned previously, advertising-related use cases
account for the top 4 of other requested combinations.
T opics
Protected Audience
Attribution Reporting
Shared Storage
Private Aggregation
0200
0
20
40
60
80
100
120
140Count by origin category
Advertisements
Business and Economy
Information T echnology
News and Media
Other
Search Engines and Portals
Unknown
Web Analytics
Web Hosting
Web Infrastructure
Fig. 4: UpSet plot of APIs enrolled together according to
attestations. Origin category is also reported.
RWSList.Similarly, we go through allRWSsubmissions
approved by Google from November 2022 to July 2025 on the
corresponding GitHub repository. We find that a total of 73 sets
made it to this reference list used by the Chrome browser. As
a result, only 73 primary websites disclosed throughRWStheir
relationships with other secondary services and websites they
also own. By doing so, requests from and to these origins are
not impacted by cross-site storage restrictions and partitioning
from Chrome.
HA-requests.Next, we pivot to measuring the JS implementa-
tion of one of the Privacy Sandbox APIs by web actors in the
HA monthly crawl. Figure 5 provides the top 10 API adopters
(hosts) we detect during a respective HA monthly crawl. These
5An UpSet plot is a type of graph used to visualize overlap between multiple
sets, as Venn diagrams scale poorly beyond 3 or 4 sets.
6https://support.forcepoint.com/s/site-lookup
attribution
fedcm
fenced_frames
floc
private_aggregationprivate_state_tokensprotected_audience
shared_storagestorage_access
topics
ua_client_hints
www.googletagmanager.com
securepubads.g.doubleclick.net
pagead2.googlesyndication.com
googleads.g.doubleclick.net
www.googletagservices.com
gum.criteo.com
connect.facebook.net
www.youtube.com
www.gstatic.com
imasdk.googleapis.com
Host
2023-09-01 (log-scale)
100
101
102
103
104
105
(a) September 2023
attribution
fedcm
fenced_frames
floc
private_aggregationprivate_state_tokensprotected_audience
shared_storagestorage_access
topics
ua_client_hints
www.googletagmanager.com
securepubads.g.doubleclick.net
pagead2.googlesyndication.com
googleads.g.doubleclick.net
www.googleadservices.com
www.gstatic.com
imasdk.googleapis.com
connect.facebook.net
tpc.googlesyndication.com
gum.criteo.com
Host
2024-09-01 (log-scale)
100
101
102
103
104
105
(b) September 2024
attribution
fedcm
fenced_frames
floc
private_aggregationprivate_state_tokensprotected_audience
shared_storagestorage_access
topics
ua_client_hints
www.googletagmanager.com
securepubads.g.doubleclick.net
pagead2.googlesyndication.com
connect.facebook.net
gum.criteo.com
ep2.adtrafficquality.google
www.googleadservices.com
imasdk.googleapis.com
www.gstatic.com
u.openx.net
Host
2025-09-01 (log-scale)
100
101
102
103
104
105
(c) September 2025
Fig. 5: API usage (log-scale) for each of the top 10 API
adopters ranked according to their combined total use. Data
obtained fromHA-requestsdataset for 3 specific dates, one
year apart each.
heatmaps showcase the total number of implementations we
detect for each API by this specific host across all visited
pages. Hosts are ranked per their combined total API usage.
We plot heatmaps for 3 specific dates spaced apart from each
other by a year. These specific dates were picked as they
correspond to the early availability of APIs (September 2023),
8

the time when adoption peaked (September 2024), and before
Google announced the end of the initiative (September 2025).
Comparing hosts across these 3 dates, we find that the set of
top adopters is somewhat consistent over the years meaning
that testers driving adoption at early stages of the project were
still the main ones responsible for API usage at later ones.
Finding F3-The majority of adopters were active starting
in the early days of the initiative.
Recommendation R5-The value of proposals should be
demonstrated upfront to secure long term commitment from
early adopters and encourage further adoption by others.
VI. SUPPORTEDAPIS(RQ3)
As a reminder, only 6 of the Privacy Sandbox APIs
will continue to be supported in Chrome:CHIPS,FedCM,
Fenced Frames,Private State Tokens,Storage
Access, andUA Client Hints.
TABLE VI: Max and recent adoption for supported APIs for
Chrome Telemetrydataset (% page loads).
API Max Q3’25 Q4’25 Q1’26
CHIPS34.45 29.44 29.36 29.43
FedCM3.39 2.04 3.39 3.28
Fenced Frames5.19 4.84 2.51 0.53
Private State Tokens5.16 0.46 0.50 0.42
Storage Access3.05 2.85 2.92 3.05
UA Client Hints62.01 61.04 61.86 62.01
Jul Oct 2025 Apr Jul Oct 2026 Apr
Date
1
2
3
4
5
6
7
8% Partitioned cookies (CHIPS)
Third-party
First-party
Fig. 6: Partitioned cookies (CHIPS) from Jun’24 to Apr’26
among first- and third-party cookies (HA-requests).
Chrome Telemetry&HA-requests.Table VI shows the maxi-
mum and recent quarterly adoption rates of these APIs pre- and
post- Google’s deprecation announcement of late 2025. We
observe thatUA Client Hintsis the API that is used the
most predominantly, i.e., on more than 62% of pages, and that
TABLE VII: Top partitioned TPC set on pages withCHIPS
cookies for April 2026 (HA-requests).
Rank Cookie (name - domain) %
1 cto bundle - .criteo.com 43.91
2 audit p - .rubiconproject.com 34.32
3 khaos p - .rubiconproject.com 34.32
4 receive-cookie-deprecation - .rubiconproject.com 29.88
5 ts - .creativecdn.com 29.02
6 VP - .contextweb.com 22.15
7 pamuid2 - .a-mo.net 21.09
8 psd amuid2 - .sync.a-mo.net 20.28
9 pb rtb ev part - .contextweb.com 19.93
10 server tracking bdsp uid - .tracookiepixel.xyz 18.88
all other 5 APIs currently exhibit a much lower adoption rate.
Indeed,CHIPSis present on about 34.5% of page loads, which
could be interpreted as a somewhat high usage. However, in
practice an average of only 6.7% of all TPC set during each
crawl since June 2024 are partitioned (max of 7.9% of TPC)
as shown by Figure 6. We report in Table VII the top 10
partitioned TPC set on pages withCHIPScookies. We find
that programmatic advertising and digital ad tech companies—
embedded on a large number of websites—are responsible for
setting the majority of these partitioned TPC.
Finding F4-Except forUA Client Hints, the other
APIs still supported by Chrome exhibit low usage.
Finding F5-CHIPSadoption is mainly driven by a few
actors with large coverage of the web.
Recommendation R6-Future attempts may require addi-
tional external incentives such as pressure stemming from
regulatory requirements, broader users’ awareness, or pri-
vacy protections shipped by competing browsers.
Perhaps, the case ofUA Client Hintsillustrates best
the dynamics of the ecosystem. While access toUAhigh
entropy features have been restricted by default on every
major browser, Chrome restored access to them by allowing
third-parties to just call the newUA Client HintsAPI.
Table VIII shows the top 10 hosts and scripts that implement
theUA Client HintsAPI through JS in April 2026 in the
HA-requestsdataset per pages percentage. We also annotated
the list with the main use case for each of these scripts.
We observe that the wide implementation ofUA Client
Hintswe detect inHA-requestsis attributable to the tracking,
advertising, analytics, and bot and spam protection services
provided by Google, Meta, and Microsoft. This continuing use
ofUA Client Hintsby such tracking entities to access
higher entropy hints raises concerns. Indeed,UAinformation
was traditionally used to fingerprint users beforeUAreduc-
tion efforts from browsers. It appears that trackers restarted
doing so through theUA Client HintsAPI [85], [63].
Moreover, a prior measurement study from Intumwayase et al.,
showed that altering theUAdoes not result in visually different
9

TABLE VIII: Top hosts and corresponding scripts implementingUA Client Hintsthrough JS in April 2026 (HA-requests).
Rank Host Script % Pages Use Case
1 www.googletagmanager.com js 68.23 Google tracking tag management
2 www.googletagmanager.com gtm.js 40.24 Google tracking tag management
3 connect.facebook.net fbevents.js 23.78 Meta tracking pixel
4 securepubads.g.doubleclick.net gpt.js 15.11 Google ad serving library
5 pagead2.googlesyndication.com ufs web display.js 12.29 Google ad serving library
6 scripts.clarity.ms clarity.js 12.28 Microsoft user behavior analytics
7 www.googletagmanager.com destination 11.62 Google tracking tag configuration
8 pagead2.googlesyndication.com adsbygoogle.js 11.44 Google ad serving library
9 bat.bing.com bat.js 9.56 Microsoft (Bing) tracking and ad serving
10 www.gstatic.com recaptcha en.js 6.59 Google reCAPTCHA service
browsing experience, suggesting that this information is not
needed anymore for the functioning of the modern web [64].
Finding F6-TheUA Client HintsAPI is being
abused for fingerprinting as it restores access toUAfeatures
that have been restricted by default otherwise.
Recommendation R7-The continuing use ofUA Client
Hintsshould be justified and user-friendly controls to
disable the API must be provided to users by Chrome and
other browsers supporting the API.
VII. DISCUSSION
Next, we reflect on the Privacy Sandbox experiment and
what we learned through our measurement findings. We also
discuss the need for user consent with respect to Google’s
initiative and contextualize how the Privacy Sandbox fits
into a broader narrative of events and tracking mitigation
implemented by other web browsers. While doing so, we also
offer some suggestions for future work.
A. Reflections
1) Findings:Through our study, we observed that some
actors in the ecosystem made a significant attempt towards
testing and adopting these new Privacy Sandbox APIs. They
did so for an extended period of time based on the visible
signals in our datasets. This resulted in a very uneven situation
with some proposals that saw substantial usage on the web
(mainly for the advertising-related mechanisms), while others
not nearly as much. Additionally, adoption quickly rose after
the APIs’ introduction, but reached its maximum and started to
stagnate around the time Google postponed and then canceled
TPC deprecation, after which overall usage never appears
to have gone up again. While we cannot be certain about
the specific reasons from actors for experimenting or not
with these APIs, without being them or Google, we provide
thereafter a few possible interpretations.
2) Incentives and Risks:Ultimately, actors had to con-
template several incentives and risk factors when making
their decisions to partially try, fully adopt, or not use these
mechanisms. A potential reason is that actors were just trying
to get ahead of the TPC deprecation and associated impact
on their business models, but as soon as Google stopped
driving the initiative, their interests plummeted too. Another
possibility is that this represented a real opportunity for some
to adapt their practices and figure out ways forward that more
adequately respect users’ privacy. Let’s also not omit that
testing and implementing these proposals into live systems and
products represents an important commitment in terms of time,
resources, people, money, etc., that not everyone was likely
able to take on. Additionally, during its development, some
aspects of the Privacy Sandbox initiative were still actively
evolving, unresolved, or unclear, such as the privacy and utility
trade-offs these actors were agreeing to, potential privacy
issues and violations, and legal exposure from using these
new mechanisms (see Section VII-B). All of these factors, and
others, could have impacted the decision-making of actors to
adopt or not adopt the Privacy Sandbox APIs.
3) Nuances:At the same time, we have seen how the con-
tinuing use ofUA Client HintsweakensUAreduction
efforts in Chrome and discussed that its usage should be re-
evaluated given its abuse in browser fingerprinting.
4) Takeaway:Overall, our data suggest that a nontrivial
portion of actors from the advertising ecosystem are willing
to experiment with web privacy proposals and that there is a
real market for such approaches, whether Privacy Sandbox
was the right solution or not. As such, future attempts at
privacy-enhancing technologies for the web may have a better
chance if economics or incentives change, for instance through
pressure stemming from new regulatory requirements and
broader awareness from users (Section VII-B) or privacy
mitigations shipped by other browsers (Section VII-C).
B. Privacy Sandbox & User Consent
1) Regulation Compliance:Although the Privacy Sandbox
aimed at deprecating TPC in Chrome, it is likely that the
need for consent management systems and banners on the web
would have remained. Indeed, similar to other web technolo-
gies, the use of the Privacy Sandbox proposals by web actors
would have still required user consent in some jurisdictions.
In fact, Google clearly stated in their compliance FAQ that the
“use of each of the Privacy Sandbox APIs involves accessing
data that is stored on the user’s device”[58] and“strictly
necessary”exemptions 7 to explicit consent would only apply
to very narrow cases and specific APIs, such as account
7This is a direct reference to the EU’s ePrivacy Directive [76], [77].
10

protection (FedCM) or fraud prevention (Private State
Tokens). Anecdotally, Google, itself, specifically prompted
Chrome users located in the European Economic Area and the
UK8 for approval before rolling outTopicsto them in 2023.
2) Continuing Need for Consent Mechanism Systems:As
such, the proposed TPC deprecation in Chrome would not
have addressed the continuing need to repetitively ask users
for consent during their browsing journey. Similarly, Google’s
Privacy Sandbox initiative did not appear to consider stream-
lining users’ experience with respect to consent until only July
2024. Then, Google confirmed that TPC deprecation was not
considered anymore in Chrome and announced that a new stan-
dalone prompt was being planned instead to let“people make
an informed choice that applies across their web browsing”.
However, this mechanism was never deployed [22], [23]. In
retrospect, this could be interpreted as a missed opportunity.
Indeed, through its Privacy Sandbox proposals, Google already
acknowledged and proposed the idea of relying more heavily
on the browser to mediate access to the newly introduced
resources. So, perhaps, the browser could also enforce that
users’ consent was actually provided before setting cookies
for instance, and if needed technically apply users’ choices
on their behalf. This would require browsers to assume more
predominantly their role of gatekeeper.
3) Potential Privacy Violations:As a result, the use of
some Privacy Sandbox APIs without explicit user consent
and agreement may constitute—under some jurisdictions—a
violation of privacy laws. Given that our results have been
obtained from crawls whose instrumentation does not interact
with visited websites nor click through banners, it appears
that the API calls observed in HA data throughblink features
were largely made without such consent being given to these
web actors. Verna et al., performed a consent-aware crawl
onTopicsand found adopters ignoring consent and using
the API anyway [91]. A similar analysis of all proposals
would help determine if APIs are indeed being invoked before
or after the acceptance or denial of consent mechanisms.
Unfortunately, no publicly available dataset has such pre- and
post-consent information. Given the deprecation of most APIs
early 2026, we focused our efforts instead on reporting on
a missing aspect in the field, i.e., a longitudinal adoption
measurement of all these APIs.
Recommendation R8-User consent and legal implica-
tions should be integral considerations at API design. For
instance, browsers should be able to enforce user consent
before returning results rather than relying on non abuse.
C. Privacy Protections Across Browsers
1) Third-party Cookies Restrictions:While Google did not
deprecate TPC in Chrome with the Privacy Sandbox, some
new cookie management policies were implemented such as
the default changes to theSameSitecookie attribute [33],
8Despite UK’s exit from the EU, UK’s privacy laws are still very much
aligned with the EU’s ePrivacy Directive and GDPR.
as well as the opt-in possibility for third-parties to use the
Storage AccessAPI [73] andCHIPSpartitioned cookies.
In the meantime, other web browsers like Brave, Firefox,
and Safari already had or enabled by default several TPC
restrictions, as described below.
Braveapplies, perhaps, the most aggressive policy by
blocking all third-party application storage (e.g., cookies,
localStorage,indexedDB). Since 2021, to reduce web-
site breakage, third parties can only access an ephemeral and
partitioned storage for the duration of the session [16].
Firefoxhas been blocking TPC set by known trackers since
2019 withEnhanced Tracking Protection. In 2022, Firefox
rolled outTotal Cookie Protectionto partition in different
cookie jars all TPC per the first-party origin visited [74].
Safariblocks all TPC by default, but has a few exceptions in
place ifStorage Accessis being used or the third-party
domain was visited as first-party by the user in the last 30 days.
Additionally, an ML model detects domains with third-party
storage access that perform web tracking [5].
2) Other Privacy Features Shipped in the Meantime:In
parallel to Google’s initiative, the following privacy solutions
were made generally available by other browsers.
BraveproposedFarblingin 2020 as a redesign of its existing
fingerprinting defenses; now by default Brave is randomly
perturbing the output of browser APIs used by fingerprint-
ing scripts (e.g.,Canvas,WebGL,Audio,Plugins,UA,
EnumerateDevices, andHardwareConcurrency).
This is done in a way that still allows legitimate use of these
features by regular websites [15], [14].
Firefoxmade modifications to how client-side state is man-
aged through implementing network, state, and dynamic par-
titioning in 2021 and 2022, followed by more fingerprinting
protections adding noise to theCanvasAPI in 2023 [72].
Safarirolled outAdvanced Fingerprinting Protectionto pri-
vate mode in 2024 and made it generally available by default in
2025. These defenses include filtering of tracking parameters
in URLs, blocking network requests from known trackers, hid-
ing IP addresses, fixing values, and injecting noise into APIs
traditionally used by fingerprinters [95]. Note how in contrast
to the opt-in mitigations now in Chrome, these solutions have
been enabled by default on other browsers, thus enhancing
privacy for all of their users.
Recommendation R9-Vetted and meaningful privacy
protections should be rolled out by default to web users.
D. Adoption of the Android Proposals
We focus on the web APIs of the Privacy Sandbox, leaving
to future work a potential extension of the measurement to
the Android proposals. Nonetheless, we give some pointers
to researchers interested in such endeavors. We suggest using
a dataset of Android applications such asAndroZoo[3] to
access archival versions of different smartphone applications
and create an.apkdecompiler to detect the potential use of
the Android APIs. This could be complemented with scanning
11

popular open-source Android apps or libraries, as the source
code and historical versions are readily available.
VIII. RELATEDWORK ONMEASUREMENT
The analyses on the Privacy Sandbox can be broadly
divided into two categories: (a) privacy evaluations of the
guarantees claimed by some proposals (see Section II-B),
and (b) measurement studies of an individual proposal or a
subset of them (described thereafter). In comparison to our
approach’s scope, the following measurements were on limited
APIs, narrow time periods, specific invocation methods, or a
combination thereof (refer to overview in Table IX). Instead,
we systematically cover all features that were made available
in Chrome, monitor their adoption longitudinally thanks to
historical data (5+ years), on the top 100k websites (per CrUX
rank) and as experienced by Chrome users when browsing.
A. Measurement of Individual Proposals
Protected Audience.In 2022, the demand-side plat-
form (DSP) RTB House published a whitepaper sharing some
findings on their early experiments performed onProtected
Audiencethrough their integrations with some of their
partners, i.e., supply-side platforms (SSP) and publishers [82].
Between April and August 2022, RTB House reports having
added 1.2M users to interest groups around the world and
made over 7MProtected Audienceimpressions. Over-
all, RTB House noticed a low engagement from the advertising
industry; observing only Google and Criteo performing other
tests, SSPs prioritizing other integrations or waiting for more
clarity on how auctions will be executed, and publishers being
largely unaware of the Privacy Sandbox origin trials. Caldero-
nio et al., studied theProtected Audienceecosystem
just around its official deployment by crawling the Tranco top
70k websites from June to September 2023 [17], and found
that the majority of the ad auctions through the API were
run by Google. A result observed as well by Philipse et al.,
in their own crawl of the Tranco 10k websites performed in
December 2023 from an EU (Amsterdam) and US (New York
City) location [79]. In addition to confirming the prevalence
of Google’s DoubleClick in the calls to theProtected
Audience, they also found 6 other advertising companies,
and exposed and analyzed their bidding logic. They also
observed as much as 3 times more calls toTopicsthan
Protected Audience, and overall much fewer requests
to join interest groups when crawling from the EU than the
US, likely due to the simplicity of callingTopicsand to EU
consent regulations, respectively.
UA Client Hints.In June 2023, Senol et al., quantified
that high-entropyUA Client Hintswere accessed on
about 60% of the home pages of the top 100k websites [85].
They found that a majority of these calls were made by track-
ers and advertisers through JS (limited use of HTTP headers)
and that the API results were routinely exfiltrated to remote
servers. In a different measurement, Wiefling et al., looked into
the use ofClient Hintsheaders, an earlier mechanism
introduced in 2013 from whichUA Client Hintsis the
most widely implemented category. In this study, Wiefling
et al., queried HA data from July 2017 to December 2023
and crawled 327k login pages monthly from August 2022 to
December 2023, also finding concerning access rates toUA
Client Hintsin third-party contexts [94]. In a followup,
Ilgaz et al., complemented the prior studies onClient
Hintsheaders by investigating their usage in HTTP/2 and
HTTP/3 on a crawl of the top 100k websites in April 2025
from an EU (Amsterdam) and US (New York City) loca-
tion [63]. The reported results show a five to ten-fold growth
in adoption rates in 2025 compared to 2023 measurements.
RWS.McQuistin et al., carried out a user study showing that
users failed to correctly identify that a relationship often exists
between websites of a sameRWS[71]. Additionally, they also
parsed and reported on the pull requests from November 2022
to March 2024 on the GitHubRWSrepository that Google
used to manage edits to theRWSlist.
CHIPS.Z ¨ollner et al., studied the adoption of partitioned
cookies among the HA data from May 2022 to September
2024 [97]. Their analysis showcased an increase in adoption
ofCHIPSaround the start of the TPC deprecation test in
Chrome, and a slow-down even before the announcement that
TPC would still be supported. They also found asymmetric
choices being made by adopters on enablingCHIPSby default
or only on certain pages and sites, and pointed out to mistakes
in the implementation by some developers of the new default
requirements for theSameSiteattribute.
Topics.Verna et al., measured the prevalence of the
TopicsAPI on the top 50k websites weekly from August
2024 to March 2025 [91]. Their crawler being consent-aware
recorded if the API was used before or after consent was
given and from different locations using a VPN. They found
thatTopicswas quite often triggered before any consent
to user cookies or similar tracking technologies was granted,
which could be interpreted as a privacy violation under some
regulations such as GDPR. They also briefly discussed the
need to have an attestation to call some specific APIs.
B. Measurement of a Subset of Proposals
Sincera.Johnson et al., partnered with Sincera, an advertis-
ing telemetry service, to obtain data and release an online
dashboard on the adoption of 3 different APIs (Protected
Audience,RWS, andTopics) on a panel of about 60k
websites from May 2023 to June 2025 [67], [66]. As far as
we can tell, since Sincera’s acquisition by another ad tech
provider, the data sharing with the researchers has ceased and
the online dashboard has been taken down.
Web Almanac.The second initiative comes from the Web
Almanac’s yearly reports on the state of the web. These
are based on the analysis by volunteers and experts of
a single HA monthly crawl. The 2024 and 2025 cook-
ies chapters [9], [13] presented some results onCHIPS,
RWS, and the attestation process. The 2024 privacy chap-
ter [90] touched on a limited analysis ofAttribution
Reporting,FLoC,Protected Audience,Topics,
andUA Client Hints.
12

TABLE IX: Comparison of prior work on the measurement adoption of Privacy Sandbox APIs.
Work
Attestation
Attr. Reporting
CHIPS
FedCM
FLoC
Fenced Frames
Private Aggregation
Priv. State Tokens
Protected Audience
RWS
Shared Storage
Storage Access
Topics
UA Client HintsVantage Point (Timeline)
Open Data
RTB House [82] DSP access (Apr-Aug’21)✗
Senol et al. [85] CrUX 100k (Jun’23)✓
Wiefling et al. [94] HA top 8M (Jul’17-Dec’23) + 327k login pages (Aug’22-Dec’23) ✓∗
Calderonio et al. [17] Tranco 70k (Jun-Sep’23)✗
Philipse et al. [79] Tranco 10k (Dec’23)✓
McQuistin et al. [71] RWSedits (Nov’22-Mar’24)✓
Z¨ollner et al. [97] HA top 8M (May’22-Sep’24)✓
Johnson et al. [67], [66] Sincera access (May’23-Jun’25)✗
Web Almanac [9], [90], [13] HA top 1M (Jun’24 + Jul’25)✓
Verna et al. [91] Tranco 50k (Mar’24 + Aug’24-Mar’25)✓
Ilgaz et al. [63] Tranco 100k (Apr’25)✓
Grib et al. [61] (concurrent work) Tranco 10k (Jun’25-Jan’26)✓
Ours
HA top 100k (Mar’21-Apr’26) +
Chrome Telemetry (Jan’20-Apr’26) +
Attestation edits (Jun’24-Jul’25) +
RWSedits (Nov’22-Jul’25)
✓
: Limited analysis. : Partial instrumentation only, e.g., JS API(s) and/or HTTP header(s) missing.✓ ∗: Artifact only partially available.
Concurrent Work.Finally, while preparing this submission
we came across a much smaller consent-aware measurement
than ours from Grib et al. [61]. The approach in this concurrent
work is complimentary to ours on some aspects as it provides
pre- and post-consent measurement, validating for instance
our observation that some adopters were calling the Privacy
Sandbox APIs without user consent. However, the scale of our
measurement is unmatched: when we systematically measured
alldifferent ways to invoke (JS, HTML attributes, and HTTP
headers listed in Table XI) and useall13 APIs from the
Privacy Sandbox, they only partially instrumented a subset of
these APIs as reported by Table IX. Moreover, this concurrent
work is only based on data and trends on the top 10k websites
and for the last 6 months of 2025 (when adoption rates had
long stabilized), when we have access to theentireadoption
timeline (7+ years from first detection in January 2020 to
April 2026) and on the top100kwebsites. As a result, our
measurement study remains the largest of its kind and is
the only one able to provide a longitudinal view into the
prevalence of each feature during the full lifetime of the
Privacy Sandbox initiative.
IX. CONCLUSION
Our longitudinal results demonstrate how adoption of the
newly proposed Privacy Sandbox APIs and technologies re-
mained very limited and uneven across the years. The adoption
rates of the flagship, but now discontinued,Attribution
Reporting,Protected Audience, andTopicsAPIs
never reached more than 23.1%, 5.7%, and 14% of page
loads, respectively. For APIs still supported by Chrome,
the situation is similarly uneven; adoption rates forFedCM,
Fenced Frames, andStorage Accesshave been lower
than 5.2%, while partitioned cookies (CHIPS) are present on
34.5% of page loads, but only account for 6.7% of third-party
cookies (TPC) on average, andUA Client HintsAPI is
being accessed on more than 62% of page loads.
If anything, Google’s global experiment with the Privacy
Sandbox has taught us that only a few actors are willing to
experiment with new proposals that may or not be deployed,
and that even then, they tend to focus on the technologies
that would affect their main use cases or services such as
(re)targeted advertising or conversion measurement. We can
also expect that potential future attempts from Google at
disrupting web tracking and deprecating TPC will be met with
even more skepticism from the ecosystem knowing that the
Privacy Sandbox plans did not go through.
Ultimately, the continuing (ab)use ofUA Client Hints
by the ecosystem is emblematic of thecat-and-mouse game
of trackers circumventing privacy protections adopted by
browsers and users, and further showcases the need to properly
consider the fingerprinting potential of newly introduced web
APIs; as expressed by the W3C Privacy Working Group in
their guidance note [62]. Perhaps, more striking are the limi-
tations and disparities across browser vendors of“fix it in the
browser”remedies that the Privacy Sandbox illustrates once
more; while Google’s global experiment resulted in largely
opt-in only restrictions being implemented in Chrome, stronger
privacy protections were enabled by default in the meantime
into other browsers (e.g., Brave, Firefox, and Safari).
13

ACKNOWLEDGMENT
The authors thank Kyle Domico, Jonathan Gregory, Kun-
yang Li, Jean-Charles Noirot Ferrand, and Jack West for their
feedback on initial versions of this paper.
Funding acknowledgment:This material is based upon work
supported by the National Science Foundation under Grant
No. CNS-2343611. Any opinions, findings, and conclusions
or recommendations expressed in this material are those of the
author(s) and do not necessarily reflect the views of the Na-
tional Science Foundation. This work was supported in part by
the Semiconductor Research Corporation (SRC) and DARPA.
The data analysis on BigQuery was also made possible by
support provided through Google Cloud Research Credits
program with the award GCP-012E72-720588-E16BBE.
ETHICSCONSIDERATIONS
This work is a longitudinal measurement of the adoption of
Google’s Privacy Sandbox APIs based on existing and pub-
licly available datasets that did not require to crawl websites
ourselves. Nevertheless, we analyze next the limited ethical
implications of our work, before justifying conducting it.
Data Collection.Our work uses the following datasets:
(1)Chrome Telemetry:aggregated and anonymous statistics
on features usage publicly released by Google, i.e., with
no identifiable information available or recoverable about
Chrome users who have telemetry turned on. (2)HTTP
Archive:archival crawl results for millions of URLs and
pages visited each month from Chrome on a desktop and
(emulated) Android devices. This is a well established
non-profit project whose collected data to be queried by
anyone, this avoids redundant similar crawls of websites
by independent actors and allows to study the evolution of
the web. The crawl identifies itself by appending aPTST
token to its User-Agent in case web servers would like to
block it. (3)Open-source repositories:we use public version
control information from thechromiumandRWSrepositories
to collect the attestation andRWSlists shipped in Chrome.
Stakeholder Analysis.Our work encompasses six
stakeholders: (1)Online users: are individuals whose
web activity is traditionally tracked and profiled. They decide
which web browsers, extensions, and other privacy settings to
use. (2)Browser vendors: are the developers of user-agents
that browse and mediate access to the web on behalf of
users. They need to consider which features, proposals,
and standards to support and implement while balancing
security, privacy, usability, performance, and compatibility
issues. Here, Google Chrome is behind the Privacy Sandbox
initiative. (3)Website publishers: are in charge of managing
websites, maintaining their functionality, and monetizing their
content while new privacy and security changes are proposed
to the web. Some Privacy Sandbox APIs were intended
for website publishers (i.e., first-party). (4)Advertising
and tracking platforms: are services that provide online
tracking and advertising infrastructures. They are affected by
regulatory changes, new browser policies or modifications,
and public scrutiny. Several Privacy Sandbox APIs were
aimed at being adopted by such third-parties. (5)Regulators
and policymakers: are entities that draft, propose, and enforce
data protection regulations and privacy laws. They often rely
on measurements to better understand ecosystems dynamics.
The UK’s CMA was investigating Google’s proposals
and cookies deprecation on Chrome. (6)Researchers:
scientists from academia and industry studying modifications
to the web and effects on privacy, advertising, regulations, etc.
Positive Impacts of the Research.(1)Improved Understanding
(Impact on all Stakeholders): by performing the largest
measurement of its kind of the Privacy Sandbox proposals,
we shed light on which APIs were used in practice, how,
and by which actors over time. This provides the most
accurate existing overview of the events and ecosystem
dynamics related to the adoption and deprecation of these
proposals. (2)Future Research Directions (Impact on Browser
Vendors, Regulators, and Researchers): by discussing the
main research challenges in evaluating these proposals, we
identify several directions where browser vendors, regulators,
and researchers could work on to improve the web in future
efforts. (3)Informing Platform and Policy Design (Impact
on Browser Vendors and Regulators): by synthesizing years
of developments, this work informs about the main issues
and gaps uncovered in the Privacy Sandbox, while suggesting
future policy changes—both at browser and legal-levels.
Negative Impacts of the Research.(1)Potential for Incorrect
Detection (Impact on Adopters): to detect JavaScript imple-
mentations of the Privacy Sandbox APIs, we used a syntactic
matching technique that could lead to some false positives if
the API method was present in a comment or in a branch not
taken by the execution path. Similarly, detections could have
been missed if obfuscation techniques were used. To control
for these, we only look for JavaScript implementations on
pages for which Chrome is already reporting the use of one
of the APIs. This reduces the possibility that adopters have
been flagged incorrectly or are missing. (2)Misinterpretation
of Findings (Impact on Policy): Policy actors may selectively
use parts of our findings to justify particular technical or
regulatory choices, potentially ignoring some nuanced trade-
offs. Specifically, we caution against interpreting our findings
as definitive evidence of non-compliance from some adopters.
Indeed, we are not lawyers, the legality of calling these Privacy
Sandbox APIs prior to user consent has not been debated as far
as we know, and a more controlled experiment (such as using a
consent-aware crawler interacting with consent banners) would
likely be required to confirm violations.
Justification for Research.Despite the prior risks, several
factors already explained above also help mitigate the high-
lighted potential negative impacts. As such, we believe that
publishing this work is ethically justified and necessary. The
primary ethical risk lies in not reflecting on the changes
brought by Google’s Privacy Sandbox global experiment and
to miss the opportunity to better understand the dynamics in
14

the ecosystem and what happened. By linking our measure-
ment findings to recommendations, we aim to encourage a
reflection on lessons that can be learned with respect to solving
novel research challenges, building better privacy enhancing
technologies, providing more accountability, and enforcing
regulations. Overall, this measurement study contributes to an
ethically grounded understanding of the web, its evolution, and
challenges faced by privacy proposals.
REFERENCES
[1] Hidayet Aksu, Badih Ghazi, Pritish Kamath, Ravi Kumar, Pasin Ma-
nurangsi, Adam Sealfon, and Avinash V . Varadarajan. Summary
Reports Optimization in the Privacy Sandbox Attribution Reporting
API.Proceedings on Privacy Enhancing Technologies, 2024. https:
//doi.org/10.56553/popets-2024-0132
[2] Mir Masood Ali, Binoy Chitale, Mohammad Ghasemisharif, Chris
Kanich, Nick Nikiforakis, and Jason Polakis. Navigating Murky Waters:
Automated Browser Feature Testing for Uncovering Tracking Vectors.In
Proceedings 2023 Network and Distributed System Security Symposium.
2023. https://doi.org/10.14722/ndss.2023.24072
[3] Kevin Allix, Tegawend ´e F. Bissyand ´e, Jacques Klein, and Yves Le
Traon. AndroZoo: Collecting Millions of Android Apps for the Research
Community.In Miryung Kim, Romain Robbes, and Christian Bird,
editors, Proceedings of the 13th International Conference on Mining
Software Repositories, MSR 2016. 2016. https://doi.org/10.1145/2901
739.2903508
[4] M ´ario S. Alvim, Natasha Fernandes, Annabelle McIver, and Gabriel H.
Nunes. The Privacy-Utility Trade-off in the Topics API.In Proceedings
of the 2024 on ACM SIGSAC Conference on Computer and Communi-
cations Security. 2024. https://doi.org/10.1145/3658644.3670368
[5] Apple. Tracking Prevention in WebKit, 2020. https://webkit.org/trackin
g-prevention/
[6] HTTP Archive. The HTTP Archive, 2010. https://httparchive.org/
[7] HTTP Archive. Methodology|The Web Almanac by HTTP Archive,
2025. https://almanac.httparchive.org/en/2025/methodology
[8] Alex Berke and Dan Calacci. Privacy Limitations of Interest-Based Ad-
vertising on The Web: A Post-Mortem Empirical Analysis of Google’s
FLoC.In Proceedings of the 2022 ACM SIGSAC Conference on
Computer and Communications Security, CCS ’22. 2022. https:
//doi.org/10.1145/3548606.3560626
[9] Yohan Beugin, Sam Dutton, Yana Dimova, Rowan Merewood, and Barry
Pollard. The 2024 Web Almanac: Cookies. In The 2024 Web Almanac.
2024. https://doi.org/10.5281/zenodo.14065903
[10] Yohan Beugin and Patrick McDaniel. Interest-disclosing Mechanisms
for Advertising are Privacy-Exposing (not Preserving).Proceedings on
Privacy Enhancing Technologies Symposium (PETS), 2024. https://doi.
org/10.56553/popets-2024-0004
[11] Yohan Beugin and Patrick McDaniel. A Public and Reproducible
Assessment of the Topics API on Real Data.In IEEE Security and
Privacy Workshop on Designing Security for the Web (SecWeb). 2024.
https://doi.org/10.48550/arXiv.2403.19577
[12] Yohan Beugin and Patrick McDaniel. Technical Report: The Need for
a (Research) Sandstorm through the Privacy Sandbox, 2025. https:
//doi.org/10.48550/arXiv.2512.03207
[13] Yohan Beugin, Jannis Rautenstrauch, Martina Kraus, Chris B ¨ottger,
Brian Smith, and Barry Pollard. The 2025 Web Almanac: Cookies.
In The 2025 Web Almanac. 2026. https://doi.org/10.5281/zenodo.182
46755
[14] Brave. Fingerprint Randomization, 2020. https://brave.com/privacy-u
pdates/3-fingerprint-randomization/
[15] Brave. Fingerprinting Defenses 2.0, 2020. https://brave.com/privacy-u
pdates/4-fingerprinting-defenses-2.0/
[16] Brave. Ephemeral Third-Party Site Storage, 2021. https://brave.com/pr
ivacy-updates/7-ephemeral-storage/
[17] Giuseppe Calderonio, Mir Masood Ali, and Jason Polakis. Fledging
Will Continue Until Privacy Improves: Empirical Analysis of Google’s
Privacy-Preserving Targeted Advertising.In 33rd USENIX Security
Symposium (USENIX Security 24). 2024. https://www.usenix.org/c
onference/usenixsecurity24/presentation/calderonio
[18] C. J. Carey, Travis Dick, Alessandro Epasto, Adel Javanmard, Josh
Karlin, Shankar Kumar, Andres Munoz Medina, Vahab Mirrokni,
Gabriel Henrique Nunes, Sergei Vassilvitskii, and Peilin Zhong. Mea-
suring Re-Identification Risk, 2023. https://doi.org/10.48550/arXiv.230
4.07210
[19] Anthony Chavez. Expanding Testing for the Privacy Sandbox for the
Web, 2022. https://blog.google/products-and-platforms/products/chro
me/update-testing-privacy-sandbox-web/
[20] Anthony Chavez. The next Stages of Privacy Sandbox: General Avail-
ability and Supporting Scaled Testing, 2023. https://privacysandbox.goo
gle.com/blog/the-next-stages-of-privacy-sandbox-general-availability
[21] Anthony Chavez. Privacy Sandbox for the Web Reaches General
Availability, 2023. https://privacysandbox.google.com/blog/privacy
-sandbox-for-the-web-reaches-general-availability
[22] Anthony Chavez. A New Path for Privacy Sandbox on the Web, 2024.
https://privacysandbox.google.com/blog/privacy-sandbox-update
[23] Anthony Chavez. Next Steps for Privacy Sandbox and Tracking
Protections in Chrome, 2025. https://privacysandbox.google.com/bl
og/privacy-sandbox-next-steps
[24] Anthony Chavez. Update on Plans for Privacy Sandbox Technologies,
2025. https://privacysandbox.google.com/blog/update-on-plans-for-pri
vacy-sandbox-technologies
[25] Competition and Markets Authority. Investigation into Google’s ‘Privacy
Sandbox’ Browser Changes, 2025. https://www.gov.uk/cma-cases/inves
tigation-into-googles-privacy-sandbox-browser-changes
[26] John Delaney, Badih Ghazi, Charlie Harrison, Christina Ilvento, Ravi
Kumar, Pasin Manurangsi, Martin P ´al, Karthik Prabhakar, and Mariana
Raykova. Differentially Private Ad Conversion Measurement.Proceed-
ings on Privacy Enhancing Technologies, 2024. https://doi.org/10.565
53/popets-2024-0044
[27] Travis Dick, Alessandro Epasto, Adel Javanmard, Josh Karlin,
Andr´es Mu ˜noz Medina, Vahab Mirrokni, Sergei Vassilvitskii, and Peilin
Zhong. Differentially Private Synthetic Data Release for Topics API
Outputs.In Proceedings of the 31st ACM SIGKDD Conference on
Knowledge Discovery and Data Mining V .2, KDD ’25. 2025. https:
//doi.org/10.1145/3711896.3737391
[28] Sam Dutton. Third-Party Cookies Restricted by Default for 1% of
Chrome Users, 2024. https://privacysandbox.google.com/blog/coo
kie-countdown-2024jan
[29] Alessandro Epasto, Andres Munoz Medina, Christina Ilvento, and Josh
Karlin. Measures of Cross-Site Re-Identification Risk: An Analysis of
the Topics API Proposal, 2022. https://github.com/patcg-individual-dra
fts/topics/blob/main/topics analysis.pdf
[30] Alessandro Epasto, Andr ´es Mu ˜noz Medina, Steven Avery, Yijian Bai,
Robert Busa-Fekete, CJ Carey, Ya Gao, David Guthrie, Subham Ghosh,
James Ioannidis, Junyi Jiao, Jakub Lacki, Jason Lee, Arne Mauser,
Brian Milch, Vahab Mirrokni, Deepak Ravichandran, Wei Shi, Max
Spero, Yunting Sun, Umar Syed, Sergei Vassilvitskii, and Shuo Wang.
Clustering for Private Interest-Based Advertising.In Proceedings of
the 27th ACM SIGKDD Conference on Knowledge Discovery & Data
Mining, KDD ’21. 2021. https://doi.org/10.1145/3447548.3467180
[31] Google. WICG/Ua-Client-Hints. Web Incubator CG, 2018. https://gith
ub.com/WICG/ua-client-hints
[32] Google. Chromium Docs - UseCounter Wiki, 2019. https://chromium
.googlesource.com/chromium/src/+/HEAD/docs/use counter wiki.md
[33] Google. Developers: Get Ready for New SameSite=None; Secure
Cookie Settings, 2019. https://blog.chromium.org/2019/10/develo
pers-get-ready-for-new.html
[34] Google. Potential Uses for the Privacy Sandbox, 2019. https://blog.chr
omium.org/2019/08/potential-uses-for-privacy-sandbox.html
[35] Google. WICG/Attribution-Reporting-Api. Web Incubator CG, 2019.
https://github.com/WICG/attribution-reporting-api
[36] Google. WICG/First-Party-Sets. Web Incubator CG, 2019. https://gith
ub.com/WICG/first-party-sets
[37] Google. WICG/Floc. Web Incubator CG, 2019. https://github.com/W
ICG/floc
[38] Google. WICG/Trust-Token-Api. Web Incubator CG, 2019. https:
//github.com/WICG/trust-token-api
[39] Google. Storage Access API - Web APIs|MDN, 2020. https://develo
per.mozilla.org/en-US/docs/Web/API/Storage Access API
[40] Google. W3c-Fedid/FedCM. W3C FedID WG, 2020. https://github.c
om/w3c-fedid/FedCM
[41] Google. WICG/Fenced-Frame. Web Incubator CG, 2020. https://github
.com/WICG/fenced-frame
15

[42] Google. WICG/Turtledove. Web Incubator CG, 2020. https://github.c
om/WICG/turtledove
[43] Google. Privacycg/CHIPS. Privacy Community Group, 2021. https:
//github.com/privacycg/CHIPS
[44] Google. What Is the Privacy Sandbox?, 2021. https://privacysandbox.g
oogle.com/overview/web
[45] Google. WICG/Shared-Storage. Web Incubator CG, 2021. https://gith
ub.com/WICG/shared-storage
[46] Google. Increasing the Privacy Sandbox Relevance and Measurement
Origin Trial to 5%, 2022. https://privacysandbox.google.com/blog/pri
vacy-sandbox-origin-trial-increase
[47] Google. Patcg-Individual-Drafts/Private-Aggregation-Api. Private Ad-
vertising Technology Community Group Individual Draft Space, 2022.
https://github.com/patcg-individual-drafts/private-aggregation-api
[48] Google. Patcg-Individual-Drafts/Topics. Private Advertising Technology
Community Group Individual Draft Space, 2022. https://github.com/p
atcg-individual-drafts/topics
[49] Google. Developer Enrollment for the Privacy Sandbox, 2023. https://pr
ivacysandbox.google.com/blog/announce-enrollment-privacy-sandbox
[50] Google. Privacysandbox/Attestation. The Privacy Sandbox, 2023. https:
//github.com/privacysandbox/attestation
[51] Google. Update on the Plan for Phase-out of Third-Party Cookies on
Chrome, 2024. https://privacysandbox.google.com/blog/update-on-the
-plan-for-phase-out-of-third-party-cookies-on-chrome
[52] Google. Deprecate and Remove: Attribution Reporting API - Chrome
Platform Status, 2025. https://chromestatus.com/feature/63206393759
66208
[53] Google. Deprecate and Remove: Private Aggregation API - Chrome
Platform Status, 2025. https://chromestatus.com/feature/46833829193
97376
[54] Google. Deprecate and Remove Protected Audience - Chrome Platform
Status, 2025. https://chromestatus.com/feature/6552486106234880
[55] Google. Deprecate and Remove: Related Website Sets (RWS) - Chrome
Platform Status, 2025. https://chromestatus.com/feature/51944738690
17088
[56] Google. Deprecate and Remove: Shared Storage API - Chrome Platform
Status, 2025. https://chromestatus.com/feature/5076349064708096
[57] Google. Intent to Deprecate and Remove: Topics API, 2025. https:
//groups.google.com/a/chromium.org/g/blink-dev/c/ R85yctz4Rs
[58] Google. Privacy-Related Compliance FAQs, 2025. https://privacysandb
ox.google.com/overview/privacy-compliance-faqs
[59] Google. Privacy Sandbox Feature Status, 2025. https://privacysandbox
.google.com/overview/status
[60] Google. Relevance and Measurement Unified Origin Trial|Privacy
Sandbox, 2025. https://web.archive.org/web/20250614061324/https:
//privacysandbox.google.com/private-advertising/setup/web/unified-ori
gin-trial
[61] Rachid Youssef Grib, Alberto Verna, Nikhil Jha, Martino Trevisan, and
Marco Mellia. The Rise and Fall of Google’s Privacy Sandbox, 2026.
https://doi.org/10.48550/arXiv.2607.00693
[62] W3C Privacy Working Group. W3c/Fingerprinting-Guidance. World
Wide Web Consortium, 2025. https://github.com/w3c/fingerprinting-g
uidance
[63] Sarp Ilgaz.Investigating High Entropy Client Hint usage in HTTP/2
and HTTP/3. Bachelor thesis, Radboud University, 2025. https://www.
cs.ru.nl/bachelors-theses/2025/Sarp Ilgaz 1093588 Investigating
High Entropy Client Hint usage in HTTP-2 and HTTP-3.pdf
[64] Jean Luc Intumwayase, Imane Fouad, Pierre Laperdrix, and Romain
Rouvoy. UA-Radar: Exploring the Impact of User Agents on the Web.In
Proceedings of the 22nd Workshop on Privacy in the Electronic Society,
WPES ’23. 2023. https://doi.org/10.1145/3603216.3624958
[65] Nikhil Jha, Martino Trevisan, Emilio Leonardi, and Marco Mellia. Re-
Identification Attacks against the Topics API.ACM Trans. Web, 2024.
https://doi.org/10.1145/3675400
[66] Garrett Johnson. Unearthing Privacy-Enhancing Ad Technologies
(PEAT): The Adoption of Google’s Privacy Sandbox, 2024. https:
//doi.org/10.2139/ssrn.4983927
[67] Garrett A Johnson and Nico Neumann. The Advent of Privacy-Centric
Digital Advertising: Tracing Privacy-Enhancing Technology Adoption,
2024. https://pep.gmu.edu/wp-content/uploads/sites/28/2024/04/Johnso
n-Neumann.pdf
[68] Guillaume Kessibi, Aymen Ould Hamouda, Charly Poirier, and Antoine
Boutet. A Complementary Utility and Privacy Trade-off Evaluation of
Google’s FloC API, 2022. https://inria.hal.science/hal-03953308v1/do
cument
[69] Elena Bakos Lang, Giacomo Pope, Giovanni De Ferrari, Huy Nguyen,
Lydia Yao, Thomas Pornin, Tyler Colgan, and Viktor Gazdag. Privacy
Sandbox Aggregation Service and Coordinator, 2024. https://www.fo
x-it.com/media/m3yogjsq/ ncc group google privacy sandbox publi
c report v2.pdf
[70] Minjun Long and David Evans. Evaluating Google’s Protected Audience
Protocol.Proceedings on Privacy Enhancing Technologies, 2024. https:
//doi.org/10.56553/popets-2024-0147
[71] Stephen McQuistin, Peter Snyder, Hamed Haddadi, and Gareth Tyson.
A First Look at Related Website Sets.In Proceedings of the 2024 ACM
on Internet Measurement Conference. 2024. https://doi.org/10.1145/36
46547.3689026
[72] MDN. State Partitioning - Privacy on the Web|MDN, 2024. https:
//developer.mozilla.org/en-US/docs/Web/Privacy/State Partitioning
[73] MDN. Storage Access API - Web APIs|MDN, 2024. https://develope
r.mozilla.org/en-US/docs/Web/API/Storage Access API
[74] Mozilla. Firefox Rolls Out Total Cookie Protection By Default To All
Users, 2022. https://blog.mozilla.org/en/mozilla/firefox-rolls-out-total-c
ookie-protection-by-default-to-all-users-worldwide/
[75] Alexandra Nisenoff, Deian Stefan, and Nicolas Christin. Exploiting
the Shared Storage API.In Proceedings of the 2025 ACM SIGSAC
Conference on Computer and Communications Security, CCS ’25. 2025.
https://doi.org/10.1145/3719027.3744848
[76] European Parliament and European Council. Directive 2002/58/EC of
the European Parliament and of the Council of 12 July 2002 Concerning
the Processing of Personal Data and the Protection of Privacy in the
Electronic Communications Sector (Directive on Privacy and Electronic
Communications), 2002. http://data.europa.eu/eli/dir/2002/58/oj/eng
[77] European Parliament and European Council. Directive 2009/136/EC
of the European Parliament and of the Council of 25 November
2009 Amending Directive 2002/22/EC on Universal Service and Users’
Rights Relating to Electronic Communications Networks and Services,
Directive 2002/58/EC Concerning the Processing of Personal Data and
the Protection of Privacy in the Electronic Communications Sector
and Regulation (EC) No 2006/2004 on Cooperation between National
Authorities Responsible for the Enforcement of Consumer Protection
Laws, 2009. http://data.europa.eu/eli/dir/2009/136/oj/eng
[78] patcg-individual-drafts. Fingerprinting Threat Using the TOPICS API·
Issue #74·Patcg-Individual-Drafts/Topics, 2023. https://github.com/p
atcg-individual-drafts/topics/issues/74#issuecomment-1603204126
[79] Michiel Philipse.Post-Third-Party Cookies: Analyzing Google’s Pro-
tected Audience API. Master thesis, Radboud University, 2024. https:
//www.cs.ru.nl/masters-theses/2024/M Philipse Post-Third-Party C
ookies Analyzing Google’s Protected Audience API..pdf
[80] Deepak Ravichandran and Sergei Vassilvitskii. Evaluation of Cohort
Algorithms for the FLoC API, 2020. https://raw.githubusercontent.co
m/google/ads-privacy/master/proposals/FLoC/FLOC-Whitepaper-Googl
e.pdf
[81] Eric Rescorla and Martin Thomson. Technical Comments on FLoC
Privacy, 2021. https://mozilla.github.io/ppa-docs/floc report.pdf
[82] Mateusz Rumi ´nski, Przemysław Iwa ´nczak, and Łukasz Włodarczyk.
Findings from the Early Fledge Experiments, 2022. https://doi.org/
10.2139/ssrn.4219796
[83] Justin Schuh. Building a More Private Web, 2019. https://blog.google/
products-and-platforms/products/chrome/building-a-more-private-web/
[84] Justin Schuh. Building a More Private Web: A Path towards Making
Third Party Cookies Obsolete, 2020. https://blog.chromium.org/2020/0
1/building-more-private-web-path-towards.html
[85] Asuman Senol and Gunes Acar. Unveiling the Impact of User-Agent
Reduction and Client Hints: A Measurement Study.In Proceedings of
the 22nd Workshop on Privacy in the Electronic Society, WPES ’23.
2023. https://doi.org/10.1145/3603216.3624965
[86] Martin Thomson. A Privacy Analysis of Google’s Topics Proposal, 2023.
https://mozilla.github.io/ppa-docs/topics.pdf
[87] Martin Thomson. Protected Audience Privacy Analysis, 2024. https:
//mozilla.github.io/ppa-docs/protected-audience.pdf
[88] Florian Turati, Karel Kubicek, Carlos Cotrini, and David Basin.
Locality-Sensitive Hashing Does Not Guarantee Privacy! Attacks on
Google’s FLoC and the MinHash Hierarchy System.Proceedings on
Privacy Enhancing Technologies, 2023. https://doi.org/10.56553/popet
s-2023-0101
16

[89] Yash Vekaria, Yohan Beugin, Shaoor Munir, Gunes Acar, Nataliia
Bielova, Steven Englehardt, Umar Iqbal, Alexandros Kapravelos, Pierre
Laperdrix, Nick Nikiforakis, Jason Polakis, Franziska Roesner, Zubair
Shafiq, and Sebastian Zimmeck. SoK: Advances and Open Problems in
Web Tracking, 2025. https://doi.org/10.48550/arXiv.2506.14057
[90] Yash Vekaria, Benjamin Standaert, Max Ostapenko, Abdul Haddi Am-
jad, Yana Dimova, Shaoor Munir, Chris B ¨ottger, Umar Iqbal, Alberto
Fernandez-de Retana, and Barry Pollard. The 2024 Web Almanac:
Privacy. In The 2024 Web Almanac. 2024. https://doi.org/10.5281/
zenodo.14261510
[91] Alberto Verna, Nikhil Jha, Martino Trevisan, and Marco Mellia. Under-
standing Topics API in the Wild: Dubious Usage and Stale Adoption.
IEEE Transactions on Privacy, 2025. https://doi.org/10.1109/TP.2025.
3615120
[92] Mike West. Mikewest/Privacy-Budget, 2019. https://github.com/mikew
est/privacy-budget
[93] Maximilian Westers, Andreas Mayer, and Louis Jannett. Single Sign-On
Privacy: We Still Know What You Did Last Summer.In 2024 Annual
Computer Security Applications Conference (ACSAC). 2024. https://do
i.org/10.1109/ACSAC63791.2024.00039
[94] Stephan Wiefling, Marian H ¨onscheid, and Luigi Lo Iacono. A Privacy
Measure Turned Upside Down? Investigating the Use of HTTP Client
Hints on the Web.In Proceedings of the 19th International Conference
on Availability, Reliability and Security, ARES ’24. 2024. https://doi.or
g/10.1145/3664476.3664478
[95] John Wilander, Charlie Wolfe, Matthew Finkel, Wenson Hsieh, and
Keith Holleman. Private Browsing 2.0, 2024. https://webkit.org/blo
g/15697/private-browsing-2-0/
[96] Yingtai Xiao, Jian Du, Shikun Zhang, Wanrong Zhang, Qiang Yan,
Danfeng Zhang, and Daniel Kifer. Click Without Compromise: On-
line Advertising Measurement via Per User Differential Privacy, 2025.
https://doi.org/10.48550/arXiv.2406.02463
[97] Maximilian Z ¨ollner, Anja Feldmann, and Ha Dao. A First Look at Cook-
ies Having Independent Partitioned State.In Cecilia Testart, Roland
van Rijswijk-Deij, and Burkhard Stiller, editors, Passive and Active
Measurement. 2025. https://doi.org/10.1007/978-3-031-85960-1 8
APPENDIXA
OPENSCIENCE
We release all our collection scripts, extraction queries,
datasets, analysis code, and documentation steps as a public
artifact to enable availability and reproducibility of our re-
search results. Our artifact can be accessed at the following
URL: https://github.com/privacysandstorm/ps-api-adoption-d
eprecation.
To foster future research and dissemination of our results
in a more accessible way and to a broader public, we will
also host on https://privacysandstorm.com/ an interactive
dashboard with graphs and statistics for visitors to explore
further our data.
APPENDIXB
ABBREVIATIONS
Table X lists the abbreviations used in this work.
TABLE X: List of abbreviations used in this paper.
Symbol Meaning
CHIPS Cookies Having Independent Partitioned State
CMA Competition and Markets Authority
CrUX Chrome User Experience Report
DSP Demand-side platform
FedCM Federated Credential Management
FLoC Federated Learning of Cohorts
GDPR General Data Protection Regulation
HA HTTP Archive
ID Identifier
JS JavaScript
OT Origin trial (test of a new feature in Chrome)
RWS Related Website Sets
SSP Supply-side platform
TPC Third-party cookies
UA User-Agent
APPENDIXC
SUPPLEMENTALTABLES ANDFIGURES
17

TABLE XI: Permissions policy directives, JS methods, and HTTP headers (if any) measured in this paper for each proposal.
The list is also available in our artifact in.JSONformat (see Appendix A).
Permissions Policy Directives JS Methods (and HTML Attributes) HTTP Headers
Attribution Reporting
attribution-reporting
conversion-measurement
XMLHttpRequest.setAttributionReporting
HTMLAnchorElement.attributionSrc
HTMLImageElement.attributionSrc
HTMLScriptElement.attributionSrc
Attribution-Reporting-Eligible
Attribution-Reporting-Register-Source
Attribution-Reporting-Register-Trigger
CHIPS Set-Cookie: Secure; Partitioned;
FLoC
interest-cohort
document.interestCohort
FedCM
identity-credentials-get
navigator.credentials.get
IdentityCredential.disconnect
IdentityProvider.close
IdentityProvider.getUserInfo
navigator.login.setStatus
Set-Login
Fenced Frames document.createElement("fencedframe")
window.Fence.getNestedConfigs
window.Fence.reportEvent
window.FencedFrameConfig.setSharedStorageContext
window.Fence.setReportEventDataForAutomaticBeacons
Sec-Fetch-Dest: fencedframe
Supports-Loading-Mode: fenced-frame
Private Aggregation
private-aggregation
privateAggregation.contributeToHistogram
privateAggregation.contributeToHistogramOnEvent
privateAggregation.enableDebugMode
Private State Tokens
private-state-token-issuance
private-state-token-redemption
trust-token-redemption
document.hasPrivateToken
document.hasRedemptionRecord
XMLHttpRequest.setPrivateToken
Sec-Private-State-Token
Sec-Private-State-Token-Lifetime
Sec-Private-State-Token-Crypto-Version
Sec-Redemption-Record
Protected Audience
join-ad-interest-group
run-ad-auction
navigator.joinAdInterestGroup
navigator.leaveAdInterestGroup
navigator.clearOriginJoinedAdInterestGroups
navigator.runAdAuction
navigator.adAuctionComponents
navigator.createAuctionNonce
Ad-Auction-Allowed
Ad-Auction-Only
Ad-Auction-Signals
Ad-Auction-Additional-Bid
X-fledge-bidding-signals-format-version
Data-Version
Sec-Ad-Auction-Fetch
RWS
top-level-storage-access
Shared Storage
shared-storage
shared-storage-select-url
window.sharedStorage.selectURL
window.sharedStorage.run
window.sharedStorage.set
window.sharedStorage.append
window.sharedStorage.delete
window.sharedStorage.clear
window.sharedStorage.worklet.addModule
window.sharedStorage.createWorklet
window.sharedStorage.worklet.run
window.sharedStorage.worklet.selectURL
window.sharedStorage.batchUpdate
Sec-Shared-Storage-Writable
Sec-Shared-Storage-Data-Origin
Shared-Storage-Write
Shared-Storage-Cross-Origin-Worklet-Allowed
Storage Access
storage-access
document.requestStorageAccess
document.requestStorageAccessFor
document.hasStorageAccess
document.hasUnpartitionedCookieAccess
Sec-Fetch-Storage-Access
Activate-Storage-Access
Topics
browsing-topics
document.browsingTopics Sec-Browsing-Topics
Observe-Browsing-Topics
UA Client Hints
ch-ua
ch-ua-arch
ch-ua-bitness
ch-ua-form-factors
ch-ua-full-version
ch-ua-full-version-list
ch-ua-high-entropy-values
ch-ua-mobile
ch-ua-model
ch-ua-platform
ch-ua-platform-version
ch-ua-wow64
navigator.userAgentData.toJSON
navigator.userAgentData.getHighEntropyValues
Accept-CH
Critical-CH
Delegate-CH
Sec-CH-UA*
18

Q1
2020
Q2 Q3 Q4 Q1
2021
Q2 Q3 Q4 Q1
2022
Q2 Q3 Q4 Q1
2023
Q2 Q3 Q4 Q1
2024
Q2 Q3 Q4 Q1
2025
Q2 Q3 Q4 Q1
2026
Q2
date
10−6
10−5
10−4
10−3
10−2
10−1
100
101
102
% page loads
❶ ❷ ❸ ❹ ❺ ❻ ❼ ❽ ❾ ❿
API
Attribution Reporting
CHIPS
FLoC
FedCM
Fenced Frames
Private Aggregation
Private State T okens
Protected Audience
Shared Storage
Storage Access
T opics
UA Client Hints
Fig. 7: General adoption rates (quarterly percentage of page loads) over time fromChrome Telemetrydataset (log-scale version
of Figure 2). Vertical numbered lines correspond to major development events (see Figure 1).
Q1
2021
Q2 Q3 Q4 Q1
2022
Q2 Q3 Q4 Q1
2023
Q2 Q3 Q4 Q1
2024
Q2 Q3 Q4 Q1
2025
Q2 Q3 Q4 Q1
2026
Q2
date
0
10
20
30
40
50
60% page loads
❶ ❷ ❸ ❹ ❺ ❻ ❼ ❽ ❾ ❿
api
Attribution Reporting
FedCM
Fenced Frames
Private State T okens
Protected Audience
Shared Storage
Storage Access
T opics
UA Client Hints
client
desktop
mobile
Fig. 8: General adoption rates (quarterly percentage of pages) over time fromHA-blinkdataset for desktop and mobile clients
(log-scale in Figure 9). Vertical numbered lines correspond to major development events (see Figure 1).
Q1
2021
Q2 Q3 Q4 Q1
2022
Q2 Q3 Q4 Q1
2023
Q2 Q3 Q4 Q1
2024
Q2 Q3 Q4 Q1
2025
Q2 Q3 Q4 Q1
2026
Q2
date
10−5
10−4
10−3
10−2
10−1
100
101
102
% page loads
❶ ❷ ❸ ❹ ❺ ❻ ❼ ❽ ❾ ❿
api
Attribution Reporting
FedCM
Fenced Frames
Private State T okens
Protected Audience
Shared Storage
Storage Access
T opics
UA Client Hints
client
desktop
mobile
Fig. 9: General adoption rates (quarterly percentage of pages) over time fromHA-blinkdataset for desktop and mobile clients
(log-scale in Figure 8). Vertical numbered lines correspond to major development events (see Figure 1).
19
