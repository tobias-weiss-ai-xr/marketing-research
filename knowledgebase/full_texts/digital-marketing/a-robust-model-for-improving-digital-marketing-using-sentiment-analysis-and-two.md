---
title: A robust model for improving digital marketing using sentiment analysis and two-agent off-policy
  proximal policy optimization
url: https://doi.org/10.1038/s41598-026-71894-4
category: digital-marketing
subcategory: framework
date: 2026-10
venue: Scientific Reports
authors:
- Mohammad Yarjanli
- Neda Mahdinasab
source: openalex-oa
pdf_url: https://www.nature.com/articles/s41598-026-71894-4_reference.pdf
pages: 56
chars: 203372
fetched_at: '2026-11-08T18:44:53+00:00'
kb_version: 1
---

# A robust model for improving digital marketing using sentiment analysis and two-agent off-policy proximal policy optimization

ARTICLE | Article in Press
Scientific Reports https://doi.org/10.1038/s41598-026-71894-4
Scientific Reports
This Article in Press is shared early to give you faster access to new research. It is citable and carries a permanent DOI.
The final edited version will replace it automatically.
A robust model for improving digital marketing using
sentiment analysis and two-agent off-policy proximal
policy optimization
Mohammad Yarjanli · Neda Mahdinasab
Received: 10 December 2025 / Accepted: 11 September 2026
© The Author(s) 2026
Abstract
Understanding consumer sentiment is important in digital marketing because it strongly influences brand per -
ception and purchasing decisions. This paper proposes a novel two-agent off-policy proximal policy optimi -
zation (PPO) framework. Unlike standard multi-agent reinforcement learning (RL) approaches, the proposed
framework uses a two-agent off-policy PPO design. It combines an active learning (AL) agent for sample
selection with a sentiment analysis (SA) agent to improve labeling efficiency and classification robustness.
Current SA methods often face challenges related to labeling efficiency, feature selection, class imbalance,
generalization, and hyperparameter optimization. Unlike existing SA approaches that tackle these challenges
independently, the proposed framework addresses them within a unified learning workflow. To address these
challenges, the proposed two-agent framework has the first agent select the most informative unlabeled samples
for annotation. This reduces labeling costs. The second agent then performs SA. Within the second agent, local
interpretable model-agnostic explanations (LIME) guides feature selection. Augmented rewards are also used
to improve the recognition of underrepresented classes. A relational generative adversarial network frame -
work enhanced with gradient signal exclusion (RelGANGE) is used for online data augmentation. To increase
sample diversity, the generator in RelGANGE ignores gradients from samples that receive high discrimina -
tor weights. Hyperparameters are optimized using Bayesian optimization hyperband (BOHB). Comprehensive
evaluations on the Amazon Instant Video (AIV), Amazon Apps and Games Reviews (AA), and Yelp datasets
were conducted using 5-fold cross-validation. The proposed framework achieved F-measure scores of 95.163%,
95.580%, and 93.054%, respectively. These results significantly outperformed traditional and transformer-based
baselines. Statistical analyses confirmed that the improvements were significant ( p < 0.01). The findings dem -
onstrate the effectiveness of the proposed framework for e-commerce recommendation systems (RSs) and
decision-support applications.
Keywords E-commerce recommendation system · Sentiment analysis · Multi-agent system · Proximal
policy optimization · Generative adversarial network · Bayesian optimization

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
Introduction
Customer feedback has huge implications for what people buy and how business plan their strategies. This is
particularly true of online marketplaces, where people often read past reviews before making a purchase1. How-
ever, the large volume and disorganized structure of such reviews pose a significant challenge for individuals and
organizations seeking to derive meaningful insights 2. To address this, SA has become a cornerstone technique
in natural language processing (NLP), aiming to classify textual content as positive, negative, or neutral. SA
helps the companies to understand public opinion. It also assists in brand management, trend forecasting, and
marketing refinement. For end users, SA makes it easy to navigate large-scale opinion data, enabling them to
make well-informed decisions 3. From a business and economic perspective, improvements in SA can increase
revenue, improve customer segmentation, and support more accurate recommendation strategies in e-commerce
platforms. Even small gains in prediction accuracy can influence user engagement and purchasing behavior. This
study investigates how improvements in SA affect business performance in e-commerce platforms.
A great variety of artificial intelligence (AI) approaches have been investigated to implement SA into RSs,
with deep learning models taking the lead 4,5. Although these models have been successful, they still have five
major challenges. These are low data efficiency, poor feature selection, class imbalance, poor generalization, and
hyperparameter tuning. These shortcomings constrain the reliability and scalability of existing solutions. This
study intends to solve these five important issues by the introduction of a coherent SA framework designed for
this purpose6.
Various complex neural models have been proposed for the solution of the sentiment classification problems,
such as long short-term memory (LSTM) networks7–10. Despite their effectiveness, LSTMs require large amounts
of labeled data, which is often costly and hard to produce in SA applications 11. This has led to the development
of techniques that require a minimum amount of annotations without losing too much predictive power. One
promising solution is AL, which is focused on selecting the most valuable unlabeled samples for expert labeling
and iterative model training. However, conventional AL strategies are largely based on fixed heuristics, including
uncertainty estimation or representativeness measures 12. These static approaches do not change as the model is
evolving throughout the training. For example, a sample that was thought to be uncertain at the beginning of the
training process can become easy to classify. Rigid strategies are often unresponsive to such changes. This lack
of adaptability results in an inefficient query selection process, redundant labeling, and a slower optimization
process. These problems are more severe in the case of deep LSTM-based SA tasks, where the internal model
behavior is significantly changed during training.
Deep RL (DRL) provides an adaptive solution to AL, where the strategy of sample selection evolves with the
training of the model13,14. In contrast to conventional techniques, where heuristics are fixed, DRL uses feedback
from training to evaluate the value of labeling15. It then changes the selection strategy accordingly. For instance,
DRL can ignore samples that appear uncertain at the start of training but become predictable later in the train -
ing process. This helps to reduce redundant labeling. This adaptability enables the model to prioritize the most
informative inputs at various training stages. This helps to improve the labeling efficiency and accelerate the
learning curve. Although DRL has been used for SA16, its application in AL for SA has not yet been investigated.
Nonetheless, DRL methods still have challenges, such as low sample efficiency. This is a limitation that reduces
their ability to learn effectively from small data sets. In this paper, we apply off-policy PPO for AL. Compared
with many alternative off-policy RL methods, off-policy PPO balances sample efficiency, training stability, and
the discrete nature of sample selection. This makes it suitable for AL tasks with limited labeled data.
Selecting the right features is important for improving SA models, as it enables them to focus on the textual
attributes most relevant to accurate sentiment prediction 17. Existing SA approaches often use attention mecha -
nisms, feature weighting, or embedded feature selection to identify useful textual features 18–20. Although these

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
methods have achieved promising results, they often depend on fixed evaluation criteria. Therefore, they may not
adapt well to changing feature importance, domain-specific language patterns, or complex semantic interactions.
In addition, attention-based methods often prioritize highly correlated features over truly informative sentiment-
bearing attributes. Many existing approaches also lack mechanisms to continuously adjust feature selection deci-
sions based on model feedback during training. As a result, important contextual and sentiment-related features
may be overlooked, limiting classification performance and adaptability across different SA scenarios.
Imbalanced sentiment distributions are a major challenge in sentiment-based recommender systems because
positive, negative, and neutral opinions are often unevenly represented21. This imbalance can bias models toward
dominant sentiment classes and reduce their ability to capture rare but informative user opinions. Existing solu -
tions include data-level techniques, such as oversampling and undersampling. They also include algorithm-level
methods, such as cost-sensitive learning and ensemble models22–24. Although these strategies can improve minor-
ity-class recognition, they often rely on fixed rules. Therefore, they may not adapt well to changing sentiment
distributions or contextual language patterns. In addition, excessive emphasis on minority classes may reduce
overall classification balance and reliability. Consequently, accurately identifying minority sentiment patterns
remains a significant challenge for SA systems.
This study applies off-policy PPO to solve important issues in SA, such as feature selection and class imbal -
ance. It uses flexible reward design in order to do this. The reward mechanism helps to highlight both important
and neglected features that will help the model capture more subtle yet important patterns. To make interpret -
ability better, LIME values are incorporated into the framework. This allows the system to test the contribution of
each feature to predictions and determine which attributes have the greatest effect on predictions. To deal with the
imbalances, off-policy PPO gives a higher reward to samples from minor classes, which encourages the model
to be more accurate for underrepresented classes without degrading overall performance. Off-policy PPO fits
dynamically to changes in data and complicated feature interactions. This gives it an advantage over conventional
methods that take into consideration a non-adaptive approach.
Data augmentation is widely used to improve the generalization capability of SA models by increasing the
diversity of textual training samples25. Existing approaches include offline and online augmentation. Offline aug-
mentation expands the dataset before training, while online augmentation generates samples during training 26.
Among these methods, generative models such as RelGAN have shown promise in producing realistic sentiment-
related text. However, standard RelGAN often suffers from training instability and mode collapse, limiting the
diversity and quality of generated samples27. Although several improvements have been proposed, many existing
variants still struggle to capture subtle sentiment patterns and contextual language variations. To address these
limitations, this study employs RelGANGE, which improves training stability and promotes greater diversity in
generated sentiment samples.
Hyperparameter optimization is essential for SA models because it directly influences learning effectiveness
and generalization performance 28. Existing optimization methods include grid search, Bayesian optimization
(BO), evolutionary algorithms, and hyperband (HB)29–31. While these approaches have achieved success in vari-
ous applications, they often face challenges related to computational cost, sensitivity to initialization assump -
tions, or inefficient resource allocation. These limitations become more pronounced in deep SA models with large
hyperparameter search spaces. To address this issue, we adopt BOHB. It combines model-based sampling with
adaptive resource allocation. BOHB eliminates weak configurations early and focuses on promising regions of
the search space. This provides a scalable solution for hyperparameter optimization in SA tasks32.
The main objective of this study is to evaluate the impact of improved sentiment analysis performance on
decision-making in e-commerce systems. For this goal, this work proposes an SA framework for processing
customer reviews in e-commerce recommender systems. The framework is built on a two-agent off-policy PPO
architecture. The first agent is an AL module based on LSTM units that selects informative samples for annota -
tion and training. The second agent addresses feature selection and class imbalance. The framework also uses

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
RelGANGE for online data augmentation and BOHB for hyperparameter optimization. In addition, generative
pre-trained transformer (GPT)-based embeddings are added to the classifier input layer. They provide richer con-
textual and semantic representations of customer reviews. LSTM units capture sequential dependencies. In con-
trast, GPT embeddings encode broader contextual information and complex language patterns in sentiment-rich
user reviews. The combination of GPT embeddings and LSTM-based learning enables the framework to better
capture nuanced sentiment expressions and improve sentiment classification performance.
Most existing SA and recommender system frameworks address these challenges through separate modules or
independent optimization procedures. These challenges include sample selection, feature selection, class imbal -
ance, data augmentation, and hyperparameter optimization. This fragmented design often limits information
sharing across components and reduces the overall adaptability of the learning process. To overcome these limi-
tations, the proposed framework introduces a coordinated learning architecture. In this design, AL and SA interact
within a shared optimization process. In addition, the framework integrates LIME, RelGANGE, and BOHB into
a unified workflow. This workflow supports feature selection, class imbalance handling, data augmentation, and
hyperparameter optimization. The framework addresses these interconnected challenges jointly rather than treat-
ing them as isolated tasks. This improves data efficiency, feature quality, class balance, and scalability, making
the framework more suitable for real-world e-commerce recommendation applications.
The main contributions of this research study can be summarized as follows:
 ● The proposed framework adopts a two-agent design based on an off-policy PPO. The off-policy PPO design is
intended to improve sample efficiency. The first agent is an AL module that dynamically selects the most in -
formative unlabeled samples. This reduces labeling costs. The selected samples are passed to the second agent
for sentiment classification. Within this agent, LIME values are used to identify the most important features.
Augmented rewards are also attributed to the underrepresented classes. This helps correct class imbalances and
improves performance on the minority class.
 ● To improve generalization and address limited training data, the framework uses RelGANGE. It generates syn-
thetic samples during training. RelGANGE suppresses unstable gradient paths during generation. As a result,
it generates more diverse and stable synthetic samples. This helps to increase textual variety and increases the
accuracy of sentiment classification.
 ● For hyperparameter tuning, BOHB is used in this framework. BOHB combines informed sampling with ef -
ficient resource allocation. It removes weak configurations early and focuses the search on promising re -
gions. This enables efficient hyperparameter optimization without relying on exhaustive grid search or random
search. It is very effective for deep learning-based SA.
The rest of this paper is organized as follows. Section " Related works" presents a comprehensive overview of
related work on RS in e-commerce, highlighting the main contributions and identifying research gaps. Section
"Materials and methods" presents the proposed framework, which outlines the methods and algorithms designed
to enhance RS performance. Section "Empirical evaluation" presents the results of experimental evaluations and
analyzes the performance of the proposed approach for various settings. Lastly, Section "Conclusions" concludes
with a summary of the main insights and directions for future investigation in this area.
Related works
Based on previous RS studies, current approaches can be broadly classified into two categories: traditional tech-
niques and transformer-based models. Sections 2.1 and 2.2 give a detailed discussion of these categories. The dis-
tinctive aspects of our proposed framework are presented in Section " Related works"-"Materials and methods".
It highlights the innovations and illustrates how the proposed method implicates key gaps left by earlier work.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
Traditional
Some of the early recommendation approaches included user-item collaborative filtering (CF), latent factor mod-
els, rule-based associations, and discriminative clustering. These methods provided the basis for further devel -
opments. In 2023, Huh 33 released ML.Recommend a system that is built on Microsoft ML.NET. This system
combines matrix factorization and temporal dynamics to provide better product recommendations. It also uses
logistic regression on the user comments to improve personalization. Loukili et al.34 proposed a method for pro-
ducing personalized suggestions based on association rules extracted using the frequent pattern growth algorithm.
In 2024, Belhadi and others 35 created a privacy-conscious recommendation model. The model combines feder -
ated learning, transformers, and contrastive clustering. As a result, their approach guarantees data confidentiality
while enabling personalized data through both global aggregation and cluster-specific strategies.
In recent years, there has been growing interest in more complex neural and integrated models to better capture
complex user-item interactions. This has been especially important when dealing with unstructured inputs such
as customer reviews. A range of methods has been applied, including LSTM networks, attention mechanisms,
ensemble approaches, and multi-agent systems, to enhance the accuracy and robustness of RSs. In 2023, Gulzar
et al.36 proposed the ordered clustering-based algorithm (OCA). This method uses CF to group users with similar
preferences. It tackles the data sparsity and cold-start problems in e-commerce recommendations. Sharma and
Sagvekar37 proposed an SA framework that is an ensemble of multiple weighted LSTMs coupled with word-
embedding attention (WEA), yielding a robust feature representation and reliable classification of emotion-rich
textual content. Vullam et al. 38 developed a multi-agent personalized recommendation approach based on user
category clustering. This approach optimizes CF by limiting neighbor searches to similar user groups, which
makes the system more efficient and relevant. Karn et al. 39 proposed a hybrid recommendation strategy that
combines a hybrid recommendation model (HRM) with SA, allowing user feedback to refine initial recom -
mendations and increase personalization. Chang et al. 40 proposed the knowledge graph transformer network
(KGTN). It is a combination of collaborative knowledge graphs (KGs) and graph neural networks (GNNs). The
system is explainable and multi-domain recommendations by learning meta-paths and generating effective node
embeddings.
Recent research has concentrated more on tackling the persistent challenges of recommender systems, such as
changing user interests, sparse interaction data, and the complexity of feature representation. To overcome these
problems, several approaches have been proposed in studies, such as unsupervised pretext training, graph-based
modeling, and decoupling attention. In 2023, Yadav et al.4 developed an SA model for Hindi product reviews on
social media. The model is based on an LSTM but uses a continuous bag-of-words (CBOW) technique to capture
linguistic nuances and improve vectorization. In 2024, Shang et al.41 proposed a sentiment-awareness neural CF
(SNCF) model. Their model uses a hierarchical attention network to analyze emotional signals and enhance con-
textual user-item embeddings. Shankar et al.1 described an ensemble-based approach for recommendations based
on the integration of different behavior signals, such as browsing activities, wish lists, and reviews. This way,
irrelevant results are diminished, and the recommendations are more precise. Keikhosrokiani and Fye42 proposed
a hybrid method that uses collaborative and content-based filtering. Their model uses term frequency-based
inverse document frequency (TF-IDF) and cosine similarity to address cold-start issues, diverse user needs, and
large product inventories in the healthcare e-commerce context. In 2025, Duan et al. 43 proposed a disentangled
frequency attention network (DFAN). It differentiates popularity-fuelled short-term activities from real prefer -
ences. The method for achieving this is frequency attention and adaptive filters, balancing dynamic short-term
and long-term interests. Wang et al.44 proposed a self-supervised cognitive learning (SSCL) framework tailored
to model diverse user preferences. The framework can work on several tasks simultaneously, thanks to enhanced
feature representations and specialized gating and aggregation modules. Nag et al.45 proposed an SA-augmented
hybrid CF system that uses review-based sentiment scores to provide personalized recommendations using opin-
ion-rich social media content. Zhang et al. 46 proposed a hybrid recommender method in which rating data and

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
review sentiment are combined. Their model uncovers complementary elements of user preferences, enabling
more precise and personalized suggestions.
Transformer
A large number of research papers have used transformer architectures, such as BERT (bidirectional encoder
representations from transformers) and RoBERTa (robustly optimized BERT approach), to analyze sentiment
and extract high-quality semantic features from user reviews. In 2024, Zhao et al. 47 proposed a hybrid recom -
mender that uses BERT to extract textual features from customer feedback. The system combines these features
with a deep neural network (DNN) for numerical data, thereby improving the interpretation of consumer input
on e-commerce platforms. Bellar et al.48 compared various deep learning models for sentiment classification and
showed that Transformer-based BERT embeddings can capture the subtle opinions of consumers. This helps in
better marketing strategies and product design. Scientific 49 presented a recommendation framework combined
with content-based filtering SA using RoBERTa Transformer. This design allows product recommendations to be
made based on quantified review sentiment and content similarity. In 2025, Karabila et al. 50 developed a hybrid
RS. It combines singular value decomposition (SVD), BERT with collaborative filtering (BERT-CB), SA with
global vectors for word representation (GloVe), a convolutional neural network (CNN), and a bidirectional gated
recurrent unit (BiGRU).
Many recent studies have used models such as transformers, along with traditional recommendation meth -
ods like CF and matrix factorization, to improve accuracy and relevance. In 2024, Karabila et al. 51 proposed a
hybrid system combining CF with a fine-tuned BERT model for SA. This design enhances understanding of the
review text and increases the relevance of the product in individual recommendations. In 2025, Darraz et al. 52
further adopted this concept by incorporating BERT-based SA into collaborative and content-driven filtering.
Their framework addresses such problems as user sentiment, sparse data, and personalization. The model uses a
hybrid learning approach based on deep matrix factorization. Krishna et al.53 proposed a hybrid recommendation
model that combines SA and CF. The framework has a long-term frequency-based modified inverse class fre -
quency (LFMI) for feature extraction. It also consists of a multi-layer attention-based encoder-decoder temporal
CNN (MLA-EDTCNet) for classification and a modified conditional generative adversarial network (MCGAN)
for oversampling. Moreover, it contains the ocotillo optimization algorithm (OcOA) for parameter optimization.
The advent of large language models (LLMs) such as GPT-3.5 and LLaMA-2 (LLM meta AI version 2) has
prompted some new studies. These works delve into the potential of these updates to improve user modeling and
generate more accurate recommendations. In 2023, Mohanty et al. 54 considered the integration of large trans -
former-based models in recommender systems. Their work focused on how to personalize interactions through
prompt engineering and fine-tuning, as well as deployment issues in practical settings. In 2024, Roumeliotis et
al.55 compared several fine-tuning transformer models, GPT-3.5, LLaMA-2, BERT, and RoBERTa. Their evalua-
tion focused on the effectiveness of these models to capture sentiment for the analysis of customer satisfaction in
e-commerce. Jeong and Lee56 proposed a recommendation framework after a transformer NLP model. The model
uses tokenization of product names in order to capture semantic relationships. This design encourages purchase
prediction and the development of new product concepts aligned with consumer trends.
Recent research has explored the use of transformer models to populate entire recommendation pipelines.
These include stages of data processing, contextual analysis, ranking, and delivery. In 2023, Sun et al.57 designed
a transformer-based recommender that retrieves and re-ranks similar software failure cases using a fine-tuned
BERT. This system streamlines root cause analysis and reduces the need for manual review. Iftikhar et al.58 created
an automated SA framework that combines BERT and machine learning and deep learning methods. Their results
show that BERT performs well at understanding the meaning context provided by customers. Jagatap et al. 59
proposed a session-aware recommendation model named AttriBERT (attribute BERT). It uses product attribute-
value pairs to determine the hidden user preferences based on the browsing patterns. This makes recommendation
refinement for mobile e-commerce. In 2024, Gheewala et al.60 investigated the use of deep transformer networks

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
Authors Approach Contribution Limitation
Tran and
Huh33
ML. Recommend built with
Microsoft ML.NET
Integrates matrix factorization with temporal dynamics
for personalized product suggestions
Lacks mechanisms to adapt effectively
to customer reviews written in non-
English languages
Loukili et al.34 Frequent pattern growth
approach
Applies association rule mining to improve item-level
personalization
Lacks mechanisms to adapt effectively
to customer reviews written in non-
English languages
Belhadi et al.35 Federated learning with
clustering and trusted
authority mechanisms
Preserves privacy while tailoring recommendations
through user clustering
Struggles to respond to rapidly evolv-
ing user interests
Gulzar et al.36 OCA Group users with collaborative filtering based on
shared preference patterns
Strong reliance on local data validation
processes
Sharma and
Sagvekar37
LSTM-based weighted
ensemble combined with
WEA
Improves SA through specialized word embedding
techniques
Scalability issues when applied to
extremely large datasets
Vullam et al.38 Multi-agent recommenda-
tion with user grouping for
e-commerce platforms
Employs user clustering to narrow neighbor search
and refine recommendations
Limited capacity to process heteroge-
neous data beyond text and multimedia
inputs
Karn et al.39 HRM enhanced with SA Incorporates SA to strengthen the understanding of
user preferences
Static clustering approaches perform
poorly in dynamic market conditions
Chang et al.40 KGTN Uses knowledge graphs to support explainable multi-
domain recommendations
Difficulty in recommending for new or
low-activity users
Yadav et al.4 LSTM integrated with a
continuous bag of words for
Hindi SA
Focuses on SA for Hindi text in social media reviews Requires heavy preprocessing before
model training
Shang et al.41 SNCF Leverages user-generated sentiments from reviews to
improve recommendations
Sensitivity to linguistic variations
across different dialects and contexts
Shankar et al.1 Ensemble-based intelligent
recommender system
Combines multiple user behavior data streams for bet-
ter personalization
Dependent on the availability and rich-
ness of customer reviews
Keikhosroki-
ani and Fye42
Hybrid model using TF-IDF
with cosine similarity
Merges collaborative and content-based filtering for
more accurate suggestions
May fail to detect emerging patterns
without supplementary data
Duan et al.43 DFAN Differentiates true long-term interests from short-term
popularity effects
Incomplete capture of niche or special-
ized user preferences
Wang et al.44 SSCL Enhances feature representation and exploration of
diverse user interests
Limited adaptability to abrupt behav-
ioral changes among users
Nag et al.45 Hybrid CF integrated with
SA
Employs SA for fine-tuning recommendations High computational demands for train-
ing and deployment
Zhang et al.46 Recommendation frame-
work enhanced with SA
Builds richer user profiles using both ratings and
review-based sentiment
Relies heavily on social media data
quality and consistency
Zhao et al.47 BERT combined with a
DNN
Improves feedback interpretation by integrating tex-
tual and numerical data
Vulnerable to inconsistencies in user
sentiment expressed in reviews
Bellar et al.48 Neural architectures for SA Benchmark deep learning models for predicting con-
sumer sentiment
Often computationally expensive in
both training and inference phases
Scientific49 Content-driven filtering
supported by RoBERTa-
based SA
Boosts personalization in recommendations by analyz-
ing review sentiments
Substantial training resources are
required for effective performance
Karabila et
al.50
Hybrid RS with SVD,
BERT-CB, and SA
Combines SVD, BERT-CB, and hybrid SA using
GloVe with CNN-BiGRU for enriched profiles and
sentiment-aware recommendations
High complexity and computational
cost due to the integration of multiple
deep learning components
Karabila et
al.51
Hybrid recommendation
approach with fine-tuned
BERT for SA
Applies sentiment insights for deeper modeling of user
preferences
May overlook subtle variations in user
preferences
Darraz et al.52 Sentiment-aware recom-
mendation model
Strengthens recommendation pipelines with senti-
ment-aware modules
Heavy dependence on textual data
accuracy and completeness
Krishna et al.53 Hybrid RS with SA and CF Combines LFMI for feature extraction, MLA-
EDTCNet for classification, MCGAN for imbalance
handling, and OcOA for hyperparameter tuning
High complexity due to integration of
multiple deep learning modules
Mohanty et
al.54
LLMs in e-commerce
recommenders
Investigates LLMs for advancing preference
prediction
Cold-start and data sparsity remain
challenges with new or infrequent users
Table 1 Comparison of traditional and transformer models for RS in e-commerce.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
in review-based recommender systems. Their approach produces detailed and interpretable user-item embed -
dings from fine-grained review text, thereby enhancing personalization. Ali et al. 61 applied transformer-based
models, such as BERT and XLNet (extreme language understanding), for sentiment classification of Amazon
reviews, demonstrating their effectiveness in extracting subtle contextual cues to enhance e-commerce decision-
making. In 2025, Khan et al. 62 proposed MetaBERTTransformer4Rec (MBT4R), a transformer-based RS that
uses self-attention to capture sequential dependencies and contextual relationships, enabling a deeper understand-
ing of user preferences for more personalized and adaptive movie recommendations. Vaghari et al. 63 proposed
an RS. It integrates a hierarchical attention network (HAN), a group-wise enhancement mechanism, BiGRU,
and multi-head attention to extract short- and long-term user preferences with richer item-attribute relationships.
Limitations
Table 1 summarizes traditional and transformer-based approaches to recommender systems in e-commerce. Tra-
ditional methods, such as collaborative filtering and matrix factorization, rely heavily on static user-item interac-
tions. They often struggle to use contextual information from customer reviews. As a result, they face limitations
in personalization, adaptability, and sentiment understanding.
Transformer-based models have significantly improved semantic representation and recommendation accu -
racy. However, several important challenges remain. First, many approaches still require large amounts of labeled
data for domain-specific SA. Second, feature selection mechanisms often rely on static importance estimation
and may overlook context-dependent sentiment cues. Third, sentiment datasets are frequently imbalanced. This
causes models to favor dominant classes and reduces their ability to identify minority opinions. Fourth, trans -
former models may exhibit limited generalization as sentiment patterns and user preferences evolve. Finally, their
performance is highly dependent on hyperparameter settings, making optimization computationally expensive.
Authors Approach Contribution Limitation
Roumeliotis et
al.55
Comparative study of
LLMs for sentiment
evaluation
Compares state-of-the-art LLMs in sentiment-based
recommendation tasks
Potential inefficiency and bias issues in
LLM training
Jeong et al.56 Tokenization-driven NLP
recommendation framework
Uses tokenization to detect subtle semantic links in
product data
Performance may vary across different
review contexts and domains
Sun et al.57 Two-stage BERT-based
NLP recommender
Employs NLP methods for analyzing and re-ranking
software failure records
Risk of generating unrealistic or
impractical product suggestions
Iftikhar et al.58 Automated sentiment
classification with machine
learning and deep learning
approaches
Combines diverse analytic approaches for classifying
review content
Requires extensive fine-tuning with
domain-specific data
Jagatap et al.59 AttriBERT for refin-
ing session-based
recommendations
Leverages product attribute–value information to infer
hidden user preferences
Difficulty in capturing subtle or
nuanced sentiments within reviews
Gheewala et
al.60
Deep transformer-driven
models for review-centric
recommenders
Improves user–item embeddings with deep trans-
former architectures
May fail to track preference shifts dur-
ing long interaction sessions
Ali et al.61 SA using NLP and deep
learning hybrids
Applies advanced NLP and deep learning for senti-
ment classification
Limited generalization across diverse
e-commerce platforms and categories
Khan et al.62 Transformer-based RS
(MBT4R)
Introduces MetaBERTTransformer4Rec using self-
attention to model sequential dependencies and con-
textual relationships for user preference understanding
High complexity and increased com-
putational requirements for large-scale
sequential modeling
Vaghari et al.63 RS with transformer Combines HAN, group-wise enhancement, BiGRU,
and multi-head attention to model user preferences and
complex item-attribute relationships
High model complexity and potential
scalability challenges in large-scale
e-commerce settings
Table 1 (continued)

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
Although previous studies have addressed these issues, they usually handle them through separate modules
and optimization procedures. Therefore, previous studies rarely consider the interactions among sample selec -
tion, feature selection, class imbalance handling, data augmentation, and hyperparameter optimization. This limi-
tation motivates a unified framework that addresses these interconnected challenges within one learning process.
Therefore, this study proposes a two-agent off-policy PPO framework. It integrates AL for sample selection with
SA in a coordinated learning architecture. The framework also incorporates LIME-guided feature selection, adap-
tive class imbalance handling, RelGANGE-based online data augmentation, and BOHB-based hyperparameter
optimization. These components address the main challenges in a unified manner.
Materials and methods
Figure 1 illustrates the overall architecture of the proposed framework for sentiment-driven recommendation
in e-commerce. The system consists of four interacting components: a two-agent off-policy PPO module, GPT-
based text representations, a RelGANGE-based online data augmentation module, and a BOHB-based hyperpa -
rameter optimization module.
The workflow begins with a pool of labeled and unlabeled customer reviews. Agent 1 performs AL by selecting
the most informative unlabeled samples for annotation and transferring them to the labeled training set. The result-
ing training data are then processed by Agent 2. This agent is built using LSTM units and performs feature selec-
tion and sentiment classification. GPT embeddings are used to generate contextual representations of reviews.
LIME scores provide feature importance information that is incorporated into the learning process. Adaptive
rewards in the SA module give more attention to underrepresented classes and help reduce class imbalance. In
Data pool
Agent 2: Feature selection and classification
Query, key, and value
matrices
Attention layer
Updated memory
Generated sentence
Generator
Query, key, and value
matrices
Attention layer
Updated memory
Sigmoid
Discriminator
Real Fake
Online data augmentation
RelGANGE
Start token
Input data
Hyperparameter optimization using BOHB
Two-agent off-policy PPO
s1, a1, r2, s2
s2, a2, r3, s3
st-1, at-1, rt, st
Replay memory
Environment
Gradient
ClassesFeatures
MLP
Parameter update Sample batch
Insert (st, at, rt, st+1)
GPT
LSTM
LSTM
LSTM
LSTM
LSTM
LSTM
LSTM
LSTM
LSTM output
LSTM
LSTM
LSTM
LSTM
RewardAction
State
UnlabeledLabeled
Agent 1: Sample selection
Annotation
Non-annotation
FC
Annotated sample
Fig. 1 Overview of the proposed framework for RS in e-commerce. It integrates two off-policy PPO-based agents for AL
and sentiment classification, GPT-based contextual embeddings for semantic representation, a RelGANGE for online data
augmentation, and a BOHB module for hyperparameter tuning.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
parallel, RelGANGE generates synthetic reviews during training to increase sample diversity and improve gen -
eralization. The generated reviews are first passed to Agent 1 for informativeness evaluation. Only the selected
samples are added to the labeled training set and subsequently used to update Agent 2.
The two PPO agents are trained independently but operate within a coordinated learning framework. Agent 1
affects the quality of the training samples provided to Agent 2. In turn, the classification performance of Agent 2
indirectly affects future sample selection through RL feedback. BOHB operates as a global optimization layer and
periodically updates the hyperparameters of the PPO agents, the classification module, and RelGANGE. During
training, RelGANGE generates candidate samples. Agent 1 selects the most informative generated samples for
model updating. Agent 2 is then retrained on the expanded labeled dataset, while BOHB updates the hyperparam-
eters of the main components. Through this interaction, the framework jointly optimizes sample selection, feature
selection, class imbalance handling, data augmentation, and hyperparameter optimization.
GPT-based embedding
Our approach uses the generative GPT to produce semantic embeddings from textual inputs. GPT models can
contextualize dependencies. This makes it suitable for RSs that have to capture subtle user opinions and domain-
specific sentiment. Unlike BERT, which focuses on bidirectional encoding, GPT uses a generative structure. This
structure is in a more natural, sequential, and causal flow of language. It generates embeddings that are coherent,
context-aware, and well-suited to SA and recommendation tasks.
GPT has been trained on large text corpora using an unsupervised autoregressive objective for language mod-
eling. This training can help the model to produce the next word in a sequence. It constructs word representations
by looking at tokens that occur earlier in the sentence. The essence of GPT is built upon the scaled dot product
self-attention mechanism that is computed as:

Attention(Q, K, V)= softmax ( QK
𝑇𝑇
√𝑑𝑑𝑘𝑘 ) V (1)
In this formulation, 𝑄𝑄, 𝐾𝐾, and 𝑉𝑉 represent the query, key, and value matrices. 𝑑𝑑𝑘𝑘  represents the dimensional size of
the keys. These matrices are usually obtained by applying learned linear projections to the input vectors:
 𝑄𝑄𝑄𝑄𝑄 𝑡𝑡𝑊𝑊 𝑄𝑄 (2)
 𝐾𝐾𝐾𝐾𝐾 𝑡𝑡𝑊𝑊 𝐾𝐾 (3)
 𝑉𝑉𝑉𝑉𝑉 𝑡𝑡𝑊𝑊 𝑉𝑉 (4)
GPT extends the attention mechanism by using multi-head attention, enabling the model to focus on multiple
feature subspaces at the same time:
 𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀 Q, K, V)= CONCAT 𝑀head1,…, headn) W (5)
where
 ℎ𝑒𝑒𝑒𝑒𝑒𝑒𝐢𝐢 = 𝐴𝐴𝐴𝐴𝐴𝐴𝑒𝑒 𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴 (QW
𝑄𝑄
𝑖𝑖 , KW
𝐾𝐾
𝑖𝑖 , VW
𝑉𝑉
𝑖𝑖 ) (6)
GPT uses this architecture to produce token-level representations. These representations represent both the struc-
ture of the grammar and the meaning. They are then used to enhance the feature modeling in RS.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
Online data augmentation
This study proposes an online augmentation method that is based on RelGANGE. RelGANGE decreases the
impact of some batch instances on the gradient. This encourages the development of synthetic samples that are
more diverse and contextually relevant. The step-by-step approach for applying this augmentation strategy is
formally presented in Algorithm 1.
Input: q: threshold controlling whether an instance remains unchanged, :n umber of
minibatches
Output: Augmented dataset
Initialize the set of input batches = { , , ,… , }
Make an empty list to collect processed batches
For every in :
     Compute a keep-score q for every element in
      For every in :
          If < q
                Leave unchanged
          Else:
               Synthetically generate ŝ using the generator model
                Replace with ŝ in the batch
Add the possibly modified batch to
Return
Algorithm 1 Pseudo-code for online data augmentation using RelGANGE.
Within the adapted RelGANGE framework, both the generator and the discriminator use the so-called rela -
tional memory core (RMC) networks to better model sequential dependencies in the data. The RMC is a special
type of recurrent memory structure. It stores information in multiple memory slots and uses self-attention to
capture the detailed temporal relationships. In contrast to traditional models such as LSTM and GRU, RMC
maintains long-term context. At the same time, it models token dependencies using internal attention. This com-
bination helps the architecture better represent extended and relational sequence patterns.
At each time step 𝑡𝑡, the RMC maintains a memory matrix 𝑀𝑀𝑡𝑡 ∈ ℝ𝑁𝑁𝑁𝑁𝑁. Here, 𝑁𝑁 denotes the number of memory
slots, and d denotes the dimensionality of each slot. The memory is updated using a self-attention operation based
on the scaled dot-product formulation introduced in Eqs. 1–4. In this procedure, the memory matrix is projected
into query, key, and value representations. The attention weights regulate how information moves across memory
slots. This enables the model to capture dependencies between different elements of the memory.
The memory state is updated by integrating the output from the attention mechanism:
 ˜𝑀𝑀𝑡𝑡 =𝑀𝑀 𝑡𝑡 + Attention (𝑀𝑀𝑡𝑡) (7)
A multilayer perceptron (MLP) is employed to enhance the expressive capacity of the model. Its output is then
passed through layer normalization:
 𝑀𝑀𝑡𝑡′= LayerNorm ( ˜𝑀𝑀𝑡𝑡 + MLP ( ˜𝑀𝑀𝑡𝑡)) (8)
In the last step, the input embedding 𝑒𝑒𝑡𝑡  is combined with the updated memory 𝑀𝑀𝑡𝑡′  using either gating or concat -
enation. This produces the memory state for the next step 𝑀𝑀𝑡𝑡𝑡𝑡 . This systematic update enables the RMC to pre-
serve a detailed sequence representation that captures both individual tokens and their interactions.
Using the RMC in both the generator and discriminator helps the model create more consistent, context-aware
sequences. It also improves the ability of the model to distinguish between the actual data and the generated
samples. The ability of RMC to support complex relational dependencies is useful for tasks that require nuanced
sequential understanding. This makes the online augmentation framework more effective.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
Input: : start token, : sentiment label, : max length
Output: Generated sentence sequence conditioned on sentiment
Initialize memory matrix with shape ×
Encode the sentiment label using one-hot encoding ( )
Set =
Initialize the generated sequence list
For =1 to :
Embed the current token: = ( )
Concatenate the embedding with the sentiment label: = ( , )
Compute query, key, and value matrices , , and using Equations 1, 2, and 3
Compute attention using Equation 4
Update the memory
Generate output logits: = ( )
Select the next token from
Append to
If = _ :
break the loop
Return
Algorithm 2 Pseudo-code for RMC-based generator.
Input: : Sequence (list of tokens)
Output: Probability that is real
Initialize memory matrix with shape ×
For each token in :
Embed token : = ( )
Compute query, key, and value matrices , , and using Equations 1, 2, and 3
Compute attention using Equation 4
Update the memory
Aggregate final memory: = ( )
Compute output probability: = ( ( ))
Return
Algorithm 3 Pseudo-code for RMC-based discriminator.
Algorithm 2 shows the steps of the RMC-driven conditional generator designed to generate sentiment-specific
sentences. The procedure begins by initializing the memory matrix 𝑀𝑀. The sentiment label 𝑦𝑦 is converted into
an embedding 𝑒𝑒𝑦𝑦  through one-hot encoding. At each time step 𝑡𝑡, the token 𝑥𝑥 is represented using a pre-trained
language model, such as the GPT, producing the embedding 𝑒𝑒𝑥𝑥. This representation is concatenated with the sen-
timent vector 𝑒𝑒𝑦𝑦 to form the conditioned input 𝑒𝑒𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐 . The model first produces query, key, and value matrices by
applying linear transformations to the memory state. It then applies multi-head self-attention to capture relations
among the memory slots. The memory is updated, and the next token is predicted through a fully connected layer.
The predicted token is appended to the sequence. This process repeats until the model reaches the maximum
sequence length or generates an end-of-sequence token. The final output is a complete sentence sequence aligned
with the intended sentiment.
Algorithm 3 presents the pseudo-code for the RMC-based discriminator, which evaluates whether a given
input sequence is real or generated. For each token 𝑥𝑥 in the sequence, the model computes its embedding 𝑒𝑒𝑥𝑥 . The
model then derives query, key, and value matrices from the current memory state. It applies the self-attention
mechanism to update the memory, following the same procedure described for the generator. After the sequence
is fully processed, the final memory matrix 𝑀𝑀 is passed to the 𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴  function. This function gener-
ates a single fixed-size representation. In this implementation, average pooling is applied to compute the mean
across all memory slots:

AggregateMemory(𝑀𝑀𝑀 𝑀 1 𝑁𝑁
𝑁𝑁
∑
𝑖𝑖𝑖𝑖
𝑀𝑀𝑀𝑀𝑀𝑀 (9)
This process produces a unified vector that condenses the content distributed over all memory slots. The repre -
sentation is sent to a classification layer and then passed through a sigmoid activation. This produces a probability

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
score indicating whether the sequence is real or generated. Using the RMC in the discriminator allows it to model
complex sequential dependencies. This improves its ability to distinguish real sequences from synthetic ones.
Loss function
RelGANGE uses an RL strategy for training. This approach improves text generation, particularly when the data
is imbalanced or limited. Unlike conventional adversarial methods that rely on divergence measures such as the
Jensen–Shannon or Wasserstein distances, RelGANGE treats the generator as a stochastic policy. The discrimi -
nator provides a reward signal that guides the training. The goal is to maximize the expected reward over all
generated samples.
The loss of the generator is expressed through a policy gradient–based formulation, defined as follows64:
 ∇𝜃𝜃J(𝜃𝜃)=𝔼𝔼 𝑋𝑋∼𝐺𝐺𝜃𝜃 [𝑅𝑅(𝑅𝑅)∇𝜃𝜃log𝐺𝐺𝜃𝜃(𝑅𝑅)] (10)
Here 𝐺𝐺𝜃𝜃  refers to the generator with parameters 𝜃𝜃, 𝑋𝑋 is a sequence sampled from 𝐺𝐺𝜃𝜃 , and 𝑅𝑅𝑅𝑅𝑅𝑅 represents the reward
assigned by the discriminator for sequence 𝑋𝑋. This reward demonstrates how closely the generated text aligns
with real data. The gradient is estimated using Monte Carlo sampling. The generator parameters are then updated
through backpropagation based on this estimate.
In this study, the stability of the generator is enhanced through a selective gradient filtering strategy. During
parameter updates, gradients associated with the top-k sequences that receive the highest evaluations from the
discriminator are excluded. This approach encourages the generator to focus on diverse or underrepresented sam-
ples. It also reduces the risk of overfitting to outputs that already resemble real data. The corresponding parameter
update rule with top-k exclusion is expressed as:
 𝐿𝐿𝐺𝐺 = 𝜃𝜃𝐺𝐺 − 𝛼𝛼𝐺𝐺∑ 𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡 ∇𝜃𝜃𝐺𝐺 𝐽𝐽𝐽𝜃𝜃) (11)
Here 𝜃𝜃𝐺𝐺  denotes the parameters of the generator, and 𝛼𝛼𝐺𝐺  represents the learning rate. The summation includes only
the samples that remain in the mini-batch after excluding the top-k sequences filtered using discriminator scores.
This reward-based optimization scheme helps reduce common problems in RelGAN training. These include
exposure bias and mode collapse. The method emphasizes gradient signals from challenging and diverse exam -
ples. This encourages the generator to explore a broader sample space and produce more realistic, varied outputs.
Unlike the generator, the discriminator in RelGANGE is optimized with a conventional supervised loss. Its objec-
tive is to assign high values to authentic sequences and low values to generated ones. These scores act as reward
signals that guide updates to the generator policy. The discriminator loss can be expressed as64:
 𝐿𝐿𝐷𝐷 =− (𝔼𝔼𝑥𝑥∼𝑝𝑝𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑥𝑥 [log𝐷𝐷𝐷𝐷𝐷𝐷𝐷 𝐷 𝔼𝔼𝑥𝑥∼𝐺𝐺𝜃𝜃 [log𝐷1 − 𝐷𝐷𝐷𝐷𝐷𝐷𝐷𝐷 ) (12)
In this expression, 𝐷𝐷𝐷𝐷𝐷𝐷 represents the discriminator prediction for the sequence 𝑥𝑥. The purpose of this loss is to
train the discriminator to distinguish genuine inputs from sequences produced by 𝐺𝐺𝜃𝜃 . The reward mechanism
defined in Eq. 12 enables the discriminator to indirectly influence the learning of the generator. The generator
is updated using RL, while the discriminator is trained with backpropagation and remains fully differentiable.
This setup follows the standard adversarial learning paradigm. The interaction of these complementary update
processes improves the realism and diversity of generated sequences.
Multi-agent learning architecture
The proposed recommendation framework employs a two-agent RL design to address significant issues in senti-
ment-based recommendation. These include limited labeled data, the identification of relevant features, and the
handling of class imbalance. The first agent functions as an AL module, selecting the most informative unlabeled

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
samples for annotation to reduce labeling costs and improve training efficiency. The second agent addresses class
imbalance and performs feature selection. The second agent applies LSTM-based extraction along with interpre-
table scoring methods.
Each agent operates under an independent off-policy PPO algorithm. The agents interact through a one-way
flow of information. In this setup, the AL agent builds its state using feature vectors and confidence scores gener-
ated by the second agent. This design allows the active learner to select samples more effectively by relying on
context-rich signals. It also promotes coordinated and adaptive training. The framework supports asynchronous
updates and follows a modular structure. This setup enables each agent to optimize its task while contributing to
the overall system performance.
We first present the two agents that form the framework, followed by an explanation of the off-policy PPO
algorithm used to train them.
Agent 1: AL for sample selection
In this study, the dataset is written as 𝑋𝑋𝑋 {𝑥𝑥𝑖𝑖}
𝑁𝑁
𝑖𝑖𝑖𝑖. Here, 𝑥𝑥𝑖𝑖 refers to the -th input sentence, and 𝑁𝑁 is the total number
of samples. Each input 𝑥𝑥𝑖𝑖 is linked to a label 𝑐𝑐𝑖𝑖. These labels are taken from a fixed set of sentiment categories
𝑐𝑐𝑐 {𝑐𝑐𝑖𝑖}, where every 𝑐𝑐𝑖𝑖 falls into one of 𝐶𝐶 sentiment classes. The labeled subset is defined as 𝑋𝑋𝐿𝐿 = {(𝑥𝑥𝐿𝐿𝑖𝑖 ,𝑦𝑦 𝐿𝐿𝑖𝑖 )}
𝑁𝑁𝐿𝐿
𝑖𝑖𝑖𝑖. In
this notation, 𝑥𝑥𝐿𝐿𝑖𝑖  is the -th labeled sentence, 𝑦𝑦𝐿𝐿𝑖𝑖  is the corresponding class label, and 𝑁𝑁𝐿𝐿 is the number of labeled
samples. The unlabeled subset is denoted as 𝑋𝑋𝑈𝑈 = {𝑥𝑥𝑈𝑈𝑖𝑖 }
𝑁𝑁𝑈𝑈
𝑖𝑖𝑖𝑖 . Each 𝑥𝑥𝑈𝑈𝑖𝑖  is an unlabeled sentence, and 𝑁𝑁𝑈𝑈 is the total
count of unlabeled samples. The setup of the off-policy PPO model for the first agent is outlined below:
 ● State: At each time step, the agent observes its environment via a state vector that encodes key, informative
attributes. The state includes two parts: feature outputs 𝑓𝑓𝑈𝑈𝑡𝑡  from the LSTM module of the second agent and a
prediction score 𝑝𝑝𝑐𝑐𝑐𝑐𝑐𝑐(𝑥𝑥𝑈𝑈𝑡𝑡 ) derived from the second agent. These two parts form a sequence of state descriptions
𝑆𝑆𝑆 {𝑠𝑠𝑡𝑡}. Each element in this sequence is written as 𝑠𝑠𝑡𝑡 = (𝑓𝑓𝑈𝑈𝑡𝑡 ,𝑝𝑝 𝑐𝑐𝑐𝑐𝑐𝑐(𝑥𝑥𝑈𝑈𝑡𝑡 )), where 𝑡𝑡 denotes the current time step.
 ● Action: The set of possible actions determines whether a sample is sent for manual annotation; it is expressed
as 𝐴𝐴𝐴 {0, 1}. If the agent selects 𝑎𝑎𝑡𝑡 =1 , the sample 𝑥𝑥𝑈𝑈𝑡𝑡  is sent to a human annotator for labeling. The updated
label is then added to the labeled data pool. This AL loop continues until either every sample has been handled
or the annotation budget has been fully utilized.
 ● Reward: The reward function plays a central role in evaluating the agent. Traditional strategies often provide
feedback only after the entire sequence finishes. In contrast, this method delivers a reward immediately after
each action. This immediate feedback strengthens the connection between each action and its long-term effect.
The reward signal is defined under two main scenarios:
 ● When the agent opts to annotate a sample ( 𝑎𝑎𝑡𝑡 =1 ): a small penalty of −𝜀𝜀 is applied. Formally, this is written
as 𝑅𝑅 (𝑠𝑠𝑡𝑡,𝑎𝑎 𝑡𝑡) =− 𝜀𝜀. This penalty discourages unnecessary labeling and supports the efficient use of annotation
resources.
 ● When the agent decides not to annotate ( 𝑎𝑎𝑡𝑡 =0 ): let mc represent the centroid of feature vectors for class c,
calculated as:

𝑚𝑚𝑐𝑐 = 1 𝑛𝑛𝑐𝑐 ∑ 𝑖𝑖∈𝜋𝜋𝑐𝑐 𝑓𝑓𝑖𝑖 (13)
In this setting, 𝑛𝑛𝑐𝑐 is the number of elements in the set 𝜋𝜋𝑐𝑐. The set 𝜋𝜋𝑐𝑐 stores the indices of samples linked to class 𝑐𝑐.
The centroid of each class is then used to compute the entropy-based loss for every unlabeled sample:

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4

𝐿𝐿 (𝑥𝑥𝑈𝑈𝑡𝑡 ,𝑐𝑐 ) =−
𝐶𝐶
∑
𝑗𝑗𝑗𝑗
𝑒𝑒
−(𝑓𝑓𝑋𝑋𝑈𝑈𝑡𝑡 − 𝑚𝑚𝑐𝑐𝑗𝑗 )2
∑
𝐶𝐶
𝑗𝑗𝑗𝑗 𝑒𝑒
−(𝑓𝑓𝑋𝑋𝑈𝑈𝑡𝑡 − 𝑚𝑚𝑐𝑐𝑗𝑗 )2 log 𝑒𝑒
−(𝑓𝑓𝑋𝑋𝑈𝑈𝑡𝑡 − 𝑚𝑚𝑐𝑐𝑗𝑗 )2
∑
𝐶𝐶
𝑗𝑗𝑗𝑗 𝑒𝑒
−(𝑓𝑓𝑋𝑋𝑈𝑈𝑡𝑡 − 𝑚𝑚𝑐𝑐𝑗𝑗 )2  (14)
In this formulation, 𝑓𝑓𝑈𝑈𝑖𝑖  denotes the feature vector of the -th unlabeled sample, obtained from the LSTM network.
The reward, in the case where ai = 0, is determined as follows:

𝑅𝑅 (𝑠𝑠𝑡𝑡,𝑎𝑎 𝑡𝑡) = { 1, 𝐿𝐿 (𝑥𝑥𝑈𝑈𝑡𝑡 ,𝑐𝑐 ) < 𝛾𝛾 −1, 𝐿𝐿 (𝑥𝑥𝑈𝑈𝑡𝑡 ,𝑐𝑐 ) > 𝛾𝛾  (15)
In this setting, 𝐿𝐿 (𝑥𝑥𝑈𝑈𝑡𝑡 ,𝑐𝑐 ) denotes the entropy-based loss for the unlabeled input 𝑥𝑥𝑈𝑈𝑡𝑡 . The parameter 𝛾𝛾 is a dynamic
threshold that adjusts as the model gains classification ability. When the entropy loss of a sample is lower than
𝛾𝛾, it indicates low confidence in the sample. In this case, a reward of + 1 is assigned to encourage annotation of
uncertain samples. If the entropy loss is higher than 𝛾𝛾, it indicates that the model is confident in its prediction.
These instances are excluded from labeling, and a penalty of − 1 is applied to conserve annotation resources and
prevent unnecessary labeling.
Figure 2 illustrates how the reward mechanism affects annotation decisions, as per Eq. 15. The plot displays
individual samples, where indices are placed on the x-axis and entropy loss values are shown on the y-axis. The
threshold 𝛾𝛾 is illustrated as a dashed red line. It indicates whether a sample will be selected for labeling. Samples
below this line, shown in blue, are considered uncertain. They receive a + 1 reward to promote their annotation.
Samples above the line, shown in yellow, represent confident predictions. These are penalized with a reward
of − 1 to avoid wasting annotation resources on clear cases.
The reward scheme in Eq. 15 differs from conventional methods that use fixed uncertainty thresholds. Instead
of relying on static criteria, it adapts as training advances. In the early stages, when accuracy is low, the threshold
𝛾𝛾 is kept small to reflect limited confidence in the extracted features. As training progresses, 𝛾𝛾 increases to show
greater confidence in the learned patterns of the model. This adaptive process helps focus annotation on the most
useful samples, making better use of labeling resources.
The policy mechanism, which serves as the decision unit of the AL framework, is implemented using two
fully connected (FC) layers. The output is a two-dimensional vector. Each element represents one of the possible
actions: 𝑎𝑎𝑡𝑡 =0  or 𝑎𝑎𝑡𝑡 =1 . The action with the larger score is selected by the agent. Training starts with the construc-
tion of a tuple (𝑠𝑠𝑡𝑡,𝑎𝑎 𝑡𝑡,𝑟𝑟𝑡𝑡,𝑠𝑠 𝑡𝑡𝑡𝑡). This tuple records the chosen action, the reward received, and the transition to the
next state.
Fig. 2 Annotation strategy driven
by reward signals, where entropy
thresholds guide the decision to
label samples in the recommenda-
tion framework.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
Input: = , , , ,… , , : set of labeled samples, =
, , , ,… , , : set of unlabeled samples, : learning rate
Output: The optimal policy for sample selection
Establish the annotation limit or the maximum number of labeling actions permitted
Create an empty memory container to accumulate interaction records
Begin training the classifier using the labeled samples from
While until a stopping criterion is met:
Randomize the sequence of to ensure unbiased selection
For in :
Produce feature representation: = LSTM ( )
Calculate the sentiment class label ( ) using the SA agent
Formulate the state:  =( , ( ))
Select action based on the current policy
If == 1:
Annotate the sample to obtain label
Incorporate ( , ) into
Assign a labeling penalty as a reward: = −
Re-train the second agent with the updated labeled dataset
Else:
Calculate reward using the predefined method (Equation 15)
Record experience tuple ( , , , ) into
If annotation budget is used up:
Initiate the termination protocol
Exit the loop
Sample tuple ( , , , ) from
Update the policy using off-policy PPO (Equation 43):
← + × ( )
Return the optimal policy
Algorithm 4 Pseudocode for the proposed AL model.
Algorithm 4 outlines the proposed AL strategy based on the off-policy PPO framework. The algorithm starts
with a labeled dataset (𝑋𝑋𝐿𝐿) and an unlabeled dataset (𝑋𝑋𝑈𝑈). It also initializes the policy network, value function, and
advantage estimator. At each iteration, the unlabeled samples are randomly shuffled to avoid selection bias. For
each candidate sample, an LSTM encoder extracts feature representations. The SA agent then estimates the prob-
abilities of the sentiment classes. These outputs are combined to construct the state representation used by the
PPO policy. Based on the current policy, the agent decides whether the sample should be selected for annotation.
If the sample is selected, it is labeled and added to the labeled dataset. The second agent is then retrained using
the expanded training set. A labeling penalty is assigned to discourage unnecessary annotations and promote
sample-efficient learning. Otherwise, the reward is computed according to the predefined reward function. The
algorithm continuously updates the advantage estimates and refines the policy using off-policy PPO. This itera -
tive process continues until the annotation budget is exhausted. The result is an optimized policy that identifies
the most informative samples for sentiment classification.
Agent 2: feature selection and SA
The second agent serves as the feature selection and sentiment classification component. Using the labeled data-
set 𝑋𝑋𝐿𝐿, the agent learns to assign a sentiment category to each input sequence. During every training iteration,
a sample 𝑥𝑥𝐿𝐿𝑡𝑡  is randomly drawn from 𝑋𝑋𝐿𝐿. As illustrated in Fig. 1, GPT first provides contextual embeddings for
the sequence. The LSTM network then processes these embeddings to generate a feature representation. The
extracted representation is subsequently fed into an MLP. The MLP carries out two tasks simultaneously. First, it
identifies the most informative elements within the input sequence. Second, it predicts the corresponding senti -
ment category. The output layer produces a vector of size 𝐶𝐶𝑆𝑆 +𝑚𝑚 . The first 𝐶𝐶𝑆𝑆 elements correspond to the predicted
sentiment classes: positive, negative, and neutral. The remaining 𝑚𝑚 elements represent feature-importance scores
derived from the MLP outputs. These scores improve interpretability by showing which features contribute most

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
to the final decision. In the off-policy PPO framework, the agent interacts with the environment using predefined
states, actions, and rewards. These elements are defined as follows:
 ● State: At step 𝑡𝑡, the state 𝑠𝑠𝑡𝑡 represents the information available to the agent from its surroundings. It is con -
structed using three components. The first component is the sequence-level representation extracted by the
LSTM from 𝑥𝑥𝐿𝐿𝑖𝑖 . The second component consists of the feature importance scores generated by the MLP . The
final component is 𝑦𝑦𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎. It includes features that have already been identified as relevant to SA. By combining
these sources of information, the state provides a comprehensive description of the current learning situation.
This representation helps the agent make informed decisions at each stage. It also reduces the need for repeated
feature selection and supports SA.
 ● Action and reward: The action space is divided into two categories. The first category, denoted by 𝐴𝐴𝑓𝑓, is re-
sponsible for identifying informative features that enhance model interpretability. The second category 𝐴𝐴𝑐𝑐
focuses on determining the sentiment class of the input sequence. When the agent selects an action from 𝐴𝐴𝑓𝑓
, the corresponding feature is incorporated into the active feature set. This updated set is subsequently used
during future classification stages. The reward for feature selection depends on the feature relevance score es-
timated by LIME. Before reward computation, the LIME importance scores are normalized to the range [0,1]
as follows:

𝐿𝐿𝐿𝐿𝐿𝐿𝐿𝐿 𝑛𝑛𝑛𝑛𝑛𝑛𝑛𝑛 (𝑓𝑓𝑖𝑖) = |𝐿𝐿𝐿𝐿𝐿𝐿𝐿𝐿 (𝑓𝑓𝑖𝑖) | max
𝑗𝑗
|𝐿𝐿𝐿𝐿𝐿𝐿𝐿𝐿 (𝑓𝑓𝑗𝑗) |  (16)
where 𝑓𝑓𝑖𝑖 denotes the -th feature and |.| denotes the absolute value operator. Since LIME values may vary in mag-
nitude and can be either positive or negative, absolute values are first computed and then scaled by the maximum
absolute LIME score within the current sample. This normalization ensures a consistent reward scale and pre -
vents large feature-importance values from dominating the policy update process.
The formulation of reward for feature selection is presented below:
 𝑟𝑟 ((𝑥𝑥𝐿𝐿𝑡𝑡 ,𝑦𝑦 𝐿𝐿𝑡𝑡 ) ,𝑎𝑎 ∈ 𝐴𝐴𝑓𝑓 ) = 𝜆𝜆 × 𝐿𝐿𝐿𝐿𝐿𝐿𝐿𝐿 𝑛𝑛𝑛𝑛𝑛𝑛𝑛𝑛 (𝑓𝑓𝑏𝑏𝑏𝑏𝑏𝑏𝑡𝑡) (17)
In this formulation, 𝜆𝜆 acts as a regularization parameter that penalizes excessive model complexity. The vari -
able 𝑓𝑓𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 denotes the feature assigned the largest importance score by the MLP during the prediction process.
This reward mechanism encourages selecting highly influential features while using LIME-based explanations
for guidance. Consequently, the agent gradually learns which inputs have the strongest impact on SA outcomes.
Policy refinement is performed iteratively through the off-policy PPO algorithm using the received reward sig -
nals. Over time, the agent captures informative patterns and exploits this knowledge in subsequent decisions. This
learning strategy improves both prediction accuracy and model interpretability.
The reward function used for the SA task is defined as follows:

𝑟𝑟 ((𝑥𝑥𝐿𝐿𝑡𝑡 ,𝑦𝑦 𝐿𝐿𝑡𝑡 ) ,𝑎𝑎 ∈ 𝐴𝐴𝑐𝑐) =
⎧{
⎨{⎩
+1𝑖𝑖𝑖𝑖𝑦𝑦𝐿𝐿𝑡𝑡 ∈ 𝐷𝐷𝑂𝑂,𝑦𝑦 𝐿𝐿𝑡𝑡 = ̂𝑦𝑦𝐿𝐿𝑡𝑡
−1𝑖𝑖𝑖𝑖𝑦𝑦𝐿𝐿𝑡𝑡 ∈ 𝐷𝐷𝑂𝑂,𝑦𝑦 𝐿𝐿𝑡𝑡 ≠ ̂𝑦𝑦𝐿𝐿𝑡𝑡
+𝛾𝛾𝑖𝑖𝑖𝑖𝑦𝑦𝐿𝐿𝑡𝑡 ∈ 𝐷𝐷𝑁𝑁,𝑦𝑦 𝐿𝐿𝑡𝑡 = ̂𝑦𝑦𝐿𝐿𝑡𝑡
−𝛾𝛾𝑖𝑖𝑖𝑖𝑦𝑦𝐿𝐿𝑡𝑡 ∈ 𝐷𝐷𝑁𝑁,𝑦𝑦 𝐿𝐿𝑡𝑡 ≠ ̂𝑦𝑦𝐿𝐿𝑡𝑡
 (18)
The minority class is written as 𝐷𝐷𝑂𝑂, and the majority class is written as 𝐷𝐷𝑁𝑁. The term ̂𝑦𝑦𝐿𝐿𝑡𝑡  refers to the predicted
label of sample 𝑥𝑥𝐿𝐿𝑡𝑡 . In this setup, the reward system gives more credit for correct decisions on minority data than
on majority data. This pushes the model toward less frequent cases and reduces its tendency to favour common
patterns. The TRPO method updates the policy in an online way using signals from these rewards. Through this
process, the model learns the features that help to distinguish minority samples from the larger group. Over time,
this continuous refinement helps the system perform better on both rare and common occurrences.
The evolution of the system between states is governed by a transition mechanism denoted as 𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡 ∪ 𝑇𝑇.
This mechanism specifies how the current state changes after an action is executed. It determines the relationship

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
between the decision of the agent and the resulting state of the environment. The transition procedure used in this
study is described in detail below:

𝑡𝑡 ((𝑥𝑥𝑥 𝑥𝑥) 𝑥𝑎𝑎 ) = { 𝑇𝑇𝑇𝑇𝑇𝑇𝑎𝑎 ∈ 𝐴𝐴𝑐𝑐 (𝑥𝑥𝑥 𝑥𝑥 ∪ 𝑎𝑎) 𝑇𝑇𝑇𝑇𝑎𝑎 ∈ 𝐴𝐴𝑓𝑓  (19)
In this formulation, 𝑇𝑇 denotes the termination point of an episode. When the selected action belongs to the
feature-selection set 𝑎𝑎 ∈ 𝐴𝐴𝑓𝑓 , the corresponding feature is incorporated into the active feature collection. Alterna -
tively, if the chosen action comes from 𝐴𝐴𝑐𝑐, the agent predicts the class label of the input sequence and concludes
the current episode. The learning process then proceeds with another sample. At each decision step 𝑡𝑡, the agent
evaluates a candidate feature using LIME-derived information. Repeated interactions gradually produce a refined
subset of features associated with SA-related behavior. These features are subsequently utilized during the final
classification stage. Unlike conventional methods that perform prediction in a single operation, the proposed
framework follows a sequential decision process. Multiple decision steps are performed before reaching the final
output. This design improves transparency and enables the model to support its predictions with informative,
interpretable features.
Input: X = ( , ), ( , ),…,( , ) :l abeled dataset for SA, :t otal number of training epochs
Output: Optimized policy for SA
Assign random initial values to the parameters of the policy
Initialize an empty replay memory for storing agent experiences
For =1 to E:
Randomly reorder the samples in to minimize sequence-related bias
for each instance in X :
Create an empty active feature collection: =∅
Extract contextual representations from using the LSTM encoder
Pass the extracted representation to an MLP to obtain feature relevance and sentiment predictions scores
While until the episode reaches its stopping condition:
Construct the current state = (embedding, features cores, )
Choose an action from the action space A= ∪
If ∈ :
Determine the feature associated with the selected action
Expand the active feature set: = ∪
Evaluate the reward according to the LIME-based criterion in Equation 17
Set _ =
Else:
Predict the sentiment category using the current state
Calculate the reward according to Equation 18
Set _ =
Generate the next state using the updated active feature set and revised model outputs
Record experience tuple ( , , , ) into
If == :
Terminate the current episode and continue with the next training sample
Sample tuple ( , , , ) from
Update the policy using off-policy PPO (Equation 43):
← + × ( )
Return the final learned policy
Algorithm 4 Pseudocode for feature selection for SA using off-policy PPO.
Algorithm 5 presents the feature selection and sentiment classification procedure based on the off-policy PPO
framework. The algorithm begins by initializing the policy network and replay memory. During each training
epoch, the labeled dataset is randomly shuffled to reduce potential bias caused by sample ordering. For each input
review, the LSTM encoder extracts contextual information. The MLP then generates sentiment predictions and
feature relevance scores. The agent then interacts with the environment through a sequence of decisions. At each
step, it can either select a feature or perform sentiment classification. When the agent selects a feature-selection
action, the chosen feature is added to the active feature set. The reward is then calculated using the LIME-based
importance score. This encourages the agent to identify informative features. When the classification action is

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
selected, the episode terminates, and the classification reward is calculated. All interactions are stored in the
replay memory. Finally, the policy is updated using off-policy PPO, allowing the agent to learn an effective strat-
egy for both feature selection and sentiment prediction.
Hyperparameter optimization
This study applies the BOHB method to adjust the hyperparameters of the proposed framework. BOHB is par -
ticularly suitable because it combines probabilistic modeling and efficient resource allocation. This makes it more
effective than traditional tuning methods. Grid search evaluates all parameter combinations and is computation -
ally expensive in high-dimensional spaces. In contrast, BOHB focuses only on promising regions and reduces
unnecessary evaluations. Compared with random search, BOHB is more sample-efficient because it uses prior
observations to guide the selection of new configurations. Standard BO does not use early stopping. BOHB
integrates the early-stopping strategy of HB to discard weak configurations and allocate resources to better ones.
This hybrid mechanism is especially beneficial for deep learning-based SA models, where training is costly
and hyperparameter interactions are complex. Therefore, BOHB achieves a better balance between exploration,
exploitation, and computational efficiency in the proposed framework.
Table 2 outlines the hyperparameter configuration of the proposed framework, which was tuned using the
BOHB optimization strategy. For every hyperparameter, we determined an appropriate range of values. These
ranges were derived from suggestions made by deep learning studies on SA.
Overal algorithm
Figure 3 shows the end-to-end workflow of the proposed SA–based recommendation framework. The pipeline
begins with text preprocessing, where raw reviews are cleaned and standardized for analysis. This step involves
removing stop-words and applying stemming. These operations reduce word variants to a common root, thereby
improving efficiency and facilitating better generalization.
Best value Ranges Hyperparam-
eterOff-policy PPO Generator Discriminator
AIV (72) and AA (79) AIV (64) and AA (78) AIV (62) and AA
(72)
[16–512] Batch size
AIV (220) and AA (259) AIV (226) and AA
(312)
AIV (215) and AA
(278)
[32–2048] Epoch
AIV (0.001) and AA
(0.0006)
AIV (0.005) and AA
(0.004)
AIV (0.0006) and
AA (0.0002)
[0–1] Learning rate
AIV (0.58) and AA (0.69) AIV (0.52) and AA
(0.58)
AIV (0.46) and
AA (0.54)
[0–1] Dropout rate
AIV (ReLU) and AA
(ReLU)
AIV (ReLU) and AA
(ReLU)
AIV (ReLU) and
AA (ReLU)
{ReLU,
Leaky
ReLU, Tanh,
Sigmoid}
Activation
function
– AIV (0.54) and AA
(0.62)
– [0–1] Retention
probability (q)
AIV (0.29) and AA (0.49) – – [0–1] 𝜀𝜀(Agent 1)
AIV (3) and AA (5) – – [1–8] LSTM layers
(Agent 2)
AIV (4) and AA (5) – – [1–8] MLP layers
(Agent 2)
AIV (0.23) and AA (0.34) – – [0–1] 𝜆𝜆 (Agent 2)
AIV (0.56) and AA (0.48) – – [0–1] 𝛾𝛾(Agent 2)
AIV (0.18) and AA (1.35) – – [0.1–0.3] Clipping
threshold (∈)
Table 2 Overview of the
hyperparameters fine-tuned
in the study, along with their
search ranges and the best
values obtained for each
sub-module.
Values in parentheses indicate
the best-performing setting for
each dataset.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
Next, BOHB is applied to optimize hyperparameters for all major components. RelGANGE is then trained
for online data augmentation. The trained model is saved and later used to generate synthetic samples, thereby
increasing diversity and reducing the risk of overfitting during training. Following this step, Agent 2, responsible
for sentiment classification and feature selection, is trained on the available labeled data.
The framework then enters an iterative loop involving both agents. In each cycle, the trained RelGANGE pro-
duces synthetic reviews conditioned on sentiment labels. Agent 1 employs AL with an off-policy PPO policy to
evaluate both unlabeled customer reviews and RelGANGE-generated samples. For unlabeled reviews, Agent 1
determines whether to select them for annotation and inclusion in the labeled training set. For RelGANGE-gen -
erated samples, Agent 1 evaluates their informativeness and determines whether to include them in the training
set. Once enough new samples have been added to the labeled dataset, Agent 2 is retrained using off-policy PPO
on the updated data. This cooperative cycle of sample generation, sample selection, and sentiment classification
continues until the termination condition is met. Finally, performance is evaluated on the test dataset to confirm
generalization.
Empirical evaluation
This section of the paper introduces the datasets used in the study, highlighting their key properties and their
roles in the experiments. It also explains the evaluation measures adopted to assess the performance of the pro -
posed framework. Additionally, the section presents the results, highlighting the most significant findings from
the model assessments. Moreover, the discussion highlights how these findings align with the research goals and
underscores their broader implications.
Start
Text preprocessing
BOHB for hyperparameter optimization
Augmentation
Train RelGANGE for online data augmentation
Save the trained RelGANGE for augmentation
Use trained RelGANGE to augment a sample
Label a sample if criteria met (Agent 1)
Retrain Agent 2 on batch of new labeled samples using off-policy PPO
Termination?
Assesses performance on test data
End
Yes
Agent 1 and Agent 2
Train Agent 2 on the available labled data
Update Agent 1 using off-policy PPO
No
Add sample to labeled set (if annotated)
Fig. 3 End-to-end workflow of the proposed SA–based
recommendation framework.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
Datasets
To assess the effectiveness of the proposed recommendation framework, three benchmark datasets were utilized:
AIV , AA, and Yelp. These datasets were chosen for their practical significance and the diversity they offer in
evaluating RSs. The AIV and AA datasets are sourced from Amazon and include 22 product review categories
and related metadata, providing rich information for system evaluation. AIV is notable for its high density, where
a focused group of users frequently reviews a small number of items. This structure allows detailed analysis of
user–item relationships while keeping computational demands manageable. These features are useful for test -
ing algorithms in dense interaction settings, especially those based on collaborative filtering. In contrast, the AA
dataset is much larger but sparsely populated, reflecting real-world e-commerce scenarios where most products
receive limited feedback. This sparsity helps evaluate whether a model can detect meaningful patterns with few
interactions, which is vital for solving cold-start problems. The Yelp dataset adds further diversity, including
reviews of restaurants, shops, and services, as well as metadata such as location and business categories. This
variability supports testing model scalability and adaptability in providing personalized recommendations across
different domains. In addition to these benchmark datasets, the Coronavirus Disease 2019 Vaccine Tweets with
Sentiment Annotation (CVT-SA) dataset was used as an external hold-out set. It was used to evaluate both cross-
domain and temporal generalization. Since this dataset was not involved in the primary training and validation
process, its analysis is presented separately in Sect. 4.3.2.
Table 3 highlights the key properties of the datasets used to evaluate recommendation models. The density
metric is the fraction of all possible user–item pairs that contain ratings. It shows how sparse or dense the dataset
is. A higher density means more overlaps between users and items. This typically enhances training and evalua-
tion of collaborative filtering methods that require extensive interaction data.
The AIV dataset, with 5130 users, 1685 items, and 37,126 ratings, has a relatively high density of 0.429%. This
makes it well-suited for benchmarking algorithms that benefit from frequent user–item connections. In contrast,
the AA dataset is significantly larger, comprising 87,271 users and 13,209 items, but has a very low density of
0.065%. This illustrates the data sparsity often observed in large e-commerce systems, where many items receive
only limited feedback. Such sparsity makes it harder to learn robust recommendations. The Yelp dataset, with
12,146 users and 27,774 items at a density of 0.121%, falls between the two extremes. The broad coverage of
interactions across different businesses makes it useful for testing scalability. It also suits models designed to
handle moderate sparsity.
A random 5% subset of each dataset (AIV , AA, and Yelp) was manually inspected to verify the quality and
consistency of sentiment labels. This human-in-the-loop step was used to assess the reliability of the existing
labels for experimental use. Random samples were selected from all three datasets to reduce potential annotation
inconsistencies across different domains. This step increases confidence in the ground-truth labels used during
training and evaluation. Although the datasets are widely used benchmark collections, this additional check pro-
vides further assurance regarding label quality and experimental reliability.
Preprocessing involved two steps: removing stop words from user reviews and item descriptions, and applying
part-of-speech-based tokenization. To reduce noise, any term with a TF-IDF value of 0.5 or less was removed.
The vocabulary was restricted to a maximum of 8000 words. Two thresholds, denoted as 𝑡𝑡𝐴𝐴 and 𝑡𝑡𝐵𝐵, were applied
to regulate the lengths of reviews and their associated documents. These thresholds could vary between users and
Dataset Users Items Ratings Ranges Density (%)
AIV 5130 1685 37,126 [1–5] 0.429
AA 87,271 13,209 752,937 [1–5] 0.065
Yelp 12,146 27,774 408,410 [1–5] 0.121
Table 3 Detail of the AIV ,
AA, and Yelp datasets.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
items, but they were fixed at 0.8 and 0.5 to maintain consistency. Items without ratings were excluded to ensure
analytical reliability.
Metrics
We used four evaluation measures: accuracy, F-measure, geometric mean (G-means), and area under the receiver
operating characteristic curve (AUC). Together, they provide a broad assessment of the RS model. Accuracy pro-
vides a straightforward measure of overall correctness, but it can be misleading in imbalanced datasets. F-mea -
sure balances precision and recall. It demonstrates the ability of the model to identify relevant recommendations
effectively. G-means measures performance across both majority and minority classes. This ensures fairness in
the imbalanced settings common in RS. Finally, AUC measures how well the model ranks recommendations
across different decision thresholds.
SA is a multi-class classification task with three labels: positive, negative, and neutral. Therefore, precision,
recall, and F-measure are computed using a one-versus-rest (OvR) strategy. The results are then macro-averaged
across all classes. In this approach, the evaluation metrics are first calculated separately for each sentiment class,
then averaged with equal weight to avoid bias toward majority classes. This ensures a balanced evaluation across
all sentiment categories. For G-means and specificity, values are computed for each class individually, and the
final score is obtained by averaging across all classes. This provides a more robust measure of performance under
class imbalance conditions. AUC is originally defined for binary classification. In this work, it is extended to the
multi-class sentiment setting using an OvR decomposition strategy. Each class is evaluated against the rest, and
the final result is obtained by averaging the AUC values across all classes.
From a mathematical perspective, the accuracy, F-measure, and G-means evaluation metrics can be expressed
as follows65:

𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴 𝐴 𝑁𝑁𝐴𝐴𝑁𝑁𝑁𝑁𝑁𝑁𝐴𝐴 𝑁𝑁𝑁𝑁 𝐴𝐴𝑁𝑁𝐴𝐴𝐴𝐴𝑁𝑁𝐴𝐴𝑁𝑁𝑁𝑁 𝐴𝐴 𝐴𝐴𝑁𝑁𝐴𝐴𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁 𝑁𝑁𝐴𝐴𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁 𝑇𝑇𝑁𝑁𝑁𝑁𝐴𝐴𝑁𝑁 𝑇𝑇𝐴𝐴𝑁𝑁𝑁𝑁𝑁𝑁𝐴𝐴 𝑁𝑁𝑁𝑁𝑁𝑁𝐴𝐴𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁  (20)
 𝐹𝐹 𝐹 𝐹𝐹𝐹𝐹𝐹𝐹𝐹𝐹𝐹𝐹𝐹𝐹𝐹𝐹 𝐹 𝐹 𝐹 𝑃𝑃𝐹𝐹𝐹𝐹𝑃𝑃𝑃𝑃 𝐹𝐹𝑃𝑃𝑃𝑃𝑃𝑃 𝐹 𝑃𝑃𝐹𝐹𝑃𝑃𝐹𝐹𝑃𝑃𝑃𝑃 𝑃𝑃𝐹𝐹𝐹𝐹𝑃𝑃𝑃𝑃 𝐹𝐹𝑃𝑃𝑃𝑃𝑃𝑃 𝑃 𝑃𝑃𝐹𝐹𝑃𝑃𝐹𝐹𝑃𝑃𝑃𝑃  (21)
 𝐺𝐺 𝐺 𝐺𝐺𝐺𝐺𝐺𝐺𝐺𝐺𝐺𝐺 𝐺 √𝑅𝑅𝐺𝐺𝑅𝑅𝐺𝐺𝑅𝑅𝑅𝑅 𝑅 𝑅𝑅𝑅𝑅𝐺𝐺𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅  (22)
where
 𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃 𝑃 𝑇𝑇𝑃𝑃 𝑇𝑇𝑃𝑃 𝑇 𝑇𝑇𝑃𝑃  (23)
 𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅 𝑅 𝑇𝑇𝑇𝑇 𝑇𝑇𝑇𝑇 𝑇 𝑇𝑇𝑇𝑇  (24)
 𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆 𝑆 𝑇𝑇𝑇𝑇 𝑇𝑇𝑇𝑇 𝑇 𝑇𝑇𝑇𝑇  (25)
where TP denotes true positives, referring to the number of actual positive instances correctly predicted by the
model. TN represents true negatives, which correspond to actual negative cases accurately classified as negative.
FP indicates false positives, meaning negative samples that are incorrectly labeled as positive by the model. FN
refers to false negatives, which are positive samples that the model wrongly classifies as negative.
Results
The study was conducted on a 64-bit version of Windows 11. The experiments used Python 3.10 and PyTorch
1.13.1 as the main deep learning framework. Compute Unified Device Architecture version 11.7 (CUDA 11.7)

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
and cuDNN 8.5 supported graphics processing unit (GPU) acceleration. The hardware setup consisted of an
NVIDIA RTX 3090 GPU with 32 gigabyte (GB) of memory, an Intel Core i9-12900K central processing unit
(CPU), and 64 GB of random-access memory (RAM). The AL and RL modules were built with the Stable-
Baselines3 (SB3) library v1.7.0, which implemented the off-policy PPO algorithm. The LIME v0.2.0.1 package
was used for feature interpretability, while scikit-learn v1.2.2 provided preprocessing utilities, evaluation metrics,
and baseline comparisons. RelGANGE developed in TensorFlow 2.11 to exploit its sequence modeling features.
Hyperparameter optimization was performed using the HpBandSter v0.7.4 library with BOHB. Text preprocess-
ing tasks, such as cleaning and tokenization, were managed with NLTK v3.8.1 and spaCy v3.5. Experiments were
logged and tracked with Weights & Biases (wandb v0.15) to ensure reproducibility and visualization.
To further evaluate the robustness of the proposed framework, 5-fold cross-validation was employed. In this
setup, the dataset is divided into five mutually exclusive folds. The model is trained and tested five times. In
each iteration, one fold is used for testing while the remaining folds are used for training. This procedure reduces
the dependency on a single random split and provides a more reliable estimate of model performance. The
final results are reported as mean ± standard deviation across the five folds. The standard deviation indicates the
variation in performance across different train-test partitions. Importantly, care was taken to ensure no overlap
between training and testing samples within each fold, thereby preventing data leakage.
For benchmarking, the model was evaluated against five conventional baselines (LSTM-WEA 37, SA-
HRM39, LSTM-CBOW4, SNCF41, and SA-CF45) as well as ten transformer-driven approaches (DNN-BERT 47,
RoBERTa49, BERT-CB50, BERT-SA52, Transformer-RS54, GPT-3.555, AttriBERT59, XLNet 61, MBT4R 62, and
HAN-RS63). To ensure fairness in the comparison, the hyperparameter values for these advanced baselines were
taken directly from their respective publications. The performance outcomes of these models, tested on the AIV
and AA datasets, are presented in detail in Tables 4 and 5.
The proposed model outperforms all state-of-the-art baselines on both datasets, with clear performance mar -
gins. On the AIV dataset, it exceeds HAN-RS (the strongest baseline) by 5.3% in accuracy, 5.6% in F-measure,
5.6% in G-means, and 4.4% in AUC. Against MBT4R, the gains are 5.2% in accuracy, 6.4% in F-measure, 6.4%
in G-means, and 5.4% in AUC. Compared to XLNet, improvements are achieved in accuracy by 5.9%, F-measure
by 8.0%, G-means by 7.9%, and AUC by 6.3%. Over AttriBERT, the margins are 7.3% in accuracy, 9.7% in
F-measure, 9.2% in G-means, and 7.9% in AUC. Relative to GPT-3.5, the improvements are 9.0% in accuracy,
10.3% in F-measure, 10.3% in G-means, and 8.8% in AUC. The same trend holds against other baselines: the
proposed model surpasses Transformer-RS by 10.5% in accuracy, BERT-SA by 11.8%, BERT-CB by 12.5%,
Model Accuracy F-measure G-means AUC
LSTM-WEA37 71.533 ± 0.083 71.998 ± 0.031 72.743 ± 0.056 0.617 ± 0.083
SA-HRM39 73.124 ± 0.089 73.448 ± 0.095 74.109 ± 0.022 0.626 ± 0.003
LSTM-CBOW4 73.808 ± 0.044 74.544 ± 0.021 75.167 ± 0.068 0.641 ± 0.024
SNCF41 75.025 ± 0.035 75.234 ± 0.027 75.853 ± 0.092 0.647 ± 0.058
SA-CF45 76.271 ± 0.058 76.232 ± 0.005 76.836 ± 0.042 0.662 ± 0.057
DNN-BERT47 79.309 ± 0.010 78.641 ± 0.067 79.226 ± 0.081 0.684 ± 0.019
RoBERTa49 80.435 ± 0.006 79.717 ± 0.033 80.344 ± 0.072 0.699 ± 0.024
BERT-CB50 82.219 ± 0.085 81.416 ± 0.100 82.029 ± 0.086 0.717 ± 0.040
BERT-SA52 82.940 ± 0.032 82.333 ± 0.058 82.969 ± 0.009 0.732 ± 0.073
Transformer-RS54 84.179 ± 0.098 83.927 ± 0.086 84.555 ± 0.052 0.738 ± 0.061
GPT-3.555 85.643 ± 0.092 84.823 ± 0.064 85.488 ± 0.077 0.750 ± 0.088
AttriBERT59 87.423 ± 0.027 85.855 ± 0.025 86.563 ± 0.097 0.759 ± 0.086
XLNet61 88.839 ± 0.015 87.189 ± 0.013 87.838 ± 0.044 0.775 ± 0.066
MBT4R62 89.446 ± 0.006 88.714 ± 0.044 89.345 ± 0.083 0.784 ± 0.076
HAN-RS63 89.962 ± 0.064 89.530 ± 0.094 90.139 ± 0.094 0.794 ± 0.016
Proposed 94.723 ± 0.024 95.163 ± 0.034 95.788 ± 0.068 0.838 ± 0.004
Table 4 Comparative perfor-
mance metrics of traditional,
transformer and proposed
models on the AIV dataset.
All results are reported as
mean ± standard deviation over
the five cross-validation folds.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
RoBERTa by 14.3%, and DNN-BERT by 15.4%. Even compared with the best traditional model (SA-CF), it
delivers a 24% increase in accuracy and a 21% boost in AUC.
On the AA dataset, the margins are larger. Against HAN-RS, the proposed model improves accuracy by 5.3%,
F-measure by 6.0%, G-means by 5.9%, and AUC by 6.3%. Over MBT4R, the gains are 6.6% in accuracy, 7.9%
in F-measure, 7.9% in G-means, and 7.5% in AUC. Compared to XLNet, the gaps are 7.9% in accuracy, 7.8%
in F-measure, 8.0% in G-means, and 9.2% in AUC. AttriBERT achieves 9.6% accuracy, 8.7% F-measure, 8.6%
G-means, and 10.3% AUC. Against GPT-3.5, the improvements are 11.3% in accuracy, 11.0% in F-measure,
9.8% in G-means, and 12.0% in AUC. The margins continue with Transformer-RS (12.6% accuracy), BERT-SA
(13.4% accuracy), BERT-CB (14.1% accuracy), RoBERTa (15.8% accuracy), and DNN-BERT (16.3% accuracy).
The strength of the proposed system lies in its integration of components that address long-standing challenges
in sentiment-driven recommendation. The two-agent off-policy PPO architecture improves sample efficiency
through AL. It also enhances the representation of minority classes with adaptive rewards. This dynamic learning
process avoids the static limitations of heuristic-based methods used in traditional and even transformer-based
pipelines. The use of LIME provides fine-grained, interpretable feature selection, ensuring relevant attributes are
emphasized without overfitting to dominant patterns. RelGANGE expands the training data with stable, diverse
synthetic samples, directly combating sparsity while avoiding the mode collapse seen in standard GANs. BOHB
hyperparameter optimization strikes a balance between exploration and exploitation, enabling efficient tuning
across high-dimensional parameter spaces. Together, these innovations explain why the proposed framework
surpasses advanced baselines such as HAN-RS and XLNet. The gains include higher accuracy and greater robust-
ness across both dense (AIV) and sparse (AA) datasets.
To test whether our proposed model statistically outperforms existing models, we used paired t-tests on the
results in Tables 4 and 5. The p-values were calculated for each comparison across all four metrics (Accuracy,
F-measure, G-means, AUC). For the AIV dataset, differences between our model and SA-CF (the strongest tra -
ditional baseline) were highly significant, with p-values < 0.001 across all metrics. Cohen’s d values were above
1.2, showing a huge effect size. The 95% confidence intervals excluded zero and ranged from about [0.85, 1.43].
In comparison to HAN-RS (the strongest transformer baseline), the model also demonstrated significant gains.
P-values were < 0.01, Cohen’s d ranged from 0.8 to 1.0, and confidence intervals were [0.62, 1.18]. On the AA data-
set, the results were even stronger. Compared to SA-CF, the proposed model achieved p-values < 0.001, Cohen’s
d well above 1.3, and confidence intervals around [0.91, 1.55], reflecting substantial effects. Against HAN-RS,
the model again showed significant gains, with p-values < 0.01, Cohen’s d > 0.9, and confidence intervals rang -
ing from [0.70, 1.25]. These results confirm that the superiority of the proposed model over both traditional and
Model Accuracy F-measure G-means AUC
LSTM-WEA37 72.568 ± 0.052 72.732 ± 0.033 73.561 ± 0.079 0.635 ± 0.076
SA-HRM39 73.523 ± 0.097 73.948 ± 0.098 74.733 ± 0.017 0.644 ± 0.066
LSTM-CBOW4 74.254 ± 0.058 75.262 ± 0.000 76.060 ± 0.010 0.655 ± 0.011
SNCF41 75.731 ± 0.016 76.881 ± 0.055 77.659 ± 0.028 0.664 ± 0.013
SACF45 76.515 ± 0.021 77.737 ± 0.096 78.497 ± 0.087 0.677 ± 0.048
DNN-BERT47 79.903 ± 0.052 79.895 ± 0.033 80.643 ± 0.077 0.709 ± 0.077
RoBERTa49 80.480 ± 0.005 81.275 ± 0.090 82.033 ± 0.073 0.723 ± 0.070
BERT-CB50 82.099 ± 0.047 82.511 ± 0.011 83.318 ± 0.021 0.740 ± 0.021
BERT-SA52 82.884 ± 0.015 83.075 ± 0.039 83.871 ± 0.048 0.748 ± 0.085
Transformer-RS54 83.687 ± 0.041 84.340 ± 0.041 85.186 ± 0.002 0.754 ± 0.051
GPT-3.555 84.906 ± 0.076 85.633 ± 0.046 86.413 ± 0.034 0.762 ± 0.082
AttriBERT59 86.667 ± 0.078 86.875 ± 0.017 87.636 ± 0.075 0.779 ± 0.015
XLNet61 88.326 ± 0.090 87.768 ± 0.002 88.484 ± 0.008 0.790 ± 0.036
MBT4R62 89.641 ± 0.029 88.790 ± 0.017 89.541 ± 0.070 0.807 ± 0.014
HAN-RS63 90.941 ± 0.089 89.591 ± 0.051 90.350 ± 0.036 0.819 ± 0.066
Proposed 96.241 ± 0.035 95.580 ± 0.069 96.220 ± 0.091 0.882 ± 0.059
Table 5 Comparative perfor-
mance metrics of traditional,
transformer and proposed
models on the AA dataset.
All results are reported as
mean ± standard deviation over
the five cross-validation folds.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
transformer baselines is consistent and statistically significant across datasets. For all other models, p-values
were < 0.01, Cohen’s d ranged from 0.7 to 1.4, and 95% confidence intervals stayed within [0.60, 1.50].
Table 6 compares the computational efficiency of the proposed model with traditional, lightweight, and trans-
former-based baselines on the AIV and AA datasets. The comparison is based on parameter count, training time,
GPU memory usage, floating point operations (FLOPs), and inference time. Parameter counts were obtained from
the model implementations used in the experiments and correspond to the number of trainable parameters for
each architecture. On the AIV dataset, the proposed model achieves the best predictive performance reported in
Table 4 while maintaining competitive computational efficiency. The model requires only 10.128M parameters,
which is 48.41% fewer than HAN-RS and 47.34% fewer than XLNet. GPU memory consumption is reduced by
18.01% compared with HAN-RS, while FLOPs are 49.88% lower. In addition, the training time is 9.57% shorter
than HAN-RS. The inference time is 18.105 ms. This represents a 25.40% reduction compared with HAN-RS.
It is also lower than the inference times of RoBERTa, XLNet, and GPT-3.5. Compared with lightweight archi -
tectures such as LSTM-WEA and SA-HRM, the proposed framework requires moderately higher computational
resources. However, this additional cost is relatively small when considering the performance improvements
reported in Table 4.
A similar pattern is observed on the AA dataset. The proposed framework uses nearly 48% fewer parameters
than HAN-RS while reducing GPU memory consumption by 18.74% and FLOPs by 39.14%. The training time
is also 3.28% lower than HAN-RS. The inference time on the AA dataset is 26.219 ms. This value is lower
than those of RoBERTa (29.296 ms), BERT-CB (33.164 ms), and Transformer-RS (28.579 ms). However, it is
slightly higher than that of some lightweight architectures. Compared with transformer-based approaches such
as RoBERTa, XLNet, and BERT-SA, the proposed model consistently requires fewer computational resources
while maintaining superior predictive performance. Although lightweight methods such as LSTM-WEA and SA-
HRM exhibit lower computational requirements in some metrics, they achieve considerably lower classification
performance. Therefore, the proposed framework achieves a favorable trade-off between efficiency and effec -
tiveness. Compared with lightweight models, it delivers substantially higher predictive performance with only
a moderate increase in computational cost. Compared with transformer-based models, the proposed framework
Table 6 Computational efficiency comparison of traditional, transformer and proposed models across the AIV and AA data-
sets.
Model Parameter
count (M)
AIV AA
Training
time (s)
GPU (GB) FLOP (×𝟏𝟏𝟏𝟏𝟏𝟏𝟏𝟏 ) Inference
time (ms)
Training
time (s)
GPU (GB) FLOP (×𝟏𝟏𝟏𝟏𝟏𝟏𝟏𝟏 ) Infer-
ence
time
(ms)
LSTM-WEA37 8.152 1771 15.869 1.041 16.356 2019 18.994 0.620 17.803
SA-HRM39 5.245 1804 16.658 0.507 20.030 2198 18.662 0.626 18.289
LSTM-CBOW4 6.369 1958 16.360 0.633 18.307 2221 16.445 1.187 21.698
SNCF41 7.148 1995 18.700 0.723 19.722 2100 19.060 1.143 20.284
SACF45 8.150 1928 16.053 0.935 21.472 2040 16.973 0.896 17.731
DNN-BERT47 13.260 1764 22.482 2.097 25.894 2650 27.400 2.341 28.916
RoBERTa49 10.302 2059 28.659 1.597 27.889 2491 27.018 1.918 29.296
BERT-CB50 18.749 1612 27.404 2.533 25.732 3173 21.063 1.491 33.164
BERT-SA52 11.652 1597 27.272 1.965 22.219 2927 24.246 1.504 25.888
Transformer-RS54 12.564 1815 22.061 1.702 24.802 2626 27.042 1.727 28.579
GPT-3.555 11.560 1684 21.354 1.526 28.901 2546 24.113 1.715 26.151
AttriBERT59 10.482 1663 23.750 1.468 28.076 2606 21.036 2.571 26.738
XLNet61 19.231 1789 26.162 2.598 27.198 2748 24.563 2.404 27.160
MBT4R62 10.065 1613 24.237 1.483 27.835 2948 20.826 1.422 25.133
HAN-RS63 19.632 2163 21.386 2.510 24.271 2685 24.968 2.583 24.255
Proposed 10.128 1956 17.532 1.258 18.105 2597 20.290 1.572 26.219

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
achieves better predictive performance. At the same time, it uses fewer parameters, consumes less GPU memory,
and requires lower computational complexity.
Figure 4 shows training and validation loss curves across 300 epochs for the AIV and AA datasets. In both
datasets, training and validation losses decrease steadily. The validation curves closely follow the training curves,
indicating that the model does not overfit. The consistent downward trend across epochs reflects stable learning.
By the end of training, the curves flatten. This confirms that the model converges effectively and generalizes well
on both datasets.
Figure 5 shows the scalability of the proposed model on the AIV and AA datasets. Performance is measured
with training data volumes ranging from 20 to 100%. For both datasets, the model exhibits a steady upward tra -
jectory in accuracy, F-measure, and G-means as the training size increases. On AIV , performance increases from
about 55% with 20% of the training data to over 92% at full size. This demonstrates that the model effectively uti-
lizes additional samples. Similar results are observed on AA, where performance improves from approximately
57% to nearly 95% when the full training data is used. This confirms stable learning. The parallel trends across
metrics and datasets show that the model scales smoothly as more data is added. This preserves efficiency and
supports use in large-scale, real-world recommendation tasks.
Figure 6 shows the decision-making time distributions of the proposed model on the AIV and AA datasets
in real-time bidding environments. This highlights the efficiency and suitability of the model for real-time use.
On AIV , decision times are tightly centered around 70 ms, with low variance, indicating stable and predictable
performance. On AA, the distribution shifts slightly higher, averaging around 80 ms. Even so, it remains well
a)                                                                                                  b)
Fig. 5 Scalability of the proposed model across different training sizes on the (a) AIV and (b) AA datasets.

a)                                                                                                 b)
Fig. 4 Training and validation loss curves over 300 epochs on the (a) AIV and (b) AA datasets.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
below the latency thresholds typical of real-time RSs. The narrow spread in both datasets shows robustness and
reliability. This confirms that the proposed model can deliver fast responses for real-time applications.
To enhance the interpretability of our proposed model, we utilized LIME across the AIV and AA datasets.
The results are shown in Fig. 7. In both datasets, sentiment lexicon scores, negations, and TF-IDF scores emerge
as the most influential features, consistently achieving the highest LIME scores. This dominance shows the
need to capture sentiment polarity and intensity. It also highlights how term weighting schemes help distinguish
subtle user opinions. Word frequency and n-grams also contribute strongly. This is especially true in the AA
Fig. 7 Comparative analysis
of feature importance across
the (a) AIV and (b) AA datas-
ets using LIME explanations.

a)                                                                                                       b)
Fig. 6 Distribution of decision-making times for the proposed model across the ( a) AIV and ( b) AA datasets in real-time
bidding environments.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
dataset, where variations in text length and structure make it important to capture local context and frequent co-
occurrences. Part-of-speech tags show moderate importance, emphasizing the role of syntactic cues in shaping
sentiment. Interestingly, features such as emojis, symbols, and subjective measures play a more significant role in
the AIV dataset, where informal reviews rely more heavily on expressive markers. In contrast, product metadata
and review length, although contributing, are less critical compared to lexical and semantic features. Overall, the
consistency of top-ranking features across both datasets shows the robustness of our model. At the same time,
dataset-specific variations confirm its adaptability to different review styles.
Ablation study
In this part of the study, we conducted an ablation analysis by systematically removing individual components of
the proposed framework to assess their contributions. The tested variants included:
 ● Proposed w/o FA: excludes the first agent responsible for AL.
 ● Proposed w/o FS: removes feature selection in the second agent.
 ● Proposed w/o LIME: excludes the use of LIME values for feature selection.
 ● Proposed w/o imbalance classification (IC): removes reward adjustments for minority samples. In this case, the
majority and minority classes are treated equally.
 ● Proposed w/o off-policy PPO: replaces off-policy PPO with a basic RL method.
 ● Proposed w/o RelGANGE: removes RelGANGE for data augmentation.
 ● Proposed w/o BOHB: excludes BOHB from the hyperparameter tuning process.
The results of these comparisons, using the AIV and AA datasets, are summarized in Tables 7 and 8. Removing
the first agent (FA) reduces performance by nearly 13% accuracy on AIV and 14% on AA, confirming the critical
role of AL in sample efficiency. FS has an even greater impact. Without it, accuracy drops by more than 21% on
AIV and over 20% on AA. This indicates that precise feature ranking drives the most significant improvements.
Excluding LIME reduces accuracy by approximately 20% on both datasets. This indicates that interpretable fea-
ture weighting helps prevent noisy attributes from dominating. Similarly, removing IC reduces performance by
18% on AIV and 19% on AA, demonstrating that adaptive rewards for minority classes are essential for fairness.
Model Accuracy F-measure G-means AUC
Proposed w/o FA 82.753 ± 0.068 81.744 ± 0.005 82.567 ± 0.069 0.719 ± 0.025
Proposed w/o FS 75.091 ± 0.051 74.341 ± 0.042 75.191 ± 0.018 0.646 ± 0.081
Proposed w/o LIME 75.668 ± 0.089 75.499 ± 0.005 76.345 ± 0.085 0.656 ± 0.083
Proposed w/o IC 76.743 ± 0.067 77.116 ± 0.097 77.927 ± 0.051 0.662 ± 0.076
Proposed w/o off-policy PPO 78.498 ± 0.096 77.930 ± 0.082 78.782 ± 0.065 0.672 ± 0.072
Proposed w/o RelGANGE 79.735 ± 0.035 79.387 ± 0.072 80.176 ± 0.097 0.685 ± 0.048
Proposed w/o BOHB 84.420 ± 0.033 82.526 ± 0.002 83.322 ± 0.080 0.733 ± 0.054
Full model 96.241 ± 0.035 95.580 ± 0.069 96.220 ± 0.091 0.882 ± 0.059
Table 8 Comparative per-
formance metrics of ablation
studies and the full proposed
model on the AA dataset.
All results are reported as
mean ± standard deviation over
the five cross-validation folds.

Model Accuracy F-measure G-means AUC
Proposed w/o FA 81.509 ± 0.028 81.912 ± 0.086 82.496 ± 0.043 0.706 ± 0.063
Proposed w/o FS 73.221 ± 0.068 74.601 ± 0.096 75.341 ± 0.086 0.638 ± 0.061
Proposed w/o LIME 74.910 ± 0.069 75.515 ± 0.061 76.239 ± 0.087 0.655 ± 0.020
Proposed w/o IC 76.352 ± 0.032 76.698 ± 0.007 77.379 ± 0.011 0.663 ± 0.095
Proposed w/o off-policy PPO 77.363 ± 0.047 77.918 ± 0.072 78.548 ± 0.076 0.676 ± 0.091
Proposed w/o RelGANGE 80.467 ± 0.064 80.762 ± 0.009 81.321 ± 0.053 0.690 ± 0.070
Proposed w/o BOHB 82.267 ± 0.083 83.265 ± 0.085 83.796 ± 0.043 0.719 ± 0.080
Full model 94.723 ± 0.024 95.163 ± 0.034 95.788 ± 0.068 0.838 ± 0.004
Table 7 Comparative per-
formance metrics of ablation
studies and the full proposed
model on the AIV dataset.
All results are reported as
mean ± standard deviation over
the five cross-validation folds.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
Substituting an off-policy PPO with a basic RL method results in a 17% loss in accuracy across datasets. This
confirms that the stability and sample efficiency of PPO are important. The absence of RelGANGE results in a
drop of approximately 14% in accuracy, highlighting the importance of diverse synthetic augmentation. Finally,
removing BOHB yields the smallest drop in accuracy, around 12%. This indicates that hyperparameter tuning
boosts performance but is less critical than FS or IC. Collectively, these comparisons show that FS, IC, and PPO
are the most decisive components, while RelGANGE and FA further reinforce robustness.
The superiority of the proposed model stems from the combined effect of its components, rather than any sin-
gle part. Feature selection, guided by LIME, ensures that the model focuses on the most discriminative attributes
while ignoring irrelevant noise. AL enhances sample efficiency, allowing effective training with fewer labels.
Off-policy PPO contributes stability and efficiency during training, while adaptive IC ensures fair representation
of minority classes. RelGANGE complements this by enriching data diversity, and BOHB fine-tunes parameters
to optimal levels. Together, these mechanisms form a cohesive pipeline. Each component addresses a differ -
ent limitation of state-of-the-art models. This synergy explains why the full model consistently outperforms all
ablated variants across both datasets. It also shows that the model is highly effective in real-world recommenda-
tion scenarios.
To evaluate the robustness of the proposed framework, a detailed statistical comparison was conducted between
the full model and its ablated variants reported in Tables 7 and 8. The significance of performance differences
was assessed using paired t-tests. Effect size analysis and confidence interval estimation were also applied to
support the statistical evaluation. On the AIV dataset, comparisons between the full model and the strongest
ablated configuration (w/o off-policy PPO) revealed statistically significant improvements, with p-values consis-
tently below 0.001 across Accuracy, F-measure, G-means, and AUC. The corresponding 95% confidence inter -
vals were strictly positive, ranging from approximately [0.78, 1.36]. This confirms the consistent superiority of
the full model. Cohen’s d values exceeded 1.1, reflecting a large effect size. Similar trends were observed on the
AA dataset. The full model again outperformed all ablated variants, with p-values < 0.001. Confidence intervals
remained positive within [0.81, 1.44], while Cohen’s d values ranged from 1.0 to 1.3, confirming strong practical
significance. Overall, across both datasets and all comparison settings, statistical tests consistently showed p-val-
ues below 0.01, 95% confidence intervals excluding zero, and Cohen’s d values greater than 0.8. These results
collectively confirm that the proposed framework provides statistically significant and practically meaningful
improvements over all baseline configurations.
Model Accuracy F-measure G-means AUC
LSTM-WEA37 70.538 ± 0.016 70.832 ± 0.049 71.676 ± 0.094 0.636 ± 0.034
SA-HRM39 72.049 ± 0.060 72.360 ± 0.011 73.210 ± 0.040 0.646 ± 0.074
LSTM-CBOW4 73.362 ± 0.049 73.589 ± 0.047 74.446 ± 0.065 0.651 ± 0.021
SNCF41 74.403 ± 0.060 74.604 ± 0.006 75.409 ± 0.030 0.665 ± 0.071
SACF45 75.312 ± 0.019 75.770 ± 0.041 76.523 ± 0.023 0.682 ± 0.061
DNN-BERT47 77.144 ± 0.035 78.269 ± 0.016 78.949 ± 0.077 0.724 ± 0.094
RoBERTa49 78.381 ± 0.088 79.330 ± 0.062 80.020 ± 0.023 0.730 ± 0.009
BERT-CB50 79.964 ± 0.069 80.318 ± 0.051 81.070 ± 0.030 0.737 ± 0.082
BERT-SA52 81.302 ± 0.010 81.198 ± 0.055 81.967 ± 0.021 0.742 ± 0.009
Transformer-RS54 82.640 ± 0.077 82.961 ± 0.083 83.719 ± 0.032 0.754 ± 0.029
GPT-3.555 84.152 ± 0.012 83.764 ± 0.100 84.551 ± 0.100 0.762 ± 0.009
AttriBERT59 85.863 ± 0.099 85.027 ± 0.049 85.818 ± 0.036 0.768 ± 0.026
XLNet61 86.950 ± 0.065 85.857 ± 0.096 86.699 ± 0.023 0.780 ± 0.052
MBT4R62 88.602 ± 0.045 87.201 ± 0.033 87.973 ± 0.028 0.794 ± 0.063
HAN-RS63 89.675 ± 0.019 88.534 ± 0.021 89.233 ± 0.045 0.808 ± 0.007
Proposed 94.175 ± 0.099 93.054 ± 0.019 93.758 ± 0.085 0.847 ± 0.027
Table 9 Comparative perfor-
mance metrics of traditional,
transformer and proposed
models on the Yelp dataset.
All results are reported as
mean ± standard deviation over
the five cross-validation folds.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
Analysis of generalizability
We utilize the Yelp dataset to assess the generalizability of the proposed RS model. The results using this dataset
are shown in Table 9. When compared with traditional baselines, our model demonstrates substantial gains across
all metrics. For instance, compared to the earliest LSTM-WEA approach, the proposed system improves accuracy
by over 23.6% and F-measure by 22.2%. This indicates that simple word embedding aggregation is insufficient to
handle complex sentiment structures. Even advanced hybrids such as SA-HRM and LSTM-CBOW provide only
marginal increases. SNCF and SA-CF integrate collaborative filtering with sentiment knowledge, but their best
results stay below 76% in G-means and 0.70 in AUC. In contrast, our model surpasses SA-CF by 25.1% in accu-
racy, 22.9% in F-measure, 22.5% in G-means, and 24.2% in AUC. This demonstrates that traditional frameworks
struggle to generalize effectively to large, diverse datasets, such as Yelp. Our approach adapts well by balancing
sample efficiency, feature selection, and class imbalance.
Turning to transformer-based baselines, the proposed model also demonstrates a clear advantage, even over
highly optimized architectures. DNN-BERT, RoBERTa, and BERT variants progressively boost accuracy into
the low 80s. However, they struggle with imbalanced data and computational efficiency, which limits improve -
ments in AUC. More advanced approaches, such as GPT-3.5 and AttriBERT, achieve mid-80s accuracy. XLNet
and MBT4R further extend this to 86–88% by utilizing permutation-based training and task-specific optimiza -
tion. HAN-RS achieves the strongest baseline with 89.7% accuracy and 0.808 AUC; however, our model further
extends these results, delivering a 5.0% improvement in accuracy, 5.1% in F-measure, 5.1% in G-means, and
3.9% in AUC. These consistent gains show that transformers excel at capturing contextual semantics. At the same
time, the synergy of our integrated components, including AL, LIME-based feature selection, off-policy PPO,
imbalance handling, RelGANGE augmentation, and BOHB tuning, creates a complementary effect. This not only
enhances raw performance but also ensures generalizability and robustness in real-world recommendation tasks.
To further strengthen the assessment of model generalizability, we additionally evaluate the proposed frame -
work on the CVT-SA dataset, which represents a substantially different application domain from the e-commerce
datasets used during training. Unlike AIV , AA, and Yelp, this dataset contains health-related social media con-
tent characterized by informal language, rapidly evolving terminology, and topic-specific sentiment expressions.
Therefore, it provides a more challenging environment for examining whether the learned representations can
transfer across domains. The CVT-SA dataset consists of COVID-19 vaccination-related tweets labeled with
three sentiment classes: positive, negative, and neutral. In addition to sentiment labels, the dataset provides time-
stamp information for each tweet, making it suitable for temporal evaluation. The dataset captures a wide range
of public opinions across different stages of vaccine-related discussions. It provides a realistic benchmark for
evaluating model robustness beyond the e-commerce domain. This temporal information allows evaluation of
the stability of the model across different stages of public discussion. To investigate both cross-domain and tem-
poral generalization, the dataset was first sorted chronologically according to tweet timestamps and then divided
into two temporally distinct subsets. The first 50% of samples were assigned to the Early-period subset, and the
remaining 50% to the Later-period subset. The model trained on AIV and AA was evaluated separately on the two
subsets to assess robustness under temporal distribution shifts.
The results obtained on the early-period and later-period subsets are reported in Tables 10 and 11, respectively.
The results demonstrate that the proposed framework maintains strong performance under both cross-domain and
temporal distribution shifts. On the early-period subset, the proposed model achieves the highest values across all
evaluation metrics. HAN-RS achieves an Accuracy of 86.887%. The proposed model improves this to 92.599%,
corresponding to a 6.57% gain. Similarly, improvements are observed across all metrics. F-measure increases
by 6.33%, G-means by 6.15%, and AUC by 5.93%. These improvements indicate that the proposed framework
is effective in identifying sentiment patterns during the early stages of vaccine-related discussions. During this
period, opinions are diverse and evolve rapidly. A similar trend is observed on the later-period subset. The pro -
posed framework again outperforms all competing methods, achieving 94.425% Accuracy, 94.981% F-mea -
sure, 95.826% G-means, and 0.849 AUC. Compared with HAN-RS, the proposed model achieves consistent

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
improvements across all metrics. The gains are 6.48% in Accuracy, 5.90% in F-measure, 5.99% in G-means, and
5.86% in AUC.
The consistent gains across both temporal subsets indicate that the proposed framework remains stable despite
changes in public sentiment and discussion topics over time. Transformer-based models such as XLNet, MBT4R,
and HAN-RS effectively capture contextual semantics. However, they do not integrate multiple learning mecha-
nisms such as AL, explainable feature selection, imbalance-aware learning, and synthetic data augmentation,
which are used in the proposed framework. As a result, the proposed model can more effectively identify dis -
criminative sentiment cues and generalize to unseen temporal distributions. These findings provide strong evi -
dence that the framework achieves both cross-domain and temporal generalization, supporting its applicability in
dynamic SA environments.
Model Accuracy F-measure G-means AUC
LSTM-WEA37 69.982 ± 0.033 71.350 ± 0.029 72.893 ± 0.037 0.642 ± 0.089
SA-HRM39 71.571 ± 0.019 72.828 ± 0.094 73.348 ± 0.043 0.649 ± 0.015
LSTM-CBOW4 72.447 ± 0.042 73.345 ± 0.026 84.859 ± 0.076 0.659 ± 0.011
SNCF41 74.085 ± 0.065 75.242 ± 0.044 76.770 ± 0.087 0.662 ± 0.069
SACF45 74.834 ± 0.001 76.332 ± 0.050 77.805 ± 0.053 0.672 ± 0.082
DNN-BERT47 76.379 ± 0.059 77.060 ± 0.071 78.532 ± 0.023 0.711 ± 0.005
RoBERTa49 77.731 ± 0.053 78.913 ± 0.012 79.391 ± 0.021 0.732 ± 0.025
BERT-CB50 78.393 ± 0.009 79.883 ± 0.045 80.695 ± 0.032 0.742 ± 0.090
BERT-SA52 80.146 ± 0.026 81.903 ± 0.080 82.711 ± 0.080 0.749 ± 0.037
Transformer-RS54 81.146 ± 0.003 82.352 ± 0.061 83.146 ± 0.067 0.759 ± 0.091
GPT-3.555 83.906 ± 0.053 84.908 ± 0.018 85.656 ± 0.043 0.762 ± 0.080
AttriBERT59 84.723 ± 0.043 85.790 ± 0.091 86.585 ± 0.061 0.772 ± 0.055
XLNet61 85.853 ± 0.092 86.013 ± 0.097 87.765 ± 0.063 0.782 ± 0.006
MBT4R62 87.000 ± 0.011 88.349 ± 0.039 89.110 ± 0.069 0.792 ± 0.048
HAN-RS63 88.676 ± 0.054 89.691 ± 0.003 90.402 ± 0.076 0.802 ± 0.081
Proposed 94.425 ± 0.033 94.981 ± 0.098 95.826 ± 0.077 0.849 ± 0.052
Table 11 Comparative
performance metrics of
traditional, transformer, and
proposed models on the
later-period subset of the
CVT-SA dataset.
All results are reported as
mean ± standard deviation over
the five cross-validation folds.

Model Accuracy F-measure G-means AUC
LSTM-WEA37 67.103 ± 0.078 68.343 ± 0.012 69.172 ± 0.035 0.626 ± 0.030
SA-HRM39 69.264 ± 0.043 70.360 ± 0.019 71.244 ± 0.020 0.632 ± 0.021
LSTM-CBOW4 70.908 ± 0.022 70.813 ± 0.020 71.917 ± 0.076 0.642 ± 0.026
SNCF41 71.101 ± 0.043 72.296 ± 0.053 73.179 ± 0.050 0.649 ± 0.044
SACF45 72.663 ± 0.040 73.787 ± 0.067 74.622 ± 0.077 0.656 ± 0.069
DNN-BERT47 74.058 ± 0.075 75.109 ± 0.037 76.886 ± 0.091 0.704 ± 0.016
RoBERTa49 75.880 ± 0.099 76.230 ± 0.067 77.016 ± 0.074 0.718 ± 0.070
BERT-CB50 76.165 ± 0.020 77.390 ± 0.060 78.097 ± 0.080 0.729 ± 0.077
BERT-SA52 78.296 ± 0.015 78.516 ± 0.014 79.187 ± 0.059 0.737 ± 0.064
Transformer-RS54 79.951 ± 0.019 80.256 ± 0.043 81.941 ± 0.064 0.745 ± 0.004
GPT-3.555 81.160 ± 0.028 82.267 ± 0.067 83.921 ± 0.094 0.752 ± 0.027
AttriBERT59 82.929 ± 0.055 83.989 ± 0.039 84.632 ± 0.099 0.760 ± 0.074
XLNet61 83.183 ± 0.090 84.024 ± 0.025 85.614 ± 0.069 0.772 ± 0.010
MBT4R62 85.962 ± 0.095 86.905 ± 0.007 87.459 ± 0.069 0.782 ± 0.066
HAN-RS63 86.887 ± 0.030 87.951 ± 0.070 88.513 ± 0.035 0.792 ± 0.027
Proposed 92.599 ± 0.090 93.521 ± 0.099 93.952 ± 0.100 0.839 ± 0.073
Table 10 Comparative
performance metrics of
traditional, transformer, and
proposed models on the
early-period subset of the
CVT-SA dataset.
All results are reported as
mean ± standard deviation over
the five cross-validation folds.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
Analysis of the multi agents
Agent 1 Figure 8 compares the performance of the proposed AL method with three basic strategies, uncertainty
sampling (US), margin-based sampling (MS), and core-set selection (CS), and three advanced approaches: Fisher
Information-based AL (FIAL), RL-based AL (RLAI), and offline RL-based AL (ORLAL). Results are reported
for the AIV and AA datasets. Across both datasets, our method consistently achieves the highest accuracy at all
labeling ratios, demonstrating its effectiveness in leveraging limited labeled data. Traditional heuristics such as
US, MS, and CS show gradual improvements but plateau quickly. They rely on static criteria that fail to adapt
when the distribution of model knowledge changes. Advanced methods, such as FIAL, RLAI, and ORLAL,
achieve stronger results. However, they remain sensitive to sampling inefficiency and make limited use of pre -
viously labeled data. By contrast, the proposed model integrates off-policy PPO. This mechanism dynamically
balances exploration and exploitation while reusing experience. This results in more informative sample selec -
tion, faster convergence, and higher accuracy, even with only 20–40% of the data labeled. Such adaptability
underscores the scalability and robustness of the approach. It makes the method highly suitable for real-world
RSs where labeling resources are scarce.
Figure 9 presents the Kullback–Leibler (KL) divergence trends for the proposed off-policy PPO method and
four baseline RL algorithms (trust-region policy optimization (TRPO), PPO, soft actor-critic (SAC), and standard
RL) over 300 epochs on the AIV and AA datasets. In both datasets, off-policy PPO shows the fastest and most
stable reduction in KL divergence. It converges to significantly lower levels than all other baselines. While TRPO
achieves greater stability than PPO, it converges more slowly, resulting in higher computational costs. SAC main-
tains relatively smooth curves but reduces divergence more slowly. This reflects weaker policy refinement when
samples are limited. Standard RL exhibits the poorest performance, with high divergence values persisting even
after 300 epochs. By contrast, off-policy PPO benefits from reusing past experiences. This enables more efficient
updates and stable convergence. This adaptability enables the model to strike a balance between exploration and
exploitation while maintaining policy stability. It is particularly suitable for real-world SA tasks where robustness
and sample efficiency are critical.
Figure 10 illustrates the cumulative reward trends over 300 training epochs for the AIV and AA datasets, which
reflect the behavior of the proposed off-policy PPO-based AL agent. In the early training stages, both datasets
exhibit negative rewards, reaching their lowest point around epoch 100–120. This initial decline reflects the phase
of exploration. In this stage, the agent experiments broadly to gather informative samples. After this phase, the
cumulative rewards begin to recover. From around epoch 200 onward, the agent shows rapid improvement. This
confirms that it has effectively learned to balance exploration with exploitation. By the end of training, the AA
a)                                                                                                      b)
Fig. 8 Comparison of the proposed AL method with basic and advanced strategies on the (a) AIV and (b) AA datasets.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
dataset achieves a cumulative reward of over 60, while the AIV dataset stabilizes at around 40, indicating robust
but dataset-specific dynamics. The consistent upward trajectories in both cases highlight the ability of the off-
policy PPO mechanism to reuse experience for stable, efficient policy updates. This makes it well-suited for AL
tasks under limited labeling budgets.
Table 12 shows the behavior of the AL agent when selecting samples for annotation, highlighting its effective-
ness in prioritizing informative and uncertain examples. The results show that the off-policy PPO–based AL agent
consistently identifies highly ambiguous reviews, reviews with mixed polarity, or reviews belonging to underrep-
resented sentiment classes. These reviews are the most valuable for improving model performance. For example,
sentences describing damaged packaging or receiving the wrong color are selected with high uncertainty scores
above 0.90. This ensures that critical negative cases, which are often undersampled, are prioritized for labeling.
Similarly, reviews with vague or mixed expressions such as “Average product” or “performance is below expec-
tations” are also chosen, as their unclear tone increases classification difficulty. In contrast, highly confident and
redundant positive sentences, such as “Loved the quality and fast shipping” or “Fantastic service,” are rejected, as
they add little new information to the training set. This balance between exploitation and exploration is achieved
through off-policy PPO. It reuses past experiences to refine selection policies. By systematically choosing bor -
derline, uncertain, or minority-class samples, the agent ensures efficient annotation, reduces redundancy, and
Fig. 10 Cumulative reward trends over 300 train-
ing epochs for the AL agent on the AIV and AA
datasets.

Fig. 9 KL divergence comparison over 300 training epochs
for the off-policy PPO and baseline RL methods in the AL
agent on the AIV and AA datasets.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
Fig. 11 KL divergence
comparison over 300 training
epochs for the off-policy PPO
and baseline RL methods
in the feature selection and
prediction agent on the AIV
and AA datasets.

# Review text (Truncated) Selected
by AL
agent
AL
score
Reason for selection/rejection Senti-
ment
label
1 The packaging was damaged and
missing parts…
Yes 0.94 High uncertainty; negative class
under-sampled
Neg-
ative
2 Loved the quality and fast shipping! No 0.22 Confident positive prediction;
low uncertainty
Posi-
tive
3 The item works, but the instructions
were confusing…
Yes 0.84 Mixed signals between function-
ality and usability
Neu-
tral
4 Average product. Nothing special,
nothing bad
Yes 0.77 Ambiguity in sentiment class Neu-
tral
5 Fantastic service and product as
expected
No 0.18 Positive sentiment
overrepresented
Posi-
tive
6 Wrong color received, not what I
ordered
Yes 0.91 Error in order increases
uncertainty; underrepresented
negative
Neg-
ative
7 I keep buying this brand, very reliable No 0.33 High confidence, repetitive posi-
tive feedback
Posi-
tive
8 Usable, but performance is below
expectations
Yes 0.81 Unclear polarity; borderline
neutral-negative
Neu-
tral
9 Terrible experience! Will not
recommend
Yes 0.95 Strong negative sentiment valu-
able for balancing data
Neg-
ative
10 Fast delivery and great
communication
No 0.25 Clear positive prediction;
redundant
Posi-
tive
Table 12 Examples illustrat-
ing the selection decisions
of the AL agent, uncertainty
scores, and rationale behind
annotation prioritization.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
accelerates convergence. This demonstrates that the proposed AL strategy selects the most effective sentences to
enhance the overall sentiment classifier.
Agent 2 Figure 11 presents the KL divergence trends for the off-policy PPO method in the feature-selection and
prediction agents. The method is compared to TRPO, PPO, SAC, and standard RL across 300 epochs on the AIV
and AA datasets. Across both datasets, the off-policy PPO shows the steepest and most consistent reduction in KL
divergence, converging to much lower values than the baselines. This indicates superior policy stability and more
reliable updates during training. In contrast, TRPO and PPO reduce divergence more gradually, while SAC and
standard RL remain considerably higher, reflecting weaker control over policy shifts. The advantage of off-policy
PPO is its ability to reuse past trajectories and strike a balance between exploration and exploitation. This leads to
smoother optimization and faster convergence. By minimizing instability in feature selection and prediction, the
method ensures more consistent learning, which is critical in SA tasks. These results demonstrate that off-policy
PPO provides the most suitable framework for stable and efficient RL–driven agents.
Figure 12 shows the cumulative reward trend of the feature-selection and prediction agent over 300 epochs
for the AIV and AA datasets. Both curves demonstrate a steady upward trajectory. This reflects the ability of
the agent to continuously improve its policy through experience. The AA dataset achieves a higher cumulative
reward, surpassing 125 by the final epoch, while the AIV dataset follows a similar trend but stabilizes just above
105. This consistent growth highlights the stability of the off-policy PPO framework in guiding feature selection
and prediction. It also ensures that each iteration brings measurable improvements. Importantly, the absence of
sharp fluctuations indicates that the agent avoids unstable updates and converges smoothly. The gap between
AA and AIV suggests dataset-specific differences. The richer and more diverse samples in AA provide greater
opportunities to maximize rewards. Overall, the results confirm that the proposed method achieves robust learn-
ing efficiency, delivering reliable improvements in both datasets across the full training horizon.
a)                                                                                         b)
Fig. 13 ( a) ROC and (b) RR curves of the proposed model on the AIV and AA datasets.

Fig. 12 Cumulative reward trends over 300 training epochs
for the feature selection and prediction agent on the AIV and
AA datasets.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
Figure 13 presents the receiver operating characteristic (ROC) and precision-recall (PR) curves of the pro -
posed model, which are essential for evaluating performance on the AIV and AA datasets. The results dem -
onstrate that the model maintains high discriminative ability even under imbalanced class conditions. On the
AA dataset, the PR-AUC reaches 0.807. On the AIV dataset, the PR-AUC is 0.793. These results demonstrate
consistent robustness across different data distributions. The strong PR curve indicates that the model effectively
minimizes false positives and accurately captures instances of the minority class, which is critical in imbalanced
recommendation tasks. Similarly, the ROC trends confirm reliable classification across thresholds. The relatively
close values of AA and AIV highlight the generalizability of the model. This result shows that reward shaping for
minority samples in the off-policy PPO framework effectively controls class imbalance while maintaining overall
accuracy.
Figure 14 presents the confusion matrices of the proposed model evaluated on the AIV and AA datasets, high-
lighting its strong performance in classifying positive, neutral, and negative sentiments. For the AIV dataset, the
model correctly predicts 2093 positive, 522 neutral, and 874 negative samples. Misclassifications are limited and
appear only in small numbers across classes. On the AA dataset, the model scales well to larger sample sizes. It
correctly classifies 43,368 positive, 10,842 neutral, and 18,071 negative samples. These results demonstrate that
the proposed model successfully captures minority classes, such as neutral and negative, which are often chal -
lenging in imbalanced datasets. The relatively low off-diagonal values confirm a reduction in false positives and
false negatives. This consistency across both datasets highlights the robustness of the reward-adjusted off-policy
PPO framework, proving its effectiveness in handling class imbalance while maintaining high overall classifica-
tion accuracy.
Table 13 reports the model performance for both majority and minority classes on the AIV and AA datasets.
For most classes, the proposed model achieves 98.40% accuracy and 99.37% F-measure on AIV . On AA, the
Table 13 Assessment of the performance of the proposed model across dominant and underrepresented classes for the AIV
and AA datasets.
Dataset AIV AA
Metric Majority Minority Majority Minority
Accuracy 98.407 ± 0.005 92.582 ± 0.040 99.716 ± 0.005 93.555 ± 0.003
F-measure 99.377 ± 0.002 93.271 ± 0.010 99.949 ± 0.001 94.128 ± 0.057
G-means 99.494 ± 0.008 93.427 ± 0.074 100 ± 0.000 95.821 ± 0.069
AUC 0.952 ± 0.009 0.818 ± 0.002 0.982 ± 0.006 0.832 ± 0.039
All results are reported as mean ± standard deviation over the five cross-validation folds.
a)                                                                                            b)
Fig. 14 Confusion matrix outputs of the proposed approach applied to the (a) AIV and (b) AA datasets.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
results are even stronger, with 99.71% accuracy and 99.94% F-measure. More importantly, the model generalizes
well to minority classes, where performance often drops. For minority classes, AIV results include 92.58% accu-
racy and 93.27% F-measure. On AA, performance improves slightly to 93.55% accuracy and 94.12% F-measure.
The G-means and AUC further confirm balanced learning across both groups, particularly with AUC scores
above 0.81 for minority categories. These results highlight that the proposed model not only excels in dominant
classes but also maintains strong predictive ability for underrepresented sentiments, which is crucial in imbal -
anced SA tasks.
Analysis of the proposed RelGANGE
This section examines the capability of RelGANGE to produce synthetic samples for online augmentation. The
model is benchmarked against eight recognized GAN variants: sequence GAN (SeqGAN) 27, leaked informa -
tion GAN (LeakGAN)66, ranking-based GAN (RankGAN)67, text GAN (TextGAN)68, maximum likelihood aug-
mented GAN (MaliGAN) 69, masked sequence GAN (MaskGAN) 70, feature-matching GAN (FM-GAN) 71, and
the original RelGAN. The evaluation is conducted on the AIV and AA datasets, with detailed results presented
in Tables 14 and 15. To measure both the quality and diversity of generated text, several established statistical
metrics are employed. These include maximum mean discrepancy (MMD), Fréchet inception distance (FID),
Wasserstein distance, and the Kolmogorov–Smirnov (KS) test. Collectively, these measures assess how well the
synthetic distributions align with real data and indicate the extent to which each model can preserve semantic
richness and structural variety.
The results demonstrate that the proposed RelGANGE model achieves substantial improvements over tradi -
tional GANs and the original RelGAN on both the AIV and AA datasets. On the AIV dataset, RelGANGE reduces
the MMD to 1.058. This corresponds to a 78.6% improvement over RelGAN and an 84% improvement over FM-
GAN. Similarly, the FID decreases to 2.462. This represents a 54.2% reduction compared to RelGAN and more
than an 85% reduction compared to TextGAN. Wasserstein distance also drops significantly, from 5.162 with
RelGAN to 2.582 with RelGANGE, marking almost a 50% improvement. KS statistics follow the same pattern,
Model MMD FID Wasserstein KS
SeqGAN 12.555 ± 0.038 16.236 ± 0.075 22.979 ± 0.062 0.821 ± 0.033
LeakGAN 11.128 ± 0.023 15.270 ± 0.094 20.990 ± 0.057 0.791 ± 0.058
RankGAN 11.021 ± 0.100 14.669 ± 0.007 19.366 ± 0.034 0.752 ± 0.078
TextGAN 10.549 ± 0.063 12.284 ± 0.088 18.989 ± 0.040 0.662 ± 0.055
MaliGAN 9.518 ± 0.010 10.293 ± 0.066 15.072 ± 0.013 0.635 ± 0.021
MaskGAN 6.766 ± 0.073 9.729 ± 0.012 12.525 ± 0.051 0.552 ± 0.053
FM-GAN 5.730 ± 0.069 5.427 ± 0.081 7.240 ± 0.019 0.542 ± 0.031
RelGAN 3.881 ± 0.032 4.439 ± 0.046 4.223 ± 0.002 0.252 ± 0.075
RelGANGE 0.914 ± 0.013 1.728 ± 0.035 1.927 ± 0.100 0.115 ± 0.070
Table 15 Comparative anal-
ysis of different GAN-based
augmentation methods
applied to the AA dataset.
All results are reported as
mean ± standard deviation over
the five cross-validation folds.

Model MMD FID Wasserstein KS
SeqGAN 13.407 ± 0.044 17.565 ± 0.012 23.466 ± 0.035 0.856 ± 0.072
LeakGAN 12.377 ± 0.021 16.914 ± 0.061 21.752 ± 0.064 0.828 ± 0.020
RankGAN 12.094 ± 0.061 15.701 ± 0.080 20.503 ± 0.070 0.779 ± 0.099
TextGAN 11.582 ± 0.029 13.102 ± 0.032 19.937 ± 0.034 0.683 ± 0.031
MaliGAN 10.271 ± 0.081 11.116 ± 0.097 16.927 ± 0.002 0.651 ± 0.024
MaskGAN 7.427 ± 0.078 10.822 ± 0.011 13.612 ± 0.024 0.598 ± 0.080
FM-GAN 6.716 ± 0.056 6.398 ± 0.085 8.147 ± 0.018 0.575 ± 0.091
RelGAN 4.949 ± 0.037 5.377 ± 0.044 5.162 ± 0.010 0.286 ± 0.045
RelGANGE 1.058 ± 0.074 2.462 ± 0.090 2.582 ± 0.024 0.126 ± 0.022
Table 14 Comparative anal-
ysis of different GAN-based
augmentation methods
applied to the AIV dataset.
All results are reported as
mean ± standard deviation over
the five cross-validation folds.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
reaching 0.126, which is less than half that of RelGAN (0.286) and far lower than early GAN baselines such as
SeqGAN (0.856). These metrics confirm that RelGANGE generates synthetic distributions that are statistically
closer to real data. They also show that the samples are more diverse, which helps alleviate data sparsity in online
augmentation.
The superiority of RelGANGE is consistent on the AA dataset. RelGANGE reduces MMD from 3.881 in
RelGAN to 0.914, a 76.5% improvement. It also reduces FID from 4.439 to 1.728, a 61% improvement. Wasser-
stein distance decreases by over 54%, while the KS statistic improves by 54.4% compared to RelGAN. Against
advanced baselines such as FM-GAN and MaskGAN, RelGANGE still maintains significant margins, highlight-
ing its robustness across varying conditions. The key reason for these improvements lies in the gradient signal
exclusion mechanism, which suppresses unstable gradients during training. RelGANGE avoids mode collapse
and reduces bias toward dominant structures. As a result, it maintains higher stability and produces outputs that
reflect nuanced semantic and syntactic patterns more effectively. This adaptive control explains why RelGANGE
consistently outperforms all other GAN variants, making it particularly effective for generating high-quality
synthetic data in SA applications.
To evaluate whether RelGANGE statistically surpasses the compared GAN baselines, we performed paired
t-tests on the results reported in Tables 14 and 15 across all four metrics (MMD, FID, Wasserstein, and KS). On
the AIV dataset, RelGANGE showed highly significant improvements over RelGAN, with p-values < 0.001 for
all metrics. The effect sizes were large, with Cohen’s d values above 1.1 and 95% confidence intervals ranging
from [0.88, 1.42]. Results against FM-GAN and MaskGAN were also significant (p < 0.01), with Cohen’s d values
between 0.9 and 1.2 and confidence intervals of [0.72, 1.30]. For the AA dataset, the superiority of RelGANGE
was again evident. Against RelGAN, the results were significant, with p-values < 0.001, Cohen’s d exceeding 1.2,
and confidence intervals ranging from [0.95, 1.48]. On the AA dataset, comparisons with FM-GAN and Mask -
GAN again showed consistent gains (p < 0.01), with Cohen’s d ranging from 0.8 to 1.0 and confidence intervals
of [0.70, 1.25]. Overall, statistical comparisons across all GAN models yielded p-values < 0.01, 95% confidence
intervals generally within [0.70, 1.45], and Cohen’s d values ranging between 0.8 and 1.3. These outcomes con-
firm that RelGANGE yields statistically significant improvements in data-generation quality, thereby validating
its effectiveness for robust online augmentation in SA.
Table 16 illustrates the quality of samples generated by the proposed RelGANGE model, evaluated across
multiple linguistic and sentiment criteria. The outputs demonstrate semantic coherence and syntactic fluency.
They produce text that closely resembles natural human expression. Positive examples such as “Absolutely loved
Generated sample Semantic
coherence
Syntactic
fluency
Sentiment
polarity
score
Human
evaluation
score (1–5)
Useful-
ness for
augmen-
tation
The pasta was delicious, but the ser-
vice was slow
High Fluent Mixed 4 Yes
Absolutely loved the friendly staff and
cozy environment!
Very High Fluent Positive 5 Yes
The food was overpriced and tasted
terrible
High Fluent Negative 5 Yes
Delivery was late, but the food quality
was good
Medium Fluent Mixed 4 Yes
Great value for money, will definitely
order again
High Fluent Positive 5 Yes
Nothing impressive, just an average
meal overall
Medium Fluent Neutral 3 Border-
line
Extremely poor hygiene, very disap-
pointing experience
High Fluent Negative 5 Yes
Tasty desserts and excellent coffee at
fair prices
High Fluent Positive 5 Yes
Table 16 Examples of text
generated by the proposed
RelGANGE model.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
the friendly staff and cozy environment!” received the highest human evaluation score of 5, reflecting very high
coherence and clear sentiment polarity. Negative reviews such as “The food was overpriced and tasted terrible”
also achieved top ratings. This shows the model can capture sharp negative sentiment without introducing gram-
matical errors. Even mixed and neutral cases, such as “Delivery was late, but the food quality was good,” scored
well. This suggests that the model can effectively handle balanced sentiment complexity. These results confirm
that RelGANGE consistently generates reliable, diverse, and useful samples for augmentation, strengthening
downstream sentiment classification tasks.
Figure 15 depicts the training loss curves for both the generator and discriminator of the proposed RelGANGE
model across 300 epochs on the AIV and AA datasets. In both cases, the losses decrease steadily. This indicates
a smooth and stable training process without sudden divergence or oscillation. For the AIV dataset, the genera -
tor loss begins around 17 and gradually declines toward 2–3. The discriminator shows a similar trend, starting
near 13 and stabilizing below 3. On the AA dataset, the pattern is consistent: both networks converge to low loss
values by the end of training. The close alignment between the generator and discriminator loss curves confirms
that neither network dominates the other, thereby preventing mode collapse. This stable convergence highlights
the effectiveness of gradient signal exclusion in maintaining balance. As a result, RelGANGE generates realistic
and diverse text samples.
Figure 16 compares the distributions generated by the original RelGAN and the proposed RelGANGE against
real data for the AIV and AA datasets. In the AIV dataset, the original RelGAN shows mode collapse. The
Fig. 16 Distributional comparison
between RelGAN and the pro-
posed RelGANGE models on the
(a) AIV and (b) AA datasets.

a) b)
Fig. 15 Visualization of generator and discriminator loss progression over 300 training epochs in the proposed RelGANGE
model across the (a) AIV and (b) AA datasets.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
generated samples cluster around limited ranges and fail to capture the multiple peaks present in real data. By
contrast, RelGANGE produces a distribution that closely mirrors the real data, maintaining distinct peaks and
balanced frequencies. A similar pattern is observed in the AA dataset. RelGAN outputs are compressed around
a narrow region, whereas RelGANGE successfully reconstructs the bimodal structure of the actual data. This
improvement stems from the exclusion of the gradient signal mechanism. It suppresses unstable gradients and
enhances sample diversity. Consequently, RelGANGE avoids mode collapse, preserves semantic variety, and
generates richer, more representative synthetic data for augmentation.
Analysis of BOHB
This section compares the BOHB algorithm with several well-known hyperparameter optimization methods. For
fairness, all model variables were standardized during testing to ensure a consistent basis for comparison. The
evaluation included three basic algorithms, including random search, grid search, and BO, as well as ten evolu -
tionary algorithms. These evolutionary methods are: human mental search (HMS), salp swarm algorithm (SSA),
cuckoo optimization algorithm (COA), firefly algorithm (FA), bat algorithm (BA), particle swarm optimization
(PSO), differential evolution (DE), covariance matrix adaptation evolution strategy (CMA-ES)72, puma optimizer
Model Accuracy F-measure G-means AUC
Random search 77.715 ± 0.092 78.095 ± 0.089 78.975 ± 0.069 0.679 ± 0.007
Grid search 78.728 ± 0.068 78.961 ± 0.020 79.842 ± 0.039 0.686 ± 0.091
BO 93.688 ± 0.028 93.454 ± 0.001 94.366 ± 0.003 0.823 ± 0.088
HB 75.937 ± 0.017 76.998 ± 0.080 77.850 ± 0.046 0.651 ± 0.011
HMS 79.604 ± 0.095 79.955 ± 0.041 80.858 ± 0.020 0.710 ± 0.077
SSA 80.721 ± 0.060 81.293 ± 0.070 82.126 ± 0.093 0.727 ± 0.079
COA 82.021 ± 0.086 82.742 ± 0.038 83.600 ± 0.013 0.735 ± 0.099
FA 83.494 ± 0.029 84.279 ± 0.039 85.073 ± 0.036 0.746 ± 0.035
BA 84.038 ± 0.040 85.050 ± 0.059 85.841 ± 0.007 0.760 ± 0.089
PSO 85.531 ± 0.062 86.338 ± 0.017 87.130 ± 0.049 0.770 ± 0.076
DE 86.324 ± 0.034 87.466 ± 0.062 88.281 ± 0.083 0.777 ± 0.015
CMA-ES 86.848 ± 0.069 88.787 ± 0.097 89.632 ± 0.079 0.793 ± 0.054
PO 87.777 ± 0.098 90.453 ± 0.030 91.254 ± 0.017 0.803 ± 0.003
AOA 88.398 ± 0.058 91.976 ± 0.089 92.757 ± 0.063 0.813 ± 0.037
BOHB 96.241 ± 0.035 95.580 ± 0.069 96.220 ± 0.091 0.882 ± 0.059
Table 18 Performance met-
rics comparison of basic and
metaheuristic techniques for
hyperparameter optimiza-
tion across the AA dataset.
All results are reported as
mean ± standard deviation over
the five cross-validation folds.

Model Accuracy F-measure G-means AUC
Random search 75.453 ± 0.036 77.764 ± 0.082 78.509 ± 0.017 0.666 ± 0.052
Grid search 76.709 ± 0.028 78.484 ± 0.043 79.221 ± 0.044 0.680 ± 0.026
BO 92.660 ± 0.062 92.697 ± 0.013 93.389 ± 0.004 0.816 ± 0.092
HB 74.270 ± 0.045 76.753 ± 0.081 77.475 ± 0.087 0.649 ± 0.037
HMS 77.764 ± 0.004 79.274 ± 0.040 79.992 ± 0.088 0.702 ± 0.096
SSA 78.283 ± 0.093 80.232 ± 0.031 80.959 ± 0.051 0.711 ± 0.041
COA 79.402 ± 0.012 81.513 ± 0.019 82.156 ± 0.028 0.721 ± 0.045
FA 80.339 ± 0.043 82.929 ± 0.037 83.584 ± 0.032 0.727 ± 0.034
BA 81.182 ± 0.004 83.892 ± 0.095 84.602 ± 0.086 0.741 ± 0.012
PSO 82.430 ± 0.071 85.216 ± 0.079 85.836 ± 0.042 0.748 ± 0.075
DE 83.955 ± 0.060 86.779 ± 0.023 87.386 ± 0.055 0.758 ± 0.055
CMA-ES 85.747 ± 0.050 87.914 ± 0.072 88.529 ± 0.001 0.768 ± 0.068
PO 86.779 ± 0.079 89.130 ± 0.091 89.701 ± 0.057 0.775 ± 0.034
AOA 88.181 ± 0.031 90.263 ± 0.046 90.863 ± 0.016 0.787 ± 0.073
BOHB 94.723 ± 0.024 95.163 ± 0.034 95.788 ± 0.068 0.838 ± 0.004
Table 17 Performance met-
rics comparison of basic and
metaheuristic techniques for
hyperparameter optimiza-
tion across the AA dataset.
All results are reported as
mean ± standard deviation over
the five cross-validation folds.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
(PO)73, and arithmetic optimization algorithm (AOA) 74. The performance of all techniques was assessed using
the AIV and AA datasets, and the results are summarized in Tables 17 and 18.
On the AIV dataset, the BOHB algorithm consistently outperformed all traditional and evolutionary optimiza-
tion methods. Compared to random search, BOHB achieved 25.5% higher accuracy, 22.9% higher F-measure,
22.3% higher G-means, and nearly 18% higher AUC. Against grid search, the gains were 23.5% in accuracy,
21.5% in F-measure, 20.8% in G-means, and about 17% in AUC. BO already provides a probabilistic and adap-
tive approach to exploring the search space. Even so, BOHB delivered notable improvements, raising accuracy
by 2.2%, F-measure by 2.7%, G-means by 2.6%, and AUC by 2.7%. Against strong evolutionary baselines such
as AOA and PO, BOHB maintained superiority, achieving 6.5% higher accuracy, 5.5% higher F-measure, 5.4%
higher G-mean, and 5.1% higher AUC.
A similar pattern emerges in the AA dataset. BOHB surpassed random search and grid search by margins
exceeding 23–24% in accuracy and 17–18% in AUC. Relative to BO, BOHB improved accuracy by 2.7%,
F-measure by 2.3%, G-means by 2.0%, and AUC by 5.9%. Compared with the most competitive evolutionary
model, AOA, BOHB still produced 7.8% higher accuracy, 3.6% higher F-measure, 3.7% higher G-mean, and
6.9% higher AUC. These consistent improvements highlight that the strength of BOHB comes from combining
Bayesian exploration with HB resource allocation. This synergy enables efficient elimination of weak candidates
and focused refinement in promising regions, allowing BOHB to outperform static search methods and computa-
tionally expensive evolutionary algorithms while ensuring scalability in high-dimensional settings.
We used paired t-tests on the results in Tables 17 and 18 to evaluate the superiority of BOHB over other hyper-
parameter optimization methods. The tests covered four metrics: Accuracy, F-measure, G-means, and AUC. On
the AIV dataset, BOHB achieved clear improvements compared to the strongest evolutionary competitor, AOA.
All metrics produced p-values < 0.001, with Cohen’s d ranging from 1.1 to 1.4, indicating a large effect size. The
95% confidence intervals excluded zero and were approximately [0.82, 1.47]. Compared with BO, the results
were also significant (p < 0.01), with Cohen’s d around 0.9 and confidence intervals ranging from [0.68, 1.22]. On
the AA dataset, the improvements were similar, and in some cases, even stronger. Against AOA and PO, BOHB
consistently achieved p-values < 0.001 across all metrics, with Cohen’s d between 1.2 and 1.5 and confidence
intervals in [0.93, 1.55]. Comparisons with BO further supported the advantage of BOHB ( p < 0.01), with effect
sizes ranging from 0.8 to 1.0 and confidence intervals of [0.65, 1.20]. Overall, the statistical results between
BOHB and all baseline optimizers showed p-values below 0.01, 95% confidence intervals within the range of
[0.65, 1.55], and Cohen’s d values between 0.8 and 1.5. These findings confirm that the improvements in BOHB
Table 19 Comparative analysis of computational efficiency across various hyperparameter optimization algorithms on the
AIV and AA datasets.
Dataset AIV AA
Model Training time (s) GPU (GB) FLOP (×𝟏𝟏𝟏𝟏𝟏𝟏𝟏𝟏 ) Training time (s) GPU (GB) FLOP (×𝟏𝟏𝟏𝟏𝟏𝟏𝟏𝟏 )
Random search 2015 22.276 0.828 2307 18.977 1.318
Grid search 2180 19.406 0.671 2336 20.364 1.427
BO 2564 31.031 1.746 3128 28.696 2.243
HB 2045 20.574 1.240 2244 18.651 0.846
HMS 3154 33.013 1.777 2995 33.130 1.765
SSA 2564 27.024 1.736 2915 32.197 1.954
COA 2540 26.924 1.947 3063 33.502 1.673
FA 2622 24.376 2.446 2713 25.594 2.661
BA 3059 27.401 2.449 2618 29.170 1.855
PSO 3005 28.341 2.428 2954 33.697 1.864
DE 3165 29.109 1.973 2769 25.959 2.000
CMA-ES 3166 26.939 2.498 3042 27.612 2.270
PO 2889 27.805 1.407 2532 26.782 2.264
AOA 2699 31.540 1.707 2948 33.355 2.253
BOHB 1956 17.532 1.258 2597 20.290 1.572

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
are both substantial and statistically significant, demonstrating its suitability as a reliable hyperparameter optimi-
zation method in real-world applications.
Table 19 highlights the computational efficiency of BOHB across the AIV and AA datasets, showing clear
advantages over conventional and evolutionary methods. On the AIV dataset, BOHB reduces training time by
2.9% compared to random search and by 10.3% compared to grid search. It also cuts GPU memory consumption
by 21.3% and 9.6%, respectively. More importantly, BOHB is 23.7% faster and 43.4% more efficient in GPU
usage than BO, while also reducing FLOPs by 28.0%. Against the strongest evolutionary baselines, such as CMA-
ES and DE, BOHB achieves up to 38% shorter training time and 35–40% less GPU usage. These results prove
its efficiency under computationally intensive scenarios. Similar improvements are observed on the AA dataset.
BOHB outperforms BO by 17% in training time, 29% in GPU usage, and 29.9% in FLOPs. Even compared to
AOA and PO, BOHB reduces training time by 12–15% while keeping FLOPs lower by around 30%. Further -
more, the generator and discriminator of the RelGANGE model converge steadily with BOHB-tuned parameters,
as evidenced by their balanced loss curves. This optimization strategy not only saves resources but also stabilizes
the adversarial training process. This combination of computational efficiency and stable convergence under -
scores the strength of BOHB as the most suitable method for hyperparameter optimization across both AIV and
AA datasets.
Figure 17 meticulously details the effectiveness of the BOHB method in optimizing hyperparameters for the
proposed model across the AIV and AA datasets. The results demonstrate that BOHB identifies the optimal values
for critical parameters. These include batch size, learning rate, number of epochs, and number of LSTM layers.
On the AIV dataset, the best configuration includes a batch size of 72, a learning rate of 0.001, 220 epochs, and
three LSTM layers. Similarly, for the AA dataset, BOHB selects a batch size of 79, a learning rate of 0.0006,
259 epochs, and five LSTM layers. In both datasets, accuracy declines when values deviate from the optimal
points. This confirms that both larger and smaller values compromise performance. This behavior demonstrates
the effectiveness of BOHB in striking a balance between exploration and exploitation. It prevents underfitting
from low parameter values and overfitting from excessively high settings. Consequently, BOHB provides stable,
high-performing configurations tailored to dataset-specific dynamics, highlighting its suitability for robust hyper-
parameter optimization.
a)                                                                                                     b)
Fig. 17 Hyperparameter optimization analysis across the (a) AIV and (b) AA datasets.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
Discussion
This article introduced a two-agent SA framework tailored for e-commerce recommendations. The framework is
designed to overcome persistent challenges, including sample efficiency, feature selection, and class imbalance.
To rigorously assess its performance, three well-known datasets were selected: AIV , AA, and Yelp. These datasets
offer a balanced view of various application scenarios, ranging from product-focused reviews to broader user-
generated content. Table 20 presents a detailed comparative analysis between the proposed model and the stron-
gest baseline, HAN-RS. The comparison is made across accuracy, F-measure, G-means, and AUC. The results
demonstrate consistent and substantial improvements across all datasets and metrics. For instance, on the AA
dataset, the proposed model achieved 96.241% accuracy and 95.580% F-measure, surpassing HAN-RS by 5.83%
and 6.68%, respectively. Similarly, on the AIV dataset, improvements include 5.29% in accuracy and 6.29% in
F-measure. On Yelp, the model achieved 94.175% accuracy and 93.054% F-measure. The AUC improvements
are also noteworthy, ranging from 4.83 to 7.69%. These margins confirm that the proposed model consistently
outperforms state-of-the-art alternatives. The results highlight its robustness, adaptability, and ability to address
the complexities of SA in e-commerce environments.
The superiority of the proposed model lies in the synergy of its integrated components, each addressing a criti-
cal challenge in SA. The overall architecture of the framework plays an important role in its performance, beyond
the effect of individual components. The adoption of a two-agent off-policy PPO structure is motivated by the
need to separate two tightly coupled yet functionally distinct tasks: sample selection and sentiment classification.
Single-agent RL models jointly optimize both tasks within one policy. In contrast, the proposed decomposition
separates them, reducing task interference and improving learning stability. This separation allows each agent to
operate within a smaller decision space, improving convergence while keeping training stable.
Off-policy PPO improves sample efficiency by reusing previously collected experiences. This is particularly
important in AL environments where labeled data is limited and expensive. Some alternative RL methods may
perform well in specific cases. However, the proposed design achieves a better balance between computational
cost and robustness when combined with LIME-based feature selection, imbalance-aware rewards, and data
augmentation. The ablation study further confirms that removing either agent or replacing off-policy PPO results
in noticeable performance degradation, highlighting the necessity of the full architectural design. Overall, the
observed performance improvements outweigh the additional computational overhead introduced by the two-
agent design, making the proposed architecture a favorable trade-off between efficiency and accuracy.
From a practical deployment perspective, the proposed framework is designed with scalability in mind using a
modular and decoupled architecture. Each component, including the AL agent, SA agent, feature selection mod-
ule, and hyperparameter optimization process, can operate independently, enabling distributed or parallel imple-
mentation in large-scale e-commerce environments. This design reduces system-level bottlenecks and allows the
framework to handle high-volume user–item interactions efficiently. The training process is performed offline,
Table 20 Comparative performance of the proposed vs. best-existing models on the AIV , AA, and Yelp datasets.
Dataset AIV AA Yelp
Metric Best previous
model
Perfor-
mance of
the model
Percentage
difference
Best previous
model
Perfor-
mance of
the model
Percentage
difference
Best previ-
ous model
Perfor-
mance of
the model
Per-
centage
differ-
ence
Accuracy HAN-RS
(89.962%)
94.723% 5.29 HAN-RS
(90.941%)
96.241% 5.83 HAN-RS
(89.675%)
94.175% 5.02
F-measure HAN-RS
(89.530%)
95.163% 6.29 HAN-RS
(89.591%)
95.580% 6.68 HAN-RS
(88.534%)
93.054% 5.11
G-means HAN-RS
(90.139%)
95.788% 6.27 HAN-RS
(90.350%)
96.220% 6.50 HAN-RS
(89.233%)
93.758% 5.07
AUC HAN-RS (0.794) 0.838 5.54 HAN-RS
(0.819%)
0.882 7.69 HAN-RS
(0.808)
0.847 4.83

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
while inference is done in real time using trained models. This reduces computational overhead during deploy -
ment. The use of off-policy learning further enhances scalability by improving sample efficiency and reducing
the need for continuous retraining. As a result, despite integrating multiple learning components, the framework
remains practically feasible for real-world RSs where both scalability and response time are critical factors.
The framework developed in this study was applied to e-commerce reviews. However, it has broad potential in
other domains where sentiment-driven decision-making is essential. For instance, in healthcare, patient feedback
collected from online forums or hospital surveys can be analyzed to identify patterns of dissatisfaction, thereby
improving service delivery and patient care. In financial markets, investor sentiments expressed in news, blogs, or
social media can be analyzed. These signals can then be integrated into recommendation engines to forecast stock
movements or investment risks. Similarly, in the tourism industry, analyzing large volumes of hotel or destination
reviews can enhance RSs by tailoring suggestions to user preferences and satisfaction levels. Beyond consumer
services, the model could support policy-making by mining citizen feedback on government platforms. This
information can then help decision-makers adapt policies in response to public sentiment. The adaptability of the
framework comes from its ability to handle imbalanced data, reduce labeling requirements, and optimize hyper-
parameters across contexts. These strengths enable the model to maintain high performance even in domains with
noisy, scarce, or biased data. Thus, the proposed approach can generalize effectively, offering a versatile solution
for SA across diverse industries and application areas.
The limitations of this study, along with the potential solutions, are summarized as follows:
 ● Computational complexity  Despite its strong performance, the proposed framework introduces additional
computational complexity due to the integration of multiple learning components, including RL agents, feature
selection, data augmentation, and hyperparameter optimization. While the modular design improves flexibil -
ity and performance, it also increases training cost compared with simpler baseline models. In large-scale or
resource-limited environments, additional optimization or hardware support may be required. Although offline
training reduces inference costs, the training pipeline remains computationally expensive. Therefore, future
work could explore lightweight variants of the proposed architecture, model compression techniques, or more
efficient RL strategies to further improve scalability in extremely large production systems.
 ● Annotation noise Another limitation of the proposed framework concerns its potential sensitivity to annotation
noise in real-world AL deployments. In the datasets used in this study, sentiment labels were already avail -
able, and no additional human annotation was required during the experiments. However, in real applications,
the framework assumes that newly assigned labels are correct and does not model annotation uncertainty or
labeling errors. Although AL reduces the annotation burden by selecting only the most informative samples,
mistakes made during manual labeling may still propagate into the training set and influence the learning pro-
cess. This is especially important in SA because the interpretation of reviews is often subjective. Ambiguous
reviews, sarcasm, mixed opinions, and domain-specific expressions may result in inconsistent labels. Future
studies could address this limitation through noise-aware AL, annotation confidence estimation, consensus-
based labeling, and automated quality-control mechanisms. These strategies could improve robustness against
annotation errors and further enhance the reliability of the proposed framework.
 ● Temporal validation The proposed framework is evaluated under temporal settings using the CVT-SA data -
set with early- and later-period splits. However, full temporal validation across all benchmark datasets is not
feasible. The primary datasets used in this study, including AIV , AA, and Yelp, do not provide explicit time-
stamp information, which prevents the construction of time-aware training and testing partitions. As a result,
temporal analysis cannot be consistently applied across all experimental settings. Nevertheless, experiments
on the CVT-SA dataset demonstrate that the proposed framework maintains strong, stable performance under
temporal distribution shifts. The results from early and later periods show that the model can handle changes
in sentiment distribution over time, indicating robustness to temporal drift. However, this validation remains
limited to a single external dataset. Therefore, future work should incorporate additional large-scale datasets
with fine-grained temporal annotations to more comprehensively evaluate long-term stability. Cross-domain

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
temporal benchmarks and streaming-based evaluations could provide further insights into model adaptability
and long-term performance in real-world dynamic settings.
 ● Reward design and augmentation bias The proposed framework relies on reward functions derived from LIME
explanations and class-imbalance adaptation mechanisms. Although these rewards guide the learning process
toward informative features and minority classes, they may occasionally introduce bias when feature-impor -
tance estimates are inaccurate or when minority-class rewards become overly dominant. In such cases, the
agent may focus excessively on specific features or classes, reducing generalization. Similarly, the RelGANGE
augmentation module may generate synthetic reviews that do not fully reflect the diversity of real customer
opinions. If synthetic samples contain repetitive linguistic patterns or imperfect sentiment expressions, the
classifier may learn biased representations. These cases may introduce bias into the learning process and re -
duce model robustness. Although the results show strong performance, future work could explore reward
regularization, confidence-aware feature selection, and quality-control methods for generated samples. Adding
diversity constraints and semantic validation can further reduce bias and improve real-world robustness.
 ● Valence-aware dictionary and sentiment reasoner (VADER) lexicon limitations The proposed framework uti-
lizes V ADER-based sentiment information as part of the feature extraction process. Although V ADER is ef-
fective for capturing general sentiment polarity, it has several limitations. First, it relies on predefined lexical
rules and may not fully capture contextual meanings, sarcasm, irony, or domain-specific expressions. As a
result, certain reviews may receive inaccurate sentiment scores. V ADER was developed using general English
resources. Therefore, it may show cultural or linguistic bias when applied to regional, informal, or evolving
online language. These limitations may affect feature representation and final sentiment prediction. Conse -
quently, sentiment scores generated by V ADER may occasionally introduce noisy or biased signals into the
learning process. Although GPT embeddings, AL, and feature selection reduce noisy sentiment signals, this
problem cannot be fully removed. Future work could use contextual sentiment models, domain-adaptive lexi-
cons, or transformer-based methods to improve robustness and reduce lexical bias.
 ● Ethical and deployment considerations  The proposed framework is designed to support large-scale SA and
may be useful for monitoring public reactions to health-related information. However, automated sentiment
classification should be used with caution in public health communication. Incorrect sentiment predictions
may misinterpret public concerns. This may also affect communication strategies and policy decisions. In pub-
lic health settings, such errors may lead to inaccurate assessments of community concerns, risk perception, and
responses to health interventions. In addition, demographic and linguistic biases may arise when some popula-
tion groups or language styles are underrepresented in the training data. Such biases could result in unequal
performance across different communities and reduce system fairness. To mitigate these risks, future studies
should incorporate more diverse datasets that include different demographic groups, regions, and linguistic
styles. Data diversification, balanced sampling, and bias auditing can improve fairness and representative -
ness. Furthermore, the proposed framework should be integrated into social monitoring systems as a decision-
support tool rather than a fully autonomous system. Human oversight, transparency, privacy protection, and
regular bias checks are essential for responsible deployment in public health applications.
Conclusions
This study proposed an SA framework for e-commerce RSs. The framework integrates multiple complementary
components to address key challenges, including sample efficiency, feature selection, class imbalance, general -
ization, and hyperparameter optimization. The proposed two-agent off-policy PPO architecture separates sample
selection from sentiment classification. The first agent reduces labeling cost using AL. The second agent improves
classification performance using LIME-based feature selection and adaptive rewards for minority classes. In
addition, RelGANGE is introduced for online data augmentation to improve data diversity, while BOHB is used

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
to efficiently optimize hyperparameters. This integrated design enhances both robustness and adaptability of the
framework. Experimental results on the AIV , AA, and Yelp datasets demonstrate strong performance, achieving
F-measure scores of 95.163%, 95.580%, and 93.054%, respectively, and significantly outperforming state-of-
the-art baselines. Statistical analysis further confirms that the improvements are significant ( p < 0.01). Overall,
the results show that the proposed framework achieves a strong balance between predictive performance, inter -
pretability, and computational efficiency. The synergy between AL, RL, explainable feature selection, imbal -
ance-aware learning, and data augmentation improves robustness in dynamic e-commerce environments. These
findings also suggest that the framework can serve as a reliable decision-support system for sentiment-driven
recommendation tasks.
Future research could focus on improving the scalability and adaptability of the proposed framework. This
should be tested in more diverse and real-world environments. In particular, extending evaluation to multilingual
and cross-domain datasets would provide a more comprehensive assessment of generalization. Moreover, incor-
porating transfer learning or continual learning strategies could reduce retraining costs. It could also improve
adaptability to evolving data distributions. From a deployment perspective, lightweight model variants and com-
pression techniques could improve efficiency in resource-constrained or edge computing environments. In addi-
tion, combining global explainability methods with local techniques such as LIME may improve interpretability
at both instance and model levels. Finally, energy-efficient RL and improved optimization methods could further
enhance computational efficiency while maintaining high predictive performance.
Appendix A:
This appendix provides a brief overview of the fundamental concepts used in this study, including LIME, PPO,
TRPO, off-policy PPO, and BOHB. These methods are introduced to support the understanding of the proposed
framework and its optimization components.
Appendix A.1: LIME
LIME explains complex model outputs using a simpler surrogate model. This surrogate focuses on the local
neighborhood around a particular data point 𝑥𝑥. Here, 𝑥𝑥 is an element from the 𝑋𝑋𝐿𝐿 dataset. The goal of LIME is
to reproduce the behavior of the black-box function 𝑓𝑓. In this study, 𝑓𝑓 represents the classification model. LIME
constructs a locally accurate model 𝑔𝑔, often linear or interpretable, to approximate 𝑓𝑓 near 𝑥𝑥. This step identifies
the features that most strongly influence the prediction of 𝑓𝑓 for the chosen instance.
For a given instance 𝑥𝑥, LIME generates an interpretation by solving the following optimization problem:
Fig. 18 Visualization of the LIME process for features {𝐴𝐴𝐴 𝐴𝐴}
. It shows perturbed samples 𝑍𝑍, the proximity-based weight-
ing 𝜋𝜋𝑥𝑥, and the local linear model 𝑔𝑔 that approximates the
black-box model 𝑓𝑓 around the instance.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4

𝜉𝜉(𝑥𝑥𝑥 𝑥 arg𝑚𝑚𝑚𝑚𝑚𝑚
𝑔𝑔∈𝐺𝐺
𝐿𝐿 (𝑓𝑓𝑓 𝑓𝑓𝑓 𝜋𝜋𝑥𝑥𝑥 + 𝛺𝛺(𝑓𝑓𝑥 (26)
In this formulation, 𝐺𝐺 represents the set of candidate interpretable models. The function 𝐿𝐿 (𝑓𝑓𝑓 𝑓𝑓𝑓 𝜋𝜋𝑥𝑥) measures
how closely the surrogate model 𝑔𝑔 matches the predictions of the original model 𝑓𝑓. The proximity function 𝜋𝜋𝑥𝑥
assigns weights to perturbed samples depending on their closeness to the instance 𝑥𝑥. The regularization term 𝛺𝛺(𝑔𝑔𝑔
limits model complexity. This prevents overly complicated explanations and ensures that 𝑔𝑔 remains interpretable.
Here, 𝑓𝑓𝑓𝑓 𝑑𝑑 →𝑓  denotes the predictive function being approximated. For a given point 𝑥𝑥, perturbed versions
𝑍𝑍𝑍 {𝑧𝑧1,𝑧𝑧 2,…,𝑧𝑧 𝑚𝑚}  are generated by making small changes to its values. The predictive model 𝑓𝑓 is applied to each
𝑧𝑧 ∈ 𝑍𝑍 to obtain the corresponding output 𝑓𝑓𝑓𝑓𝑓𝑓. Every perturbed instance receives a weight through the proximity
function:

𝜋𝜋𝑥𝑥(𝑧𝑧𝑧 𝑧 exp (− 𝐷𝐷(𝐷𝐷𝐷 𝑧𝑧𝑧
2
𝜎𝜎2 ) (27)
In this setting, 𝐷𝐷𝐷𝐷𝐷𝐷 𝐷𝐷𝐷 is the distance between the original instance 𝑥𝑥 and a perturbed sample 𝑧𝑧. This distance is
usually computed using the Euclidean metric. The kernel width parameter 𝜎𝜎 controls the rate at which weights
decay with distance.
The surrogate model 𝑔𝑔 ∈ 𝐺𝐺, often linear, is fitted to the weighted dataset {(𝑧𝑧𝑧 𝑧𝑧(𝑧𝑧𝑧𝑧 ∣ 𝑧𝑧 ∈ 𝑍𝑍}. When a linear approx-
imation is employed, 𝑔𝑔 takes the following form:

𝑔𝑔𝑔𝑔𝑔𝑔 𝑔 𝑔𝑔 0 +
𝑑𝑑
∑
𝑗𝑗𝑗𝑗
𝑔𝑔𝑗𝑗𝑔𝑔𝑗𝑗 (28)
In this step, the weights 𝑤𝑤𝑗𝑗 are updated to minimize the weighted loss function:

ˆ𝑤𝑤 𝑤arg𝑚𝑚𝑚𝑚𝑚𝑚
𝑤𝑤
∑
𝑧𝑧∈𝑍𝑍
𝜋𝜋𝑥𝑥(𝑧𝑧𝑧(𝑧𝑧(𝑧𝑧𝑧 𝑧 𝑧𝑧(𝑧𝑧𝑧 𝑤𝑤𝑧𝑧
2
+ 𝛺𝛺(𝑧𝑧𝑧 (29)
The coefficients 𝑤𝑤𝑗𝑗 show how much each feature contributes to the prediction of 𝑓𝑓 near 𝑥𝑥. A positive coefficient
indicates that the feature increases the prediction value, whereas a negative coefficient suggests it decreases it. In
this way, LIME provides a clear and faithful explanation of the behavior of the model around a chosen instance.
By restricting analysis to the neighborhood of 𝑥𝑥, LIME avoids the difficulty of explaining the global behavior of
𝑓𝑓. Instead, it highlights the features that most strongly affect the prediction for that instance.
In this framework, LIME is not used as a separate predictive model. Instead, LIME is applied only to gener -
ate local importance scores for individual samples, which are then integrated into the reward formulation. The
surrogate model 𝑔𝑔 in LIME is not trained globally. Instead, it is built dynamically around a single instance x
using perturbations. Consequently, LIME avoids the need for an additional lengthy training phase. Its function is
restricted to producing interpretable coefficients 𝑤𝑤𝑗𝑗 that reflect the most significant features at a local scale. This
design ensures that the values used in the LIME-based reward signal in Eq. 17 stay efficient and reliable, without
adding unnecessary computation or complexity.
Figure 18 shows how LIME values are computed for a feature pair {𝐴𝐴𝐴 𝐴𝐴}. The horizontal axis represents fea-
ture 𝐴𝐴, and the vertical axis represents feature 𝐵𝐵, forming a two-dimensional feature plane. Predictions are gener-
ated across this space by the black-box model 𝑓𝑓. LIME creates perturbed samples Z around the target instance 𝑥𝑥
, which is marked as the central point. These samples appear as scattered neighboring points. Each sample 𝑧𝑧 is
weighted using the proximity function 𝜋𝜋𝑥𝑥, with larger weights assigned to points closer to 𝑥𝑥. A simple surrogate
model 𝑔𝑔, often shown as a linear boundary, is fitted to approximate 𝑓𝑓 in this local region. The slope of 𝑔𝑔 indicates
the strength of the contribution of features 𝐴𝐴 and 𝐵𝐵 to the prediction.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
Appendix A.2: PPO, TRPO, and off-policy PPO
In this section, we outline PPO. PPO applies a clipped surrogate objective to control the large policy shifts that
can occur in TRPO. Finally, we introduce the off-policy PPO variant. This variant combines features of TRPO
and PPO, resulting in more stable and effective training.
Appendix A.2.1 TRPO
In RL, the main goal is to determine a policy 𝜋𝜋 that optimizes the expected sum of discounted rewards75:

𝜂𝜂 (𝜋𝜋) =𝐸𝐸 𝑠𝑠0 ,𝑎𝑎0 ,… [𝑅𝑅0] =𝐸𝐸 𝑠𝑠0 ,𝑎𝑎0 ,…[
∞
∑
𝑡𝑡𝑡0
𝛾𝛾𝑡𝑡𝑟𝑟(𝑟𝑟𝑡𝑡,𝑎𝑎 𝑡𝑡)] (30)
In this setup, 𝑠𝑠0 ∼ ρ0 represents the initial state sampled from a predefined distribution. The policy 𝜋𝜋(𝑎𝑎𝑡𝑡|𝑠𝑠𝑡𝑡) gives
the probability of taking action 𝑎𝑎𝑡𝑡 in state 𝑠𝑠𝑡𝑡. The transition function 𝑃𝑃𝑃𝑃𝑃𝑡𝑡𝑡𝑡|𝑃𝑃𝑡𝑡,𝑎𝑎 𝑡𝑡) describes the probability of reach-
ing the next state given the current state and chosen action. The discount parameter 𝛾𝛾 regulates the weight of
future rewards. TRPO improves the policy by maximizing a surrogate objective. It also controls policy updates
with a KL divergence constraint75:

max
𝜋𝜋
𝐸𝐸𝑠𝑠∼𝜌𝜌𝜋𝜋𝜃𝜃𝑜𝑜𝑜𝑜𝑜𝑜 ,𝑎𝑎∈𝜋𝜋𝜋𝜋𝑜𝑜𝑜𝑜𝑜𝑜 [ 𝜋𝜋𝜃𝜃 (𝑎𝑎𝑎𝑎𝑎) 𝜋𝜋𝜃𝜃𝑜𝑜𝑜𝑜𝑜𝑜 (𝑎𝑎𝑎𝑎𝑎) 𝐴𝐴𝜋𝜋𝑜𝑜𝑜𝑜𝑜𝑜 (𝑎𝑎𝑠 𝑎𝑎)] (31)
subject to
 𝐸𝐸𝑠𝑠∼𝜌𝜌𝜋𝜋𝑜𝑜𝑜𝑜𝑜𝑜 [𝐷𝐷𝐾𝐾𝐾𝐾(𝜋𝜋𝑜𝑜𝑜𝑜𝑜𝑜(.|𝑠𝑠𝑠||𝜋𝜋(.|𝑠𝑠𝑠𝑠] ≤𝛿𝛿  (32)
In this context, 𝜋𝜋𝑜𝑜𝑜𝑜𝑜𝑜 denotes the previous policy, while 𝛿𝛿 specifies the allowable divergence threshold. The term
𝐷𝐷𝐾𝐾𝐾𝐾(𝜋𝜋𝑜𝑜𝑜𝑜𝑜𝑜(.|𝑠𝑠𝑠||𝜋𝜋(.|𝑠𝑠𝑠𝑠 represents the KL divergence. It measures how much the new policy 𝜋𝜋 differs from the old policy
𝜋𝜋𝑜𝑜𝑜𝑜𝑜𝑜 in state 𝑠𝑠. The expression 𝜌𝜌𝜋𝜋𝑜𝑜𝑜𝑜𝑜𝑜 (𝑠𝑠) =
∞
∑
𝑡𝑡𝑡𝑡
𝛾𝛾𝑡𝑡𝑃𝑃(𝑠𝑠𝑡𝑡 = 𝑠𝑠𝑠𝑠𝑠 𝑡, 𝜋𝜋𝑜𝑜𝑜𝑜𝑜𝑜) defines the discounted state distribution. This distribu-
tion is obtained when the system starts from the initial state 𝑠𝑠0 and follows the old policy. Without this divergence
constraint, maximizing the surrogate objective in Eq. 32 could cause large and unstable policy updates.
Appendix A.2.2 PPO
To ensure stable policy adjustments, PPO employs a clipped surrogate objective function75:

𝐿𝐿𝐶𝐶𝐶𝐶𝐶𝐶𝐶𝐶 𝐶𝐶𝐶𝐶𝑃𝑃 =𝐸𝐸 𝑠𝑠∼𝜌𝜌𝜋𝜋𝑜𝑜𝑜𝑜𝑜𝑜 ,𝑎𝑎∼𝜋𝜋𝑜𝑜𝑜𝑜𝑜𝑜 [min( 𝜋𝜋 (𝑎𝑎𝑎𝑎𝑎) 𝜋𝜋𝑜𝑜𝑜𝑜𝑜𝑜 (𝑎𝑎𝑎𝑎𝑎) 𝐴𝐴𝜋𝜋𝑜𝑜𝑜𝑜𝑜𝑜 (𝑎𝑎𝑠 𝑎𝑎) 𝑠 𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐( 𝜋𝜋 (𝑎𝑎𝑎𝑎𝑎) 𝜋𝜋𝑜𝑜𝑜𝑜𝑜𝑜 (𝑎𝑎𝑎𝑎𝑎) 𝑠 1− ∈𝑠 1+ ∈)𝐴𝐴𝜋𝜋𝑜𝑜𝑜𝑜𝑜𝑜 (𝑎𝑎𝑠 𝑎𝑎))] (33)
The parameter 𝜖𝜖 is a small positive constant that helps balance stability and exploration during learning. The
advantage function 𝐴𝐴𝜋𝜋𝑜𝑜𝑜𝑜𝑜𝑜 (𝑠𝑠𝑠 𝑠𝑠) measures how much better action 𝑎𝑎 in state 𝑠𝑠 performs compared to the average
performance of all actions under the previous policy. Clipping the probability ratio limits large policy deviations
and improves training stability75:
 𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐 𝑐𝑐𝑐 𝑐𝑐𝑐 𝑐 𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐 𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐 𝑐𝑐𝑐𝑐  (34)
Here, 𝑥𝑥 is the variable being constrained. The values 𝑎𝑎 and 𝑏𝑏 define the lower and upper bounds of the allowed
range. This mechanism discourages policy updates when the probability ratio strays too far from 1. PPO offers
several benefits. However, it has a key drawback: a strong dependence on on-policy samples. This dependence

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
increases sample complexity. It forces repeated agent–environment interactions and raises the computational cost
of training.
Appendix A.2.3 Off-policy PPO
This section introduces the off-policy PPO algorithm. It aims to improve sample efficiency by using information
from past interactions and multiple policy choices. Unlike standard on-policy PPO, which relies mainly on data
from ongoing interactions and therefore requires many new samples, off-policy PPO learns from a broader pool
of experiences. This pool includes prior trajectories and diverse decision-making strategies. For example, imag-
ine a robot navigating a complicated maze. On-policy PPO updates its behavior only based on the current run,
whereas off-policy PPO also incorporates insights from previous attempts made under different conditions. This
method accelerates learning by minimizing the need for exhaustive exploration. It also enhances performance by
utilizing a broader range of experiences.
Off-policy PPO was selected because it balances sample efficiency, training stability, and suitability for discrete
decision-making tasks. Unlike on-policy PPO, it can reuse historical experiences, which is particularly impor -
tant in AL settings where labeled samples are limited and costly to obtain. Methods such as deep deterministic
policy gradient (DDPG) and twin delayed deep deterministic policy gradient (TD3) are primarily designed for
continuous control problems and are less suitable for the discrete actions involved in sample selection and feature
selection. Although algorithms such as SAC offer strong exploration capabilities, they often require more com -
plex value estimation mechanisms and additional hyperparameter tuning. In contrast, off-policy PPO preserves
stable policy updates and improves sample efficiency through experience reuse. These characteristics make it
well-suited to the proposed two-agent framework, which requires stable, data-efficient learning for AL and SA.
Fig. 19 Off-policy PPO optimization workflow for coordi -
nated enhancement of dual-agent learning in the proposed
framework.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
The off-policy PPO method addresses the optimization problem by maximizing a surrogate objective with off-
policy samples. It follows a strategy similar to off-policy TRPO75:

max
𝜋𝜋
𝐸𝐸𝑠𝑠∼𝜌𝜌𝜇𝜇,𝑎𝑎∈𝜇𝜇 [ 𝜋𝜋 (𝑎𝑎𝑎𝑎𝑎) 𝜇𝜇 (𝑎𝑎𝑎𝑎𝑎) 𝐴𝐴𝜋𝜋𝑜𝑜𝑜𝑜𝑜𝑜 (𝑎𝑎𝑠 𝑎𝑎)] (35)
Subject to:
 𝐷𝐷
𝜌𝜌𝜇𝜇,𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠
𝐾𝐾𝐾𝐾 (𝜇𝜇, 𝜋𝜋𝑜𝑜𝑜𝑜𝑜𝑜) 𝐷𝐷
𝜌𝜌𝜇𝜇,𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠
𝐾𝐾𝐾𝐾 (𝜋𝜋𝑜𝑜𝑜𝑜𝑜𝑜, 𝜋𝜋) + 𝐷𝐷
𝜌𝜌𝜇𝜇
𝐾𝐾𝐾𝐾 (𝜋𝜋𝑜𝑜𝑜𝑜𝑜𝑜, 𝜋𝜋) ≤𝛿𝛿  (36)
where

𝜌𝜌𝜇𝜇 (𝑠𝑠) =
∞
∑
𝑡𝑡𝑡𝑡
𝛾𝛾𝑡𝑡𝑃𝑃(𝑠𝑠𝑡𝑡 = 𝑠𝑠𝑠𝑠𝑠 𝑡, 𝜇𝜇) (37)
 𝐷𝐷
𝜌𝜌𝜇𝜇
𝐾𝐾𝐾𝐾 (𝜋𝜋𝑜𝑜𝑜𝑜𝑜𝑜, 𝜋𝜋) =𝐸𝐸 𝑠𝑠∼𝜌𝜌𝜇𝜇 [𝐷𝐷𝐾𝐾𝐾𝐾 (𝜋𝜋𝑜𝑜𝑜𝑜𝑜𝑜 (.|𝑠𝑠) ||𝜋𝜋 (.|𝑠𝑠))] (38)
 𝐷𝐷
𝜌𝜌𝜇𝜇,𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠
𝐾𝐾𝐾𝐾 (𝜇𝜇, 𝜋𝜋𝑜𝑜𝑜𝑜𝑜𝑜) =𝐸𝐸 𝑠𝑠∼𝜌𝜌𝜇𝜇 [√𝐷𝐷𝐾𝐾𝐾𝐾 (𝜇𝜇 (.|𝑠𝑠) ||𝜋𝜋𝑜𝑜𝑜𝑜𝑜𝑜 (.|𝑠𝑠))] (39)
 𝐷𝐷
𝜌𝜌𝜇𝜇,𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠
𝐾𝐾𝐾𝐾 (𝜋𝜋𝑜𝑜𝑜𝑜𝑜𝑜, 𝜋𝜋) =𝐸𝐸 𝑠𝑠∼𝜌𝜌𝜇𝜇 [√𝐷𝐷𝐾𝐾𝐾𝐾 (𝜋𝜋𝑜𝑜𝑜𝑜𝑜𝑜 (.|𝑠𝑠) ||𝜋𝜋 (.|𝑠𝑠))] (40)
Here, 𝜇𝜇 denotes the behavior policy. Without the restriction in Eq. 36, optimizing the surrogate function with
off-policy data from Eq. 35 could lead to large and unstable policy shifts. To prevent this, the PPO clipping
mechanism is applied. It reshapes the surrogate objective to maintain stability75:

𝐿𝐿𝜇𝜇 (𝜋𝜋) =𝐸𝐸 𝑠𝑠∼𝜌𝜌𝜇𝜇,𝑎𝑎∈𝜇𝜇[ 𝜋𝜋 (𝑎𝑎𝑎𝑎𝑎) 𝜇𝜇 (𝑎𝑎𝑎𝑎𝑎) 𝐴𝐴𝜋𝜋𝑜𝑜𝑜𝑜𝑜𝑜 (𝑎𝑎𝑠 𝑎𝑎)] (41)
Based on 𝐿𝐿𝜇𝜇 (𝜋𝜋) in Eq. 41, the clipped surrogate objective that incorporates off-policy samples can be expressed
as 75:

𝐿𝐿𝜇𝜇 (𝜋𝜋) =𝐸𝐸 𝑠𝑠∼𝜌𝜌𝜇𝜇,𝑎𝑎∈𝜇𝜇[min( 𝜋𝜋 (𝑎𝑎𝑎𝑎𝑎) 𝜇𝜇 (𝑎𝑎𝑎𝑎𝑎) 𝐴𝐴𝜋𝜋𝑜𝑜𝑜𝑜𝑜𝑜 (𝑎𝑎𝑠 𝑎𝑎) 𝑠 𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐( 𝜋𝜋 (𝑎𝑎𝑎𝑎𝑎) 𝜇𝜇 (𝑎𝑎𝑎𝑎𝑎) 𝑠 1− ∈𝑠 1+ ∈)𝐴𝐴𝜋𝜋𝑜𝑜𝑜𝑜𝑜𝑜 (𝑎𝑎𝑠 𝑎𝑎))] (42)
In most cases, the ratio 𝜋𝜋 (𝑎𝑎𝑎𝑎𝑎) 𝜇𝜇 (𝑎𝑎𝑎𝑎𝑎)  falls outside the range (1 − 𝜖𝜖,1+ 𝜖𝜖). As a result, the policy 𝜋𝜋 (𝑎𝑎𝑎𝑎𝑎) does not change
during optimization of the clipped surrogate function. To solve this problem, Eq. 42 adjusts the clipping bounds
(1 − 𝜖𝜖,1+ 𝜖𝜖) by adding a correction factor 𝜋𝜋𝜃𝜃𝑖𝑖 (𝑎𝑎𝑎𝑎𝑎) 𝜇𝜇 (𝑎𝑎𝑎𝑎𝑎) 75:

𝐿𝐿𝐶𝐶𝐶𝐶𝐶𝐶𝐶𝐶 𝑂𝑂𝑂𝑂𝑂𝑂𝑂𝐶𝐶𝑂𝑂𝑂𝑂𝑂𝑂𝑂𝑂𝑂𝑂𝐶𝐶𝐶𝐶𝑂𝑂 (𝜋𝜋)=𝐸𝐸 𝑠𝑠∼𝜌𝜌𝜇𝜇,𝑎𝑎∈𝜇𝜇[min[ 𝜋𝜋 (𝑎𝑎𝑎𝑎𝑎) 𝜇𝜇 (𝑎𝑎𝑎𝑎𝑎) 𝐴𝐴𝜋𝜋𝑂𝑂𝑂𝑂𝑜𝑜 (𝑎𝑎𝑠 𝑎𝑎) 𝑠 𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐 ( 𝜋𝜋 (𝑎𝑎𝑎𝑎𝑎) 𝜇𝜇 (𝑎𝑎𝑎𝑎𝑎) 𝑠 𝜋𝜋𝑂𝑂𝑂𝑂𝑜𝑜 (𝑎𝑎𝑎𝑎𝑎) 𝜇𝜇 (𝑎𝑎𝑎𝑎𝑎) (1− ∈)𝑠 𝜋𝜋𝑂𝑂𝑂𝑂𝑜𝑜 (𝑎𝑎𝑎𝑎𝑎) 𝜇𝜇 (𝑎𝑎𝑎𝑎𝑎) (1+ ∈)) 𝐴𝐴𝜋𝜋𝑂𝑂𝑂𝑂𝑜𝑜 (𝑎𝑎𝑠 𝑎𝑎)]] (43)
Figure 19 illustrates a concise, seven-step pipeline for enhancing both agents in the proposed model through
the off-policy PPO approach. The workflow starts by defining the optimization target in the model. A surrogate
objective is introduced, along with a clipping strategy, to prevent unstable shifts in learning. Next, historical
training data are incorporated into the objective, enabling the model to capture broader patterns and generalize
more effectively. The ratio of new to old policies is then checked, and adjustments are applied if the ratio exceeds
the permitted bounds, thereby promoting controlled, steady updates. This refined policy is continually improved
through iterative updates until the system reaches convergence.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
Appendix A.3. BOHB
BOHB combines the probabilistic modeling capabilities of BO with the adaptive resource allocation strategy of
HB. Conventional BO techniques, such as the tree-structured Parzen estimator (TPE), optimize parameters one
at a time. In contrast, BOHB employs a unified kernel density estimator (KDE) to jointly evaluate all parameters.
This joint modeling helps the algorithm capture dependencies and interactions between hyperparameters more
effectively.
In BOHB, the random sampling step from HB is replaced with a model-guided approach. Here, a KDE pro -
poses promising hyperparameter values by analyzing past evaluations. These candidates are evaluated using the
successive halving procedure of HB. In this process, more resources are gradually allocated to the strongest per-
formers across rounds. By combining model-based selection with adaptive allocation, BOHB explores hyperpa-
rameter choices more effectively. It balances searching for unexplored configurations (exploration) with focusing
on high-potential ones (exploitation). This strategy is particularly effective in complex optimization tasks with
limited resources. It finds strong parameter choices with fewer trials than conventional methods.
Algorithm 6 outlines the pseudocode for optimizing hyperparameters with the BOHB method. The goal is to
refine a set of parameters 𝑥𝑥. These may include batch size, learning rate, and other key model settings. A history
log 𝐷𝐷 records tested configurations along with their performance scores. This record begins empty and expands
as the algorithm evaluates more candidates. The optimization runs iteratively until a stopping criterion is reached.
Examples include a predefined number of iterations or a time limit.
Next, two KDEs are created: 𝑙𝑙𝑙𝑙𝑙𝑙 from 𝐷𝐷𝑔𝑔𝑔𝑔𝑔𝑔𝑔𝑔 and 𝑔𝑔𝑔𝑔𝑔𝑔 from 𝐷𝐷𝑏𝑏𝑏𝑏𝑏𝑏. These estimators model the likelihood that a
configuration will yield strong or weak performance. The bandwidth of each KDE is modified with a scaling
parameter 𝑏𝑏𝑤𝑤 to expand the search space. The univariate KDE formulation applied in this context is expressed
as76:

ˆ𝑓𝑓𝑓𝑓𝑓𝑓 𝑓 1 𝑛𝑛𝑛
𝑛𝑛
∑
𝑖𝑖𝑖𝑖
𝐾𝐾 ( 𝑓𝑓 𝑥𝑓𝑓 𝑖𝑖
𝑛 ) (44)
In this equation, ˆ𝑓𝑓𝑓𝑓𝑓𝑓 represents the estimated probability density at point x. The variable 𝑛𝑛 refers to the number
of data samples, while ℎ denotes the bandwidth parameter that determines the smoothness of the density estimate.
The kernel function 𝐾𝐾 is symmetric and non-negative. A common choice is the Gaussian kernel, which integrates
to one. Each 𝑥𝑥𝑖𝑖 corresponds to an observation drawn from the dataset. In BOHB, a multivariate version of KDE
is used. This allows the method to evaluate several hyperparameters simultaneously. This version builds a joint
probability distribution over the hyperparameter space. It helps reveal dependencies among parameters.
At this stage, the procedure generates 𝑁𝑁𝑠𝑠 trial hyperparameter configurations using the KDE 𝑙𝑙𝑙𝑙𝑙𝑙. For each can-
didate 𝑥𝑥𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐, the algorithm computes the ratio 𝑙𝑙 (𝑥𝑥𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐) 𝑔𝑔(𝑥𝑥𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐) . This ratio indicates whether the candidate is more
likely to perform well or poorly. The candidate with the highest ratio is chosen for evaluation in the following
iteration. BOHB repeats this cycle, balancing the search for new parameter options with the refinement of prom-
ising ones. This approach enables the rapid identification of effective configurations while keeping computational
costs under control.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
Input: Probability of selecting a random configuration , threshold percentile for selecting top-performing
configurations , number of configuration candidates to generate , minimum number of samples required to train
KDE , Bandwidth adjustment factor for KDE
Output: Best hyperparameter configuration ∗
Historical record ←∅ to store evaluated configurations and their performance
While until a stopping criterion is met do:
← Generate a random value [0,1]
If r < then:
Randomly choose a new configuration
Else:
Find the highest budget level such that ∣ ∣≥ +2
If no such is found then:
Randomly choose a new configuration
Else:
Split into two groups:
:T op ×∣ ∣ configurations with best performance
: Rest configurations
Train two KDEs:
( ) using
( ) using
Sample configuration candidates from ( ) using bandwidth scaled by
For each :
compute the likelihood ratio
( )
( )
Select the candidate with the highest likelihood ratio as the new configuration
Evaluate the performance of configuration
Store the result in the historical set
Return ∗
Algorithm 4 Pseudocode for BOHB-based hyperparameter optimization.
Algorithm 6:
Author contributions  Mohammad Yarjanli: conceptualization, methodology, validation, investigation, resources, writ -
ing–original draft, writing–review and editing, visualization. Neda Mahdinasab: software, data curation, validation, formal
analysis, investigation, visualization, writing–review and editing.
Data availability The datasets utilized in this study, AIV , AA, Yelp, and CVT-SA, are publicly available benchmark datas-
ets. Their original sources can be accessed via the following repositories: AIV and  A A :   h t t p s : / / s n a p . s t a n f o r d . e d u / d a t a / w e b - A
m a z o n . h t m l     Yelp:https://business.yelp.com/data/resources/open-dataset  C V T - S A :   h t t p s : / / w w w . k a g g l e . c o m / d a t a s e t s / d a t a s c i e
n c e t o o l / c o v i d 1 9 - v a c c i n e - t w e e t s - w i t h - s e n t i m e n t - a n n o t a t i o n
Declarations
Competing interests The authors declare no competing interests.
Open Access  This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 Interna-
tional License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as
long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence,
and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material
derived from this article or parts of it. The images or other third party material in this article are included in the article’s Cre-
ative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s
Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you
will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit  h t t p : / / c r e a t i v e c o m m o
n s . o r g / l i c e n s e s / b y - n c - n d / 4 . 0 /     .
References
 1. Shankar, A. et al. An intelligent recommendation system in e-commerce using ensemble learning. Multim. Tools
Appl.83(16), 48521–48537 (2024).

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
 2. Li, R. et al. Federated cross-view e-commerce recommendation based on feature rescaling. Sci.  R e p .    h t t p s : / / d o i . o r g / 1 0 . 1
0 3 8 / s 4 1 5 9 8 - 0 2 4 - 8 1 2 7 8 - 1     (2024).
 3. Tiwari, D., Nagpal, B., Bhati, B. S., Mishra, A. & Kumar, M. A systematic review of social network sentiment analysis
with comparative study of ensemble-based techniques. Artif. Intell. Rev. https://doi.org/10.1007/s10462-023-10472-w
(2023).
 4. Yadav, V ., Verma, P. & Katiyar, V . Long short term memory (LSTM) model for sentiment analysis in social data for
e-commerce products reviews in Hindi languages. Int. J. Inf. Technol.15(2), 759–772 (2023).
 5. Tiwari, D. & Nagpal, B. KEAHT: A knowledge-enriched attention-based hybrid transformer model for social sentiment
analysis. New Gener. Comput.40(4), 1165–1202 (2022).
 6. Tiwari, D. et al. SPSO-EFVM: A particle swarm optimization-based ensemble fusion voting model for sentence-level
sentiment analysis. IEEE Access12, 23707–23724 (2024).
 7. Mahadevaswamy, U. & Swathi, P. Sentiment analysis using bidirectional LSTM network. Procedia Comput. Sci.218,
45–56 (2023).
 8. Yarjanli, M. & Mahdinasab, N. A hybrid deep learning model for E‐commerce recommendations: Sentiment analysis
with autoencoders and generative adversarial networks. Int. J. Intell. Syst.2025(1), 3852068 (2025).
 9. Tiwari, D. et al. A swarm-optimization based fusion model of sentiment analysis for cryptocurrency price prediction. Sci.
Rep.15(1), 8119 (2025).
 10. Tiwari, D., Bhati, B. S., Nagpal, B., Alturki, N. & Bayisenge, L. Attention-augmented hybrid CNN-LSTM model for
social media sentiment analysis in cryptocurrency investment decision-making. Sci. Rep.15(1), 33201 (2025).
 11. Kaseb, A. & Farouk, M. Active learning for Arabic sentiment analysis. Alex. Eng. J.77, 177–187 (2023).
 12. Liebenlito, M., Inayah, N., Choerunnisa, E., Sutanto, T. E. & Inna, S. Active learning on Indonesian Twitter sentiment
analysis using uncertainty sampling. J Appl Data Sci5(1), 114–121 (2024).
 13. Reka, K., Raja, G., Malarchelvi, P.D.S.K. AI and deep reinforcement learning for sentiment analysis of customer reviews.
in Web Intelligence, 2025, p. 24056456241304010: SAGE Publications Sage UK: London
 14. Motevalli, M.M. and Moravvej, S.V . Schizophrenia detecting using reinforcement learning-based active learning and
hyperparameter optimization. In: Artificial Intelligence for Neuroscience, Mental Health, and Neurodegenerative
Disorders: 11th International Work-Conference on the Interplay Between Natural and Artificial Computation, IWINAC
2026, Canary Islands, Spain, May 26–29, 2026, Proceedings, Part I, 2026, p. 25: Springer Nature.
 15. Zareeihemat, P., Farokhi, A., Valipour, J., Moravvej, S. V . & Mousavirad, S. J. An evolutionary hyperparameter-optimized
off-policy feature selection for real estate tax prediction. Int. J. Comput. Intell. Syst.19(1), 72 (2026).
 16. Eyu, J. M., Yau, K.-L.A., Liu, L. & Chong, Y .-W. Reinforcement learning in sentiment analysis: A review and future
directions. Artif. Intell. Rev.58(1), 6 (2024).
 17. Rasappan, P., Premkumar, M., Sinha, G. & Chandrasekaran, K. Transforming sentiment analysis for e-commerce product
reviews: Hybrid deep learning model with an innovative term weighting and feature selection. Inf. Process. Manag.61(3),
103654 (2024).
 18. Xia, S. & Yang, Y . A model‐free feature selection technique of feature screening and random forest‐based recursive
feature elimination. Int. J. Intell. Syst.2023(1), 2400194 (2023).
 19. Parveen, N., Chakrabarti, P., Hung, B. T. & Shaik, A. Twitter sentiment analysis using hybrid gated attention recurrent
network. J. Big Data10(1), 50 (2023).
 20. Blanchard, J. Enhancing lexical sentiment analysis using LASSO style regularization. (2023).
 21. Liu, P. & Lu, G. Addressing data imbalance for federated recommender systems: A rebalancing framework with gradient
alignment regularization. J. Intell. Inf. Syst.63(2), 657–679 (2025).
 22. Zareeihemat, P., Mohamadi, S., Valipour, J. & Moravvej, S. V . Forecasting stock market volatility using housing market
indicators: A reinforcement learning-based feature selection approach. IEEE Access13(1), 52621–52643 (2025).
 23. Ravikumar, R., Jain, S., Sarkar, M. SMOTE and hyperparameter optimization: a dual machine learning strategy for
enhancing coupon recommendation in vehicular contexts. In: 2023 3rd International Conference on Smart Generation
Computing, Communication and Networking (SMART GENCON), pp. 1–6: IEEE. (2023)
 24. Anggraini, D. P., Ambarwati, R., Dedy, D. & Toirxonovna, A. M. Workplace hazard identification through near-miss
reports: A social network analysis. Indones. J. Inf. Syst.7(1), 70–83 (2024).
 25. Shaikh, S., Kagita, V . R., Kumar, V . & Pujari, A. K. Data augmentation and refinement for recommender system: A semi-
supervised approach using maximum margin matrix factorization. Expert Syst. Appl.238, 121967 (2024).
 26. Chen, X., Wang, S., McAuley, J., Jannach, D. & Yao, L. On the opportunities and challenges of offline reinforcement
learning for recommender systems. ACM Trans. Inf. Syst.42(6), 1–26 (2024).
 27. Li, X., Mao, K., Lin, F. & Feng, Z. Feature-aware conditional GAN for category text generation. Neurocomputing547,
126352 (2023).
 28. Qi, Y . & Shabrina, Z. Sentiment analysis using Twitter data: A comparative application of lexicon-and machine-learning-
based approach. Soc. Netw. Anal. Min.13(1), 31 (2023).

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
 29. Shetty, A.M., Aljunid, M.F., Manjaiah, D., Afzal, S.A.M. Hyperparameter Optimization of machine learning models
using grid search for amazon review sentiment analysis. In: International Conference on Data Science and Applications,
pp. 451–474: Springer, (2023)
 30. Srivastava, S., Bala, N., Gupta, A., Priya, B.D., Kumar, S., Raj, A., Optimization of sentiment analysis models using
bayesian hyperparameter tuning. In 2024 International Conference on Artificial Intelligence and Quantum Computation-
Based Sensor Application (ICAIQSA), pp. 1–6: IEEE. (2024)
 31. Vincent, A. M. & Jidesh, P. An improved hyperparameter optimization framework for AutoML systems using evolutionary
algorithms. Sci. Rep.13(1), 4737 (2023).
 32. Viadinugroho, R. A. A. & Rosadi, D. A weighted metric scalarization approach for multiobjective BOHB hyperparameter
optimization in LSTM model for sentiment analysis. Inf. Sci.644, 119282 (2023).
 33. Tran, D. T. & Huh, J.-H. New machine learning model based on the time factor for e-commerce recommendation systems.
J. Supercomput.79(6), 6756–6801 (2023).
 34. Loukili, M., Messaoudi, F. & El Ghazi, M. Machine learning based recommender system for e-commerce. IAES Int J
Artif Intell (IJ-AI)12(4), 1803–1811 (1803).
 35. Belhadi, A., Djenouri, Y ., de Alcantara Andrade, F. A. & Srivastava, G. Federated constrastive learning and visual
transformers for personal recommendation. Cognitive Comput16(5), 2551–2565 (2024).
 36. Gulzar, Y ., Alwan, A. A., Abdullah, R. M., Abualkishik, A. Z. & Oumrani, M. OCA: Ordered clustering-based algorithm
for E-commerce recommendation system. Sustainability15(4), 2947 (2023).
 37. Sharma, P. & Sagvekar, V . R. Weighted ensemble LSTM model with word embedding attention for E-commerce product
recommendation. J. Commun. Softw. Syst.19(4), 299–307 (2023).
 38. Vullam, N., Vellela, S.S., Reddy, V ., Rao, M.V ., Roja, D. Multi-agent personalized recommendation system in e-commerce
based on user. In 2023 2nd International Conference on Applied Artificial Intelligence and Computing (ICAAIC) , pp.
1194–1199: IEEE, (2023)
 39. Karn, A. L. et al. Customer centric hybrid recommendation system for E-commerce applications by integrating hybrid
sentiment analysis. Electron. Commer. Res.23(1), 279–314 (2023).
 40. Chang, C. et al. KGTN: Knowledge graph transformer network for explainable multi-category item recommendation.
Knowl. Based Syst.278, 110854 (2023).
 41. Shang, F., Shi, J., Shi, Y . & Zhou, S. Enhancing e-commerce recommendation systems with deep learning-based sentiment
analysis of user reviews. Int J Eng Manag Res14(4), 19–34 (2024).
 42. Keikhosrokiani, P. & Fye, G. M. A hybrid recommender system for health supplement e-commerce based on customer
data implicit ratings. Multimed. Tools Appl.83(15), 45315–45344 (2024).
 43. Duan, S., Ouyang, M., Wang, R., Li, Q. & Xiao, Y . Let long-term interests talk: An disentangled learning model for
recommendation based on short-term interests generation. Inf. Process. Manag.62(2), 103997 (2025).
 44. Wang, Y ., Zhang, D. & Wulamu, A. Self-supervised cognitive learning for multifaced interest in large-scale industrial
recommender systems. Inf. Sci.686, 121338 (2025).
 45. Nag, A. et al. Fusing sentiment analysis with hybrid collaborative algorithms for enhanced recommender systems. In
Wellness Management Powered by AI Technologies 343–362 (2025).
 46. Zhang, V . W. et al. Advancing consumer insights: efficient sentiment analysis-based recommendation system using multi-
criteria decision making with a game theoretic approach. Ann Op Res356(1), 539–5558 (2025).
 47. Zhao, Z. et al. Enhancing e-commerce recommendations: Unveiling insights from customer reviews with
BERTFusionDNN. J Theory Pract Eng Sci4(02), 38–44 (2024).
 48. Bellar, O., Baina, A. & Ballafkih, M. Sentiment analysis: Predicting product reviews for e-commerce recommendations
using deep learning and transformers. Mathematics12(15), 2403 (2024).
 49. Scientific, L.L. Sentiment-based recommendation for online Shopping. Journal of Theoretical and Applied Information
Technology. 102(9), (2024).
 50. Karabila, I., Darraz, N., El-Ansari, A., Alami, N. & El Mallahi, M. A hybrid approach combining sentiment analysis and
deep learning to mitigate data sparsity in recommender systems. Neurocomputing636, 129886 (2025).
 51. Karabila, I., Darraz, N., EL-Ansari, A., Alami, N. & EL Mallahi, M. BERT-enhanced sentiment analysis for personalized
e-commerce recommendations. Multim. Tools Appl.83(19), 56463–56488 (2024).
 52. Darraz, N., Karabila, I., El-Ansari, A., Alami, N. & El Mallahi, M. Integrated sentiment analysis with BERT for enhanced
hybrid recommendation systems. Expert Syst. Appl.261, 125533 (2025).
 53. Krishna, E. P. et al. Enhancing e-commerce recommendations with sentiment analysis using MLA-EDTCNet and
collaborative filtering. Sci. Rep.15(1), 6739 (2025).

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
 54. Mohanty, I. Recommendation Systems in the Era of LLMs. In Proceedings of the 15th Annual Meeting of the Forum for
Information Retrieval Evaluation, pp. 142–144, (2023)
 55. Roumeliotis, K. I., Tselikas, N. D. & Nasiopoulos, D. K. LLMs in e-commerce: A comparative analysis of GPT and
LLaMA models in product review evaluation. Nat. Lang. Process. J.6, 100056 (2024).
 56. Jeong, B. & Lee, K. J. NLP-based recommendation approach for diverse service generation. IEEE Accesshttps://doi.
org/10.1109/ACCESS.2024.3355546 (2024).
 57. Sun, X., Holm, H., Molavipour, S., Gebre, F.G., Pawar, Y ., Radnosrati, K., Shalmashi, S., Recommendation system for
product test failures using BERT. In KDIR, pp. 206–213, (2023)
 58. Iftikhar, S., Alluhaybi, B., Suliman, M., Saeed, A. & Fatima, K. Amazon products reviews classification based on machine
learning, deep learning methods and BERT. TELKOMNIKA (Telecommun Comput Electron Control)21(5), 1084–1101
(2023).
 59. Jagatap, A., Gupta, N., Farfade, S., Comar, P.M., Attribert-session-based product attribute recommendation with bert, in
Proceedings of the 46th International ACM SIGIR Conference on Research and Development in Information Retrieval ,
pp. 3421–3425, (2023)
 60. Gheewala, S., Xu, S., Yeom, S. & Maqsood, S. Exploiting deep transformer models in textual review based recommender
systems. Expert Syst. Appl.235, 121120 (2024).
 61. Ali, H., Hashmi, E., Yayilgan Yildirim, S. & Shaikh, S. Analyzing amazon products sentiment: A comparative study of
machine and deep learning, and transformer-based techniques. Electronics13(7), 1305 (2024).
 62. Khan, H. U., Naz, A., Alarfaj, F. K. & Almusallam, N. A transformer-based architecture for collaborative filtering
modeling in personalized recommender systems. Sci. Rep.15(1), 24503 (2025).
 63. Vaghari, H., Hosseinzadeh Aghdam, M. & Emami, H. Group attention for collaborative filtering with sequential feedback
and context aware attributes. Sci. Rep.15(1), 10050 (2025).
 64. Koscinski, V ., Hashemi, S., Mirakhorli, M., On-demand security requirements synthesis with relational generative
adversarial networks. In 2023 IEEE/ACM 45th International Conference on Software Engineering (ICSE) . pp. 1609–
1621: IEEE, 2023
 65. Farshidvard, A., Hooshmand, F. & MirHassani, S. A novel two-phase clustering-based under-sampling method for
imbalanced classification problems. Expert Syst. Appl.213, 119003 (2023).
 66. Ghosh, S., Konar, A., Nagar, A.K. Computational creativity by generative adversial network with leaked information. In
2024 International Joint Conference on Neural Networks (IJCNN), pp. 1–8: IEEE, (2024)
 67. Juefei-Xu, F., Dey, R., Boddeti, V .N., Savvides, M., Rankgan: A maximum margin ranking gan for generating faces.
In Computer Vision–ACCV 2018: 14th Asian Conference on Computer Vision, Perth, Australia, December 2–6, 2018,
Revised Selected Papers, Part III 14. pp. 3–18: Springer (2019)
 68. Yu, J., Li, H., Hao, Y ., Zhu, B., Xu, T., He, X. CgT-GAN: Clip-guided text GAN for image captioning. In Proceedings of
the 31st ACM International Conference on Multimedia. pp. 2252–2263 (2023)
 69. Zhao, W., Liu, L., Wu, F., Pan, S., Wu, D., Wang, H. A knowledge–enhanced text clustering based adversarial learning
for text generation, In CCF National Conference of Computer Applications. pp. 241–255: Springer, (2024)
 70. Song, K., Tan, X., Qin, T., Lu, J., Liu, T.-Y . Mass: Masked sequence to sequence pre-training for language generation,"
arXiv preprint arXiv:1905.02450 (2019).
 71. Liu, Y ., Liu, Y . & Wang, J. RFM-GAN: Robust feature matching with GAN-based neighborhood representation for
agricultural remote sensing image registration. IEEE Geosci. Remote Sens. Lett.20, 1–5 (2023).
 72. Sinha, N. & Chen, K.-W. Neural architecture search using covariance matrix adaptation evolution strategy. Evol.
Comput.32(2), 177–204 (2024).
 73. Abdollahzadeh, B. et al. Puma optimizer (PO): A novel metaheuristic optimization algorithm and its application in
machine learning. Clust. Comput.27(4), 5235–5283 (2024).
 74. Yıldız, B. S. et al. A novel hybrid arithmetic optimization algorithm for solving constrained optimization problems.
Knowl. Based Syst.271, 110554 (2023).
 75. Yixin, Z. et al. An off-policy deep reinforcement learning-based active learning for crime scene investigation image
classification. Inf. Sci.710, 122074 (2025).
 76. Dogan, V ., Prestwich, S. BHO-MA: Bayesian hyperparameter optimization with multi-objective acquisition. In
International Conference on Optimization, Learning Algorithms and Applications. pp. 391–408: Springer (2023)
Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional
affiliations.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-71894-4
Authors and Affiliations
Mohammad Yarjanli1 · Neda Mahdinasab2
 Mohammad Yarjanli
mohammad.yarjanli@students.mq.edu.au
1 Macquarie Business School, Macquarie University, Sydney, NSW, Australia
2 Faculty of Management, Science and Technology, Amirkabir University of Technology, Tehran, Iran
