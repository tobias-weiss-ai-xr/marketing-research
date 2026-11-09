---
title: 'The DSA''s Blind Spot: Algorithmic Audit of Advertising and Minor Profiling on TikTok'
url: https://arxiv.org/abs/2603.05653
category: digital-marketing
subcategory: empirical
date: 2026-03
venue: ''
authors:
- Sara Solarova
- Matej Mosnar
- Matus Tibensky
- Jan Jakubcik
- Adrian Bindas
source: arxiv
pdf_url: https://arxiv.org/pdf/2603.05653
pages: 16
chars: 91413
fetched_at: '2026-11-08T12:58:59+00:00'
kb_version: 1
---

# The DSA's Blind Spot: Algorithmic Audit of Advertising and Minor Profiling on TikTok

The DSA’s Blind Spot: Algorithmic Audit of Advertising and
Minor Profiling on TikTok
Sara Solarova
Kempelen Institute of Intelligent
Technologies
Bratislava, Slovakia
sara.solarova@kinit.sk
Matej Mosnar
Kempelen Institute of Intelligent
Technologies
Bratislava, Slovakia
matej.mosnar@kinit.sk
Matus Tibensky
Kempelen Institute of Intelligent
Technologies
Bratislava, Slovakia
matus.tibensky@kinit.sk
Jan Jakubcik
Kempelen Institute of Intelligent
Technologies
Bratislava, Slovakia
jan.jakubcik@kinit.sk
Adrian Bindas
Kempelen Institute of Intelligent
Technologies
Bratislava, Slovakia
adrian.bindas@kinit.sk
Simon Liska
Kempelen Institute of Intelligent
Technologies
Bratislava, Slovakia
simon.liska@kinit.sk
Filip Hossner
Kempelen Institute of Intelligent
Technologies
Bratislava, Slovakia
filip.hossner@kinit.sk
Matúš Mesarčík
Kempelen Institute of Intelligent
Technologies
Bratislava, Slovakia
Comenius University Bratislava
Bratislava, Slovakia
matus.mesarcik@kinit.sk
Ivan Srba
Kempelen Institute of Intelligent
Technologies
Bratislava, Slovakia
ivan.srba@kinit.sk
Abstract
Adolescents spend an increasing amount of their time in digital en-
vironments where their still-developing cognitive capacities leave
them unable to recognize or resist commercial persuasion. Article
28(2) of the Digital Service Act (DSA) responds to this vulnerabil-
ity by prohibiting profiling-based advertising to minors. However,
the regulation’s narrow definition of “advertisement” excludes cur-
rent advertising practices including influencer paid partnerships
and brand promotional content that serve functionally equivalent
commercial purposes. We provide the first empirical evidence of
how this definitional gap operates in practice through an algorith-
mic audit of TikTok. Our approach deploys sock-puppet accounts
simulating a pair of minor and adult users with matching interest
profiles. The content recommended to these users is automatically
annotated, enabling systematic statistical analysis across four video
categories: containing formal, disclosed, undisclosed advertisement
and non-advertisement; as well as advertisement topical relevance
to user’s interest. Our findings reveal a stark regulatory paradox.
TikTok demonstrates formal compliance with Article 28(2) by shield-
ing minors from profiled formal advertisements, yet both disclosed
and undisclosed ads exhibit significant profiling aligned with user
interests (5-8 times stronger than for adult formal advertising). The
strongest profiling emerges within undisclosed commercial content,
where creators/brands fail to label paid partnership/promotional
This work is licensed under a Creative Commons Attribution 4.0 International License.
FAccT ’26, Montreal, QC, Canada
©2026 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-2596-8/2026/06
https://doi.org/10.1145/3805689.3812355
content and the platform neither corrects this omission nor pre-
vents its personalized delivery to minors. These results demonstrate
that minors remain exposed to algorithmically targeted commer-
cial content through the same recommendation mechanisms the
DSA seeks to constrain. We argue that protecting minors requires
expanding the definition of advertisement in EU law to encompass
influencer and brand promotional content, and ensuring that any
such expansion is accompanied by a corresponding prohibition on
profiling-based targeting of minors, so that commercial content
cannot circumvent protections merely by operating outside formal
advertising channels.
CCS Concepts
•Human-centered computing → HCI design and evaluation
methods;Collaborative and social computing design and evalua-
tion methods;•Social and professional topics→Computing /
technology policy.
Keywords
Digital Services Act, advertisement, algorithmic auditing, minor
profiling, TikTok
ACM Reference Format:
Sara Solarova, Matej Mosnar, Matus Tibensky, Jan Jakubcik, Adrian Bindas,
Simon Liska, Filip Hossner, Matúš Mesarčík, and Ivan Srba. 2026. The DSA’s
Blind Spot: Algorithmic Audit of Advertising and Minor Profiling on TikTok.
InThe 2026 ACM Conference on Fairness, Accountability, and Transparency
(FAccT ’26), June 25–28, 2026, Montreal, QC, Canada.ACM, New York, NY,
USA, 16 pages. https://doi.org/10.1145/3805689.3812355
arXiv:2603.05653v2  [cs.CY]  9 May 2026

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Solarova et al.
1 Introduction
A teenager on TikTok today interacts in a fundamentally different
information environment than most adults did when they first
opened social media. A decade ago, feeds had natural limits. Users
saw what their contacts posted, and when posting stopped, so did
the feed. Today, content loads immediately as an endless stream,
shaped by everything a user has ever watched, liked or lingered on.
There is effectively no moment when the feed runs out, no natural
stopping point. Nor do users have meaningful visibility into what
the algorithm has learned about them and how it operates. And
within this endless stream, the line between entertainment and
advertisement (hereafter also ads) has effectively disappeared.
For adults, this blurring is confusing. For children, it may be not
only problematic but also harmful. Decades of research, on food
marketing to children [6, 9, 29], gambling-like design of the apps
and adolescent behaviour [36, 44], adolescent brain development
[13, 35, 51] and minors advertising literacy [33, 39, 40, 45, 59, 60]
demonstrate that minors lack the cognitive defences against ads
that adults have developed.
Platforms like TikTok are where these vulnerabilities meet com-
mercial interests. TikTok has 169 million monthly active users in
the EU [55], and among young Europeans it has become a primary
channel for information: 64 percent of 15-24 year-olds now cite
social media as their main source of information overall [ 21]. In
2024, TikTok generated approximately€21 billion in revenue and
the vast majority was from advertising [8]. Attention has become
the commodity, where advertising is the revenue and the algorith-
mic feed exists to maximise both. The algorithm infers interests,
insecurities, and aspirations from behavioural signals invisible to
anyone but the platform. Minors no longer scroll through content
from friends but from brands and influencers, much of it packed
with ads, sometimes disclosed but often undisclosed. While the
platforms provide disclosure tools, creators rarely use them, often
burying commercial indicators in hashtags effectively invisible to
users. At the EU level, only 20 percent of influencers systematically
indicate the commercial nature of their content [17].
The European Union has recognised these harms in the Digital
Services Act (DSA), which entered into force in 2024 and introduced
Article 28(2), which prohibits online platforms, including Very Large
Online Platforms (VLOPs) and Very Large Search Engines (VLOSEs),
from presenting ads based on profiling when they know “with
reasonable certainty” that the user is a minor. The intent is clear:
minors shall not be targeted with personalised advertising. But the
prohibition contains a critical gap. Article 3(r) of the DSA defines
“advertisement” narrowly, covering only ads purchased through a
platform’s ad system for which a platform is directly paid (hereafter:
formal ads) [26]. This definition does not capture brand or influencer
marketing, affiliate content, or unlabelled commercial posts, which
are precisely the formats that dominate what minors actually see.
Minors should be able to participate in online spaces without
being manipulated, exploited, or exposed to risks they cannot de-
fend themselves against the way adults can. The DSA’s Article 28(2)
embodies this principle but principles without enforcement mecha-
nisms are merely aspirational. This raises two questions: first, how
to verify that platforms are honouring their obligations and second,
whether the regulatory framework covers the commercial practices
that actually reach children.
Answering these questions presents a fundamental methodologi-
cal challenge. Algorithmic systems are not static objects that can be
inspected once and declared compliant based on a document review
or management attestations [48]. They are dynamic, adaptive, and
opaque, commonly understood as black boxes whose behaviour
can only be assessed empirically. We must study these systems
behaviourally, longitudinally, through systematic simulation and
observation of their outputs that reveal what the algorithm actually
does rather than what the platform claims it does. However, the
research on verifying compliance with provisions like Article 28(2)
is limited or completely absent.
To fill this gap, we conduct analgorithmic auditon TikTok using
sock-puppet accounts simulating pairs of minor and adult users
with the same interest profiles. The observed recommended videos
are then, with the help of Large Vision-Language Models (LVLMs),
automatically categorised as containing:
(1) Formal ads– commercial content promoted through TikTok’s
advertising system, where a creator pays the platform for
distribution, this satisfies Article 3(r)’s narrow definition of
advertisement as content promoted “against remuneration
specifically for promoting that information”;
(2) Disclosed ads– commercial content where remuneration does
not flow to the platform, labelled by creators using TikTok’s
disclosure tools. This includespaid partnership(where a
brand pays a creator to promote products on the creator’s
account) andpromotional content(where a brand promotes
its own products on its own account or where an individual
promotes a brand they own or have a commercial stake in,
without paying the platform or any third party);
(3) Undisclosed ads– same type of content as commercial con-
tent—paid partnerships or brand self-promotion, where cre-
ators have failed to apply disclosure labels despite platform
rules requiring it; and finally,
(4)Non-ads– content with no commercial purpose.
Furthermore, the topic of advertisement is detected and com-
pared with the user’s interest – such a match serves as an input to
measuring the potential personalization and profiling. We assess
whether the recommendation algorithm treats these advertisement
types differently and specifically, whether profiling occurs for com-
mercial content that falls outside the DSA’s narrow definition of
“advertisement”.
We focus on TikTok for the following reasons. First, it is the
platform where the gap between regulatory intent and commercial
reality is most visible: when a user opens TikTok, they land by
default on the “For You Page”, which is a feed driven entirely by
the platform’s recommender system rather than social connections.
Most users spend the majority of their time on this algorithmically
curated feed, meaning that content minors see has been selected
based on their inferred preferences and interests. Second, TikTok
has been the subject of multiple EU enforcement actions under the
Digital Services Act, including proceedings concerning addictive
design and default settings for minors [ 19], making it a critical
test case for whether existing regulation can protect minors from
commercial exploitation [18].

The DSA’s Blind Spot: Algorithmic Audit of Advertising and Minor Profiling on TikTok FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
Our findings reveal a significant enforcement gap. Formal ad-
vertisements are recommended to minors to a limited extent (in
comparison with adults) and show no evidence of profiling, con-
sistent with DSA compliance. However, disclosed, and especially
undisclosed commercial content (which represents a substantial
share of commercial content minors are exposed to), show clear ev-
idence of profiling based on inferred user interests. In other words,
while the minors are exposed to less amount of commercial con-
tent, such content is highly tailored/personalized according to their
profiles. The implication is stark: the DSA protects minors from
one category of commercial content while leaving the dominant
forms of commercial exposure practically unregulated.
Our main contributions are as follows:
• We introduce a novel methodology proceeding from the sock-
puppet algorithmic audits. It can be characterized as apaired
userstudy design (as an analogy topaired adsmethodology
[32]), which provides a unique user-centric insight what
kind of commercial content is recommended to a minor/an
adult under the same conditions (an interest, a time period, a
gender, a location) removing potential confounding factors.
• By applying the proposed methodology to 3 user pairs over
the period of 10 days, we collected and automatically eval-
uated 7095 TikTok videos, of which 1346 were classified as
containing one of studied advertisement types. Based on this
data, we provide the first empirical evidence that profiling-
based targeting of minors continues on TikTok through con-
tent formats not covered by DSA Article 3(r)’s definition of
“advertisement” (including disclosed and undisclosed influ-
encer and branded content).
• We identify a regulatory gap: while the DSA prohibits profiling-
based advertising to minors for formal ads, influencer and
brand promotional content falls outside this definition en-
tirely, leaving the dominant forms of commercial exposure
minors face without any corresponding prohibition on profiling-
based targeting. To address this gap, we propose four specific
policy recommendations.
2 Background and Related Work
2.1 Negative Influence of Social Media
Platforms and Advertisement on Minors
Adolescence is a critical developmental period during which on-
going brain development increases vulnerability to commercial
content and its influence. Regions of the brain governing reward
and salience, the ventral striatum, amygdala, and insula, become hy-
peractive while the prefrontal cortex, which governs cognitive con-
trol and self-regulation, continues to mature into the mid-twenties
[13, 51]. The prefrontal cortex enables deliberate evaluation of in-
coming information, including recognising and resisting persuasive
intent, and its immaturity during adolescence means that cognitive
control is substantially limited at the moment it is most needed.
This matters because the platform environment described above
is one in which commercial and organic content are frequently
indistinguishable, particularly where creator-driven commercial
content carries no disclosure label. Algorithmically-curated feeds,
infinite scrolling, and sentiment-aware recommendation systems
create a continuous, non-predictable stream of content that sustains
engagement through reward patterns theoretically comparable to
partial reinforcement in gambling [36, 44], with no natural stopping
point at which a user can step back and assess what they have been
watching.
Resisting advertising requires recognising persuasive intent and
the capacity to resist it [ 27, 29]. Research shows that while mi-
nors can identify advertising as selling products, they often fail to
recognise its intent to shape attitudes and behaviour, a limitation
that persists through adolescence [40, 51]. Even when recognised,
active resistance requires switching from automatic affective pro-
cessing to deliberate, critical evaluation, a capacity dependent on
still-developing prefrontal function [13]. Because this switching
capacity is substantially limited, adolescents process advertising
through low-elaboration pathways. Rather than engaging in critical
evaluation, they respond to advertising affectively: commercial con-
tent that matches their interests evokes positive feelings, and these
feelings transfer directly to brand attitudes through processes that
bypass deliberate evaluation [45, 60]. Advertising literacy alone is
therefore insufficient, as its application depends on capacities that
are still developing.
Profiling-based targeting exploits this constraint directly. Minors
cannot recognize targeting as a deliberate marketing technique and
therefore they process such advertising in a non-critical manner
[59, 60]. As a result,targeting increases advertisement liking while
evading recognition and foreclosing the first condition of any de-
fence model before adolescents even encounter the content.
Creator-driven commercial content compounds these vulner-
abilities through a mechanism rooted in the same social reward
hyperactivity that characterises adolescent brain development. Ado-
lescents’ heightened sensitivity to peer-related social signals makes
them particularly susceptible to para-social relationships, the illu-
sion of a long-lasting personal bond with a media figure that fosters
trust and reduces critical distance [3, 30]. Influencers function as
quasi-peers whose opinions carry persuasive weight precisely be-
cause of this dynamic [3], and social learning theory indicates that
liking a figure increases the probability of imitating their actions
[12]. Although disclosures can activate recognition of advertising
intent [5], minors with strong para-social relationships do not trans-
late that recognition into critical evaluation — the bond with the
creator outweighs the scepticism that awareness of commercial
intent would otherwise trigger [5]. When content carries no dis-
closure at all, sponsored material mimics the visual aesthetics of
everyday posts and recognition is foreclosed entirely [28, 38]. The
consequences are documented: internal research disclosed by for-
mer Facebook employee Frances Haugen confirmed that platforms
were aware that exposure to appearance-related content worsens
body image and self-esteem among teenage girls, yet algorithmic
amplification of such content continued [61]. It is within this con-
text of structural vulnerability that the adequacy of the current
regulatory framework must be assessed.
2.2 Regulation of Displaying Advertisements to
Minors in the DSA
DSA establishes a tiered framework of obligations for digital ser-
vices operating in the EU [31]. Universal obligations apply to all
intermediary services, while the specific subset of hosting services

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Solarova et al.
– online platforms – face additional requirements covering, among
other things, the protection of minors, recommender systems, and
advertising transparency. Very Large Online Platforms (VLOPs) face
the strictest requirements, including mandatory risk assessments,
mitigation measures, and independent external audits.
The reach of these obligations depends fundamentally on how
the DSA defines “advertisement”. Article 3(r) DSA defines advertise-
ment as “information designed to promote the message of a legal or
natural person, irrespective of whether to achieve commercial or
non-commercial purposes, and presented by an online platform on
its online interface against remuneration specifically for promoting
that information”. This definition is grounded in payment structure
rather than commercial purpose, meaning only content for which a
platform receives remuneration for promotion qualifies as an adver-
tisement under the DSA. Commercial content presented without
such remuneration, including hidden or undisclosed commercial
content, falls outside its scope [31].
This boundary directly determines the scope of minors’ pro-
tection under the DSA. Article 26(1) DSA requires platforms to
ensure that recipients can identify each advertisement as such,
including the entity behind it, who paid for it, the main target-
ing parameters used, and how users can change those parameters.
Article 26(2) DSA extends this by requiring platforms to provide
creators with a functionality to declare when content constitutes
a commercial communication, placing compliance responsibility
on creators rather than platforms. Article 26(3) independently pro-
hibits profiling-based targeting using special categories of personal
data regardless of the recipient’s age. For minors, Article 28(2) DSA
goes further, prohibiting platforms from presenting profiling-based
advertisements to users they are "aware with reasonable certainty"
to be minors, where the European Commission’s Guidelines de-
fine minors as individuals below 18 years [ 20]. Because Articles
26(1) and 28(2) operate within Article 3(r)’s definition, their obliga-
tions do not extend to commercial content for which the platform
receives no remuneration.
The application of Article 28(2) further depends on the GDPR’s
definition of profiling. Some authors argue that where data is vol-
untarily disclosed by the user, its subsequent use falls outside the
scope of profiling and therefore outside Article 28(2) [62]. In our
view, this argumentation is incorrect. Profiling under GDPR Article
4(4) is defined as "any form of automated processing of personal
data consisting of the use of personal data to evaluate certain per-
sonal aspects relating to a natural person, in particular to analyse
or predict aspects concerning that natural person’s performance at
work, economic situation, health, personal preferences, interests,
reliability, behaviour, location or movements" [25]. This definition
emphasises what is done with data rather than how it was acquired.
The European Data Protection Board (EDPB) affirms this position
by treating profiling as a function of automated logic rather than
data origin [1], and its guidance on age-assurance warns controllers
against using data collected for age verification to profile minors
beyond what is strictly necessary [22].
The narrow definition of advertisement by Article 3(r) is par-
tially addressed by other EU instruments. The Unfair Commercial
Practices Directive (UCPD) covers deceptive and manipulative com-
mercial practices against consumers regardless of payment struc-
ture [11], including hidden marketing (UCPD, Annex I, point 11)
and false representations of commercial intent (UCPD, Annex I,
point 22). Article 5(3) UCPD requires that disclosures to be under-
standable to minors as a vulnerable consumer group, while Annex I
point 28 prohibits directly prompting minors to purchase advertised
products [16]. Digital consent by children is further governed by
Article 8 GDPR [ 34], and the Audiovisual Media Services Direc-
tive (AVMSD) imposes protection requirements on video-sharing
platforms [23]. None of these instruments, however, specifically
imposes on platforms a systemic obligation to detect or prevent
the profiling-based delivery of commercial content to minors. The
Article 28(2) prohibition therefore remains the most specific and
enforceable protection available in this domain, yet its reach is con-
fined to the narrow category of content that Article 3(r) recognises
as advertisement.
2.3 Algorithmic Auditing
Algorithmic audits are commonly defined as systematic assess-
ments of the negative impacts that algorithmic systems may have
on the rights and interests of affected stakeholders, together with
identifying of algorithmic features or situations that give rise to
such harms [7]. In the context of social media platforms, AI-driven
recommender systems, including ad delivery algorithms, are largely
opaque and inaccessible to external inspection. Audits assessing
their properties (e.g., potential biases) must therefore rely on be-
havioural analysis. Rather than examining internal model parame-
ters, researchers infer system properties from platform responses
to controlled user interactions, such as content consumption or
engagement, and by analysing the resulting recommendations.
To operationalize such behavioural audits, prior work has pri-
marily employed simulated user interactions through automated
agents (bots) [57] or human participants [43], commonly referred
to as sock-puppeting audits and crowdsourcing (or collaborative)
audits, respectively [46]. These approaches allow researchers to sys-
tematically probe platform behaviour under predefined conditions,
such as specific user interests, interaction patterns, or demographic
profiles. When deployed at sufficient scale and diversity, algorith-
mic audits have proven effective in uncovering issues related to
harmful content amplification (e.g., misinformation [49]), political
bias, or unfair exposure, and they can also serve as an independent
mechanism for validating regulatory compliance, including audit
reports mandated under the DSA for VLOPs and VLOSEs [48].
A typical algorithmic audit follows a structured multi-step pro-
cess. First, an audit question is formulated, which guides the design
of audit scenarios capturing specific user profiles and sequences
of actions intended to simulate realistic user behaviour. These sce-
narios are then executed by bots or human agents, during which
platform responses (such as recommended content or changes in
content exposure) are systematically recorded. Finally, the collected
data are analysed to detect the presence, magnitude, and dynamics
of the audited phenomenon, enabling empirical conclusions about
the platform’s algorithmic behaviour and its potential societal im-
pacts.
The current generation of algorithmic audits is still in early
stages and may suffer from various limitations, such as low repro-
ducibility and short-term validity of results [ 37, 47]; or focus on

The DSA’s Blind Spot: Algorithmic Audit of Advertising and Minor Profiling on TikTok FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
few online platforms, Western contexts, particularly the US, Eng-
lish language data and specific (commonly over-simplified) user
properties [58]. However, due to growing research efforts as well
as new paradigms, such as model-based algorithmic auditing [50],
their overall maturity and robustness is continuously increasing.
2.4 Auditing Policy Compliance and Ad
Delivery Algorithms
To assess platforms’ compliance with the DSA, VLOPs and VLOSEs
are required to undergo annual external audits. These audits aim
to provide an independent assessment of compliance with legal
obligations, particularly regarding risk assessment and mitigation
of systemic risks (DSA Articles 33, 34, and 37). Analysis of pub-
lic audit reports showed that such external audits rely mostly on
conventional audit methodologies, rooted in compliance auditing
traditions developed for financial reporting and IT controls [ 48].
These methodologies were, however, designed for relatively static
systems and therefore face unprecedented challenges when applied
to modern AI-based systems that interact dynamically with human
users.
In parallel, there are complementary independent audits by re-
searchers, non-profit watchdog organizations or algorithmic assess-
ment / ethics-focused companies. These audits commonly apply
various algorithmic auditing methodologies. Panigutti et al . [41]
recently conducted a literature review of audit study designs suit-
able for investigating algorithmic-driven risks in digital services
focusing on DSA provisions addressing algorithmic systems. The
outcome is four main categories of methodologies: risk-uncovering,
reverse engineering, interface design, and risk-measuring; with the
main steps and best practices associated with each approach.
While existing literature proves that various types of algorithm
audits represent a suitable approach how to assess compliance with
policy and regulations, the number of existing studies remain lim-
ited. In regards to black-box audits of ad delivery algorithms, the
existing works (such as [32]) employpaired adsmethodology. In
this methodology, an auditor runs a pair of ads targeting the same
audience and at the same time [32]. The content of ads, however,
intentionally introduces a hypothetical bias (e.g., one ad is hypoth-
esized that will be propagated more to men and second to women).
Algorithmic bias is then measured by looking at relative difference
in delivery along a demographic attribute of interest to the auditor.
Such anad-centricapproach (centred around a specific ad analysing
how it is delivered to users with various demographics) is, however,
not appropriate for assessing the compliance with protection of
minors, which is subject of our study. Instead, we aim for more
user-centricapproach, which will allow us to focus on a user (e.g.,
a minor or an adult) and study what kind of advertisements are
delivered (in terms of type and topic) to such a user. To the best
of our knowledge, there is no such work yet. To make it possible,
the sock-puppeting algorithmic audits represents a potential and
suitable solution, which is adopted also in our work.
3 Preliminary Analysis
As existing works focusing on user-centric algorithmic auditing of
ad delivery systems remain limited or even completely absent as
well as findings from the existing studies on constantly-evolving
TikTok ad delivery system may be already obsolete (also as a result
of DSA adoption), we opted for iterative approach. At first, we
applied qualitative methods to obtain initial insights, namely adoc-
umentary analysisof TikTok’s disclosure framework and amanual
content analysisfrom selected creators. The obtained initial findings
subsequently served us as important inputs to design a quantitative
methodology and experiment utilizing the sock-puppeting algo-
rithmic audit (e.g., to determine topics the simulated users should
express interest in, or to determine the taxonomy of ad types present
on the TikTok platform).
3.1 Documentary Analysis
At first, we analysed TikTok’s publicly available policies on com-
mercial content disclosure using four sources: the Branded Content
Policy [52], the Commercial Content Disclosure guidelines in Tik-
Tok’s Business Help Center [56], the Community Guidelines [53],
and the TikTok’s Commercial Content Library [54].
The Branded Content policy (BCP) [52] defined branded content
as content promoting third-party brand in exchange for payment
or incentive for the creator, such as gifted products, monetary
payment, affiliate commissions and brand partnerships. TikTok
shifts compliance responsibility onto creators, who must ensure
adherence to applicable laws and platform rules.
When creators post branded content, they must enable the ’Dis-
close commercial content’ toggle. The toggle offers two options:
“Your brand” or “Branded content. ” Selecting “Your brand” produces
a “Promotional content” label; selecting “Branded content” produces
a "Paid partnership" label. Once published, these labels cannot be
changed and if there is a mistake creators must delete and repost to
correct errors. Advertisements purchased directly through TikTok
Ads Manager carry a separate “Sponsored” or “Ad” label (depending
on whether it is TikTok app or desktop version) that TikTok injects
automatically [52].
TikTok’s Community Guidelines [53] address commercial disclo-
sure under "Regulated Goods, Services, and Commercial Activities. "
The guidelines state disclosure is required when “marketing for your
own business, product, or service” or when engaging in “promotion
or review of a third-party brand, product, or service in exchange for
money, goods, or any other kind of incentive”. However, the guide-
lines remain broad regarding enforcement mechanisms, referring
users to the Branded Content Policy for specifics.
TikTok hosts a Commercial Content Library [54], introduced in
July 2023 for DSA Article 39 compliance, through which it aggre-
gates ads and creator-disclosed commercial content with at least
one impression. The library contains two sections: the Ad Library
(content TikTok is paid to display) and “Other commercial content”
(content TikTok is not paid to display but which creators have dis-
closed). The “Other commercial content” section depends entirely
on creators using the disclosure toggle – if a creator does not enable
it, the content does not appear regardless of its commercial nature
[54].
The Business Help Center [ 56] claims TikTok flags videos as
commercial content based on financial incentives (URLs, promo
codes, hashtags, collaboration mentions, QR codes, overlay ads),
brand mentions (brand hashtags, @tags, logos), and product recom-
mendations (calls-to-action such as “buy now” or “shop today”), yet

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Solarova et al.
how this operates in practice remains unclear. We identified videos
with multi-thousand impressions where creators mentioned brand
partnerships in descriptions or in the video itself, yet the platform
took no visible action.
3.2 Manual Content Analysis
Second, we identified influencers popular among minors across cat-
egories: fitness, fashion, beauty, gaming, and lifestyle. We focused
on creators known to have brand deals and examined how they label
their content. We manually reviewed 15 influencers and approxi-
mately 50 videos. We found substantial variation both within indi-
vidual accounts and across creators. Follower size did not determine
disclosure practices, meaning larger influencers with hundreds of
thousands of followers sometimes used only hashtags (ad, Wer-
bung) or promo codes in descriptions without enabling the toggle.
Thus, these videos do not appear in TikTok’s Commercial Content
Library and lack the grey disclosure label (Paid Partnership) at the
bottom of the video.
We also found creators promoting third-party products who en-
abled the toggle but selected the wrong category, labelling content
as “Promotional content” (dedicated to be used by brands or users
to indicate their own commercial content) instead of “Paid part-
nership” (dedicated to creators to indicate third party commercial
content). It seems that TikTok is not taking any actions to cor-
rect these labels over time. Furthermore, we identified variation
between TikTok’s app and desktop interfaces. Content labelled as
"Ad" in-app appeared sometimes as "Sponsored" on desktop and
vice-versa.
4 Algorithmic Audit of TikTok Advertisement
System
4.1 Methodology and Experimental Setup
To empirically assess TikTok’s compliance with Article 28(2) of the
DSA, we conducted an algorithmic audit using a sock-puppet ap-
proach1. This methodology allowed us to control for user variables,
specifically age and interest, while eliminate undesired confound-
ing factors (such as random variations in gender, location, activity
time). As a result, we were able to systematically observe the plat-
form’s ad delivery and recommendation behaviour in a naturalistic
setting.
4.1.1 Experimental Design and Agent Configuration.We employed
apaired user study designto isolate the effect of age on ad delivery.
We created paired automated agents (sock-puppets), each consisting
of aminoragent (aged 16–17) and anadultagent (aged 20–21). We
avoided the borderline age of 18 (legal majority in all EU Member
States except Scotland) to ensure a clear distinction in platform
signals. The small age gap was chosen to minimise confounding
from generational content preferences, ensuring that differences in
recommendations reflect legal status rather than cohort effects.
1To allow replicability of results presented in this study, the anonymised collected
data, altogether with their predicted annotations, are available for research purposes
only at Zenodo upon request: https://doi.org/10.5281/zenodo.18879043; the code used
for data analysis is publicly available as a Github repository: https://github.com/kinit-
sk/ai-auditology-advertising-and-minor-profiling-tiktok.
The gender (femaleormale) was assigned to each pair randomly,
being the same for minor and adult user (to prevent introducing
another undesired confounding factor).
Out of total 4 pairs of agents, each pair was assigned a specific
interest profile corresponding to high-engagement topics among
adolescents:beauty,fitness,gamingandpolitics. These topics are
selected from the main topical groups provided by the TikTok
platform in the Explore feature – out of them, we selected such
topics, where the sufficient amount of commercial communication
appears.
All agents were configured to access the platform via thedesktop
web interface(Google Chrome). To ensure the application of the
DSA’s jurisdiction, all traffic was routed through static residential
proxies located inGermany, establishing a consistent geo-location
signal for the platform’s compliance mechanisms. Age was sig-
naled to the platform exclusively through the date of birth provided
during account registration, without additional behavioural age
verification signals. The audit took place during December 2025.
4.1.2 Interest Seeding Phase.To overcome the “cold start” problem
inherent in fresh accounts, we implemented a rigorous one-day
seeding phase prior to the main data collection phase. Agents began
as “blank slates” and were trained to acquire their target interest
profiles through active engagement.
For each interest profile, we defined a set of domain-specific
search queries (e.g., makeup, skincare, or cosmetics for the beauty
topic). The agents executed these queries and selected videos from
the search results to interact with based on a semantic relevance
check. To decide how a user should interact with each of the re-
turned videos, we utilized auser interaction predictor. This compo-
nent employs a Large Language Model (LLM), specificallyGPT-4.1,
to analyze the video metadata (e.g., title and description) and deter-
mine whether the topic of the video matches the topic from the user
interest profile. The utilized LLM prompt is available in Appendix A.
This classification model was reused from our previous work [42],
where we thoroughly evaluated it. It achieves accuracy of 95-98%
(depending on a specific topic), being sufficient for the auditing
purposes.
In user-video topic matches, the agent signalled “strong inter-
est” by watching the video until the end, “liking” it, and saving
it to bookmarks. This training loop ran until the agent had either
watched 25 relevant videos or evaluated 51 candidates, ensuring a
consistent baseline of interest history across all agents.
4.1.3 Data Collection Phase.Following the seeding phase, we con-
ducted the main data collection over a 10-day longitudinal period
in December 2025. Each bot interacted with the TikTok for 1 hour
in one session each day, while each adult-minor pair was running
in parallel. The duration of 1 hour corresponds to an average time
spent by TikTok users on the platform per day. By running bots con-
temporaneously, we secured that there are no time-of-day-specific
effects that may cause potential undesired biases.
Unlike passive observation studies, our agents maintained their
interest profiles through conditional interaction, simulating a user
who selectively engages with relevant content while ignoring irrel-
evant recommendations.
For every video presented in the “For You” feed, the system
performed a real-time relevance assessment using the sameuser

The DSA’s Blind Spot: Algorithmic Audit of Advertising and Minor Profiling on TikTok FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
interaction predictorbased on the video’s textual metadata. If the
video matched the agent’s assigned interest, the agent executed the
engagement routine (watch, like, and bookmark). If the content was
unrelated, the agent immediately skipped the video. Crucially, we
captured comprehensive metadata—including descriptions, hash-
tags, and visual frames—forallvideos appearing in the feed, re-
gardless of whether they were watched or skipped. This ensured
we captured the platform’s unfiltered recommendation stream and
ad delivery logic rather than just the user’s interaction history.
4.1.4 Ad Detection and Classification Pipeline.A core challenge of
this audit was identifying not only formal advertisements but also
disclosed and undisclosed advertisements. To address this, we de-
veloped a multi-modal classification pipeline utilizing a quantized
Large Vision-Language Model (LVLM), specificallyQwen3-VL-4B-
Instruct. The specific prompt used for annotation purposes is avail-
able in Appendix A. The ad detection and classification pipeline
was applied on collected data in the post-audit phase, i.e., the anal-
ysis does not need to be done in real-time (in contrast to the user
interaction predictor) and thus a deeper content analysis with a
larger model was possible.
For each video, the model analysed three key frames (beginning,
middle, and end) to detect the advertisement presence and eventu-
ally, classify it into three mutually exclusive ad types based on a
strict decision hierarchy:
(1) Formal Ads– content where the platform injects a formal
overlay label (specifically “Sponsored” or “Ad”) at the bottom
of the video frame.
(2) Disclosed Ads– content where the creator has utilized the
platform’s disclosure tools, resulting in a “Paid partnership”
or “Promotional content” grey overlay label.
(3) Undisclosed Ads– content lacking any platform-generated
disclosure labels but containing strong semantic or visual
indicators of commercial intent identified by the model (e.g.,
verbal product endorsements, visible discount codes, or hash-
tags).
The model also classified ad topic into one of the following
options:beauty,fitness,gaming,politicsorother.
This visual-first approach allowed us to detect regulatory compli-
ance failures that text-only analysis would miss, particularly where
overlay labels are rendered in the UI but missing from the textual
metadata.
4.1.5 Manual Validation of Ad Detection and Classification Pipeline.
To ensure validity, a subset of the automatically annotated videos
was manually annotated by the research team to verify the accuracy
of the detection logic. For this purpose, to achieve a representative
set of data, we applied the stratified sampling strategy on the top of
the collected and annotated data. More specifically, for each out of
8 users, we randomly selected 5 videos containing formal, disclosed,
undisclosed, and none ads (if there was less than 5 videos in any of
these categories, all videos have been selected).
Utilizing the custom developed tool (see Appendix C), two au-
thors of this study independently manually examined the selected
videos and provided human-based ad type and topic annotations.
They have been subsequently compared with automatic annota-
tions. Specifically forpoliticstopic, we observed that both users
(a minor as well as an adult) got enclosed during the main audit
phase in very specific topical filter bubbles (a significant potion of
videos contained AI-generated satire, or videos tackling currently
ongoing Pakistani political issues). The classification model did not
perform well on this type of content in certain cases, and the videos
were also difficult to annotate for human annotators. Therefore, we
decided to removepoliticstopic from further analysis.
For the remaining topics, out of 113 manually annotated videos,
the automatic annotated ad type was correct in 102 (90.3%) and 100
(88.5%) of samples respectively (according to individual annotators).
Out of 78/74 videos containing any type of advertisement, the ad
topic was correctly annotated in 74 (94.9%) and 63 (85.1%). The inter-
annotator agreement achieved high rates – 94.7% for ad type and
89.2% for ad topic. A lower agreement for ad topic was caused by
videos containing fashion ads, which can be considered as closely
relevant and sometimes overlapping with the beauty topic and
annotators approached it in some cases differently.
Deeper insight into misclassified samples revealed that the errors
occurred approximately equally between each pair of predicted-
true labels (see also Figure 3), therefore, no systematic bias has been
introduced. Considering the challenging nature of these annotation
tasks (especially detection of undisclosed commercial content), we
consider the achieved accuracy as sufficient for the purpose of this
audit study.
4.2 Results
4.2.1 Metrics and Statistical Analysis Description.For the purpose
of this study, we consider the advertisement to bepersonalized
to the user interest profile, if its topic matches a topic present
in the used interest profile. Subsequently, apersonalization rate–
calculated as a proportion of personalized ads out of total ads –
represents a proportion of ads presented to a user that matches
their interest profile. However, some number of advertisements
may naturally occur in the user feed regardless of their interest
profile and such a number can vary accordingly to the popularity
and overall prevalence of such advertisements in the platform. To
consider this potential bias, we measure explicitly aprofiling effect.
Profiling effect is a percentage point (pp) difference ( Δ) between
a personalization rate (i.e., a ratio between ads relevant for a user
and all ads seen by the user) and a baseline rate (a proportion of
ads with the same topic that naturally appeared for users with the
same age but different interest profiles).
To evaluate statistical significance of profiling effect (i.e., whether
a difference between personalization and baseline rate is statistically
significant), we measure the p-value of proportions z-test.
4.2.2 Dataset Description.The outcome of our paired user audit
study are data collected by six sock-puppet accounts (differentiated
by an age group and an interest) and automatically annotated into
four mutually exclusive video categories: formal ads, disclosed ads,
undisclosed ads and non-ads and four ad topics: beauty, fitness,
gaming, other. Overview of individual accounts, their character-
istics and total number of videos and ads are presented in Table
1. In total, during the 10 days of main data collection phase, the
users encountered 7095 videos. Out of them, 1346 (18.97%) were
classified to contain one type of advertisement we are interested

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Solarova et al.
Table 1: Overview of user characteristics and total number of
observed videos and ads (formal + disclosed + undisclosed)
User Gender Age Total videos Total ads Avg video length
BeautyMinor Female 16 651 169 (25.96%) 55 seconds
BeautyAdult Female 21 1088 246 (22.61%) 36 seconds
FitnessMinor Male 17 876 45 (5.14%) 36 seconds
FitnessAdult Male 20 2341 534 (22.81%) 14 seconds
GamingMinor Female 16 868 51 (5.88%) 30 seconds
GamingAdult Female 21 1271 301 (23.68%) 30 seconds
Total 7095 1346 (18.97%)
Figure 1: Ad distribution by ad type and ad topic match per
user. While minors are recommended less ads in total, such
ads are not properly disclosed and are heavily personalized
to match their interest.
in. Adults watched more videos primarily because the content rec-
ommended to them was significantly shorter (by 10 seconds) on
average than the content served to minors. Summary of all collected
and annotated data are available in Appendix B, Table 4.
Summary of all collected and annotated data are available in
Appendix B, Table 4.
Such data allowed us to perform a unique investigation across
three dimensions: 1) How advertisement types are distributed for
adults vs. minors and across different user interest profiles (Figure
1); 2) How advertisement topics are distributed for adults vs. mi-
nors (Figure 2); and finally 3) An extent to which advertisement are
personalized to user interest profiles (Table 2 and Table 3). As we
observed only a limited number of disclosed ads, for the purpose
of some analysis we group them together with undisclosed ads (as
from the perspective of DSA, they are treated equally – both fall out-
side Article 28(2)’s scope and represent creator-driven commercial
content differing only in labelling tag).
4.2.3 Overall Advertising.As Table 1 clearly shows, advertising
exposure (regardless of its specific type) varies substantially by
interest category and age group. Minors with fitness and gam-
ing interests are less exposed to advertisements (comprising 4.35%
and 5.18% of their feeds respectively). Nevertheless, a minor inter-
ested in beauty was exposed to a significantly larger amount of
ads (23.12%), even surpassing the paired adult user (20.08%). This
finding can be attributed to a high prevalence of beauty-oriented
commercial content on TikTok platform, that is created especially
by a considerable number influencers.
A deeper insight into distribution of advertisement types and
their match with user profiles (Figure 1) further shows that de-
spite minors are exposed to less ads (in absolute as well as relative
numbers), such ads comprises particularly undisclosed content that
matches their interest.
In the following analysis, we provide a more detailed breakdown
of results by each type of advertisement.
4.2.4 Formal Advertising.Regarding formal ads, the category ex-
plicitly covered by DSA, we observed patterns consistent with the
regulation’s intent. Adult accounts received substantially more for-
mal advertising than minors (e.g., 301 formal ads for Fitness Adult
compared to 0 for FitnessMinor; 207 for GamingAdult compared to 7
for GamingMinor). An exception is a beauty topic, where both an
adult and a minor received only a relatively low number of formal
ads (6 and 21 respectively).
From ad topic distribution (Figure 2, sub-charts (a) and (b)), the
proportion of ads matching user interest (i.e., a diagonal dominance)
goes up to 21.2% for adults vs. 14.3% for minors. Most advertisement
presented to minors (and partially also for adults) was classified as
“other” topic, indicating low personalization of formal ads.
Adult formal ads also exhibited a higher profiling toward user
interests as it is in case of minors (Table 2). The profiling effect
ranges between 10.39 pp to 16.43 pp (being statistically significant
for fitness and gaming topics), e.g., FitnessAdult achieved a +10.39pp
profiling effect (19.17% personalization rate compared to 8.88%
baseline rate, p<0.01). Minor accounts, by contrast, showed no
consistent interest-based profiling: BeautyMinor exhibited a negative
effect (Δ = -23.81 pp), Fitness Minor received zero formal ads, and
while GamingMinor showed 3 of 8 ads to be interest-matched, the
small numbers precludes reliable inference.
These results indicate that TikTok’s formal advertising system
operates in compliance with DSA Article 28(2).
4.2.5 Disclosed Advertising.Disclosed ads which is understood as
content labelled by brands and creators as promotional content or
paid partnership, constituted a negligible share of detected adver-
tising across all accounts (both for minors and adults) (Figure 1).
Among minors, we observed only 8 disclosed ads for beauty, 1 for
fitness, and 5 for gaming (Table 4). This scarcity does not reflect an
absence of brand/influencer marketing, it rather reveals a labelling
deficit. The disclosure rate (disclosed ads as a proportion of all
creator-driven commercial content) was 5.4% for BeautyMinor (8 out
of 148), 2.2% for FitnessMinor (1 out 45) and 11.4% for GamingMinor (5
out of 44). Adult accounts showed similarly low rates. This observa-
tion aligns with previous work [2] providing quantitative evidence
that formal disclosure tools for commercial content are rarely used
by creators.
Even within this small advertisement type category, personaliza-
tion was evident: 7 out of 8 disclosed ads for BeautyMinor concerned
beauty topics and all 5 disclosed ads for GamingMinor were gaming-
related.
4.2.6 Undisclosed Advertising.Undisclosed advertising is type of
ads that are clearly commercial content but lack creator disclosure
and the corresponding label. These undisclosed ads constituted
the largest advertising category (constituting 55.8% of all ads) and
exhibited personalization intensities far exceeding those observed

The DSA’s Blind Spot: Algorithmic Audit of Advertising and Minor Profiling on TikTok FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
(a) Formal Ads, Adults
 (b) Formal Ads, Minor
 (c) Disclosed + Undisclosed Ads, Adults
 (d) Disclosed + Undisclosed Ads, Minor
Figure 2: Ad topic distribution. While formal ads distribution indicate no significant personalization, disclosed and undisclosed
ads show strong diagonal dominance.
in formal advertising. The high-prevalence of undisclosed adver-
tisement is in line with the previous work [14], which reported an
undisclosed share of commercial communication on Twitter even
up to 96%. BeautyMinor received 140 undisclosed ads, of which 129
(92.1%) matched their interest profile; FitnessMinor received 44, with
39 (88.6%) fitness-related, GamingMinor received 39, with 36 (92.3%)
gaming-related (Table 4).
For ad topic distribution, we report diagonal dominance for
disclosed and undisclosed ads combined (Figure 2, sub-charts (c)
and (d)). For minors, diagonal dominance was 91.6% (217 of 237 ads)
– to compare, a diagonal dominance for formal ads was only 14.3%.
Table 2: Profiling effect forformalads.Personalization rate
is a ratio between ads relevant for a user and all ads.Baseline
rateis determined by proportion of ads with the same topic
that naturally appeared for users with the same age but a
different interest.Profiling effectis a percentage point (pp)
difference between these two numbers.
User Pers. Rate Pers./Total Ads Baseline Rate Pers./Total Ads Profiling Effect Stat. Diff.
BeautyMinor 4.76% (1/21) 28.57% (2/7) -23.81 pp
BeautyAdult 33.33% (2/6) 16.90% (86/509) 16.43 pp
FitnessMinor 0.00% (0/0) 3.57% (1/28) -3.57 pp
FitnessAdult 19.27% (58/301) 8.88% (19/214) 10.39 pp **
GamingMinor 42.86% (3/7) 9.52% (2/21) 33.34 pp *
GamingAdult 23.56% (49/208) 9.12% (28/307) 14.44 pp ***
*** for p < 0.001 (highly significant), ** for p < 0.01 (very significant), * for p < 0.05
(significant)
Table 3: Profiling effect fordisclosedandundisclosedads.
User Pers. Rate Pers./Total Ads Baseline Rate Pers./Total Ads Profiling Effect Stat. Diff.
BeautyMinor 91.89% (136/148) 5.62% (5/89) 86.27 pp ***
BeautyAdult 64.17% (154/240) 3.68% (12/326) 60.49 pp ***
FitnessMinor 88.89% (40/45) 5.21% (10/192) 83.68 pp ***
FitnessAdult 91.85% (214/233) 24.62% (82/333) 67.23 pp ***
GamingMinor 93.18% (41/44) 0.00% (0/193) 93.18 pp ***
GamingAdult 88.17% (82/93) 0.85% (4/473) 87.32 pp ***
*** for p < 0.001 (highly significant), ** for p < 0.01 (very significant), * for p < 0.05
(significant)
Figure 2 visualizes this contrast by highlighting that disclosed and
undisclosed ads cluster tightly on the diagonal for both minor and
adults, whereas minor formal ads disperse across the “other” topical
category.
Analysing undisclosed ads separately yields 91.5% (204 of 223);
within disclosed ads alone, interest-matching was similarly con-
centrated (e.g., 7 of 8 for BeautyMinor, though the small sample size
limits interpretation). This confirms that combining disclosed and
undisclosed ads does not obscure category-specific patterns.
For disclosed and undisclosed ads, profiling effects for minors
ranged from +83.68 pp to +93.18 pp (See Table 3). Beauty Minor
showed 91.89% personalization rate versus a 5.62% baseline rate
(Δ = +86.27 pp, p<0.001); FitnessMinor showed 88.99% versus 5.21%
baseline (Δ = +83.68 pp, p<0.001) and GamingMinor showed 93.18%
versus 0.00% (Δ= + 93.18 pp, p<0.001).
The results show that minors received stronger interest-based
targeting through disclosed and undisclosed ads (+83.68 pp to +93.18
pp) than adults received through formal ads (+10.39 pp to +16.43
pp, Table 2). These profiling effects are 5-8 times larger than adult
formal advertising profiling effects that DSA Article 28(2) permits.
5 Discussion and Policy Recommendations
Our results show two central findings. First, the majority of advertis-
ing falls into the undisclosed category, suggesting that creators and
brands are not using the available labelling tools. However, even
in this case, TikTok officially complies with Article 26(2) of DSA
because it in fact provides the functionality for creators to declare
commercial content, but the platform’s obligation ends there. When
creators fail to label such content through the provided tools, the
platform bears no direct obligation to intervene – neither detects
the omission nor corrects it. Second, it is precisely these undisclosed
ads that exhibit the strongest profiling toward user interests. TikTok
demonstrates formal compliance with Article 28(2) by shielding
minors from profiled formal ads, but minors still remain exposed
to highly profiling-based advertising that the regulation does not
recognize as such.
The pattern across categories reinforces this finding. Formal ads
do not show evidence of profiling toward minors, which is consis-
tent with the requirements of the DSA. We observed a slight in-
crease in profiling toward minors with disclosed ads, where creators
and brands used corresponding labelling tools. The vast majority

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Solarova et al.
falls into the undisclosed category. Minors with specific interest
profiles received a significantly higher number of undisclosed ads
aligned with those interests at higher rates (ranging from +83.68 to
+93.18 percentage points) than other minors with different interests.
The finding related to the beauty topic deserves particular attention
beyond its statistical significance. The literature consistently links
targeted exposure to appearance-related commercial content with
negative body image and diminished self-esteem among adolescent
girls [4, 10]. Therefore, a 16-year-old girl algorithmically fed undis-
closed beauty advertisements at a 92.1 percent personalization rate
represents a documented harm pathway.
The gap appears to be structural. Article 3(r)’s narrow defini-
tion of advertisement excludes influencer marketing and brand
self-promotion from Article 28(2)’s scope. This framing is notably
narrower than Directive 2006/114/EC, which defines advertising as
“the making of a representation in any form in connection with a
trade, business, craft or profession in order to promote the supply of
goods or services”. This definition is based on commercial purpose
rather than payment structure [ 24]. It is also narrower than the
E-Commerce Directive’s (Directive 2000/31/EC) definition of com-
mercial communication, which covers any form of communication
for promotion with aim of commercial gain. TikTok thus demon-
strates formal compliance while the vast majority of advertising
and its subsequent profiling reaches minors and operates outside
the prohibition’s reach.
Based on our findings, we propose the following four recommen-
dations.
(1) First, we advocate for expansion of the definition of adver-
tisement in EU law to encompass advertising by commercial
purpose rather than payment structure, which would as a re-
sult include influencer and brand promotional content in line
with the spirit of definitions of advertising and commercial
communications across EU legislation.
(2) Second, labelling obligations should be strengthened so that
platforms bear direct responsibility for detecting and correct-
ing missing labels on commercial content, not merely pro-
viding functionality for creators and brands to self-label. Our
classification model achieved accuracy as high as 88.5/90.3%
using only publicly observable features, suggesting that plat-
forms’ internal models should perform even better. Although
VLOPs should detect these issues through risk-assessment
obligations, fulfilment relies on thorough auditing and en-
forcement – and this issue has not yet been tackled [ 15].
Alongside platform responsibility, creators should be subject
to a graduated accountability mechanism: where a platform
detects unlabelled commercial content, it should flag it, apply
the appropriate label, and warn the creator, with repeated
failures triggering content removal.
(3) Third, any legislative instrument expanding the definition
of advertisement to encompass influencer and brand promo-
tional content must include a corresponding prohibition on
profiling-based targeting of minors, ensuring that the protec-
tions currently limited to formal advertisements extend to
all commercial content regardless of its channel of delivery.
(4) Finally, compliance with these obligations must be indepen-
dently verified. In our prior work [ 48], we demonstrated
that conventional additional audit methodologies are inade-
quate for assessing dynamic algorithmic systems. Annual,
independent DSA audits should incorporate algorithmic au-
dit mechanism, such as the methodology employed here, to
verify whether ads, under this expanded definition, reach
minors through profiling.
There are positive aspect to minors being in the digital environ-
ment but they should be able to be present there without being
exploited, manipulated or exposed to harmful effects against which
they cannot defend themselves the same way adults do. Our find-
ings demonstrate that current definitional boundaries render this
vision largely symbolic. The legal precedent exists, the enforcement
methodology exists, too. What remains is the regulatory and policy
decision to align them.
This study has some inevitable limitations. Conducting the sock-
puppet algorithmic auditing studies is a challenging task. Deploying
sock-puppet agents in a real-world social media environment is
technologically challenging (e.g., to prevent a platform from ban-
ning sock-puppet accounts, to realistically simulate user’s location,
browser or interactions) as well as demanding on costs (e.g., run-
ning GPU-powered machines capable analysing videos in real time)
and on human oversight (during the audit, the agents were under
continuous monitoring). This limits the possible scope of such stud-
ies (in our case, it was 4 topics, 1 location, 10 days of the main
data collection phase). Furthermore, the simulated user profiles
expressed a single interest topic, whereas real adolescents typically
exhibit multiple overlapping interests, meaning the observed pro-
filing effects may not fully capture the complexity of real-world
algorithmic behaviour. Future studies should also consider using
longer-established accounts, as platforms calibrate recommenda-
tions over time and fresh accounts may not fully reflect how the
system operates for users with a longer interaction history.
The utilized automatic labelling is also naturally imperfect and
assigning ad type/topic labels for some samples may be subjective.
However, the accuracy and inter-annotator agreement showed that
the data quality is high enough taking the purpose of the study into
consideration. Also, the observed differences between minor and
adult behaviour are so significant, that they cannot be explained by
potential false positives introduced by automatic labelling. There-
fore, we consider the collected and annotated data to be sufficiently
representative and the findings derived from them to be generaliz-
able also to additional topics or locations.
6 Conclusions
Minors are spending increasing amounts of time on social media,
which raises well-documented concerns about their development
and mental health. Meanwhile, social media platforms have evolved
into environments which are heavily shaped by commercial content.
To protect minors, who are especially vulnerable to persuasive, per-
sonalized marketing communication, the EU’s legislation – Digital
Service Act (DSA) – bans profiling of minors for advertising pur-
poses. However, verifying compliance is challenging and requires
behavioural approach. Despite a growing body of algorithmic au-
dits, compliance of social media platforms with minor-protection
obligations in ad delivery systems remained unexamined.

The DSA’s Blind Spot: Algorithmic Audit of Advertising and Minor Profiling on TikTok FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
To fill this gap, we conducted an algorithmic audit of all major
types of advertising types on TikTok to examine whether minors
are subject to profiling-based delivery of ads despite the DSA’s ban.
Through algorithmic auditing we deployed sock-puppet agents sim-
ulating adult-minor pairs, with matching interest profiles. Collected
content was automatically classified into four video categories: for-
mal ads, disclosed ads (labelled paid partnership or promotional
content), undisclosed ads (unlabelled paid partnership/promotional
content) and non-ads (classic content); as well as their topics.
The results are concerning. On one hand, formal ads are shown
less frequently to minors than to adults and show no evidence
of profiling toward minors. This indicates TikTok’s formal com-
pliance with DSA Article 28(2). On the other hand, disclosed and
undisclosed ads, which comprise a majority of commercial content
delivered to minors, show very strong personalization rates and pro-
filing effects. These findings reveal a crucial blind spot: the DSA’s
narrow definition of advertisement, grounded in payment struc-
ture rather than commercial purpose, leaves the dominant forms of
commercial exposure minors face practically unregulated. To this
end, we provide four policy recommendations to close this gap, and
call for their urgent consideration given the scale of commercial
exposure minors experience without adequate protection.
In our future work, we plan to cover additional DSA obligations,
replicate the audit over time, and expand to additional countries
and platforms.
Ethical Considerations Statement
The research presented in this paper was done as a part of the
research project, which obtained approval from the organisational
Ethics Committee (decision as of December 17, 2024). To minimise
any potential legal and ethical issues, we directly involve legal
and ethics experts as part of this project. Researchers and research
engineers conducting this auditing study also participated in four
ethics assessment workshops together with ethics and legal experts,
where relevant ethical and legal challenges have been identified
and appropriate mitigations proposed.
The execution of sockpuppeting audits requires creating auto-
mated bots and using them for data collection, which is a potential
violation of the terms of service of the social media platforms. How-
ever, this breach of ToS is permitted by Article 40 (12) of the EU Act
on Digital Services (DSA) if the research concerns systemic risks.
This work directly addresses such a systemic risk by the assessment
of social media platforms compliance with obligations imposed by
legislation, specifically prohibiting profiling-based advertising to
minors stated by the Article 28(2) of DSA, as foreseen by Recital
83 of the DSA. Second, the interaction of the bots with the content
on the platform may impact the platform and society (e.g., increas-
ing the view or like count). However, we minimise the number of
bots that we run. When it comes to data, we collect only publicly
available metadata.
To mitigate potential biases and inaccuracies inherent in the
Large Vision-Language Model (LVLM) used for advertisement clas-
sification, we implemented a multi-layered validation process. This
included both ad-hoc and systematic manual audits of dataset sub-
sets. Data failing to meet accuracy benchmarks were excluded, and
we have reported the estimated error rates accordingly. To prioritize
ethical standards and researcher well-being, all manual annotations
were conducted solely by the study’s authors, following expert
ethical guidelines.
Generative AI Usage Statement
Generative AI has not been used to generate any text for this pub-
lication. LLMs were used solely for the purpose of grammar and
stylistic improvements.
Acknowledgments
This work was partially funded by the EU NextGenerationEU through
the Recovery and Resilience Plan for Slovakia under the project
AI-Auditology, No. 09I03-03-V03-00020.
References
[1] Article 29 Data Protection Working Party. 2018. Guidelines on Automated
Individual Decision-Making and Profiling for the Purposes of Regulation (EU)
2016/679 (WP251rev.01). https://ec.europa.eu/newsroom/article29/items/612053/
en Adopted 22 August 2018.
[2] Valentine Auer, Julia Krickl, Irem Hölzl, and Louise Beltzung. 2025.
#KEINEWERBUNG? Schleichwerbung auf TikTok. Technical Report. Öster-
reichisches Institut für angewandte Telekommunikation (ÖIAT), Vienna.
https://wien.arbeiterkammer.at/beratung/konsumentenschutz/achtungfalle/
Schleichwerbung_auf_Tiktok_202505.pdf Commissioned by AK Wien (Vienna
Chamber of Labour).
[3] Rachel Berryman and Misha Kavka. 2017. ‘I guess a lot of people see me as a big
sister or a friend’: The role of intimacy in the celebrification of beauty vloggers.
Journal of gender studies26, 3 (2017), 307–320.
[4] Madison R. Blackburn and Rachel C. Hogg. 2024. #ForYou? The Impact of Pro-Ana
TikTok Content on Body Image Dissatisfaction and Internalisation of Societal
Beauty Standards.PLOS ONE19, 8 (2024), e0307597. doi:10.1371/journal.pone.
0307597
[5] Sophie C Boerman and Eva A Van Reijmersdal. 2020. Disclosing influencer mar-
keting on YouTube to children: The moderating role of para-social relationship.
Frontiers in psychology10 (2020), 3042.
[6] Emma Jane Boyland and Rosa Whalen. 2015. Food advertising to children and
its effects on diet: review of recent prevalence and impact data.Pediatric diabetes
16, 5 (2015), 331–337.
[7] Shea Brown, Jovana Davidovic, and Ali Hasan. 2021. The algorithm audit: Scoring
the algorithms that score us.Big Data & Society8, 1 (2021), 2053951720983865.
arXiv:https://doi.org/10.1177/2053951720983865 doi:10.1177/2053951720983865
[8] Business of Apps. 2024. TikTok Revenue and Usage Statistics. https://www.
businessofapps.com/data/tik-tok-statistics/.
[9] Georgina Cairns, Kathryn Angus, Gerard Hastings, and Martin Caraher. 2013.
Systematic reviews of the evidence on the nature, extent and effects of food
marketing to children. A retrospective summary.Appetite62 (2013), 209–215.
[10] Sophia Choukas-Bradley, Savannah R. Roberts, Anne J. Maheux, and Jacqueline
Nesi. 2022. The Perfect Storm: A Developmental–Sociocultural Framework
for the Role of Social Media in Adolescent Girls’ Body Image Concerns and
Mental Health.Clinical Child and Family Psychology Review25, 4 (2022), 681–701.
doi:10.1007/s10567-022-00404-5
[11] Laura Clausen and Christine Riefa. 2019. Towards Fairness in Digital Influ-
encers’ Marketing Practices.Journal of European Consumer and Market Law
8, 2 (2019), 64–74. https://kluwerlawonline.com/journalarticle/Journal+of+
European+Consumer+and+Market+Law/8.2/EuCML2019012
[12] Anna Elizabeth Coates, Charlotte Alice Hardman, Jason Christian Grovenor
Halford, Paul Christiansen, and Emma Jane Boyland. 2019. The effect of influencer
marketing of food and a “protective” advertising disclosure on children’s food
intake.Pediatric obesity14, 10 (2019), e12540.
[13] Eveline A Crone and Elly A Konijn. 2018. Media use and brain development
during adolescence.Nature communications9, 1 (2018), 588.
[14] Daniel Ershov, Yanting He, and Stephan Seiler. 2025. Frontiers: How Much
Influencer Marketing Is Undisclosed? Evidence from Twitter.Marketing Science
44, 3 (2025), 505–515. arXiv:https://doi.org/10.1287/mksc.2024.0838 doi:10.1287/
mksc.2024.0838
[15] European Board for Digital Services and European Commission. 2025.
First report of the European Board for Digital Services in coopera-
tion with the Commission pursuant to Article 35(2) DSA on the most
prominent and recurrent systemic risks as well as mitigation mea-
sures. https://digital-strategy.ec.europa.eu/en/news/press-statement-european-

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Solarova et al.
board-digital-services-following-its-16th-meeting. Report pursuant to Arti-
cle 35(2) of the Digital Services Act, published 18 November 2025. Accessed
05-01-2026.
[16] European Commission. 2021. Commission Notice — Guidance on the interpre-
tation and application of Directive 2005/29/EC concerning unfair commercial
practices in the internal market. Official Journal of the European Union, C 526,
29 December 2021, pp. 1–129. https://eur-lex.europa.eu/legal-content/EN/TXT/
?uri=CELEX:52021XC1229(05) CELEX:52021XC1229(05).
[17] European Commission. 2024. Investigation of influencer marketing practices:
Results of the EU-wide sweep. https://commission.europa.eu/live-work-travel-
eu/consumer-rights-and-complaints/influencer-legal-hub_en.
[18] European Commission. 2025.Better Internet for Kids: Review of the Year 2024. Tech-
nical Report. European Commission, DG CONNECT. https://better-internet-for-
kids.europa.eu/sites/default/files/2025-02/BIK_Report2024_WEB.pdf Published
under the Better Internet for Kids+ (BIK+) strategy.
[19] European Commission. 2025. Commission accepts TikTok’s commit-
ments on advertising transparency under the Digital Services Act.
https://digital-strategy.ec.europa.eu/en/news/commission-accepts-tiktoks-
commitments-advertising-transparency-under-digital-services-act. Press
release, European Commission. Accessed 05-01-2026.
[20] European Commission. 2025. Commission publishes draft guidelines on protec-
tion of minors online under Digital Services Act. European Commission News
Release. https://digital-strategy.ec.europa.eu/en/news/commission-publishes-
draft-guidelines-protection-minors-online-under-digital-services-act Accessed
27 May 2025.
[21] European Commission. 2025. Flash Eurobarometer: Social Media Survey 2025.
https://europa.eu/eurobarometer/surveys/detail/3592.
[22] European Data Protection Board (EDPB). 2025. Statement 1/2025 on Age As-
surance. https://www.edpb.europa.eu/system/files/2025-04/edpb_statement_
20250211ageassurance_v1-2_en.pdf Adopted 11 February 2025.
[23] European Parliament. 2025. Report on the protection of minors online. https:
//www.europarl.europa.eu/doceo/document/A-10-2025-0213_EN.html Commit-
tee on the Internal Market and Consumer Protection, Rapporteur: Christel
Schaldemose, 2025/2060(INI), A10-0213/2025. Adopted in plenary 26 Novem-
ber 2025 by 483 votes in favour, 92 against, 86 abstentions.
[24] European Parliament and Council of the European Union. 2006. Directive
2006/114/EC of the European Parliament and of the Council of 12 December
2006 concerning misleading and comparative advertising (codified version) (Text
with EEA relevance). https://eur-lex.europa.eu/eli/dir/2006/114/oj OJ L 376,
27.12.2006, pp. 21–32; CELEX: 32006L0114.
[25] European Parliament and Council of the European Union. 2016. Regulation (EU)
2016/679 of the European Parliament and of the Council of 27 April 2016 on the
protection of natural persons with regard to the processing of personal data and
on the free movement of such data, and repealing Directive 95/46/EC (General
Data Protection Regulation). https://eur-lex.europa.eu/eli/reg/2016/679/oj OJ L
119, 4.5.2016, p. 1; CELEX: 32016R0679; text with EEA relevance.
[26] European Parliament and Council of the European Union. 2022. Regulation (EU)
2022/2065 of the European Parliament and of the Council of 19 October 2022 on
a Single Market for Digital Services and amending Directive 2000/31/EC (Digital
Services Act). https://eur-lex.europa.eu/eli/reg/2022/2065/oj OJ L 277, 27.10.2022,
pp. 1–102; CELEX: 32022R2065; text with EEA relevance.
[27] Marian Friestad and Peter Wright. 1994. The persuasion knowledge model: How
people cope with persuasion attempts.Journal of consumer research21, 1 (1994),
1–31.
[28] Gönenç Gürkaynak and Ç Olgu Kama. 2018. Navigating the uncharted risks of
covert advertising in influencer marketing.Business Law Review39, 1 (2018).
[29] Jennifer L Harris, Kelly D Brownell, and John A Bargh. 2009. The food marketing
defense model: integrating psychological research to protect youth and inform
public policy.Social issues and policy review3, 1 (2009), 211–271.
[30] Donald Horton and R Richard Wohl. 1956. Mass communication and para-social
interaction: Observations on intimacy at a distance.psychiatry19, 3 (1956),
215–229.
[31] Martin Husovec. 2024.Principles of Digital Services Act. Oxford University Press,
Oxford.
[32] Basileal Imana, Aleksandra Korolova, and John Heidemann. 2025. Auditing for
Bias in Ad Delivery Using Inferred Demographic Attributes. InProceedings of
the 2025 ACM Conference on Fairness, Accountability, and Transparency (FAccT
’25). Association for Computing Machinery, New York, NY, USA, 2640–2656.
doi:10.1145/3715275.3732172
[33] Deborah Roedder John. 1999. Consumer socialization of children: A retrospective
look at twenty-five years of research.Journal of consumer research26, 3 (1999),
183–213.
[34] Monika Macenaite and Eleni Kosta. 2017. Consent for processing children’s
personal data in the EU: following in US footsteps?Information & Communications
Technology Law26, 2 (2017), 146–197. doi:10.1080/13600834.2017.1321096
[35] Maria T Maza, Kara A Fox, Seh-Joo Kwon, Jessica E Flannery, Kristen A Lindquist,
Mitchell J Prinstein, and Eva H Telzer. 2023. Association of habitual checking
behaviors on social media with longitudinal functional brain development.JAMA
pediatrics177, 2 (2023), 160–167.
[36] Christian Montag, Bernd Lachmann, Marc Herrlich, and Katharina Zweig. 2019.
Addictive features of social media/messenger platforms and freemium games
against the background of psychological and economic theories.International
journal of environmental research and public health16, 14 (2019), 2612.
[37] Matej Mosnar, Adam Skurla, Branislav Pecher, Matus Tibensky, Jan Jakubcik,
Adrian Bindas, Peter Sakalik, and Ivan Srba. 2025. Revisiting Algorithmic Audits
of TikTok: Poor Reproducibility and Short-term Validity of Findings. InProceed-
ings of the 48th International ACM SIGIR Conference on Research and Development
in Information Retrieval(Padua, Italy)(SIGIR ’25). Association for Computing
Machinery, New York, NY, USA, 3357–3366. doi:10.1145/3726302.3730293
[38] Ruvimbo Musiyiwa and Jenna Jacobson. 2023. Sponsorship disclosure in social
media influencer marketing: The algorithmic and non-algorithmic barriers.Social
Media+ Society9, 3 (2023), 20563051231196870.
[39] Agnes Nairn and Cordelia Fine. 2008. Who’s messing with my mind? The
implications of dual-process models for the ethics of advertising to children.
International Journal of Advertising27, 3 (2008), 447–470.
[40] Jessica Packer, Helen Croker, Anne-Lise Goddings, Emma J Boyland, Claire Stans-
field, Simon J Russell, and Russell M Viner. 2022. Advertising and young people’s
critical reasoning abilities: Systematic review and meta-analysis.Pediatrics150,
6 (2022), e2022057780.
[41] Cecilia Panigutti, Delia Fano Yela, Lorenzo Porcaro, Astrid Bertrand, and
Josep Soler Garrido. 2025. How to investigate algorithmic-driven risks in online
platforms and search engines? A narrative review through the lens of the EU
Digital Services Act. InProceedings of the 2025 ACM Conference on Fairness, Ac-
countability, and Transparency (FAccT ’25). Association for Computing Machinery,
New York, NY, USA, 828–839. doi:10.1145/3715275.3732052
[42] Branislav Pecher, Adrian Bindas, Jan Jakubcik, Matus Tuna, Matus Tibensky,
Simon Liska, Peter Sakalik, Andrej Suty, Matej Mosnar, Filip Hossner, and Ivan
Srba. 2026. Algorithmic Audit of Personalisation Drift in Polarising Topics on
TikTok. arXiv:2603.20723 [cs.IR] https://arxiv.org/abs/2603.20723
[43] Manoel Horta Ribeiro, Raphael Ottoni, Robert West, Virgílio A. F. Almeida, and
Wagner Meira. 2020. Auditing radicalization pathways on YouTube. InProceedings
of the 2020 Conference on Fairness, Accountability, and Transparency(Barcelona,
Spain)(FAT* ’20). Association for Computing Machinery, New York, NY, USA,
131–141. doi:10.1145/3351095.3372879
[44] Jan Ole Rixen, Luca-Maxim Meinhardt, Michael Glöckler, Marius-Lukas Ziegen-
bein, Anna Schlothauer, Mark Colley, Enrico Rukzio, and Jan Gugenheimer. 2023.
The loop and reasons to break it: Investigating infinite scrolling behaviour in
social media applications and reasons to stop.Proceedings of the ACM on Human-
Computer Interaction7, MHCI (2023), 1–22.
[45] Esther Rozendaal, Matthew A Lapierre, Eva A Van Reijmersdal, and Moniek
Buijzen. 2011. Reconsidering advertising literacy as a defense against advertising
effects.Media psychology14, 4 (2011), 333–354.
[46] Christian Sandvig, Kevin Hamilton, Karrie Karahalios, and Cedric Langbort. 2014.
Auditing algorithms: Research methods for detecting discrimination on internet
platforms.Data and discrimination: converting critical concerns into productive
inquiry22 (2014), 4349–4357.
[47] Jakub Simko, Matus Tomlein, Branislav Pecher, Robert Moro, Ivan Srba, Elena Ste-
fancova, Andrea Hrckova, Michal Kompan, Juraj Podrouzek, and Maria Bielikova.
2021. Towards Continuous Automatic Audits of Social Media Adaptive Behavior
and its Role in Misinformation Spreading. InAdjunct Proceedings of the 29th ACM
Conference on User Modeling, Adaptation and Personalization(Utrecht, Nether-
lands)(UMAP ’21). Association for Computing Machinery, New York, NY, USA,
411–414. doi:10.1145/3450614.3463353
[48] Sara Solarova, Matúš Mesarčík, Branislav Pecher, and Ivan Srba. 2026. Beyond the
Checkbox: Strengthening DSA Compliance Through Social Media Algorithmic
Auditing. arXiv:2601.18405 [cs.CY] https://arxiv.org/abs/2601.18405 Presented
at 2026 CHI Conference on Human Factors in Computing Systems.
[49] Ivan Srba, Robert Moro, Matus Tomlein, Branislav Pecher, Jakub Simko, Elena
Stefancova, Michal Kompan, Andrea Hrckova, Juraj Podrouzek, Adrian Gavornik,
and Maria Bielikova. 2023. Auditing YouTube’s Recommendation Algorithm for
Misinformation Filter Bubbles.ACM Trans. Recomm. Syst.1, 1, Article 6 (Jan.
2023), 33 pages. doi:10.1145/3568392
[50] Ivan Srba, Branislav Pecher, Jakub Simko, Robert Moro, and Maria Bielikova. 2025.
Model-based Algorithmic Auditing of Social Media AI Algorithms. InProceedings
of European Workshop on Algorithmic Fairness, EW AF’25. June 30 – July 02, 2025.
Eindhoven, NL.
[51] Laurence Steinberg. 2004. Risk taking in adolescence: what changes, and why?
Annals of the New York Academy of Sciences1021, 1 (2004), 51–58.
[52] TikTok. 2025.Branded Content Policy. TikTok. https://www.tiktok.com/legal/
page/global/bc-policy/en Last updated July 2025.
[53] TikTok. 2025.Community Guidelines. TikTok. https://www.tiktok.com/
community-guidelines/en-GB Released April 17, 2024; updated September 13,
2025.
[54] TikTok. 2025.TikTok Library FAQ. TikTok. https://library.tiktok.com/faq
Frequently Asked Questions about the TikTok Library (accessed online).

The DSA’s Blind Spot: Algorithmic Audit of Advertising and Minor Profiling on TikTok FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
[55] TikTok. 2025. TikTok – DSA Transparency Report: January – June 2025.
https://sf16-va.tiktokcdn.com/obj/eden-va2/zayvwlY_fjulyhwzuhy%5B/
ljhwZthlaukjlkulzlp/DSA_H1_2025/TikTok-DSATransparencyReport-January-
June-2025.pdf. Accessed: 2026-01-07.
[56] TikTok For Business. 2025.About the Commercial Content Disclosure Setting
for Creators. TikTok. https://ads.tiktok.com/help/article/about-the-content-
disclosure-setting-for-creators Last updated December 2025.
[57] Matus Tomlein, Branislav Pecher, Jakub Simko, Ivan Srba, Robert Moro, Elena Ste-
fancova, Michal Kompan, Andrea Hrckova, Juraj Podrouzek, and Maria Bielikova.
2021. An Audit of Misinformation Filter Bubbles on YouTube: Bubble Bursting
and Recent Behavior Changes. InProceedings of the 15th ACM Conference on
Recommender Systems(Amsterdam, Netherlands)(RecSys ’21). Association for
Computing Machinery, New York, NY, USA, 1–11. doi:10.1145/3460231.3474241
[58] Aleksandra Urman, Mykola Makhortykh, and Aniko Hannak. 2025. WEIRD
Audits? Research Trends, Linguistic and Geographical Disparities in the Algo-
rithm Audits of Online Platforms - A Systematic Literature Review. InProceed-
ings of the 2025 ACM Conference on Fairness, Accountability, and Transparency
(FAccT ’25). Association for Computing Machinery, New York, NY, USA, 375–390.
doi:10.1145/3715275.3732026
[59] Eva A Van Reijmersdal, Sophie C Boerman, Moniek Buijzen, and Esther Rozendaal.
2017. This is advertising! Effects of disclosing television brand placement on
adolescents.Journal of youth and adolescence46, 2 (2017), 328–342.
[60] Eva A Van Reijmersdal, Esther Rozendaal, Nadia Smink, Guda Van Noort, and
Moniek Buijzen. 2017. Processes and effects of targeted online advertising among
children.International journal of advertising36, 3 (2017), 396–414.
[61] Georgia Wells, Jeff Horwitz, and Deepa Seetharaman. 2021. Facebook Knows
Instagram Is Toxic for Teen Girls, Company Documents Show.The Wall Street
Journal(14 September 2021). https://https://www.wsj.com/tech/personal-
tech/facebook-knows-instagram-is-toxic-for-teen-girls-company-documents-
show-11631620739
[62] Pieter Wolters and Frederik Zuiderveen Borgesius. 2025. The EU Digital Services
Act: what does it mean for online advertising and adtech?International Journal
of Law and Information Technology33 (2025), eaaf004. doi:10.1093/ijlit/eaaf004
A Prompts Utilized for Automatic Data
Annotation
The prompt used by LLM (GPT-4.1) as a part of theuser interaction
predictor:
Your task is to determine the topic and the stance of the video
given its available metadata. The only possible answers for the
topic is: 1) beauty, 2) fitness, 3) gaming, 4) politics. For
stance, the possibilities are: 1) support; 2) oppose. Use only
these possibilities when answering.
Here is a closer description for the topics and their stances:
Beauty should be given to anything that is related to beauty or
personal care and related products.
Fitness should be given to anything that is related to fitness,
exercise, workouts and related products.
Gaming should be given to anything that is related to video games or
computer hardware.
Politics should be given to anything that is related to politics,
national policies, elections and world events. For example
politics related to economy, employment, war and peace, housing
, education.
Other should be given to anything that is not related to the
previous topics.
In this case, the stance does not matter, so always put support.
Provide the answer in structured form that looks like this:
Topic: beauty/fitness/gaming/politics/other
Stance: support/oppose
Here is the video information.
Author: {author_name}
Video description and hashtags: {video_description_and_hashtags}
Video transcript: {video_transcript}
The prompt used by LVLM (Qwen3-VL-4B-Instruct) as a part of
thead detection and classification pipeline:
You are an assistant that identifies commercial content, both
disclosed and undisclosed, in TikTok videos for regulatory
compliance audits.
Your task is to analyze a screenshot from a short-video platform and
classify it into specific categories.
INSTRUCTIONS:
1. Detection: Determine if the image contains an advertisement.
2. Type Classification: If it is an ad, classify the TYPE based on
visual indicators:
- Formal: Look for platform-injected labels "Sponsored" or "Ad"
displayed on the bottom of the video.
- Influencer: Look for creator-injected labels "Paid partnership"
or "Promotional content" displayed on the bottom of the
video,
- Other: Look for videos with commercial content that lacks
proper disclosure. Look for: product names or prices or
discount codes mentioned/shown, brand endorsements by the
creator, or promotional hashtags (e.g., #ad, #partnership,
#collaboration) used without corresponding platform
disclosure labels.
3. Topic Classification: Classify the primary content of the ad into
exactly one of these categories:
-`beauty`(makeup, skincare, cosmetics, clearskin, kbeauty,
glasskin)
-`fitness`(abs, workout, gym, sports, health, nutrition, gymtok
, supplements)
-`gaming`(video games, consoles, streamers, gamer, gaming,
gamerlife)
-`politics`(political news, political debate, voting,
politicians, breaking news)
-`other`(anything else)
RESPONSE FORMAT:
Reply with valid JSON only.
IMPORTANT: Do NOT use double quotes " inside your string values. Use
single quotes'instead.
Example: "reasoning": "The text says'Buy now'which implies..."
{
"is_ad": boolean,
"ad_type": "formal" | "influencer" | "other" | null,
"ad_topic": "beauty" | "fitness" | "gaming" | "politics" | "other"
| null,
"visual_indicators": ["list", "of", "labels", "found"],
"reasoning": "brief explanation"
}
B Summary of collected data
Table 4 provides a summary of all data collected during the main
audit phase. These numbers provide necessary basis for all calcula-
tions, tables and figures presented in the Section 4.2.
C Tool for Examination and Manual
Annotation of Collected Data
For the purposes of initial examination and manual annotation of
data collected during the algorithmic auditing study, we have devel-
oped a custom tool visualizing the collected data. After selecting the
corresponding simulated user, it allows to display an overview of
TikTok videos displayed to a user, with options to filter the content
according to the ad type and topic (Figure 4). By selecting a specific
video, it provides a video detail page showing the selected frame
from the video, automatic content analysis as well as additional
content metadata collected during the study (Figure 5).

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Solarova et al.
Table 4: Summary table of data collected during the audit.
Interest beauty beauty fitness fitness gaming gaming
Age Group minor adult minor adult minor adult
Gender female female male male female female
Total Records 651 1088 876 2341 868 1271
Non Ad Records 482 842 831 1807 817 970
Ads Detected 169 246 45 534 51 301
Avg Video Length 54.8 35.6 35.8 14 30 30
Formal Ads 21 6 0 301 7 208
Formal Ads / Beauty 1 2 0 62 2 24
Formal Ads / Fitness 1 0 0 58 0 19
Formal Ads / Gaming 2 3 0 25 3 49
Formal Ads / Other 17 1 0 156 2 116
Disclosed Ads 8 8 1 10 5 20
Disclosed Ads / Beauty 7 8 0 1 0 0
Disclosed Ads / Fitness 0 0 1 8 0 0
Disclosed Ads / Gaming 0 0 0 0 5 19
Disclosed Ads / Other 1 0 0 1 0 1
Undisclosed Ads 140 232 44 223 39 73
Undisclosed Ads / Beauty 129 146 3 11 2 0
Undisclosed Ads / Fitness 10 81 39 206 0 1
Undisclosed Ads / Gaming 0 2 0 2 36 63
Undisclosed Ads / Other 1 3 2 4 1 9
(a) Ad Type - Annotator 1
 (b) Ad Type - Annotator 2
(c) Ad Topic - Annotator 1
 (d) Ad Topic - Annotator 2
Figure 3: Predicted-true confusion matrices for ad type and
ad topic labels for each of human annotators.
The tool served during this study two purposes: 1) it allows
us to effectively examine the collected data and obtain the first
insights, as well as 2) it provides us the mean to manually evaluate
the accuracy of automatic data analysis.

The DSA’s Blind Spot: Algorithmic Audit of Advertising and Minor Profiling on TikTok FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
Figure 4: Screenshot of the custom-developed tool providing an overview of the collected data. The displayed videos were
presented to a user Beauty Minor (a 16-year-old minor with an expressed interest in beauty). The tags determine whether the
annotation model determined any kind of advertisement or not. The faces and personal identifying information were blurred
or anonymised to preserve creators’ privacy.

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Solarova et al.
Figure 5: Screenshot of the custom-developed tool providing a detail of the video observed by a user. The displayed video was
presented to a user Fitness Minor (a 17-year-old minor with an expressed interest in fitness). The tool displays automatic content
analysis (including the reasoning of the model) together with the screenshot and URL to the video, streamlining the manual
annotation process. The displayed video represents an example of paid partnership content. The faces and personal identifying
information were hidden or anonymised to preserve creators’ privacy.
