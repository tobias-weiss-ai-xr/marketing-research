---
title: Expecting (Targeted Ads)? Network Analysis of User Health Data Leakage in Fertility Tracking Apps
url: https://arxiv.org/abs/2606.26276
category: privacy-data
subcategory: measurement
date: 2026-06
venue: arXiv (Cornell University)
authors:
- Yeeun Jo
- Shahanaasree Sivakumar
- Mahnoor Jameel
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.26276
pages: 9
chars: 46643
fetched_at: '2026-11-08T12:59:50+00:00'
kb_version: 1
---

# Expecting (Targeted Ads)? Network Analysis of User Health Data Leakage in Fertility Tracking Apps

Expecting (Targeted Ads)? Network Analysis of User
Health Data Leakage in Fertility Tracking Apps
Yeeun Jo, Shahanaasree Sivakumar, Mahnoor
Jameel, Camille Cobb, Adam Bates
{yeeunjo2,ss290,mjameel2,batesa,camillec}@illinois.edu
University of Illinois at Urbana-Champaign
Champaign, Illinois, USA
Brad Reaves
bgreaves@ncsu.edu
North Carolina Statae University
Raleigh, North Carolina, USA
Abstract
While human factors in the privacy of fertility tracking apps
– health trackers that record users’ menstrual or pregnancy
data – has been the subject of extensive study, little attention
has been paid to the technical aspects of apps’ data handling
practices. We conduct a network-based measurement study
of a corpus of 20 Android fertility tracking apps from the
Google Play Store, focusing on how user data is shared with
third party advertising services. After systematizing app fea-
tures, we conduct a series of standardized user interactions
across all apps in an environment that records TLS-stripped
network traffic. In a subset of apps (n=5) we identify explicit
leakage of user health data as well implicit leakage through
highly targeted contextual advertising URL’s. Equally im-
portantly, we observe additional apps that use an ad-based
monetization model without apparent leakage of user data, as
well as several apps the interact only minimally with ad ser-
vices. These findings provide technical grounding for wide-
spread user concerns, but also underscore the importance of
consumer choice in the privacy implications of app-based
fertility tracking.
1 Introduction
Fertility tracking apps enable users to take daily notes and
track premenstrual syndrome, pregnancy symptoms, moods,
intercourse, and period flow. While these apps have contin-
ued to grow in popularity since their introduction, the highly
sensitive and intimate information they collect has also been
a long-held source of concern (e.g., [ 1, 2]). In the United
States, these concerns were further amplified following the
Supreme Court’s 2022 Dobbs decision, overturning Roe v.
Wade (1973) and removing federal protections for abortion.
The digital privacy for fertility trackers is now a rich area
of research, but prior work exhibits a noticeable methodolog-
ical skew. On the one hand, numerous studies have examined
user’s perceptions and mental models of fertility tracking pri-
vacy, conducting interviews [3], surveys [4, 5], or examining
social network posts [6] to better understand how users rea-
soned about and managed privacy risks. On the other hand,
researchers have examined tracking vendors’ public state-
ments [7], privacy policies [8, 9]. Studies oriented around
users and policies constitute the majority of work in the
space, providing valuable insights into both users’ and ven-
dors’ attitudes and privacy management strategies in the
ecosystem.
However, technical analysis of fertility tracking apps’ ac-
tual data handling practices are underrepresented in the
literature. When software is addressed at all, prior work
has typically conducted surface-level analysis as a means
of grounding user- or policy-centered methods. Malki et al.
extend their policy analysis with a visual inspection of apps’
user interfaces [8]. Hudig et al. anchor their user survey by
profiling theencryptednetwork traffic of 8 apps [ 5]; however,
with encrypted traffic they are unable to confirm or char-
acterize the transmission of user data, instead establishing
a correlation between active device usage and the volume
of data transmission. Hassan et al. analyze Android permis-
sions and test apps for the presence of common third party
trackers [9], again extending a policy analysis methodol-
ogy. Taken as a whole, prior studies of fertility trackers are
limited in that they must speculate about how user privacy
mightbe violated through app usage, grounding speculation
through analysis of developer statements, privacy policies,
access control lists, etc.To advance this area of study, what is
required is technical ground truth – Do fertility trackers share
user health data with third parties, and if so how fine-grained
is the data being shared?
As a first step to answering this question, we conduct a
systematic analysis of fertility tracking apps’unencrypted
network transmissions to third party advertising networks.
On a corpus of 20 apps, we conduct a series of 8 interac-
tion sessions designed to exercise the common features of
tracking apps. These interactions were conducted in an emu-
lated Android environment instrumented withmitmproxy to
record TLS-stripped copies of network traffic. After filtering
the traffic captures for ad network domains, we catalog the
role and function of ad network API endpoints then manu-
ally review URL query parameters and HTML request bodies
for evidence of user health data leakage. All instances of
data leakage were then confirmed through manual review
arXiv:2606.26276v3  [cs.CR]  30 Jun 2026

Yeeun Jo, Shahanaasree Sivakumar, Mahnoor Jameel, Camille Cobb, Adam Bates and Brad Reaves
of decompiled app source code. We organize our findings
through the following high-level research questions.
RQ1: How do fertility trackers interact with advertis-
ing services?We identify interactions with 22 advertising
network services and characterize their role and prominence
within the fertility tracking ecosystem. We observe that preg-
nancy journaling is associated withat least 2.5 timesthe
volume of ad network activity when compared to other jour-
naling features. We go on to characterize this activity by
the specific role of API Endpoints, demonstrating a broad
continuum of ad-based monetization strategies.
RQ2: Does advertising network traffic contain user
health data?We analyze 108,534 URL query parameters and
50,088 key-value pairs from HTML request bodies from our
7,829 HTTP request dataset, searching for evidence of data
leakage. In total, we find that 5 of 20 apps (25%) leak sufficient
data for ad network’s to infer the user’s high-level interaction
patterns. In 2 apps, we find that finer-grained user health
data is leaked, including the user’s pregnancy and current
trimester, the age in weeks of the user’s child postpartum,
and the occurrence and approximate date of pregnancy loss.
We verify that these parameters were indeed populated with
user-provided data through manual review of decompiled
app source code. These patterns are observed in extremely
popular apps includingBaby Center,What To Expect,The
Bump, which on Google Play reported 10M+, 5M+, and 1M+
installs respectively at the time of our analysis.
We conclude by considering the implications of our re-
sults. While in some cases highly sensitive user health data
is leaked to ad networks, our findings also demonstrate a
spectrum of strategies for managing privacy and monetiza-
tion in the fertility tracking ecosystem. Notably, many apps
serve ads without apparent transmission of user health data
to ad networks, while some apps are observed to forego ads
altogether. Provided that they are informed, this variance
suggests the potential for users to engage in meaningful
decision making based on their privacy concerns and man-
agement strategies.
2 Data Collection
To explore the interconnection between advertising and
fertility privacy, we analyzed the network traffic emitted
by tracking apps during normal user interactions. Network
traces were collected in October 2025 at a Midwest city in
United States, from a representative selection of Android
apps from the Google Play store. The network traces were
generated by a human experimenter entering scripted se-
ries of inputs across all apps in eight interaction sessions.
Once the data was collected, we developed tooling to iden-
tify active ad networks in each app, recovered the purpose
and function of different Ad Network API endpoints, and
reviewed URL and JSON data sent by the app to the network.
We then compare our findings across apps. In this section,
we describe how we selected apps, structured the system
side for network data profiling, and conducted ad network
activity profiling.
2.1 App Selection
We primarily identified fertility apps through keywords searches
on the Google Play Store using the following phrases: “Pe-
riod Tracker, ” “Period Cycle”, “Fertility Tracker” “Ovulation
Tracker, ” and “Pregnancy Tracker & Calendar. ” Our searches
identified 254 total apps. We then considered the app for
inclusion in the study based on the following criteria:
• Provides features related to menstruation, fertility, preg-
nancy, or menopause.
• Accepts as input user data related to (in)fertility (e.g., pe-
riod cycles, pregnancy, symptoms).
• Includes calendar-based features, a proxy for self-tracking
functionality.
•Is a live service that is actively maintained.
We applied these criteria to filter from our consideration
apps that did not handle sensitive user data related to fer-
tility, and thus do not have the same privacy concerns as
fertility trackers. In addition to Google Play search results,
we included 4 additional apps: 1 app developed by a non-
profit organization (Euki); 1 app that appeared in a web
advertisement served to one of the authors claiming to be
a privacy-preserving period tracker (Stardust); and 2 apps
based on one of the authors’ prior experience with fertility
trackers.
In all, 258 fertility tracking apps were in our candidate set,
from which we selected 20 apps that represented a balanced
mix of app categories, developer types, and install count
estimates, ensuring coverage of both popular and niche ap-
plications. Our corpus of apps is shown in Table 4 in the
appendix.1 The Google Play reported number of installs in
our sample ranged between50and100 , 000, 000, while the
average user rating was 4.4. 17 apps used free-with-ads mon-
etization models, 1 app exclusively used in-app-purchases,
while 2 used a “freemium” model that supported either.
2.2 Interaction Procedure
Interaction sessions were designed around the core user
features of fertility tracking apps that were collecting user
data. We began by conducting affinity diagraming to orga-
nize the fertility tracking apps’ features into natural clusters
based on shared characteristics and emergent themes. This
1Several additional apps with 1M+ downloads (Flo, Clue, Ovia Cycle, and FF
App) were initially selected but were later excluded because they required
single-sign-on authentication that did not work in our analysis environment,
making them unusable.

Expecting (Targeted Ads)? Network Analysis of User Health Data Leakage in Fertility Tracking Apps
Interaction Session # Apps Data Types
Registration 13 Personal Identification, (Reproductive
State Indicators, Menstrual Activity )
Menstruation Journaling 16 Menstrual Activity, Physical Symptoms,
Emotional and Behavioral symptoms
Fertility Journaling 14 Hormonal or Cycle-specific Physiologi-
cal Indicators, Sexual and Relationship
Data
Sleep Journaling 15 Lifestyle and General Health
Contraceptions Journaling 13 Sexual and Relationship Data, Physical
Symptoms, Emotional and Behavioral
symptoms, and Medical data
Pregnancy Journaling 15 Sexual and Relationship Data, Reproduc-
tive State Indicators, Pregnancy Track-
ing, and Medical data
Postpartum Journaling 14 Physical Symptoms, Emotional and Be-
havioral symptoms, and Medical Records
Pregnancy Loss Journaling 15 Reproductive State Indicators, Physical
Symptoms, Emotional and Behavioral
symptoms
Table 1: Interaction Sessions used in Data Collection.
collaborative grouping process naturally revealed a hierar-
chical taxonomy, which we then formalized to categorize the
apps’ core functionalities. Leveraging this taxonomy, we de-
signed structured interaction sessions around representative
user personas. For example, interaction sessions involved
sequential inputs such as logging menstrual cycle start dates,
recording symptoms (e.g., period flows or cramps), and gen-
erating ovulation predictions. These actions simulated user
behavior to provoke ad network requests, which may contain
sensitive health data (e.g., cycle phase indicators) alongside
device identifiers. By specifying an interaction procedure for
each fertility tracking feature, the network traces become
easier to interpret and compare across apps. This also allows
us to control the information provided to the app and test
for its impact on the resulting ad network traffic. Resulted
interaction sessions are summarized in Table 1.
2.3 Network Profiling Apparatus
For each app, we download the Android APK files, then in-
stalled them in Android 11 in the Waydroid Emulator 1.5.1.
Waydroid was set to default configurations, except that the
environment was modified to intercept HTTPS traffic, strip
TLS, and record the packet captures to disk. Specifically, we
used a rootkit to escalate privilege in the operating system, in-
stalled a custom self-signed Certificate Authority (CA) certifi-
cate to Android’s certificate store, then deployed mitmproxy
with the new CA keypair.2
As this process was difficult to fully automate, we re-used
the same Waydroid environment for all apps. Unfortunately,
Waydroid does not offer a snapshot feature, which would
have allowed us to quickly reset the environment to a clean
state for each app. Instead, to minimize the risk of interfer-
ence, we force-stopped all apps in the Android settings prior
2Details at https://github.com/ddxv/mobile-network-traffic.
Adobe
Nimbus
Smaato
Tremor
Y andex
ByteDance
InMobi
PubMatic
SmartAdServer
Teads
Vungle
Smadex
AppLovin
Mintegral
BidEase
LiftOff
Magnite
Amazon
Moloco
Criteo
Meta
Google
0 5 10 15
Number of Apps
Service
Service Type Ad Network Buy−Side Data+Identity Integrated Sell−Side
Figure 1: Number of occurrences of each advertising
service in the dataset.
to interacting with the application of interest. Upon review
of the mitmproxy logs, we also confirmed that all network
traces originated from the application of interest and not
from other senders on the device.
2.4 Manual Code Review
To validate and deepen our understanding of the advertising-
related behaviors observed at the network level, we decom-
piled codes of each fertility tracking app. Using JADX de-
compiler, we decompiled the APKs and exported the recon-
structed source code as Java files for comprehensive manual
review. This process revealed direct correlations between
network payloads and specific code paths. In cases where
we detect sensitive data transmission to ad networks – such
as fertility metrics, user demographics, or device identifiers
– manual code was used to verify that these values were dy-
namically constructed based on user data. This dual network-
static validation approach eliminated false positives and pro-
vided actionable evidence of user data leakage patterns across
all analyzed apps, strengthening the causal linkage between
app features and advertising ecosystem interactions.
‘
3 How do fertility trackers interact with
advertising services?
From the network traffic dataset, we filter for domains at-
tributed to advertising services by appgoblin.info,3 a site
that monitors Android marketing and advertising analytics.
Service TypeA high-level summary of observed services,
by number of apps, can be found in Figure 1. We classify
each service by its function in the ecosystem:Ad Networks
intermediaries that aggregate and resell ad inventory (space),
Buy-Sideplatforms help advertisers purchase ad space,Data
3https://github.com/appgoblin-dev/

Yeeun Jo, Shahanaasree Sivakumar, Mahnoor Jameel, Camille Cobb, Adam Bates and Brad Reaves
Pregnancy Loss (n=16)
Postpartum (n=15)
Pregnancy (n=16)
Contraception (n=14)
Sleep (n=16)
Fertility (n=15)
Menstruation (n=17)
Registration (n=14)
0 1000 2000
HTTP Requests
Interaction
Service Type Ad Network Buy−Side Data+Identity Integrated Sell−Side
Figure 2: Number of HTTP Requests by interaction
session to different advertising network service types.
Endpoint Role Requests Perc.
Configuration 234 3%
Conversion Tracking 146 2%
Cookie Synchronization 60 1%
Event Tracking 257 3%
Get Ad 5,032 64%
Impression Tracking 1,022 13%
Static Content 979 13%
Unclear 99 1%
Table 2: Request distribution by API Endpoint Role
and Identitymeasurement platforms collect and unify con-
sumer information across different channels, andSell-Side
services help developers to automatically sell ad space and
mediate multiple ad networks competing. Most prevalent in
our data, verticallyIntegratedad networks may perform all
of these functions.
Figure 2 reports how these different services contributed
to network traffic in our dataset, grouped by interaction
session. Here, it can be seen that the vast majority of traffic is
sent to the major integrated ad platforms, which is consistent
with the app-service peering relationships reported in Figure
1. We also observe large differences in the volume of ad
traffic encountered in different interaction sessions – besides
registration, most sessions ranged from 692 to 1,035 requests,
but pregnancy interactions saw 2,663 requests. App counts
per interaction session, marked on the y-axis labels show
this increase is not explained by the pregnancy interaction
(𝑛= 15) being supported by more apps than other interactions
(𝑛=13-17).
API Endpoint Roles.Large number of HTTP requests to
ad services does not necessarily imply leakage of user halth
data. For example,many of these requests were for static con-
tent – no dynamic information is transmitted in the request.
Kindara
Stardust
Radhu Pregnancy
My Period Calendar
Mira
Preglife
Timskiy Pregnancy
Pregnancy +
Eveline
Clover
Pregnancy (duff hl studio)
My Calendar
Lily Tracker
GP Tracker
Ovyu
Amila Pregnancy
MIA
The Bump
BabyCenter
What to Expect
0 500 1000
HTTP Requests
Fertility Tracking App
API
Endpoint
Role
Configuration
Conversion Tracking
Cookie Synchronization
Event Tracking
Get Ad
Impression Tracking
Static Content
Unclear
Figure 3: Number of HTTP Requests by API Endpoint
Role issued by different Fertility Trackers.
To better characterize the privacy implications of this traffic,
we systematically categorized each of the 7,829 HTTP re-
quest by the function of the API Endpoint. To do so, we first
defined the endpoints of an API as the set of paths associated
with a domain that did not contain any dynamic or non-
deterministic content. Because dynamic content appeared
later on the URL path, we define an API endpoint as a domain
and path prefix pair. Of the resulting 196 endpoints, we then
reviewed public documentation and the request/response
pairs in our dataset to determine their high-level function
within the API. Using this strategy we were able to identify
a high-level role for 98.7% of API Endpoints, the distribution
for which are summarized in Table 2.
4 Does advertising network traffic contain
user health data?
Having documented the widespread practice of ad-based
monetization in the prior section, we continue by investi-
gating whether this ad traffic contains user-provided health
information as part of a targeted advertising strategy. Specif-
ically, we defineuser data leakageas any information that
would permit a bystander to learn something about the user
at a finer-granularity than the installation of the app itself.
As a guiding example from our data, a field containing the
URL https://www.whattoexpect.com is not data leakage,
as this domain is associated with any use ofWhat to Expect;
on the other hand, a field that references this domain with
the URL path /pregnancy/after-miscarriage, it is data
leakage because the bystander can infer that the user was
journaling about a pregnancy loss.
Our procedure was as follows. First, we split dynamic data
from our 7,829 HTTP requests into key-value pairs, resulting
in 108,534 tuples from URL query parameters and 50,088
from HTTP Request Body parameters. Two experimenters

Expecting (Targeted Ads)? Network Analysis of User Health Data Leakage in Fertility Tracking Apps
321216 52161 183 13
2
556 5 55 5
1412 63108 162 29
295225 27140 562 20
Kindara
Stardust
Radhu Pregnancy
My Period Calendar
Mira
Preglife
Timskiy Pregnancy
Pregnancy +
Eveline
Clover
Pregnancy (duff hl studio)
My Calendar
Lily Tracker
GP Tracker
Ovyu
Amila Pregnancy
MIA
The Bump
BabyCenter
What to Expect
Registration
Menstruation
Fertility
Sleep
Contraception
Pregnancy
Postpartum
Pregnancy Loss
Interaction
App
Requests
40
80
120
160
Figure 4: Number of HTTP Requests per App and Inter-
action session that were labeled as leaking user data.
then manually reviewed the contents of all fields for evidence
of data leakage. The process of labeling all fields was made
simpler by sorting by parameter key, allowing many tuples to
be labeled after reviewing a small handful. When key-value
pairs contained complex or non-human-readable data, we
attempted Base64 or URL decoding to interpret the value.
We also consulted available documentation and community
posts to interpret parameters that were not immediately
interpretable. Because of the opacity of ad network API’s,
as well as the potential for false negatives in our review
procedure, our analysis represents a conservative estimation
of leakage in the dataset. Inter-coder reliability and coder
disagreement procedures were not needed, as all explicit
leakage of user data is verified in Appendix A through review
of decompiled app source code.
4.1 Findings
Our findings are summarized by App and Interaction session
in Figure 4; this figure reports the number of HTTP requests
that were found to leak some form of user data. Examples
of data leakage are found in Table 3. Examining the specific
conditions of data leakage, we identify several broad patterns,
described below.
Explicit Leakage in Developer-Defined Parameters.
In this pattern, which was observed in the Google services on
Interaction Example Health Leakage Parameters
Registration us=precon,us=preg02,tri1
Menstruation appmode=ttc,csw=preg02,tri1,
sid=pregnancy-prep-for-moms-to-be,subcat=ovulation
Fertility cat=gettingpregnant,subcat=preppingforpregnancy,
contentidentifiers=conceptionbasics, preconceptiontests,
naturalfamilyplanning symptomsallkinds,
vaginalbleedingdischarge
Sleep No unique values, repeats other leakage parameters
Contraception topic=baby-products-health-and-safety
Pregnancy bage=33,cat=pregnancy,csw=preg02,tri1,
sid=checklist-packing-a-hospital-bag, registry,
spot=child-growth, isitsafe, birthprefs,
subtopic=pregnancy-weight-gain,tid=weight-gain
Postpartum appmode=baby,cat=firstyear,csw=post7m,child0yr,phase=
baby,sid=your-baby-week-1,subcat=monthbymonth
Pregnancy Loss subcat=pregnancyloss,wknum=17,us=null
Table 3: Example URL query parameters identified as
leaking user health data.
2 apps (What to Expect,BabyCenter), developers define cus-
tom parameters that explicitly correspond to user-provided
health information. Fields matching this pattern included us,
csw, appmode, bage, phase, and wknum. InBabyCenter, these
fields tracked the stage of the pregnancy (csw=preg02,tri1)
or the age of the newborn child ( csw=post7m_3w), which
was also possible inWhat to Expect( us=preg17,tri2, us=
post7m _3w,child0yr). Most concerningly, inWhat to Ex-
pecttwo parameters appear to explicitly signify pregnancy
loss – appmode was set to NULL only in the Pregnancy Loss
session, while wknum is set to 17 in this session but was
NULL in all other sessions, suggesting that the parameter is
tracks the week of pregnancy loss. To ensure that we did not
misinterpret these fields, we reviewed the decompiled app
source code that constructed these strings to confirm they
are constructed from user data.
Implicit Leakage in Developer-Defined Parameters.
While explicit leakage patterns were less common, we ob-
served implicit leakage through Google’s custom parame-
ters in 5 apps. Broadly, this data could be used to consis-
tently infer how the user was interacting with the app, but
typically nothing else. Some parameters in this category
stored extremely coarse-grained user health information,
e.g., appmode=ttc (trying to conceive) in Fertility journaling.
More often, these fields corresponded to developer-defined
usage themes, e.g.,The Bumpdefines a content carousel con-
trolled by thesid field with values such aspregnancy-prep-
for-moms-to-be. In the minimal leakage case,Pregnancy +
statically setGAMAudience to GAMAudience_MaternalHealth
_Emotional in all interaction sessions, suggesting a partially
implement targeted advertising strategy.
Explicit/Implicit Leakage in Contextual Ad URLs.
We found that contextual ad URLs – which are intended
to enable targeted advertising without sharing user infor-
mation – regularly leaked user data in requests to Google
and Amazon. This pattern is observed inWhat To Expect,

Yeeun Jo, Shahanaasree Sivakumar, Mahnoor Jameel, Camille Cobb, Adam Bates and Brad Reaves
BabyCenter,The Bump, andGP Tracker,Pregnancy +. Most
often this leakage was implicit and could be used to infer the
interaction session. For example, theBabyCenterapp links to
babycenter.com’s ovulation-calculator in the fertility
session, birth-class in the Pregnancy Session, teaching-
yourbabyandtoddlertosleep in the Postpartum session,
and grief-loss in the Pregnancy Loss session. In some
cases, however, these contextual URL’s were so scoped that
they constituted explicit data leakage. For example, contex-
tual ads inWhat to Expectrepeated the same fine-grained
pregnancy information, e.g., month-by-month/month-7 in
the Pregnancy session.
Implicit Leakage in Ad Inventory Heirarchies.We
identify a final pattern inThe Bump, which implicitly leaks
user interactions in the way they organized their available ad
space. Following an OpenRTB standard [10], ad requests to
Amazon contain references to ad “slots” like/4879/Tri1.n_
TB/tools#m-top-input where 4879 is a developer account
ID, Tri1.n_TB is a collection of related content,tool is a spe-
cific page or activity, andm-top-input is a specific DOM ele-
ment ID. Requests for ads in the Pregnancy, Postpartum, and
Menstruation interactions reference the Tri[1,2,3].n_TB,
Postnatal.n_TB, andTTC.n_TB collections, respectively How-
ever, this signal is less reliable than other implicit leakage due
to pre-emptive fetching of many ads that are never displayed.
For example, we see referenes to Tri1, Tri2, and Tri3 ad
inventory even though our Pregnancy interaction described
a first trimester pregnancy. This suggests the app proactively
fetches ads for many pages that are never visited, a common
practice that is resolved through impression tracking and
mediation mechanisms.
5 Discussion & Conclusion
Confirming widely held concerns about the privacy implica-
tions of fertility tracking apps, we document two instances
of user health data being explicitly transmitted to third party
advertising services. In addition, we identify several design
patterns through which coarser-grained knowledge about
users’ app interactions is implicitly leaked. While we are
confident in the correctness of our results, the nature of
our study design assures that our estimates of user health
data leakage are conservative. Several of the most popular
fertility tracking apps were excluded from our study due
to incompatibility with our HTTPS proxy. Further, because
our analysis depended on identifying human-interpretable
strings in outbound HTTP traffic, any level of data encoding
would lead to a false negative. Some apps for which we did
not find evidence of data leakage may have indeed be trans-
mitting user health data without the presence of conspicuous
substrings like “preg, ” “tri, ” “ttc, ” etc. Acknowledgment of
this limitation underscores the overtness of the uncovered
privacy violations. Further, even the most naïve standardiza-
tion of these custom parameters values would measurably
improve user privacy, complicating attempts by third parties
to make inferences about the fields’ meanings.
Regardless of whether we identified all instances of data
leakage in this app corpus, our findings sketch a richer con-
tinuum of monetization strategies in the fertility tracking
ecosystem. In addition to membership-based services that
allow users to opt-out of ads, there appears to be a thriv-
ing plurality of apps that conduct ad-based monetization
without extensive targeting based on user data. Even among
the 5 apps for which we find to engage in targeted advertis-
ing, important distinctions exist. Some perform contextual
targeting that implicitly leaks minimal data about user inter-
actions, or organize their ad inventory in such a way that
those interactions can be inferred. In the most extreme cases,
apps aggressively targeted based on highly-sensitive user
health inputs.
The high degree of variance in the monetization strategies
of fertility tracking apps should be viewed as an opportu-
nity for user privacy. Consumer choice – which apps a user
chooses to install – could be associated with dramatically
different privacy outcomes within this ecosystem. Further,
there appear to exist highly accessible ad-based trackers that
generate revenue without user targeting. The difficult task,
of course, is communicating to users these data handling
practices and the potential tradeoffs between apps, empow-
ering them to make informed choices. Our work is a first
step towards documenting these practices and tradeoffs at
a technical level; we are fortunate that fertility tracking is
already a rich area of study in the usable privacy commu-
nity, assuring there will be experts to investigate effective
methods of translating this knowledge to users. Additional
steps in future work include approaching data leakage as a
software analysis problem, which could be conducted using
information flow analysis techniques (e.g., [11]). Our findings
illuminate the breadth of implicit control flow patterns that
would need to be accounted for in order for these approaches
to be effective.
In this work, we have conducted (to our knowledge) the
first systematic study of how advertising informs the privacy
of fertility tracking app usage. Confirming widespread con-
cerns that sensitive health data could be shared with third
parties, we uncover several patterns through which user
data can be explicitly or implicitly leaked to advertising net-
works. Our network-based approach to the matter enabled
us to quickly identify instances of data leakage, but could not
holistically identify all sensitive data transmissions. We thus
view our work as a first step towards a more comprehensive
understanding of privacy in the fertility tracking ecosystem.

Expecting (Targeted Ads)? Network Analysis of User Health Data Leakage in Fertility Tracking Apps
Acknowledgements
We thank James O’Claire (AppGoblin) for open-sourcing his
tools, helping us configure the network profiling environ-
ment, and meeting with us to share his insights into the
Android advertising ecosystem. This work was generously
funded, in part, by the SPLICE research program, supported
by a collaborative award from the National Science Foun-
dation (NSF) SaTC Frontiers program under award number
1955228.
References
[1] N. Felizi and J. Varon, “Menstruapps - how to turn your period
into money (for others), ” https://chupadados .codingrights.org/en/
menstruapps-como-transformar-sua-menstruacao-em-dinheiro-
para-os-outros-2/, 2017.
[2] V. Rizk and D. Othman, “Quantifying fertility and reproduction
through mobile apps: a critical overview.”Arrow for Change, vol. 22, p.
13–21, 2016.
[3] N. Mcdonald and N. Andalibi, ““i did watch ‘the handmaid’s tale”:
Threat modeling privacy post-roe in the united states, ”ACM Transac-
tions on Computer-Human Interaction, vol. 30, no. 4, pp. 1–34, 2023.
[4] J. Cao, H. Laabadli, C. H. Mathis, R. D. Stern, and P. Emami-Naeini, ““i
deleted it after the overturn of roe v. wade”: Understanding women’s
privacy concerns toward period-tracking apps in the post roe v. wade
era, ” inProceedings of the 2024 CHI Conference on Human Factors in
Computing Systems, 2024, pp. 1–22.
[5] A. I. Hudig and J. Singh, “Intimate data sharing: Enhancing trans-
parency and control in fertility tracking, ” inProceedings of the 2025
CHI Conference on Human Factors in Computing Systems, 2025, pp.
1–24.
[6] Q. Song, R. Ma, Y. Kou, and X. Gui, “Collective privacy sensemaking
on social media about period and fertility tracking post roe v. wade, ”
Proceedings of the ACM on human-computer interaction, vol. 8, no.
CSCW1, pp. 1–35, 2024.
[7] Q. Song, R. H. Hernandez, Y. Kou, and X. Gui, ““our users’ privacy is
paramount to us”: A discourse analysis of how period and fertility
tracking app companies address the roe v wade overturn, ” inPro-
ceedings of the 2024 CHI Conference on Human Factors in Computing
Systems, 2024, pp. 1–21.
[8] L. M. Malki, I. Kaleva, D. Patel, M. Warner, and R. Abu-Salma, “Explor-
ing privacy practices of female mhealth apps in a post-roe world, ” in
Proceedings of the 2024 CHI Conference on Human Factors in Computing
Systems, 2024, pp. 1–24.
[9] M. Hassan, M. Jameel, T. Wang, and M. Bashir, “Unveiling privacy
and security gaps in female health apps, ” 2025. [Online]. Available:
https://arxiv.org/abs/2502.02749
[10] G. D. Documentation, “OpenRTB Integration, ” 2026. [Online]. Avail-
able: https://developers.google.com/authorized-buyers/rtb/openrtb-
guide
[11] W. Enck, P. Gilbert, B.-G. Chun, L. P. Cox, J. Jung, P. McDaniel, and
A. N. Sheth, “TaintDroid: An Information-flow Tracking System for
Realtime Privacy Monitoring on Smartphones, ” inProceedings of the 9th
USENIX Symposium on Operating Systems Design and Implementation,
ser. OSDI’10, Oct. 2010.
[12] L. Cohen and H. Hongo, “The Government Uses Targeted Advertising
to Track Your Location. Here’s What We Need to Do.” 2026.
[Online]. Available: https://www.eff.org/deeplinks/2026/03/targeted-
advertising-gives-your-location-government-just-ask-cbp
[13] Mozilla Foundation, “*Privacy Not Included: Reproductive Health, ”
2026. [Online]. Available: https://www .mozillafoundation.org/en/
privacynotincluded/categories/period-ovulation-trackers/
A Explicit Data Leakage Source Code
Verification
To verify that suspicious query parameters explicitly leaked
user health data, we conducted manual review of decompiled
app source code. Foreknowledge of the specific (sub)strings
of interest in the network data greatly simplified this review.
We omit detailed verification of the implicit leakage patterns
for brevity and because they largely self-evident given their
correlation with specific interaction sessions.
A.1 BabyCenter
The getAdsUserStage found incom.babycenter.pregbaby.
api.model.ChildViewModel is responsible for populating
the csw and us. As the APK retained function names, the
significance of the lines of code are relatively easy to discern.
Line 5, 8, and 11 delineate stage building for the trying-to-
conceive, pregnancy, and postpartum stages, respectively.
We can see in Line 11 that the postpartum stage is inferred
by the stage name reaching 11 months (11m) and 3 weeks
(3w) of pregnancy. The strings constructed in lines 9 and
17 correspond to the values we see in the pregnancy and
postpartum interaction sessions, respectively.
A.2 What to Expect
We are also able to easily identify the functions responsible
for constructing suspicious query parameters inWhat to
Expect. Once again, the combination of string literals and
function names provides strong evidence that these values
are being constructed based on dynamic user inputs.
Notably absent from the AdManager code is is explicit
logic for constructing custom parameters related to preg-
nancy loss. A more careful review of code suggests that this
data leakage was inadvertent on the part ofWhat to Expect.
We do not provide a code snippet here due to large volume
of source code across multiple files, but describe the control
flow path below: AdManager also contains a buildState
function that, among other things passes along the value
that eventually initializes the wknum field that signalled the
pregnancy loss in our network analysis. This function also
contains a switch statement that sets the value for appmode
by checking if a function argument is 2 (“no pregnancy”),
3 (“healing”), 4 (“ttc”), 5 (“pregnancy”), 6 or 7 (“baby”), oth-
erwise it defaults to NULL. We traced this input value back
through the main app logic, whose functions lacked symbol
names in the APK. Here, a similar function checks the same
variable but includes a case for 8 (“CHILD_HARD_STOP”),
which we believe to be associated with the pregnancy loss

Yeeun Jo, Shahanaasree Sivakumar, Mahnoor Jameel, Camille Cobb, Adam Bates and Brad Reaves
1p u b l i cS t r i n g g e t A d s U s e r S t a g e ( StageDay stageDay ) {
2i f( stageDay ==n u l l) {
3r e t u r n" " ;
4}
5i f( stageDay . i s S t a g e T t c ( ) ) {
6r e t u r nC o n s t a n t s . PRECON_PHASE ;
7}
8i f( stageDay . i s S t a g e P r e g ( ) ) {
9r e t u r nstageDay . getStageName ( ) + " , " +
↩→a d d T r i m e s t e r ( stageDay ) ;
10}
11i f( stageDay . getStageName ( ) . e q u a l s ( " post11m_3w " ) )
↩→{
12i n t[ ] i A r r D a t e D i f f I n t l = StageMapperHelper .
↩→d a t e D i f f I n t l (t h i s. mBirthDate ,
↩→BCDateTimeFormatUtil .
↩→g e t S t o r a g e D a t e S t r i n g (newDate ( ) ) ) ;
13i f( i A r r D a t e D i f f I n t l [ 0 ] ! = 0 ) {
14i n ti 2 = ( i A r r D a t e D i f f I n t l [ 0 ]∗1 2 ) +
↩→i A r r D a t e D i f f I n t l [ 1 ] ;
15i n ti 3 = i A r r D a t e D i f f I n t l [ 2 ] ;
16i n ti 4 = i A r r D a t e D i f f I n t l [ 0 ] ;
17r e t u r ni 3 == 0 ? S t r i n g . f o r m a t ( L o c a l e . US ,
↩→" p o s t %1$dm , c h i l d %2 $dyr " , I n t e g e r
↩→. v a l u e O f ( i 2 ) , I n t e g e r . v a l u e O f ( i 4 )
↩→) : S t r i n g . f o r m a t ( L o c a l e . US , "
↩→p o s t %1$dm_%2$dw , c h i l d %3 $dyr " ,
↩→I n t e g e r . v a l u e O f ( i 2 ) , I n t e g e r .
↩→v a l u e O f ( i 3 ) , I n t e g e r . v a l u e O f ( i 4 ) )
↩→;
18}
19}
20r e t u r nstageDay . getStageName ( ) ;
21}
Figure 5: InBabyCenter, the
getAdsUserStage function in
com.babycenter.pregbaby.api.model.ChildViewModel
populates thecswanduscustom parameters.
journaling feature. Setting case 8 to NULL may have been
an attempt to avoid transmitting pregnancy loss to the ad
network. However, since there appear to be few interaction
paths where appmode=NULL, the pregnancy loss is implicitly
leaked. Further, back in buildState, the string for wknum is
passed on regardless of the result of the switch statement.
As this value is (presumably) not updated again following a
pregnancy loss, the approximate date of the pregnancy loss
is passed to the ad network.
B Ethics
Justification for Research.This work is motivated by eth-
ical concerns surrounding the aggregation and sharing of
fertility data. Prior work has helped to document the wide-
spread public concern regarding the privacy policies of fer-
tility trackers, including the risk of data access by law en-
forcement (e.g., [4]). However, to our knowledge there has
been no study that attempts to assess the prevalence of such
data sharing on a technical level. Due to recent confirmation
1p u b l i c s t a t i cS t r i n g b u i l d C o n t e n t S t a g e B a b y (i n ti3 ,i n ti 4
↩→) {
2i n ti 5 = i 3 / 1 2 ;
3i f( i 3 > 2 ) {
4i 4 = Math . min ( i4 , 3 ) ;
5}
6r e t u r ng e t S t a g e V a l u e F o r B a b y ( i3 , i4 , i5 ,t r u e) ;
7}
8p u b l i c s t a t i cS t r i n g b u i l d C o n t e n t S t a g e B a b y J u s t M o n t h (i n t
↩→i3 ,i n ti 4 ) {
9i f( i 3 > 2 ) {
10i 4 = Math . min ( i4 , 3 ) ;
11}
12r e t u r nA b s t r a c t C 1 9 3 4 a . k ( " p o s t " , i 3 >= 2 ? a n d r o i d x .
↩→c o n c u r r e n t . f u t u r e s . a . g ( i3 , "m" ) : " " , i 4 > 0
↩→? i 3 < 2 ? a n d r o i d x . c o n c u r r e n t . f u t u r e s . a . g ( i4
↩→, "w" ) : a n d r o i d x . c o n c u r r e n t . f u t u r e s . a . h ( i4 ,
↩→" _ " , "w" ) : i 3 < 2 ? a n d r o i d x . c o n c u r r e n t .
↩→f u t u r e s . a . g ( i4 , "w" ) : " " ) ;
13}
14p u b l i c s t a t i cS t r i n g b u i l d C o n t e n t S t a g e P r e g n a n c y (i n ti 3 ) {
15r e t u r n" preg " + fixWeek ( i 3 ) + " , t r i " + P . b ( i 3 ) ;
16}
17p u b l i c s t a t i cS t r i n g
↩→b u i l d C o n t e n t S t a g e P r e g n a n c y N o T r i m e s t e r (i n ti 3 ) {
18r e t u r n" preg " + fixWeek ( i 3 ) ;
19}
20p u b l i c s t a t i cS t r i n g b u i l d C o n t e n t S t a g e T r y i n g T o C o n c e i v e ( )
↩→{
21r e t u r n" precon " ;
22}
23p r i v a t e s t a t i cS t r i n g g e t S t a g e V a l u e F o r B a b y (i n ti3 ,i n ti4
↩→,i n ti5 ,booleanz10 ) {
24S t r i n g st rH = i 4 > 0 ? ( i 3 >= 2 | | ! z10 ) ? a n d r o i d x .
↩→c o n c u r r e n t . f u t u r e s . a . h ( i4 , " _ " , "w" ) :
↩→a n d r o i d x . c o n c u r r e n t . f u t u r e s . a . g ( i4 , "w" ) : (
↩→i 3 >= 2 | | ! z10 ) ? " " : a n d r o i d x . c o n c u r r e n t .
↩→f u t u r e s . a . g ( i4 , "w" ) ;
25S t r i n g s t r G = ( i 3 >= 2 | | ! z10 ) ? a n d r o i d x . c o n c u r r e n t
↩→. f u t u r e s . a . g ( i3 , "m" ) : " " ;
26i f( i 3 ! = 0 && i 3 % 12 == 0 ) {
27i5− −;
28}
29r e t u r n" p o s t " + s t r G + st rH + " , c h i l d " + i 5 + " yr " ;
30}
Figure 6: InWhat to Expect, numerous functions in
app/src/main/java/com/whattoexpect/ad/AdManager
support the construction of query parameters that
leak user health data.
of federal law enforcement agencies using real-time bidding
markets as a means of sourcing surveillance data [12], the
user data that fertility tracking apps transmit to advertising
services is highly relevant to this broader societal concern
and thus worthy of study.
Stakeholder Analysis.This ecosystem is comprised of
three primary stakeholders: (1)Usersof fertility tracking
apps that generate health data, (2)Developersof those apps
that determine how that data is managed and shared, and
(3)Advertising Servicesthat developers establish business
relationships with in order to monetize the app.

Expecting (Targeted Ads)? Network Analysis of User Health Data Leakage in Fertility Tracking Apps
App Title App ID App Modes Revenue Model Installs Dev. Name Headquarters
Clover com.wachanga.womancalendar Hybrid FREE w/ ADS 5M+ Wachanga Limassol, Cyprus
Stardust com.stardust.app Hybrid FREE w/ ADS 500K+ Stardust App Inc. New York, NY, USA
My Calendar com.popularapp.periodcalendar Period FREE w/ ADS 100M+ Simple Design Ltd Tortola, United Kingdom
My Period Calendar com.lbrc.PeriodCalendar Period IAP 10M+ SimpleInnovation Redmond, WA, USA
Lily Tracker com.smsrobot.period Period FREE w/ ADS 10M+ SMSROBOT LTD Dublin, Ireland
GP Tracker com.period.tracker.lite Period FREEMIUM 10M+ GP International LLC Los Angeles, CA, USA
MIA com.azarou.aventure.spoonge.run Period FREE w/ ADS 1K+ octave
BabyCenter com.babycenter.pregnancytracker Pregnancy FREE w/ ADS 10M+ BabyCenter New York New York, USA
Pregnancy + com.hp.pregnancy.lite Pregnancy FREE w/ ADS 50M+ Philips Digital UK Noord-Holland-Amsterdam, Netherlands
Amila Pregnancy com.easymobs.pregnancy Pregnancy FREEMIUM 5M+ Amila Paphos, Cyprus
What to Expect com.wte.view Pregnancy FREE w/ ADS 5M+ What to Expect New York, NY, USA
Pregnancy (duff hl studio) com.women.pregnancytrackerapp22 Pregnancy FREE w/ ADS 5M+ duff hl studio
Preglife com.gravid.gravid Pregnancy FREE w/ ADS 1M+ Preglife
The Bump com.xogrp.thebump Pregnancy FREE w/ ADS 1M+ The Bump Chevy Chase, MD, USA
Timskiy Pregnancy com.timskiy.pregnancy Pregnancy FREE w/ ADS 1M+ Timskiy
Ovyu com.ishitechnolabs.ovyu Pregnancy FREE w/ ADS 1K+ Ishi Technolabs Gujarat Surat, India
Radhu Pregnancy com.radhu.pregnancytracker Pregnancy FREE w/ ADS 50+ Radhu
Eveline com.ixensor.lh TTC FREE w/ ADS 100K+ iXensor Co. Ltd. Taipei City, Taiwan
Kindara com.kindara.pgap TTC FREE w/ ADS 100K+ Kindara, Inc. Boulder, Colorado , USA
Mira mira.fertilitytracker.android_us TTC FREE w/ ADS 50K+ Quanovate Tech Inc Pleasanton , CA, USA
Table 4: Fertility Tracking Mobile Apps and Developer Company Headquarters. Revenue models: HARDPAY
use required hardware purchase; FREE w/ ADS monetizes exclusively on ad revenue. IAP uses in-app purchases.
FREEMIUM uses both ads and in-app purchases.
Potential Impacts.Our work has potential positive im-
pacts, specifically for users, who may become more informed
about the privacy implications of using different apps, al-
lowing them to choose apps whose data handling practices
are more aligned with their privacy concerns. Informed con-
sumer choice could lead to positive incentive structures for
apps to adopt more privacy-preserving data sharing practices.
This argument is consistent with the Mozilla Foundation’s
Privacy Not Includedproject, which includes recommenda-
tions on reproductive health apps [13]. We plan to share our
findings with Mozilla and other privacy advocacy groups
following submission. We also plan to notifyWhat to Expect
of the apparent inadvertent disclosure of pregnancy loss in
their AdManager class. Our work will also benefit the privacy
research community through the open sourcing of our data
and analysis code following publication.
On the other hand, our work may have potential negative
impacts for some app developers. To our knowledge our anal-
ysis did not violate the terms of service of these applications
– we did not modify the app and installing HTTPS proxies
is a common organizational security practice – nonetheless
developers may be surprised to discover we were able to
review their HTTPS requests to ad networks. For apps that
were shown to engage in highly targeted advertising based
on transmission of user health data, the developers may face
financial consequences for the publication of this work, how-
ever unlikely. We feel that in both cases the risks of negative
impacts are outweighed by the potential public good of dis-
seminating these findings, especially in the latter case where
the negative impact to one developer may be offset by a pos-
itive impact to another developer that can offer users greater
privacy.
Mitigations.Our study is observational in nature; it does
not propose a new defense nor provide instructions for
launching a new attack. An attacker could potentially lever-
age knowledge of this documented data leakage to surveil a
targeted user by conducting their own man-in-the-middle
attack on the user’s device. However, we find this risk eso-
teric and unlikely, as an attacker in a position to launch such
an attack would have more direct means of surveilling the
user. Therefore, we pursue no mitigation beyond disseminat-
ing our results with concerned parties and advocacy groups,
which we plan to undertake following submission.
