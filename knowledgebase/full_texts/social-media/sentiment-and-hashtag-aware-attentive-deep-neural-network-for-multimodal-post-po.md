---
title: Sentiment and Hashtag-aware Attentive Deep Neural Network for Multimodal Post Popularity Prediction
url: https://arxiv.org/abs/2412.10737
category: social-media
subcategory: empirical
date: 2024-12
venue: ''
authors:
- Shubhi Bansal
- Mohit Kumar
- Chandravardhan Singh Raghaw
- Nagendra Kumar
source: arxiv
pdf_url: https://arxiv.org/pdf/2412.10737
pages: 44
chars: 110904
fetched_at: '2026-11-08T13:09:55+00:00'
kb_version: 1
---

# Sentiment and Hashtag-aware Attentive Deep Neural Network for Multimodal Post Popularity Prediction

Sentiment and Hashtag-aware Attentive Deep Neural
Network for Multimodal Post Popularity Prediction
Shubhi Bansal1 (phd2001201007@iiti.ac.in), Mohit Kumar1 (cse190001038@iiti.ac.in),
Chandravardhan Singh Raghaw1(phd2201101016@iiti.ac.in),
Nagendra Kumar1 (nagendra@iiti.ac.in)
1Department of Computer Science and Engineering, Indian Institute of Technology Indore,
Khandwa Road, Simrol, Indore 453552, Madhya Pradesh, India.
Corresponding Author:
Shubhi Bansal
Department of Computer Science and Engineering, Indian Institute of Technology Indore,
Khandwa Road, Simrol, Indore 453552, Madhya Pradesh, India.
Tel: +91-7988361678
Email: phd2001201007@iiti.ac.in
arXiv:2412.10737v1  [cs.IR]  14 Dec 2024

Sentiment and Hashtag-aware Attentive Deep
Neural Network for Multimodal Post Popularity
Prediction
Abstract
Social media users articulate their opinions on a broad spectrum of subjects and
share their experiences through posts comprising multiple modes of expression,
leading to a notable surge in such multimodal content on social media plat-
forms. Nonetheless, accurately forecasting the popularity of these posts presents
a considerable challenge. Prevailing methodologies primarily center on the con-
tent itself, thereby overlooking the wealth of information encapsulated within
alternative modalities such as visual demographics, sentiments conveyed through
hashtags and adequately modeling the intricate relationships among hashtags,
texts, and accompanying images. This oversight limits the ability to capture
emotional connection and audience relevance, significantly influencing post pop-
ularity. To address these limitations, we propose a seNtiment and hAshtag-aware
attentive deep neuRal netwoRk for multimodAl posT pOpularity pRediction,
herein referred to as NARRATOR that extracts visual demographics from faces
appearing in images and discerns sentiment from hashtag usage, providing a more
comprehensive understanding of the factors influencing post popularity Moreover,
we introduce a hashtag-guided attention mechanism that leverages hashtags as
navigational cues, guiding the model’s focus toward the most pertinent features
of textual and visual modalities, thus aligning with target audience interests and
broader social media context. Experimental results demonstrate that NARRA-
TOR outperforms existing methods by a significant margin on two real-world
datasets. Furthermore, ablation studies underscore the efficacy of integrating vi-
sual demographics, sentiment analysis of hashtags, and hashtag-guided attention
mechanisms in enhancing the performance of post popularity prediction, thereby
facilitating increased audience relevance, emotional engagement, and aesthetic
appeal.
Keywords: Multimodal Data Analysis, Hashtags, Sentiment, Deep Neural Network,
Social Media Analysis
2

1 Introduction
The explosive growth of Social Network Services (SNS) such as Flickr1, Facebook2 and
Instagram3, has revolutionized content creation and consumption [1, 2]. Users now ac-
tively generate and share vast amounts of User-Generated Content (UGC) in a wide
array of formats such as texts, images, audios and videos. This has not only trans-
formed online interactions but also resulted in a massive influx of UGC [3] as exhibited
by Flickr receiving 25 million daily uploads 4 and Instagram 1.3 billion 5. This abun-
dance of content has led to information overload, making it increasingly difficult to
discover relevant and engaging information. Popularity prediction emerges as a crucial
solution, and aims to forecast the level of public attention UGC will receive early on.
This is vital because only a small fraction of UGC truly captures widespread attention,
while the vast majority remains unnoticed. By predicting popularity and identifying
hot content early on, users can easily navigate information overload. The ability to
forecast which content will capture public attention provides insights by identifying
patterns in what resonates with their interests, revolutionize how users understand
and interact with the digital world, and enable content creators to tailor their content
for maximum impact. Popularity prediction models can empower platforms to make
strategic decisions, optimize resource allocation, and enhance targeted advertising [4].
Moreover, the insights gained from popularity prediction can be leveraged to inform
government policies and schemes, enhancing the effectiveness of public services. Accu-
rate popularity forecasting has broad applications such as online marketing, and trend
detection, leading to improved service effectiveness and advancements in areas such
as recommender systems [5, 6], online advertising [7, 8], information retrieval [9, 10]
and demand forecasting [11]. By analyzing patterns in what captures public attention,
we gain insights into sentiment shifts and evolving user behaviors. These insights, in
turn, drive advancements in sentiment analysis [12], digital marketing [13], and user
privacy protection [14, 15], empowering us to make more informed decisions in the
complex digital landscape.
Unveiling Hashtag-guided Attention Mechanism : Existing approaches to
fuse multimodal data for popularity prediction employ attention [16] mechanisms
to adjust feature weights dynamically. These mechanisms range from self-attention
[17, 18], hierarchical attention [19], which focus on individual modalities, to mecha-
nisms capturing interactions among modalities. For instance, context-aware attention
[20] captures interplay among content, time and user, dual-attention [21] considers
both image-caption pairs and user environment , user guided hierarchical attention [22]
learns the user’s influence on texts and images, and hierarchical fusion [23] operates
on textual and visual modalities and attributes. However, these approaches predom-
inantly focus on intrinsic content features, overlooking the influence of hashtags on
image and text interpretation. Hashtags [24] i.e., words with the “#” prefix, are widely
used by SNS users to provide valuable contextual cues. They encode semantic rela-
tionships that reveal the creator’s intended message and desired perception. Hashtags
1https://www.flickr.com/
2https://www.facebook.com/
3https://www.instagram.com/
4https://photutorial.com/flickr-statistics/
5https://www.omnicoreagency.com/instagram-statistics/
3

facilitate event and topic dissemination, bridging complex concepts with messages and
connecting content at a granular level. Neglecting this rich source of information lim-
its the accuracy of popularity prediction models, as hashtags significantly impact the
interpretation and engagement of social media posts. Empirical evidence underscores
the power of hashtags in boosting visibility since posts with hashtags garner twice
the level of engagement than those without [25]. For instance, in the given example
Figure 1: Example Social Media Post
post (Figure 1), existing attention mechanisms would analyze the selfie itself, focusing
on the woman’s smile, the blurred crowd in the background, or colors in her cloth-
ing. However, they might miss the contextual richness embedded in hashtags such as
#chasefield, which pinpoints the location to a baseball game at Chase Field, #summer
which indicates the weather, and #azdbacks and #arizona guide the model’s atten-
tion toward relevant features in the selfie: her team jersey, revealing her support for a
specific team, the Arizona Diamondbacks. Therefore, it is crucial to leverage hashtags
to guide model attention towards contextually relevant content features. In the dy-
namic social media landscape, where trends and user preferences evolve rapidly, such
a mechanism is paramount for developing robust popularity prediction models.
Unveiling the Power of Visual Demographics: Previous studies on social me-
dia popularity prediction have largely relied on using metadata [26] and user profiles to
incorporate demographic information. However, these approaches have limitations, as
metadata can be incomplete or inaccurate, and user profiles may contain outdated or
intentionally misleading information. Moreover, relying solely on explicit user data can
raise privacy concerns. In contrast, extracting demographic attributes directly from vi-
sual cues, particularly faces, presents an untapped opportunity. Bakshiet al.[27] found
that among 1.1 million Instagram photos, those containing faces had a 38% higher
likelihood of receiving likes and a 32% higher likelihood of receiving comments. This
highlights the power of faces in capturing attention and conveying emotions, which
directly impacts the post’s popularity. Therefore, we aim to explore the untapped po-
tential of visual demographic analysis in improving popularity prediction models for
4

multimodal social media posts. By incorporating visual demographic information into
popularity prediction models, we can enhance their accuracy and predictive power.
Harnessing Sentiment from Hashtags : Existing methods [28–30] primarily
focus on harnessing sentiment from the textual content of social media posts, over-
looking the valuable sentiment information embedded in hashtags. Hashtags not only
convey topical information but also reveal user sentiment [31] and audience percep-
tion, both of which can significantly influence a post’s popularity. While prior studies
have leveraged structural [32, 33] and topical information [32, 34] from hashtags for
predicting the popularity of multimodal content, the influence of hashtag sentiment
remains underexplored. Figure 1 features a user’s selfie at a baseball game, annotated
with hashtags such as #baseball, #diamondbacks, and #arizona, conveying specific
content-related information. Hashtags such as #smile, #funtimes, and #goodtimes
reflect the user’s sentiment during the event. The sentiment expressed through hash-
tags can mirror the audience’s collective perception of the content, providing valuable
insights into ongoing conversations and prevailing trends. Emotional intensity within
topics tends to generate more engagement, with hashtags encapsulating sentiments
that might not be fully expressed in captions alone. Despite the potential of hashtag
sentiment analysis for enhancing popularity prediction, it remains an underutilized re-
source. This research gap presents an opportunity to develop more comprehensive and
accurate methods by incorporating the sentimental insights embedded in hashtags.
To address the identified research gaps, we propose NARRATOR, a Sentiment and
hAshtag-aware deep neuRal netwoRk for multimodAl posT pOpularity pRediction.
NARRATOR introduces a novel hashtag-guided attention mechanism allows the model
to dynamically weigh the importance of different features in images and text, guided
by the contextual cues provided by hashtags. This enables a more comprehensive un-
derstanding of the interplay between content and context. Furthermore, NARRATOR
leverages visual cues within images to gain demographic insights, discerning fine-
grained details such as age, gender, race, and emotions directly from faces. Moreover,
NARRATOR explicitly incorporates sentiments extracted from hashtags, capturing
the subtle emotional undertones that resonate with audiences and further refining our
ability to predict post popularity. By combining these innovations- hashtag-guided
attention, leveraging visual demographics, and analysing sentiment of hashtags, NAR-
RATOR provides a deeper understanding of user engagement and emotional response,
improving the performance of popularity forecasts.
Our major contributions are enlisted below.
• We propose a deep neural network that leverages sentiment from hashtags, vi-
sual demographic information, and employs a hashtag-guided attention mechanism
to forecast post popularity comprehensively besides content-based features and
sentiment from text.
• We devise a novel hashtag-guided attention mechanism that uses hashtags to guide
the model’s focus on content features most relevant to the intended audience and
context.
• Our work pioneers the use of visual demographic information for popularity predic-
tion. We leverage visual demographics to identify engagement trends within specific
audience contexts.
5

• We derive sentiment information embedded in hashtags to decipher the emotional
appeal of a post and understand how it amplifies user engagement.
• Extensive experiments conducted on two real-world datasets demonstrate the su-
perior performance of our proposed method over existing state-of-the-art methods
both empirically and qualitatively.
The rest of the paper is structured as follows. The related works are covered
in Section 2. Section 3 presents a mathematical formulation of the problem. We elabo-
rate on our methodology in Section 4. The evaluations of experiments are then covered
in Section 5. Section 7 presents the concluding remarks of our research.
2 Related Work
In this section, we cover existing efforts in the domains of popularity prediction,
hashtag representation, and attention techniques.
2.1 Popularity Prediction in Social Media
Popularity prediction of online content has attracted significant research interest, with
scholars proposing diverse methodologies. These methodologies leverage a variety of
techniques, datasets, model structures, and problem formulations i.e., either classifi-
cation or regression. Kumar et al. [35] focused on predicting the popularity of news
articles, particularly their ability to attract user comments, offering the opportunity
for informed content modifications using various features extracted from article con-
tent. Lin et al.[36] devised a framework by stacking multiple regression models across
several layers, fostering synergies among diverse models to anticipate engagement of
posts on a platform similar to Flickr. Purba et al. [34] devised a novel approach for
predicting Instagram post engagement rates (ER) on a global dataset. It utilizes SVR
and incorporates features from hashtags, image analysis, user history, and manual
image assessment. Cao et al. [37] proposed CoupledGNN, a novel graph neural net-
work framework designed for predicting popularity with network awareness on social
platforms. This framework leverages two interconnected GNNs to capture the propa-
gation of influence. One GNN models the user activation status within the network,
while the other GNN models the dissemination of information itself. Mannepalli et
al. [38] leveraged a Long Short-Term Memory (LSTM) network to predict popularity
by combining features extracted from text content, user data, time series information,
and user sentiment analysis. Furthermore, Self-Adaptive Rain Optimization (SA-RO)
is employed to fine-tune the LSTM weights, enhancing the prediction accuracy. Tan
et al. [39] leveraged transformers for time series feature extraction and CatBoost for
feature selection, enabling comprehensive multi-view feature extraction and achieving
superior prediction accuracy on the Social Media Prediction Dataset.
The effectiveness of these approaches depends on the selection and quality of fea-
tures used to represent the content. These models may not capture several other
modalities comprising the social media post, and their interrelationships might have
been overlooked.
6

2.2 Hashtag Representation
Prior studies have not employed hashtags used in a post as the main feature in popu-
larity prediction tasks. According to Zappavigna [40], hashtags have a variety of uses
on social media, with subject markers serving as the most important ones. Hashtag
efficiently defines the topic of the post and help the user to easily identify if the post
is related to them or not. Few researchers have also explored the representation of
hashtags in the form of graphs. Liu et al. [41] proposed a network framework where
hashtags serve as nodes. Each node is linked to a collection of tweets, which them-
selves are comprised of individual words. To capture the inherent relationships within
this hierarchical, heterogeneous network, they introduce the Hashtag2Vec embedding
model. This model extends its embedding capability beyond hashtags to encompass
short social text elements (i.e., tweets) by simultaneously considering relationships be-
tween hashtags themselves (hashtag-hashtag), hashtags and tweets (hashtag-tweet),
tweets and their constituent words (tweet-word), and finally, word-to-word relation-
ships within tweets. Liao et al. [32] proposed a multimodal framework that analyzes
hashtag network structure semantics, and topic modeling besides captions and images
to predict popular influencer posts in Taiwan. Chakrabarti et al. [42] addressed the
challenge of maximizing social media popularity by recommending context-relevant
hashtags. The proposed framework leveraged post keywords, user popularity, and
trending hashtags to recommend effective hashtags.
However, these approaches focus on the structural and textual aspects of hashtags
ignoring the sentiment information embedded in them. Posts with positive or senti-
mental hashtags tend to perform better than those with neutral or negative hashtags.
This indicates that sentiment analysis of hashtags can be employed to forecast which
posts are more inclined to become viral.
2.3 Attention Mechanism
Many researchers have stated that using the attention mechanism as a part of the
popularity prediction model can significantly enhance performance. As many models
use images and texts as primary features to predict the popularity score, the attention
mechanism can help represent these features in a better way. Xu et al. [16] proposed
a regression model to predict popularity where they used an attention layer at the
top of the model and showed a significant improvement when compared to models
without attention. Lin et al. [17] utilized a self-attention mechanism to fuse semantic
and numeric features effectively for social media popularity prediction, outperforming
other methods. Bansal et al.[43] devised a word-level parallel co-attention mechanism
to derive an enriched representation of multimodal social media posts by capturing
the mutual influence of text and image on each other. Wang et al. [44] presented a
novel multimodal popularity prediction model grounded in hierarchical fusion, where
extracted features encompass visual elements, textual content, along with attributes
extracted from both modalities. The model innovatively integrates three integration
stages- early integration, representation integration, and modality integration - culmi-
nating in a fully fused vector inputted into an XGBoost regression model for effectively
estimating the virality of posts.
7

However, extant approaches prioritize local features, neglecting a holistic under-
standing of the content’s multimodal nature. To overcome this limitation, we propose
a novel multimodal deep learning model with an attention mechanism. This model
incorporates diverse feature types known to influence post popularity, encompassing
content characteristics, sentiment analysis, hashtag information, and user demograph-
ics. The proposed model uses transfer learning, deep learning, attention mechanism,
and graph neural networks to learn fine-grained representations of these features and
then feed these enhanced feature representations into a unified framework to estimate
the post popularity.
3 Problem Definition
Suppose there are P multimodal social media posts. Let pi denote the ith multimodal
post such that pi = {pt i, pv i , pd i , ph i , pm i }. Here, pt i = {wx i }X x=1 denotes the textual modal-
ity of the post, X denotes the length of the post caption and wx denotes xth word
appearing in pi. Furthermore, pv i and ph i denote the visual and hashtag modality of the
post such that ph i = {hj i }H j=1. Here, hi is the set of hashtags associated with post pi, j
is used to index a hashtag in set hi, H is the cardinality of hashtag set ( hi) assigned
to ( pi). The symbol pd i represents the demographic information such as age, gender,
race, and emotion on the faces of people appearing in images and pm i denotes meta-
data of pi and the user ( ui) who created it which contains followers count, following
count, post count, hashtag count, and caption length. We specify our problem using
the notations discussed above.
Given a multimodal social media post(pi), our aim is to train a functionf (.) that
allows us to forecast its popularity score.
ˆyi = f (pi) (1)
Here, ˆyi represents the predicted popularity score for the post pi. We frame the pop-
ularity prediction task as a regression problem. Our objective is to learn the enriched
feature representation of ( pi) and predict its popularity score.
4 Methodology
We introduce our novel methodological approach within this section. Figure 2 illus-
trates the architecture of our proposed framework for the popularity prediction of
multimodal posts. We analyze varied features that significantly influence the popu-
larity prediction of social media content. First, we investigate the textual features of
captions followed by visual features derived from images of social media posts. Addi-
tionally, we examine the demographic information from the faces of people appearing
in images accompanying social media posts. Then, several social features based on user
and post metadata are explored. We leverage content-based and sentiment-based in-
formation from hashtags and post captions to effectively capture the rich information
embedded in these posts. We derive topical and structural information from hashtags
annotated to these posts. We also learn the mutual influence of hashtags on visual and
textual modalities by devising a novel hashtag-guided attention mechanism. These
8

Figure 2: System Architecture of NARRATOR
features are then passed to several dense layers to predict the popularity score. Our
proposed framework entails a three-step process for accurately predicting the popu-
larity score of social media posts: (1) feature extraction, (2) feature interaction, and
(3) feature fusion for popularity prediction. These steps are discussed in detail below.
4.1 Feature Extraction
In this part of the paper, we discuss the feature retrieval procedure for multimodal
posts.
9

4.1.1 T extual F eature Extraction
Social media posts inherently rely on user-provided captions for context. To extract
a textual feature representation from these captions, we leverage a transformer-
based model known as Bidirectional Encoder Representations from Transformers
(BERT) [45]. Limited by its context-agnostic approach, word2vec [46] cannot effec-
tively handle homonyms. BERT, on the other hand, prioritizes the words surrounding
a target word during the embedding creation process. This enables BERT to capture
the nuances of language and generate more semantically rich representations.
For the textual modality of social media post (pt i) which comprises a word sequence
denoted by pt i = {wx i }W x=1, we add two tokens: class (CLS) and separator (SEP) to
indicate the beginning and end of the input text respectively. Here, W is the number
of words appearing in the post caption. We generate the corresponding set of tokens
T using the BERT tokenizer as given in Equation 2.
T = BERT T okenizer(pt i) (2)
We process the text sequence, denoted by T , through the BERT model as defined
in Equation 3. This process yields a 768-dimensional vector representation for each
token within the sequence.
B = BERT (T ) (3)
Here, B = {ex}M x=1 is a matrix that encodes the textual features extracted from
the post caption using BERT. This matrix comprises M rows, where M represents
the fixed length of the token sequence. Each row ex contains the 768-dimensional
BERT embedding for a corresponding token within the sequence (where x denotes
the token index ranging from 1 to M). For textual descriptions less than M , we apply
padding, otherwise, we perform truncation to make all textual descriptions of uniform
size. Further, we use Long Short Term Memory (LSTM) to model the sequential
relationship among words. The LSTM unit outputs a hidden state tx i for the current
word wx i by taking the embedding of the current word derived from BERT i.e., ex i and
the hidden state of the preceding time step tx−1 i as inputs as shown in Equation 4.
tx i = LST M(ex i , tx−1 i ) (4)
Here tx i ∈ RD, x = 1, 2, . . . , M, and D=768. For the sake of conciseness, we skip the
specific LSTM formulae. We stack hidden state feature vectors for each word derived
from LSTM to generate textual feature matrix E as given in Equation 5.
E = {tx i }M x=1 (5)
Here, E ∈ RM ×D is the textual feature matrix, and M = 15 denotes the maximum
length of the associated text for the post. The dimension of each tx i is RD where
D = 768 denotes the embedding dimension.
10

4.1.2 Visual F eature Extraction
The image of the social media post plays a pivotal role in predicting the post’s
popularity. Deep learning approaches for extracting visual information have pro-
gressed remarkably in recent years. To extract visual features of the post, we employ
VGG19 [47] model. The VGG19 model classifies 1.2 million images from the Ima-
geNet [48] database into 1000 categories during its training process. We extracted
visual features using the output of the final pooling layer of VGG19. We create sev-
eral feature vectors for a picture by retaining the regional feature vectors. The feature
matrix for an image ( V ) can be expressed as exhibited in Equation 6.
V = {vk i }K k=1 (6)
Here vk i ∈ RN , k = 1, 2, . . . , Kwith N = 512 which denotes the size of regional feature
vector. We retain K = 7×7 = 49 regional feature vectors for each image since the final
pooling layer of VGG-19 is a 7 × 7 × 512 tensor for 7 × 7 regions, each of which is rep-
resented by a 512-dimensional vector. Following the feature extraction stage, a fully
connected (FC) layer is employed to project each regional feature vector into a new vec-
tor space. This transformation ensures that the dimensionality of the resulting image
feature vectors aligns with the dimensionality of the text feature vectors, facilitating
their subsequent concatenation and joint processing within the model architecture.
The mathematical formulation for this transformation is presented in Equation 7.
I = {vk i }K k=1 (7)
Here, I is the visual feature matrix where I ∈ RK×D and vk i ∈ RD where D = 768 is
the embedding dimension for each regional feature vector.
4.1.3 Demographic F eature Extraction
We used DeepFace [49], a compact framework for identifying faces and analyzing char-
acteristics namely age, gender, race, and emotion from faces of people appearing in
images associated with the uploaded post. The VGG-Face model was used to investi-
gate DeepFace. In DeepFace, 101 nodes are present for predicting the age between 0
to 100 years of the person present in the image. The race model predicts six different
races namely Black, White, Asian, Middle Eastern, Indian, and Latino. The emotion
on the users’ faces is computed as one of the seven categories i.e., fear, sadness, hap-
piness, anger, disgust, surprise, and neutral. The gender of the user is defined as male
or female. Race, emotion, and gender were present as integral values. At last, we de-
rive the demographic feature vector by concatenating gender, age, emotion, and race
as given in Equation 8.
f d i = {g, a, e, r} (8)
Here, f d i denotes the derived demographic feature vector that has a dimension of 116
and g, a, e, rrepresents gender, age, emotion, and race.
11

Figure 3: Posts depicting Demographic Features
Figure 3 shows shows four Flickr posts where we used a DeepFace model to analyze
facial features and infer emotions and demographics. The first Flickr post shows an
Asian woman with long hair who appears to be in her early thirties, smiling and
happy. The second post shows an early middle-aged white man playing guitar and is
sad. The third post shows a man with eyes frowning and trying to silence; hence, the
inferred emotion from facial expression is fear. The fourth post is a man who is in his
late thirties, inferred ethnicity is black, and emotion is sad because of his furrowed
brows, downturned mouth, and dimly lit surroundings.
4.1.4 Hashtag F eature Extraction
In social media, hashtags serve as useful subject labels and search tools. Rather than
attractive titles or pictures, trendy hashtags are the reason behind some social me-
dia posts getting a lot of attention. Hashtags encapsulate important information that
should be incorporated in social media post representation. However, conveying textual
or topical information is just as crucial as providing the hashtag network’s structural
components. Hence, we define the hashtag feature as a combination of topic embed-
dings and node embeddings that represent the content of the hashtag and the graphical
structure between hashtags respectively. For the extraction of topic embeddings (Xh),
we used the BERTopic [50]. BERTopic is a topic modeling technique that builds topic
representations using the transformers framework and c-TFIDF. BERTopic first uses
sentence transformers to produce a number of document embeddings. Next, it uses
HDBSCAN [51] for document clustering and UMAP [52] for embedding dimension
reduction. In order to determine the relevance of each word inside each subject, we
compute the class-based TFIDF for every cluster (topic). The average of all docu-
ment embeddings inside a given subject is used to determine the topic embedding for
a particular topic.
12

For the structure embedding, we constructed a graph-like network where we used
hashtags as nodes of the network, and edges between two hashtags are created based
on co-occurrence. We assign weights to the edge as the number of times the two hash-
tags appear in a single post. Further, we calculated structure embeddings ¯Vh for each
node using GraphSAGE [53]. GraphSAGE is used for inductive representation learn-
ing on huge graphs. When creating low-dimensional vector representations of nodes,
GraphSAGE is particularly helpful for graphs that include a wealth of node attribute
data. The structural embedding of a post denoted by ¯Vh is determined only if there
are at least two hashtags present in the post and taking the average of node embed-
dings of hashtags appearing in the post. On the other hand, a zero-vector is allocated
as the structural embedding if a post is devoid of any hashtags. We then concatenate
the topic and structure embedding to derive the overall hashtag representation for the
post as shown in Equation 9.
f h i = {Xh ⊕ ¯Vh} (9)
Here, f h i is the resultant hashtag feature vector post pi, Xh is the topic embedding
and ¯Vh is the average hashtag node embedding.
4.1.5 Sentiment F eature Extraction
We embed each post caption into a 5-dimensional vector using Stanford’s CoreNLP
Sentiment Analysis tool6. The scale for sentiment values ranges from zero to four which
represents the likelihood that the sentence is extremely negative, negative, neutral,
positive, or very positive. This tool was created by the Stanford NLP group as a module
of the Stanford CoreNLP toolset [54]. Java is used to power Stanford’s CoreNLP.
Unlike Vader [55] and TextBLob which look at the sentiment of individual words,
Stanford CoreNLP output the sentiment values based on the entire sentence structure
resulting in improved performance. We derive the sentiment features from the post
caption as shown in Equation 10.
st = Stanf ord CoreN LP(pt i) (10)
Here, st denotes the sentiment feature vector derived from the textual modality of the
post ( pt i). We additionally treat hashtags as sentences and construct a 5-dimensional
vector from the hashtag modality ( ph i ) of the multimodal social media post using
Stanford CoreNLP.
sh = Stanf ord CoreN LP(ph i ) (11)
Here, sh denotes the hashtag-based sentiment feature vector having a dimension of 5.
The overall sentiment feature vector for the post ( pi) is derived by concatenating the
text-based and hashtag-based sentiment feature vectors as illustrated below.
f st i = concat(st, sh) (12)
Here, f st i is the resultant sentiment feature vector for the post (pi) having a dimension
of 10, st and sh denote the text-based and hashtag-based sentiment feature vectors,
respectively.
6https://stanfordnlp.github.io/CoreNLP/
13

4.1.6 Social F eature Extraction
The multimodal post’s popularity is influenced by both its content and the user who
posted it in terms of social media presence [56]. We have categorized social features
into two categories i.e., user metadata and post metadata. We discuss these two below.
1. User Metadata: The number of prior posts a user has made and their activity on
the platform are both strongly connected with the popularity of their most recent
post. Therefore, we have taken some user-centric features which are as follows:
(a) User Id: A unique integer defining the user on the platform uniquely.
(b) Average Views: It is obtained by computing the sum of all views over all the
posts posted by the user in the past divided by the number of his previously
uploaded posts.
(c) Group Count: Total number of groups the user has joined on that platform.
(d) Average Member Count: Average number of members in the group that the user
joined.
2. Post Metadata: The textual information associated with a post significantly influ-
ences the post’s popularity. A post with a large title may not get huge popularity
or a post with a large number of hashtags will appear more frequently so that it
may gain more popularity. The post metadata consists of:
(a) Tag Count: The number of hashtags a person used in their post.
(b) Title Length: Word count of the caption of the post.
(c) Description Length: Length of the description of the post
(d) Tagged People: It is defined by a binary number 0 if people are not tagged in
the post else 1.
(e) Comment Count: The number of comments received by a post from other users.
3. Time: Beyond user and content characteristics, predicting post popularity necessi-
tates incorporating temporal features. Research suggests a diurnal cycle in social
media activity, with weekends experiencing increased user engagement. Conse-
quently, posts uploaded during these high-activity periods are tend to garner more
views and interactions. To account for this temporal influence, we leverage the
following time-based features:
(a) Post Day: This categorical feature denotes the day of the week on which a
post is uploaded. We employ one-hot encoding to represent the post-day as a
7-dimensional vector.
(b) Post Month: This categorical feature indicates the month in which a post is
uploaded. Similar to post-day, one-hot encoding is used to represent the post-
month as a 12-dimensional vector.
(c) Post Time: This categorical feature captures the time of day during which a
post is uploaded. We divide the day into four distinct time segments (morning,
afternoon, evening, and night), each encompassing six hours. One-hot encoding
is then applied to represent the post time as a 4-dimensional vector.
(d) Post Duration: This numerical feature represents the number of days an image
remains posted on the platform (e.g., Flickr).
By incorporating these temporal features, our model can learn how time-related trends
impact post popularity, potentially leading to more accurate predictions. The social
14

feature vector (f s i ) is obtained using the user ID, average views, group count, average
member count, tag count, title length, description length, tagged people, comment
count, and temporal data.
4.2 Feature Interaction
The feature interaction module sheds light on how hashtags interact with textual
and visual modalities by devising a novel hashtag-guided attention mechanism. At
its core, this mechanism utilizes hashtags as guiding signals to focus the attention of
the predictive model on relevant features within the content. By considering hashtags
associated with the content, the model can better understand the context in which the
content is shared, leading to more accurate predictions. It allows the model to adapt its
focus dynamically, making it suitable for a wide range of content types and social media
platforms. Algorithm 1 shows how our devised hashtag-guided attention mechanism
leverages hashtags to guide attention toward relevant text and image features. The
use of hashtag embeddings and attention weights provides insights into the factors
influencing content popularity, making the model more interpretable for users and
content creators. By doing so, it aims to improve the prediction of social media post
popularity. Lines 1-6 show how to compute the intermediate representation of text
and image based on hashtags. We apply transformations on text and image feature
matrices using learnable parameters to capture their interactions with hashtags. Here,
Yt ∈ RD×A and Yi ∈ RD×A are the intermediate representation of the text and image
feature matrix based on hashtags, respectively, A is the number of attention units set
to 768, U t ∈ RM ×A, V t ∈ RL×A, U i ∈ RK×A, V i ∈ RL×A are learnable parameters.
The hashtags associated with the post are embedded into a continuous vector space
representation by using BERT.
H = BERT (ph i ) (13)
Here, H ∈ RL×D is the resultant hashtag feature matrix, L=60 based on the maxi-
mum number of hashtags associated with a post. To have a feature matrix of uniform
dimensions across different posts in the data, we padded zeros for posts having a tag
count of less than 60. We employ BERT because one hashtag can have different mean-
ings in different posts. For example, #rock can be used to refer to stones and in other
posts, the same hashtag can refer to music rock band. Therefore, it is important to cap-
ture the context in which a particular hashtag is being used. BERT-based embeddings
of hashtags capture their semantic relationships, allowing the model to understand
their contextual meanings. By introducing learnable parameters associated with the
transformation of text/image features, the model can adaptively learn how to combine
these features with hashtag features to derive meaningful representations. This allows
the model to adapt to the specific characteristics of the content and the nuances of
hashtag usage patterns. The resulting intermediate representations encapsulate not
only the inherent characteristics of the text/image features but also their contextual
relevance concerning the associated hashtags. This semantic enrichment enhances the
model’s ability to understand the underlying themes, topics, and sentiments expressed
15

Algorithm 1 Hashtag-guided Attention
Input: E: Text feature matrix
V : Image Feature Matrix
H: Hashtag Feature Matrix
Output: ˜c: Updated Content Feature Vector
function Hashtag-guided Attention(T, V, H)
1: for all t = 1 to M do
2: Yt[t] = tanh(E[t] × Ut + H × V [t])
3: end for
4: for all i = 1 to K do
5: Yi[i] = tanh(V [i] × Ui + H × V [i])
6: end for
7: for all t = 1 to M do
8: αt[t] = softmax(Yt[t] × Wt)
9: end for
10: for all i = 1 to K do
11: αi[i] = softmax(Yi[i] × Wi)
12: end for
13: for all j = 1 to D do
14: ˜t[j] = P t(E[t][j] × αt[t])
15: end for
16: for all j = 1 to D do
17: ˜i[j] = P i(V [i][j] × αi[i])
18: end for
19: ˜c = ˜i + ˜t
20: return ˜c
in the content, thereby improving the quality of feature representations. These inter-
mediate representations Yt and Yi signify how text and image features are influenced
by associated hashtags. We apply the hyperbolic tangent (tanh) activation function to
a combination of text feature matrix ( E) and hashtag feature matrix ( H) represented
by Yt. Similarly, for image features, we apply tanh to a combination of image feature
matrix (I) and hashtag feature matrix (H) which is denoted by Yi. The intuition here
is to capture the interaction between text and hashtags ( Yt), and image and hashtags
(Yi). Lines 7-12 compute the attention weights for text and image features. Here, αt
and αi denote attention weights for text modality and image modality, respectively.
Here, W t ∈ RA×D, W i ∈ RA×D are learnable parameters. These weights represent
the importance of different features based on the associated hashtags. The idea is that
certain hashtags may be more relevant to either text or image content, affecting their
contribution to the overall content vector. Then, we compute the attended modality
representations. Here, ˜t ∈ RD and ˜i ∈ RD denotes the attended text feature vector and
attended image feature vector, respectively. In Lines 13-15, we take the weighted sum
of text feature matrix (E) with the attention weights αt to get an attended text repre-
sentation ˜t. This step emphasizes the text features that align with relevant hashtags.
16

Similarly, in Lines 16-18, we multiply the image feature matrix I with the attention
weights αi to get an attended image feature vector representation ( ˜i). Here, the focus
is on image features associated with specific hashtags. Line 20 computes the hashtag-
guided content feature vector by taking the sum of the attended text feature vector ˜t
and the attended image feature vector ˜i. Here, ˜c ∈ RD represents the comprehensive
feature vector derived from hashtag guidance. This updated feature vector represents
a comprehensive view of the content, incorporating information from both text and
image modalities, with attention focused on the relevant features guided by hashtags.
By leveraging hashtags as guiding signals, the algorithm enhances the model’s ability
to capture contextually relevant features, ultimately improving the performance of the
model in predicting popularity.
4.3 Feature Fusion
In this section, we delve into the details of feature fusion, a critical step in constructing
a unified representation of multimodal social media posts and ultimately predicting
their popularity within the proposed framework followed by the theoretical background
for feature fusion. Figure 4 depicts the underlying details of the feature fusion compo-
nent which is structured in a grid-like manner, with layers arranged horizontally. Each
layer corresponds to a stage in the data processing conducted by the CNN. During
the feature extraction stage, we extract demographic, sentiment, hashtag, and social
context features from each post denoted by f d i , fst i , fh i , fs i , respectively. Conv1D refers
to a one-dimensional convolutional layer, a common building block in CNNs for pro-
cessing sequential data. Each layer has a box with parameters such as the filter size,
number of filters, and activation function (ReLU). These parameters define how the
layer performs its operations on the data. Dropout layers randomly set a fraction of
activations to zero during training. This helps prevent the network from overfitting
to the training data. After the convolutional layers, there are “Flatten” layers. These
layers flatten the data from a multi-dimensional representation into a one-dimensional
vector suitable for feeding into a fully connected layer.
Following the extraction of social features, we concatenate them into a single
feature vector with a dimensionality of 85. To address potential issues of high dimen-
sionality and redundancy within this feature space, we employ Principal Component
Analysis (PCA) [57]. PCA is a widely recognized method for reducing dimensionality,
wherein the data is projected into a lower-dimensional space to maximize the retained
variance.
PCA is a well-established dimensionality reduction technique that transforms the
data into a lower-dimensional space while maximizing the captured variance. In this
context, we utilize PCA to reduce the dimensionality of the social feature vector from
85 to 6, thereby selecting the most salient features that contribute most significantly to
the prediction task. For demographic features, we obtain a feature vector of dimension
four. As stated above the final hashtag vector has a dimension of 818. The combined
sentiment feature vector derived from hashtags and captions has a dimension of 10. All
feature vectors thus obtained are passed to an individual network consisting of three
CNN layers. The output of all CNNs along with the hashtag-guided content feature
vector is fed into a fusion network. The fusion network is composed of a merged layer
17

Figure 4: Feature Fusion
and a series of several Fully Connected (FC) layers termed Cascade Feed-Forward
Network (CFFN). The output of all CNN networks along with the hashtag-guided
content feature vector are concatenated in the merged layer. The merged layer’s con-
catenated output serves as the input for the CFFN. Ultimately, the output of CFFN
is summed together at the final node, which gives the popularity score for the spe-
cific social media post. Mean Squared Error (MSE) is then calculated using both the
ground truth and forecasted popularity scores. The computed error is backpropagated
and weights are updated accordingly. For each iteration output vectors for the so-
cial feature, demographic feature, hashtag, and sentiment feature are calculated as
illustrated in Equation 14, Equation 15, Equation 16, Equation 17.
Si = Conv 1Ds3(Conv 1Ds2(Conv 1Ds1(f s i ))) (14)
Di = Conv 1Df 3(Conv 1Df 2(Conv 1Df 1(f d i ))) (15)
Hi = Conv 1Dh3(Conv 1Dh2(Conv 1Dh1(f h i ))) (16)
18

Sti = Conv 1Dst3(Conv 1Dst2(Conv 1Dst1(f st i ))) (17)
where i = 1, 2, . . . , N. Here, Si,Di, Hi, and Sti denote the social, demographic, hash-
tag, and sentiment feature vectors obtained after passing through CNN layers. Further,
we have flattened Si, Di, Hi, and Sti and concatenated these feature vectors along
with the hashtag-guided content feature vector (˜c) and denote the final merged vector
as Mi where
Mi = [Si, Fi, Hi, Sti, Ci] (18)
Here, Mi denotes the concatenated feature vector which has a size of 27104.
4.4 Popularity Prediction
We employ a Deep Feedforward Neural Network (DNN) as illustrated in Figure 5,
consisting of 12 fully connected layers (denoted by N ) with decreasing sizes (13552,
6776, 3388, 1694, 847, 424, 212, 106, 53, 27, 13, 1) to forecast the popularity score.
Each hidden layer is followed by a ReLU activation function and a dropout [58] layer
with a rate of 0.2. The output layer utilizes a linear activation function to directly
predict the continuous star count.
Figure 5: Deep Feedforward Neural Network for Popularity Score Prediction
The final popularity score can be calculated as given in Equation 19.
ˆYi = DN N(Mi) (19)
19

Here, ˆYi and Yi are predicted and ground-truth popularity score of post pi, and,
DNN is the Deep Feedforward Neural Network. The training objective is defined
in Equation 20.
M SE(θ) = min
θ

 1
2|P |
|X
i=1
P |( ˆYi − Yi)2

 (20)
Here, |P | is the number of posts in the training data andθ represent the NARRATOR’s
parameters. These are trained via back-propagation by maximizing the Mean Squared
Error (MSE) cost function after being set with random values between -1 and 1.
4.4.1 Theoretical Underpinnings of F eature F usion
The proposed model employs a multi-stage architecture for feature extraction and
fusion:
• Feature Retrieval: Separate Convolutional Neural Networks (CNNs) are employed
to retrieve relevant features from each modality (social context, demographics,
hashtags, sentiment). This allows the model to learn modality-specific patterns.
• Dimensionality Reduction: Techniques such as Principal Component Analysis
(PCA) have been applied to social features to reduce redundancy and improve
computational efficiency while preserving essential information.
• Fusion Network: The retrieved features from each modality are then concatenated
and fed into a Deep Feedforward Neural Network (DNN). This network learns
to integrate the complementary information from different modalities, potentially
revealing latent relationships that contribute to post popularity.
The theoretical foundation of this approach lies in the concept of multimodal repre-
sentation learning. By learning a unified representation that captures the combined
influence of different modalities, the model can potentially achieve superior prediction
performance compared to models that rely on individual modalities.
5 Experimental Evaluations
Following a detailed account of the experimental setup, this section presents a compre-
hensive analysis of the data obtained from the experiments. This analysis will provide
valuable insights into the effectiveness of our proposed approach.
5.1 Experimental Setup
This section details the datasets used in the study and the adopted preprocessing pro-
cedures. We next go through several comparison techniques, which are then followed
by evaluation metrics.
5.1.1 Datasets
In this section, we cover various datasets on which experiments were conducted,
followed by strategies for dataset preprocessing.
20

• SMP: The Social Media Prediction (SMP) [59] is a real-world dataset provided
by ACM Multimedia Grand Challenge in 2019. Initially, the raw data collection
consisted of about 432K posts that were gathered from 135 distinct users’ personal
Flickr albums. In the dataset, each post has a unique picture ID that identifies the
image and a user ID that identifies the person who uploaded it, the date the post was
created, how many comments it received, how many hashtags were used, whether
any users were tagged in the image, number of words in the title and the image
caption. User-centric information such as the average view count, average member
count, and group count were also collected as part of the data. Each image has a
label that reflects its popularity based on the number of log-normalized views.
• TPIC: TPIC2017 [60] is a social media dataset for temporal popularity prediction
that contains 680K photos and accompanying photo-sharing records on Flickr over
a three-year period. The TPIC2017 dataset is diverse, containing photos, user data,
and time information.
Dataset Preprocessing
We preprocess the input data to convert it into an appropriate format to extract
coherent features and accurately predict the popularity of multimodal posts. We apply
several adaptations and normalization techniques to these datasets. To this end, we
have taken all posts that contain hashtags, titles, and faces in the image. This left us
with a total of 21,000 samples in the SMP dataset and 11,000 samples in the TPIC
dataset. For our experiments, 80% of the posts were utilized for training, 10% for
validation, and 10% for testing.
5.1.2 Compared Methods
In this part, we discuss various state-of-the-art methods for assessing the effectiveness
of the suggested framework.
1. Leveraging Hashtag Networks for Multimodal Popularity Prediction of Instagram
Posts (HashPop): Liao et al. [32] has predominantly used hashtags as a separate
modality to gauge the popularity of a specific post. The authors have constructed
a graph-like hashtag network where hashtags used in the post serve as nodes of the
graph. Edges are created between hashtags if many hashtags appear in a single post.
This combined vector is then represented as a hashtag feature. In addition, authors
used InceptionV3 to obtain image embedding, and sentence transformer to obtain
caption embedding for the post along with additional metadata. The overall post-
representation is obtained by concatenating these obtained features. The output
from the last layer is utilized to calculate the popularity score in a dense layer once
this composite representation has been passed through.
2. Multimodal Deep Learning Framework for Image Popularity Prediction on Social
Media (VSCNN): Abousaleh et al. [26] chose social metadata, post metadata, and
time metadata as primary components for predicting post popularity. Low-level,
high-level, and Deep Learning-based visual attributes are extracted from the image
that constitutes a given post. Furthermore, after feature extraction, the authors
employed CNNs on visual and social metadata features independently to learn their
21

high-level representations. At the output layer, shared multimodal properties are
learned and the popularity score is determined. To this end, the output of two
separate CNN networks is then integrated into a shared network which is made up
of one merge layer and two dense layers to predict the popularity of a post.
3. Multimodal Deep Learning for Social Media Popularity Prediction With Attention
Mechanism (MMAtt): Xu et al.[16] provided an attention mechanism for forecast-
ing post popularity. The authors retrieved four distinct features namely categorical,
numerical, visual, and textual. The categorical feature consists of category, sub-
category, and path alias of post embeddings which were obtained and passed to
individual dense layers, the output of which was further passed to the common
dense layer. The numerical information contains the number of followers, the date
the post was created, and the location. The authors applied ResNet50 to extract
visual features which were later sent to a dense layer. The textual features contain
the title and hashtags of the post, and embeddings of both were obtained using
word2vec and were passed to two-layer LSTM and individual dense layers. The
output of all dense layers was concatenated and transferred to a single dense layer,
after which an attention layer was utilized to compute a popularity score.
4. Social Media Popularity Prediction: A Multiple Feature Fusion Approach with Deep
Neural Networks (FuseDNN): Ding et al. [61] retrieved visual, textual, user, tem-
poral, and geographical location features. In visual features, the authors retrieved
ResNet-101 characteristics, an intrinsic popularity score, and an aesthetics score
from the post’s provided image. Tag count, title length, and title embedding using
BERT are all included in text features. While the time component contains the post
duration and the location information provides geographic coordinates, user data
includes the count of followers, followings, and posts. The remaining entities were
concatenated and passed to a different dense layer. The ResNet-101 and BERT
embeddings were passed to separate dense layers. To forecast the popularity score,
the output from all three dense layers was combined and transferred to three dense
layers to yield the predicted popularity score.
5. Predicting Tweet Engagement with Graph Neural Networks (TweetGage): Arazzi
et al. [33] developed a novel Graph Neural Network framework for predicting user
engagement on social media. TweetGage leverages a graph-based model based
on hashtag relationships, capturing semantic connections beyond individual post
features.
6. Gradient Boost Tree Network based on Extensive Feature Analysis for Popular-
ity Prediction of Social Posts (MFTM): Hsu et al. [62] presented a multi-modality
feature mining framework for social media popularity prediction. It leverages
identity-related user features alongside traditional modalities (text and image) to
achieve significant performance improvements, suggesting a stronger influence of
identity compared to other user metadata. LightGBM and TabNet are employed
to capture complex relationships within the enriched feature set.
7. Enhanced CatBoost with Stacking Features for Social Media Prediction (ECSF):
Mao et al.[63] proposed a novel social post popularity prediction approach utilizing
enriched post and user features. ECSF employs innovative stacking features to cap-
ture higher-order interactions between text and image features, potentially leading
22

to a more comprehensive understanding of the underlying factors that influence
social media post popularity. ECSF’s effectiveness is substantiated by its state-of-
the-art performance on the SMP challenge dataset, surpassing prior methods that
primarily relied on extracting lower-order features.
5.1.3 Evaluation Metrics
In this study, we adopted Mean Squared Error (MSE) and Mean Absolute Error
(MAE) as the primary metrics to quantify the prediction accuracy of our model.
• MSE: To determine the mean of the squared sum of prediction errors, MSE is
frequently used. Each prediction error represents the discrepancy between a data
point’s actual value and the value estimated by a regression model. It is simpler to
determine the gradient of MSE since it has straightforward mathematical features.
Due to its computational simplicity, smooth differentiability, and greater optimiza-
tion amenability, MSE is typically supplied as the default measure for the majority
of predictive models. A serious flaw with MSE is that it squares large prediction
errors, which strongly penalizes them. Due to the quadratic accumulation of each
MSE error, the overall error is significantly influenced by outliers in data. This
demonstrates that MSE undervalues the model’s performance because of its high
sensitivity to outliers and the disproportionate weight assigned to their effects, MSE
undervalues the model’s performance in this case. When outliers are present in
the data, only then the disadvantage of MSE becomes obvious, making MAE an
adequate replacement. MSE is defined as given in Equation 21.
M SE= 1 |N |
NX
i=1
(yi − ˆyi)2 (21)
Here, N denotes the total number of posts, ˆ yi denotes the predicted popularity
score, and yi denotes the actual popularity score of the ith multimodal post ( pi).
• MAE: MAE is a straightforward metric typically used to assess the precision of a
regression model. It calculates the mean absolute value of each prediction mistake
made by the model overall test set samples. Unlike metrics sensitive to outliers, MAE
assigns equal weight to all prediction errors. This characteristic ensures that larger
deviations from the actual values contribute linearly to the overall error score. How-
ever, MAE focuses solely on the absolute magnitude of the error, without considering
the direction of the discrepancy (overprediction or underprediction). Consequently,
MAE provides an objective measure of the model’s overall performance in terms
of absolute prediction error, but it doesn’t necessarily indicate whether the model
consistently overestimates or underestimates the target variable. By employing the
absolute value of the prediction error rather than its squared value, MAE becomes
more resilient to outliers than MSE because it does not penalize significant errors
as heavily as MSE. Therefore, MAE has both benefits and drawbacks. While it
helps in managing outliers, it does not penalize significant forecasting errors. MAE
is described in Equation 22.
23

M AE= 1 |N |
NX
i=1
|yi − ˆyi| (22)
Here, N denotes the total number of posts, ˆyi denotes the predicted popularity score,
and yi denotes the actual popularity score of the ith multimodal post ( pi).
5.2 Experimental Results
The experimental results for the proposed and current state-of-the-art approaches
on various datasets, ablation investigations, visualization of predictions from both
existing and proposed methods, statistical analysis, ranking of important features,
implementation details, and limitations are all covered in this section.
5.2.1 Effectiveness Comparison
To assess the performance of our suggested technique on various datasets, we compare
it to the existing methods on TPIC and SMP datasets. The performance comparison
T able 1: Effectiveness Comparison Results on Different Datasets
Methods TPIC SMP
MSE MAE MSE MAE
FuseDNN, Dinget al.’19 2.716 1.318 4.831 1.707
MMAtt, Xu et al.’20 2.367 1.170 4.447 1.617
VSCNN, Abousaleh et al.’20 1.711 1.015 5.023 1.732
HashPop, Liao et al.’22 3.200 1.435 6.262 1.946
TweetGage, Arazziet al.’23 2.132 1.145 4.211 1.566
MFTM, Hsu et al.’23 5.264 1.946 6.815 2.097
ECSF, Mao et al.’23 5.115 1.911 6.783 2.072
NARRA TOR 1.196 0.854 2.022 0.972
MSE: Mean Squared Error, MAE: Mean Average Error
using the aforementioned datasets is given in Table 1. It is evident from Table 1
that our suggested model, NARRATOR, performs noticeably better than state-of-
the-art methods. NARRATOR beats HashPop with a 62.625% improvement in MSE
and 40.487% in MAE on the TPIC dataset and 67.709% improvement in MSE and
50.051% in MAE on the SMP dataset. The authors in HashPop have focused more
on using the hashtag network besides content-based and metadata information. Our
proposed model which consists of demographic and sentiment information embedded
in captions and hashtags along with hashtag-guided attention content features beats
HashPop. NARRATOR beats VSCNN with a relative improvement of 30.099% in
terms of MSE and 15.862% in terms of MAE on the TPIC dataset and 59.745% in MSE
and 78.189% in MAE on the SMP Dataset. VSCNN predicted popularity based on
social and visual features whereas in our model we have incorporated four additional
features namely demographic information, hashtag, textual, sentiment of caption, and
hashtags besides a hashtag-guided attention mechanism employed on content-based
features. NARRATOR beats MMAtt with a relative improvement of 49.471% in MSE
24

and 27.008% in MAE on the TPIC dataset and 54.531% in MSE and 39.888% in
MAE on the SMP dataset. While the authors incorporated an attention mechanism
within their model, NARRATOR achieves demonstrably stronger performance. This
improvement can be attributed to our implementation of a hashtag-guided attention
mechanism that models the influence of hashtags on linguistic and visual features. Our
attention mechanism produces superior results because the hashtags are very closely
related to the title and the image associated with the post, which in turn boosts
the model’s performance significantly. The proposed model beats FuseDNN exhibiting
a relative improvement of 55.964% and 35.204% in MSE and MAE on the TPIC
dataset and 58.145% improvement in MSE and 43.057% in MAE on the SMP dataset.
NARRATOR surpasses TweetGage exhibiting a relative improvement of 43.092% and
25.415% in terms of MSE and MAE on the TPIC dataset and 51.982% improvement in
terms of MSE and 37.931% in terms of MAE on the SMP dataset. Unlike TweetGage
which captures relationships among posts based on common hashtags, we employ the
topical, structural, semantic, and sentiment information from hashtags besides image,
caption, and demographics. The proposed model beats MFTM exhibiting a relative
improvement of 77.279% and 56.115% in terms of MSE and MAE on the TPIC dataset
and 70.330% improvement in terms of MSE and 53.648% in terms of MAE on the
SMP dataset. After feature extraction, MFTM employs an ensemble of TabNet and
LightGBM which are Machine Learning models to predict post popularity whereas
NARRATOR employs a hashtag-guided attention mechanism on content features and
a a deep neural network to forecast the post popularity. NARRATOR surpasses ECSF
by a relative improvement of 76.617% in MSE and 55.311% in MAE on the TPIC
dataset and 70.190% improvement in MSE and 53.088% in MAE on the SMP dataset.
ECSF relies on feature stacking and a CatBoost model for prediction, which limits
its ability to capture complex relationships between features. NARRATOR’s deep
neural network with a hashtag-guided attention mechanism overcomes this limitation
by learning more intricate feature interactions.
Figure 6: Effectiveness Comparison Curves on TPIC Dataset
25

As illustrated in Figure 6 and Figure 7, NARRATOR demonstrates superior per-
formance compared to all four baseline models on both datasets. This is evident in the
consistently lower MSE and MAE values achieved by NARRATOR. Notably, on the
TPIC dataset, NARRATOR achieves the lowest MSE of 1.196 and the lowest MAE
of 0.854. Similarly, on the SMP dataset, NARRATOR outperforms other models with
an MSE of 2.022 and an MAE of 0.972. These results suggest that NARRATOR effec-
tively captures the underlying factors influencing social media post popularity across
different datasets.
Figure 7: Performance Comparison Curves on SMP Dataset
This implies that our derived features, such as sentiments, demographics, and
hashtags, are essential for determining how popular social media posts are. The fact
that hashtags influence both textual and visual content features and enrich the overall
representation of the posts in predicting post popularity on social network platforms
is another important result.
5.2.2 Ablation Studies
In this section, we discuss the model’s performance by analyzing feature combinations,
and the effectiveness of different attention mechanisms on the performance of the
proposed model.
Feature Ablation
We investigate the role of our two novel features- visual demographics and sentiment
extracted from hashtags in enhancing popularity prediction. Table 2 demonstrates
that the complete NARRATOR model, incorporating both novel features- visual de-
mographics and sentiment extracted from hashtags, achieves superior performance
compared to ablated versions. The complete model achieves the lowest MSE and MAE
values across both TPIC and SMP datasets, highlighting the significant contribution
of these features to accurate popularity prediction. This degradation is particularly
26

T able 2: Feature Ablation Study
V ariant TPIC SMP
MSE MAE MSE MAE
NARRATOR w/o (Sentiment from Hashtags+ Demographics) 1.387 0.912 2.367 1.084
NARRATOR w/o Sentiment from Hashtags 1.372 0.872 2.346 1.092
NARRATOR w/o Demographics 1.238 0.897 2.465 1.131
NARRA TOR 1.196 0.854 2.022 0.972
MSE: Mean Squared Error, MAE: Mean Average Error
pronounced when both features are removed simultaneously, resulting in an absolute
increase of 13.77% and 6.36% in MSE and MAE on TPIC, and 14.58% and 10.33%
on SMP, respectively. Removing demographics and sentiment features from hashtags
affects the model’s ability to understand the target audience and the emotional tone
of the post, both of which could be relevant for popularity. The exclusion of visual
demographics leads to an absolute increase of 3.39%, 4.79% in MSE and MAE on
TPIC and 17.97% and 14.06% in MSE and MAE on SMP dataset, respectively. This
highlights the importance of understanding the target audience. Visual demographics
provide insights into the age group, gender, and other visual cues that may resonate
with specific user segments, enabling the model to better predict post appeal. The ex-
clusion of sentiments from hashtags leads to an absolute increase of 12.83%, 2.06% in
MSE and MAE on TPIC and 13.81% and 10.99% in MSE and MAE on SMP dataset,
respectively. This emphasizes the role of emotional tone in driving post popularity.
Hashtags often encapsulate the sentiment or theme associated with a post. By incor-
porating hashtag sentiment, the model can gauge the emotional appeal of the content,
which is a key factor influencing user engagement and sharing behavior. In essence, vi-
sual demographics help the model understand who the content might appeal to, while
hashtag sentiment helps understand how the content might make the audience feel.
By integrating both, NARRATOR gains a more comprehensive understanding of the
factors driving popularity, enabling it to make more accurate predictions. This under-
scores the synergistic effect of combining visual demographics and hashtag sentiment
for understanding and predicting multimodal post popularity.
Attention Mechanisms
To demonstrate the significance of the novel hashtag-guided attention mechanism,
we compare its performance with various attention mechanisms discussed below.
Table 3 showcases the performance of NARRATOR with different attention mecha-
nisms. Here, the variants that use no attention, self-attention, cross-attention, parallel
co-attention, and hashtag-guided attention are N ARRAT ORN A, N ARRAT ORSA,
N ARRAT ORCA, N ARRAT ORP A, N ARRAT ORHGA respectively. The perfor-
mance difference when NARRATOR is implemented without any attention mechanism
is 23.68% and 9.53% in MSE and MAE on the TPIC dataset and 41.80% and 32.73%
on the SMP dataset compared to hashtag-guided attention. The performance of NAR-
RATOR is the lowest in the absence of any attention mechanism. Compared to
self-attention, hashtag-guided attention shows and absolute improvement of 23.68%,
9.53% in MSE and MAE on TPIC dataset and 41.80% and 32.73% on SMP dataset.
27

T able 3: Effectiveness of Attention Mechanisms
Attention T echnique TPIC SMP
MSE MAE MSE MAE
N ARRAT ORN A 1.510 0.917 3.715 1.417
N ARRAT ORSA 1.567 0.944 3.474 1.445
N ARRAT ORCA 1.486 0.916 2.904 1.218
N ARRAT ORP A 1.389 0.905 3.367 1.359
N ARRAT ORHGA 1.196 0.854 2.022 0.972
MSE: Mean Squared Error, MAE: Mean Average Error
The superior performance of hashtag-guided attention over self-attention indicates
that solely modeling intra-modal relationships (within text or image) is less effective
than incorporating the semantic context provided by hashtags. Compared to cross-
attention, hashtag-guided attention shows and absolute improvement of 19.52%, 6.77%
in MSE and MAE on TPIC dataset and 30.37% and 20.20% on SMP dataset. While
cross-attention improves performance by modeling inter-modal interactions (between
text and image), hashtag-guided attention further refines this by leveraging the con-
textual cues embedded in hashtags, leading to a better understanding of content. Our
hashtag-guided attention mechanism outperforms parallel co-attention, demonstrating
an absolute improvement of 13.89% and 56.35% on TPIC and 39.95% and 39.81% on
SMP in terms of MSE and MAE metrics, respectively. Unlike the parallel co-attention
mechanism that solely focuses on the relationship between text and image features,
the proposed hashtag-guided attention mechanism introduces a crucial element: the
influence of hashtags on both modalities. The superior performance of hashtag-guided
attention compared to parallel co-attention emphasizes the value of explicitly incor-
porating hashtag semantics into the attention mechanism. Hashtags provide a bridge
between textual and visual content, allowing the model to focus on the most relevant
aspects of both modalities for popularity prediction.
Advantages of Hashtag-Guided Attention
Hashtag-guided attention utilizes hashtag embeddings to guide the model’s focus to-
wards features in both text and images that align semantically with the hashtags. This
targeted approach allows the model to:
1. Grasp the intended meaning and purpose of the post, as hashtags often encapsulate
the core message.
2. Bridge contextual gaps, going beyond literal content to interpret nuances that
contribute to popularity.
By combining content analysis with hashtag-driven context, our approach achieves a
more holistic understanding of social media posts, leading to more accurate popularity
predictions.
28

5.2.3 Qualitative Analysis
Predicting the popularity score of the given post is a common evaluation protocol
in popularity prediction tasks. This section presents a qualitative evaluation aimed
at understanding how accurately our proposed model predicts the popularity of so-
cial media posts. Example posts with accompanying captions, images, and associated
hashtags are illustrated. We also display the ground-truth popularity scores and pop-
ularity scores predicted by state-of-the-art methods. These example posts have been
chosen randomly from test data. As can be seen in Figure 8a, our proposed model
(a) Post 1
 (b) Post 2
Figure 8: Posts Depicting Popularity Scores Predicted by Different Methods
predicts a popularity score that is very close to the ground-truth popularity score.
The caption of the first example post i.e., “Holi festival in Madrid”, bears a striking
resemblance to the accompanying image, which depicts a girl celebrating the festival.
Hashtags such as #holi and #spain indicate a cultural celebration happening outside
its traditional location (India), #india and #bollywood suggest the post might target
the Indian diaspora or Bollywood fans in Spain. The model focuses on visual features
in the image related to the Holi celebration (colors, people celebrating). Textual fea-
tures in the caption (“Holi festival”) are analyzed alongside hashtags such as #india
to understand the cultural significance. Hashtags such as #spain and #bollymadrid
help identify a potential audience interested in Indian culture or Bollywood within
Spain. By considering these contextual cues from hashtags, the model refines its under-
standing of the post’s content and target audience. This validates our hypothesis that
modeling the interaction between the title and image under the influence of hashtags
via a hashtag-guided attention mechanism effectively captured the relevant aspects for
29

predicting engagement and considerably enhanced the model’s performance. Further-
more, our experimental results show that sentiments are related to post popularity.
The hashtags #holi and #india are directly related to the post caption as Holi is
the festival of colors that celebrates spring and the triumph of good over evil in In-
dia and is associated with joy, love, and new beginnings. Hashtag “#bollymadrid”
combines Bollywood with Madrid, suggesting a fusion of Indian and Spanish culture,
which can be seen as positive. Overall, the post promotes a positive and inclusive sen-
timent about cultural exchange. The positive mood communicated by captions and
hashtags aids the model in anticipating better outcomes. Further, as illustrated in
Figure Figure 8b, the ground-truth popularity score for the post is 1.6. Our model’s
prediction closely approximates this value, achieving a score of 1.580. Overall, this re-
search helps to visualize our model’s ability to estimate post popularity accurately by
leveraging innovative features.
5.2.4 Statistical Analysis
This section explores the statistical relationship between NARRATOR’s predictions
and real-world content popularity using two established correlation coefficients: Spear-
man’s Rank Correlation Coefficient (SRCC) and Pearson Correlation Coefficient
(PCC). To evaluate the NARRATOR’s effectiveness, we calculated correlation coeffi-
cients based on predictions by NARRATOR and the ground-truth popularity scores
of posts in TPIC and SMP datasets. Our analysis yielded significant correlations, vi-
(a) Correlation on TPIC Dataset
 (b) Correlation on SMP Dataset
Figure 9: Statistical Analysis
sually depicted in the scatterplots of Figure 9. Here, proximity to a straight diagonal
line signifies a robust correlation (shown in red). As can be seen from Figure 9, the
SRCC values were found to be 0.885 and 0.8773, while the PCC values were com-
puted as 0.8355 and 0.8409 for TPIC and SMP datasets, respectively. Moreover, the
calculated p-values for these correlations were determined to be highly significant
(p ≤ 0.05), affirming the robustness of the observed relationships between predicted
and actual popularity levels across social media platforms. In summary, our research
demonstrates the efficacy of NARRATOR in accurately forecasting the popularity of
30

multimodal content, as evidenced by strong correlations established through rigorous
statistical analyses conducted on real-world TPIC and SMP datasets. These findings
have implications for various fields, including content marketing, audience engagement
strategies, and social media analytics.
5.2.5 F eature Correlation Analysis
To investigate the influence of individual features on predicting post popularity, we
calculated Spearman’s Rank Correlation Coefficient (Spearman’s Rho) [64] with the
popularity score. The results for the TPIC and SMP datasets are shown in Table 4.
T able 4: Spearman’s Rank Correlation of Features with
Popularity Scores
F eature SRCC (TPIC) SRCC (SMP)
Post Id -0.529 -0.244
User Id -0.097 -0.319
Title length 0.3999 0.018
Description Length 0.552 -
Tagcount 0.458 0.446
Avgview 0.778 -
Groupcount 0.473 -
Avgmembercount 0.319 -
Postday -0.066 0.042
Posttime 0.263 -0.008
Postmonth -0.112 -0.074
Hashtags 0.402 0.237
Sentiment 0.429 0.117
Demographic Features 0.225 0.095
Our derived features i.e., sentiment, hashtags, and demographic features exhibit a pos-
itive correlation on both datasets. On the TPIC dataset, the post id has the highest
negative correlation and average views (avgview) has the highest positive correlation,
whereas the user id has the highest negative correlation, and tag count has the highest
positive correlation on the SMP dataset. However, correlation does not imply cau-
sation, and it might miss non-linear relationships. The drawback Spearman’s rank
correlation coefficient can only detect monotonic relationships and is not suitable for
non-linear relationships.
5.2.6 F eature Ranking and Importance
To assess the importance of derived features, we independently ranked the perfor-
mance of each feature in terms of Mean Squared Error (MSE) and the Mean Absolute
Error (MAE), with a higher rank of 1 indicating optimal performance. Following that,
by aggregating the preliminary ranks acquired for each parameter, the resulting av-
erage rank was used as a comprehensive assessment of overall performance. Table 5
highlights the significance of both established and newly introduced features in pre-
dicting post popularity. While certain features such as social information and hashtags
31

T able 5: Feature Ranking and Importance
F eature TPIC SMP
MSE/MAE Rank MSE / MAE Rank
w/o Sentiment (Text) 1 .362(5)/0.867(6) 5.5 2 .367(5)/ 1.084(6) 5.5
w/o Sentiment (Hashtags) 4.51 .372(4)/0.872(5) 4.5 2 .346(6)/ 1.092(5) 5.5
w/o Hashtags 2 .553(1) / 1.251(1) 1 2 .458(4) / 1.125(4) 4
w/o Demographics 1 .238(6) / 0.897(4) 5 2 .465(3) /1.131(3) 3
w/o Social 2 .166(2) / 1.093(2) 2 2 .897(2)/1.267(1) 1.5
w/o Content 1 .435(3) / 0.908(3) 3 3 .021(1)/1.228(2) 1.5
MSE: Mean Squared Error, MAE: Mean Average Error
consistently rank high across both datasets, showcasing their fundamental role in
capturing engagement and contextual information, respectively, the impact of other
features such as sentiment and visual demographics appears to be more nuanced and
context-dependent. The relatively lower individual ranks of the newly introduced fea-
tures (sentiments from hashtags and visual demographics) might not fully reflect their
true value. Their strength lies in their synergistic contribution to the overall model,
capturing subtle nuances and previously overlooked aspects of popularity dynamics. In
particular, they address specific gaps in prior research, offering a more comprehensive
understanding of the factors influencing post popularity. Furthermore, the importance
of features can vary depending on the specific platform and its user base. While some
features might be universally influential, others might play a more significant role in
specific contexts or for particular types of posts. Our analysis underscores the complex
and multifaceted nature of popularity prediction, highlighting the need for a holistic
approach that considers a diverse range of features and their interactions.
5.2.7 Implementation Details
The experiments leveraged a high-performance computing environment featuring a
Linux server architecture. The server’s processing power included an Intel(R) Xeon(R)
Silver 4215R CPU operating at 3.20 GHz, complemented by 256 GB of RAM and
a dedicated NVIDIA Tesla T4 GPU with 16 GB of memory. This configuration
facilitated efficient model training and experimentation. To achieve optimal model per-
formance, a rigorous hyperparameter tuning process was conducted. The learning rate
was meticulously set to 0.0001, ensuring convergence without excessive learning speed.
A batch size of 20 was chosen to strike a balance between computational efficiency
and gradient estimation accuracy. The Adam optimizer, renowned for its adaptive
learning rate capabilities, was employed to facilitate efficient optimization. Training
proceeded for a maximum of 30 epochs, incorporating an early stopping mechanism
with a patience of 5 epochs to prevent overfitting. Additionally, a dropout rate of 0.2
was strategically applied after each layer within the model architecture to further mit-
igate overfitting tendencies. To ensure a level playing field for performance evaluation,
the embedding dimension (D) was consistently set to 768 for all comparative methods
employed in the study. Before feeding image data into the VGG-19 network, all image
samples underwent a standardized pre-processing step. This step involved rescaling
32

each image to a uniform size of 224 x 224 pixels. This normalization ensured consistent
image representation and facilitated network training. In Deep Feed Forward Network,
we employ a series of 12 fully connected layers of size 13552, 6776, and so on till size 1.
5.2.8 Computational Cost Analysis
To assess the cost implications of our proposed model, NARRATOR, we investigated
its runtime and scalability. The training and inference time taken by different methods
T able 6: Computational Time Analysis
Methods TPIC SMP
T raining Inference T raining Inference
FuseDNN, Ding et al.’19 2 1 3 0.5
MMAtt, Xu et al.’20 38 1 85 2
VSCNN, Abousaleh et al.’20 7 1 23 2
HashPop, Liao et al.’22 11 1 21 2
TweetGage, Arazziet al.’23 88 17 188 62
MFTM, Hsu et al.’23 6.5 2.5 7 3
ECSF, Mao et al.’23 1.5 0.01 17 1
NARRA TOR 81 5 175 14
as listed in Table 6 is reported in seconds. As can be seen from Table 6, NARRA-
TOR’s training time is notably higher than the state-of-the-art methods due to the
complexity of handling multiple modalities and the substantial number of trainable
parameters. However, it is worth noting that its inference time is significantly faster
than a recent state-of-the-art method, TweetGage [33]. This observation is atttibuted
to the complexity of handling multiple modalities and the substantial number of train-
able parameters in NARRATOR. Specifically, training on the TPIC dataset takes 81
seconds per epoch and increases to 175 seconds per epoch for the SMP dataset. In
contrast, inference takes 5 seconds and 14 seconds per epoch for TPIC and SMP
datasets, respectively. This suggests the model is capable of real-time or near-real-time
predictions, a critical factor for many practical applications. NARRATOR’s complex-
ity is underscored by its memory footprint. With 34,903,017 trainable parameters, it
occupies 133.14 MB of memory, highlighting its capacity to capture intricate patterns
from multimodal data. Although NARRATOR incurs a higher computational cost
compared to simpler baselines, its superior performance in predicting social media post
popularity justifies the trade-off. The model’s ability to leverage diverse modalities, in-
cluding user demographics, sentiment analysis, and hashtag-guided attention, enables
it to capture subtle nuances that contribute to post engagement. Future work could
explore optimizations to enhance NARRATOR’s computational efficiency without
compromising its predictive accuracy, further broadening its applicability.
6 Discussion
This section delves into analysis of PCA on social features, comparison of novel
hashtag-guided attention with parallel co-attention mechanism. Further, we discuss the
33

limitations of NARRATOR and its broader significance, encompassing both theoretical
and practical implications.
6.1 Analysis of PCA on Social Features
A simple technique such as PCA might seem out of place alongside the complex
multimodal feature processing in our approach. However, feature extraction and di-
mensionality reduction are not contradictory but rather complementary steps. We
first extract a rich set of features to capture the diverse aspects of the data, then use
PCA to create a more manageable and efficient representation for the model. The
motivation behind applying PCA was twofold:
1. Managing High Dimensionality: The extracted social features can be numerous,
and some may introduce noise. PCA helps identify and retain the most important
features while mitigating noise and reducing computational complexity.
2. Reducing Model Complexity: Applying PCA to social features significantly de-
creases the total number of trainable parameters from 197,268,457 to 34,903,017,
and the memory usage from 752.52 MB to 133.14 MB. This reduction enhances the
model’s efficiency and scalability, crucial factors for real-world applications.
While PCA is a relatively simple technique, our empirical results demonstrate its effec-
tiveness in this context. To further validate this, we conducted experiments comparing
the performance of NARRATOR with and without PCA applied to social features.
The results, presented below, show that while removing PCA leads to a slight de-
crease in performance and provides the benefits of reduced dimensionality and fewer
trainable parameters. Furthermore, we conducted experiments by removing social
T able 7: Analysis of Dimensionality Reduction on PCA
V ariant TPIC SMP
MSE MAE MSE MAE
NARRATOR w/o PCA on Social 1.495 0.913 2.616 1.267
NARRATOR with PCA on Social 1.196 0.854 2.022 0.972
NARRATOR w/o Social 2.166 1.093 2.897 1.267
NARRATOR with Social 1.196 0.854 2.022 0.972
features to investigate their importance. our ablation study results show a signifi-
cant drop in performance when social features are discarded, as shown in Table 7
underscores their valuable contribution to capturing the social context and dynam-
ics that influence content popularity. In conclusion, PCA strikes a suitable balance
between dimensionality reduction, information preservation, and model complexity.
While we acknowledge the potential of exploring alternative dimensionality reduction
techniques in future work, our current approach effectively leverages social features
while maintaining computational efficiency.
34

6.2 Comparison with Parallel Co-attention
In social media popularity prediction, understanding the interplay between various
modalities is crucial, and while both hashtag-guided attention and parallel co-attention
address this, they differ in how they incorporate contextual information. Our proposed
(a) Parallel Co-attention Mechanism
 (b) Hashtag-guided Attention
Mechanism (Proposed)
Figure 10: Comparative Analysis of Attention Mechanisms
hashtag-guided attention mechanism, illustrated in Figure 10, draws inspiration from
parallel co-attention but introduces a key innovation: the explicit utilization of hash-
tags as an additional source of context to compute attention weights. We recognize
that the popularity of a post is not solely determined by its intrinsic content (text
and images), but also by the broader social context in which it is shared, as conveyed
through hashtags. By mathematically integrating hashtag embeddings into the atten-
tion computation, our mechanism dynamically weighs features from both textual and
visual modalities based on the contextual cues provided by the hashtags. This approach
fills a research gap by directly addressing the limitation of existing attention mecha-
nisms, including parallel co-attention [25], which primarily focus on intrinsic content
features and overlook the rich contextual cues offered by hashtags. By incorporating
hashtag information, our mechanism guides attention and enhances feature selection,
leading to improved prediction accuracy and interpretability. While the core concept
of attention is not new, our specific implementation and integration of hashtag guid-
ance into the attention mechanism represent a methodological innovation. We have
carefully designed the algorithm to capture the complex interplay between hashtags,
textual content, and visual content, resulting in a more effective and context-aware
model. The key advantages of hashtag-guided attention are discussed below:
• Explicit Contextualization: Directly incorporates the semantic and contextual in-
formation encoded in hashtags, enhancing the model’s understanding of the post’s
intended audience and relevance to trending topics.
35

• Dynamic Adaptation: Allows the model to adapt its focus based on the specific
hashtags associated with the post, making it more versatile for diverse content types
and social media platforms.
• Interpretability: Provides insights into how hashtags influence feature selection,
offering greater transparency into the factors driving popularity predictions.
In contrast, parallel co-attention primarily focuses on capturing the interplay between
textual and visual modalities within the post itself. It learns to align and weigh features
from both modalities to generate a more holistic representation of the content. While
valuable for understanding the intrinsic relationship between text and images, parallel
co-attention neglects the broader social context provided by hashtags, which serve as
crucial signals of the creator’s intent, the target audience, and the current trends. As
shown in Table 3, our hashtag-guided attention mechanism outperforms parallel co-
attention, demonstrating an absolute improvement of 13.89% and 56.35% on TPIC
and 39.95% and 39.81% on SMP in terms of MSE and MAE metrics, respectively. This
highlights the effectiveness of incorporating hashtag information into the attention
mechanism for improved popularity prediction. Both hashtag-guided attention and
parallel co-attention contribute to a richer understanding of multimodal social media
posts. However, by explicitly incorporating and mathematically integrating hashtag
information into the attention computation, our hashtag-guided attention mechanism
provides a more context-aware and adaptable approach, leading to more accurate and
interpretable popularity predictions.
6.3 Limitations and Future Work
While NARRATOR exhibits several strengths, it is essential to acknowledge its limi-
tations. The model’s performance is inherently dependent on the quality and diversity
of the training data. In scenarios where the training data is biased, incomplete, or fails
to adequately represent the target population or specific social media platform, NAR-
RATOR’s predictions may exhibit biases. The accuracy of demographic information
derived from faces in images may be compromised by factors such as image resolution,
lighting conditions, image noise, and occlusions. Low-quality images or images with
obscured faces may lead to inaccurate demographic predictions. Although NARRA-
TOR demonstrates improved performance on real-world datasets, its applicability to
other domains has yet to be explored. Cultural disparities, language variations, and
platform-specific trends are all potential influences on the model’s performance.
6.4 Significance
Accurately predicting online content popularity early on holds both theoretical and
practical significance across various domains. To showcase the importance of popular-
ity prediction and the capabilities of NARRATOR, we will delve into its theoretical
implications and explore its potential real-world applications.
36

6.4.1 Theoretical Implications
NARRATOR’s innovative approach to multimodal popularity prediction offers several
key theoretical contributions, enhancing our understanding of content dynamics and
user engagement on social media platforms.
1. Enhanced Understanding of Multimodal Content: NARRATOR’s integration of
visual demographics, analysing sentiments of hashtags, and hashtag-guided at-
tention offers a better understanding of how different modalities (text, images,
hashtags) interact to influence post popularity. This contributes to the theoretical
understanding of multimodal content processing and its impact on user engagement.
2. Context-Aware Feature Selection: The hashtag-guided attention mechanism
demonstrates the importance of incorporating contextual cues for effective feature
selection in multimodal data. This highlights the limitations of traditional attention
mechanisms that solely focus on intrinsic content features and opens new avenues
for research into context-aware deep learning methods and techniques.
3. Role of Hashtag Sentiment in Popularity Prediction: NARRATOR’s explicit incor-
poration of sentiment analysis from hashtags underscores their significance beyond
mere metadata. By demonstrating the impact of hashtag sentiment on understand-
ing audience perception and predicting post popularity, this research contributes to
the theoretical understanding of how emotions expressed through hashtags shape
online discourse and user engagement.
6.4.2 Practical Implications
As discussed below, the practical implications of NARRATOR in multimodal popu-
larity prediction are far-reaching, revolutionizing how individuals interact with social
media platforms.
1. Improved Content Recommendation and Targeted Advertising: NARRATOR’s
ability to accurately predict popularity can enable social media platforms to rec-
ommend content that is more likely to resonate with individual users, leading
to increased user engagement and satisfaction. Similarly, advertisers can benefit
from more targeted ad placements based on predicted popularity and audience
demographics.
2. Trend Detection and Analysis: NARRATOR’s ability to analyze sentiment of hash-
tags, visual demographics and content-based features in conjunction with hashtag
context can help researchers and marketers identify emerging trends, understand
audience preferences, and track shifts in public opinion.
3. Enhanced User Experience: By facilitating the discovery of relevant and engaging
content, NARRATOR can help mitigate information overload and enhance the
overall user experience on social media platforms.
4. Combating Misinformation: The ability to predict the popularity of content early
on can enable platform managers to proactively identify and address the spread of
misinformation or harmful content.
37

7 Conclusion
In this paper, we propose a novel paradigm for forecasting the popularity of social
media posts by leveraging multimodal characteristics. Our approach leverages a mul-
tifaceted feature extraction process, capturing content-based information from both
text and visuals, sentiment-oriented information from hashtags and text, user demo-
graphics, and social network data, along with topical and structural characteristics
derived from hashtags. We propose a novel hashtag-guided attention mechanism that
captures the influence of hashtags on both visual and textual content. This mechanism
facilitates the model in learning the relative importance of different image regions and
text segments based on their association with hashtags, leading to a more nuanced
understanding of how hashtags shape user engagement. To demonstrate the efficacy
of our proposed method, we undertake quantitative and qualitative comparisons in
addition to ablation and statistical investigations. Our method achieves significant
performance improvements compared to existing state-of-the-art approaches, as eval-
uated on two real-world datasets. This finding suggests the potential effectiveness of
our proposed method for predicting the popularity of multimodal posts.
Declarations
Competing interests
The authors declare that they have no known competing financial interests or personal
relationships that could have appeared to influence the work reported in this paper.
Availability of data and materials
Data will be made available on request.
References
[1] Shen, F., Xia, C., Skoric, M.: Examining the roles of social media and alternative
media in social movement participation: A study of hong kong’s umbrella move-
ment. Telematics and Informatics 47, 101303 (2020) https://doi.org/10.1016/j.
tele.2019.101303
[2] Anderson, M., Brook, A.: Social Media Use in 2021 — Pew Research Center
(2021)
[3] Cao, Q., Shen, H., Gao, J., Wei, B., Cheng, X.: Popularity prediction on so-
cial platforms with coupled graph neural networks. In: Proceedings of the 13th
International Conference on Web Search and Data Mining, pp. 70–78 (2020).
https://doi.org/10.1145/3336191.3371834
[4] Wu, B., Mei, T., Cheng, W.-H., Zhang, Y.: Unfolding temporal dynamics: Pre-
dicting social media popularity using multi-scale temporal decomposition. In:
38

Proceedings of the AAAI Conference on Artificial Intelligence, vol. 30 (2016).
https://doi.org/10.1609/aaai.v30i1.9970
[5] Gon¸ calves, M.A., Almeida, J.M., Santos, L.G., Laender, A.H., Almeida, V.: On
popularity in the blogosphere. IEEE Internet Computing 14(3), 42–49 (2010)
https://doi.org/10.1109/MIC.2010.73
[6] Majid, A., Chen, L., Chen, G., Mirza, H.T., Hussain, I., Woodward, J.: A context-
aware personalized travel recommendation system based on geotagged social
media data mining. International Journal of Geographical Information Science
27(4), 662–684 (2013) https://doi.org/10.1080/13658816.2012.696649
[7] Li, C., Lu, Y., Mei, Q., Wang, D., Pandey, S.: Click-through prediction for adver-
tising in twitter timeline. In: Proceedings of the 21th ACM SIGKDD International
Conference on Knowledge Discovery and Data Mining, pp. 1959–1968 (2015).
https://doi.org/10.1145/2783258.2788582
[8] Aven, B.L., Burgess, D.A., Haynes, J.F., Merino, J.R., Moore, P.C.: Using product
and social network data to improve online advertising. Google Patents. US Patent
8,843,406 (2014)
[9] Roy, S.D., Mei, T., Zeng, W., Li, S.: Towards cross-domain learning for social
video popularity prediction. IEEE Transactions on multimedia 15(6), 1255–1267
(2013) https://doi.org/10.1109/TMM.2013.2265079
[10] Gan, C., Sun, C., Duan, L., Gong, B.: Webly-supervised video recognition by
mutually voting for relevant web images and web video frames. In: Computer
Vision–ECCV 2016: 14th European Conference, Amsterdam, The Netherlands,
October 11-14, 2016, Proceedings, Part III 14, pp. 849–866 (2016). https://doi.
org/10.1007/978-3-319-46487-9 52 . Springer
[11] Kim, W., Won, J.H., Park, S., Kang, J.: Demand forecasting models for medicines
through wireless sensor networks data and topic trend analysis. International
Journal of Distributed Sensor Networks 11(9), 907169 (2015) https://doi.org/10.
1155/2015/907169
[12] Wang, J., Xu, B., Zu, Y.: Deep learning for aspect-based sentiment analysis. In:
2021 International Conference on Machine Learning and Intelligent Systems En-
gineering (MLISE), pp. 267–271 (2021). https://doi.org/10.1109/MLISE54096.
2021.00056 . IEEE
[13] Saura, J.R.: Using data sciences in digital marketing: Framework, methods, and
performance metrics. Journal of Innovation & Knowledge 6(2), 92–102 (2021)
https://doi.org/10.1016/j.jik.2020.08.001
[14] Saura, J.R., Ribeiro-Soriano, D., Palacios-Marqu´ es, D.: From user-generated data
to data-driven innovation: A research agenda to understand user privacy in digital
39

markets. International Journal of Information Management 60, 102331 (2021)
https://doi.org/10.1016/j.ijinfomgt.2021.102331
[15] Ribeiro-Navarrete, S., Saura, J.R., Palacios-Marqu´ es, D.: Towards a new era of
mass data collection: Assessing pandemic surveillance technologies to preserve
user privacy. Technological Forecasting and Social Change 167, 120681 (2021)
https://doi.org/10.1016/j.techfore.2021.120681
[16] Xu, K., Lin, Z., Zhao, J., Shi, P., Deng, W., Wang, H.: Multimodal deep learning
for social media popularity prediction with attention mechanism. In: MM 2020
- Proceedings of the 28th ACM International Conference on Multimedia (2020).
https://doi.org/10.1145/3394171.3416274
[17] Lin, H.H., Lin, J.D., Ople, J.J.M., Chen, J.C., Hua, K.L.: Social media popular-
ity prediction based on multi-modal self-attention mechanisms. IEEE Access 10
(2022) https://doi.org/10.1109/ACCESS.2021.3136552
[18] Nguyen, M.-T., Le, D.H., Nakajima, T., Yoshimi, M., Thoai, N.: Attention-based
neural network: A novel approach for predicting the popularity of online content.
In: 2019 IEEE 21st International Conference on High Performance Computing
and Communications; IEEE 17th International Conference on Smart City; IEEE
5th International Conference on Data Science and Systems (HPCC/SmartCi-
ty/DSS), pp. 329–336 (2019). https://doi.org/10.1109/HPCC/SmartCity/DSS.
2019.00058 . IEEE
[19] Liao, D., Xu, J., Li, G., Huang, W., Liu, W., Li, J.: Popularity prediction on online
articles with deep fusion of temporal process and content features. In: Proceedings
of the AAAI Conference on Artificial Intelligence, vol. 33, pp. 200–207 (2019).
https://doi.org/10.1609/aaai.v33i01.3301200
[20] Chen, J., Liang, D., Zhu, Z., Zhou, X., Ye, Z., Mo, X.: Social media popularity
prediction based on visual-textual features with xgboost. In: Proceedings of the
27th ACM International Conference on Multimedia, pp. 2692–2696 (2019). https:
//doi.org/10.1145/3343031.335607
[21] Zhang, Z., Chen, T., Zhou, Z., Li, J., Luo, J.: How to become instagram famous:
Post popularity prediction with dual-attention. In: 2018 IEEE International Con-
ference on Big Data (big Data), pp. 2383–2392 (2018). https://doi.org/10.1109/
BigData.2018.8622461 . IEEE
[22] Zhang, W., Wang, W., Wang, J., Zha, H.: User-guided hierarchical attention net-
work for multi-modal social image popularity prediction. In: The Web Conference
2018 - Proceedings of the World Wide Web Conference, WWW 2018 (2018).
https://doi.org/10.1145/3178876.3186026
[23] Wang, J., Yang, S., Zhao, H., Yang, Y.: Social media popularity prediction with
multimodal hierarchical fusion model. Computer Speech & Language 80, 101490
40

(2023) https://doi.org/10.1016/j.csl.2023.101490
[24] Caleffi, P.-M.: The ‘hashtag’: A new word or a new rule? SKASE Journal of
Theoretical Linguistics 12 (2015) https://doi.org/10.24093/awej/call6.6
[25] Zhang, S., Yao, Y., Xu, F., Tong, H., Yan, X., Lu, J.: Hashtag recommendation
for photo sharing services. In: Proceedings of the AAAI Conference on Artificial
Intelligence (2019). https://doi.org/10.1609/aaai.v33i01.33015805
[26] Abousaleh, F.S., Cheng, W.H., Yu, N.H., Tsao, Y.: Multimodal deep learning
framework for image popularity prediction on social media. IEEE Transactions on
Cognitive and Developmental Systems 13 (2021) https://doi.org/10.1109/TCDS.
2020.3036690
[27] Bakhshi, S., Shamma, D.A., Gilbert, E.: Faces engage us: Photos with faces at-
tract more likes and comments on instagram. In: Proceedings of the SIGCHI
Conference on Human Factors in Computing Systems (2014). https://doi.org/10.
1145/2556288.2557403
[28] Gelli, F., Uricchio, T., Bertini, M., Bimbo, A.D., Chang, S.F.: Image popularity
prediction in social media using sentiment and context features. In: Proceedings
of the 23rd ACM International Conference on Multimedia (2015). https://doi.
org/10.1145/2733373.2806361
[29] Li, J., Gao, Y., Gao, X., Shi, Y., Chen, G.: Senti2pop: Sentiment-aware topic
popularity prediction on social media. In: Proceedings - IEEE International Con-
ference on Data Mining, ICDM, vol. 2019-November (2019). https://doi.org/10.
1109/ICDM.2019.00143
[30] Mannepalli, K., Singh, S.P., Kolli, C.S., Raj, S., Bojja, G.R., Rajakumar, B.,
Binu, D.: Popularity prediction model with context, time and user sentiment infor-
mation: An optimization assisted deep learning technique. International Journal
of Uncertainty, Fuzziness and Knowledge-Based Systems 31(02), 283–302 (2023)
https://doi.org/10.1142/S0218488523500150
[31] Yang, C., Wang, X., Jiang, B.: Sentiment enhanced multi-modal hashtag recom-
mendation for micro-videos. IEEE Access 8, 78252–78264 (2020) https://doi.org/
10.1109/ACCESS.2020.2989473
[32] Liao, Y.Y.: Leveraging hashtag networks for multimodal popularity prediction of
Instagram posts. In: Calzolari, N., B´ echet, F., Blache, P., Choukri, K., Cieri, C.,
Declerck, T., Goggi, S., Isahara, H., Maegaard, B., Mariani, J., Mazo, H., Odijk,
J., Piperidis, S. (eds.) Proceedings of the Thirteenth Language Resources and
Evaluation Conference, pp. 7191–7198. European Language Resources Associa-
tion, Marseille, France (2022). https://aclanthology.org/2022.lrec-1.779
[33] Arazzi, M., Cotogni, M., Nocera, A., Virgili, L.: Predicting tweet engagement with
41

graph neural networks. In: Proceedings of the 2023 ACM International Conference
on Multimedia Retrieval, pp. 172–180 (2023). https://doi.org/10.1145/3591106.
3592294
[34] Purba, K.R., Asirvatham, D., Murugesan, R.K.: Instagram post popularity trend
analysis and prediction using hashtag, image assessment, and user history fea-
tures. International Arab Journal of Information Technology 18 (2021) https:
//doi.org/10.34028/iajit/18/1/10
[35] Kumar, N., Yadandla, A., Suryamukhi, K., Ranabothu, N., Boya, S., Singh, M.:
Arousal prediction of news articles in social media, vol. 10682 LNAI (2017). https:
//doi.org/10.1007/978-3-319-71928-3 30
[36] Lin, Z., Huang, F., Li, Y., Yang, Z., Liu, W.: A layer-wise deep stacking model
for social image popularity prediction. World Wide Web 22 (2019) https://doi.
org/10.1007/s11280-018-0590-1
[37] Cao, Q., Shen, H., Gao, J., Wei, B., Cheng, X.: Popularity prediction on social
platforms with coupled graph neural networks. (2020). https://doi.org/10.1145/
3336191.3371834
[38] Mannepalli, K., Singh, S.P., Kolli, C.S., Raj, S., Bojja, G.R., Rajakumar, B.R.,
Binu, D.: Popularity prediction model with context, time and user sentiment
information: An optimization assisted deep learning technique. International
Journal of Uncertainty, Fuzziness and Knowledge-Based Systems31 (2023) https:
//doi.org/10.1142/S0218488523500150
[39] Tan, Y., Liu, F., Li, B., Zhang, Z., Zhang, B.: An efficient multi-view multimodal
data processing framework for social media popularity prediction. In: MM 2022
- Proceedings of the 30th ACM International Conference on Multimedia, pp.
7200–7204 (2022). https://doi.org/10.1145/3503161.3551607
[40] Zappavigna, M.: Searchable talk: The linguistic functions of hashtags. Social
Semiotics 25(3), 274–291 (2015) https://doi.org/10.1080/10350330.2014.996948
[41] Liu, J., He, Z., Huang, Y.: Hashtag2vec: Learning hashtag representation with
relational hierarchical embedding model. In: IJCAI, vol. 2018-July (2018). https:
//doi.org/10.24963/ijcai.2018/480
[42] Chakrabarti, P., Malvi, E., Bansal, S., Kumar, N.: Hashtag recommendation for
enhancing the popularity of social media posts. Social Network Analysis and
Mining 13 (2023) https://doi.org/10.1007/s13278-023-01024-9
[43] Bansal, S., Gowda, K., Kumar, N.: A hybrid deep neural network for multimodal
personalized hashtag recommendation. IEEE Transactions on Computational
Social Systems 10 (2023) https://doi.org/10.1109/TCSS.2022.3184307
42

[44] Wang, J., Yang, S., Zhao, H., Yang, Y.: Social media popularity prediction with
multimodal hierarchical fusion model. Computer Speech and Language 80 (2023)
https://doi.org/10.1016/j.csl.2023.101490
[45] Devlin, J., Chang, M.-W., Lee, K., Toutanova, K.: BERT: Pre-training of deep
bidirectional transformers for language understanding. In: Burstein, J., Doran,
C., Solorio, T. (eds.) Proceedings of the 2019 Conference of the North Ameri-
can Chapter of the Association for Computational Linguistics: Human Language
Technologies, Volume 1 (Long and Short Papers), pp. 4171–4186. Association for
Computational Linguistics, Minneapolis, Minnesota (2019). https://doi.org/10.
18653/v1/N19-1423 . https://aclanthology.org/N19-1423
[46] Mikolov, T., Sutskever, I., Chen, K., Corrado, G., Dean, J.: Distributed repre-
sentations of words and phrases and their compositionality. Advances in Neural
Information Processing Systems (2013)
[47] Simonyan, K., Zisserman, A.: Very deep convolutional networks for large-scale
image recognition. In: 3rd International Conference on Learning Representations,
ICLR 2015 - Conference Track Proceedings (2015)
[48] Deng, J., Dong, W., Socher, R., Li, L.-J., Li, K., Fei-Fei, L.: Imagenet: A large-
scale hierarchical image database. In: 2009 IEEE Conference on Computer Vision
and Pattern Recognition (2010). https://doi.org/10.1109/cvpr.2009.5206848
[49] Serengil, S.I., Ozpinar, A.: Hyperextended lightface: A facial attribute analysis
framework. In: 2021 International Conference on Engineering and Emerging Tech-
nologies (ICEET) (2021). https://doi.org/10.1109/ICEET53442.2021.9659697
[50] Grootendorst, M.: Bertopic: Neural topic modeling with a class-based tf-idf
procedure. https://arxiv.org/abs/2203.05794 (2022)
[51] McInnes, L., Healy, J., Astels, S.: hdbscan: Hierarchical density based clustering.
The Journal of Open Source Software 2 (2017) https://doi.org/10.21105/joss.
00205
[52] McInnes, L., Healy, J., Saul, N., Großberger, L.: Umap: Uniform manifold ap-
proximation and projection. Journal of Open Source Software 3 (2018) https:
//doi.org/10.21105/joss.00861
[53] Hamilton, W.L., Ying, R., Leskovec, J.: Inductive representation learning on large
graphs. In: Neural Information Processing Systems, vol. 2017-December (2017)
[54] Manning, C.D., Surdeanu, M., Bauer, J., Finkel, J., Bethard, S.J., McClosky,
D.: The stanford corenlp natural language processing toolkit. In: Proceedings of
52nd Annual Meeting of the Association for Computational Linguistics: System
Demonstrations, vol. 2014-June (2014). https://doi.org/10.3115/v1/p14-5010
43

[55] Hutto, C.J., Gilbert, E.: Vader: A parsimonious rule-based model for sentiment
analysis of social media text. In: Proceedings of the International AAAI Con-
ference on Web and Social Media (2014). https://doi.org/10.1609/icwsm.v8i1.
14550
[56] Aloufi, S., Zhu, S., Saddik, A.E.: On the prediction of flickr image popularity
by analyzing heterogeneous social sensory data. Sensors (Switzerland) 17 (2017)
https://doi.org/10.3390/s17030631
[57] Jollife, I.T., Cadima, J.: Principal component analysis: A review and recent
developments (2016). https://doi.org/10.1098/rsta.2015.0202
[58] Srivastava, N., Hinton, G., Krizhevsky, A., Sutskever, I., Salakhutdinov, R.:
Dropout: a simple way to prevent neural networks from overfitting. journal of
machine learning research. Journal of Machine Learning Research 15 (2014)
[59] Wu, B., Liu, B., Cheng, W.H., Zeng, Z., Liu, P., Luo, J.: Smp challenge: An
overview of social media prediction challenge 2019. In: MM 2019 - Proceedings of
the 27th ACM International Conference on Multimedia (2019). https://doi.org/
10.1145/3343031.3356084
[60] Wu, B., Cheng, W.H., Zhang, Y., Huang, Q., Li, J., Mei, T.: Sequential pre-
diction of social media popularity with deep temporal context networks. In:
IJCAI International Joint Conference on Artificial Intelligence, vol. 0 (2017).
https://doi.org/10.24963/ijcai.2017/427
[61] Ding, K., Wang, R., Wang, S.: Social media popularity prediction: A multiple
feature fusion approach with deep neural networks. In: Proceedings of the 27th
ACM International Conference on Multimedia (2019). https://doi.org/10.1145/
3343031.3356062
[62] Gradient boost tree network based on extensive feature analysis for popularity
prediction of social posts. In: Proceedings of the 31st ACM International Con-
ference on Multimedia, pp. 9451–9455 (2023). https://doi.org/10.1145/3581783.
3612843
[63] Mao, S., Xi, W., Yu, L., L¨ u, G., Xing, X., Zhou, X., Wan, W.: Enhanced catboost
with stacking features for social media prediction. In: Proceedings of the 31st
ACM International Conference on Multimedia, pp. 9430–9435 (2023). https://
doi.org/10.1145/3581783.3612839
[64] Spearman, C.: The proof and measurement of association between two things.
The American Journal of Psychology 15 (1904) https://doi.org/10.2307/1412159
44
