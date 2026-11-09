---
title: A Data-Driven Multimodal Method for Early Detection of Coordinated Abnormal Behaviors in Live-Streaming
  Platforms
url: https://arxiv.org/abs/2609.01649
category: ai-marketing
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Jingwen Luo
- Pinrui Zhu
- Yiyan Wang
- Zilin Xiao
- Jingqi Li
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.01649
pages: 27
chars: 99820
fetched_at: '2026-11-08T13:19:35+00:00'
kb_version: 1
---

# A Data-Driven Multimodal Method for Early Detection of Coordinated Abnormal Behaviors in Live-Streaming Platforms

Academic Editor: Xin Luo
Received: 26 December 2025
Revised: 26 January 2026
Accepted: 9 February 2026
Published: 11 February 2026
Copyright: © 2026 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license.
Article
A Data-Driven Multimodal Method for Early Detection of
Coordinated Abnormal Behaviors in Live-Streaming Platforms
Jingwen Luo 1,2,†, Pinrui Zhu 1,†, Yiyan Wang 1,†, Zilin Xiao 1,3,†, Jingqi Li 1, Xuebei Kong 1 and Yan Zhan 1,4,*
1 National School of Development, Peking University, Beijing 100871, China
2 College of Information and Electrical Engineering, China Agricultural University, Beijing 100083, China
3 School of Foreign Studies, Beijing Language and Culture University, Beijing 100083, China
4 Artificial Intelligence Research Institute, Tsinghua University, Beijing 100084, China
* Correspondence: yan_zhan_thu@163.com
† These authors contributed equally to this work.
Abstract
With the rapid growth of live-streaming e-commerce and digital marketing, abnormal mar-
keting behaviors have become increasingly concealed, coordinated, and intertwined across
heterogeneous data modalities, posing substantial challenges to data-driven platform gover-
nance and early risk identification. Existing approaches often fail to jointly model cross-modal
temporal semantics, the gradual evolution of weak abnormal signals, and organized group-
level manipulation. To address these challenges, a data-driven multimodal abnormal behavior
detection framework, termed MM-FGDNet, is proposed for large-scale live-streaming envi-
ronments. The framework models abnormal behaviors from two complementary perspectives,
namely temporal evolution and cooperative group structure. A cross-modal temporal align-
ment module first maps video, text, audio, and user behavioral signals into a unified temporal
semantic space, alleviating temporal misalignment and semantic inconsistency across modali-
ties. Building upon this representation, a temporal fraud pattern modeling module captures
the progressive transition of abnormal behaviors from early incipient stages to abrupt out-
breaks, while a cooperative manipulation detection module explicitly identifies coordinated
interactions formed by organized user groups and automated accounts. Extensive experi-
ments on real-world multi-platform live-streaming e-commerce datasets demonstrate that
MM-FGDNet consistently outperforms representative baseline methods, achieving an AUC of
0.927 and an F1 score of 0.847, with precision and recall reaching 0.861 and 0.834, respectively ,
while substantially reducing false alarm rates. Moreover, the proposed framework attains
an Early Detection Score of 0.689. This metric serves as a critical benchmark for operational
viability , quantifying the system’s capacity to shift platform governance from passive reme-
diation to proactive prevention. It confirms the reliable identification of the “weak-signal”
stage—rigorously defined as the incipient phase where subtle, synchronized deviations in
interaction rhythms manifest prior to traffic inflation outbreaks—thereby providing the neces-
sary time window for preemptive intervention against coordinated manipulation. Ablation
studies further validate the independent contributions of each core module, and cross-domain
generalization experiments confirm stable performance across new streamers, new product
categories, and new platforms. Overall, MM-FGDNet provides an effective and scalable data-
driven artificial intelligence solution for early detection of coordinated abnormal behaviors in
live-streaming systems.
Keywords: live-streaming analysis; big data; graph neural networks; cross-modal temporal
alignment; cross-domain generalization
Electronics 2026, 15, 769 https://doi.org/10.3390/electronics15040769
arXiv:2609.01649v1  [cs.SI]  30 Aug 2026

Electronics 2026, 15, 769 2 of 27
1. Introduction
With the rapid development of the digital economy and platform-based business
models, live-streaming e-commerce, short-video marketing, and social media content dis-
tribution have become deeply integrated, gradually forming a digital marketing ecosystem
driven by user interaction behaviors [ 1]. Within this ecosystem, metrics such as watch
duration, comment content, likes, and tipping behaviors not only directly influence product
conversion rates but also serve as critical signals for platform recommendation mechanisms
and traffic allocation strategies [2]. However, alongside the continuous amplification of
commercial value, a wide range of profit-driven abnormal marketing and fraudulent be-
haviors have emerged with increasing frequency, including fake tipping, order brushing,
traffic inflation, bot-generated comments, coordinated opinion manipulation by organized
groups, fabricated follower growth, and emotional manipulation [3]. For instance, orga-
nized groups often utilize high-frequency fake tipping to trigger algorithmic promotion
mechanisms, leading to artificial traffic inflation that unfairly displaces legitimate content.
By creating such artificial popularity, these behaviors mislead consumer decision-making,
undermine the fairness of platform ecosystems, and significantly increase the difficulty
of platform governance and regulatory enforcement [4]. Unlike traditional e-commerce
scenarios, live-streaming e-commerce is characterized by strong temporal dynamics, high
interactivity, and the coexistence of multiple information modalities [5]. Crucially, abnor-
mal marketing behaviors manifest across these heterogeneous modes: a sudden surge in
transaction volume (behavioral modality) may contradict the flat emotional trajectory of the
streamer (audio/visual modality), or a flood of bot-generated comments (textual modality)
may appear semantically disjointed from the current video context. These behaviors are
rarely isolated events; instead, they tend to emerge gradually through coordinated changes
in streamer behaviors, comment sentiment, transaction rhythms, and user interaction net-
works [6]. As a result, single-modality or static features are insufficient to comprehensively
capture the evolutionary process of fraudulent behaviors [7]. Therefore, the development of
an intelligent detection framework capable of integrating multimodal information, model-
ing temporal evolution, and identifying cooperative manipulation patterns is of significant
theoretical value and practical importance for safeguarding platform content ecosystems,
protecting consumer rights, and improving regulatory efficiency.
Early studies on marketing fraud detection primarily relied on statistical modeling
and manual feature engineering, such as threshold-based abnormal traffic detection, time-
series statistical feature analysis, and anomaly scoring methods based on user behavior
frequency [8]. Although these methods demonstrate certain effectiveness in scenarios
with clear rules and stable patterns, they heavily depend on prior experience and struggle
to adapt to complex and rapidly evolving live-streaming marketing environments [ 9].
Subsequently, machine learning models [10], including logistic regression, support vector
machines, and random forests, were introduced to perform fraud classification based on
manually designed feature vectors [11]. However, such approaches typically assume rela-
tively stable data distributions and require high-quality labeled data [12,13]. In real-world
live-streaming scenarios, abnormal marketing behaviors are often characterized by extreme
class imbalance, rapid evolution of fraud patterns, and high annotation costs, which sig-
nificantly limits model generalization performance [14]. In addition, some studies have
employed graph-based models or social network analysis techniques to characterize user
interaction relationships for identifying order-brushing groups or abnormal user commu-
nities. Nevertheless, these methods predominantly focus on structural information while
overlooking the temporal evolution of behaviors and cross-modal semantic consistency,
making it difficult to explain the coordinated manifestations of complex fraudulent be-
haviors across content, emotion, and transaction dimensions [15]. Overall, conventional
https://doi.org/10.3390/electronics15040769

Electronics 2026, 15, 769 3 of 27
approaches generally suffer from the following limitations: (1) reliance on single-modality
or static features, resulting in limited sensitivity to cross-modal abnormal signals; (2) in-
sufficient capability to detect small-sample, weak-signal, and covert fraud patterns; and
(3) poor adaptability to distribution shifts across platforms, streamer types, and product
categories.
In recent years, deep learning has achieved remarkable progress in computer vision,
natural language processing, and speech analysis, providing new technical foundations
for fraud detection in complex marketing scenarios [ 16]. Several studies have explored
the use of convolutional neural networks or transformer architectures for video content
analysis to identify abnormal behaviors or emotional variations, while text models based
on sentiment analysis and semantic representation learning have been applied to detect
abnormal comments and coordinated spam content [17]. Moreover, recurrent neural net-
works and transformer-based models have demonstrated strong capabilities in modeling
temporal dependencies within user behavior sequences [18]. Building upon these advances,
multimodal deep learning approaches have gradually attracted attention by integrating
visual, textual, audio, and behavioral sequence information to enhance the perception of
complex abnormal patterns [19]. Despite these advances, significant challenges remain.
First, substantial discrepancies in temporal granularity and semantic representation exist
across different modalities, rendering simple concatenation or attention-based fusion insuf-
ficient for effective alignment [20]. Second, most existing models rely on large-scale labeled
data for supervised training, leading to pronounced performance degradation in scenarios
with scarce fraud samples or noisy annotations [21,22]. Third, the organizational structure
of cooperative behaviors is often neglected, limiting the ability to identify artificially gener-
ated popularity driven by coordinated bot clusters or organized groups [23]. Consequently,
achieving cross-modal temporal alignment under weak supervision, modeling the dynamic
evolution of abnormal behaviors, and explicitly characterizing cooperative manipulation
patterns remain critical open problems. Khodabandehlou et al. [24] proposed FiFrauD, an
unsupervised financial fraud detection framework that performs temporal representation
learning on dynamic transaction graph streams by jointly modeling node structural features
and behavioral evolution patterns. Under unsupervised settings, effective identification of
financial fraud was achieved, with significant improvements over traditional static graph
models and statistical anomaly detection methods on multiple real-world financial datasets,
particularly in terms of AUC, detection accuracy, early risk identification capability, and
generalization performance in dynamic graph scenarios. Chen et al. [ 25] proposed an
opinion evolution analysis framework for live-streaming e-commerce regulation policies
based on online comment mining, in which LDA topic modeling and sentiment analysis
were employed to reveal dynamic changes in public sentiment and attention focus follow-
ing policy implementation, enabling quantitative characterization of policy effects and
behavioral patterns. Shehnepoor et al. [ 26] introduced the HIN-RNN heterogeneous infor-
mation network representation learning framework, which constructs meta-path-guided
node sequences and leverages recurrent neural networks to automatically learn high-order
cooperative behavior patterns among fraudsters without manual feature engineering, sig-
nificantly improving AUC and recall for fraud group detection on real-world datasets. Yu
et al. [27] proposed the TGFDN group fraud detection framework, which incorporates a
Temporal Group Dynamics Analyzer to model the temporal evolution of group behaviors
in transaction networks, achieving substantial improvements in accuracy and recall for
group fraud identification on large-scale e-commerce and bitcoin datasets. Li et al. [ 28]
developed the LIFE heterogeneous graph neural network framework, which integrates
multiple entity relationships among users, streamers, and products and introduces a label
https://doi.org/10.3390/electronics15040769

Electronics 2026, 15, 769 4 of 27
propagation mechanism, leading to significant gains in abnormal transaction detection
accuracy and recall in live-streaming e-commerce fraud detection tasks.
To address the aforementioned challenges, a multimodal fraud behavior detection
framework for live-streaming e-commerce, termed MM-FGDNet, is proposed, with the
main contributions summarized as follows:
1. A multimodal abnormal marketing dataset encompassing video, text, audio, and user
behavior sequences is constructed, together with data synchronization and quality
calibration strategies to enhance cross-modal consistency and reliability.
2. A cross-modal temporal alignment module is proposed, which integrates dynamic
time alignment and semantic attention mechanisms to achieve effective fusion of
heterogeneous modalities within a unified temporal semantic space.
3. A transformer-based temporal anomaly modeling module is designed to capture
early weak signals and abrupt abnormal patterns of fraudulent behaviors, thereby
enhancing the detection capability for covert marketing fraud.
4. A cooperative behavior detection module is introduced, in which graph neural net-
works are employed to model user interaction structures, enabling the identification
of organized groups such as paid posters and bot clusters, along with interpretable
abnormal subgraph analysis.
5. Diffusion models and self-supervised learning strategies are incorporated to improve
model generalization performance and cross-scenario transferability under weakly
labeled and small-sample conditions.
The proposed MM-FGDNet systematically characterizes abnormal marketing behav-
iors in live-streaming e-commerce from three complementary perspectives: multimodal
temporal alignment, temporal anomaly evolution modeling, and cooperative behavior
identification. Compared with existing approaches, the proposed framework is capable
of capturing cross-modal weak signals and identifying complex fraud patterns organized
through multi-user coordination, demonstrating significant advantages in early risk de-
tection and cross-platform generalization, and providing a practically valuable intelligent
detection solution for digital marketing regulation and platform governance.
2. Related Work
2.1. Multimodal Temporal Representation Learning
The core objective of multimodal temporal representation learning lies in jointly mod-
eling dynamic information from different perceptual channels and characterizing their com-
plementary relationships within a unified temporal semantic space [29]. In live-streaming
e-commerce and digital marketing scenarios, visual content, speech signals, textual com-
ments, and user interaction behaviors collectively constitute a complex, time-evolving mar-
keting context [30]. Existing studies have demonstrated that relying on a single modality is
often insufficient for capturing rapidly changing behavioral nuances, whereas multimodal
fusion can substantially enhance the representation of complex temporal semantics [31]. In
the visual modality, approaches such as temporal convolutional networks or transformer
architectures are commonly deployed to characterize streamers’ body movements, facial
expressions, and scene transitions, thereby capturing continuous behavioral cues related to
user engagement [32]. With the introduction of self-attention mechanisms, these models
can effectively capture long-range temporal dependencies, enabling a more comprehensive
understanding of behavioral evolution throughout live-streaming sessions [33]. However,
such approaches typically prioritize content representation and rarely model the dynamic,
non-linear interactions between content evolution and user feedback [34].
https://doi.org/10.3390/electronics15040769

Electronics 2026, 15, 769 5 of 27
For the speech and audio modality, sequential modeling techniques for emotion recog-
nition and prosody analysis have been widely adopted to characterize streamers’ emotional
states and expressive styles over time [35]. Deep neural networks based on acoustic features
can reflect the rhythm of live-streaming and instantaneous emotional fluctuations, provid-
ing potential temporal cues for abnormal behavior analysis [36]. Nevertheless, the causal
relationship between vocal emotion and marketing outcomes is highly context-dependent,
and audio features alone are often insufficient to yield stable risk judgments [37]. Similarly,
research on the textual modality has shifted from static sentiment analysis to dynamic mod-
eling of comments and bullet screens [38]. Methods based on pretrained language models
are capable of capturing emotional tendencies, topic shifts, and potential manipulation
traces in text streams [39]. However, in live-streaming e-commerce scenarios, the text data
is characterized by high noise, short length, and extreme repetition, making it difficult for
standard sequential text models to distinguish genuine high-frequency interactions from
organized comment brushing behaviors [40].
To bridge these gaps, cross-modal representation learning aims to enable informa-
tion interaction across modalities through shared embedding spaces or attention mecha-
nisms [41]. Representative approaches include fusion models based on alignment learning
and contrastive learning, whose objective is to establish semantic consistency among differ-
ent modalities [42]. Despite these advancements, existing multimodal temporal paradigms
face significant limitations when addressing organized group-level manipulation in real-
time. Most current approaches focus on the temporal evolution of individual users or
isolated content semantics, lacking the capability to explicitly model the topological struc-
ture of coordinated interactions among multiple accounts. Consequently, these paradigms
struggle to distinguish between genuine organic popularity and synchronized artificial traf-
fic generated by bot clusters or “water armies,” rendering them insufficient for the timely
detection and mitigation of collaborative fraud patterns in highly dynamic live-streaming
environments.
2.2. Graph-Based Relational Structure Modeling
While fundamental anomaly detection relies on identifying deviations from normal
patterns [43], traditional statistical and time-series approaches—ranging from distribu-
tion analysis [44] to transformer-based temporal modeling [45]—predominantly focus on
individual behavioral sequences. These methods exhibit advantages in detecting sud-
den trend changes but struggle to identify abnormal patterns formed through multi-user
coordination [46]. To address this limitation, graph-based relational structure modeling
has been widely adopted to characterize the topological dependencies among users. By
constructing user–user or user–item interaction networks, these approaches leverage graph
neural networks to learn high-order relational information, showing strong potential in
detecting group-based order brushing and cooperative fraud structures that are invisible to
independent sequence analysis [47].
However, a critical bottleneck remains in the current landscape: most existing graph
models treat user interactions as static topological snapshots or overlook the fine-grained
temporal evolution of node behaviors alongside multimodal content [48]. By separating
structural inference from temporal dynamics and content semantics, existing paradigms
fail to capture the continuous, dynamic formation process of organized group-level manip-
ulation in real-time. Consequently, these methods are often unable to distinguish between
organic community growth and the rapid, synchronized deployment of “water armies” or
bot clusters during live-streaming events, leading to a lag in risk response.
https://doi.org/10.3390/electronics15040769

Electronics 2026, 15, 769 6 of 27
2.3. Generative and Weakly Supervised Learning Paradigms
In real-world marketing scenarios, fraud samples are typically scarce and costly to
annotate, posing severe challenges to traditional supervised learning methods [ 49]. To
address this, the central idea of weakly supervised learning is to reduce dependence
on manually labeled data by exploiting intrinsic data structures or generating auxiliary
samples to enhance model learning capability [50]. Self-supervised learning paradigms
enable models to learn general representations from unlabeled data by designing surrogate
prediction tasks, thereby providing effective initialization for downstream tasks [51]. In the
context of fraud detection, self-supervised approaches are employed to model the temporal
regularities of normal behaviors, such that abnormal behaviors naturally deviate from the
normal distribution in the representation space [ 52]. Furthermore, contrastive learning
strengthens sensitivity to subtle differences by constructing positive and negative sample
pairs, demonstrating promising performance in anomaly detection and user behavior
modeling [53].
Complementing these approaches, generative models provide an alternative solution
to the few-shot problem. Methods based on generative adversarial networks can synthesize
limited fraud samples to alleviate class imbalance, while diffusion models progressively
model data distributions and exhibit stronger stability in generating high-quality temporal
samples [54]. Such generative approaches are beneficial for enriching the representational
space of abnormal patterns when fraudulent interaction data are scarce [55]. Meanwhile,
few-shot classification methods aim to achieve effective classification under extremely
limited labeled samples through metric learning or prototypical learning [56]. However, in
complex marketing scenarios, fraudulent behaviors are often highly diverse and covert,
rendering it difficult for standalone few-shot classification methods to cover all potential
patterns [57]. More critically, while these paradigms effectively address data scarcity, they
typically focus on individual sample augmentation or static distribution learning. They
lack the mechanism to explicitly model the dynamic topological evolution of organized
group-level manipulation, and thus fail to capture the real-time synchronized signals
characteristic of collaborative fraud in live-streaming environments.
3. Materials and Method
3.1. Data Collection
The data collection process in this study was conducted around real-world live-
streaming e-commerce and digital marketing scenarios, with the objective of systematically
characterizing the manifestations of abnormal marketing and fraudulent behaviors in mul-
timodal spaces. The data were primarily collected from publicly accessible live-streaming
rooms and product promotion scenarios on multiple mainstream live e-commerce and
short-video platforms, with a continuous collection period spanning six months. This
temporal coverage included different time intervals, streamer types, and product categories
to reduce temporal bias and scenario-specific bias. The collected data encompassed mul-
tiple heterogeneous modalities, including live-streaming video streams, streamer speech
signals, user comments and barrage text, tipping and transaction logs, and user interaction
behavior sequences, as shown in Table 1. All data were obtained through publicly available
platform interfaces, compliant crawling tools, and real-time stream monitoring, without
involving any user private information.
For the visual modality, live-streaming video data were collected in raw stream format,
and key frames were extracted at fixed temporal intervals to balance temporal completeness
and computational efficiency. Video resolution and frame rate were preserved according
to the original platform settings to ensure the authenticity of streamer facial expressions,
body movements, and scene variations. Audio data were synchronously collected with
https://doi.org/10.3390/electronics15040769

Electronics 2026, 15, 769 7 of 27
video streams and processed using a unified sampling rate, enabling the extraction of vocal
emotion, prosodic variations, and abnormal expressive patterns. Textual modality data
included live comment streams and barrage streams, for which timestamps, user identifiers,
and textual content were fully retained to support subsequent temporal analysis and
cooperative behavior modeling. Behavioral and transaction data covered interaction events
such as likes, follows, shares, tipping, and purchases, with millisecond-level timestamps,
behavior types, and associated targets recorded to characterize behavior intensity, frequency
variations, and bursty anomalies.
To support cross-modal analysis, all modalities were synchronously aligned through
a unified timestamp mechanism, thereby constructing a consistent temporal index across
data sources. During data collection, both normal marketing scenarios and abnormal
marketing events confirmed through a combination of manual inspection and rule-based
verification were included, covering typical patterns such as concentrated bursts of fake
tipping, highly homogeneous comment content, and coordinated interactions among user
groups. The resulting dataset exhibits strong representativeness in terms of temporal
span, modal coverage, and behavioral complexity, providing a solid data foundation for
subsequent multimodal alignment, temporal anomaly modeling, and cooperative behavior
detection.
Table 1. Overview of the multimodal fraud detection dataset.
Data Modality Source Quantity Granularity
Live-stream video frames Live e-commerce platforms 3.2 M frames Frame-level
Audio segments Live-stream audio tracks 18,400 clips Segment-level
Comments & barrage text Live comment streams 12.6 M entries Message-level
Transaction records Tipping and order logs 1.8 M events Event-level
User interaction sequences Likes, follows, shares 9.4 M actions Action-level
3.2. Data Preprocessing and Augmentation
In live-streaming e-commerce scenarios, multimodal data are characterized by het-
erogeneous sources, high noise levels, and inconsistent temporal granularity. Directly
feeding raw data into learning models often leads to disordered feature distributions and
the masking of abnormal patterns. Therefore, systematic preprocessing and augmentation
of text, video, and user behavior sequences prior to modeling are essential for improving
robustness and generalization performance. In this study, unified processing is conducted
from multiple perspectives, including multimodal signal denoising, explicit modeling of se-
mantic and emotional information, temporal behavior normalization, and synthesis of rare
fraud patterns, thereby laying a solid foundation for subsequent cross-modal alignment and
anomaly detection. For the textual modality, live-streaming comments and bullet-screen
messages typically exhibit extremely short length, strong colloquiality, high redundancy,
and frequent noise tokens. The primary objective of text preprocessing is to reduce the
interference of irrelevant noise on semantic representations while preserving emotional
and semantic cues indicative of abnormal marketing behaviors. Specifically, raw comment
text is first processed through a normalization mapping function that converts emojis,
abbreviations, and non-standard characters into unified semantic units. Let the original
text sequence be denoted as T = {w1, w2, . . ., wn}, and the normalized text representation
can be expressed as
˜T = ϕ(T), (1)
where ϕ(·) denotes the text cleaning and standardization mapping operator. On this
basis, a contextual encoding model is employed to extract semantic representations Et,
while an emotion analysis module is introduced to model the emotional states of the text.
https://doi.org/10.3390/electronics15040769

Electronics 2026, 15, 769 8 of 27
Emotional labels can be regarded as projections of the text in an emotional space, and their
computation can be formulated as
st = femo(Et), (2)
where femo(·) denotes the emotion prediction function, and st represents the emotion score
or emotion vector at the corresponding time step. Through joint modeling of semantic and
emotional representations, the textual modality not only reflects comment content itself
but also captures potential fraud signals such as emotional manipulation and abnormal
opinion guidance.
In the video modality, live-streaming frames are often affected by illumination vari-
ations, compression artifacts, and motion blur, which may interfere with the analysis of
streamer behaviors and scene changes. To address this issue, denoising and quality cor-
rection are first applied to video frame sequences. Let the original video frame at time t
be denoted as It, and the enhanced frame after denoising and illumination correction is
given by
˜It = ψ(It), (3)
where ψ(·) denotes the video enhancement operator. As live-streaming sessions typically
last for extended durations and exhibit high redundancy across consecutive frames, a
key-frame selection strategy is further adopted to retain frames that are most discriminative
for behavioral changes. Key-frame selection is achieved by measuring inter-frame feature
differences, where the difference between adjacent frames is defined as
dt = |F(It) − F(It−1)|2, (4)
with F(·) denoting the visual feature extraction function. When dt exceeds a predefined
threshold δ, the corresponding frame is retained as a key frame. Through these procedures,
the video modality preserves essential behavioral information while significantly reducing
redundant noise, which is beneficial for subsequent cross-modal temporal alignment.
User behavior sequences constitute a critical data source for characterizing abnormal
marketing behaviors and can be viewed as multivariate time series containing events such
as likes, comments, tipping, and following. Given the strong randomness and burstiness
of user behaviors, directly using raw sequences may cause models to overemphasize
short-term fluctuations. Accordingly, smoothing and differencing operations are applied
to behavior sequences to highlight trend changes and abnormal bursts. Let the original
behavior sequence be denoted as xt, and its smoothed representation is defined as
¯xt = αxt + (1 − α) ¯xt−1, (5)
where α ∈ (0, 1) is the smoothing coefficient. To characterize behavior change rates, a
first-order difference is introduced as
∆xt = xt − xt−1. (6)
In addition, certain abnormal marketing behaviors exhibit clear periodic patterns, such
as concentrated traffic boosting within fixed time intervals. To capture such characteristics,
periodic pattern analysis is incorporated by mapping behavior sequences into the frequency
domain via the Fourier transform, whose spectral representation is given by
X( f ) =
T
∑
t=1
xte−j2π f t. (7)
https://doi.org/10.3390/electronics15040769

Electronics 2026, 15, 769 9 of 27
This transformation enables the identification of periodic anomalies hidden within
time-series data, allowing the model to detect not only instantaneous abnormalities but also
long-term and regular fraudulent behaviors. As genuine fraud samples typically account
for a very small proportion of the overall data, training models solely on original data
often leads to severe class imbalance and overfitting. To mitigate this issue, generative data
augmentation strategies are introduced to synthesize rare abnormal samples by learning
latent distributions of fraudulent behaviors. Within the generative adversarial network
framework, a generator G takes random noise z as input and outputs a synthetic sequence
ˆx, and its objective function can be expressed as
min
G
max
D
Ex∼pdata [log D(x)] +Ez∼p(z)[log(1 − D(G(z)))], (8)
where D denotes the discriminator. To further improve the temporal continuity and
distributional stability of generated sequences, diffusion models are additionally employed
to model abnormal behaviors. Diffusion models approximate real data distributions by
gradually injecting noise into data and learning the reverse denoising process. The forward
diffusion process can be formulated as
q(xt|xt−1) =N (
p
1 − βtxt−1, βtI), (9)
where βt denotes the noise scheduling parameter. By learning the reverse process
pθ(xt−1|xt), the model is capable of generating temporal segments that closely resemble
real fraudulent behaviors. Specifically, this generative capability is leveraged to synthesize
rare coordinated burst sequences, effectively alleviating the scarcity of organized attack
samples and enhancing model robustness against high-intensity manipulation. Through
the aforementioned multi-level preprocessing and augmentation strategies, textual, video,
and behavioral sequences are mapped into representation spaces with lower noise, clearer
semantics, and more balanced distributions prior to model input. This not only improves
the accuracy of cross-modal alignment but also substantially enhances the capability of the
model to identify covert fraud patterns under weak supervision, providing a solid data
foundation for subsequent temporal anomaly modeling and cooperative behavior detection
in MM-FGDNet.
3.3. Proposed Method
3.3.1. Overall
A unified end-to-end modeling pipeline is adopted in the proposed multimodal fraud
detection framework MM-FGDNet, where preprocessed and augmented multimodal tem-
poral data are jointly modeled to systematically characterize the generation and evolution
mechanisms of abnormal marketing behaviors from both temporal and group-structural
perspectives. The overall framework is initiated with cross-modal temporal semantic
alignment, through which feature representations derived from video, text, audio, and
user behavior sequences are projected into a unified temporal semantic space, thereby
eliminating discrepancies in sampling frequency, temporal granularity, and response la-
tency across different modalities. Specifically, features from each modality are first fed into
modality-specific encoders to obtain intra-modal temporal representations, which are then
flexibly mapped through a dynamic temporal alignment mechanism, enabling consistent
temporal correspondence of the same latent behavioral event across different modalities.
On this basis, a semantic attention fusion mechanism is employed to adaptively integrate
the aligned multimodal features, yielding a discriminative and temporally comparable
multimodal joint representation at each time step.
https://doi.org/10.3390/electronics15040769

Electronics 2026, 15, 769 10 of 27
After cross-modal alignment, the multimodal temporal representations are further
processed by the temporal anomaly modeling module for deep sequential analysis. By
leveraging self-attention structures, long-range dependencies among behavioral signals
over extended time spans are explicitly captured, allowing early weak signals and subse-
quent abnormal bursts to be jointly perceived. Through multi-scale modeling of behavioral
variations, both short-term abrupt anomalies and long-term covert fraud patterns emerg-
ing through gradual evolution can be effectively identified. The output of this module
consists of temporally continuous risk representations, which provide fine-grained tem-
poral characterization for downstream risk assessment. Meanwhile, user-level interaction
behaviors are abstracted into dynamic graph structures and are simultaneously fed into
the cooperative manipulation detection module. Graph neural networks are utilized to
model user interaction topologies, enabling the propagation and aggregation of individual
behavioral information within group structures and explicitly characterizing cooperative
relationships among multiple users. The group-level features learned from graph modeling
are jointly analyzed with the temporal risk representations produced by the temporal
anomaly modeling module in a high-level semantic space, so as to determine whether
detected anomalies originate from individual behavioral deviations or coordinated group
manipulation. Through subgraph-level anomaly identification and cross-modal consistency
verification, potential bot clusters or organized manipulation groups can be localized, and
their contributions to abnormal popularity formation can be interpreted. Finally, outputs
from the temporal anomaly modeling module and the cooperative manipulation detection
module are fused at the decision layer to jointly produce time-step-level fraud probabilities,
abnormal behavior category predictions, and comprehensive risk scores. Through this
bottom-up modeling process that progresses from temporal dynamics to group structures,
MM-FGDNet enables systematic identification of complex abnormal marketing behaviors
in live-streaming e-commerce scenarios and provides a unified and effective technical
framework for early risk warning and interpretable regulation.
3.3.2. Cross-Modal Temporal Alignment
The cross-modal temporal alignment module constitutes a core component of MM-
FGDNet, aiming to establish unified and comparable temporal semantic representations
across multimodal signals with heterogeneous temporal granularities, semantic response
delays, and noise characteristics, such that responses of the same latent marketing behavior
in video, text, audio, and transaction modalities can be consistently aligned along the
temporal axis. As shown in Figure 1, preprocessed multimodal features are first fed into
modality-specific encoders to obtain intra-modal temporal feature sequences. Lightweight
temporal encoding networks are employed for visual and audio modalities to preserve
continuous dynamic information, while text and transaction modalities are projected into
the same latent space dimension as other modalities via multilayer perceptrons, achieving
preliminary alignment at the feature dimension level. Let the encoded representation of
the m-th modality at time step t be denoted as h(m) t ∈ Rd, where d represents the unified
latent space dimension.
To address asynchronous responses across modalities along the temporal axis, a
dynamic temporal alignment mechanism is introduced to learn flexible temporal mappings
for modality-specific features. Instead of relying on fixed windows or hard alignment
strategies, this mechanism establishes soft associations between neighboring time steps via
learnable alignment weight functions, allowing the model to automatically capture realistic
behavioral response patterns, such as streamer actions preceding comment sentiment
changes or abnormal tipping lagging behind content stimulation. Through this process,
original modality-specific temporal sequences are remapped to a shared temporal index
https://doi.org/10.3390/electronics15040769

Electronics 2026, 15, 769 11 of 27
t′, yielding aligned feature representations ˜h(m) t′ and effectively eliminating structural
biases caused by sampling frequency differences and response delays. After temporal
alignment, a semantic attention fusion structure is further employed to jointly model
multimodal information. At each aligned time step t′, features from different modalities are
regarded as multi-view expressions of the same behavioral event, and modality weights are
dynamically assigned via attention mechanisms, such that modalities contributing more
to anomaly discrimination receive higher importance. This strategy not only avoids noise
amplification induced by naive feature concatenation but also enables adaptive modulation
of modality importance across different stages, for example, relying more on textual and
behavioral signals during early anomaly stages and emphasizing visual and transaction
modalities during abnormal bursts. The fused multimodal representation can be expressed
as zt′ = ∑m α(m) t′ ˜h(m) t′ , where α(m) t′ denotes the modality weight learned by the attention
function.
Data
Image
Video
Audio
Text
Transaction
MLP
MLP
Encoder Multimodal
features
+
+
+
+
+
Concat
 +
FFN+
MSAξ
Modality-specific Transformer
Training Only
Concat
 +
FFN+
MCA
ξ
Modality-fusionTransformer
Learnable
Fusion Token
+
Both Training and Inference
ξF
Alignment
Contrastive
Loss
Figure 1. Illustration of the cross-modal temporal alignment module.
To further enhance cross-modal semantic consistency, a cross-modal contrastive con-
straint is incorporated during training, encouraging multimodal representations corre-
sponding to the same temporal semantics to remain close in the latent space, while rep-
resentations from unrelated time steps or inconsistent behaviors are pushed apart. This
design explicitly suppresses modality drift induced by noise or incidental events and
strengthens the focus on genuine behavior-driven signals. From a mathematical perspec-
tive, this constraint effectively minimizes distances among modality representations at the
same t′ while maximizing discriminability across different time steps or samples, thereby
improving both the discriminative power and stability of aligned representations. Com-
bined with the shared fusion Transformer employed during both training and inference,
this module significantly enhances alignment quality and downstream anomaly detection
performance while maintaining inference efficiency. Overall, through the synergistic de-
sign of intra-modal encoding, flexible temporal alignment, semantic attention fusion, and
cross-modal consistency constraints, the cross-modal temporal alignment module effec-
tively addresses asynchronous responses, semantic misalignment, and noise interference
in multimodal live-streaming e-commerce data. As a result, highly consistent multimodal
input representations in both temporal and semantic dimensions are provided for subse-
quent temporal anomaly modeling, substantially improving the model’s sensitivity to weak
signals and covert abnormal marketing behaviors.
3.3.3. Temporal Fraud Pattern Modeling
The temporal fraud pattern modeling module takes the unified temporal semantic
representations produced by the cross-modal temporal alignment module as input. Let the
aligned sequence be denoted as X ∈ RT×d, where T represents the length of the aligned
https://doi.org/10.3390/electronics15040769

Electronics 2026, 15, 769 12 of 27
temporal sequence, which can be regarded as the temporal height, andd denotes the feature
width, which is set to 256 in the implemented configuration. To balance the requirements
of long live-streaming sequences and computational efficiency, a cross-modal semantic
compression strategy is first applied, in which highly redundant audio and video token
pools are jointly selected and merged with text and transaction tokens to form a compact
cross-modal temporal token sequence. The compressed length is denoted as K, which is
typically set to 128, ensuring that subsequent temporal modeling focuses on key segments
with higher information density. Subsequently, a hierarchical temporal Transformer encoder
is employed to model the evolution of abnormal behaviors, with the network depth set to
L = 6 layers. Each layer contains H = 8 attention heads, where the dimension of each head
is d/H = 32, and the feed-forward network dimension is set to d f f = 1024. A pre-norm
residual structure is adopted to stabilize training on long sequences. For the ℓ-th layer, the
attention computation is formulated as
Q(ℓ) = X(ℓ−1)W(ℓ) Q , K(ℓ) = X(ℓ−1)W(ℓ) K , V(ℓ) = X(ℓ−1)W(ℓ) V , (10)
Attn(ℓ)(X(ℓ−1)) =softmax

Q(ℓ)K(ℓ)⊤
√
d/H
+ M
!
V(ℓ), (11)
where M denotes a causal or local-window mask. A hybrid masking strategy that combines
local windows with a small number of global tokens is adopted, enabling the model
to stably capture short-term bursts while establishing long-range dependencies through
global tokens. To further enhance local–global pattern fusion, a lightweight temporal
convolution branch is introduced in parallel after each attention output to amplify local
abrupt variations. The convolution kernel size is set to k = 3, and dilation rates r ∈ {1, 2, 4}
are alternated across layers, allowing the effective receptive field to expand with depth.
The fused representation is expressed as
U(ℓ) = Attn(ℓ)(X(ℓ−1)) + ∑
r∈{1,2,4}
Convk,r

X(ℓ−1)

, (12)
followed by a feed-forward transformation
X(ℓ) = U(ℓ) + σ  U(ℓ)W(ℓ) 1  W(ℓ) 2 , (13)
where σ(·) denotes the gelu activation function. To improve sensitivity to weak signals
without excessive reliance on explicit labels, a set of implicit fraud pattern embeddings is
introduced as a learnable prototype set P = {p1, . . ., pM} ⊂Rd, with M = 16. Prototype
attention is used to map temporal representations to anomaly evidence strength:
at = max m≤M
exp(τ · ⟨xt, pm⟩)
∑M j=1 exp  τ · ⟨xt, pj⟩  , (14)
where xt denotes the final-layer representation at time step t, and τ is a temperature pa-
rameter. This design allows stable amplification of weak signals when fraud patterns
form clusters in the latent space. Specifically, the optimization of τ is critical for balancing
sensitivity and precision; by tuning τ to sharpen the attention distribution only when pro-
totype similarity exceeds a confidence margin, the mechanism acts as a soft-thresholding
filter. This ensures that genuine weak signals aligning with learned prototypes are am-
plified, while random noise with low similarity scores is suppressed, thereby preventing
non-specific fluctuations from elevating the false alarm rate. Furthermore, to enable inter-
https://doi.org/10.3390/electronics15040769

Electronics 2026, 15, 769 13 of 27
pretable detection of abrupt anomalies, a temporal variation energy is defined by jointly
considering adjacent state differences and prototype evidence:
et = ∥xt − xt−1∥2 2 + λat, (15)
which is used to produce time-step-level risk logits ℓt = w⊤xt + b + ηet, and the final
fraud probability is obtained as ˆyt = σ(ℓt). A key advantage of combining this module
with the cross-modal temporal alignment module lies in the fact that aligned multimodal
responses are mapped into a shared temporal semantic space, such that evidence of the
same latent event forms consistent correlation structures within X. Consequently, the
attention matrix QK⊤ becomes more block- or band-separable, reducing attention noise
caused by semantic misalignment. Formally, if alignment errors randomly mismatch a
proportion ϵ of truly correlated pairs, the expected signal-to-noise ratio of attention scores
satisfies E[∆] ≥ (1 − ϵ)∆0 − ϵ∆1, where ∆0 denotes the average margin of correctly matched
pairs and ∆1 represents an upper bound on mismatched margins, implying that reducing ϵ
linearly improves separability and weak-signal detection, as shown in Figure 2.
S0 S1 S2 S3 S4 S5 S6 S7 S8 S9 S10 S11
Cross-Modal Semantic
Combined
Audio/Video Pool
Top-K Selection
Vision Encoder Audio Encoder Tokenizer
Feed Forward
LayerNorm
Attention
LayerNorm
Cross-Modal Encoder
Video tokens Audio tokens
Text tokens Transaction
tokens
Image tokens
Figure 2. This figure illustrates the architecture and information flow of the temporal fraud pattern
modeling module.
Finally, the necessity of local–global fusion can be explained by the fact that when only
local convolutions are used, the effective receptive field of a network with depth L is at
most 1 + 2 ∑L ℓ=1 rℓ, which is insufficient for long live-streaming sequences. By introducing
global attention, any time step t can establish a one-hop dependency with any other step
s, reducing the upper bound of influence path length from O(T) to O(1), which can be
characterized as
∀t, s, ∂x(ℓ) t
∂x(ℓ−1) s ̸= 0 may hold through attention. (16)
This ensures that early weak signals can influence subsequent decisions across long
time spans, while the convolution branch remains sensitive to high-frequency components
of abrupt spikes. Their complementarity enables both early trend recognition and instanta-
neous burst capture, which is consistent with the progressive evolution and sudden ampli-
fication characteristics of abnormal marketing behaviors in live-streaming e-commerce.
3.3.4. Cooperative Manipulation Detection
The cooperative manipulation detection module takes the user interaction graph as its
core input and explicitly models the organizational structures of coordinated manipulation,
such as bot clusters and paid commentator groups, which constitute a key fraud mechanism
in live-streaming e-commerce. This module forms a complementary closed loop with the
cross-modal temporal alignment and temporal fraud pattern modeling modules. As shown
in Figure 3, within a live-streaming time window of length T, a dynamic graph G = (V, E)
https://doi.org/10.3390/electronics15040769

Electronics 2026, 15, 769 14 of 27
is constructed, where |V| = N denotes the number of user nodes, which can be regarded
as the graph height, and each edge eij ∈ E represents an interaction between users i and
j within the window, such as comment replies, co-tipping to the same streamer, mutual
mentions, or short-term synchronized likes. Edge weights are determined by interaction
intensity and temporal proximity. The initial representation of each node is composed of
multi-source behavioral statistics and aligned content evidence, denoted as h(0) i ∈ Rdg,
where dg = 256 is the graph feature width. To inject cross-modal consistency evidence,
the time-step-level risk sequence output by the temporal anomaly module is aggregated
along user events to obtain a user-level risk summary ri ∈ R64, which is concatenated
with structural features and linearly projected before entering the graph network, enabling
graph representations to simultaneously encode individual temporal anomalies and group
structural relations.
hp hn gp,n
GraphConnection
a∈𝑅!!"#×!"$%
𝑆𝑜𝑓𝑡𝑚𝑎𝑥	(𝑟𝑜𝑤−𝑤𝑖𝑠𝑒)
Weight Matrix
Hit Views Vhit
W1,1=0.67 W1,2=0.33
Weight Prediction Cooperative ManipulationDetection
W1,4W1,3W1,2W1,1
W2,4W2,3W2,2W2,1
W3,4W3,3W3,2W3,1
Wp,4Wp,iWp,2Wp,1
Q1
Q2
Q3
Qp
…
…
User Nodes Un
g1,1 g1,2 g1,3 g1,4
g#,%=[𝑝𝑜𝑠,ℎ𝑒𝑖𝑔ℎ𝑡,𝑑𝑖𝑠𝑡,𝑎𝑛𝑔𝑙𝑒𝑠]
Graph Construction
Figure 3. This figure depicts the overall pipeline and structural design of the cooperative manipulation
detection module.
The graph encoder adopts a Lg = 3-layer graph attention network to enhance the
representation of heterogeneous relations and cooperative behaviors. The output channel
dimensions are set to 256 → 256 → 128, with the number of attention heads Hg = 4 and
each head having a dimension of 64. For the ℓ-th layer, message passing is formulated as
e(ℓ) ij = LeakyReLU  a(ℓ)⊤ W(ℓ)h(ℓ−1) i ∥ W(ℓ)h(ℓ−1) j ∥ gij  , (17)
where gij denotes the edge attribute vector, including time difference, interaction type
distribution, and shared targets, which is linearly projected to aligned dimensions. Row-
wise softmax normalization is applied to obtain interpretable neighbor contribution weights
α(ℓ) ij = exp(e(ℓ) ij ) ∑k∈N (i) exp(e(ℓ) ik ) , (18)
and node updates are performed as
h(ℓ) i = σ

 ∑
j∈N (i)
α(ℓ) ij W(ℓ)h(ℓ−1) j

, (19)
which is consistent with the “GAT–row-wise softmax–weight matrix” pipeline illustrated
in the architecture, allowing higher attention weights to be assigned to the most likely
cooperative accomplices and highlighting strong intra-group connections. For subgraph-
https://doi.org/10.3390/electronics15040769

Electronics 2026, 15, 769 15 of 27
level anomaly detection, a learnable set of group prototypes C = {c1, . . ., cK} ⊂R128 is
introduced, with K = 8, and soft clustering is used to compute node memberships to each
prototype:
πik =
exp

κ · h(Lg)⊤ i ck 
∑K u=1 exp  κ · h(Lg)⊤ i cu  . (20)
Based on this, subgraph risk is defined as a joint function of prototype consistency
and edge-level cooperation strength:
ssub =
K
∑
k=1
 ∑ i∈V πikh(Lg) i − µk  2 2 + ρ ∑ (i,j)∈E K ∑ k=1 πik πjkwij, (21)
where µk denotes the running mean of the k-th prototype center and wij is the edge
weight. The second term mathematically encourages nodes connected by high-strength
edges to achieve higher consistency under the same prototype, which corresponds to the
organizational characteristics of coordinated manipulation. In this context, the coefficient ρ
serves as a regularization parameter that calibrates the trade-off between feature consistency
and structural density. Optimizing ρ ensures that high interaction density alone—which
may appear in legitimate fan communities—does not dominate the risk score. Instead,
it enforces a dual constraint where subgraphs are only flagged if they simultaneously
exhibit tight coordination and alignment with fraud prototypes, effectively amplifying
covert organized signals without misclassifying benign group activities. For cross-modal
consistency verification, user embeddings from content and behavior perspectives, denoted
as uc i and ub i , are constructed using aligned temporal semantics, and their discrepancy is
used as evidence of pseudo-cooperation:
∆i = 1 − uc⊤ i ub i ∥uc i ∥2∥ub i ∥2 . (22)
When a large number of nodes simultaneously exhibit low content diversity but
high behavioral synchrony, both ∆i and ssub increase, facilitating the localization of bot
clusters. The advantage of combining this module with the temporal anomaly modeling
module lies in the complementary nature of evidence: the temporal module provides fine-
grained information about when anomalies occur, while the graph module identifies who is
cooperating. These signals are fused at the decision layer via learnable gating, yielding the
final risk score ˆy = σ(θ1 ¯p + θ2ssub + θ3 ¯∆), where ¯p denotes aggregated temporal risk and
¯∆ denotes aggregated consistency discrepancy. It can be shown that when intra-group edge
weights wij increase and group members become more concentrated in the prototype space,
ssub increases monotonically, that is, ∂ssub/∂wij ≥ 0, indicating that this metric provides
an interpretable response to cooperation strength. Meanwhile, ∆i is scale-invariant due to
cosine discrepancy, allowing stable discrimination across different streamers and product
categories, thereby significantly improving cross-scenario generalization and detection of
covert cooperative fraud.
4. Results and Discussion
4.1. Experimental Configuration
4.1.1. Hardware and Software Platform
All experiments were conducted on a unified high-performance computing platform
to ensure stability and reproducibility during model training and evaluation. In terms
of hardware configuration, the experimental server was equipped with multi-core high-
https://doi.org/10.3390/electronics15040769

Electronics 2026, 15, 769 16 of 27
performance CPUs and large-capacity memory to support parallel loading and preprocess-
ing of large-scale multimodal data, and was further accelerated by high-performance GPUs
for deep learning model training and inference. The GPU memory capacity was sufficient
to accommodate simultaneous multimodal feature inputs and long-sequence modeling,
thereby effectively avoiding gradient truncation or batch size reduction caused by memory
limitations. A high-speed solid-state drive storage system was adopted to ensure efficient
read and write operations for video frames, textual logs, and user behavior sequences,
which collectively improved experimental efficiency and overall system throughput. Re-
garding the software environment, the experimental platform was built upon mainstream
deep learning frameworks and deployed on a 64-bit Linux distribution to ensure robust
support for GPU drivers and parallel computing libraries. Model implementation was
completed using mature deep learning frameworks with automatic differentiation and
distributed training mechanisms to enhance training stability. Common numerical compu-
tation and data analysis libraries were employed in multimodal data processing to support
text processing, video decoding, feature extraction, and graph structure construction. In
addition, random seeds were consistently controlled across experiments to reduce stochas-
tic variation between different runs and to ensure strong reproducibility of experimental
results.
To strictly prevent future information leakage and simulate real-world streaming
scenarios, the dataset was partitioned chronologically. Specifically, the first 70% of the
timeline was designated for training, the subsequent 10% for validation, and the final
20% for testing. The training set was used for model parameter learning, the validation
set for hyperparameter tuning and model selection, and the test set exclusively for final
performance evaluation. To further enhance the reliability of experimental results, a five-
fold cross-validation strategy was adopted on the entire dataset. Specifically, the dataset
was divided into five mutually exclusive subsets, with one subset used as the test set
in each experimental round and the remaining subsets used for training and validation.
Final results were reported as the average performance over the five runs. During model
training, an adaptive gradient-based optimization strategy was employed, with the initial
learning rate set to α and gradually decayed according to a predefined schedule to balance
convergence speed and training stability. The batch size was determined based on GPU
memory capacity and model complexity to ensure stable gradient estimation. The hidden
dimensions and numbers of attention heads in temporal models were tuned using the vali-
dation set to achieve an appropriate trade-off between performance and computational cost.
Regularization weights and dropout probabilities were introduced to mitigate overfitting,
and their values were determined through comparative experiments. All hyperparameters
were kept consistent across cross-validation folds to ensure comparability of results.
4.1.2. Baseline Models and Evaluation Metrics
A diverse set of representative models was selected as baseline methods for compari-
son, including LSTM/GRU-based temporal models [58,59], transformer-based temporal
models without multimodal fusion [60], graph neural network based fraud detection mod-
els [61], multimodal fusion models such as MMBT and CLIP-style fusion approaches [62,63],
as well as commercial or publicly available anomaly detection models including isolation
forest and one-class svm [64,65]. LSTM and GRU model user behavior sequences through
gated recurrent mechanisms and are effective at capturing short-term temporal dependen-
cies, benefiting from mature architectures and stable training behavior. Transformer-based
temporal models rely on self-attention mechanisms to model global temporal dependencies
and exhibit advantages in capturing long-range behavioral patterns. GNN-based fraud
detection methods propagate node information over user interaction graphs to identify
https://doi.org/10.3390/electronics15040769

Electronics 2026, 15, 769 17 of 27
abnormal structures, demonstrating strong expressive power for detecting coordinated
group behaviors. MMBT and CLIP-style fusion models jointly model textual and visual
features to enhance cross-modal semantic alignment by leveraging complementary multi-
modal information. Isolation forest and one-class svm identify deviations by modeling the
distribution of normal samples, requiring no large-scale labeled data and offering simple
implementation, which makes them suitable as unsupervised baseline methods.
For experimental evaluation, a comprehensive set of metrics was adopted to assess
discriminative capability, stability, and practical applicability in live-streaming e-commerce
fraud detection tasks. These metrics include auc, precision, recall, and f1 for overall classifi-
cation performance; fraud detection rate (fdr) and false alarm rate (far) for characterizing
risk identification effectiveness; and early detection score and cross-domain generalization
score to reflect the capability of capturing early weak signals and generalizing across differ-
ent scenarios. The mathematical definitions of the evaluation metrics are provided below,
where the binary confusion matrix consists of true positives, false positives, true negatives,
and false negatives:
Precision = TP TP + FP , Recall = TP TP + FN , F1 = 2 · Precision · Recall Precision + Recall , (23)
AUC =
Z 1
0
TPR(FPR) dFPR, (24)
FDR = TP TP + FN , FAR = FP FP + TN , (25)
EDS = 1 N N ∑ i=1 exp  −γ · (tdet i − t f raud i )  , (26)
CDGS = F1target
F1source
, (27)
where TP denotes the number of correctly identified fraud samples,FP denotes the number
of normal samples incorrectly classified as fraud, TN denotes the number of correctly
identified normal samples, and FN denotes the number of missed fraud samples. TPR
and FPR represent the true positive rate and false positive rate, respectively. N denotes
the total number of test samples. t f raud i and tdet i indicate the true occurrence time of the
i-th fraud event and the first detection time predicted by the model, respectively. γ is
the temporal penalty coefficient. F1source and F1target represent the f1 scores achieved by
the model on the source domain and target domain, respectively. These metrics reflect
model performance from multiple perspectives. Specifically, auc and f1 measure overall
discriminative capability, precision and recall focus on false alarm control and missed de-
tection risk, fdr and far directly correspond to fraud identification accuracy and false alarm
rates in practical business scenarios, early detection score emphasizes sensitivity to early
weak fraud signals, and cross-domain generalization score evaluates the transferability and
generalization capability across platforms, streamers, and product categories.
4.2. Overall Performance Comparison with Baseline Methods
The objective of this experiment is to systematically evaluate, from an overall perspec-
tive, the comprehensive discriminative capability, risk recognition stability, and practical
applicability of different categories of methods in the task of abnormal marketing de-
tection in live-streaming e-commerce. By introducing representative baselines covering
unsupervised methods, traditional temporal models, deep temporal models, graph-based
models, and multimodal fusion models, the applicability boundaries of different modeling
https://doi.org/10.3390/electronics15040769

Electronics 2026, 15, 769 18 of 27
assumptions and mathematical structures in complex marketing scenarios are thoroughly
examined.
As reported in Table 2, unsupervised methods based on distributional assumptions,
including Isolation Forest and One-Class SVM, exhibit relatively inferior performance
in terms of AUC and F1. This behavior can be attributed to the fact that such methods
primarily rely on modeling a global normal distribution and identifying isolated devia-
tions, whereas abnormal marketing behaviors in live-streaming scenarios often emerge
gradually through weak signals and coordinated patterns, making them difficult to appear
as isolated outliers in the feature space. As the modeling paradigm shifts from unsuper-
vised distribution modeling to temporal modeling, LSTM and GRU achieve noticeable
improvements in Recall, F1, and EDS, indicating that incorporating temporal dependency
structures facilitates the capture of user behavior evolution. However, due to their reliance
on limited-length hidden state propagation, recurrent models still suffer from gradient
attenuation and constrained memory when handling long time spans and abrupt anomalies,
which restricts their gains in AUC, EDS, and CDGS.
Table 2. Overall performance comparison with baseline methods.
Method AUC ↑ Precision ↑ Recall ↑ F1 ↑ FDR ↑ FAR ↓ EDS ↑ CDGS ↑
Isolation Forest 0.781 0.702 0.648 0.674 0.648 0.142 0.412 0.681
One-Class SVM 0.793 0.718 0.662 0.689 0.662 0.136 0.438 0.695
LSTM 0.834 0.756 0.721 0.738 0.721 0.121 0.502 0.734
GRU 0.842 0.764 0.728 0.746 0.728 0.118 0.517 0.742
Transformer (temporal) 0.867 0.791 0.756 0.773 0.756 0.106 0.561 0.771
GNN-based Fraud Detection 0.872 0.798 0.761 0.779 0.761 0.103 0.548 0.786
MMBT 0.883 0.812 0.774 0.793 0.774 0.097 0.584 0.801
CLIP-style Fusion 0.889 0.819 0.781 0.800 0.781 0.094 0.601 0.812
MM-FGDNet (Ours) 0.927 0.861 0.834 0.847 0.834 0.071 0.689 0.872
As shown in Figure 4, temporal Transformer models based on self-attention further
enhance long-range dependency modeling and outperform recurrent models in AUC,
F1, and EDS, highlighting the advantage of global temporal modeling for identifying
abnormal trends. After introducing user relationship information at the structural level,
GNN-based methods achieve further improvements in F1 and CDGS, demonstrating that
group-structure modeling effectively captures user coordination in organized fraud behav-
iors. Nevertheless, these methods heavily depend on graph construction quality and make
limited use of content modalities and temporal semantics, resulting in a performance bot-
tleneck in early detection as reflected by EDS. Multimodal fusion models, including MMBT
and CLIP-style fusion, further improve Precision, F1, and AUC by jointly modeling visual
and textual features, confirming that cross-modal semantic complementarity alleviates the
limitations of single-modality representations. However, such approaches often rely on
static or weakly temporal fusion strategies and do not explicitly model temporal alignment
and behavioral evolution across modalities, leaving room for improvement in FAR control
and early risk perception. In contrast, MM-FGDNet consistently achieves superior per-
formance across all evaluation metrics, with particularly pronounced advantages in F1,
EDS, and CDGS. These gains stem from the systematic architectural design of the proposed
framework. Cross-modal temporal alignment mitigates noise amplification caused by
semantic misalignment, deep temporal modeling captures the progressive evolution from
weak signals to abnormal bursts, and cooperative behavior modeling explicitly charac-
terizes organized multi-user manipulation. By jointly constraining temporal, semantic,
and structural dimensions, the proposed framework maintains a stable decision boundary
under complex distributions and cross-scenario shifts, thereby significantly outperforming
https://doi.org/10.3390/electronics15040769

Electronics 2026, 15, 769 19 of 27
existing baselines in overall performance, early detection capability, and cross-domain
generalization.
,VRODWLRQ)RUHVW 2QH&ODVV690
/670 *58
7UDQVIRUPHU *11)UDXG
00%7
&/,3)XVLRQ
00)*'1HW2XUV









$8&6FRUH
Figure 4. Overall performance comparison with baseline methods.
4.3. Ablation Study of Different Components in MM-FGDNet
The ablation study is designed to systematically evaluate the individual contributions
and collaborative effects of the core components in MM-FGDNet with respect to overall
performance, early risk detection, and cross-scenario generalization. By removing the cross-
modal temporal alignment module, the temporal fraud modeling module, the cooperative
manipulation detection module, and the diffusion-based augmentation strategy one at
a time while keeping the remaining architecture unchanged, the influence of different
modeling assumptions on the decision boundary and risk perception capability can be
directly analyzed.
As shown in Table 3, the full model consistently achieves the best performance across
all metrics, indicating that the proposed components are not merely additive but form
complementary constraints at both the mathematical structure and information flow levels.
When the cross-modal alignment module is removed, both AUC and F1 decrease substan-
tially, accompanied by a significant increase in FAR. This suggests that misalignment across
modalities in temporal and semantic dimensions amplifies noise in the discriminative
space, making non-fraudulent behaviors more likely to be misclassified as anomalies. This
observation underscores the critical role of cross-modal alignment in reducing feature
distribution shifts and stabilizing joint representations. When the temporal fraud modeling
module is excluded, the EDS metric exhibits the most pronounced degradation, demon-
strating a severe loss in sensitivity to early weak signals and validating the importance of
explicitly modeling behavioral evolution for capturing the onset of fraudulent activities.
Table 3. Ablation study of different components in MM-FGDNet.
Variant AUC ↑ F1 ↑ FDR ↑ FAR ↓ EDS ↑ CDGS ↑
Full MM-FGDNet 0.927 0.847 0.834 0.071 0.689 0.872
w/o Cross-Modal Alignment 0.898 0.812 0.798 0.089 0.602 0.821
w/o Temporal Fraud Modeling 0.883 0.799 0.782 0.093 0.531 0.814
w/o Cooperative Detection 0.892 0.807 0.791 0.086 0.578 0.793
w/o Diffusion Augmentation 0.901 0.818 0.804 0.082 0.614 0.839
From the perspective of model structure, the performance variations observed across
different ablation settings can be reasonably explained by their underlying mathematical
https://doi.org/10.3390/electronics15040769

Electronics 2026, 15, 769 20 of 27
modeling capacities. As shown in Figure 5, without temporal fraud modeling, the repre-
sentation of the temporal dimension degenerates into near-static discrimination, causing
the decision boundary to rely primarily on local feature distributions and limiting the accu-
mulation of anomaly evidence across time steps. The removal of the cooperative detection
module leads to a notable decline in CDGS indicating reduced generalization ability across
streamers and platforms. This substantial performance gap can be attributed to the loss of
high-order structural constraints among users; without these invariant topological patterns,
the model is forced to rely more heavily on superficial platform- or individual-specific
features rather than stable cooperative patterns. Although excluding diffusion-based aug-
mentation results in relatively smaller performance drops, consistent declines in F1, EDS,
and CDGS are still observed, suggesting that generative augmentation plays an important
regularization role in smoothing the decision boundary and improving representation cov-
erage under class imbalance and weak supervision. Overall, the ablation results validate
the rationality of the MM-FGDNet design from both mathematical modeling capability and
information constraint perspectives, demonstrating that cross-modal alignment reduces
representation noise, temporal modeling accumulates anomaly evidence, and structural
modeling constrains cooperative behaviors, collectively enabling stable, generalizable, and
early-warning-capable fraud detection in complex marketing environments.
AUC
F1
FDR
FAR
EDS
CDGS
0.2
0.4
0.6
0.8
1.0
Full MM-FGDNet
w/o Cross-Modal Alignment
w/o T emporal Fraud Modeling
w/o Cooperative Detection
w/o Diffusion Augmentation
Figure 5. Radar chart illustrating the comprehensive ablation study results, comparing the full
MM-FGDNet framework against four variants with specific core components removed. The axes
represent six key evaluation metrics: AUC, F1-Score, Fraud Detection Rate (FDR), False Alarm Rate
(FAR, plotted inversely where outward indicates lower FAR), Early Detection Score (EDS), and
Cross-Domain Generalization Score (CDGS).
https://doi.org/10.3390/electronics15040769

Electronics 2026, 15, 769 21 of 27
4.4. Cross-Domain Generalization Performance Under Different Target Scenarios
The purpose of the cross-domain generalization experiment is to systematically evalu-
ate the stability and transferability of different models under significant distribution shifts,
thereby verifying whether abnormal marketing behaviors are captured at the mechanism
level rather than relying on superficial characteristics such as streamer style, product at-
tributes, or platform-specific rules. By constructing three target scenarios, namely a new
streamer, a new product category, and a new platform, robustness is examined under
conditions involving changes in content entities, variations in business semantics, and
shifts in system environments.
As shown in Table 4, the overall performance of all models declines under cross-
domain conditions compared with in-domain settings, although the magnitude of degrada-
tion varies substantially. The temporal transformer-based model exhibits relatively stable
yet limited generalization across all scenarios, with the most pronounced drops in F1 and
AUC observed in the new platform setting, indicating that reliance on temporal depen-
dency modeling alone remains sensitive to platform-level distributional shifts. Multimodal
fusion models achieve moderate improvements in the new streamer and new product
scenarios by incorporating visual and textual information; however, the gains remain lim-
ited under the new platform condition, suggesting that static semantic fusion encounters
adaptation bottlenecks when migrating across system environments. GNN-based methods
consistently outperform the former two categories across all scenarios, particularly in
terms of F1 and AUC, demonstrating that group-structure information exhibits stronger
cross-domain stability. Nevertheless, the relatively limited improvement in EDS indicates
that such methods remain insufficiently sensitive to the early stages of abnormal behavior.
Table 4. Cross-domain generalization performance under different target scenarios.
Target Scenario Method F1 ↑ AUC ↑ EDS ↑
New Streamer
Transformer (temporal) 0.742 0.851 0.512
Multimodal Fusion (MMBT) 0.769 0.873 0.548
GNN-based Fraud Detection 0.779 0.881 0.536
MM-FGDNet 0.816 0.914 0.662
New Product Category
Transformer (temporal) 0.736 0.846 0.498
Multimodal Fusion (MMBT) 0.761 0.869 0.531
GNN-based Fraud Detection 0.771 0.878 0.519
MM-FGDNet 0.808 0.909 0.643
New Platform
Transformer (temporal) 0.721 0.832 0.471
Multimodal Fusion (MMBT) 0.747 0.861 0.503
GNN-based Fraud Detection 0.756 0.871 0.491
MM-FGDNet 0.801 0.902 0.628
As shown in Figure 6, the attention weights learned by temporal transformer models
are optimized under source-domain distributions; when streamer pacing, product conver-
sion dynamics, or platform interaction rules change, the learned temporal dependency
patterns become misaligned, resulting in decision boundary drift. Although multimodal
fusion models mitigate single-modality bias by introducing additional semantic views, the
absence of explicit temporal alignment and cross-modal consistency constraints allows
domain-specific noise to interfere with fused representations. GNN-based models bene-
fit from user collaboration structures learned through graph propagation, which remain
relatively invariant across scenarios, thereby enabling improved structural generalization.
However, the de-emphasis on temporal evolution limits their ability to detect early weak
signals. In contrast, MM-FGDNet consistently achieves superior performance across all
https://doi.org/10.3390/electronics15040769

Electronics 2026, 15, 769 22 of 27
three scenarios, with particularly notable advantages in EDS, indicating that abnormal
behavior evolution can still be perceived at an early stage under distribution shifts. This
robustness arises from the joint constraint mechanism embedded in the model architecture:
cross-modal temporal alignment mitigates semantic drift across domains, temporal fraud
modeling accumulates evolution evidence independent of specific domains, and cooper-
ative manipulation detection introduces group-level structural priors as stable anchors.
Consequently, the model maintains focus on the core generative mechanisms of abnormal
marketing behaviors when facing changes in streamers, products, or platforms, thereby
exhibiting stronger generalization capability and practical value.
1HZ6WUHDPHU 1HZ3URGXFW&DWHJRU\ 1HZ3ODWIRUP







 










)6FRUH3HUIRUPDQFH
1HZ6WUHDPHU 1HZ3URGXFW&DWHJRU\ 1HZ3ODWIRUP







 

 

 

 

$8&3HUIRUPDQFH
1HZ6WUHDPHU 1HZ3URGXFW&DWHJRU\ 1HZ3ODWIRUP



















('63HUIRUPDQFH
&URVVGRPDLQ*HQHUDOL]DWLRQ3HUIRUPDQFH$QDO\VLV
7UDQVIRUPHUWHPSRUDO

 0XOWLPRGDO)XVLRQ00%7

 *11EDVHG)UDXG'HWHFWLRQ 00)*'1HW
Figure 6. Cross-domain generalization performance under different target scenarios.
4.5. Discussion
The performance advantages demonstrated by MM-FGDNet across multiple exper-
iments carry clear and concrete practical implications, particularly in real-world live-
streaming e-commerce environments characterized by high dynamics and strong interac-
tivity. In operational settings, abnormal marketing behaviors rarely manifest as abrupt
and explicit violations; instead, risk often accumulates gradually through subtle changes
in streamer behavior, comment sentiment, and user interaction rhythms. For instance,
certain live-streaming sessions may appear compliant in terms of content and presentation,
while the comment section suddenly exhibits highly homogeneous emotional expressions
accompanied by unusually concentrated tipping activity. Such patterns are easily over-
looked by manual inspection or rule-based systems. By performing cross-modal temporal
alignment, MM-FGDNet maps content variations, emotional fluctuations, and transactional
behaviors into a unified temporal semantic space, enabling systematic detection of these
seemingly normal yet intrinsically abnormal early signals and providing platforms with
more proactive risk warning capabilities. From the perspective of platform governance,
the explicit modeling of cooperative behaviors offers interpretable evidence for identifying
organized water-army groups and bot clusters. In practice, platforms frequently encounter
scenarios in which individual user actions remain compliant while collective outcomes are
anomalous, such as multiple newly registered accounts simultaneously tipping, liking, and
commenting on the same product. While each individual action may appear legitimate,
the overall interaction rhythm deviates significantly from that of normal user populations.
Traditional models based on user profiling or point-wise anomaly detection struggle to
address such cases. By modeling interaction structures and cooperative patterns among
users, MM-FGDNet identifies consistency in timing, interaction targets, and emotional
expression at the group level, revealing how abnormal popularity is orchestrated and am-
plified. This capability not only reduces the risk of mistakenly penalizing legitimate users
but also provides actionable and interpretable insights to support fine-grained governance
strategies.
Furthermore, the stable performance observed in cross-domain experiments highlights
the strong deployment potential of the proposed framework across multiple platforms
https://doi.org/10.3390/electronics15040769

Electronics 2026, 15, 769 23 of 27
and product categories. In real business environments, platform rules, streamer profiles,
and product structures evolve continuously, and models trained on historical data or sin-
gle scenarios often require frequent retraining to maintain effectiveness. By modeling
the generative mechanisms of abnormal marketing behaviors rather than memorizing
platform-specific features, MM-FGDNet preserves detection capability when confronted
with new streamers, new products, or even entirely new platforms. This property en-
ables the framework to function as a core component of platform-level risk monitoring
systems, supporting human review processes, optimizing recommendation strategies, and
enhancing regulatory efficiency while safeguarding user experience and ecosystem fairness.
Regarding system implementation and deployment, MM-FGDNet is designed to op-
erate within a high-concurrency stream processing architecture suitable for large-scale
platforms. To balance detection accuracy with real-time response requirements, a hierar-
chical deployment strategy is recommended. In this setup, lightweight rule-based filters
serve as the first line of defense to screen out obvious traffic anomalies, while MM-FGDNet
functions as the core deep analysis engine for processing complex, ambiguous interaction
sequences. By leveraging distributed inference frameworks (e.g., TensorRT on GPU clus-
ters) and asynchronous message queues, the model can process multimodal data streams
with second-level latency, ensuring that risk warnings are generated before significant
ecosystem damage occurs. Additionally, the interpretable subgraphs generated by the
cooperative detection module can be directly integrated into human-in-the-loop review
workstations, visualizing the core members of fraud syndicates to assist moderators in
making rapid, evidence-based decisions.
4.6. Limitation and Future Work
Although MM-FGDNet achieves substantial performance improvements in abnormal
marketing detection for live-streaming e-commerce, several aspects remain open for further
investigation. First, the joint modeling of multimodal signals and group-level structures
enhances representational capacity but also incurs increased computational and storage
overhead, which may pose challenges in ultra-large-scale platforms or latency-sensitive
scenarios where careful trade-offs between accuracy and efficiency are required. Second,
the cooperative manipulation detection module relies on the availability and quality of
user interaction graphs; when interaction data are sparse or user relationships are par-
tially unobservable due to platform constraints, detection effectiveness may be affected.
Moreover, while cross-domain experiments demonstrate strong generalization, the model
still primarily transfers knowledge from historical patterns when encountering extreme
cold-start scenarios or entirely novel marketing mechanisms, which may lead to delayed
responses. Future research may extend the framework along several directions. More
lightweight cross-modal alignment and graph modeling strategies could be explored, po-
tentially in combination with model compression or online learning techniques, to improve
deployability in large-scale real-time environments. In addition, incorporating stronger
causal modeling or active learning mechanisms may reduce reliance on historical fraud
patterns and enhance adaptability to emerging abnormal behaviors. Finally, tighter integra-
tion between model outputs, platform governance rules, and human review workflows
may facilitate the construction of human-in-the-loop risk identification and intervention
systems, promoting sustained and effective real-world deployment.
5. Conclusions
A data-driven multimodal abnormal behavior detection framework, termed MM-
FGDNet, has been presented to address the growing concealment, coordination, and
cross-modal heterogeneity of abnormal marketing behaviors in live-streaming e-commerce
https://doi.org/10.3390/electronics15040769

Electronics 2026, 15, 769 24 of 27
and digital marketing environments. By systematically modeling abnormal behavior
mechanisms from the complementary perspectives of temporal evolution and group-level
coordination, the proposed framework overcomes the limitations of rule-based or static-
feature-driven approaches that are increasingly inadequate for large-scale platform gover-
nance and early risk warning. MM-FGDNet integrates cross-modal temporal alignment,
temporal fraud pattern modeling, and cooperative manipulation detection into a unified
architecture, enabling robust aggregation of weak signals across time and explicit character-
ization of organized group behaviors. Crucially, the framework incorporates interpretable
abnormal subgraph analysis within the cooperative behavior detection module. By visu-
alizing high-order interaction structures and pinpointing the core members of organized
groups—such as bot clusters and paid poster networks—this mechanism provides granular,
intuitive evidence that empowers human reviewers to rapidly validate algorithmic alerts,
thereby significantly accelerating evidence-based decision-making in platform governance
workflows. Extensive experiments on real-world multi-platform datasets demonstrate
that MM-FGDNet consistently outperforms representative baseline methods, achieving
an AUC of 0.927 and an F1 score of 0.847, with precision and recall reaching 0.861 and
0.834, respectively, while significantly reducing false alarm rates. Moreover, the proposed
framework attains an Early Detection Score of 0.689, indicating a superior capability to
identify abnormal behaviors at their incipient stages. Ablation and cross-domain general-
ization studies further confirm the robustness and transferability of the proposed design
across new streamers, new product categories, and new platforms. Overall, MM-FGDNet
provides an effective, scalable, and practically deployable data-driven artificial intelligence
solution for high-accuracy abnormal behavior detection and intelligent risk governance in
live-streaming platforms.
Author Contributions: Conceptualization, J.L. (Jingwen Luo), P .Z., Y.W. and Y.Z.; Data curation, J.L.
(Jingqi Li) and X.K.; Formal analysis, Z.X.; Funding acquisition, Y.Z.; Investigation, Z.X.; Methodology,
J.L. (Jingwen Luo), P .Z. and Y.W.; Project administration, Y.Z.; Resources, J.L. (Jingqi Li) and X.K.;
Software, J.L. (Jingwen Luo), P .Z. and Y.W.; Supervision, Y.Z.; Validation, Z.X.; Visualization, J.L.
(Jingqi Li) and X.K.; Writing—original draft, J.L. (Jingwen Luo), P .Z., Y.W., Z.X., J.L. (Jingqi Li), X.K.
and Y.Z.; J.L. (Jingwen Luo), P .Z., and Y.W. contributed equally to this work. All authors have read
and agreed to the published version of the manuscript
Data Availability Statement: The data presented in this study are available on request from the
corresponding author.
Conflicts of Interest: The authors declare no conflict of interest.
References
1. Rachmad, Y.E. The Evolution Of Seller Behavior: From Traditional Markets To Live Streaming ; YER E-Book Publication: Jakarta,
Indonesia, 2024.
2. Yang, L.; Yuan, X.; Yang, X. Study of the influencing mechanism of user interaction behavior of short video e-commerce
live-streaming from the perspective of SOR theory and interactive ritual chains. Curr. Psychol. 2024, 43, 28403–28415.
3. Fan, J.; Peng, L.; Chen, T.; Cong, G. Regulation strategy for behavioral integrity of live streamers: From the perspective of the
platform based on evolutionary game in China. Electron. Mark. 2024, 34, 21.
4. Chen, X.; Ji, L.; Jiang, L.; Huang, J.T. The bright side of emotional extremity: Evidence from tipping in live streaming platform.
Inf. Manag. 2023, 60, 103726.
5. Wang, Y.; Liu, J.; Fang, Y. Live streaming e-commerce: The impact of the intensity, duration, and phases of peak interaction on
sales performance. In Proceedings of the 14th China Summer Workshop on Information Management (CISWIM), Chongqing,
China, 26–28 June 2021; Volume 6.
6. Wu, Q.; Sang, Y.; Wang, D.; Lu, Z. Malicious selling strategies in livestream e-commerce: A case study of Alibaba’s Taobao and
ByteDance’s TikTok. Acm Trans. Comput.-Hum. Interact. 2023, 30, 1–29.
https://doi.org/10.3390/electronics15040769

Electronics 2026, 15, 769 25 of 27
7. Gan, T.; Yang, K.; Wang, W. Review of Machine Learning and False Advertising in Live E-commerce: Features, Motivations,
and Identification Studies. In International Conference on Computing and Communication Networks; Springer: Berlin/Heidelberg,
Germany, 2024; pp. 297–306.
8. Zhang, X.; Han, Y.; Xu, W.; Wang, Q. HOBA: A novel feature engineering methodology for credit card fraud detection with a
deep learning architecture. Inf. Sci. 2021, 557, 302–316.
9. Baesens, B.; Höppner, S.; Verdonck, T. Data engineering for fraud detection. Decis. Support Syst. 2021, 150, 113492.
10. Zhang, L.; Zhang, Y.; Ma, X. A new strategy for tuning ReLUs: Self-adaptive linear units (SALUs). In ICMLCA 2021, 2nd
International Conference on Machine Learning and Computer Application; VDE: Offenbach am Main, Germany, 2021; pp. 1–8.
11. Nyasala, U.S.; Lingannagari, N.R.; Kakarla, P .; Gujjala, U.K.; Neeruganti, S.H.V . Predictive analytics with machine learning for
fraud detection of online marketing transactions. In AIP Conference Proceedings; AIP Publishing LLC: Melville, NY, USA, 2025;
Volume 3237, p. 020029.
12. Li, Q.; Ren, J.; Zhang, Y.; Song, C.; Liao, Y.; Zhang, Y. Privacy-Preserving DNN Training with Prefetched Meta-Keys on
Heterogeneous Neural Network Accelerators. In 2023 60th ACM/IEEE Design Automation Conference (DAC); IEEE: New York, NY,
USA, 2023; pp. 1–6.
13. Olushola, A.; Mart, J. Fraud detection using machine learning. Sci. Prepr. 2024; pp. 1–17..
14. Wang, Y. Analysis of users’ impulse purchase behavior based on data mining for e-commerce live broadcast. In Electronic
Commerce Research; Springer: Berlin/Heidelberg, Germany, 2024; pp. 1–24.
15. Zhang, C.; Wang, Y.; Zhang, J. Identification and Evaluation of Key Risk Factors of Live Streaming e-Commerce Transactions
Based on Social Network Analysis. J. Theor. Appl. Electron. Commer. Res. 2025, 20, 169.
16. Malik, M. The Future of Modern Finance: AI-Driven Fraud Detection and Energy Market Forecasting; Springer: Berlin/Heidelberg,
Germany, 2025.
17. Kokab, S.T.; Asghar, S.; Naz, S. Transformer-based deep learning models for the sentiment analysis of social media data. Array
2022, 14, 100157.
18. Hasan, M.; Islam, L.; Jahan, I.; Meem, S.M.; Rahman, R.M. Natural language processing and sentiment analysis on bangla social
media comments on russia–ukraine war using transformers. Vietnam J. Comput. Sci. 2023, 10, 329–356.
19. Ayetiran, E.F.; Özgöbek, Ö. An inter-modal attention-based deep learning framework using unified modality for multimodal
fake news, hate speech and offensive language detection. Inf. Syst. 2024, 123, 102378.
20. Xiao, K.; Qian, Z.; Qin, B. A survey of data representation for multi-modality event detection and evolution. Appl. Sci. 2022,
12, 2204.
21. Li, Q.; Zhang, Y.; Ren, J.; Li, Q.; Zhang, Y. You can use but cannot recognize: Preserving visual privacy in deep neural networks.
arXiv 2024, arXiv:2404.04098.
22. Song, H.; Kim, M.; Park, D.; Shin, Y.; Lee, J.G. Learning from noisy labels with deep neural networks: A survey. IEEE Trans.
Neural Netw. Learn. Syst. 2022, 34, 8135–8153.
23. Chen, Y.; Zhou, J.; Chen, Y.; Chen, Z.; Hong, L.; Chen, G. Comment detection algorithm of e-commerce water army based on
BERT. In Proceedings of the 2024 International Conference on Smart City and Information System, Kuala Lumpur, Malaysia,
17–19 May 2024; pp. 597–603.
24. Khodabandehlou, S.; Golpayegani, A.H. FiFrauD: Unsupervised financial fraud detection in dynamic graph streams. Acm Trans.
Knowl. Discov. Data 2024, 18, 1–29.
25. Chen, T.; Tong, C.; Bai, Y.; Yang, J.; Cong, G.; Cong, T. Analysis of the public opinion evolution on the normative policies for the
live streaming e-commerce industry based on online comment mining under COVID-19 epidemic in China. Mathematics 2022,
10, 3387.
26. Shehnepoor, S.; Togneri, R.; Liu, W.; Bennamoun, M. HIN-RNN: A graph representation learning neural network for fraudster
group detection with no handcrafted features. IEEE Trans. Neural Netw. Learn. Syst. 2021, 34, 4153–4166.
27. Yu, J.; Wang, H.; Wang, X.; Li, Z.; Qin, L.; Zhang, W.; Liao, J.; Zhang, Y.; Yang, B. Temporal insights for group-based fraud
detection on e-commerce platforms. IEEE Trans. Knowl. Data Eng. 2024, 37, 951–965.
28. Li, Z.; Wang, H.; Zhang, P .; Hui, P .; Huang, J.; Liao, J.; Zhang, J.; Bu, J. Live-streaming fraud detection: A heterogeneous graph
neural network approach. In Proceedings of the 27th ACM SIGKDD Conference on Knowledge Discovery & Data Mining,
Singapore, 14–18 August 2021; pp. 3670–3678.
29. Li, W.; Fan, H.; Wong, Y.; Yang, Y.; Kankanhalli, M. Improving context understanding in multimodal large language models
via multimodal composition learning. In Proceedings of the Forty-First International Conference on Machine Learning, Vienna,
Austria, 21–27 July 2024.
30. Wan, Q.; Chen, J.; Yu, C.; Lu, M.; Liu, D. Optimal marketing strategies for live streaming rooms in livestream e-commerce.
Electron. Commer. Res. 2024, 25, 4655.
31. Xu, G.; Ren, M.; Wang, Z.; Li, G. MEMF: Multi-entity multimodal fusion framework for sales prediction in live streaming
commerce. Decis. Support Syst. 2024, 184, 114277.
https://doi.org/10.3390/electronics15040769

Electronics 2026, 15, 769 26 of 27
32. Porras, D.C.; Louwerse, M.M. Face to face: The eyes as an anchor in multimodal communication. Cognition 2025, 256, 106047.
33. Zhang, Q.; Li, X.; Gao, P . Forecasting Sales in Live-Streaming Cross-Border E-Commerce in the UK Using the Temporal Fusion
Transformer Model. J. Theor. Appl. Electron. Commer. Res. 2025, 20, 92.
34. Zhang, W.; Xie, R.; Quan, P .; Ma, Z. Product return prediction in live streaming e-commerce with cross-modal contrastive
transformer. Decis. Support Syst. 2025, 194, 114470.
35. Li, H.; Wang, R.; Shi, C. “Oh My God! Buy it!” Analysis on the Characteristics of Anchor’s Speech in Live Broadcast E-Commerce
and Purchase Intention: A Linguistic Perspective. Sage Open 2023, 13, 21582440231202126.
36. Luo, H.; Cheng, S.; Zhou, W.; Yu, S.; Lin, X. A study on the impact of linguistic persuasive styles on the sales volume of live
streaming products in social e-commerce environment. Mathematics 2021, 9, 1576.
37. Lin, W.; Li, C. Review of studies on emotion recognition and judgment based on physiological signals. Appl. Sci. 2023, 13, 2573.
38. Xiong, Y.; Wei, N.; Qiao, K.; Li, Z.; Li, Z. Exploring consumption intent in live e-commerce barrage: A text feature-based approach
using Bert-BiLSTM model. IEEE Access 2024, 12, 69288–69298.
39. Kwon, O.H.; Vu, K.; Bhargava, N.; Radaideh, M.I.; Cooper, J.; Joynt, V .; Radaideh, M.I. Sentiment analysis of the United States
public support of nuclear power on social media using large language models. Renew. Sustain. Energy Rev. 2024, 200, 114570.
40. Zhou, R.; Shen, Q.; Kong, H. A study of text classification algorithms for live-streaming e-commerce comments based on
improved BERT model. PLoS ONE 2025, 20, e0316550.
41. Cross-Modal Representation Learning: Joint and Distributed Embedding. Ph.D. Thesis, Seoul National University Graduate
School, Seoul, Republic of Korea, 2022.
42. Yuan, X.; Qi, A.; Wu, H.; Wang, J.; Guo, Y.; Li, S.; Zhao, L. Cross-modal feature alignment and fusion with contrastive learning in
multimodal recommendation. Knowl.-Based Syst. 2025, 326, 114020.
43. Popoola, N.T. Big data-driven financial fraud detection and anomaly detection systems for regulatory compliance and market
stability. Int. J. Comput. Appl. Technol. Res 2023, 12, 32–46.
44. Khodabandehlou, S.; Hashemi Golpayegani, S.A. How do abnormal trading behaviors diffuse in electronic markets? Soc. Netw.
Anal. Min. 2024, 14, 98.
45. Thundiyil, S.; Shalamzari, S.; Picone, J.; McKenzie, S. Transformers for modeling long-term dependencies in time series data: A
review. In 2023 IEEE Signal Processing in Medicine and Biology Symposium (SPMB); IEEE: New York, NY, USA, 2023; pp. 1–5.
46. Hamidi, H.H.; Haghi, B. An approach based on data mining and genetic algorithm to optimizing time series clustering for
efficient segmentation of customer behavior. Comput. Hum. Behav. Rep. 2024, 16, 100520.
47. Ren, L.; Hu, R.; Li, D.; Liu, Y.; Wu, J.; Zang, Y.; Hu, W. Dynamic graph neural network-based fraud detectors against collaborative
fraudsters. Knowl.-Based Syst. 2023, 278, 110888.
48. Wen, Z.; Fang, Y. Trend: Temporal event and node dynamics for graph representation learning. In Proceedings of the ACM Web
Conference 2022, Lyon France, 25–29 April 2022; pp. 1159–1169.
49. Walauskis, M.A.; Khoshgoftaar, T.M. Unsupervised label generation for severely imbalanced fraud data. J. Big Data 2025, 12, 63.
50. Njima, W.; Bazzi, A.; Chafii, M. DNN-based indoor localization under limited dataset using GANs and semi-supervised learning.
IEEE Access 2022, 10, 69896–69909.
51. Lee, J.D.; Lei, Q.; Saunshi, N.; Zhuo, J. Predicting what you already know helps: Provable self-supervised learning. Adv. Neural
Inf. Process. Syst. 2021, 34, 309–323.
52. Liu, X.; Zhang, F.; Hou, Z.; Mian, L.; Wang, Z.; Zhang, J.; Tang, J. Self-supervised learning: Generative or contrastive. IEEE Trans.
Knowl. Data Eng. 2021, 35, 857–876.
53. Liu, Y.; Li, Z.; Pan, S.; Gong, C.; Zhou, C.; Karypis, G. Anomaly detection on attributed networks via contrastive self-supervised
learning. IEEE Trans. Neural Netw. Learn. Syst. 2021, 33, 2378–2392.
54. Ghaleb, F.A.; Saeed, F.; Al-Sarem, M.; Qasem, S.N.; Al-Hadhrami, T. Ensemble synthesized minority oversampling-based
generative adversarial networks and random forest algorithm for credit card fraud detection. IEEE Access 2023, 11, 89694–89710.
55. Lin, L.; Li, Z.; Li, R.; Li, X.; Gao, J. Diffusion models for time-series applications: A survey. Front. Inf. Technol. Electron. Eng. 2024,
25, 19–41.
56. Gharoun, H.; Momenifar, F.; Chen, F.; Gandomi, A.H. Meta-learning approaches for few-shot learning: A survey of recent
advances. Acm Comput. Surv. 2024, 56, 1–41.
57. Jin, J.; Zhang, Y. The analysis of fraud detection in financial market under machine learning. Sci. Rep. 2025, 15, 29959.
58. Hochreiter, S.; Schmidhuber, J. Long short-term memory. Neural Comput. 1997, 9, 1735–1780.
59. Cho, K.; Van Merriënboer, B.; Bahdanau, D.; Bengio, Y. On the properties of neural machine translation: Encoder-decoder
approaches. arXiv 2014, arXiv:1409.1259.
60. Vaswani, A.; Shazeer, N.; Parmar, N.; Uszkoreit, J.; Jones, L.; Gomez, A.N.; Kaiser, Ł.; Polosukhin, I. Attention is all you need. In
Advances in Neural Information Processing Systems; NeurIPS Proceedings: San Diego, CA, USA, 2017; Volume 30.
https://doi.org/10.3390/electronics15040769

Electronics 2026, 15, 769 27 of 27
61. Liu, Z.; Dou, Y.; Yu, P .S.; Deng, Y.; Peng, H. Alleviating the inconsistency problem of applying graph neural network to fraud
detection. In Proceedings of the 43rd International ACM SIGIR Conference on Research and Development in Information
Retrieval, Xi’an, China, 25–30 July 2020; pp. 1569–1572.
62. Kiela, D.; Bhooshan, S.; Firooz, H.; Perez, E.; Testuggine, D. Supervised multimodal bitransformers for classifying images and
text. arXiv 2019, arXiv:1909.02950.
63. Radford, A.; Kim, J.W.; Hallacy, C.; Ramesh, A.; Goh, G.; Agarwal, S.; Sastry, G.; Askell, A.; Mishkin, P .; Clark, J.; et al. Learning
transferable visual models from natural language supervision. In International Conference on Machine Learning; PMLR: Cambridge
MA, USA, 2021; pp. 8748–8763.
64. Liu, F.T.; Ting, K.M.; Zhou, Z.H. Isolation forest. In 2008 Eighth IEEE International Conference on Data Mining; IEEE: New York, NY,
USA, 2008; pp. 413–422.
65. Schölkopf, B.; Platt, J.C.; Shawe-Taylor, J.; Smola, A.J.; Williamson, R.C. Estimating the support of a high-dimensional distribution.
Neural Comput. 2001, 13, 1443–1471.
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.
https://doi.org/10.3390/electronics15040769
