---
title: 'SoK: Advances and Open Problems in Web Tracking'
url: https://arxiv.org/abs/2506.14057
category: digital-marketing
subcategory: empirical
date: 2025-06
venue: ''
authors: []
source: arxiv
pdf_url: https://arxiv.org/pdf/2506.14057
pages: 43
chars: 203907
fetched_at: '2026-11-08T13:18:48+00:00'
kb_version: 1
---

# SoK: Advances and Open Problems in Web Tracking

SoK: Advances and Open Problems in Web Tracking
Yash Vekaria⋆
 ,Yohan Beugin ⋆
 ,Shaoor Munir
 ,Gunes Acar
 ,Nataliia Bielova
 ,
Steven Englehardt †,Umar Iqbal
 ,Alexandros Kapravelos
 ,Pierre Laperdrix
 ,
Nick Nikiforakis
 ,Jason Polakis
 ,Franziska Roesner
 ,Zubair Shafiq
 ,Sebastian Zimmeck
University of California, Davis, USA
 University of Wisconsin–Madison, USA
 Radboud University, Netherlands
Inria Centre at Université Côte d’Azur, France † Independent Researcher, USA
 Washington University in St. Louis, USA
North Carolina State University, USA
 Centre National de la Recherche Scientifique, France
 Stony Brook University, USA
University of Illinois Chicago, USA
 University of Washington, USA
 Wesleyan University, USA
Abstract
Web tracking is a pervasive and opaque practice that enables
personalized advertising, retargeting, and conversion tracking.
Over time, it has evolved into a sophisticated and invasive
ecosystem, employing increasingly complex techniques to
monitor and profile users across the web. The research com-
munity has a long track record of analyzing new web track-
ing techniques, designing and evaluating the effectiveness of
countermeasures, and assessing compliance with privacy reg-
ulations. Despite a substantial body of work on web tracking,
the literature remains fragmented across distinctly scoped
studies, making it difficult to identify overarching trends, con-
nect new but related techniques, and identify research gaps
in the field. Today, web tracking is undergoing a transforma-
tion, driven by fundamental shifts in the advertising industry,
the adoption of anti-tracking countermeasures by browsers,
and the growing enforcement of emerging privacy regulations.
This Systematization of Knowledge (SoK) aims to consolidate
and synthesize this wide-ranging research, offering a com-
prehensive overview of the technical mechanisms, counter-
measures, and regulations that shape the modern and rapidly
evolving web tracking landscape. This SoK also highlights
open challenges and outlines directions for future research.
1 Introduction
Users access a variety of free content and services on the web,
which are largely funded through online advertising. In turn,
advertising is heavily dependent on monitoring users’ online
activities for various purposes such as analytics, (re)targeting,
and conversion tracking. To realize these objectives, user
tracking has become a pervasive part of the web—today, 92%
of webpages embed at least one third-party tracker [294].
Over the years, researchers have conducted numerous stud-
ies to examine the evolution of web tracking mechanisms,
⋆Equal contribution.
An extended and living version of this document is available at
https://github.com/privacysandstorm/sok-advances-open-
problems-web-tracking
browser developments, and regulatory compliance. However,
despite a considerable body of work, major findings remain
scattered across many disparate studies, and existing survey
papers have either been too high-level [84], too narrowly-
focused on specific forms of web tracking such as caching
and browser fingerprinting [42, 155], or are not current with
modern techniques anymore [188]. Furthermore, as privacy
defenses improve in browsers, trackers continually adapt with
new evasion techniques [209, 303]. The result is an ever-
shifting technical landscape of tracking techniques.
Regulations often govern tracking practices and although
regulatory changes have had a more gradual impact than
browser-based technical interventions, together they have con-
tinued to reshape the ecosystem. Today, web tracking is un-
dergoing a transformative change due to the introduction of
privacy-enhancing protections in major web browsers, new ad-
vertising paradigms that do not rely on cross-site tracking, and
evolving regulatory frameworks [50, 108]. These shifts call
for a comprehensive study of emerging trends in the evolving
tracking landscape to identify crucial research gaps.
To this end, we synthesize disparate lines of research and
practices in web tracking—spanning across technical mecha-
nisms, mitigations, and regulatory changes—to systematically
provide an overview of the current state of web tracking. We
scope this SoK to how the data iscollectedabout users, not
how that data might then beused. This unified perspective
enables a critical reflection on how far the community has
come and which research directions it should prioritize. Our
main contributions are as following:
• We systematize the extensive body of research on web
tracking, providing a consolidated knowledge base of ad-
vances, highlighting evolving trends, and bridging emerg-
ing but related tracking mechanisms.
• We systematically organize anti-tracking interventions
proposed by researchers, major browser providers, and
community as well as relevant regulatory and compli-
ance actions across the EU and the US to assess how
they have altered the ecosystem over the years.
1
arXiv:2506.14057v2  [cs.CR]  16 Sep 2026

• We identify key open challenges and promising future
research directions in web tracking.
2 Background & Prior Work
Browser’s Security Model: Context-Origin Boundaries.
The browser’s context model denotes that every document
runs in a container that maintains its state (e.g., DOM, vari-
ables, scripts) separate from others, while the origin model
associates the document with an origin determining the code’s
privileges. Thus, the browser uses both the origin and con-
text to enforce policies—it isolates contexts from each other,
and when an interaction is attempted, it checks the origins
involved. Under theSame-Origin Policy (SOP)[190], two
contexts can interact freely only if they share the same origin.
Entities (Figure 1).Theuseris an individual accessing web-
sites on the internet through their browser (also known as user
agent [194]), seeking to keep their online behavior private.
Thebrowsermediates all interactions between the user and
the web content, enforcing context-origin policies. Thefirst-
party websiteis the webpage that the user directly browses
for content. It often includes resources fromthird-parties, i.e.,
hosted on a different domain than the first-party website [189].
Partitioned
Browser Storage
tracker1.com
tracker2.com
sports.com
news.com
first-party third-party
 https://www.news.com
news.com <mainframe>
tracker1.com <iframe>
tracker2.com <iframe>
tracker1.com
news.com
tracker2.com
news.com
sports.com
Server-to-Server
Sharing
 https://www.sports.com
sports.com <mainframe>
tracker2.com <iframe>
user@example.com
user@example.com
203.0.113.0/24
Tracking
Servers
User
Devices
Figure 1: Conceptual overview of our threat model where
news.com and sports.com are the first-party websites
visited by the user from their personal device(s) and
tracker1.comandtracker2.comembedded third-parties.
Adversary Goals.A tracker is any party whose goal is to
collect user’s data in order to profile or identify the user’s
behavior across one site (same-site tracking), several sites
(cross-site tracking), across contexts (cross-context tracking)
on a given device or across devices. Besides, a secondary goal
may be to avoid detection and anti-tracking measures.
Adversary Capabilities.Inclusion I .A first-party tracker is
assumed to directly monitor user activities within the top-level
browsing context. A third-party tracker could be embedded
as an inline resource (e.g., image/script tag) within the main-
frame by the first-party assuming trust delegation, an iframe
with a separate context under its origin, or as a resource within
a third-party iframe.Execution E .A tracker aims to collect
user data through available browser features within the con-
text where it is embedded. A script’s execution privileges
are tied to its context’s origin—implying that it always “acts
as” whatever origin its document has. By including external
scripts, the webpage implicitly declares that it trusts that code
with its own origin’s privileges [305].Storage T .Trackers
may also read, write, or modify data in the user’s browser stor-
ages, which are partitioned by origin, as well as the cookie jar,
which is scoped by domain (and path) rather than the full ori-
gin. Stored data can be accessed by the tracker in subsequent
visits to either the same site or a different site. Scripts from
one origin cannot read or write to another origin’s storage.
Because cookies are not origin-partitioned, third-party scripts
included in the main execution context can read and write
first-party cookies.Sharing S .To share collected data with
its own servers or a partner’s, trackers can initiate network
requests including the user data in one of four ways: (1) as a
URL query parameter, (2) request payload, (3) request header,
or (4) through HTTP cookies.Observation O .A tracker
present outside the browser can also passively observe and
analyze network traffic from the user’s browser or device.
Related Systematization Work.Over the years, the web
tracking community has produced a considerable amount of
findings. Unfortunately, these have largely remained scattered
across disjoint works making it difficult to draw connections
between related techniques, assess the state of the field, and
identify future research directions. Our SoK addresses these
by providing the most recent, systematic, and unified view
of the evolution of all known tracking techniques and their
research-, industry-, and community-based defense mecha-
nisms in parallel to major EU and US regulatory and com-
pliance changes. Prior survey and SoK papers in the space
(see comparison overview in Table 1) have only partially cov-
ered such aspects; being too high-level [42, 84], too narrowly-
focused on specific tracking mechanisms [155, 240], research
measurement methodologies [238, 270], or regulations ex-
clusively [31], or too old and outdated by newer techniques,
defenses, and policies that appeared in recent years [188,247].
3 Methodology
Literature Review.To systematize the evolution of web track-
ing, we perform a literature search (see Figure 2) to identify
all relevant papers published at any of the following seven
venues—IEEE S&P, USENIX Security, ACM CCS, NDSS,
ACM IMC, PETS, and WWW—since their creation (i.e., from
2

Table 1: Comparison overview to prior SoK and survey papers related to web tracking.
 : Cookie-based,
 : Navigational,
: Fingerprinting,
 : JavaScript-based,
 : Side-channels,
 : Privacy proposals. : Partial coverage compared to our SoK.
Tracking Defenses
Work Year Scope
Stateful
Stateless
MixedTechniques
Industry
Research
CommunityRegulations
Future
Directions
Nb Papers
Studied
Mayer et al. [188] 2012 Third-party tracking and policy
 EU & US✗≈65
Bujlow et al. [42] 2017 Tracking techniques and defenses
 EU (briefly)✓≈70
Sanchez-Rola et al. [247] 2017 Techniques and countermeasures
 EU & US✗≈35
Ermakova et al. [84] 2018 High-level tracking survey
 ✗ ✗31
Laperdrix et al. [155] 2020 Browser fingerprinting
 EU (briefly)✓≈57
Rokicki et al. [240] 2021 JS timers-based attacks
 ✗✓≈30
Stafeev et al. [270] 2024 Crawlers’ measurement methodology ✗ ✗✓403+27
Birrell et al. [31] 2024 Internet privacy regulations ✗ Worldwide✓270
Rieder et al. [238] 2026 Detection measurement methodology
 ✗✓59+16
Ours2026 Techniques, mitigations, regulations
 EU & US✓255
1980 to 2026 1). We obtain a total of 19438 papers that we
filter using keywords (see Appendix A.1). These keywords
were refined over multiple iterations by discussion among
two expert authors. The resulting list of 768 candidate papers
is manually reviewed to further exclude publications unre-
lated to web tracking techniques, mitigations, or regulatory
compliance (e.g., IoT tracking, advertising use cases).
 N=302
N=458 /uss
 /ccs
 /pet
 /imc
 /www
 /sp    N=2303IEEE S&P
Exclusion Keywords
   N=2924
   N=3852
   N=1115
   N=1241
   N=6205
USENIX
ACM CCS
ACM IMC
PETS
WWW
https://dblp.org/db/conf
 /ndss    N=1798NDSS
Title
Authors
Year
DOI
Abst.
N=19438
Title
Abst.
N=13728
Inclusion
Keywords
(set 1)
PDF
DOI
Abst.
PDF
N=768
Inclusion
Keywords
(set 2)
 N=195Title
N=255
Extracting 1980-2026 papers
published at top venues
DOI lookup to
obtain abstract
Obtaining paper PDF from DOI and
filtering to retain relevant papers
Papers included
after manual review
Techniques (58)
Measurements (108)
Defenses (65)
Regulations (34)
Figure 2: Overview of our literature search.
Systematization.This yields a final set of 255 research papers
across the following dimensions: 58 tracking techniques and
108 measurements, 65 defenses, and 34 regulatory compliance
papers (see Appendix A.2 for details). We systematize the
evolution of web tracking along these dimensions by follow-
ing Clarke and Braun’s thematic analysis [39] that eliminates
the need for inter-rater reliability. First, one researcher with
expertise in web tracking, reviewed each included paper in
detail to evaluate it based on our systematization criteria listed
in Table 2. For each criteria, the expert assigned one or more
relevant categories. Next, the evaluator convened with a sec-
ond expert to deliberate the assigned categories, resolve any
ambiguities, and reach a consensus on the final taxonomy. We
1Only papers available on DBLP (https://dblp.org/db/conf) by June
1st, 2026 were included. Papers were queried using conference-specific paths,
e.g., for PETS, we use ‘conf/pet’ (2000-2014) & ‘journals/popets’ (2015+).
structure the SoK around this taxonomy and systematize evo-
lution of tracking techniques, defenses, and regulatory com-
pliance, while identifying research gaps and future directions.
When needed, we use our domain expertise to complement
our explanations with other relevant publications or aspects.
Approach Limitations.Selection Bias.We scope our SoK
to the seven aforementioned venues where web tracking re-
search has been commonly published, and so, we may have
missed other relevant publications.Coding Bias.As with any
qualitative analysis, our systematization is subject to a degree
of subjectivity. We mitigate this following Clarke and Braun’s
thematic analysis approach [39] coupled with our domain
expertise.Focus on EU and US Regulations.We scope our
approach to the EU and US contexts because they are the
closest to our expertise and their regulations have often been
precursors to others around the globe2. For a broader explo-
ration of privacy regulations elsewhere and their nuances, we
refer readers to the following SoK from Birrell et al. [31].
Scope coverage.We consider adjacent topics such as advertis-
ing out-of-scope. Also, we focus on systematizing high-level
advances across literature rather than detailing findings from
individual papers. Due to space constraints, mixed tracking
techniques and their defenses are deferred to Appendix C.
4 Tracking Techniques
Our approach described in Section 3 to systematize 58 pa-
pers on specific web tracking techniques, complemented by
108 measurement studies that characterize their real-world
aspects, yields 24 distinct tracking techniques, mapped in Ta-
ble 7. Fundamentally, each tracking technique relies on ar-
tifacts tied either to the user, their device, or their browsing
activity. To this end, we systematize the artifacts that track-
ers are observed to rely on across different papers into eight
2Seehttps://cnil.fr/en/data-protection-around-the-world
3

Table 2: Summary of systematization criteria and taxonomy for tracking techniques, defenses, and regulatory compliance.
Criteria and Description TaxonomyTechniques
Technique: What tracking is studied in this research? See 24 techniques in Table 3.
Artifact(s): What artifact(s) is used by this technique? See 8 artifact types listed in Table 6.
Capabilities: What capabilities are required by this technique? I Inclusion, E Execution, O Observation, T Storage, S Sharing.
State: What state does this technique maintain? Stateful, Stateless, Mixed.
Context: In what context does it function? Third-party, First-party, Both.
Goals: What are the goals of the tracker using this technique? Same-site, Cross-site, Cross-context.
Defenses
Technique: What tracking does this defense protect against? See 24 techniques in Table 3.
Artifact(s): What artifact(s) does it apply protection to? See 8 artifact types listed in Table 6.
Development: Who developed this tracking defense? Research-based, Industry-based, Community-based.
Deployment: How is this defense deployed?●In-browser,◆Extension,▲Infrastructural,❍Offline.
Support: What is the support for this defense? See Table 10, Table 11, and Figure 3.
Goals: What are the goals of this defense mechanism? Detection & Blocking and Signal Reduction & Obfuscation .
Type: How can the defense mechanism be classified? See 8 research (Table 4), 23 industry&community (Table 10, Table 11).
Policies
Policies: What regulations and standards are studied? See EU and US regulations, and standards in Table 14.
Aspects: Which aspects of these policies are covered? See mapping of 9 policy aspects onto 6 user rights in Table 15.
Compliance: What are the enforcement challenges? Reconciling Incentives , Expectations , and Responsibilities .
Gaps
Open Problems: What are potential gaps and future directions
in the evolution of these techniques, defenses, and regulations?
See the 24 open problems throughout the paper as well as 4 open
problems in appendix.
categories (Table 6). Table 3 systematizes research to map
tracker capabilities exercised over artifact categories for each
tracking technique, with a paper-level breakdown represented
in Table 8. This section systematizes tracking techniques by
state maintained by the trackers across different contexts.
4.1 Stateful Tracking
Stateful trackingtechniques involve maintainingstateby stor-
ing a unique identifier in the user’s browser and retrieving it
or updating it across visits, using either dedicated browser-
provided interfaces (e.g., cookies) or as side effects of other
functionality (e.g., E-Tags, HSTS upgrades) [9, 79, 266].
4.1.1 Cookie-based Tracking
Cookie-based tracking relies on the browser’s cookie jar T to
maintain state, with cookies set and retrieved via HTTP head-
ers S or JavaScript (JS) APIs such as document.cookie E .
Cookies were adopted for cross-site tracking almost imme-
diately after their introduction in the 1990s [201], prompt-
ing early privacy concerns [152, 285]. Despite these con-
cerns, third-party cookie-based tracking remained dominant
for nearly two decades, becoming both widespread and con-
centrated among a few third parties [83, 135, 151, 167, 314].
Browsers mediate cookie access based on the context in
which they are set [25, 190, 258]. As Safari and Firefox
began blocking or partitioning third-party cookies by de-
fault [193, 305] between 2018 and 2020 (Section 5.1), track-
ing shifted to the first-party context—nearly 90% of websites
now set first-party tracking cookies, 96% of which are set by
third-party scripts, making browsing with third-party cook-
ies disabled largely indistinguishable from the pre-blocking
web [172, 207, 301]. Meanwhile, trackers continue exploiting
browser- and protocol-level edge cases such as opting out
of SameSite=Lax and instead relying on SameSite=None
cookies [139], to retain stateful tracking capabilities [17].
4.1.2 Cookie Respawning
Once a user clears their cookies, a tracker that has stashed
the same identifier somewhere else in the browser can rewrite
it back into the cookie jar, “respawning” or reconstructing
the identifier and creating a so-called “supercookie” or “ever-
cookie” [2,12,268] as described in Section 5.1.1. Respawning
was first demonstrated at scale using Flash Local Shared Ob-
jects and other legacy plugin storage [2, 83], and later shown
to also draw on browser fingerprints themselves—a 2022
study measured a lower bound on fingerprint-based respawn-
ing by detecting it on 1,150 of the top 30K sites [93]. More
recently, respawning has expanded beyond the browser, lever-
aging cross-context state shared with native applications to
recover identifiers [306] (further discussed in Appendix C.1).
4.1.3 Cookie Syncing
To exchange information about users across domains included
on a webpage I , third-party companies rely oncookie sync-
ing[2]—first described by Olejnik et al. [222]—which syn-
chronizes user identifiers maintained in each party’s cookie
jar T , most commonly shared via URL parameters embedded
in redirects S between them, requiring script execution E
4

Table 3: Tracker capabilities most commonly exercised over each artifact (rows) for each tracking technique (columns). I Inclu-
sion, E Execution, T Storage, S Sharing, O Observation.
Tracked
Artifacts
Third-party Cookie Tracking
Cookie Respawning
Cookie Syncing
First-party Cookie Tracking
Tracking Pixels/Tags
CNAME Tracking
Link Decorations
Bounce Tracking
Authentication-based Tracking
Cross-context Tracking
Javascript-based Tracking
Browser Fingerprinting
Extension Fingerprinting
Device Fingerprinting
Passive Fingerprinting
Kernel-based Side-channels
Network-based Side-channels
Timing-based Side-channels
Storage-based Side-channels
Behavioral Tracking
Browser Storage and Cache T T T T T T T T T T T T
JS-Accessible Browser APIs E E E E E E E E E E E E E E E
Webpage Artifacts I I I I I E I I I I I I E I E I E I E I I I I I E
Hardware Artifacts E O E O E O E O
Network Protocol Artifacts S O O O O
HTTP Traffic Artifacts S S S S S S S S S S S S S S S S O S S S
Navigational Artifacts S S S S S
Identifiers T S T S T S T S T S T S S T S T S T S T S S S S
to initiate the sync. Earlier works formalized cookie syncing
detection [2, 18, 83], which has since been refined [228] and
scaled into automated, graph- and ML-based pipelines trac-
ing identifier flows across the ecosystem [120, 228]. Cookie
syncing is not just confined to the third-party context [244],
as identifiers in first-party cookies have been observed to be
shared with hundreds of other third-party domains [207, 213].
4.1.4 Tracking Pixels/Tags
Tracking pixels, traditionally referred to as 1x1 image ele-
ments embedded I on a webpage, shared S user data with a
tracking endpoint over HTTP traffic artifacts, enabling same-
and cross-site tracking [83, 210]. Their prevalence and pri-
vacy risks have been measured extensively, from early ar-
chaeological studies of the tracking ecosystem [83, 167] to
recent audits of their collection of personal data [19, 113]. As
browser restrictions rendered third-party image-based pixels
increasingly ineffective, modern tracking pixels have evolved
into JS-basedtracking tagsthat execute E with the embed-
ding site’s first-party privileges to collect richer behavioral
data [20, 207], while trackers increasingly obfuscate pixel
behavior via falsified image dimensions, redirect chains, and
encoded identifiers [113]. Modern tags have also expanded
in scope to support tag management, bot detection, session
replays, and email tracking [1, 80, 82, 91, 252]. Recent studies
have shown deployments of the same vendor’s tag to vary sub-
stantially across websites in their data collection [19, 96, 140].
Open Problem: Detecting the mere presence of a track-
ing tag is not enough to understand its capabilities—how
do different configurations across sites and vendors deter-
mine what data is tracked, collected and shared, and how
those settings evolve? What generalizable approaches can
systematically measure tracking deployments across tags?
4.1.5 CNAME Tracking
Rather than embedding a third-party resource directly, a web-
site can create a CNAME DNS record pointing a first-party
subdomain (e.g.,metrics.news.com) to a third-party’s infras-
tructure. Because the browser only resolvesmetrics.news.com,
cookies set through this alias are treated as first-party T , al-
lowing trackers to evade defenses that block third-party do-
mains rather than DNS resolution [75] (a network protocol
artifact). First documented in 2014 [221,222], CNAME cloak-
ing became widely adopted later in the decade as a response
to browser anti-tracking measures. Deployed on roughly one
in ten of the top-10k websites [75], cloaked requests are in-
distinguishable from legitimate first-party traffic [54, 75].
More broadly, CNAME cloaking supports an emerging
server-side trackingparadigm, which reuses client-side pix-
el/tag instrumentation to collect tracking data but routes the
resulting requests through a publisher-controlled first-party
endpoint—often a CNAME-aliased or A/AAAA-record sub-
domain [124]—before forwarding payloads to the tracker’s
backend via server-to-server communication, rendering client-
side defenses ineffective [92]. Major platforms including
Google, Meta, and TikTok have already deployed conversion
APIs adopting this architecture [94].
Open Problem: As tracking logic shifts from client-side to
server-side, it removes the vantage point that the research
5

community has relied on to detect and mitigate online track-
ing. How can we characterize the prevalence and behavior
of server-side tracking technologies, and what new method-
ologies (e.g., differential traffic probing, cooperation with
first parties) are needed to study and defend against it?
4.1.6 Navigational Tracking via Link Decorations
Link decorationsallow sharing identifiers S via query param-
eters, resource path segments, or URL fragments appended to
an otherwise ordinary navigation. The technique dates to the
standardization of query parameters (RFC 1630, 1994) and
the Referer header (RFC 1945, 1996), but became a deliber-
ate tracking channel with the introduction of UTM parameters
by Urchin/Google Analytics in 2005 and Google’s click ID
(gclid) in 2010. As browsers began restricting third-party
cookies, major ad platforms followed with their own click IDs
(e.g., Meta’s fbclid, Microsoft’s msclkid), and over 70% of
websites now use decorations to share user data such as first-
party cookies and email across navigations [150, 206]. Sim-
ilarly, linkshimminginvolves a first-party rewriting the out-
bound links with decorations to route clicks through its own
domain before redirecting. While used for HTTPS upgrading
or malicious-URL blocking, it equally enables the first party
to log every outbound navigation [168]. A recent audit of
the Referer header further shows that inconsistent browser
enforcement of Referrer-Policy still permits the cross-site
identifier leakage the policy was designed to prevent [317].
4.1.7 Bounce Tracking
Bounce trackingis another navigation-based mechanism that
renders third-party cookie blocking ineffective [138]. Unlike
link shimming, bounce tracking specifically involves navi-
gating athird-partytracker’s domain in first-party context,
momentarily surfacing it during a redirect chain so it can read
and write identifiers (via JS APIs E or cookie headers S )
that persist in first-party storage T , linking them with website-
specific identifiers for cross-site tracking. Bounce chains can
involve two (news.com→tracker.com→news.com ) or
more unrelated sites. Due to usability disruptions and defen-
sive measures, bounce tracking is not as widely pervasive as
link decorations [120], but both mechanisms are often used
together. Measurements in 2020 found that 11.6% of sites
use one of the top 100 redirectors [150], and in 2022 such
identifiers were present in 8.1% of crawled navigations [233].
Open Problem: Each generation of navigational tracking,
from UTM parameters to click IDs to bounce tracking,
emerged as its predecessor was restricted. How will track-
ers adapt these channels to complement server-side tracking
and how can we defend against it?
Overall, every time an anti-tracking defense closes off one
tracking vector, stateful trackers relocate tracking a layer fur-
ther from the browser—from third-party cookies, to first-party
cookies and synced identifiers, to DNS aliases, to server-side.
Open Problem: As tracking logic keeps moving away from
the browser, the community’s tooling needs to advance with
it, or risk studying an increasingly small unrepresentative
slice of how users are actually tracked.
4.2 Stateless Tracking
Unlike stateful tracking,statelesstracking does not rely on
stored identifiers but instead collects artifacts of the user’s
behavior, browser, or hardware to generate a fingerprint that
correlates users across sites and sessions. Nearly all stateless
techniques are realized by exercising the E capability, with
JavaScript running in the including context’s privileges I .
Fingerprinting.Fingerprinting corresponds to the gather-
ing of information on users’ behavioral (e.g., mouse move-
ments, keystrokes), browser (e.g., version, screen size, in-
stalled fonts), and hardware/OS in real-time via HTTP headers
and JS APIs to identify users. Its use for tracking is hard to
prevent due to the duality of fingerprinting (see Appendix B)
which serves both constructive (e.g., bot and fraud detection)
and destructive (e.g., tracking anonymous users) purposes. Re-
cent work only began to differentiate intent, e.g., by using ad
changes as a heuristic for fingerprinting-driven tracking [177].
Open Problem: Can we automatically assign the purposes
of trackers to determine fingerprinting intent and block only
tracking use cases while allowing the benign ones?
4.2.1 Passive Fingerprinting
Passive fingerprintingexploits metadata attached to every
request—most commonly IP address and User-Agent string
(IPUA). Despite its instability across networks, IP alone,
or combined with minimal additional signals, can identify
users [144, 200], and even IPv6 address rotations intended to
improve privacy is undermined by predictable ISP schedules
and stable interface-identifier components [242]. Recent User-
Agent reduction efforts have partially shrunk this surface, but
remaining passive signals and Chrome’s new Client Hints API
still carry substantial identifying information [78, 251, 307].
4.2.2 Browser Fingerprinting
Browser fingerprintingactively probes browser APIs to col-
lect configuration information about the browser, device, and
OS. Since the first academic work on browser fingerprinting
in 2009 [187] and the Electronic Frontier Foundation’s Panop-
ticlick shortly after [78], researchers have extensively studied
its impact on privacy and diversity [99, 156], its evolution
and stability over time [299], its detection [217, 275], and
discovered abusable browser APIs [67, 116, 173, 220]. We
6

refer readers to Laperdrix et al.’s SoK [155] for a compre-
hensive understanding of foundational aspects of browser
fingerprinting. Over the years, its prevalence has grown
steadily [3, 83, 118, 212]. Browser fingerprints are inher-
ently unstable, with 80% of instances changing within 10
days [169, 299]. So trackers often link evolving fingerprints
by combining them with stateful techniques such as cookie
respawning [93] (Section 4.1.2). Meanwhile, the exploitable
surface continues to widen beyond Canvas, WebGL, and
Audio APIs [47]: permission states [217], CSS and font-
rendering differences [173], divergent JS execution across
platforms [316], and, even privacy-hardening switches them-
selves [116]. Conclusions from prior studies about fingerprint
uniqueness vary with dataset scale, and it remains unclear
whether they generalize across devices, populations [23, 231],
or real browsing conditions [73, 208], rendering its purpose
and integration within live systems poorly understood.
Open Problem: What is the real impact of fingerprinting at
scale, on vulnerable populations (e.g., minorities, children,
marginalized), and paired with other techniques?
4.2.3 Hardware Fingerprinting
Hardware fingerprintingexploits physical-layer variations
to identify devices, first demonstrated via TCP clock-skew
measurements [148] and later extended to the web through JS-
accessible device [212] and cross-browser OS/hardware [45]
properties. Researchers have since demonstrated fingerprint-
ing of specific components including CPUs [246, 289], GPUs
via rendering variations [154], DRAM via Rowhammer-styled
access patterns [302], and kernel-level PRNG state [141,149].
The mobile ecosystem expands this surface through BLE
frames [184] and motion, orientation, and acoustic sensors
that are accessible without permission prompts [67, 319, 323].
Open Problem: Hardware fingerprinting exploits manu-
facturing variations that cannot be mitigated via software
updates. What principled abstractions or hardware-software
co-designs can provably bound the fingerprintable informa-
tion leaking through device APIs, while preserving func-
tionality and security properties (e.g., hardware attestation,
PUFs) that rely on the same physical-layer uniqueness?
4.2.4 Behavioral Fingerprinting
Fine-grained interaction signals such as mouse movements,
keystroke patterns, and touch gestures can reliably distinguish
users and support continuous authentication [10,87,165,321].
Mobile touch dynamics alone offers roughly 20 bits of entropy
without requiring any permissions [185]. Keystroke patterns
link users across devices [315], engagement patterns correlate
users across unrelated sites [98], and form-filling behavior is
collected at scale via session replay technologies [1, 66, 174].
Recent work has begun assessing how well behavioral meth-
ods hold up as a general-purpose fingerprinting signal [64].
Open Problem: As AI agents automate web browsing, they
will impact behavioral fingerprinting techniques, raising
questions on its effectiveness, attribution, and evasion.
4.2.5 Extension Fingerprinting
Browserextension fingerprintinginfers the presence of spe-
cific extensions, which can reveal sensitive user attributes
(e.g., health conditions, religion) [136]. Early approaches re-
lied on probing web-accessible resources (W ARs) that exten-
sions expose [271–273], but because static WAR probing is
comparatively easy to randomize away [291], research shifted
towardsbehavioralextension fingerprinting—inferring ex-
tensions through side-effects during execution such as in-
formation leakage across components [55], user-triggered
actions [264], injected CSS [157], and transient DOM ed-
its [265]. Behavioral fingerprints have proven far more re-
silient, with 88% remaining effective even against dedicated
countermeasures [136], making defense fundamentally harder
than blocking resource enumeration. Most recently, even ad
blockers have been shown to be fingerprintable through script-
less, filter-list-driven side effects, where customizing a rule
set paradoxically shrinks a user’s anonymity set [51].
Open Problem: How can future browser architectures and
extension frameworks be co-designed so that extensions
can modify page behavior without exposing detectable side-
effects, and what privacy guarantees can such designs for-
mally provide against an adaptive adversary that combines
behavioral, stylistic, and scriptless fingerprinting vectors?
4.2.6 Side-channel Fingerprinting
Side-channel fingerprintingexploits unintended information
leakage across browser, network, and hardware layers to track
users without relying on stored identifiers or active probing.
These mechanisms are challenging to detect and mitigate.
Kernel-based Side-channels.At the OS level, process-
accounting interfaces leak enough about recent activity to
fingerprint browsing history from kernel artifacts alone [123].
Additionally, Linux’s shared kernel PRNG state lets attack-
ers correlate DNS and TCP/IP behavior into a stable device
identifier that persists until reboot [141, 149].
Network-based Side-channels.Encrypted traffic still leaks
sensitive state through observation O of network-level arti-
facts such as packet sizes and timing [57, 100], TLS client
certificates act as persistent supercookies rarely revoked by
users [90], and QUIC’s connection-migration feature lets
server-chosen connection IDs be encoded and visible to on-
path observers even as clients change networks [277].
Storage-based Side-channels.Multiple browser caching lay-
ers such as favicon cache [266], HTTP cache, ETags, Alt-
Svc [199], and DNS resolver cache [142] were independently
7

proven abusable as cross-context identifier stores T , since
none were originally designed with cross-site isolation in
mind. More recent works have demonstrated that shared
browser resource pools create cross-context timing channels
in all major browsers [261] and automated feature-testing
frameworks have surfaced previously unknown tracking vec-
tors by probing browser features systematically [4].
Timing-based Side-channels.Timing attacks on the web
date to Felten and Schneider’s 2000 demonstration that cache
behavior reveals browsing history [85], and have since esca-
lated through JS-driven CPU cache attacks [223], browser-
level side-channels independent of network conditions [296],
and concurrency-based timing that eliminates the need for
absolute clocks [297]. Most notably, Chrome’s Site Isolation—
introduced specifically to counter Spectre—was itself shown
to introduce new cross-origin timing side-channels [127].
Open Problem: Major browser features added for perfor-
mance or security have often retrospectively introduced a
tracking side-channel. Can browsers move from reactive
patching to proactive side-channel auditing of new APIs
and architectural changes before deployment? How can
researchers build automated discovery frameworks directly
integrable into the browser feature review process?
5 Tracking Defenses
We systematize defenses against tracking techniques de-
scribed in Section 4 across three dimensions in accordance
with the criteria defined in Table 2:industry-based,research-
based, andcommunity-based. Following the methodology
described in Section 3 and Appendix A.2, we first curate
industry-based (see Table 12) and community-based (see Ta-
ble 13) defenses and research literature comprising 65 pa-
pers on tracking defenses (see Table 9). Each defense tech-
nique is grouped by its goal either as detection and blocking
or signal reduction and obfuscation . For industry-based and
community-based defenses, we identify 12 techniques against
stateful tracking (see Table 10) and 11 techniques against
stateless tracking (see Table 10). We also systematize support
of defense techniques across each browser (Edge, Firefox,
Brave, Chrome, and Safari). For research-based defenses, we
identify 8 defense techniques described in Table 4, grouped
by the two defense goals. Table 9 maps each paper to these
defense techniques. Figure 3 depicts the evolution of tracking
defenses under a single timeline from 2000 to 2026.
5.1 Defenses Against Stateful Tracking
5.1.1 Industry-based Defenses (Table 10)
Clearing State.A user could clear their browser’s cookies
at the end of session, however, ordinary cookie clearing does
not remove identifiers stored in localStorage, IndexedDB,
E-Tags, or the browser cache, letting trackers respawn deleted
cookies from such copies [3, 12, 269]—any API that per-
sists even a single bit of state is a potential supercookie vec-
tor [4,132,145,268]. This motivated the cache-, network-, and
storage-partitioning efforts that Firefox, Chrome, and Safari
each shipped between 2020 and 2021, isolating TLS sessions,
DNS caches, connection pools, and the HTTP cache by top-
level site [104, 191, 198], closing off cross-site respawning
even where same-site respawning may still be possible.
Restricting or Partitioning Third-party State.Initially,
browser vendors attempted to restrict third-party cookies
themselves, leaving exceptions for non-tracking uses such as
single sign-on [65], before blocking or partitioning them out-
right. Safari’s ITP, introduced in 2017, used an on-device ML
classifier to identify likely trackers and eventually blocked
all third-party cookies by default in 2020 unless a site was
explicitly visited as first-party or used the Storage Access
API [305]. Firefox’s ETP shipped off by default in 2018, on
by default a year later, and added Total Cookie Protection in
2021, which partitions cookies per top-level site rather than
blocking them outright [193]. Brave has blocked all third-
party cookies and storage through Shields since its earliest
developer preview, granting only ephemeral, per-session par-
titioned storage to third parties that need it [280]. Chrome
has moved far more cautiously: it initially blocked third-party
cookies only in Incognito by default, introduced CHIPS as an
opt-in partitioned-cookie attribute in 2023, and after repeated
delays abandoned its plan to deprecate third-party cookies
altogether in 2024 [49], leaving SameSite and the Storage
Access API [192] as its main developer-facing tools; Edge
inherits Chromium’s defaults. Systematic testing of these
cookie-blocking implementations has repeatedly uncovered
bypass vectors via redirects, popups, and nested iframes [95].
Restricting or Limiting First-party State.First-party cook-
ies cannot be blocked without breaking site functionality,
so browsers instead limit their lifetime. Safari’s ITP expires
script-set first-party cookies after seven days (24 hours with
link decoration) and applies CNAME and IP heuristics to un-
mask disguised third-party hosts [305]; Brave applies equiv-
alent caps and adds Forgetful Browsing to clear storage for
sites the user stops visiting [40]; Chrome, Firefox, and Edge
apply no equivalent first-party lifetime cap by default. As
third-party cookies are restricted, websites increasingly rely
on a handful ofidentity providersthat combine first-party
data with offline data (e.g., loyalty cards, point-of-sale) to
construct proprietaryidentity graphs, concentrating behav-
ioral insights and eroding users’ ability to maintain separate
or pseudonymous personas [71, 205].
Open Problem: How can defenses detect, audit, or con-
strain opaque first-party data flows within the identity
provider ecosystem, which enables persistent user tracking
and identity continuity across contexts and devices?
8

Removing or Limiting Navigational Parameters.Browsers
remove URL parameters used by trackers. Firefox (ETP
Strict), Brave, and DuckDuckGo strip known tracking query
parameters from URLs, while Safari does so in Private
Browsing [305]. All five major browsers also default
to strict-origin-when-cross-origin Referrer-Policy,
stripping parameters from cross-originRefererheaders.
Protecting Against Bounce Tracking.Bounce tracking
grants a tracker temporarily unrestricted first-party storage
access. Moreover, resemblance of authentication flows to a
bounce complicates the defense [138]. Firefox and Chrome
mitigate it by deleting storage for domains visited only in
redirects without recent user interaction [260], while Brave
combinesdebouncing(skipping known bounce-tracker redi-
rects) withunlinkable bouncing(routing suspected bounces
through temporary, unlinkable storage) [281]. What counts as
“legitimate” interaction to spare a domain varies by browser.
Blocking Trackers.Firefox and Edge block trackers from the
Disconnect list; Brave’s Shields blocks via its own curated list
and uses PageGraph, a page-execution graph recorder, to make
decisions based on a script’s runtime behavior instead of URL
alone; Safari pairs its blocklist with its ML classifier. Chrome
ships no native filter-list blocking, and the Manifest V3 shift
has curtailed the dynamic request-blocking APIs that exten-
sions previously relied on. Against CNAME-cloaked trackers,
Brave resolves CNAME for every sub-resource request and
checks both requested and canonical domains against its filter
lists [40]; Safari caps cookie lifetime to seven days when
it detects a differing canonical domain [305], extended into
Advanced Tracking and Fingerprinting Protection (ATFP) in
2023; Chrome, Edge, and Firefox ship no CNAME defense.
Open Problem: CNAME cloaking, server-side implemen-
tations, and edge-compute proxies erase the first-/third-
party origin boundary that every major browser defense
relies on. What architectural primitive could replace it with-
out requiring visibility into server-side data flows?
5.1.2 Research-based Defenses (Table 4)
Detecting and Blocking Stateful Trackers.Most research
on tracker detection represents a webpage as a graph of its
HTML structure, network requests, and JS execution, and
trains a classifier to separate tracking from functional re-
sources. AdGraph [119] pioneered this approach (inspir-
ing Brave’s PageGraph), with subsequent work refining fea-
tures [257, 312], extending to code-property graphs and real-
world deployment [161, 163], and fully automating filter-rule
generation [159]. Complementary classifiers extended exist-
ing lists by labeling unlisted tracker domains from request
features [105, 117, 235], while Khaleesi classified requests
from their sequential redirect context to catch cookie syncing
and bounce tracking missed by per-request classifiers [120].
A subsequent line of work moved from blocking third-party
requests to classifying first-party cookies by purpose. Cook-
ieGraph separated tracking cookies from functional ones via
cookie-creation flow graphs [207], semantics-aware checkers
used LLMs to compare a cookie’s inferred purpose against
its declared consent category [52], PURL applied purpose
inference to link-decoration parameters [206], and TGNN
extended LLM-based classification to tracking pixels via
graph neural networks [310]. On mobile, NoMoAds [256]
and NoMoATS [255] intercepted app traffic through a local
VPN and classified it from traffic features alone.
Open Problem: Can current defenses move from binary
block/allow to enforcing purpose limitations—allowing
data collection for a declared purpose while preventing its
repurposing for cross-site tracking—and can such enforce-
ment be made verifiable without trusting the data collector?
Table 4: Taxonomy of research-based tracking defenses along
with its distribution across the literature (# = paper count).
Goal Defense Technique #
Machine Learning based Classification 28
Program Analysis and Code Instrumentation 17
Circumvention based Behavioral Classification 4
Detection &
BlockingLLM based Classification 2
API Output Perturbation 8
Browser State Isolation and Partitioning 6
Network Protocol level Modifications 4
Signal
Reduction &
ObfuscationCryptographic Defenses 6
Reducing or Obfuscating Signals for Stateful Trackers.
This line of research sidesteps detection by changing what
state a tracker can accumulate. Early work proposed per-
origin partitioning of visited-link styling and caches [121],
over a decade before any browser shipped it as a default.
Subsequent systems assigned each first-party a separate non-
unique browser principal [226], generalized private brows-
ing into configurable isolation levels [311], systematically
tested cross-site leak defenses [146], and isolated cookies
set by third-party-origin scripts with first-party privileges
including CNAME-cloaked ones [214]. TrackMeOrNot of-
fered per-site tracking preferences, though this does not scale
to thousands of sites [197, 215]. Server-side approaches
have anonymized user profiles before they reach trackers
through de-identification [320], formal anonymization guar-
antees [326], and adversarial browsing patterns via reinforce-
ment learning [318]. Cryptographic defenses have replaced
identifiers with privacy-preserving protocols, from probabilis-
tic cookie structures that limit cross-site linkability [202] to
private ad auctions [322] and encrypted access logging [224].
5.1.3 Community-based Defenses (Table 10)
Filter Lists.Community-maintained blocklists predate al-
most every industrial defense, with Peter Lowe’s list main-
9

tained since 1997, EasyList since 2005, and EasyPrivacy since
2006. Disconnect’s tracker list (2011) was later adopted as
the default blocklist in Firefox, Safari, and Edge, making it
the closest thing to a shared industry standard. Despite their
ubiquity, these lists face structural limitations: they are main-
tained by small groups of volunteers, do not capture nuanced
or newly emerging techniques, accumulate stale entries—
roughly 90% of EasyList’s rules are never triggered [263]—
and being static, trackers continually evade them.
Extensions and Tools.Adblock Plus, the earliest main-
stream filter-list extension (2006), popularized browser-level
ad blocking but drew criticism for its Acceptable Ads pro-
gram, which whitelists certain ads in exchange for pay-
ment from advertisers. uBlock Origin, the community’s most
widely deployed blocker, ships with EasyList, EasyPrivacy,
and its own curated filters, and also added CNAME uncloak-
ing on Firefox in 2019 to unmask cloaked trackers that no
mainstream browser could detect natively—though Chrome’s
Manifest V3 transition removed it from the Chrome Web
Store in 2025 by disabling the dynamic request-rule APIs it
depended on. Other extensions occupy complementary niches:
AdGuard maintains its own filter lists alongside EasyList
compatibility and ships as both extension and standalone
network-level application, Privacy Badger learns tracker be-
havior from cross-site request patterns rather than static lists,
Ghostery’s open-sourced engine powers the public Who-
Tracks.me dataset, and NoScript blocks all JS by default un-
less explicitly permitted. At the network layer, Pi-hole and
NextDNS block tracking domains via DNS, and ClearURLs
strips known tracking parameters before requests are made.
Open Problem: Every defense—browser defaults, research
prototypes, or extension—is evaluated in isolation, yet
users run them in combination. Can we develop a repro-
ducible framework that measures aggregate tracking resis-
tance under realistic defense compositions?
5.2 Defenses Against Stateless Tracking
5.2.1 Industry-based Defenses (Table 11)
Browser vendors treat fingerprinting as a form of covert track-
ing harmful to the web, and the W3C encourages specification
authors to consider how a new API expands the browser’s fin-
gerprinting surface [77, 218]. Yet, no browser found a way to
close this surface without a utility cost, and vendors disagree
on whether incremental mitigation is worth pursuing without a
credible path to eliminating fingerprinting entirely [236, 262].
Reducing IPUA Exposure.Safari’s iCloud Private Relay,
Chrome’s IP Protection (now discontinued), and Brave’s Tor-
routed private windows each route traffic through independent
relays so that neither the destination nor the relay operator
can link a request to a user’s real IP address. On the User-
Agent side, vendors have frozen the minor version out of
the string and shipped User-Agent reduction across Chrome,
Edge, and Firefox. MAC address randomization, now standard
on mobile, closes off a comparable network-layer identifier.
Normalizing and Randomizing API Outputs.The most di-
rect defense is to make browser-exposed information less iden-
tifying. Normalization approaches include Firefox’s resist-
fingerprinting mode (screen, hardware, and timing values), Sa-
fari’s ATFP (fonts, plugins, and User-Agent in Private Brows-
ing), and outright API removal where fingerprintability is
disproportionate (e.g., Battery Status API) or declining to im-
plement new ones (e.g., Network Information API in WebKit
and Firefox) [305]. Where normalization would break legiti-
mate site functionality, browsers instead add randomized, site-
specific noise so a device’s fingerprint changes across page
loads—Brave introduced this as “farbling” in 2020 [279],
with Firefox [114] and Safari’s ATFP [308] later adopting
it for Canvas, WebGL, and AudioBuffer outputs. All five
browsers additionally reduce high-resolution timer precision,
closing off APIs that side-channel research (Section 4.2.6)
relies on. Because normalization makes all users look alike
while randomization only makes one user’s fingerprint noisy
over time, the two trade off differently against a patient tracker,
and browsers have generally converged on randomization as
the more deployable default. Chrome’s Privacy Budget pro-
posal [158], meant to bound per-tracker API exposure, was
discontinued due to concerns about website breakage and risk
of exposing additional tracking surface [164, 236, 262].
Open Problem: Can a perturbation scheme be designed
with an output distribution provably indistinguishable from
the natural device population? Could a browser bound
the cumulative information any page extracts about a user
across its entire interaction and enforce this bound natively?
Blocking JS, Tracking Scripts, or Mixed Scripts.Mozilla’s
anti-tracking policy forbids fingerprinting [204]; Firefox
blocks scripts detected to include fingerprinting code [81].
Firefox and Edge use Disconnect’s fingerprinting list to block
scripts, Brave’s Shields uses its PageGraph execution recorder,
and Safari’s ATFP blocks known fingerprinting scripts in Pri-
vate Browsing. Browsers also allow disabling JS per site.
Side-channel Mitigations.Chrome, Edge, and Firefox further
isolate cross-origin content into separate OS processes (Site
Isolation and Firefox’s Fission) but this introduces new timing
side-channels, on top of the timer-precision reductions.
Open Problem: How can browsers defend against emerg-
ing side channels, including XS-Leaks and cross-site sig-
nals exposed by CDNs, that persist even when traditional
fingerprinting is mitigated?
5.2.2 Research-based Defenses (Table 4)
Detecting and Blocking Stateless Trackers.Detection has
moved from heuristic-based approaches flagging known prob-
ing patterns [3] to ML classifiers over static and dynamic
10

script behavior [118] and longitudinal models predicting
which newly shipped APIs are likely to become fingerprinting
vectors [16]. Dynamic taint tracking has been applied to fol-
low fingerprinting-relevant values from API call to network
request inside instrumented Chromium builds [37, 115, 134],
while coarse server-side fingerprints have also been used
defensively to flag fraudulent device configurations [131].
Beyond request-level, several systems have blocked tracking
at the script level. TrackerSift [7] and Duumviri [254] sep-
arated tracking from functional code within mixed scripts,
SugarCoat [259] generated replacement scripts preserving
page functionality, and finer-grained approaches have blocked
at function [6, 8], bytecode [15, 97], graph [229], or event-
loop [56] levels. As blocking may cause site breakage, com-
plementary work has also detected it from screenshots [107]
and studied user perception [215]. Trackers often evade
blocking: anti-adblock circumvention has been characterized
through differential execution [324] and automated detec-
tion [160]. Adversarial perturbations against perceptual block-
ers [290] have motivated adversarially robust classifiers [171].
Reducing or Obfuscating Signals for Stateless Trackers.
Gummy Browsers showed that a script’s own fingerprint-
collection routine can be turned against it, replaying a target’s
attribute values to impersonate a different device [179], while
UNIGL rewrites WebGL shaders so GPU rendering output
is identical across hardware, removing device-level variation
at its source [309]. On the randomization side, PriVaricator
injects policy-controlled noise into fingerprintable APIs [211],
ML-CB decides per call whether a Canvas access looks like
fingerprinting before blocking [235], and FP-Sandbox de-
grades API output past a privacy budget [286]. Comparative
evaluations have consistently found that such defenses leave
a residual detectable signature [70]. Extension fingerprinting
has been countered by Simulacrum’s DOM virtualization, giv-
ing every page a consistent view regardless of installed exten-
sions [137]. Behavioral tracking has been addressed by obfus-
cating interest profiles: Bloom Cookies encode profiles with
controlled false positives [202], HARPO poisons ad-interest
profiles with reinforcement-learned decoy actions [318], and
profile generalization provides k-anonymity for browsing
history [320, 326]. Passive IPUA fingerprinting is harder
to counter in the browser alone, so proposals have acted at
the network layer: unlinkable pseudonymous tokens [128],
ISP-level address mixing [232], TLS handshake metadata re-
duction [278], and MAC-address randomization, whose real-
world effectiveness has been found incomplete [86]. Side-
channel defenses draw on the same partitioning techniques
used against stateful supercookies [121], alongside system-
atic cross-browser XS-Leak testing [146] and network-level
tracking detection from encrypted packet metadata [162].
5.2.3 Community-based Defenses (Table 11)
Filter Lists.Stateless tracking has no dedicated filter-list
ecosystem of its own; instead, the same Disconnect, EasyList,
and EasyPrivacy lists that community maintainers curate for
cookie- and script-based blocking (Section 5.1.3) carry the
fingerprinting script and known-tracker entries that Firefox,
Edge, and Brave draw on for the blocking described above.
Extensions and Tools.Tor Browser, launched in 2008, re-
mains the reference implementation for fingerprinting re-
sistance, providing first-party isolation and a uniform, one-
fingerprint-for-all browser configuration by reporting the
same values for a wide range of APIs [230], and Mullvad
Browser extended the same hardening to users who want
it without routing through the Tor network itself. NoScript
blocks JavaScript per site by default, eliminating essentially
every stateless technique that depends on script execution at
the cost of breaking sites that need it, and AdGuard’s Stealth
Mode layers User-Agent overriding and referrer stripping on
top of its filter-list blocking. The EFF’s Panopticlick project,
and later the Markup’s Blacklight and DuckDuckGo’s Tracker
Radar, have shifted the community’s role from blocking alone
to auditing, letting any user or researcher scan a site and see
exactly which fingerprinting and tracking techniques it uses.
6 Regulations & Compliance
Here, we describe the enactment and evolution of EU and
US privacy regulations. We start by curating the 34 research
papers identified in Section 3 to systematize the different
regulations and standards they cover (Table 14) according
to Table 2. We map in Table 15 the mentioned policy aspects
onto the six self-managed rights3 granted by regulations and
their applicability in the EU and US (California) contexts.
Then, we categorize the suggested limitations with compli-
ance (Table 5). Finally, we complement this taxonomy with
our expertise to provide a cohesive view of the evolution of
regulatory actions in the EU and US (overview in Figure 3).
6.1 Regulatory Actions
In the EU.First data protection national laws were estab-
lished in the late 1970s, followed by the EU Data Protection
Directive in 1995, and the GDPR applicable to all EU mem-
bers in 2018. Personal EU-US data transfers are currently
regulated by the EU–US Data Privacy Framework. The ePri-
vacy Directive (ePD, 2002, amended in 2009) requires a valid
user’s consent before“storing of information”. This notion
was redefined by GDPR by setting higher-level legal require-
ments [248]. EU regulators continuously update their national
3For a taxonomy of rights and requirements imposed by privacy regula-
tions, we refer to the SoK on Internet Regulations from Birrell et al. [31].
11

laws and compliance guidelines to further interpret and im-
plement the ePD [30], for instance to: (1) require consent
before cookies are set, read, or sent to third-parties, (2) es-
tablish a legitimate interest exemption, and (3) cover various
types of devices (mobile, IoT) and technologies (pixels, link
decoration). EU laws like the Digital Markets Act set up
rules on valid consent for major“gatekeeper”companies and
the Digital Services Act on dark patterns and advertising for
platforms. Currently, the Digital Omnibus proposal aims to
amend, simplify, and optimize the EU’s digital rulebook to
reduce compliance burden and increase EU competitiveness.
In the US.States enact their own privacy legislation: Califor-
nia passed the CCPA (2020) and CPRA (2023), soon followed
by other states [31, 298] as depicted in Figure 3. Only a few
narrow privacy laws exist at the federal level. Thus, apart
from mandatory provisions, the notice and choice principle,
implemented via privacy policies, governs what a recipient of
personal information can do with it [250, 327]. Additionally,
under its jurisdiction, the FTC can consider privacy policies
that misrepresent a business’s data handling practices as un-
fair or deceptive, affecting commerce. In California, recent
changes to CCPA via CPRA may negatively impact the us-
ability, scope, and visibility of the right to opt-out of sale [48].
Open Problem: Does the EU’s Digital Omnibus carry
similar risks to the CPRA in its proposed amendments?
Policy-oriented Solutions.Several attempts were made at
policy-oriented protocols through opt-out signals (see Ap-
pendix C.2.3) or by the industry with the Data Rights Protocol,
GDPR consent (TCF), or CCPA compliance frameworks—
whose efforts overall remain in early stages [13, 109, 186].
6.2 Regulatory Compliance
EU Regulators.In the Planet49 case [36], the highest court in
the EU (CJEU) established legal precedent by declaring pre-
ticked boxes in consent design interfaces illegal. Similarly
the French CNIL found that consent banners must offer a
reject option on the first layer [29], and companies have been
fined for setting cookies prior to consent [183, 276]. For more
GDPR-related decisions, see the GDPRhub4 inventory.
US Regulators.Through its enforcement actions over the
years, the FTC has effectively created a body of common law
of privacy [267]. Similarly, state attorney generals increased
their regulatory activity based on new state privacy laws [13].
In Literature.Various studies have shown that many web-
sites’ actual behaviors are not compliant with their own pri-
vacy policies [170,182,225], or do not respect or register users’
consent correctly [31, 36, 46, 133, 178, 186, 195, 245, 298]. Re-
searchers also studied the effects of GDPR, CCPA, or both on
(a) privacy policies, noting improved transparency and unde-
sired reduction of specificity in some updates [66, 112, 176],
4Athttps://gdprhub.eu/
(b) business practices related to incomplete data redac-
tion [181] and deletion requests [74, 129, 196, 241], and (c)
non compliance of consent management platforms (CMPs)
with the right to consent or opt-out [13, 32, 34, 227, 287]
Open Problem: While the existing focus is on privacy
policy and consent, other types of compliance (e.g., EU-US
data transfer law, revoking previously agreed opt-in, data
minimization, consent propagation, etc.) are understudied.
6.3 Compliance Challenges
Multiple reasons explain such low compliance rates, we
map them to the need to reconcile actors’ Incentives ,
Expectations , and Responsibilities (see Table 5).
Table 5: Taxonomy of compliance challenges along with their
distribution across the literature (# = paper count).
Category Challenge #
Third-parties: dark patterns, server-side tracking 12Incentives Publishers: overlooking compliance 10
Regulators: clarification, enforcement, GPC 19
Researchers: collaboration, evidence collection 12Expectations
Browsers: acting on behalf of users 5
Responsibilities Third-parties: escaping their legal obligations 9
Incentives .A lack of incentive or knowledge from website
publishers can lead to privacy compliance being overlooked
when integrating third-parties or delegating consent manage-
ment to CMPs—except when legal requirements or respective
guidelines exist [274, 295]. In turn, embedded third-parties
are placed in a privileged position, giving them access to user
data, and may not act as transparently as desired resulting in
the use of dark patterns or server-side tracking [102,196,287].
Expectations .Better enforcement power from regulators
is needed [34, 196, 203, 298]. However, regulators may not
have the required manpower, financial resources, and dedi-
cated technical departments [33] to investigate that websites
are compliant not just “at the surface” [153]. The research
community could step in to fill this gap, but user studies and
web measurement artifacts are not always specific enough
to be used by policymakers in guidelines or as evidence of
violations [29, 30, 36]. This calls for closer collaboration to
ensure compliance [243] and anticipate harms associated with
future tracking techniques [66, 92, 111, 287].
Beyond legally-binding decisions, regulators can also per-
form more supportive actions such as clarifying legal aspects.
For example, they should provide guidelines and endorse spe-
cific designs of compliant CMP interfaces [93, 109, 112, 186,
196] and consider CMPs as data controllers [227, 287]. Sim-
ilarly, ambiguity should be lifted [13, 112], such as around
data deletion in the contexts of cookies respawning, legitimate
12

interest exemption, or further data sharing with other third-
parties [93, 241, 241]. Related is the ask to clarify the website
categories to which CCPA and CPRA apply to [13, 48, 298]
and the applicability of GPC in the EU context [13, 329, 332].
Finally, browsers should be expected to play a more promi-
nent role. As an example, they could technically enforce in
real time users’ consent or opt-out choices [34,36,227], remov-
ing the need to rely on a CMP, third-party, or web extension
to fill in and respect users’ preferences [13, 72].
Open Problem: How can we develop viable browser-based
consent mechanisms, integrate automated real-time compli-
ance verification, ensure their legal robustness, and enable
effective enforcement?
Responsibilities .Finally, third-parties escape legal respon-
sibility as current laws often place the main compliance obli-
gations on website owners [249] even though several studies
have identified problems around the default configurations of
third-party services [147, 239, 287].
Open Problem: What future transdisciplinary studies are
needed to ensure that research and legal communities con-
tribute to assigning responsibility to all actors fairly?
7 Discussion
7.1 Privacy-preserving advertising paradigms
The Privacy Sandbox from Google was the most recent and
extensive industrial attempt to deprecate cross-site identifiers,
by relying more heavily on on-device computation and the
browser to mediate access. However, achieving private, but
useful, ad targeting and measurement is challenging [111], as
illustrated by the following privacy limitations uncovered in
recent proposals: (a) anonymity and re-identification concerns
with FLoC [22,237], Topics [26,27,126,283], Protected Audi-
ence [180, 284], or Apple’s Private Click Measurement [282]
and Private Relay [333], (b) flawed implementations or side-
channel leakage [4, 44, 216, 292], and (c) abuse [251, 307].
Open Problem: What new privacy-preserving technolo-
gies can be built by learning from issues in prior proposals?
By late 2025, Google deprecated most Privacy Sandbox
APIs, leaving third-party cookies largely opt-in in Chrome [50,
103], while such restrictions already exist by default in Brave,
Firefox, or Safari. Overall, Privacy Sandbox demonstrated that
besides technical challenges, economic and other (misaligned)
incentives often dominate with advertising [24, 28]. Ideally,
browsers would coordinate work on privacy-preserving ad-
vertising through the W3C’s Private Advertising Technology
Community Group (PATCG), chartered in 2021, rather than
shipping unilateral, mutually incompatible APIs. Meta and
Mozilla’s Interoperable Private Attribution proposal is cur-
rently under such W3C incubation.
Open Problem: What would a standardized, cross-browser
on-device computation primitive look like that advertisers
could build against regardless of which browser a user runs?
7.2 Tracking in other ecosystems
While our focus was on web tracking, similar tracking mech-
anisms also exist in mobile apps and IoT ecosystems—using
often a richer set of sensor information available via OS APIs
rather than web APIs. Some key differences and similarities
exist: reliance on cookies on the web and on device-level iden-
tifiers such as the Ad ID (known as IDFA on iOS, AAID on
Android, or TIFA on Samsung Smart TVs), and vendors mak-
ing different design choices across ecosystems. For instance,
while Safari blocks third-party cookies by default, iOS instead
asks permission to give access to device-level identifier.
Open Problem: If cross-device tracking is understood the-
oretically, characterizing its occurrence in practice and de-
fending against it requires more efforts. How do techniques
and protections combine and diverge across ecosystems?
7.3 AI as an emerging tracking surface
AI is beginning to reshape web tracking on multiple fronts.
Browsing behaviors are shifting as AI assistants navigate
the web on behalf of users. This introduces a new context
where account-linked identity meets rich conversational and
behavioral signals otherwise not shared on the web [300].
As AI platforms already embed trackers [125], introduce ads
in chatbots (e.g., ChatGPT), or use LLM to infer sensitive
user attributes from ordinary browsing data [53], harms and
privacy concerns may amplify. Browsers have a key role to
play in ensuring security and privacy of novel AI integrations.
Open Problem: Will advertising and tracking shift to AI
platforms, creating new tracking surfaces or amplifying the
existing ones? Conversely, can real-time adaptive defenses
be built with LLMs to surpass today’s static heuristics?
8 Conclusion
Decades after its introduction, web tracking still remains an
archetypal cat-and-mouse game. This adversarial dynamic
shows that purely reactive approaches cannot deliver privacy
guarantees for online users.Regulations alone are insufficient
as enforcement lags the speed of technical changes in evolving
tracking mechanisms, and trackers often find tolerated gray
zones to bypass regulations. Regulators and the measurement
community need to collaborate to incorporate agile, evidence-
driven auditing methods to avoid any oversight and ensure that
regulations evolve competitively with the technical reality. On
the other hand, whilebrowsers can be powerful gatekeepers,
they provide an unreliable line of defense. Default protections
13

vary widely across browser vendors, mitigations ship years
after the issues are identified, and commercial incentives of-
ten result in more permissive designs. Future research must
therefore look beyond “fix it in the browser” remedies and
explore complementary approaches that truly safeguard users’
privacy. The current tracking landscape demands adefault
privacy-first solutionwhere users can control their privacy.
By systematizing evolution of web tracking, its defenses, and
regulatory compliance, this SoK calls for a privacy-first web
in which tracking is systematically measured and proactively
audited, while users remain in control of their data by default.
Acknowledgments
This material is based upon work supported by the National
Science Foundation under Grant Numbers 2041894, 2138138,
2047260, 2343611, and 2143363. Any opinions, findings, and
conclusions or recommendations expressed in this material
are those of the author(s) and do not necessarily reflect the
views of the National Science Foundation. This work was
also supported in part by the Semiconductor Research Cor-
poration (SRC) and DARPA, the Agence Nationale de la
Recherche through the ANR-21-CE39-0019 FACADES and
the ProjetIA-22-PECY-0002 iPoP projects, and ANR MRSEI
TULIP (ANR-24-MRS0-0004), Inria DATA4US Exploratory
Action project.
Ethical Considerations
This work is a Systematization of Knowledge (SoK) on web
tracking. As such, it does not involve any data collection, user
studies, or measurement and deployment of tracking tech-
nologies. Instead, it systematizes developments in the field on
online tracking through research and industrial advancements
to identify gaps and open problems. Nevertheless, we discuss
the ethical implications of our work in shaping the future
research directions and influencing the involved stakeholders.
Stakeholder Analysis.Our work discusses six stakeholders:
(1)Online users: are individuals whose web activity may
be observed, inferred, or profiled using different tracking
mechanisms. (2)Browser vendors: are the developers of
browsers that mediate access to the web, while designing
and deploying technical countermeasures to balance privacy,
usability, performance, and compatibility. (3)Website
publishers: operate websites and monetize their content
by relying on analytics, personalization, and advertising,
while maintaining functionality under evolving privacy
constraints. (4)Advertising and tracking platforms: that
design and operate tracking infrastructures and are affected by
regulatory changes, browser policies, and public scrutiny. (5)
Regulators and policymakers: are responsible for enforcing
data protection and competition laws. They rely on accurate
technical understanding to craft effective and enforceable
regulation. (6)Research community: academic and industrial
researchers studying web tracking and privacy to understand,
measure, and defend against evolving tracking techniques.
Impact of the Research.Next, we list the positive and nega-
tive impacts of our research on different stakeholders.
Positive Impacts.(1)Improved Understanding (Impact on
Users, Regulators, and Researchers): By systematizing ad-
vances in tracking techniques, defenses, and measurement
methodologies, this work benefits users and regulators by
clarifying what forms of tracking are known, which ones are
mitigated, and which ones remain unresolved. This SoK also
serves as a unified source of knowledge for early career re-
searchers, users, and regulators to understand technicalities
of different tracking mechanisms. (2)Future Research Di-
rections (Impact on Researchers and Browser Vendors): Our
work identifies underexplored areas and open problems based
on advancements in tracking landscape allowing new as well
as established researchers to focus on important directions
of research to improve the state of web tracking rather than
making marginal improvements or working well-explored
problems. Similarly, it can also inform browser vendors to
anticipate emerging forms of web tracking and work towards
in-browser countermeasures. (3)Informing Platform and Pol-
icy Design (Impact on Browser Vendors and Regulators): By
synthesizing years of developments in web tracking, this SoK
informs browser vendors and policymakers about unintended
consequences and gaps in current approaches, while guiding
future policy changes—both browser-level as well as legal.
Negative Impacts.(1)Potential for Adversarial Use (Impact
on Users): This paper can inform motivated adversaries (i.e.,
trackers) to exploit the identified gaps in online tracking
research by deploying them within their tracking technologies
to circumvent existing protections. Identified open problems
may further motivate to make these mechanisms stealthier.
(2)Misinterpretation or Selective Use of Findings (Impact on
Policy): Industry or policy actors may selectively cite parts of
this SoK to justify particular technical or regulatory choices,
potentially oversimplifying nuanced trade-offs discussed in
the specific academic work in the literature.
Justification for Research.Despite these risks, we argue that
publishing this SoK is ethically justified and necessary. Web
tracking is already widely deployed at scale, often with lim-
ited transparency to users and regulators. The primary ethical
risk lies not in documenting this ecosystem, but in allow-
ing knowledge fragmentation or obscurity to persist. Several
factors mitigate the highlighted potential negative impacts.
First, this work does not introduce new tracking mechanisms,
datasets, or attack surfaces; it systematizes and critically eval-
uates information that is already publicly available on the
internet or published in the research literature. Second, by ex-
plicitly framing open problems, we aim to encourage research
14

that prioritizes user protection, accountability, and robustness
rather than exploitation. Finally, increased visibility into the
limitations of existing defenses and measurements enables
more informed decision-making by browser vendors, regula-
tors, and researchers, reducing the likelihood of misleading
claims about privacy guarantees. Overall, this SoK contributes
to an ethically grounded understanding of web tracking. By es-
tablishing what is known, what remains unsolved, and where
future research efforts are needed the most, this work supports
long-term improvements in web privacy that outweigh the
potential risks from systematizing this knowledge.
Open Science
The main artifact produced by our work includes the thematic
organization and categorization of the literature on web track-
ing identified as relevant in Section 3. As a result, we release
the code to obtain papers, keywords used to filter them as well
as the list of publications organized under tracking techniques,
defenses, and regulatory compliance along with the assigned
codes, annotations, and identified themes. Our artifacts can
be obtained at: https://osf.io/zsy7e/overview?view_
only=a346b98bf89244b5b17d842f6fb3fb13
Additionally, we maintain an extended and live version
of this SoK at https://github.com/privacysandstorm/
sok-advances-open-problems-web-tracking to pro-
vide more details on the concepts covered and enable reg-
ular updates based on ecosystem changes, new findings, and
community suggestions on our LATEX code repository.
References
[1] Gunes Acar, Steven Englehardt, and Arvind Narayanan.
No Boundaries: Data Exfiltration by Third Parties
Embedded on Web Pages.Proceedings on Privacy
Enhancing Technologies, 2020. https://doi.org/
10.2478/popets-2020-0070
[2] Gunes Acar, Christian Eubank, Steven Englehardt,
Marc Juarez, Arvind Narayanan, and Claudia Diaz.
The Web Never Forgets: Persistent Tracking Mech-
anisms in the Wild.In Proceedings of the 2014 ACM
SIGSAC Conference on Computer and Communica-
tions Security. 2014. https://doi.org/10.1145/
2660267.2660347
[3] Gunes Acar, Marc Juarez, Nick Nikiforakis, Claudia
Diaz, Seda Gürses, Frank Piessens, and Bart Preneel.
FPDetective: Dusting the Web for Fingerprinters.In
Proceedings of the 2013 ACM SIGSAC Conference on
Computer & Communications Security. 2013. https:
//doi.org/10.1145/2508859.2516674
[4] Mir Masood Ali, Binoy Chitale, Mohammad Ghasem-
isharif, Chris Kanich, Nick Nikiforakis, and Jason Po-
lakis. Navigating Murky Waters: Automated Browser
Feature Testing for Uncovering Tracking Vectors.
In Proceedings 2023 Network and Distributed Sys-
tem Security Symposium. 2023. https://doi.org/
10.14722/ndss.2023.24072
[5] Mir Masood Ali, Peter Snyder, Chris Kanich, and
Hamed Haddadi. Unbundle-Rewrite-Rebundle: Run-
time Detection and Rewriting of Privacy-Harming
Code in JavaScript Bundles.In Proceedings of the
2024 on ACM SIGSAC Conference on Computer and
Communications Security. 2024. https://doi.org/
10.1145/3658644.3690262
[6] Abdul Haddi Amjad, Shaoor Munir, Zubair Shafiq, and
Muhammad Ali Gulzar. Blocking Tracking JavaScript
at the Function Granularity.In Proceedings of the
2024 on ACM SIGSAC Conference on Computer and
Communications Security. 2024. https://doi.org/
10.1145/3658644.3670329
[7] Abdul Haddi Amjad, Danial Saleem, Muhammad Ali
Gulzar, Zubair Shafiq, and Fareed Zaffar. TrackerSift:
Untangling Mixed Tracking and Functional Web Re-
sources.In Proceedings of the 21st ACM Internet
Measurement Conference. 2021. https://doi.org/
10.1145/3487552.3487855
[8] Abdul Haddi Amjad, Zubair Shafiq, and Muham-
mad Ali Gulzar. Blocking JavaScript Without Break-
ing the Web: An Empirical Investigation.Proceedings
on Privacy Enhancing Technologies, 2023. https:
//doi.org/10.56553/popets-2023-0087
[9] Ashkan Soltani. Flash Cookies and Privacy II,
2011. https://ashkansoltani.org/2011/08/11/
respawn-redux-flash-cookies/
[10] Richard Atterer, Monika Wnuk, and Albrecht Schmidt.
Knowing the User’s Every Move: User Activity Track-
ing for Website Usability Evaluation and Implicit Inter-
action.In Proceedings of the 15th International Con-
ference on World Wide Web. 2006.https://doi.org/
10.1145/1135777.1135811
[11] Attorney General Becerra. #CCPA Requires Busi-
nesses to Treat a User-Enabled Global Privacy Con-
trol, 2021. https://x.com/AGBecerra/status/
1354850758236102656
[12] Mika D. Ayenson, Dietrich James Wambach, Ashkan
Soltani, Nathan Good, and Chris Jay Hoofnagle. Flash
Cookies and Privacy II: Now with HTML5 and ETag
Respawning, 2011. https://doi.org/10.2139/
ssrn.1898390
15

[13] Muhammad Abu Bakar Aziz and Christo Wilson.
Johnny Still Can’t Opt-out: Assessing the IAB CCPA
Compliance Framework.Proceedings on Privacy
Enhancing Technologies, 2024. https://doi.org/
10.56553/popets-2024-0120
[14] Michael Backes, Aniket Kate, Matteo Maffei, and Kim
Pecina. ObliviAd: Provably Secure and Practical On-
line Behavioral Advertising.In 2012 IEEE Symposium
on Security and Privacy. 2012. https://doi.org/
10.1109/SP.2012.25
[15] Pouneh Nikkhah Bahrami, Dylan Cutler, and Igor Bilo-
grevic. Byte by Byte: Unmasking Browser Finger-
printing at the Function Level Using V8 Bytecode
Transformers.In Proceedings of the 2025 ACM
SIGSAC Conference on Computer and Communica-
tions Security. 2025. https://doi.org/10.1145/
3719027.3765158
[16] Pouneh Nikkhah Bahrami, Umar Iqbal, and Zubair
Shafiq. FP-Radar: Longitudinal Measurement and
Early Detection of Browser Fingerprinting.Pro-
ceedings on Privacy Enhancing Technologies, 2022.
https://doi.org/10.2478/popets-2022-0056
[17] Muhammad Ahmad Bashir, Sajjad Arshad, Engin
Kirda, William Robertson, and Christo Wilson. How
Tracking Companies Circumvented Ad Blockers Us-
ing WebSockets.In Proceedings of the Internet Mea-
surement Conference 2018. 2018. https://doi.org/
10.1145/3278532.3278573
[18] Muhammad Ahmad Bashir, Sajjad Arshad, William
Robertson, and Christo Wilson. Tracing Information
Flows Between Ad Exchanges Using Retargeted Ads.
In 25th USENIX Security Symposium. 2016. https://
www.usenix.org/conference/usenixsecurity16/
technical-sessions/presentation/bashir
[19] Paschalis Bekos, Panagiotis Papadopoulos, Nicolas
Kourtellis, and Michalis Polychronakis. PIIxel Leaks:
Passive Identification of Personally Identifiable Infor-
mation Leakage through Meta Pixel.In Proceed-
ings of the 2025 ACM SIGSAC Conference on Com-
puter and Communications Security. 2025. https:
//doi.org/10.1145/3719027.3765113
[20] Paschalis Bekos, Panagiotis Papadopoulos, Evange-
los P. Markatos, and Nicolas Kourtellis. The Hitch-
hiker’s Guide to Facebook Web Tracking with Invisible
Pixels and Click IDs.In Proceedings of the ACM Web
Conference 2023. 2023. https://doi.org/10.1145/
3543507.3583311
[21] Robin Berjon. GPC under the GDPR, 2021. https:
//berjon.com/gpc-under-the-gdpr/
[22] Alex Berke and Dan Calacci. Privacy Limitations
of Interest-Based Advertising on The Web: A Post-
Mortem Empirical Analysis of Google’s FLoC.In
Proceedings of the 2022 ACM SIGSAC Conference
on Computer and Communications Security. 2022.
https://doi.org/10.1145/3548606.3560626
[23] Alex Berke, Badih Ghazi, Enrico Bacis, Pritish Kamath,
Ravi Kumar, Robin Lassonde, Pasin Manurangsi, and
Umar Syed. How Unique Is Whose Web Browser?
The Role of Demographics in Browser Fingerprinting
among US Users.Proceedings on Privacy Enhancing
Technologies, 2025. https://doi.org/10.56553/
popets-2025-0038
[24] Yohan Beugin, Paul Barford, and Patrick McDaniel.
Lessons from the Adoption and Deprecation of the
Privacy Sandbox Web APIs, 2026.https://doi.org/
10.48550/arXiv.2606.26390
[25] Yohan Beugin, Sam Dutton, Yana Dimova, Rowan
Merewood, and Barry Pollard. The 2024 Web Almanac:
Cookies. In The 2024 Web Almanac. 2024. https:
//almanac.httparchive.org/en/2024/cookies
[26] Yohan Beugin and Patrick McDaniel. Interest-
Disclosing Mechanisms for Advertising Are Privacy-
Exposing (Not Preserving).Proceedings on Privacy
Enhancing Technologies, 2024. https://doi.org/
10.56553/popets-2024-0004
[27] Yohan Beugin and Patrick McDaniel. A Public
and Reproducible Assessment of the Topics API on
Real Data.In IEEE Security and Privacy Work-
shops (SecWeb). 2024. https://doi.org/10.48550/
arXiv.2403.19577
[28] Yohan Beugin and Patrick McDaniel. Technical Re-
port: The Need for a (Research) Sandstorm through
the Privacy Sandbox, 2025. https://doi.org/
10.48550/arXiv.2512.03207
[29] Nataliia Bielova, Laura Litvine, Anysia Nguyen,
Mariam Chammat, Vincent Toubiana, and Es-
telle Hary. The Effect of Design Patterns on
(Present and Future) Cookie Consent Deci-
sions.In 33rd USENIX Security Symposium.
2024. https://www.usenix.org/conference/
usenixsecurity24/presentation/bielova
[30] Nataliia Bielova, Cristiana Santos, and Colin M Gray.
Two Worlds Apart! Closing the Gap between Regulat-
ing EU Consent and User Studies.Harvard Journal
of Law & Technology, 2024. https://hal.science/
hal-04913768/
16

[31] Eleanor Birrell, Jay Rodolitz, Angel Ding, Jenna Lee,
Emily McReynolds, Jevan Hutson, and Ada Lerner.
SoK: Technical Implementation and Human Impact of
Internet Privacy Regulations.In 2024 IEEE Symposium
on Security and Privacy. 2024. https://doi.org/
10.1109/SP54263.2024.00206
[32] Tom Biselli, Laura Utz, and Christian Reuter. Sup-
porting Informed Choices about Browser Cookies:
The Impact of Personalised Cookie Banners.Pro-
ceedings on Privacy Enhancing Technologies, 2024.
https://doi.org/10.56553/popets-2024-0011
[33] European Data Protection Board. Contribution
of the EDPB to the Report on the Application
of the GDPR under Article 97, 2023. https:
//www.edpb.europa.eu/our-work-tools/our-
documents/other/contribution-edpb-report-
application-gdpr-under-article-97-2023_en
[34] Dino Bollinger, Karel Kubicek, Carlos Cotrini,
and David Basin. Automating Cookie Con-
sent and GDPR Violation Detection.In
31st USENIX Security Symposium. 2022.
https://www.usenix.org/conference/
usenixsecurity22/presentation/bollinger
[35] Rob Bonta. Attorney General Bonta An-
nounces Settlement with Sephora as Part of
Ongoing Enforcement of CCPA, 2022. https:
//oag.ca.gov/news/press-releases/attorney-
general-bonta-announces-settlement-
sephora-part-ongoing-enforcement
[36] Ahmed Bouhoula, Karel Kubicek, Amit Zac,
Carlos Cotrini, and David Basin. Automated
Large-Scale Analysis of Cookie Notice Com-
pliance.In 33rd USENIX Security Symposium.
2024. https://www.usenix.org/conference/
usenixsecurity24/presentation/bouhoula
[37] Soumaya Boussaha, Lukas Hock, Miguel Bermejo,
Ruben Cuevas Rumin, Angel Cuevas Rumin, David
Klein, Martin Johns, Luca Compagna, Daniele Anto-
nioli, and Thomas Barber. FP-Tracer: Fine-Grained
Browser Fingerprinting Detection via Taint-Tracking
and Entropy-Based Thresholds.Proceedings on
Privacy Enhancing Technologies, 2024. https://
doi.org/10.56553/popets-2024-0092
[38] Luís T. A. N. Brandão, Nicolas Christin, George
Danezis, and Anonymous. Toward Mending Two
Nation-Scale Brokered Identification Systems.Pro-
ceedings on Privacy Enhancing Technologies, 2015.
https://doi.org/10.1515/popets-2015-0022
[39] Virginia Braun and Victoria Clarke. Successful Quali-
tative Research: A Practical Guide for Beginners. 2013.
ISBN 978-1-84787-581-5
[40] Brave. Privacy Protection & Security Features. https:
//brave.com/privacy-features/
[41] Justin Brookman, Phoebe Rouge, Aaron Alva, and
Christina Yeung. Cross-Device Tracking: Measure-
ment and Disclosures.Proceedings on Privacy Enhanc-
ing Technologies, 2017. https://doi.org/10.1515/
popets-2017-0020
[42] Tomasz Bujlow, Valentín Carela-Español, Josep Solé-
Pareta, and Pere Barlet-Ros. A Survey on Web
Tracking: Mechanisms, Implications, and Defenses.
Proceedings of the IEEE, 2017. https://doi.org/
10.1109/JPROC.2016.2637878
[43] Simon Byers, Lorrie Faith Cranor, Dave Kormann, and
Patrick McDaniel. Searching for Privacy: Design and
Implementation of a P3P-Enabled Search Engine. In
Privacy Enhancing Technologies. 2005. https://
doi.org/10.1007/11423409_20
[44] Giuseppe Calderonio, Mir Masood Ali, and
Jason Polakis. Fledging Will Continue Un-
til Privacy Improves: Empirical Analysis of
Google’s Privacy-Preserving Targeted Adver-
tising.In 33rd USENIX Security Symposium.
2024. https://www.usenix.org/conference/
usenixsecurity24/presentation/calderonio
[45] Yinzhi Cao, Song Li, and Erik Wijmans. (Cross-
)Browser Fingerprinting via OS and Hardware Level
Features.In Proceedings 2017 Network and Dis-
tributed System Security Symposium. 2017. https:
//doi.org/10.14722/ndss.2017.23152
[46] Caudio Carpineto, Davide Lo Re, and Giovanni Ro-
mano. Automatic Assessment of Website Compliance
to the European Cookie Law with CooLCheck.In Pro-
ceedings of the 2016 ACM on Workshop on Privacy
in the Electronic Society. 2016. https://doi.org/
10.1145/2994620.2994622
[47] Shekhar Chalise, Hoang Dai Nguyen, and Phani
Vadrevu. Your Speaker or My Snooper?: Measuring
the Effectiveness of Web Audio Browser Fingerprints.
In Proceedings of the 22nd ACM Internet Measure-
ment Conference. 2022. https://doi.org/10.1145/
3517745.3561435
[48] Jan Charatan and Eleanor Birrell. Two Steps For-
ward and One Step Back: The Right to Opt-out of
Sale under CPRA.Proceedings on Privacy Enhancing
Technologies, 2024. https://doi.org/10.56553/
popets-2024-0042
17

[49] Anthony Chavez. A New Path for Privacy Sandbox
on the Web, 2024. https://privacysandbox.com/
news/privacy-sandbox-update
[50] Anthony Chavez. Update on Plans for Pri-
vacy Sandbox Technologies, 2025. https:
//privacysandbox.google.com/blog/update-
on-plans-for-privacy-sandbox-technologies
[51] Saiid El Hajj Chehade, Ben Stock, and Carmela Tron-
coso. Double-Edged Shield: On the Fingerprintability
of Customized Ad Blockers.In 34th USENIX Security
Symposium. 2025. https://www.usenix.org/
conference/usenixsecurity25/presentation/
el-hajj-chehade
[52] Baiqi Chen, Jiawei Lyu, Tingmin Wu, Mohan
Baruwal Chhetri, and Guangdong Bai. Semantics-
Aware Cookie Purpose Compliance.In Proceedings
of the ACM on Web Conference 2025. 2025. https:
//doi.org/10.1145/3696410.3714746
[53] Baiyu Chen, Benjamin Tag, Hao Xue, Daniel Angus,
and Flora Salim. When Ads Become Profiles: Un-
covering the Invisible Risk of Web Advertising at
Scale with LLMs.In Proceedings of the ACM Web
Conference 2026. 2026. https://doi.org/10.1145/
3774904.3793060
[54] Quan Chen, Panagiotis Ilia, Michalis Polychronakis,
and Alexandros Kapravelos. Cookie Swap Party: Abus-
ing First-Party Cookies for Web Tracking.In Pro-
ceedings of the Web Conference 2021. 2021. https:
//doi.org/10.1145/3442381.3449837
[55] Quan Chen and Alexandros Kapravelos. Mys-
tique: Uncovering Information Leakage from Browser
Extensions.In Proceedings of the 2018 ACM
SIGSAC Conference on Computer and Communica-
tions Security. 2018. https://doi.org/10.1145/
3243734.3243823
[56] Quan Chen, Peter Snyder, Ben Livshits, and Alexan-
dros Kapravelos. Detecting Filter List Evasion with
Event-Loop-Turn Granularity JavaScript Signatures.In
2021 IEEE Symposium on Security and Privacy. 2021.
https://doi.org/10.1109/SP40001.2021.00007
[57] Shuo Chen, Rui Wang, XiaoFeng Wang, and Kehuan
Zhang. Side-Channel Leaks in Web Applications: A
Reality Today, a Challenge Tomorrow.In 2010 IEEE
Symposium on Security and Privacy. 2010. https:
//doi.org/10.1109/SP.2010.20
[58] California Code. BPC 22575, 2003.
https://leginfo.legislature.ca.gov/faces/
codes_displaySection.xhtml?lawCode=
BPC&sectionNum=22575
[59] Colorado Department of Law. Universal Opt-Out
Shortlist, 2024.https://coag.gov/uoom/
[60] L. Cranor, S. Byers, and David P. Kormann. An Anal-
ysis of P3P Deployment on Commercial, Government,
and Children’s Web Sites as of May 2003.In Fed-
eral Trade Commission Workshop on Technologies
for Protecting Personal Information. 2003. https://
lorrie.cranor.org/pubs/p3p-census-may03.pdf
[61] Lorrie Cranor, Brooks Dobbs, Serge Egelman, Giles
Hogben, Jack Humphrey, Marc Langheinrich, Mas-
simo Marchiori, Martin Presler-Marshall, Joseph Rea-
gle, Matthias Schunter, David Stampley, and Rigo
Wenning. The Platform for Privacy Preferences 1.1
(P3P1.1) Specification, 2006. https://www.w3.org/
TR/P3P11/
[62] Lorrie Cranor, Marc Langheinrich, Massimo Marchiori,
Martin Presler-Marshall, and Joseph Reagle. The Plat-
form for Privacy Preferences 1.0 (P3P1.0) Specifica-
tion, 2002.https://www.w3.org/TR/P3P/
[63] Lorrie Faith Cranor, Manjula Arjula, and Praveen
Guduru. Use of a P3P User Agent by Early Adopters.
In Proceedings of the 2002 ACM Workshop on Privacy
in the Electronic Society. 2002. https://doi.org/
10.1145/644527.644528
[64] Kyle Crichton, Lorrie Faith Cranor, and Nicolas
Christin. Rethinking Fingerprinting: An Assessment of
Behavior-Based Methods at Scale and Implications for
Web Tracking.Proceedings on Privacy Enhancing
Technologies, 2025. https://doi.org/10.56553/
popets-2025-0158
[65] Luke Crouch. Improving Privacy without Breaking
the Web, 2018. https://blog.mozilla.org/
data/2018/01/26/improving-privacy-without-
breaking-the-web
[66] Hao Cui, Rahmadi Trimananda, and Athina
Markopoulou. Understanding Privacy
Norms through Web Forms.Proceedings
on Privacy Enhancing Technologies, 2025.
https://doi.org/10.56553/popets-2025-0002
[67] Anupam Das, Gunes Acar, Nikita Borisov, and Amogh
Pradeep. The Web’s Sixth Sense: A Study of Scripts
Accessing Smartphone Sensors.In Proceedings of
the 2018 ACM SIGSAC Conference on Computer and
Communications Security. 2018. https://doi.org/
10.1145/3243734.3243860
[68] Anupam Das, Nikita Borisov, and Matthew Caesar.
Tracking Mobile Web Users Through Motion Sensors:
Attacks and Defenses.In Proceedings 2016 Network
18

and Distributed System Security Symposium. 2016.
https://doi.org/10.14722/ndss.2016.23390
[69] Anupam Das, Nikita Borisov, and Edward Chou. Ev-
ery Move You Make: Exploring Practical Issues in
Smartphone Motion Sensor Fingerprinting and Coun-
termeasures.Proceedings on Privacy Enhancing Tech-
nologies, 2018. https://doi.org/10.1515/popets-
2018-0005
[70] Amit Datta, Jianan Lu, and Michael Carl
Tschantz. Evaluating Anti-Fingerprinting
Privacy Enhancing Technologies.In The
World Wide Web Conference. 2019. https:
//doi.org/10.1145/3308558.3313703
[71] Autorité de la concurrence. The Autorité de La Con-
currence Imposes a Fine of C150,000,000 on Apple
for the Implementation of the “ATT” Framework, 2025.
https://www.autoritedelaconcurrence.fr/
en/press-release/targeted-advertising-
autorite-de-la-concurrence-imposes-fine-
eu150000000-apple
[72] Nurullah Demir, Tobias Urban, Norbert Pohlmann,
and Christian Wressnegger. A Large-Scale Study of
Cookie Banner Interaction Tools and Their Impact on
Users’ Privacy.Proceedings on Privacy Enhancing
Technologies, 2024. https://doi.org/10.56553/
popets-2024-0002
[73] Clemens Deuser, Steffen Passmann, and Thorsten
Strufe. Browsing Unicity: On the Limits of Anonymiz-
ing Web Tracking Data.In 2020 IEEE Symposium
on Security and Privacy. 2020. https://doi.org/
10.1109/SP40000.2020.00018
[74] Mariano Di Martino, Isaac Meers, Peter Quax, Ken
Andries, and Wim Lamotte. Revisiting Identifica-
tion Issues in GDPR ‘Right Of Access’ Policies: A
Technical and Longitudinal Analysis.Proceedings
on Privacy Enhancing Technologies, 2022. https:
//doi.org/10.2478/popets-2022-0037
[75] Yana Dimova, Gunes Acar, Lukasz Olejnik, Wouter
Joosen, and Tom Van Goethem. The CNAME of the
Game: Large-Scale Analysis of DNS-Based Tracking
Evasion.Proceedings on Privacy Enhancing Tech-
nologies, 2021. https://doi.org/10.2478/popets-
2021-0053
[76] Yana Dimova, Tom Van Goethem, and Wouter Joosen.
Everybody’s Looking for SSOmething: A Large-Scale
Evaluation on the Privacy of OAuth Authentication
on the Web.Proceedings on Privacy Enhancing
Technologies, 2023. https://doi.org/10.56553/
popets-2023-0119
[77] Nick Doty. Mitigating Browser Fingerprinting in
Web Specifications, 2019. https://www.w3.org/TR/
fingerprinting-guidance/
[78] Peter Eckersley. How Unique Is Your Web Browser?
In Privacy Enhancing Technologies. 2010. https:
//doi.org/10.1007/978-3-642-14527-8_1
[79] Steven Englehardt.Automated Discovery of Privacy
Violations on the Web. Ph.D. thesis, Princeton Uni-
versity, 2018. https://arks.princeton.edu/ark:
/88435/dsp01hq37vr346
[80] Steven Englehardt. No Boundaries for Cre-
dentials: New Password Leaks to Mixpanel
and Session Replay Companies, 2018. https:
//freedom-to-tinker.com/2018/02/26/no-
boundaries-for-credentials-password-leaks-
to-mixpanel-and-session-replay-companies/
[81] Steven Englehardt. Firefox 72 Blocks
Third-Party Fingerprinting Resources, 2020.
https://blog.mozilla.org/security/2020/
01/07/firefox-72-fingerprinting
[82] Steven Englehardt, Jeffrey Han, and Arvind Narayanan.
I Never Signed up for This! Privacy Implications of
Email Tracking.Proceedings on Privacy Enhanc-
ing Technologies, 2018. https://doi.org/10.1515/
popets-2018-0006
[83] Steven Englehardt and Arvind Narayanan. Online
Tracking: A 1-Million-Site Measurement and Anal-
ysis.In Proceedings of the 2016 ACM SIGSAC Confer-
ence on Computer and Communications Security. 2016.
https://doi.org/10.1145/2976749.2978313
[84] Tatiana Ermakova, Benjamin Fabian, Benedict Ben-
der, and Kerstin Klimek. Web Tracking - A Liter-
ature Review on the State of Research.In Hawaii
International Conference on System Sciences. 2018.
https://doi.org/10.24251/HICSS.2018.596
[85] Edward W. Felten and Michael A. Schneider. Tim-
ing Attacks on Web Privacy.In Proceedings of the
7th ACM Conference on Computer and Communica-
tions Security. 2000. https://doi.org/10.1145/
352600.352606
[86] Ellis Fenske, Dane Brown, Jeremy Martin, Travis May-
berry, Peter Ryan, and Erik Rye. Three Years Later:
A Study of MAC Address Randomization In Mo-
bile Devices And When It Succeeds.Proceedings
on Privacy Enhancing Technologies, 2021. https:
//doi.org/10.2478/popets-2021-0042
19

[87] Hossein Fereidooni, Jan Koenig, Phillip Rieger, Marco
Chilese, Bora Goekbakan, Moritz Finke, Alexandra
Dmitrienko, and Ahmad-Reza Sadeghi. Authen-
tiSense: A Scalable Behavioral Biometrics Authen-
tication Scheme Using Few-Shot Learning for Mobile
Platforms.In Proceedings 2023 Network and Dis-
tributed System Security Symposium. 2023. https:
//doi.org/10.14722/ndss.2023.23194
[88] Daniel Fett, Ralf Küsters, and Guido Schmitz.
SPRESSO: A Secure, Privacy-Respecting Single Sign-
On System for the Web.In Proceedings of the 22nd
ACM SIGSAC Conference on Computer and Communi-
cations Security. 2015. https://doi.org/10.1145/
2810103.2813726
[89] Roy Fielding and David Singer. Tracking Preference
Expression (DNT), 2019. https://www.w3.org/TR/
tracking-dnt/
[90] Lucas Foppe, Jeremy Martin, Travis Mayberry, Erik C.
Rye, and Lamont Brown. Exploiting TLS Client
Authentication for Widespread User Tracking.Pro-
ceedings on Privacy Enhancing Technologies, 2018.
https://doi.org/10.1515/popets-2018-0031
[91] Imane Fouad, Nataliia Bielova, Arnaud Legout, and
Natasa Sarafijanovic-Djukic. Missed by Filter Lists:
Detecting Unknown Third-Party Trackers with Invisi-
ble Pixels.Proceedings on Privacy Enhancing Tech-
nologies, 2020. https://doi.org/10.2478/popets-
2020-0038
[92] Imane Fouad, Cristiana Santos, and Pierre Laperdrix.
The Devil Is in the Details: Detection, Measurement
and Lawfulness of Server-Side Tracking on the Web.
Proceedings on Privacy Enhancing Technologies, 2024.
https://doi.org/10.56553/popets-2024-0125
[93] Imane Fouad, Cristiana Santos, Arnaud Legout, and
Nataliia Bielova. My Cookie Is a Phoenix: Detection,
Measurement, and Lawfulness of Cookie Respawning
with Browser Fingerprinting.Proceedings on Privacy
Enhancing Technologies, 2022. https://doi.org/
10.56553/popets-2022-0063
[94] Asmaa El Fraihi, Nardjes Amieur, Walter Rudametkin,
and Oana Goga. Client-Side and Server-Side Tracking
on Meta: Effectiveness and Accuracy.Proceedings
on Privacy Enhancing Technologies, 2024. https:
//doi.org/10.56553/popets-2024-0086
[95] Gertjan Franken, Tom Van Goethem, and Wouter
Joosen. Who Left Open the Cookie Jar?
A Comprehensive Evaluation of Third-Party
Cookie Policies.In Proceedings of the 27th
USENIX Conference on Security Symposium.
2018. https://www.usenix.org/conference/
usenixsecurity18/presentation/franken
[96] Abdullah Ghani, Yash Vekaria, and Zubair Shafiq. Pix-
elConfig: Longitudinal Measurement and Reverse-
Engineering of Meta Pixel Configurations, 2026.
https://doi.org/10.48550/arXiv.2603.09380
[97] Mohammad Ghasemisharif and Jason Polakis. Read
Between the Lines: Detecting Tracking JavaScript with
Bytecode Classification.In Proceedings of the 2023
ACM SIGSAC Conference on Computer and Communi-
cations Security. 2023. https://doi.org/10.1145/
3576915.3616637
[98] Oana Goga, Howard Lei, Sree Hari Krishnan
Parthasarathi, Gerald Friedland, Robin Sommer, and
Renata Teixeira. Exploiting Innocuous Activ-
ity for Correlating Users across Sites.In Pro-
ceedings of the 22nd International Conference on
World Wide Web. 2013. https://doi.org/10.1145/
2488388.2488428
[99] Alejandro Gómez-Boix, Pierre Laperdrix, and Benoit
Baudry. Hiding in the Crowd: An Analysis of
the Effectiveness of Browser Fingerprinting at Large
Scale.In Proceedings of the 2018 World Wide
Web Conference. 2018. https://doi.org/10.1145/
3178876.3186097
[100] Roberto Gonzalez, Claudio Soriente, and Nikolaos
Laoutaris. User Profiling in the Time of HTTPS.
In Proceedings of the 2016 Internet Measurement
Conference. 2016. https://doi.org/10.1145/
2987443.2987451
[101] Google. Global Privacy Control - Chrome Platform Sta-
tus, 2025. https://chromestatus.com/feature/
5137324344213504
[102] Colin M. Gray, Cristiana Santos, Nataliia Bielova,
Michael Toth, and Damian Clifford. Dark Patterns
and the Legal Requirements of Consent Banners: An
Interaction Criticism Perspective.In Proceedings of
the 2021 CHI Conference on Human Factors in Com-
puting Systems. 2021. https://doi.org/10.1145/
3411764.3445779
[103] Rachid Youssef Grib, Alberto Verna, Nikhil Jha, Mar-
tino Trevisan, and Marco Mellia. The Rise and Fall of
Google’s Privacy Sandbox, 2026. https://doi.org/
10.48550/arXiv.2607.00693
[104] Privacy Community Group. Client-Side Storage
Partitioning, 2022. https://privacycg.github.io/
storage-partitioning/
20

[105] David Gugelmann, Markus Happe, Bernhard Ager, and
Vincent Lenders. An Automated Approach for Com-
plementing Ad Blockers’ Blacklists.Proceedings
on Privacy Enhancing Technologies, 2015. https:
//doi.org/10.1515/popets-2015-0018
[106] Saikat Guha, Bin Cheng, and Paul Francis. Privad:
Practical Privacy in Online Advertising.In Proceed-
ings of the 8th USENIX Conference on Networked
Systems Design and Implementation. 2011. https:
//doi.org/10.5555/1972457.1972475
[107] Saiid El Hajj Chehade, Sandra Siby, and Carmela
Troncoso. SINBAD: Saliency-Informed Detection
of Breakage Caused by Ad Blocking.In 2024 IEEE
Symposium on Security and Privacy. 2024. https:
//doi.org/10.1109/SP54263.2024.00199
[108] James Hercher. The W3C Ad Privacy Group Taking
The Little-Engine-That-Could Path To Success, 2022.
https://www.adexchanger.com/ad-exchange-
news/the-w3c-ad-privacy-group-taking-the-
little-engine-that-could-path-to-success/
[109] Maximilian Hils, Daniel W. Woods, and Rainer Böhme.
Measuring the Emergence of Consent Management on
the Web.In Proceedings of the ACM Internet Measure-
ment Conference. 2020. https://doi.org/10.1145/
3419394.3423647
[110] Maximilian Hils, Daniel W. Woods, and Rainer Böhme.
Privacy Preference Signals: Past, Present and Future.
Proceedings on Privacy Enhancing Technologies, 2021.
https://doi.org/10.2478/popets-2021-0069
[111] Kyle Hogan, Alishah Chator, Gabriel Kaptchuk,
Mayank Varia, and Srinivas Devadas. Making Sense of
Private Advertising: A Principled Approach to a Com-
plex Ecosystem.Proceedings on Privacy Enhancing
Technologies, 2026. https://doi.org/10.56553/
popets-2026-0023
[112] Henry Hosseini, Christine Utz, Martin Degeling, and
Thomas Hupperich. A Bilingual Longitudinal Analy-
sis of Privacy Policies Measuring the Impacts of the
GDPR and the CCPA/CPRA.Proceedings on Privacy
Enhancing Technologies, 2024. https://doi.org/
10.56553/popets-2024-0058
[113] Hang Hu, Peng Peng, and Gang Wang. Characteriz-
ing Pixel Tracking through the Lens of Disposable
Email Services.In 2019 IEEE Symposium on Secu-
rity and Privacy. 2019. https://doi.org/10.1109/
SP.2019.00033
[114] Tim Huang. 1816056 - (Fp-Randomization)
[Meta] Implement Fingerprinting Randomization Sys-
tem, 2023. https://bugzilla.mozilla.org/show_
bug.cgi?id=1816056
[115] François Hublet, David Basin, and Sr ¯dan Krsti´c. User-
Controlled Privacy: Taint, Track, and Control.Pro-
ceedings on Privacy Enhancing Technologies, 2024.
https://doi.org/10.56553/popets-2024-0034
[116] Maxime Huyghe, Walter Rudametkin, and Clément
Quinton. FP-Rainbow: Fingerprint-Based Browser
Configuration Identification.In Proceedings of the
ACM on Web Conference 2025. 2025. https://
doi.org/10.1145/3696410.3714699
[117] Muhammad Ikram, Hassan Jameel Asghar, Mo-
hamed Ali Kaafar, Anirban Mahanti, and Balachan-
dar Krishnamurthy. Towards Seamless Tracking-Free
Web: Improved Detection of Trackers via One-Class
Learning.Proceedings on Privacy Enhancing Tech-
nologies, 2017. https://doi.org/10.1515/popets-
2017-0006
[118] Umar Iqbal, Steven Englehardt, and Zubair Shafiq.
Fingerprinting the Fingerprinters: Learning to Detect
Browser Fingerprinting Behaviors.In 2021 IEEE
Symposium on Security and Privacy. 2021. https:
//doi.org/10.1109/SP40001.2021.00017
[119] Umar Iqbal, Peter Snyder, Shitong Zhu, Benjamin
Livshits, Zhiyun Qian, and Zubair Shafiq. AdGraph: A
Graph-Based Approach to Ad and Tracker Blocking.In
2020 IEEE Symposium on Security and Privacy. 2020.
https://doi.org/10.1109/SP40000.2020.00005
[120] Umar Iqbal, Charlie Wolfe, Charles Nguyen,
Steven Englehardt, and Zubair Shafiq. Khaleesi:
Breaker of Advertising and Tracking Request
Chains.In 31st USENIX Security Symposium.
2022. https://www.usenix.org/conference/
usenixsecurity22/presentation/iqbal
[121] Collin Jackson, Andrew Bortz, Dan Boneh, and John C.
Mitchell. Protecting Browser State from Web Pri-
vacy Attacks.In Proceedings of the 15th Interna-
tional Conference on World Wide Web. 2006.https:
//doi.org/10.1145/1135777.1135884
[122] Sakshi Jain, Mobin Javed, and Vern Paxson. Towards
Mining Latent Client Identifiers from Network Traffic.
Proceedings on Privacy Enhancing Technologies, 2016.
https://doi.org/10.1515/popets-2016-0007
[123] Suman Jana and Vitaly Shmatikov. Memento: Learn-
ing Secrets from Process Footprints.In 2012 IEEE
Symposium on Security and Privacy. 2012. https:
//doi.org/10.1109/SP.2012.19
21

[124] Muhammad Jazlan, Alexander Gamero-Garrido,
Zubair Shafiq, and Yash Vekaria. SST-
Guard: Detecting and Characterizing Server-
Side Google Analytics in the Wild, 2026.
https://doi.org/10.48550/arXiv.2604.27497
[125] Muhammad Jazlan, Ethan Wang, Yash Vekaria, and
Zubair Shafiq. Tracking Conversations: Measuring
Content and Identity Exposure on AI Chatbots, 2026.
https://doi.org/10.48550/arXiv.2604.27438
[126] Nikhil Jha, Martino Trevisan, Emilio Leonardi, and
Marco Mellia. On the Robustness of Topics API to
a Re-Identification Attack.Proceedings on Privacy
Enhancing Technologies, 2023. https://doi.org/
10.56553/popets-2023-0098
[127] Zihao Jin, Ziqiao Kong, Shuo Chen, and Haixin Duan.
Timing-Based Browsing Privacy Vulnerabilities Via
Site Isolation.In 2022 IEEE Symposium on Secu-
rity and Privacy. 2022. https://doi.org/10.1109/
SP46214.2022.9833710
[128] Peter C. Johnson, Apu Kapadia, Patrick P. Tsang,
and Sean W. Smith. Nymble: Anonymous IP-
Address Blocking. In Privacy Enhancing Technolo-
gies. 2007. https://doi.org/10.1007/978-3-540-
75551-7_8
[129] Scott Jordan, Yoshimichi Nakatsuka, Ercan Ozturk,
Andrew Paverd, and Gene Tsudik. VICEROY: GDPR-
/CCPA-Compliant Enforcement of Verifiable Account-
less Consumer Requests.In Proceedings 2023 Network
and Distributed System Security Symposium. 2023.
https://doi.org/10.14722/ndss.2023.23074
[130] Andrew J. Kaizer and Minaxi Gupta. Characterizing
Website Behaviors Across Logged-in and Not-Logged-
in Users.In Proceedings of the 2016 Internet Measure-
ment Conference. 2016. https://doi.org/10.1145/
2987443.2987450
[131] Faezeh Kalantari, Mehrnoosh Zaeifi, Yeganeh Safaei,
Marzieh Bitaab, Adam Oest, Gianluca Stringhini,
Yan Shoshitaishvili, and Adam Doupé. BROWSER
POLYGRAPH: Efficient Deployment of Coarse-Grained
Browser Fingerprints for Web-Scale Detection of
Fraud Browsers.In Proceedings of the 2024 ACM
on Internet Measurement Conference. 2024. https:
//doi.org/10.1145/3646547.3688455
[132] Samy Kamkar. Samy Kamkar - Evercookie - Vir-
tually Irrevocable Persistent Cookies, 2010. https:
//samy.pl/evercookie/
[133] Gayatri Priyadarsini Kancherla, Nataliia Bielova, Cris-
tiana Santos, and Abhishek Bichhawat. Johnny Can’t
Revoke Consent Either: Measuring Compliance of
Consent Revocation on the Web.Proceedings on
Privacy Enhancing Technologies Symposium, 2025.
https://doi.org/10.56553/popets-2025-0133
[134] Rahul Kanyal and Smruti R. Sarangi. PanoptiChrome:
A Modern In-Browser Taint Analysis Framework.In
Proceedings of the ACM Web Conference 2024. 2024.
https://doi.org/10.1145/3589334.3645699
[135] Arjaldo Karaj, Sam Macbeth, Rémi Berson, and
Josep M. Pujol. WhoTracks .Me: Shedding Light on
the Opaque World of Online Tracking, 2019. http:
//arxiv.org/abs/1804.08959
[136] Soroush Karami, Panagiotis Ilia, Konstantinos Solo-
mos, and Jason Polakis. Carnus: Exploring the Privacy
Threats of Browser Extension Fingerprinting.In Pro-
ceedings 2020 Network and Distributed System Secu-
rity Symposium. 2020. https://doi.org/10.14722/
ndss.2020.24383
[137] Soroush Karami, Faezeh Kalantari, Mehrnoosh Za-
eifi, Xavier J. Maso, Erik Trickel, Panagiotis Ilia,
Yan Shoshitaishvili, Adam Doupé, and Jason Po-
lakis. Unleash the Simulacrum: Shifting Browser
Realities for Robust Extension-Fingerprinting Pre-
vention.In 31st USENIX Security Symposium.
2022. https://www.usenix.org/conference/
usenixsecurity22/presentation/karami
[138] Ben Kelly and Brian Lefler. Bounce Tracking
Mitigations Explainer, 2022. https://github.com/
privacycg/nav-tracking-mitigations/blob/
main/bounce-tracking-explainer.md
[139] Soheil Khodayari and Giancarlo Pellegrino. The State
of the SameSite: Studying the Usage, Effectiveness,
and Adequacy of SameSite Cookies.In 2022 IEEE
Symposium on Security and Privacy. 2022. https:
//doi.org/10.1109/SP46214.2022.9833637
[140] Julia B. Kieserman, Athanasios Andreou, Chris Geeng,
Tobias Lauinger, and Damon McCoy. Tracker In-
stallations Are Not Created Equal: Understanding
Tracker Configuration of Form Data Collection.Pro-
ceedings on Privacy Enhancing Technologies, 2025.
https://doi.org/10.56553/popets-2025-0151
[141] Amit Klein. Cross Layer Attacks and How to Use
Them (for DNS Cache Poisoning, Device Tracking
and More).In 2021 IEEE Symposium on Secu-
rity and Privacy. 2021. https://doi.org/10.1109/
SP40001.2021.00054
[142] Amit Klein and Benny Pinkas. DNS Cache-Based
User Tracking.In Proceedings 2019 Network and
22

Distributed System Security Symposium. 2019. https:
//doi.org/10.14722/ndss.2019.23186
[143] David Klein, Benny Rolle, Thomas Barber, Manuel
Karl, and Martin Johns. General Data Protection Run-
time: Enforcing Transparent GDPR Compliance for
Existing Applications.In Proceedings of the 2023
ACM SIGSAC Conference on Computer and Communi-
cations Security. 2023. https://doi.org/10.1145/
3576915.3616604
[144] Jeff Kline, Paul Barford, Aaron Cahn, and Joel Som-
mers. On the Structure and Characteristics of User
Agent String.In Proceedings of the 2017 Internet
Measurement Conference. 2017. https://doi.org/
10.1145/3131365.3131406
[145] Alexander Klink. 1334485 - Tracking Us-
ing Intermediate CA Caching, 2017. https:
//bugzilla.mozilla.org/show_bug.cgi?id=
1334485
[146] Lukas Knittel, Christian Mainka, Marcus Niemietz,
Dominik Trevor Noß, and Jörg Schwenk. XSina-
tor.Com: From a Formal Model to the Automatic
Evaluation of Cross-Site Leaks in Web Browsers.In
Proceedings of the 2021 ACM SIGSAC Conference
on Computer and Communications Security. 2021.
https://doi.org/10.1145/3460120.3484739
[147] Simon Koch, Manuel Karl, Robin Kirchner, Malte
Wessels, Anne Paschke, and Martin Johns. The Im-
pact of Default Mobile SDK Usage on Privacy and
Data Protection.Proceedings on Privacy Enhancing
Technologies, 2025. https://doi.org/10.56553/
popets-2025-0042
[148] T. Kohno, A. Broido, and K. Claffy. Remote Physi-
cal Device Fingerprinting.In 2005 IEEE Symposium
on Security and Privacy. 2005. https://doi.org/
10.1109/SP.2005.18
[149] Moshe Kol, Amit Klein, and Yossi Gilad. Device
Tracking via Linux’s New TCP Source Port Selec-
tion Algorithm.In 32nd USENIX Security Symposium.
2023. https://www.usenix.org/conference/
usenixsecurity23/presentation/kol
[150] Martin Koop, Erik Tews, and Stefan Katzenbeisser. In-
Depth Evaluation of Redirect Tracking and Link Usage.
Proceedings on Privacy Enhancing Technologies, 2020.
https://doi.org/10.2478/popets-2020-0079
[151] Balachander Krishnamurthy and Craig Wills. Privacy
Diffusion on the Web: A Longitudinal Perspective.In
Proceedings of the 18th International Conference on
World Wide Web. 2009. https://doi.org/10.1145/
1526709.1526782
[152] David M. Kristol. HTTP Cookies: Standards, Pri-
vacy, and Politics.ACM Transactions on Inter-
net Technology, 2001. https://doi.org/10.1145/
502152.502153
[153] Lin Kyi, Sushil Ammanaghatta Shivakumar, Cris-
tiana Teixeira Santos, Franziska Roesner, Frederike
Zufall, and Asia J. Biega. Investigating Deceptive De-
sign in GDPR’s Legitimate Interest.In Proceedings of
the 2023 CHI Conference on Human Factors in Com-
puting Systems. 2023. https://doi.org/10.1145/
3544548.3580637
[154] Tomer Laor, Naif Mehanna, Antonin Durey, Vitaly
Dyadyuk, Pierre Laperdrix, Clémentine Maurice, Yossi
Oren, Romain Rouvoy, Walter Rudametkin, and Yuval
Yarom. DRAWN APART : A Device Identification
Technique Based on Remote GPU Fingerprinting.Pro-
ceedings 2022 Network and Distributed System Secu-
rity Symposium, 2022. https://doi.org/10.14722/
ndss.2022.24093
[155] Pierre Laperdrix, Nataliia Bielova, Benoit Baudry,
and Gildas Avoine. Browser Fingerprinting: A Sur-
vey.ACM Transactions on the Web, 2020. https:
//doi.org/10.1145/3386040
[156] Pierre Laperdrix, Walter Rudametkin, and Benoit
Baudry. Beauty and the Beast: Diverting Modern Web
Browsers to Build Unique Browser Fingerprints.In
2016 IEEE Symposium on Security and Privacy. 2016.
https://doi.org/10.1109/SP.2016.57
[157] Pierre Laperdrix, Oleksii Starov, Quan Chen, Alexan-
dros Kapravelos, and Nick Nikiforakis. Fingerprinting
in Style: Detecting Browser Extensions via Injected
Style Sheets.In 30th USENIX Security Symposium.
2021. https://www.usenix.org/conference/
usenixsecurity21/presentation/laperdrix
[158] Brad Lassey. Mikewest/Privacy-Budget, 2019. https:
//github.com/mikewest/privacy-budget
[159] Hieu Le, Salma Elmalaki, Athina Markopoulou,
and Zubair Shafiq. AutoFR: Automated Fil-
ter Rule Generation for Adblocking.In
32nd USENIX Security Symposium. 2023.
https://www.usenix.org/conference/
usenixsecurity23/presentation/le
[160] Hieu Le, Athina Markopoulou, and Zubair Shafiq. CV-
Inspector: Towards Automating Detection of Adblock
Circumvention.In Proceedings 2021 Network and
Distributed System Security Symposium. 2021. https:
//doi.org/10.14722/ndss.2021.24055
23

[161] Changmin Lee and Sooel Son. AdCPG: Classifying
JavaScript Code Property Graphs with Explanations for
Ad and Tracker Blocking.In Proceedings of the 2023
ACM SIGSAC Conference on Computer and Communi-
cations Security. 2023. https://doi.org/10.1145/
3576915.3623084
[162] Dongkeun Lee, Minwoo Joo, and Wonjun Lee. Net-
Track: Generic Web Tracking Detection Using Packet
Metadata.In Proceedings of the ACM Web Con-
ference 2023. 2023. https://doi.org/10.1145/
3543507.3583372
[163] Kiho Lee, Chaejin Lim, Beomjin Jin, Taeyoung Kim,
and Hyoungshick Kim. AdFlush: A Real-World De-
ployable Machine Learning Solution for Effective Ad-
vertisement and Web Tracker Prevention.In Pro-
ceedings of the ACM Web Conference 2024. 2024.
https://doi.org/10.1145/3589334.3645698
[164] Brian Lefler. What Happened to the Privacy Budget?
· Issue #413 · Privacysandbox/Privacy-Sandbox-
Dev-Support, 2024. https://github.com/
privacysandbox/privacy-sandbox-dev-
support/issues/413
[165] Luis A. Leiva, Ioannis Arapakis, and Costas Iordanou.
My Mouse, My Rules: Privacy Issues of Behavioral
User Profiling via Mouse Tracking.In Proceedings
of the 2021 Conference on Human Information In-
teraction and Retrieval. 2021. https://doi.org/
10.1145/3406522.3446011
[166] Pedro Giovanni Leon, Lorrie Faith Cranor, Aleecia M.
McDonald, and Robert McGuire. Token Attempt:
The Misrepresentation of Website Privacy Policies
through the Misuse of P3P Compact Policy Tokens.
In Proceedings of the 9th Annual ACM Workshop
on Privacy in the Electronic Society. 2010. https:
//doi.org/10.1145/1866919.1866932
[167] Adam Lerner, Anna Kornfeld Simpson, Tadayoshi
Kohno, and Franziska Roesner. Internet Jones and
the Raiders of the Lost Trackers: An Archaeological
Study of Web Tracking from 1996 to 2016.In
Proceedings of the 25th USENIX Conference on Se-
curity Symposium. 2016. https://www.usenix.org/
conference/usenixsecurity16/technical-
sessions/presentation/lerner
[168] Frank Li. Shim Shimmeny: Evaluating the Security
and Privacy Contributions of Link Shimming in the
Modern Web.In Proceedings of the 29th USENIX
Conference on Security Symposium. 2020
[169] Song Li and Yinzhi Cao. Who Touched My
Browser Fingerprint?: A Large-Scale Measurement
Study and Classification of Fingerprint Dynamics.
In Proceedings of the ACM Internet Measurement
Conference. 2020. https://doi.org/10.1145/
3419394.3423614
[170] Timothy Libert. An Automated Approach to Au-
diting Disclosure of Third-Party Data Collection in
Website Privacy Policies.In Proceedings of the
2018 World Wide Web Conference. 2018. https:
//doi.org/10.1145/3178876.3186087
[171] Chaejin Lim, Kiho Lee, Beomjin Jin, Heewon Baek,
and Hyoungshick Kim. AdVersa: Adversarially-
Robust and Practical Ad and Tracker Blocking in
the Wild.In Proceedings of the ACM Web Con-
ference 2026. 2026. https://doi.org/10.1145/
3774904.3792735
[172] Maxwell Lin, Shihan Lin, Helen Wu, Karen Wang,
and Xiaowei Yang. Browsing without Third-Party
Cookies: What Do You See?In Proceedings of the
2024 ACM on Internet Measurement Conference. 2024.
https://doi.org/10.1145/3646547.3689014
[173] Xu Lin, Frederico Araujo, Teryl Taylor, Jiyong Jang,
and Jason Polakis. Fashion Faux Pas: Implicit
Stylistic Fingerprints for Bypassing Browsers’ Anti-
Fingerprinting Defenses.In 2023 IEEE Symposium
on Security and Privacy. 2023. https://doi.org/
10.1109/SP46215.2023.10179437
[174] Xu Lin, Panagiotis Ilia, and Jason Polakis. Fill in the
Blanks: Empirical Analysis of the Privacy Threats of
Browser Form Autofill.In Proceedings of the 2020
ACM SIGSAC Conference on Computer and Communi-
cations Security. 2020. https://doi.org/10.1145/
3372297.3417271
[175] Xu Lin, Panagiotis Ilia, Saumya Solanki, and Ja-
son Polakis. Phish in Sheep’s Clothing: Explor-
ing the Authentication Pitfalls of Browser Finger-
printing.In 31st USENIX Security Symposium.
2022. https://www.usenix.org/conference/
usenixsecurity22/presentation/lin-xu
[176] Thomas Linden, Rishabh Khandelwal, Hamza Hark-
ous, and Kassem Fawaz. The Privacy Policy Landscape
After the GDPR.Proceedings on Privacy Enhanc-
ing Technologies, 2020. https://doi.org/10.2478/
popets-2020-0004
[177] Zengrui Liu, Jimmy Dani, Yinzhi Cao, Shujiang Wu,
and Nitesh Saxena. The First Early Evidence of the Use
of Browser Fingerprinting for Online Tracking.In Pro-
ceedings of the ACM on Web Conference 2025. 2025.
https://doi.org/10.1145/3696410.3714548
24

[178] Zengrui Liu, Umar Iqbal, and Nitesh Saxena. Opted
Out, Yet Tracked: Are Regulations Enough to Protect
Your Privacy?Proceedings on Privacy Enhancing
Technologies, 2024. https://doi.org/10.56553/
popets-2024-0016
[179] Zengrui Liu, Prakash Shrestha, and Nitesh Saxena.
Gummy Browsers: Targeted Browser Spoofing Against
State-of-the-Art Fingerprinting Techniques.In Inter-
national Conference on Applied Cryptography and
Network Security. 2022. https://doi.org/10.1007/
978-3-031-09234-3_8
[180] Minjun Long and David Evans. Evaluating Google’s
Protected Audience Protocol.Proceedings on Privacy
Enhancing Technologies, 2024. https://doi.org/
10.56553/popets-2024-0147
[181] Chaoyi Lu, Baojun Liu, Yiming Zhang, Zhou Li,
Fenglu Zhang, Haixin Duan, Ying Liu, Joann Qiongna
Chen, Jinjin Liang, Zaifeng Zhang, Shuang Hao, and
Min Yang. From WHOIS to WHOWAS: A Large-
Scale Measurement Study of Domain Registration Pri-
vacy under the GDPR.In Proceedings 2021 Network
and Distributed System Security Symposium. 2021.
https://doi.org/10.14722/ndss.2021.23134
[182] Sunil Manandhar, Kapil Singh, and Adwait Nadkarni.
Towards Automated Regulation Analysis for Effective
Privacy Compliance.In Proceedings 2024 Network
and Distributed System Security Symposium. 2024.
https://doi.org/10.14722/ndss.2024.24650
[183] Tina Marjanov, Maria Konstantinou, Magdalena
Jó´ zwiak, and Dayana Spagnuelo. Data Security on
the Ground: Investigating Technical and Legal Re-
quirements under the GDPR.Proceedings on Privacy
Enhancing Technologies, 2023. https://doi.org/
10.56553/popets-2023-0088
[184] Jeremy Martin, Douglas Alpuche, Kristina Bodeman,
Lamont Brown, Ellis Fenske, Lucas Foppe, Travis May-
berry, Erik Rye, Brandon Sipes, and Sam Teplov. Hand-
off All Your Privacy – A Review of Apple’s Blue-
tooth Low Energy Continuity Protocol.Proceedings
on Privacy Enhancing Technologies, 2019. https:
//doi.org/10.2478/popets-2019-0057
[185] Rahat Masood, Benjamin Zi Hao Zhao, Hassan Jameel
Asghar, and Mohamed Ali Kaafar. Touch and You’re
Trapp(Ck)Ed: Quantifying the Uniqueness of Touch
Gestures for Tracking.Proceedings on Privacy
Enhancing Technologies, 2018. https://doi.org/
10.1515/popets-2018-0016
[186] Célestin Matte, Nataliia Bielova, and Cristiana San-
tos. Do Cookie Banners Respect My Choice? : Mea-
suring Legal Compliance of Banners from IAB Eu-
rope’s Transparency and Consent Framework.In
2020 IEEE Symposium on Security and Privacy. 2020.
https://doi.org/10.1109/SP40000.2020.00076
[187] Jonathan R. Mayer."Any Person. . . a Pamphle-
teer" Internet Anonymity in the Age of Web 2.0.
Ph.D. thesis, Princeton University Senior Theses,
2009. https://arks.princeton.edu/ark:/88435/
dsp01nc580n467
[188] Jonathan R. Mayer and John C. Mitchell. Third-Party
Web Tracking: Policy and Technology.In 2012 IEEE
Symposium on Security and Privacy. 2012. https:
//doi.org/10.1109/SP.2012.47
[189] MDN. Domain - MDN Web Docs Glossary,
2024. https://developer.mozilla.org/en-US/
docs/Glossary/Domain
[190] MDN. Same-Origin Policy - Security on the Web,
2024. https://developer.mozilla.org/en-US/
docs/Web/Security/Same-origin_policy
[191] MDN. State Partitioning - Privacy on the Web,
2024. https://developer.mozilla.org/en-US/
docs/Web/Privacy/State_Partitioning
[192] MDN. Storage Access API - Web APIs,
2024. https://developer.mozilla.org/en-US/
docs/Web/API/Storage_Access_API
[193] MDN. Third-Party Cookies - Privacy on the Web,
2024. https://developer.mozilla.org/en-US/
docs/Web/Privacy/Third-party_cookies
[194] MDN. User Agent - MDN Web Docs Glossary,
2025. https://developer.mozilla.org/en-US/
docs/Glossary/User_agent
[195] Maryam Mehrnezhad. A Cross-Platform Evalua-
tion of Privacy Notices and Tracking Practices.In
2020 IEEE European Symposium on Security and Pri-
vacy Workshops. 2020. https://doi.org/10.1109/
EuroSPW51379.2020.00023
[196] Maryam Mehrnezhad, Kovila Coopamootoo, and
Ehsan Toreini. How Can and Would People Pro-
tect From Online Tracking?Proceedings on Privacy
Enhancing Technologies, 2022. https://doi.org/
10.2478/popets-2022-0006
[197] Wei Meng, Byoungyoung Lee, Xinyu Xing, and Wenke
Lee. TrackMeOrNot: Enabling Flexible Control on
Web Tracking.In Proceedings of the 25th Interna-
tional Conference on World Wide Web. 2016.https:
//doi.org/10.1145/2872427.2883034
25

[198] Matt Menke. Storage Isolation Project,
2020. https://docs.google.com/
document/d/1V8sFDCEYTXZmwKa_
qWUfTVNAuBcPsu6FC0PhqMD6KKQ
[199] Vikas Mishra, Pierre Laperdrix, Walter Rudametkin,
and Romain Rouvoy. Déjà vu: Abusing Browser Cache
Headers to Identify and Track Online Users.Pro-
ceedings on Privacy Enhancing Technologies, 2021.
https://doi.org/10.2478/popets-2021-0033
[200] Vikas Mishra, Pierre Laperdrix, Antoine Vastel, Wal-
ter Rudametkin, Romain Rouvoy, and Martin Lopatka.
Don’t Count Me Out: On the Relevance of IP Address
in the Tracking Ecosystem.In Proceedings of The Web
Conference 2020. 2020. https://doi.org/10.1145/
3366423.3380161
[201] Lou Montulli and David M. Kristol. HTTP State Man-
agement Mechanism. Request for comments, Internet
Engineering Task Force, 1997. https://doi.org/
10.17487/RFC2109
[202] Nitesh Mor, Oriana Riva, Suman Nath, and John Kubi-
atowicz. Bloom Cookies: Web Search Personalization
without User Tracking.In Proceedings 2015 Network
and Distributed System Security Symposium. 2015.
https://doi.org/10.14722/ndss.2015.23108
[203] Zahra Moti, Asuman Senol, Hamid Bostani, Fred-
erik Zuiderveen Borgesius, Veelasha Moonsamy,
Arunesh Mathur, and Gunes Acar. Targeted and Trou-
blesome: Tracking and Advertising on Children’s
Websites.In 2024 IEEE Symposium on Security
and Privacy. 2024. https://doi.org/10.1109/
SP54263.2024.00118
[204] Mozilla. Security/Anti Tracking Policy - MozillaWiki,
2019. https://wiki.mozilla.org/Security/
Anti_tracking_policy
[205] Shaoor Munir, Konrad Kollnig, Anastasia Shuba, and
Zubair Shafiq. Google’s Chrome Antitrust Para-
dox, 2024. https://papers.ssrn.com/abstract=
4780718
[206] Shaoor Munir, Patrick Lee, Umar Iqbal, Zubair
Shafiq, and Sandra Siby. PURL: Safe
and Effective Sanitization of Link Decora-
tion.In 33rd USENIX Security Symposium.
2024. https://www.usenix.org/conference/
usenixsecurity24/presentation/munir
[207] Shaoor Munir, Sandra Siby, Umar Iqbal, Steven Engle-
hardt, Zubair Shafiq, and Carmela Troncoso. Cookie-
Graph: Understanding and Detecting First-Party Track-
ing Cookies.In Proceedings of the 2023 ACM
SIGSAC Conference on Computer and Communica-
tions Security. 2023. https://doi.org/10.1145/
3576915.3616586
[208] Meenatchi Sundaram Muthu Selva Annamalai, Emil-
iano De Cristofaro, and Igor Bilogrevic. Beyond the
Crawl: Unmasking Browser Fingerprinting in Real
User Interactions.In Proceedings of the ACM on Web
Conference 2025. 2025. https://doi.org/10.1145/
3696410.3714871
[209] Arvind Narayanan. The Web Tracking Arms
Race: Past, Present, and Future.In Enigma.
2018. https://www.usenix.org/conference/
enigma2018/presentation/narayanan
[210] Arvind Narayanan and Dillon Reisman. The
Princeton Web Transparency and Accountability
Project.Transparent Data Mining for Big and
Small Data, 2017. https://doi.org/10.1007/978-
3-319-54024-5_3
[211] Nick Nikiforakis, Wouter Joosen, and Benjamin
Livshits. PriVaricator: Deceiving Fingerprinters with
Little White Lies.In Proceedings of the 24th In-
ternational Conference on World Wide Web. 2015.
https://doi.org/10.1145/2736277.2741090
[212] Nick Nikiforakis, Alexandros Kapravelos, Wouter
Joosen, Christopher Kruegel, Frank Piessens, and Gio-
vanni Vigna. Cookieless Monster: Exploring the
Ecosystem of Web-Based Device Fingerprinting.In
2013 IEEE Symposium on Security and Privacy. 2013.
https://doi.org/10.1109/SP.2013.43
[213] Pouneh Nikkhah Bahrami, Aurore Fass, and Zubair
Shafiq. COOKIEGUARD: Characterizing and Isolat-
ing the First-Party Cookie Jar.In Proceedings of the
2025 ACM Internet Measurement Conference. 2025.
https://doi.org/10.1145/3730567.3764490
[214] Pouneh Nikkhah Bahrami, Aurore Fass, and Zubair
Shafiq. $CookieGuard:$ Characterizing and Isolating
the First-Party Cookie Jar.In Proceedings of the 2025
ACM Internet Measurement Conference. 2025. https:
//doi.org/10.1145/3730567.3764490
[215] Alexandra Nisenoff, Arthur Borem, Madison Pick-
ering, Grant Nakanishi, Maya Thumpasery, and
Blase Ur. Defining "Broken": User Experiences
and Remediation Tactics When Ad-Blocking or
Tracking-Protection Tools Break a Website’s User
Experience.In 32nd USENIX Security Symposium.
2023. https://www.usenix.org/conference/
usenixsecurity23/presentation/nisenoff-
broken
26

[216] Alexandra Nisenoff, Deian Stefan, and Nicolas
Christin. Exploiting the Shared Storage API.In
Proceedings of the 2025 ACM SIGSAC Conference
on Computer and Communications Security. 2025.
https://doi.org/10.1145/3719027.3744848
[217] Kazuki Nomoto, Takuya Watanabe, Eitaro Shioji,
Mitsuaki Akiyama, and Tatsuya Mori. Browser
Permission Mechanisms Demystified.In Proceed-
ings 2023 Network and Distributed System Secu-
rity Symposium. 2023. https://doi.org/10.14722/
ndss.2023.23109
[218] Mark Nottingham. Unsanctioned Web Tracking,
2015. https://w3ctag.github.io/unsanctioned-
tracking/
[219] Jasmine Novak, Prabhakar Raghavan, and Andrew
Tomkins. Anti-Aliasing on the Web.In Proceedings of
the 13th International Conference on World Wide Web.
2004.https://doi.org/10.1145/988672.988678
[220] Łukasz Olejnik, Gunes Acar, Claude Castelluccia,
and Claudia Diaz. The Leaking Battery: A Privacy
Analysis of the HTML5 Battery Status API. In
Data Privacy Management, and Security Assurance,
vol. 9481. 2016. https://doi.org/10.1007/978-3-
319-29883-2_18
[221] Lukasz Olejnik and C. Castelluccia. To Bid or
Not to Bid? Measuring the Value of Privacy in
RTB, 2014. https://www.inrialpes.fr/planete/
people/lukasz/rtb2.pdf
[222] Lukasz Olejnik, Minh-Dung Tran, and Claude Castel-
luccia. Selling off Privacy at Auction.In Pro-
ceedings 2014 Network and Distributed System Secu-
rity Symposium. 2014. https://doi.org/10.14722/
ndss.2014.23270
[223] Yossef Oren, Vasileios P. Kemerlis, Simha Sethumad-
havan, and Angelos D. Keromytis. The Spy in the
Sandbox: Practical Cache Attacks in JavaScript and
Their Implications.In Proceedings of the 22nd ACM
SIGSAC Conference on Computer and Communica-
tions Security. 2015. https://doi.org/10.1145/
2810103.2813708
[224] Carolina Ortega Pérez and Alaa Daffalla. Encrypted
Access Logging for Online Accounts: Device Attribu-
tions without Device Tracking.In Proceedings of the
34th USENIX Security Symposium. 2025. https://
www.usenix.org/conference/usenixsecurity25/
presentation/ortega-perez
[225] Haoran Ou, Yong Fang, Yongyan Guo, Wenbo Guo,
and Cheng Huang. Viopolicy-Detector: An Auto-
mated Approach to Detecting GDPR Suspected Com-
pliance Violations in Websites.In Proceedings of the
25th International Symposium on Research in Attacks,
Intrusions and Defenses. 2022. https://doi.org/
10.1145/3545948.3545952
[226] Xiang Pan, Yinzhi Cao, and Yan Chen. I Do Not
Know What You Visited Last Summer: Protecting
Users from Stateful Third-Party Web Tracking with
TrackingFree Browser.In Proceedings 2015 Network
and Distributed System Security Symposium. 2015.
https://doi.org/10.14722/ndss.2015.23163
[227] Emmanouil Papadogiannakis, Panagiotis Papadopou-
los, Nicolas Kourtellis, and Evangelos P. Markatos.
User Tracking in the Post-Cookie Era: How Web-
sites Bypass GDPR Consent to Track Users.In Pro-
ceedings of the Web Conference 2021. 2021. https:
//doi.org/10.1145/3442381.3450056
[228] Panagiotis Papadopoulos, Nicolas Kourtellis, and Evan-
gelos Markatos. Cookie Synchronization: Everything
You Always Wanted to Know But Were Afraid to
Ask.In The World Wide Web Conference. 2019.
https://doi.org/10.1145/3308558.3313542
[229] Namyong Park, Ryan Rossi, Eunyee Koh,
Iftikhar Ahamath Burhanuddin, Sungchul Kim,
Fan Du, Nesreen Ahmed, and Christos Faloutsos.
CGC: Contrastive Graph Clustering forCom-
munity Detection and Tracking.In Proceed-
ings of the ACM Web Conference 2022. 2022.
https://doi.org/10.1145/3485447.3512160
[230] Mike Perry, Erinn Clark, and Steven Mur-
doch. The Design and Implementation of
the Tor Browser [DRAFT], 2013. https:
//people.torproject.org/{~}weasel/tor-
web-underlay/projects/torbrowser/design/
[231] Amogh Pradeep, Álvaro Feal, Julien Gamba, Ashwin
Rao, Martina Lindorfer, Narseo Vallina-Rodriguez, and
David Choffnes. Not Your Average App: A Large-
Scale Privacy Analysis of Android Browsers.Pro-
ceedings on Privacy Enhancing Technologies, 2023.
https://doi.org/10.56553/popets-2023-0003
[232] Barath Raghavan, Tadayoshi Kohno, Alex C. Snoeren,
and David Wetherall. Enlisting ISPs to Improve Online
Privacy: IP Address Mixing by Default. In Privacy
Enhancing Technologies. 2009. https://doi.org/
10.1007/978-3-642-03168-7_9
[233] Audrey Randall, Peter Snyder, Alisha Ukani, Alex C.
Snoeren, Geoffrey M. V oelker, Stefan Savage, and
27

Aaron Schulman. Measuring UID Smuggling in the
Wild.In Proceedings of the 22nd ACM Internet
Measurement Conference. 2022. https://doi.org/
10.1145/3517745.3561415
[234] Joseph Reagle and Lorrie Faith Cranor. The Platform
for Privacy Preferences.Communications of the ACM,
1999.https://doi.org/10.1145/293411.293455
[235] Nathan Reitinger and Michelle L. Mazurek. ML-
CB: Machine Learning Canvas Block.Proceedings
on Privacy Enhancing Technologies, 2021. https:
//doi.org/10.2478/popets-2021-0056
[236] Eric Rescorla. Technical Comments on Pri-
vacy Budget. Technical report, Mozilla, 2021.
https://mozilla.github.io/ppa-docs/privacy-
budget.pdf
[237] Eric Rescorla and Martin Thomson. Technical
Comments on FLoC Privacy. Technical report,
Mozilla, 2021. https://mozilla.github.io/ppa-
docs/floc_report.pdf
[238] Wolf Rieder, Philip Raschke, Thomas Cory, Chris-
tian Rene Sechting, Aditya Kumar, and Axel Küp-
per. SoK: After Decades of Web Tracker Detection,
What’s Next?In 2026 IEEE Symposium on Secu-
rity and Privacy. 2026. https://doi.org/10.1109/
SP63933.2026.00222
[239] David Rodriguez, Joseph A. Calandrino, José M. del
Álamo, and Norman Sadeh. Privacy Settings of Third-
Party Libraries in Android Apps: A Study of Facebook
SDKs.Proceedings on Privacy Enhancing Technolo-
gies, 2025. https://doi.org/10.56553/popets-
2025-0056
[240] Thomas Rokicki, Clémentine Maurice, and Pierre
Laperdrix. SoK: In Search of Lost Time: A Re-
view of JavaScript Timers in Browsers.In 2021
IEEE European Symposium on Security and Pri-
vacy (EuroS&P). 2021. https://doi.org/10.1109/
EuroSP51992.2021.00039
[241] Eduard Rupp, Emmanuel Syrmoudis, and Jens
Grossklags. Leave No Data Behind – Empirical
Insights into Data Erasure from Online Services.Pro-
ceedings on Privacy Enhancing Technologies, 2022.
https://doi.org/10.56553/popets-2022-0080
[242] Erik Rye, Robert Beverly, and K C Claffy. Follow
the Scent: Defeating IPv6 Prefix Rotation Privacy.
In Proceedings of the 21st ACM Internet Measure-
ment Conference. 2021. https://doi.org/10.1145/
3487552.3487829
[243] Marlene Saemann, Daniel Theis, Tobias Urban, and
Martin Degeling. Investigating GDPR Fines in
the Light of Data Flows.Proceedings on Privacy
Enhancing Technologies, 2022. https://doi.org/
10.56553/popets-2022-0111
[244] Iskander Sanchez-Rola, Matteo Dell’Amico, Davide
Balzarotti, Pierre-Antoine Vervier, and Leyla Bilge.
Journey to the Center of the Cookie Ecosystem: Unrav-
eling Actors’ Roles and Relationships.In 2021 IEEE
Symposium on Security and Privacy. 2021. https:
//doi.org/10.1109/SP40001.2021.9796062
[245] Iskander Sánchez-Rola, Matteo Dell’Amico, Platon
Kotzias, Davide Balzarotti, Leyla Bilge, Pierre-Antoine
Vervier, and Igor Santos. Can I Opt Out Yet?: GDPR
and the Global Illusion of Cookie Control.In Pro-
ceedings of the 2019 ACM Asia Conference on Com-
puter and Communications Security. 2019. https:
//doi.org/10.1145/3321705.3329806
[246] Iskander Sanchez-Rola, Igor Santos, and Davide
Balzarotti. Clock Around the Clock: Time-Based
Device Fingerprinting.In Proceedings of the 2018
ACM SIGSAC Conference on Computer and Communi-
cations Security. 2018. https://doi.org/10.1145/
3243734.3243796
[247] Iskander Sanchez-Rola, Xabier Ugarte-Pedrero, Igor
Santos, and Pablo G. Bringas. The Web Is Watching
You: A Comprehensive Review of Web-Tracking Tech-
niques and Countermeasures.Logic Journal of IGPL,
2017.https://doi.org/10.1093/jigpal/jzw041
[248] Cristiana Santos, Nataliia Bielova, and Célestin Matte.
Are Cookie Banners Indeed Compliant with the Law?
: Deciphering EU Legal Requirements on Consent
and Technical Means to Verify Compliance of Cookie
Banners.Technology and Regulation, 2020. https:
//doi.org/10.26116/techreg.2020.009
[249] Cristiana Santos, Midas Nouwens, Michael Toth, Na-
taliia Bielova, and Vincent Roca. Consent Manage-
ment Platforms Under the GDPR: Processors and/or
Controllers?In Privacy Technologies and Policy: 9th
Annual Privacy Forum. 2021. https://doi.org/
10.1007/978-3-030-76663-4_3
[250] Florian Schaub, Rebecca Balebako, Adam L. Du-
rity, and Lorrie Faith Cranor. A Design Space
for Effective Privacy Notices.In Eleventh
Symposium On Usable Privacy and Security.
2015. https://www.usenix.org/conference/
soups2015/proceedings/presentation/schaub
[251] Asuman Senol and Gunes Acar. Unveiling the Im-
pact of User-Agent Reduction and Client Hints: A
28

Measurement Study.In Proceedings of the 22nd
Workshop on Privacy in the Electronic Society. 2023.
https://doi.org/10.1145/3603216.3624965
[252] Asuman Senol, Gunes Acar, Mathias Humbert, and
Frederik Zuiderveen Borgesius. Leaky Forms: A
Study of Email and Password Exfiltration Before Form
Submission.In 31st USENIX Security Symposium.
2022. https://www.usenix.org/conference/
usenixsecurity22/presentation/senol
[253] Asuman Senol, Alisha Ukani, Dylan Cutler, and Igor
Bilogrevic. The Double Edged Sword: Identify-
ing Authentication Pages and Their Fingerprinting
Behavior.In Proceedings of the ACM Web Con-
ference 2024. 2024. https://doi.org/10.1145/
3589334.3645493
[254] He Shuang, Lianying Zhao, and David Lie. Duumviri:
Detecting Trackers and Mixed Trackers with a Break-
age Detector.In Proceedings of the Network and Dis-
tributed System Security Symposium. 2025. https:
//doi.org/10.14722/ndss.2025.230267
[255] Anastasia Shuba and Athina Markopoulou. NoMoATS:
Towards Automatic Detection of Mobile Tracking.Pro-
ceedings on Privacy Enhancing Technologies, 2020.
https://doi.org/10.2478/popets-2020-0017
[256] Anastasia Shuba, Athina Markopoulou, and Zubair
Shafiq. NoMoAds: Effective and Efficient Cross-App
Mobile Ad-Blocking.Proceedings on Privacy Enhanc-
ing Technologies, 2018. https://doi.org/10.1515/
popets-2018-0035
[257] Sandra Siby, Umar Iqbal, Steven Englehardt, Zubair
Shafiq, and Carmela Troncoso. WebGraph: Capturing
Advertising and Tracking Information Flows for Ro-
bust Blocking.In 31st USENIX Security Symposium.
2022. https://www.usenix.org/conference/
usenixsecurity22/presentation/siby
[258] Kapil Singh, Alexander Moshchuk, Helen J. Wang,
and Wenke Lee. On the Incoherencies in Web Browser
Access Control Policies.In 2010 IEEE Symposium
on Security and Privacy. 2010. https://doi.org/
10.1109/SP.2010.35
[259] Michael Smith, Pete Snyder, Benjamin Livshits, and
Deian Stefan. SugarCoat: Programmatically Gener-
ating Privacy-Preserving, Web-Compatible Resource
Replacements for Content Blocking.In Proceed-
ings of the 2021 ACM SIGSAC Conference on Com-
puter and Communications Security. 2021. https:
//doi.org/10.1145/3460120.3484578
[260] Pete Snyder and Jeffrey Yasskin. Navigational-
Tracking Mitigations, 2024. https:
//privacycg.github.io/nav-tracking-
mitigations/
[261] Peter Snyder, Soroush Karami, Arthur Edelstein,
Benjamin Livshits, and Hamed Haddadi. Pool-
Party: Exploiting Browser Resource Pools for Web
Tracking.In 32nd USENIX Security Symposium.
2023. https://www.usenix.org/conference/
usenixsecurity23/presentation/snyder
[262] Peter Snyder and Ben Livshits. Brave, Fingerprint-
ing, and Privacy Budgets, 2019.https://brave.com/
web-standards-at-brave/2-privacy-budgets/
[263] Peter Snyder, Antoine Vastel, and Ben Livshits. Who
Filters the Filters: Understanding the Growth, Use-
fulness and Efficiency of Crowdsourced Ad Block-
ing.In Abstracts of the 2020 SIGMETRICS/Perfor-
mance Joint International Conference on Measurement
and Modeling of Computer Systems. 2020. https:
//doi.org/10.1145/3393691.3394228
[264] Konstantinos Solomos, Panagiotis Ilia, Soroush
Karami, Nick Nikiforakis, and Jason Polakis.
The Dangers of Human Touch: Fingerprint-
ing Browser Extensions through User Ac-
tions.In 31st USENIX Security Symposium.
2022. https://www.usenix.org/conference/
usenixsecurity22/presentation/solomos
[265] Konstantinos Solomos, Panagiotis Ilia, Nick Niki-
forakis, and Jason Polakis. Escaping the Confines
of Time: Continuous Browser Extension Fingerprint-
ing Through Ephemeral Modifications.In Proceed-
ings of the 2022 ACM SIGSAC Conference on Com-
puter and Communications Security. 2022. https:
//doi.org/10.1145/3548606.3560576
[266] Konstantinos Solomos, John Kristoff, Chris Kanich,
and Jason Polakis. Tales of Favicons and Caches:
Persistent Tracking in Modern Browsers.In Pro-
ceedings 2021 Network and Distributed System Secu-
rity Symposium. 2021. https://doi.org/10.14722/
ndss.2021.24202
[267] Daniel J. Solove and Woodrow Hartzog. The FTC
and the New Common Law of Privacy, 2013. https:
//doi.org/10.2139/ssrn.2312913
[268] Ashkan Soltani, Shannon Canty, Quentin Mayo, Lau-
ren Thomas, and Chris Jay Hoofnagle. Flash Cook-
ies and Privacy, 2009. https://doi.org/10.2139/
ssrn.1446862
29

[269] Ove Sörensen. Zombie-Cookies: Case Studies and
Mitigation.In 8th International Conference for In-
ternet Technology and Secured Transactions. 2013.
https://doi.org/10.1109/ICITST.2013.6750214
[270] Aleksei Stafeev and Giancarlo Pellegrino. SoK:
State of the Krawlers – Evaluating the Effective-
ness of Crawling Algorithms for Web Security Mea-
surements.In 33rd USENIX Security Symposium.
2024. https://www.usenix.org/conference/
usenixsecurity24/presentation/stafeev
[271] Oleksii Starov, Pierre Laperdrix, Alexandros Kaprav-
elos, and Nick Nikiforakis. Unnecessarily Identifi-
able: Quantifying the Fingerprintability of Browser
Extensions Due to Bloat.In The World Wide
Web Conference. 2019. https://doi.org/10.1145/
3308558.3313458
[272] Oleksii Starov and Nick Nikiforakis. Extended Track-
ing Powers: Measuring the Privacy Diffusion Enabled
by Browser Extensions.In Proceedings of the 26th
International Conference on World Wide Web. 2017.
https://doi.org/10.1145/3038912.3052596
[273] Oleksii Starov and Nick Nikiforakis. XHOUND: Quan-
tifying the Fingerprintability of Browser Extensions.
In 2017 IEEE Symposium on Security and Privacy.
2017.https://doi.org/10.1109/SP.2017.18
[274] Alina Stöver, Nina Gerber, Henning Pridöhl, Max
Maass, Sebastian Bretthauer, Indra Spiecker genannt
Döhmann, Matthias Hollick, and Dominik Herrmann.
How Website Owners Face Privacy Issues: Thematic
Analysis of Responses from a Covert Notification
Study Reveals Diverse Circumstances and Challenges.
Proceedings on Privacy Enhancing Technologies, 2023.
https://doi.org/10.56553/POPETS-2023-0051
[275] Junhua Su and Alexandros Kapravelos. Automatic
Discovery of Emerging Browser Fingerprinting Tech-
niques.In Proceedings of the ACM Web Con-
ference 2023. 2023. https://doi.org/10.1145/
3543507.3583333
[276] Chen Sun, Evan Jacobs, Daniel Lehmann, Andrew
Crouse, and Supreeth Shastri. GDPRxiv: Establish-
ing the State of the Art in GDPR Enforcement.Pro-
ceedings on Privacy Enhancing Technologies, 2023.
https://doi.org/10.56553/popets-2023-0121
[277] Erik Sy, Christian Burkert, Hannes Federrath, and
Mathias Fischer. A QUIC Look at Web Tracking.Pro-
ceedings on Privacy Enhancing Technologies, 2019.
https://doi.org/10.2478/popets-2019-0046
[278] Erik Sy, Tobias Mueller, Christian Burkert, Hannes
Federrath, and Mathias Fischer. Enhanced Perfor-
mance and Privacy for TLS over TCP Fast Open.Pro-
ceedings on Privacy Enhancing Technologies, 2020.
https://doi.org/10.2478/popets-2020-0027
[279] Brave Privacy Team. Fingerprinting Defenses 2.0,
2020. https://brave.com/privacy-updates/4-
fingerprinting-defenses-2.0/
[280] Brave Privacy Team. Ephemeral Third-Party Site Stor-
age, 2021. https://brave.com/privacy-updates/
7-ephemeral-storage/
[281] Brave Privacy Team. "Unlinkable Bouncing"
for More Protection against Bounce Tracking,
2022. https://brave.com/privacy-updates/16-
unlinkable-bouncing/
[282] Martin Thomson. An Analysis of Apple’s Private Click
Measurement, 2022. https://mozilla.github.io/
ppa-docs/pcm.pdf
[283] Martin Thomson. A Privacy Analysis of Google’s Top-
ics Proposal. Technical report, Mozilla, 2023. https:
//mozilla.github.io/ppa-docs/topics.pdf
[284] Martin Thomson. Protected Audience Pri-
vacy Analysis. Technical report, Mozilla,
2024. https://mozilla.github.io/ppa-docs/
protected-audience.pdf
[285] The New York Times. Senator Raises Privacy
As Federal Web Site Issue.The New York Times,
2001. https://www.nytimes.com/2001/04/
17/business/senator-raises-privacy-as-
federal-web-site-issue.html
[286] Ryan Torok and Amit Levy. Only Pay for What You
Leak: Leveraging Sandboxes for a Minimally Inva-
sive Browser Fingerprinting Defense.In 2023 IEEE
Symposium on Security and Privacy. 2023. https:
//doi.org/10.1109/SP46215.2023.10179385
[287] Michael Toth, Nataliia Bielova, and Vincent Roca. On
Dark Patterns and Manipulation of Website Publish-
ers by CMPs.Proceedings on Privacy Enhancing
Technologies, 2022. https://doi.org/10.56553/
popets-2022-0082
[288] Vincent Toubiana, Arvind Narayanan, Dan Boneh,
Helen Nissenbaum, and Solon Barocas. Ad-
nostic: Privacy Preserving Targeted Advertising.
In Proceedings of the 2010 Network and Dis-
tributed System Security Symposium. 2010. https:
//www.ndss-symposium.org/ndss2010/adnostic-
privacy-preserving-targeted-advertising/
30

[289] Leon Trampert, Christian Rossow, and Michael
Schwarz. Browser-Based CPU Fingerprinting.In
Computer Security – ESORICS 2022. 2022. https:
//doi.org/10.1007/978-3-031-17143-7_5
[290] Florian Tramèr, Pascal Dupré, Gili Rusak, Giancarlo
Pellegrino, and Dan Boneh. AdVersarial: Perceptual
Ad Blocking Meets Adversarial Machine Learning.In
Proceedings of the 2019 ACM SIGSAC Conference
on Computer and Communications Security. 2019.
https://doi.org/10.1145/3319535.3354222
[291] Erik Trickel, Oleksii Starov, Alexandros Kaprav-
elos, Nick Nikiforakis, and Adam Doupé. Ev-
eryone Is Different: Client-Side Diversification
for Defending Against Extension Fingerprint-
ing.In 28th USENIX Security Symposium.
2019. https://www.usenix.org/conference/
usenixsecurity19/presentation/trickel
[292] Florian Turati, Karel Kubicek, Carlos Cotrini, and
David Basin. Locality-Sensitive Hashing Does Not
Guarantee Privacy! Attacks on Google’s FLoC and the
MinHash Hierarchy System.Proceedings on Privacy
Enhancing Technologies, 2023. https://doi.org/
10.56553/popets-2023-0101
[293] Alisha Ukani, Hamed Haddadi, Alex C. Snoeren, and
Peter Snyder. Local Frames: Exploiting Inherited
Origins to Bypass Content Blockers.In Proceed-
ings of the 2025 ACM SIGSAC Conference on Com-
puter and Communications Security. 2025. https:
//doi.org/10.1145/3719027.3744843
[294] Tobias Urban, Yash Vekaria, Zubair Shafiq, Chris
Böttger, and Barry Pollard. The 2024 Web Al-
manac: Third Parties. In The 2024 Web Al-
manac. 2024. https://almanac.httparchive.org/
en/2024/third-parties
[295] Christine Utz, Sabrina Amft, Martin Degeling,
Thorsten Holz, Sascha Fahl, and Florian Schaub. Pri-
vacy Rarely Considered: Exploring Considerations in
the Adoption of Third-Party Services by Websites.Pro-
ceedings on Privacy Enhancing Technologies, 2023.
https://doi.org/10.56553/popets-2023-0002
[296] Tom Van Goethem, Wouter Joosen, and Nick Niki-
forakis. The clock is still ticking: Timing attacks in
the modern web.In Proceedings of the 22nd ACM
SIGSAC Conference on Computer and Communica-
tions Security. 2015. https://doi.org/10.1145/
2810103.2813632
[297] Tom Van Goethem, Christina Pöpper, Wouter Joosen,
and Mathy Vanhoef. Timeless timing attacks: Ex-
ploiting concurrency to leak secrets over remote con-
nections.In 29th USENIX Security Symposium.
2020. https://www.usenix.org/conference/
usenixsecurity20/presentation/van-goethem
[298] Maggie Van Nortwick and Christo Wilson. Setting the
Bar Low: Are Websites Complying With the Minimum
Requirements of the CCPA?Proceedings on Privacy
Enhancing Technologies, 2022. https://doi.org/
10.2478/popets-2022-0030
[299] Antoine Vastel, Pierre Laperdrix, Walter Rudametkin,
and Romain Rouvoy. FP-STALKER: Tracking
Browser Fingerprint Evolutions.In 2018 IEEE Sym-
posium on Security and Privacy. 2018. https://
doi.org/10.1109/SP.2018.00008
[300] Yash Vekaria, Aurelio Loris Canino, Jonathan Levitsky,
Alex Ciechonski, Patricia Callejo, Anna Maria Man-
dalari, and Zubair Shafiq. Big Help or Big Brother?
Auditing Tracking, Profiling, and Personalization in
Generative AI Assistants, 2025. https://doi.org/
10.48550/arXiv.2503.16586
[301] Yash Vekaria, Benjamin Standaert, Max Ostapenko,
Amjad Abdul Haddi, Yana Dimova, Shaoor Munir,
Chris Böttger, Umar Iqbal, Alberto Fernandez-de-
Retana, and Barry Pollard. The 2024 Web Almanac:
Privacy. In The 2024 Web Almanac. 2024. https:
//almanac.httparchive.org/en/2024/privacy
[302] Hari Venugopalan, Kaustav Goswami, Zainul Abi
Din, Jason Lowe-Power, Samuel T. King, and Zubair
Shafiq. FP-Rowhammer: DRAM-Based Device
Fingerprinting, 2024. https://doi.org/10.48550/
arXiv.2307.00143
[303] Tim Vlummens, Aniketh Girish, Nipuna Weerasekara,
Frederik Zuiderveen Borgesius, Acar Gunes,
Narseo Vallina-Rodriguez, et al. Bridges to
self: Silent web-to-app tracking on mobile via
localhost.In 35th USENIX Security Symposium.
2026. https://www.usenix.org/conference/
usenixsecurity26/presentation/vlummens
[304] Philipp V ogt, Florian Nentwich, Nenad Jo-
vanovic, Engin Kirda, Christopher Krügel, and
Giovanni Vigna. Cross Site Scripting Preven-
tion with Dynamic Data Tainting and Static
Analysis.In Proceedings of the Network and
Distributed System Security Symposium. 2007.
https://www.ndss-symposium.org/ndss2007/
cross-site-scripting-prevention-dynamic-
data-tainting-and-static-analysis/
[305] WebKit Development Team. Tracking Prevention
in WebKit, 2020. https://webkit.org/tracking-
prevention/
31

[306] Malte Wessels, Simon Koch, Jan Drescher, Louis Bet-
tels, David Klein, and Martin Johns. HyTrack: Resur-
rectable and Persistent Tracking Across Android Apps
and the Web.In 34th USENIX Security Symposium.
2025. https://www.usenix.org/conference/
usenixsecurity25/presentation/wessels
[307] Stephan Wiefling, Marian Hönscheid, and Luigi Lo Ia-
cono. A Privacy Measure Turned Upside Down?
Investigating the Use of HTTP Client Hints on the
Web.In Proceedings of the 19th International Con-
ference on Availability, Reliability and Security. 2024.
https://doi.org/10.1145/3664476.3664478
[308] John Wilander, Charlie Wolfe, Matthew Finkel, Wen-
son Hsieh, and Keith Holleman. Private Browsing 2.0,
2024. https://webkit.org/blog/15697/private-
browsing-2-0/
[309] Shujiang Wu, Song Li, Yinzhi Cao, and Ningfei
Wang. Rendered Private: Making GLSL Execu-
tion Uniform to Prevent WebGL-Based Browser Fin-
gerprinting.In 28th USENIX Security Symposium.
2019. https://www.usenix.org/conference/
usenixsecurity19/presentation/wu
[310] Shenping Xiong, Xutong Wang, Ze Jin, Xinyu Liu,
Haoqiang Wang, Zhen Chen, Ru Tan, and Qixu Liu.
TGNN: Enhancing Pixel Tracking Detection via LLM-
Driven Annotation and GAT-Powered Structural Rep-
resentation.In Proceedings of the ACM Web Con-
ference 2026. 2026. https://doi.org/10.1145/
3774904.3792149
[311] Meng Xu, Yeongjin Jang, Xinyu Xing, Taesoo Kim,
and Wenke Lee. UCognito: Private Browsing
without Tears.In Proceedings of the 22nd ACM
SIGSAC Conference on Computer and Communica-
tions Security. 2015. https://doi.org/10.1145/
2810103.2813716
[312] Zhiju Yang, Weiping Pei, Monchu Chen, and Chuan
Yue. WTAGRAPH: Web Tracking and Advertising De-
tection Using Graph Neural Networks.In 2022 IEEE
Symposium on Security and Privacy. 2022. https:
//doi.org/10.1109/SP46214.2022.9833670
[313] T. Yen, Yinglian Xie, Fang Yu, Roger Peng Yu, and
M. Abadi. Host Fingerprinting and Tracking on the
Web: Privacy and Security Implications.In Network
and Distributed System Security Symposium. 2012.
https://www.ndss-symposium.org/ndss2012/
ndss-2012-programme/host-fingerprinting-
and-tracking-web-privacy-and-security-
implications/
[314] Zhonghao Yu, Sam Macbeth, Konark Modi, and
Josep M. Pujol. Tracking the Trackers.In Pro-
ceedings of the 25th International Conference on
World Wide Web. 2016. https://doi.org/10.1145/
2872427.2883028
[315] H. Yuan, C. Maple, C. Chen, and T. Watson. Cross-
Device Tracking through Identification of User Typ-
ing Behaviours.Electronics Letters, 2018. https:
//doi.org/10.1049/el.2018.0893
[316] Ahsan Zafar, Junhua Su, Sohom Datta, Alexandros
Kapravelos, and Anupam Das. Same Script, Dif-
ferent Behavior: Characterizing Divergent JavaScript
Execution Across Different Device Platforms.In
Proceedings of the 2025 ACM SIGSAC Conference
on Computer and Communications Security. 2025.
https://doi.org/10.1145/3719027.3765202
[317] Luqman Zagi, Zahra Moti, and Gunes Acar. Refer-
rer Policy: Implementation and Circumvention.Pro-
ceedings on Privacy Enhancing Technologies, 2025.
https://doi.org/10.56553/popets-2025-0092
[318] Jiang Zhang, Konstantinos Psounis, Muhammad Ha-
roon, and Zubair Shafiq. HARPO: Learning to Sub-
vert Online Behavioral Advertising.In Proceed-
ings 2022 Network and Distributed System Secu-
rity Symposium. 2022. https://doi.org/10.14722/
ndss.2022.23062
[319] Jiexin Zhang, Alastair R Beresford, and Ian Sheret.
SensorID: Sensor calibration fingerprinting for smart-
phones.In 2019 IEEE Symposium on Security
and Privacy. 2019. https://doi.org/10.1109/
SP.2019.00072
[320] Jiaqian Zheng, Jing Yao, and Junyu Niu. Web
User De-Identification in Personalization.In Pro-
ceedings of the 17th International Conference on
World Wide Web. 2008. https://doi.org/10.1145/
1367497.1367666
[321] Nan Zheng, Aaron Paloski, and Haining Wang. An
Efficient User Verification System via Mouse Move-
ments.In Proceedings of the 18th ACM Conference
on Computer and Communications Security. 2011.
https://doi.org/10.1145/2046707.2046725
[322] Ke Zhong, Yiping Ma, and Sebastian Angel. Ibex:
Privacy-Preserving Ad Conversion Tracking and Bid-
ding.In Proceedings of the 2022 ACM SIGSAC Confer-
ence on Computer and Communications Security. 2022.
https://doi.org/10.1145/3548606.3560651
[323] Zhe Zhou, Wenrui Diao, Xiangyu Liu, and Kehuan
Zhang. Acoustic Fingerprinting Revisited: Generate
32

Stable Device ID Stealthily with Inaudible Sound.In
Proceedings of the 2014 ACM SIGSAC Conference
on Computer and Communications Security. 2014.
https://doi.org/10.1145/2660267.2660300
[324] Shitong Zhu, Xunchao Hu, Zhiyun Qian, Zubair Shafiq,
and Heng Yin. Measuring and Disrupting Anti-
Adblockers Using Differential Execution Analysis.
In Proceedings 2018 Network and Distributed Sys-
tem Security Symposium. 2018. https://doi.org/
10.14722/ndss.2018.23331
[325] Shitong Zhu, Umar Iqbal, Zhongjie Wang, Zhiyun
Qian, Zubair Shafiq, and Weiteng Chen. ShadowBlock:
A Lightweight and Stealthy Adblocking Browser.In
The World Wide Web Conference. 2019. https://
doi.org/10.1145/3308558.3313558
[326] Yun Zhu, Li Xiong, and Christopher Verdery.
Anonymizing User Profiles for Personalized Web
Search.In Proceedings of the 19th Interna-
tional Conference on World Wide Web. 2010.
https://doi.org/10.1145/1772690.1772886
[327] Sebastian Zimmeck. The Information Privacy
Law of Web Applications and Cloud Comput-
ing.Santa Clara High Technology Law Jour-
nal, 2013.https://digitalcommons.law.scu.edu/
chtlj/vol29/iss3/1
[328] Sebastian Zimmeck and Steven M. Bellovin. Privee:
An Architecture for Automatically Analyzing Web Pri-
vacy Policies.In Proceedings of the 23rd USENIX
Security Symposium. 2014
[329] Sebastian Zimmeck, Eliza Kuller, Chunyue Ma, Bella
Tassone, and Joe Champeau. Generalizable Active
Privacy Choice: Designing a Graphical User Interface
for Global Privacy Control.Proceedings on Privacy
Enhancing Technologies, 2024. https://doi.org/
10.56553/popets-2024-0015
[330] Sebastian Zimmeck, Jie S. Li, Hyungtae Kim,
Steven M. Bellovin, and Tony Jebara. A Privacy
Analysis of Cross-Device Tracking.In Proceed-
ings of the 26th USENIX Conference on Security
Symposium. 2017. https://www.usenix.org/
conference/usenixsecurity17/technical-
sessions/presentation/zimmeck
[331] Sebastian Zimmeck, Peter Snyder, Justin Brookman,
and Aram Zucker-Scharff. Global Privacy Control
(GPC), 2024.https://w3c.github.io/gpc/
[332] Sebastian Zimmeck, Oliver Wang, Kuba Alicki, Jo-
celyn Wang, and Sophie Eng. Usability and En-
forceability of Global Privacy Control.Proceedings
on Privacy Enhancing Technologies, 2023. https:
//doi.org/10.56553/popets-2023-0052
[333] Ali Zohaib, Jade Sheffey, and Amir Houmansadr.
Investigating Traffic Analysis Attacks on Apple
iCloud Private Relay.In Proceedings of the 2023
ACM Asia Conference on Computer and Communi-
cations Security. 2023. https://doi.org/10.1145/
3579856.3595793
A SoK Methodology
A.1 Search Criteria for Literature Review
Web tracking comprises a vast body of literature published
over the last few decades—spanning across technical mecha-
nisms, defenses, and regulatory compliance. Through our lit-
erature search (see Section 3), we obtained a list of 19438 pa-
pers along with their metadata (title, authors, year, and DOI),
missing abstracts were completed by performing a DOI-based
query on Semantic Scholar5 and OpenAlex6. To further filter
that list, we first use exclusion keywords to remove potential
papers that could be incorrectly retained under web tracking.
Exclusion Keywords:NOT [TitleORabstract: crypto*
OR blockchain* OR website fingerprint* OR “tor” OR
“poster:” OR differential* priva* OR “federated learning”
OR “membership inference” OR “trusted execution” OR
“unlearning” OR “inversion” OR multi-party computa-
tion* OR airtag* OR privacy label* OR sdk* OR “app
store” OR “google play” OR “social media” OR smart tv*
OR smart home* OR “iot” OR “virtual reality” OR “3g”
OR “4g” OR “5g” OR “wireless” OR “censorship” OR
“voice” OR “gaze” OR “eye” OR “genome” OR scam*
OR “bitcoin” OR fuzz* OR cve* OR certificate authorit*
OR public key* OR vehicle* OR robot*]
Second, two sets of inclusion keywords are used to narrow
down potential candidates for manual review. The first set
is used to filter publications that are related to web tracking
techniques and defenses based on their title and abstract text.
Inclusion Keywords for Techniques and Defenses:
[TitleORabstract: tracking OR web track* OR online
track* OR user track* OR track* user* OR web privacy
OR online privacy OR user* privacy OR user *identifi*
OR track* circumvent* OR track* eva* OR track* defen*
OR track* block* OR ad*block* OR ad* block*]
The second set of keywords is used to identify papers dis-
cussing privacy regulations and compliance in the context of
web tracking in their full text. We rely on full text search to
5https://www.semanticscholar.org/
6https://openalex.org/
33

identify papers that may not primarily be regulation-focused
(hence lower probability of a match in title or abstract), but
may still discuss regulatory implications of the studied track-
ing technique or defense in the paper.
Inclusion Keywords for Regulations and Compliance:
[Full paper: regulat* compliance OR regulation* OR
track* violat* OR privacy polic* OR privacy law* OR
privacy regulation* OR “privacy compliance” OR “gdpr”
OR “ccpa” OR “cpra” OR “cookie banner” OR “cookie
compliance” OR compliance with cookie* OR “cookie
consent” OR track* consent OR consent management*
OR opt*out OR opt* out]
A.2 Thematic Literature Analysis
We consider a paper to be atracking techniquepaper if it
provides an in-depth or foundational understanding of a spe-
cific tracking mechanism (e.g., first or reference paper on
a technique). Similarly, atracking defensepaper comprises
research that builds a system or an approach to block, pre-
vent, or defend against a tracking technique, whileregula-
tory complianceresearch discusses different aspects of public
policies (i.e., privacy regulation, standard, or guideline), their
enforcement, and perhaps limitations. Other papers focusing
on measuring the prevalence or impact of different tracking
techniques are classified asmeasurementresearch and used
throughout this SoK to support systematization of advances
in web tracking. This thematic organization is available as
part of our artifact (see our Open Science statement).
We complement our systematization of research-based
tracking defenses with industry-based ones by performing
a systematic review of changelogs and release notes for each
version of five popular browsers—Brave, Google Chrome,
Microsoft Edge (including former Internet Explorer), Mozilla
Firefox, and Apple Safari—since their creation. Specifically,
we extract tracking defense related features across stable ver-
sions of browsers based on the description of changes and
apply our defense-specific systematization criteria from Ta-
ble 2 to each defense technique. For each tracking technique
and defense technique identified, we also find and associate
community-built defenses (if any).
B Need for Fingerprinting
Constructively, fingerprinting can be thought of as a form
of intrusion detection. Web applications can learn about the
browsing environment or behavior of their first-party users
and associate it with specific user identities [175]. For exam-
ple, a website can learn that the user is using a smartphone
with specific dimensions or a desktop browser with a specific
kind of GPU. If the user’s credentials are ever stolen and an at-
tacker attempts to login to that service, the service can extract
the attacker’s fingerprint, observe a major difference against
fingerprints from prior sessions, and request additional authen-
tication data from the attacker (such as a one-time password).
The same techniques can be constructively used to differenti-
ate real users from malicious bots or attackers engaging in ad
fraud. In practice, large online services commonly incorporate
fingerprinting-derived signals into broader abuse-mitigation
pipelines to detect automated account creation, credential
stuffing, and spam. These signals are typically combined with
behavioral features and rate-limiting mechanisms, enabling
services to adapt authentication requirements based on as-
sessed risk and maintaining service integrity in adversarial
environments where traditional identifiers are unreliable.
Destructively, the same techniques that can identify user-
impersonating attackers and bots, are turned against users
who wish to remain anonymous. With fingerprinting, a web
app may be able to determine that a certain anonymous user
is in fact eponymous, since their browser fingerprint matches
that of a known user on the same platform. This undesired re-
identification occurs despite user’s attempt to hide by deleting
cookies or using the browser’s private mode. In a cross-site
context, fingerprinting can be abused to link unrelated website
visits, even when third-party cookies are disabled.
C Mixed Tracking
C.1 Mixed Tracking Techniques
Prior stateful and stateless approaches can also be combined
to track users across contexts—bridging identity across login
boundaries, devices, browsers, and native apps.
C.1.1 JavaScript-based Tracking
JavaScript can be used to read and write browser cookies
and storage for persistence by stateful techniques while also
be used to probe browser APIs to construct a fingerprint by
stateless techniques. Although JS-based approaches don’t
constitute a different tracking technique, it is included here as
a canonical example of mixed tracking in practice.
C.1.2 Authentication-based Tracking
Authentication creates a deterministic, cross-context identifier
(an account or email address) far more durable than any cookie
34

Table 6: Web tracking artifact taxonomy: mapping of tracked artifacts to artifact labels.
Artifact Label Artifacts Observed in the Literature Review
Browser Storage & Cache Cookies;Web Storage(localStorage, sessionStorage, IndexedDB);Browser Caches(HTTP, HSTS, favicon,
Alt-Svc, Service Worker, and Cache API)
JavaScript-Accessible
Browser APIs
Fingerprinting APIs(e.g., Navigator, Screen, Canvas, WebGL, AudioContext);Device APIs(Battery Status,
Media Devices, Gamepad, Speech Synthesis voices);Browser Permissions(e.g., camera, microphone)
Hardware Artifacts GPU Rendering Behavior(timing variations, memory allocation, performance counters);Sensor Calibration
Data(accelerometer or gyroscope imperfections, speaker frequency response);Clock Drift Patterns(system
time offset, TCP timestamp skew);CPU Microarchitectural State(scheduling statistics, memory footprint)
Network Protocol Artifacts IP Address;TLS/SSL Handshake Parameters(cipher suites, SNI, client certificates);TCP/IP Stack Characteris-
tics(source port selection, IP ID fields, IPv6 flow labels);DNS Records(CNAME records, reverse hostnames,
TTL values);QUIC/HTTP2+ Transport Metadata(connection IDs, retry tokens, transport parameters)
HTTP Traffic Artifacts Request Metadata, Response Content, Headers, Payload
Navigational ArtifactsURL Components(host, domain, path, query parameters);Redirect Chains
Webpage Artifacts Resources(DOM elements and their modifications, stylesheets, scripts);Interaction Patterns(click traces,
touch gesture characteristics, keystrokes, mouse movements, scroll depth, click coordinates, interaction timing);
Rendering Characteristics(font rendering, CSS feature detection, element bounding dimensions)
Identifiers Authentication IDs(OAuth tokens, SSO redirect parameters, session IDs);PII(email addresses, phone, PII
hashes);Device-specific IDs(IDFA, EMEI, MAC address);Advertiser-specific IDs(e.g., UUIDs)
or fingerprint. Logged-in users are served more third-party
trackers and personalized content [130], and logged-in pages
exhibit more fingerprinting than other pages on the same
site, suggesting trackers use authentication to link a stateless
fingerprint to stable account identifiers to extend identifica-
tion into anonymous sessions [253]. Moreover, OAuth-based
single sign-on itself routinely leaks identifying information
to identity providers and relying parties [76]. As email ad-
dresses survive cookie clears and device changes, first parties
increasingly hash and share them with advertising partners to
build cross-site identity graphs that restore the linkage that
third-party cookie restrictions were designed to prevent.
C.1.3 Cross-device Tracking
When deterministic identifiers are unavailable (e.g., logged
out state), trackers fall back to probabilistic signals to link
activity across devices—shared IP addresses, browsing pat-
terns [45], and behavioral features such as typing dynam-
ics [315]. These signals are combined into proprietarycross-
device graphs, a practice found to be largely opaque to both
users and regulators [41, 330]. Because probabilistic identi-
fiers are inherently noisy (e.g., ISPs dynamically rotate and
share public IP addresses across households), trackers apply
heuristics such as ignoring commercial, private, and proxied
IP ranges or setting temporal thresholds to filter false matches.
Open Problem: Given the lack of ground truth and diver-
sity of proprietary linking algorithms forming cross-device
identity graphs, how can cross-device tracking be reliably
measured and systematically attributed to uncover specific
signals used by different trackers?
C.1.4 Other Cross-Context Tracking
Trackers also bridge contexts within the same device. Cross-
browser fingerprinting uses OS- and hardware-level features
stable across browsers to link users across browser bound-
aries [45]. On mobile, Android Custom Tabs and Web-
Views share the browser’s cookie jar with native apps, let-
ting a tracker plants an identifier in one context that resur-
faces in the other, surviving app reinstalls and device back-
ups [306]. Recently, some native apps and in-browser scripts
have been found to silently link identities by communicating
over localhost, a channel neither the browser’s permission
model nor the OS sandbox was designed to police [303].
These vectors share a common root cause—OS- and browser-
level integration points enabling legitimate app-to-web hand-
offs that are invisible to in-browser tracking defenses.
Open Problem: Cross-context tracking exploits integration
boundaries between browsers, between apps and the web,
and between user profiles that no single platform controls
end to end. What architectural principles can unify isolation
across these boundaries without fragmenting the seamless
cross-context experiences users and developers expect?
35

C.2 Defenses Against Mixed Tracking
C.2.1 Industry-based Defenses
Against Cross-device and Cross-context Tracking.Deter-
ministic cross-device tracking through shared login accounts
is inherently difficult to defend against at the browser level,
since the user has explicitly linked their devices by authenticat-
ing. Browsers instead address the authentication pathway with
purpose-built APIs: the Storage Access API, now shipped
by all five major browsers, lets a third party request first-
party-equivalent storage explicitly. Chrome and Edge addi-
tionally support Federated Credential Management (FedCM),
which preserves single sign-on while preventing the identity
provider from learning which relying party the user logs into.
Brave blocks unrecognized identity providers by default. On
mobile, Apple’s ATT framework has required explicit opt-in
before an app can access the device’s advertising identifier
since iOS 14.5, and Google’s Privacy Sandbox for Android
proposed similar restrictions before being abandoned. How-
ever, WebViews and in-app browsers share few of the stan-
dalone browser’s tracking defenses—no extension support,
no storage partitioning, no filter-list blocking—leaving users
exposed in these embedded contexts.
Open Problem: In cases such as WebViews and in-app
browsers, can browser-level tracking protections be ex-
tended to embedded rendering engines, or does defense in
these contexts require OS-level enforcement that applies
regardless of which engine serves the page?
C.2.2 Research-based Defenses
Hardening the Identity Layer.Because cross-device and
authentication-based tracking often runs through a shared
identity provider, several proposals harden that layer directly.
SPRESSO inserts a forwarder between the relying party and
the identity provider so the provider cannot learn which site a
user logs into [88], encrypted access logging lets a service au-
dit device access without retaining a persistent identifier [224],
and identity-system reform proposals re-architect national-
and platform-level infrastructure to decouple shared identity
from cross-service activity correlation [38].
Cryptographic Advertising Proposals.A parallel line of
work shows that measurements advertisers need such as con-
version attribution and bid optimization, can be computed
without either party learning individual user data. Adnostic,
Privad, and ObliviAd demonstrated this for on-device ad se-
lection [14, 106, 288], and Ibex later extended the guarantee
to conversion attribution and bid optimization jointly using
cryptographic aggregation [322]. Few of these designs have
been adopted by browser vendors, largely due to computation
and coordination costs, but they remain the clearest evidence
that interest-based advertising does not inherently require
disclosing anything about an individual user.
C.2.3 Community-based Defenses
Universal Opt-out Signals.Several attempts were made at
implementing opt out and consent signals for users to com-
municate their privacy preferences to services. However, the
adoption and enforcement of such signals by both senders
and recipients is an unresolved coordination problem [110].
Platform for Privacy Preferences Project (P3P)[43, 61, 62,
234] enabled websites to communicate their privacy practices
to users in a standardized and fine-grained format. The P3P
specification was published by the W3C in 2002, but was
rapidly criticized for being too complex to implement or un-
derstand. Its utility was limited by the low number of sites
that were adopting it [63] and those implementing it correctly
and transparently [60, 166]. Ultimately, the specification was
officially obsoleted by the W3C in 2018.
Do Not Track (DNT)[89], proposed in 2009 as a binary opt
out signal, was adopted by every major browser but was never
given legal force. Indeed, CalOPPA, which influenced the
design of DNT, only requires online services to say whether
or not they respect it [58]. The W3C working group for DNT
closed in 2019 without industry consensus.
Global Privacy Control (GPC)[331] can be viewed as a
successor to DNT, but succeeds where DNT failed by be-
ing legally enforceable: California’s 2022 settlement with
Sephora [35] established that ignoring GPC violates the
CCPA [11], and Colorado has since imposed a similar require-
ment in 2024 [59]. Additional recognition of universal opt
outs by states like Connecticut, Montana, Oregon, and Texas
is driving broader adoption than DNT ever achieved, although
it is still slow despite people finding the signal useful and
usable [13, 329, 332]. DuckDuckGo, Brave, and Firefox send
GPC by default; Chrome added support only in 2026 [101].
As GPC is not tied to any single storage or fingerprinting
mechanism, it acts as a cross-cutting signal that covers every
technique discussed in this SoK, given a site honors it.
Open Problem: The applicability of GPC in the EU within
ePD and GDPR context is an open discussion [21,29]. Will
EU regulators incorporate GPC as an opt-out signal?
36

CA vs Sephora
23 Adds DNT header
Industrial Defenses
 2030
IE6 P3P Introduced IE8 InPrivate browsing
IE9 Adds DNT header
IE8 InPrivate filtering
Legacy Edge Birth
20 Includes InPrivate browsing + DNT
20 No TPL
IE9 Tracking Protection List (TPL) replaces InPrivate filtering
    Edge Birth
79 Disconnect-based Tracking Prevention
86 Inherits     HTTP Cache Partitioning
101-116     CHIPS + UA reduction
IE Death
Phoenix 0.1 Birth
Firefox 1.0 Birth
3.5 Private browsing
4 Adds DNT header
42 Disconnect Tracking Protection (Private)
57 Tracking Protection (all modes)
72 Disconnect FP-script blocking
63 Default-off ETP
102 URL query-params stripping
85 Network partitioning
86 Total Cookie Protection (cookie jar per site)
128 Bounce Tracking Protection
67 Default-on ETP (blocks 3P tracking cookies)
Brave Birth
0.7 Brave Shields blocks 3P ads/trackers
1.5 Farbling
1.17 CNAME defense
1.12 Grab bag: URL query-params stripping
1.21 Ephemeral partitioned 3P storage
1.35 Network partitioning
1.32 Debouncing
1.53 Forgetful browsing
1.37 Unlinkable bouncing
1.64 Simplified FP protection
Chrome 1.0 Birth
Safari 1.0 Birth 5.1 Adds DNT header
2.0 Private bowsing
1.0 Blocks 3P cookies (unvisited) 11 ML-classifier based 24hr 3P cookie limits
PS Privacy Sandbox Birth
11 ITP Introduced
13.1 Full 3P cookie blocking
89 FLoC
86 Network partitioning
83 Blocks 3P cookies Incognito
101-110 UA Reduction
17 CNAME defense
100-115 CHIPS
14.1 PCM Introduced
100-116 Protected Audience
101-115 FLoC ➔  Topics
17 Link decoration protection
17 FP API noise injection
26 ATFP made default
3P cookies retained
PS Death
17 Adv. Tracking and FP Protection (ATFP) in private
18.4 CHIPS-style cookie partitioning
105-115 Storage partitioning
138 MV3 enforcement
20052000 2015 202520202010
uBO removed from ChromeWebStore
Community Defenses
20052000 2015 20252020 2030
Adblock
2010
Research Defenses
Adblock Plus
Peter Lowe's List
since 1997
EasyList
NoScript
EasyPrivacy
Tor Browser
Ghostery
DNT header
Fanboy's Lists
Disconnect
DNT adoption
EFF Panopticlick
Fanboy ➔  EasyList
EFF Privacy badger
uBlock Origin
AdGuard
Pi-hole
WhoTracks.Me
Ghostery powers WhoTracks.Me
Industry abandons DNT
ClearURLs
NextDNS
GPC
GPC adoption
uBO protects against CNAME
DDG's Tracker Radar
Markup's Blacklight
Mullvad Browser
Filter/block list Extension
 Tool/dataset/signal
Anti-aliasing [Novak+W04]
Browser state protection [Jackson+W06]
Nymble [Johnson+P07]
IP Mixing [Raghavan+P09]
FPDetective [Acar+C13]
Identity system [Brandão+P15]
Anti-FP [Datta+W19]
AdGraph [Iqbal+I20]
SugarCoat/PageGraph [Chen+I21]
WTAGRAPH [Yang+I22] Khaleesi [Iqbal+U22] WebGraph [Siby+U22]FP-Radar [Bahrami+P22]Simulacrum [Karami+U22]
Cobweb [Amjad+C24]Unbundle-Rewrite-Rebundle [Ali+C24]FP-tracer [Boussaha+P24]Byte by Byte [Bahrami+C25]
FP-Inspector [Iqbal+I21] CV-Inspector [Le+N21]TrackerSift [Amjad+I21]XSinator [Knittel+C21]
AutoFR [Le+U23] CookieGraph [Munir+C23]JS-ByteCode [Ghasemisharif+C23] Net-track [Lee+W23]
SINBAD [Chehade+I24]
Duumviri [He+N25]Semantics-Aware Cookie Compliance [Chen+W25] CookieGuard [Bahrami+I25]TGNN [Xiong+W26]
SPRESSO [Fett+C15]
PriVaricator [Nikiforakis+W15]
TrackingFree browser [Pan+N15]
Cookie Jar [Franken+U18]
ShadowBlock [Zhu+W19]
UNIGL [Wu+U19]
PURL [Munir+U24]
Stateless
Stateful
Regulations
203020052000 2015 202520202010
since 1970s
since 1995EU/US
ePrivacy Directive (ePD)EU Data Protection Directive
Data Protection laws in several EU states GDPR
CNIL cases Digital Omnibus Proposal?Planet49 case
Safe Harbor (2000-2015) Privacy Shield (2016-2020) Data Privacy Framework (since 2023)
FTC vs Snapchat FTC vs Facebook
CCPA (CA) VA, CO, UT, CT MT, TX, OR KY, RI
IA, IN, TN, DE, NJ, NH, NE, MD, MN
Digital Markets Act (DMA) & Digital Services Act (DSA)
Federal regulation?
FTC Act
since 1994
HIPAA
since 1996
COPPA
since 1998
Gramm-Leach-Bliley Act
since 1999
Other states?
Federal State
CPRA (CA)
Figure 3: Evolution ofindustry-,community-, andresearch-baseddefenses from 2000–2026 with EU and USregulations.
37

Tracking Technique
Literature
Venue
Year
Third-party Cookie Tracking
Cookie Respawning
Cookie Syncing
First-party Cookie Tracking
Tracking Pixels/Tags
CNAME Tracking
Server-side Tracking
Link Decorations
Bounce Tracking
Authentication-based Tracking
Javascript-based Tracking
Browser Fingerprinting
Browser Extension Fingerprinting
Device Fingerprinting
Passive Fingerprinting
Kernel-based Side-channels
Network-based Side-channels
Storage-based Side-channels
Timing-based Side-channels
Behavioral Tracking
Cross-context Tracking
FLoC / Topics API
Protected Audience
Ad-Blocking Circumvention
Felten et al. [85] CCS’00 ✓
Kohno et al. [148] S&P’05 ✓
Chen et al. [57] S&P’10 ✓
Yen et al. [313] NDSS’12 ✓ ✓
Jana et al. [123] S&P’12 ✓
Nikiforakis et al. [212] S&P’13 ✓ ✓
Acar et al. [2] CCS’14 ✓ ✓ ✓ ✓
Zhou et al. [323] CCS’14 ✓
Oren et al. [223] CCS’15 ✓
Das et al. [67–69] NDSS’16 ✓ ✓
Laperdrix et al. [156] S&P’16 ✓ ✓
Jain et al. [122] PETS’16 ✓
Gonzalez et al. [100] IMC’16 ✓
Kaizer et al. [130] IMC’16 ✓ ✓ ✓ ✓
Cao et al. [45] NDSS’17 ✓ ✓
Starov et al. [273] S&P’17 ✓ ✓
Vastel et al. [299] S&P’18 ✓ ✓
Foppe et al. [90] PETS’18 ✓
Masood et al. [185] PETS’18 ✓ ✓
Olejnik et al. [220] USENIX’18 ✓ ✓
Bashir et al. [17] IMC’18 ✓ ✓
Klein et al. [142] NDSS’19 ✓ ✓
Hu et al. [113] S&P’19 ✓
Martin et al. [184] PETS’19 ✓
Sy et al. [277] PETS’19 ✓ ✓
Karami et al. [136] NDSS’20 ✓ ✓
Koop et al. [150] PETS’20 ✓
Li et al. [168] USENIX’20 ✓
Mishra et al. [200] WWW’20 ✓
Solomos et al. [266] NDSS’21 ✓
Klein et al. [141] S&P’21 ✓ ✓
Dimova et al. [75] PETS’21 ✓ ✓
Mishra et al. [199] PETS’21 ✓
Laperdrix et al. [157] USENIX’21 ✓ ✓
Chen et al. [54] WWW’21 ✓ ✓
Rye et al. [242] IMC’21 ✓
Laor et al. [154] NDSS’22 ✓ ✓
Jin et al. [127] S&P’22 ✓ ✓
Khodayari et al. [139] S&P’22 ✓ ✓
Randall et al. [233] IMC’22 ✓ ✓
Berke et al. [22] CCS’22 ✓ ✓
Solomos et al. [265] CCS’22 ✓ ✓
Ali et al. [4] NDSS’23 ✓ ✓ ✓
Nomoto et al. [217] NDSS’23 ✓ ✓
Lin et al. [173] S&P’23 ✓ ✓
Jha et al. [126] PETS’23 ✓ ✓
Kol et al. [149] USENIX’23 ✓ ✓
Snyder et al. [261] USENIX’23 ✓ ✓ ✓
Su et al. [275] WWW’23 ✓ ✓
Beugin et al. [26] PETS’24 ✓ ✓
Fouad et al. [92] PETS’24 ✓
Chehade et al. [51] USENIX’25 ✓ ✓
Wessels et al. [306] USENIX’25 ✓ ✓
Huyghe et al. [116] WWW’25 ✓ ✓
Bekos et al. [19] CCS’25 ✓ ✓
Ukani et al. [293] CCS’25 ✓ ✓ ✓ ✓
Table 7: Literature on papers studying web tracking techniques over the years.
38

Tracking Technique
Literature
Browser Storage and Cache
JavaScript-Accessible Browser APIs
Webpage Artifacts
Hardware Artifacts
Network Protocol Artifacts
HTTP Traffic Artifacts
Navigational Artifacts
Identifiers
Felten et al. [85] T E I
Kohno et al. [148] O O
Chen et al. [57] O
Yen et al. [313] T E I O I S O
Jana et al. [123] O
Nikiforakis et al. [212] E I E I S
Zhou et al. [323] E
Acar et al. [2] T E I E I S S T S
Oren et al. [223] E E
Das et al. [67–69] E E
Laperdrix et al. [156] E I E I S
Jain et al. [122] O O
Gonzalez et al. [100] O O
Kaizer et al. [130] T I E I S T
Cao et al. [45] E I E E
Starov et al. [273] I E
Vastel et al. [299] E I E I S
Foppe et al. [90] O O
Masood et al. [185] E I E
Olejnik et al. [220] E
Bashir et al. [17] T E I I S
Klein et al. [142] E I O
Hu et al. [113] T I I S S T S
Sy et al. [277] O O
Martin et al. [184] O O
Karami et al. [136] I E I S
Koop et al. [150] T I S
Li et al. [168] I I S S
Mishra et al. [200] T O I S
Solomos et al. [266] T
Klein et al. [141] O O
Mishra et al. [199] T I I S
Dimova et al. [75] T I S I S
Laperdrix et al. [157] E I E
Chen et al. [54] T I E I S
Rye et al. [242] O
Laor et al. [154] E I E E
Khodayari et al. [139] T S
Jin et al. [127] E E
Randall et al. [233] T E I E I S S T S
Berke et al. [22] E
Solomos et al. [265] E I E
Nomoto et al. [217] E
Ali et al. [4] T
Lin et al. [173] E I E
Jha et al. [126] E
Kol et al. [149] O O
Snyder et al. [261] T E
Su et al. [275] E I E
Beugin et al. [26] E
Fouad et al. [92] T I S I S
Chehade et al. [51] I E I S
Wessels et al. [306] T T
Huyghe et al. [116] E I E
Ukani et al. [293] T E I E
Bekos et al. [19] T E I E I S S
Table 8: Tracker capabilities exercised over artifacts as studied
in each tracking techniques related paper.
Tracking Defense
Literature
(Defense System Name)
Venue
Year
Deployment Type
ML-based
Program Instrum.
Circumvention-based
LLM-based
API Perturbation
State Partitioning
Network Modif.
Cryptographic
Anti-aliasing [219] WWW’04 ● ✓
Browser state protection [121] WWW’06 ● ✓ ✓
XSS Prevention with Taint [304] NDSS’07 ● ✓
Nymble [128] PETS’07 ● ▲ ✓
De-identification [320] WWW’08 ▲ ✓
IP Address Mixing [232] PETS’09 ▲ ✓
UPS anonymization [326] WWW’10 ◆ ▲ ✓
FPDetective [3] CCS’13 ❍ ✓
Privee [328] USENIX’14 ❍ ✓
SPRESSO [88] CCS’15 ● ▲ ✓
UCognito [311] CCS’15 ● ✓
Bloom Cookies [202] NDSS’15 ◆ ▲ ✓
TrackingFree Browser [226] NDSS’15 ● ✓
Auto-blacklist [105] PETS’15 ◆ ❍ ✓
Identity System Reform [38] PETS’15 ▲ ✓
PriVaricator [211] WWW’15 ● ✓
TrackMeOrNot [197] WWW’16 ◆ ✓
One-class tracker classifier [117] PETS’17 ❍ ✓
Anti-adblock diff. exec. [324] NDSS’18 ● ❍ ✓ ✓
NoMoAds [256] PETS’18 ▲ ✓ ✓
AdVersarial [290] CCS’19 ▲ ✓
UNIGL [309] USENIX’19 ● ✓ ✓
ShadowBlock [325] WWW’19 ● ✓
AdGraph [119] S&P’20 ● ❍ ✓
NoMoATS [255] PETS’20 ▲ ✓
TFO-TLS Enhancement [278] PETS’20 ▲ ✓
XSinator [146] CCS’21 ❍ ✓
FP-Inspector [118] S&P’21 ● ❍ ✓
SugarCoat/PageGraph-based [56] S&P’21 ● ❍ ✓ ✓
TrackerSift [7] IMC’21 ❍ ✓
CV-Inspector [160] NDSS’21 ❍ ✓ ✓
MAC Randomization [86] PETS’21 ▲ ✓
ML-CB [235] PETS’21 ◆ ✓
Ibex [322] CCS’22 ● ▲ ✓
WTAGRAPH [312] S&P’22 ● ◆ ✓
HARPO [318] NDSS’22 ◆ ✓
FP-Radar [16] PETS’22 ❍ ✓
Khaleesi [120] USENIX’22 ◆ ✓
Simulacrum [137] USENIX’22 ● ✓
WebGraph [257] USENIX’22 ● ❍ ✓
CGC [229] WWW’22 ❍ ✓
AdCPG [161] CCS’23 ❍ ✓ ✓
CookieGraph [207] CCS’23 ● ❍ ✓
GDPR Runtime [143] CCS’23 ▲ ✓
JS-ByteCode [97] CCS’23 ❍ ✓ ✓
FP-Sandbox [286] S&P’23 ● ✓
Tracking JS blocking [8] PETS’23 ● ✓
AutoFR [159] USENIX’23 ◆ ❍ ✓
Net-track [162] WWW’23 ▲ ✓
Cobweb [6] CCS’24 ● ◆ ✓
Unbundle-Rewrite-Rebundle [5] CCS’24 ◆ ✓
SINBAD [107] S&P’24 ❍ ✓
Browser Polygraph [131] IMC’24 ▲ ✓
FP-tracer [37] PETS’24 ● ✓
User-Controlled Privacy [115] PETS’24 ● ✓
PURL [206] USENIX’24 ● ❍ ✓
AdFlush [163] WWW’24 ◆ ✓
PanoptiChrome [134] WWW’24 ● ✓
Byte-level FP Detection [15] CCS’25 ❍ ✓ ✓
CookieGuard [214] IMC’25 ● ◆ ✓
Duumviri [254] NDSS’25 ◆ ❍ ✓ ✓
CSAL [224] USENIX’25 ● ▲ ✓
Semantics-aware Cookies [52] WWW’25 ❍ ✓
AdVersa [171] WWW’26 ◆ ✓
TGNN [310] WWW’26 ❍ ✓
Table 9: Defense deployment and mechanism types for track-
ing defense literature. Deployment: ● in-browser; ◆ browser
extension;▲infrastructure-level;❍offline.
39

Table 10:Industrial and community defenses against stateful trackingacross two defense goals: detection & blocking and
signal reduction & obfuscation . Protects against:
 : Cookie-based tracking,
 : Navigational tracking,
 : Fingerprinting,
 :
JavaScript-based tracking,
 : Side-channels. “(D)” is by-default, “(P)” is private-mode only, and “(O)” is opt-in based.
Defense Technique
(Protects Against) Brave Chrome Edge Firefox Safari Community Defense
Blocking
3P cookies/storage
 all 3P cookies and storage
blocked via Shields (D)
3P cookies and storage
blocked in Incognito (P)
known tracker 3P cookies
blocked (D)
known tracker 3P cookies
blocked in ETP stnd. (D);
all 3P cookies blocked in
ETP Strict (D)
all 3P cookies and storage
blocked (D)
Tor blocks 3P cookies and
storage
uBO, Privacy Badger,
AdGuard, Ghostery blocks
known tracker cookies via
filter lists
Partitioning
3P cookies/storage
uses Chromium’s storage
partitioning;
ephemeral 3P cookies/stor-
age cleared on tab close
(D)
opt-in partitioned cookies
via Partitioned attribute:
CHIPS;
storage partitioned by top-
level site (D)
uses Chromium’s CHIPS
and its storage partitioning
(D)
Total Cookie Protection:
separate cookie jar per top-
level site for all embedded
3P origins;
all storage APIs isolated
per top-level site (D)
Partitioned cookie at-
tribute supported;
Access to the 3P storage re-
stricted under ITP;
Storage API provides a
controlled opt-in (D)
—
Blocking
1P tracking cookies/storage
 Brave Shields blocks 1P-
disguised trackers via filter
lists (D)
NA NA NA
ITP purges 1P cookies
from classified trackers af-
ter inactivity (D)
uBO and AdGuard sup-
ports targeted deletion of
known 1P tracking cookies
via filter rules and scriptlets
Limiting
1P cookie/storage lifetime
Caps lifetime of script-set
cookies to 7 days;
Forgetful Browsing auto-
clears 1P storage per-site
(O)
NA NA NA
all script-set 1P cookies/s-
torage expire after 7 days
without interaction;
Expiry reduced to 24h
when link decoration is de-
tected (D)
—
HTTP cache partitioning
 Inherits Chromium cache
partitioning (D)
Cache keyed by top-level
site (D)
Inherits Chromium cache
partitioning (D)
Network partitioning in-
cludes cache isolation per
top-level site (D)
ITP’s isolation addresses
cache-based tracking vec-
tors (D)
—
Network state partitioning
 Network state partitioned
(D)
Included with broader par-
titioning effort (D)
Inherits Chromium net-
work partitioning (D)
TLS sessions, DNS cache,
HSTS, OCSP, connections
all isolated per top-level
site (D)
Isolation at network-level
under ITP’s tracking pre-
vention framework (D)
—
URL parameter stripping
 Strips the known tracking
query parameters (D) NA NA
Query-parameter stripping
for known tracking param-
eters in ETP Strict and Pri-
vate Browsing (O)
ITP detects link decora-
tion and reduces script-
writable storage lifetime
from 7 to 24 hours (D);
ATFP’s link tracking pro-
tection strips params (P)
ClearURLs strips utm_*,
gclid, fbclid
DuckDuckGo strips by de-
fault
Referrer policy restrictions
 Strict referrer policy strips
cross-origin referrer detail
(D)
Defaults to strict-origin-
when-cross-origin (D)
Inherits Chromium referrer
policy (D)
Defaults to strict-origin-
when-cross-origin (D)
Defaults to strict-origin-
when-cross-origin (D)
AdGuard stealth strips re-
ferrers;
uBO can modify referrer
headers via dynamic filter-
ing
Blocking
CNAME-cloaked trackers
 Blocks CNAME-cloaked
trackers (D) NA NA
NA;
uBO performs CNAME
uncloaking through the
browser.dnsAPI
ITP applies CNAME/IP
heuristics for detecting
cloaked 3P hosts;
ATFP blocks CNAME-
cloaked trackers (D)
uBO performs CNAME un-
cloaking (only Firefox);
AdGuard does CNAME
resolution;
Extension-based defenses
lack full DNS visibility
Protecting
against bounce tracking
Debouncing skips known
bounce-tracker redirects;
Unlinkable bouncing rou-
tes visits through tempo-
rary unlinkable storage (D)
Heuristics-based deletion
of site storage for bounce
domains without any recent
user interaction (D)
NA
ETP Strict uses blocklists;
deletes storage without re-
cent interaction (D)
Behavioral heuristics for
deletion of storage for sus-
pected trackers lacking le-
gitimate interaction (D)
—
Blocking known trackers
via filter/block lists
 Shields blocks known 3P
ads, trackers, crypto (D) NA
Balanced and Strict mode
blocks trackers from Dis-
connect list (D)
ETP blocks trackers from
Disconnect list (D)
ITP and ATFP blocks kn-
own and CNAME-cloaked
trackers (D)
List: easylist, easyprivacy,
disconnect, Fanboy’s lists,
Peter Lowe’s list, AdGuard
lists, DuckDuckGo Tracker
Radar;
Extension: Ghostery, Ad-
Guard, Privacy Badger,
uBO;
DNS: Pi-hole, NextDNS
ML-based
ad/tracker blocking
 PageGraph detects trackers
via page-level graph analy-
sis (D)
NA NA NA
ITP uses ML classifier to
identify tracking domains
from cross-site loading pat-
terns (D)
Privacy Badger learns fr-
om observed cross-site be-
havior;
Blacklight scans sites for
trackers and fingerprinting
40

Table 11:Industrial and community defenses against stateless trackingacross defense goals: detection & blocking and
signal reduction & obfuscation . Protects against:
 : Cookie-based tracking,
 : Navigational tracking,
 : Fingerprinting,
 :
JavaScript-based tracking,
 : Side-channels. “(D)” is by-default, “(P)” is private-mode only, and “(O)” is opt-in based.
Defense Technique
(Protects Against) Brave Chrome Edge Firefox Safari Community Defense
Masking or hiding
IP address
 Private Window with Tor
routes traffic through Tor
network (O)
IP Protection hides IP via
two-hop proxy system (P)
(discontinued)
NA NA; Mozilla VPN available iCloud’s Private Relay routes Safari traffic via two relays to hide IP (O) Tor Browser routes all traf- fic via onion network
Reducing
User-Agent string
 Inherits Chromium UA re-
duction (D)
UA reduction and UA
Client Hints (D)
Inherits Chromium UA re-
duction and Client Hints
(D)
Uses the reduced form of
Gecko UA string; resist-
fingerprinting feature re-
ports generic UA (D)
Freezes Safari version in
UA string; limits exposed
platform detail (D)
AdGuard’s Stealth Mode
can override UA
Blocking
fingerprinting scripts
PageGraph records page
execution for fingerprint-
ing detection;
Shields blocks known fin-
gerprinting scripts (D)
NA
Fingerprinting tracker blo-
cking via Disconnect lists
(D)
Fingerprinting script blo-
cking via Disconnect lists
(D)
ATFP blocks known finger-
printing scripts (P)
NoScript blocks JS (D);
uBO, AdGuard block fin-
gerprinting domains;
Privacy Badger detects fi-
ngerprinting-like behavior
Normalizing
browser API outputs
 NA NA NA
resist-fingerprinting stan-
dardizes API outputs to
uniform values for system
specs like hardware and
screen metrics (O)
ATFP normalizes fonts,
plugins, UA (D);
ATFP standardizes some
outputs such as screen, win-
dow, hardware metrics by
default in private mode (O)
Tor normalizes API outputs
for a uniform fingerprint
Mullvad Browser applies
same hardening for non-
Tor use (D)
Randomizing
browser API outputs
Farbling does site-specific
randomization of API out-
puts via noise injection so
that fingerprint changes per
page load (D)
NA NA
Randomizes API outputs
of Canvas, JS floating po-
int math operations, and pe-
ripheral touch support (D)
ATFP injects noise to au-
dio, canvas, WebGL by de-
fault in private mode (O)
—
Reducing precision
of browser API outputs
 Reduces timer’s precision
(D)
Reduces
performance.now resolu-
tion (D)
Inherits Chromium timer
precision reductions (D)
Reduces event time and
performance.now preci-
sion
resist-fingerprinting mode
applies broader reductions
by injecting noise into dy-
namic hardware hooks like
Canvas and timer (D)
Reduces timer’s precision
(D) —
Removing or declining
fingerprintable APIs
 Restricts or disables the
fingerprinting-prone APIs
where feasible (D)
Removed Battery Status
API (D)
Inherits Chromium API re-
movals (D)
Removed Battery Status
API; declined Network In-
formation API (D)
Declined Network Informa-
tion API, Web Bluetooth;
WebKit policy considers
fingerprinting impact for
new APIs (D)
—
Blocking JavaScript
 Brave Shields allows per-
site script blocking; aggres-
sive mode blocks all scripts
(O)
Available via site settings
(O)
Available via site settings
(O)
Available via about:config
and site permissions (O)
Available via site settings
(O)
NoScript blocks JS by de-
fault per-site; highly effec-
tive but significant usability
burden
Neutralization of
mixed scripts
SugarCoat generates rep-
lacement scripts preserv-
ing the functionality while
neutralizing tracking (D)
NA NA
NA;
uBO scriptlets can override
specific functions
NA —
Defending against
Extension fingerprinting
 Randomizes artifacts de-
tectable by extensions (D) NA NA
Extension APIs somewhat
isolated but not fully hard-
ened
Extensions are run within
sandboxed context with
limited web-accessible re-
sources (D)
—
Side-channel defenses
 Inherits Chromium miti-
gations;
Shields provides additio-
nal isolation (D)
Site Isolation COOP/
COEP headers;
State partitioning (D)
Inherits Chromium Site
Isolation & COOP/COEP
(D)
Site Isolation (Fission);
Network partitioning;
Reduced timer precision
(D)
Process-per-tab isolation
ITP state partitioning (D) —
41

Table 12:Evolution of industry-driven tracking defenses across different browsers.
 : Cookie-based tracking,
 : Naviga-
tional tracking,
 : Fingerprinting,
 : JavaScript-based tracking,
 : Side-channels,
 : Privacy proposals.
Browser Release Date Browser Version Protects Against Description of the Introduced Tracking Defenses
Aug 2001 6
 P3P support; 3P cookies restricted by default unless an acceptable P3P compact policy is present
Mar 2009 8
 Introduced InPrivate Browsing and InPrivate Filtering (blocks 3P content loaded across>10 sites)
Mar 2011 9
 Tracking Protection Lists (TPL) replaces InPrivate Filtering; Do Not Track (DNT) support added
Jun 2022 11 — Last IE 11 desktop app retired and disabled, redirecting to Microsoft Edge
Jul 2015 20 — Edge launches with Windows 10, InPrivate browsing, and DNT; drops IE’s TPL
Jan 2020 79
 Chromium Edge with Disconnect-based blocking; blocks cryptomining+fingerprinting trackers
Oct 2020 86
 Inherits Chromium HTTP cache partitioning
2022–2023 101–116
 Inherits Chromium User-Agent reduction (reduced UA string; UA Client Hints)
May 2023 114
 Inherits Chromium CHIPS (partitioned 3P cookies)
Aug 2023 115
 Inherits Chromium Storage Partitioning
Jun 2024 139 — Inherits Chromium Manifest V3 enforcement; MV2 ad/tracker blockers phased out
Sep 2002 0.1
 Launch of Phoenix 0.1 with basic cookie management
Nov 2004 1
 Launch of Firefox 1.0: cookie manager with exceptions; option to block 3P cookies
Jun 2009 3.5 — Private Browsing mode introduced
Mar 2011 4 — Do Not Track (DNT) header adopted; first browser to implement DNT
Nov 2015 42
 Tracking Protection blocks known trackers in Private Browsing using Disconnect list
Nov 2017 57
 Tracking Protection available outside Private Browsing (optional)
Oct 2018 63
 Enhanced Tracking Protection (ETP) introduced (off by default)
Jun 2019 67
 ETP turned on by default for new installs (Standard mode)
Jan 2020 72
 Fingerprinting-script blocking enabled by default via Disconnect’s fingerprinting list
Jul 2020 79
 Basic redirect (bounce) tracking protection introduced
Jan 2021 85
 Supercookie protection via network partitioning (caches/connections isolated per top-level site)
Feb 2021 86
 Total Cookie Protection introduced (separate cookie jar per website under ETP Strict)
Jun 2022 102
 URL query-parameter stripping for known tracking parameters (ETP Strict and Private Browsing)
Aug 2024 128
 Bounce Tracking Protection introduced to ETP Strict
Jun 2003 1
 Launch of Safari 1.0: blocks 3P cookies from unvisited sites by default
Apr 2005 2 — Private Browsing mode introduced; first browser to offer it
Jul 2011 5.1 — DNT header support added
Sep 2017 11
 ITP 1.0: ML identifies tracking cookies; 24h 3P cookie window; purges 30d+ unused cookies
Sep 2019 13
 ITP 2.3: 7-day cap on all script-writable storage to counter storage and link-decoration tracking
Mar 2020 13.1
 Complete 3P cookie blocking enabled by default; first mainstream browser to block all 3P cookies
Apr 2021 14.1
 Private Click Measurement (PCM) enabled by default for privacy-preserving ad click attribution
Sep 2023 17
 Advanced Tracking and Fingerprinting Protection (ATFP) in Private Browsing: Link Tracking Protection, API noise
injection, blocks known/CNAME-cloaked trackers
Mar 2025 18.4
 Support for the CHIPS-styled partitioned cookie attribute introduced
Sep 2025 26
 Advanced Fingerprinting Protection extended to default (non-Private) browsing
Dec 2008 1 — Launch of Chrome 1.0 stable: Incognito mode
Nov 2012 23 — DNT header support added
Aug 2019 —
 Privacy Sandbox initiative announced
May 2020 83
 3P cookies blocked by default in Incognito mode; new cookie controls
Oct 2020 86
 HTTP cache partitioning (cache keyed by top-level site)
Apr 2021 89
 FLoC origin trial begins (interest cohorts as a 3P cookie alternative)
Jan 2022 101–115 (OT)
 FLoC abandoned; Topics API proposed as replacement
Apr 2022 100–116 (OT)
 FLEDGE in-browser ad-auction origin trial begins
Jun 2022 101–110 (OT)
 UA Reduction introduced: browser minor version reduced to 0.0.0 in the UA string
May 2023 100–115 (OT)
 ,
 CHIPS (Cookies Having Independent Partitioned State) introduced
Aug 2023 105–115 (OT)
 Storage Partitioning (localStorage, IndexedDB, CacheStorage partitioned by top-level site)
Apr 2025 —
 Google drops planned 3P cookie prompt; cookies remain; deprecation effort ended
Sep 2025 138 — Manifest V3 enforcement; MV2 ad/tracker blockers phased out
Oct 2025 —
 Privacy Sandbox APIs (Topics, Protected Audience, Attribution Reporting, etc.) retired
Jan 2016 0.7
 Developer preview: blocks 3P ads/trackers and 3P storage by default; HTTPS Everywhere
Nov 2019 1
 Launch of Brave 1.0: Shields blocks 3P ads/trackers, cross-site cookies, and fingerprinting by default
Mar 2020 1.5
 Fingerprint randomization (farbling) introduced
Jul 2020 1.12
 URL query-parameter stripping, stricter referrer policy, Reporting API limits
Jul 2020 1.17
 Defense against CNAME-cloaked trackers
Feb 2021 1.21
 Ephemeral 3P site storage (partitioned and cleared when site closes)
Oct 2021 1.32
 Debouncing introduced; skips known bounce-tracker redirects
Dec 2021 1.35
 Partitioning of network state
Mar 2022 1.37
 Unlinkable Bouncing: routes suspected-site visits through temporary, unlinkable storage
May 2023 1.53
 Forgetful Browsing: auto-clear first-party storage per-site
Jan 2024 1.64
 Simplified fingerprinting protections
42

Table 13:Timeline of community-driven tracking defenses.
 : Filter/block list,
 : Browser extension,
 : represents tools,
standards, dataset, or browser.
Year Community Defense Type Description
1997 Peter Lowe’s list (pgl.yoyo.org)
 Initially created for personal local DNS use, this crowdsourced adblock list is widely consumed by hosts files, Pi-hole, AdGuard, uBO
2002 Adblock
 Ad blocking extension created for Firefox; later replaced by its successors
2005 EasyList
 Created as a maintainable ad-blocking subscription for the Adblock extension; has become the de-facto core ad filter list
2005 NoScript
 Blocks JavaScript content by default per-site, cutting JS-based tracking and fingerprinting
2006 Adblock Plus (Eyeo)
 Adblock extension re-written as Adblock Plus with subscribable filter lists (e.g. EasyList)
2006 EasyPrivacy
 Companion list to EasyList targeting trackers, analytics, tracking pixels/beacons, and web bugs (not just ads)
2008 Tor Browser (Tor Project)
 Reference anti-fingerprinting and onion-routing browser; provides first-party isolation and uniform fingerprint (one-fingerprint-for-all)
2009 Ghostery
 Detects and (optionally) blocks 3P trackers; also exposes who is tracking on each page
2009 Do Not Track (DNT)
 Proposed by researchers as a browser header to opt out of cross-site tracking
2010 Fanboy’s Annoyance List
 List targeting cookie-consent notices, social-media widgets, and in-page annoyances (basis for EasyList Cookie List)
2010 EFF Panopticlick
 EFF tool demonstrating browser fingerprint uniqueness and tracker exposure
2011 Disconnect
 List blocks 3P trackers; its open tracker list got later on adopted by Firefox, Safari, and Edge
2011 Do Not Track (DNT)
 Implemented by Firefox, IE, Safari, Opera, then Chrome; W3C Tracking Protection WG chartered to standardize it
2013 Fanboy→EasyList
 Fanboy’s List merged into EasyList, consolidating the dominant English ad-filter lists
2014 Privacy Badger (EFF)
 Heuristic tracker blocker that learns about trackers from observed cross-site behavior rather than a static list
2014 uBlock Origin
 uBlock released for Chrome/Opera
2014 AdGuard
 Extension blocks ad/tracker domains based on various lists; Stealth Mode strips referrers, 3P cookies, and reduces fingerprinting surface
2014 Pi-hole
 Open-source network-wide DNS sinkhole (Raspberry Pi); blocks ad/tracker domains for an entire network via DNS
2017 WhoTracks.me
 Open dataset and reporting of trackers’ prevalence and behavior across the web
2018 Ghostery powers WhoTracks.Me
 Ghostery goes open source; powers the WhoTracks.me tracker dataset
2019 Do Not Track (DNT)
 W3C Tracking Protection Working Group closed without DNT adoption; DNT effectively abandoned by industry
2019 ClearURLs
 Strips known tracking parameters (e.g. utm_*, gclid, fbclid) from URLs before requests and on copy
2019 NextDNS
 Cloud DNS resolver with configurable ad/tracker blocklists, applied across devices/browsers
2019 uBO protects against CNAME
 uBO (Firefox) adds CNAME-uncloaking to defeat first-party-disguised (CNAME-cloaked) trackers; advanced dynamic filtering/scriptlets
2020 Global Privacy Control (GPC)
 EFF-led universal opt-out signal; legally enforceable under CCPA/CPRA; adopted by DuckDuckGo, Brave, Abine, Firefox
2020 DuckDuckGo Tracker Radar
 Open, auto-generated tracker dataset (domains→owners→behaviors); powers DDG protections, Vivaldi, and Blacklight
2020 Blacklight
 Markup’s web tool that scans any site and reports trackers, cookies, session recorders, pixels, and fingerprinting
2022 GPC Adoption
 California Sephora settlement establishes that ignoring GPC violates CCPA, driving site adoption
2023 Mullvad Browser
 Tor Project + Mullvad: Tor Browser’s anti-fingerprinting hardening for everyday (non-Tor-network) use
2025 uBO removed from Chrome
 uBO removed from the Chrome Web Store as Chrome disables MV2 extensions by July 2025; remains full-featured on Firefox/Brave
Table 14: Taxonomy of policies along with their distribution across the literature (# = paper count).
EU Regulation #
GDPR 27
ePrivacy Directive (ePD) 9
Digital Services Act (DSA) 3
Digital Markets Act (DMA) 1
(a) EU Regulations
US Regulation #
CCPA (California) 11
CPRA (California) 3
Other states 2
FTC Act or COPPA (Federal) 2
(b) US Regulations
Standard #
GPC 5
P3P 3
DNT 3
IAB TCF or CCPA Compliance Framework 3
(c) Opt-Out Signals and Industry Frameworks
Table 15: Taxonomy of policy aspects (along with its distribution across literature) mapped onto rights and context applicability.
Right to
Policy Aspect
# Paper count
Access
Portability
Correct
Delete
Opt-out
ConsentGDPR/ePD Context CCPA/CPRA Context
User Consent 18 ✓Opt-in design✗Opt-out design
Notice 8 ✓Prelude for consent✓Disclosure requirements
Sharing & Consent Propagation 7 ✓Processor obligations✗Third-party notices
Opt-out Sale 6 ✗Opt-in design✓Opt-out design
Data Access Request 5 ✓Controller must provide info.✓Requests to know
Data Minimization 4 ✓Processing principle✓CPRA amendment
Legitimate Interest Exemption 5 ✓Specific purposes only✗No equivalent
Data Storage (persistence) 3 ✓Storage limitations✓Retention schedules
Privacy by Design 1 ✓By design and by default✓CPRA amendment
43
