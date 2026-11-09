---
title: A multi-task learning approach for consumer sentiment classification and emotion detection via
  behavioral data
url: https://doi.org/10.1038/s41598-026-72542-7
category: consumer-behavior
subcategory: review
date: 2026-10
venue: Scientific Reports
authors:
- Farhan Alam
- Ashraf Kamal
- Mohammad Meraj
source: openalex-oa
pdf_url: https://www.nature.com/articles/s41598-026-72542-7.pdf
pages: 16
chars: 70230
fetched_at: '2026-11-08T19:34:25+00:00'
kb_version: 1
---

# A multi-task learning approach for consumer sentiment classification and emotion detection via behavioral data

Scientific Reports |        (2026) 16:33392 1
www.nature.com/scientificreports
| https://doi.org/10.1038/s41598-026-72542-7
OPEN
1School of Management and Commerce, Dev Bhoomi Uttarakhand University, Dehradun 248007, India.
2Department of Privacy, PayPal, Chennai 600119, India. 3College of Applied Computer Science, King Saud
University, 11432 Riyadh, Saudi Arabia. 4College of Computer and Information Sciences, Imam Mohammad Ibn
Saud Islamic University (IMSIU), Riyadh, Saudi Arabia. 5Department of Mathematics, Jamia Millia Islamia, New Delhi
110025, India. 6Indira Gandhi National Open University, IOP , Regional Centre, NOIDA 201306, India. 7Directorate of
Education, New Delhi 110054, India. 8Department of Intelligent Systems, KTH Royal Institute of Technology, 10044
Stockholm, Sweden. email: dr.saqibqamar@gmail.com
A multi-task learning approach for
consumer sentiment classification
and emotion detection via
behavioral data
Farhan Alam1, Ashraf Kamal2, Mohammad Meraj3, Mohd Fazil4, Ahmad Kamal5,
Shakir Khan4, Shama Faridi6, Vineet Kumar Sejwal7, Saqib Qamar8  & Riyad Almakki4
Sentiment analysis captures overall opinion polarity, but it often fails to reveal the key emotions that
drive consumer behavior. The recognition of both sentiment and emotions provides crucial information
to uncover underlying drivers of consumers behavior and brand loyalty. These important insights
enable businesses to detect emerging issues, refine products and services, and personalize consumer
experiences. This study proposes a multi-task approach that performs sentiment classification and
emotion detection tasks based on consumer reviews and corresponding ratings. To this end, we
propose Consumer Sentiment and Emotion Modeling (COSMO-MT), a deep learning-based multi-task
model for sentiment classification and emotion detection. It begins with an input layer followed by
embedding layers that provide sentiment-specific, emotion-specific, and shared embeddings from
the input text. Each embedding is processed through shared layers consisting of CNN, BiLSTM, and
attention mechanisms. Moreover, several auxiliary features are incorporated into the shared layers to
provide explicit linguistic information. The outputs of the shared layers are then passed to task-specific
layers for sentiment classification and emotion detection. Finally, corresponding dense and output
layers generate predictions for both tasks. We evaluate the efficacy of the proposed COSMO-MT model
on two publicly available datasets. It significantly outperforms existing studies and baseline methods.
Keywords Sentiment classification, Emotion detection, Consumer reviews, Information retrieval, Deep
learning, Natural language processing
Over the last two decades, social media has evolved into one of the most efficient sources of communication.
Social networking and e-commerce platforms, such as Facebook, Twitter, Instagram, Y elp, and Amazon provide
consumers with platforms to share their experiences, opinions, and emotions about products and services. This
digital transformation has resulted in large volumes of user-generated content (UGC) 1. Recent advancements
in intelligent deep learning (DL) frameworks across diverse domains, including predictive analytics, healthcare
modelling, and hate speech detection further motivate the development of robust AI-driven approaches for
analyzing consumer-centric textual data2. Consequently, consumers tend to make purchasing decisions based
on the informative UGC, including product reviews, ratings, and features. The accessibility of this information
has led to significant changes in consumers behavior and decision-making via transparency and actionable
insights. However, this shift also presents both opportunities and challenges for businesses to manage online
reputation and leverage consumer feedback for continuous improvement3.
Sentiment classification (SC) and emotion detection (ED) are application-level natural language processing
(NLP) tasks that are intrinsically connected 4. Sentiment represents the comprehensive attitude, opinion, or
viewpoint that a person holds toward something and reflects whether an individual’s perspective is favorable,
unfavorable, or neutral. It is exhibited in daily communication through both written expressions and non-verbal

Scientific Reports |        (2026) 16:33392 2| https://doi.org/10.1038/s41598-026-72542-7
www.nature.com/scientificreports
cues5. In contrast, emotion is an integral constituent of human life. It influences decision-making and assists in
expressing views and thoughts in a precise manner. Emotion recognizes a person’s feelings, such as happiness,
sadness, anger, or fear. The varied forms of emotion represent complex states that influence human thoughts,
behavior, and personality. These emotional states provide rich and nuanced layers of feeling, that give rise to
sentiment with emotion acts as a stimulus that shapes the directional attitude expressed as positive, negative,
or neutral. Consequently, assessing individuals’ emotions and sentimental traits through their online and social
activities has attracted significant attention from the computational linguistics community6.
Considering this, the vast number of customer reviews is important for SC and ED from a business perspective.
These reviews contain authentic and unfiltered emotional responses. This can help reveal consumers’ sentiments
about brands, products, and experiences. Companies leverage millions of customer reviews to understand
customers’ delight or frustration. These sentiment and emotion insights allow businesses to make a variety of
strategic choices, including enhancements to products, improvements in customer service, the development of
marketing initiatives, crisis management, and the prediction of customer churn.
Our contributions
Admitting the aforementioned facts, a multi-task approach is introduced wherein both sentiment and emotion
are jointly modeled with the purpose to investigate consumer behavior. We devise a new DL-based multi-task
model for SC and ED, referred to as Consumer Sentiment and Emotion Modeling using Multi-Task Learning
(COSMO-MT). It consists of input, embedding, shared, task-specific, dense, and output layers. Each layer is
responsible to perform a specific function that supports both SC and ED. The process commences with an
input layer which takes the consumer review as input text and converts it into the corresponding input vector.
Sentiment-, emotion-, and language model (LM)-specific embeddings at the embedding layer receive the
input vector in parallel and generate the corresponding embedding vectors. A shared embedding is formed
by combining these three embedding outcomes. The shared layers, which operate as three parallel networks,
consist of convolutional neural networks (CNN)7 to extract low-level sentiment- and emotion-related syntactic
and semantic information, bi-directional long short-term memory 8 to capture latent contextual information,
and the attention layer is applied to capture crucial information from relevant sentiment- and emotional-related
keywords of the input text. Moreover, the outcomes of the corresponding three attention layers are fused to
provide a shared attention vector, which is concatenated with 15-dimensional hand-crafted auxiliary features
generated from four auxiliary feature groups to provide better linguistic insights to the shared networks and
to make the joint operation of the multi-task model more effective and informed. Thereafter, the shared layer
outcome as fused context vector is forwarded to the task-specific layers, wherein task-level attention is responsible
to retrieve sentiment- and emotion-specific information separately. Lastly, classification task is performed using
task-specific dense layers. The role of the output layer is to finalize the resulting class separately for SC and ED.
The key contributions of this study are highlighted below:
• We formulate a multi-task learning problem for SC and ED using online consumer reviews and correspond-
ing ratings. This enables the joint modeling of sentiment polarity and emotional states to obtain consumer
behavioral insights.
• We develop a novel DL–based multi-task model, referred to as COSMO-MT. It performs SC and ED via shared
and task-specific representation learning mechanisms.
• We incorporate a rich set of auxiliary features into the proposed model to improve linguistic representation
and upport improved SC and ED performance.
• We evaluate the proposed model on publicly available datasets and compare it with existing state-of-the-art
(SOTA) and baseline methods to validate its effectiveness.
The rest of the paper is structured as follows: ’Related works’ section presents a detailed review of the existing
studies. ’Research overview’ section presents the problem statement and data preparation steps. ’Proposed
model’ section presents a comprehensive description of our proposed model. ’Experimental setup and results’
section presents an extensive experimental evaluation and comparative analysis. Lastly, ’Conclusion and future
works’ section concludes this study and highlights key future research directions.
Related works
This section presents a comprehensive overview of the existing SOTA methods for SC and ED. It also outlines
the existing status and discusses their limitations.
Sentiment classification
This section presents the SOTA for SC. Vaish et al. 9 considered hotel reviews and applied latent dirichlet
allocation for SC. They applied numerous machine learning (ML) classifiers including naïve bayes (NB)
classifier, support vector machine (SVM), decision tree (DT), etc. Kausar et al. 10 discussed a comprehensive
overview of SC across various online domains and applied SVM. Kumar et al.11 applied multiple ML algorithms,
such as Logistic Regression (LR) and Multinomial NB to analyze Amazon product reviews based on books and
medicines. Authors reported that LR performed better for the SC task. It can be used to predict the sentiments
of future reviews. Fahim et al.12 applied techniques like word normalization to reduce text features and advanced
word embedding methods to capture contextual semantics. Sahoo et al. 13 applied DL approaches for SC. They
considered LSTM, gated recurrent unit (GRU), CNNs, and transformers. Habimana et al. 14 considered DL
techniques for various SC-related tasks. They analyzed the performance of models like CNN and recurrent
neural network (RNN) across different SC related tasks, including document-level, sentence-level, aspect-based
SC, multilingual, and multi-modal. Rasheed et al. 15 examines the underlying factors associated with negative

Scientific Reports |        (2026) 16:33392 3| https://doi.org/10.1038/s41598-026-72542-7
www.nature.com/scientificreports
sentiment through a mixed-methods approach based on expression capacity. Ashraf and Choi 16 proposed
the a sentiment transferability model to analyze negative sentiment propagation across various social media
platforms using transformer-based representations, network embeddings, and cascade dynamics modelling.
Ashraf17 analyzed and mitigated negative sentiment propagation using graph-theoretic analysis, psychological
modeling, and influencer-driven cascade monitoring across social media platforms. proposed SentiNet, a
hybrid deep learning architecture integrating BiLSTM, CNN, and attention mechanisms to improve sentiment
classification performance across noisy and domain-specific social media datasets. Madhurika and Malleswari18
proposed SentiNet, a hybrid deep learning architecture integrating BiLSTM, CNN, and attention mechanisms
to improve sentiment classification performance across noisy and domain-specific social media datasets. Park
et al.19 proposed a data-driven customer segmentation framework that combines neural network–based feature
importance estimation with network construction techniques to improve customer-oriented analysis of sentiment
and market segmentation. These studies demonstrate the growing adoption of hybrid DL, transformer-based
architectures, and graph-driven analytical frameworks for improving sentiment understanding, propagation
analysis, and customer-centric opinion mining across diverse online platforms.
Emotion detection
This section presents the existing SOTA methods for ED. Siam et al. 20 applied SVM, NB, and LR classifiers.
They adopted an angular encoding algorithm that generated ten discriminative features for ED. Pereira et al. 21
explored Emotion Recognition in Conversations (ERC) and observed that most ERC models predominantly
rely on Transformer architectures, gated networks, and graph neural networks. Bharti et al.22 presented a hybrid
model that integrated ML and DL methods for ED in textual data. They considered CNN and BiGRU, and
SVM models and evaluated them on three datasets. They considered various text formats, such as sentences,
tweets, dialogues, keywords, and emotion-specific lexicons. Adamu et al.23 proposed a hybrid stacked ensemble
framework integrating multiple transformer-based models and a random forest-based meta-classifier to
improve multi-label emotion classification across high-resource and low-resource multilingual datasets.
Khan et al.24 proposed a hybrid architecture integrating RoBERTa and LSTM networks to improve contextual
emotion detection by capturing sequential and deep contextual emotional representations from text. Nguyen
et al. 25 applied ensemble learning–based multi-label classification models to analyze customer emotions in
hotel reviews, demonstrating improved performance for emotion-aware customer feedback analysis and
eWOM understanding. Prova 26 proposed a T5-CapsNet meta-ensemble framework integrating transformer-
based contextual embeddings, capsule networks, and GAN-based data augmentation to improve multilingual
sentiment and emotion classification in e-commerce reviews. These studies highlight the growing use of
transformer-based architectures, ensemble learning, and hybrid DL frameworks for improving contextual and
multilingual emotion understanding across diverse textual domains.
Status and limitations
It can be observed that existing studies demonstrate strong performance in SC and ED, but they are mostly
treated as independent tasks. Furthermore, task interference and label dependency are rarely analyzed, which
restricts the understanding of cross-task knowledge transfer. As a result, the potential benefits of unified multi-
task models for improved generalization and consistency across related affective tasks are underexplored. Hence,
our proposed model represents a significant and worthwhile research contribution to consumer behavior
understanding through SC and ED.
Research overview
This section presents the problem statement and data preparation steps for the proposed approach.
Problem statement
Let 𝒟𝒟𝒟 {(𝑥𝑥𝑖𝑖,𝑦𝑦 𝑠𝑠𝑠𝑠 𝑖𝑖 ,𝑦𝑦 𝑒𝑒𝑒𝑒 𝑖𝑖 )}𝑁𝑁 𝑖𝑖𝑖𝑖 denote a dataset of N consumer reviews and ratings collected from multiple online
platforms, where 𝑥𝑥𝑖𝑖 represents the 𝑖𝑖𝑡𝑡𝑡 input text. Each review is associated with two task-specific labels: 𝑦𝑦𝑠𝑠𝑠𝑠 𝑖𝑖  for
SC and 𝑦𝑦𝑒𝑒𝑒𝑒 𝑖𝑖  for ED. The SC label belongs to the sentiment label space 𝒴𝒴𝑠𝑠𝑠𝑠 = {positive, neutral, andnegative}
, whereas the ED label refers to the emotion label space 𝒴𝒴𝑒𝑒𝑒𝑒 = {anger, fear, sadness, joy, surprise, anddisgust}.
In this study, the objective is to learn a multi-task model that jointly predicts 𝑦𝑦𝑠𝑠𝑠𝑠 𝑖𝑖  and 𝑦𝑦𝑒𝑒𝑒𝑒 𝑖𝑖  for each input
review 𝑥𝑥𝑖𝑖. Thus, SC is formulated as a three-class classification task for identifying sentiment polarity, while ED
is formulated as a six-class classification task for identifying the dominant emotion expressed in the review. This
joint formulation enables the proposed framework to integrate sentiment polarity with underlying emotional
states conveyed by consumers.
Although SC and ED are closely related tasks, they operate at different semantic granularities. SC identifies
the overall polarity of a review as positive, neutral, or negative, whereas ED captures fine-grained emotional states
such as anger, fear, sadness, joy, surprise, and disgust. Multiple emotions may exist within the same sentiment
polarity. For example, both anger and sadness correspond to negative sentiment while convey different affective
meanings. Therefore, SC and ED are formulated as two related yet distinct tasks within a multi-task learning
framework. The proposed framework employs shared representations to capture common semantic and
contextual information across both tasks, while task-specific layers learn discriminative representations specific
to SC and ED individually. This shared–private learning mechanism enables knowledge transfer between related
tasks and improves contextual representation learning.
Data preparation
This section presents the data collection and pre-processing steps.

Scientific Reports |        (2026) 16:33392 4| https://doi.org/10.1038/s41598-026-72542-7
www.nature.com/scientificreports
Dataset collection: In this study, we collect and prepare two publicly available two datasets. A brief description
of the two datasets is given below:
• Amazon product review—2023  (Dataset-1)1: This dataset consists of 571.54M Amazon product reviews. It
contains several entities, such as rating, title, text, images, asin, parent_asin, user_id, timestamp, helpful_vote,
and verified_purchase. We consider 100,000 randomly selected reviews from this dataset using only the review
text and rating entities.
• Women’s clothing e-Commerce dataset (Dataset-2)2: This dataset is taken from Kaggle. It consists of 23,486
consumer reviews along with clothing ID, age, title, review text, rating, recommended IND, positive feedback
count, division name, department name, and class name. We consider only the review text and rating entities.
In both datasets, the ratings of each review range from 1 to 5, and each consumer review is labeled as positive (1),
negative (0), or neutral (2). Reviews with rating scores of 4 or 5 are labeled as positive, ratings of 1 or 2 as negative,
and ratings of 3 as neutral. The final statistics of the datasets are presented in Table 1.
We further annotate each review with one of six core emotions and consider six core emotions, namely anger,
fear, sadness, joy, surprise, and disgust, based on the NRC EmoLex3 resource. The rating-derived sentiment labels
are used only as an initial sentiment-level guidance mechanism, whereas the final emotion labels are assigned
using a lexicon-based contextual annotation strategy. Specifically, explicit emotion-bearing terms extracted from
the NRC EmoLex resource, contextual semantic dependencies within the review text, co-occurrence patterns of
affective expressions, and the dominant affective intent conveyed by the overall context are jointly considered to
determine the most representative emotion category for each review.
Labeling technique Positive sentiment reviews are generally associated with emotions, such as joy and surprise,
whereas negative sentiment reviews are commonly associated with emotions, such as anger, sadness, fear, and
disgust. Neutral reviews are generally associated with relatively low-intensity affective states. If multiple emotions
appear within the same review, the dominant emotion that represents the primary affective intent is selected as
the final label. For the exemplar review, “I was disappointed when the package arrived damaged, but what really
made me angry was the seller refusing to help” , the text expresses multiple emotions, including sadness and anger.
However, the final emotion label is assigned as anger because the dominant contextual and affective intensity of
the review is primarily dominated by anger.
Although the proposed labeling strategy incorporates contextual and affective cues, certain limitations
remain due to possible ambiguity in emotional expressions and dependence on the coverage of the lexicon.
Reviews containing subtle or overlapping emotions may still introduce annotation uncertainty in some cases.
Pre-processing We perform several pre-processing steps on the above two finalized datasets. These steps
thoroughly clean and normalize the collected data into lower-case form. Moreover, punctuation, exclamation
marks, stop words, special characters, unnecessary white-spaces, digits, and non-ASCII characters are eliminated
during the pre-processing steps. Consequently, the pre-processing steps produce a cleaned and normalized
dataset for further processing by the input layer of the new multi-task COSMO-MT model.
1 https://amazon-reviews-2023.github.io/ [Accessed: 12-Aug-2026]
2 https://www. kaggle.com/d atasets/nica potato/wome ns-ecommerce-clothing-reviews [Accessed: 12-Aug-2026]
3 https:   //saifmohamm ad. com/WebP age s/NRC-E mot ion- Lexicon.htm [Accessed: 12-Aug-2026]
Tasks Class Dataset-1 Dataset-2
SC
Positive 35,000 18,206
Neutral 32,000 2,872
Negative 33,000 2,408
#instances 100,000 23,486
ED
Joy 35,000 18,206
Surprise 32,000 2,872
Anger 9,250 625
Fear 7,813 548
Sadness 9,892 996
Disgust 6,045 239
#instances 100,000 23,486
Training set (70%) 70,000 16,440
Validation set
(15%) 15,000 3,523
Test set (15%) 15,000 3,523
Table 1. Final statistics of both datasets for SC (3-class) and ED (6-class) tasks for dataset-1 (Amazon product
review—2023) and dataset-2 (Women’s clothing e-Commerce).

Scientific Reports |        (2026) 16:33392 5| https://doi.org/10.1038/s41598-026-72542-7
www.nature.com/scientificreports
Proposed model
This section presents a detailed discussion of our proposed COSMO-MT model. Figure 1 depicts the end-to-end
architecture of the proposed model. A brief description of each layer is provided in the following sub-sections:
Input layer
The input layer performs tokenization and numerical encoding of the input review text to generate a fixed-length
representation suitable for embedding and downstream neural processing. It takes the pre-processed consumer
review text i as input, which consists of 𝑟𝑟𝑖𝑖 words. The input text is tokenized in the this layer, and each token
is mapped to a dictionary index. The resulting token sequence is converted into a numerical vector n. A fixed
length l is then defined, and n is padded to obtain a vector v of length l, such that |𝑣𝑣| 𝑣 𝑣𝑣 ≥ |𝑛𝑛|. The padded vector
𝑣𝑣 ∈ ℝ1×𝑝𝑝 is passed to the three corresponding embedding layers.
Embedding layers
Text embedding represents words or tokens in the form of dense numerical vectors. It learns in a low-dimensional
continuous space and is able to capture semantic and contextual relationships. In this study, we consider three
embeddings, including sentiment-specific word embeddings (SSWE) 27, Emo2Vec28, and LM. Firstly, SSWE is
used to encode sentiment information directly into word vectors. Emo2Vec, an emotion-aware embedding,
learns dense word vectors to encode emotional semantics. We use 100-dimensional word embeddings for both
content-based semantic embeddings. Finally, BERT 29, a well-known multi-layered bidirectional transformer
encoder, is employed as a language model (LM) embedding. It generates contextualized representations
adapted to sentiment- and emotion-related linguistic contexts in both directions of the input review text via
a 768-dimensional word vector representation. Three embedding vectors are generated and combined to form
a shared embedding representation. The shared embedding captures semantic information enriched with
sentiment and emotion along with contextual knowledge from BERT. Finally, the learned embedding vectors
from SSWE, shared representation, and Emo2Vec are forwarded to their corresponding networks within the
shared embedding layer.
Shared layer
The shared layer consists of CNN, BiLSTM, and attention layers. It is designed to learn shared semantic and
contextual representations that can be jointly utilized by both sentiment classification and emotion detection
tasks. It operates as three parallel networks, and each receives the corresponding embedding vectors from SSWE,
the shared embedding, and Emo2Vec. This parallel integration enables the learning of hierarchical and context-
aware shared sentiment and emotion representations of the input review text. Furthermore, it incorporates
hand-crafted auxiliary features to improve the overall model performance. A brief discussion of the shared layer
is given below:
CNN
In the shared layer, CNN is employed to extract shared sentiment and emotion features from textual input. It
captures local n-gram features (e.g., ’very good’ , ’not happy’), extracts common syntactic and semantic features,
and contributes to identifying emotional intensity and sentiment polarity. In the proposed model, we apply a
one-dimensional convolutional layer with 256 filters and a kernel (window) size of 5 to the input sequence. Each
filter performs a convolutional operation to extract local features from the sequence. The max-pooling layer
selects the maximum value within each feature map, captures the most salient features, and retains important
sentiment- and emotion-related information. Consequently, CNN produces a set of feature sequences for each
filter to capture relevant patterns across various regions of the input review text. Equation 1 shows the extraction
of the 𝑖𝑖𝑡𝑡𝑡 feature sequence, 𝑓𝑓𝑖𝑖 from the convolution operation, where x denotes the input feature vector, 𝑟𝑟𝑟⋅)
represents the ReLU activation function, w refers to the weight, and b denotes the bias.
Fig. 1. Architecture of the proposed COSMO-MT model. (Source Author’s own illustration).

Scientific Reports |        (2026) 16:33392 6| https://doi.org/10.1038/s41598-026-72542-7
www.nature.com/scientificreports
 𝑓𝑓𝑖𝑖 = 𝑟𝑟𝑟𝑟𝑟 ⋅ 𝑥𝑥 𝑥 𝑥𝑥𝑥 (1)
BiLSTM
BiLSTM is a well-known variant of RNN that can capture long-term dependencies in both directions of the
input text. In the proposed model, it provides sentiment- and emotion-related contextual information through
temporal dependency modelling and generates contextual semantic feature sequences. It produces forward
and backward contextual representations of the input text. The two hidden states, ⃗ℎ𝑓𝑓  and ⃖ℎ𝑏𝑏, are generated
from the forward and backward directions of the BiLSTM, respectively. Equation  2 presents the fused hidden
representation generated by combining the forward and backward contextual representations.
 𝑓𝑓𝑙𝑙 =[ ⃖ℎ𝑏𝑏, ⃗ℎ𝑓𝑓 ] (2)
Attention network
The attention mechanism empowers the model to focus on the relevant parts of the input data30. In the proposed
model, it identifies sentiment- and emotion-relevant features using a word-level attention mechanism. It
receives the fused hidden representation vectors 𝑓𝑓𝑙𝑙 as input and emphasizes important sentiment- and emotion-
related tokens. Equation  3 presents the hidden representation, 𝑢𝑢𝑡𝑡. It is calculated by applying the non-linear
activation function tanh to the linear transformation of the hidden representation vectors, 𝑓𝑓𝑙𝑙, where the hidden
representation vector, 𝑓𝑓𝑙𝑙 is multiplied by a learnable weight matrix, 𝑊𝑊𝑤𝑤 and added to a bias vector, 𝑏𝑏𝑤𝑤.
 𝑢𝑢𝑡𝑡 = tanh(𝑊𝑊𝑤𝑤𝑓𝑓𝑙𝑙 +𝑏𝑏 𝑤𝑤) (3)

𝛼𝛼𝑡𝑡 = exp(𝑢𝑢𝑡𝑡) ∑𝑡𝑡(exp(𝑢𝑢𝑡𝑡))  (4)
where 𝛼𝛼𝑡𝑡 denotes the normalized attention weight corresponding to the hidden representation 𝑢𝑢𝑡𝑡.
Equation 5 computes the attention vector 𝑎𝑎𝑖𝑖 as a weighted combination of the contextual representations 𝑓𝑓𝑙𝑙
. The attention weights 𝛼𝛼𝑡𝑡 determine the relative importance of each contextual representation. It enables the
model to focus on sentiment- and emotion-relevant information from the input text.

𝑎𝑎𝑖𝑖 =
𝑡𝑡
∑
𝑖𝑖𝑖𝑖
𝛼𝛼𝑡𝑡𝑓𝑓𝑙𝑙 (5)
Shared attention layer It receives the outputs of the three corresponding attention layers and integrates them into
a unified shared representation. As a result, it generates the shared attention vector, 𝑠𝑠𝑖𝑖, which captures high-level
shared contextual information related to sentiment and emotion present in the input text.
Auxiliary features
In this study, we consider four auxiliary feature groups (sentiment, affective, psycholinguistics, and syntactic).
The inclusion of these feature groups enriches the proposed model with complementary information, enhances
feature diversity, improves representation robustness, and improves generalization across multi-task learning. A
brief description of each feature group is given below in the following sub-sections:
• Sentiment features Sentiment is a key indicator to analyze consumer behavior and can be explicitly observed
from the review text and ratings. We extract four sentiment-oriented independent features from each input
text: (i) polarity, (ii) subjectivity, (iii) frequency of positive words, and (iv) frequency of negative words. These
features are extracted using TextBlob, a well-known Python library for information retrieval tasks. 4. The
extracted scores are normalized by dividing the aggregated word-level scores by the total sum of the cor -
responding scores across all words in the input text. Equation  6 presents the normalized sentiment feature
score, where 𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠 𝑖𝑖) denotes the sentiment score of the 𝑖𝑖𝑡𝑡𝑡 word in the input text.

𝑠𝑠𝑓𝑓 =
∑
𝑛𝑛
𝑖𝑖𝑖𝑖 𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠 𝑖𝑖𝑖
∑
𝑛𝑛
𝑖𝑖𝑖𝑖 |𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠 𝑖𝑖)|
 (6)
• Affective features Affective content in review texts reflects the underlying emotional states of consumers. We
extract three affective independent features from each input text: (i) valence score (i.e., measures the pleas -
antness of emotions expressed in the text), (ii) arousal score (i.e., captures the level of emotional activation
through words), and (iii) dominance score (i.e., reflects the degree of control or power expressed in the text).
These features are computed using the ANEW lexicon31. The extracted scores are normalized using the sum
of the scores of each word in the input text. Equation 7 presents the normalized affective feature score, where
𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎 𝑖𝑖) represents the valence, arousal, or dominance score of the 𝑖𝑖𝑡𝑡𝑡 word.
4 https://textblob.readthedocs.io/en/dev/[Accessed: 12-Aug-2026]

Scientific Reports |        (2026) 16:33392 7| https://doi.org/10.1038/s41598-026-72542-7
www.nature.com/scientificreports

𝑎𝑎𝑓𝑓 = 1 𝑛𝑛
𝑛𝑛
∑
𝑖𝑖𝑖𝑖
𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎 𝑖𝑖) (7)
• Psycholinguistic features Psychological cues are important indicators to analyze consumer behavior in terms
of sentiment and emotion. We consider four independent psycholinguistic features: (i) linguistic (which
captures structural aspects of review language, such as grammar, syntax, and vocabulary), (ii) psychological
(which reflects cognitive and emotional processes through affective and perceptual word usage), (iii) personal
(which captures references to self-related experiences, concerns, and personal expressions), and (iv) spoken
(which measures conversational characteristics, such as informal expressions, fillers, and dialogue markers).
These features are computed using the popular LIWC lexicon5. The feature values are represented as normal-
ized frequencies based on the total number of words in the input text. Equation 8 presents the psycholinguis-
tic feature score, where count(c) denotes the number of words belonging to category c in the input text.
 𝑝𝑝𝑓𝑓 = 𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐 𝑐𝑐  (8)
• Syntactic features These features capture affective intensity patterns in the input text. In this study, we extract
four independent syntactic features from the input text: (i) frequency of verbs, (ii) frequency of nouns, (iii)
frequency of adverbs, and (iv) frequency of adjectives. These features are computed using PennTreebank6. If
the frequency of POS tags is at least 3 in the input text, then a score of 1 is assigned; otherwise, 0. Equation 9
presents the syntactic feature score, where freq(pos) denotes the frequency of a POS tag in the input text.

𝑠𝑠𝑠𝑠𝑠𝑠𝑓𝑓 = { 1, if 𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑠𝑠𝑓 ≥ 3 0, otherwise  (9)
Finally, a total of 15 independent features are extracted from four feature groups. As a result, it generates a
15-dimensional feature vector, 𝑎𝑎𝑣𝑣, as given in eq. 10, where 𝑠𝑠𝑓𝑓 , 𝑎𝑎𝑓𝑓 , 𝑝𝑝𝑓𝑓 , and 𝑠𝑠𝑠𝑠𝑠𝑠𝑓𝑓  represent sentiment, affective,
psycholinguistic, and syntactic feature vectors, respectively, and ⊕ denotes the concatenation operation.
 𝑎𝑎𝑣𝑣 =𝑠𝑠 𝑓𝑓 +𝑎𝑎 𝑓𝑓 +𝑝𝑝 𝑓𝑓 + 𝑠𝑠𝑠𝑠𝑠𝑠𝑓𝑓  (10)
.
Fused context vector It combines the shared attention vector, 𝑠𝑠𝑖𝑖, with the auxiliary feature vector, 𝑎𝑎𝑣𝑣, generated
from the auxiliary feature groups. Before fusion, 𝑎𝑎𝑣𝑣 is projected into the same dimensional space as 𝑠𝑠𝑖𝑖 to ensure
dimensional compatibility. This fusion enhances the learned representation and leverages contextual and
linguistic information. As a result, it gives the fused context vector, 𝑓𝑓𝑣𝑣, as given in eq. 11, where 𝑤𝑤𝑝𝑝 denotes the
projection matrix used to map 𝑎𝑎𝑣𝑣 into the same dimensional space as 𝑠𝑠𝑖𝑖.
 𝑓𝑓𝑣𝑣 =𝑠𝑠 𝑖𝑖 +𝑤𝑤 𝑝𝑝 𝑎𝑎𝑣𝑣 (11)
Task-specific layers
The main purpose of the task-specific layers is to provide high-level task-specific features relevant to sentiment
and emotion analysis. The task-specific layers are designed to learn discriminative representations specific to
sentiment classification and emotion detection individually. They operate in parallel for both tasks. Each task-
specific branch consists of a task-level attention followed by dense and output layers. Each task-specific branch
receives the fused context vector, 𝑓𝑓𝑣𝑣, as input for the two parallel tasks. A brief description of these layers is
provided below:
Task-level attention layer
The role of the two high-level task-specific attention layers is to capture more fine-grained contextual information
for each task (i.e., sentiment and emotion). These attention layers enable the model to selectively focus on
task-relevant contextual patterns for SC and ED independently. Two task-specific attention layers receive the
outcomes of the shared layer in the form of the fused context vector, 𝑓𝑓𝑣𝑣, in parallel and produce two high-level
context vectors, 𝑡𝑡𝑠𝑠 and 𝑡𝑡𝑒𝑒, corresponding to the sentiment and emotion detection tasks, respectively.
Dense and output layers
Two fully connected dense layers are employed in parallel to generate sentiment- and emotion-specific feature
representations from the two high-level context vectors, 𝑡𝑡𝑠𝑠 and 𝑡𝑡𝑒𝑒, respectively. The dense layers transform the
high-level contextual representations into task-specific feature spaces for final classification. The sentiment and
emotion output layers correspond to three and six classes, respectively. Finally, a softmax activation function is
applied at the output of each task-specific layer and a sparse categorical cross-entropy loss is used independently
for sentiment classification (SC) and emotion detection (ED).
5 https://tinyurl.com/mxsz895x [Accessed: 12-Aug-2026]
6 https://tinyurl.com/2jx5f657 [Accessed: 12-Aug-2026]

Scientific Reports |        (2026) 16:33392 8| https://doi.org/10.1038/s41598-026-72542-7
www.nature.com/scientificreports
Experimental setup and results
This section presents the empirical evaluation of the proposed model. It covers datasets, metrics, results and
comparative analysis, ablation study, several analyses, findings and limitations, and lastly a discussion.
Datasets
In this section, we present the statistics of the two datasets in terms of class distributions for SC and ED tasks.
Since, our proposed COSMO-MT framework jointly models SC and ED tasks, we assign three sentiment classes
(positive, neutral, and negative) and six emotion classes ( joy, anger, sadness, fear, disgust, and surprise) for each
input review. Table 1 presents the final statistics and data partitioning details of both datasets for SC and ED
tasks, including the training, validation, and test splits in the ratio of 70:15:15. Dataset-1 corresponds to the
Amazon Product Review-2023 dataset, whereas Dataset-2 corresponds to the Women’s Clothing E-Commerce
Review dataset. The sentiment labels indicate class imbalance in Dataset-2, while emotion labels in both datasets
also exhibit imbalance. In Table 1, #instances in bold typeface represents the total number of samples including
all classes in each dataset. Therefore, we employ a class-weighted sparse categorical cross-entropy loss during
training. Higher weights are assigned to minority classes to mitigate majority class bias.
Evaluation metrics
In this study, SC and ED are evaluated using four metrics – Precision, Recall, F-score, and Accuracy, as defined in
Eqs. 12 to 15. These metrics are defined using the following four key terms:
• True positive (TP): Total number of consumer review instances where the model correctly predicts the actual
sentiment or emotion label.
• False positive (FP): Total number of consumer review instances where the model predicts a sentiment or emo-
tion label that is not present in the ground truth.
• False negative (FN): Total number of consumer review instances where the model fails to predict the actual
sentiment or emotion label present in the text.
• True negative (TN): Total number of consumer review instances correctly identified as not belonging to a
particular sentiment or emotion class.
 𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃 𝑃 𝑇𝑇𝑃𝑃 𝑇𝑇𝑃𝑃 𝑇 𝑇𝑇𝑃𝑃  (12)
 𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅 𝑅 𝑇𝑇𝑇𝑇 𝑇𝑇𝑇𝑇 𝑇 𝑇𝑇𝑇𝑇  (13)
 𝐹𝐹 𝐹 𝐹𝐹𝐹𝐹𝐹𝐹𝐹𝐹𝐹𝐹𝐹𝐹𝐹𝐹𝐹𝐹𝐹𝐹𝐹𝐹𝐹𝐹𝐹 𝐹 2×𝑃𝑃 ×𝑃𝑃 𝑃𝑃𝑃𝑃𝑃  (14)
 𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴 𝐴 𝑇𝑇𝑇𝑇 𝑇 𝑇𝑇𝑇𝑇 𝑇𝑇 𝑇𝑇𝑇𝑇𝑇 𝑇𝑇𝑇𝑇𝑇 𝑇𝑇𝑇𝑇𝑇 𝑇𝑇  (15)
Parameter settings
This section presents the details of the experimental and model parameter settings, as given in Table  2. We
use the Adam optimizer, softmax activation function, and sparse categorical cross-entropy loss function. All
experiments are conducted with an Intel Core i7 processor and 128 GB RAM. The proposed COSMO-MT model
is trained using the Adam optimizer with a batch size of 64 for 30 epochs on both datasets. The complete training
and testing process require approximately 4.1 hours for Dataset-1 and 1.2 hours for Dataset-2. Although, GPU
acceleration can further reduce computational time, all experiments are conducted using the available CPU-
based computing environment. The obtained execution times demonstrate that the proposed COSMO-MT model
remains computationally feasible under commonly accessible hardware resources. Future work will investigate
GPU-accelerated implementations to further improve training efficiency and scalability for larger datasets.
Compared methods
We compare our proposed model with three SOTA methods and six baseline methods. A brief description of
these methods is provided below:
Experimental settings Model parameter settings
Environment Configuration Parameters Value
Operating system Windows 11 SSWE (Embedding) 100
Machine Intel i-3 CPU Emo2Vec (Embedding) 100
Memory 64 GB BERT (Embedding) 786
Language Python 3.7 CNN filters 256
Library Keras 2.2.4 BiLSTM (#neurons) 128
Epoch 30 Batch size 64
Table 2. Experimental configuration and model parameter settings.

Scientific Reports |        (2026) 16:33392 9| https://doi.org/10.1038/s41598-026-72542-7
www.nature.com/scientificreports
State-of-the-art methods
We consider three existing SOTA methods related to consumer-centric SC and ED.
• Rana et al.3: This method considers a combined approach of NLP and DL. They consider BERT and BiGRU
for feature extraction and graph neural network for analyzing sentiment classification.
• Xu et al.32: This method consists of BiLSTM and syntax-aware attention network for aspect-based sentiment
analysis.
• Sandiwarno et al. 6: This method recognized sentiment and emotion to analyze consumer satisfaction via
CNN and BiLSTM models.
Baseline methods
We consider the following baseline models to compare with our proposed model.
• DeBERTa-v3-base: It is a Transformer-based language model. It includes disentangled attention and relative
positional encoding.
• RoBERTa + Attention: It is a combination of RoBERTa and attention network.
• RoBERTa: It is an improved version of BERT that uses more data and larger batch sizes to provide better
performance.
• SentiBERT: It is a BERT variant specialized for sentiment understanding.
• BERT + Attention: It is a combination of BERT and attention network.
• DistilBERT : It is a smaller and faster version of BERT.
Results and comparative analysis
This section presents the analysis of the results of the proposed model. It also highlights a detailed comparative
analysis with SOTA and six baseline methods. Table 3 presents the performance evaluation results of the proposed
model and comparison with SOTA and baseline methods on SC and ED tasks on both datasets. Observe that,
our COSMO-MT model shows remarkable performance on both SC and ED tasks on both datasets across all
evaluation metrics. Observe that, the high F1-score indicates that our COSMO-MT model achieves accurate
positive predictions (high precision) and effectively identifies relevant instances (high recall). This demonstrates
that our COSMO-MT model is capable to minimize both false positives and false negatives, which ensures reliable
and stable classification performance on both tasks.
Our COSMO-MT model reports F1-score and accuracy of 0.93 and 0.94, respectively for the SC task, whereas
it achieves F1-score and accuracy of 0.92 and 0.91, respectively for ED task on dataset-1. Likewise, our COSMO-
MT model receives F1-score and accuracy of 0.92 and 0.93, respectively for SC task, whereas it obtains F1-
score and accuracy of 0.93 and 0.91 for ED task on dataset-2. These results demonstrate the robustness and
generalization capability of the proposed multi-task architecture on both balanced and relatively imbalanced
Datasets Methods/Models
Sentiment classification
(SC) Emotion detection (ED)
Pre Rec F1 Acc Pre Rec F1 Acc
Dataset-1
Ours 0.95 0.92 0.93 0.94 0.91 0.94 0.92 0.91
Rana et al.3 0.90 0.85 0.87 0.92 0.77 0.70 0.73 0.81
Xu et al.32 0.89 0.84 0.86 0.91 0.75 0.69 0.72 0.79
Sandiwarno et al.6 0.88 0.83 0.85 0.90 0.74 0.68 0.71 0.78
DeBERTa-v3-base 0.87 0.82 0.84 0.89 0.73 0.67 0.70 0.77
RoBERTa + Attention 0.86 0.81 0.83 0.88 0.71 0.65 0.68 0.75
RoBERTa 0.85 0.80 0.82 0.87 0.69 0.63 0.66 0.74
SentiBERT 0.84 0.79 0.81 0.86 0.67 0.61 0.64 0.72
BERT + Attention 0.83 0.78 0.80 0.85 0.65 0.59 0.62 0.71
DistilBERT 0.82 0.77 0.79 0.84 0.63 0.57 0.60 0.69
Dataset-2
Ours 0.90 0.95 0.92 0.93 0.92 0.94 0.93 0.91
Rana et al.3 0.88 0.82 0.85 0.89 0.71 0.64 0.67 0.77
Xu et al.32 0.87 0.81 0.84 0.88 0.70 0.63 0.66 0.76
Sandiwarno et al.6 0.86 0.80 0.83 0.87 0.69 0.62 0.65 0.75
DeBERTa-v3-base 0.85 0.79 0.82 0.86 0.67 0.60 0.63 0.73
RoBERTa + attention 0.84 0.78 0.81 0.85 0.65 0.58 0.61 0.72
RoBERTa 0.83 0.77 0.80 0.84 0.64 0.57 0.60 0.71
SentiBERT 0.82 0.76 0.79 0.83 0.62 0.55 0.58 0.69
BERT + Attention 0.81 0.75 0.78 0.82 0.60 0.53 0.56 0.68
DistilBERT 0.80 0.74 0.77 0.81 0.58 0.51 0.54 0.66
Table 3. Performance evaluation results of the proposed COSMO-MT model and comparison with SOTA and
baseline methods on SC and ED tasks on both datasets. Best results are shown in bold.

Scientific Reports |        (2026) 16:33392 10| https://doi.org/10.1038/s41598-026-72542-7
www.nature.com/scientificreports
datasets. The consistent performance across both datasets further indicates the robustness and generalization
capability of the proposed COSMO-MT model under varying data distributions.
Comparison with SOTA methods We compare our COSMO-MT model with three relevant and recent SOTA
methods. Observe that from table 3, our COSMO-MT model outperforms SOTA methods across evaluation
metrics on both datasets for SC and ED tasks. Rana et al.3 performs better across SOTA on both datasets for SC
and ED tasks. Our COSMO-MT model performs 6% and 2% better than SOTA methods in terms of F1-score
and accuracy, respectively for SC task and 19% and 10% better than SOTA methods in terms of F1-score and
accuracy, respectively for ED task on dataset-1. Likewise, our COSMO-MT model performs 7% and 4% better
than SOTA methods in terms of F1-score and accuracy, respectively for SC task and 26% and 14% better than
SOTA methods in terms of F1-score and accuracy, respectively for ED task on dataset-2. These percentage gains
observed across both tasks and datasets demonstrate the significant performance of our COSMO-MT model and
show better sentiment classification reliability with fine-grained emotional discrimination as compared to the
SOTA methods on different datasets.
Comparison with baseline models We compare our COSMO-MT model with six baseline methods. Observe
that from the results in table 3 that our COSMO-MT model outperforms baseline models across evaluation
metrics on both datasets for SC and ED tasks. DeBERTa-v3-base reports the best performance across baseline
models on both datasets for both tasks. Our COSMO-MT model outperforms the DeBERTa-v3-base model,
achieves improvements of approximately 10.7% and 5.6% in terms of F1-score and accuracy, respectively for SC
task and 31.4% and 18.2% in terms of F1-score and accuracy, respectively for ED task on dataset-1. Similarly, our
COSMO-MT model outperforms DeBERTa-v3-base model with significant percentage gain of 12.2% and 8.1% in
terms of F1-score and accuracy, respectively for SC task and 47.6% and 24.7% in terms of F1-score and accuracy,
respectively for ED task. These results validate the effectiveness of our COSMO-MT model. One possible reason
is that baseline models primarily lack task-specific joint operation mechanisms, such as SC and ED, which limits
their ability to capture subtle affective distinctions effectively as compared to our COSMO-MT model.
The improved performance of the proposed COSMO-MT model is mainly attributed to its shared–private
multi-task architecture, which jointly learns sentiment and emotion representations while preserving task-
specific contextual information. The integration of contextual embeddings, attention mechanisms, and auxiliary
linguistic features enables the model to capture both coarse-grained sentiment polarity and fine-grained
emotional nuances more effectively. Furthermore, the shared representation learning mechanism improves
feature generalization and reduces redundancy across SC and ED tasks.
Ablation study
This section presents the ablation study of our proposed COSMO-MT model. Table 4 presents ablation study of
our proposed model on both datasets for SC and ED tasks. Observe that, these results demonstrate that each
component of our COSMO-MT model contributes significantly to the overall performance. It can be seen that
removal of individual modules can degrade the performance of the proposed model across both SC and ED tasks
on both datasets.
The performance of the proposed model declines without the shared-layer attention mechanism. It highlights
the importance of shared contextual interaction for effective cross-task representation learning. Likewise, the
exclusion of the task-specific attention layer and BiLSTM indicates the importance of contextual refinement
and sequential dependency. Exclusion of CNN highlights the importance of local feature extraction which helps
capture semantic and emotional cues. The performance of the COSMO-MT model declines without auxiliary
features, which highlights the importance of explicit linguistic contribution. Further, independent ablation
analysis of auxiliary feature categories reveals that sentiment and emotion features contribute significantly to
polarity and affective understanding in SC and ED tasks. The results also indicate that psycholinguistic and
syntactic features improve contextual and linguistic representation learning. These observations indicate that
each auxiliary feature category provides complementary information, thereby improve the overall performance
of the proposed COSMO-MT model.
Model Variant
Dataset-1 Dataset-2
SC ED SC ED
F1 Acc F1 Acc F1 Acc F1 Acc
ProposedCOSMO-MT model 0.93 0.94 0.92 0.91 0.92 0.93 0.93 0.91
w/o CNN 0.85 0.86 0.83 0.82 0.84 0.85 0.84 0.82
w/o BiLSTM 0.84 0.85 0.82 0.81 0.83 0.84 0.82 0.80
w/o (attention) task-specific 0.83 0.84 0.81 0.80 0.82 0.83 0.81 0.79
w/o (attention) shared-layer 0.82 0.83 0.80 0.79 0.81 0.82 0.79 0.78
w/o auxiliary features 0.86 0.87 0.84 0.83 0.85 0.86 0.84 0.82
w/o sentiment features (auxiliary) 0.84 0.82 0.80 0.82 0.86 0.81 0.87 0.83
w/o affective features (auxiliary) 0.78 0.85 0.88 0.84 0.87 0.84 0.85 0.88
w/o psycholinguistics features (auxiliary) 0.80 0.79 0.84 0.86 0.83 0.85 0.81 0.85
w/o syntactic features (auxiliary) 0.87 0.84 0.81 0.83 0.76 0.84 0.80 0.81
Table 4. Ablation study of our proposed model on both datasets for sentiment classification (SC) and emotion
detection (ED) tasks. Best results are shown in bold.

Scientific Reports |        (2026) 16:33392 11| https://doi.org/10.1038/s41598-026-72542-7
www.nature.com/scientificreports
Qualitative and error analysis
This section presents the qualitative and error analysis of our proposed COSMO-MT model. Table  5 presents
sample review instances of classification results for SC and ED tasks taken from the datasets, as given in table
1. The first two examples show that our proposed model accurately identifies overall sentiment polarity and
corresponding emotion. These results indicate that the shared task enables cross-task knowledge transfer and the
task-level representations capture task-dependent features for SC and ED efficiently .
The third sample instance which is labeled as neutral is incorrectly predicted as negative. This may be due to
the presence of complaint-related lexical cues, which introduce bias towards SC. Likewise, in the fourth instance,
sentiment polarity is misclassified and the predicted emotion deviates from the ground truth due to overlapping
affective expressions. These errors suggest that the multi-task model enhances contextual feature learning, but
the presence of subtle sentiment and emotion expressions remains challenging in complex real-world review
texts.
Parametric analysis
This section presents the analysis of three model parameters to examine the performance of our proposed
COSMO-MT model.
GRU—hidden units
Choosing the exact number of GRU hidden units significantly impacts the learning capacity and performance
of the model. Figures 2 and 3 present the impact of GRU hidden units in terms of F1-score and accuracy on
dataset-1 and dataset-2, respectively for both tasks. Observe that, 128 hidden units performs better as compared
to 64 and 256 hidden units of GRU. The selection of 64 hidden units shows lower representational capacity of
the model, whereas 256 hidden units introduce potential overfitting and increased computational complexity
for both tasks.
CNN—kernel sizes
The selection of an appropriate CNN kernel size helps the model to effectively balance the capture of semantic,
syntactic, and contextual features. Figures 4 and 5 present the impact of different CNN kernel sizes in terms
of F1-score and accuracy on dataset-1 and dataset-2, respectively for both tasks. Observe that, kernel size of
5 achieves the highest performance for both evaluation metrics across datasets and tasks. The reason is that
a medium-sized kernel captures the most relevant features and provides an optimal balance between feature
extraction and classification performance on both datasets for SC and ED.
Fig. 2. Performance evaluation results of proposed model on the two tasks with different GRU hidden units on
Dataset-1. (Source Authors’ own analysis based on experimental results).

Sample
Actual
SC Pred SC
Actual
ED
Pred
ED
After weeks of waiting, the package finally arrived damaged. I tried contacting support multiple times but received no response, which
has been incredibly frustrating and exhausting. Negative Negative Anger Anger
The headphones are surprisingly comfortable and the sound clarity is better than I expected. I was honestly not anticipating this level
of quality at this price point. Positive Positive Surprise Joy
The product functions as described, but the constant software glitches make me uneasy about its long-term reliability. I’m not entirely
confident it will last. Neutral Negative Fear Sadness
Although the seller eventually refunded my payment, the entire experience left a bad impression. It wasn’t terrible, just disappointing
overall. Negative Neutral Sadness Disgust
Table 5. Few Samples for qualitative and error analysis in terms of actual and predictive (Pred) outcomes.

Scientific Reports |        (2026) 16:33392 12| https://doi.org/10.1038/s41598-026-72542-7
www.nature.com/scientificreports
Fig. 5. Performance evaluation results of proposed model on the two tasks with different CNN Kernel sizes on
Dataset-2. (Source Authors’ own analysis based on experimental results).

Fig. 4. Performance evaluation results of proposed model on the two tasks with different CNN Kernel sizes on
Dataset-1. (Source Authors’ own analysis based on experimental results).

Fig. 3. Performance evaluation results of proposed model on the two tasks with different GRU hidden units on
Dataset-2. (Source Authors’ own analysis based on experimental results).

Scientific Reports |        (2026) 16:33392 13| https://doi.org/10.1038/s41598-026-72542-7
www.nature.com/scientificreports
Optimization algorithms
Optimization algorithms are crucial for efficiently updating model parameters, ensure faster convergence,
stable training, and improved overall performance. Figures 6 and 7 present the impact of different optimization
algorithms, including Adadelta, Adam, and RMSProp in terms of F1-score and accuracy on dataset-1 and
dataset-2, respectively for both tasks. Observe that, Adam achieves the highest performance and demonstrates
superior convergence and stability compared to Adadelta and RMSProp. These results indicate that Adam
provides a better balance between adaptive learning and gradient optimization. Thus, it is the best-suited
optimizer for the proposed model.
Findings and limitations
This study introduces COSMO-MT, a novel multi-task model that outperforms existing SOTA and baseline
methods for joint SC and ED tasks. We observe several key findings from this work: (i) our proposed model
integrates shared contextual encoding with task-specific attention layers to provide cross-task knowledge
transfer, (ii) the combination of local feature extraction (CNN), sequential modeling (BiLSTM), and attention
layers enhances representation learning, and (iii) the multi-task modeling improves generalization and predictive
performance on both datasets. The empirical evidence indicates that the integration of components at shared
and task-specific layers contributes to substantial improvements in model performance.
We also notice certain limitations, such as the reliance on domain-specific datasets, which may introduce
inherent distributional biases. Consequently, misclassifications may occur in ambiguous or overlapping
emotional contexts. Subtle emotional expressions may not be fully captured by the model. In addition, the
lexicon-based emotion annotation strategy may introduce uncertainty in reviews containing subtle, implicit, or
overlapping emotional expressions. These limitations emphasize the importance of comprehensive evaluation
and methodological transparency.
Fig. 7. Performance evaluation results of proposed model on the two tasks with different optimization
algorithms on Dataset-2. (Source Authors’ own analysis based on experimental results).

Fig. 6. Performance evaluation results of proposed model on the two tasks with different optimization
algorithms on Dataset-1. (Source Authors’ own analysis based on experimental results).

Scientific Reports |        (2026) 16:33392 14| https://doi.org/10.1038/s41598-026-72542-7
www.nature.com/scientificreports
Discussion
The proposed COSMO-MT framework has significant potential for real-world applications because it jointly
learns sentiment polarity and emotional states from textual data. Traditional sentiment analysis approaches
typically classify opinions as positive, negative, or neutral, which may overlook the emotional factors underlying
user opinions. The proposed COSMO-MT model provides a more comprehensive understanding of user-
generated content and enables richer interpretation of consumer behaviour by combine modeling of sentiment
and emotion.
In consumer analytics, the proposed model can help organizations identify not only whether customers are
satisfied or dissatisfied, but also the specific emotions associated with their experiences, such as joy, trust, anger,
sadness, or frustration. Leveraging such information can support targeted marketing campaigns, customer
retention strategies, and product improvement initiatives. Likewise, in customer feedback monitoring and
opinion mining, the combination of sentiment and emotion information can facilitate the early detection of
emerging issues and service-related concerns, which allow organizations to respond proactively before negative
perceptions spread widely.
The proposed model can also be valuable for personalized recommendation systems. Incorporate emotional
signals together with sentiment information, recommendation engines can better capture user preferences
and contextual reactions, potentially improving recommendation relevance and user engagement. In business
intelligence applications, aggregated sentiment-emotion trends can provide decision-makers with deeper
insights into customer perception, brand reputation, and market dynamics. These insights can support strategic
planning, competitive analysis, and evidence-based decision-making.
An additional advantage of the proposed approach is the use of multi-task learning, which enables knowledge
sharing between sentiment and emotion classification tasks. Since sentiment and emotion are inherently related,
jointly learning both tasks allows the model to capture complementary information and improve representation
learning. This capability is particularly useful in real-world scenarios, where emotional context can strengthen
sentiment interpretation and vice-versa.
Despite its promising performance, the proposed model is evaluated on benchmark datasets within a
controlled experimental environment. Future work may investigate the deployment of COSMO-MT in large-
scale real-time applications, explore GPU-accelerated implementations for enhanced computational efficiency,
and assess its effectiveness across multilingual and domain-specific datasets. Such extensions would further
demonstrate the scalability and practical applicability of the proposed model in diverse industrial settings.
Conclusion and future works
This study demonstrates the importance of combining sentiment and emotion analysis in customer reviews
and corresponding ratings to provide deeper insights into consumer behavior and to support the development
of adaptive, sentiment-responsive digital environments that account for consumers’ emotional states. We have
proposed a new DL-based multi-task model referred to as COSMO-MT for SC and ED on consumer reviews and
ratings. It has consisted of input, embedding, shared, task-specific, dense, and output layers. The input layer has
transformed the input texts into input vectors. The embedding layers have provided sentiment, emotion, and
shared (sentiment and emotion) embeddings from the input vector. Thereafter, shared layers have constituted
of CNN, BiLSTM, and attention layers and receive the corresponding embedding outputs. The shared layers
have facilitated knowledge sharing between SC and ED by learning common representations that capture both
semantic and contextual information from consumer reviews and ratings. Furthermore, a rich set of hand-crafted
auxiliary features have incorporated within the shared layers to enhance the linguistic coverage. The outputs of
the shared layers have passed to the task-specific layers to accomplish sentiment- and emotion-specific tasks,
followed by dense and output layers that perform SC and ED. We have conducted extensive experiments on two
well-known datasets. Experimental results have shown that our proposed model outperforms existing SOTA
and baseline methods. Overall, the proposed COSMO-MT framework demonstrates the effectiveness of joint
sentiment and emotion learning for improving consumer-centric opinion analysis.
In the future, research on multi-task learning approaches for SC and ED can advance in several key
directions. Consideration of multi-modal data sources, such as voice signals, chat interactions, and social media
content could enrich shared representations. One of the possible research directions could be the adoption of
domain-adaptive multi-task models. Moreover, applying multilingual and multi-task related models can support
analysis across multiple languages in future. Integration of multi-task related models with predictive analytics
could support several applications, such as churn prediction, data erasure or access request forecasting, and
personalized service delivery. Future work can also focus on the improvement of task interaction and balance
learning between sentiment and emotion to enhance the overall performance of the model. Provide simpler
and more efficient multi-task architectures may reduce computational cost and improve scalability. Future work
may also explore more advanced contextual and human-assisted emotion annotation strategies to better handle
implicit and overlapping emotional expressions. The proposed model achieves promising results, its evaluation
is currently limited to benchmark datasets. Future work will explore GPU-accelerated implementations and
broader validation across multi-lingual and domain-specific real-world applications. Lastly, ethical issues, such
as bias, transparency, and data privacy need to be addressed to ensure responsible use in future work.
Data availability
In this study, two publicly available benchmark datasets are used from the following repositories: (i) Amazon
product review—2023 dataset: https://amazon-reviews-2023.github.io/ and (ii) Women’s clothing e-Commerce
dataset: https://www. kaggle.com/d atasets/nica potato/wome ns-ecommerce-clothing-reviews.

Scientific Reports |        (2026) 16:33392 15| https://doi.org/10.1038/s41598-026-72542-7
www.nature.com/scientificreports
Code availability
The source code is available at GitHub: https://github.com/Ashraf-Kamal/COSMO-MT. The source code  i s a r c h
i v e d in Zenodo with the following DOI:https://doi.org/10.5281/zenodo.20750033.
Received: 6 March 2026; Accepted: 16 September 2026
References
 1. Ashraf, S., Rasheed, Z. & Arbaz, M. Adopting proactive results by developing the shrewd model of pandemic covid-19. Arch.
Commun. Med. Public Health 8, 062–067 (2022).
 2. Ashraf, S. Development of sustainable wireless resource model through shrewd neural network. DI 6, 649–665 (2024).
 3. Rana, M. R. R. et al. BERT-BiGRU-Senti-GCN: An advanced NLP framework for analyzing customer sentiments in e-commerce.
Int. J. Comput. Intell. Syst. 18, 21 (2025).
 4. Abulaish, M., Kamal, A. & Zaki, M. J. A survey of figurative language and its computational detection in online social networks.
ACM Trans. Web (TWEB) 14, 1–52 (2020).
 5. Kamal, A. & Abulaish, M. Contextualized satire detection in short texts using deep learning techniques. J. Web Eng. 23(1), 27–52
(2024).
 6. Sandiwarno, S., Sensuse, D. I., Santoso, H. B., Hidayat, D. S. & Nyamawe, A. S. Semar: A multi-task term weighting approach for
sentiment and emotion-based e-learning users’ satisfaction analysis. IEEE Access 13, 187584–187601 (2025).
 7. Kim, Y . Convolutional neural networks for sentence classification. In Proceedings of the EMNLP 1746–1751 (ACL, 2014).
 8. Hochreiter, S. & Schmidhuber, J. Long short-term memory. Neural Comput. 9, 1735–1780 (1997).
 9. Vaish, N., Goel, N. & Gupta, G. Machine learning techniques for sentiment analysis of hotel reviews. In Proceedings of the
International Conference on Computer Communication and Informatics (ICCCI), 01–07 (2022).
 10. Kausar, A., Kanwar, G. & Kumar, R. Emotion detection using sentiment analysis. In Proceedings of the International Conference on
Integration of Computational Intelligent System (ICICIS), 1–5 (2023).
 11. Kumar, K., Singh, S., Kumar, A. & Singh, A. S. Sentimental analysis of customer’s reviews using machine learning. In Proceedings
of the International Conference on Advances in Computing, Communication Control and Networking (ICAC3N), 326–330 (2023).
 12. Fahim, S. Twitter sentiment analysis based public emotion detection using machine learning algorithms. In Proceedings of the 17th
International Conference on Emerging Technologies (ICET) 107–112 (2022).
 13. Sahoo, C., Wankhade, M. & Singh, B. K. Sentiment analysis using deep learning techniques: A comprehensive review. Int. J.
Multimed. Inf. Retrieval 12, 41 (2023).
 14. Habimana, O., Li, Y ., Li, R., Gu, X. & Yu, G. Sentiment analysis using deep learning approaches: An overview. Sci. China Inf. Sci.
63, 111102 (2020).
 15. Rasheed, Z., Ashraf, S. & Mehak, S. K. M. Ansec-mm: Identifying antecedents of negative public sentiment through expression
capacity: A mixed-methods approach to crisis mitigation. Data 10, 203 (2025).
 16. Ashraf, S. & Choi, C. XP-STM: A cross-platform sentiment transferability model for negative public sentiment identification and
mitigation. J. Eng. Res. 14, 1548 (2025).
 17. Ashraf, S. Expression capacity-based negative sentiment (ECNS) detection and mitigation in online social networks. J. Intell.
Commun. 5, 99–115 (2026).
 18. Madhurika, B. & Malleswari, D. N. Deep learning based sentinet architecture with hyperparameter optimization for sentiment
analysis of customer reviews. Sci. Rep. 15, 35525 (2025).
 19. Park, S., Jiang, Y . & Kim, H. Importance-induced customer segmentation using explainable machine learning. J. Mech. Des. 147,
044501 (2025).
 20. Siam, A. I., Soliman, N. F ., Algarni, A. D., El-Samie, F . E. A. & Sedik, A. Deploying machine learning techniques for human
emotion detection. Comput. Intell. Neurosci. 2022, 8032673 (2022).
 21. Pereira, P ., Moniz, H. & Carvalho, J. P . Deep emotion recognition in textual conversations: A survey. Artif. Intell. Rev. 58, 1–37
(2025).
 22. Bharti, S. K. et al. Text-based emotion recognition using deep learning approach. Comput. Intell. Neurosci. 2022, 2645381 (2022).
 23. Adamu, H., Murad Azmi, A. M. & Nasharuddin, N. A. A hybrid stacked ensemble learning framework for multilabel text emotion
detection. Sci. Rep. 16, 7714 (2026).
 24. Khan, B., Usman, M. & Binsawad, M. A novel hybrid model for emotion detection in text through sequential and transformer-
based approaches: LSTM enhanced roberta (LER). Sci. Rep. 16, 2224 (2026).
 25. Nguyen, V .-H. et al. Customer emotion detection and analytics in hotel and tourism services using multi-label classificational
models based on ensemble learning. Ann. Oper. Res. 353, 575–605 (2025).
 26. Prova, N. Multilingual emotion classification in e-commerce customer reviews using GPT and deep learning-based meta-ensemble
model. Available at SSRN 5161505 (2025).
 27. Duyu  Tang, F .  W ., Y ang, N., Zhou, M., Liu, T. & Qin, B. Learning sentiment-specific word embedding for twitter sentiment
classification. In Proceedings of the 52nd ACL, 1555–1565 (ACL, 2014).
 28. Xu, P ., Madotto, A., Wu, C.-S., Park, J. H. & Fung, P . Emo2vec: Learning generalized emotion representation by multi-task training.
Proceedings of the WASSA 292–298 (2018).
 29. Devlin, J., Chang, M.-W ., Lee, K. & Toutanova, K. Bert: Pre-training of deep bidirectional transformers for language understanding.
In Proceedings of the NAACL-HLT, 4171–4186 (2019).
 30. Luong, M.-T., Pham, H. & Manning, C. D. Effective approaches to attention-based neural machine translation. In Proceedings of
the EMNLP 1412–1421 (2015).
 31. Bradley, M. M. & Lang, P . J. Affective norms for English words (anew): Instruction manual and affective ratings. Technical report
C-1, the center for research in psychophysiology, University of Florida (1999).
 32. Xu, G., Chen, Z. & Zhang, Z. Aspect category sentiment analysis based on pre-trained BiLSTM and syntax-aware graph attention
network. Sci. Rep. 15, 3333 (2025).
Author contributions
Conceptualization, Farhan Alam (F .A.), Ashraf Kamal (A.K.), Mohammad Meraj (M.M.), Mohd Fazil (M.F .),
and Ahmad Kamal (AH.K.); Software, A.K., M.M., and M.F .; validation, F .A. M.M., Shakir Khan (S.K.), Shama
Faridi (S.F .), Saqib Qamar (S.Q.); data curation, F .A, A.K., M.M., AH.K.; writing-original draft preparation, F .A.,
A.K., M.M. M.F; writing-review and editing, F .A, A.K, M.M., M.F ., AH.K., S.K. S.F , M.F ., Riyad Almakki (R.A.);
visualization, F .A., A.K., M.F ., S.F , AH.K., S.Q; supervision, A.K; project administration, S.K.; funding acquisi-
tion, S.K.,M.F .; All authors have read and agreed to the published version of the manuscript.

Scientific Reports |        (2026) 16:33392 16| https://doi.org/10.1038/s41598-026-72542-7
www.nature.com/scientificreports
Declarations
Competing interests
The authors declare no competing interests.
Additional information
Correspondence and requests for materials should be addressed to S.Q.
Reprints and permissions information is available at www.nature.com/reprints.
Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and
institutional affiliations.
Open Access  This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives
4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in
any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide
a link to the Creative Commons licence, and indicate if you modified the licensed material. Y ou do not have
permission under this licence to share adapted material derived from this article or parts of it. The images or
other third party material in this article are included in the article’s Creative Commons licence, unless indicated
otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence
and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to
obtain permission directly from the copyright holder. To view a copy of this licence, visit  h t t p : / / c r e a t i v e c o m m o
n s . o r g / l i c e n s e s / b y - n c - n d / 4 . 0 /     .
© The Author(s) 2026
