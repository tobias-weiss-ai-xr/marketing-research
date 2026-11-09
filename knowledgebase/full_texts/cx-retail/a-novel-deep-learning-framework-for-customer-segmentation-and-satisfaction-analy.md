---
title: A Novel Deep Learning Framework for Customer Segmentation and Satisfaction Analysis in Tourism
  using Multimodal User-generated Content
url: https://doi.org/10.5815/ijisa.2026.05.08
category: cx-retail
subcategory: framework
date: 2026-09
venue: International Journal of Intelligent Systems and Applications
authors:
- Gaganmeet Kaur Awal
- Ujjwal Tehlan
source: openalex-oa
pdf_url: https://www.mecs-press.org/ijisa/ijisa-v18-n5/IJISA-V18-N5-8.pdf
pages: 20
chars: 91039
fetched_at: '2026-11-08T18:50:46+00:00'
kb_version: 1
---

# A Novel Deep Learning Framework for Customer Segmentation and Satisfaction Analysis in Tourism using Multimodal User-generated Content

I.J. Intelligent Systems and Applications, 2026, 5, 153-172
Published Online on October 8, 2026 by MECS Press (http://www.mecs-press.org/)
DOI: 10.5815/ijisa.2026.05.08
This work is open access and licensed under the Creative Commons CC BY 4.0 License.
A Novel Deep Learning Framework for Customer
Segmentation and Satisfaction Analysis in
Tourism using Multimodal User -generated
Content

Gaganmeet Kaur Awal
Delhi School of Management, Delhi Technological University (Formerly Delhi College of Engineering, Govt. of NCT of
Delhi), New Delhi, India
E-mail: gaganmeetkaur.awal@dtu.ac.in
ORCID iD: https://orcid.org/0000-0003-1403-5792

Ujjwal Tehlan*
Delhi School of Management, Delhi Technological University (Formerly Delhi College of Engineering, Govt. of NCT of
Delhi), New Delhi, India
E-mail: tehlan2000@gmail.com
ORCID iD: https://orcid.org/0009-0001-7425-2978
*Corresponding author

Received: April 3, 2026; Revised: June 20, 2026; Accepted: July 24, 2026; Published: October 8, 2026

Abstract: The tourism industry has experienced substantial growth in recent years, propelled by the evolving customer
preferences and pervasive influence  of social media platforms. To gain a competitive advantage, it is imperative to
develop innovative approaches that enable the delivery of personalized services and a deeper understanding of customer
satisfaction. By leveraging user -generated content, firm s can better understand dynamic customer trends and optimize
their marketing strategies accordingly. However, our research aims to develop a novel customer segmentation framework
using advanced deep learning techniques to analyze user -generated content within the rapidly growing tourism industry.
The methodology employs a novel hybrid deep learning approach that integrates Sentence-BERT for contextualized
embeddings and a GRU-based Autoencoder for feature reduction  in an adaptive manner. This process is followed by k-
means clustering, which segments  customers using both multi-criteria ratings and online reviews to provide a holistic
understanding of customer experiences. The proposed framework's effectiveness is compared with multiple state -of-the-
art models using robust evaluation metrics such as the silhouette coefficient and the Davies –Bouldin index. The study’s
findings highlight that the proposed model classifies customers into four distinct segments , and the statistical test
performed shows the significance of our result.  The research study contributes to the advancement of user -generated
content based market segmentation in the tourism industry by unifying textual and numerical feedback into a single
analytical framework. The findings offer valuable ins ights for tourism businesses seeking to enhance  customer
satisfaction through personalized service strategies and data-driven decision-making.

Index Terms: Market Segmentation, Customer Satisfaction, BERT, Text Mining, Tourism Industry, Gated Recurrent
Unit, Autoencoder.

1. Introduction
The tourism industry has  recently emerged as a leading force  in the global economy, offering various employment
opportunities and stimulating trade and investment activities worldwide [1]. The growing prominence of this industry is
propelled by the forces of globalization, rapid technological advancements, and evolving con sumer behaviors, thereby
gaining traction as a legitimate area of interest among the research community [2]. Customer satisfaction has traditionally
been a cornerstone for sustaining growt h in the hospitality industry by providing exceptional customer experiences [3].
According to the expectation-disconfirmation paradigm [4], customer satisfaction is determined by comparing a product
or service’s perceived performance with the customer’s prior expectations.  However, the dynamic shift of customer

A Novel Deep Learning Framework for Customer Segmentation and Satisfaction Analysis in Tourism using
Multimodal User-generated Content
Volume 18 (2026), Issue 5 – Page 154
preferences and the increasing intensity of market competition necessitate innovative approaches for predicting and
understanding customer satisfaction , as well as  delivering personalized services to enhance customer retention  [5].
Establishing a competitive advantage through customer experiences has become one of the primary strategic objectives
of contemporary firms [ 6]. Recent technological advancements have led to a substantial increase in the availability and
accessibility of customer-related data. This development has urged researchers to explore various data -driven marketing
strategies to enhance customer experience and improve business profitability across industries such as
telecommunications, hospitality, and hotels [7].
The segmentation of customers is a fundamental aspect of strategic planning and marketing strategy, serving as a
necessary pillar of effective marketing [ 8]. It involves grouping consumers with similar characteristics, behaviors, and
preferences to tailor products and services more effectively [ 9]. The widespread adoption of Information and
Communication Technology has created essential platforms for consumers to share their experiences with products and
services [10]. User-generated content (UGC) is recognized as the most reliable source of information, and as a prevalent
form of Electronic Word of Mouth (eWOM), it exerts significant influence on consumer behavior and decision-making
processes [11]. Over the past few years, eWOM has transformed the competitive landscape for businesses, as customers
often base their purchasing decisions on eWOM before making a purchase . As the tourism industry thrives and UGC
flourishes, this data has garnered significant attention from hospitality researchers seeking to opti mize enterprise
performance [12]. UGC-based customer segmentation models are more feasible and effective than conventional methods,
such as questionnaires or interviews, which are prone to selection bias [1 3].
Many studies have been conducted across various domains to investigate customer satisfaction, preferences, and
segmentation using online reviews and multi -criteria ratings [14,15]. Despite the widespread use of UGC for customer
segmentation and preference prediction, researchers have not yet explored leveraging the combined potential of online
textual reviews and multi -criteria ratings in the tourism industry  through deep learning -based architectural integration .
Existing research predominantly relies on online reviews and multi-criteria ratings individually [16,17] or combines them
through post-hoc concatenation [ 18], thereby missing opportunities for deeper and more nuanced ins ights into tourists'
preferences and experiences that emerge through joint feature learning.
With the increasing prominence of machine learning and deep learning methodologies, research studies have
demonstrated the efficacy of these approaches in extracting dimensions of customer experience, identifying emerging
market segments, and uncovering valuable insights in a cost-efficient manner [14,18-21]. Various text mining techniques
have been employed, such as topic modeling for uncovering customer experience themes and autoencoders for feature
reduction and extraction [22,23]. Various algorithms lik e support vector machines and swarm optimization have been
used for predictive tasks, while different clustering techniques such as self -organizing maps, k-means, and other
unsupervised learning methods have been applied to customer segmentation. Although these techniques provide valuable
insights, a major challenge persists in identifying relevant features without losing the rich semantic content of user -
generated content.
Moreover, conventional approaches [24,25] often fail to adequately capture the contextual significance and long-
term dependencies inherent in textual content. This limitation restricts their ability to extract a compact and informative
feature space from customer reviews. Textual sequences often need to consolidate information from different sections of
the text. Feature extraction is crucial for identifying the most concise and informative representation while preventing the
processing of redundant or irre levant data. In this context, Bidirectional Encoder Representations from Transformers
(BERT) provides high -quality semantic embeddings by capturing deep contextual relationships between words [26].
Gated Recurrent Unit (GRU) also addresses the limitation by retaining essential information over long sequences through
a gating mechanism [27], making them well-suited for handling the complexity of textual UGC.
To address the research gaps , the study proposes a novel framework, BIGA (BERT Integrated GRU-based
Autoencoder), that integrates Sentence-BERT contextualized embeddings with GRU-based autoencoder feature reduction
and multi-dimensional ratings for hospitality customer segmentation . While individual components have been explored
in isolation —BERT variants for text classification [ 28,29], GRU autoencoders for time -series analysis [ 30,31], and
various machine learning approaches for segmentation [15,17,3 2,33]—no prior research  in hospitality literature has
combined these specific techniques for unsupervised customer segmentation using both textual reviews and numerical
ratings. The primary contributions of our paper are outlined below:

• Our proposed work is a pioneering attempt to develop a novel framework, BIGA (BERT Integrated GRU-based
Autoencoder), that considers semantic and contextual information and then extracts relevant latent dimensions
to identify customer segments. Firstly, Sentence-BERT is utilized to transform raw textual data into
contextualized embeddings to capture text sequences' context and underlying structure. Subsequently, a GRU -
based Autoencoder is applied for more compact and informative feature reduction with relevant ess ential
information from the online reviews. This hybrid approach integrates t he strengths of BERT and GRU -based
Autoencoder to extract rich latent embedded dimensions/features. Then, these latent features combined with
multi-criteria numerical ratings are analyzed using k-means clustering to identify distinct customer segments.
The framework is designed to preserve long -term contextual information without degradation of important
information while effectively reflecting customer preferences derived from UGC.
• Our research also addresses the underexplored integration of online textual reviews and numerical multi-criteria
ratings together for customer segmentation. The proposed BIGA framework's effectiveness was empirically and

A Novel Deep Learning Framework for Customer Segmentation and Satisfaction Analysis in Tourism using
Multimodal User-generated Content
Volume 18 (2026), Issue 5 – Page 155
statistically validated through comprehensive experiments on a real-world dataset.

The remainder of this paper is organized in the following manner: Section 2 outlines the existing body of literature
and summarizes relevant previous research. Section 3 provides the methodology of the proposed framework BIGA.
Section 4 provides a description of  the dataset utilized in the study and details about the  experimental setup for
benchmarking against several state -of-the-art models. Section 5 presents the experimental results, analyzes the model’s
performance, and discusses the implications of the findings.  Furthermore, Section 6 provides a summary of the study’s
key findings, limitations, and conclusions.
2. Literature Review
This section provides an overview of  the literature on various approaches for market segmentation and customer
satisfaction, contrasting traditional methods with different machine learning and deep learning algorithms. It also explores
the emerging trends and identifies research gaps within the field.
Traditionally, customer segmentation in the hospitality industry divides consumers into segments based on specific
characteristics such as age, gender, pain point, demographics, geography, psychographics, behavior, or value [ 34-36].
The optimization of resource allocation and delivering personalized services and products have become integral
components of contemporary firms' strategic objectives. However, with the proliferation of big data and recent
technological advancements driven by social media, businesses are shifting towards need-based segmentation to analyze
behavioral patterns and customer preferences over static attributes [37,38].
The proliferation of UGC and eWOM has revolutionized how businesses understand customer satisfaction [12].
Online reviews can serve as a reflection of customer experiences making them a valuable source for customer
segmentation [30]. Unlike traditional segmentation through questionnaire surveys, which are often prone to selection bias,
segmentation through UGC provides real -time insights into customer experiences. In recent years, researchers have
largely focused on employing UGC, which includes social media posts, textual reviews, and numerical ratings for needs-
based and behavioral segmentation [13,3 7-39]. Elwalda et al. [3 9] highlight that online reviews significantly influence
customer perception. Sparks and Browning [ 40] emphasize the role of online reviews in guiding consumer decision -
making in the tourism industry. Furthermore, Zhang et al. [ 41] demonstrated that customer -generated reviews are
positively associated with hotel popularity. Jiang et al. [13] also highlighted the role of UGC for need-based segmentation
and generated the consumer characteristics matrix for describing segments. Due to the significant attention, many
businesses are investing substantial resources to better understand consumers' wants and preferences and assess their
satisfaction with products and services [42].
Previous research has employed UGC, particularly online reviews and multi-criteria ratings, to understand customer
satisfaction, preferences, and segmentation, specifically based on prediction and classification tasks [18-23]. Nilashi et al.
[19] employed deep belief networks to predict customer choice, self -organizing maps for clustering, and latent Dirichlet
allocation for feature extraction based on past ratings and reviews in the tourism context. Alsayat [18] introduced an
integrated framework for exami ning large-scale social datasets by  combining support vector regression, latent Dirichlet
allocation, and k-means clustering. Furthermore, Nilashi et al. [20] developed a hybrid methodology that combines self-
organizing maps, latent Dirichlet allocation, and a classification -and-regression-tree-based predictive technique  for
evaluating customer satisfaction in vegetarian restaurants. Nilashi et al. [21] further explored the impact of online reviews
on understanding customer preferences by employing multi -criteria decision -making techniques alongside machine
learning approaches. The proposed model [21] incorporated the Expectation -Maximization algorithm for clustering
reviews, higher-order singular value decomposition for analyzing traveler preferences, and the Adaptive Neuro-Fuzzy
Inference System for supervised learning.
Various other approaches have also been applied in the literature. Ahani et al. [22] proposed a  hybrid machine
learning approach that includes self -organizing maps, higher -order singular value decomposition, classification and
regression trees, and text mining techniques for travel prediction based on customer reviews. Using a data mining
approach, Martinez-Torres and Toral [23] identified polarity -oriented features that effectively distinguish deceptive and
non-deceptive reviews in the hospitality industry . However, existing studies have primarily explored online reviews and
multi-criteria ratings separately to understand customer decision -making, satisfaction, and prediction in the various
domains of the hospitality industry.
Numerous other studies have also focused on analyzing customer satisfaction and segmentation within the hospitality
industry by employing different machine learning and deep learning methodologies [15 -17,28,33]. Ansari [15] used a
combination of unsupervised artificial neural networks and self -organizing maps to perform market segmentation in the
B2B industrial automation  sector. Similarly, Alghamdi [3 3] integrated clustering with an artificial neural network,
utilizing a particle swarm optimization technique for clustering and prediction tasks in the restaurant industry for customer
segmentation. Khan et al. [ 28] proposed a bidirectional Long Short-Term Memory (LSTM) model with convolutional
attention that combines next-word, next-sequence, and pattern prediction techniques to improve aspect category detection.
To address the challenge associated with high-dimensional textual representations, prior research has applied various
dimensionality reduction techniques. Alkhayrat et al. [17] compared Principal Component Analysis (PCA) and
feedforward autoencoders for cu stomer segmentation in the telecommunications industry to demonstrate that nonlinear

A Novel Deep Learning Framework for Customer Segmentation and Satisfaction Analysis in Tourism using
Multimodal User-generated Content
Volume 18 (2026), Issue 5 – Page 156
autoencoders outperform linear PCA for analyzing numerical tabular features rather than textual embeddings. Hosseini
and Varzaneh [43] applied stacked autoencoders for deep text clustering, achieving improved performance over traditional
methods. However, their approach used conventional word embeddings as input rather than contextualized transformer -
based representations, and focused on document-level topic clustering rather than customer segmentation with integrated
ratings. Che et al. [ 44] proposed a Sta cked Variational Autoencoder for text feature extraction in classification tasks,
operating on character -level or word -level embeddings without sentence -level transformer outputs or multi -modal
integration with structured data. However, these studies relied on conventional word embeddings and did not utilize
contextualized transformer-based representations or integrate structured ratings data.
More recently, researchers have increasingly adopted modern , contextualized word embedding techniques, such as
BERT [26,29], to capture more syntactic and semantic properties of words within their linguistic context. Yi and Hu [30]
explored the use of a pre -trained BERT-GRU model for relation extraction. Their hybrid approach effectively captured
both lexical meaning and syntactic dependencies, which helped it outperform existing methods. Ma et al. [31] introduced
a BERT-enhanced Bidirectional LSTM Conditional Random Field model  to extract temporal information from Chinese
social media messages. Autoencoders have also been explored to learn compact and informative representations of textual
data for downstream tasks such as classification and clustering. Huang et al. [45] used a Recurrent Neural Network-based
Variational Autoencoder to reduce the features in sequential data while preserving  high-dimensional information. In
another study, Abboush et al. [46] proposed a GRU-based autoencoder for denoising purposes and applied the clustering
k-means algorithm to identify faults and group data in sequential datasets.
Despite extensive research on UGC-based customer segmentation using various machine learning and deep learning
approaches, the early methods were predominantly grounded in text mining techniques and topic modeling, such as Latent
Dirichlet Allocation for feature extraction, Higher-Order Singular Value Decomposition, and sentiment analysis to extract
opinions from textual reviews. These traditional methods have proven ineffective in analyzing text -review data due to
their context-dependent nature, as they often fail to capture long-range contextual information inherent in natural language.
The architectural design adopted in our study is grounded in the evolution of recurrent neural network architectures.
Conventional Recurrent Neural Networks (RNNs) are theoretically capable of modeling sequential dependencies, but are
fundamentally limited  by the vanishing and exploding gradients during backpropagation through time [ 47], thereby
restricting their effectiveness in learning long-range dependencies. LSTM was subsequently introduced to mitigate these
limitations, but it requires significant com putational resources and a complex architecture [48]. Therefore, GRU was
introduced as a computationally efficient alternative to LSTM, performing the gating operations with two gates: an update
gate and a reset gate for controlling the information flow an d retaining the context [27]. The update gate governs the
extent to which the preceding hidden state is propagated forward, while the reset gate determines the degree to which
prior contextual information is discarded [47]. However, the motivation for employing GRU layers within our architecture
is fundamentally and deliberately grounded in the adaptive gating-based non-linear transformation capability of the GRU,
rather than in its sequential dependency modeling property.
To the best of our knowledge, our study is among the first in the hospitality domain to jointly feed both contextual
textual embeddings and structured multi-criteria ratings into a unified deep learning framework for unsupervised customer
segmentation. This integration provides deeper and meaningful insights about customer preferences and experiences
within the tourism industry. Our proposed BIGA framework addresses this gap by seamlessly integrating Sentence-BERT
embeddings and GRU-based Autoencoder reduced feature representations, along with multi-criteria ratings, into a unified
feature space for k-means clustering, enabling a more holistic, semantically enriched understanding of customer behavior
and satisfaction.
3. Methodology
This section outlines the steps involved in the  proposed BIGA framework for effectively segmenting customers  in
the tourism industry. The proposed model is developed in three phases: starting with pre-trained BERT word embeddings
for feature extraction, then employing a dimensionality reduction technique to reduce features, and finally, performing k-
means clustering to identify segments. The proposed BIGA framework is illustrated in Figure 1. The BIGA framework
consists of the following steps:

Step 1 The collected dataset containing textual reviews and multi-criteria ratings was pre-processed.
Step 2 The cleaned text was then passed through a pre -trained Sentence-BERT model to generate contextualized
embeddings.
Step 3 A GRU -based Autoencoder was utilized to create a more compact and informative feature space on the
contextualized embeddings to retain high-dimensional information.
Step 4 k-means clustering was applied to the relevant latent features along with multi -criteria ratings to segment
customers into distinct groups.
3.1. Data Preprocessing
Initially, the text data underwent preprocessing steps to ensure data quality and reliability. Firstly, the reviews were
filtered to retain only English-language reviews for semantic embedding. Reviews with missing values in any of the key

A Novel Deep Learning Framework for Customer Segmentation and Satisfaction Analysis in Tourism using
Multimodal User-generated Content
Volume 18 (2026), Issue 5 – Page 157
attributes—including overall rating, cleanliness, value, location, room, sleep quality, hotel ID, user ID, review text, stay
year, and title—were excluded for data integrity and multimodal analysis. Additionally, a minimum length threshold was
applied to remove reviews containing fewer  than 5 words. Following these initial filters , text cleaning operations were
performed, specifically removing square-bracketed text, punctuation, URLs, HTML tags, and words containing digits, to
ensure clean, more focused input for feature extraction and reduction.  These preprocessing steps eliminated extraneous
noise while preserving the linguistic structure and semantic content of the reviews. The Sentence-BERT model is
pretrained on natural language text , relies on contextual word relationships, and does not require traditional natural
language processing techniques, such as stopword removal and lemmatization, as these would disrupt linguistic patterns
and significantly degrade embedding quality [49].

Fig. 1. Proposed BIGA framework
3.2. Feature Extraction using BERT Embeddings
It is essential to convert text into numerical values before using machine learning models, such as neural networks,
to enable  computers to understand natural language  [50]. Text representation plays a key role in model training and
identifying data patterns. Our proposed model utilizes a pre -trained transformer -based sentence embedding model,
sentence-transformers/all-mpnet-base-v2, implemented via the Sentence Transformers framework  [51]. The model
generates contextualized embeddings  using a multi -layer transformer encoder with 12 attention heads, 12 transformer
layers, and 768 hidden dimensions per layer  [51]. The model contains approximately 110 million parameters. In this

A Novel Deep Learning Framework for Customer Segmentation and Satisfaction Analysis in Tourism using
Multimodal User-generated Content
Volume 18 (2026), Issue 5 – Page 158
process, each review in our dataset is mapped to a feature with an associated weight and generates a dense representation
that reflects the sentiments of the text . Also, Senten ce-BERT incorporate s mean-level pooling strategies , and after
tokenization, the model automatically truncates the input to a maximum sequence length  of 512 tokens.
3.3. Feature Reduction using GRU-based Autoencoder
The compact feature space, which contains essential information, is pivotal for the subsequent application of the
models. Optimizing model performance requires the identification of key, relevant, and informative features. In recent
years, among the various dimensionality reduction techniques, autoencoders have garnered significant prominence owing
to their capacity for unsupervised feature learning through a compression -reconstruction objective [52]. Autoencoders
can capture complex nonlinear relationships  in high -dimensional data, which makes them particularly suitable for
processing rich semantic representations derived from transformer -based language models.  However, standard
feedforward autoencoders apply uniform transformations across the input space without a mechanism for adaptive and
selective feature filtering [53]. This limitation becomes pronounced when the input comprises dense and high-dimensional
embeddings that encapsulate heterogeneous and contextually rich semantic content, as is the case wi th Sentence-BERT
representations of customer reviews.
The autoencoder architecture employed in this study comprises two primary components: an encoder and a decoder.
The encoder maps the input data (N) into a compressed latent feature space  (Z). This transformation is achieved
through a learned weight matrix (W) and bias vector (b), followed by a non-linear activation function fenc , as in Equation
(1):

Z = fenc(WN + b)                                                                           (1)

Subsequently, the decoder uses the latent feature space to reconstruct the original input and generates the output (X̂)
is represented mathematically in Equation (2):

X̂ = fdec(W′ ⋅ Z + b′)                                                                       (2)

where W′ represents the decoder’s weight matrix and b′ as the bias vector, while the activation function fdec responsible
for transforming the latent representation  Z into a reconstructed input space . The entire architecture is optimized by
minimizing the reconstruction loss, representing the error between the original input and the reconstructed output X̂. The
resulting compressed bottleneck representation constitutes the latent feature space used for subsequent dimensionality
reduction and clustering.

Fig. 2. Architecture of the proposed BIGA framework
The GRU -based Autoencoder employs a deep layered architecture, where the output of each hidden layer is
forwarded to the subsequent layer. The encoder component of the GRU -based Autoencoder employs a deep hierarchical
architecture with progressively dimini shing dimensionality, comprising three stacked GRU layers. Specifically, the
update and reset gates of the GRU perform a distinctly richer, more selective nonlinear transformation of the 768 -
dimensional input than the uniform transformations applied by sta ndard feedforward autoencoder layers. Batch
normalization is applied after each GRU layer to stabilize the training dynamics and mitigate the effects of internal

A Novel Deep Learning Framework for Customer Segmentation and Satisfaction Analysis in Tourism using
Multimodal User-generated Content
Volume 18 (2026), Issue 5 – Page 159
covariate shift. The output of the final GRU encoder layer is fed into a dense layer to produce a compressed representation,
called the feature space. The decoder consists of three GRU layers, each mirroring the encoder’s layer. Finally, a Time
Distributed Dense layer with an activation function is applied to reconstruct the original 768 -dimensional embedding.
The architecture of the GRU-based Autoencoder model for the latent dimension (n) is shown in Figure 2.
3.4. k-means Clustering
In this study, k-means clustering is applied to the low -dimensional latent representations generated by the GRU -
based autoencoder with multi -dimensional numerical ratings rather than to raw high -dimensional textual embeddings.
Prior research suggests that clustering perfo rmance and stability improve substantially when distance -based algorithms
are applied in compact latent spaces, where noise and sparsity are reduced [17,21,54]. The k -means clustering algorithm
was selected due to its wide adoption as a clu stering baseline for customer segmentation, and also due to its scalability
and computational efficiency [17,21,33,35].
4. Experimental Setup
This section provides a description of the dataset, the evaluation metrics used to evaluate the performance of the
model, a detailed overview of the hyperparameter tuning of the GRU -based Autoencoder model, and a n outline of the
state-of-the-art models used for comparison . All the experiments were implemented using Python 3.7 with Jupyter
Notebook running on an Intel Core Ultra 7 255H central processing unit, 32 GB random -access memory, with graphics
processing handled by an integrated Intel Arc graphics processor.
4.1. Dataset Description
We have used the TripAdvisor review ratings dataset [55]. It contains information about the customers' multi-criteria
ratings and text reviews  for the year 2012. The total number of reviews is 201,291, and the number of unique hotel IDs
is 3,547. The customers provided ratings on six different criteria, which are overall, cleanliness, value, location, room,
and sleep quality, on a scale of 1 to 5.
4.2. Evaluation Metrics
The proposed customer segmentation framework is validated using a clustering technique, and internal evaluation
metrics are employed to assess the clustering algorithm's performance and quantify the structural properties of the
resulting clusters. The quality of clustering results in an unsupervised customer segmentation can be assessed through
internal validity indices, as no ground -truth labels exist to serve as external reference points. The adoption of internal
evaluation metrics in unsupervised customer segmentatio n is widely accepted in the literature [17,5 4,56-57]. The
following internal evaluation measures are used in our study:
A. Silhouette Coefficient
The Silhouette analysis determines how well the features  are grouped by comparing the similarity of an object to
points within a cluster against its similarity to points in  other clusters [5 8]. The value of the Silhouette score can vary
between -1 and +1, with higher values meaning the object fits well in its cluster and poorly in others [5 9].
The Silhouette Coefficient is calculated using the following Equation (3):

𝑆 =
1
𝑁𝐶 ∑ 1 𝑛𝑖𝑖 ∑ 𝑏(𝑥)−𝑎(𝑥) 𝑚𝑎𝑥[𝑏(𝑥),𝑎(𝑥)]𝑥∈𝑐𝑖                                                                            (3)

Here, 𝑎 represents the intra-cluster distance, while  𝑏  denotes the inter-cluster distance. 𝑁𝐶 is the total number of
clusters, 𝑐𝑖 indicates the centroid, and 𝑛𝑖 shows the number of points in that cluster.
B. Davies–Bouldin Index
The Davies–Bouldin (DB) Index measures the performance of clusters by evaluating the similarity score of each
cluster relative to  its most similar cluster . The similarity score is calculated by comparing within-cluster distances to
between-cluster distances [60]. A lower DB Index value corresponds to well -separated and compact clusters, whereas a
higher value suggests overlapping or poorly separated clusters  [61]. The DB Index is calculated using the following
Equation (4):

𝐷𝐵 𝐼𝑛𝑑𝑒𝑥 =
1
𝑘 ∑ 𝑚𝑎𝑥 𝑖 ≠ 𝑗 𝑘 𝑖=1 ( 𝜎𝑖 +𝜎𝑗 𝑑 (𝐶𝑖,𝐶𝑗 )                                                                (4)

Here, 𝑘 denotes the total clusters,  𝜎 measures the spread of points , and (𝐶𝑖, 𝐶𝑗) represents the distance between the
cluster centroids.

A Novel Deep Learning Framework for Customer Segmentation and Satisfaction Analysis in Tourism using
Multimodal User-generated Content
Volume 18 (2026), Issue 5 – Page 160
4.3. Different Parameters to Optimize the GRU-based Autoencoder Model
This section describes the various hyperparameters in subsection 4.3(A) and details the tuning of these parameters
in subsection 4.3(B).
A. Hyperparameters Description
The role of hyperparameters in neural networks is crucial for training the model and significantly impacts the results.
Before the training, the model architecture, its parameters, and hyperparameters must be configured to ensure optimal
performance. The data were partitioned into three subsets: training, validation, and testing. The training set enabled model
fitting, while the validation set was used to optimize the hyperparameters . To enhance model effectiveness, various
architectural and training -related parameters were systematically explored. These include the number of hidden layers,
the number of GRU units per layer, and the selection of the loss function. Additionally, key training variables such as
activation function, learning rate, and batch size were optimized through experimentation.

• Layer Dimension: This refers to the number of neurons or units in each layer of the neural network to determine
the complexity of the model [62]. More neurons can capture hidden patterns, but this can increase the problem
of overfitting in the data.
• Batch Size: This represents the number of data points used in each training step [63]. Larger batch sizes speed
up the training, and smaller batch sizes enable the model to update and explore data thoroughly.
• Number of Layers: This indicates the number of layers stacked upon each other. More layers help the model
learn from abstract features in the data, but also require high computational resources.
• Learning Rate: The learning rate defines the step size for the optimizer and determines the number of parameters
updated during each iteration [6 4]. A high learning rate may cause the model to  overshoot the optimal point,
whereas a lower learning rate facilitates more stable and gradual convergence.
• Activation Function: In the neural network, activation functions provide a non-linear transformation that allows
the model to learn intricate data patterns [65].
• Loss Function: The loss function quantifies the difference between the model’s predicted outputs and the true
values during training [66,67].
B. Hyperparameters Tuning
The criteria defined for hyperparameter tuning in our research focus on achieving stable convergence. During the
optimization phase, training performance was closely monitored by tracking the loss and relevant performance metrics.
Based on these observations, hyperparameters were iteratively adjusted until convergence was attained.
The GRU -based Autoencoder was implemented and trained using Keras with a TensorFlow backend and GPU
acceleration. The training process was carried out with a batch size of 256  for 100 epochs. The activation function used
in the bottleneck layer is a linear function  to preserve the structure of the latent feature space. In addition, the final layer
of the decoder utilizes the sigmoid activation function to reconstruct the output . The model was trained across various
configurations to identify the optimal hyp erparameter values. The finalized set of tuned hyperparameters for the GRU -
based Autoencoder model is presented in Table 1.
Table 1. Optimal Hyperparameters of the GRU-based Autoencoder
Hyperparameter Optimal Values
GRU Layers 6
Dense Layers 2
Batch Normalization Layer 4
Epochs 100
Batch Size 256
Learning Rate 0.00001
Activation Function tanh
Optimizer Adam

The dimensions of the bottleneck, which represent the extracted features, are of particular interest in this study. To
explore their impact, we experimented with various bottleneck dimensions. To compare the performance of different
dimensionality reductio n settings, the reconstruction loss, measured using mean squared error , was tracked on  both
training and validation sets across latent dimensions of 10, 20, 30, 40, and 50. This analysis facilitated the identification
of the most effective configuration fo r the proposed model. The reconstruction loss curves corresponding to each
bottleneck dimension are presented in Figure 3.

A Novel Deep Learning Framework for Customer Segmentation and Satisfaction Analysis in Tourism using
Multimodal User-generated Content
Volume 18 (2026), Issue 5 – Page 161

(a)                                                                                               (b)

(c)                                                                                                    (d)

(e)
Fig. 3. Training and validation loss curves during hyperparameter optimi zation of the GRU -based Autoencoder model across different bottleneck
dimensions: (a) 10, (b) 20, (c) 30, (d) 40, and (e) 50
4.4. Baseline Methods
This section highlights the different models that were used in previous studies [17,4 3] to provide baseline
comparisons for assessing the  performance of our proposed BIGA framework. To ensure a fair comparison, Sentence -
BERT was applied to obtain embeddings across all baselines, which were then fine-tuned and optimized with comparable
effort.
A. Principal Component Analysis (PCA)
PCA is one of the widely recognized standard approaches for linear dimensionality reduction [68].  We obtained
contextual word embeddings using BERT and then applied PCA to transform the high-dimensional vectors into a lower-
dimensional feature space . PCA accomplishes this by constructing linear combinations of the original features that
preserve the maximum variance in the data [69]. It is applied to reduce dimensionality to a specific number of components
or until a desired explained variance ratio is achieved before applying clustering or classification algorithms [70]. As one
of our baselines, we applied the Sentence-BERT embeddings + PCA + k-means on the dataset.
B. Uniform Manifold Approximation and Projection (UMAP)
UMAP is a non-linear dimensionality reduction technique [71] that operates on the principles of topology and graph-
based modelling.  It creates a high -dimensional graph representation and then learns a lower -dimensional layout that
maintains both local and global relationships [72]. UMAP is particularly effective in capturing both linear and non-linear
relationships [73] that linear methods may overlook. For the baselines, we  applied Sentence-BERT to obtain contextual
embeddings, followed by the UMAP feature reduction technique and the k-means clustering algorithm.
C. Autoencoder (AE)
AE is another state -of-the-art deep-learning-based dimensionality reduction technique that learns to map the input
data into a low-dimensional latent space and then reconstructs the original input from this compressed representation [74].
It is effective in preserving important information from high -dimensional data and is commonly used for anomaly
detection and data reconstruction (including denoising) tasks [44]. As one of the baselines, we utilize the encoder part of
the AE to transform Sentence-BERT embeddings into a latent representation, followed by k-means clustering. This can

A Novel Deep Learning Framework for Customer Segmentation and Satisfaction Analysis in Tourism using
Multimodal User-generated Content
Volume 18 (2026), Issue 5 – Page 162
be referred to as BERT + AE + k-means clustering.
5. Results and Discussion
This section presents the experimental evaluation conducted on the dataset to assess and compare the performance
of the proposed BIGA framework against state-of-the-art dimensionality reduction techniques. The experimental results
were discussed, along with their implications.
5.1. Performance Comparison of Our Proposed BIGA Model vs. Baseline Models
This section examines the effectiveness of the BIGA framework against the other baseline models that deploy
different dimensionality reduction techniques. The latent features were obtained from the text reviews using PCA, UMAP,
AE, and the BIGA framework. The robustness of the BIGA framework was evaluated across latent feature dimensions of
10, 20, 30, 40, and 50, which were extracted across all models and then assessed further using the Silhouette Coefficient
and DB Index as the evaluation metrics after clustering.
The dimensions extracted by employing different dimensionality reduction techniques for the baseline and BIGA
framework were normalized using min -max scaling before clustering on these dimensions. The min -max scaling was
applied for normalization, calculated using the following Equation (5):

MinMax_Score =
x−min(x)
max(x)−min(x)                                                                   (5)

(a)                                                                                                        (b)

(c)                                                                                                    (d)

(e)
Fig. 4. Average Silhouette Coefficient for the BIGA, AE, UMAP, and PCA across the following reduced dimensions: (a) 10, (b) 20, (c) 30, (d) 40, and
(e) 50
Following normalization, k-means clustering was applied to the extracted dimensions and the multi-criteria ratings,
and the performance was evaluated using the average Silhouette Coefficient for each model across the aforementioned
dimensionalities. These results are illustrated in Figure 4 and demonstrate that the BIGA framework consistently achieves
superior performance across all dimensions and indicates its effectiveness in capturing meaningful latent contextual

A Novel Deep Learning Framework for Customer Segmentation and Satisfaction Analysis in Tourism using
Multimodal User-generated Content
Volume 18 (2026), Issue 5 – Page 163
representations from the text. In contrast, PCA exhibits the lowest Silhouette Coefficient, suggesting its limited
effectiveness in extracting relevant latent features, resulting in poor quality clusters. Based on the observed Silhouette
Coefficient, the performance ranking is as follows: BIGA > AE > UMAP > PCA.
We also considered the average DB Index on the clustering results obtained to further evaluate clustering quality for
all models across different dimensions, which are presented in Figure 5. The DB Index evaluates clustering performance,
with lower values indicating better separation betwee n clusters and reduced intra -cluster variance. The results indicate
that the BIGA framework consistently attains the lowest DB Index across all tested latent dimensions , which indicates
superior performance in generating well-separated and tightly grouped clusters. In contrast, PCA records the highest DB
Index values, further reinforcing its weaker clustering capability. These findings align with the Silhouette Coefficient
results and collectively highlight BIGA’s effectiveness in learning discriminative and structure -preserving feature
representations.

(a)                                                                                                        (b)

         (c)                                                                                                           (d)

(e)
Fig. 5. Average DB Index for the PCA, UMAP, AE, and BIGA across the following dimensions: (a) 10, (b) 20, (c) 30, (d) 40, and (e) 50
5.2. Cluster Analysis
Cluster analysis was performed to segment customers based on various  dimensions of customer experience. The
proposed BIGA framework requires determining the optimal latent bottleneck dimensions of the GRU-based Autoencoder
and the optimal number of clusters k for identifying customer segments.
To identify the optimal number of compressed dimensions, five latent dimensions were evaluated: 10, 20, 30, 40,
and 50. The clustering quality is assessed using the Silhouette Coefficient (higher is better) and the DB Index (lower is
better). The 40 -dimensional configuration achieved the h ighest Silhouette Coefficient, the lowest DB Index, and the
highest average Silhouette Coefficient across all tested values of k, outperforming all other dimensions.
The optimal number of clusters, k, was determined using the elbow method, the Silhouette Coefficient, and the DB
Index, as shown in Figure 6 . The elbow curve reveals an inflection point at k = 4 and indicates that additional clusters
beyond 4 diminish improvements in intra-cluster compactness. The Silhouette Coefficient was computed, and at k=2 and
k=3 it yielded a high Silhouette score but lacks the granularity necessary for actionable management insights. At k=4, the

A Novel Deep Learning Framework for Customer Segmentation and Satisfaction Analysis in Tourism using
Multimodal User-generated Content
Volume 18 (2026), Issue 5 – Page 164
Silhouette Coefficient represents the optimal balance between cluster cohesion and granularity of segmentation. The
lower DB Index value at k=4 further indicates cluster separation.  Based on this analysis, four clusters were identified as
the most appropriate.

Fig. 6. Convergence of Elbow Method, Silhouette Coefficient, and Davies–Bouldin Index
In the context of the tourism industry, customer satisfaction is shaped by a variety of key factors , which include
cleanliness, location, value for money, room quality, sleep quality, and the overall guest experience. These variables
capture guests' expectations and experiences during their stay, which are essential for understanding satisfaction levels
and improving service strategies.
To characterize the identified clusters, centroids were calculated based on multi -criteria rating aspects, as these
features encapsulate critical aspects of customer satisfaction in tourism . The centroids reflect the average rating for each
aspect within the identified clusters, which highlight different segments of customers according to their preferences and
experiences. The result of the cluster analysis based on customer rating dimensions is illustrated in Figure 7.

Fig. 7. Cluster centroids across key dimensions of customer satisfaction for ratings only
5.3. Statistical Validation of Inter-cluster Differences
To statistically substantiate the qualitative interpretations of the identified customer segments, quantitative
characterization of the inter -cluster differences was conducted across all rating dimensions —overall satisfaction,
cleanliness, value, location, room quality, and sleep quality. The analysis includes three statistical procedures:

• The Kruskal–Wallis non-parametric test to assess the overall significance of inter-cluster differences [75].
• Dunn's post-hoc test with Bonferroni correction for pairwise cluster comparisons [76].
• Cohen's d and eta -squared (η²) effect size measures to quantify the practical magnitude of the observed
differences.
A. Kruskal–Wallis Test

A Novel Deep Learning Framework for Customer Segmentation and Satisfaction Analysis in Tourism using
Multimodal User-generated Content
Volume 18 (2026), Issue 5 – Page 165
The Kruskal–Wallis test was selected as the appropriate statistical method for comparing rating distributions across
the four identified clusters, consistent with its use for ordinal data analysis where normality assumptions are not
guaranteed [77]. This approach is aligned with recent hospitality research employing Kruskal –Wallis tests to validate
differences in customer rating profiles across hotel clusters [75].
The descriptive statistics for each cluster across all rating dimensions are presented in Table 2. The Kruskal–Wallis
test revealed statistically highly significant differences across the four customer segments for all six rating dimensions,
as presented in Table 3. The H -statistics with p < 0.001 confirm that the identified clusters differ significantly in their
rating profiles across all evaluated dimensions. Effect sizes were interpreted with thresholds of η² ≥ 0.01 (small), ≥ 0.06
(medium), and ≥ 0.14 ( large) following Cohen [78]. The eta-squared (η²) values computed from the Kruskal –Wallis H-
statistic indicate large effect sizes for five of the six dimensions —overall satisfaction, cleanliness, rooms, sleep quality,
and value —and a medium effect size for location. These effect sizes indicate that cluster membership explains a
substantial and practically meaningful proportion of the variance in customer ratings.
Table 2. Descriptive statistics of cluster rating profiles (Mean ±  SD, Original 1–5 Scale)
Ratings Dimension C0 (n=106,762) C1 (n=19,611) C2 (n=12,728) C3 (n=62,190)
Overall 4.060 ±  1.068 2.557 ±  0.911 4.118 ±  1.025 4.530 ±  0.568
Cleanliness 4.285 ±  1.003 2.977 ±  1.077 4.338 ±  0.959 4.696 ±  0.510
Value 3.982 ±  1.091 2.594 ±  0.994 4.038 ±  1.040 4.416 ±  0.690
Location 4.465 ±  0.838 3.736 ±  1.079 4.484 ±  0.814 4.696 ±  0.578
Rooms 4.034 ±  1.061 2.612 ±  0.911 4.090 ±  1.010 4.479 ±  0.638
Sleep Quality 4.142 ±  1.075 2.739 ±  1.057 4.200 ±  1.019 4.577 ±  0.620
Table 3. Kruskal–Wallis test results and effect sizes
Ratings Dimension H-statistic p-value η² Effect Magnitude
Overall 43,749.84 < 0.001 0.2173 Large
Cleanliness 39,521.66 < 0.001 0.1963 Large
Value 35,614.70 < 0.001 0.1769 Large
Location 18,237.28 < 0.001 0.0906 Medium
Rooms 40,009.87 < 0.001 0.1988 Large
Sleep Quality 38,226.92 < 0.001 0.1899 Large

B. Dunn's Post-hoc Test
Dunn’s post -hoc test with Bonferroni correction [78,79] was employed for all six ratings for pairwise cluster
comparisons. The results  show that 23 out of 24 pairwise comparisons are statistically significant at p < 0.001 after
Bonferroni correction. The non-significant comparison between C0 and C2 on the location dimension (adjusted p = 0.2299)
indicates that these two segments perceive the location of the hotel similarly.
C. Cohen's d Effect Size Analysis
The sample size of our dataset is large (N = 201,291), and to assess the practical meaningfulness, statistical
significance alone is insufficient.  To quantify the practical magnitude of inter -cluster differences, effect size was
computed. The interpretation thresholds for Cohen's d are: Negligible < 0.2, Small 0.2 –0.5, Medium 0.5–0.8, Large 0.8–
1.2, Very Large > 1.2. The results are indicated in Table 4.
Table 4. Cohen's d Effect Sizes for Pairwise Cluster Comparisons
Cluster Pair Overall Cleanliness Value Location Rooms Sleep Quality Avg d Magnitude
C0 vs C1 1.438 1.288 1.289 0.828 1.367 1.309 1.253 Large
C0 vs C2 0.054 0.053 0.052 0.023 0.053 0.054 0.048 Negligible
C0 vs C3 0.512 0.481 0.451 0.307 0.480 0.466 0.45 Small
C1 vs C2 1.631 1.318 1.426 0.760 1.554 1.402 1.348 Large
C1 vs C3 2.961 2.492 2.354 1.315 2.618 2.457 2.366 Very Large
C2 vs C3 0.616 0.587 0.496 0.340 0.544 0.536 0.520 Medium

The effect size analysis reveals important findings. First, the C1 and C3 segments represent distinct customer
experiences across all rating dimensions. Second, the C1 segment is statistically and practically distinct from all other

A Novel Deep Learning Framework for Customer Segmentation and Satisfaction Analysis in Tourism using
Multimodal User-generated Content
Volume 18 (2026), Issue 5 – Page 166
segments across all rating dimensions. Third, the comparison between C3 and C2 shows moderate but meaningful
differences. This suggests that these clusters vary mainly in satisfaction level rather than in the overall pattern  of their
satisfaction.
The statistical results suggest that clusters C0 and C2 are similar when considering numerical ratings alone. This is
evidenced by the negligible Cohen’s d effect size (d = 0.048) and the non-significant Dunn’s post-hoc test for the location
dimension between these clusters. The findings provide empirical support for the BIGA framework's ability to identify
nuanced and behaviorally meaningful segments that would remain hidden in rating-only or text-only approaches.
5.4. Implications
The study significantly contributes to the theoretical and practical perspectives of market segmentation. Over the
past decade, the emergence of rapid technological advancements and the digitalization of resources have increasingly
garnered widespread attention for customer profiling and personalized service delivery in the dynamic landscape of the
tourism industry. The results of our study demonstrate that both online reviews and multi -criteria ratings can serve as a
valuable instrument in shaping the decision-making journey of the modern traveler. Learning-based techniques provide a
robust foundation for analyzing big data of the traveler -generated online reviews and multi -criteria ratings on social
networking platforms.
Despite the unprecedented growth of UGC in recent years, UGC-based market research remains in its nascent stage,
underscoring a critical need for comprehensive theoretical frameworks to guide future investigations. Our research study
provides a feasible an d impactful contribution toward UGC -based market segmentation. Most of the previous research
has been confined to specific industries and has largely been constrained by conventional machine learning algorithms
and basic clustering techniques [15,18,33,80]. Our approach introduces a broader and more adaptable theoretical model.
The proposed BIGA framework may not be flawless, but it serves as a constructive reference point for advancing
methodological and theoretical development in this emerging field.
Second, in terms of methodology, to the best of our knowledge, our study is the first to integrate Sentence-BERT
with a GRU-based autoencoder for analyzing textual online reviews and extracting contextual information and gaining a
deeper understanding of customer preferences. Previous researchers have attempted to use different word embeddings,
such as Word2Vec, TF-IDF, and even BERT, to analyze textual UGC [17, 43,81], and have also employed autoencoders
for extracting latent features in UGC [ 82,83]. These approaches often fail to adequately capture the context -sensitive
nature of natural language. Our approach offers new theoretical perspectives to derive the evolving customer preferences
and sentiments from the unstructured textual data. This appr oach enables the extraction of relevant semantic features
without degradation of important information and context to group heterogeneous customers into well-defined and
homogeneous clusters. Contributing to segmentation theory and expanding the scope for personalization and targeted
marketing strategies, the proposed BIGA framework empowers UGC-based segmentation by incorporating multiple facets,
including online reviews and multi-criteria ratings of UGC for strategic marketing and customer personalization.
The research findings of our study offer valuable practical implications for academic researchers and industry
practitioners within the tourism sector. First, our research introduces a practical method for utilizing traveler -generated
content to perform market  segmentation within the tourism sector. As users increasingly take to social media platforms
to share detailed reviews and personal experiences [ 84], their vocal digital presence has transformed user -generated
content into a highly reliable and authentic source of consumer insights [85]. The rapid growth of large-scale user opinions,
often unstructured and noisy, frequently prevents enterprises from using this data effectively for marketing purposes. The
success of a company lies in its capability to satisfy customers’ preferences [ 86]. Amidst the vast volume of available
multimodal data, our proposed framework would offer a compelling motivation for enterprises to explore and implement
UGC for efficient large-scale market segmentation and also serve as a reliable reference for enterprises’ strategic decision-
making within the dynamic tourism landscape, compared to traditional approaches of market segmentation.
Moreover, the findings from our data -driven market segmentation, which utilizes multimodal travelers’ opinions,
would also help enterprises achieve their primary objective: profitability. Our study provides a valuable tool for aligning
services with the dynamic needs of customers. Furthermore, our segmentation approach not only facilitates acquiring new
customers but also improves the retention of existing ones. Businesses can develop their targeted marketing strategies by
identifying distinct customer segm ents and aligning with their preferences, thereby reducing advertising costs. The
proposed method is designed to provide actionable insights that can enhance service quality and guest satisfaction by
developing targeted marketing promotions and campaigns using online reviews and mult i-criteria ratings together.
6. Conclusion
Our research study proposes a novel framework for customer segmentation using textual reviews and multi -criteria
ratings to enhance customer satisfaction in the tourism industry. The hybrid dual -modality framework utilizes Sentence-
BERT with a GRU -based Autoencoder to capture the semantic and contextualized information while preserving long -
term contextual dependencies without degradation of important information from online reviews. The experimental
results demonstrated that the proposed BIGA framework achieved a high Silhouette Coefficient and a low DB Index,
which showcases its superiority over the different state-of-the-art approaches and other traditional approaches, which are
either based on ratings data or text data, effectively capturing the multi -criteria aspects of customer feedback. The

A Novel Deep Learning Framework for Customer Segmentation and Satisfaction Analysis in Tourism using
Multimodal User-generated Content
Volume 18 (2026), Issue 5 – Page 167
identified distinct customer cluster segments based on real customer experiences provide practical insights for marketers
to tailor marketing strategies that strategically adapt to evolving consumer preferences.
Despite the valuable contribution of our research study, certain limitations need to be acknowledged. First, our
framework successfully integrates textual reviews and multi -criteria numerical ratings; however, it does not incorporate
several other potentially significant variables. Attributes such as user demographics, booking patterns, frequency of visits,
and external contextual factors—like seasonality, regional events, or macroeconomic conditions—are excluded. This may
reduce the effectiveness in captur ing intricate customer behaviors required to define clear segments.  Second, the
evaluation framework employed in our study adopts internal evaluation metrics for unsupervised UGC -based customer
segmentation. Future research can also explore expert labeling or deployment-based evaluation frameworks to provide
external validation of the identified customer segments in real-world settings. Third, online review platforms often attract
users at the extremes of satisfaction—those who are highly pleased or deeply dissatisfied [87], and sometimes companies
publish fabricated reviews to enhance the perceived quality  and attract potential customers [8 8]. This tendency may
overlook the insights of moderately satisfied customers, whose insights may be critical for a balanced understanding of
customer behavior. This skewed representation may introduce potential biases that may constrain the model’s ability  to
detect meaningful and representative customer patterns. Despite these imperfections, the authentic voice of customers
remains an invaluable source of insights that should not be overlooked. Future studies could explore the steps to identify
fake review s [89] and implement methods to rebalance skewed datasets using sampling or weighting mechanisms to
ensure the full spectrum of customer experiences in segmentation or analysis models. Lastly, the computational demand
of the BIGA framework presents a practical challenge. The training and fine -tuning of deep learning models for big
datasets demand significant computational resources, such as high-performance GPUs and extended processing times.
Future research can be conducted in the following ways. First, to deliver more personalized suggestions aligned with
diverse user preferences, a hybrid comprehensive framework could be developed by incorporating additional behavioral,
personal, and other important dimensions along with performance measures of  the tourism industry. Also, our study
employed k-means clustering to identify distinct segments of customers. Researchers have attempted to use alternative
clustering techniques, such as hierarchical c lustering [90], density-based clustering [16], and other deep learning - based
clustering techniques [ 91] for the segmentation process. Therefore, it opens future research avenues for incorporating
advanced technologies such as deep learning models, hierarchical clustering, and density -based clustering techniques to
empower businesses to understand users’ interests and facilitate efficient resource allocation. Future research should also
prioritize the development of a comprehensive predictive model for fore casting booking patterns to optimize pricing
strategies, promotional campaigns, and resource allocation for competitive advantage.
Moreover, with the accelerated deployment of AI-based solutions, a growing body of literature also underscores the
importance of explainable artificial intelligence (XAI) models to maintain transparency, accountability, and adaptability
in deep learning-based models [92,93]. This would not only foster trust in AI-driven systems but also provide actionable
insights about the customer navigational journey to cater to the needs more efficiently. This emerging research frontier,
leveraging UGC for the customer segmentation process, must also address multifaceted challenges to better understand
customer preferences and enhance user experience, thereby enhancing the global tourism sector .

All the Declarations and Statements
Author Contributions Statement
Gaganmeet Kaur Awal: Conceptualization, Methodology, Framework Design, Analysis, Writing – Review & Editing, and
Supervision
Ujjwal Tehlan: Conceptualization, Methodology, Implementation, Validation, Model Training,  and Writing – Original
Draft

All authors have read and agreed to the published version of the manuscript.

Conflict of Interest Statement
The authors declare no conflicts of interest.

Funding Declaration
This research received no external funding.

Data Availability Statement
This study analyzed a publicly available TripAdvisor review ratings dataset as cited in the paper [55].

Ethical Declarations
None

A Novel Deep Learning Framework for Customer Segmentation and Satisfaction Analysis in Tourism using
Multimodal User-generated Content
Volume 18 (2026), Issue 5 – Page 168

Acknowledgments
The authors would like to express their sincere gratitude to  the anonymous reviewers for their valuable suggestions and
recommendations, which helped in improving the quality of our manuscript.

Declaration of Generative AI in Scholarly Writing
The authors acknowledge the use of OpenAI GPT-4 solely for minor language refinement.

Abbreviations
The following abbreviations are used in this manuscript:

UGC - User-Generated Content
eWOM - Electronic Word of Mouth
BERT - Bidirectional Encoder Representations from Transformers
GRU - Gated Recurrent Unit
LSTM - Long Short-Term Memory
RNN - Recurrent Neural Network
DB Index - Davies–Bouldin Index
PCA - Principal Component Analysis
UMAP - Uniform Manifold Approximation and Projection
AE - Autoencoder
XAI - Explainable Artificial Intelligence

Appendix
None

References
[1] Aksoy, Lerzan, Sunmee  Choi, Tarik Dogru, Timothy Keiningham, Melanie Lorenz, Dan Rubin, and J. Bruce Tracey. "Global
trends in hospitality." Journal of Business Research 142 (2022): 957-973. DOI:10.1016/j.jbusres.2021.12.068
[2] Hwang, Yujong, and Jaeseok Jeong. "Electronic commerce and online consumer behavior research: A literature
review." Information Development 32, no. 3 (2016): 377-388. DOI:10.1177/0266666914551071
[3] Secchi, Enrico, Aleda Roth, and Rohit Verma. "The impact of service improvisation competence on customer satisfaction:
evidence from the hospitality industry."  Production and Operations Management  28, no. 6 (2019): 1329 -1346.
DOI:10.1111/poms.12969
[4] Johnson, Michael D., Georg Nader, and Claes Fornell. "Expectations, perceived performance, and customer satisfaction for a
complex service: The case of bank loans."  Journal of Economic Psychology  17, no. 2 (1996): 163 -182. DOI:10.1016/0167-
4870(96)00002-5
[5] Rodrigues, Gourab Nicholas, MD Nazmul Hossain Mir, MD Shahriar Mahmud Bhuiyan, M. D. A. L. Rafi, ASM Morshedul
Hoque, Jannatul Maua, and M. F. Mridha. "NLP -driven customer segmentation: A comprehensive review of methods and
applications in personalized marketing." Data Science and Management (2025). DOI:10.1016/j.dsm.2025.09.002
[6] Masoud, Rawan, and Sarah Basahel. "The effects of digital transformation on firm performance: The role of customer experience
and IT innovation." Digital 3, no. 2 (2023): 109-126. DOI:10.3390/digital3020008
[7] Grandhi, Balakrishna, Nitin Patwa, and Kashaf Saleem. "Data -driven marketing for growth and profitability."  EuroMed Journal
of Business 16, no. 4 (2021): 381-398. DOI:10.1108/EMJB-09-2018-0054
[8] Hasan, Reduanul. "Enhancing market competitiveness through AI -powered SEO and digital marketing strategies in e -
commerce." ASRC Procedia: Global Perspectives in Science and Scholarship 1, no. 01 (2025): 465-500. DOI:10.63125/31tpjc54
[9] Camilleri, Mark Anthony. "Market segmentation, targeting and positioning." In  Travel marketing, tourism economics and the
airline product: An introduction to theory and practice, pp. 69 -83. Cham: Springer International Publishing, 2017.
DOI:10.1007/978-3-319-49849-2_4
[10] Ukpabi, D. C., & Karjaluoto, H. (2017). Consumers’ acceptance of information and communications technology in tourism: A
review. Telematics and Informatics, 34(5), 618-644. DOI:10.1016/j.tele.2016.12.002
[11] Khan, Aasif Mohammad, Umer Yousuf Parray , Fayaz Ahmad Loan, and Shahid Rashid Parray. "Exploring digital voices to
evaluate user perception, satisfaction and service quality in libraries." Performance Measurement and Metrics 25, no. 3-4 (2024):
162-180. DOI:10.1108/PMM-04-2024-0021
[12] Liu, Xue, Ning Zhang, and Xiaoling Hao. "A Strategic model for service-oriented enterprises based on online reviews: the research
of budget hotel chains in China." Information Technology and Management 26, no. 3 (2025): 361-378. DOI:10.1007/s10799-024-
00417-2
[13] Jiang, Xiaoyan, Jie Lin, Chao Wang, and Lixin Zhou. "Seize market opportunities: market segmentation, profile and monitoring
through user-generated content." Kybernetes 53, no. 10 (2024): 3061-3086. https://doi.org/10.1108/K-12-2022-1721
[14] Oh, Soyoung, Honggeun Ji, Jina Kim, Eunil Park, and Angel P. del Pobil. "Deep learning model based on expectation-confirmation
theory to predict customer satisfaction in hospitality service."  Information Technology & Tourism  24, no. 1 (2022): 109 -126.
DOI:10.1007/s40558-022-00222-z

A Novel Deep Learning Framework for Customer Segmentation and Satisfaction Analysis in Tourism using
Multimodal User-generated Content
Volume 18 (2026), Issue 5 – Page 169
[15] Benbrahim Ansari, Oussama. "Geo -marketing segmentation with deep learning."  Businesses 1, no. 1 (2021): 51 -71.
DOI:10.3390/businesses1010005
[16] Ferro-Díez, Luis E., Norha M. Villegas, Javier Díaz -Cely, and Sebastián G. Acosta. "Geo -spatial market segmentation &
characterization exploiting user generated text through transformers & density -based clustering." IEEE Access 9 (2021): 55698-
55713. DOI:10.1109/ACCESS.2021.3071620
[17] Alkhayrat, Maha, Mohamad Aljnidi, and Kadan Aljoumaa. "A comparative dimensionality reduction study in telecom customer
segmentation using deep learning and PCA." Journal of Big Data 7, no. 1 (2020): 9. DOI:10.1186/s40537-020-0286-0
[18] Alsayat, Ahmed. "Customer decision-making analysis based on big social data using machine learning: a case study of hotels in
Mecca." Neural Computing and Applications 35, no. 6 (2023): 4701-4722. DOI:10.1007/s00521-022-07992-x
[19] Nilashi, Mehrbakhsh, Sarminah Samad, Behrouz Minaei-Bidgoli, Fahad Ghabban, and Eko Supriyanto. "Online reviews analysis
for customer segmentation through dimensionality reduction and deep learning techniques."  Arabian Journal for Science and
Engineering 46, no. 9 (2021): 8697-8709. DOI:10.1007/s13369-021-05638-z
[20] Nilashi, Mehrbakhsh, Hossein Ahmadi, Goli Arji, Khalaf Okab Alsalem, Sarminah Samad, Fahad Ghabban, Ahmed Omar
Alzahrani, Ali Ahani, and Ala Abdulsalam Alarood. "Big social data and customer decision making in vegetarian restaurants: A
combined machine lea rning method."  Journal of Retailing and Consumer Services  62 (2021): 102630.
DOI:10.1016/j.jretconser.2021.102630
[21] Nilashi, Mehrbakhsh, Behrouz Minaei-Bidgoli, Mesfer Alrizq, Abdullah Alghamdi, Abdulaziz A. Alsulami, Sarminah Samad, and
Saidatulakmal Mohd. "An analytical approach for big social data analysis for customer decision -making in eco -friendly
hotels." Expert Systems with Applications 186 (2021): 115722. DOI:10.1016/j.eswa.2021.115722
[22] Ahani, Ali, Mehrbakhsh Nilashi, Elaheh Yadegaridehkordi, Louis Sanzogni, A. Rashid Tarik, Kathy Knox, Sarminah Samad, and
Othman Ibrahim. "Revealing customers’ satisfaction and preferences through online review analysis: The case of Canary Islands
hotels." Journal of Retailing and Consumer Services 51 (2019): 331-343. DOI:10.1016/j.jretconser.2019.06.014
[23] Martinez-Torres, Maria del Rocío, and Sergio L. Toral. "A machine learning approach for the identification of the deceptive
reviews in the hospitality sector using unique attributes and sentiment orientation."  Tourism Management 75 (2019): 393 -403.
DOI:10.1016/j.tourman.2019.06.003
[24] Alshattnawi, Sawsan, Amani Shatnawi, Anas MR AlSobeh, and Aws A. Magableh. "Beyond word -based model embeddings:
Contextualized representations for enhanced social media spam detection."  Applied Sciences  14, no. 6 (2024): 2254.
DOI:10.3390/app14062254
[25] Naseem, Usman, Imran Razzak, Shah Khalid Khan, and Mukesh Prasad. "A comprehensive survey on word representation models:
From classical to state -of-the-art word representation language models."  Transactions on Asian and Low -Resource Language
Information Processing 20, no. 5 (2021): 1-35. DOI:10.1145/3434237
[26] Devlin, Jacob, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. "Bert: Pre-training of deep bidirectional transformers for
language understanding." In  Proceedings of the 2019 conference of the North American chapter of the association for
computational linguistics: human language technologies, volume 1 (long and short papers), pp. 4171 -4186. 2019.
DOI:10.18653/v1/N19-1423
[27] Dey, Rahul, and Fathi M. Salem. "Gate-variants of gated recurrent unit (GRU) neural networks." In 2017 IEEE 60th international
Midwest symposium on circuits and systems (MWSCAS), pp. 1597-1600. IEEE, 2017. DOI:10.1109/MWSCAS.2017.8053243
[28] Khan, Mohib Ullah, Abdul Rehman Javed, Mansoor Ihsan, and Usman Tariq. "A novel category detection of social media reviews
in the restaurant industry." Multimedia Systems 29, no. 3 (2023): 1825-1838. https://doi.org/10.1007/s00530-020-00704-2
[29] Kokab, Sayyida Tabinda, Sohail Asghar, and Shehneela Naz. "Transformer-based deep learning models for the sentiment analysis
of social media data." Array 14 (2022): 100157. DOI:10.1016/j.array.2022.100157
[30] Yi, Rongli, and Wenxin Hu. "Pre-trained BERT-GRU model for relation extraction." In Proceedings of the 2019 8th international
conference on computing and pattern recognition, pp. 453-457. 2019. DOI:10.1145/3373509.3373533
[31] Ma, Kai, Yongjian Tan, Miao Tian, Xuejing Xie, Qinjun Qiu, Sanfeng Li, and Xin Wang. "Extraction of temporal information
from social media messages using the BERT model." Earth Science Informatics 15, no. 1 (2022): 573-584. DOI:10.1007/s12145-
021-00756-6
[32] Pandey, Shweta, Neeraj Pandey, and Deepak Chawla. "Market segmentation based on customer experience dimensions extracted
from online reviews using data mining." Journal of Consumer Marketing 40, no. 7 (2023): 854-868. DOI:10.1108/JCM-10-2022-
5654
[33] Alghamdi, Abdullah. "A hybrid method for customer segmentation in Saudi Arabia restaurants using clustering, neural networks
and optimization learning techniques."  Arabian Journal for Science and Engineering  48, no. 2 (2023): 2021 -2039.
DOI:10.1007/s13369-022-07091-y
[34] Morritt, Ron, and Art Weinstein. “Segmentation strategies for hospitality managers: Target marketing for competitive advantage.”
Routledge, 2012.DOI:10.4324/9780203050095
[35] Abdi, Farshid, and Shaghayegh Abolmakarem. "Customer Behavior Mining Framework (CBMF) using clustering and
classification techniques." Journal of Industrial Engineering International 15, no. Suppl 1 (2019): 1-18. DOI:10.1007/s40092-018-
0285-3
[36] George, Richard. "Market segmentation, targeting, and positioning." In Marketing Tourism and Hospitality: Concepts and Cases,
pp. 199-221. Cham: Springer Nature Switzerland, 2025. DOI:10.1007/978-3-031-65983-6_7
[37] Dibb, Sally. "Changing times for social marketing segmentation." In  Segmentation in social marketing: process, methods and
application, pp. 41-59. Singapore: Springer Singapore, 2016. DOI:10.1007/978-981-10-1835-0_4
[38] Alves Gomes, Miguel, and Tobias Meisen. "A review on customer segmentation methods for personalized customer targeting in
e-commerce use cases." Information Systems and e-Business Management 21, no. 3 (2023): 527-570. DOI:10.1007/s10257-023-
00640-4
[39] Elwalda, Abdulaziz, and Kevin Lu. "The impact of online customer reviews (OCRs) on customers' purchase decisions: An
exploration of the main dimensions of OCRs."  Journal of Customer Behaviour  15, no. 2 (2016): 123 -152.
DOI:10.1362/147539216X14594362873695
[40] Sparks, Beverley A., and Victoria Browning. "The impact of online reviews on hotel booking intentions and perception of
trust." Tourism Management 32, no. 6 (2011): 1310-1323. DOI:10.1016/j.tourman.2010.12.011

A Novel Deep Learning Framework for Customer Segmentation and Satisfaction Analysis in Tourism using
Multimodal User-generated Content
Volume 18 (2026), Issue 5 – Page 170
[41] Zhang, Ziqiong, Qiang Ye, Rob Law, and Yijun Li. "The impact of e -word-of-mouth on the online popularity of restaurants: A
comparison of consumer reviews and editor reviews." International Journal of Hospitality Management 29, no. 4 (2010): 694-700.
DOI:10.1016/j.ijhm.2010.02.002
[42] Kiran, Prabha, and S. Vasantha. "Analysing the role of user generated content on consumer purchase intention in the new era o f
social media and big data."  Indian Journal of Science and Technology  9, no. 43 (2016): 1 -7. DOI:
10.17485/ijst/2016/v9i43/104754
[43] Hosseini, Soodeh, and Zahra Asghari Varzaneh. "Deep text clustering using stacked AutoEncoder."  Multimedia Tools and
Applications 81, no. 8 (2022): 10861-10881. DOI:10.1007/s11042-022-12155-0
[44] Che, Lei, Xiaoping Yang, and Liang Wang. "Text feature extraction based on stacked variational autoencoder." Microprocessors
and Microsystems 76 (2020): 103063. DOI: 10.1016/j.micpro.2020.103063
[45] Huang, Yang, Chiun-Hsun Chen, and Chi-Jui Huang. "Motor fault detection and feature extraction using RNN -based variational
autoencoder." IEEE Access 7 (2019): 139086-139096. DOI:10.1109/ACCESS.2019.2940769
[46] Abboush, Mohammad, Christoph Knieke, and Andreas Rausch. "GRU-based denoising autoencoder for detection and clustering
of unknown single and concurrent faults during system integration testing of automotive software systems."  Sensors 23, no. 14
(2023): 6606. DOI:10.3390/s23146606
[47] Zucchet, Nicolas, and Antonio Orvieto. "Recurrent neural networks: vanishing and exploding gradients are not the end of the
story." Advances in Neural Information Processing Systems 37 (2024): 139402-139443. DOI:10.52202/079017-4425
[48] Leng, Xue-Liang, Xiao-Ai Miao, and Tao Liu. "Using recurrent neural network structure with enhanced multi-head self-attention
for sentiment analysis." Multimedia Tools and Applications 80, no. 8 (2021): 12581-12600.  DOI:10.1007/s11042-020-10336-3
[49] Reimers, Nils, and Iryna Gurevych. "Sentence -bert: Sentence embeddings using siamese bert -networks." In Proceedings of the
2019 conference on empirical methods in natural language processing and the 9th international joint conference on natural
language processing (EMNLP-IJCNLP), pp. 3982-3992. 2019. DOI:10.18653/v1/D19-1410
[50] Goyal, Palash, Sumit Pandey, and Karan Jain. "Deep learning for natural language processing." New York: Apress (2018): 1624-
1633. DOI:10.1007/978-1-4842-3685-7
[51] Hussain, Shaik Arsh, Ravishta Kohli, Saniya Zahoor, and Shabir A. Sofi. "Transforming the GUI Landscape: Harnessing the
Power of MPNet base v2 Sentence Transformers."  Procedia Computer Science  259 (2025): 1809 -1816.
DOI:10.1016/j.procs.2025.04.136
[52] Berahmand, Kamal, Fatemeh Daneshfar, Elaheh Sadat Salehi, Y uefeng Li, and Y ue Xu. "Autoencoders and their applications in
machine learning: a survey." Artificial Intelligence Review 57, no. 2 (2024): 28. DOI:10.1007/s10462-023-10662-6
[53] Han, Kai, Yunhe Wang, Chao Zhang, Chao Li, and Chao Xu. "Autoencoder inspired unsupervised feature selection." In  2018
IEEE international conference on acoustics, speech and signal processing (ICASSP), pp. 2941 -2945. IEEE, 2018.
DOI:10.1109/ICASSP.2018.8462261
[54] Sinaga, Kristina P., and Miin -Shen Yang. "Unsupervised K-means clustering algorithm."  IEEE Access 8 (2020): 80716 -80727.
DOI:10.1109/ACCESS.2020.2988796
[55] Li, Jiwei, Myle Ott, and Claire Cardie. "Identifying manipulated offerings on review portals." In  Proceedings of the 2013
conference on empirical methods in natural language processing, pp. 1933-1942. 2013. DOI:10.18653/v1/D13-1199
[56] Wang, Zeya, and Chenglong Ye. "Deep Clustering Evaluation: How to Validate Internal Clustering Validation Measures." Journal
of the American Statistical Association just-accepted (2025): 1-23. https://doi.org/10.1080/01621459.2025.2592926
[57] Saraswat, Shweta, Vaibhav Agrohi, Mahesh Kumar, Monica Lamba, and Raminder Kaur. "Unveiling consumer segmentation:
Harnessing K-means clustering using elbow and silhouette for precise targeting." In International Conference on Computing and
Communication Networks, pp. 355-369. Singapore: Springer Nature Singapore, 2023. DOI:10.1007/978-981-97-0892-5_28
[58] Vardakas, Georgios, Ioannis Papakostas, and Aristidis Likas. "Deep clustering using the soft silhouette score: Towards compac t
and well-separated clusters." arXiv preprint arXiv:2402.00608 (2024). DOI:10.48550/arXiv.2402.00608
[59] Suraya, S., M. Sholeh, and U. Lestari. "Evaluation of data clustering accuracy using K-means algorithm." International Journal of
Multidisciplinary Approach Research and Science 2, no. 01 (2023): 385-396. DOI:10.59653/ijmars.v2i01.504
[60] Ikotun, Abiodun M., Faustin Habyarimana, and Absalom E. Ezugwu. "Performance Evaluation of Validity Indices on Evolutionary
K-Means Clustering." In  International Conference on Neural Information Processing, pp. 325 -341. Singapore: Springer Nature
Singapore, 2025. DOI:10.1007/978-981-95-4384-7_23
[61] Kumar, K. Mahesh, and A. Rama Mohan Reddy. "An efficient k -means clustering filtering algorithm using density based initial
cluster centers." Information Sciences 418 (2017): 286-301. DOI:10.1016/j.ins.2017.07.036
[62] Sheela, K. Gnana, and Subramaniam N. Deepa. "Review on methods to fix number of hidden neurons in neural
networks." Mathematical Problems in Engineering 2013, no. 1 (2013): 425740. DOI:10.1155/2013/425740
[63] Smith, Leslie N. "A disciplined approach to neural network hyper -parameters: Part 1--learning rate, batch size, momentum, and
weight decay." arXiv preprint arXiv:1803.09820 (2018). DOI:10.48550/arXiv.1803.09820
[64] Mehmood, Faisal, Shabir Ahmad, and Taeg Keun Whangbo. "An efficient optimization technique for training deep neural
networks." Mathematics 11, no. 6 (2023): 1360. DOI:10.3390/math11061360
[65] Nwankpa, Chigozie, Winifred Ijomah, Anthony Gachagan, and Stephen Marshall. "Activation functions: Comparison of trends in
practice and research for deep learning." arXiv preprint arXiv:1811.03378 (2018). DOI:10.48550/arXiv.1811.03378
[66] Tian, Yingjie, Duo Su, Stanislao Lauria, and Xiaohui Liu. "Recent advances on loss functions in deep learning for computer
vision." Neurocomputing 497 (2022): 129-158. DOI:10.1016/j.neucom.2022.04.127
[67] Hui, Like, and Mikhail Belkin. "Evaluation of neural architectures trained with square loss vs cross -entropy in classification
tasks." arXiv preprint arXiv:2006.07322 (2020). DOI:10.48550/arXiv.2006.07322
[68] Velliangiri, S., and S. J. P. C. S. Alagumuthukrishnan. "A review of dimensionality reduction techniques for efficient
computation." Procedia Computer Science 165 (2019): 104-111. DOI:10.1016/j.procs.2020.01.079
[69] Roy, Kowshik Sankar, Pritom Biswas Udas, Bashirul Alam, and Koushik Paul. "Unveiling hidden patterns: A deep learning
framework utilizing pca for fraudulent scheme detection in supply chain analytics." Int. J. Intell. Syst. Appl 17, no. 2 (2025): 14-
30. DOI: 10.5815/ijisa.2025.02.02
[70] Bharti, Kusum Kumari, and Pramod Kumar Singh. "Hybrid dimension reduction by integrating feature selection with feature
extraction method for text clustering."  Expert Systems with Applications  42, no. 6 (2015): 3105 -3114.

A Novel Deep Learning Framework for Customer Segmentation and Satisfaction Analysis in Tourism using
Multimodal User-generated Content
Volume 18 (2026), Issue 5 – Page 171
https://doi.org/10.1016/j.eswa.2014.11.038
[71] Oskolkov, Nikolay. "Dimensionality reduction: Overview, technical details, and some applications."  Applied Data Science in
Tourism: Interdisciplinary Approaches, Methodologies, and Applications (2022): 151-167. DOI:10.1007/978-3-030-88389-8_9
[72] McInnes, Leland, John Healy, and James Melville. "Umap: Uniform manifold approximation and projection for dimension
reduction." arXiv preprint arXiv:1802.03426 (2018). DOI:10.48550/arXiv.1802.03426
[73] Allaoui, Mebarka, Mohammed Lamine Kherfi, and Abdelhakim Cheriet. "Considerably improving clustering algorithms using
UMAP dimensionality reduction technique: a comparative study." In International conference on image and signal processing, pp.
317-325. Cham: Springer International Publishing, 2020. DOI:10.1007/978-3-030-51935-3_34
[74] Yun, Hye Sun, Ariungerel Jargal, Chang Min Hyun, and Jin Keun Seo. "Nonlinear Representation and Dimensionality Reduction."
In Deep Learning and Medical Applications, pp. 1 -49. Singapore: Springer Nature Singapore, 2023.  DOI:10.1007/978-981-99-
1839-3_1
[75] Messias, Ana, Gilberto Rosa, Pedro Couto, Vítor Rodrigues, Luís M. Silva, and Jorge Marques. "A new hotel classification model
combining guest reviews with official hotel classification systems: Bridging expert and consumer ratings."  Tourism and
Hospitality Research (2025): 14673584251379305. DOI:10.1177/14673584251379305
[76] Vagts, Christen, Christian Ascoli, Dustin R. Fraidenburg, Robert P. Baughman, Yue Huang, Russell Edafetanure -Ibeh, Samreen
Ahmed et al. "Unsupervised clustering reveals sarcoidosis phenotypes marked by a reduction in lymphocytes relate to increased
inflammatory activity on 18FDG-PET/CT." Frontiers in Medicine 8 (2021): 595077. DOI: 10.3389/fmed.2021.595077
[77] Kruskal, William H., and W. Allen Wallis. "Use of ranks in one -criterion variance analysis." Journal of the American Statistical
Association 47, no. 260 (1952): 583-621. DOI:10.1080/01621459.1952.10483441
[78] Cohen, Jacob. Statistical power analysis for the behavioral sciences. routledge, 2013.
[79] Dunn, Olive Jean. 1964. “Multiple Comparisons Using Rank Sums.”  Technometrics 6 (3): 241 –52.
DOI:10.1080/00401706.1964.10490181.
[80] Yoseph, Fahed, Nurul Hashimah Ahamed Hassain Malim, Markku Heikkilä, Adrian Brezulianu, Oana Geman, and Nur Aqilah
Paskhal Rostam. "The impact of big data market segmentation using data mining and clustering techniques." Journal of Intelligent
& Fuzzy Systems 38, no. 5 (2020): 6159-6173. DOI:10.3233/JIFS-179698
[81] Vyshotravka, Diana, Victoria V ysotska, Zhengbing Hu, Dmytro Uhryn, Yuriy Ushenko, and Kyrylo Smelyakov. "Smart
Application for Recruiting Based on Natural Language Processing Methods, Transformer Models and Siamese Neural Network
Architecture," Internation al Journal of Intelligent Systems and Applications  17, no. 5 (2025): 95 -157. DOI:
10.5815/ijisa.2025.05.07
[82] Shen, Tiancheng, Jia Jia, Yan Li, Hanjie Wang, and Bo Chen. "Enhancing music recommendation with social media content: an
attentive multimodal autoencoder approach." In 2020 International Joint Conference on Neural Networks (IJCNN), pp. 1-8. IEEE,
2020. DOI:10.1109/IJCNN48605.2020.9206894
[83] Yang, Hang, Lin Bao, XiaoYan Sun, and YuMeng Peng. "Dual Sparse Variational Autoencoder-driven Interactive Estimation of
Distribution Algorithm with User Generated Contents." In  2024 International Conference on New Trends in Computational
Intelligence (NTCI), pp. 172-177. IEEE, 2024. DOI:10.1109/NTCI64025.2024.10776443
[84] Sotiriadis, Marios D. "Sharing tourism experiences in social media: A literature review and a set of suggested business
strategies." International Journal of Contemporary Hospitality Management 29, no. 1 (2017): 179-225. DOI:10.1108/IJCHM-05-
2016-0300
[85] Abbas, Ash Mohammad. "An algorithm for next-level connections of users in online social networks." Iran Journal of Computer
Science 7, no. 2 (2024): 189-201. DOI:10.1007/s42044-023-00168-3
[86] Okeke, Nnenna Ijeoma, Olufunke Anne Alabi, Abbey Ngochindo Igwe, Onyeka Chrisanctus Ofodile, and Chikezie Paul -Mikki
Ewim. "Customer journey mapping framework for SMEs: Enhancing customer satisfaction and business growth." World Journal
of Advanced Research and Reviews 24, no. 1 (2024): 2004-2018. DOI:10.30574/wjarr.2024.24.1.3206
[87] Dai, Qi, and Jingyi Zhang. "Interaction between satisfaction and incentives on online reviews." Asia Pacific Journal of Marketing
and Logistics 32, no. 4 (2020): 899-921. DOI:10.1108/APJML-04-2019-0238
[88] Luca, Michael, and Georgios Zervas. "Fake it till you make it: Reputation, competition, and Yelp review fraud."  Management
Science 62, no. 12 (2016): 3412-3427. DOI:10.1287/mnsc.2015.2304
[89] Salminen, Joni, Chandrashekhar Kandpal, Ahmed Mohamed Kamel, Soon -gyo Jung, and Bernard J. Jansen. "Creating and
detecting fake reviews of online products."  Journal of Retailing and Consumer Services  64 (2022): 102771.
DOI:10.1016/j.jretconser.2021.102771
[90] Hemalatha, B., R. Karthika, and B. Kavya Srinidhi. "Customer Segmentation using Clustering Techniques: Data-Driven Approach
to Enhance Marketing Strategy." In  2024 International Conference on Sustainable Communication Networks and Application
(ICSCNA), pp. 1127-1134. IEEE, 2024. DOI:10.1109/ICSCNA63714.2024.10864053
[91] Chowdhury, Ananya Ghosh, Ridhi Deora, Rahul Prathikantam, and Samant Kumar. "Dynamic Clustering with Deep Learning for
Customer Segmentation." In 2025 7th International Conference on Intelligent Sustainable Systems (ICISS), pp. 674 -680. IEEE,
2025. DOI:10.1109/ICISS63372.2025.11076506
[92] Kalasampath, Khushi, K. N. Spoorthi, Sreeparvathy Sajeev, Sahil Sarma Kuppa, Kavya Ajay, and M. Angulakshmi. "A literature
review on applications of explainable artificial intelligence (XAI)." IEEE Access (2025). DOI:10.1109/ACCESS.2025.3546681
[93] ŞAHiN, Emrullah, Naciye Nur Arslan, and Durmuş Özdemir. "Unlocking the black box: an in -depth review on interpretability,
explainability, and reliability in deep learning."  Neural Computing and Applications  37, no. 2 (2025): 859 -965.
DOI:10.1007/s00521-024-10437-2

A Novel Deep Learning Framework for Customer Segmentation and Satisfaction Analysis in Tourism using
Multimodal User-generated Content
Volume 18 (2026), Issue 5 – Page 172
Authors’ Profiles
Gaganmeet Kaur Awal is an Assistant Professor at the Department of DSM, Delhi Technological University (DTU),
Delhi, India (Formerly Delhi College of Engineering). She holds a Ph.D. from the School of Computer and Systems
Sciences, Jawaharlal Nehru University (JNU), New Delhi, India. She has completed M.Tech (CST) from JNU a nd
B.Tech (CSE) from GGSIPU, Delhi. She has been awarded the prestigious DST Inspire Fellowship from the Ministry
of Science and Technology, Govt. of India. Prior to DTU, she had teaching experience at Sha heed Sukhdev College
of Business Studies, University of Delhi and Jaypee Institute of Information Technology, Main Campus, Sector 62,
Noida. She has published papers in reputed international journals and conferences. Her research interests include
Machine Learning and Data Analytics/Mining, Collective Intelligence in Social Computational Systems, Social Networks Analysis ,
and Business Analytics.

Ujjwal Tehlan  is currently pursuing Ph.D. from Delhi School of Management  (DSM), Delhi Technological
University (DTU), New Delhi, India.  She received her Master of Business Administration in Business Analytics
from DTU and Bachelor of Science from the University of Delhi (DU). She has work ed with reputed firms  like
Nagarro and Hays. Her research interests include Machine Learning, Deep Learning, and Business Analytics.

How to cite this paper:
Gaganmeet Kaur Awal, Ujjwal Tehlan, "A Novel Deep Learning Framework for Customer Segmentation and Satisfaction Analysis in
Tourism using Multimodal User -generated Content", International Journal of Intelligent Systems and Applications  (IJISA), Vol.18,
No.5, pp.153-172, 2026. DOI:10.5815/ijisa.2026.05.08
