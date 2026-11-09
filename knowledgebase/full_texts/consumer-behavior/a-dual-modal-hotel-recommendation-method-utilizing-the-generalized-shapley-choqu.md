---
title: A dual-modal hotel recommendation method utilizing the generalized Shapley-Choquet integral
url: https://doi.org/10.1057/s41599-026-09225-1
category: consumer-behavior
subcategory: framework
date: 2026-10
venue: Humanities and Social Sciences Communications
authors:
- Fanyong Meng
- Qi Wang
source: openalex-oa
pdf_url: https://www.nature.com/articles/s41599-026-09225-1_reference.pdf
pages: 33
chars: 108908
fetched_at: '2026-11-08T19:19:48+00:00'
kb_version: 1
---

# A dual-modal hotel recommendation method utilizing the generalized Shapley-Choquet integral

Humanities and Social Sciences Communications
ARTICLE | Article in Press
A dual-modal hotel recommendation method utilizing
the generalized Shapley-Choquet integral
Fanyong Meng
●
Qi Wang
Received: 4 February 2026 / Accepted: 16 September 2026
© The Author(s) 2026
Abstract
This paper examines hotel management and consumer decision-making within the platform economy. Online reviews
serve as key instruments for analyzing complex consumer behavior. The new method converts computational
techniques—such as natural language processing, multimodal sentiment analysis, and fuzzy mathematics —into
quantitative analytical tools. The analytical framework systematically explores consumers ’ latent interactive
psychology. First, a data-driven hotel rating indicator system provides detailed characterization of service
experiences. Second, sentiment scores, derived from textual and image-based analyses, integrate cross-modal sensory
experiences through con ﬁdence levels, thereby reducing cognitive biases in emotional expression. The method
accounts for heterogeneous consumer preferences and psychological interactions among attributes. A 2-additive
measure, based on sentiment scores, dynamically determines attribute importance. The generalized Shapley value and
Choquet integral comprehensively capture compensation patterns across attribute subsets. Personalized demands are
mined from consumers’ historical accommodation records. A triple-hybrid similarity method screens candidate hotels
and enables personalized recommendations. The case study demonstrates that the proposed method effectively
captures consumers ’ multisensory and multi-attribute decision-making characteristics. The ﬁndings offer robust
managerial implications and support precise hotel service design and dynamic supply-demand alignment within the
platform economy ecosystem.
Introduction
The advancement of the Internet and digitalization drives more consumers to book hotels through online platforms
such as Ctrip and Qunar. Platform-mediated evaluations signi ﬁcantly reshape consumer behavior. In the tourism
information economy, user-generated content serves as a core mechanism to reduce information asymmetry, foster
consumer trust, and alter ﬁnal decision-making pathways (Filieri et al., 2015). In the era of the sharing economy and
big data, consumers shared their accommodation experiences through online reviews. Online hotel reviews became a
vital data source for analyzing consumer psychology and behavior. Compared with of ﬁcial hotel descriptions,
reviews provided a more objective re ﬂection of consumer needs and experiences. Consumers increasingly relied on
online reviews as their primary reference for hotel selection. Hotel managers used online reviews as feedback to
improve service offerings. Many studies explored effective methods to leverage online reviews and reveal their social
scientiﬁc and managerial value (Zhang et al., 2023; Zhu et al., 2021; Zhang et al., 2021; Liu et al., 2023).
This Article in Press is shared early to give you faster access to new research. It is citable and carries a permanent
DOI. The ﬁnal edited version will replace it automatically.
Humanities and Social Sciences Communications https://doi.org/10.1057/s41599-026-09225-1

Consumers express themselves in diverse ways, and online reviews often contain multimodal information such as
text, images, and geographic locations. This multi-source, heterogeneous data creates a multidimensional perceptual
space re ﬂecting consumer experience. Online hotel reviews include attribute scores, user data, interaction data, text,
images, and geographic information. These data enable the extraction of rich consumer behavioral characteristics,
such as user satisfaction, emotional preferences, service quality, and development trends. Existing technologies (Zhao
et al., 2024; Pang et al., 2016) can convert and process this information. Multimodal sentiment analysis integrates
data from different modalities and comprehensively captures consumers ’ emotional expressions in reviews (Zhao
et al., 2025; Wang et al., 2024). For example, SnowNLP quanti ﬁes textual sentiment tendencies (isnowfy, 2013),
while the CLIP model interprets image sentiment (Radford et al., 2021). Multimodal analysis reduces single-sensory
bias through fusion strategies. This study uses multimodal sentiment analysis as the primary tool to quantify
consumers’ emotional perceptions of their online accommodation experiences.
Current hotel recommendation and decision-making methods primarily focus on two areas: overall scoring and
multi-attribute analysis, and topic mining and sentiment analysis of textual data. The former predicts consumer
satisfaction, while the latter explores differences in experiences and preferences among consumer groups (Chen et al.,
2022). However, extant hotel recommendation methods exhibit pronounced de ﬁciencies in capturing actual consumer
behavior, which may be summarized as follows:
(1) The assumption of attribute independence imposes excessive restrictions. Most existing methods assume mutual
independence among hotel attributes. These approaches overlook the in ﬂuence of complex inter-attribute
interactions in consumer psychology, including compensation and penalty effects on satisfaction. Such methods
do not fully capture the intricate decision trade-offs that arise under bounded rationality.
(2) Insuf ﬁcient utilization of multimodal information persists. Most existing approaches depend heavily on review
text analysis. These methods perform limited mining of multimodal sensory information, particularly images.
Such approaches do not fully capture the affective value of visual information in representing consumer
experiences. This limitation constrains the platform ecosystem ’s ability to pro ﬁle users ’ true perceptions
accurately.
(3) Dif ﬁculties persist in extracting information effectively and building systematic frameworks. Automated
screening of valid reviews from unstructured consumer narratives and the systematic extraction of standardized
service evaluation frameworks aligned with human cognitive logic present substantial challenges. These barriers
limit support for enforcement operations and service improvement.
(4) Lack of dynamic adaptation for attribute weights remains a critical limitation. Most recommendation methods
do not dynamically adjust attribute weights based on satisfaction disparities among different hotel customer
segments. Static weight allocation fails to capture the psychological signi ﬁcance consumers place on attribute
trade-offs and their interactions. These limitations impede the realization of precision marketing for
heterogeneous customer groups in modern hotel management.
This paper aims to enhance the theoretical and practical implications of research across consumer behavior, hotel
operations, and platform economy domains. The study addresses four core social science and management research
questions:
(1) Within platform-mediated evaluation systems, how can multisensory visual cues be introduced to overcome the
limitations of single-textual expression, thereby restoring consumers ’ authentic accommodation experiences and
affective preferences?
(2) How can structured evaluation metrics, consistent with consumer cognitive logic, be extracted from massive and
dispersed online platform reviews to provide actionable guidance for hotel operations and service quality
enhancement?
(3) Assuming that statistical affective correlations re ﬂect underlying psychological associations, how can complex
psychological interactions among consumers be quanti ﬁed and explored during multi-attribute decision-
making? Such interactions may involve possible synergistic compensation and antagonistic penalty effects.
(4) How can the heterogeneous satisfaction and attention-allocation characteristics of different customer groups be
Article in Press https://doi.org/10.1057/s41599-026-09225-1
Humanities and Social Sciences Communications

captured within the digital platform ecosystem to support dynamic decision-making for hotel precision
marketing and personalized matching?
To address these key research questions and challenges, this study seeks to develop a more accurate consumer
decision support and recommendation framework within a social science context. The core contributions are as
follows:
(1) This paper proposes a cross-modal affective cognitive analysis framework. The new method leverages visual
information to correct subjective expression biases found in platform textual reviews. This approach provides
new insights into the transmission mechanisms of consumers ’ authentic multisensory experiences in platform-
mediated contexts.
(2) This paper introduces a reconstruction framework for evaluation systems that integrates data-driven methods
with industry service standards. The new method eliminates cognitive noise present in large-scale reviews. It
extracts ﬁne-grained service indicators aligned with consumer decision-making logic and provides practical
guidance for hotel operations.
(3) This paper challenges the strong assumption of service attribute independence in conventional decision models.
The new method employs 2-additive measures to explore and quantify latent attribute interactions based on
statistical correlations derived from real affective data. This approach provides new quantitative perspectives for
theoretical investigation of multi-attribute decision-making behavior under bounded rationality.
(4) This paper combines the generalized Shapley –Choquet operator with TF-IDF to capture dynamic attention
weights of customer groups. The new method incorporates behavioral similarity to match heterogeneous
individual preferences with precision. It establishes an adaptive personalized recommendation scheme. This
approach provides practical managerial tools for hotels in the platform economy, enabling differentiation of
services and precise supply-demand matching.
This paper ’s core innovation is a rigorous quantitative analytical framework for analyzing complex consumer
decision-making and hotel management practices. The main features are as follows:
(1) This paper introduces an entropy-based cross-modal con ﬁdence evaluation mechanism. The new method
provides quantitative support for conveying multisensory experiences and restoring consumers ’ authentic online
affective perceptions.
(2) This paper establishes a ﬁne-grained evaluation system that aligns with consumer experience narratives. The
system offers a structured analytical framework for precise measurement of hotel service quality and daily
operations management.
(3) This paper breaks the attribute independence assumption by applying 2-additive measures. The new approach
provides a scienti ﬁc quantitative pathway to investigate consumers ’ complex psychological synergistic and
antagonistic mechanisms under bounded rationality.
(4) This paper integrates the generalized Shapley –Choquet operator with dynamic attention weights. The resulting
multi-dimensional decision model analyzes heterogeneous customer group preferences and enables personalized
supply-demand matching within the platform economy.
The remainder of this paper is organized as follows: Section 2 reviews relevant literature; Section 3 details the
proposed recommendation method; Section 4 presents case studies and experimental validation; Section 5 discusses
management implications; and Section 6 concludes the paper and outlines future research directions.
Literature review
The use of multi-source information in online hotel reviews and related recommendation methods has attracted
signiﬁcant research attention. In the digital economy, arti ﬁcial intelligence and digital technologies are widely applied
in areas such as enhancing corporate green innovation ef ﬁciency (Mansour et al., 2026), and the digital economy
https://doi.org/10.1057/s41599-026-09225-1 Article in Press
Humanities and Social Sciences Communications

signiﬁcantly drives improvements in corporate performance (Mansour et al., 2026). Digital maturity and information
transparency further improve industrial performance and optimize governance mechanisms (Mansour et al., 2026).
With the rise of generative AI, big data analytics, business intelligence (BI), and decision support systems are
reshaping corporate business process management (Theodorakopoulos and Theodoropoulou, 2026). In the hospitality
industry, the Internet of Things (IoT) and data-driven decision models promote sustainable operations (Abdou and
Shehata, 2026), while arti ﬁcial intelligence disrupts traditional hotel service paradigms (Law et al., 2024). Achieving
intelligent decision-making and service innovation requires a deep understanding and accurate matching of multi-
source user feedback. This section reviews the literature from three perspectives: multimodal sentiment analysis,
evaluation indicator system construction, and recommendation algorithms.
Multimodal emotion analysis
Users often express emotions through multiple media. While natural language processing (NLP) and machine
learning algorithms can accurately predict the sentiment of online hotel reviews, these methods are limited to textual
data. Single-modal sentiment analysis cannot capture complex emotions, leading to the development of multimodal
sentiment analysis.
Early and late fusion are two traditional categories of multimodal fusion methods, ﬁrst systematically described by
Pantic and Rothkrantz ( 2003). Poria et al. ( 2017) used the LSTM model to capture contextual information from
videos. Zadeh et al. ( 2018) aligned different modalities and modeled each separately using LSTM. Poria et al. ( 2016)
extracted visual, textual, and audio features, then concatenated them for classi ﬁcation. For late fusion, Nicolle et al.
(2012) addressed the AVEC'12 challenge, while Kampman et al. ( 2018) independently obtained unimodal scores and
applied weighted fusion. However, neither early nor late fusion effectively addresses modality heterogeneity.
Multi-stage fusion methods combine the strengths of early and late fusion. Zadeh et al. ( 2017) based their work on
the Tensor Fusion Network, while Mai et al. ( 2019) developed a hierarchical feature fusion network that generates
local tensors and global fusion through tensor fusion. Majumder et al. ( 2018) designed a hierarchical fusion network
using contextual information to map local correlations across modalities.
Following the Transformer model (Vaswani et al., 2017), Delbrouck et al. ( 2020) developed a joint encoding
approach with self-attention and co-attention mechanisms for multimodal fusion. Tsai et al. ( 2019) introduced a
cross-modal Transformer to process unaligned sequences. Tang et al. ( 2021) proposed a coupled fusion network
based on generative adversarial networks to enhance robustness.
Representation learning is essential in multimodal sentiment analysis. Hazarika et al. ( 2020) mapped modality
features into distinct subspaces and designed loss functions to optimize feature representations. Yu et al. ( 2021)
introduced self-supervised representation learning. Han et al. ( 2021) preserved key sentiment analysis information by
maximizing mutual information.
Construction of evaluation index system
An evaluation indicator system comprises multiple indicators that represent the characteristics of research objects and
their interrelationships.
The Delphi method and dimensional division are widely used. Yang and Chen ( 2010) developed an evaluation
system for urban construction modernization. Li and Li ( 2024) proposed a ﬁve-dimensional evaluation approach for
zero-waste cities. Xiao et al. ( 2024) created an assessment system for medical virtual teaching and research sections
using two rounds of the Delphi method.
Auxiliary methods can enhance the ef ﬁciency of constructing evaluation systems. Yafei ( 2019) developed a health
policy evaluation system using system dynamics and complex networks. Ji et al. ( 2023) used TF-IDF, Word2Vec,
and K-means to establish an indicator system for hotel recommendations. Chen and Shi ( 2022) applied the Analytic
Hierarchy Process (AHP) and grey relational analysis to assess ecological civilization construction. Cai et al. ( 2024)
created a sensory evaluation system for steamed purple sweet potato rice sponge cake through expert consultation and
Article in Press https://doi.org/10.1057/s41599-026-09225-1
Humanities and Social Sciences Communications

fuzzy binary comparison. Li ( 2024) analyzed the interactive evaluation system of preschool education in universities
using machine learning algorithms (NB, KNN, LR, SVM), verifying the effectiveness of SVM.
Hotel recommendation methods
The core of hotel recommendation systems is the alignment of user preferences with hotel characteristics. In the
context of a highly digitalized platform economy, the deep integration of multi-dimensional affective perceptions and
heterogeneous contexts for personalized supply-demand matching has become a central research hotspot in inter-
disciplinary recommendation and decision-making systems (Zheng et al., 2018). Dominant approaches include multi-
criteria decision-making and machine learning.
Multi-criteria decision-making methods: Liu et al. ( 2019) proposed a time-semantic-aware Poisson tensor
decomposition approach. Pu et al. ( 2025) developed a two-stage hotel recommendation model integrating customers ’
risk attitudes and preferences. Wang et al. ( 2020) used TF-IDF and Word2Vec to identify key factors and introduced
a decision model incorporating fuzzy image information. Zhao et al. ( 2025) performed ﬁne-grained sentiment
analysis on UGC texts and provided recommendations based on prospect theory.
Machine learning methods: Chen ( 2017) proposed a method combining Fuzzy Weighted Average (FWA) and
Back Propagation Neural Network (BPN). Darraz et al. ( 2025) introduced a hybrid sentiment analysis approach
integrating TextBlob and Multi-Layer Perceptron (MLP). Yin et al. ( 2022) developed a Multi-Scenario Query-Free
Search network (MSQS). Li et al. ( 2023) presented a Feature-based Multi-Task Learning (FMTL) method with multi-
layer feature extraction networks to optimize Click-Through Rate (CTR) and Conversion Rate (CVR). As recom-
mendation algorithms continue to evolve, recent studies have incorporated generative arti ﬁcial intelligence. By
providing personalized, contextualized explanations, generative AI can signi ﬁcantly increase the acceptance rate of
hotel recommendation results (Hatt et al., 2025).
Materials and Methods
This paper proposes a systematic analytical framework that integrates the cognitive logic of hotel management. The
framework uncovers consumers ’ authentic experience preferences within the platform economy and examines core
behavioral issues, including cognitive biases and latent attribute interactions. The computational components in this
section, such as cross-modal data processing and fuzzy mathematical measures, provide a rigorous quantitative
support pathway for investigating complex consumer psychological trade-offs and platform supply-demand
matching.
This section is structured as follows. Section 3.1 develops an evaluation indicator system using structured
extraction to reduce information overload and subjectivity in feature extraction. Section 3.2 integrates cross-modal
data with entropy-based con ﬁdence measurement to address expressive biases from multi-sensory experiences.
Section 3.3 applies a 2-additive measure to quantify synergistic and antagonistic effects among attributes, capturing
complex psychological trade-offs under bounded rationality. Section 3.4 delivers personalized recommendations for
heterogeneous preferences using generalized Shapley value and comprehensive similarity metrics. The overall
recommendation procedure is shown in Algorithm 1.
Algorithm 1. Overall recommendation algorithm ﬂow
Input: The original multi-source review dataset collected from online platforms, comprising an unstructured review
text set R, an attached image set I, and a hotel set HðgÞ representing the historical accommodation records for target
consumer g.Output: An optimized personalized hotel recommendation list tailored to consumers with heterogeneous
preferences.
https://doi.org/10.1057/s41599-026-09225-1 Article in Press
Humanities and Social Sciences Communications

Phase 1: Construction of the Service Attribute Evaluation Indicator System 1. The BERT model and a neural
network classi ﬁer are applied to process the unstructured review text set R. After ﬁltering out irrelevant noise, a
reﬁned textual corpus T is generated.2. Dependency syntactic analysis and the Af ﬁnity Propagation (AP) clustering
algorithm are then employed to extract service features from the re ﬁned corpus T. Based on these extracted features, a
hierarchical evaluation indicator system for service attributes is constructed, denoted as the attribute set
C ¼f cj;ljj ¼ 1; 2; ::::n; l ¼ 1; 2; :::; njg.
Phase 2: Calibration of Cross-Modal Sensory Experience Bias 3. For each hotel hi 2 H, the following procedure
(steps 4 –10) is executed.4. For each review ri;k and associated service attribute cj;l 2 C, the subsequent calculations
are performed.5. The SnowNLP tool generates the initial text sentiment score ScoreðTj;l i;kÞ, and the entropy HðTj;l i;kÞ of
the text probability distribution is computed.6. The text con ﬁdence is calculated based on the maximum entropy
Hmax:conf ðTj;l i;kÞ¼ 1 /C0 HðTj;l i;k Þ Hmax 7. The CLIP model is used to extract visual semantics, from which the sentiment score
ScoreðimgiÞ for the image set is derived, and the entropy HðimgiÞ of the similarity probability distribution is also
calculated.8. Image con ﬁdence is computed from the similarity probability distribution according to the formula:
conf ðimgiÞ¼ 1 /C0 HðimgiÞ Hmax The image with the highest con ﬁdence is selected as the representative visual evidence,
denoted img/C3. Subsequently, the image modal weight ωimg/C3 and the text modal weight ωTj;l i;k are dynamically
assigned.9. The ﬁnal perceived sentiment score after cross-modal fusion is obtained via the weighted update:
ScorefinalðTj;l i;kÞ¼ ScoreðTj;l i;kÞ/C2 ωTj;l i;k þ Scoreðimg/C3Þ/C2 ωimg/C3 10. The inner and outer loops terminate after processing
all reviews and all hotels.
Phase 3: Measurement of Psychological Interaction Effects 11. For each hotel hi 2 H, the following steps (12 –18)
are carried out.12. The independent importance μiðcj;lÞ of each attribute is computed using the historical average of
the fused sentiment scores.13. For each pair of attributes under the same primary indicator cj, the Pearson correlation
coefﬁcient rl;^l i is calculated.14. The joint importance of each attribute pair is de ﬁned as:
μiðcj;l; cj;^lÞ¼ μiðcj;lÞþ μiðcj;^lÞþ rl;^l i 15. Based on the above importance indicators, the 2-additive fuzzy measure μ over
the attribute set C is constructed and then normalized.16. The generalized Shapley value is applied to estimate the
global marginal psychological contribution φiðμ; NÞ for any subset of attributes.17. The TF-IDF algorithm is
employed to extract word frequencies from the reviews, thereby quantifying the customer attention preference,
denoted as TD‑IDF.28. The marginal psychological contributions and the attention weights are integrated to
dynamically generate exclusive feature weights ω/C3 i;j;l for each attribute of each hotel.19. The loop over hotels
concludes.
Phase 4: Heterogeneous Preference-Driven Personalized Decision Recommendation 20. If the target consumer g
is a cold-start user with no historical accommodation records, then steps 21 –22 are executed.21. The dynamic weights
and sentiment scores are aggregated using the generalized Shapley-Choquet integral to obtain the comprehensive
hotel score GG/C0SC i .22. Hotels are ranked in descending order of GG/C0SC i , and the ranked list is output as the
recommendation result.23. Otherwise (i.e., the consumer has historical records), for each candidate hotel h and for
each historical hotel hg 2 HðgÞ of consumer g, steps 24 –27 are performed.24. Collaborative ﬁltering is used to
identify common user groups, and the behavioral similarity simCF ðh; hgÞ is calculated.25. Euclidean distances dw and
ds between feature vectors are computed to construct the weight similarity simwðh; hgÞ and the sentiment similarity
simsðh; hgÞ, respectively.26. The three similarity measures are integrated to calculate the ﬁnal recommendation score
Scoreðg; hÞ for candidate hotel h and user g:Scoreðg; hÞ¼ P hg2Hg simðh; hgÞ27. The inner loop over historical hotels
ends.28. Candidate hotels are sorted in descending order by the ﬁnal recommendation score Scoreðg; hÞ, and a
personalized recommendation list is output.29. The conditional branch concludes.
Article in Press https://doi.org/10.1057/s41599-026-09225-1
Humanities and Social Sciences Communications

Acquisition and preparation of hotel reviews
To accurately extract valid evaluations of service attributes that re ﬂect actual accommodation experiences from
unstructured consumer narratives, and to construct standardized indicators aligned with human cognitive logic, this
paper develops a data-driven processing method.
Let H ¼f hiji¼1; 2;:::;mg denote the collection of hotels, with m representing the total number of establishments.
For a given hotel hi, the gathered reviews are denoted as Ri ¼f ri;kjk ¼ 1; 2; :::; nig, where ri;k refers to the k-th review
about hotel hi, encompassing both textual content and images. Additionally, ni indicates the total number of reviews
associated with hotel hi.
During denoising and validity screening, the system segments review texts into sentences and uses a pre-trained
BERT model to generate context-aware sentence vectors with high-dimensional semantic features, creating a sen-
tence vector space of 3,237,120 sentences. Then, 10,000 samples are randomly selected for manual binary labeling
(validity labels: 0/1) to build a supervised corpus. This corpus is used to train a neural network classi ﬁer that
automatically ﬁlters out noisy reviews irrelevant to actual accommodation experiences.
During indicator extraction, recognizing that consumers often use nouns as carriers of service when expressing
satisfaction, this study uses the Stanford CoreNLP toolkit (Manning et al., 2014) for dependency syntactic parsing
and multi-dimensional word segmentation on screened, valid sentences to extract nouns. After removing irrelevant
nouns from the hotel evaluation, Word2Vec vectorizes the remaining nouns to preserve latent semantic correlations
among consumer perceptions. The Af ﬁnity Propagation clustering algorithm, based on a message passing mechanism
(Frey and Dueck, 2007), then automatically groups semantically similar nouns into distinct experience categories
through dynamic similarity propagation. Combined with the national standard Classi ﬁcation and Evaluation of Star-
Rated Tourist Hotels (GB/T 14308-2010), this process establishes an evaluation indicator system aligned with
consumers’ cognitive logic.
For subsequent discussions, let C ¼f cj;ljj ¼ 1; 2; ::::n; l ¼ 1; 2; :::; njg denote the attribute set, and let cj;l represent
the attribute corresponding to the j-th primary indicator and the l-th secondary indicator, with n indicating the total
number of primary indicators and nj signifying the number of secondary indicators linked to the j-th primary
indicator.
Processing of heterogeneous data
Consumers’ multi-sensory experience expressions (text and images) in online reviews are often inconsistent. Tra-
ditional text-only analysis is prone to cognitive and semantic biases, such as exaggerated subjective descriptions and
social desirability bias, making it dif ﬁcult to accurately assess true satisfaction. This section uses multimodal sen-
timent analysis as a core tool to address biases in consumers ’ multi-sensory expressions on digital platforms. Visual
images, as unintentional symbolic evidence, convey implicit psychological preferences and naturally complement
textual information.
This section proposes a con ﬁdence (Gal and Ghahramani, 2016) evaluation mechanism based on probability
distribution entropy (Shannon, 1948). The image with the highest con ﬁdence is used to dynamically adjust textual
sentiment scores, restoring a more authentic perceived experience. To enable fusion of heterogeneous data within the
same dimension, both textual and visual sentiment scores are mapped to the interval [0, 10].
Text preprocessing
Let Tj;l i;k denote the sentences in review ri;k that pertain to attribute cj;l. The Chinese NLP toolkit SnowNLP analyzes
the text to output the initial probability Ppos Tj:l i:k
/C16/C17
that it conveys positive sentiment. This probability is linearly
https://doi.org/10.1057/s41599-026-09225-1 Article in Press
Humanities and Social Sciences Communications

mapped to [0, 10] to obtain the initial textual sentiment score:
ScoreðTj:l i:kÞ¼ PposðTj:l i:kÞ/C2 10 ð1Þ
To assess the reliability of sentiment judgments, Shannon entropy for binary probability distributions is introduced
to quantify uncertainty. By measuring uncertainty and the dispersion of probability distributions, this method miti-
gates cognitive biases such as exaggerated subjective descriptions and social desirability bias in online consumer
reviews. It also provides theoretical support for preventing cognitive noise accumulation using image con ﬁdence:
HðTj;l i;kÞ¼/C0 X2
i¼1
PðTj;l i;k Þilog2ðPðTj;l i;kÞi þ εÞ ð2Þ
where ε ¼ 10/C09 is introduced as a numerical stability term to mitigate the risk of computational over ﬂow when
calculating the logarithm of probabilities that may equal zero. The maximum entropy value is Hmax ¼ 1. A
normalization function converts the dispersion of this probability space into an intuitive textual decision con ﬁdence
level:
conf ðTj;l i;kÞ¼ 1 /C0 HðTj;l i;kÞ Hmax ð3Þ
The more de ﬁnite and concentrated a text ’s sentiment tendency, the closer the entropy value is to 0 and the higher
the con ﬁdence conf ðTj;l i;kÞ. Conversely, ambiguous semantic meaning results in lower con ﬁdence conf ðTj;l i;kÞ.
Image preprocessing
For the image modality, the CLIP Zero-Shot vision-language perception model is used to directly link visual scenes
with emotional semantics without additional training. First, for each service attribute cj;l, a positive prompt set Qþ and
a negative prompt set Q/C0, each with n elements, are designed such that corresponding words are antonyms. Next, all
images Ij;l i;k ¼f img1; img2; :::; imgIg associated with the review containing sentence Tj;l i;k are extracted. The CLIP
model calculates the semantic matching similarity between each image Ij;l i;k and every prompt set element. Averaging
the positive and negative similarity probabilities pð/C15Þ yields the positive and negative sentiment scores:
ScoreposðimgiÞ¼ 1 n Xn k¼1 pkðimgi; qþ k Þ ð4Þ
and
ScorenegðimgiÞ¼ 1 n X2n k¼nþ1 pkðimgi; q/C0 k Þ ð5Þ
By integrating positive and negative sentiment scores, the ﬁnal emotional intensity of images is mapped to the
interval [0, 10]:
ScoreðimgiÞ¼ð ScoreposðimgiÞ/C0 ScorenegðimgiÞþ 1Þ/C2 5 ð6Þ
Similarly, to assess the reliability of sentiment analysis for each image, the positive and negative similarity
probability distributions are combined and normalized to obtain the similarity probability distribution pðimgiÞ for
Article in Press https://doi.org/10.1057/s41599-026-09225-1
Humanities and Social Sciences Communications

imgi. The entropy of this distribution is calculated as follows:
HðimgiÞ¼/C0
X2n
k¼1
PðimgiÞklnðPðimgiÞk þ εÞ ð7Þ
where PðimgiÞk indicates the k-th element within the similarity probability distribution of imgi, while ε ¼ 10/C09
functions as a numerical stability term. With 2 n prompt words, the maximum entropy value is Hmax ¼ lnð2nÞ. This
value is then converted into a uni ﬁed image con ﬁdence indicator for cross-modal comparison:
conf ðimgiÞ¼ 1 /C0 HðimgiÞ Hmax ð8Þ
Conﬁdence-based heterogeneous information fusion
When consumers’ subjective textual expressions con ﬂict with objective visual content, the system should implement
a certainty-based screening mechanism to prevent cognitive noise accumulation.
All images attached to the review are examined, and the image with the highest con ﬁdence is selected as the most
representative visual evidence, denoted as img/C3. Theoretically, consumers often upload multiple images in a single
review, each capturing different physical spaces or service details (e.g., room views or bathroom facilities). An
image-selection mechanism based on maximum con ﬁdence acts as an “attribute-relevance noise-reduction ﬁlter.” It
automatically removes visual noise unrelated to the evaluated attribute and extracts the most relevant image features.
Based on the principle of credible complementarity between text and image modalities for the same attribute, the
Fig. 1 Heterogeneous data processing processes.
https://doi.org/10.1057/s41599-026-09225-1 Article in Press
Humanities and Social Sciences Communications

dynamic visual fusion weight is calculated as follows:
ωimg/C3 ¼ conf ðimg/C3Þ conf ðimg/C3Þþ conf ðTj;l i;kÞ ð9Þ
The weight assigned to the emotional score of the text is as follows:
ωTj;l i;k ¼ 1 /C0 ωimg/C3 ð10Þ
The emotional score of the ﬁnal comment ri;k regarding the attribute cj;l is obtained through weighted fusion:
ScorefinalðTj;l i;kÞ¼ ScoreðTj;l i;k Þ/C2 ωTj;l i;k þ Scoreðimg/C3Þ/C2 ωimg/C3 ð11Þ
To facilitate a comprehensive understanding of heterogeneous data processing, the speci ﬁc ﬂow of the method is
depicted in Fig. 1.
2-Additive measure on attribute sets
Traditional models (e.g., weighted averaging) often assume attribute independence, which contradicts the complex
decision-making psychology of consumers under bounded rationality. For example, a “good view ” can partially
offset negative perceptions of “cramped space,” while “severely outdated facilities ” may cause a nonlinear decline in
overall satisfaction.
To quantify these nonlinear interaction effects and address the limitation of assuming independent hotel attributes,
this section introduces 2-additive measure (Grabisch, 1997) based on fuzzy measure theory. As a type of non-additive
measure, this metric captures interactions among factors while reducing computational complexity, ensuring rational
weight determination for hotel attributes.
Speciﬁcally, let the attribute set be denoted as N ¼f 1; 2; :::; ng, and the 2-additive measure μ : 2N !½ 0; 1/C138 must
fulﬁll the following conditions:
1. Normativity: μð+Þ¼ 0, μðXÞ¼ 1;
2. 2 Monotonicity: If A /C18 B, μðAÞ/C20 μðBÞ.
The formula for constructing the 2-additive measure of set S /C18 N is as follows:
μðSÞ¼
X
i2S
μðiÞþ
X
fi;jg/C18S
μði; jÞ
where μðiÞ signiﬁes the importance attributed to element i, whereas μði; jÞ indicates the joint importance of elements i
and j.
To limit the interaction scope and reduce computational complexity, this paper proposes a hierarchical modeling
approach: only secondary attributes under the same primary indicator (or primary indicators at a higher level) interact
and trade off directly, while dependencies across different primary indicators are indirectly transmitted through
hierarchical integration at upper levels.
Evaluation of the signi ﬁcance of a single attribute
For hotel hi, the independent importance of each primary indicator cj and secondary indicator cj;l is de ﬁned as the
average feedback from all group samples for that indicator. Review all hotel reviews Ri. If a customer review
mentions cj, extract and combine all sentences referring to cj into a text Tj i:k. Calculate the text-image fused sentiment
score ScorefinalðTj i;k Þ using the method described previously to represent consumer satisfaction with cj.I f cj is not
mentioned, assign a neutral sentiment value of 5 to ScorefinalðTj i;kÞ. The weighted sum of all consumer satisfaction
Article in Press https://doi.org/10.1057/s41599-026-09225-1
Humanities and Social Sciences Communications

scores represents the independent importance of cj for hotel hi, denoted as μiðcjÞ.
μiðcjÞ¼ ScoreiðcjÞaverage ¼
Pni
k¼1
ScorefinalðTj i;kÞ
ni
ð12Þ
where ni signiﬁes the cumulative number of reviews associated with hotel hi.
The independent importance μiðcj;lÞ of secondary indicators within each primary indicator is measured in the same
way.
μiðcj;lÞ¼ Scoreiðcj;lÞaverage ¼
Pni
k¼1
ScorefinalðTj;l i;kÞ
ni
ð13Þ
Determination of importance for pairwise attribute combinations
Consumers’ psychological trade-offs and con ﬂicts across service attributes under bounded rationality are re ﬂected in
the correlation of satisfaction scores at the group level. This paper assumes that the Pearson correlation coef ﬁcient
(Pearson, 1894) objectively measures the statistical correlation between attributes in affective perception. Based on
this premise, the study examines the potential psychological trade-offs and con ﬂicts of consumers under bounded
rationality that this coef ﬁcient may reﬂect. The direction and magnitude of these latent joint evaluations are intuitively
reﬂected by standardized covariance.
For hotel hi, when determining the signi ﬁcance of any pairwise combinations of ﬁrst-level indicators, let us
consider a speciﬁc attribute combination fcj; c^jg, where j≠^j. To elucidate the method for calculating the importance of
this attribute combination, one should analyze all customer reviews Ri associated with the hotel. From each review,
extract the emotional scores, ScorefinalðTj i;kÞ and ScoreaverageðT ^j i;kÞ, for attributes cj and c^j, respectively, and compute
the Pearson correlation coef ﬁcient between these two attributes to quantify the interaction effect:
rj;^j i ¼
Pni
k¼1ðScorefinalðTj i;kÞ/C0 ScoreiðcjÞaverageÞðScorefinalðT ^j i;kÞ/C0 Scoreiðc^jÞaverageÞ
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ ﬃ
ðScorefinalðTj i;kÞ/C0 ScoreiðcjÞaverageÞ 2
q ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ ﬃ
ðScorefinalðT
^j
i;kÞ/C0 Scoreiðc^jÞaverageÞ
2
r ð14Þ
The signi ﬁcance of the attribute combination fcj; c^jg is as follows:
μiðcj; c^jÞ¼ μiðcjÞþ μiðc^jÞþ rj;^j i ð15Þ
Similarly, the joint importance of each pair of secondary attributes is measured in the same way:
μiðcj;l; cj;^lÞ¼ μiðcj;lÞþ μiðcj;^lÞþ rl;^l i ð16Þ
When r> 0, the two service attributes show a positive correlation in affective scores, which may indicate a strong
“synergistic-compensation effect ” in consumer psychology. When r< 0, a negative correlation appears, potentially
pointing to a latent “cask-antagonism or penalty effect. ” Relying on the assumed correlation of affective attributes,
this metric explores consumers ’ behavioral trade-offs under bounded rationality when evaluating intrinsically related
attributes.
https://doi.org/10.1057/s41599-026-09225-1 Article in Press
Humanities and Social Sciences Communications

Constructing the 2-additive measure on attribute sets
Following the assessment of the signi ﬁcance of individual attributes and the combinations of attribute pairs within the
attribute set, the 2-additive measure μðSÞ for set S is constructed using the approach above, with normalization
applied to ensure the measure ’s validity.
For hotel hi, the construction of the 2-additive measure is executed for any subset S of the ﬁrst-level indicator set:
μiðSÞ¼
X
cj2S
μiðcjÞþ
X
fcj;c^jg/C18S
μiðcj; c^jÞ ð17Þ
Subsequently, formulate the 2-additive measure for any subset Sj of secondary indicators in relation to the primary
indicator cj:
μiðSjÞ¼
X
cj;l/C18Sj
μiðcj;lÞþ
X
fcj;l;cj;^lg/C18Sj
μiðcj;l; cj;^lÞ ð18Þ
Following the normalization process, the construction of the 2-additive measure for all subsets of primary and
secondary indicators has been successfully completed.
Comprehensive and personalized recommendations
To fully utilize fuzzy measures for capturing complex correlations, the traditional aggregation framework must be
restructured. The discrete Choquet integral (Choquet, 1954) formula is as follows:
Cμðf Þ¼
Xn
i¼1
f ðxðiÞÞðμðAiÞ/C0 μðAiþ1ÞÞ
where f ðxðiÞÞ denotes the sorted attribute values, μ is the fuzzy measure, Ai ¼f i; :::; ng and Anþ1 ¼ +.
Although power set measures ﬂexibly assign weights to subsets, computation is typically limited to local, chained
correlations between adjacent ordered subsets, hindering the global reconstruction of the complex psychological
interaction trade-off network. To address this, the generalized Shapley value (Meng and Chen, 2014) is introduced.
By accurately quantifying the global marginal psychological contribution of any subset of service attributes to overall
satisfaction, this function is combined with the Choquet integral to create a generalized Shapley-Choquet integral.
This integrated approach comprehensively quanti ﬁes the marginal contributions of ordered coalitions and derives the
overall evaluation score for hotels. It fully characterizes multi-attribute synergy from a global perspective and
provides a robust foundation for subsequent numerical analysis and personalized recommendations.
Ascertain the weights of the attributes
Within the 2-additive measure framework, the generalized Shapley value of any attribute i (which reduces to the
standard form when the ordered subset ( S ¼f ig) accurately captures the global marginal contribution of the attribute
to consumer satisfaction, accounting for all higher-order interactions. The calculation formula is as follows:
φiðμ; NÞ¼ 3 /C0 n 2 μðiÞþ 1 2 X j2Nnfig ðμði; jÞ/C0 μðjÞÞ
where n denotes the number of elements within the set.
In addition to global marginal psychological contributions, consumers ’ attention allocation across service attributes
is a key determinant of ﬁnal recommendation weights. To objectively measure this attention bias from information
salience, the Term Frequency-Inverse Document Frequency (TF-IDF) algorithm (Salton and Buckley, 1988) is used
Article in Press https://doi.org/10.1057/s41599-026-09225-1
Humanities and Social Sciences Communications

to adaptively extract the salience of textual attribute words from large-scale unstructured reviews:
TF /C0 IDFðt; d; DÞ¼ TFðt; dÞ/C2 IDFðt; DÞ
where TFðt; dÞ reﬂects the frequency of a word ’s occurrence in a single document; IDFðt; dÞ reduces the weight of
words that commonly appear in most documents. This indicator automatically eliminates interference from general
vocabulary and accurately captures inherent attention bias patterns among speci ﬁc consumer groups.
By analyzing the attribute terms in AP clustering, we can derive the levels of consumer attention to various
attributes associated with each hotel:
TF /C0 IDFðcj;l; Ri; RÞ¼ TFðtðcj;lÞ; RiÞ/C2 IDFðtðcj;lÞ; RÞð 19Þ
where tðcj;lÞ refers to the descriptive term corresponding to attribute cj;l, Ri signiﬁes the review document pertaining
to hotel hi, and R denotes the corpus that consists of all hotel review documents.
Through cross-layer satisfaction transmission, this study integrates the generalized Shapley value of primary
indicators into secondary indicators. Combined with objectively captured consumer attention patterns, personalized
decision weights are dynamically generated for each hotel attribute. This approach moves beyond traditional
homogeneous algorithm-based recommendations, ensuring ﬁnal results closely align with the personalized accom-
modation needs of diverse user groups:
ω/C3 i;j;l ¼ φ/C3 i ðcj;lÞ/C2ð 1 þ TF /C0 IDFðcj;l; Ri; RÞÞ ð20Þ
Recommendation
Based on the distribution of historical accommodation data for consumer groups, the system adaptively employs two
differentiated, context-driven recommendation schemes. For consumers without historical accommodation records,
individual preferences for various attributes cannot be identi ﬁed. Therefore, the system generates global recom-
mendations using the hotels ’ comprehensive service quality characteristics. Dynamic weights and multimodal fused
sentiment scores are aggregated with the generalized Shapley-Choquet integral to produce the comprehensive score
CG/C0SC i , which is ranked in descending order. The resulting hotel evaluation values are used directly for recom-
mendation ranking.
CG/C0SC i ¼ Xn
j¼1
Xnj
l¼1
ω/C3 i;j;l /C2 Scoreiðcj;lÞaverage ð21Þ
For consumer g with historical accommodation records, let Hg ¼f hgjg ¼ 1; 2; :::; mgg represent the set of hotels
recorded in a consumer ’s accommodation history, where Hg /C18 H and mg denotes the total number of hotels that the
consumer has previously stayed in. To begin with, for each prospective hotel h 2f HnHgg, it is essential to develop
both a weight vector Wh and an emotional vector Sh:
Wh ¼½ ω/C3 h;1;1; ω/C3 i;1;2; :::; ω/C3 i;n;nj /C138 ð22Þ
and
Sh ¼½ Scorehðc1;1Þaverage; Scorehðc1;2Þaverage; :::Scorehðcn;nj Þaverage/C138 ð23Þ
The following three hybrid similarity measures are deduced from three dimensions: group commonality, hetero-
geneous preference, and performance consistency.
https://doi.org/10.1057/s41599-026-09225-1 Article in Press
Humanities and Social Sciences Communications

(1) Behavioral Similarity: A collaborative ﬁltering mechanism quanti ﬁes the overlap in behavioral trajectories
between two hotels by identifying commonalities among user groups who have stayed at both hotels.
simCF ðh; hgÞ¼ jUh \ Uhg j jUh ∪ Uhg j ð24Þ
where Uh and Uhg represent the sets of users who have previously resided at hotel h and hotel hg,
respectively.
(2) Weight Similarity and Sentiment Similarity: To prevent the severe misjudgments of traditional cosine similarity
in bounded rational decision-making scenarios —such as “high psychological weight with low actual sentiment ” or
“low psychological weight with high actual sentiment ”—this paper constructs a transformation function based on
spatial Euclidean distance. First, the absolute Euclidean distances dW and dS between feature vectors of candidate and
historical hotels are calculated:
dW ðh; hgÞ¼
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
Xn
j¼1
Xnj
l¼1
ðω/C3 h;j;l /C0 ω/C3 hg;j;lÞ2
vuut ð25Þ
and
dSðh; hgÞ¼
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ ﬃ
Xn
j¼1
Xnj
l¼1
ðScorehðcj;lÞaverage /C0 Scorehg ðcj;lÞaverageÞ2
vuut ð26Þ
Next, employ Euclidean distance to assess similarity.
simW ðh; hgÞ¼ 1 1 þ dW ðh; hgÞ ð27Þ
and
simSðh; hgÞ¼ 1 1 þ dSðh; hgÞ ð28Þ
After computing weight and sentiment similarity from the three heterogeneous features above, all three similarities
are summed to calculate the ﬁnal recommendation score for candidate hotel h and user g:
Scoreðg; hÞ¼
X
hg2Hg
simðh; hgÞ ð29Þ
The recommendation system ranks candidates in descending order by score and generates an exclusive perso-
nalized recommendation list for target consumers, accounting for psychological interaction trade-offs and scenario-
speciﬁc demands.
Case application
To evaluate the effectiveness of the proposed framework in explaining consumer behavior and platform-mediated
evaluations, this section presents a case study using online review data from 789 hotels collected on Ctrip. It details
the workﬂow, including data collection, indicator construction, and personalized recommendation. Integrating image-
text fusion sentiment analysis, quantitative measurement of psychological interaction effects, and comparative
experiments, this paper thoroughly examines consumers ’ actual decision-making during hotel evaluation. The
research demonstrates the analytical model ’s practicality and provides empirical evidence for understanding con-
temporary hotel review culture and complex experiential characteristics.
Article in Press https://doi.org/10.1057/s41599-026-09225-1
Humanities and Social Sciences Communications

Data crawling
For the case analysis, to obtain a reliable empirical social science corpus re ﬂecting consumers’ actual accommodation
experiences, this paper collects online review data for 789 hotels from the Ctrip website, spanning October 2021 to
November 2024. The dataset includes usernames, review texts, and attached images. Each hotel has more than 300
reviews, and all-star ratings are represented among the 789 hotels. This compilation of hotels will be denoted as
H ¼f hiji ¼ 1; 2; :::; 789g.
Construction of evaluation index system
To convert unstructured consumer narratives into structured evaluation dimensions aligned with human decision-
making logic, this study screens valid reviews and clusters the data using the methods described in Section 3. In
accordance with the Classi ﬁcation and Evaluation of Star-Rated Tourist Hotels (GB/T 14308-2010), a hotel eva-
luation indicator system is constructed with seven primary indicators —including infrastructure and living amenities
Table 1 Evaluation index system.
Primary indicator Secondary indicator
infrastructure Windows, balcony, Room size, Bed, Interior decoration, Audio-visual equipment, air conditioning.
Amenities for living Furniture, wireless network, toilet, Household items, Laundry Room, Parking Lot, Takeaway service.
Leisure and recreational facilities Swimming, ﬁtness, other sports, amusement park, show venue, leisure, bar.
Service and Reception Front desk service, luggage service, gift-giving, airport and station pick-up and drop-off, extended service,
catering service, room type upgrade.
Transportation and Location High-speed railway station, airport, bus, subway, scenic area, commercial district.
Room quality and sensory experience Room smell, room lighting, room air permeability, room noise, scenery, facing the street.
Customer experience Cost-performance ratio, family-friendly, safety, privacy, comfort.
Table 2 Display of positive
and negative prompt words
for some attributes.
Attribute Positive prompt words Negative prompt words
Furniture The hotel furniture is beautiful and durable.
The hotel furniture is comfortable and tidy.
The hotel furniture is old and damaged.
The hotel furniture is dirty, messy, and poor.
Wireless network The router in the hotel room is lit up.
The Wi-Fi password card on the table.
The mobile phone shows full signal.
Laptop networking in the guest room.
The TV synchronously displays the Wi-Fi
connection status.
The router ’s fault light is off.
There is no Wi-Fi password card on the table.
The mobile phone has no signal.
The laptop cannot connect to the network.
The TV does not display the Wi-Fi status.
Bathroom The ﬂoor is non-slip and free of standing
water.
Chrome-plated high-end hardware.
Floating basin.
Frameless glass partition.
Powerful exhaust system.
Mildew and standing water in ﬂoor gaps.
Inferior rusty hardware.
Bulky ﬂoor-standing basin.
Cheap shower curtain.
Poor ventilation and dampness.
Daily necessities Daily necessities are independently sterilized
and packaged.
Daily necessities are made of wear-resistant
and anti-fouling materials.
Bulk daily necessities.
Daily necessities are faded and damaged.
Laundry Wash and dry sorting line.
Classiﬁed washing process.
Sterile packaged detergent.
Household washing machine.
Piled and mixed laundry.
Residual washing foam.
Parking lot The hotel parking lot is spacious and tidy
with clear signage.
The hotel parking lot is narrow and chaotic
with blurred signage.
Food delivery
service
Robot food delivery, with the meals intact. Takeout is piled up at the front desk, and oil
stains are splashing from the meals.
https://doi.org/10.1057/s41599-026-09225-1 Article in Press
Humanities and Social Sciences Communications

—and 45 secondary indicators such as room area and bathroom, as shown in Table 1. The collection of attributes is
represented as C ¼f cj;ljj ¼ 1; 2; ::::7; l ¼ 1; 2; :::; 45g.
Heterogeneous data processing and analysis
After constructing the evaluation indicator system, the textual and image data in hotel reviews are integrated and
processed. First, positive cue words Qþ and negative cue words Q/C0 are identiﬁed for each attribute cj;l. Table 2 lists
the positive and negative cue words for the secondary indicators under the primary indicator “living amenities.” Once
these cue words are determined, the sentiment score for each attribute in the review is calculated. If the review
Fig. 2 Image-selection Sensitivity Analysis.
Fig. 3 Affective integration of graphics and texts.
Article in Press https://doi.org/10.1057/s41599-026-09225-1
Humanities and Social Sciences Communications

includes images, the textual sentiment score is adjusted based on the image with the highest con ﬁdence, and this
revised score is used for subsequent calculations.
To assess the effectiveness of CLIP-based affective scoring, this study resampled 120 “attribute-image” pairs from
real reviews for independent manual three-category annotation validation. After mapping continuous CLIP scores to
matching categories, overall agreement with human judgments reached 88.33%, with a Cohen ’s Kappa coef ﬁcient of
0.784. The accuracy for positive and negative classes was 98.7% and 93.8%, respectively, supporting the reliability of
visual evaluation. This paper also includes an image-selection sensitivity analysis to justify the Top-1 (highest-
conﬁdence) strategy. Analysis of 100 multi-image reviews (680 images total) revealed substantial differences in
affective scores across images within the same review and attribute, with a mean intra-group standard deviation of
1.98. As shown in Fig. 2, the mean absolute error (MAE) between Top-1 scores and full-image average scores was
1.89—a highly signi ﬁcant difference (Wilcoxon test, p < 0.001). This result suggests that undifferentiated averaging
of all images introduces irrelevant scene noise and dilutes true affective polarity. By contrast, the Top-1 screening
strategy identi ﬁes the most reliable visual evidence and demonstrates practical value as a noise-reduction ﬁlter.
Figure 3 shows the data and process for fusing text-image sentiment scores for a single review.
Unimodal text analysis in hotel experience evaluation is frequently compromised by subjective expressions and
cognitive biases—such as semantic exaggeration or information omission —which impede the accurate assessment of
consumer satisfaction. To validate the utility of cross-modal sensory evaluation within the proposed recommendation
framework, this study conducts a comparative analysis between text-only and text-image fusion modalities. The
former captures users ’ subjective perceptions at the semantic level, whereas the latter calibrates textual biases by
leveraging visual features extracted from images (e.g., rectifying distorted hygiene descriptions through actual guest
room photographs). The subsequent analysis examines the scoring patterns of both modalities across primary indi-
cators and other attributes, highlights the corrective in ﬂuence of images on textual assessments, and demonstrates the
Fig. 4 The average adjusted emotional score of visual information.
https://doi.org/10.1057/s41599-026-09225-1 Article in Press
Humanities and Social Sciences Communications

optimization ef ﬁciency achieved by the fusion modality. These ﬁndings furnish empirical evidence supporting the
effectiveness of the multimodal fusion approach in capturing genuine consumer psychology.
Figure 4 presents the average correction values of textual sentiment scores adjusted by images for the seven
primary indicators in the text-image fusion modality. Overall, all service indicators exhibit corrections for psycho-
logical biases in both positive and negative directions.
Among the green bars, the User Experience indicator shows the highest positive correction value at 1.473. Real
images of guest rooms and surroundings visualize positive psychological experiences that are inadequately described
in text, compensating for the consumers ’ limited linguistic expression of satisfying hotel experiences.
Among the red bars, the Convenience Facilities indicator displays the largest negative correction value at −1.316.
Textual evaluations of convenience facilities are highly in ﬂuenced by consumers ’ initial expectations and the
anchoring effect, leading to over-idealized semantic bias. Images disrupt the sensory ﬁlter of textual descriptions and
objectively reveal overstated satisfaction with convenience facilities in written narratives.
These two-way corrections reveal “expression bias ” and “visual recti ﬁcation” mechanisms in platform-mediated
evaluations. Textual reviews tend to show positive exaggeration due to cognitive constraints and social desirability
expectations. Images serve as unintentional symbolic evidence and restore experiences more objectively. Identifying
two-way corrections helps dissect the complex psychological motives underlying online review behavior from a
social science perspective. Textual evaluations often re ﬂect cognitive constraints or social desirability bias. The
multimodal fusion mechanism mitigates such information distortion. Introducing unintentional visual evidence
provides a necessary pathway to recover authentic user experience within the platform-mediated consumption eco-
system. This conclusion aligns with recent academic ﬁndings in hotel management. These studies indicated that
unstructured visual images compensated for the limitations of textual semantics and served as key cues that convey
authentic experiential perceptions and build social trust within the platform-mediated ecosystem (Ma et al., 2018).
Figure 5 presents the optimization of evaluation dispersion achieved by the fused modality, measured as a
percentage reduction in standard deviation. The Recreation indicator records an 8.5% reduction in standard deviation,
ranking ﬁrst among the seven indicator categories. This result demonstrates that text-image fusion signi ﬁcantly
lowers the dispersion of recreation-related evaluations. The evidence con ﬁrms the “visual standardization ” effect in
platform-mediated consumption from a social science perspective. In conventional online review behavior, textual-
only expressions often produce substantial perceptual divergence due to individual differences in vocabulary. Images
function as shared physical references and effectively reduce such cognitive disparities. This ﬁnding demonstrates
Fig. 5 Multimodal assessment stability improvement.
Article in Press https://doi.org/10.1057/s41599-026-09225-1
Humanities and Social Sciences Communications

that multimodal fusion extends beyond algorithmic noise reduction. It provides a theoretical tool for understanding
how consumers bridge semantic gaps and form group consensus about authentic user experience.
Fig. 6 . Hotel ranking comparison.
Fig. 7 Comparison of weight variances.
https://doi.org/10.1057/s41599-026-09225-1 Article in Press
Humanities and Social Sciences Communications

Analysis of attribute interaction effects
Grabisch (1996) demonstrated the importance of considering attribute interactions in multi-attribute decision-making
through mathematical proofs and practical applications. Based on consumer feedback, this study constructs a
2-additive fuzzy measure and introduces the generalized Shapley value. This function precisely quanti ﬁes the
marginal contribution of any service subset to overall satisfaction. Assuming that statistical correlation objectively
maps affective associations, it simulates the mental-account-driven logic behind synergistic-compensation or
antagonistic behaviors in consumer decision-making. This approach offers a quantitative perspective for analyzing
higher-order and global experience interaction effects among consumers.
Figure 6 shows the ranking changes of hotels that average in the top ten before and after incorporating generalized
Shapley value. Overall, hotel rankings ﬂuctuate signi ﬁcantly depending on whether generalized Shapley value is
used.
For example, Hotel A7 ’s ranking rises signi ﬁcantly after incorporating generalized Shapley value. The generalized
Shapley value is shown to capture the hotel ’s attribute synergy potential, which traditional methods overlook. By
quantifying global interactions, this approach recti ﬁes evaluation biases dominated by local correlations, rendering
the ranking more consistent with consumers ’ actual experiences.
Figure 7 uses Hotel A5 as an example to illustrate how generalized Shapley values ﬁne-tune local attribute
interactions. Generalized Shapley values allocate weights more evenly to the “Recreation” and “User Experience ”
indicators. This ﬁnding indicates that conventional evaluation methods tend to overemphasize local correlations and
exaggerate the independent contribution of individual indicators. The result suggests that consumer decisions do not
depend solely on scores of independent attributes. Instead, they re ﬂect combined in ﬂuences from synergistic com-
pensation mechanisms within mental accounts. The analysis clari ﬁes that consumer decision-making is not a linear
summation of isolated attributes but a complex psychological process rooted in holistic user experience. Under-
standing synergy and interaction among attributes holds signi ﬁcant theoretical value for interpreting the motives
behind online review behavior within the platform-mediated consumption ecosystem. This observation addresses
broader theoretical debates on the asymmetric response mechanism of service attributes in tourist consumer behavior.
Fig. 8 . Heat map of ﬁrst-level indicators.
Article in Press https://doi.org/10.1057/s41599-026-09225-1
Humanities and Social Sciences Communications

In practice, consumer evaluation models are not simple linear summations. They depend on intricate psychological
trade-offs, such as synergy or compensation, among speci ﬁc attributes (Bi et al., 2019).
Figure 8 takes all hotels as samples to globally visualize the interaction intensity of primary indicators and verify
the core value of the generalized Shapley value:
In the heatmap, the cross-cell for Accessibility and User Experience shows the darkest color, indicating strong
global interaction between these indicators. Comparing cross cells horizontally reveals moderate to high interactions
(dark blue tones) between Infrastructure and Convenience Facilities, Infrastructure and Recreation, and Livability and
Hospitality. This demonstrates that the generalized Shapley value overcomes the constraint of adjacent ordered
subsets, extending attribute interactions from local chained correlations to global networked synergy. It fully
visualizes multidimensional and cross-layer interaction networks in hotel evaluation —such as
“Infrastructure–Convenience Facilities –Recreation Experience ” and “Livability–Hospitality–User Experience ”—
providing a global perspective for understanding attribute synergy effects.
Table 3 reports the average contribution ratios of four groups of key service indicators to overall hotel evaluations.
The calculation synthesizes differences in weights and psychological interaction strength across indicators in the
sample hotels. Among these groups, {Accessibility, User Experience} ranks ﬁrst, with an average contribution share
of 35.92%. This combination serves as the core interacting attribute set that dominates overall consumer satisfaction.
This ﬁnding reveals the dual-driver compensation logic in consumer decision-making within the platform-mediated
consumption ecosystem. The synergistic effect of accessibility conditions and affective value far exceeds the simple
summation of isolated factors. From a behavioral economics perspective, this quantitative result con ﬁrms that
authentic user experience does not arise from isolated ratings of individual services. Instead, it re ﬂects a complex
Table 3 The contribution
proportions of key primary
indicators.
Interactive attribute
set
{Infrastructure,
convenience facilities}
{Accessibility, user
experience}
{Recreation,
hospitality}
{Livability,
infrastructure}
Mean value of
contribution
proportion
22.32% 35.92% 30.46% 23.62%
Fig. 9 Comparison of attribute contribution degrees.
https://doi.org/10.1057/s41599-026-09225-1 Article in Press
Humanities and Social Sciences Communications

psychological process involving holistic synergy and trade-offs across multi-dimensional scenarios under bounded
rationality.
Figure 9 illustrates how the contribution values of sub-attributes change under each primary indicator. Within
Accessibility, the orange polygon expands signi ﬁcantly to cover sub-dimensions such as Bus, Subway, Scenic Spot,
and Business District after incorporating the generalized Shapley value. The core logic is as follows: global marginal
contribution calculations using the generalized Shapley value reveal that the intrinsic value of Accessibility arises
from synergy between transportation networks (Bus/Subway) and practical usage scenarios (Scenic Spot, Business
District). Different combinations of transportation modes and scenarios yield distinct overall marginal contributions.
Quantifying these global interactions directly reshapes attribute weight distribution. Attributes with initially low
weights (e.g., Bus, Scenic Spot) gain higher contribution shares through high-order synergy with other attributes. In
contrast, the weight share of the Airport attribute, which depends on local correlations, decreases. This approach
ultimately calibrates the true contribution of each attribute to the comprehensive evaluation.
Consumers evaluate “convenience” not on isolated features (e.g., proximity to airports) but on scenario-based
demand bundles (e.g., the synergy among buses, scenic spots, and business districts). The generalized Shapley value
effectively simulates these complex psychological trade-offs and provides a novel instrument for analyzing demand
heterogeneity in platform-mediated evaluations.
Within the User Experience dimension, the orange polygon expands to include sub-dimensions such as Family
Friendly, Safety, and Comfort after introducing the generalized Shapley value. The underlying logic is that the
generalized Shapley value reveals the core of “user experience” lies in the synergy of multiple demands. For example,
in family travel scenarios, high-order interactions among family-friendly facilities, safety guarantees, and accom-
modation comfort produce an overall marginal contribution that far exceeds the local contribution of cost-
performance alone. Quantifying these global interactions directly restructures attribute weights. Attributes previously
underestimated, such as family friendliness and safety, experience a substantial increase in contribution share due to
the global value of synergy. In contrast, the weight of standalone cost-performance decreases because of its limited
connection to other demands. The expanded orange polygon across multiple dimensions accurately re ﬂects that user
experience depends on the synergy of diverse demands.
Comparing multi-dimensional data before and after introducing generalized Shapley value clearly demonstrates its
optimization effects on the hotel evaluation system. In key indicator analysis, high-value interaction combinations are
accurately identi ﬁed, breaking the limitations of local correlations in traditional methods. Corrections to primary
indicators and attribute contributions for individual hotels follow evaluation logic driven by global interactions. The
Fig. 10 The heatmap of Spearman correlation coef ﬁcient matrix.
Article in Press https://doi.org/10.1057/s41599-026-09225-1
Humanities and Social Sciences Communications

heatmap visualizes high-order interaction networks, enabling comprehensive interpretation of complex attribute
correlations.
In summary, generalized Shapley value reshape the hotel evaluation system, from attribute interactions to eva-
luation logic. They overcome the analytical limitations of Choquet integrals in traditional frameworks, precisely
capture global and high-order interaction effects, and demonstrate clear value in optimizing evaluation models and
restoring real consumer experience correlations. Their effectiveness underscores the necessity of analyzing attribute
interactions in hotel evaluation.
Comparative analysis
This study employs three research methods to comprehensively analyze hotel review texts: the Choquet integral
method (CIM), interactive multi-criteria decision-making method (TODIM), and simple mean sentiment score
method (SMSSM). The comparative analysis evaluates the Choquet integral hybrid similarity algorithm, the colla-
borative ﬁltering method (CFM), and TODIM, which uses sentiment score amplitudes for weighting. Using multi-
dimensional visualization, the research compares ranking consistency and weight allocation differences, highlighting
how each algorithm simulates human decision-making logic. The detailed analysis is as follows:
Figure 10 shows the variation in pairwise ranking consistency coef ﬁcients between the proposed method and
traditional approaches, including TODIM, CIM, and SMSSM. The proposed method exhibits distinctly different
consistency performance because it adaptively emphasizes correlations among indicators by hotel type, thereby
overcoming the limitations of uni ﬁed evaluation criteria in conventional algorithms. This transformation signals a
shift in platform recommendation systems from algorithmic logic to consumer-behavioral logic: the psychological
salience of any single attribute varies with consumption scenarios, re ﬂecting bounded rationality as consumer
preferences adjust to usage context.
Figure 11 shows that the Relative Standard Index of Average Rank Difference (RSI) bar chart reveals signi ﬁcant
ranking discrepancies between the proposed method and classical approaches, including TODIM, CIM, and SMSSM.
In hotel recommendations, the proposed method identi ﬁes high-quality hotels often overlooked by traditional
algorithms. For example, small boutique hotels with unique design styles and personalized services are often
neglected by algorithms that use ﬁxed weights. In contrast, the proposed dynamic algorithm accounts for correlations
among evaluation indicators and prioritizes such distinctive hotels. These results demonstrate that the algorithm
innovates on the traditional ranking system and effectively meets travelers ’ demands for personalized, diverse
accommodation experiences.
Fig. 11 The heatmap of Spearman correlation coef ﬁcient matrix.
https://doi.org/10.1057/s41599-026-09225-1 Article in Press
Humanities and Social Sciences Communications

This study experiments with 79 users who each have over 10 hotel check-in records. For data analysis, 60% of
each user ’s hotel consumption data is used for preference modeling, while the remaining 40% validates the per-
formance of the proposed personalized recommendation algorithm. To rigorously evaluate algorithm performance,
this study calculates the mean and standard deviation of NDCG@10 scores for each method across 79 users. It also
applies the Wilcoxon signed-rank test to assess statistical signi ﬁcance. As shown in Table 4, the proposed method
achieves the highest average score (0.7356 ± 0.0469). Statistical test results show that, for real-consumer choice
ranking prediction, the proposed method signi ﬁcantly outperforms the Choquet integral method (CIM,
0.6905 ± 0.0507), collaborative ﬁltering method (CFM, 0.6455 ± 0.1040), and TODIM (0.4995 ± 0.0247). All
compared p-values are highly signi ﬁcant (p < 0.001). NDCG@10 is a core metric measuring how closely the top-10
recommendations match the ideal ranking; higher values indicate greater alignment with consumers ’ ideal selections.
The proposed algorithm establishes a ranking logic based on dynamic correlations among hotel attributes, adapts to
travelers’ diverse preferences, and ef ﬁciently arranges cost-effective hotel options in the recommendation list. Most
traditional algorithms use ﬁxed weights and a single theoretical framework, overlooking the psychological trade-off
mechanism of bounded rationality. In contrast, by leveraging cross-modal fusion and dynamic interactive weights, the
proposed algorithm adapts to heterogeneous social preferences and demonstrates clear advantages in recommendation
accuracy and psychological adaptation.
This statistical test result demonstrates the superiority of the algorithm and delivers a key social science insight.
Consumer decision-making in real scenarios does not follow a linear summation of individual attributes. Instead, it
reﬂects context-dependent, intricate psychological trade-offs. The proposed model signi ﬁcantly outperforms con-
ventional linear models such as TODIM and CIM by accurately capturing synergistic effects under bounded
rationality. As a result, it achieves a high goodness-of- ﬁt for actual choice behavior within platform-mediated
consumption.
In summary, the recommendation model developed in this paper —based on generalized Shapley-Choquet integral
and dynamic interaction weights —stands apart from traditional algorithms such as TODIM and collaborative ﬁltering
in hotel recommendation ranking. This model introduces an operational mechanism aligned with consumers ’ actual
experiential trade-offs. Supported by ranking schemes tailored to real decision-making scenarios, it advances hotel
recommendation from homogeneous algorithmic screening to personalized experience customization that closely
matches human psychological expectations.
To clarify each innovative module ’s contribution to overall recommendation performance, this study conducts
ablation experiments using NDCG@10 as the core evaluation metric. Four variant models are created by removing
the personalized similarity, attribute-interaction modeling, multimodal fusion, and dynamic weight modules,
respectively. The experimental results appear in Table 5.
Experimental results indicate that the full model achieves optimal performance at 0.7356. Removing individual
modules causes recommendation performance to decline to varying extents. Excluding the personalized similarity
Table 4 Comparison of
various methods. Methods New method CIM CFM TODIM
NDCG@10 (Mean ± SD) 0.7356 0.0469 0.6905 0.0507 0.6455 0.1040 0.4995 0.0247
Wilcoxon test p-value - <0.001 <0.001 <0.001
Table 5 Ablation
experiment results and
performance contribution of
each module.
Model variants Removed component NDCG@10 Drop (pp) Relative drop
Full Model - 0.7356 - -
w/o Personalized
Similarity
Personalized Similarity (Degraded to CF) 0.6455 −9.0 −12.2%
w/o Interaction Attribute Interaction (Degraded to Linear
Weighting)
0.6537 −8.2 −11.1%
w/o Multimodal Multimodal Fusion (Text-only Sentiment) 0.6945 −4.1 −5.6%
w/o Dynamic Weighting Dynamic Weighting (Global Static Weight) 0.6857 −5.0 −6.8%
Article in Press https://doi.org/10.1057/s41599-026-09225-1
Humanities and Social Sciences Communications

module reduces performance to 0.6455, a 9.0% decrease. Omitting the attribute interaction modeling module lowers
performance to 0.6537, representing an 8.2% decrease. These ablation results quantitatively demonstrate, from a
social science perspective, that consumer decision-making within platform-mediated consumption depends heavily
on precise matching of individual preferences (12.2% performance contribution) and complex interactions among
psychological attributes (11.1% performance contribution). The performance collapse of conventional models after
module exclusion occurs because these models ignore psychological compensation and penalty mechanisms
embedded in authentic user experience. Removing the dynamic weight and multimodal fusion modules results in
performance declines of 5.0% and 4.1%, respectively. These ﬁndings con ﬁrm that multimodal data denoising and
adaptive attention allocation serve as essential auxiliary modules. Synergistic effects across all modules support the
optimal performance of the full model. This evidence comprehensively veri ﬁes the effectiveness and necessity of all
innovative mechanisms proposed in this paper.
Managerial implications and research opportunities
This study transforms algorithmic innovations into actionable strategies with substantial hotel management value in
the platform economy ecosystem. The outputs from the data model integrate into a consumer behavior insight system.
This system aligns with the theoretical core of modern hospitality Customer Experience Management (CEM).
Enterprises conduct cross-analysis of multisensory feedback and cognitive data to diagnose and reshape the full-
journey experiential value of consumers (Kandampully et al., 2018). First, the method standardizes attribute weights
and affective scores to map consumers ’ attention priorities and authentic satisfaction levels toward service indicators
during decision-making. Next, the K-Means clustering algorithm structures data and groups hotel-attribute combi-
nations with similar consumer value perceptions. Building on this foundation, the approach adopts the market
positioning dimension of hotel star rating and delivers multi-angle data visualization through two-dimensional and
three-dimensional scatter plots. These visual outputs reveal complex psychological interconnections among consumer
attention allocation, affective perceptions, and brand tiers. Finally, to strengthen the practical guidance of analytical
conclusions, the analysis further explores the interior of each cluster. It identi ﬁes and highlights representative typical
Fig. 12 . 2D distribution of attribute weight and sentiment score by star level.
https://doi.org/10.1057/s41599-026-09225-1 Article in Press
Humanities and Social Sciences Communications

attribute points. These points correspond to critical touchpoints within consumer decision paths and provide data-
driven insight for targeted marketing, service redesign, and strategic positioning among star-rated hotels with dif-
ferentiated pro ﬁles.
Managerial implications
To extract actionable managerial insights from extensive customer experience feedback, this study translates algo-
rithm outputs into a consumer behavior insight framework. First, attribute weights and sentiment scores are stan-
dardized to accurately map consumer attention priorities for service indicators and genuine satisfaction during
decision-making. Next, the K-Means clustering algorithm structures the dataset, grouping hotel-attribute combina-
tions with similar consumer value perceptions. Incorporating hotel star ratings as a market positioning dimension,
multi-perspective data visualization is performed using two- and three-dimensional scatter plots. These visualizations
reveal the complex psychological interactions among consumer attention allocation, emotional perceptions, and brand
tiers. Finally, to enhance the practical signi ﬁcance of the analysis, within-cluster analysis identi ﬁes and highlights
representative “typical attribute points. ” These correspond to critical touchpoints in the consumer decision-making
journey, providing data-driven insights to support targeted marketing, service optimization, and strategic positioning
for star hotels with differentiated market positioning.
Figures 12 and 13 use hotel star ratings as the classi ﬁcation dimension to illustrate online review distribution
characteristics. The horizontal axis shows standardized weights, re ﬂecting the importance of attributes in consumers ’
decision-making. The vertical axis displays standardized sentiment scores, indicating consumers ’ experiential
Fig. 13 . 3D distribution of attribute weight, sentiment score, and star level.
Article in Press https://doi.org/10.1057/s41599-026-09225-1
Humanities and Social Sciences Communications

preferences for service indicators. In the three-dimensional graph, the Z-axis differentiates hotels by star grade,
enabling analysis of trends in psychological weights and experiential feedback across hotel tiers.
(i) Low-star hotels: Some data points show low weight and low sentiment, indicating a gap between the core
experience of low-star hotels and consumers ’ psychological expectations. For budget-conscious visitors, it is
important to assess whether valued attributes fall within this dual-low zone, as this suggests a likely
unsatisfactory experience. This highlights the compromise-based evaluation mechanism of price-sensitive
consumers in online review culture: low-star hotels are typically assigned low baseline expectations, and
consumers tolerate basic amenities. However, severe negative word-of-mouth spreads quickly when key
attributes (e.g., hygiene and safety) fall into the dual-low range. Hotel operators should identify de ﬁciencies in
this zone and address expectation gaps through targeted experience optimization to meet the core demands of
budget customers, preventing customer churn from breached psychological contracts.
(ii) High-star hotels: Data points cluster in the medium-to-high weight region with elevated sentiment scores,
indicating that high-star hotels have established strong reputations in core service attributes. Consumers seeking
premium experiences can prioritize hotels with this dual-high pro ﬁle. This conﬁrms the brand premium effect in
platform-based evaluations: patrons of high-star hotels purchase not only tangible services, but also emotional
value and symbolic social status. High sentiment scores on high-weight attributes (e.g., service quality and
ambient environment) reinforce brand reputation. These zones form the core of the brand ’s emotional premium.
Hotel operators should focus on distinctive experiences and customized scenarios to strengthen status
identiﬁcation among high-end clientele.
The optimal number of clusters is set at K = 3, determined by the Sum of Squared Errors (SSE) and silhouette
coefﬁcients. Clustering results are shown in Fig. 14. From a consumer perspective, hotels can be matched to cluster
characteristics: consumers seeking premium experiences on high-weight attributes should prioritize hotels in the high-
weight cluster with favorable sentiment scores, while those with speci ﬁc preferences should target clusters aligned
with their individual demands. This classi ﬁcation framework also enables hotels to focus on three core operational
scenarios and clarify priorities based on each cluster ’s distribution of attribute weights and sentiment scores:
Fig. 14 K-means clustering result distribution.
https://doi.org/10.1057/s41599-026-09225-1 Article in Press
Humanities and Social Sciences Communications

(i) Cluster 1 (Low Weight – High Sentiment, Basic Zone): These attributes do not form the core of decision-
making but generate signi ﬁcant spillover affective perceptions. This pattern re ﬂects the “delight effect ”
observed in online review behavior. When basic services exceed expectations, they reinforce overall user
experience and establish a foundation for brand trust. Hotels should maintain resilience in standardized services
and ensure that basic experiences support overall performance.
(ii) Cluster 2 (High Weight – High Sentiment, Advantage Zone): Value-creation points directly address pain points
and enable successful conversion. This cluster uncovers the “value resonance ” rule in platform-mediated
consumption. Superior user experience translates into positive word-of-mouth, shapes the decision-making of
potential customers, and drives a self-reinforcing reputation cycle. Hotels may transform these strengths into
social marketing labels. High-star hotels create an “experience ecosystem. ” Low-star hotels pursue a “low
investment, distinctive strength ” model.
(iii) Cluster 3 (Medium-Low Weight – Low Sentiment, Improvement Zone): Risk-averse consumers easily identify
and reject these shortcomings. This ﬁnding con ﬁrms the “negativity bias ” in consumer decision-making. In
online review behavior, exposure of core weaknesses holds veto power. A single negative comment about a
drawback often outweighs multiple positive reviews. Hotels should address critical complaint-triggering issues
and implement targeted risk-mitigation plans. Low-star hotels focus on essential service upgrades. High-star
hotels emphasize supplementary details such as empathy.
Figure 15 connects clustering results, hotel star ratings, and representative attributes, combining psychological
weights and sentiment distributions to reveal optimization directions for consumer perceptions at each star tier.
Fig. 15 Distribution of typical attributes by cluster and star level.
Article in Press https://doi.org/10.1057/s41599-026-09225-1
Humanities and Social Sciences Communications

(i) 2-star hotels (orange representative points): Representative points in Cluster 2 fall within the high-weight, high-
sentiment zone, where distinctive experiences —such as local small-scale cultural activities —can be developed.
This reﬂects the differentiation survival strategy of low-star hotels in the platform economy. By creating unique,
story-worthy experiences, hotels can generate narrative content in consumer reviews and escape intense price
competition. Dual-low basic attributes in Cluster 3 (including air conditioning and daily amenities) require
standardized upgrades to enhance perceived cost performance.
(ii) 3-star hotels (green representative points): Attributes like “cost performance ” and “family friendliness ” are
distinctively distributed in Cluster 1, supporting the launch of themed services such as parent-child packages.
This suggests that mid-tier hotel consumers prioritize the psychological trade-off of value for money, with
family-friendly attributes serving as key drivers for repeat purchases and referrals. Basic attributes in Cluster 3
perform poorly and require hardware upgrades and quality control improvements.
(iii) 4-5 Star Hotels (star-shaped and triangular representative points): Medium-to-high weight, high-sentiment
attributes in Cluster 2 —such as room size and room upgrades —are core strengths that support further
reﬁnement of customized services. This highlights the experience hierarchy among high-end hotel consumers,
whose demand shifts from functional satisfaction to symbolic consumption. Minor perks, such as room
upgrades, serve as status symbols. Cluster 3 attributes related to re ﬁned details (e.g., laundry service, late check-
out) require improvement and can bene ﬁt from process optimization.
Hotels employ cluster analysis and star-rating adaptation as core decision logic. By leveraging psychological
weights and affective preference trends, hotels implement a tiered strategy: enhance strengths in the Strength Zone,
maintain stability in the Basic Zone, and address de ﬁciencies in the Improvement Zone. This approach enables
precise demand matching across consumer segments. Consumers may consult cluster analysis and star-rating
adaptation results to prioritize hotels with Strength Zone attributes that match their preferences. The framework
converts platform review data from statistical ﬁgures into behavioral insights. It establishes a paradigm shift from
homogeneous recommendations to contextualized experience matching. This strategy offers actionable pathways for
value co-creation within review culture. It also supports hotels in service upgrading and resource optimization based
on consumer behavioral logic amid intense competition within the platform economy. These aspects represent the
core practical contributions of this study to hotel management. Insights from this study have signi ﬁcant societal and
platform implications. The cross-modal denoising and heterogeneous preference matching framework effectively
reduces information overload and decision anxiety for consumers in the digital era. This approach enables consumers
with bounded rationality to avoid cognitive traps and select accommodations that suit their authentic needs. From a
digital platform perspective, the study con ﬁrms the central role of visual evidence and multi-attribute interaction
models in reshaping social trust mechanisms. The ﬁndings suggest important implications for online travel agencies
(OTAs). These platforms should move beyond traditional traf ﬁc generation through low pricing and linear scoring.
Contextualized experience matching should become the new standard. This transition leads the hospitality industry
away from homogeneous price competition and toward a sustainable competitive ecosystem centered on service
innovation and value co-creation.
Conclusion and prospect
This paper integrates platform economics, hospitality management, and consumer behavior theories. To address
theoretical limitations in exploring attribute correlations and isolating sensory representation, the new method uses
advanced computational techniques to decode human behavior. It applies a cross-modal affective cognitive analysis
framework that fuses visual and textual data with an entropy-based con ﬁdence mechanism to investigate and mitigate
cognitive biases in consumers ’ cross-sensory expressions. An indicator construction framework coordinates data-
driven approaches and standard mapping. This framework extracts ﬁne-grained attributes through neural networks
and semantic clustering, producing a structured evaluation system. The research introduces 2-additive measures and
generalized Shapley values to quantify complex psychological synergistic or antagonistic effects in consumers ’ trade-
offs among accommodation attributes. The approach relaxes the attribute independence assumption in conventional
https://doi.org/10.1057/s41599-026-09225-1 Article in Press
Humanities and Social Sciences Communications

models. With the TF-IDF mechanism, it dynamically generates customized experience weights for customer groups
and delivers personalized recommendations that align with humans ’ bounded-rationality decision-making logic.
Case studies demonstrated that multimodal fusion corrected cognitive biases in consumers ’ textual expressions.
The “User Experience ” indicator, representing abstract subjective perceptions, achieved a positive correction of
1.473. The “Amenities” indicator, focused on tangible touchpoints, reached a negative calibration of −1.316.
Generalized Shapley values reshaped evaluation logic consistent with actual mental representations. High-order
psychological synergy combinations, such as {Accessibility, User Experience}, dominated decision-making with a
contribution rate of 35.92%. The proposed method outperforms conventional approaches with an NDCG@10 value
of 0.7356. These quantitative results verify algorithm effectiveness and systematically reveal inherent patterns in
platform-mediated consumption. The ﬁndings provide robust empirical evidence for understanding motives behind
online review behavior, recovering multisensory user experience, and deconstructing the mechanisms of consumer
decision-making. At the macro theoretical level, this paper contributes interdisciplinary insights to three advanced
research ﬁelds. First, in Consumer Behavior, the work empirically extended the boundary of bounded rationality
theory. It con ﬁrmed that cross-modal synergy across multiple senses (visual and textual) and psychological com-
pensation mechanisms among service attributes form the basis of consumer decision-making logic. Second, in
Hospitality Research, the new method relaxed the independent attribute assumption in traditional service quality
evaluations, such as SERVQUAL. It transformed static service fragments into an interactive “experience co-creation
network” and renewed the value assessment paradigm for service touchpoints. Third, in Digital Platform Studies, the
research unpacked the nonlinear mechanism of heterogeneous user-generated content in mitigating information
asymmetry, reducing transaction frictions, and reconstructing digital trust systems. The ﬁndings offer new theoretical
perspectives for platform governance and for the evolution of recommendation mechanisms in the digital economy.
Future research may be pursued along several key directions. First, on the technical front, in addition to enhancing
real-time data processing and incorporating audio, geospatial, and behavioral data, studies could explore the inte-
gration of large language models (LLMs) to construct explainable AI (XAI) agents for recommendation systems.
Such agents would translate numerical feedback derived from high order interactions into transparent natural lan-
guage explanations, thereby increasing consumer trust. Second, with respect to model evolution, deep learning –based
sentiment extraction can enhance recognition accuracy for multidimensional features, while time series analysis can
examine the dynamic evolution of consumer preferences and track shifts in psychological trade-offs across different
lifecycle stages and macroeconomic environments. Finally, neuromarketing can support theoretical cross-validation.
Biometric data, such as eye-tracker recordings and electroencephalography (EEG), may verify the synergistic effects
of visual and textual information in reducing cognitive biases based on physiological evidence. In addition, this paper
examines synergistic and antagonistic effects primarily through statistical correlations, such as the Pearson correlation
coefﬁcient. Future research should use direct causal evidence from behavioral experiments to validate the psycho-
logical mechanisms behind these statistical correlations. This approach encourages deeper integration of recom-
mendation systems, moving from algorithm-centric optimization toward cognitive science.
Acknowledgements This work was supported by the National Natural Science Foundation of China (No. 72371134), the
National Social Science Fund of China (No. 22BJY019), the Humanities and Social Science Fund of Ministry of Education of
China (No. 22YJ630061), the Natural Science Foundation of Hunan Province of China (No. 2024JJ5451).
Author contributions Conceptualization: Fanyong Meng; Funding acquisition: Fanyong Meng; Methodology: Fanyong Meng,
Qi Wang; Supervision: Fanyong Meng; Validation: Fanyong Meng; Visualization: Fanyong Meng, Qi Wang; Writing and
Editing: Fanyong Meng, Qi Wang. Formal analysis: Qi Wang; Investigation: Qi Wang; Writing —original draft: Qi Wang.
Funding This work was supported by the National Natural Science Foundation of China (No. 72371134), the National Social
Science Fund of China (No. 22BJY019), the Humanities and Social Science Fund of the Ministry of Education of China (No.
22YJ630061), and the Natural Science Foundation of Hunan Province of China (No. 2024JJ5451).
Data availability The code and datasets used in this study are provided as related ﬁles in the journal ’s submission system. All
supporting materials are available from the corresponding author upon reasonable request.
Competing interests The authors declare no competing interests.
Article in Press https://doi.org/10.1057/s41599-026-09225-1
Humanities and Social Sciences Communications

Ethics approval and consent to participate No human subject research was undertaken, so ethics approval is not required.
Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International
License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you
give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if
you modi ﬁed the licensed material. You do not have permission under this licence to share adapted material derived from this
article or parts of it. The images or other third party material in this article are included in the article's Creative Commons licence,
unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and
your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission
directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/.
References
Abdou AH, Shehata HS (2026) Digital synergy for hospitality sustainability: a moderated mediation model of IoT, data-driven
decision-making, AI, and hotel sustainable performance. Front Sustain 6: 1727952
Bi JW, Liu Y, Fan ZP, Zhang J (2019) Wisdom of crowds: Conducting importance –performance analysis (IPA) through online
reviews. Tour Manag 70:460 –478
Radford A, Kim JW, Hallacy C, Ramesh A, Goh G, Agarwal S, Sastry G, Askell A, Mishkin P, Clark J, Krueger G, Sutskever I
(2021) Learning transferable visual models from natural language supervision. In: The 38th International Conference on
Machine Learning. Proceedings of Machine Learning Research, Vol. 139, pp. 8748-8763
Cai HY, Liu YT, Jin WP, Li F, Chen X, Yang GY, Shen WY (2024) Construction of sensory evaluation system of purple sweet
potato rice steamed sponge cake based on fuzzy mathematics. Foods 13(21):3527
Chen T (2017) Ubiquitous hotel recommendation using a fuzzy-weighted-average and backpropagation-network approach. Int J
Intell Syst 32(4):316 –341
Chen P, Shi X (2022) Dynamic evaluation of China ’s ecological civilization construction based on target correlation degree and
coupling coordination degree. Environ Impact Assess Rev 93: 106734
Chen Y, Zhong Y, Yu S, Xiao Y, Chen S (2022) Exploring bidirectional performance of hotel attributes through online reviews
based on sentiment analysis and Kano-IPA model. Appl Sci 12:692
Choquet G (1954) Theory of capacities. Ann l ’Inst Fourier 5:131 –295
Darraz N, Karabila I, El-Ansari A, Alami N, El-Mallahi M (2025) Advancing recommendation systems with DeepMF and hybrid
sentiment analysis: deep learning and lexicon-based integration. Expert Syst Appl 279: 127432
Delbrouck JB, Tits N, Brousmiche M, Dupont S (2020) A transformer-based joint-encoding for emotion recognition and
sentiment analysis. In: The Second Grand-Challenge and Workshop on Multimodal Language. Second Grand-Challenge and
Workshop on Multimodal Language (Challenge-HML), pp. 1-7
Devlin J, Chang MW, Lee K, Toutanova K (2019) BERT: pre-training of deep bidirectional transformers for language
understanding. In: The 2019 Conference of the North American Chapter of the Association for Computational Linguistics:
Human Language Technologies, Vol. 1, pp. 4171 –4186
Filieri R, Alguezaui S, McLeay F (2015) Why do travelers trust TripAdvisor? Antecedents of trust towards consumer-generated
media and its in ﬂuence on recommendation adoption and word of mouth. Tour Manag 51:174 –185
Frey BJ, Dueck D (2007) Clustering by passing messages between data points. Science, 315:972 –976
Gal Y, Ghahramani Z (2016) Dropout as a Bayesian approximation: representing model uncertainty in deep learning. In: The
33rd International Conference on Machine Learning. Proceedings of Machine Learning Research, Vol 48, 1050-1059
Grabisch M (1996) The application of fuzzy integrals in multicriteria decision making. Eur J Oper Res, 89:445 –456
Grabisch M (1997) K-order additive discrete fuzzy measures and their representation. Fuzzy Sets Syst, 92:167 –189
Han W, Chen H, Poria S (2021) Improving multimodal fusion with hierarchical mutual information maximization for multi-
modal sentiment analysis. In: The 2021 Conference on Empirical Methods in Natural Language Processing, pp. 9180-9192
Hazarika D, Zimmermann R, Poria S (2020) MISA: modality-invariant and -speci ﬁc representations for multimodal sentiment
analysis. In: The 28th ACM International Conference on Multimedia, pp. 1122-1131
Hatt F, Casasso S, Krishnanathan K (2025) Improving acceptance rate for hotel partners ’ recommendations: generative AI
personalization, contextualization and explainability. OARS Workshop
Isnowfy (2013) SnowNLP: simpli ﬁed Chinese text processing. In: GitHub Open Source Software Repository. GitHub. Available
via GitHub. https://github.com/isnowfy/snownlp. Accessed 04 Feb 2026
Ji F, Cao Q, Li H, Fujita H, Liang C, Wu J (2023) An online reviews-driven large-scale group decision-making approach for
evaluating user satisfaction of sharing accommodation. Expert Syst Appl 213: 118875
Kampman O, Barezi EJ, Bertero D, Fung P (2018) Investigating audio, video, and text fusion methods for end-to-end automatic
personality prediction. In: The 56th Annual Meeting of the Association for Computational Linguistics, Vol. 2, pp. 606-611
Kandampully J, Zhang T, Jaakkola E (2018) Customer experience management in hospitality: A literature synthesis, new
understanding and research agenda. Int J Contemp Hosp Manag 30(1):21 –56
https://doi.org/10.1057/s41599-026-09225-1 Article in Press
Humanities and Social Sciences Communications

Law R, Lin KJ, Ye H, Fong DKC (2024) Arti ﬁcial intelligence research in hospitality: a state-of-the-art review and future
directions. Int J Contemp Hosp Manag 36:2049 –2068
Li Y, Zeng F, Zhang N, Chen Z, Zhou L, Huang M, Zhu T, Wang J (2023) Multitask learning using feature extraction network
for smart tourism applications. IEEE Internet Things J 10:18790 –18798
Li D (2024) An interactive teaching evaluation system for preschool education in universities based on a machine learning
algorithm. Comput Hum Behav, 157: 108211
Li Y, Li J (2024) Method development and empirical research in examining the construction of China ’s “Zero-waste Cities. Sci
Total Environ 906: 167345
Liu S, Chen Z, Li X (2019) Time-semantic-aware Poisson tensor factorization approach for scalable hotel recommendation. Inf
Sci 504:422 –434
Liu F, Liao H, Al-Barakati A (2023) Physician selection based on user-generated content considering interactive criteria and risk
preferences of patients. Omega 115: 102784
Mai S, Hu H, Xing S (2019) Divide, conquer and combine: hierarchical feature fusion network with local and global perspectives
for multimodal affective computing. In: The 57th Annual Meeting of the Association for Computational Linguistics, Vol. 2,
pp. 476-481
Ma Y, Xiang Z, Du Q, Fan W (2018) Effects of user ‑provided photos on hotel review helpfulness: An analytical approach with
deep learning. Int J Hosp Manag 71:120 –131
Majumder N, Hazarika D, Gelbukh A, Cambria E, Poria S (2018) Multimodal sentiment analysis using hierarchical fusion with
context modeling. Knowl-Based Syst, 161:124 –133
Manning C, Surdeanu M, Bauer J, Finkel J, Bethard S, McClosky D (2014) The Stanford CoreNLP natural language processing
toolkit. In: The 52nd Annual Meeting of the Association for Computational Linguistics: System Demonstrations, pp. 55 –60
Meng F, Chen X (2014) An approach to interval-valued hesitant fuzzy multi-attribute decision making with incomplete weight
information based on hybrid Shapley operators. Informatica 25:617 –642
Mansour M, Albawwat AH, Marei A, Abozeid HO (2026) Cybersecurity disclosure and digital maturity as strategic drivers of
banking performance: Evidence from Europe. Int J Inf Manag Data Insights 6: 100403
Mansour M, Saleh MWA, Jaradat Z, AL-Hawamleh A, Al Zobi MT, Marei A (2026) Digital economy development and ﬁrm-
level sustainability performance in Europe. Discov Sustain 7:322
Mansour M, Zobi MA, Alomair M (2026) Arti ﬁcial intelligence, ESG governance, and green innovation ef ﬁciency in emerging
economies. Economies 14:11
Nicolle J, Rapp V, Bailly K, Prevost L, Chetouani M (2012) Robust continuous prediction of human emotions using multiscale
dynamic cues. In: The 14th ACM International Conference on Multimodal Interaction, pp. 501 –508
Pang Q, Wang H, Xu Z (2016) Probabilistic linguistic term sets in multi-attribute group decision making. Inf Sci 369:128 –143
Pantic M, Rothkrantz LJ (2003) Toward an affect-sensitive multimodal human-computer interaction. Proc IEEE 91:1370 –1390
Pearson K (1894) Contributions to the mathematical theory of evolution. Philos Trans R Soc Lond A 185:71 –110
Poria S, Chaturvedi I, Cambria E, Hussain A (2016) Convolutional MLK-based multimodal emotion recognition and sentiment
analysis. In: The 16th IEEE International Conference on Data Mining, pp. 439-448
Poria S, Cambria, E, Hazarika, D, Majumder, N, Zadeh, A, Morency LP (2017) Context-dependent sentiment analysis in user-
generated videos. In: The 55th Annual Meeting of the Association for Computational Linguistics, Vol. 1, pp. 873-883
Pu Z, Xu Z, Zhang C, Zeng XJ, Gan W (2025) An online review-driven two-stage hotel recommendation model considering
customers’ risk attitudes and personalized preferences. Omega 131: 103197
Salton G, Buckley C (1988) Term-weighting approaches in automatic text retrieval. Inf Process Manag, 24:513 –523
Shannon CE (1948) A mathematical theory of communication. Bell Syst Tech J, 27:379 –423
Tang J, Li K, Jin X, Cichocki A, Zhao Q, Kong W (2021) CTFN: hierarchical learning for multimodal sentiment analysis using
coupled-translation fusion network. In: The 59th Annual Meeting of the Association for Computational Linguistics and the
11th International Joint Conference on Natural Language Processing, Vol. 1, pp. 5301-5311
Tsai Y-HH, Bai S, Liang PP, Kolter JZ, Morency L-P, Salakhutdinov R (2019) Multimodal transformer for unaligned multi-
modal language sequences. In: The 57th Annual Meeting of the Association for Computational Linguistics, pp. 6558-6569
Theodorakopoulos L, Theodoropoulou A (2026) Business intelligence and business process management in the era of generative
AI: a review of big data analytics, process mining, and decision support systems. Appl Sci 16(10):4603
Vaswani A, Shazeer N, Parmar N, Uszkoreit J, Jones L, Gomez AN, Kaiser Ł, Polosukhin I (2017) Attention is all you need. In:
The 31st Conference on Neural Information Processing Systems. Advances in Neural Information Processing Systems, Vol.
30, pp. 6000 –66010
Wang L, Wang XK, Peng JJ, Wang JQ (2020) The differences in hotel selection among various types of travellers: a comparative
analysis with a useful bounded rationality behavioural decision support model. Tour Manag, 76: 103961
Wang X, Lyu J, Kim BG, Parameshachari BD, Li K, Li Q (2024) Exploring multimodal multiscale features for sentiment
analysis using fuzzy-deep neural network learning. IEEE Trans Fuzzy Syst 33:28 –42
Xiao H, Lu Y, Huang F, Li S, Liao J (2024) Construction of the medical virtual teaching and research of ﬁce evaluation system in
China based on the context, input, process, product model: a Delphi study. BMC Med Educ 24: 1322
Yafei W (2019) Evaluation system construction of health policy based on system dynamics and complex network. Clust Comput
22:4589–4596
Article in Press https://doi.org/10.1057/s41599-026-09225-1
Humanities and Social Sciences Communications

Yang J, Chen W (2010) Research on the evaluation model of the modernization level of urban construction in Jiangsu Province,
China. Sci China Technol Sci 53:2510 –2514
Yin Y, Zhang N, Chen Z, Li M, Li Y, Gao H, He L (2022) Exploiting user preferences for multiscenarios in query-less search.
IEEE Trans Comput Soc Syst 9:1794 –1806
Yu W, Xu H, Yuan Z, Wu J (2021) Learning modality-speci ﬁc representations with self-supervised multi-task learning for
multimodal sentiment analysis. : 35th AAAI Conf Artif Intell 35(No. 12):10790 –10797
Zadeh A, Chen M, Poria S, Cambria E, Morency L-P (2017) Tensor fusion network for multimodal sentiment analysis. In: 2017
Conference on Empirical Methods in Natural Language Processing, pp. 1103 –1114
Zadeh A, Liang PP, Mazumder N, Poria S, Cambria E, Morency L-P (2018) Memory fusion network for multi-view sequential
learning. In: The 32nd AAAI Conference on Arti ﬁcial Intelligence, Vol. 32, No. 1, pp. 1404 –1410
Zhang C, Xu Z, Gou X, Chen S (2021) An online reviews-driven method for the prioritization of improvements in hotel services.
Tour Manag 87: 104382
Zhang Z, Yang K, Zhang JZ, Palmatier RW (2023) Uncovering synergy and dysergy in consumer reviews: a machine learning
approach. Manag Sci 69(4):2339 –2360
Zhao H, Yang M, Bai X, Liu H (2024) A survey on multimodal aspect-based sentiment analysis. IEEE Access 12:12039 –12052
Zhao E, Sun S, Fu C, Wu J, Wang S (2025) How user-generated content in ﬂuence different types of travelers to select hotels? A
perspective with prospect theory. Inf Process Manag 62:104049
Zhao X, Li X, Jiang R, Tang B (2025) Resolving multimodal ambiguity via knowledge-injection and ambiguity learning for
multimodal sentiment analysis. Inf Fusion 115: 102745
Zheng X, Luo Y, Sun L, Zhang J, Chen F (2018) A tourism destination recommender system using users ’ sentiment and
temporal dynamics. J Intell Inf Syst 51:557 –578
Zhu JJ, Chang YC, Ku CH, Li SY, Chen CJ (2021) Online critical review classi ﬁcation in response strategy and service provider
rating: algorithms from heuristic processing, sentiment analysis to deep learning. J Bus Res 129:860 –877
Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional
afﬁliations.
Authors and Af ﬁliations
Fanyong Meng 1 ● Qi Wang 1
1 Nanjing University of Information Science and Technology, Nanjing, China
https://doi.org/10.1057/s41599-026-09225-1 Article in Press
Humanities and Social Sciences Communications
