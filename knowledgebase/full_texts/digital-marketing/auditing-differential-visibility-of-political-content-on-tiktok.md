---
title: Auditing Differential Visibility of Political Content on TikTok
url: https://arxiv.org/abs/2607.17356
category: digital-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Hazem Ibrahim
- Tewoflos Girmay
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.17356
pages: 14
chars: 72500
fetched_at: '2026-11-08T13:20:36+00:00'
kb_version: 1
---

# Auditing Differential Visibility of Political Content on TikTok

Auditing Differential Visibility of Political Content on TikTok
Hazem Ibrahim1, Tewoflos Girmay1
1New York University Abu Dhabi, UAE
hazem.ibrahim@nyu.edu
Abstract
Allegations that TikTok shadow bans political content shape
what creators post, what advertisers fund, and how regulators
act, yet they are hard to adjudicate because platforms do not
disclose how content is ranked. We test the claim with a dense
hourly panel of556,946follower-normalized view observa-
tions across2,753videos from67accounts curated into pro
and anti sides of three contested topics (U.S. immigration en-
forcement, Trump coverage, and Israel/Palestine). On-topic
videos are identified by a multi-step classifier, and stance
is taken from each account’s curated side. The conventional
analysis appears to answer yes. Pooling the hourly snapshots,
the topic-conditional reach gap reachesp <10 −140. Ana-
lyzed at the account level, the independent unit at which we
sample accounts and assign stance, the gap disappears. Every
account-level reach contrast is null after correction (BH-FDR
q≈0.9), with near-zero effect sizes. We find no evidence
of moderate-to-large reach suppression on any topic. The
null is informative. Account-level confidence intervals and a
power analysis rule out such effects. As a design check, the
same framework detects a clear asymmetry on a different out-
come. Oppositional content (anti-Trump, pro-Palestine) earns
more engagement per view rather than less reach (Cliff’s
δ=−0.51and−0.64;q <0.03). Higher engagement per
view does not by itself rule out suppression, but it shows that
the design can detect effects of this magnitude when they ex-
ist. The apparent reach gap is an artifact of two factors. The
first is pseudoreplication, which counts tens of thousands of
autocorrelated video-hours as independent observations; the
second is confounding, since the side that looks suppressed
is larger and, in the case of the Israel/Palestine topic, posts
mostly in Arabic. In this corpus, what is taken for a shadow
ban is better explained by a more engaged audience than by a
suppressed one. We close with what a credible visibility audit
requires.
1 Introduction
On creator forums the same accusation recurs, that the
platform quietly throttles a user’s reach because of what
they post. On TikTok the charge attaches especially to
political content, where users, journalists, and advocacy
groups allege that one side of a contested issue is sup-
pressed (Savolainen 2022; Cotter 2023; Nicholas 2022).
These beliefs have concrete effects. They change what peo-
ple post, drive advertiser and platform policy, and feed narra-
tives of political censorship. Platforms do not disclose rank-
ing, so the claim is argued from the outside by comparison,
at every level of formality. Creators read a drop in their own
view counts against their usual numbers as proof (Nicholas
2022; Delmonaco et al. 2024), advocacy reports compare
pooled hashtag totals across sides and platforms or com-
pile user-reported takedowns (Network Contagion Research
Institute 2023; Human Rights Watch 2023), and published
audits formalize the same design, pooling posts from the ac-
counts on each side and reporting the gaps that reach sig-
nificance (Yarchi and Boxman-Shabtai 2025). What almost
none of these comparisons fix is the unit of independent ob-
servation, and that choice, we show, decides the answer.
The measurement problem has consequences beyond re-
search. Allegations of partisan suppression now feed con-
gressional hearings, ad-spend decisions, and a fast-moving
regulatory agenda that increasingly turns on independent
audits of platform behavior (Nicholas 2022; Metaxa et al.
2021). When a headline is manufactured by an analysis
choice rather than a platform action, it misdirects all three.
Getting the method right is therefore part of the finding, and
it is why we treat the gap between a significant-looking re-
sult and a defensible one as a result in its own right.
Here, we ask whether TikTok shadow bans political con-
tent, quietly suppressing one side of a contested issue be-
cause of the stance that content takes. To answer it, we
tracked2,753videos from67curated political accounts
across three contested topics, recording reach and engage-
ment every hour, labeling on-topic videos with a human-
validated ensemble LLM classifier, and taking each video’s
stance from its account’s curated side. This process yielded
556,946hourly observations, a dense panel with a median
of99observations per video. We hypothesized that visibil-
ity might differ by stance, both because shadow-ban dis-
course predicts such a gap and because TikTok’s recom-
mender allegedly favored Republican-aligned content dur-
ing the 2024 U.S. elections (Ibrahim et al. 2026). Running
the literature’s standard pooled analysis on our own data, the
topic-conditional reach asymmetry appears atp <10 −140,
comfortably surviving a multiple-testing correction. How-
ever, this detection does not survive scrutiny. Analyzed at
the account level, the gap disappears. No topic shows a sig-
nificant difference in reach, and the effect sizes are essen-
tially zero. The design has the power to detect a reach gap.
At the same sample size, the same test finds a clear differ-
arXiv:2607.17356v1  [cs.SI]  19 Jul 2026

ence inengagement, with oppositional content earning more
reactions per view, a direction inconsistent with a visibility
penalty.
The two analyses disagree by more than a hundred or-
ders of magnitude on identical data, and explaining the dis-
agreement is the methodological contribution of the paper.
The pooledp <10 −140 is manufactured by counting tens of
thousands of autocorrelated hourly snapshots as independent
observations, a textbook pseudoreplication, and the resid-
ual gap that remains is explained by account size and con-
tent language rather than stance. The pattern has a precedent
in the account-level reanalysis that overturned the YouTube
radicalization claim (Hosseinmardi et al. 2021).
Three contributions follow. First, we provide a dense,
classifier-labeled TikTok audit of differential visibility on
three contested political topics, and a clean account-level
result ofno evidence of moderate-to-large reach suppres-
sion, accompanied by confidence intervals and a power anal-
ysis that make the null informative and quantified (Sec-
tions 3 and 4). Second, we identify the one robust signal in
the data, anengagementasymmetry favoring oppositional
content, which reframes perceived suppression in terms of
audience intensity (Section 4). Third, we give a quantified
account ofwhy the conventional analysis concludes oth-
erwise, tracing the spurious detection to pseudoreplication
and stance-aligned confounds on the same corpus, and dis-
till a short protocol for credible visibility audits (Section 5).
We do not claim that platforms never differentially distribute
content. We claim that on a high-quality panel, analyzed at
the account level, the alleged effect is not present at the mag-
nitudes the design can resolve, while a different and measur-
able asymmetry is present.
2 Related work
2.1 Shadow banning, visibility moderation, and
folk theories
Shadow banning denotes a platform reducing a user’s visi-
bility without notice (Le Merrer, Morgan, and Tr´edan 2021).
Platforms increasingly moderate by demotion rather than
removal, treating “borderline” content with reduced distri-
bution (Gillespie 2022; Zuckerberg 2018; Goldman 2021),
which makes reduced reach a genuine governance lever
but a hard one to observe from outside (Zeng and Kaye
2022; Gillespie 2018; Gorwa, Binns, and Katzenbach 2020).
Because ranking is opaque, users reason about it through
folk theories assembled from personal observation (Eslami
et al. 2015; Rader and Gray 2015). The belief in being
shadow banned is one such theory, an “algorithmic folk-
lore” that platforms deny and users cannot readily dis-
prove (Savolainen 2022; Cotter 2023). On TikTok, the the-
ory is bound up with identity. Creators infer that the plat-
form buries content tied to marginalized identities or out-of-
favor politics, and they adapt what they post to test and evade
the suspected penalty (Karizat et al. 2021; Simpson and Se-
maan 2021; Are 2022; Duffy and Meisner 2023). The folk
method of “proof” is comparative and widespread. In a rep-
resentative U.S. survey, a drop in engagement metrics was
the most common way users diagnosed their own shadow-
ban (44%), followed by checking visibility from a second
account (42%) (Nicholas 2022), and interview studies find
users treating view-count gaps between comparable posts as
definitive proof (Delmonaco et al. 2024; Cotter 2023). That
comparative logic is exactly what a pooled audit formalizes,
and showing where it breaks is the purpose of this paper.
2.2 Auditing algorithmic systems
External audits are the standard tool for studying opaque
platforms (Sandvig et al. 2014; Metaxa et al. 2021; Bandy
2021; Ibrahim et al. 2023; Aldahoul et al. 2026), ranging
from sock-puppet personalization audits of search (Hannak
et al. 2013; Robertson et al. 2018) to recommender audits
of video platforms (Hussein, Juneja, and Mitra 2020). A
recurring lesson is that conclusions are fragile to how the
data are analyzed, and that the unit of analysis often mat-
ters more than the size of the corpus. Hosseinmardi et al.
(2021) show that account-level consumption data overturn
the popular claim that YouTube’s algorithm drives radical-
ization. Account-level evidence has also reshaped the de-
bate over political amplification. Analyzing a randomized
holdout rather than an observational side-by-side, Husz ´ar
et al. (2022) estimate that Twitter’s algorithm amplifies
right-leaning content in six of seven countries studied, a
real but bounded effect. The same study detects no signif-
icant association between an individual politician’s party
and amplification, so even with platform-side randomization
the unit of analysis changes the answer. On TikTok, audits
have characterized the For You feed’s personalization fac-
tors (Boeker and Urman 2022; V ombatkere et al. 2024), its
political content (Medina Serrano, Papakyriakopoulos, and
Hegelich 2020; Ibrahim et al. 2026), and users’ theories of
how it boosts or buries posts (Klug et al. 2021; Bhandari and
Bimo 2022).
Direct attempts to measure differential visibility vary
widely in method, and the axis on which they vary most
is the unit of analysis. At one end, high-profile advo-
cacy comparisons use no independent unit at all. A widely
circulated report benchmarks platform-lifetime post totals
for sixty hashtags on TikTok against Instagram and reads
the skewed ratios as evidence of likely deliberate suppres-
sion, with no uncertainty quantification and no adjustment
for platform age, regional availability, or audience demo-
graphics (Network Contagion Research Institute 2023); its
critics answered with placebo hashtags rather than statis-
tics (Matzko 2024; Harwell 2023). A descriptive analysis
of Israel/Gaza content on TikTok reports side-level view to-
tals whose mean and median disagree, the pro-Palestinian
mean running nearly five times higher while its median is
lower, the signature of a tail-driven pooled comparison (Rad-
way and Edelson 2025). In the peer-reviewed literature the
same comparative design appears at the post level. An audit
of the May 2021 escalation compares318hashtag-sampled
TikTok videos across sides using independent-samplest-
tests and pooled regressions, treating each video as an in-
dependent observation with no clustering by account, while
the sides differ by an order of magnitude in mean follower
count (Yarchi and Boxman-Shabtai 2025). At the other end
sit account-level designs. Le Merrer, Morgan, and Tr ´edan

(2021) test shadow-ban detections account by account over
2.5million Twitter profiles and argue that much of the pub-
lic evidence dissolves under careful definition and measure-
ment; Jaidka, Mukerjee, and Lelkes (2023) repeatedly test
a stratified random sample of roughly25,000U.S. accounts
and find shadowbans rare and concentrated among bot-like
accounts; recent sock-puppet audits aggregate exposure to
the account before testing (Ye, Luceri, and Ferrara 2025) or
cluster errors by bot and week (Ibrahim et al. 2026). The lit-
erature, in short, straddles the unit-of-analysis line, and no
external audit has to our knowledge shown on a single cor-
pus that this choice alone manufactures or dissolves a de-
tection. That demonstration is our contribution, on a dataset
dense enough to remove the objection that the data are too
thin.
The strongest evidence about platform effects comes from
experiments run on the platform itself. In the 2020 U.S.
Facebook and Instagram studies, researchers randomized
feed ranking and composition for consenting users and mea-
sured downstream exposure, attitudes, and behavior (Guess
et al. 2023; Nyhan et al. 2023; Gonz´alez-Bail´on et al. 2023);
switching to a chronological feed changed what users saw
substantially but moved their attitudes little. These designs
identify causal effects because treatment is assigned rather
than inferred; absent platform cooperation, an external audit
can characterize exposure and distribution but should report
bounded, correlational conclusions.
2.3 Measurement hazards
Three known hazards shape any such audit. The first is
pseudoreplication, in which correlated repeated measure-
ments are treated as independent replicates, inflating sig-
nificance without adding information (Hurlbert 1984; Lazic
2010; Lazic, Clarke-Williams, and Munaf`o 2018; Galbraith,
Daniel, and Vissel 2010); the remedies are to analyze at the
independent unit or model the dependence, and to report the
design effect and effective sample size (Aarts et al. 2014;
Kish 1965). The second isresearcher degrees of freedom,
the data-contingent analytic choices that manufacture signif-
icance even without intent (Gelman and Loken 2016; Sim-
mons, Nelson, and Simonsohn 2011), a recognized driver
of the broader replication crisis (Ioannidis 2005; Collabora-
tion 2015); the accepted defenses are pre-registration, full-
grid reporting with multiplicity control, and specification-
curve or multiverse analysis (Simonsohn, Simmons, and
Nelson 2020; Steegen et al. 2016; Benjamini and Hochberg
1995; Nosek et al. 2018). The third ismeasurement bias.
The language-identification and LLM stance classifiers now
common in audits are less reliable on non-English, Global-
South content (Blasi, Anastasopoulos, and Neubig 2022;
Joshi et al. 2020; Kreutzer et al. 2022), and content clas-
sifiers carry social bias (Sap et al. 2019; Bender et al.
2021); LLM annotation is promising but non-deterministic
and task-dependent, and must be validated against human
labels (Gilardi, Alizadeh, and Kubli 2023; Reiss 2023; Pan-
gakis, Wolken, and Fasching 2023; Ziems et al. 2024). Our
design is built to address all three.
3 Data and design
TikTok distributes most views through the For You feed, a
recommender that surfaces posts to users who do not follow
the creator, so a post’s reach is only loosely tied to its au-
thor’s follower count (Boeker and Urman 2022; V ombatkere
et al. 2024). A shadow ban is therefore plausible in princi-
ple, the platform damping a post’s distribution with no vis-
ible action, and the same opacity makes reach hard to mea-
sure from outside. We use follower-normalized plays as our
reach proxy because it is the quantity the folk audits them-
selves use and the one a creator can observe, while noting
that it confounds algorithmic distribution with audience be-
havior; only platform-side logs could separate the two, and
we return to this limitation in the discussion.
3.1 A dense hourly panel
We tracked public TikTok accounts curated into pro and
anti sides of three topics, U.S. immigration enforcement
(ICE), Trump coverage (TRUMP), and Israel/Palestine.
For each account we followed its recent posts, record-
ingplayCount,diggCount(likes),commentCount,
shareCount, andcollectCount(saves) every hour,
alongside follower counts. Collection ran through TikAPI,
a third-party wrapper over TikTok’s public app endpoints.
We polled each tracked post’s public counters directly rather
than sampling any personalized For You feed, so personal-
ization does not enter the measurements. Over the collec-
tion window (3–28 April 2026) the collector completed604
hourly sweeps, and598of the602inter-sweep gaps are ex-
actly one hour. The realized panel is therefore dense and
uniform, with556,946real snapshot rows over2,753videos
and67accounts and a median of99observations per video.
Cumulative counters increment organically between consec-
utive hours, so each row is a fresh measurement rather than
a carried-forward value; by the standards of prior audits, this
is a high-quality panel, and the problems we document are
not artifacts of thin data.
3.2 Account selection and the analytic sample
The 67 accounts were curated before data collection began
to ensure representation of both sides of each topic across
a broad range of audience sizes. For each topic, we identi-
fied candidate accounts through Google searches for promi-
nent voices on each side of the issue, classified them by their
publicly expressed position, organized them into predefined
follower-size tiers (from micro accounts to multi-million-
follower creators), and selected accounts so that opposing
sides contained comparable coverage across these strata.
The resulting roster spans approximately 2.5K to 22M fol-
lowers and includes the actors that shape political discourse
on TikTok, from institutional and official accounts (party
organizations, campaigns, militaries, news outlets) to com-
mentators, independent creators, and on-the-ground journal-
ists. Side membership reflects each account’s publicly ex-
pressed position on the topic under study; accounts produc-
ing content on several issues appear in more than one topic,
assigned by their position on each. The roster was finalized
before hourly collection began, so selection is independent

of the outcomes analyzed here. Table 4 lists these accounts
in de-identified form; we withhold handles because naming
public figures next to a stance and reach claim on these top-
ics could be used to target them.
The follower-size tiers reduce structural differences in au-
dience size rather than produce one-to-one matching, so the
sides remain heterogeneous in follower count, posting ca-
dence, language, and content; we measure and adjust for
these differences analytically (Section 5) rather than elimi-
nate them by design. The dataset is therefore a curated, strat-
ified convenience sample, not a probability sample of politi-
cal TikTok, which limits external validity (Appendix 7). An
account enters a topic-specific analysis only if it posted at
least one relevant video during the window, so the accounts
analyzed per topic (Table 2) number fewer than the curated
roster. Appendix A reconciles every sample count reported
in the paper, from the complete curated roster to each ana-
lytic subset.
3.3 Stance and outcome measures
Our reach measure is ViewsPer1K= 1000·
playCount/followers, and engagement-per-view is
total reactions divided by plays. Each video passed
through a multi-step LLM classifier that first de-
cides relevance, then topic, then a per-video stance
(relevance→topic→stance). Of the2,753tracked videos,
2,469were classifiable and940are on-topic for one of
the three issues;754of these also carry a clear per-video
stance (Table 3). Because LLM classifiers are contestable
on non-English content (Gilardi, Alizadeh, and Kubli 2023;
Reiss 2023; Blasi, Anastasopoulos, and Neubig 2022), we
deliberately limit the classifier’s authority, using it only
to identify which of an account’s videos are on-topic and
taking stance for the primary analysis from the account’s
curated side rather than from the per-video label. The
account-level reach analysis therefore aggregates the816
on-topic videos belonging to a curated pro/anti account
to one value per account (Table 2). Taking stance from
the curated side insulates the headline result from the
classifier’s largest source of error, and the per-video labels
agree with the curated side often enough to corroborate
the curation (Section 3.4). We report engagement-per-view
pooled and decomposed into likes, comments, shares, and
saves, since the components carry different signals about
audience intensity.
3.4 Classifier and its reliability
The classifier pipeline deployed is a three-model LLM en-
semble (GPT-4o, Gemini, and Claude Sonnet) queried at
temperature0, run relevance→topic→stance; the models
vote, we keep the majority label, and the26on-topic videos
without a majority are excluded. The models read content in
its original language, including Arabic, with no translation
step. Inter-model agreement (Krippendorff’sα) is0.81for
topic and0.78for stance, lower for relevance (0.56), which
is why we use relevance only as a coarse filter. Because
the headline estimand takes stance from the curated account
side, classifier error enters the primary analysis only through
which videos count as on-topic. As a check on the curation,
the per-video stance label agrees with the curated side on
93.1%of clearly-stanced videos, and the agreement does
not degrade on Arabic (93.4%against92.6%on English),
counter to the usual non-English reliability gap (Blasi, Anas-
tasopoulos, and Neubig 2022; Joshi et al. 2020; Kreutzer
et al. 2022); the per-topic and per-language breakdown is in
Appendix C. To validate the filter directly, we hand-labeled a
stratified gold set of200videos (balanced across topic, side,
and language) plus100videos on which the three models
disagreed on relevance; the ensemble matches the human la-
bels closely on both (on-topic inclusionF 1 = 0.88strati-
fied and0.80on the hard disagreement cases; full metrics in
Appendix C). The low relevanceαtherefore reflects single-
model disagreement that the majority vote resolves correctly
rather than a biased on-topic filter. The same per-video labels
drive the video-level rung of the pseudoreplication ladder
(Section 5), where the reach null is unchanged.
3.5 The account as the unit of analysis
Because accounts are the units we sample and the level at
which side labels are curated, our primary estimand is an
account-level side difference in follower-normalized reach.
We therefore aggregate videos to accounts and use account-
level randomization inference, and we do not claim to iden-
tify within-account, post-level demotion. This makes the ac-
count the independent unit of inference; whether any plat-
form treatment operates at the account or the post level
is a separate question, which we revisit with a per-video,
account-clustered model in Section 5. We analyze each topic
separately, as the original claim oftopic-conditionalasym-
metry was framed (Table 2). ICE is near-empty as a content
topic; we report it throughout but it cannot support inference,
so the informative topics are Trump and Israel/Palestine.
3.6 Estimators and pre-registration
We summarize each video by its peak observed reach and
collapse videos to the account by the median, giving one
value per account. For each account-level set we report
Cliff’sδ, a rank effect size in[−1,1], with an account-
bootstrap95%CI. The primary test is a Mann–WhitneyU
on the account values; our preferredp-value comes from
randomization inference, permuting stance labels across
accountsB= 2×10 4 times, which needs no large-
sample assumption. We additionally fit cluster-robust re-
gressions with follower and age controls, while noting that
cluster-robust standard errors are unreliable at our cluster
counts (Colin Cameron and Miller 2015; Barr et al. 2013).
The analysis grid (3 topics×3 outcomes), the account-
level unit, the estimators, and the discovery/confirmatory
split were fixed in a pre-registration frozen before any infer-
ential test was run; deviations are logged with it. Following
that plan we correct each outcome family with Benjamini–
Hochberg (Benjamini and Hochberg 1995; Nosek et al.
2018), because the three outcomes answer three distinct
questions (reach, engagement, velocity) rather than one; we
report a stricter global correction across the full grid as a
sensitivity in Section 4, and the conclusions do not change.
To calibrate the procedures themselves, rather than only
the data, we run a constructed-null simulation. We repeat-

edly reassign the stance labels at random across accounts
(3,000draws), which destroys any true stance effect by con-
struction, and record how often each test rejects atα= 0.05.
A correctly specified test should reject about5%of the time;
a test that rejects far more often is detecting the data’s depen-
dence structure, not a stance effect. We run this calibration
at each unit of analysis, which lets us measure directly how
pooling inflates the false-positive rate (Section 5).
4 An engagement gap, but no reach
suppression
4.1 A gap that vanishes at the account level
The discourse and the standard analysis alike predict a topic-
conditional reach gap, and at first our data appear to de-
liver one. Pooling the hourly snapshots and comparing sides
with a rank test, the Israel/Palestine reach gap reachesp=
6.7×10 −147 and the Trump gap falls below floating-point
precision. The significance is already large at the video level
(Trumpδ= 0.40,p= 4×10 −10; Israel/Palestineδ= 0.24,
p= 4×10 −4), and grows by scores of orders of magnitude
when the hourly snapshots are added. By the conventions of
the pooled designs reviewed in Section 2, largeN, a vanish-
ingp, and a passed multiple-testing correction, this meets the
standard for a detection (Yarchi and Boxman-Shabtai 2025).
This apparent detection does not survive the move to
account-level analysis. At the account level no reach com-
parison is significant (ICEδ= 0.07,p= 0.93; TRUMP
δ= 0.08,p= 0.71; Israel/Palestineδ= 0.06,p= 0.81),
with BH-correctedq≈0.93throughout and randomization
inference in agreement (Table 1). The point estimates are
near zero throughout (|δ| ≤0.08).
4.2 The null is informative
A null is only as strong as the design’s power to detect an ef-
fect. The same design and sample size detect a clear effect on
a different outcome. Engagement-per-view is lower for the
establishment side on both informative topics, surviving the
pre-registered correction (TRUMPδ=−0.51,q= 0.025;
Israel/Palestineδ=−0.64,q= 0.021), with bootstrap
CIs that exclude zero ([−0.82,−0.15]and[−0.94,−0.26]).
We useestablishmentas descriptive shorthand for the pro-
Trump and pro-Israel side andoppositionalfor the anti-
Trump and pro-Palestine side, with no normative judgment
intended. We treat the engagement effect as a secondary,
supporting result rather than a headline. It also survives a
correction across the six informative-topic cells (q= 0.049,
0.043); only under the strictest possible correction, a global
BH across all nine grid cells, does it turn borderline, withq
rising to0.073(Trump) and0.064(Israel/Palestine). Its role
is to show that the design can resolve an effect of this size at
this sample, which is what makes the reach null informative.
Two further analyses make the bound explicit. First, a
Monte-Carlo power analysis shows that at the observed ac-
count counts the reach test has76–89%power to detect a
true effect ofδ= 0.6and63–70%atδ= 0.5, the range
of the engagement effect we do detect. Second, the account-
bootstrap intervals for reach turn the null into a quantified
equivalence statement. We can rule out a reach effect larger
Table 1: No reach effect survives at the account level, while
the engagement effect survives on both informative top-
ics with a CI that excludes zero. Pre-registered grid with
account-bootstrap95%CIs, rank-testp, BH-correctedq
(within outcome family), and randomizationp.
Topic Outcomen a/nb δ[95% CI]p MW qBH pperm
ICE reach 6/5+0.07 [-0.67,0.73] 0.93 0.93 0.86
TRUMP reach 17/14+0.08 [-0.34,0.49] 0.71 0.93 0.75
ISR/PAL reach 13/12+0.06 [-0.41,0.51] 0.81 0.93 0.91
ICE eng/view 6/5−0.13 [-0.80,0.60] 0.79 0.79 1.00
TRUMP eng/view 17/14−0.51 [-0.82,-0.15] 0.016 0.025 0.015
ISR/PAL eng/view 13/12−0.64 [-0.94,-0.26] 0.007 0.021 0.002
ICE velocity 6/5+0.13 [-0.67,0.80] 0.79 0.79 0.81
TRUMP velocity 17/14−0.23 [-0.62,0.19] 0.29 0.44 0.21
ISR/PAL velocity 13/12+0.42 [-0.01,0.80] 0.077 0.23 0.26
than|δ|= 0.49on Trump and|δ|= 0.51on Israel/Palestine
at95%confidence (Table 1), while smaller effects remain
possible; the null is therefore bounded and quantified. The
reach nulls also reproduce across pre-specified discovery (3–
15 Apr) and confirmatory (16–28 Apr) windows, with none
of the strengthening under confirmation that a real effect
would produce (Appendix D).
4.3 An engagement asymmetry, not reduced
reach
The engagement asymmetry is the clearest signal in the data,
and it points the opposite way from a visibility penalty. Op-
positional content earns more per-view likes, shares, and
saves on both informative topics, while comments, them-
selves an effortful reaction, differ little (Figure 1). The per-
component gaps are consistent and sizable. On Trump,δ=
−0.47for likes,−0.44for shares, and−0.69for saves,
against−0.07for comments; on Israel/Palestine,−0.67,
−0.54, and−0.64against−0.10for comments. Saves,
among the most deliberate signals a viewer can send, show
the largest gap on both topics. Higher engagement per view
does not by itself rule out reach suppression, since a plat-
form could in principle demote content that draws strong
reactions; but paired with the reach null, the pattern is more
consistent with audience mobilization than with reach sup-
pression, in line with the long-noted gap between counted
engagement and circulation (Gerlitz and Helmond 2013;
Cotter 2019). A pooled video-level comparison of the May
2021 escalation likewise reported higher engagement on
pro-Palestinian posts (Yarchi and Boxman-Shabtai 2025); at
the account level, that engagement asymmetry survives the
unit correction while the reach suppression the discourse in-
fers from such gaps does not. The engagement gap also per-
sists under an English-only restriction, whereas the apparent
reach gap, as we show next, does not.
5 Why the conventional analysis finds
otherwise
The same data yield “p <10 −140” and “null” depending
on a single choice, the unit of analysis. Two mechanisms
account for the gap.

δ=-0.47*
δ=-0.67*
δ=-0.07
δ=-0.10
δ=-0.44*
δ=-0.54*
δ=-0.69*
δ=-0.64*
Isr/Pal · Likes Isr/Pal · Comments Isr/Pal · Shares Isr/Pal · Saves
Trump · Likes Trump · Comments Trump · Shares Trump · Saves
1.0
3.0
10.0
1.0
10.0
100.0
0.3
1.0
3.0
10.0
30.0
1.0
10.0
100.0
1.0
3.0
10.0
1.0
3.0
10.0
30.0
10.0
30.0
100.0
300.0
30.0
100.0
300.0Reactions per 1,000 views (log scale)
Establishment Oppositional
Oppositional content earns more engagement per view on every component but comments
Figure 1: Oppositional content earns more reactions per view, a direction inconsistent with a visibility penalty. Per-account rates
by side (log scale), annotated with the account-level Cliff’sδ(∗marksp <0.05); the gap appears in likes, shares, and saves
while comments differ little. Establishment denotes pro-Trump and pro-Israel accounts, oppositional their opposites.
5.1 Pseudoreplication
Repeated hourly snapshots of one video are near-duplicates.
Decomposing the variance oflog(ViewsPer1K), snapshots
within a video have an intraclass correlation of0.98(Ap-
pendix B). Therefore, the173,050on-topic snapshot rows
carry the information of about960independent videos (de-
sign effect≈180) (Kish 1965; Killip, Mahfoud, and Pearce
2004), and those videos nest within only the few dozen ac-
counts where stance varies. Counting the snapshots as inde-
pendent observations, as a pooled test does, treats an effec-
tive sample of dozens as one of hundreds of thousands (Hurl-
bert 1984; Lazic, Clarke-Williams, and Munaf`o 2018; Aarts
et al. 2014). The per-topic effective sample is471videos
for Trump and460for Israel/Palestine (Appendix B), not
the tens of thousands of rows, and those videos in turn nest
within31and25accounts. Because ap-value shrinks with√
Nwhile a rank effect size does not, inflating the unit
drives thep-value toward zero while leavingδessentially
where it was.
Figure 2 shows the consequence. For each topic we
run the same reach comparison at the account, video, and
video-hour units. As the unit inflates, thep-value collapses
while the effect size remains essentially unchanged. For
Israel/Palestine the account-level gap is null (δ= 0.06,
p= 0.81) yet reachesp= 6.7×10 −147 at the video-hour
level, withδnever exceeding0.24. A constructed-null simu-
lation makes the error explicit. When we randomly reassign
stance to accounts, destroying any true effect, the account-
level test holds near its nominal rate (4%pooled,3–6%by
topic), while the pooled video-hour test rejects95%of the
time (Figure 5; per-topic detail in Appendix D). Under a
constructed null with no stance effect at all, the pooled pro-
cedure still reports significance almost every time, so the re-
ported detection is manufactured outright. The pooled de-
sign is not a strawman. A peer-reviewed TikTok compari-
son of this same conflict treats hashtag-sampled videos as
independent observations in exactly this way (Yarchi and
Boxman-Shabtai 2025), and the comparisons that reached
congressional testimony pool hashtag aggregates with no
unit at all (Network Contagion Research Institute 2023).
5.2 Confounds aligned with stance
The residual gap that pooling exaggerates is not stance to
begin with, because the sides are not comparable on three
nuisance dimensions. The first issize. Reach is sublinear in
followers (the slope oflogplayCountonlogfollowers is
0.73for Trump and near zero for Israel/Palestine, both be-
low one), so the per-follower metric over-penalizes large ac-
counts, and the pro-Palestine accounts are3.6×larger than
pro-Israel accounts at the median (Figure 3). The second is
age. Pro-Israel videos enter our panel far later in their life
cycle (median128hours since creation, against under one
hour for pro-Palestine), so the two sides are compared at
different points on the view-accumulation curve. The third
islanguage. Pro-Palestine accounts post mostly Arabic con-
tent and pro-Israel accounts almost none, while collection
defaulted to a U.S. region, so stance is nearly collinear with
content language and audience geography (Blasi, Anasta-
sopoulos, and Neubig 2022; Sap et al. 2019; Kreutzer et al.
2022). The collector ran with a default U.S. country setting;
because the public counters are global totals, this does not
change a video’s numbers, only which videos are discover-
able and the language environment in which a U.S. viewer
would meet them, so the confound is one of content and
audience composition rather than of measurement. Restrict-
ing to English-only videos, the account-level reach contrast
stays null (δ=−0.21,p= 0.42; Figure 6). There is no
account-level reach gap for language to explain in the first
place; the pooled gap that does appear is partly a compari-
son of Arabic content delivered to a U.S. audience against

p=0.93 p=0.89 p=0.22 p=0.71 p=4e-10
p<1e-300
p=0.81 p=4e-04
p=7e-147
ICE Trump Israel/Palestine
Account Video Video-hour Account Video Video-hour Account Video Video-hour
0
100
200
300
−log10(p)
Significance explodes as autocorrelated rows are pooled…
+0.07 +0.04 -0.01 +0.08
+0.40 +0.40
+0.06
+0.24
+0.11
Account Video Video-hour Account Video Video-hour Account Video Video-hour
0.0
0.2
0.4
Cliff's δ
…while the effect size stays small at every unit
Figure 2: Inflating the unit of analysis manufactures significance. The same reach comparison at three units; thep-value (top)
grows without bound as autocorrelated snapshots are counted as independent, while Cliff’sδ(bottom) stays small at every unit.
English content. The engagement gap, by contrast, persists
within English and in fact strengthens slightly on the re-
stricted set (engagement-per-viewδ=−0.76for English-
only, against−0.64for all videos; Figure 6), so it reflects
how the two audiences react rather than a language artifact.
5.3 Adjusting the confounds directly
Adjusting for a confound in a model agrees with subsetting
it away. We fit a per-video model oflog(peak plays)on side,
withlog(followers)andlog(video age)as controls and stan-
dard errors clustered by account. The post is the observation
but the account remains the unit of inference, the specifi-
cation appropriate if moderation acts at the post level. Af-
ter these controls no topic shows a significant side differ-
ence in reach (Trumpβ= 0.84,p= 0.07; Israel/Palestine
β= 0.45,p= 0.46; ICEβ= 0.34,p= 0.70); the
single borderline cell, Trump, points if anything toward
the establishment side rather than against the oppositional
one. Because cluster-robust errors are anti-conservative at
these cluster counts (Colin Cameron and Miller 2015), we
recompute each side coefficient with a wild-cluster boot-
strap (Rademacher weights, null imposed,B= 9,999; Ap-
pendix E). The correction removes even the Trump signal,
whose bootstrapprises from0.07to0.22, and no topic is
significant under the small-cluster-aware test. The post-level
adjusted analysis thus reaches the same place as the account-
level test, with no robust reach gap.
Two targeted subset checks, restricting to videos first
observed within24h (48h) of posting and stratifying the
English-only topics by language, leave the reach nulls un-
changed (Appendix D).
5.4 The result is fragile across the specification
space
The choices that flip the result, the unit of analysis, the out-
come metric, and the language subset, are each individually
defensible, and an analyst rarely commits to all of them in
advance (Gelman and Loken 2016; Simmons, Nelson, and
Simonsohn 2011). Across24defensible specifications (Fig-
ure 4),19are “significant” and the sign is mixed, but the
variation is structured; significance is governed almost en-
tirely by the unit of analysis, rising from50%of account-
level specifications to100%at the video-hour level (Simon-
sohn, Simmons, and Nelson 2020; Steegen et al. 2016; Sil-
berzahn et al. 2018). Fix the unit at the account and the am-
biguity collapses, with the reach question consistently null
and the engagement question consistently positive.
5.5 Toward credible visibility audits
From these mechanisms we distill a minimal practice.
(1) Analyze real observations at the level of the independent
unit, and report the design effect and effectiveNbefore any
pooled test. (2) Make the sampled independent unit explicit;
for account-curated side comparisons like ours it is the ac-
count, and if the hypothesized treatment is post-level, use
hierarchical or cluster-aware models rather than treating re-
peated posts or snapshots as independent. (3) De-confound
account size, video age, and content language and region
before attributing any gap to stance. (4) Pre-register the grid
and publish a specification curve rather than a single favor-
able cell. (5) Report power and frame the result as a bounded
claim, reserving causal claims for randomized on-platform
experiments.
6 Discussion
Anyone who pools the snapshots can produce a significant-
looking shadow-ban result from these data, complete with a
vanishingly smallp. Producing a defensible result is slower
and, here, ends in a reach null. That asymmetry of effort has
consequences beyond research, because journalists and ad-
vocacy organizations run effectively the same observational
comparisons (Network Contagion Research Institute 2023;
Radway and Edelson 2025; Harwell 2023), and the incen-
tives favor the significant-looking result. Our constructed-

10K
100K
1M
Pro-
Israel
Pro-
Palestine
Followers (log scale)
(a) Account size
0
10
100
1,000
10,000
Pro-
Israel
Pro-
Palestine
Hours since creation
(b) Video age at first obs.
0%
25%
50%
75%
100%
Pro-
Israel
Pro-
Palestine
Share of on-topic videos
English Arabic Unknown Other
(c) Language mix
Figure 3: Stance is confounded with (a) account size, (b) video age at first observation, and (c) content language on the Is-
rael/Palestine topic, so a between-stance reach gap pooled below the account level is not identifiable.
-0.75
-0.50
-0.25
0.00
0.25
0.50
Cliff's δ
Not significant Significant (p<.05)
Sign and significance hinge on the unit of analysis
English
All-lang
Video-hour
Video
Account
Eng/view
Reach
Israel/Palestine
Trump
Specifications sorted by effect size
Figure 4: Sign and significance of the reach “effect” flip
across the24defensible specifications, driven mainly by the
unit of analysis. Each point (top) is one analysis; its choices
are shown below.
null and specification analyses quantify how easily that re-
sult can be manufactured, and in which direction. The mech-
anism involves no fraud, only the ordinary accumulation of
defensible-looking choices. An analyst who collects hourly
snapshots because dense data seem better, pools them be-
cause more rows seem better, and reports the comparison
that reaches significance never once does anything that looks
like p-hacking, yet arrives at a result inflated by two orders
of magnitude.
The one asymmetry we do find, more sharing and sav-
ing of oppositional content, is consistent with audience mo-
bilization rather than suppression. Saves and shares, the
most effortful reactions a viewer can give, show the largest
gaps; comments barely differ. The effect is correlational and
may reflect who follows these accounts rather than how the
platform treats them, and we do not claim otherwise. The
methodological lesson is more general. Reach is a single,
noisy measure of a post’s reception, and an audit that mea-
sures the full interaction profile can find a real signal exactly
where the reach comparison finds a spurious one.
None of this shows that platforms are even-handed; dif-
ferential distribution may exist and matter greatly. The
point is that establishing it requires either randomized on-
platform experiments or observational designs with matched
accounts, dense and uniform sampling, language and re-
gion held fixed, and analysis at the account level with pre-
registration. Account-level care has overturned algorithmic-
amplification claims before (Hosseinmardi et al. 2021); on
these three topics, applied to TikTok reach, it does so again.
7 Limitations
Several limitations bound our claims. Our corpus is obser-
vational, single-platform, and built from curated accounts,
so we characterize the accounts we tracked, not TikTok as
a whole. The account counts per topic are in the tens, so
we bound rather than exclude reach effects smaller than the
design resolves (Section 4). Reach is measured by follower-
normalized plays, a proxy for distribution rather than a di-
rect read of the ranker, and it cannot separate algorithmic
demotion from audience behavior; only platform-side logs
could. Our language analysis relies on imperfect platform
language tags, which only sharpens the difficulty of separat-
ing stance from language. Stance is assigned at the account
level from a curated side, our sampling unit, though it misses
within-account variation across posts. The on-topic filter is
an LLM ensemble; because the headline stance comes from
the curated side, classifier error enters only through which
videos count as on-topic, a gate we validate against a human-

labeled gold set (F1 ≈0.80even on the model-disagreement
cases; Section 3.4). That gold set is author-labeled, which
bounds the check. Finally, ICE is too sparse to support in-
ference and is reported for completeness only. None of these
limitations is repaired by adding more autocorrelated rows,
which is the central point of the paper.
8 Ethics and data
This study uses only data that TikTok exposes publicly, the
counts of plays, likes, comments, shares, and saves for posts
from public accounts, together with public follower counts.
We did not interact with users or alter their feeds. We report
results only in aggregate, at the level of curated sides and
topics; released artifacts give per-account quantities only in
de-identified, hashed form and never join a named handle
to a stance attribution or a suppression claim. The topics,
especially Israel/Palestine, are sensitive, and a per-account
stance-and-reach table could be repurposed to target indi-
viduals. Stance labels describe an account’s public, curated
position, not any inference about a person’s identity. Be-
cause measurement instruments such as language identifi-
cation and LLM stance classifiers are known to be biased
against non-English and Global-South content (Blasi, Anas-
tasopoulos, and Neubig 2022; Sap et al. 2019), we keep
those instruments out of the headline estimand and validate
the ones we do use against human labels. Because this study
analyzes only public, aggregate platform counters and in-
volves no interaction with users, it did not require IRB re-
view under our institution’s criteria for research on public,
non-interactive data.
9 Conclusion
We asked whether TikTok shadow bans political content, us-
ing a dense hourly panel built to answer the question. An-
alyzed conventionally, the data “detect” suppression with
overwhelming significance. Analyzed at the unit where
stance is defined, and after accounting for size and language
confounds, they show no evidence of moderate-to-large dif-
ferential reach suppression across three contested topics.
The one robust asymmetry is greater audience engagement
for oppositional content, with reach unchanged. Detecting
differential visibility from public data is harder than current
practice assumes, and in this corpus what is read as a shadow
ban is better explained by a more engaged audience than by
a suppressed one.
References
Aarts, E.; Verhage, M.; Veenvliet, J. V .; Dolan, C. V .; and
Van Der Sluis, S. 2014. A solution to dependency: using
multilevel analysis to accommodate nested data.Nature neu-
roscience, 17(4): 491–496.
Aldahoul, N.; Ibrahim, H.; Mahmutoglu, M.; Tarar, H.; Zaf-
far, M. F.; Rahwan, T.; and Zaki, Y . 2026. Schadenfreude
in the Digital Public Sphere: A cross-national and decade-
long analysis of Facebook news engagement.arXiv preprint
arXiv:2601.20413.
Are, C. 2022. The Shadowban Cycle: an autoethnography of
pole dancing, nudity and censorship on Instagram.Feminist
Media Studies, 22(8): 2002–2019.
Bandy, J. 2021. Problematic machine behavior: A system-
atic literature review of algorithm audits.Proceedings of the
acm on human-computer interaction, 5(CSCW1): 1–34.
Barr, D. J.; Levy, R.; Scheepers, C.; and Tily, H. J. 2013.
Random effects structure for confirmatory hypothesis test-
ing: Keep it maximal.Journal of memory and language,
68(3): 255–278.
Bender, E. M.; Gebru, T.; McMillan-Major, A.; and
Shmitchell, S. 2021. On the dangers of stochastic par-
rots: Can language models be too big? InProceedings of
the 2021 ACM conference on fairness, accountability, and
transparency, 610–623.
Benjamini, Y .; and Hochberg, Y . 1995. Controlling the false
discovery rate: a practical and powerful approach to multi-
ple testing.Journal of the Royal statistical society: series B
(Methodological), 57(1): 289–300.
Bhandari, A.; and Bimo, S. 2022. Why’s everyone on Tik-
Tok now? The algorithmized self and the future of self-
making on social media.Social media+ society, 8(1):
20563051221086241.
Blasi, D.; Anastasopoulos, A.; and Neubig, G. 2022. Sys-
tematic inequalities in language technology performance
across the world’s languages. InProceedings of the 60th
Annual Meeting of the Association for Computational Lin-
guistics (V olume 1: Long Papers), 5486–5505.
Boeker, M.; and Urman, A. 2022. An empirical investigation
of personalization factors on TikTok. InProceedings of the
ACM web conference 2022, 2298–2309.
Colin Cameron, A.; and Miller, D. L. 2015. A practitioner’s
guide to cluster-robust inference.Journal of human re-
sources, 50(2): 317–372.
Collaboration, O. S. 2015. Estimating the reproducibility of
psychological science.Science, 349(6251): aac4716.
Cotter, K. 2019. Playing the visibility game: How digital
influencers and algorithms negotiate influence on Instagram.
New media & society, 21(4): 895–913.
Cotter, K. 2023. “Shadowbanning is not a thing”: Black
box gaslighting and the power to independently know and
credibly critique algorithms.Information, Communication
& Society, 26(6): 1226–1243.
Delmonaco, D.; Mayworm, S.; Thach, H.; Guberman, J.;
Augusta, A.; and Haimson, O. L. 2024. ” What are you do-
ing, TikTok?”: How Marginalized Social Media Users Per-
ceive, Theorize, and” Prove” Shadowbanning.Proceedings
of the ACM on Human-Computer Interaction, 8(CSCW1):
1–39.
Duffy, B. E.; and Meisner, C. 2023. Platform governance
at the margins: Social media creators’ experiences with al-
gorithmic (in) visibility.Media, Culture & Society, 45(2):
285–304.
Eslami, M.; Rickman, A.; Vaccaro, K.; Aleyasen, A.; Vuong,
A.; Karahalios, K.; Hamilton, K.; and Sandvig, C. 2015. ” I

always assumed that I wasn’t really that close to [her]” Rea-
soning about invisible algorithms in news feeds. InProceed-
ings of the 33rd annual ACM conference on human factors
in computing systems, 153–162.
Galbraith, S.; Daniel, J. A.; and Vissel, B. 2010. A study
of clustered data and approaches to its analysis.Journal of
Neuroscience, 30(32): 10601–10608.
Gelman, A.; and Loken, E. 2016. The statistical crisis in
science.The best writing on mathematics (Pitici M, ed),
102: 305–318.
Gerlitz, C.; and Helmond, A. 2013. The like economy: So-
cial buttons and the data-intensive web.New Media & Soci-
ety, 15(8): 1348–1365.
Gilardi, F.; Alizadeh, M.; and Kubli, M. 2023. ChatGPT
outperforms crowd workers for text-annotation tasks.Pro-
ceedings of the National Academy of Sciences, 120(30):
e2305016120.
Gillespie, T. 2018.Custodians of the Internet: Platforms,
content moderation, and the hidden decisions that shape so-
cial media. Yale University Press.
Gillespie, T. 2022. Do not recommend? Reduction as a
form of content moderation.Social Media+ Society, 8(3):
20563051221117552.
Goldman, E. 2021. Content moderation remedies.
Gonz´alez-Bail´on, S.; Lazer, D.; Barber ´a, P.; Zhang, M.;
Allcott, H.; Brown, T.; Crespo-Tenorio, A.; Freelon, D.;
Gentzkow, M.; Guess, A. M.; et al. 2023. Asymmetric ide-
ological segregation in exposure to political news on Face-
book.Science, 381(6656): 392–398.
Gorwa, R.; Binns, R.; and Katzenbach, C. 2020. Algorith-
mic content moderation: Technical and political challenges
in the automation of platform governance.Big Data & So-
ciety, 7(1): 2053951719897945.
Guess, A. M.; Malhotra, N.; Pan, J.; Barber´a, P.; Allcott, H.;
Brown, T.; Crespo-Tenorio, A.; Dimmery, D.; Freelon, D.;
Gentzkow, M.; et al. 2023. How do social media feed algo-
rithms affect attitudes and behavior in an election campaign?
Science, 381(6656): 398–404.
Hannak, A.; Sapiezynski, P.; Molavi Kakhki, A.; Krishna-
murthy, B.; Lazer, D.; Mislove, A.; and Wilson, C. 2013.
Measuring personalization of web search. InProceedings
of the 22nd international conference on World Wide Web,
527–538.
Harwell, D. 2023. TikTok was slammed for its pro-
Palestinian hashtags. But it’s not alone. The Washington
Post.
Hosseinmardi, H.; Ghasemian, A.; Clauset, A.; Mobius, M.;
Rothschild, D. M.; and Watts, D. J. 2021. Examining the
consumption of radical content on YouTube.Proceedings of
the national academy of sciences, 118(32): e2101967118.
Human Rights Watch. 2023. Meta’s Broken Promises: Sys-
temic Censorship of Palestine Content on Instagram and
Facebook. Technical report, Human Rights Watch.
Hurlbert, S. H. 1984. Pseudoreplication and the design
of ecological field experiments.Ecological monographs,
54(2): 187–211.
Hussein, E.; Juneja, P.; and Mitra, T. 2020. Measuring mis-
information in video search platforms: An audit study on
YouTube.Proceedings of the ACM on human-computer in-
teraction, 4(CSCW1): 1–27.
Husz´ar, F.; Ktena, S. I.; O’Brien, C.; Belli, L.; Schlaikjer, A.;
and Hardt, M. 2022. Algorithmic amplification of politics on
Twitter.Proceedings of the national academy of sciences,
119(1): e2025334119.
Ibrahim, H.; AlDahoul, N.; Lee, S.; Rahwan, T.; and Zaki, Y .
2023. YouTube’s recommendation algorithm is left-leaning
in the United States.PNAS nexus, 2(8): pgad264.
Ibrahim, H.; Jang, H. D.; Aldahoul, N.; Kaufman, A. R.;
Rahwan, T.; and Zaki, Y . 2026. Systematic partisan con-
tent skews in TikTok during the 2024 US elections.Nature,
1–8.
Ioannidis, J. P. 2005. Why most published research findings
are false.PLoS medicine, 2(8): e124.
Jaidka, K.; Mukerjee, S.; and Lelkes, Y . 2023. Silenced
on social media: The gatekeeping functions of shadowbans
in the American Twitterverse.Journal of Communication,
73(2): 163–178.
Joshi, P.; Santy, S.; Budhiraja, A.; Bali, K.; and Choudhury,
M. 2020. The state and fate of linguistic diversity and in-
clusion in the NLP world. InProceedings of the 58th an-
nual meeting of the association for computational linguis-
tics, 6282–6293.
Karizat, N.; Delmonaco, D.; Eslami, M.; and Andalibi, N.
2021. Algorithmic folk theories and identity: How TikTok
users co-produce knowledge of identity and engage in al-
gorithmic resistance.Proceedings of the ACM on human-
computer interaction, 5(CSCW2): 1–44.
Killip, S.; Mahfoud, Z.; and Pearce, K. 2004. What is an
intracluster correlation coefficient? Crucial concepts for pri-
mary care researchers.The Annals of Family Medicine, 2(3):
204–208.
Kish, L. 1965. Survey sampling.
Klug, D.; Qin, Y .; Evans, M.; and Kaufman, G. 2021. Trick
and please. A mixed-method study on user assumptions
about the TikTok algorithm. InProceedings of the 13th ACM
web science conference 2021, 84–92.
Kreutzer, J.; Caswell, I.; Wang, L.; et al. 2022. Quality at
a Glance: An Audit of Web-Crawled Multilingual Datasets.
Transactions of the Association for Computational Linguis-
tics, 10: 50–72.
Lazic, S. E. 2010. The problem of pseudoreplication in neu-
roscientific studies: is it affecting your analysis?BMC neu-
roscience, 11(1): 5.
Lazic, S. E.; Clarke-Williams, C. J.; and Munaf `o, M. R.
2018. What exactly is ‘N’in cell culture and animal experi-
ments?PLoS biology, 16(4): e2005282.
Le Merrer, E.; Morgan, B.; and Tr´edan, G. 2021. Setting the
record straighter on shadow banning. InIEEE INFOCOM
2021-IEEE conference on computer communications, 1–10.
IEEE.

Matzko, P. 2024. Lies, Damned Lies, and Statistics: A Mis-
leading Study Compares TikTok and Instagram. Cato at Lib-
erty, Cato Institute.
Medina Serrano, J. C.; Papakyriakopoulos, O.; and
Hegelich, S. 2020. Dancing to the partisan beat: A first anal-
ysis of political communication on TikTok. InProceedings
of the 12th ACM Conference on Web Science, 257–266.
Metaxa, D.; Park, J. S.; Robertson, R. E.; Karahalios, K.;
Wilson, C.; Hancock, J.; and Sandvig, C. 2021. Auditing al-
gorithms: Understanding algorithmic systems from the out-
side in.F oundations and Trends® in Human–Computer In-
teraction, 14(4): 272–344.
Network Contagion Research Institute. 2023. A Tik-Tok-
ing Timebomb: How TikTok’s Global Platform Anomalies
Align with the Chinese Communist Party’s Geostrategic Ob-
jectives. Technical report, Network Contagion Research In-
stitute.
Nicholas, G. 2022. Shedding light on shadowbanning. Tech-
nical report.
Nosek, B. A.; Ebersole, C. R.; DeHaven, A. C.; and Mellor,
D. T. 2018. The preregistration revolution.Proceedings of
the National Academy of Sciences, 115(11): 2600–2606.
Nyhan, B.; Settle, J.; Thorson, E.; Wojcieszak, M.; Barber´a,
P.; Chen, A. Y .; Allcott, H.; Brown, T.; Crespo-Tenorio, A.;
Dimmery, D.; et al. 2023. Like-minded sources on Facebook
are prevalent but not polarizing.Nature, 620(7972): 137–
144.
Pangakis, N.; Wolken, S.; and Fasching, N. 2023. Auto-
mated Annotation with Generative AI Requires Validation.
arXiv preprint arXiv:2306.00176. arXiv:2306.00176.
Rader, E.; and Gray, R. 2015. Understanding user beliefs
about algorithmic curation in the Facebook news feed. In
Proceedings of the 33rd annual ACM conference on human
factors in computing systems, 173–182.
Radway, E.; and Edelson, L. 2025. Updating our Israel/Gaza
Analysis 2 Years On. Cybersecurity for Democracy.
Reiss, M. V . 2023. Testing the Reliability of ChatGPT for
Text Annotation and Classification: A Cautionary Remark.
arXiv preprint arXiv:2304.11085. arXiv:2304.11085.
Robertson, R. E.; Jiang, S.; Joseph, K.; Friedland, L.; Lazer,
D.; and Wilson, C. 2018. Auditing partisan audience bias
within google search.Proceedings of the ACM on human-
computer interaction, 2(CSCW): 1–22.
Sandvig, C.; Hamilton, K.; Karahalios, K.; and Langbort, C.
2014. Auditing algorithms: Research methods for detecting
discrimination on internet platforms.Data and discrimina-
tion: converting critical concerns into productive inquiry,
22(2014): 4349–4357.
Sap, M.; Card, D.; Gabriel, S.; Choi, Y .; and Smith, N. A.
2019. The Risk of Racial Bias in Hate Speech Detection. In
Proceedings of the 57th Annual Meeting of the Association
for Computational Linguistics (ACL), 1668–1678.
Savolainen, L. 2022. The shadow banning controversy: per-
ceived governance and algorithmic folklore.Media, culture
& society, 44(6): 1091–1109.
Silberzahn, R.; Uhlmann, E. L.; Martin, D. P.; Anselmi, P.;
Aust, F.; Awtrey, E.; Bahn´ık, ˇS.; Bai, F.; Bannard, C.; Bon-
nier, E.; et al. 2018. Many analysts, one data set: Making
transparent how variations in analytic choices affect results.
Advances in methods and practices in psychological science,
1(3): 337–356.
Simmons, J. P.; Nelson, L. D.; and Simonsohn, U. 2011.
False-positive psychology: Undisclosed flexibility in data
collection and analysis allows presenting anything as sig-
nificant.Psychological science, 22(11): 1359–1366.
Simonsohn, U.; Simmons, J. P.; and Nelson, L. D. 2020.
Specification curve analysis.Nature human behaviour,
4(11): 1208–1214.
Simpson, E.; and Semaan, B. 2021. For you, or for” you”?
Everyday LGBTQ+ encounters with TikTok.Proceedings
of the ACM on human-computer interaction, 4(CSCW3): 1–
34.
Steegen, S.; Tuerlinckx, F.; Gelman, A.; and Vanpaemel, W.
2016. Increasing transparency through a multiverse analysis.
Perspectives on Psychological Science, 11(5): 702–712.
V ombatkere, K.; Mousavi, S.; Zannettou, S.; Roesner, F.;
and Gummadi, K. P. 2024. Tiktok and the art of personal-
ization: investigating exploration and exploitation on social
media feeds. InProceedings of the ACM Web Conference
2024, 3789–3797.
Yarchi, M.; and Boxman-Shabtai, L. 2025. The Image War
Moves to TikTok: Evidence from the May 2021 Round of
the Israeli–Palestinian Conflict.Digital Journalism, 13(1):
115–135.
Ye, J.; Luceri, L.; and Ferrara, E. 2025. Auditing Politi-
cal Exposure Bias: Algorithmic Amplification on Twitter/X
During the 2024 U.S. Presidential Election. InProceedings
of the 2025 ACM Conference on Fairness, Accountability,
and Transparency.
Zeng, J.; and Kaye, D. B. V . 2022. From content modera-
tion to visibility moderation: A case study of platform gov-
ernance on TikTok.Policy & Internet, 14(1): 79–95.
Ziems, C.; Held, W.; Shaikh, O.; Chen, J.; Zhang, Z.; and
Yang, D. 2024. Can Large Language Models Transform
Computational Social Science?Computational Linguistics,
50(1): 237–291.
Zuckerberg, M. 2018. A Blueprint for Content Governance
and Enforcement. Facebook note, 15 November 2018.
A Sample accounting
Table 2 gives the per-topic account-level design, and Table 3
reconciles every sample count used in the paper, from the
full tracked panel to each analytic subset. Table 4 lists the
analytic accounts individually in de-identified form.
B Variance components and effective sample
size
Table 5 decomposes the variance oflog(ViewsPer1K)
within videos on the real on-topic snapshots. Repeated
hourly snapshots are near-duplicates, so the per-video effec-
tive sample size is roughly two orders of magnitude below

Table 2: Per-topic account-level design. Reach observations
are real snapshots; the unit of analysis is the account.
Topic Side Accounts Videos Median followers
ICEPRO6 8 82K
ICEAGAINST5 13 274K
TRUMPPRO17 143 224K
TRUMPAGAINST14 246 326K
ISR/PALPRO-ISRAEL13 101 75K
ISR/PALPRO-PALESTINE12 305 274K
Table 3: Sample accounting, from the full panel to each
analytic subset. Counts that appear elsewhere in the paper
are reconciled here; “–” marks a count we do not use. The
account-level reach set attributes each on-topic video to its
account’s curated side (Section 3.2); the clearly-stanced set
uses the per-video classifier label.
Stage Videos Snap. rows Handles
All tracked public videos2,753 556,946 65 ∗
Classifiable by the ensemble2,469– –
On-topic (one of three issues)940 173,050 59
Strict inclusion (non-ambiguous)900– –
Clearly stanced (per-video)754– –
Account-level reach set816–57 †
TheHandlescolumn counts distinct posting handles, so each row
is bounded by the row above it. The curated roster is67accounts
(94handle×topic cells); ∗65of them posted≥1tracked video.
†the reach set’s57handles form the67account×topic cells
analyzed per topic (Table 2).
the row count, and these videos nest within the few dozen
accounts of Table 2.
C Classifier reliability detail
The per-video stance label agrees with the curated account
side on93.1%of the clearly-stanced videos for which both
are defined (637of684). The agreement is stable across
topics (ICE94.1%, Israel/Palestine95.8%, Trump90.3%)
and across languages (English92.6%of514videos, Ara-
bic93.4%of137), so the per-video labels do not degrade
on non-English content. The residual disagreement is domi-
nated by the expected case of an account occasionally post-
ing off its usual side rather than by any systematic, language-
aligned error. Inter-model reliability across the three ensem-
ble members, by Krippendorff’sαon nominal labels, is0.56
for relevance,0.81for topic, and0.78for stance.
Human validation.To validate the classifier against hu-
man judgment we hand-labeled a gold set comprising a strat-
ified random sample of200videos (balanced across topic,
side, and language) and an additional100videos drawn from
the cases where the three models disagreed on relevance, the
hardest inputs for the ensemble. Table 6 scores the ensemble
majority vote against these labels. Agreement is high on the
stratified set and stays strong on the disagreement cases; the
most policy-relevant number, the on-topic inclusion decision
that builds the analytic sample, matches the human labels at
F1 = 0.80(disagreement).
D Additional robustness
Discovery and confirmatory windows.Table 7 reports
the account-level reach contrast separately in the pre-
specified discovery (3–15 Apr) and confirmatory (16–
28 Apr) windows. The contrast is null and stable across both,
with none of the strengthening under confirmation that a real
effect would produce.
Targeted confound checks.Two targeted checks close the
remaining confound channels. Forage, where the two sides
enter the panel at very different points in a video’s life,
we recompute the account-level reach contrast on only the
videos first observed within24h of posting (and within48h).
The contrast stays null on every topic (Trumpδ=−0.27,
p= 0.29; Israel/Palestineδ= 0.13,p= 0.71; ICE
δ= 0.20,p= 0.79at the24h cut), so the age imbalance
is not hiding a reach gap, though these subsets are small.
Forlanguage, ICE and Trump content is almost entirely En-
glish, so the Arabic confound is specific to Israel/Palestine;
stratifying the other two topics by language leaves their
reach nulls unchanged. Finally, because the account median
is the primary estimand we report its support. The median
account-topic unit rests on5videos (range1–164), thin for
ICE (mostly one to three videos per account, another reason
we do not infer from it) and adequate for the informative
topics.
Per-topic constructed null.Figure 5 (Appendix H) shows
the constructed-null false-positive rate at each unit of analy-
sis, pooled and per topic. The naive pooled test rejects al-
most always; the account-level test is calibrated near the
nominal5%.
Multiple-testing sensitivity.Under the pre-registered
Benjamini–Hochberg correction within outcome families,
the engagement effect survives (q= 0.025for Trump,q=
0.021for Israel/Palestine). Under a correction across the six
informative-topic cells it remains below0.05(q= 0.049
and0.043); under the strictest global correction across all
nine grid cells it is borderline (q= 0.073and0.064). No
reach cell is significant under any of the three families.
E Adjusted post-level model
Table 8 details the per-video model oflog(peak plays)
on curated side withlog(followers)andlog(video age)as
controls, standard errors clustered by account (Section 5).
Alongside the cluster-robust Waldpwe report a wild-cluster
bootstrapp(Rademacher weights, null imposed,B= 9,999,
seed fixed), the small-cluster-aware sensitivity appropriate at
a few dozen clusters. No side coefficient is significant under
either test, and the nominally borderline Trump cell (p=
0.07) is clearly null under the bootstrap (p= 0.22), con-
sistent with the known anti-conservatism of cluster-robust
Wald tests at these cluster counts.
F Extended discussion
None of these steps is novel on its own; each is standard
in the literatures on clustered data and researcher degrees
of freedom (Lazic, Clarke-Williams, and Munaf `o 2018; Si-
monsohn, Simmons, and Nelson 2020). What is specific to

Table 4: De-identified roster of the57accounts underlying the account-level tests, one row per account. Handles are withheld
and follower counts are banded so that no account can be joined to a stance and a reach claim; per-topic-side membership
counts reproduce Table 2.
ID Tier Followers Side(s)
A01 3 100K–1M IP·p
A02 3 100K–1M TR·a
A03 3 100K–1M IP·p
A04 1 10–100K IP·i
A05 1 10–100K IP·i
A06 3 100K–1M IP·p
A07 1<10K TR·p
A08 1<10K IP·p
A09 6 1–10M TR·p
A10 3 100K–1M TR·a
A11 1 10–100K TR·a
A12 3 100K–1M IP·p
A13 5 1–10M TR·a
A14 2 100K–1M TR·p
A15 3 100K–1M TR·p
A16 2 10–100K TR·a
A17 2 10–100K IP·p
A18 4 100K–1M IP·p
A19 1<10K IP·p
A20 2 10–100K IP·i
A21 4 100K–1M IP·i
A22 4 1–10M TR·a
A23 3 100K–1M IP·i
A24 5 1–10M TR·a
A25 1<10K TR·p
A26 3 100K–1M IC·a, TR·a
A27 4 1–10M IP·i
A28 1<10K IP·i
A29 1 10–100K IC·p
ID Tier Followers Side(s)
A30 3 100K–1M TR·p
A31 1 10–100K TR·a
A32 2 10–100K IP·i
A33 2 10–100K IC·p, IP·i
A34 2 10–100K IP·i
A35 4 1–10M TR·p
A36 5 1–10M IC·p, TR·p
A37 6>10M TR·p
A38 3 100K–1M IP·i
A39 1 10–100K TR·a
A40 1<10K IC·p, TR·p
A41 2 10–100K IC·a, TR·a
A42 5 1–10M IC·a, TR·a
A43 2 10–100K TR·p
A44 2 10–100K TR·p
A45 3 100K–1M IP·p
A46 3 100K–1M IP·p
A47 1 10–100K IC·a
A48 6>10M TR·p
A49 4 100K–1M IC·p, TR·p
A50 3 100K–1M TR·p
A51 2 10–100K IC·p, TR·p
A52 3 100K–1M IC·a, TR·a
A53 4 1–10M IP·p
A54 3 100K–1M IP·p
A55 4 100K–1M TR·p, IP·i
A56 1<10K IP·i
A57 2 10–100K TR·a
Topic codes IC (ICE), TR (Trump), IP (Israel/Palestine); side·p denotes the pro side (pro-Palestine under IP),·a the anti side, and·i
pro-Israel. Tier runs from1(smallest) to6(largest) follower stratum. Each account appears once and lists every topic it was curated into, so
per-topic-side membership counts reproduce Table 2.
Table 5: Variance components forlog(ViewsPer1K)within
videos on the real on-topic snapshots, reporting the intra-
class correlation (ICC), design effect (Deff), and effective
sample size (Neff).
Topic (within video) Videos Rows ICC DeffN eff
All on-topic 940 173,050 0.98 180 963
ICE 32 11,159 0.97 339 33
TRUMP 458 71,717 0.97 152 471
Israel/Palestine 450 90,174 0.98 196 460
visibility auditing is the order of operations. The unit must
be fixed first, because it is the choice with the largest and
least visible effect on the result, and the design effect must
be reported alongside thep-value, because the two together
are what distinguish an informative sample from a repeated
one. A reader given onlyNandpcannot distinguish the
dense audit we analyze from a thin one inflated by pooling,
which is precisely the confusion on which the shadow-ban
discourse depends.
What would settle the question.Our null is observa-
Table 6: Human validation of the ensemble classifier against
an author-labeled gold set of200stratified videos plus100
videos where the models disagreed on relevance.F 1 is for
the positive/on-topic class (binary tasks) or macro-averaged
(multiclass, marked m);κis Cohen’sκ(binary tasks).
Stratified200Disagreement100
Task AccF 1 κ AccF 1 κ
Relevance (YES/NO)0.91 0.91 0.88 0.82 0.82 0.79
On-topic inclusion0.88 0.88 0.85 0.80 0.80 0.77
Topic (4-class)0.93 0.92 m – 0.990 0.993 m –
tional, and we read it as the absence of evidence at a level the
design can resolve, not as proof of platform neutrality. The
cleanest test is the one the 2020 Facebook and Instagram
studies ran (Guess et al. 2023; Nyhan et al. 2023; Gonz´alez-
Bail´on et al. 2023), randomizing a ranking intervention for
consenting users and measuring the downstream change.
Where the amplification audit of Husz´ar et al. (2022) found a
real but bounded partisan effect on Twitter using a random-

Table 7: Discovery (3–15 Apr)→confirmatory (16–28 Apr)
account-level reach contrast. Null and stable across win-
dows.
Topic Windown a/nb δ p
TRUMP discovery 17/13+0.22 0.32
TRUMP confirmatory 16/13−0.04 0.88
ISR/PAL discovery 12/12+0.17 0.51
ISR/PAL confirmatory 13/12+0.09 0.72
Table 8: Adjusted post-level model oflog(peak plays)on
curated side, withlogfollowers andlogvideo age as con-
trols and account-clustered errors. Coefficients are the log
peak-play difference, establishment minus oppositional side.
Wildpis a wild-cluster bootstrap (Rademacher, null im-
posed,B= 9,999). Cluster-robust SEs are anti-conservative
at these cluster counts (especially ICE,16clusters); no co-
efficient is significant under either test.
Topic Side coding Coef Cluster SE 95% CIpWildpVideos Clusters
ICEPRO−AGAINST0.34 0.86[-1.49,2.16]0.70 0.69 28 16
TrumpPRO−AGAINST0.84 0.47[-0.10,1.79]0.07 0.22 355 37
Israel/PalestinePRO-ISR−PRO-PAL0.45 0.61[-0.79,1.69]0.46 0.56 371 32
ized holdout, our account-level audit finds none for reach
on TikTok, and the contrast is instructive precisely because
both estimate effects at the account level. An external obser-
vational audit, however dense, should be read as a calibrated
bound on the size of any effect, not as a verdict on intent.
Toward auditable platforms.The asymmetry we doc-
ument, that a significant-looking result is easy to produce
and a defensible one is costly, is ultimately an argument for
structured data access. Independent verification of visibil-
ity claims needs sampling frames that fix account size, lan-
guage, and region, and ideally platform-side randomization
or logged exposure. Until such access is routine, the bur-
den falls on analysts to report design effects, effective sam-
ple sizes, and full specification grids, so a reader can see
whether a reported gap survives the choices that produced
it.
G Reproducibility
Every number in this paper is derived from a single statistics
file produced by our analysis pipeline, and the figures are
generated from that file and a small set of tidy per-account
tables. The analysis grid (3 topics×3 outcomes), unit, es-
timators, correction family, and discovery/confirmatory split
were fixed in a pre-registration frozen before any inferen-
tial test; we report every cell with Benjamini–Hochberg cor-
rection and log all deviations against that plan. We will re-
lease the pre-registration, the de-identified analysis code, the
figure-generation scripts, and the derived statistics (with an
anonymized pre-registration reference during review) so that
the full grid, the constructed-null calibration, and the speci-
fication curve can be reproduced and re-examined.
H Additional figures
Nominal 5%
0%
25%
50%
75%
100%
Account Video Video-hour
False-positive rate (constructed null)
Pooled Trump Israel/Palestine
Type-I error climbs as account clusters
are split into pseudo-independent rows
Figure 5: False-positive rate as a function of the analysis
unit, under a constructed null with no true stance effect. Er-
ror is calibrated only at the account level and climbs toward
certainty as the unit is inflated.
Engagement / view
Reach
-1.0 -0.5 0.0 0.5
Cliff's δ  (Pro-Israel − Pro-Palestine)
All videos English-only
English-only leaves reach null;
the engagement gap remains
Figure 6: Israel/Palestine account-level comparison, all
videos vs. English-only. The reach contrast is null in both;
the engagement contrast (pro-Palestine higher) persists.
