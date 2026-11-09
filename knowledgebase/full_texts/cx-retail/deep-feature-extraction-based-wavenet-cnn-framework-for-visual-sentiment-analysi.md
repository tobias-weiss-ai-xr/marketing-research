---
title: Deep feature extraction based WaveNet CNN framework for visual sentiment analysis
url: https://doi.org/10.1007/s44163-026-02185-0
category: cx-retail
subcategory: framework
date: 2026-09
venue: Discover Artificial Intelligence
authors:
- Siddhi Kadu
- Bharti Joshi
- Pratik K. Agrawal
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1007/s44163-026-02185-0.pdf
pages: 28
chars: 80154
fetched_at: '2026-11-08T18:48:00+00:00'
kb_version: 1
---

# Deep feature extraction based WaveNet CNN framework for visual sentiment analysis

RESEARCH Open Access
Discover Artificial IntelligenceKadu et al. Discover Artificial Intelligence          (2026) 6:1266
https://doi.org/10.1007/s44163-026-02185-0
Deep feature extraction based WaveNet CNN
framework for visual sentiment analysis
Siddhi Kadu1*, Bharti Joshi1 and Pratik Agrawal2*
  * C o r r e s p o n d e n c e :
Siddhi Kadu
siddhi.k1121989@gmail.com
Pratik Agrawal
pratik.agrawaal@gmail.com; Pratik.
agrawal@sitnagpur.siu.edu.in
1Computer Engineering
Department, Ramrao Adik Institute
of Technology, D Y Patil Deemed to
be University, Nerul, Navi Mumbai,
Maharashtra 400706, India
2Symbiosis Institute of Technology,
Nagpur Campus, Symbiosis
International(Deemed University),
Pune, India
© The Author(s) 2026. Open Access  This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International
License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate
credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material.
You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party
material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material
is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted
use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit  h t t p :  / / c r e a  t i v e c  o m m o  n s . o r g / l i c e n s
e s / b y - n c - n d / 4 . 0 /     .
Abstract
The rise of internet reviews, driven by smartphone use, has led to a trend of
incorporating images in feedback on platforms like Yelp, TripAdvisor, and Google.
This research shifts focus from traditional textual sentiment analysis (SA) to visual
sentiment analysis (VSA), particularly in the restaurant domain, where images of food,
ambiance, and facial expressions significantly influence user perception. People often
check reviews before selecting a restaurant for dining. Reviewers frequently post
restaurant images with the purpose of reviewing them in order to classify the polarity
of sentiment depending on factors such as face expressions, food presentation, or
ambiance. Therefore, this research focuses on analyzing images to classify them in
neutral, negative, or positive sentiment categories. This study addresses limitations
in existing VSA approaches, particularly in extracting and selecting discriminative
features for accurate sentiment classification. The framework processes images
through a combination of a custom convolutional neural network (CNN) and an
optimal wavelet transform, utilising spatial and frequency features. To optimise
feature selection, a dual-moth flame optimization (DMFO) algorithm is employed,
followed by an ensemble classifier for sentiment prediction. The proposed approach
achieves an impressive accuracy of 75.15%, 87.42% and 89.72% on the FER2013,
JAFFE and restaurant review datasets, respectively, outperforming existing methods.
The results demonstrate the effectiveness of combining multi-domain features with
optimized selection techniques. This framework can support real-world applications
such as restaurant decision-making, customer experience analysis, and automated
review understanding.
Keywords Reviews, Visual sentiment analysis, Feature extraction, Feature selection,
Ensemble classifier
 1 Introduction
Due to rise of smartphones these days, people have started posting reviews through
images and videos as well. Online review becomes key for sentiment analysis(SA). Con -
sidering that 60% of readers choose content enriched with images and more than 70% of
social media posts are visual, there is an emerging need to develop strong techniques for
extracting sentiment from images. Expressions, aesthetics, and even context play a huge
role in shaping public perception and decision making, thereby making excellent visual

Page 2 of 28
Kadu et al. Discover Artificial Intelligence           (2026) 6:1266
sentiment analysis (VSA) techniques crucial. For example, people will check Amazon
reviews for any given product before making a decision on the best product to meet their
particular needs. Similarly, before choosing a place to go eat, that person will check Yelp,
TripAdvisor, and Google. SA is an area of AI and NLP , which categorizes the reviews
as positive, negative, or neutral according to their capability of actually reflecting the
experiences of past consumers. More precisely, by finding the consumer-expressed sen -
timent, the experience will be spotted—whether pleasant, negative, or neutral—about
the review [ 1]. Sentiment inference is a fundamental task in the review analysis, as it
indicates customer preferences and strengths/flaws of products. This information is ben-
eficial for recommendations, product design, marketing, and similar applications. In the
nascent stages of the Web, when online reviews became available, most material on the
web was textual. The current web is rich in visual content. It allows customers to express
their views in ways that words cannot tell. For example, more and more users started
commenting on restaurants by adding images to the reviews. Image sentiment analysis
solves this problem since it assesses non-verbal cues such as facial expressions, food pre-
sentation, or ambiance to give a more complete grasp of customer feedback [2]. This will
really assist restaurant managers in tracking customers’ feedback in real time. By identi -
fying and categorizing sentiments expressed in images of reviews, enterprises will be in a
position where they can easily detect trends or issues, such as negative reviews regarding
certain menu items or poor decor, thus enabling timely responses aimed at solving these
issues. This kind of monitoring enhances electronic word-of-mouth (eWOM) manage -
ment, which has become an intrinsic function in the hospitality business given the com -
petitive nature of this business [ 3]. Most of the existing systems for VSA, focused on a
few feature dimensions, usually spatial features from a CNN. Generally, these work for
detecting objects and textures but most of those spatial features do not capture the finer
details, such as color variations or subtle nuances in texture or pattern, which may be
prominent in the frequency domain. Furthermore, these models often ignore the impor-
tance of integrating feature selection to provide optimized feature sets, thereby produc -
ing redundant or non-informative features. This particular set of limitations to increase
computational complexity and bring down the overall efficiency and performance of the
model when crossed onto any varied set of visual datasets [ 4, 5]. The paper fills this gap
by presenting a novel system, for VSA which combines custom CNN for the extraction
of features in the spatial domain and optimal wavelet transform for frequency-based
feature extraction named WaveNet-CNN. Feature selection is done for further optimi -
zation of the concatenated feature set using Dual Moth Flame Optimization algorithm
(DMFO), an enhanced variant of the Moth Flame Optimization algorithm (MFO). This
ensures that only the most relevant features will be retained to improve accuracy with
computational efficiency. In order to further classify the sentiments as positive, negative,
or neutral, the selected feature set is fed into the ensemble classifier consisting of using
Naive Bayes (NB), K-Nearest Neighbour (KNN), Support Vector Machine (SVM), Deep
Forest (DF), and Logistic Regression (LR). After that, a dataset consisting of restaurant
reviews is used to conduct extensive tests in order to ascertain the effectiveness of the
proposed approach. Here are our system’s primary contributions:
  • To create a feature extraction mechanism, WaveNet-CNN uses custom CNN for
spatial feature extraction and the optimal wavelet transform for frequency based

Page 3 of 28
Kadu et al. Discover Artificial Intelligence           (2026) 6:1266
feature extraction. This makes sure that fine-grained details related to sentiment are
captured.
  • For feature selection, DMFO is incorporated which ensures a high degree of
discriminant factors and no redundancy by evaluating and choosing the appropriate
feature subsets using both intraclass and interclass variance.
  • An ensemble classification pipeline is developed which uses NB, KNN, SVM, DF, and
LR classifiers, with the aim of improving sentiment prediction accuracy and model
robustness by combining the strengths of multiple classifiers.
  • The dataset of restaurant review images is collected from Yelp, TripAdvisor, and
Google reviews to conduct the necessary experiments for validating our proposed
VSA model, V-SentimentNet.
This study is organized into six sections, which are highlighted in the following divisions.
The previously reported research on VSA is reviewed in Sect.  2. Details of the suggested
strategy are given in Sect.  3. The data from the experiment are shown in Sect.  4, along
with an analysis of the findings. The conclusion, along with some recommendations for
future research, is discussed in Sect. 5.
2 Literature review
Recent years have yielded advances in image-based SA, leading to the development
of various methodologies focused on evaluating emotions in content disseminated
throughout social media platforms. Despite increasing popularity, these models persis -
tently exhibit issues related to performance consistency and classification accuracy. To
address these limitations, researchers have proposed many ways to improve the accuracy
of sentiment analysis in visual data. This section examines these techniques, particularly
their application in restaurant review analysis, food image classification and the emo -
tional interpretation of user-generated content. This study [6] uses the improved variant
of CNN Inception-v3 and auxiliary features to improve general performance in classify -
ing images in the dataset, including FER2013 and JAFFE. In another [ 7], the extraction
of artificial features with a Gabor filter is combined with an evolutionary algorithm to
optimize the SVM hyperparameters with genetic algorithms. This means that relatively
high classification accuracies are achieved (94.20% on the CK dataset and 94.26% on
the CK+ dataset). In a different study [ 8], the DCNN-based model with an underlying
architecture called AlexNet is implemented to differentiate among various emotional
states and the result obtained is 93.66% average accuracy of the data in the CK and CK +
datasets, establishing the success of deep architectures in image sentiment classification.
Moreover, the HERO model [ 9], as one of the CNN-based hybrid ensembles, incorpo -
rates three separate sub-networks into a unified framework to enhance the process of
emotion recognition.
The work examines how two pertinent CNN hyperparameters (i.e., filter sizes and net-
work depth) affect classification in the FER-2013 dataset. With the help of these experi -
ments, the best combinations achieve optimization that could increase the accuracy
of emotion detection. A different research [ 10] presents specially adapted CNN mod -
els that are best suited for visual sentiment analysis. These models focus on combining
the features of a product image with the textual metadata and provide a complete com -
prehension of the consumer sentiment. The aim of such multimodal approaches is to

Page 4 of 28
Kadu et al. Discover Artificial Intelligence           (2026) 6:1266
provide solutions to the drawbacks of traditional text-only sentiment systems that can -
not grasp the richness of the visual content.
The field of image SA continues to encounter notable challenges from existing image
representation methods, ML classifiers and fusion techniques. The models depend on
basic representations, which include raw pixel values and handcrafted features, because
these methods cannot effectively identify the emotional and contextual details that exist
in visual data [ 11, 12]. Many systems today employ traditional classifiers that use com -
plete connection layers although these systems function effectively most of the time but
they cannot match the expressive capabilities of deep learning model. The models expe -
rience difficulty in representing complex relationships between elements of visual senti -
ment analysis because these models fail to comprehend the needed interdependencies
[13–15]. Another prominent issue lies in integrating diverse visual descriptors extracted
using techniques for feature extraction. Several transform-domain methods have been
performed, namely the Discrete Cosine Transform (DCT), Wavelet Transform (WT),
Fourier Transform (FT), and Convolution Transform (CT). Most current solutions do
not use good methods to combine these different features, greatly affecting their ability
to classify accurately and reducing how well they can tell things apart [16–19].
The RA-DLNet deep model applies residual attention modeling methods to analyze
emotions in images and has a deep convolutional structure in Ref. [ 19]. The remaining
attention layers allow the model to focus on areas of the image that are rich in emotion,
making it easier to interpret and more precise. The architecture was assessed on eight
benchmarks with art-image and social media image sets. The results revealed that the
RA-DLNets performed better than the baseline CNNs (VGG-16, VGG-19, ResNet-50,
Inception-V3 and Xception), and were able to generate an accurate sentiment analysis of
89–90% in Twitter-based sentiment data. In this strategy [ 20], a pretrained ResNet50 is
used to extract early image highlights, which are classified at that point using a gradient
boost ensemble technique. The method was tested using two sets that included emo -
tional images labeled: CrowdFlower and GAPED. The model demonstrated robust per -
formance, achieving scores of up to 98% in GAPED and 87% on CrowdFlower, utilizing
the most advanced indicators available in the field.
Recent studies have shown, in a kind of general sense, the effectiveness of transformer-
based architectures for visual sentiment analysis, and well, you can see why. The [ 21]
model introduces an enhanced effective region and context-aware vision transformer,
which, kind of, at the same time, grabs the most salient emotional areas and also the
broader context cues. That combo helps with image sentiment recognition, more accu -
rately than before, or at least that’s the claim. Likewise, [ 22] takes advantage of Swin
Transformer’s hierarchical feature extraction. This helps it model both local and more
global visual dependencies, which ends up boosting sentiment classification perfor -
mance in practice. For multimodal sentiment analysis, [ 23] uses a pre-trained CLIP
model, but with dynamic prompt optimization. On top of that, it applies cross-modal
contrastive learning so the visual and textual parts align in a more meaningful semantic
way. The outcome is enhanced multimodal sentiment prediction, with better agreement
across modalities. And also, the [ 24] model brings dependency-guided large language
model techniques to improve aspect-level sentiment analysis while still offering inter -
pretable explanations tied to the sentiment outputs. That interpretable layer, it seems,
makes the whole thing less of a black box, somehow.

Page 5 of 28
Kadu et al. Discover Artificial Intelligence           (2026) 6:1266
Table 1 show that the authors used methods that only considered spatial features using
CNN and the lack of feature selection techniques.
Optimization methods have now become essential for improving the performance of
an SA model. These methods, particularly selection methods, can reduce redundancy in
feature representation to enhance generalization of the model and select features that
are highly relevant for improving classification accuracy from high-dimensional data.
The authors are utilizing nature-inspired algorithms to boost the performance of visual
analysis systems. These algorithms are utilized for the purpose of feature extraction from
images, in an effort to identify a subset of pertinent characteristics that contribute to
more accurate picture classification or analysis [29] [30].
The above literature survey, emphasizes the limitations of existing models that focus
solely on techniques such as CNN and it variants i.e. only the spatial features. Few
researchers combined the CNN with wavelet transform. While some models show
improvements in accuracy through advanced architectures, the absence of compre -
hensive feature extraction methods and robust feature selection mechanisms lim -
its their overall performance and scalability. This highlights the need for more holistic
approaches that integrate both spatial and frequency domain features along with effec -
tive feature selection techniques to enhance the precision, generalization, and computa -
tional efficiency of SA models in real-world applications.
3 Proposed methodology
This section introduces the proposed system for VSA to enhance the accuracy and gen -
eralizability by integrating both spatial and frequency domain features, followed by
optimal feature selection and ensemble-based classification. Figure  1 below explains the
framework designed to classify the sentiment of restaurant review images into positive,
negative, or neutral categories.
Table 1 Summary of image sentiment analysis techniques and limitations
References Algorithm used Dataset used Feature
selection
method
Limitations
 [25] Deep CNN Disaster images None Limited generalization to real-world
scenarios; lacks feature selection
 [26] Weakly Super-
vised Coupled
Networks
Flickr and
Instagram
None Weak supervision results in lower
accuracy in noisy real-world data
 [27] CNN Review images Item and
User-Oriented
CNN
Higher computational cost, lacks
advanced feature selection
 [1] DCNN Restaurant Review
Images
None No feature selection; generalization
issues with unstructured data
 [6] Inception-
V3 (Transfer
Learning)
FER2013, JAFFE None High computational cost; limited
interpretability
 [8] Deep CNN FER2013, JAFFE None Performance depends on gradient
features; sensitive to noise
 [28] Gabor Filters +
CNN
Custom Social
Media Dataset
None High processing cost; scalability
issues in real-time deployment
 [16] Wavelet + SVM,
KNN
CK+, JAFFE None SWT alone may miss relevant fea-
tures; poor large-scale performance
 [17] DWT + Deep CNN Custom Multi-
focus dataset
None Complex fusion; high computation;
tuning required

Page 6 of 28
Kadu et al. Discover Artificial Intelligence           (2026) 6:1266
3.1 Pre-processing
Pre-processing was applied uniformly to all images, including resizing to 224 × 224 pix-
els and normalization of pixel values to the range [0, 1]. This preprocessed image was
further processed for feature extraction.
3.2 Feature extraction
A novel WaveNet-CNN model is proposed that extracts intricate visual features from
images, which involves concatenation of features obtained from custom CNN and an
optimal wavelet transform. The feature vector obtained is an integrated feature that
accurately captures both the spatial and frequency properties of images. Frequency fea -
tures capture finer details, such as texture smoothness and color gradients, which are
crucial to understanding more subtle visual cues, such as ambiance or food texture, in
restaurant reviews. This makes sentiment classification more accurate, more resistant to
image differences and more efficient, which improves the performance of systems that
use SA.
3.2.1 Custom CNN model
Initially, the image is passed to custom CNN and the mathematical Eqs. 1–6 are given
below.
Image
Preprocessing
Optimal
Wavelet
Transform
Feature
conactenation
Image Feature
Vector
Customi-
zed CNN
Image Feature
Extraction
Image Dataset
Dual Moth Flame
Optimization
Ensemble
Classification Model
Sentiment
Predicted
KNNNB
LR
SVM
DF
Feature Selection
WaveNet-CNN
Fig. 1 Proposed visual sentiment analysis system

Page 7 of 28
Kadu et al. Discover Artificial Intelligence           (2026) 6:1266
(1) Convolution operation

Z(f ) u,v =
P∑
p=1
Q∑
q=1
D∑
d=1
I(d) u+p,v+q · K(d,f ) p,q + δ(f ) (1)
where:
  • I(d) u+p,v+q is the input image value at channel d and location (u + p, v + q),
  • K(d,f ) p,q  is the filter weight at channel d and position (p, q) for filter f,
  • δ(f ) is the bias term for filter f,
  • Z(f ) u,v  is the output of the convolution at location (u, v) for filter f.
(2) Batch normalization

ˆz = z − µB√
σ2 B + ε , ˜z = α · ˆz + β (2)
where:
  • µB  and σ2 B  are the mean and variance of the batch,
  • ε is a small constant for numerical stability,
  • α and β are learnable scaling and shifting parameters,
  • ˜z  is the normalized output.
(3) ReLU activation
 ϕ(z) = max(0 ,z ) (3)
(4) Max pooling

M (f ) u,v = max (p,q)∈R Z(f ) u+p,v+q (4)
where R denotes the pooling region, typically 2 × 2.
(5) Global average pooling (GAP)

gf = 1 H · W
H∑
u=1
W∑
v=1
M (f ) u,v  (5)
where H and W are the height and width of the feature map.
(6) Flattening operation
 G =[ g1,g 2,...,g F ] (6)
where G is the final flattened feature vector used for classification.
The CNN architecture shown in Table 2 which consists of six convolutional layers,
each followed by batch normalization and a ReLU activation function. These are essen -
tial to ensure stability and non-linearity. The convolutional blocks gradually increase
their filter count from 32 to 512 so that they can capture low-level (e.g., edges, textures)
and high-level (e.g., semantic) features. Each of these convolutional blocks is followed by
a MaxPooling layer to down-sample the feature maps and thus reduce spatial dimension
and computational complexity, while at the same time retaining most of the information.

Page 8 of 28
Kadu et al. Discover Artificial Intelligence           (2026) 6:1266
After the last convolutional layer comes the GAP operation, which condenses one fea -
ture map into one number, forming a very compact representation of size 512 × 1 ×
1. This result is then flattened to a 512-dimensional feature vector. The depth architec -
ture of the first-order hierarchy, together with normalization and pooling procedures,
ensures efficient learning of features with fewer parameters and yields better generaliza -
tion. Custom CNN draws inspiration from both architectures, preserving VGG’s sim -
plicity and incorporating ResNet’s optimization efficiency, while minimizing overfitting
by using fewer convolutional layers, batch normalization and GAP instead of bulky fully
connected layers.
3.2.2 Optimal wavelet transform model
Similarly, now the image is passed to a biorthogonal wavelet, one of the wavelet types of
the discrete wavelet transform (DWT), which is a powerful signal and image processing
technique that decomposes data into different frequency components across multiple
resolutions. It uses filter banks comprising low-pass and high-pass filters to separate
an image into subbands such as approximation (LL) and detail components (LH, HL,
HH).There are various types of wavelet that can be used within DWT, including Haar,
Daubechies, Symlets, Coiflets and Biorthogonal wavelets. Among them, biorthogonal
wavelets preserve the structural properties of organizers in objects such as edges, con -
tours and textures. The ability to retain linearity allows the extraction of discriminative
multi-resolution features that represent smooth regions as well as crisp details of high-
frequency components. These rich feature representations offer a more capable input for
the subsequent classification steps in image-based sentiment analysis, thus improving
the performance of image-based sentiment analysis systems. This type of wavelet has
two sets of wavelet functions called analysis and synthesis. The analysis function is used
to extract the features and the synthesis is used to rebuild the original features. As we
need to only extract features, we use only the analysis function. Filter banks are the fun -
damental components of wavelet transforms, consisting of a low-pass filter (LPF) and a
high-pass filter (HPF). Each of these filters is defined by a specific set of numerical coef -
ficients that determine how the input signal or image is decomposed into approximation
and detail components. Popular biorthogonal wavelets include bior1.3, bior2.2, bior3.3,
Table 2 Layer-wise summary of the proposed CNN architecture
Layer type Details / Parameters Output shape Activation
Input RGB image input [3, 224, 224] –
conv1 + bn1 Conv2d + BatchNorm, in: 3 → 32, kernel: 3 × 3, padding=1 [32, 224, 224] ReLU
maxpool MaxPool2d, kernel: 2 × 2, stride: 2 [32, 112, 112] –
conv2 + bn2 Conv2d + BatchNorm, in: 32 → 64, kernel: 3 × 3, padding=1 [64, 112, 112] ReLU
maxpool MaxPool2d, kernel: 2 × 2, stride: 2 [64, 56, 56] –
conv3 + bn3 Conv2d + BatchNorm, in: 64 → 128, kernel: 3 × 3, padding=1 [128, 56, 56] ReLU
maxpool MaxPool2d, kernel: 2 × 2, stride: 2 [128, 28, 28] –
conv4 + bn4 Conv2d + BatchNorm, in: 128 → 256, kernel: 3 × 3, padding=1 [256, 28, 28] ReLU
maxpool MaxPool2d, kernel: 2 × 2, stride: 2 [256, 14, 14] –
conv5 + bn5 Conv2d + BatchNorm, in: 256 → 512, kernel: 3 × 3, padding=1 [512, 14, 14] ReLU
maxpool MaxPool2d, kernel: 2 × 2, stride: 2 [512, 7, 7] –
conv6 + bn6 Conv2d + BatchNorm, in: 512 → 512, kernel: 3 × 3, padding=1 [512, 7, 7] ReLU
maxpool MaxPool2d, kernel: 2 × 2, stride: 2 [512, 3, 3] –
global_avg_pool AdaptiveAvgPool2d, Output size = 1 × 1 [512, 1, 1] –
flatten Remove spatial dimensions [512] –

Page 9 of 28
Kadu et al. Discover Artificial Intelligence           (2026) 6:1266
bior4.4 and bior6.8, each differing in filter length, vanishing moments and smoothness.
In order to reduce computational complexity while maintaining high-quality feature
extraction, the HPF and LPF filter coefficients are altered in the analysis stage. Unlike
the more conventional wavelet transforms, like daubechies and biorthogonal wavelets,
which normally rely on fixed, predefined filter coefficients, the proposed Optimal Wave -
let Filter Bank (OWFB) does things a bit differently; it uses customized analysis low-pass
and high-pass filters that are tuned specifically for visual sentiment analysis.
The proposed OWFB employs only the analysis filter bank for feature extraction,
where the input image is decomposed into approximation and detail sub-bands using
the analysis LPF and HPF. The analysis HPF is derived from the corresponding LPF
according to Eq. 7
 ˜M (n)=( −1)nf (len − 1 − n) (7)
where f(n) represents the analysis LPF coefficients and len denotes the filter length. The
analysis LPF is mathematically represented as Eq. 8
 M (i)=
(
1+ i−1)v ( 1+ y1i−1 + y2i−2 + ··· + yv−1i−(v−1) )  (8)
where v denotes the number of vanishing moments that control the regularity and fre -
quency selectivity of the wavelet filter bank. In other words, those tailored filter coef -
ficients help lift the sentiment-linked texture, edge, and structural cues more effectively,
while still keeping the multi-resolution feel that wavelet transforms are known for. As a
result, OWFB tends to yield more discriminative frequency-domain features compared
to the usual wavelet methods, and that ends up improving how restaurant review images
get represented for sentiment classification. This improved wavelet is an optimal wavelet
transform and the coefficients altered for filter banks for the vanishing moments v = 2, 4
and 6 as the optimal wavelet filter bank (OWFB) are mentioned below.
  • At v=2,
 AnalysisLP F  = [− 66, 115, 425, 247]/512;
 AnalysisHPF  = [− 247, 425, − 115, − 66]/512;
  • At v=4,
 AnalysisLP F  = [− 10/1024, 17/512, 63/2048, − 383/2048, − 57/2048, 1292/2048,
1460/2048, 470/2048];
 AnalysisHPF  = [ − 470/2048, 1460/2048, − 1292/2048, − 57/2048, 383/2048,
63/2048, − 17/512, − 10/1024];
  • At v=6,
 AnalysisLP F  = [− 2, 10, 1, − 66, 58, 208, − 272, − 472, 660, 1572, 1036, 232]/2048;
 AnalysisHPF  = [− 232, 1036, − 1572, 660, 472, − 272, − 208, 58, 66, 1, − 10, − 2]/2048;
These are the values altered and used for feature extraction.
The customized analysis filter coefficients were obtained by minimizing the Canoni -
cal Signed Digit (CSD) representation while preserving the fundamental properties of
orthogonal wavelet filter banks. The optimization objective is expressed as

Ymod = min k
∑
k
YCSD(Mv (k)) (9)

Page 10 of 28
Kadu et al. Discover Artificial Intelligence           (2026) 6:1266
where YCSD  represents the arithmetic complexity of the filter coefficients and Mv (k)
denotes the analysis filter coefficients corresponding to the vth vanishing moment. This
optimization minimizes the number of arithmetic operations required during feature
extraction while preserving the discriminative capability of the extracted frequency-
domain features.
The custom filter coefficients were put together while still aiming to honor the core
properties of wavelet filter banks, like multi-resolution decomposition, frequency selec -
tivity, and accurate signal reconstruction. In particular, a few different filter setups were
tested, each tied to vanishing moments of 2, 4, and 6, experimentally and quite deliber -
ately too. As the number of vanishing moments goes up, the wavelet transform tends
to become better at capturing those smoother image areas, and at the same time it can
reduce noise quite well but without washing out the meaningful edge cues. From the
experimental checks, the OWFB6 option ended up offering the nicest trade-off between
feature discriminability and computational efficiency, so it was picked for the framework
that was proposed here.
After obtaining features from the custom CNN, the features are concatenated with
the optimal wavelet transform to form the vector of image features using the following
Eq. 10.
 Fimage = concat(Fcnn,F owt) (10)
The concatenated feature vector is then passed as input to the feature selection algo -
rithm to remove redundant or irrelevant features and retain maximum discriminative
features which helps in improving the performance of classification and has reduced
computational complexity.
3.3 Feature selection
To select the most optimal subset of features for classification tasks, the fused features
are sent to the optimization algorithm named DMFO algorithm, an advanced variation
of the MFO. The fitness function in the conventional MFO approach is usually a single
objective function that assesses a solution’s (moth) performance in relation to the opti -
mization issue. However, DMFO incorporates intraclass variance ( σ2 intra ) to measure
feature variations within each class and interclass variance ( σ2 inter ) to evaluate feature
differences across classes. This approach facilitates selecting the most relevant feature
subsets, justifying its "dual" designation. The goal is to minimize the fitness function,
leading to a more compact feature set while reducing σ2 intra  and σ2 inter .
The DMFO parameter setting comprises the maximum number of iterations ( Max-
Iter), the number of moths( Mn) and flames ( Fn). The process begins by initializing
populations of moths and flames, setting a baseline fitness threshold, and incorporating
constants such as b and t. The algorithm then evaluates each moth’s fitness, ranks them
based on their scores, updates the flames, and selects a flame from the set. It then refines
the moth’s position using a spiral mechanism, calculates a new fitness value, compares
it with a predefined threshold, and identifies the most optimal moth and corresponding
fitness value. This cycle continues from iteration 1 to MaxIter, ensuring that the best
solution is obtained. Therefore, the DMFO algorithm can be regarded as an effective
feature selection method since it makes advantage of the data that moths and flames
offer, giving us a rather quick and comprehensive feature selection method. Equations 11

Page 11 of 28
Kadu et al. Discover Artificial Intelligence           (2026) 6:1266
and 12 demonstrate how it evaluates and chooses the appropriate feature subsets using
σ2 inter  and σ2 intra , respectively.

σ2 inter (i)= 1 Ns(i)
Ni∑
j=1
(xj (i) − µi)2 (11)
where, µ is the average of all classes taken together, Ns is the number of samples and,
xj (i) is the value of the jth sample for feature i.
 σ2 intra (i, j)= |σ2 inter (i) − σ2 inter (j)| (12)
Based on this assessment, dual moth fitness is calculated using Eq.  13 The ratio’s goal is
to minimize the fitness function, which will lead to fewer selected features, higher σ2 inter
variance, and lower σ2 intra  variation.

fm =
∑NC
i=1
∑NC
j=1 σ2 intra (i, j) ∑NC
i=1 σ2 inter (i)  (13)
The variable NC represents each of the classes utilized in sentiment analysis. The inter-
class variance for the ith feature is denoted by σ2 inter (i). Additionally, the intra-class
variance between the ith and jth characteristics is denoted by σ2 intra (i, j). Equation 14 is
used to determine the fitness threshold value following several iterations of the process
for nm moths.

fth = 1 Mn
Mn∑
i=1
fm(Mi) · LM (14)
Where, Mn is the number of moths, LM is the MFO process’s learning rate, and fm(Mi)
is the ith moth’s fitness value. The moths with a fm(Mi) > f th value are retained for the
following iteration, while the ones with other values are eliminated using Eqs. 11, 12, and
13. The characteristics of a moth flame are reproduced by this method. This approach
helps identify a set of highly variable traits by iterating to produce new moths after each
Imax iteration. This optimization method was proposed in the prior work.
Compared with conventional optimization algorithms such as PSO, GWO, and
standard MFO, the proposed DMFO exhibits comparable computational complex -
ity while providing improved convergence towards discriminative feature subsets
through its dual-objective fitness function. The computational complexity of DMFO is
O(NM × Imax), where NM  denotes the number of moths and Imax represents the maxi-
mum number of iterations. Although DMFO introduces an additional fitness evaluation
based on inter-class and intra-class variance, the convergence behaviour remains stable
and enables faster selection of informative features, thereby improving the overall clas -
sification performance.
3.4 Classification
The chosen features are categorized using an ensemble classification procedure called a
weighted hard voting method, which uses each feature’s correctness to determine senti -
ment. The final sentiment prediction is obtained by combining the predictions of each

Page 12 of 28
Kadu et al. Discover Artificial Intelligence           (2026) 6:1266
base classifier (SVM, NB, KNN, LR, and DF) after each classifier has been trained on the
features.
The performance of various ensemble learning techniques was assessed on the basis
of the same feature subset using the following classifiers: Soft Voting, Hard Voting, Bag -
ging, AdaBoost, Gradient Boosting, Stacking and Weighted Soft Voting. For the frame -
work, the ensemble’s base learners were SVM, NB, KNN, LR and DF. In the framework
of the weighted soft voting classifier, the voters of each base learner were determined
by their validation accuracy, and thus, the base learners who achieved better validation
were attributed higher voting weights. In the case of stacking, the base learners’ predic -
tion probabilities were used to train a logistic regression meta-learner, and the result -
ing final prediction was in the form of a sentiment guess. While the ensemble classifiers
were created with defaults to all hyperparameters. The configurations of these base
learners classifiers are listed below.
  • SVM: RBF kernel, C =1 .0, gamma = scale, tol=10−3, max iter = 1000
  • NB: GaussianNB with var smoothing = 10−9
  • KNN: k =5 , Euclidean distance, weights=distance, leaf size=30
  • LR: L2 penalty, C = 1.0, max iter = 1000, solver = lbfgs
  • DF: 100 trees, Gini, max depth = 10, max features = auto
In order to enhance predictive performance and generalization for final sentiment classi-
fication, several ensemble mechanisms are being deployed. Base classifiers encompassed
SVM, NB, KNN, LR, and DF. These are the basic models upon which many ensemble
mechanisms are executed. Soft voting averages the predicted class probabilities gener -
ated from all the base models to determine the final class, while hard voting assigns the
label selected by the majority of models as the final class to be adopted by all models.
Bagging works through random forest that grows a large number of decision trees on
randomly drawn data subsets with the key objective of reducing overfitting. Boosting
approaches like AdaBoost and gradient boosting go further by training one weak learner
after another while emphasizing examples that were misclassified previously. XGBoost
further improves accuracy as a more regularized and faster variant of gradient boosting.
Last but not least, stacking predicts the outcomes of all base classifiers and passes them
as input to a meta-classifier for the final decision, which uses complementary strengths
of each single model. The categorization model categorizes each sentiment prediction
as positive, neutral, or negative.. The categorization model categorizes each sentiment
prediction as positive, neutral, or negative.
4 Experimental setup
The proposed model utilizes WaveNet-CNN features, DMFO for feature selection,
and ensemble classification procedures to accurately identify various sentiments from
images.
4.1 Description of dataset
  • Dataset 1: FER2013
 https://www .kaggle.com /datasets/m sambare/ fer2013
 This dataset serves as one of the most acknowledged benchmarks in facial expression
recognition, containing about 35,887 grayscale images. These images are gathered

Page 13 of 28
Kadu et al. Discover Artificial Intelligence           (2026) 6:1266
from different real-world settings, hence making the dataset quite difficult due
to aspects such as low resolution, varying facial expressions and unconstrained
backgrounds; these are all scenarios that would map to social media or video analysis.
Different emotions are categorized into seven classes: angry, disgust, fear, happy,
neutral, sad and surprised. For sentiment classification, in this work, the classes are
further combined into positive (happy), neutral (neutral, surprised) and negative
(angry, disgust, fear, sad). This grouping indicates that there are 35,887 images
in FER2013, comprising 13,287 positive, 6,198 neutral and nearly 6,402 negative
samples.
  • Dataset 2: JAFFE
 https:   //w ww.kag gle .com/dat asets/tarun pa ruchu r/jaff  e-image-dataset
 This dataset is provided by Kyushu University and contains 213 grayscale facial
images taken from 10 Japanese female subjects. Each subject presents several facial
expressions in a controlled environment. The dataset, though relatively smaller, offers
high-quality and clearly labeled expression samples for the same seven categories as
the FER2013. JAFFE contains 240 positive, 240 neutral and 1,224 negative samples of
a total of 1,704 images. The sample images for FER2013 and JAFFE dataset are shown
in Fig. 2.
  • Dataset 3: restaurant review images
 The original image dataset consisted of 935 positive, 1,007 neutral and 920 negative
samples i.e. total review images collected from various social media and internet
platforms and also curated from existing research datasets used in prior scholarly
work [1].
 The original restaurant review dataset was first divided into 80% training and 20%
testing subsets. Data augmentation was subsequently applied only to the training
set, while the testing set consisted solely of original images. This strategy prevented
data leakage by ensuring that augmented versions of the same image did not appear
in both the training and testing sets. In order to improve model generalization, an
augmentation pipeline was applied and the dataset was expanded to 8,790 positive,
9,263 neutral and 8,648 negative images. The augmentation techniques included
horizontal flipping with 50% probability, random affine transformations (rotation
between − 40◦ to +40◦ and shear between − 10 to +10), gamma contrast adjustment
(0.7–1.3), addition of Gaussian noise (scale up to 10% of pixel intensity), image
sharpening (10–100%), coarse dropout (2–10% of pixels in patches) and Gaussian
blur (0.0–2.0 sigma). Each augmented image was resized to 224 × 224 pixels. It
should be noted that the augmentation process does not introduce new semantic
information, but generates transformed versions of the original images to improve
model robustness against variations such as illumination, orientation, noise, and
scale. Therefore, the augmented dataset is intended to reduce overfitting and improve
generalization rather than increase the intrinsic diversity of the original dataset. The
sample images of dataset 3 are shown below in Fig. 3.
Fig. 2 Sample images from FER2013 and JAFFE dataset

Page 14 of 28
Kadu et al. Discover Artificial Intelligence           (2026) 6:1266
The benchmark facial expression datasets together with the expanded restaurant image
dataset provide researchers with both testing standards and practical application testing
grounds. The model performance increases because of the diverse visual elements which
help to create different testing environments.
4.2 Feature extraction and selection parameters
The dataset was divided into 80% training and 20% testing. The WaveNet-CNN method
was used for feature extraction, which is a combination of optimal wavelet transform
and custom CNN. This allows for the extraction of complex visual information. To form
an integrated feature, the feature vectors obtained from these two methods are com -
bined. The hyperparameters used for customized CNN are the Adam optimizer, learning
rate = 0.00001 and criterion = crossentropy. For the optimal wavelet transform, filter
banks were used on different vanishing moments (OWFB2, OWFB4, OWFB6). The
total number of features extracted from WaveNet-CNN is 1512. The final 1512-dimen -
sional feature vector consists of 512 spatial features extracted from the customized CNN
and 1000 frequency-domain features extracted from the Optimal Wavelet Filter Bank
(OWFB). These features are combined using feature-level concatenation to form a uni -
fied feature representation before DMFO-based feature selection.
For selecting features, The DMFO algorithm was configured with the following param-
eters: 30 moths, 15 flames, a maximum of 100 iterations and a learning multiplier of
0.5. The selected features after applying DMFO are 725. The combined WaveNet-CNN
framework enables comprehensive extraction of spatial and frequency features, while
DMFO effectively reduces dimensionality. This balance enhances classification perfor -
mance with controlled computational cost.
4.3 Sentiment categorization criteria
The suggested model output is classified into three categories: positive (2), negative (1)
and neutral (0). Table 3 shows the sentiment score range which applies to each of the
three categories.
The established sentiment score limits create a framework for translating model out -
puts into distinct sentiment categories which maintains consistent results. The method
enhances visual sentiment prediction reliability.
Table 3 Sentiment categories based on sentiment score
Sentiment score range Assigned sentiment category
0 ≤ score < 1 Negative
1 ≤ score < 1.5 Neutral
1.5 ≤ score ≤ 2 Positive
Score > 2 or score < 0 Invalid score
Fig. 3 Sample images from restaurant review dataset

Page 15 of 28
Kadu et al. Discover Artificial Intelligence           (2026) 6:1266
4.4 Feature maps
The hierarchical feature learning in a CNN is illustrated in Fig.  4. In the initial layers
(channels 1–4), the network captures low-level details such as textures, colors and spa -
tial layout. As we move deeper (layers 2–3), the model begins to recognize mid-level
features like object parts (e.g., faces, drinks). In the deepest layers (layers 4–6), activa -
tions become sparse, with some channels turning dark due to selective feature encoding.
These layers focus on high-level semantic information such as identity, object categories,
or emotions. This progression enables CNN to learn and represent complex patterns
critical for tasks such as sentiment or emotion recognition.
The decomposition of an image into subbands: cA (approximation) captures the low-
frequency structure, while cH, cV and cD highlight horizontal, vertical and diagonal
edges, respectively is illustrated in Fig.  5. This decomposition effectively captures fine
textures and directional details, which are valuable for tasks such as face recognition and
food-related images. The model complements CNNs by introducing explicit frequency
and directional features that CNNs may not inherently learn, enhancing the overall fea -
ture representation.
The hybrid set of feature maps formed by combining custom CNN output (captur -
ing semantic and spatial patterns) with wavelet coefficients (capturing frequency and
edge details) is illustrated in Fig.  6. The maps are diverse and non-redundant, showing
both blocky and smoothly varying patterns. This fusion provides a rich representation
that combines deep-learning features with hand-crafted frequency information. In the
model, this fused representation improves robustness and expressiveness, improving
classification performance by leveraging complementary feature domains.
Fig. 4 Feature map custom CNN

Page 16 of 28
Kadu et al. Discover Artificial Intelligence           (2026) 6:1266
The progressive visualization of CNN, wavelet, and fused feature maps demonstrates
effective hierarchical and complementary feature learning. This confirms the model’s
ability to capture both semantic and fine-grained visual sentiment cues.
5 Results and discussion
The system evaluation for image-based sentiment analysis system testing happens in this
section through detailed assessment. The evaluation tests multiple benchmarking datas -
ets to measure system performance which gets compared against traditional deep learn -
ing methods and current leading techniques. The study uses Precision(P) and Recall(R)
and Accuracy(Acc) and F1-Score(F1) as essential performance assessment criteria.
A critical analysis is made on the effectiveness of components such as feature extrac -
tion using custom CNN and optimal wavelet transform, feature selection using DMFO
on different classifiers. The superiority and effectiveness of the proposed techniques
in sentiment recognition from visual content are shown using comparative tables and
representations.
5.1 Performance analysis
The experiments were carried out on dataset 3, which involves a comparative evalua -
tion between the proposed custom CNN and several established deep learning models,
including basic CNN, VGG-19, InceptionV3 and ResNet. These models were used for
Fig. 6 Fused feature map

Fig. 5 Feature map optimal wavelet transform

Page 17 of 28
Kadu et al. Discover Artificial Intelligence           (2026) 6:1266
feature extraction, followed by classification using different classifiers. Among the com -
binations tested, the custom CNN paired with the SVM classifier demonstrated superior
performance, achieving the highest accuracy. The detailed performance metrics of each
model and classifier combination are presented in Table  4. Further, experiments were
performed making comparisons between different transforms for feature extraction and
on different classifiers, and it was found that wavelet transform with the SVM classifier
model outperforms them in terms of accuracy. Table 5 shows the performance of differ-
ent transform models and classifiers.
For the WT, initial experiments were performed using base Daubechies wavelets as
the mother wavelet at db2, db4 and db6. The results indicate that db4 performs well with
the SVM classifier, as shown in Table 6.
Later, the experiment was performed using another type of wavelet called biorthog -
onal wavelets in a specific biorthogonal wavelet family (e.g. bior2.3, bior4.4, bio6.4) as
shown in Fig. 7. It is observed that the features extracted from bio4.4 with the SVM clas-
sifier perform better.
To improve the accuracy of the model, the custom CNN with the optimal wavelet
transform is combined which is obtained by modifying the values of the HPF and LPF
coefficients of the biorthogonal wavelet for the vanishing moments v = 2, 4 and 6. Further
experiments were performed using this combination on different vanishing moments
with different classifiers including ensemble classifiers. Figures  8 and 9 show the impact
of vanishing moment in optimal filter banks on classifier performance without using
DMFO. It is observed that as the number of vanishing moments (v) in the OWFB
increases, most models show enhanced performance, with the ensemble technique
Table 4 Performance comparison of feature extraction models (Deep Learning) with classifiers
Model Classifier Acc P R F1
CNN NB 70.23 70.34 70.00 70.10
KNN 70.11 70.32 70.30 70.11
SVM 71.78 71.20 71.00 71.48
DF 71.50 71.10 71.10 71.70
LR 71.90 71.70 71.50 71.40
VGG19 NB 71.32 71.01 71.80 71.40
KNN 71.60 71.80 71.50 71.60
SVM 72.20 72.40 72.10 72.20
DF 72.60 72.80 72.50 72.60
LR 72.80 73.00 72.60 72.70
InceptionV3 NB 71.22 72.10 71.00 71.50
KNN 72.30 73.00 71.90 72.40
SVM 73.90 74.50 73.60 73.90
DF 74.50 74.80 74.00 74.40
LR 74.80 75.00 74.50 74.80
ResNet NB 75.50 76.30 75.00 75.60
KNN 76.30 77.10 76.00 76.50
SVM 77.00 77.50 76.70 77.00
DF 77.20 77.50 76.90 77.10
LR 77.40 77.80 77.00 77.30
Custom CNN NB 76.80 77.50 76.30 76.90
KNN 77.00 77.80 76.80 77.20
SVM 78.84 79.01 78.07 78.07
DF 77.70 78.40 77.50 77.90
LR 77.50 78.10 77.30 77.70

Page 18 of 28
Kadu et al. Discover Artificial Intelligence           (2026) 6:1266
consistently achieving the highest quality outcomes. Higher vanishing moments provide
superior feature extraction, enabling the capture of intricate patterns in the data. This, in
turn, increases the accuracy and dependability of the classification models.
The DMFO algorithm shows better performance results after different feature selec -
tion algorithms have been implemented. Figure  10 presents a comparative study of vari -
ous feature selection methods.
The performance of various classifiers using a novel WaveNet-CNN method is shown
in Table 7. This method is a fusion of custom CNN and the optimal wavelet transform
where the filer banks are modified at different vanishing moments using DMFO, a
feature selection method. It is observed that as the number of vanishing moments in
the OWFB increases, most models show enhanced performance, with the ensemble
Table 5 Performance comparison of feature extraction models (Transform-based) with classifiers
Model Classifier Acc P R F1
Wavelet transform (WT) NB 64.12 62.65 62.89 63.36
KNN 62.75 61.29 61.76 61.70
SVM 69.23 67.22 68.12 68.44
DF 68.17 68.01 68.17 67.93
LR 64.23 62.83 63.14 63.07
Fourier transform (FT) NB 62.22 61.27 60.89 61.52
KNN 61.12 59.91 60.47 60.56
SVM 64.56 63.57 63.65 63.11
DF 65.02 63.76 64.10 64.06
LR 63.45 62.10 62.24 62.41
Discrete cosine transform (DCT) NB 63.84 62.88 62.35 62.34
KNN 60.45 59.47 59.45 59.66
SVM 63.32 62.46 62.80 62.03
DF 64.94 63.81 63.76 63.44
LR 62.11 60.98 60.85 60.72
Convolutional transform (CT) NB 61.22 60.41 60.31 60.18
KNN 58.35 56.97 57.74 57.34
SVM 60.42 59.66 58.95 59.84
DF 61.77 61.10 61.12 61.11
LR 60.33 59.38 59.01 59.24
Table 6 Performance comparison of classifiers using Daubechies wavelets
Classifiers Daubechies wavelet Acc (%) P (%) R (%) F1 (%)
SVM db2 67.85 66.41 66.90 66.65
db4 69.23 67.22 68.12 68.44
db6 66.43 65.17 65.68 65.42
NB db2 61.40 60.80 61.12 60.96
db4 62.25 61.50 61.89 61.68
db6 64.12 62.65 62.89 63.36
KNN db2 61.34 60.70 60.98 60.84
db4 62.75 61.29 61.76 61.70
db6 60.42 59.87 60.10 59.98
LR db2 62.89 61.72 62.01 61.86
db4 64.23 62.83 63.14 63.07
db6 61.53 60.38 60.70 60.54
DF db2 66.74 66.43 66.59 66.51
db4 68.17 68.01 68.17 67.93
db6 65.49 65.23 65.38 65.30

Page 19 of 28
Kadu et al. Discover Artificial Intelligence           (2026) 6:1266
technique consistently achieving the highest outcomes. Higher vanishing moments pro -
vide superior feature extraction, enabling the capture of intricate patterns in the data.
This, in turn, increases the accuracy and dependability of the classification models.
The comparative analysis of the proposed model with the existing systems for data -
set 3 is illustrated in Table 8. Models built on the basis of item-orientated CNN and
InceptionV3 demonstrate reduced accuracy and F1 scores, which state that these types
of model have poor performance in extracting complex cues of sentiment using visual
data. DenseNet-121 performs rather well with an accuracy of 89.00% and an F1 score
of 87.00% that indicates the potential of DenseNet to represent features. More recent
Fig. 8 Impact of vanishing moment in optimal filter banks on classifier performance w/o using DMFO

Fig. 7 Accuracy comparison of classifiers using biorthogonal wavelets (2.3, 4.4, 6.4)

Page 20 of 28
Kadu et al. Discover Artificial Intelligence           (2026) 6:1266
architectures, including EfficientNet-B0 and Swin Transformer-T, further improve the
classification performance by achieving accuracies of 84.15% and 87.35%, respectively.
However, the proposed system (WaveNet-CNN) beats all baseline models with an accu -
racy of 89.72%, a precision of 88.72%, a recall of 88.12% and an F1 score of 89.71%. This
enhancement confirms the power of the optimized WaveNet-CNN in extracting and uti-
lizing discriminative features for sentiment classification.
The comparison of different deep learning models with the proposed system in Dataset
1 (FER2013) is summarized in Table 9. Whereas traditional models such as CNN, ResNet
and InceptionV3 exhibit average results. Recent architectures, including EfficientNet-B0
and Swin Transformer-T, further enhance the performance through improved feature
extraction and hierarchical representation learning, achieving accuracies of 74.10% and
74.72%, respectively. Nevertheless, the proposed WaveNet-CNN dominates with the
best accuracy of 75.15% and an F1 score of 74.36%, demonstrating its ability to essen -
tially extract deeper spatial and frequency features for image sentiment classification.
From Table 10, the proposed system (WaveNet-CNN) achieves the best perfor -
mance among all, with an Acc of 87.42% and an F1 of 87.72%, surpassing Gabor filters,
ResNet101, InceptionV3, MTF. Recent architectures, including EfficientNet-B0 and Swin
Transformer-T, further improve feature extraction efficiency and hierarchical repre -
sentation learning, achieving accuracies of 86.58% and 87.10%, respectively on dataset2
(JAFFE). This proves to be a great leverage in mixing spatial and frequency domain fea -
tures for better image sentiment classification.
Fig. 10 Comparative analysis of different feature selection algorithms

Fig. 9 Impact of vanishing moment in optimal filter banks on classifier performance w/o using DMFO (continued)

Page 21 of 28
Kadu et al. Discover Artificial Intelligence           (2026) 6:1266
5.2 Cross-dataset evaluation
The cross-dataset evaluation results of the proposed WaveNet-CNN model are pre -
sented in Table 11. The primary objective of this evaluation is to assess the general -
ization capability of the model when trained on one dataset and tested on a different
dataset. In Case 1, the model trained on Dataset 1 and tested on Dataset 3 achieves an
Table 7 Performance comparison using optimal wavelet filter banks (OWFB) with DMFO
Models OWFB Acc(%) P(%) R(%) F1(%)
SVM OWFB2 73.61 73.62 72.61 75.94
OWFB4 75.83 77.91 73.83 71.88
OWFB6 74.17 74.01 72.17 73.93
NB OWFB2 67.83 64.91 67.83 64.88
OWFB4 73.52 77.05 74.52 72.85
OWFB6 65.60 68.03 65.23 70.72
KNN OWFB2 67.83 68.49 67.83 67.60
OWFB4 73.83 77.91 73.83 71.88
OWFB6 71.17 71.01 70.17 70.93
LR OWFB2 70.61 70.62 70.61 72.94
OWFB4 67.83 68.49 67.83 67.60
OWFB6 73.48 73.52 73.48 73.40
DF OWFB2 69.09 69.03 69.09 65.94
OWFB4 66.70 64.44 66.70 72.53
OWFB6 67.39 67.47 67.39 67.39
Soft voting OWFB2 85.76 86.38 85.76 86.14
OWFB4 87.03 85.03 86.03 86.02
OWFB6 88.94 87.53 88.94 88.04
Hard voting OWFB2 84.87 87.91 84.87 83.56
OWFB4 82.56 85.18 82.56 83.01
OWFB6 86.45 89.72 86.45 86.59
Bagging OWFB2 80.93 75.42 79.83 75.14
OWFB4 79.65 78.62 75.65 65.54
OWFB6 82.87 83.44 71.87 72.43
AdaBoost OWFB2 81.80 84.74 81.80 82.43
OWFB4 83.73 86.25 83.73 82.88
OWFB6 86.12 88.95 86.12 86.02
Gradient boosting OWFB2 83.44 82.44 82.13 83.12
OWFB4 83.19 86.10 83.19 84.02
OWFB6 88.60 88.33 88.60 89.07
Stacking OWFB2 85.52 87.06 85.52 83.91
OWFB4 84.42 87.25 84.42 83.96
OWFB6 89.21 88.01 89.21 88.61
Weighted soft voting OWFB2 86.76 89.38 87.76 85.14
OWFB4 88.01 88.37 88.01 88.27
OWFB6 89.72 88.72 89.12 89.71
Table 8 Performance comparison between existing models and proposed system on dataset 3
Models Acc (%) P (%) R (%) F1 (%)
Item-oriented CNN [27] 67.80 67.00 67.32 65.80
CNN-based Inception-v3 [6] 73.00 67.20 68.00 68.20
DenseNet-121 [31] 89.00 86.00 88.00 87.00
MTF 74.80 75.00 74.50 74.80
EfficientNet-B0 84.15 83.72 83.21 83.46
Swin Transformer-T 87.35 86.91 86.54 86.72
Proposed WaveNet-CNN 89.72 88.72 88.12 89.71

Page 22 of 28
Kadu et al. Discover Artificial Intelligence           (2026) 6:1266
accuracy of 66.30% and an F1-score of 64.74%, indicating moderate generalization per -
formance when exposed to images with different visual characteristics. In Case 2, where
the model is trained on Dataset 2 and tested on Dataset 3, the performance further
decreases, achieving an accuracy of 62.10% and an F1-score of 60.69%. This additional
performance degradation suggests a larger domain gap between Dataset 2 and Dataset 3,
making cross-domain adaptation more challenging.
The decrease in the accuracy of cross-dataset performance is largely due to the fun -
damental differences between the two datasets. Dataset 1 (FER2013) and Dataset 2
(JAFFE) have mostly images of facial expressions taken under standardized or controlled
settings. However, Dataset 3 includes natural images of restaurant reviews that have
varied visual components, including food arrangement, ambiance, facial expressions,
lighting, occlusions, and background. Such discrepancies bring about a change in the
underlying distribution of the visual features, thus resulting in poor generalizability of
the learned features to new datasets. Nonetheless, despite the variations, the developed
model, WaveNet-CNN, exhibits relatively good transfer learning ability without any
form of dataset-specific fine-tuning, meaning that the learned visual features are dis -
criminative to a certain degree.
Overall, the results demonstrate that although the proposed model maintains rea -
sonable performance across datasets, variations in image quality, expression styles, and
sentiment cues significantly impact prediction accuracy, highlighting the importance of
incorporating diverse data sources during training to enhance cross-dataset robustness.
Table 9 Comparison of existing models with proposed system on dataset 1
Models Acc(%) P(%) R(%) F1(%)
CNN [9] 65.20 73.40 69.40 69.40
Resnet101 [32] 71.90 71.70 71.40 71.40
Inception V3 based model [33] 73.00 67.20 68.00 68.20
MTF [34] 73.50 70.10 68.90 72.90
EfficientNet-B0 74.10 73.62 73.25 73.43
Swin Transformer-T 74.72 74.21 73.88 74.05
Proposed WaveNet-CNN 75.15 74.72 75.15 74.36
Table 10 Comparison of existing models with proposed system on dataset 2
Models Acc(%) P(%) R(%) F1(%)
Gabor filters [7] 76.31 72.32 71.92 71.94
Resnet101 [32] 76.44 71.42 75.84 75.84
Inception V3 based model [33] 86.00 82.00 84.00 84.44
MTF [34] 87.34 87.21 86.45 86.24
EfficientNet-B0 86.58 86.30 86.12 86.21
Swin Transformer-T 87.10 86.84 86.72 86.78
Proposed WaveNet-CNN 87.42 87.02 87.87 87.72
Table 11 Cross-dataset results for the proposed WaveNet-CNN system
Case Train → Test Acc (%) P (%) R (%) F1 (%)
Case 1 Dataset 1 → Dataset 3 66.30 65.50 64.00 64.74
Case 2 Dataset 2 → Dataset 3 62.10 61.40 60.00 60.69

Page 23 of 28
Kadu et al. Discover Artificial Intelligence           (2026) 6:1266
5.3 Ablation study
In Table 12, an extensive ablation study is presented which measures the degree of
contribution of each component in the proposed WaveNet-CNN framework. The per -
formance of the CNN combined with an LR classifier is 71.50% accuracy; thus, it dem -
onstrates the very limited capabilities of the spatial features used alone. Wavelet-based
approaches utilizing db4 and biorthogonal (bio4.4) wavelets get 69.23% and 72.65%
accuracy, respectively, which suggests that the information from the frequency domain
does help in distinguishing but still remains insufficient by itself. The OWFB6 wavelet
on top of that already gives the performance a boost to 73.40%. The custom CNN has
a remarkable impact on accuracy and raises it to 78.84%; thus, it reveals its capability
for extracting richer spatial semantics. Upon the combination of Custom CNN and
OWFB6, followed by WSV classification, accuracy is uplifted to 87.87%. The inclusion
of MFO-based feature selection results in a further leap to 88.76%, reflecting that the
classifier’s power is enhanced through the removal of the redundant and irrelevant fea -
tures. The full pipeline—Custom CNN + OWFB6 + DMFO—reaches the peak accuracy
of 89.72%, thereby confirming that the fusion of optimized multi-domain features and
metaheuristic feature selection produces the most effective configuration for visual sen -
timent analysis.
6 Statistical analysis and validation
Statistical analysis was done to check how well the WaveNet-CNN framework works,
how reliable it is, and if its results are statistically significant. The analysis also looked at
how the framework classifies data, what the prediction errors are, how fast it computes
results, and what the confidence intervals are. Also, feature selection algorithms were
compared statistically to see if the DMFO algorithm is better than the others. Statis -
tical analysis was performed to evaluate the significance, reliability, and consistency of
the proposed WaveNet-CNN framework. All experimental results reported in this study
represent the mean of ten independent experimental runs ( n = 10). The standard devia-
tion (SD), 95% confidence intervals, and paired Student’s t-test were computed based on
these repeated runs using a significance level of α =0 .05.
Then your section becomes: The next sections will go over the analysis of the classifi -
cation models and the feature selection methods in more detail.
6.1 Statistical comparison of classification models
Table 13 presents a comparative evaluation of baseline models and the proposed
WaveNet-CNN using statistical and computational metrics on the restaurant review
dataset. The proposed model achieves the lowest MAE (0.11), which demonstrates its
Table 12 Ablation study illustrating the impact of individual components on classification accuracy
Model configuration Accuracy (%)
CNN + Classifier (LR) 71.50
Wavelet Features Only(db4) + Classifier(SVM) 69.23
Custom CNN + Classifier(SVM) 78.84
Biorthogonal WT Features Only(bio4.4) + Classifier(SVM) 72.65
OWFB6 Features only + Classifier(SVM) 73.40
(Custom CNN + OWFB6)+ Classifier(WSV) 87.87
(Custom CNN + OWFB6) + With MFO + Classifier(WSV) 88.76
Proposed WaveNet-CNN (with DMFO) 89.72

Page 24 of 28
Kadu et al. Discover Artificial Intelligence           (2026) 6:1266
ability to make accurate predictions with very small measurement errors.It also records
the lowest Standard Deviation (SD) of 0.21, demonstrating consistent and stable perfor -
mance across repeated runs. The method requires extra time because it needs to process
wavelet data and perform feature selection, but this time requirement produces statisti -
cally significant performance enhancements according to p value results, which show
values below 0.001. The narrow confidence interval [88.6, 90.8] establishes that the pro -
posed method maintains both consistent and reliable performance. The baseline models
show lower stability and predictive performance because they produce higher error rates
and wider confidence intervals.
6.2 Statistical analysis of feature selection methods
Table 14 shows the comparison of the different feature selection algorithms used in
our framework. The DMFO has a classification accuracy of 89.72% with a low standard
deviation of ±0.25. This means that DMFO performs more stable and consistent across
repeated experiments. The p-value is than 0.001 which confirms that DMFOs better
performance is statistically significant. DMFO performs better because it uses an objec -
tive fitness function. This function helps to maximize the difference between classes and
minimize the difference within classes. As a result DMFO selects useful feature subsets
than other algorithms like GA, PSO and MFO. DMFOs approach makes it a good choice
for feature selection in our framework. The results show that DMFO is better than GA,
PSO and MFO in terms of classification accuracy. DMFOs performance is more stable
and consistent, across repeated runs.
6.3 Computational complexity analysis
The computational complexity in the proposed WaveNet-CNN framework is basically
made of four big stages: optimal wavelet-based feature extraction, a custom CNN-style
spatial feature extraction, then DMFO-driven feature selection, and finally the sentiment
classification, yeah. First, the wavelet transform does a multi-resolution decomposition;
it works with linear complexity relative to how many image pixels you have. Next, the
customized CNN becomes the main computational burden while training because it
keeps doing multiple convolution and pooling operations across successive epochs, so
it just stacks up. After that, the DMFO algorithm adds extra optimization overhead by
Table 13 Performance comparison of deep learning models on restaurant review dataset using
statistical and computational metrics
Model MAE SD Computational time (s) p value 95% Confidence interval
CNN 0.44 0.62 0.05 0.032 [53.8, 57.6]
VGG19 0.39 0.51 0.09 0.021 [58.5, 62.5]
InceptionV3 0.25 0.42 0.12 0.008 [73.5, 76.1]
ResNet 0.23 0.37 0.14 0.005 [76.2, 78.6]
Proposed WaveNet-CNN 0.11 0.21 0.18 < 0.001 [88.6, 90.8]
Table 14 Statistical comparison of feature selection algorithms on the restaurant review dataset
Feature selection Accuracy (%) Std. Dev. p value 95% Confidence interval
GA 88.05 ±0.54 0.012 [87.4, 88.9]
PSO 88.32 ±0.49 0.008 [87.8, 89.2]
MFO 88.76 ±0.37 0.004 [88.2, 89.3]
DMFO 89.72 ±0.25 < 0.001  [89.1, 90.2]

Page 25 of 28
Kadu et al. Discover Artificial Intelligence           (2026) 6:1266
iteratively picking the most discriminative feature subset, although this part only runs
during training, not inference. The overall computational complexity of the proposed
framework can be stated as the combined complexity of its major components. For the
OWFB component, the required computational complexity is O(N) for an image of size
N. The computational complexity of the custom CNN feature extraction part is stated as
O(C), where C is the total number of convolution operations throughout the network.
The complexity of DMFO-based feature selection is given as O(Mn × M axIter × F ),
where Mn is the number of moths used, MaxIter is the maximum number of iterations,
and F is the number of extracted features. Since the DMFO algorithm runs during the
training phase only, the prediction phase includes only the wavelet transform, CNN fea -
ture extraction, and classification, which results in decreased computational complexity.
The memory requirements are mainly based on CNN feature maps and the DMFO moth
population during training and the model parameters only during inference.
7 Limitation of work
The proposed WaveNet-CNN has shown best results on all three datasets used for eval -
uation, it still has quite a few drawbacks. Its effectiveness is very much dependent on the
quality of the images; thus, it is very sensitive to low-quality images, occlusions, and even
the cluttered backgrounds which are very common in real-world social media images.
The combined application of WaveNet-CNN, wavelet transforms, and DMFO increases
computational complexity, making it less suitable for real-time applications. Moreover,
the model considers only three sentiment classes, which leads to its inability to perceive
complex emotions, plus it does not take into account the textual information that usually
comes with the images, which might limit sentiment interpretation in unclear cases. The
use of metaheuristic feature selection gives rise to variability and requires precise tun -
ing, and the ensemble method, while being robust, complicates the deployment further.
8 Conclusion and future scope
This work presents a comprehensive framework for visual sentiment analysis by inte -
grating spatial and frequency-domain feature extraction using a custom CNN and an
optimal wavelet transform. The proposed approach effectively combines complementary
features through feature-level fusion and enhances performance using DMFO-based
feature selection and ensemble classification. Based on the experimental results per -
formed on dataset 3, several key observations can be drawn. The transition from stan -
dard CNN architectures to the custom CNN architecture, without feature selection,
on different classifiers yielded an increase in accuracy. In addition, different transforms
were compared demonstrating that the WT achieved superior performance. The wavelet
transform with modified filter banks coefficients was integrated with the custom CNN
to enhance spatial and frequency feature extraction. The WaveNet-CNN model gives an
accuracy of 87.87% which is improved by approximately 2% with the integration of the
DMFO algorithm for optimal feature selection. This emphasizes the importance of both
architectural improvements in feature extraction and the application of effective feature
selection to enhance image sentiment analysis performance. The proposed model dem -
onstrated strong accuracy across the benchmark datasets, achieving 75.15% on dataset
1, 87.42% on dataset 2 and 89.72% on dataset 3, validating the robustness and generaliz -
ability of the approach.

Page 26 of 28
Kadu et al. Discover Artificial Intelligence           (2026) 6:1266
The proposed work can be extended in several directions to further enhance perfor -
mance and applicability. Future research will investigate how multimodal data integra -
tion can improve sentiment analysis when visual features are combined with textual
data from captions and user reviews. Advanced metaheuristic optimization techniques
together with hybrid methods will improve the feature selection process. The model
performance will benefit from exploring deep learning architectures that include atten -
tion mechanisms and transformers and generative models. Future work might look into
vision-language foundation models like CLIP and also multimodal transformer designs
to see how well the proposed framework stacks up against newer state-of-the-art visual
sentiment analysis methods. This should help with a broad comparison to large-scale
pre-trained models, and it will further support the effectiveness of the WaveNet-CNN
approach. The current study is restricted to the performance evaluation of the suggested
WaveNet-CNN on the chosen visual sentiment data sets without any cross-data set vali -
dation, domain adaptation studies, and explainable artificial intelligence (XAI) analysis
with methods like Grad-CAM, SHAP , LIME, and saliency maps. All of these are out of
the scope of the current study and shall be done in future studies to enhance the robust -
ness and cross-domain adaptability of the proposed system. The framework can also be
evaluated through testing on real-world datasets which have larger scales and more var -
ied content to assess its ability to handle different situations. Future efforts will focus on
collecting larger real-world visual sentiment datasets from multiple domains, including
restaurant reviews, tourism, product reviews, and social media images, to further vali -
date the proposed WaveNet-CNN under diverse real-world conditions and improve its
cross-domain generalization capability, and investigate domain adaptation techniques,
such as domain-invariant feature learning and adversarial domain adaptation, to reduce
domain shift across heterogeneous datasets. The model will achieve better user senti -
ment understanding through its extension to fine-grained and multi-class emotion rec -
ognition systems.
Author contributions
Siddhi Kadu: Conceptualization, Methodology, Software, Field study, Bharti Joshi: Data curation, Writing-Original draft
preparation, Software, Field study, Pratik Agrawal: Visualization, Investigation, Writing-Reviewing and Editing.
Funding
Open access funding provided by Symbiosis International (Deemed University). The authors declare that no funding
source has been used for the current manuscript.
Data availability
Data will be available on reasonable request
Declarations
Ethics approval and consent to participate
Not applicable.
Consent for publication
Not applicable.
Research involving human and/or animals
This article does not contain any studies with human participants or animals performed by any of the authors.
Competing interests
Siddhi Kadu declares that she has no competing interests.
Received: 30 May 2026 / Accepted: 31 August 2026

Page 27 of 28
Kadu et al. Discover Artificial Intelligence           (2026) 6:1266
References
1. Mamatha M, Shivakumar S, Thriveni J, Venugopal KR. Visual sentiment classification of restaurant review images using
deep convolutional neural networks. In: 2022 IEEE international conference on electronics, computing and communica-
tion technologies (CONECCT). IEEE; 2022. p. 1–6.
2. Liu J, Hu S, Mehraliyev F, Zhou H, Yu Y, Yang L. Recognizing emotions in restaurant online reviews: a hybrid model integrat-
ing deep learning and a sentiment lexicon. Int J Contemp Hosp Manag. 2024;36(9):2955–76.
3. Pang B, Lee L. Opinion mining and sentiment analysis. Found Trends Inf Retr. 2008;2(1–2):1–135.
4. Mittal N, Sharma D, Joshi ML. Image sentiment analysis using deep learning. In: 2018 IEEE/WIC/ACM international confer-
ence on web intelligence (WI), IEEE;2018. p. 684–7.
5. Xu J, Li Z, Huang F, Li C, Yu PS. Visual sentiment analysis with social relations-guided multiattention networks. IEEE Trans
Cybern. 2020;52(6):4472–84.
6. Meena G, Mohbey KK, Kumar S. Sentiment analysis on images using convolutional neural networks based inception-v3
transfer learning approach. Int J Inf Manage Data Insights. 2023;3(1):100174.
7. Boughida A, Kouahla MN, Lafifi Y. A novel approach for facial expression recognition based on gabor filters and genetic
algorithm. Evol Syst. 2022;13(2):331–45.
8. Fallahzadeh MR, Farokhi F, Harimi A, Sabbaghi-Nadooshan R. Facial expression recognition based on image gradient and
deep convolutional neural network. J AI Data Min. 2021;9(2):259–68.
9. Hua W, Dai F, Huang L, Xiong J, Gui G. Hero: Human emotions recognition for realizing intelligent internet of things. IEEE
Access. 2019;7:24321–32.
10. Agrawal A, Mittal N. Using CNN for facial expression recognition: A study of the effects of kernel size and number of filters
on accuracy. Vis Comput. 2020;36(2):405–12.
11. Alzamzami F, El Saddik A. Transformer-based feature fusion approach for multimodal visual sentiment recognition using
tweets in the wild. IEEE Access. 2023;11:47070–9.
12. Yuting S, Zhao W, Jing P , Nie L. Exploiting low-rank latent gaussian graphical model estimation for visual sentiment distri-
butions. IEEE Trans Multimed. 2022;25:1243–55.
13. Kossaifi J, Walecki R, Panagakis Y, et al. Sewa db: A rich database for audio-visual emotion and sentiment research in the
wild. IEEE Trans Pattern Anal Mach Intell. 2019;43(3):1022–40.
14. Stappen L, Baird A, Schumann L, Schuller B. The multimodal sentiment analysis in car reviews (muse-car) dataset: collec-
tion, insights and improvements. IEEE Trans Affect Comput. 2021;14(2):1334–50.
15. He J, Mai S, Haifeng H. A unimodal reinforced transformer with time squeeze fusion for multimodal sentiment analysis.
IEEE Signal Process Lett. 2021;28:992–6.
16. Qayyum H, Majid M, Anwar SM, Khan B. Facial expression recognition using stationary wavelet transform features. Math
Probl Eng. 2017;2017:9854050.
17. Avcı D, Sert E, Özyurt F, Avcı E. Mfif-dwt-cnn: Multi-focus image fusion based on discrete wavelet transform with deep
convolutional neural network. Multimed Tools Appl. 2024;83(4):10951–68.
18. You N, Han L, Zhu D, Song W. Research on image denoising in edge detection based on wavelet transform. Appl Sci.
2023;13(3):1837.
19. Yadav A, Vishwakarma DK. A deep learning architecture of ra-dlnet for visual sentiment analysis. Multimed Syst.
2020;26(4):431–51.
20. Arslan M, Mubeen M, Akram A, Abbasi SF, Ali MS, Tariq MU. A deep features based approach using modified resnet50 and
gradient boosting for visual sentiments classification. In: 2024 IEEE 7th international conference on multimedia informa-
tion processing and retrieval (MIPR), 2024;239–42. IEEE.
21. Wang X, Yang J, Min H, Ren F. Eerca-vit: enhanced effective region and context-aware vision transformers for image senti-
ment analysis. J Vis Commun Image Represent. 2023;97:103968.
22. Rajput GK, Srivastava SK, Gupta N. Leveraging swin transformer for advanced sentiment analysis: a new paradigm. Cogn
Neurodyn. 2026;20(1):13.
23. Qin J, Sun Y-T. Fine-tuning clip with dynamic prompt tuning and cross-modal contrastive alignment for multimodal senti-
ment analysis. IEEE Access; 2026.
24. Wang Zhongzheng, Tian Yuanhe, Wang Hongzhi, Song Yan. Explainable multimodal aspect-based sentiment analysis with
dependency-guided large language model. arXiv:2601.06848 [Preprint]. 2026.
25. Hassan KZ, Ahmad K, Hicks P , Halvorsen A, Al-Fuqaha N, Conci M, et al. Visual sentiment analysis from disaster images in
social media. Sensors. 2022;22(10):3628.
26. She D, Yang J, Cheng M-M, Lai Y-K, Rosin PL, Wang L. Wscnet: Weakly supervised coupled networks for visual sentiment
classification and detection. IEEE Trans Multimed. 2019;22(5):1358–71.
27. Truong QT, Lauw HW. Visual sentiment analysis for review images with item-oriented and user-oriented CNN. In: Proceed-
ings of the 25th ACM international conference on multimedia, 2017;1274–82.
28. Urolagin S, Nayak J, Acharya UR. Gabor CNN based intelligent system for visual sentiment analysis of social media data on
cloud environment. IEEE Access. 2022;10:132455–71.
29. Chatterjee S, Saha D, Sen S, Oliva D, Sarkar R. Moth-flame optimization based deep feature selection for facial expression
recognition using thermal images. Multimed Tools Appl. 2024;83(4):11299–322.
30. Mirjalili S. Moth-flame optimization algorithm: a novel nature-inspired heuristic paradigm. Knowl-Based Syst.
2015;89:228–49.
31. Chandrasekaran G, Antoanela N, Andrei G, Monica C, Hemanth J. Visual sentiment analysis using deep learning models
with social media data. Appl Sci. 2022;12(3):1030.
32. Agrawal A, Mittal N. Using CNN for facial expression recognition: a study of the effects of kernel size and number of filters
on accuracy. Vis Comput. 2020;36(2):405–12.
33. Rahman A Md Mostafizer, Islam Shiplu Y, Watanobe MA, Alam. Roberta-bilstm: A context-aware hybrid model for senti-
ment analysis. In: IEEE transactions on emerging topics in computational intelligence. 2025.

Page 28 of 28
Kadu et al. Discover Artificial Intelligence           (2026) 6:1266
34. Kadu S, Joshi B, Agrawal P . Optimization for image sentiment analysis using novel dual moth flame algorithm. SN Comput
Sci. 2025;6(2):134.
Publisher's Note
Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.
