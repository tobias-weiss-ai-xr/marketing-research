---
title: 'ChildSafeAds Shared Task 2026: Commercial Content in Child-Facing YouTube Videos'
url: https://arxiv.org/abs/2608.19165
category: digital-marketing
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Thales Bertaglia
- Catalina Goanta
- Gerasimos Spanakis
- Gunes Acar
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.19165
pages: 9
chars: 39068
fetched_at: '2026-11-08T13:19:59+00:00'
kb_version: 1
---

# ChildSafeAds Shared Task 2026: Commercial Content in Child-Facing YouTube Videos

ChildSafeAds Shared Task 2026: Commercial Content in Child-Facing
YouTube Videos
Thales Bertaglia1* Catalina Goanta1 Gerasimos Spanakis2 Güne¸ s Acar3
1Utrecht University, Netherlands
2Maastricht University, Netherlands
3Radboud University, Netherlands
Abstract
CHILDSAFEADS 1 is a shared task on commer-
cial content in YouTube videos likely to reach
children and teenagers. The dataset contains
3,360 videos from 939 channels, each starting
with a sponsor segment submitted to Sponsor-
Block. We pair each segment with its transcript,
video, and channel information, plus a sales or
service page linked from the video description.
Systems determine the type of offer being pro-
moted (ST1), assign product categories (ST2),
and identify potential legal risks (ST3). Evi-
dence is divided into four cumulative access
levels, from the transcript to the linked page, so
performance can be compared against the cost
of collecting additional data. YouTube’s “In-
cludes paid promotion” label was absent from
45.5% of the videos. GPT-5.4 produced the la-
bels after the organiser team, including a legal
expert, reviewed samples and iterated on the
taxonomy, prompts and model choices. GPT-
5.6-luna independently labelled the develop-
ment set to measure cross-model agreement.
The evaluation received 21 entries; the high-
est mean macro-F1 was 0.735, while the best
transcript-only entry reached 0.652. Across
four system papers, the linked promotional
page mainly helped identify what was being
sold and added little to compliance-risk classi-
fication. The competition also exposed sensi-
tivity to rare labels, advertiser overlap across
splits and substantial variation in the ST3 la-
bels.
1 Introduction
Advertising on YouTube often appears inside the
video itself, delivered by the same creator and in
the same style as the surrounding content. Chil-
dren and teenagers can struggle to recognise this
form of commercial persuasion (De Veirman et al.,
*Corresponding author:t.f.costabertaglia@uu.nl
1The competition is available on CodaBench: https://
www.codabench.org/competitions/17595/.
2019; Loose et al., 2023). Disclosure is also incon-
sistent across countries and platforms (Bertaglia
et al., 2025; Gui et al., 2025b). An audit of affiliate-
sponsored YouTube videos found a disclosure in
about 10% of cases (Mathur et al., 2018). Au-
thorities seeking to monitor this content at scale
cannot begin with disclosures alone. SponsorBlock
provides candidates independent of platform dis-
closure. It is an open-source crowdsourced browser
extension and public API for skipping sponsor seg-
ments in YouTube videos.2 A contributor marks
where a sponsorship starts and ends; other users can
vote on the submission, and the extension skips ac-
cepted segments automatically. The resulting pub-
lic database provides an independent signal that a
video may contain commercial content. YouTube’s
own “Includes paid promotion” label was absent
from 45.5% of the videos in our data, so a monitor-
ing system relying only on that label would miss
many relevant candidates.
Once a candidate segment has been found, three
questions follow. What is being promoted? What
type of product is it? What aspects of the promotion
need closer legal review? CHILDSAFEADSturns
these questions into three linked classification tasks.
Systems can work from the transcript alone or add
video metadata, channel information and the linked
promotional page. Every submission records which
evidence it used, so the shared task can compare
accuracy at different levels of data access and cost.
The evaluation received 21 entries. The highest
mean macro-F1 was 0.735, and the best transcript-
only system reached 0.652. The four system papers
for the task go beyond that leaderboard comparison.
In their experiments, the linked promotional page
mainly helps identify the offer and product. It adds
little to compliance-risk classification, and chan-
nel information brings no measurable gain in the
systems that test it. Running the competition also
2https://sponsor.ajay.app/.
arXiv:2608.19165v2  [cs.CL]  26 Sep 2026

exposed weaknesses in the benchmark itself: very
rare labels carry a large weight in the metric, adver-
tisers recur across splits, and some compliance-risk
labels are unstable.
We first set out the legal context and the tasks,
then describe how we built and evaluated the
dataset, and close with the participating systems
and what they found.
2 Legal Context
The labels draw on EU consumer and audiovisual
advertising law, limited to what the released data
allow us to infer. ST1 describes what the con-
sumer receives, using distinctions from the Con-
sumer Rights Directive (CRD) (European Parlia-
ment and Council of the European Union, 2011).
ST3 draws mainly on the Unfair Commercial Prac-
tices Directive (UCPD), Audiovisual Media Ser-
vices Directive (A VMSD) and Digital Services Act
(DSA) (European Parliament and Council of the
European Union, 2005, 2010, 2022).
The ST3 flags fall into three groups. Disclosure
flags ask whether the audience can recognise the
content’s commercial nature. UCPD Article 5(3)
requires the assessment to account for an identi-
fiable vulnerable group, so disclosure clear to an
adult may still be inadequate for children. The
main legal references are UCPD Articles 6–7 and
Annex I point 11, A VMSD Articles 10–11 and 28b,
and DSA Articles 26 and 28. We label a promo-
tion asundisclosed advertisingwhen the available
transcript, description and platform field contain
no disclosure.Inadequate disclosureapplies when
a disclosure is present but may not be clear enough
for the intended audience.
Content flags cover misleading claims and di-
rect exhortation. UCPD Articles 6–7 address mis-
leading actions and omissions. Annex I point 28
prohibits directly urging children to buy a prod-
uct or persuade an adult to buy it for them. We
use a narrow test: language that pressures a child
to make the purchase happen qualifies, while a
generic instruction to click a link, download an app
or use a code does not. Product flags cover age-
restricted or prohibited products and the marketing
of foods high in fat, salt or sugar, grounded mainly
in A VMSD Article 9 and DSA Article 28.
The released data include files that map each flag
to the relevant provisions and explain the connec-
tion. They provide citations and notes rather than
reproducing the law verbatim. The flags indicate
cases for further review. They do not capture every
fact needed for a legal assessment, and a flag is not
a finding of infringement.
3 Related Work
Research on influencer advertising has measured
disclosure practices across platforms and coun-
tries and studied how children and teenagers recog-
nise commercial persuasion (Mathur et al., 2018;
Bertaglia et al., 2025; Gui et al., 2025b; De Veir-
man et al., 2019; Loose et al., 2023). Related work
examines children’s economic exploitation, adoles-
cent advertising literacy and food marketing (van
der Hof et al., 2020; Zarouali et al., 2020; Martínez-
Pastor et al., 2021). These studies establish why
disclosure and product type matter for child-facing
content, but they do not provide a benchmark for
classifying both from the same videos.
Computational work has detected sponsored
YouTube segments and used model explanations
to support human labelling and assess influencer-
marketing compliance (Rodrigues et al., 2021;
Bertaglia et al., 2023; Gui et al., 2025a). CHILD-
SAFEADSuses SponsorBlock’s crowd-submitted
segment boundaries for discovery and focuses
on classifying the resulting cases. In legal NLP,
LexGLUE benchmarks legal text analysis and
legal knowledge (Chalkidis et al., 2022), while
consumer-law research connects legal rules to data-
driven analysis (Lippi et al., 2020). Recent work
also combines legal analysis with platform data to
audit DSA transparency (Kaushal et al., 2024) and
youth safety (Xue et al., 2025).
The closest shared-task precedent is LegalLens,
which links the detection of legal violations in
ordinary text to supporting legal provisions (Ha-
gag et al., 2024). CHILDSAFEADSfollows the
same structure, connecting evidence from a video,
the platform and the promoted product to a set of
legally grounded labels.
4 Task Definition
Each CHILDSAFEADSinstance starts with a crowd-
submitted SponsorBlock interval: a start and end
time within a YouTube video where a contributor
identified a sponsorship. The dataset also includes
the words spoken during that interval, information
about the video and channel, and one likely sales
or service page linked from the video description.
Systems do not decide whether the segment is com-
mercial or whether the channel is child-facing; both

are defined when the dataset is built.
The three tasks share the same instances and evi-
dence. Teams may enter any subset. Because every
instance begins with a SponsorBlock mark, the
benchmark does not evaluate commercial-content
detection and contains no non-commercial exam-
ples.
ST1: Commercial type.ST1 asks what the con-
sumer receives through the promoted transaction.
It assigns one of five labels:physical goods,digital
content or services,physical services,no identifi-
able offer, orother.
ST2: Product category.ST2 asks what kind
of product is being promoted. It assigns one or
more of twelve categories covering apps, hardware
and electronics, food, fashion, health, education,
financial products, gambling, gambling-adjacent
mechanics, toys, creator communities and other
products.
ST3: Compliance-risk indicators.ST3 asks
which aspects of the promotion potentially require
closer legal review. It assigns any of six flags: mis-
leading claim, inadequate disclosure, undisclosed
advertising, direct exhortation, age-restricted or
prohibited product, and marketing for foods high
in fat, salt or sugar (HFSS). The labelsno flagand
insufficient contextstand alone. Systems predict
the flags, not the legal provisions behind them. The
labelled data include short supporting quotes when
the quoted text matches the released evidence.
Figure 1 shows how the fields work together.
The linked page identifies an online betting service,
which determines the product category. The tran-
script says that a bet cannot lose, supporting the
misleading-claim flag. The video did not include
a paid-promotion label, but the speaker names the
sponsor in the segment, so the instance receives no
disclosure flag.
5 Dataset Construction
Source data and sampling.On 5 May 2026,
we downloaded a copy of SponsorBlock’s pub-
lic database. We selected intervals submitted in
the sponsorship category when they had at least
one more upvote than downvote. When a video
contained several eligible intervals, we kept the
highest-voted one. Contributors make these sub-
missions to improve their viewing experience, not
to make a legal determination. We use them only
to build the initial pool of likely commercial seg-
ments.
We then selected channels likely to reach a sub-
stantial teenage audience. The screening combined
keywords and other public information about each
channel with a GPT-5.4 classifier. It was designed
to remove clearly adult-oriented channels, not to
estimate each viewer’s age. In the released task,
“child-facing” means that a channel passed this
screening process. Systems receive that designa-
tion and do not predict it.
Evidence collection.For each selected video, we
collected the transcript around the marked interval,
the video title and description, and basic channel
information. We also followed links in the descrip-
tion, resolved redirects and extracted text from the
page most likely to describe the promotion. We
added a video to the dataset only when at least
one link produced a usable page. This requirement
removed 1,116 of 4,985 candidates (22.4%), so
the dataset underrepresents expired links and pages
that block automated access.
Video descriptions often contain several links.
Of the 3,300 instances with a transcript, GPT-5.4
compared the marked segment with the candidate
links and selected a likely matching page for 2,092.
For the other 1,208, we could not confidently match
a link, so we kept the first usable page in the de-
scription. Some of these fallback pages may belong
to a different promotion in the same video. Another
60 instances have no transcript, but still include the
available video, channel and page evidence.
We also recorded whether YouTube reported that
the video “Includes paid promotion”. On 17 July
2026, this field was present for 1,791 videos, ab-
sent for 1,529 and unavailable for 40. The 45.5%
absence rate is tied to that collection date because
YouTube can change both the label and the inter-
face that exposes it.
Splits.The 3,360 instances come from 3,360
videos and 939 channels, split into train (2,353
instances, 632 channels), dev (504, 154) and test
(503, 153). No channel appears in more than one
split. A system therefore cannot learn a channel’s
presentation style or disclosure habits from train-
ing data and encounter the same channel at test
time. Brands and destination pages can recur, so
the benchmark tests generalisation to new channels
rather than new advertisers.

Record stage Anonymised content
1. Commercial
segment
The speaker names [brand] as the sponsor, promotes a sports bet and says that the
bet cannot lose.
2. Description link[URL]
3. Resolved page [page title]; online sports betting and gambling service.
Platform disclosurefalse
Task output Released label
ST1digital_content_or_services
ST2gambling
ST3age_restricted_or_prohibited_product;misleading_claim
4. Released evidence age_restricted_or_prohibited_product: “This episode of [programme] is
sponsored by [brand].” The resolved page identifies an online betting service.
misleading_claim: “[brand] is giving you a bet you can’t lose.”
Figure 1: A real training instance with identifiers removed. Source summaries are paraphrased; evidence quotes
reproduce the release after redaction and punctuation adjustments. Labels are unchanged.
Level Field group Contents Collection cost
1transcript Segment text, start and end time Lowest; platform-scale text
2video_context Video ID, title, description, plat-
form disclosure
One metadata call per video
3channel_contextChannel ID and channel name One channel lookup
4product_page Raw and resolved URL, page ti-
tle and page text
Outbound crawl; pages may be dead or block automation
Table 1: Access levels are ordered by the cost of obtaining fields at platform scale. Teams report the highest level
used, so accuracy can be interpreted alongside collection cost.
Data access levels.Table 1 groups the released
fields by the work needed to collect them. Level 1
requires only the marked transcript. Level 2 adds
video metadata, level 3 adds channel information,
and level 4 adds the crawled promotional page.
The levels are cumulative. Teams report the high-
est level they use, allowing comparison between
systems with different data requirements.
Tables 2 and 3 show strong label imbalance. The
most common ST3 flag is misleading claim, while
each product-risk flag has fewer than 60 training
examples. The rarest labels are ST1other(2), ST2
gambling(12) and ST3insufficient context(15).
Macro-F1 weights each label equally, but scores for
these rare labels remain sensitive to a small number
of predictions.
The release also includes the label taxonomy and
legal-reference file. SponsorBlock-derived data
retain the CC BY-NC-SA 4.0 licence. The data-
use agreement covers video-derived fields, requires
compliance with YouTube’s Terms of Service, and
prohibits redistribution, re-identification, contact
and publications that single out a creator.
6 Annotation and Reliability
LLM annotation.We used GPT-5.4 to produce
the labels. For each instance, the model received
the available evidence and label definitions and
returned the applicable labels. The process was
iterative. The organiser team, including a legal
expert, reviewed samples, discussed errors and re-
vised the taxonomy, prompts and model choices.
This review led, for example, to a narrower defi-
nition of direct exhortation and a new annotation
pass for that flag. The sample review was not a
systematic double-annotation study, so we do not
report human inter-annotator agreement.
For ST1 and ST2, GPT-5.4 received the ex-
tracted brand, the linked page title and text, the tran-
script, and the video description. The main ST3
pass received the same evidence, except for the
page title, along with YouTube’s paid-promotion
field and summaries of the relevant legal provisions.
The revised direct-exhortation pass used only the

ST1: commercial type
Label Train Dev Test
Physical goods 1,125 218 235
Digital content or services 1,069 248 225
Physical services 122 24 33
No identifiable offer 35 14 9
Other 2 0 1
ST2: product category
Label Train Dev Test
Apps 654 171 124
Hardware and electronics 516 120 99
Other 412 87 97
Food 293 49 52
Creator community 269 47 70
Fashion 267 50 78
Health 264 55 50
Education 140 12 18
Financial products 135 20 56
Gambling-adjacent 92 17 25
Toys 77 8 29
Gambling 12 5 3
Table 2: ST1 and ST2 label counts by split. ST1 assigns one commercial type to each instance; ST2 may assign
multiple product categories.
ST3 flag Legal family Train Dev Test
Misleading claim Content 1,277 260 259
Inadequate disclosure Disclosure 611 118 139
No flag Housekeeping 529 127 112
Undisclosed advertising Disclosure 352 74 89
Direct exhortation Content 304 77 71
Age-restricted or prohib-
ited product
Product 59 16 17
HFSS food marketing Product 40 5 5
Insufficient context Housekeeping 15 7 6
Table 3: ST3 compliance-risk counts by split. ST3 is
multi-label; family-level evaluation groups the eight
labels into four families: disclosure, content, product
and housekeeping.
brand and transcript.
To measure label stability across models, GPT-
5.6-luna independently labelled the 504 develop-
ment instances.
Cross-model agreement.The two models assign
the same ST1 label in 94.4% of cases. For multi-
label ST2, they assign the same label set in 66.3%
of cases; their average set overlap, measured by
Jaccard similarity, is 0.74. They assign the same
full ST3 flag set in 44.4% of cases. The largest
differences concern inadequate disclosure and mis-
leading claims. The GPT-5.4 labels include inad-
equate disclosure in 98 cases where GPT-5.6-luna
does not, while GPT-5.6-luna assigns misleading
claim in 128 cases where GPT-5.4 does not. We re-
port both fine-grained and family-level ST3 scores
so that results can also be read at the broader dis-
closure, content and product levels.
7 Evaluation Setup
We hosted the competition on CodaBench, an on-
line platform for running reproducible benchmarks
(Xu et al., 2022). Teams could enter any subset
of the three tasks. A submission contains one
machine-readable prediction record for each in-
stance; a missing prediction receives zero credit.
The development phase ran from 20 July to 10 Au-
gust 2026. The evaluation phase ran from 11 to
18 August. The final export contains 21 entries,
excluding the organiser baseline.
For each task, we compute F1 for each label that
occurs in the gold labels or the predictions and av-
erage those labels equally (macro-F1). The overall
score is the mean of the three task scores. We also
report a family-level ST3 score that groups the
eight labels into four families: disclosure, content,
product and housekeeping. The organiser baseline
predicts the majority class for every instance.
Each submission states the highest data-access
level used, which CodaBench displays beside the
score. Teams can also report their method, esti-
mated cost and whether they retrieved legal mate-
rial beyond the references supplied with the task.
We do not score legal grounding because the sub-
mission format does not support reliable evaluation
of retrieved provisions. Section 8 instead reports
how the system papers used the supplied legal ma-
terial.
8 Participating Systems
The evaluation phase received 21 entries (Table 4).
The highest mean macro-F1 was 0.7347. Fourteen
entries used all four access levels, six used the

transcript alone, and one used the transcript with
video context. The best transcript-only entry placed
seventh with 0.6521, 0.083 below the top entry.
Since the systems also differ in models, training
and validation, this gap cannot be attributed to data
access alone. Section 8 instead compares access
levels within the four systems for which we have
detailed reports.
We invited five teams to write system descrip-
tion papers, and four did. Rank was one criterion,
but not the main one. The access levels were de-
signed to test a practical question: how much ad-
ditional data does a monitoring system need, and
when is the cost of collecting it worthwhile? Be-
fore the deadline, we explicitly told participants
that a transcript-only system performing close to
one using the full crawl would itself be an interest-
ing result. We therefore also considered the infor-
mation reported in the submission questionnaire,
whether the reported claims were supported by the
submitted results, and whether the invited systems
represented different approaches. Each invitation
asked teams to report data-access levels, validation
protocol, test-set cost and negative results.
thylinao.Silchenko (2026) combines six mem-
bers at equal weight: two fine-tuned encoders,
a zero-shot Qwen3-32B, a LoRA-tuned Qwen3-
14B used only for ST2, a TF-IDF model and
a stacker for ST3. Every threshold is fitted on
channel-grouped out-of-fold predictions and never
on the development set. The zero-shot member
contributes the most while being one of the cheap-
est components, whereas removing the fine-tuned
DeBERTa produces no measurable change. One
14-minute GPU pass dominates inference over the
test set.
Nürnberg NLP.Steigerwald et al. (2026) (entry
broxy) build a nine-voter ensemble for each sub-
task from branches that differ in backbone, adapta-
tion method and class scope. V oters are selected by
channel-disjoint cross-validation, with the develop-
ment set used only as a transfer check. The entry
has the highest ST2, ST3 and family-level ST3
scores, while its difference from the top overall
entry comes entirely from ST1. At full access, it
labels the test set in under three GPU-hours on one
A100.
Alphastream.Narayan (2026) (entry runner)
combines a multi-task ModernBERT-large encoder
with an entailment-style reformulation of ST3 and
merges their probabilities label by label under a
paired bootstrap. The system uses no generative
model, and all experiments cost about US$17 in to-
tal. In a single-seed ablation, adding the four access
levels increases mean macro-F1 by 0.042, com-
pared with 0.128 from increasing encoder scale.
Among five negative results, retraining on 21%
more data lowered the test score, and seed variance
was as large as the largest modelling gains.
AI-Monitors.Sahoo et al. (2026) use differ-
ent input levels and models for each subtask. A
ModernBERT-large encoder reading all four levels
handles ST1 and ST2. For ST3, a transcript-only
encoder is averaged with a QLoRA-tuned Qwen2.5-
7B-Instruct for the two disclosure flags. The system
labels the test set in 25.5 GPU-minutes. Two of
their other submissions ranked above this system
on the development set, but the ordering reversed
on the test set.
Contribution of the access levels.The four sys-
tem papers are the best evidence we have on what
each additional data source contributes. Their com-
parisons are not directly equivalent: thylinao ab-
lates its zero-shot member, Nürnberg NLP pools
about 150 voters per level, Alphastream runs a
single-seed ablation and AI-Monitors compares en-
coder runs. Even so, all four draw the same line
between product identification and compliance-risk
classification.
The linked promotional page is most useful for
identifying what is being sold. Adding it raises
ST2 by 0.128 for AI-Monitors. For Nürnberg NLP,
the level-4 gain is concentrated in ST1 (+0.080)
and ST2 (+0.116). The same page contributes little
to ST3: the score falls by 0.031 for AI-Monitors,
rises by 0.013 for Nürnberg NLP and does not
change measurably for thylinao.
The cheaper levels add little. Neither thylinao
nor Nürnberg NLP finds any benefit from the chan-
nel name, and for Nürnberg NLP most of the ST3
improvement is already there once video metadata
is added. thylinao and AI-Monitors also tested
the legal material supplied with the task: giving
a prompted model the relevant provisions did no
better than giving it the flag definitions alone.
These are comparisons within individual sys-
tems, not controlled estimates of each source’s
value, and the systems use the evidence differently.
The pattern is nonetheless consistent across the
four papers. Crawling the linked page helps estab-
lish what is being promoted but adds little to the

# Team Level Mean ST1 ST2 ST3 ST3 fam. System paper
1 abc-abc 1–40.7347 0.84960.7550 0.5996 0.6834
2 thylinao a 1–4 0.7260 0.8049 0.7900 0.5830 0.6620 Silchenko (2026)
3 broxy 1–4 0.7079 0.64640.8243 0.6530 0.7031Steigerwald et al. (2026)
4 runner b 1–4 0.7022 0.7923 0.7945 0.5197 0.6359 Narayan (2026)
5 rudolpheric 1–4 0.6699 0.6581 0.7364 0.6153 0.6984
6 9999_9999_99 1–4 0.6666 0.6093 0.8034 0.5870 0.6688
7 Happy 1 0.6521 0.7305 0.6967 0.5290 0.6201
8 moumita 1–4 0.6261 0.6189 0.6724 0.5870 0.6694
9 shayyy 1 0.6256 0.5778 0.7954 0.5036 0.6176
10 k_n_n_nlp 1 0.6252 0.5980 0.7607 0.5170 0.6642
11 AI-Monitors 1–4 0.6223 0.5906 0.6979 0.5784 0.6501 Sahoo et al. (2026)
12 koshi 1–4 0.6205 0.5734 0.7233 0.5647 0.6650
13 g_n_n_grease 1 0.5933 0.5977 0.7221 0.4600 0.5547
14 Abid 1–4 0.5790 0.5689 0.7559 0.4121 0.6006
15 thenandinee 1 0.5721 0.5491 0.6818 0.4854 0.5900
16 vimalkumark 1–4 0.5709 0.5168 0.6885 0.5074 0.6155
17 midushi 1–4 0.5625 0.5447 0.6696 0.4733 0.6231
18 mercancanpolat 1–2 0.5587 0.5203 0.6229 0.5329 0.6692
19 taitran501 1–4 0.5499 0.5396 0.7090 0.4011 0.5139
20 Axiom 1–4 0.5410 0.5964 0.6669 0.3598 0.4880
21 avkiran 1 0.4926 0.4781 0.5571 0.4427 0.5713
– Majority class – 0.0818 0.1274 0.0330 0.0850 0.1856
Table 4: Final evaluation-phase leaderboard (503 test instances, macro-F1). The top four entries lie within 0.033
of each other on the mean, and no entry leads all three subtasks. Level is the highest data-access level the team
declared. Bold marks the best score in each column. aThe entry includes three labels set by hand; the system alone
scores 0.6537. bThe entry was chosen between two variants with one leaderboard probe; the probe-free primary
system scores 0.6798. Both teams disclosed these choices.
compliance-risk labels. For those labels, part of the
ceiling may lie in the labels themselves. The two
annotating models agree on the full ST3 label set in
only 44.4% of development instances (Section 6),
and Alphastream finds that near-duplicate training
examples often carry different flag sets.
9 Discussion, Limitations and Ethics
The access levels make the cost of collecting evi-
dence part of the evaluation. A transcript can be
processed cheaply across many videos. A promo-
tional page must be found, resolved, and crawled,
and it may no longer exist or may block automated
access. In the system papers, that extra work helped
mainly with identifying the offer or product and
added little to compliance-risk classification, while
the channel name added nothing measurable. A
monitoring pipeline may therefore need different
evidence depending on what it is trying to estab-
lish, rather than collecting every available source
for every task.
Running the competition also exposed evalua-
tion weaknesses we had not seen in the dataset
alone. Macro-F1 averages only over labels that
occur in the gold labels or the predictions, and
because ST1otherhas a single test instance, pre-
dicting it or not changes about a fifth of the ST1
score (Silchenko, 2026; Narayan, 2026). Publish-
ing the majority-class baseline’s per-subtask scores
also made it possible to recover a gold class count
in closed form, while the leaderboard revealed that
otheroccurred in the test labels.
The channel-disjoint split handles only one kind
of dependence. It keeps the same channel out of
both training and test data, but advertisers and des-
tination domains can recur. By thylinao’s count,
54.5% of test advertisers, covering 70.4% of test
instances, also appear in the labelled data, and sim-
ply copying an advertiser’s majority training label
scores 0.4649 on the development set (Silchenko,
2026). At the domain level, 65.0% of test instances
promote a domain seen in training (Sahoo et al.,
2026). This does not make the current split invalid:
generalising to new channels was its intended pur-
pose. It does mean the benchmark cannot tell us
how well a system handles an advertiser it has never
seen. A future edition should either hold out adver-
tisers as well or report results separately for seen
and unseen advertisers.
Many differences between systems are also
small compared with task noise. Near-duplicate
training instances agree on the full ST3 flag set

only 43–63% of the time (Narayan, 2026), close to
the 44.4% exact cross-model agreement on the de-
velopment set. Alphastream finds seed variance as
large as its largest modelling gains (Narayan, 2026),
while Nürnberg NLP finds that the 504 develop-
ment instances are not enough to reliably separate
its strongest candidates (Steigerwald et al., 2026).
Small leaderboard differences should therefore be
interpreted cautiously, particularly for ST3. The
top four entries are separated by only 0.033 mean
macro-F1, and no system leads all three subtasks.
The dataset does not represent all advertising on
YouTube. It contains only videos with a Sponsor-
Block sponsorship mark and a promotional page
that we could crawl. Both requirements introduce
selection bias, and we have no non-commercial ex-
amples to measure discovery at a realistic base rate.
The channel screen estimates which channels are
likely to reach teenagers from public metadata; it
does not measure the actual audience. The selected
page could not be aligned confidently to the marked
segment in 1,208 instances, and 60 instances have
no transcript. Pages can also change after collec-
tion.
The benchmark is predominantly English and
text-based. It does not include video frames, visual
disclosure timing, non-verbal audio or all transac-
tion details that could matter in a legal assessment.
These omissions matter most for ST3. The final la-
bels were produced by GPT-5.4 after the organisers
reviewed samples and iterated on the task defini-
tions and prompts. Systems are therefore evaluated
against the released taxonomy and model-produced
labels, not against an independent legal assessment.
The benchmark allows systems to be compared un-
der a common operationalisation of these risks, but
its scores should not be read as accurate indicators
of legal compliance.
The release contains no viewer records or mea-
sured audience demographics, but it includes chan-
nel names, video identifiers, titles and descriptions.
The data-use agreement prohibits redistribution,
re-identification, contact, harassment and publica-
tions that single out a creator. We redact identifiers
in worked examples. The dataset is intended for
research and human review, not profiling or auto-
matic enforcement.
10 Conclusion
CHILDSAFEADSprovides a 3,360-video bench-
mark for classifying commercial offers, product
categories and potential compliance risks in child-
facing YouTube content. The shared task received
21 entries. In the four system papers, additional
evidence helps some tasks and not others: crawling
the promotional page improves product identifica-
tion but adds little to compliance-risk classification,
and the channel name brings no measurable gain.
For monitoring in practice, this argues for collect-
ing evidence according to the question being asked
rather than gathering every source for every task.
The competition also showed where the benchmark
needs work before a second edition: label stability,
advertiser overlap, and handling rare labels in the
metric.
Acknowledgements.We thank the SponsorBlock
contributors and the participating teams. This re-
search was supported by the ERC Starting Grant
HUMANads (ERC-2021-StG No 101041824).
References
Thales Bertaglia, Catalina Goanta, Gerasimos Spanakis,
and Adriana Iamnitchi. 2025. Influencer self-
disclosure practices on Instagram: A multi-country
longitudinal study.Online Social Networks and Me-
dia, 45:100298.
Thales Bertaglia, Stefan Huber, Catalina Goanta, Gerasi-
mos Spanakis, and Adriana Iamnitchi. 2023. Closing
the loop: Testing ChatGPT to generate model ex-
planations to improve human labelling of sponsored
content on social media. InExplainable Artificial In-
telligence, pages 198–213. Springer Nature Switzer-
land.
Ilias Chalkidis, Abhik Jana, Dirk Hartung, Michael
Bommarito, Ion Androutsopoulos, Daniel Katz, and
Nikolaos Aletras. 2022. LexGLUE: A benchmark
dataset for legal language understanding in English.
InProceedings of the 60th Annual Meeting of the
Association for Computational Linguistics (Volume
1: Long Papers), pages 4310–4330, Dublin, Ireland.
Association for Computational Linguistics.
Marijke De Veirman, Liselot Hudders, and Michelle R.
Nelson. 2019. What is influencer marketing and how
does it target children? a review and direction for
future research.Frontiers in Psychology, 10:2685.
European Parliament and Council of the European
Union. 2005. Directive 2005/29/ec concerning unfair
business-to-consumer commercial practices in the
internal market. Accessed 18 August 2026.
European Parliament and Council of the European
Union. 2010. Directive 2010/13/eu on the coordi-
nation of certain provisions laid down by law, regu-
lation or administrative action in member states con-
cerning the provision of audiovisual media services.
Accessed 18 August 2026.

European Parliament and Council of the European
Union. 2011. Directive 2011/83/eu on consumer
rights. Accessed 18 August 2026.
European Parliament and Council of the European
Union. 2022. Regulation (eu) 2022/2065 on a sin-
gle market for digital services. Accessed 18 August
2026.
Haoyang Gui, Thales Bertaglia, Taylor Annabell,
Catalina Goanta, Tjomme Dooper, and Gerasimos
Spanakis. 2025a. Evaluating LLM-generated legal
explanations for regulatory compliance in social me-
dia influencer marketing. InProceedings of the Nat-
ural Legal Language Processing Workshop 2025,
pages 157–171, Suzhou, China. Association for Com-
putational Linguistics.
Haoyang Gui, Thales Bertaglia, Catalina Goanta, Sybe
de Vries, and Gerasimos Spanakis. 2025b. Across
platforms and languages: Dutch influencers and legal
disclosures on Instagram, YouTube and TikTok. In
Social Networks Analysis and Mining, pages 3–12.
Springer Nature Switzerland.
Ben Hagag, Gil Gil Semo, Dor Bernsohn, Liav Harpaz,
Pashootan Vaezipoor, Rohit Saha, Kyryl Truskovskyi,
and Gerasimos Spanakis. 2024. LegalLens shared
task 2024: Legal violation identification in unstruc-
tured text. InProceedings of the Natural Legal Lan-
guage Processing Workshop 2024, pages 361–370,
Miami, FL, USA. Association for Computational Lin-
guistics.
Rishabh Kaushal, Jacob van de Kerkhof, Catalina
Goanta, Gerasimos Spanakis, and Adriana Iamnitchi.
2024. Automated transparency: A legal and empir-
ical analysis of the digital services act transparency
database. InProceedings of the 2024 ACM Confer-
ence on Fairness, Accountability, and Transparency,
pages 1121–1132. Association for Computing Ma-
chinery.
Marco Lippi, Giuseppe Contissa, Agnieszka
Jabłonowska, Francesca Lagioia, Hans-Wolfgang
Micklitz, Przemysław Palka, Giovanni Sartor, and
Paolo Torroni. 2020. The force awakens: Artificial
intelligence for consumer law.Journal of Artificial
Intelligence Research, 67:169–190.
Femke Loose, Liselot Hudders, Steffi De Jans, and
Ini Vanwesenbeeck. 2023. A qualitative approach
to unravel young children’s advertising literacy for
youtube advertising: In-depth interviews with chil-
dren and their parents.Young Consumers, 24(1):74–
94.
Esther Martínez-Pastor, Ricardo Vizcaíno-Laorga, and
David Atauri-Mezquida. 2021. Health-related food
advertising on kid youtuber vlogger channels.He-
liyon, 7(10):e08178.
Arunesh Mathur, Arvind Narayanan, and Marshini
Chetty. 2018. Endorsements on social media: An
empirical study of affiliate marketing disclosures on
youtube and pinterest.Proceedings of the ACM on
Human-Computer Interaction, 2(CSCW):1–26.
Raghavendra Prasad Narayan. 2026. Alphastream at
ChildSafeAds 2026: Gated per-label merging and an
advertiser-precedent rule for rare compliance classes.
InProceedings of the Natural Legal Language Pro-
cessing Workshop 2026, Budapest, Hungary. Associ-
ation for Computational Linguistics.
Joao P. Santos Rodrigues, Ana C. Munaro, and Emer-
son Cabrera Paraiso. 2021. Identifying sponsored
content in youtube using information extraction. In
2021 IEEE International Conference on Systems,
Man, and Cybernetics, pages 3075–3080. IEEE.
Pragyananda Sahoo, Vishnu Tripathi, Prakhar Joshi,
Gaurav Kumar, and Neel Mani. 2026. AI-monitors
at ChildSafeAds 2026: A routed hybrid for com-
mercial content in child-facing YouTube videos. In
Proceedings of the Natural Legal Language Process-
ing Workshop 2026, Budapest, Hungary. Association
for Computational Linguistics.
Maksim Silchenko. 2026. thylinao at ChildSafeAds
2026: A six-member ensemble and what each level
of data access provided. InProceedings of the Natu-
ral Legal Language Processing Workshop 2026, Bu-
dapest, Hungary. Association for Computational Lin-
guistics.
Philipp Steigerwald, Eric Rudolph, and Jens Albrecht.
2026. Nürnberg NLP at ChildSafeAds 2026: Struc-
turally dissimilar voter ensembles under four levels
of data access. InProceedings of the Natural Le-
gal Language Processing Workshop 2026, Budapest,
Hungary. Association for Computational Linguistics.
Simone van der Hof, Eva Lievens, Ingrida Milkaite, Va-
lerie Verdoodt, Tineke Hannema, and Ton Liefaard.
2020. The child’s right to protection against eco-
nomic exploitation in the digital world.The Interna-
tional Journal of Children’s Rights, 28(4):833–859.
Zhen Xu, Sergio Escalera, Adrien Pavão, Magali
Richard, Wei-Wei Tu, Quanming Yao, Huan Zhao,
and Isabelle Guyon. 2022. Codabench: Flexible,
easy-to-use, and reproducible meta-benchmark plat-
form.Patterns, 3(7):100543.
Linda Xue, Francesco Corso, Nicolo Fontana, Geng
Liu, Stefano Ceri, and Francesco Pierri. 2025. To-
wards an automated framework to audit youth safety
on TikTok. InProceedings of the Fourth Workshop
on Bridging Human-Computer Interaction and Nat-
ural Language Processing, pages 113–119, Suzhou,
China. Association for Computational Linguistics.
Brahim Zarouali, Valerie Verdoodt, Michel Walrave,
Karolien Poels, Koen Ponnet, and Eva Lievens. 2020.
Adolescents’ advertising literacy and privacy protec-
tion strategies in the context of targeted advertising
on social networking sites: Implications for regula-
tion.Young Consumers, 21(3):351–367.
