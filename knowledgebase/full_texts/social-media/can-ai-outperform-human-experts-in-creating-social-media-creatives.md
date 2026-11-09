---
title: Can AI Outperform Human Experts in Creating Social Media Creatives?
url: https://arxiv.org/abs/2404.00018
category: social-media
subcategory: empirical
date: 2024-03
venue: ''
authors:
- Eunkyung Park
- Raymond K. Wong
- Junbum Kwon
source: arxiv
pdf_url: https://arxiv.org/pdf/2404.00018
pages: 17
chars: 57993
fetched_at: '2026-11-08T13:01:25+00:00'
kb_version: 1
---

# Can AI Outperform Human Experts in Creating Social Media Creatives?

Can AI Outperform Human Experts in Creating Social Media Creatives?
Eunkyung Park1 , Raymond K. Wong1 , Junbum Kwon1
1UNSW Sydney
{eunkyung.park, ray.wong,junbum.kwon}@unsw.edu.au
Abstract
Artificial Intelligence (AI) has outperformed hu-
man experts in functional tasks such as chess and
baduk. How about creative tasks? This paper
evaluates AI’s capability in the creative domain
compared to human experts, which little research
has been conducted so far. We propose a novel
Prompt-for-Prompt to generate social media cre-
atives via prompt augmentation by Large Language
Models (LLMs). We take the most popular In-
stagram posts (with the biggest number of like
clicks) in top brands’ Instagram accounts to cre-
ate social media creatives. We give GPT-4 several
prompt instructions with text descriptions to gen-
erate the most effective prompts for cutting-edge
text-to-image generators: Midjourney, DALL-E 3,
and Stable Diffusion. LLM-augmented prompts
can boost AI’s abilities by adding objectives, en-
gagement strategy, lighting and brand consistency
for social media image creation. We conduct an ex-
tensive human evaluation experiment, and find that
(1) AI excels human experts, and (2) Midjourney
is better than the other text-to-image generators.
Surprisingly, unlike conventional wisdom in the
social media industry, prompt instruction includ-
ing ‘eye-catching’ shows much poorer performance
than those including ‘natural’. Regarding the type
of creatives, AI improves creatives with animals or
products but less with real people. Also, AI im-
proves creatives with short text descriptions more
than with long text descriptions, because there is
more room for AI to augment prompts with shorter
descriptions.
1 Introduction
As generative AI products such as ChatGPT become popular,
people are growingly worried about whether AI will replace
humans across many sectors, including creative domains. For
example, Hollywood workers recently had a five-month strike
because they were concerned about losing their jobs due to
AI [Horton, 2018 ]. Creative agencies have also started re-
ducing the number of junior workers because AI can make
(a) Human-generated social media image from Apple Instagram
(b) Our Prompt-for-Prompt-generated social media creatives
Figure 1: Human-generated vs AI-generated social media creatives
from original text : “My goal was to make the viewer feel like the
cat was taking a selfie.”#ShotoniPhone by Rashid S.@rashid bin
a draft quickly [Miller and Cox, 2023 ]. However, while AI
has outperformed human experts in functional tasks such as
chess and baduk, it has rarely been documented whether AI
is indeed doing a better job than human experts in creative
tasks. Leading companies often hire top design experts to
make attractive social media creatives. This paper evaluates
AI’s capability in the creative domain compared to human ex-
perts.
arXiv:2404.00018v1  [cs.HC]  19 Mar 2024

Designing an automatic system of social media creatives
from textural descriptions, i.e., the text-to-image tasks, is
challenging. However, with the advance of deep learning, re-
searchers have shown a substantial improvement in the image
generation task. [Ramesh et al., 2021a; Yu et al., 2022a] em-
ploy large scale data for text-to-image task including DALL-
E [Ramesh et al. , 2021a ]. The Diffusion Model (DM) has
recently become the new state-of-the-art model in text-to-
image generation tasks such as Stable Diffusion[Podell et al.,
2023]. While the existing research in the text-to-image litera-
ture focuses on improving the ability to generate images from
“given” text input, we change the research direction by im-
proving the “quality” of text input via Large Language Mod-
els (LLMs).
The recent success of LLMs has led to growing interest and
prevalence in improving their capability to perform tasks via
prompting. Researchers have published their work regard-
ing AI’s power compared to human ability. Marked Personas
[Cheng et al. , 2023] compares LLMs’ outputs with human-
written works. A series of research on In-Context Learning
(ICL) such as [Chen et al., 2023] and CoT [Wei et al., 2022b]
also compare AI with humans. Most of the above research in
the LLM literature focuses on text output or reasoning tasks.
This paper makes the following contributions and new
findings. First, our research evaluates AI’s ability in Cre-
ative tasks compared to human experts and shows that AI-
generated creatives receive higher engagement (i.e., willing-
ness to like and comment) than creatives of human experts.
Our result can give more confidence to companies in creative
industries about adopting generative AI. Second, more im-
portantly, we propose a novel Prompt-for-Prompt approach
to generating social media creatives via prompt augmenta-
tion by leveraging the power of LLMs. Specifically, we take
the most popular Instagram posts (with the biggest number of
like clicks) in top brands’ Instagram accounts. Then, we give
GPT-4 several prompt instructions with its text description
of such top posts to generate the most effective prompts for
cutting-edge text-to-image generators: Midjourney, DALL-E,
and Stable Diffusion.
For example, Figure 1 shows a social media post from Ap-
ple Instagram. Figure 1a is the most popular post (made by
human experts) with the biggest number of likes within top
brands’ Instagram accounts.
Figure 1b is an AI-generated image via our prompt aug-
mentation using the original text description. From the exper-
iments, we find that our Prompt-for-Prompt can boost AI’s
abilities by adding creatives’ objectives, engagement strategy,
lighting and brand consistency for social media image cre-
ation. Our proposed approach is efficient regarding computa-
tion time and cost, and can be adapted to many other appli-
cations easily beyond social media image generation. Also,
our results show that a Midjourney is better than the other
text-to-image generators.
Third, we identify effective Prompt-for-Prompt to gener-
ate social media creatives. Surprisingly, unlike conventional
wisdom in the social media industry, prompt instructions in-
cluding ‘eye-catching’ show much poorer performance than
that including ‘natural’. Fourth, we also identify the type of
content on which AI (vs human experts) is better or worse.
Prompt instruction Output
P I1 Natural+Social Media Images+ P 0 Pa1
P I2 Eye-Catching+Social Media Images+ P 0 Pa2
P I3 Social Media Images + P 0 Pa3
Table 1: Examples of prompt instruction. P 0 is an original text
description
AI improves creatives with animals or products rather than
with real people. Also, AI improves creatives with short text
descriptions more than with long text descriptions perhaps
because there is more room for AI to augment prompts with
short descriptions.
2 Related Work
2.1 Large Language Models (LLMs)
As LLMs receive great attention from academics and indus-
tries, many researchers have tried to uncover the real effects
of LLMs outputs [Dinan et al., 2020; Weidinger et al., 2021].
They compare AI-generated outputs to the human-generated
outputs. For example, Marked Personas [Cheng et al., 2023]
compares GPT-3.5 and GPT-4 outputs with human-written
texts.
In addition, the recent success of Large Language Models
has led to growing interest in improving their capability to
perform tasks via prompting [Brown et al., 2020; Liu et al.,
2023]. Some researchers suggested significantly improving
LLMs’ capability by augmenting the task instructions[Raffel
et al., 2020; Wei et al., 2022a]. Other lines of research work
such as zero-shot CoT [Kojima et al. , 2022], auto-CoT [?],
and Tree of Thoughts (ToT) [Yao et al., 2023] have adapted
intermediate language steps since the publication of Chain-
of-Thoughts (CoT) [Wei et al., 2022b], which augments each
demo with a chain of rational steps. [Chen et al., 2023] have
studied a demo of In-Context Learning.
Similar to the above studies, our research also uses prompt-
ing. However, most of the previous work mainly covers tex-
tual data-based tasks. In this paper, we particularly focus on
the AI’s creativity in text-to-image task.
2.2 Text-to-Image
Text-to-image is to generate a realistic image from natural
language descriptions. AlignDRAW [Mansimov et al., 2016]
is a pioneering work that generates images from natural lan-
guages but suffers from unrealistic results.[Reed et al., 2016]
is one of the first to tackle this with a conditional GAN.
From the previous work, multi-stage model [Zhang et al. ,
2016], attention mechanisms [Xu et al. , 2018 ], contrastive
methods [Zhou et al. , 2022; Zhang et al. , 2021 ] have been
adapted. [Ramesh et al. , 2021b; Ding et al. , 2021 ] em-
ploy sequence modeling approaches. [Esser et al. , 2021;
Yu et al. , 2022b ] introduce stronger image quantizers and
scaling up model parameters.
Recently [Nichol et al., 2022; Ramesh et al., 2022; Rom-
bach et al., 2022] apply Diffusion Models [Ho et al., 2020]
to improve generated image quality. [Saharia et al. , 2022;

Figure 2: Our Prompt-for-Prompt
Yu et al., 2022b] scale up text encoder models to achieve sig-
nificant gains in generating relevant images. DALL-E 3 [Shi
et al. , 2020 ] is a text-to-image model by OpenAI, released
in Oct 2023. DALL-E 3 is trained from the highly descrip-
tive generated image captions, while existing text-to-image
models have difficulty following detailed image descriptions.
It uses a bespoke image captioner to recaption the training
dataset.
Stable Diffusion XL [Podell et al. , 2023 ] is a latent dif-
fusion model for text-to-image synthesis. It applies a three
times larger UNet backbone than previous models and utilises
many more model parameters to have more attention blocks
and a larger cross-attention context. Midjourney V5.2 gener-
ates images from text description and released in June 2023.
This paper uses state-of-the-art models such as Midjour-
ney, DALL-E 3, and Stable Diffusion. However, we are not
attempting to improve the text-to-image generators by pay-
ing computing costs and increasing the parameters. Instead,
we propose a novel Prompt-for-Prompt to generate social
media creatives via prompt augmentation by LLM (GPT-4).
3 Approach : Prompt-for-Prompt
Figure 2 shows our overall framework Prompt-for-Prompt
for social media image creation. On the top, there is a so-
cial media image and text description. Let I0 be the human-
generated original image, and P 0 denotes the original text
description in the Instagram post. Therefore, P 0 is “apple
“My goal was to make the viewer feel like the cat was taking
a selfie” #ShotoniPhone by Rashid S. @rashid bin ”
3.1 Prompt Instruction
From the original text description P 0, we leverage LLM to
generate an augmented prompt. We use 3 prompt instructions
(P I1, P I2, P I3) in Table 1 and original text description (P 0)
together as an input for GPT-4. For instance, to make an aug-
mented prompt by the instruction - ‘eye-catching’ and ‘social
media images’ ( Pa2), we ask LLM with Prompt instruction
(P I2), “Can you create a prompt to make eye-catching social
media images for the following description:( P 0)?” by con-
catenating ‘eye-catching social media images’ andP 0. Then,
LLM creates the augmented prompt Pa2. Eye-catching con-
tent is preferred in social media creatives to increase engage-
ment [Wawrzuta et al. , 2021 ]. Also, we select ‘natural’ as
another instruction because we worry that AI-generated cre-
atives are not natural from our preliminary experiment.
3.2 Prompt Augmentation by LLM for Social
Media Creatives
From the text description augmentation using GPT-4, we ob-
tain augmented prompt Pa1 from the prompt instruction such
as Pa1,Pa2, Pa3. Table 2 shows the examples of augmented
prompts from GPT-4. It includes key strategies for success-
ful social media image creation, including objectives and En-
gagement Strategy (Pa1) to create a natural social media im-
age. It also includes Lighting (Natural light) to create nat-

Pa1 Pa2 Pa3
Objective: Produce an image that
encapsulates the charming and play-
ful moment as if a cat is taking a
selfie, capturing the creativity and
quality of iPhone photography. En-
gagement Strategy:Craft the caption
or image in a way that encourages
viewers to share their own pet self-
ies taken on an iPhone, possibly cre-
ating a user-generated content stream
that broadens the campaign’s reach.
Lighting:Natural light should be uti-
lized to give life to the cat’s fur and
eyes, enhancing the image’s overall
warmth and appeal. Props and Ac-
cessories:Include iPhone accessories
or props that are typically associated
with selfies, like a ring light or a prop
to stabilize the iPhone, which can add
to the storytelling aspect.
Brand Consistency :Keep the image
sleek and consistent with Apple’s
branding. The composition should be
minimalistic yet striking, with a fo-
cus on the clever setup that makes the
cat appear to take a selfie. Call to
Action: Incorporate a subtle call to
action, such as “Show us your best
selfie #ShotoniPhone” to encourage
user engagement and participation in
the campaign. Scene Setup :Position
an iPhone in a scene in such a way
that a cat appears to be looking into
the front camera or tapping the shutter
button. This could be done by placing
the iPhone against a backdrop where
a cat typically lounges, like a sunny
windowsill, a cozy corner with scatter
cushions, or an interesting outdoor lo-
cale.
Scene Concept :Set up a whimsical
yet plausible scenario where a cat
appears to be using an iPhone to
take a selfie. Consider staging the
iPhone in a position that could nat-
urally be operated by the cat, such
as propped against a pile of books
or resting on a soft surface within
the cat’s reach. Cat’s Interaction
with the iPhone:Pose the cat with one
paw extended toward the iPhone as
if pressing the shutter button. En-
sure the cat’s face is prominently re-
flected on the iPhone screen, captur-
ing a clear selfie expression. Back-
ground Setting :Choose a simple yet
visually appealing background that
doesn’t distract from the subject, such
as a brightly lit room with minimal
furniture or an outdoor setting with
natural light.
Table 2: Examples of augmented prompts from GPT-4 for social media creatives. Due to the page limitation, we present only part of each
augmented prompt.
ural social media images. Pa2 presents a strategy regarding
Brand Consistency and Call to Action. It also suggests the
Scene Setup concept to create eye-catching social media im-
ages. Pa3 represents a strategy for social media creatives by
introducing Cat’s interaction and background setting.
Compared to the original text description, which includes
only a description of images, augmented prompts suggest
critical strategies for social media creatives. Figure 1b is gen-
erated from our proposed Prompt-for-Prompt. It shows a
more detailed cat for taking a selfie by adding a frame of an
iPhone and a pose for taking pictures by herself. This im-
provement is possible due to the augmented prompts’ detailed
direction, which is not presented in the original text descrip-
tion (P 0).
We use state-of-the-art text-to-image models such as Mid-
journey, DALL-E 3, and Stable Diffusion to create social me-
dia creatives using the augmented prompts ( Pa1, Pa2, Pa3)
from the previous step. Let m be a text-to-image method.
m ∈ {Midjourney, DALL-E 3, Stable Diffusion}. Therefore,
we generate social media images ImiPaj .
3.3 Robustness Check and Evaluation Measures
For qualitative evaluation from human participants, we ask
them two questions - willingness to like and comment for ro-
bustness check. The usage of willingness to like and com-
ment on Instagram posts is inspired by recent research [Ri-
etveld et al. , 2020 ]. Commenting requires higher levels of
cognitive and behavioural effort than liking. Thus, writing
comments can be considered more ‘profound engagement’
than clicking the like button [Yoon et al. , 2018 ]. Our ex-
periments also find a lower willingness to comment than a
willingness to like.
In addition to the two measures, we add further measure-
ments such as Share, Appealing, Relevant to text description,
Creative, and Natural to assess social media creatives as im-
age quality and text-image alignment are the two main criteria
of text-to-image are [Zhang et al., 2023].
4 Experiments
4.1 Tasks and Datasets
We conduct experiments on 10 Instagram accounts such as
Apple, Google, Louis Vuitton, and Tesla from various in-
dustries: IT, Fashion, Car, Food & Beverage. The overall
statistics are listed in Table 3. We collect social media data
using the automatic data scraping platform, PhantomBuster
(https://phantombuster.com/). We select top-ranked posts for
each brand based on the number of likes. We use social media
creatives as human expert-generated creatives. We use text
descriptions from the post as input to generate social media
creatives with Prompt instruction and text-to-image methods.
We rely on a LLM (GPT-4) to generate prompts. For each
brand, we generate 10 tasks.
4.2 Text-to-Image Methods and LLM for Prompts
We use state-of-art text-to-image methods and a LLM.
• Midjourney V .5.2 generates images from text descrip-
tions. It is released in June 2023. It combines CLIP
(Contrast Language Image Pretraining) with a con-
stantly changing set of image generation methods. One
can use the Midjourney Bot on Discord.

Brand Industry # Likes # Followers Image type Desc len # Tasks
Apple IT 1193014 31.9M animal-only 118 10
Coca-Cola Food & Beverage 41453 3M product-only 127 10
Google IT 92156 14.6M product-only 159 10
Herm´es Luxury 126411 13.5M people+product 250 10
Louis Vuitton Luxury 8354713 54.8M people+product 328 10
Mercedes-Benz Car 1275283 37.9M people+product 165 10
Nike Fashion 2069991 306M people+product 27 10
Rolex Luxury 402222 15.4M product-only 511 10
Starbucks Food & Beverage 618791 18M product-only 206 10
Tesla Car 1041648 9.4M product-only 72 10
Table 3: Statistics of datasets. We collect data from Instagram.
• DALL-E 3 is a text-to-image model by OpenAI and re-
leased in October 2023. To overcome limitations from
the training of noisy and inaccurate image captions, it
trains a bespoke image captioner to recaption the train-
ing dataset.
• Stable Diffusion SDXL is a latent diffusion model for
text-to-image and is released in 2023. It uses more at-
tention blocks and a larger cross-attention context. It in-
troduces a refinement model and post-hoc text-to-image
technique.
To generate prompts for social media creatives, we se-
lect GPT-4. From our preliminary experiments, Meta’s
Llama 2 (https://www.llama2.ai/) gives us outputs, includ-
ing multiple images with short prompts. The outputs from
Google’s BARD (https://bard.google.com) are similar to
GPT-4. Therefore, we conduct further experiments using only
GPT-4 to simplify the experiment.
4.3 Human Evaluation
We conduct human surveys using Amazon Mechanical Turk
(https://www.mturk.com). To minimise bias from the order-
ing effect, we randomise the order of the questionnaire us-
ing an online survey tool, Qualtrics (https://www.qualtrics.
com/). We have 100 sets of questionnaires and collect 500
human participants. Human participants are given 10 so-
cial media posts, including human-generated creative ( I0)
+ text description ( P 0) or AI-generated creative + text
description(P 0). Participants are asked questions, including
willingness to like and comment. We collect all responses
from the survey and calculate the mean values. We model
regression models for each question to assess the relation-
ship between our prompt approach to generate social media
creatives and target variables (willingness to like/comment),
including statistical significance.
5 Can AI Outperform Human Experts in
Creating Social Media Creatives?
To more precisely quantify whether AI-generated creatives
from augmented prompts ( Pa) obtain higher willingness to
like/comment, we model the outcome variables received by
Instagram’s ranked post as a function of Pa where the Pa is
computed at the aggregate level by combining all types of
augmented Prompts. In other words, Pa=1 if the image is
generated from Prompt-for-Prompt or 0 otherwise.
β1 measures the difference between human-generated (I0)
and AI-generated creatives from Prompt-for-Prompt (Pa1
or Pa2 or Pa3).
The regression model also includes several control vari-
ables, such as brand, age, gender, and duration to control
other effects:
Like or Comment=β0 + β1Pa + β2M ale
+β3Age + β4Duration
+µi + τj + ϵ (1)
where :
• β1 is a core coefficient of interest in this study, which is
the main effect of Prompt-for-Prompt (vs human);
• β0 is a constant term;
• β2, β3, β4 capture the effect of male (vs female), Age,
and Duration;
• Pa is 1 if the image is generated byPrompt-for-Prompt
or 0 otherwise;
• Male is 1 if the respondent is male or 0 otherwise;
• Age is an age of a participant;
• Duration is a time for completing human survey;
• µi is dummies for each brand (e.g., Apple, Coca-Cola);
• τj is dummies for the participants;
• ϵ is an error term.
Table 4 shows that people like AI-generated social me-
dia creatives more than human expert-generated ones. The
key coefficients of interest ( Pa) for both like and comment
are positive and significant, respectively. On average, people
like creatives from our proposed approach 2.48 (out of 10)
more than those from human experts. The model’s small p-
values show the statistically significant differences between
the baseline (human expert-generated creatives) and the AI-
generated creatives. Similarly, regarding comments, our pro-
posed augmented prompt approach (Pa) achieves a 2.17 (out

Response Variable Coef p-value
Like Pa 2.48 0.002 ***
Male -2.38 1.65e-14 ****
Age 0.34 0.076 *
Duration 0.01 6.73e-05 ****
Adjusted R-squared: 0.676
Comment Pa 2.17 0.012 **
Male -2.99 0.009 ***
Age 0.29 0.172
Duration 0.01 0.007 ***
Adjusted R-squared: 0.673
*p < 0.1; **p < 0.05; ***p < 0.01; ****p < 0.001.
Table 4: Regression result of Model 1
Response Variable Coef p-value
Like Pa1 2.49 0.005 ***
Pa2 1.85 0.037 **
Pa3 2.58 0.003 ***
Male -2.34 2.96e-16 ****
Age 0.37 0.038 **
Duration 0.01 8.79e-06 ****
Adjusted R-squared: 0.665
Comment Pa1 1.632 0.090 *
Pa2 1.856 0.054 *
Pa3 2.634 0.006 ***
Male -3.11 -10.127 < 2e-16 ****
Age 0.34 0.072 *
Duration 0.01 0.002 ***
Adjusted R-squared: 0.678
*p < 0.1; **p < 0.05; ***p < 0.01; ****p < 0.001.
Table 5: Regression result from each augmented prompt
of 10) more willingness to comment compared to the base-
line (human-generated creatives), and the difference is statis-
tically significant. Also, across willingness to like and com-
ment, female (vs male) and older participants give higher
willingness to like or comment.
6 Ablation Study
To examine whether each augmented prompt can generate
better social media creatives than the creatives by human
experts, we model the willingness to like and comment on
which Instagram top-ranked posts received as a function of
Pa1, Pa2, and Pa3, which are dummy variables. For exam-
ple, Pa1=1 when the image is generated from the augmented
prompt Pa1 or 0 otherwise. The function includes several
control variables like the previous regression model. (Refer
to the model in Appendix A.1).
Table 5 shows that all the coefficients of Pa1, Pa2, and
Pa3 are positive and significant, suggesting that people are
more willing to like/comment creatives from our Prompt-
for-Prompt methods than the human-generated creatives.
Also, a small p-value means that the differences are statis-
tically significant. Specifically, regarding likes prompts Pa3
Response Variable Coef p-value
Like Mid+ Pa1 3.02 0.006 ***
Mid+Pa2 0.97 0.374
Mid+ Pa3 3.57 0.001 ***
DALL+Pa1 2.81 0.010 **
DALL+Pa2 2.37 0.030 **
DALL+ Pa3 2.55 0.019 **
SD+Pa1 1.66 0.127
SD+Pa2 2.24 0.040 **
SD+ Pa3 1.63 0.135
Male -2.34 2.96e-16 ****
Age 0.37 0.038 **
Duration 0.01 8.79e-06 ****
Adjusted R-squared: 0.665
Comment Mid+ Pa1 1.46 0.218
Mid+Pa2 2.57 0.029 **
Mid+ Pa3 3.29 0.005 ***
DALL+Pa1 1.31 0.267
DALL+Pa2 0.67 0.570
DALL+ Pa3 2.66 0.025 **
SD+Pa1 2.13 0.071429 *
SD+Pa2 2.33 0.049 **
SD+ Pa3 1.96 0.098 *
Male -3.11 -10.121 < 2e-16 ****
Age 0.34 0.072 *
Duration 0.01 0.002 ***
Adjusted R-squared: 0.671
*p < 0.1; **p < 0.05; ***p < 0.01; ****p < 0.001.
Table 6: Regression result for text-to-image methods+augmented
prompts with human-generated creatives baseline
Like Comment
Prompt Mid DALL SD Mid DALL SD
Pa1 7.14 6.93 5.78 3.99 3.85 4.67
Pa2 5.09 6.49 6.36 5.11 3.21 4.87
Pa3 7.69 6.66 5.75 5.83 5.20 4.50
Note: Mid-Midjourney, DALL-DALL-E 3, SD-Stable Diffusion
Table 7: Text-to-Image methods comparison
(social media image prompts), Pa1 (Natural social media im-
age prompts), Pa2 (eye-catching prompts) show 2.58, 2.49,
1.85 compared to baseline (human-generated creatives), re-
spectively. The differences between the baseline and itself
are statistically significant. In addition, regarding the com-
ment, all 3 prompt methods achieve higher willingness than
the human-generated creatives. The differences are statisti-
cally significant for Pa3 and marginally significant (i.e. p-
value is between 0.05 and 0.1) for Pa1 and Pa2.
Table 6 presents the effects of prompts and text-to-image
methods. Midjourney and Pa3 create the best willingness
to like and comment compared to the baseline (human-
generated) and the difference is statistically significant (Refer
to the model in Appendix A.2).

Like Comment Share Appealing Relevant Creative Natural
Product-only Human 5.33 1.06 3.74 7.54 7.47 7.47 7.50 Prompt-AI 6.33 3.36 4.09 7.59 7.44 7.47 7.57
People+product Human 7.54 4.65 6.82 7.56 7.26 7.53 7.53 Prompt-AI 7.16 5.16 6.52 7.62 7.36 7.51 7.50
Animal-only Human 7.09 4.36 5.88 7.64 7.53 7.36 7.40 Prompt-AI 8.05 6.04 6.36 7.85 7.55 7.64 7.62
Table 8: Human vs AI based on image characteristics
Like Comment Share Appealing Relevant Creative Natural
Short Human 4.65 1.87 4.48 7.65 7.45 7.51 7.65 Prompt-AI 5.89 4.01 4.49 7.72 7.49 7.53 7.62
Medium Human 7.65 3.91 5.75 7.48 7.47 7.50 7.37 Prompt-AI 7.99 5.56 6.05 7.63 7.43 7.53 7.47
Long Human 7.45 3.01 5.55 7.52 7.24 7.43 7.44 Prompt-AI 6.92 3.57 5.59 7.57 7.30 7.44 7.52
Table 9: Prompt-for-Prompt effects based on text description length
7 Deeper Analysis
Table 7 shows that for both the Like and Comment measure,
Midjourney achieves the highest scores. For like, Midjourney
records the best score from the 2 measures among 3, and the
average score across all measures is 7.01, 7.79% higher than
DALL-E 3 and 17.80% higher than Stable Diffusion. For the
Comment, Midjourney shows the best score in all the 3 mea-
sures.
Our proposed Prompt-for-Prompt approach can more
effectively increase social media creatives for Animal and
product-only. However, they need more improvement for the
creatives, including real people (Table 8). In detail, in animal-
only creatives, AI presents improvement for 7 measures and
improvement for product-only creatives from 6 measures.
However, prompts fail to improve the image quality for peo-
ple creatives. Prompt shows improvement only 3 measures
out of 7. Figure 1 presents an example of an animal-only im-
age. Figure 3 is a people+product image, and Figure 4 is a
product-only image.
We categorize our datasets into 3 groups (short, medium,
and long) based on the length of the text description (Table 3).
On average, prompts improve 20.39% for short text descrip-
tions compared to human-generated social media creatives
while they boost 7.90% from the medium length and 2.14%
for long text descriptions. This means that a short text de-
scription is not enough to generate high quality social media
creatives, and text augmentation using Prompt-for-Prompt
can improve the AI’s capabilities to generate social media
creatives.
8 Conclusion
Prompt augmentation via LLMs is essential for generating
creatives, even in the creative domain. However, recent re-
search mainly covers textual data and reasoning tasks. This
paper examines the effect of prompts for generating social
media creatives from real Instagram data.
Figure 3: AI-generated creative - people+product
Figure 4: AI-generated creative - product-only

References
[Brown et al., 2020] Tom Brown, Benjamin Mann, Nick Ry-
der, Melanie Subbiah, Jared D Kaplan, Prafulla Dhari-
wal, Arvind Neelakantan, Pranav Shyam, Girish Sastry,
Amanda Askell, Sandhini Agarwal, Ariel Herbert-V oss,
Gretchen Krueger, Tom Henighan, Rewon Child, Aditya
Ramesh, Daniel Ziegler, Jeffrey Wu, Clemens Winter,
Chris Hesse, Mark Chen, Eric Sigler, Mateusz Litwin,
Scott Gray, Benjamin Chess, Jack Clark, Christopher
Berner, Sam McCandlish, Alec Radford, Ilya Sutskever,
and Dario Amodei. Language models are few-shot learn-
ers. In Neural Information Processing Systems, volume 33,
pages 1877–1901, 2020.
[Chen et al., 2023] Jiuhai Chen, Lichang Chen, Chen Zhu,
and Tianyi Zhou. How many demonstrations do you need
for in-context learning? In Empirical Methods in Natural
Language Processing, pages 11149–11159, 2023.
[Cheng et al., 2023] Myra Cheng, Esin Durmus, and Dan Ju-
rafsky. Marked personas: Using natural language prompts
to measure stereotypes in language models. InAssociation
for Computational Linguistics, pages 1504–1532, 2023.
[Dinan et al., 2020] Emily Dinan, Angela Fan, Ledell Wu,
Jason Weston, Douwe Kiela, and Adina Williams. Multi-
dimensional gender bias classification. In Empirical Meth-
ods in Natural Language Processing , pages 314–331,
November 2020.
[Ding et al., 2021] Ming Ding, Zhuoyi Yang, Wenyi Hong,
Wendi Zheng, Chang Zhou, Da Yin, Junyang Lin, Xu Zou,
Zhou Shao, Hongxia Yang, and Jie Tang. Cogview: Mas-
tering text-to-image generation via transformers. In Neu-
ral Information Processing Systems , pages 19822–19835,
2021.
[Esser et al., 2021] Patrick Esser, Robin Rombach, and
Bj¨orn Ommer. Taming transformers for high-resolution
image synthesis. In Computer Vision and Pattern Recog-
nition, pages 12873–12883, 2021.
[Ho et al., 2020] Jonathan Ho, Ajay Jain, and Pieter Abbeel.
Denoising diffusion probabilistic models. In in Neural In-
formation Processing Systems, 2020.
[Horton, 2018] Adrian Horton. Embrace it or risk obsoles-
cence: How will ai jobs affect hollywood? The Guardian,
2018. Available at: https://www.theguardian.com/film/
2023/aug/21/ai-jobs-hollywood-writers-actors-strike
(Accessed: Jan 13th, 2023).
[Kojima et al., 2022] Takeshi Kojima, Shixiang (Shane) Gu,
Machel Reid, Yutaka Matsuo, and Yusuke Iwasawa. Large
language models are zero-shot reasoners. In Neural In-
formation Processing Systems , volume 35, pages 22199–
22213, 2022.
[Liu et al., 2023] Pengfei Liu, Weizhe Yuan, Jinlan Fu,
Zhengbao Jiang, Hiroaki Hayashi, and Graham Neubig.
Pre-train, prompt, and predict: A systematic survey of
prompting methods in natural language processing. ACM
Computing Surveys, 55(9), 2023.
[Mansimov et al., 2016] Elman Mansimov, Emilio Parisotto,
Lei Jimmy Ba, and Ruslan Salakhutdinov. Generating im-
ages from captions with attention. In Yoshua Bengio and
Yann LeCun, editors, International Conference on Learn-
ing Representations, 2016.
[Miller and Cox, 2023] Claire Cain Miller and Courtney
Cox. In reversal because of a.i., office jobs are
now more at risk. The Guardian , 2023. Avail-
able at: https://www.theguardian.com/film/2023/aug/21/
ai-jobs-hollywood-writers-actors-strike (Accessed: Jan
13th, 2023).
[Nichol et al., 2022] Alexander Quinn Nichol, Prafulla
Dhariwal, Aditya Ramesh, Pranav Shyam, Pamela
Mishkin, Bob McGrew, Ilya Sutskever, and Mark Chen.
GLIDE: towards photorealistic image generation and edit-
ing with text-guided diffusion models. In International
Conference on Machine Learning , volume 162, pages
16784–16804, 2022.
[Podell et al., 2023] Dustin Podell, Zion English, Kyle
Lacey, Andreas Blattmann, Tim Dockhorn, Jonas M ¨uller,
Joe Penna, and Robin Rombach. SDXL: improving la-
tent diffusion models for high-resolution image synthesis.
CoRR, abs/2307.01952, 2023.
[Raffel et al., 2020] Colin Raffel, Noam Shazeer, Adam
Roberts, Katherine Lee, Sharan Narang, Michael Matena,
Yanqi Zhou, Wei Li, and Peter J. Liu. Exploring the limits
of transfer learning with a unified text-to-text transformer.
Journal of Machine Learning Research, 21, 2020.
[Ramesh et al., 2021a] Aditya Ramesh, Mikhail Pavlov,
Gabriel Goh, Scott Gray, Chelsea V oss, Alec Radford,
Mark Chen, and Ilya Sutskever. Zero-shot text-to-image
generation. In International Conference on Machine
Learning, pages 8821–8831, 2021.
[Ramesh et al., 2021b] Aditya Ramesh, Mikhail Pavlov,
Gabriel Goh, Scott Gray, Chelsea V oss, Alec Radford,
Mark Chen, and Ilya Sutskever. Zero-shot text-to-image
generation. In International Conference on Machine
Learning, volume 139, pages 8821–8831, 2021.
[Ramesh et al., 2022] Aditya Ramesh, Prafulla Dhariwal,
Alex Nichol, Casey Chu, and Mark Chen. Hierarchi-
cal text-conditional image generation with CLIP latents.
CoRR, abs/2204.06125, 2022.
[Reed et al., 2016] Scott Reed, Zeynep Akata, Xinchen Yan,
Lajanugen Logeswaran, Bernt Schiele, and Honglak Lee.
Generative adversarial text to image synthesis. In Interna-
tional Conference on Machine Learning, volume 48, pages
1060–1069, 2016.
[Rietveld et al., 2020] Robert Rietveld, Willemijn Van
Dolen, Masoud Mazloom, and Marcel Worring. What
you feel, is what you like influence of message appeals on
customer engagement on instagram. Journal of Interactive
Marketing, 49(1):20–53, 2020.
[Rombach et al., 2022] Robin Rombach, Andreas
Blattmann, Dominik Lorenz, Patrick Esser, and Bj ¨orn
Ommer. High-resolution image synthesis with latent

diffusion models. In Computer Vision and Pattern
Recognition, pages 10674–10685, 2022.
[Saharia et al., 2022] Chitwan Saharia, William Chan,
Saurabh Saxena, Lala Li, Jay Whang, Emily L. Denton,
Seyed Kamyar Seyed Ghasemipour, Raphael Gontijo
Lopes, Burcu Karagol Ayan, Tim Salimans, Jonathan Ho,
David J. Fleet, and Mohammad Norouzi. Photorealistic
text-to-image diffusion models with deep language un-
derstanding. In Neural Information Processing Systems ,
2022.
[Shi et al., 2020] Zhan Shi, Xu Zhou, Xipeng Qiu, and Xi-
aodan Zhu. Improving image captioning with better use
of caption. In Association for Computational Linguistics ,
pages 7454–7464, 2020.
[Wawrzuta et al., 2021] Dominik Wawrzuta, Mariusz Ja-
worski, Joanna Gotlib, and Mariusz Panczyk. Characteris-
tics of antivaccine messages on social media: Systematic
review. Journal of Medical Internet Research, 23, 2021.
[Wei et al., 2022a] Jason Wei, Yi Tay, Rishi Bommasani,
Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yo-
gatama, Maarten Bosma, Denny Zhou, Donald Metzler,
Ed H. Chi, Tatsunori Hashimoto, Oriol Vinyals, Percy
Liang, Jeff Dean, and William Fedus. Emergent abilities of
large language models. Transactions on Machine Learn-
ing Research, 2022.
[Wei et al., 2022b] Jason Wei, Xuezhi Wang, Dale Schuur-
mans, Maarten Bosma, brian ichter, Fei Xia, Ed Chi,
Quoc V Le, and Denny Zhou. Chain-of-thought prompting
elicits reasoning in large language models. In Neural In-
formation Processing Systems , volume 35, pages 24824–
24837, 2022.
[Weidinger et al., 2021] Laura Weidinger, John Mellor,
Maribeth Rauh, Conor Griffin, Jonathan Uesato, Po-Sen
Huang, Myra Cheng, Mia Glaese, Borja Balle, Atoosa
Kasirzadeh, Zac Kenton, Sasha Brown, Will Hawkins,
Tom Stepleton, Courtney Biles, Abeba Birhane, Julia
Haas, Laura Rimell, Lisa Anne Hendricks, William Isaac,
Sean Legassick, Geoffrey Irving, and Iason Gabriel. Ethi-
cal and social risks of harm from language models. CoRR,
abs/2112.04359, 2021.
[Xu et al., 2018] Tao Xu, Pengchuan Zhang, Qiuyuan
Huang, Han Zhang, Zhe Gan, Xiaolei Huang, and Xi-
aodong He. Attngan: Fine-grained text to image gener-
ation with attentional generative adversarial networks. In
Computer Vision and Pattern Recognition, , pages 1316–
1324, 2018.
[Yao et al., 2023] Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak
Shafran, Thomas L. Griffiths, Yuan Cao, and Karthik R
Narasimhan. Tree of thoughts: Deliberate problem solv-
ing with large language models. In Neural Information
Processing Systems, 2023.
[Yoon et al., 2018] Gunwoo Yoon, Cong Li, Yi (Grace) Ji,
Michael North, Cheng Hong, and Jiangmeng Liu. At-
tracting comments: Digital engagement metrics on face-
book and financial performance. Journal of Advertising ,
47(1):24–37, 2018.
[Yu et al., 2022a] Jiahui Yu, Yuanzhong Xu, Jing Yu Koh,
Thang Luong, Gunjan Baid, Zirui Wang, Vijay Vasude-
van, Alexander Ku, Yinfei Yang, Burcu Karagol Ayan,
Ben Hutchinson, Wei Han, Zarana Parekh, Xin Li, Han
Zhang, Jason Baldridge, and Yonghui Wu. Scaling autore-
gressive models for content-rich text-to-image generation.
Transactions on Machine Learning Research, 2022.
[Yu et al., 2022b] Jiahui Yu, Yuanzhong Xu, Jing Yu Koh,
Thang Luong, Gunjan Baid, Zirui Wang, Vijay Vasude-
van, Alexander Ku, Yinfei Yang, Burcu Karagol Ayan,
Ben Hutchinson, Wei Han, Zarana Parekh, Xin Li, Han
Zhang, Jason Baldridge, and Yonghui Wu. Scaling autore-
gressive models for content-rich text-to-image generation.
Transactions on Machine Learning Research, 2022.
[Zhang et al., 2016] Han Zhang, Tao Xu, Hongsheng Li,
Shaoting Zhang, Xiaogang Wang, Xiaolei Huang, and
Dimitris N. Metaxas. Stackgan: Text to photo-realistic
image synthesis with stacked generative adversarial net-
works. International Conference on Computer Vision ,
pages 5908–5916, 2016.
[Zhang et al., 2021] Han Zhang, Jing Yu Koh, Jason
Baldridge, Honglak Lee, and Yinfei Yang. Cross-modal
contrastive learning for text-to-image generation. In Com-
puter Vision and Pattern Recognition , pages 833–842,
2021.
[Zhang et al., 2023] Chenshuang Zhang, Chaoning Zhang,
Mengchun Zhang, and In So Kweon. Text-to-image
diffusion models in generative AI: A survey. CoRR,
abs/2303.07909, 2023.
[Zhou et al., 2022] Yufan Zhou, Ruiyi Zhang, Changyou
Chen, Chunyuan Li, Chris Tensmeyer, Tong Yu, Jiuxi-
ang Gu, Jinhui Xu, and Tong Sun. Towards language-free
training for text-to-image generation. In Computer Vision
and Pattern Recognition, pages 17907–17917, 2022.

A Regression models
A.1 Augmented prompts effect
Model 1 is a function to show the synergy effects between
text-to-image methods and augmented prompts.
Like or Comment=β0 + β1Pa1 + β2Pa2
+β3Pa3 + β4M ale+ β5Age
+β6Duration + µi + τj + ϵ (1)
where :
• β1, β2, β3 are the key coefficients of interest of this pa-
per, which are the main effects ofPa1, Pa2, Pa3, respec-
tively (vs human-generated)
• β0 is an intercept;
• Pa1 is 1 if the creatives are generated by Pa1 - Natu-
ral+Social Media Image or 0 otherwise;
• Pa2 is 1 if the creatives are generated by Pa2 - Eye-
Catching+Social Media Image or 0 otherwise;
• Pa3 is 1 if the creatives are generated by Pa3 -Social
Media Image or 0 otherwise;
• Male is 1 if the respondent is male or 0 otherwise;
• Age is an age of a participant;
• Duration is a time for completing human survey;
• µi is dummies for each brand (e.g., Apple, Coca-Cola);
• τj is dummies for the participants;
• ϵ is an error term.
A.2 Effects of text-to-image methods and
augmented prompts
Model 2 is a function to show the effects text-to-image meth-
ods and augmented prompts.
Like or Comment=β0
+β1M idPa1 + β2M idPa2 + β3M idPa3
+β4DalPa1 + β5DalPa2 + β6DalPa3
+β7SdPa1 + β8SdPa2 + β9SdPa3
+β10M ale+ β11Age + β12Duration
+µi + τj + ϵ (2)
where :
• β1, β2, β3, β4, β5, β6, β7, β8, β9 are the key
coefficients of interest of this paper, which are the
main effects of M idPa1, M idPa2, M idPa3, DalPa1,
DalPa2, DalPa3, SdPa1, SdPa2, SdPa3, respectively
(vs human-generated)
• β0 is an intercept;
• M idPa1 is 1 if the creatives are generated by Midjour-
ney and Pa1 - Natural+Social Media Image and or 0 oth-
erwise;
• M idPa2 is 1 if the creatives are generated by Midjour-
ney and Pa2 - Eye-Catching+Social Media Image or 0
otherwise;
• M idPa3 is 1 if the creatives are generated by Midjour-
ney and Pa3 -Social Media Image or 0 otherwise;
• DalPa1 is 1 if the creatives are generated by DALL-E 3
and Pa1 - Natural+Social Media Image and or 0 other-
wise;
• DalPa2 is 1 if the creatives are generated by DALL-
E 3 and Pa2 - Eye-Catching+Social Media Image or 0
otherwise;
• DalPa3 is 1 if the creatives are generated by DALL-E 3
and Pa3 -Social Media Image or 0 otherwise;
• SdPa1 is 1 if the creatives are generated by Stable Dif-
fusion and Pa1 - Natural+Social Media Image and or 0
otherwise;
• SdPa2 is 1 if the creatives are generated by Stable Dif-
fusion and Pa2 - Eye-Catching+Social Media Image or
0 otherwise;
• SdPa3 is 1 if the creatives are generated by Stable Dif-
fusion and Pa3 -Social Media Image or 0 otherwise;
• Male is 1 if the respondent is male or 0 otherwise;
• Age is an age of a participant;
• Duration is a time for completing human survey;
• µi is dummies for each brand (e.g., Apple, Coca-Cola);
• τj is dummies for the participants;
• ϵ is an error term.
B Examples of augmented prompt
The full contents of augmented prompts are in Tables 1, 2,
and 3.
C Examples of AI-generated creatives from
the same prompt
Figure 1 illustrates a comparison of Prompt-for-Prompt out-
puts from the same augmented prompt (Table 4) using differ-
ent text-to-image methods.
D Augmented prompts from other LLMs
Table 5 is an augmented prompt from Llama 2 and Table 6 is
an augmented prompt from BARD.

Pa1
Objective: Design an image series that whimsically suggests a cat taking a selfie, showcasing the high-quality
capabilities of the iPhone camera as captured by Rashid S.
Scene Setup: Position an iPhone in a scene in such a way that a cat appears to be looking into the front camera
or tapping the shutter button. This could be done by placing the iPhone against a backdrop where a cat typically
lounges, like a sunny windowsill, a cozy corner with scatter cushions, or an interesting outdoor locale.
Cat Interaction: Feature a cat interacting with the iPhone, with one paw extended towards the camera as if in the
midst of taking a selfie. The cat should be the primary subject, with its personality and expression taking center
stage.
iPhone Display: The iPhone screen should be visible, potentially reflecting the cat’s face on the screen to enhance
the selfie effect. You can also show the camera app interface around the cat’s reflection for a more authentic selfie
look.
Vibrant and Playful Aesthetic : Use a bright and attractive color palette to catch the eye and evoke a playful
mood. The image should use the natural light to sparkle off the cat’s eyes and the iPhone screen, highlighting the
quality of the photo.
Intriguing Angles: Experiment with various angles and perspectives to find the most engaging shot — overhead,
from the side, or with the cat’s face coming into the foreground and the iPhone angled towards it.
Engagement Elements : Add a caption or graphic element that encourages viewers to interact, such as ”Guess
what I’m thinking?” above the cat’s selfie or a prompt for users to post their pet’s selfie shot on an iPhone.
Hashtag Integration: Ensure that the hashtag #ShotoniPhone is prominently featured in the image in a style that
complements Apple’s branding. The font should be modern and clean, matching the aesthetics of Apple’s design.
Photographer Tag: Include a tasteful shout-out to the original photographer, @rashid bin , using a lower-third
graphic or a discreet corner placement that doesn’t take away from the overall design.
Call to Action: Incorporate a subtle call to action, such as “Show us your best selfie #ShotoniPhone” to encourage
user engagement and participation in the campaign.
Brand Consistency : Keep the image sleek and consistent with Apple’s branding. The composition should be
minimalistic yet striking, with a focus on the clever setup that makes the cat appear to take a selfie.
This prompt is tailored to create a playful and engaging visual story that resonates with the audience, driving home
the campaign’s creative angle and the technical prowess of the iPhone’s camera.
Table 1: Example of augmented prompt (Natural+Social Media Images) from GPT-4

Pa1
Objective: Create an image that captures a cat in the act of taking a selfie, showcasing the iPhone’s camera quality
and the playful, creative scenario envisioned by Rashid S.
Scene Concept : Set up a whimsical yet plausible scenario where a cat appears to be using an iPhone to take
a selfie. Consider staging the iPhone in a position that could naturally be operated by the cat, such as propped
against a pile of books or resting on a soft surface within the cat’s reach.
Cat’s Interaction with the iPhone: Pose the cat with one paw extended toward the iPhone as if pressing the shutter
button. Ensure the cat’s face is prominently reflected on the iPhone screen, capturing a clear selfie expression.
Background Setting: Choose a simple yet visually appealing background that doesn’t distract from the subject,
such as a brightly lit room with minimal furniture or an outdoor setting with natural light.
Props and Accessories : Add a few playful props around the scene to enhance the storytelling element. These
could include items typically associated with selfies or personalization, like sunglasses, small hats, or toys to add
character to the scene.
Photography Techniques: Utilize a high depth of field to keep the iPhone and the cat in sharp focus while softly
blurring the background. Employ lighting that flatters the cat’s features and enhances the iPhone’s screen visibility.
Image Style and Composition : Maintain a balance between fun and sophistication in the image composition.
Align the iPhone’s branding with the creative concept to ensure the product is recognizable and the scenario is
believable.
Caption and Hashtag Integration : Design the image with space to include an engaging caption and the hashtag
#ShotoniPhone. Ensure that the caption complements the visual content and continues the story that the image
portrays.
Photographer Tag: Place @rashid bin ’s handle in the image subtly but legibly to attribute the original concept
and maintain connection with the campaign’s community.
Viewer Engagement: Encourage interaction by prompting viewers to share their interpretation of the concept or
post their pet’s selfies, leveraging the initial creative idea for wider campaign participation.
Final Touches: Apply final edits to enhance the image’s clarity, color balance, and overall impact, ensuring that
the image meets the high-quality standards associated with Apple’s brand.
This prompt is designed to inspire the creation of an image that not only fits the playful narrative but also empha-
sizes the camera capabilities of the iPhone, reflecting the innovative and user-friendly reputation of Apple products.
Table 2: Example of augmented prompts (Eye-catching+Social Media Images) from GPT-4

Pa1
Objective: Craft a series of images that creatively depict a cat taking a selfie, illustrating the unique and user-
centric capabilities of the iPhone’s camera as visualized by photographer Rashid S.
Scene Composition: Set up a scene where a cat is positioned with an iPhone in such a way that it appears to be
taking a selfie. This could involve the cat’s paw placed on the iPhone screen as if it’s pressing the shutter button or
the iPhone propped up against an object with the cat looking directly into the front-facing camera.
Cat’s Pose and Expression : Capture the cat’s personality and curiosity, with its eyes focused on the screen,
ensuring that the moment conveys intention, akin to a selfie pose. The cat could be in a playful state or a more
serene, relaxed posture that people associate with taking selfies.
iPhone Orientation and Visibility : The iPhone should be visible in the frame, showing the camera interface
around the cat’s reflection on the screen, adding to the selfie illusion. Make sure the iPhone model is identifiable
to showcase the latest technology by Apple.
Background and Setting : Use a cozy and homely background, or place the cat in an unexpected but photogenic
location to add an element of surprise and delight to the composition. The background should be aesthetic but not
distracting, complementing the subject.
Lighting: Utilize natural lighting to create a soft and flattering ambiance that enhances the cat’s features and the
iPhone’s design. The lighting should also highlight the clarity and color accuracy of the iPhone’s camera.
Interaction with the Camera : To emphasize the concept of the cat taking a selfie, arrange the scene to include a
mirror reflection or a clear view of the cat’s face in the camera’s selfie mode.
Photographer Credit : Incorporate a credit to the contributing photographer Rashid S. (@rashid bin ) with a
discreet watermark or text overlay, ensuring it blends with the overall design and maintains the focus on the image.
Hashtag Placement: Place the campaign hashtag #ShotoniPhone prominently in the image, using Apple’s clean
and contemporary typography for consistency with the campaign’s branding.
Viewer Engagement: Craft the image to encourage viewers to participate in the campaign, perhaps by adding a
thought bubble graphic emanating from the cat with a prompt like ”Your turn to selfie” or ”Can you beat my selfie
game?”
Final Touches: Ensure the final image looks polished and vibrant, with balanced saturation and contrast to make
the visual pop on social media feeds.
By following this prompt, the resulting images should engage the audience with their creativity and interactive
narrative, encouraging them to view the iPhone as a device that captures not just images, but unique stories and
moments.
This prompt targets the production of playful and engaging content, fitting for social media shares and resonating
with the creative and high-quality essence of the Apple brand.
Table 3: Example of augmented prompt (Social Media Images) from GPT-4

Pa1
Composition Focus: Create a central, striking image of Vinicius Junior (@vinijr) as the main subject, capturing
his intensity on the field. Consider a freeze-frame of a memorable play or a stylized portrait that showcases his
determination and spirit.
Nike Branding: Ensure that Vinicius is wearing Nike gear prominently displaying the Nike logo. Position the
logo naturally but in a way that catches the eye, such as on his shirt or shoes.
Color Scheme and Lighting : Use a bold and contrasting color scheme that matches the Nike brand palette, with
emphasis on stark lighting to highlight @vinijr’s features and Nike’s products. Incorporate a gradient or lighting
effect that spotlights the athlete, drawing attention to the message of support.
Support Message: Overlay the image with the supportive slogan ”We stand with @vinijr” in bold, clear typogra-
phy. The font style should resonate with Nike’s sleek and modern branding, and the placement should complement
the image without obstructing the view of Vinicius Junior.
Visual Effects: Add dynamic visual effects that echo Vinicius Junior’s agility and speed, such as motion blur lines
trailing behind a kicked ball or speed-induced ripple effects around him.
Background Elements : Consider a backdrop that reflects the sport—like a blurred stadium full of fans or an
abstract representation of a football pitch—to keep the focus on the athlete while still conveying the energy of the
game.
Call to Action: Include a subtle but persuasive call to action that invites engagement from the community, such as
”Show your support” or ”Stand with us” with a designated hashtag that encourages user participation.
Imagery Cohesion: Ensure that the image looks cohesive, with all elements from Vinicius Junior to Nike branding,
the supportive message, and the visual style working together to create an impactful impression.
Authenticity: Despite the stylization, maintain a sense of authenticity to resonate with viewers on a personal level,
reminding them of Vinicius Junior’s real struggles and achievements.
Visual Flow : Design the image so the viewers’ eyes are naturally drawn across the different elements, from
Vinicius Junior to the support message and Nike branding, ensuring all components are seen.
When applying this prompt, the generated image will serve to unite Nike’s audience in support of Vinicius Junior
while staying true to Nike’s core values and aesthetic guidelines. The result should be an engaging and supportive
message wrapped in Nike’s powerful brand imagery.
Table 4: Example of augmented prompt from GPT-4

Pa1
Prompt: Create a series of social media images that showcase the unique and playful perspective of a cat taking
selfies with an iPhone. The images should be natural, fun, and showcase the cat’s personality while highlighting
the features of the iPhone. The goal is to make the viewer feel like the cat is taking a selfie and to showcase the
iPhone as the perfect tool for capturing life’s moments.
Image 2:A close-up shot of the cat’s face as it looks directly at the camera, with the iPhone held at paw-level. The
cat should have a playful expression, as if it’s about to take a selfie. The background should be blurred, with the
cat’s fur and whiskers in sharp focus. Use the iPhone’s Portrait mode to create a shallow depth of field.
Image 2: A shot of the cat holding the iPhone and taking a selfie. The cat should be positioned at an angle, with
the iPhone screen facing the viewer. The cat’s paw should be visible as it taps the screen to take the photo. The
background should be a colorful and fun environment, such as a cat toy or scratching post.
Image 3: A shot of the cat capturing a moment with its owner. The cat and owner should be positioned in a playful
pose, such as the cat sitting on the owner’s lap or the owner holding the cat. The iPhone should be visible in the
shot, with the cat’s paw or face in the foreground. The background should be a cozy and intimate environment,
such as a living room or bedroom.
Image 4: A shot of the cat taking a photo of its food or water bowl. The cat should be positioned directly above
the bowl, with the iPhone held at paw-level. The background should be a clean and modern kitchen or dining
area. Use the iPhone’s macro feature to capture the details of the food or water.Image 5: A shot of the cat taking
a selfie with a fun filter or effect. The cat should be positioned directly in front of the camera, with the iPhone
screen facing the viewer. The cat’s paw should be visible as it taps the screen to apply the filter. The background
should be a plain color or a fun pattern, such as stripes or polka dots.Image 6: A shot of the cat capturing a moment
with its toys. The cat should be positioned in the center of the shot, with its toys scattered around it. The iPhone
should be visible in the shot, with the cat’s paw or face in the foreground. The background should be a colorful
and playful environment, such as a cat playground or toy box.Image 7: A shot of the cat taking a photo of its
favorite spot in the house. The cat should be positioned in its favorite spot, such as a windowsill or a cozy blanket.
The iPhone should be held at paw-level, with the cat’s face or paw in the foreground. The background should be
a warm and inviting environment, such as a sunny window or a cozy fireplace.Image Image 8: A shot of the cat
taking a selfie with its owner in the background. The cat should be positioned directly in front of the camera, with
the iPhone screen facing the viewer. The cat’s paw should be visible as it taps the screen to take the photo. The
owner should be visible in the background, with a playful or fun expression. The background should be a colorful
and fun environment, such as a park.
Table 5: Example of augmented prompt from Llama 2

Pa1
1. Capture the Selfie Spirit:
• Scene: A playful cat perched on its owner’s shoulder, head tilted at the camera, paw outstretched like it’s
holding the phone. Use a wide-angle shot to capture the playful interaction between cat and owner.
• Lighting: Natural light, outdoors or by a window, creating a warm and inviting atmosphere.
• Color Palette: Bright and engaging, emphasizing the cat’s fur and eyes, complemented by the owner’s cloth-
ing.
• Hashtag: #ShotoniPhone #Caturday #PawfectSelfie
2. Focus on the Details:
• Close-up shot: Zoom in on the cat’s face, emphasizing its expressive eyes and the way it interacts with the
camera lens. Capture the slight blur of movement as it bats at the phone.
• Macro focus: Highlight the texture of the cat’s fur, tiny whiskers, and delicate nose. Use soft lighting to create
a dreamlike quality.
• Hashtag: #MacroMagic #iPhonePortrait #SeeTheUnseen
3. Showcase the iPhone’s Capabilities:
• Play with depth of field: Blur the background to make the cat the main focus, highlighting its personality and
independent spirit.
• Capture action: Use burst mode to freeze the cat mid-leap or playful swipe at the phone, emphasizing its
energy and dynamism.
• Hashtag: #iPhoneAction #FastFocus #UnleashYourInnerMeow
4. Tell a Story:
• Show the behind-the-scenes: Capture the owner setting up the ”selfie,” adjusting the angle, and interacting
with the cat to get the perfect shot.
• Series of images: Create a mini-storyboard showing the cat’s journey from curiosity to capturing the perfect
pose.
• Hashtag: #StorytellingWithiPhone #CatsofInstagram #LifeThroughAniPhoneLens
Additional Tips:
• Use props that are relatable to cats, like toys, balls, or catnip, to add visual interest and encourage interaction.
• Incorporate natural elements like greenery or sunlight to create a vibrant and refreshing feel.
• Keep the editing minimal and natural, focusing on highlighting the cat’s personality and the iPhone’s pho-
tographic capabilities. By incorporating these prompts and tips, you can create natural and engaging social
media images for Apple that capture the spirit of Rashid’s original ”ShotoniPhone” photo and connect with a
wide audience of cat lovers and iPhone users.
Table 6: Example of augmented prompt from BARD

(a) AI-generated image by Midjourney
(b) AI-generated image - DALL-E 3
(c) AI-generated image - Stable Diffusion
Figure 1: Image comparison from the same prompt
