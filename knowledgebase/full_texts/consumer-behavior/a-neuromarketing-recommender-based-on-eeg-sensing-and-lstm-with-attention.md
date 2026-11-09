---
title: A neuromarketing recommender based on EEG sensing and LSTM with attention
url: https://doi.org/10.1038/s41598-026-69684-z
category: consumer-behavior
subcategory: framework
date: 2026-08
venue: Scientific Reports
authors:
- Xuan Yang
- Zhiqing Bai
- Dejuan Li
source: openalex-oa
pdf_url: https://www.nature.com/articles/s41598-026-69684-z_reference.pdf
pages: 29
chars: 75444
fetched_at: '2026-11-08T18:51:07+00:00'
kb_version: 1
---

# A neuromarketing recommender based on EEG sensing and LSTM with attention

ARTICLE IN PRESS
Article in Press
A neuromarketing recommender based on EEG
sensing and LSTM with attention
Scientific Reports
Received: 3 August 2024
Accepted: 28 August 2026
Cite this article as: Yang X., Bai Z.,
Li D. et al. A neuromarketing
recommender based on EEG sensing
and LSTM with attention. Sci Rep
(2026). https://doi.org/10.1038/
s41598-026-69684-z
Xuan Yang, Zhiqing Bai, Dejuan Li, M. Khosravi, Qinyong Wang, Feng Wang & Xubo Ye
We are providing an unedited version of this manuscript to give early access to its
findings. Before final publication, the manuscript will undergo further editing. Please
note there may be errors present which affect the content, and all legal disclaimers
apply.
If this paper is publishing under a Transparent Peer Review model then Peer
Review reports will publish with the final article.
https://doi.org/10.1038/s41598-026-69684-z
© The Author(s) 2026. Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International
License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit
to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do
not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this
article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the
article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain
permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/.

A neuromarketing recommender based on EEG sensing
and LSTM with attention
Xuan Yang
New Generation Information Technology Research Center, Weifang University of Science and Technology,
Weifang 262700, China
Email: yangxuan@wfust.edu.cn
Zhiqing Bai
School of Electronic Engineering and School of Intelligent Manufacturing, Anhui Xinhua University, Hefei
City 230088, China
Email: baizhiqing@axhu.edu.cn
Dejuan Li
New Generation Information Technology Research Center, Weifang University of Science and Technology,
Weifang 262700, China
Email: lidejuan2016@wfust.edu.cn
M. Khosravi*
Shiraz University of Medical Sciences, Shiraz, Iran
Email: dr_mkhosravi@sums.ac.ir, mohammadr.khosravi@iran.ir
Qinyong Wang
College of Artificial Intelligence, Zhejiang College of Security Technology, Wenzhou City 325000, China
Email: qinyong.wang@foxmail.com
Feng Wang
Hangzhou itutori Technology Co., Ltd., Hangzhou 311400, China
Email: jxhaohaizi@gmail.com
Xubo Ye
School of Information Engineering, Xinyang Agriculture and Forestry University, Xinyang 464000, China
Email: 2025270007@xyafu.edu.cn
* Corresponding Author
Abstract
Conventional EEG-based recommendation systems, such as those employing standard LSTM, bidirectional
LSTM, or attention-augmented LSTM, have demonstrated potential in decoding consumer preferences.
However, these models often fail to account for irregular temporal intervals between decision-making
events and tend to underutilize critical neural dynamics, leading to suboptimal performance in
neuromarketing applications where timing and cognitive state transitions are pivotal. To address these
limitations, we propose a distributed attention-aware long short-term memory (ataLSTM) framework
designed for EEG-driven recommendation systems. This approach explicitly models temporal irregularities
and leverages a distributed attention mechanism to prioritize EEG features most predictive of consumer
“like” or “dislike” responses. Evaluated on an open-access neuromarketing dataset of EEG recordings from
neurologically healthy adults (aged 18–38) using the 14-channel EMOTIV EPOC+ headset (configured
according to the 10–20 system), the framework analyzed brain activity during real-time assessments of 14
consumer product categories. Through a robust evaluation protocol employing stratified 10-fold cross-
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

validation with five repeated runs, ataLSTM achieved a classification accuracy of 92.42%, surpassing LSTM,
biLSTM, and attention-enhanced LSTM baselines by an average of 3.2% across categories. Optimal
performance was observed with the 10–20-window configuration and 30% overlap, highlighting the
model’s ability to capture nuanced neural variations. The distributed attention mechanism significantly
reduced false negatives and enhanced preference discrimination. By embedding cognitive-state modeling
into the recommendation pipeline, ataLSTM enables precise, real-time personalization of product
suggestions, thereby improving targeted advertising, cross-selling, and customer conversion rates. This
work establishes a new standard for brain–computer interface applications in consumer analytics, bridging
neuromarketing research and practical recommender systems.
Keywords: Recommendation system, EEG signals, Consumer purchasing, Attention-aware LSTM, Online
shopping.
1- Introduction
Neuromarketing is best understood as an interdisciplinary framework that integrates concepts from
psychology, economics, neuroscience, and business to assess the effectiveness of marketing strategies [1–
3]. Its ability to uncover subconscious motives, preferences, judgments, and attitudes of consumers without
relying solely on self-reported responses has attracted growing academic attention [4,5]. By bridging
neuroscience and marketing, neuromarketing offers novel methods for understanding consumer behavior,
particularly in evaluating advertising, product perception, and purchasing intent [6–8]. It draws on advanced
neuroscientific techniques to explore the emotional and cognitive reactions of consumers, providing deeper
insights than traditional marketing research can achieve [9,10].
The field encompasses both commercial and non-commercial applications, such as social marketing, brand
evaluation, and retail strategy development [11,12]. Unlike neuroeconomics—which primarily studies the
brain’s role in economic decisions—neuromarketing focuses directly on marketing stimuli and real-time
consumer reactions. This real-time perspective is particularly valuable because traditional marketing
techniques often rely on delayed, biased, and simplified survey-based feedback, which fails to reflect the
immediate psychological state of customers during product exposure or decision-making [13–15].
Neuromarketing utilizes physiological monitoring techniques such as electroencephalogram (EEG),
functional magnetic resonance imaging (fMRI), and complementary non-neural sensors such as eye-
tracking for gaze behavior. Steady-state topography (SST) is a neural signal analysis technique typically
derived from EEG data, not a measurement device, and therefore should be distinguished from modalities
such as EEG or fMRI. Among these modalities, EEG stands out for its affordability, portability, and real-
time signal acquisition, making it a highly practical tool for neuromarketing research [16]. Portable and
mobile EEG systems have also been used outside laboratory environments in field or semi-naturalistic
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

studies—enabled by lower upfront investment and real-time analysis capabilities—though such use remains
less frequent than in controlled laboratory settings [13]. Traditional marketing techniques, however, often
rely on delayed, biased, and simplified survey-based feedback, which inadequately captures consumers’
immediate psychological states during exposure or decision-making. EEG-based methods have been
applied to various marketing domains, including general marketing experiments [17], pre-launch feasibility
testing [18], packaging evaluation [19], and pricing strategy analysis [20].
In parallel, recommender systems have become increasingly prominent in e-commerce by guiding users
toward personalized choices without requiring prior in-depth knowledge of the products. These systems
leverage historical preferences, behavioral patterns, or contextual information to suggest relevant items
[21]. Some prior studies have explored EEG-based recommendation frameworks. For instance, Guo and
Elgendi [22] utilized EEG signals to rate virtual products before and after purchase, and Bandara et al. [23]
combined EEG features with machine learning models to predict user preferences in video commercials.
While valuable, these works primarily target single-product ratings or static evaluations and rarely model
the temporal dynamics of consumer behavior or incorporate real-time personalization strategies.
With the rise of deep learning in signal processing, neural networks such as Long Short-Term Memory
(LSTM) have proven effective in modeling temporal dependencies in EEG data [24]. LSTM networks are
particularly suited to sequential data and have mitigated key limitations of traditional RNNs, such as
vanishing gradients [25]. However, conventional LSTM models often fall short in scenarios where temporal
irregularity and interpretability are critical—such as in neuromarketing applications, where intuitive
understanding and timing of decisions matter. In such contexts, the ability to identify and prioritize specific
neural events that influence consumer decisions is as important as overall predictive accuracy.
Motivated by these gaps, and given the time-dependent nature of purchase behavior, we employed LSTM
networks, which are well-suited for capturing sequential patterns in EEG signals. Moreover, by integrating
attention mechanisms, we enhance the model’s ability to focus on key decision-making moments in the
customer journey, providing a more personalized and dynamic recommendation experience. This
combination enables both better predictive performance and more interpretable output, which is essential
for practical neuromarketing tools.
In this paper, we propose an EEG-assisted recommendation framework that incorporates an attention-based,
time-aware LSTM (ataLSTM) model to provide product suggestions based on real-time brain activity. Our
model addresses the limitations of prior studies by accounting for non-uniform time intervals between
purchases and incorporating attention to prioritize meaningful neural patterns. Using a publicly available
neuromarketing EEG dataset [44], we demonstrate the ability of our system to identify consumer
preferences across diverse product categories. Our contributions include the development of a temporally-
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

aware attention mechanism, robust EEG preprocessing and augmentation techniques, and comprehensive
evaluation using accuracy, sensitivity, and specificity metrics.
Fig. 1. A typical neuromarketing infrastructure is illustrated in this figure using EEG signals.
Fig. 1 illustrates the conventional neuromarketing infrastructure based on EEG signals. The following are
our contributions to this research:
1. As part of our EEG-based analysis, we introduce a recommendation system designed to provide
accurate, data-driven predictions for marketing applications. The proposed attention-based time-
aware LSTM (ataLSTM) model captures both the user's cognitive attention and temporal
irregularities in purchasing behavior. Unlike standard models, our approach enhances LSTM
memory by incorporating richer contextual information from multiple past events rather than
relying solely on the immediate past.
2. While conventional LSTM models are effective in handling sequential data, they face significant
challenges in consumer-oriented domains. Specifically, standard LSTMs often fail to interpret
irregular event timing and lack transparency in their predictions. These limitations are especially
problematic in neuromarketing, where models must not only be accurate but also interpretable. To
address these challenges, we implemented signal windowing techniques and applied multiple signal
transformers to expand the training dataset and compensate for the limited amount of available
EEG signals.
3. Our neuro-recommendation approach groups items that elicit similar neural responses, enabling the
system to make personalized recommendations that reflect each user's cognitive and emotional
patterns. By analyzing EEG data in combination with the customer’s purchase history, the model
provides more precise and context-aware suggestions. This framework can be broadly applied
across various product and service categories, supporting more targeted and effective marketing
strategies.
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

In this study, we introduce an attention-based time-aware LSTM (ataLSTM) framework designed to predict
consumer preferences based on EEG signals. The model captures both short- and long-term neural
dynamics and accounts for irregular elapsed-time gaps between sequential decision-making events by
integrating temporal memory with stimulus weighting. Our method fills the gap left by prior work that
primarily focused on single-product suggestions or static EEG snapshots. By leveraging an attention
mechanism, the proposed approach dynamically prioritizes impactful stimuli and improves
recommendation accuracy in real-world neuromarketing scenarios. The remainder of this paper is organized
as follows: Section 2 reviews related work; Section 3 presents the experimental results of the proposed
framework; Section 4 discusses the findings; and Section 5 concludes the study.
2- Related work
2.1 Neuromarketing and EEG
Neuromarketing uses scientific methods to study purchasing behavior. It examines the cognitive
mechanisms involved in preference and purchasing intention processing in the brain. In large consumer
markets, even small improvements in decision modeling can create significant value. Traditional marketing
relies on delayed feedback—questionnaires, product assessments, and reviews—that often fail to capture
the real-time cognitive and emotional reactions of consumers. Therefore, these approaches fall short in
explaining instantaneous decision-making. To address this limitation, researchers have explored
physiological measures to track consumer responses. Among them, EEG has gained popularity due to its
portability, affordability, and capability to reflect immediate neural states [16,26]. EEG-based studies in
neuromarketing have used various signals—including brainwaves and spectral power shifts—to detect
consumer preference, attention, and engagement [17–20,27,28]. Additional studies have leveraged EEG to
evaluate consumer perception of commercials, pricing, and packaging [29,30].
Other physiological tools like fMRI, fNIRS, and eye-tracking have also been utilized [31,32], but EEG
remains dominant in non-laboratory and mobile settings due to its practicality. Researchers have
demonstrated that EEG responses change significantly depending on preference, especially in frontal and
parietal brain regions [33,34]. The integration of EEG with other modalities like facial expressions and eye
movement has further increased prediction accuracy [30].
2.2 EEG-Based Recommendation
Despite advancements in neuromarketing, the use of EEG in personalized recommendation remains
underexplored. Guo and Elgendi [22] proposed a 3D e-commerce recommender that used EEG signals
captured before and after product interaction to compute user preferences. Similarly, Bandara et al. [23]
presented an EEG-based movie recommendation model that used a Random Forest classifier to classify
emotional reactions with high accuracy. Chang et al. [35] used EEG data in music recommendation by
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

correlating neural signals with musical features, and Shaw and Patra [36] leveraged EEG to recommend
educational videos based on student attention.
These systems show the feasibility of EEG-enhanced recommendation models. However, most are limited
to single domains and lack generalizability. They often rely on single-instance EEG readings and ignore
temporal variations, user history, and sequential behavior. Furthermore, some EEG recommender models
are limited to small product sets or single-item predictions, such as recommending only shirts [25], and do
not account for multi-item or basket-based decision dynamics.
Aldayel et al. [37] employed a deep learning model to classify consumer preferences using EEG signals
from the DEAP dataset, with a focus on power spectral density and valence features. Their approach aimed
to bridge the gap between traditional marketing methods, which rely on explicit responses, and
neuromarketing techniques that capture implicit neural signals. The deep learning model outperformed
Support Vector Machine (SVM) and k-nearest neighbors (KNN) in terms of accuracy, recall, and precision,
while Random Forest achieved comparable results. Although effective in capturing subconscious reactions,
the deep learning model showed only marginal improvement over ensemble methods.
Al-Nafjan [38] explored the impact of feature selection on EEG-based consumer preference detection in
neuromarketing. Utilizing PCA, mRMR, RFE, and ReliefF alongside five classifiers, the study
demonstrated that dimensionality reduction significantly improved classification performance across all
models. The findings underscore the importance of feature selection in enhancing EEG signal analysis.
However, the study lacked detailed insights into classifier-specific behavior and did not address
generalization beyond binary preference classification.
Pagan et al. [39] conducted an EEG-based wine-tasting experiment to evaluate how country-of-origin
labeling influences consumer preferences, with consideration of gender and involvement level. While
overall preferences remained unchanged, Brazilian wine elicited stronger cognitive processing in male and
low-involvement participants. The study offers a novel integration of neuromarketing with demographic
psychology, though its small and homogeneous sample limits the generalizability of the findings.
Kaya et al. [40] introduced a fuzzy linguistic summarization approach to analyze EEG responses to a hotel’s
audio, video, and web advertisements. Using a modified emotional model and multigranular trend analysis,
the system generated interpretable summaries segmented by demographic variables. This method enhances
expert decision-making in neuromarketing, though it depends heavily on subjective parameter tuning and
expert interpretation.
Cenizo et al. [41] conducted a systematic literature review on neuromarketing applications in web-based
environments, identifying key gaps in emotional-cognitive integration, cultural adaptation, and
accessibility. Using the SPAR-4-SLR protocol and TCCM framework, the study highlighted the promise
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

of tools such as EEG and eye-tracking for enhancing user experience. Despite offering valuable research
directions, the absence of empirical validation limited its practical impact.
Panda et al. [42] proposed a robust EEG-based neuromarketing framework that integrates deep transfer
learning with a Convolutional Block Attention Module (CBAM) to classify consumer preferences in e-
commerce settings. By refining connectivity features through spatial attention mechanisms, the model
achieved a classification accuracy of 95.60%, surpassing previous benchmarks by 2.6%. While the
framework demonstrated high accuracy, its computational complexity may hinder real-time or large-scale
deployment.
Song et al. [43] presented a comprehensive literature review on the role of neuromarketing in consumer
behavior research, covering technologies such as EEG, fMRI, MEG, PET, and eye-tracking. The review
emphasized how these tools enhance the understanding of emotional and cognitive responses to marketing
stimuli. Although it highlighted the importance of ethical considerations in the field, the study did not
propose empirical models or comparative analyses.
Previous EEG-based recommendation methods often rely on static data and lack modeling of temporal
dynamics or multi-item purchasing behavior. While deep learning approaches like Aldayel et al. [37] and
Panda et al. [42] improved accuracy, they remain computationally heavy and offer limited real-time
interpretability. In contrast, our attention-based time-aware LSTM (ataLSTM) captures both temporal
patterns and basket-level preferences, providing a more accurate and practical framework for
neuromarketing applications.
3- Proposed method
In this study, we propose an attention-based time-aware LSTM (ataLSTM) framework for predicting
consumer preferences based on EEG signals recorded during real-time exposure to marketing stimuli. The
model captures both short- and long-term neural dynamics and accounts for irregular elapsed-time gaps
between sequential decision-making events by integrating temporal memory with stimulus weighting.
Unlike traditional models that rely on static EEG snapshots or session-level analysis, our approach
dynamically tracks evolving neural responses, allowing for more personalized and context-aware product
recommendations.
The incorporation of an attention mechanism enables the model to highlight cognitively significant patterns
in EEG activity, improving both classification accuracy and interpretability. Furthermore, the proposed
system supports basket-level recommendations rather than single-item suggestions, providing a more
comprehensive view of consumer decision-making. By transforming raw EEG data into actionable
marketing insights, this framework bridges the gap between neural signal processing and practical
applications in neuromarketing. Fig. 2 illustrates the proposed neuro-recommendation system design.
Provided below is a comprehensive depiction of each component of the intended framework.
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

3-1 EEG dataset
The EEG signals analyzed in this study were obtained from the publicly available neuromarketing dataset
described in Ref. [44]. According to the original dataset report, the EEG recordings were collected from
adult participants aged between 18 and 38 years. No new participants were recruited, and no new EEG data
were collected in the present study.
The original study reported that the participants had no diagnosed mental or neurological disorders and
were asymptomatic at the time of data collection. None of the female participants was reported to be
pregnant. These participant-related characteristics and eligibility criteria refer to the original data-collection
study reported in Ref. [44].
The EEG recordings were originally acquired using an Emotiv EPOC+ wireless headset (Emotiv Inc., San
Francisco, CA, USA) at a sampling rate of 128 Hz. Fourteen EEG electrodes were positioned according to
the international 10–20 system at AF3, F7, F3, FC5, T7, P7, O1, O2, P8, T8, FC6, F4, F8, and AF4. The
Common Mode Sense (CMS) and Driven Right Leg (DRL) electrodes were used as reference electrodes.
The EEG signals were recorded in real time using the Emotiv Xavier Control Panel, version 3.1.29.
The experimental stimuli in the original dataset included several categories of consumer products, such as
belts, ties, shoes, and shirts. In the present study, the publicly available EEG data were processed offline
using MATLAB R2022b on a Windows 10 operating system. The MATLAB source code used for EEG
data processing, construction of the attention-aware LSTM network, and model analysis is publicly
available at https://github.com/Khosravi4GH/eeg-attention-lstm-neuromarketing.
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

Fig. 2. An illustration of our proposed neuro-recommendation system can be seen in this figure.
Every product consists of three distinct versions. EEG data were recorded throughout each 4-second
display. A total of 42 product-image presentations were included, corresponding to 168 seconds of
cumulative stimulus-exposure time. Importantly, the fixed 4-second duration refers only to the presentation
period of each individual product image and should not be interpreted as a fixed interval between
consecutive decision-making events. The elapsed time between successive events was retained separately
and used as the temporal-interval input (Δt) to the proposed ataLSTM model. Fig. 3 displays a
comprehensive array of product variants. Throughout this inquiry, participants conducted online shopping
activities while wearing EEG sensors attached to their craniums. While the individual browsed an online
store, EEG signals were recorded as well. After showing an image of a product to a subject, researchers
documented their reaction to the product, in particular whether they liked or disliked it. The data points
exhibit a uniform distribution across the two output categories (like and hate) with an equal 5:5 split. Before
starting data collection, participants were given instructions on how to assess things based on their own
preferences (e.g., liking or disliking).
Items Type 1 Type 2 Type 3 Items Type 1 Type 2 Type 3
Pen Shirts
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

Wrist
watch
Shoes
Sun
glasses
Bag
Sweater Muffler
Socks Belt
Wall
clock
Gloves
Bracelet Ties
Fig. 3. Among the 14 commodities, there are three different kinds (types 1, 2, and 3), each with its own colors and
designs [44].
It is important to note that the raw EEG data has undergone pre-processing procedures to enhance signal
quality and increase the accuracy of categorization outcomes. A band-pass filter ranging from 1 to 40 Hz
was utilized to remove high-frequency disturbances from unprocessed EEG data. Subsequently, the EEG
data was subjected to independent component analysis to remove any anomalies, such as ocular and cardiac
artifacts.
While the sample size limits broad statistical generalization, the study was designed as a proof-of-concept
to evaluate the effectiveness of the proposed ataLSTM-based neuro-recommendation framework. The
consistency of the signal preprocessing, stimulus presentation, and binary labeling protocol (like/dislike)
ensures that each participant contributes a well-structured dataset suitable for model training and validation.
To further address the challenges posed by the limited participant pool, we incorporated techniques that
enhance the richness and variability of the collected data without compromising reliability.
One such technique was the application of a signal windowing strategy, which effectively manages the non-
stationary nature of EEG signals. Each continuous EEG recording was segmented into overlapping time
windows, allowing the model to capture fine-grained temporal dynamics and localized neural activity
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

patterns. This not only increased the total number of training instances but also improved the model’s
sensitivity to transient cognitive states, leading to better generalization across products and user behaviors.
In addition to windowing, we employed multiple data augmentation strategies to further enrich the dataset.
These included the introduction of controlled Gaussian noise, as well as the use of signal transformation
methods such as wavelet transforms, autoregressive modeling, and Hilbert transforms. These techniques
help extract relevant temporal and frequency-domain features, contributing to the diversity of the training
data. A filtering mechanism was also applied to ensure only high-quality augmented samples were retained.
While some computationally intensive augmentation methods yielded only marginal accuracy
improvements, they still contributed meaningfully to the model's robustness and performance.
Notably, each stimulus (product image) was presented for 4 seconds, during which EEG signals were
continuously recorded. This 4-second duration defines the EEG segment associated with an individual
stimulus and is distinct from the elapsed interval between successive decision-making events. The latter
was allowed to vary across the sequence and was explicitly represented by Δt in the time-aware component
of ataLSTM. Our analysis used the 4-second EEG segments as the basis for signal windowing and
classification, while the corresponding event-to-event temporal intervals were used for time-aware memory
weighting.
3-2 Attention-based Time-Aware LSTM
In a conventional LSTM unit, the cell state c t serves as the internal memory, regulating the flow of
information through the network. As expressed in equation (1), the state c t-1 is derived from the operation
of the forget gate 𝑓𝑡 on the preceding cell state. Furthermore, the input gate iti_tit interacts with the
candidate cell state to update the memory content [45]:
𝑖𝑡 = sigmoid(𝑊𝑖 𝑥•𝑥𝑡 + 𝑊𝑖 ℎ•ℎ𝑡―1)
𝑐𝑡 = tanh( 𝑊𝑐 𝑥•𝑥𝑡 + 𝑊𝑐 ℎ•ℎ𝑡―1)
𝑓𝑡 = sigmoid(𝑊𝑓 𝑥•𝑥𝑡 + 𝑊𝑓 ℎ•ℎ𝑡―1) (1)
The variables are defined as follows: HHH denotes the total number of hidden nodes, while ℎ𝑡―1 refers to
the initial hidden state derived from 𝑐𝑡―1. The terms {𝑊𝑥 ∈  ℝ𝐻×𝐷, 𝑊ℎ ∈  ℝ𝐻×𝐻 } correspond to the first
set of network parameters. Here, D represents the number of features or measurements recorded for each
event, and H indicates the count of hidden nodes. Methods for achieving a modified cell state include:
𝑐𝑡 = 𝑖𝑡 ⊗ 𝑐𝑡 + 𝑓𝑡 ⊗ 𝑐𝑡―1 (2)
Here, ⨂ represents the aggregation of the constituent elements. The hidden state is then generated by
passing the updated cell state through an output gate layer, denoted as 𝑜𝑡. Furthermore, a sigmoid function
parameterized by U is applied to estimate the probability of consumer preference at time t:
 𝑜𝑡 = sigmoid 𝑊𝑜 𝑥•𝑥𝑡 + 𝑊𝑜 ℎ•ℎ𝑡―1
ℎ𝑡 = 𝑜𝑡 ⊗ tanh( 𝑐𝑡)
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

𝑝𝑡 = sigmoid(𝑈•ℎ𝑡) (3)
The proposed framework, seen in Fig. 4, is an Attention-based Time-Aware Long Short-Term Memory
network (ataLSTM).
Fig. 4. This is a depiction of the ataLSTM model that was proposed. Moreover, ataLSTM integrates cell states from
prior instances and stabilizes older memories by including weights derived from the time intervals (∆) and attention
mechanism (α).
Algorithm 1. In this algorithm, pseudo-code of ataLSTM method is displayed.
Algorithm 1: Classification procedure using Attention-based Time-Aware LSTM
Initialize: 𝑥 = [𝑥1, 𝑥2, ..., 𝑥𝑛]
Input: 𝑊, 𝑈, 𝑖, 𝑐, 𝑜, ℎ, 𝑝
1 for 𝑡 = 1 to K do
2 Enter the x inputs to the LSTM structures, respectively.
3 Create the new branches between inputs to the attention and time-aware
4 Calculate the outputs in Eqs. 1, 2, and 3.
5 Calculate ℎ𝑡 after each LSTM structure
6 Concatenate the outputs of attention and time-aware modules to 𝐶3
7 Concatenate the outputs of 𝐶3 and each LSTM to output part
8 Calculate the output of ℎ4 and update cell state
9 Calculate the output of 𝑦5
4 end for
5 Achieve the output classifier based on the Eq. 4.
Output: ℎ and 𝑦
As stated in (2), the first LSTM utilizes the cell state, 𝑐𝑡, to represent the current event. This is learned from
the state representing the prior event, 𝑐𝑡―1. In Algorithm 1, pseudo-code of ataLSTM method is displayed.
The well-known vanishing of gradient (VoG) issue [46] makes recent events critical for cell state learning.
Neuromarketing reduces the time constraints on relationships between customers and products on the
market. A drawback of a single memory read is its failure to consider previous occurrences. However, in
reality, experts usually analyze user data to identify significant previous purchases.
3-2-1 Memory mechanism
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

This study investigates the attention mechanism's cognitive ability to retrieve diverse memories. It aims to
establish correlations between events in online consumers' trajectories. This technique is expected to
enhance forecast accuracy and enable rapid decision-making. Conventional LSTM operates on the implicit
premise that the intervals between sequence events, also known as time steps, follow a normal distribution.
Nevertheless, the frequency of data collection from consumers might significantly differ based on many
parameters. The duration between two occurrences during a user's visit might vary from a few seconds to
several weeks. Hence, it is crucial to consider temporal progression when generating prognostics for
advantaging consumer expenditure. Furthermore, in some future situations, these occasional time intervals
might serve as an indication of users' visiting status. When a user is in a less advantageous circumstance,
such as being less likely to document items than when they are in a favorable one.
The intervals are fed into a function that decreases in a consistent manner to include the passage of time in
the standard ataLSTM model. Typically, a discounting factor known as "decay" is used to adjust the
collected memories from previous purchases of each event. The time between those events and the current
purchase is utilized to compute this decay factor. Hence, if the previous buy occurred a significant duration
ago, the trust placed on that period would not actively contribute to predicting the current one.
Fig. 4 illustrates that the proposed ataLSTM gathers information from several previous cell states instead
of relying on a single one. It is our goal to normalize these long-dismissed memories. This method involves
weights obtained from the attention mechanism and time intervals.
𝐶𝑡―1 = ∑𝑡―1 𝑖=𝑡―𝑚 𝛼𝑡𝑖•𝑐𝑖•𝑔(𝛥𝑡𝑡𝑖) (4)
𝛼𝑡𝑖 is the relative importance of the 𝑖𝑡ℎ event relative to the current event at time 𝑡. The time difference,
denoted by 𝛥𝑡𝑡𝑖, between the i-th and present events. In the present study, Δ𝑡,𝑖 denotes the actual elapsed
time between the occurrence of a previous decision-making event 𝑖 and the current event 𝑡, rather than the
fixed 4-second duration of the corresponding EEG stimulus segment. Consequently, although each product
image was displayed for the same 4-second period, the temporal distances used by the ataLSTM memory
mechanism could vary across successive events. It may be said that g(.) is a decay function. The number of
historical occurrences, denoted by m, will be taken into account. The new cell state is then generated by
replacing 𝑐𝑡―1 with 𝐶𝑡―1 in (2).
3-2-2 Attention module
Three approaches are examined to establish the value of m parameter.
a) Local Attention: During event processing, Local Attention exclusively considers the preceding m
events. To determine the ideal value of the hyperparameter 𝑚, one can do either grid search or seek advice
from an expert.
𝑒𝑡𝑖 = (𝑥𝑖)𝑇•𝑊𝛼•𝑥𝑡          𝑖 = (𝑡 ― 𝑚), (𝑡 ― 𝑚 +1), ...,(𝑡 ― 1) (5)
where,
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

𝛼𝑡 = softmax(𝑒𝑡(𝑡―𝑚), 𝑒𝑡(𝑡―𝑚+1), ..., 𝑒𝑡(𝑡―1)) (6)
b) Global Attention: Global Attention generates attention weights 𝛼𝑡𝑖 for the current time step t,
considering all previous events, as shown by m = t-1 in (4).
𝑒𝑡𝑖 = (𝑥𝑖)𝑇•𝑊𝛼•𝑥𝑡        𝑖 = 1, 2, ..., (𝑡 ― 1) (7)
where,
𝛼𝑡 = softmax(𝑒𝑡1, 𝑒𝑡2, ..., 𝑒𝑡(𝑡―1)) (8)
Global attention offers the advantage of considering all past instances, but it incurs a significant computing
burden and exhibits unevenly distributed attention weights. Additionally, we explore two alternative
approaches to address these concerns.
c) Flexible Attention: The optimal number of past experiences, denoted as 𝑚, that should be stored for
each specific occurrence 𝑡, is acquired through attention in a flexible manner. The concept is that the number
of previous events to be considered depends on the current event.
𝑚(𝑡) = (𝑡 ― 1)•Sigmoid(𝑣𝑇 𝑚•tanh(𝑊𝑚•𝑥𝑡)) (9)
where,
𝛼𝑡 = softmax(𝑒𝑡(𝑡―𝑚(𝑡)), 𝑒𝑡(𝑡―𝑚(𝑡)+1), ...,𝑒𝑡(𝑡―1)) (10)
where, 𝑊𝑚 and 𝑣𝑚 are learnable parameters, 𝑚(𝑡) is belong to [1, t-1].
3-2-3 Time-aware Function
The duration of market and online shopping sessions might vary from a few minutes to many hours. In
order to produce predictions that take into account time passage, we include intervals in our model and
utilize LSTM. Multiple previous studies have confirmed and supported the reliability of (11) as a reliable
principle for prolonged applications in the market and e-commerce sector.
𝑔(𝛥𝑡) =  log(𝑒 +  𝛥𝑡)―1 (11)
As a result, ataLSTM makes use of temporal dynamics by retrieving the most significant moments in the
past by adapting its memory. Weights for both time intervals and attention mechanisms are adjusted
simultaneously. When analyzing case histories, ataLSTM uses reasoning similar to that used by experts to
determine the marginal item. Each scenario highlights the most representative examples from the history
of shopping by users, highlighting current events. As a result, ataLSTM outperforms conventional LSTMs
in terms of predictive accuracy.
4- Results
This section presents the experimental findings of the proposed EEG-based recommendation framework.
We first describe the computational environment, evaluation metrics, and validation procedures used in the
analysis. The subsequent subsections report the model’s classification performance, comparative
assessment against baseline deep learning approaches, cross-validation outcomes under different signal
windowing configurations, and error analysis based on RMSE.
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

4-1 Experimental Setup and Metrics
The proposed ataLSTM recommendation framework was implemented and executed on a workstation
running Windows 10 with MATLAB R2022b. The hardware configuration included an Intel® Core™ i5-
8500 CPU, 16 GB of RAM, and a solid-state drive (SSD) to ensure fast data access and efficient model
training. The ataLSTM architecture combines temporal modeling through LSTM layers with an attention
mechanism that assigns higher weights to decision-relevant EEG segments.
Model hyperparameters were tuned through a grid search across plausible ranges, with validation accuracy
as the selection criterion. The optimal configuration employed 128 LSTM units, an attention layer
dimension of 64, a batch size of 32, a learning rate of 0.001 using the Adam optimizer, a dropout rate of
0.3 to mitigate overfitting, ReLU activation for dense layers, sigmoid activation for the output layer, and
binary cross-entropy loss. Hyperparameter tuning was carried out using 10% of the training data as a hold-
out validation set during cross-validation.
The dataset was randomly partitioned into training (70%), validation (10%), and testing (20%) subsets,
ensuring that samples from the same participant were not split across different sets to prevent data leakage.
To enhance robustness and reduce bias from random splits, a 10-fold cross-validation procedure was
applied, whereby the training, validation, and testing processes were repeated across ten folds, and the final
performance metrics represent the average results from all folds. Model performance was evaluated using
classification metrics derived from the confusion matrix, including true positives (correctly predicted “like”
responses), true negatives (correctly predicted “dislike” responses), false positives (cases incorrectly
predicted as “like”), and false negatives (cases incorrectly predicted as “dislike”). From these values,
accuracy, sensitivity (recall), and specificity were calculated to provide a balanced assessment across both
preference categories. Additionally, root mean square error (RMSE) was computed for comparative error
analysis against baseline models.
4-2 Assessment of Model Performance
Table 1 compares the classification accuracy of four deep learning approaches—baseline LSTM,
bidirectional LSTM (biLSTM), LSTM with an attention mechanism, and the proposed attention-based
time-aware LSTM (ataLSTM)—across 14 distinct product categories in the EEG-driven recommendation
task. The dataset comprises preference samples labeled as “like” or “dislike” and further organized by Type
values (1–3), which correspond to different experimental repetitions or folds within the cross-validation
procedure. Each cell in the table reports the percentage classification accuracy for a given model, type, and
product class, enabling a fine-grained comparison of model behavior across object categories.
Table 1. Classification accuracy of different deep learning models across 14 product categories,
highlighting the superior performance of the proposed ataLSTM approach. The bold values indicate the
highest reported accuracy for each item category
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

Method Type Pen Wrist watch Sun glasses Sweater Socks Wall clock Bracelet Shirts Shoes Bag Muffler Belt Gloves Ties
1 89.2 89.3 89.2 88.1 87.9 89.1 88.6 88.9 88.7 87.2 87.3 88.5 89.7 89.3
2 88.2 90.0 89.0 88.3 87.6 89.6 87.2 88.7 88.9 88.2 87.3 88.4 89.7 90.1LSTM
3 89.6 90.1 88.6 88.6 87.6 88.3 88.5 88.6 89.6 89.2 86.6 89.4 90.1 89.6
1 89.6 90.3 89.5 89.2 88.6 90.2 89.5 89.5 89.6 88.6 88.2 89.2 90.1 90.5
2 88.6 90.6 89.6 89.1 89.2 89.8 88.6 89.3 89.6 89.1 89.1 89.8 90.0 90.4biLSTM
3 90.5 90.2 89.3 90.2 88.6 89.6 89.2 89.6 90.4 90.2 87.5 90.2 90.6 90.1
1 90.7 92.5 91.1 90.3 89.4 92.2 90.1 90.1 90.6 90.0 89.3 91.3 92.2 91.5
2 90.1 91.8 91.3 89.6 90.0 91.6 90.2 89.3 91.1 89.6 89.6 90.2 90.1 92.1LSTM+ Attention 3 91.0 92.8 90.2 90.6 89.0 92.8 90.2 90.2 91.3 91.3 88.6 91.5 92.5 92.3
1 92.6 93.4 92.0 91.2 90.3 93.4 91.6 91.6 91.9 90.8 90.2 92.3 93.1 93.4
2 92.9 93.1 92.1 90.8 91.1 92.9 91.8 91.8 92.1 90.9 90.9 91.8 93.6 93.6ataLSTM
3 91.5 93.1 91.8 91.6 90.3 93.1 91.8 91.8 92.3 92.1 89.8 92.8 93.1 93.2
Across all product types and experimental repetitions, ataLSTM consistently outperforms the baseline
architectures, with classification accuracies frequently exceeding 93% for items such as wristwatches, belts,
and ties. In contrast, standard LSTM models show lower performance, particularly in categories like socks
and wall clocks, where accuracies occasionally fall below 88%. The inclusion of bidirectionality in biLSTM
provides moderate gains over the basic LSTM, but its improvements are less pronounced than those
achieved by integrating attention. The LSTM+Attention configuration yields substantial boosts—often 1–
2 percentage points—highlighting the benefit of weighting temporally salient EEG segments during
classification. However, the further incorporation of time-aware modeling in ataLSTM produces the most
consistent and robust improvements across all product classes and types. Moreover, the proposed ataLSTM
model achieved a peak classification accuracy of 92.42%, representing an average improvement of 3.2%
over the LSTM, biLSTM, and LSTM+Attention baselines across all product categories.
Moreover, a closer examination of the table reveals that the proposed ataLSTM model consistently achieves
the highest classification accuracy across most item classes, including wrist watch, belt, ties, and wall clock,
while also demonstrating strong performance in more challenging categories such as socks and muffler.
This superiority can be attributed to two key factors: first, the model’s ability to account for irregular
elapsed-time gaps between sequential decision-making events, enabling it to capture user decision-making
patterns in a more realistic and dynamic context; and second, the integration of an attention mechanism,
which assigns greater weight to temporal segments and EEG channels most relevant to the user’s
preferences. This combination not only mitigates accuracy degradation in classes with weaker or noisier
signal patterns but also enhances sensitivity in classes with more distinctive neural responses. As a result,
the ataLSTM outperforms standard LSTM, biLSTM, and LSTM+Attention methods with consistently high
accuracy across all item categories.
Notably, the performance gains of ataLSTM are not confined to a few select items but are observed across
nearly the entire product spectrum, suggesting that its combination of temporal irregularity handling and
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

attention enhances generalization in diverse neuromarketing contexts. The consistency of high accuracies
across Type 1–3 trials also indicate the model’s stability under repeated evaluation.
The application of windowing and overlap in EEG signal processing is critical for balancing temporal
resolution and feature stability. In this study, signals were segmented into varying window counts (from 1–
10, 10–20, and 20–30 windows) with a fixed 30% overlap. This overlap ensures that transient neural
patterns occurring at window boundaries are not lost, while multiple segmentation levels enable the model
to capture both coarse and fine temporal structures in consumer responses. The choice of 30% overlap
reflects a trade-off between increasing the effective number of training samples and minimizing
redundancy, which is particularly important in relatively small datasets such as the one used here.
Table 2 reports ataLSTM performance across 10-fold cross-validation repetitions, demonstrating
consistently high accuracies across all window configurations. The maximum accuracies are generally
achieved in the 10–20 window range, with values reaching up to 0.938 in some folds, indicating that this
segmentation scale offers the best balance between capturing detailed temporal features and maintaining
signal stability. Average accuracies remain tightly clustered around 0.925–0.928, with small standard
deviations (0.012–0.019), underscoring the robustness of the model. Minimum accuracies rarely fall below
0.910, suggesting that the method generalizes well across folds and is resilient to variability in signal
segmentation.
Interestingly, while the maximum accuracy occasionally appears in the 20–30 window range, the 10–20
configuration tends to produce more consistent average performance. This stability is valuable for practical
neuromarketing applications, where reliable performance is preferred over marginal peaks that may not
generalize. The slightly lower sensitivity compared to specificity, as noted in the description, may reflect a
conservative bias in the classifier, prioritizing avoidance of false positives in preference detection.
Table 2. Classification performance of the proposed ataLSTM model under different windowing configurations,
evaluated using 10-fold cross-validation.
Accuracy of ataLSTMCross validation No. windows  Maximum Average Minimum
1 to 10 0.931 ± (0.002) 0.926 ± (0.016) 0.917 ± (0.025)
10 to 20 0.932 ± (0.002) 0.925 ± (0.012) 0.913 ± (0.020)10-fold (1)
20 to 30 0.931 ± (0.003) 0.925 ± (0.015) 0.914± (0.021)
1 to 10 0.933 ± (0.002) 0.928 ± (0.017) 0.913 ± (0.028)
10 to 20 0.936 ± (0.002) 0.922 ± (0.014) 0.915 ± (0.022)10-fold (2)
20 to 30 0.934 ± (0.002) 0.925 ± (0.014) 0.916 ± (0.021)
1 to 10 0.932 ± (0.001) 0.924 ± (0.019) 0.910 ± (0.021)
10 to 20 0.937 ± (0.003) 0.924 ± (0.013) 0.911 ± (0.028)10-fold (3)
20 to 30 0.938 ± (0.003) 0.921 ± (0.016) 0.911 ± (0.025)
1 to 10 0.936 ± (0.001) 0.923 ± (0.019) 0.918 ± (0.023)
10 to 20 0.936 ± (0.001) 0.924 ± (0.013) 0.913 ± (0.014)10-fold (4)
20 to 30 0.934 ± (0.003) 0.929 ± (0.018) 0.915 ± (0.023)
1 to 10 0.933 ± (0.002) 0.921 ± (0.017) 0.916 ± (0.025)10-fold (5) 10 to 20 0.930 ± (0.002) 0.926 ± (0.015) 0.916 ± (0.016)
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

Moreover, the main reason for conducting five repeated 10-fold cross-validation runs is to obtain a more
stable and reliable estimate of the model’s performance by averaging results over multiple random data
partitions. This repetition reduces the influence of any single, potentially unrepresentative split of the
dataset, mitigates variance in accuracy caused by sampling bias, and increases the robustness of the
evaluation—particularly important in EEG-based studies where datasets are often small and variability
across trials can be high.
4-3 Error Analysis
The three subplots in Fig. 5 present the Root Mean Square Error (RMSE) values over training epochs for
three participant groups, comparing the proposed ataLSTM with LSTM+Attention and biLSTM+Attention
baselines. Across all groups, the ataLSTM model (red curve) consistently demonstrates a steeper and more
sustained reduction in RMSE, indicating faster convergence and better generalization throughout the
training process. In contrast, the LSTM+Attention and biLSTM+Attention models (yellow and orange
curves) converge more slowly and plateau at higher RMSE levels, suggesting comparatively higher residual
prediction errors. These trends are stable across the three independent participant groups, showing that the
advantage of ataLSTM is not group-specific but generalizes well across different subsets of the dataset. The
RMSE curves for ataLSTM also exhibit less fluctuation toward the later training epochs, implying greater
stability and robustness against overfitting. The consistently lower final RMSE values highlight its capacity
to capture fine-grained temporal dependencies and leverage attention for more precise EEG-to-preference
mappings.
Fig. 5. In this figure, we compare the almost real-time error of monitoring item selection for three random groups of
participants with two DL structures based on RMSE.
The superior error performance of ataLSTM can be attributed to its architectural integration of attention
with time-aware LSTM gating, which enables the model to assign differential weights to salient temporal
segments while maintaining awareness of irregular elapsed-time intervals between sequential decision-
making events. This dual capability reduces noise sensitivity and improves feature discrimination, leading
to more accurate and stable predictions. By contrast, the baseline models either lack explicit time-awareness
(LSTM+Attention) or do not optimize attention allocation to the same degree (biLSTM+Attention),
resulting in higher residual errors. These findings confirm that ataLSTM not only improves classification
20 to 30 0.931 ± (0.001) 0.926 ± (0.018) 0.913 ± (0.020)
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

accuracy but also minimizes prediction uncertainty, reinforcing its suitability for EEG-driven
recommendation systems.
5- Discussion
The following discussion interprets the superior accuracy and lower error rates of the proposed ataLSTM
model, linking these gains to its time-aware and attention mechanisms, and explores their implications for
neuromarketing applications.
5-1 Interpretation of Key Findings
Fig. 6 compares the confidence interval measures for item selection across three EEG-based
recommendation models—LSTM, LSTM+Attention, and the proposed ataLSTM—highlighting
differences in predictive reliability for both positive and negative consumer decisions. In Fig. 6a, the simple
LSTM model demonstrates relatively stable confidence levels across all items, with maximum confidence
values clustering between 82–83% and minimum values ranging from approximately 73–75%. The narrow
spread between max and min indicates consistent performance, though the overall confidence levels are
modest compared to more advanced models. Items such as wall clocks and belts show slightly higher
maximum confidence, suggesting that the LSTM model may capture distinctive EEG patterns for certain
product categories more effectively. However, the limited integration of temporal weighting in this
architecture constrains its ability to differentiate subtle preference signals.
73
78
83
88
Pen Wrist
watch
Sun
glasses
Sweater Socks Wall
clock
Bracelet Shirts Shoes Bag Muffler Belt Gloves Ties
Max Min
(a)
Confidence (%)
Items
EEG-based item selection utilizing confidence interval measures (LSTM)
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

Fig. 6. Average fluctuation in confidence parameters across multiple product categories for both positive
and negative customer decisions, derived from EEG-based item selection using three models: (a) LSTM,
(b) LSTM+Attention, and (c) ataLSTM. Error bars represent variability between maximum and minimum
confidence levels.
Fig. 6b shows the LSTM+Attention model, which achieves a modest yet noticeable improvement in both
maximum and minimum confidence values, with maxima consistently between 84–85% and higher minima
(~74–76%) compared to the baseline LSTM. This enhancement suggests that the attention mechanism
improves the model’s focus on key temporal segments of the EEG signal, enabling better discrimination
between liked and disliked items. The improvement is particularly pronounced for products like wall clocks,
ties, and wristwatches, which may benefit from the model’s ability to capture temporally salient decision-
making cues. Nevertheless, the gain is relatively uniform across items, indicating that attention alone cannot
fully exploit the temporal irregularities present in real EEG data.
Fig. 6c illustrates the ataLSTM model’s clear superiority, with maximum confidence values approaching
95% and minimum values rarely dropping below 75–77%. This model not only delivers higher confidence
74
79
84
89
Pen Wrist
watch
Sun
glasses
Sweater Socks Wall
clock
Bracelet Shirts Shoes Bag Muffler Belt Gloves Ties
Max Min
(b)
Confidence (%)
Items
EEG-based item selection utilizing confidence interval measures (LSTM+Attention)
75
80
85
90
95
Pen Wrist
watch
Sun
glasses
Sweater Socks Wall
clock
Bracelet Shirts Shoes Bag Muffler Belt Gloves Ties
Max Min
(c)
Confidence (%)
Items
EEG-based item selection utilizing confidence interval measures (ataLSTM)
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

across all product categories but also reduces variability, as shown by narrower error bars in several cases.
The incorporation of a time-aware mechanism in conjunction with attention appears to enhance the model’s
ability to weigh historical signals according to their temporal relevance, leading to more reliable
predictions. Items such as wall clocks, ties, and pens exhibit particularly strong performance, suggesting
that ataLSTM effectively exploits temporal dependencies and aligns them with neural activity patterns to
yield robust recommendations.
5-2 Confidence Analysis and Practical Implications
In the context of EEG-based recommendation systems, confidence represents the probability that a given
recommendation aligns with a user’s true preference, conditioned on prior behavioral or neural responses.
Unlike a static accuracy score, confidence is a dynamic measure, sensitive to the temporal and contextual
dependencies within the data. As illustrated in Fig. 6, all three models—LSTM, LSTM+Attention, and
ataLSTM—demonstrate distinct patterns in maximum and minimum confidence levels across various
product categories. These fluctuations reflect not only the variability in neural signal clarity but also the
robustness of each model’s ability to generalize beyond the training instances. The use of random sampling
for participant selection ensures that the results are not biased toward a specific subgroup, allowing the
observed confidence distributions to be attributed primarily to model behavior rather than sample
composition.
From a practical standpoint, the data in Fig. 6 reveal that the overall confidence range varies across product
categories, especially for categories with consistent neural responses (e.g., wall clocks and ties). The typical
confidence interval of 0.75–0.88 suggests a strong likelihood that a recommended product will meet user
expectations, with ataLSTM consistently pushing toward the upper bound across categories. This
improvement is particularly meaningful in neuromarketing applications, where purchase decisions are often
impulsive and time-constrained; higher confidence translates directly into more reliable real-time
personalization. Furthermore, the stability of the confidence parameter across both positive and negative
decisions implies that the proposed method minimizes bias toward either likes or dislikes, maintaining
balanced predictive behavior. When integrated with precision–recall metrics, as reflected in the F-measure,
this stability supports not only accurate classification but also consumer trust in the recommendation
pipeline.
Additionally, within EEG-driven neuromarketing recommendation frameworks, preference classification
serves as the decision-making core, transforming raw neural signals into actionable inputs that directly
shape the recommendation pipeline. The “confidence” parameter derived from EEG pattern recognition
serves as a probabilistic indicator of a user’s preference, enabling the system to rank, filter, and present
products that align closely with the user’s latent interests. By integrating temporal attention mechanisms,
the proposed ataLSTM model captures both the stability and fluctuation of user responses over time,
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

thereby enhancing the reliability of confidence scores. These scores, in turn, drive the recommendation
process by prioritizing items with the highest likelihood of acceptance while minimizing exposure to
products with low predicted relevance. Consequently, the high classification accuracy achieved in our
results directly translates into improved recommendation precision, reduced false suggestions, and a more
engaging, personalized user experience. This tight coupling between preference classification and
recommendation generation positions the system as both a robust predictive engine and an adaptive
recommender tailored to individual consumer behavior patterns.
5-3 Comparison
The F-measure, ranging from 0 to 1, serves as a balanced indicator of a system’s predictive quality by
integrating both precision and recall. In the context of EEG-driven recommendation systems, this measure
is especially critical because a model must not only correctly identify a user’s preferences but also minimize
false suggestions that could erode trust. Using the open-source neuromarketing EEG dataset [44], our
results show that the proposed ataLSTM consistently delivers higher precision–recall performance
compared to baseline LSTM and LSTM+Attention models, achieving a classification accuracy of 92.42%.
This advantage stems from its combined attention and time-aware design, which enables the model to
capture both spatial–temporal dependencies in EEG signals and the nuanced variations in neural patterns
preceding a decision. By contrast, conventional LSTM architectures, while capable of modeling sequential
dependencies, fail to fully exploit temporal weighting; and LSTM+Attention, though better at focusing on
salient EEG segments, does not explicitly account for time-based relevance decay. This distinction explains
why ataLSTM shows superior alignment between predicted and actual consumer preferences across a broad
set of product categories, surpassing results reported in prior EEG-based recommendation systems [22, 27].
From a practical perspective, incorporating time awareness into the attention mechanism addresses a key
limitation in earlier neuromarketing models [22, 27, 44]: the implicit assumption that all past neural events
contribute equally to prediction accuracy. In reality, decision-making processes are temporally sensitive,
and EEG responses closer to the purchase moment often hold greater predictive power than older, less
contextually relevant signals. By dynamically weighting these events, ataLSTM not only improves
classification performance but also provides interpretable outputs, allowing marketers to understand why
certain items were recommended or rejected. This is crucial for real-time neuromarketing applications,
where both speed and interpretability matter. When benchmarked against previous architectures using the
same dataset [44], ataLSTM demonstrates consistently narrower confidence intervals, higher classification
accuracy, and better generalization across different item categories, reinforcing its suitability for
deployment in operational consumer analytics platforms.
Despite these strengths, several limitations remain. The dataset [44], while publicly available and
standardized, involves a relatively small participant pool, which may limit the model’s exposure to the
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

diversity of consumer behaviors found in real-world markets. Furthermore, while the time-aware attention
mechanism enhances the detection of recency effects, it may underweight persistent long-term preferences
that are not strongly time-dependent. Lastly, the model’s validation has thus far been tied to the Emotiv
EPOC+ configuration; generalizing to other EEG acquisition systems or varying electrode layouts remains
an open challenge. Future research should focus on expanding participant diversity, incorporating adaptive
attention strategies that balance short- and long-term preference signals, and validating the model’s
robustness across multiple EEG hardware platforms.
6- Conclusion
This study involved adult participants in a controlled neuromarketing experiment. While limited in scale,
the results demonstrate the feasibility and promise of EEG-driven recommendation systems for enhancing
consumer experience. This study introduces a pioneering, time-aware, attention-based EEG
recommendation framework that translates neural responses to marketing stimuli into actionable,
personalized product suggestions. By aggregating EEG activity from multiple participants and weighting
prior events through an attention mechanism, the framework captures both temporal dynamics and
consumer-specific patterns. It accommodates diverse inputs, including static imagery and promotional
videos, while employing band-power-based channel selection and topographical mapping to improve
predictive accuracy and computational efficiency. Beyond its technical rigor, the system offers substantial
practical value: clustering correlated neural responses reveals distinct consumer segments, and integrating
purchase histories enables highly tailored recommendations. Attention outputs also highlight influential
temporal windows and EEG channels, providing marketers with interpretable insights to guide campaign
strategy and creative design.
Despite these contributions, several limitations remain. The framework relies on a single neuromarketing
dataset with a relatively homogeneous participant pool, which may limit generalizability across
demographic and cultural contexts. Its commercial impact has yet to be validated through live campaign
trials, leaving current claims as inferential rather than causal. The band-power selection method may
overlook subtle yet meaningful EEG features, and attention weights indicate model relevance rather than
neuroscientific causality. While transparency and privacy are conceptually addressed, practical mechanisms
for their implementation are not yet developed. In sum, this work delivers a robust and empirically grounded
EEG recommendation framework that bridges marketing science and consumer experience design. By
outlining a clear path for broader validation, multimodal integration, and privacy-preserving deployment,
it establishes a strong foundation for future innovations in neuromarketing—offering the potential to
transform how neural insights drive personalized consumer engagement.
Declarations
(1) Data and code availability
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

The input data used in this study were obtained from the publicly available neuromarketing EEG dataset
described in Ref. [44]. The dataset used in the present analysis, together with the MATLAB source code and
supporting materials, is publicly available through the following repository:
https://github.com/Khosravi4GH/eeg-attention-lstm-neuromarketing
The repository includes the dataset used for the present analysis, main analysis scripts, data-reading and
preprocessing functions, attention-based time-aware LSTM network-construction code, label files, the
trained network, and supporting documentation required to reproduce the reported analyses.
(2) Competing interests
The authors declare that they have no competing interests.
(3) Funding and support
This work was supported by the following grants and research projects:
Key Research Project of Natural Science in Colleges and Universities of Anhui Provincial Department of
Education (KJ2021A1163);
Anhui Xinhua University – Intelligent Automation Research Institute (yjs202104);
Major Teaching and Research Project of Quality Engineering Project of Education Department of Anhui
Province, No. 2022jyxm649;
High-level Talent Research Start-up Fund Project and Class A Doctoral Research Fund Project of WFUST
(KJRC2024016, KJRC2025002, KJRC2026003);
Anhui Provincial Department of Education Quality Engineering Project School-Enterprise Cooperation
Practice Education Base (2022xqhz028).
(4) Ethics approval and consent to participate
This study involved only a secondary analysis of a publicly available dataset. The authors did not recruit new
participants, collect new human data, or conduct any animal experiments. Therefore, no separate ethical
approval or informed consent was obtained for the present secondary analysis. Ethical approval and
informed-consent procedures relating to the original data collection remain as reported by the creators of
the dataset in Ref. [44].
The dataset used for the present secondary analysis is available through the public repository specified in
the Data and code availability statement above.
(5) Consent for publication
Not applicable.
(6) Author contributions statement
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

X.Y. (Yang), Z.B., and D.L. prepared the initial draft, data, and code, with Z.B. and D.L. providing assistance
with their preparation. M.K. managed the research project together with X.Y. (Yang) and contributed to the
development of the research concept. Q.W., F.W., and X.Y. (Ye) provided technical feedback and editorial
support for different aspects of the work.
(7) Statement on AI-assisted language editing
We acknowledge that AI-based language-editing tools, such as Google Gemini, were used exclusively for
light grammatical correction and stylistic refinement. No content generation or substantive writing was
performed using AI, and all revisions were fully reviewed and approved by the authors.
References
1. Halkiopoulos C, Antonopoulou H, Gkintoni E, Aroutzidis A. Neuromarketing as an indicator of cognitive
consumer behavior in decision-making process of tourism destination—An overview. InTranscending
Borders in Tourism Through Innovation and Cultural Heritage: 8th International Conference, IACuDiT,
Hydra, Greece, 2021 2022 Apr 28 (pp. 679-697). Cham: Springer International Publishing.
2. Lee N, Broderick AJ, Chamberlain L. What is ‘neuromarketing’? A discussion and agenda for future
research. International journal of psychophysiology. 2007 Feb 1;63(2):199-204.
3. Iloka BC, Onyeke KJ. Neuromarketing: a historical review. Neuroscience Research Notes. 2020 Sep
20;3(3):27-35.
4. Hsu L, Chen YJ. Neuromarketing, subliminal advertising, and hotel selection: An EEG study. Australasian
Marketing Journal. 2020 Nov;28(4):200-8.
5. Boriceanu V. How to Understand the Consumer’s and the Market’s Way of Thinking. Marketing From
Information to Decision. 2009(2):95-104.
6. Fisher CE, Chin L, Klitzman R. Defining neuromarketing: Practices and professional challenges. Harvard
review of psychiatry. 2010 Jul 1;18(4):230-7.
7. Mansor AA, Isa SM. Fundamentals of neuromarketing: what is it all about?. Neuroscience Research Notes.
2020 Dec 3;3(4):22-8.
8. Javor A, Koller M, Lee N, Chamberlain L, Ransmayr G. Neuromarketing and consumer neuroscience:
contributions to neurology. BMC Neurology. 2013;13:13. doi:10.1186/1471-2377-13-13.
9. Nemorin S, Gandy Jr OH. Exploring neuromarketing and its reliance on remote sensing: Social and ethical
concerns. International Journal of Communication. 2017 Nov 13;11:21.
10. Robaina-Calderín L, Martín-Santana JD. A review of research on neuromarketing using content analysis: key
approaches and new avenues. Cognitive Neurodynamics. 2021 Dec;15(6):923-38.
11. Kreutzer RT. General Basics of Marketing. InPractice-Oriented Marketing: Basics–Instruments–Case
Studies 2023 Mar 9 (pp. 1-65). Wiesbaden: Springer Fachmedien Wiesbaden.
12. Babiloni F, Cherubino P. Consumer Neuroscience: A Neural Engineering Approach. InHandbook of
Neuroengineering 2023 Feb 3 (pp. 2861-2889). Singapore: Springer Nature Singapore.
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

13. Costa-Feito, A., González-Fernández, A. M., Rodríguez-Santos, C., & Cervantes-Blanco, M. (2023).
Electroencephalography in consumer behaviour and marketing: a science mapping approach. Humanities and
Social Sciences Communications, 10(1), 1-13.
14. Agarwal S, Dutta T. Neuromarketing and consumer neuroscience: current understanding and the way
forward. Decision. 2015 Dec;42(4):457-62.
15. Dutta T, Mandal MK. Consumer happiness and decision making: the way forward. Consumer Happiness:
Multiple Perspectives. 2021:153-61.
16. Khurana V, Gahalawat M, Kumar P, Roy PP, Dogra DP, Scheme E, Soleymani M. A survey on
neuromarketing using EEG signals. IEEE Transactions on Cognitive and Developmental Systems. 2021 Mar
12;13(4):732-49.
17. Zhang Y, Thaichon P, Shao W. Neuroscientific research methods and techniques in consumer research.
Australasian Marketing Journal. 2023 Aug;31(3):211-27.
18. Ariely D, Berns GS. Neuromarketing: the hope and hype of neuroimaging in business. Nature reviews
neuroscience. 2010 Apr;11(4):284-92.
19. Suhendro JM, Wibawa AD, Mas A. Analysis of Attraction Response on Product Packaging Based on EEG
Signal:(A preliminary study of Neuromarketing on Packaging). In2023 International Electronics Symposium
(IES) 2023 Aug 8 (pp. 479-485).
20. Boz H, Arslan A, Koc E. Neuromarketing aspect of tourısm pricing psychology. Tourism Management
Perspectives. 2017 Jul 1;23:119-28.
21. Sharma L, Gera A. A survey of recommendation system: Research challenges. International Journal of
Engineering Trends and Technology (IJETT). 2013 May;4(5):1989-92.
22. Guo G, Elgendi M. A new recommender system for 3D e-commerce: an EEG based approach. Journal of
Advanced Management Science. 2013 Mar;1(1):61-5.
23. Bandara SK, Wijesinghe UC, Jayalath BP, Bandara SK, Haddela PS, Wickramasinghe LM. Eeg based
neuromarketing recommender system for video commercials. In2021 IEEE 16th International Conference on
Industrial and Information Systems (ICIIS) 2021 Dec 9 (pp. 11-16).
24. Khosravi M, Parsaei H, Rezaee K. Novel Classification Scheme for Early Alzheimer's Disease (AD) Severity
Diagnosis Using Deep Features of the Hybrid Cascade Attention Architecture: Early Detection of AD on
MRI Scans. Tsinghua Science and Technology. 2025 Jul 4;30(6):2572-91. doi:10.26599/TST.2024.9010080
25. Liu Y, Li D, Wan S, Wang F, Dou W, Xu X, Li S, Ma R, Qi L. A long short‐term memory‐based model for
greenhouse climate prediction. International Journal of Intelligent Systems. 2022 Jan;37(1):135-51.
26. Oon HN, Saidatul A, Ibrahim Z. Analysis on Non-linear features of electroencephalogram (EEG) signal for
neuromarketing application. In2018 international conference on computational approach in smart systems
design and applications (ICASSDA) 2018 Aug 15 (pp. 1-8).
27. Panda D, Chakladar DD, Rana S, Parayitam S. An EEG‐based neuro‐recommendation system for improving
consumer purchase experience. Journal of Consumer Behaviour. 2024 Jan;23(1):61-75.
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

28. Mashrur FR, Rahman KM, Miya MT, Vaidyanathan R, Anwar SF, Sarker F, Mamun KA. Intelligent
neuromarketing framework for consumers' preference prediction from electroencephalography signals and
eye tracking. Journal of Consumer Behaviour. 2024 May;23(3):1146-57.
29. Wang J, Alsharif AH, Abd Aziz N, Khraiwish A, Salleh NZ. Neuro-Insights in Marketing Research: A
PRISMA-Based Analysis of EEG Studies on Consumer Behavior. SAGE Open. 2024
Dec;14(4):21582440241305365.
30. Wang P, Mu W, Zhan G, Wang A, Song Z, Fang T, Zhang X, Wang J, Niu L, Bin J, Zhang L. Preference
detection of the humanoid robot face based on EEG and eye movement. Neural Computing and Applications.
2024 Jul;36(19):11603-21.
31. Golnar-Nik P, Farashi S, Safari MS. The application of EEG power for the prediction and interpretation of
consumer decision-making: A neuromarketing study. Physiology & behavior. 2019 Aug 1;207:90-8.
32. Gauba H, Kumar P, Roy PP, Singh P, Dogra DP, Raman B. Prediction of advertisement preference by fusing
EEG response and sentiment analysis. Neural Networks. 2017 Aug 1;92:77-88.
33. Panda D, Chakladar DD, Dasgupta T. Prediction of consumer preference for the bottom of the pyramid using
EEG-based deep model. International Journal of Computational Science and Engineering. 2021;24(5):439-
49.
34. Ishtiaque F, Miya MT, Mashrur FR, Rahman KM, Vaidyanathan R, Anwar SF, Sarker F, Ali NA, Tat HH,
Mamun KA. Machine learning-based viewers’ preference prediction on social awareness advertisements
using EEG. Frontiers in Human Neuroscience. 2025 Jun 13;19:1542574.
35. Chang HY, Huang SC, Wu JH. A personalized music recommendation system based on
electroencephalography feedback. Multimedia Tools and Applications. 2017 Oct;76:19523-42.
36. Shaw R, Patra BK. Cognitive-aware lecture video recommendation system using brain signal in flipped
learning pedagogy. Expert Systems with Applications. 2022 Nov 30;207:118057.
37. Aldayel M, Ykhlef M, Al-Nafjan A. Deep learning for EEG-based preference classification in -
neuromarketing. Applied Sciences. 2020 Feb 24;10(4):1525. Doi: 10.3390/app10041525
38. Al-Nafjan A. Feature selection of EEG signals in neuromarketing. PeerJ Computer Science. 2022 Apr
26;8:e944.
39. Pagan KM, Giraldi JD, Maheshwari V, de Paula AL, de Oliveira JH. Evaluating cognitive processing and
preferences through brain responses towards country of origin for wines: the role of gender and involvement.
International Journal of Wine Business Research. 2021 Nov 12;33(4):481-501.
40. Kaya Ü, Akay D, Ayan SŞ. EEG-based emotion recognition in neuromarketing using fuzzy linguistic
summarization. IEEE Transactions on Fuzzy Systems. 2024 Apr 22;32(8):4248-59.
41. Cenizo C. A Neuromarketing Approach to Consumer Behavior on Web Platforms. International Journal of
Consumer Studies. 2025 Mar;49(2):e70034.
42. Panda D, Chakladar DD, Rana S, Shamsudin MN. Spatial attention-enhanced EEG analysis for profiling
consumer choices. Ieee Access. 2024 Jan 19;12:13477-87.
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS

43. Song G, Gazi MA, Waaje A, Roshid MM, Karim R, Rahaman MA, Min Z, bin S Senathirajah AR. The
neuromarketing: Bridging neuroscience and marketing for enhanced consumer engagement. IEEE Access.
2025 Feb 25.
44. Yadava M, Kumar P, Saini R, Roy PP, Prosad Dogra D. Analysis of EEG signals and its application to
neuromarketing. Multimedia Tools and Applications. 2017 Sep;76:19087-111.
45. Wang M, Yao R, Rezaee K. MU-Net-optLSTM: Two-Stream Spatial–Temporal Feature Extraction and
Classification Architecture for Automatic Monitoring of Crowded Art Museums. Tsinghua Science and
Technology. 2026;31(4):2304–2321. doi:10.26599/TST.2024.9010003.
46. Baytas IM, Xiao C, Zhang X, Wang F, Jain AK, Zhou J. Patient subtyping via time-aware LSTM networks.
InProceedings of the 23rd ACM SIGKDD international conference on knowledge discovery and data mining
2017 Aug 4 (pp. 65-74).
ACCEPTED MANUSCRIPT
ARTICLE IN PRESSARTICLE IN PRESS
