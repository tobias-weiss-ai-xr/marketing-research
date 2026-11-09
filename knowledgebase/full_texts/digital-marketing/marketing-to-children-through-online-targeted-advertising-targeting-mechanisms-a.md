---
title: 'Marketing to Children Through Online Targeted Advertising: Targeting Mechanisms and Legal Aspects'
url: https://arxiv.org/abs/2310.04104
category: digital-marketing
subcategory: empirical
date: 2023-10
venue: ''
authors:
- Tinhinane Medjkoune
- Oana Goga
- Juliette Senechal
source: arxiv
pdf_url: https://arxiv.org/pdf/2310.04104
pages: 16
chars: 103036
fetched_at: '2026-11-08T13:12:25+00:00'
kb_version: 1
---

# Marketing to Children Through Online Targeted Advertising: Targeting Mechanisms and Legal Aspects

Marketing to Children Through Online Targeted Advertising:
Targeting Mechanisms and Legal Aspects
Tinhinane Medjkoune
Univ. Grenoble Alpes, CNRS,
Grenoble INP, LIG
France
Oana Goga
LIX, CNRS, Inria, Ecole Polytechnique,
Institut Polytechnique de Paris
France
Juliette Senechal
Université de Lille, CRDP,
DReDIS-IRJS
France
ABSTRACT
Many researchers and organizations, such as WHO and UNICEF,
have raised awareness of the dangers of advertisements targeted
at children. While most existing laws only regulate ads on televi-
sion that may reach children, lawmakers have been working on
extending regulations to online advertising and, for example, forbid
(e.g., the DSA) or restrict (e.g., the COPPA) advertising based on
profiling to children.
At first sight, ad platforms such as Google seem to protect chil-
dren by not allowing advertisers to target their ads to users that
are less than 18 years old. However, this paper shows that other
targeting features can be exploited to reach children. For example,
on YouTube, advertisers can target their ads to users watching a
particular video through placement-based targeting, a form of con-
textual targeting. Hence, advertisers can target children by simply
placing their ads in children-focused videos. Through a series of ad
experiments, we show that placement-based targeting is possible
on children-focused videos and, hence, enables marketing to chil-
dren. In addition, our ad experiments show that advertisers can use
targeting based on profiling (e.g., interest, location, behavior) in
combination with placement-based advertising on children-focused
videos. We discuss the lawfulness of these two practices with re-
spect to DSA and COPPA.
Finally, we investigate to which extent real-world advertisers are
employing placement-based targeting to reach children with ads on
YouTube. We propose a measurement methodology consisting of
building a Chrome extension able to capture ads and instrumenting
six browser profiles to watch children-focused videos. Our results
show that 7% of ads that appear in the children-focused videos
we test use placement-based targeting. Hence, targeting children
with ads on YouTube is not only hypothetically possible but also
occurs in practice. We believe that the current legal and technical
solutions are not enough to protect children from harm due to
online advertising. A straightforward solution would be to forbid
placement-based advertising on children-focused content.
CCS CONCEPTS
• Information systems→ Online advertising.
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than the
author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or
republish, to post on servers or to redistribute to lists, requires prior specific permission
and/or a fee. Request permissions from permissions@acm.org.
CCS ’23, November 26–30, 2023, Copenhagen, Denmark
© 2023 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM ISBN 979-8-4007-0050-7/23/11. . . $15.00
https://doi.org/10.1145/3576915.3623172
KEYWORDS
YouTube, online advertising, children
ACM Reference Format:
Tinhinane Medjkoune, Oana Goga, and Juliette Senechal. 2023. Marketing
to Children Through Online Targeted Advertising: Targeting Mechanisms
and Legal Aspects. In Proceedings of the 2023 ACM SIGSAC Conference on
Computer and Communications Security (CCS ’23), November 26–30, 2023,
Copenhagen, Denmark. ACM, New York, NY, USA, 16 pages. https://doi.org/
10.1145/3576915.3623172
1 INTRODUCTION
Many researchers have studied how advertisements affect children
since their television appearance and highlight their potential neg-
ative impact on children’s development and well-being [43]. One
reason why advertisements can harm children is that their cognitive
skills are underdeveloped. Children cannot distinguish an advertise-
ment from a television program before age three and hence cannot
fire the mental defenses adults have when seeing ads [ 56]. Only
between the ages of 8 and 12 do children begin to understand the
commercial ambitions of ads [61]. Nevertheless, even if they un-
derstand the underlying commercial intent, the attractive nature of
advertisements makes children infatuated with them (see Section 7).
As WHO & UNICEF put it in their 2020 report [11]: “Marketing to
children is deliberate, strategic, innovative and well resourced, and
exploits their developmental vulnerability. ”
Understandably, many laws across the World forbid or restrict
children’s advertising. For example, in France, Article 7 of the de-
cree of March 27, 1992, states that “advertising must not cause moral
or physical harm to minors [...] it must not directly encourage minors
to purchase a product or service by exploiting their inexperience or
credulity [...]” and Article 15 of the same decree prohibits advertis-
ing breaks on television during children’s programs of less than
30 minutes [41]. While most existing laws have been set to pro-
tect children from television ads, legislators worldwide have been
working on updating legislation to consider ads on social media
and streaming platforms.
Given the gravity of the problem, in this paper, we focus onunder-
standing whether children can be targeted with ads on online stream-
ing platforms.1 For clarity, our work focuses not on whether children
accidentally see ads while watching videos on online streaming
platforms but on whether advertisers can intentionally target them
with ads. We take YouTube as a case study as it is one of the most
used online platforms for children [10, 55]. Understanding how and
if advertisers can reach children is essential for understanding what
1By targeting children, we refer to any means an advertiser can exploit features provided
by online advertising platforms to reach an audience made mostly of children; hence,
targeting does not necessarily mean micro-targeting or profiling.
arXiv:2310.04104v1  [cs.SI]  6 Oct 2023

CCS ’23, November 26–30, 2023, Copenhagen, Denmark Tinhinane Medjkoune, Oana Goga, & Juliette Senechal
risks targeting technologies bring to children, understanding what
transparency we need, and helping inform lawmakers with adapted
restrictions.
We review in Section 3 legal acts that relate to advertising to
children in the U.S. and Europe to understand what is currently
legally allowed, forbidden, or restricted. In particular, we exam-
ine the Children’s Online Privacy Protection Rule (COPPA) in the
U.S. [23] and the Digital Services Act, a new Regulation voted on
19 October 2022 at the European Union level [46]. The COPPA Act
does not prohibit advertising to children; however, it places some
restrictions on it: it states that advertisers and content owners may
not collect any personal information (which includes cookies and
other persistent identifiers) from children under 13 years of age
without verifiable parental consent. Hence, COPPA restricts online
platforms’ capabilities to serve profile-based ads to children but
does not restrict contextual-based advertising. The DSA takes a step
further and forbids altogether targeting children with ads based on
profiling (e.g., interest, location, behavior).
On the technical side, ad platforms have also deployed solutions
to protect children from online marketing. For example, the ad-
vertising interface on Google does not allow advertisers to target
users less than 18 years old [ 30]. In addition, Google launched
YouTube Kids in 2015. This platform only contains content (videos
and ads) filtered explicitly for children. Content creators and ad-
vertisers cannot explicitly ask for their videos or ads to be shown
on YouTube Kids. YouTube curates content in an independent way
(see Section 2) [ 28]. As there is no direct way to target children
on YouTube Kids, this paper focuses on targeting mechanisms that
allow advertisers to target children on YouTube. This choice is
consequential because content available on YouTube Kids is also
available on YouTube, and previous studies showed parents use
YouTube more frequently than YouTube Kids to let their children
watch videos [37].
First, we investigate what targeting mechanisms can be exploited
to target children with ads on YouTube (see Section 4). We find
that, Google allows advertisers to target their ads to users watch-
ing a particular video through placement-based targeting, a form
of contextual advertising. Hence, advertisers could target children
by simply placing their ads in children-focused videos. Through
a series of real-world ad experiments, we show that placement-
based targeting is allowed on a set of children-focused videos we
curated from YouTube Kids, hence, enabling marketing to chil-
dren. In addition, through four other ad campaigns, we show that
placement-based targeting on children-focused videos can be used
in combination with targeting based on profiling. 2 According to
our legal analysis, placement-based targeting on children-focused
videos is not forbidden by either the COPPA or the DSA; however,
the use of profiling for targeting children is forbidden in the DSA
and might be (as the text is not clear in this respect) forbidden in
the COPPA as well. Hence, combining placement-based targeting
with targeting based on profiling is against these rules.
Second, we investigate if advertisers exploit these targeting
mechanisms to reach children in the wild (see Section 5). For this,
2For example, target users interested in Sports that are watching the video “Peppa
Learns How To Whistle. ”
we propose a measurement methodology that consists of build-
ing a Chrome extension that can collect data about the ads shown
on YouTube videos and instrument six browser profiles to watch
children-focused videos. Using this approach, we collected 3,321 ads
that appear on 620 videos. Next, given an ad shown on a particular
video, the challenge is to distinguish whether the ad was targeted
based on contextual parameters (e.g., placement-based), based on
profiling parameters (e.g., behavior, interest, location), or based on
other parameters such as time and language. We find a simple yet
effective way to make the distinction by exploiting the ad explana-
tions provided in the “Why you’re seeing this ad” feature [35]. Our
analysis shows that 7% of the ads we collected while watching two
sets of children-focused videos (across the six profiles) had an ad ex-
planation suggesting the advertiser used placement-based targeting.
In addition, 25% of ads collected on children-focused videos had ad
explanations suggesting they have been targeted based on profiling.
While these numbers are not representative and are obtained over
a small scale dataset, they show that targeting children is not only
hypothetically possible but also appears to occur in practice.
Finally, we observe that YouTube provides a reduced level of
transparency for ads on YouTube videos labeled as being suitable
for children3 compared to other videos (see Section 5.3). To val-
idate this, we created an ad campaign and instructed Google to
use placement-based targeting and show it on ten videos sourced
from YouTube Kids and ten adult-focused videos. Whenever our
ad was shown on adult-focused videos, it had the ad explanation,
“The video you are watching. ” that reflected precisely our targeting
parameters. However, on the children-focused videos sourced from
YouTube Kids, the explanation was: “Personalization is disabled
for this account or content. Therefore, this ad is not personalized
based on your data. Its distribution depends on other factors (such
as the time or your geographical position)”. While this explana-
tion is not necessarily wrong, it does not reflect the precise target-
ing parameters we used in our ad campaign. Hence, for the same
ad campaign (and the same targeting parameters) and the same
profile watching the video, Google showed different ad explana-
tions depending on whether the video was present on YouTube
Kids or not. Therefore, not only can children be targeted with ads
through placement-based advertising, the ad explanations provided
on children-focused videos do not reflect the use of such targeting.
The implications of this study are multi-faceted. Since many
countries are updating their legislation to protect children from
online harm, we hope our paper clarifies how advertisers can reach
children online and provides valuable technical insights. In partic-
ular, we want to raise awareness that advertisers can reach chil-
dren through placement-based advertising. While the DSA and the
COPPA do not currently forbid this practice, we think regulators
have not realized that contextual advertising can be done at the
granularity of the video the user is watching and, hence, can be
used to reach children watching well chosen sets of videos that
could be indicators of their age, gender, or interests. Even worse,
current online advertising legislation is missing clear guidelines on
the ad content that can be targeted at children (as in the case of
3These YouTube videos have a redirection to YouTube Kids as shown in Figure 2 in
appendix just below the video content.

Marketing to Children Through Online Targeted Advertising: Targeting Mechanisms and Legal Aspects CCS ’23, November 26–30, 2023, Copenhagen, Denmark
television advertising); this is important to clarify, especially since
placement-based advertising is currently allowed.
We believe that the current legal and technical solutions are not
enough to protect children from harm due to online advertising.
We recommend that: (1) Regulators and ad platforms should simply
forbid placement-based advertising on children-focused content.
(2) Regulators should set clear guidelines on the ad content that
can be shown on children-focused content, including ads that are
shown because they were targeted at children-focused content or
ads that appear there by chance and use other targeting parame-
ters. (3) When addressing Article 39 (Additional online advertising
transparency) in the DSA, ad platforms should include, for all ads,
whether the advertiser used placement-based targeting and pro-
vide the complete list of placements used by the advertiser. This
will enable researchers to check if the ads’ content is harmful to
the chosen audience. (4) Ad platforms should provide consistent
ad explanations for the same ad. Ad explanations should not be
generated on the fly based on the content watched or the profile
of the user watching. In addition, we believe that the current ad
explanations provided by Google on children-focused videos are
misleading and not “meaningful” as demanded in Article 26 of the
DSA.
At last, we want to salute efforts from online platforms to provide
data about how their systems work, including explanations of why
users receive particular ads and detailed statistics on ad delivery.
Without such platform-provided data, this auditing study could not
have been performed.
2 BACKGROUND
2.1 Advertising on YouTube
Google provides seven broad categories of targeting for advertising
on YouTube [33]:
• Location-based: Advertisers can specify the country, city, postal
codes, or a radius as small as 1 km around an address.
• Demographic-based: Advertisers can select over 440 combina-
tions of demographic groups based on gender, age, parental status,
and household income.
• Behavioral or interest-based: Advertisers can select people
with particular interests (such as technology), habits (such as Cin-
ema enthusiasts), or Market Audience and Life Events.
• Re-targeting: Re-targeting allows advertisers to reach on YouTube,
the users that visited their websites or application (outside Google
or YouTube). Advertisers can also upload a CSV file that contains
the contact information (e.g., emails, phone numbers, physical ad-
dresses) of the users they want to reach. This data is typically
collected through loyalty cards.
• Keyword-based: Advertisers can specify a list of keywords, and
their ads will appear when users search for the particular keywords
on YouTube.
• Theme-based: This allows advertisers to place their ads on videos
related to a specific topic. There are over 26 proposed topics ranging
from real estate to art.
• Placement-based: This targeting category is the most interesting
to our study. Google allows advertisers to specify precisely on which
YouTube channels or videos they wish their ads to appear on (see
Figure 1: Placement-based targeting in Google.
Figure 1). For example, an advertiser can specify their ad should
only appear on the "Food Court: France Edition" video.
Both theme-based advertising and placement-based advertising
are two forms of contextual-based advertising, as the targeting
is based only on information related to the content and not the user.
For placement-based targeting, the advertiser specifies precisely
the placement of the ad; hence, the ad will then appear only on the
specific videos selected by the advertiser. For theme-based targeting,
the advertiser just specifies the theme, and the ad platform decides
what videos are related to the theme selected by the advertiser.
Demographic, behavioral, interest-based as well as re-targeting
are forms of profiling-based advertising, as the targeting is based
on information gathered on the (historical) activity of the user. This
targeting is also sometimes called personalized advertising.
These targeting categories can be combined when placing an
ad. In addition, advertisers can set the language, the time when to
broadcast the ad and the devices used by the users they want to
reach. Google imposes a minimum reach requirement, and ads will
not be delivered if Google estimates they have an audience of less
than 1000 users. Finally, Google proposes an “audience expansion”
feature that gives Google the power to expand the targeting to
additional relevant audiences [29].
Google supports different ad formats: (1) in-stream video ads –
which appear before, during, or after a YouTube video watched on
YouTube or the Display Network. The Display Network is made of
applications on mobile phones or websites that partner with Google
to serve their ads. A video ad can be skippable or not, depending
on the parameters chosen by the advertiser. (2) floating banner ad –
which is an image banner shown on top of the video watched for
several seconds. And (3) video discovery ads–that can appear on the
YouTube search results page, alongside related videos, or on the
YouTube homepage.
Transparency All ads are marked with an "Ad" disclaimer. When
users are watching an ad, they can click on “Why you’re seeing this
ad” to learn what parameters and data were used to target the ad.
Figure 4 (appendix) shows a screenshot of such an ad explanation.
2.2 Advertising on YouTube Kids
YouTube Kids is a video streaming platform that only contains
video content curated for children [ 37]. While YouTube Kids is
widely adopted, still more parents say they are using YouTube to
let their children watch videos [45]. Videos that are on YouTube

CCS ’23, November 26–30, 2023, Copenhagen, Denmark Tinhinane Medjkoune, Oana Goga, & Juliette Senechal
Kids are curated from YouTube according to three age categories:
(1) The very young: 4 years old and under; (2) The little ones: 5-
8 years old; (3) The older ones 9-12 years old. The selection is
made through a combination of algorithmic detection and manual
review [36]. YouTube Kids is “invitation only”, and creators cannot
request to participate. Whenever a video exists on the two platforms,
YouTube proposes a redirection link to YouTube Kids (see Figure 2
in appendix).
In YouTube Kids, advertising is possible, but the total number
of ads delivered is limited. All YouTube Kids Paid Ads must be
pre-approved by YouTube’s policy team before being served in the
YouTube Kids app. Ads have to follow strict creative guidelines,
and many products are prohibited from being advertised, such as
food and beauty products [31]. Advertisers cannot instruct Google
to show their ads on YouTube Kids –the platform itself curates ads
and whitelists them for being shown in YouTube Kids. Moreover,
it is not possible to send interest-based ads, it is forbidden to use
remarking and tracking pixels, and ads are not allowed to redirect
to websites or product purchase paths [31].
Transparency Before being shown an ad, children are presented
with a short intro video explaining that what comes next is an ad.
In addition, the video ad is marked with an "Ad" disclaimer. On
YouTube Kids, there is no equivalent to the “Why you’re seeing
this ad” button; hence, there is no way, to our knowledge, to know
the precise reasons and parameters why an ad has been shown.
3 LEGISLATION ON ADVERTISING TO
CHILDREN
Historically, legislation regarding advertising and children has been
developed for ads on television and not for ads online. However,
more recently, to adapt to the new online advertising ecosystem,
privacy legislations such as the COPPA and online platforms legisla-
tions such as the DSA have started to include provisions regarding
online advertising and children. In this section, we aggregate and
review legislation related to children and advertising in the E.U. and
the U.S. to understand what practices are regulated and how. Note
that there is no single legal text that covers advertising to children,
and the rules are generally spread across various broader legal texts.
Hence, we present next the excerpts that apply to advertising and
children. While we only interpret our findings in the context of the
DSA and the COPPA, this section contains a more comprehensive
set of text related to advertising to children that we hope can serve
as a reference for researchers wanting to learn more about rules
in the space. When possible, we cite the actual text (provided it is
not too long) of the rules to not bias the description with our inter-
pretation. However, to improve understandability, we provide an
overall summary of the topics treated by the rules at the beginning
of each subsection.
3.1 Legislation on advertising on television
Legislation that applies to advertising to children on television im-
poses rules on the content that can be advertised, on the duration of
ads, and on the separation between ads and the television program.
E.U. legislation. In the E.U., some legal texts come from the Eu-
ropean Union, and they have to be implemented by all the Mem-
ber States, and some are set at the national level, and they ap-
ply to only a specific country. At E.U. level, legislation regard-
ing advertising to children on television is contained in the larger
Directive 2010/13/EU of March 10, 2010, on Audiovisual Media
Services Directive amended by the Directive (EU) 2018/1808” [47,
48]. Regarding content, the Article 9 of this directive (that applies
to advertising to children) states that: “(1e) audiovisual commercial
communications for alcoholic beverages shall not be aimed specifi-
cally at minors and shall not encourage immoderate consumption of
such beverages.”, and “(1g) audiovisual commercial communications
shall not cause physical or moral detriment to minors. Therefore they
shall not directly exhort minors to buy or hire a product or service
by exploiting their inexperience or credulity, directly encourage them
to persuade their parents or others to purchase the goods or services
being advertised, exploit the special trust minors place in parents,
teachers or other persons, or unreasonably show minors in dangerous
situations. ”
In addition, Article 20 (2) prohibits advertising breaks on tele-
vision during children’s programs of less than 30 minutes: “ The
transmission of children’s programmes may be interrupted by televi-
sion advertising and/or teleshopping once for each scheduled period
of at least 30 minutes, provided that the scheduled duration of the
programme is greater than 30 minutes. ” Finally, Article 11 (3d) im-
poses a clear separation between the advertised message and the
rest of the broadcasted program: “Programmes containing product
placement shall be appropriately identified at the start and the end of
the programme, and when a programme resumes after an advertising
break, in order to avoid any confusion on the part of the viewer. ” [41].
This directive was transposed in every Member State of the
European Union, with some national adaptations. For example, in
France, the directive was transposed by a decree of 27 March 1992,
amended by a decree of 2 July 2010 [41].
U.S. legislation. The Federal Communication Commission’s (FCC)
rules and regulations on advertising and children are located in
Title 47 of the Code of Federal Regulations (CFR). These regulations
are colloquially referred to as the Children’s Television Act (CTA).
They have been initially proposed in 1990, and have been updated
several times since with the latest update in 2019. The regulation
imposes rules on advertising in broadcast and cable television pro-
gramming targeting children 12 and younger, including limits on
ad time, and prohibiting the airing of advertising for products
related to the program currently airing. 73.670 and 76.225 state
that “No cable operator shall air more than 10.5 minutes of com-
mercial matter per hour during children’s programming on week-
ends, or more than 12 minutes of commercial matter per hour on
weekdays. ”[21, 22]. In addition, rules related to content in gen-
eral, present in 73.3999, also apply to content advertised to chil-
dren. Federal law prohibits obscene, indecent and profane content
from being broadcast on the radio or T.V. [ 20]. Finally, FCC has
several policies that are designed to protect children from con-
fusion that may result from the intermixture of programs and
commercial material in children’s television programming in the
Sponsorship Identification Rules and Embedded Advertising [19].

Marketing to Children Through Online Targeted Advertising: Targeting Mechanisms and Legal Aspects CCS ’23, November 26–30, 2023, Copenhagen, Denmark
3.2 Legislation on advertising online
Regulations on online advertising and children restrict some target-
ing mechanisms for reaching children (namely through profiling)
while they allow others (namely through contextual advertising).
Per our research, regulations on online advertising seem to miss the
precise rules present in television advertising regarding the content
and the duration of ads. In addition, the E.U. legislation imposes
obligations on platforms to assess systemic risk incurred by their
systems that could affect minors and an obligation to mitigate such
risks.
E.U. legislation. At E.U. level, a new Regulation of 19 October
2022, the Digital Services Act contains regulations regarding adver-
tising to children online [46]. The DSA follows the European Com-
mission Communication “European Strategy for a Better Internet
for Children” regarding minors [17, 18]. At a high level, the DSA
forbids advertising to children based on profiling and puts an obli-
gation on online platforms to assess systemic risks that might harm
children’s rights and mental well-being and health. Interpretation
hint: the actual rules are present in “Articles”, while “Recitals” can
provide additional explanations and intentions behind the rules.
Article 28 (2) of the DSA states that “Providers of online plat-
form shall not present advertisements on their interface based
on profiling as defined in Article 4, point (4), of Regulation (EU)
2016/679 using personal data of the recipient of the service when they
are aware with reasonable certainty that the recipient of the ser-
vice is a minor”. In theArticle 4 (4) of the GDPR, “profiling” means
“any form of automated processing of personal data consisting of the
use of personal data to evaluate certain personal aspects relating to
a natural person, in particular to analyse or predict aspects concern-
ing that natural person’s performance at work, economic situation,
health, personal preferences, interests, reliability, behaviour, location
or movements".
The notion of “ reasonable certainty” is a complex concept
that can be interpreted in different ways. Article 28 (3) states that
“compliance” with Article 28 (2) “shall not oblige providers of online
platforms to process additional personal data in order to assess whether
the recipient of the service is a minor”. This paragraph is, itself, open
to several interpretations, which Recital 71 clarifies as follows: “In
accordance with Regulation (EU) 2016/679, notably the principle of
data minimisation as provided for in Article 5(1), point (c), thereof,
this prohibition should not lead the provider of the online platform
to maintain, acquire or process more personal data than it already
has in order to assess if the recipient of the service is a minor. Thus,
this obligation should not incentivize providers of online platforms
to collect the age of the recipient of the service prior to their use ”.
To comply with such rules and to not ask for additional data on
the age of the users, YouTube is asking content creators to label
whether their content is intended for children or not [63, 64].
Furthermore, given the importance of very large online plat-
forms and search engines (VLOPS), in facilitating public debate,
economic transactions, and the dissemination to the public of infor-
mation, opinions, and ideas and in influencing how recipients obtain
and communicate information online, the Section V of Chapter III
of the DSA (Due Diligence Obligations for Very Large Online Plat-
forms and Search Engine) impose specific obligations on the providers
of very large online platforms in addition to the obligations applica-
ble to all online platforms. In particular,Articles 34 and 35 of the DSA
place an obligation on VLOPS to assess four broad categories of
systemic risk, as well as an obligation to mitigate such risks. VLOPS
must therefore be particularly vigilant about these risks, which
involve the impact of their recommendation, moderation, and ad-
vertising systems on the health, safety, and fundamental rights of
consumers, whether minors or adults. The two systemic risks that
relate to advertising and children are described in Recital 81 and
Recital 83:
Recital 81 “concerns the actual or foreseeable impact of the service
on the exercise of fundamental rights, as protected by the Charter,
including but not limited to human dignity, freedom of expression
and of information, including media freedom and pluralism, the right
to private life, data protection, the right to non-discrimination, the
rights of the child and consumer protection. Such risks may arise,
for example, in relation to the design of the algorithmic systems used
by the very large online platform or by the very large online search
engine or the misuse of their service through the submission of abusive
notices or other methods for silencing speech or hampering competi-
tion. When assessing risks to the rights of the child , providers of
very large online platforms and of very large online search engines
should consider for example how easy it is for minors to understand
the design and functioning of the service, as well as how minors can
be exposed through their service to content that may impair minors’
health, physical, mental and moral development. Such risks may arise,
for example, in relation to the design of online interfaces which inten-
tionally or unintentionally exploit the weaknesses and inexperience
of minors or which may cause addictive behavior ”.
Recital 83 identifies another important risk: “ category of risks
stems from similar concerns relating to the design, functioning or
use, including through manipulation, of very large online platforms
and of very large online search engines with an actual or foreseeable
negative effect on the protection of public health, minors and serious
negative consequences to a person’s physical and mental well-being,
or on gender-based violence. Such risks may also stem from coor-
dinated disinformation campaigns related to public health, or from
online interface design that may stimulate behavioural addictions of
recipients of the service ”.
Finally, regarding the content of online ads, we found a broad pro-
vision in theDirective (EU) 2018/1808 of 14 November 2018 amended
by Directive 2010/13/EU (Audiovisual Media Services Directive).
The amended directive states in Article 28b (a) that “Member States
shall ensure that video-sharing platform providers under their ju-
risdiction take appropriate measures to protect minors from
programmes, user-generated videos and audiovisual commercial
communications which may impair their physical, mental or
moral development”. Where the appropriate measures are strict
access control, age verification and parental control (see Appen-
dix A.2 for the description of appropriate measures). Note that, this
article applies to all continent that might be seen by minors on
video-sharing platforms and is not specific to advertising.

CCS ’23, November 26–30, 2023, Copenhagen, Denmark Tinhinane Medjkoune, Oana Goga, & Juliette Senechal
U.S. legislation. The Children’s Online Privacy Protection Rule
(COPPA) [23] has restrictions on advertising to children. The pro-
posed rules are intended to stop the behavioral advertising, retar-
geting, and profiling of children under 13, but not contextual adver-
tising. More precisely, COPPA states that advertisers and content
owners may not collect any personal information (which includes
cookies and other persistent identifiers) from children under 13
years of age without verifiable parental consent (see Appen-
dix A.2 for a definition of verifiable legal consent and personal
infromation). However, COPPA allows operators to collect per-
sonal information only for “support for the internal operations of
the Web site or online service means that those are activities necessary
to (...) authenticate users of, or personalize the content on, the Web
site or online service (...) serve contextual advertising on the Web
site or online service or cap the frequency of advertising (...) so long
as the information collected for these activities is not used or disclosed
to contact a specific individual, including through behavioral adver-
tising, to amass a profile on a specific individual, or for any other
purpose”’.
Senators introduced in January 2022 in front of the US Congress
a proposal for “ Banning Surveillance Advertising Act” [58]. This
text, which is at the proposal stage, intends to prohibit targeted
advertising, under certain conditions, but regardless of the age of
the recipient, whether a minor or an adult.
4 MECHANISMS FOR TARGETING CHILDREN
When advertising, Google does not allow advertisers to choose au-
diences of users under 18. Hence, the advertising interface does not
allow advertisers to target children directly. However, placement-
based advertising can be easily exploited to target children with ads:
an advertiser simply needs to aggregate a list of videos or channels
with content for children and target its ads at these videos. Next, we
evaluate whether such targeting works in practice. We first describe
how one can aggregate a list of children-focused videos. We then
describe how we performed ad experiments to test whether Google
allows placement-based advertising on children-focused videos.
4.1 Curated children-focused videos
We compiled two lists of children-focused videos and one list of
general-audience videos (as control):
Children YTB Kids List –To compile a list of children-focused
videos, we first take advantage of YouTube Kids and, hence, YouTube’s
own characterization of videos as being dedicated to children. For
this, we created an adult account, and we used it to create three
children’s accounts corresponding to the three age groups proposed
by YouTube Kids (under 4, 5 to 8, and 9 to 12). We then manually
browse the different categories of videos recommended when nav-
igating to the broadcasts, music, learning, and discovery tabs in
YouTube Kids and collect the corresponding channels. We collected
22 YouTube Kids channels. For each channel, we then collect the ten
most recent videos from its YouTube Kids channel page.
Children Seed List –We observed that not all children-focused
videos available on YouTube are part of YouTube Kids. To build a
complementary list, we took three channels with a large number of
subscribers: Swan & Néo (5.97 M subscribers), Madame Récré FR
(3.81 M subscribers), and Studio Bubble Tea (1.82 M subscribers),
and did a snowball sample on the “Channels” section. The “Chan-
nels” section contains channels with similar content according to
YouTube or that have been manually added by the channel’s owner.
We added the channels collected (avoiding duplicates) at the end
of our list and browsed this list in FIFO. Our stopping point was to
have 200 YouTube channels in total. We then manually filtered out
channels present on YouTube Kids (one can copy-paste the YouTube
link on YouTube Kids to check if it exists) and channels not mainly
intended for children according to the FTC guidelines [27]. Finally,
we kept a list of 20 children-focused channels, and we collected the
ten most recent videos from their YouTube channel pages.
Adult List–We compiled a list of general-audience channels to
have a point of reference. For this, we created a profile with no
search history or preferences. We collected the channels corre-
sponding to videos recommended on YouTube when logging in
for the first time. We compiled a list of 20 adult-focused channels
(the intersection with the children-focused lists is empty), and we
collected the ten most recent videos from their YouTube channel
pages. The lists we compiled are not representative and are biased
toward videos recommended by YouTube and more popular videos
on the platform. Nevertheless, representativeness is not necessary
if the goal of the ad experiments is just to test whether something
is possible.
4.2 Targeting ad experiments
To check whether Google allows advertisers to target their ads to
children-focused videos, we created seven real-world ad campaigns
in which we instructed Google to place our ads on children-focused
videos. Section 4.3 describes how we chose the content of the ads
to minimize risks for children. As campaign parameters we chose
the “Brand Awareness and Reach” campaign objective, instructed
Google only to show the ad on YouTube (and not on its Display
Network), and disabled the “audience expansion” option. We left
all other parameters on the default value. We launched three ad
campaigns where we only used placement-based targeting (CID 1
to 3 in Table 1) and four ad campaigns combining both placement-
based and interest-based targeting (CID 4 to 7 in Table 1). For each
ad campaign, we chose various combinations of placements: videos
or channels from Children YTB Kids List , Children Seed List,
and Adult List. CID 1 and 5-7 only use children-focused videos
as placement, while CID 2-4 combine adult-focused with children-
focused videos as placement. Our ad experiments were launched
between Sept. and Nov. 2022. All our seven ad campaigns have
been validated by Google and delivered to users. Nevertheless,
this information alone is not enough to prove that Google delivered
our ads on children-focused videos, as the platform could have
potentially not respected our criteria and delivered our ads on
videos that are not on our list.
Luckily, Google provides advertisers with an interface where
they can check statistics about the delivery of their ad campaigns
and allows us to check for each ad campaign the total number of
ad impressions as well as the number of ad impressions on each
video the ad was placed on [32]. Table 1 reports the total number
of impressions as well as impressions on Children YTB Kids List
and Children Seed List videos only. The table shows that all our

Marketing to Children Through Online Targeted Advertising: Targeting Mechanisms and Legal Aspects CCS ’23, November 26–30, 2023, Copenhagen, Denmark
Table 1: Targeting parameters of our ad campaigns and their impressions. * Total impressions (out of which impressions on
videos in Children YTB Kids List ; and in Children Seed List).
CID Placement Interests Location Impressions*
1 3 Children YTB Kids List videos None U.S. 450 (450; 0)
2 4 Adult List videos + 7 Children YTB Kids List videos + 1
Children Seed List video
None Fr. 605 (43; 75)
3 10 Adult List videos + 10 Children YTB Kids List videos + 10
Children Seed List videos
None Fr. 6,124 (1,414; 2)
4 3 Adult List videos + 6 Children YTB Kids List videos + 1
Children Seed List video
News & Politics, Travel, Sports & Fitness Fr. 941 (121; 471)
5 20 Children YTB Kids List channels + 4 Children Seed List
channels
Shoppers, Sports Game Fans U.S. 10,854 (1,657; 9,203)
6 20 Children YTB Kids List videos Shoppers, Food & Dining, Education, Media & Entertainment,
Beauty & Wellness, Banking & Finance
U.S. 4,650 (1,058; 0)
7 20 Children YTB Kids List videos Shoppers, Food & Dining, Education, Media & Entertainment,
Beauty & Wellness, Banking & Finance
E.U.† 2,372 (2,372; 0)
† Belgium, Denmark, Finland, France, Germany, Italy, Netherlands, Poland, Romania, Spain, Sweden.
ad campaigns resulted in our ads being shown on children-focused
videos including videos sourced from YouTube Kids–these videos
are marked by the platform itself as being primarily intended for
children. Hence, this shows that advertisers can target children
with ads on YouTube by asking the platform to place their
ads on children-focused videos .
Placement-based targeting is done independently of the identity
of the connected user and their Google profile. Hence, we per-
formed four experiments where we instructed Google to combine
placement-based with interest-based targeting in order to target
ads both based on the video watched and based on the profile of the
user watching the video. We perform this experiment because both
the DSA and COPPA ban or restrict the use of profiling in advertis-
ing to children. Table 1 (CID 4 to 7) shows the placements and the
interests we used. To check if Google has a different treatment for
videos on YouTube Kids (as the platform knows they are intended
for children), for CID 6 and CID 7, we used as placement only videos
on YouTube Kids. We also checked if Google has different policies
across different countries, maybe due to differences in legislation.
CID 6 was targeted at the U.S., while CID 7 was targeted at 11 coun-
tries in the European Union. All four ad campaigns were validated
and shown to users. Again, this is not enough to prove that Google
is serving ads based on the profiles of users on children-focused
videos, as Google might have ignored the profiling part of our re-
quest. Luckily, Google also provides statistics about the number
of impressions shown to users with particular characteristics. For
example, the statistics provided by Google for CID 4 say it had 393
impressions on users interested in “Travel”, 387 in “Sports & Fitness”
and 161 in “News & Politics”. The statistics provided by Google
indicate that for all four ad campaigns (CID 4 to 7), Google delivered
the ads to only users with the interests we asked for (i.e., the total
number of impressions across placements = the total number of
impressions across interests). Hence, Google allows advertisers
to perform targeting based on profiling when placing their
ads on children-focused videos. Such a combination of targeting
is allowed both in the U.S. and E.U.; it is also allowed on videos
marked by YouTube itself as intended for children.
4.3 Ethics statement
We ran ad experiments on real ad platforms and targeted children-
focused videos with our ads. Hence, our ads have probably been
seen by children. We chose the content of the video ad and the
landing page to limit potentially harmful effects on children. We
first created a short video that records trees while walking in a park
(the video does not capture any visible human face). Second, we
used an already existing children-focused video on YouTube under
a Creative Commons License that allows redistribution (Figure 3, in
the appendix, show a screenshot of our two ads). Finally, the landing
URL of the ad was either the tourism office of the city we lived in or
the YouTube Channel page corresponding to the video we used as an
ad. We set small ad budgets to limit the number of children that see
our ads and stopped the ad campaign as soon as we saw impressions.
We did an informal validation with colleagues (including legal
scholars, behavioral economists, and cognitive scientists), and they
did not express any concern regarding potential harm from our
video ads.
We filed a request with our institute’s DPO (Data Protection
Officer) for the data collection in Section 4.2, and we were exempt
as we do not collect personal information from users in these exper-
iments. The data collection gathered through a browser extension
(Section 5) and the ad experiments to assess risks with online plat-
forms (Section 4.2) were covered by a project-level IRB.
4.4 Implications
Our experiments show that is possible for advertisers to directly
market to children on YouTube through placement-based targeting
on children-focused videos. In light of the texts applicable in the
E.U. and the U.S., it appears that the online targeting of children
by contextual advertising is permitted . Hence, placement-based
advertising is also permitted as it is a form of contextual advertising.
Nevertheless, contextual advertising targeting children online is less
secure than contextual advertising targeting children on television.
Online advertisers can place an ad under a single piece of content
(e.g., a particular cartoon or a particular video clip dedicated to
children), which can make verification of the content of the ad very
difficult in practice, as it will only be seen by children who have
seen that content, with very little possibility of effective verification
of the content of the ad by adults.
In contrast, the online targeting of children by profiling (such as
interest, location, and behavior) is clearly banned in the European
(DSA) and might be restricted in the American (COPPA). In fact,
COPPA restricts the collection of personal information on content
primarily intended to children, however, it is not clear from the
text if it also restricts the use of previously complied user profiles

CCS ’23, November 26–30, 2023, Copenhagen, Denmark Tinhinane Medjkoune, Oana Goga, & Juliette Senechal
(e.g., profiles complied when the users was browsing adult-focused
videos) when serving an ad on a children-focused video. Hence,
it appears from the experiments that there is a need to better dis-
tinguish between cases where targeting is carried out solely on
the basis of context or where targeting is carried out by mixing
contextual placement and profiling. This distinction is necessary to
effectively implement the DSA and COPPA texts protecting children
against advertising based on profiling.
Nevertheless, in 2019, the Federal Trade Commission (FTC) served
YouTube with a $170 million fine for violating COPPA because it
had illegally collected information on children for its personalized
ads. To avoid future fines, YouTube committed to better distinguish
content intended primarily for children by relying on a combination
of self-reports from creators and algorithms. Since then, content
creators have been obligated to label their videos as “Made for Kids”
(or risks $45k fines otherwise). YouTube said they would assume any
viewer of children-focused videos is underage, no personal data collec-
tion will be performed on such content, and no personalized ads will be
sent on such content (as per the COPPA rule) [26, 60, 63, 64]. Hence,
contrary to this declaration, we were able to send personalized ads
on such content.
5 USAGE OF PLACEMENT-BASED TARGETING
This section proposes a measurement methodology to investigate
whether advertisers, in the wild, are exploiting placement-based
targeting to advertise their products to children.
5.1 Data collection methodology
Our methodology is based on a browser extension that can cap-
ture information about the ads shown when a user is watching a
YouTube video. At a high level, the measurement methodology con-
sists in instructing six browser profiles to watch children-focused
videos and collect the ads shown.
Ad capture tool. Each time an ad is shown to the user, the DOM
is updated to add new elements to the HTML code of the video
watched. So, to capture ads, our browser extension simply monitors
the DOM for changes. Our extension works on Chrome and can
capture both video ads–video ads launched at the beginning, middle,
or end of a watched video; and float card ads –ads containing an
image, a GIF, or text showed while watching a video above the nav-
igation bar. When our browser extension detects an ad, it collects
the following information (mainly textual):
• Ad data: The name of the advertiser, the advertiser’s YouTube
channel, the advertiser’s link, the image or GIF in the case of float
ads, and the URL of the ad for video ads.
• Video watched data : We collect the title of the video watched
(the video on which the ad appears), its URL, its description, the
nb. of views, the date the video was published, the corresponding
channel, and the nb. of channel followers.
• YouTube Kids redirection : We collect if YouTube proposes
redirecting the user to YouTube Kids (it means the video is on
YouTube Kids–see Figure 2 in appendix).
• Ad explanation : The browser extension collects data that
appears in the “Why am I seeing this ad?” feature. This feature can
be accessed by clicking on the button i○ at the bottom left of the
ad video. A modal opens and describes to users the reasons the ad
Table 2: Characteristics of our browser profiles.
Profile Details
P1 No Google profile + no search history
P2 No Google profile + no search history
P3 Empty google Profile + no search history and no gender
P4 Empty google Profile + no search history and no gender
P5 Google profile (woman) + browse four sites related to clothes, cats food,
Volkswagen cars and animal’s rights in France
P6 Google profile (man) + browse one site related to plastic surgery
was shown to them. We collect this information by simulating a
click on the button, and thus we recover the response to the request
sent after the click. To close the modal, we simulate another click
outside the modal’s window.
We do not collect information about the profile/identity watching
the video (each user is associated with a unique identifier generated
by the browser extension). This data is sent and stored in our lab
servers through a secure HTTPS connection. The storage server is
protected by a firewall.
Personas. The ads shown when someone watches a video on
YouTube can depend on the browser profile (as determined by the
cookies present in the browser that track sites previously visited)
and the Google profile of the user in case the user is logged in.
Hence, to have a broader view and account for how the browser
profile could influence the results, we created six browsing profiles
with different parameters–see Table 2.
We created: (1) Two browser profiles without a Google profile
associated and no browsing history. (2) Two profiles are associated
with an empty Google profile with no gender specification and no
browsing history (the profiles only have the age set because the
users are obliged to specify the date of birth to create a Google
account). And (3) two profiles are associated with Google accounts
and browsing history. One account has the gender set to female and
the other to male. For the female profile, we visited four sites related
to clothes, cats’ food, Volkswagen cars, and animal rights in France;
for the male profile, we visited one site related to plastic surgery.
For P3-P6, we checked the Google Ads Settings page to investigate
what interests Google has inferred for the different profiles [34]. P3
and P4 have, as expected, no interests. The P5 profile had Fashion
& Trend, Pets, and Auto & Vehicles as interests, and P6 had Body
Care & Fitness as interests. These interests are consistent with the
sites consulted.
Google does not allow children (younger than 18 years old)
to create Google profiles. Our profile choice is motivated by the
possibilities offered by Google for how a child could watch videos
on YouTube: (1) a child can use an incognito browser that is not
connected to any profile; (2) a child could create an account with an
erroneous age; or (3) a child can use the account of one of his/her
parents, who may have already used this account on sites and
applications so that browsing history is already present.
Instrumentation. We conducted our data collection on YouTube
between April 28th 2022 and May 5th 2022. We collected data
simultaneously from the six profiles on two different computers.
We launch the six personas simultaneously by creating six Selenium
sessions. The personas browse the ten most recent videos in each of
the channels in the three lists: Children YTB Kids List, Children
Seed List, and Adult List. Each video was watched from start to

Marketing to Children Through Online Targeted Advertising: Targeting Mechanisms and Legal Aspects CCS ’23, November 26–30, 2023, Copenhagen, Denmark
Table 3: Number of ads received by the different profiles.
Profile No. of Video ads No. of Float ads
P1 239 0
P2 205 0
P3 437 162
P4 396 139
P5 541 393
P6 441 368
ALL 2,259 1,062
finish. With the help of the extension, each ad served is collected
and stored on our servers. Our stopping point is the end of the
entire YouTube channel list–620 videos. Table 3 shows the number
of video and float card ads we collected for each list and each profile.
Across the six profiles, we collected 3,221 ads.
Note on experimental difficulties: The data collection is time-consuming:
(1) we need to watch videos until the end to catch all ads because
ads can appear at random times during the video, and there is no
fixed number of ads that appears during a video. The length of the
videos varies from less than 2 minutes to more than one hour. And
(2) our simulated double-click to recover the information in the
“Why am I seeing this ad?” sometimes triggers a modal that does
not close, interrupting the video’s progress and therefore requiring
human intervention to close the modal and restart the video. This
limits the scale of the experiment. Nevertheless, since this paper
focuses on whether advertisers use placement-based advertising to
target children and not on providing a representative characteriza-
tion of ads shown on children-focused videos, we believe that our
instrumentation with six browser profiles is enough.
5.2 Detection of placement-based targeting
The reasons why an ad is shown on a video depend on the targeting
parameters set by the advertiser and the platforms’ algorithms to
deliver ads. In this paper, we focus on placement-based advertising.
Hence, given a set of ads shown on a video, the challenge is to
distinguish between ads targeted at the video (i.e., placement-based)
and ads that were shown due to other reasons (e.g., interest-based,
re-targeting).
Our first idea was to watch the same video simultaneously, using
multiple browser profiles, and consider only ads present in all pro-
files as placement-based ads. Out of the 668 unique ads we collected
across the six profiles, only two ads were received by all six profiles.
For information, 39 ads were received by four or more profiles, and
128 ads were received by two or more profiles. Nevertheless, this
method sadly suffers from both false positives (the ad appears in all
profiles because the advertiser launched a very big campaign and
it is outbidding the competition) as well as false negatives (an ad
might be placement-based but does not appear in all videos because
of budget constraints and competition). Therefore, this method
cannot provide reliable ground truth.
Luckily, Google provides users explanations for why they re-
ceived a particular ad in the “Why you’re seeing this ad” feature
(see Section 2). Hence, we decided to investigate whether these
explanations are precise enough to help us distinguish between
placement-based ads and the rest. Our Chrome extension was able
to collect the information in the “Why you’re seeing this ad” button
for all the ads we collected. Table 4 shows the different explana-
tions provided by Google. Note that our study was conducted in
French, so the reasons in the table are translated from French and
might have a slightly different syntax in English. We group these
reasons into eight broad targeting categories: P–placement-based
ads; R–Re-targeting ads; T–Theme-based ads; K–Keyword-based; I–
Identity-based; B–Behavioral or interest-based; L–Location-based;
and G-General targeting. The different ad explanations cover the
different targeting types offered by Google, and the explanations
provided are quite precise such as “The topics on the website you
were looking at” or “Estimate of your housing occupancy status by
Google”. More interesting for us, the explanation with EID 1, “The
video you are watching” seems to correspond to placement-based
advertising. Another interesting explanation is EID 27, “Ad person-
alizing is disabled for this account or content. Therefore, this ad is
not personalized based on your data. ” as it clearly states that the
ad is not personalized. This is interesting because Google claims to
not deliver personalized ads on children-focused videos [63, 64].
Validation. Previous works have shown that ad explanations on
Facebook were incomplete and misleading [4]. While it is outside
the scope of this paper to perform a full audit of ad explanations on
YouTube, we validate the correspondence between placement-based
targeting and the “The video you are watching? ad explanation. For
this, we analyze its: (1) sensitivity – the extent to which when an
advertiser uses placement-based targeting, this is the corresponding
ad explanation Google provides users; and its (2) specificity – the
extent to which this ad explanation does NOT appear on ads that
do not use placement-based targeting. For example, if the ad expla-
nation EID 1 also appears on ads that use theme-based targeting,
then it is not specific to placement-based targeting.
We created a Google ad campaign targeting only one specific
video to investigate the sensitivity. Then we instructed the six
browser profiles to watch the video we targeted, collect whether
our ad was shown, and collect the corresponding explanation from
Google. In every instance where we collected our ad, Google pro-
vided the “The video you are watching” (EID 1) ad explanation. We
repeated the experiment in three ad campaigns with other place-
ments and always got EID 1. Hence, as expected, EID 1 is given for
ads that use placement-based targeting.
The specificity is harder to demonstrate as the ad platform pro-
vides numerous targeting parameters to advertisers, and it is hard
to prove that no other combination of targeting parameters results
in an EID 1 explanation. The difficulty comes from a combination of
technical and financial issues: it is hard using a few browser profiles
to catch an ad that was, for example, targeted at users interested in
“Shopping” when being on a limited ad budget, as the likelihood of
our ad being seen by our profiles is very low.
Hence, we tested the specificity with respect to four types of
targeting (theme-based, behavioral-based, demographic-based, and
general-based), which is a subset of all possible targeting strategies,
but covers some of the most used targeting techniques. For this,
we again created four ad campaigns that used the four types of
targeting and tried to collect our ads and check the explanation
provided by Google. For none of the ad campaigns, we collected a
“The video you are watching” explanation, and the ad explanations
provided were coherent with our categorization in Table 4. Hence,

CCS ’23, November 26–30, 2023, Copenhagen, Denmark Tinhinane Medjkoune, Oana Goga, & Juliette Senechal
Table 4: List of the explanations why a user receives an ad.
We group them into eight targeting categories: A–placement-
based ads; R–Re-targeting ads; T–Theme-based ads; K–
Keyword-based; D–Demographic-based; B–Behavioral or
interest-based; L–Location-based; G–General targeting. The
grouping is made based on our intuition and not based on ad
experiments with definite proof.
EID Cat. “Why am I seeing this ad?” explanations
1 P The video you are watching.
2 K Your current search terms.
3 T The topics on the website you were looking at.
4 T Popular products from this advertiser.
5 B Your activity while signed in to Google.
6 B Your estimated interests based on your activity on Google (e.g.
searches) on this device.
7 B Google’s estimate of your interests based on your activity (e.g.
searches) while you were signed in to Google.
8 B Your activity, while you were signed in to Google.
9 B Your activity on this device.
10 D Your gender.
11 D Estimate of your level of education by Google.
12 D The age you added to your Google Account.
13 D Estimate of your housing occupancy status by Google.
14 D Your gender estimated by Google based on your activity on this
device.
15 D Estimation of your parental status by Google.
16 D Your age group.
17 R Your visit to the advertiser’s website or app.
18 R The websites you visited.
19 R Websites you’ve visited.
20 R-L The time of day, the website you were viewing or your general
location (for example country or city).
21 R Your similarities to the groups of people the advertiser is trying to
reach.
22 L Your geographic location (your country or city, for example).
23 L The time of day or your general geographic location (e.g. country
or city).
24 L Google’s estimate of your current approximate location.
25 L Google’s estimate (based on your past activities) of general geogra-
phies you may be interested in.
26 G Time of day.
27 G Ad personalizing is disabled for this account or content.
Therefore, this ad is not personalized based on your data.
Its distribution depends on other factors (such as the time
or your geographical position).
while we cannot prove absolute specificity, we show the specificity
of EID 1 with respect to these four categories of targeting.
One concern we did not manage to test is what explanation
Google provides if an advertiser selects the “audience expansion”
feature when using placement-based targeting. This feature allows
Google to deliver the ad on videos other than the ones initially spec-
ified by the advertiser. If Google provides the EID 1 explanation for
all the ads it delivers as part of this campaign, this could lead to false
positives, as the EID 1 explanation will appear on videos selected
by Google in addition to the videos specified by the advertiser in
its placements.
Limitation: Since we cannot fully prove the specificity of “The video
you are watching” ad explanation, our results should be read as an
upper bound on placement-based targeting.
Note: We conducted our data collection on YouTube rather than
YouTube Kids. The main technical reason behind this is that YouTube
Table 5: Overlap between video ads across different profiles.
P2 P3 P4 P5 P6
P1 19% 6.8% 8.3% 8.60% 14%
P2 2.5% 2.9% 2.8% 3.7%
P3 19% 20.5% 16.7%
P4 16.2% 14.3%
P5 23%
Kids does not offer users the “Why am I seeing this ad?” feature;
hence, we cannot deduct when advertisers use placement-based
advertising. Nevertheless, surveys claim that YouTube is still used
more than YouTube Kids by parents [45]. Hence, it also makes prac-
tical sense to investigate placement-based advertising on YouTube.
5.3 Analysis of ads
This section analyzes the 3,221 ads we collected with the six profiles
when watching the 620 videos in YouTube.
Ad frequency. Table 3 shows the number of video and float ads
we collected with the different profiles. We can see that P1 and P2,
which do not have associated Google profiles, have not received
any float ads and have the lowest number of video ads. For the
other profiles, we can notice that they receive approximately the
same number of ads. Still, the highest number of ads are for browser
profiles associated with Google profiles with browsing history (P5
and P6).
Overlap. Table 5 reports the overlap in video ads between the six
browser profiles. Recall that all six browser profiles are watching the
same videos at relatively the same time. To compute the overlap, we
computed the unique set of video ads for each profile and computed
the intersection between the different profiles. We can see that the
overlap between P1 and P2 is 19% (the two browser profiles are
not associated with Google profiles). In contrast, the intersection
of either P1 or P2 with the rest of the profiles is much lower. The
intersection between the four profiles associated with a Google
profile, with or without browsing history, is between 15% to 23%.
This suggests that the set of ads received by browser profiles not
associated with a Google profile differs from browser profiles with
an associated Google profile.
Placement-based ads. The central question of this section is whether
advertisers employ placement-based targeting on children-focused
videos in the real-world. Table 6 presents the ad explanations corre-
sponding to the ads received by the six browser profiles for videos
on the Children YTB Kids List , the Children Seed List , and
the Adult List. We consider an ad to be placement-based if the
ad explanation is “ The video you are watching ” (i.e., EID 1). We
consider an ad to be non-personalized if the ad explanation is “Ad
personalizing is disabled for this account or content. Therefore, this
ad is not personalized based on your data. Its distribution depends on
other factors (such as the time or your geographical position) ” (i.e.,
EID 27). And other if the ad explanations are one of EID 2 to 26.
The table shows that ads with a placement-based ad expla-
nation account for 5% of ads collected on Children YTB Kids
List; 14% of the ads collected on Children Seed List ; and 23%
of the ads collected on Adult List. Hence, 7% of ads across both

Marketing to Children Through Online Targeted Advertising: Targeting Mechanisms and Legal Aspects CCS ’23, November 26–30, 2023, Copenhagen, Denmark
Table 6: Targeting categories (sourced from ad explanations) for ads received by the six profiles on the different video lists.
Children YTB Kids List Children Seed List Adult List
Profile No. ads Other Placement Non-pers. Other Placement Non-pers. Other Placement Non-pers.
P1 239 36 0 129 26 0 0 48 0 0
P2 205 10 0 52 68 0 0 75 0 0
P3 599 75 27 274 83 39 0 55 46 0
P4 535 114 25 251 46 17 0 55 27 0
P5 934 144 49 443 112 40 0 122 23 0
P6 809 0 0 390 0 0 264 110 45 0
Total 3,321 379 101 1,539 335 96 264 465 141 0
our children-focused lists ( Children YTB Kids List and Chil-
dren Seed List) have placement-based ad explanations, suggesting
that real-world advertisers use placement-based targeting on
children-focused videos . Given the limitations of ad explana-
tions, the biased set of videos we watch, and our made-up browser
profiles, this number should only be seen as evidence that such
targeting occurs in practice without being representative.
Non-personalized ads. Table 6 shows that ads that 76% of ads in
the Children YTB Kids List , 38% of ads in Children Seed List
and 0% of ads in Children Seed List have a non-personalized ad
explanation. At a first sight this makes sense, as YouTube might im-
pose stricter restrictions on videos and channels it had whitelisted
to be part of YouTube Kids than other children-focused videos and
adult-focused videos.
However, what triggered our attention is that while the major-
ity of ads on Children YTB Kids List have a non-personalized
ad explanation, there are some that have a placement-based or
other ad explanation. Hence, we manually checked whether there
is any difference between videos with ads whit non-personalized
explanations and videos with ads with other or placement-based
explanations. We observed two things: (1) Not all videos in Chil-
dren YTB Kids List had a redirection on YouTube to YouTube
Kids as presented in Figure 2). To clarify, while all the videos in
Children YTB Kids List are accessible on YouTube Kids, not all
have the YouTube Kids redirection on YouTube. (2) We observed
that all the ads on videos with a YouTube Kids redirection have a
non-personalized ad explanation. At the same time, none of the
ads in Children YTB Kids List with no YouTube Kids redirec-
tion have a non-personalized ad explanation. This was surprising,
as our experiments in Section 4.2 showed that we could target
videos that appear on YouTube Kids, including the videos YouTube
Kids redirection. Hence, we decided to test the logic behind the
non-personalized ad explanation.
On the correctness of the non-personalized ad explanation. We hy-
pothesized that Google provides a non-personalized ad explanation
for videos with the YouTube Kids redirection, irrespective of the
actual targeting parameters specified by the advertiser and used to
deliver the ad on the video. To test this, we created an ad campaign,
and we set as placement nine videos from Adult List, five videos
from Children Seed List without a YouTube Kids redirection, and
15 videos from Children YTB Kids List with a YouTube Kids redi-
rection. Statistics provided by Google showed that the ad had 466
impressions on Adult List, 41 on Children Seed List, and 372
on Children YTB Kids List .
Table 7: Ad explanations provided by YouTube for our ad
campaign by category of video.
Ad explanation
Adult List
“The video you are watching. Your activity while you were logged in to
Google. Google’s estimate of your current approximate location. Google’s
estimate (based on your past activity) of general geographies you may be
interested in. "
Children Seed List
“The video you are watching. Your activity while you were logged in to
Google. Google’s estimate of your current approximate location. Google’s
estimate (based on your past activity) of general geographies you may be
interested in. "
Children YTB Kids List
“Ad personalizing is disabled for this account or content. Therefore,
this ad is not personalized based on your data. Its distribution depends
on other factors (such as the time or your geographical position). ”
During the experiment, we used one single profile and watched
de various videos used in the placement to collect our ad and the
corresponding ad explanation provided by Google. Table 7 presents
the ad explanations we collected for our ad. We can see that the
ad explanation we received on both the Adult List videos and
Children Seed List videos is consistent with the configuration of
our ad campaign (i.e., placement-based). However, the explanation
we got on Children YTB Kids List indicates that this ad is not
personalized. Hence, for the same ad campaign and browser profile,
Google changed its explanation depending on whether the
video has a YouTube Kids redirection or not . This situation is
misleading and alarming; not only can children be targeted with
ads through placement-based advertising, but the ad explanations
provided on many children-focused videos do not reflect the use of
this targeting technique. Hence, placement-based targeting might
be even more frequent than we estimated on children-focused videos,
as Google does not provide the precise parameters advertisers use to
target their ads on many of the videos we tested.
Finally, the results for P6 are also strange because it has non-
personalized ad explanations for all the ads in the children-focused
videos we tested, while other profiles, such as P3, P4, and P5, do
not. According to Table 5 there is a 15% to 20% overlap between the
ads received by P6 and ads received by P3, P4, or P5. We checked
the common ads, and we observed they have different ad expla-
nations when shown to P6 and when shown to the other profiles.
We believe that Google detected activity consistent with a child
watching videos and changed the ad explanation policy for P6. We
believe that the current ad explanations provided by Google on
children-focused videos are misleading and not “meaningful” as
demanded in Article 26 of the DSA.

CCS ’23, November 26–30, 2023, Copenhagen, Denmark Tinhinane Medjkoune, Oana Goga, & Juliette Senechal
6 LIMITATIONS
Ad explanations correctness One important limitation of our
study is that we rely on ad explanations provided by Google to
detect the corresponding targeting parameters used by advertisers.
As we showed these, explanations are not always an accurate reflec-
tion of the targeting parameters. In particular, because we could not
fully prove specificity, the fraction of ads targeted using placement-
based targeting might be lower if the ad explanation “The video
you are watching?” is also given for other types of targeting. While
we tested specificity with respect to four types of targeting (theme-
based, behavioral-based, demographic-based, and general-based),
proving complete specificity is hard as even if we could manage to
test all the different combinations of targeting parameters offered
by ad platforms (which is financially prohibitive in our case), there
could still be a theoretical chance, there are parameters outside
our control that could trigger this ad explanation. The other prob-
lem comes from the fact that Google did not provide the precise
targeting parameters on the videos we tested that had a YouTube
Kids redirection. Hence, placement-based advertising might even
be higher than reported. Nevertheless, we think that the paper’s
more long-lasting and meaningful contribution is pinpointing that
placement-based targeting can be used to target children and show
that the use of placement-based advertising on children-focused
videos occurs in practice, irrespective of how prevalent this is.
Ad delivery statistics We also rely on statistics provided by Google
to check if our ads were delivered on the videos we asked as place-
ment and if our ads were delivered to audiences with the character-
istics we asked for. We think Google does not have any incentives
to provide inaccurate statistics as this data is key to businesses
deploying ad campaigns on their platform.
Small dataset and representativenessThe videos in our children-
focused lists are biased toward videos coming from channels rec-
ommended by Google, channels that are popular, and videos that
are recent. The evaluation is also done over a small dataset that
uses only six non-representative browser profiles to watch content.
Hence, our results on the prevalence of placement-based advertis-
ing are not representative of the fraction of placement-based ads
children receive when watching videos on YouTube and should
only be seen as evidence that this occurs in practice.
No real data In this study, we did not use data collected from actual
children. Such data collection would be much harder to get, as we
would need to convince parents to install our tool. In addition, the
data collection would pose many more ethical and legal issues. We
leave the collection and analysis of such data for future works.
Targeting mechanismsThere might be other ways, besides placement-
based targeting, to reach children on YouTube, such as keyword-
based or theme-based targeting, that we did not investigate. We,
again, leave this for future work.
7 RELATED WORKS
There is a large body of work on advertising and children. Many
of the seminal studies have been done by child developmental
psychologists and have focused on ads on television. Next, we
present some works that look at a child’s understanding, perception,
and effect of ads.
In 1982, in the context of television, Stephen, Levin, and Petrella
found that children as young as three years old could distinguish
between TV programs and advertisements. Still, they had no un-
derstanding or awareness of advertisers’ motivations and sales
intentions [56]. In 1992, Bijmolt et al. [6] further investigated the
question and analyzed whether gender, age, and parental influence
have an influence on whether children can distinguish between
advertising content and other content, as well as understand its
commercial intent. For this, they conducted verbal and non-verbal
measurements on children between five and eight years old. This
paper shows that, according to non-verbal measures, most chil-
dren can distinguish commercials from programs and have some
insight into advertising intent. Whereas verbal measures are not as
conclusive, it shows that the percentage of children who show un-
derstanding of TV advertising is substantially lower. For the effect
of age on understanding the ad, the study shows that the older the
child is, the better they understand the ads. However, the effect of
gender and parent-child interaction is relatively small. Other works
such as [43] have shown that children tend to misunderstand the
message of ads and focus more on the negative side of the message
than the positive side. However, this work has also emphasized the
potential positive effect of ads as children can be better informed
on many subjects. For example, an advertisement for toothpaste
can make them aware of problems with their teeth if one does not
brush their teeth regularly. Related to this, a children’s psychology
study claimed that young children do not realize that a message
(of an ad) can only present positive information while retaining
negative information to manipulate the mental state of people [15].
The study analyzed the development of self-promotion in 6- to
10-year-old children. Children were asked to submit a description
of themselves to be chosen for a fictional team. Younger children
included both negative and positive information. In comparison,
older children were better at self-promotion and included only pos-
itive descriptions. Hence, older children can understand that ads
only present positive information, while younger children do not.
A large body of research and reports have specifically focused on
the negative effects of food advertising on children [7, 24, 25, 38–
40, 49, 57]. According to all these studies, it is clear that we need to
take measures to protect children from possible manipulation and
harm from advertisers.
A survey by Raju et al. [51] said that targeting children has been
part of the corporate business since the appearance of ads. Among
the reasons that push a company to target a child: is the size of
the business; there were 14 million children/teenagers between 0
and 17 years old in France in 2018, according to INSEE. The second
reason would be the purchasing power of children who receive
more and more money nowadays; their consumption is mainly
focused on snacks and sweets, followed by toys and games. One of
the other most important reasons remains the power of persuasion
that a child can have on their parents; a child actively contributes
to the purchasing choices in the family, from breakfast cereals to
the color of the car to buy. In addition, the children of today are
the adults of tomorrow and those who will be able to spend their
own money. They also discussed that the content of advertisements
could influence a child’s consumption, especially when it is about
food. Among other points, they concluded that advertisements

Marketing to Children Through Online Targeted Advertising: Targeting Mechanisms and Legal Aspects CCS ’23, November 26–30, 2023, Copenhagen, Denmark
targeting adults could influence children’s vision of the world of
adults, their preferences, and choices when they grow up.
A more recent body of work has studied online advertising and
children [5, 8, 9, 14, 44, 59]. A recent (2020) report from Common
Sense [13] analyzed what videos children are watching on Youtube
and what is being advertised to children. To gather children view-
ing data, they asked parents to participate in a study and provide
the URLs their children viewed by copying and pasting a list from
the browsing history of YouTube [12]. They coded more than 1600
videos afterward according to the topic and analyzed the ads on
these videos. They found that about 20% of the videos contained
age-inappropriate ads. Other works have looked at the frequency
and duration of advertising on popular children-focused channels
on YouTube [62]. Jenny Radesky encourages pediatricians to discuss
with parents and children the dangers of advertising and explain
children’s cognitive capabilities when faced with ads [50]. Finally,
three other works have looked at mobile applications used by chil-
dren: one study provides a content analysis of advertising [ 42];
a second study looked at data collection practices [ 65], and a fi-
nal study looked at the compliance of mobile applications with
COPPA [52]. While many studies are emerging in recent years
around online advertising [1–4, 16, 53, 54], to our knowledge, no
study has investigated how advertisers can target children with ads
on video streaming platforms and analyze the available targeting
techniques from the perspective of current and future laws.
8 CONCLUSION
This paper investigates the mechanisms through which advertisers
can target their ads to children on YouTube and whether real-world
advertisers are actually employing such mechanisms. Our experi-
mental methodology showed that advertisers could target children
through placement-based targeting. This targeting technique allows
advertisers to specify the videos on which they want their ads to
be shown. Our measurement methodology provides evidence that
supports that real-world advertisers employ these techniques to
target children with ads. We also discovered that placement-based
advertising can be combined with targeting based on user profiling.
We performed a legal analysis of the different texts regulating
children’s advertising in the E.U. and the U.S. According to COPPA
and DSA, placement-based advertising on children-focused videos
is not forbidden; however, targeting children based on user profiling
is restricted (in the case of COPPA) and forbidden (in the case of
DSA). The DSA, which was published in October 2022, is supposed
to come into force gradually, and platforms have until 2024 to
comply. As many countries are updating their legislation to protect
children from online harm, we hope our study raises awareness of
the possible targeting mechanisms that advertisers can exploit to
target children and allows lawmakers to refine the legislation.
Given the fact that targeting children is permitted through con-
textual advertising and that ad platforms allow advertisers to place
an ad under a single piece of content specifically targeted at chil-
dren (e.g., a particular cartoon or a particular video clip dedicated
to children), this can make verification of the content of the ad-
vertisement very difficult in practice, as it will only be seen by
children who have seen that content, with very little possibility of
adequate verification of the content of the ad by adults. Therefore,
we strongly believe that we need transparency mechanisms that
allow researchers and the civil society to scrutinize these ads. For
example, ad platforms could provide ad libraries for ads shown on
children-focused videos as they do for political ads.
Google has set up a streaming platform dedicated to children,
YouTube Kids, with increased ad and content restrictions to protect
children. This is a very positive initiative. However, surveys are
showing that YouTube might still be more used by parents; hence,
we encourage Google to adopt the same restrictions on the main
platform YouTube for children-focused videos and have efficient
algorithms to detect children-focused videos that are not labeled as
such by content creators.
9 ACKNOWLEDGEMENTS
We thank the anonymous reviewers for their helpful comments.
This research was supported in part by the French National Re-
search Agency (ANR) through the ANR-17-CE23-0014, ANR-21-
CE23-0031-02, by the MIAI@Grenoble Alpes ANR-19-P3IA-0003
and by the EU 101041223, and 101021377 grants.
REFERENCES
[1] Muhammad Ali, Piotr Sapiezynski, Miranda Bogen, Aleksandra Korolova, Alan
Mislove, and Aaron Rieke. 2019. Discrimination through Optimization: How
Facebook’s Ad Delivery Can Lead to Biased Outcomes. In ACM Conference on
Computer Supported Cooperative Work (CSCW) 2019 .
[2] Muhammad Ali, Piotr Sapiezynski, Aleksandra Korolova, Alan Mislove, and
Aaron Rieke. 2021. Ad Delivery Algorithms: The Hidden Arbiters of Political
Messaging. In ACM International Conference on Web Search and Data Mining
(WSDM) 2021.
[3] Athanasios Andreou, Márcio Silva, Fabrício Benevenuto, Oana Goga, Patrick
Loiseau, and Alan Mislove. 2019. Measuring the Facebook Advertising Ecosystem.
In Network and Distributed System Security Symposium (NDSS) 2019 .
[4] Athanasios Andreou, Giridhari Venkatadri, Oana Goga, Krishna Gummadi,
Patrick Loiseau, and Alan Mislove. 2018. Investigating ad transparency mecha-
nisms in social media: A case study of Facebook’s explanations. In Network and
Distributed System Security Symposium (NDSS) 2018 .
[5] Michael J. Austin and Mary Lynn Reed. 1999. Targeting children online: Internet
advertising ethics issues. Journal of Consumer Marketing (1999).
[6] Tammo Bijmolt, Wilma Claassen, and Britta Brus. 1998. Children’s Understanding
of TV Advertising: Effects of Age, Gender, and Parental Influence. Journal of
Consumer Policy (1998).
[7] Emma Jane Boyland and Rosa Whalen. 2015. Food advertising to children and its
effects on diet: review of recent prevalence and impact data. Pediatric Diabetes
(2015).
[8] Xiaomei Cai and Xiaoquan Zhao. 2010. Click here, Kids! Journal of Children and
Media (2010).
[9] Xiaomei Cai and Xiaoquan Zhao. 2013. Online advertising on popular children’s
websites: Structural features and privacy issues. Computers in Human Behavior
(2013).
[10] Pew Research Center. 2023. Many Turn to YouTube for Children’s Content, News,
How-To Lessons. https://www.pewresearch.org/internet/2018/11/07/many-turn-
to-youtube-for-childrens-content-news-how-to-lessons/
[11] Helen Clark, Awa Coll-Seck, Anshu Banerjee, Stefan Peterson, Sarah Dalglish,
Shanthi Ameratunga, Dina Balabanova, Maharaj Bhan, Zulfiqar Bhutta, John
Borrazzo, Mariam Claeson, Tanya Doherty, Fadi El-Jardali, Asha George, Angela
Gichaga, Lu Gram, David Hipgrave, Aku Kwamie, Qingyue Meng, and Anthony
Costello. 2020. A future for the world’s children? A WHO–UNICEF–Lancet
Commission. The Lancet (2020).
[12] Common Sense. 2020. The Common Sense Census: Media Use by Kids Age Zero to
Eight, 2020. https://www.commonsensemedia.org/sites/default/files/research/
report/2020_zero_to_eight_census_final_web.pdf
[13] Common Sense. 2020. Young Kids and YouTube: How Ads, Toys, and Games
Dominate Viewing . https://www.commonsensemedia.org/sites/default/files/
research/report/2020_youngkidsyoutube-report_final-release_forweb_1.pdf
[14] Lara Spiteri Cornish. 2014. Mum, can I play on the internet?International Journal
of Advertising (2014).
[15] Robin Banerjee Dawn Watling. 2007. Children’s Differentiation Between Ingrati-
ation and Self-Promotion. Social Development (2007).
[16] Laura Edelson, Tobias Lauinger, and Damon McCoy. 2020. A Security Analysis of
the Facebook Ad Library. In IEEE Symposium on Security and Privacy (S&P) 2020 .

CCS ’23, November 26–30, 2023, Copenhagen, Denmark Tinhinane Medjkoune, Oana Goga, & Juliette Senechal
[17] European Commission. 2022. COMMUNICATION FROM THE COMMISSION TO
THE EUROPEAN PARLIAMENT, THE COUNCIL, THE EUROPEAN ECONOMIC
AND SOCIAL COMMITTEE AND THE COMMITTEE OF THE REGIONS A Digital
Decade for children and youth: the new European strategy for a better internet for
kids (BIK+). https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=COM:2022:
212:FIN
[18] European Commission. 2022. European Strategy for a Better Internet for Children .
https://digital-strategy.ec.europa.eu/en/policies/strategy-better-internet-kids
[19] FCC. 2023. Sponsorship Identification Rules and Embedded Advertising, MB Docket
No. 08-90, Notice of Inquiry and Notice of Proposed Rulemaking, 23 FCC Rcd
10682, 10687, para. 6 (2008); 1991 Memorandum Opinion and Order, 6 FCC Rcd
at 5094-99, paras. 3-34; 1991 Report and Order, 6 FCC Rcd at 2111-13, paras. 2-
1. FCC. https://www.fcc.gov/document/sponsorship-identification-rules-and-
embedded-advertising-0
[20] FCC. 2023. Title 47 of the Code of Federal Regulations 73.3999 Enforcement of
18 U.S.C. 1464 (restrictions on the transmission of obscene and indecent material) .
FCC. https://www.ecfr.gov/current/title-47/chapter-I/subchapter-C/part-73/
subpart-H/section-73.3999
[21] FCC. 2023. Title 47 of the Code of Federal Regulations 73.670 Commercial limits
in children’s programs . FCC. https://www.ecfr.gov/current/title-47/chapter-
I/subchapter-C/part-73/subpart-E/section-73.670
[22] FCC. 2023. Title 47 of the Code of Federal Regulations 76.225 Commercial limits
in children’s programs . FCC. https://www.ecfr.gov/current/title-47/chapter-
I/subchapter-C/part-76/subpart-G/section-76.225
[23] Federal Trade Commission. 2017. Children’s Online Privacy Protection Rule; Final
Rule. https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-312
[24] Frans Folkvord, Doeschka J Anschütz, Emma Boyland, Bridget Kelly, and Moniek
Buijzen. 2016. Food advertising and eating behavior in children. Current Opinion
in Behavioral Sciences (2016). Diet, behavior and brain function.
[25] Sara C. Folta, Jeanne P. Goldberg, Christina Economos, Rick Bell, and Rachel
Meltzer. 2006. Food Advertising Targeted at School-Age Children: A Content
Analysis. Journal of Nutrition Education and Behavior (2006).
[26] FTC. 2019. Case 1:19-cv-02642: FTC against Google and YouTube on COPPA settle-
ment. https://www.ftc.gov/system/files/documents/cases/172_3083_youtube_
coppa_consent_order.pdf
[27] FTC. 2019. YouTube channel owners: Is your content directed to chil-
dren? https://www.ftc.gov/business-guidance/blog/2019/11/youtube-channel-
owners-your-content-directed-children
[28] Google. 2022. Advertising on YouTube Kids . https://support.google.com/
youtubekids/answer/6130541?hl=fr
[29] Google. 2023. About audience expansion . https://support.google.com/google-
ads/answer/9496986?hl=en
[30] Google. 2023. Add age targeting to ad groups. https://support.google.com/google-
ads/editor/answer/47640?hl=en
[31] Google. 2023. Advertising on YouTube Kids. https://support.google.com/youtube/
answer/6168681?hl=en
[32] Google. 2023. Google Ads. https://ads.google.com/
[33] Google. 2023. Google Ads Help: Targeting your ads . https://support.google.com/
google-ads/answer/1704368?hl=en
[34] Google. 2023. Google Ads Settings. https://adssettings.google.com/
[35] Google. 2023. My Ad Center. https://support.google.com/My-Ad-Center-Help/
?hl=en#topic=11616697
[36] Google. 2023. Videos in YouTube Kids. https://support.google.com/youtubekids/
answer/6172307?hl=en
[37] Google. 2023. YouTube Kids. https://www.youtube.com/intl/en_us/kids/
[38] Bridget Kelly, Jason C.G. Halford, Emma J. Boyland, Kathy Chapman, Inmacu-
lada Bautista-Castaño, Christina Berg, Margherita Caroli, Brian Cook, Janine G.
Coutinho, Tobias Effertz, Evangelia Grammatikaki, Kathleen Keller, Raymond
Leung, Yannis Manios, Renata Monteiro, Claire Pedley, Hillevi Prell, Kim Raine,
Elisabetta Recine, Lluis Serra-Majem, Sonia Singh, and Carolyn Summerbell. 2010.
Television Food Advertising to Children: A Global Perspective. American Journal
of Public Health (2010).
[39] Bridget Kelly, Ben Smith, Lesley King, Victoria Flood, and Adrian Bauman. 2007.
Television food advertising to children: the extent and nature of exposure. Public
Health Nutrition 10 (2007).
[40] Matthew A. Lapierre, Frances Fleming-Milici, Esther Rozendaal, Anna R. McAl-
ister, and Jessica Castonguay. 2017. The Effect of Advertising on Children and
Adolescents. Pediatrics (2017).
[41] Legifrance. 1992. Décret no. 92-280 du 27 mars 1992 pris pour l’application des
articles 27 et 33 de la loi no. 86-1067 du 30 septembre 1986 et fixant les principes
généraux définissant les obligations des éditeurs de services en matière de pub-
licité, de parrainage et de télé-achat. https://www.legifrance.gouv.fr/loda/id/
JORFTEXT000000346165/
[42] Marisa Meyer, Victoria Adkins, Nalingna Yuan, Heidi M. Weeks, Yung-Ju Chang,
and Jenny S. Radesky. 2019. Advertising in Young Children’s Apps: A Content
Analysis. Journal of Developmental & Behavioral Pediatrics (2019).
[43] Sudip Basu Mithun Das, Sisir Ghorai. 2018. A Study on Effects of TV Advertising
on Children. International Journal of Research and Scientific Innovation (IJRSI)
(2018).
[44] Elizabeth S. Moore. 2004. Children and the Changing World of Advertising.
Journal of Business Ethics (2004). https://doi.org/10.1023/b:busi.0000035907.
66617.f5
[45] NScreenMedia. 2020. YouTube used by more children than YouTube Kids. https:
//nscreenmedia.com/more-kids-youtube-versus-youtube-kids
[46] Official Journal of the European Union. 2022. Regulation (EU) 2022/2065 of the
European Parliament and of the Council of 19 October 2022 on a Single Mar-
ket For Digital Services and amending Directive 2000/31/EC (Digital Services
Act - DSA). https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:
32022R2065&from=EN
[47] European Parliament and Council. 2010. DIRECTIVE 2010/13/EU OF THE EU-
ROPEAN PARLIAMENT AND OF THE COUNCIL of 10 March 2010 on the co-
ordination of certain provisions laid down by law, regulation or administra-
tive action in Member States concerning the provision of audiovisual media ser-
vices (Audiovisual Media Services Directive) . https://eur-lex.europa.eu/legal-
content/EN/TXT/HTML/?uri=CELEX:32010L0013
[48] European Parliament and Council. 2018. DIRECTIVE (EU) 2018/1808 OF THE
EUROPEAN PARLIAMENT AND OF THE COUNCIL of 14 November 2018 amending
Directive 2010/13/EU on the coordination of certain provisions laid down by law,
regulation or administrative action in Member States concerning the provision
of audiovisual media services (Audiovisual Media Services Directive) in view of
changing market realities . https://eur-lex.europa.eu/legal-content/EN/TXT/
HTML/?uri=CELEX:32018L1808&qid=1689960710955#d1e1811-69-1
[49] Jenny Radesky, Yolanda (Linda) Reid Chassiakos, Nusheen Ameenuddin, Dipesh
Navsaria, and COUNCIL ON COMMUNICATION AND MEDIA. 2020. Digital
Advertising to Children. Pediatrics (2020).
[50] Jenny Radesky, Yolanda Reid-Chassiakos, Nusheen Ameenuddin, and Dipesh
Navsaria. 2020. Digital Advertising to Children. Pediatrics (2020).
[51] P. S. Raju and Subhash C. Lonial. 1990. Advertising to Children: Findings and
Implications. Current Issues and Research in Advertising (1990).
[52] Irwin Reyes, Primal Wijesekera, Joel Reardon, Amit Elazari, Abbas Razaghpanah,
Narseo Vallina-Rodriguez, and Serge Egelman. 2018. Won’t Somebody Think of
the Children? Examining COPPA Compliance at Scale. Proceedings on Privacy
Enhancing Technologies (PETS) (2018).
[53] Filipe N. Ribeiro, Koustuv Saha, Mahmoudreza Babaei, Lucas Henrique, Johnnatan
Messias, Oana Goga, Fabrício Benevenuto, Krishna P. Gummadi, and Elissa M.
Redmiles. 2019. On Microtargeting Socially Divisive Ads: A Case Study of Russia-
Linked Ad Campaigns on Facebook. In FAT* 2019.
[54] Márcio Silva, Lucas Santos de Oliveira, Athanasios Andreou, Pedro Olmo Vaz de
Melo, Oana Goga, and Fabrício Benevenuto. 2020. Facebook Ads Monitor: An In-
dependent Auditing System for Political Ads on Facebook. InThe Web Conference
(WWW) 2020.
[55] Statista. 2023. Websites and mobile apps used to watch video content online by
children in the United Kingdom (UK) as of January 2021 . https://www.statista.
com/statistics/1251996/platforms-online-videos-uk-children/
[56] Thomas V. Petros Stephen R. Levin and Florence W. Petrella. 1982. Preschoolers’
Awareness of Television Advertising. Child Development (1982).
[57] Mary Story and Simone French. 2004. Food Advertising and Marketing Directed
at Children and Adolescents in the US. The international journal of behavioral
nutrition and physical activity (2004).
[58] U.S. 117TH CONGRESS. 2022. Banning Surveillance Advertising Act . https:
//www.congress.gov/117/bills/s3520/BILLS-117s3520is.pdf
[59] Eva A. van Reijmersdal, Esther Rozendaal, Nadia Smink, Guda van Noort, and
Moniek Buijzen. 2017. Processes and effects of targeted online advertising among
children. International Journal of Advertising (2017).
[60] Washingtonpost. 2020. YouTube overhauls advertising, data collection on kids
content. https://www.washingtonpost.com/technology/2020/01/06/youtube-
overhauls-advertising-data-collection-kids-content/
[61] Brian Wilcox, Dale Kunkel, Joanne Cantor, Peter Dowrick, Susan Linn, and
Edward Palmer. 2004. Report of the APA Task Force on Advertising and Chil-
dren. Section: Psychological issues in the increasing commercialization of childhood
(2004).
[62] Samantha L. Yeo, Alexandria Schaller, Michael B. Robb, and Jenny S. Radesky. 2021.
Frequency and Duration of Advertising on Popular Child-Directed Channels on
a Video-Sharing Platform. JAMA Network Open (2021).
[63] YouTube. 2020. COPPA and YouTube: Answering Your Top QuestionsA . https:
//www.youtube.com/watch?v=KdIlQ9kq4F4
[64] YouTube. 2020. Important Update for All Creators: Complying with COPPA . https:
//www.youtube.com/watch?v=-JzXiSkoFKw
[65] Fangwei Zhao, Serge Egelman, Heidi Weeks, Niko Kaciroti, Alison Miller, and
Jenny Radesky. 2020. Data Collection Practices of Mobile Applications Played by
Preschool-Aged Children. JAMA Pediatrics (2020).

Marketing to Children Through Online Targeted Advertising: Targeting Mechanisms and Legal Aspects CCS ’23, November 26–30, 2023, Copenhagen, Denmark
A APPENDIX
A.1 Screenshots
Figure 2: Redirection from YouTube to YouTube Kids.
Figure 3: Screenshot of our two ads.
A.2 Additional legal excerpts
This section provides more details on the meaning and definition of
precise words used in different legislations we discuss in Section 3.
A.2.1 Additional provisions in the DSA. The Article 28 of the DSA
is without prejudice to Union law on protection of personal data.
In particular, Article 8 of the GDPR states, concerning conditions
applicable to child’s consent in relation to information society ser-
vices, that, “where the criteria for making data processing lawful is
consent (6.1.a of the GDPR) (...) the processing of the personal data of
a child shall be lawful where the child is at least 16 years old. Where
the child is below the age of 16 years, such processing shall be lawful
only if and to the extent that consent is given or authorised by the
holder of parental responsibility over the child. Member States may
provide by law for a lower age for those purposes provided that
such lower age is not below 13 years.
To ensure effective implementation of these due diligence obliga-
tions by platforms, the DSA defines a set of administrative sanctions
and monitoring measures that will be implemented by the Euro-
pean Commission in relation to VLOPS. In Article 54 supplements
this by the possibility for a recipient of services who suffers damage
as a result of the violation of a due diligence obligation to obtain
compensation for his loss in: “ Recipients of the service shall have
the right to seek, in accordance with Union and national law, com-
pensation from providers of intermediary services, in respect of any
damage or loss suffered due to an infringement by those providers
of their obligations under this Regulation ”. This solution is a major
novelty. It is important to specify that liability will be triggered
by the occurrence of a systemic risk, for example concerning the
mental health of a child.
Figure 4: Example of ad explanation provided in “Why you’re
seeing this ad”.
A.2.2 Additional provisions in the Directive (EU) 2018/1808 of 14
November 2018. Article 28b (3) states that “appropriate measures
shall be determined in light of the nature of the content in question,
the harm it may cause, the characteristics of the category of persons
to be protected as well as the rights and legitimate interests at stake,
including those of the video-sharing platform providers and the users
having created or uploaded the content as well as the general public
interest (...). For the purposes of the protection of minors (...) the
most harmful content shall be subject to the strictest access control
measures. Those measures shall consist of, as appropriate : (...) (f)
establishing and operating age verification systems for users of
video-sharing platforms with respect to content which may impair the
physical, mental or moral development of minors; (...) (g) providing for
parental control systems that are under the control of the end-user
with respect to content which may impair the physical, mental or
moral development of minors (...). ”
A.2.3 Relevant nomenclature in the COPPA. Verifiable parental
consent means “any reasonable effort (taking into consideration
available technology), including a request for authorization for future
collection, use, and disclosure described in the notice, to ensure that a
parent of a child receives notice of the operator’s personal information
collection, use, and disclosure practices, and authorizes the collection,
use, and disclosure, as applicable, of personal information and the
subsequent use of that information before that information is collected
from that child. ”
Personal information means “individually identifiable infor-
mation about an individual collected online, including: (1) A first
and last name; (2) A home or other physical address including street
name and name of a city or town; (3) Online contact information as
defined in this section; (4) A screen or user name where it functions
in the same manner as online contact information, as defined in this
section; (5) A telephone number; (6) A Social Security number; (7) A
persistent identifier that can be used to recognize a user over time and
across different Web sites or online services. Such persistent identifier

CCS ’23, November 26–30, 2023, Copenhagen, Denmark Tinhinane Medjkoune, Oana Goga, & Juliette Senechal
includes, but is not limited to, a customer number held in a cookie, an
Internet Protocol (IP) address, a processor or device serial number, or
unique device identifier; (8) A photograph, video, or audio file where
such file contains a child’s image or voice; (9) Geolocation information
sufficient to identify street name and name of a city or town; or (10)
Information concerning the child or the parents of that child that the
operator collects online from the child and combines with an identifier
described in this definition.”
