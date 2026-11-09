---
title: 'SMTPD: A New Benchmark for Temporal Prediction of Social Media Popularity'
url: https://arxiv.org/abs/2503.04446
category: social-media
subcategory: empirical
date: 2025-03
venue: ''
authors:
- Yijie Xu
- Bolun Zheng
- Wei Zhu
- Hangjia Pan
- Yuchen Yao
source: arxiv
pdf_url: https://arxiv.org/pdf/2503.04446
pages: 11
chars: 48576
fetched_at: '2026-11-08T13:01:18+00:00'
kb_version: 1
---

# SMTPD: A New Benchmark for Temporal Prediction of Social Media Popularity

SMTPD: A New Benchmark for Temporal Prediction of Social Media Popularity
1Yijie Xu*, 1Bolun Zheng*†, 1Wei Zhu*, 1Hangjia Pan, 1Yuchen Yao,
2Ning Xu, 2Anan Liu, 3Quan Zhang, 1Chenggang Yan
1Hangzhou Dianzi University, 2Tianjin University, 3Peking University
Abstract
Social media popularity prediction task aims to predict the
popularity of posts on social media platforms, which has
a positive driving effect on application scenarios such as
content optimization, digital marketing and online advertis-
ing. Though many studies have made significant progress,
few of them pay much attention to the integration between
popularity prediction with temporal alignment. In this pa-
per, with exploring YouTube’s multilingual and multi-modal
content, we construct a new social media temporal popu-
larity prediction benchmark, namely SMTPD, and suggest
a baseline framework for temporal popularity prediction.
Through data analysis and experiments, we verify that tem-
poral alignment and early popularity play crucial roles in
social media popularity prediction for not only deepening
the understanding of temporal dynamics of popularity in so-
cial media but also offering a suggestion about developing
more effective prediction models in this field. Code is avail-
able at https://github.com/zhuwei321/SMTPD
1. Introduction
With the advancement of Internet communication technol-
ogy in recent years, social media has gradually emerged
and has influenced various aspects of human life. Any con-
tent posted on social media stands the chance of becoming
hot spot, and widely disseminated social media content can
generate significant social and economic benefits. The pre-
diction of social media popularity holds immense potential
applications in content optimization [1, 30], online advertis-
ing [14, 15], digital marketing [19, 45], search recommen-
dations [4, 17], intelligent fashion [10], and beyond.
In the early stages of popularity research, statistical and
topological methods [41, 43, 53] were extensively em-
ployed, with the research focus primarily on time-aware
popularity prediction. These prediction methods rely on
information about the earlier popularity of posted content.
*These authors contributed equally to this work.
†Corresponding author
This work is supported by the the National Key Research and Devel-
opment Program of China under Grant 2020YFB1406600.
(a) A social media post, also serving as a sample in SMTPD.
(b) Box plots of popularity scores over time.
Figure 1. Content sections and popularity trend of SMTPD. In 1a,
a sample involves four sections of content, with temporal popu-
larity. 1b depicts box plots of daily popularity scores, illustrating
variations in popularity distribution at different time points. The
distribution consistently demonstrates a decay pattern over time.
Along with the many large-scale social media popularity
datasets are proposed [3, 42, 47, 48], the machine learn-
ing based methods are widely employed to achieve reason-
able predictions of social media popularity and have shown
remarkable performance. These methods emphasize metic-
ulous design in feature extraction and fusion, followed by
popularity prediction using machine learning models such
as deep neural networks (DNN) and gradient boosting deci-
sion trees (GBDT).
Table 1 lists the public or mentioned social media pop-
ularity datasets in the most recent years as far as we know.
For above machine learning based methods, the large-scale
arXiv:2503.04446v1  [cs.SI]  6 Mar 2025

Dataset Source Category Samples Language Prediction Type
Mazloom [35] Instagram fast food brand 75K English single
Sanjo [42] Cookpad recipe 150K Japanese single
TPIC17 [47] Flickr - 680K English single
SMPD [48] Flickr 11 categories 486K English single
AMPS [11] YouTube shorts 13K Korean single
SMTPD (ours) YouTube 15 categories 282K over 90 languages sequential
Table 1. Comparing SMTPD with existed multi-modal social me-
dia popularity datasets.
social media popularity datasets [3, 11, 35, 42, 47, 48] pro-
vide the fundamental supports.
However, existing datasets and related studies have no-
table limitations, such as insufficient multi-modal data, lim-
ited language diversity, and, crucially, the absence of a con-
sistent timeline for prediction. As shown in Figure1b, pop-
ularity distributions shift over time, and predictions made
at irregular intervals can reduce accuracy and create chal-
lenges for practical applications.
Furthermore, effective popularity prediction requires in-
tegrating both the multi-modal content of social media and
information on the communication process to capture the
dynamic trends in popularity. This essential aspect is miss-
ing in most current prediction efforts.
Targeting to fix up the above shortcomings of existed
datasets, in this paper, we propose a new benchmark called
Social Media Temporal Popularity Dataset (SMTPD) by ob-
serving multi-modal content from mainstream for cutting-
edge research in the field of social multimedia along with
multi-modal feature temporal prediction. As shown in Fig-
ure 1a, multi-modal contents of social media posts in mul-
tiple languages generated the daily popularity information
during the communication process. We define such a post as
a sample of SMTPD, and propose a multi-modal framework
as a baseline to achieve the temporal prediction of popular-
ity scores.The proposed framework consists of two parts,
feature extraction and regression. In the feature extraction
part, multiple pre-training models and pre-processing meth-
ods are introduced to translate the multi-modal content into
deep features. In the regression part, we encode the state
and time sequence of the extracted features, and adopt the
LSTM-based structure to regress the 30-day popularities.
Through analysis and experiments, we discover the impor-
tance of early popularity to the task of popularity prediction,
and demonstrate the effectiveness of our method in tempo-
ral prediction. Generally, the contribution of this work can
be summarized as:
• Against the missing of temporal information in social me-
dia popularity researches, we observe over 282K multi-
lingual samples from mainstream social media since they
released on the network lasting for 30 days. We refer to
these samples as SMTPD, a new benchmark for temporal
popularity prediction.
• Basing on existed methods, we innovate in both the se-
lection of feature extractors and the construction of the
temporal regression component, and suggest a baseline
model which enables temporal popularity prediction to be
conducted across multiple languages while aligning pre-
diction times.
• Exploring the popularity distribution and the correlation
between popularity at different times. Based on these, We
find the importance of early popularity for popularity pre-
diction task, and point out that the key-point for predict-
ing popularity is to accurately predict the early popularity.
2. Related work
Statistical and topological methods . Szabo et al. [43]
found that the early-stage popularity notably influences sub-
sequent popularity. Yang et al. [53] conducted cluster anal-
ysis on temporal patterns within online content, revealing
distinct characteristics of popularity variations across dif-
ferent clusters. Richier et al. [40, 41] proposes bio-inspired
models to characterize the evolution of video view counts.
Wu et al. [51] suggested that the information cascade pro-
cess is best described as an activate–decay dynamic process.
Multi-modal feature based Methods . Ding et al. [13]
use pre-trained ResNet and BERT to extract visual and tex-
tual features, with the DNN regression. Xu et al. [52] and
Lin et al. [31] adopted attention mechanisms to effectively
integrate multi-modal features. Chen et al. [6] compared
the performance of several regression models, among which
XGBoost [7] exhibited the best results. Hsu et al. [22] em-
ployed LightGBM [23] and TabNet [2] to capture intricate
semantic relationships in multi-modal features. Lai et al.
[26] engineered handcrafted features, exploiting CatBoost
for regression. Mao et al. [34] enhanced CatBoost-based
model by stacking features. Tan et al. [44] extracted visual-
textual features by ALBEF [29] and Chen et al. [8, 9] en-
riched more intermodal features to promote predictive per-
formance. Wu et al. [50] emphasized increasing feature
dimensions to improving predictive performance. The post
dependencies captured by sliding window average [46] and
DSN [54] has also led to improvements. Many of these
multi-modal methods are based on the SMPD and working
out great [32, 49].
Social media popularity datasets . Mazloom et al. [35]
conducted experiments using a dataset of posts related to
fast-food brands collected from Instagram. Sanjo et al. [42]
provided a recipe popularity prediction dataset based on
Cookpad, which includes text content entirely in Japanese.
Li et al. [28] predicted the future popularity of topics by us-
ing historical sentiment information based on Twitter’s text
data records. TPIC17 [47] and SMPD [48] are datasets for
single popularity prediction task based on Flickr.
We believe that the loss of temporal alignment about

popularity in existing methods is a common problem. The
image dynamic popularity dataset [37] gave us insights, so
we propose a multi-modal temporal popularity benchmark
to address the shortcomings of existing studies.
3. SMTPD Dataset
With the great development of web communication tech-
nologies, social multimedia has become the most popular
media around the world. However, most existing social me-
dia prediction datasets are built on the basis of single-output
prediction, meaning they observe existing posts and infer
their popularity based on their posting time. As mentioned
earlier, these data without aligned posting times exhibit
non-uniform popularity distributions. Therefore, SMTPD
keep an eye on one of the most popular worldwide so-
cial media, YouTube [5], with over 282K samples, primar-
ily focusing on the evolution of popularity over time for
these samples. We collected over 402K raw data samples.
Specifically, we first removed records with missing val-
ues—which likely resulted from network issues during data
acquisition. Next, we eliminated samples that either failed
to be crawled on certain days or had been deleted within 30
days. Finally, we filtered out potential outliers using the 3σ
rule. In this section, we provide a comprehensive overview
of the SMTPD’s composition. Additionally, we present var-
ious data analysis results that contribute to the feasibility of
our approach.
Unlike the retrospective methods used in previous
datasets, we take note of the newly posted multi-modal con-
tent and then observe popularity information every 24 hours
via YouTube API. Considering that in real-world applica-
tions, the posts to be predicted are always new, this data
observation method allows us to obtain aligned temporal
popularity of new posts, which is more in line with prac-
tical applications. Figure 1a show a sample from SMTPD.
We note diverse attributes, including visual content, textual
content, metadata, and user profiles. Additionally, we focus
on the temporal popularity for each sample within 30 days
after release. We perform basic statistics for SMTPD, as
shown in Table 2.
3.1. Temporal Popularity
The utilization of temporal popularity data is versatile. It
not only serves as the output for predictions but also as
inputs, where a segment preceding a specific time point,
coupled with multi-modal content, can forecast subsequent
popularity. We analyze the distribution and the correlation
of popularity over time, so as to facilitate a comprehensive
understanding of the significance of temporal popularity for
predictions from different perspectives.
A number of popularity definitions have been born from
previous work [27, 55]. We use Khosla’s popularity score
transformation [24] as it can normalize the distribution of
view counts to a suitable popularity score’s distribution. It
can be represented as:
p = log2( v d + 1) (1)
where p is the popularity score, v is the view counts of a
sample, d represents the corresponding number of days af-
ter the post’s release. As shown in Figure 1, the histogram
of view counts reveals an extreme long-tailed distribution,
which might not be suitable as a prediction target. It’s evi-
dent that the distribution of the popularity score metric be-
comes more reasonable.
In addition, we notice that there is a strong correlation
between the popularity scores of different days. The Pear-
son Correlation (PC) and Spearman Ranking Correlation
(SRC) can respectively reflect the linear relationship and
rank-order correlation between popularity scores of differ-
ent days as follows:
P C=
Pn
i=1(Xi − ¯X)(Yi − ¯Y )qPn
i=1(Xi − ¯X)2
qPn
i=1(Yi − ¯Y )2
(2)
SRC = 1 n − 1
nX
i=1
( Xi − ¯X σX )( Yi − ¯Y σY ) (3)
where X and Y denote the popularity scores belonging to 2
different days, while ¯X and σX denote the mean and stan-
dard deviation of X, and similarly for Y . PC and SRC re-
spectively reflect the linear relationship and rank-order cor-
relation between popularity scores of different days.
The Pearson Correlation (PC) and Spearman Rank Cor-
relation (SRC) heat maps illustrate internal relationships in
daily popularity scores, establishing a basis for prediction
based on these temporal patterns. Further details are avail-
able in the supplementary materials.
Statistics SMTPD SMPD (Train/Test)
Number of samples 282.4K 305K/181K
Number of users 152.7K 38K/31K
Mean popularity 5.95 6.41/5.12
STD popularity 4.15 2.47/2.41
Number of categories 15 11
Number of custom tags 960K 250K
Average length of title 53.4 chars 29 words
Mean duration 1853.4 s -
Table 2. The basic statistics of all samples in SMTPD, comparing
to SMPD[48]. Due to the multilingual environment, we use chars
(characters) to describe the average length of title.

3.2. Multi-Modal Content
Multi-modal feature fusion is the mainstream approach in
today’s popularity prediction methods. In this section, we
will divide the data into corresponding modality and eluci-
date the multi-modal content in SMTPD.
3.2.1. Visual Content
SMTPD samples, primarily drawn from a multi-modal so-
cial media platform, are heavily influenced by visual ele-
ments. Since metrics like view count and popularity score
are often based on the cover frame that viewers see before
clicking to play, we use the cover frame as the primary
visual content. This approach balances popularity impact
with copyright considerations.
3.2.2. Textual Content
The textual content in posts plays a crucial role in media dis-
semination and user engagement. We examine several core
elements, including category, title, description, and hash-
tags (denoted by the “#” symbol), along with the user ID
(user nickname) from profile metadata. YouTube defines
15 distinct video categories, all in English, which support
content organization and discovery. Figure 3 shows the sta-
tistical distribution of content by category.
(a) The PC Matrix
 (b) The SRC Matrix
Figure 2. The heat map of daily popularity correlations. The
figure clearly shows that there is a high degree of correlations in
popularity between consecutive days.
As an international platform, YouTube hosts user-
defined textual content in multiple languages beyond stan-
dard categories. Figure 4 illustrates the distribution and
popularity bias across title languages.
In previous researches, the datasets typically had uni-
form language for text content, without considering mul-
tilingual aspects. While this simplifies modeling for pre-
diction methods, it also poses significant limitations for in-
ternational social media platforms which not restricted to a
single language. Besides, predictions based on a few lan-
guages may introduce biases [16] against popularity.
3.2.3. Numerical values
Numerical attributes frequently function as supplementary
factors in enhancing prediction accuracy. In this study, we
examined key attributes, including video duration, uploader
follower count, and the number of posts by the uploader.
Additionally, we manually derived several auxiliary met-
rics, such as title length, the count of custom tags, and de-
scription length, to further enrich the feature set and support
predictive robustness.
4. Temporal popularity prediction
The multi-modal feature-based temporal prediction frame-
work is shown in Figure 5, which is divided into two main
parts: multi-modal feature extraction and temporal popular-
ity score regression. This framework is designed to adapt to
the multilingual temporal prediction tasks under time align-
ment. The prediction target is set as the popularity of sam-
ples, which corresponds to the temporal popularity within
30 days after the sample’s release.
4.1. Multi-Modal Feature Extraction
For different modalities in SMTPD, we adopted distinct fea-
ture extraction methods. We additionally incorporated fea-
tures from the categorical modality to investigate the impact
of categorical features on popularity prediction.
4.1.1. Visual Features
The cover image of a social media content is a very impor-
tant component which would help users to quickly under-
stand what they would see if clicking to view this content.
(a) The statistics of samples in each category
(b) Average popularity of each category
Figure 3. The statistics based on category. 3a counts the number
of samples in each category, and 3b shows the average popularity
score of samples in each category.

Figure 4. Languages analysis. The left is the proportions of these
languages, with ”Other” encompassing 90 different languages.
The right represents the average popularity in different languages,
revealing the geographic biases . The languages of samples are
counted by reference to the title.
Therefore, the cover image would directly affect the pop-
ularity of a social media content. The semantic informa-
tion provided in the cover image plays a key role for user’s
understanding. We adopt convolutional neural networks
ResNet-101 [20] pre-trained on ImageNet as our visual fea-
ture extraction model to obtain the semantic information
provided by the cover. To match the input size of ResNet-
101, we re-scale the size of cover image to 224 × 224. The
2048-dimension feature vector before the final classification
layer will be selected as the final visual feature fv:
fv = ResNet(S(I)) (4)
where I denotes the cover image and S denotes the re-scale
operation. However, the cover image would not always be
uploaded by authors or be unavailable due to the network
transmission. For those contents missing the cover image,
we use blank images with all pixels are set to zero instead.
4.1.2. Textual Features
Textual information significantly impacts a user’s choice to
view or skip content. Key textual inputs include category, ti-
tle, tags, description, and user profile ID. Extracting seman-
tic features from these inputs is crucial for accurate popu-
larity prediction.
However, unlike previous popularity prediction tasks,
one distinguishing characteristic of SMTPD is that its text
content includes multiple languages, and many samples
contain text in more than one language. This makes it chal-
lenging to use many pre-trained word vector models based
on single-language corpora, such as [18, 36, 38].
Thanks to the multilingual capability of BERT-
Multilingual [12], which processes text across languages in
a single model, we use it to extract a 768-dimensional fea-
ture vector for each text, capturing semantic information as:
f k t = BERT(T k) (5)
Figure 5. The proposed model consists of two layers. The upper
layer processes visual, textual, numerical, and categorical features,
which are input to a multi-layer perceptron (MLP). The MLP out-
puts are concatenated and fed into a lower LSTM layer for regres-
sion. Each LSTM cell’s output is passed through another MLP,
with the final MLP outputs combined to generate a time predic-
tion sequence using the ReLU activation function.
where k ∈ {cat, tit, tag, des, uid} maps to category, ti-
tle, tags, description, and user ID. These are combined into
a 768 × 5 matrix, transformed through 5 × 5 convolution to
produce the 768D textual featureft, which can be expressed
as:
ft = Conv5×5(C(f cat t , ftit t , ftag t , fdes t , fuid t )) (6)
where C denotes the above combing operation.
4.1.3. Numerical Features
Numerical metrics directly influence whether an audience
clicks to watch which sample on social media platform.
Also, the number of followers and the number of posts
also impact the process through which an audience navi-
gates from content uploaders’ user pages to click and watch
videos. Hence, we selected these influential numerical met-
rics for numerical features extraction.As the number of user
followers share a similar distribution pattern that exhibiting
long-tailed characteristics as view counts, it is necessary to
apply a logarithmic transformation before feeding it into the
network. Afterward, all numerical items are Z-score nor-
malized and concatenated as numerical features:
f j n = T j − µj σj (7)
fn = Concat(f f ol n , fpos n , fdur n , ftl n , ftn n , fdl n , fEP n ) (8)
where j ∈ {f ol, pos, dur, tl, tn, dl, EP} represents the
log-scaled follower counts, total number of posts, video du-

ration, title length, the number of tags, description length
and the early popularity (the 1st day’s popularity). The
µ and σ represents the mean and standard deviation of all
samples. And Concat denotes the horizontal concatenating
operation.
4.1.4. Categorical Features
The categorical disparities across social media platforms are
depicted in Figure 3b. Beyond text-based feature extrac-
tion, these disparities inform the generation of categorical
features. Language functions as a key marker of regional
and cultural distinctions among content creators, as high-
lighted by the language bias observed in Figure 4. Conse-
quently, language classification features are crucial for en-
hancing prediction accuracy. To develop these classification
features, two sub-features are selected: label and language
attributes. The label feature captures the semantic category,
while the language attribute is derived from the language in
the video title. Assuming that the primary language of all
text content matches the title’s language, we use langid [33]
for classification. Two embedding layers are introduced
to encode label and language features independently, each
processed by a dedicated multi-layer perceptron (MLP). Fi-
nally, the outputs are combined via cumulative multiplica-
tion to form the classification feature fc, defined as:
fc = MLP1(E1(T cat)) ⊙ MLP2(E2(langid(T tit))) (9)
where E1 and E2 represent two independent embedding
layers, and MLP 1 and MLP 2 refer to multi-layer percep-
trons applied to the label embedding E 1(T cat) and the lan-
guage embedding E 2(langid(T tit )), respectively. The op-
erator ⊙ denotes element-wise multiplication, which com-
bines the outputs of the two MLPs to produce the final clas-
sification feature fc.
4.1.5. Feature Fusion
After extraction, features from different modalities are
aligned in dimension through multi-layer perceptrons
(MLPs) and then concatenated into fused features F .
4.2. Temporal Popularity Regression
4.2.1. Sequential Encoding and Adjustment
Considering the high correlation between popularity values
on adjacent days in the ground truth, we employ a LSTM
[21] structure to get the temporal variations in popularity.
As shown in Figure 5, multiple LSTM cells are constructed
to transmit temporal information. The initial states (both
hidden state and cell state) of the LSTM are generated by
passing the F through the same MLP as state encoding. Ad-
ditionally, the input for LSTM cell at each time step is con-
structed from F through temporal encoding MLPs. These
two encoding process can be written as:
h0 = c0 = MLPhc(F ) (10)
xs = MLPx s(F ) (11)
In this formulation, h0 and c0 denote the initial hidden state
and cell state, while xs represents the input at time step
s. The MLP hc module encodes the state information, and
MLPx s handles the temporal encoding at the s-th time step,
effectively capturing the sequence dynamics.
At each time step, both states are treated as the s-th
step’s features for output. After concatenating and process-
ing through independent MLPs, each LSTM cell produces
outputs, helping capture temporal popularity via backprop-
agation during training. Before final predictions, we apply a
non-negative adjustment since popularity scores cannot be
negative. This process is formulated as:
pres = max(0, MLPout s (Concat(hs, cs))) (12)
Where pres, hs, cs, and MLPout s denote the predicted value,
hidden state, cell state, and output MLP at time step s, re-
spectively. The operation Concat refers to the process of
horizontally concatenating the vectors. After these steps,
the final temporal popularity predictions are produced.
4.2.2. Loss Function
The core component of our approach is the Composite
Gradient Loss (CGL), specifically designed for this task.
This custom loss function consists of several components:
SmoothL1Loss (SL) between the model’s outputs and tar-
gets, the first-order and second-order derivative differences
between the outputs and targets, the L1 loss between the
onehot encodings of the predicted and ground truth peaks,
and the Laplacian remainder (LR). These components are
combined with a weight ratio of 1:1:1:1e-6. The overall
loss function L is formulated as:
L = SL( ˆPd,i, Pd,i) +λ1 · SL( ˆP (1) d,i , P(1) d,i ) +λ2 · SL( ˆP (2) d,i , P(2) d,i )
(13)
+ α ·
nX
i=1

δargmaxd( ˆPd,i) − δargmaxd(Pd,i)

 + ϵ · LR
And the Laplacian remainder is:
LR =
nX
i=1

 ˆP (1) d,i

 + nX
i=1

 ˆP (2) d,i

 (14)
The term SL ( ˆPd,i, Pd,i) (with β = 0 .1) is used to com-
pute the error between the predicted outputs and the ground
truth targets. Here, ˆPd,i represents the predicted popularity
for data point i on day d, while Pd,i denotes the ground truth
popularity for the same data point. The differences between
the one-hot encoded predicted and true peak values are mea-
sured using δargmaxd( ˆPd,i) and δargmaxd(Pd,i), respec-
tively. Additionally, the term ϵ · LR introduces a Lapla-
cian remainder (LR) to provide further regularization. Dur-
ing training, the weights for the first-order and second-order

derivative terms, as well as the L1 loss weight between the
one-hot encodings (λ1, λ2, α), are adjusted dynamically us-
ing a cosine annealing algorithm to ensure smoother conver-
gence throughout the training process.
5. Experiments
In this section, we first describe the experiment settings
and evaluation metrics for training models and comparison.
Then various experimental results and detailed discussions
are provided including evaluations for SMTPD dataset, pro-
posed baseline, multi-modal features and early popularity.
5.1. Experiment settings
We implement our approaches using the Pytorch * frame-
work and train it with the Adam [25] optimizer incorporat-
ing L2 penalty of 10−3, while the batch size is set to 64.
The learning rate is initialized to 10−3 and adjusted by the
ReduceLROnPlateau scheduler provided by PyTorch when
one epoch is end. Supervised training was performed using
the Composite Gradient Loss (CGL) metioned before.
We introduce error-based metrics and correlation-based
metrics to fairly evaluate the compared datasets and mod-
els. We introduce the Absolute Error (MAE) and average
MAE (AMAE) to respectively evaluate models for single-
day prediction and temporal prediction. Assuming that the
daily MAE and average MAE are denoted as M AEd and
AM AE, they can be defined as:
M AEd = 1 n
nX
i=1

 ˆPd,i − Pd,i

 (15)
AM AE= 1 m
mX
d=1
M AEd (16)
where n denotes the total of samples and m denotes total of
days, while the Pd and ˆPd respectively denotes the ground-
truth popularity and predicted popularity for the day d.
For correlation-based metrics, we introduce the daily
SRC and the average SRC to evaluate the models for both
single-day prediction and temporal prediction from a differ-
ent perspective. Assuming n, m, Pd, and ˆPd are defined
consistently as mentioned earlier, the daily SRC and aver-
age SRC can be formulated as follows:
SRCd = 1 n − 1
nX
i=1
(
ˆPd,i − ¯ˆPd
σ ˆPd
)( Pd,i − ¯Pd
σPd
) (17)
ASRC = 1 m
mX
d=1
SRCd (18)
where ¯Pd and σPd are mean and standard deviation of the
corresponding popularity for the day d.
*https://pytorch.org
In the curves, sequential performance is represented by
the MAE and SRC metrics, which illustrate daily prediction
errors and correlations for popularity scores. The X-axis
denotes days, while the Y-axis shows M AEd or SRCd.
5.2. SMTPD VS. SMPD
In this subsection, we conduct comparisons and discussions
between the SMTPD and SMPD. We first measure three
most recently proposed state-of-the-art popularity predic-
tion methods on two datasets. As these methods are all
designed basing on the settings of SMPD, we make some
modifications to let them fit for training and testing on our
SMTPD. Other top-performing models (e.g. [44, 46, 50])
include components that are not applicable to SMTPD or
are not reproducible, such as sliding window average or
undisclosed self-trained modules. Hence, we do not dis-
cuss them in our experiments. First, we distribute content
from corresponding modalities into their respective feature
extraction modules. Then we use BERT-Multilingual as the
textual feature extractor to address the challenges of multi-
lingual text. Given that our SMTPD dataset consists of tem-
poral popularity scores, we restrict these methods to predict
only the single popularity score on day 30. To mitigate ran-
dom bias, we evaluate using 5-fold cross-validation.
Table 4 shows minimal performance differences across
folds, confirming that SMTPD contains abundant data un-
der a well-balanced sample distribution. It is evident that on
the single-output prediction of popularity on days 7, 14, and
30 within SMTPD, the performance of method [26] based
on GBDT outperforms the deep learning method [13] and
[52] in terms of both MAE and SRC through its powerful re-
gression capabilities of Catboost [39]. Notably, our method
achieves the best results with the addition of EP, where the
AMAE of the other three models increases as the prediction
horizon extends. In contrast, our model’s AMAE begins
to decrease after day 14. The deep learning method [13]
also performs well on days 7 and 14, but its effectiveness
declines beyond day 14.
Morever there are also two interesting observation. First,
all methods achieve higher SRC on SMTPD than on SMPD,
likely because SMPD lacks specific time points, making it
challenging to predict time-dependent popularity trends ac-
curately as popularity declines and their MAE performances
are certainly reduced that the MAE values increase by over
0.16. Besides, the larger popularity range and standard de-
viation among SMTPD samples (shown in Table 2) also
contributes to prediction difficulties.
5.3. Evaluation for Proposed Baseline
Refer to Table 3, we attempted to validate the rationale of
partial structures in the proposed baseline model by em-
ploying alternative feature extractors and regression net-
works. Using BERT-Base as the textual features extractor

lead to an increase of MAE by around 0.19. This decline
in performance may be caused by the limitations of BERT-
base model in handling multilingual texts, as it struggles to
effectively capture the semantics and contextual informa-
tion across different languages. The MAE also increased
when the MLP (3 layers) was used as the regression struc-
ture. Such a structure is similar to [13], suggesting that
MLP lacks the capture of temporal information. The SRC
did not change for either of the above substitutions, proba-
bly due to the high correlation given by EP.
5.4. Discussion of Early Popularity
We evaluate the performance of proposed baseline on
SMTPD.As shown in Table 5, the proposed baseline gets
a great improvement from existed methods that surpassing
the second best method by -0.798/0.109 MAE/SRC for pre-
dicting the popularity of day 30. This great improvement
is mainly brought by the early popularity (EP). Without the
assistant of EP (row 2 in Table 5), the baseline performance
sharply reduced around the existed methods.Using the EP
predicted by existed method (1.717/0.864 MAE/SRC) as an
input also contributes to the baseline’s performance (row 3
in Table 5).However the performance gap between the pre-
dicted EP and true EP remains large.
Instead of directly involving the EP in the model archi-
tecture, introducing EP in the training supervision is another
suitable option.To validate the effectiveness of such opera-
tion, we train a baseline model for predicting the populari-
ties from day 1 to 30. As it presented by the row 1 in Table
5, adding the 1st day’s popularity to the prediction sequence
make a slight boost, what is in line with the LSTM’s ability
to capture temporal dependencies in popularity sequences.
Having more preceding temporal information from back-
propagation leads to more precise predictions of popularity
in subsequent time steps.
These comparisons clearly indicate that EP plays a cru-
cial role in popularity prediction, and accurately forecasting
the first day’s popularity is key to predicting future popular-
ity. The strong correlation between EP and future popular-
ity significantly benefits the prediction task. Our results, as
demonstrated by the MAE and SRC curves for both natu-
ral EP and our model’s predictions, underscore the model’s
capability to leverage EP for enhanced accuracy. From the
BERT-Base BERT-Mul MLP LSTM AMAE ASRC
✓ ✓ 0.782 0.958
✓ ✓ 0.786 0.958
✓ ✓ 0.717 0.959
Table 3. The evaluation for the proposed baseline model, mainly
on evaluating the model’s performance in adapting to multilingual
and temporal popularity.
Method SMTPD (day 7) SMTPD (day 14) SMTPD (day 30)
A verage A verage A verage
Ding et al. [13] 1.715/0.849 1.669/0.846 1.592/0.843
w. EP 0.715/0.964 0.742/0.959 0.749/0.931
Lai et al. [26] 1.573/0.875 1.524/0.872 1.495/0.864
w. EP 0.725/0.957 0.753/0.962 0.760/0.957
Xu et al. [52] 1.895/0.817 1.832/0.818 1.743/0.820
w. EP 0.754/0.962 0.798/0.956 0.822/0.949
Ours w/o. EP 1.673/0.852 1.628/0.850 1.563/0.848
Ours 0.713/0.964 0.735/0.959 0.732/0.959
Table 4. The performance (MAE/SRC) was compared across four
models, including our model, using the SMTPD dataset, both with
and without EP.
Method AMAE ASRC MAE SRC
(day 30 only) (day 30 only)
w/o. EP(1-30) 1.562 0.856 1.530 0.850
w/o. EP(2-30) 1.630 0.849 1.551 0.849
w/o. EP+[26] 1.628 0.851 1.555 0.848
ours 0.717 0.959 0.732 0.959
Table 5. Assessment of EP across different scenarios. Here, ”1-
30” denotes the prediction target spanning a continuous sequence
from the 1st day to the 30th day, as does ”2-30” (to align with
methods having EP).
visualized results, tough EP exhibits high correlation to the
popularities of following days, the MAE sharply increased
over time. By contrast, our baseline model could well op-
timize the MAE and achieve even better SRC performance
comparing to the natural EP curve. Therefore, the proposed
baseline model is effective to utilize EP achieving better
prediction accuracy.
6. Conclusion
This study aims to address the challenge of time-series pop-
ularity prediction in social media. In this paper, we intro-
duce a novel multilingual, multi-modal time-series popu-
larity dataset based on YouTube and suggest a multilingual
temporal prediction model tailored to this dataset. Through
experiments, we demonstrate the effectiveness of this ap-
proach in predicting social media popularity time-series in a
multilingual environment. The experiments show that com-
bining multi-modal features with early popularity signifi-
cantly improves prediction accuracy. However, this study
has yet to address challenges such as multi-frame informa-
tion in videos, maximizing the use of language diversity,
and deeper multi-modal exploration. These areas will be
key focuses for our future work.

References
[1] Deepak Agarwal, Bee-Chung Chen, Pradheep Elango, Nitin
Motgi, Seung-Taek Park, Raghu Ramakrishnan, Scott Roy,
and Joe Zachariah. Online models for content optimiza-
tion. Advances in Neural Information Processing Systems ,
21, 2008. 1
[2] Sercan ¨O Arik and Tomas Pfister. Tabnet: Attentive inter-
pretable tabular learning. In Proceedings of the AAAI con-
ference on artificial intelligence, pages 6679–6687, 2021. 2
[3] Peng Bao, Hua-Wei Shen, Junming Huang, and Xue-Qi
Cheng. Popularity prediction in microblogging network: a
case study on sina weibo. In Proceedings of the 22nd in-
ternational conference on world wide web , pages 177–178,
2013. 1, 2
[4] Shenghua Bao, Guirong Xue, Xiaoyuan Wu, Yong Yu, Ben
Fei, and Zhong Su. Optimizing web search using social an-
notations. In Proceedings of the 16th international confer-
ence on World Wide Web, pages 501–510, 2007. 1
[5] Laura Ceci. Youtube-statistics & facts. Statista. com [on-
line].[cit. 2022-05-05]. Dostupn ´e z: https://www. statista.
com/topics/2019/youtube, 2022. 3
[6] Junhong Chen, Dayong Liang, Zhanmo Zhu, Xiaojing Zhou,
Zihan Ye, and Xiuyun Mo. Social media popularity predic-
tion based on visual-textual features with xgboost. In Pro-
ceedings of the 27th ACM International Conference on Mul-
timedia, pages 2692–2696, 2019. 2
[7] Tianqi Chen and Carlos Guestrin. Xgboost: A scalable tree
boosting system. In Proceedings of the 22nd acm sigkdd
international conference on knowledge discovery and data
mining, pages 785–794, 2016. 2
[8] Weilong Chen, Chenghao Huang, Weimin Yuan, Xiaolu
Chen, Wenhao Hu, Xinran Zhang, and Yanru Zhang. Title-
and-tag contrastive vision-and-language transformer for so-
cial media popularity prediction. In Proceedings of the 30th
ACM International Conference on Multimedia, pages 7008–
7012, 2022. 2
[9] Xiaolu Chen, Weilong Chen, Chenghao Huang, Zhongjian
Zhang, Lixin Duan, and Yanru Zhang. Double-fine-tuning
multi-objective vision-and-language transformer for social
media popularity prediction. In Proceedings of the 31st ACM
International Conference on Multimedia, pages 9462–9466,
2023. 2
[10] Wen-Huang Cheng, Sijie Song, Chieh-Yun Chen, Shin-
tami Chusnul Hidayati, and Jiaying Liu. Fashion meets com-
puter vision: A survey.ACM Computing Surveys (CSUR), 54
(4):1–41, 2021. 1
[11] Minhwa Cho, Dahye Jeong, and Eunil Park. Amps: Pre-
dicting popularity of short-form videos using multi-modal
attention mechanisms in social media marketing environ-
ments. Journal of Retailing and Consumer Services , 78:
103778, 2024. 2
[12] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina
Toutanova. Bert: Pre-training of deep bidirectional trans-
formers for language understanding. In Proceedings of the
2019 conference of the North American chapter of the asso-
ciation for computational linguistics: human language tech-
nologies, pages 4171–4186, 2019. 5
[13] Keyan Ding, Ronggang Wang, and Shiqi Wang. Social me-
dia popularity prediction: A multiple feature fusion approach
with deep neural networks. In Proceedings of the 27th ACM
International Conference on Multimedia, pages 2682–2686,
2019. 2, 7, 8
[14] Zhabiz Gharibshah and Xingquan Zhu. User response pre-
diction in online advertising. aCM Computing Surveys
(CSUR), 54(3):1–43, 2021. 1
[15] Anindya Ghose and Sha Yang. An empirical analysis of
search engine advertising: Sponsored search in electronic
markets. Management science, 55(10):1605–1622, 2009. 1
[16] Sayan Ghosh, Dylan Baker, David Jurgens, and Vinodkumar
Prabhakaran. Detecting cross-geographic biases in toxicity
modeling on social media. In Proceedings of the Seventh
Workshop on Noisy User-generated Text (W-NUT) , pages
313–328, 2021. 4
[17] Marcos Andr ´e Gonc ¸alves, Jussara M Almeida, Luiz GP dos
Santos, Alberto HF Laender, and Virgilio Almeida. On pop-
ularity in the blogosphere. IEEE Internet Computing, 14(3):
42–49, 2010. 1
[18] Edouard Grave, Piotr Bojanowski, Prakhar Gupta, Armand
Joulin, and Tomas Mikolov. Learning word vectors for 157
languages. In Proceedings of the International Conference
on Language Resources and Evaluation (LREC), 2018. 5
[19] Mohammad Hajarian, Mark Anthony Camilleri, Paloma
D´ıaz, and Ignacio Aedo. A taxonomy of online marketing
methods. In Strategic corporate communication in the digi-
tal age, pages 235–250. Emerald Publishing Limited, 2021.
1
[20] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun.
Deep residual learning for image recognition. In Proceed-
ings of the IEEE conference on computer vision and pattern
recognition, pages 770–778, 2016. 5
[21] Sepp Hochreiter and J ¨urgen Schmidhuber. Long short-term
memory. Neural computation, 9(8):1735–1780, 1997. 6
[22] Chih-Chung Hsu, Chia-Ming Lee, Xiu-Yu Hou, and Chi-Han
Tsai. Gradient boost tree network based on extensive feature
analysis for popularity prediction of social posts. InProceed-
ings of the 31st ACM International Conference on Multime-
dia, pages 9451–9455, 2023. 2
[23] Guolin Ke, Qi Meng, Thomas Finley, Taifeng Wang, Wei
Chen, Weidong Ma, Qiwei Ye, and Tie-Yan Liu. Lightgbm:
A highly efficient gradient boosting decision tree. Advances
in neural information processing systems, 30, 2017. 2
[24] Aditya Khosla, Atish Das Sarma, and Raffay Hamid. What
makes an image popular? In Proceedings of the 23rd in-
ternational conference on World wide web , pages 867–876,
2014. 3
[25] Diederik P Kingma and Jimmy Ba. Adam: A method for
stochastic optimization. In Proceedings of the 3rd Interna-
tional Conference on Learning Representations(ICLR),San
Diego,California,USA,May 7-9, 2015. 7
[26] Xin Lai, Yihong Zhang, and Wei Zhang. Hyfea: Winning
solution to social media popularity prediction for multime-
dia grand challenge 2020. In Proceedings of the 28th ACM
International Conference on Multimedia, pages 4565–4569,
2020. 2, 7, 8

[27] Chenyu Li, Jun Liu, and Shuxin Ouyang. Analysis and
prediction of content popularity for online video service: a
youku case study. China Communications, 13(12):216–233,
2016. 3
[28] Jinning Li, Yirui Gao, Xiaofeng Gao, Yan Shi, and Guihai
Chen. Senti2pop: sentiment-aware topic popularity predic-
tion on social media. In 2019 IEEE International conference
on data mining (ICDM), pages 1174–1179. IEEE, 2019. 2
[29] Junnan Li, Ramprasaath Selvaraju, Akhilesh Gotmare,
Shafiq Joty, Caiming Xiong, and Steven Chu Hong Hoi.
Align before fuse: Vision and language representation learn-
ing with momentum distillation. Advances in neural infor-
mation processing systems, 34:9694–9705, 2021. 2
[30] Yury Lifshits. Ediscope: Social analytics for online news.
Yahoo Labs, 2010. 1
[31] Hung-Hsiang Lin, Jiun-Da Lin, Jose Jaena Mari Ople, Jun-
Cheng Chen, and Kai-Lung Hua. Social media popularity
prediction based on multi-modal self-attention mechanisms.
IEEE Access, 10:4448–4455, 2022. 2
[32] An-An Liu, Xiaowen Wang, Ning Xu, Junbo Guo, Guo-
qing Jin, Quan Zhang, Yejun Tang, and Shenyuan Zhang. A
review of feature fusion-based media popularity prediction
methods. Visual Informatics, 2022. 2
[33] Marco Lui and Timothy Baldwin. langid.py: An off-the-
shelf language identification tool. In Proceedings of the ACL
2012 System Demonstrations, pages 25–30, 2012. 6
[34] Shijian Mao, Wudong Xi, Lei Yu, Gaotian L ¨u, Xingxing
Xing, Xingchen Zhou, and Wei Wan. Enhanced catboost
with stacking features for social media prediction. In Pro-
ceedings of the 31st ACM International Conference on Mul-
timedia, pages 9430–9435, 2023. 2
[35] Masoud Mazloom, Robert Rietveld, Stevan Rudinac, Marcel
Worring, and Willemijn Van Dolen. Multimodal popularity
prediction of brand-related social media posts. In Proceed-
ings of the 24th ACM international conference on Multime-
dia, pages 197–201, 2016. 2
[36] Tomas Mikolov, Kai Chen, Greg Corrado, and Jeffrey Dean.
Efficient estimation of word representations in vector space.
In Proceedings of the 1st International Conference on Learn-
ing Representations(ICLR),Scottsdale,Arizona,USA,May 2-
4, 2013. 5
[37] Alessandro Ortis, Giovanni Maria Farinella, and Sebastiano
Battiato. Prediction of social image popularity dynamics.
In Image Analysis and Processing–ICIAP 2019: 20th Inter-
national Conference, Trento, Italy, September 9–13, 2019,
Proceedings, Part II 20, pages 572–582. Springer, 2019. 3
[38] Jeffrey Pennington, Richard Socher, and Christopher D Man-
ning. Glove: Global vectors for word representation. In
Proceedings of the 2014 conference on empirical methods in
natural language processing (EMNLP) , pages 1532–1543,
2014. 5
[39] Liudmila Prokhorenkova, Gleb Gusev, Aleksandr V orobev,
Anna Veronika Dorogush, and Andrey Gulin. Catboost: un-
biased boosting with categorical features. Advances in neu-
ral information processing systems, 31, 2018. 7
[40] C ´edric Richier, Eitan Altman, Rachid Elazouzi, Tania Alt-
man, Georges Linares, and Yonathan Portilla. Modelling
view-count dynamics in youtube. CoRR, abs/1404.2570,
2014. 2
[41] Cedric Richier, Eitan Altman, Rachid Elazouzi, Tania
Jimenez, Georges Linares, and Yonathan Portilla. Bio-
inspired models for characterizing youtube viewcout. In
2014 IEEE/ACM International Conference on Advances in
Social Networks Analysis and Mining (ASONAM) , pages
297–305. IEEE, 2014. 1, 2
[42] Satoshi Sanjo and Marie Katsurai. Recipe popularity predic-
tion with deep visual-semantic fusion. In Proceedings of the
2017 ACM on Conference on Information and Knowledge
Management, pages 2279–2282, 2017. 1, 2
[43] Gabor Szabo and Bernardo A Huberman. Predicting the pop-
ularity of online content. Communications of the ACM , 53
(8):80–88, 2010. 1, 2
[44] YunPeng Tan, Fangyu Liu, BoWei Li, Zheng Zhang, and Bo
Zhang. An efficient multi-view multimodal data processing
framework for social media popularity prediction. In Pro-
ceedings of the 30th ACM International Conference on Mul-
timedia, pages 7200–7204, 2022. 2, 7
[45] Alexandru Tatar, Marcelo Dias De Amorim, Serge Fdida,
and Panayotis Antoniadis. A survey on predicting the popu-
larity of web content. Journal of Internet Services and Ap-
plications, 5(1):1–20, 2014. 1
[46] Kai Wang, Penghui Wang, Xin Chen, Qiushi Huang, Zhen-
dong Mao, and Yongdong Zhang. A feature generalization
framework for social media popularity prediction. In Pro-
ceedings of the 28th ACM International Conference on Mul-
timedia, pages 4570–4574, 2020. 2, 7
[47] Bo Wu, Wen-Huang Cheng, Yongdong Zhang, Qiushi
Huang, Jintao Li, and Tao Mei. Sequential prediction of so-
cial media popularity with deep temporal context networks.
In Proceedings of the 26th International Joint Conference on
Artificial Intelligence (IJCAI), pages 3062–3068, 2017. 1, 2
[48] Bo Wu, Wen-Huang Cheng, Peiye Liu, Bei Liu, Zhaoyang
Zeng, and Jiebo Luo. Smp challenge: An overview of social
media prediction challenge 2019. In Proceedings of the 27th
ACM International Conference on Multimedia, pages 2667–
2671. ACM, 2019. 1, 2, 3
[49] Bo Wu, Peiye Liu, Wen-Huang Cheng, Bei Liu, Zhaoyang
Zeng, Jia Wang, Qiushi Huang, and Jiebo Luo. Smp chal-
lenge: An overview and analysis of social media prediction
challenge. In Proceedings of the 31st ACM International
Conference on Multimedia, pages 9651–9655, 2023. 2
[50] Jianmin Wu, Liming Zhao, Dangwei Li, Chen-Wei Xie,
Siyang Sun, and Yun Zheng. Deeply exploit visual and lan-
guage information for social media popularity prediction. In
Proceedings of the 30th ACM International Conference on
Multimedia, pages 7045–7049, 2022. 2, 7
[51] Leilei Wu, Lingling Yi, Xiao-Long Ren, and Linyuan L ¨u.
Predicting the popularity of information on social platforms
without underlying network structure. Entropy, 25(6):916,
2023. 2
[52] Kele Xu, Zhimin Lin, Jianqiao Zhao, Peicang Shi, Wei Deng,
and Huaimin Wang. Multimodal deep learning for social
media popularity prediction with attention mechanism. In
Proceedings of the 28th ACM International Conference on
Multimedia, pages 4580–4584, 2020. 2, 7, 8

[53] Jaewon Yang and Jure Leskovec. Patterns of temporal varia-
tion in online media. InProceedings of the fourth ACM inter-
national conference on Web search and data mining , pages
177–186, 2011. 1, 2
[54] Zhizhen Zhang, Xiaohui Xie, Mengyu Yang, Ye Tian, Yong
Jiang, and Yong Cui. Improving social media popular-
ity prediction with multiple post dependencies. CoRR,
abs/2307.15413, 2023. 2
[55] Alireza Zohourian, Hedieh Sajedi, and Arefeh Yavary. Popu-
larity prediction of images and videos on instagram. In 2018
4th International Conference on Web Research (ICWR) ,
pages 111–117, 2018. 3
