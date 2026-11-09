---
title: 'PROMINET: Prototype-based Multi-View Network for Interpretable Email Response Prediction'
url: https://arxiv.org/abs/2310.16753
category: ai-marketing
subcategory: empirical
date: 2023-10
venue: EMNLP 2023
authors:
- Yuqing Wang
- Prashanth Vijayaraghavan
- Ehsan Degan
source: arxiv
pdf_url: https://arxiv.org/pdf/2310.16753
pages: 14
chars: 56947
fetched_at: '2026-11-08T13:12:27+00:00'
kb_version: 1
---

# PROMINET: Prototype-based Multi-View Network for Interpretable Email Response Prediction

PROMINET: Prototype-based Multi-View Network for Interpretable Email
Response Prediction
Yuqing Wang∗
University of California, Santa Barbara
Santa Barbara, CA 93106
wang603@ucsb.edu
Prashanth Vijayaraghavan∗
IBM Research
San Jose, CA 95120
prashanthv@ibm.com
Ehsan Degan
IBM Research
San Jose, CA 95120
edehgha@us.ibm.com
Abstract
Email is a widely used tool for business commu-
nication, and email marketing has emerged as
a cost-effective strategy for enterprises. While
previous studies have examined factors affect-
ing email marketing performance, limited re-
search has focused on understanding email re-
sponse behavior by considering email content
and metadata. This study proposes a Prototype-
based Multi-view Network (PROMINET) that
incorporates semantic and structural informa-
tion from email data. By utilizing prototype
learning, the PROMINET model generates la-
tent exemplars, enabling interpretable email
response prediction. The model maps learned
semantic and structural exemplars to observed
samples in the training data at different levels
of granularity, such as document, sentence, or
phrase. The approach is evaluated on two real-
world email datasets: the Enron corpus and
an in-house Email Marketing corpus. Experi-
mental results demonstrate that thePROMINET
model outperforms baseline models, achiev-
ing a ∼ 3% improvement in F1 score on both
datasets. Additionally, the model provides in-
terpretability through prototypes at different
granularity levels while maintaining compara-
ble performance to non-interpretable models.
The learned prototypes also show potential for
generating suggestions to enhance email text
editing and improve the likelihood of effective
email responses. This research contributes to
enhancing sender-receiver communication and
customer engagement in email interactions.
1 Introduction
With the ever-increasing volume of emails being
exchanged daily, email communication remains
a cornerstone of business interactions and an ef-
fective means of content distribution. As the pri-
mary communication tool for organizations and
individuals alike, email marketing has maintained
*These authors contributed equally to this work.
its popularity over the years, evolving and expand-
ing alongside advancements in technology. This
form of marketing enables businesses to tailor tar-
geted messages to customers based on their prefer-
ences, leveraging the quick, easy, and cost-effective
nature of email communication. In this context,
predicting customer response behavior in email
marketing campaigns becomes crucial for optimiz-
ing customer-product engagements and enhancing
communication efficiency between senders and re-
cipients. Consider the example email shown in
Figure 1, where various factors such as the email’s
contents (subject and body) and the recipient’s
organization, can influence the likelihood of re-
ceiving a response. Therefore, understanding the
impact of these factors and their correlation with
email response behavior is paramount. Research
(Kim et al., 2016) has shown that a single word
can make a substantial difference in how a text
is interpreted. This insight applies to our email
response prediction task, making it essential to ad-
dress this challenge. The likelihood of an email
receiving a response can be influenced by vari-
ous factors, including the use of power words or
phrases, the persuasiveness of the text, and align-
ment with client preferences. Given the sensitivity
of words or phrases in our task, we need methods
to extract both the structural and semantic informa-
tion from email text to develop an effective predic-
tion model. Recently, there have been efforts to
To: john@<recipient_org_name>.com
From: callie@<sender_org_name>.com
Subject: Confirming you know
05/01/2020, Fri., 09:04 AM
Hi John,
<product_name> aims to address some of the most pressing issues
organizations are facing due to the impacts of COVID-19. We look
forward to you discovering new ways to work, manage risk, optimize
cost, and maintain customer satisfaction during this time. Stay safe and
well, John.
Best regards,
Callie
Email: [EMAIL] Phone: [PHONE_NO]
Figure 1: Sample Email with relevant contents.
study different explanation techniques for text clas-
arXiv:2310.16753v1  [cs.CL]  25 Oct 2023

sification. These methods typically fall into two
categories: post-hoc explanation methods (Mad-
sen et al., 2021) and self-explaining approaches
(Alvarez Melis and Jaakkola, 2018). Post-hoc ex-
planations use an additional explanatory model
to provide explanations after making predictions,
while self-explaining approaches generate explana-
tions simultaneously with the prediction. However,
post-hoc explanations may not accurately reveal the
reasoning process of the original model (Rudin,
2019), making it preferable to build models with
inherent interpretability. In this work, we propose
PROMINET, a novel interpretable email response
prediction model that integrates semantic and struc-
tural information from email data. PROMINET uti-
lizes prototype learning, a form of case-based rea-
soning, to make predictions based on similarities to
representative examples (prototypes) in the training
data. Unlike existing prototype-based architectures,
PROMINET provides explanations from multiple
perspectives: semantic (using transformer-based
models) and structural (using graph-based depen-
dency parsing with GNN). By leveraging a multi-
branch network, PROMINET offers holistic ex-
planations at different levels, including document-
level, sentence-level, and phrase-level prototypes.
We conduct quantitative analyses and ablation stud-
ies using two real-world email datasets: the Enron
corpus and the in-house email marketing corpus.
Our PROMINET model achieves superior perfor-
mance and offers explanations that simulate po-
tential edits, resulting in improved response rates.
Contributions: The key contributions of this work
are summarized as follows:
• We present PROMINET, the inaugural method
for interpretable email response prediction.
By combining transformer-based models and
dependency graphs with GNN, our approach
captures semantic and structural information
at various granularities.
• We conduct extensive experiments on real-
world email corpora. PROMINET outper-
forms the strongest baselines on both the En-
ron and Email Marketing corpus.
• Simulation experiments demonstrate the effec-
tiveness of learned prototypes in generating
email text editing suggestions, leading to a
significant enhancement in the overall email
response likelihood. These results indicate
promising avenues for further research.
2 Related Work
2.1 Email Response Prediction
Researchers have used machine learning methods
to improve email efficiency by predicting email re-
sponses. Previous work includes predicting email
importance and ranking by likelihood of user ac-
tion (Aberdeen et al., 2010), classifying emails into
common actions – read, reply, delete, and delete-
WithoutRead (Di Castro et al., 2016), and char-
acterizing response behavior based on various fac-
tors (On et al., 2010; Kooti et al., 2015; Qadir et al.,
2016) including time, length, and conversion, tem-
poral, textual properties, and historical interactions.
Our work differs from previous studies by consid-
ering both semantic and structural information in
email response prediction and developing an inter-
pretable model.
2.2 Explainability in Text Classification
Model explainability has gained significant atten-
tion with different explainability methods catego-
rized into post-hoc or self-explaining. Post-hoc
methods (Ribeiro et al., 2016; Simonyan et al.,
2013; Smilkov et al., 2017; Arras et al., 2016)
separate explanations from predictions, while self-
explaining methods (Bahdanau et al., 2014; Ra-
jagopal et al., 2021) generate explanations simulta-
neously with predictions. Drawing from previous
studies (Sun et al., 2020; Ming et al., 2019), our
work falls into the self-explainable category, pro-
viding explanations through prototypes. Prototype-
based networks make decisions based on the simi-
larity between inputs and selected prototypes. Orig-
inally used for image classification (Chen et al.,
2019), several methods (Ming et al., 2019; Hong
et al., 2020; Pluci ´nski et al., 2021) have been
adapted for text classification, where a similarity
score is used to learn prototypes, that represent
the characteristic patterns in the data. These proto-
types serve as exemplars or representative instances
from the dataset. However, these models provid-
ing unilateral explanations have limitations as they
lack granularity, provide an incomplete picture,
have limited coverage, and reduced interpretability.
In contrast, granular prototypes produced by our
PROMINET offer a more nuanced and interpretable
approach to understanding email data.
3 Problem Setup
We tackle the interpretable email response predic-
tion problem as a self-explainable binary classifica-

tion task. Given a training set D with email texts
xi and binary response labels yi ∈ {0, 1}, our goal
is to predict the likelihood of receiving a response
while providing insights into the decision process.
The labels indicate whether an email received a
response (1) or not (0), which could include clicks,
views, or replies. To enhance interpretability, we
learn latent prototypes at the document, sentence,
and phrase levels, mapping them to representative
observations in the training set. These prototypes
serve as classification references and analogical
explanations for the model’s decisions.
4 Methodology
In this section, we introduce PROMINET model,
that incorporates multi-view representations and
prototype layers to develop a self-explainable
email response prediction model. Our architec-
tural choices prioritize two key factors: accuracy
and interpretability. To ensure accurate email re-
sponse predictions, our model leverages features
derived from the email subject, body, and recipi-
ent information. It does so by employing a multi-
view architecture that captures the interplay be-
tween different factors. The model extracts both
structural and semantic information to comprehend
the valuable cues pertaining to email persuasive-
ness and engagement. Moreover, our model is de-
signed to be interpretable, offering insights into
decision-making at various levels. Using the in-
formation from the multi-view representations, the
model achieves interpretability through granular
latent prototypes that serve as explanations for pre-
dictions. By considering both accuracy and inter-
pretability, the model aims to strike a balance be-
tween making accurate predictions and providing
transparent reasoning. In our PROMINET model,
we incorporate two main views, namely the Seman-
tic view and the Structural view, to achieve our goal.
We acquire embeddings at the document, sentence,
and phrase-level by employing different compo-
nents described in the subsequent subsections.
4.1 Semantic View
The Semantic view focuses on capturing features
at both the document-level and sentence-level from
email data. To extract document-level features, we
employ a document encoder (f D) that considers
the interaction between different elements such as
the email subject (S), body/content (C), recipient
organization (O), and their interests (E). These el-
ements are separated by a special token ([SEP ]),
and we prepend the email with a token ([CLS ]). By
utilizing a pre-trained transformer-based encoder,
the email data is transformed into token-level repre-
sentations, where the [CLS ] token representation
serves as the document-level embedding, eD. For
sentence-level features, a similar transformer-based
sentence encoder (f S) is used to process each sen-
tence within the email body. We add special tokens
([CLS ] and [SEP ]) at the beginning and end of
each sentence respectively. We denote the sentence-
level embedding as eS.
4.2 Structural View
The structural view emphasizes the importance of
specific phrases in email engagement by examin-
ing the relationships between tokens or phrases
within email sentences. By employing dependency
parsing on the sentences, we create a graphical rep-
resentation known as a dependency graph. The
dependency graph comprises nodes representing
tokens and links representing dependency relation-
ships. These relationships are expressed as triples:
(vdep, < rel >, vgov), where vdep and vgov de-
note the dependent and governing tokens, respec-
tively; < rel >refers to the dependency relation-
ship between the tokens. To obtain phrase-level
embeddings eP , we extract dependency subgraphs
from the sentences, focusing on dependencies like
nominal subject (nsubj) and direct object (dobj)
relative to the ‘ROOT’ token. Utilizing a graph en-
coder (f P ), we generate embeddings for each de-
pendency subgraph, effectively capturing the struc-
tural information they convey.
4.3 Prototype Layers
In our approach, we utilize a prototype layer p con-
sisting of three sets of prototypes: pD ∈ Rj×d
for latent document prototypes, pS ∈ Rk×d for
sentence prototypes, and pP ∈ Rm×d for phrase
prototypes, where d is the dimension of the proto-
type embeddings (set identical to the dimensions
of the output representations from the encoders)
and j, k, mrefers to the number of prototypes as-
sociated with each granularity level. To guaran-
tee effective representation of each class through
learned prototypes at varying levels of granular-
ity, we assign a fixed number of prototypes to each
class. These prototypes are learned during the train-
ing process and represent groups of data instances,
such as documents, sentences, or phrases, found
in the training set. For each granularity level g,

Document
Encoder
Sentence
Encoder
Graph
Encoder
Structural View
Semantic View
Prototype LayerPrototype LayerPrototype Layer
Output Layer
Losses
Email Body (C)
Confirming you know
Email Subject (S)
Organization & Interests (O & E)
< Org_Name >
1. < Org_Name > helps Mid and South
Essex ICS boost engagement
2. < Org_Name > Reinvents the Public
Meeting Again; Launches Most Advanced
Remote & Hybrid Meeting Platform
S1: <product_name> aims to address
some of the most pressing issues
organizations are facing...
S2: We look forward to you discovering
new ways...
S3: Stay Safe and well
S1
S2
S3
Dependency
Parser
S3
S2
S1
S
C
O
E
PROMINET
Figure 2: Illustration of our PROMINET model. The model consists of an encoder and a prototype layer for each
granularity g (document (D), sentence (S) and phrase (P )) with two different views – semantic & structural.
which can be either document (D), sentence (S), or
phrase (P), the layer calculates the similarity be-
tween the granularity-specific embedding (eg) and
each trainable prototype. Formally,
sim(pg i , eg) = log

||p(g) i − eg||2 2 + 1
||pg i − eg||2 2 + ϵ
!
(1)
Here, pg i represents the ith prototype for gran-
ularity g, and it has the same dimension as the
embedding ( eg). The similarity score decreases
monotonically as the Euclidean distance||pg i −eg||2
increases, and it is always positive. For numeri-
cal stability, we set ϵ to a small value, specifically
1e − 4. We denote the computed similarity for each
granularity level g as S g.
4.4 Output Layer
Finally, our model’s output layer, denoted as c,
includes a fully connected layer followed by a soft-
max layer to predict the likelihood of an email
receiving a response. The prediction is determined
by the weighted sum S D + λ1S S + λ2S P , which
involves averaging the scores at the sentence and
phrase levels with their weights denoted by λ1 and
λ2, respectively.
4.5 Learning Objectives
We introduce different loss functions that ensure
accuracy and interpretability. For accuracy, we
have cross entropy loss:
Lce = 1 n nX i=1 CE (c ◦ p ◦ f (xi), yi) (2)
where the output layer c combines the informa-
tion captured by different encoders ( f) and pro-
totype layers (p) from multiple views at different
granularity levels. Drawing ideas from previous
studies (Zhang et al., 2022; Ming et al., 2019), we
introduce additional losses for prototype learning
including: (a) diversity loss ( Ldiv) that penalizes
prototypes that are too similar to each other, (b)
clustering loss (Lcls) that ensures that each embed-
ding (text or graph) is close to at least one proto-
type of its own class and (c) separation loss (Lsep)
encourages each embeddings to be distant from
prototypes not of its class. Formally,
Ldiv =
CX
k=1
X
q̸=r
pg q ,pg r ∈p
max(0, cos(pg q, pg r) − θ) (3)
Lcls = 1 n nX i=1 min q:pg q ∈pg yi ||f g(xi) − pg q||2 2 (4)
Lsep = − 1 n nX i=1 min q:pq /∈pg yi ||f g(xi) − pg q||2 2 (5)
where n is the total number of samples, C is the
number of classes, θ is the threshold of cosine sim-
ilarity, and cos(·, ·) measures the cosine similarity,
pg yi represents the set of prototypes belonging to

class yi for granularity g. Finally, we use L1 regu-
larization as the sparsity loss (Lspa) to the output
layer weights. The overall objective is:
L := Lce + αLdiv + βLcls + γLsep + δLspa (6)
where α, β, γ, δare the loss coefficients.
4.6 Prototype Projection
For improved interpretability, we project the latent
prototypes onto the closest emails, sentences, or
phrases from the training data. Each prototype’s
abstract representation is substituted with the near-
est latent email, sentence, or phrase embedding in
the training set that corresponds to its respective
class of interest, measured by Euclidean distance.
This conceptual alignment of prototypes with sam-
ples from the training set offers an intuitive and
human-understandable interpretation of the proto-
types associated with each class.
5 Experimental Setup
5.1 Datasets
Our framework is evaluated on two email datasets:
the Enron corpus 1 and the email marketing cor-
pus. The Enron dataset, collected by the CALO
Project, consists of ∼ 500k emails from around
150 Enron Corporation employees. The email mar-
keting corpus contains ∼ 400k email data, includ-
ing response details such as clicks, views, and
replies from vendors. These emails were part of an
email marketing program and only a subset of these
emails get responded to. In order to handle the data
imbalance, we perform a random sampling to cre-
ate a balanced split and conduct experiments over
5 runs. The dataset statistics and our other experi-
mental settings for both the datasets are included
in Appendix A, C.
5.2 Baselines
To demonstrate the effectiveness of our method,
we compare our proposed PROMINET with
transformer-based pretrained masked language
models such as BERT-base (Kenton and Toutanova,
2019), DistilBERT (Sanh et al., 2019), RoBERTa
(Liu et al., 2019), autoregressive language model
like XLNet (Yang et al., 2019), graph neural
network-based TextGCN (Yao et al., 2019) that op-
erates over a word-document heterogeneous graph,
and prototype learning-based (ProSeNet (Ming
1https://www.cs.cmu.edu/~enron/
et al., 2019) and ProtoCNN (Pluci´nski et al., 2021))
methods that learns to construct prototypes forsen-
tences or phrases.
Methods Enron Email Marketing
BERT-base 83.9±2.9 78.9±2.5
DistilBERT 79.3±2.6 73.6±2.7
RoBERTa 85.2±3.0 79.5±2.9
XLNet 85.6±3.4 80.2±3.6
TextGCN 80.9±3.7 74.1±3.4
ProSeNet 82.1±3.0 73.6±3.2
ProtoCNN 83.6±3.8 73.3±3.6
PROMINET VARIANTS
BERT + GCN 84.6±3.3 81.1±3.6
BERT + GAT 85.2±2.9 81.2±2.6
RoBERTa + GCN 87.8±2.8 83.1±3.2 ∗
RoBERTa + GAT 87.4±3.4 82.6±3.4
XLNet + GCN 88.2±3.2 83.1±3.6 ∗
XLNet + GAT 88.6±3.3 ∗ 82.6±3.4
Improvement (%) 3.50 3.62
Table 1: Evaluation results on two email corpus. We
report the weighted F1 score (%) & SD based on 5 runs.
Our method achieve statistically significant improve-
ments over the closest baselines (p <0.01).
5.3 Metrics
We calculate both the macro F1 and the weighted
F1-score to evaluate the performance of the pro-
posed models in the context of email response pre-
diction on both datasets. Nevertheless, we priori-
tize the weighted F1-score as our primary evalua-
tion metric due to the balanced class distributions in
our data splits. Additionally, we present the mean
and standard deviations of the F1-score across five
runs in Section 6. Finally, we also perform a statis-
tical analysis to assess the significance of the differ-
ences in F1-scores between our proposed method
and the nearest baselines using a paired t-test.
6 Results & Discussion
6.1 Overall Performance Comparison
Table 1 summarizes our evaluation results.
PROMINET consistently achieves the best perfor-
mance on both datasets. Specifically, using XLNet
encoder for texts and GAT encoder for dependency
graphs, our model improves the weighted average
F1 score by 3.50% for the Enron corpus. Similarly,
with RoBERTa/XLNet encoder for texts and GCN
encoder for dependency graphs, PROMINET im-
proves the weighted average F1 score by 3.62%
for the Email Marketing corpus. Compared to
the other transformer-based models, PROMINET

demonstrates performance improvements, indicat-
ing that incorporating dependency graphs enhances
word connections and contextual meaning, leading
to better overall performance. P ROMINET outper-
forms TextGCN significantly, suggesting that con-
sidering local information, such as word order, in
addition to global vocabulary information is crucial
for accurate classification. Moreover, PROMINET
surpasses prototype learning methods (ProSeNet
and ProtoCNN), highlighting the importance of
learning prototypes that capture both semantic and
structural aspects.
6.2 Ablation Study
In our ablation experiments 2, we scrutinize
the influence of various model components in
PROMINET. The amalgamation of XLNet, GAT,
and prototype learning demonstrates the highest
performance, underscoring their complementary
attributes. Prototype-based models exhibit compa-
rable performance to their non-interpretable coun-
terparts. Moreover, the fusion of XLNet with pro-
totype learning surpasses the combination of GAT
and prototype learning, highlighting the signifi-
cance of semantic information in text comprehen-
sion. This experiment not only illustrates the supe-
riority of multi-view representations derived from
both semantic and structural perspectives over mod-
els relying on embeddings from a single view, but
also showcases that when coupled with prototype
learning, PROMINET achieves the highest perfor-
mance. We present comprehensive ablation studies
that assess the impact of factors such as the num-
ber of prototypes, sensitivity to weights (λ1, λ2),
the contribution of various email metadata, and
detailed error analyses. For further information,
please refer to Appendix D.
6.3 Explanations for Prediction
6.3.1 Case study
Figure 3 illustrates the reasoning process of
PROMINET using an input example from the test
set in the Email Marketing corpus. It showcases the
most similar prototypes at the document, sentence,
and phrase levels. The selected prototypes, along
with their original labels, provide evidence for why
the input example is classified as "negative". Two
key observations emerge from the analysis: (a)
2Please refer to the Appendix for additional analyses,
including information on Datasets, Hyperparameters, Ablation
studies, Visualization, and Limitations.
Methods Enron Email Marketing
XLNet 85.6±3.4 80.2±3.6
GAT 81.4 ±3.1 78.1±2.9
XLNet + GAT 88.2±2.8 81.8±3.0
XLNet + Prototypes 86.2±2.9 80.8±3.1
GAT + Prototypes 82.9±3.2 78.3±3.6
XLNet + GAT +
Prototypes (PROMINET) 88.6∗ ±3.3 82.6∗ ±3.4
Table 2: Investigation of the Impact of Various Com-
ponents in PROMINET on Both Datasets. We analyze
different model variants to assess the influence of se-
mantic and structural views, as well as prototype layers.
All the learned prototypes associated with the in-
put have the label "negative", consistent with the
prediction of the input example; (b) The document-
level prototypes exhibit similar topics to the input
example, such as event invitations and basic event
introductions. The sentence-level and phrase-level
prototypes share similarities in terms of client inter-
ests, patterns, and grammatical relationships. We
present similar analysis for an example from the
Enron corpus in Appendix E.
6.4 Suggest Edits based on Prototypes
We utilize the attention mechanism from GAT to
identify key phrases and important dependency re-
lationships2 that contribute to the prediction. The
words in a sentence are categorized into different
types, such as nouns, verbs, adjectives, and ad-
verbs. Since adjectives and nouns usually form key
phrases, which are crucial, we focus on nouns and
related words, considering their attention scores.
Additionally, we use layer integrated gradients
(LIG) (Sundararajan et al., 2017) and transformer-
based embeddings to determine the importance of
words in a sentence. After extracting the top-1
keyword/top-1 keyphrase for each sentence, we
substitute keywords/keyphrases associated with
prototypes with the label “positive" (i.e., emails
with response) for the keywords and key phrases
of sentences in the test set with the label “nega-
tive" (i.e., emails without response) to investigate
whether there is a possibility to improve the ratio
of “positive" labels, that is, to improve the overall
response rate. Here, the selected prototype emails
share similar topics with the email to be edited.
Otherwise, we randomly choose a prototype with
response for edits. For an email, there are a few po-
sitions we consider editing: (1) email subjects; (2)
email opening sentence/greeting (e.g., I hope you

S1: Hi Jorge, you may have heard that <company>’s conference is entirely virtual this year and
free with everything going on in the world right now. S2: It may be a welcome distraction to
advance your expertise and learn something new. S3: We think we can help here. S4: There are
some particular <product team> topics we’ll discuss that you may be interested in supporting
cyber resiliency monitor your infrastructure with storage insights. S5: Take a look at the Think
site to see additional topics and register for your free pass.
Hi Andrew, I hope your New Year is off to a great start. It’s me again from the <product> team. Come to
learn about converges IDA and <company>’s hybrid cloud approach while sampling some delicious
whiskey wings. Interested join us Wednesday February 17th at 2pm? You do not want to miss this great
dialogue and food seating is limited, so reserve you spot now. If you have any questions, feel free to
reach out.
Hello Delli, I’m reaching out to invite you to <event>. At <event>, you’ll have the chance to directly
engage with world-class experts, industry leaders and peers gain insights guidance and valuable
connections your business needs and learn how groundbreaking technologies like hybrid cloud and AI
can positively impact your business.
Y ou’re interested in taking advantage of fast low-cost storage or needing a solution that can grow
according to your requirements. S4
Again, I invite you to take a look at the short video and supporting materials.        S5
Input
Text
Top-2 Prototypes
(email-level)
Prototypes
(sentence-level)
Importance Score
(Similarity * Weight)
3.28 * 0.46 = 1.51
3.06 * 0.35 = 1.07
2.50 * 0.29 = 0.73
2.34 * 0.68 = 1.59
Prototypes
(dependency
tree)
Text: I have access to pricing tools and exclusive access to the demo of our new system.        S2
1.98 * 0.42 = 0.83
Prediction: Negative    Gold Standard: Negative
Prototype
Label
Negative
Negative
Negative
Negative
Negative
Figure 3: Example inputs and PROMINET prototypes for Email Marketing corpus. While classifying the input as
negative (no response), the labels of prototypes are also negative. Due to space constraint, we only show a few
prototypes with the largest weights.
are doing well); (3) main contents of the email; (4)
closing sentence (e.g., best regards). In our experi-
ence, we observe that using prototype-based edits
of email subjects and main contents bring signifi-
cant improvement of the overall email response rate
on both datasets. For instance, the model captures
the importance of creating a sense of urgency that
improves the likelihood of receiving a response.
A sentence from an email labeled as “negative"
turns “positive” when the sentence containing a
phrase “register for your free pass" is replaced with
a prototype-based phrase “get your free pass before
the offer expires". Investigations on the impact of
suggested edits on the effectiveness of our models
are detailed in Appendix D.
7 Conclusion
In this study, we introduced PROMINET, a
Prototype-based Multi-view Network that incor-
porates semantic and structural information from
email data for interpretable email response predic-
tion. PROMINET compared inputs to representa-
tive instances (prototypes) in the latent space to
make predictions and offers prototypical explana-
tions at the document, sentence, and phrase levels
for enhanced human understanding. The evalua-
tion on real-world email datasets demonstrates that
PROMINET outperforms baseline models, achiev-
ing a significant improvement of approximately
3% in F1 score on both the Enron corpus and the
Email Marketing corpus. Our research contributes
to enhancing sender-receiver communication and
customer engagement in email interactions, fill-
ing a gap in understanding by considering email
content and metadata. Future research directions
involve addressing limitations such as time and
historical interactions, handling unseen scenarios,
improving interpretability, and balancing personal-
ized content with prototypical information. These
advancements will further propel the usage AI tech-
nqiues in email marketing and communication.
Ethics Statement
For this research, we utilized two distinct datasets.
One of them comprises a publicly available col-
lection, while the other involves IBM’s internal
email marketing corpus. It’s important to note that
we exclusively employed anonymized training data
from the latter 3, ensuring the removal of any per-
sonally identifiable information. Furthermore, our
methodology aims to enhance the interpretability
of the email response prediction system, providing
insights into the model’s decision-making process
3Although anonymized data was utilized for training and
evaluation, in this paper, we have incorporated randomly gen-
erated names in email samples for the purpose of visualization
and enhanced comprehension.

at different levels of granularity without compro-
mising proprietary or sensitive information. How-
ever, a noteworthy concern arises regarding the
potential influence on user sentiments and actions
in subtle ways, which could be interpreted as coer-
cion. In such scenarios, the explanations provided
through prototypes may inadvertently reveal biases
or problematic training scenarios. This underscores
the need for stringent guidelines and explainabil-
ity, particularly in sensitive real-world contexts, to
ensure that the model’s predictions do not exert
any harmful or ethically questionable influences on
user decision-making. It’s important to acknowl-
edge that these risks are not unique to our method-
ology, but rather, they are pertinent to various AI
techniques. This emphasizes the necessity for a
consistent and vigilant review process and update
of ethical standards and practices.
References
Douglas Aberdeen, Ondrey Pacovsky, and Andrew
Slater. 2010. The learning behind gmail priority in-
box.
David Alvarez Melis and Tommi Jaakkola. 2018. To-
wards robust interpretability with self-explaining neu-
ral networks. Advances in neural information pro-
cessing systems, 31.
Leila Arras, Franziska Horn, Grégoire Montavon, Klaus-
Robert Müller, and Wojciech Samek. 2016. Explain-
ing predictions of non-linear classifiers in nlp. In
Proceedings of the 1st Workshop on Representation
Learning for NLP, pages 1–7.
Dzmitry Bahdanau, Kyunghyun Cho, and Yoshua Ben-
gio. 2014. Neural machine translation by jointly
learning to align and translate. arXiv preprint
arXiv:1409.0473.
Chaofan Chen, Oscar Li, Daniel Tao, Alina Barnett,
Cynthia Rudin, and Jonathan K Su. 2019. This looks
like that: deep learning for interpretable image recog-
nition. Advances in neural information processing
systems, 32.
Dotan Di Castro, Zohar Karnin, Liane Lewin-Eytan, and
Yoelle Maarek. 2016. You’ve got mail, and here is
what you could do with it! analyzing and predicting
actions on email messages. In Proceedings of the
ninth acm international conference on web search
and data mining, pages 307–316.
Dat Hong, Stephen S Baek, and Tong Wang. 2020. In-
terpretable sequence classification via prototype tra-
jectory. arXiv preprint arXiv:2007.01777.
Jacob Devlin Ming-Wei Chang Kenton and Lee Kristina
Toutanova. 2019. Bert: Pre-training of deep bidirec-
tional transformers for language understanding. In
Proceedings of NAACL-HLT, pages 4171–4186.
Joon Hee Kim, Amin Mantrach, Alejandro Jaimes, and
Alice Oh. 2016. How to compete online for news
audience: Modeling words that attract clicks. In Pro-
ceedings of the 22nd ACM SIGKDD International
Conference on Knowledge Discovery and Data Min-
ing, pages 1645–1654.
Farshad Kooti, Luca Maria Aiello, Mihajlo Grbovic,
Kristina Lerman, and Amin Mantrach. 2015. Evolu-
tion of conversations in the age of email overload. In
Proceedings of the 24th international conference on
world wide web, pages 603–613.
Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Man-
dar Joshi, Danqi Chen, Omer Levy, Mike Lewis,
Luke Zettlemoyer, and Veselin Stoyanov. 2019.
Roberta: A robustly optimized bert pretraining ap-
proach. arXiv preprint arXiv:1907.11692.
Andreas Madsen, Siva Reddy, and Sarath Chandar. 2021.
Post-hoc interpretability for neural nlp: A survey.
arXiv preprint arXiv:2108.04840.
Yao Ming, Panpan Xu, Huamin Qu, and Liu Ren. 2019.
Interpretable and steerable sequence learning via pro-
totypes. In Proceedings of the 25th ACM SIGKDD
International Conference on Knowledge Discovery
& Data Mining, pages 903–913.
Byung-Won On, Ee-Peng Lim, Jing Jiang, Amruta Pu-
randare, and Loo-Nin Teow. 2010. Mining interac-
tion behaviors for email reply order prediction. In
2010 International Conference on Advances in So-
cial Networks Analysis and Mining, pages 306–310.
IEEE.
Kamil Pluci ´nski, Mateusz Lango, and Jerzy Ste-
fanowski. 2021. Prototypical convolutional neu-
ral network for a phrase-based explanation of sen-
timent classification. In Joint European Conference
on Machine Learning and Knowledge Discovery in
Databases, pages 457–472. Springer.
Ashequl Qadir, Michael Gamon, Patrick Pantel, and
Ahmed Hassan. 2016. Activity modeling in email.
In Proceedings of the 2016 Conference of the North
American Chapter of the Association for Computa-
tional Linguistics: Human Language Technologies,
pages 1452–1462.
Dheeraj Rajagopal, Vidhisha Balachandran, Eduard H
Hovy, and Yulia Tsvetkov. 2021. Selfexplain: A self-
explaining architecture for neural text classifiers. In
Proceedings of the 2021 Conference on Empirical
Methods in Natural Language Processing, pages 836–
850.
Marco Tulio Ribeiro, Sameer Singh, and Carlos
Guestrin. 2016. " why should i trust you?" explaining
the predictions of any classifier. In Proceedings of
the 22nd ACM SIGKDD international conference on

knowledge discovery and data mining, pages 1135–
1144.
Cynthia Rudin. 2019. Stop explaining black box ma-
chine learning models for high stakes decisions and
use interpretable models instead. Nature Machine
Intelligence, 1(5):206–215.
Navdeep S Sahni, S Christian Wheeler, and Pradeep
Chintagunta. 2018. Personalization in email market-
ing: The role of noninformative advertising content.
Marketing Science, 37(2):236–258.
Victor Sanh, Lysandre Debut, Julien Chaumond, and
Thomas Wolf. 2019. Distilbert, a distilled version
of bert: smaller, faster, cheaper and lighter. arXiv
preprint arXiv:1910.01108.
Karen Simonyan, Andrea Vedaldi, and Andrew Zis-
serman. 2013. Deep inside convolutional networks:
Visualising image classification models and saliency
maps. arXiv preprint arXiv:1312.6034.
Daniel Smilkov, Nikhil Thorat, Been Kim, Fernanda
Viégas, and Martin Wattenberg. 2017. Smoothgrad:
removing noise by adding noise. arXiv preprint
arXiv:1706.03825.
Zijun Sun, Chun Fan, Qinghong Han, Xiaofei Sun,
Yuxian Meng, Fei Wu, and Jiwei Li. 2020. Self-
explaining structures improve nlp models. arXiv
preprint arXiv:2012.01786.
Mukund Sundararajan, Ankur Taly, and Qiqi Yan. 2017.
Axiomatic attribution for deep networks. In Interna-
tional conference on machine learning, pages 3319–
3328. PMLR.
Zhilin Yang, Zihang Dai, Yiming Yang, Jaime Car-
bonell, Russ R Salakhutdinov, and Quoc V Le. 2019.
Xlnet: Generalized autoregressive pretraining for lan-
guage understanding. Advances in neural informa-
tion processing systems, 32.
Liang Yao, Chengsheng Mao, and Yuan Luo. 2019.
Graph convolutional networks for text classification.
In Proceedings of the AAAI conference on artificial
intelligence, volume 33, pages 7370–7377.
Zaixi Zhang, Qi Liu, Hao Wang, Chengqiang Lu,
and Cheekong Lee. 2022. Protgnn: Towards self-
explaining graph neural networks. In Proceedings
of the AAAI Conference on Artificial Intelligence ,
volume 36, pages 9127–9135.
A Dataset Details
Summary statistics of the datasets are shown in
Table A1. Here, the striking difference in the ratio
of “response" and “no response" samples between
two email corpus is due to different email intents.
The Enron corpus is pertaining to personal commu-
nication while the Email Marketing corpus is used
for focused marketing campaigns.
Datasets Enron Email Marketing
Total 497,465 404,167
Response 270,309 57,607
No Response 227,156 346,560
Table A1: Statistics of the datasets.
A.1 Enron Corpus
The Enron email dataset does not have explicit
“response" and “no response" classes. Since “reply"
and “forward" email threads appear in the original
corpus, we categorize a single email as “response"
as long as the original email contains “reply" or
“forward" tag and extract only the portion of the
email after the “reply" or “forward" tag. Otherwise,
we categorize the single email as “no response" and
keep the entire email text.
A.2 Email Marketing Corpus
We obtained this in-house corpus for research pur-
poses. This dataset contains response information
from clients in the form of clicks, views or replies.
We label a single email as “response" as long as
the original email is clicked, viewed, or replied at
least once. Otherwise, we label the email as “no
response".
B Experimental Settings
At encoder layer f, we use three variants of BERTs
for text embedding, i.e., BERT-base, RoBERTa,
and XLNet. Meanwhile, we use two variants of
GNNs for subgraph embedding, i.e., GCN and
GAT. Since the dataset is skewed, we perform a
random downsample to create a balanced split and
conduct experiments over 5 runs. We adopt the
AdamW optimizer with a weight decay of 0.1. The
hyperparameter search space for both datasets is
included in Table A2. We perform random search
for hyperparameter optimization. All of the experi-
ments are conducted on four NVIDIA Tesla P100
GPUs.

C Hyperparameter Search Space
Hyperparameters Search Space
Batch size [16, 32, 64, 128]
Learning rate [ 1e−5, 2e−5, 5e−5]
Class weight for lce [0.2, 0.3, 0.4, 0.5]
j, k, m [6, 10, 20, 30, 40, 50]
θ [0.2, 0.3, 0.4]
α [0.001, 0.005, 0.01, 0.015, 0.02]
β [0.005, 0.01, 0.02, 0.05, 0.1]
γ [0.001, 0.005, 0.01, 0.015, 0.02]
δ [0.001, 0.005, 0.01, 0.015, 0.02]
λ1 [0.1, 0.3, 0.5, 0.7, 0.9]
λ2 [0.1, 0.3, 0.5, 0.7, 0.9]
Table A2: Hyperparameter search space of PROMINET
on both datasets.
D Ablation Studies
D.1 Effect of Email Components
We study the contribution of different email com-
ponents as text inputs to the model’s performance.
In this study, we consider the subject, body text,
and recipient’s email organization as email com-
position components. Additionally, we utilize the
AYLIEN news API4 to extract the interests of orga-
nizations. Our assumption is that the intent of an
email may be associated with the recipient’s orga-
nization’s topic of interest. The API extracts news
categories and headlines associated with the orga-
nization. For the Enron corpus, we evaluate the
influence of the subject and body text only since all
the recipients’ email organizations in this corpus
are from Enron. In the Email Marketing corpus,
there are a considerable number of email recipient
organizations for which the API is unable to extract
interest information. In such cases, we leave the
interests unknown. However, the goal of this exper-
iment is to estimate the extent to which the interest
information can boost our prediction performance.
An example email from the Email Marketing cor-
pus that contains all the pieces of information is
provided in Figure A1. This example helps in un-
derstanding the information contained in each part
of the email before feeding it to the model. Based
on the results presented in Table 1, we evaluate
the contributions of email components using the
PROMINET setting (XLNet + GAT) for the En-
ron corpus and the PROMINET setting (XLNet +
GCN) for the Email Marketing corpus. We summa-
rize the experimental results in Table A3 and make
4https://aylien.com/
the following observations: The introduction of
organization interests in the Email Marketing cor-
pus shows marginal improvements in performance,
confirming our assumption that there is an associ-
ation between the intent of the sending email and
the interests of the recipient’s organization. The
high standard deviation in performance when incor-
porating organization interests can be attributed to
incomplete information. Despite these limitations,
we observed some marginal improvement. A more
in-depth analysis with complete information could
yield significantly better results, but such investi-
gation is beyond the scope of this paper and can
be pursued in future research. When considering
individual components of an email, the model’s per-
formance using body text as input outperforms the
performance when using only the subject or email
organization information. This finding highlights
the significance of body texts in predicting email
responses. The best performance is achieved when
incorporating all three components—the subject,
body text, and recipient’s email organization. This
indicates that each piece of information is valu-
able and contributes to performance gains. Overall,
these observations emphasize the importance of
considering multiple components and organization
interests in improving the performance of email
response prediction models.
S: Confirming You Know
O: granicus.com
C: Hi <NAME>,
 <PRODUCT_NAME> aims to address some of the most pressing issues organizations are
facing due to the impacts of COVID-19. Throughout <LINK> the sessions at our digital
event, gain insights on how you and your organization can navigate through uncertainty,
and adapt to changing conditions. Take a few minutes to explore our response <LINK> to
COVID-19. We look forward to you discovering new ways to work, manage risk,
optimize cost, and maintain customer satisfaction during this time. Stay safe and well,
<NAME>.
Best regards,
<NAME>
<ORG> Client
Email: <EMAIL> Phone: <PHONE_NO>
E: U.S. Government Resources | Law | Politics (categories)
Granicus helps Mid and South Essex ICS boost engagement (news headlines)
Granicus Reinvents the Public Meeting, Again; Launches Most Advanced
Remote and Hybrid Meeting Platform (news headlines)
Figure A1: An example email from Email marketing
corpus that contains subject (S), content (C), organiza-
tion (O), and interests (E).
D.2 Error Analysis of
Transformer-based/GNN Models
Analyzing the error patterns of our Transformer-
based/GNN models allows us to demonstrate the
benefits provided by our PROMINET model. We

focus on qualitatively examining email samples
that are correctly classified by PROMINET but mis-
classified by other baseline models. For example,
the sample email input provided in Figure 3 was
misclassified by models that do not jointly model
semantic and structural prototypes for response pre-
diction. Additional analyses on models that solely
utilize either semantic or structural prototypes are
provided in Appendix D.2.1.
D.2.1 Effects of Using only BERT/GNN
When using a combination of a transformer-based
model and prototype learning, the input shown in
Figure 3 is associated with the following top-2
email-level prototypes:
1. Prototype 1: “Hi Phil, I hope this email finds
you well. Just a quick line inviting you to at-
tend <company_name>’s online launch event
storage made simple for all. During this event,
you’ll see how we are revolutionizing the en-
try enterprise storage space. If aah pharma-
ceuticals is challenged to deliver more with
less budget it will be well worth your time
attending.”
2. Prototype 2: “Hi John, hope this message
finds you doing well today. My name is
Nicholas Tompkins with <product_name>,
reaching out to personally invite you to
an upcoming event. Did you know <com-
pany_name> technology is simple innovative
flexible fast and infused by AI. In this session,
you will learn how we co-create solutions with
you using flash systems virtualization, data
protection cyber resiliency and business conti-
nuity strategies.”
The most similar prototypes mapped to S4 and S5
are as follows:
• Prototype mapped to S4: “Hi Jack, do you
have the need to refresh or add additional stor-
age to your environment?”
• Prototype mapped to S5: “Click here to regis-
ter.”
The majority of prototypes associated with the in-
put are labeled as "positive." However, the true
label of the input is "negative." It is possible that al-
though BERT captures the contextual information
of an email, its ability to analyze dependencies and
determine the grammatical structure of sentences is
limited. Grammatical structures play a crucial role
in enhancing sentence clarity and governing how
words can be combined to form coherent sentences.
Email
Components
Enron
PROMINET (XLNet + GAT)
Email Marketing
PROMINET (XLNet + GCN)
S 80.2 ± 3.6 76.9 ± 3.2
O —- 73.4 ± 2.9
C 85.1 ± 3.2 80.1 ± 3.4
S + O —- 78.4 ± 3.6
S + C 88.6 ± 3.3 82.6 ± 3.3
O + C —- 81.8 ± 3.7
S + O + C —- 83.1 ± 3.6
S + O + C + E —- 83.5 ± 4.1∗
Table A3: Effects of different email components as in-
puts of PROMINET on both datasets. The performance
is evaluated via weighted average F1 score (%). Ex-
periments are conducted with 5 random initializations.
The results are shown in the format of mean and stan-
dard deviation. Here, S, O, C, and E represent subject,
organization, body text and organization interests, re-
spectively.
When employing a combination of GNN (Graph
Neural Network) and prototype learning, we ob-
serve that the most similar prototype mapped to S2
can be seen in Figure 3. However, there is a discrep-
ancy between the label assigned to the prototype
("positive") and the label assigned to the sentence
("negative"). This mismatch suggests that the GNN
component might lack the necessary information
on text semantics to fully comprehend the content
of the text.
This observation highlights the importance of
investigating the interpretability capability of indi-
vidual model components. In this case, it verifies
the effectiveness of combining a transformer-based
model, which excels at capturing contextual infor-
mation, with a GNN, which is adept at capturing
grammatical structures. The combination of these
two components allows them to mutually influence
and complement each other, resulting in a more
comprehensive understanding of the input text.
D.3 Effect of Suggested Edits
We also investigate the impact of suggested edits on
the effectiveness of our models. To simulate this,
we conduct experiments where we make edits to
the emails and observe the resulting changes in the
ratio of “positive” labels. Table A4 presents the ra-
tios of original “negative” emails that are predicted
as “positive” after making edits under different situ-
ations on both datasets. We employ a combination
of XLNet and GAT for predictions and find that ap-
propriate edits to email subjects and main content

Weights Prototypes
0.45
0.61
Dear Brad, it was great to speak to you today. I have provided the instructions to upgrade ICE to version 737. Please forward these instructions to your IT
Department. We are strongly recommending that you upgrade. It involves some major changes. Please call me if you have any further questions. Thanks for
your assistance.
Email Marketing
Corpus
Enron Corpus
Following my previous email, I wanted to make sure you’re aware of some of the changes we’ve made to our portfolio and how that may impact your
systems as a storage contact for <company>.0.64
0.33
We have delivered an electronic ticket to the airlines notifying them of your purchase.0.21
0.24
pD
pS
pD
pS
pP
pP
Hello Iris, it’s Ann Marie from the <product> team. I hope you are keeping well. I’m just following up on my previous email to advise that the storage
assessment is still available to you and your team, but that we also have a live demo I can take you through on <company>’s new storage all
<product_name> this year. <company> have released some incredibly affordable all <product_name>. If you are in the market for an upgrade on your
current infrastructure or are curious to see how the new technology works, I really think it would be worth taking a look at.
Figure A2: Visualization of three types of prototypes (i.e., document (pD), sentence (pS), phrase-level (pP ))
learned from the PROMINET model on Enron Corpus and Email Marketing corpus.
lead to improvements in the overall email response
rate for both datasets. These improvements signify
the potential of using prototypes to enhance the
likelihood of generating favorable email responses.
Editing Positions Enron Email Marketing
Subjects 1.4 ± 0.2 2.1 ± 0.3
Open sentence 0.3 ± 0.0 0.9 ± 0.1
Main contents 1.9 ± 0.3 3.8 ± 0.5
Closing sentence 0.3 ± 0.0 0.4 ± 0.1
Table A4: Drop ratio of “negative" labels after making
edits on both datasets.
D.4 Effect of hyperparameters in PROMINET
We conducted a study to examine the impact of
certain hyperparameters on model performance,
specifically focusing on the number of prototypes
and the addition weights.
Number of Prototypes (j,k,m): Figure A3a il-
lustrates the relationship between the number of
prototypes and the model performance, measured
by the weighted average F1 score, for both datasets.
We observed that increasing the number of proto-
types initially led to a significant improvement in
performance. However, once the number of proto-
types surpassed 20, the performance gains became
less prominent, and in some cases, adding more
prototypes even resulted in slightly worse perfor-
mance. This phenomenon can be attributed to the
increased complexity of the model, making it more
challenging to train and comprehend. It demon-
strates the trade-off between performance and inter-
pretability. The optimal number of prototypes was
found to be 20 for the Email Marketing corpus and
10 for the Enron corpus, as the model performance
10
 20
 30
 40
 50
 60
Number of prototypes
81
82
83
84
85
86
87
88Weighted average F1 score (%)
Email Marketing
Enron
(a) Effects of j, k, m.
0.1 0.3 0.5 0.7 0.9
1
0.9
0.7
0.5
0.3
0.1 2
Weighted Average F1 (%)
77
78
79
80
81
82
83 (b) Effects of λ1, λ2.
Figure A3: Hyperparameter effects on performance.
peaked at these values.
Addition Weight ( λ1, λ2): The addition
weights, λ1 and λ2, control the training balance
among the three branches in our model. Figure A3b
presents the performance variations on the Email
Marketing corpus when different combinations of
λ1 and λ2 were used. The results demonstrate that
the best performance was achieved when λ1 was
set to 0.3 and λ2 was set to 0.5 in PROMINET.
By investigating these hyperparameters, we gain
insights into their effects on model performance,
enabling us to optimize the performance and inter-
pretability of our PROMINET model.
E Case Study
In Figure A4, we can examine the selected proto-
types and their original labels, which serve as evi-
dence for why the input example has been classified
as positive. We can make two key observations:
• The majority of prototypes associated with the
input have the label “positive”, which aligns
with the prediction of the input example being
“positive”.

S1: Dorie and Michelle, this will update you on the latest developments. S2: Bob and I are
working on finding a solution that resolves all the issues which get complex due to the fact that
not only has the Hilton made claims against Enron but also against Event Resources in the
bankruptcy proceeding. S3: In other words, even if we succeed in facing down the Hilton on its
claims directly against us, the Hilton may be able to recover some percentage of those claims
directly from Event Resources in the bankruptcy proceeding.
The consumer advocates strongly feel that the generators have to take a hair cut as part of the solution as
well. The governor will announce later this afternoon a framework solution identical to that we have
reported previously a state purchase of transmission assets and an issuance of bonds by the utilities but
with state support through the DWR. However, it remains unclear whether the framework will be
acceptable to all parties.
I would like to keep everyone updated with changes on the floor. S1
Transwestern had met with the AQB over this issue in 1996 and assumed that the issue
had been resolved..        S5
Input
Textdocument-levelsentence-level
Importance Score
(Similarity * Weight)
2.26 * 0.54 = 1.22
2.03 * 0.48 = 0.97
1.78 * 0.29 = 0.52
1.96 * 0.33 = 0.65
phrase-level
Text: : Have a good day and have fun.        S1
1.46 * 0.20 = 0.829
Prediction: Positive Gold Standard: Positive
Prototype
Label
Negative
Positive
Positive
Negative
Positive
Governor Davis is committed to solving the California energy crisis by developing consumer driven
solutions. Protecting customers from short term market aberrations. Continuing to expand the consumers
ability to choose. We are missing thoughtful Orderly Process.
Figure A4: Example inputs and PROMINET prototypes for Enron corpus. While classifying the input as positive
(response), the majority of the prototype labels are also positive. Due to space constraint, we only show a few
prototypes with the largest weights.
• The prototypes at the document-level share
similar topics with the input example, specif-
ically related to problem-solving. At the
sentence-level, both S1 and its corresponding
prototype discuss update notifications, while
S2 and its prototype exhibit similar patterns.
In terms of phrase-level prototypes, phrases
extracted by S1 and its prototype share similar
grammatical relationships, such as nominal
subject (nsubj), adjectival modifier (amod),
coordination (cc), and so on.
F Prototype Visualization
We provide prototype visualization, where each
prototype is mapped to the latent representation of
the most similar email in the training set. This map-
ping is facilitated by assigning static index num-
bers to each email or sentence from the same email
during the model training phase. These index num-
bers enable us to visualize the prototypes later on.
Figure A5 showcases some learned prototypes in a
human-readable form for both datasets. The weight
assigned to each prototype is derived from the fully
connected layer. This diversity in different types of
prototypes enhances our ability to provide explana-
tions for prototype-based predictions.
G Limitations
This work has several limitations that should be
acknowledged. Firstly, the focus of this study is
primarily on the text aspects of email data, disre-
garding factors such as time and historical inter-
actions with customers. While this approach is
suitable for the prediction task at hand, it overlooks
potentially valuable contextual information that
could impact email response behavior. Addition-
ally, while prototypes are useful for the intended
use case, there may be unseen scenarios or outliers
that cannot be accurately mapped to examples in
the training set, posing a challenge in dealing with
such cases. Exploring alternative approaches to
enhance interpretability and present explanations
in a more user-friendly manner is an avenue for
future research. Furthermore, the prototype-based
suggestion of edits presented in this work is a sim-
ulation experiment and may not capture the exact
dynamics of real-time scenarios. The proposed
shortcuts for improving model performance should
be carefully considered to ensure alignment with
actual email interactions. Lastly, using prototypical
information in email composition runs the risk of
generating templated emails with reduced personal-
ization, even though personalization is known to be
beneficial in email marketing (Sahni et al., 2018).
Thus, addressing these limitations and exploring

Figure A5: Most similar dependency subgraph prototype associated with S2 of input example in Figure 3 using only
GNN.
these areas of improvement could be the scope of
future research.
