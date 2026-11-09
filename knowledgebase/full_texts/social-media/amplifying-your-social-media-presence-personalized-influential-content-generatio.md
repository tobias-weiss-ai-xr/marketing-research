---
title: 'Amplifying Your Social Media Presence: Personalized Influential Content Generation with LLMs'
url: https://arxiv.org/abs/2505.01698
category: social-media
subcategory: empirical
date: 2025-05
venue: ''
authors:
- Yuying Zhao
- Yu Wang
- Xueqi Cheng
- Anne Marie Tumlin
- Yunchao Liu
source: arxiv
pdf_url: https://arxiv.org/pdf/2505.01698
pages: 12
chars: 47594
fetched_at: '2026-11-08T13:01:37+00:00'
kb_version: 1
---

# Amplifying Your Social Media Presence: Personalized Influential Content Generation with LLMs

Amplifying Your Social Media Presence:
Personalized Influential Content Generation with LLMs
Yuying Zhao1, Yu Wang2, Xueqi Cheng1, Anne Marie Tumlin1,
Yunchao Liu1, Damin Xia1, Meng Jiang3, Tyler Derr 1
1Vanderbilt University,2University of Oregon, 3University of Notre Dame
{yuying.zhao, xueqi.cheng, anne.m.tumlin, yunchao.liu, damin.xia, tyler.derr}@vanderbilt.edu
yuwang@uoregon.edu, mjiang2@nd.edu
Abstract
The remarkable advancements in Large Lan-
guage Models (LLMs) have revolutionized the
content generation process in social media, of-
fering significant convenience in writing tasks.
However, existing applications, such as sen-
tence completion and fluency enhancement, do
not fully address the complex challenges in
real-world social media contexts. A prevalent
goal among social media users is to increase
the visibility and influence of their posts. This
paper, therefore, delves into the compelling
question: Can LLMs generate personalized in-
fluential content to amplify a user’s presence on
social media? We begin by examining preva-
lent techniques in content generation to assess
their impact on post influence. Acknowledg-
ing the critical impact of underlying network
structures in social media, which are instru-
mental in initiating content cascades and highly
related to the influence/popularity of a post, we
then inject network information into prompt
for content generation to boost the post’s in-
fluence. We design multiple content-centric
and structure-aware prompts. The empirical
experiments across LLMs validate their ability
in improving the influence and draw insights
on which strategies are more effective. Our
code is available at https://github.com/
YuyingZhao/LLM-influence-amplifier
1 Introduction
Large Language Models (LLMs) have marked a
significant milestone in content generation. Their
applications span a diverse range of areas, includ-
ing but not limited to question answering, transla-
tion, and summarization (Hadi et al., 2023). On
social media platforms, users can leverage these
tools to facilitate the content creation process. For
instance, a user might specify keywords or pro-
vide the initial part of a post, enabling the model
to generate content based on this input. Alterna-
tively, a user could submit the entire post, seeking
Figure 1: Many social media users strive to maximize
their influence, seeking more reposts and likes. In real-
ity this is quite challenging and they may only receive
engagement from a small portion of their audience. How
can a user create a post that gains larger influence?
the model’s assistance in refining the content for
enhanced coherence and fluency. These comple-
tion or refinement methods substantially reduce the
writing burden of content creators, allowing users
to focus more on the creative aspects rather than
the writing details, thereby offering considerable
convenience (Radensky et al., 2024).
Nevertheless, the objectives of completing a sen-
tence or enhancing its fluency do not entirely en-
capsulate the inherent complexities encountered
in real-world social media environments. In such
settings, content generation is not the sole ultimate
goal. Many social media users aspire to increase
their posts’ visibility and influence (Kempe et al.,
2003). This objective differs fundamentally from
generating or refining sentences which can be mea-
sured by comparing the pair of generated content
and the target content. As illustrated in Fig. 1,
when a user posts a piece of information, it will
disseminate according to the underlying network
that connect users together. This demonstrates that
gaining popularity is not a simple pairwise task but
a multifaceted challenge involving complex interac-
tions among multiple users. Social media strategist
can contribute to this goal of gaining popularity by
analyzing the interests and behavior patterns of the
target audience. However, scaling these insights
to a larger audience and applying them to revise
posts can be challenging in practice. In order to
automate such process, we turn to LLMs.
arXiv:2505.01698v1  [cs.SI]  3 May 2025

Inspired by the success of LLMs in general con-
tent generation tasks, we explore their potential in
this complex social task by posing the question:
Can LLMs generate personalized influential con-
tent to amplify a user’s presence on social media?
Addressing this question is challenging since it
requires (1) a deep understanding of how generated
content spreads within social networks, and (2) the
development of effective strategies to amplify its
dissemination. To answer this question, we first de-
sign a content-aware influence estimator which en-
ables the influence evaluation of generated content
so that we have the tool to determine which strate-
gies are more effective. Equipped with the evalua-
tor, we investigate whether the commonly utilized
strategies for adapting LLMs to downstream tasks
are effective in improving content influence (named
as content-centric strategies). Furthermore, the so-
cial network structure is crucial for the content
propagation. In Fig. 2, we show how the online
community structure (i.e., neighborhood) largely
impacts the information spread through a simple
example. For instance, a creator is currently think-
ing about writing a post about LLM. With the given
keywords, the main idea of the generated content
might be positive (e.g., LLM is great) or negative
(e.g., Avoid LLM). The impact of these two posts
vary significantly on diverse networks. If the major-
ity of neighbors are tech-friendly, the positive post
about new technology is highly likely to intrigue
more reposts than a negative one in Fig. 2(a, b). A
similar case happens when the majority of neigh-
bors are tech-skeptical in Fig. 2(c, d). Inspired
by the significance of structure, we design several
strategies to extract local neighborhood informa-
tion of the content creator and inject them into the
prompting (named as structure-aware strategies).
Our main contributions are summarized as:
• To the best of our knowledge, we are the initial
work to explore whether LLMs help improve
influence spread in social media.
• We design a content-aware influence estimator
and devise multiple content-centric and structure-
aware prompts to amplify the social impact.
• We empirically evaluate the proposed prompts
on various LLMs to validate their ability in am-
plifying the influence.
2 Related Work
Here we review works on the estimation of influ-
ence spread and LLM applications in social media.
Figure 2: Online community structure matters: the same
post related to LLM will spread differently in a tech-
friendly versus tech-skeptical local neighborhood.
2.1 Influence Estimation
Influence estimation aims to approximate the num-
ber of influenced nodes, denoted as σ(S), of a
given seed set S (Li et al., 2018). This pro-
cess is initially performed based on independent
cascade (IC) or linear threshold (LT) model via
Monte Carlo (MC) simulation (Kempe et al.,
2003), which is computationally expensive. To
improve the efficiency, simulation-based speedup
techniques (Leskovec et al., 2007; Goyal et al.,
2011), proxy-based approach (Kimura and Saito,
2006; Chen et al., 2010), and sampling-based ap-
proach (Tang et al., 2014; Nguyen et al., 2016;
Huang et al., 2017) are proposed. In addition to
these traditional methods, deep learning (DL) tech-
niques have been developed to estimate influence
on large-scale networks (Li et al., 2023). Deep-
Cas (Li et al., 2017) predicts the size of cascade
through sampling node sequence from cascade,
learning subgraph embedding with Gated Recur-
rent Unit (GRU) model, and predicting the size
with a multilayer perceptron (MLP). DeepInf (Qiu
et al., 2018) predicts user-level social influence
(i.e., the action status of a user given neighbor-
hood status and local structure information) based
on a convolutional network and attention network.
Furthermore, there is a growing trend towards in-
corporating contextual information, such as top-
ics (Li et al., 2019), locations (Cai et al., 2020),
and temporal data (Meirom et al., 2021), to en-
hance influence estimation. Despite these advance-
ments, only a few study estimate influence us-
ing the detailed content which is crucial for the
estimation (Chen et al., 2023). CMINet (Chen
et al., 2023) proposes a graph-based framework for
content-aware multi-channel influence diffusion
which is able to fully leverage content information
consisting of various types (e.g., texts, images, and
videos). While most traditional methods improve
the efficiency of influence estimation, they are in-
herently non-differentiable and thus not suitable
for end-to-end training. In this study, we develop

context-aware method pioneered by CMINet, pre-
training a model to predict the likelihood of influ-
ence while incorporating content information into
training. While CMINet focuses on estimating in-
fluence given fixed content, we aim to generate
content that maximizes influence.
2.2 LLMs in Social Media
LLMs have been extensively adopted across vari-
ous downstream tasks (Hadi et al., 2023). Specif-
ically, within the domain of social media, LLMs
have been utilized to improve the personalized rec-
ommendation so that a higher-qualified feed will be
presented to the audience (Zhao et al., 2024). Addi-
tionally, LLMs have revolutionized content genera-
tion, exhibiting the capability to produce text in di-
verse styles (Grimme et al., 2023; Meier, 2024) and
generate persuasive content (Burtell and Woodside,
2023). LLM agents have been designed to select
the influencer in digital advertising campaigns with
simulation of real-world dynamics (Zhang et al.,
2024). Despite these advancements, a comprehen-
sive analysis exploring the potential of LLMs to
enhance content dissemination remains absent.
3 Content-Aware Influence Estimator
To generate influential content, we need to under-
stand the definition of influence and therefore it can
be used for potential optimization and further eval-
uation. Equipped with the preliminary knowledge
in the last section, we introduce our content-aware
method to estimate the influence of a new piece
of content. Specifically, we (1) train a model to
estimate the pairwise influence of the probability
that a user would repost a given content by another
user based on the historical interactions; (2) obtain
the content influence based on the commonly-used
cascade model and the learned probability.
3.1 Pairwise Influence Estimation
The likelihood of reposting behavior is affected
by post content and author identity. For example,
if two creators post similar content but a viewer
prefers one creator over the other, the chances of
the viewer reposting the content will vary signif-
icantly. This observation leads to our design of
a pairwise influence estimator Pθ(ur, uc, c). It is
trained to predict the probability that a potential
recipient user ur will repost the content c posted
by creator uc. The probability equation is:
Pθ(ur, uc, c) =sigmoid

xur ⊤diag(xc)xuc

Detailedly, xur = MLPU (EU ur ), xuc =
MLPU (EU uc), and xc = MLPC(EC c ) where EU
and EC are the user and content embeddings, EU ur
denotes the embedding for user ur and similar no-
tations for the content side. EU is learnable em-
bedding while EC is non-learnable and obtained
from the text of posts via a sentence embedding
model1. To perform the matrix multiplications, the
embeddings are all mapped to the same dimen-
sion through two multi-layer perceptron (MLP) for
users and content respectively. The diag operation
transforms a vector into a square diagonal matrix.
The final score is passed through sigmoid func-
tion to obtain the probability. The detailed model
architecture is in the Appendix.
To train the model, the dataset is constructed
based on the historical interactions. The for-
mat of each instance in the training dataset D is
(ur, uc, c, pc) where pc represents the probability
of whether user ur will repost content c created
by user uc. To build the instances, for each con-
tent c posted by uc, we collected the users who
have reposted it as positive samples and the users
who follow uc but do not repost c as the negative
instances. We assign 1 for the positive instances
and 0 for the negative instances. There could be
many negative instances if the creator has many
followers, resulting in severe data imbalance and
computational expenses. To avoid these issues, we
randomly sample two users from the negative set.
We form this problem as a regression problem
and train the predictor parameterized by θ with the
following Mean Square Error (MSE) loss:
L = E(ur,uc,c,pc)∈D(Pθ(ur, uc, c) − pc)2.
3.2 Content Influence Estimation
Given social network structure G and probabili-
ties derived from the pairwise influence estimator
Pθ(ur, uc, c), we estimate the influence of a user
u posting content c (denoted as I c u) using the Inde-
pendent Cascade Model (Kempe et al., 2003). In
this work, we adopt the following relationship as
the underlying network structure.
The influence estimation is achieved through
Monte Carlo simulations, where the process is re-
peated multiple times to obtain the average influ-
ence spread. In each simulation, user u is the ini-
tial active node. The activation then propagates to
neighbors based on the pre-determined probabil-
ities from the pairwise influence estimator. The
1Sentence-Transformer: https://sbert.net/

activations continue until no further activation hap-
pens. The number of activated nodes in a single
simulation is represented by Ni. The influence I c u
of user u posting content c is calculated as the aver-
age number of activated nodes over R simulations:
I c u =
PR
i=1 Ni
R . (1)
3.3 Problem Statement
In this paper, our focus is on generating content
with substantial influence. Formally, a user u can
pre-define certain elements of the content they wish
to generate, which are represented as Cu. Exam-
ples of Cu include keywords, the initial part of
a sentence, or even the entire sentence. 2 This
user-defined components are utilized to form the
prompts according to various prompting strategies
(i.e., P(Cu)). The generated content after feeding
the prompt to a LLM M is denoted as M(P(Cu)).
Our goal is to obtain the best prompting strategy
that can generate content of a high influence, mea-
sured as I c u. Formally, the objective is defined as:
P ∗ = argmax
P
Eu
h
I M(P(Cu)) u
i
(2)
Fig. 3 shows our framework to solve this problem.
4 Content-Centric Strategies
In this section, we explore the prevalent in-context
learning (ICL) techniques in content generation to
assess their impact on the influence of the gener-
ated posts. ICL is an advanced prompting strat-
egy, which could potentially boost the downstream
tasks (Dong et al., 2022). We explore commonly
used zero-shot and few-shot settings.
For zero-shot ICL, we define the scenario in
social media and formalize the task to generate
posts of high influence (Prompt 1). For few-shot
ICL, in addition to the provided information in
the zero-shot setting, we provide several posts of
high/low influence as examples (Prompt 2). The
posts used in the prompt are sampled from the train-
ing dataset where we heuristically treat the top20%
posts sorted by influence 3 as posts of high influ-
ence and the bottom 20% as posts of low influence.
2While our primary focus is on revising the original content
to be more influential/popular, it’s important to note that other
elements can also be accommodated by modifying the prompts
and inputs used in training.
3The reposting behavior in the real world is a reliable
indicator of the post’s influence. Therefore, for training posts,
we use the repost number to measure the influence.
Based on whether the sampled posts are personal-
ized to the input post, there are two variants:
• Prompt 2.1 [fixed to all posts]: the sampled in-
stances are randomly drawn from the entire list
of popular/unpopular posts in the training dataset
and fixed for different inputs.
• Prompt 2.2 [personalized to the input post]: the
sampled instances vary for input posts where the
selected instances are the top similar posts in the
textual embedding space.
Prompt 1: Content-Centric-Zero-Shot
Instruction: Imagine you have a piece of text that you
want to share on social media, but you want to ensure it
catches the maximum attention and engagement from your
audience. Your task is to creatively revise the original text
to make it more engaging and more likely to be shared
widely. The revised version should retain the core message
but be optimized to resonate with social media trends and
audience preferences. Your goal is to transform the text
into a revised one that can lead to a larger cascade of shares,
likes, and comments.
Input Data: Input text={input post}.
Prompt 2: Content-Centric-Few-Shot
Instruction: Imagine ... Your goal is to ...
Demonstration: Following are the examples of popular
posts: {sampled popular posts}. Following are the exam-
ples of unpopular posts: {sampled unpopular posts}.
Input Data: Input text={input post}.
5 Structure-Aware Strategies
Content-centric strategies focus on the textual con-
tent but ignore the structural information, which
will result in a sub-optimal performance in con-
tent dissemination. Inspired by the significant role
of network structures in information spread (Li
et al., 2023), we propose structure-aware strategies
in this section to inject neighborhood information
into prompt for generation.
Specifically, we augment prompt from P(Cu) in
Eq. 2 to P(Cu, N h u ) to include the neighborhood
information N within the specified network where
h is the number of hops and N h u are the users who
needs at least h steps for a content to spread from
the creator u. For instance, in the following net-
work, the neighbors are those who follow the cre-
ator directly or can be reached via paths in the
network. These target recipients N h u , once receiv-
ing the post, could facilitate the information spread
by reposting the message. Given the limitations
imposed by prompt length, although the entire set
of the historical reposts from the audience contains

Figure 3: The overall framework consists of the following steps: (1) input data are collected based on prompt
requirement; (2) prompts are generated using content-centric and structure-aware strategies; (3) the prompts are fed
into LLMs to generate posts; and (4) the influence of the generated posts is evaluated through spread modeling.
a full knowledge of their observed interests, it is im-
practical to incorporate all these posts into prompt.
To best describe the neighborhood briefly, one can
extract the representative posts from the audience’s
interactions, or directly summarize the audience’s
interests. Different ways are explored below and
their prompts are listed as Prompt 3 and Prompt 4.
Prompt 3: Structure-Aware-Neighbor-Posts
Instruction: Imagine ... Your goal is to ...
Neighborhood Information Your audience has interacted
with the following posts: {posts from neighborhood inter-
actions}. Based on their preferences, now transform the
text for higher popularity.
Input Data: Input text={input post}.
Prompt 4: Structure-Aware-Neighbor-Interest
Instruction: Imagine ... Your goal is to ...
Neighborhood Information Your audience has the fol-
lowing interest: {summarized interest from neighborhood
interactions}. Based on their preferences, now transform
the text for higher popularity.
Input Data: Input text={input post}.
5.1 Representative Posts
In Prompt 3, we inject the posts from neighborhood
historical interactions to represent the interests of
the potential audiences. Based on how the posts
are selected, we have the following variants:
• Prompt 3.0 [randomly from all training posts]:
posts are randomly selected from the whole train-
ing dataset.
• Prompt 3.1 [randomly from the historical inter-
actions of neighborhood]: the content that the
neighbors has interacted with indicates the inter-
est, the posts are randomly sampled from their
historical reposts.
• Prompt 3.2 [randomly from the historical inter-
actions of influential neighborhood] : since an
influential user has many audiences, targeting
this user could potentially lead to a large cascade.
Based on this, posts are sampled from the history
of most influential audience.
5.2 Summarized Interests
Prompt 4 describes the neighborhood information
by summarizing their interests. Specifically, a list
of posts from the audience are first obtained and
the interests from these posts are summarized us-
ing LLMs into a short sentence. The prompts for
summarizing the interests are as follows.
Prompt: Interest Summarization
Instruction: Your goal is to summarize the interest of
your audience based on their interactions and output the
interests immediately, without any explanation or intro-
duction. Your audience have interacted with the following
posts: {Neighborhood Posts}. The response should be the
interests and they are separated by ‘;’.
Similarly, there are two variants based on the
ways to obtain the neighborhood posts:
• Prompt 4.1 [uniform sampling]: firstly, a neigh-
bor is randomly sampled from the neighborhood
and then the post is randomly selected from this
user’s repost history. This process is repeated
until reaching the defined number.
• Prompt 4.2 [score-based sampling]: the uniform
method treats each audience equally, however,
users will affect content spread differently. In-
tuitively, (1) if a user has more followers (i.e.,
higher degree), this user has a higher potential
to increase the content’s influence, (2) the impor-
tance of audience from 1-hop neighbors differs
from that of 2-hop, as the latter is influenced
by the activation of the former based on the dif-
fusion model. Based on these two factors, we
use message passing in Graph Neural Networks
(GNNs) (Wu et al., 2020), which inherently uti-
lizes the structure, as an aggregator to calcu-
late the importance. More specifically, the user
embedding is initialized as the binary encoding
whose length equals user number and the element
is set to 1 for user id otherwise 0. Then these em-
beddings are propagated based on a variant of
non-parametric GCN to obtain the aggregated
results with E(l+1) = D 1 2 AD 1 2 E(l), where A is

Figure 4: Probability comparison between the original post and the revised post.
the adjacency matrix and D is the diagonal de-
gree matrix. The i-th position of the aggregated
embedding is the importance of user i. Note that
different than the traditional GCN where node
with high degree is punished, we assign higher
weights for high-degree node due to their impor-
tance in spreading the information. After having
the importance, the audience is sampled based
on the softmax probability and this process is
repeated until reaching the pre-defined number.
6 Experiments
In this section, we aim to answer the following:
• RQ1: How well can the strategies amplify the
influence of the generated post?
• RQ2: How effective is the influence estimator?
• RQ3: How does the neighborhood in the prompt
affect the dissemination of the generated content?
• RQ4: How does user popularity relate to the con-
tent spread and the amplification effect through
the strategies?
6.1 Settings
We conduct experiments on the publicly available
Weibo dataset4 that is commonly used for influ-
ence study (Qiu et al., 2018). This dataset contains
the raw text of the weibo posts and the follow-
ing relationships between users as well as their
post/repost behaviors. We use the repost interac-
tions to train the pairwise influence estimator and
use the following relationship as the underlying
social network structure. For LLMs, we conduct
experiments on the following models: Phi-2 and
Phi-3 from Microsoft (Abdin et al., 2024), Mistral
from Mistral AI (Jiang et al., 2023). We also ex-
plore LLaMA 2 from Meta (Touvron et al., 2023),
which exhibits strong ethical constraints and often
refuses to perform the revision task. Consequently,
we do not include it in this comparison. The de-
tails about the datasets, models, hyperparameters,
4Weibo Dataset: http://aminer.org/Influencelocality
and computing infrastructure are included in Ap-
pendix. Our code is available at https://github.
com/YuyingZhao/LLM-influence-amplifier.
6.2 RQ1: Effectiveness
To evaluate the effectiveness, we investigate from
two perspectives. From a local probability per-
spective: targeting a single user, whether LLM can
improve the probability of this user’s repost be-
havior? Furthermore, given the current inference
challenges, it is impractical to design personalized
content for each viewer. A piece of content will be
generated and disseminated to the audience rather
than one individual. This inspires the global per-
spective. To evaluate how many users will be im-
pacted globally, we measure the influence spread.
These two perspectives provide unique benefits.
The local aspect (i.e., singular-user scenario) iso-
lates the challenge of aggregating interests from a
user’s network and focuses primarily on the indi-
vidual repost probability. The global aspect (i.e.,
influence spread) requires dedicated consideration
of multiple simulations and reposting rounds as
well as a broader range of users, thus presenting
the more complex scenario.
6.2.1 Singular-User Scenario
The local perspective evaluates a single tuple
(ur, uc, c) to assess whether userur will repost con-
tent c posted by user uc. Ideally, content tailored
specifically to an individual user is hypothesized
to be more influential. To empirically test this hy-
pothesis and verify the effectiveness of LLM in im-
proving the influence on singular user, we employ
LLM prompted with content c and randomly se-
lected reposts from user ur that reflect their content
preferences according to Prompt 3. The effective-
ness is assessed by analyzing 20 posts processed
by different LLMs, as illustrated in Fig. 4. For
each post, we compute the average influence prob-
ability over 20 randomly chosen neighbors. For
better clarity of the visualization, The arrangement
of posts is organized by the repost probability prior
to revision. Vertical lines connect the pre- and post-

Table 1: Content-Centric: influence spread.
Zero-Shot Few-Shot
Prompt 1 Prompt 2.1 Prompt 2.2
Phi-2 122.97 (+0.86%) 137.75 (+12.99%) 133.96 (+9.88%)
Phi-3 140.43 (+15.18%) 145.24 (+19.13%) 144.83 (+18.79%)
Mistral 139.18 (+14.16%) 141.68 (+16.2%) 139.31 (+14.27%)
Average +10.73% +16.77% +14.31%
revision states of each post, where a solid green line
indicates the revision increase in influence proba-
bility, and a grey dashed line indicates a decrease.
The majority of revised posts demonstrate an in-
creased probability, thus supporting the efficacy of
the LLM. Specifically, the success rates for increas-
ing influence probability after the revision are 70%
for Phi-2, 90% for Phi-3, and 85% for Mistral, in-
dicating a substantial potential of LLMs to enhance
content impact in single-user scenarios.
6.2.2 Influence Spread: Content-Centric
The influence spread is calculated according to
Eq. (1). The average spread of the original posts
is 121.92. The results for different prompts and
LLMs are reported in Table 1, which also includes
the relative gain compared with the original posts.
The table provides several key insights:
LLM Comparison: All combinations of the LLMs
and prompts result in an enhanced influence spread
over the original posts, confirming the broad ef-
ficacy of LLMs in amplifying content impact.
Notably, within the same series, Phi-3 model,
which possesses more parameters, outperforms
its smaller counterpart, Phi-2. Conversely, de-
spite having a larger parameter set, Mistral slightly
under-performs Phi-3, potentially due to specific as-
pects of its architectural design or training dataset.
Among the prompts, Phi-3 consistently shows supe-
rior performance. This observation also aligns with
singular-user scenario where Phi-3 has the highest
ratio of improving the probability.
Prompts Comparison: All prompts consistently
improve the influence spread across LLMs, val-
idating the effectiveness of the LLM-aided con-
tent generation for higher popularity/influence.
Prompts utilizing multiple examples (few-shot)
show greater improvements over their counterparts
without examples (15.54 % vs. 10.73 %), under-
scoring the effectiveness of including examples.
Moreover, prompts that sample globally from pop-
ular/unpopular posts (Prompt 2.1) prove to be more
effective than those sampling locally based on the
input content (Prompt 2.2), highlighting the value
of a broader sampling strategy.
Figure 5: Influence evaluation performance comparison.
6.2.3 Influence Spread: Structure-Aware
Similarly, we report the average influence spread
for the structure-aware prompts in Table 2. Note
that these prompts are based on Prompt 1 (zero-
shot) and they can be used simultaneously with the
few-shot strategies. Compared with the Prompt
1 with an average of 10.73 % improvement, the
prompts with the structural information consis-
tently have a better improvement. This shows that
incorporating the neighborhood information is ben-
eficial in boosting the influence. Additionally, di-
rectly incorporating the sampled posts (Prompt3.∗)
is more effective than the summarized interests
(Prompt 4.∗). Targeting the most influential audi-
ence does not guarantee a better improvement as
evidenced by Prompt 3.2 and Prompt 4.2.
6.3 RQ2: Effectiveness of Influence Estimator
To verify the effectiveness of the influence esti-
mator, we compare its performance with differ-
ent variants based on the same independent cas-
cade model. These compared methods differ in the
probability assignment to the edges in the network.
Our content-aware evaluator learns the probability
based on the historical interactions. We compare
other probability assignments including (1) uni-
formly assigning a fixed probability to all edges,
with explored values ranging from 0.1 to 0.6, and
(2) employing the inverse of node degree as the
probability, a strategy to mimic the user’s behavior
where individuals following numerous others are
less likely to further propagate a message.
One inherent challenge in measuring the perfor-
mance is the absence of concrete ‘ground truth’
data regarding the influence of generated content,
as these contents have not been disseminated in
real-world settings. However, the collected posts
have actual repost behavior in practice, providing
a reliable indicator of the influence. Therefore, for
the collected posts, we treat the users who reposted
the post as the positive ground truth and those who
are within the following network without repost
behavior as the negative ground truth. Based on
the ground truth, we calculate the Recall, Preci-

Table 2: Structure-Aware: average influence spread across different prompts.
Sampled Posts Summarized Interests
Prompt 3.0 Prompt 3.1 Prompt 3.2 Prompt 4.1 Prompt 4.2
Phi-2 135.79 (+11.37%) 136.62 (+12.06%) 131.88 (+8.17%) 131.44 (+7.81%) 129.0 (+5.81%)
Phi-3 148.48 (+21.79%) 146.69 (+20.32%) 144.69 (+18.67%) 144.93 (+18.87%) 143.44 (+17.65%)
Mistral 145.42 (+19.27%) 141.88 (+16.37%) 140.68 (+15.39%) 143.49 (+17.69%) 139.16 (+14.14%)
Average +17.48% 16.25% +14.08% +14.79% +12.53%
Figure 6: Performance gain comparison for different
hops: (A) Phi-2, (B) Phi-3, (C) Mistral.
sion, and F1 for the simulations and get the average
scores. Fig. 5 presents the results. From the figure,
we notice a clear trend for the methods with fixed
probabilities. As probability increases, the recall
will improve and the precision will decrease. This
trend is expected, as higher probabilities typically
yield a greater number of positive instances. In
comparison, methods employing inverse degree ad-
justments exhibit higher precision but lower recall.
This is attributed to the reduced probabilities as-
sociated with high-degree users. In contrast, our
method has the best F1 score when compared with
the others. This underscores the significant role
of content in influencing spread estimation. Our
content-aware approach more reliably estimates
influence probabilities, thereby enhancing the ac-
curacy of influence estimation.
6.4 RQ3: Impact of Neighborhood
The number of hops determines the creator neigh-
borhood and will affect the prompts that use
neighborhood information, including posts-based
prompts 3.1 and 3.2, and interest-based prompts
4.1 and 4.2. The results are shown in Fig. 6. For
Prompt 3.1 and 4.1 which are both based on ran-
domly sampled posts, they are not affected signifi-
cantly. For Prompt 3.2 and 4.2 that favor influential
audience, there is a varied trend as the number of
hops increases. For post-based prompt, the perfor-
mance drops for all LLMs including a significant
drop for Phi-2. The interest-based one shows a
consistent improvement. Comparing prompt 4.1
and 4.2, influential-based sampling is better than
random-based sampling for multiple hops.
Figure 7: Group-level influence spread and gain (Phi-3).
6.5 RQ4: Analysis Across User Groups
We group users into three even groups based on
follower numbers. Group 1 has the lowest degree
and Group 3 has the highest. Results are shown in
Fig. 7. The influence spread per group shows that
the influence spread is highly related to the user
degree where the higher degree users tends to have
larger influence, aligning with real-world observa-
tion. We also plot the relative gain compared with
original post. Generally the users with low and
high degrees have a larger improvement. For low
degree users it is possible their initial spread is low
and the ratio for improvement becomes high. For
high degree users, despite their initial large spread,
the improvements are the highest. This suggests
that cautions need to be paid in practice for such
revising tool which might enlarge the difference be-
tween popular and unpopular creators. The results
for two other LLMs are in the Appendix.
7 Conclusion
In this work, we investigate the intriguing question:
Can LLMs generate personalized influential con-
tent to amplify a user’s presence on social media?
We propose a content-aware influence estimator
to evaluate the influence of generated content and
design diverse content-centric and structure-aware
prompts. Through empirical experiments, we vali-
date that LLMs can improve the content influence
and draw insights on which prompts are more ef-
fective. In the future, we aim to optimize LLMs to
generate influential content from a model perspec-
tive. While fixing the best prompt strategy, how to
find the optimal model poses new challenges.

Limitations and Discussions
Our study aims to help benign users amplify their
social presence. While these methods are promis-
ing and can potentially help many users to reach
their goal, they also present risks, as they could be
a double-edged sword. We acknowledge the poten-
tial for misuse by malicious users to spread mis-
information. In practice, similar strategies might
already be in use by these users to spread misinfor-
mation, even without our research. One limitation
of this work is the absence of direct strategies to
counter such misuse. However, our work can serve
as an essential first step by simulating how adver-
saries might devise and execute such tactics. Ex-
isting works on misinformation prevention mainly
focuses on detection. However, preventing mis-
information spread is as crucial as designing the
detection. In the age of LLMs, the quality of the
generated misinformation has been improved by
leveraging the open-world knowledge encoded in
LLMs, which inherently increases the challenges
of detecting misinformation. Furthermore, the cost
of generating misinformation is largely reduced
and malicious users now can produce and spread
higher-quality misinformation at an unprecedented
rate. Therefore, the content evading detection, even
if of a small percentage, will result in a substantial
volume of misleading posts online. Such spread of
misinformation poses a high threat to society. By
understanding and replicating potential adversarial
behavior, this research lays a strong foundation for
future initiatives focused on developing effective
countermeasures against misinformation dissemi-
nation.
In this study, we focus on explicit following re-
lationships as the foundation of the social network.
However, on modern social media platforms, infor-
mation can also be disseminated through recom-
mendations, where content is suggested to potential
recipients by the platform. Therefore, in practice,
it is possible to extract a recommendation network
and combine it with the following network to an-
alyze information propagation in a more compre-
hensive and realistic manner. While our framework
can be extended to the recommendation or merged
networks, the findings presented here are restricted
to the following network.
References
Marah Abdin, Sam Ade Jacobs, Ammar Ahmad Awan,
Jyoti Aneja, Ahmed Awadallah, Hany Awadalla,
Nguyen Bach, Amit Bahree, Arash Bakhtiari, Harki-
rat Behl, et al. 2024. Phi-3 technical report: A
highly capable language model locally on your phone.
arXiv.
Matthew Burtell and Thomas Woodside. 2023. Artifi-
cial influence: An analysis of ai-driven persuasion.
arXiv.
Taotao Cai, Jianxin Li, Ajmal Mian, Rong-Hua Li,
Timos Sellis, and Jeffrey Xu Yu. 2020. Target-aware
holistic influence maximization in spatial social net-
works. IEEE TKDE, 34(4):1993–2007.
Hsi-Wen Chen, De-Nian Yang, Wang-Chien Lee,
Philip S Yu, and Ming-Syan Chen. 2023. Cminet: a
graph learning framework for content-aware multi-
channel influence diffusion. In ACM Web Conference
2023, pages 545–555.
Wei Chen, Chi Wang, and Yajun Wang. 2010. Scalable
influence maximization for prevalent viral marketing
in large-scale social networks. In KDD, pages 1029–
1038.
Qingxiu Dong, Lei Li, Damai Dai, Ce Zheng, Zhiy-
ong Wu, Baobao Chang, Xu Sun, Jingjing Xu, and
Zhifang Sui. 2022. A survey on in-context learning.
arXiv.
Amit Goyal, Wei Lu, and Laks VS Lakshmanan. 2011.
Celf++ optimizing the greedy algorithm for influence
maximization in social networks. In Proceedings
of the 20th international conference companion on
WWW, pages 47–48.
Britta Grimme, Janina Pohl, Hendrik Winkelmann, Lu-
cas Stampe, and Christian Grimme. 2023. Lost in
transformation: Rediscovering llm-generated cam-
paigns in social media. In Multidisciplinary Interna-
tional Symposium on Disinformation in Open Online
Media, pages 72–87. Springer.
Muhammad Usman Hadi, Rizwan Qureshi, Abbas Shah,
Muhammad Irfan, Anas Zafar, Muhammad Bilal
Shaikh, Naveed Akhtar, Jia Wu, Seyedali Mirjalili,
et al. 2023. A survey on large language models:
Applications, challenges, limitations, and practical
usage. Authorea Preprints.
Keke Huang, Sibo Wang, Glenn Bevilacqua, Xiaokui
Xiao, and Laks VS Lakshmanan. 2017. Revisiting
the stop-and-stare algorithms for influence maximiza-
tion. VLDB, 10(9):913–924.
Albert Q Jiang, Alexandre Sablayrolles, Arthur Men-
sch, Chris Bamford, Devendra Singh Chaplot, Diego
de las Casas, Florian Bressand, Gianna Lengyel, Guil-
laume Lample, Lucile Saulnier, et al. 2023. Mistral
7b. arXiv.

David Kempe, Jon Kleinberg, and Éva Tardos. 2003.
Maximizing the spread of influence through a social
network. In KDD, pages 137–146.
Masahiro Kimura and Kazumi Saito. 2006. Tractable
models for information diffusion in social networks.
In European conference on principles of data mining
and knowledge discovery, pages 259–271. Springer.
Jure Leskovec, Andreas Krause, Carlos Guestrin,
Christos Faloutsos, Jeanne VanBriesen, and Natalie
Glance. 2007. Cost-effective outbreak detection in
networks. In KDD, pages 420–429.
Cheng Li, Jiaqi Ma, Xiaoxiao Guo, and Qiaozhu Mei.
2017. Deepcas: An end-to-end predictor of informa-
tion cascades. In WWW, pages 577–586.
Yandi Li, Haobo Gao, Yunxuan Gao, Jianxiong Guo,
and Weili Wu. 2023. A survey on influence maxi-
mization: From an ml-based combinatorial optimiza-
tion. ACM TKDD, 17(9):1–50.
Yuchen Li, Ju Fan, George Ovchinnikov, and Panagio-
tis Karras. 2019. Maximizing multifaceted network
influence. In ICDE, pages 446–457. IEEE.
Yuchen Li, Ju Fan, Yanhao Wang, and Kian-Lee Tan.
2018. Influence maximization on social graphs: A
survey. IEEE TKDE, 30(10):1852–1872.
Raphael Meier. 2024. Llm-aided social media influ-
ence operations. Large Language Models in Cyber-
security: Threats, Exposure and Mitigation , pages
105–112.
Eli Meirom, Haggai Maron, Shie Mannor, and Gal
Chechik. 2021. Controlling graph dynamics with
reinforcement learning and graph neural networks.
In ICML, pages 7565–7577. PMLR.
Hung T Nguyen, My T Thai, and Thang N Dinh. 2016.
Stop-and-stare: Optimal sampling algorithms for vi-
ral marketing in billion-scale networks. In Proceed-
ings of the 2016 international conference on manage-
ment of data, pages 695–710.
Jiezhong Qiu, Jian Tang, Hao Ma, Yuxiao Dong,
Kuansan Wang, and Jie Tang. 2018. Deepinf: Social
influence prediction with deep learning. In KDD,
pages 2110–2119.
Marissa Radensky, Daniel S Weld, Joseph Chee Chang,
Pao Siangliulue, and Jonathan Bragg. 2024. Let’s get
to the point: Llm-supported planning, drafting, and
revising of research-paper blog posts. arXiv.
Youze Tang, Xiaokui Xiao, and Yanchen Shi. 2014. In-
fluence maximization: Near-optimal time complexity
meets practical efficiency. In SIGMOD, pages 75–86.
Hugo Touvron, Louis Martin, Kevin Stone, Peter Al-
bert, Amjad Almahairi, Yasmine Babaei, Nikolay
Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti
Bhosale, et al. 2023. Llama 2: Open foundation and
fine-tuned chat models. arXiv.
Zonghan Wu, Shirui Pan, Fengwen Chen, Guodong
Long, Chengqi Zhang, and S Yu Philip. 2020. A com-
prehensive survey on graph neural networks. IEEE
transactions on neural networks and learning sys-
tems, 32(1):4–24.
Xiaoqing Zhang, Xiuying Chen, Yuhan Liu, Jianzhou
Wang, Zhenxing Hu, and Rui Yan. 2024. Llm-driven
agents for influencer selection in digital advertising
campaigns. arXiv.
Zihuai Zhao, Wenqi Fan, Jiatong Li, Yunqing Liu, Xi-
aowei Mei, Yiqi Wang, Zhen Wen, Fei Wang, Xi-
angyu Zhao, Jiliang Tang, et al. 2024. Recommender
systems in the era of large language models (llms).
IEEE TKDE.

A Appendix
A.1 Predictor Architecture
According to the equation of pairwise influence
estimator:
Pθ(ur, uc, c) =sigmoid

xur ⊤diag(xc)xuc

,
the pipeline is illustrated in Fig. 8. The user
embeddings are randomly initialized embeddings
which are learnable. Item embeddings are pre-
computed by feeding the posts into sentence
transformer (specifically, we used pre-trained sen-
tence model sentence-transformers/distiluse-base-
multilingual-cased-v25). They are fixed throughout
the training. There are two MLPs to transform the
embeddings into the same dimension for users and
items separately. Both of them have one hidden
layer. The dimensions in user MLP are [32, 64, 32]
for input layer, hidden layer, and output layer, and
[512, 128, 32] for item MLP. A dropout of 0.5 has
been applied to the layers to prevent over-fitting.
The batch size of training is set to 1024 and the
learning rate is 1e−4.
Figure 8: The pipeline of pairwise influence predictor.
A.2 Dataset
The original weibo dataset is downloaded from
http://aminer.org/Influencelocality. The original
data contains many files, we use the following in
our study since they contain all the necessary infor-
mation we need to conduct the investigation.
• root_content.txt: it contains the raw textual con-
tent of the posts;
• weibo_network.txt: it contains the following rela-
tionships between users;
• total.txt: it records the post and repost beheviors
(e.g., who created which post and who reposted
which post).
5The url of the specific sentence transformer model that
is used in the predictor: https://huggingface.co/sentence-
transformers/distiluse-base-multilingual-cased-v2
To mitigate the sparsity issues in the original
dataset, we perform the following preprocessing
steps. We use the authors of the top 20 mostly re-
posted content as the initial seed Useed and extract
the relevant users who has reposted Useed’ posts
and the users that Useed have reposted. These users
become the new seed. We repeat this process two
times to obtain the relatively dense users where
they have probabily interacted with the others in the
network. Additionally, only users having at least
one post behavior and one repost behavior have
participated in the above process. The network
structure is extracted based on the obtained user
subset where edges (u, v) are kept when u and v
both fall in the user subset. We further conduct the
pruning from the content perspective. When inves-
tigating the spread of posts, we focus on posts that
have at least been reposted by 5 users within the
users’ following network. The motivation behind
this is that we focus on the following relationship in
this study while the methodology can be extended
to other networks (e.g., implicit recommendation
network learned from historical interactions). The
post subset is splitted into train/val/test based on
60%/20%/20% proportion. After the prepossess-
ing steps, there are 13863 users and 6112 posts for
the influence investigation.
A.3 Hyperparameters
For predictor training, we set learning rate as 1e−4,
batch size as 1024, the dimension of user embed-
ding as 32. For prompt 2.1 and 2.2, we sample two
popular posts and two unpopular posts. For the
post-based prompts (3.1 and 3.2), the inserted post
number is set to 3. For the interest-based prompts
(4.1 and 4.2), there are 10 posts initially sampled
from the neighborhood to do the interest extraction.
We experienced out of memory issue when sam-
pling more posts in the current server. The number
of simulation rounds during influence evaluation is
set to 20.
A.4 Computing Infrastructure
The experiments in this work were conducted us-
ing an NVIDIA GeForce RTX 3090 GPU with
24GB memory. The operating system was Ubuntu
22.04.4 LTS. In terms of the software, our code for
LLM part is mainly based on the popular frame-
work called LitGPT6 that implemented 20+ high-
performance LLMs with recipes to pretrain, fine-
6LitGPT: https://github.com/Lightning-AI/litgpt

(a) Phi-2
 (b) Mistral
Figure 9: Group-level average influence spread and relative gain on Phi-2 and Mistral models.
tune and deploy at scale. An easy installation of
the packages can be achieved by pip install ‘lit-
gpt[all]’. Since we use sentence transformer to
compute the post embedding during pairwise influ-
ence predictor training, also need to download the
package using pip install -U sentence-transformers.
Detailed descriptions of the software environment
and code are provided in the readme in the zipped
code file.
A.5 LLMs
In our current work, we compare three models,
Phi-27, Phi-38 from Microsoft, and Mistral9 from
Mistral AI. The number of parameters in three mod-
els are 2.7B, 3.8B and 7B. In the future, we plan to
explore more LLMs.
A.6 Group-Level Results
The average influence spread and the relative im-
provement in percent are shown in Fig. 9 for the
other two models: Phi-2 and Mistral. Firstly, they
show the same trend for the average influence
spread with the observation in main content for
Phi-3, where users with high degree have a higher
influence spread. Additionally, except Prompt 1 in
Phi-2, the other prompts across models all have the
best improvement for group 3 with a high degree.
7Phi-2: https://huggingface.co/microsoft/phi-2
8Phi-3: https://huggingface.co/microsoft/Phi-3-mini-4k-
instruct
9Mistral: https://huggingface.co/mistralai/Mistral-7B-
Instruct-v0.3
