---
title: 'Generative AI in a new era of computer model-informed tobacco research: a short report'
url: https://doi.org/10.1136/tc-2024-058887
category: ai-marketing
subcategory: empirical
date: 2025-01
venue: Tobacco Control
authors:
- Julia Vassey
- Chris J. Kennedy
- Ho-Chun Herbert Chang
source: openalex-oa
pdf_url: https://tobaccocontrol.bmj.com/content/tobaccocontrol/early/2025/01/30/tc-2024-058887.full.pdf
pages: 4
chars: 27822
fetched_at: '2026-11-08T18:52:53+00:00'
kb_version: 1
---

# Generative AI in a new era of computer model-informed tobacco research: a short report

1
Vassey J, et al. Tob Control 2025;0:1–4. doi:10.1136/tc-2024-058887
Generative AI in a new era of computer model-
informed tobacco research:
 a short report
Julia Vassey   ,1 Chris J Kennedy   ,2,3 Ho- Chun Herbert Chang    ,4
Jennifer B Unger
   1
Short report
To cite: Vassey J, Kennedy CJ,
Chang H-

CH, et al.
Tob Control Epub ahead of
print: [please include Day
Month Year]. doi:10.1136/
tc-2024-058887
 ► Additional supplemental
material is published online
only. To view, please visit the
journal online (https://

doi.

org/
10.

1136/

tc-

2024-

058887).
1Department of Population
and Public Health Sciences,
University of Southern
California, Los Angeles,
California, USA
2Center for Precision Psychiatry,
Massachusetts General Hospital,
Boston, Massachusetts, USA
3Department of Psychiatry,
Harvard Medical School, Boston,
USA
4Department of Quantitative
Social Science, Dartmouth
College, Hanover, New
Hampshire, USA
Correspondence to
Dr Julia Vassey;
vassey@

usc.

edu
Received 21 June 2024
Accepted 22 January 2025
© Author(s) (or their
employer(s)) 2025. Re-
 use
permitted under CC BY
-
 NC
. No
commercial re-
 use
. See rights
and permissions. Published by
BMJ Group.
ABSTRACT
Background
 Social media influencers who promote
e-
 cigarettes on Instagr
am or TikTok for tobacco brands
use marketing tactics to increase the appeal of their
promotional content, for example, depicting e-
 cigarettes
alongside healthy lifestyle or entertainment imagery that
could decrease youths’ risk perceptions of e-
 cigarettes
.
Monitoring the prevalence of such content on social
media using computer vision and generative AI (artificial
intelligence) can provide valuable data for tobacco
regulatory science (TRS).
Methods
 W
e selected 102 Instagram and TikTok
videos posted by micro-
 influencers in 2021–2024 who
promoted e-
 cigarettes alongside posts featuring four
themes:
 cannabis, entertainment, fashion or healthy
lifestyle. We used OpenAI’s GPT-
 4o multimodal large-

scale visual linguistic model to detect the presence of
nicotine v
aping, cannabis vaping, fashion, entertainment
and healthy lifestyle. The model did not require any
additional training and improved its performance as we
modified the text prompt.
Results
 T
he model’s accuracy was 87% for nicotine
vaping, 96% for cannabis vaping, 99% for fashion, 96%
for entertainment and 98% for healthy lifestyle.
Conclusions
 Gener
ative AI can achieve accurate object
detection with zero-
 shot learning (no additional tr
aining
of the pretrained model). This model can be applied to
big data-
 scale sample sizes of images and videos to
detect e-
 cigarette-
 related and other substance-
 related
promotional content and contexts (eg,
 healthy lifestyle)
used for the promotion of these products on social
media, providing valuable data for TRS.
INTRODUCTION
Social media influencers who promote e-  cigarettes
on Instagram or T
ikT ok for tobacco brands use
diverse marketing features to increase audiences’
appeal to their promotional content. For example,
micro-
 influencers (content
creators with∼10

000

to
∼100

000 followers) 1 often promote e-  cigarettes
alongside posts
 featuring positively perceived
lifestyle contexts or themes (eg, healthy life -
style, gaming) or alongside cannabis use. 1–4 Such
marketing may affect youth perceptions of influ-
encer relatability and contribute to normalisation
of e-
 cigarette and other substance
(eg, cannabis)
use.5–8 While some social media platforms’ commu-
nity guidelines (eg, Instagram and TikT ok) prohibit
influencer e-
 cigarette-
 related
promotional posts,
they still exist on social media. 9 The platforms
detect and remove some of this content10 but do not
use efficient algorithms to eliminate all e-
 cigarette
promotional posts.
Data
on the prevalence of tobacco-
 related
promotional
posts is valuable for tobacco regu-
latory science. Prior studies used human qualita -
tive coding 11–15 and automated machine learning
approaches16–20 to analyse tobacco-  related images
and videos. Automated approaches include
computer vision, a field of artificial intelligence
(AI) that applies machine learning and artificial
neural networks to analyse visual content of image-

based and video-
 based e-
 cigarette-
 related promo -
tional
content on social media. Prior research 16 20
used convolutional neural networks-
 based models
(that gradually
learn information from simple to
more complex patterns of an image) 21 to classify
e-
 cigarette
products and nicotine warning labels
in e-

cigarette-

related Instagram images. Another
study19 applied a transformer-  based model (that
WHAT IS ALREADY KNOWN ON THIS TOPIC
 ⇒ Research has shown that computer vision
models can be trained to detect e-
 cigarette
objects in social media videos
, including
e-
 cigarette promotional content posted by
influencers
. Generative artificial intelligence
(AI) models have not yet been applied to detect
e-
 cigarette or cannabis products and different
lifestyle contexts such as entertainment,
 fashion
or healthy lifestyle, depicted alongside e-

cigarette promotions
, in social media videos.
WHAT THIS STUDY ADDS
 ⇒ A generative AI model (GPT- 4o) w as able to
accurately detect the presence of nicotine and
cannabis vaping as well as entertainment,
fashion and healthy lifestyle themes in
Instagram and TikTok videos featuring
micro-
 influencers
. The model did not require
any additional training and improved its
performance as we modified the text prompt
guiding the model to detect these themes in
videos.
HOW THIS STUDY MIGHT AFFECT RESEARCH,
PRACTICE OR POLICY
 ⇒ The pilot study demonstrated that GPT- 4o and
related models can now be applied to big data-

scale sample sizes of images and videos to
detect not only e-
 cigarette or other substance-

related (eg,
 cannabis) promotional content but
also contexts (eg, healthy lifestyle) used for
promotion of these products on social media,
providing valuable data for tobacco regulatory
science.
Protected by copyright, including for uses related to text and data mining, AI training, and similar technologies.
. Marburg
at Universitatsbibliothek on November 8, 2026 http://tobaccocontrol.bmj.com/Downloaded from 30 January 2025. 10.1136/tc-2024-058887 on Tob Control: first published as

2
Vassey J, et al. Tob Control 2025;0:1–4. doi:10.1136/tc-2024-058887
Short report
selectively focuses on important image regions) 22 to identify
e-
 cigarette-
 related products
and attributes (ie, mod and pod
devices, e-
 juices
and their flavour names, nicotine warning
labels and e-
 cigarette brand names). These models required large
training samples to detect research-
 specific objects.19
Newer, more efficient transformer-  based models such as
OpenAI’s GPT-
 4
(generative pretrained transformers) can often
solve human-
 level object detection tasks without additional
model training.23–25 These models, originally trained on text and
visual elements from numerous online open sources, can detect
objects accurately without building a custom model fine-
 tuned
on a
training data set (ie, ‘zero-
 shot’ learning).26 GPT- 4 outper-
formed over 20 other multimodal models (eg, BLIP
-
 2, LLaV
A-

1.5) that process text and image-
 based
data.27 GPT- 4’s capability
of analysing images and videos is an upgrade from
the earlier
GPT-
 3 version that analysed text data. 25 28 In this pilot proof-
of
-
 concept study
, we applied GPT-
 4o, a
multimodal large-
 scale
visual linguistic model (L
VM), to detect nicotine or cannabis
vaping, and contexts (ie, healthy lifestyle, entertainment and
fashion) appearing alongside promotions of these substances, in
Instagram and TikT ok videos featuring micro-
 influencers.1
METHODS
Social media data collection
Micro- influencers were selected from 219 profiles identified in
prior research1 19 using social media data provider Meltwater. 29
From these, we randomly selected nine profiles who posted
about at least one theme (cannabis, entertainment, fashion or
healthy lifestyle), besides e-
 cigarettes. V
ideos reflecting the study
themes were either drawn from 40
 000 Instagram and
TikT ok
e-
 cigarette-
 related publicly availa
ble videos collected in prior
research1 19 or directly downloaded for this study from the nine
selected micro-
 influencers’ Instagram and T
ikT ok pages. The
data collection resulted in a final sample of 102 videos (mean
duration=29
 s) posted in 2021–2024.
Description of themes
We selected the influencer videos featuring nicotine vaping, one
of the four other themes, or a combination of those in one video;
22 videos contained nicotine vaping (disposable or refillable
pod devices), while 20 videos each featured cannabis (dispos -
able pod devices, blunts or bongs (water pipes)), healthy lifestyle
(exercising, hiking, playing tennis, swimming or skateboarding),
entertainment (DJ-
 ing, dancing) or fashion (modelling); 12
videos contained multiple themes.
Model architecture
We applied a novel model that uses the transformer architec-
ture and OpenAI’s GPT-
 4.23 24 28  GPT- 4o, a multimodal LVM,
combines text and visual comprehension. 25 It takes images
and videos (broken into frames that are analysed as images) as
input and, using text instructions in a prompt we engineered
to guide the model, provides textual responses based on the
visual content. Model performance gets improved with prompt
modifications. Figure

1 shows an example of an input video, the
prompt we engineered to guide the model, and the output. The
prompt guided the model to provide a probability of a specific
theme’s presence in a video. We iterated through multiple
prompt revisions until we found reliable model outputs that
could be extracted using simple text processing. T o verify the
robustness of the results, we ran the same prompt three times 30
and the results remained consistent. For theme detection in each
video, we selected four frames evenly distributed over the whole
duration of a video. The decision to analyse four frames instead
of the entire video was driven by efficiency and to minimise the
cost per token (the amount of information processed per query)
set by OpenAI’s API. The output included one probability per
theme in a video based on the prompt (figure

1).
Model performance evaluation
The model accuracy was evaluated against the true content
observed in the videos, as described by human coders (a graduate
student at the University of Southern California and an author
of this manuscript (JV)). Inter-
 rater reliability
(Kappa) was 0.99.
We assessed GPT-
 4’s
accuracy, the area under the curve (AUC),
precision, recall and F1 score for all themes. T o validate GPT-
 4’s
performance on the nicotine vaping theme, where it showed the
Figure 1 T heme detection with generative AI multimodal large-  scale visual linguistic model GPT -  4o . The figure features an example of a 10  s TikTok
video clip as an input (A) for the model to perform theme detection, a text prompt that guides the model to identify nicotine vaping, cannabis vaping,
fashion, entertainment or healthy lifestyle (B), and the output showing probability responses for each theme (C). A publicly available video featuring
a person in this figure was sourced from the public Instagram account of an influencer Vapes_aby in August 2023 (https://www.instagram.com/
vapes_aby/).
Protected by copyright, including for uses related to text and data mining, AI training, and similar technologies.
. Marburg
at Universitatsbibliothek on November 8, 2026 http://tobaccocontrol.bmj.com/Downloaded from 30 January 2025. 10.1136/tc-2024-058887 on Tob Control: first published as

3
Vassey J, et al. Tob Control 2025;0:1–4. doi:10.1136/tc-2024-058887
Short report
lowest accuracy, we used the DyHead model developed in our
prior research specifically for e-
 cigarette object detection.19
RESULTS
GPT- 4o’s accuracy was 87% for nicotine vaping, 96% for
cannabis vaping, 99% for fashion, 96% for entertainment
and 98% for healthy lifestyle, with AUC, precision, recall and
F1-
 score ranging from 0.75 to 1 across the themes (online
supplemental tables 1 and 2). The DyHead validation model
achieved 81% accuracy for e-
 cigarette (nicotine vaping) theme
detection—comparable but slightly lower than the GPT
-
 4o
model’s
87% accuracy for nicotine vaping. The GPT-
 4o and
DyHead models’ A
UC (online supplemental table 1), precision,
recall and F1-
 scores (online supplemental table 2) for nicotine
vaping detection were also comparable but slightly lower overall
for DyHead. Online supplemental tables
3 and 4 present the
GPT-
 4o model’s
predicted probabilities for theme detection
across all videos and for multiple themes in 12 videos, respec-
tively. Online supplemental figure 1 provides error analyses for
both models, while online supplemental figure 2 displays the
distribution of confidence scores from the validation model.
DISCUSSION
This proof-  of -  concept study showed that GPT -  4o can accu -
rately identify e-
 cigarettes, cannab
is, entertainment, fashion and
healthy lifestyle. GPT-
 4o and related models can
now be applied
to big data-
 scale
sample sizes of images and videos to detect not
only nicotine or cannabis products but also contexts appearing
alongside promotions of these substances on social media. Esti-
mating the prevalence of these marketing features is important
since they could increase audiences’ (including youth) appeal to
e-
 cigarette
products and contribute to normalisation of e-
 ciga
-
rette and other substance use.
GPT-
 4o achieved
high accuracy with zero-
 shot learning,
that
is, without explicit training on a labelled data set of images or
videos. This high accuracy may reflect the scope of GPT-
 4o’s
pretraining and
potential exposure to similar content. Perfor -
mance improved as we modified the text prompt guiding the
model. Zero-
 shot learning
was not possible in prior studies
that used non-
 generative AI
transformer-
 based
models which
required a large training sample of images. Fine-
 tuning of GPT
-

based models might still be needed for some research tasks;
however
, their zero-
 shot performance will
likely only improve
over time as these models get constantly upgraded.
GPT-
 4o’s performance on small object detection such as nico
-
tine vaping was lower than on the other themes but slightly
higher than DyHead’s performance on nicotine vaping detec-
tion. The non-  OpenAI DyHead model (developed in
our prior
research)19 was specifically chosen for validation to compare
OpenAI’s GPT-
 4o performance with non-  OpenAI approaches,
particularly
for small object detection, such as e-
 cigarettes,
where GPT
-
 4o
demonstrated its lowest performance among
the evaluated themes. DyHead is an e-
 cigarette object detection
model focusing on spatial
object recognition whereas GPT-
 4o
identifies broader themes by analysing data without spatial local-
isation. While using DyHead model predictions as a comparator
for the GPT
-
 4o
model’s results is reasonable, the DyHead model
provides more detailed frame-
 level inference not currently
possible via
GPT and was intended for a different use case than
video-
 level
theme identification. As such, comparing theme-

detection accuracy
between the two models captures only one
aspect of their respective utilities.
GPT-
 style models
provide new self-
 service
capabilities to
tobacco researchers due to the web-
 based
interface for inputting
research questions in written language and generating model
predictions. Researchers without deep learning expertise are
now empowered to define marketing themes, iterate on prompts
and take advantage of these models without coding directly or
creating custom models that need to be maintained and updated
over time. GPT-
 4 can
also be useful to analyse data sets with
no protected health information, (as is the case with publicly
available social media imagery used in this study). Overall, this
hints at a new era of model-
 informed tobacco
research broadly
available throughout the research community. However, the goal
of this pilot study was not to identify the best suitable model but
rather to explore an alternative to the custom models used in
prior research.16–20 This manuscript offers the scientific commu-
nity the opportunity to see the strengths and limitations of the
GPT-
 4 and make
a decision about which model suits best to their
research question.30
Limitations
GPT- 4o sometimes misclassified cannabis vaping as nicotine
vaping, likely due to the high resemblance of disposable devices,4
which could only be distinguished by cannabis logos or brand
names that the model occasionally missed. False negatives for
nicotine vaping detection for both GPT-
 4o and DyHead were
caused
by obscured objects (a white pod on a white background)
and missed objects likely due to sampling only four frames (in
one video a pod did not appear throughout the whole clip).
GPT-
 4o failed
to detect one older-
 generation pod device, likely
due
to the absence of such examples in the pretraining data
set, whereas DyHead identified it accurately. Future research
could evaluate GPT-
 4o’s performance
on out-
 of
-
 distribution
samples
(eg, niche topics or unique objects) to better understand
its generalisability. DyHead was used only for nicotine vaping
detection. We treated any disposable vaping device as nicotine
vaping while assessing DyHead’s accuracy, since the model was
specifically designed for e-
 cigarette object detection and was
not trained to distinguish between identically
shaped dispos -
able nicotine and cannabis vape devices based on logos or brand
names shown on the device. Unlike GPT-
 4o, DyHead cannot
detect broad themes (eg,
fashion). Given GPT-
 4o’s high perfor-
mance on broad theme detection in this study and its superior
performance compared with
other models (eg, LLaVA-
 1.5) in
prior research,27 we did not apply alternative models to validate
its performance on broad theme detection. We used only 102
videos for this study. Although small sample sizes are typical for
pilot studies, future work should evaluate larger samples to esti-
mate performance more precisely.
CONCLUSION
This proof-  of -  concept study showed that the GPT-  4o model
was capable
of accurate e-
 cigarette-
 related and non-
 e-
 cigarette-

related theme detection featured in influencer marketing
without any fine-
 tuning of the model
(additional training of the
pretrained model to improve accuracy). The study adds evidence
to the existing literature16–20 that computer vision and generative
AI models can now be applied to big data-
 scale
sample sizes of
images and videos to detect not only nicotine or cannabis prod -
ucts but also contexts appearing alongside promotions of these
substances on social media.
X Julia Vassey @JVassey and Chris J Kennedy @c3K
Protected by copyright, including for uses related to text and data mining, AI training, and similar technologies.
. Marburg
at Universitatsbibliothek on November 8, 2026 http://tobaccocontrol.bmj.com/Downloaded from 30 January 2025. 10.1136/tc-2024-058887 on Tob Control: first published as

4
Vassey J, et al. Tob Control 2025;0:1–4. doi:10.1136/tc-2024-058887
Short report
Contributors Concept and design—JV . Acquisition, analysis or interpretation of
data—all authors. Draft of the manuscript—JV . Critical revision of the manuscript
for important intellectual content—all authors. Prompt generation and analysis—
CJK and JV . Obtaining funding—JBU. Administrative, technical or material
support—JV , H-
 CHC and JBU
. Supervision—JBU. All coauthors approved the final
version. JV is the guarantor. We used OpenAI’s GPT-
 4o multimodal large-
 scale
visual linguistic model to detect the presence of nicotine v
aping, cannabis vaping,
fashion, entertainment and healthy lifestyle in the videos. This was the goal of this
manuscript. We did not use AI for any other purposes rather than testing the model
described in the manuscript.
Funding
 Research reported in this publication w
as supported by the National
Institute of Health (Grant # 1R01CA260459-
 01) and the NCI & FDA Center for
T
obacco Products (CTP) Award (NCI/FDA Grant #U54CA180905). The funders had
no role in study design; collection, analysis, and interpretation of data; writing the
report; and the decision to submit the report for publication. The content is solely the
responsibility of the authors and does not necessarily represent the official views of
the funders.
Competing interests
 No
, there are no competing interests.
Patient consent for publication
 Not applicable
.
Provenance and peer review
 Not commissioned;
 externally peer reviewed.
Data availability statement
 Data and the python code underlying this article are
shared on GitHub:
 https://github.com/e-cigarette-marketing-ml/vaping-gpt
Supplemental material
 T
his content has been supplied by the author(s). It
has not been vetted by BMJ Publishing Group Limited (BMJ) and may not have
been peer-
 reviewed.
 Any opinions or recommendations discussed are solely those
of the author(s) and are not endorsed by BMJ. BMJ disclaims all liability and
responsibility arising from any reliance placed on the content. Where the content
includes any translated material, BMJ does not warrant the accuracy and reliability
of the translations (including but not limited to local regulations, clinical guidelines,
terminology, drug names and drug dosages), and is not responsible for any error
and/or omissions arising from translation and adaptation or otherwise.
Open access
 T
his is an open access article distributed in accordance with the
Creative Commons Attribution Non Commercial (CC BY-
 NC 4.0) license
, which
permits others to distribute, remix, adapt, build upon this work non-
 commercially,

and license their derivative works on different terms, provided the original work is
properly cited, appropriate credit is given, any changes made indicated, and the use
is non-
 commercial
. See: http://creativecommons.org/licenses/by-nc/4.0/.
ORCID iDs
Julia Vassey http://orcid.org/0000-0003-3002-2000
Chris J Kennedy http://orcid.org/0000-0001-7444-2766
Ho-

Chun Herbert Chang http://orcid.org/0000-0002-0056-2527
Jennifer B Unger http://orcid.org/0000-0001-9064-6603
REFERENCES
 1  V assey J, Valente T, Barker J, et al. E-  cigarette br ands and social media influencers on
Instagram: a social network analysis. Tob Control 2023;32:e184–91.
 2
 P
adon AA, Maloney EK, Cappella JN. Youth-
 T
argeted E-
 cigarette Mark
eting in the US.
Tob Regul Sci 2017;3:95–101.
 3
 V
assey J, Allem J-
 P
, Barker J, et al. E-
 cigarette use and promotion by social media
influencers during videogame play on
Twitch. Tob Control 2023;32:526–7.
 4
 V
assey J, Chen-
 Sank
ey J, Unger JB. E-
 cigarette and cannabis influencer mark
eting on
social media despite regulations. Blog - Tobacco Control; 2024. Available: https://

blogs
.bmj.com/tc/2024/06/03/e-cigarette-and-cannabis-influencer-marketing-on-

social-media-despite-regulations/
 5
 Bentivegna K,
 Atuegwu NC, Oncken C, et al. Electronic Cigarettes Associated
With Incident and Polysubstance Use Among Youth. Journal of Adolescent Health
2021;68:123–9.
 6
 Childers CC
, Lemon LL, Hoy MG. #Sponsored #Ad: Agency Perspective on Influencer
Marketing Campaigns. Journal of Current Issues & Research in Advertising
2019;40:258–74.
 7
 V
ogel EA, Guillory J, Ling PM. Sponsorship Disclosures and Perceptions of E-
 cigarette
Instagr
am Posts. Tob Regul Sci 2020;6:355–68.
 8
 V
assey J, Vogel EA, Unger JB. US adolescents’ response to nicotine warning labels
in influencer e-
 cigarette mark
eting social media posts: a survey-
 based r
andomised
between-

subject experiment. Tob Control 2024;15:2024.
 9
 K
ong G, Laestadius L, Vassey J, et al. Tobacco promotion restriction policies on social
media. Tob Control 2024;33:398–403.
 10
 Rutherford BN
, Sun T, Lim CCW, et al. Changes in Viewer Engagement and
Accessibility of Popular Vaping Videos on TikTok: A 12-
 Month Prospective Study.
 Int J
Environ Res Public Health 2022;19:1141.
 11
 Galimov A,
 Albers L, Rahman T, et al. Assessing the public discourse on Twitter:
Reactions to the JUUL e-
 cigarettes ban in the United States
. Tob Induc Dis
2024;22:1–8.
 12
 Galimov
A, Vassey J, Galstyan E, et al. Ice Flavor-
 Related Discussions on
Twitter:
Content Analysis. J Med Internet Res 2022;24:e41785.
 13
 V
assey J, Donaldson SI, Dormanesh A, et al. Themes in TikTok Videos Featuring Little
Cigars and Cigarillos: Content Analysis. J Med Internet Res 2022;24:e42441.
 14
 Allem J-
 P
, Escobedo P , Chu K-
 H,
 et al. Images of Little Cigars and Cigarillos on
Instagram Identified by the Hashtag #swisher: Thematic Analysis. J Med Internet Res
2017;19:e255.
 15
 Bark
er JO, Vassey J, Chen-
 Sank
ey JC, et al. Categorizing IQOS-
 Related
Twitter
Discussions. Int J Environ Res Public Health 2021;18:4836.
 16
 V
assey J, Metayer C, Kennedy CJ, et al. #Vape: Measuring E-
 Cigarette Influence
on Instagr
am With Deep Learning and Text Analysis. Front Commun (Lausanne)
2020;4:75.
 17
 K
etonen V , Malik A. Characterizing vaping posts on Instagram by using unsupervised
machine learning. Int J Med Inform 2020;141:104223.
 18
 Jung S
, Murthy D, Bateineh BS, et al. The Normalization of Vaping on TikTok Using
Computer Vision, Natural Language Processing, and Qualitative Thematic Analysis:
Mixed Methods Study. J Med Internet Res 2024;26:e55591.
 19
 V
assey J, Kennedy CJ, Herbert Chang HC, et al. Scalable Surveillance of E-
 Cigarette
Products on Instagr
am and TikTok Using Computer Vision. Nicotine and Tobacco
Research 2024;26:552–60.
 20
 K
ennedy CJ, Vassey J, Chang HCH, et al. Tracking e-
 cigarette w
arning label compliance
on instagram with deep learning. 2021.
 21
 Deshpande
A. A beginner’s guide to understanding convolutional neural networks.
Available: https://adeshpande3.github.io/A-Beginner%27s-Guide-To-Understanding-

Convolutional-Neur
al-Networks/ [Accessed 11 Oct 2024].
 22
 Liu Z,
 Lin Y , Cao Y , et al. Swin transformer: hierarchical vision transformer using shifted
windows. 2021 IEEE/CVF International Conference on Computer Vision (ICCV);
10012–22. Montreal, QC, Canada. 10.1109/ICCV48922.2021.00986 Available:
https://openaccess.thecvf.com/content/ICCV2021/html/Liu_Swin_Transformer_

Hier
archical_Vision_Transformer_Using_Shifted_Windows_ICCV_2021_paper.html
 23
 OpenAI AJ
, Achiam J, Adler S, et al. GPT-
 4 technical report.
 2024.
 24
 What is GPT
AI? -generative pre-
 tr
ained transformers explained - AWS. Amazon Web
Services, Inc. Available: https://aws.amazon.com/what-is/gpt/ [Accessed 26 May
2024].
 25  Hello GPT -  4o . Available: https://openai.com/index/hello-gpt-4o/ [Accessed 26 May
2024].
 26
 What is zero-
 shot learning? | IBM.
 2024. Available: https://www.ibm.com/topics/zero-

shot-learning [Accessed 26 May 2025].
 27
 Y
ue X, Ni Y , Zhang K, et al. MMMU: a massive multi-
 discipline multimodal
understanding and reasoning benchmark for expert
AGI. 2023. Available: http://arxiv.

org/abs/2311.16502 [Accessed 26 May 2024].
 28
 GPT
-
 4:
 a complete guide to understanding its functionalities. plain concepts. 2024.
Available: https://www.plainconcepts.com/gpt-4-guide/ [Accessed 26 May 2024].
 29
 Meltw
ater: media, social & consumer intelligence. Meltwater. Available: https://www.

meltw
ater.com/en [Accessed 16 May 2024].
 30
 K
ong G, Ouellette RR, Murthy D. Generative artificial intelligence and social media:
insights for tobacco control. Tob Control 2024;6:2024.
Protected by copyright, including for uses related to text and data mining, AI training, and similar technologies.
. Marburg
at Universitatsbibliothek on November 8, 2026 http://tobaccocontrol.bmj.com/Downloaded from 30 January 2025. 10.1136/tc-2024-058887 on Tob Control: first published as
