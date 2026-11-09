---
title: 'SPILLOVER: Measuring Cyberbullying NormPropagation on Social Media'
url: https://arxiv.org/abs/2607.19646
category: social-media
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Arslan Bisharat
- Katelyn Skees
- Mujtaba Nazari
- Ayaan Khan
- Manuel Sandoval
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.19646
pages: 15
chars: 43925
fetched_at: '2026-11-08T12:59:55+00:00'
kb_version: 1
---

# SPILLOVER: Measuring Cyberbullying NormPropagation on Social Media

SPILLOVER: Measuring Cyberbullying Norm
Propagation on Social Media
Arslan Bisharat1, Katelyn Skees2, Mujtaba Nazari1, Ayaan Khan1, Manny
Sandoval1, Mohammed Abuhamad1, Deborah Hall2, and Yasin Silva1
1 Loyola University Chicago, Chicago, IL, USA
{marslan,mnazari,akhan95,msandovalmadrigal,mabuhamad,ysilva1}@luc.edu
2 Arizona State University, Glendale, AZ, USA
{kskees,d.hall}@asu.edu
Abstract.While certain aspects of cyberbullying (CB) such as its fac-
tors and prevalence have been studied extensively, relatively little at-
tention has been given to specifically how the aggression transfers from
comment to comment. This understanding could have important im-
plications for designing better anti-bullying features. In this paper, we
study multiple aspects of the nature of this aggression transference in so-
cial media sessions. Using data from 32,754 consecutive comment pairs
from 430 Instagram sessions, we find that a preceding CB comment sub-
stantially raises the odds of the next comment being CB, an effect con-
firmed by session fixed-effects controls and driven primarily by cross-
user spread. We also find that CB→CB pairs are more textually sim-
ilar than NoCB→CB pairs across five complementary methods, and
that this pattern holds under a matched cross-session baseline that rules
out shared vocabulary, session toxicity, and session length as confounds.
Moreover, non-aggressive replies grow more negative as preceding CB
severity increases, a graded pattern consistent with automatic emotional
influence below the threshold of overt aggression. These key findings
replicate across three independent datasets (Reddit, Wikipedia Detox,
and SOCC), with spillover rates that track platform visibility design. Fi-
nally, we show that a single binary feature (whether the prior comment
was CB) improves prediction over session-level baselines and over a fine-
tuned HateBERT classifier, serving as a real-time moderation signal that
targets the spreading chain rather than individual offenders.
Keywords:Cyberbullying·Normpropagation·Cyberbullyingspillover
·Social media·Cross-platform analysis
1 Introduction
Cyberbullying (CB) is targeted, repeated online aggression toward a specific
individual with an underlying power imbalance. CB-identified comments are
known to cluster within conversations, suggesting that cyberbullying spills over
into subsequent comments within a post’s comments. Previous work by Kramer
et al.[14] showed that, at the platform level, negative content on Facebook shifts
arXiv:2607.19646v1  [cs.SI]  22 Jul 2026

2 A. Bisharat et al.
subsequent emotional expression and Chenget al.[8] showed that, at the user
level, prior negative mood and conversational context predict trolling beyond
a user’s intrinsic propensity. However, neither study considered how aggression
transfers from comment-to-comment within the same session, which is the gap
that this paper addresses.
The contributions of this paper are:3 ❶the first evidence, to our knowledge,
that CB spillover at the level of comment pairs is content-specific rather than
generically disinhibiting, with convergent support from five similarity methods
and a matched cross-session baseline that controls for shared vocabulary, session
toxicity, session length, and topic;❷a dose-response gradient linking preceding
CB severity to sentiment shift in non-CB replies, consistent with emotional con-
tagion;❸evidence that most cross-user CB→CB commenters are aggressors
rather than victims, which separates norm adoption from retaliation;❹a chain-
length decay curve showing the spillover signal persists two to three steps beyond
the triggering comment;❺cross-platform replication across four datasets with
spillover rates that vary systematically with platform visibility design; and❻a
real-time binary predictor that improves AUPRC over session-level baselines and
over a standalone text classifier, and serves as a directly deployable moderation
signal.
2 Background and Related Work
The field of cyberbullying detection has evolved considerably, from binary clas-
sifiers built on lexical features [9, 22] and deep learning models [1, 7] to severity
measurement through machine-learning classifiers [20] and the use of victim psy-
chological attributes in detection [16], as well as identity-targeted variants such
as LGBTQ+ cyberbullying detection [5] and context-aware attention models
[4]. Most of these models score each comment independently, with few exam-
ining whether conversational context shapes what kind of aggression appears
next. Yet how cyberbullying spills over and through what mechanisms remains
underexplored, given evidence that aggression spreads online [8, 14]. Two psy-
chological mechanisms, in particular, predict how a CB comment may transmit
an aggressive norm within a session.Emotional contagion[11] holds that expo-
sure to negative content triggers automatic negative responses, especially when
reactions are publicly visible, and research confirms this mechanism extends to
online networks [18]. The theory predicts that the emotional tone of a conversa-
tion should shift after CB exposure and that the magnitude of the shift should
scale with the intensity of the exposure.Moral disengagement[2, 6, 15] predicts
that aggressive behavior by one user signals its acceptability to others, allowing
others to displace responsibility for and minimize the perceived consequences of
their own aggressive responses. Indeed, online moral disengagement is directly
associated with cyberbullying perpetration. This theory predicts not just that
other users will become aggressive but that they will adopt the specific content
and style of the preceding aggression. Together, these two mechanisms predict
3 Dataset and code:https://github.com/ysilva/spillover

SPILLOVER: Measuring Cyberbullying Norm Propagation on Social Media 3
a feedback cycle: contagion spreads negative affect while disengagement lowers
inhibition and provides a behavioral template.
3 Analysis and Results
3.1 Dataset and Pair Construction
Our primary data source is an Instagram dataset [12], extended with comment-
level CB severity and topic annotations contributed by our group. The dataset
and code are available athttps://github.com/ysilva/spillover. Each Insta-
gram session consists of a post (an image and its accompanying caption) together
with all comments it received. The corpus contains 1,559 sessions comprising
106,618 comments. Each comment was annotated by five independent annota-
tors on a four-level severity scale (0 = not CB; 1 = mild CB; 2 = moderate CB;
3 = severe CB), with final labels assigned by majority agreement. A comment is
classified as CB if its severity is≥1, and as NoCB otherwise. The CB rate of a
set of comments is the proportion with CB status. The dataset also includes ten
topic labels and seven role labels (bully, bully assistant, non-aggressive victim,
aggressive victim, non-aggressive defender of the victim, aggressive defender of
the victim, and passive bystander). Of the 1,559 sessions, we consider the 430 ses-
sions that contain at least one cyberbullying comment. This restriction is inten-
tional: sessions with no CB comments contribute no CB-initiating events and do
not bear on the spreading mechanism. The measured spillover rate is, therefore,
scoped to sessions where a spreading chain can activate. Within these 430 ses-
sions, we construct consecutive comment pairs(ci−1, ci)ordered by timestamp.
Each pair is characterized by three properties: the CB status of each comment,
the individual severity score (0–3) of each comment, and the time gap between
them. Pairs are categorized by the CB status of both comments: CB→CB,
CB→NoCB, NoCB→CB, and NoCB→NoCB. This process produces 32,754
pairs, which serve as the primary unit of analysis. The pair design isolates the
immediate sequential effect of one comment on the next, the most direct test of
comment-to-comment contagion. Each claim is, therefore, scoped to immediate
sequential spreading rather than long-range dynamics. Because session fixed-
effects regression requires a separate intercept for each session, we restrict that
particular analysis to sessions with≥20 comments, where enough pairs exist to
produce stable estimates. Table 1 summarizes the main dataset statistics. For
the cross-platform analysis, we use three additional datasets where a session cor-
responds to a single submission thread on Reddit, a single talk-page discussion
on Wikipedia Detox, and a single article comment section on SOCC. On Reddit,
pairs are extracted within each thread in reply-chain order to preserve logical
sequential relationships rather than global timestamp order.
3.2 Occurrence-Level Spillover
To the extent that cyberbullying spreads, a comment that follows a CB comment
should be more likely to be CB than one that follows a noCB comment. We

4 A. Bisharat et al.
Type of Pair Pairs (N) CB Rate Mean Severity
CB→CB/NoCB 10,877 49.3% 0.512
NoCB→CB/NoCB 21,877 20.5% 0.338
Difference 28.8pp 0.174
Table 1.Core properties of the Instagram dataset including number of pairs, CB
rates, and mean severity across 32,754 consecutive comment pairs.N= number of
pairs. CB→CB/NoCB denotes pairs where the preceding comment is CB; NoCB→
CB/NoCB denotes pairs where the preceding comment is not CB. CB rate is 2.4×
higher when the prior comment is CB (χ2=2847.3,p<10 −275). pp = percentage points.
measure this as the simple conditional difference:
∆spillover =P(CB i |CB i−1)−P(CB i | ¬CBi−1)(1)
with significance assessed with chi-squared tests and effect sizes reported as Co-
hen’sd. Within the 430 CB-containing sessions, the CB rate in CB→CB/NoCB
pairs was 49.3%, compared to 20.5% in NoCB→CB/NoCB pairs, a 28.8 per-
centage point gap (Table 1). The mean severity was also higher in the CB→CB
condition, though this effect is small by conventional standards (d= 0.212). It
is possible, however, that certain sessions simply attract more aggressive users
and, therefore, produce more consecutive CB comments as a byproduct. In other
words, the raw difference could be an artifact of session-level toxicity rather than
evidence of a real spreading process. To pull apart within-session influence from
between-session differences, we apply three statistical controls. The results of
these analyses are presented in the next sub-sections.
Within-Session V alidation.The raw spillover number conflates two things:
comment-to-commentassociationandthebackgroundtoxicitylevelofthesession
as a whole. Consider a session about a controversial political figure: the higher
likelihood of toxic language throughout may make consecutive CB comments
appear linked even if neither one actually caused the other. To hold session-level
factors including a session’s baseline toxicity constant, we apply two statistical
control strategies. First, astratified analysisdivides sessions into five groups
by their overall CB rate and recomputes the spillover within each group. If the
effectsurvivesevenamonglow-toxicitysessions,itcannotbeexplainedbysession
composition alone. Second, asession fixed-effects logistic regressionprovides the
most rigorous test:
logit

P(CB i)

=α s +β·1[CB i−1](2)
The session interceptα s absorbs all between-session variation (topic, audi-
ence, and overall toxicity level), so the coefficientβcaptures only within-session
influence; that is, each session serves as its own control group. All effects are
validated with permutation tests (1,000 iterations) and bootstrap confidence
intervals (10,000 resamples). The stratified analysis found positive spillover in

SPILLOVER: Measuring Cyberbullying Norm Propagation on Social Media 5
Comment Source CB→CB All post-CB Per-pair CB Rate
Different user 82.9% 90.3% 31.2%
Same user 17.1% 9.7% 59.9%
Table 2.Identity tracking of CB→CB pairs by comment source.CB→CB: fraction
of CB→CB pairs from each source.All post-CB: fraction of all pairs where the
preceding comment is CB (regardless of the following comment’s CB status) from each
source.Per-pair CB Rate: the rate at which the following comment is CB, broken
down by source. Cross-user spread accounts for 83% of CB→CB pairs by volume,
though same-user pairs show a higher per-pair CB rate (59.9% vs. 31.2%).
all five toxicity quintiles (7.4pp–17.7pp across Q1–Q5). Session heterogeneity
is, therefore, not the sole explanation. The fixed-effects model estimated OR
= 1.83(p <10−61), with each session as its own control. As a robustness check,
a lower threshold of≥10 comments per session gives OR= 1.79(p <10 −58).
The result is, therefore, not specific to longer sessions. To test whether the effect
extends beyond the immediate next comment, we definedk-step pairs(ci, ci+k)
fork∈ {1,2,3}wherec i is a CB comment, and computed the conditional CB
rate ofc i+k in each case. The rate decays from 49.3% atk= 1to 35.1% atk= 2
and 26.8% atk= 3, compared to the noCB baseline of 20.5%. This traces a
spreading chain that attenuates rather than immediately extinguishes.
Cross-User Spread versus Persistence.An alternate explanation to rule
out is that a user who posts one CB comment may simply post another, with
CB→CB pairs more accurately reflecting individual persistence than a norm
that extends beyond a single user. To test this, we track user identity across
consecutive pairs and measure what fraction of CB→CB comments come from
a different user. Of the CB comments that followed another CB comment, 82.9%
(95% CI: 81.4%–84.3%) were written by a different user (Table 2). Same-user
pairsdoshowhigherper-pairCBratesbutcross-userspreadaccountsforthevast
majority of cases by volume. To address whether this cross-user spread reflects
victims retaliating rather than new aggressors joining, we examine the role labels
of the second commenter in cross-user CB→CB pairs. Only 3.2% of second
commenters are annotated as victims; 84.4% are bullies or bully assistants. The
cross-user effect, therefore, predominantly reflects new aggressors joining the
aggressive exchange, not victims responding in kind. This pattern aligns with a
moral disengagement account [2] by suggesting that a CB comment lowers the
aggression threshold forotherparticipants rather than just the original poster.
Permutation tests confirmed that the observed spillover exceeds chance (p <
0.001) and the effect is stable across topics and session lengths. Disaggregating
by CB topic using the same conditional OR formula (Eq. 1) applied within each
of the ten topic strata reveals heterogeneity in susceptibility: appearance-based
attacks show the highest within-session spillover (OR= 2.1), followed by racial
and ethnic attacks (OR= 1.9) and political CB (OR= 1.7). This variation
across topics is consistent with the moral disengagement account that norm-
laden contexts lower the aggression threshold more sharply for bystanders.

6 A. Bisharat et al.
0 (NoCB) 1 (Mild) 2 (Moderate) 3 (Severe)
Preceding comment severity
0.25
0.20
0.15
0.10
0.05
0.00
Mean sentiment of
next NoCB comment
d=0.115
d=0.218
d=0.345
Spearman  = 0.112,  p < 10 15
Fig.1.Dose-response gradient: mean sentiment of NoCB replies as a function of pre-
ceding comment severity. Sentiment grows monotonically more negative; the effect size
between severity 0 and severity 3 isd= 0.345.
3.3 Sentiment Shift and Dose-Response
If the spreading is a genuine contagion process rather than generic disinhibition,
then exposure to CB should affect theemotional toneof subsequent comments,
even those that are not, themselves, aggressive. We score sentiment with VADER
and RoBERTa-base-sentiment. The sentiment shift is defined as:
∆sentiment =E[sent(c i)|CB i−1]−E[sent(c i)| ¬CBi−1](3)
This is restricted to NoCB repliesc i, so it captures sub-threshold emotional
leakage rather than overt aggression. The dose-response test then checks whether
the shift scales with the severity of the preceding comment (s∈ {0,1,2,3}). This
distinction is critical: an artifact driven by topic or user selection would produce
a uniform increase in negativity, not a graded one. Indeed, noCB comments that
followed a CB comment were detectably more negative (d= 0.115,p <10−13; a
small effect by conventional standards), a finding confirmed by both RoBERTa
and VADER. The dose-response gradient (Fig. 1) shows that sentiment grows
monotonically more negative across all four severity levels (0 through 3); the
effect size between the lowest and highest severity levels isd= 0.345. Given that
a confound driven by shared context would produce a uniform shift rather than
a graded one, this pattern is consistent with a genuine spillover effect rather
than a shared-context artifact.
3.4 Content-Level Spreading
Because emotional tone shifts on their own do not prove that specificcon-
tenttransfers, a more stringent test is whether the topics and language of CB
carry over from one comment to the next. That is, if cyberbullying spillover is

SPILLOVER: Measuring Cyberbullying Norm Propagation on Social Media 7
Method CB→CB NoCB→NoCB NoCB→CBd 1 d2 XUd
TF-IDF cosine 0.112 0.060 0.044 0.418 0.276 0.328
Word Jaccard 0.085 0.049 0.030 0.472 0.242 0.450
Char 3-gram 0.098 0.053 0.039 0.508 0.305 0.506
MiniLM-L6-v2 0.335 0.249 0.224 0.655 0.449 0.588
MPNet-base-v2 0.357 0.253 0.232 0.707 0.533 0.641
Table 3.Mean pairwise text similarity for consecutive comment pairs across five meth-
ods. NoCB→NoCB is used as a general conversational coherence baseline.d1: Cohen’sd
for CB→CB vs NoCB→CB;d2: Cohen’sdfor CB→CB vs NoCB→NoCB; XUd: cross-
user pairs only (d1). NoCB→NoCB pairs are slightly more similar than NoCB→CB
pairs, confirming a small general conversational coherence effect. CB→CB similarity
exceeds this baseline by a factor of2–3. Allp<10−100.
content-specific, then CB→CB pairs should be more linguistically similar than
NoCB→CB pairs. We study content transfer using five methods spanning lex-
ical and semantic representations. The three lexical methods (TF-IDF cosine,
word Jaccard, character 3-gram) share surface-level vocabulary signal and are
treated as one convergent line of evidence. The two neural sentence encoders
(MiniLM-L6-v2 [17] and MPNet-base-v2 [19]) capture semantic similarity inde-
pendently of exact word overlap and constitute a second, independent line of
evidence. We compare text similarity between CB→CB and NoCB→CB
pairs. Both pair types are drawn from the same sessions, so any shared session
vocabulary affects both equally. A content-transfer process would predict a con-
sistent CB→CB advantage. All five text similarity methods confirmed that
CB→CB pairs are more textually similar than NoCB→CB pairs (Table 3),
with effect sizes fromd= 0.42tod= 0.71. These effects persist after remov-
ing same-author pairs (d= 0.33–0.64for cross-user only). To assess whether
the elevated CB→CB similarity reflects something specific to cyberbullying or
merely general conversational coherence, we include NoCB→NoCB pairs as a
third reference condition. NoCB→NoCB pairs are slightly more similar than
NoCB→CB pairs (d= 0.11–0.17). This confirms a small background coher-
ence effect: conversations, in general, tend to stay somewhat on-topic. However,
CB→CB similarity substantially exceeds this background level (d= 0.24–0.53
across all five methods; Table 3), an excess2–3×larger than the general same-
type coherence. The within-type similarity advantage is not simply a property
of consecutive comments sharing a topic; it is markedly stronger for cyberbul-
lying transitions. Users are not just becoming generically aggressive after expo-
sure to CB: they adopt the specific language and style of the preceding aggres-
sion to a degree that exceeds ordinary conversational drift. Together with the
dose-response gradient, this pattern is consistent with content-specific contagion
rather than generic disinhibition.
Ruling Out V ocabulary Confounds.A natural objection to the content
similarity finding is a shared-label vocabulary confound: CB comments may ap-
pear similar to each other simply because both are CB and, therefore, share

8 A. Bisharat et al.
the aggressive vocabulary common to cyberbullying, not because one caused the
other. We construct a matched cross-session baseline to test this directly. For
each within-session CB→CB pair, we retain the preceding comment but replace
the following CB comment with a randomly-sampled CB comment drawn from
adifferentsession. Both the within-session and cross-session groups, therefore,
contain two CB comments. To ensure a fair comparison, we stratify sessions into
five quintile bins on CB rate and five quintile bins on session length to form
25 match cells, then sample replacement comments from the same cell. We run
1,000 independent bootstrap samples and average scores across samples for sta-
bility. This produces four comparison conditions: unmatched, toxicity-matched,
fully-matched (toxicity and length combined), and the standard NoCB→CB
baseline. Within-session CB→CB pairs remain substantially more similar than
the fully-matched cross-session baseline across all five methods (d= 0.51–1.03,
allp≈0). The marginal contribution of each matching dimension is small:
adding toxicity matching shifts the baseline byd= 0.04–0.13and adding length
matching adds a furtherd= 0.04–0.07. This means that even the unmatched
cross-session comparison already controlled for the bulk of compositional differ-
ences; the main effect is robust to both confounds (CB rate and session length).
To test whether shared topic labels drive any residual gap, we additionally re-
strict to pairs that share at least one topic label and apply the same matching
procedure within each topic. This topic-stratified ablation producesd= 0.61–
1.13, larger than the unrestricted estimate because it isolates pairs where topic
alignment is guaranteed on both sides. The consistent within-session advantage
across all conditions makes shared aggressive vocabulary, session toxicity, length,
or topic unlikely as the primary drivers of the elevated similarity, though obser-
vational data cannot fully rule out unobserved confounders.
3.5 Spreading-A ware Prediction
If the spreading signal is real, it should improve the ability to anticipate CB
before it occurs. We frame this as a binary classification task: can we predict
whetherc i is CBwithout access toc i’s text? We test three conditions. The
sole-signalcondition uses a single binary feature: was the prior comment CB?
Thebaselinemodel uses 7 session-level features (position, session length, time
elapsed,etc.). TheCB-signalmodel adds the binary CB-status feature to the
baseline. Because the positive class is rare (9.2%), we report Average Preci-
sion (AUPRC) as the primary metric: a random classifier would attain AUPRC
equal to the prevalence (0.092). Gains are, therefore, directly interpretable as
improvement over chance. All conditions are tested on Logistic Regression, Ran-
dom Forest, and Gradient Boosting with 5-fold session-grouped cross-validation.
Improvements are assessed with pairedt-tests on fold-level AUPRC. Used alone,
the prior comment’s CB status attains AUPRC= 0.289(a 3.2×lift above the
random baseline of 0.092) and ROC-AUC= 0.72. This confirms the spillover sig-
nal carries genuine predictive information even in isolation. When added to the
session-level baseline, this single binary feature improves AUPRC by+0.031–
+0.037(+6.6–8.2%;p <0.01across all three classifiers). A per-feature abla-

SPILLOVER: Measuring Cyberbullying Norm Propagation on Social Media 9
Model Met. Baseline +CB Status∆ 1 +Content∆ 2
Logistic Regression AUC 0.713 0.740 +0.027∗∗∗ 0.740 <0.001n.s.
Random Forest AUC 0.705 0.732+0.027 ∗∗∗ 0.740+0.008 ∗∗∗
Gradient Boosting AUC 0.684 0.716 +0.032∗∗∗ 0.727 +0.012n.s.
Gradient Boosting F1 0.292 0.339+0.047 ∗∗∗ 0.374+0.035 ∗∗
Table 4.Spillover-aware CB prediction: three-condition ablation across classifiers.
Adding the CB status of the prior comment (+CB Status) is the primary driver of im-
provement; content features (+Content) add a small further increment.∆1 = gain over
Baseline;∆ 2 = gain over +CB Status.∗∗∗p <0.001; ∗∗p <0.01; n.s.=not significant.
Pairedt-tests on 5-fold AUC/F1 scores.
Model AUPRC∆
Sole signal (prev_is_cbonly) 0.289 –
HateBERT (text only) 0.710 –
HateBERT +prev_is_cb 0.740 +0.030∗∗
Table 5.HateBERT integration: addingprev_is_cbto a fine-tuned HateBERT clas-
sifier. The spillover signal captures information orthogonal to comment text.
tion across five candidate predecessor features confirms thatprev_is_cbis the
only feature that is positive and statistically significant across all three classi-
fiers; timing, authorship, and text-length features are inconsistent or near zero
(Table 4). The spillover signal should be used as a complement to text-based
classifiers, not a replacement. Practically, the use of this signal could be help-
ful for early detection of cyberbullying and proactive moderation. To verify the
signal is orthogonal to text-level evidence, we fine-tuned a HateBERT [7] classi-
fier on the same 430-session folds (3 epochs, learning rate2×10−5, batch size 16;
prev_is_cbwas appended as a binary feature to the pooled [CLS] representation
before the final classification layer). As Table 5 shows, HateBERT alone attains
AUPRC= 0.71; addingprev_is_cbas a single additional feature raises this
to0.74(+0.03,p <0.01). The spillover signal, therefore, captures information
orthogonal to comment text.
3.6 Cross-Platform Replication
The results discussed thus far came from Instagram, whose flat comment layout
and younger users may amplify the effect. Our final analysis tested the gen-
eralizability of the key findings across three additional platforms with different
interaction designs. Specifically, we performed the core spillover, content similar-
ity, and identity analyses on Reddit [3] (threaded comments from five subreddits
spanning news, politics, and community discussion; 2015–2019; 314,588 pairs),
Wikipedia Detox [21] (English page discussions; 2004–2015; 63,155 pairs) and
SOCC [13] (Globe & Mail news comments; 2012–2016; 338,909 pairs). Because

10 A. Bisharat et al.
Platform Pairs Sessions Lift ContentdCross-Userp-value
InstaCTSR 32,754 430 1.83× 0.42–0.71 82.9% <10 −61
Wikipedia Detox 63,155 15,789 1.95×0.537 100.0%<10 −275
SOCC (Globe & Mail)338,909 3,703 1.42× 0.362 93.8% <10 −61
Reddit (5 subreddits) 314,588 2,440 1.26×0.264 97.6%<10 −124
Table 6.Cross-platform replication of the spillover effect. Lift = ratio of CB rate
after CB to CB rate after NoCB. Contentd= Cohen’sdfor text similarity between
CB→CB and NoCB→CB pairs (word Jaccard for Reddit, overall for others). Cross-
User = percentage of CB→CB pairs from different users.
these datasets lack human severity annotations, the toxicity labels are generated
with the Detoxify unbiased classifier [10] at a threshold of 0.5. Detoxify’s toxi-
city construct is broader than cyberbullying, which requires targeted harm and
repetition; the cross-platform findings, therefore, reflect toxicity spillover and
should be interpreted with that scope in mind. To validate label consistency,
we applied Detoxify to the Instagram data and compared its predictions against
human annotations. The comparison gives AUC= 0.91, which supports treating
the automated labels as a reasonable proxy for the cross-platform analyses. The
cross-platform results are also robust to threshold choice: repeating all analy-
ses at thresholds of 0.3 and 0.7 gives spillover ORs within 0.08 of the values
reported at 0.5 across all three platforms. This rules out threshold sensitivity
as an explanation for the observed effects. The spillover effect replicated on all
three platforms (allp <10−61, Table 6). Wikipedia Detox showed the strongest
lift (1.95×), followed by SOCC (1.42×) and Reddit (1.26×). This ordering ef-
fect tracks platform design: Wikipedia talk pages and SOCC comment sections
display comments in a linear layout where prior content stays visible and suscep-
tibility to contagion is high. Reddit’s nested threading distributes replies across
sub-threads and dilutes the sequential signal. The lift’s systematic variation with
users’ prior content exposure supports a visibility-driven contagion mechanism.
Content-level spreading also replicated on all platforms (Table 6) and cross-user
spread was the primary driver on every platform (90–100%; the 100% figure
for Wikipedia Detox reflects the structural constraint that Wikipedia edits are
always by different users).
4 Discussion
Not Just More, But Alike.Cyberbullyingclusteringinonlineconversations
is well known. This paper provides new evidence of immediate comment-to-
comment spillover within conversations; our content-level analyses suggest that
this spillover is not a session-level artifact. Whereas prior work has shown that
exposure to aggression makes more aggression likely [8, 14], our findings suggest
that it makesthe same kindof aggression likely. CB→CB pairs are more tex-
tually similar than NoCB→CB pairs across five methods spanning lexical and

SPILLOVER: Measuring Cyberbullying Norm Propagation on Social Media 11
semantic representations and this holds after the removal of same-author pairs.
A shared situational trigger would elevate CB rates without the texts becoming
more alike, but the textsaremore alike. Critically, including NoCB→NoCB
pairs as a baseline reveals that CB-specific within-type similarity (d= 0.24–0.53
above the NoCB→NoCB level) is2–3×larger than the general conversational
coherence effect (d= 0.11–0.17). This rules out the possibility that the finding
merely reflects topic drift common to all same-type pairs. This illustrates an
important distinction between generic disinhibition (whereby exposure to ag-
gression increases subsequent aggression, broadly) and content-specific spillover
(where, for example, exposure to a religion-based attack increases the likelihood
of a subsequent religion-based attack). This distinction has direct consequences
for cyberbullying classifiers. Most severity classifiers score comments indepen-
dently of conversational context, capturing a snapshot of the text but not the
conversational process that shaped it. If CB spillover shapes the language of sub-
sequent comments, then severity labels may partly reflect conversational history
ratherthanthetextalone,ahypothesistestablebypresentingthesamecomment
to annotators in different conversational contexts. Our HateBERT experiment
shows that preceding CB status is not fully captured by the comment text, so
incorporating it as a contextual feature offers a direct model improvement.
Interpreting the Evidence.Whereasobservationaldatacannotconclusively
establish causation, our findings offer evidence that goes beyond mere associa-
tion. The common-cause alternative, that unobserved time-varying confounders
independently and chiefly effect consecutive comments, is difficult to reconcile
with three features of the data. First, the sentiment shift scales monotonically
with preceding severity (the dose-response gradient). A common cause would el-
evate aggression uniformly regardless of the preceding comment’s severity level,
not produce a graded pattern. This graded pattern is more consistent with gen-
uine spillover than with a session-level artifact. Second, the content similarity
results show that CB→CB pairs are not just more frequent but more textually
similar. CB→CB similarity exceeds the background conversational coherence
established by NoCB→NoCB pairs by a factor of2–3, a gap that a common-
cause account driven by shared topic or session context alone would not predict.
Third, the matched cross-session baseline confirms that the similarity advan-
tage cannot be attributed to shared aggressive vocabulary, session toxicity, ses-
sion length, or topic alignment. Within-session pairs remain substantially more
similar than the matched cross-session comparison (d= 0.51–1.03, allp≈0),
and the topic-stratified ablation strengthens rather than weakens this finding
(d= 0.61–1.13). These three lines of evidence, together with the cross-platform
replication, are collectively more consistent with a genuine spillover effect than
with common-cause alternatives. The spillover rate also varies with platform de-
sign: strongest on linear-comment platforms (Wikipedia: 1.95×, SOCC: 1.42×)
and weakest on Reddit (1.26×), where threading dilutes sequential exposure. A
statistical artifact would not co-vary systematically with platform design.
Implications.The present findings are consistent with both emotional conta-
gion and moral disengagement, though observational data cannot establish these

12 A. Bisharat et al.
mechanisms conclusively. Emotional contagion [11, 18] predicts that exposure to
negativity triggers automatic negative responses that scale with the intensity
of exposure. The observed dose-response gradient aligns with this prediction:
even noCB comments become more negative after CB exposure, and the effect
tracks severity. Moral disengagement [2, 6, 15] predicts that modeled aggression
provides permission and a behavioral template. Content similarity results are
consistent with users adopting specific themes and language of preceding ag-
gression, not just general negativity. The cross-user finding (82.9% of successive
CB from different users) is consistent with moral disengagement, as prior com-
ments may lower the aggression threshold for others. The prediction analysis
shows that there is a usable signal in the conversational context. A single binary
feature (whether the prior comment was CB) attains AUPRC=0.289 in isola-
tion (3.2×above chance) and improves AUPRC by+0.031–+0.037when added
to a session-level baseline (p <0.01across all classifiers). This opens the door
to conversation-level interventions. At a threshold of 0.40, the sole-signal model
attains precision 0.38 and recall 0.51 on held-out folds; approximately 62% of
flagged comments are false positives, soprev_is_cbis best used as a priority
signal to focus reviewer attention rather than as an automatic block. One further
caveat for deployment is adversarial adaptation: if users learn that inserting a
noCB comment resets the signal, they may do so to break the detection chain,
a standard arms-race concern for any rule-based moderation trigger. Content
downranking could break the transmission chain by reducing the visibility of
a comment. Warning labels could counteract moral disengagement by making
other users more explicitly aware of aggressive content and an emerging pattern
within asession. Allofthesetargetthe spreadingmechanismrather thanany sin-
gle offender. Notably, within-session analyses show that the spillover effect does
not decay with the time gap between comments. This pattern is more consis-
tent with content visibility than with emotional urgency as the primary driver,
though both may operate simultaneously. Content-level interventions such as
warnings, downranking, and flagging are, therefore, likely to be more actionable
than timing-based constraints alone.
Limitations.The primary Instagram dataset was collected in 2012–2014; plat-
form interfaces and moderation policies have since evolved. While cross-platform
replication (Reddit, Wikipedia Detox, and SOCC) supports generalizability,
these external datasets use Detoxify automated labels rather than human anno-
tation. Detoxify attains≥0.95 AUC on its test set and the directional findings
replicate those from human-annotated Instagram data. The unit of analysis in
this work is the consecutive comment pair, capturing immediate sequential in-
fluence but not longer-range trajectories. We extend to three-step chains, but
graph-based analyses could reveal dynamics beyond this window. Two confounds
bear on the content similarity results. For shared aggressive vocabulary, the
matched cross-session baseline addresses this directly: within-session pairs re-
main more similar than matched cross-session pairs (d= 0.51–1.03) and the
topic-stratified ablation (d= 0.61–1.13) rules out shared topic labels. For tem-
poral escalation, the dose-response gradient scales with the severity of the imme-

SPILLOVER: Measuring Cyberbullying Norm Propagation on Social Media 13
diately preceding comment rather than session stage, and the 82.9% cross-user
spread indicates the effect holds across different participants. Experimental vali-
dation remains the definitive next step. A within-session time-varying confound
also warrants acknowledgment: a viral post or trending controversy could drive
many users to comment aggressively in rapid succession without any transmis-
sion between comments. The session fixed-effects model absorbs between-session
variation but does not eliminate this within a session. The dose-response gradi-
ent and the matched cross-session baseline provide partial evidence against this
alternative, but only a controlled experiment can fully rule it out.
F uture W ork.Although our cross-platform replication confirms that the spill-
over effect generalizes, the observational evidence warrants further investiga-
tion to more conclusively establish causation. A natural next step is random-
ized content-delay interventions with platform partners, which could examine
whether breaking the transmission chain actually reduces downstream aggres-
sion. Ephemeral platforms like Snapchat and real-time interactions like gaming
chat remain untested and may reveal different spreading dynamics, given that
message persistence and visibility differ from the comment threads studied here.
Finally, user-specific psychological and demographic factors [16] could reveal who
is most susceptible to content-level contagion.
5 Conclusion
Whereaspriorworkhasshownthatonlinetoxicityclusters,thispapershowsthat
cyberbullying, a more specific construct than general online toxicity, spills over
immediately from one comment to the next within conversations and that this
spillover is content-specific. Across 32,754 comment pairs from 430 Instagram
sessions, cyberbullying occurrence spreads within conversations (OR= 1.83,
p <10−61) and the effect is primarily cross-user (82.9% of successive CB comes
from different users). Content-level analyses provide evidence consistent with
genuine content-specific spillover. CB→CB pairs are more textually similar
than NoCB→CB pairs across five similarity methods spanning lexical and
semantic representations (d= 0.42–0.71), sentiment in non-aggressive replies
shifts in proportion to preceding severity (d= 0.345), and these patterns repli-
cate across Reddit, Wikipedia Detox, and SOCC with spillover rates that track
platform design (1.26×to 1.95×). A single binary feature (whether the prior
comment was CB) attains AUPRC=0.289 as the sole predictor (3.2×above the
random baseline of 0.092), improves AUPRC by+0.031–+0.037when added to
a session-level baseline (p <0.01across three classifiers), and raises a fine-tuned
HateBERT classifier from 0.71 to 0.74 (+0.03,p <0.01), orthogonal to comment
text. This translates the spillover effect into a real-time moderation signal for
early cyberbullying detection and proactive moderation.
Acknowledgements.This research was supported in part by National Science
Foundation Awards No. 2435164 and No. 2435165, a Google Award for Inclusion
Research, and a Lambda Research Grant.

Bibliography
[1] Agrawal, S., Awekar, A.: Deep learning for detecting cyberbullying across
multiple social media platforms. In: Advances in Information Retrieval: 40th
European Conference on IR Research, ECIR 2018. pp. 141–153 (2018)
[2] Bandura, A.: Moral disengagement in the perpetration of inhumanities. Per-
sonality and Social Psychology Review3(3), 193–209 (1999)
[3] Baumgartner, J., Zannettou, S., Keegan, B., Squire, M., Blackburn, J.: The
pushshift Reddit dataset. In: Proceedings of the International AAAI Con-
ference on Web and Social Media. vol. 14, pp. 830–839 (2020)
[4] Bisharat, A., Sandoval, M., Nazari, M., Hall, D.L., Abuhamad, M., Silva,
Y.N.: SpectrumNet: Detecting LGBTQ+ cyberbullying with dynamic
context-aware attention. In: Proceedings of the International AAAI Con-
ference on Web and Social Media (ICWSM). vol. 20, pp. 276–290 (2026).
https://doi.org/10.1609/icwsm.v20i1.42638
[5] Bisharat, A., Sandoval Madrigal, M., Abuhamad, M., Hall, D.L., Silva,
Y.N.: Detecting LGBTQ+ instances of cyberbullying. arXiv preprint
arXiv:2409.12263 (2024)
[6] Bussey, K., Fitzpatrick, S., Raman, A.: The role of moral disengagement
and self-efficacy in cyberbullying. Journal of School Violence14(1), 30–46
(2015)
[7] Caselli, T., Basile, V., Mitrović, J., Granitzer, M.: Hatebert: Retraining
bert for abusive language detection in english. In: Proceedings of the 5th
Workshop on Online Abuse and Harms (WOAH 2021). pp. 17–25 (2021)
[8] Cheng, J., Bernstein, M., Danescu-Niculescu-Mizil, C., Leskovec, J.: Anyone
can become a troll: Causes of trolling behavior in online discussions. In: Pro-
ceedings of the 2017 ACM Conference on Computer Supported Cooperative
Work and Social Computing. pp. 1217–1230 (2017)
[9] Dinakar, K., Reichart, R., Lieberman, H.: Modeling the detection of textual
cyberbullying. In: Proceedings of the International AAAI Conference on
Web and Social Media. vol. 5, pp. 11–17 (2011)
[10] Hanu, L., Unitary team: Detoxify.https://github.com/unitaryai/
detoxify(2020)
[11] Hatfield,E.,Cacioppo,J.T.,Rapson,R.L.:Emotionalcontagion.Cambridge
University Press (1994)
[12] Hosseinmardi, H., Mattson, S.A., Rafiq, R.I., Han, R., Lv, Q., Mishra, S.:
Detection of cyberbullying incidents on the instagram social network. arXiv
preprint arXiv:1503.03909 (2015)
[13] Kolhatkar, V., Wu, H., Cavasso, L., Francis, E., Shukla, K., Taboada, M.:
The SFU opinion and comments corpus: A large-scale dataset with anno-
tations for stance, constructiveness and toxicity. Corpus Pragmatics4(2),
155–190 (2020)

SPILLOVER: Measuring Cyberbullying Norm Propagation on Social Media 15
[14] Kramer, A.D., Guillory, J.E., Hancock, J.T.: Experimental evidence of
massive-scale emotional contagion through social networks. Proceedings of
the National Academy of Sciences111(24), 8788–8790 (2014)
[15] Paciello, M., Tramontano, C., Nocentini, A., Fida, R., Menesini, E.: The
role of traditional and online moral disengagement on cyberbullying: Do
externalising problems make any difference? Computers in Human Behavior
103, 190–198 (2020).https://doi.org/10.1016/j.chb.2019.09.024
[16] Prama, T.T., Amrin, J.F., Anwar, M.M., Sarker, I.H.: Ai-enabled user-
specific cyberbullying severity detection with explainability. SSRN Preprint
(2025).https://doi.org/10.2139/ssrn.5167003
[17] Reimers, N., Gurevych, I.: Sentence-BERT: Sentence embeddings using
Siamese BERT-networks. In: Proceedings of the 2019 Conference on Em-
pirical Methods in Natural Language Processing. pp. 3982–3992 (2019)
[18] Rosenbusch, H., Evans, A.M., Zeelenberg, M.: Multilevel emotion trans-
fer on YouTube: Disentangling the effects of emotional contagion and ho-
mophily on video audiences. Social Psychological & Personality Science
10(8), 1028–1035 (2019).https://doi.org/10.1177/1948550618820309
[19] Song, K., Tan, X., Qin, T., Lu, J., Liu, T.Y.: MPNet: Masked and permuted
pre-training for language understanding. In: Advances in Neural Informa-
tion Processing Systems. vol. 33, pp. 16857–16867 (2020)
[20] Talpur, B.A., O’Sullivan, D.: Cyberbullying severity detection: A machine
learning approach. PLoS ONE15(10), e0240924 (2020).https://doi.org/
10.1371/journal.pone.0240924
[21] Wulczyn, E., Thain, N., Dixon, L.: Ex machina: Personal attacks seen at
scale. In: Proceedings of the 26th International Conference on World Wide
Web. pp. 1391–1399 (2017).https://doi.org/10.1145/3038912.3052591
[22] Xu, J.M., Jun, K.S., Zhu, X., Bellmore, A.: Learning from bullying traces in
social media. In: Proceedings of the 2012 Conference of the North American
ChapteroftheAssociationforComputationalLinguistics:HumanLanguage
Technologies. pp. 656–666 (2012)
