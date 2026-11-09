---
title: 'Designed to Spread: A Generative Approach to Enhance Information Diffusion'
url: https://arxiv.org/abs/2511.12516
category: social-media
subcategory: empirical
date: 2025-11
venue: ''
authors:
- Ziqing Qian
- Jiaying Lei
- Shengqi Dang
- Nan Cao
source: arxiv
pdf_url: https://arxiv.org/pdf/2511.12516
pages: 9
chars: 45872
fetched_at: '2026-11-08T13:12:10+00:00'
kb_version: 1
---

# Designed to Spread: A Generative Approach to Enhance Information Diffusion

Designed to Spread: A Generative Approach to Enhance Information Diffusion
Ziqing Qian*1,2, Jiaying Lei*1,3, Shengqi Dang1,2,3, Nan Cao1,2,3†
1Intelligent Big Data Visualization Lab, Tongji University, Shanghai, China
2Shanghai Research Institute for Intelligent Autonomous System, Tongji University, Shanghai, China
3Shanghai Innovation Institute, Shanghai, China
2411920@tongji.edu.cn, jiaying.lei@outlook.com, dangsq123@tongji.edu.cn, nan.cao@gmail.com
Abstract
Social media has fundamentally transformed how people ac-
cess information and form social connections, with content
expression playing a critical role in driving information dif-
fusion. While prior research has focused largely on network
structures and tipping point identification, it provides lim-
ited tools for automatically generating content tailored for
virality within a specific audience. To fill this gap, we pro-
pose the novel task ofDiffusion-Oriented Content Genera-
tion(DOCG) and introduce an information enhancement al-
gorithm for generating content optimized for diffusion. Our
method includes an influence indicator that enables content-
level diffusion assessment without requiring access to net-
work topology, and an information editor that employs rein-
forcement learning to explore interpretable editing strategies.
The editor leverages generative models to produce semanti-
cally faithful, audience-aware textual or visual content. Ex-
periments on real-world social media datasets and user study
demonstrate that our approach significantly improves diffu-
sion effectiveness while preserving the core semantics of the
original content.
Code— https://github.com/idvxlab/designed-to-spread
Introduction
Social media has reshaped how people communicate, ac-
cess information, and form connections. Platforms such as
X, Facebook, and TikTok have become powerful channels
for news dissemination, public discourse, and cultural influ-
ence. Information spreads via diffusion-like processes along
user networks, motivating extensive research on diffusion
mechanisms (Bakshy et al. 2012; Guille et al. 2013; Weng,
Menczer, and Ahn 2013).
Extensive research has examined information diffusion
in social networks, including modeling diffusion dynam-
ics (Granovetter 1978; Pastor-Satorras and Vespignani 2001;
Kempe, Kleinberg, and Tardos 2003), identifying influen-
tial seed users (Chen, Wang, and Yang 2009), and lim-
iting spread via edge removal (Tong et al. 2012). These
approaches typically depend on detailed network struc-
ture, which is often unavailable or incomplete in real-world
*These authors contributed equally.
†Corresponding author.
Copyright © 2026, Association for the Advancement of Artificial
Intelligence (www.aaai.org). All rights reserved.
settings. Meanwhile, how content is crafted also signifi-
cantly affects its diffusion, especially for specific audiences.
Yet, content-level optimization remains underexplored. This
highlights the need for automated methods to generate
audience-aware, diffusion-oriented content without relying
on explicit network information.
The rapid development of AIGC techniques offers
promising potential to fulfill the above needs. While these
methods excel at generating high-quality text and image
content (Chen et al. 2023; Podell et al. 2023), optimizing
content specifically for maximizing information diffusion
remains challenging due to three key issues: (1) diffusion
impact is difficult to measure at the content level, espe-
cially when network topology is unavailable or incomplete;
(2) preserving the original message’s intent while generat-
ing user-preferred representations is non-trivial, as misalign-
ment may cause misunderstanding or even unintentional
misinformation; and (3) designing a unified framework that
integrates diffusion feedback into multimodal content gen-
eration remains an open challenge.
To address the above challenges, we introduce the task
ofDiffusion-Oriented Content Generation(DOCG), which
aims to generate a semantically faithful variant (text or
image) of a given message on a specific topic, optimized
to maximize its diffusion impact among a target audience
group. We propose an information enhancement framework
with two key components: aninfluence indicatorand anin-
formation editor. The influence indicator estimates content-
level diffusion potential within the target audience. The
information editor formulates content generation as a re-
inforcement learning (RL) problem, guiding a generative
model to revise content through interpretable, modality-
specific editing actions (e.g., amplifying emotional tone).
The RL objective is to maximize predicted influence while
preserving the original message’s semantics. Our main con-
tributions are summarized as follows:
• We propose a new task,Diffusion-Oriented Content Gen-
eration(DOCG), which aims to generate audience-aware
content to maximize diffusion influence.
• We propose a reinforcement learning framework that re-
shapes input messages to enhance diffusion while pre-
serving their original intent. It leverages an influence in-
dicator to estimate content-level impact for target audi-
ences without relying on network topology, using this
arXiv:2511.12516v2  [cs.SI]  12 Mar 2026

feedback to guide iterative multimodal revisions.
• We demonstrate the versatility of our method across both
textual and visual modalities, achieving significant im-
provements on real-world social media dataset.
Related Work
In this section, we review related work in three areas most
relevant to our study: social media analysis, information dif-
fusion models, and content editing and generation.
Social Media Analysis
Social media analysis explores the complex interplay of fac-
tors that shape how information is created, interpreted, and
propagated online. Early studies primarily adopted descrip-
tive approaches to reveal observable trends (Cheng et al.
2014; De Francisci Morales, Monti, and Starnini 2021; Etta
et al. 2023; Flamino et al. 2023), drawing insights from three
main perspectives.
The first focuses on content virality. For example,
V osoughi et al. (V osoughi, Roy, and Aral 2018) found that
false information spreads more rapidly than truthful con-
tent on X, largely due to its novelty and emotional appeal.
The second examines user engagement behaviors, includ-
ing posting frequency (Benevenuto et al. 2009; Spasojevic
et al. 2015), reaction latency (Hodas and Lerman 2014),
and cross-platform activity (Xu et al. 2014; Iamnitchi et al.
2023; Alipour et al. 2024). Especially, Shahbaznezhad et
al. (Shahbaznezhad, Dolan, and Rashidirad 2021) further
demonstrated that content format and platform-specific al-
gorithms significantly affect user responsiveness, with emo-
tionally charged posts eliciting faster reactions. The third
investigates the structural properties of diffusion cascades.
Notarmuzi et al. (Notarmuzi et al. 2022) identified universal
propagation patterns in early retweet cascades, highlighting
the role of network topology and user influence in determin-
ing final reach and virality.
While these studies offer valuable insights into diffusion
dynamics, they remain largely observational and often over-
look the causal impact of content transformation on user be-
havior. This gap motivates our generative approach to en-
hancing information diffusion through content design.
Information Diffusion Model
Research on information diffusion models seeks to model
the content propagation through social networks. Early ap-
proaches were inspired by epidemiological processes, such
as the Independent Cascade (IC) and Linear Threshold (LT)
models; however, these models assume static networks and
fixed influence probabilities among different people (Gold-
enberg, Libai, and Muller 2001; Kempe, Kleinberg, and Tar-
dos 2003).
To overcome these simplifications, subsequent work has
incorporated temporal dynamics, deep learning, and evolv-
ing network structures. For example, NetRate (Gomez-
Rodriguez, Leskovec, and Krause 2012) applies survival
analysis to infer time-dependent transmission functions
from cascade data. Inf-V AE (Sankar et al. 2020) models la-
tent diffusion representations via variational autoencoders,
while DeepDiffuse (Islam et al. 2018) leverages deep neural
networks to predict both the participants and timing of in-
formation cascades. More recently, Meng et al. (Meng et al.
2025) propose a data-driven model that captures the dynam-
ics of social reinforcement and decay in online diffusion,
offering a concise formulation for large-scale spread.
Despite these advancements, existing models still exhibit
critical limitations: a strong reliance on explicit network
structures, sensitivity to seed selection, and a lack of con-
tent awareness in modeling (Jiang, Ren, and Ferrara 2023).
These challenges underscore the need for a content-based
diffusion influence indicator that functions independently of
network topology.
Content Editing and Generation
Content editing and generation synthesize new content
aligned with a target distribution or specific objectives such
as style transfer. Generation creates content from scratch,
while editing modifies existing references to achieve desired
transformations, preserving coherence and semantics.
Early work on content generation used variational au-
toencoders (V AEs) (Kingma, Welling et al. 2013) and gen-
erative adversarial networks (GANs) (Goodfellow et al.
2020) to learn latent representations for attribute-controlled
editing (Radford, Metz, and Chintala 2016; Dumoulin
et al. 2017). With large-scale pretrained models, generation
has become more fluent and controllable. Large language
models (LLMs) such as GPT-3 (Brown et al. 2020) and
T5 (Raffel et al. 2020) enable fine-grained text editing via
prompts. In vision, diffusion models including Stable Dif-
fusion (Rombach et al. 2022), SDXL (Podell et al. 2023),
and PixArt-α(Chen et al. 2023) support high-quality image
generation and editing. Multimodal systems such as BLIP-
Diffusion (Li, Li, and Hoi 2023) and MIGE (Tian et al.
2025) further unify the editing across modalities.
However, most methods focus on general-purpose gen-
eration. Although recent work explores engagement-driven
generation for social networks (Coppolillo et al. 2025),
audience-specific preferences remain overlooked. Leverag-
ing the adaptability of LLMs and diffusion models, we ex-
plore audience-aware content generation to better support
information diffusion.
Diffusion-Oriented Content Generation
In this paper, we introduce a new task,Diffusion-Oriented
Content Generation(DOCG), which aims to generate a se-
mantically faithful variant (text or image) of a given message
c, optimized to maximize its diffusion impact among a group
of target audiencesU. We also propose a novel modality-
free algorithm framework based on reinforcement learning
to accomplish this task. The core idea of our framework is
to evaluate the diffusion impact and select strategies to edit
the original message iteratively based on pretrained gener-
ative models such as GPT-4 (for text) or Pixart-α(Chen
et al. 2023) (for image). By repeating this evaluation–editing
loop, the framework progressively enhances the expected
diffusion impact, ultimately producing an optimized variant
tailored for the group of target audiences.

𝑐
𝑈
ℒ𝑈ሺ𝑐ሻ
𝑝௜௝ሺ𝑐ሻ 𝑎
Figure 1: Overview of our proposed information enhancement framework, consisting of two main components: the influence
indicator, and the information editor.
As shown in Figure 1, our framework accepts an initial
messagecand a group of target audiencesUas the inputs,
and comprises two components: (b.1) theinfluence indica-
torand (b.2) theinformation editor. The influence indicator
computes an overall influence scoreL U (c)to measure the
diffusion impact. The information editor treatsL U (c)as the
reward signal for a policy network that samples an editing
actiona. This action is executed by a generative agent (e.g.,
a large language or text-to-image model) to produce a re-
vised message. In the following sections, we describe the
modeling and implementation details of each component.
Influence Indicator
The influence indicator produces an influence score to quan-
tify the diffusion impact of the message contentcwithin the
group of target audiencesU. Formally, the influence score is
defined as:
LU (c) = max i
 1
|U|
X
uj ∈U
pij(c)

(1)
wherep ij(c)denotes the probability that useru j ∈Uwill
spread (e.g., retweet or reply to) contentcafter being ex-
posed to it from useru i ∈U. This formulation captures the
diffusion potential of the most influential initiator. In the fol-
lowing, we detail the pairwise diffusion estimator for com-
putingp ij(c), its training data, and its loss function.
Pairwise Diffusion Estimator.The pairwise diffusion esti-
mator is implemented as a neural network that predicts the
probabilityp ij(c). The model operates in three stages: fea-
ture extraction, projection, and interaction. First, we extract
the featuresf i,f j, andf(c)corresponding to usersu i,u j,
and contentc, respectively. User features are computed as
the average of features from previously created or shared
content, while content features are obtained using a pre-
trained CLIP encoder (Radford et al. 2021), which aligns the
text and image features in a shared space. To handle long-
text inputs, we adopt Long-CLIP (Zhang et al. 2024), a vari-
ant of CLIP designed to overcome token length limitations.
Then, all input features are projected into a latent space via
a shared Multilayer Perceptron (MLP), denoted asM 1. The
combined representationhis obtained by concatenating the
projected vectors:
h=M 1(fi)⊕M 1(fj)⊕M 1(f(c))(2)
where⊕denotes vector concatenation. Finally,his passed
through another MLP,M2, which captures nonlinear interac-
tions among the user and content features. A sigmoid func-
tionσ(·)is applied to obtain the final probability:
pij(c) =σ

M2(h)

(3)
Training Data. We construct the training data not rely on
explicit social network topology by assuming a fully con-
nected graph over the audiences of each content. We for-
mulate each training sample as a quadruple(u i, uj, c, yijc),
whereu i andu j are user pairs,cis the content, andy ijc ∈
{0,1}is the label showcasing the interaction behavior. For
a given contentc, letu o denote the original poster andU c
the set of users who interacted withu o (e.g., via retweet or
reply). A sample is labeled as positive (y ijc = 1) if either
(1)u i =u o andu j ∈U c, or (2) bothu i, uj ∈U c. All other
user pairs are labeled as negative (y ijc = 0), indicating no
observed interaction related tocbetweenu i andu j. To miti-
gate class imbalance, we perform negative sampling by ran-
domly dropping a subset of training samples withy ijc = 0,
ensuring that the number of negative samples approximately
matches the number of positive ones for each content.
Loss Function. To train the pairwise diffusion estimator,
we minimize a binary cross-entropy loss, defined as:
LCE = 1 M X i,j,c [yijc logp ij(c) + (1−y ijc) log (1−p ij(c))]
(4)
whereMis the total number of training instances,p ij(c)is
the output of the predicted diffusion estimator, andy ijc ∈
{0,1}is the groundtruth label. The first term penalizes the
model when it assigns a low probability to observed diffu-
sion events, encouraging high confidence in positive cases.
The second term penalizes false positives, pushing the model
to assign low scores when diffusion does not occur.
Information Editor
Figure 2 illustrates the algorithm workflow of the informa-
tion editor introduced in our framework. It rewrites the text
or image contentcto improve its diffusion impact. The con-
tentc, along with its CLIP featuresf(c), is treated as the
states. Based on the state, the policy networkπθ, parameter-
ized byθ, produces a conditional distributionπ θ(a|s)over
editing actions and samples an interpretableactionvectora.
This action is then passed to anagent(i.e., GPT-4 for text

Dimension Description
Social Currencywhether the text enhances the sharer’s profile (e.g., appearing good, intelligent, funny).
Triggers whether the text is strongly connected to real-life scenarios, promoting frequent recall.
Emotionwhether the text evokes high-arousal emotions (e.g., excitement, surprise, delight).
Public whether the text format is easily shareable and visible.
Practical Valuewhether the text offers concrete guidelines or useful information.
Text
Stories whether the text includes a narrative framework or memorable elements.
Colorfulnesswhether the image is rich in color and has visual impact.
Human Scene whether the image includes scenes with people to enhance emotional resonance.
Emotionwhether the image can evoke strong emotional responses (such as joy, shock, or being moved).
Professional whether the image has the quality of professional photography.
Brightnesswhether the image is bright and attention-grabbing.
Clarity whether the image is clear and its details are prominent.
Visual Balancewhether the visual elements in the image are evenly distributed.
Image
Focus of the Picture whether the image focuses on the subject, avoiding visual dispersion.
Table 1: Action space for text and image content generation.
𝑎
𝑓ሺ𝑐ሻ
Δℒ
ݏ
𝑐
𝜋𝜃
𝒞
ݎ
Figure 2: Our information editor for editing message content
c. The policy network generates editing actions to iteratively
revise the content, guided by the reward signal.
revision or GPT-4 combined with PixArt-αfor image gener-
ation), which produces the revised content representing the
next state. To train the policy network and guide the rewrit-
ing process toward maximizing diffusion impact, areward
is computed by combining two parts: (i) influence gain∆L,
quantifying the improvement of the influence score as esti-
mated by the influence indicator, and (ii) semantic similarity
C, measuring semantic consistency of the rewritten content
and the original message. We describe each of these algo-
rithm details in the rest of the section.
Action. We define an interpretable action vectora, where
each dimensiona i ∈[−1,1](as detailed in Table 1) cor-
responds to a specific content feature to be modified. The
value ofa i indicates the degree and direction of modifica-
tion:a i ≈+1enhances thei-th feature,a i ≈0leaves it
unchanged, anda i ≈ −1suppresses it. For text content, we
adopt the STEPPS framework (Pressgrove, McKeever, and
Jang 2018), which includes six dimensions—Social Cur-
rency,Triggers,Emotion,Public,Practical Value, andSto-
ries—each empirically linked to increased virality. For im-
age content, the action space comprises eight perceptual di-
mensions related to visual engagement, such asColorful-
ness,Brightness, andVisual Balance. These dimensions are
informed by Li and Xie (Li and Xie 2020), who identified
image characteristics (e.g., color variation, emotional ex-
pression, and photographic quality) as key drivers of user
engagement on social media.
Agent. The agent leverages prompt engineering to rewrite
content using large language models, such as GPT-4 in our
implementation (implementation details are available in the
Appendix). Briefly, we embed the editingactioninto the
prompt, guiding the model to perform controlled rewrit-
ing. For text content, we construct a dynamic prompt that
encodes the action vector values (ranging from−100%to
100%) across six STEPPS dimensions. Each dimension is
associated with a natural language instruction, annotated
with the action vector value. For image content, we adopt
a similar strategy to construct the text-to-image prompt,
guided by eight predefined visual dimensions. The result-
ing prompt is then input into the image generation model
(e.g., PixArt-αin our implementation), enabling controlled
manipulation of visual features that affect diffusion.
Reward. The reward quantifies the quality of a revision
by jointly considering diffusion improvement and semantic
fidelity. It is defined as:
r=
(√ ∆L · C∆L ≥0
−
p
−∆L ·(1− C) ∆L<0
(5)
where the influence gain∆Land the semantic similarityC
are defined as:
∆L=L U (c)− LU (cori)(6)
C= cos(f(c), f(cori))(7)
wherec ori is the original input message content,cosdenotes
the cosine similarity. This formulation rewards the edits that
boost diffusion while preserving semantic fidelity, and pe-
nalizes changes that are either semantically inconsistent or
reduce diffusion potential.
Policy Network. The policy network defines a conditional
distributionπ θ(a|s)over editing actionsa, given the current
states, represented by the content feature vectorf(c). To
generate a continuous action vectora∈[−1,1], we use a
reparameterization strategy:
a= tanh (µ θ(c) +σ θ(c)·ϵ)(8)

Dataset Seed Tweets Users All Tweets Time Period
Olympics 4,375 10,097 5,812,520 2024.8-2024.11
Movie 6,625 14,552 6,181,779 2022.4-2024.11
Table 2: Statistics of datasets.
Observed
 Permuted
0.0
0.5
1.0Diffusion Indicator U(c)
0.99
0.76
0.53
0.53
***
Olympics
Observed
 Permuted
0.99
0.79
0.46
0.45
***
Movie
Median Mean
Figure 3: Distribution of influence scores for messages on
observed(orange) andpermuted(blue) combinations. ***
denotes statistical significance atp <0.001.
whereϵ∼ N(0, I)is standard Gaussian noise that in-
troduces controlled stochasticity to encourage exploration.
The hyperbolic tangent functiontanh(·)bounds the out-
put within[−1,1], promoting numerical stability and inter-
pretability. The meanµθ(c)and standard deviationσ θ(c)are
predicted by a two-layer MLP applied tof(c), enabling the
policy to flexibly capture uncertainty in the action space.
The objective is to learn an optimal policy that maximizes
the expected reward:
π∗(a|s) = arg max
πθ
X
a
πθ(a|s)·Q(s, a)(9)
whereQ(s, a)is the expected reward for applying actionato
states, andπ θ is the policy parameterized byθ. We optimize
the policy network using the policy gradient method (Sutton
et al. 1999), which updates parameters to maximize the ex-
pected cumulative reward:
θ←θ+lr· 1 B
BX
i=1
TX
t=1
∇θ logπ θ(a(t) i |s(t) i )·J i,t (10)
whereiindexes the sample in the batch,a (t) i is the action
taken at stept,s (t) i is the state at stept,∇ θ is the gradient
with respect to policy parametersθ,Bis the batch size,γ
is the discount factor,lris the learning rate, andJ i,t is the
discounted return from stept, defined as:
Ji,t =
TX
k=t
γk−tri,k (11)
in whichr i,k is the reward at stepkcomputed by Eq. (5).
Evaluation
We conducted comprehensive experiments to evaluate the
effectiveness of our proposed framework. In this section, we
begin by describing the dataset details. We then separately
Dataset Precision Recall F1-score AUC
Olympics 0.8187 0.8122 0.8113 0.9042
Movie 0.8360 0.8286 0.8277 0.9186
Table 3: Performance of the pairwise diffusion estimator.
evaluate the influence indicator and the information editor.
Finally, we present results from a user study designed to as-
sess whether the generated content aligns with human pref-
erences in the real-world information diffusion scenarios.
Datasets
We constructed two X (Twitter) datasets focused on dis-
cussions about recent movies and the Paris 2024 Summer
Olympics (Table 2) using a three-step process. First, we col-
lected tweets containing topic-relevant keywords, referred to
asseed tweets. Second, for each seed tweet, we defined its
audience group as the original poster and users who directly
interacted with it via retweets or replies. Third, we merged
all audience groups to form a unified topic-specific audience
group, and collected their tweets within a defined time win-
dow to build the final dataset. In total, the datasets comprise
over 10,000 users and 11 million tweets.
Indicator Estimation
In this section, we present the implementation and exper-
imental setup of the influence indicator, followed by an
evaluation of its effectiveness from two perspectives: (1)
the predictive capacity of the pairwise diffusion estimator
pij(c), and (2) the ability of the influence scoreL U (c)to
capture variations in diffusion impact across different audi-
ence groups. We also provide qualitative examples of con-
tent with high and low influence scores to demonstrate the
practical utility of the proposed indicator.
Implementation & Settings. We trained the pairwise diffu-
sion estimator using the Adam optimizer with a learning rate
of1×10 −4. Input features were standardized by removing
the mean and scaling to unit variance along each dimension.
The dataset was split into training and test sets in a 4:1 ratio,
with no overlap in users or messages between the two sets.
Results. As shown in Table 3, the pairwise diffusion esti-
mator demonstrates strong predictive performance, achiev-
ing AUC scores of 0.9042 on Olympics and 0.9186 on
Movie, indicating its effectiveness in distinguishing diffu-
sion from non-diffusion behaviors. To evaluate the influ-
ence scoreL U (c), we compare its values onobservedmes-
sage–audience combinations(c i, Ui)againstpermutedcom-
binations(c i, Uj)withi̸=j, whereU i is the actual au-
dience group for messagec i andU j is unrelated. Figure 3
shows that observed combinations yield significantly higher
scores (mean: 0.76 vs. 0.53 for Olympics; 0.79 vs. 0.45
for Movie), with minimal overlap between distributions. A
Mann–WhitneyUtest confirms these differences are highly
significant (p <0.001), demonstrating thatL U (c)effec-
tively captures audience-specific diffusion potential.
Visualization. Figure 4 presents representative messages
from the Olympics dataset with low and high influence

Texts with high influence scores
Silver medalist in China working in her restaurant.  Meanwhile bronze medalist
in India.
@CRhodes92 @BartRiles @T_REX1991 The women’s basketball league has
won the big 12 6 times since Mack took over btw
0.888
Texts with low influence scores
Images with high influence scores Images with low influence scores
0.287
ONE WEEK TO GO
🥳 #Paris2024 #Paralympics 0.789
IT ALL COMES DOWN TO THIS.
🥇
🥈
🥉  #Paris2024 x #Basketball 0.769
@DeadlineDayLive That would be a huge move! Real Madrid getting Haaland
could shake up European football.
0.836
0.290
 0.355
 0.360
 0.361
0.825
0.815
 0.806
4 cr = $500k is far more than wht any actual Olympic medalist frm US/Europe/
Can/Oz will get frm her govt. We have skewed the taxpayer money mngt biz in India...
0.311
0.719 0.711
@mr_mayank True. The PM should have intervene and at least get her the Silver
 Medal she earned rightfully
0.302
Figure 4: Representative text and image examples across different levels of influence scoresL U (c).
scores. Low-scoring examples typically lack topical rele-
vance or suffer from weak linguistic or visual quality. In
contrast, high-scoring messages exhibit strong contextual
alignment, coherent composition, and features (e.g., emo-
tion) that are more likely to engage the target audience.
Editor Estimation
In this section, we firstly describe the implementation details
and experimental setup of information editor. We then out-
line the baselines and evaluation metrics, and present both
quantitative and qualitative comparisons with baselines. Fi-
nally, we conduct an ablation study on the reward function.
Implementation & Settings. We trained the policy net-
work for 350 episodes with a trajectory length of 3, using the
Adam optimizer with a learning rate of1×10 −4. For image
content generation, each input message was first converted
into a text-to-image prompt by GPT-4 and then processed
by PixArt-αto generate the initial image. For evaluation,
we sampled 200 messages from the Olympics test set and
computed their influence scores. The 40 messages with the
lowest scores were used as the test set, while the remaining
160 messages formed the training set.
Baselines. We compare our framework with the follow-
ing baselines (detailed implementation could be found in
the appendix): (1)Large Language Model (LLM): directly
prompts a pretrained language model to rewrite the input
message, without any audience-specific guidance; (2)In-
Context Learning (IC-L): for each audience group, retrieves
messages with the highest and lowest observed influence
scores as positive and negative exemplars, respectively, and
uses them as few-shot prompts to guide LLM-based rewrit-
ing; (3)Greedy Search (Greedy): as a non-learning variant
of our framework, uniformly samples editing actions and se-
lects the revised message with the highest reward at each
step, without learning a policy network.
Metrics. We assess our information editor using two met-
rics: (1)Diffusion Gain, which measures the relative in-
crease of influence scores after rewriting, and (2)Consis-
tency, which quantifies semantic preservation between orig-
inal and edited content via the cosine similarity of their fea-
tures. The details can be found in the appendix.
Diffusion Gain↑ Consistency↑
Text
Ours 20.69% 0.9510
LLM 14.03% 0.9590
IC-L 13.43% 0.9509
Greedy 17.93% 0.9470
Image
Ours 11.20% 0.8730
LLM 1.36% 0.8743
IC-L 3.05% 0.8748
Greedy 7.93% 0.8693
Table 4: Quantitative comparison with baselines.
Quantitative Comparison. Table 4 presents the perfor-
mance on both text and image generation tasks. In the text
task, our method achieves the highest Diffusion Gain at
20.69%, significantly outperforming other baselines. Ad-
ditionally, our method attains a high Consistency score
(0.9510), indicating effective semantic preservation. Al-
though LLM achieves slightly higher Consistency (0.9590),
its diffusion improvement is considerably weaker. For the
image task, our method again leads with a Diffusion Gain
of 11.20%, surpassing other baselines. In terms of Consis-
tency, IC-L (0.8748) and LLM (0.8743) slightly exceed our
score (0.8730). However, the difference is minimal, confirm-
ing that our edits maintain semantic integrity while deliver-
ing significantly better diffusion performance.
Qualitative Comparison. Figure 5 illustrates representa-
tive generation results for both text and image content. In
the text examples, our framework transforms generic state-
ments into vivid, action-oriented language that heightens
emotional engagement and topical relevance while preserv-
ing the original intent. In the image examples, our approach
enhances visual appeal by emphasizing human subjects, re-
sulting in more compelling and audience-aware imagery.
Ablation Study. We assess the reward function by compar-
ing the variant optimizing only the influence gain component
∆L. Table 5 shows the results. When trained with only the
influence gain, the model boosts diffusion but sacrifices se-

Original
@MythNix @HimuraShintaX @Hoophall @Nike @nikebasketball
@Converse @chicagobulls @MiamiHEAT @cavs @FIBA @Lakers
@WashWizards if you think he dont suppose to be in the finals against
those teams then thats just saying you think his comp in the east was
wack .
@PaulKearney65 @adam_stillfedup If an athlete wins back to back
Olympic golds and receives less coverage than an athlete who doesn't
medal to me that is unfair and shows a bias. If an athlete is celebrated not
on merit but for identity that is wrong. Facts aren't snide.
Ours
@MythNix @HimuraShintaX @Hoophall @Nike @nikebasketball
@Converse @chicagobulls @MiamiHEAT @cavs @FIBA @Lakers
@WashWizards
 Think he shouldn't face off in the finals? That
means you believe his Eastern rivals weren't tough enough!
@PaulKearney65 @adam_stillfedup Ever notice how sometimes an
athlete with back-to-back Olympic golds gets less attention than a non-
medalist?
 This really highlights a bias. We should focus on
celebrating athletes for what they've achieved, not who they are.
Remember, facts speak for themselves, not with sarcasm.
LLM
Hey @MythNix @HimuraShintaX @Hoophall @Nike
@nikebasketball @Converse @chicagobulls @MiamiHEAT @cavs
@FIBA @Lakers @WashWizards, if you believe he shouldn't be in the
finals facing those teams, then you're basically saying his Eastern
Conference rivals were weak!
@PaulKearney65 @adam_stillfedup
 When an athlete secures
consecutive Olympic golds but gets overshadowed by someone who
didn't even medal, it's simply unjust and reveals a clear bias. Celebrating
athletes based on identity rather than achievement is misguided. Facts
speak for themselves and aren't snide!
IC-L
@MythNix @HimuraShintaX @Hoophall @Nike @nikebasketball
@Converse @chicagobulls @MiamiHEAT @cavs @FIBA @Lakers
@WashWizards Does he deserve to face these legendary teams in the
finals?
 If not, you're saying the competition in the East was weak!
Back-to-back Olympic golds should shine brighter! It's puzzling
when an athlete with no medal gets more spotlight.
 Merit should lead
the celebration, not identity. Let's keep it fair! #AthleteMerit
#OlympicGold
Greedy
@MythNix @HimuraShintaX @Hoophall @Nike @nikebasketball
@Converse @chicagobulls @MiamiHEAT @cavs @FIBA @Lakers
@WashWizards
 Do you really think he shouldn't have a finals spot
among these legendary teams? If so, maybe you believe the East's
competition is falling short!
@PaulKearney65 @adam_stillfedup
 Isn't it astonishing when an
athlete clinches back-to-back Olympic golds but gets overshadowed by
someone who doesn't even medal? That seems unfair, revealing a clear
bias. Celebrating athletes for identity over merit? That's just not right.
Facts aren't snide—they're the truth!
0.360
0.528
0.380
0.362
0.450
0.356
0.456
0.343
0.408
0.430
0.445
0.576
0.454
0.469
0.514
0.435
0.503
0.359
0.387
0.45
Texts Images
Figure 5: Qualitative comparison with baselines. Each piece of content is annotated with its corresponding influence score.
Diffusion Gain↑ Consistency↑
Text
√
∆L · C 20.69% 0.9510
∆L 21.98% 0.9471
Image
√
∆L · C 11.20% 0.8730
∆L 12.43% 0.8707
Table 5: Results of ablation study.
mantic accuracy. This highlights the importance of incorpo-
rating semantic similarity, as it ensures that the content re-
mains meaningful while still achieving improved diffusion.
User Study
We conducted a user study to evaluate whether the generated
content increases users’ likelihood of sharing information in
realistic settings.
Procedure & Metric. We conducted a user study on the
Prolific platform (Prolific 2025), recruiting native English
speakers with informed consent. Participants were screened
based on their X activity and recent engagement with the
target topic. A total of 100 qualified users were selected (76
male, 24 female; ages: 18–25 (11%), 26–50 (68%), 51–60
(21%)). Each participant evaluated 100 tweet pairs and 100
image pairs, each consisting of an original and a revised ver-
sion of either text or visual content. For each pair, partic-
ipants selected the version they were more likely to share
(via retweet or reply). To mitigate ordering bias, all pairs
were presented in randomized order.
We evaluated performance using theRetweet Preference
Rate(RPR)—the average proportion of times the rewritten
version was preferred by our participants.
Results & Analysis. The results indicate that the gener-
ated content significantly increased participants’ willingness
to retweet. The overall RPR was62.36%(64.00%for text
and60.72%for image), suggesting that enhancements in
both modalities contribute to improved diffusion impact. A
paired-sample t-test confirmed that the overall preference for
the rewritten content is statistically significant (p <0.001).
We further analyzed participants’ stated reasons for their
choices. Common reasons included stronger emotional res-
onance and alignment with personal experiences.
Discussion and Conclusion
In this work, we introduce a novel task,Diffusion-Oriented
Content Generation, and propose a reinforcement learning
(RL)–based framework that rewrites messages to enhance
diffusion among targeted audiences. Central to our approach
is an influence indicator that estimates the diffusion potential
of content for a given audience, without relying on explicit
network topology. Based on this indicator, we develop an
information editor that optimizes message rewrites for max-
imal diffusion. We model the editor as a finite-horizon MDP
and adopt a stationary policy for practicality, which remains
effective even though optimal policies are generally non-
stationary. Experiments on real-world datasets show that our
indicator accurately predicts diffusion outcomes, and that
the RL-based rewriting strategy yields significant diffusion
gains while maintaining semantic fidelity.
Despite promising performance, our method still has lim-
itations. Our current iterative rewriting strategy incurs sig-
nificant latency per instance. Integrating diffusion feedback
directly into the generative model could mitigate this, but
real-world diffusion signals are often noisy, hindering reli-
able feedback integration. Our method currently does not
account for temporal variations in audience features, and in-
corporating such dynamics remains an important direction
for future research. Another future work is to explore more
modalities beyond text and image. Extending the framework
to audio and video could enhance its practicality.

Acknowledgments
Nan Cao is the corresponding author. This work was sup-
ported by the National Key Research and Development Pro-
gram of China (2023YFB3107100).
References
Alipour, S.; Galeazzi, A.; Sangiorgio, E.; Avalle, M.; Bo-
jic, L.; Cinelli, M.; and Quattrociocchi, W. 2024. Cross-
platform social dynamics: an analysis of ChatGPT and
COVID-19 vaccine conversations.Scientific Reports, 14(1):
2789.
Bakshy, E.; Rosenn, I.; Marlow, C.; and Adamic, L. 2012.
The role of social networks in information diffusion. InPro-
ceedings of the international conference on World Wide Web,
519–528.
Benevenuto, F.; Rodrigues, T.; Cha, M.; and Almeida, V .
2009. Characterizing user behavior in online social net-
works. InProceedings of the ACM SIGCOMM Conference
on Internet Measurement, 49–62.
Brown, T.; Mann, B.; Ryder, N.; Subbiah, M.; Kaplan, J. D.;
Dhariwal, P.; Neelakantan, A.; Shyam, P.; Sastry, G.; Askell,
A.; et al. 2020. Language models are few-shot learners.Ad-
vances in neural information processing systems, 33: 1877–
1901.
Chen, J.; Yu, J.; Ge, C.; Yao, L.; Xie, E.; Wu, Y .; Wang, Z.;
Kwok, J.; Luo, P.; Lu, H.; and Li, Z. 2023. PixArt-α: Fast
Training of Diffusion Transformer for Photorealistic Text-
to-Image Synthesis. arXiv:2310.00426.
Chen, W.; Wang, Y .; and Yang, S. 2009. Efficient influ-
ence maximization in social networks. InProceedings of
the ACM SIGKDD international conference on Knowledge
discovery and data mining, 199–208.
Cheng, J.; Adamic, L.; Dow, P. A.; Kleinberg, J. M.; and
Leskovec, J. 2014. Can cascades be predicted? InPro-
ceedings of the international conference on World wide web,
925–936.
Coppolillo, E.; Cinus, F.; Minici, M.; Bonchi, F.; and Manco,
G. 2025. Engagement-driven content generation with large
language models. InProceedings of the 31st ACM SIGKDD
Conference on Knowledge Discovery and Data Mining V . 2,
369–379.
De Francisci Morales, G.; Monti, C.; and Starnini, M. 2021.
No echo in the chambers of political interactions on Reddit.
Scientific reports, 11(1): 2818.
Dumoulin, V .; Belghazi, I.; Poole, B.; Mastropietro, O.;
Lamb, A.; Arjovsky, M.; and Courville, A. 2017. Adver-
sarially Learned Inference. arXiv:1606.00704.
Etta, G.; Sangiorgio, E.; Di Marco, N.; Avalle, M.; Scala, A.;
Cinelli, M.; and Quattrociocchi, W. 2023. Characterizing
engagement dynamics across topics on Facebook.Plos one,
18(6): e0286150.
Flamino, J.; Galeazzi, A.; Feldman, S.; Macy, M. W.; Cross,
B.; Zhou, Z.; Serafino, M.; Bovet, A.; Makse, H. A.; and
Szymanski, B. K. 2023. Political polarization of news media
and influencers on Twitter in the 2016 and 2020 US presi-
dential elections.Nature Human Behaviour, 7(6): 904–916.
Goldenberg, J.; Libai, B.; and Muller, E. 2001. Talk of the
network: A complex systems look at the underlying process
of word-of-mouth.Marketing letters, 12: 211–223.
Gomez-Rodriguez, M.; Leskovec, J.; and Krause, A. 2012.
Inferring networks of diffusion and influence.ACM Trans-
actions on Knowledge Discovery from Data (TKDD), 5(4):
1–37.
Goodfellow, I.; Pouget-Abadie, J.; Mirza, M.; Xu, B.;
Warde-Farley, D.; Ozair, S.; Courville, A.; and Bengio, Y .
2020. Generative adversarial networks.Communications of
the ACM, 63(11): 139–144.
Granovetter, M. 1978. Threshold models of collective be-
havior.American journal of sociology, 83(6): 1420–1443.
Guille, A.; Hacid, H.; Favre, C.; and Zighed, D. A. 2013.
Information diffusion in online social networks: A survey.
ACM Sigmod Record, 42(2): 17–28.
Hodas, N. O.; and Lerman, K. 2014. The simple rules of
social contagion.Scientific reports, 4(1): 4343.
Iamnitchi, A.; Hall, L. O.; Horawalavithana, S.; Mubang, F.;
Ng, K. W.; and Skvoretz, J. 2023. Modeling information dif-
fusion in social media: data-driven observations.Frontiers
in Big Data, 6: 1135191.
Islam, M. R.; Muthiah, S.; Adhikari, B.; Prakash, B. A.;
and Ramakrishnan, N. 2018. Deepdiffuse: Predicting
the’who’and’when’in cascades. In2018 IEEE international
conference on data mining (ICDM), 1055–1060. IEEE.
Jiang, J.; Ren, X.; and Ferrara, E. 2023. Retweet-bert: polit-
ical leaning detection using language features and informa-
tion diffusion on social networks. InProceedings of the in-
ternational AAAI conference on web and social media, vol-
ume 17, 459–469.
Kempe, D.; Kleinberg, J.; and Tardos, ´E. 2003. Maximizing
the spread of influence through a social network. InPro-
ceedings of the ACM SIGKDD international conference on
Knowledge discovery and data mining, 137–146.
Kingma, D. P.; Welling, M.; et al. 2013. Auto-encoding vari-
ational bayes.
Li, D.; Li, J.; and Hoi, S. 2023. Blip-diffusion: Pre-trained
subject representation for controllable text-to-image genera-
tion and editing.Advances in Neural Information Process-
ing Systems, 36: 30146–30166.
Li, Y .; and Xie, Y . 2020. Is a picture worth a thousand
words? An empirical study of image content and social me-
dia engagement.Journal of marketing research, 57(1): 1–19.
Meng, F.; Xie, J.; Sun, J.; Xu, C.; Zeng, Y .; Wang, X.; Jia, T.;
Huang, S.; Deng, Y .; and Hu, Y . 2025. Spreading dynamics
of information on online social networks.Proceedings of the
National Academy of Sciences, 122(4): e2410227122.
Notarmuzi, D.; Castellano, C.; Flammini, A.; Mazzilli, D.;
and Radicchi, F. 2022. Universality, criticality and complex-
ity of information propagation in social media.Nature com-
munications, 13(1): 1308.
Pastor-Satorras, R.; and Vespignani, A. 2001. Epidemic
spreading in scale-free networks.Physical review letters,
86(14): 3200.

Podell, D.; English, Z.; Lacey, K.; Blattmann, A.; Dockhorn,
T.; M¨uller, J.; Penna, J.; and Rombach, R. 2023. SDXL: Im-
proving Latent Diffusion Models for High-Resolution Image
Synthesis. arXiv:2307.01952.
Pressgrove, G.; McKeever, B. W.; and Jang, S. M. 2018.
What is Contagious? Exploring why content goes viral on
Twitter: A case study of the ALS Ice Bucket Challenge.In-
ternational Journal of Nonprofit and Voluntary Sector Mar-
keting, 23(1): e1586.
Prolific. 2025. Prolific: Participant recruitment for online
research. https://www.prolific.com. Accessed: 2025-06-06.
Radford, A.; Kim, J. W.; Hallacy, C.; Ramesh, A.; Goh, G.;
Agarwal, S.; Sastry, G.; Askell, A.; Mishkin, P.; Clark, J.;
et al. 2021. Learning transferable visual models from nat-
ural language supervision. InInternational conference on
machine learning, 8748–8763. PmLR.
Radford, A.; Metz, L.; and Chintala, S. 2016. Unsupervised
Representation Learning with Deep Convolutional Genera-
tive Adversarial Networks. arXiv:1511.06434.
Raffel, C.; Shazeer, N.; Roberts, A.; Lee, K.; Narang, S.;
Matena, M.; Zhou, Y .; Li, W.; and Liu, P. J. 2020. Explor-
ing the limits of transfer learning with a unified text-to-text
transformer.Journal of machine learning research, 21(140):
1–67.
Rombach, R.; Blattmann, A.; Lorenz, D.; Esser, P.; and Om-
mer, B. 2022. High-resolution image synthesis with latent
diffusion models. InProceedings of the IEEE/CVF confer-
ence on computer vision and pattern recognition, 10684–
10695.
Sankar, A.; Zhang, X.; Krishnan, A.; and Han, J. 2020. Inf-
V AE: A variational autoencoder framework to integrate ho-
mophily and influence in diffusion prediction. InProceed-
ings of the international conference on web search and data
mining, 510–518.
Shahbaznezhad, H.; Dolan, R.; and Rashidirad, M. 2021.
The role of social media content format and platform in
users’ engagement behavior.Journal of Interactive Market-
ing, 53(1): 47–65.
Spasojevic, N.; Li, Z.; Rao, A.; and Bhattacharyya, P. 2015.
When-to-post on social networks. InProceedings of the
ACM SIGKDD International Conference on Knowledge
Discovery and Data Mining, 2127–2136.
Sutton, R. S.; McAllester, D.; Singh, S.; and Mansour, Y .
1999. Policy gradient methods for reinforcement learning
with function approximation.Advances in neural informa-
tion processing systems, 12.
Tian, X.; Li, W.; Xu, B.; Yuan, Y .; Wang, Y .; and Shen, H.
2025. MIGE: Mutually Enhanced Multimodal Instruction-
Based Image Generation and Editing. InProceedings of the
33rd ACM International Conference on Multimedia, MM
’25, 10622–10631. ACM.
Tong, H.; Prakash, B. A.; Eliassi-Rad, T.; Faloutsos, M.; and
Faloutsos, C. 2012. Gelling, and melting, large graphs by
edge manipulation. InProceedings of the ACM interna-
tional conference on Information and knowledge manage-
ment, 245–254.
V osoughi, S.; Roy, D.; and Aral, S. 2018. The spread of true
and false news online.science, 359(6380): 1146–1151.
Weng, L.; Menczer, F.; and Ahn, Y .-Y . 2013. Virality predic-
tion and community structure in social networks.Scientific
reports, 3(1): 2522.
Xu, J.; Lu, T.-C.; Compton, R.; and Allen, D. 2014. Quan-
tifying cross-platform engagement through large-scale user
alignment. InProceedings of the ACM conference on Web
science, 281–282.
Zhang, B.; Zhang, P.; Dong, X.; Zang, Y .; and Wang, J. 2024.
Long-clip: Unlocking the long-text capability of clip. InEu-
ropean conference on computer vision, 310–325. Springer.
