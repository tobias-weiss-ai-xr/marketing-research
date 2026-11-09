---
title: 'Auditing Engagement Incentives in the Kidfluencer Ecosystem: A Multimodal Weak Supervision Approach'
url: https://arxiv.org/abs/2606.03173
category: digital-marketing
subcategory: empirical
date: 2026-06
venue: ''
authors:
- Zijing Wei
- Chao Peter Yang
- Xuanjie Chen
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.03173
pages: 12
chars: 49208
fetched_at: '2026-11-08T13:09:53+00:00'
kb_version: 1
---

# Auditing Engagement Incentives in the Kidfluencer Ecosystem: A Multimodal Weak Supervision Approach

Auditing Engagement Incentives in the Kidfluencer Ecosystem: A Multimodal
Weak Supervision Approach*
Zijing Wei1, Chao Peter Yang2, Xuanjie Chen1
1Independent Contributor
2Duke University
Abstract
The rapid rise of “kidfluencers” on YouTube has raised pro-
found ethical concerns regarding child digital labor and ex-
ploitation. While emerging legislation attempts to regulate
this ecosystem, empirical evidence on the relationship be-
tween child exploitation and engagement metrics remains
scarce due to the challenge of operationalizing and scal-
ing exploitation measurements. This study presents a multi-
modal AI audit of 5,051 videos across 79 kidfluencer chan-
nels, utilizing a weak supervision approach to detect ex-
ploitation signals without requiring large-scale manually la-
beled ground truth. We aggregate noisy labeling functions—
including LLM-based classification of titles and GPT-4 Vi-
sion analysis of thumbnails and descriptions across six
literature-grounded dimensions—to assign a probabilistic ex-
ploitation score to each video. A multi-annotator validation
study (N= 107videos) combining independent human an-
notations demonstrates strong agreement with human judg-
ment across six exploitation dimensions (macro-average F1
= 0.911) and high sensitivity for overall exploitation risk (re-
call= 0.960, overall F1= 0.793).
Our findings reveal a highly significantengagement pre-
mium associated with performative labor, emotional bait,
and privacy violations. Overall exploitation scores correlate
significantly with view counts (Spearmanρ= 0.229,p <
10−50). Mixed-effects regression, controlling for channel-
level variation, demonstrates that a one-unit increase in ex-
ploitation score is associated with a 4.4×increase in views
(p <0.001). Within-channel analyses show that emotional
bait and performative content are associated with median
view boosts of+65.6%and+56.0%respectively (FDR-
correctedp <0.001). These effects hold in robustness
checks comparing videos published within the same year
(p= 0.030). Conversely, we find that explicit commercial
content (product placement) does not benefit from this en-
gagement premium (−3.8%, n.s.), suggesting that the plat-
form ecosystem rewards the commodification of the child’s
identity and labor rather than traditional advertising. These
findings challenge policy frameworks focused solely on fi-
nancial trusts, demonstrating that engagement metrics are
systematically associated with the intensive, performative la-
bor of children.
*Preprint. Preliminary Work.
1 Introduction
The commercialization of childhood through digital plat-
forms has created a lucrative “kidfluencer” economy in
which children are featured in YouTube videos—unboxing
toys, participating in challenges, performing scripted role-
play, and documenting their daily lives (Clark and Jno-
Charles 2025). This phenomenon has sparked intense debate
regarding the ethics of child digital labor, the psychological
impact of public exposure, and the blurring of lines between
play and work, often termed “playbour” (Abidin 2015).
Recent legislative efforts, such as the Illinois PA 103-0556
(2024) (ill 2024), aim to protect child creators by mandat-
ing financial trusts and limiting working hours. However,
these regulations treat kidfluencing as a traditional labor
market, often failing to address how platform ecosystems
actively shape content creation (UNICEF 2025). A funda-
mental question remains:How do engagement metrics as-
sociate with specific dimensions of child exploitation?
Previous research on the kidfluencer ecosystem has
largely relied on qualitative content analysis or small-scale
manual coding (Divon et al. 2025; Anderson 2025). While
valuable, these approaches cannot scale to audit the mas-
sive volume of content generated. Conversely, purely com-
putational approaches often struggle to operationalize com-
plex, nuanced concepts like “exploitation” or “performativ-
ity” without expensive, large-scale human annotation. Fur-
thermore, prior audits of platform algorithms (Husz ´ar et al.
2022; Haroon et al. 2023) have often focused on political
content rather than child safety (Papadamou et al. 2020).
This study bridges this gap by deploying amultimodal
weak supervision pipelineto conduct a large-scale ob-
servational audit. We ground our conceptualization of ex-
ploitation risk in the UN Convention on the Rights of the
Child (UNCRC), specifically drawing on Clark and Jno-
Charles’s (Clark and Jno-Charles 2025) five fundamental
threats framework for kidfluencing. We operationalize these
theoretical threats into six measurable content dimensions:
performative labor, emotional bait, narrative conflict, chal-
lenge formats, commercial content, and privacy violations.
Crucially, because we rely on observational data via the
YouTube API, we cannot directly observe the recommen-
dation algorithm’s internal scoring (Bouchaud et al. 2024;
Rieder, Matamoros-Fern ´andez, and Coromina 2018). In-
stead, we measure theengagement premium—the asso-
arXiv:2606.03173v1  [cs.CY]  2 Jun 2026

ciation between exploitative content dimensions and view
counts—which serves as a proxy for the incentive structures
shaping creator behavior.
Our core research questions are:
•RQ1:Can a weak supervision framework effectively
synthesize multimodal signals (text, LLM classifications,
and computer vision) to measure kidfluencer exploitation
at scale?
•RQ2:Are specific dimensions of exploitation (e.g., per-
formative labor vs. commercial content) associated with
higher view counts (an “engagement premium”)?
•RQ3:Does this engagement premium persistwithin
channels and when controlling for video age, indicat-
ing a structural correlation rather than merely a channel-
popularity effect?
2 Related Work
2.1 The Kidfluencer Economy and Exploitation
Frameworks
The kidfluencer economy relies on the continuous docu-
mentation of children’s private lives and their participa-
tion in scripted entertainment. Clark and Jno-Charles (Clark
and Jno-Charles 2025) propose analyzing this phenomenon
through the lens of the UNCRC, identifying five fundamen-
tal threats to children’s rights in the kidfluencing context:
(1) violation of consent, (2) violation of privacy, (3) eco-
nomic exploitation (e.g., blurring work/leisure, making the
child the product), (4) exposure to physical or psychologi-
cal harm, and (5) suppression of authentic expression. Di-
von et al. (Divon et al. 2025) further describe how chil-
dren are transformed into “concealed commodities” through
practices like transactional play. Because direct observation
of rights violations (e.g., a child’s true consent or compensa-
tion) is impossible via public metadata, computational audits
must rely on proxy indicators of labor intensity and risk.
Other literature highlights the privacy risks of “sharent-
ing” (Steinberg 2017; Kopeck ´y et al. 2020), where parents
overshare children’s lives online, potentially leading to emo-
tional neglect (Keskin 2023). In extreme cases, such as the
“Elsagate” phenomenon, platforms have struggled to mod-
erate inappropriate content targeting toddlers (Papadamou
et al. 2020; Bridle 2017; Tahir et al. 2019). Building on these
frameworks, we operationalize exploitation not merely as
overt abuse, but as the intensive, performative labor required
to maintain engagement.
2.2 Algorithmic Auditing and Engagement
Metrics
Algorithmic auditing investigates platform behavior without
direct access to proprietary code, aiming to uncover sys-
temic biases or perverse incentives (Sandvig et al. 2014;
Metaxa et al. 2021). Previous studies have successfully au-
dited YouTube and Twitter for political radicalization, algo-
rithmic amplification of extreme content, and gender bias
(Ribeiro et al. 2020; Husz´ar et al. 2022; Haroon et al. 2023;
Hussein, Juneja, and Mitra 2020). These audits typically em-
ploy either active experimental designs, such as using sock
puppet accounts to simulate user journeys (Habib 2025),
or large-scale observational analyses of engagement data
(Bouchaud et al. 2024).
However, the application of algorithmic auditing to child
safety and the kidfluencer ecosystem remains limited. While
platforms have implemented mechanisms like YouTube
Kids to filter inappropriate content (Papadamou et al. 2020),
the incentive structures driving the creation of borderline
exploitative content on the main platform are less under-
stood. Because direct recommendation rates and internal al-
gorithmic weights are hidden from external researchers, we
must rely on observational proxies. Following established
methodologies (Covington, Adams, and Sargin 2016; Zhou,
Khemmarat, and Gao 2010; Rieder, Matamoros-Fern ´andez,
and Coromina 2018), we use engagement metrics (specifi-
cally, view counts) as a proxy for algorithmic reach and au-
dience demand. By measuring the “engagement premium”
(the positive association with specific content types), we can
infer the economic incentives that likely shape creator be-
havior.
2.3 Weak Supervision and LLM Content Analysis
Traditional machine learning requires massive labeled
datasets, which are difficult to obtain for subjective con-
cepts. Weak supervision frameworks like Snorkel (Ratner
et al. 2017, 2016; Bach et al. 2019) allow researchers to
encode domain knowledge as noisy heuristic rules (La-
beling Functions) to generate probabilistic labels (Johnson
and Khoshgoftaar 2022). Recently, Large Language Models
(LLMs) and Vision-Language Models (VLMs) have shown
promise in zero-shot content moderation and annotation (Ma
et al. 2023; Gilardi, Alizadeh, and Kubli 2023; T ¨ornberg
2024). We combine LLMs and VLMs within a weak super-
vision framework to scale our exploitation analysis across
text and visual modalities.
3 Methodology
3.1 Data Collection and Sampling
We collected metadata for 58,965 videos from 79 family and
kidfluencer YouTube channels using the YouTube Data API.
Channels were selected based on prior literature and popular
influencer lists, covering a spectrum of channel sizes and tar-
get audiences. The selected 79 channels represent a diverse
cross-section of the kidfluencer ecosystem: 9 small chan-
nels (<50K median views), 31 medium (50K–500K), 26
large (500K–5M), and 13 very large (>5M median views),
with an overall median of approximately 445,000 views per
video. All channels are primarily English-language family
vlog or kidfluencer channels featuring real children; ani-
mated channels were strictly excluded.
To manage computational costs while maintaining repre-
sentativeness, we employed a stratified sampling strategy.
For each of the 79 channels, we stratified videos into terciles
based on view counts (high, medium, low) and randomly
sampled up to 20 videos per tercile, resulting in a final strat-
ified sample of 5,051 videos with valid view counts. We re-
trieved the title, description, thumbnail image, and publica-
tion date for each sampled video.

For the engagement analysis, we restricted the sample to
56kid-centricchannels (n= 4,208videos) by excluding 23
channels where the primary content creator is an adult (e.g.,
adult family vloggers who occasionally feature children).
This ensures that the engagement premium analysis specif-
ically captures incentives related to child-centered content.
Within-channel pairwise comparisons further required suffi-
cient within-channel variance in exploitation scores, yield-
ing 47 channels with both exploitative and non-exploitative
videos for the within-channel analysis.
3.2 Exploitation Risk Dimensions
Because actual exploitation (e.g., lack of consent, uncom-
pensated labor) occurs off-camera, we cannot measure it di-
rectly. Instead, we operationalize Clark and Jno-Charles’s
(Clark and Jno-Charles 2025) five fundamental threats into
six observable content dimensions that serve as proxy indi-
cators of exploitation risk and labor intensity (Table 1).
UNCRC Threat
(Clark and Jno-
Charles 2025)
Our Observable Dimension
Consent ViolationPerformative Labor:Scripted/planned
content suggesting directed labor rather
than organic play.
Privacy ViolationPrivacy Violation:Exposure of pri-
vate, vulnerable, or medical moments.
Economic Ex-
ploitation
Commercial Content:Child used ex-
plicitly for product placement, making
the child the product.
Exposure to HarmChallenge Format:High-effort physi-
cal competitions.
Emotional Bait:Exaggerated distress
or emotional extremes used for click-
bait.
Expression Sup-
pression
Narrative Conflict:Manufactured
drama replacing the child’s authentic
voice.
Table 1: Mapping theoretical UNCRC threats to our observ-
able content dimensions.
3.3 Multimodal Weak Supervision Pipeline
We implemented a multimodal weak supervision pipeline
(Figure 1) using the Snorkel framework (Ratner et al. 2017).
Rather than relying on a single model or manual weighting,
we designed 33 heterogeneous Labeling Functions (LFs)
across the six dimensions. These LFs capture diverse signals
from the metadata:
•LLM and VLM Zero-Shot Classifiers:We deployed
GPT-4.1-mini (text-only, analyzing titles) and GPT-4.1-
mini Vision (analyzing titles, thumbnails, and descrip-
tions) as high-capacity LFs.
•Keyword and Pattern Heuristics:Regular expressions
detecting explicit clickbait patterns (e.g., ALL CAPS,
excessive punctuation, “GONE WRONG”), emotional
triggers (e.g., specific emojis, words like “crying” or
YouTube Data API
58,965 videos, 79 channels
Stratified Sampling
5,051 videos
33 Labeling Functions
(LLM, VLM, Keywords,
Metadata Heuristics)
Snorkel Label Model
(Learns LF accuracies
and correlations)
Probabilistic Aggregation
→Exploitation Score∈[0,1]
Human Validation
N=107, Macro-F1=0.911
Engagement Analysis
Mixed Effects + FDR
Figure 1: The multimodal weak supervision pipeline. LLM
text and VLM multimodal scores are aggregated into a prob-
abilistic exploitation score, validated against human annota-
tions.
“scared”), and commercial tags (e.g., “#ad”, “spon-
sored”).
•Metadata Heuristics:Rules based on video duration
(e.g., videos over 30 minutes are more likely to be ex-
tended challenges) and description structures.
For each dimension, a Snorkel Label Model was trained
to automatically estimate the unknown accuracies and cor-
relations of these LFs without ground truth data. The Label
Model aggregates the noisy, conflicting signals from the 33
LFs into a single probabilistic exploitation score (∈[0,1])
for each video. For example, in the performative labor di-
mension, the Label Model learned to assign high weights
to the VLM’s high-confidence predictions (w= 0.962) and
specific organic-content keyword rules (w= 0.977), while
down-weighting noisier heuristics. This data-driven aggre-
gation ensures that our final exploitation scores are robust to
the failure modes of any single LF or model.
Human Validation and Annotation Protocol.To rig-
orously validate the multimodal pipeline, we conducted a
multi-annotator validation study. Three independent anno-
tators manually labeled a stratified random sample of 107
unique videos from kid-centric channels. Annotators were
trained on the Clark and Jno-Charles (Clark and Jno-Charles
2025) five fundamental threats framework and assessed the
overall exploitation risk of each video by reviewing the ti-
tle, thumbnail, and at least 30 seconds of video content. The
annotation protocol instructed coders to identify performa-

Dimension Prev Prec Rec F1
Performative Labor 69.8% 0.923 0.973 0.947
Emotional Bait 85.0% 0.944 1.000 0.971
Narrative Conflict 59.5% 1.000 0.955 0.977
Challenge Format 36.7% 1.000 0.944 0.971
Commercial Content 51.0% 0.641 1.000 0.781
Privacy Violation 29.5% 1.000 0.692 0.818
Macro-Average 0.911
Table 2: Per-dimension validation of the multimodal
pipeline against consensus human annotations (N= 53
videos with per-dimension labels).
tive labor when the child was clearly engaging in scripted
or planned activities solely for the camera (e.g., skits, struc-
tured games), as opposed to organic documentation of daily
life (e.g., vlogs of shopping or moving). Emotional bait was
coded when the title or thumbnail explicitly manufactured
exaggerated emotional states (e.g., shock, fear, guilt) to at-
tract clicks.
In total, we compiled 191 annotation entries across 107
unique videos that matched our kid-centric Snorkel dataset.
For the 53 videos where detailed per-dimension labels were
available, we computed consensus labels via majority vote.
Table 2 reports the model’s performance on these individ-
ual dimensions. The pipeline demonstrated exceptionally
strong capability in identifying specific exploitation signals,
achieving a macro-average F1 score of0.911. Notably, the
model achieved near-perfect F1 scores (>0.94) for perfor-
mative labor, emotional bait, narrative conflict, and chal-
lenge formats. Commercial content exhibited lower preci-
sion (0.641) despite perfect recall; this occurred because the
model detected subtle commercial signals (e.g., brand men-
tions in descriptions) that human annotators did not flag un-
less explicit sponsorship was present. Similarly, privacy vi-
olations showed lower recall (0.692) as the model missed a
few cases where implicit privacy issues were not fully cap-
tured by metadata and visual heuristics alone.
For the overall binary exploitation risk, we evaluated the
pipeline against the full set of 107 unique annotated videos.
Using an exploitation score threshold of0.5, the model
achieved an overall accuracy of0.766, precision of0.676,
recall of0.960, and an F1 score of0.793. The model’s pri-
mary error mode was false positives (moderate precision),
reflecting a deliberate design choice to err on the side of
flagging potential exploitation (high recall), consistent with
the audit’s protective intent. Human annotators generally ap-
plied a higher, more conservative threshold for determining
whether a video was ”overall exploitative,” even when 1-2
mild exploitation signals were present.
The pipeline computed a combined probability score for
each dimension, and anOverall Exploitation Score∈[0,1]
for each video.
4 Results
4.1 Pipeline Performance and Dimension
Prevalence
The multimodal pipeline successfully processed 4,208
videos from 56 kid-centric channels. Overall, 26.5% of the
sampled videos (n= 1,114) were classified as exploitative
(score≥0.7).
Figure 2: Distribution of the probabilistic exploitation score
generated by the multimodal weak supervision model.
Performative labor was the most prevalent dimension (de-
tected in 69.5% of videos), followed by emotional bait
(56.2%), commercial content (41.4%), narrative conflict
(34.9%), challenge formats (32.4%), and privacy violations
(22.9%). Overall, using an aggregated probability threshold
of 0.7, 26.5% of videos in the kid-centric dataset were clas-
sified as high exploitation risk.
4.2 The Engagement Premium (RQ2 & RQ3)
We found a highly significant positive correlation between a
video’s continuous exploitation risk score and its view count
(Spearmanρ= 0.229,p <10 −50).
To determine if this association is a structural platform
correlation rather than merely an artifact of highly exploita-
tive channels being more popular overall, we conducted
two primary analyses: mixed-effects regression and within-
channel pairwise comparisons.
Mixed-Effects Regression.We fit a mixed-effects linear
regression model predictinglog 10(views)from the overall
exploitation score, including random intercepts for each of
the 56 kid-centric channels to control for baseline channel
popularity. The model specification is:
log10(viewsij) =β0 +β 1 ·ExploitScore ij +u j +ϵ ij
whereu j ∼N(0, σ2 u)represents the channel-level random
intercept for channelj, andϵ ij is the residual error. This
formulation ensures that the estimated effect of exploitation
score reflectswithin-channelvariation rather than between-
channel differences in baseline popularity.
The model revealed a massive, highly significant effect:
a one-unit increase in the exploitation risk score is asso-
ciated with a0.647increase inlog 10(views)(β= 0.647,
SE= 0.059,z= 10.91,p <0.001). This translates
to approximately a4.4×increase in raw view counts

Exploitation Dimension Prevalence Mean Log-Premium Cohen’sdFDRp-value Mixed-Effectsβ
Performative Labor 69.5%+0.193 +0.524<0.001 ∗∗∗ 0.091∗∗∗
Emotional Bait 56.2%+0.219 +0.751<0.001 ∗∗∗ 0.264∗∗∗
Narrative Conflict 34.9%+0.145 +0.511<0.001 ∗∗∗ 0.153∗∗∗
Challenge Format 32.4%+0.082 +0.320 0.081(n.s.)0.003(n.s.)
Commercial Content 41.4%−0.017−0.073 0.516(n.s.)0.042(n.s.)
Privacy Violation 22.9%+0.147 +0.650<0.001 ∗∗∗ 0.226∗∗∗
Overall Exploitation26.5%+0.123 +0.582<0.001 ∗∗∗ 0.647∗∗∗
Table 3: Summary of engagement premiums by exploitation dimension. Mean log-premium represents the within-channel
difference inlog 10(views). Mixed-effectsβrepresents the coefficient in the joint model controlling for all dimensions simulta-
neously.
(100.647 ≈4.4). The random intercept variance was substan-
tial (σ 2 u = 0.741), confirming that channels vary consider-
ably in baseline popularity and justifying the multilevel ap-
proach. The intraclass correlation coefficient (ICC= 0.738)
indicates that 73.8% of the variance inlog 10(views)is at-
tributable to between-channel differences, underscoring the
importance of controlling for channel identity.
We then fit a second mixed-effects model using the con-
tinuous probabilities of the six individual dimensions as
fixed effects. When controlling for all dimensions simul-
taneously,emotional bait(β= 0.264,p <0.001),pri-
vacy violations(β= 0.226,p <0.001),narrative con-
flict(β= 0.153,p <0.001), andperformative labor
(β= 0.091,p <0.001) remained highly significant predic-
tors of increased viewership. Challenge formats (β= 0.003,
p= 0.91) and commercial content (β= 0.042,p= 0.24)
were not statistically significant in the joint model, suggest-
ing their effects may be mediated by correlation with the
primary dimensions.
Within-Channel Pairwise Comparisons.For each di-
mension, we compared the median views of videos exhibit-
ing that dimension against videos from thesame channel
lacking it. To account for multiple comparisons, we applied
False Discovery Rate (FDR) correction using the Benjamini-
Hochberg procedure.
Figure 3: Mean within-channel view boost by exploitation
dimension (FDR-corrected). Error bars represent 95% con-
fidence intervals.
The results reveal a clear engagement premium structure
across channels with sufficient data:
•Emotional Baitis associated with the largest premium,
generating+65.6%more views than non-emotional
videos on the same channel (Cohen’sd= 0.751, FDR
p <0.001).
•Performative Laboris associated with a+56.0%view
premium (d= 0.524, FDRp <0.001).
•Privacy ViolationsandNarrative Conflictare associ-
ated with+40.3%(d= 0.650, FDRp <0.001) and
+39.7%(d= 0.511, FDRp <0.001) premiums respec-
tively.
•Challenge Formatsshowed a smaller, non-significant
positive premium (+20.9%, FDRp= 0.081).
Crucially,Commercial Contentexhibited a slightneg-
ativepremium (−3.8%, FDRp= 0.516). While not sta-
tistically significant after FDR correction, the directionality
suggests that videos featuring explicit product placements
do not benefit from the massive engagement boosts seen in
emotional and performative exploitation dimensions.
Figure 4: Contrasting effects: Emotional exploitation dimen-
sions show positive engagement premiums while commer-
cial content shows a negative premium.
4.3 Robustness Checks
To ensure our findings were not merely artifacts of video
age (older videos accumulating more views), we con-
ducted asame-year within-channel comparisonon the
subset of videos with valid ISO-8601 publication dates

(N= 907). By matching exploitative and non-exploitative
videos published by the same channel in the same year (23
channel-year groups), we found the engagement premium
holds robustly: high-exploitation videos received+44.4%
more views than their same-year, same-channel counterparts
(Wilcoxonp= 0.030).
Figure 5: Distribution of overall within-channel premiums.
76.6% of channels exhibit a positive premium for exploita-
tive content.
Additionally, we verified the robustness of our results
by analyzing the overall exploitation flag at the channel
level. Across 47 channels with sufficient variance, 36 chan-
nels (76.6%) exhibited a positive engagement premium
for high-exploitation videos, yielding an average within-
channel boost of+32.8%(Wilcoxonp= 0.001). This con-
firms that the performativity premium is a widespread struc-
tural phenomenon, not driven by a few outlier channels.
5 Discussion
5.1 The “Performativity Premium” vs. The
Commercial Non-Effect
Our findings provide large-scale empirical evidence for a
“performativity premium” in the kidfluencer ecosystem. En-
gagement metrics are systematically associated with con-
tent features that proxy for intensive, performative labor
(scripted conflict, emotional bait) over organic family docu-
mentation. This premium creates a structural incentive gra-
dient where creators who push boundaries, manufacture
drama, and expose children’s emotional vulnerabilities are
systematically rewarded with higher attention in a highly
competitive market. Crucially, while our metrics capture
content features rather than direct UNCRC violations, the
high prevalence of these features (e.g., 69.5% performative
labor) suggests that the labor intensity required to succeed
on the platform is structurally high.
Interestingly, traditional commercial content (e.g., ex-
plicit toy unboxing or product placement) does not benefit
from this engagement premium (−3.8%, n.s.). This suggests
a fundamental shift in the kidfluencer economy: the most
successful strategy for driving massive viewership is not to
use the child to sell a physical toy, but to make the child’s
labor, emotions, and manufactured drama the product itself.
This aligns with Divon et al.’s (Divon et al. 2025) concept
of “transactional childhood.” Audiences appear less respon-
sive to overt advertising but are heavily drawn to the com-
modification of the child’s identity. Furthermore, the lack
of an engagement premium for commercial content may
partially reflect platform-level interventions; following the
FTC’s COPPA settlement, YouTube implemented stricter
policies on “made for kids” content, potentially reducing the
algorithmic reach or monetization potential of explicit ad-
vertising aimed at minors.
5.2 Qualitative Nuances: Vlog vs. Staged Drama
During our human validation process, we observed that
distinguishing between organic documentation (vlogging)
and performative labor (staged drama) is highly nuanced.
Some channels operate with a fundamentally exploitative
premise (e.g., daily scripted pranks), while others primar-
ily document family life but occasionally use exaggerated
thumbnails (emotional bait) to drive clicks. Our multimodal
pipeline’s ability to output a continuous probability score
(∈[0,1]) rather than a binary label effectively captures this
spectrum of exploitation. Videos with clickbait thumbnails
but organic content received moderate scores, while highly
scripted, high-conflict videos received the highest scores.
This continuous measurement highlights that exploitation in
the kidfluencer space is rarely binary; it exists on a spectrum
driven by the constant pressure to optimize for engagement.
5.3 Case Study: The Industrialized Kidfluencer
Network
To illustrate the structural dynamics our pipeline cap-
tures, we briefly describe the operational characteristics of
one of the most-subscribed children’s channel networks
(anonymized). This network operates 13 YouTube channels
across multiple languages, collectively reaching over 300
million subscribers. A 50-person professional production
team manages daily content output, including scripted narra-
tives, custom animations, elaborate physical sets, and post-
production editing indistinguishable from broadcast televi-
sion. Each child in the family maintains independent ac-
counts across YouTube, TikTok, Instagram, and Facebook,
with near-daily uploads on each platform. Thumbnails fol-
low a systematic design strategy: saturated colors, children’s
faces in exaggerated emotional expressions, and text over-
lays engineered for maximum click-through rates.
Crucially, while this operation presents itself as organic
family content, the scale of production (daily uploads across
13 channels with professional crews) represents a labor in-
tensity that far exceeds what any individual family could
sustain without treating content creation as a full-time com-
mercial enterprise. In our framework, such channels con-
sistently score high on performative labor and commercial
content dimensions—not because any single video is neces-
sarily harmful, but because thesystemic patternreveals an
industrial operation built around children’s continuous on-
camera presence.
5.4 Proxy Indicators and the Limits of
Observational Measurement
A critical epistemological caveat must be acknowledged: our
exploitation score measures theintensity of content features
associated with exploitation risk, not exploitation itself. A

high score indicates that a video exhibits characteristics—
scripted performativity, emotional manipulation in meta-
data, commercial framing—that prior literature identifies
as risk factors (Clark and Jno-Charles 2025; Divon et al.
2025). However, a child may enthusiastically participate in a
challenge video without experiencing harm, and conversely,
exploitation may occur in videos that appear benign from
metadata alone.
We therefore frame our findings not as evidence that spe-
cific children are being exploited, but as evidence thatplat-
form incentive structures systematically reward content
features associated with exploitation risk. This framing
strengthens rather than weakens our policy argument: re-
gardless of whether any individual family is exploiting their
children, the engagement premium we document creates
structural pressure toward increasingly intensive child labor.
The policy concern is not any single video, but the cumu-
lative incentive gradient that shapes creator behavior across
the ecosystem.
5.5 Policy Implications
Our findings have direct implications for the ongoing pol-
icy debate surrounding child digital labor. Current legisla-
tive frameworks, such as the Illinois PA 103-0556 and the
proposed federal KIDS Act (S. 1409), focus primarily on fi-
nancial compensation—mandating trust funds and limiting
working hours. While these protections are necessary, our
results suggest they are insufficient. The engagement pre-
mium we document operates independently of direct mon-
etary compensation: a child’s performative labor is strongly
associated with views (and thus advertising revenue) regard-
less of whether the child receives a share of that income.
Platform-level interventions may be more effective than
purely legislative approaches. Our finding that commercial
content does not benefit from the engagement premium sug-
gests that YouTube’s existing policies on “made for kids”
content may already be partially effective at reducing the
incentive for overt commercialization. Similar mechanisms
could be extended to address the performativity premium:
for instance, platforms could reduce algorithmic amplifica-
tion of content flagged as involving intensive child labor, or
implement friction mechanisms (e.g., mandatory cooling-
off periods) for channels that consistently produce high-
exploitation content. However, such interventions must be
carefully designed to avoid penalizing legitimate family doc-
umentation or cultural expression.
5.6 Methodological Contributions
This study demonstrates the efficacy of multimodal weak su-
pervision for large-scale observational auditing. By combin-
ing LLM text analysis and VLM visual analysis, we suc-
cessfully scaled the operationalization of complex ethical
concepts without requiring massive manual ground truth.
Our multi-annotator validation (overall F1= 0.793, re-
call= 0.960, macro-average per-dimension F1= 0.911)
demonstrates that the pipeline reliably identifies specific ex-
ploitation risk indicators in a manner consistent with trained
human judgment. The approach is particularly well-suited
to domains where ground truth is inherently subjective and
expensive to obtain at scale, such as hate speech detection,
misinformation assessment, and content safety evaluation.
5.7 Limitations and Future Work
This study has several limitations. First, while we conducted
a multi-annotator validation (N= 107), we observed that
different annotators exhibited varying thresholds for defin-
ing exploitation risk, highlighting the inherent subjectivity
of the concept. For example, a more conservative annotator
often labeled family game night videos as low-risk, whereas
the primary annotator flagged them as performative labor.
While inter-rater agreement on overlapping samples was
perfect (Cohen’sκ= 1.0), this was based on a small over-
lap set (n= 3); future work should expand the overlap set
to systematically study these subjective disagreements. Fur-
thermore, our dimensions are proxy indicators of exploita-
tion risk, not definitive proof of UNCRC violations. A child
may happily participate in a challenge video without being
exploited, but the systemic prevalence of such content indi-
cates a high baseline of labor intensity.
Second, our analysis relies on observational data. We
measureengagement metrics(views), which are proxies
for algorithmic reach, but we cannot claim a direct causal
link to YouTube’s internal recommendation weights (Rieder,
Matamoros-Fern´andez, and Coromina 2018). The engage-
ment premium we observe may reflect audience preferences,
algorithmic amplification, or both.
Third, our VLM classification primarily analyzed video
titles, thumbnails, and descriptions; future work should in-
corporate full video transcripts and duration data to cap-
ture intra-video dynamics. A video’s thumbnail may suggest
emotional bait while the actual content is benign, or con-
versely, a neutral thumbnail may mask exploitative content
within the video itself. Incorporating temporal signals (e.g.,
video duration, upload frequency) could also reveal patterns
of labor intensity that metadata alone cannot capture.
Fourth, our sample is limited to English-language chan-
nels based in North America and the UK. The kidflu-
encer economy operates globally, with significant markets
in South Korea, Brazil, India, and Southeast Asia. Cross-
cultural analyses may reveal different exploitation patterns
and engagement dynamics shaped by distinct regulatory en-
vironments, cultural norms around childhood, and platform-
specific affordances (e.g., YouTube Shorts vs. long-form
content).
Finally, our study captures a cross-sectional snapshot.
Longitudinal analyses tracking how individual channels
evolve their content strategies in response to engagement
feedback would provide stronger evidence for the causal
mechanisms underlying the performativity premium.
6 Ethics and Positionality Statement
6.1 Ethical Considerations
This research utilizes publicly available, observational data
from YouTube via the official API. The study was deemed
IRB-exempt by our institutional review board as it involves
no direct interaction with human subjects or minors, and an-
alyzes public figures participating in the digital economy.

However, we recognize that the subjects of these videos are
children who cannot legally consent to their digital footprint.
To minimize potential harm, we adhered to strict data min-
imization principles. We did not download or store video
files; we only retrieved metadata, thumbnails, and descrip-
tions necessary for the analysis. Furthermore, we report all
findings as aggregate statistics or anonymized trends. When
discussing specific examples or qualitative findings, we in-
tentionally obscure identifying details to prevent further am-
plification or privacy violations of the children involved.
Our goal is to audit the systemic incentives of the platform
ecosystem, not to target or shame individual families.
6.2 Positionality Statement
The authors approach this research from the perspective
of computational social scientists and algorithmic auditors
based in North America. We acknowledge that our op-
erationalization of “exploitation” is grounded in Western
frameworks of child rights (e.g., the UNCRC) and North
American legislative contexts (e.g., the Illinois PA 103-
0556). The kidfluencer economy operates globally, and cul-
tural norms regarding child labor, family documentation,
and privacy vary significantly. Our analysis of English-
language channels may not capture the nuances of exploita-
tion in other cultural contexts. We also recognize the inher-
ent subjectivity in labeling content as “exploitative.” By em-
ploying a weak supervision approach and providing trans-
parent validation metrics, we aim to make our assumptions
explicit and open to critique, rather than presenting our
pipeline’s outputs as absolute ground truth.
7 Conclusion
As the kidfluencer economy matures, regulatory focus must
expand beyond financial compensation to address the struc-
tural forces shaping content creation. Our multimodal au-
dit of 4,208 videos across 56 kid-centric channels demon-
strates that engagement metrics are significantly associated
with content featuring child performative labor, privacy vio-
lations, and emotional bait, while overt commercial content
does not benefit from this premium. By highlighting this
“performativity premium,” this study underscores the need
for platform-level interventions that disincentivize the com-
modification of child labor and stress.
References
2024. Illinois Child Influencer Act. 820 ILCS 152.
Abidin, C. 2015. Micromicrocelebrity: Branding babies on
the internet.M/C Journal, 18(5).
Anderson, J. 2025. Growing up online: Children, family
vlogs, and the monetization of childhood.
Bach, S. H.; et al. 2019. Snorkel DryBell: A case study in
deploying weak supervision at industrial scale. InProceed-
ings of the 2019 International Conference on Management
of Data.
Bouchaud, P.; et al. 2024. Auditing the audits: Evaluating
methodologies for social media platform audits.Applied
Network Science, 9: 55.
Bridle, J. 2017. Something is wrong on the internet.
Medium.
Clark, D. R.; and Jno-Charles, A. B. 2025. The child labor in
social media: Kidfluencers, ethics of care, and exploitation.
Journal of Business Ethics.
Covington, P.; Adams, J.; and Sargin, E. 2016. Deep neural
networks for YouTube recommendations. InProceedings of
the 10th ACM Conference on Recommender Systems.
Divon, T.; et al. 2025. Children as concealed commodities.
New Media & Society.
Gilardi, F.; Alizadeh, M.; and Kubli, M. 2023. ChatGPT
outperforms crowd workers for text-annotation tasks.Pro-
ceedings of the National Academy of Sciences, 120(30).
Habib, H. 2025. Auditing algorithmic bias with
emotionally-agentic sock puppets.arXiv preprint
arXiv:2501.15048.
Haroon, M.; Wojcieszak, M.; Chhabra, A.; Liu, X.; Mo-
hammadi, P.; Shrestha, P.; and Muric, G. 2023. Auditing
YouTube’s recommendation system for ideologically conge-
nial, extreme, and problematic recommendations.Proceed-
ings of the National Academy of Sciences, 120(50).
Hussein, E.; Juneja, P.; and Mitra, T. 2020. Measuring mis-
information in video search platforms: An audit study on
YouTube.Proceedings of the ACM on Human-Computer
Interaction, 4(CSCW1).
Husz´ar, F.; Ktena, S. I.; O’Brien, C.; Belli, L.; Schlaikjer, A.;
and Ber, M. 2022. Algorithmic amplification of politics on
Twitter.Proceedings of the National Academy of Sciences,
119(1).
Johnson, J. M.; and Khoshgoftaar, T. M. 2022. A survey on
classifying big data with label noise.ACM Journal of Data
and Information Quality, 14(4).
Keskin, A. D. 2023. Sharenting syndrome: An appropriate
use of social media?Cureus, 15(5).
Kopeck´y, K.; et al. 2020. The phenomenon of sharenting
and its risks in the online environment.Children and Youth
Services Review, 119.
Ma, H.; et al. 2023. Adapting large language models for
content moderation.arXiv preprint.
Metaxa, D.; Park, J. S.; Karahalios, K.; and Sandvig, C.
2021. Auditing algorithms: Understanding algorithmic sys-
tems from the outside in.F oundations and Trends in Human-
Computer Interaction, 14(4).
Papadamou, K.; Papasavva, A.; Zannettou, S.; Blackburn, J.;
Kourtellis, N.; Leontiadis, I.; Stringhini, G.; and Sirivianos,
M. 2020. Disturbed YouTube for kids: Characterizing and
detecting inappropriate videos targeting young children. In
Proceedings of the International AAAI Conference on Web
and Social Media, volume 14, 522–533.
Ratner, A.; Bach, S. H.; Ehrenberg, H.; Fries, J.; Wu, S.;
and R´e, C. 2017. Snorkel: Rapid training data creation with
weak supervision.Proceedings of the VLDB Endowment,
11(3).
Ratner, A.; De Sa, C.; Wu, S.; Selsam, D.; and R´e, C. 2016.
Data programming: Creating large training sets, quickly. In

Advances in Neural Information Processing Systems, vol-
ume 29.
Ribeiro, M. H.; Ottoni, R.; West, R.; Almeida, V . A.; and
Meira Jr, W. 2020. Auditing radicalization pathways on
YouTube. InProceedings of the 2020 Conference on Fair-
ness, Accountability, and Transparency, 131–141.
Rieder, B.; Matamoros-Fern ´andez, A.; and Coromina, ¨O.
2018. From ranking algorithms to ‘ranking cultures’: In-
vestigating the modulation of visibility in YouTube search
results.Convergence, 24(1).
Sandvig, C.; Hamilton, K.; Karahalios, K.; and Langbort, C.
2014. Auditing algorithms: Research methods for detect-
ing discrimination on internet platforms. InData and Dis-
crimination: Converting Critical Concerns into Productive
Inquiry.
Steinberg, S. B. 2017. Sharenting: Children’s privacy in the
age of social media.Emory Law Journal, 66: 839.
Tahir, R.; et al. 2019. Bringing the kid back into YouTube
Kids. InProceedings of the International Conference on
Advances in Social Networks Analysis and Mining.
T¨ornberg, P. 2024. ChatGPT-4 outperforms experts and
crowd workers in annotating political Twitter messages with
zero-shot learning.arXiv preprint.
UNICEF. 2025. Trends in online platform regulation and
children’s rights.
Zhou, R.; Khemmarat, S.; and Gao, L. 2010. The impact of
YouTube recommendation system on video views. InPro-
ceedings of the 10th ACM SIGCOMM Conference on Inter-
net Measurement.
A Labeling Function Inventory
Table 4 provides the complete list of 33 labeling functions
(LFs) used in our weak supervision pipeline. Each LF is
trained independently per dimension using Snorkel’s label
model, which learns the accuracy and correlation structure
of the LFs without requiring ground truth labels.
B Snorkel Label Model Diagnostics
Table 5 reports the standard diagnostic metrics for our
Snorkel label model, computed per dimension.
C LLM and VLM Prompts
C.1 LLM Title Classification Prompt
(GPT-4.1-nano)
The following system prompt is used for text-only classifi-
cation of video titles:
You are an expert in children’s media
and child exploitation research. You
will classify YouTube video titles from
kidfluencer/family vlog channels along
5 dimensions. For each title, output a
JSON object with these fields:
- ‘‘performative’’: 1 if the child
is clearly performing/working FOR the
video (challenges, roleplay, scripted
skits, dance routines, unboxing,
reviews, pranks, games designed
for content). 0 if organic/natural
(birthday, vacation, daily life that
would happen without a camera). -1 if
ambiguous.
- ‘‘emotional bait’’: 1 if the title
uses exaggerated emotional language
or manufactured drama to attract
clicks. This includes: ALL CAPS
shouting, excessive punctuation,
fake emergencies, exaggerated
reactions, manufactured urgency. 0 if
calm/descriptive.
- ‘‘narrative conflict’’: 1 if the
title implies interpersonal conflict,
mystery, or dramatic tension (theft,
confrontation, betrayal, punishment,
secrets revealed). 0 if no narrative
tension.
- ‘‘challenge format’’: 1 if the title
indicates a challenge, competition, or
game format (‘‘24 HOURS’’, ‘‘LAST TO
LEAVE’’, ‘‘VS’’, dares, contests). 0 if
not.
- ‘‘commercial content’’: 1 if the
title references specific brands,
products, stores, or commercial
activities. 0 if no brand/product
reference.
C.2 VLM Multimodal Prompt (GPT-4.1-mini
Vision)
The following prompt is sent with the video thumbnail (low-
detail mode), title, and first 300 characters of the description:
You are analyzing a YouTube video
thumbnail and title to assess potential
child exploitation signals. The video
is from a family/kid YouTube channel.
Analyze the thumbnail image and title
together. For each dimension below,
provide a score from 0.0 to 1.0:
1. performative labor (0.0--1.0): Is
the child performing scripted/staged
content? Score HIGH if the activity
would NOT happen without the camera.
2. emotional bait (0.0--1.0): Does
the thumbnail/title use exaggerated
emotions to attract clicks? Look for:
children with mouths wide open in
shock, crying faces, ALL CAPS.
3. narrative conflict (0.0--1.0):
Does the content manufacture drama or
conflict?
4. challenge format (0.0--1.0): Is this
a challenge/dare/competition format?
5. commercial content (0.0--1.0): Is
there visible product placement, brand
logos, or sponsored content signals?
6. privacy violation (0.0--1.0): Does
the content expose the child’s private
moments, body, or medical situations?

7. overall exploitative (0.0--1.0):
Considering ALL dimensions, is this
video likely exploitative?
Return ONLY valid JSON.

Dim. LF Name Type Cov. Description
Perf. Labor
lf llm performative LLM 1.000 GPT-4.1-nano classifies title as performa-
tive (scripted/staged) vs. organic
lf vlm performative high VLM 0.780 GPT-4.1-mini Vision scores≥0.7for per-
formative labor
lf vlm performative med VLM 0.932 GPT-4.1-mini Vision scores≥0.4for per-
formative labor
lf scripted keywords Rule 0.253 Title contains scripted content keywords
(skit, challenge, prank, etc.)
lf organic keywords Rule 0.076 Title contains organic family keywords
(birthday, vacation)→NOT exploit
lf roleplay title Rule 0.031 Title contains roleplay/acting keywords
lf desc scripted Rule 0.408 Description contains scripted production in-
dicators
lf duration long Meta 0.035 Video duration>30 minutes (long-form
scripted content)
Emot. Bait
lf llm emotional LLM 0.100 GPT-4.1-nano classifies title as emotional
bait
lf vlm emotional VLM 0.625 GPT-4.1-mini Vision scores emotional bait
from thumbnail+title
lf emotional caps Rule 0.179 Title has>60%uppercase characters
(ALL CAPS clickbait)
lf emotional punct Rule 0.063 Title contains≥3exclamation marks
lf emotional keywords Rule 0.018 Title contains emotional distress words
(crying, meltdown, etc.)
lf emotional emojis Rule 0.001 Title contains emotional emojis (crying
face, etc.)
Narr. Confl.
lf llm narrative LLM 0.091 GPT-4.1-nano classifies title as narrative
conflict
lf vlm narrative VLM 0.753 GPT-4.1-mini Vision scores narrative con-
flict
lf conflict keywords Rule 0.056 Title contains conflict keywords (fight,
stolen, arrested, etc.)
lf prank gone wrong Rule 0.016 Title contains “prank” or “gone wrong” pat-
terns
lf clickbait patterns Rule 0.004 Title matches clickbait structural patterns
Challenge
lf llm challenge LLM 0.175 GPT-4.1-nano classifies title as challenge
format
lf vlm challenge VLM 0.903 GPT-4.1-mini Vision scores challenge for-
mat
lf challenge keywords Rule 0.136 Title contains challenge keywords (24
hours, last to, vs, etc.)
lf competition format Rule 0.051 Title matches competition format patterns
lf duration challenge Meta 0.003 Video duration matches typical challenge
length
Commercial
lf llm commercial LLM 0.032 GPT-4.1-nano classifies title as commercial
content
lf vlm commercial VLM 0.715 GPT-4.1-mini Vision scores commercial
signals from thumbnail
lf commercial title Rule 0.136 Title contains brand names or product ref-
erences
lf commercial desc Rule 0.129 Description contains affiliate links, discount
codes, or #ad
lf commercial tags Rule 0.345 Video tags contain commercial/brand indi-
cators
Privacy
lf llm privacy LLM 0.027 GPT-4.1-nano classifies title as privacy vio-
lation
lf vlm privacy VLM 0.818 GPT-4.1-mini Vision scores privacy con-
cern from thumbnail
lf privacy keywords Rule 0.034 Title contains privacy-sensitive keywords
(bath, potty, etc.)
lf privacy medical desc Rule 0.013 Description mentions medical/health de-
tails of child
Table 4: Complete inventory of 33 labeling functions. Type: LLM = GPT-4.1-nano text classification; VLM = GPT-4.1-mini
Vision multimodal analysis; Rule = keyword/regex heuristic; Meta = metadata-based (duration, tags). Coverage = proportion
of videos receiving a non-abstain vote.

Dimension # LFs Abstain % Mean Cov. Mean Conf.
Performative Labor 8 0.0% 0.439 0.243
Emotional Bait 6 29.2% 0.164 0.009
Narrative Conflict 5 23.1% 0.184 0.002
Challenge Format 5 8.7% 0.253 0.008
Commercial Content 5 14.7% 0.271 0.096
Privacy Violation 4 16.2% 0.223 0.012
Aggregate (33 LFs)33 — 0.271 0.078
Table 5: Snorkel label model diagnostics per dimension. Abstain % = proportion of videos where no LF votes (label model uses
prior). Mean Cov. = average LF coverage. Mean Conf. = average pairwise conflict rate among LFs.
