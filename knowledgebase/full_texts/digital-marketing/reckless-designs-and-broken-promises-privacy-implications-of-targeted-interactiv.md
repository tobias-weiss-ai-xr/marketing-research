---
title: 'Reckless Designs and Broken Promises: Privacy Implications of Targeted Interactive Advertisements
  on Social Media Platforms'
url: https://arxiv.org/abs/2603.03659
category: digital-marketing
subcategory: empirical
date: 2026-03
venue: ''
authors:
- Julia B. Kieserman
- Athanasios Andreou
- Laura Edelson
- Sandra Siby
- Damon McCoy
source: arxiv
pdf_url: https://arxiv.org/pdf/2603.03659
pages: 4
chars: 12452
fetched_at: '2026-11-08T12:59:41+00:00'
kb_version: 1
---

# Reckless Designs and Broken Promises: Privacy Implications of Targeted Interactive Advertisements on Social Media Platforms

Reckless Designs and Broken Promises: Privacy Implications of Targeted Interactive
Advertisements on Social Media Platforms
Julia B. Kieserman 1, Athanasios Andreou 1, Laura Edelson 2, Sandra Siby 3, Damon McCoy 1,
1New York University
2Northeastern University
3New York University Abu Dhabi
Emails:{julia.kieserman, a.andreou, sandra.siby, mccoy}@nyu.edu, l.edelson@northeastern.edu
Abstract—Popular social media platforms TikTok, Facebook
and Instagram allow third-parties to run targeted advertising
campaigns on sensitive attributes in-platform. These ads are
interactive by default, meaning users can comment or “react”
(e.g., “like”, “love”) to them. We find that this platform-level
design choice creates a privacy loophole such that advertisers
can view the profiles of those who interact with their ads, thus
identifying individuals that fulfill certain targeting criteria.
This behavior is in contradiction to the promises made by
the platforms to hide user data from advertisers. We conclude
by suggesting design modifications that could provide users
with transparency about the consequences of ad interaction to
protect against unintentional disclosure.
1. Introduction
Many social media companies own and operate adver-
tising tools. With a wealth of users, and user data, they are
well-equipped to help advertisers reach large numbers of
people targeted across a diverse set of demographics and
interests. There are known issues with targeted advertising,
including that they exhibit discriminatory behavior, rely on
sensitive user attributes, and target individual users [1]–[3].
Nevertheless, social media companies claim that they protect
user privacy from advertisers. For example, TikTok claims
that they share only “aggregated statistics and insights with
users of our analytics services” [4]. Similarly, Faceook
promises not to tell “advertisers who you are or sell your
information to anyone” [5].
However, the design decisions made by platforms may
impact their ability to uphold these privacy claims. TikTok
and Meta, the focus of this study and two advertising
platforms with significant user bases, have designed their
infrastructure such that ads are interactive by default. Much
like user-generated content, users can comment on or react
to (e.g., “like,” “love”) an ad. This leaves a record of
engagement which, if made visible to advertisers, would
create a privacy loophole; since advertisers already know
the potentially sensitive nature of the targeting criteria they
have selected (e.g., household income, dependents’ age), this
would allow them to learn the usernames of individuals that
fit this criteria.
To understand if this is possible, we ran advertisements
on TikTok and Meta (Instagram and Facebook). We found
that neither platform takes precautions to obscure the in-
dividual usernames of those who interact with ads from
advertisers. TikTok shares the username of individuals who
comment on (but not react to) ad content directly through
the advertising interface. Meta shares the usernames of
both users who comment and users who react to an ad.
This means that users who interact with targeted ads are
inadvertently identifying themselves to advertisers as indi-
viduals who meet specific targeting criteria. In summary, we
demonstrate that social media platforms leak the personal
data of users who interact with advertisements directly to
advertisers, in contradiction to their own documentation.
2. Background
Many social media platforms provide an infrastructure
and user interface for advertisers to run marketing cam-
paigns. These platforms make a set of design choices, and
expose certain configuration options to advertisers, which
dictate how users experience ads. As a baseline, advertisers
typically need to specify a budget and creative copy (i.e.,
photo or video advertisements). After the initial setup, adver-
tisers can use a provided user interface to view aggregated
metrics about who viewed their advertisements, including
demographics (e.g., age, gender, geography) and device in-
formation (e.g., iOS, Android). Two of these design choices,
when combined, have significant privacy implications: tar-
geting and interactivity.
Targeting. Platforms like Meta and TikTok allow
advertisers to choose from a set of platform-defined target-
ing criteria to determine what characteristics about users
should make them eligible to view an ad. A subset of the
targeting options are potentially sensitive including age and
gender (TikTok and Meta), household income (TikTok and
Meta), U.S. postal code (Meta), age range of dependents
(Meta), and interest and behavior-based targeting (TikTok
and Meta). Targeted advertising alone can be privacy inva-
sive; prior work has shown it can facilitate discriminatory
targeting [2], use sensitive user attributes [1], and, with the
right combination of attributes, target individual people [3].
arXiv:2603.03659v2  [cs.CR]  5 Mar 2026

Platform Person Who Commented Visible Person Who Reacted Visible Interactivity Configurable
Meta(Facebook + Instagram) ✓ ✓ ✻
TikTok ✓ ✓
TABLE 1: Summary interaction data visibility and configurability across platforms
✻The documentation suggests it is available in a limited capacity but it was not available to the papers’ authors.
Further, despite calls for user ad transparency and the in-
troduction of features like Meta’s “Why Am I Seeing This
Ad” [6], users still have no way to adequately understand
why they were targeted for a particular ad [7], and thus what
sensitive attribute groups they belong to.
Interactivity. Ad interactivity, which allows users
to comment on an ad, is a default behavior in both Meta
and TikTok. It is configurable in TikTok, although the
user interface hides the toggle and the accompanying text
description discourages advertisers from disabling this fea-
ture (Appendix Figure 2). Although the ability to disable
comments in the Meta ads interface is reported to exist
in a limited capacity, it was not available to our business
account at the time of the study [8]. There are ways to limit
interactions through the post, but not disable them entirely.
3. Case Studies: TikTok and Meta
To find out if user information is visible to advertisers,
we ran advertisements on TikTok and Meta using their UI
business tools. Our advertisements were targeted to users
over 18 in the United States.
TikTok. We ran our TikTok advertisement (Figure 1)
on December 18-20, 2025, where it was viewed 11,667
times. Two users commented on the advertisement and one
”liked” it. Through the TikTok advertising interface, we
were able to view the name and profile image of the users
that left a comment. We were not able to view the username
of the individual who ”liked” it.
Figure 1: Advertisement run through TikTok’s campaign platform,
which targeted users over 18 in the United States.
Meta. We ran our Meta advertisement (nearly iden-
tical to Figure 1) on January 6-9, 2026, across Facebook and
Instagram. It was shown to approximately 13,755 accounts
on Facebook and 17,546 on Instagram. On Facebook, it
received 4 reactions, all of which were visible to advertisers
with a username and profile photo. On Instagram, it received
11 comments and 14 reactions. We were able to view the
username and photo for 10 out of 11 comments and the
username, account name, and profile photo for 8 of the
14 reactions. We do not know exactly why some of the
comments/reactions were hidden, but we verified that the
visible reactions and comments came from a mixture of
public and private accounts. As our ad was not shared on
either platform, we do not know how that action might
impact data visibility but see it as an area for future work.
Ethics. Our study was reviewed and approved by
our Institutional Review Board (IRB). The content of the
advertisement (Figure 1) clearly stated its intended purpose
and the potential implications for users who interacted with
it. We did not recruit participants and used the broadest
possible targeting criteria through the platforms’ interface
to target only users over 18 who are in the United States.
Finally, we did not remove any user data from the platform
or perform further analysis.
4. Discussion and Future Work
Our findings show that users who interact with ad-
vertisements on TikTok and Meta expose their usernames
to advertisers, thus revealing that they are identifiable by
potentially sensitive targeting criteria. The platform decision
to make ads interactive (by default or as the only option) is
not simply an inevitable consequence of online advertising.
Other platforms that serve advertisements to users (e.g.,
YouTube) treat it as fundamentally different content that
users can not actively engage with and therefore are unlikely
to have this privacy issue.
Platforms may argue that by choosing to interact with
an ad, users are implicitly agreeing or even taking respon-
sibility for sharing their username (or legal names [9]) with
advertisers. However, they are doing more than that; they are
linking their username to a specific set of unknown targeting
criteria, likely unwittingly disclosing potentially sensitive
information about themselves [10]. Future work could in-
vestigate how users understand the privacy implications of
interactive ads and how it changes their platform behavior.
Platforms like TikTok and Meta could consider other
design choices that alleviate the risk of users unintentionally
identifying themselves to advertisers. One method would be
to include disclaimers in both the user documentation and
in-platform ads, as well as a correction to the inaccurate
statements currently in the documentation, that warn users
of the consequences of interacting with an ad. However,
this is not ideal as it puts undue burden on users. As an
alternative, platforms could commit to turning interactivity
off by default.

Acknowledgment
This work was funded by National Science Founda-
tion Grant #2151837 and NYU Abu Dhabi’s 19WSN Co-
Mentoring Initiative.
References
[1] A. Andreou, M. Silva, F. Benevenuto, O. Goga, P. Loiseau, and
A. Mislove, “Measuring the facebook advertising ecosystem,” in
NDSS 2019-Proceedings of the Network and Distributed System
Security Symposium, 2019, pp. 1–15.
[2] T. Speicher, M. Ali, G. Venkatadri, F. N. Ribeiro, G. Arvanitakis,
F. Benevenuto, K. P. Gummadi, P. Loiseau, and A. Mislove, “Potential
for discrimination in online targeted advertising,” inConference on
fairness, accountability and transparency. PMLR, 2018, pp. 5–19.
[3] J. Gonz ´alez-Caba˜nas, ´A. Cuevas, R. Cuevas, J. L´opez-Fern´andez, and
D. Garc´ıa, “Unique on facebook: formulation and evidence of (nano)
targeting individual users with non-pii data,” inProceedings of the
21st ACM Internet Measurement Conference, 2021, pp. 464–479.
[4] TikTok, “Privacy Policy — TikTok,” https://web.archive.org/
web/20251204211610/https://www.tiktok.com/legal/page/row/
privacy-policy/en, 2025, Accessed: 2025-12-30.
[5] Meta, “Hard Questions: What Information Do Facebook Advertis-
ers Know About Me?” https://web.archive.org/web/20250903200256/
https://about.fb.com/news/2018/04/data-and-advertising/, 2018, Ac-
cessed: 2025-12-22.
[6] ——, “Increasing Our Ads Transparency,” https://web.archive.
org/web/20251124152052/https://about.fb.com/news/2023/02/
increasing-our-ads-transparency/, 2025, Accessed: 2026-1-13.
[7] J. Burgess, N. Carah, D. Angus, A. Obeid, and M. Andrejevic, “Why
am i seeing this ad? the affordances and limits of automated user-
level explanation in meta’s advertising system,”New Media & Society,
vol. 26, no. 9, pp. 5130–5149, 2024.
[8] Samantha Stetson, “Advertising Week 2024: New Brand Suitability
Controls — Meta for Business,” https://web.archive.org/web/
20241122001220/https://www.facebook.com/business/news/
Advertising-Week-2024-New-Brand-Suitability-Controls, 2025,
Accessed: 2026-01-13.
[9] Meta, “Names allowed on Facebook — Facebook Help
Center,” https://web.archive.org/web/20250812210152/https:
//www.facebook.com/help/229715077154790, , Accessed: 2025-
12-22.
[10] A. Andreou, G. Venkatadri, O. Goga, K. P. Gummadi, P. Loiseau,
and A. Mislove, “Investigating ad transparency mechanisms in social
media: A case study of facebook’s explanations,” inNDSS 2018-
Network and distributed system security symposium, 2018, pp. 1–15.

Appendix
Figure 2: Configuration to disable user comments on TikTok
advertisements
Figure 3: Screenshot of Meta’s interface for setting targeting
criteria
