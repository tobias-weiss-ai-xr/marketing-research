---
title: Multimodal sentiment analysis using image and text fusion for emotion detection
url: https://doi.org/10.1007/s10791-025-09756-2
category: digital-marketing
subcategory: measurement
date: 2025-10
venue: Discover Computing
authors:
- Uttam U. Deshpande
- Supriya Shanbhag
- Amit Sukhasare
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1007/s10791-025-09756-2.pdf
pages: 24
chars: 69093
fetched_at: '2026-11-08T17:08:59+00:00'
kb_version: 1
---

# Multimodal sentiment analysis using image and text fusion for emotion detection

RESEARCH Open Access
© The Author(s) 2025. Open Access  This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use,
sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the
source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article
are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the
article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to
obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
Deshpande et al. Discover Computing          (2025) 28:230
https://doi.org/10.1007/s10791-025-09756-2
*Correspondence:
Uttam U. Deshpande
uttamudeshpande@gmail.com
Sangeeta Sangani
sangeeta.sangani@manipal.edu
1Department of Electronics and
Communication Engineering, KLS
Gogte Institute of Technology,
Belagavi, Karnataka, India
2Department of Electronics and
Communication Engineering, KLS
VDIT, Haliyaal, Karnataka, India
3Department of Computer Science
and Engineering, KLS Gogte
Institute of Technology, Belagavi,
Karnataka, India
4School of Computer Engineering,
Manipal Institute of Technology
Bengaluru, Manipal Academy of
Higher Education, Manipal, India
5Master of Computer Applications
Department, Bangalore Institute of
Technology, Bengaluru, India
6Department of MCA, KLS Gogte
Institute of Technology, Belagavi,
Karnataka, India
Multimodal sentiment analysis using image
and text fusion for emotion detection
Uttam U. Deshpande1*, Supriya Shanbhag1, Amit Sukhasare1, Mahendra M. Dixit2, Rudragoud Patil3,
Sangeeta Sangani4*, Sowmyashree H. Srinivasaiah5, Swetha Goudar6 and Manjunath Managuli1
1 Introduction
People’s innate attitudes about a specific subject, person, or thing are known as their
sentiments. It is useful for us to communicate, learn, and make decisions when we are
aware of people’s attitudes. With the popularity of social media and mobile devices,
Discover Computing
Abstract
Social media has become an essential platform for expressing personal experiences
and emotions. Today’s youth frequently share images that reflect their emotional
states, including happiness, excitement, sadness, anxiety, and distress. Accurately
analyzing these images using new frameworks can offer beneficial insights into
the emotional well-being of individuals. Beyond mental health applications, image
sentiment analysis has significant potential in marketing and advertising. Brands and
Marketers can get a more comprehensive understanding of consumer sentiments
and preferences by examining the emotional reactions elicited by visual content. For
instance, companies can analyze images shared by customers to gauge sentiment
towards their products and services. Positive or negative feedback expressed through
images can offer practical insights for improving products and customer experience.
Additionally, Sentiment analysis is one tool that marketers can use to gauge the
effectiveness of their advertising campaigns. By analyzing the sentiments of images
associated with a campaign, they can determine which aspects resonate most
with the audience and adjust their strategies accordingly. Our research focuses on
creating an advanced multimodal sentiment analysis system that combines BERT
and Vision Transformers (ViT) to analyze textual and image data. High-precision
sentiment classification is achieved by our technique using a preprocessed AllenTAN
dataset from Hugging Face. It conducts sentiment analysis using BERT, creates
captions for unlabeled photos, and uses OCR to retrieve embedded image text.
The suggested ViT + BERT technique performs well with a variety of social network
content. The proposed system achieves an accuracy of 96.91%, demonstrating its
robust performance across diverse social media content and benchmark models.
This technology has several uses, particularly in social media monitoring to promote
mental health content, as teens frequently use visuals to describe their feelings.
Keywords Mental health, Image sentiment analysis, Emotion, AllenTAN, Vision
transformers (ViT), Optical character recognition (OCR), BERT

Page 2 of 24
Deshpande et al. Discover Computing          (2025) 28:230
individuals are posting text and images together to share their thoughts and feelings.
Sentiment analysis uses text, audio, video, and picture analysis to gather people’s view -
points, opinions, attitudes, and emotions [ 1–3]. For instance, product-based sentiment
analysis [4] is popular among consumers and e-commerce websites because it can assess
users’ emotional inclinations toward items and brands. Businesses may then utilize this
information to enhance the quality of their products and brand image. A business or
retailer may alter their operations accordingly based on the opinions of their customers
regarding their product or brand. The government can benefit from social media sen -
timent analysis [ 5] in understanding public views or positions on important events or
popular subjects. Public opinion can be influenced by government entities through the
assessment of online voting. For this reason, researchers in Artificial Intelligence have
been working to give machines the cognitive capacity to identify, understand, and com -
municate emotions over the past 20 years. Social media’s rapid growth in popularity
has had a profound impact on how people communicate and express their emotions in
recent years, making websites like Facebook, Instagram, and Twitter vital channels for
sharing experiences and sentiments via photos and captions. These platforms are now
essential for how people express their emotions, particularly young people, who fre -
quently do so by fusion of textual and visual aspects. The ability to evaluate and decipher
these emotions could provide an invaluable understanding of the emotional health of the
general population and open the door to prompt mental health interventions.
There are benefits and drawbacks to gathering and analyzing data from different
sources when compared to single-modal sentiment analysis. Since text and visuals typi -
cally come in pairs in real life, information is frequently not unimodal. Multimodal senti-
ment analysis, which seeks to identify and analyze feelings from data with a variety of
modalities, has garnered more and more attention from researchers in recent years [ 6].
Most early multimodal works rely on handcrafted features. Nevertheless, handcrafted
features are usually created with a limited amount of human expertise and are not able
to fully capture the high complexity of sentiment, which results in undesirable out -
comes. Three categories can be used to organize various fusion techniques: early fusion,
middle fusion, and late fusion. The primary means of achieving early fusion is feature
extraction from multi-modal data, followed by splicing, weighting, and other fusion
techniques. However, the fusion output may contain many redundant vectors, leading to
information redundancy and dependence and a poor fusion effect. Convolutional neu -
ral networks have been used in multimodal sentiment analysis with positive results in
recent years, thanks to the advancements in deep learning. The neural network is pri -
marily used to achieve intermediate fusion, sharing the shared network’s middle layer
as it goes through the fusion process. After training each modality to select the one that
best fits its needs, late fusion performs decision fusion using many classifiers to provide
predictions. However, late fusion is not very good at coordinating correlations across
the different modalities. However, most Convolutional Neural Networks (CNN)-based
methods either fuse characteristics obtained from several modalities [ 7] or allow for an
elementary understanding of the link between text and images [ 8]. Human emotions are
mostly elicited by specific regions [9] in images and are conveyed through phrases in the
commented text that goes along with the image. The current state of image sentiment
analysis techniques still faces some unresolved issues that require immediate attention.
For example, the accuracy of the image regions that feature extraction networks target is

Page 3 of 24
Deshpande et al. Discover Computing          (2025) 28:230
insufficient, information redundancy arises from the straightforward feature extraction
process for independent modalities, and the semantic correlation between multimodali -
ties is not sufficiently analyzed and fused.
The motivation behind this research is driven by the increasing concerns about mental
health, particularly among youth. Social media networks have observed a surge in posts
reflecting emotions such as sadness, anxiety, and depression, underscoring the require -
ment for monitoring instruments and understanding emotional well-being through
social media activity. Early detection of negative emotions can result in timely support
and intervention, potentially treating mental health conditions before their escalation.
This real-time sentiment analysis can function as a critical component in mental health
monitoring systems, enabling experts in mental health to identify at-risk individuals and
provide necessary support. This proposed work intends to promote content creation,
improve marketing strategies, and improve mental health monitoring by providing a
powerful tool for real-time sentiment analysis. We explore the possibility of applying
cutting-edge machine learning methods to important real-world problems by integrat -
ing Vision Transformers (ViT) and Bidirectional Encoder Representations from Trans -
formers (BERT) models in a single framework. The objectives of the proposed work are
summarized as follows,
i. Developing an integrated sentiment analysis system using ViT and BERT-based
models. Based on visual content and associated language, this system will reliably
classify photos into sentiment categories (positive, negative, and neutral) using deep
learning algorithms.
ii. Enhancing accuracy and efficiency of sentiment analysis through the integration
of ViT for image feature extraction and BERT for textual sentiment classification.
The goal is to achieve state-of-the-art performance in recognizing and interpreting
emotional cues from images and associated captions.
iii. Enable real-time sentiment analysis capabilities by providing instantaneous feedback
on the emotional content of images, facilitating prompt responses and interventions
where necessary.
iv. Ensure the system is scalable to handle large volumes of images from different social
media platforms. Integrate cross-modal analysis capabilities to correlate sentiment
between images and accompanying text, enhancing the depth and accuracy of
emotional understanding.
v. Implement mechanisms for continuous learning and model adaptation to evolving
trends and changes in user behavior on social media platforms. Extend sentiment
analysis capabilities to support multiple languages, accommodating diverse global
users and content across different linguistic contexts.
The structure of the paper is as follows: In Sect.  2, important past literature is reviewed.
The proposed methodology is presented in Sect.  3. The system architecture and imple -
mentation techniques are described in Sect.  4. The experimental results and analysis are
provided in Sect.  5. In Sect.  6, the research findings are summarized, and future work is
suggested.
2 Literature overview
This section reviews sentiment analysis literature.

Page 4 of 24
Deshpande et al. Discover Computing          (2025) 28:230
2.1 Multimodal sentiment analysis
In recent years, multi-modal sentiment analysis has drawn increasing attention, and
it is an exceedingly challenging research area. Unlike single-modal sentiment analy -
sis, multi-modal sentiment analysis incorporates several domains, including computer
vision, natural language processing, and others. It is a field of study that involves mul -
tiple disciplines. The incorporation of both verbal and nonverbal information, such as
visual and audio data, has boosted multimodal sentiment analysis to a prominent area of
study. Historically, multimodal fusion and representation learning have been the focus
of research.
Splicing, weighing, and other techniques are used to carry out the fusion process once
the feature extraction from different modal information is accomplished by the early
fusion method. Feature splicing creates a single bag of words [ 10] by merging text and
visuals to create the final representation. The interactive information approach [ 11]
gathers the underlying picture features and binary representation to extract text fea -
tures. The resultant similarity-based neighbourhood classifier is then subjected to binary
classification using the approach. Each modality’s data is trained independently in late
fusion, which then chooses the best classifier and provides the final fused result. First,
distinct characteristics for text and images were retrieved using CNN [ 12]. Next, differ-
ent emotions were predicted and examined using logistic regression. Finally, a weighted
fusion technique with an average was used to conduct the final emotion prediction
study. Modality-specific and modality-invariant representations were presented [ 13] for
multimodal representation learning. Depending on the stage at which fusion is imple -
mented, the information that is currently available on multimodal fusion can be divided
into two categories: early fusion and late fusion. Early attempts at cross-modal fusion
typically employed subtle attention mechanisms. A hybrid deep learning model [14] first
performs fine-grained analysis on multi-modal data and then utilizes a decision-level
multi-modal combination to categorize and output the data. A cross-modal converter
[15] was proposed to learn cross-modal attention to improve the target modality. After
learning the intra-modal representation, inter-modal fusion was accomplished using a
tensor fusion network and post-fusion approaches. However, this method did not allow
for any multimodal interaction. To solve this issue, a multi-tensor fusion method [ 15]
based on cross-modal feature extraction was put forth. However, this method ignored
any data transferred between the modalities and only roughly fused the image and text
modalities during the feature fusion phase. The global context of modalities was over -
looked despite the introduction of a multi-tensor fusion network [ 15] to depict inter -
actions between many bimodal pairs. Additionally, to enhance model performance, a
hybrid model that used a knowledge graph Long Short-Term Memory (LSTM) and CNN
was developed [ 16]. LSTMs’ temporal data memory functions and CNNs’ local feature
extraction powers are both utilized in this technique. However, the approach is depen -
dent on the structure of the knowledge graph; therefore, processing complex linguistic
phenomena such as puns and sarcasm may potentially generate instability in the model.
Creating a unified dataset was a critical component of our proposed research. We
combined and preprocessed datasets from various sources to ensure consistency and
accuracy in sentiment labels and image paths. This involved handling missing values,
standardizing sentiment labels, and ensuring that image paths were correctly mapped
to their corresponding sentiment labels. The comprehensive dataset served as the

Page 5 of 24
Deshpande et al. Discover Computing          (2025) 28:230
foundation for training and evaluating models, ensuring that the system could accurately
interpret a wide range of emotional expressions in images.
2.2 Vision transformers (ViT) and BERT-based models
When used to model sequential data, a Transformer is a non-looping sequence-to-
sequence design that can provide better depth, efficiency, and outcomes than cyclic
structures [17]. ViT and BERT are two models that are based on the Transformer. The
ViT vision model, which is built on the Transformer architecture, performs exception -
ally well [18, 19] in computer vision tasks with intriguing applications. It is predicated on
the idea of breaking up an image into smaller plots and using a self-attention process to
model and extract features from the images. The successful use of the Transformer for
language models is BERT [20–22], which achieves exceptional accuracy in a range of text
processing applications that extract features from text and picture data, respectively. The
open-source pre-trained BERT and ViT models are employed to accomplish these tasks.
A machine learning technique called multi-task learning (MTL) [ 23, 24] builds a model
to learn several related tasks at once. It can somewhat increase the model’s efficiency and
ability for generalization. By considering the correlations and contrasts between differ -
ent tasks, multitask learning can facilitate information transfer and interaction between
them while building a suitable model architecture and loss function. For MSA, multi-
task learning [25–27] has been widely utilized.
2.3 Enhancing multimodal sentiment analysis by integrating ViT-BERT
Significant progress has been made in multimodal sentiment analysis, especially with the
use of deep learning and attention-based methods. Particularly in practical applications
like social media analysis, e-commerce reviews, and content moderation, traditional
unimodal methods frequently fall short of capturing the complete semantic and emo -
tional complexity of information. A deeper comprehension of sentiment is provided by
multimodal models, which integrate textual and visual data. The development of fusion
techniques is highlighted in recent publications. A late fusion-based multi-task learning
framework [ 26] demonstrated cutting-edge performance on the gathered multimodal
dataset. A two-stage multi-task sentiment analysis framework [25] combined pre-trained
models with multi-task learning strategies. This framework improved multimodal senti -
ment classification performance and produced positive findings on multimodal datasets.
Multi-tensor fusion was presented [ 15] as a method to improve cross-modal represen -
tation learning and, consequently, the synergy between text and image inputs. A thor -
ough analysis of current fusion techniques and benchmark datasets was presented [ 8],
setting the stage for comparative analysis. A hybrid deep learning architecture tailored
for sentiment-rich data was presented [16], which also showed gains in identifying subtle
emotional indicators. A multi-task learning model that included specialized scoring and
cascade [27] concurrently executed intra- and inter-modal interactions to improve mul -
timodal sentiment representation skills. These models are developed using MSA, strug -
gle to produce a comprehensive comprehension of the emotional content when the text
fails to sufficiently convey the nuanced emotional aspects of the imagery.
The goal of our proposed work is to create a system for sentiment analysis of images
by using ViT and BERT-based models to extract hidden text, create captions for images,
and assess the overall sentiment. Applying transformer models to sequences of image

Page 6 of 24
Deshpande et al. Discover Computing          (2025) 28:230
patches, vision transformers provide state-of-the-art performance and have become
an excellent way to identify images. BERT-based models, on the other hand, have com -
pletely changed natural language processing by offering strong comprehension and
production capabilities for human language. The suggested method seeks to offer a
thorough comprehension of the emotions expressed through both textual and visual
information by combining both technologies. This research intends to promote content
production, improve marketing strategies, and improve mental health monitoring by
providing a powerful tool for real-time sentiment analysis. The integration of ViT and
BERT models in a unified framework demonstrates the potential of leveraging state-of-
the-art machine learning technologies to address critical real-world challenges. Not only
does this method offer sentiment categorization as positive, negative, or neutral, but it
also delves deeper into specific emotions such as sadness, anxiety, anger, and depres -
sion for negative sentiments, and happiness, joy, and excitement for positive sentiments,
thereby offering a nuanced understanding of user emotions. We test our model on the
AllenTAN image sentiment dataset, which provides a carefully chosen collection of pho-
tos from various web sources and social media platforms.
3 Methodology
As shown in Fig. 1, the AllenTAN/image sentiment dataset [ 28] forms the core of our
image sentiment analysis, offering a curated selection of images sourced from diverse
social media platforms and online repositories. Each image in this dataset is meticu -
lously annotated with sentiment labels, categorizing them into positive, negative, or
neutral sentiments based on user interactions and annotations. This dataset is instru -
mental in training and evaluating our sentiment analysis model, providing a rich variety
of visual content across different contexts.

The dataset possesses the following characteristics,
i. Source Diversity: Images are collected from different platforms and online repositories,
ensuring a broad representation of user-generated content.
ii. Sentiment Labels: Each image is labeled with sentiment categories, enabling the model
to learn and classify sentiments effectively.
iii. Metadata Enrichment : Alongside sentiment labels, images are accompanied by
metadata such as captions, tags, and timestamps. These metadata elements provide
Fig. 1 AllenTAN dataset [28]

Page 7 of 24
Deshpande et al. Discover Computing          (2025) 28:230
crucial contextual information, enriching the understanding of image content and
sentiment nuances.
Sentiment labels are assigned through a manual annotation process where human anno-
tators categorize images based on visual cues and accompanying textual information.
Rigorous quality checks ensure the accuracy and consistency of sentiment annotations,
minimizing labeling bias and errors. The AllenTAN/image sentiment dataset serves as
the primary training set for our sentiment analysis model. Its diverse nature and com -
prehensive annotation facilitate robust model learning and generalization. This datas -
et’s images are utilized to assess the models, measuring accuracy, precision, recall, and
other evaluation metrics to assess sentiment classification effectiveness. Hugging Face
provides the AllenTAN/image sentiment dataset, which has previously undergone pre -
processing. This guarantees constant sentiment tagging, metadata integration, and
image resolution. To improve model generalization, we supplemented this with an addi -
tional dataset of 10,000 images. This dataset augments the primary dataset by offering a
broader variety of visual content across various domains and contexts. While not anno -
tated with sentiment labels as comprehensively as the primary dataset, the supplemen -
tary dataset enriches our training corpus with additional diversity and variability.
3.1 Data preprocessing
A common format for raw picture data is created during image preprocessing so that
deep learning models can use it to analyze sentiment. Images in the dataset often vary in
resolution and size. Standardizing images to a common resolution, such as 224 × 224 pix-
els, ensures uniformity and compatibility across the dataset. This standardization simpli-
fies the input requirements for neural networks, which typically expect fixed-size inputs
for efficient processing. We perform normalization to adjust the pixel values of images
to a standardized range, typically [0, 1] or [− 1, 1]. Normalizing pixel values enhances
model stability during training and convergence, preventing the dominance of certain
features due to differing scales. Data augmentation techniques are applied to increase
the diversity and robustness of the training dataset. Augmentation methods such as
rotation, flipping, cropping, and brightness adjustments generate variations of the origi -
nal images, effectively increasing the dataset size and improving model generalization.
The data preprocessing steps are described in Fig. 2.
3.1.1 Data cleaning
Data cleaning involves removing noise and irrelevant characters from textual metadata,
ensuring that the processed text retains only the essential semantic content. Here are the
common steps involved in text cleaning. HTML tags and special characters, such as ‘<‘,
‘>’ , and ‘&’ , are typically found in web-based textual data. These tags do not contribute to
the semantic meaning and are removed to clean the text. Punctuation marks (e.g., ‘. ‘, ‘, ‘,
‘?‘) and numeric characters are often irrelevant for sentiment analysis tasks and can be
safely removed. This step helps reduce the vocabulary size and computational complex -
ity. Text normalization involves converting all characters to lowercase. This standardizes
the text and ensures that words with different cases (e.g., ‘Hello’ and ‘hello’) are treated
as identical tokens during tokenization.

Page 8 of 24
Deshpande et al. Discover Computing          (2025) 28:230
3.1.2 Tokenization
Tokenization is the process of breaking down textual data into smaller units, such as
words or sub-words, which will be converted into numerical representations. Effec -
tive tokenization is important for handling text data in deep learning models. Modern
tokenization methods, particularly those used with transformer-based models, employ
sub-word tokenization techniques that split words into meaningful subunits called
tokens. This approach allows the model to handle rare words and out-of-vocabulary
terms effectively. Transformer-based models like BERT shown in Fig.  3, use sub-word
tokenization, such as WordPiece or Byte-Pair Encoding (BPE), to tokenize text.
3.1.3 Embedding techniques
 Embedding techniques transform textual data from a sparse, high-dimensional space
(vocabulary space) into a dense, lower-dimensional vector space (embedding space).
This embedding detects semantic resemblances between words and enables deep learn -
ing models to understand the contextual meaning of text. We use the following embed -
ding techniques in our proposed approach.
Word embedding (Word2Vec, GloVe) Word embedding represents words as dense vec -
tors in an embedding space where similar words are mapped to nearby points. Word2Vec
and GloVe (Global Vectors for Word Representation) are some methods for generating
word embeddings. Using the Word2Vec approach, the word representations are learned
in a dispersed manner. Whereas GloVe embeddings are trained on global word-word co-
occurrence statistics from a corpus and capture semantic bonding between words.
Transformer-Based embedding (BERT embedding)  Transformer models, such as BERT,
have revolutionized NLP by capturing bidirectional contextual information. BERT
embeddings are generated by pre-training a deep bidirectional model on large corpora.
Fig. 2 Data preprocessing

Page 9 of 24
Deshpande et al. Discover Computing          (2025) 28:230
BERT uses attention mechanisms to generate contextual embeddings that consider both
contexts of each token. These embeddings are effective for many different NLP tasks,
like sentiment analysis and text classification. Because BERT [ 29] has demonstrated the
capacity to capture complex contextual relationships in text and has built-in multilingual
support through models such as mBERT, we used it. BERT creates contextual embed -
dings, which enable it to distinguish word meanings based on surrounding text, in con -
trast to conventional static word embeddings like Word2Vec [30] and GloVe [31], which
assign a single vector per word regardless of context. BERT showed better generalization
and accuracy in both binary and multi-class sentiment tasks in comparative sentiment
classification trials. Its performance was especially noteworthy when it came to managing
negation, sarcasm, and context-dependent phrases—all of which are frequently challeng-
ing for conventional embedding techniques. This conclusion has been corroborated by
earlier research; for example, the BERT-based models perform noticeably better in senti-
ment classification across a variety of datasets than traditional embedding-based models
[32]. BERT was kept as the preferred embedding method due to its strong performance.
Through transformer-based parallelization, BERT maintained computational efficiency
while continuously providing greater precision, recall, and F1-scores, even when tested
alongside other embeddings in different settings. We utilized BERT for its superior con -
textual understanding and multilingual adaptability. According to comparative tests,
BERT constantly performed better in sentiment prediction than traditional embeddings
(Word2Vec, GloVe). BERT was retained because of its accuracy and efficiency, even when
other embeddings were taken into consideration.
3.2 Fusion of image and textual data
After completing the preprocessing steps for image and textual data, the next critical
phase is a fusion of these two modalities into a cohesive data pipeline. Before classifi -
cation, textual embeddings (BERT) and visual features (ViT) are combined via inter -
mediate fusion. Hence, the accuracy of sentiment inference is improved by the model’s
Fig. 3 Data tokenization

Page 10 of 24
Deshpande et al. Discover Computing          (2025) 28:230
ability to jointly assess multimodal information. Here, each image is paired with its cor -
responding textual features (captions, tags) to create composite input examples. This
ensures that visual and textual information are considered jointly during model train -
ing and inference. Figure  4 illustrates the process of intermediate fusion of textual and
visual data in a structured pipeline to demonstrate how multimodal sentiment analysis
operates using ViT and BERT. Two inputs are used in the process: an image and any text
that goes with it, like a description, tags, or caption. In the example, the picture shows
a serene country road with some clouds in the sky. A Vision Transformer (ViT) is used
to process a picture to extract high-level visual information, such as a product photo or
user-generated content. This image is converted into an image matrix (III), a numerical
format that contains the spatial and pixel-level information required for machine learn -
ing models. At the same time, BERT processes accompanying text (such as a product
review or caption) to produce contextual textual embeddings. Tokenization is used to
preprocess the image description text, producing a series of textual tokens (TTT). These
tokens stand for significant linguistic units that language models can assess. After that,
the model can develop joint representations that capture interactions between modali -
ties by concatenating (intermediate fusion) the textual embeddings and visual character-
istics in an intermediate layer. The text and image data are fed into a structured pipeline,
a deep learning-based system made to process and combine multimodal inputs. The
objective here is to identify whether an input image and the text convey good, negative,
or neutral emotional expressions. Attention mechanisms known as fusion layers can
teach us the connections between textual and visual information. For example, a picture
by itself could provide a sense of serenity, but the caption may add background informa-
tion that changes the impression. A sentiment label—positive, negative, or neutral—is
the pipeline’s final output, which is determined by the combined interpretation of the
text and the image.
3.3 Convolutional neural networks (CNNs)
CNNs are used for extracting visual features from images. They consist of layers that
apply filters to images to capture hierarchical patterns such as edges, textures, and
shapes. Multiple layers help in capturing local visual context and features required for
Fig. 4 Intermediate fusion process in multimodal sentiment analysis using Vision Transformer (ViT) for visual fea -
tures and BERT for textual embeddings

Page 11 of 24
Deshpande et al. Discover Computing          (2025) 28:230
understanding the sentiment expressed through visual content. CNNs are pivotal in
our image sentiment analysis research, primarily through the Vision Transformer (ViT)
model. The Vision Transformer (ViT) is a transformer-based model made for image clas-
sification tasks. It processes images by dividing them into fixed-size patches and treating
them as tokens. ViT then applies transformer layers to capture global dependencies and
relationships between these patches, as shown in Fig. 5.
While ViT is not traditional CNN architecture, it adopts its principles in its design.
CNNs are known for the ability to automatically learn data representation hierarchically,
for tasks such as image classification and feature extraction. In ViT, the model breaks
down images into smaller patches and processes them through multiple layers of self-
attention mechanisms. These mechanisms allow ViT to capture spatial dependencies
and context within the image, like how CNNs detect patterns like edges, textures, and
shapes. This process enables ViT to effectively encode visual information from images,
which is crucial for understanding the sentiment conveyed through visual content on
social media platforms and other sources. The pipeline steps are below:
i. Data Preprocessing: Images are divided into parts of fixed size. Let XXX represent the
input image, and xijx_{ij}xij denote the patch at position (i, j)(i, j)(i, j). Each patch is
reshaped into a vector and embedded with positional encodings.
ii. Transformer Encoder: ViT employs a self-attention mechanism to compute attention
scores between all pairs of patches xijx_{ij}xij and aggregate information across the
entire image. Following self-attention, a multi-layer perceptron (MLP) processes each
patch’s aggregated features to capture nonlinear transformations:
Fig. 5 ViT model representation

Page 12 of 24
Deshpande et al. Discover Computing          (2025) 28:230
iii. Pretrained Weights and Fine-tuning : ViT models are pre-trained on large-scale
datasets like ImageNet.
3.4 Natural language processing (NLP) techniques
NLP plays an important role in our research, especially in using the BERT model. BERT
is an architecture that excels in understanding and processing textual data. In our image
sentiment analysis system, BERT is utilized to analyze textual metadata associated with
images, such as captions and descriptions. These textual inputs often provide additional
context and sentiment cues that complement the visual content, as highlighted in Fig.  6.
BERT’s ability to capture bidirectional context and semantic meaning allows it to infer
the sentiment expressed in the text accurately.
By tokenizing context and adding textual inputs into dense vector representations,
BERT transforms raw text into numerical formats that can be processed effectively. The
pipeline steps are below:
i. Tokenization: Textual metadata (captions, tags) associated with images are tokenized
using the BERT tokenizer, which segments words into tokens and sub-word units.
BERT embeds map tokens into dense vector representations that preserve semantic
relationships and contextual meanings.
ii. Transformer Encoder : Like ViT, BERT employs self-attention and MLP layers to
process token embeddings and capture contextual dependencies.
iii. Pre-trained Weights and Fine-tuning: BERT models are pre-trained on large-scale text
corpora using masked language modeling and next-sentence prediction tasks. During
fine-tuning of your textual metadata, BERT’s weights are adjusted to optimize for
sentiment prediction. These steps are depicted in Fig. 7.
3.5 Integration of CNNs and NLP
The integration of CNNs (ViT) and NLP techniques (BERT) forms the backbone of our
image sentiment analysis approach. This hybrid approach leverages the strengths of both
domains: CNNs for processing visual content and extracting visual features, and NLP
for understanding textual semantics and sentiment. By combining these techniques, our
system can perform comprehensive sentiment analysis across multimedia data sources.
For instance, ViT uses image processing to identify visual characteristics that are then
combined with BERT’s analysis of textual metadata to predict sentiment labels such as
Fig. 6 Natural language processing representation

Page 13 of 24
Deshpande et al. Discover Computing          (2025) 28:230
positive, negative, or neutral. This integration ensures that our system can handle the
complexities of sentiment analysis in diverse contexts, such as social media posts, mar -
keting materials, and user-generated content. Moreover, the synergistic use of CNNs
and NLP enhances the robustness and interpretability of our sentiment analysis model,
providing deeper insights into the emotional content conveyed through multimedia
content.
4 Implementation
The proposed implementation methods are indicated in Fig. 8. These steps are discussed
in detail later.
4.1 Hugging face dataset
Hugging Face is a leading provider of open-source libraries and pre-trained models.
Their offerings include the Transformers library, Tokenizers, and Datasets, which make
it easier to create and use cutting-edge machine-learning models. It is designed pri -
marily for NLP tasks. The Transformers library provides access to various pre-trained
models like BERT, GPT, RoBERTa, and, more recently, Vision Transformer (ViT) for
image-related tasks. It mainly supports model architecture for various tasks like classifi -
cation and language generation. The major advantage is that the developers can leverage
pre-trained models, fine-tune them on specific tasks using transfer learning, and inte -
grate them into custom applications. This library supports various tokenization algo -
rithms, including byte-pair encoding (BPE), WordPiece, and sentencepiece, which are
important in handling different languages and tokenization needs. Tokenizers transform
unprocessed text into numerical tokens suitable for model input. The library also pro -
vides access to a vast collection of datasets through the dataset library. It facilitates the
seamless integration of datasets into machine learning pipelines for training, evaluation,
and testing models.
4.2 Vision transformer (ViT) architecture
Although transformer architecture is now the industry standard for jobs involving
natural language processing, there are still few uses for it in computer vision. In vision,
attention is either employed in tandem with convolutional networks or to substitute cer-
tain convolutional network components while maintaining the general architecture of
the network. A deep learning architecture called “Vision Transformers” (ViTs) uses the
Fig. 7 BERT model representation

Page 14 of 24
Deshpande et al. Discover Computing          (2025) 28:230
ideas of transformers, which were first created for natural language processing, to ana -
lyze images. ViT splits the image into fixed-size patches (e.g., 16 × 16 pixels) rather than
processing the full image as a whole or through local receptive fields (as in CNNs), as
indicated in Fig.  9. After being flattened and linearly embedded, each patch is handled
similarly to a word in a phrase. After passing these patch embeddings through a trans -
former encoder, self-attention mechanisms can determine the relationships between
Fig. 9 ViT transformer architecture [33]

Fig. 8 Implementation flow diagram

Page 15 of 24
Deshpande et al. Discover Computing          (2025) 28:230
various patches. The model’s ability to capture long-range dependencies and interac -
tions across remote areas of the image is made possible by its global attention, which is
essential for sentiment-related elements, including body language, face emotions, and
background context. The input sequence contains a unique [CLS] token, and the final
embedding of this token represents the image. For classification tasks like identifying the
image’s emotional state (e.g., joyful, sad, neutral), this embedding is utilized. ViT can be
used in conjunction with language models such as CLIP or BERT for multimodal sen -
timent analysis. This enables the model to combine textual and visual data, extracting
context from images and related text (such as social media postings or memes).
We demonstrate that this reliance on CNNs is not required, and that image clas -
sification tasks can be effectively completed with a pure transformer applied directly
to sequences of picture patches. Vision Transformer (ViT) achieves superior perfor -
mance to state-of-the-art convolutional networks with significantly less computational
resources when pre-trained on large amounts of data and transferred to multiple mid-
sized or small image recognition benchmarks (ImageNet, CIFAR-100, VTAB, etc.). The
Transformers library is pivotal for integrating pre-trained models into machine-learn -
ing workflows. It supports both PyTorch and TensorFlow, allowing flexibility in model
implementation and deployment. The ViT transformer architecture is diverse and pro -
vides a spectrum of transformer-based architecture tailored for various tasks in NLP and
multimodal domains.

The models range from basic models like BERT to sophisticated models like GPT-
3, catering to different levels of complexity and task requirements. This enables us to
train models from scratch or fine-tune pre-trained models on specific datasets. This
architecture integrates seamlessly with PyTorch and TensorFlow ecosystems, leverag -
ing their capabilities for efficient computation and model optimization. The architec -
ture provides high-level abstractions known as pipelines, simplifying the application of
pre-trained models for various tasks like text generation, sentiment analysis, and image
classification.
4.3 Implementation pipeline
Each experiment was carried out on an NVIDIA GeForce GTX GPU using the Hug -
ging Face Transformers framework and PyTorch. To preprocess the data, we scaled the
images to 224 × 224 pixels and manually padded and cropped text material to a maxi -
mum length of 50 words. Using BERT, OCR was used to extract and examine embed -
ded text. Previously trained vision-language models were used to produce captions for
text-free images. The original label distribution was preserved by randomly dividing the
dataset into training, validation, and test sets in an 8:1:1 ratio after data transformation.
To minimize sentiment bias, images and text were sourced from diverse platforms and
demographics. We use CrossEntropyLoss, which works well for multi-class classification
applications, to train the sentiment analysis model. The Adam optimizer was employed,
with a weight decay set to 3e− 5 and an initial learning rate of 0.001 that was lowered by a
factor of 10 every 10 epochs.
As discussed earlier, Fig.  8 describes the implementation pipeline of the proposed
method. The steps are explained below.

Page 16 of 24
Deshpande et al. Discover Computing          (2025) 28:230
Loading and preprocessing data Metadata containing image names and sentiment labels
are loaded along with an image directory. Additional data from AllenTAN/image_senti -
ment is extracted, and sentiment labels are processed.
Combining datasets  Metadata and additional data from datasets are combined into a
unified data frame to consolidate information from multiple sources. This combined
dataset is crucial for subsequent tokenization and model training stages.
Tokenization and dataset preparation Combined textual data is tokenized using a BERT
tokenizer. The dataset is then converted into the Hugging Face Dataset format and
tokenized in batches to facilitate efficient model training. This step ensures that textual
inputs are formatted appropriately for deep learning models.
Model loading The pre-trained Vision Transformer (ViT) model is loaded from Hugging
Face’s model hub for image classification tasks. Similarly, the BERT model is loaded to
carry out sentiment analysis tasks, specifically multilingual sentiment classification.
4.4 Evaluation metrics
We evaluate a model’s performance using the following metrics.
Accuracy This measures the general accuracy of the model’s predictions, showing the
percentage of cases that were correctly classified.
Precision and recall  Precision measures the percentage of genuine positive forecasts
among all positives. While recall measures the percentage of true positives found among
all actual positives.
F1-score The mean of recall and precision together provides a balanced measure of per -
formance, especially important for datasets that are not balanced.
Evaluation loss This indicates the model’s performance on the evaluation set; lower val -
ues indicate better performance.
Evaluation runtime It provides information regarding the time taken to run the model,
in turn providing insights into the model’s efficiency.
Evaluation samples per second  The number of samples processed per second during
evaluation is calculated to obtain the model’s processing speed.
Evaluation steps per second  The number of steps processed per second during evalua -
tion, further indicating the model’s efficiency.
5 Results and discussion
A significant strength of our system lies in its ability to handle multimedia content with
diverse characteristics. When analyzing images containing embedded text, our model
effectively utilized optical character recognition (OCR) to extract textual content. The
text was then examined using BERT-based models to derive sentimental insights. For

Page 17 of 24
Deshpande et al. Discover Computing          (2025) 28:230
images without embedded text, our Vision Transformer (ViT) model generated captions
based on visual features for sentiment using BERT. This dual approach ensured com -
prehensive sentiment analysis irrespective of whether images contained readable text or
relied solely on visual cues. Our system’s versatility and accuracy make it highly suitable
for real-world applications across various domains. Figure  10 describes the sentiment
distribution carried out in our work.
In social media monitoring, the model accurately captured sentiment trends in user-
generated content, providing valuable insights for brand reputation management and
customer engagement strategies. In marketing and advertising, the system effectively
analyzes sentiment in promotional materials and customer feedback, aiding in campaign
optimization and audience targeting. Testing with images collected from different social
media handles further demonstrated the model’s robustness and its ability to accurately
predict sentiments in real-world, dynamic environments. Beyond traditional applica -
tions, our model contributes to understanding the mental health of social media users
by analyzing the sentiment of their posts. By identifying patterns of positive, negative,
or neutral sentiments in user-generated content, the system provides perceptions of the
emotional states and well-being of users. This capability is important for proactive men -
tal health monitoring, enabling early intervention strategies and support systems based
on sentiment analysis of social media posts. Figure  11 shows an example of an output by
our proposed system where positive sentiments were correctly classified.
Our proposed research demonstrated scalability in handling large volumes of multi -
media data, supported by efficient data preprocessing and optimized model architec -
tures. Utilizing GPU acceleration enhances computational efficiency, enabling rapid
processing of images and text for sentiment analysis tasks. This scalability ensures the
system’s suitability for deployment in dynamic environments where real-time or batch
processing of multimedia content is required. The Receiver Operating Characteristic
Fig. 10 Sentiment distribution plot

Page 18 of 24
Deshpande et al. Discover Computing          (2025) 28:230
curve, also known as the ROC curve, describes the performance of a binary classifier
at various classification thresholds and is shown graphically. The ROC plot in Fig.  12
depicts the model’s performance. A diagonal line from the bottom left to the top right
corner of this plot indicates that our proposed model is a perfect classifier that correctly
identifies all positive cases and no negative cases.
The neural network’s parameters are changed during training to minimize a cost func-
tion. Assessing a model’s accuracy on a subset of data is known as validation. The ability
of a model to predict the right output given the input is known as accuracy. Figure  13
shows the proposed models’ training and validation performances. Our model achieved
91.11% training accuracy and 86.77% validation accuracy at 10 epochs. These values
keep on growing with an increase in epochs as indicated in Fig. 13a.
Two important measures for tracking the model’s performance and capacity for gener-
alization are training loss and validation loss. The inaccuracy of the data that the model
was trained on is referred to as training loss. The error on unseen data, or validation loss,
is used to assess the model’s performance outside of the training dataset. Our model pro-
duced training and validation losses of 0.223 and 0.289 at 10 epochs. These values fur -
ther decrease with the increase of epochs concerning time and are indicated in Fig. 13b.
The proposed ViT + BERT multimodal sentiment analysis model’s confusion matrix,
shown in Fig. 14, demonstrates outstanding performance for all three sentiment classes:
Positive, Neutral, and Negative. With 966 out of 992 samples accurately predicted, our
model showed impressive accuracy. Each class has many correct classifications, as shown
Fig. 11 Sentimental analysis result (a) Test image 1 outputted as positive sentiment (b) Test image 2 outputted as
positive sentiment (c) Other sample images used for testing.

Page 19 of 24
Deshpande et al. Discover Computing          (2025) 28:230
by the diagonal members of the matrix (323 Positive, 315 Neutral, and 328 Negative).
The few misclassifications—mostly neighbouring feelings, such as a few Positives classi -
fied as Neutral or Negatives—reflect the nuanced nature of sentiment overlap. Overall,
the matrix shows that the model manages sentiment predictions with few errors. The
metrics from the confusion matrix are calculated as below:
Accuracy This measures the overall percentage of correct predictions. In this case, accu-
racy is calculated as the ratio of correct predictions to total samples.
Accuracy = TP + TN + True Neutral Total Samples = 323 + 315 + 328 961 = 96 .91% (1)
Fig. 13 Model training and validation performance (a) Accuracy (b) Loss. (a) Training and validation accuracy, (b)
Training and validation loss

Fig. 12 ROC curve plot

Page 20 of 24
Deshpande et al. Discover Computing          (2025) 28:230
Precision Precision indicates the accuracy of the positive predictions. In other words, it
measures how many of the samples predicted as positive are positive.
Precision = TP TP + FP = 323 323 + 5 =0 .970 (2)
A precision of 0.970 means that when the model predicts a sample to be positive, there is
a 97.0% chance it is indeed positive.
Recall Recall is a measure of how many actual positive samples the model correctly
identified.
Recall = TP TP + FN = 323 323 + 4 =0 .969 (3)
This indicates that the model identified 96.9% of all the actual positive samples.
F1 score  The F1-score combines both precision and recall into a single metric, which
is especially useful when dealing with imbalanced datasets. It is the harmonic mean of
precision and recall.
F1 Score =2 x Precision + Recall Precision × Recall =0 .969 (4)
With an accuracy of 96.91%, the proposed ViT + BERT image sentiment analysis model
predicts over 97% of the samples correctly, indicating good overall performance. The
model’s performance was further validated by precision, recall, and F1-score measures,
which guaranteed accurate sentiment categorization for positive, negative, and neutral
sentiments. According to the precision (0.970), the model predicts positive, neutral, or
Fig. 14 Confusion matrix of multi-class sentiment analysis for the proposed ViT + BERT model

Page 21 of 24
Deshpande et al. Discover Computing          (2025) 28:230
negative labels with an average accuracy of 97%. The recall (0.969) shows that the model
successfully identifies over 97% of the actual positive, neutral, or negative samples. The
F1 score of 0.969, which displays the balance between the two criteria, validates the
model’s capacity to efficiently manage precision and recall. Table 1 provides an overview
of these findings.
We compared our method with several baseline models to verify its effectiveness. The
embedding technique developed by ViT + Word2Vec [ 30] produced ground-breaking
results for Word2Vec, proving the efficacy of both visual and textual representations
in sentiment classification. The BERT and ViT + Word2Vec models were based on a
Vision Transformers (ViT) in the forefront of visual-language integration [ 34]. In the
present analysis, the models obtained an F1-score of 0.901 and an impressive accuracy
of 91.8%, respectively. Like techniques that incorporate complex feature extractors, a
novel LSTM–CNN hybrid with grid search optimization was presented [ 35] employ -
ing ResNet and GloVe (Global Vectors for Word Representation) embeddings, attain -
ing 88.6% accuracy and a 0.875 F1-score. Recent studies have shown that different deep
learning architectures have improved sentiment analysis model evaluation. The efficacy
of sequence-aware architecture was confirmed by a CNN-LSTM hybrid model [ 36] on
tweets regarding monkeypox, which demonstrated an accuracy of 84.3% and an F1-score
of 0.807. The comparative analysis is presented in Table 2 below.
Our model shows significant improvements due to the synergistic integration of ViT
and BERT techniques over other benchmark models. To evaluate each component’s con-
tribution to overall performance, we conducted an ablation study, and it is summarized
in Table 3. The results demonstrate the critical role of each module, particularly the tex -
tual fusion via BERT.
In multimodal sentiment analysis, dataset constraints can have a major effect on the
generalizability and effectiveness of the model. The lack of diversity in many current
Table 1 Proposed ViT + BERT models’ performance results
Evaluation metric Values
Loss 0.137
Accuracy 96.91%
Precision 0.970
Recall 0.969
F1 score 0.969
Samples per second 0.847
Steps per second 0.213
Table 2 Performance comparison with benchmark models
Model ViT + Word2Vec
[34]
ResNet-50 + GloVe
[35]
CNN + LSTM
[36]
ViT + BERT (proposed)
Accuracy 91.8% 88.6% 84.3% 96.91%
F1-score 0.901 0.875 0.807 0.969
Table 3 Ablation study results for ViT, BERT, and OCR configurations
Configuration Without OCR Without Captioning Without BERT
(only ViT)
Full Model
(ViT + BERT + OCR)
Accuracy 92.1% 90.3% 88.7% 96.91%
F1-Score 0.921 0.910 0.880 0.969

Page 22 of 24
Deshpande et al. Discover Computing          (2025) 28:230
datasets, which are frequently skewed toward languages, cultural contexts, or domains
(such as social media or movie reviews), hinders the model’s capacity to generalize to
cross-domain, real-world situations. Another frequent problem is data imbalance, which
causes skewed predictions by favoring sentiment classes (such as positive or neutral).
Errors in sentiment tagging can be introduced by noisy or poor-quality data, especially
in user-generated material. Furthermore, the model’s capacity to acquire significant mul-
timodal representations may be hampered by modalities that are not aligned, such as
text and images that are not matched. Lastly, multimodal datasets are frequently smaller
in scale than unimodal datasets, which restricts the ability to train more intricate models
and raises the possibility of overfitting.
Although there are legitimate worries about relying too much on pre-trained models
such as ViT and BERT in multimodal sentiment analysis, their application is supported
by the reliable performance improvements they provide on a variety of tasks and datas -
ets. These models reduce the computational and data constraints associated with train -
ing from scratch and enable efficient transfer learning by encapsulating massive amounts
of linguistic and visual knowledge obtained from large-scale data. Pre-trained models
are strong bases that researchers may modify and refine, encouraging experimentation
with new architectures, fusion techniques, and domain-specific improvements rather
than stifling creativity. As a result, using pre-trained models speeds up development
while preserving space for creativity and domain adaptation.
6 Conclusion
We developed an advanced image sentiment analysis system that leverages cutting-edge
deep learning models to analyze both visual and textual content. By integrating Vision
Transformers (ViT) for extracting intricate visual features and BERT-based models for
analyzing textual sentiment, we created a comprehensive framework capable of accu -
rately predicting emotions like positive, negative, and neutral from social media images
and other sources. Our experiments demonstrated the system’s effectiveness in handling
images with embedded text and complex visual elements. The combination of ViT and
BERT allowed for high accuracy in sentiment prediction, making the system versatile
across various types of social media posts and marketing content. This versatility is
crucial for applications such as digital marketing, mental health monitoring, and pub -
lic opinion analysis. The work also highlighted the potential of image sentiment anal -
ysis in assessing the emotional well-being of social media users, offering insights into
online sentiment trends. Our proposed ViT + BERT system produced exceptional accu -
racy (96.91%) and robustness for different sentiment predictions over other benchmark
models.
However, multimodal sentiment analysis models frequently encounter dataset issues
like imbalanced sentiment classes, a lack of contextual richness across domains, and
inadequate modality diversity. Since ViT and BERT-based multimodal sentiment anal -
ysis models reliance on pre-trained models can limit performance because of domain
mismatch, inadequate modeling of cross-modal interactions, and excessive fine-tuning
computational costs.
The development of large-scale, balanced, and context-aware multimodal datasets
that better represent real-world situations and facilitate fine-grained sentiment under -
standing should be the top priority of future research. Effective fine-tuning methods,

Page 23 of 24
Deshpande et al. Discover Computing          (2025) 28:230
domain-adaptive pre-training, and building architectures that more accurately represent
complex sentiment across modalities can overcome pre-trained model limitations. Look-
ing forward, expanding multilingual support, refining text extraction through enhanced
OCR, and enabling real-time analysis can increase the system’s accuracy, scalability, and
real-world applicability. In conclusion, this work underscores the transformative power
of combining NLP and computer vision for sentiment analysis. By utilizing cutting-edge
AI technologies, our system can provide deeper insights into emotional dynamics in the
digital landscape, empowering businesses and researchers to better understand user
behaviors.
Author contributions
Authors U.D., S.S., A.S, and M.D. were involved in methodology, Formal analysis, conceptualization, Software,
Investigation, and overall Project Supervision. Authors R.P ., S. Sanagni, and S.H.S. were involved in Data curation, Formal
analysis, and writing—original draft.Authors S.G. and M.M. were involved in Writing, review & editing, and Investigation.
Funding
Open access funding provided by Manipal Academy of Higher Education, Manipal
Data availability
Data sharing not applicable to this article as no datasets were generated or analysed during the current study.
Declarations
Ethics approval and consent to participate
This research did not involve human participants or animals; hence ethical approval was not required.
Consent for publication
Not applicable, as no personal data, images, or details of individual participants are included in this manuscript.
Competing interests
The authors declare no competing interests.
Received: 15 May 2025 / Accepted: 13 October 2025
References
1. Hu R, Rui L, Zeng P , Chen L, Fan X. Text sentiment analysis: a review. In Proceedings of the 2018 IEEE 4th International
Conference on Computer and Communications (ICCC), Chengdu, China, 7–10 December 2018; IEEE: Piscataway, NJ, USA,
2018.
2. Cai Z, Cao D, Ji R. Video (GIF) sentiment analysis using large-scale mid-level ontology. ArXiv. 2015. ArXiv:1506.00765.
3. Xu C, Cetintas S, Lee KC, Li LJ. Visual sentiment prediction with deep convolutional neural networks. ArXiv. 2014.
ArXiv:1411.5731.
4. Tang D, Qin B, Liu T. Learning semantic representations of users and products for document level sentiment classification.
In Proceedings of the 53rd annual meeting of the association for computational linguistics and the 7th international joint
conference on natural language processing, Beijing, China, 26–31 July 2015; Volume 1: Long Papers, pp. 1014–1023.
5. Ibrahim M, Abdillah O, Wicaksono AF, Adriani M. Buzzer detection and sentiment analysis for predicting presidential
election results in a twitter nation. In Proceedings of the 2015 IEEE International Conference on Data Mining Workshop
(ICDMW), Atlantic City, NJ, USA, 14–17 November 2015; IEEE: Piscataway, NJ, USA; 2015. pp. 1348–1353.
6. Yue L, Chen W, Li X, Zuo W, Yin M. A survey of sentiment analysis in social media. Knowl Inf Syst. 2019;60(2):617–63.
7. Guo W, Zhang Y, Cai X, Meng L, Yang J, Yuan X. LD-MAN: Layout-driven multimodal attention network for online news
sentiment recognition. IEEE Trans Multimedia. 2021;23:1785–98. https://doi.org/10.1109/TMM.2020.3003648.
8. Gandhi A, Adhvaryu KU, Poria S, Cambria E, Hussain A. Multimodal sentiment analysis: A systematic review of history,
datasets, multimodal fusion methods, applications, challenges and future directions. Inform Fusion. 2022;91:424–44.  h t t p s :
/ / d o i . o r g / 1 0 . 1 0 1 6 / j . i n ff   u s . 2 0 2 2     . 09.025.
9. She D, Yang J, Cheng M, Lai Y, Rosin PL, Wang L. WSCNet: weakly supervised coupled networks for visual sentiment clas-
sification and detection. IEEE Trans Multimedia. 2020;22(5):1358–71. https://doi.org/10.1109/TMM.2019.2939744.
10. Wang M, Cao D, Li L, Li S, Ji R. Microblog sentiment analysis based on cross-media bag-of-words model. In Proceedings of
the international conference on internet multimedia computing and service, Xiamen, China, 10–12 July 2014; pp. 76–80.
11. Zhang Y, Shang L, Jia X. Sentiment analysis on microblogging by integrating text and image features. In Proceedings of
the Pacific-Asia conference on knowledge discovery and data mining, Ho Chi Minh City, Vietnam, 19–22 May 2015; pp.
52–63. 26.
12. Yu Y, Lin H, Meng J, Zhao Z. Visual and textual sentiment analysis of a microblog using deep convolutional neural net-
works. Algorithms. 2016;9:41.
13. Tsai YH, Bai S, Liang PP , Kolter JZ, Morency L, Salakhutdinov R. 2019. Multimodal transformer for unaligned multimodal
language sequences. In Proceedings of the Conference. Association for Computational Linguistics Meeting, Florence, Italy,
6558–69. Vol. 2019. NIH Public Access.

Page 24 of 24
Deshpande et al. Discover Computing          (2025) 28:230
14. Kumar A, Srinivasan K, Cheng WH, Zomaya AY. Hybrid context enriched deep learning model for fine-grained sentiment
analysis in textual and visual semiotic modality social data. Inf Process Manag. 2020;57:102141.
15. Yan X, Xue H, Jiang S, Liu Z. Multimodal sentiment analysis using multi-tensor fusion network with cross-modal modeling.
Appl Artif Intell. 2021;36(1):2000688.  h t t p s :  / / d o i  . o r g / 1  0 . 1 0  8 0 / 0 8  8 3 9 5 1  4 . 2 0 2 1  . 2 0 0  0 6 8 8.
16. Meena G, Mohbey K, Kumar K, Lokesh K. A hybrid deep learning approach for detecting sentiment polarities and knowl-
edge graph representation on Monkeypox tweets. Decis Analytics J. 2023;7:100243.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . d a j o u r . 2 0 2 3 .
1 0 0 2 4 3     .
17. Xu Y, Wei H, Lin M, Deng Y, Sheng K, Zhang M, Tang F, Dong W, Huang F, Xu C. Transformers in computational visual media:
A survey. Comput Visual Media. 2021;8(1):33–62. https://doi.org/10.1007/s41095-021-0247-3.
18. Paul S, Chen PY. Vision Transformers are robust learners. Proc AAAI Conf Artif Intell. 2022;36(2):2071–81.  h t t p s : / / d o i . o r g / 1 0 .
1 6 0 9 / a a a i . v 3 6 i 2 . 2 0 1 0 3     .
19. Xie Y, Liao Y. 2023. Efficient-ViT: a light-weight classification model based on CNN and ViT. In Proceedings of the 2023 6th
International Conference on Image and Graphics Processing, 64–70. https://doi.org/10.1145/3582649.3582676
20. Bao H, Dong L, Wei F. Beit: Bert pre-training of image transformers. 2021. ArXiv abs/ 210608254.
21. Chen CF, Fan Q, Panda R. CrossViT: cross-attention multi-scale vision transformer for image classification. Proc IEEE Int Conf
Comput Vis. 2021;347–356. https://doi.org/10.48550/arxiv.2103.14899.
22. Chen J, Zhang Y, Pan Y, et al. A transformer-based deep neural network model for SSVEP classification. Neural Netw.
2023;164:521–34. https://doi.org/10.1016/J.NEUNET.2023.04.045.
23. Gao Q, Cao B, Guan X, Gu T, Bao X, Wu J, Liu B, Cao J. Emotion recognition in conversations with emotion shift detection
based on multi-task learning. Knowl Based Syst. 2022;248:108861. https://doi.org/10.1016/j.knosys.2022.108861.
24. Tan CH, Chan A, Haldar M, Tang J, Liu X, Abdool M, Gao H, He L, Katariya S. 2023. Optimizing Airbnb search journey with
multi-task learning. In Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining,
4872–81. https://doi.org/10.1145/3580305.3599881
25. Yang B, Wu L, Zhu J, Shao B, Lin X, Liu T. Multimodal sentiment analysis with two-phase multi-task learning. IEEE/ACM
Trans Audio Speech Lang Process. 2022;30:2015–24. https://doi.org/10.1109/TASLP .2022.3178204.
26. Yu W, Xu H, Meng F, Zhu Y, Ma Y, Wu J, Zou J, Yang K. CH-SIMS: a Chinese multimodal sentiment analysis dataset with fine-
grained annotation of modality. Proc 58th Annual Meeting Association Comput Linguistics. 2020;3718–27.  h t t p s :  / / d o i  . o r g /
1  0 . 1 8  6 5 3 / v  1 / 2 0 2  0 . a c l -  m a i n  . 3 4 3.
27. Zhang S, Yin C, Yin Z. Multimodal sentiment recognition with multi-task learning. IEEE Trans Emerg Top Comput Intell.
2023;7(1):200–09. https://doi.org/10.1109/TETCI.2022.3224929.
28.  h t t p s :  / / h u g  g i n g f a  c e . c  o / d a t  a s e t s  / A l l e n  T A N /  i m a g e _ s e n t i m e n t.
29. Devlin J et al. BERT: pre-training of deep bidirectional transformers for language understanding. North American chapter
of the association for computational linguistics. 2019. https://arxiv.org/abs/1810.04805
30. Mikolov T, Chen K, Corrado Gs, Dean J. Efficient estimation of word representations in vector space. Proceedings of Work-
shop at ICLR. 2013. https://doi.org/10.48550/arXiv.1301.3781.
31. Pennington J, Socher R, Manning C. GloVe: Global Vectors for Word Representation. In Proceedings of the 2014 Confer-
ence on Empirical Methods in Natural Language Processing (EMNLP), pp 1532–1543, Doha, Qatar. Association for Compu-
tational Linguistics. 2014.
32. Sun C, Huang L, Qiu X. Utilizing BERT for Aspect-Based sentiment analysis via constructing auxiliary sentence. NAACL-HLT.
2019. https://arxiv.org/abs/1903.09588.
33.  h t t p s :  / / h u g  g i n g f a  c e . c  o / d o c  s / t r a  n s f o r m  e r s /  m o d e l _ d o c / v i t.
34. Dosovitskiy A, Beyer L, Kolesnikov A, Weissenborn D, Zhai X, Unterthiner T, Dehghani M, Minderer M, Heigold G,
Gelly S, Uszkoreit J, Houlsby N. An image is worth 16x16 words: transformers for image recognition at scale. 2020.
ArXivabs/2010.11929.
35. Priyadarshini I, Cotton C. A novel LSTM–CNN–grid search-based deep neural network for sentiment analysis. J Supercom-
put. 2021;77:13911–32. https://doi.org/10.1007/s11227-021-03838-w.
36. Mohbey K, Meena G, Kumar S, Lokesh K. A CNN-LSTM-based hybrid deep learning approach to detect sentiment polari-
ties on Monkeypox tweets. 2022. https://doi.org/10.48550/arXiv.2208.12019.
Publisher’s note
Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.
