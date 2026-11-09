---
title: On the Differential Privacy and Interactivity of Privacy Sandbox Reports
url: https://doi.org/10.56553/popets-2025-0104
category: privacy-data
subcategory: measurement
date: 2025-05
venue: Proceedings on Privacy Enhancing Technologies
authors:
- Badih Ghazi
- Charlie Harrison
- Arpana Hosabettu
source: openalex-oa
pdf_url: https://petsymposium.org/popets/2025/popets-2025-0104.pdf
pages: 16
chars: 82322
fetched_at: '2026-11-08T17:31:43+00:00'
kb_version: 1
---

# On the Differential Privacy and Interactivity of Privacy Sandbox Reports

On the Differential Privacy and Interactivity of Privacy Sandbox
Reports
Badih Ghazi∗
Google
Mountain View, California, USA
badihghazi@gmail.com
Charlie Harrison∗
Google
Texas, USA
csharrison@google.com
Arpana Hosabettu∗
Google
Mountain View, California, USA
arpanah@google.com
Pritish Kamath∗
Google
Mountain View, California, USA
pritishk@google.com
Alexander Knop∗
Google
New York City, New York, USA
alexanderknop@google.com
Ravi Kumar∗
Google
Mountain View, California, USA
ravi.k53@gmail.com
Ethan Leeman∗
Google
Cambridge, Massachusetts, USA
ethanleeman@google.com
Pasin Manurangsi∗
Google
Bangkok, Thailand
pasin@google.com
Mariana Raykova∗
Google
New York City, New York, USA
marianar@google.com
Vikas Sahu∗
Google
Mountain View, California, USA
vikassahu@google.com
Phillipp Schoppmann∗
Google
New York City, New York, USA
schoppmann@google.com
Abstract
The Privacy Sandbox initiative from Google includes APIs for en-
abling privacy-preserving advertising functionalities as part of the
effort around limiting third-party cookies. In particular, the Pri-
vate Aggregation API (PAA) and the Attribution Reporting API
(ARA) can be used for ad measurement while providing different
guardrails for safeguarding user privacy, including a framework
for satisfying differential privacy (DP). In this work, we provide an
abstract model for analyzing the privacy of these APIs and show
that they satisfy a formal DP guarantee under certain assumptions.
Our analysis handles the case where both the queries and database
can change interactively based on previous responses from the API.
Keywords
Ads, Privacy Sandbox, Aggregation Service, Differential Privacy,
Individual Differential Privacy, Key Discovery, Requerying
1 Introduction
Third-party cookies have been a cornerstone of online advertis-
ing for more than two decades. They are small text files that are
stored on a user’s computer by websites other than the one they
are currently visiting, allowing websites to track users across the
internet and gather data about their browsing habits, thus enabling
∗Alphabetical author order.
This work is licensed under the Creative Commons Attribu-
tion 4.0 International License. To view a copy of this license
visit https://creativecommons.org/licenses/by/4.0/ or send a
letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
Proceedings on Privacy Enhancing Technologies 2025(3), 382–397
© 2025 Copyright held by the owner/author(s).
https://doi.org/10.56553/popets-2025-0104
advertisers and publisher to measure performance of ad campaigns.
However, in recent years, growing privacy concerns have led major
web browsers to take action: both Apple’s Safari [48] and Mozilla’s
Firefox [10] deprecated third-party cookies in2019 and 2021, respec-
tively; Google has made an informed choice proposal to explicitly
ask users to choose whether they want to disable or enable third-
party cookies [38]. This marks a significant change in the online
advertising landscape, increasing the need for new solutions that
prioritize user privacy.
In addition to the informed choice proposal, Google has led the
Privacy Sandbox [31] initiative, which includes a set of privacy-
preserving technologies aimed at replacing third-party cookie-
based ad measurement. Two key components of this initiative are
the Private Aggregation API (PAA) [32] and the Attribution Report-
ing API (ARA) [29], which seek to provide advertisers with reports
that yield insights into the performance of ad campaigns while
protecting user privacy. This is already rolled out and activated on
roughly 3.5% and 22.1% of all page loads in Chrome respectively
as of February 1, 2025 [40, 41]. These APIs offer various privacy
guardrails, including a framework [30] for satisfying differential
privacy (DP) [15, 16].
Recall that an advertising (ad, for short) campaign is a collection
of impressions, each of those indicating a user interaction: either a
user viewing an ad or clicking on one. The websites on which the ads
are displayed, and possibly clicked, are referred to aspublishers. The
goal of an ad campaign is to drive useful actions on the advertiser
website (e.g., purchases); these events are usually referred to as
conversions. Therefore, goal of measurement for advertiser is to
learn about campaign performance to answer questions like how
many users did this ad campaign reach or how many converted as
a result of this ad.
382

On the Differential Privacy and Interactivity of Privacy Sandbox Reports Proceedings on Privacy Enhancing Technologies 2025(3)
A main component of ARA and PAA are thesummary reports [28],
which enable the estimation of aggregate ad metrics such as the
average number of conversions that can be attributed to a certain
ad campaign [27], or the reach of the ad campaign [3, 37]. These
reports are usually sliced by some parameters called keys (e.g., the
ad-tech could slice by geography or a device type). Summary re-
ports have been proposed in two flavors depending on whether the
set of keys over which the aggregates are sliced is pre-specified
or not; the latter is referred to as key discovery [2] and arises in
practical settings where the set of attributes (pertaining to the ad,
publisher, advertiser and/or user) is very large. In addition, it was
proposed to extend summary reports to enable requerying [50],
which would allow analysts to aggregate their measurement re-
ports on different overlapping slices in an interactive manner (i.e.,
where the output of previous queries can influence the choice of
the subsequent queries issued by the analyst).
ARA also offers event-level reports [26], which can provide for
each ad impression, a discretized and noisy estimate of the list of
conversions and conversion values attributed to this impression.
This type of data enables the training of ad conversion models,
which are machine learning models that predict the expected num-
ber of conversions (or the conversion value) that would be driven
by an ad impression. The output of these ML models is typically
used as input when determining the bid price in the online auctions
that power automated bidding across the Web.
Despite being deployed in the web browsers of hundreds of
millions of users and supporting critical ad functionalities, the
privacy guarantee of neither ARA nor PAA has been formalized
rigorously. This gap has been raised in recent work [42, 51].
Our Contributions. In this work, we address this gap and obtain
several results formalizing the DP properties of ARA and PAA.
Specifically:
• We prove that summary reports in ARA and PAA as well as
event-level reports in ARA satisfy a formal DP guarantee even
in a highly interactive setting (which captures common practical
use cases) where the queries and the underlying database can
change arbitrarily depending on previous reports.
• Our privacy proof for ARA and PAA summary reports applies
to the aforementioned proposed extensions that would support
key discovery and requerying.
Note, however, that both ARA and PAA protect only the cross-
website (a.k.a. “third-party”) information while the single-website
(a.k.a. “first-party”) information is assumed to be known to the ad-
tech1. For example, if a user is logged-in on the publisher website,
then the publisher knows the ads shown to the user and if a user is
logged-in on the advertiser website, then the advertiser knows the
user’s conversions. However, if the two websites do not share the
same login credentials, the ad-tech will be unable to attribute the
conversion to the ad shown, without third party cookies. The ARA
allows the ad-tech to access this attribution information, but in a
privacy-preserving manner.
1In this work, we use the term ad-tech to refer to an analyst that performs analysis on
ads and their attributed conversions, thereby helping publishers and advertisers with
the placement and measurement of digital ads.
1.1 Related Work
Differential Privacy. Over the last two decades, DP [15, 16] has
become a widely popular notion of privacy in data analytics and
modeling, due to its compelling mathematical properties and the
strong guarantees that it provides. It has been used in several prac-
tical deployments in government agencies (e.g., [ 7, 22]) and the
industry (e.g., [21]); we refer the reader to [14] for a list covering
many deployments. As DP is rolled out in ad measurement to re-
place third-party cookies, it is likely to become one of the largest,
if not the largest, real-world deployment of DP, in terms of the
number of daily queries and affected users.
Private Ad Measurement. In addition to the Privacy Sandbox on
Google Chrome and Android, several other APIs have been pro-
posed by various browsers, ad-tech companies, and researchers.
These include Private Click Measurement (PCM) on Safari [ 49],
SKAdNetwork on iOS [5], Interoperable Private Attribution (IPA)
that was developed by Meta and Mozilla [43], Masked LARK from
Microsoft [23], and Cookie Monster which was recently introduced
in [42]. All of these APIs, except PCM, use DP to ensure privacy.
We note that our proof, inspired by Cookie Monster [ 42] is us-
ing individual differential privacy accounting. Interestingly, while
CookieMonster analyzes a similar setting, their notion of adjacency
assumes that only impressions, or only conversions are known
to the adversary. In other words, CookieMonster setting assumes
the ability to hide impressions and/or conversions from the adver-
sary, which may not be compatible with proposed APIs from most
browsers, in particular the ARA and the PAA.
The recent work of [12] studied the interplay between attribution
and DP budgeting for an abstract conversion measurement system.
It showed that depending on the attribution logic (e.g., first-touch,
last-touch, uniform), the privacy unit (e.g., per impression, per user
× publisher, per user× advertiser), and whether contribution cap-
ping is performed before or after attribution, the sensitivity of the
output aggregate can increase with the number of publishers and
advertisers rendering the noise too high for accurate measurements.
There has also been recent work on optimizing the utility of
the Privacy Sandbox ARA summary reports. For hierarchical query
workloads, [11] gave algorithms for denoising summary reports, en-
suring consistency, and optimizing the contribution budget across
different levels of the hierarchy. On the other hand, [1] presented
methods for optimizing the allocation of the contribution budget
for general (not necessarily hierarchical) workloads.
Finally, there has been recent work on DP ad (click and conver-
sion) modeling (e.g., [8, 13, 44]), some of it based on the Privacy
Sandbox APIs.
Organization. Section 2 provides a simplified description of ARA
and PAA; we focus primarily on details relevant for our analysis.
Section 3 provides formal notations, covers basic background on DP
and defines the notion of an interactive mechanism and adversary
that is relevant for our modeling of ARA and PAA. In Section 4, we
model summary reports of ARA and PAA and provide the formal DP
guarantee for the same. In Section 5 we model event-level reports
of ARA and provide a formal DP guarantee.
383

Proceedings on Privacy Enhancing Technologies 2025(3) Ghazi et al.
2 Privacy Sandbox Measurement APIs
We next describe the details of the ARA and PAA APIs and their
role in collecting measurements about ads and their attributed con-
versions. (See Table 2 for a glossary of the involved terminology.)
The Attribution Reporting API (ARA) enables ad-techs to mea-
sure ad-conversions in a privacy-preserving manner (without third-
party cookies). In particular, ARA supports two types of reports:
• summary reports, that allow collecting aggregated statistics of
ad campaigns and their “attributed” conversions, and
• event-level reports, that associate a particular ad with very limited
(and noisy) data on the conversion side, which are sent with a
larger time delay.
The Private Aggregation API (PAA) is another API that also
supports summary reports for collecting aggregated statistics in
a privacy-preserving manner. While it is a general API (not nec-
essarily about ads), a typical use-case is in estimating reach (the
number of users who were exposed to an ad) and frequency (the
number of users that were exposed to an ad𝑘 times, for each𝑘).
We first provide a high-level overview of thesummary reports
in ARA and PAA (in Section 2.1), and of the event-level reports in
ARA (in Section 2.2).
2.1 Summary Reports
Summary reports in both ARA and PAA rely on two main com-
ponents: (i) the client, which runs in the browser, and (ii) the ag-
gregation service, which runs in a trusted execution environment
(TEE) [18]. Each client performs local operations based on browser
activity and sends aggregatable reports to ad-techs. (The exact
mechanism that generates these reports is different for ARA and
PAA, and we explain this shortly.) Formally, an aggregatable re-
port is a tuple(𝑟,𝑘,𝑣,𝑚 ) containing a key𝑘 ∈K :={0, 1}128, a
value 𝑣 ∈ {0, 1,..., Λ1} (where Λ1 := 216), a random identifier
𝑟 ∈ I:={0, 1}128 unique to each report (the Privacy Sandbox
implementation uses AEAD [ 47] to ensure that the identifier is
tamper-proof), and some metadata𝑚 that can depend on “trigger
information” as explained later. Here,𝑘 and𝑣 are encrypted, where
the secret key for decrypting is held by the aggregation service
thereby ensuring that an ad-tech cannot see them and𝑚 is visible
to the ad-tech in the clear, who can use it to batch the reports for
aggregation. For simplicity, henceforth, we drop𝑚 from aggregate
reports as it does not affect the privacy analysis.
2.1.1 Aggregation Service. Ad-techs can send a subset of the re-
ports,𝑆 ={(𝑟1,𝑘 1,𝑣 1),..., (𝑟𝑛,𝑘𝑛,𝑣𝑛)}, they hold (filtered based on
the available metadata) to the aggregation service, with the goal
of learning, for any 𝑘∈K , the aggregated value𝑤𝑘 = ˝ 𝑖:𝑘𝑖 =𝑘𝑣𝑖.
The aggregation service aggregates the reports to generate a noisy
version of this aggregated value. It supports two modes: one with
key discovery and other without.
• Without key discovery, the ad-tech needs to provide a subset
𝐿⊆K of keys they are interested in, and they only get cor-
responding aggregated values 𝑤ℓ for ℓ ∈ 𝐿 after addition of
noise sampled from the discrete Laplace distribution, denoted as
DLap(𝑎), which is supported over all integers with probability
mass at𝑥 proportional to𝑒−𝑎|𝑥|.
Algorithm 1 AggregationService (with or without Key Discovery)
[Parts specific to the service without key discovery are in blue.]
[Parts specific to the service with key discovery are in green.]
Params: Contribution budget Λ1∈ Z>0,
privacy parameters𝜀∗∈ R≥0 and𝛿∗∈[ 0, 1],
State: Privacy budget trackers𝐵𝜀 :I→ R≥0 ,𝐵𝛿 :I→[ 0, 1].
Inputs: Privacy parameters𝜀 > 0 and𝛿∈[ 0, 1],
Aggregatable reports(𝑟1,𝑘 1,𝑣 1), . . . ,(𝑟𝑛,𝑘𝑛,𝑣𝑛),
Subset𝐿 ={ℓ1,...,ℓ 𝑚}⊆K of keys.
Output: Summary report(ℓ1,𝑤 1), . . . ,(ℓ𝑚,𝑤𝑚).
if∃𝑖∈[ 𝑛] such that𝐵𝜀(𝑟𝑖)+ 𝜀 >𝜀∗ or𝐵𝛿(𝑟𝑖)+ 𝛿 >𝛿∗ then
Abort [Privacy budget violated for some report.]
else
𝐵𝜀(𝑟𝑖)← 𝐵𝜀(𝑟𝑖)+ 𝜀 for all𝑖∈[ 𝑛]
𝐵𝛿(𝑟𝑖)← 𝐵𝛿(𝑟𝑖)+ 𝛿 for all𝑖∈[ 𝑛]
Let𝐿⊆𝐾 be the set of distinct keys among𝑘1, . . . ,𝑘𝑛
𝜏← Λ1·(1+ log(Λ0/𝛿)/𝜀)
forℓ∈𝐿 do
𝑤ℓ←𝑧ℓ+ ˝ 𝑗 :𝑘 𝑗 =ℓ𝑣𝑗 for 𝑧ℓ∼ DLap𝜏(𝜀/Λ1)
return {(ℓ,𝑤ℓ) :ℓ∈𝐿 and𝑤ℓ >𝜏}
• With key discovery, the aggregation service adds noise to each
𝑤𝑘 sampled from the truncated discrete Laplace distribution,
DLap𝜏(𝑎), supported over integers in[−𝜏,𝜏] with probability
mass at𝑥 proportional to𝑒−𝑎|𝑥|. But the noisy values are released
only for keys𝑘 where these noisy values are greater than𝜏. The
subset𝐿 of keys is thus “discovered” from the reports themselves.
In addition, the aggregation service uses a privacy budget service to
enforce that the privacy budget is respected for each aggregatable
report.2 This entails maintaining 𝐵𝜀 :I→ R≥0 that tracks, for
each report, the sum of 𝜀 values with which the said report has
participated in aggregation requests; the privacy budget service
enforces that this sum never exceeds a fixed value𝜀∗3 Additionally, if
using the key discovery mode, an additional state of𝐵𝛿 :I→[ 0, 1]
is maintained that tracks the number of times a report participated
in an aggregation request; and it is enforced that this never exceeds
a fixed valueℓ∗4 For simplicity we present the aggregation service
(with or without key discovery) and the privacy budget service
together in Algorithm 1. All pseudocode we provide in this paper
are for explaining the underlying functionality, and not meant to
reflect actual implementation of these APIs.
Remark 2.1. We note that the currently supported implementation
of the aggregation service is weaker than our description in that the key
discovery mode is not supported and ℓ∗ = 1 is enforced for all reports
(that is, each report can participate in at most one aggregation request).
However, our results hold even under these proposed extensions of key
discovery [2] and requerying [50].
2In this paper we assume that the aggregation service is tracking budget “per report”,
but in reality it uses a coarse id called shared report id that consists of the API version,
the website that generated the report, and the reporting time in seconds [34] to track
a single budget for all reports assigned to the shared report id.
3Currently this value is equal to 64 [39].
4Currently this value is equal to 1 for both ARA and and PAA; this corresponds to no
“re-querying” [50].
384

On the Differential Privacy and Interactivity of Privacy Sandbox Reports Proceedings on Privacy Enhancing Technologies 2025(3)
Next, we describe the clients for ARA and PAA that generate
aggregatable reports based on cross-site information and send them
to the ad-tech.
2.1.2 ARA Client. We explain the workings ofARA-SR-Client (the
client that supports ARA summary reports in the browser) in con-
text of an example visualized in Figure 1. Suppose a publisher’s page
(some-blog.com) displays ads as part of a “Thanksgiving” campaign
about sneakers, sandals, and flip-flops that can be purchased on an
advertiser’s page (shoes-website.com). The ad-tech would like to
measure the amount of money spent on shoes on the advertiser’s
page that could be attributed to these ads, and in particular, with
an attribution rule that “the purchase must happen within three
days after an ad was shown”.
To use ARA-SR-Client, the ad-tech annotates both the publisher
and advertiser pages with additional JavaScript or HTML that
points to a URL with a specific HTTP header (see [29] for details).
ARA-SR-Client can get invoked in two ways, either when the ad is
shown on the publisher’s page, or when a conversion happens on
the advertiser’s page as described below.
• On the publisher page, the ad-tech registers a so-called “attribu-
tion source” with the ARA-SR-Client in the browser (e.g., corre-
sponding to a view/click ad event). In our example the source
corresponds to an ad shown onsome-blog.com. This entails spec-
ifying a tuple(srcId,dest,expDate,srcFilt,srcKey), where
⊲ srcId is an identifier associated to the source event (in our
example it is a random id generated when an ad is shown on
some-blog.com),
⊲ dest is the advertiser domain where the conversion could
happen (shoes-website.com in our example),
⊲ expDate is an expiration date for attributing conversions to
the source (three days in our example),
⊲ srcFilt is a set of filter keys, each being a bounded bit string,
(treated as strings “sneakers”, “sandals”, and “flip-flops” in our
example for simplicity),
⊲ srcKey∈K is a key associated with the source (in our example
we take it to be the string “Thanksgiving:” for illustration).
Each source registration invokes the “Source registration” part
of Algorithm 2, which updates a setS of registered sources.
• On the advertiser page, the ad-tech registers a so-called “trigger”
corresponding to a qualifying user activity (such as a purchase
on shoes-website.com in our example) by specifying a tuple
(trigId,trigFilt,trigKey,trigValue), where
⊲ trigId is an identifier associated with the trigger (in our exam-
ple it is a random id generated when the purchase happened
on shoes-website.com),
⊲ trigFilt is a set of filter keys similar tosrcFilt (in our exam-
ple it could be either “sneakers”, or “sandals”, or “flip-flops”),
⊲ trigKey∈K is a key associated to the trigger (in our example
we take it to be the string “shoes-value” for illustration).
⊲ trigValue∈{ 0, 1,..., Λ1} is a value associated to the trigger
(in our example it is the price of the shoes purchased).
Each trigger registration invokes the “Trigger registration” part
of Algorithm 2.
At any point of time, ARA-SR-Client uses𝐿1 :S→ Z≥0 to track
the sum of all values contributed, and𝐿0 :S→ Z≥0 to denote the
number of non-zero values contributed per registered source, with
𝐿0(𝑠) and𝐿1(𝑠) initialized to 0 at the time of registration of source
𝑠∈S .
When a user visits the advertiser’s page and a trigger is reg-
istered, ARA-SR-Client (Algorithm 2) matches the trigger to the
most recently registered active source (namely, those withexpDate
ahead of the current time) and generates an aggregatable report;
aggregatable reports for ARA containtrigId as part of its metadata
(earlier referred to as𝑚 in(𝑟,𝑘,𝑣,𝑚 )). If no source is matched, a
null report, denoted(𝑟,⊥,⊥) in Algorithm 2 is sent. Such reports
are ignored by the aggregation service (Algorithm 1).
Remark 2.2. In reality the metadata 𝑚 and the time the report is
sent can allow the ad-tech to associate the received report with the
particular device. Moreover, if the trigger does not get attributed to
any source, and trigId is not set, the corresponding null report is not
sent (see [35]). This could potentially allow the ad-tech to know if a
trigger was attributed to a source or not. These are handled by the
ARA client in practice with some heuristics such as sending reports
without a trigger id with some delay, as well as sending some fake
null reports with small probability. However, these heuristics would
not allow us to prove a formal DP guarantee, so we do not consider
this case.
Remark 2.3. ARA-SR-Client (Algorithm 2) is using the so-called
“last-touch” attribution, namely, that in presence of several potentially
matching sources, the most recently registered one is chosen. While
we choose to only consider last-touch attribution for simplicity, our
results hold for any attribution method (as long as any trigger is
fully attributed to only one source). Indeed, ARA uses a more involved
attribution strategy where impressions can be assigned priority (at
source registration) and the trigger is attributed to the last source with
the highest priority.
Here is how our example would play out, as visualized in Fig-
ure 1. A publisher’s page (some-blog.com) displays an ad, on Nov
18th about shoes that can be purchased on an advertiser’s page
(shoes-website.com). When an ad is displayed at some-blog.com
the source gets registered with a random srcId, with dest equal
to “shoes-website.com”, an expiry date of Nov 21st, that is three
days into the future from the time the ad was shown, a set of
srcFilt = {“sneakers”, “sandals”, “flip-flops”} that restricts
which purchases can be attributed to this source and, a source key
srcKey = “Thanksgiving:” to tie this ad to a certain campaign.
When the user subsequently purchases a sneaker from the ad-
vertiser’s page, the advertiser can choose to register a trigger with
a random trigId, a set of trigFilt = {“sneakers”} that restricts
the potential sources that this conversion can be attributed to, a
trigger key trigKey = “shoes-value” to record the interpretation
of the value, and finally trigValue = 70, which is the price of the
sneaker.
The ARA-SR-Client (Algorithm 2) then attributes the trigger to
the source and generates an aggregatable report(𝑟,𝑘,𝑣) with the
key being𝑘 = “Thanksgiving:shoes-value” (where for ease of
illustration we use string concatenation instead of bitwise-OR),
value𝑣 = 70, and𝑟 being a random id.
Recall that the ad-tech knows details of the ad impression that
was displayed on the publisher website, as well as details of the
conversion that happened on the advertiser’s website; these are
385

Proceedings on Privacy Enhancing Technologies 2025(3) Ghazi et al.
Trigger
registration
Publisher Page ( )
ARA-SR-Client
(Browser)
Ad
Advertiser Page ( )
Aggregatable Report
StoreBlog
Ad seen on Nov 18, 2024 Purchase made on Nov 20, 2024
(before  = Nov 21, 2024)
Attribution Source
Trigger
Source
registration
Buy
Figure 1: Illustrative example of an aggregatable report generated by ARA-SR-Client.
Algorithm 2 ARA-SR-Client
Params: Contribution and sparsity budgets Λ1, Λ0∈ Z>0.
State:
• Set of registered sourcesS,
• Sparsity Budget Tracker𝐿0 :S→ Z≥0,
• Contribution Budget Tracker𝐿1 :S→ Z≥0.
Source registration:
On input𝑠 =(srcId,dest,expDate,srcFilt,srcKey)
S←S∪{ 𝑠} [Add𝑠 to set of registered sources.]
𝐿0(𝑠) = 0 and𝐿1(𝑠) = 0
Trigger registration:
On input(dest,trigId,trigFilt,trigKey,trigValue).
𝑟← a random report id inI
if trigValue > 0 then
for active𝑠∈S (in reverse chronological order) do
if dest =𝑠.dest and trigFilt∩𝑠.srcFilt ≠∅ then
if𝐿0(𝑠)+ 1≤ Λ0 and𝐿1(𝑠)+ trigValue≤ Λ1 then
𝑣← trigValue
𝑘← bit-wise OR of srcKey and trigKey
𝐿0(𝑠)← 𝐿0(𝑠)+ 1
𝐿1(𝑠)← 𝐿1(𝑠)+ trigValue
Send report(𝒓, 𝒌, 𝒗) and halt
Send null report(𝒓,⊥,⊥)
referred to as “first-party” information. However, without third-
party cookies, the ad-tech cannot link the two events as happening
on the same browser and thus cannot attribute the conversion to
the impression. The ARA helps ad-techs access this “third-party”
information linking the conversion to the impression. But it does so
in a privacy-preserving manner by enforcing that the total number
of generated reports associated to any source is at most Λ0, and
that the total value of such generated reports is at most Λ1. We
provide the formal privacy guarantees implied by these properties
of ARA summary reports as Theorem 4.4 in Section 4.
2.1.3 PAA Client & Shared Storage. The PAA client is typically
used in tandem with the Shared Storage API [36]. Shared Storage
is a key-value database stored on the browser that can be accessed
by the code using PAA across any websites visited on a browser,
which the ad-tech can annotate with their code.
Recall that ARA-SR-Client tracks the contribution and sparsity
budgets for each “source”. However, unlike ARA, the PAA does
not have a concept of registering a source. PAA instead enforces
contribution and sparsity budgets separately for each ad-tech and
each “time-window”. Formally, letU denote the set of all devices,
and letT denote the partition of all time into contiguous time
windows, each of a fixed length.5 We use Ξ to denote the shared
storage, where Ξ𝑢 denotes the part of storage accessible to the
device𝑢∈U . At any point of time, PAA-SR-Client uses𝐿1 :U×
T→ Z≥0 to track the sum of all values contributed and𝐿0 :U×
T→ Z≥0 to track the number of non-zero values contributed per
(𝑢,𝑡), with𝐿0(𝑢,𝑡) and𝐿1(𝑢,𝑡) initialized to 0 at the start of time
window𝑡 for any𝑢∈U .
We explain the working onPAA-SR-Clientin context of an exam-
ple visualized in Figure 2. Assume an ad-tech has four ad campaigns
(for shoes, pants, jackets, and shirts) running in parallel and they
want to estimate the reach of each campaign (the number of people
exposed to the ads from campaigns) across different publisher web-
sites. Suppose the ad-tech expects that most of the people would
only see at most two ads within a single time window𝑡∈T .
To use the PAA and Shared Storage APIs, the ad-tech annotates
any webpage it has access to with a JavaScript that can read and
write to Shared Storage and can register an adevent; the registration
requires providing a method𝜋 that maps the current state of the
shared storage, to the next state of the storage, a key𝑘∈K , and a
corresponding value𝑣∈{ 0, 1,..., Λ1} (in our example the key is
the campaign name and the value is Λ1/2 if the ad from that cam-
paign was seen for the first time and 0 otherwise; this is looked up
from shared storage). When an event is registered, PAA-SR-Client
(Algorithm 3) checks that the new addition would not violate the
contribution and sparsity budget for the ad-tech at the current time
5Each time window is 10 minutes long in the current implementation of PAA [24].
386

On the Differential Privacy and Interactivity of Privacy Sandbox Reports Proceedings on Privacy Enhancing Technologies 2025(3)
Λ Λ Λ
No report sent
(since the contribution
budget is exhausted)
Time
PAA-SR-Client
(Browser)
 Ad For PantsAd For Shoes Ad For Jacket Ad For Shirt
Shared
Storage
Aggregatable
Reports:
New time window startsNew time window starts
Ad For Shoes
⊥
= Event registration
Figure 2: Illustrative example of an aggregatable report generated by PAA-SR-Client.
Algorithm 3 PAA-SR-Client
Params: Contribution and sparsity budgets Λ1, Λ0∈ Z>0.
State:
• Shared storage Ξ∈ 𝔛U (we use 𝔛 to denote the set of possible
states of the shared storage, one for each device𝑢∈U ),
• Sparsity Budget Tracker𝐿0 :U×T→ Z≥0,
• Contribution Budget Tracker𝐿1 :U×T→ Z≥0.
Event Registration
On following inputs:
• The device𝑢 registering the event,
• Time window𝑡 when event is invoked, and
• Function𝜋 : 𝔛→ 𝔛×K×{ 0, 1,..., Λ1} that on input being
the current state of shared storage Ξ, returns its next state in
addition to a key value pair(𝑘,𝑣).
Ξ𝑢,𝑘,𝑣 ←𝜋(Ξ𝑢) [Note: Ad-tech does not learn what is inside Ξ𝑎.
Moreover, even the returned(𝑘,𝑣) is not visible to ad-tech.]
𝑟← a random report id inI
if𝑣 > 0 then
if𝐿0(𝑎,𝑡)+ 1≤ Λ0 and𝐿1(𝑎,𝑡)+ 𝑣≤ Λ1 then
𝐿0(𝑢,𝑡)← 𝐿0(𝑢,𝑡)+ 1
𝐿1(𝑢,𝑡)← 𝐿1(𝑢,𝑡)+ 𝑣
Send aggregatable report(𝒓, 𝒌, 𝒗) and halt
Send null report(𝒓,⊥,⊥)
window, and if that is indeed the case, it generates an aggregatable
report(𝑟,𝑘,𝑣) for a random ID𝑟∈I .
To run through our example, the user sees first the ads for shoes
and pants and the reports are sent; next the user sees an ad for a
jacket, but the contribution budget is exhausted so no report is sent.
Finally, in the next time window, the user sees an ad for a shirt and
the report is sent since the budget is refreshed. However, when the
user sees an ad for shoes again, a null report is sent because the
contribution is 0, since shared storage indicates that a shoes ad was
seen previously.
Similar to case of ARA, recall that the ad-tech knows details of
any specific event in PAA, which is considered “first-party” informa-
tion. However, without third-party cookies, the ad-tech cannot link
information across events happening on the same browser across
different websites; this would be “third-party” information. The
PAA helps ad-techs access this “third-party” information via the
use of the Shared Storage API. But it does so in a privacy-preserving
manner by enforcing that the total number of generated reports for
any ad-tech in any time window is at most Λ0, and that the total
value of such generated reports is at most Λ1. The access to Shared
Storage is also “sandboxed” in a manner that the information within
can only be used for purposes of generating the aggregatable re-
port. We provide the formal privacy guarantees implied by these
properties of PAA summary reports as Theorem 4.6 in Section 4.
2.2 Event-level Reports
In addition to summary reports, ARA also supports event-level
reports [33]. Before describing the event-level reports formally,
we consider an example visualized in Figure 3. Again, suppose a
publisher’s webpage (some-blog.com) displays an ad for footwear
sold on an advertiser’s site (shoes-website.com).
To use ARA-Event-Client, the ad-tech annotates both the pub-
lisher and advertiser pages in a manner that is similar to case of sum-
mary reports (see Section 2.1.2). ARA-Event-Client can get invoked
in three ways, (i) when the ad is shown on publisher’s page, (ii)
when a conversion happens on the advertiser’s page, and (iii) on the
passing of a “reporting window”, as explained below (this happens
automatically without any action from the ad-tech). For simplicity,
we first describe the “noiseless” version of ARA-Event-Client in
Algorithm 4.
• On the publisher page, the ad-tech registers an attribution source
with ARA-Event-Client in the browser. This entails specifying a
tuple(srcId,dest,expDate,srcFilt,maxRep,trigSpec), where
⊲ srcId, dest, expDate, srcFilt are the same as in the case of
the ARA summary reports,
⊲ maxRep is the maximum number of event-level reports that
can be attributed to this source (in our example it is 3),
⊲ trigSpec,6 short for “trigger specificiation”, is a list of at most
32 elements (in our case we have two specifications, one for
“sneakers” and one for “sandals”) each consisting of
6In real implementation a list of possible values of trigger data is passed separately
and there is a default specification, but we ignore this here for simplicity.
387

Proceedings on Privacy Enhancing Technologies 2025(3) Ghazi et al.
No report sent for
trigData: “sandals”
(since total trigger value for “sandals” < $10)
srcId: 94298
dest: “shoes-website.com”
srcFilt: { “shoes” }
maxReports: 3
trigSpec: [
  (“sneakers”, [2d, 7d], [$20, $70]),
  (“sandals”,  [1d, 5d], [$10, $50]),
]
Publisher Page (some-blog.com)
ARA-Event-Client
(Browser)
Ad
Blog
Attribution Source
srcId: 94298
trigData: “sneakers”
summaryBucket: $20-$69
$30 $65 $10 $20$60
srcId: 94298
trigData: “sandals”
summaryBucket: ≥ $50
1d 2d 5d 7d
srcId: 94298
trigData: “sandals”
summaryBucket: $10-$49
No report sent for
trigData: “sneakers”
(since maxRep limit is reached)
Time since
source registration
→ source registration
→ trigger registration
→ passing of reporting window
Notation
Figure 3: Illustrative example of event-level reports generated by ARA-Event-Client.
□ trigData∈ TD, where TD is the set of possible values that
trigData can take; while this is restricted to be a 5-bit inte-
ger, we treattrigData as a string in our example for ease
of visualization.
□ at most five reporting windows that specify when the new
reports should be sent; each reporting window is time (in
seconds) from the source registration time.
□ summary buckets, an increasing list of integer thresholds
such that a report is sent when the threshold is met (subject
to maxRep limit).
Each source registration invokes the “Source registration” part
of Algorithm 4; visualized by the red dot in Figure 3. This adds
the source to the list of active registered sourcesS and initializes
the current values and last reported bucket values to zero.
• On the advertiser page , the ad-tech registers a trigger corre-
sponding to a qualifying user activity (such as a purchase on
shoes-website.com in our example) by specifying a tuple con-
taining(dest,trigId,trigFilt,trigData,trigValue), where
⊲ dest, trigId, trigFilt are the same as in the case of ARA
summary reports,
⊲ trigData is data associated with the trigger, which must match
one fromtrigSpec (if it does not match any in the specification
it gets ignored), and
⊲ trigValue is an integer value associated with the trigger (in
our example the amount spent on the shoes).
Each trigger registration invokes the “Trigger registration” part
of Algorithm 4; visualized by the cyan diamond in Figure 3. Here
ARA-Event-Client searches for an active source that this trigger
could be attributed to, and upon finding one, adds the value of
the current trigger to the value associated to the source for this
trigData.
Finally, for each registered source𝑠, whenever the amount of time
passed equals the reporting window for anytrigData in𝑠.trigSpec,
a report is sent to the ad-tech using Algorithm 4; in our example,
1 day after the source is registered, the first reporting window for
trigData = “sandals” is passed and ARA-Event-Client get invoked.
All such invocations associated to passing of reporting windows is
visualized as a green pentagon in Figure 3.
Algorithm 4 ARA-Event-Client (Noiseless version).
State:
• Sequence of active registered sourcesS,
• Current value𝑉 :S× TD→ Z≥0,
• Last reported bucket𝑈 :S× TD→ Z≥0,
• Number of reports sent𝑁 :S→ Z≥0.
Source registration:
On input𝑠 =(srcId,dest,expDate,srcFilt,maxRep,trigSpec)
S←S∪{ 𝑠} [Add𝑠 to set of active sources.]
𝑁(𝑠)← 0
for trigData∈ TD do
𝑉(𝑠,trigData)← 0 and𝑈(𝑠,trigData)← 0
Trigger registration:
On input(dest,trigId,trigFilt,trigData,trigValue)
if trigValue > 0 then
for𝑠∈S (in reverse chronological order) do
if dest =𝑠.dest and trigFilt∩𝑠.srcFilt ≠∅ then
if trigData listed in𝑠.trigSpec then
𝑉(𝑠,trigData)← 𝑉(𝑠,trigData)+ trigValue
[Add to value associated to this source and trigData.]
break
At passing of time window for (𝒔, trigData)∈S× TD:
Let𝑏1,...,𝑏 𝑘∈ Z>0 be the list of associated summary buckets
to trigData in trigSpec of source𝑠, in increasing order.
for𝑖 = 1,...,𝑘 do
if𝑈(𝑠,trigData) <𝑏𝑖≤𝑉(𝑠,trigData) then
𝑈(𝑠,trigData) =𝑏𝑖
if𝑁(𝑠) <𝑠.maxRep then
𝑁(𝑠)← 𝑁(𝑠)+ 1
Send report(𝒔.srcId, trigData, 𝒃𝒊) to ad-tech
We now walk through the behavior of ARA-Event-Client in the
example visualized in Figure 3; we present the “noiseless” behavior
of the algorithm before describing the noisy version.
• Day 0: An ad is shown on publisher’s page and the source𝑠 gets
registered.
388

On the Differential Privacy and Interactivity of Privacy Sandbox Reports Proceedings on Privacy Enhancing Technologies 2025(3)
• Day 1: The user buys $30 sneakers from advertiser’s page. This
is attributed to source𝑠 and𝑉(𝑠,sneakers) is set to 30.
At the end of day 1, the reporting window for sandals is passed,
but no report is generated because𝑉(𝑠,sandals) is still 0.
• Day 2: The user buys $60 sandals. This is attributed to source𝑠,
and𝑉(𝑠,sandals) is set to 60.
At the end of day 2, the reporting window forsneakers is passed,
and a report is generated indicating a bucket value of $20-$69.
At this point𝑈(𝑠,sneakers) is 20.
• Day 4: The user buys $65 sneakers. This is attributed to source
𝑠 and𝑉(𝑠,sneakers) gets incremented to become 95.
• Day 5: At the end of day 5, the second reporting window for
sandals is passed, and two reports are generated for sandals as
𝑉(𝑠,sandals) = 60, which exceeds both summary bucket values
of $10 and $50.
• Day 6: The user buys $10 sneakers. This is attributed to source
𝑠 and𝑉(𝑠,sneakers) is incremented to become 105.
• Day 7: At the end of day 7, the second reporting window for
sneakers is passed, but no reports are sent, as the maximum
number of reports 3 for this source has been reached. Further-
more, the source now gets marked as inactive and no further
purchases get attributed to this source.
Noisy Version of ARA-Event-Client. Note that for each source,
the setO of possible combinations of reports that could be sent is
finite. In our example, reports are sent for “sandals” only at the
end of Day 1 and Day 5. The number of reports sent on each of
the two days is one among the 6 possible options shown in Table 1.
Day 1 Day 5
0 0
0 1
0 2
1 0
1 1
2 0
Table 1: Possible
number of reports
sent on Day 1 and
Day 5 for “sandals”.
Similarly, the number of reports sent
at the end of Day 2 and Day 7 is
also among 6 possible options. While
these lead to 36 possible configura-
tions of reports sent, 9 of them corre-
spond to sending of 4 reports, which
is larger than the maximum limit of
3 reports that could be sent. Thus, in
total, there are27 possible valid config-
urations of reports that could get sent.
The private version of event-level re-
ports works as follows: with probabil-
ity 𝑒𝜀−1 𝑒𝜀+|O|− 1 we proceed like in the noiseless version in Algorithm 4,
otherwise we sample an element ofO uniformly at random, and
generate responses accordingly. This choice can be made at the time
of source registration, even before any triggers are observed. We
provide the formal privacy guarantees implied by these properties
of ARA event-level reports as Theorem 5.1 in Section 5.
3 Differential Privacy
We use the notion of differential privacy (DP), which typically con-
siders mechanismsM :D→ Δ(R) that map input datasets𝐷∈D
to probability distributions over a setR of responses. Central to the
notion of DP, is the definition of “adjacency” of databases. Loosely
speaking two databases𝐷,𝐷′∈D are said to be adjacent if they
“differ in one record”. We defer the definition of a database and the
notion of adjacencies relevant for the analysis in each application to
Section 4. But for any notion of database and adjacency, differential
privacy (DP) quantifies the ability (or lack thereof) of an adversary
to distinguish two “adjacent” datasets 𝐷 and𝐷′ by observing a
sample fromM(𝐷) orM(𝐷′).
Definition 3.1 ((𝜀,𝛿)-Indistinguishability). Two distributions𝑃,
𝑄 are said to be(𝜀,𝛿)-indistinguishable, denoted𝑃≈𝜀,𝛿 𝑄 if for all
events𝑊 , it holds that
𝑃(𝑊)≤ 𝑒𝜀𝑄(𝑊)+ 𝛿 and 𝑄(𝑊)≤ 𝑒𝜀𝑃(𝑊)+ 𝛿.
Definition 3.2 (Differential Privacy). [15, 16] A mechanismM :
D→ Δ(R) satisfies(𝜀,𝛿)-DP if for all adjacent datasets𝐷,𝐷′∈D ,
it holds thatM(𝐷)≈ 𝜀,𝛿M(𝐷′). The special case of (𝜀, 0)-DP is
denoted as𝜀-DP for short.
We will often refer to parameter𝜀 or both𝜀 and𝛿 in the definition
of(𝜀,𝛿)-DP as the privacy budget.
However, as we discuss shortly, modeling the setting of ARA
and PAA as mechanisms operating on a “static” database does not
capture the interactive nature of these systems. Hence we consider
a stronger notion of “interactive mechanisms” and “interactive
adversaries” defined in Section 3.1.
Since the aggregation service adds noise from the (truncated)
discrete Laplace distribution, we rely on the following fact to prove
DP properties of summary reports (for both ARA and PAA). For
any integer𝑑∈ Z>0, let DLap𝜏(𝑎)⊗𝑑 be the distribution over Z𝑑
where each coordinate is drawn independently from DLap𝜏(𝑎).
Fact 3.3 ([ 20]). For all 𝜀 > 0 and integer Δ > 0, and vectors
𝑢,𝑣 ∈ Z𝑑 such that∥𝑢−𝑣∥1 = Δ, the distributions𝑃 and𝑄 drawn as
𝑢+𝜉 and𝑣+𝜉 for𝜉∼ DLap(𝜀/Δ)⊗𝑑 satisfy𝑃≈𝜀,0𝑄.
Furthermore, if𝑢−𝑣 has at most𝑠 non-zero coordinates, then for
all𝛿 > 0 and𝜏≥ Δ·( 1+ log(𝑠/𝛿)/𝜀), the distributions 𝑃 and𝑄
drawn as𝑢+𝜉 and𝑣+𝜉 for𝜉∼ DLap𝜏(𝜀/Δ)⊗𝑑 satisfy𝑃≈𝜀,𝛿 𝑄.
While the privacy guarantee of the discrete Laplace mechanism
was studied in [20], we include a proof for the case of truncated
discrete Laplace noise in Section A for completeness.
3.1 Interactive Mechanisms
As noted earlier, DP is typically defined for “one-shot” mechanisms
that map databases to probability distributions over a response set.
However, there are two key reasons why the generation process of
ARA/PAA summary reports is not a “one-shot” mechanism:
(1) There is adaptivity in the choice of contribution values, which
can be changed based on previously observed summary reports.
For example, in context of ARA, the ad-tech can change the
scale and interpretation of trigValue when making contribu-
tions based on previously observed summary reports.
(2) The ad-tech can have some influence on the new events that get
added to the database themselves. For example, in the context
of ARA, the advertiser might decide based on summary reports
obtained on day 1 to change the product price on day 2, which
could influence the number of subsequent conversions.
To argue the DP properties of summary and event-level reports,
it is helpful to model their generation process as an interaction
between a mechanism and an adversary defined below. Abstractly
speaking, letD denote the set of all “databases”, and letQ andR
denote a set of “queries” and “responses” as used below.
389

Proceedings on Privacy Enhancing Technologies 2025(3) Ghazi et al.
Algorithm 5 Interactive Transcript IT(M :A).
Inputs: ⊲ Interactive mechanismM with initial state𝑆0,
⊲ Interactive adversaryA
Π←() and𝑡← 1 [Empty transcript.]
whileA( Π) ≠
 do
(𝐷𝑡,𝑞𝑡)←A( Π) [Adversary creates database & query.]
(𝑆𝑡,𝑟𝑡)∼M( 𝑆𝑡−1,𝐷𝑡,𝑞𝑡) [Mechanism samples response.]
Π← Π◦𝑟𝑡 and𝑡←𝑡+ 1
return Π
Definition 3.4 (Interactive Mechanism). An interactive mechanism
with state setS is represented by an initial state 𝑆0 ∈S and a
functionM :S×D×Q→S× Δ(R) , that maps the current state
𝑆∈S , a database𝐷∈D and a query𝑞∈Q to the next state𝑆′∈S
and a distribution over responses𝑟∈R .
We will often abuse notation to denote the output ofM(𝑆,𝐷,𝑞)
as(𝑆′,𝑟) where𝑆′ is the next state and𝑟 is drawn from the distri-
bution overR returned byM(𝑆,𝐷,𝑞).
Definition 3.5 (Interactive Adversary). An interactive adversary
A :R∗→(D×Q)∪{
 } maps the history of responses(𝑟1,𝑟 2,... )∈
R∗, to the next database𝐷∈D and query𝑞∈Q , or “halt” (
 ).
The interaction betweenM with initial state 𝑆0∈S , and an
interactive adversaryA is described in Algorithm 5 and results in
the probability distribution IT(M :A) of transcripts Π, which is a
sequence of responses(𝑟1,𝑟 2,... )∈R ∗.
In order to define what it means for an interactive mechanism to
satisfy DP, we need to define the notion of “adjacency” for databases.
For now, let us abstractly say that database is a set of records(𝑥,𝑦)∈
X×Y . The setX is assumed to be known to the adversary and we
will refer to𝑥∈X as a “privacy unit”. LetY be an arbitrary set
for the sake of our notation here; we instantiate it appropriately as
relevant later. For any database𝐷, let𝐷−𝑥 denote the database that
loosely speaking “removes records in𝐷 corresponding to𝑥∈X or
replaces them with a certain generic one”. We leave this notion to be
abstract for now, and we instantiate the specific notion of adjacency
when describing the formal guarantees of ARA and PAA. For any
interactive mechanismM and any 𝑥 ∈X , letM−𝑥 denote the
mechanism that replaces the dataset𝐷𝑡 by𝐷−𝑥 𝑡 at each step: that is,
(𝑆𝑡,𝑟𝑡)∼M( 𝑆𝑡−1,𝐷𝑡,𝑞𝑡) is replaced by(𝑆𝑡,𝑟𝑡)∼M( 𝑆𝑡−1,𝐷−𝑥 𝑡 ,𝑞𝑡)
in Algorithm 5. We define DP for interactive mechanisms as follows.
Definition 3.6 (DP for Interactive Mechanisms). An interactive
mechanismM satisfies(𝜀,𝛿)-DP if for all interactive adversaries
A and all𝑥∈X , it holds that IT(M :A)≈𝜀,𝛿 IT(M−𝑥 :A).
Remark 3.7. A single round version of our definition coincides
with the standard definition of DP for the adjacency notion where 𝐷
and𝐷−𝑥 are adjacent. For multiple rounds, our definition is strictly
stronger than the standard definition of DP for interactive mechanisms,
where the adversary always returns the same database at each step;
we refer to such adversaries as “stable”.
4 Analysis of Summary Reports
4.1 DP guarantees from IDP
For any interactive mechanismM and a sequence of databases
and queries((𝐷1,𝑞 1),(𝐷2,𝑞 2),... ), letF𝑡(·) denote the distribution
over response 𝑟𝑡 as returned by M(𝑆𝑡−1,·,𝑞𝑡); note that the se-
quence(𝑆0,𝑆 1,...,𝑆 𝑡−1) of mechanism states is deterministic given
the sequence of databases and queries. We say that the sequence
((𝜀1,𝛿 1),(𝜀2,𝛿 2),... ) is a privacy rollout of the mechanismM for
𝑥 ∈ Xon the sequence ((𝐷1,𝑞 1),(𝐷2,𝑞 2),... ), ifF𝑡(𝐷𝑡) ≈𝜀𝑡,𝛿𝑡
F𝑡(𝐷−𝑥 𝑡 ) holds for all𝑡.
Definition 4.1 (Individual DP). An interactive mechanism M
satisfies(𝜀∗,𝛿∗)-IDP if for all 𝑥 ∈X and all sequences((𝐷1,𝑞 1),
(𝐷2,𝑞 2),...) of databases and queries, if((𝜀1,𝛿 1),(𝜀2,𝛿 2),... ) is a
privacy rollout ofM for𝑥 on the said input sequence, then˝ 𝑡𝜀𝑡≤
𝜀∗ and ˝ 𝑡𝛿𝑡≤𝛿∗.
Our main technical result is that IDP implies DP. This can be viewed
as the approximate-DP variant of [19, Theorem 4.5], which proves
a qualitatively similar statement for Rényi DP although our result
is for the more general case of interactive adversaries, wherein
even the database can change based on previous responses. We
note however that our proof technique is quite general, and can be
applied in the Rényi DP setting to extend the result of [19] to the
case of interactive adversaries as well.
Theorem 4.2. If an interactive mechanism satisfies(𝜀∗,𝛿∗)-IDP,
then it satisfies(𝜀∗,𝛿∗)-DP.
To prove the above, we apply the tool of DP filters [25] in the
setting of IDP [17, 19].
We defer the full proof to Section 4.4, and first describe how this
implies the DP guarantees of the ARA and PAA summary reports by
appropriately instantiating the notion of a database and adjacency
as well as the notion of queries and responses and showing that the
interactive mechanism that generates the corresponding summary
reports satisfies an IDP guarantee and hence by the above result,
also satisfies a DP guarantee.
4.2 Privacy of ARA Summary Reports
To prove the DP properties of ARA, we formalize an end-to-end
mechanismMSR (Algorithm 6) that simulates the joint behavior
of ARA-SR-Client (Algorithm 2) and the aggregation service (Algo-
rithm 1) ultimately generating the summary reports.
Databases and Adjacency. We model a database 𝐷∈D ARA as
consisting of records(𝑥,𝑦)∈X ⊥×Y whereX⊥ =X∪{ 𝑥⊥} is
the setX of all possible “sources” registered across all devices in
addition to a “dummy source” that we denote as𝑥⊥ andY is the
set of all possible “triggers” registered across all devices; note that
triggers are in one-to-one correspondence with the report ID 𝑟
part of the generated aggregatable report (𝑟,𝑘,𝑣), and thus for
simplicitly, we interchangeably use𝑦∈Y to denote the report ID.
For any database𝐷∈D and𝑥∈X , let𝐷−𝑥 be the dataset obtained
by moving all aggregatable reports associated to 𝑥 to instead be
associated with𝑥⊥, that is, replace(𝑥,𝑦) by(𝑥⊥,𝑦). We note that
adjacent databases in our notion have the same set of𝑥’s and𝑦’s,
and thus, DP is not protecting against knowledge of these, but only
the knowledge of which𝑦’s are attributed to which𝑥’s.
390

On the Differential Privacy and Interactivity of Privacy Sandbox Reports Proceedings on Privacy Enhancing Technologies 2025(3)
Queries, Responses and Mechanism States. The query setQ for
MSR consists of tuples𝑞 =(𝜀,𝛿,𝑌,𝑓 ) where(𝜀,𝛿)∈ R≥0×[ 0, 1]
are privacy parameters for the query,𝑌⊆Y is a subset of triggers
whose corresponding reports need to be aggregated and 𝑓 :X×
Y→K× N is a function mapping a pair of a source and a trigger
to the candidate (key, value) for the aggregatable report generated
by them. The response setR ofMSR is the set of summary reports,
namely(K× Z)∗. Finally, the state setS ofMSR is given by the tuple
({(𝐿𝑥,𝑠𝑥)}𝑥∈X,{(𝜀𝑦,𝛿𝑦)}𝑦∈Y,𝑅). Here,𝐿𝑥 (resp.,𝑠𝑥) is the sum of
all (resp., number of non-zero) contributions attributed to𝑥∈X ,
𝜖𝑦,𝛿𝑦 are privacy budgets consumed for each report (equivalently
trigger)𝑦∈Y , and𝑅 is the set of all aggregatable reports generated
so far.
RelatingMSR to ARA Client and Aggregation Service. ForMSR
to simulate the end-to-end generation of summary reports by ARA,
we instantiate the database 𝐷 at each step to be the set of new
impressions and trigger pairs registered since the last query to
MSR. In phase #1,MSR updates the set𝑅 in its state to have all the
aggregatable reports generated so far, applying the contribution
and sparsity bounding similar to ARA-SR-Client (Algorithm 2). In
phase #2,MSR tracks and enforces that the privacy budget used per
report specified in𝑌 is under limits. If not, it aborts. Else it updates
these privacy budgets per report and in phase #3, returns the noisy
summation per key (with or without key discovery as specified).
Phases #2 and #3 simulate the aggregation service (Algorithm 1).
Theorem 4.3. MSR satisfies(𝜀∗,𝛿∗)-IDP with respect to aforemen-
tioned set of databases and neighbouring relation for ARA.
Before proving Theorem 4.3, we note that putting this together
with Theorem 4.2, immediately implies the following corollary.
Corollary 4.4. MSR satisfies(𝜀∗,𝛿∗)-DP with respect to afore-
mentioned set of databases and neighbouring relation for ARA.
Proof of Theorem 4.3. Let(𝐷1,(𝜀1,𝛿 1,𝑌 1,𝑓 1)),..., be any se-
quence of databases and queries that is provided toMSR; assume
the state at step𝑡 is({(𝐿𝑡,𝑥,𝑠𝑡,𝑥)}𝑥∈X ,{(𝜀𝑡,𝑦,𝛿𝑡,𝑦)}𝑦∈Y,𝑅𝑡). We as-
sume without loss of generality that there is no round whereMSR
returns a response of abort. This is because whetherMSR outputs
abort or not is only a function of the𝑦 values in the database, and
is the same for𝐷 and𝐷−𝑥.
Consider any𝑥∈X . Denote by 𝑅𝑥,𝑡 ⊆ 𝑅𝑡 the set of all aggre-
gatable reports generated for𝑥. Let𝑌𝑥,𝑡 denote the set of all𝑦∈𝑌𝑡
such that(𝑦,𝑘𝑦,𝑣𝑦)∈ 𝑅𝑥,𝑡 for some(𝑘𝑦,𝑣𝑦) and let𝑌𝑥 := — 𝑡𝑌𝑥,𝑡 .
Note that ˝ 𝑦∈𝑌𝑥𝑣𝑦≤ Λ1 and|𝑌𝑥|≤ Λ0 for all𝑡.
Thus, from the privacy guarantee of the discrete Laplace mecha-
nism (Theorem 3.3) we have thatMSR(𝑆𝑡−1,𝐷𝑡,(𝜀𝑡,𝛿𝑡,𝑌𝑡,𝑞𝑡))≈ 𝜀𝑥,𝑡,𝛿𝑥,𝑡
MSR(𝑆𝑡−1,𝐷−𝑥 𝑡 ,(𝜀𝑡,𝛿𝑡,𝑌𝑡,𝑞𝑡)) where
𝜀𝑥,𝑡 := 𝜀𝑡 Λ1 · ∑︁ 𝑦∈𝑌𝑥,𝑡 𝑣𝑦 and 𝛿𝑥,𝑡 := 𝛿𝑡 Λ0 ·|𝑌𝑥,𝑡|,
and each step𝑡. Thus, we get thatMSR satisfies(𝜀∗,𝛿∗)-IDP, since
for any𝑥∈X , it holds that
∑︁
𝑡
𝜀𝑥,𝑡 =
∑︁
𝑡
'›
«
𝜀𝑡
Λ1
·
∑︁
𝑦∈𝑌𝑥,𝑡
𝑣𝑦 “ﬁ
‹
≤
∑︁
𝑦∈𝑌𝑥
𝑣𝑦
Λ1
·
∑︁
𝑡 :𝑌𝑥,𝑡∋𝑦
𝜀𝑡 ≤ 𝜀∗,
Algorithm 6 Interactive mechanismMSR :S×D×Q→S× Δ(R) .
Params: ⊲ Contribution budget Λ1, Sparsity budget Λ0,
⊲ Global privacy parameters(𝜀∗,𝛿∗).
State: ⊲{(𝐿𝑥,𝑠𝑥)}𝑥∈X ,{(𝜀𝑦,𝛿𝑦)}𝑦∈Y , and𝑅⊆Y×K× N.
Inputs: ⊲ Database𝐷∈D ARA,
⊲ Privacy parameters𝜀 > 0 and𝛿∈[ 0, 1],
⊲ The list of triggers𝑌⊆Y whose corresponding
reports are to be aggregated, and
⊲ The function𝑓 :X×Y→K× N
# 1. Contribution Bounding Per𝑥∈X (cf. ARA-SR-Client)
for(𝑥,𝑦)∈ 𝐷 do
(𝑘,𝑣)← 𝑓(𝑥,𝑦)
if𝐿𝑥+𝑣≤ Λ1 and𝑠𝑥+ 1≤ Λ0 then
𝐿𝑥←𝐿𝑥+𝑣
𝑠𝑥←𝑠𝑥+ 1
𝑅←𝑅∪{(𝑦,𝑘,𝑣)}
# 2. Budget Bounding Per𝑦∈Y (cf. Aggregation Service)
if∃𝑦∈Y such that𝜀𝑦+𝜀 >𝜀∗ or𝛿𝑦+𝛿 >𝛿∗ then
return (({(𝐿𝑥,𝑠𝑥)}𝑥∈X,{(𝜀𝑦,𝛿𝑦)}𝑦∈Y,𝑅 ), abort)
else
𝜀𝑦←𝜀𝑦+𝜀 and𝛿𝑦←𝛿𝑦+𝛿 for all𝑦∈𝑌
# 3. Noisy summation (cf. Aggregation Service)
𝜏←
(
∞ if𝛿 = 0,
Λ1·( 1+ log(Λ0/𝛿)/𝜀) if𝛿 > 0.
𝑆←∅
for𝑘∈K do
𝑐𝑘←𝜉+ ˝ (𝑦,𝑘′,𝑣)∈𝑅 :𝑦∈𝑌,𝑘 ′=𝑘𝑣 for 𝜉∼ DLap𝜏(𝜀/Λ1)
if𝜏 =∞ or𝑐𝑘 >𝜏 then
𝑆←𝑆∪{( 𝑘,𝑐𝑘)}
return ({(𝐿𝑥,𝑠𝑥)}𝑥∈X,{(𝜀𝑦,𝛿𝑦)}𝑦∈Y,𝑅),𝑆 
where the last inequality follows because ˝ 𝑡 :𝑌𝑥,𝑡∋𝑦𝜀𝑡≤𝜀∗ for all
𝑦∈Y and ˝ 𝑦∈𝑌𝑥𝑣𝑦≤ Λ1 for all𝑥∈X . Similarly,
∑︁
𝑡
𝛿𝑥,𝑡 =
∑︁
𝑡
𝛿𝑡
Λ0
·|𝑌𝑥,𝑡|

≤
∑︁
𝑦∈𝑌𝑥
1
Λ0
∑︁
𝑡 :𝑌𝑥,𝑡∋𝑦
𝛿𝑡 ≤ 𝛿∗,
where the last inequality follows because ˝ 𝑡 :𝑌𝑥,𝑡∋𝑦𝛿𝑡≤𝛿∗ for all
𝑦∈Y and|𝑌𝑥|≤ Λ0 for all𝑥∈X . □
4.3 Privacy of PAA Summary Reports
The DP properties of PAA can be proved with the same formal-
ism of the interactive mechanismMSR (Algorithm 6), with just a
reinterpretation of databases and the adjacency notion.
In the context of PAA summary reports, we model a database
𝐷∈D PAA as consisting of records(𝑥,𝑦)∈X×Y ⊥ whereX is the
set of all pairs consisting of (device,𝑡) for𝑡∈T is the time window
andY⊥ is the set of all possible states of the shared storageY and
a dummy shared storage𝑦⊥ (denoting an “empty” shared storage).
For any database𝐷∈D and𝑥∈X , let𝐷−𝑥 be the dataset obtained
by replacing all shared storage states associated to 𝑥 by𝑦⊥. The
notion of queries, responses and states remain the same as in the
case of ARA.
391

Proceedings on Privacy Enhancing Technologies 2025(3) Ghazi et al.
The following theorem has essentially the same proof as Theo-
rem 4.3, so we do not repeat it.
Theorem 4.5. MSR satisfies(𝜀∗,𝛿∗)-IDP with respect to aforemen-
tioned set of databases and neighbouring relation for PAA.
Hence, a corollary similar to Theorem 4.4 holds.
Corollary 4.6. MSR satisfies(𝜀∗,𝛿∗)-DP with respect to afore-
mentioned set of databases and neighbouring relation for ARA.
Note however, that it might be desirable to have privacy guaran-
tees per device, but the above only provides a privacy guarantee
per (device, time window𝑡). One could try to obtain a device-level
DP guarantee by using the “group privacy” property of DP.
Fact 4.7 (Group Privacy [ 45]). If distributions𝑃0,𝑃 1,...,𝑃 𝑘 are
such that𝑃𝑖≈𝜀,𝛿 𝑃𝑖+1 for all𝑖, then the distributions 𝑃0≈𝜀′,𝛿′ 𝑃𝑘 for
𝜀′ =𝑘𝜀 and𝛿′ =𝛿𝑒𝑘𝜀−1 𝑒𝜀−1 .
However, it is tricky to apply this property because if the shared
storage is disabled or cleared in a certain time window 𝑡, it can
affect the future states of shared storage and thereby also affect the
aggregatable reports generated by events on that device.
One can however formulate a weaker notion of device-level DP
guarantee for PAA, by considering a variant of DP with gradual
expiration that is considered in [4].
Definition 4.8 (DP for Interactive Mechanisms with Gradual Ex-
piration). An interactive mechanism M satisfies(𝜀,𝛿)-DP with
gradual expiration if for all interactive adversaries A, all 𝑒 ∈ Z,
all devices𝑢∈U and all𝑡1,𝑡 2∈T with𝑡1 <𝑡2, the distributions
IT

M−(𝑢,>𝑡1) :A  ≈𝜀′,𝛿′ IT  M−(𝑢,>𝑡2) :A  where𝜀′ =𝜀(𝑡2−𝑡1),
𝛿′ =𝛿𝑒𝜀′−1 𝑒𝜀−1 , andM−(𝑎,>𝑡1) denotes the mechanism that replaces
the dataset𝐷𝑡 by𝐷−(𝑢,>𝑡1) 𝑡 (obtained by replacing all shared storage
states associated to(𝑢,𝑡) for𝑡 >𝑡1 by𝑦⊥) at each step.
It is immediate to see that ifM satisfies(𝜀,𝛿)-DP, then it satisfies
(𝜀,𝛿)-DP with gradual expiration via Theorem 4.7. Thus, we get
that in the context of PAA, the mechanismMSR satisfies(𝜀∗,𝛿∗)-DP
with gradual expiration.
4.4 Proof of Theorem 4.2
As mentioned before, to prove Theorem 4.2, we apply the tool of
DP filters [ 25] in the setting of IDP [ 17, 19], that we discuss in
Sections 4.4.1 and 4.4.2 below respectively.
4.4.1 Privacy Filters. To discuss privacy filters, consider databases
𝑈⊆X that contain only privacy units. We use𝑈−𝑥 to denote the
dataset𝑈 ∖{𝑥}.7
For Θ = R≥0×[ 0, 1] being the parameter space underlying(𝜀,𝛿)-
DP, let𝜙 : Θ∗→{
 ,
 } be a function, called filter, that maps a
sequence of parameters to
 or
 . For anyR, andP(X) denoting
the powerset ofX, we consider the following notion of a universal
interactive mechanismM𝜙 :S×P(X)×Q U→S× Δ((R∪{⊥})) ,
parameterized by𝜙, that performs on-the-fly privacy budgeting
defined as follows:
7The notation𝑈−𝑥 is useful only when𝑥∈𝑈 . Otherwise𝑈−𝑥 =𝑈 , which can lead
to vacuous statements. Since these are also correct we do not enforce that𝑥∈𝑈 .
•Q U :={𝑞 :P(X)→ Δ(R)} consists of “universal queries” that
can be arbitrary “one-shot” mechanisms; an example of such a
mechanism is𝑞(𝑈) = ˝ 𝑥∈𝑈 𝑣𝑥+ DLap(𝑎), where𝑣𝑥 and𝑎 are
chosen as part of the query,
•S = Θ∗ consists of sequences of privacy parameters.
On query𝑞 such that𝑞 satisfies𝜃-DP,8M𝜙 operates as follows:
M𝜙((𝜃1,...,𝜃 𝑡),𝐷,𝑞)
:=
(
((𝜃1,...,𝜃 𝑡,𝜃),𝑞(𝐷)) if𝜙(𝜃1,...,𝜃 𝑡,𝜃) =
((𝜃1,...,𝜃 𝑡, 0),⊥) if𝜙(𝜃1,...,𝜃 𝑡,𝜃) =
That is, if𝜙 applied on the current state (sequence of𝜃𝑖’s so far)
concatenated with the current𝜃 returns
 , then𝜃 is concatenated
to the current state, and the one-shot mechanism𝑞 is applied on𝑈 .
But if not, then 0 is concatenated to the state and⊥ is returned.
The interactive mechanismM𝜙 interacts with an adversaryA
in the same way as in Algorithm 5 to produce IT M𝜙 :A.
For(𝜀,𝛿)∈ Θ, we define the filter𝜙𝜀,𝛿 : Θ∗→{
 ,
 } as:
𝜙𝜀,𝛿((𝜀1,𝛿 1),..., (𝜀𝑛,𝛿𝑛)) :=
 

if
𝑛˝
𝑖=1
𝜀𝑖≤𝜀 &
𝑛˝
𝑖=1
𝛿𝑖≤𝛿
otherwise.
It is known thatM𝜙 with the above filter satisfies DP guarantees.
Lemma 4.9 ([ 25]). For all (𝜀,𝛿) ∈Θ,M𝜙𝜀,𝛿 satisfies(𝜀,𝛿)-DP
against stable adversaries. 9
4.4.2 Individual Differential Privacy. We now consider a universal
interactive mechanism with a privacy filter but using the notion of
IDP [17, 19].
Definition 4.10. For𝑝 :X→ Θ, a mechanismF :P(X) →
Δ(R) satisfies𝑝-IDP if for all𝑈∈P(X) and all𝑥∈X , it holds that
F(𝑈)≈ 𝑝(𝑥)F(𝑈−𝑥).
As before, for 𝜙 : Θ∗→{
 ,
 }, we consider a universal in-
teractive mechanismMind 𝜙 :S×P(X)×Q U→S× Δ(R) , that
performs on-the-fly privacy budgeting, where S = (ΘX)∗ con-
sists of sequences of privacy parameters, one for each unit𝑥∈X .
On query𝑞 such that𝑞 satisfies𝑝-IDP,Mind 𝜙 operates as follows.
On current state (𝑝1,...,𝑝 𝑡), it constructs a “masked database”
𝑈 :=𝑈∩{𝑥 :𝜙(𝑝1(𝑥),...,𝑝 𝑡(𝑥),𝑝(𝑥)) =
 } and the consumed
individual privacy𝑝𝑡+1 :X→ Θ as:
𝑝𝑡+1(𝑥) :=
(
𝑝(𝑥) if𝜙(𝑝1(𝑥),...,𝑝 𝑡(𝑥),𝑝(𝑥)) =
0 if𝜙(𝑝1(𝑥),...,𝑝 𝑡(𝑥),𝑝(𝑥)) =
 .
And the mechanism returns,
M𝜙((𝑝1,...,𝑝 𝑡),𝑈,𝑞) :=((𝑝1,...,𝑝 𝑡+1),𝑞(𝑈)).
Lemma 4.11. For all(𝜀,𝛿)∈ Θ,Mind 𝜙𝜀,𝛿 satisfies(𝜀,𝛿)-DP against
stable adversaries.
8𝑞 may satisfy𝜃-DP for a number of different𝜃∈ Θ, and while any such𝜃 could be
used, it is important to specify a particular choice of𝜃 to makeM𝜙 well-defined. The
definition ofQ could be modified to additionally provide the specific𝜃 along with𝑞,
but we avoid doing so for simplicity.
9[25] also provides an improved “advanced composition”-like filter for(𝜀,𝛿)-DP, that
was subsequently improved in [46]. However, since we only use this version, we do
not state the advanced version.
392

On the Differential Privacy and Interactivity of Privacy Sandbox Reports Proceedings on Privacy Enhancing Technologies 2025(3)
Proof. Fix some database𝑈⊆X . Consider a stable adversary
A : R∗ → (P(X)×Q U)∪{
 } that returns the same data-
base𝑈 on each step. We want to show that for any 𝑥 ∈ Xit
holds that IT

Mind 𝜙𝜃 :A  ≈𝜀,𝛿 IT  Mind 𝜙𝜃 −𝑥 :A  . This follows
by “zooming in on unit 𝑥”. Namely, considerX′ ={𝑥}, and let
Q′ U :={𝑞 :X′→ Δ(R)} be the set of universal queries onX′. Con-
struct an adversaryA′ :R∗→(P(X ′)×Q ′ U)∪{
 } as follows:
A′(Π) first computes(𝐷,𝑞)←A( Π), and return(𝐷′,𝑞′) where
𝐷′ =𝐷∩X′ and𝑞′(𝑈′) :=𝑞( ˜𝑈−𝑥∪𝑈′) for𝑈′⊆X′ and ˜𝑈−𝑥⊆𝑈−𝑥
that have the privacy budget to participate. Thus, when𝑈∋𝑥, we
have IT

Mind 𝜙𝜃 :A  ≡ IT M𝜙𝜃 :A′≈𝜀,𝛿 IT M𝜙𝜃 −𝑥 :A′≡
IT

Mind 𝜙𝜃
−𝑥
:A

, by Theorem 4.9. □
4.4.3 Putting it Together: Proof of Theorem 4.2.
Proof of Theorem 4.2. LetM be an interactive mechanism sat-
isfying(𝜀∗,𝛿∗)-IDP guarantees. To prove the statement it suffices
to show that for any adversaryA that interacts withM, there is
an adversaryA′ forM𝜙𝜀∗,𝛿∗ such that
IT

Mind 𝜙𝜀∗,𝛿∗ :A′

≡ IT(𝑀 :A), and
IT

Mind 𝜙𝜀∗,𝛿∗
−𝑥
:A′

≡ IT(𝑀−𝑥 :A).
Conditioned on a sequence(𝑟1,...,𝑟 𝑡) of responses, let the corre-
sponding states ofM when interacting withA be𝑆0,𝑆 1,...,𝑆 𝑡 ;
note𝑆𝑖 is deterministic given database𝐷𝑖 and query𝑞𝑖, which are
in turn deterministic given𝑟1,...,𝑟 𝑖−1.
We defineA′ that on input(𝑟1,...,𝑟 𝑡), computes(𝐷𝑡+1,𝑞𝑡+1)←
A(𝑟1,...,𝑟 𝑡) and returns(𝐷𝑡+1,𝑞′ 𝑡+1) where𝑞′ 𝑡+1( ˜𝐷) is distribution
over responses𝑟 returned byM(𝑆𝑡, ˜𝐷,𝑞𝑡+1). It is easy to see that
A′ satisfy the condition sinceM𝜙𝜀∗,𝛿∗ will always output𝑞′(𝐷𝑡+1)
givenM is(𝜀∗,𝛿∗)-IDP, that is, the filter never masks any ele-
ment of the database; hence from Theorem 4.11, we conclude that
IT(𝑀 :A)≈𝜀∗,𝛿∗ IT(𝑀−𝑥 :A). □
5 Analysis of Event-Level Reports
The database and the privacy unit in event-level reports is the same
as described in Section 4.2.
The event-level API is based on what we refer to as interactive
randomized response (IRR); see Algorithm 8 for details. In this setting,
we have finite setO1,..., O𝑖,... of outputs at each time step and a
finite setO⊆O 1×···×O 𝑖×··· of valid combinations of these
outputs. The algorithm decides (randomly) at the very beginning
of the run whether it is going to report truthfully (i.e., 𝑠∗ =⊥) or
whether it is going to report some other output (i.e., 𝑠∗∈O ). In
the latter case, the algorithm simply reports based on𝑠∗ regardless
of the input. On the other hand, in the former case, the algorithm
evaluates the query it receives and outputs truthfully in each step.
It is possible to see that event-level reports can be captured by
the interactive mechanismMER. Indeed, let us chooseO(𝑥) so that
O(𝑥) 𝑖 is the set of all combinations of possible reports that could
be sent at𝑖th second. Then𝑞𝑥 on𝑖th iteration is the function that
creates the reports that would be sent on 𝑖th second. (Note that
we allow𝑞𝑥 to depend on all the events, not just the one created
Algorithm 7 Interactive Transcript IT(M : A).
Inputs: ⊲ Interactive mechanismM with initial state𝑆0,
⊲ A distribution of interactive adversaries A.
SampleA∼ A.
return IT(M :A).
Algorithm 8 InteractiveRandomizedResponseI𝜀,O.
Params: ⊲ Privacy parameter𝜀∈ R,
⊲ Output setO⊆O 1×···×O 𝑖×··· .
Inputs: ⊲ State𝑆 encoding𝑖∈ N and𝑠∗∈O∪{⊥} ,
⊲ Set of events𝑌⊆Y of events,
⊲ Query𝑞 :P(Y)→O 𝑖.
if𝑖 = 1 then
Set𝑠∗ to⊥ with probability 𝑒𝜀−1 𝑒𝜀+|O|− 1 , otherwise set it to a
random sample fromO
if𝑠∗ =⊥ then
return (𝑠∗,𝑞(𝑌))
else
return (𝑠∗,𝑠∗ 𝑖)
during this second, this makes our privacy guarantee stronger than
actually necessary.)
The main result of this section is that this is indeed𝜀-DP.
Theorem 5.1. MER satisfies𝜀-DP.
To prove this theorem, one may notice that while our definition
of DP for interactive mechanisms assumed that the adversary is
deterministic it is not strictly necessary. This follows from a simple
joint-convexity property of DP.
Fact 5.2 (Joint Convexity (see e.g. Lemma B.1 in [ 9])). Given
two families of distributions{𝑃𝑖}𝑖 and{𝑄𝑖}𝑖 , if 𝑃𝑖≈𝜀,𝛿 𝑄𝑖 for all𝑖,
then for all mixture distributions 𝑃 = ˝ 𝑖𝛼𝑖𝑃𝑖 and𝑄 = ˝ 𝑖𝛼𝑖𝑄𝑖 , it
holds that𝑃≈𝜀,𝛿 𝑄.
We extend the notion of a transcript to support distributions of
adversaries (Algorithm 7). For any distribution A over interactive
adversaries, by applying the above fact for𝑃A = IT(M :A) and
𝑄A = IT(M−𝑥 :A) for eachA in the support of A, we get the
following corollary.
Corollary 5.3. For all mechanismsM, if for all 𝑥∈X and all
interactive adversaries it holds that IT(M :A)≈𝜀,𝛿 IT(M−𝑥 :A),
then IT(M : A)≈𝜀,𝛿 IT(M−𝑥 : A) holds for all distributions A over
interactive adversaries.
Proof of Theorem 5.1. The proof consists of two parts: first,
we show thatMER is private whenX has only one element𝑥; next,
we prove that general privacy guarantee follows from this.
Assume thatX ={𝑥}. Note that state of the mechanism does
not change over the course of execution. Let us denote the random
variable for this state as𝑠∗. It is easy to see that for any ˜𝑜∈O ,
Pr[IT(MER :A) = ˜𝑜 | 𝑠∗ = ˜𝑜] =
Pr[IT M−𝑥 ER :A = ˜𝑜 | 𝑠∗ = ˜𝑜] = 1.
393

Proceedings on Privacy Enhancing Technologies 2025(3) Ghazi et al.
Algorithm 9 Interactive mechanismMER :S×D×Q→S× Δ(R) .
Params: ⊲ Privacy parameter𝜀 > 0,
⊲ Output sets{O(𝑥)}𝑥∈X .
Inputs: ⊲ State𝑆 encoding𝑖∈ N and{𝑠∗ 𝑥∈O (𝑥)∪{⊥}} 𝑥∈X ,
⊲ Database𝐷∈D ,
⊲ Queries{𝑞𝑥 :Y∗→O (𝑥) 𝑖 }𝑥∈X .
for𝑥∈X do
(𝑠′ 𝑥,𝑟𝑥)←I 𝜀,O(𝑥)(𝑖,𝑠∗ 𝑥,𝑁𝐷(𝑥),𝑞𝑥)
return ((𝑖,{𝑠′ 𝑥}𝑥∈X),{𝑟𝑥}𝑥∈X)
Therefore,
Pr[IT(MER :A) = ˜𝑜]≥ Pr[𝑠∗ = ˜𝑜] = 1 𝑒𝜀+|O (𝑥)|− 1 and
Pr[IT M−𝑥 ER :A = ˜𝑜]≥ Pr[𝑠∗ = ˜𝑜] = 1 𝑒𝜀+|O (𝑥)|− 1.
Furthermore, for any ˜𝑜∈O ,
Pr[IT(MER :A) = ˜𝑜]
= Pr[IT(MER :A) = ˜𝑜∧𝑠∗ =⊥]+ Pr[IT(MER :A) = ˜𝑜∧𝑠∗ ≠⊥]
≤ Pr[𝑠∗ =⊥]+ Pr[𝑠∗ = ˜𝑜]
= 𝑒𝜀− 1 𝑒𝜀+|O (𝑥)|− 1+ 1 𝑒𝜀+|O (𝑥)|− 1 = 𝑒𝜀 𝑒𝜀+|O (𝑥)|− 1,
which implies that IT(MER :A)≈𝜀,0 IT M−𝑥 ER :A.
First, we denote the mechanism MER operating on a dataset
X ={𝑥} asM(𝑥) ER . Let us now assume thatX > 1. We claim that
for each𝑥∈X , any adversaryA, and any transcript Π, there is a
distribution A′ over adversaries forM(𝑥) ER and a transcript Π′ for
M(𝑥) ER such that
Pr[IT(MER :A) = Π] = Pr[IT

M(𝑥) ER : A′

= Π′],
Pr[IT M−𝑥 ER :A = Π] = Pr[IT  M(𝑥) ER −𝑥 : A′  = Π′].
Note that this implies thatMER is𝜀-DP.
Let us now constructA′. First, we define an adversaryA′ {𝑠∗ 𝑥′}𝑥′≠𝑥
that runsA using actual response for𝑥 and simulated responses
for𝑥′ ≠𝑥 using𝑠∗ 𝑥′ (note that if the state is fixed, the mechanism
is deterministic). It is clear that a distribution A′ that samples first
{𝑠∗ 𝑥′}𝑥′≠𝑥 and returns the adversaryA′ {𝑠∗ 𝑥′}𝑥′≠𝑥 satisfies the desired
condition. □
6 Conclusion
In this work, we modeled the summary reports in the Attribution
Reporting API (ARA) and the Private Aggregation API (PAA), as
well as the event-level reports in ARA. We established formal DP
guarantees for these mechanisms, even against the stringent no-
tion of interactive adversaries that can influence the database in
subsequent rounds based on responses in previous rounds.
Acknowledgments
We thank the anonymous reviewers, for their feedback, which sig-
nificantly improved the clarity of this paper. We thank Roxana
Geambasu, Pierre Tholoniat for discussions about [42]. We are also
grateful to Jolyn Yao and Christina Ilvento for their invaluable con-
tributions, without which this paper might not have been possible.
394

On the Differential Privacy and Interactivity of Privacy Sandbox Reports Proceedings on Privacy Enhancing Technologies 2025(3)
References
[1] Hidayet Aksu, Badih Ghazi, Pritish Kamath, Ravi Kumar, Pasin Manurangsi, Adam
Sealfon, and Avinash V. Varadarajan. 2024. Summary Reports Optimization in
the Privacy Sandbox Attribution Reporting API. PoPETS 2024, 4 (2024), 605–621.
[2] Hidayet Aksu and Charlie Harrison. 2023. Summary reports with key discov-
ery. Google. https://github.com/WICG/attribution-reporting-api/blob/main/
aggregate_key_discovery.md
[3] Hidayet Aksu, Alexander Knop, and Pasin Manurangsi. 2024. Reach Implementa-
tion Best Practices in the Privacy Sandbox Shared Storage + Private Aggregation
APIs. Google. https://github.com/patcg-individual-drafts/private-aggregation-
api/blob/main/reach_whitepaper.md
[4] Joel Daniel Andersson, Monika Henzinger, Rasmus Pagh, Teresa Anna Steiner,
and Jalaj Upadhyay. 2024. Continual Counting with Gradual Privacy Expiration.
In NeurIPS.
[5] Apple. 2024. SKAdNetwork. Apple. https://developer.apple.com/documentation/
storekit/skadnetwork/
[6] Mark Bun and Thomas Steinke. 2016. Concentrated Differential Privacy: Sim-
plifications, Extensions, and Lower Bounds. In Theory of Cryptography (TCC)
(Lecture Notes in Computer Science, Vol. 9985) , Martin Hirt and Adam D. Smith
(Eds.). 635–658. https://doi.org/10.1007/978-3-662-53641-4_24
[7] United States Census Bureau. 2023.Shared Storage overview. United States Census
Bureau. https://www.census.gov/programs-surveys/decennial-census/decade/
2020/planning-management/process/disclosure-avoidance.html
[8] Lynn Chua, Qiliang Cui, Badih Ghazi, Charlie Harrison, Pritish Kamath, Walid
Krichene, Ravi Kumar, Pasin Manurangsi, Nicolas Mayoraz, Hema Venkata Kr-
ishna Giri Narra, Steffen Rendle, Amer Sinha, Avinash V. Varadarajan, and
Chiyuan Zhang. 2024. Training Differentially Private Ad Prediction Models
With Semi-Sensitive Features. In AdKDD.
[9] Lynn Chua, Badih Ghazi, Pritish Kamath, Ravi Kumar, Pasin Manurangsi, Amer
Sinha, and Chiyuan Zhang. 2024. How Private are DP-SGD Implementations?.
In International Conference on Machine Learning, ICML . OpenReview.net. https:
//openreview.net/forum?id=xWI0MKwJSS
[10] Luke Crouch and Maxx Crawford. 2022. Over a decade of anti-tracking work
at Mozilla. Mozilla. https://blog.mozilla.org/en/privacy-security/mozilla-anti-
tracking-milestones-timeline/
[11] Matthew Dawson, Badih Ghazi, Pritish Kamath, Kapil Kumar, Ravi Kumar, Bo
Luan, Pasin Manurangsi, Nishanth Mundru, Harikesh Nair, Adam Sealfon, and
Shengyu Zhu. 2023. Optimizing Hierarchical Queries for the Attribution Report-
ing API. In AdKDD.
[12] John Delaney, Badih Ghazi, Charlie Harrison, Christina Ilvento, Ravi Kumar,
Pasin Manurangsi, Martin Pál, Karthik Prabhakar, and Mariana Raykova. 2024.
Differentially Private Ad Conversion Measurement. PoPETS 2024, 2 (2024), 124–
140.
[13] Carson Denison, Badih Ghazi, Pritish Kamath, Ravi Kumar, Pasin Manurangsi,
Krishna Giri Narra, Amer Sinha, Avinash V. Varadarajan, and Chiyuan Zhang.
2023. Private Ad Modeling with DP-SGD. In AdKDD.
[14] Damien Desfontaines. 2025. A list of real-world uses of differential privacy . https:
//desfontain.es/blog/real-world-differential-privacy.html
[15] Cynthia Dwork, Krishnaram Kenthapadi, Frank McSherry, Ilya Mironov, and
Moni Naor. 2006. Our Data, Ourselves: Privacy Via Distributed Noise Generation.
In EUROCRYPT. 486–503.
[16] Cynthia Dwork, Frank McSherry, Kobbi Nissim, and Adam D. Smith. 2016. Cali-
brating Noise to Sensitivity in Private Data Analysis. J. Priv. Confidentiality 7, 3
(2016), 17–51.
[17] Hamid Ebadi, David Sands, and Gerardo Schneider. 2015. Differential Privacy:
Now it’s Getting Personal. In POPL. 69–81.
[18] Renan Feldman. 2024. Public Cloud TEE Requirements . Google.
https://github.com/privacysandbox/protected-auction-services-docs/blob/
main/public_cloud_tees.md
[19] Vitaly Feldman and Tijana Zrnic. 2021. Individual Privacy Accounting via a
Rényi Filter. In NeurIPS. 28080–28091.
[20] Arpita Ghosh, Tim Roughgarden, and Mukund Sundararajan. 2012. Universally
Utility-maximizing Privacy Mechanisms. SIAM J. Comput. 41, 6 (2012), 1673–
1693.
[21] Google. 2022. See how your community moved differently due to COVID-19 . https:
//www.google.com/covid19/mobility/
[22] Shlomi Hod and Ran Canetti. 2025. Differentially Private Release of Israel’s
National Registry of Live Births. In S & P. 101–101.
[23] Joseph J. Pfeiffer III, Denis Charles, Davis Gilton, Young Hun Jung, Mehul Parsana,
and Erik Anderson. 2021. Masked LARk: Masked Learning, Aggregation and
Reporting worKflow. arXiv:2110.14794
[24] Privacy Sandbox. 2024. Private Aggregation API fundamentals . Google.
https://developers.google.com/privacy-sandbox/private-advertising/private-
aggregation/fundamentals#contribution_budget
[25] Ryan M. Rogers, Salil P. Vadhan, Aaron Roth, and Jonathan R. Ullman. 2016.
Privacy Odometers and Filters: Pay-as-you-Go Composition. InNIPS. 1921–1929.
[26] Privacy Sandbox. 2021. Attribution Reporting for Web overview: Event-level reports.
Google. https://developers.google.com/privacy-sandbox/private-advertising/
attribution-reporting#event-level_reports
[27] Privacy Sandbox. 2021. Attribution Reporting for Web overview: Summary reports .
Google. https://developers.google.com/privacy-sandbox/private-advertising/
attribution-reporting#summary_reports
[28] Privacy Sandbox. 2021. Attribution Reporting: generating summary reports .
Google. https://developers.google.com/privacy-sandbox/private-advertising/
attribution-reporting/summary-reports
[29] Privacy Sandbox. 2022. Attribution Reporting for Web overview. Google. https:
//developers.google.com/privacy-sandbox/relevance/attribution-reporting
[30] Privacy Sandbox. 2022. Differential Privacy. Google. https://github.com/WICG/
attribution-reporting-api/blob/main/AGGREGATE.md#differential-privacy
[31] Privacy Sandbox. 2022. Maximize ad relevance without third-party cookies .
Google. https://privacysandbox.com/news/maximize-ad-relevance-after-third-
party-cookies/
[32] Privacy Sandbox. 2022. Private Aggregation API overview . https://developers.
google.com/privacy-sandbox/relevance/private-aggregation
[33] Privacy Sandbox. 2024. Attribution Reporting with event-level reports . Google.
https://github.com/WICG/attribution-reporting-api/blob/main/EVENT.md
[34] Privacy Sandbox. 2024. Intelligent Tracking Prevention 2.3 . Google. https:
//github.com/privacysandbox/aggregation-service/blob/main/docs/batching-
strategies.md/#aggregatable-report-accounting
[35] Privacy Sandbox. 2024. A list of real-world uses of differential privacy . https:
//desfontain.es/blog/real-world-differential-privacy.html
[36] Privacy Sandbox. 2024. Shared Storage overview . Google. https://developers.
google.com/privacy-sandbox/private-advertising/shared-storage
[37] Privacy Sandbox. 2024. Unique reach measurement . Google. https:
//developers.google.com/privacy-sandbox/private-advertising/private-
aggregation/unique-reach
[38] Privacy Sandbox. 2024. Update on the plan for phase-out of third-party cookies on
Chrome. Google. https://privacysandbox.com/news/update-on-the-plan-for-
phase-out-of-third-party-cookies-on-chrome/
[39] Privacy Sandbox. 2025. Aggregation Service for the Attribution Reporting
API. Google. https://github.com/WICG/attribution-reporting-api/blob/main/
AGGREGATION_SERVICE_TEE.md#initial-experiment-plans
[40] Chrome Platform Status. 2024. Percentage of page loads over time for Conversion-
APIAll. Google. https://chromestatus.com/metrics/feature/timeline/popularity/
3365
[41] Chrome Platform Status. 2024. Percentage of page loads over time for PrivateAg-
gregationApiAll. Google. https://chromestatus.com/metrics/feature/timeline/
popularity/4333
[42] Pierre Tholoniat, Kelly Kostopoulou, Peter McNeely, Prabhpreet Singh Sodhi,
Anirudh Varanasi, Benjamin Case, Asaf Cidon, Roxana Geambasu, and Mathias
Lécuyer. 2024. Cookie Monster: Efficient On-Device Budgeting for Differentially-
Private Ad-Measurement Systems. In SOSP. 693–708.
[43] Martin Thomson. 2022. Privacy Preserving Attribution for Advertising .
Mozilla. https://blog.mozilla.org/en/mozilla/privacy-preserving-attribution-
for-advertising/
[44] Matilde Tullii, Solenne Gaucher, Hugo Richard, Eustache Diemert, Vianney
Perchet, Alain Rakotomamonjy, Clément Calauzènes, and Maxime Vono. 2024.
Position Paper: Open Research Challenges for Private Advertising Systems under
Local Differential Privacy. In WISE. 107–122.
[45] Salil P. Vadhan. 2017. The Complexity of Differential Privacy. In Tutorials on the
Foundations of Cryptography, Yehuda Lindell (Ed.). Springer, 347–450.
[46] Justin Whitehouse, Aaditya Ramdas, Ryan Rogers, and Steven Wu. 2023. Fully-
Adaptive Composition in Differential Privacy. In ICML. 36990–37007.
[47] Wikipedia. 2024. Authenticated encryption with associated data . Wikipedia.
https://en.wikipedia.org/wiki/Authenticated_encryption#Authenticated_
encryption_with_associated_data
[48] John Wilander. 2019. Intelligent Tracking Prevention 2.3. Apple. https://webkit.
org/blog/9521/intelligent-tracking-prevention-2-3/
[49] John Wilander. 2021. Introducing Private Click Measurement, PCM . Apple. https:
//webkit.org/blog/11529/introducing-private-click-measurement-pcm/
[50] Albert Wu. 2024. Support for Requerying in Aggregation Service: Feedback Re-
quested. Privacy Sandbox. https://github.com/privacysandbox/aggregation-
service/issues/71
[51] Yingtai Xiao, Jian Du, Shikun Zhang, Qiang Yan, Danfeng Zhang, and Daniel
Kifer. 2024. Click Without Compromise: Online Advertising Measurement via
Per User Differential Privacy. arXiv:2406.02463
395

Proceedings on Privacy Enhancing Technologies 2025(3) Ghazi et al.
A Analysis of (Truncated) Discrete Laplace
Mechanism
We provide a proof of Theorem 3.3 for completeness. The first
component of this proof is the following tail-bound for discrete
Laplace distributions.
Lemma A.1. Let𝜏 be an integer such that 𝜏≥ log(1/𝛿)/𝑎+ Δ.
Then Pr𝑋∼DLap𝜏(𝑎)[𝑋 >𝜏− Δ]≤ 𝛿.
Proof.
Pr
𝑋∼DLap𝜏(𝑎)
[𝑋 >𝜏] =
˝𝜏
𝑥=𝜏−Δ+1𝑒−𝑎𝑥 ˝𝜏
𝑥=−𝜏𝑒−𝑎|𝑥|
≤
˝𝜏
𝑥=𝜏−Δ+1𝑒−𝑎𝑥 ˝𝜏
𝑥=0𝑒−𝑎𝑥
≤
˝∞
𝑥=𝜏−Δ+1𝑒−𝑎𝑥 ˝∞
𝑥=0𝑒−𝑎𝑥
≤ 𝑒−𝑎(𝜏−Δ) ≤ 𝛿.
where the last inequality uses that𝜏≥ log(1/𝛿)/𝑎+ Δ. □
Proof of Theorem 3.3. First, we observe that by shifting the
vectors𝑢 and𝑣, we can assume without loss of generality that𝑢 = 0.
First, we consider the case of (untruncated) discrete Laplace noise.
Let𝑃 and𝑄 be the distributions of𝑢+𝜁 and𝑣+𝜁 respectively for
𝜁∼ DLap(𝑎)⊗𝑑. In other words, for any𝑤∈ Z𝑑, it holds that
𝑃(𝑤) = 1 𝑍𝑒−𝑎∥𝑢−𝑤∥1 and 𝑄(𝑤) = 1 𝑍𝑒−𝑎∥𝑣−𝑤∥1
where𝑍 =(𝑒𝑎+1 𝑒𝑎−1)𝑑. Thus, we have
𝑃(𝑤)
𝑄(𝑤) =𝑒−𝑎(∥𝑢−𝑤∥1−∥𝑣−𝑤∥1)
and it is thus easy to see that
𝑒−𝑎Δ≤𝑒−𝑎∥𝑢−𝑣∥1≤ 𝑃(𝑤) 𝑄(𝑤)≤𝑒𝑎∥𝑢−𝑣∥1≤𝑒𝑎Δ
and thus,𝑃≈𝜀,0𝑄 when𝑎 =𝜀/Δ.
Next, moving to the case of truncated discrete Laplace noise, let
𝑃 and𝑄 be the distributions of 𝑢+𝜁 and𝑣+𝜁 respectively for
𝜁∼ DLap𝜏(𝑎)⊗𝑑. In particular, we have
𝑃(𝑤) =
(
1
𝑍𝑒−𝑎∥𝑢−𝑤∥1 if∥𝑢−𝑤∥∞≤𝜏
0 if∥𝑢−𝑤∥∞ >𝜏
and similarly for𝑄, where𝑍 = ˝𝜏 𝑥=−𝜏𝑒−𝑎|𝑥|. Let𝑆 :={𝑤 :∥𝑢−
𝑤∥∞≤𝜏 and∥𝑣−𝑤∥∞≤𝜏}. Similar to the case of untruncated
case above, it follows that for all 𝑤 ∈ 𝑆, it holds that 𝑒−𝑎Δ ≤
𝑃(𝑤)/𝑄(𝑤) ≤𝑒𝑎Δ. Thus, for 𝑎 = 𝜀/Δ, it holds for all 𝐸 ⊆ Z𝑑
that
𝑃(𝐸) = 𝑃(𝐸∩𝑆)+ 𝑃(𝐸 ∖𝑆)
≤ 𝑒𝜀𝑄(𝐸∩𝑆)+ 𝑃(𝐸 ∖𝑆)
≤ 𝑒𝜀𝑄(𝐸)+ 𝑃(Z𝑑 ∖𝑆)
Thus, 𝑃 ≈𝜀,𝛿 𝑄 where𝛿 := 𝑃(Z𝑑 ∖𝑆). To complete the proof,
we need to show that when 𝜏≥ Δ(1+ log(𝑠/𝛿)/𝜀), it holds that
𝑃(Z𝑑 ∖𝑆)≤ 𝛿; recall that𝑢 and𝑣 differ on𝑠 coordinates. We have
𝑃(Z𝑑 ∖𝑆) = 1−𝑃(𝑆)
= 1−
𝑑Ö
𝑖=1
Pr
𝑤𝑖∼𝑢𝑖+DLap𝜏(𝑎)
[|𝑤𝑖−𝑣𝑖|≤ 𝜏]
≤ 𝑠· Pr𝑋∼DLap𝜏(𝑎)[𝑋 >𝜏− Δ] (1)
where, we use that when𝑢𝑖 =𝑣𝑖, we have
Pr
𝑤𝑖∼𝑢𝑖+DLap𝜏(𝑎)
[|𝑤𝑖−𝑣𝑖|≤ 𝜏] = 1
and when𝑢𝑖 ≠𝑣𝑖, we have
Pr
𝑤𝑖∼𝑢𝑖+DLap𝜏(𝑎)
[|𝑤𝑖−𝑣𝑖|≤ 𝜏] = Pr 𝑋∼DLap𝜏(𝑎) [|𝑋+𝑢𝑖−𝑣𝑖|≤ 𝜏]
≥ 1− Pr
𝑋∼DLap𝜏(𝑎)
[𝑋 >𝜏− Δ].
Note that Theorem A.1 implies that
Pr
𝑋∼DLap𝜏(𝑎)
[𝑋 >𝜏− Δ]≤ 𝛿/𝑠.
since𝜏≥ Δ(1+ log(𝑠/𝛿)/𝜀). Combining with Equation (1), we get
that𝑃(Z𝑑 ∖𝑆)≤ 𝛿, thereby completing the proof. □
B Extension to other notions of DP
While we primarily studied(𝜀,𝛿)-DP notion in this paper, our defi-
nitions and techniques readily extend to any other notion of DP that
admits privacy filters. In particular, we could consider the following
notion of Approximate zero Concentrated DP.
Definition B.1 ([ 6]). Two distributions𝑃,𝑄 are said to be(𝜌,𝛿)-
AzCDP-indistinguishable10 if there exist events𝑊 and𝑊′ such that
𝑃(𝑊)≥ 1−𝛿, 𝑄 (𝑊′)≥ 1−𝛿,
R𝛼(𝑃|𝑊∥𝑄|𝑊′)≤𝜌𝛼, and R𝛼(𝑄|𝑊′∥𝑃|𝑊)≤𝜌𝛼,
where for any𝛼 > 1, R𝛼(𝑈∥𝑉) := 1 𝛼−1 log ∫ 𝑈(𝑥)𝛼𝑉(𝑥)1−𝛼𝑑𝑥
denotes the𝛼-Rényi divergence between𝑈 and𝑉 .
All the proof techniques we applied for(𝜀,𝛿)-DP also extend to
hold for(𝜌,𝛿)-AzCDP. In particular, we have to rely on the privacy
filter𝜙𝜌,𝛿 for AzCDP that is defined similarly.
𝜙𝜌,𝛿((𝜌1,𝛿 1),..., (𝜌𝑛,𝛿𝑛)) :=
 

if
𝑛˝
𝑖=1
𝜌𝑖≤𝜌 &
𝑛˝
𝑖=1
𝛿𝑖≤𝛿
otherwise.
Lemma B.2 ([ 46]). For all 𝜌 ≥ 0 and𝛿 ∈ [0, 1], the universal
interactive mechanismM𝜙𝜌,𝛿 satisfies(𝜌,𝛿)-AzCDP.
AzCDP is useful in performing privacy accounting of the Gauss-
ian mechanism, where using standard(𝜀,𝛿)-DP notion results in
sub-optimal privacy guarantees under composition.
10(𝜌,𝛿)-AzCDP is referred to as𝛿-approximate𝜌-zCDP in [6].
396

On the Differential Privacy and Interactivity of Privacy Sandbox Reports Proceedings on Privacy Enhancing Technologies 2025(3)
Keyword Meaning
ad Advertisement shown on a publisher website.
ad-tech The entity that helps advertisers & publishers with placement and measurement of digital ads.
advertiser The entity that is paying for the advertisement, e.g. an online shoes shop.
aggregatable report An encrypted report that is sent to ad-tech every time a trigger is registered.
ARA Attribution Reporting API, that supports generation of summary reports and event level reports for
attributed conversions.
attribution A conversion is attributed to an impression if the ads system beleives that this conversion happened
due to this impression.
conversion An action on the advertiser website; for example, it could be a purchase.
impression An event where a user is exposed to some marketing information; for example, an ad is shown to the
user.
key discovery The functionality that allows ad-techs to get a summary report without passing a list of keys of interest.
PAA Private Aggregation API, that supports generation of summary reports, corresponding to cross-website
events.
publisher The entity that hosts the website that displays an advertisement, e.g. a news website.
requerying The functionality that allows ad-techs to process the same report multiple times using aggregation
service.
shared storage The API that allows persisting a cross-web key-storage with read access being restricted to preserve
privacy.
source The event on publisher website registered by the ad-tech with the browser; in typical use-cases, it
corresponds to an impression. ThesrcKey gets used in the generation of the aggregatable report for
any trigger that get attributed to this source.
summary report The report obtained as a result of aggregating aggregatable reports and adding noise to the result.
trigger The event on advertiser website registered by the ad-tech that makes the ARA Client generate an
aggregatable report; in typical use-cases it corresponds to conversions.
Table 2: Glossary of commonly used terminology regarding the Privacy Sandbox.
397
